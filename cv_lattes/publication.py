class Publication:
	
	#???? Perguntar utilidade para Jean	
	# type_list = ["TCC", "IC"]
	# status_list = ["In Progress", "Concluded"]

	def __init__(self):
		self.id = None #???? como definir o id para dar match com orintador orientado e participante de banca
		self.title = None
		self.author_name_list = None
		self.advisor_name = None ###
		self.year = None
		self.country = None
		self.status = None #Concluida ou em andamento
		self.type = None #TCC ou IC
		self.lang = None
		self.name_institution = None
		self.name_course = None
		self.name_cod = None
	
	#Pegando dados das orientações concluidas
	def get_data(self, root):
		#Navegando por outras produções
		for other_prod in root.findall('.//OUTRA-PRODUCAO'): 
			#Criando lista de orientações concluídas
			other_prod_list = other_prod.findall('.//ORIENTACOES-CONCLUIDAS')
			
			#Navegando na lista de orientações concluídas
			for completed_prod in other_prod_list:
				completed_prod_list = completed_prod.findall('.//OUTRAS-ORIENTACOES-CONCLUIDAS')
				
				#Navegando pelos dados básicos de orientações concluidas
				for completed_prod_item in completed_prod_list:
					data_completed_prod = completed_prod_item.find('.//DADOS-BASICOS-DE-OUTRAS-ORIENTACOES-CONCLUIDAS')
					if data_completed_prod is not None:
						#Tornando o status da classe em concluido
						self.status = 'Concluded'
						#Adicionando atributos na classe
						self.title = data_completed_prod.attrib.get('TITULO')
						self.year = data_completed_prod.attrib.get('ANO')
						self.country = data_completed_prod.attrib.get('PAIS')
						self.lang = data_completed_prod.attrib.get('IDIOMA')
						self.type = data_completed_prod.attrib.get('NATUREZA')
						
				#Navegando pelos dados detalhados de orientações concluidas
				for completed_prod_item in completed_prod_list:
					details_completed_prod = completed_prod_item.find('.//DETALHAMENTO-DE-OUTRAS-ORIENTACOES-CONCLUIDAS')
					if details_completed_prod is not None:		
						
						#Adicionando atributos na classe
						self.name_institution = details_completed_prod.attrib.get('NOME-DA-INSTITUICAO')
						self.name_course = details_completed_prod.attrib.get('NOME-DO-CURSO')
						self.cod_course = details_completed_prod.attrib.get('CODIGO-CURSO')
						
						#Extraindo lista de autores do xml
						self.authors_xml = details_completed_prod.attrib.get('NOME-DO-ORIENTADO')
						
		# return authors_xml						


	#Ainda não funciona	
	def format_authors(self):
		formatted_authors = []
		
		for author in self.authors_xml:
			parts = author.split(' e')
			if len(parts) > 1:
				formatted_authors.append(parts)
			else:
				print("errou")
			
		return formatted_authors

