# Poetry Tutorial

This repository holds all python learnings.

## Testing

`poetry run pytest`

## FastAPI

Run the dev server with `fastapi dev fastapi_tutorial/main.py`.

## Pre-commit Hook

Install the pre-commit hook with `pre-commit install`.

> Note: the these pre-commit hooks can be written by anyone, so fix the version to a trusted source.

## python-dotenv

```python
# Load .env as environment variables
load_dotenv()
os.getenv('API_KEY')

# Load .env as dictionary
config = {
    **dotenv_values(),
    **os.environ # Loads all environment variables
}
```
