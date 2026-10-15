# Panel de control de una aplicación web usando el servicio de Render

Aplicación web construida con **Streamlit** y **Plotly** para explorar un conjunto de datos de anuncios de venta de coches en EE. UU. (`vehicles_us.csv`).

🔗 **Aplicación desplegada:** [https://streamlit-webapp-tlvd.onrender.com](https://streamlit-webapp-tlvd.onrender.com)

## Funcionalidades

- Encabezado y resumen del conjunto de datos.
- Casilla para mostrar una muestra de los datos.
- Casilla para construir un **histograma** de la distribución del odómetro.
- Casilla para construir un **gráfico de dispersión** de odómetro frente a precio, coloreado según la condición del coche.

## Estructura

```
├── app.py              # Aplicación Streamlit
├── vehicles_us.csv     # Datos
├── requirements.txt    # Dependencias
├── .python-version     # Versión de Python (3.12)
└── notebooks/
    └── EDA.ipynb       # Análisis exploratorio de datos
```

## Ejecución local

```bash
uv venv --python 3.12
uv pip install -r requirements.txt
uv run streamlit run app.py
```

## Despliegue

Desplegada en [Render](https://render.com) como Web Service:

- **Build Command:** `pip install --upgrade pip && pip install -r requirements.txt`
- **Start Command:** `streamlit run app.py`