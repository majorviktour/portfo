from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        db.write(f'\n{email},{subject},{message}')
        print("Data saved:", email, subject, message)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        data = request.form.to_dict()
        print("Form submitted with data:", data)  # DEBUG print
        write_to_file(data)
        return redirect('/thankyou.html')
    except Exception as e:
        print("Error during form submission:", e)
        return 'Something went wrong. Try again later.'
