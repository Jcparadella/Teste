import streamlit as st
import pandas as pd

# --- Configuração da Página ---
st.set_page_config(
    page_title="Formulário de Registro - IHC",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Título e Descrição ---
st.title("📝 Sistema de Registro de Usuários")
st.markdown(
    """
    Preencha os campos abaixo para registrar novos usuários. Os dados serão exibidos em uma tabela
    e você terá a opção de baixá-los em formato CSV.
    """
)
st.markdown("---")

# --- Inicialização da Sessão (para armazenar os dados) ---
# Adicionamos as novas colunas "Nome" e "CPF" ao DataFrame
if 'df_registros' not in st.session_state:
    st.session_state.df_registros = pd.DataFrame(columns=["Nome", "Sexo", "Idade", "CPF"])

# --- Formulário de Registro ---
st.header("✨ Registrar Novo Usuário")

with st.form(key='registro_form', clear_on_submit=True): # clear_on_submit=True já limpa os campos automaticamente
    # Campo Nome
    nome = st.text_input(
        "Nome Completo:",
        placeholder="Digite o nome do usuário",
        help="Informe o nome completo do usuário."
    )

    # Campos Sexo e Idade em colunas para melhor organização visual
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
    
    # Campo CPF
    cpf = st.text_input(
        "CPF:",
        placeholder="___.___.___-__",
        max_chars=14, # Limita o número de caracteres para um CPF formatado
        help="Informe o CPF do usuário (apenas números ou formatado)."
    )

    st.markdown("---") # Separador visual

    # Botão de Registro
    submit_button = st.form_submit_button(label='✅ Registrar Usuário')

if submit_button:
    # Validação simples dos campos
    if nome and sexo and idade is not None and cpf:
        novo_registro = pd.DataFrame([{"Nome": nome, "Sexo": sexo, "Idade": idade, "CPF": cpf}])
        st.session_state.df_registros = pd.concat([st.session_state.df_registros, novo_registro], ignore_index=True)
        st.success("Usuário registrado com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos para registrar o usuário.")

### Tabela de Dados

st.header("📋 Dados Registrados")

if not st.session_state.df_registros.empty:
    st.dataframe(st.session_state.df_registros.style.set_properties(**{'background-color': '#f0f2f6', 'color': 'black'}), use_container_width=True)

    # --- Botão de Download CSV ---
    st.markdown("---") # Separador visual para o botão
    
    # Converte o DataFrame para CSV
    csv = st.session_state.df_registros.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="📥 Baixar Tabela em CSV",
        data=csv,
        file_name="registros_usuarios.csv",
        mime="text/csv",
        help="Clique para baixar os dados da tabela em formato CSV."
    )
else:
    st.info("Nenhum dado registrado ainda. Utilize o formulário acima para adicionar usuários.")


st.markdown("---")
st.caption("Desenvolvido com ❤️ por seu especialista em Python e Streamlit em Serra, Espírito Santo.")
