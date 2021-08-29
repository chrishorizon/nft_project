from flask import render_template, redirect, session, flash, request
from flask_app import app
# from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.forum import Forum

# bcrypt = Bcrypt(app)

@app.route('/forum')
def forum_page():
    if 'user_id' not in session:
        return redirect('/logout')
    logged_in_user = User.get_user_by_id({'id': session['user_id']})

    all_forum_posts = Forum.get_all()
    
    return render_template('forum.html', user = logged_in_user, all_forum_posts = all_forum_posts)

@app.route('/forum/create')
def create_forum():
    if 'user_id' not in session:
        return redirect('/')
    
    logged_in_user = User.get_user_by_id({'id': session['user_id']})
    
    return render_template('create_forum.html', user=logged_in_user)


@app.route('/create', methods=['POST'])
def create():
    if 'user_id' not in session:
        return redirect('/')

    if not Forum.valid_post(request.form):
        return redirect('/new/sighting')
    
    sighting = {
        'location': request.form['location'],
        'date_of_sighting': request.form['date_of_sighting'],
        'what_happened': request.form['what_happened'],
        'num_of_sas': request.form['num_of_sas'],
        'user_id': session['user_id']
    }

    Sighting.save(sighting)
    return redirect('/dashboard')


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