import sqlite3

conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM

cursor = conn.cursor()

# create a table
# SQLite only supports five data types: null, integer, real, text and blob
sql = """CREATE TABLE albums (title text, artist text, release_date text, publisher text, media_type text)"""
cursor.execute(sql)


# insert some data
cursor.execute("""INSERT INTO albums VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')""")
#save data to database
conn.commit()


# insert multiple records using the more secure "?" method
albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TF\Kmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()


# update record in databse
sql = """UPDATE albums SET artist = 'John Doe' WHERE artist = 'Andy Hunter' """
cursor.execute(sql)
conn.commit()


# delete records from database
sql = """ DELETE FROM albums WHERE artist = 'John Doe'"""
cursor.execute(sql)
conn.commit()


# select records
sql = "SELECT * FROM albums WHERE artist=?"
cursor.execute(sql, [("Red")])
print(cursor.fetchall()) # or use fetchone() - to get only first record from result, fetchall() to get all records from result

print("\nHere's a listing of all the records in the table:\n")
for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
    print(row)

print("\nResults from a LIKE query:\n")
sql = """SELECT * FROM albums WHERE title LIKE 'The%'"""
cursor.execute(sql)
print(cursor.fetchall())