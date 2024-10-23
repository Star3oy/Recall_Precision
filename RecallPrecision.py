quasi_list = []

print("Ingrese los DOI de los trabajos obtenidos con el quasi-gold (escriba 'fin' para terminar):")
while True:
    doi = input().strip()
    if doi.lower() == 'fin':
        break
    quasi_list.append(doi.lower()) 

doi_list = []
print("Ingrese los DOI de los trabajos obtenidos con la cadena de búsqueda (escriba 'fin' para terminar):")
while True:
    doi = input().strip()  
    if doi.lower() == 'fin':
        break
    doi_list.append(doi.lower())

doi_found = []
for doi in quasi_list:
    if doi in doi_list:
        doi_found.append(doi)

total_doi_founded = len(doi_found);
total_doi_quasigold = len(quasi_list);
total_doi_chain = len(doi_list)

recall = total_doi_founded / total_doi_quasigold;
precision = total_doi_founded / total_doi_chain;

print("-----------------------Resultados-----------------------")
print("El número de coincidencias es: ", total_doi_founded);
print("Las coincidencias son: ", doi_found)
print("\n");
print("RECALL: ", recall);
print("PRECISION: ", precision);



