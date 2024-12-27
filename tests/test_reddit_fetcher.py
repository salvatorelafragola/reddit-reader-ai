import unittest
from unittest.mock import MagicMock, patch
from praw.models import Comment
from src.reddit_fetcher import RedditFetcher


class TestRedditFetcher(unittest.TestCase):
    @patch('praw.Reddit')
    def setUp(self, mock_reddit):
        self.mock_reddit_instance = mock_reddit.return_value
        self.fetcher = RedditFetcher(
            client_id="dummy_id",
            client_secret="dummy_secret",
            user_agent="dummy_agent",
            limit_posts=5,
            limit_comments=3
        )

    def test_get_posts_formatted_with_comments_by_channel(self):
        # Configurazione dei mock per i post e i commenti
        mock_post = MagicMock()
        mock_post.title = "Test Title"
        mock_post.url = "https://example.com/test"
        mock_post.selftext = "Test content of the post"
        mock_post.comments = MagicMock()
        mock_post.comments.replace_more = MagicMock(return_value=None)

        # Creazione di commenti finti
        mock_comment_1 = MagicMock()
        mock_comment_1.body = "First comment"
        mock_comment_1.score = 10

        mock_comment_2 = MagicMock()
        mock_comment_2.body = "Second comment"
        mock_comment_2.score = 5

        mock_post.comments.__iter__.return_value = [mock_comment_1, mock_comment_2]

        # Configurazione del subreddit
        self.mock_reddit_instance.subreddit.return_value.hot.return_value = [mock_post]

        # Esegui il metodo
        result = self.fetcher.get_posts_formatted_with_comments_by_channel("test_channel")

        # Verifica i risultati
        expected_result = [
            {
                "channel": "test_channel",
                "titolo": "Test Title",
                "url": "https://example.com/test",
                "contenuto": "Test content of the post",
                "commenti": ["First comment", "Second comment"]
            }
        ]

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
