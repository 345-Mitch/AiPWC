#!/usr/bin/env node
// Renders the concept drawings to PNG and builds the photo boards.
// Usage: node tools/gen_boards.js <dir with product photos>
// Photo files are named: cube here4 rfd900 teensy rockblock actuator poynting
// axis estop xintex rule bluesea5025 bluesea6006 victron flir
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const IMG = path.join(__dirname, '..', 'docs', 'img');
const PH = path.resolve(process.argv[2] || 'photos');
const mime = b => b[0] === 0x89 ? 'image/png' : b[0] === 0xff ? 'image/jpeg' : 'image/webp';
const photo = n => { const b = fs.readFileSync(path.join(PH, n)); return `data:${mime(b)};base64,${b.toString('base64')}`; };
const COL = { auto: '#2563eb', comms: '#7c3aed', safety: '#dc2626', power: '#d97706', video: '#0d9488', act: '#16a34a' };
const css = `body{margin:0;font-family:Helvetica,Arial,sans-serif;color:#0f172a;background:#f8fafc}
.card{position:absolute;width:185px;height:236px;background:#fff;border-radius:10px;box-shadow:0 1px 4px #0003;text-align:center;overflow:hidden}
.card .ph{height:132px;display:flex;align-items:center;justify-content:center;padding:8px 8px 0}
.card img{max-width:165px;max-height:124px}
.card b{display:block;font-size:14px;margin:6px 6px 2px;line-height:1.15}
.card span{font-size:12.5px;color:#475569}
.badge{position:absolute;left:8px;top:8px;min-width:26px;height:26px;border-radius:13px;color:#fff;font-weight:bold;font-size:14px;line-height:26px;padding:0 4px;box-sizing:border-box}
.bar{position:absolute;left:0;right:0;bottom:0;height:6px}`;

// [photo, name, price, category, badge, [marker xy in side-view coords...]]
const TOP = [
  ['here4', 'Here4 RTK GNSS ×2', '$225–280 each', 'auto', '3·4', [[208, 222], [950, 262]]],
  ['flir', 'FLIR M232 (optional)', '$2,795–3,095', 'video', '8', [[330, 188]]],
  ['poynting', 'Poynting OMNI-402', '$409–450', 'comms', '9', [[342, 118]]],
  ['actuator', 'Ultra Motion AM actuator', '$1,500–4,000', 'act', '5', [[668, 300]]],
  ['axis', 'Axis P1465-LE camera', '$600–900', 'video', '7', [[730, 188]]],
  ['cube', 'Cube Orange+', '$450', 'auto', '1', [[862, 362]]],
  ['teensy', 'Teensy 4.1 (VIU)', '$32', 'act', '1', [[862, 362]]],
];
const BOT = [
  ['rule', 'Rule LoPro LP900S', '$87–118', 'safety', '13', [[228, 422]]],
  ['estop', 'FORT wireless e-stop', '$2,500–5,000', 'safety', '11', [[367, 357]]],
  ['xintex', 'Xintex G-1B-R', '$200–350', 'safety', '12', [[470, 428]]],
  ['victron', 'Victron Orion-Tr Smart', '$160–270', 'power', '2', [[777, 368]]],
  ['bluesea6006', 'Blue Sea 6006 switch', '$30–45', 'power', '2', [[777, 368]]],
  ['bluesea5025', 'Blue Sea 5025 fuses', '$40–60', 'power', '1', [[862, 362]]],
  ['rfd900', 'RFD900x bundle', '$220–380', 'comms', '1', [[862, 362]]],
  ['rockblock', 'RockBLOCK 9603', '$300', 'comms', '1', [[862, 362]]],
];

function board() {
  const W = 1600, H = 1140, OX = 200, OY = 300;
  const side = fs.readFileSync(path.join(IMG, 'concept-side.svg'), 'utf8')
    .replace(/<text[^>]*>Concept layout, side view<\/text>/, '').replace(/<text[^>]*>Schematic, not to scale[^<]*<\/text>/, '')
    .replace(/<rect x='\d+' y='528'[^>]*\/>/g, '').replace(/<text x='\d+' y='541'[^>]*>[^<]*<\/text>/g, '');
  let cards = '', lines = '';
  const row = (items, y, up) => {
    const gap = (W - 30 - items.length * 185) / (items.length - 1);
    items.forEach(([p, name, price, cat, badge, pts], i) => {
      const x = 15 + i * (185 + gap);
      cards += `<div class="card" style="left:${x}px;top:${y}px"><div class="badge" style="background:${COL[cat]}">${badge}</div>
        <div class="ph"><img src="${photo(p)}"></div><b>${name}</b><span>${price}</span><div class="bar" style="background:${COL[cat]}"></div></div>`;
      for (const [mx, my] of pts) {
        const x1 = x + 92, y1 = up ? y + 236 : y, x2 = OX + mx, y2 = OY + my;
        const d = Math.hypot(x2 - x1, y2 - y1), ex = x2 - (x2 - x1) / d * 18, ey = y2 - (y2 - y1) / d * 18;
        lines += `<line x1="${x1}" y1="${y1}" x2="${ex}" y2="${ey}" stroke="${COL[cat]}" stroke-width="2.5" stroke-linecap="round" opacity=".8"/>`;
      }
    });
  };
  row(TOP, 62, true); row(BOT, 840, false);
  return `<style>${css}</style><div style="position:relative;width:${W}px;height:${H}px">
    <div style="position:absolute;left:20px;top:14px;font-size:26px;font-weight:bold">AiPWC concept: selected parts on the craft</div>
    <div style="position:absolute;right:20px;top:22px;font-size:14px;color:#475569">Schematic, not to scale. Numbers match the layout table.</div>
    <div style="position:absolute;left:${OX}px;top:${OY}px">${side}</div>
    <svg width="${W}" height="${H}" style="position:absolute;left:0;top:0">${lines}</svg>${cards}
    <div style="position:absolute;left:0;right:0;bottom:14px;text-align:center;font-size:12.5px;color:#64748b">Product photos © their manufacturers and sellers (IR-LOCK, SparkFun, Ultra Motion, Axis, Poynting, Clearpath/FORT, Mealey Marine), shown for identification.</div></div>`;
}

function avionics() {
  const cell = (cat, w, name, sub, p) => `<div style="flex:${w};background:#fff;border:3px solid ${COL[cat]};border-top-width:12px;border-radius:10px;height:200px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:4px">
    ${p ? `<img src="${photo(p)}" style="max-height:112px;max-width:92%">` : ''}<b style="font-size:17px;margin-top:6px">${name}</b><span style="font-size:13px;color:#475569">${sub}</span></div>`;
  const rows = [
    [['comms', 3, 'Peplink BR1 Pro 5G', 'dual-SIM router'], ['video', 2.2, 'Teltonika TSW101', 'PoE switch'], ['comms', 2.6, 'RFD900x', '900 MHz MAVLink', 'rfd900'], ['comms', 2.4, 'RockBLOCK 9603', 'Iridium SBD', 'rockblock']],
    [['auto', 3, 'Cube Orange+', 'ArduPilot Rover', 'cube'], ['auto', 2.8, 'Raspberry Pi 5 + CAN HAT', 'BlueOS, video, VPN, logs'], ['act', 4.4, 'Vehicle Interface Unit', 'Teensy 4.1 · DACs · relays · CAN tap', 'teensy']],
    [['power', 2.6, 'Orion-Tr Smart 12/12', 'isolated charger', 'victron'], ['power', 2.4, 'Orion-Tr 12/24', 'actuator supply'], ['power', 2, '12→5 V × 2', 'Cube + companion'], ['power', 3, 'Fuse block', 'one fuse per load', 'bluesea5025']],
  ];
  return `<style>${css}</style><div style="width:1300px;padding:20px 24px 16px;box-sizing:border-box">
    <div style="font-size:26px;font-weight:bold">Avionics box mock-up, with selected parts</div>
    <div style="font-size:14px;color:#475569;margin:4px 0 14px">Sealed IP67 box in the front storage bin. Blocks without a photo: picture not available. Not to scale.</div>
    <div style="border:4px solid #0f172a;border-radius:24px;background:#e2e8f0;padding:18px;display:flex;flex-direction:column;gap:14px">
    ${rows.map(r => `<div style="display:flex;gap:14px">${r.map(c => cell(...c)).join('')}</div>`).join('')}</div>
    <div style="text-align:center;font-size:12.5px;color:#64748b;margin-top:12px">Product photos © their manufacturers and sellers, shown for identification.</div></div>`;
}

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ deviceScaleFactor: 2, viewport: { width: 1600, height: 1140 } });
  await p.setContent(board()); await p.screenshot({ path: path.join(IMG, 'concept-board.png') });
  await p.setViewportSize({ width: 1300, height: 800 });
  await p.setContent(avionics()); await p.screenshot({ path: path.join(IMG, 'avionics-board.png'), fullPage: true });
  for (const n of ['concept-side', 'concept-top', 'avionics-box', 'gcs-mockup']) {
    const svg = fs.readFileSync(path.join(IMG, n + '.svg'), 'utf8');
    const [, w, h] = svg.match(/width='(\d+)' height='(\d+)'/);
    await p.setViewportSize({ width: +w, height: +h });
    await p.setContent(`<body style="margin:0">${svg}</body>`); await p.screenshot({ path: path.join(IMG, n + '.png') });
  }
  await b.close();
})();
