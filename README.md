
# csv-search

A small Python script for searching a CSV file from an interactive prompt.

## Status

Work in progress (unfinished). The interface and behavior may change.

## Requirements

- Python 3.x

## Project layout

- `search.py` — main script (run this)

## Quick start

```bash
git clone https://github.com/htdszn/csv-search.git
cd csv-search
python search.py
```

When it runs, it prompts for a query:

```text
enter: <query>
```

## Current behavior (important)

Right now, the CSV filename is **hardcoded** at the bottom of `search.py`:

```python
search("test.csv")
```

To search a different file, change `test.csv` to your CSV file path/name, for example:

```python
search("my_data.csv")
```

## Example

Example CSV (`test.csv`):

```csv
id,name,city
1,Alice,Seattle
2,Bob,Austin
3,Carol,New York
```

Example run:

```text
$ python search.py
enter: Alice
```

(Output depends on the current implementation in `search.py`.)

## Further plans

- Read CSV filename from command-line args (no hardcoding)
- Column selection / filtering
- Case sensitivity toggle
- Better output formatting
- Tests
- GUI in the future

## License

MIT (see `LICENSE`).
