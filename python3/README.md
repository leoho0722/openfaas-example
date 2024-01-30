# python3-openfaas-example

## Official Documentation

[Official Documentation](https://docs.openfaas.com/languages/python/)

## Step 1: Get Template

```shell
faas-cli template pull https://github.com/openfaas/python-flask-template
```

## Step 2: Create New Function

### Parameters

TEMPLATE: python3-flash-debian
HANDLER: hello

In this case, params ```TEMPLATE``` is ```python3-flash-debian``` and ```HANDLER``` is ```hello```

```shell
faas-cli new --lang <TEMPLATE> <HANDLER>

# Example:
# faas-cli new --lang python3-flash-debian hello
```

## Step 3: Build、Push Image and Deploy

### Parameters

YAML_FILE: hello.yml

In this case, params ```YAML_FILE``` is ```hello.yml```

```shell
faas-cli up -f <YAML_FILE>

# Example:
# faas-cli up -f hello.yml
```

## Step 4: Test

### cURL

```shell
curl -H "Content-Type: application/json" -X POST -d '{"message": "OpenFaaS Example using Python"}' http://127.0.0.1:8080/function/hello
```

### OpenFaaS WebUI

Choose JSON radio button first, and input some jsonData in Request Body.
Finally, press invoke button to test, and Response body will be shown.

![OpenFaaS WebUI test](./hello/assets/OpenFaaS%20WebUI%20test.png)
