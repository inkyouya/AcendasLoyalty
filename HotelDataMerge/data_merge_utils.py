def merge_hotel_set(hotel_id, hotel_dict):
    list_of_hotel = []
    for hotel_data in hotel_dict:
        if hotel_id in hotel_data:
            list_of_hotel.append(hotel_data[hotel_id])

    result = {}
    result["id"] = hotel_id

    destination_id_list = get_all_value_with_key("destination_id", list_of_hotel)
    result["destination_id"] = pick_highest_occurance(destination_id_list)

    name_list = get_all_value_with_key("name", list_of_hotel)
    result["name"] = pick_highest_occurance(name_list)

    description_list = get_all_value_with_key("description", list_of_hotel)
    result["description"] = pick_longest(description_list)

    location_list = get_all_value_with_key("location", list_of_hotel)
    result["location"] = pick_location(location_list)

    amenities_list = get_all_value_with_key("amenities", list_of_hotel)
    result["amenities"] = pick_amenities(amenities_list)

    booking_conditions_list = get_all_value_with_key(
        "booking_conditions", list_of_hotel
    )
    result["booking_conditions"] = merge_unique_lists(booking_conditions_list)

    images_list = get_all_value_with_key("images", list_of_hotel)
    result["images"] = pick_images(images_list)

    return result


def get_all_value_with_key(key, data_sets):
    result = []
    for data_set in data_sets:
        if key in data_set and data_set[key] is not None:
            result.append(
                data_set[key]
            )
    return result


def pick_highest_occurance(data_list):
    if not data_list:
        return None
    return max(set(data_list), key=data_list.count)


def pick_longest(data_list):
    if not data_list:
        return None
    return sorted(data_list, key=len, reverse=True)[0]


def merge_unique_lists(data_list):
    result = set()
    for item in data_list:
        result = result.union(set(item))
    return list(result)


def merge_lists(data_list):
    result = []
    for item in data_list:
        result += item
    return result


def pick_location(data_list):
    result = {}
    lat_list = get_all_value_with_key("lat", data_list)
    lng_list = get_all_value_with_key("lng", data_list)
    address_list = get_all_value_with_key("address", data_list)
    city_list = get_all_value_with_key("city", data_list)
    country_list = get_all_value_with_key("country", data_list)
    result = {
        "lat": pick_highest_occurance(lat_list),
        "lng": pick_highest_occurance(lng_list),
        "address": pick_highest_occurance(address_list),
        "city": pick_highest_occurance(city_list),
        "country": pick_highest_occurance(country_list)
    }
    return result


def pick_amenities(data_list):
    result = {}
    amenities_types = set().union(*data_list)
    for amenities_type in amenities_types:
        amentity_list = []
        for data_point in data_list:
            if amenities_type in data_point:
                amentity_list.append(data_point[amenities_type])
        result[amenities_type] = pick_longest(amentity_list)
    return result


def pick_images(data_list):
    result = {}
    image_types = set().union(*data_list)
    for image_type in image_types:
        image_lists = get_all_value_with_key(image_type, data_list)
        result[image_type] = merge_lists(image_lists)
    return result