from posixpath import split
from compare import text1, text2
import difflib

textone = text1.splitlines()
texttwo = text2.splitlines()

test = {
    'compering': []
}

# for diff in difflib.context_diff(textone, texttwo):
#     print(diff)

d = difflib.Differ()
diff = d.compare(textone, texttwo)
print('\n'.join(diff))
