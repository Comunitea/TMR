# Odoo Pricing Module

Este módulo de Odoo está diseñado para calcular y gestionar los precios de los productos según diferentes tarifas. Permite registrar modificaciones en los precios y almacenar la fecha de dichas modificaciones.

## Estructura del Proyecto

El módulo contiene los siguientes archivos y directorios:



- **models/**: Contiene los modelos de datos del módulo.
  - `__init__.py`: Inicializa el módulo de modelos.
  - `product_pricing.py`: Define el modelo de datos para el cálculo de precios de productos.

- **views/**: Contiene las vistas del módulo.
  - `product_pricing_views.xml`: Define las vistas para mostrar los precios de los productos y sus tarifas.

- `__init__.py`: Inicializa el módulo principal.

- `__manifest__.py`: Contiene la configuración del módulo.

## Instalación

1. Clona este repositorio en tu entorno de Odoo.
2. Asegúrate de que el módulo esté en la carpeta de addons de Odoo.
3. Actualiza la lista de módulos en Odoo.
4. Busca "Odoo Pricing Module" en la lista de módulos y haz clic en "Instalar".

## Uso

Una vez instalado, el módulo te permitirá:

- Calcular precios de productos según tarifas definidas.
- Registrar cualquier modificación en los precios junto con la fecha de modificación.
- Visualizar los precios y sus tarifas a través de las vistas proporcionadas.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este módulo, por favor abre un issue o un pull request en este repositorio.

## Licencia

Este proyecto está bajo la Licencia MIT.
