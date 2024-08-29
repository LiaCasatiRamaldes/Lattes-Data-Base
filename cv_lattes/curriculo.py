class Curriculo:	

	def __init__(self):
		self.name = None
		self.last_att = None
		self.sex = None
		self.lattes_id = None
		self.nacionality = None
		
		self.publications = [] #Lista de publicações
		self.adivisor_publications = [] #Lista de publicações como orientador

	#função para pegar dados da classe curriculo
	def get_data(self, root):
		for cv_data in root.iter('CURRICULO-VITAE'):
			self.last_att = cv_data.get('DATA-ATUALIZACAO')
			self.lattes_id = cv_data.get('NUMERO-IDENTIFICADOR')		
			
		for general_data in root.iter('DADOS-GERAIS'):
			self.name = general_data.get('NOME-COMPLETO')
			self.nacionality = general_data.get('PAIS-DE-NACIONALIDADE')
	
	