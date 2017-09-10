from bottle import route, run, template, error, static_file, request
from scrapy.conf import settings
import pymongo
import subprocess

HTML_ROOT = settings['HTML_ROOT']
CONN = pymongo.MongoClient(
    settings['COMPOSE_URI']
)
MDB = CONN[settings['MONGODB_DB']]
NEWS_COLLECTION = MDB[settings['MONGODB_COLLECTION']]
ERR_COLLECTION = MDB[settings['MONGODB_ERRORS']]
STATS_COLLECTION = MDB[settings['MONGODB_STATS']]


tpl_start = '''<html>
  <head>
      <title>News Article Search</title>
	  <link rel="stylesheet" href="styles.css">	  
  </head>
  <body>
	
    <form method="post" action="/search">
        <fieldset align="center">				  
            <legend align="center">News Article Search</legend> <br>
			<br/> <br/>
			<b>Enter Keywords</b> <br><input id="textboxid" name='keyword' required>
			<br/><br/>
			<input id="searchbox" type='submit' value='Search'> 
			<br/> <br/> <br/> <br/>
        </fieldset>
    </form>'''


# '''<html>
#             <head>
#                 <title>News Article Search</title>
#             </head>
#             <body>
#                 <form method="post" action="/search">
#                     <fieldset>
#                         <legend>News Article Search</legend>
#                         <ul>
#                             <li>Keywords: <input name='keyword'></li>
#                         </ul><input type='submit' value='Search News'>
#                     </fieldset>
#                 </form> '''

p_tag = '''<p><pre><code style=display:block;white-space:pre-wrap>{txt}</pre></p>'''


auth_tag = '''<p>By <b><i>{author}</i></b></p>'''

title_tag = '''<p style="font-size: 22px;><a href='{url}' target="_blank"><b>{title}</b></a></p>'''

tpl_end = '''</body>
         </html> '''

def query_db(keywords):
    if keywords:
        NEWS_COLLECTION.create_index([('article', 'text')])

        keywords = "\\".join(keywords.split())
        news_hits = NEWS_COLLECTION.find({"$text": {"$search": keywords}}, {"score": {"$meta": "textScore"}}).sort(
            [("score", {"$meta": "textScore"})])


        for hit in news_hits:
            # hit_list.append()
            yield {'title' : str(hit['title']),
                             'url': str(hit['url']),
                             'article': str(hit['article']),
                             'author': str(hit['author'])
                             }



@route('/<filename>')
def server_static(filename):
  return static_file(filename, root=HTML_ROOT)


@route('/')
@route('/search')
def search():
    return template("home.tpl", message="Please enter the keywords you wish to search in the news database", results="")


@route('/', method="POST")
@route('/search', method="POST")
def formhandler():
    # return template("form.tpl", message=request.forms.get('keyword'))
    # keyword = request.forms.get('keyword')
    keywords = request.forms.get('keyword')
    hits = query_db(keywords)
    message = "You searched for '" + keywords + "'\n\n\n"
    tpl = tpl_start

    for hit in hits:
        tpl += title_tag.format(title=hit['title'], url=hit['url'])
        if hit['author'] != 'None':
            tpl += auth_tag.format(author=hit['author'])
        tpl += p_tag.format(txt=hit['article'])
    tpl += tpl_end
    if tpl == tpl_start + tpl_end:
        return template("home.tpl", message=message, results="No Related Articles Found")
    else:
        return template(tpl, message=message)



@error(404)
def error404(error):
    return 'Nothing here, sorry'




run(server='auto', host=subprocess.getoutput('curl http://169.254.169.254/latest/meta-data/public-hostname/public-hostname').split()[-1])