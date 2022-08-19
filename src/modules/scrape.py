from typing import Dict, Optional
from urllib import request
from urllib.parse import urljoin

from bs4 import BeautifulSoup as bs


def get_soup(url: str) -> bs:
    webpage = request.urlopen(url)
    return bs(webpage, "html.parser")


def find_title(soup: bs) -> str:
    return soup.find("meta", attrs={"property": "og:title"})["content"]


def find_image_url(soup: bs, page: int) -> str:
    imglink3 = soup.find("meta", attrs={"property": "og:image"})["content"]
    imglink2 = imglink3.replace("1.jpg", "")
    return f"{imglink2}{page}.jpg"


def find_metadata(soup: bs, url: str, title: str) -> Dict[str, str]:
    def find_uploaded_time(soup: bs) -> Optional[str]:
        uploaded_time = soup.find("div", attrs={"itemprop": "datePublished"})
        if uploaded_time is not None:
            return uploaded_time["datetime"]

    def find_uploaded_link(soup: bs) -> Optional[str]:
        uploaded_link = soup.find("div", attrs={"class": "PublisherInfo__name--3j27Y"})
        if uploaded_link is not None:
            return urljoin("https://issuu.com", uploaded_link.a["href"])

    def find_description(soup: bs) -> Optional[str]:
        description = soup.find("meta", attrs={"property": "og:description"})
        if description is not None:
            return description["content"]

    def find_author(soup: bs) -> Optional[str]:
        find_author = soup.find("a", attrs={"itemprop": "author"})
        if find_author is not None:
            return find_author.contents[0]

    return {
        "URL": url,
        "description": find_description(soup),
        "uploaded": find_uploaded_time(soup),
        "uploaded_link": find_uploaded_link(soup),
        "author": find_author(soup),
        "title": title,
    }
