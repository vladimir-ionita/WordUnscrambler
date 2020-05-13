# About
Word unscrambler inspired from the `Wordscapes` game.

## Installation
1. Clone or download the repository locally.
2. Install the dependencies: ```pip install -r requirements.txt```.
3. Done!

## Usage
1. Before the first usage, you need to download the dictionary:
   ```
   python dd.py
   ```
   A GUI window will open for the download. Follow the steps.
2. Run the unscrambler:
   ```
   python main.py
   ```
   The process of unscrambling a word consists of two parts:
   1) Enter the scrambled word. This represents a collection of letters you want your words to be formed from.
   For example, enter `rtue` if you want to compose words from the letters `r`, `t`, `u` and `e`. Keep in mind that a letter can be used only once in a word.
   
   2) Enter the pattern or the length of the word. For example, if you want a word of 4 letters, enter 4.
   If, otherwise, you have more specific constraints, you can enter a pattern.
   
   Pattern examples:
   
   ```__e``` - words that are 3 characters long and must end with an `e`, for example `rue`;
   
   ```__u_``` - words that are 4 characters long and the 3rd character must be `u`, for example `true`;
    

## Dependencies
This unscrambler heavily depends on [NLTK (Natural Language Toolkit)](https://www.nltk.org/) for the words' dictionary (the list of words).
The list of words might be incomplete, and it is easy to change it.
In the `main.py`, find the 6th line: 

```dictionary = words.words()```

and change it to a list of words of your choice.
