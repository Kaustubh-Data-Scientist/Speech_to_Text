# Speech-to-Text Application

## Overview
This project uses **AssemblyAI's API** to convert uploaded audio files into text, distinguishing between speakers in a conversation. The application is built with Flask for the backend and integrates a modern UI for ease of use.

## Features
- **Upload Audio Files**: Supports `.mp3`, `.wav`, and other audio formats.
- **Speaker Separation**: Differentiates between caller and receiver in call recordings.
- **Real-Time Processing**: Converts audio to text efficiently using AssemblyAI.
- **User-Friendly Interface**: Web-based UI built with HTML templates.

## File Structure
```
Speech_to_Text/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── transcription.py
│   ├── upload.py
├── templates/
│   ├── index.html
│   ├── result.html
├── audio/
├── requirements.txt
├── .env
```

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Kaustubh-Data-Scientist/Speech_to_Text.git
   cd Speech_to_Text
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add AssemblyAI API Key**:
   - Create a `.env` file:
     ```plaintext
     ASSEMBLYAI_API_KEY=your_api_key_here
     ```
   - Replace `your_api_key_here` with your actual API key.

5. **Run the Application**:
   ```bash
   flask run
   ```
   Access the app at `http://127.0.0.1:5000`.

## Usage
1. Visit the homepage.
2. Upload a supported audio file.
3. View the transcribed text and speaker separation.

## Requirements
- Python 3.7+
- Dependencies listed in `requirements.txt`

## License
This project is open-source and available under the [MIT License](LICENSE).
