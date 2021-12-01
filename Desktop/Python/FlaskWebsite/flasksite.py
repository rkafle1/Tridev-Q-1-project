from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bb0f8c93f67318baff0c519a931f68bf'


posts = [
    {
        'author': 'Joshua Park',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Oct 20, 2021'
    },
    {
        'author': 'Heyjin Kim',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Oct 21, 2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    profile = []
    showmoviename = []
    description = []
    likes = []
    for i in range(0, len(posts)):
        profile.append(posts[i]['author'])
        showmoviename.append(posts[i]['title'])
        description.append(posts[i]['content'])
        likes.append(posts[i]['likes'])
        return render_template('home.html', profile = profile, showmoviename = showmoviename, description = description, likes = likes )


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # if the register website receives data:
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
