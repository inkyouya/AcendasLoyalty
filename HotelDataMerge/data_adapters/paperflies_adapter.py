from HotelDataMerge.data_adapters.base_adapter import BaseDataSourceAdapter
from HotelDataMerge.constants import PAPERFLIES_URL, PAPERFLIES


class PaperfliesAdapter(BaseDataSourceAdapter):

    def get_data_source_name(self):
        return PAPERFLIES

    def get_data_source_url(self):
        return PAPERFLIES_URL

    def fetch_and_filter_data(self, hotels, destination):
        data = self.fetch_data()
        result = {}

        for hotel in data:
            if str(hotel.get("destination_id")) == destination or hotel.get("hotel_id") in hotels:
                serialized_hotel_data = self.serialize_data(hotel)
                hotel_id = serialized_hotel_data["id"]
                result[hotel_id] = serialized_hotel_data

        return result

    def serialize_data(self, hotel):
        result = {}
        result["id"] = hotel.get("hotel_id")
        result["destination_id"] = hotel.get("destination_id")
        result["name"] = hotel.get("hotel_name")
        result["description"] = hotel.get("details")

        hotel_location = hotel.get("location")
        result["location"] = {
            "lat": None,
            "lng": None,
            "address": hotel_location.get("address"),
            "city": None,
            "country": hotel_location.get("country")
        }

        result["amenities"] = hotel.get("amenities", {})

        hotel_images = hotel.get("images", {})
        result["images"] = {}
        for amenity_type in hotel_images:
            result["images"][amenity_type] = []
            for amenity in hotel_images[amenity_type]:
                result["images"][amenity_type] = {
                    "link": amenity.get("link", ""),
                    "description": amenity.get("caption", "")
                }

        result["booking_conditions"] = hotel.get("booking_conditions")
        return result
