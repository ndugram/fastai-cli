# fastai-cli

A modern CLI tool for FastAPI developers - initialize projects and generate SSL certificates.

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![PyPI Version](https://img.shields.io/badge/pypi-latest-blue)

## Features

- 🚀 Initialize FastAPI project structure with Django-like folder layout
- 🔐 Generate self-signed SSL certificates
- 💅 Beautiful output with Rich library
- ⚡ Fast and easy to use
- 📦 Ready for PyPI publication

## Installation


### From GitHub

```bash
pip install git+https://github.com/ndugram/fastai-cli.git
```

### From Source

```bash
git clone https://github.com/ndugram/fastai-cli.git
cd fastai-cli
pip install -e .
```

## Quick Start

```bash
# Initialize a new project
fastai init myproject

# Enter project directory
cd myproject

# Start development server
python manage.py runserver

# Open in browser
# http://127.0.0.1:8000
# API docs: http://127.0.0.1:8000/docs
```

## Initialize Project

```bash
fastai init [name]
```

Creates a new FastAPI project structure:

```
project_name/
├── api/
│   └── __init__.py
├── core/
│   └── __init__.py
├── database/
│   └── __init__.py
├── schema/
│   └── __init__.py
├── service/
│   └── __init__.py
├── views/
│   └── __init__.py
├── main.py
└── manage.py
```

Default project name: `backend`

## Generate SSL Certificates

```bash
fastai ssl
```

Creates SSL certificates in `certs/` directory:
- `certs/cert.pem` - SSL certificate
- `certs/key.pem` - Private key

## Commands

| Command | Description |
|---------|-------------|
| `init [name]` | Initialize FastAPI project structure |
| `ssl` | Generate self-signed SSL certificates |
| `help` | Show available commands |

## manage.py Commands

After initializing a project, use `manage.py` for development tasks:

```bash
cd myproject
```

### Run Development Server

```bash
python manage.py runserver                    # Default: 127.0.0.1:8000
python manage.py runserver --host 0.0.0.0     # Bind to all interfaces
python manage.py runserver --port 8080        # Custom port
python manage.py runserver --noreload         # Disable auto-reload
```

### Show Help

```bash
python manage.py help
```

## Project Structure

Generated projects follow a clean architecture:

```
myproject/
├── api/          # API route handlers
├── core/         # Core application settings
├── database/     # Database models and connections
├── schema/       # Pydantic schemas
├── service/      # Business logic
├── views/        # View controllers
├── main.py       # FastAPI application entry point
└── manage.py     # Django-like management script
```

## Requirements

- Python 3.10+
- OpenSSL (for SSL certificate generation)

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md).

## Security

For security issues, please read our [Security Policy](SECURITY.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.