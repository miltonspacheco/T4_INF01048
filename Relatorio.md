2.2

a)

(i) O minimax sempre ganha ou empata contra o randomplayer?

Sim, o minimax analisa toda a árvore de jogo do jogo da velha invertido, já que o número de estados possíveis é pequeno. Isso permite que ele escolha sempre a jogada que maximiza suas chances de vitória ou no mínimo evita qualquer possibilidade de derrota. Como o randomplayer escolhe jogadas aleatórias, ele frequentemente comete erros que abrem caminho para vitórias do minimax. Mesmo quando não comete erros graves, o minimax ainda consegue garantir ao menos um empate, pois nunca toma decisões que levem a posições perdedoras. Portanto, o minimax nunca perde e geralmente vence contra um jogador aleatório.

(ii) O minimax sempre empata consigo mesmo?

Sim, nesse caso ambos agentes avaliam a árvore completa do jogo e executam apenas jogadas consideradas ótimas pela estratégia perfeita. No jogo da velha invertido, já se sabe que essa estratégia ótima leva inevitavelmente ao empate quando ambos os jogadores são perfeitos. SLogo, se existir um caminho que garantisse vitória para um dos lados o outro minimax também encontraria essa mesma linha de jogo ao analisar o estado inicial, o que resultaria em uma contradição, por isso, dois minimax jogando um contra o outro se anulam mutuamente e terminam o jogo da velha empatando.

(iii) O minimax não perde para você mesmo usando sua melhor estratégia?

O minimax calcula o desfecho de todas as sequências possíveis e escolhe sempre a jogada que evita derrotas, se você jogar perfeitamente, o resultado será um empate pois você estará seguindo exatamente a mesma estratégia ótima que o minimax identificou. Porém, a única forma de o minimax ganhar é se você cometer algum erro durante a partida, nesse caso ele imediatamente identifica a jogada que explora esse erro e força uma vitória. Logo, contra um jogador humano que utiliza a melhor estratégia possível o minimax não tende a perder ele empata no pior caso e vence caso encontre alguma falha na sua decisão.