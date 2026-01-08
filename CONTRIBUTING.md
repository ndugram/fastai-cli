# Contributing to fastapi-cli

Thank you for your interest in contributing! We welcome contributions from the community.

## How to Contribute

### 1. Fork the Repository

Fork the repository on GitHub and clone it locally:

```bash
git clone https://github.com/ndugram/fastai-cli.git
cd fastapi-cli
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### 3. Make Your Changes

- Create a new branch for your feature or bugfix
- Write clean, documented code
- Add tests for your changes
- Ensure all tests pass

### 4. Submit a Pull Request

1. Push your changes to your fork
2. Open a Pull Request against the `main` branch
3. Fill in the PR template completely
4. Link any related issues

## Code Style

- Follow [PEP 8](https://pep8.org/) guidelines
- Use type hints for all functions
- Write docstrings for public functions
- Keep lines under 100 characters

### Linting and Formatting

```bash
# Run linter
ruff check .

# Format code
ruff format .

# Run type checker
mypy src/
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src
```

## Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <description>

body (optional)

footer (optional)
```

Types:
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation changes
- `style` - Code style changes
- `refactor` - Code refactoring
- `test` - Adding tests
- `chore` - Maintenance tasks

Example:
```
feat(ssl): add certificate expiration warning

Add a warning when certificates are about to expire within 30 days.

Closes #123
```

## Issue Tracking

- Before submitting an issue, search existing issues to avoid duplicates
- Use the issue template when creating a new issue
- Provide as much detail as possible (steps to reproduce, expected vs actual behavior)

## Questions?

If you have questions, feel free to:
- Open a [Discussion](https://github.com/ndugram/fastai-cli/discussions)
- Ask in our community chat

We appreciate your contribution!