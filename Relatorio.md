João Vitor de Souza (581431) - Turma A
Milton Pacheco (590535) - Turma B

2.2 a)

(i) O minimax sempre ganha ou empata contra o randomplayer?

Sim, o minimax analisa toda a árvore de jogo do jogo da velha invertido, já que o número de estados possíveis é pequeno. Isso permite que ele escolha sempre a jogada que maximiza suas chances de vitória ou no mínimo evita qualquer possibilidade de derrota. Como o randomplayer escolhe jogadas aleatórias, ele frequentemente comete erros que abrem caminho para vitórias do minimax. Mesmo quando não comete erros graves, o minimax ainda consegue garantir ao menos um empate, pois nunca toma decisões que levem a posições perdedoras. Portanto, o minimax nunca perde e geralmente vence contra um jogador aleatório.

(ii) O minimax sempre empata consigo mesmo?

Sim, nesse caso ambos agentes avaliam a árvore completa do jogo e executam apenas jogadas consideradas ótimas pela estratégia perfeita. No jogo da velha invertido, já se sabe que essa estratégia ótima leva inevitavelmente ao empate quando ambos os jogadores são perfeitos. SLogo, se existir um caminho que garantisse vitória para um dos lados o outro minimax também encontraria essa mesma linha de jogo ao analisar o estado inicial, o que resultaria em uma contradição, por isso, dois minimax jogando um contra o outro se anulam mutuamente e terminam o jogo da velha empatando.

(iii) O minimax não perde para você mesmo usando sua melhor estratégia?

O minimax calcula o desfecho de todas as sequências possíveis e escolhe sempre a jogada que evita derrotas, se você jogar perfeitamente, o resultado será um empate pois você estará seguindo exatamente a mesma estratégia ótima que o minimax identificou. Porém, a única forma de o minimax ganhar é se você cometer algum erro durante a partida, nesse caso ele imediatamente identifica a jogada que explora esse erro e força uma vitória. Logo, contra um jogador humano que utiliza a melhor estratégia possível o minimax não tende a perder ele empata no pior caso e vence caso encontre alguma falha na sua decisão.


Resultados:

Partida 1 - Contagem de peças X Valor posicional:
  B (advsearch/secret_agent): 37 peças - win
  W (advsearch/secret_agent): 27 peças - loss

Partida 2 - Valor posicional X Contagem de peças:
  B (advsearch/secret_agent): 26 peças - loss
  W (advsearch/secret_agent): 38 peças - win

Partida 3 - Contagem de peças X Heurística customizada:
  B (advsearch/secret_agent): 12 peças - loss
  W (advsearch/secret_agent): 52 peças - win

Partida 4 - Heurística customizada X Contagem de peças:
  B (advsearch/secret_agent): 35 peças - win
  W (advsearch/secret_agent): 29 peças - loss

Partida 5- Valor posicional X Heurística customizada:
  B (advsearch/secret_agent): 8 peças - loss
  W (advsearch/secret_agent): 56 peças - win

Partida 6 - Heurística customizada X Valor posicional:
  B (advsearch/secret_agent): 38 peças - win
  W (advsearch/secret_agent): 26 peças - loss

Resultado final:
A heurística customizada foi a mais bem-sucedida com 4 vitórias em 4 partidas disputadas.


Heurística customizada:

A heurística combina mobilidade e valor posicional para medir a vantagem no tabuleiro. A mobilidade indica a diferença entre as opções de jogada do jogador e do adversário, já o valor posicional considera o peso estratégico das casas ocupadas, com destaque para a importância dos cantos e o risco das casas adjacentes.
Essa abordagem surgiu de discussões entre os membros do grupo, analisando diferentes alternativas de implementação, além disso, foram realizadas discussões também com o ChatGPT para apoiar o refinamento das explicações e estruturar melhor o raciocínio, até se chegar à fórmula final adotada.


Critério de parada:

O critério de parada da busca utiliza uma profundidade máxima fixa de 5 níveis, dessa forma, o algoritmo interrompe a expansão das jogadas quando atinge esse limite ou quando identifica um estado terminal do jogo. Não há uso de aprofundamento iterativo nem limite de tempo, sendo a profundidade é o único fator de controle da exploração. Assim, a busca sempre finaliza ao alcançar o quinto nível ou ao encontrar uma posição em que a partida já esteja decidida.


Diante dos resultados obtidos nas partidas realizadas, a heurística customizada demonstrou desempenho superior às demais, vencendo todos os confrontos. Por demonstrar melhor equilíbrio entre análise posicional e controle das decisões ao longo da partida, ela foi definida como a estratégia oficial do agente para o torneio, com isso, utilizamos a solução mais sólida e de maior impacto entre as alternativas desenvolvidas e testadas pelo grupo.