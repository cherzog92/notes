import os
import json
import re
from tinydb import TinyDB, Query

#initialize database
db = TinyDB("notes_tinydb.json")


#get the list of notes
def get_notes(search=None):
    global db
    query = Query()
    if search:
        the_notes = db.search(query.text.matches(".*"+search+".*", flags=re.IGNORECASE))
    else:
        the_notes = db.all()
    print(the_notes)
    for n in the_notes:
        n['id'] = n.doc_id
    #the_notes = [n["text"] for n in the_notes]
    return the_notes

# add a note to the list of notes
def add_note(note):
    global db
    db.insert({"text":note})
    return id

# delete a note
def delete_note(id):
    global db
    try:
        db.remove(doc_ids = [id])
    except KeyError:
        pass
