# 🌧️ Análise de Precipitação em Estações Meteorológicas do Interior Paulista

Este projeto tem como objetivo analisar dados de precipitação coletados em diversas estações meteorológicas localizadas no interior do estado de São Paulo. A motivação surge da necessidade de compreender como as chuvas intensas contribuem para os alagamentos que afetam tanto grandes centros urbanos quanto municípios de menor porte.

🔗 **Acesse o site da análise em:**
👉 [checkpoint2precipitacao.streamlit.app](https://checkpoint2precipitacao.streamlit.app)

## 🧩 Contextualização

Diversas cidades do interior paulista, como Ribeirão Preto, São José do Rio Preto, Franca, Barretos, Catanduva, Sertãozinho, Bebedouro, Monte Alto e Pontal, enfrentam problemas recorrentes com alagamentos. Os impactos desses eventos incluem:

- Desalojamento de famílias: Centenas de famílias já foram obrigadas a deixar suas residências devido às inundações.

- Danos materiais: Perdas em residências, comércios e indústrias devido à invasão da água.

- Problemas na infraestrutura urbana: Ruas alagadas, erosão de vias, rompimento de pavimentação e problemas na rede elétrica.

- Impactos na mobilidade: Interrupção de vias e dificuldades no transporte público e privado.

- Riscos à saúde pública: Contaminação da água, proliferação de doenças transmitidas por enchentes (como leptospirose) e aumento da umidade, favorecendo doenças respiratórias.

- Prejuízos ao agronegócio: Perdas de plantações e impactos na produção agrícola, especialmente em regiões com grandes áreas de cultivo.

## 📉 Objetivos da Análise

- Avaliar a distribuição das chuvas nas regiões analisadas
- Investigar a variabilidade das precipitações ao longo do tempo
- Verificar padrões sazonais de chuva e períodos de estiagem
- Explorar a relação entre instabilidade na precipitação e eventos extremos
- Gerar insights para políticas públicas e planejamento urbano e agrícola

## 🧪 Técnicas Utilizadas

- **Distribuição Normal:** Verificação da normalidade dos dados de precipitação
- **Intervalo de Confiança:** Estimativas da média com margem de erro
- **Teste de Hipóteses:** Comparação de médias entre regiões e períodos
- **Análise Regional:** Visualização das diferenças entre as cidades monitoradas
- **Padrões Sazonais:** Identificação de sazonalidade das chuvas e secas

## 📦 Bibliotecas Utilizadas

O projeto foi desenvolvido em Python, utilizando as seguintes bibliotecas:

- `pandas` – Manipulação e análise de dados
- `numpy` – Cálculos matemáticos e estatísticos
- `scipy` – Testes estatísticos e análise científica
- `streamlit` – Interface web interativa para visualização de dados
- `plotly` – Gráficos interativos
- `plotnine` – Visualização de dados com gramática de gráficos (inspirado no ggplot2)
- `pymannkendall` – Análise de tendências climáticas
- `geopy` – Cálculo de distâncias e localização geográfica

## ❓ Principais Perguntas de Pesquisa

1. Quais regiões do dataset apresentam maior ocorrência de precipitação?
2. Como a instabilidade na precipitação (desvio padrão alto) impacta a frequência de eventos extremos?
3. Existe um padrão sazonal na incidência de chuvas mais volumosas?
4. Quais regiões apresentam maior número de dias consecutivos de chuva ou estiagem?
5. Há relação entre a estação do ano e a ocorrência de períodos chuvosos ou secos?

## 🔍 Fontes de Dados

Os dados utilizados nesta análise provêm de estações meteorológicas distribuídas pelo interior do estado de São Paulo. Essas informações foram tratadas e estruturadas para permitir análises estatísticas e inferências relevantes.

## 🚀 Como Executar Localmente

1. Clone o repositório:

   ```bash
   git clone https://github.com/CavMCarolina/Analise-Precipitacao.git
   cd Analise-Precipitacao
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute o Streamlit:

   ```bash
   streamlit run introducao.py
   ```

## 💡 Conclusão

A análise de dados meteorológicos permite não só entender a frequência e intensidade das chuvas, mas também prever riscos e apoiar políticas públicas para mitigar os impactos de alagamentos em áreas vulneráveis. Este projeto é uma ferramenta importante para o planejamento urbano sustentável e estratégias preventivas.