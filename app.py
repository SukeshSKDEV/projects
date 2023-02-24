from flask import Flask, render_template, request, jsonify
import math
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')


@app.route('/math',methods=['POST'])
def math_operation():
    if request.method=='POST':
        math_ops=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if math_ops=='add':
            r=num1+num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
    
        if math_ops=='subract':
            r=num1-num2
            result = "The subtraction of " + str(num1) + ' and ' + str(num2) + " s " + str(r)
        
        if math_ops=='multiply':
            r=num1*num2
            result = "The muliplication of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
        if math_ops=='division':
            r=num1/num2
            result = "The division of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
        if math_ops=='log':
            r=math.log(num1,num2)
            result = "Logarith base  " + str(num1) + ' of ' + str(num2) + " is " + str(r)

        return render_template('results.html' , result = result)


#  POSTMAN

@app.route('/postman_data',methods=['POST'])
def math_operations():
    if request.method=='POST':
        math_ops=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])

        if math_ops=='add':
            r=num1+num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
    
        if math_ops=='subract':
            r=num1-num2
            result = "The subtraction of " + str(num1) + ' and ' + str(num2) + " s " + str(r)
        
        if math_ops=='multiply':
            r=num1*num2
            result = "The muliplication of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
        if math_ops=='division':
            r=num1/num2
            result = "The division of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
        if math_ops=='log':
            r=math.log(num1,num2)
            result = "Logarith base  " + str(num1) + ' of ' + str(num2) + " is " + str(r)

        return jsonify(result)
      

if __name__=="__main__":
    app.run(host="0.0.0.0")
