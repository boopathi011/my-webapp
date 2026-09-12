from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from my web app</h1>" \
    "<a href='/about'>About</a>"
    

@app.route('/about')
def about():
    return "<p>Built Locally, pushed via github</p>"

if __name__ =='__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
