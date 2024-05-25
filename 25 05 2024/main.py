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
#conn.close()


def criacaoLavagem(matricula, data_lavagem, tipo, estado):
    query = """
    INSERT INTO lavagem (matricula, data_lavagem, tipo, estado)
    VALUES (%s, %s, %s, %s)
    """
    valores = (matricula, data_lavagem, tipo, estado)
    cursor.execute(query, valores)
    conn.commit()
    conn.close()
    print("criacao OK")


def updateLavagem(id, matricula, data_lavagem, tipo, estado):
    query = """
    UPDATE lavagem
    SET matricula = %s, data_lavagem = %s, tipo = %s, estado = %s
    WHERE id = %s
    """
    valores = (matricula, data_lavagem, tipo, estado, id)
    cursor.execute(query, valores)
    conn.commit()
    conn.close()
    print("update OK")

#criacaoLavagem("92-22-AZ", datetime(2024, 5, 25, 11, 30), "Detalhada2", "estado1")
updateLavagem("92-22-MS", datetime(2024, 5, 25, 11, 30), "Detalhada", "Agendado", 7)
print("Ok, update")