# reel2obsidian
*Convert saved Instagram reels into individual Obsidian notes.*


**INSTRUCTIONS**

*open the instagram playlist in your browser* 
*and run ctrl+shift+I (dev console)*


here run -->

```
const found = new Set();

setInterval(() => {
  document.querySelectorAll('a').forEach(a => {
    if (a.href.includes('/reel/') || a.href.includes('/p/')) {
      found.add(a.href);
    }
  });

  window.scrollBy(0, 2000);

  console.clear();
  console.log("Collected:", found.size);
}, 1500);

```

*what this does --*

```
scroll
↓
collect links currently visible
↓
store them
↓
scroll again
↓
repeat
```

Because we store them in a Set, duplicates disappear automatically.

After scrolling through the whole playlist {you may wanna scroll twice just to make sure you captured all of them}

Stop it with:
```
Ctrl + C
```

Run this in the console:
```
copy([...found].join('\n'))
```

*now all the links are in your clipboard*


**If copy() doesn’t work**

(Some browsers occasionally decide to be difficult.)

Run:

```
console.log([...found].join('\n'))
```
Then:

Right-click the console output

Copy string contents




*finally*

run

```
python3 node_generator.py 


```


*a new reels directory will be created with files for each reel*


**Further**

```
when you save new reels, grab the links of apprioximately where the reels are using the console command and paste the links in reels.md, the node generator checks for previously saved links automatically

```