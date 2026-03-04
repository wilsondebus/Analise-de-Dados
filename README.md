# 📊 Análise de Cancelamento de Clientes (Churn Analysis)

Projeto de análise de dados desenvolvido em Python com o objetivo de identificar os principais fatores que levam clientes ao cancelamento de contrato.

A partir de uma base de dados (cancelamentos.csv), foram realizadas etapas de tratamento, análise exploratória e simulação de cenários para redução da taxa de churn.

# 🎯 Objetivo do Projeto

Entender o comportamento dos clientes que cancelaram

Identificar padrões relacionados ao cancelamento

Propor estratégias para reduzir a taxa de churn

Simular cenários após possíveis melhorias no processo

# 🛠️ Tecnologias Utilizadas
🐍 Python
📊 Pandas
📄 CSV (base de dados)
📓 Jupyter Notebook / ambiente interativo

# 📂 Estrutura do Projeto
📁 analise-cancelamentos
│-- analise.py (ou notebook.ipynb)
│-- cancelamentos.csv
│-- README.md
# 📌 Etapas do Projeto
1️⃣ Importação da Base de Dados

Leitura do arquivo CSV com pandas.read_csv()

Visualização inicial com display()

2️⃣ Tratamento de Dados

Análise estrutural com tabela.info()

Remoção de valores vazios (dropna())

Exclusão de colunas irrelevantes (ex: CustomerID)

3️⃣ Análise Exploratória

Contagem de cancelamentos

Cálculo do percentual de churn

Identificação de padrões comportamentais

tabela["cancelou"].value_counts(normalize=True)
# 🔎 Principais Insights Encontrados

📌 Clientes com contrato mensal cancelam mais
→ Estratégia sugerida: oferecer desconto para migração para planos trimestrais/anuais.

📌 Clientes que ligam mais de 4 vezes para o call center tendem a cancelar
→ Estratégia sugerida: criar alerta preventivo ao atingir 3 ligações.

📌 Clientes com mais de 20 dias de atraso apresentam alta taxa de cancelamento
→ Estratégia sugerida: política de renegociação preventiva após 15 dias.

# 📉 Simulação de Cenário

Após filtrar:

Contratos diferentes de "Monthly"

Até 4 ligações ao call center

Até 20 dias de atraso

Foi recalculada a taxa de cancelamento para avaliar o impacto potencial das melhorias.

# 🧠 Conceitos Aplicados

Limpeza e tratamento de dados

Análise exploratória (EDA)

Manipulação de DataFrames

Filtros condicionais

Geração de insights estratégicos

Simulação de cenários de negócio

# 🚀 Possíveis Melhorias Futuras

📊 Visualizações com Matplotlib ou Seaborn
📈 Modelo preditivo de Machine Learning (Logistic Regression)
📋 Dashboard interativo (Power BI ou Streamlit)
📉 Métricas mais avançadas de retenção


# 👨‍💻 Autor
Wilson Dias Debus

Estudante de Ciências da Computação
