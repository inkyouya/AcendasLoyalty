import logging
import requests

from django.core.cache import cache
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class BaseDataSourceAdapter(ABC):

    @abstractmethod
    def get_data_source_name(self):
        pass

    @abstractmethod
    def get_data_source_url(self):
        pass

    def fetch_data(self, force=False):
        url = self.get_data_source_url()
        source_name = self.get_data_source_name()

        cached_resp = cache.get(source_name)
        if cached_resp:
            return cached_resp

        try:
            resp = requests.get(url)
            resp.raise_for_status()
            resp_json = resp.json()
            cache.set(source_name, resp_json, timeout=1000)
            return resp_json
        except Exception as e:
            logger.exception(
                f"Error fetching data from {source_name}: {e}"
            )
            return {}

    @abstractmethod
    def fetch_and_filter_data(self, hotels, destination):
        pass

    @abstractmethod
    def serialize_data(self):
        pass
