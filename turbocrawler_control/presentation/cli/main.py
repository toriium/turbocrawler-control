import typer
from rich.console import Console
from rich.table import Table

from turbocrawler_control.application.crawler.crawler_service import CrawlerService

console = Console()

app = typer.Typer()


@app.command()
def list():
    crawlers, error = CrawlerService.get_all_crawlers()
    table = Table("Id", "Name")
    for crawler in crawlers:
        table.add_row(str(crawler.id), crawler.name)
    console.print(table)


@app.command()
def main2():
    ...


if __name__ == "__main__":
    app()
