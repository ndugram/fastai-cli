import typer
from pathlib import Path
from rich.console import Console


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
        """from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok"}
"""
    )

    console.print("✅ Project structure created successfully!",
                  style="bold green")
    console.print(
        f"👉 Next steps:\n"
        f"   uvicorn {name}.main:app --reload"
    )
