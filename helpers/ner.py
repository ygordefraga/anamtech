import spacy


class NamedEntityRecognizer():

    def __init__(self):
        self._nlp = spacy.load('model/output/model-last')

    def recognize(self, text):
        print("Identifying entities")
        return [
            {
                "text": entity.text,
                "entity": entity.label_
            }
            for entity in self._nlp(text).ents
        ]
