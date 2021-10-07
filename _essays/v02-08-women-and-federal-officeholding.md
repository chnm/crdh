---
title: "Women and Federal Officeholding in the Late Nineteenth-Century U.S."
doi: "https://doi.org/10.31835/crdh.2019.08"
volume-number: 2
year: 2019
date: 2019-08-23
authors:
- last: Blevins
  first: Cameron
  email: c.blevins@northeastern.edu
  affiliation: "Department of History, Northeastern University"
  orcid: 0000-0002-5272-5770
  url: "http://www.cameronblevins.org"
abstract: |
  When and how did American women enter the federal workforce? In order to answer this question I turn to the nineteenth century's largest government institution, the U.S. Post. During the nineteenth century thousands of women served as postmasters. As is often the case for women's history, however, an incomplete archival record makes it difficult to know how many were in office and how that number changed over time. This essay compares three separate data sources to distill that pattern. All three data sources show a similar trajectory: beginning in the 1860s and accelerating through the 1870s and 1880s, many more women began serving as postmasters in the federal government. The nature of the nineteenth-century postal system provided women with a number of advantages for women to step into public office. The wave of female postmasters during the late nineteenth century was a crucial wedge for women's broader entry into the federal government.
preview: "/assets/img/v02/blevins/preview.png"
---

The last decades of the nineteenth century witnessed a surge of women
into the public sphere. Through leadership positions in voluntary
associations, religious groups, and other social reform movements, women
shaped public policies on issues like education, welfare, sanitation,
temperance, and (most famously) women's suffrage.[^1]

They also entered public life through official government positions.
During and after the U.S. Civil War the federal government established a
host of new agencies and initiatives that both expanded its
administrative capacity and swelled the ranks of its workforce. The
pioneering work of historian Cindy Aron has documented how thousands of
largely middle-class women secured some of these new positions, working
as clerks, copyists, and other positions for federal agencies in
Washington, D.C.[^2]

Outside of the nation's capital, however, the picture is much murkier.
When and how did women enter the public sector workforce across the rest
of the country? The answer lies with the federal government's single
largest organization: the Post Office Department.

As is often the case for women's history, the archival record is
frustratingly limited and incomplete. No single source systematically
records the number of women who served in the Post Office Department --
much less the wider federal government -- on a year-by-year basis.
Instead, I turn to three different measurements to try and distill a
larger pattern. On their own, each method is incomplete. Taken together,
however, they point to the same trend: beginning in the 1860s and
accelerating through the 1870s and 1880s, women served as postmasters in
the federal government in ever-increasing numbers. By 1891, roughly ten
percent of the nation's post offices (6,335 in total) were run by
women.[^3] This wave of female officeholders was a crucial wedge for
women's broader entry into public life during the late nineteenth
century.

### Measurement #1: Presidential Appointments

The first measurement comes from a dataset collected by political
scientist Scott James. It contains information about some 49,000 people
appointed by the president and sent to the U.S. Senate for confirmation
between the years 1829 and 1917. The dataset covers many different
federal agencies, but the bulk of these nominations were for so-called
"Presidential" postmasters who managed the nation's large urban post
offices. Using the gender package in the programming language R, I
inferred the gender of these Senate-confirmed appointees based on their
first names. Through 1865, the number of women appointed to these
Presidential postmaster positions never exceeded *five* women in a
single year. By 1895, roughly *fifty-five* women were appointed. This
growth cannot be chalked up to a wider expansion in the federal
workforce. Even when calculated as a percentage of all Presidential
postmaster appointments, the share of women roughly tripled between the
1860s and the 1890s (see figure 1).[^4] 

{% figure caption: "Figure 1. Each year, sitting U.S. Presidents would nominate people to federal office and the Senate would then confirm those nominations. The majority of these appointments were for postmaster positions in large urban post offices (shown here). The share of these nominations that were filled by women roughly tripled between the 1860s and the 1890s, part of a larger entry of women into the postal workforce. The chart was calculated from a dataset provided by Scott James." %}
![Line graph of percentage of women among U.S. Presidential postmaster nominations.]({{site.url}}/assets/img/v02/blevins/figure1.png)
{% endfigure %}

A few notes of caution: these numbers are estimated inferences. They
rely on a computational method that assumes a problematic gendered
binary of naming practices and says absolutely nothing about how
individuals may have identified themselves. Moreover, the gender package
was not able to infer the gender for every name in the dataset. In cases
of uncommon first names ("Selucius Garfield") or initials ("A.P.K.
Safford"), it left the gender unidentified. It is safe to say, then,
that these figures undercount the proportion of women in the dataset.
Finally, these Senate-confirmed appointments were only a tiny fraction
of the nation's total postal workforce. To see if this trend can be
verified, we need to turn to other sources.[^5]

### Measurement #2: State-Level Data

The vast majority---around 95--96%---of postmaster appointments did
*not* require Senate confirmation.[^6] For these offices, the position
of postmaster was rarely a full-time occupation. Instead, a local
private business person (usually a storeowner) would run the post office
out of their storefront or other place of business. For most, the work
was part-time and the pay was modest.

Records for these smaller offices are harder to track. Fortunately,
postal history attracts a number of philatelists and amateur
enthusiasts. In the mid-2000s, a postal historian named Jim Wheat posted
webpages containing transcriptions of every postmaster appointed in the
state of Texas between 1846--1930. I scraped this data from his website,
processed it into a database, and then used the same gender R package to
infer the gender of some 38,500 Texas postmasters. Jim Wheat's dataset
of Texas postmasters shows a similar pattern as Scott James's dataset of
Presidential postmaster appointments, with a steady rise in the share
of female appointees over the final decades of the nineteenth
century (see figure 2).[^7]

{% figure caption: "Figure 2. This chart illustrates the share of all nineteenth-century postmaster appointments in Texas that were held by women. The proportion of women holding postmaster positions briefly spiked and dropped during the political tumult of the U.S. Civil War and Reconstruction before steadily rising from the 1870s to the 1890s. Data compiled from Wheat, “Postmasters & Post Offices of Texas, 1846--1930.”" %}
![Line graph of percentage of women among postmaster appointments in Texas in the nineteenth-century.]({{site.url}}/assets/img/v02/blevins/figure2.png)
{% endfigure %}

There are some telling differences between the two measurements. First,
as shown in the chart in figure 2, the share of women in Texas post
offices spiked during the 1860s and early 1870s. This was due to Texas
joining the Confederate Rebellion, throwing the state's postal system
into temporary flux. When the so-called "ironclad" oath effectively
barred ex-Confederate soldiers from taking public office after the war,
Texas women temporarily stepped into the vacuum.[^8] When loyalty
restrictions eased following Reconstruction, the share of women dropped
back down before climbing steadily over the next two decades.

The second difference between the two datasets was that women generally
made up a larger share of Texas postmaster appointments (10--15% by the
1890s) than they did Presidential postmaster appointments (3--7% by the
1890s). This was due to the fact that there was more competition for the
higher-paying Presidential postmaster positions in Scott James's dataset
compared to lower-paying positions that make up the bulk of Jim Wheat's
dataset.

### Measurement #3: N-Grams

The third measurement for tracking the entry of women in the postal
workforce comes from three large-scale textual databases: the Library of
Congress's *Chronicling America* collection of historical newspapers
along with the digital libraries HathiTrust and Google Books. None of
these databases measure the number of female postmasters directly.
Instead, I used n-grams (the relative frequency of strings of words
within a corpus) as a proxy indicator by tracking the phrase
"postmistress" (postmasters who were women) across the three historical
databases. All three datasets show the same pattern, and one that
mirrors that of the first two datasets: use of the phrase "postmistress"
rose dramatically in printed texts during the 1870s and 1880s. (See
figures 3, 4, and 5.)

{% figure caption: "Figure 3. This chart shows the relative frequency of the term “postmistress” (or female postmaster) in the *Chronicling America* Database of Historical Newspapers from 1840--1900. The chart shows a dramatic increase in the use of this phrase within American newspapers in the late nineteenth century, which likely reflects a real-world phenomenon of more women serving as postmasters. The search term was case-insensitive and the chart uses a three-year smoothing. It comes from a [Bookworm interface for Chronicling America](http://benschmidt.org/ChronAm/#?%7B%22words_collation%22%3A%22Case_Insensitive%22%2C%22search_limits%22%3A%5B%7B%22word%22%3A%5B%22postmistress%22%5D%2C%22publish_year%22%3A%7B%22%24gte%22%3A1836%2C%22%24lte%22%3A1922%7D%7D%5D%7D.) developed by Benjamin Schmidt, Matt Nicklay, Neva Cherniavsky Durand, Martin Camacho, and Erez Lieberman Aiden at the Cultural Observatory. Generated on October 15, 2018." %}
![Line graph of the term “postmistress” in the *Chronicling America* Database of Historical Newspapers, using two million texts and twenty-two billion words.]({{site.url}}/assets/img/v02/blevins/figure3.png)
{% endfigure %}

{% figure caption: "Figure 4. This chart shows the relative frequency of the term “postmistress” in the HathiTrust Digital Library from 1840--1900. Much like the trend in newspapers shown in figure 3, the phrase “postmistress” skyrocketed in popularity from the 1860s onwards in the HathiTrust corpus. The search term was case-insensitive and searched a corpus of English language books published in the United States. The chart uses a three-year smoothing, and comes from a [Bookworm interface for HathiTrust](https://bookworm.htrc.illinois.edu/develop/#?%7B%22search_limits%22:%5B%7B%22word%22:%5B%22postmistress%22%5D,%22date_year%22:%7B%22$gte%22:1840,%22$lte%22:1900%7D,%22language__id%22:%5B%221%22%5D,%22publication_country__id%22:%5B%221%22%5D%7D%5D,%22counttype%22:%22WordsPerMillion%22%7D) developed by Benjamin Schmidt, Matt Nicklay, Neva Cherniavsky Durand, Martin Camacho, and Erez Lieberman Aiden at the Cultural Observatory. Generated on October 15, 2018." %}
![Line graph of the term “postmistress” in the HathiTrust Digital Library, using six hundred and twenty-five thousand texts and one hundred and seventeen billion words.]({{site.url}}/assets/img/v02/blevins/figure4.png)
{% endfigure %}

{% figure caption: "Figure 5. This chart shows the relative frequency of the term “postmistress” as a percentage of all words in Google Books (American English Corpus) from 1840--1900. Similar to figures 2 and 3, this corpus shows a rise in the phrase in the Google Books corpus during the final decades of the nineteenth century. This was likely tied to a real-world phenomenon of more women serving as postmasters. The search term was case-sensitive and searched the Google Books American English corpus. The chart uses a three-year smoothing, and comes from the [Google Books NGram Viewer](https://books.google.com/ngrams/graph?content=postmistress&year_start=1840&year_end=1900&corpus=17&smoothing=3&share=&direct_url=t1%3B%2Cpostmistress%3B%2Cc0). Generated on October 15, 2018." %}
![Line graph of the term “postmistress” in the Google Books American English Corpus.]({{site.url}}/assets/img/v02/blevins/figure5.png)
{% endfigure %}

On their own, the charts in figures 3, 4, and 5 don't tell us all that
much. Compared to the first two datasets, they are a far-removed proxy
measurement for a real-world pattern. The relationship between lexical
use and material changes is fuzzy at best: "postmistress" might have
become a more popular phrase for reasons other than (or in addition to)
the entry of women into the postal workforce. Moreover, all three
databases have their own pitfalls, from corpus coverage to OCR quality.[^9]

Given that this lexical pattern roughly mirrors the trajectory of
postmaster appointments in the first two datasets, however, we can
hypothesize that there was at least *some* connection between them.
Moreover, n-gram measurements give us a slightly different vantage
point. Whether or not they measure an actual rise in postmistresses,
they do indicate that nineteenth-century people were commenting on the
phenomenon of women postmasters more frequently.

### The Big Picture

Like the parable of the blind men and the elephant, none of the above
datasets tell the entire story. Their creators---a political scientist,
an amateur historian, the Library of Congress, HathiTrust, and Google---did not make them in order to track the entry of women into the federal
workforce. They had to be repurposed and reprocessed to answer this
question. In an age of ever-expanding digitized historical material,
stitching together these kinds of seemingly disparate datasets to look
for shared patterns is becoming more and more common. It needs to be
done, however, with a concrete understanding of what is and is not
included in these measurements. And even when a trend *does* emerge,
historians still need to interpret its causes and significance.

What, then, explains the widespread rise of women as postmasters and why
does it matter? The position of postmaster presented a number of
advantages to women hoping to secure a position in government. One
advantage was that the position of postmaster was the most commonly
available federal job. Outside of times of war, the Post Office
Department regularly employed more people than the entire rest of the
executive, judicial, and legislative branches combined.[^10] Moreover,
because postmasters were typically linked to party patronage and
electoral politics, turnover in office was common. Whichever party
controlled the presidency had the power to dismiss and appoint most of
the nation's postal workforce. This meant that every changeover in the
executive branch brought a wave of removals and resignations in the
nation's post offices. (See figure 6.) Although the carousel of partisan
patronage wasn't good for job security, it did give women many more
opportunities to jump on board.

{% figure caption: "Figure 6. New presidential administrations would often remove officeholders in the Post Office Department and dispense their positions as patronage to party loyalists. These partisan purges of the postal workforce followed the 1884, 1888, 1892, and 1896 elections that flipped the presidency between Republicans and Democrats. Annual figures were transcribed from *Annual Reports of the Postmaster General*, 1865--1900, with each year reflecting the *previous* fiscal year running from July to June. For example, 1886 represents removals from July 1, 1885 to June 30, 1886." %}
![Bar chart showing the number of postmasters removed during each presidential administration from eighteen sixty-five to nineteen hundred.]({{site.url}}/assets/img/v02/blevins/figure6.png)
{% endfigure %}

The second advantage had to do with the job itself. Unlike today, most
post offices were an extension of the postmaster's private business or
residence. Many of them consisted of little more than the cluttered
corner of a general store. This meant that postmasters themselves were
seen as a hybrid of private citizens and public officeholders. This
blurring between private and public gave women an opening in which to
step into public office without representing a wholesale transgression
of traditional gendered boundaries. This was especially true if the post
office itself was housed within the postmaster's home, a space over
which women held traditional authority.[^11] The nature of the work
helped as well. Postmasters did not wield regulatory or coercive power.
They were not tax collectors or constables, instead acting as vendors
who provided a popular public service. This made local communities
generally more comfortable with a woman holding the position---even as
writers lampooned postmistresses as gossiping busybodies and newspapers
never tired of making endless puns about their ability to handle both
"the mails" and "the males."[^12]

The entry of women into these offices represented a quiet yet important
initial foray into public officeholding for women who were eager to take
on official roles in government and politics. The position may have paid
poorly, but it did come with benefits. It carried a certain degree of
prestige: small-town postmasters were often seen as "local notables" on
par with a sheriff or justice of the peace. Post offices were also
clearinghouses of information where people would regularly congregate to
exchange news and gossip. Postmasters knew what magazines or newspapers
their neighbors subscribed to, which parties and organizations they
belonged to, and who they were communicating with. Finally, given the
partisan nature of the position, securing an appointment required the
officeholder to lobby local and national politicians. This gave women a
chance to establish channels of communication and develop important
relationships that they could then turn towards other sorts of public
pursuits.[^13]

Finally, the sheer ubiquity of postmasters---numerically and
geographically---meant that the position was one of the most common
ways in which Americans first caught a glimpse of a woman serving in
federal office. This early wave of public officeholding helped normalize
the idea of women holding official government positions. Although a
small-town postmaster was an unelected position with limited
responsibilities, it nevertheless paved the way for women to take on
larger roles in federal government. In 1920, for instance, Oklahoma
voters elected Alice Mary Robertson to the U.S. House of Representatives
just a few months after the passage of the Nineteenth Amendment, making
her the second woman to serve in U.S. Congress. It was not, however,
Robertson's first time to hold federal office. A decade before, she had
run the post office in Muskogee as an official U.S. postmaster. She was
far from alone.[^14]

{% figure caption: "Figure 7. Alice Robertson was the postmaster of Muskogee, Oklahoma, from 1905--1913 before she was elected Congresswoman from Oklahoma in 1920." Image: "Alice Robertson, 1922." Library of Congress.%}
![Photograph of Alice Robertson in old age, seated with papers on a table in front of her.]({{site.url}}/assets/img/v02/blevins/figure7.jpg)
{% endfigure %}

---

### Bibliography

Aron, Cindy. *Ladies and Gentlemen of the Civil Service: Middle-Class Workers in Victorian America*. Oxford University Press, 1987.

Blevins, Cameron. *Gossamer Network: The U.S. Post and State Power in the American West*. New York: Oxford University Press, *forthcoming*.

Boggs, Mae Helene Bacon. *My Playhouse Was a Concord Coach: An Anthology of Newspaper Clippings and Documents Relating to Those Who Made California History During the Years 1822--1888*. Oakland, CA: Howell-North Press, 1942.

Cushing, Marshall Henry. *The Story of Our Post Office*. Boston, Mass: A. M. Thayer & Co., 1893.

Edwards, Rebecca. *Angels in the Machinery: Gender in American Party Politics from the Civil War to the Progressive Era*. New York: Oxford University Press, 1997.

Foss, Sam Walter. "The Postmistress of Pokumville." In *Dreams in Homespun*, 180--82. Boston: Lee & Shepard, 1898. <http://books.google.com/books?id=YiQ-AAAAYAAJ&pg=PA180>.

Gilmore, Glenda Elizabeth. *Gender and Jim Crow: Women and the Politics of White Supremacy in North Carolina, 1896--1920*. Chapel Hill: University of North Carolina Press, 1996.

Greenwald, Maurine Weiner. "Working-Class Feminism and the Family Wage Ideal: The Seattle Debate on Married Women's Right to Work, 1914--1920." *The Journal of American History* 76, no. 1 (1989): 118--49. <https://doi.org/10.2307/1908346>.

James, Scott C. "Patronage Regimes and American Party Development from 'The Age of Jackson' to the Progressive Era." *British Journal of Political Science* 36, no. 1 (2006): 39--60. <https://doi.org/10.1017/S0007123406000032>.

Library of Congress. "Alice Robertson, 1922." Photographic Print, National Photo Company
Collection. No. 17381 (January 3, 1922). <https://lccn.loc.gov/2002697188>.

"Males and Mails." *The United States Mail* 3, no. 33 (June 1887): 122.

Mullen, Lincoln, Cameron Blevins, and Ben Schmidt. *Gender: Predict Gender from Names Using Historical Data* (version 0.5.2), 2018. <https://CRAN.R-project.org/package=gender>.

Painter, Nell Irvin. *Standing at Armageddon: A Grassroots History of the Progressive Era*. W. W. Norton & Company, 1987.

Pechenick, Eitan Adam, Christopher M. Danforth, and Peter Sheridan Dodds. "Characterizing the Google Books Corpus: Strong Limits to Inferences of Socio-Cultural and Linguistic Evolution." *PLOS ONE* 10, no. 10 (October 7, 2015): e0137041. <https://doi.org/10.1371/journal.pone.0137041>.

Richter, William L. "'We Must Rubb Out and Begin Anew': The Army and the Republican Party in Texas Reconstruction, 1867--1870." *Civil War History* 19, no. 4 (1973): 334--52. <https://doi.org/10.1353/cwh.1973.0041>.

Rubin, Anne Sarah. *A Shattered Nation: The Rise and Fall of the Confederacy, 1861--1868*. Chapel Hill: University of North Carolina Press, 2005.

United States. *Annual Reports of the Postmaster General*. Washington, D.C.: Government Printing Office, 1865--1900.

United States Congress. *Official Register of the United States*. Washington, DC: Government
Printing Office, 1865--1899.

United States Congress. "Robertson, Alice Mary." In *Biographical Directory of the United States Congress: 1774-present*. Accessed October 15, 2018. <http://bioguide.congress.gov/scripts/biodisplay.pl?index=R000318>.

Wallis, John Joseph. "Table Ea894-903 -- Federal Government Employees, by Government Branch and Location Relative to the Capital: 1816--1992." In *Historical Statistics of the United States, Earliest Times to the Present*, edited by Susan B. Carter, Scott Sigmund Gartner, Michael R. Haines, Alan L. Olmstead, Richard Sutch, and Gavin Wright. New York: Cambridge University Press, 2006.

Wheat, Jim. "Postmasters & Post Offices of Texas, 1846--1930." December 28, 2006. Accessed January 10, 2013. <http://sites.rootsweb.com/~txpost/postmasters.html>. 

---

### Notes

[^1]: Painter, *Standing at Armageddon*, 62--64, 231--35; Edwards, *Angels in the Machinery*, 12--58; Gilmore, *Gender and Jim Crow*, 31--60.

[^2]: Aron, *Ladies and Gentlemen of the Civil Service*.

[^3]: Cushing, *Story of Our Post Office*, 442--43; “1891 Annual Report of the Postmaster General,” 265.

[^4]: Many thanks to Scott James for providing his dataset: James, “Patronage Regimes and American Party Development from ‘The Age of Jackson’ to the Progressive Era.” Gender was inferred using: Mullen, Blevins, and Schmidt, *Gender*.

[^5]: The gender package was able to infer the gender of 41,520 appointees between 1840--1900, or 97.5% of all names for this period.

[^6]: In 1871, 96% of the post offices were fourth-class offices. “1871 Annual Report of the Postmaster General,” 85. In 1899, 94.4% of post offices were fourth-class offices. “1899 Annual Report of the Postmaster General,” 822--823.

[^7]: Varun Vijay helped process this data while working as an undergraduate Research Assistant at the Stanford Center for Spatial and Textual Analysis during the spring of 2015. Wheat, “Postmasters & Post Offices of Texas, 1846--1930.” I conducted a similar state-level analysis of Oregon during this same period, using bi-annual data from The *Official Register of the United States* that lists the names of every federal employee. This analysis showed a similar pattern: the proportion of postmasters who were women increased roughly fivefold from the 1870s to the 1890s.

[^8]: Richter, “We Must Rubb Out and Begin Anew,” 348--50. For the larger context of “loyalty oaths” in the South, see Rubin, *A Shattered Nation*, 164--71.

[^9]: Pechenick, Danforth, and Dodds, “Characterizing the Google Books Corpus.”

[^10]: Wallis, “Table Ea894-903.”

[^11]: The blurring of different kinds of work space and the opportunities this has provided for women can be seen especially clearly during times of war. See, for instance, Edwards, *Angels in the Machinery*, 12--38; Greenwald, “Working-Class Feminism and the Family Wage Ideal.”

[^12]: Foss, “The Postmistress of Pokumville.” For “mails/males” jokes, see *Trinity Journal* (Yreka, CA), March 22, 1873, quoted in Boggs, *My Playhouse Was a Concord Coach*, 584; “Males and Mails.”

[^13]: I explore the nineteenth-century U.S. Post in more detail in my forthcoming book, Blevins, *Gossamer Network*.

[^14]: United States Congress, "[Robertson, Alice Mary](http://bioguide.congress.gov/scripts/biodisplay.pl?index=R000318)."
