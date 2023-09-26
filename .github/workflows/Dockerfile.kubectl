# Use an official Linux distribution as a parent image
FROM alpine:latest

# Install curl and SSL certificates
RUN apk add --update --no-cache curl ca-certificates

# Download and install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
RUN chmod +x kubectl
RUN mv kubectl /usr/local/bin/kubectl

# Set the entry point
ENTRYPOINT ["/usr/local/bin/kubectl"]
