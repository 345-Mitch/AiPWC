# Parts Summary and Where to Buy

Companion to the [bill of materials](02-bom.md). Each table lists the part, what
it does in this build, quantity, an indicative price, and where to get it.

**How far to trust this page**

- Links were found by web search on 2026-11-09. They could not be opened from the build environment, so none has been click-tested; stock and prices were not checked beyond what the search results showed.
- Prices are from those search results where one was shown, otherwise they are estimates. Marked **(est.)** when estimated.
- Parts with no specific model (relays, sensors, wire, hardware) link to a distributor's front page; search the part number there.
- Sellers are mostly US. The same part numbers are available from regional distributors.

## 1. Autopilot, navigation and computing

| Part | Role in the build | Qty | Indicative price | Where to buy |
|---|---|---|---|---|
| CubePilot Cube Orange+ Standard Set (HX4-06222) | Autopilot running ArduPilot Rover. Set includes the ADS-B carrier board and one power brick. | 1 | ≈ $450 | [RobotShop](https://www.robotshop.com/products/cube-orange-standard-set) · [3DXR (UK)](https://www.3dxr.co.uk/products/cubepilot-the-cube-orange-standard-set-with-ads-b-carrier-board-hx4-06222) · [IR-LOCK](https://irlock.com/) |
| Second power brick | Redundant 5 V supply to the Cube's second power input | 1 | $20–50 (est.) | [IR-LOCK](https://irlock.com/) · [GetFPV](https://www.getfpv.com/) |
| CubePilot Here4 RTK GNSS | Two units on a rigid bar give position and GNSS heading (moving-baseline), so the compass is only a fallback | 2 | $225–280 each | [IR-LOCK](https://irlock.com/products/here4-multiband-rtk-gnss) · [RobotShop](https://www.robotshop.com/products/here-4-multiband-rtk-gnss) · [GetFPV](https://www.getfpv.com/electronics/flight-controllers/cubepilot-here4-multiband-rtk-gnss-gps-module.html) |
| Alternative: Holybro H-RTK F9P Rover (IP66, RM3100 compass) | Same role as Here4, weather-sealed housing and a better magnetometer | 2 | ≈ $270–325 each | [Holybro docs](https://docs.holybro.com/gps-and-rtk-system/h-rtk-neo-f9p-series-rm3100-compass/overview) · [Holybro](https://holybro.com/) |
| Alternative: Septentrio mosaic-go H heading kit | Single dual-antenna receiver with strong interference rejection; higher cost | 1 | €745 (kit), €1,495 (dev kit with two antennas) | [Septentrio shop](https://shop.septentrio.com/en/shop/mosaic-go-h-heading-gnss-module-evaluation-kit) · [dev kit](https://shop.septentrio.com/en/shop/mosaic-h-gnss-heading-module-evaluation-kit-2-gnss-antennae) |
| RTK corrections | NTRIP service over LTE, or a second F9P as a shore base | 1 | $0–600 (est.) | State or national CORS network; base receiver from the GNSS sellers above |
| Blue Robotics Ping2 echosounder | Depth under the hull, 100 m range, TTL serial into the Cube or BlueOS. 5 V TTL only: never connect to RS-232/RS-485 | 1 | ≈ $450 (est.) | [Blue Robotics](https://bluerobotics.com/store/sonars/echosounders/ping-sonar-r2-rp) · [RobotShop](https://robotshop.com/products/bluerobotics-ping2-sonar-altimeter-echosounder) |
| Alternative: Airmar DST810 | Depth, speed through water and temperature on NMEA 2000; needs a through-hull fitting | 1 | $399–624 | [Defender](https://defender.com/en_us/airmar-dst810-smart-multisensor) |
| Raspberry Pi 5 (8 GB) with NVMe | Companion computer running BlueOS: MAVLink routing, video server, VPN, logging | 1 | $120–200 (est.) | [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-5/) · [PiShop.us](https://www.pishop.us/) |
| BlueOS | Companion operating system | n/a | Free | [Blue Robotics](https://bluerobotics.com/) |
| RadioMaster Boxer (ELRS) and RP3 receiver | Hand controller for close-range manual driving at launch and recovery | 1 + 1 | $150–300 (est.) | [RadioMaster](https://www.radiomasterrc.com/collections/boxer-radio) · [GetFPV](https://www.getfpv.com/drone-brands/radiomaster/radiomaster-boxer-radio-transmitter-4-in-1-multi-protocol-cc2500-elrs-2-ghz.html) |

## 2. Steering and actuation

Do not order the actuator until the steering cable force has been measured (Phase 1, section 1.2).

| Part | Role in the build | Qty | Indicative price | Where to buy |
|---|---|---|---|---|
| Ultra Motion Servo Cylinder, **AM series** | Steering actuator. Brushless, built-in controller and absolute position sensor, 8–36 V, IP65 moving / IP67 static. Specify force, speed and 100 mm stroke with the factory. | 1 | $1,500–4,000 (est.; quote) | [Ultra Motion, AM series](https://www.ultramotion.com/servo-cylinder?series=am) · [all actuators](https://www.ultramotion.com/linear-actuators/) |
| Alternative: Thomson Electrak HD (CAN J1939 or CANopen) | Heavier and usually slower, but IP66 moving / IP67 and IP69K static and widely stocked. Check speed at load against the 80 mm/s target. | 1 | $1,000–2,000 (est.) | [Thomson example part page](https://www.thomsonlinear.com/en/product/HD12B026-1000CNO1MESD) · [MRO Supply](https://www.mrosupply.com/) |
| Novotechnik RFC-4800 touchless rotary sensor | Independent nozzle angle feedback. Magnet on the nozzle pivot, sensor up to IP69K; analog, redundant analog or CAN versions. | 1 | $80–250 (est.) | [Novotechnik](https://www.novotechnik.com/) · [datasheet (CAN J1939)](https://www.novotechnik.com/resources/manuals/40_DS_491_RFC-4800_CAN_J1939_12_24V--enUS.pdf) |
| S-type load cell, 2 kN, with amplifier | One-off measurement of real steering cable force | 1 | $100–250 (est.) | [Omega](https://www.omega.com/) · [McMaster-Carr](https://www.mcmaster.com/) |
| 316 stainless rod ends, clevises, fasteners | Linkage between actuator and steering stem arm | set | $100–250 (est.) | [McMaster-Carr](https://www.mcmaster.com/) |
| Breakaway / overload link and stem bracket | Lets a rider overpower a seized actuator; bracket is custom | 1 | $200–500 (est.) | Local machine shop; hardware from [McMaster-Carr](https://www.mcmaster.com/) |

A rotary servo on the steering stem was listed as an option in the BOM. The Volz DA 58-D turned out to be an aerospace-class unit (200 N·m peak, 5.6 kg, redundant), far more than this job needs; the linear actuator is the practical route.

## 3. Electronics and vehicle interfacing

| Part | Role in the build | Qty | Indicative price | Where to buy |
|---|---|---|---|---|
| Teensy 4.1 | Vehicle Interface Unit microcontroller: three CAN ports, fast ADC, plenty of I/O. Now manufactured by SparkFun. | 1 (+1 spare) | ≈ $32 | [SparkFun](https://sparkfun.com/products/16771) · [PJRC](https://pjrc.com/store/teensy41.html) |
| Microchip MCP4922 dual 12-bit DAC | Emulates the two throttle sensor tracks, and a second chip the iBR lever. External reference pin tied to the ECU's 5 V sensor supply. | 2 | $4–5 each (est.) | [DigiKey](https://www.digikey.com/) · [Mouser](https://www.mouser.com/) |
| TI OPA2192 op-amp | Output buffers for the emulated sensor signals | 2 | $4–6 each (est.) | [TI](https://www.ti.com/product/OPA2192) · [DigiKey](https://www.digikey.com/) |
| Omron G6K-2 (or TE IM) sealed signal relay, DPDT | Changeover between stock sensor and emulated signal; normally-closed side is the stock sensor | 2 (+2 spare) | $4–6 each (est.) | [DigiKey](https://www.digikey.com/) · [Mouser](https://www.mouser.com/) |
| TI TPS3823 watchdog supervisor | Drops the changeover relays if the VIU firmware stops | 1 | $2–3 (est.) | [TI](https://www.ti.com/product/TPS3823) |
| TI ISO1042 isolated CAN transceiver | Listen-only tap on the BRP CAN bus (TX left unconnected) | 2 | $5–15 each (est.) | [TI](https://www.ti.com/product/ISO1042) · [DigiKey](https://www.digikey.com/) |
| PEAK PCAN-USB (IPEH-002022 isolated, or IPEH-002021) | Bench and on-trailer CAN sniffing during reverse-engineering | 1 | $235–300 | [PEAK-System](https://peak-system.com/PCAN-USB.199.0.html?L=1) · [Grid Connect](https://gridconnect.com/products/can-usb-adapter-pcan-usb) |
| Waveshare 2-CH isolated CAN HAT | Gives the companion computer an NMEA 2000 port and a second logging port | 1 | $25–40 (est.) | [Waveshare](https://www.waveshare.com/product/2-ch-can-hat.htm) · [PiShop.us](https://www.pishop.us/product/2-channel-isolated-can-bus-hat-for-raspberry-pi/) |
| Alternative: Actisense NGX-1 | Certified NMEA 2000 to USB gateway. The NGT-1 named in earlier drafts is retired. | 1 | $200–300 (est.) | [Actisense](https://actisense.com/) · [Defender](https://defender.com/) |
| NMEA 2000 starter kit | Backbone, tees, terminators, power tap | 1 | $60–100 (est.) | [Defender](https://defender.com/) · [West Marine](https://www.westmarine.com/) |
| CanDooPro, Limited Home version | Reads live data and fault codes for correlating CAN frames; SBT lists Sea-Doo coverage through 2023 models | 1 | ≈ $527 (full shop version ≈ $2,399) | [SBT, home version](https://sbt.com/products/can-doo-pro-limited-home-version-diagnostic-tool) · [SBT, shop version](https://sbt.com/products/can-doo-pro-unlimited-shop-system-diagnostic-tool) |
| BRP BUDS2 with MPI-3 | Dealer tool; needed for key programming and some settings | n/a | Dealer service | Authorised Sea-Doo dealer |
| BRP shop manual and wiring diagrams, 2019 RXP-X 300 | Pinouts, sensor voltages, fuse and relay layout | 1 | $50–120 (est.) | Authorised Sea-Doo dealer |
| Deutsch DT / DTM connector kits and crimp tool | T-harnesses and box connections | 1 kit | $80–200 (est.) | [Prowire USA kits](https://www.prowireusa.com/c-19-deutsch-dt-connector-kits.html) · [BuyDeutsch](https://www.buydeutsch.com/collections/project-packs) |
| OEM-pattern pigtails for throttle sensor, iBR lever and diagnostic port | Lets the T-harness plug in without cutting the factory loom. Identify the connector family on the craft first. | 3 | $30–100 (est.) | Sea-Doo dealer parts counter; [Prowire USA](https://prowireusa.com/) |
| DS18B20 sealed probes, SHT31 sensor | Engine bay and avionics box temperature and humidity | 3 + 1 | $20–40 (est.) | [SparkFun](https://www.sparkfun.com/) · [Adafruit](https://www.adafruit.com/) |

## 4. Telemetry and video

| Part | Role in the build | Qty | Indicative price | Where to buy |
|---|---|---|---|---|
| Peplink MAX BR1 Pro 5G | Primary link: dual-SIM 5G router with SpeedFusion bonding. Current SKU is MAX-BR1-PRO-5GN-T-PRM; the 5GH is discontinued. | 1 | ≈ $1,000 (est.) | [Peplink](https://www.peplink.com/products/max-br1-pro-5g) · [5Gstore](https://5gstore.com/) · [Westward Sales](https://westwardsales.com/peplink-br1-pro-5g) |
| Budget alternative: Teltonika RUTX50 | Dual-SIM 5G with failover, no bonding. End of ordering is announced for February 2027; RUTM50 is the successor. | 1 | $350–450 (est.) | [Teltonika](https://teltonika-networks.com/products/routers/rutx50) |
| Poynting OMNI-402-5G (A-OMNI-0402-V2-01) | Marine 2×2 MIMO cellular antenna, IP68, 1"-14 marine mount | 1 (2 for 4×4) | $409–450 | [Poynting](https://poynting.tech/antennas/omni-402/) · [5Gstore](https://5gstore.com/product/14692_poynting_omni-402-5g_2x2_mimo_matine_lte5g_antenna) · [Westward Sales](https://westwardsales.com/poynting-omni-402-mimo-lte-antenna) |
| RFDesign RFD900x-US bundle | Independent 900 MHz MAVLink link, two modems with antennas (RFD868x for EU) | 1 bundle | $220–380 | [IR-LOCK](https://irlock.com/products/rfd900ux-us-modem-bundle-fcc) · [ReadyMadeRC](https://www.readymaderc.com/products/details/rfdesign-900x-telemetry-modem-bundle) · [RFDesign store](https://store.rfdesign.com.au/) |
| LoRa alternative: mLRS | Open-source LoRa MAVLink link, longer range at lower data rate | 1 pair | $60–150 (est.) | [mLRS project](https://github.com/olliw42/mLRS) |
| Ground Control RockBLOCK 9603 | Iridium short-burst modem for last-resort position and status | 1 | £242 (≈ $300) plus airtime | [Ground Control](https://www.groundcontrol.com/product/rockblock-9603/) |
| Optional: Starlink Mini | Broadband backup where there is no cellular cover | 1 | ≈ $599 plus plan | [Starlink](https://www.starlink.com/) |
| Axis P1465-LE bullet camera | Pilot camera: 2 MP, IP66/IP67, NEMA 4X, PoE | 1 | $600–900 (est.) | [Axis](https://www.axis.com/products/axis-p1465-le) |
| Side and aft cameras | Three fixed wide-angle IP67 PoE cameras; any ONVIF/RTSP model with H.264 | 3 | $100–300 each (est.) | Security camera distributors |
| Optional: FLIR M232 | Pan/tilt marine thermal camera, 320×240, H.264 network stream, 12/24 V | 1 | $2,795–3,095 | [FLIR](https://www.flir.com/products/m232/) · [Raymarine](https://raymarine.com/en-us/our-products/thermal-cameras/flir-thermal-cameras/flir-m232) · [Fisheries Supply](https://www.fisheriessupply.com/flir-maritime-us-m232-pan-and-tilt-marine-thermal-camera) |
| Optional: Sionyx Nightwave | Fixed ultra-low-light colour camera, IP67; the Nightwave Digital version has IP/PoE output | 1 | ≈ $1,895 | [Sionyx](https://www.sionyx.com/pages/nightwave-digital) · [Defender](https://defender.com/en_us/sionyx-nightwave-ultra-low-light-night-vision-marine-camera) |
| Teltonika TSW101 | 5-port gigabit switch, four PoE+ ports, 9–30 V DC input so it runs straight off the avionics battery | 1 | ≈ $90–200 | [Teltonika](https://teltonika-networks.com/products/switches/tsw101) |
| MediaMTX | Video server on the companion: RTSP in, WebRTC and SRT out | n/a | Free | [GitHub](https://github.com/bluenviron/mediamtx) |
| SIM plans, two carriers | Data for the router | 2 | $40–120 per month (est.) | Carriers or IoT SIM providers |

## 5. Power, enclosures and safety

| Part | Role in the build | Qty | Indicative price | Where to buy |
|---|---|---|---|---|
| Victron Orion-Tr Smart 12/12-18A Isolated (ORI121222120) | Charges the avionics battery from the craft battery with galvanic isolation. IP43: mount inside the sealed box. | 1 | $160–270 | [Battle Born](https://battlebornbatteries.com/products/victron-orion-tr-smart-isolated-dc-dc-chargers) · [Fisheries Supply](https://www.fisheriessupply.com/victron-energy-orion-tr-smart-dc-dc-charger-isolated) · [Powerwerx](https://powerwerx.com/victron-ori121222120-oriontrsmart-18a-isolated) |
| Victron Orion-Tr 12/24-15A Isolated (ORI122441110) | 24 V, 360 W supply for the steering actuator | 1 | $200–240 | [eMarine](https://emarineinc.com/products/victron-orion-tr-12-24-15a-360w-isolated-dc-dc-converter) · [Mealey Marine](https://mealeymarine.com/products/victron-orion-tr-12-24-15a-360w-isolated-dc-dc-converter-ori122441110) |
| 12 V LiFePO4 battery, 20–30 Ah, with BMS | Avionics battery; rides through cranking dips and keeps alarms alive with the engine off | 1 | $120–300 (est.) | Marine or battery suppliers |
| 12→5 V converters (Mean Well or Traco) | Companion computer supply and the Cube's second feed | 2 | $20–50 each (est.) | [DigiKey](https://www.digikey.com/) · [Mouser](https://www.mouser.com/) |
| Blue Sea 5025 ST Blade fuse block | Six fused circuits with negative bus and cover | 1 | $40–60 (est.) | [Blue Sea](https://www.bluesea.com/products/5025/ST_Blade_ATO_Fuse_Block_-_6_Circuits) · [Defender](https://defender.com/en_us/blue-sea-systems-st-blade-6-fuse-block-with-common-negative-bus-5025) · [Waytek](https://waytekwire.com/product/blue-sea-systems-5025-st-blade-fuse-block) |
| Blue Sea 6006 m-Series battery switch | Isolates the avionics system | 1 | $30–45 (est.) | [Blue Sea](https://www.bluesea.com/) · [Defender](https://defender.com/) |
| Polycase WQ-series enclosure, clear cover | Avionics box: hinged polycarbonate, NEMA 4X, IP67 (some sizes IP68) | 1 | $60–200 (est.) | [Polycase WQ series](https://www.polycase.com/wq-series) |
| Small die-cast IP67 box (Hammond 1550Z or similar) | Aft relay box for the kill relays | 1 | $30–60 (est.) | [DigiKey](https://www.digikey.com/) · [Mouser](https://www.mouser.com/) |
| M12 panel connectors, cable glands, membrane vent | Box penetrations for CAN, Ethernet and power; vent equalises pressure | set | $100–300 (est.) | [DigiKey](https://www.digikey.com/) · [McMaster-Carr](https://www.mcmaster.com/) |
| Wire-rope or elastomer isolators | Vibration mounts for the avionics box | 4 | $40–120 (est.) | [McMaster-Carr](https://www.mcmaster.com/) |
| **Wireless e-stop, long range** | Independent engine-kill radio. Must be a 900 MHz class system: FORT's 900 MHz Wireless E-Stop with Vehicle Safety Controller is quoted at about 2 km line of sight; Cattron BWI Eagle at about 1.5 km standard, further with high-gain antennas. | 1 system | Quote; budget $2,500–5,000 (est.) | [FORT via Clearpath](https://store.clearpathrobotics.com/products/wireless-e-stop) · [BWI Eagle](https://www.bwieagle.com/products/wireless-e-stops/) · [Cattron](https://www.cattron.com/products/wireless-emergency-stops/l-stop/) |
| IP67 mushroom e-stop buttons, NC contacts | Local stop on the craft, in series with the radio receiver | 2 | $20–50 each (est.) | [McMaster-Carr](https://www.mcmaster.com/) · [DigiKey](https://www.digikey.com/) |
| Sealed 12 V relays (TE or Littelfuse), 30–40 A | Kill relays K1–K3 | 3 (+1 spare) | $10–40 each (est.) | [Waytek](https://waytekwire.com/) · [DigiKey](https://www.digikey.com/) |
| Fireboy-Xintex G-1B-R gasoline fume detector | Fuel vapour alarm with remote sensor, 12/24 V. Replaces the MB-1, which is discontinued. Confirm it has a relay output for the safety chain; the G-1BB-R blower-control version does. | 1 | $200–350 (est.) | [Mealey Marine](https://mealeymarine.com/products/xintex-gasoline-fume-detector-alarm-w-plastic-sensor-black-bezel-display-g-1b-r) · [West Marine M-series](https://www.westmarine.com/fireboy-xintex-m-series-gasoline-fume-detector-18233080.html) |
| Rule LoPro LP900S | Automatic 900 GPH bilge pump with built-in water sensing, 4 A, low profile | 1 | $87–118 | [Defender](https://defender.com/en_us/rule-lopro-automatic-bilge-pump-lp900s) · [Fisheries Supply](https://www.fisheriessupply.com/rule-lopro-series-900-gph-bilge-pumps-low-profile) |
| Water Witch 101 electronic bilge switch | High-water switch for the safety chain; no moving parts | 1–2 | $48–55 each | [Defender](https://defender.com/en_us/water-witch-submersible-electronic-bilge-pump-switch-101) · [Fisheries Supply](https://fisheriessupply.com/water-witch-bilge-pump-switch-101/101) · [Go2marine](https://www.go2marine.com/products/water-witch-bilge-switch-101-12v) |
| Sea-Doo RF D.E.S.S. key (295100945) | Extra key to be programmed by a dealer as a speed-limited Learning Key for testing. Confirm the part number for a 2019 RXP with the dealer. | 1 | $60–120 plus programming (est.) | [BRP Sea-Doo shop](https://sea-doo-shop.brp.com/us/en/295100945-rf-d-e-s-s-key.html) · [RIVA Racing](https://rivaracing.com/sea-doo-learning-key-lanyard-spark-with-dess-278003094.html) |
| BlazeCut T-series | Self-contained automatic fire suppression tube for the engine bay; needs an enclosed space, and marine approval is not confirmed | 1 | $150–400 (est.) | [BlazeCut](https://www.blazecut.com/) |
| All-round white LED navigation light and flag | Visibility to other water users | 1 | $40–100 (est.) | [West Marine](https://www.westmarine.com/) · [Defender](https://defender.com/) |

## General suppliers

| Supplier | Good for |
|---|---|
| [DigiKey](https://www.digikey.com/), [Mouser](https://www.mouser.com/) | Chips, relays, connectors, DC-DC modules, enclosures |
| [McMaster-Carr](https://www.mcmaster.com/) | Hardware, rod ends, isolators, e-stop buttons, glands |
| [Defender](https://defender.com/), [West Marine](https://www.westmarine.com/), [Fisheries Supply](https://www.fisheriessupply.com/) | Marine electrical, pumps, detectors, NMEA 2000 |
| [IR-LOCK](https://irlock.com/), [GetFPV](https://www.getfpv.com/), [RobotShop](https://www.robotshop.com/) | Autopilot, GNSS, radios |
| [Prowire USA](https://prowireusa.com/), [Waytek](https://waytekwire.com/) | Deutsch connectors, wire, relays, fusing |
| [SBT](https://sbt.com/), [RIVA Racing](https://rivaracing.com/) | Sea-Doo parts and diagnostic tools |
| Authorised Sea-Doo dealer | Shop manual, OEM connectors, key programming |
