import flet as ft
import random

#Se crea la funcion para comprobar la respuesta del usuario
def verificar_adivinansa(e,page):
    adivinanza_usuario=int(entrada_numero.value)
    
    #Se Hacen las condiciones para ganar 
    if adivinanza_usuario==numero_secreto:
        dialog=ft.AlertDialog(
            title=ft.Text("Ganaste Adivinaste el numero"),
            content=ft.Image(src="descarga (1).jpg",width=150,height=150),
            actions=[
                    ft.TextButton(text="Cerrar",on_click=lambda e:cerrar(e))
                ],
            )
        texto_resultado.value="Felicidades Adivinaste el numero secreto"
        boton_adivinar.disabled=True
        
        page.add(ft.Audio(src="Victoria.mp3",autoplay=True))


    elif adivinanza_usuario<numero_secreto:
        dialog=ft.AlertDialog(
            title=ft.Text("Fallaste"),
            content=ft.Image(src="descarga.jpg",width=150,height=150),
            actions=[
                    ft.TextButton(text="Cerrar",on_click=lambda e:cerrar(e))
                ],
            )
        texto_resultado.value="Fallaste  el numero secreto es mayor"
        page.add(ft.Audio(src="Boing.mp3",autoplay=True))

                 
    else:
        dialog=ft.AlertDialog(
            title=ft.Text("Fallaste"),
            content=ft.Image(src="descarga.jpg",width=150,height=150),
            actions=[
                    ft.TextButton(text="Cerrar",on_click=lambda e:cerrar(e))
                ],
            )
        texto_resultado.value="Fallaste  el numero secreto es menor"
        page.add(ft.Audio(src="Boing.mp3",autoplay=True))

        
    page.dialog=dialog
    page.dialog.open=True
    page.update()
    
    #Se crea la funcion para cerrar el cuadro de dialogo
    def cerrar(e):
        page.dialog.open=False
        page.update()    
        
    
#funcion principal 
def main(page: ft.Page):
    #variables globales
    global numero_secreto,entrada_numero,texto_resultado,boton_adivinar,img

    page.title="Adivina el numero"
    
    #generar numero aleatoreo
    numero_secreto= random.randint(1,100)
    
    #crear los elementos de la interfaz
    titulo=ft.Text("Adivina el numero secreto entre 1 y 100",size=20,color="white")
    entrada_numero=ft.TextField(label="tu Adivinansa",width=150)
    boton_adivinar=ft.ElevatedButton("Adivinar", on_click=lambda e:verificar_adivinansa(e,page))
    texto_resultado=ft.Text("",color="white")
    img=ft.Image(src="https://i.ibb.co/Gxgryg9/laser.gif",fit=ft.ImageFit.COVER,width=150,height=200)
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                texto_resultado,
                img
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="black",
        width=page.window.width,
        height=page.window.height,
        padding=20
    )
    page.add(contenedor_principal)
ft.app(main)
