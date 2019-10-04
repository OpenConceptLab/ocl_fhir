import OCLAPI
from fhir.resources.valueset import ValueSet
from fhir.resources.valueset import fhirdate
from fhir.resources.valueset import ValueSetCompose
from fhir.resources.valueset import ValueSetComposeInclude
from fhir.resources.valueset import ValueSetComposeIncludeConcept
from fhir.resources.identifier import Identifier

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

    oid_identifier = Identifier()
    oid_identifier.system = "urn:ietf:rfc:3986"
    oid_identifier.value  = "urn:oid:" + ocl_collection['extras']['OID']
    vs.identifier = []
    vs.identifier.append(oid_identifier)

    compose = ValueSetCompose()
    compose.include = []

    url_concepts = ocl_collection['concepts_url']
    concepts = OCLAPI.get(url_concepts)

    source_map = {}
    for concept in concepts:
        source_url = concept['owner_url'] + 'sources/' + concept['source']
        if source_url not in source_map.keys():
            source_map[source_url] = []

        include_concept = ValueSetComposeIncludeConcept()
        include_concept.code     = concept['id']
        include_concept.display  = concept['display_name']
        source_map[source_url].append(include_concept)

    for source_url in source_map.keys():
        source = OCLAPI.get(source_url)
        compose_include = ValueSetComposeInclude()
        compose_include.system = source['extras']['uri']
        compose_include.concept = source_map[source_url]
        compose.include.append(compose_include)

    vs.compose = compose

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
