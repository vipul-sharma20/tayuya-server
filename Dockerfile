FROM python:3.7

WORKDIR /home/tayuya-server/
COPY . /home/tayuya-server/

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
