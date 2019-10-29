import OCLAPI
from fhir.resources.conceptmap import ConceptMap
from fhir.resources.conceptmap import ConceptMapGroup
from fhir.resources.conceptmap import ConceptMapGroupElement
from fhir.resources.conceptmap import ConceptMapGroupElementTarget
from fhir.resources.conceptmap import fhirdate


def build_from_dictionary(ocl_conceptmap):
    source_system_url = ocl_conceptmap['extras']['source_code_system']
    target_system_url = ocl_conceptmap['extras']['target_code_system']
    mappings_url = ocl_conceptmap['mappings_url']

    cm = ConceptMap()

    date = fhirdate.FHIRDate(ocl_conceptmap['updated_on'])
    cm.date = date
    cm.description = ocl_conceptmap['description']
    cm.experimental = False
    cm.id = ocl_conceptmap['id']
    cm.name = ocl_conceptmap['name']
    cm.publisher = ocl_conceptmap['owner']
    cm.status = 'active'
    cm.title = ocl_conceptmap['full_name']

    cm.sourceUri = source_system_url
    cm.targetUri = target_system_url

    mappings = OCLAPI.get(mappings_url)

    group = ConceptMapGroup()
    group.source = source_system_url
    group.target = target_system_url
    group_elements = []

    for mapping in mappings:
        e = ConceptMapGroupElement()
        e.id = mapping['id']

        e.code      = mapping['from_concept_code']
        e.display   = mapping['from_concept_name']

        t = ConceptMapGroupElementTarget()
        t.code      = mapping['to_concept_code']
        t.display   = mapping['to_concept_name']
        t.equivalence = get_equivalence(mapping['map_type'])

        e.target = [t]

        group_elements.append(e)

    group.element = group_elements
    cm.group = [group]

    return cm


def get_equivalence(map_type):

    if (map_type == 'Same As'):
        return 'equivalent'
    #
    # Put other value translations here
    #
    # default to 'relatedto'? Guess on my part - DT
    else:
        return 'relatedto'

