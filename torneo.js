// rackers.app/t/{código}: la invitación a un torneo. Es el enlace que manda el
// organizador desde la app. Quien tiene Rackers ni la ve —iOS abre la app
// directamente, porque /t/* está en el apple-app-site-association de abajo— y
// quien no la tiene ve el torneo, el código y cómo apuntarse.
//
// El torneo lo da la API (racqer.app), que lo enseña sin cuenta: el código ya
// es la llave. Los textos los prepara build.py en static/torneo.json, sacando
// los de la app de su catálogo para que la web diga lo mismo que la app.

import { elegirIdioma, idiomasPedidos } from './idioma.js';

const API = 'https://racqer.app/v1/tournaments/code/';
const APP_ID = 'Y5WK4UKFTA.com.rackers.app';
export const RUTA_TORNEO = /^\/t\/([A-Za-z0-9-]{4,14})\/?$/;

/** Qué enlaces de rackers.app abren la app: solo los de torneo. La web sigue siendo web. */
export function asociacion() {
  return Response.json(
    { applinks: { details: [{ appIDs: [APP_ID], components: [{ '/': '/t/*' }] }] } },
    { headers: { 'Cache-Control': 'public, max-age=3600' } },
  );
}

export async function paginaTorneo(peticion, env, url, codigoCrudo) {
  const codigo = codigoCrudo.toUpperCase().replace(/[^A-Z0-9]/g, '');
  const datos = await env.ASSETS.fetch(new URL('/static/torneo.json', url));
  if (!datos.ok) return new Response('Rackers', { status: 503 });
  const { css, idiomas } = await datos.json();

  const galleta = /(?:^|;\s*)idioma=([^;]+)/.exec(peticion.headers.get('Cookie') || '');
  const idioma = elegirIdioma({
    hay: Object.keys(idiomas),
    pedidos: idiomasPedidos(peticion.headers.get('Accept-Language')),
    pais: peticion.cf?.country || null,
    guardado: galleta ? decodeURIComponent(galleta[1]) : null,
  });
  const t = idiomas[idioma];

  let torneo = null;
  try {
    // `API_TORNEOS` solo sirve para probar contra una API en local.
    const respuesta = await fetch((env.API_TORNEOS || API) + encodeURIComponent(codigo), { cf: { cacheTtl: 30 } });
    if (respuesta.ok) torneo = (await respuesta.json()).tournament;
  } catch {
    // Sin API se enseña lo mismo que con un código que no existe.
  }

  const cuerpo = torneo ? invitacion(t, torneo, codigo, peticion.cf?.timezone || 'UTC', idioma) : noExiste(t);
  const titulo = torneo ? `${escapar(torneo.name)} · Rackers` : 'Rackers';
  const resumen = torneo ? escapar(`${t.invitacion} · ${t.deportes[torneo.sport] || ''}`) : escapar(t.descripcion);
  const html = `<!doctype html>
<html lang="${idioma}" dir="${t.dir}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${titulo}</title>
<meta name="description" content="${resumen}">
<meta property="og:title" content="${titulo}">
<meta property="og:description" content="${resumen}">
<meta property="og:image" content="https://rackers.app/static/rackers.png">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#0B1322">
<link rel="icon" href="/static/rackers.png">
<link rel="stylesheet" href="${css}">
</head>
<body>
<div class="ambiente" aria-hidden="true"><span class="luz lima"></span><span class="luz rosa"></span></div>
<main class="invitacion">
  <a class="marca" href="/"><img src="/static/rackers-logotipo.png" width="201" height="34" alt="Rackers"></a>
  ${cuerpo}
</main>
</body>
</html>`;
  return new Response(html, {
    status: torneo ? 200 : 404,
    headers: {
      'Content-Type': 'text/html; charset=utf-8',
      'Cache-Control': 'private, max-age=30',
      Vary: 'Accept-Language, Cookie',
    },
  });
}

function invitacion(t, torneo, codigo, zona, idioma) {
  let fecha = '';
  try {
    fecha = new Intl.DateTimeFormat(idioma, { dateStyle: 'full', timeStyle: 'short', timeZone: zona })
      .format(new Date(torneo.date));
  } catch {
    fecha = new Date(torneo.date).toISOString().slice(0, 10);
  }
  const organiza = torneo.organizer.kind === 'organization'
    ? escapar(torneo.organizer.name)
    : escapar(t.organiza.replace('{nombre}', torneo.organizer.name));
  const verificado = torneo.organizer.is_verified ? ' <span class="verificado" aria-hidden="true">✓</span>' : '';
  const plazas = torneo.max_entrants ? `${torneo.entrants} / ${torneo.max_entrants}` : `${torneo.entrants}`;
  const datos = [
    `<li>${ICONOS.fecha}<span>${escapar(fecha)}</span></li>`,
    torneo.venue ? `<li>${ICONOS.pista}<span>${escapar(torneo.venue.name)}</span></li>` : '',
    `<li>${torneo.organizer.kind === 'organization' ? ICONOS.club : ICONOS.persona}<span>${organiza}${verificado}</span></li>`,
    `<li>${ICONOS.inscritos}<span>${escapar(t.inscritos)}: ${plazas}</span></li>`,
  ].join('');
  const abierto = torneo.status === 'open';
  const apuntarse = abierto
    ? `<p class="pasos">${escapar(t.pasos)}</p>
  <p class="codigo" aria-label="${escapar(t.codigo)}">${codigo}</p>
  ${t.boton}`
    : `<p class="pasos">${escapar(t.cerrado)}</p>`;
  return `<p class="antetitulo">${escapar(t.invitacion)}</p>
  <h1>${escapar(torneo.name)}</h1>
  <p class="tipo">${escapar(t.deportes[torneo.sport] || '')} · ${escapar(t.formatos[torneo.format] || '')} · ${escapar(torneo.visibility === 'public' ? t.publico : t.privado)}</p>
  <ul class="datos">${datos}</ul>
  ${apuntarse}`;
}

// Los iconos de cada dato, de trazo como los de la app.
const icono = (trazos) => `<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${trazos}</svg>`;
const ICONOS = {
  fecha: icono('<rect x="3.5" y="5" width="17" height="15" rx="3"/><path d="M3.5 10h17M8 3v4M16 3v4"/>'),
  pista: icono('<path d="M12 21s-6.5-5.6-6.5-11A6.5 6.5 0 0 1 18.5 10c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>'),
  persona: icono('<circle cx="12" cy="8" r="3.6"/><path d="M5 20a7 7 0 0 1 14 0"/>'),
  club: icono('<path d="M4 20V6l8-3 8 3v14M9 20v-5h6v5M8 9h.01M12 9h.01M16 9h.01"/>'),
  inscritos: icono('<circle cx="9" cy="8" r="3.3"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.8a3.3 3.3 0 0 1 0 6.4M18 14.3a6.5 6.5 0 0 1 3.5 5.7"/>'),
};

function noExiste(t) {
  return `<h1>${escapar(t.no_existe)}</h1>
  <p class="pasos"><a href="/">rackers.app</a></p>`;
}

function escapar(texto) {
  return String(texto ?? '').replace(/[&<>"']/g, (c) => (
    { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}
