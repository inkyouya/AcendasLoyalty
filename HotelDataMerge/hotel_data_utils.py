from HotelDataMerge.data_adapters import BaseDataSourceAdapter
from HotelDataMerge.data_merge_utils import merge_hotel_set


def search_hotels(hotels, destination):
    adapters = BaseDataSourceAdapter.__subclasses__()
    filtered_results = []
    for adapter in adapters:
        adapter_instance = adapter()
        source_result = adapter_instance.fetch_and_filter_data(
            hotels, destination
        )
        filtered_results.append(source_result)
    return filtered_results


def merge_data_source_results(data_to_merge):
    result = []
    hotel_id_set = set().union(*data_to_merge)
    for hotel_id in hotel_id_set:
        result.append(
            merge_hotel_set(hotel_id, data_to_merge)
        )
    return result
