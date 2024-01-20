# main.py
from src.adapters.implementations.freeProxyList import FreeProxyList
from src.adapters.implementations.geonode import Geonode
from src.core.proxy_scraper import ProxyScraper
from src.utils.logger import Logger
from src.utils.file_operation import FileOperations
from src.utils.timer import Timer


# Set logger:
logger = Logger(module=FileOperations.get_file_name(__file__, False),
                level="INFO")  # Set in configuration file


@Timer(logger=logger, text="Proxies found in {:.2f} seconds\n")
def get_proxies(country_codes_filter, anonymity_filter, https_filter):
    logger.set_message(level="INFO",
                       message_level="SECTION",
                       message=f"Start proxies scraper")

    # Configure port adapters
    freeProxyList_adapter = FreeProxyList()
    geonode_adapter = Geonode()

    # Create service with each adapter:
    freeProxyList_service = ProxyScraper(freeProxyList_adapter)
    geonode_service = ProxyScraper(geonode_adapter)

    # Process proxies from different sources:
    processed_proxies = []
    processed_proxies += freeProxyList_service.get_proxies(country_codes_filter, anonymity_filter, https_filter)
    processed_proxies += geonode_service.get_proxies(country_codes_filter, anonymity_filter, https_filter)

    logger.set_message(level="INFO",
                       message_level="SECTION",
                       message=f"Finish proxies scraper")

    logger.set_message(level="INFO",
                       message=f"Number of proxies scraped: {len(processed_proxies)}")

    return processed_proxies


if __name__ == "__main__":
    get_proxies()
