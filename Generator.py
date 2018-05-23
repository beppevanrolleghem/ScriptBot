import numpy as np
import pandas as pd
import ijson

filename = "OUTPUTFILE.json"
with open(filename, 'r') as f:
    objects = ijson.items(f, 'Episodes.Scenes.item')
    columns = list(objects)

print(columns)
