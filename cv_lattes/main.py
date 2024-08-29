import publication
import curriculo
import xml.etree.ElementTree as ET


if __name__ == '__main__':
	
	#Transformando o xml em arvore 
	tree = ET.parse('cv/jean.xml')
	root = tree.getroot()
	
	
	#criando um curriculo
	cv1 = curriculo.Curriculo()
	cv1.get_data(root)
	cv1.last_att
	
	#criando uma publicação
	pb = publication.Publication()
	pb.get_data(root)
	print(pb.authors_xml)
	
	
	# autores = pb.format_authors()
	# print(autores)
	
	
	
	# print(cv1.name, cv1.last_att, cv1.nacionality)
	# print(pb)

