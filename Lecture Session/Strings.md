# Problems on string

## Strings in python

```text
Strings are arrays of bytes representing Unicode characters.

Python does not have a character data type.

A single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
```

## Pattern searching

```text
Yoy are given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(txt, pat) that prints all occurrences of pattern in text. Assuming that n > m.
```

```text
Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12
```

```text
Best case - First character of the pattern is not present in text
```

```text
Worst case -  When all characters of the text and pattern are same or only the last character is different.
```

```text
Complexity - O(m*(n-m+1))
```

## KMP (Knuth Morris Pratt) algorithm

```text
The KMP matching algorithm uses degenerating property (pattern having same sub-patterns appearing more than once in the pattern)

Example -

txt = "AAAAABAAABA" 
pat = "AAAA"

We only compare fourth A of pattern with fourth character of current window of text to decide whether current window matches or not. Since we know first three characters will anyway match, we skipped matching first three characters.
```

```text
Preprocessing - lps[], Longest proper prefix which is also a suffix

lps[i] = Longest proper prefix of pat[0..i], which is also a suffix of pat[0..i].

For example, prefixes of “ABC” are “”, “A”, “AB” and “ABC”. Proper prefixes are “”, “A” and “AB”. Suffixes of the string are “”, “C”, “BC” and “ABC”.

For the pattern “AAAA”, 
lps[] is [0, 1, 2, 3]
```

## Problems
```text
Length of the longest substring that does not contain any vowel

Input: S = "helloworld"
Output: 3

Input: S = “ceebbaceeffo”
Output: 2
```


```text
A string consisting only of a, b, c can be made empty by removing substring “abc” recursively

Input: abcabc
Output: Yes

Input: abcabcababccc
Output: Yes
```