from pdf2image import convert_from_path
import os

poppler_path = r'C:\Users\aluno\Downloads\Release-25.07.0-0\poppler-25.07.0\Library\bin'
pdf_path = "enem2024.pdf"
output_folder = "imagens"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
resolucao_dpi = 300

print("Convertendo '{pdf_path}' para imagens com {resolucao_dpi} DPI...")

try:
    images = convert_from_path(
        pdf_path,
        dpi=resolucao_dpi,
        output_folder=output_folder,
        fmt="png",
        paths_only=False,
        poppler_path=poppler_path
    )
    
    for i, image in enumerate(images):
        image_filename = os.path.join(output_folder, f"pagina_enem_{i+1}.png")
        image.save(image_filename)
        print(f"Página {i+1} salva como '{image_filename}'")
        
    print(f"\nConversão concluída! As images foram salvas na pasta '{output_folder}'.")
    
except Exception as e:
    print(f"Ocorreu um erro durante a converção: {e}")
    print("Verifique se o Poppler está instalado corretamente e se o caminho do PDF está correto.")