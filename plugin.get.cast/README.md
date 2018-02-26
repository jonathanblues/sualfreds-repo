plugin.get.cast

### HowTo

Include the following in your addon.xml
`<import addon="plugin.get.cast" version="0.0.1"/>`

Script call using a DBID
`<content>plugin://plugin.get.cast?mode=dbid&amp;dbtype=$INFO[ListItem.DBTYPE]&amp;dbinfo=$INFO[ListItem.DBID]</content>`

Script call using a movie title
`<content>plugin://plugin.get.cast?mode=title&amp;dbtype=movie&amp;dbinfo=$INFO[ListItem.Label]</content>`

Script call using a TV show title
`<content>plugin://plugin.get.cast?mode=title&amp;dbtype=tvshow&amp;dbinfo=$INFO[ListItem.TVShowTitle]</content>`

### Available ListItem values

 - ListItem.Label - Name
 - ListItem.Label2 - Role
 - ListItem.Icon - Actor thumbnail (Fallback `DefaultActor.png`)