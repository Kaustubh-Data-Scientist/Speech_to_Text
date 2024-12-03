import os
from werkzeug.utils import secure_filename

def save_uploaded_file(file, upload_folder):
    """Saves the uploaded file to the specified folder."""
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    # Secure the filename
    filename = secure_filename(file.filename)
    filepath = os.path.join(upload_folder, filename)

    # Save the file
    file.save(filepath)

    return filepath
