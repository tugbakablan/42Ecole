#!/usr/bin/env python
# coding: utf-8

# # Spam or Ham (project 1)
# 
# ## 1- Introduction with the Bernoulli model
# 
# 
# We say that a random variables $X \in \{0, 1\}$ follows a Bernoulli distribution of parameter $\theta$ if $\mathbb{P}(X = 1) = \theta$ and $\mathbb{P}(X = 0) = 1 − \theta$.
# 
# 
# 1.  Show that we can write the probability distribution of $X$ in a compact form as : 
# $$
# \mathbb{P}(X = x) = \theta^{x} (1 − \theta)^{1−x}
# $$
# 
# 2. Suppose now that we have a set of n independent variables $x_1,...,x_n$. If we note $n_1 = \sum_{i=1}^n \mathbb{1}_{\{x_i=1\}}$ and $n_0 = n − n_1$, show that :
# $$
# \mathbb{P}(x_1,\ldots,x_n \mid \theta)=\theta^{n_1} (1−\theta)^{n_0}
# $$
# 
# 3. Show that the maximum likelihood estimator is $\hat{\theta}_{ML} = \frac{n_1}{n}$
# 
# 4. A conjugate prior for the Bernoulli distribution is the Beta distribution. 
# $$
# Beta(\theta \mid a, b) \propto \theta^{a−1} (1 − \theta)^{b−1}
# $$
# The Beta distribution has the following properties for its expectation and mode (for more details you can look in one of the books like the Bishop):
# $$
# \mathbb{E}(\theta) = \frac{a}{a+b} \text{, mode}(\theta) = \frac{a-1}{a+b-2}
# $$
# 
# Show that with a $Beta(a,b)$ prior the posterior distribution 
# $\mathbb{P}(\theta \mid x_1,\ldots, x_n)$
# is proportional to $\theta^{n_1+a-1} \cdot (1 − \theta)^{n_0+b-1}$ 
# 
# 5. (Those two questions are optional, you can also simply use the result in the following)
# 
#   a. Show that the maximum a posteriori _mode_ estimate is in the form $\bar{\theta}_{MAP} = \frac{n_1+a-1}{n+a+b-2}$
# 
#   b. Show that the maximum a posteriori 
# _mean_ estimate is in the form $\hat{\theta}_{MAP} = \mathbb{E}(\theta \mid x_1,\ldots, x_n) = 
# \int_{\theta =0}^1 \mathbb{P}(\theta \mid x_1\ldots x_n) d\theta  = \frac{n_1+a}{n+a+b}$
# 

# ### 1. Compact Form of the Bernoulli Distribution
# 
# A random variable \( X \in \{0, 1\} \) follows a Bernoulli distribution with parameter \( \theta \in [0, 1] \) if:
# 
# \[
# \mathbb{P}(X = 1) = \theta \quad \text{and} \quad \mathbb{P}(X = 0) = 1 - \theta
# \]
# 
# Let's show that this can be written in the following compact form:
# 
# \[
# \mathbb{P}(X = x) = \theta^x (1 - \theta)^{1 - x}
# \]
# 
# ---
# 
# #### 🔹 Case 1: \( x = 1 \)
# 
# If \( x = 1 \), we can calculate:
# 
# \[
# \mathbb{P}(X = 1) = \theta^1 (1 - \theta)^{1 - 1} = \theta \cdot 1 = \theta
# \]
# 
# ✅ This matches the definition.
# 
# ---
# 
# #### 🔹 Case 2: \( x = 0 \)
# 
# If \( x = 0 \), we get:
# 
# \[
# \mathbb{P}(X = 0) = \theta^0 (1 - \theta)^{1 - 0} = 1 \cdot (1 - \theta) = 1 - \theta
# \]
# 
# ✅ This also matches the definition.
# 
# ---
# 
# ### ✅ Conclusion:
# 
# The expression
# 
# \[
# \mathbb{P}(X = x) = \theta^x (1 - \theta)^{1 - x}
# \]
# 
# correctly describes both cases (\( x = 0 \) and \( x = 1 \)) and thus represents a **compact and general form** of the Bernoulli distribution.
# 
# ---
# 
# ### 2. Likelihood of a Set of Independent Bernoulli Trials
# 
# Suppose we have a dataset consisting of \( n \) independent observations:
# 
# \[
# x_1, x_2, \ldots, x_n \quad \text{where each} \quad x_i \in \{0, 1\}
# \]
# 
# Each \( x_i \) is assumed to follow a Bernoulli distribution with the same parameter \( \theta \). Since the observations are independent, the joint probability (likelihood) of the dataset is the product of the individual probabilities:
# 
# \[
# \mathbb{P}(x_1, x_2, \ldots, x_n \mid \theta) = \prod_{i=1}^{n} \mathbb{P}(x_i \mid \theta)
# \]
# 
# From **Question 1**, we know:
# 
# \[
# \mathbb{P}(x_i \mid \theta) = \theta^{x_i} (1 - \theta)^{1 - x_i}
# \]
# 
# So we can write:
# 
# \[
# \mathbb{P}(x_1, \ldots, x_n \mid \theta) = \prod_{i=1}^{n} \theta^{x_i} (1 - \theta)^{1 - x_i}
# \]
# 
# ---
# 
# #### 🔹 Combine the powers:
# 
# Let:
# - \( n_1 = \sum_{i=1}^{n} \mathbb{1}_{\{x_i = 1\}} \): the number of 1's in the dataset
# - \( n_0 = n - n_1 \): the number of 0's
# 
# Then:
# 
# \[
# \prod_{i=1}^{n} \theta^{x_i} (1 - \theta)^{1 - x_i} = \theta^{n_1} (1 - \theta)^{n_0}
# \]
# 
# ---
# 
# ### ✅ Conclusion:
# 
# The likelihood of the dataset is:
# 
# \[
# \mathbb{P}(x_1, \ldots, x_n \mid \theta) = \theta^{n_1} (1 - \theta)^{n_0}
# \]
# 
# This compact expression summarizes the contribution of all 1's and 0's in the dataset to the likelihood.
# 
# ---
# 
# ### 3. Maximum Likelihood Estimation (MLE) of \( \theta \)
# 
# We are given a dataset \( x_1, x_2, \ldots, x_n \), where each \( x_i \in \{0, 1\} \) follows a Bernoulli distribution with parameter \( \theta \). 
# 
# From **Question 2**, the likelihood function is:
# 
# \[
# \mathbb{P}(x_1, \ldots, x_n \mid \theta) = \theta^{n_1} (1 - \theta)^{n_0}
# \]
# 
# Where:
# - \( n_1 = \sum_{i=1}^{n} x_i \)
# - \( n_0 = n - n_1 \)
# 
# ---
# 
# #### 🔹 Step 1: Log-Likelihood
# 
# We take the natural logarithm of the likelihood function to obtain the log-likelihood:
# 
# \[
# \log \mathcal{L}(\theta) = \log \left( \theta^{n_1} (1 - \theta)^{n_0} \right)
# = n_1 \log \theta + n_0 \log (1 - \theta)
# \]
# 
# ---
# 
# #### 🔹 Step 2: Differentiate and Maximize
# 
# To find the MLE, we take the derivative of the log-likelihood with respect to \( \theta \):
# 
# \[
# \frac{d}{d\theta} \log \mathcal{L}(\theta) = \frac{n_1}{\theta} - \frac{n_0}{1 - \theta}
# \]
# 
# Set the derivative to zero to find the maximum:
# 
# \[
# \frac{n_1}{\theta} - \frac{n_0}{1 - \theta} = 0
# \]
# 
# Multiply both sides by \( \theta(1 - \theta) \):
# 
# \[
# n_1 (1 - \theta) = n_0 \theta
# \]
# 
# \[
# n_1 - n_1 \theta = n_0 \theta
# \]
# 
# \[
# n_1 = (n_0 + n_1) \theta = n \theta
# \]
# 
# ---
# 
# ### ✅ Maximum Likelihood Estimator:
# 
# \[
# \hat{\theta}_{ML} = \frac{n_1}{n}
# \]
# 
# This is simply the proportion of 1's in the dataset.
# 
# ---
# 
# ### 4. Posterior Distribution with Beta Prior (Conjugacy)
# 
# We are using a **Beta prior** for the Bernoulli distribution parameter \( \theta \):
# 
# \[
# \text{Prior: } \mathbb{P}(\theta) = \text{Beta}(\theta \mid a, b) \propto \theta^{a - 1}(1 - \theta)^{b - 1}
# \]
# 
# From **Question 2**, the likelihood of the data \( x_1, \ldots, x_n \) is:
# 
# \[
# \mathbb{P}(x_1, \ldots, x_n \mid \theta) = \theta^{n_1}(1 - \theta)^{n_0}
# \]
# 
# Where:
# - \( n_1 = \sum_{i=1}^{n} x_i \)
# - \( n_0 = n - n_1 \)
# 
# ---
# 
# #### 🔹 Posterior Derivation
# 
# Using **Bayes' Theorem**:
# 
# \[
# \mathbb{P}(\theta \mid x_1, \ldots, x_n) \propto \mathbb{P}(x_1, \ldots, x_n \mid \theta) \cdot \mathbb{P}(\theta)
# \]
# 
# Substitute the expressions for likelihood and prior:
# 
# \[
# \mathbb{P}(\theta \mid x_1, \ldots, x_n) \propto \theta^{n_1}(1 - \theta)^{n_0} \cdot \theta^{a - 1}(1 - \theta)^{b - 1}
# \]
# 
# \[
# = \theta^{n_1 + a - 1} (1 - \theta)^{n_0 + b - 1}
# \]
# 
# ---
# 
# ### ✅ Conclusion:
# 
# The posterior distribution is a **Beta distribution**:
# 
# \[
# \mathbb{P}(\theta \mid x_1, \ldots, x_n) \propto \theta^{n_1 + a - 1} (1 - \theta)^{n_0 + b - 1}
# = \text{Beta}(\theta \mid n_1 + a, n_0 + b)
# \]
# 
# This confirms the conjugacy: the **posterior** is in the **same family** as the **prior** (Beta).
# 

# ## Spam classifier
# 
# The goal of this small project is to use a Naive bayes classifier to build a spam filter. To build our filter, we will use a dataset of 5,572 SMS messages put together by Tiago A. Almeida and José María Gómez Hidalgo. 
# The dataset and the article describing the dataset are in the whiteboard directory together with this notebook. Of note, the SMS messages have already been processed for ease of use: all punctuation marks have been removed and the text has been transformed into lowercase. It is also common practice to remove any stop words such as `a`, `as`, `the` and to perform stemming (reduce words to their base form, such as stripping  the final `s*` in plural words, or the `*ing` from verbs (e.g., running becomes run)). For the sake of simplicity, we did not do that in this exercise.
# 
# We will use a bag of word model:
#  - We construct a corpus of the possible words $\mathcal{D} = \{w_1, \ldots , w_d\}$.
#  - Each document is described by a vector of binary values $(x^{(1)}, \ldots , x^{(d)})$ where $x^{(i)} = 1$ if $w_i$ occurs in the document and $0$ otherwise.
# 
# The classification task is to predict for an SMS message if it is a _spam_ or a _ham_ (e.g. non-spam).
# 
# Our data is thus $\mathbf{x} = (x^{(1)},\ldots, x^{(d)})$, $x^{(i)} \in \{0,1\}$ and $y \in \{s,h\}$
# We hypothesise that the values $x^{(i)}$ are drawn according to a Bernoulli distribution whose parameter depends on the class:
# $$
# \mathbb{P}(x^{(i)} \mid y = s) = \theta_{i,s}^{x^{(i)}} \cdot (1-\theta_{i,s})^{1-x^{(i)}}
# $$
# and 
# $$
# \mathbb{P}(x^{(i)} \mid y = h) = \theta_{i,h}^{x^{(i)}} \cdot (1-\theta_{i,h})^{1-x^{(i)}}
# $$
# As we will use a naive Bayes classifier, the occurences of the different words are independent from each other.
# \begin{align}
# \mathbb{P}(\mathbf{x} \mid y = s) & = \prod_{i=1}^{d} \mathbb{P} (x^{(i)} \mid y = s)\\
#   & =  \prod_{i=1}^{d} \theta_{i,s}^{x^{(i)}} \cdot (1-\theta_{i,s})^{1-x^{(i)}}
# \end{align}
# 

# ## Importing library
# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from collections import Counter

##Load the dataset (if in the same directory as the notebook)
sms_data = np.loadtxt("C:/Users/TUĞBA KABLAN/Desktop/ML-Spam Clasifier/02-2-SpamClassifier/SMSSpamCollection_cleaned.csv", delimiter="\t", skiprows=1, dtype=str)

## create test data set for checkpointing
checkpoint_data = np.array([['spam', 'dear researcher submit manuscript money'], 
          ['ham','dear friend meet beer'],
          ['ham', 'dear friend meet you']], dtype=str)


# In[12]:


##Check the dataset
sms_data


# In[9]:


## Check the size of the dataset
num_messages = sms_data.shape[0]
print(f"Total message number in data group: {num_messages}")

## Third message is a...
print("Third messages's etiquet:", sms_data[2][0])

## Dividing the third message into words
print("Dividing the third message into the words :", sms_data[2][1].split())


# ## 2 - Construction of the Corpus
# 
# Construct the corpus $\mathcal{D}$ of all words in the dataset. The corpus will be represented as a hash table where each key is a unique word in the dataset and each value is the row index for that word. 
#  - How many unique words are there? 
#  - What are the 10 most common words (_e.g._ occuring in the most documents)?
#  - Transform the set of messages in the form of a binary matrix of word occurrences.
#  
#  You can evaluate whether your implementation works using the checkpoint_data array. For this dataset the corpus could look as follows :
# 
# `{'dear': 0, 'researcher': 1, 'submit': 2, 'manuscript': 3, 'money': 4, 'friend': 5, 'meet': 6, 'beer': 7, 'you': 8}`
# (of course you could have other index values for the words). 
# 
# The recoding of the checkpoint data will give you the following numpy array:
# 
# ```
# [[1. 1. 1. 1. 1. 0. 0. 0. 0.]
#  [1. 0. 0. 0. 0. 1. 1. 1. 0.]
#  [1. 0. 0. 0. 0. 1. 1. 0. 1.]]
# ```

# In[11]:


def construct_corpus(data):
    """
    np.array[str, str] -> dict[str:int]
    
    from a 2D array of str, return a hash table
    """
    corpus = {}  # Initialize an empty dictionary to store words and their row index
    row_index = 0  # This will track the index of each message in the data

    # Loop over the rows of the data
    for label, message in data:
        words = message.split()  # Split the message into words
        
        for word in words:
            if word not in corpus:  # If the word is not already in the corpus
                corpus[word] = row_index  # Add the word with the current row index
        
        row_index += 1  # Move to the next message

    return corpus  # Return the constructed corpus

# Test the function with some data
sms_data = np.array([['ham', 'go until jurong point crazy available only in bugis n great world la e buffet cine there got amore wat'],
                     ['ham', 'ok lar joking wif u oni'],
                     ['spam', 'free entry in 2 a wkly comp to win fa cup final tkts 21st may 2005 text fa to 87121 to receive entry question std txt rate t c s apply 08452810075over18 s']])

# Construct the corpus from the data
corpus = construct_corpus(sms_data)

# Display the corpus (first 10 words for brevity)
print({k: corpus[k] for k in list(corpus.keys())[:10]})



# In[ ]:


def recode_messages(data, corpus):
    """
    np.array[str, str] * dict[str:int] -> np.array[int, int]
    
    returns the binary matrix encoding 
    """
    num_messages = data.shape[0]  # Number of messages
    num_words = len(corpus)  # Number of unique words in the corpus
    matrix = np.zeros((num_messages, num_words))  # Create a matrix with all zeros
    
    for i, (label, message) in enumerate(data):
        words = message.split()  # Split the message into words
        
        for word in words:
            if word in corpus:  # If the word is in the corpus
                word_index = corpus[word]  # Get the index of the word from the corpus
                matrix[i, word_index] = 1  # Mark the presence of the word in the binary matrix
    
    return matrix

D = construct_corpus(sms_data)  # Construct the corpus
sms_matrix = recode_messages(sms_data, D)  # Convert messages into binary matrix

print(sms_matrix)


D = construct_corpus(sms_data)

sms_matrix = recode_messages(sms_data, D)


# ## 3 - Construct a training and a testing set and estimation of parameters
# 
# 
# To do the evaluation of the model afterward we will split the dataset randomly in two: 
# - one dataset for training (80% of the messages) 
# - one dataset for testing (20% of the messages).
# 
# If you are familiar with it, you can use the `sklearn.model_selection` functions to construct the train and test datasets.
# 

# In[15]:


from sklearn.utils import shuffle

def train_test_split(X, Y, train_percentage=0.8):
    assert X.shape[0] == Y.shape[0]

    number_examples = X.shape[0]
    num_train = int(train_percentage * number_examples)
  
    assert X.shape[0] == Y.shape[0]
    
    X, Y = shuffle(X, Y, random_state=42)
    
    number_examples = X.shape[0]
    num_train = int(train_percentage * number_examples)
    
    X_train, Y_train = X[:num_train], Y[:num_train]
    X_test, Y_test = X[num_train:], Y[num_train:]
    
    return X_train, Y_train, X_test, Y_test

X = sms_matrix  
Y = sms_data[:, 0] 

X_train, Y_train, X_test, Y_test = train_test_split(X, Y)

print(f"Training set size: {X_train.shape[0]} messages")
print(f"Testing set size: {X_test.shape[0]} messages")
    


# ## 4 - Estimation of the model parameters
# 
# We will now estimate our model on the training set. This means estimating two types of parameters: the class prior, and the conditional word occurence probabilities.
# 
# 1.  Estimate the class prior $\mathbb{P}(c) = \mathbb{P}(y = c), (c = s, h)$
# 2.  Using the results from section 1, compute the Maximum a posteriori estimator for the $d \times 2$ matrix of parameters.
# $$
# \Theta = \left(
# \begin{array}{cc}
# \theta_{1,h}   & \theta_{1,s} \\
# \theta_{2,h} & \theta_{2,s} \\
# \vdots & \vdots \\
# \theta_{d,h} & \theta_{d,s} \\
# \end{array}
# \right).
# $$ You can use as conjugate prior a Beta(1, 1) distribution for instance (then $\theta_{i,c} = \frac{n_{i,c}+1}{N+2}$ where $n_{i,c}$ is the number of documents from the class $c$ where the word $w_i$ is present and $N$ is the total number of documents).
# 
# When applied to the checkpoint data, your $\Theta$ matrix should look like this:
# 
# ```
# # h    s
# [[0.75 0.66666667]  #'dear'
#  [0.25 0.66666667]  #'researcher'
#  [0.25 0.66666667]  #'submit'
#  [0.25 0.66666667]  #'manuscript'
#  [0.25 0.66666667]  #'money'
#  [0.75 0.33333333]  #'friend'
#  [0.75 0.33333333]  #'meet'
#  [0.5  0.33333333]  #'beer'
#  [0.5  0.33333333]] #'you'
# ```
# 
# 3. Represent the fitted class conditional densities $(\theta_{i,h})_{i \in \mathcal{D}}$ and $(\theta_{i,s})_{i \in \mathcal{D}}$ like on the corresponding slide of the course.
# 

# In[3]:


import numpy as np

def estimate_proportions(data_matrix, labels):
    """
    Estimate the matrix theta from a binary data matrix and class labels.
    
    """
    d = data_matrix.shape[1]
    theta = np.zeros((d, 2))  # 0: ham, 1: spam

    ham_indices = np.where(labels == 'ham')[0]
    spam_indices = np.where(labels == 'spam')[0]

    N_ham = len(ham_indices)
    N_spam = len(spam_indices)

    for i in range(d):
        n_i_ham = np.sum(data_matrix[ham_indices, i])
        n_i_spam = np.sum(data_matrix[spam_indices, i])

        # Apply Beta(1,1) prior smoothing
        theta[i, 0] = (n_i_ham + 1) / (N_ham + 2)
        theta[i, 1] = (n_i_spam + 1) / (N_spam + 2)

    return theta

# Test data
Dico = {'dear': 0, 'researcher': 1, 'money': 2, 'friend': 3}
datam = np.array([
    [1, 0, 1, 1],  # spam
    [1, 1, 0, 1],  # ham
    [0, 0, 1, 1]   # ham
], dtype=int)

labels = np.array(['spam', 'ham', 'ham'])

# Run function
theta = estimate_proportions(datam, labels)
print(theta)


# ## 4 - Message classification
# 
# 
# 3. Classify the messages in the test set using the Maximum a posteriori rule, and evaluate the performance of the model by computing the True Positive Rate (also called Sensitivity) and the False Positive Rate (the same as 1-Specificity).
# 
# 4. The performance of the model above was obtained by using a classification threshold of $0.5$ on the posterior probability. In other words, if $\mathbb{P}(y = s \mid \mathbb{x}) \ge 0.5$ then the message is classified as spam. Draw a ROC curve for your classifier. Note that you have to consider multiple values of the threshold to draw the ROC curve. 
# 
# 5. Why did we use the Maximum a posteriori estimator rather than the maximum likelihood one?
# 
# 
# 

# ## 5 - Extension of the model 
# 
# One extension of the model is to consider a matrix of word counts instead of simply their presence/absence. 
# The model will change in various ways in this case: 
#    - We will count the total number of occurence in the spam or the ham set for each word.
#    - the words are now considered to occur independently along the sentence (independent Multinoulli). Thus, for a document with k words $\mathbf{v}=(v_1,\ldots, v_k)$
#     \begin{align}
#     \mathbb{P}(\mathbf{v} \mid y = s) 
#   & =  \prod_{t=1}^{k} p_{v_t}
#     \end{align}
#        where $p_v$ is the probability to observe a word $v$
#        
# Note that with this new model we compute a product over the positions in the sentence while the bernoulli model did a product over all the words in the corpus.
# 
# 1. Implement the estimation of parameters for this model and the computation of the posterior class probabilities. This question can be interpreted in different ways, please explain your choices.
# 2. Compare its accuracy and ROC curve with the previous model on a test set (*e.g.* go over section 3 and 4 again for this model).
# 
# 
