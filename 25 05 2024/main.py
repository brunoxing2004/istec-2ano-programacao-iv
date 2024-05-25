import mysql.connector
from datetime import datetime

# DB connection
conn = mysql.connector.connect(
host="100.88.190.56",
user="programacao-istec",
password="programacao-istec",
database="programacao-istec"
)
cursor = conn.cursor()

# Execute query
#cursor.execute("SELECT * FROM lavagem")

# Get data
#results = cursor.fetchall()
#for line in results:
#    print(line)

# Close connection
conn.close()


def criacaoLavagem(matricula, data_lavagem, tipo, estado):
    query = """
    INSERT INTO lavagem (matricula, data_lavagem, tipo, estado)
    VALUES (%s, %s, %s, %s)
    """

    #matricula = "92-22-MS"
    #data_lavagem = datetime(2024, 5, 25, 11, 30)
    #tipo = "Detalhado"
    #estado = "Agendado"
    valores = (matricula, data_lavagem, tipo, estado)
    cursor.execute(query, valores)
    conn.close()


def updateLavagem(id, matricula, data_lavagem, tipo, estado):
    query = """
    UPDATE lavagem
    SET matricula = %s, data_lavagem = %s, tipo = %s, estado = %s
    WHERE id = %s
    """
    valores = (id, matricula, data_lavagem, tipo, estado)
    cursor.execute(query, valores)
    conn.close()

updateLavagem(1, "92-22-MS", datetime(2024, 5, 25, 11, 30), "Detalhada", "Agendado")
print("Ok, update")