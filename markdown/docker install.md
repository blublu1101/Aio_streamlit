# Docker Engine install (Ubuntu)

[documentation](https://docs.docker.com/engine/install/ubuntu/)

## Prerequisites

### Uninstall old versions

Run the following command to uninstall all conflicting packages:

```shell
$ for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

## Install using the `apt` repository

### Set up Docker's `apt` repository

```shell
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

### Install the Docker packages

To install the `latest` version, run:

```shell
$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

To install a `specific` version of Docker Engine, start by listing the available versions in the repository:

```shell
# List the available versions:
apt-cache madison docker-ce | awk '{ print $3 }'

5:26.1.0-1~ubuntu.24.04~noble
5:26.0.2-1~ubuntu.24.04~noble
...

# Select the desired version and install:
$ VERSION_STRING=5:26.1.0-1~ubuntu.24.04~noble
$  sudo apt-get install docker-ce=$VERSION_STRING docker-ce-cli=$VERSION_STRING containerd.io docker-buildx-plugin docker-compose-plugin
```

### Verify that the Docker Engine installation is successful by running the `hello-world` image.

```shell
$ sudo docker run hello-world
```

### Upgrade docker engine

To upgrade Docker Engine, follow step 2 of the [installation instructions](#install-the-docker-packages), choosing the new version you want to install.

