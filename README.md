# fastai-cli

A modern CLI tool for FastAPI developers - generate SSL certificates and bootstrap projects.

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![PyPI Version](https://img.shields.io/badge/pypi-latest-blue)

## Features

- 🚀 Initialize FastAPI project structure
- 🔐 Generate self-signed SSL certificates
- 💅 Beautiful output with Rich library
- ⚡ Fast and easy to use

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

## Usage

### Initialize Project

```bash
fastai init [name]
```

Creates a new FastAPI project structure:
```
project_name/
├── api/__init__.py
├── core/__init__.py
├── database/__init__.py
├── schema/__init__.py
├── service/__init__.py
├── views/__init__.py
└── main.py
```

Default project name: `backend`

### Generate SSL Certificates

```bash
fastai ssl
```

Creates:
- `certs/cert.pem` - SSL certificate
- `certs/key.pem` - Private key

### Show Help

```bash
fastai help
```

## Commands

| Command | Description |
|---------|-------------|
| `init [name]` | Initialize FastAPI project structure |
| `ssl` | Generate self-signed SSL certificates |
| `help` | Show available commands |

## Requirements

- Python 3.10+
- OpenSSL (for SSL certificate generation)

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md).

## Security

For security issues, please read our [Security Policy](SECURITY.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.