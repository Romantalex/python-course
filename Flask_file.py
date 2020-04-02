from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/News.html', methods = ['POST'])
def news():
    name = request.form['name']
    age = request.form['age']
    comment = request.form['comment']
    return render_template('News.html', name = name, age = age, comment = comment)

if __name__ == ("__main__"):
    app.run(debug = True)
