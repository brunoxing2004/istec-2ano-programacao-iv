import mysql.connector

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

def updateDados():
  print("Hello from a function")

my_function()