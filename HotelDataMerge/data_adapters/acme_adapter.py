import pycountry

from HotelDataMerge.data_adapters.base_adapter import BaseDataSourceAdapter
from HotelDataMerge.constants import ACME_URL, ACME


class AcmeAdapter(BaseDataSourceAdapter):

    def get_data_source_name(self):
        return ACME

    def get_data_source_url(self):
        return ACME_URL

    def fetch_and_filter_data(self, hotels, destination):
        data = self.fetch_data()
        result = {}

        for hotel in data:
            if str(hotel.get("DestinationId")) == destination or hotel.get("Id") in hotels:
                serialized_hotel_data = self.serialize_data(hotel)
                hotel_id = serialized_hotel_data["id"]
                result[hotel_id] = serialized_hotel_data

        return result

    def serialize_data(self, hotel):
        result = {}
        result["id"] = hotel.get("Id")
        result["destination_id"] = hotel.get("DestinationId")
        result["name"] = hotel.get("Name")
        result["description"] = hotel.get("Description")

        country = pycountry.countries.get(
            alpha_2=hotel.get("Country")
        ).name
        result["location"] = {
            "lat": hotel.get("Latitude"),
            "lng": hotel.get("Longitude"),
            "address": hotel.get("Address"),
            "city": hotel.get("City"),
            "country": country
        }

        result["amenities"] = {}
        result["images"] = {}
        result["booking_conditions"] = []
        return result
