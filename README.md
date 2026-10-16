# Muffin Math

Muffin batter honesty. The recipe says stir until just combined, and it never says what combined costs. Muffin Math does the sugar-ratio, stroke-count and well-fill arithmetic a muffin depends on, with every norm labeled.

## What it computes

- **The batter truth** - sugar per cup of flour rounded to tenths, then judged: lean and breakfast-leaning, a true muffin, or cupcake territory wearing a muffin paper (the half-cup line is a labeled kitchen norm).
- **The stir truth** - strokes stirred against the 10-to-12 just-combined norm (a labeled kitchen norm): tender crumb, a little past, or tunnels and peaky tops.
- **The scoop truth** - batter cups against wells to fill at a third of a cup per standard well (a labeled kitchen norm): covers with cups to spare, covers exactly, or comes up short by a counted amount.

## Boundary

Illustrative arithmetic only. Every norm is a labeled kitchen norm; your recipe and your tin win every tie. Muffin Math never judges doneness or food safety - follow your recipe's bake guidance.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (22 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/muffinmath/
Repo: https://github.com/iLanis-agent/muffinmath
