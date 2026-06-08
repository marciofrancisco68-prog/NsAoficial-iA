from crewai import Agent, Task, Crew
from crewai_tools import DuckDuckGoSearchTool

# Ferramenta de busca na web
search_tool = DuckDuckGoSearchTool()

# Criando o Agente
pesquisador = Agent(
    role='Pesquisador Autônomo',
    goal='Encontrar as principais novidades sobre tecnologia hoje',
    backstory='Você é um especialista em monitorar a web e resumir notícias.',
    tools=[search_tool],
    verbose=True
)

# Criando a tarefa
tarefa = Task(
    description='Faça uma busca sobre avanços em IA em 2026 e resuma em 3 pontos.',
    expected_output='Um resumo de 3 pontos com as principais notícias.',
    agent=pesquisador
)

# Executando
equipe = Crew(agents=[pesquisador], tasks=[tarefa])
resultado = equipe.kickoff()

print("Resultado da pesquisa:")
print(resultado)
