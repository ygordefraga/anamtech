#! /usr/bin/env python3

from json import loads
import spacy
from spacy.tokens import DocBin
from tqdm import tqdm


def main() -> None:
    pre_processing_json = [loads(line) for line in open(
        "model/data/pre_processing_train.json", "r")]

    nlp = spacy.blank("pt")
    db = DocBin()

    for line in tqdm(pre_processing_json):
        doc = nlp.make_doc(line["data"].lower())
        doc.ents = [doc.char_span(
            ent[0], ent[1], label=ent[2],
            alignment_mode="contract")
            for ent in line["label"]]
        db.add(doc)

    db.to_disk("model/data/train_data.spacy")


if __name__ == '__main__':
    main()
