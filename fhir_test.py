import json
import OCLAPI
import FHIRValueSetFactory
import FHIRCodeSystemFactory
import FHIRConceptMapFactory

url_concepts                = '/orgs/PEPFAR/sources/PLM/concepts/?verbose=true&limit=0'
url_concepts_with_mappings  = '/orgs/PEPFAR/sources/PLM/concepts/?verbose=true&limit=0&includeMappings=true&includeInverseMappings=true'
url_mappings                = '/orgs/PEPFAR/sources/PLM/mappings/?verbose=true&limit=0'
url_plm                     = '/orgs/PEPFAR/sources/PLM/?verbose=true&limit=0'
url_admingender_vs          = '/orgs/HL7/collections/HL7-AdministrativeGender/'
url_admingender_cs          = '/orgs/HL7/sources/HL7-AdministrativeGender/'
url_concept_map             = '/orgs/OCL-Test/sources/FhirConceptMap/'

results = OCLAPI.get(url_admingender_vs)
valueset = FHIRValueSetFactory.build_from_dictionary(results)
print json.dumps(valueset.as_json())

results = OCLAPI.get(url_admingender_cs)
codesystem = FHIRCodeSystemFactory.build_from_dictionary(results)
print json.dumps(codesystem.as_json())

results = OCLAPI.get(url_concept_map)
concept_map = FHIRConceptMapFactory.build_from_dictionary(results)
print json.dumps(concept_map.as_json())

#print eval(json.dumps(concept_map.as_json()))
