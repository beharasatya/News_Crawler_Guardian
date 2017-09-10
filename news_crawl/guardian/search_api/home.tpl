<html>
  <head>
      <title>News Article Search</title>
	  <link rel="stylesheet" type="text/css" href="styles.css">
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
    </form>

    <p>{{message}}</p>
    <p>{{results}}</p>

  </body>
</html>