# pandanistas website

The source is in the `source` branch, while the `master` branch only contains the files generated from the source (the files in the `output` folder in the `source` branch).

Build the content by running:
```
pelican content
```

or

```
make html
```

See the website live at http://localhost:8000/ by running:

```
pelican --listen
```

or

```
make serve
```

Theme is based on <https://github.com/mc-buckets/brutalistpelican/>.

## Publishing to GitHub Pages
Run Pelican to generate the static HTML files in output:
```
pelican content -o output -s publishconf.py
```

Use ghp-import to add the contents of the output directory to the master branch: 
```
 ghp-import -m "Generate Pelican site" --no-jekyll -b master output
```

You can install `ghp-import` by running `pip install ghp-import`. See <https://pypi.org/project/ghp-import/> for more information.

Commit and push the new content to the content branch: 
```
git push origin master
```

Source: <https://opensource.com/article/19/5/run-your-blog-github-pages-python/>