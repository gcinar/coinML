# coinML

This is an exploratory repo for crypto currency analysis.

To build the master branch and develop in a docker container do the following:

```
docker build --no-cache -t dev-container .
```

In Visual Studio Code, you can attach to the ```dev-container``` image using Remote- Containers extension.

Run the tests:

```
poetry run pytest ./tests/
```
