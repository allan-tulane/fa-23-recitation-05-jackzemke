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

Because all of the characters have the same frequency, they will all be at the leaf level of the tree. Because the length of the code is proportional to the level of the tree the character is on, the characters will, on average, have an encoding of length $\log_2(|\Sigma|)$ (the depth of the tree).

The expected cost of the encoding can be calculated by multiplying the average number of bits required to encode a character by the number of characters, $n$, in the document. Therefore $C_{expected} = n\log_2(|\Sigma|)$

