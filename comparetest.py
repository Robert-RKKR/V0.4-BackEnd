from posixpath import split
from compare import text1, text2
import difflib

textone = text1.splitlines()
texttwo = text2.splitlines()

test = {
    'compering': []
}

for diff in difflib.context_diff(textone, texttwo):
    test['compering'].append(diff)

for row in test['compering']:
    print(row)

