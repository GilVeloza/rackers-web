// El Worker de rackers.app. La web son ficheros y los sirve Cloudflare tal
// cual; por aquí solo pasan los vídeos (ver `run_worker_first` en
// wrangler.jsonc) y solo para una cosa: contestar a los trozos.
//
// El iPhone no pide un vídeo entero de una vez: pide trozos con `Range`
// —primero `bytes=0-1`, para saber cuánto mide, y luego el resto— y si el
// servidor le devuelve el archivo entero con un 200 en vez del trozo con un
// 206, no lo reproduce y se queda en el cartel. Chrome y el Safari del Mac sí
// se apañan con el 200, así que en el ordenador todo se movía y en el iPhone
// ninguna raqueta. El servidor de ficheros de Workers no hace caso de `Range`,
// así que el trozo se corta aquí. Los vídeos son de un par de megas como
// mucho: se leen enteros y se recortan, sin más.

export default {
  async fetch(peticion, env) {
    return trozo(peticion, await env.ASSETS.fetch(peticion));
  },
};

export async function trozo(peticion, respuesta) {
  const rango = peticion.headers.get('Range');
  const siRango = peticion.headers.get('If-Range');
  // Sin trozo pedido, o si el fichero no está (404) o no ha cambiado (304),
  // va tal cual; solo se avisa de que se pueden pedir trozos. Igual si el
  // trozo va condicionado a una versión que ya no es la que hay: entonces
  // toca mandarlo entero.
  if (!rango || peticion.method !== 'GET' || respuesta.status !== 200
      || (siRango && siRango !== respuesta.headers.get('ETag'))) {
    return conCabeceras(respuesta.body, respuesta, respuesta.status);
  }
  // Un solo trozo: «bytes=inicio-fin», «bytes=inicio-» o «bytes=-los últimos».
  // Varios a la vez no los pide nadie; a esos se les manda el archivo entero,
  // que también vale.
  const pedido = /^bytes=(\d*)-(\d*)$/.exec(rango.trim());
  if (!pedido || (pedido[1] === '' && pedido[2] === '')) {
    return conCabeceras(respuesta.body, respuesta, 200);
  }
  const cuerpo = await respuesta.arrayBuffer();
  const total = cuerpo.byteLength;
  let inicio, fin;
  if (pedido[1] === '') {
    inicio = Math.max(0, total - Number(pedido[2]));
    fin = total - 1;
  } else {
    inicio = Number(pedido[1]);
    fin = pedido[2] === '' ? total - 1 : Math.min(Number(pedido[2]), total - 1);
  }
  if (inicio >= total || fin < inicio) {
    return new Response(null, { status: 416, headers: { 'Content-Range': `bytes */${total}` } });
  }
  return conCabeceras(cuerpo.slice(inicio, fin + 1), respuesta, 206, {
    'Content-Range': `bytes ${inicio}-${fin}/${total}`,
    'Content-Length': String(fin - inicio + 1),
  });
}

function conCabeceras(cuerpo, original, estado, extra = {}) {
  const cabeceras = new Headers(original.headers);
  cabeceras.set('Accept-Ranges', 'bytes');
  for (const [nombre, valor] of Object.entries(extra)) cabeceras.set(nombre, valor);
  return new Response(cuerpo, { status: estado, headers: cabeceras });
}
