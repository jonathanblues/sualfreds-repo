plugin.get.cast

### HowTo

Include the following in your addon.xml

`<import addon="plugin.get.cast" version="0.0.1"/>`

Script call using a DBID

`<content>plugin://plugin.get.cast?mode=dbid&&dbtype=$INFO[ListItem.DBTYPE]&&dbinfo=$INFO[ListItem.DBID]</content>`

Script call using a movie title

`<content>plugin://plugin.get.cast?mode=title&&dbtype=movie&&dbinfo=$INFO[ListItem.Label]</content>`

Script call using a TV show title

`<content>plugin://plugin.get.cast?mode=title&&dbtype=tvshow&&dbinfo=$INFO[ListItem.TVShowTitle]</content>`

### Available ListItem values

 - ListItem.Label - Name
 - ListItem.Label2 - Role
 - ListItem.Icon - Actor thumbnail (Fallback `DefaultActor.png`)
