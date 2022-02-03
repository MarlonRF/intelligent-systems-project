FROM jupyter/scipy-notebook
COPY requirements.txt ./requirements.txt
COPY modelo_classificador_texto_MB.sav ./modelo_classificador_texto_MB.sav
COPY dados_elo7.csv ./dados_elo7.csv
COPY metricas.txt ./metricas.txt
COPY trainer.ipynb ./trainer.ipynb
RUN pip install --upgrade pip

RUN pip install --upgrade -r requirements.txt