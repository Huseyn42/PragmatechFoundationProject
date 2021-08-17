from flask import Flask, render_template

app=Flask(__name__,template_folder='templates')

@app.route('/')
def main():
    return render_template('main.html')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/workers')
def workers():
    return render_template('workers.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)