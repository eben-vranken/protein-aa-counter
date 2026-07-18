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