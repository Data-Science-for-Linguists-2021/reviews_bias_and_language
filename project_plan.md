# Restaurant reviews, Bias, and Language
## Jordan Picone

Cultural bias impacts nearly every facet of life, and the food service industry is no exception. Reviews often contain examples of bias, either conscious or unintentional. To quantify this, I will take the following steps.

Data:
  Since the Yelp dataset is already well structured, there isn't much to be done in terms of polishing the data. Instead, I will create a classifier to tag each sentence in a review as referring to (1) the food, (2) the service, (3) the restaurant's atmosphere and other features, and (4) misc/irrelevant background info from the reviewer. This will allow me to look at the issue with a finer grain, and I want to get more experience with ML models.
  
Analysis:
  What terms do people tend to use to describe foods from restaurants of different cultural background? A great deal of these will no doubt have to do with flavors and presentation, but could bias be expressed through word choices? Making a hypothesis as to the exact words used feels unscientific as it would be based on my knowledge of our society's stereotypes, but I predict that there will be a significant difference in the terms used to describe foods, service, and restaurants in general that are based in the cuisine the restaurant serves.
   To do this I will use several possible approaches. One would be a simple statistical analysis of words that are most overrepresented in reviews of restaurants. Another is to use a classifier that can display the most significant features, although under the hood these two may be similar. 
   Another interesting possibility is to tie the use of these overrepresented terms to the star ratings of the reviews and the restaurants. There may be some corrolation between these two features.
   
Presentation:
  I don't have anything specific in mind here, possibly word clouds or something similar but as I work on the data more I'll have a better idea of how I want to present it.
