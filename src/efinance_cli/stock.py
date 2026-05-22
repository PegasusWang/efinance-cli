"""
Stock related commands
"""
import typer
from typing import Optional, List
from datetime import datetime
from rich import print as rprint
import pandas as pd
import efinance as ef
from efinance_cli.main import display_dataframe

app = typer.Typer(help="Stock market data commands")


@app.command("history")
def get_quote_history(
    code: str = typer.Argument(..., help="Stock code (e.g., 600519 for 贵州茅台)"),
    start_date: Optional[str] = typer.Option(None, "--start", "-s", help="Start date (YYYY-MM-DD)"),
    end_date: Optional[str] = typer.Option(None, "--end", "-e", help="End date (YYYY-MM-DD)"),
    klt: int = typer.Option(101, "--klt", "-k", help="K-line type: 101=day, 102=week, 103=month, 5=5min, 15=15min, 30=30min, 60=60min"),
    fqt: int = typer.Option(1, "--fqt", "-f", help="Adjustment type: 0=none, 1=forward, 2=backward"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get stock K-line history data"""
    try:
        df = ef.stock.get_quote_history(code, beg=start_date, end=end_date, klt=klt, fqt=fqt)

        if df is None or df.empty:
            rprint(f"[red]No data found for stock {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Stock History: {code}", max_rows=limit)

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
    """Get real-time quotes for all A-shares"""
    try:
        df = ef.stock.get_realtime_quotes()

        if df is None or df.empty:
            rprint("[red]No data available[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="Real-time Quotes (A-shares)", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("billboard")
def get_daily_billboard(
    start_date: Optional[str] = typer.Option(None, "--start", "-s", help="Start date (YYYY-MM-DD)"),
    end_date: Optional[str] = typer.Option(None, "--end", "-e", help="End date (YYYY-MM-DD)"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get daily billboard (龙虎榜) data"""
    try:
        df = ef.stock.get_daily_billboard(start_date=start_date, end_date=end_date)

        if df is None or df.empty:
            rprint("[red]No data available[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="Daily Billboard", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("performance")
def get_company_performance(
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get quarterly performance of all companies"""
    try:
        df = ef.stock.get_all_company_performance()

        if df is None or df.empty:
            rprint("[red]No data available[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="Company Performance", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("base-info")
def get_base_info(
    codes: List[str] = typer.Argument(..., help="Stock codes (space-separated)"),
):
    """Get basic information for stocks"""
    try:
        df = ef.stock.get_base_info(codes)

        if df is None or df.empty:
            rprint(f"[red]No data found for stocks: {codes}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="Stock Basic Information")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("holder")
def get_top10_holder(
    code: str = typer.Argument(..., help="Stock code"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
):
    """Get top 10 stock holders information"""
    try:
        df = ef.stock.get_top10_stock_holder_info(code)

        if df is None or df.empty:
            rprint(f"[red]No holder data found for stock {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Top 10 Holders: {code}")

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("report-dates")
def get_all_report_dates(
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
):
    """Get all report dates"""
    try:
        df = ef.stock.get_all_report_dates()

        if df is None or df.empty:
            rprint("[red]No data available[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="All Report Dates")

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("board")
def get_belong_board(
    code: str = typer.Argument(..., help="Stock code"),
):
    """Get the board that the stock belongs to"""
    try:
        df = ef.stock.get_belong_board(code)

        if df is None or df.empty:
            rprint(f"[red]No board data found for stock {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Belong Board: {code}")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("deal")
def get_deal_detail(
    code: str = typer.Argument(..., help="Stock code"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get stock deal detail"""
    try:
        df = ef.stock.get_deal_detail(code)

        if df is None or df.empty:
            rprint(f"[red]No deal data found for stock {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Deal Detail: {code}", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("history-bill")
def get_history_bill(
    code: str = typer.Argument(..., help="Stock code"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get historical bill (capital flow) data"""
    try:
        df = ef.stock.get_history_bill(code)

        if df is None or df.empty:
            rprint(f"[red]No history bill data found for stock {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"History Bill: {code}", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("holder-number")
def get_latest_holder_number(
    code: str = typer.Argument(..., help="Stock code"),
):
    """Get latest holder number"""
    try:
        df = ef.stock.get_latest_holder_number(code)

        if df is None or df.empty:
            rprint(f"[red]No holder number data found for stock {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Latest Holder Number: {code}")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("ipo")
def get_latest_ipo_info(
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get latest IPO information"""
    try:
        df = ef.stock.get_latest_ipo_info()

        if df is None or df.empty:
            rprint("[red]No IPO data available[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="Latest IPO Information", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("latest-quote")
def get_latest_quote(
    codes: List[str] = typer.Argument(..., help="Stock codes (space-separated)"),
):
    """Get latest quote for stocks"""
    try:
        df = ef.stock.get_latest_quote(codes)

        if df is None or df.empty:
            rprint(f"[red]No quote data found for stocks: {codes}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="Latest Quote")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("members")
def get_members(
    board_code: str = typer.Argument(..., help="Board code"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
):
    """Get board members"""
    try:
        df = ef.stock.get_members(board_code)

        if df is None or df.empty:
            rprint(f"[red]No members found for board {board_code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Board Members: {board_code}")

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("snapshot")
def get_quote_snapshot(
    codes: List[str] = typer.Argument(..., help="Stock codes (space-separated)"),
):
    """Get quote snapshot"""
    try:
        df = ef.stock.get_quote_snapshot(codes)

        if df is None or df.empty:
            rprint(f"[red]No snapshot data found for stocks: {codes}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title="Quote Snapshot")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command("today-bill")
def get_today_bill(
    code: str = typer.Argument(..., help="Stock code"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (CSV format)"),
    limit: int = typer.Option(50, "--limit", "-l", help="Maximum number of rows to display"),
):
    """Get today's bill (capital flow) data"""
    try:
        df = ef.stock.get_today_bill(code)

        if df is None or df.empty:
            rprint(f"[red]No today bill data found for stock {code}[/red]")
            raise typer.Exit(1)

        display_dataframe(df, title=f"Today Bill: {code}", max_rows=limit)

        if output:
            df.to_csv(output, index=False, encoding='utf-8-sig')
            rprint(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        rprint(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
