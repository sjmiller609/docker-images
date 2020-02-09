FROM ubuntu:18.04 AS build

ENV KEA_VERSION="1.6.1"

# Install build dependencies
RUN apt-get update
RUN apt-get install -y automake libtool pkg-config build-essential ccache
RUN apt-get install -y libboost-dev libboost-system-dev liblog4cplus-dev libssl-dev
# Enable compile for PostgreSQL
RUN apt-get install -y postgresql-server-dev-all libpq-dev
# Install wget to copy from FTP server
RUN apt-get install -y wget
# Build Kea
COPY include/build /build
RUN chmod +x /build && /build
# Install Kea
COPY include/install /install
RUN chmod +x /install && /install

FROM ubuntu:18.04 AS server

# Copy installation directory
COPY --from=build /usr/local /usr/local

# Install runtime dependencies
RUN apt-get update \
  && apt-get install -y libboost-dev libboost-system-dev liblog4cplus-dev libssl-dev postgresql-client
# Install extra packages
RUN apt-get install -y net-tools netcat

# Ensure linking
RUN echo "/usr/local/lib/hooks" > /etc/ld.so.conf.d/kea.conf \
    && ldconfig
