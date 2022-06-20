# login test
from flask import Flask, Response, redirect, url_for, request, session, abort, render_template_string
from flask_login import LoginManager, UserMixin, \
    login_required, login_user, logout_user
from datetime import timedelta
from flask_wtf.csrf import CSRFProtect
from wtforms.form import Form

csrf = CSRFProtect()
WTF_CSRF_SECRET_KEY = 'asdfadsfad'
app = Flask(__name__)
app.debug = True
csrf.init_app(app)
# config
app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)
# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# silly user model
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "_secret"

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)


# create some users with ids 1 to 20
users = [User(id) for id in range(1, 21)]


# some protected url
@app.route('/')
@login_required
def home():
    return Response("Hello World!")


# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    form = Form()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form['username']
            password = request.form['password']
            id = 1
            user = User(id)
            login_user(user, True, timedelta(seconds=400))
            # return redirect(request.args.get("next"))
            return Response('login!')
    else:
        return render_template_string('''
        <form action="" method="post">
            <input type="hidden" name="csrf_token" value="{{ csrf_token() }}" />
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''', form=form)


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User(userid)


# @login_manager.user_loader
# def user_loader(token):
#     print("---user_loader, token=", token)
#     return load_token(token)
if __name__ == "__main__":
    app.run()
