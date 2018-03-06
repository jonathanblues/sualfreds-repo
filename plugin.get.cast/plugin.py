#!/usr/bin/python

import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import json as simplejson

ADDON = xbmcaddon.Addon()
ADDON_VERSION = ADDON.getAddonInfo('version')
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_LANGUAGE = ADDON.getLocalizedString

def log(txt):
    message = '%s: %s' % (ADDON_NAME, txt.encode('ascii', 'ignore'))
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)

def get_actors(mode, dbtype, dbinfo, full_liz):

    cast = None
    result = None

    json_query = get_query(dbtype, dbinfo, mode)
    json_query = unicode(json_query, 'utf-8', errors='ignore')
    json_query = simplejson.loads(json_query)

    if 'result' in json_query and 'moviedetails' in json_query['result']:
        cast = json_query['result']['moviedetails']['cast']
    elif 'result' in json_query and 'episodedetails' in json_query['result']:
        cast = json_query['result']['episodedetails']['cast']
    elif 'result' in json_query and 'tvshowdetails' in json_query['result']:
        cast = json_query['result']['tvshowdetails']['cast']
    elif 'result' in json_query and 'movies' in json_query['result']:
        cast = json_query['result']['movies'][0]['cast']
    elif 'result' in json_query and 'tvshows' in json_query['result']:
        cast = json_query['result']['tvshows'][0]['cast']
    
    if cast:
        for actor in cast:
            liz = xbmcgui.ListItem(actor["name"])
            liz.setLabel(actor["name"])
            liz.setLabel2(actor["role"])
            liz.setThumbnailImage(actor.get('thumbnail', ""))
            liz.setIconImage('DefaultActor.png')
            full_liz.append(("", liz, False))

    del json_query


def get_query(dbtype, dbinfo, mode):

    try:
        if mode == "title":
            if dbtype == "movie":
                method = '"VideoLibrary.GetMovies"'
            elif dbtype == "tvshow":
                method = '"VideoLibrary.GetTVShows"'
                json_query = xbmc.executeJSONRPC('''{"jsonrpc": "2.0", "params": { "filter": {"operator": "contains", "field": "title", "value": "%s"}, "properties": ["cast"]}, "limits": { "start" : 0, "end": 1 }, "method": %s, "id": 1 })''' % (dbinfo, method))
        else:
            if dbtype == "movie":
                method = '"VideoLibrary.GetMovieDetails"'
                param = '"movieid"'
            elif dbtype == "tvshow":
                method = '"VideoLibrary.GetTVShowDetails"'
                param = '"tvshowid"'
            elif dbtype == "episode":
                method = '"VideoLibrary.GetEpisodeDetails"'
                param = '"episodeid"'
            json_query = xbmc.executeJSONRPC('''{ "jsonrpc": "2.0", "method": %s, "params": {%s: %d, "properties": ["title", "file", "cast"]}, "id": 1 }''' % (method, param, int(dbinfo)))
    except:
        json_query = None

    return json_query

class Main:

    def __init__(self):
        try:
            params = dict(arg.split("=") for arg in sys.argv[2].split("&&"))
        except:
            params = {}
        self.mode = params.get("?mode", "")
        self.dbtype = params.get("dbtype", False)
        self.dbinfo = params.get("dbinfo", False)
        full_liz = list()
        get_actors(self.mode, self.dbtype, self.dbinfo, full_liz)
        xbmcplugin.addDirectoryItems(int(sys.argv[1]), full_liz)
        xbmcplugin.endOfDirectory(handle=int(sys.argv[1]))

log('script version %s started' % ADDON_VERSION)
Main()
log('script version %s stopped' % ADDON_VERSION)
