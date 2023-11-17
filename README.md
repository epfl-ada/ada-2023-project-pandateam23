# Actors Representation: Actor’s Recognition, Gender and Ethnicity throughout history and time 📆

## Abstract 
In the enthralling world of cinema 🎥, actors play a pivotal role, shaping and being shaped by the ever-evolving tapestry of human history. Embark with us on a cinematic journey through time as we explore actor’s recognition and their evolving representation in the world of cinema across history. Has an actor's recognition and its longevity been influenced by specific attributes such as genre, ethnicity?  Acting isn't an isolated art form but rather intricately connected to the tapestry of human existence, always influenced and shaped by historical events. Our objective is to decode the impact of pivotal historical events, such as the Civil Rights and Feminist Movements, on the composition of actors in terms of gender and ethnicity. This project invites you on a cinematic journey delving into the life of actors who have graced the Cinema screens, examining how they have been portrayed, known and represented over time.

## Research Questions 🔎
1. How do age, gender, the genre of movies in which an actor has played, and ethnicity influence the attainment and magnitude of an actor’s recognition?
2. Can specific patterns be identified regarding an actor's recognition longevity based on factors such as age, gender, ethnicity, and the genres of movies in which they have participated?
3. To what extent have historical events, particularly the Civil Rights Movement and the Feminist Movement, influenced the composition of actors in terms of ethnicity and gender?
4. In what ways have trends related to an actor's recognition and longevity evolved over time, considering changing societal norms and historical events? Meaning have age, gender, ethnicity, and the genre of movies of recognized actors evolved over time?
5. How have changes in the representation of actors in cinema, resulting from historical events, affected the Box Office performance of movies? Is there a discernible correlation between shifts in representation due to historical events and the financial success or failure of movies at the Box Office?

## Additional Datasets 📉
- [IMDb Movies Dataset](https://developer.imdb.com/non-commercial-datasets/): To diversify the definition of movie success beyond financial terms, we aim to incorporate IMDb data. Two datasets, namely `title.basics.tsv.gz` and `title.ratings.tsv.gz`, will be utilized. The former includes movie name, release year, and runtime, enabling integration with our movie dataset. The latter provides average ratings and the number of votes received, offering a qualitative measure of success.
- [World Bank](https://www.worldbank.org/en/research/brief/inflation-database): To accurately assess changes in the real value of movie budgets and box office revenue over time, we propose incorporating inflation rates data from the World Bank into our analysis. `inflation.xlsx` contains inflation rates by country and over the timespan 1970-2022.
- [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&select=movies_metadata.csv) :  These files contain metadata for all 45,000 movies released before 2017 listed in the Full MovieLens Dataset. The dataset `movies_metadata.csv` allows us to complete missing movie’s box office revenues.
- [Mojo Movie](https://www.kaggle.com/datasets/kalilurrahman/top-box-office-revenue-data-english-movies/data?select=boxofficemojoustop1000.tsv) : The files `boxofficemojointernationaltop1000.tsv` and `boxofficemojoustop1000.tsv`respectively contain metadata for the top 1000 international grossing movies and the top 1000 US Grossing Movies. These files are used to further complete missing values of movie’s box office revenues.
- [Knowledge Graph API](https://developers.google.com/knowledge-graph?hl=fr) as a replacement for the deprecated Freebase API to obtain ethnicity names from their corresponding IDs in our dataset
- Wikipedia pages of actors: To address missing values of actors' ethnicities, we developed a web scraping tool that extracts ethnicities from the respective actors' Wikipedia pages.

## Methods: 
1. **Normalization** is applied to variables with disparate scales, such as `Movie box office revenue` and `Movie rating`, to facilitate meaningful comparisons. Depending on the data distribution, a logarithmic transformation is implemented for heavy-tailed distributions, while Z-score normalization is utilized for those with a normal distribution.
2. The **Pearson correlation coefficient** quantifies the linear relationship between two variables, and it's used to check the linear dependence between features and outcomes; in our analysis, it was employed to assess the correlation between annual average recognition coefficient of all actors and year/  average recognition coefficient of an actor in a movie and age of the actor at the movie's release date.
3. The **Kolmogorov-Smirnov test** is a non-parametric method for comparing probability distributions, useful when dealing with data that may not follow a specific distribution. It was used to assess whether the distribution of recognition coefficients for male and female actors differed significantly. The test aimed to check the null hypothesis that there is no significant difference in recognition coefficients between male and female actors.
4. **OLS Regression** is a statistical method used to model the relationship between a dependent variable and one or more independent variables by minimizing the sum of squared differences. In your analysis, OLS regression was employed to analyze the correlation between an actor's recognition coefficient and the actor's genre and age


## Proposed Timeline⏰📝:
- 17.11.2023 - Project Milestone 2 Deadline
- 24.12.2023 - 01.12.2023 - Pause the project for the duration of HW2
- 11.12.2023 - Perform final analysis and visualizations and start datastory implementation
- 18.12.2023 - Finish datastory
- 19.12.2023 - Internal final review of notebook/datastory before final submission
- 22.12.2023 - Project Milestone 3 Deadline
- 24.12.2023 - Happy Christmas

## Organization within the team 🤝

<table class="tg" style="undefined;table-layout: fixed; width: 342px">
<colgroup>
<col style="width: 164px">
<col style="width: 178px">
</colgroup>
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax">Tasks</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Andre</td>
    <td class="tg-0lax">Actor Recognition </td>
  </tr>
  <tr>
    <td class="tg-0lax">Ali</td>
    <td class="tg-0lax">Composition of actors in terms of gender over time</td>
  </tr>
  <tr>
    <td class="tg-0lax">Peter</td>
    <td class="tg-0lax">Actor recognition longevity</td>
  </tr>
  <tr>
    <td class="tg-0lax">Nicolas</td>
    <td class="tg-0lax">Composition of actors in terms of ethnicity over time</td>
  </tr>
    <tr>
    <td class="tg-0lax">Diego</td>
    <td class="tg-0lax">Actor recognition, longevity and trends evolution over time, considering changing societal norms and historical events </td>
  </tr>
     <tr>
    <td class="tg-0lax">Team together 🤲</td>
    <td class="tg-0lax">Create meaningful visualizations<br><br>Continue exploring the dataset<br><br>Finalize Datastory implementation HTML coding<br>Develop a consistent, fluent and clear datastory</td>
  </tr>
</tbody>
</table>