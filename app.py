import pandas as pd
import plotly.express as px
import streamlit as st

#importar datos
st.title("Análisis de Ventas de Propiedades")
df=pd.read_csv('house_sales.csv')
df=df.dropna()
df["DocumentDate"]=pd.to_datetime(df["DocumentDate"])
df=df[["DocumentDate","SalePrice","PropertyType","SqFtLot","YrBuilt","LandVal"]]
df=df.rename(columns={"DocumentDate":"Fecha de Venta","SalePrice":"Precio de Venta","PropertyType":"Tipo de Propiedad",
                      "SqFtLot":"Pies cuadrados","YrBuilt":"Año de Propiedad","LandVal":"Costo del Terreno"})
df["Antiguedad"]=2025-df["Año de Propiedad"]
df["Metros cuadrados"]=df["Pies cuadrados"]*0.092903
del df["Pies cuadrados"]
del df["Año de Propiedad"]

por_antiguedad = st.toggle("Realizar analisis por antiguedad")
if por_antiguedad:
    #Filtro por rango de antiguedad
    antiguedad_selec_desd = st.slider("Seleccione la antiguedad en anos para filtrar las propiedades inicial",
                                        min_value=int(df["Antiguedad"].min()),
                                        max_value=int(df["Antiguedad"].max()),
                                        value=int(df["Antiguedad"].min()))
    antiguedad_selec_hasta = st.slider("Seleccione la antiguedad en anos para filtrar las propiedades final",
                                        min_value=int(df["Antiguedad"].min()),
                                        max_value=int(df["Antiguedad"].max()),
                                        value=int(df["Antiguedad"].max()))
    df_filtrado=df[(df["Antiguedad"]>=antiguedad_selec_desd) & (df["Antiguedad"]<=antiguedad_selec_hasta)]
    st.write(f"Existe {df_filtrado.shape[0]} resultados para la antiguedad seleccionada")
    st.dataframe(df_filtrado)

por_tipo = st.toggle("Realizar analisis por tipo")
if por_tipo:
    #Filtro por tipo de propiedad
    df["Tipo de Propiedad"].replace("Single Family","Casa unifamiliar",inplace=True)
    df["Tipo de Propiedad"].replace("Townhouse","Casa adosada",inplace=True)
    df["Tipo de Propiedad"].replace("Multiplex","Multifamiliar",inplace=True)
    tabla=df["Tipo de Propiedad"].value_counts()
    lista=tabla.index.tolist()
    tipo_selec=st.selectbox("Seleccione el tipo de propiedad",lista)
    df_filtrado=df[df["Tipo de Propiedad"]==tipo_selec]
    st.dataframe(df_filtrado)
    st.write(f"Existe {df_filtrado.shape[0]} resultados para la el tipo seleccionado")

#Toggle
por_fecha = st.toggle("Realizar analisis por fecha")
if por_fecha:
    #Filtrar por fecha
    df["Fecha"]=df["Fecha de Venta"].dt.date
    fecha_selec_desd = st.date_input("Seleccione una fecha de venta inicial",
                                        min_value=df["Fecha de Venta"].min(),
                                        max_value=df["Fecha de Venta"].max(),
                                        value=df["Fecha de Venta"].min())
    fecha_selec_hasta = st.date_input("Seleccione una fecha de venta final",
                                        min_value=df["Fecha de Venta"].min(),
                                        max_value=df["Fecha de Venta"].max(),
                                        value=df["Fecha de Venta"].max())
    df_filtrado=df[(df["Fecha"]>=fecha_selec_desd) & (df["Fecha"]<=fecha_selec_hasta)]
    df_filtrado = df_filtrado.sort_values("Fecha de Venta")
    st.write(f"Existe {df_filtrado.shape[0]} resultados para la fecha seleccionada")
    st.dataframe(df_filtrado)