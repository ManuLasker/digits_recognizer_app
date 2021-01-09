FROM continuumio/miniconda3

COPY . digits_recognizer_app/
RUN pip install -r digits_recognizer_app/requirements.txt
