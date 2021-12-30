pip3 install virtualenv
python3 -m venv .venv
source .venv/bin/activate
brew install portaudio
pip install --upgrade pip
pip3 install -r requirements.txt
python3 -m spacy download pt_core_news_lg