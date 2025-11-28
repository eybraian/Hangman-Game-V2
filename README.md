<h1>Hangman Game</h1>
<h2>Python algorithm making use of SQLite database integration for managing playable words</h2>

<h3>Structure</h3>
<div>  The game was divided into two files, "main.py" and "database_manager.py", so it would be easy to organize code by its function - Main Game Logic and Database Operations. To make this possible, I used OOP Classes systems.</div>
<div> <br> It contains a WordsDatabase table wich contains the columns "word" (TEXT PRIMARY KEY) and "played" (BOOLEAN), tracking words status so each replay could use a brand new table word.</div>
<div> <br> If the game starts without an existing table, it creates one with a selection of sample words.</div>

<h3>Features</h3>
<ul>
  <li>In-Terminal Menu Navigation</li>
  <li>ASCII Art</li>
  <li>Visual Database Interface using Tabulate Library</li>
  <li>Automatic & random word selection, based on non-played database status</li>
  <li>Acess to add/remove playable words and reset word status</li>
</ul>

<h3>Requirements</h3>
<ul><li><h4>"tabulate" package (pip install tabulate)</h4></li></ul>

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![SQLite](https://img.shields.io/badge/database-SQLite-lightgrey.svg)
