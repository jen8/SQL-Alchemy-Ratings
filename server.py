"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session)

# from flask import Flask (Flask, render_template, redirect, request, flash,
#                    session)



from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Rating, Movie, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined

import pdb
@app.route('/')
def filter():
    """Homepage."""
    # pdb.set_trace()

    q = request.args.get('q')

    return render_template("homepage.html")


@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)


# added a route to that shows the login form from register_form.html
@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup."""

    return render_template("register_form.html")    


   
# This route handles the submission of the login form.
@app.route("/register", methods=['POST'])
def process_form_new_user():

    email = request.form.get('email')
    password = request.form.get('password')
    age = int(request.form.get('age'))
    zipcode = int(request.form.get('zipcode'))

    """ take user name from form and check if it exists in database """
    
    new_user = User(email=email, password=password, age=age, zipcode=zipcode)

    # Adds the new_user info to database?
    db.session.add(new_user)
    db.session.commit()
    
    return redirect("/")


@app.route('/login_form', methods=['GET'])
def show_form():
    """Show form for existing users."""

    return render_template("log_in_form.html")




@app.route("/login", methods=['POST'])
def process_form_existing_user():
     """Process form for existing users."""
    email = request.form.get('email')
    password = request.form.get('password')
    #adding user_id aka email to Flask session
    
    

    #query for username in database
    current_user = User.query.filter(User.email == 'email') 

    #check if username matches passsword
    # if user_id[email] =  passsword:
        # if session['email'] = user.email and session['password'] = user.password:
        # if session['email'] = user.password
        if current_user = True:
        # flash('logged in!')
    return redirect('/')
    # return render_template('/')
        else:
    flash('Please try again, username/password not found!')
    return ("homepage.")

   


    """ take user name from form and check if it exists in database """
    
    new_user = User(email=email, password=password, age=age, zipcode=zipcode)

    # Adds the new_user info to database?
    
    db.session.commit()
    
    return redirect("/")

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()
