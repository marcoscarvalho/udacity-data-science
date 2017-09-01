# Resumo
Neste projeto, você irá demonstrar seu conhecimento em estatística descritiva, realizando uma experiência que lida com a distribuição de um baralho de cartas, e criando uma anotação com suas descobertas.

## Perguntas para Investigação
Esta experiência exigirá o uso de um baralho padrão de cartas. Este é um baralho de cinquenta e duas cartas dividido em quatro naipes (espadas (♠), copas (♥), ouros (♦) e paus (♣)), cada naipe contendo treze cartas (Ás, cartas numeradas de 2-10, e cartas figuradas Valete, Dama e Rei). Para esta experiência, você pode usar um baralho físico ou o nosso gerador de dados na seção Gerar dados.

Para os fins desta tarefa, atribua a cada carta um valor: o Ás tem valor de 1, as cartas numeradas recebem o valor impresso nelas e as figuradas, Valetes, Damas e Reis, têm valor de 10.

Para o resto da aula, você fará o seguinte:

* **Distribuição de Valores das Cartas:** Nesta seção, você criará um histograma e responderá perguntas do questionário sobre a distribuição dos valores das cartas.
* **Gerar dados:** Nesta seção, você receberá amostras para uma nova distribuição. Para obter uma amostra única, embaralhe o baralho e tire três cartas dele. (Você terá uma amostragem do baralho sem substituição). Registre as três cartas que você tirou e a soma dos valores delas. Substitua as cartas retiradas do baralho e repita este procedimento de amostragem no total, pelo menos, trinta vezes.
* **Criar Anotações:** Você criará um resumo de suas descobertas.
* **Avaliar as respostas:** Você irá comparar seus resultados com os de um programa de computador que gera os resultados automaticamente.

## Distribuição de valores das cartas
Para começar, faça um histograma representando as frequências relativas dos valores quando você distribui as cartas apenas um vez . Ou seja, pegue todas as cartas do baralho e coloque na mesa, digite em uma planilha os valores correspondentes a cada carta, você deve contar 52 cartas no final. Faça um histograma com esses valores. Depois de fazer isso, preencha a caixa de seleção para verificar seu trabalho.

![alt text](https://github.com/marcoscarvalho/udacity-data-science/blob/master/distribuicao-de-cartas/histogram-of-single-draw-values.png "Histograma de cartas")

# Gerando dados
Agora que você calculou as estatísticas para uma única distribuição de cartas, iremos analisar as estatísticas da soma das pontuações ao fazer distribuições de três cartas. Uma vez que existem muitas formas tirar três cartas de um baralho, vamos abordar isso usando amostragem para fazer estimativas.

Em cada teste, as cartas serão distribuídas sem substituição, o que significa que em um único conjunto de três, cada carta pode aparecer no máximo uma vez. Após cada teste, as cartas que foram distribuídas foram recolocadas no baralho para que sejam re-embaralhadas e distribuídas novamente no próximo teste.

Você pode gerar cartas de dois modos. Em primeiro lugar, você pode usar a caixa de perguntas abaixo para gerar dados para você. Os testes serão organizados em linhas individuais. Cada carta é codificada como uma string que consiste na classificação (A, 2-10, J, Q, K) seguida pelo terno (c, d, h, s). Trinta testes serão realizados para sua análise. Alternativamente, você pode executar o procedimento de amostragem usando um baralho físico. Certifique-se de que você só substitui e embaralha as cartas no baralho depois que cada conjunto de três cartas é distribuído. Junte pelo menos trinta testes para sua análise.

Quando você pressiona Testar ou Enviar, um conjunto aleatório de trinta ensaios, composto por Trêss cartas cada, serão gerados de acordo com a documentação acima. Você irá calcular estatísticas resumidas desses resultados e usá-los para responder a uma série de questionários.

Antes de enviar, selecione um valor de semente. Isso garantirá que, se você precisar volta para este questionário, os resultados das cartas aleatório serão os mesmos. Você também pode usar essa semente na seção Avaliar resposta para verificar sua resposta por resultados específicos.

add codigo
```python
s = "Python syntax highlighting"
print s
```

# Resumo das suas conclusões
Crie um arquivo PDF ou markdown que contenha o seguinte:

Primeiro, crie um histograma que represente as frequências relativas dos valores das cartas para uma única distribuição. Informe a média, a mediana e o desvio padrão da distribuição de valor. (Você deve ter realizado esta etapa na seção _Distribuição de Valores das Cartas).
Dê uma olhada na distribuição das somas de três cartas das amostras que você obteve, seja de Generate Data ou de sua própria coleção. Informe as estatísticas descritivas das amostras que você distribuiu. Inclua pelo menos duas medidas de tendência central e duas medidas de variabilidade.
Crie um histograma das somas das três cartas de amostra. Compare a sua forma com a distribuição original. Veja como eles são diferentes, e se você pode explicar porque esse é o caso.
Faça algumas estimativas sobre os valores que você obteria em distribuições futuras. Dentro de qual intervalo você espera que aproximadamente 90% dos valores da sua distribuição caiam? Qual é a probabilidade aproximada de que você obtenha um valor de distribuição de pelo menos 20? Certifique-se de justificar como você obteve seus valores.
Salve suas anotações para que você possa incluí-las em seu portfólio! Esta é uma ótima maneira de ensinar aos outros sobre o teorema do limite central. Depois de criar sua anotação, você pode verificar suas respostas na próxima página.

### Estatísticas descritivas
Use este questionário para verificar se você calculou suas estatísticas descritivas corretamente. O feedback sobre este questionário irá relatar as medidas mais comuns, mas você pode ter escrito algumas outras respostas. Digite o número de semente que você usou para gerar os dados e, em seguida, envie para ver o que obtivemos.
* add resultado

### Histograma de valores

Use o questionário abaixo para verificar o seu trabalho em relação a um histograma dos dados da amostra. Como essa forma se compara à distribuição de um único desenho? Cocê pode explicar por que? Certifique-se de responder antes de enviar suas respostas!

Use o Test Run para gerar o histograma e verificar a forma de distribuição. Depois de verificar a sua resposta, escolha Enviar resposta para verificar o seu raciocínio do por que a forma da distribuição é assim.

add codigo e image

### Distribuição de valores
Dentro de qual intervalo você espera que aproximadamente 90% dos valores da sua distribuição das três cartas caiam? Qual é a probabilidade aproximada de que você obtenha um valor de ao menos 20 em uma distribuição aleatória? Insira seu número de seed para ver como as suas respostas se comparam com as outras.