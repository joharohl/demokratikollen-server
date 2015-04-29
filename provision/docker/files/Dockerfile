FROM registry:2.0

# Add the custom configuration file we made 
ADD ./registry_config.yml cmd/registry/config.yml

RUN mkdir /var/registry-data

# Create the data directory
VOLUME /var/registry-data