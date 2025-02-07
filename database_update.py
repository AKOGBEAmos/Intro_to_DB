import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="adm1n",
    password="Spydeon123",
    database="alx_book_store"
)

mycursor = mydb.cursor()

def add_author(name):
    query = "INSERT INTO Authors (author_name) VALUES (%s)"
    value = (name,)
    mycursor.execute(query, value)
    mydb.commit()  # Ensure changes are committed to the database

def add_book(title, author_id, price):
    query = "INSERT INTO Books (title, author_id, price) VALUES (%s, %s, %s)"
    values = (title, author_id, price)
    mycursor.execute(query, values)
    mydb.commit()

if __name__ == "__main__":
    add_author("J.K Rowling")
    add_author("Jean Pliya")
    add_author("Chimamanda Ngozi Adichie")

    try:
        add_book("Harry Potter", 1, 21)
        add_book("La secrétaire particulière", 2, 25)
    except mysql.connector.Error as e:
        print(f"Error: {e}")

