# Contributing to cli-toolbox

Thanks for wanting to add a tool! This project deliberately keeps things tiny:

1. **One tool per pull request.** A tool is a single file in `tools/` plus a matching `tests/test_<name>.py`.
2. **Standard library only.** If it needs `pip install`, it does not belong here.
3. **Every tool gets tests.** Aim for the happy path plus the obviously-wrong inputs.
4. **Random behavior must be seedable.** Accept an `rng` parameter (defaulting to `random`) so tests can be deterministic.
5. **Update the README table** in the same PR so the catalog stays complete.

## Adding a tool in 5 steps

```bash
git checkout -b feat/my-tool
# write tools/my_tool.py and tests/test_my_tool.py
python3 -m unittest discover -v
git commit -m "Add my tool"
git push -u origin feat/my-tool
```

Then open a pull request. CI will run the full suite on Python 3.10 and 3.12.

## Style notes

- Each tool starts with a module docstring showing real usage examples.
- Wrap the CLI in a `main()` function with an `if __name__ == "__main__":` guard so tests can import it.
- Prefer `parser.error(...)` for bad user input — it prints a clean message and exits with status 2.
