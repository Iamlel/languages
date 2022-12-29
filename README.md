Find out all the languages used in a directory.

You can use the provided langs.json, or use your own. For example, here is a script to generate a langs.json that is properly formatted for this project, from [language-map](https://github.com/blakeembrey/language-map/blob/main/languages.json).

```python
import json

with open("test.txt", "r") as f:
    langs = json.load(f)

with open("langs.json", "w") as f:
    f.write("{\n")
    for k, v in langs.items():
        if "extensions" in v:
            for e in v["extensions"]:
                f.write(f'  "{e[1:]}": "{k}",\n')
    f.write("}")
```
