// El Worker de rackers.app. La web son ficheros y los sirve Cloudflare tal
// cual; por aquí solo pasa lo que necesita algo más (ver `run_worker_first`
// en wrangler.jsonc):
//
// - Las entradas sin idioma —rackers.app/ y /privacidad/, /condiciones/ y
//   /soporte/—, que mandan a cada uno a su idioma con lo que solo sabe el
//   servidor: el país desde el que entra (ver idioma.js).
// - Los vídeos, para contestar a los trozos (ver rangos.js).
// - Las invitaciones a un torneo, rackers.app/t/{código}, y el archivo que le
//   dice a iOS que esos enlaces abren la app (ver torneo.js).

import { elegirIdioma, idiomasPedidos } from './idioma.js';
import { trozo } from './rangos.js';
import { RUTA_TORNEO, asociacion, paginaTorneo } from './torneo.js';

// Con su nombre en inglés también, que son los que van en App Store Connect
// (ver PAGINAS_EN_INGLES en build.py).
const ENTRADAS = {
  '/': '',
  '/privacidad/': 'privacidad', '/condiciones/': 'condiciones', '/soporte/': 'soporte',
  '/privacy/': 'privacidad', '/terms/': 'condiciones', '/support/': 'soporte',
};

export default {
  async fetch(peticion, env) {
    const url = new URL(peticion.url);
    if (url.pathname === '/.well-known/apple-app-site-association') return asociacion();
    const torneo = RUTA_TORNEO.exec(url.pathname);
    if (torneo) return paginaTorneo(peticion, env, url, torneo[1]);
    if (Object.hasOwn(ENTRADAS, url.pathname)) {
      const salto = await entrada(peticion, env, url, ENTRADAS[url.pathname]);
      if (salto) return salto;
    }
    return trozo(peticion, await env.ASSETS.fetch(peticion));
  },
};

// Si algo falla —falta idiomas.json, por ejemplo—, devuelve null y se sirve
// la portada de siempre, que elige con el mismo idioma.js pero sin país.
async function entrada(peticion, env, url, pagina) {
  const lista = await env.ASSETS.fetch(new URL('/static/idiomas.json', url));
  if (!lista.ok) return null;
  const hay = (await lista.json())[pagina];
  if (!hay?.length) return null;
  const galleta = /(?:^|;\s*)idioma=([^;]+)/.exec(peticion.headers.get('Cookie') || '');
  const idioma = elegirIdioma({
    hay,
    pedidos: idiomasPedidos(peticion.headers.get('Accept-Language')),
    pais: peticion.cf?.country || null,
    guardado: galleta ? decodeURIComponent(galleta[1]) : null,
  });
  const destino = new URL(`/${idioma}/${pagina ? pagina + '/' : ''}`, url);
  destino.search = url.search;
  return new Response(null, {
    status: 302,
    headers: {
      Location: destino.toString(),
      // Cada visita tiene su respuesta: que nadie la guarde para otro.
      'Cache-Control': 'private, no-store',
      Vary: 'Accept-Language, Cookie',
    },
  });
}
