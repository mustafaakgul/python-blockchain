# hashlib modülünü ekliyoruz
import hashlib

# Zaman ve tarih bilgileri modülünü ekliyoruz
from datetime import datetime

# Block adında bir sınıfı oluşturuyoruz.
class Block:

# Block sınıfına ait işlemlerin yapılacağı ana yönteme ait parametreler
  def __init__(self, sira, zaman_damgasi, bilgi, onceki_hash):
# block oluştururken gereken sıra bilgisi
    self.sira = sira
# block a ait zaman damgası
    self.zaman_damgasi = zaman_damgasi
# block a ait bilgi
    self.bilgi = bilgi
# block oluştutururken gereken önceki hash parametresi
    self.onceki_hash = onceki_hash
# karıştırılan bilgilerin ataması
    self.hash = self.karistir_hashle()

## Block sınıfına ait dönüş bilgilerinin bulundupu string değer
  def __str__(self):
## dönüş bilgisi formatı
    return '{}. blok'.format(self.sira)

# Block sınıfına gönderilen değerlerin karıştırılması için özel fonksiyon
  def karistir_hashle(self):
## hashlib altında bulunan sha256 ile karıştırma algoritması kullanılacak
    sha = hashlib.sha256()
## gönderilen değerler bir dizi haline getiriliyor
    dizi = (str(x) for x in (self.sira, self.zaman_damgasi, self.bilgi, self.onceki_hash))
# tüm değerler join ile birleştiriliyor encode işlemi Pyhton 3 için gerekli.
    sha.update(''.join(dizi).encode('utf-8'))

# karıştırılan değerler HEX stringleri haline getiriliyor ve cevap olarak gönderiliyor.
    return sha.hexdigest()

## Block un çalışmaıs için gerekli ilk işlem
def ilk_block():
  block = Block(sira=0,
    zaman_damgasi=datetime.now(),
    bilgi="İlk Block",
    onceki_hash="0")
  return block

## yeni block oluşturmak için özel fonksiyon. Önceki block ve karıştırılacak bilgi parametreleri gerekli
def yeni_block_olustur(onceki_block, bilgi=''):
## yeni block için sırayı 1 artırıyoruz
  sira_artir = onceki_block.sira + 1
# yeni block için Block sınıfına değerler gönderiliyor.
  yeni_block = Block(sira=sira_artir,
    zaman_damgasi=datetime.now(),
    bilgi='{}{}'.format(bilgi, sira_artir),
    onceki_hash=onceki_block.hash)
  return yeni_block

## uygulamanın çalıştırılması için fonksiyonumuz.
def test_et():
## zincir adında bir liste oluştururouz ve ilk block u çağırıyoruz
  zincir = [ilk_block()]
# zincirde var olan tek ve ilk block u onceki_block olarak tanımlıyoruz
  onceki_block = zincir[0]

## üretilecek block sayısını belirtiyoruz ve döngüye başlıyoruz
  for _ in range(0, 2):
# yeni block oluşturmak için fonksiyona gerekli parametreleri gönderiyoruz.
    yeni_block = yeni_block_olustur(onceki_block, bilgi='NEYI KARIŞIRACAK!')
## oluşturlan yeni block u zincir listesine ekliyoruz
    zincir.append(yeni_block)
# yeni block üretmek için oluşturulan yeni block u onceki_block olarak tanımlayıp sırayla devam ediyoruz.
    onceki_block = yeni_block
    print('{} zincire eklendi!'.format(yeni_block))
    print('Hash: {}\n'.format(yeni_block.hash))


test_et()