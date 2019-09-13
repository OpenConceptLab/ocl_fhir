import OCLAPI
from fhir.resources.valueset import ValueSet
from fhir.resources.valueset import fhirdate
from fhir.resources.valueset import ValueSetCompose
from fhir.resources.valueset import ValueSetComposeInclude
from fhir.resources.valueset import ValueSetComposeIncludeConcept

def build_from_dictionary(ocl_collection):

    vs = ValueSet()

    date = fhirdate.FHIRDate(ocl_collection['updated_on'])
    vs.date             = date
    vs.description      = ocl_collection['description']
    vs.experimental     = False
    vs.id               = ocl_collection['id']
    vs.name             = ocl_collection['name']
    vs.publisher        = ocl_collection['owner']
    vs.status           = 'active'
    vs.title            = ocl_collection['extras']['Title']
    vs.url              = ocl_collection['extras']['uri']

    compose = ValueSetCompose()
    compose_include = ValueSetComposeInclude()
    compose_include.concept = []

    url_concepts = ocl_collection['concepts_url']
    concepts = OCLAPI.get(url_concepts)

    for concept in concepts:
        include_concept = ValueSetComposeIncludeConcept()
        include_concept.code     = concept['id']
        include_concept.display  = concept['display_name']
        compose_include.concept.append(include_concept)

    compose.include = [compose_include]
    vs.compose = compose

    # vs.compose
    # vs.contact
    # vs.contained
    # vs.copyright
    # vs.expansion
    # vs.extension
    # vs.identifier
    # vs.immutable
    # vs.implicitRules
    # vs.jurisdiction
    # vs.language
    # vs.meta
    # vs.modifierExtension
    # vs.purpose
    # vs.server
    # vs.text
    # vs.useContext
    # vs.version

    return vs
