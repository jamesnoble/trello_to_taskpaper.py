# trello_to_taskpaper.py

trello_to_taskpaper.py is a small utility to take a Trello board in Trello's JSON export format and convert it to a simple TaskPaper list.

## Usage

Export your board to JSON following [these instructions](http://help.trello.com/article/747-exporting-data-from-trello-1).

Once you have your board exported as JSON, run the following:
```
python trello_to_taskpaper.py board.json > board.taskpaper
```
