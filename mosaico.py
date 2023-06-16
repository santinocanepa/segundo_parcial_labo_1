import pygame 
import random

PURPURA_P = (113, 14, 255)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

def crear_mosaico(izq,arriba,ancho,alto):
    imagen_mosaico = pygame.image.load("segundo_parcial_labo_1\mosaico_buscaminas.jpg")
    imagen_mosaico = pygame.transform.scale(imagen_mosaico, (ancho, alto))
    rect_mosaico = imagen_mosaico.get_rect()
    rect_mosaico.x = izq
    rect_mosaico.y = arriba

    dict_mosaico = {}
    dict_mosaico["imagen"] = imagen_mosaico
    dict_mosaico["rect"] = rect_mosaico

    return dict_mosaico

def actualizar_pantalla(lista_mosaicos,pantalla):                   
    for mosaico in lista_mosaicos:
        pygame.draw.rect(pantalla, PURPURA_P,mosaico["rect"],)
        pantalla.blit(mosaico["imagen"], mosaico["rect"])

def crear_lista_mosaicos(cantidad):
    lista_mosaicos = []
    for i in range(cantidad):
        if cantidad > 0 and cantidad < 11:
            lista_mosaicos.append(crear_mosaico(0+(i*50),0,50,50))
        elif cantidad >9 and cantidad <21:
            lista_mosaicos.append(crear_mosaico(0+(i*50),0,50,50))
            lista_mosaicos.append(crear_mosaico(0+(i*50),50,50,50))
        elif cantidad >19 and cantidad <31:
            lista_mosaicos.append(crear_mosaico(0+(i*50),0,50,50))
            lista_mosaicos.append(crear_mosaico(0+(i*50),50,50,50))
            lista_mosaicos.append(crear_mosaico(0+(i*50),100,50,50))
        elif cantidad >29 and cantidad <41:
            lista_mosaicos.append(crear_mosaico(0+(i*50),0,50,50))
            lista_mosaicos.append(crear_mosaico(0+(i*50),50,50,50))
            lista_mosaicos.append(crear_mosaico(0+(i*50),100,50,50))
            lista_mosaicos.append(crear_mosaico(0+(i*50),150,50,50))
    return lista_mosaicos

"""def __init__(nombre_imagen,nombre_imagen_bomba,izq,arriba):
    dict_mosaico = {}
    dict_mosaico["visible"] = True
    dict_mosaico["bomba"] = False
    dict_mosaico["path_imagen"] = PATH_RECURSOS + nombre_imagen
    dict_mosaico["superficie"] = pygame.transform.scale(pygame.image.load(dict_mosaico["path_imagen"]),(50,50))
    dict_mosaico["superficie_bomba"] = pygame.transform.scale(pygame.image.load(PATH_RECURSOS + nombre_imagen_bomba),(500,500))
    dict_mosaico["rect"] = dict_mosaico["superficie"].get_rect()
    dict_mosaico["rect"].x = izq
    dict_mosaico["rect"].y = arriba"""