// Qué idioma ve quien entra por rackers.app/ (o por /privacidad/,
// /condiciones/ y /soporte/, que tampoco llevan idioma).
//
// Manda el navegador, no el país: quien tiene el móvil en inglés y vive en
// Portugal lee inglés. El país solo decide la variante —pt-PT o pt-BR, es-ES
// o es-MX, en-GB, en-US, en-AU o en-CA, fr-FR o fr-CA— y, si el navegador
// está en un idioma que no tenemos, el idioma que se habla allí. Y si alguien
// ya eligió uno en el selector, ese y ya está: lo guarda la galleta `idioma`.
//
// Lo usan el Worker (worker.js), que sabe el país, y la portada de respaldo
// que escribe build.py, que no lo sabe: build.py la mete tal cual en la
// página, quitándole los `export`. Por eso aquí no hay `import` ni nada que
// no entienda un navegador.

const LATINOAMERICA = 'MX AR BO CL CO CR CU DO EC GT HN NI PA PE PR PY SV UY VE US 419';

// Las variantes de cada idioma y en qué países va cada una. Donde no va
// ninguna, la de `defecto`.
export const VARIANTES = {
  pt: { paises: { 'pt-PT': 'PT AO MZ CV GW ST TL MO', 'pt-BR': 'BR' }, defecto: 'pt-BR' },
  es: { paises: { 'es-MX': LATINOAMERICA, 'es-ES': 'ES AD GQ' }, defecto: 'es-ES' },
  en: {
    paises: {
      'en-US': 'US PR GU VI AS MP UM',
      'en-CA': 'CA',
      'en-AU': 'AU NZ',
      'en-GB': 'GB IE IM JE GG GI MT CY IN PK BD LK NG GH KE UG TZ ZA ZW ZM BW NA MW SL ' +
               'SG MY HK BN FJ JM TT BB BS BZ GY',
    },
    defecto: 'en-US',
  },
  fr: { paises: { 'fr-CA': 'CA', 'fr-FR': 'FR BE CH LU MC' }, defecto: 'fr-FR' },
  // El chino va por escritura, no por acento: si el navegador la dice
  // (zh-Hant, zh-TW…), manda eso aunque esté en otro país.
  zh: { paises: { 'zh-Hant': 'TW HK MO', 'zh-Hans': 'CN SG MY' }, defecto: 'zh-Hans', etiquetaPrimero: true },
};

// Si el navegador está en un idioma que no tenemos: el del país.
const POR_PAIS = {
  'es-ES': 'ES', 'es-MX': LATINOAMERICA.replace(' US', ''), 'ca': 'AD',
  'pt-PT': 'PT AO MZ CV GW ST TL', 'pt-BR': 'BR',
  'fr-FR': 'FR BE LU MC SN CI ML BF NE TG BJ GN CM GA CG CD MG HT RE GP MQ GF NC PF DJ TD CF BI KM',
  'en-US': 'US', 'en-CA': 'CA', 'en-AU': 'AU NZ',
  'en-GB': 'GB IE MT CY NG GH KE UG TZ ZA ZW ZM BW NA MW SL SG JM TT LK ET RW LR GM',
  'de': 'DE AT CH LI', 'it': 'IT SM VA', 'nl': 'NL SR', 'da': 'DK GL FO', 'sv': 'SE AX',
  'nb': 'NO SJ', 'fi': 'FI', 'pl': 'PL', 'cs': 'CZ', 'sk': 'SK', 'sl': 'SI', 'hr': 'HR BA',
  'hu': 'HU', 'ro': 'RO MD', 'el': 'GR', 'tr': 'TR', 'uk': 'UA',
  'ru': 'RU BY KZ KG TJ UZ TM AM AZ GE',
  'ar': 'SA AE EG MA DZ TN LY JO LB SY IQ KW QA BH OM YE SD PS MR SO',
  'he': 'IL', 'hi': 'IN NP', 'bn': 'BD', 'ur': 'PK', 'th': 'TH', 'vi': 'VN', 'id': 'ID',
  'ms': 'MY BN', 'fil': 'PH', 'ja': 'JP', 'ko': 'KR', 'zh-Hans': 'CN', 'zh-Hant': 'TW HK MO',
};

// Los códigos viejos o hermanos que mandan algunos navegadores.
const ALIAS = { iw: 'he', in: 'id', no: 'nb', nn: 'nb', tl: 'fil' };

const base = (codigo) => codigo.split('-')[0].toLowerCase();

// «pt-PT» → { base: 'pt', region: 'PT' }; «zh-Hant-TW» → escritura 'hant'.
function partes(etiqueta) {
  const trozos = etiqueta.replace(/_/g, '-').split('-');
  const primera = trozos[0].toLowerCase();
  let region = null, escritura = null;
  for (const trozo of trozos.slice(1)) {
    if (/^[a-z]{4}$/i.test(trozo)) escritura = trozo.toLowerCase();
    else if (/^([a-z]{2}|\d{3})$/i.test(trozo)) region = trozo.toUpperCase();
  }
  return { base: ALIAS[primera] || primera, region, escritura };
}

function enLista(lista, lugar) {
  return lugar ? lista.split(' ').includes(lugar) : false;
}

function variante(reglas, candidatos, { pais, region, escritura }) {
  if (escritura) {
    const porEscritura = candidatos.find((c) => c.toLowerCase().endsWith('-' + escritura));
    if (porEscritura) return porEscritura;
  }
  const lugares = reglas.etiquetaPrimero ? [region, pais] : [pais, region];
  for (const lugar of lugares) {
    for (const [codigo, paises] of Object.entries(reglas.paises)) {
      if (candidatos.includes(codigo) && enLista(paises, lugar)) return codigo;
    }
  }
  return candidatos.includes(reglas.defecto) ? reglas.defecto : candidatos[0];
}

// La cabecera Accept-Language, en orden de preferencia: «pt-PT,pt;q=0.9,en;q=0.8».
export function idiomasPedidos(cabecera) {
  return (cabecera || '')
    .split(',')
    .map((trozo, orden) => {
      const [etiqueta, ...params] = trozo.trim().split(';');
      const q = params.map((p) => /^\s*q=([\d.]+)/.exec(p)).find(Boolean);
      return { etiqueta: etiqueta.trim(), q: q ? Number(q[1]) : 1, orden };
    })
    .filter((p) => p.etiqueta && p.etiqueta !== '*' && p.q > 0)
    .sort((a, b) => b.q - a.q || a.orden - b.orden)
    .map((p) => p.etiqueta);
}

// hay: los códigos que tiene la página; pedidos: los del navegador, en orden;
// pais: el de Cloudflare («PT»), o null; guardado: la galleta, o null.
export function elegirIdioma({ hay, pedidos = [], pais = null, guardado = null }) {
  if (guardado && hay.includes(guardado)) return guardado;
  pais = /^[A-Z]{2}$/.test(pais || '') ? pais : null;
  const lugar = { pais };
  for (const pedido of pedidos) {
    const { base: suya, region, escritura } = partes(pedido);
    const candidatos = hay.filter((c) => base(c) === suya);
    if (candidatos.length === 1) return candidatos[0];
    if (candidatos.length > 1) {
      const reglas = VARIANTES[suya] || { paises: {}, defecto: candidatos[0] };
      return variante(reglas, candidatos, { ...lugar, region, escritura });
    }
  }
  // Ninguno de los del navegador: el del país, o su variante más cercana.
  for (const [codigo, paises] of Object.entries(POR_PAIS)) {
    if (!enLista(paises, pais)) continue;
    if (hay.includes(codigo)) return codigo;
    const candidatos = hay.filter((c) => base(c) === base(codigo));
    if (candidatos.length) return variante(VARIANTES[base(codigo)] || { paises: {}, defecto: candidatos[0] }, candidatos, lugar);
  }
  return hay.includes('en-US') ? 'en-US' : hay[0];
}
