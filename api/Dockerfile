FROM python:3.9

ENV news_api_key L6o8h7xhThCghcZgfZIuKzB_WBfqRmETQ8BUBmjEMgw
ENV weather_api_key c95e0841860d4390be8153737222502
ENV mongodb_user admin
ENV mongodb_secret wfg0wpMfEpRm6Co6
ENV mongodb_host cluster0.sgaqs.mongodb.net/userSession

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
