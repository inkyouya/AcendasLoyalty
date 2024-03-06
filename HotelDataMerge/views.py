import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from HotelDataMerge.hotel_data_utils import (
    search_hotels,
    merge_data_source_results,
)

logger = logging.getLogger(__name__)


class HotelView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self, request):
        hotels = request.query_params.getlist("hotels")  # list of hotel IDs
        destination = request.query_params.get("destination")  # a given destination ID

        try:
            unmerged_results = search_hotels(hotels, destination)
            merged_results = merge_data_source_results(unmerged_results)
        except Exception as e:
            logger.exception(
                f"Hotel search error: {e}"
            )
            return Response(
                {},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            merged_results,
            status=status.HTTP_200_OK
        )
