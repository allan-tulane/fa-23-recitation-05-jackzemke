# CMPS 2200 Recitation 6

## Answers

**Name:** Jack Zemke


Place all written answers from `recitation-06.md` here for easier grading.



- **d.**

|   File    |   Fixed-Length Coding   |   Huffman Coding   |   Huffman vs. Fixed-Length   |
|:-----:|:------------:|:------------:|:------------:|
f1.txt    |       $1340$               |     $826$           | $1 : 0.616$
alice29.txt    |      $1039367$               |       $676374$         |$1 : 0.651$
asyoulik.txt    |        $876253$             |           $606448$     |$1 : 0.692$
grammar.lsp    |           $26047$          |        $17356$        |$1 : 0.666$
fields.c    |           $78050$          |        $56206$        |$1 : 0.720$

The Fixed-Length Coding is consistently only around $2/3$ as effecient as the Huffman Coding. These results are consistent across the board, where Fixed-Length coding is between $0.616$ and $0.720$ as effecient as Huffman Coding, depending on the file.
- **e.**

If every character has the same frequency, they all have the same probability of $\frac{1}{n}$, where $n$ is the number of characters in the alphabet.

The expected cost $C$ of the Huffman encoding is  the *average* number of bits required to encode a single character. Because they all have the same probability, their *average* number of bits to encode is the same. The average enumber of bits required to represent a character will be proportional to the depth of the tree. This is because if every character appears with the same probability then they should all be at the leaf node of the tree, which is $\log_2(n)$. 

The expected cost of the encoding can be calculated by multiplying the average number of bits required for a character by the probability that a character may appear, so $C = \log_2(n) * \frac{1}{n} = \frac{\log_2(n)}{n}$

