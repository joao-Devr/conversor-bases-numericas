# Trabalho de Conversão de bases Numéricas 

#### Nomes
Katriel Felipe Reis Carvalho
João Pedro Campolina Rodrigues


#### Linguagem Escolhida
Python

## Intruções de como usar
Para poder usar o projeto é necessário ter o [Python3](https://www.python.org/downloads/) instalado.

Após a instalação do python3, é necessário clonar o projeto na sua máquina e entrar na pasta do projeto:

```bash
git clone https://github.com/joao-Devr/conversor-bases-numericas.git
cd conversor-bases-numericas
```

Após isso, abra o terminal da pasta conversor-bases-numericas e execute o comando:

```bash
python3 main.py
```
## Estrutura do projeto
```
conversor-bases-numericas/
├── conversor.py   # Arquivo em que é feita as conversões
├── entrada.csv    # Arquivo de csv contendo valores, base_origem e base_destino.
├── formatador.py  # Arquivo que administra as respostas e administra a impressão de saida.csv
├── main.py        # Menu simples para selecionar a opção
├── parser.py      # Responsável pela entrada dos valores
├── quiz_core.py   # Núcleo responsavel pela elaboração do quiz
└── saida.csv      # Arquivo com as respostas para os valores passados pelo entrada.csv
``` 

Vídeo explicativo sobre o projeto: LINK

## Exemplos de Uso

O projeto pode ser usado para converter bases a fim de aprender, pois possui metódo passo a passo para que o aluno possa além de ver a resposta, ver onde ele pode ter possívelmente errado. Além disso, para melhor aprofundar os estudos, o projeto também tem um modo quiz, com perguntas que o aluno pode responder para frizar o conteúdo.

Além de ser usado para aprender, pode também ser usado diretamente para ser uma calculadora de conversão de bases.


## Limitações
Não possuí suporte para números negativos, além disso, ele aceita apenas as bases binário, decimal, octal e hexadecimal, ou seja, não aceita bases customizáveis. 
