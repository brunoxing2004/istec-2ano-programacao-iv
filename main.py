import mysql.connector

baseDados = mysql.connector.connect(
  host="plesk2.server.highcloudservices.eu",
  user="base_dados_programacao",
  password="base_dados_programacao",
  database="base_dados_programacao"
)

conectorBD = baseDados.cursor()

conectorBD.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")