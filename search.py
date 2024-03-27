import os
import fitz  # PyMuPDF

def find_keywords_in_pdf(pdf_path, keywords):
    """
    Search for the keywords in the specified PDF and return paragraphs containing them.
    """
    paragraphs = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text = page.get_text("text")
            for paragraph in text.split('\n\n'):
                if any(keyword.lower() in paragraph.lower() for keyword in keywords):
                    paragraphs.append(paragraph)
    return paragraphs

def process_pdfs_in_directory(directory, keywords, output_file):
    """
    Process all PDFs in the given directory to find the keywords and output paragraphs to a text file.
    """
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for filename in os.listdir(directory):
            if filename.lower().endswith('.pdf'):
                pdf_path = os.path.join(directory, filename)
                paragraphs = find_keywords_in_pdf(pdf_path, keywords)
                if paragraphs:
                    for paragraph in paragraphs:
                        out_file.write(f"File: {filename}\n{paragraph}\n\n")

if __name__ == "__main__":
    directory = "PDF"  # Change this to the path of your PDF directory
    keywords = ["anti-lgr5", "lgr5 primary antibody"]  # Replace with your list of keywords
    output_file = "output.txt"  # The output file path
    
    process_pdfs_in_directory(directory, keywords, output_file)
    print("Processing complete. Check the output.txt file.")
