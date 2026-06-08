import streamlit as st
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import DuckDuckGoSearchTool

# Configura a chave de API
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def rodar_agente(pergunta):
    search_tool = DuckDuckGoSearchTool()
    pesquisador = Agent(
        role='Especialista Nsaoficial iA',
        goal='Fornecer análises com a qualidade Nsaoficial',
        backstory='Você é a IA oficial da Nsaoficial iA, focada em precisão.',
        tools=[search_tool]
    )
    tarefa = Task(description=pergunta, expected_output='Um resumo de 3 pontos', agent=pesquisador)
    equipe = Crew(agents=[pesquisador], tasks=[tarefa], process=Process.sequential)
    return equipe.kickoff()

# Interface Streamlit
st.title("🤖 Painel Nsaoficial iA")
query = st.text_input("O que a Nsaoficial iA deve pesquisar?")

if st.button("Executar Pesquisa"):
    with st.spinner('A Nsaoficial iA está trabalhando...'):
        resultado = rodar_agente(query)
        st.success("Pesquisa concluída!")
        st.write(resultado)
