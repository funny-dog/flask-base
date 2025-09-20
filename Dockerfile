FROM python:3.8-alpine


# Packages required for psycopg2
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Ruby sass
RUN apk add --no-cache make ruby-dev ruby-full gcc musl-dev libxml2-dev libxslt-dev
RUN gem sources --add https://gems.ruby-china.com/ --remove https://rubygems.org/
RUN gem install sass -v 3.7.4

#MAINTANER Your Name "youremail@domain.tld"
ENV MAIL_USERNAME=yourmail@test.com
ENV MAIL_PASSWORD=testpass
ENV SECRET_KEY=SuperRandomStringToBeUsedForEncryption
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
ENV PIP_TIMEOUT=600
RUN pip3 install -r requirements.txt --retries 5 --timeout 600
ENV PYTHONIOENCODING=UTF-8
RUN pip3 install sqlalchemy_utils==0.38.3 flask_dance==5.1.0 Flask-Caching==1.11.1 python-gitlab==3.10.0

COPY . /app

#RUN python3 manage.py recreate_db && python3 manage.py setup_dev && python3 manage.py add_fake_data

ENTRYPOINT ["python3", "-u" ,"manage.py", "runserver"]

