arq = open('texto.txt','r')
#lê o arquivo
print(arq.read())
#quantidade de caracteres
print(arq.tell())
#voltar para o inicio do arquivo
print(arq.seek(0,0))
#lendo ate um index selecionado
print(arq.read(20))