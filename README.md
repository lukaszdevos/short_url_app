## SHORT URL APP 
Django Application to shorten your long URLs with provide a simple statistics like counter for redirection, saving user agent data 


### Endpoints: 
- `/shortener/` POST - creating shorten url based on given `long_url` in body
- `/shortener/<short_url_token>/` GET - redirects to `long_url` given in previous endpoint
- `/shortener/statistics/<short_url_token>/` GET - retrieve statistic information based on `short_url` token  


### Environment variables
```
SECRET_KEY=
DEBUG=False
# default to run for local environment
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 

DB_HOST=db
# setup your postgres database below 
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432

DJANGO_SETTINGS_MODULE=config.settings

# default value is 5
CHAR_LENGTH_IN_SHORT_URL=5

```

### App commands
`make start-local` to start app

`make stop-local` to stop app

`make build` to rebuild app

`make restart-local` to restart app

`make test` to run tests with coverage

`make clean_code` to run linters (isort, black)
 
`make shell` go to shell 