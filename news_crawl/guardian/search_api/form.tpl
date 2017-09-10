<html>
  <head>
      <title>News Article Search</title>
  </head>
  <body>
    <form method="post" action="/search">
        <fieldset>
            <legend>News Article Search</legend>
            <ul>
                <li>Keywords: <input name='keyword'>
                </li>
            </ul><input type='submit' value='Search News'>
        </fieldset>
    </form>

    <p>{{message}}</p>

  </body>
</html>