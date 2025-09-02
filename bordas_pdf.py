from PIL import Image
import os

input_folder = "metades"
output_folder = "metades_cortadas"

os.makedirs(output_folder, exist_ok=True)

print(f"Processando imagens da pasta '{input_folder}'...")
print(f"Removendo 25 pixels e salvando em: '{output_folder}'")

for nome_arquivo in sorted(os.listdir(input_folder)):
    if nome_arquivo.lower().endswith(".png"):
        caminho_entrada = os.path.join(input_folder, nome_arquivo)
        imagem = Image.open(caminho_entrada)
        
        largura, altura = imagem.size
        
        if "_esquerda.png" in nome_arquivo:
            imagem_cortada = imagem.crop((0, 0, largura - 25, altura))
            output_filename = os.path.join(output_folder, nome_arquivo)
            imagem_cortada.save(output_filename)
            print(f"{nome_arquivo} -> 25px removidos da direita")
            
        elif "_direita.png" in nome_arquivo:
            imagem_cortada = imagem.crop((25, 0, largura, altura))
            output_filename = os.path.join(output_folder, nome_arquivo)
            imagem_cortada.save(output_filename)
            print(f"{nome_arquivo} -> 25px removidos da esquerda")
            
        else:
            output_filename = os.path.join(output_folder, nome_arquivo)
            imagem.save(output_filename)
            print(f"{nome_arquivo} -> copiada sem modificações")

print(f"\nProcesso concluído!")
print(f"Imagens processadas salvas em: '{output_folder}'")