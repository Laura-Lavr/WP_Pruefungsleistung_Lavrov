from flask import Flask, request, jsonify, make_response, abort, render_template
from flask_sqlalchemy import SQLAlchemy
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 's9d78f6s9d8fhksahdfkj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passwordHash = db.Column(db.String(128), nullable=False)
    isAdmin = db.Column(db.Boolean, default=False)


def pos_by_email(email):
    return User.query.filter_by(email=email).first()


@app.route('/')
def index():
    return render_template('index.html')
 

@app.route('/users/login', methods=["POST"])
def login():
    data = request.json
    if "email" not in data.keys() or "passwordHash" not in data.keys():
        abort(400, "Required data missing!")
    user = pos_by_email(data['email'])
    if not user:
        abort(400, "User not found!")
    if user.passwordHash != data['passwordHash']:
        abort(401, "Password incorrect!")
    token = jwt.encode({"user_id": user.id}, app.config["SECRET_KEY"], algorithm="HS256")
    return make_response(jsonify({"token": token}), 200)


@app.route('/users/signup', methods=["POST"])
def signup():
    data = request.json
    if "username" not in data.keys() or "email" not in data.keys() or "password" not in data.keys():
        abort(400, "Required data missing!")
    if pos_by_email(data['email']):
        abort(400, "Email already exists!")
    new_user = User(
        username=data["username"],
        email=data["email"],
        passwordHash=data["password"]
    )
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({"message": "User created!"}), 201)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)
