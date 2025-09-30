from flask import Flask
app= Flask(__name__)
@app.route("/")
def inicio():
    msj='''
    <h1>bienvenido a mi calculadora chafa<h1>
    <footer>
    <p>Dylan<p>
    
    </footer>
    
    
    '''
    return msj
@app.route("/suma/v1/v2")
def suma(v1,v2):
    num1=int(v1)
    num2=int(v2)
    r=num1+num2
    return(r"la suma de {v1} y {v2} es {r}")

@app.route("/resta/v1/v2")
def resta(v1,v2):
    num1=int(v1)
    num2=int(v2)
    r=num1-num2
    return(r"la resta de {v1} y {v2} es {r}")
@app.route("/multiplicacion/v1/v2")
def mult(v1,v2):
    num1=int(v1)
    num2=int(v2)
    r=num1*num2
    return(r"la multiplicacion de {v1} y {v2} es {r}")
@app.route("/division/v1/v2")
def divisiom(v1,v2):
    num1=int(v1)
    num2=int(v2)
    r=num1/num2
    return(r"la division de {v1} y {v2} es {r}")
@app.route("/mayor/v1/v2")
def mayor(v1,v2):
    num1=int(v1)
    num2=int(v2)
    if num1>num2:
        return("el {num1} es mayor")
    else:
        return("el {num2} es mayor")
@app.route("/menor/v1/v2")
def menor(v1,v2):
    num1=int(v1)
    num2=int(v2)
    if num1>num2:
        return("el {num2} es menor")
    else:
        return("el {num1} es menor")

if __name__=="__main__":
    app.run(debug=True)