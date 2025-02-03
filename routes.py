from flask import Blueprint, render_template, request

router = Blueprint('router', __name__)

@router.route('/')
def hello_world():
    return render_template('waitlist.html')

@router.route('/dashboard', methods= ['GET', 'POST'])
def dashboard():
    LastName = request.form['Last_Name']
    FirstName = request.form['First_Name']
    Email = request.form['Email']
    return render_template('dashboard.html', Last_Name = LastName, First_Name=FirstName, Email=Email)

@router.route('/logout')
def logout():
    return render_template('waitlist.html')