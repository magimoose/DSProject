from api import search_videos, get_comments, get_comment_reply_dict
from models import *

def main():
    brand_name = "nike"
    search_queries = [f"{brand_name} sustainability", f"{brand_name} ecofriendly", f"{brand_name} greenwashing"]
    video_count = 10

    print("Brand:", brand_name)
    print("Search queries:", search_queries)

    for search_query in search_queries:
        videos = search_videos(search_query, max_results=video_count)
        videos = searchListResponse(**videos)
        video_ids = [item.id.videoId for item in videos.items]

        print(f"Search query: {search_query}")
        print(f"Video IDs: {video_ids}")

        
        

    # comments = get_comments("dQw4w9WgXcQ", max_results=50)
    # # video = api.search_videos("Python programming", max_results=1)
    # comments = models.commentListResponse(**comments)
    # comment_reply_dict = get_comment_reply_dict(comments)
    # print(comment_reply_dict)

if __name__ == "__main__":
    main()
