import streamlit as st
from src.extraction import load_data

st.set_page_config(layout = 'wide')

def create_dataframe_selection(df):
    st.title("Database")

    col1, col2 = st.columns(2)

    col1.header("Database")
    col1.dataframe(df, heigth=530)

    col2.header("Data Description")

    data_description = """
                        | Coluna | Descrição |
                        | ID | Identificado da linha/registro|       
                        | name | Fabricante e Modelo da Moto |
                        | selling_price | Preço de Venda |
                        | year | Ano de Fabricação da Moto |
                        | seller_type | Tipo do Vendedor - Se é pessoal ou revendedor |
                        | owner | Se é primeiro, segundo, terceiro ou quarto dono da moto |
                        | km_driven | Quantidade de quilometros percorrido pela moto |
                        | ex_showroom_price | Preço da motocicleta sem as taxas de seguro e registro |  
                        | age | Quantidade de anos em que a moto está em uso |
                        | km_class | Classificação das motos conforme a quilometragem percorrida | 
                        | km_per_year | Quantidade de Quilometros percorridos a cada ano |
                        | km_per_month | Quantidade de Quilometros percorridos a cada mês |
                        | company | Fabricante da Motocicleta |
    """
    col2.markdown(data_description)

    return None

def main():    
    df_raw = load_data()

    st.dataframe(df_raw)

if __name__ == '__main__':
    main()
