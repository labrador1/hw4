import pandas as pd
import numpy as np
import sys

#ファイルを読み込む
def read():
	links = pd.read_table("links.txt",header=None)
	links.columns = ["START", "GOAL"]
	pages = pd.read_table("pages.txt",header=None)
	pages.columns = ["INDEX", "WORD"]
	return links, pages

#幅優先探索
def search(start, goal, links, pages):
	g = []
	start_index = pages[pages.WORD == start].INDEX.values
	goal_index = pages[pages.WORD == goal].INDEX.values

	start_index = start_index.tolist()
	q = [start_index]
	while len(q) > 0:
		path = q.pop(0)
		n = path[-1]
		if n == goal_index:
			print("START -> ",end="")
			for n in path:
				 print(pages[pages.INDEX == n].WORD.values[0] +" "+"->"+" ", end="")
			print("END",end="")
			sys.exit()
		else:
			g = links[links.START == n].GOAL.values
			g = g.tolist()
			for x in g:
				if x not in path:
					new_path = path[:]            
					new_path.append(x)
					q.append(new_path)				

#スタートとゴールの設定
def start_goal():
	start = input("Please Enter Start: ")
	goal = input("Please Enter Goal: ")
	return start, goal

def main():
	links, pages = read()
	start, goal = start_goal()
	search(start, goal, links, pages)

main()
