# Organiza arquivos por extensão em subpastas (Downloads, por ex.)
# CUIDADO: Faz move real dos arquivos.

from pathlib import Path
import shutil

PASTA_ALVO = Path.home() / "Downloads"  # altere se quiser
MAPA = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "PDFs": [".pdf"],
    "Docs": [".doc", ".docx", ".odt", ".rtf", ".txt", ".md", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
    "Áudio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Vídeos": [".mp4", ".mkv", ".avi", ".mov"],
    "Zips": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executáveis": [".exe", ".msi", ".apk"],
    "Código": [".py", ".js", ".ts", ".java", ".c", ".cpp", ".html", ".css"]
}

def categoria(ext):
    for nome, exts in MAPA.items():
        if ext.lower() in exts: return nome
    return "Outros"

cont = 0
for item in PASTA_ALVO.iterdir():
    if item.is_file():
        destino = PASTA_ALVO / categoria(item.suffix)
        destino.mkdir(exist_ok=True)
        try:
            shutil.move(str(item), destino / item.name)
            cont += 1
        except shutil.Error:
            pass
print(f"Movidos {cont} arquivo(s).")
