import typer
import time
from turbocrawler_control.application.crawler.crawler_service import CrawlerService
from rich.console import Console
from rich.table import Table
import subprocess
from turbocrawler_control.application.crawler.crawler_service import CrawlerService
from turbocrawler_control.application.crawler.crawler_error import CrawlerError
from turbocrawler_control.application.scheduled_execution.scheduled_execution_service import ScheduledExecutionService

app = typer.Typer()

console = Console()


def run_crawler(crawler_name: str, output_file__path: str = None) -> None:
    command = "python"
    args = ["--crawler", crawler_name]
    shell_command = [command, *args]

    with open(output_file__path, 'w') as file:
        subprocess.run(
            shell_command,
            stdout=file,
        )


@app.command()
def start_controller():
    console.print('Starting crawler controller')
    while True:
        scheduled_executions, error = ScheduledExecutionService.get_all_scheduled_execution()

        if error:
            if error == CrawlerError.not_found:
                time.sleep(30)
                continue

        for scheduled_execution in scheduled_executions:
            scheduled_execution, error = ScheduledExecutionService.pop_scheduled_execution(
                crawler_name=scheduled_execution.crawler_name)

    ...


@app.command()
def list_crawlers():
    crawlers, error = CrawlerService.get_all_crawlers()
    table = Table("Id", "Name", "Active")
    for crawler in crawlers:
        active = str(crawler.active)
        table.add_row(str(crawler.id), crawler.name, active)
    console.print(table)


if __name__ == "__main__":
    app()
