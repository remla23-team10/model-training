import joblib
import nltk
import random
from nltk.corpus import stopwords, wordnet
from restaurant_preprocessing import Preprocessing
nltk.download('wordnet')

classifier = joblib.load('models/Classifier_Sentiment_Model.joblib')
preprocesser = Preprocessing()
preprocesser.vectorizer_from_pkl('data/processed/BoW_Vectorizer.joblib')

prediction_map = {
    0: "negative",
    1: "positive"
}

def preprocess(sentence):
    preprocessed = preprocesser.preprocess_review(sentence)
    return preprocesser.transform([preprocessed])

def get_trained_model():
    """Load the model"""
    yield joblib.load('models/Classifier_Sentiment_Model.joblib')


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

def automatic_test_oracle_generation(original, mutants):
    processed_original = preprocess(original)
    print("PROCESSED ORIGINAL:", processed_original[0])
    processed_mutants = [preprocess(m) for m in mutants]
    print("PROCESSED MUTANTS:", processed_mutants)
    prediction_original = classifier.predict(processed_original)[0]
    print("PREDICTION ORIGINAL:", prediction_original)
    prediction_mutants = [classifier.predict(m)[0] for m in processed_mutants]
    print("PREDICTION MUTANTS:", prediction_mutants)
    # prediction_mutants is now an array of 0s and 1s. Return the one that occurs the most.
    res = max(set(prediction_mutants), key=prediction_mutants.count)
    print("RES:", res)
    return res


def automatic_inconsistency_repair():
    pass

if __name__ == "__main__":
    # just some testing
    mutants = automatic_test_input_generation("It's good and amazing.")
    print(automatic_test_oracle_generation("The service at this restaurant is really good.", mutants))
