![Example-TODO](https://img.shields.io/badge/Example--TODO-75%25%206%2F8-green) 
![Example-Checklist-NFR](https://img.shields.io/badge/Example--Checklist--NFR-12%25%205%2F40-red) 


# gha-nfr-checklist-badges

Example USAGE:

1. Create `.md` file with checklist (Look at `examples/` dir)
2. Create `.github/workflows/nfr_on_push.yaml` with content:

```
name: NFR documents changed
on:
  workflow_dispatch:
  push:
    paths:
      - "*.md"
jobs:
  push:
    name: NFR documents changed
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
        with:
          fetch-depth: 0
      - name: Update NFR badges
        uses: dodopizza/gha-checklist-badges@main
        with:
          readme-fname: README.md
          nfr-fnames: ChecklistFileOne.md ChecklistFileTwo.md
          github_token: ${{ secrets.GITHUB_TOKEN }}
```

3. Now, your `README.md` will be automatically updated with auto-generated badges following `ChecklistFileOne.md`/`ChecklistFileTwo.md` changes
