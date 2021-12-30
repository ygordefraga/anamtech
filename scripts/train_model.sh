source .venv/bin/activate
python3 -m model

python3 -m spacy init fill-config model/config/base_config.cfg \
    model/config/config.cfg

python3 -m spacy train model/config/config.cfg \
    --output model/output \
    --paths.train model/data/train_data.spacy \
    --paths.dev model/data/train_data.spacy