"""Privacidad, Condiciones y Soporte en ms.

Lo que dice aquí tiene que casar con lo que hace el código: la copia de
seguridad sube partidos (con el pulso que midió el reloj), la salud de «Cómo
llegas hoy» no sale del iPhone y del vídeo del entrenador no se guarda nada.
Si eso cambia en la app o en el servidor, esto cambia también.
"""

TEXTO = {
    "legal_volver": "Kembali ke laman utama",
    "legal_actualizado": "Dikemas kini pada 25 September 2026",

    # --- Privacidad ---------------------------------------------------------
    "privacidad_titulo": "Privasi",
    "privacidad_entrada": "Rackers dibuat untuk bermain, bukan untuk mengumpul data. Di "
                          "sini dinyatakan dengan jelas apa yang disimpan, di mana dan "
                          "bagaimana memadamnya.",
    "privacidad_secciones": [
        ("Tanpa akaun, tiada apa keluar dari iPhone", [
            "Anda boleh menggunakan Rackers sepenuhnya tanpa membuka akaun. Perlawanan, "
            "kejohanan dan tetapan kekal dalam peranti anda dan tidak pergi ke mana-mana.",
            "Akaun berguna untuk tiga perkara: supaya iPhone dan jam tangan mempunyai "
            "perkara yang sama, supaya anda tidak kehilangan apa-apa apabila bertukar "
            "telefon, dan supaya boleh bermain dengan kawan.",
        ]),
        ("Apa yang disimpan oleh akaun", [
            "Akaun dibuka dengan Log Masuk dengan Apple. Apple memberi kami pengenal "
            "tetap, nama anda dan satu e-mel, iaitu alamat pemajuan peribadi Apple jika "
            "anda memilih untuk menyembunyikan alamat sendiri.",
            "Kami menyimpan pengenal itu, e-mel, nama yang anda tunjukkan dan @nama "
            "yang anda pilih. Juga kebenaran yang diberi Apple supaya akses boleh "
            "ditarik apabila anda memadam akaun.",
        ]),
        ("Salinan sandaran", [
            "Dengan akaun dihidupkan, aplikasi memuat naik kandungannya: pemain, hari "
            "permainan, perlawanan, kejohanan, analisis dan tetapan.",
            "Perlawanan membawa apa yang diukur oleh jam tangan semasa anda bermain: "
            "nadi, jarak dan tenaga. Ia pergi bersama perlawanan kerana ia milik "
            "perlawanan itu.",
        ]),
        ("Apa yang tidak keluar dari iPhone anda", [
            "Nadi rehat, kebolehubahan dan tidur — yang untuk «Keadaan anda hari ini» — "
            "dibaca daripada aplikasi Kesihatan dan kekal dalam peranti. Ia tidak "
            "dimuat naik ke pelayan dan tidak dikongsi dengan sesiapa.",
            "Kebenaran Kesihatan boleh ditarik bila-bila masa di Tetapan › Kesihatan › "
            "Akses Data, tanpa aplikasi berhenti berfungsi.",
        ]),
        ("Jurulatih AI", [
            "Apabila anda meminta analisis, aplikasi mengambil bingkai daripada video "
            "dan menghantarnya ke OpenAI melalui pelayan kami, yang memulangkan "
            "laporan.",
            "Tiada apa daripada video disimpan di pelayan. Laporan kembali ke aplikasi "
            "dan kekal dalam salinan anda.",
            "Yang kekal ialah rekod berapa analisis anda minta, daripada sukan apa dan "
            "sebesar mana. Ia untuk had penggunaan dan untuk tahu berapa kosnya.",
        ]),
        ("Langganan", [
            "Pro dicaj melalui App Store. Kami tidak melihat atau menyimpan kad anda "
            "atau butiran pembayaran anda pada bila-bila masa.",
            "Kami menggunakan RevenueCat untuk tahu sama ada langganan anda masih aktif, "
            "dengan pengenal akaun anda sahaja.",
        ]),
        ("Kawan dan keluarga", [
            "Jika anda berpaut dengan seseorang, disimpan bahawa anda berdua berpaut "
            "dan perlawanan yang dikongsi.",
            "@nama anda ialah cara orang lain menemui anda. Anda boleh mengubahnya "
            "bila-bila masa.",
        ]),
        ("Di mana ia disimpan", [
            "Di Cloudflare, dalam pangkalan data D1. Pelayan hanya menjawab aplikasi "
            "dan menyimpan apa yang aplikasi hantar kepadanya.",
        ]),
        ("Tiada iklan, tiada penjejakan", [
            "Tiada pengiklanan. Tiada penjejakan merentas aplikasi atau laman web. "
            "Tiada apa dijual atau diserahkan kepada pihak ketiga untuk kegunaan "
            "mereka sendiri.",
        ]),
        ("Cara memadam semuanya", [
            "Dari aplikasi: Tetapan › Akaun › Padam akaun. Semua milik anda dipadam "
            "daripada pelayan dan akses yang anda beri melalui Apple ditarik balik.",
            "Apa yang hanya ada dalam peranti hilang apabila anda memadam aplikasi.",
        ]),
        ("Kanak-kanak", [
            "Rackers tidak ditujukan kepada kanak-kanak bawah 13 tahun dan kami tidak "
            "meminta data daripada mereka dengan sengaja.",
        ]),
        ("Siapa yang bertanggungjawab", [
            "Pemprosesan data ini di bawah tanggungjawab {responsable}, yang bekerja "
            "sendiri dan menerbitkan Rackers atas namanya. Untuk apa-apa berkaitan data "
            "anda, tulis ke {correo}.",
            "Anda berhak melihat data anda, membetulkannya, memadamnya, membawanya ke "
            "tempat lain dan membantah pemprosesannya. Paling pantas ialah memadam "
            "akaun dari aplikasi, tetapi jika anda lebih suka memohon secara bertulis, "
            "tulis sahaja dan ia akan diuruskan.",
        ]),
        ("Perubahan", [
            "Jika ini berubah, ia diberitahu di halaman ini juga dengan tarikhnya di "
            "atas.",
        ]),
    ],

    # --- Condiciones --------------------------------------------------------
    "condiciones_titulo": "Terma penggunaan",
    "condiciones_entrada": "Peraturan menggunakan Rackers, ringkas dan tanpa cetakan "
                           "halus.",
    "condiciones_secciones": [
        ("Apa ini", [
            "Rackers ialah papan mata dan buku catatan perlawanan untuk padel, tenis, "
            "pickleball, skuasy, ping pong dan badminton, untuk iPhone dan Apple Watch.",
            "Dengan menggunakannya anda menerima terma ini. Jika anda tidak menerimanya, "
            "jangan gunakannya.",
        ]),
        ("Akaun anda", [
            "Akaun itu milik anda dan anda bertanggungjawab atas apa yang dilakukan "
            "dengannya. @nama tidak boleh menyamar sesiapa atau bersifat menghina; jika "
            "ya, ia boleh ditarik.",
            'Hinaan, gangguan dan kandungan yang menyinggung tidak diterima. Dalam aplikasi, anda boleh menyekat atau melaporkan mana-mana akaun; laporan disemak oleh manusia dalam masa 24 jam, dan sesiapa yang melanggar peraturan ini akan kehilangan akaunnya.',
        ]),
        ("Pro dan pembayaran", [
            "Rackers percuma. Pro ialah langganan yang dicaj melalui akaun App Store "
            "anda apabila anda mengesahkan pembelian.",
            "Ia diperbaharui sendiri melainkan anda membatalkannya sekurang-kurangnya "
            "24 jam sebelum tempoh tamat. Ia diuruskan dan dibatalkan di Tetapan "
            "peranti anda › nama anda › Langganan.",
            "Bayaran balik diberikan oleh Apple, bukan kami, mengikut peraturan mereka "
            "sendiri.",
        ]),
        ("Pelan keluarga", [
            "Pelan keluarga memberi Pro kepada yang membayarnya dan kepada akaun yang "
            "dijemputnya, sehingga had yang dinyatakan aplikasi. Yang membayar boleh "
            "mengeluarkan sesiapa bila-bila masa.",
        ]),
        ("Jurulatih bukan doktor", [
            "Laporan jurulatih dan apa yang aplikasi kira daripada data Kesihatan anda "
            "adalah panduan sahaja. Ia bukan diagnosis, bukan rawatan, dan bukan nasihat "
            "perubatan atau sukan profesional.",
            "Jika anda kurang sihat atau ada keraguan tentang kesihatan, tanya "
            "profesional.",
        ]),
        ("Perkhidmatan", [
            "Kami berusaha supaya semuanya berfungsi, tetapi aplikasi dan pelayan "
            "ditawarkan sebagaimana adanya, tanpa jaminan ia tersedia tanpa gangguan "
            "atau tiada kesilapan.",
            "Simpan apa yang penting bagi anda: salinan sandaran membantu, tetapi tidak "
            "menggantikan salinan anda sendiri.",
        ]),
        ("Penggunaan yang betul", [
            "Tidak dibenarkan cuba merosakkan perkhidmatan, mengambil data akaun orang "
            "lain atau menggunakannya untuk apa-apa yang menyalahi undang-undang. Jika "
            "berlaku, akaun boleh ditutup.",
        ]),
        ("Perubahan", [
            "Terma ini boleh berubah. Perubahan diterbitkan di sini dengan tarikhnya, "
            "dan terus menggunakan aplikasi bermakna anda menerimanya.",
        ]),
    ],

    # --- Soporte ------------------------------------------------------------
    "soporte_titulo": "Sokongan",
    "soporte_entrada": "Ada yang tak jalan, atau anda terfikir sesuatu yang lebih baik? "
                       "Tulis dan kami akan jawab.",
    "soporte_correo_titulo": "Tulis kepada kami",
    "soporte_correo_nota": "Yang menjawab ialah manusia. Jika ia pepijat, ceritakan apa "
                           "yang anda buat, apa yang anda jangka dan apa yang berlaku, "
                           "dan nyatakan iPhone mana dan versi iOS mana yang anda guna: "
                           "supaya ia lebih cepat dibaiki.",
    "soporte_secciones": [
        ("Memadam akaun anda", [
            "Dalam aplikasi: Tetapan › Akaun › Padam akaun. Semua milik anda dipadam "
            "daripada pelayan dan akses Apple ditarik balik. Tidak perlu menulis kepada "
            "kami.",
        ]),
        ("Langganan", [
            "Pro diuruskan dan dibatalkan di Tetapan peranti anda › nama anda › "
            "Langganan. Bayaran balik diberikan oleh Apple melalui "
            "reportaproblem.apple.com.",
        ]),
        ("Jam tangan tidak nampak perlawanan", [
            "Jam tangan dan iPhone menyegerakkan apabila berdekatan dan kedua-duanya "
            "membuka aplikasi. Jika tidak, buka Rackers pada kedua-duanya dan tunggu "
            "beberapa saat.",
            "Jam tangan berfungsi sendiri: anda boleh mengira mata sepanjang perlawanan "
            "tanpa iPhone bersama anda, nanti mereka akan segerak sendiri.",
        ]),
        ("Kesihatan dan kebenaran", [
            "Untuk mengukur nadi, Kesihatan perlu diberi kebenaran. Jika anda menolak, "
            "berikan semula di Tetapan › Kesihatan › Akses Data › Rackers.",
            "Nadi diukur sebagai satu latihan, jadi jam tangan kekal dalam aplikasi "
            "semasa anda bermain.",
        ]),
        ("Jurulatih", [
            "Analisis video ialah Pro dan mempunyai had penggunaan sehari dan sebulan. "
            "Jika analisis gagal, ia tidak dikira.",
        ]),
    ],
}
