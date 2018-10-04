# -*- coding: utf-8 -*-
import numpy as np

#Entrada: um arquivo
def criaGrafo(arquivo):
    
    #Abertura do arquivo
    with open(arquivo) as f:
        texto = f.readlines()
    
    #Cada linha do arquivo pega as arestas  
    arestas = [linha.strip().split(' ')  for linha in texto] #Lista com todas as arestas, cada aresta é uma lista com dois elementos
    quntArestas = len(arestas) #Quantidade de arestas
    #print(arestas)
    
    #Para saber quantas cores foram utilizadas (cada cor do arquivo representa um vértice)
    cores = []
    for i in arestas:
        cores = cores + i
    cores = list(set(cores)) #Total de cores
    
    #Dicionário para armazenar os vértices
    #A chave do dicionário representa a cor (vértice) e o valor representa um número correspondente
    #Convertemos cada vértice em um número
    dicio = {}
    for i,x in enumerate(cores):
        dicio[x] = i
    #print(dicio)
    
    n = len(cores) #Quantidade de vértices
    
    #Criando uma matriz de adjacência nxn
    matriz = np.zeros((n,n))
    #print(matriz)
    
    #Preeenche a matriz de adjacência
    for aresta in arestas:
        a = aresta[0]
        b = aresta[1]
        matriz[dicio[a],dicio[b]] = 1
        matriz[dicio[b],dicio[a]] = 1
    
    return matriz, n, quntArestas
#Retorno: matriz (grafo), n (quantidade de vértices), quntArestas (quantidade de arestas)
