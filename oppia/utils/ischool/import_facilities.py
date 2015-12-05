import argparse
import csv

# rows: "ProvinceName","DistrictName","FacilityTypeName","FacilityName","FacilityCode"

def run(import_file):
    
    from oppia.profile.models import Province, District, Facility
    
    csv_file = csv.DictReader(open(import_file))
    
    for row in csv_file:
        print row["ProvinceName"]
        province, prov_created = Province.objects.get_or_create(name=row["ProvinceName"])
        district, dist_created = District.objects.get_or_create(name=row["DistrictName"], province=province)
        facility, fac_created = Facility.objects.get_or_create(name=row["FacilityName"], district=district)
        facility.code = row["FacilityCode"]
        facility.type = row["FacilityTypeName"]
        facility.active = True
        facility.save()
    
if __name__ == "__main__":
    import django
    django.setup()
    parser = argparse.ArgumentParser()
    parser.add_argument("import_file", help="Specify full path to the import file")
    args = parser.parse_args()
    run(args.import_file) 
    
    
