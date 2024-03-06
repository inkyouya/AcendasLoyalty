from HotelDataMerge.data_adapters.base_adapter import BaseDataSourceAdapter
from HotelDataMerge.constants import PATAGONIA_URL, PATAGONIA


class PatagoniaAdapter(BaseDataSourceAdapter):

    def get_data_source_name(self):
        return PATAGONIA

    def get_data_source_url(self):
        return PATAGONIA_URL

    def fetch_and_filter_data(self, hotels, destination):
        data = self.fetch_data()
        result = {}

        for hotel in data:
            if str(hotel.get("destination")) == destination or hotel.get("id") in hotels:
                serialized_hotel_data = self.serialize_data(hotel)
                hotel_id = serialized_hotel_data["id"]
                result[hotel_id] = serialized_hotel_data

        return result

    def serialize_data(self, hotel):
        result = {}
        result["id"] = hotel.get("id")
        result["destination"] = hotel.get("destination")
        result["name"] = hotel.get("name")
        result["description"] = hotel.get("info")

        result["location"] = {
            "lat": hotel.get("lat"),
            "lng": hotel.get("lng"),
            "address": hotel.get("address"),
            "city": None,
            "country": None
        }

        amenities = hotel.get("amenities", [])
        if not amenities:  # account for null
            amenities = []
        result["amenities"] = {
            "room": amenities
        }

        hotel_images = hotel.get("images", {})
        result["images"] = {}
        for amenity_type in hotel_images:
            result["images"][amenity_type] = []
            for amenity in hotel_images[amenity_type]:
                result["images"][amenity_type].append(
                    {
                        "link": amenity.get("url"),
                        "description": amenity.get("description")
                    }
                )

        result["booking_conditions"] = []
        return result
