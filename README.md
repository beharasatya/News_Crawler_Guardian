# isentia_guardian
Project to crawl through Guardian news website and store the scraped results in mongo db on cloud

You can access the api to search for articles on:
  http://ec2-54-252-255-96.ap-southeast-2.compute.amazonaws.com:8080/search
  

{web crawl can be done by running 'scrapy crawl guardian_hom' inside "news_crawl" directory}

Uses scrapy to:
  -- crawl through guardian.com
  -- parse the title, author & contents of each page 
  -- store the fresh crawl results to mongo DB on www.compose.com (results from the previous crawl are auto cleared)


Uses bottle (https://bottlepy.org/docs/dev/) to:
  -- host the search api
  -- display the search results fetched from mondo db on compose.com


