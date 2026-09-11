---
title: "{{ replace (replaceRE "^v\\d+-\\d+-" "" .File.ContentBaseName) "-" " " | title }}"
subtitle: ""
doi: "https://doi.org/10.31835/crdh.{{ now.Format "2006" }}.NN"
volume_number: {{ sub (int (now.Format "2006")) 2017 }}
year: "{{ now.Format "2006" }}"
volume: "{{ now.Format "2006" }}"
date: {{ now.Format "2006-01-02" }}
authors:
- last: ""
  first: ""
  email: ""
  affiliation: ""
  orcid: ""
  url: ""
abstract: |
  One-paragraph abstract. Inline HTML such as <em>italics</em> is allowed.
# appendix:
# - name: "Data archive"
#   file: "lastname-vNN/data.zip"
preview: "preview.png"
---

Opening paragraph.

### First Section Heading

Body text with a footnote.[^1]

{{< figure caption="Figure 1: Caption text. Markdown and *emphasis* allowed." >}}![Alt text describing the image](figure1.png)
{{< /figure >}}

[^1]: Footnote text.
