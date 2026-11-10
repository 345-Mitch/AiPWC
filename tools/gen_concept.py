#!/usr/bin/env python3
"""Generate the concept drawings in docs/img/. Schematic only, not to scale."""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "img")
FONT = "font-family='Helvetica,Arial,sans-serif'"
C = dict(auto="#2563eb", comms="#7c3aed", safety="#dc2626", power="#d97706",
         video="#0d9488", act="#16a34a", stock="#64748b")
INK, BG, HULL, DECK = "#0f172a", "#f8fafc", "#e2e8f0", "#cbd5e1"


def svg(w, h, body, bg=BG):
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' "
            f"width='{w}' height='{h}' {FONT}>"
            f"<rect width='{w}' height='{h}' rx='14' fill='{bg}'/>{body}</svg>")


def text(x, y, s, size=16, fill=INK, anchor="start", weight="normal"):
    return (f"<text x='{x}' y='{y}' font-size='{size}' fill='{fill}' "
            f"text-anchor='{anchor}' font-weight='{weight}'>{s}</text>")


def marker(x, y, n, cat):
    return (f"<circle cx='{x}' cy='{y}' r='16' fill='{C[cat]}' stroke='#fff' stroke-width='2.5'/>"
            + text(x, y + 6, n, 17, "#fff", "middle", "bold"))


def box(x, y, w, h, cat, dashed=True, label=None, size=13):
    d = "stroke-dasharray='6 4'" if dashed else ""
    s = (f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='5' fill='{C[cat]}22' "
         f"stroke='{C[cat]}' stroke-width='2' {d}/>")
    if label:
        s += text(x + w / 2, y + h / 2 + 5, label, size, C[cat], "middle", "bold")
    return s


def legend(x, y):
    items = [("auto", "Autonomy"), ("act", "Actuation"), ("safety", "Safety"),
             ("power", "Power"), ("comms", "Radio links"), ("video", "Sensors / video"),
             ("stock", "Stock craft")]
    s = ""
    for cat, name in items:
        s += f"<rect x='{x}' y='{y - 12}' width='16' height='16' rx='4' fill='{C[cat]}'/>"
        s += text(x + 22, y + 1, name, 14)
        x += 150
    return s


# marker positions: number -> (category, side-view xy list, top-view xy list)
M = {
    1: ("auto", [(862, 362)], [(855, 260)]),
    2: ("power", [(777, 368)], [(780, 335)]),
    3: ("auto", [(950, 262)], [(965, 260)]),
    4: ("auto", [(208, 222)], [(238, 260)]),
    5: ("act", [(668, 300)], [(722, 260)]),
    6: ("act", [(636, 200)], [(690, 172)]),
    7: ("video", [(730, 188)], [(800, 260)]),
    8: ("video", [(330, 188)], [(290, 302)]),
    9: ("comms", [(342, 118)], [(290, 260)]),
    10: ("safety", [(206, 296), (612, 262)], [(200, 150), (650, 345)]),
    11: ("safety", [(367, 357)], [(350, 180)]),
    12: ("safety", [(470, 428)], [(480, 260)]),
    13: ("safety", [(228, 422)], [(190, 260)]),
    14: ("act", [(98, 372)], [(112, 222)]),
    15: ("video", [(560, 446)], [(600, 365)]),
    16: ("auto", [(624, 376)], [(640, 205)]),
}


def side():
    b = text(30, 40, "Concept layout, side view", 22, weight="bold")
    b += text(30, 62, "Schematic, not to scale. Bow to the right. Dashed = inside the hull.", 14, C["stock"])
    b += "<rect x='14' y='424' width='1172' height='70' fill='#bae6fd' opacity='.55'/>"
    # hull
    b += (f"<path d='M160,446 L880,446 Q1010,430 1060,338 L905,300 L760,232 L705,228 "
          f"L648,286 L390,278 L362,266 L336,312 L170,320 Z' fill='{HULL}' stroke='{INK}' stroke-width='2.5'/>")
    b += f"<path d='M392,280 L646,288 L640,300 L396,294 Z' fill='{INK}' opacity='.75'/>"   # seat
    b += f"<line x1='700' y1='232' x2='678' y2='206' stroke='{INK}' stroke-width='6' stroke-linecap='round'/>"
    b += f"<line x1='664' y1='206' x2='694' y2='206' stroke='{INK}' stroke-width='7' stroke-linecap='round'/>"
    # stock internals
    b += box(410, 335, 190, 82, "stock", label="Rotax 1630 ACE")
    b += box(650, 345, 85, 68, "stock", label="Fuel")
    b += box(256, 350, 44, 40, "stock", label="12 V")
    b += box(124, 398, 78, 34, "stock", False, "Jet / iBR", 12)
    # added equipment
    b += box(815, 335, 95, 55, "auto")
    b += box(750, 345, 55, 46, "power")
    b += box(690, 292, 62, 16, "act")
    b += box(345, 340, 45, 35, "safety")
    b += f"<path d='M940,300 q10,-16 20,0 Z' fill='{C['auto']}'/>"
    # mast
    b += f"<line x1='290' y1='314' x2='290' y2='140' stroke='{INK}' stroke-width='5'/>"
    b += f"<line x1='246' y1='236' x2='290' y2='236' stroke='{INK}' stroke-width='4'/>"
    b += f"<path d='M236,236 q10,-16 20,0 Z' fill='{C['auto']}'/>"
    b += f"<line x1='270' y1='140' x2='312' y2='140' stroke='{INK}' stroke-width='4'/>"
    for x, hgt in ((272, 44), (290, 14), (310, 34)):
        b += f"<line x1='{x}' y1='140' x2='{x}' y2='{140 - hgt}' stroke='{C['comms']}' stroke-width='4' stroke-linecap='round'/>"
    b += f"<rect x='280' y='180' width='28' height='16' rx='3' fill='{C['video']}'/>"
    b += f"<rect x='716' y='214' width='24' height='14' rx='3' fill='{C['video']}'/>"
    b += f"<rect x='548' y='446' width='24' height='7' fill='{C['video']}'/>"
    for n, (cat, pts, _) in M.items():
        for x, y in pts:
            b += marker(x, y, n, cat)
    b += legend(30, 540)
    return svg(1200, 570, b)


def top():
    b = text(30, 40, "Concept layout, top view", 22, weight="bold")
    b += text(30, 62, "Schematic, not to scale. Bow to the right, port side at the top.", 14, C["stock"])
    b += (f"<path d='M150,95 L700,95 Q960,112 1060,260 Q960,408 700,425 L150,425 Z' "
          f"fill='{HULL}' stroke='{INK}' stroke-width='2.5'/>")
    b += f"<rect x='330' y='112' width='330' height='70' rx='10' fill='{DECK}'/>"
    b += f"<rect x='330' y='338' width='330' height='70' rx='10' fill='{DECK}'/>"
    b += f"<rect x='370' y='215' width='285' height='90' rx='26' fill='{INK}' opacity='.75'/>"
    b += f"<ellipse cx='745' cy='260' rx='62' ry='56' fill='{DECK}' stroke='{INK}' stroke-width='1.5'/>"
    b += f"<line x1='690' y1='172' x2='690' y2='348' stroke='{INK}' stroke-width='8' stroke-linecap='round'/>"
    b += f"<rect x='812' y='212' width='96' height='96' rx='10' fill='none' stroke='{INK}' stroke-width='1.5'/>"
    b += box(822, 224, 76, 72, "auto")
    b += box(754, 318, 54, 36, "power")
    b += box(326, 162, 48, 36, "safety")
    b += f"<rect x='96' y='240' width='54' height='40' rx='4' fill='{C['stock']}55' stroke='{C['stock']}' stroke-width='2'/>"
    b += text(123, 300, "Nozzle", 12, C["stock"], "middle")
    b += f"<line x1='238' y1='260' x2='290' y2='260' stroke='{INK}' stroke-width='4'/>"
    b += text(500, 85, "port", 13, C["stock"], "middle") + text(500, 447, "starboard", 13, C["stock"], "middle")
    for n, (cat, _, pts) in M.items():
        for x, y in pts:
            b += marker(x, y, n, cat)
    b += legend(30, 490)
    return svg(1200, 520, b)


def avionics():
    b = text(30, 40, "Avionics box, internal layout", 22, weight="bold")
    b += text(30, 62, "Mock-up of the sealed IP67 box in the front storage bin. All parts on one aluminium plate.", 14, C["stock"])
    b += f"<rect x='40' y='86' width='1120' height='500' rx='22' fill='#fff' stroke='{INK}' stroke-width='3'/>"
    b += f"<rect x='62' y='108' width='1076' height='456' rx='10' fill='{HULL}' stroke='{DECK}' stroke-width='2'/>"
    rows = [
        (124, 120, [("comms", 300, "Peplink BR1 Pro 5G", "dual-SIM router"),
                    ("video", 220, "Teltonika TSW101", "PoE switch, 4 cameras"),
                    ("comms", 230, "RFD900x", "900 MHz MAVLink"),
                    ("comms", 250, "RockBLOCK 9603", "Iridium SBD")]),
        (262, 130, [("auto", 250, "Cube Orange+", "ArduPilot Rover"),
                    ("auto", 290, "Raspberry Pi 5 + CAN HAT", "BlueOS, video, VPN, logs"),
                    ("act", 460, "Vehicle Interface Unit", "Teensy 4.1 · DACs · changeover relays · CAN tap")]),
        (410, 138, [("power", 250, "Orion-Tr Smart 12/12", "isolated charger"),
                    ("power", 250, "Orion-Tr 12/24", "actuator supply"),
                    ("power", 200, "12→5 V × 2", "Cube + companion"),
                    ("power", 300, "Fuse block + TVS", "one fuse per load")]),
    ]
    for y, h, cells in rows:
        x = 78
        for cat, w, name, sub in cells:
            b += (f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='8' fill='#fff' "
                  f"stroke='{C[cat]}' stroke-width='3'/>")
            b += f"<rect x='{x}' y='{y}' width='{w}' height='10' rx='4' fill='{C[cat]}'/>"
            b += text(x + w / 2, y + h / 2 + 4, name, 17, INK, "middle", "bold")
            b += text(x + w / 2, y + h / 2 + 26, sub, 13, C["stock"], "middle")
            x += w + 15
    b += text(203, 380, "arrow on Cube points to bow →", 12, C["auto"], "middle")
    ports = [("power", "12 V in"), ("power", "24 V out"), ("auto", "CAN: craft"), ("auto", "CAN: N2K"),
             ("act", "Throttle / iBR"), ("video", "Ethernet × 4"), ("auto", "GNSS × 2"),
             ("comms", "RF × 4"), ("stock", "Vent")]
    x = 62
    for cat, name in ports:
        w = 112
        b += f"<rect x='{x + 36}' y='586' width='40' height='22' rx='4' fill='{C[cat]}'/>"
        b += text(x + 56, 630, name, 13, INK, "middle")
        x += w + 8.5
    b += text(600, 664, "All connectors exit the underside, with drip loops. The e-stop receiver and kill relays are in a separate box aft.",
              14, C["stock"], "middle")
    return svg(1200, 690, b)


def gcs():
    D, P, T, G = "#0b1220", "#141c2e", "#e2e8f0", "#22c55e"
    b = f"<rect x='16' y='16' width='1168' height='44' rx='8' fill='{P}'/>"
    b += text(32, 45, "AiPWC ground station", 18, T, weight="bold")
    chips = [("HOLD", "#f59e0b"), ("RTK FIX", G), ("LTE 2/2", G), ("900 MHz", G), ("SAT standby", "#64748b"),
             ("E-STOP ARMED", G)]
    x = 330
    for name, col in chips:
        w = 26 + 9.4 * len(name)
        b += f"<rect x='{x}' y='26' width='{w}' height='24' rx='12' fill='{col}'/>"
        b += text(x + w / 2, 43, name, 13, "#0b1220", "middle", "bold")
        x += w + 10
    # video
    b += f"<rect x='16' y='72' width='780' height='470' rx='8' fill='#7dd3fc'/>"
    b += f"<path d='M16,300 L796,300 L796,534 Q796,542 788,542 L24,542 Q16,542 16,534 Z' fill='#0e7490'/>"
    b += f"<path d='M330,542 L390,330 L420,330 L480,542 Z' fill='#e2e8f0' opacity='.25'/>"
    b += f"<path d='M300,542 Q405,470 510,542 Z' fill='{P}' opacity='.9'/>"
    b += f"<rect x='250' y='84' width='310' height='34' rx='6' fill='{D}' opacity='.75'/>"
    for i, h in enumerate(("330", "345", "N", "015", "030")):
        b += text(285 + i * 60, 108, h, 15, T if h != "N" else "#facc15", "middle", "bold")
    b += f"<path d='M405,120 l-8,12 h16 Z' fill='#facc15'/>"
    for x, lab, val in ((32, "SPEED", "14 kn"), (32 + 150, "THROTTLE", "22 %"), (32 + 300, "RPM", "4 150"),
                        (32 + 450, "DEPTH", "8.4 m"), (32 + 600, "LATENCY", "180 ms")):
        b += f"<rect x='{x}' y='470' width='136' height='58' rx='6' fill='{D}' opacity='.78'/>"
        b += text(x + 12, 490, lab, 12, "#94a3b8") + text(x + 12, 518, val, 22, T, weight="bold")
    b += text(32, 96, "CAM 1 · PILOT", 13, D, weight="bold")
    # map
    b += f"<rect x='808' y='72' width='376' height='250' rx='8' fill='#1e3a5f'/>"
    b += f"<path d='M808,250 Q900,215 960,260 T1184,240 L1184,314 Q1184,322 1176,322 L816,322 Q808,322 808,314 Z' fill='#365314'/>"
    b += f"<path d='M840,100 L1150,96 L1160,215 L870,225 Z' fill='none' stroke='#f87171' stroke-width='2.5' stroke-dasharray='8 5'/>"
    b += f"<path d='M900,205 L960,140 L1060,130 L1110,180' fill='none' stroke='#facc15' stroke-width='2.5'/>"
    for x, y in ((900, 205), (960, 140), (1060, 130), (1110, 180)):
        b += f"<circle cx='{x}' cy='{y}' r='6' fill='#facc15'/>"
    b += f"<path d='M990,128 l14,7 l-14,7 l4,-7 Z' fill='#fff' stroke='#fff' stroke-width='3'/>"
    b += text(820, 92, "MAP · geofence dashed", 12, "#cbd5e1")
    # engine panel
    b += f"<rect x='808' y='334' width='376' height='208' rx='8' fill='{P}'/>"
    b += text(824, 358, "ENGINE (from craft CAN)", 12, "#94a3b8")
    gauges = [("Coolant", "78 °C", .55, G), ("Oil press.", "3.9 bar", .65, G), ("Boost", "0.3 bar", .25, G),
              ("Intake air", "41 °C", .4, G), ("Battery", "13.9 V", .8, G), ("Bilge", "DRY", 1, G)]
    for i, (lab, val, f, col) in enumerate(gauges):
        x, y = 824 + (i % 2) * 182, 378 + (i // 2) * 54
        b += text(x, y + 4, lab, 13, "#94a3b8") + text(x + 164, y + 4, val, 15, T, "end", "bold")
        b += f"<rect x='{x}' y='{y + 14}' width='164' height='8' rx='4' fill='#334155'/>"
        b += f"<rect x='{x}' y='{y + 14}' width='{164 * f}' height='8' rx='4' fill='{col}'/>"
    # camera strip + stop
    for i, name in enumerate(("CAM 2 · PORT", "CAM 3 · STBD", "CAM 4 · AFT")):
        x = 16 + i * 200
        b += f"<rect x='{x}' y='554' width='188' height='110' rx='8' fill='#0e7490'/>"
        b += f"<rect x='{x}' y='554' width='188' height='48' rx='8' fill='#7dd3fc'/>"
        b += text(x + 10, 574, name, 12, D, weight="bold")
    b += f"<rect x='616' y='554' width='180' height='110' rx='8' fill='{P}'/>"
    b += text(706, 580, "MODE", 12, "#94a3b8", "middle")
    for i, (m, on) in enumerate((("MANUAL", 0), ("HOLD", 1), ("AUTO", 0))):
        col = "#f59e0b" if on else "#334155"
        b += f"<rect x='{628 + i * 56}' y='596' width='50' height='52' rx='6' fill='{col}'/>"
        b += text(653 + i * 56, 627, m, 10, T if not on else D, "middle", "bold")
    b += f"<rect x='808' y='554' width='376' height='110' rx='8' fill='#b91c1c'/>"
    b += text(996, 606, "HOLD · IDLE + NEUTRAL", 20, "#fff", "middle", "bold")
    b += text(996, 632, "software stop. Engine kill is the separate hardware e-stop.", 12, "#fecaca", "middle")
    b += text(600, 688, "Concept mock-up with invented values. Not a screenshot of working software.", 13, "#94a3b8", "middle")
    return svg(1200, 704, b, D)


for name, fn in (("concept-side", side), ("concept-top", top), ("avionics-box", avionics), ("gcs-mockup", gcs)):
    with open(os.path.join(OUT, name + ".svg"), "w") as f:
        f.write(fn())
    print("wrote", name)
