"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None
        self.isPaused = False
        self.isPlaying = False
        self.playlist = {""}
        

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        print("Funny Dogs (funny_dogs_video_id)  [#dog , #animal]")
        print("Amazing Cats (amazing_cats_video_id) [#cat , #animal]")
        print("Another Cat Video (another_cat_video_id)  [#cat , #animal]")
        print("Life at Google (life_at_google_video_id)  [#google , #career]")
        print("Video about nothing (nothing_video_id) []")

    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        
        if video and self.isPaused == True:
            print(f'Stopping video: {self._current_video.title}')
        if video:
            print(f"Playing video: {video.title}")
            self._current_video = video
        else:
            print("Cannot play video: Video does not exist")
        
             
    def stop_video(self):
        """Stops the current video."""
 
        current_video = self._current_video
        if  current_video:
            print(f'Stopping video: {self._current_video.title}')
            self._current_video = None
        else:
            print("Cannot play video: Video does not exist")
        

    def play_random_video(self):
        """Plays a random video from the video library."""
        random_video = random.choice(self._video_library.get_all_videos())
        print(f"Playing video: {random_video.title}")

    def pause_video(self):
        """Pauses the current video."""
        if self.isPaused == False:
            print(f"Pausing video: {self._current_video.title}")
            self.isPaused = True
        else:
            print(f"Video already paused: {self._current_video.title}")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.isPaused == True:
            print(f'Continuing video: {self._current_video.title}')
        if self._current_video == None:
            print("Cannot continue video: no video is currently playing.")
        if self.isPaused == False and self._current_video != None:
            print("Cannot continue video: video is not paused")
        self.isPaused = False
        
    def show_playing(self):
        """Displays video currently playing."""
        if self._current_video == None:
            print("No video is currently playing")
        else: 
            print(f'Currently playing: {self._current_video.title} ({self._current_video.video_id}) [{self._current_video.tags}]')

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        if  playlist_name.lower() not in self.playlist:
            print(f"Successfully created new playlist: {playlist_name}")
            self.playlist = {playlist_name:[]}
        else:
            print("Cannot create playlist: playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        video = self._video_library.get_video(video_id)
        vid_validity = 0
        if video and video_id not in self.playlist:
            self.playlist[playlist_name].append(f"{video.title}, {video.video_id}, {video.tags}")
            vid_validity = 1
            print(f"Added video to {playlist_name}: {video.title}")

        if video and video_id in self.playlist:
            vid_validity = 1
            print(f"Cannot add video to {playlist_name}, video already added")
        
        if video and playlist_name.lower() not in self.playlist:
            vid_validity = 1
            print(f"Cannot add video to {playlist_name}, playlist does not exist")
            
        if vid_validity == 0:
            print(f"Cannot add video to {playlist_name}, video does not exist")
        


    def show_all_playlists(self):
        """Display all playlists."""
        if self.playlist == {}:
            print("No playlists exist yet")
        else:
            print(self.playlist.keys())

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name not in self.playlist:
            print(f"Cannot show playlist {playlist_name}: playlist does not exist ")
        if playlist_name in self.playlist:
            print(f"Showing playlist: {playlist_name}")
            if self.playlist[playlist_name] == []:
                print("No videos here yet")
            else:
                print(self.playlist[playlist_name])

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        video = self._video_library.get_video(video_id)
        vid_validity = 0
        if video_id in self.playlist[playlist_name]:
            vid_validity = 1
            print(f"Removed video from {playlist_name}: {video.title}")
            self.playlist[playlist_name].pop(f"{video.title}, {video.video_id}, {video.tags}")

        if video_id not in self.playlist[playlist_name]:
            vid_validity = 1
            print(f"Cannot remove video from {playlist_name}, video is not in playlist")
        
        if playlist_name.lower() not in self.playlist:
            vid_validity = 1
            print(f"Cannot remove video from {playlist_name}, playlist does not exist")
            
        if vid_validity == 0:
            print(f"Cannot remove video from {playlist_name}, video does not exist")
        

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        self.playlist[playlist_name].clear()
        print(f"Successfully removed all videos from {playlist_name}")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name in self.playlist: 
            print(f"Deleted playlist: {playlist_name}")
            del self.playlist[playlist_name]
        else:
            print(f"Cannot delete playlist {playlist_name}: playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

