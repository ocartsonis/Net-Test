from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # This function will be called when someone visits /user/<username>
    return 'User %s' % username

if __name__ == '__main__':
    app.run()