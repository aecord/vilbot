# FROM python:3.12-slim AS builder
# RUN python -m pip install --no-cache-dir pdm
# RUN pdm config python.use_venv false
#
# COPY pyproject.toml pdm.lock /project/
# WORKDIR /project
# RUN pdm install --prod --no-lock --no-editable
#
# FROM python:3.12-slim AS bot
# RUN apt-get update -y && \
#   apt-get install -y --no-install-recommends \
#   apt-get autoclean -y && \
#   apt-get autoremove -y
#
# ENV PYTHONPATH=/project/pkgs
#
# COPY src/ /project/pkgs/
#
# COPY --from=builder /project/__pypackages__/3.12/lib /project/pkgs
# WORKDIR /project
# ENTRYPOINT ["python", "-m", "vilbot"]
#
FROM python:3.12-slim AS builder
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends gcc python3-dev libffi-dev && \
    python -m pip install --no-cache-dir pdm && \
    pdm config python.use_venv false

COPY pyproject.toml pdm.lock /project/
WORKDIR /project
RUN pdm install --prod --no-lock --no-editable && \
    apt-get remove --purge -y gcc python3-dev libffi-dev && \
    apt-get autoclean -y && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

FROM python:3.12-slim AS bot
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends && \
    apt-get autoclean -y && \
    apt-get autoremove -y

ENV PYTHONPATH=/project/pkgs

COPY src/ /project/pkgs/
COPY --from=builder /project/__pypackages__/3.12/lib /project/pkgs
WORKDIR /project

ENTRYPOINT ["python", "-m", "vilbot"]
