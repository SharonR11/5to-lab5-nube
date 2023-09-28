# Laboratorio 5 - 5C24B - RUDAS

En este laboratorio, se desarrollará una aplicación que mostrará un menú donde se encontrará una lista de alumnos registro, además de que se podrá registrar, modificar y eliminar, utilizando Django y postgresql. Esta aplicación se guardará en nuestro repositorio público. Luego, se creará una instancia en AWS donde se realizará la ejecución de nuestros archivos como dockerfile y Docker-compose que permitirá ejecutar la aplicación desde nuestra instancia.

## Materiales, Programas y Recursos:

- Una computadora o laptop
- Conexión a internet
- Cuenta en AWS
- Git bash
- Render

## Creación de Instancia en AWS:

1. Realizar la creación de nuestra instancia con Ubuntu 20.
2. Crear una nueva llave para poder conectarnos en cualquier momento.
3. Indicar que tenga 10GB de almacenamiento.

<img width="437" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/f8c53e45-27ca-4d9c-8d95-79d5c6f1bbd5">

<img width="434" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/9cf6baa7-8d9d-4979-a209-62a7e44e7bbc">

<img width="432" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/e028e0fa-9413-490e-bd20-0989958e8196">


## Creación de la Aplicación con Django:

1. Crear una carpeta donde estará nuestro entorno y la aplicación.
2. Instalar Django.
3. Ejecutar comandos para la creación del proyecto y su startapp.

<img width="439" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/2945e6e6-2335-4c80-844f-bd3377449f6f">

## Uso de Comandos de Django:

1. Ejecutar el comando `migrate` para obtener funciones de administrador y más, que permiten manejar los registros de manera directa.

<img width="440" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/026696f7-224a-44f9-9f75-dc9d31161a44">

2. Realizar la creación del objeto Alumno.

<img width="364" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/0193981e-cc6e-46ae-bdb5-90bf256097f8">

3. Generar funciones que permiten listar, registrar, editar y eliminar alumnos.

<img width="425" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/ffe6db1e-47b2-4442-bb9d-cb9f159d844e">

<img width="345" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/08c81652-4636-4243-add7-6a7205054ca5">

<img width="278" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/c0846495-be3b-422b-a234-13d9b32102bc">

## Creación de Base de Datos:

En Render, realizaremos la creación de nuestra base de datos con PostgreSQL.

<img width="180" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/bf28c108-65e9-42fe-920d-af96bfb33161">

## Conectar la Base de Datos con la Aplicación:

<img width="435" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/ac061fe3-3ab2-41c6-9ef0-afec659a5ed4">

## Crear un archivo `Requirements.txt` e instalar `psycopg2`.

<img width="445" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/b78b381e-4d7f-45d8-af4e-8fe3b02f15d8">

<img width="179" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/447e7791-389d-4563-9875-b876f0cc0445">

## Crear Docker-compose.

<img width="223" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/b4853329-e9cb-4af7-a185-28372b2da094">

## Crear Dockerfile.

<img width="344" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/da738e3c-2704-4e1b-9a30-55a9df8eb4d9">

## Estructura de la Aplicación:

<img width="150" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/18063008-ba53-4022-96bc-713bdad7fb31">

## Conectar la Aplicación en nuestra Instancia:

1. Iniciar nuestra instancia en el repositorio local.

<img width="428" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/9bb6ed35-9429-406e-ac79-51afac61f88d">

2. Actualizar las librerías.

<img width="436" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/61ba5d7e-f11d-4c43-8a0c-6dd50b45107c">

3. Instalar Docker.

<img width="441" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/b9bcee32-72e6-4724-b819-3c2b99728465">

4. Crear mkdir donde se almacenara nuestro proyecto.

<img width="437" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/7990b6af-f993-4540-b8be-133021296f48">

5. Clonar proyecto desde git.

<img width="439" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/363065c2-663a-41ba-9672-607002f31398">

6. Levantar los servicios definidos en el docker-compose.yml

<img width="393" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/ca377948-e40c-49ec-811d-9d574ede5596">

## Aplicación con Uso de Composer:

<img width="546" alt="image" src="https://github.com/SharonR11/5to-lab5-nube/assets/129893932/7ead434a-4d7f-42eb-87f6-2e786ad14cd0">

## Enlaces a Repositorios:

- [Repositorio Estudiantil](https://github.com/Tecsupsoft/practica01-dsn-SharonR11)
