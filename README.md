# Honey_Bun

Honey_Bun es una base para proyectos web en Django 5, preparada para desarrollo y despliegue con Docker, PostgreSQL y Nginx. Incluye integración con [django-components](https://github.com/EmilStenstrom/django-components) para desarrollo modular de componentes frontend.

## Estructura del Proyecto
```
├── src/
│   ├── ecommerce/           # Proyecto principal Django
│   ├── static/              # Archivos estáticos globales
│   └── templates/           # Plantillas globales
├── nginx/
│   ├── default.conf/        # Configuración de Nginx
├── .env                     # Variables de entorno
├── docker-compose.yml       # Orquestación de servicios Docker
├── requirements.txt         # Dependencias de Python
└── README.md                # Documentación del proyecto
```

## Características Principales

- **Django 5**: Framework robusto para desarrollo web.
- **Docker**: Contenedores para desarrollo y producción.
- **PostgreSQL**: Base de datos relacional avanzada.
- **Nginx**: Servidor web para servir estáticos y proxy reverso.
- **django-components**: Desarrollo frontend modular y reutilizable.

## Instalación Rápida

1. Clona el repositorio:
    ```bash
    git clone https://github.com/Helien-Dev/Honey_Bun.git
    cd Honey_Bun
    ```

2. Copia el archivo `.env.example` a `.env` y ajusta las variables necesarias.

3. Levanta los servicios con Docker:
    ```bash
    docker-compose up --build
    ```

4. Accede a la aplicación en `http://localhost:8000`.

## Uso de django-components

Agrega componentes reutilizables en `src/widgets` y úsalos en tus plantillas con `{% component 'nombre' %}`.

## Scripts Útiles

- Migraciones:
  ```bash
  docker-compose exec backend python manage.py migrate
  ```
- Crear superusuario:
  ```bash
  docker-compose exec backend python manage.py createsuperuser
  ```
El script initializer.sh contiene estas migraciones
## Despliegue

Configura variables de entorno para producción y ajusta los archivos en `docker/nginx/` según tus necesidades.

## Contribuciones

¡Las contribuciones son bienvenidas! Abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT.