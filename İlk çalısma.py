import pygame

pygame.init()

genislik_yukseklik=(450,360)

pencere=pygame.display.set_mode(genislik_yukseklik)

durum = True
while durum:
    for etkinlik in pygame.event.get():
        print(etkinlik)
    if etkinlik.type==pygame.QUIT: # çarpıya basınca kapan
        durum = False
pygame.quit()