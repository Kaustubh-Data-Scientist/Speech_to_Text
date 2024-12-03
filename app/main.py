from flask import Flask, render_template, request, redirect, url_for, flash
import os
from app.transcription import transcribe_audio
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure key
app.config['UPLOAD_FOLDER'] = 'audio/'
app.config['ALLOWED_EXTENSIONS'] = {'wav', 'mp3', 'm4a'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    """Render the home page with the file upload form."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and transcription."""
    if 'audio_file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['audio_file']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Transcribe the audio file
        transcription_result = transcribe_audio(filepath)
        
        # Pass result to result.html for display
        return render_template('result.html', transcription=transcription_result)
    else:
        flash('Invalid file format. Please upload a .wav, .mp3, or .m4a file.')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)