## Using highlight to copy code snippets with formatting

#### Install 
```bash
brew install highlight
```

#### Highlight Code 

```bash
highlight -O rtf --font Consolas --font-size 16  --style naivebayes --syntax py snippets2.py | pbcopy
```

#### Paste 

Command + V 


#### Customizing The Themes

I cusyomised my themes in 2 ways 

1) Changing the colour schemes 
2) Customising specific keywords to highlight in the Python language file

1) Changing the colour schemes 

Locate your theme files under this folder

```bash
/usr/local/Cellar/highlight/3.61/share/highlight/themes
```
Example theme: `naivebayes.theme`

2) Customising specific keywords to highlight in the Python language file

For futher customization, also checkout the language definition file in the `langDefs` dir. 
```bash
/usr/local/Cellar/highlight/3.61/share/highlight/langDefs/
```

Example customized language definition: `python.lang` where I added custom keywords to highlight. 

#### References 


* [Highlight Documentation](http://www.andre-simon.de/doku/highlight/en/highlight.php)

