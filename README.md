# CoRe Lab website

Built with Jekyll and hosted on GitHub Pages.

## First-time setup
1. Edit `url` and `baseurl` in `_config.yml`.
2. In the repo go to Settings > Pages, set Source to "Deploy from a branch", branch `main`, folder `/ (root)`.
3. Settings > Actions > General > Workflow permissions: choose "Read and write permissions".
4. Go to the Actions tab, choose "Update publications" and click "Run workflow".

## Adding content
- **Person:** add a file to `_people/` (copy an existing one). `category` must be exactly Members, Affiliate Members, Researchers or Students.
- **Project:** add a file to `_projects/`.
- **News post:** add a file to `_posts/` named `YYYY-MM-DD-title.md`.
- **Publications:** add an `orcid` line to a person's file. The list updates every Monday.
- **Group lead / contact details:** edit the three lines in `_config.yml`.
