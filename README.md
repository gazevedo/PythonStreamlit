Dashboard de Contratos com Streamlit e Heroku


Desenvolvemos uma aplicação web interativa usando Python e Streamlit, hospedada no Heroku, para visualização e análise de dados de contratos.
Este dashboard fornece uma interface amigável para que usuários possam explorar e analisar dados de contratos de maneira eficiente e intuitiva.

Funcionalidades:
- Carregamento de Dados:
Utilizamos a biblioteca pandas para carregar e manipular dados de um arquivo CSV contendo informações sobre contratos.
Os dados são carregados e armazenados em cache utilizando st.cache_data para melhorar o desempenho.
Visualização Interativa:

A interface principal do aplicativo permite aos usuários visualizar um dashboard com gráficos interativos.
Os gráficos são atualizados dinamicamente com base no período selecionado pelo usuário (1 dia, 15 dias, 31 dias).
 
Tecnologias Utilizadas:
Python: Linguagem principal para desenvolvimento da aplicação.
Streamlit: Framework usado para criar a interface web interativa.
Pandas: Biblioteca para manipulação e análise de dados.
Heroku: Plataforma de nuvem usada para hospedar a aplicação.
