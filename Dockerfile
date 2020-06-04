FROM alpine
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
    apk add --no-cache tzdata python3 py3-multidict py3-yarl py3-pip gmp-dev gcc libc-dev && \
    pip3 install --no-cache-dir nonebot[scheduler] base58 pycryptodome -i https://pypi.tuna.tsinghua.edu.cn/simple