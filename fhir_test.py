import OCLAPI
import FHIRValueSetFactory

url_concepts                = '/orgs/PEPFAR/sources/PLM/concepts/?verbose=true&limit=0'
url_concepts_with_mappings  = '/orgs/PEPFAR/sources/PLM/concepts/?verbose=true&limit=0&includeMappings=true&includeInverseMappings=true'
url_mappings                = '/orgs/PEPFAR/sources/PLM/mappings/?verbose=true&limit=0'
url_plm                     = '/orgs/PEPFAR/sources/PLM/?verbose=true&limit=0'
url_admingender_vs          = "/orgs/HL7/collections/HL7-AdministrativeGender/"

results = OCLAPI.get(url_admingender_vs)

valueset = FHIRValueSetFactory.build_from_dictionary(results)

print valueset.as_json()




