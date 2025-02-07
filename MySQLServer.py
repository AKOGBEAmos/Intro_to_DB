import mysql.connector

 # Connect to MySQL server
mydb = mysql.connector.connect(host="localhost", user="adm1n", password="Spydeon123")

mycursor = mydb.cursor()

def create_database():
    try:

        # mycursor.execute("show databases")


        if mydb.is_connected():
            print("Database 'alx_book_store' created successfully!")
            mycursor.execute("USE alx_book_store")
            mycursor.execute("CREATE TABLE Authors (author_id INT PRIMARY KEY AUTO_INCREMENT,author_name VARCHAR(215) NOT NULL)")
            
            query2 = ("CREATE TABLE Books (book_id INT PRIMARY KEY AUTO_INCREMENT,title VARCHAR(130) NOT NULL,author_id INT NOT NULL,price DOUBLE NOT NULL,publication_date DATE)")
            
            query3 = ("CREATE TABLE Customers (customer_id INT PRIMARY KEY AUTO_INCREMENT,customer_name VARCHAR(215) NOT NULL,email VARCHAR(215) UNIQUE NOT NULL,address TEXT)")
            
            query4 =(""" CREATE TABLE Orders (
                order_id INT PRIMARY KEY AUTO_INCREMENT,
                customer_id INT NOT NULL,
                order_date DATE NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
            ) """)

            query5 = (""" CREATE TABLE Order_Details (
                order_detail_id INT PRIMARY KEY AUTO_INCREMENT,
                order_id INT NOT NULL,
                book_id INT NOT NULL,
                quantity DOUBLE NOT NULL,
                FOREIGN KEY (order_id) REFERENCES Orders(order_id),
                FOREIGN KEY (book_id) REFERENCES Books(book_id)
            ) """)

            mycursor.execute(query2)
            mycursor.execute(query3)
            mycursor.execute(query4)
            mycursor.execute(query5)

            # Insert some customer data
            sql = "INSERT INTO Customers (customer_name, email) VALUES (%s, %s)"
            val = ("John Doe", "john.doe@example.com")
            mycursor.execute(sql, val)
            mydb.commit()
           
    
    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and mycursor is not None:
            mycursor.close()
        if 'mydb' in locals() and mydb is not None and mydb.is_connected():
            mydb.close()
            print("MySQL connection closed.")

def add_author(author_name):
	mycursor.execute("INSERT INTO Authors (author_name) VALUES (author_name)")
     
def add_book(title, author):
	mycursor.execute("INSERT INTO Books (title, author_id) VALUES (title, author)")

if __name__ == "__main__":
    create_database()
    add_author("J.K Rowling")
    add_author("Jean Pliya")
    add_author("Chimamanda Ngozi Adechie")

    #Adding books
    add_book("Harry Potter", 1)
    add_book("La sécrétaire particulière", 2)