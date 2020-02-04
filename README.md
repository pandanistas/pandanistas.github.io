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

Theme is based on <https://github.com/mc-buckets/brutalistpelican/>