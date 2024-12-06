
Setup
#### Python Version: 3.11

1. Setup EnvVars
```bash
cp .env.example .env
```

2. Assure that poetry is using python3.11
```bash
poetry env use python3.11
```

3. Poetry install dependencies
```bash
poetry install
```

4. Run locally

```bash
uvicorn src.main:app --port 8005 --reload
```

5. Run project or use an external controller service

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8005
```

- #### To generate requirements

```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```



## 📂 Project Structure

```plaintext
.
├── src/
│   ├── application/
│   ├── domain/
│   ├── infra/
│   ├── di.py
│   ├── main.py
├── tests/
├── .env.example
├── pyproject.toml
├── poetry.lock
├── requirements.txt
├── README.md

 - src/: Contains the core application code.
 - tests/: Contains unit tests for the project.
 - .env.example: Example configuration file for environment variables.
 - pyproject.toml: Project configuration and dependency management (Poetry).
 - requirements.txt: Exported dependencies for environments not using Poetry.
```
