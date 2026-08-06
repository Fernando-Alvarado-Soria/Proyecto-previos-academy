# SICCO - Sistema Inteligente de Cubicacion de Contenedores

Proyecto en Python para detectar cajas mediante marcadores ArUco usando webcam, registrar sus dimensiones y calcular una distribucion dentro de un contenedor. La interfaz grafica esta hecha con PyQt6 y la deteccion de camara con OpenCV.

## Requisitos

- Python 3.10 o superior
- Webcam disponible
- Git, si vas a clonar el repositorio
- En Linux, librerias graficas necesarias para PyQt6

## Dependencias De Python

El proyecto usa principalmente:

```text
PyQt6
opencv-contrib-python
```

Importante: se usa `opencv-contrib-python` porque el proyecto necesita el modulo `cv2.aruco`.

## Instalacion En Linux

1. Entrar a la carpeta del proyecto:

```bash
cd "/ruta/del/proyecto/Proyecto-previos-academy"
```

2. Crear el entorno virtual:

```bash
python3 -m venv .venv
```

3. Activar el entorno virtual:

```bash
source .venv/bin/activate
```

4. Actualizar `pip`:

```bash
python -m pip install --upgrade pip
```

5. Instalar dependencias:

```bash
python -m pip install PyQt6 opencv-contrib-python
```

6. Si PyQt6 muestra errores relacionados con `xcb`, instalar dependencias del sistema:

```bash
sudo apt update
sudo apt install libxcb-cursor0 libxkbcommon-x11-0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xinerama0
```

7. Ejecutar el proyecto:

```bash
python main.py
```

## Instalacion En Windows

1. Entrar a la carpeta del proyecto desde PowerShell o CMD:

```powershell
cd "C:\ruta\del\proyecto\Proyecto-previos-academy"
```

2. Crear el entorno virtual:

```powershell
python -m venv .venv
```

3. Activar el entorno virtual en PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Si usas CMD:

```cmd
.venv\Scripts\activate.bat
```

4. Si PowerShell bloquea la activacion del entorno virtual, ejecutar:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Luego volver a activar:

```powershell
.venv\Scripts\Activate.ps1
```

5. Actualizar `pip`:

```powershell
python -m pip install --upgrade pip
```

6. Instalar dependencias:

```powershell
python -m pip install PyQt6 opencv-contrib-python
```

7. Ejecutar el proyecto:

```powershell
python main.py
```

## Uso Del Programa

- Al ejecutar `python main.py`, se abre la interfaz grafica y la camara.
- El sistema busca marcadores ArUco con OpenCV.
- Si el marcador existe en `datos/cajas.json`, se registra una caja con sus dimensiones.
- El boton `OPTIMIZAR` calcula la ubicacion de las cajas dentro del contenedor.
- El boton `LIMPIAR` borra la lista actual.
- Para salir de la ventana de camara de OpenCV, presionar `Esc`.

## Probar El Optimizador Sin Camara

Si solo quieres probar el algoritmo de acomodacion sin abrir la interfaz principal ni usar webcam:

```bash
python prueba_optimizador.py
```

En Windows el comando es el mismo:

```powershell
python prueba_optimizador.py
```

## Generar Marcadores ArUco

El proyecto incluye un script para generar imagenes ArUco:

```bash
python herramientas/generar_arucos.py
```

Los archivos se generan en la carpeta `arucos/`.

Actualmente `datos/cajas.json` tiene configurados los marcadores ArUco `10`, `11`, `12` y `13`. Si se generan o escanean otros IDs, tambien deben agregarse al archivo `datos/cajas.json` para que el sistema conozca sus dimensiones.

## Estructura Del Proyecto

```text
Proyecto-previos-academy/
├── main.py
├── prueba_optimizador.py
├── arucos/
├── core/
├── datos/
│   └── cajas.json
├── herramientas/
│   └── generar_arucos.py
├── modelos/
│   ├── caja.py
│   ├── catalogo.py
│   ├── contenedor.py
│   └── posicion.py
├── packing/
│   ├── optimizador.py
│   └── posicion.py
├── ui/
│   ├── main_window.py
│   ├── plano_contenedor.py
│   └── controles_capas.py
└── vision/
    ├── camera.py
    └── detector_aruco.py
```

## Problemas Comunes

### Error: Could not load the Qt platform plugin "xcb"

En Linux, instalar:

```bash
sudo apt update
sudo apt install libxcb-cursor0 libxkbcommon-x11-0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xinerama0
```

### Error: No se pudo abrir la camara

Revisar que:

- La webcam este conectada.
- Otra aplicacion no este usando la camara.
- El sistema tenga permisos para acceder a la camara.

### Error: module 'cv2.aruco' not found

Instalar OpenCV contrib:

```bash
python -m pip uninstall opencv-python
python -m pip install opencv-contrib-python
```

## Desactivar El Entorno Virtual

Cuando termines de trabajar:

```bash
deactivate
```
