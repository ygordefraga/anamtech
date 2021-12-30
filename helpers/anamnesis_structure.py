from json import loads, dump
from time import localtime, strftime

registered_entities = loads(open("constants/entities.json")
                            .read())


class AnamnesisStructure():

    def create_json(self, recognized_entities):
        json = {}
        for recognized_entity in recognized_entities:
            entity = recognized_entity["entity"]
            if entity in registered_entities:
                if entity not in json.keys():
                    json[entity] = \
                        [recognized_entity["text"]]
                else:
                    if recognized_entity["text"] \
                            not in json[entity]:
                        json[entity]\
                            .append(recognized_entity["text"])

        for key in json.keys():
            if len(json[key]) == 1:
                json[key] = json[key][0]

        final_json = {}
        for ent in registered_entities:
            if ent in json.keys():
                final_json[ent] = json[ent]

        date_time = strftime("%Y-%m-%d_%H:%M:%S", localtime())
        path = f"output/anamnesis_{date_time}.json"

        with open(path, 'w', encoding='utf-8') as f:
            dump(final_json, f, ensure_ascii=False, indent=4)

        print(f"Output: {path}")
