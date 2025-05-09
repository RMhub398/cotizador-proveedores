import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Cotizador de Equipos", page_icon="💰")

st.title("📊 Cotizador de Equipos - Grupo Proservices")

# --- Cargar archivo CSV directamente desde GitHub ---
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/RMhub398/cotizador-proveedores/main/Matriz_proveedores.csv"
    return pd.read_csv(url)

df = load_data()

# --- Filtros de búsqueda ---
st.sidebar.header("Filtros")
marca = st.sidebar.selectbox("Selecciona una marca", df["Marca"].dropna().unique())
modelo = st.sidebar.selectbox("Selecciona el modelo", df[df["Marca"] == marca]["Línea de Producto"].dropna().unique())

# --- Selección del producto ---
producto = df[(df["Marca"] == marca) & (df["Línea de Producto"] == modelo)].iloc[0]

# --- Mostrar información del producto ---
st.subheader(f"🧾 Detalles de {marca} - {modelo}")
st.write(f"**Proveedor:** {producto['Proveedor']}")
st.write(f"**Categoría:** {producto['Categoría Producto']}")
st.write(f"**Procedencia:** {producto['Procedencia']}")
st.write(f"**Descuento base:** {producto['% Desc. Proveedor']*100:.2f}%")
st.write(f"**Forma de cotizar:** {producto['Buscar Precio en']}")
st.write(f"**Condiciones de pago:** {producto['Condición de pago por monto']}")
st.write(f"**Garantía:** {producto['Garantía']}")

# --- Cálculo del precio ---
st.divider()
st.subheader("💰 Calculadora de Precio")

precio_lista = st.number_input("Ingresa precio de lista", min_value=0.0, step=1000.0)
descuento_base = producto['% Desc. Proveedor']
precio_con_desc = precio_lista * (1 - descuento_base)

if precio_con_desc > 1500000:
    st.success("🎯 Aplica a descuento extra")
    desc_extra = st.slider("Descuento adicional (%)", 0.0, 20.0, 5.0)
    precio_final = precio_con_desc * (1 - desc_extra/100)
else:
    desc_extra = 0.0
    precio_final = precio_con_desc

# --- Resultados finales ---
st.divider()
st.subheader("📌 Resultado Final")
col1, col2 = st.columns(2)
col1.metric("Precio Final", f"${precio_final:,.0f}")
col2.metric("Descuento Total", f"{(1 - precio_final/precio_lista)*100:.2f}%")

# --- Contacto proveedor ---
st.divider()
st.subheader("📞 Contacto del Proveedor")
st.write(f"**Vendedor:** {producto['Contacto Vendedor']}")
st.write(f"**Email:** {producto['Email']}")
st.write(f"**Teléfono:** {producto['Teléfono Oficina/ Sino hay respuesta del vendedor']}")
st.write(f"**Web/App:** {producto['Web/App proveedor']}")
