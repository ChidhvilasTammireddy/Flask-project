from flask import Flask, render_template, url_for,flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '7765da232d6c386950a8173f0cc3d79a'

posts=[
    {
        'Recipe_by': 'Tapan Kumar',
        'Title': 'Recipe1',
        'Date_posted':'09/15/20',
        'Recipe_name' : 'Dhokla',
        'Style' : 'Indian'
    },
    {
        'Recipe_by': 'Karan Racca',
        'Title': 'Recipe2',
        'Date_posted' : '09/15/20',
        'Recipe_name' : 'Manachurian Noodles',
        'Content': 'Recipe content',
        'Style' : 'Chinese'  
    },
    {
        'Recipe_by': 'Preetam Jain',
        'Title': 'Recipe3',
        'Date_posted' : '09/14/20',
        'Recipe_name' : 'Dal Chawal',
        'Content': 'Recipe content',
        'Style' : 'Indian'
    },
    {
        'Recipe_by': 'Kailash Nadkar',
        'Title': 'Recipe4',
        'Date_posted' : '09/10/20',
        'Recipe_name' : 'Hariyali Chicken Curry',
        'Content': 'Recipe content',
        'Style' : 'Indian'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title ='Register', form=form)


@app.route('/login')
def login():
    form= LoginForm()
    return render_template('login.html', title ='Login', form=form)




if __name__ =='__main__':
    app.run(debug=True)