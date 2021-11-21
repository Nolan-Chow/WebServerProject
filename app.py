from flask import Flask, request, render_template
from controller.authcontroller import checkAuth
from controller.flashcardcontroller import displaySets, displaySet

app = Flask(__name__)

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def authenticate_user():
    email = request.form.get("email")
    password = request.form.get("password")
    return checkAuth(email, password)

@app.route('/home/<int:userId>')
def get_home(userId):
    return displaySets(userId)

@app.route('/flashcards/<int:flashcardSetId>')
def get_set(flashcardSetId):
    return displaySet(flashcardSetId)


if __name__ == "__main__":
    app.run(debug=True)