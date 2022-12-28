INSTITUTO POLITÉCNICO DE TOMAR

UNIDADE DEPARTAMENTAL DE TECNOLOGIAS DE INFORMAÇÃO E COMUNICAÇÃO


Projeto (Parte I)
(Trabalho de Grupo)
APIs, Packages

Objetivo: Familiarização com os conceitos de obtenção de dados a partir de diferentes
sources via APIs e packages Python
Entrega: Os trabalhos devem ser inseridos na plataforma de e-Learning em data a anunciar
pelo docente.

Realização do trabalho: Os trabalhos devem ser entregues em formato notebook
(devidamente documentados).

Neste exercício pretende-se reunir os dados meteorológicos de um conjunto de cidades portuguesas bem como a sua distância para uma cidade de referência. Pretende-se com esta base de dados reunir informação que permita no futuro aplicar um algoritmo de machine learning que estude o efeito (se algum) que a proximidade de uma cidade, ao mar, tem no clima local. Para esse efeito, pretende-se reunir um conjunto de 10 cidades com diferentes distâncias relativamente a uma cidade costeira de referência. Na escolha das cidades devese optar por deixar de fora, cidades montanhosas por forma a evitar a introdução de outros fatores que poderão afetar o clima (nomeadamente a altitude).

Deverá proceder à recolha dos dados meteorológicos a cada 1 hora durante o espaço de 5 dias consecutivos.
Para a obtenção automática das distâncias (air distance) entre as cidades
sugere-se o recurso a packages de Geocoding (Geocoding is the computational process of
transforming a physical address description to a location on the Earth’s surface (spatial
representation in numerical coordinates) — Wikipedia).
1. Recorra a uma biblioteca Python que permita plotar num mapa google as localidades
consideradas.
2. Com recurso à API “Current Weather” (https://openweathermap.org/current) obtenha
os seguintes dados meteorológicos a cada hora durante o espaço de 5 dias consecutivos:

• Temperature

• Humidity

• Pressure

• Description

• Wind speed

• Wind degree

• Timestamp (dt)

Para a obtenção dos dados (e em alternativa ao uso da sua máquina local) sugere-se
executar o código durante os referidos 5 dias na seguinte máquina virtual:
https://www.pythonanywhere.com/
3. Recorra a packages de geocoding (e.g., “Geopy”
(https://geopy.readthedocs.io/en/stable/) para obter de forma programática a distância
entre as cidades selecionadas e a cidade de referência.
4. Guarde os dados obtidos num único ficheiro json.
5. Liste os dados num dataframe.
