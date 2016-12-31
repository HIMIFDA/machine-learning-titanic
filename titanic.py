'''

YES YOU CAN

'''
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np

# Data preprocessing
# Drop everything we don't need
# Change our label y to one-hot encoding
# Split our data into two parts, train and testing
titanic_df = pd.read_excel("data/titanic3.xls", "titanic3", index_col=None, na_values=["NA"])
titanic_df.index = titanic_df["body"]
titanic_df.index = titanic_df["cabin"]
titanic_df.index = titanic_df["boat"]
titanic_df["home.dest"] = titanic_df["home.dest"].fillna("NA")
titanic_df = titanic_df.drop(["body","cabin","boat"], axis=1)
titanic_df = titanic_df.dropna()

def preprocess_titanic_df(df):
    processed_df = df.copy()
    le = preprocessing.LabelEncoder()
    processed_df.sex = le.fit_transform(processed_df.sex)
    processed_df = processed_df.drop(["name", "ticket", "home.dest", "sibsp", "parch", "fare", "embarked"], axis=1)
    processed_df['deceased'] = processed_df['survived'].apply(lambda s: 1 - s)
    processed_X = processed_df[['sex', 'age', 'pclass']].as_matrix()
    processed_y = processed_df[['deceased', 'survived']].as_matrix()
    return processed_X, processed_y

dataset_X, dataset_y = preprocess_titanic_df(titanic_df)

X_train, X_test, y_train, y_test = train_test_split(dataset_X, dataset_y, test_size=0.2, random_state=42)

################################
# Constructing Dataflow Graph
################################

# define placeholder for our features and labels
# X is None x 3 dimensional matrix
# y is None x 2 dimensional matrix
X = tf.placeholder(tf.float32, shape=[None, 3])
y = tf.placeholder(tf.float32, shape=[None, 2])

# define our weights and bias
weights = tf.Variable(tf.random_normal([3, 2]))
bias = tf.Variable(tf.zeros([2]))
hypothesis = tf.nn.softmax(tf.add(tf.matmul(X, weights), bias))

# Minimise cost function using cross entropy
# NOTE: add a epsilon(1e-10) when calculate log(hypothesis),
# otherwise the result will be -inf
cross_entropy = - tf.reduce_sum(y * tf.log(hypothesis + 1e-10), reduction_indices=1)
cost_function = tf.reduce_mean(cross_entropy)


# use gradient descent optimizer to minimize cost function
optimizer = tf.train.GradientDescentOptimizer(0.001).minimize(cost_function)

# calculate accuracy
correct_pred = tf.equal(tf.argmax(y, 1), tf.argmax(hypothesis, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Add an op to initialize the variables.
init_op = tf.global_variables_initializer()

saver = tf.train.Saver()


################################
# Training and Evaluating the model
################################

# use session to run the calculation
with tf.Session() as sess:
    # Run the init operation.
    # it must be run before all of this shit
    sess.run(init_op)

    # training loop
    for epoch in range(50):
        total_loss = 0.
        for i in range(len(X_train)):
            # prepare feed data and run
            feed_dict = {X: [X_train[i]], y: [y_train[i]]}
            _, loss = sess.run([optimizer, cost_function], feed_dict=feed_dict)
            total_loss += loss
        # display loss per epoch
        print('Epoch: %04d, total loss=%.9f' % (epoch + 1, total_loss))

    # Accuracy
    accuracy_pred = sess.run(accuracy, feed_dict={X: X_test, y: y_test})
    print("Accuracy on validation set: %.9f" % accuracy_pred)

    # test our model 
    print("=================================")
    bingo = sess.run(hypothesis, feed_dict={X: [[0., 5., 1.]]})
    print("bingo: ", np.argmax(bingo,1))
    print("bingo: ", bingo)
    print("=================================")

    
    # save our model
    # we save our model so that we can use that on production
    saver.save(sess, 'model/titanic_softmax')
