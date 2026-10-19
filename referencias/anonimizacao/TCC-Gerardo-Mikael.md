## **Fundação Getulio Vargas** Escola de Matemática Aplicada Ciência de Dados e Inteligência Artificial Gerardo Mikael do Carmo Pereira

# **Anonimização dos Microdados do Enem Através de** **Geração de Dados Sintéticos**

## Trabalho de conclusão de curso

Orientador: Júlio César Chaves


**RIO** **DE JANEIRO**

**2025**


# **1 Introdução**

A Lei Geral de Proteção de Dados (LGPD), ou Lei nº 13.709/2018, é a lei brasileira
aprovada em 2018 criada para garantir a privacidade e a segurança das informações
pessoais dos cidadãos brasileiros. Ela estabelece regras claras sobre como dados pessoais podem ser coletados, armazenados e utilizados, sendo relevante em diversos
contextos, um deles a divulgação de dados educacionais. O Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), disponibiliza os microdados
do ENEM com o objetivo de fomentar pesquisas e análises sobre a educação no país,
ao mesmo tempo cumpre a LGPD assegurando que nenhuma informação permita a
identificação dos participantes.


Para proteger a identidade dos candidatos, - INEP aplica técnicas de anonimização
nos dados divulgados, sendo as principais abordagens k-anonimato, agrupamento e
remoção de certas variáveis. Essas decisões foram tomadas após a aprovação da LGPD
ao longo dos últimos anos, assim a base de dados vem sendo alterada visando garantir
a incapacidade de reidentificação de qualquer indivíduo presente nela.


No entanto, essa proteção muitas vezes vem acompanhada de perda de valor analítico, o que pode dificultar análises mais profundas por pesquisadores independentes,
jornalistas ou cidadãos interessados em entender melhor a situação educacional brasileira, visto que é necessário um processo longo e burocrático (com razão) para acesso
completo dos dados. Diante dessas limitações, surge a iniciativa deste projeto que
busca melhorar a utilidade dos dados anonimizados sem comprometer a privacidade
dos indivíduos.


Este relatório se refere aos processos iniciais da elaboração do trabalho de conclusão
de curso sobre o desenvolvimento de métodos complementares de anonimização, com
a geração de dados sintéticos a partir de algoritmos derivados do SMOTE, que visam
preservar a estrutura estatística dos dados reais enquanto mantêm a proteção dos dados pessoais. A abordagem pode ajudar a tornar os dados públicos mais acessíveis e
informativos, ampliando as possibilidades de participação cidadã e de produção de
conhecimento sobre a educação no Brasil.

# **2 Metodologia**


O SMOTE ou _Synthetic_ _Minority_ _Over-sampling_ _Technique_ é uma técnica de préprocessamento aplicada em bases de dados com desbalanceamento de classes em problemas de classificação supervisionada. Para esse tipo de problemas há predominância de instâncias de determinadas classes em detrimento de certa classe minoritária,

- método em questão consiste em gerar novos pontos sintéticos da classe minoritária
a partir da interpolação entre amostras reais e seus vizinhos mais próximos, ampliando o número de registros dessa classe e aprimorando o desempenho do modelo de
classificação.


Neste trabalho, utilizamos uma variação do SMOTE que também se baseia nos vizinhos para gerar novos dados, mas que difere do método original por replicar toda
a base de dados de forma sintética gerando uma nova base de dados. Assim, cada
registro da nova tabela é criado a partir de combinações interpoladas de dados reais,


2


preservando a distribuição das variáveis e as correlações observadas. Dessa forma,
tem-se como objetivo manter - valor analítico da base, ao mesmo tempo em que se
garante o anonimato dos indivíduos originais.

## **2.1 Base de dados escolhida**


A aplicação dessa variação do SMOTE requer uma base com estrutura suficientemente
rica para preservar relações estatísticas significativas. As bases de dados escolhidas
para a análise serão os microdados do Enem disponibilizados anualmente pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP). A base
conta com - menor nível de desagregação de dados recolhidos por meio do exame
atendendo a demanda por informações específicas ao disponibilizar as provas, os gabaritos, as informações sobre os itens, as notas e - questionário socioeconômico respondido pelos inscritos no Enem.


Os dados disponibilizados compreendem as seguintes categorias:


**Informações do Participante**


Dados cadastrais e de identificação indireta dos candidatos:


 - Número de inscrição


 - Ano de aplicação do ENEM


 - Faixa etária (substitui a idade exata)


 - Sexo


 - Estado civil


 - Cor/raça (autodeclarada)


 - Nacionalidade


 - Situação de conclusão do ensino médio


 - Ano de conclusão do ensino médio


 - Tipo de escola (pública/privada)


 - Tipo de instituição em que concluiu ou concluirá o ensino médio


 - Indicador de “treineiro” (Se está participando do enem apenas para treinamento
com notas não válidas para ingressar na faculdade)


**Informações da Escola**


Dados gerais da escola declarada na inscrição:


 - Código do município da escola


 - Nome do município da escola


 - Código e sigla da UF da escola


 - Dependência administrativa da escola


3


 - Localização (urbana ou rural)


 - Situação de funcionamento da escola


**Informações do Local de Aplicação da Prova**


 - Código e nome do município de aplicação


 - Código e sigla da UF de aplicação


**Informações das Provas Objetivas**


 - Presença nas provas (Ciências da Natureza, Ciências Humanas, Linguagens e
Códigos, Matemática)


 - Tipo de prova aplicada (A cor do caderno que diferencia a ordem que as questões
aparecem)


 - Nota obtida em cada área


 - Vetor de respostas do participante (sequência de itens de A, B, C, D ou E assimilados pelo participante em cada questão)


 - Opção de língua estrangeira


 - Gabarito oficial por área (sequência de itens de A, B, C, D ou E corretos para cada
questão)


**Informações da Redação**


 - Situação da redação (ex: corrigida, anulada)


 - Nota da redação (total e por competências 1 a 5)


**Informações do Questionário Socioeconômico**


 - Respostas às 25 questões do questionário (ex: renda, escolaridade dos pais, posse
de bens, transporte, acesso à internet, entre outros)


**Quasi-identificadores na Base**


Embora a base pública do ENEM não contenha identificadores diretos, como nome
ou CPF, ela apresenta diversas variáveis que, quando combinadas, podem permitir a reidentificação de indivíduos. Essas variáveis são conhecidas como quasiidentificadores, pois descrevem características demográficas, geográficas ou institucionais suficientemente específicas para distinguir indivíduos em subconjuntos da população.


As seguintes variáveis da base de dados são consideradas quasi-identificadoras:


 - Faixa etária: embora agrupada, pode restringir significativamente  - grupo de
comparação;


 - Sexo;


4


 - Estado civil;


 - Cor/raça (autodeclarada);


 - Nacionalidade;


 - Ano de conclusão do ensino médio;


 - Tipo de escola (pública ou privada);


 - Tipo de instituição de conclusão do ensino médio;


 - Código e nome do município de aplicação da prova;


 - UF da escola e UF de aplicação;


 - Dependência administrativa da escola;


 - Localização da escola (urbana ou rural);


 - Situação de funcionamento da escola.


Essas variáveis, mesmo isoladamente inofensivas, podem ser combinadas com dados
externos como cadastros municipais, registros escolares ou redes sociais, para gerar
riscos de reidentificação. Diante desse risco, tornou-se imperativo que - tratamento
dos dados siga as diretrizes estabelecidas pela LGPD. Na seção a seguir, detalham-se
as medidas específicas adotadas pelo INEP para adequar os microdados a essa realidade normativa.

## **2.2 Adequação da base à LGPD**


Os Microdados do Enem tem dados recolhidos desde as provas de 1998, porém a partir de 2018 após a aprovação da LGPD e com base no Relatório de Impacto à Proteção
de Dados Pessoais (RIPD) do INEP, diversas medidas foram adotadas para minimizar o risco de reidentificação dos participantes do ENEM, em conformidade com a lei
aprovada. A criação de um novo modelo de microdados com nível reduzido de detalhamento de forma a priorizar variáveis relevantes para pesquisa, excluindo as que
elevam o risco de identificação foi essencial para se adequar as novas medidas.


Assim, a partir de 2018 os microdados vêm sofrendo atualizações para se adequar a
essas novas regras. Abaixo, seguem as principais mudanças desde então:


 - CO_ESCOLA (código da escola) foi removido, por permitir que gestores escolares identificassem alunos.


 - Idade foi substituída por faixas etárias, reduzindo  - risco de identificação por
combinação com outros dados.


 - Municípios de nascimento e residência foram excluídos mantendo apenas o município de aplicação da prova.


 - Informações de atendimento especializado e específico foram excluídas por serem altamente sensíveis.


 - Cor/raça foi mantida, mas justificada como não representando alto risco de identificação.


5


 - Variáveis que agregavam pouco valor às análises, mas aumentavam o risco, foram descartadas.


Como resultado disso temos grandes trechos na bases de dados que estão ocultos, mas
que representavam anteriormente variáveis relacionadas à escola que o aluno frequentava no ano de sua participação. Isso se deve a iniciativa de k-anonimização onde em
qualquer caso que não haja pelo menos k alunos com dados semelhantes haverá a
ocultação do dado. Como consequência disso temos boa parte dos dados incompletos
quando lidamos com a escola do aluno participante.


Figura 1: Exemplo de trecho com dados relacionados à escola do aluno participante
faltantes


Esta é apenas uma das medidas tomadas para a execução da plena disponibilidade pública desses dados. É notável que aplicação de técnicas tradicionais de anonimização,
como a supressão de colunas e a generalização de valores, gera um impacto negativo
direto na qualidade da pesquisa científica que se utiliza apenas dos dados públicos.
Como observado no relatório do INEP, a tentativa de se adequar à LGPD resultou na
ocultação de quase 70% das variáveis escolares, o que acaba dificultando análises socioeconômicas profundas. Murthy em ’A Comparative Study of Data Anonymization
Techniques’ destaca que esse dilema de ’privacidade-utilidade’ é um desafio central
onde, quanto maior a segurança aplicada, menor - valor analítico restante. A proposta deste TCC, fundamentada na geração de dados sintéticos via SMOTE, busca
subverter essa lógica ao criar uma nova base que não contém indivíduos reais, mas
preserva a utilidade estatística necessária para a produção de conhecimento. Dessa
forma, busca-se um equilíbrio onde a proteção do cidadão não signifique o cegamento
da gestão pública e acadêmica.


Assim, diante da indisponibilidade legal dos microdados completos do ENEM, este
trabalho propõe seus testes e validações a partir da base pública já com as medidas de
adequação aplicadas disponibilizada publicamente pelo INEP. Apesar das transformações como a substituição de identificadores diretos, a agregação de faixas etárias e
a exclusão de variáveis sensíveis, a base ainda mantém estrutura estatística suficiente
para permitir análises informativas e a reconstrução parcial de perfis. Será realizada
então a aplicação de técnicas de geração de dados sintéticos e a avaliação da preserva

6


ção de propriedades analíticas relevantes.

## **2.3 Metodologia de Geração de Dados Sintéticos**


A geração da base sintética utiliza uma adaptação do algoritmo SMOTE-NC (Synthetic
Minority Over-sampling Technique for Nominal and Continuous). O processo baseiase na identificação de vizinhos próximos no espaço numérico normalizado e na aplicação de transformações estocásticas controladas para replicar a totalidade da base
original ( _Nsint_ = _Nreal_ ).


**Vizinhança e Distância** Para cada instância real _xi_, identifica-se um conjunto de _K_ =
5 vizinhos mais próximos através de uma busca em _Ball Tree_ . A métrica de distância
utiliza o vetor de características numéricas escalonadas ( _z_ ):



_d_ ( _xi_, _xj_ ) =




- _n_
# ∑

_k_ =1



( _zi_, _k −_ _zj_, _k_ ) <sup>2</sup>



Para lidar com a natureza híbrida da base, a seleção de vizinhos é penalizada pela variação das variáveis nominais, conforme a lógica do SMOTE-NC, utilizando a mediana
dos desvios padrão numéricos para equilibrar as escalas.


**Interpolação Numérica com** **_Jittering_** **(ruído)** A geração de atributos numéricos sintéticos ( _xsint_, _j_ ) ocorre via interpolação linear. Para mitigar o acúmulo artificial de densidade em torno das médias e melhorar a generalização, foi introduzido um termo de
ruído gaussiano ( _jittering_ ):


_xsint_, _j_ = _xorig_, _j_ + _λ ·_ ( _xviz_, _j −_ _xorig_, _j_ ) + _ϵ_


Onde _λ ∼_ _U_ (0, 1) representa o fator de interpolação e _ϵ ∼_ _N_ (0, _σ_ <sup>2</sup> ) é o ruído estatístico
aplicado para expandir a cobertura do espaço de características e reduzir riscos de
reidentificação por redundância.


**Tratamento de Variáveis Categóricas** A preservação da distribuição local das variáveis nominais é garantida por uma máscara binária estocástica. Para cada atributo
categórico _ck_, o valor sintético é definido pela amostragem entre o registro de referência e seu vizinho:



_csint_, _k_ =




_corig_, _k_, se _p <_ 0, 5
_cviz_, _k_, se _p ≥_ 0, 5


## **2.4 Avaliação: Qualidade Analítica e Garantia de Privacidade**

A avaliação do método de geração sintética será feita com foco em dois critérios centrais: a equivalência analítica e a garantia de anonimização.


7


**Equivalência Analítica**


Para validar que os dados sintéticos mantêm o valor estatístico da base original, serão
aplicadas as seguintes análises:


 - Comparação das distribuições marginais e condicionais entre variáveis reais e
sintéticas;


 - Análise de Componentes Principais (PCA) para verificar preservação da estrutura multivariada;


 - Testes estatísticos replicados em ambas as bases.


**Garantia de privacidade**


A privacidade dos dados será avaliada por meio de:


 - Medição da distância mínima entre registros reais e seus vizinhos sintéticos;


 - Simulações de ataques de linkage para verificar a possibilidade de reidentificação;


Essas estratégias visam demonstrar que é possível gerar dados sintéticos úteis para
análise estatística sem violar os princípios da LGPD.

# **3 Testes e Resultados**

## **3.1 Avaliação do Algoritmo, Teste Inicial: Análise dos Dados do To-** **cantins**


Para reduzir o tempo de processamento e obter resultados preliminares, será utilizado
um recorte da base de dados correspondente a um único estado, o Tocantins.


Adicionalmente, serão realizadas modificações na base com foco nas variáveis de
maior relevância analítica. Algumas variáveis serão explicitamente excluídas ou tratadas com precaução durante o processo, conforme descrito a seguir:


 - **Variáveis excluídas** :


**–** `CO_ESCOLA` (Código da escola);


**–** Município de nascimento e residência;


**–** Informações de atendimento especializado;


**–** Identificadores únicos ou pseudonimizados (e.g. número de inscrição).


 - **Variáveis transformadas** :


**–** Pontuação socioeconômica — indicador numérico de 0 a 10 que sintetiza as

25 questões do questionário socioeconômico, representando o nível geral de
condição socioeconômica do participante.


8


O modelo trabalha apenas sobre variáveis consideradas quasi-identificadoras ou analíticamente úteis para casos de estudos, de forma a não comprometer a identidade dos
participantes, mas preservam a estrutura útil da base de dados.

## **3.2 Resultados Preliminares**


Foram gerados um total de 32.618 instâncias de dados a partir da mesma quantidade
de dados originais. O código utilizado define uma métrica de distância mista capaz
de lidar simultaneamente com atributos numéricos e categóricos.


Antes da geração, definimos explicitamente quais colunas são numéricas e quais são
categóricas, - que determina - comportamento da distância e da interpolação. Também tratamos ausências com média para numéricos e moda para categóricos, garantindo consistência dos valores de entrada.


Dessa forma o teste inicial devolveu os seguintes resultados:


Figura 2: Gráfico de Estimativa de Densidade por Kernel das variáveis numéricas dados de Tocantins


9


Figura 3: Exemplos gráficos de distribuição de algumas das variáveis nominais - dados
de Tocantins


Em relação às variáveis numéricas, observa-se nos dados sintéticos uma concentração anormal de instâncias nas proximidades da média de algumas distribuições, indicando um comportamento que deverá ser investigado e aprimorado em etapas posteriores. Por outro lado, nas variáveis categóricas, verifica-se uma correspondência
bastante próxima entre as distribuições do conjunto sintético e do conjunto original
para todas as variáveis estatisticamente relevantes e não aleatórias.


Embora os resultados obtidos com - recorte do Tocantins forneçam indícios positivos sobre a preservação das variáveis categóricas, - caráter exploratório dessa etapa
serviu primordialmente para validar o pipeline de processamento e a métrica de distância. Contudo, para testar a robustez do algoritmo frente a um volume de dados
significativamente maior e verificar se as anomalias de densidade se mantêm ou se
intensificam, torna-se necessária uma avaliação em base ampliada. Para isso, a seção
seguinte replica - experimento utilizando os microdados do estado de São Paulo, maior contingente da base nacional.


10


## **3.3 Avaliação do Algoritmo em Base Ampliada: Análise dos Dados** **do Estado de São Paulo**

De forma semelhante ao procedimento adotado na análise dos dados do Tocantins, o
experimento em base ampliada concentra-se nas variáveis estatisticamente relevantes
para os objetivos analíticos do estudo. Para isso, são mantidos os mesmos critérios de
seleção, exclusão e transformação de atributos, priorizando variáveis com potencial
informativo e de quasi-identificadores.

## **3.4 Resultados da Avaliação**


Desta vez foram gerados pelo algorítmo 590.767 instâncias sintéticas a partir dos dados do estado de São Paulo. A Figura 4 apresenta as estimativas de densidade por
kernel para algumas das variáveis numéricas, comparando as distribuições dos dados
originais e sintéticos.


**3.4.1** **Equivalência Analítica**


**Densidades dos Parâmetros Numéricos**


Figura 4


Observa-se que o comportamento anômalo identificado no teste preliminar volta a se
manifestar, com uma concentração excessiva de instâncias sintéticas nas proximidades da média de determinadas distribuições. Esse padrão sugere uma tendência do
algoritmo em privilegiar regiões de maior densidade do espaço amostral durante processo de interpolação, efeito que se torna mais pronunciado à medida que - volume de dados aumenta.


Tentativas exploratórias de diminuir desse acúmulo, por meio do aumento do ruído,
ou com mudanças na lógica de escolha dos vizinhos para a supressão ou suavização
das regiões centrais das distribuições, resultaram no surgimento de novas anomalias,
em especial uma concentração artificial de valores próximos de zero em algumas variáveis. Portanto, o acúmulo observado não decorre de um erro pontual de implemen

11


tação, mas de uma propriedade estrutural do método de interpolação adotado, a qual
deve ser considerada na interpretação dos resultados.


**Correlações dos Parâmetros Numéricos**


Figura 5


A Figura 5 apresenta as matrizes de correlação entre os parâmetros numéricos calculadas a partir dos dados originais e dos dados sintéticos. Observa-se uma forte similaridade entre os padrões de correlação dos dois conjuntos, indicando que as relações
lineares entre as variáveis foram amplamente preservadas pelo processo de geração
sintética, mesmo diante das distorções observadas em algumas distribuições marginais.


A comparação quantitativa dos coeficientes mostra que o erro médio absoluto entre as
correlações reais e sintéticas é da ordem de 0,02, com variações pontuais de pequena
magnitude. Esse resultado sugere que a estrutura multivariada subjacente foi mantida
de forma consistente, reforçando a adequação do método para análises exploratórias
e estudos preliminares em contextos nos quais - acesso aos microdados originais é
restrito.


12


**Densidades dos Parâmetros Nominais**


Figura 6


As distribuições das variáveis nominais nos dados sintéticos reproduzem de forma
bastante próxima as proporções observadas no conjunto original, com apenas variações pontuais de pequena magnitude em categorias menos frequentes, - que não
compromete a utilidade analítica do conjunto gerado.


Para validar se a base sintética gerada é de fato representativa e útil, não basta apenas
comparar médias isoladas; é necessário garantir que a estrutura multivariada dos dados originais foi mantida. Conforme proposto por Snoke a avaliação da utilidade geral
pode ser realizada através do Propensity Score Mean-Squared Error (pMSE). Esta métrica utiliza um modelo de aprendizado de máquina, como a regressão logística, para
tentar distinguir quais registros pertencem à base real e quais pertencem à base sintética. Se o modelo não conseguir realizar essa separação com precisão (resultando em
um pMSE próximo de zero), conclui-se que os dados sintéticos são estatisticamente
indistinguíveis dos reais para fins de pesquisa. Esta abordagem confere um rigor matemático ao projeto, provando que a anonimização não comprometeu a veracidade
das correlações educacionais observadas.


13


**Variância acumulada por componentes principais**


Figura 7


Observa-se que uma fração significativa da variância dos dados originais é explicada
por um número reduzido de componentes principais, evidenciando a presença de uma
estrutura latente de baixa dimensionalidade. Em particular, a primeira componente
principal (PC1) concentra aproximadamente 59% da variância total, enquanto a inclusão sucessiva de PC2, PC3 e PC4 eleva esse percentual para cerca de 73%, 83% e
91%, respectivamente. A partir desse ponto, os ganhos marginais tornam-se pouco
expressivos, indicando que a maior parte da informação relevante dos microdados do
ENEM já é capturada por poucas direções dominantes, - que sugere a existência de
um eixo principal associado a desempenho geral ou perfil socioeconômico agregado,
acompanhado por fatores secundários responsáveis por variações mais específicas.


Do ponto de vista da anonimização e da geração de dados sintéticos, essa característica impõe restrições importantes, uma vez que a não preservação adequada das
primeiras componentes principais pode comprometer a estrutura global dos dados
e, consequentemente, sua utilidade analítica. Por outro lado, a manutenção dessas
componentes tende a garantir a preservação de propriedades estatísticas de alto nível, essenciais para análises exploratórias e inferenciais. Nesse contexto, - gráfico de
variância explicada pelas componentes principais estabelece um baseline estrutural
do dado real, permitindo avaliar em que medida a estrutura latente fundamental é
mantida nos dados anonimizados ou sintéticos ao longo do processo de geração.


14


**Projeção dos dados no espaço dos 2 componentes principais**


Figura 8


A projeção dos dados reais e sintéticos no subespaço definido pelas duas primeiras
componentes principais permite avaliar a geometria global no domínio mais informativo dos dados. Como PC1 e PC2 concentram conjuntamente cerca de 73% da variância
total, essa visualização constitui uma comparação estrutural relevante entre as distribuições real e sintética. Observa-se uma sobreposição quase total entre as nuvens de
pontos, tanto em termos de centro quanto de orientação, escala e formato elíptico, indicando que a estrutura linear dominante foi bem preservada no processo de geração
sintética. Esse resultado sugere que médias, variâncias e correlações principais dos
dados originais são adequadamente reproduzidas, sustentando a afirmação de que os
dados sintéticos mantêm boa fidelidade estatística em relação aos dados reais.


Por outro lado, uma análise mais detalhada revela um comportamento anômalo em
regiões específicas do espaço projetado. Na região à esquerda do gráfico, aproximadamente entre PC1 _≈−_ 10 e _−_ 7, observam-se estruturas alongadas e mais densas nos
dados sintéticos, com aparência quase em forma de linha reta, padrão pouco pronunciado nos dados reais. Esse efeito é consistente com um artefato clássico de métodos
baseados em interpolação linear, como o SMOTE, indicando interpolação intensa entre poucos vizinhos em regiões de baixa densidade do espaço original, possivelmente
associadas a perfis extremos, notas muito baixas ou valores faltantes. Tal comportamento não invalida o método, mas explicita seus limites, mostrando que, embora a
estrutura global seja preservada, regiões marginais podem apresentar distorções locais
relevantes para a avaliação da utilidade dos dados anonimizados.


15


**3.4.2** **Garantia de privacidade**


**Linkage**


Figura 9


O gráfico apresentado mostra a distribuição das menores distâncias de linkage entre os
dados sintéticos e os dados reais. A maior parte das distâncias se concentra em torno
de 0,15, com uma quantidade significativa de observações em distâncias mais baixas,
indicadas pela alta frequência na faixa de 0,05 a 0,20. Esse comportamento sugere
que, em muitos casos, os dados sintéticos estão localizados próximos aos dados reais,

- que pode indicar uma boa preservação das relações de proximidade e uma baixa
possibilidade de reidentificação para esses registros.


No entanto, é importante notar a presença de algumas distâncias mais elevadas, indicando exceções onde o processo de anonimização pode ter introduzido maior discrepância. Isso pode ser um sinal de que, em certos casos, a geração dos dados sintéticos
não preservou perfeitamente as relações estruturais e marginais dos dados originais.
De maneira geral, o gráfico sugere que, para a maioria dos registros, os dados sintéticos mantêm uma boa semelhança com os dados reais, mas o controle da variabilidade
nas distâncias maiores é um ponto que deve ser observado para garantir a robustez da
anonimização e a privacidade dos indivíduos.

# **4 Conclusão**


A anonimização de dados permanece como um desafio central na conciliação entre
a preservação da privacidade individual e a manutenção da utilidade analítica dos
dados, principalmente no contexto educacional e acadêmico.


A abordagem utilizada no presente trabalho baseada na adaptação do algoritmo
SMOTE para a geração de dados sintéticos a partir dos microdados do ENEM teve


16


como objetivo principal avaliar em que medida os dados sintéticos gerados são capazes de preservar propriedades estatísticas relevantes dos dados originais, ao mesmo
tempo em que ampliam a proteção à privacidade dos indivíduos representados.


Os resultados indicam que, para um conjunto significativo de variáveis, os dados anonimizados mantêm correlações semelhantes às observadas na base original, além de
apresentarem distribuições compatíveis em variáveis categóricas, com proporções relativas próximas às reais. Esses achados sugerem que, sob determinadas condições, os
dados sintéticos preservam parte da estrutura analítica necessária para estudos educacionais.


Entretanto, a análise também evidenciou limitações importantes da abordagem proposta. Foram identificadas anomalias na distribuição de variáveis numéricas, incluindo acúmulos artificiais e distorções locais decorrentes do processo de interpolação, especialmente em contextos de normalização e em variáveis com natureza não
contínua. Tais resultados reforçam que a aplicação do SMOTE em microdados educacionais requer cuidados adicionais e validações específicas, especialmente quando
empregada como mecanismo de geração de dados sintéticos para fins analíticos.


Conclui-se, portanto, que a metodologia explorada produz resultados analiticamente
informativos, ainda que não isentos de falhas, sendo particularmente útil em contextos nos quais - pesquisador não dispõe de acesso direto aos microdados completos.
Nesses cenários, os dados sintéticos podem atuar como um instrumento exploratório,
permitindo a identificação de padrões gerais e direções de investigação sem a necessidade de exposição aos dados originais sensíveis.


Os resultados obtidos ampliam o debate sobre o uso ético e seguro de microdados públicos, indicando caminhos para o aprimoramento de técnicas que busquem equilibrar
transparência, reprodutibilidade científica e proteção à privacidade.

# **Referências**


[1] BRASIL, Lei nº 13.709 de 14 de Agosto de 2018. Dispõe sobre - tratamento de

dados pessoais, inclusive nos meios digitais, por pessoa natural ou por pessoa
jurídica de direito público ou privado, com o objetivo de proteger os direitos fundamentais de liberdade e de privacidade e o livre desenvolvimento da personalidade da pessoa natural.


Disponível em: `[https://www.planalto.gov.br/ccivil_03/_ato2015-2018/](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm)`
`[2018/lei/L13709.htm](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm)` Acesso em: 10 out. 2025.


[2] INSTITUTO NACIONAL DE ESTUDOS E PESQUISAS EDUCACIONAIS ANÍ
SIO TEIXEIRA (INEP). Relatório de Impacto à Proteção de Dados Pessoais: microdados dos Censos da Educação. Brasília: Inep, 2022.


Disponível em: `[https://download.inep.gov.br/microdados/RIPD_dos_](https://download.inep.gov.br/microdados/RIPD_dos_microdados_dos_Censos_da_Educa%C3%A7%C3%A3o.pdf)`
`[microdados_dos_Censos_da_Educa%C3%A7%C3%A3o.pdf](https://download.inep.gov.br/microdados/RIPD_dos_microdados_dos_Censos_da_Educa%C3%A7%C3%A3o.pdf)` . Acesso em: 20 out. 2025.


[3] CHAWLA, BOWYER, HALL & KEGELMEYER (2002), SMOTE: Synthetic Mi
nority Over-sampling Technique, Journal of Artificial Intelligence Research 16
321–357.


17


[4] LUBARSKY, Boris. Re-identification of "Anonymized Data". Georgetown Law Te
chnology Review, v. 1, 2017.


[5] SNOKE, Joshua et al. General and specific utility measures for synthetic data.

Journal of the Royal Statistical Society: Series A (Statistics in Society), 2018.


[6] MURTHY, Suntherasvaran et al. A Comparative Study of Data Anonymization

Techniques. In: 2019 IEEE 5th Intl Conference on Big Data Security on Cloud
(BigDataSecurity). IEEE, 2019. p. 306-309.


[7] MATHISEN, Bjørn Magnus et al. Learning similarity measures from data. Pro
gress in Artificial Intelligence, 2020.


[8] JI, Shouling; MITTAL, Prateek; BEYAH, Raheem. Graph Data Anonymization,

De-anonymization Attacks, and De-anonymizability Quantification: A Survey.
IEEE Communications Surveys & Tutorials, 2017.


[9] FERNÁNDEZ, Alberto et al. SMOTE for Learning from Imbalanced Data: Pro
gress and Challenges, Marking the 15-year Anniversary. Journal of Artificial Intelligence Research, 2018.


18


