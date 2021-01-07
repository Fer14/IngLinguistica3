



Ingredientes = ["huevos","mantequilla","leche","harina","azucar","sal"]
Valor = {}
Valor["ingredientes"] = Ingredientes
Valor["cantidad"] = {"huevos":"2 huevos","mantequilla":"30 g","leche":"250 ml","azucar":"1 cucharada","sal":"una pizca","harina":"140 g"}
Valor["tiempo"] = {"huevos":"hasta que se disuelva", "harina":"hasta obtener una masa de sonsistencia pastosa","leche":"hasta deshacer todos los grumos",
"mantequilla":"hasta que se integre con el resto de ingredientes","nevera":"almenos media hora" ,"receta":"la noche anterior a tu fenomenal desayuno","sarten":"cuando comiencen a aparecer burbujas en la masa"}
Valor["autor"] = "Guadalupe, de codigococina.com"
Valor["preparacion"] = ["batir los huevos con el azucar","añadir harina y pizquita de sal","incorpora la leche","añade mantequilla derretida en el microondas","cubre el recipiente donde tengas la masa con un papel de film y dejala reposar en la nevera",
 "vierte un poco de masa en una sarte","Ve colocando los crepes en una plato y tápalo con otro para que se mantengan calientes","decora los crepes con el topping o el relleno que prefieras"]
Valor["consejos"] = ["Si el primer crepe te sale un poco regular, es normal","Es posible que durante la preparación de los crepes tengas que volver a engrasar la sartén con otro pelín de mantequilla.","Prepara solamente los crepes que te vayas a comer en ese momento"]
Valor["utensilios"] = ["un batidor de mano","una sartén","un recipiente para la masa"]
Valor["acompañamiento"] = ["vainilla","vanela","ralladura de citricos"]


print("Haz tu pregunta. Para acabar escribe SALIR")
print("\n")
query = input().lower()


while query != "salir":


    Respuesta = ""

    if ((query.find("cuales") != -1) or (query.find("que")!= -1)) and (query.find("ingredientes")!= -1):
        Respuesta = Valor["ingredientes"]


    elif ((query.find("cuanta") != -1) or (query.find("cuantas") != -1) or (query.find("cuantos") != -1) or (query.find("cuanto") != -1)or (query.find("cantidad")!= -1)) and (any(ingredients in query for ingredients in Ingredientes)):   

        if (query.find("huevos")!= -1):
            Respuesta = Valor["cantidad"]["huevos"]
        elif (query.find("mantequilla")!= -1):
            Respuesta = Valor["cantidad"]["mantequilla"]
        elif (query.find("leche")!= -1):
            Respuesta = Valor["cantidad"]["leche"]
        elif (query.find("harina")!= -1):
            Respuesta = Valor["cantidad"]["harina"]
        elif (query.find("azucar")!= -1):
            Respuesta = Valor["cantidad"]["azucar"]
        elif (query.find("sal")!= -1):
            Respuesta = Valor["cantidad"]["sal"]

    elif (((query.find("cuanto") != -1) and (query.find("tiempo"))) or (query.find("cuando")!= -1)) and (any(ingredients in query for ingredients in Ingredientes) or query.find("sarten")!= -1 or query.find("nevera")!= -1 or query.find("receta")!= -1): 

        if (query.find("huevos")!= -1):
            Respuesta = Valor["tiempo"]["huevos"]
        elif (query.find("mantequilla")!= -1):
            Respuesta = Valor["tiempo"]["mantequilla"]
        elif (query.find("leche")!= -1):
            Respuesta =  Valor["tiempo"]["leche"] 
        elif (query.find("harina")!= -1):
            Respuesta = Valor["tiempo"]["leche"]
        elif (query.find("nevera")!= -1):
            Respuesta = Valor["tiempo"]["nevera"]
        elif (query.find("sarten")!= -1):
            Respuesta = Valor["tiempo"]["sarten"]
        elif (query.find("receta")!= -1):
            Respuesta = Valor["tiempo"]["receta"]

    elif ((query.find("quien") != -1) or (query.find("autor")!= -1)) and (query.find("receta")!= -1):
        Respuesta = Valor["autor"]

    elif ((query.find("cuales") != -1) or (query.find("que")!= -1)) and (query.find("pasos")!= -1):
        Respuesta = Valor["preparacion"]
            
    elif (query.find("que") != -1) and ((query.find("hacer")) or (query.find("hace")!= -1)) and (any(ingredients in query for ingredients in Ingredientes)): 

        if (query.find("huevos")!= -1):
            Respuesta = "preparacion" 
        if (query.find("mantequilla")!= -1):
            Respuesta = "preparacion" 
        if (query.find("leche")!= -1):
            Respuesta = "preparacion" 
        if (query.find("harina")!= -1):
            Respuesta = "preparacion" 
        if (query.find("azucar")!= -1):
            Respuesta = "preparacion" 
        if (query.find("sal")!= -1):
            Respuesta = "preparacion" 
            

    elif ((query.find("consejos") != -1) or (query.find("recomiendas")!= -1)):
        Respuesta = Valor["consejos"]        

    elif ((query.find("utensilios") != -1)):
        Respuesta = Valor["utensilios"] 

    elif ((query.find("acompañamientos") != -1) or (query.find("añadir")!= -1)):
        Valor["acompañamiento"]

######################################BIOGRAFIA################################################        

    elif ((query.find("cuando")!= -1) or (query.find("fecha")!= -1)) and (query.find("diogenes")!=-1):
    	if ((query.find("nacio")!= -1) or (query.find("nacimiento")!= -1)):
    		Respuesta ="412 a.C"
    	elif ((query.find("murio")!= -1) or (query.find("defuncion")!= -1)):
    		Respuesta ="412 a.C"


    elif ((query.find("donde")!= -1) or (query.find("lugar")!= -1)) and (query.find("diogenes")!=-1):
    	if ((query.find("nacio")!= -1) or (query.find("nacimiento")!= -1)):
    		Respuesta ="Synope"
    	elif ((query.find("murio")!= -1) or (query.find("defuncion")!= -1)):
    		Respuesta ="Corinto"
    	elif ((query.find("vivio")!= -1) or (query.find("vida")!= -1)):
    		Respuesta ="Las calles de Atenas"

    elif ((query.find("cuales")!= -1) or (query.find("como")!= -1)) and ((query.find("nombres")!= -1) or (query.find("llama")!= -1)):
    	if (query.find("diogenes")!= -1):
    		Respuesta ="“Diógenes de Synope o Diógenes el Cinico”"
    	elif query.find("padre")!= -1:
    		Respuesta = "Hicesias"
    	elif query.find("maestro")!= -1:
    		Respuesta = "Antístenes el más antiguo pupilo de Sócrates"

    elif ((query.find("trabajo") != -1) or (query.find("acupacion")!= -1)) and (query.find("padre") != -1):
        Respuesta = "Banquero"

    elif  (query.find("cual") != -1) and (query.find("filosofia de vida")!= -1):
    	Respuesta = "renunciar por todas partes lo convencional y oponer a ello su naturaleza"

    elif ((query.find("tenido") != -1) or (query.find("viviendo")!= -1)) and (query.find("qué") != -1):
        Respuesta = "un manto, un zurrón, un báculo y un cuenco"

    elif ((query.find("cual")!= -1) or (query.find("que")!= -1)) and ((query.find("mision")!= -1) or (query.find("hecho")!= -1)) and (query.find("Atenas") != -1):
        Respuesta = "de metafóricamente falsificar/desfigurar la “moneda” de las costumbres"

    elif ((query.find("definicion") != -1) and (query.find("costumbre")!= -1)):
        Respuesta = "la falsa moneda de la moralidad"

    elif (query.find("exilio")!=-1):
        if (query.find("por que")!= -1) or (query.find("razon")!=-1):
            Respuesta = "desterrados por haber fabricado moneda falsa"
        elif query.find("de donde")!=-1:
            Respuesta="exiliado de su ciudad natal Synope"

    elif ((query.find("a quien") != -1) or (query.find("cual fue")!= -1)) and ((query.find("conocia") != -1) or (query.find("conocidas") != -1)):
        Respuesta = "Alejandro Magno y Platón"

    elif ((query.find("como") != -1) or (query.find("manera")!= -1)) and (query.find("murio") != -1) and (query.find("diogenes") != -1):
        Respuesta = "murió de un cólico provocado por la ingestión de un pulpo vivo o murió al caerse de un caballo o haberle mordido un tendón uno de los perros entre los que trataba de repartir un pulpo o murió por su propia voluntad, reteniendo la respiración"

    elif (query.find("cuales") != -1) and (query.find("ultimas palabres")!= -1) and (query.find("diogenes")!= -1) :
        Respuesta = "Cuando me muera, echadme a los perros. Ya estoy acostumbrado"




    if type(Respuesta) is list:
        for i in range(len(Respuesta)-1):
            print(Respuesta[i])

        print("y")
        print(Respuesta[-1])    
    else:
        print(Respuesta)

    print("\n")
    print("Haz tu pregunta. Para acabar escribe SALIR")

    query = input().lower()
    


