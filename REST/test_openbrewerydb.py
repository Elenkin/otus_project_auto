import pytest
import requests

from REST.helper import HelpersApi


base_url = 'https://api.openbrewerydb.org/v1/breweries'

list_brewery_type = pytest.mark.parametrize('brewery_type',
                             [
                                 'micro',
                                 'nano',
                                 'regional',
                                 'planning',
                                 'closed'
                             ])

list_brewery_country = pytest.mark.parametrize('country',
                             [
                                 'United States',
                                 'South Korea',
                                 'England'
                             ])

class TestBrewery:

    @list_brewery_type
    def test_filter_brewery_by_type(self, brewery_type):
        """Filter by type of brewery. Must be one of: {brewery_type}"""

        response = HelpersApi.get_request(base_url, params={'by_type': brewery_type})

        for brewery in response:
            assert brewery['brewery_type'] == brewery_type

    @list_brewery_country
    def test_filter_brewery_by_country(self, country):
        """Filter by country of brewery. Must be one of: {country}"""

        response = HelpersApi.get_request(base_url, params={'by_country': country})

        for brewery in response:
            assert brewery['country'] == country

    def test_check_status_code_200(self):
        """ """
        response = requests.get(base_url)
        assert response.status_code == 200

    def test_default_per_page_50(self):
        """Number of breweries to return each call.
         Default per page 50. Max per page is 200 """

        response = HelpersApi.get_request(base_url)
        assert len(response) == 50

    def test_search_by_city(self):
        """Search for breweries based on a search term"""

        url = f'{base_url}/search'
        city = 'San Diego'

        response = HelpersApi.get_request(url, params={'query': {city}})
        all_cities_are = all(item['city'] == city for item in response)

        if all_cities_are:
            print("Все значения в поле 'city' равны {city}")
        else:
            print("Есть значения, отличные от {city}")
