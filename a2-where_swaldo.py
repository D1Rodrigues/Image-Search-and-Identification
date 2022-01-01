scene = makePicture("/Users/dylanrodrigues/Documents/School/ComSci/Assessments/Assignments/Assignment_Qs/tinyscene.jpg")
waldo = makePicture("/Users/dylanrodrigues/Documents/School/ComSci/Assessments/Assignments/Assignment_Qs/tinywaldo.jpg")

#Function 1
#(x1, y1) is a pixel in search image, which is overlaid with top left pixel in template and...
#... all pixels of template have their luminance values subtracted from luminance values...
#... in search image from (x1, y1) on. 
#The differences are added into a running sum
def compareOne(template, searchImage, x1, y1): #function 1
  w = getWidth(template) #this and following lines find the width and height of template
  h = getHeight(template)
  sum = 0 # the running sum variable
  for x in range(w): #so for each x, y variable in template
    for y in range(h):
      pixel1 = getPixel(template, x, y) #pixel of template
      L1 = getRed(pixel1) #gets its luminance
      pixel2 = getPixel(searchImage, x1 + x, y1 + y) #pixel from search image
      #as the loop moves through pixels of template, it also moves through pixels of...
      #... the search image from the point given, the pixels are covered according to...
      #... width and height of the template
      L2 = getRed(pixel2) #luminance of search image pixel
      difflum = abs(L1 - L2) #difference in luminances
      sum += difflum #difference is added to running sum
  return sum #returns the sum
 
  
#Function 2
#Where the prior function only checked a certain area in the image...
#This function checks all areas in search image, except for the edges
def compareAll(template, searchImage): 
  w = getWidth(searchImage) #this and following lines find the width and height of the search image
  h = getHeight(searchImage)
  grayscale(template) #this and next line grayscales the two images
  grayscale(searchImage)
  BIG = 99999999
  matrix = [[BIG for i in range(w)] for j in range(h)] #initializing the 2D array
  for x in range(w - (getWidth(template))): 
    for y in range(h - (getHeight(template))):
      matrix [x][y] = compareOne(template, searchImage, x, y) #calling the compareOne function...
      #to check from the pixel in this iteration
  return matrix #returns the matrix

#Function 3
#returns the position of the minimum values in a 2D array
#since values in array contain difference in luminance between search and template image
#the position of the least values reflect where the template is in the search image
def find2Dmin(matrix):
  mincol, minrow = 0, 0 #variables holds where the small values are in the array
  min = 10000000 #a large number
  for j in range(len(matrix)): #for number in a row
    for i in range(len(matrix[j])): #for number in a column
      if matrix[j][i] < min: #if the values are less than max...
        mincol = i #... their position in array is stored here...
        minrow = j #... and here and the values are...
        min = matrix[j][i] #... set as the max variable
  return (minrow, mincol) #returns minrow and mincol as xy-coordinates of pixel
      
#Function 4
#creates a box in the search image
#inputs determine color of box, width, height and location
def displayMatch(searchImage, x1, y1, w1, h1, color):
  for i in range(3): #the for loop gives box width of 3, as needed
    addRect(searchImage, x1 - i, y1 - i, w1, h1, color) #by creating three boxes on top...
    #... of each other

#Function 5
#grayscales picture  
def grayscale(picture): 
  for pixel in getPixels(picture):
    L = (getRed(pixel) + getGreen(pixel) + getBlue(pixel)) / 3 #finding luminance value
    setColor(pixel, makeColor(L, L, L)) #setting color of pixel to luminance value
    
#Function 6
#calls on all the other functions written above
#looks through the search image for template after both are grayscaled
#once found, a box is drawn around it
def findWaldo(targetJPG, searchJPG):
  matrix = compareAll(targetJPG, searchJPG) #looks for template in search image
  x, y = find2Dmin(matrix) #finds the coordinate in search image where template is located
  displayMatch(searchJPG, x, y, getWidth(targetJPG), getHeight(targetJPG), red) #based on...
  #... where the template is found, a box is drawn around it.
  
  
  

  