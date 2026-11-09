# Phase 1: Systems Architecture and Technical Design

Items marked **(verify)** must be confirmed against the BRP shop manual for the
2019 RXP-X 300 and by measurement on the craft.

## 0. Architecture overview

```mermaid
flowchart LR
  subgraph Shore
    GCS[GCS: QGroundControl / Mission Planner]
    ESTX[E-stop transmitter]
    RC[RC handset]
  end
  subgraph Avionics box, front storage bin
    AP[Cube Orange+ / ArduPilot Rover]
    CC[Companion computer]
    RTR[LTE/5G router]
    R900[900 MHz MAVLink radio]
    SAT[Iridium SBD modem]
    VIU[Vehicle Interface Unit]
  end
  subgraph Safety chain, no software
    ESRX[E-stop receiver]
    KR[Kill relay chain]
  end
  subgraph Craft
    ECU[Bosch ME17.8.5]
    IBR[iBR module]
    STR[Steering actuator]
    BCAN[(BRP CAN)]
  end
  GCS <-- VPN --> RTR <--> CC <--> AP
  GCS <--> R900 <--> AP
  GCS <-. high latency .-> SAT <--> AP
  RC --> AP
  AP -- DroneCAN / PWM --> VIU
  AP -- CAN / PWM --> STR
  VIU -- dual APS analog --> ECU
  VIU -- lever analog --> IBR
  BCAN -- listen only --> VIU
  ESTX -. dedicated RF .-> ESRX --> KR
  KR -- cuts fuel + ignition feed --> ECU
  KR -- drops mux relays --> VIU
```

Three layers, in order of authority:

1. **Safety chain**: e-stop receiver, kill relays, physical buttons, lanyard. Relays and wire only.
2. **Vehicle Interface Unit (VIU)**: a small microcontroller board that translates autopilot commands into the signals the craft expects and enforces limits (throttle ceiling, slew rates, watchdog).
3. **Autonomy**: autopilot, companion computer, links, video.

A lower layer can always override a higher one; a higher layer can never override a lower one.

## 1. Autopilot and control surface interfacing

### 1.1 Autonomy core

| Choice | Recommendation |
|---|---|
| Firmware | **ArduPilot Rover, boat frame** (`FRAME_CLASS=2`). PX4's boat support is much less mature; use ArduPilot. |
| Controller | **Cube Orange+** on a carrier board with two CAN ports. Matek H743 is a workable low-cost spare but has no IMU vibration isolation or heating. |
| Companion | Raspberry Pi 5 or Jetson Orin Nano running BlueOS (MAVLink routing, video, VPN). The companion is never in the control loop for steering, throttle or stop. |
| Navigation | Dual-antenna RTK GNSS for heading (a magnetometer is unreliable next to the engine and steel hardware), plus one external compass as a fallback. |

Control mapping:

| Function | ArduPilot output | Goes to |
|---|---|---|
| Steering | `SERVO1_FUNCTION=26` (GroundSteering) | Steering actuator |
| Throttle, forward | `SERVO3_FUNCTION=70` (Throttle), positive half | VIU → APS emulation |
| Reverse / brake | Throttle, negative half | VIU → iBR lever emulation |
| Engine start/stop request | Relay output | VIU (request only; the safety chain can always veto) |

Parameters to set from day one:

- `MOT_THR_MAX`: start at 15–20 %. The craft planes at a small fraction of full throttle.
- `MOT_SLEWRATE`: limit throttle rate so the hull does not launch or stuff the bow.
- `MOT_VEC_ANGLEMAX`: vectored-thrust steering, so steering gain scales with throttle.
- `CRUISE_SPEED` / `CRUISE_THROTTLE`, `WP_SPEED`: conservative.
- `FENCE_ENABLE=1` with a polygon fence and `FENCE_ACTION` = hold.
- `FS_ACTION`, `FS_GCS_ENABLE`, `FS_THR_ENABLE`, `FS_TIMEOUT`: on loss of control link, hold (idle + neutral). The engine kill on prolonged loss is done by the safety chain, not by ArduPilot.

Second governor: program a Sea-Doo **Learning Key** and use it for all early testing. The ECU then limits speed itself, independent of anything in this project **(verify the limit options in BUDS2)**.

### 1.2 Steering actuation

The stock system is a push-pull cable from the steering stem to the nozzle. Two places to actuate:

| Option | For | Against |
|---|---|---|
| **A. Linear actuator on the stem arm, cable left intact** (recommended) | Dry, cool location under the helm cover; cable and nozzle untouched; handlebars still move, so a rider can see and overpower it through a clutch or breakaway link | Must back-drive or declutch for manual riding |
| B. Linear actuator on the cable at the stern | Shortest load path | Hot, wet, cramped; hardest to service; replaces the cable end |
| C. Rotary servo on the steering stem | Compact | Needs 30–60 N·m continuous at the stem; few IP67 servos reach it without a gearbox |

**Force estimate** (to be replaced by a measurement):

| Quantity | Assumption | Value |
|---|---|---|
| Peak thrust T | 300 hp jet pump, static | ≈ 4.2 kN (≈ 950 lbf) **(verify)** |
| Nozzle deflection δ | each side of centre | ≈ 20° **(verify)** |
| Side force on hull | T·sin δ | ≈ 1.4 kN (taken by the nozzle pivots, not the cable) |
| Hinge moment | side force × centre-of-pressure offset from pivot axis, 15–25 mm | ≈ 20–35 N·m |
| Nozzle steering arm | | ≈ 65 mm **(verify)** |
| Cable force from flow | hinge moment ÷ arm | ≈ 300–550 N |
| Cable friction | aged cable, bends | ≈ 50 N |
| **Design load** | peak ≈ 600 N × 1.7 margin | **≈ 1,000 N (225 lbf) dynamic** |

**Throw and speed:**

| Spec | Target |
|---|---|
| Stroke | Cable travel is about ±40 mm **(verify)**; specify a 100 mm actuator and limit travel in software to 2–3 mm inside the mechanical stops so the actuator never drives into the nozzle stops |
| Speed | Lock to lock in ≤ 1 s, so ≥ 80 mm/s under load |
| Mechanical power | 1,000 N × 0.08 m/s ≈ 80 W peak; allow 15–20 A at 24 V |
| Duty | Continuous small corrections; needs a servo-grade actuator, not a trim or hatch actuator |

Before ordering, measure the real cable force with an inline load cell while a rider does full-throttle turns. This one measurement sizes the actuator.

**Anti-jam measures:**

- Soft limits in the actuator drive, plus current limit set just above the design load.
- A spring-centred breakaway link or shear pin between actuator and stem arm, rated above the design load, so a seized actuator cannot lock the nozzle against a rider.
- Actuator loss of power: the nozzle stays where it is. The safety chain response to a steering fault is throttle to idle.

**Feedback redundancy:**

1. Actuator's internal absolute position sensor (closes the position loop).
2. Independent sensor on the **nozzle** itself (sealed Hall rotary or linear sensor), read by the VIU. This catches a broken cable or linkage, which the actuator's own sensor cannot see.
3. VIU compares the two; disagreement above a threshold for more than 200 ms → throttle to idle, alert to GCS.

### 1.3 Throttle integration (iTC)

The throttle lever carries a dual-track Hall accelerator position sensor (APS). The ECU supplies 5 V, reads both tracks, and checks that they agree; a mismatch puts the engine in limp-home. Track voltages and ratio must be measured **(verify; many Bosch systems use a second track at half the first)**.

Method: **emulate the sensor, switch at the harness, default to stock.**

```
Stock APS ──┐
            ├─ NC ─┐
            │      ├──► ECU APS inputs (track 1, track 2)
VIU DACs ───┴─ NO ─┘
   changeover relay, coil powered through the safety chain
```

- A two-channel 12-bit DAC with an **external reference pin**, referenced to the ECU's own 5 V sensor supply, so the emulated signals are ratiometric exactly like the real sensor.
- Rail-to-rail buffer on each channel, with output impedance matched to the stock sensor and series resistors so a VIU fault cannot drive the ECU inputs outside their valid range.
- A double-pole signal relay (gold contacts, sealed) switches both tracks together. **Normally closed = stock lever.** With the relay de-energised, the ECU sees the real, spring-returned lever: idle.
- The relay coil is fed through the safety chain and through the VIU's hardware watchdog. E-stop, VIU hang, or avionics power loss all return the throttle to the stock lever.
- Transfer only when both stock and emulated signals are at idle, so the ECU never sees a step or a track mismatch.
- The VIU reads its own outputs back with an ADC and drops the relay if either track is more than a few percent from the commanded value.
- Firmware clamps: absolute throttle ceiling, slew rate, and zero throttle whenever iBR is not in forward.

Use a T-harness with the same connector family as the stock sensor so the factory loom is never cut and the craft returns to stock by unplugging.

### 1.4 Reverse and braking (iBR)

| Method | Assessment |
|---|---|
| CAN spoofing of iBR commands | BRP's messages are proprietary and unpublished. Two nodes sending the same ID collide, so the real sender would have to be cut out and gatewayed. High effort, high chance of fault codes. Not recommended. |
| Direct H-bridge drive of the gate motor | Bypasses the iBR module's position control, end-stop logic and the interlocks that limit reverse and braking by speed and RPM. A gate dropped at speed is violent. Not recommended. |
| **Emulate the iBR lever sensor** (recommended) | The left-hand lever is a Hall sensor, like the throttle. Inject an analog signal through the same NC changeover relay arrangement as 1.3. The iBR module keeps all its own logic and protections. |

**(verify)** in the wiring diagram: which module reads the iBR lever, the number of tracks, and the voltage range.

The VIU maps the negative half of ArduPilot's throttle to iBR lever position, with the forward throttle held at idle. Forward/neutral/reverse state is confirmed from the CAN bus (section 2.1) once decoded; until then, by timers.

### 1.5 Safety and kill-switch architecture

A single series loop holds the craft alive. Any opening stops the engine. No microcontroller sits in the loop.

```
+12 V ─ fuse ─ onboard mushroom button(s) ─ e-stop receiver contacts (2 in series)
      ─ bilge high-high float ─ fuel vapour alarm contact ─► kill relay coils K1, K2
```

| Relay | Opens | Effect |
|---|---|---|
| K1 | Fused feed to injectors and ignition coils | Engine stops immediately, independent of the ECU |
| K2 | Fuel pump feed | Backup stop within seconds |
| K3 | Mux relay coil supply (throttle and iBR) | Controls revert to stock levers |

- **Normally energised to run.** Lost power, a broken wire, or a flat e-stop battery all stop the engine.
- The **e-stop radio is its own link** with its own antenna and frequency, sharing nothing with telemetry. The receiver opens its contacts on a button press or on loss of the transmitter heartbeat (1–2 s). Its range therefore defines the operating area.
- A safety-rated commercial unit with dual redundant outputs (for example FORT Robotics) is the recommended choice. A home-built LoRa heartbeat receiver driving the same relays is cheaper but is not safety rated; if used, give it two independent output stages.
- **D.E.S.S.:** do not try to simulate the key. Keep a programmed key on the post so the ECU's own security stays satisfied, and keep the lanyard so anyone aboard can pull it. The hardware kill sits downstream of all that.
- Relays K1/K2 switch inductive loads in a fuel-vapour space: use sealed, ignition-protected relays or mount them in the sealed avionics box.
- Cutting coil and injector feed while the ECU is powered may log fault codes; clear them with BUDS2 during commissioning and record which ones are expected.

Stop levels:

| Level | Trigger | Action | Done by |
|---|---|---|---|
| 0 Hold | Link loss, fence breach, GCS command | Idle, iBR neutral | ArduPilot |
| 1 Revert | VIU watchdog, signal readback fault, steering disagreement | Mux relays drop to stock levers (idle) | VIU hardware watchdog |
| 2 Kill | E-stop button, e-stop heartbeat loss, vapour alarm, bilge high-high | K1 + K2 open | Safety chain |

## 2. Telemetry, engine health and CAN logging

### 2.1 BRP CAN extraction

- Tap at the diagnostic connector with a T-harness. Expect 11-bit IDs at **500 kbps (verify; confirm with a scope or auto-baud sniffer)**.
- The tap is **listen-only**: isolated transceiver with the TX line physically disconnected, so the project cannot disturb the bus.
- The message set is proprietary. No CAN IDs are given here because none can be stated with confidence. Decode procedure:
  1. Log raw frames (`candump`) on the trailer with a flush hose, then on the water with a rider.
  2. Log BUDS2 live data at the same time and correlate: RPM, throttle, coolant temperature, intake air temperature, manifold pressure, oil pressure, battery voltage, iBR position.
  3. Record the results in a DBC file kept in this repository.
- Fault codes: read passively if the cluster broadcasts are decodable. Otherwise query the ECU with UDS/KWP diagnostic requests, which needs a transmitting node; do that only at idle or engine off, from a separate enabled-by-jumper path.

Getting the data to the ground station:

| Target | Route |
|---|---|
| MAVLink | Cube CAN2 set to scripting (`CAN_D2_PROTOCOL=10`), a Lua script decodes BRP frames into ArduPilot's EFI backend (`EFI_TYPE=7`). The GCS then shows RPM, temperatures, pressures and voltage as standard `EFI_STATUS` data. Alternatively the VIU decodes and sends the same over DroneCAN. |
| NMEA 2000 | Separate 250 kbps backbone. The companion (SignalK with a CAN HAT) publishes PGN 127488 (engine rapid) and 127489 (engine dynamic). The two buses are never joined electrically. |
| Logging | Companion stores raw CAN alongside the ArduPilot dataflash log, time-synced by GNSS. |

Alarms raised by the VIU regardless of link state: coolant over-temperature, low oil pressure and over-rev each force throttle to idle.

### 2.2 Long-range datalink

| Bearer | Role | Hardware | Notes |
|---|---|---|---|
| LTE/5G | Primary: telemetry and video | Dual-SIM industrial router, two carriers | WireGuard tunnel to a small cloud relay or direct to the GCS; MAVLink over UDP |
| 900 MHz (868 MHz in EU) | Independent telemetry and control, no infrastructure | RFD900x-class radio, or a LoRa MAVLink link (mLRS) for more range at lower rate | Line of sight over water; mount the antenna high. RFD900 is FHSS, not LoRa |
| Iridium SBD | Last resort: position and status every 30–60 s, simple commands | RockBLOCK 9603 with ArduPilot's RockBlock Lua script (MAVLink high-latency mode) | Not a piloting link |
| RC handset | Close-range manual control for launch and recovery | ELRS or similar, direct to the Cube | |

`mavlink-router` on the companion multiplexes the LTE path. The 900 MHz radio and the Iridium modem connect straight to Cube serial ports so they survive a companion crash.

### 2.3 In-hull environmental sensing

| Sensor | Location | Action |
|---|---|---|
| Bilge float, low | Lowest point aft | Runs an added electric bilge pump directly through its own switch (the stock craft relies on siphon bailers); state reported to the VIU |
| Bilge float, high-high | 50–75 mm above | In the safety chain: kill, and alarm |
| Fuel vapour detector, marine type | Sensor low in the engine bay, away from spray | Alarm contact in the safety chain; also inhibits start |
| Engine bay temperature ×2 | Near exhaust and near avionics | Telemetry and alarm |
| Avionics box temperature and humidity | Inside the box | Telemetry |
| Pump current sense | Bilge pump feed | Detects a running-dry or jammed pump |

The bilge pump and its float switch are wired to the battery through a fuse, independent of every computer on board.

## 3. Video telemetry and perception

| Element | Recommendation |
|---|---|
| Pilot camera | One fixed, wide (100–120°), low-latency IP67 camera on a short mast, H.264 hardware-encoded. Fixed cameras survive PWC slamming better than gimbals. |
| Situational awareness | Three more fixed cameras (port, starboard, aft) give near-360° cover with no moving parts. This is preferred over a single 360° camera, which is hard to stream at low latency. |
| Thermal / zoom | Optional single marine thermal pan-tilt unit for night work and target inspection. It adds weight high up; fit it after the basics work. |
| Encoding | 720p30 H.264 at 2–4 Mbps for piloting (H.264 decodes faster than H.265 on most GCS hardware); other cameras at 1 Mbps or on demand. |
| Server | MediaMTX on the companion takes RTSP from the cameras and republishes. |
| Transport | **WebRTC** for the pilot view (lowest latency, handles NAT through the VPN). **SRT** for recording-quality feeds and for bonded links, since it tolerates loss. Raw RTSP only on the local network. |
| Bonding | A bonding router (Peplink SpeedFusion or similar) across two carriers for video; MAVLink also has the 900 MHz path so it does not depend on bonding. |

Expect 150–300 ms glass-to-glass over LTE. At 30 mph that is 2–4 m of travel before the pilot sees anything, so remote FPV piloting is limited to modest speeds; higher speeds are for supervised waypoint runs in clear water.

Overlay speed, heading, RPM and link quality on the pilot view in the GCS rather than burning it into the video.

## 4. Power distribution and environmental protection

### 4.1 Power

```
Craft battery (12 V, magneto charged)
  └─ fuse ─ isolation switch ─ isolated DC-DC charger ─► Avionics LiFePO4 12 V, 20–30 Ah
                                                          ├─ isolated 12→24 V  ─► steering actuator
                                                          ├─ 12 V filtered     ─► router, cameras, radios
                                                          └─ 12→5 V ×2         ─► Cube (dual redundant), companion
```

- A separate avionics battery behind an **isolated** DC-DC charger keeps starter-motor dips, load dumps and ignition noise away from the electronics, and keeps telemetry and bilge alarms alive with the engine off.
- The magneto's spare output is limited. Total the avionics load (roughly 60–90 W average, 400 W actuator peaks buffered by the battery) and confirm against the charging output in the shop manual **(verify)**.
- The Cube gets two independent 5 V supplies on its two power inputs.
- Single-point ground for avionics; signal interfaces to the craft (CAN tap, APS, iBR) are galvanically isolated or referenced only to the ECU's sensor ground, never both.
- TVS diode and fuse at every entry to the avionics box.

### 4.2 Enclosures and environment

| Topic | Design |
|---|---|
| Location | Avionics box in the **front storage bin**, not the engine bay: cooler, drier, less vibration. Only the kill relays, sensors and actuator live aft. |
| Enclosure | NEMA 4X / IP67 polycarbonate or cast aluminium with a clear lid for status LEDs; pressure-equalising membrane vent; desiccant pack. |
| Connectors | Deutsch DT/DTM or Amphenol AT for power and discrete signals (same family as marine and powersports looms), M12 A-coded for CAN and Ethernet (X-coded), Souriau UTS or MIL-DTL-38999 where a true bulkhead circular is wanted. All penetrations on the box underside or sides, with drip loops. |
| Thermal | 30–40 W dissipated inside a sealed box: mount the router, companion and DC-DC converters on an aluminium plate bonded to the enclosure wall; no fans through the wall. Derate everything to 70 °C ambient. |
| Vibration | Box on wire-rope or elastomer isolators tuned well below engine firing frequency; the Cube already isolates its IMUs internally, so mount it rigidly to the plate. Strain-relieve every cable within 100 mm of its connector; use locking connectors only. |
| Corrosion | 316 stainless hardware, tinned marine wire, adhesive-lined heat shrink, dielectric grease on connector seals, conformal coat on the VIU board. |
| Ignition protection | Anything aft of the bulkhead that can arc is SAE J1171 / ISO 8846 rated or inside a sealed enclosure. |
| Antennas | GNSS pair on a rigid bar with at least 0.5 m baseline; LTE, 900 MHz and e-stop antennas on a short folding mast, separated from each other; Iridium patch with clear sky view. |

## 5. Commissioning sequence

1. Bench: VIU with a simulated ECU load; verify ratiometric outputs, readback trip, watchdog, relay defaults.
2. Trailer, engine off: T-harnesses in, verify stock operation is unchanged with the VIU unpowered.
3. Trailer, engine on flush hose: transfer to emulated throttle at idle only; test every stop level; log CAN.
4. Tethered in the water: steering and iBR under thrust at low throttle; measure cable force.
5. Open water with a rider aboard holding the lanyard: `MOT_THR_MAX` at 15 %, Learning Key in, chase boat present.
6. Unmanned, inside the e-stop radio's proven range, raising limits in small steps.

## 6. Open items to verify

| # | Item | How |
|---|---|---|
| 1 | APS track voltages, ratio, connector pinout | Shop manual, then measure |
| 2 | iBR lever sensor: reading module, tracks, range | Wiring diagram, then measure |
| 3 | CAN bit rate and message set | Sniff and correlate with BUDS2 |
| 4 | Steering cable travel and peak force | Measure with a load cell |
| 5 | Which fused feed supplies coils, injectors and fuel pump | Wiring diagram |
| 6 | Charging system spare capacity | Shop manual |
| 7 | Local rules for unmanned operation and radio licensing on the chosen bands | Maritime and spectrum authorities for the operating area |
