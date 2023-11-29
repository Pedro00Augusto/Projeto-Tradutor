# -*- coding: utf-8 -*-
from deep_translator import GoogleTranslator
import pandas as pd

listaLinguas = GoogleTranslator().get_supported_languages(as_dict=True)
tabela_linguas = pd.DataFrame()

siglas = list(listaLinguas.values())
nomes = list(listaLinguas.keys())

tabela_linguas = pd.DataFrame(zip(nomes, siglas), columns=["Nomes","Siglas"]) 
i = int(input("Deseja começar o programa? Digite 1 para sim e 0 para não: "))

while i == 1:
    escolha = int(input("As linguas possuem códigos especiais, caso queira ver a lista de idiomas digite 1, caso contrário digite 0: "))
    
    if escolha == 1:
        print(tabela_linguas.to_string())
        
    
    linguaInicial = str(input("Escolha sua língua incial como escrito na lista acima: "))
    
    linguaFinal = str(input("Escolha sua língua final como escrito na lista acima: "))
    
    #Comando para limpar a tela
    print("\033[H\033[J", end="")
    
    texto = str(input("Digite seu texto aqui: "))
    texto = texto.title()
    
    tradutor = GoogleTranslator(source=linguaInicial, target=linguaFinal)
    
    print(tradutor.translate(texto))
    i = int(input("Deseja continuar o programa? Digite 1 para sim e 0 para não: "))
    print("\033[H\033[J", end="")
    
