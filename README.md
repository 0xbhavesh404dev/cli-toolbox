# 🧰 cli-toolbox

A growing collection of small, dependency-free Python command-line tools.

- Every tool is a **single file** in [`tools/`](tools/) — no frameworks, no third-party packages.
- Each tool ships with **unit tests** in [`tests/`](tests/).
- Every tool landed through a small, focused pull request.

## Tools

| Tool | What it does | Try it |
|---|---|---|
| [dice.py](tools/dice.py) | Roll dice, e.g. `3d6+2` | `python3 tools/dice.py 3d6+2` |
| [passgen.py](tools/passgen.py) | Random passwords via `secrets` | `python3 tools/passgen.py --length 24` |
| [units.py](tools/units.py) | Convert length, mass, temperature | `python3 tools/units.py 5 km mi` |
| [wordcount.py](tools/wordcount.py) | Lines, words, characters | `python3 tools/wordcount.py README.md` |
| [b64tool.py](tools/b64tool.py) | Base64 encode/decode | `python3 tools/b64tool.py encode --text hello` |
| [uuidgen.py](tools/uuidgen.py) | Generate UUID4s | `python3 tools/uuidgen.py --count 5` |
| [picker.py](tools/picker.py) | Pick random items / flip a coin | `python3 tools/picker.py pizza pasta --seed 42` |
| [organize.py](tools/organize.py) | Sort files into type folders | `python3 tools/organize.py ~/Downloads` |
| [textstats.py](tools/textstats.py) | Reading time, top words | `python3 tools/textstats.py README.md` |
| [csvsum.py](tools/csvsum.py) | Summarize one CSV column | `python3 tools/csvsum.py data.csv --column score` |
| [tzconv.py](tools/tzconv.py) | Convert time between zones | `python3 tools/tzconv.py 14:30 --from Asia/Kolkata --to UTC` |
| [subnet.py](tools/subnet.py) | IPv4 subnet facts | `python3 tools/subnet.py 192.168.1.0/24` |
| [palette.py](tools/palette.py) | Shades of a hex color | `python3 tools/palette.py #e63946` |
| [lorem.py](tools/lorem.py) | Placeholder text | `python3 tools/lorem.py --paragraphs 2 --seed 7` |

## Running the tests

No dependencies needed — plain `unittest`:

```bash
python3 -m unittest discover -v
```

CI runs the same suite on Python 3.10 and 3.12 for every pull request.

## Project structure

```
cli-toolbox/
├── tools/          # one self-contained CLI tool per file
├── tests/          # unittest test cases, mirroring tools/
└── .github/workflows/ci.yml
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The short version: one tool per pull request, keep it stdlib-only, add tests, keep the README table updated.

## Challenges & lessons learned

Honest notes from building this toolbox:

- **Testing random code needs seams.** The first versions of `picker.py` and `lorem.py` called `random` directly, which made tests flaky. Injecting an `rng` parameter (defaulting to `random`) made every test deterministic, and `--seed` made the CLIs repeatable too.
- **Time-zone tests drift if you pick the wrong zones.** Converting between `Asia/Kolkata` and `UTC` is stable all year, but `America/New_York` jumps twice a year with DST. Tests now pin an explicit date, so both behaviors are asserted instead of guessed.
- **Assumptions get caught by tests, not by vibes.** The palette tests assumed 3-digit hex `08f` expands to `0080ff` (it actually doubles each digit to `0088ff`) and that "lighten ×3" becomes white (channels clamp individually). Two wrong assumptions, two failing tests, two quick fixes.
- **Consistency across many small CLIs is its own discipline.** With 14 tools, the repeated pattern — parse args, validate, do the work, `parser.error()` on bad input — had to be copied carefully each time. Keeping every tool a single file forces the interface to stay simple.
- **`shutil.move` over `Path.replace`** so the organizer still works when moving across filesystems, and tests use `tempfile.TemporaryDirectory` so nothing on disk is ever touched for real.

## License

[MIT](LICENSE)
