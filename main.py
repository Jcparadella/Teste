import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações iniciais da página
st.set_page_config(
    page_title="Formulário de Registro - IHC",
    page_icon="📊",
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
with st.container():
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

# --- Tabela de Dados ---
st.markdown("---") # Separador visual
st.header("Dados Registrados")
if not st.session_state.df_registros.empty:
    st.dataframe(st.session_state.df_registros.style.set_properties(**{'background-color': '#f0f2f6', 'color': 'black'}), use_container_width=True)
else:
    st.info("Nenhum dado registrado ainda. Utilize o formulário acima para adicionar registros.")

# --- Gráficos de Estatísticas ---
st.markdown("---") # Separador visual
st.header("Estatísticas dos Registros")

if not st.session_state.df_registros.empty:
    col_graph1, col_graph2 = st.columns(2)

    with col_graph1:
        st.subheader("Distribuição por Sexo")
        fig_sexo, ax_sexo = plt.subplots(figsize=(6, 4))
        sexo_counts = st.session_state.df_registros['Sexo'].value_counts()
        sns.barplot(x=sexo_counts.index, y=sexo_counts.values, palette="viridis", ax=ax_sexo)
        ax_sexo.set_xlabel("Sexo")
        ax_sexo.set_ylabel("Número de Registros")
        ax_sexo.tick_params(axis='x', rotation=45)
        st.pyplot(fig_sexo)

    with col_graph2:
        st.subheader("Distribuição de Idade")
        fig_idade, ax_idade = plt.subplots(figsize=(6, 4))
        sns.histplot(st.session_state.df_registros['Idade'], bins=10, kde=True, color="skyblue", ax=ax_idade)
        ax_idade.set_xlabel("Idade")
        ax_idade.set_ylabel("Frequência")
        st.pyplot(fig_idade)
else:
    st.warning("Não há dados suficientes para gerar os gráficos. Registre alguns usuários primeiro.")

st.markdown("---")
st.caption("Desenvolvido com Streamlit e Matplotlib para IHC - 2025")
