from fpdf import FPDF

def remove_non_ascii(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = ''.join(filter(lambda x: ord(x) < 128, lines[i]))
    return lines

def convert_to_pdf(input_file, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    lines = remove_non_ascii(input_file)
    for line in lines:
        pdf.cell(200, 10, txt=line, ln=1)
    pdf.output(output_file)

# Example usage:

