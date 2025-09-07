import os
import dotenv
import pandas as pd
import numpy as np
import re
from googleapiclient.discovery import build
from models import commentListResponse, commentListResponse, comment

dotenv.load_dotenv()

key = os.getenv("KEY")

youtube = build('youtube', 'v3', developerKey=key)

def search_videos(query, max_results=50):
    request = youtube.search().list(
        q=query,
        part='id,snippet',
        type='video',
        maxResults=max_results,
        order='relevance',
    )
    response = request.execute()
    return response

def get_comments(video_id, max_results=50):
    request = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id,
        maxResults=max_results,
        order='relevance',
    )
    response = request.execute()
    return response

def get_comment_reply_dict(comment_threads: commentListResponse):
    comment_reply_dict = {}
    for comment_thread in comment_threads.items:
        top_level_comment = comment_thread.snippet.topLevelComment
        comment_text = top_level_comment.snippet.textOriginal
        replies = comment_thread.replies['comments'] if comment_thread.replies else []
        reply_texts = []
        for reply in replies:
            reply_text = reply.snippet.textOriginal
            reply_texts.append(reply_text)
        comment_reply_dict[comment_text] = reply_texts
    return comment_reply_dict


