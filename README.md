# new world navigator

# Settings del juego
* resolución 1920x1080, contraste y brillo por defecto
* activa la visualización de los FPS para que se muestren las coordenadas del personaje

# Instalacion
* Descomprime la carpeta /tesseract/x64.zip para que quede como /tesseract/x64/*

# Guia de uso
* Indica las posiciones correctas para la detección de la brujula del juego
* Indica las posiciones correctas para la detección de las coordenadas (en la esquina superior derecha cuandoa activas los FPS)
* Escoge los recursos que deseas perseguir
* Pulsa Iniciar Navegación

# Personalización
* Cierra la aplicación y edita el fichero config.xml para editar los parametros siguientes:
  * __loop.sec__: segundos que tarda en volverse a analizar la pantalla para obtener información de la ubicación del juego. Cuanto más bajo sea, más recursos consumirá pero más reactivo será a nuestra ubicación real.
  * __compass__: brujula del jugador en la zona superior en el centro del area de juego. Parametros: ancho (w), alto (h) del area de lectura, y su posición en la pantalla del juego (x, y)
  * __location__: localización en la esquina superior derecha cuando se activan los FPS en el area de juego. Parametros: ancho (w), alto (h) del area de lectura, y su posición en la pantalla del juego (x, y)
  * __log_lvl__: puede tomar valores INFO o DEBUG para mostrar un mayor numero de trazas

# Compilación del código fuente
* Instala python 3.8 https://www.python.org/downloads/
* Crea el entorno virtual de python ```python3 -m venv instalation_directory\nw-navigator```
* Activa el entorno virtual ```Scripts\activate```
* Instala los módulos: ```pip install -r requirements.txt```
* Ejecuta ```python navigator.py``` 
* Aparecerá la interfaz

## Para crear un .exe distrubuible
1. Instala: ```pip install pyinstaller```
2. Ejecuta el comando: ```pyinstaller --add-data resources;resources navigator.py```
3. Se generará un exe en la ruta ```dist\navigator\navigator.exe ```

# Troubleshooting

### Error importando win32api

Si te sale este error: __"ImportError: DLL load failed" while importing win32api__
> conda install pywin32
> pip install --upgrade pywin32==225

[StackOverflow](https://stackoverflow.com/questions/58612306/how-to-fix-importerror-dll-load-failed-while-importing-win32api)


### Seleccionar interprete en VSCode

En VSCode, pulsa CTRL+SHIFT+P > Python select iterpreter y escoge el de nw-navigator/Scripts/python.exe

### Importar Yaml en VSCode

Si en VSCode no encuenta el paquete yaml, despues de seleccionar el iterprete como se indica en el punto anterior, ejecuta su terminal:
> pip install pyyaml

### Importar Pytesseract

En el entorno hay que instalar pytesseract, por ejemplo:

> conda install -c conda-forge tesseract

