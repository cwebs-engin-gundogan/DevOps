Devops Case
Genel notlar. 
Yaptığın her aşamayı commitlemeyi unutma. Attığın commitlere göre iş yapma şeklini değerlendireceğiz. 
AI vs herşeyi kullanabilirsin. Gidip başkasına da yaptırabilirsin ama iş yapış şekillerini soracağım :) Bu yüzden mümkün olduğu kadar sindirmeye çalış.
Kullandığın şifre vs şeylerin güçlü olmasına dikkat et. 

Görevler
1-Bu dizini bir git reposu haline getir. 
2- Docker compose dosyasına bir docker network'ü ekle
3- Docker compose dosyasına bir postgresql instance'ı ekle
4- Postgresql instance'ı data dizinini dışarıya host makine docker volume olarak çıkar. 
5- Postgresql instance'ın da users isimli bir tablo oluştur. İçeriği boş olabilir.
6- flask klasöründeki Flask uygulamasını docker container'i olarak build et. 
7- Flask uygulamasını compose kullanarak ayağa kaldır. (Compose dosyası eksik olabilir-Uygulamada hata alabilirsin. Compose dosyasını düzenle. Hatayı bir sonraki aşamada çözeceksin.)
8- Compose dosyasına bir docker networkü ekle . Compose dosyasındaki env değişkenlerini kullanarak docker networkü üzerinde db ile uygulama arasında bağlantı kur. 
9- postgresql instance'ını backup alacak bir bash script yaz. Script input alarak verdiğim dizine backup almalı.
10- html bir hello world sayfası oluştur. Bu hello world sayfasını dockerfile ile docker imajı build ederken imajın içerisine ekle. Nginx imajını çalıştırdığımızda bu hello world sayfasını görebilelim.
11- nginx imajına bir healthcheck ekle. Container ayağa kalktıktan 20 sn sonra healthy statusunu görebilelim.
12- docker compose up dediğim zaman 3 uygulama da sorunsuz ayağa kalkmalı.
