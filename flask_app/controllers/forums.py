from flask import render_template, redirect, session, flash, request
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User

# bcrypt = Bcrypt(app)

@app.route('/forum')
def forum_page():
    if 'user_id' not in session:
        return redirect('/logout')
    logged_in_user = User.get_user_by_id({'id': session['user_id']})
    
    return render_template('forum.html', user = logged_in_user)

# @app.route('/login', methods=['POST'])
# def login():
#     user = User.valid_login(request.form)
#     if not user:
#         return redirect('/')
#     session['user_id'] = user.id
#     return redirect('/home')


# @app.route('/register')
# def create_account():
#     return render_template('register.html')


# @app.route('/register/account',methods=['POST'])
# def register():
#     if not User.valid_registration(request.form):
#         return redirect('/register')
#     data ={ 
#         "username": request.form['username'],
#         # "first_name": request.form['first_name'],
#         # "last_name": request.form['last_name'],
#         "email": request.form['email'],
#         "password": bcrypt.generate_password_hash(request.form['password'])
#     }
#     id = User.save(data)
#     session['user_id'] = id

#     return redirect('/home')