# -*- coding: utf-8 -*-
import random

#Função que retorna o tour Euleriano
def hierholzer(grafo, n, quantArestas):
    
    #Vértice inicial escolhido arbitrariamente
    noInicial = random.randint(0,len(grafo)-1)
    
    #Armazena as arestas do tour Euleriano
    tour = []
    
    while(True):
        noAtual = noInicial
        
        #Coloca o vértice inicial como visitado
        visitados = [noInicial]
        
        while(True):
            
            #Visita o vértice adjacente (u)
            for u in range(n):
                if(grafo[noAtual,u] == 1):
                    
                    tour.append([noAtual,u]) #Coloca a aresta no tour
                    
                    #Marca a posição da aresta visitada com o -1
                    grafo[noAtual,u] = -1 
                    grafo[u,noAtual] = -1
                    
                    visitados.append(u) #Coloca o vértice que foi visitado em visitados
                    
                    noAtual = u #O próximo nó que será expandido será u
                    break;
            
            #Verifica se a busca completou um ciclo
            if(noInicial == noAtual):
                break;
        

        #Verifica se todas as arestas foram colicadas no tour
        if(quantArestas == len(tour)):
            return tour
        
        #Caso ainda não tenha retorna o tour ele irá escolher outro vértice que não foi visitado para começar novamente
        while(True):
            aux = random.randint(0,len(grafo)-1) #Vértice arbitrário
            if(aux not in visitados):
                noInicial = aux
                break;  
 #Fim da função

