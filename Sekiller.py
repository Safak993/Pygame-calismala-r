import pygame

pygame.init()

Genislik =750
Yukseklik=600
pencere=pygame.display.set_mode([Genislik,Yukseklik])

Beyaz = [255,255,255]# kırmızı,yeşil,mavi = beyaz
Kirmizi = [255,0,0]
Mavi = [0,0,255]
pygame.draw.line(pencere,Kirmizi,(0,0),(150,250),100)
pygame.draw.line(pencere,Mavi,(250,250),(150,250),100)
durum = True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum = False
    pygame.display.update()
pygame.quit()