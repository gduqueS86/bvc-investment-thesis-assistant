import os
import pdfplumber
import pandas as pd
from datetime import datetime

print("=== BVC Investment Thesis Assistant - Extractor de PDFs ===\n")
print(f"Inicio: {datetime.now()}\n")

def extraer_pdf(ruta_pdf):
    print(f"Procesando: {ruta_pdf}")
    texto_completo = ""
    tablas = []
    
    with pdfplumber.open(ruta_pdf) as pdf:
        for i, pagina in enumerate(pdf.pages):
            # Extraer texto completo (incluye notas)
            texto = pagina.extract_text()
            if texto:
                texto_completo += f"\n--- Página {i+1} ---\n{texto}\n"
            
            # Extraer tablas
            tablas_pagina = pagina.extract_tables()
            for tabla in tablas_pagina:
                if tabla and len(tabla) > 1:
                    df = pd.DataFrame(tabla[1:], columns=tabla[0])
                    tablas.append({
                        "pagina": i+1,
                        "tabla": df
                    })
    
    return texto_completo, tablas


def procesar_todos_pdfs():
    carpeta_pdfs = "pdfs"
    if not os.path.exists(carpeta_pdfs):
        print("No existe carpeta pdfs/")
        return
    
    for empresa in os.listdir(carpeta_pdfs):
        ruta_empresa = os.path.join(carpeta_pdfs, empresa)
        if os.path.isdir(ruta_empresa):
            print(f"\n📁 Empresa: {empresa}")
            
            for archivo in os.listdir(ruta_empresa):
                if archivo.endswith(".pdf"):
                    ruta_pdf = os.path.join(ruta_empresa, archivo)
                    texto, tablas = extraer_pdf(ruta_pdf)
                    
                    # Guardar texto completo
                    nombre_base = archivo.replace(".pdf", "")
                    with open(f"data/{nombre_base}_texto_completo.md", "w", encoding="utf-8") as f:
                        f.write(f"# {archivo}\n\n")
                        f.write(texto)
                    
                    print(f"   ✅ Extraído: {archivo}")
                    print(f"   Tablas encontradas: {len(tablas)}")
                    print(f"   Texto guardado en: data/{nombre_base}_texto_completo.md\n")


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    procesar_todos_pdfs()
    print("🎯 Extracción terminada. Revisa la carpeta 'data/'")