# Phase 2: Bill of Materials and Sourcing Matrix

Costs are rough USD estimates for single quantities and will have moved; get
current quotes before budgeting. Part numbers are options that fit the
architecture in [Phase 1](01-architecture.md), not tested selections. Where two
options are listed, the first is the recommendation.

## 1. Autopilot, IMU and navigation

| Subsystem | Component Description | Specific Part/Model Options | Interface/Protocol | Est. Cost | Vendor / Source Type |
|---|---|---|---|---|---|
| Autopilot | Flight controller, triple IMU, isolated and heated | CubePilot Cube Orange+ with ADS-B or Kore carrier; spare: Matek H743-Wing | DroneCAN ×2, UART, PWM, USB | $350–500 | CubePilot resellers, drone distributors |
| Autopilot | Redundant 5 V supply for controller | 2 × Mauch or CubePilot power brick | Analog V/I sense | $40–100 | Drone distributors |
| Navigation | Dual-antenna RTK GNSS for position and heading | 2 × CubePilot Here4, or Holybro H-RTK F9P pair, or Septentrio mosaic-H | DroneCAN / UART | $500–1,500 | Drone distributors, Septentrio direct |
| Navigation | RTK corrections | NTRIP subscription over LTE, or own base (Here4 Base / F9P) | NTRIP / RTCM3 | $0–600 | State CORS network, drone distributors |
| Navigation | External compass (fallback) | RM3100 DroneCAN magnetometer | DroneCAN | $60–120 | Drone distributors |
| Navigation | Depth sounder | Blue Robotics Ping2; or Airmar DST810 (depth/speed/temp) | UART (Ping protocol) / NMEA 2000 | $400–600 | Blue Robotics direct, marine electronics dealers |
| Companion | Onboard computer | Raspberry Pi 5 8 GB with NVMe, running BlueOS; or Jetson Orin Nano for onboard vision | Ethernet, USB, UART | $150–600 | Electronics distributors |
| Manual control | RC link for launch and recovery | RadioMaster handset with ELRS receiver | CRSF | $150–300 | Hobby RC retailers |

## 2. Mechanical steering and actuation

| Subsystem | Component Description | Specific Part/Model Options | Interface/Protocol | Est. Cost | Vendor / Source Type |
|---|---|---|---|---|---|
| Steering | Servo-grade linear actuator, about 1,000 N dynamic, ≥ 80 mm/s, 100 mm stroke, IP67, absolute feedback | Ultra Motion Servo Cylinder (A-series); or Kar-Tech / Thomson Electrak HD with CAN (check speed) | CAN / RS-422 / PWM; 12–36 V | $1,500–4,000 | Manufacturer direct |
| Steering | Rotary alternative on the stem | Volz DA 58-D or Hitec industrial servo with reduction to 40–60 N·m | PWM / CAN / RS-485 | $1,500–3,500 | Manufacturer direct |
| Steering | Independent nozzle position sensor | Sealed Hall rotary sensor (Novotechnik RFC-4800 series, Piher PST-360) | 0.5–4.5 V analog or CAN | $80–250 | Industrial sensor distributors |
| Steering | Breakaway link / spring-centred overload coupling | Custom, or adjustable ball-detent overload link | Mechanical | $100–300 | Machine shop, power transmission suppliers |
| Steering | Rod ends, clevises, stem arm bracket | 316 stainless rod ends, custom laser-cut bracket | Mechanical | $100–250 | McMaster-Carr, local fabricator |
| Steering | Inline load cell for the sizing measurement | S-type 2 kN load cell with amplifier | Analog / USB | $100–250 | Test equipment suppliers |
| Mounting | Fasteners and backing plates | 316 stainless, nylon-insert nuts, marine sealant | Mechanical | $50–100 | Marine chandlery |

## 3. Electronics and vehicle interfacing

| Subsystem | Component Description | Specific Part/Model Options | Interface/Protocol | Est. Cost | Vendor / Source Type |
|---|---|---|---|---|---|
| VIU | Microcontroller with CAN and hardware watchdog | Teensy 4.1; or STM32 Nucleo / custom STM32G4 board | CAN, SPI, ADC, UART | $30–80 | Electronics distributors (PJRC, DigiKey, Mouser) |
| VIU | Dual 12-bit DAC with external reference (ratiometric to ECU 5 V) ×2 | Microchip MCP4922 | SPI | $5–10 | DigiKey, Mouser |
| VIU | Rail-to-rail output buffers | TI OPA2192 or similar precision RRIO op-amp | Analog | $5–15 | DigiKey, Mouser |
| VIU | Changeover signal relays, sealed, gold contact, DPDT (throttle, iBR) | Omron G6K / TE IM series | Coil via safety chain | $10–20 | DigiKey, Mouser |
| VIU | External watchdog supervisor | TI TPS3823 or similar | Discrete | $2–5 | DigiKey, Mouser |
| CAN | Isolated CAN transceiver for the listen-only tap | TI ISO1042 or ADI ADM3053 breakout (TX not connected) | CAN 2.0 | $10–30 | DigiKey, Mouser |
| CAN | Bench sniffer | PEAK PCAN-USB; or CANable 2.0 | USB, SocketCAN | $40–300 | PEAK, hobby electronics vendors |
| CAN | NMEA 2000 gateway for the companion | Waveshare isolated CAN HAT, or Actisense NGT-1 | NMEA 2000, 250 kbps | $30–250 | Electronics distributors, marine dealers |
| CAN | NMEA 2000 backbone starter kit | Tees, terminators, power tap | NMEA 2000 (DeviceNet micro-C) | $60–100 | Marine electronics dealers |
| Harness | T-harnesses for APS, iBR lever and diagnostic port | Matching OEM-family connectors (identify from the craft), tinned wire | Analog, CAN | $80–200 | Connector specialists, BRP dealer for pigtails |
| Diagnostics | Dealer-level tool for live data and fault codes | BRP BUDS2 with MPI-3 interface; or CanDooPro | CAN diagnostic | $400–1,000 | BRP dealer channel, aftermarket tool vendors |
| Documentation | Factory shop manual and wiring diagrams, 2019 RXP-X 300 | BRP publication | n/a | $50–120 | BRP dealer, BRP online manuals |
| Sensors | Bilge float switches ×2 | Water Witch 101 / Rule-A-Matic Plus | Switch contact | $60–100 | Marine chandlery |
| Sensors | Engine bay and box temperature / humidity | DS18B20 sealed probes, SHT31 | 1-Wire, I²C | $20–40 | Electronics distributors |

## 4. Telemetry and video transmission

| Subsystem | Component Description | Specific Part/Model Options | Interface/Protocol | Est. Cost | Vendor / Source Type |
|---|---|---|---|---|---|
| Cellular | Dual-SIM industrial router with bonding | Peplink MAX BR1 Pro 5G (SpeedFusion); budget: Teltonika RUTX50 / RUTX11 | Ethernet, LTE/5G, WireGuard | $300–1,100 | Networking distributors |
| Cellular | Data plans, two carriers | Business or IoT SIMs with static or CGNAT-tolerant VPN | LTE/5G | $40–120 per month | Carriers, IoT MVNOs |
| Cellular | Marine MIMO antenna | Poynting OMNI-402 / OMNI-496 | SMA, 2×2 or 4×4 MIMO | $150–350 | Antenna distributors |
| VPN | Relay endpoint | Small cloud VM running WireGuard, or Tailscale / ZeroTier | UDP | $5–10 per month | Cloud providers |
| Sub-GHz | MAVLink telemetry radio pair | RFD900x (900 MHz) or RFD868x (EU); LoRa option: mLRS-compatible modules | UART, MAVLink | $200–350 | RFDesign resellers, hobby vendors |
| Sub-GHz | Antennas | Marine 900 MHz omni on the craft; Yagi or patch on a tracker at the GCS | RP-SMA / N | $80–300 | Antenna distributors |
| Satellite | Iridium short-burst modem | Ground Control RockBLOCK 9603 | UART; MAVLink high-latency via Lua | $250–300 plus airtime | Ground Control direct |
| Satellite | Optional broadband | Starlink Mini with marine-suitable plan | Ethernet | $300–600 plus plan | Starlink direct |
| Video | Pilot camera, fixed, IP67, low latency | Axis M20/P14 bullet series; budget: Hikvision / Dahua IP67 mini bullet | Ethernet PoE, RTSP H.264 | $150–600 | Security camera distributors |
| Video | Side and aft cameras ×3 | Same family as above, wide lens | Ethernet PoE, RTSP | $300–1,200 | Security camera distributors |
| Video | Optional marine thermal pan-tilt | FLIR M232; budget: Sionyx Nightwave (fixed low-light) | Ethernet, RTSP | $1,500–3,500 | Marine electronics dealers |
| Video | PoE switch, hardened | Planet / Teltonika TSW industrial 5–8 port | Ethernet, 802.3af | $80–200 | Networking distributors |
| Video | Streaming server software | MediaMTX on the companion | RTSP in; WebRTC / SRT out | Free | Open source |
| GCS | Ground station | Rugged laptop or tablet with QGroundControl / Mission Planner, joystick | USB, Wi-Fi, LTE | $800–2,000 | Computer retailers |

## 5. Power, enclosures and safety

| Subsystem | Component Description | Specific Part/Model Options | Interface/Protocol | Est. Cost | Vendor / Source Type |
|---|---|---|---|---|---|
| Power | Isolated DC-DC charger, craft battery to avionics battery | Victron Orion-Tr Smart 12/12-18 Isolated | 12 V in / 12 V out | $150–250 | Marine electrical dealers |
| Power | Avionics battery | 12 V 20–30 Ah LiFePO4 with BMS, IP67 case | 12 V | $120–300 | Marine / battery suppliers |
| Power | Isolated 12→24 V for the actuator | Victron Orion-Tr 12/24-15 Isolated | 24 V, 360 W | $120–180 | Marine electrical dealers |
| Power | 12→5 V converters ×2 | Mean Well DDR-30 / RSD-30 series, or Traco isolated modules | 5 V | $40–100 | Electronics distributors |
| Power | Fuse block, breakers, battery switch | Blue Sea Systems ST Blade block, 285-series breakers, m-Series switch | 12 V | $100–180 | Marine chandlery |
| Power | Surge protection | TVS diodes (SMDJ series) at each box entry | Discrete | $10–20 | DigiKey, Mouser |
| Enclosure | Avionics box, IP67 / NEMA 4X, clear lid | Fibox ARCA / Polycase WQ / Integra | Mechanical | $80–200 | Enclosure distributors |
| Enclosure | Aft relay box, IP67 | Small die-cast aluminium, gasketed (Hammond 1550Z series) | Mechanical | $30–60 | Electronics distributors |
| Enclosure | Bulkhead connectors | Deutsch DT/DTM and Amphenol AT; M12 A- and X-coded panel mounts; Souriau UTS or MIL-DTL-38999 for multi-pin circulars | Power, CAN, Ethernet | $200–600 | Connector distributors |
| Enclosure | Vent and desiccant | Gore or Amphenol membrane vent, silica gel | Mechanical | $15–30 | Electronics distributors |
| Enclosure | Vibration isolators | Wire-rope isolators or Sorbothane mounts sized to box mass | Mechanical | $40–120 | McMaster-Carr, isolator manufacturers |
| Safety | Wireless e-stop, safety rated, dual output | FORT Robotics Wireless E-Stop Pro; budget, not safety rated: custom LoRa heartbeat pair with dual relay outputs | Dedicated RF; dry contacts | $2,500–5,000 (custom: $100–200) | Manufacturer direct |
| Safety | Onboard mushroom e-stop buttons ×2 | IP67 / IP69K twist-release, NC contacts | Switch contact | $40–100 | Industrial control distributors |
| Safety | Kill relays K1–K3, sealed, ignition protected | TE / Littelfuse sealed automotive relays in the aft box; or Blue Sea ML-series for high current | 12 V coil | $40–150 | Marine electrical dealers, DigiKey |
| Safety | Fuel vapour detector, marine | Fireboy-Xintex MB-1 or M-1 | Alarm relay contact | $200–350 | Marine safety dealers |
| Safety | Electric bilge pump | Rule 800 / Rule LoPro 900 | 12 V | $40–90 | Marine chandlery |
| Safety | Speed-limited key | Sea-Doo Learning Key, programmed to the craft | D.E.S.S. | $60–120 plus programming | BRP dealer |
| Safety | Fire suppression, automatic | Fireboy or Blazecut small-compartment unit | Mechanical / thermal | $150–400 | Marine safety dealers |
| Safety | Navigation light, all-round white, and high-visibility flag | USCG-approved LED all-round light on the mast | 12 V | $40–100 | Marine chandlery |

## Budget summary

| Section | Low | High |
|---|---|---|
| 1. Autopilot, IMU and navigation | $1,650 | $4,300 |
| 2. Mechanical steering and actuation (linear option; rotary alternative excluded) | $1,900 | $5,100 |
| 3. Electronics and vehicle interfacing | $800 | $2,300 |
| 4. Telemetry and video (hardware, excluding optional thermal and Starlink) | $2,300 | $6,400 |
| 5. Power, enclosures and safety | $1,600 | $8,400 |
| **Total** | **≈ $8,300** | **≈ $26,500** |

The low end assumes the custom e-stop, budget cameras and the Teltonika router;
the high end assumes the safety-rated e-stop, Axis cameras, Peplink bonding and
a Septentrio GNSS. Section totals are rounded sums of the row ranges above;
monthly service costs are not included.

## Order of purchase

1. Shop manual, BUDS2 or CanDooPro, CAN sniffer, load cell: these resolve the open items in Phase 1 section 6 and cost little.
2. Autopilot, GNSS, companion, VIU parts, 900 MHz radios: bench development.
3. E-stop, kill relays, vapour detector, bilge pump: fitted before any powered test.
4. Steering actuator: only after the cable force measurement.
5. Router, cameras, antennas, satellite modem.
