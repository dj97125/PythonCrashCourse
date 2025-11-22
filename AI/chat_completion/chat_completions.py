import openai
import AI.chat_completion.config as config
from openai import OpenAI
import typer
from rich import print
from rich.table import Table

# https://typer.tiangolo.com/
# https://platform.openai.com/docs/api-reference/chat/create Chat completions

def main():
  
  # python3 -m pip install pymongo
  client = OpenAI(api_key= config.api_key)
  print("[bold green]ChatGPT API en python[/bold green]")

  table = Table("Comando","Descripcion")
  table.add_row("exit", "Salir de la app")
  table.add_row("new", "Crear una nueva conversarcion")

  print(table)

  # Contexto del asistente
  context = {"role":"system",
              "content":"Eres un asistente muy util."
              }
  messages = [context]


  while True:


    content = _prompt()
   
    if content == "new":
      print("Nueva conversacion creada")
      messages = [context]
      content = _prompt()

    
  
    messages.append({"role":"user", "content": content})

    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        messages
      ]
    )

    response_content = response.choices[0].message.content

    messages.append({"role":"assistant", "content": response_content})

    print(f"[bold green] --> [/bold green][green]{response_content}[/green]")

def _prompt() -> str:

  prompt = typer.prompt("\nSobre que quieres hablar?")

  if prompt == "exit":
    exit = typer.confirm("Estas seguro?")

    if exit:
      print("Hasta luego")
      raise typer.Abort()
    return _prompt()
  
  return prompt



if __name__ == "__main__": typer.run(main)