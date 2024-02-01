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
kubectl apply -f https://raw.githubusercontent.com/openfaas/faas-netes/master/namespaces.yml
```

#### Step 2: Helm charts

```shell
helm repo add openfaas https://openfaas.github.io/faas-netes/
helm repo update
helm upgrade openfaas --install openfaas/openfaas --namespace openfaas
```

#### Step 3: Expose OpenFaaS Gateway Service to LoadBalancer

```shell
kubectl patch svc gateway-external -n openfaas -p '{"spec":{"type": "LoadBalancer"}}'
```

#### Step 4: Get OpenFaaS WebUI Password

```shell
PASSWORD=$(kubectl -n openfaas get secret basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode) && \
echo "OpenFaaS admin password: $PASSWORD"
```

#### Step 5: Login OpenFaaS WebUI via credential

```shell
faas-cli login -u admin -p $PASSWORD
```

#### Other

Please reference to OpenFaaS Official Documentation.

[OpenFaaS Official Documentation](https://docs.openfaas.com/deployment/kubernetes/)
