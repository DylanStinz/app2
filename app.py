from flask import Flask
app= Flask(__name__)
@app.route("/")
def inicio():
    msj='''
    <h1>bienvenido a mi calculadora chafa<h1>
    <p>para sumar ingresa este link /suma/v1/v2 donde v1 y v2 son los numeros a sumar<p>
    <p>para restar ingresa este link /resta/v1/v2 donde v1 y v2 son los numeros a restar<p>
    <p>para multiplicar ingresa este link /multiplicacion/v1/v2
    <p>para dividir ingresa este link /division/v1/v2 donde v1 y v2 son los numeros a dividir<p>
    <p>para saber cual numero es mayor ingresa este link /mayor/v1/v2<p>
    <p>para saber cual numero es menor ingresa este link /menor/v1/v2<p>
    <footer>
    <p>Dylan Stinze Reyes<p>
    <p>5:D<p>
    <p>CETis 61<p>
    <p>programacion<p>
    </footer>
    
    
    '''
    return msj
@app.route("/suma/<v1>/<v2>")
def suma(v1,v2):
    num1=int(v1)
    num2=int(v2)
    r=num1+num2
    return(f"la suma de {v1} y {v2} es {r}")

@app.route("/resta/<v1>/<v2>")
def resta(v1,v2):
    num1=int(v1)
    num2=int(v2)
    r=num1-num2
    return(f"la resta de {v1} y {v2} es {r}")
@app.route("/multiplicacion/<v1>/<v2>")
def mult(v1,v2):
    num1=int(v1)
    num2=int(v2)
    r=num1*num2
    return(f"la multiplicacion de {v1} y {v2} es {r}")
@app.route("/division/<v1>/<v2>")
def divisiom(v1,v2):
    num1=int(v1)
    num2=int(v2)
    r=num1/num2
    return(f"la division de {v1} y {v2} es {r}")
@app.route("/mayor/<v1>/<v2>")
def mayor(v1,v2):
    num1=int(v1)
    num2=int(v2)
    if num1>num2:
        return(f"el {num1} es mayor")
    else:
        return(f"el {num2} es mayor")
@app.route("/menor/<v1>/<v2>")
def menor(v1,v2):
    num1=int(v1)
    num2=int(v2)
    if num1>num2:
        return(f"el {num2} es menor")
    else:
        return(f"el {num1} es menor")

if __name__=="__main__":
    app.run(debug=True)