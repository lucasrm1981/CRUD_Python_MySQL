import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",user="root",password="",database="db_python")

mycursor = mydb.cursor()
campoBusca = input("Deseja procurar por qual campo?")
valorBusca = input("Digite o valor da Busca")
## LIKE %TEXTO ignora a parte inicial e completa com o valor digitado
## TEXTO% ignora a parte final
query = f"SELECT * FROM alunos WHERE {campoBusca} LIKE '%{valorBusca}%'"
mycursor.execute(query)

myresult = mycursor.fetchall()
## Imprime como uma Lista Linha a Linha
for x in myresult:
    print(x)
print(myresult)## Imprime tudo de uma única Vez