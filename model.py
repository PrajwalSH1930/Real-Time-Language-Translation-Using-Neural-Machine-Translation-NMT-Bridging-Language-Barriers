# from transformers import MarianMTModel, MarianTokenizer

# def translate_english_to_indian(english_text, target_language_code):
#     """Translates English text to an Indian language."""

#     try:
#         model_name = f"Helsinki-NLP/opus-mt-en-{target_language_code}"
#         tokenizer = MarianTokenizer.from_pretrained(model_name)
#         model = MarianMTModel.from_pretrained(model_name)

#         input_ids = tokenizer.encode(english_text, return_tensors="pt")
#         outputs = model.generate(input_ids)
#         decoded_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

#         return decoded_text

#     except OSError:
#         return f"Error: Translation model for language code '{target_language_code}' not found."
#     except Exception as e:
#         return f"An unexpected error occurred: {e}"

# def main():
#     """Takes user input for English sentence and target language, then translates."""

#     english_text = input("Enter the English sentence to translate: ")
#     target_language = input("Enter the target Indian language code (e.g., hi for Hindi, ta for Tamil, bn for Bengali): ").lower()

#     translated_text = translate_english_to_indian(english_text, target_language)
#     print(f"Translated to {target_language}: {translated_text}")

# if __name__ == "__main__":
#     main()
from transformers import MarianMTModel, MarianTokenizer

# Dictionary of supported Indian languages and their codes
supported_languages = {
    "Hindi": "hi",
    "Tamil": "ta",
    "Bengali": "bn",
    "Marathi": "mr",
    "Telugu": "te",
    "Gujarati": "gu",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Punjabi": "pa",
    "Odia": "or",
    "Assamese": "as",
    "Maithili": "mai",
    "Sindhi": "sd",
    "Konkani": "kok",
    "Nepali": "ne",
    "Santali": "sat",
    "Kashmiri": "ks"
}

def translate_english_to_indian(english_text, target_language_code):
    """Translates English text to an Indian language."""

    try:
        model_name = f"Helsinki-NLP/opus-mt-en-{target_language_code}"
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)

        input_ids = tokenizer.encode(english_text, return_tensors="pt")
        outputs = model.generate(input_ids)
        decoded_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return decoded_text

    except OSError:
        return f"Error: Translation model for language code '{target_language_code}' not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def main():
    """Takes user input for English sentence and target language, then translates."""

    print("Supported Indian Languages:")
    for language, code in supported_languages.items():
        print(f"- {language} ({code})")

    while True: # loop so the user can keep entering sentences
        english_text = input("\nEnter the English sentence to translate (or type 'exit' to quit): ")

        if english_text.lower() == "exit":
            break

        target_language = input("Enter the target Indian language code (e.g., hi, ta, bn): ").lower()

        translated_text = translate_english_to_indian(english_text, target_language)
        print(f"Translated to {target_language}: {translated_text}")

if __name__ == "__main__":
    main()