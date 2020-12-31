FROM python:3.4-alpine
ADD . /code
WORKDIR /code
EXPOSE 80
# ENV https_proxy=https://87.254.212.120:8080
# ENV http_proxy=http://87.254.212.120:8080
RUN pip install flask datetime pymongo[srv]
# ENV https_proxy=
# ENV http_proxy=
CMD ["python", "app.py"]

