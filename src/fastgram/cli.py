import typer

from .commands import app_router, console_router


app = typer.Typer()


def main() -> None:
    app.add_typer(app_router)
    app.add_typer(console_router)
    typer.main.get_command(app)()


if __name__ == "__main__":
    main()
