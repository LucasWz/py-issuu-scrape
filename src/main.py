from modules.convert_to_pdf import convert_img_to_pdf
from modules.download import download_image
from modules.helpers import clean_temp_folder, save_metadata, save_url
from modules.scrape import find_image_url, find_metadata, find_title, get_soup
from modules.user_inputs import get_page_count, get_url
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main() -> None:
    TEMP_FILES = "../temp/*"
    URL_PATH = "../out/url.txt"
    METADATA_PATH = "../out/metdata.json"
    img_path = "../temp/page_{}.jpg".format
    pdf_path = "../out/{}.pdf".format

    url = get_url()
    page_count = get_page_count()

    soup = get_soup(url)

    title = find_title(soup)
    metadata = find_metadata(soup, url, title)
    save_metadata(metadata, METADATA_PATH)
    metadata_string = "\n".join([f"'{k}':'{v}'" for k, v in metadata.items()])
    logging.info("Metadata saved:\n{}".format(metadata_string))

    for page in range(1, page_count + 1):

        img_url = find_image_url(soup, page)
        logger.info("Page {}: {}".format(page, img_url))
        download_image(img_url, img_path(page))
        save_url(img_url, URL_PATH)

    logger.info("Converting {} pages to PDF.".format(page_count))
    convert_img_to_pdf(TEMP_FILES, pdf_path(title.replace(" ", "-")))

    clean_temp_folder(TEMP_FILES)
    logger.info("Book : '{}' saved successfully.".format(title))


if __name__ == "__main__":
    main()
