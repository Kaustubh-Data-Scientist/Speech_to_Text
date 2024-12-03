from flask import Flask, render_template, request, redirect, url_for, flash
import os
from app.transcription import transcribe_audio
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
# Initialize Flask app
app = Flask(__name__, template_folder=r'C:\Users\Ajay\Desktop\Data Science\Project\Speech_to_Text\templates')
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your_secret_key')  # Replace with a secure key
app.config['UPLOAD_FOLDER'] = 'audio/'
app.config['ALLOWED_EXTENSIONS'] = {'wav', 'mp3', 'm4a'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    """Check allowed file extensions."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def flash_and_redirect(message, endpoint):
    """Flash a message and redirect to a specified endpoint."""
    flash(message)
    return redirect(url_for(endpoint))

@app.route('/')
def index():
    """Render the home page with the file upload form."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    print(f"Request method: {request.method}")  # Debugging log
    if 'audio' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['audio']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Save the file
        file.save(filepath)

        try:
            # Perform transcription
            transcription_result = transcribe_audio(filepath)
            os.remove(filepath)  # Clean up after successful processing
            return render_template('result.html', transcription=transcription_result)
        except Exception as e:
            # Log the error and clean up
            print(f"Error during transcription: {e}")
            if os.path.exists(filepath):
                os.remove(filepath)  # Ensure file is deleted even if transcription fails
            flash("An error occurred during transcription.")
            return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)