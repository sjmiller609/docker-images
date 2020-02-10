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

# Install runtime dependencies
RUN apt-get update \
  && apt-get install -y \
    libboost-dev libboost-system-dev liblog4cplus-dev libssl-dev \
    postgresql-client \
    net-tools netcat \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Copy installation directory
COPY --from=build /usr/local /usr/local

# Copy runtime scripts
COPY include/bin/* /bin/

# Ensure linking
RUN echo "/usr/local/lib/hooks" > /etc/ld.so.conf.d/kea.conf \
    && ldconfig
