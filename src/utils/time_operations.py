from pathlib import Path
import zoneinfo
from datetime import datetime


ROOT_PATH = str(Path(__file__).parent.parent.resolve())


class Time:
    @staticmethod
    def get_datetime(time_zone, format="%Y-%m-%d %H:%M:%S.%f") -> str:
        tz_zone_info = zoneinfo.ZoneInfo(time_zone)
        return str(datetime.now(tz_zone_info).strftime(format))
