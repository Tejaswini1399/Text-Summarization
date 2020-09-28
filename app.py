from flask import Flask
from flask import request
import helper
from flask import jsonify
app=Flask(__name__)
@app.route('/result/',methods=['GET'])
def prediction():
          input=str(request.args.get('url'))
          out=helper.get_output(input)
          dict={0:out[0],1:out[1],2:out[2],3:out[3],4:out[4]}
          return jsonify(dict)
if __name__=='__main__':
    app.run(port=5000,host='0.0.0.0')