"""Type hints for ballotpedia.api.py"""
from typing import Optional

from typing_extensions import TypedDict


class Location(TypedDict):
    lat: float
    long: float


class OfficeHolders(Location):
    collections: Optional[str]


class ElectionDates(TypedDict):
    state: Optional[str]
    type: Optional[str]
    year: Optional[int]
    page: Optional[int]


class ElectionLocation(Location):
    election_date: str
    collections: Optional[str]


class ElectionStates(TypedDict):
    state: str
    election_date: str
    collections: Optional[str]
    office_level: Optional[str]
    office_branch: Optional[str]
    district_type: Optional[str]
    page: Optional[int]


# Optional[
#     Union[
#         SupportsItems[
#             Union[str, bytes, int, float],
#             Union[
#                 str, bytes, int, float, Iterable[Union[str, bytes, int, float]], None
#             ],
#         ],
#         Tuple[
#             Union[str, bytes, int, float],
#             Union[
#                 str, bytes, int, float, Iterable[Union[str, bytes, int, float]], None
#             ],
#         ],
#         Iterable[
#             Tuple[
#                 Union[str, bytes, int, float],
#                 Union[
#                     str,
#                     bytes,
#                     int,
#                     float,
#                     Iterable[Union[str, bytes, int, float]],
#                     None,
#                 ],
#             ]
#         ],
#         str,
#         bytes,
#     ]
# ]
