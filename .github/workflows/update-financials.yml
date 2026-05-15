name: Actualizar Reportes Financieros BVC

on:
  schedule:
    - cron: '0 10 5 * *'     # Corre el día 5 de cada mes a las 10:00 UTC
  workflow_dispatch:         # Permite ejecutarlo manualmente

jobs:
  update:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run downloader
        run: python downloader.py

      - name: Commit and push new files
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add pdfs/ data/ 
          git commit -m "Actualización automática de reportes financieros - $(date +'%Y-%m-%d')" || echo "No hay cambios nuevos"
          git push