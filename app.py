from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for login page
@app.route('/')
def login():
    return render_template('login.html')

# Route to handle login form submission
@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']
    # Simple authentication check (this can be extended)
    if username == 'admin' and password == 'password':
        return redirect(url_for('feedback'))
    else:
        return "Invalid credentials. Please try again."

# Route for feedback form
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

# Route to handle feedback form submission
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    overall_rating = request.form['overall-rating']
    food_quality = request.form['food-quality']
    service_offering = request.form['service-offering']
    cleanliness = request.form['cleanliness']
    overall_impression = request.form['overall-impression']
    comments = request.form['comments']

    # Store feedback in a text file
    with open('data/feedback.txt', 'a') as f:
        f.write(f'Name: {name}\n')
        f.write(f'Overall Rating: {overall_rating}\n')
        f.write(f'Food Quality: {food_quality}\n')
        f.write(f'Service Offering: {service_offering}\n')
        f.write(f'Cleanliness: {cleanliness}\n')
        f.write(f'Overall Impression: {overall_impression}\n')
        f.write(f'Comments: {comments}\n\n')
    
    return "Thank you for your feedback!"

if __name__ == '__main__':
    app.run(debug=True)
