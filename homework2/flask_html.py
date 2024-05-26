from flask import Flask, render_template, request, redirect, session, url_for


app = Flask(__name__)
app.secret_key = "78dc6f1b096d06757909333ff5acfb515b83bb3745e49d2ed3c8d8ac945760e0"


@app.route('/')
def index():
    if 'username' in session:
        return render_template('exit.html')
    else:
        return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        return redirect(url_for('index'))
    return render_template('username_form.html')

@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)