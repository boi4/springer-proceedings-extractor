# Springer Proceedings Extractor

![it-aint-much-meme](https://github.com/boi4/springer-proceedings-extractor/assets/33987679/28c77871-7c18-4849-8985-c64502cd9dda)

Don't you love it when you download an article from Springer and suddendly you are greeted with a 200MB PDF with far too many pages?

Me neither! That's why I wrote this little script .

## Description

This is a Python script that allows you to extract articles from a Springer Proceedings PDF into separate PDF files.

## Usage

To use this script, follow the steps below:

1. Ensure that you have Python 3 installed on your system.
2. Install the required libraries by running the following command in your
terminal:
```
pip install PyPDF2
```
3. Run the following command to execute the script:
```
./springer_extract.py <filename> -f <filter> -o <output_directory>
```
Replace `<filename>` with the name of the PDF file you want to extract from.
Replace `<filter>` with an optional case-insensitive regex expression to filter
the articles by title.
Replace `<output_directory>` with an optional directory to save the extracted
articles. If not provided, a directory will be created using the name of the
input file.

The script will parse the PDF file, extract the specified articles, and save
them as separate PDF files in the specified output directory.


## Example

To extract articles from a PDF file named "proceedings.pdf" and save them in a
directory named "articles", you can run the following command:
```
./springer_extract.py proceedings.pdf -o articles
```

To extract articles with a specific title pattern, you can provide a filter
using the `-f` option. For example, to extract articles with titles containing the
word "machine learning", you can run the following command:
```
./springer_extract.py proceedings.pdf -f "machine learning"
