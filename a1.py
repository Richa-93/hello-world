'''Set your OpenAI API key
openai.api_key = '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'''


        
'''import os
import openai
from PIL import Image
import pytesseract

# Set up your OpenAI API key
openai.api_key = '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'
 # Replace with your actual API key

def perform_ocr(image_path):
    try:
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img)
        print(f"OCR Output for {image_path}:\n{text}\n")
        return text
    except Exception as e:
        print(f"Error performing OCR on {image_path}: {e}")
        return None



# Function to use OpenAI API to analyze text
def analyze_text_with_openai(text):
    prompt = f"Analyze the details from the invoice:\n{text}"
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use an appropriate engine
        prompt=prompt,
        max_tokens=150  # Adjust based on your requirements
    )
    return response.choices[0].text.strip()

# Path to the folder containing invoice images
invoices_folder = 'D:/richa/Invoices Found'

# Output file path
output_file_path = 'D:/richa/image.txt'

# Open a file for writing
with open(output_file_path, 'w') as output_file:
    # Read details from each invoice image in the folder
    for filename in os.listdir(invoices_folder):
        if filename.endswith('.jpg'):  # Assuming invoices are jpg images
            image_path = os.path.join(invoices_folder, filename)

            # Perform OCR on the image
            invoice_details = perform_ocr(image_path)

            if invoice_details:
                # Use OpenAI API to analyze the invoice details
                analysis_result = analyze_text_with_openai(invoice_details)
                # Before making the API call
                print(f"Analyzing text with OpenAI for {filename}")

                # After making the API call
                print(f"OpenAI API Response: {response}")


                # Display and write results
                print(f"Invoice: {filename}")
                print(f"Details:\n{invoice_details}")
                print(f"Analysis Result:\n{analysis_result}")
                print("\n" + "=" * 50 + "\n")

                # Write details to the output file
                output_file.write(f"Invoice: {filename}\n")                            
                output_file.write(f"Details:\n{invoice_details}\n")
                output_file.write(f"Analysis Result:\n{analysis_result}\n")
                output_file.write("\n" + "=" * 50 + "\n")

print(f"Results saved to {output_file_path}")'''


import os
import openai
from PIL import Image
import pytesseract
import re

# Set up your OpenAI API key
openai.api_key = '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'  # Replace with your actual API key

# Function to perform OCR on an image file
def perform_ocr(image_path):
    try:
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error performing OCR on {image_path}: {e}")
        return None

# Function to use OpenAI API to analyze text
def analyze_text_with_openai(text):
    prompt = f"Analyze the details from the invoice:\n{text}"
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use an appropriate engine
        prompt=prompt,
        max_tokens=150  # Adjust based on your requirements
    )
    return response.choices[0].text.strip()

# Function to extract invoice details using regular expressions
def extract_invoice_details(text):
    # Example regular expressions, adjust as needed
    invoice_number_pattern = re.compile(r'Invoice Number: (\w+)', re.IGNORECASE)
    invoice_date_pattern = re.compile(r'Invoice Date: (\d{2}/\d{2}/\d{4})', re.IGNORECASE)
    invoice_amount_pattern = re.compile(r'Invoice Amount: (\$\d+\.\d{2})', re.IGNORECASE)

    # Extract details using regular expressions
    invoice_number_match = invoice_number_pattern.search(text)
    invoice_date_match = invoice_date_pattern.search(text)
    invoice_amount_match = invoice_amount_pattern.search(text)

    invoice_number = invoice_number_match.group(1) if invoice_number_match else "Not Found"
    invoice_date = invoice_date_match.group(1) if invoice_date_match else "Not Found"
    invoice_amount = invoice_amount_match.group(1) if invoice_amount_match else "Not Found"

    return invoice_number, invoice_date, invoice_amount

# Path to the folder containing invoice images
invoices_folder = 'D:/richa/Invoices Found'

# Output file path
output_file_path = 'D:/richa/image.txt'

# Open a file for writing
with open(output_file_path, 'w') as output_file:
    # Read details from each invoice image in the folder
    for filename in os.listdir(invoices_folder):
        if filename.endswith('.jpg'):  # Assuming invoices are jpg images
            image_path = os.path.join(invoices_folder, filename)

            # Perform OCR on the image
            invoice_details_text = perform_ocr(image_path)

            if invoice_details_text:
                # Extract specific details using regular expressions
                invoice_number, invoice_date, invoice_amount = extract_invoice_details(invoice_details_text)

                # Use OpenAI API to analyze the invoice details
                analysis_result = analyze_text_with_openai(invoice_details_text)

                # Display and write results
                print(f"Invoice: {filename}")
                print(f"Invoice Number: {invoice_number}")
                print(f"Invoice Date: {invoice_date}")
                print(f"Invoice Amount: {invoice_amount}")
                print(f"Analysis Result:\n{analysis_result}")
                print("\n" + "=" * 50 + "\n")

                # Write details to the output file
                output_file.write(f"Invoice: {filename}\n")
                output_file.write(f"Invoice Number: {invoice_number}\n")
                output_file.write(f"Invoice Date: {invoice_date}\n")
                output_file.write(f"Invoice Amount: {invoice_amount}\n")
                output_file.write(f"Analysis Result:\n{analysis_result}\n")
                output_file.write("\n" + "=" * 50 + "\n")

print(f"Results saved to {output_file_path}")

