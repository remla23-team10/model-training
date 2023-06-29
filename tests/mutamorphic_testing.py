import joblib
import nltk
import random
import logging
import pandas as pd
from pprint import pprint
from nltk.corpus import stopwords, wordnet
from restaurant_preprocessing import Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
nltk.download('wordnet')

classifier = joblib.load('models/Classifier_Sentiment_Model.joblib')
count_vectorizer = CountVectorizer(max_features = 1440)
preprocesser = Preprocessing()
preprocesser.vectorizer_from_pkl('data/processed/BoW_Vectorizer.joblib')

# prediction_map = {
#     0: "negative",
#     1: "positive"
# }

def preprocess(sentence):
    preprocessed = preprocesser.preprocess_review(sentence)
    return preprocesser.transform([preprocessed])

def automatic_test_input_generation(sentence: str) -> set:
    """
    For each word in the sentence excluding stopwords,
    generate a mutant by replacing the word with a similar word.
    """
    
    mutants = set(sentence)
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
    processed_original = preprocess(original)
    processed_mutants = [preprocess(m) for m in mutants]
    prediction_original = classifier.predict(processed_original)[0]
    prediction_mutants = [classifier.predict(m)[0] for m in processed_mutants]
    # prediction_mutants is now an array of true and false. Return the one that occurs the most.
    res = max(set(prediction_mutants), key=prediction_mutants.count)
    logging.info("PROCESSED ORIGINAL: %s", processed_original)
    logging.info("PROCESSED MUTANTS: %s", processed_mutants)
    logging.info("PREDICTION ORIGINAL: %s", prediction_original)
    logging.info("PREDICTION MUTANTS: %s", prediction_mutants)
    logging.info("RES: %s", res)
    return {"original": prediction_original, "mutants": res}

if __name__ == "__main__":
    # Test 100 sentences. 
    corpus = joblib.load('data/processed/corpus.joblib')
    dataset = pd.read_csv('data/external/a1_RestaurantReviews_HistoricDump.tsv',
                          delimiter = '\t', quoting = 3,
                          dtype={'Review': str, 'Liked': bool})
    
    random_lines = dataset.sample(n=100)
    x_values = random_lines['Review'].values
    # print(x_values[:3]); raise SystemExit

    predictions = []
    for index, row in dataset.iterrows():
        test_sentence = row['Review']
        mutants = automatic_test_input_generation(test_sentence)
        result = automatic_test_oracle_generation_and_repair(test_sentence, mutants)
        result["true_value"] = 1 if row['Liked'] else 0
        predictions.append(result)
    avg_original = sum([1 for p in predictions if p["original"] == p["true_value"]]) / len(predictions)
    avg_mutants = sum([1 for p in predictions if p["mutants"] == p["true_value"]]) / len(predictions)
    print("Average original: ", avg_original)
    print("Average mutants: ", avg_mutants)
    assert avg_original <= avg_mutants
