import os
import yaml
import requests
import sys
from datetime import datetime

print("=== BVC Investment Thesis Assistant - Downloader Flexible ===\n")
print(f"Inicio: {datetime.now()}\n")

# Crear estructura
os.makedirs("pdfs", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Cargar configuración base
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def descargar_pdf(url, empresa, nombre_archivo):
    carpeta = os.path.join("pdfs", empresa.upper())
    os.makedirs(carpeta, exist_ok=True)
    filepath = os.path.join(carpeta, nombre_archivo)
    
    print(f"⬇️  Descargando: {empresa} → {nombre_archivo}")
    try:
        r = requests.get(url, headers=headers, timeout=60)
        if r.status_code == 200 and len(r.content) > 100000:
            with open(filepath, 'wb') as f:
                f.write(r.content)
            print(f"✅ ¡DESCARGADO! ({len(r.content)/1024/1024:.1f} MB)")
            return True
        else:
            print(f"❌ Error ({r.status_code})")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


if __name__ == "__main__":
    # === Permitir pasar empresas por comando ===
    if len(sys.argv) > 1:
        empresas = [sys.argv[1].upper()]
        print(f"Modo manual: Solo empresa {empresas[0]}")
    else:
        empresas = config.get('watchlist', ["ECOPETROL"])
        print(f"Modo config: {empresas}")

    print("\nIniciando descargas...\n")

    # ==================== EJEMPLOS DE DESCARGAS ====================
    for empresa in empresas:
        print(f"\n📌 Empresa: {empresa}")
        
        # Aquí puedes ir agregando más enlaces según la empresa
        if empresa == "ECOPETROL":
            descargar_pdf(
                "https://files.ecopetrol.com.co/web/esp/inversionista/reporte-1t-2026.pdf",
                empresa,
                "ECOPETROL_Informe_1T2026.pdf"
            )
            # Agrega más trimestres aquí
            
        elif empresa == "BANCOLOMBIA":
            print("   → Agregar enlaces de Bancolombia aquí")
            # Ejemplo futuro: descargar_pdf(url_bancolombia, empresa, nombre)
            
        else:
            print(f"   → No hay enlaces configurados aún para {empresa}")
    
    print("\n" + "="*70)
    print("✅ Descarga finalizada.")
    print("Puedes ejecutar con empresa específica usando: python downloader.py ECOPETROL")