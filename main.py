from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def homePage():

    pageType = 'Controller' 
    btn1 = True

    if request.method == 'POST':
        if request.form['lamp'] == 'off':
            btn1 = True
            print "SP-1 ON"
        elif request.form['lamp'] == 'on':
            btn1 = False    
            print "SP-1 OFF"

    return render_template("2.html", pageType = pageType, btn1 = btn1)

if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)
