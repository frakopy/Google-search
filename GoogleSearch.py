#Este programa genera x numero de enlaces referentes a una palabara ingresada por teclado
from googlesearch import  search

consulta_google =  input('Ingresa un tema a buscar en google: ')

for enlace in search(consulta_google, start=0, pause=2):
    print(enlace)
