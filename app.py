from flask import Flask, request, redirect
import smtplib

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Replace with your email and password
    your_email = 'your_email@example.com'
    your_password = 'your_password'

    # Set up the email content
    email_body = f"Name: {name}\nEmail: {email}\n\n{message}"

    # Send the email using smtplib
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(your_email, your_password)
        server.sendmail(your_email, your_email, email_body)
        server.quit()
    except Exception as e:
        print(f"Error: {e}")

    return redirect('/#contact')

if __name__ == '__main__':
    app.run(debug=True)
