FROM debian:jessie

MAINTAINER hug33k

ENV PORT	80

RUN	mkdir /work

COPY	./requirements.txt /work/requirements.txt

RUN	apt-get update -qqy && \
	apt-get install -qqy python2.7 python-dev python-pip curl && \
	pip install -r /work/requirements.txt

RUN	apt-get update -qqy && \
	apt-get install -qqy zip

EXPOSE 80

COPY	./EpitechAPI-0.0.0.zip /work/EpitechAPI.zip

RUN		cd /work && unzip EpitechAPI.zip

COPY	./run.sh /work/run.sh

CMD ["sh", "/work/run.sh"]