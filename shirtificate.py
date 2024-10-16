from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        # Set font and add title at the top of the PDF
        self.set_font("Arial", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", ln=True, align="C")  # Centered, moving to the next line

def create_shirtificate(name):
    # Initialize PDF
    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Add the shirt image
    # The image will be scaled and centered on the page
    pdf.image("shirtificate.png", x=15, y=60, w=180)

    # Add the user's name in white text on top of the shirt image
    pdf.set_text_color(255, 255, 255)  # Set text color to white
    pdf.set_font("Arial", "B", 32)
    pdf.text(x=55, y=140, txt=f"{name} took CS50!")  # Place text over the shirt

    # Save the PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    # Prompt the user for their name
    name = input("Name? ")
    create_shirtificate(name)
