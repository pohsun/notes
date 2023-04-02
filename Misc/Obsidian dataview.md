[Dataview official doc](https://blacksmithgu.github.io/obsidian-dataview/)

Here is the simplest way to collect a list from tags
```dataview
LIST
FROM #ZZZ/index
SORT file.mtime DESC
```

Or you could express it as a table 

```dataview
TABLE file.tags AS "Tags", file.mday AS "Last Modified"
FROM #CS/Lang/Python OR #CS/DSA/ML 
```