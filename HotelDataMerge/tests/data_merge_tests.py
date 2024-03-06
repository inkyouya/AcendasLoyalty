from django.test import TestCase
from HotelDataMerge.data_merge_utils import (
    get_all_value_with_key,
    pick_highest_occurance,
    pick_longest,
    merge_unique_lists,
    merge_lists,
    pick_location,
    pick_amenities,
    pick_images,
)


class DataMergeUtilsTestCase(TestCase):
    def test_get_all_value_with_key(self):
        data = [
            {"description": "A", "other_key": "G"},
            {"description": "B"},
            {"description": "C"},
            {"description": None},
            {"wrong_key": 1},
        ]
        result = get_all_value_with_key("description", data)
        self.assertIsInstance(result, list)
        self.assertEqual(result, ['A', 'B', 'C'])

    def test_pick_highest_occurance(self):
        data = [1, 1, 5, 3, "A", 1]
        result = pick_highest_occurance(data)
        self.assertEqual(result, 1)

    def test_pick_longest(self):
        data = [
            [1],
            [1, 3, 5, 2, 1],
            [56],
            [4, 7, 1]
        ]
        result = pick_longest(data)
        self.assertEqual(result, [1, 3, 5, 2, 1])

    def test_merge_unique_lists(self):
        data = [
            [1],
            [1, 3, 5, 2, 1],
            [56],
            [4, 7, 1]
        ]
        result = merge_unique_lists(data)
        self.assertIsInstance(result, list)
        self.assertEqual(result, [1, 2, 3, 4, 5, 7, 56])

    def test_merge_lists(self):
        data = [
            [1],
            [1, 3, 5, 2, 1],
            [56],
            [4, 7, 1]
        ]
        result = merge_lists(data)
        self.assertIsInstance(result, list)
        self.assertEqual(result, [1, 1, 3, 5, 2, 1, 56, 4, 7, 1])

    def test_pick_location(self):
        data = [
            {
                "lat": 1,
                "lng": 2,
                "address": "test_address",
                "city": "test_city",
                "country": "test_country"
            },
            {
                "lat": 1,
                "lng": 2,
                "address": "test_address",
                "city": "test_city",
                "country": "other_test_country"
            },
            {
                "lat": 5,
                "lng": 6,
                "address": "other_test_address",
                "city": "other_test_address",
                "country": "test_country"
            },
            {
                "lat": None,
                "lng": None,
                "address": None,
                "city": None,
                "country": None
            }
        ]
        result = pick_location(data)
        self.assertIsInstance(result, dict)
        self.assertDictEqual(
            result,
            {
                "lat": 1,
                "lng": 2,
                "address": "test_address",
                "city": "test_city",
                "country": "test_country"
            }
        )

    def test_pick_amenities(self):
        data = [
            {
                "general": ["outdoor pool", "indoor pool"],
                "room": ["tv", "coffee machine"]
            },
            {
                "general": ["outdoor pool", "business center"],
                "room": ["aircon"]
            }
        ]
        result = pick_amenities(data)
        self.assertIsInstance(result, dict)
        self.assertDictEqual(
            result,
            {
                "general": ["outdoor pool", "indoor pool"],
                "room": ["tv", "coffee machine"]
            }
        )

    def test_pick_images(self):
        data = [
            {
                "rooms": [
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg",
                        "description": "Double room"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/4.jpg",
                        "description": "Bathroom"
                    }
                ],
                "amenities": [
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/0.jpg",
                        "description": "RWS"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/6.jpg",
                        "description": "Sentosa Gateway"
                    }
                ]
            },
            {
                "rooms": [
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/YwAr/i10_m.jpg",
                        "description": "Suite"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/YwAr/i11_m.jpg",
                        "description": "Suite - Living room"
                    }
                ],
                "amenities": [
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/YwAr/i57_m.jpg",
                        "description": "Bar"
                    }
                ]
            }
        ]
        result = pick_images(data)
        self.assertIsInstance(result, dict)
        self.assertDictEqual(
            result,
            {
                "rooms": [
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg",
                        "description": "Double room"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/4.jpg",
                        "description": "Bathroom"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/YwAr/i10_m.jpg",
                        "description": "Suite"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/YwAr/i11_m.jpg",
                        "description": "Suite - Living room"
                    }
                ],
                "amenities": [
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/0.jpg",
                        "description": "RWS"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/6.jpg",
                        "description": "Sentosa Gateway"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/YwAr/i57_m.jpg",
                        "description": "Bar"
                    }
                ]
            }
        )
