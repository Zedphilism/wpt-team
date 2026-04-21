const fs = require('fs');
const html = fs.readFileSync('C:/Users/user/Desktop/wpt-team/alatganti.html', 'utf8');

const items = [];
let totalCount = 0;

// simple state machine to parse tr and td
const trMatches = html.split('<tr>');
for(let i = 1; i < trMatches.length; i++) {
  const tr = trMatches[i].split('</tr>')[0];
  if(tr.includes('subtotal') || !tr.includes('<td')) continue;
  
  const tds = tr.split(/<td[^>]*>/);
  if(tds.length < 8) continue;
  
  // tds[0] is garbage before first td
  // tds[1] = index
  // tds[2] = pn
  // tds[3] = part name
  // tds[4] = oem
  // tds[5] = mock
  // tds[6] = qty
  // tds[7] = price
  
  const pnMatch = tds[2].match(/class="pn">(.*?)</);
  const pn = pnMatch ? pnMatch[1].trim() : 'Unknown';
  
  const nameBase = tds[3].split('<')[0].trim();
  const malayMatch = tds[3].match(/class="malay">(.*?)</);
  const malay = malayMatch ? malayMatch[1].trim() : '';
  const nameDesc = nameBase + (malay ? ' - ' + malay : '');
  
  let qty = 1;
  const qMatch = tds[6].match(/([0-9]+)/);
  if(qMatch) qty = parseInt(qMatch[1]);
  
  let price = 0;
  const pMatch = tds[7].match(/RM ([0-9,.]+)/);
  if(pMatch) price = parseFloat(pMatch[1].replace(/,/g, ''));
  
  let cat = 'Body';
  if (nameDesc.toLowerCase().includes('brk') || nameDesc.toLowerCase().includes('brek')) cat = 'Consumable';
  if (nameDesc.toLowerCase().includes('pad')) cat = 'Consumable';
  if (nameDesc.toLowerCase().includes('chain') || nameDesc.toLowerCase().includes('rantai')) cat = 'Consumable';
  if (nameDesc.toLowerCase().includes('sprocket') || nameDesc.toLowerCase().includes('sproket')) cat = 'Consumable';
  if (nameDesc.toLowerCase().includes('lamp') || nameDesc.toLowerCase().includes('meter') || nameDesc.toLowerCase().includes('winker') || nameDesc.toLowerCase().includes('relay')) cat = 'Elektronik';
  if (nameDesc.toLowerCase().includes('fan') || nameDesc.toLowerCase().includes('pump') || nameDesc.toLowerCase().includes('coolant')) cat = 'Engine';
  if (nameDesc.toLowerCase().includes('shock') || nameDesc.toLowerCase().includes('cushion') || nameDesc.toLowerCase().includes('cylinder')) cat = 'Safety Critical';
  
  let src = 'AutoDenso';
  if (cat === 'Consumable') src = 'Shopee Mall (Bendix/RK-M)';
  if (cat === 'Elektronik') src = 'HQ / Eang Chun Motor';
  if (cat === 'Safety Critical') src = 'Boon Siew Honda HQ / EMOS HQ';
  
  let model = pn.includes('KZZ') || pn.includes('KYJ') ? 'Honda CRF250L' : 'Kawasaki KLX 250';
  
  items.push({ model, pn, nameDesc, cat, src, qty, price });
  totalCount += qty;
}

console.log('Final Total QTY Extracted: ' + totalCount);
console.log('Unique Rows Extracted: ' + items.length);

let outStr = 'const rawData = [\n';
items.forEach(i => {
  outStr += `  { model: "${i.model}", pn: "${i.pn}", name: "${i.nameDesc.replace(/"/g, "'")}", cat: "${i.cat}", src: "${i.src}", qty: ${i.qty}, price: ${i.price} },\n`;
});
outStr += '];\n';

fs.writeFileSync('C:/Users/user/Desktop/wpt-team/extracted_items.txt', outStr);
