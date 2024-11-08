import pandas as pd 
import numpy as np

try:
  print('\nCalculando ocorrencias de estelionato')
  ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
  df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
  df_estelionato = df_ocorrencias[['mes', 'estelionato']]
  df_estelionato = df_estelionato.groupby(['mes']).sum(['estelionato']).reset_index()
  
  print(df_estelionato.head())
  
  print('\nDados obtidos com sucesso!')

except Exception as e: 
  print(f'Erro ao obter dados {e}')
  exit()


try:
  print('\nCalculando padrão ')
  array_estelionato = np.array(df_estelionato['estelionato'])

# media de roubo_veiculo:
  media_estelionato = np.mean(array_estelionato)
# mediana de roubo_veiculo - divide 
  mediana_estelionato = np.median(array_estelionato)


except Exception as e: 
    print('Erro ao obter informações sobre padrão de estelionato: {e}')
    exit()

disancia_media_mediana = abs((media_estelionato - mediana_estelionato) / mediana_estelionato)

print('\nMedidas de tendência central: ')
print(30*'=')
print(f'Média estelionato: {media_estelionato}')
print(f'Mediana de estelionato: {mediana_estelionato}')
print(f'Total {disancia_media_mediana}')




