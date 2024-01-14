import enum
from src.utils.pandas_operations import PandasOperations
from src.utils.postman import Postman



# TODO: refactor and set in general configuration file
PandasOperations.set_printing_options()


class Anonymity(enum.Enum):
    ELITE = 1
    ANONYMOUS = 2
    TRANSPARENT = 3


class Proxies:
    URL = ""
    HEADERS = {}
    MODEL = {
        "ip_address": str,
        "port": str,
        "proxy": str,
        "code": str,
        "country": str,
        "anonymity": bool,
        "https": bool,
        "last_checked": str,
        "created_date": str,
        "created_user": "ordillan",
        "available": True
    }
    MODEL_MAPPER = {}
    TIMEZONE = "Europe/Madrid"

    @staticmethod
    def _type_converter(value, parameter_type):
        if parameter_type == "affirmation":
            if value == "yes":
                return True
            elif value == "no":
                return False
            else:
                return False

        if parameter_type == "protocol":
            if value == "HTTPS" or value == "https":
                return True
            else:
                return False

        if parameter_type == "anonymity":
            if value == "elite proxy" or value == "elite" or value == "Alto anonimato" or value == "Elite":
                return Anonymity.ELITE.value
            elif value == "transparent" or value == "Transparente":
                return Anonymity.TRANSPARENT.value
            elif value == "anonymous" or value == "Anónimo":
                return Anonymity.ANONYMOUS.value
            else:
                return None

        raise Exception(f"Unknown parameter type conversion: {parameter_type}")

    def _api_request(self, url=None) -> dict:
        try:
            response = Postman.send_request(method='GET',
                                            url=self.URL if url is None else url,
                                            headers=self.HEADERS,
                                            status_code_check=200)
        except Exception as exc:
            print(f"Api request failed: {str(exc)}")
            response = {}
        return response

    def _dict_mapper(self, unmapped_dict) -> dict:
        mapped_dict = self.MODEL_MAPPER.copy()
        for key, value in unmapped_dict.items():
            if key in self.MODEL_MAPPER.keys():
                mapped_dict[self.MODEL_MAPPER[key]] = value
        return mapped_dict

    def _model_validator(self, data_dict) -> dict:
        for key in data_dict.keys():
            if key not in self.MODEL.keys():
                raise Exception(f"Data dictionary {data_dict} has incorrect model key: {key}")
        return data_dict

    def get_proxies(self) -> list:
        return []
