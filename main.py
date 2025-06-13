import streamlit as st
import pandas as pd

# Configurações iniciais da página
st.set_page_config(
    page_title="Formulário de Registro - IHC",
    page_icon="📝", # Ícone ajustado para formulário/registro
    layout="centered",
    initial_sidebar_state="expanded"
)

# Título principal da aplicação
st.title("Sistema de Registro de Usuários")
st.markdown("Preencha os campos abaixo para registrar e visualizar os dados.")

# Inicializa o DataFrame no Session State se ele ainda não existe
if 'df_registros' not in st.session_state:
    st.session_state.df_registros = pd.DataFrame(columns=["Sexo", "Idade"])

# --- Formulário de Registro ---
st.header("Novo Registro")
with st.form(key='registro_form', clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        sexo = st.selectbox(
            "Sexo:",
            options=["Masculino", "Feminino", "Outro", "Não Informar"],
            help="Selecione o sexo do usuário."
        )
    with col2:
        idade = st.number_input(
            "Idade:",
            min_value=0,
            max_value=120,
            value=25,
            step=1,
            help="Informe a idade do usuário (entre 0 e 120 anos)."
        )

    st.markdown("---") # Separador visual
    submit_button = st.form_submit_button(label='Registrar')

if submit_button:
    if sexo and idade is not None:
        novo_registro = pd.DataFrame([{"Sexo": sexo, "Idade": idade}])
        st.session_state.df_registros = pd.concat([st.session_state.df_registros, novo_registro], ignore_index=True)
        st.success("Registro adicionado com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos para registrar.")

### Tabela de Dados

st.header("Dados Registrados")
if not st.session_state.df_registros.empty:
    st.dataframe(st.session_state.df_registros.style.set_properties(**{'background-color': '#f0f2f6', 'color': 'black'}), use_container_width=True)
else:
    st.info("Nenhum dado registrado ainda. Utilize o formulário acima para adicionar registros.")

st.markdown("---")
st.caption("Desenvolvido com Streamlit para IHC - 2025")


import streamlit as st
import pandas as pd

# Configurações iniciais da página
st.set_page_config(
    page_title="Formulário de Registro - IHC",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Título principal da aplicação
st.title("Sistema de Registro de Usuários")
st.markdown("Preencha os campos abaixo para registrar e visualizar os dados.")

# Inicializa o DataFrame no Session State se ele ainda não existe
if 'df_registros' not in st.session_state:
    st.session_state.df_registros = pd.DataFrame(columns=["Sexo", "Idade"])

# --- Formulário de Registro ---
st.header("Novo Registro")
with st.form(key='registro_form', clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        sexo = st.selectbox(
            "Sexo:",
            options=["Masculino", "Feminino", "Outro", "Não Informar"],
            help="Selecione o sexo do usuário."
        )
    with col2:
        idade = st.number_input(
            "Idade:",
            min_value=0,
            max_value=120,
            value=25,
            step=1,
            help="Informe a idade do usuário (entre 0 e 120 anos)."
        )

    st.markdown("---") # Separador visual
    submit_button = st.form_submit_button(label='Registrar')

if submit_button:
    if sexo and idade is not None:
        novo_registro = pd.DataFrame([{"Sexo": sexo, "Idade": idade}])
        st.session_state.df_registros = pd.concat([st.session_state.df_registros, novo_registro], ignore_index=True)
        st.success("Registro adicionado com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos para registrar.")

### Tabela de Dados

st.header("Dados Registrados")
if not st.session_state.df_registros.empty:
    st.dataframe(st.session_state.df_registros.style.set_properties(**{'background-color': '#f0f2f6', 'color': 'black'}), use_container_width=True)

    # --- Botão de Download CSV ---
    st.markdown("---") # Separador visual para o botão
    
    # Converte o DataFrame para CSV
    # index=False evita que o índice do DataFrame seja escrito no CSV
    csv = st.session_state.df_registros.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="Download Tabela em CSV",
        data=csv,
        file_name="registros_usuarios.csv",
        mime="text/csv",
        help="Clique para baixar os dados da tabela em formato CSV."
    )
else:
    st.info("Nenhum dado registrado ainda. Utilize o formulário acima para adicionar registros.")

st.markdown("---")
st.caption("Desenvolvido com Streamlit para IHC - 2025")
