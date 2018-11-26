
from os import scandir, getcwd
from os.path import abspath
import os

def ls(ruta = getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]

lista_arq = ls("C:\\Users\\rhprincipal\\Desktop\\pruebas ptyhon")


for base, dirs, files in os.walk("C:\\Users\\rhprincipal\\Desktop\\pruebas ptyhon"):	
  print (files)