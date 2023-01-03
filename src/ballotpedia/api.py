"""
Python interface to the Ballotpedia API (https://developer.ballotpedia.org/)

Please note that in order to hit the following endpoints from an application on the internet, you must contact the
Ballotpedia team to whitelist the domains from which those requests will originate. Requests from non-whitelisted origin
domains will receive a preflight CORS permissions error. You are free to run test requests locally or in a non-cors
context such as cURL, Postman, etc.
"""
from datetime import date
from typing import Literal, Optional
import requests

_COLLECTIONS_TYPES = Literal["social", "contact"]
_ELECTION_TYPES = Literal["General", "Primary", "Special", "Recall"]
_OFFICE_TYPES = Literal["Federal", "State", "Local"]
_OFFICE_BRANCH_TYPES = Literal["Legislative", "Executive", "Judicial"]
_DISTRICT_TYPES = Literal["Country", "Congress", "State", "State Legislative (Upper)", "State Legislative (Lower)",
"Judicial District", "County", "County subdivision", "City-town", "School District", "State subdivision",
"Special district subdivision", "Judicial district subdivision", "Special District", "City-town subdivision",
"School district subdivision"]


class Ballotpedia:

    def __init__(self, api_key):
        self.headers = {
            'x-api-key': api_key,
            'Content-Type': 'application/json'
        }

    def districts(self, lat: float, lng: float):
        """
        Given a latitude and longitude point, a list of voting districts will be returned in which that point (address)
        lies.

        :param lat: latitude to search for current office holders
        :param lng: longitude to search for current office holders
        """
        payload = {'lat': lat, 'long': lng}
        return requests.get(f'https://api4.ballotpedia.org/data/districts/point',
                            params=payload,
                            headers=self.headers).json()

    def officeholders(self, lat: float, lng: float, collections: Optional[_COLLECTIONS_TYPES] = None):
        """
        Given a latitude and longitude point, a list of current officeholders representing the point (address) will be
        returned with accompanying information and data points on the district, office, officeholder and person.

        :param lat: latitude to search for current office holders
        :param lng: longitude to search for current office holders
        :param collections: type of collection to search (social,contact)
        """
        payload = {'lat': lat, 'long': lng}
        if collections:
            payload['collections'] = collections
        return requests.get(f'https://api4.ballotpedia.org/data/officeholders',
                            params=payload,
                            headers=self.headers).json()

    def election_dates_by_point(self, lat: float, lng: float):
        """
        Given a latitude and longitude point, a list of election dates will be returned for the particular point
        (address) that have occurred 1 year in the past and will occur 1 year in the future according to today's date.

        :param lat: latitude to search for current office holders
        :param lng: longitude to search for current office holders
        """
        payload = {'lat': lat, 'long': lng}
        return requests.get(f'https://api4.ballotpedia.org/data/election_dates/point',
                            params=payload,
                            headers=self.headers).json()

    def election_dates_list(self,
                            state: Optional[str] = None,
                            election_type: Optional[_ELECTION_TYPES] = None,
                            year: Optional[int] = None,
                            page: Optional[int] = None):
        """
        Election dates can be queried via several parameters which will return data from 2018+ and several years into
        the future. Data is returned in an ascending matter according to date, with limits of 25 results per page.

        :param state: abbreviated state to search
        :param election_type: election type to search (General,Primary,Special,Recall)
        :param year: election year to search
        :param page: data is returned in an ascending matter according to date, with limits of 25 per page; if this is
        specified, then it will return that set of responses. otherwise it will be returned as a generator with 25
        results per iteration
        """
        payload = {}
        if state:
            payload['state'] = state
        if election_type:
            payload['type'] = election_type
        if year:
            payload['year'] = year
        if page:
            payload['page'] = page

        if page:
            return requests.get('https://api4.ballotpedia.org/data/election_dates/list',
                                params=payload,
                                headers=self.headers).json()
        else:
            yield requests.get(f'https://api4.ballotpedia.org/data/election_dates/list',
                               params=payload,
                               headers=self.headers).json()

    def elections_by_point(self, lat: float, lng: float, election_date: date,
                           collections: Optional[_COLLECTIONS_TYPES] = None):
        """
        Given a latitude and longitude point and an election date, a list of candidates, ballot measures and races will
        be returned along with district, office, and person information for the particular point.

        Results of the election will be returned if included in your API package. Including which candidates won/lost,
        vote totals, and which ballot measures were approved or defeated.

        :param lat: latitude to search for current office holders
        :param lng: longitude to search for current office holders
        :param election_date: date of the election
        :param collections: type of collection to search (social,contact)
        """
        payload = {'lat': lat, 'long': lng, 'election_date': election_date.strftime('%Y-%m-%d')}
        if collections:
            payload['collections'] = collections

        return requests.get('https://api4.ballotpedia.org/data/elections_by_point',
                            params=payload,
                            headers=self.headers).json()

    def elections_by_state(self,
                           state: str,
                           election_date: date,
                           collections: Optional[_COLLECTIONS_TYPES] = None,
                           office_level: Optional[_OFFICE_TYPES] = None,
                           office_branch: Optional[_OFFICE_BRANCH_TYPES] = None,
                           district_type: Optional[_DISTRICT_TYPES] = None,
                           page: Optional[int] = None):
        """
        Given a state and an election date, a list of candidates, ballot measures and races will be returned along with
        district, office, and person information for the entire state.

        Results of the election will be returned if included in your API package. Including which candidates won/lost,
        vote totals, and which ballot measures were approved or defeated.

        :param state: abbreviated state to search
        :param election_date: date of the election
        :param collections: type of collection to search (social,contact)
        :param office_level: the office level to search (federal, state, local)
        :param office_branch: the office branch to search (legislative, executive, judicial)
        :param district_type: district type to search (Country,Congress,State,State Legislative (Upper),
        State Legislative (Lower),Judicial District,County,County subdivision,City-town,School District,
        State subdivision,Special district subdivision,Judicial district subdivision,Special District,
        City-town subdivision,School district subdivision)
        :param page: data is returned in an ascending matter according to date, with limits of 25 per page; if this is
        specified, then it will return that set of responses. otherwise it will be returned as a generator with 25
        results per iteration
        """
        payload = {'state': state, 'election_date': election_date}
        if collections:
            payload['collections'] = collections
        if office_level:
            payload['office_level'] = office_level
        if office_branch:
            payload['office_branch'] = office_branch
        if district_type:
            payload['district_type'] = district_type
        if page:
            payload['page'] = page

        if page:
            return requests.get('https://api4.ballotpedia.org/data/elections_by_state',
                                params=payload,
                                headers=self.headers).json()

        yield requests.get('https://api4.ballotpedia.org/data/elections_by_state',
                           params=payload,
                           headers=self.headers).json()