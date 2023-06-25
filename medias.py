"""
Programa: medias
Descrição: Este programa solicita suas notas deste curso, e retorna como está sua situação acadêmica.
Data : 24/06/2023
Versão: 0.0.1
"""

#Atribuição de variáveis



t1 = 0
t2 = 0
pf = 0

#Entrada de dados

t1 = float(input("Qual foi sua nota do teste 1? "))
t2 = float(input("Qual foi sua nota do teste 2? "))
pf = float(input("Qual foi sua nota na prova final? "))

#Processamento de dados
mf = ((t1 * 0.15) + (t2 * 0.15) + (pf * 0.7))
if (mf >= 6):
    print(f"Sua média final foi {mf}, você passou na disciplina.")

else:
    print(f"Sua média final foi {mf}, você não passou na disciplina.")
    
#Saida de dadaos