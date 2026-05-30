from crewai import Agent, Task, Crew, LLM
from crewai_tools import ScrapeWebsiteTool

# Configuração do LLM via Ollama
# Na live usamos "ollama/glm-5:cloud" (gratuito no Ollama Cloud)
# Para rodar local, troque para "ollama/qwen3:8b" ou outro modelo disponível
llm = LLM(
    model="ollama/glm-5:cloud",
    base_url="http://localhost:11434"
)

# Ferramenta para acessar a página de carreiras da DIO
ferramenta_dio = ScrapeWebsiteTool(
    website_url="https://www.dio.me/#careers"
)

# TODO: Defina o Agente Mentor de Carreira em Tecnologia
mentor = Agent(
    role="Mentor Especialista e vasta experiência em Carreiras de Tecnologia",
    goal="Analisar o perfil, habilidades, comportamentos, histórico passado e interesses da pessoa no processo de mentoria, orientação e direcionamento, objetivando recomendar a trilha de carreira mais adequada entre as opções disponíveis na DIO em alinhamento com necessidades e oportunidades de mercado, explicando os diferenciais de cada área e os passos concretos para ingressar nela, esclarecendo o motivo das indicações e fornecendo 3 pontos diferencias dessas aopções oferecidas.",
    backstory="Você é um mentor de carreira com mais de 25 anos de experiência no mercado de tecnologia, tendo atuado como engenheiro de software, líder técnico e gerente de contratação em grandes empresas, possuindo formação psicanalítica e neurociência, o que embasa suas habilidades investigativas junto as pessoas, entendendo ainda melhor o perfil, à partir de comportamentos e aprendizados do passado destas pessoas. Ao longo da sua trajetória, você ajudou mais de 1000 profissionais a iniciarem ou fazerem transições de carreira na área de tecnologia. Você conhece profundamente as competências exigidas pelo mercado, as tendências de contratação e as trilhas de aprendizado mais eficientes. Na DIO, você acompanha de perto as oportunidades de carreira e os programas de formação disponíveis, permitindo oferecer conselhos práticos e personalizados para cada aluno.",
    tools=[ferramenta_dio],
    llm=llm,
    verbose=True
)

# Input do aluno
print("=== Mentor de Carreira em Tecnologia ===\n")
necessidade_aluno = input("Conte sobre sua situação atual e o que você busca na área de tecnologia:\n> ")

# TODO: Defina a Tarefa do agente
tarefa = Task(
    description=f"Com base na página de carreiras da DIO, oportunidades e necessidades de mercado, e nas informações das pessoas no processo de mentoria, analise e recomende a(s) melhor(es) trilha(s) de tecnologia para o seguinte perfil. Para cada recomendação, justifique com base nas habilidades da pessoa, nas exigências do mercado e nas oportunidades oferecidas pela DIO. Inclua uma sugestão de plano de estudos detalhada, com carga horária e sugestão de materiais de apoio e possíveis foruns para contato com outros profissionais e os próximos passos práticos.",
    expected_output="Um relatório completo e personalizado contendo: (1) análise do perfil do aluno identificando pontos fortes e áreas de desenvolvimento, (2) recomendações de 1 a 3 trilhas de carreira em tecnologia disponíveis na DIO com justificativas detalhadas, (3) comparação entre as opções destacando prós e contras de cada uma, (4) um plano de ação sugerido com próximos passos concretos e recursos de aprendizado recomendados, (5) Uma página para anotações de evolução e dúvidas.",
    agent=mentor
)

# Execução
crew = Crew(agents=[mentor], tasks=[tarefa])
resultado = crew.kickoff()
print("\n=== Resultado ===\n")
print(resultado)
