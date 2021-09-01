from flask import Blueprint, render_template, request, flash

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
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 character.', category='error')
        elif len(firstname) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords dont match.', category='error')
        elif len(password1) < 7:
            flash('password must be at least 7characters.', category='error')
        else:
            #add user to database
            flash('account created!', category='success')

    return render_template("sign up.html")
