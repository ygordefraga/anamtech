#! /usr/bin/env python3

import argparse
from json import loads
from helpers \
    import *


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text",
                        help="Anamnesis to be structured")
    text = parser.parse_args().text

    if text is None:
        recognition_options = loads(
            open("constants/recognition_options.json", "r").read())
        text = SpeechRecognition(recognition_options["MIC"])\
            .recognize()
        print(f"Recognized text: {text}")

    entities = NamedEntityRecognizer().recognize(text)
    AnamnesisStructure().create_json(entities)


if __name__ == '__main__':
    main()
