from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-12345'

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html', message="Welcome to your dashboard!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
