# from flask import Flask, request, render_template, jsonify
# import secrets
# import string
# import math
# import re

# app = Flask(__name__)

# # Function to generate a secure password
# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(secrets.choice(characters) for _ in range(length))
#     return password

# # Function to analyze password strength
# def analyze_password(password):
#     entropy = len(password) * math.log2(len(set(password)))
    
#     strength = "Weak"
#     if len(password) >= 8:
#         if re.search(r"\d", password) and re.search(r"[A-Z]", password) and re.search(r"[!@#$%^&*]", password):
#             strength = "Strong" if entropy > 50 else "Moderate"
    
#     return {"strength": strength, "entropy": round(entropy, 2)}

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/generate', methods=['GET'])
# def generate():
#     length = int(request.args.get('length', 12))
#     return jsonify({"password": generate_password(length)})

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     data = request.get_json()
#     password = data.get("password", "")
#     return jsonify(analyze_password(password))

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS  # Import CORS
import secrets
import string
import math
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to generate a secure password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Function to analyze password strength
def analyze_password(password):
    entropy = len(password) * math.log2(len(set(password)))
    
    strength = "Weak"
    if len(password) >= 8:
        if re.search(r"\d", password) and re.search(r"[A-Z]", password) and re.search(r"[!@#$%^&*]", password):
            strength = "Strong" if entropy > 50 else "Moderate"
    
    return {"strength": strength, "entropy": round(entropy, 2)}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate():
    length = int(request.args.get('length', 12))
    return jsonify({"password": generate_password(length)})

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    password = data.get("password", "")
    return jsonify(analyze_password(password))

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS  # Import CORS
import secrets
import string
import math
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to generate a secure password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Function to analyze password strength
def analyze_password(password):
    entropy = len(password) * math.log2(len(set(password)))
    
    strength = "Weak"
    if len(password) >= 8:
        if re.search(r"\d", password) and re.search(r"[A-Z]", password) and re.search(r"[!@#$%^&*]", password):
            strength = "Strong" if entropy > 50 else "Moderate"
    
    return {"strength": strength, "entropy": round(entropy, 2)}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate():
    length = int(request.args.get('length', 12))
    return jsonify({"password": generate_password(length)})

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    password = data.get("password", "")
    return jsonify(analyze_password(password))

if __name__ == '__main__':
    app.run(debug=True)
