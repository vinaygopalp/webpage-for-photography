from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
 # create the extension
db = SQLAlchemy()
  
# create the app
app = Flask(__name__)
# mail = Mail(app)

 
# app.config.update(
#     MAIL_SERVER = 'smtp.gmail.com',
#     MAIL_PORT = '465',
#     MAIL_USE_SSL = True,

#     MAIL_USERNAME = 'photovphactory@gmail.com',
#     MAIL_PASSWORD = 'photovphactory@2003'
# )
# mail = Mail(app)
#configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/mini_project'
# # initialize the app with the extension
db.init_app(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    sub = db.Column(db.String(120), nullable=False)
    mes = db.Column(db.String(120), nullable=False)
@app.route("/contact", methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        
        
        email = request.form.get('email')
        sub = request.form.get('sub')
        mes = request.form.get('mes')
        entry = Contacts(name=name,email = email,sub = sub, mes = mes )
        db.session.add(entry)
        db.session.commit()
        # mail.send_message('New message from ' + name,
        #                   sender='photophactory@gmail.com',
        #                   recipients = email,
        #                   body = mes + "\n" + sub
        #                   )
    return render_template('contact.html')   

@app.route('/home')
def home():
    return render_template('index.html')   


@app.route('/more')
def more():
    return render_template('more.html')        
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')    
@app.route('/subscribe')
def subscription():
    return render_template('subscription.html')         
if __name__=="__main__":
    app.run(debug=True)