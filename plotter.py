## Depêndencias de Plotagem
import matplotlib.pyplot as plotlib
import numpy

## Depêndencias de Configuração
import json
import os


def config(path: str):
    configuracao = []
    for file in os.listdir(path):
        conf_file = open(f"{path}/{file}").read()
        json_config = json.loads(conf_file)
        configuracao.append(json_config)
        
    print(configuracao)
    return configuracao

def plot_all(arquivos_configuracao: list[dict[str]], outdir: str):
    for grafico in arquivos_configuracao:
        print(grafico)
        figura, ax = plotlib.subplots()
        ax.plot([1,2], [3,4])

        ax.set_title(grafico["titulo"])
        plotlib.savefig(f"{outdir}/{grafico['nome_arquivo']}.{grafico['formato']}")
        plotlib.show()

arquivos = config("./conf")

plot_all(arquivos, "outputs/")

