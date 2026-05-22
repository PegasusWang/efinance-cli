"""
Futures related commands
"""
import typer
from typing import Optional, List
from rich import print as rprint
import efinance as ef
from efinance_cli.main import display_dataframe

app = typer.Typer(help="Futures market data commands")


@app.command("info")
def get_futures_base_info(
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get futures basic information"""
    try:
        df = ef.futures.get_futures_base_info()

        if df is None or df.empty:
            rprint("[red]No data available[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="Futures Basic Information", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("realtime")
def get_realtime_quotes(
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get real-time quotes for futures"""
    try:
        df = ef.futures.get_realtime_quotes()

        if df is None or df.empty:
            rprint("[red]No data available[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="Real-time Futures Quotes", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("history")
def get_quote_history(
    quote_ids: List[str] = typer.Argument(..., help="Quote ID(s) (e.g., 115.ZCM)"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get futures K-line history data"""
    try:
        # If only one quote_id, get single result
        if len(quote_ids) == 1:
            df = ef.futures.get_quote_history(quote_ids[0])

            if df is None or df.empty:
                rprint(f"[red]No data found for quote ID: {quote_ids[0]}[/red]")
                raise typer.Exit(1)

            display_dataframe(df, title=f"Futures History: {quote_ids[0]}", max_rows=limit)

            if output:
                df.to_csv(output, index=False, encoding='utf-8-sig')
                rprint(f"[green]Data saved to {output}[/green]")
        else:
            # Multiple quote_ids
            result = ef.futures.get_quote_history(quote_ids)

            if result is None:
                rprint(f"[red]No data found for quote IDs: {quote_ids}[/red]")
                raise typer.Exit(1)

            for quote_id, df in result.items():
                display_dataframe(df, title=f"Futures History: {quote_id}", max_rows=limit)

            if output:
                rprint("[yellow]Note: Multiple quote IDs selected. Saving to separate files.[/yellow]")
                for quote_id, df in result.items():
                    safe_id = quote_id.replace('.', '_')
                    filename = f"{output.rsplit('.', 1)[0]}_{safe_id}.csv"
                    df.to_csv(filename, index=False, encoding='utf-8-sig')
                    rprint(f"[green]Data saved to {filename}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("deal")
def get_deal_detail(
    quote_id: str = typer.Argument(..., help="Quote ID (e.g., 115.ZCM)"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get futures deal detail"""
    try:
        df = ef.futures.get_deal_detail(quote_id)

        if df is None or df.empty:
            rprint(f"[red]No deal data found for quote ID: {quote_id}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Futures Deal Detail: {quote_id}", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
