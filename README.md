# Actors Representation: Actor’s Recognition, Gender and Ethnicity throughout history and time 📆

## Abstract 
In the enthralling world of cinema 🎥, actors play a pivotal role, shaping and being shaped by the ever-evolving tapestry of human history. Embark with us on a cinematic journey through time as we explore actor’s recognition and their evolving representation in the world of cinema across history. Has an actor’s recognition and its longevity been influenced by specific attributes such as gender or ethnicity? Acting isn’t an isolated art form but rather intricately connected to the tapestry of human existence, always influenced and shaped by historical events. Our objective is to decode the impact of pivotal historical events, such as the Civil Rights and Feminist Movements, on the composition of actors in terms of gender and ethnicity. This project invites you on a cinematic journey delving into the life of actors who have graced the Cinema screens, examining how they have been portrayed, known and represented over time.

You can discover our Datastory [here](https://andreschakkal.github.io/ada-actor-website/).

## Research Questions 🔎
1. How do age, gender, the genre of movies in which an actor has played, and ethnicity influence the evolution and magnitude of an actor’s recognition?
2. Can specific patterns be identified regarding an actor's recognition longevity based on factors such as age, gender, ethnicity, and the genres of movies in which they have participated?
3. To what extent have historical events, particularly the Civil Rights Movement and the Feminist Movement, influenced the composition of actors in terms of ethnicity and gender?
4. In what ways have trends related to an actor's recognition and longevity evolved over time, considering changing societal norms and historical events? Meaning have age, gender and ethnicity of recognized actors evolved over time?
5. How does the recognition of specific actors vary with time? What are the factors that influence it?


## Additional Ressources 📉
### Datatsets
- [CMU Movie Summary Corpus](https://www.cs.cmu.edu/~ark/personas//): The CMU Movie Summary Corpus is a comprehensive dataset providing information about movies, including box office revenue, genre, release date, runtime, language, actors, and plot summaries.

- [IMDb Movies Dataset](https://developer.imdb.com/non-commercial-datasets/): The IMDb Movies Dataset is a valuable resource for incorporating IMDb ratings into our analysis. It also helps enhance our dataset by filling in missing information not covered by the CMU Movie Summary Corpus.

- [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&select=movies_metadata.csv) : The Movies Dataset is another dataset containing information about movies. We leverage this dataset to supplement our analysis with additional data that may be absent from the CMU Movie Summary Corpus.


- [Mojo Movie](https://www.kaggle.com/datasets/kalilurrahman/top-box-office-revenue-data-english-movies/data?select=boxofficemojoustop1000.tsv) : The Mojo Movie dataset provides information on top box office revenue for English movies. It complements our analysis by filling potential gaps in the CMU Movie Summary Corpus.


- [Global Database of Inflation](https://www.worldbank.org/en/research/brief/inflation-database): The Global Database of Inflation is a dataset containing information on world inflation. We use it to normalize movie revenues, ensuring a consistent monetary scale over the years.



### APIs
- [Knowledge Graph API](https://developers.google.com/knowledge-graph?hl=fr) We utilize the Knowledge Graph API as a replacement for the deprecated Freebase API. This helps us map Freebase IDs of ethnicities to their corresponding names.


### Webpages
- [List of African-American actors](https://en.wikipedia.org/wiki/List_of_African-American_actors), [List of Hispanic and Latino American actors](https://en.wikipedia.org/wiki/List_of_Hispanic_and_Latino_American_actors), and [List of Italian-American actors](https://en.wikipedia.org/wiki/List_of_Italian-American_actors): Wikipedia pages we use to supplement our analysis with additional actors' ethnicities that may be absent from the CMU Movie Summary Corpus.
## Methods: 
1. **Normalization** is applied to variables with disparate scales, such as `Movie box office revenue` and `Movie rating`, to facilitate meaningful comparisons. Depending on the data distribution, a logarithmic transformation is implemented for heavy-tailed distributions, while standardization is utilized for those with a normal distribution.
2. The **Pearson correlation coefficient** quantifies the linear relationship between two variables, and it's used to check the linear dependence between features and outcomes; in our analysis, it was employed to assess the correlation between annual average recognition coefficient of all actors and year/  average recognition coefficient of an actor in a movie and age of the actor at the movie's release date.
3. The **Kolmogorov-Smirnov test** is a non-parametric method for comparing probability distributions, useful when dealing with data that may not follow a specific distribution. It was used to assess whether the distribution of recognition coefficients for male and female actors differed significantly. The test aimed to check the null hypothesis that there is no significant difference in recognition coefficients between male and female actors.
4. The **Chow test** is a statistical method used to detect structural breaks in a time series dataset. It assesses whether regression coefficients significantly differ between distinct groups or time periods, testing the null hypothesis that there is no structural change in the relationship being studied. 
5. **OLS Regression** is a statistical method used to model the relationship between a dependent variable and one or more independent variables by minimizing the sum of squared differences. In our analysis, OLS regression was employed to analyze the correlation between an actor's recognition coefficient and the actor's genre and age.


## Proposed Timeline⏰📝:
- 17.11.2023 - Project Milestone 2 Deadline
- 24.12.2023 - 01.12.2023 - Pause the project for the duration of HW2
- 11.12.2023 - Perform final analysis and visualizations and start datastory implementation
- 18.12.2023 - Finish datastory
- 19.12.2023 - Internal final review of notebook/datastory before final submission
- 22.12.2023 - Project Milestone 3 Deadline
- 24.12.2023 - Merry Christmas!

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
    <td class="tg-0lax">André Schakkal</td>
    <td class="tg-0lax">Writing the Datastory <br> Working on Actor Recognition </td>
  </tr>
  <tr>
    <td class="tg-0lax">Ali Elguindy</td>
    <td class="tg-0lax">Working on Actors representation in terms of gender</td>
  </tr>
  <tr>
    <td class="tg-0lax">Peter Harmouch</td>
    <td class="tg-0lax">Working on Actor recognition longevity</td>
  </tr>
  <tr>
    <td class="tg-0lax">Nicolas Matekalo</td>
    <td class="tg-0lax">Working on Actors representation in terms of ethnicity</td>
  </tr>
    <tr>
    <td class="tg-0lax">Diego Vermeire</td>
    <td class="tg-0lax">Working on the impact of historical events on Actors representation in terms of gender and ethnicity <br> Organizing the repo </td>
  </tr>
     <tr>
    <td class="tg-0lax">Team together 🤲</td>
    <td class="tg-0lax">Create meaningful visualizations<br>Continue exploring the dataset<br>Finalize Datastory implementation HTML coding<br>Develop a consistent, fluent and clear datastory</td>
  </tr>
</tbody>
</table>
