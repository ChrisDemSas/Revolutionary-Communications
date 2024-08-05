from flask import Flask, render_template

app = Flask(__name__, static_folder = 'app/style', template_folder='app')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


if __name__ == '__main__':
    app.run(debug=True)