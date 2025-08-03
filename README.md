# 🐍 Snake Game - Cobra Multicolorida

Um jogo Snake avançado implementado em Python usando Pygame, com sistema de fases, dificuldade progressiva, comidas especiais e **cobra multicolorida**!

## 🎮 Como Jogar

### Controles:
- **Setas direcionais**: Controlam a direção da cobra
- **ESPAÇO**: Pausar/despausar o jogo
- **R**: Reiniciar o jogo (após Game Over)
- **ESC**: Sair do jogo

### Objetivo:
- Coma as comidas para crescer e ganhar pontos
- Evite colidir com as bordas, obstáculos ou o próprio corpo
- Complete fases para aumentar a dificuldade
- Colete comidas especiais para bônus!
- **Crie uma cobra única e multicolorida!** 🌈

## 🚀 Como Executar

### Pré-requisitos:
- Python 3.7 ou superior
- Pygame

### Instalação:

1. Clone ou baixe este repositório
2. Instale as dependências:
```bash
py -m pip install pygame
```

3. Execute o jogo:
```bash
py main.py
```

## 🎯 Novas Funcionalidades

### 🌈 **Cobra Multicolorida Progressiva:**
- **Sistema progressivo**: O padrão de cores muda conforme a cobra cresce
- **1-10 segmentos**: 1 quadrado por cor (arco-íris individual)
- **11-20 segmentos**: 2 quadrados por cor
- **21-30 segmentos**: 3 quadrados por cor
- **31-40 segmentos**: 4 quadrados por cor
- **41+ segmentos**: 5 quadrados por cor
- **Comidas coletadas**: Substituem as cores padrão
- **História visual**: A cobra mostra todas as comidas que você coletou!

### 🌟 **Sistema de Fases:**
- **Fase 1**: Sem obstáculos, velocidade baixa
- **Fase 2+**: Obstáculos aparecem gradualmente
- **Progressão**: Cada fase adiciona mais obstáculos
- **Máximo**: 15 obstáculos por fase

### ⚡ **Velocidade Gradativa:**
- **Velocidade base**: 5 FPS (mais lento no início)
- **Aumento gradativo**: Baseado no tamanho da cobra
  - 1-5 segmentos: 5 FPS (muito lento)
  - 6-10 segmentos: 6 FPS
  - 11-15 segmentos: 7 FPS
  - 16-20 segmentos: 8 FPS
  - 21-25 segmentos: 9 FPS
  - 26-30 segmentos: 10 FPS
  - 31+ segmentos: 11 FPS
- **Aumento por fase**: +1 FPS por nível
- **Boost temporário**: +3 FPS por 5 segundos
- **Velocidade máxima**: 11 FPS + boost + nível

### 🍎 **Comidas Especiais:**
- **🔴 Comida Normal**: 10 pontos × nível atual
- **🟡 Comida Bônus**: +50 pontos extras
- **🟣 Comida Speed**: Boost de velocidade por 5 segundos

### 🏆 **Sistema de Pontuação:**
- **Pontos baseados no nível**: Mais pontos em fases avançadas
- **Bônus especiais**: Comidas especiais dão pontos extras
- **Progressão**: Cada fase vale mais pontos

### 🎨 **Melhorias Visuais:**
- **Cobra multicolorida**: Cada segmento tem a cor da comida coletada
- **Obstáculos cinzas**: Blocos que devem ser evitados
- **Comidas coloridas**: Cada tipo tem sua cor
- **Interface informativa**: Mostra fase, velocidade, pontuação e cores coletadas

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pygame 2.6.1**

## 📁 Estrutura do Projeto

```
snakegame/
├── main.py              # Jogo principal com todas as funcionalidades
├── requirements.txt     # Dependências do projeto
└── README.md           # Este arquivo
```

## 🎨 Personalização

Você pode facilmente personalizar o jogo modificando as constantes no início do arquivo `main.py`:

- `WINDOW_WIDTH` e `WINDOW_HEIGHT`: Tamanho da janela
- `GRID_SIZE`: Tamanho de cada célula da grade
- `base_speed`: Velocidade inicial do jogo
- Cores: Modifique as constantes de cores para mudar a aparência

## 🏆 Dicas para Jogar

1. **Planeje seus movimentos**: Com obstáculos, planejamento é essencial
2. **Use o boost de velocidade**: Aproveite as comidas roxas para escapar de situações difíceis
3. **Colete bônus**: As comidas amarelas dão muitos pontos extras
4. **Adapte-se à velocidade**: Cada fase fica mais rápida
5. **Pause quando necessário**: Use ESPAÇO para pensar em estratégias
6. **Crie padrões coloridos**: Colete comidas em sequência para criar padrões únicos!

## 🎯 Estratégias Avançadas

- **Manobras de emergência**: Use boost de velocidade para escapar
- **Rota planejada**: Antes de comer, planeje seu caminho de volta
- **Gestão de espaço**: Em fases avançadas, espaço é limitado
- **Priorize bônus**: Comidas especiais valem muito mais pontos
- **Arte com cores**: Tente criar padrões específicos na sua cobra!

## 🌈 Sistema de Cores

### Como funciona:
1. **Cabeça**: Sempre verde (padrão)
2. **Segmentos**: Cada um tem a cor da comida que foi coletada
3. **Ordem**: As cores aparecem na ordem que você coletou as comidas
4. **História**: A cobra conta a história de todas as suas conquistas!

### Tipos de comida e cores:
- **🔴 Vermelho**: Comida normal
- **🟡 Amarelo**: Comida bônus (+50 pontos)
- **🟣 Roxo**: Comida speed (boost de velocidade)

Divirta-se criando sua cobra única e multicolorida! 🎮🌈 