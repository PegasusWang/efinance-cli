"""
efinance-cli main entry point
"""
import typer
from typing import Optional
from rich.console import Console
from rich.table import Table
from rich import print as rprint
import pandas as pd
import efinance as ef
from efinance_cli import __version__

app = typer.Typer(
    name="efinance-cli",
    help="CLI tool for efinance - Get stock, fund, bond and futures data from command line"
)
console = Console()


def display_dataframe(df: pd.DataFrame, title: Optional[str] = None, max_rows: int = 50):
    """Display a pandas DataFrame in a formatted table"""
    if df is None or df.empty:
        console.print("[yellow]No data available[/yellow]")
        return

    # Limit rows if too many
    if len(df) > max_rows:
        console.print(f"[yellow]Showing {max_rows} of {len(df)} rows[/yellow]")
        df = df.head(max_rows)

    # Create table
    table = Table(show_header=True, header_style="bold cyan", title=title)

    # Add columns
    for col in df.columns:
        table.add_column(str(col))

    # Add rows
    for _, row in df.iterrows():
        table.add_row(*[str(v) for v in row.values])

    console.print(table)


# Import subcommands
from efinance_cli import stock, fund, bond, futures

# Add subcommand groups
app.add_typer(stock.app, name="stock", help="Stock related commands")
app.add_typer(fund.app, name="fund", help="Fund related commands")
app.add_typer(bond.app, name="bond", help="Bond related commands")
app.add_typer(futures.app, name="futures", help="Futures related commands")


@app.command()
def version():
    """Show version information"""
    rprint(f"[bold green]efinance-cli version: {__version__}[/bold green]")
    rprint(f"[bold blue]efinance version: {ef.__version__ if hasattr(ef, '__version__') else 'unknown'}[/bold blue]")


if __name__ == "__main__":
    app()
