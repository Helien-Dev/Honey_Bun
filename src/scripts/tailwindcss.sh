#!/bin/sh

# 🛠 Si no existe el output, compílalo una vez
if [ ! -f ./static/css/output.css ]; then
  echo "Compilando TailwindCSS por primera vez..."
  npx tailwindcss -i ./src/assets/input.css -o ./src/static/css/output.css --minify
fi

# 🌀 Ejecuta Django y Tailwind en paralelo
echo "Iniciando servidor de desarrollo y Tailwind CLI..."

# Ejecuta tailwind en segundo plano
npx tailwindcss -i ./src/assets/input.css -o ./src/static/css/output.css --watch &
TAILWIND_PID=$!

# Ejecuta Django (puedes cambiar por gunicorn si es prod)
python src/manage.py runserver 0.0.0.0:8000

# Esperar procesos (opcional)
wait $TAILWIND_PID
