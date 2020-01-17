FROM python:3

WORKDIR /var/www

ADD scripts scripts
ADD service service
ADD Pipfile ./
ADD Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install
RUN chmod +x ./scripts/run-service.sh

EXPOSE 5000

CMD [ "./scripts/run-service.sh" ]