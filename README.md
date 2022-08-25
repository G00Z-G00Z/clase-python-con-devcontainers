# Usar python con dev containers

Se puede usar docker para poder usar python, lo cual hace que los proyectos
sean muy fáciles de instalar. Sin embargo, esto puede necesitar conocimiento
tecnico para poder realizarse. Por lo que para usuarios nuevos puede ser un
poco intimidante. 

La extensión de **devcontainer** soluciona el problema de no conocer Docker
(aunque recomiendo mucho que lo aprendan). Los devcontainers usan docker en el
background, para levantar un ecosistema de python. **Vscode** maneja el docker
sin necesidad de que el usuario tenga conocimiento de python. 

Todo esto sigue la [documentacion oficial de los remote
containers](https://code.visualstudio.com/docs/remote/containers) 

# Requerimientos

Para poder usar los dev containers necesitaras: 

- [Docker](https://www.docker.com/) instalado en tu computadora (puede ser Docker desktop también).
- Vscode instalado en tu computadora.
- Extension de [Remote containers](vs_code_extension_url) en vscode.

# Instrucciones para instalacion

## Desde el repositorio

Puedes clonar el repositorio y puedes abrir un devcontainer en vscode. Sin
embargo, necesitas cumplir los requerimientos para poder usarlo.

## Desde 0

1. Abrir una carpeta donde se quiere instalar el contenedor.
2. Abrir la paleta de comandos, y elegir **Remote containers: Open in container**.
3. Elegir las opciones que necesitas para el contenedor (Python 3.10).
4. Instalar esto generara una carpeta .devcontainers/ con la informacion del contenedor.
5. Abrir el devcontainer en vscode.

## Instalar librerias

Para instalar librerias tienes que seguir los siguientes pasos.

1. Escribir un archivo en la raiz que se llame `requirement.txt`.
2. Poner todas las librerias que necesites. Una libreria por linea.

**Ejemplo**

```text
numpy
matplotlib
pillow
```

3. Descomentar la linea en el devcontainer/Dockerfile que habla sobre las instalaciones de pip.

```Dockerfile
# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp
```

4. Reconstruir el contenedor. 

## Limitaciones

- No se pueden mostrar los plots de matlplotlib en pop ups. Para eso puedes
- Hacer un `plt.savefigure('figura')` para salvarlo en tus archivos. De ahi puedes ver la figura.

[vs_code_extension_url]: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
