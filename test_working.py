from fpdf import FPDF

class Shirtificate(FPDF):
    def __init__(self, name):
        super().__init__(orientation="Portrait", unit="mm", format="A4")
        self.name = name
        self.add_page()
        self._add_title()
        self._add_name()
        self._add_shirt()

    def _add_title(self):
        self.set_font("Helvetica", "B", 46)

        self.cell(0, 50, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    def _add_shirt(self):
        self.image("shirtificate.png", x=10, y=70, w=190)

    def _add_name(self):
        self.set_text_color(255, 255,255)
        self.set_font("Helvetica", "B", 28)
        self.set_y(140)

        self.cell(0,10, f"{self.name} took CS50", align="C")
    def save_pdf(self, filename="shirtificate.pdf"):
        self.output(filename)

def main():
    name = input("Name: ")

    pdf = Shirtificate(name)
    pdf.save_pdf("shirtificate.pdf")


if __name__ == "__main__":
    main()
