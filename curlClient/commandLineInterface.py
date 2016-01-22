"""
command-line interface to REST api

list_action := list | l
delete_action := delete | d
add_action := add | a
action := list_action | delete_action | add_action

user_resource := users | user | u
playlist_catalog_resource := playlist_catalog | playlists | pc
playlist_resource := playlist | p
video_resource := videos | video | v
resource := user_resource | video_resource | playlist_catalog_resource | playlist_resource

key := <int:id> | <string:name>
payload := <json:data>


wclient list playlists
wclient l playlist_catalog
wclient l pc
wclient a pc <json:data>
wclient d pc
wclient d pc <string:name>

wclient list videos
wclient l videos
wclient l v
wclient a v <json:data>
wclient d v <int:id>

wclient list users
wclient l users
wclient l u
wclient a u <json:data>
wclient d u <int:id>

"""


import argparse


parser = argparse.ArgumentParser(description='interface to REST api calls')

parser.add_argument('operation', help='select operation of the api like add, delete or list')
parser.add_argument('resource', help='the resource operation is applied to')
parser.add_argument('-data', help='data used as payload')
parser.add_argument('-rkey', help='resource string identifier')
parser.add_argument('-key', help='string identifier')
parser.add_argument('-id', type=int, help='int identifier')
parser.add_argument('-json', action="store_true", help='response in json')
parser.add_argument('-html', action="store_true", help='response in html')

args = parser.parse_args()



import json
import curlClient as c

if args.resource == "pc":

    if args.operation == "l":
        if args.key:
            print c.get_playlistsEntry(args.key)
        else:
            print c.get_playlists()

    if args.operation == "d":
        if args.key:
            print c.delete_playlistsEntry(args.key)
        elif args.id:
            print c.delete_playlistsEntryById(args.id)
        else:
            print c.delete_playlists()

    if args.operation == "a":
        if args.data:
            entry = json.loads(args.data)
            c.add_playlistsEntry(entry)


if args.resource == "p":
    if args.operation == "l":
        if args.key and args.id:
            print c.get_videoFromPlaylist(args.key, args.id)
        elif args.key:
            print c.get_playlistByName(args.key)

    if args.operation == "d":
        if args.key and args.id:
            print c.delete_videoFromPlaylist(args.key, args.id)

    if args.operation == "a":
        if args.key and args.data:
            entry = json.loads(args.data)
            c.add_videoToPlaylist(args.key, entry)


if args.resource == "u":

    if args.operation == "l":
        if args.key:
            print c.get_user(args.key)
        else:
            print c.get_users()

    if args.operation == "d":
        if args.key:
            print c.delete_user(args.key)

    if args.operation == "a":
        if args.key and args.data:
            entry = json.loads(args.data)
            c.add_user(entry)


if args.resource == "v":

    if args.operation == "l":
        if args.key:
            print c.get_videoByName(args.key)
        else:
            pass

    if args.operation == "d":
        if args.key:
            print c.delete_videoByName(args.key)

    if args.operation == "a":
        if args.data:
            c.add_user(args.data)

