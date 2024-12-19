Import("env")
import shutil
import os

# Função que copia o arquivo .bin gerado para outra pasta
def copy_bin_file(source, target, env):
    bin_file = str(target[0])  # O arquivo .bin gerado
    bin_dir = os.path.join(env["PROJECT_DIR"], "bin_files")  # Diretório de destino para o .bin

    # Cria o diretório de destino, se não existir
    os.makedirs(bin_dir, exist_ok=True)

    # Caminho final da cópia do arquivo .bin
    bin_copy_file = os.path.join(bin_dir, os.path.basename(bin_file))

    # Copia o arquivo .bin para o novo diretório
    print(f"[INFO] Copiando arquivo .bin para: {bin_copy_file}")
    shutil.copy(bin_file, bin_copy_file)

# Adiciona a ação após o build do .bin
env.AddPostAction("$BUILD_DIR/${PROGNAME}.bin", copy_bin_file)
