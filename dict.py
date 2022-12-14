import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="database",
   user="postgres",
   password="hZEYeS4E"
)

print('''Welcome! PLease use of the commands to access and navigate
within the dicationary database. The available commands are:\n
list, add, delete, and quit''')

def read_dict(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_word(conn, word, translation):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def delete_word(conn, ID):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
def save_dict(conn):
    cur = conn.cursor()
    cur.execute("COMMIT;")
    cur.close()
def insert_word(C, word, translation):
    print("fake insert")

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").strip().lower()
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()
