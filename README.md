# Algoritmo-Genetico-Modulos
Este trabalho propõe uma solução para otimizar o tempo de atualização de um data warehouse utilizando algoritmo genético para encontrar grupos de módulos a serem processados em paralelo, sem sobrecarregar o servidor da empresa. A ideia é que os grupos sejam definidos com base nos dados de 2024, para que o método esteja operacional a partir de 2025.


### Descrição
Na Controllab, empresa especializada em controle de qualidade para laboratórios, a equipe de análise de dados desenvolveu um pipeline para criar e alimentar um data warehouse, atendendo as demandas do setor e da empresa. Devido à complexidade do banco de dados em produção, a equipe de TI implementou endpoints para facilitar a extração de informações. 

O endpoint principal permite buscar apenas um módulo por vez, correspondente a um ano de dados. Para melhorar o entendimento, módulo é um conjunto de exames definidos para o ensaio de proficiência. Cada módulo contém um volume variável de informações, dependendo do número de participantes do programa (quórum). Com mais de 800 módulos gerados anualmente, o processo de atualização completo leva mais de 4,5 horas para ser concluído. 

Este trabalho propõe uma solução para otimizar esse tempo, utilizando um algoritmo genético para agrupar módulos que possam ser processados simultaneamente, sem sobrecarregar o servidor da empresa. A ideia é que os grupos sejam definidos com base nos dados de 2024, para que o método esteja operacional a partir de 2025.

### Objetivo
Reduzir significativamente o tempo de atualização do data warehouse, maximizando o número de requisições em paralelo.

### Restrições
A soma do número de linhas de cada grupo de módulos não pode exceder 200 mil, para evitar sobrecarga no servidor.

Por exemplo, o módulo 58 possui mais de 1 milhão de linhas. Colocá-lo em paralelo com outro módulo pode gerar prejuízos de performance e comprometer o sistema.


### Resultados
Os resultados obtidos foram satisfatórios, com potencial significativo para reduzir o tempo total do ETL. Como o processo de atualização tem o intuito de ser diário, o uso de paralelismo mostra-se indispensável. O algoritmo genético foi aplicado em looping, buscando otimizar os grupos em cada iteração. Os 10 primeiros grupos gerados apresentaram resultados próximos ao limite de 200 mil linhas, evidenciando o bom ajuste do algoritmo.

### Melhorias
Embora os resultados sejam promissores, uma melhoria relevante é incluir o tempo de requisição como variável. O paralelismo apresenta maior eficiência quando as requisições de um mesmo grupo possuem tempos de resposta similares. No entanto, atualmente não dispomos do tempo médio por módulo, e sua obtenção envolve desafios, como a necessidade de estabilidade do servidor durante todo o período de análise para garantir a confiabilidade dos dados de tempo. 

Com esses dados adicionais, seria possível implementar melhorias que minimizem ainda mais o tempo total de requisição, mantendo a restrição de não sobrecarga do servidor. Essa abordagem abriria novas possibilidades para otimizar tanto a alocação dos módulos quanto a performance geral do sistema.

Buscando contornar esse problema, testamos colocar o desvio padrão dos dados como parte da função objetivo. Entretanto, não foi encontrada forma de minimizar o desvio garantindo a maximização da soma das linhas.

# Autor

| [<img src="https://avatars.githubusercontent.com/u/109088916?s=400&u=0128dd8ac18d3e18783c4f52c5bb89578f12311f&v=4" width=115><br><sub>Bruno Cavalcanti Santos</sub>](https://github.com/BrunoSantos14) |  [<img src="https://avatars.githubusercontent.com/u/117787474?v=4" width=115><br><sub>Victor Gomes</sub>](https://github.com/victoralmeida428) |
| :---: | :---:
