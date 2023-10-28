import sys; args = sys.argv[1:]
from PIL import Image; img = Image.open(args[0])
#file = Image.open(args[0])
import PIL
import random, math
#import urllib.request
#import io, sys, os, random, math
#import tkinter as tk
#from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/errors)

def choose_random_means(k, img, pix):
   means = []
   for x in range(k):
      newmean = (int(random.random()*255),int(random.random()*255),int(random.random()*255))
      means.append(newmean)
   return means

# goal test: no hopping
def check_move_count(mc):
   for x in mc:
      if x != 0:
         return False
   return True

# calculate distance with the current color with each mean
# return the index of means
def dist(col, means): #need to fix i think
   minIndex, dist_sum = 0, 255**2+255**2+255**2
   count = 0
   for mean in means:
      distance = math.sqrt(((mean[0]-col[0])**2+(mean[1]-col[1])**2+(mean[2]-col[2])**2))
      if distance < dist_sum:
         minIndex = count
         dist_sum = distance
      count+=1
   return minIndex 

def clustering(img, pix, cb, mc, means, count):
   temp_pb, temp_mc, temp_m = [[] for x in means], [], [] #mc-move count m-means cb-count buckets
   colorinfo = {}
   temp_placement = {}
   temp_mints = []
   temp_cb = [0 for x in means]
   for x in range(img.size[0]):
      for y in range(img.size[1]):
         color = (pix[x,y][0],pix[x,y][1],pix[x,y][2])
         place = dist(pix[x,y],means)
         temp_cb[place] += 1
         temp_pb[place].append(pix[x,y])
         temp_placement[(x,y)] = place
         colorinfo[color] = [place]

   for x in temp_pb:
      rsum = gsum = bsum = 0
      for y in x:
         rsum += y[0]
         gsum += y[1]
         bsum += y[2]
      if len(x) > 0:
         rsum = rsum/len(x)
         gsum = gsum/len(x)
         bsum = bsum/len(x)
      temp_m.append((rsum,gsum,bsum))
      temp_mints.append((int(rsum),int(gsum),int(bsum)))
   temp_mc = [ (a-b) for a, b in zip(temp_cb, cb)]
   print ('diff', count, ':', temp_mc)
   return temp_cb, temp_mc, temp_m, temp_placement,temp_mints

# import time 
def update_picture(img, pix, means, colorgroup):
   # print("updating")
   # tic = time.process_time()
   region_dict = {}
   for x in range(img.size[0]):
      for y in range(img.size[1]):
         pix[x,y] = means[colorgroup[(x,y)]]
   # toc = time.process_time()
   # print(toc - tic)
   return pix, region_dict
   
def distinct_pix_count(img, pix):
   cols = {}
   max_col, max_count = pix[0, 0], 0
   for x in range(img.size[0]):
      for y in range(img.size[1]):
         if pix[x,y] not in cols.keys():
            cols[pix[x,y]] = 1
         else:
            cols[pix[x,y]] += 1
   max_col = max(cols,key = cols.get)
   max_count = cols[max_col]
   return len(cols.keys()), max_col, max_count


def count_regions(img, region_dict, pix, colorgroup, means):
   region_count = [0 for x in means]
   visited = set()
   frontier = []
   for x in range(img.size[0]):
      for y in range(img.size[1]):
         coordinate = (x,y)
         color = pix[x,y]
         if coordinate not in visited:
            frontier.append(coordinate)
            while frontier:
               coordinate = frontier.pop(0)
               xcord = coordinate[0]
               ycord = coordinate[1]
               if coordinate not in visited: #coordinate not in visited and
                  visited.add(coordinate)
                  if xcord < img.size[0]-1 and pix[xcord+1,ycord] == color:
                     frontier.append((xcord+1,ycord))
                     if ycord < img.size[1]-1:
                        if pix[xcord+1,ycord+1] == color:
                           frontier.append((xcord+1,ycord+1))
                        if pix[xcord,ycord+1] == color:
                           frontier.append((xcord,ycord+1))
                     if ycord > 0:
                        if pix[xcord+1,ycord-1] == color:
                           frontier.append((xcord+1,ycord-1))
                        if pix[xcord,ycord-1] == color:
                           frontier.append((xcord,ycord-1))
                  if xcord > 0 and pix[xcord-1,ycord] == color:
                     frontier.append((xcord-1,ycord))
                     if ycord < img.size[1]-1:
                        if pix[xcord-1,ycord+1] == color:
                           frontier.append((xcord-1,ycord+1))
                        if pix[xcord,ycord+1] == color:
                           frontier.append((xcord,ycord+1))
                     if ycord > 0:
                        if pix[xcord-1,ycord-1] == color:
                           frontier.append((xcord-1,ycord-1))
                        if pix[xcord,ycord-1] == color:
                           frontier.append((xcord,ycord-1))
            # index = means.index(pix[x,y])
         region_count[means.index(color)] += 1
         #    color = pix[x,y]
         #    while frontier:
         #       coordinate = frontier.pop(0)
         #       xcord = coordinate[0]
         #       ycord = coordinate[1]
         #       if coordinate not in visited and coordinate not in frontier and pix[xcord,ycord] == color:
         #          visited.append(coordinate)
   return region_count

def main():
   k = int(args[1])
   # k = int(sys.argv[1])
   # file = sys.argv[2]
   #k = 6
   #file = 'https://cf.geekdo-images.com/imagepage/img/5lvEWGGTqWDFmJq_MaZvVD3sPuM=/fit-in/900x600/filters:no_upscale()/pic260745.jpg'
   #k = 6
   # file = 'cute_dog.jpg'
   # k = 4
   # if not os.path.isfile(file):
   #    file = io.BytesIO(urllib.request.urlopen(file).read())
   
   # window = tk.Tk() #create an window object
   # window2 = tk.Toplevel()
   # img = Image.open(file)
   
   # img_tk = ImageTk.PhotoImage(img)
   # lbl = tk.Label(window, image = img_tk).pack()  # display the image at window
   
   pix = img.load()   # pix[0, 0] : (r, g, b) 
   print ('Size:', img.size[0], 'x', img.size[1])
   print ('Pixels:', img.size[0]*img.size[1])
   d_count, m_col, m_count = distinct_pix_count(img, pix)
   print ('Distinct pixel count:', d_count)
   print ('Most common pixel:', m_col, '=>', m_count)

   count_buckets = [0 for x in range(k)]
   move_count = [10 for x in range(k)]
   means = choose_random_means(k, img, pix)
   # means = [(150,111,72),(171,138,95),(245,210,154),(127,87,52)]
   #print ('random means:', means)
   count = 1
   while not check_move_count(move_count):
      count += 1
      count_buckets, move_count, means, colorgroup, means_int = clustering(img, pix, count_buckets, move_count, means, count)
      # if count == 2:
      #    print ('first means:', means_int)
      #    print ('starting sizes:', count_buckets)
   pix, region_dict = update_picture(img, pix, means_int, colorgroup)  # region_dict can be an empty dictionary
   #print ('Final sizes:', count_buckets)
   print ('Final means:')
   for i in range(len(means)):
      print (i+1, ':', means[i], '=>', count_buckets[i])
   print('Region counts:', count_regions(img,region_dict,pix,colorgroup,means_int))
   #print(count_region2(colorgroup,means))
   # img_tk2 = ImageTk.PhotoImage(img)
   # lbl2 = tk.Label(window2, image = img_tk2).pack()  # display the image at window
   #img.save('kmeans/2023rfu', 'PNG')  # change to your own filename
   img.save("kmeans/{}.png".format('2023rfu'), "PNG")
   #window.mainloop()
   
   #img.show()
   
if __name__ == '__main__': 
   main()
# Randy Fu, pd.5, 2023