#Class Exportar
class Export():
    
  #Método Exportar
  def Rename(self, df):
    self.nome = str(input('Nome para o arquivo: '))
    df.to_csv(f'out/{self.nome}.csv', encoding='utf-8', index=False)
    print('Salvo com sucesso!')
    indf = self.nome
    return indf
