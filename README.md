# Issuu : from reader Iframe to PDF

## Objectif 

**Issuu** platform share a lot of documents but some of them are not dowloadable. The problem for me is that I like to keep track of my readings and join notes with them. 
This package a only one usage : **download some or all pages from the site and merge it into a nice pdf format.**


## Basic usage

 1. Run : `python3 ./main.py`;
 2. Input `URL`; 
 3. Input the `page count` you want ;

## Features 

 * Loading pages as `jpg` file in `./temp`folder;
 * Metada saved in json format in `./out`folder;
 * URL parsed saved in txt format in `./out` folder;
 * Some logging for debugging ;
 * Progress bar ;

## Requirements

### Python

This script requires Python 3 and BeautifulSoup. To install the required packages:

#### Conda users (For the exact configuration I uses)

    conda env create -f ENV.yml
    conda activate scrape_issuu

#### Pip users 

    pip3 install bs4

### ImageMagick

This package also requires the `convert` command from [ImageMagick](https://www.imagemagick.org/)

#### Known issues 

 * memory issues, go see [this github thread](https://github.com/ImageMagick/ImageMagick/issues/396);
 * authorization issue, go see this [askubuntu thread](https://askubuntu.com/questions/1081895/trouble-with-batch-conversion-of-png-to-pdf-using-convert)

## Credits

This package is **mainly a refactoring**s of https://github.com/dkl3/py-issuu-scrape . Thanks dude :). 

dkl3 was inspired by the Ruby script from pietrop: https://github.com/pietrop/issuu.com-downloader as well as dkl3's original python script: https://github.com/dkl3/py-issuu-scrape
