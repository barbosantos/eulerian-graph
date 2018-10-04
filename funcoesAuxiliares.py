# -*- coding: utf-8 -*-
import numpy as np

#Função que calcula a DFS, ou seja, verifica se o grafo é conexo
def DFS(g,v,n,cor):
    cor[v] = 1
    for i in range(n):
        if(cor[i] == 0 and g[v,i] == 1):
            DFS(g,i,n,cor)
 #Fim da função
 
#Função para saber se o grafo é conexo
#Entrada: Um grafo (matriz adjacencia) e sua dimensão (quantidade de vértices)
def conexo(g,n):
    
    #Vetor de cor marca se um vértice foi visitado
    cor = []
    for i in range(n):
        cor.append(0)
    
    #A DFS é chamada em um vértice arbitrário, nesse caso é o vértice 0 (zero)
    DFS(g,0,n,cor)
    
    #Saber se todos os vértices foram coloridos (visitados)
    aux = 1
    for i in range(n):
        aux = aux and cor[i]
    
    #Se aux == 1 é porque todos os vértices foram coloridos (visitados)
    if(aux):
        print('O grafo é conexo!')
        return 1
    
    print('O grafo é desconexo!')
    return 0
 #Retorno: 1 para o grafo conexo, 0 caso contrário
 
#Função para calcular os graus de cada vértice
def grau(g):
    
    #Soma os graus de cada vértice
    #Soma os valores de cada linha (vértice), a soma representa o grau daquele vértice 
    graus = np.sum(g, axis=1) #Lista com os graus de cada vértice
    
    #Verifica se algum grau é ímpar
    for grau in graus:
        if(grau%2 == 1):
            print('Vértice com grau ímpar encontrado!')
            return 0
    
    print('O grafo tem todos os vértices com grau par!')
    return 1
 #Retorno: 0 se encontrar vértice com grau ímpar, 1 caso contrário
