# Document-similarity-visualization-using-NLP-and-Elmo
Helps in visualization of documents in 2-D space and find most similar documents to a given document. Also, works for  a small set of documents.

The semantic clustering is performed via a two stage process:
1.	Training - Creation of embedding (vectors for mathematical representation) per test case, by training the input feed data on ELMo (pre-trained on 1 Billion Word Benchmark language model).

2.	Inference - Clustering of test cases on the basis of embedding obtained in the previous stage, after applying some suitable dimensionality reduction as well as transformation.

Stage 1: Training the dataset for creating embeddings for test cases
•	Upload all the documents containing concerned test cases in the Files tab on Google Colab.

•	Run the code cells subsequently.

•	Once the inferring part is finished (when the last cell completes execution), click the Refresh tab beside the Files tab.

•	Two new files will be displayed- doc_names.txt and embeds.txt

•	Download them and save them in a folder named cluster, along with doc_sim.py

Stage 2: Clustering the test cases and its visualization

•	Open the Anaconda Prompt with admin permission OR cmd with admin rights (if Python3 and other prerequisites have been pre-installed), and browse to location where the folder cluster is saved.

•	Type python doc_sim.py and press Enter.
A graph will pop up depicting the clustered documents.

Use the zoom option in the panel at the bottom of that window to zoom in some area, and pan option to move around.
Also, right-click on a test-case-of-interest and enter the value of k (no. of nearest test cases to be analyzed) in the terminal OR enter it in the text bar as follows;
Format: document_name-k  
e.g. 3900-20 where 3900 is the document name and 20 is the no. of nearest neighbors to be analyzed.
A new plot will open in a new window, depicting the same.


Pre-requisites:
Programming language: Python 3
Libraries required:  matplotlib, numpy, scikit-learn, pandas
(Libraries are pre-installed in Anaconda. To install additional lib, run in Anaconda prompt: conda install lib-name)

Setup Environment variable for python:
•	Locate the PATH where Python has been installed.
•	Search environment in the Win search bar and open “Edit the system environment variables”.
•	In the Advanced tab, click on “Environment Variables…”, and in the upper section i.e. user variables for Admin, Click on “New…” 
option, and enter details as follows:

	Variable name: Path
	Variable value : Path-to-python-folder
and save it, and close the dialog boxes.

Note: The main strength of this model lies on transfer learning, and it has been trained on 1 Billion Word benchmark dataset which is generally able to capture context for almost all English sentences/words.
Hence, for better accuracy and performance, please try to use sentences as much as possible for description instead of short forms/codes (if possible), and also try to include the meaning of certain technical terms in brackets or one or two occurrences.


