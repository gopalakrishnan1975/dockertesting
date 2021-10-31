FROM python:3.7.4
COPY ./Centrality.py ./app
WORKDIR ./app
COPY ../requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD python Centrality.py
