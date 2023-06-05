# Análise Exploratória de Dados - Spotify

## Integrantes

| Nome | RA |
|------|-----------|
| Guilherme Samuel de Souza Barbosa | 19.00012-0 |
| Guilherme Cury Galli | 19.00374-9 |
| Matheus dos Santos Galbiati | 19.01324-8 |
| Fernando Laiser F Kon | 19.01336-0 |
| Igor Eiki Ferreira Kubota | 19.02466-5 |
| Gustavo Consoleti | 19.00715-9 |


## Bases de Dados Utilizadas

[Spotify Oficial API](https://developer.spotify.com/documentation/web-api/)

[Spotify Million Playlist Dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge/dataset_files)


## Objetivos

O objetivo do projeto é a construção completa de um EDA (Exploratory Data Analysis) sobre o conjunto de dados do spotify.

Ao final, foi respondido perguntas a respeito das principais características das músicas dos artistas mais populares de cada gênero, além de uma análise temporal da evolução das features das músicas ao longo dos anos.


## Como Rodar

O projeto foi dividido principalmente em dois notebooks, o "01_extração.ipynb" que foi utilizado para realizar a extração, tratamento  e limpeza de dados provenientes do _Spotify Million Playlist Dataset_ utilizando a API oficial do Spotify, formando assim os datasets utilizados, que se encontra no outro repositório do projeto , portanto não é necessário rodá-lo.

No notebook "02_EDA.ipynb" foram utilizados os datasets criados, tratando novamente os dados para realização de uma análise quantitativa. Com os dados tratados e outliers removidos, é feita a análise exploratória em cima, como correlação entre as variáveis. **Somente esse notebook deve ser rodado para a exibição do projeto**.


## Dotenv (24/05/2023)
```
CLIENT_ID=
CLIENT_SECRET=
API_TOKEN=
```
