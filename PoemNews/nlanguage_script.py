# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import language_v1

#export GOOGLE_APPLICATION_CREDENTIALS="/Users/alan/Desktop/service-account-file.json"

def main( phrase ):

    try:
        client = language_v1.LanguageServiceClient()

        # text_content = 'That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows.'

        # Available types: PLAIN_TEXT, HTML
        type_ = enums.Document.Type.PLAIN_TEXT

        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        language = "en"
        document = {"content": phrase, "type": type_, "language": language}

        response = client.classify_text(document)
        # Loop through classified categories returned from the API
        for category in response.categories:
            # Get the name of the category representing the document.
            # See the predefined taxonomy of categories:
            # https://cloud.google.com/natural-language/docs/categories
            print(u"Category name: {}".format(category.name))
            # Get the confidence. Number representing how certain the classifier
            # is that this category represents the provided text.
            print(u"Confidence: {}".format(category.confidence))

        return response
        
    except:
        pass
