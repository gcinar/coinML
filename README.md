# coinML

This is an exploratory repo for crypto currency analysis.

To build the master branch and develop in a docker container do the following:

```
docker build --no-cache -t dev-container .
```

In Visual Studio Code, you can attach to the ```dev-container``` image using Remote- Containers extension.
Once in the container install the dependencies using the following command at the root level of the repo:

```
poetry install
```

Run the tests:

```
poetry run pytest ./tests/
```
