import os
import random
import PyPDF2

def get_random_pdf_text():
    pdf_dir = "./pdfs/"
    files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
    if not files:
        raise FileNotFoundError("Nessun file PDF trovato.")
    
    random_file = os.path.join(pdf_dir, random.choice(files))
    
    with open(random_file, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        num_pages = len(reader.pages)
        
        # Seleziona una pagina casuale
        random_page = random.randint(0, num_pages - 1)
        
        # Estrai il testo della pagina casuale
        text = reader.pages[random_page].extract_text()
    
    return text