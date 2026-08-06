# Plan De Desarrollo - SICCO

## Objetivo General

Desarrollar un prototipo estudiantil que ayude a registrar cajas mediante marcadores ArUco, calcular un acomodo recomendado dentro de una maqueta de contenedor y mostrar visualmente como volver a acomodar la mercancia.

El proyecto se enfoca primero en una maqueta educativa con cajas de medicina y contenedores a escala. La idea es que el sistema pueda escalar conceptualmente a un caso real en zona de previos del puerto.

## Contexto Del Problema

En la zona de previos, la mercancia se retira del contenedor para verificar que coincida con su documentacion. Al intentar volver a colocarla, muchas veces ya no queda acomodada igual y pueden sobrar cajas fuera del contenedor.

SICCO busca apoyar ese proceso mediante vision artificial, registro de cajas y optimizacion de volumen.

## Alcance Inicial Del Prototipo

- Usar marcadores ArUco pegados en cada caja.
- Asociar cada ArUco con dimensiones registradas en `datos/cajas.json`.
- Detectar cajas mediante webcam.
- Agregar cajas detectadas a una lista de carga.
- Calcular un acomodo dentro de un contenedor `20FT` o `40FT`.
- Mostrar el acomodo en una interfaz grafica por capas.
- Permitir que el acomodo se replique en la maqueta fisica.

## Fase 1 - Preparacion Del Proyecto

Objetivo: dejar el proyecto listo para que cualquier integrante pueda instalarlo y ejecutarlo desde cero.

Estado de checklist:

- `[ ]` Pendiente.
- `[x]` Completado.

Tareas:

- [x] Crear `.gitignore` para evitar subir el entorno virtual y archivos temporales.
- [x] Crear `README.md` con guia de instalacion en Linux y Windows.
- [x] Crear `requirements.txt` con dependencias de Python.
- [x] Verificar ejecucion de `python main.py`.
- [ ] Verificar prueba del optimizador con `python prueba_optimizador.py`.

Resultado esperado:

- El proyecto puede instalarse desde cero.
- El entorno virtual no se sube a GitHub.
- Las dependencias quedan claras.
- Cualquier integrante puede levantar el proyecto siguiendo el README.

Estado actual:

- `.gitignore` creado.
- `README.md` creado.
- `requirements.txt` creado.

## Fase 2 - Definicion De La Maqueta

Objetivo: establecer medidas reales de trabajo para el prototipo fisico.

Tareas:

- [ ] Confirmar medidas del contenedor de 40 pies a escala: `60 x 12 x 13`.
- [ ] Confirmar medidas del contenedor de 20 pies a escala: `30 x 12 x 13`.
- [ ] Medir las cajas fisicas de medicamento.
- [ ] Asignar un ArUco unico a cada caja.
- [ ] Registrar todas las cajas en `datos/cajas.json`.
- [ ] Revisar que las dimensiones del codigo coincidan con la maqueta real.

Resultado esperado:

- Cada caja fisica tiene un ArUco.
- Cada ArUco tiene dimensiones registradas.
- El programa puede identificar todas las cajas de la maqueta.

## Fase 3 - Catalogo De Cajas Y ArUco

Objetivo: tener una relacion clara entre marcador, caja y dimensiones.

Tareas:

- [ ] Revisar los ArUco disponibles en la carpeta `arucos/`.
- [ ] Decidir cuantos ArUco se usaran en la demostracion.
- [ ] Completar `datos/cajas.json` con todas las cajas reales.
- [ ] Agregar nombre o descripcion de cada caja si se requiere.
- [ ] Validar que no existan IDs ArUco repetidos.
- [ ] Mostrar aviso cuando se detecte un ArUco que no existe en el catalogo.

Resultado esperado:

- El catalogo representa fielmente las cajas de la maqueta.
- La deteccion por camara puede convertirse en una caja con dimensiones utiles para el optimizador.

## Fase 4 - Mejora Del Registro De Cajas

Objetivo: hacer mas confiable la captura de cajas durante la demostracion.

Tareas:

- [ ] Revisar deteccion actual de ArUco.
- [ ] Evitar registros duplicados.
- [ ] Mostrar claramente que caja fue detectada.
- [ ] Agregar opcion para registrar una caja manualmente si falla la camara.
- [ ] Mostrar mensaje cuando un ArUco no exista en el catalogo.
- [ ] Permitir limpiar la lista de cajas registradas.

Resultado esperado:

- El usuario puede registrar cajas por camara o manualmente.
- La demostracion no depende completamente de la webcam.
- El flujo de captura es mas estable.

## Fase 5 - Integracion De Camara En La Interfaz

Objetivo: evitar que la camara se abra en una ventana separada de OpenCV y hacer que todo funcione dentro de PyQt6.

Tareas:

- [ ] Integrar la imagen de la camara dentro de la ventana principal.
- [ ] Reemplazar el ciclo `while True` por `QTimer` o `QThread`.
- [ ] Mantener activa la interfaz mientras la camara detecta cajas.
- [ ] Agregar boton para iniciar escaneo.
- [ ] Agregar boton para detener escaneo.
- [ ] Mostrar estado de la camara en la interfaz.

Resultado esperado:

- La camara se muestra dentro del programa.
- La interfaz no se bloquea.
- El proyecto se ve mas profesional para una presentacion academica.

## Fase 6 - Mejora Del Optimizador

Objetivo: mejorar el acomodo de cajas dentro del contenedor.

Tareas:

- [ ] Revisar algoritmo actual de `packing/optimizador.py`.
- [ ] Validar colisiones correctamente.
- [ ] Probar diferentes orientaciones de cajas.
- [ ] Reportar cajas colocadas.
- [ ] Reportar cajas que no cupieron.
- [ ] Calcular porcentaje de volumen utilizado.
- [ ] Mejorar acomodo por capas.
- [ ] Agregar pruebas con diferentes combinaciones de cajas.

Resultado esperado:

- El sistema genera un acomodo mas confiable.
- El usuario sabe que cajas caben y cuales no.
- El acomodo se puede explicar como optimizacion de volumen.

## Fase 7 - Visualizacion Del Contenedor

Objetivo: mostrar el acomodo de forma clara para replicarlo en la maqueta fisica.

Tareas:

- [ ] Mejorar dibujo del contenedor.
- [ ] Mostrar cajas por capas.
- [ ] Identificar cada caja con numero o ArUco.
- [ ] Mostrar dimensiones de caja seleccionada.
- [ ] Agregar resumen del acomodo.
- [ ] Usar la imagen `imgContenedorConcepto.jpeg` como referencia local del objetivo fisico.

Resultado esperado:

- El usuario puede seguir el plano para acomodar las cajas.
- El sistema funciona como guia visual tipo Tetris.
- El acomodo digital se puede comparar con la maqueta fisica.

## Fase 8 - Pruebas Con La Maqueta

Objetivo: validar el programa con cajas reales.

Tareas:

- [ ] Probar con pocas cajas.
- [ ] Probar con muchas cajas.
- [ ] Probar con contenedor `40FT`.
- [ ] Probar con contenedor `20FT`.
- [ ] Verificar deteccion de ArUco con diferentes luces.
- [ ] Ajustar medidas si alguna caja no coincide con la maqueta.
- [ ] Documentar fallos encontrados durante pruebas.

Resultado esperado:

- El prototipo puede demostrarse en clase.
- El acomodo calculado puede replicarse fisicamente.
- Se identifican limitaciones reales del prototipo.

## Fase 9 - Presentacion Final

Objetivo: preparar el proyecto para exposicion academica.

Tareas:

- [ ] Preparar explicacion del problema real en zona de previos.
- [ ] Explicar uso de ArUco.
- [ ] Explicar relacion con optimizacion de volumenes.
- [ ] Mostrar flujo completo del programa.
- [ ] Mostrar maqueta funcionando.
- [ ] Documentar limitaciones.
- [ ] Proponer mejoras futuras.

Resultado esperado:

- El proyecto queda listo para presentarse como prototipo academico.
- Se puede explicar tanto la parte tecnica como la parte matematica.

## Prioridad Inicial

Primer bloque de trabajo recomendado:

- [x] Crear `requirements.txt`.
- [ ] Completar `datos/cajas.json` con todas las cajas reales de la maqueta.
- [ ] Mejorar el flujo de camara e interfaz.
- [ ] Agregar registro manual de cajas.
- [ ] Mejorar reporte del optimizador.

## Decisiones Tecnicas Iniciales

- No medir dimensiones reales con la camara en la primera version.
- Usar ArUco como identificador de caja.
- Guardar dimensiones de cajas en `datos/cajas.json`.
- Mantener las medidas del contenedor en unidades de maqueta.
- Priorizar estabilidad para la demostracion antes que complejidad matematica avanzada.

## Comandos Base Del Proyecto

Crear entorno virtual en Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Crear entorno virtual en Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Ejecutar proyecto principal:

```bash
python main.py
```

Probar optimizador sin camara:

```bash
python prueba_optimizador.py
```
