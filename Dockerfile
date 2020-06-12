FROM python:slim
WORKDIR /root
COPY ./ ./

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["hypercorn","run:app"]