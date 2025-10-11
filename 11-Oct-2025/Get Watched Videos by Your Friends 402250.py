# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

from collections import deque, Counter
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited = set([id])
        queue = deque([(id, 0)])
        people_at_level = []
        while queue:
            person, lvl = queue.popleft()
            if lvl == level:
                people_at_level.append(person)
                continue
            for nei in friends[person]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, lvl + 1))
        videos = []
        for p in people_at_level:
            videos += watchedVideos[p] 
        video_count = Counter(videos)
        return sorted(video_count.keys(), key=lambda v: (video_count[v], v))

            