import sqlite3
import random
import string
import hashlib

def create_salt():
    letters=string.ascii_lowercase
    return''.join(random.choice(letters) for i in range(10))


def hash_str(string):
    return hashlib.md5(string.encode()).hexdigest()


def create_account(username, pw):
    salt = create_salt()
    username = str(username)
    pw_hash = hash_str(str(pw)+salt)

    connection=sqlite3.connect("db.db")
    cursor = connection.cursor()

    sql_str = f"""INSERT INTO user (username, salt, password_hash)
VALUES ('{username}', '{salt}', '{pw_hash}');
"""
    try:
        cursor.execute(sql_str)
        connection.commit()
        print("Account created!")
        return True
    except:
        print("User already exists")
        return False
    finally:
         connection.close()


def login(username, password):
    sql = f"""SELECT salt, password_hash
FROM user
WHERE username = '{username}'
"""
    connection=sqlite3.connect("db.db")
    cursor = connection.cursor()

    cursor.execute(sql)
    result = cursor.fetchone()

    if result is None:
        return False

    check_hash = hash_str(password+result[0])

    return check_hash == result[1]





def comment(fullname, email, comment):

    fullname = str(fullname)
    email= str(email)
    comment=str(comment)

    connection=sqlite3.connect("db.db")
    cursor = connection.cursor()

    sql_str = f"""INSERT INTO contact (Fullname, Email,comment)
VALUES ('{fullname}', '{email}', '{comment}');
"""
    cursor.execute(sql_str)
    connection.commit()

    connection.close()





