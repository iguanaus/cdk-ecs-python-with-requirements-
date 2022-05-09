FROM registry.gitlab.com/floating-point-group/garda/python:3.8.7-slim-buster

COPY requirements.txt /requirements.txt

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        wget \
        git \
    && pip3 install --no-cache-dir -r /requirements.txt \
    && apt-get remove -y git

COPY basic_python_code.py /basic_python_code.py

CMD ["/basic_python_code.py"]
ENTRYPOINT ["python"]
