# ✊✋✌️ Rock Paper Scissors CLI (Jokenpô)

A terminal version of rock-paper-scissors against the computer, with a short countdown ("JO... KEN... PÔ!") for a bit of suspense.

## How the game works

1. Choose **1** (rock), **2** (paper) or **3** (scissors)
2. The computer picks a random option
3. After the "JO · KEN · PÔ!" countdown, the result is shown
4. A **tie** or a **loss** starts a new round. The game ends when **you win**

## Features

- Input validation: letters or numbers outside 1–3 are rejected and asked again, no crash
- Random computer choice with `random.randint`
- Pauses with `time.sleep` for the countdown effect
- Clear result messages for win, tie and loss

## Concepts practiced

- `while` loops and loop control
- `try`/`except` (`ValueError`) for safe input
- Conditionals (`if`/`elif`/`else`) for the game rules
- Standard library: `random` and `time`

## Requirements

- Python 3.8+
- No external dependencies

## How to run

```bash
git clone https://github.com/<your-user>/rock-paper-scissors-cli.git
cd rock-paper-scissors-cli
python rock_paper_scissors.py
```

## Example output

```
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
§§§§§§§§§§§ JOKENPÔ §§§§§§§§§§§
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
CARREGANDO JOGO...
(1) PEDRA
(2) PAPEL
(3) TESOURA
 Digite: 2
JO
KEN
PÔ!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
O computador jogou PEDRA!
Você jogou PAPEL!
PARABÉNS VOCÊ VENCEU
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
```

## Ideas for improvement

- Replace the nine hand-written cases with a dictionary of winning pairs (`{"rock": "scissors", ...}`)
- Add a score counter and a "best of N" mode
- Add a "play again?" prompt instead of ending on the first win
- Add the Rock-Paper-Scissors-Lizard-Spock variant
