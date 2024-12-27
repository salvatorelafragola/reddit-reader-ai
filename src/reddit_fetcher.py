import json
from typing import List, Dict

import praw
from praw.models.comment_forest import CommentForest


class RedditFetcher:
    def __init__(self,
                 client_id: str,
                 client_secret: str,
                 user_agent: str,
                 limit_posts: int,
                 limit_comments: int):
        self.reddit = praw.Reddit(client_id=client_id,
                                  client_secret=client_secret,
                                  user_agent=user_agent)
        self.limit_posts = limit_posts
        self.limit_comments = limit_comments

    def get_posts_formatted_with_comments_by_channel(self, channel: str) -> List[Dict]:
        """
        Recupera i post di un canale Reddit con i commenti più popolari formattati.

        :param channel: Nome del subreddit
        :return: Lista di dizionari con informazioni sul post e commenti più popolari
        """
        try:
            reddit_posts = self.reddit.subreddit(channel).hot(limit=self.limit_posts)
        except Exception as e:
            print(f"Post non trovati. {e}")
            return []
        formatted_posts = []
        for post in reddit_posts:
            if not post:
                continue
            else:
                post.comments.replace_more(limit=0)
            comments = self.__get_most_popular_comments(post.comments)

            formatted_posts.append({
                "channel": channel,
                "titolo": post.title,
                "url": post.url,
                "contenuto": post.selftext,
                "commenti": comments
            })

        return formatted_posts

    def __get_most_popular_comments(self, post_comments: CommentForest) -> List[str]:
        """
          Recupera i commenti più votati da un albero di commenti di un post Reddit.

          :param post_comments: Albero dei commenti del post (CommentForest)
          :return: Lista dei testi dei commenti più popolari
          """
        sorted_comments = []
        for comment in post_comments:
            sorted_comments = sorted(post_comments, key=lambda comment: comment.score, reverse=True)
        return list(comment.body for comment in sorted_comments[:self.limit_comments])
