# **Análisis de Penetración de Internet por Hogar**

## **Introducción**
Este proyecto tiene como objetivo principal analizar la penetración del servicio de Internet en los hogares de distintas provincias en Argentina. Usamos herramientas como Power BI y Streamlit para crear dashboards interactivos, Python para la exploración y limpieza de datos, y MySQL como base de datos relacional para gestionar los datos de manera eficiente.

El análisis incluye la implementación de KPIs clave que permiten evaluar el progreso hacia un mayor acceso a Internet, identificar brechas digitales y proponer estrategias para cerrar esas diferencias.

### **Objetivos específicos**
- Crear dashboards interactivos que faciliten la interpretación de datos.
- Realizar un análisis exploratorio de datos (EDA) para evaluar su calidad e identificar patrones.
- Implementar KPIs relevantes, incluyendo el crecimiento del 2% en el acceso a Internet por cada 100 hogares.
- Integrar y limpiar los datos en una base de datos relacional.
- Extraer insights significativos que apoyen en la toma de decisiones informadas.

---

## **Estructura del repositorio**
El proyecto está organizado en las siguientes carpetas y archivos clave:

### **Carpetas**
- **`dashboards/`**:
  - `Internet.pbix`: Archivo Power BI que contiene las visualizaciones y los KPIs desarrollados.
  - `app.py`: Script Streamlit que ofrece un panel interactivo para filtrar y visualizar datos dinámicamente.
  
- **`data/`**:
  - `Internet.xlsx`: Dataset principal con los datos utilizados para el análisis.

### **Archivos principales**
- **`README.md`**: Documentación del proyecto que detalla su propósito, estructura y cómo reproducirlo.
- **`tp2.ipynb`**: Notebook Jupyter con Script que realizan el análisis exploratorio, vuelco de datos a MySQL y limpieza avanzada.
- **`tp2-pruebas.ipynb`**: Notebooks utilizados para realizar pruebas en los datos y métricas.

---

## **Descripción de las funcionalidades del proyecto**
### **1. Análisis Exploratorio de Datos (EDA)**
El archivo `tp2.ipynb` implementa las siguientes funcionalidades:
- **Exploración de datos**:
  - Detección de valores faltantes y duplicados.
  - Estadísticas descriptivas para columnas numéricas.
- **Visualización de outliers y distribuciones**:
  - Boxplots y histogramas para detectar valores extremos e interpretar distribuciones.

### **2. Vuelco de datos a MySQL**
Los datos del archivo `Internet.xlsx` son cargados a una base de datos MySQL con las siguientes características:
- **Creación automática de tablas**:
  - Cada hoja del archivo Excel se convierte en una tabla, ajustando los nombres para evitar errores SQL.
- **Inserción dinámica de datos**:
  - Los registros de cada hoja son insertados respetando la estructura definida.

### **3. Limpieza de datos en MySQL**
La limpieza se realiza directamente en las tablas creadas y consta de:
- Eliminación de registros con valores faltantes o vacíos en columnas críticas (`Año`, `Trimestre`, `Provincia`, etc.).
- Corrección de valores mal ingresados (por ejemplo, años con caracteres erróneos).
- Validación para garantizar consistencia en los datos.

### **4. Dashboards interactivos con Power BI y Streamlit**
- **Power BI**:
  - Dashboards que incluyen visualizaciones estáticas de KPIs y tendencias clave, como el crecimiento del acceso a Internet.
- **Streamlit**:
  - `app.py` permite filtrar datos por provincia, visualizar gráficos interactivos y resaltar el cumplimiento de objetivos con colores (verde, amarillo y rojo).

---

## **Reporte de análisis**
### **Visualizaciones clave**
1. **Crecimiento de acceso por provincia**:
   - Muestra el porcentaje de incremento en el acceso a Internet por cada 100 hogares.
2. **Promedio de accesos por tecnología**:
   - Destaca la adopción de ADSL, fibra óptica, wireless, entre otras tecnologías.
3. **Mapa de penetración**:
   - Representa geográficamente la cobertura del servicio.

### **Hallazgos principales**
- Las provincias urbanas presentan un crecimiento sostenido gracias a la adopción de tecnologías avanzadas.
- Las regiones rurales enfrentan mayores desafíos, con un acceso significativamente limitado.

---

## **Análisis de KPIs**
### **KPI principal: Incremento del 2%**
- **Fórmula**:
  $$KPI = \frac{\text{NuevoAcceso} - \text{AccesoActual}}{\text{AccesoActual}} \times 100$$
- **Descripción**:
  - Mide si el crecimiento del acceso a Internet alcanzó un 2% adicional por cada 100 hogares en el próximo trimestre.
- **Resultados**:
  - Provincias como Córdoba lograron el objetivo, mientras que otras áreas rurales muestran dificultades.

### **KPIs adicionales**
1. **Penetración total**:
   - Evalúa el porcentaje de hogares conectados en relación con el total.
2. **Comparación tecnológica**:
   - Analiza la proporción de hogares que utilizan diferentes tecnologías de acceso (ADSL, fibra óptica, etc.).

---

## **Conclusiones**
- El análisis resalta una brecha digital significativa entre provincias urbanas y rurales.
- Se recomienda priorizar inversiones en infraestructura de fibra óptica para aumentar el acceso en áreas rurales.

---

## **Instrucciones para reproducir el proyecto**
### **Requisitos previos**
- **Power BI Desktop** para explorar el archivo `Internet.pbix`.
- **MySQL** configurado para la base de datos relacional.
- **Python 3.x** y las siguientes librerías:
  ```bash
  pip install pandas numpy matplotlib seaborn mysql-connector-python streamlit