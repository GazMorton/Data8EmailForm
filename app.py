from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        # Handle form submission
        email = request.form['email']

        # Process the email or perform any desired actions
        # (e.g., send an email, store in a database, etc.)


        return 'Thank you for your Email!'
    
    # Render the form template for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
