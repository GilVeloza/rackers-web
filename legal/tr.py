"""Gizlilik, Koşullar ve Destek Türkçe."""

TEXTO = {
    "legal_volver": 'Ana sayfaya dön',
    "legal_actualizado": "8 Ekim 2026'da güncellendi",

    "privacidad_titulo": 'Gizlilik',
    "privacidad_entrada": 'Rackers oynamak için yapıldı, veri toplamak için değil. Burada açıkça yazıyor: ne saklanıyor, nerede ve nasıl silinir.',
    "privacidad_secciones": [
        ("Hesap olmadan iPhone'undan hiçbir şey çıkmaz", [
            "Rackers'ın tamamını hesap açmadan kullanabilirsin. Maçların, turnuvaların ve ayarların cihazda kalır ve hiçbir yere gitmez.",
            'Hesap üç şey yapar: iPhone ile saati aynı tutar, telefon değiştirirken hiçbir şey kaybolmaz ve arkadaşlarınla oynayabilirsin.',
        ]),
        ('Hesabın sakladıkları', [
            "Hesap, Apple ile Oturum Aç ile oluşturulur. Apple bize sabit bir tanımlayıcı, adını ve bir e-posta adresi verir; kendi adresini gizlersen bu, Apple'ın özel yönlendirme adresi olur.",
            "Bu tanımlayıcıyı, e-posta adresini, gösterdiğin adı ve seçtiğin @adı saklıyoruz. Bir de hesabını sildiğinde erişimin geri alınabilmesi için Apple'ın verdiği izni.",
        ]),
        ('Yedek', [
            'Hesapla birlikte uygulama içeriğini yükler: oyuncular, oyun günleri, maçlar, turnuvalar, analizler ve ayarlar.',
            'Maçlar, sen oynarken saatin ölçtüklerini de taşır: nabız, mesafe ve enerji. Maçla birlikte gider çünkü maça aittir.',
        ]),
        ("iPhone'undan asla çıkmayanlar", [
            'Dinlenme nabzı, değişkenlik ve uyku — « Bugün nasıl geliyorsun » kısmındakiler — Sağlık uygulamasından okunur ve cihazda kalır. Yüklenmez ve kimseyle paylaşılmaz.',
            "Sağlık izni istediğin zaman Ayarlar › Sağlık › Veri Erişimi'nden geri alınabilir, uygulama çalışmaya devam eder.",
        ]),
        ('Yapay zekâ antrenörü', [
            "Bir analiz istediğinde uygulama videodan kareler alır ve sunucumuz üzerinden OpenAI'ye gönderir; o da raporu döndürür.",
            "Videonun tamamından sunucuda hiçbir şey saklanmaz. Rapor uygulamaya döner ve senin yedeğinde kalır; yanında her gelişimin sessiz birkaç saniyesi de durur, böylece onları başka bir iPhone'da da görürsün. Analizi ya da hesabı sildiğinde bunlar da silinir.",
            'Kalan şey, kaç analiz istediğinin, hangi spor için ve ne kadar büyük olduğunun kaydı. Bu, kullanım sınırları ve maliyeti bilmek için.',
        ]),
        ('Abonelik', [
            'Pro, App Store üzerinden tahsil edilir. Kartını veya ödeme bilgilerini asla görmeyiz ve saklamayız.',
            'Aboneliğinin geçerli olup olmadığını bilmek için RevenueCat kullanıyoruz; hesap tanımlayıcın dışında hiçbir şeyle.',
        ]),
        ('Arkadaşlar ve aile', [
            'Biriyle bağlanırsan, bağlı olduğunuz ve paylaştığınız maçlar saklanır.',
            '@adın, başkalarının seni bulma şeklidir. İstediğin zaman değiştirebilirsin.',
        ]),
        ("Turnuvalar", [
            "Bir turnuva yayımlarsan adını, sporu, formatı, tarihi, sahayı ve düzenleyenin adını saklarız. Tablo ve sonuçlar iPhone'unda ve yedeğinde kalır.",
            "Herkese açık bir turnuvayı, hesabı olmasa bile herkes Turnuvalar › Herkese açık bölümünde ve rackers.app bağlantısında görebilir. Gizli bir turnuvaya yalnızca kodu ya da bağlantısı olan ulaşır.",
            "Hesabınla kaydolursan düzenleyen, kaydolduğun adı görür ve iPhone'una bildirim gelir. İstediğin zaman kaydını silebilirsin; birini engellediğinde aranızdaki kayıtlar kaldırılır.",
        ]),
        ('Nerede saklanıyor', [
            "Cloudflare'de, bir D1 veritabanında. Sunucu yalnızca uygulamaya yanıt verir ve yalnızca uygulamanın gönderdiğini tutar.",
            "Antrenörün video saniyeleri Cloudflare R2'de durur. Veritabanı da videolar da Avrupa Birliği'ndedir.",
        ]),
        ('Ne reklam ne takip', [
            'Reklam yok. Uygulamalar veya siteler arası takip yok. Hiçbir şey satılmaz ve üçüncü taraflara kendi kullanımları için verilmez.',
        ]),
        ('Her şeyi nasıl silersin', [
            'Uygulamada: Ayarlar › Hesap › Hesabı sil. Sana ait her şey sunucudan silinir ve Apple ile verdiğin erişim geri alınır.',
            'Yalnızca cihazda olanlar, uygulamayı sildiğinde gider.',
        ]),
        ('Küçükler', [
            'Rackers 13 yaşın altındaki çocuklar için tasarlanmadı ve bilerek verilerini toplamıyoruz.',
        ]),
        ('Bundan kim sorumlu', [
            "Bu verilerin işlenmesinden {responsable} sorumludur; kendi hesabına çalışır ve Rackers'ı kendi adıyla yayımlar. Verilerinle ilgili her şey için {correo} adresine yaz.",
            'Verilerini görme, düzeltme, silme, başka yere taşıma ve işlenmesine itiraz etme hakkın var. En hızlısı hesabı uygulamadan silmek, ama yazılı olarak istemeyi tercih edersen yaz, yapılır.',
        ]),
        ('Değişiklikler', [
            'Bunlardan biri değişirse, bu sayfada üstte tarihiyle birlikte yazacak.',
        ]),
    ],

    "condiciones_titulo": 'Kullanım koşulları',
    "condiciones_entrada": "Rackers'ı kullanmanın kuralları, kısa ve küçük punto olmadan.",
    "condiciones_secciones": [
        ('Bu nedir', [
            'Rackers; padel, tenis, pickleball, squash, masa tenisi ve badminton için bir skorbord ve maç defteridir, iPhone ve Apple Watch için.',
            'Kullanarak bu koşulları kabul edersin. Kabul etmiyorsan kullanma.',
        ]),
        ('Hesabın', [
            'Hesap senin ve onunla yapılanlardan sen sorumlusun. @ad kimseyi taklit edemez ve saldırgan olamaz; öyleyse geri alınabilir.',
            'Hakaret, taciz ve saldırgan içeriğe izin verilmez. Uygulamadan herhangi bir hesabı engelleyebilir veya bildirebilirsin; bildirimleri 24 saat içinde bir kişi inceler ve bu kuralları çiğneyen hesabını kaybeder.',
        ]),
        ('Pro ve ödemeler', [
            'Rackers ücretsizdir. Pro, satın almayı onayladığında App Store hesabına tahsil edilen bir aboneliktir.',
            'Dönem bitmeden en az 24 saat önce iptal etmezsen kendi kendine yenilenir. Cihazının Ayarlar › adın › Abonelikler kısmından yönetilir ve iptal edilir.',
            'İadeleri biz değil, Apple kendi kurallarına göre verir.',
        ]),
        ('Aile planı', [
            'Aile planı, ödeyene ve davet ettiği hesaplara, uygulamanın belirttiği sınıra kadar Pro verir. Ödeyen, istediği zaman herkesi çıkarabilir.',
        ]),
        ('Antrenör doktor değildir', [
            'Antrenörün raporu ve uygulamanın Sağlık verilerinle hesapladığı her şey yol göstericidir. Teşhis, tedavi ya da tıbbi veya profesyonel spor tavsiyesi değildir.',
            'Kendini kötü hissediyorsan veya sağlığınla ilgili şüphen varsa bir uzmana sor.',
        ]),
        ('Hizmet', [
            'Her şeyin çalışması için elimizden geleni yapıyoruz, ama uygulama ve sunucu olduğu gibi sunulur; kesintisiz erişilebilirlik veya hatasızlık garantisi yoktur.',
            'Sana önemli geleni sakla: yedek yardımcı olur ama kendi kopyalarının yerini tutmaz.',
        ]),
        ('Doğru kullanım', [
            'Hizmeti kırmaya çalışmak, ondan başka hesapların verilerini çekmek veya yasa dışı bir şey için kullanmak olmaz. Olursa hesap kapatılabilir.',
        ]),
        ('Değişiklikler', [
            'Bu koşullar değişebilir. Değişiklikler tarihleriyle burada yayımlanır ve uygulamayı kullanmaya devam etmek onları kabul etmek demektir.',
        ]),
    ],

    "soporte_titulo": 'Destek',
    "soporte_entrada": 'Bir şey çalışmıyor mu, yoksa daha iyi bir fikrin mi var? Yaz, cevaplayalım.',
    "soporte_correo_titulo": 'Bize yaz',
    "soporte_correo_nota": 'Bir insan cevaplıyor. Hataysa; ne yaptığını, ne beklediğini ve ne olduğunu anlat, hangi iPhone ve hangi iOS sürümü olduğunu da söyle: böylece daha çabuk düzelir.',
    "soporte_secciones": [
        ('Hesabını silmek', [
            'Uygulamada: Ayarlar › Hesap › Hesabı sil. Sana ait her şey sunucudan silinir ve Apple erişimi geri alınır. Bize yazman gerekmez.',
        ]),
        ('Abonelik', [
            'Pro, cihazının Ayarlar › adın › Abonelikler kısmından yönetilir ve iptal edilir. İadeleri Apple reportaproblem.apple.com üzerinden verir.',
        ]),
        ('Saat maçları görmüyor', [
            "Saat ve iPhone, birbirine yakınken ve ikisinde de uygulama açıkken güncellenir. Değilse Rackers'ı ikisinde de aç ve birkaç saniye bekle.",
            'Saat kendi başına çalışır: iPhone yanında olmadan bütün bir maçı sayabilirsin, sonra kendi aralarında anlaşırlar.',
        ]),
        ('Sağlık ve izinler', [
            "Nabzı ölçmek için Sağlık izni gerekir. Hayır dediysen Ayarlar › Sağlık › Veri Erişimi › Rackers'tan yeniden verebilirsin.",
            'Nabız bir antrenmanla ölçülür, bu yüzden sen oynarken saat uygulamada kalır.',
        ]),
        ('Antrenör', [
            "Video analizi Pro'ya aittir ve günlük ile aylık sınırı vardır. Bir analiz başarısız olursa sayılmaz.",
        ]),
    ],
}
