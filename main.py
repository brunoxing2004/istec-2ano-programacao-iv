import mysql.connector

baseDados = mysql.connector.connect(
  host="plesk2.server.highcloudservices.eu",
  user="nop",
  password="nop",
  database="nop"
)

conectorBD = baseDados.cursor()

conectorBD.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")