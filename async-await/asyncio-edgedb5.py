import edgedb
import datetime

conn = edgedb.connect("edgedb://edgedb@localhost/ambv")
conn.execute("""
	CREATE TYPE User {
		CREATE REQUIRED PROPERTY name -> str;
		CREATE PROPERTY date_of_birth -> cal::local_date;
	}
""")

conn.query("""
	INSERT User {
		name := <str>$name,
		date_of_birth := <cal::local_date>$dob
	}
""", name="Lukasz Langa", dob=datetime.date(1985, 3, 7))

conn.query("SELECT User {name, date_of_birth);")