"""
Fund related commands
"""
import typer
from typing import Optional, List
from rich import print as rprint
import efinance as ef
from efinance_cli.main import display_dataframe

app = typer.Typer(help="Fund market data commands")


@app.command("history")
def get_quote_history(
    code: str = typer.Argument(..., help="Fund code (e.g., 161725)"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get fund net value history"""
    try:
        df = ef.fund.get_quote_history(code)

        if df is None or df.empty:
            rprint(f"[red]No data found for fund {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Fund History: {code}", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("position")
def get_invest_position(
    code: str = typer.Argument(..., help="Fund code"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
):
    """Get fund investment position"""
    try:
        df = ef.fund.get_invest_position(code)

        if df is None or df.empty:
            rprint(f"[red]No position data found for fund {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Fund Position: {code}")

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("base-info")
def get_base_info(
    codes: List[str] = typer.Argument(..., help="Fund codes (space-separated)"),
):
    """Get basic information for funds"""
    try:
        df = ef.fund.get_base_info(codes)

        if df is None or df.empty:
            rprint(f"[red]No data found for funds: {codes}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="Fund Basic Information")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("manager")
def get_fund_manager(
    code: str = typer.Argument(..., help="Fund code"),
):
    """Get fund manager information"""
    try:
        df = ef.fund.get_fund_manager(code)

        if df is None or df.empty:
            rprint(f"[red]No manager data found for fund {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Fund Manager: {code}")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("codes")
def get_fund_codes():
    """Get all fund codes"""
    try:
        df = ef.fund.get_fund_codes()

        if df is None or df.empty:
            rprint("[red]No fund codes available[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="All Fund Codes", max_rows=50)

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("industry")
def get_industry_distribution(
    code: str = typer.Argument(..., help="Fund code"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
):
    """Get fund industry distribution"""
    try:
        df = ef.fund.get_industry_distribution(code)

        if df is None or df.empty:
            rprint(f"[red]No industry distribution data found for fund {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Industry Distribution: {code}")

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("pdf-reports")
def get_pdf_reports(
    code: str = typer.Argument(..., help="Fund code"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
):
    """Get fund PDF reports"""
    try:
        df = ef.fund.get_pdf_reports(code)

        if df is None or df.empty:
            rprint(f"[red]No PDF reports found for fund {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"PDF Reports: {code}")

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("period-change")
def get_period_change(
    code: str = typer.Argument(..., help="Fund code"),
):
    """Get fund period change"""
    try:
        df = ef.fund.get_period_change(code)

        if df is None or df.empty:
            rprint(f"[red]No period change data found for fund {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Period Change: {code}")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("public-dates")
def get_public_dates(
    code: str = typer.Argument(..., help="Fund code"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
):
    """Get fund public dates"""
    try:
        df = ef.fund.get_public_dates(code)

        if df is None or df.empty:
            rprint(f"[red]No public dates found for fund {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Public Dates: {code}")

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("history-multi")
def get_quote_history_multi(
    codes: List[str] = typer.Argument(..., help="Fund codes (space-separated)"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get multiple funds history data"""
    try:
        result = ef.fund.get_quote_history_multi(codes)

        if result is None:
            rprint(f"[red]No data found for funds: {codes}[/red]")
            raise typer.Exit(1)

        # result is a dict of DataFrames
        for code, df in result.items():
            display_dataframe(df, title=f"Fund History: {code}", max_rows=limit)

        if output:
            rprint("[yellow]Note: Multiple funds selected. Saving to separate files.[/yellow]")
            for code, df in result.items():
                filename = f"{output.rsplit('.', 1)[0]}_{code}.csv"
                df.to_csv(filename, index=False, encoding='utf-8-sig')
                rprint(f"[green]Data saved to {filename}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("realtime-rate")
def get_realtime_increase_rate(
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get real-time increase rate for all funds"""
    try:
        df = ef.fund.get_realtime_increase_rate()

        if df is None or df.empty:
            rprint("[red]No data available[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="Real-time Increase Rate", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("types")
def get_types_percentage(
    code: str = typer.Argument(..., help="Fund code"),
):
    """Get fund types percentage"""
    try:
        df = ef.fund.get_types_percentage(code)

        if df is None or df.empty:
            rprint(f"[red]No types percentage data found for fund {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Types Percentage: {code}")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
