import PyPDF2

# Open the PDF file in read-binary mode
pdf_file = open(r"D:\recorded_videos\WA-Provider-Directory-Clallam-Jefferson-Kitsap.pdf", 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Define the range of pages to extract (inclusive, 0-based index)
start_page = 242  # Page 243 (0-based index)
end_page = 305    # Page 306 (0-based index)

# Ensure that the specified page range is valid
if 0 <= start_page <= end_page < pdf_reader.numPages:
    # Initialize an empty string to store the extracted text
    extracted_text = ""

    # Loop through the specified page range and extract text
    for page_number in range(start_page, end_page + 1):
        page = pdf_reader.getPage(page_number)
        extracted_text += page.extractText()

    # Print the extracted text
    print(extracted_text)
else:
    print("Invalid page range specified.")