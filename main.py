import pdfkit

# set path to input HTML file and output PDF file
input_file = 'pptemp.html'
output_file = 'output.pdf'

# configure options for pdfkit
options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in'
}

# convert HTML file to PDF
pdfkit.from_file(input_file, output_file, options=options)

