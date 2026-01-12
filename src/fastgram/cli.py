import subprocess
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table
from .init_cli import router


"""
fastai-cli - A modern CLI tool for FastAPI developers

This module provides command-line interface for managing FastAPI projects.

Usage:
    fastai init [name]     - Initialize new FastAPI project
    fastai ssl             - Generate self-signed SSL certificates
    fastai help            - Show available commands

For more information, visit: https://github.com/ndugram/fastai-cli
"""


app = typer.Typer()


@app.command("help")
def show_help():
    """
    Show help command
    """
    table = Table(title="FastAI CLI Commands")
    console = Console()

    table.add_column("Command", style="cyan")
    table.add_column("Description", style="magenta")

    table.add_row("init [name]", "Initialize FastAPI project structure")
    table.add_row("ssl", "Generate self-signed SSL certificates (cert.pem & key.pem)")

    console.print(table)


@app.command()
def ssl():
    """
    Generate self-signed SSL certs without questions
    """
    certs = Path.cwd() / "certs"
    certs.mkdir(exist_ok=True)

    key = certs / "key.pem"
    cert = certs / "cert.pem"

    cmd = [
        "openssl", "req",
        "-x509",
        "-newkey", "rsa:4096",
        "-keyout", str(key),
        "-out", str(cert),
        "-days", "365",
        "-nodes",
        "-subj", "/C=US/ST=None/L=None/O=FastAI/OU=Dev/CN=localhost",
    ]

    typer.echo("🔐 Generating SSL certs (non-interactive)...")

    subprocess.run(cmd, check=True)

    typer.echo("✅ Done")
    typer.echo("📁 certs/key.pem")
    typer.echo("📁 certs/cert.pem")


def main() -> None:
    app.add_typer(router)
    typer.main.get_command(app)()


if __name__ == "__main__":
    main()
