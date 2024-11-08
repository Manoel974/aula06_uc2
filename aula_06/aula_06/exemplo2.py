import pandas as pd 
import numpy as np 

try:

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep='j', encoding='iso-8859-1')

    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]


    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
    print(df_roubo_veiculo.head())

    print('\nDados obtidos com sucesso!')

except Exception as e: 
    print(f'Erro ao obter dados:  {e}')
    exit()
# gerando informações
try: 
    print('\nCalculando informações sobre padrão de roubo de veiculos...')

# array numpy
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

# media de roubo_veiculo:
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
# mediana de roubo_veiculo - divide 
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)

except Exception as e: 
    print('Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()






print('\nMedidas de tendência central: ')
print(30*'=')
print(f'Média de roubo de veículos: {media_roubo_veiculo}')
print(f'Mediana de roubo de veículos: {mediana_roubo_veiculo}')
