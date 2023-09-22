FROM python:3.9

WORKDIR /app

RUN pip install --upgrade pip

COPY . .
RUN pip install openpyxl
RUN pip install path
RUN pip install djangorestframework
RUN pip install django-cors-headers
RUN pip install gunicorn
RUN pip install pyparsing
RUN pip install sympy

COPY entrypoint.sh .

EXPOSE 5000

ENTRYPOINT ["sh","entrypoint.sh"]
