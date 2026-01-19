from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-registration', methods=['POST'])
def submit_registration():
    data = request.get_json()
    
    registration_data = {
        'online_registration': data.get('onlineRegistration'),
        'medical_clearance': data.get('medicalClearance'),
        'grade': data.get('grade'),
        'section': data.get('section')
    }
    
    # Here you can save to database or file
    print(f"Registration submitted: {registration_data}")
    
    return jsonify({
        'status': 'success',
        'message': 'Congratulations! You are part of the Yellow Tigers 🐯'
    })

if __name__ == '__main__':
    app.run(debug=True)