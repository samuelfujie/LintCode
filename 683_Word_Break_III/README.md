# 683. Word Break III
[ https://www.lintcode.com/problem/word-break-iii/description ]

Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.

## Example
**Example 1:**

Input:
```sh
"CatMat"
["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
```
Output:
```sh
3
```
Explanation:
we can form 3 sentences, as follows:
"CatMat" = "Cat" + "Mat"
"CatMat" = "Ca" + "tM" + "at"
"CatMat" = "C" + "at" + "Mat"

**Example 2:**

Input:
```sh
"a"
[]
```
Output:
```sh
0
```

## Notice
Ignore case