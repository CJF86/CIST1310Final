import sqlite3 as sql

DatabaseConnection = sql.connect("IceCreamDataBase.db")

print("Database created")

DatabaseConnection.execute("CREATE TABLE IceCream (IcecreamName TEXT, Flavor TEXT, Creator TEXT, CreatorPhone TEXT, Amount TEXT)")

print("Table Created")

DatabaseConnection.close()
