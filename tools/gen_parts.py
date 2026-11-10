#!/usr/bin/env python3
"""Generate docs/03-sourcing.md: one row per part, with price and importance."""
import os
L = dict(
 irlock="https://irlock.com/", dk="https://www.digikey.com/", mc="https://www.mcmaster.com/",
 defender="https://defender.com/", wm="https://www.westmarine.com/")
C, R, M, O = "Critical", "Required", "Recommended", "Optional"
# (group, part, role, qty, unit_lo, unit_hi, estimated, importance, links)
P = [
 ("Autopilot and navigation","CubePilot Cube Orange+ Standard Set (HX4-06222)","Autopilot running ArduPilot Rover; includes carrier board and one power brick",1,450,450,0,C,"[IR-LOCK](https://irlock.com/products/cube-orange-plus-standard-set) · [RobotShop](https://www.robotshop.com/products/cube-orange-standard-set)"),
 ("Autopilot and navigation","CubePilot Here4 RTK GNSS","Position and GNSS heading from a bow and an aft antenna",2,225,280,0,C,"[IR-LOCK](https://irlock.com/products/here4-multiband-rtk-gnss) · [GetFPV](https://www.getfpv.com/electronics/flight-controllers/cubepilot-here4-multiband-rtk-gnss-gps-module.html)"),
 ("Autopilot and navigation","Raspberry Pi 5 (8 GB) with NVMe","Companion computer: BlueOS, video server, VPN, logging",1,120,200,1,R,"[Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-5/) · [SparkFun](https://www.sparkfun.com/raspberry-pi-5-8gb.html)"),
 ("Autopilot and navigation","Second power brick","Redundant 5 V feed to the Cube",1,20,50,1,M,f"[IR-LOCK]({L['irlock']})"),
 ("Autopilot and navigation","Blue Robotics Ping2 echosounder","Depth under the hull",1,450,450,1,M,"[Blue Robotics](https://bluerobotics.com/store/sonars/echosounders/ping-sonar-r2-rp)"),
 ("Autopilot and navigation","RadioMaster Boxer (ELRS) with RP3 receiver","Hand controller for launch and recovery",1,150,300,1,M,"[RadioMaster](https://www.radiomasterrc.com/collections/boxer-radio)"),
 ("Autopilot and navigation","RTK corrections (NTRIP service or shore base)","Centimetre-level position; heading works without it",1,0,600,1,O,"State or national CORS network"),

 ("Steering and actuation","Ultra Motion Servo Cylinder, AM series","Steering actuator. Order only after the cable force is measured",1,1500,4000,1,C,"[Ultra Motion](https://www.ultramotion.com/servo-cylinder?series=am)"),
 ("Steering and actuation","Breakaway link and stem bracket","Lets a rider overpower a seized actuator",1,200,500,1,C,f"Local machine shop · [McMaster-Carr]({L['mc']})"),
 ("Steering and actuation","316 stainless rod ends, clevises, fasteners","Linkage from actuator to steering stem arm",1,100,250,1,C,f"[McMaster-Carr]({L['mc']})"),
 ("Steering and actuation","Novotechnik RFC-4800 rotary sensor","Independent nozzle angle feedback; catches a broken cable",1,80,250,1,R,"[Novotechnik](https://www.novotechnik.com/)"),
 ("Steering and actuation","S-type load cell, 2 kN, with amplifier","One-off measurement that sizes the actuator",1,100,250,1,R,"[Omega](https://www.omega.com/)"),

 ("Vehicle interface electronics","Teensy 4.1 (one fitted, one spare)","Vehicle Interface Unit controller",2,32,32,0,C,"[SparkFun](https://www.sparkfun.com/products/16771)"),
 ("Vehicle interface electronics","Microchip MCP4922 dual DAC","Emulates throttle and iBR lever sensor signals",2,4,5,1,C,f"[DigiKey]({L['dk']})"),
 ("Vehicle interface electronics","TI OPA2192 op-amp","Buffers the emulated sensor signals",2,4,6,1,C,"[TI](https://www.ti.com/product/OPA2192)"),
 ("Vehicle interface electronics","Omron G6K-2 sealed signal relay (two fitted, two spare)","Fail-to-stock changeover for throttle and iBR",4,4,6,1,C,f"[DigiKey]({L['dk']})"),
 ("Vehicle interface electronics","TI TPS3823 watchdog","Drops the changeover relays if firmware stops",1,2,3,1,C,"[TI](https://www.ti.com/product/TPS3823)"),
 ("Vehicle interface electronics","BRP shop manual and wiring diagrams","Pinouts, sensor voltages, fuse and relay layout",1,50,120,1,C,"Authorised Sea-Doo dealer"),
 ("Vehicle interface electronics","TI ISO1042 isolated CAN transceiver","Listen-only tap on the craft CAN bus",2,5,15,1,R,"[TI](https://www.ti.com/product/ISO1042)"),
 ("Vehicle interface electronics","PEAK PCAN-USB","CAN sniffing during reverse-engineering",1,235,300,0,R,"[PEAK-System](https://peak-system.com/PCAN-USB.199.0.html?L=1) · [Grid Connect](https://gridconnect.com/products/can-usb-adapter-pcan-usb)"),
 ("Vehicle interface electronics","CanDooPro, Limited Home version","Live data and fault codes to decode CAN frames",1,527,527,0,R,"[SBT](https://sbt.com/products/can-doo-pro-limited-home-version-diagnostic-tool)"),
 ("Vehicle interface electronics","Deutsch DT/DTM connector kit and crimp tool","All harnesses and box connections",1,80,200,1,R,"[Prowire USA](https://www.prowireusa.com/c-19-deutsch-dt-connector-kits.html)"),
 ("Vehicle interface electronics","OEM-pattern pigtails (throttle, iBR lever, diagnostic port)","Plug-in T-harnesses, no cutting of the factory loom",3,10,35,1,R,"Sea-Doo dealer parts counter"),
 ("Vehicle interface electronics","Temperature and humidity sensors (3 × DS18B20, 1 × SHT31)","Engine bay and avionics box monitoring",1,20,40,1,M,"[SparkFun](https://www.sparkfun.com/)"),
 ("Vehicle interface electronics","Waveshare 2-CH isolated CAN HAT","NMEA 2000 port for the companion computer",1,25,40,1,O,"[Waveshare](https://www.waveshare.com/product/2-ch-can-hat.htm)"),
 ("Vehicle interface electronics","NMEA 2000 starter kit","Backbone for marine instruments",1,60,100,1,O,f"[Defender]({L['defender']})"),

 ("Telemetry and video","Peplink MAX BR1 Pro 5G","Primary data link, dual SIM with bonding",1,1000,1000,1,R,"[Peplink](https://www.peplink.com/products/max-br1-pro-5g) · [Westward Sales](https://westwardsales.com/peplink-br1-pro-5g)"),
 ("Telemetry and video","Poynting OMNI-402-5G antenna","Marine cellular antenna on the mast",1,409,450,0,R,"[Poynting](https://poynting.tech/antennas/omni-402/) · [5Gstore](https://5gstore.com/product/14692_poynting_omni-402-5g_2x2_mimo_matine_lte5g_antenna)"),
 ("Telemetry and video","RFDesign RFD900x-US bundle","Second, independent control and telemetry link",1,220,380,0,R,"[IR-LOCK](https://irlock.com/products/rfd900ux-us-modem-bundle-fcc)"),
 ("Telemetry and video","Axis P1465-LE camera","Pilot camera",1,600,900,1,R,"[Axis](https://www.axis.com/products/axis-p1465-le)"),
 ("Telemetry and video","Teltonika TSW101 PoE switch","Powers and connects the cameras",1,90,200,0,R,"[Teltonika](https://teltonika-networks.com/products/switches/tsw101)"),
 ("Telemetry and video","Fixed IP67 PoE cameras (port, starboard, aft)","All-round view",3,100,300,1,M,"Security camera distributors"),
 ("Telemetry and video","Ground Control RockBLOCK 9603","Last-resort satellite position and status; airtime extra",1,300,300,0,M,"[Ground Control](https://www.groundcontrol.com/product/rockblock-9603/)"),
 ("Telemetry and video","Starlink Mini","Broadband where there is no cellular cover; plan extra",1,599,599,0,O,"[Starlink](https://www.starlink.com/)"),
 ("Telemetry and video","FLIR M232 thermal camera","Night and thermal view",1,2795,3095,0,O,"[FLIR](https://www.flir.com/products/m232/) · [Mealey Marine](https://mealeymarine.com/products/flir-m232-pan-tilt-9hz-marine-thermal-camera-e70354)"),

 ("Safety","Long-range wireless e-stop system (FORT 900 MHz or Cattron BWI Eagle)","Independent engine kill by radio. Price needs a quote",1,2500,5000,1,C,"[FORT via Clearpath](https://store.clearpathrobotics.com/products/wireless-e-stop) · [BWI Eagle](https://www.bwieagle.com/products/wireless-e-stops/)"),
 ("Safety","Sealed 12 V relays, 30–40 A (three fitted, one spare)","Kill relays K1–K3",4,10,40,1,C,"[Waytek](https://waytekwire.com/)"),
 ("Safety","IP67 mushroom e-stop buttons","Local stop at the helm and rear deck",2,20,50,1,C,f"[McMaster-Carr]({L['mc']})"),
 ("Safety","Fireboy-Xintex G-1B-R fume detector","Fuel vapour alarm in the closed hull",1,200,350,1,C,"[Mealey Marine](https://mealeymarine.com/products/xintex-gasoline-fume-detector-alarm-w-plastic-sensor-black-bezel-display-g-1b-r)"),
 ("Safety","Aft IP67 die-cast box","Houses the e-stop receiver and kill relays",1,30,60,1,R,f"[DigiKey]({L['dk']})"),
 ("Safety","Rule LoPro LP900S bilge pump","Automatic bilge pump",1,87,118,0,R,"[Defender](https://defender.com/en_us/rule-lopro-automatic-bilge-pump-lp900s) · [Mealey Marine](https://mealeymarine.com/products/rule-lopro-900gph-bilge-pump-automatic-lp900s)"),
 ("Safety","Water Witch 101 bilge switch","High-water input to the kill chain",1,48,55,0,R,"[Defender](https://defender.com/en_us/water-witch-submersible-electronic-bilge-pump-switch-101)"),
 ("Safety","All-round white LED light and flag","Visibility to other water users",1,40,100,1,R,f"[West Marine]({L['wm']})"),
 ("Safety","Sea-Doo RF D.E.S.S. key (295100945), dealer-programmed as a Learning Key","Speed limit enforced by the ECU during testing; programming extra",1,60,120,1,M,"[BRP Sea-Doo shop](https://sea-doo-shop.brp.com/us/en/295100945-rf-d-e-s-s-key.html)"),
 ("Safety","BlazeCut T-series fire suppression","Automatic engine bay fire suppression",1,150,400,1,M,"[BlazeCut](https://www.blazecut.com/)"),

 ("Power and enclosures","Victron Orion-Tr Smart 12/12-18A isolated charger","Charges the avionics battery, isolated from the craft",1,160,270,0,R,"[Mealey Marine](https://mealeymarine.com/products/victron-orion-tr-smart-12-12-18-18a-220w-isolated-dc-dc-charger-or-power-supply-ori121222120) · [Powerwerx](https://powerwerx.com/victron-ori121222120-oriontrsmart-18a-isolated)"),
 ("Power and enclosures","Victron Orion-Tr 12/24-15A isolated converter","24 V supply for the steering actuator",1,200,240,0,R,"[eMarine](https://emarineinc.com/products/victron-orion-tr-12-24-15a-360w-isolated-dc-dc-converter)"),
 ("Power and enclosures","12 V LiFePO4 battery, 20–30 Ah","Avionics battery",1,120,300,1,R,"Marine or battery suppliers"),
 ("Power and enclosures","12→5 V converters","Companion computer and the Cube's second feed",2,20,50,1,R,f"[DigiKey]({L['dk']})"),
 ("Power and enclosures","Blue Sea 5025 fuse block","One fuse per load",1,40,60,1,R,"[Blue Sea](https://www.bluesea.com/products/5025/ST_Blade_ATO_Fuse_Block_-_6_Circuits) · [Mealey Marine](https://mealeymarine.com/products/blue-sea-5025-st-blade-fuse-block-w-cover-6-circuit-w-negative-bus-5025)"),
 ("Power and enclosures","Blue Sea 6006 battery switch","Isolates the avionics system",1,30,45,1,R,"[Mealey Marine](https://mealeymarine.com/products/blue-sea-6006200-battery-switch-mini-on-off-black-6006200)"),
 ("Power and enclosures","Polycase WQ-series enclosure, clear cover","Sealed avionics box",1,60,200,1,R,"[Polycase](https://www.polycase.com/wq-series)"),
 ("Power and enclosures","M12 panel connectors, cable glands, membrane vent","Box penetrations",1,100,300,1,R,f"[DigiKey]({L['dk']})"),
 ("Power and enclosures","Vibration isolators (set of four)","Mounts for the avionics box",1,40,120,1,M,f"[McMaster-Carr]({L['mc']})"),
]
ALT = [
 ("Holybro H-RTK F9P Rover","Here4","$270–325 each","[Holybro](https://holybro.com/)"),
 ("Septentrio mosaic-go H kit","Both Here4 units","€745","[Septentrio](https://shop.septentrio.com/en/shop/mosaic-go-h-heading-gnss-module-evaluation-kit)"),
 ("Airmar DST810","Ping2","$399–624","[Defender](https://defender.com/en_us/airmar-dst810-smart-multisensor)"),
 ("Thomson Electrak HD (CAN)","Ultra Motion actuator","$1,000–2,000 (est.)","[Thomson](https://www.thomsonlinear.com/en/product/HD12B026-1000CNO1MESD)"),
 ("Actisense NGX-1","Waveshare CAN HAT","$200–300 (est.)","[Actisense](https://actisense.com/)"),
 ("Teltonika RUTX50","Peplink router","$350–450 (est.)","[Teltonika](https://teltonika-networks.com/products/routers/rutx50)"),
 ("mLRS LoRa radio pair","RFD900x","$60–150 (est.)","[mLRS](https://github.com/olliw42/mLRS)"),
 ("Sionyx Nightwave","FLIR M232","≈ $1,895","[Sionyx](https://www.sionyx.com/pages/nightwave-digital)"),
 ("Custom LoRa heartbeat e-stop (not safety rated)","Commercial e-stop","$100–200 (est.)","Built from parts"),
]
m = lambda v: f"${v:,}"
rng = lambda a, b: m(a) if a == b else f"{m(a)}–{b:,}"
out = ["# Parts List: Price, Importance and Where to Buy", "",
"One row per part. This is the single list to order from; the [BOM](02-bom.md) gives the same parts in the Phase 2 subsystem format with their interfaces.", "",
"**Importance**", "",
"| Level | Meaning |", "|---|---|",
"| Critical | The craft cannot be controlled or stopped safely without it. Fit before any powered test. |",
"| Required | Needed for the system to work as designed. |",
"| Recommended | Improves reliability or testing. Can be added later. |",
"| Optional | Useful extra. The design works without it. |", "",
"**Prices** are USD for one unit. Those marked *est.* are my estimates; the rest come from seller listings found by web search in November 2026 and were not re-checked. Links were found the same way and not all could be opened from the build environment. Within each group, parts are sorted by importance.", ""]
tot = {k: [0, 0, 0] for k in (C, R, M, O)}
n = 0
groups = []
for g in [p[0] for p in P]:
    if g not in groups: groups.append(g)
for g in groups:
    out += [f"## {g}", "", "| # | Part | What it does | Qty | Unit price | Line total | Importance | Where to buy |", "|---|---|---|---|---|---|---|---|"]
    for _, part, role, q, lo, hi, est, imp, links in P:
        if _ != g: continue
        n += 1
        e = " *est.*" if est else ""
        out.append(f"| {n} | {part} | {role} | {q} | {rng(lo, hi)}{e} | {rng(lo*q, hi*q)} | {imp} | {links} |")
        tot[imp][0] += lo*q; tot[imp][1] += hi*q; tot[imp][2] += 1
    out.append("")
out += ["## Cost by importance", "", "| Importance | Parts | Low | High | Running total, low | Running total, high |", "|---|---|---|---|---|---|"]
rl = rh = 0
for k in (C, R, M, O):
    rl += tot[k][0]; rh += tot[k][1]
    out.append(f"| {k} | {tot[k][2]} | {m(tot[k][0])} | {m(tot[k][1])} | {m(rl)} | {m(rh)} |")
out += ["", f"A working build is Critical plus Required: about {m(tot[C][0]+tot[R][0])} to {m(tot[C][1]+tot[R][1])}. "
        "The wireless e-stop and the steering actuator are roughly 40 to 50 percent of that, and both need a supplier quote.", "",
"Not in the totals: two cellular SIM plans ($40–120 per month, est.), Iridium airtime, a Starlink plan, dealer key programming, and free software (ArduPilot, BlueOS, MediaMTX, QGroundControl).", "",
"## Alternatives (not counted above)", "", "Swap one of these in for the listed part; do not buy both.", "",
"| Alternative | Replaces | Price | Where to buy |", "|---|---|---|---|"]
out += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in ALT]
open(os.path.join(os.path.dirname(__file__), "..", "docs", "03-sourcing.md"), "w").write("\n".join(out) + "\n")
print(n, "parts"); [print(k, tot[k]) for k in tot]
