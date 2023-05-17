# Colorama, ASCII Art and Virtual Env

Practica de python para repasar la creación de un virtual environment y el uso de las librerías ASCII Art y Colorama

## Pasos realizados en la practica

1. Crear un repositorio en GITHUB y añadir la plantilla de `.gitignore Python`

2. Clonar el repositorio 
```bash
git clone https://github.com/VanessaRubiera/Colorama.git
```

3. Crear el entorno virtual
```bash
python -m venv env
```

4. Activar el entorno virtual en windows(en terminal de bash)
```bash
source env/Scripts/activate
```

5. Instalar las dependencias para el proyecto. 
```bash
pip install ipython
pip install colorama
pip install art
```

6. Revisar las dependencias del proyecto
```bash
pip freeze
```

7. Guardar las dependencias del proyecto
```bash
pip freeze > requerimientos.txt
```

8. Ver status del archivos y añadir al stagging area todos los archivos modificados
```bash
git status
git add . 
```
9. 