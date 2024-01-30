# openfaas-example

## Languages

* Go
* [Python](./python3/)

## Environment Install

### OpenFaaS Command Line Tool (faas-cli)

#### macOS

Use Homebrew to install it.

```shell
brew install faas-cli
```

#### Other Platform

Please reference to OpenFaaS Official Documentation.

[OpenFaaS Official Documentation](https://docs.openfaas.com/cli/install/)

### Deploy OpenFaaS Community Edition (CE) to Kubernetes Cluster

#### Requirement

1. Kubernetes Cluster

#### Step 1: Create Kubernetes Namespace

```shell
kubectl create ns openfaas && kubectl create ns openfaas-fn
```

#### Step 2: Helm charts

```shell
helm repo add openfaas https://openfaas.github.io/faas-netes/
helm repo update
helm upgrade openfaas --install openfaas/openfaas --namespace openfaas
```

#### Other

Please reference to OpenFaaS Official Documentation.

[OpenFaaS Official Documentation](https://docs.openfaas.com/deployment/kubernetes/)
