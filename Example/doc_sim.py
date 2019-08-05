#import required modules
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
import random
from matplotlib.widgets import TextBox
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import pandas as pd

#fetch test-id names from text file
file=open("doc_names.txt","r")
name=file.read()
file.close()

#because, names are seperated by "\n"
name=name.split("\n")

#fetch embedings(vectors) from text file
file=open("embeds.txt","r")
embeds=file.read()
file.close()

#because vectors are seperated by 'end'
embeds=embeds.split("end")
embeds.pop()

#convert extracted embedings(vectors) strings to float and store in variable- vec
vector=[]
for each in embeds:
    vector.append([])
    b=each.split()
    for i in b:
        vector[-1].append(float(i))


#use PCA to for transforming 'number of files * vector length' to '1*2'(coordinates).
#Decription- convert huge matrix of vector to coordinates in order to plot them in 2-D space        
pca = PCA()
y1 = pca.fit_transform(vector)
y1 = TSNE(n_components=2).fit_transform(y1)

#store x-coordinates and y-coordinates seperately
x=[i[0] for i in y1]
y=[i[1] for i in y1]

#initialize a plot canvas
fig1,ax = plt.subplots()
sc1 = plt.scatter(x,y,s=50,c=[[0.2,0.4,0.7]])

#initialize annotation  (further mannipulated)
annot = ax.annotate("", xy=(0,0), xytext=(10,10),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

#funtion for updation of annotation when hovered upon
def update_annot(ind):
    pos1 = sc1.get_offsets()[ind["ind"][0]]
    annot.xy = pos1
    text = "{}".format(" ".join([name[n] for n in ind["ind"]]))    
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor([1,1,1])
    annot.get_bbox_patch().set_alpha(1)

#hover callback function
def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc1.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig1.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig1.canvas.draw_idle()

#function for managing subplot
def subplt(ind,knn):
    output =[]
    bb=ind
    
    #function for updating annotation in subplot
    def update_bnnot(ind):
        pos2 = sc2.get_offsets()[ind["ind"][0]]
        bnnot.xy = pos2
        text = "{}".format(" ".join([output[n] for n in ind["ind"]]))
        bnnot.set_text(text)    
        bnnot.get_bbox_patch().set_facecolor([1,1,1])
        bnnot.get_bbox_patch().set_alpha(1)

    #hover-callback function for subplot
    def hove(event):
        vis = bnnot.get_visible()
        if event.inaxes == bx:
            cont, ind = sc2.contains(event)
            if cont:
                update_bnnot(ind)
                bnnot.set_visible(True)
                fig2.canvas.draw_idle()
            else:
                if vis:
                    bnnot.set_visible(False)
                    fig2.canvas.draw_idle()
    
    #knn,rel_inp are number of nearest neighbor entered by user
    rel_inp=knn

    #find euclidean distance amongst given vector and all pairs
    eucledian = pd.Series(euclidean_distances([vector[ind]], vector).flatten())
    k_largest=[]

    #select k nearest neighbors of given test case and store  them in k_largest
    for i,j in eucledian.nsmallest(int(rel_inp)).iteritems():
        output.append(name[i])
        k_largest.append(y1[i])

    #seperate x, y- coordinates for purpose of plotting    
    subx=[i[0] for i in k_largest]
    suby=[i[1] for i in k_largest]
    fig2,bx = plt.subplots()
    sc2 = plt.scatter(subx,suby,s=50,c=[[0.2,0.4,0.7]])

    #annotations for subplot
    bnnot = bx.annotate("", xy=(0,0), xytext=(10,10),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
    bnnot.set_visible(False)
    cnnot = bx.annotate("", xy=(0,0), xytext=(10,10),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
    cnnot.set_visible(False)
    #connect the callback function
    fig2.canvas.mpl_connect("motion_notify_event", hove)
    
    plt.show()

#callback function to manage click
def onclick(event):
        #get text of clicked test case
        id_name=annot.get_text()
        #if test-case is invalid
        if(str(event.button)=='MouseButton.RIGHT' and id_name not in name):
            print("Please enter a valid test id")
        #if testcase is valid
        elif(str(event.button)=='MouseButton.RIGHT'):
            knn=input("enter k-- ")
            print(id_name)
            ind=name.index(id_name)
            #call subplot function to create subplot 
            subplt(ind,knn)

#function for submitting text (when submitted using text-box, enter id of document and number of similar documnets you need seperated by a '-')
def submit(text):
    data = "Test ID : "+str(text.split('-')[0])
    knn=int(text.split('-')[1])
    print(data)
    #if test-id is not valid
    if(data not in name):
        print("Please enter a valid test id")
    #if test-id is invalid
    else:
        ind=name.index(data)
        subplt(ind,knn)
        
#create text-box at bottom of plot
axbox = plt.axes([0.122, 0.01, 0.5, 0.05])
text_b = TextBox(axbox, 'Enter test-id')
text_b.on_submit(submit)

#connect the callback function
fig1.canvas.mpl_connect('button_press_event', onclick)
fig1.canvas.mpl_connect("motion_notify_event", hover)

#show plot
plt.show()

    
