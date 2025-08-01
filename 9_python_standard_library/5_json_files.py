# popular way to to format data in a human readable way
import json
from pathlib import Path

# movies = [
#     {
#         "id":1,
#         "title":"Terminator",
#         "year":"1994"
#     },
#     {
#         "id":2,
#         "title":"Terminator 2",
#         "year":"1994 "
#     }
# ]

# data = json.dumps(movies)
# print(data)

# Path("9_python_standard_library/ecommerce/movies.json").write_text(data)

data = Path("9_python_standard_library/ecommerce/movies.json").read_text()
movies = json.loads(data)  # parse the data string as json
print(movies)