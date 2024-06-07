# FastAPI MVC Project

This project is a FastAPI application structured using the MVC (Model-View-Controller) pattern. It includes request and response validation using Pydantic models, performs addition on input lists using Python's multiprocessing pool, and has logging and error handling configured. The project is also dockerized for easy deployment.


## Requirements

- Python 3.9+
- Docker
- Docker Compose

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd ey_assigment
    ```

2. Build project:

    ```bash
    docker-compose up --build
    ```

3. Swagger UI URL:
   ```bash
   URL : http://127.0.0.1:8000/docs
   ```

## Usage

The FastAPI application exposes a POST endpoint `/add` which accepts a JSON payload and returns the sum of integer pairs.

### Request Format

```json
{
    "batchid": "id0101",
    "payload": [[1, 2], [3, 4]]
}

```

### Response Format

```json
{
  "batchid": "id0101",
  "response": [
    3,
    11
  ],
  "status": "complete",
  "started_at": "2024-06-07T10:59:12.483610",
  "completed_at": "2024-06-07T10:59:13.159512"
}

```

### Testing
    
```bash
   pytest app/tests/
   ```


