from flask import Flask, jsonify, abort, request, make_response, url_for, render_template
import numpy as np
import tensorflow as tf


app = Flask(__name__, static_url_path = "/static")

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


# main route
# render index.html
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

# endpoint to predict the probability
# we restore our tensorflow model in model folder
# and use that to make a prediction
@app.route('/api/v1.0/predict', methods = ['POST'])
def predict():
   
    X_predict = np.float32([[request.form['sex'], request.form['age'], request.form['class']]])
    
    ################################
    # Constructing Dataflow Graph
    ################################

    # create new graph
    tf_graph = tf.Graph()
    with tf_graph.as_default():

        # define placeholder for our features and labels
        # X is None x 3 dimensional matrix
        # y is None x 2 dimensional matrix
        X = tf.placeholder(tf.float32, shape=[None, 3])
        y = tf.placeholder(tf.float32, shape=[None, 2])

        # define our weights and bias
        weights = tf.Variable(tf.random_normal([3, 2]))
        bias = tf.Variable(tf.zeros([2]))

        # define out hypothesis, we use softmax regression
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

        # we use saver on production so that we dont have to train our model first
        saver = tf.train.Saver()

    # use session to run the model
    with tf.Session(graph=tf_graph) as sess:
        
        # Restore model from disk.

        new_saver = tf.train.import_meta_graph('model/titanic_softmax.meta')
        new_saver.restore(sess, tf.train.latest_checkpoint('./model'))

        # dicaprio
        # 1.
        # 20.
        # 3.
        # kate winslet
        # 0.
        # 17.
        # 1.  
        predict = sess.run(hypothesis, feed_dict={X: X_predict})
        result = np.argmax(predict, 1)


    response = {
        'endpoint': 'api/v1.0/predict',
        'method': 'POST',
        'percentage_alive': float(predict[0][1]),
        'percentage_dead': float(predict[0][0]),
        'survive': int(result[0])
    }

    return jsonify( { 'response': response } )

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
