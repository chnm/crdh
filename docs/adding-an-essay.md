# Adding a new essay

This is the checklist for publishing a new essay on the CRDH site. The site is built with Hugo (extended, with the Tailwind/PostCSS pipeline). Each essay is a Hugo *page bundle*: a folder under `content/essays/` holding an `index.md` plus every image the essay uses.

## Quick version

```sh
# 1. Scaffold the bundle (adjust the volume, number, and slug)
hugo new essays/v09-02-short-slug

# 2. Fill in the front matter and paste in the body text
$EDITOR content/essays/v09-02-short-slug/index.md

# 3. Drop the images (including preview.png) into the same folder

# 4. Preview
just preview        # or: hugo server --buildDrafts --navigateToChanged
```

Then open <http://localhost:1313/essays/v09-02-short-slug/> and check the essay, the volume listing at `/volume/2026/`, and the home page.

## 1. Name the folder

The folder name is the URL and controls ordering, so get it right before sharing links:

```
content/essays/v<VOLUME>-<NUMBER>-<slug>/
                   ^^        ^^      ^^^^
                   two-digit volume, two-digit essay number, short lowercase slug
```

Examples: `v08-07-louis-xiv-appartement`, `v09-01-unexpected-origins`.

- The URL is `/essays/<folder-name>/` (set by the `permalinks` rule in `hugo.yaml`). Renaming the folder later changes the public URL and breaks the DOI landing page, so treat the name as permanent once the DOI is registered.
- Essays within a volume are listed in *descending* folder-name order, so the `NN` number is what puts the newest essay at the top. Number essays sequentially within the volume.
- Volume numbers are one per year: volume = year − 2017 (2018 is volume 1, 2026 is volume 9).

Running `hugo new essays/<folder-name>` copies the archetype in `archetypes/essays/` into place with the volume, year, and date pre-filled and a starter title derived from the slug.

## 2. Fill in the front matter

Every essay carries this block. All of these fields are used by the templates or the `<meta name="citation_…">` tags that Google Scholar and Zotero read, so none are optional unless marked.

```yaml
---
title: "Unexpected Origins"
subtitle: "Mapping Assisted Female Immigrants to New South Wales"   # optional
doi: "https://doi.org/10.31835/crdh.2026.01"
volume_number: 9
year: "2026"
volume: "2026"
date: 2026-05-12
authors:
- last: Connor
  first: Kimberley G.
  email: kgconnor@wm.edu
  affiliation: "William & Mary"
  orcid: 0000-0003-3803-2764
  url: "https://example.org"          # optional
abstract: |
  One paragraph. Inline HTML such as <em>italics</em> is fine here.
appendix:                              # optional
- name: Data archive
  file: connor-v09/connor-data.zip
preview: "preview.png"
---
```

Field notes:

| Field | What it does |
|---|---|
| `title`, `subtitle` | Rendered as `Title: Subtitle` on listings and the page. HTML such as `<em>` is allowed in both. |
| `doi` | Full URL. Pattern is `10.31835/crdh.<YEAR>.<NN>` where `NN` matches the essay number in the folder name. Shown on the page and in citation metadata. |
| `volume_number` | Integer. Displayed in the citation block and `citation_volume`. Must equal `year − 2017`. |
| `year` | String. Groups the essay on the essays listing page and sets `citation_publication_date`. |
| `volume` | String, same value as `year`. This is the taxonomy term that creates the `/volume/2026/` page. |
| `date` | Online publication date. Sets `citation_online_date` and groups the home page by year, so its year must match `year`. |
| `authors` | List in author order. `last`, `first`, `email`, `affiliation`, `orcid` are used; `url` is optional. |
| `abstract` | YAML block scalar (`|`). Rendered as Markdown, so inline HTML and emphasis work. |
| `appendix` | Optional list of `name`/`file` pairs. Files are **not** in this repo; `file` is a path under `https://crdh.rrchnm.org/appendices/`, so the data has to be uploaded to that server separately. |
| `preview` | Bare filename of an image inside the bundle. Used for the card on listings and the home-page image carousel. Every essay has one; `preview.png` is the convention. |

Do not rely on `draft: true` to hide an unfinished essay. The Docker/CI build runs `hugo --buildDrafts --buildFuture`, so drafts and future-dated essays are published. Keep unfinished essays on a branch instead.

## 3. Write the body

Essays are Markdown with Goldmark's `unsafe` renderer on, so raw HTML works where you need it.

**Headings.** Use `###` for section headings and `####` for subsections. The table of contents in the sidebar picks up `###` headings only. Don't use `#` or `##`; the title already occupies those levels.

**Footnotes.** Standard Markdown footnotes:

```markdown
…as Guldi argues.[^1]

[^1]: Jo Guldi, *The Long Land War* (Yale University Press, 2022), 12.
```

Footnote definitions can live anywhere in the file; putting them at the end keeps the body readable.

**Figures.** Put the image file in the bundle and reference it by bare filename inside the `figure` shortcode:

```markdown
{{</* figure caption="Figure 2: Places of origin, 1848–1887. Map by author." */>}}![Map of the UK with density dots](figure2.png)
{{</* /figure */>}}
```

- The image line must be a Markdown image. Alt text is required for accessibility; the caption does not substitute for it.
- Captions are rendered as Markdown, so `*emphasis*` and links work.
- Figures get sequential ids (`fig-1`, `fig-2`, …) and open in a lightbox on click. You don't need to number them yourself beyond the caption text.
- Keep images web-sized. A few existing figures are 15–20 MB; aim for under 1 MB each (PNG for maps and charts, JPEG for photographs).

**Interactive plots.** There is also a `plot` shortcode that loads Observable Plot, D3, and topojson-client from a CDN and runs the JavaScript you put inside it. `container`, `Plot`, `d3`, and `topojson` are in scope:

```markdown
{{</* plot caption="Figure 3: Arrivals per year." height="400px" */>}}
const data = await d3.csv("arrivals.csv", d3.autoType);
container.append(Plot.plot({
  marks: [Plot.barY(data, { x: "year", y: "count" })]
}));
{{</* /plot */>}}
```

Data files referenced this way must also sit in the bundle. No published essay uses this yet, so test it locally before relying on it.

**Table of contents.** It is on by default. Add `toc: false` to the front matter for a short essay with no section headings.

## 4. Check it locally

```sh
just preview
```

Confirm:

- The essay page renders with title, authors, abstract, DOI, and figures.
- `/essays/` shows the essay under the right volume with its preview image.
- `/volume/<year>/` lists it.
- The home page shows it in the current-volume section.
- `hugo --minify` (or `just build`) completes without warnings about missing resources.

## 5. Register the DOI

The `doi/` folder keeps the Crossref deposit XML for past essays (for example `doi/doi_crdh_vol8_06.xml`). Copy the most recent one, update the article title, authors, ORCIDs, dates, DOI, and landing-page URL to match the front matter, and deposit it with Crossref. The `<resource>` URL must be the essay's final `/essays/<folder-name>/` URL.

## 6. Commit and deploy

Commit the whole bundle (`index.md` and images) together. The site is built from the `Dockerfile`, which runs `npm ci` and then `hugo` with the flags above, so nothing else needs to be generated by hand. `public/` and `resources/_gen/` are build output and should not be committed.

## Reference: an existing essay to copy from

`content/essays/v09-01-unexpected-origins/` is the most recent essay and a good template: three figures, footnotes, `###` headings, and a preview image that reuses one of the figures.
