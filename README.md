# Automatización E2E — Lovell Soccer

Pruebas automatizadas sobre [lovellsoccer.co.uk](https://www.lovellsoccer.co.uk/) con Selenium + Python.

## Qué cubre

- Ingreso a la cuenta: apertura de la web, click en login, carga de email y contraseña y confirmación, con captura de pantalla adjunta al reporte.
- Filtro de botines Nike → "Nike Mercurial Boots", selección de modelo Superfly, elección de talle 10 y agregado al carrito. Si el modelo elegido no tiene stock, el flujo prueba otro botín.

Pendiente: el test de cambio de contraseña está declarado pero todavía no tiene implementación. Los tests actuales no tienen asserts de resultado de negocio: el resultado se observa en la ejecución y en las capturas de Allure.

## Stack

Python · Selenium · pytest · Allure (screenshots) · WebDriverWait / expected_conditions

No hay `requirements.txt` declarado en el repo. Para ejecutarlo hic falta instalar Selenium, pytest y allure-pytest.

## Estructura

```
global_functions/ → helpers de interacción y login
test/             → tests de login y de filtro de botines
main.py           → archivo sin implementación
```

## Cómo correrlo

```bash
pip install selenium pytest allure-pytest
pytest -v
```

## Decisiones de diseño

- Helpers reutilizables para acciones comunes y login en `global_functions/`.
- Esperas explícitas con `WebDriverWait` y `expected_conditions`, además de esperas fijas en algunos pasos.
- Evidencia con `allure.attach` de capturas de pantalla.

## Estado

Suite de demostración ejecutada en local. Sin CI por ahora.
