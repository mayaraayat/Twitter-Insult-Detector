import pickle

from insult_training import preprocessing, convert_to_numbers, to_tfidf, train_test_set, load_and_store_data


def replies_repercussions(text):
    with open('first_classifier_insult', 'rb') as training_model:
        model = pickle.load(training_model)

    y = model.predict(text)
    print(y)


replies_repercussions(
    to_tfidf(convert_to_numbers(preprocessing(['fuck you']))))
