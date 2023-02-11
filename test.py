import anime
import os


links = "https://anoboy.zone/2023/02/spy-kyoushitsu-episode-6/" 
link_download = anime.link.getting(links)
os.system(f"wget {link_download}")
