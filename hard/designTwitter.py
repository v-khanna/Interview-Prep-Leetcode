"""
Design Twitter (Hard)
https://leetcode.com/problems/design-twitter/

Problem: Design a simplified version of Twitter where users can post tweets, follow/unfollow other users, and see the 10 most recent tweets in their news feed.

Example:
Input: ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output: [null, null, [5], null, null, [6, 5], null, [5]]

Approach: Heap + Hash Map for efficient feed retrieval
Time Complexity: O(1) for postTweet, follow, unfollow; O(k log n) for getNewsFeed
Space Complexity: O(n + m) where n is users, m is tweets
"""

import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = defaultdict(list)  # userId -> list of (timestamp, tweetId)
        self.following = defaultdict(set)  # userId -> set of followed users
        self.timestamp = 0  # Global timestamp for tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet IDs in the user's news feed.
        """
        # Get all tweets from user and followed users
        all_tweets = []

        # Add user's own tweets
        if userId in self.tweets:
            all_tweets.extend(self.tweets[userId])

        # Add tweets from followed users
        for followed_user in self.following[userId]:
            if followed_user in self.tweets:
                all_tweets.extend(self.tweets[followed_user])

        # Sort by timestamp (most recent first) and get top 10
        all_tweets.sort(reverse=True)
        return [tweetId for _, tweetId in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee.
        """
        if followerId != followeeId:  # Users can't follow themselves
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee.
        """
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


class TwitterOptimized:
    def __init__(self):
        """
        Optimized version using heap for better performance
        """
        self.tweets = defaultdict(list)  # userId -> list of (timestamp, tweetId)
        self.following = defaultdict(set)  # userId -> set of followed users
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet IDs using heap.
        """
        # Create a set of all users to get tweets from
        users = {userId} | self.following[userId]

        # Create a heap with tweets from all relevant users
        heap = []
        user_indices = {
            user: len(self.tweets[user]) - 1 for user in users if self.tweets[user]
        }

        # Add the most recent tweet from each user to the heap
        for user in users:
            if user in self.tweets and self.tweets[user]:
                timestamp, tweetId = self.tweets[user][-1]
                heapq.heappush(
                    heap, (-timestamp, tweetId, user, len(self.tweets[user]) - 1)
                )

        # Get top 10 tweets
        result = []
        for _ in range(10):
            if not heap:
                break

            _, tweetId, user, index = heapq.heappop(heap)
            result.append(tweetId)

            # Add next tweet from the same user if available
            if index > 0:
                timestamp, next_tweetId = self.tweets[user][index - 1]
                heapq.heappush(heap, (-timestamp, next_tweetId, user, index - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee.
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee.
        """
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


def test_twitter():
    """Test cases for Design Twitter"""

    # Test case 1: Basic operations
    twitter1 = Twitter()
    twitter1.postTweet(1, 5)
    assert twitter1.getNewsFeed(1) == [5]
    twitter1.follow(1, 2)
    twitter1.postTweet(2, 6)
    assert twitter1.getNewsFeed(1) == [6, 5]
    twitter1.unfollow(1, 2)
    assert twitter1.getNewsFeed(1) == [5]

    # Test optimized version
    twitter2 = TwitterOptimized()
    twitter2.postTweet(1, 5)
    assert twitter2.getNewsFeed(1) == [5]
    twitter2.follow(1, 2)
    twitter2.postTweet(2, 6)
    assert twitter2.getNewsFeed(1) == [6, 5]

    # Test case 2: Multiple tweets
    twitter3 = Twitter()
    twitter3.postTweet(1, 1)
    twitter3.postTweet(1, 2)
    twitter3.postTweet(1, 3)
    assert twitter3.getNewsFeed(1) == [3, 2, 1]

    # Test case 3: Follow/unfollow
    twitter4 = Twitter()
    twitter4.postTweet(1, 1)
    twitter4.postTweet(2, 2)
    twitter4.follow(1, 2)
    assert twitter4.getNewsFeed(1) == [2, 1]
    twitter4.unfollow(1, 2)
    assert twitter4.getNewsFeed(1) == [1]

    # Test case 4: Self-follow prevention
    twitter5 = Twitter()
    twitter5.follow(1, 1)  # Should not allow self-follow
    twitter5.postTweet(1, 1)
    assert twitter5.getNewsFeed(1) == [1]

    print("All test cases passed!")


if __name__ == "__main__":
    test_twitter()
