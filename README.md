# Ejecutar prueba tecnica

Seguir los siguientes pasos:

1. Clonar repositorio

```
git clone <URL_DEL_REPOSITORIO>
```

2. Navegar al directorio python (validar su ruta)

```
cd /prueba/tests
```

3. instalar dependencias usando pip

```
pip install -r requirements.txt
```

4. Ejecutar tests desde consola (cambiar datos en data.csv si quiere probrar con diferente data)

```
pytest TestRunner.py ó python -m pytest TestRunner.py
```



