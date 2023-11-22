FROM alpine:latest
RUN apk add python3 py3-pip \
    && pip3 install flask requests
COPY app /
WORKDIR /
EXPOSE 5000
ENTRYPOINT ["sh", "start.sh"]