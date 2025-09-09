from api import get_video_details, get_comments, search_videos
from models import *
import pandas as pd

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


def video_to_dataframe(videos: searchListResponse):
    video_data = []
    for item in videos.items:
        video_id = item.id.videoId
        video_details = get_video_details(video_id)
        video_details = videoListResponse(**video_details)
        video_stats = get_video_stats(video_details)
        video_data.append({
            'video_id': video_id,
            'title': item.snippet.title,
            'description': item.snippet.description,
            'published_at': item.snippet.publishedAt,
            'channel_title': item.snippet.channelTitle,
            'like_count': video_stats.likeCount,
            'view_count': video_stats.viewCount,
            'comment_count': video_stats.commentCount,
        })
    df = pd.DataFrame(video_data)
    return df

def get_video_stats(video_details: videoListResponse):
    stats = video_details.items[0].statistics
    return stats

def comments to 
