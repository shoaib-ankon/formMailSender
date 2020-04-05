# importing libraries 
from flask import Flask,render_template, request 
from flask_mail import Mail, Message 

app = Flask(__name__) 
mail = Mail(app)

# configuration of mail 
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) 




@app.route("/") 
def index():
	return render_template('mail.html') 
	


@app.route("/submit", methods=['post']) 
def submitting():
	name = request.form.get('name')
	email = request.form.get('email')
	order = request.form.get('order')
	total = name+"\n"+email+"\n"+order
	msg = Message( 
				'Response arrived', 
				sender ='', 
				recipients = [''] 
				) 
	msg.body = total
	mail.send(msg) 
	return 'Thank You'	
	

if __name__ == '__main__': 
	app.run(debug = True) 
