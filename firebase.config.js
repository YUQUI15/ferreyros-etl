// =============================================================================
// firebase.config.js — CONFIGURACIÓN DE FIREBASE
// =============================================================================
//
// INSTRUCCIONES (Solo 3 pasos, 2 minutos):
//
// 1. Ve a: https://console.firebase.google.com
// 2. Abre tu proyecto → Haz clic en el ícono ⚙️ (Config) → "Configuración del Proyecto"
// 3. En la sección "Tus apps", haz clic en "</>" (Web App).
//    Si no existe app web, haz clic en "Agregar app" → elige Web.
//    Copia el bloque "firebaseConfig" y reemplaza los valores debajo.
//
// TAMBIÉN DEBES HABILITAR FIRESTORE:
// → Console Firebase → Firestore Database → "Crear base de datos" → Modo de prueba → Listo
//
// =============================================================================

const FIREBASE_CONFIG = {
  apiKey:            "PEGA_TU_API_KEY_AQUI",
  authDomain:        "TU_PROYECTO.firebaseapp.com",
  projectId:         "TU_PROYECTO_ID",
  storageBucket:     "TU_PROYECTO.appspot.com",
  messagingSenderId: "PEGA_TU_SENDER_ID",
  appId:             "PEGA_TU_APP_ID"
};

// Si no tienes Firebase configurado todavía, la app funciona igualmente
// usando almacenamiento local del navegador (localStorage). 
// Cuando pegues los valores reales arriba, se activará Firestore automáticamente.
