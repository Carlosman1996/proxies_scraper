import pytest
from unittest.mock import patch
from proxies_scraper.main import get_proxies
from proxies_scraper.utils.file_operation import JsonFileOperations


@patch('proxies_scraper.main.FreeProxyList')
@patch('proxies_scraper.main.Geonode')
def test_get_proxies_no_filters(mock_geonode, mock_free_proxy_list):
    free_proxy_list_instance = mock_free_proxy_list.return_value
    geonode_instance = mock_geonode.return_value

    free_proxy_list_instance.get_proxies.return_value = (
        JsonFileOperations.read_file("./fixtures/mock_freeProxyList_get_proxies.json"))
    geonode_instance.get_proxies.return_value = (
        JsonFileOperations.read_file("./fixtures/mock_geonode_get_proxies.json"))

    results = get_proxies()
    assert len(results) == 6
