from src.adapters.ports.proxies_source import Proxies
from src.utils.logger import Logger
from src.utils.file_operation import FileOperations


class ProxyScraper:
    def __init__(self, proxy_port: Proxies):
        self.proxy_port = proxy_port

        # Set logger:
        self._logger = Logger(module=FileOperations.get_file_name(__file__, False),
                              level="INFO")  # Set in configuration file

    def _get_page_proxies(self):
        proxies = []
        try:
            proxies = self.proxy_port.get_proxies()
        except Exception as e:
            self._logger.set_message(level="WARNING",
                                     message_level="MESSAGE",
                                     message=f"Proxies page {str(self.proxy_port.NAME)} scraping failed due to the "
                                             f"following exception {str(e)}")
        return proxies

    @staticmethod
    def _filter_proxies(proxies, country_codes_filter, anonymity_filter, https_filter):
        if isinstance(country_codes_filter, list):
            proxies = [proxy for proxy in proxies if proxy['country_code'] in country_codes_filter]
        if isinstance(country_codes_filter, list):
            proxies = [proxy for proxy in proxies if proxy['anonymity'] in anonymity_filter]
        if isinstance(country_codes_filter, bool):
            proxies = [proxy for proxy in proxies if proxy['https'] == https_filter]
        return proxies

    def get_proxies(self,
                    country_codes_filter: list = None,
                    anonymity_filter: list = None,
                    https_filter: bool = None):

        self._logger.set_message(level="INFO",
                                 message_level="SUBSECTION",
                                 message=f"Process proxies from {self.proxy_port.NAME}")

        self._logger.set_message(level="INFO",
                                 message="Read proxies")
        proxies = self._get_page_proxies()

        self._logger.set_message(level="INFO",
                                 message="Filter proxies")
        proxies = self._filter_proxies(proxies, country_codes_filter, anonymity_filter, https_filter)

        return proxies
