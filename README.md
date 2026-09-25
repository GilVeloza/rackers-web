# La web de Rackers

La web de Rackers, [rackers.app](https://rackers.app), en los mismos idiomas
de la ficha de la tienda y con las mismas capturas: cada página enseña la app
en su idioma, porque las capturas salen de `design/app-store/idiomas/<idioma>/app/`.

La app está en otro repo, `racqer-ios`, y la web tira de él: las capturas, el
logo, los marcos y los vídeos se hacen allí, en `design/`, y las variantes por
país salen de sus reglas, en `tools/loc.py`. Así que para construir la web hace
falta tener ese repo clonado al lado de este, en `../padelapp`:

```sh
git clone git@github.com:GilVeloza/racqer-ios.git ../padelapp
```

Si está en otro sitio, se dice con `RACKERS_APP=/ruta/al/repo` delante de
cada comando.

```sh
python3 build.py             # todos los idiomas que tengan texto
python3 build.py es-ES ja    # solo esos
python3 build.py --servir    # y la sirve en localhost:8000
```

Sale en `publico/` (no se guarda en git: se rehace con un comando). Una
página por idioma, un `index.html` que manda a cada visitante al suyo, y
`static/` con el CSS, el JavaScript y las imágenes. Las capturas se reducen a
520 px y se guardan en JPEG, que si no la web pesa setenta megas; el logo y las
raquetas van en PNG porque necesitan el fondo transparente.

El texto vive en `textos/`, un archivo por idioma, y **no** sale del
catálogo de la app: es márketing, no interfaz. Las variantes por país no se
escriben dos veces —el inglés británico sale del americano, el mexicano del
español, el portugués de Portugal del de Brasil— con las mismas reglas que usa
`tools/loc.py`; lo único que se escribe a mano de cada variante son los precios
de su tienda, en `PARCHES`.

La página es el azul de Pista nocturna con la misma luz de la app: dos manchas
de color que respiran detrás de todo, tarjetas con un filo de luz arriba, el
botón lima con su latido, y cada bloque aparece al llegar con la pantalla.
Quien tenga puesto «reducir movimiento» no ve ninguna animación. No usa
librerías: el CSS y el JavaScript se escriben enteros en `build.py`, como los
SVG del logo.

En «Seis deportes» las seis raquetas pelotean en corro —el rally de
`design/video/rally.mp4`, en el repo de la app, 4,4 s en bucle, con la pelota que se convierte en la
de cada deporte según va hacia su raqueta— y debajo sale el nombre del deporte
que le da, cambiando en el mismo fotograma del golpe. Esos fotogramas están
medidos sobre el vídeo y apuntados en `GOLPES_RALLY`, en `build.py`: si
cambia el vídeo, hay que volver a medirlos. Quien pide menos movimiento ve el
primer fotograma y los seis nombres en fila.

Las raquetas sueltas, cada una girando en su cuadrado azul, ya no están en la
web pero siguen en `design/video/deportes/` del repo de la app: vídeos de 6 s en bucle, con las
mismas raquetas, materiales y luces que el rally. Las saca Blender:

```sh
# en el repo de la app
python3 design/video/deportes/build.py              # los seis, un par de minutos cada uno
python3 design/video/deportes/build.py padel tenis  # solo esos
```

La escena está en `design/video/deportes/escena.py`. Sin GPU cada fotograma
tarda medio minuto; con `RACKERS_MUESTRAS=32` delante tarda la mitad y a la
vista sale igual.

El hero es el peloteo: una raqueta a cada lado del móvil, que enseña Inicio en
el idioma de la página, y la pelota cruzando por delante de la pantalla. En
cada golpe, la raqueta que la recibe se convierte en el deporte siguiente
—pádel, tenis, pickleball, squash, tenis de mesa y bádminton— y la pelota, en
la suya: seis golpes y vuelta a empezar, un bucle sin costura de 4,8 s. El
móvil no va dentro del vídeo sino debajo, en la página, así que el vídeo vale
para todos los idiomas: lleva transparencia y deja libre el centro. Cada
navegador entiende la transparencia en un formato —Safari en HEVC y los demás
en WebM—, así que `build.py` saca los dos del máster en ProRes (el HEVC
con VideoToolbox, o sea en un Mac) y el JavaScript pone el que toca; hasta que
arranca, y para quien pide menos movimiento, se ve el primer fotograma. El
logotipo animado de la barra va igual: RACKERS se escribe, pasan las seis
raquetas por la Q y acaba en la Q en 3D.

```sh
# en el repo de la app
python3 design/video/peloteo/build.py web   # el del hero, unos minutos
python3 design/video/peloteo/build.py       # y además el horizontal y el vertical, para redes
python3 design/video/logo/build.py          # el logotipo: horizontal, vertical y vertical-cerca
```

Cada encuadre sale en MP4, sobre el azul, para verlo o subirlo tal cual, y en
MOV (ProRes 4444 con transparencia) para montarlo encima de otra cosa. Los MOV
no se guardan en git —pesan de 100 a 220 MB—, así que en un clon nuevo hay que
sacarlos con Blender antes de construir la web.

Cloudflare sirve `publico/` tal cual (ver `wrangler.jsonc`), salvo los
vídeos, que pasan antes por `rangos.js`. El iPhone pide los vídeos a trozos
(`Range`) y, si le llega el archivo entero en vez del trozo, no reproduce
ninguno: en el ordenador se mueve todo y en el móvil nada. El servidor de
ficheros de Cloudflare no hace caso de los trozos, así que los corta ese Worker.

## Publicar

```sh
python3 build.py
npx wrangler@4 deploy
```
