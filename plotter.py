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

        for i, legendas in zip(grafico["pontos"], grafico["legendas"]): 
            x = []
            y = []
            for j in i:
                v1, v2 = eval(j)
                x.append(v1)
                y.append(v2)
            print(legendas)
            print(x)
            print(y)
            print("--")
            ax.plot(x,y, label=legendas)  
 
        
        if grafico["grid"] != None:
            ax.grid(color=grafico["grid"]["cor"], linestyle = grafico["grid"]["estilo"], linewidth = grafico["grid"]["tamanho"])

        ax.set_title(grafico["titulo"])
        ax.set_xlabel(grafico["xlabel"])
        ax.set_ylabel(grafico["ylabel"])
        ax.legend()
        plotlib.savefig(f"{outdir}/{grafico['nome_arquivo']}.{grafico['formato']}")
        
        plotlib.show()

arquivos = config("./conf")

plot_all(arquivos, "outputs/")

