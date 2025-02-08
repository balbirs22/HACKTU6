# text_preprocessing.py

import re
import spacy

# Load the spaCy English model once for efficiency.
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """
    Clean the input text by removing extra whitespaces and converting it to lowercase.
    
    Parameters:
        text (str): The raw text to be cleaned.
    
    Returns:
        str: The cleaned text.
    """
    # Remove extra whitespace and line breaks
    text = re.sub(r'\s+', ' ', text)
    # Convert text to lowercase (optional, based on your requirements)
    text = text.lower()
    return text

def advanced_tokenize_text(text, use_lemmatization=False, remove_stopwords=True, remove_punctuation=True):
    """
    Tokenizes the input text using spaCy's NLP pipeline with advanced options.
    
    Parameters:
        text (str): The input text to tokenize.
        use_lemmatization (bool): If True, returns the lemma of each token.
        remove_stopwords (bool): If True, filters out stopwords.
        remove_punctuation (bool): If True, filters out punctuation tokens.
    
    Returns:
        list: A list of processed tokens.
    """
    doc = nlp(text)
    tokens = []
    for token in doc:
        # Skip spaces
        if token.is_space:
            continue
        
        # Optionally remove stopwords
        if remove_stopwords and token.is_stop:
            continue
        
        # Optionally remove punctuation
        if remove_punctuation and token.is_punct:
            continue
        
        # Use lemma if requested; otherwise, use the token text.
        token_text = token.lemma_ if use_lemmatization else token.text
        tokens.append(token_text)
    
    return tokens

# Example usage (for testing or demonstration purposes)
if __name__ == "__main__":
    sample_text = ("This is an example sentence, demonstrating advanced tokenization with spaCy! "
                   "Let's see how it works.")
    
    # Clean the text first
    cleaned_text = clean_text(sample_text)
    print("Cleaned Text:", cleaned_text)
    
    # Tokenize the cleaned text using advanced tokenization (with lemmatization)
    tokens = advanced_tokenize_text(cleaned_text, use_lemmatization=True)
    print("Advanced Tokens:", tokens)
