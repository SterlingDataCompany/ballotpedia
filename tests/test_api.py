import data


def test_districts(fixture_ballotpedia, requests_mock):
    """tests ballotpedia.api.districts"""
    requests_mock.get('https://api4.ballotpedia.org/data/districts/point',
                      status_code=200,
                      contents=data.DISTRICTS_RESP)
    ret = fixture_ballotpedia.districts(40.5550746, -74.27596989999999)
    assert ret["success"] == 'true'


def test_officeholders(fixture_ballotpedia, requests_mock):
    """tests ballotpedia.api.officeholders"""
    requests_mock.get('https://api4.ballotpedia.org/data/officeholders',
                      status_code=200,
                      contents=data.OFFICEHOLDERS)
    ret = fixture_ballotpedia.officeholders(-89.3818172, 43.079896, 'contact')
    assert ret["success"] == 'true'


def test_election_dates_by_point(fixture_ballotpedia, requests_mock):
    """tests ballotpedia.api.election_dates_by_point"""
    requests_mock.get('https://api4.ballotpedia.org/data/election_dates/point',
                      status_code=200,
                      contents=data.ELECTION_DATES)
    ret = fixture_ballotpedia.election_dates_by_point(40.5550746, -74.27596989999999)
    assert ret["success"] == 'true'


def test_election_dates_list(fixture_ballotpedia, requests_mock):
    """tests ballotpedia.api.election_dates_list"""
    requests_mock.get('https://api4.ballotpedia.org/data/election_dates/list',
                      status_code=200,
                      contents=data.ELECTION_DATES_NO_PARAM)
    ret = fixture_ballotpedia.election_dates_list()
    assert ret["success"] == 'true'
