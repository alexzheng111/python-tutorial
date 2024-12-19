# Poetry Tutorial

This repository holds all python learnings.

## Debugging

In VSCode, follow these instructions: [link](https://fastapi.tiangolo.com/tutorial/debugging/#run-your-code-with-your-debugger)

Though I was able to just use the `Python Debugger: FastAPI` option.

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
