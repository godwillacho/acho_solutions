from flask import Flask, render_template
import os

# Set correct paths for UI files
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, '../ui/templates')  # UI templates path
STATIC_DIR = os.path.join(BASE_DIR, '../ui/static')  # UI static files path



print("TEMPLATE_DIR:", TEMPLATE_DIR)  # Debugging output

# Check if index.html exists
if not os.path.exists(os.path.join(TEMPLATE_DIR, "index.html")):
    print("Error: index.html NOT found in", TEMPLATE_DIR)

    
# Initialize Flask with custom paths
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/')
def home():
    return render_template('index.html')  # Load from /ui/templates/

if __name__ == '__main__':
    app.run(debug=True)