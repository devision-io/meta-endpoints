FROM alpine/git as git_api_common_protos
RUN git clone https://github.com/devision-io/api-common-protos /api-common-protos

FROM google/cloud-sdk:220.0.0-slim

COPY --from=git_api_common_protos /api-common-protos /api-common-protos

RUN apt-get update && apt-get install -qqy python3-pip
RUN python3 -m pip install grpcio-tools==1.25.0
RUN python3 -m pip install mypy-protobuf==1.7
RUN apt-get install -qqy apt-utils golang-goprotobuf-dev


ADD cli/entrypoint.py /entrypoint.py
RUN chmod +x /entrypoint.py

WORKDIR /run
ENTRYPOINT [ "/entrypoint.py" ]

