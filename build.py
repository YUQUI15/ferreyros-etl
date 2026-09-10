import sys

try:
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    target_html = '<section id="tab-content-etl" class="tab-pane hidden"><div class="text-center py-20 text-slate-500 font-bold">Módulo ETL Libre conservado en código base. Omitido en UI principal para foco en pipeline SAP.</div></section>'

    replacement_html = '''
  <!-- TAB 3: ETL LIBRE -->
  <section id="tab-content-etl" class="tab-pane hidden space-y-6">
    <div class="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm">
      <div class="border-b border-slate-200 dark:border-slate-800 pb-5 mb-6">
        <h2 class="text-xl font-black text-slate-800 dark:text-white flex items-center gap-2"><i data-lucide="git-merge" class="w-6 h-6 text-amber-500"></i> Motor ETL Libre (Universal)</h2>
        <p class="text-sm font-medium text-slate-500 dark:text-slate-400 mt-2">Herramienta flexible para cruzar cualquier par de archivos Excel (.xlsx, .csv). Sin restricciones de esquemas SAP.</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
        <!-- Archivo A -->
        <div class="bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 space-y-4">
          <h4 class="text-sm font-black text-amber-600 dark:text-amber-400">Archivo A (Origen Principal)</h4>
          <div class="drop-zone border-2 border-dashed border-slate-300 dark:border-slate-700 rounded-xl p-4 text-center cursor-pointer hover:border-amber-500 transition" onclick="document.getElementById('etl-input-a').click()">
            <div class="text-sm text-slate-500 mb-2 font-medium">Carga archivo .xlsx/.csv</div>
            <div id="etl-fname-a" class="text-xs font-bold text-emerald-600 dark:text-emerald-400 font-mono">Sin archivo</div>
            <input type="file" id="etl-input-a" class="hidden" accept=".xlsx,.xls,.csv" onchange="onEtlFileSelect(this,'a')">
          </div>
          <div><label class="text-xs font-bold block mb-1 text-slate-500 dark:text-slate-400">Hoja</label><select id="etl-sheet-a" onchange="onEtlSheetSelect('a')" class="w-full bg-white dark:bg-slate-900 border border-slate-300 dark:border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-800 dark:text-slate-200 focus:outline-none"><option value="">— Selecciona hoja —</option></select></div>
          <div><label class="text-xs font-bold block mb-1 text-slate-500 dark:text-slate-400">Columna Clave</label><select id="etl-key-a" class="w-full bg-white dark:bg-slate-900 border border-slate-300 dark:border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-800 dark:text-slate-200 focus:outline-none"><option>— Selecciona columna —</option></select></div>
        </div>

        <!-- Archivo B -->
        <div class="bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 space-y-4">
          <h4 class="text-sm font-black text-blue-600 dark:text-blue-400">Archivo B (Datos a Extraer)</h4>
          <div class="drop-zone border-2 border-dashed border-slate-300 dark:border-slate-700 rounded-xl p-4 text-center cursor-pointer hover:border-blue-500 transition" onclick="document.getElementById('etl-input-b').click()">
            <div class="text-sm text-slate-500 mb-2 font-medium">Carga archivo .xlsx/.csv</div>
            <div id="etl-fname-b" class="text-xs font-bold text-emerald-600 dark:text-emerald-400 font-mono">Sin archivo</div>
            <input type="file" id="etl-input-b" class="hidden" accept=".xlsx,.xls,.csv" onchange="onEtlFileSelect(this,'b')">
          </div>
          <div><label class="text-xs font-bold block mb-1 text-slate-500 dark:text-slate-400">Hoja</label><select id="etl-sheet-b" onchange="onEtlSheetSelect('b')" class="w-full bg-white dark:bg-slate-900 border border-slate-300 dark:border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-800 dark:text-slate-200 focus:outline-none"><option value="">— Selecciona hoja —</option></select></div>
          <div><label class="text-xs font-bold block mb-1 text-slate-500 dark:text-slate-400">Columna Clave</label><select id="etl-key-b" class="w-full bg-white dark:bg-slate-900 border border-slate-300 dark:border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-800 dark:text-slate-200 focus:outline-none"><option>— Selecciona columna —</option></select></div>
        </div>
      </div>

      <div class="bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 space-y-4 mb-6">
        <div class="grid grid-cols-1 sm:grid-cols-4 gap-4">
          <div><label class="text-xs font-bold block mb-1 text-slate-500 dark:text-slate-400">Tipo de Join</label><select id="etl-join-type" class="w-full bg-white dark:bg-slate-900 border border-slate-300 dark:border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-800 dark:text-slate-200 focus:outline-none"><option value="left">Left Join (Todo A + Coincidencias de B)</option><option value="inner">Inner Join (Solo Coincidencias)</option></select></div>
          <div><label class="text-xs font-bold block mb-1 text-slate-500 dark:text-slate-400">Filtro rápido</label><select id="etl-filter-col" class="w-full bg-white dark:bg-slate-900 border border-slate-300 dark:border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-800 dark:text-slate-200 focus:outline-none"><option value="">Sin filtro</option></select></div>
          <div><label class="text-xs font-bold block mb-1 text-slate-500 dark:text-slate-400">Contiene (Texto)</label><input type="text" id="etl-filter-val" placeholder="Ej: repuesto" class="w-full bg-white dark:bg-slate-900 border border-slate-300 dark:border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-800 dark:text-slate-200 focus:outline-none"></div>
          <div class="flex items-end">
            <button onclick="runEtl()" class="w-full py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-900 font-black shadow-lg shadow-amber-500/20 transition">CRUZAR Y DESCARGAR</button>
          </div>
        </div>
      </div>
    </div>
  </section>
'''

    if target_html in html:
        html = html.replace(target_html, replacement_html)
    else:
        print("Target HTML not found.")
        sys.exit(1)

    target_js = '</script>\n</body>'
    
    replacement_js = '''
// ============================================================================
// ETL LIBRE (UNIVERSAL) LOGIC
// ============================================================================
const ETL_SHEETS = { a: {}, b: {} };

async function onEtlFileSelect(input, side) {
  const file = input.files[0]; if (!file) return;
  document.getElementById(`etl-fname-${side}`).textContent = file.name;
  
  // Update button for loading
  const originalFname = document.getElementById(`etl-fname-${side}`).innerHTML;
  document.getElementById(`etl-fname-${side}`).innerHTML = "<span class='animate-pulse text-amber-500'>Leyendo archivo en memoria...</span>";
  
  setTimeout(async () => {
    try {
      const parsed = await parseFile(file);
      ETL_SHEETS[side] = parsed.sheets;
      const sheetSel = document.getElementById(`etl-sheet-${side}`);
      sheetSel.innerHTML = parsed.sheetNames.map(s => `<option value="${s}">${s}</option>`).join('');
      onEtlSheetSelect(side);
      document.getElementById(`etl-fname-${side}`).innerHTML = file.name;
    } catch (e) {
      alert("Error leyendo archivo: " + e.message);
      document.getElementById(`etl-fname-${side}`).innerHTML = "Error";
    }
  }, 50);
}

function onEtlSheetSelect(side) {
  const sheet = document.getElementById(`etl-sheet-${side}`).value;
  const rows = ETL_SHEETS[side][sheet] || [];
  const cols = rows.length > 0 ? Object.keys(rows[0]) : [];
  
  const keySel = document.getElementById(`etl-key-${side}`);
  keySel.innerHTML = cols.map(c => `<option value="${c}">${c}</option>`).join('');
  
  if (side === 'a') {
    document.getElementById('etl-filter-col').innerHTML = '<option value="">Sin filtro</option>' + cols.map(c => `<option value="${c}">${c}</option>`).join('');
  }
}

function runEtl() {
  const sA = document.getElementById('etl-sheet-a').value;
  const sB = document.getElementById('etl-sheet-b').value;
  const kA = document.getElementById('etl-key-a').value;
  const kB = document.getElementById('etl-key-b').value;
  const join = document.getElementById('etl-join-type').value;
  const fCol = document.getElementById('etl-filter-col').value;
  const fVal = document.getElementById('etl-filter-val').value.toLowerCase().trim();

  if (!ETL_SHEETS.a[sA]) return alert('Debes cargar y seleccionar una hoja del Archivo A.');
  
  let result = [...(ETL_SHEETS.a[sA] || [])];

  if (ETL_SHEETS.b[sB] && kA && kB) {
    const mapB = new Map();
    for (const r of ETL_SHEETS.b[sB]) { 
      mapB.set(normalizeKey(r[kB]), r); 
    }
    
    let joined = [];
    for (const rA of result) {
      const key = normalizeKey(rA[kA]);
      const rB = mapB.get(key);
      
      if (join === 'inner' && !rB) continue;
      
      const merged = { ...rA };
      if (rB) {
        for (const [bk, bv] of Object.entries(rB)) {
           const outK = (bk in merged) ? `${bk}_B` : bk;
           merged[outK] = bv;
        }
      }
      joined.push(merged);
    }
    result = joined;
  } else if(join === 'inner') {
    return alert('Para hacer Inner Join, necesitas obligatoriamente cargar el Archivo B y seleccionar sus columnas clave.');
  }

  // Filtrado post-cruce
  if (fCol && fVal) {
    result = result.filter(r => String(r[fCol] || '').toLowerCase().includes(fVal));
  }

  if(result.length === 0) return alert('El cruce o los filtros no generaron ningún resultado. La tabla quedó vacía.');
  
  const ts = new Date().toISOString().replace(/[:.]/g,'-').substring(0,19);
  
  const wb = XLSX.utils.book_new();
  const ws = XLSX.utils.json_to_sheet(result);
  XLSX.utils.book_append_sheet(wb, ws, 'Cruce_ETL');
  const wbout = XLSX.write(wb, {bookType:'xlsx', type:'array'});
  
  saveAs(new Blob([wbout], {type:"application/octet-stream"}), `Cruce_ETL_Libre_${ts}.xlsx`);
}
</script>
</body>
'''

    if target_js in html:
        html = html.replace(target_js, replacement_js)
    else:
        print("Target JS not found.")
        sys.exit(1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Successfully restored ETL Libre functionality.")

except Exception as e:
    print(f"Python Script Error: {e}")
    sys.exit(1)
