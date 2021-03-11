# MapRoulette Repo Analysis

[back to README](../README.md)

## webapp
- #### WEB-INF
	- Private resources that are exposed to the server but not public
		- configs (i.e. `app-engine`, `web`)
		- libs (i.e. `app-engine`, `gwt-servlet`, `httpclient`)
		- deployment (i.e. `manifest`)
- #### maproulette/gwt
	- Google Web Toolkit config & wrapper
	- Allows writing Java code for the client side
		- `Java` -> `JS`
- #### assets
	- files that power the client app
		- `js`
		- `css`
		- `media`
- #### pages
	- `html` files that allow users to have access on the web app

## java
- #### fi.foyt.four.square
	- FourSquare API wrappers and entities
- #### com.pixeltron
	- mapquest
		- `mapquestapi` wrapper
			- Handles geocoding in case FourSquare API is not used
	- maproulette
		- models
		- responses
		- servlets
- #### org.json
	- json.org wrapper for java
		- handles json types in Java