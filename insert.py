import mysql.connector
import random
mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="db_python")
mycursor = mydb.cursor()

matricula = random.randint(10000,90000)
nome = input("Digite seu Nome: ")
sobrenome = input("Digite seu Sobrenome: ")
idade = int(input("Digite sua Idade: "))
email = input("Digite seu e-mail: ")
rf = float(input("Digite su Renda Familiar: R$ "))
fil = input("Digite sua Filiação: ")
cpf = input("Digite seu CPF: ")
esc = input("Digite sua escolaridade: ")
if idade>=16:
    enem_n = input("Digite sua nota do ENEM")
else:
    enem_n =0

sql = (f"INSERT INTO alunos (matricula,nome, sobrenome,idade,email,rf,fil,cpf,esc,enem_n) "
       f"VALUES ({matricula}, '{nome}','{sobrenome}',{idade},'{email}',"
       f"{rf},'{fil}','{cpf}','{esc}',{enem_n})")

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "Registro Inserido.") ## IMPRESSÃO DA QUANTIDADE DE LINHAS INSERIDAS