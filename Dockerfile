FROM gitpod/workspace-full:latest AS gitpod

FROM mongo:4 AS mongo
RUN mongod --fork --logpath /var/log/mongod.log

FROM python:stretch AS python
