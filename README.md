# Springer Proceedings Extractor

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
3. Save the provided script to your local machine.
4. Open your terminal and navigate to the directory where the script is saved.
5. Run the following command to execute the script:
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
python script.py proceedings.pdf -o articles
```

To extract articles with a specific title pattern, you can provide a filter
using the `-f` option. For example, to extract articles with titles containing the
word "machine learning", you can run the following command:
```
python script.py proceedings.pdf -f "machine learning"
