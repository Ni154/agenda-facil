from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from datetime import datetime

def gerar_recibo_pdf(path: str, dados: dict) -> None:
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4
    margin = 15 * mm
    y = height - margin
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y, "RECIBO")
    y -= 12*mm

    c.setFont("Helvetica", 11)
    lines = [
        f"Recebedor: {dados.get('empresa_nome','')}",
        f"CNPJ: {dados.get('empresa_cnpj','')}",
        f"Cliente: {dados.get('cliente_nome','')}",
        f"Descrição: {dados.get('descricao','')}",
        f"Valor: R$ {dados.get('valor','0,00')}",
        f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
    ]
    for line in lines:
        c.drawString(margin, y, line)
        y -= 8*mm
    c.showPage()
    c.save()
