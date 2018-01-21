# Guardian
Project to crawl through Guardian news website and store the scraped results in mongo db on cloud


{web crawl can be done by running 'scrapy crawl guardian_home' inside "news_crawl" directory}

Uses scrapy to:
  -- crawl through guardian.com
  -- parse the title, author & contents of each page 
  -- store the fresh crawl results to Mongo DB on www.compose.com (results from the previous crawl are auto cleared)


Uses bottle (https://bottlepy.org/docs/dev/) to:
  -- host the search api
  -- display the search results fetched from Mongo DB on compose.com


