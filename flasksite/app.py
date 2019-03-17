from flask import Flask, redirect, url_for, request, render_template, make_response

app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello World'

# @app.route('/new')
# def new():
#     return 'new page'

# @app.route('/demo')
# def demo():
#     return 'This is the demo'

#   <> between that is a variable

# Dynamic routing
# @app.route('/profile/<int:id>')
# def profile(id):
#     return 'this profile belongs to %d' % id


# more dynamic stuff
# @app.route('/admin')
# def hello_admin():
#     return 'hello admin'

# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return 'hello guest %s' % guest

# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':
#         return redirect(url_for('hello_admin'))
    
#     else:
#         return redirect(url_for('hello_guest',guest = name))


#   more stuff
# @app.route('/success/<name>')
# def success(name):
#     return 'welcome %s' % name


# @app.route('/login', methods=['POST','GET'])
# def login():
#     if request.method == 'POST':
#         username = request.form['nm']
#         return redirect(url_for('success', name=username))
#     else:
#         username = request.args.get('nm')
#         return redirect(url_for('success', name=username))



#   Passing data from url to template
# @app.route('/welcome/<username>')
# def index(username):
#     #   looks for the hello.html file in the templates folder
#     return render_template('hello.html', name=username)


#   passing in js file
# @app.route('/')
# def index():
#     return render_template('hello.html')



#   Passing form data from one template to another
# @app.route('/')
# def student():
#     return render_template('student.html')

# @app.route('/result', methods=['POST','GET'])
# def result():
#     if request.method == 'POST':
#         result = request.form
#         return render_template('result.html', result=result)


#   Cookies
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods= ['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID',user)

        return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>hello' + name + '</h1>'


@app.route('/farts/<fartType>')
def fart(fartType):
        return render_template('fart.html', fartType= fartType)

if __name__ == '__main__':
    app.run()