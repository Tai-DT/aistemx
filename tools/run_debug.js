const fs = require('fs');
const entries = JSON.parse(fs.readFileSync('tools/debug_entries.json', 'utf8'));

const errCount = {};
const samples = {};

for (const f of entries) {
  if (!f.is_computable || !f.expression_js) continue;
  const scope = {};
  for (const inp of f.inputs || []) {
    scope[inp.symbol] = inp.default !== undefined ? inp.default : 2.0;
  }
  const keys = Object.keys(scope);
  const vals = Object.values(scope);
  try {
    const fn = new Function(...keys, 'return (' + f.expression_js + ');');
    const res = fn(...vals);
    if (typeof res !== 'number' || isNaN(res) || !isFinite(res)) {
      const key = 'NaN/Non-Finite';
      errCount[key] = (errCount[key] || 0) + 1;
      if (!samples[key]) samples[key] = { fid: f.formula_id, expr: f.expression_js, res };
    }
  } catch (e) {
    const key = e.message.split('\n')[0];
    errCount[key] = (errCount[key] || 0) + 1;
    if (!samples[key]) samples[key] = { fid: f.formula_id, expr: f.expression_js, err: e.message };
  }
}

console.log('Error counts:');
console.log(JSON.stringify(errCount, null, 2));
console.log('Samples:');
console.log(JSON.stringify(samples, null, 2));
