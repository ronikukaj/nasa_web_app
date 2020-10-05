from ecovision import app

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Hello world</h1>"
