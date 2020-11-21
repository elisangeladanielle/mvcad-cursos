import psycopg2

conn = psycopg2.connect("dbname=curso_mvcad user=postgres password=esquecer host=localhost")

conn.autocommit = True

cursor = conn.cursor()

# cursor.execute("create database curso_mvcad")
#
# conn.commit()
# cursor.close()
# conn.close()
