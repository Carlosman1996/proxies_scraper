import pytest
from unittest.mock import patch
from proxies_scraper.main import get_proxies
from proxies_scraper.utils.file_operation import JsonFileOperations


@patch('proxies_scraper.main.FreeProxyList')
@patch('proxies_scraper.main.Geonode')
def test_get_proxies(mock_geonode, mock_free_proxy_list):
    free_proxy_list_instance = mock_free_proxy_list.return_value
    geonode_instance = mock_geonode.return_value

    free_proxy_list_instance.get_proxies.return_value = (   # noqa
        JsonFileOperations.read_file("./fixtures/mock_freeProxyList_get_proxies.json"))
    geonode_instance.get_proxies.return_value = (   # noqa
        JsonFileOperations.read_file("./fixtures/mock_geonode_get_proxies.json"))

    results = get_proxies()
    assert list(map(lambda proxy: proxy["ip"], results)) == ["192.168.1.1",
                                                             "192.168.1.2",
                                                             "192.168.1.3",
                                                             "192.168.2.1",
                                                             "192.168.2.2",
                                                             "192.168.2.3"]


@patch('proxies_scraper.main.FreeProxyList')
@patch('proxies_scraper.main.Geonode')
def test_get_proxies_filters_country_https(mock_geonode, mock_free_proxy_list):
    free_proxy_list_instance = mock_free_proxy_list.return_value
    geonode_instance = mock_geonode.return_value

    free_proxy_list_instance.get_proxies.return_value = (   # noqa
        JsonFileOperations.read_file("./fixtures/mock_freeProxyList_get_proxies.json"))
    geonode_instance.get_proxies.return_value = (   # noqa
        JsonFileOperations.read_file("./fixtures/mock_geonode_get_proxies.json"))

    results = get_proxies(country_codes_filter=["CA", "FR"],
                          https_filter=True)
    assert list(map(lambda proxy: proxy["ip"], results)) == ["192.168.1.3", "192.168.2.3"]


@patch('proxies_scraper.main.FreeProxyList')
@patch('proxies_scraper.main.Geonode')
def test_get_proxies_country_anonimity(mock_geonode, mock_free_proxy_list):
    free_proxy_list_instance = mock_free_proxy_list.return_value
    geonode_instance = mock_geonode.return_value

    free_proxy_list_instance.get_proxies.return_value = (   # noqa
        JsonFileOperations.read_file("./fixtures/mock_freeProxyList_get_proxies.json"))
    geonode_instance.get_proxies.return_value = (   # noqa
        JsonFileOperations.read_file("./fixtures/mock_geonode_get_proxies.json"))

    results = get_proxies(country_codes_filter=["CA", "FR", "US"],
                          anonymity_filter=[3, 1])
    assert list(map(lambda proxy: proxy["ip"], results)) == ["192.168.1.1", "192.168.2.3"]
