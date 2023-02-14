arq2 = open('texto2.txt','w')# abrindo para escrever
arq2.write('será que a dopamina realmente desregula essas funções cerebrais?')
arq2.close()

'''arq2 = open('texto2.txt','r')# abrindo para ler
print(arq2.read())
arq2.close()
'''
arq2 = open('texto2.txt','a')# abrindo para adicionar
arq2.write('\nsim, de acordo com artigos cientificos, é possivel que essa desregulação afete essas funcionalidade\
do cerebro')
arq2.close()

arq2 = open('texto2.txt','r')# abrindo para ler
print(arq2.read())
arq2.close()
