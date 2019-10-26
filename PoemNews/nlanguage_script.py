import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def helper(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return score

def main(words):
    client = language.LanguageServiceClient()
    document = types.Document(
        content=words,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    score = helper(annotations)
    return score
