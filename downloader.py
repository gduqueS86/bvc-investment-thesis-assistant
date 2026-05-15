import os
import yaml
import requests
from datetime import datetime

print("=== BVC Investment Thesis Assistant - Downloader Automático ===\n")
print(f"Inicio: {datetime.now()}\n")

# Crear estructura de carpetas
os.makedirs("pdfs", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Cargar configuración
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def descargar_pdf(url, empresa, nombre_archivo):
    """Descarga un PDF y lo guarda organizado"""
    carpeta = os.path.join("pdfs", empresa.upper())
    os.makedirs(carpeta, exist_ok=True)
    
    filepath = os.path.join(carpeta, nombre_archivo)
    
    print(f"Descargando → {empresa} / {nombre_archivo}")
    try:
        r = requests.get(url, headers=headers, timeout=60)
        if r.status_code == 200 and len(r.content) > 100000:  # archivo decente
            with open(filepath, 'wb') as f:
                f.write(r.content)
            print(f"✅ ¡ÉXITO! ({len(r.content)/1024/1024:.1f} MB)")
            return True
        else:
            print(f"❌ Error o archivo pequeño ({r.status_code})")
            return False
    except Exception as e:
        print(f"❌ Error descargando: {e}")
        return False


if __name__ == "__main__":
    print("Iniciando descargas automáticas...\n")
    
    # ==================== DESCARGAS DIRECTAS ====================
    
    # Ecopetrol (fácil de descargar)
    descargar_pdf(
        "https://files.ecopetrol.com.co/web/esp/inversionista/reporte-1t-2026.pdf",
        "ECOPETROL",
        "Informe_Trimestral_1T2026.pdf"
    )
    
    # Bancolombia (puedes agregar más enlaces)
    # descargar_pdf("URL_AQUI", "BANCOLOMBIA", "Informe_Trimestral.pdf")
    
    print("\n" + "="*60)
    print("Descargas completadas.")
    print("Revisa la carpeta 'pdfs' en tu repositorio.")
    print("Próximo paso: Agregar más empresas y enlaces automáticos.")