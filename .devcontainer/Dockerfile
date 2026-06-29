FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# Remove a broken Yarn apt source from the base image.
RUN rm -f /etc/apt/sources.list.d/yarn.list /etc/apt/sources.list.d/yarn.sources \
    && apt-get update
