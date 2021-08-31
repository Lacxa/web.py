from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("Login.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>logout</P"


@auth.route('/sign up', methods=['GET', 'POST'] )
def sign_up():
    return render_template("sign up.html")
