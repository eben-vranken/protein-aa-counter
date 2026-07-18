<h1 align="center">🧫 Protein Amino Acid Counter</h1>

<p align="center">
    A command-line utility to count amino acid frequencies in a protein sequence.
</p>

<p align="center">
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
</p>

A modular, zero-dependency Python CLI built to analyze protein sequences. It takes a raw sequence or a FASTA file, validates it against the 20-letter amino acid alphabet, tallies how often each amino acid occurs, and reports the result as plain output or a formatted table.

## Install

Clone the repository directly:
```bash
git clone https://github.com/eben-vranken/protein-aa-counter.git
cd protein-aa-counter
```

## Usage

Pass a raw protein sequence with `-s`, or a FASTA file with `-f`. Exactly one of the two is required. The tool counts every amino acid in the sequence and can print the result as a plain list or as a table, with optional full amino acid names.

```bash
python amino-acid-counter.py -s MTEYKLVVVGAGGVGKSALTIQ --table --verbose
```

### Short Flags

The same arguments are available in short form:

```bash
python amino-acid-counter.py -s MTEYKLVVVGAGGVGKSALTIQ -t -v
```

### FASTA Input

```bash
python amino-acid-counter.py -f data/human_protein.fasta -t
```

### Example Output
```
| Amino | Count |
| A     | 2     |
| R     | 0     |
| N     | 0     |
| D     | 0     |
| C     | 0     |
| E     | 1     |
| Q     | 1     |
| G     | 4     |
| H     | 0     |
| I     | 1     |
| L     | 2     |
| K     | 2     |
| M     | 1     |
| F     | 0     |
| P     | 0     |
| S     | 1     |
| T     | 2     |
| W     | 0     |
| Y     | 1     |
| V     | 4     |
```

## Configuration Matrix

| Argument | Option / Choices | Default | Description |
| --- | --- | --- | --- |
| `-s`, `--sequence` | *Protein sequence string* | *None* | Raw protein sequence to count (e.g. `MTEYK`). Required unless `-f` is used. |
| `-f`, `--file` | *File path* | *None* | Path to a FASTA protein file. Required unless `-s` is used. |
| `-t`, `--table` | *Flag* | `False` | Print the frequencies as a formatted table instead of a plain list. |
| `-v`, `--verbose` | *Flag* | `False` | Print full amino acid names (e.g. `Alanine`) instead of single-letter codes. |

## Feature Set

* **Sequence Parsing:** Reads a raw sequence directly, or extracts and concatenates the sequence lines from a FASTA file, skipping header lines.
* **Input Validation:** Rejects any character outside the 20-letter amino acid alphabet and requires exactly one of `-s` or `-f`.
* **Frequency Counting:** Tallies occurrences of all 20 amino acids across the sequence, including ones with zero occurrences.
* **Plain Output:** Prints each amino acid and its count on its own line.
* **Table Rendering:** Prints a clean, column-aligned table of counts, with column widths sized to fit the longest label.
* **Verbose Labels:** Swaps single-letter codes for full amino acid names in either output mode.

## License

MIT