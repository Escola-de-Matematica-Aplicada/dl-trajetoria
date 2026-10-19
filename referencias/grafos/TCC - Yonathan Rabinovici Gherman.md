# **Fundação Getulio Vargas** **Escola de Matemática Aplicada** **Curso de Graduação em Ciência de Dados e** **Inteligência Artificial**

## **Sistema de Apoio a Atendimento de Chamados via** **GraphRAG com Grafo de Conhecimento em Neo4j** **por Yonathan Rabinovici Gherman**

Rio de Janeiro              - Brasil

2025


# **Fundação Getulio Vargas** **Escola de Matemática Aplicada** **Curso de Graduação em Ciência de Dados e** **Inteligência Artificial**

## **Sistema de Apoio a Atendimento de Chamados via** **GraphRAG com Grafo de Conhecimento em Neo4j**

“ **Declaro** **ser** **o** **único** **autor** **do** **presente** **projeto** **de** **monografia** **que** **refere-se**


**ao** **plano** **de** **trabalho** **a** **ser** **executado** **para** **continuidade** **da** **monografia** **e**


**ressalto** **que** **não** **recorri** **a** **qualquer** **forma** **de** **colaboração** **ou** **auxílio** **de**

**terceiros** **para** **realizá-lo** **a** **não** **ser** **nos** **casos** **e** **para** **os** **fins** **autorizados** **pelo**


**professor** **orientador.** ”

## **Yonathan Rabinovici Gherman**


Rio de Janeiro              - Brasil

2025


# **Fundação Getulio Vargas** **Escola de Matemática Aplicada** **Curso de Graduação em Ciência de Dados e** **Inteligência Artificial**

## **Sistema de Apoio a Atendimento de Chamados via** **GraphRAG com Grafo de Conhecimento em Neo4j**

“ **Projeto** **de** **Monografia** **apresentado** **à** **Escola** **de** **Matemática** **Aplicada** **como**

**requisito** **parcial** **para** **continuidade** **ao** **trabalho** **de** **monografia.** ”


**Aprovado** **em** **de** **de**


**Grau** **atribuído** **ao** **Projeto** **de** **Monografia:**


**Professor** **Orientador:** **Júlio** **César** **Chaves**


**Escola** **de** **Matemática** **Aplicada**


**Fundação** **Getúlio** **Vargas**


## **Resumo**

O suporte técnico em Tecnologia da Informação (TI) enfrenta desafios constantes relacionados à triagem eficiente de chamados e à resolução de problemas que dependem de
informações contextuais frequentemente omitidas pelos usuários em suas solicitações iniciais. O avanço dos Grandes Modelos de Linguagem (LLMs) permitiu - desenvolvimento
de novas abordagens para automação, dentre as quais se destaca a Geração Aumentada
por Recuperação (RAG). Contudo, sistemas de RAG tradicionais baseados puramente em
vetores muitas vezes falham em capturar as regras de negócio e dependências explícitas
necessárias para um diagnóstico preciso. Este trabalho propõe - desenvolvimento de um
sistema baseado em **GraphRAG**, que integra um Grafo de Conhecimento estruturado no
banco de dados Neo4j com modelos generativos (GPT-4o). O sistema utiliza uma abordagem híbrida, combinando busca vetorial para identificação de similaridade semântica e
travessia de grafos para identificar informações faltantes cruciais (como número de patrimônio, modelo de hardware ou localização) antes de sugerir uma solução. A metodologia
envolveu a estruturação de uma base de conhecimento de incidentes comuns, a ingestão
desses dados em uma instância Neo4j AuraDB e - desenvolvimento de um pipeline de
orquestração em Python. Os resultados indicam que a abordagem aumenta significativamente a completude dos chamados abertos, reduzindo - tempo de interação humana no
primeiro nível de suporte e padronizando - atendimento.


**Palavras-chave:** GraphRAG, Neo4j, Grafo de Conhecimento, Suporte Técnico, LLM,
Inteligência Artificial.


3


## **Abstract**

IT technical support faces constant challenges regarding the efficient triage of tickets and
the resolution of problems that depend on contextual information often omitted by users
in their initial requests. The advancement of Large Language Models (LLMs) has enabled
the development of new approaches for automation, among which Retrieval-Augmented
Generation (RAG) stands out. However, traditional RAG systems based purely on vectors
often fail to capture the business rules and explicit dependencies necessary for an accurate diagnosis. This work proposes the development of a system based on **GraphRAG**,
which integrates a Knowledge Graph structured in the Neo4j database with generative
models (GPT-4o). The system uses a hybrid approach, combining vector search for semantic similarity identification and graph traversal to identify crucial missing information
(such as asset number, hardware model, or location) before suggesting a solution. The
methodology involved structuring a knowledge base of common incidents, ingesting this
data into a Neo4j AuraDB instance, and developing an orchestration pipeline in Python.
The results indicate that the approach significantly increases the completeness of opened
tickets, reducing human interaction time at the first level of support and standardizing
service.


**Keywords:** GraphRAG, Neo4j, Knowledge Graph, Technical Support, LLM, Artificial Intelligence.


4


## **Lista de Figuras**

1 Esquema de modelagem proposto para  - Grafo de Suporte no Neo4j, evidenciando as relações direcionadas. . . . . . . . . . . . . . . . . . . . . . . 14
2 Pipeline de processamento do sistema GraphRAG desenvolvido. . . . . . . 15


5


## **Lista de Tabelas**

1 Comparativo: Banco Relacional vs. Banco de Grafos . . . . . . . . . . . . 13
2 Comparativo: Suporte Humano vs. GraphRAG . . . . . . . . . . . . . . . 25


6


## **Lista de Abreviaturas e Siglas**

**API**   - Application Programming Interface


**GraphRAG**  - Graph-based Retrieval-Augmented Generation


**ITSM**  - IT Service Management


**JSON**  - JavaScript Object Notation


**LLM**  - Large Language Model


**MVP**  - Minimum Viable Product


**NLP**  - Natural Language Processing


**RAG**  - Retrieval-Augmented Generation


**SLA**  - Service Level Agreement


**SQL**  - Structured Query Language


**VPN**  - Virtual Private Network


7


## **Sumário**

**1** **Introdução** **10**

1.1 Problema de Pesquisa . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
1.2 Objetivos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
1.2.1 Objetivo Geral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
1.2.2 Objetivos Específicos . . . . . . . . . . . . . . . . . . . . . . . . . . 10
1.3 Justificativa . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11


**2** **Referencial** **Teórico** **12**

2.1 Grandes Modelos de Linguagem (LLMs) . . . . . . . . . . . . . . . . . . . 12
2.1.1 Mecanismo de Atenção . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.2 Embeddings e Representação Vetorial . . . . . . . . . . . . . . . . . . . . . 12
2.3 Retrieval-Augmented Generation (RAG) . . . . . . . . . . . . . . . . . . . 13
2.4 Grafos de Conhecimento e GraphRAG . . . . . . . . . . . . . . . . . . . . 13
2.4.1 Comparativo de Tecnologias de Banco de Dados . . . . . . . . . . . 13
2.5 Engenharia de Prompt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14


**3** **Materiais** **e** **Métodos** **15**

3.1 Arquitetura do Sistema . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.2 Ferramentas Utilizadas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.3 Estruturação e Ingestão de Dados . . . . . . . . . . . . . . . . . . . . . . . 16
3.4 O Algoritmo de Recuperação (Retrieval) . . . . . . . . . . . . . . . . . . . 17
3.5 Custos e Viabilidade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18


**4** **Resultados** **e** **Discussão** **19**

4.1 Cenário 1: Hardware Crítico . . . . . . . . . . . . . . . . . . . . . . . . . . 19
4.1.1 Caso 1.1: Computador Inoperante . . . . . . . . . . . . . . . . . . . 19
4.1.2 Caso 1.2: Reinicialização Inesperada . . . . . . . . . . . . . . . . . 19
4.2 Cenário 2: Periféricos e Acessórios . . . . . . . . . . . . . . . . . . . . . . . 19
4.2.1 Caso 2.1: Monitor sem Imagem . . . . . . . . . . . . . . . . . . . . 19
4.2.2 Caso 2.2: Teclado Inoperante . . . . . . . . . . . . . . . . . . . . . 20
4.2.3 Caso 2.3: Mouse sem Resposta . . . . . . . . . . . . . . . . . . . . 20
4.2.4 Caso 2.4: Scanner não Reconhecido . . . . . . . . . . . . . . . . . . 20
4.2.5 Caso 2.5: Falha em Projetor . . . . . . . . . . . . . . . . . . . . . . 20
4.3 Cenário 3: Conectividade e Redes . . . . . . . . . . . . . . . . . . . . . . . 21
4.3.1 Caso 3.1: Lentidão de Rede . . . . . . . . . . . . . . . . . . . . . . 21
4.3.2 Caso 3.2: Falha de Conexão Wi-Fi . . . . . . . . . . . . . . . . . . 21
4.3.3 Caso 3.3: Acesso VPN . . . . . . . . . . . . . . . . . . . . . . . . . 21
4.4 Cenário 4: Software e Sistemas Internos . . . . . . . . . . . . . . . . . . . . 22


8


4.4.1 Caso 4.1: Erro de Login . . . . . . . . . . . . . . . . . . . . . . . . 22
4.4.2 Caso 4.2: Erro em Software de Gestão . . . . . . . . . . . . . . . . 22
4.4.3 Caso 4.3: Travamento de Software . . . . . . . . . . . . . . . . . . . 22
4.4.4 Caso 4.4: Envio de E-mails . . . . . . . . . . . . . . . . . . . . . . 22
4.4.5 Caso 4.5: Permissão de Arquivos . . . . . . . . . . . . . . . . . . . 23
4.4.6 Caso 4.6: Falha de Backup . . . . . . . . . . . . . . . . . . . . . . . 23
4.5 Cenário 5: Manutenção de Sistema Operacional . . . . . . . . . . . . . . . 23
4.5.1 Caso 5.1: Lentidão Geral . . . . . . . . . . . . . . . . . . . . . . . . 23
4.5.2 Caso 5.2: Atualização do Windows . . . . . . . . . . . . . . . . . . 23
4.5.3 Caso 5.3: Problemas de Áudio . . . . . . . . . . . . . . . . . . . . . 24
4.5.4 Caso 5.4: Impressão . . . . . . . . . . . . . . . . . . . . . . . . . . 24
4.6 Análise Geral dos Resultados . . . . . . . . . . . . . . . . . . . . . . . . . 24
4.7 Comparativo de Desempenho Qualitativo . . . . . . . . . . . . . . . . . . . 24
4.8 Limitações Identificadas . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25


**5** **Trabalhos** **Futuros** **e** **Continuidade** **26**

5.1 Expansão da Ontologia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
5.2 Interface de Usuário (Frontend) . . . . . . . . . . . . . . . . . . . . . . . . 26
5.3 Aprendizado Contínuo (Feedback Loop) . . . . . . . . . . . . . . . . . . . 26
5.4 Continuidade via Iniciação Científica . . . . . . . . . . . . . . . . . . . . . 27


**6** **Conclusão** **27**


**7** **Referências** **Bibliográficas** **29**


## **1 Introdução**

O avanço dos modelos de linguagem natural (NLP), impulsionado pela arquitetura Transformer e - surgimento dos Grandes Modelos de Linguagem (LLMs), tem permitido desenvolvimento de sistemas inteligentes capazes de auxiliar na resolução de problemas
complexos com uma fluidez sem precedentes. No contexto corporativo, especificamente
no suporte técnico de Tecnologia da Informação (TI), a eficiência operacional é frequentemente prejudicada pela qualidade das informações fornecidas pelos usuários finais.

Muitos chamados não podem ser resolvidos de forma imediata devido à ausência de
informações específicas. Um usuário pode relatar "a internet não funciona", mas para técnico, essa informação é insuficiente sem saber se é uma conexão cabeada ou Wi-Fi, qual

- local do usuário, ou se outros dispositivos estão afetados. O processo tradicional envolve
uma troca de mensagens assíncrona ("ping-pong") para coletar esses dados, consumindo
tempo valioso de SLA (Service Level Agreement).

Este projeto propõe o desenvolvimento de um sistema de **GraphRAG**, que utiliza um
grafo de conhecimento estruturado no Neo4j para fornecer respostas automáticas a esses
chamados. Diferente de chatbots tradicionais baseados apenas em similaridade de texto,

- sistema proposto entende a estrutura do problema: ele sabe que para - problema _X_,
as informações _A_, _B_ e _C_ são obrigatórias, e instrui - modelo de linguagem a solicitá-las
proativamente.

### **1.1 Problema de Pesquisa**


Como automatizar a triagem de incidentes de TI garantindo que - modelo de linguagem
não apenas responda ao usuário, mas siga rigorosamente os procedimentos de coleta de
dados obrigatórios definidos pela organização, minimizando alucinações e incompletude?

### **1.2 Objetivos**


**1.2.1** **Objetivo** **Geral**


Desenvolver um sistema RAG utilizando grafo de conhecimento para responder chamados
que não podem ser resolvidos de imediato, focando na completude da informação no
momento da abertura do ticket.


**1.2.2** **Objetivos** **Específicos**


  - Estruturar a base de conhecimento de problemas comuns de TI em um formato
de grafo adequado para   - Neo4j, modelando as dependências entre problemas e
requisitos de informação.


10


  - Integrar a base de dados em grafo com um sistema de RAG leve e eficiente, utilizando
a API da OpenAI.


  - Implementar algoritmos de busca híbrida que unam  - poder semântico dos embeddings com a precisão determinística dos grafos.


  - Testar  - sistema com cenários reais de chamados de suporte (hardware, software,
redes).


  - Avaliar a efetividade do sistema em fornecer respostas relevantes e solicitar dados
faltantes.

### **1.3 Justificativa**


A escolha por uma arquitetura baseada em Grafos de Conhecimento (Knowledge Graphs)
justifica-se pela limitação dos modelos vetoriais puros. Vetores são excelentes para encontrar similaridade ("impressora"é similar a "xerox"), mas ruins em lógica estruturada ("se
impressora, então preciso do número de série"). O Neo4j, como banco de dados nativo de
grafos, permite modelar essas regras de negócio explicitamente, garantindo que a IA não
alucine procedimentos, mas siga um fluxo de diagnóstico rigoroso.


11


## **2 Referencial Teórico**

Esta seção apresenta os fundamentos teóricos que sustentam - desenvolvimento do sistema, abrangendo desde a evolução dos modelos de linguagem até a aplicação de grafos
de conhecimento.

### **2.1 Grandes Modelos de Linguagem (LLMs)**


A área de Processamento de Linguagem Natural (PLN) passou por uma revolução com
a introdução da arquitetura Transformer por Vaswani et al. (2017). Diferente das Redes Neurais Recorrentes (RNNs) e LSTMs, que processavam texto sequencialmente, os
Transformers utilizam mecanismos de _Self-Attention_ para processar sequências inteiras
simultaneamente.


**2.1.1** **Mecanismo** **de** **Atenção**


O mecanismo de _Scaled_ _Dot-Product_ _Attention_ é a base dos Transformers. Ele permite
que - modelo pondere a importância de diferentes palavras na sentença de entrada ao
gerar uma representação. A fórmula matemática é dada por:



Attention( _Q, K, V_ ) = softmax




- _<u>QK</u>_ _T_
_~~√~~_ _dk_




_V_ (1)



Onde _Q_ (Query), _K_ (Key) e _V_ (Value) são matrizes derivadas da entrada, e _dk_ é a
dimensão das chaves. Essa capacidade de capturar dependências de longo prazo é - que
permite ao GPT-4o entender contextos complexos de um chamado de suporte.

### **2.2 Embeddings e Representação Vetorial**


Para que máquinas processem linguagem, é necessário converter texto em números. Embeddings são representações vetoriais densas onde palavras ou frases com significados
similares ficam próximas no espaço vetorial. Matematicamente, dado um vocabulário _V_,
uma função de embedding _E_ mapeia uma palavra _w_ para um vetor _v_ _∈_ R <sup>_d_</sup> .

A similaridade entre dois textos _A_ e _B_ é frequentemente calculada pelo Cosseno do
ângulo entre os vetores:



_<u>A · B</u>_
sim( _A, B_ ) = cos( _θ_ ) = _∥A∥∥B∥_ <sup>=</sup>




<u>�</u> _n_
_<u>i</u>_ <u>=1</u> <sup>_<u>AiBi</u>_</sup>

~~<u>�</u>~~ <u>�</u> _<u>n</u>_ ~~<u>�</u>~~ <u>�</u>
_i_ =1 <sup>_A_</sup> _i_ <sup>2</sup> _i_



_i_



(2)




~~<u>�</u>~~ <u>�</u> _<u>n</u>_
_i_ =1 <sup>_B_</sup> _i_ <sup>2</sup>



_i_



No presente trabalho, utilizamos  - modelo `text-embedding-3-small` da OpenAI,
que gera vetores de 1536 dimensões. Isso permite que frases como "O PC morreu"e
"Computador não liga"tenham alta similaridade (próxima de 1), enquanto "Impressora
sem papel"teria similaridade baixa.


12


### **2.3 Retrieval-Augmented Generation (RAG)**

Para mitigar as limitações dos LLMs - como alucinação e conhecimento desatualizado
—, Lewis et al. (2020) propuseram a arquitetura RAG. O RAG divide - processo em
duas etapas principais:


1. **Recuperação** **(Retrieval):** Busca em uma base externa os trechos ( _chunks_ ) mais
relevantes para a consulta do usuário.


2. **Geração** **(Generation):** Os trechos recuperados são concatenados ao prompt do
sistema e enviados ao LLM para gerar a resposta final.

### **2.4 Grafos de Conhecimento e GraphRAG**


Enquanto bancos de dados vetoriais (Vector DBs) são excelentes para busca semântica,
eles perdem as relações explícitas entre entidades. Um Grafo de Conhecimento organiza
a informação em nós e arestas, preservando a semântica estrutural.

A integração de RAG com Grafos ( **GraphRAG** ) permite consultas complexas, conhecidas como _multi-hop_ _retrieval_ . Ao invés de apenas buscar "textos sobre erro de
impressora", podemos percorrer - grafo: "Encontre - erro de impressora _E_, navegue até
as soluções _S_ conectadas a ele, e verifique quais informações _I_ são pré-requisitos para _S_ ".


**2.4.1** **Comparativo** **de** **Tecnologias** **de** **Banco** **de** **Dados**


A Tabela 1 compara as abordagens relacionais tradicionais com a abordagem de grafos
utilizada neste projeto.


Tabela 1: Comparativo: Banco Relacional vs. Banco de Grafos


**Característica** **Banco** **Relacional** **(SQL)** **Banco** **de** **Grafos**

**(Neo4j)**


Estrutura Tabelas, Linhas, Colunas Nós, Relacionamentos, Propriedades
Relacionamentos Chaves Estrangeiras (Jo- Arestas diretas ( _Index-free_
ins custosos computacional- _adjacency_ )
mente)

Flexibilidade Esquema rígido Schema-less ou flexível
Modelagem de Problemas Difícil para hierarquias pro- Natural para dependências
fundas e redes e fluxos


13


Figura 1: Esquema de modelagem proposto para - Grafo de Suporte no Neo4j, evidenciando as relações direcionadas.

### **2.5 Engenharia de Prompt**


A qualidade da resposta do LLM depende drasticamente de como a instrução é passada.
A Engenharia de Prompt (Prompt Engineering) envolve técnicas como:


  - **Persona:** Definir quem  - modelo é (ex: "Você é um técnico de TI Sênior").


  - **Few-Shot Learning:** Fornecer exemplos de perguntas e respostas ideais no prompt.


  - **Chain-of-Thought:** Pedir para  - modelo raciocinar passo a passo antes de responder.


Neste trabalho, utilizamos um "System Prompt"robusto que injeta o contexto recuperado
do grafo e instrui - modelo a focar nas informações faltantes.


14


## **3 Materiais e Métodos**

### **3.1 Arquitetura do Sistema**

O sistema foi projetado como uma aplicação modular em Python, executada em nuvem.
A arquitetura segue um fluxo de dados linear com feedback, conforme ilustrado na Figura
2.


1. **Interface** **de** **Entrada:** Recebe a descrição do problema em linguagem natural do
usuário.


2. **Módulo** **de** **Embedding:** Converte a entrada em um vetor denso utilizando a API
da OpenAI.


3. **Motor** **de** **Busca** **Híbrido** **(Neo4j):**


    - Realiza uma busca vetorial (KNN) para encontrar o nó ‘:Problema‘ mais similar
semanticamente.


    - A partir do nó encontrado, realiza uma travessia no grafo para coletar nós
vizinhos de ‘:Solucao‘ e ‘:Informacao‘.


4. **Montagem** **de** **Contexto:** Estrutura os dados recuperados em um formato JSON
ou textual claro.


5. **LLM** **(GPT-4o):** Gera a resposta final ao usuário, solicitando os dados pendentes.







Figura 2: Pipeline de processamento do sistema GraphRAG desenvolvido.

### **3.2 Ferramentas Utilizadas**


  - **Linguagem** **de** **Programação:** Python 3.10+, escolhida pela vasta biblioteca de
suporte a IA e dados.


15


   - **Banco** **de** **Dados:** Neo4j AuraDB (Enterprise Free Tier). O Neo4j foi selecionado
por ser o líder de mercado em bancos de grafos e oferecer algoritmos de similaridade
vetorial nativos ( _Graph_ _Data_ _Science_ _Library_ ).


   - **Driver:** `neo4j` python driver oficial.


   - **LLM** **e** **Embeddings:** OpenAI API.


**–** Modelo Generativo: `gpt-4o-mini` (pelo equilíbrio entre custo e performance).


**–** Modelo de Embedding: `text-embedding-3-small` .


   - **Ambiente** **de** **Desenvolvimento:** Google Colab para prototipagem rápida e validação.

### **3.3 Estruturação e Ingestão de Dados**


A base de conhecimento foi construída a partir de um levantamento de incidentes comuns
em ambientes corporativos (Nível 1). Os dados foram estruturados em uma lista de
dicionários Python, simulando uma base de conhecimento curada.


1 <mark>`problemas_ti`</mark> <mark>`=`</mark> <mark>`[`</mark>


2 <mark>`{`</mark>


3 <mark>`"descricao"`</mark> <mark>`:`</mark> <mark>`"Meu`</mark> <mark>`computador`</mark> <mark>`nao`</mark> <mark>`liga"`</mark> <mark>`,`</mark>


4 <mark>`"solucao"`</mark> <mark>`:`</mark> <mark>`"Verifique`</mark> <mark>`o`</mark> <mark>`cabo`</mark> <mark>`de`</mark> <mark>`energia`</mark> <mark>`e`</mark> <mark>`a`</mark> <mark>`tomada.`</mark> <mark>`Teste`</mark> <mark>`com`</mark>

```
   outro cabo ...",

```

5 <mark>`"informacoes"`</mark> <mark>`:`</mark> <mark>`[`</mark> <mark>`"Numero`</mark> <mark>`do`</mark> <mark>`patrimonio"`</mark> <mark>`,`</mark> <mark>`"Modelo`</mark> <mark>`do`</mark> <mark>`computador"`</mark> <mark>`,`</mark>

```
   "Ultimo local de uso" ]

```

6 <mark>`},`</mark>


7 <mark>`{`</mark>


8 <mark>`"descricao"`</mark> <mark>`:`</mark> <mark>`"A`</mark> <mark>`internet`</mark> <mark>`esta`</mark> <mark>`lenta"`</mark> <mark>`,`</mark>


9 <mark>`"solucao"`</mark> <mark>`:`</mark> <mark>`"Reinicie`</mark> <mark>`o`</mark> <mark>`roteador`</mark> <mark>`e`</mark> <mark>`verifique`</mark> <mark>`dispositivos`</mark>

```
   conectados ...",

```

10 <mark>`"informacoes"`</mark> <mark>`:`</mark> <mark>`[`</mark> <mark>`"Localizacao"`</mark> <mark>`,`</mark> <mark>`"Tipo`</mark> <mark>`de`</mark> <mark>`conexao"`</mark> <mark>`,`</mark> <mark>`"Numero`</mark> <mark>`de`</mark>

```
   usuarios afetados" ]

```

11 <mark>`}`</mark>


12 <mark>`#`</mark> <mark>`...`</mark> <mark>`(outros`</mark> <mark>`18`</mark> <mark>`c e n`</mark> <mark>`r i o s`</mark> <mark>`mapeados)`</mark>


13 <mark>`]`</mark>


Listing 1: Estrutura de Dados dos Problemas (Exemplo)


Para popular   - grafo, desenvolveu-se um script que utiliza a linguagem Cypher. O
uso da cláusula `MERGE` é fundamental, pois garante a idempotência da operação: se  - nó
já existe, ele não é duplicado, apenas atualizado. Isso permite rodar  - script de ingestão
múltiplas vezes sem corromper  - grafo.


1 <mark>`#`</mark> <mark>`Conexao`</mark> <mark>`e`</mark> <mark>`ingestao`</mark>


2 <mark>`with`</mark> <mark>`driver.session ()`</mark> <mark>`as`</mark> <mark>`session:`</mark>


16


3 <mark>`for`</mark> <mark>`item`</mark> <mark>`in`</mark> <mark>`problemas_ti:`</mark>


4 <mark>`#`</mark> <mark>`Gera`</mark> <mark>`o`</mark> <mark>`embedding`</mark> <mark>`da`</mark> <mark>`descricao`</mark>


5 <mark>`embedding`</mark> <mark>`=`</mark> <mark>`gerar_embedding (item[`</mark> <mark>`"descricao"`</mark> <mark>`])`</mark>


6


7 <mark>`#`</mark> <mark>`Executa`</mark> <mark>`a`</mark> <mark>`query`</mark> <mark>`de`</mark> <mark>`criacao`</mark> <mark>`de`</mark> <mark>`nos`</mark> <mark>`e`</mark> <mark>`relacionamentos`</mark>


8 <mark>`session.run(`</mark> <mark>`"""`</mark>


9 <mark>`MERGE`</mark> <mark>`(p:Problema`</mark> <mark>`{descricao:`</mark> <mark>`$descricao })`</mark>


10 <mark>`SET`</mark> <mark>`p.solucao`</mark> <mark>`=`</mark> <mark>`$solucao,`</mark>


11 <mark>`p.embedding`</mark> <mark>`=`</mark> <mark>`$embedding`</mark>


12 <mark>`WITH`</mark> <mark>`p`</mark>


13 <mark>`UNWIND`</mark> <mark>`$infos`</mark> <mark>`AS`</mark> <mark>`info`</mark>


14 <mark>`MERGE`</mark> <mark>`(i:Informacao`</mark> <mark>`{tipo:`</mark> <mark>`info })`</mark>


15 <mark>`MERGE`</mark> <mark>`(p) -[: REQUER_INFORMACAO ]->(i)`</mark>


16 <mark>`"""`</mark> <mark>`,`</mark>


17 <mark>`descricao=item[`</mark> <mark>`"descricao"`</mark> <mark>`],`</mark>


18 <mark>`solucao=item[`</mark> <mark>`"solucao"`</mark> <mark>`],`</mark>


19 <mark>`embedding=embedding,`</mark>


20 <mark>`infos=item[`</mark> <mark>`"informacoes"`</mark> <mark>`])`</mark>


Listing 2: Script de Ingestão no Neo4j

### **3.4 O Algoritmo de Recuperação (Retrieval)**


A recuperação é - componente central do sistema. Diferente de uma busca simples por
palavra-chave ( `CONTAINS` ou `LIKE` ), utiliza-se a similaridade de cosseno. A query Cypher
desenvolvida realiza uma operação em dois estágios:


1. **Busca** **Vetorial:** Compara o vetor da pergunta do usuário com todos os vetores de
problemas armazenados, retornando os top 3 mais similares.


2. **Navegação** **no** **Grafo:** Para cada problema encontrado,    - Neo4j navega pelas
arestas `:REQUER_INFORMACAO` para coletar os nós de informação associados.


1 <mark>`WITH`</mark> <mark>`$embedding`</mark> <mark>`AS`</mark> <mark>`inputEmbedding`</mark>


2 <mark>`MATCH`</mark> <mark>`(p:Problema)`</mark>


3 <mark>`WITH`</mark> <mark>`p,`</mark> <mark>`gds.similarity.cosine(p.embedding,`</mark> <mark>`inputEmbedding )`</mark> <mark>`AS`</mark> <mark>`score`</mark>


4 <mark>`ORDER`</mark> <mark>`BY`</mark> <mark>`score`</mark> <mark>`DESC`</mark>


5 <mark>`LIMIT`</mark> <mark>`3`</mark>


6 <mark>`OPTIONAL`</mark> <mark>`MATCH`</mark> <mark>`(p) -[: REQUER_INFORMACAO ]->(i:Informacao)`</mark>


7 <mark>`RETURN`</mark> <mark>`p.descricao`</mark> <mark>`AS`</mark> <mark>`descricao,`</mark>


8 <mark>`p.solucao`</mark> <mark>`AS`</mark> <mark>`solucao,`</mark>


9 <mark>`collect(i.tipo)`</mark> <mark>`AS`</mark> <mark>`informacoes_faltantes,`</mark>


10 <mark>`score`</mark>


Listing 3: Query de Recuperação Híbrida


17


### **3.5 Custos e Viabilidade**

Para a viabilidade econômica do projeto, considerou-se - custo por token da OpenAI. O
modelo `gpt-4o-mini` apresenta um custo extremamente reduzido ($0.15 / 1M tokens de
entrada), tornando a solução viável mesmo para volumes altos de chamados. O Neo4j
AuraDB possui planos gratuitos para grafos de até 200 mil nós, suficiente para a maioria
das bases de conhecimento de PMEs (Pequenas e Médias Empresas).


18


## **4 Resultados e Discussão**

Nesta seção, apresentamos os resultados obtidos com a execução do sistema GraphRAG
em 20 cenários reais de suporte técnico. Os testes visam validar a capacidade do sistema
em identificar corretamente - problema (via busca vetorial) e solicitar as informações
obrigatórias modeladas no grafo (via travessia de arestas).

Os resultados abaixo representam a saída bruta gerada pelo modelo GPT-4o, instruído
pelo contexto recuperado do Neo4j.

### **4.1 Cenário 1: Hardware Crítico**


Neste grupo, testamos falhas físicas que impedem - uso do equipamento. A prioridade é
identificar - ativo para substituição ou reparo físico.


**4.1.1** **Caso** **1.1:** **Computador** **Inoperante**


**Pergunta** **do** **Usuário:** "Meu computador não liga"


**Resposta** **do** **Sistema:** Verifique  - cabo de energia e a tomada. Teste com outro
cabo e veja se há luzes acendendo no gabinete.

Informações faltantes: Número do patrimônio, Modelo do computador, Último local
de uso.


**4.1.2** **Caso** **1.2:** **Reinicialização** **Inesperada**


**Pergunta** **do** **Usuário:** "O computador reinicia sozinho"


**Resposta** **do** **Sistema:** Solução: Verifique se há superaquecimento, se os drivers
estão atualizados e execute uma verificação de vírus.

Informações faltantes: Modelo do computador, Versão do sistema operacional, Último
local de uso.

### **4.2 Cenário 2: Periféricos e Acessórios**


Problemas em dispositivos externos exigem validação de conexão física antes de qualquer
intervenção de software.


**4.2.1** **Caso** **2.1:** **Monitor** **sem** **Imagem**


**Pergunta** **do** **Usuário:** "O monitor não está mostrando sinal"


19


**Resposta** **do** **Sistema:** Para resolver  - problema do monitor sem sinal, verifique se

- cabo HDMI/VGA está bem conectado e se - monitor está na entrada correta. Teste
outro cabo ou porta.

Informações faltantes: Modelo do monitor, Tipo de conexão usada, Número de patrimônio.


**4.2.2** **Caso** **2.2:** **Teclado** **Inoperante**


**Pergunta** **do** **Usuário:** "O teclado parou de funcionar"


**Resposta** **do** **Sistema:** Solução: Verifique se  - cabo do teclado está corretamente
conectado, teste em outra porta USB ou em outro computador.

Informações faltantes: Número de patrimônio do teclado, Modelo do teclado, Último
local de uso.


**4.2.3** **Caso** **2.3:** **Mouse** **sem** **Resposta**


**Pergunta** **do** **Usuário:** "O mouse não responde"


**Resposta** **do** **Sistema:** Solução: Verifique se  - mouse está conectado corretamente,
teste em outra porta USB ou em outro computador, e certifique-se de que as pilhas (se
for sem fio) estão carregadas.

Informações faltantes: Número do patrimônio, Modelo do mouse, Último local de uso.


**4.2.4** **Caso** **2.4:** **Scanner** **não** **Reconhecido**


**Pergunta** **do** **Usuário:** "O scanner não é reconhecido"


**Resposta** **do** **Sistema:** Solução: Verifique se  - scanner está ligado, conectado ao
computador e se os drivers estão instalados corretamente.

Informações faltantes: Modelo do scanner, Número de patrimônio do scanner, Sistema
operacional do computador.


**4.2.5** **Caso** **2.5:** **Falha** **em** **Projetor**


**Pergunta** **do** **Usuário:** "Não consigo conectar - projetor"


20


**Resposta** **do** **Sistema:** Solução: Verifique se  - projetor está ligado, conectado ao
computador e selecione a entrada correta.

Informações faltantes: Modelo do projetor, Número de patrimônio do projetor.

### **4.3 Cenário 3: Conectividade e Redes**


Questões de rede exigem distinção entre problemas locais (dispositivo) e problemas de
infraestrutura (roteador/VPN).


**4.3.1** **Caso** **3.1:** **Lentidão** **de** **Rede**


**Pergunta** **do** **Usuário:** "A internet está muito lenta"


**Resposta** **do** **Sistema:** Para resolver o problema de internet lenta, por favor, reinicie

- roteador e verifique se há muitos dispositivos conectados. Além disso, teste a velocidade
e veja se há interferência.

Faltam as seguintes informações para abrir um chamado completo:  - Localização  Tipo de conexão (Wi-Fi ou cabo) - Número de usuários afetados


**4.3.2** **Caso** **3.2:** **Falha** **de** **Conexão** **Wi-Fi**


**Pergunta** **do** **Usuário:** "Não consigo conectar no Wi-Fi"


**Resposta** **do** **Sistema:** Para resolver  - problema de conexão no Wi-Fi, sugiro que
você esqueça a rede e tente reconectar digitando a senha novamente. Verifique também
se há restrições no roteador.

Informações faltantes para abrir um chamado completo:  - SSID da rede  - Usuário  Data e hora do erro


**4.3.3** **Caso** **3.3:** **Acesso** **VPN**


**Pergunta** **do** **Usuário:** "Não consigo acessar a VPN"


**Resposta** **do** **Sistema:** Solução: Verifique se suas credenciais estão corretas e tente
reiniciar sua conexão com a VPN. Caso continue, peça um reset de senha ao suporte.

Informações faltantes para abrir um chamado completo: Usuário de login, Sistema
afetado, Horário do erro.


21


### **4.4 Cenário 4: Software e Sistemas Internos**

Erros lógicos, de permissão ou de configuração de software.


**4.4.1** **Caso** **4.1:** **Erro** **de** **Login**


**Pergunta** **do** **Usuário:** "O sistema interno apresenta erro ao fazer login"


**Resposta do Sistema:** Para resolver o erro ao fazer login no sistema interno, verifique
se suas credenciais estão corretas e se a VPN está ativa. Caso o problema persista, solicite
um reset de senha ao suporte.

Informações faltantes para abrir um chamado completo:  - Usuário de login  - Sistema
afetado - Horário do erro


**4.4.2** **Caso** **4.2:** **Erro** **em** **Software** **de** **Gestão**


**Pergunta** **do** **Usuário:** "Erro ao abrir - software de gestão"


**Resposta** **do** **Sistema:** Solução: Verifique se as credenciais estão corretas e se a
VPN está ativa. Caso continue, solicite reset de senha ao suporte.

Informações faltantes: Usuário de login, Sistema afetado, Horário do erro.


**4.4.3** **Caso** **4.3:** **Travamento** **de** **Software**


**Pergunta** **do** **Usuário:** "O software trava ao iniciar"


**Resposta** **do** **Sistema:** Solução: Tente iniciar o software em modo seguro e verifique
se há atualizações disponíveis. Se - problema persistir, pode ser necessário reinstalar software.

Informações faltantes: Nome do software, Mensagem de erro apresentada (se houver),
Versão do software, Sistema operacional em uso.


**4.4.4** **Caso** **4.4:** **Envio** **de** **E-mails**


**Pergunta** **do** **Usuário:** "Não consigo enviar e-mails"


**Resposta** **do** **Sistema:** Solução: Verifique sua conexão com a internet e se o servidor
de e-mail está fora do ar. Caso - problema persista, reinicie - aplicativo de e-mail.

Informações faltantes: Endereço de e-mail, horário do erro, mensagem de erro recebida.


22


**4.4.5** **Caso** **4.5:** **Permissão** **de** **Arquivos**


**Pergunta** **do** **Usuário:** "Erro de permissão ao salvar arquivos"


**Resposta do Sistema:** Solução: Verifique as permissões da pasta onde está tentando
salvar os arquivos e certifique-se de que possui as permissões necessárias.

Informações faltantes: Usuário, Caminho da pasta, Tipo de arquivo que está sendo
salvo, Data e hora do erro.


**4.4.6** **Caso** **4.6:** **Falha** **de** **Backup**


**Pergunta** **do** **Usuário:** "O backup não completou"


**Resposta** **do** **Sistema:** Solução: Verifique os logs do backup para identificar o erro e
tente reiniciar o serviço de backup. Se persistir, considere reconfigurar a tarefa de backup.

Informações faltantes: Código do erro, Data e hora da falha, Método de backup utilizado.

### **4.5 Cenário 5: Manutenção de Sistema Operacional**


**4.5.1** **Caso** **5.1:** **Lentidão** **Geral**


**Pergunta** **do** **Usuário:** "Meu computador está muito lento"


**Resposta** **do** **Sistema:** Para resolver o problema do seu computador lento, recomendamos limpar arquivos temporários, desativar inicializações automáticas e verificar se disco está quase cheio.

Informações faltantes para abrir um chamado completo: uso de disco, memória RAM
disponível, versão do sistema operacional.


**4.5.2** **Caso** **5.2:** **Atualização** **do** **Windows**


**Pergunta** **do** **Usuário:** "Falha ao atualizar - Windows"


**Resposta** **do** **Sistema:** Solução: Execute  - solucionador de problemas do Windows
Update e reinicie - sistema. Se persistir, atualize manualmente.

Informações faltantes para abrir um chamado completo:  - Versão atual do Windows  Código do erro - Data da última atualização bem-sucedida


23


**4.5.3** **Caso** **5.3:** **Problemas** **de** **Áudio**


**Pergunta** **do** **Usuário:** "O áudio não funciona"


**Resposta** **do** **Sistema:** Solução: Verifique se  - volume está ativado, se  - dispositivo
de saída de áudio está selecionado corretamente e se os cabos de áudio estão conectados.

Informações faltantes: Número do patrimônio, Modelo do computador, Sistema operacional, Tipo de conexão de áudio usada.


**4.5.4** **Caso** **5.4:** **Impressão**


**Pergunta** **do** **Usuário:** "Não consigo imprimir documentos"


**Resposta** **do** **Sistema:** Para resolver  - problema de impressão, por favor, verifique
se a impressora está ligada, conectada ao computador e se há papel e tinta suficientes.

Informações faltantes para abrir um chamado completo:  - Modelo da impressora  Número de patrimônio da impressora

### **4.6 Análise Geral dos Resultados**


A consistência observada nas respostas demonstra que o modelo LLM aderiu estritamente
às instruções injetadas pelo grafo. Em todos os casos, a "Solução"sugerida foi a paliativa
(Nível 0) e as "Informações Faltantes"foram exatamente aquelas modeladas nas arestas
`:REQUER_INFORMACAO` do Neo4j. Isso valida a hipótese de que - GraphRAG pode atuar
como um filtro eficaz de triagem, garantindo que nenhum ticket seja escalado para um
humano sem os dados mínimos necessários (patrimônio, usuário, erro específico).

### **4.7 Comparativo de Desempenho Qualitativo**


A Tabela 2 apresenta um resumo comparativo entre - atendimento humano tradicional
de Nível 1 e - sistema automatizado proposto.


24


Tabela 2: Comparativo: Suporte Humano vs. GraphRAG



|Critério|Suporte Humano (N1)|Sistema GraphRAG|
|---|---|---|
|Tempo de Resposta|10 min - 4 horas (depen-<br>dendo da fla)|< 5 segundos|
|Padronização|Variável (depende do trei-<br>namento do atendente)|Totalmente<br>padronizado<br>(segue o grafo)|
|Coleta de Dados|Frequentemente esquece da-<br>dos obrigatórios|Segue estritamente as ares-<br>tas do grafo|
|Escalabilidade|Linear<br>(precisa<br>contratar<br>mais pessoas)|Exponencial (custo margi-<br>nal baixo)|
|Disponibilidade|Horário<br>comercial<br>(geral-<br>mente)|24/7|

### **4.8 Limitações Identificadas**





Apesar dos resultados positivos, algumas limitações foram observadas:


  - **Dependência** **da** **Base:** Se  - nó no Neo4j contiver uma solução desatualizada,  sistema a propagará. Isso exige um processo de curadoria contínua.


  - **Ambiguidade** **Semântica:** Frases muito curtas ou gírias regionais podem ter embeddings que não se alinham perfeitamente aos descritores técnicos, exigindo um
fine-tuning do modelo de embedding ou expansão dos sinônimos no grafo.


25


## **5 Trabalhos Futuros e Continuidade**

O presente trabalho estabelece uma base sólida para a automação de suporte via GraphRAG, validando a eficácia da estruturação de conhecimento para a triagem de chamados.
No entanto, o campo oferece diversas avenidas de pesquisa para a evolução deste sistema,
tanto em nível de engenharia de software quanto em pesquisa acadêmica aplicada.

### **5.1 Expansão da Ontologia**


Atualmente, - grafo possui apenas três tipos de nós principais ( `:Problema`, `:Solucao`,
`:Informacao` ). Futuros trabalhos podem expandir a ontologia para capturar a complexidade organizacional, incluindo nós de:


  - `:Departamento` : Para roteamento automático de chamados (ex: separar tickets de
RH, Financeiro e TI).


  - `:SLA` : Para definir níveis de urgência automaticamente baseados no tipo de problema.


  - `:Especialista` : Para sugerir qual técnico ou grupo resolbedor é mais adequado
para   - ticket.

### **5.2 Interface de Usuário (Frontend)**


O MVP atual opera via notebooks e terminal. O desenvolvimento de um chatbot web (utilizando frameworks como Streamlit ou React) ou uma integração nativa com plataformas
de comunicação corporativa (como Slack ou Microsoft Teams) aumentaria a usabilidade.
Isso permitiria a realização de testes com usuários finais reais (Teste Beta) para validar a
experiência de uso (UX) e a clareza das perguntas formuladas pelo bot.

### **5.3 Aprendizado Contínuo (Feedback Loop)**


Implementar um mecanismo de feedback explícito onde, se a solução sugerida não resolver

- problema, o usuário possa sinalizar (ex: botão de "não funcionou"). Esse sinal negativo
poderia ser utilizado para:


1. Re-ponderar as arestas do grafo, diminuindo a relevância de soluções ineficazes.


2. Alertar um curador humano para revisar a base de conhecimento.


3. Criar um dataset de "casos de falha"para retreinar  - modelo de embedding.


26


### **5.4 Continuidade via Iniciação Científica**

Como desdobramento direto deste trabalho, iniciou-se um projeto de Iniciação Científica
(IC) intitulado **"Desenvolvimento** **de** **um** **Modelo** **de** **Resposta** **Automática** **para**

**Coleta** **de** **Informações** **Faltantes** **em** **Chamados** **de** **Suporte** **Técnico** **Usando**

**Machine** **Learning"** .

Enquanto este TCC focou na estruturação determinística do conhecimento via Grafos, a IC visa avançar para modelos probabilísticos que aprendam com - histórico de
interações. O objetivo geral é desenvolver um modelo de _Machine_ _Learning_ capaz de
identificar dinamicamente lacunas informacionais em novos chamados, facilitando o início
do atendimento.

Os objetivos específicos definidos para esta etapa de continuidade incluem:


  - **Revisão Bibliográfica em NLP:** Investigação aprofundada sobre técnicas de Processamento de Linguagem Natural e arquiteturas de chatbots focadas em detecção
de ambiguidade e preenchimento de slots ( _slot_ _filling_ ).


  - **Curadoria** **e** **Ética** **de** **Dados:** Coleta e pré-processamento de dados anônimos de
chamados históricos, garantindo a aplicação de técnicas rigorosas de anonimização
para conformidade ética e proteção de privacidade.


  - **Modelagem** **com** **Transformers:** Treinamento e avaliação de modelos de IA conversacional (como BERT ou GPT fine-tuned) especificamente para a tarefa de gerar
perguntas de sondagem ( _probing_ _questions_ ) quando detectarem dados faltantes.


  - **Análise de Desempenho:** Avaliação do impacto real na agilidade do atendimento,
medindo métricas como precisão na detecção da lacuna e redução no tempo total
de resolução (TTR).


Essa abordagem híbrida — unindo a confiabilidade do Grafo de Conhecimento (TCC)
com a adaptabilidade do Machine Learning (IC) - representa - estado da arte na automação de suporte técnico.

## **6 Conclusão**


O desenvolvimento do sistema GraphRAG demonstrou a viabilidade e a eficácia de combinar Grafos de Conhecimento com Modelos de Linguagem para o domínio de suporte técnico. A principal hipótese do trabalho — de que a estruturação explícita do conhecimento
melhora a completude dos chamados - foi validada pelos estudos de caso apresentados.

Enquanto a IA Generativa pura impressiona pela fluência, é a estrutura do grafo
que confere a confiabilidade necessária para processos empresariais críticos. Ao forçar a
solicitação de dados como "patrimônio"e "modelo", - sistema atua não apenas como um


27


chatbot, mas como um analista de suporte júnior diligente, filtrando o ruído antes que ele
chegue aos especialistas humanos.

Conclui-se que  - uso de GraphRAG representa uma evolução natural para sistemas
de ITSM, reduzindo custos operacionais, melhorando a experiência do usuário através de
respostas instantâneas e garantindo que, quando um humano precisar intervir, ele tenha
todas as informações necessárias à mão para uma resolução rápida.


28


## **7 Referências Bibliográficas**

ARAI, K. **Design** **of** **On-Premises** **Version** **of** **RAG** **with** **AI** **Agent** **for** **Fra-**

**mework** **Selection** **Together** **with** **Dify** **and** **DSL** **as** **Well** **as** **Ollama** **for**

**LLM** . The SAI Organization, 2025.


BROWN, T. B. et al. **Language** **Models** **are** **Few-Shot** **Learners** . NeurIPS,
2020.


HAIGHT, C. **AI** **Agents** **Will** **Transform** **Enterprise** **IT** **Operations** . Gartner
Research, 2024.


HOMAYOUN, S. **Building** **Knowledge** **Graphs** **using** **Neo4j** **and** **OpenAI** .
Medium, 2023. Disponível em: `[https://homayounsrp.medium.com/building-a](https://homayounsrp.medium.com/building-a-knowledge-graph-for-rag-using-neo4j-e69d3441d843)`
`[-knowledge-graph-for-rag-using-neo4j-e69d3441d843](https://homayounsrp.medium.com/building-a-knowledge-graph-for-rag-using-neo4j-e69d3441d843)` .


LEWIS, P. et al. **Retrieval-Augmented Generation for Knowledge-Intensive**
**NLP** **Tasks** . NeurIPS, 2020.


NEO4J. **Graph** **Data** **Science** **Library** **Documentation** . 2025. Disponível em:
`[https://neo4j.com/docs/graph-data-science/](https://neo4j.com/docs/graph-data-science/)` .


STEWART, D. **Bring** **Knowledge** **and** **Trust** **to** **Generative** **AI** **with** **Graph-**
**RAG** . Gartner Research, 2024.


VASWANI, A. et al. **Attention** **Is** **All** **You** **Need** . In: Advances in Neural
Information Processing Systems, 2017.


29


