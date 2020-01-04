def db_create():
    conn = sqlite3.connect('capitals.sqlite')
    cur = conn.cursor()
    
    cur.execute('DROP TABLE IF EXISTS capitals')
    cur.execute('''
    CREATE TABLE "capitals"(
    "capital_id" TEXT,
    "state_id" TEXT,
    "note_id" TEXT)''')
    
    with open('directory/capitals.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)
            capital_id=row[0]
            state_id=row[1]
            cur.execute('''INSERT INTO capitals(
            capital_id, state_id) VALUES (?,?)''',
                        (capital_id, state_id))
            conn.commit()

def db_edit():
    conn = sqlite3.connect('capitals.sqlite')
    cur = conn.cursor()

    cur.execute('UPDATE capitals SET note_id= ? WHERE capital_id= ?', (args.been, args.city))
    conn.commit()
    conn.close()
    
def db_check():
    conn = sqlite3.connect('capitals.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT * FROM capitals WHERE capital_id= ?', (args.city,))
    print (cur.fetchone())
    conn.close()
