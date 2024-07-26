FROM        python:3.10-bullseye AS base
COPY        requirements.txt requirements.txt
RUN         pip install -r requirements.txt

FROM base
ENV         PYTHONUNBUFFERED=1
WORKDIR     /API/
COPY        . .
EXPOSE      8001
ENTRYPOINT  ["python", "main.py"]
