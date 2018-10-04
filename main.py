# -*- coding: utf-8 -*-
#Importando códigos auxiliares
from criaGrafo import *
from funcoesAuxiliares import *
from hierholzer import *

#
grafo,n,m = criaGrafo('exemplo1.txt')
#print(grafo)


#Verifica se o grafo é Euleriano
if(conexo(grafo, n) and grau(grafo)):
    print('\nTour Euleriano do grafo:')
    print(hierholzer(grafo, n ,m))
else:
    print('\nGrafo não Euleriano!')

#Fim do main