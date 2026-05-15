import os
import pdfplumber
from datetime import datetime

print("=== Extractor Resumido para Celular ===\n")

def extraer_resumen_pdf(ruta_pdf):
    print(f"Procesando: {ruta_pdf}")
    texto_resumen = ""
    
    with pdfplumber.open(ruta_pdf) as pdf:
        for i, pagina in enumerate(pdf.pages[:10]):  # Solo primeras 10 páginas (las más importantes)
            texto = pagina.extract_text()
            if texto:
                texto_resumen += texto + "\n\n"
    
    # Guardar resumen corto
    nombre = os.path.basename(ruta_pdf).replace(".pdf", "")
    with open(f"data/{nombre}_RESUMEN.md", "w", encoding="utf-8") as f:
        f.write(f"# Resumen {nombre}\n\n")
        f.write(texto_resumen[:15000])  # Limitamos para que sea más fácil copiar
    
    print(f"✅ Resumen guardado en: data/{nombre}_RESUMEN.md")
    print("   (Primeras 10 páginas - suficiente para tesis)")


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    
    # Procesa todos los PDFs
    for root, dirs, files in os.walk("pdfs"):
        for file in files:
            if file.endswith(".pdf"):
                ruta = os.path.join(root, file)
                extraer_resumen_pdf(ruta)
    
    print("\n🎯 Listo. Ahora abre los archivos _RESUMEN.md y copia el contenido.")