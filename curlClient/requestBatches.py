
create_requests = [
{
    'method' : 'POST',
    'payload' : 'name=default',
    'url' : '/api/playlists/add'
},
{
    'method' : 'GET',
    'url' : '/api/playlists'
},
{
    'method' : 'GET',
    'url' : '/api/playlist/default'
},
{
    'method' : 'POST',
    'payload' : 'name=yeah',
    'url' : '/api/playlists/add'
},
{
    'method' : 'POST',
    'payload' : 'name=new',
    'url' : '/api/playlists/add'
},
{
    'method' : 'POST',
    'payload' : 'name=cat&video_uri=cat.sing.com',
    'url' : '/api/playlist/yeah/video/add'
},
{
    'method' : 'POST',
    'payload' : 'name=dog&video_uri=dog.sing.com',
    'url' : '/api/playlist/yeah/video/add'
},
{
    'method' : 'GET',
    'url' : '/api/playlist/yeah'
},
{
    'method' : 'GET',
    'url' : '/api/playlist/yeah/video/6473924464345088'
},
]

clean_requests = [
{
    'method' : 'POST',
    'payload' : 'name=cat&video_uri=cat.sing.com',
    'url' : '/api/playlist/yeah/video/delete'
},
{
    'method' : 'POST',
    'payload' : 'name=dog&video_uri=dog.sing.com',
    'url' : '/api/playlist/yeah/video/delete'
},
{
    'method' : 'GET',
    'url' : '/api/playlist/yeah'
},
{
    'method' : 'POST',
    'payload' : 'name=yeah',
    'url' : '/api/playlist/delete'
},
{
    'method' : 'GET',
    'url' : '/api/playlists'
},
]

read_requests = [
{
    'method' : 'GET',
    'url' : '/api/playlists'
},
{
    'method' : 'GET',
    'url' : '/api/playlist/yeah'
},
]

