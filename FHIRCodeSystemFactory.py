import OCLAPI
from fhir.resources.codesystem import CodeSystem
from fhir.resources.codesystem import CodeSystemConcept
from fhir.resources.codesystem import fhirdate
from fhir.resources.identifier import Identifier

def build_from_dictionary(ocl_source):
    cs = CodeSystem()

    date = fhirdate.FHIRDate(ocl_source['updated_on'])
    cs.date = date
    cs.description = ocl_source['description']
    cs.experimental = False
    cs.id = ocl_source['id']
    cs.name = ocl_source['name']
    cs.publisher = ocl_source['owner']
    cs.status = 'active'
    cs.title = ocl_source['extras']['Title']
    cs.url = ocl_source['extras']['uri']

    oid_identifier = Identifier()
    oid_identifier.system = "urn:ietf:rfc:3986"
    oid_identifier.value  = "urn:oid:" + ocl_source['extras']['OID']
    cs.identifier = []
    cs.identifier.append(oid_identifier)

    # content is required, but there is no value in OCL to use
    # valid values are not-present | example | fragment | complete | supplement
    cs.content = 'complete'

    url_concepts = ocl_source['concepts_url']
    concepts = OCLAPI.get(url_concepts)

    cs.concept = []
    for concept in concepts:
        cs_concept = CodeSystemConcept()
        cs_concept.code     = concept['id']
        cs_concept.display  = concept['display_name']
        cs.concept.append(cs_concept)


    return cs