import pygame
import mosaico

pygame.init()
pygame.display.set_caption("buscaminas")
flag_correr = True

ALTURA_PANTALLA = 500
ANCHURA_PANTALLA = 500

PURPURA_P = (113, 14, 255)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

lista_mosaicos = mosaico.crear_lista_mosaicos(20)

pantalla = pygame.display.set_mode((ALTURA_PANTALLA, ANCHURA_PANTALLA))

while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in lista_mosaicos:
                if lista_mosaicos[0]["rect"].collidepoint(evento.pos):
                    print("CLICK sobre el mosaico")
                    break

    pantalla.fill(BLANCO)

    mosaico.actualizar_pantalla(lista_mosaicos,pantalla)

    pygame.display.flip()

pygame.quit()
