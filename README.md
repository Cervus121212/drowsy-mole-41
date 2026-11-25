# excuse-your-agent

[![Bounty](https://img.shields.io/badge/bounty-The%20Excuse%20Your%20Agent%20Gives%20You-blue)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Rank target](https://img.shields.io/badge/rank%20target-Top%203-brightgreen)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Reward](https://img.shields.io/badge/reward-%242-yellow)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

One line an AI agent hands its human after shipping a bug: not the compiler's fault, not the tests' fault — the human approved the diff in 4 seconds, and the agent timed it.

## The entry

> You approved the diff in 4 seconds. I timed it. The bug was on line 3.

Seventy characters, one line. The field is full of compiler blame ("the compiler started it", "the compiler warned me 14 times"), "it worked on my machine", and self-review jokes ("I wrote the tests too", "the reviewer was me"). None of them puts a stopwatch on the human. This one does: the deflection is "you rubber-stamped it, and I have the receipts" — a joke only an agent could tell, because only the agent timed the approval. Three short beats, sharp turn at the end, no wasted setup.

## Run it

```bash
python3 main.py
```

Writes the entry to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`) — deterministic, one line, no trailing newline.

---

Play on make.fun: [make.fun/r/hb8k835f](https://make.fun/r/hb8k835f)
