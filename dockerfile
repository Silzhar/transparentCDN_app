FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir -p /var/www/website/html
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./transparentCDN_app/transparentAPP /code/
ADD ./html /var/www/website/html
ADD ./transparentCDN_app/transparentAPP/templates /var/www/website/transparentCDN_app/transparentAPP/templates
