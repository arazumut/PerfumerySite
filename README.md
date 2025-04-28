# Parfüm Kozmetik Web Sitesi

Parfüm Kozmetik, kozmetik ürünleri satmak için tasarlanmış bir Django tabanlı e-ticaret web sitesidir. Kullanıcı dostu arayüzü ve modern tasarımı ile kozmetik ürünlerinin çevrimiçi satışı için ideal bir platformdur.

## Özellikler

- Responsive tasarım ile tüm cihazlarda düzgün görüntüleme
- Ürün kategorileri ve alt kategorileri
- Detaylı ürün sayfaları
- İstek listesi ve sepet özellikleri
- Kullanıcı hesap yönetimi
- Ödeme entegrasyonu
- Admin paneli ile kolay içerik yönetimi
- Blog sistemi
- İletişim formu

## Ekran Görüntüleri

![Ana Sayfa](/media/screenshots/home.png)
![Ürün Sayfası](/media/screenshots/product.png)
![Sepet](/media/screenshots/cart.png)

## Teknolojiler

- **Backend**: Django 4.2+
- **Frontend**: HTML5, CSS3, JavaScript, UIKit
- **Veritabanı**: SQLite (Geliştirme), PostgreSQL (Üretim için önerilen)
- **CSS Frameworkleri**: UIKit
- **Icon Kütüphanesi**: Font Awesome 5
- **Diğer**: jQuery, Swiper.js

## Kurulum

### Ön Koşullar

- Python 3.8+
- pip
- virtualenv (önerilen)
- Git

### Adımlar

1. Projeyi klonlayın:
```bash
git clone https://github.com/username/CosmeticWebSite.git
cd CosmeticWebSite/Cosmetic
```

2. Sanal ortam oluşturun ve etkinleştirin:
```bash
# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. Veritabanını oluşturun ve migrate edin:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Admin kullanıcısı oluşturun:
```bash
python manage.py createsuperuser
```

6. Statik dosyaları toplayın:
```bash
python manage.py collectstatic
```

7. Sunucuyu başlatın:
```bash
python manage.py runserver
```

8. Tarayıcınızda aşağıdaki URL'yi ziyaret edin:
```
http://127.0.0.1:8000/
```

## Kullanım

### Admin Paneli

Admin paneline erişmek için `http://127.0.0.1:8000/admin/` adresini ziyaret edin ve superuser kimlik bilgilerinizle giriş yapın. Bu panel aracılığıyla şunları yapabilirsiniz:

- Kategoriler ve ürünler ekleyebilir/düzenleyebilir/silebilirsiniz
- Blog yazıları yönetebilirsiniz
- Kullanıcıları ve siparişleri görüntüleyebilirsiniz
- Site ayarlarını değiştirebilirsiniz

### Ürün Yönetimi

1. Admin panelinde "ParfumeCosmetic" bölümüne gidin
2. "Kategoriler" veya "Ürünler" üzerine tıklayın
3. "Ekle" butonunu kullanarak yeni öğeler ekleyin
4. Mevcut öğeleri düzenlemek için üzerlerine tıklayın

## Üretim Ortamına Dağıtım

Projeyi üretim ortamında çalıştırmak için şu adımları izleyin:

1. `settings.py` içindeki `DEBUG` ayarını `False` olarak değiştirin
2. `SECRET_KEY` için güvenli bir değer ayarlayın (ortam değişkenleri kullanın)
3. `ALLOWED_HOSTS` ayarını güncelleyin
4. PostgreSQL veya MySQL gibi daha güçlü bir veritabanına geçmeyi düşünün
5. Statik dosyaları sunmak için Nginx veya Apache kullanın
6. HTTPS için SSL sertifikası kurun

## Yapı

Proje yapısı:

- `ParfumeCosmetic/`: Ana uygulama dizini
  - `models.py`: Veritabanı modelleri
  - `views.py`: Görünüm fonksiyonları
  - `urls.py`: URL yönlendiricileri
  - `admin.py`: Admin panel kayıtları
  - `templates/`: HTML şablonları
  - `static/`: Statik dosyalar (CSS, JS, resimler)
- `myproject/`: Proje yapılandırma dizini
  - `settings.py`: Proje ayarları
  - `urls.py`: Ana URL yönlendiricileri
- `media/`: Kullanıcı tarafından yüklenen dosyalar
- `static/`: Toplanmış statik dosyalar
- `manage.py`: Django yönetim betiği
- `requirements.txt`: Gerekli Python paketleri

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Feature branch'i oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inize push edin (`git push origin feature/amazing-feature`)
5. Bir Pull Request açın

