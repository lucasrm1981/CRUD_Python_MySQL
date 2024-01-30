import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",user="root",password="",database="db_python")

mycursor = mydb.cursor()
campoBusca = input("Deseja procurar por qual campo para Deletar?")
valorBusca = input("Digite o valor da Busca")
## LIKE %TEXTO ignora a parte inicial e completa com o valor digitado
## TEXTO% ignora a parte final
query = f"DELETE FROM alunos WHERE {campoBusca} LIKE '%{valorBusca}%'"
mycursor.execute(query)
mydb.commit()
if mycursor.rowcount>0:
    print(mycursor.rowcount, "Registro(s) Apagado.")
else:
    print("Nenhum Resultado encontrado")