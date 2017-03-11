# TMC2

Super minimalist quote gathering tool.

Based on <http://charlesleifer.com/blog/saturday-morning-hack-a-little-note-taking-app-with-flask/>

## quoteimport.py

`quoteimport.py` lets you import quotes from a JSON file. The JSON file must
have the following format:

    {
        "quotes": [
            {
                "date": "date-in-iso8601-format",
                "text": "quote text"
            },
            //...
        ]
    }

## Static files sources

Bootstrap: <https://github.com/twbs/bootstrap/releases/download/v3.3.7/bootstrap-3.3.7-dist.zip>

## License

Apache 2.0
