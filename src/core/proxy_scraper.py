from src.adapters.ports.proxies import Proxies


class ProxyScraper:
    def __init__(self, proxy_port: Proxies):
        self.proxy_port = proxy_port

    def process_proxies(self):
        proxies = self.proxy_port.get_proxies()

        # Validate proxies result:


        return proxies
