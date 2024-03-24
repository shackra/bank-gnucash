#!/usr/bin/env sh

if [ "$#" -ne 2 ]; then
  echo "Uso: $0 <directorio_de_entrada> <directorio_de_salida>"
  exit 1
fi

# Directorio de los archivos .ui (primer argumento)
UI_DIR="$1"

# Directorio de salida para los archivos .py (segundo argumento)
OUTPUT_DIR="$2"

# Crear el directorio de salida si no existe
mkdir -p "$OUTPUT_DIR"

# Bucle a través de todos los archivos .ui en el directorio de entrada
for ui_file in "$UI_DIR"/*.ui; do
  # Obtener el nombre base del archivo sin la extensión
  base_name=$(basename "$ui_file" .ui)

  # Definir el nombre del archivo de salida .py
  py_file="$OUTPUT_DIR/$base_name.py"

  # Usar pyside2-uic para convertir el archivo .ui a .py
  pyside2-uic "$ui_file" -o "$py_file"

  echo "Convertido: $ui_file -> $py_file"
done
