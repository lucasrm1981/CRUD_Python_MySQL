import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="db_python")
## Nome da base criada
mytable = mydb.cursor()
mytable .execute("CREATE TABLE alunos ("
                 "id_aluno INTEGER primary key auto_increment NOT NULL, "
                 "matricula INTEGER, "
                 "nome VARCHAR(100), "
                 "sobrenome VARCHAR(100), "
                 "idade INTEGER,"
                 "email VARCHAR(255),"
                 "rf FLOAT,"
                 "fil VARCHAR(255),"
                 "cpf VARCHAR(14),"
                 "esc VARCHAR(20),"
                 "enem_n INTEGER"
                 ")")