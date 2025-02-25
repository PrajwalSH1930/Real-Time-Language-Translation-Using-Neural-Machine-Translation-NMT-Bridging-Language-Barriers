# English to Indian Language Translator

This is a web application that translates English text to various Indian languages.

## How to Run

1.  Clone the repository:
    ```bash
    git clone [your-repository-url]
    cd your-translation-project
    ```
2.  Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the Flask application:
    ```bash
    python app.py
    ```
5.  Open your web browser and go to `http://127.0.0.1:5000/`.

## Dependencies

* Flask
* Transformers (Hugging Face)

## Supported Languages

* Hindi (hi)
* Tamil (ta)
* Bengali (bn)
* ... (and others from your supported_languages dictionary)

## Notes

* Ensure you have a stable internet connection for the model to download.
* The translation quality may vary depending on the language and the complexity of the input text.
