💜 HYPER TOOL

========================================

HYPER TOOL, Python ile geliştirilmiş çok amaçlı bir sistem araç setidir.
Sistem bilgisi, ağ araçları ve dosya yönetimi gibi birçok temel aracı tek bir panelde toplar.
-------------------------------------------------------------------
📁 PROJE YAPISI

HYPERTOOL/
│
├── main.py
└── modules/
├── systeminfo.py
├── ipscanner.py
├── portscanner.py
├── iplogger.py
├── network.py
├── filemanager.py
├── processviewer.py
└── cleaner.py
------------------------------------------------------------------
⚙️ ÖZELLİKLER
System Information Viewer
IP Scanner (GeoIP bilgi alma)
Port Scanner (TCP port tarama)
Network Tools (ping, DNS, internet kontrolü)
Process Viewer (çalışan işlemleri listeleme)
System Cleaner (geçici dosya temizleme)
File Manager (dosya gezici)
IP Logger (IP tespit aracı)
🚀 KURULUM (PC / UBUNTU)
Python kurulu olmalı (3.10+ önerilir)

Gerekli kütüphaneler:

pip install psutil requests

Programı çalıştır:

python3 main.py
------------------------------------------------------------------
📦 EXE YAPMA (WINDOWS)

pyinstaller --onefile --console main.py
------------------------------------------------------------------
📱 TERMUX KURULUM

Gerekli paketler:

pkg install python -y
pkg install clang -y
pip install psutil requests

Repo klonla:

git clone https://github.com/HyperProductions/HYPERTOOL-BETA.git

Çalıştır:

cd HYPERTOOL-BETA
python3 main.py
-------------------------------------------------------------------
🌐 TRACEROUTE GEREKSİNİMİ

Traceroute özelliğinin çalışması için sistemde traceroute aracı kurulu olmalıdır.

📱 TERMUX:
pkg install traceroute -y
🐧 UBUNTU / LINUX:
sudo apt update
sudo apt install traceroute -y
⚠️ NOT: Eğer traceroute kurulu değilse sistem otomatik olarak ping fallback kullanır.

💡 Neden önemli?

Çünkü:

Python kodu doğru olsa bile
dış sistem tool’u yoksa → hata verir
------------------------------------------------------------------
⚠️ UYARI

Bu araç yalnızca eğitim ve kişisel kullanım içindir.
Yetkisiz sistemlerde kullanım sorumluluğu kullanıcıya aittir.
-------------------------------------------------------------------
💜 HYPER TOOL v2
-------------------------------------------------------------------
