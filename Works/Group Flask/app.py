from flask import Flask,render_template

app=Flask(__name__,template_folder='templates')

class News():
    def __init__(self,_id,_name,_date,_summary):
        self.id=_id
        self.name=_name
        self.date=_date
        self.summary=_summary


news=[]


@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add_delete')
def add_delete():
    return render_template('add_delete.html')


if __name__ == '__main__':
    app.run(debug=True)