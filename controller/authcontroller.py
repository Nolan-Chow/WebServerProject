import mysql.connector
from werkzeug.utils import redirect
from flask import render_template

def checkAuth(email, password):
    db = mysql.connector.connect(
            host="localhost",
            user="web_app",
            passwd="NewPass123!"
        )
    cursor = db.cursor()
    cursor.execute("SELECT password FROM testu.user WHERE email = %(email)s", {'email':email})
    result = cursor.fetchall()
    if result[0][0] == password:
        cursor.execute("SELECT userId FROM testu.user WHERE email = %(email)s", {'email':email})
        result = cursor.fetchall()
        return redirect("/home/" + str(result[0][0]))
    else:
        return render_template("index.html")
