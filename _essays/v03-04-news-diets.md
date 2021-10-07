---
title: "News Diets"
subtitle: "Main Courses and Side Dishes"
doi: "https://doi.org/10.31835/crdh.2020.04"
volume-number: 3
year: 2020
authors:
- last: Hulden
  first: Vilja
  email: Vilja.Hulden@colorado.edu
  affiliation: "Department of History, University of Colorado Boulder"
  orcid: 0000-0002-3812-7010
  url: "https://www.colorado.edu/faculty/hulden-vilja/"
abstract: |
  This article uses topic modeling to examine the "news(paper) diets" served up in the papers read by ordinary early-twentieth-century Americans. In the early twentieth century, a large proportion of the still-mostly-rural American population read what were known as "country weeklies," whose content was dominated by reprinted advertising and news and by local gossip and announcements. "Hard news" content was thus limited, but the practical information and gossip may have meant a closer engagement with the newspaper, and thus also with its news content. Country weeklies are also compared in this article to labor papers (broadly construed). The analysis shows a stark difference between mainstream and labor papers. In hard news topics, stories about strikes rise to the top in labor papers, while being nearly absent in mainstream papers. Labor papers also had far less of the practical information that made the country weekly so crucial to its readership, and none of the local gossip. Thus the labor papers filled an important niche, but one also had to choose to receive them for the news content; unlike the mainstream country weeklies, one did not get labor news as a "side dish" to one's regular fare of train timetables and crop news.
appendix:
- name: README
  file: hulden-v03/README.txt
- name: Data archive
  file: hulden-v03/hulden-data.zip  
- name: Code archive
  file: hulden-v03/hulden-code.zip  
preview: "/assets/img/v03/hulden/preview.png"
---

Newspapers and journalism evoke strong connotations of civic idealism,
self-improvement, and objectivity---ideals that journalists building up
a new professional identity in the early twentieth century increasingly
embraced. Yet other, perhaps less quintessentially middle-class,
traditions of journalism remained alive and well. Most strikingly,
small-town and rural weeklies that tended to hew to an older culture of
openly partisan journalism far outnumbered metropolitan dailies on their
way to professionalization. In addition, various groups had their own
newspaper landscapes: there were African American papers, immigrant
papers (in English as well as in other languages), and a significant
number of working-class papers that provided vociferous advocacy.[^1]

The contents of newspapers can tell us about much more than news.[^2]
This article aims to provide a glimpse into the "news(paper) diets"
served up in the papers read by ordinary early-twentieth-century
Americans. It considers two separate sets of material. One set consists
of 12 country weeklies published in Missouri in 1906--1907. The other
contains 16 papers published in 1909-1911: four labor papers, each from
a different state, and twelve "mainstream" papers, published in towns
nearby the labor papers' place of publication.[^3] Using topic modeling,
this paper takes a birds-eye view of the content in such papers,
comparing the content along two main axes: national vs. local (for the
Missouri set) and labor vs. mainstream (for the labor paper set). It
finds that for both local country weeklies and labor papers, the content
on politics, accidents, and other current events that we conceptualize
as "the news" was very much a side dish rather than the main course. The
country weeklies provided a plethora of practical information and
entertainment that drew the readers to subscribe to and open the paper,
and once they did, they probably read the news as well, especially as
these papers were generally only eight pages total. The labor papers, on
the other hand, provided news that was not available elsewhere, and put
that news in the context of advocacy for labor causes. Neither hewed
particularly to a standard of journalistic objectivity. Rather than
undermining readers' engagement with the news, however, both arguably
contributed to a more informed and engaged public in different ways: one
by providing news as a side dish to important local information, and the
other by making the news it provided part of a movement and a world
view.

### The National vs. the Local

The study of the national vs. the local news presented here relies on
reprint detection and topic modeling.[^4] The reprint detection was
carried out in the full content of [Chronicling America](https://chroniclingamerica.loc.gov/) for the years 1906--1907, though for feasibility the analysis here makes use of a smaller subset---twelve papers published in Missouri. Like many early-twentieth-century small-town and country weeklies, many of these Missouri papers contained substantial amounts of material that was not original but that was also printed in other papers. Indeed, that such papers were able to survive at all was probably due largely to the existence of two forms of distributing material that entailed substantial savings in typesetting expenses: readyprint and boilerplate. Readyprint was simply newsprint paper that was pre-printed on one side. Often, because of advertising that came with the readyprint, the cost of readyprint barely exceeded the price for blank newsprint. Boilerplate or plate matter (which could be used instead of or in addition to readyprint) referred to pre-typeset metal sheets that could be cut and rearranged by the publisher as he pleased, by story or even by paragraph.[^5]

A combination of a topic modeling and reprint detection reveals quite a
stark national-local contrast both in the type of advertisements and in
the type of news. Running a topic model on all the material while
preserving information about which snippet of text comes from which
paper as well as whether the snippet comes from the reprint set, and
then processing the resulting composition file to aggregate the
information by reprint/full material and by newspaper, one can create a
file showing the average weight of each topic in each newspapers' full
("local-heavy") material as well as each newspapers' reprint material.
Figure 1 displays the breakdown of topics (with some topics, like those
consisting of OCR junk, removed) sorted by their prominence in
local-heavy vs. reprint material.

{% figure caption: "Figure 1. Prominence of different topics, sorted by reprint/full material. The length of the bar indicates the size of the difference; the calculation is (average of topic weight in all material)-(average of topic weight in reprint material). Note: the full material serves as a proxy for local-heavy material (it is not feasible to remove reprints from the full material). Topic labels by author. Note the differences. Both sets of materials have quite a lot of ads, though it is clear that some products (Uneeda Biscuit, Postum, Lydia Pinkham's remedies) have become national brands, while others (such as clothing, mostly not yet brand-named) are sold and advertised locally. Of news-like material, the most prominent topic in the reprint material concerns ballots and election candidates, while personal news is clearly dominant in local-heavy material (although, to be sure, an election-related topic is also the top 'hard news' topic in the local-heavy material)." %}
![Two horizontial bar charts. The first shows the topics most prominent in all materials ('local'). The second shows the topics most prominent in all reprints ('national').]({{site.url}}/assets/img/v03/hulden/figure1.png)
{% endfigure %}

Topics that are roughly equally prominent in both reprint and full
material are not particularly revealing: they include general news about
accidents, deaths, government regulations, and legislatures, as well as
food recipes and a few categories of ads (shoes, professional services,
and the like). If one contrasts topics that are prominent in only one
set (either reprint material or full material but not both), however,
one is struck by how little a newspaper's local function had to do with
the news. Although there are a few news topics that are prominent in the
news material (elections, reports on events and visitors, and some news
about foreign policy and immigration), the vast majority of locally
prominent topics have to do with local gossip, general entertainment,
and practical information. Thus (apart from advertisements), the top
topic is personal news ("Mrs. Jones' cousin is visiting from Seattle,
Washington"; "Mr. and Mrs. Smith are pleased to announce the engagement
of their daughter to Mr. Brown of Chicago"), while the next most
prominent topic is fiction and jokes, followed by announcements about
club meetings, train timetables, and classifieds about sale of horses
and farm equipment and livestock.[^6]

{% figure caption: "Figure 2. Topics characteristic of full ('local-heavy') material. Each row is a topic, each column is a newspaper. The darker the cell the more prominent the topic represented by that cell in the respective topic / paper / material combination. Each newspaper is represented twice, once for the full material (which serves as a proxy for local-heavy material) and once for reprint-only material. Sorting of material top to bottom so that top contains material most characteristic of the full material and least characteristic of the reprint material. The figure illustrates that although some topics like foreign policy or farm & DIY advice show a fair amount of crossover, others diverge significantly: personal news, dominant in local material, is (unsurprisingly) barely present in reprints, for instance, and while fiction and stories is present in reprints, it is much more prominent in the full material." %}
![Heat map showing the topics most prominent in all materials ('local') vs. reprints ('national').]({{site.url}}/assets/img/v03/hulden/figure2.png)
{% endfigure %}

This emphasis on local gossip and practical information is, I believe,
more important than it looks at first glance. It highlights the role of
the newspaper as both a necessary source of practical
information---information that has nothing to do with one's commitment
to being an informed citizen, but that is simply useful as one goes
about one's daily business. That this information came from the (weekly)
*newspaper*, which then probably proceeded to sit on the kitchen table
for most of the week, to be leafed through at odd moments of the day,
meant that in getting such information, one also got basic national and
regional news. Thus staying at least somewhat informed happened without
much conscious effort, without a particular civic goal in mind. Given
that in people's busy lives, things civic requiring extra effort easily
fall by the wayside, this may be quite important.

Meanwhile, the local gossip as well as the information on club and
church meetings contained in the paper underlines the role of the
newspaper as the glue of local community, something that can also be
important in somewhat surprising ways. As Theda Skocpol and Vanessa
Baird (and, from a somewhat different angle, Robert Putnam) have
emphasized, the mundane organizational and community life that was much
more prominent in the America of the nineteenth and first half of the
twentieth century than it is now had multiple social and political
consequences that, while not necessarily always noticed by scholars as
significant, may have given ordinary citizens a stronger understanding
of themselves *as* citizens and as political actors.[^7]

The emphasis on community-building is particularly prominent in the two
African American papers in the sample. As Figure 3 shows, the African
American papers had a distinctive focus on club and lodge meeting
announcements, topics related to family and religion, and church meeting
announcements. It is also worth noting that the papers emphasized
education and self-improvement (the topic is a mix of advertisements and
news items) and news and ads about business opportunities, underlining
the role of the African American press in "uplifting the race" and
promoting upward mobility.[^8]

{% figure caption: "Figure 3. Topics characteristic of African American papers in sample (n=2). Each row is a topic, each column is a newspaper. Each newspaper is represented twice, once for the full material and once for reprint-only material. Sorting of material top to bottom so that top contains material most characteristic of the material in the two African American papers; calculation (average of topic in African American papers) -- (average of topic in all other papers). Note how the top topics reflect an emphasis on community and uplift." %} ![Heat map showing the topics most prominent in African American newspapers.]({{site.url}}/assets/img/v03/hulden/figure3.png)
{% endfigure %}

### Labor vs. Mainstream

While the topic distribution in the non-labor papers had a similar focus
on personal news, fiction, general news, and advertisements, the mix of
topics in the labor papers was quite different.[^9]

{% figure caption: "Figure 4. Top topics by average in all material *except* labor. News and editorial topics in **bold**, topics containing a mix of notices/advertising and news/editorials in ***bold italic***. Each square represents the strength of a topic in a particular newspaper title; the darker the square, the more prominent the topic was in that title. Note especially the prominence of personal news in non-labor material and its almost complete absence in labor material." %} ![Heat map showing the topics most prominent in non-labor materials.]({{site.url}}/assets/img/v03/hulden/figure4.png)
{% endfigure %}

As Figure 5 shows, news about strikes dominates the papers, along with
news about labor and socialism, and the categories of "analysis,
principles, ideals" (a mix of editorial-type material, reports of
speeches, et cetera, that cultivates the fairly flowery language often
common in political rhetoric and laying out of first principles[^10])
and the category of "political demands," which contains Socialist Party
platforms and political demands of labor federations.

{% figure caption: "Figure 5: Topics most characteristic of the labor material. News and editorial topics in **bold**, topics containing a mix of notices/advertising and news/editorials in ***bold italic***. Each square represents the strength of a topic in a particular newspaper title; the darker the square, the more prominent the topic was in that title. Note especially the starkly disproportionate reporting on strikes in labor papers, and the near-absence of the topic from mainstream papers. Note also the prominence of the 'analysis, principles, ideals' topic." %} ![Heat map showing the topics most prominent in labor materials.]({{site.url}}/assets/img/v03/hulden/figure5.png)
{% endfigure %}

The differences in topics underline the extent to which the labor press
distributed news ignored or slighted by the mainstream press. The labor
press provided news about strikes; it offered a forum for discussing
labor's political demands; it (sometimes) represented the viewpoint of
the Socialist Party; and it invested heavily in adding labor's vision to
the mix of political rhetoric (represented by the "analysis, principles,
ideals" topic).

At the same time, the labor press did not provide the daily news, nor
did it provide the all-important non-news practical information and
gossip about the local community that probably prompted at least as many
subscriptions to a country weekly as did a desire for news. That is, the
labor paper was explicitly *in addition to* rather than *in lieu of* a
more mainstream publication. The labor paper gave its reader the labor
news; it did not let them know that the city council had decided on a
new road, that Mrs. Jones' cousin was visiting, that farmer Smith was
selling his cow, or that the trains to Chicago had a new schedule.

### Conclusion

Most newspapers in the early twentieth century were only secondarily
about the news. The country weeklies that dominated the
early-twentieth-century newspaper landscape served as a community glue
of sorts: filled with mundane but locally important information, they
served the news on the side. Yet the news they served mattered; in all likelihood, the local paper's content formed the bulk of the news its readers consumed. And
thus, while the labor papers created a different community, one more
widely dispersed in geography but limited to those who identified as a
worker, the labor papers faced an additional hurdle to delivering their
news: a person had to actually want that news. It was not served on the
side of the necessary crop price or train timetable information.

As journalism scholars have noted, the rise of the objective ideal in
journalism did not necessarily benefit democracy: with a mandate to
report "just the facts," the journalist lost some of the footing that
partisan affiliation or explicit issue advocacy had provided for an
independent, vigorous questioning of democratically elected
officials.[^11] Somewhat analogously, as country weeklies and niche
papers (not only the labor press but also the farm press and the
immigrant press) declined and the newspaper became more and more about
the news, one could argue that the very impersonality of such "news"
made for a readership less likely to pay attention.

---

### Bibliography

Baldasty, Gerald J. *The Commercialization of News in the Nineteenth Century*. Madison, WI: University of Wisconsin Press, 1992.

Baldasty, Gerald J., and Mark E. LaPointe. "The Press and the African-American Community: The Role of the 'Northwest Enterprise' in the 1930s." *The Pacific Northwest Quarterly* 94, no. 1, (Winter 2002): 14--26.

Bekken, Jon. "'No Weapon so Powerful': Working-Class Newspapers in the United States." *Journal of Communication Inquiry* 12 (1988): 104--19. <https://doi.org/10.1177/019685998801200208>.

Bekken, Jon. "The Working-Class Press at the Turn of the Century." In *Ruthless Criticism: New Perspectives in U.S. Communication History*, edited by William S. Solomon, and Robert W. McChesney, 151--75. Minneapolis, MN: University of Minnesota Press, 1993.

Blevins, Cameron. "Space, Nation, and the Triumph of Region: A View of the World from Houston." *Journal of American History* 101, no. 1 (June 2014): 122--47. <https://doi.org/10.1093/jahist/jau184>.

Fowler, Nathaniel C., Jr. *The Handbook of Journalism: All About Newspaper Work*. New York: Sully and Kleinteich, 1913.

Fry, John J. *The Farm Press, Reform, and Rural Change, 1895--1920*. New York: Routledge, 2005. <https://doi.org/10.4324/9780203958650>.

Gaines, Kevin K. *Uplifting the Race: Black Leadership, Politics, and Culture in the Twentieth Century*. Chapel Hill, NC: The University of North Carolina Press, 1996. <https://doi.org/10.5149/uncp/9780807845431>.

Herman, Edward S., and Noam Chomsky. *Manufacturing Consent: The Political Economy of the Mass Media*. New York: Pantheon Books, 1988.

Jacobs, Ronald N. *Race, Media and the Crisis of Civil Society: From Watts to Rodney King*. New York: Cambridge University Press, 2004. <https://doi.org/10.1017/cbo9780511489211>.

Kaplan, Richard L. *Politics and the American Press: The Rise of Objectivity, 1865--1920*. New York: Cambridge University Press, 2001.

Kuypers, Jim A. *Partisan Journalism: A History of Media Bias in the United States*. New York: Rowman & Littlefield, 2014.

Pawley, Christine. *Reading on the Middle Border: The Culture of Print in Late-Nineteenth-Century Osage, Iowa*. Boston: University of Massachusetts Press, 2001.

Putnam, Robert. *Bowling Alone: The Collapse and Revival of American Community*. New York: Simon & Schuster, 2000.

Shore, Elliot, Ken Fones-Wolf, and James P. Danky, eds. *The German-American Radical Press: The Shaping of a Left Political Culture ,1850--1940*. Urbana, IL: University of Illinois Press, 1992.

Skocpol, Theda. *Diminished Democracy: From Membership to Management in American Civic Life*. Norman, OK: University of Oklahoma Press, 2003.

Tebbel, John. *The Compact History of the American Newspaper*. 2nd ed. New York: Hawthorn Books, 1969.

Teel, Leonard Ray. *The Public Press, 1900--1945*. Westport, CT: Praeger Publishers, 2006.

United States House of Representatives, Committee on the Judiciary. *Trust Legislation. Western Newspaper Union, Parts 1--3*. Washington, D.C.: Government Printing Office, 1912.

Vesanto, Aleksi, Asko Nivala, Heli Rantala, Tapio Salakoski, Hannu Salmi, and Filip Ginter. "Applying BLAST to Text Reuse Detection in Finnish Newspapers and Journals, 1771--1910." In *Proceedings of the NoDaLiDa 2017 Workshop on Processing Historical Language*, 54--58. Linköping University Electronic Press, 2017. <http://www.ep.liu.se/ecp/133/010/ecp17133010.pdf>.

Vesanto, Aleksi, Asko Nivala, Tapio Salakoski, Hannu Salmi, and Filip Ginter. "A System for Identifying and Exploring Text Repetition in Large Historical Document Corpora." In *Proceedings of the 21st Nordic Conference on Computational Linguistics, NoDaLiDa, 22-24 May 2017, Gothenburg, Sweden*, 330--33. Linköping University Electronic Press, 2017. <http://www.ep.liu.se/ecp/article.asp?issue=131&article=049&volume=>.

---

### Notes

[^1]: Around World War I, there were some 14,500 weeklies, and hundreds of labor papers. The figure for labor papers is obviously a more complex question; here I am relying on Bekken, "The Working-Class Press"; Bekken, "'No Weapon so Powerful'." The number 14,500 appears in e.g. Tebbel, *The Compact History of the American Newspaper*. In the OCLC Newspaper Union List database there are far more weeklies listed for 1910, but there is substantial duplication due to the titles of papers changing and publication date information being spotty: <https://chroniclingamerica.loc.gov/search/titles>.

    On the middle-class associations of newspapers, see especially Pawley, *Reading on the Middle Border*. The theme of the rise of objectivity is discussed in many of the standard works on American journalism. See e.g. Teel, *The Public Press, 1900--1945*. Of course, there is significant debate about whether and how the press ever achieved the ideal of objectivity, and to what extent any major daily at a given moment was beholden to various economic powers. For two more or less opposite takes on the question, see Herman and Chomsky, *Manufacturing Consent*; Kuypers, *Partisan Journalism*.

[^2]: For a good example, see Blevins, "Space, Nation, and the Triumph of Region."

[^3]: Missouri papers were used as a case study here because Chronicling America contains a nice selection of Missouri papers of differing affiliations, and because Missouri sits at the intersection of east and west as well as north and south both geographically and, to some extent at least, culturally as well. The sample contains the full run of 12 papers from 1906--1907; five of the papers are affiliated with the Republican Party, four with the Democratic Party, one with the Socialist Party, and two are African American papers without an explicit party affiliation.

    The data set used for the labor vs. mainstream press analysis consists of the full run of 16 newspapers for the years 1909--1911. The papers include 4 labor papers published in four different states (Minnesota, Washington, West Virginia, and Nebraska) and 12 mainstream papers (2-4 per state from towns nearby the place of publication of the labor papers.) The years for the labor papers were selected because all four papers were in continuous publication in those years (many labor papers were precarious enterprises with fairly short lives.) The definition of a "labor paper" is of course somewhat ambiguous and is used here in a broad sense. Only the *Labor Journal* (WA) was an organ of organized labor, while the other papers here---*Labor Argus* (WV), *Labor World* (MN), and *Wageworker* (NE)---were not formally affiliated with any union, but were run by editors either sympathetic to the movement or members of a particular union.

    The OCR (Optical Character Recognition) quality of these newspapers varies heavily, and (as most newspaper OCR) generally contains a significant amount of errors. Topic modeling, however, is fairly robust with regard to OCR errors.

[^4]: The reprint detection was performed by Aleksi Vesanto at the University of Turku, using the BLAST algorithm that Vesanto et al. have applied to newspaper material more broadly: Vesanto et al., "A System for Identifying and Exploring Text Repetition"; Vesanto et al., "Applying BLAST to Text Reuse Detection."

[^5]: Testimony of Courtland Smith, U.S. House, *Trust Legislation*, 9, 20--21; Fowler, *Handbook of Journalism*; see also Baldasty, *Commercialization of News*, 91--94.

[^6]: There is also a clear difference in advertisements: contrasting national and local materials underlines how some types of products (some food products, patent remedies) had become brand-dependent and nationally advertised while others (clothing) had not.

[^7]: Skocpol, *Diminished Democracy*; Putnam, *Bowling Alone*.

[^8]: See e.g. Baldasty and LaPointe, "The Press and the African-American Community." For a particularly informative discussion of the role of the African American press in supplementing and providing an alternative to mainstream news and of niche media outlets' role in supporting "overlapping, interconnected, and competing public spheres" (also applicable to the labor papers discussion here), see Jacobs, *Race, Media and the Crisis of Civil Society*. On the role of the African American (upper) middle class in developing and deploying a racial uplift ideology, see Gaines, *Uplifting the Race*.

[^9]: Note that all analysis here concerns the full material. No reprint detection was performed for this sample.

[^10]: The list of words most prominently associated with the topic is: people men man great country life good public law power world government american time true things fact human free political.

[^11]: Kaplan, *Politics and the American Press*. For other analyses emphasizing the community and advocacy functions of particular groups of newspapers, see e.g. Fry, *The Farm Press*; essays in Shore, Fones-Wolf, and Danky, *The German-American Radical Press*.
