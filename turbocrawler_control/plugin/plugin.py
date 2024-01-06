import logging

from turbocrawler import CrawlerRequest, CrawlerResponse, CrawlerRunner, ExecutionInfo
from turbocrawler.engine.plugin import Plugin
from turbocrawler_control.application.crawler.crawler_service import CrawlerService
from turbocrawler.engine.control import StopCrawler
from turbocrawler_control.data.repository.logs_repository import LogsRepository
from turbocrawler_control.presentation.schemas.crawler_schema import CreateCrawlerInput


class TurboCrawlerControlHandler(logging.StreamHandler):
    def __init__(self, running_id: str):
        super().__init__()
        self.running_id = running_id

    def emit(self, record: logging.LogRecord):
        if hasattr(record, 'json'):
            ...
        else:
            LogsRepository.create_log(running_id=self.running_id, level=record.levelname, message=record.msg)


class TurboCrawlerPlugin(Plugin):

    def start_crawler(self) -> None:
        print("[TurboCrawlerPlugin] start_crawler")
        crawler_name = self.crawler.crawler_name
        crawler, error = CrawlerService.find_crawler_by_name(crawler_name)
        if error:
            raise StopCrawler("error to find crawler")

        if not crawler:
            new_crawler = CreateCrawlerInput(name=crawler_name)
            crawler, error = CrawlerService.insert_crawler(new_crawler)

    def crawler_first_request(self) -> None:
        print("[TurboCrawlerPlugin] crawler_first_request")

    def process_request(self, crawler_request: CrawlerRequest) -> CrawlerResponse | CrawlerRequest | None:
        print("[TurboCrawlerPlugin] process_request")
        return None

    def process_response(self, crawler_request: CrawlerRequest, crawler_response: CrawlerResponse) -> CrawlerResponse:
        print("[TurboCrawlerPlugin] process_response")
        return crawler_response

    def stop_crawler(self, execution_info: ExecutionInfo) -> None:
        print("[TurboCrawlerPlugin] process_request")

    def log_handler(self, running_id: str) -> logging.Handler | None:
        return TurboCrawlerControlHandler(running_id)
