# Custom Jenkins image for the learning labs.
#
# The official jenkins/jenkins image only contains Java and Jenkins itself.
# Our six lab projects need build tools INSIDE Jenkins, so we bake them in:
#   Python 3, Node.js 24 LTS, Go 1.27, Maven 3.10, Docker CLI, git, zip
#
# Build happens automatically via ./setup.sh (docker compose up -d --build).

FROM jenkins/jenkins:lts

USER root

# docker sets TARGETARCH automatically (amd64 on most laptops, arm64 on ARM)
ARG TARGETARCH
ENV NODE_VERSION=24.22.3 \
    GO_VERSION=1.27.4 \
    MAVEN_VERSION=3.10.0

# ---- Base tools + Docker CLI (talks to your laptop's Docker via the socket) ----
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates curl xz-utils git zip unzip \
        python3 python3-pip python3-venv \
        docker.io \
    && rm -rf /var/lib/apt/lists/*

# ---- Node.js LTS (official tarball, arch-aware) ----
RUN case "$TARGETARCH" in \
        arm64) NODE_ARCH=arm64 ;; \
        *)     NODE_ARCH=x64   ;; \
    esac \
    && curl -fsSL "https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-${NODE_ARCH}.tar.xz" \
         -o /tmp/node.tar.xz \
    && tar -xJf /tmp/node.tar.xz -C /usr/local --strip-components=1 \
    && rm /tmp/node.tar.xz

# ---- Go (official tarball, arch-aware) ----
RUN case "$TARGETARCH" in \
        arm64) GO_ARCH=arm64 ;; \
        *)     GO_ARCH=amd64 ;; \
    esac \
    && curl -fsSL "https://go.dev/dl/go${GO_VERSION}.linux-${GO_ARCH}.tar.gz" -o /tmp/go.tgz \
    && tar -C /usr/local -xzf /tmp/go.tgz \
    && rm /tmp/go.tgz

ENV PATH=/usr/local/go/bin:$PATH

# ---- Maven (arch-independent) ----
RUN curl -fsSL "https://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz" \
         -o /tmp/mvn.tgz \
    && tar -xzf /tmp/mvn.tgz -C /opt \
    && ln -s /opt/apache-maven-${MAVEN_VERSION}/bin/mvn /usr/local/bin/mvn \
    && rm /tmp/mvn.tgz

USER jenkins
