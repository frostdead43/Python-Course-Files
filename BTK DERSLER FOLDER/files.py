# dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amacla actigimizi belirtir

#'w'(Write): Yazma modu. Dosyayı konumda oluşturur.

# file = open("new file.txt","w")
# file.close()

#'a'(Append): Ekleme. Dosya konumda yoksa oluşturur.
#'x'(Create): Oluşturma. Dosya zaten varsa hata verir.
#'r'(Read): Okuma. Dosya konumda yoksa hata verir.