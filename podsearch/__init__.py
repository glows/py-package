"""Let's Find Some podcasts!"""

__version__ = "0.1.0"
SEARCH_URL = ""


@dataclass
class Podcast:
    """Podcast metadata"""

    id: str
    name: str
    author: str
    url: str
    feed: Optional[str] = None
    category: Optional[str] = None
    image: Optional[str] = None


def search(name, count=5):
    """Search podcast by name."""
    # raise NotImplementedError()
    params = {"term": name, "limit": limit}

    response = _get(url=SEARCH_URL)
    return _parse(reponse)
