FROM gitpod/workspace-full:latest AS gitpod

FROM mongo:4 AS mongo
RUN mongod

FROM python:stretch AS python
