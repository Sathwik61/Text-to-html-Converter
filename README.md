
# Text to HTML Converter

This is a Django-based web application that allows users to convert plain text into HTML content. The application provides a rich-text editor where users can input their text, and upon submission, the HTML output is displayed.

## Features

- **Rich Text Editor**: Input text with formatting options using CKEditor.
- **HTML Output**: Converts the input text into HTML format.
- **Copy to Clipboard**: Easily copy the generated HTML output to the clipboard.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 - 3.12 
- Django 4.2
- Tailwind CSS (included via CDN)
- CKEditor (included via CDN)

## Installation

1. **Clone the repository:**
   ```bash
   https://github.com/Sathwik61/Text-to-html-Converter.git
   cd text-to-html-converter
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: `env\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install django
   ```

4. **Run the Django development server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Project Structure

- **converter/**: Contains the main application files.
  - **forms.py**: Defines the `TextForm` form class for input.
  - **views.py**: Contains the view function `convert_text` to handle form submissions.
  - **urls.py**: Maps the view function to the root URL.
  - **templates/converter/index.html**: The main HTML template for the converter page.

## Usage

1. Open the application in your browser.
2. Enter your text in the rich-text editor.
3. Click the "Convert" button to generate the HTML output.
4. Use the "Copy" button to copy the HTML to your clipboard.

## Customization

- **Styling**: The application uses Tailwind CSS for styling, which can be customized as needed.
- **Editor**: CKEditor is used as the text editor. You can configure it further in the HTML template.

## Contributing

Feel free to contribute to the project by forking the repository and submitting a pull request. Please make sure to follow the coding standards and write appropriate documentation.


---
