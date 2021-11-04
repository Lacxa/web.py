from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("Login.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>wait when logout ...</P>"


@auth.route('/sign up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        Firstname = request.form.get('Firstname')
        Password1 = request.form.get('Password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 character.', category='error')
        elif len(Firstname) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(Password1) < 7:
            flash('password must be at least 7 characters.', category='error')
        elif Password1 != password2:
            flash('Passwords dont match.', category='error')
        else:
            flash('account created!', category='success')

    return render_template("sign up.html")
