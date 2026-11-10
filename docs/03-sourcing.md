# Parts List: Price, Importance and Where to Buy

One row per part. This is the single list to order from; the [BOM](02-bom.md) gives the same parts in the Phase 2 subsystem format with their interfaces.

**Importance**

| Level | Meaning |
|---|---|
| Critical | The craft cannot be controlled or stopped safely without it. Fit before any powered test. |
| Required | Needed for the system to work as designed. |
| Recommended | Improves reliability or testing. Can be added later. |
| Optional | Useful extra. The design works without it. |

**Prices** are USD for one unit. Those marked *est.* are my estimates; the rest come from seller listings found by web search in November 2026 and were not re-checked. Links were found the same way and not all could be opened from the build environment. Within each group, parts are sorted by importance.

## Autopilot and navigation

| # | Part | What it does | Qty | Unit price | Line total | Importance | Where to buy |
|---|---|---|---|---|---|---|---|
| 1 | CubePilot Cube Orange+ Standard Set (HX4-06222) | Autopilot running ArduPilot Rover; includes carrier board and one power brick | 1 | $450 | $450 | Critical | [IR-LOCK](https://irlock.com/products/cube-orange-plus-standard-set) · [RobotShop](https://www.robotshop.com/products/cube-orange-standard-set) |
| 2 | CubePilot Here4 RTK GNSS | Position and GNSS heading from a bow and an aft antenna | 2 | $225–280 | $450–560 | Critical | [IR-LOCK](https://irlock.com/products/here4-multiband-rtk-gnss) · [GetFPV](https://www.getfpv.com/electronics/flight-controllers/cubepilot-here4-multiband-rtk-gnss-gps-module.html) |
| 3 | Raspberry Pi 5 (8 GB) with NVMe | Companion computer: BlueOS, video server, VPN, logging | 1 | $120–200 *est.* | $120–200 | Required | [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-5/) · [SparkFun](https://www.sparkfun.com/raspberry-pi-5-8gb.html) |
| 4 | Second power brick | Redundant 5 V feed to the Cube | 1 | $20–50 *est.* | $20–50 | Recommended | [IR-LOCK](https://irlock.com/) |
| 5 | Blue Robotics Ping2 echosounder | Depth under the hull | 1 | $450 *est.* | $450 | Recommended | [Blue Robotics](https://bluerobotics.com/store/sonars/echosounders/ping-sonar-r2-rp) |
| 6 | RadioMaster Boxer (ELRS) with RP3 receiver | Hand controller for launch and recovery | 1 | $150–300 *est.* | $150–300 | Recommended | [RadioMaster](https://www.radiomasterrc.com/collections/boxer-radio) |
| 7 | RTK corrections (NTRIP service or shore base) | Centimetre-level position; heading works without it | 1 | $0–600 *est.* | $0–600 | Optional | State or national CORS network |

## Steering and actuation

| # | Part | What it does | Qty | Unit price | Line total | Importance | Where to buy |
|---|---|---|---|---|---|---|---|
| 8 | Ultra Motion Servo Cylinder, AM series | Steering actuator. Order only after the cable force is measured | 1 | $1,500–4,000 *est.* | $1,500–4,000 | Critical | [Ultra Motion](https://www.ultramotion.com/servo-cylinder?series=am) |
| 9 | Breakaway link and stem bracket | Lets a rider overpower a seized actuator | 1 | $200–500 *est.* | $200–500 | Critical | Local machine shop · [McMaster-Carr](https://www.mcmaster.com/) |
| 10 | 316 stainless rod ends, clevises, fasteners | Linkage from actuator to steering stem arm | 1 | $100–250 *est.* | $100–250 | Critical | [McMaster-Carr](https://www.mcmaster.com/) |
| 11 | Novotechnik RFC-4800 rotary sensor | Independent nozzle angle feedback; catches a broken cable | 1 | $80–250 *est.* | $80–250 | Required | [Novotechnik](https://www.novotechnik.com/) |
| 12 | S-type load cell, 2 kN, with amplifier | One-off measurement that sizes the actuator | 1 | $100–250 *est.* | $100–250 | Required | [Omega](https://www.omega.com/) |

## Vehicle interface electronics

| # | Part | What it does | Qty | Unit price | Line total | Importance | Where to buy |
|---|---|---|---|---|---|---|---|
| 13 | Teensy 4.1 (one fitted, one spare) | Vehicle Interface Unit controller | 2 | $32 | $64 | Critical | [SparkFun](https://www.sparkfun.com/products/16771) |
| 14 | Microchip MCP4922 dual DAC | Emulates throttle and iBR lever sensor signals | 2 | $4–5 *est.* | $8–10 | Critical | [DigiKey](https://www.digikey.com/) |
| 15 | TI OPA2192 op-amp | Buffers the emulated sensor signals | 2 | $4–6 *est.* | $8–12 | Critical | [TI](https://www.ti.com/product/OPA2192) |
| 16 | Omron G6K-2 sealed signal relay (two fitted, two spare) | Fail-to-stock changeover for throttle and iBR | 4 | $4–6 *est.* | $16–24 | Critical | [DigiKey](https://www.digikey.com/) |
| 17 | TI TPS3823 watchdog | Drops the changeover relays if firmware stops | 1 | $2–3 *est.* | $2–3 | Critical | [TI](https://www.ti.com/product/TPS3823) |
| 18 | BRP shop manual and wiring diagrams | Pinouts, sensor voltages, fuse and relay layout | 1 | $50–120 *est.* | $50–120 | Critical | Authorised Sea-Doo dealer |
| 19 | TI ISO1042 isolated CAN transceiver | Listen-only tap on the craft CAN bus | 2 | $5–15 *est.* | $10–30 | Required | [TI](https://www.ti.com/product/ISO1042) |
| 20 | PEAK PCAN-USB | CAN sniffing during reverse-engineering | 1 | $235–300 | $235–300 | Required | [PEAK-System](https://peak-system.com/PCAN-USB.199.0.html?L=1) · [Grid Connect](https://gridconnect.com/products/can-usb-adapter-pcan-usb) |
| 21 | CanDooPro, Limited Home version | Live data and fault codes to decode CAN frames | 1 | $527 | $527 | Required | [SBT](https://sbt.com/products/can-doo-pro-limited-home-version-diagnostic-tool) |
| 22 | Deutsch DT/DTM connector kit and crimp tool | All harnesses and box connections | 1 | $80–200 *est.* | $80–200 | Required | [Prowire USA](https://www.prowireusa.com/c-19-deutsch-dt-connector-kits.html) |
| 23 | OEM-pattern pigtails (throttle, iBR lever, diagnostic port) | Plug-in T-harnesses, no cutting of the factory loom | 3 | $10–35 *est.* | $30–105 | Required | Sea-Doo dealer parts counter |
| 24 | Temperature and humidity sensors (3 × DS18B20, 1 × SHT31) | Engine bay and avionics box monitoring | 1 | $20–40 *est.* | $20–40 | Recommended | [SparkFun](https://www.sparkfun.com/) |
| 25 | Waveshare 2-CH isolated CAN HAT | NMEA 2000 port for the companion computer | 1 | $25–40 *est.* | $25–40 | Optional | [Waveshare](https://www.waveshare.com/product/2-ch-can-hat.htm) |
| 26 | NMEA 2000 starter kit | Backbone for marine instruments | 1 | $60–100 *est.* | $60–100 | Optional | [Defender](https://defender.com/) |

## Telemetry and video

| # | Part | What it does | Qty | Unit price | Line total | Importance | Where to buy |
|---|---|---|---|---|---|---|---|
| 27 | Peplink MAX BR1 Pro 5G | Primary data link, dual SIM with bonding | 1 | $1,000 *est.* | $1,000 | Required | [Peplink](https://www.peplink.com/products/max-br1-pro-5g) · [Westward Sales](https://westwardsales.com/peplink-br1-pro-5g) |
| 28 | Poynting OMNI-402-5G antenna | Marine cellular antenna on the mast | 1 | $409–450 | $409–450 | Required | [Poynting](https://poynting.tech/antennas/omni-402/) · [5Gstore](https://5gstore.com/product/14692_poynting_omni-402-5g_2x2_mimo_matine_lte5g_antenna) |
| 29 | RFDesign RFD900x-US bundle | Second, independent control and telemetry link | 1 | $220–380 | $220–380 | Required | [IR-LOCK](https://irlock.com/products/rfd900ux-us-modem-bundle-fcc) |
| 30 | Axis P1465-LE camera | Pilot camera | 1 | $600–900 *est.* | $600–900 | Required | [Axis](https://www.axis.com/products/axis-p1465-le) |
| 31 | Teltonika TSW101 PoE switch | Powers and connects the cameras | 1 | $90–200 | $90–200 | Required | [Teltonika](https://teltonika-networks.com/products/switches/tsw101) |
| 32 | Fixed IP67 PoE cameras (port, starboard, aft) | All-round view | 3 | $100–300 *est.* | $300–900 | Recommended | Security camera distributors |
| 33 | Ground Control RockBLOCK 9603 | Last-resort satellite position and status; airtime extra | 1 | $300 | $300 | Recommended | [Ground Control](https://www.groundcontrol.com/product/rockblock-9603/) |
| 34 | Starlink Mini | Broadband where there is no cellular cover; plan extra | 1 | $599 | $599 | Optional | [Starlink](https://www.starlink.com/) |
| 35 | FLIR M232 thermal camera | Night and thermal view | 1 | $2,795–3,095 | $2,795–3,095 | Optional | [FLIR](https://www.flir.com/products/m232/) · [Mealey Marine](https://mealeymarine.com/products/flir-m232-pan-tilt-9hz-marine-thermal-camera-e70354) |

## Safety

| # | Part | What it does | Qty | Unit price | Line total | Importance | Where to buy |
|---|---|---|---|---|---|---|---|
| 36 | Long-range wireless e-stop system (FORT 900 MHz or Cattron BWI Eagle) | Independent engine kill by radio. Price needs a quote | 1 | $2,500–5,000 *est.* | $2,500–5,000 | Critical | [FORT via Clearpath](https://store.clearpathrobotics.com/products/wireless-e-stop) · [BWI Eagle](https://www.bwieagle.com/products/wireless-e-stops/) |
| 37 | Sealed 12 V relays, 30–40 A (three fitted, one spare) | Kill relays K1–K3 | 4 | $10–40 *est.* | $40–160 | Critical | [Waytek](https://waytekwire.com/) |
| 38 | IP67 mushroom e-stop buttons | Local stop at the helm and rear deck | 2 | $20–50 *est.* | $40–100 | Critical | [McMaster-Carr](https://www.mcmaster.com/) |
| 39 | Fireboy-Xintex G-1B-R fume detector | Fuel vapour alarm in the closed hull | 1 | $200–350 *est.* | $200–350 | Critical | [Mealey Marine](https://mealeymarine.com/products/xintex-gasoline-fume-detector-alarm-w-plastic-sensor-black-bezel-display-g-1b-r) |
| 40 | Aft IP67 die-cast box | Houses the e-stop receiver and kill relays | 1 | $30–60 *est.* | $30–60 | Required | [DigiKey](https://www.digikey.com/) |
| 41 | Rule LoPro LP900S bilge pump | Automatic bilge pump | 1 | $87–118 | $87–118 | Required | [Defender](https://defender.com/en_us/rule-lopro-automatic-bilge-pump-lp900s) · [Mealey Marine](https://mealeymarine.com/products/rule-lopro-900gph-bilge-pump-automatic-lp900s) |
| 42 | Water Witch 101 bilge switch | High-water input to the kill chain | 1 | $48–55 | $48–55 | Required | [Defender](https://defender.com/en_us/water-witch-submersible-electronic-bilge-pump-switch-101) |
| 43 | All-round white LED light and flag | Visibility to other water users | 1 | $40–100 *est.* | $40–100 | Required | [West Marine](https://www.westmarine.com/) |
| 44 | Sea-Doo RF D.E.S.S. key (295100945), dealer-programmed as a Learning Key | Speed limit enforced by the ECU during testing; programming extra | 1 | $60–120 *est.* | $60–120 | Recommended | [BRP Sea-Doo shop](https://sea-doo-shop.brp.com/us/en/295100945-rf-d-e-s-s-key.html) |
| 45 | BlazeCut T-series fire suppression | Automatic engine bay fire suppression | 1 | $150–400 *est.* | $150–400 | Recommended | [BlazeCut](https://www.blazecut.com/) |

## Power and enclosures

| # | Part | What it does | Qty | Unit price | Line total | Importance | Where to buy |
|---|---|---|---|---|---|---|---|
| 46 | Victron Orion-Tr Smart 12/12-18A isolated charger | Charges the avionics battery, isolated from the craft | 1 | $160–270 | $160–270 | Required | [Mealey Marine](https://mealeymarine.com/products/victron-orion-tr-smart-12-12-18-18a-220w-isolated-dc-dc-charger-or-power-supply-ori121222120) · [Powerwerx](https://powerwerx.com/victron-ori121222120-oriontrsmart-18a-isolated) |
| 47 | Victron Orion-Tr 12/24-15A isolated converter | 24 V supply for the steering actuator | 1 | $200–240 | $200–240 | Required | [eMarine](https://emarineinc.com/products/victron-orion-tr-12-24-15a-360w-isolated-dc-dc-converter) |
| 48 | 12 V LiFePO4 battery, 20–30 Ah | Avionics battery | 1 | $120–300 *est.* | $120–300 | Required | Marine or battery suppliers |
| 49 | 12→5 V converters | Companion computer and the Cube's second feed | 2 | $20–50 *est.* | $40–100 | Required | [DigiKey](https://www.digikey.com/) |
| 50 | Blue Sea 5025 fuse block | One fuse per load | 1 | $40–60 *est.* | $40–60 | Required | [Blue Sea](https://www.bluesea.com/products/5025/ST_Blade_ATO_Fuse_Block_-_6_Circuits) · [Mealey Marine](https://mealeymarine.com/products/blue-sea-5025-st-blade-fuse-block-w-cover-6-circuit-w-negative-bus-5025) |
| 51 | Blue Sea 6006 battery switch | Isolates the avionics system | 1 | $30–45 *est.* | $30–45 | Required | [Mealey Marine](https://mealeymarine.com/products/blue-sea-6006200-battery-switch-mini-on-off-black-6006200) |
| 52 | Polycase WQ-series enclosure, clear cover | Sealed avionics box | 1 | $60–200 *est.* | $60–200 | Required | [Polycase](https://www.polycase.com/wq-series) |
| 53 | M12 panel connectors, cable glands, membrane vent | Box penetrations | 1 | $100–300 *est.* | $100–300 | Required | [DigiKey](https://www.digikey.com/) |
| 54 | Vibration isolators (set of four) | Mounts for the avionics box | 1 | $40–120 *est.* | $40–120 | Recommended | [McMaster-Carr](https://www.mcmaster.com/) |

## Cost by importance

| Importance | Parts | Low | High | Running total, low | Running total, high |
|---|---|---|---|---|---|
| Critical | 15 | $5,628 | $11,603 | $5,628 | $11,603 |
| Required | 25 | $4,456 | $6,640 | $10,084 | $18,243 |
| Recommended | 9 | $1,490 | $2,680 | $11,574 | $20,923 |
| Optional | 5 | $3,479 | $4,434 | $15,053 | $25,357 |

A working build is Critical plus Required: about $10,084 to $18,243. The wireless e-stop and the steering actuator are roughly 40 to 50 percent of that, and both need a supplier quote.

Not in the totals: two cellular SIM plans ($40–120 per month, est.), Iridium airtime, a Starlink plan, dealer key programming, and free software (ArduPilot, BlueOS, MediaMTX, QGroundControl).

## Alternatives (not counted above)

Swap one of these in for the listed part; do not buy both.

| Alternative | Replaces | Price | Where to buy |
|---|---|---|---|
| Holybro H-RTK F9P Rover | Here4 | $270–325 each | [Holybro](https://holybro.com/) |
| Septentrio mosaic-go H kit | Both Here4 units | €745 | [Septentrio](https://shop.septentrio.com/en/shop/mosaic-go-h-heading-gnss-module-evaluation-kit) |
| Airmar DST810 | Ping2 | $399–624 | [Defender](https://defender.com/en_us/airmar-dst810-smart-multisensor) |
| Thomson Electrak HD (CAN) | Ultra Motion actuator | $1,000–2,000 (est.) | [Thomson](https://www.thomsonlinear.com/en/product/HD12B026-1000CNO1MESD) |
| Actisense NGX-1 | Waveshare CAN HAT | $200–300 (est.) | [Actisense](https://actisense.com/) |
| Teltonika RUTX50 | Peplink router | $350–450 (est.) | [Teltonika](https://teltonika-networks.com/products/routers/rutx50) |
| mLRS LoRa radio pair | RFD900x | $60–150 (est.) | [mLRS](https://github.com/olliw42/mLRS) |
| Sionyx Nightwave | FLIR M232 | ≈ $1,895 | [Sionyx](https://www.sionyx.com/pages/nightwave-digital) |
| Custom LoRa heartbeat e-stop (not safety rated) | Commercial e-stop | $100–200 (est.) | Built from parts |
