"""Implementation for mutamorphic testing and automatic repair"""
import random
import logging

import nltk
import joblib
import pandas as pd
from nltk.corpus import stopwords, wordnet
from restaurant_preprocessing import Preprocessing
from sklearn.feature_extraction.text import CountVectorizer
nltk.download('wordnet')

classifier = joblib.load('models/Classifier_Sentiment_Model.joblib')
count_vectorizer = CountVectorizer(max_features = 1440)
preprocesser = Preprocessing()
preprocesser.vectorizer_from_pkl('data/processed/BoW_Vectorizer.joblib')

def preprocess(sentence):
    """Preprocess a sentence"""
    preprocessed = preprocesser.preprocess_review(sentence)
    return preprocesser.transform([preprocessed])

def automatic_test_input_generation(sentence: str) -> set:
    """
    For each word in the sentence excluding stopwords,
    generate a mutant by replacing the word with a similar word.
    """

    mutants = {sentence}
    for i, word in enumerate(sentence.split()):
        if word not in stopwords.words('english'):
            # Get one synonym.
            syn = wordnet.synsets(word)
            if len(syn) > 0:
                new_sentence = sentence.split()
                synonyms = []
                for synset in wordnet.synsets(word):
                    synonyms += [lemma.name() for lemma in synset.lemmas() if lemma.name() != word]
                if synonyms:
                    new_sentence[i] = random.choice(synonyms)
                    mutants.add(' '.join(new_sentence))
    return mutants


def automatic_test_oracle_generation_and_repair(original, mutants):
    """Test the original and mutants"""
    processed_original = preprocess(original)
    processed_mutants = [preprocess(m) for m in mutants]
    prediction_original = classifier.predict(processed_original)[0]
    prediction_mutants = [classifier.predict(pm)[0] for pm in processed_mutants]
    # prediction_mutants is now an array of true and false. Return the one that occurs the most.
    res = max(set(prediction_mutants), key=prediction_mutants.count)
    logging.info("PROCESSED ORIGINAL: %s", processed_original)
    logging.info("PROCESSED MUTANTS: %s", processed_mutants)
    logging.info("PREDICTION ORIGINAL: %s", prediction_original)
    logging.info("PREDICTION MUTANTS: %s", prediction_mutants)
    logging.info("RES: %s", res)
    return {"original": prediction_original, "mutants": res}

def test_mutamorphic():
    """Test 100 sentences."""
    dataset = pd.read_csv('data/external/a1_RestaurantReviews_HistoricDump.tsv',
                          delimiter = '\t', quoting = 3,
                          dtype={'Review': str, 'Liked': bool})
    random_lines = dataset.sample(n=100)

    # Get average accuracy of original vs mutants
    predictions = []
    for _, row in random_lines.iterrows():
        test_sentence = row['Review']
        mutants = automatic_test_input_generation(test_sentence)
        result = automatic_test_oracle_generation_and_repair(test_sentence, mutants)
        result["true_value"] = 1 if row['Liked'] else 0
        predictions.append(result)
    avg_original = sum([1 for p in predictions if p["original"] == p["true_value"]]) / len(predictions)
    avg_mutants = sum([1 for p in predictions if p["mutants"] == p["true_value"]]) / len(predictions)
    print("Average original: ", avg_original)
    print("Average mutants: ", avg_mutants)
    assert abs(avg_original-avg_mutants) <= 0.05
