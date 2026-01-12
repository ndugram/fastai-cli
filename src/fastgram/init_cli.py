import typer
from pathlib import Path
from rich.console import Console


"""
fastai-cli - A modern CLI tool for FastAPI developers

This module provides commands for initializing FastAPI projects
and managing development servers.

Usage:
    fastai init <project_name>    - Create new FastAPI project structure
    fastai help                   - Show available commands
"""


router = typer.Typer()
console = Console()


FOLDERS = [
    "service",
    "core",
    "database",
    "schema",
    "api",
    "views",
]


@router.command("init")
def init_command(
    name: str = typer.Argument(
        "backend",
        help="Project folder name (default: backend)"
    ),
):
    project_dir = Path(name)

    if project_dir.exists():
        console.print(
            f"❌ Directory '{name}' already exists",
            style="bold red"
        )
        raise typer.Exit(code=1)

    console.print(f"🚀 Initializing FastAPI project: [bold]{name}[/bold]")

    project_dir.mkdir()

    for folder in FOLDERS:
        folder_path = project_dir / folder
        folder_path.mkdir(parents=True)
        (folder_path / "__init__.py").touch()

    main_py = project_dir / "main.py"
    main_py.write_text(
        '''"""FastAPI application module.

This module contains the main FastAPI application instance and all
registered routes. The application is created using FastAPI framework
with automatic OpenAPI documentation generation.

To run the application:
    python manage.py runserver

The application will be available at http://127.0.0.1:8000
API documentation: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
"""
from fastapi import FastAPI


app = FastAPI(
    title="FastAPI Project",
    description="A modern FastAPI application",
    version="1.0.0",
)


@app.get("/")
async def root():
    """Root endpoint - returns API status."""
    return {"status": "ok", "message": "Welcome to FastAPI"}

'''
    )

    manage_py = project_dir / "manage.py"
    manage_py.write_text(
        '''
"""
Script for FastAPI projects.

This utility provides a set of commands to help you manage your FastAPI
application during development.

Usage:
    python manage.py <command> [options]

Available commands:
    runserver    Start the development server
    help         Show this help message

Options for runserver:
    --host HOST     Bind to this host (default: 127.0.0.1)
    --port PORT     Bind to this port (default: 8000)
    --noreload      Disable auto-reload
"""

import sys
import uvicorn


def main():
    """Run administrative tasks."""
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    host = "127.0.0.1"
    port = 8000
    reload = True

    i = 0
    while i < len(args):
        if args[i] == "--host" and i + 1 < len(args):
            host = args[i + 1]
            i += 2
        elif args[i] == "--port" and i + 1 < len(args):
            port = int(args[i + 1])
            i += 2
        elif args[i] == "--noreload":
            reload = False
            i += 2
        else:
            i += 1

    if command == "runserver":
        print(f"🚀 Starting server at http://{host}:{port}")
        uvicorn.run(
            "main:app",
            host=host,
            port=port,
            reload=reload,
        )
    elif command == "help":
        print(__doc__)
    else:
        print(f"Unknown command: {command}")
        print("Run 'python manage.py help' for usage information.")
        sys.exit(1)


if __name__ == "__main__":
    main()
'''
    )

    console.print("✅ Project structure created successfully!",
                  style="bold green")
    console.print(
        f"👉 Next steps:\n"
        f"✅ cd {name}"
    )
