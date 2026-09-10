# FERREYROS ETL PRO 3.0 ☁️ — Plataforma Web en la Nube

**URL Pública en Vercel · Firebase Firestore · Cero Instalación · Funciona en Cualquier Dispositivo**

---

## 🚀 Despliegue en 15 minutos (3 pasos)

### Paso 1: Subir este repositorio a GitHub

1. Ve a [github.com/new](https://github.com/new)
2. Crea un repositorio llamado `ferreyros-etl` (puede ser privado)
3. Arrastra todos estos archivos al repositorio o usa Git:

```bash
git init
git add .
git commit -m "feat: Plataforma ETL Ferreyros v3.0"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/ferreyros-etl.git
git push -u origin main
```

### Paso 2: Conectar a Vercel

1. Ve a [vercel.com](https://vercel.com) → "New Project"
2. Haz clic en "Import" junto a tu repositorio `ferreyros-etl`
3. Haz clic en **"Deploy"** (sin cambiar ninguna configuración)
4. En 30 segundos tendrás tu URL: `https://ferreyros-etl.vercel.app`

### Paso 3: Configurar Firebase (para historial en la nube)

1. Ve a [console.firebase.google.com](https://console.firebase.google.com)
2. Crea un proyecto (o abre el tuyo existente)
3. Haz clic en **"<> Agrega Firebase a tu app web"**
4. Copia el bloque `firebaseConfig = { ... }` que aparece
5. Edita el archivo `firebase.config.js` y pega tus valores
6. Activa **Firestore Database** → "Crear base de datos" → "Modo de prueba"
7. Haz commit y push → Vercel redespliega automáticamente

---

## ✅ Qué puede hacer esta plataforma

| Funcionalidad | Descripción |
|---|---|
| **Pipeline Maestro (1 Clic)** | Carga EWM + MB51 + Planilla + Transferencias → repara #N/A → genera 4 reportes Excel |
| **Dashboard Interactivo** | KPIs, gráficos de salud de stock, top quiebres, top consumos en tiempo real |
| **Motor ETL Universal** | Cruza CUALQUIER par de archivos (.xlsx, .csv) con Join visual + filtros + cálculos |
| **Historial en Firebase** | Cada corrida queda guardada. Accesible desde cualquier dispositivo |
| **Descarga en 1 Clic** | MACRO_CONSOLIDADO.xlsx, alertas, transferencias reparadas, consumo MB51 |

## 📁 Archivos del repositorio

```
ferreyros-etl/
├── index.html          → Aplicación completa (SPA, 700+ líneas)
├── firebase.config.js  → Tu configuración de Firebase (pega tus keys)
├── vercel.json         → Configuración de despliegue Vercel
└── README.md           → Esta guía
```

## 🔒 Privacidad

- Los archivos Excel se procesan **únicamente en la RAM del navegador** (SheetJS).
- **Ningún dato de inventario se envía a servidores externos**.
- Solo los KPIs resumidos (números agregados) se guardan en Firebase para el historial.

---

*FERREYROS ETL PRO 3.0 — Construido con FastAPI → Migrado a Vercel + Firebase + SheetJS*
