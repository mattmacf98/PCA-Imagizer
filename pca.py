import numpy as np 
import matplotlib.pyplot as plt
import random
from PIL import Image
import requests
from io import BytesIO

def kMeansInitCentroids(X,K):
    centroids = np.zeros((K, len(X[1])))

    for i in range(K):
        id = random.randint(0,len(X))
        centroids[i] = X[id]
    return centroids

def findClosestCentroids(X, centroids):
    K = len(centroids)
    idx = np.zeros((len(X),1))

    for i in range(0,len(X)):
        nearest = 0
        dist_best = np.sum((X[i,:] - centroids[0,:])*(X[i,:] - centroids[0,:]))
        for j in range(1,K):
            dist = np.sum((X[i,:] - centroids[j,:])*(X[i,:] - centroids[j,:]))
            if dist < dist_best:
                nearest = j
                dist_best = dist
        idx[i] = nearest
    return idx

def computeCentroids(X, idx, K):
    centroids = np.zeros((K,len(X[0])))
    for i in range(0,K):
        num = 0
        sum = np.zeros((1,len(X[0])))
        for j in range(0,len(X)):
            if idx[j] == i:
                sum = sum + X[j,:]
                num = num + 1
        centroids[i,:] = sum/num
    return centroids

def runMeans(X,init_centroids, max_iters,K):
    centroids = init_centroids
    for i in range(0,max_iters):
        print(i)
        idx = findClosestCentroids(X, centroids)
        centroids = computeCentroids(X, idx, K)
    return idx,centroids

def createImage(path):
    response = requests.get(path)
    img = Image.open(BytesIO(response.content))
    img.save('Img.png')

    image  = plt.imread('Img.png')
    height = len(image)
    width = len(image[0])
    if height > 256 and width > 256:
        if height > width:
            height = int((1.0*height)/width)*256
            width = 256
        else:
            width = int((1.0*width)/height)*256
            height = 256

        img = Image.open('Img.png')
        img = img.resize((height, width))
        img.save('temp.png')
        img.save('./static/images/temp.png')
        image = plt.imread('temp.png')

    
    image = np.reshape(image, (len(image)*len(image[0]),3))

    K = 8
    max_iters = 10

    initCentroids = kMeansInitCentroids(image,K)
    idx,centroids = np.array(runMeans(image, initCentroids, max_iters,K))

    idx = findClosestCentroids(image, centroids)
    X_recovered = centroids[idx.astype(int),:]

    X_recovered = np.reshape(X_recovered, (height, width, 3))
    X_recovered = (X_recovered*255).astype('uint8')
    image_r = Image.fromarray(X_recovered)
    image_r.save("./static/images/your_file.png")

