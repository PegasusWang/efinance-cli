"""
Bond related commands
"""
import typer
from typing import Optional
from rich import print as rprint
import efinance as ef
from efinance_cli.main import display_dataframe

app = typer.Typer(help="Bond market data commands")


@app.command("realtime")
def get_realtime_quotes(
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get real-time quotes for all convertible bonds"""
    try:
        df = ef.bond.get_realtime_quotes()

        if df is None or df.empty:
            rprint("[red]No data available[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="Real-time Quotes (Convertible Bonds)", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("history")
def get_quote_history(
    code: str = typer.Argument(..., help="Bond code (e.g., 123111 for 东财转3)"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get bond K-line history data"""
    try:
        df = ef.bond.get_quote_history(code)

        if df is None or df.empty:
            rprint(f"[red]No data found for bond {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Bond History: {code}", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("all-info")
def get_all_base_info(
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get all convertible bonds basic information"""
    try:
        df = ef.bond.get_all_base_info()

        if df is None or df.empty:
            rprint("[red]No data available[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="All Convertible Bonds", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("base-info")
def get_base_info(
    code: str = typer.Argument(..., help="Bond code"),
):
    """Get bond basic information"""
    try:
        df = ef.bond.get_base_info(code)

        if df is None or df.empty:
            rprint(f"[red]No base info found for bond {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Bond Basic Info: {code}")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("deal")
def get_deal_detail(
    code: str = typer.Argument(..., help="Bond code"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get bond deal detail"""
    try:
        df = ef.bond.get_deal_detail(code)

        if df is None or df.empty:
            rprint(f"[red]No deal data found for bond {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Bond Deal Detail: {code}", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("history-bill")
def get_history_bill(
    code: str = typer.Argument(..., help="Bond code"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get historical bill (capital flow) data for bond"""
    try:
        df = ef.bond.get_history_bill(code)

        if df is None or df.empty:
            rprint(f"[red]No history bill data found for bond {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Bond History Bill: {code}", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("today-bill")
def get_today_bill(
    code: str = typer.Argument(..., help="Bond code"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get today's bill (capital flow) data for bond"""
    try:
        df = ef.bond.get_today_bill(code)

        if df is None or df.empty:
            rprint(f"[red]No today bill data found for bond {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Bond Today Bill: {code}", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
