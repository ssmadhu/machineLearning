import apiclient
import io
import json
import os
import sys
KEY = 'AIzaSyDnJrrbMMMnkL-93na2ogPcYDjLfWTJRlU'


def build_comment(sn):
    return "\"" + sn['publishedAt'] + " === " +  sn['textOriginal'] + "\""


def scrape(comments, video_id, token=None):

    youtube = apiclient.discovery.build('Youtube', 'v3', developerKey=KEY)

    if token:
        results = youtube.commentThreads().list(
            part='snippet,replies',
            videoId=video_id,
            pageToken=token,
            textFormat='plainText',
            maxResults=100
        ).execute()
    else:
        results = youtube.commentThreads().list(
            part='snippet,replies',
            videoId=video_id,
            textFormat='plainText',
            maxResults=100
        ).execute()

    for item in results['items']:
        comment = build_comment(item['snippet']['topLevelComment']['snippet'])
        comments.append(comment)
        # if 'replies' in item.keys():
        #     for reply in item['replies']['comments']:
        #         comment = build_comment(reply['snippet'])
        #         comments.append(comment)

    with io.open('conjuring1.txt', 'a', encoding='utf8') as fp:
        for items in comments:
            fp.write(json.dumps(items))
        fp.close()

    if 'nextPageToken' in results:
        scrape(comments, video_id, results['nextPageToken'])



if __name__ == '__main__':
    comments_list = scrape([], 'h9Q4zZS2v1k')
    