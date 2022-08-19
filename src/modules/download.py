from urllib.request import urlretrieve


def download_image(img_url: str, img_path: str) -> None:
    urlretrieve(img_url, filename=img_path)
