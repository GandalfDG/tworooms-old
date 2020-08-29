FROM python

COPY ./requirements.txt ./

RUN python -m pip install -r requirements.txt