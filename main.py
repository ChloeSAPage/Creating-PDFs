from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", )

df = pd.read_csv("topics.csv")

for index, rows in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    
    pdf.cell(w=0, h=12, txt=rows["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)


pdf.output("name.pdf")
