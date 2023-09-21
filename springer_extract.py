#!/usr/bin/env python3
import argparse
import os
import re

import PyPDF2


def parse_outline_items(fname):
    """
    Parse the outline items from the PDF file fname
    returns a list of 3-tuples, (title, page number start, page number end) for each article
    """

    # 3-tuples, (title, page number start, page number end)
    titles_and_pages = []

    # Open the PDF file in read-binary mode
    pdf_reader = PyPDF2.PdfReader(open(fname, 'rb'))


    since_article_cnt = 100
    for item in pdf_reader.outline:
        since_article_cnt += 1

        if since_article_cnt == 2:
            pagenum = pdf_reader.get_destination_page_number(item)
            titles_and_pages[-1] = (titles_and_pages[-1][0], titles_and_pages[-1][1], pagenum-1)

        # so far, this is unique to outline elements containing an article
        if '/Count' in item and item['/Count'] > 0:
            pagenum = pdf_reader.get_destination_page_number(item)
            titles_and_pages.append((item.title, pagenum, pagenum))
            since_article_cnt = 0

    return titles_and_pages


def cat_pdf(fname, start_page, end_page, output_fname):
    """
    Extract pages start_page to end_page from fname and save to output_fname
    """
    pdf_reader = PyPDF2.PdfReader(open(fname, 'rb'))
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(start_page, end_page + 1):
        page_obj = pdf_reader.pages[page_num]
        pdf_writer.add_page(page_obj)

    pdf_output_file = open(output_fname, 'wb')
    pdf_writer.write(pdf_output_file)
    pdf_output_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extracts the articles from a Springer Proceedings PDF.')
    parser.add_argument('filename', type=str, help='the filename of the PDF to extract from')
    parser.add_argument('-f', '--filter', type=str, help='only extract articles with this case insenstivie regex in the title', default=None)
    parser.add_argument('-o', '--output', type=str, help='the directory to output the articles to', default=None)

    args = parser.parse_args()

    if args.output is None:
        output_dir = os.path.splitext(os.path.basename(args.filename))[0]
    else:
        output_dir = args.output

    # create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # parse the outline items
    outline_items = parse_outline_items(args.filename)


    # extract the articles
    for i, (title, start_page, end_page) in enumerate(outline_items):
        if args.filter and not re.search(args.filter, title, re.IGNORECASE):
                continue
        # sanitize title
        title = title.lower().replace(" ", "-").replace(':', '').replace('?', '').replace('/', '-').replace('\\', '-').replace('*', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
        output_fname = os.path.join(output_dir, f"{i+1:03}-" + title + '.pdf')
        print(f"Extracting {output_fname} from pages {start_page} to {end_page}")
        cat_pdf(args.filename, start_page, end_page, output_fname)
