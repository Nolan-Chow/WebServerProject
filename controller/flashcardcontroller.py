import mysql.connector
from flask import render_template

def displaySets(userId):
    db = mysql.connector.connect(
            host="websvrdb.c6bigksqpjev.us-east-1.rds.amazonaws.com",
            user="web_app",
            passwd="NewPass123!"
        )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM testu.set WHERE frn_userId = %(userId)s", {'userId':userId})
    result = cursor.fetchall()
    return render_template("home.html", flashcardSets=result)

def displaySet(setId):
    query = "SELECT title, description, tags, GROUP_CONCAT(term), GROUP_CONCAT(definition) " \
          "FROM testu.set as a " \
          "INNER JOIN testu.flashcard as b " \
          "ON a.setId = b.frn_setId " \
          "WHERE setId = %(setId)s;"

    db = mysql.connector.connect(
            host="websvrdb.c6bigksqpjev.us-east-1.rds.amazonaws.com",
            user="web_app",
            passwd="NewPass123!"
        )
    cursor = db.cursor()
    cursor.execute(query, {'setId':setId})
    result = cursor.fetchall()
    return render_template("flashcard_set.html", flashcardSet=result[0])
