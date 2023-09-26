# Use Alpine Linux 3.18 as a parent image
FROM alpine:3.18

# Install curl and SSL certificates
RUN apk add --update --no-cache curl ca-certificates

# Download and install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
RUN chmod +x kubectl
RUN mv kubectl /usr/local/bin/kubectl

# Install kubeval
RUN curl -LO "https://github.com/instrumenta/kubeval/releases/latest/download/kubeval-linux-amd64"
RUN chmod +x kubeval-linux-amd64
RUN mv kubeval-linux-amd64 /usr/local/bin/kubeval

# Set the entry point
ENTRYPOINT ["/usr/local/bin/kubectl"]
