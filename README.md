## Run hypercorn
```sh
uv run hypercorn --config hypercorn-config.toml orchestrator_workflows.main:app
```

## FastApi
```sh
uv run fastapi dev app/main.py
```
## File Path CSV
```sh
/home/felipecc/projetos/restate-webserice/data/users.csv
```

## Curl invoke

```sh
curl localhost:8080/ReadFileWorkflow/12345/run \
    -H 'content-type: application/json' \
    -d '{"file_path": "/home/felipecc/projetos/restate-webserice/data/users.csv"}'
```

## Curl invoke

```sh
curl localhost:8080/ActivateService/active_read_file_wf \
    -H 'content-type: application/json' \
    -d '{"file_path": "/home/felipecc/projetos/restate-webserice/data/users.csv"}'
```    

## Cancel invoke

```sh
restate invocations cancel inv_1jDbkfiEhIjV62J9VufpkgdbEfgEt7nRkZ
```