FROM python:3.8-slim
ENV LANG=C.UTF-8

RUN pip install --upgrade pip setuptools wheel
RUN pip install hazm parsivar      

WORKDIR /app
COPY . .                            

CMD ["python"]                     
