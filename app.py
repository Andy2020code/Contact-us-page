from flask import Flask, render_template, request
from flask_mail import Mail, Message

app  = Flask(__name__)

# Configure Flask_Mail to work with GMail

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'email@email.com'
app.config['MAIL_PASSWORD'] = 'lesssecuregmailpasssword'
app.config['MAIL_DEFAULT_SENDER'] = 'email@email.com'

mail = Mail(app)


# Configure Routes for IMG/CSS/JAVASCRIPT

@app.route('/IMG/<filename>')
def serve_images(filename):
    return app.send_static_file('IMG/' + filename)

@app.route('/css/<filename>')
def serve_css(filename):
    return app.send_static_file('css/' + filename)

@app.route('/js/<filename>')
def serve_js(filename):
    return app.send_static_file('js/' + filename)


# Configure server page routes

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    data = request.json # Get JSON data from the javascript file

    # Process the data
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Send email
    try:
        send_email(name, email, message)
        print("E-mail sent successfully!")
    except Exception as e:
        print(f"Error Sending E-mail: {e}")
    return 'OK', 200 # Return simple response to the client


def send_email(name, email, message):
    recipient_email = email@email.com

    # E-mail body set-up
    subject = f"New Contact Form Submition from {name}"
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    msg = Message(subject, recipients=[recipient_email])
    msg.body = body

    try:
        mail.send(msg)
    except Exception as e:
        print(f"Error sending e-mail: {e}")

# Configure Server hosting 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True, use_reloader=True)