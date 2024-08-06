import requests
import time
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from .serializers import *
from .models import *


class LoadCompanyData(APIView):
    def post(self, request):
        serializer = CompanyBinSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        company_bin = serializer.data["company_bin"]
        
        company_url = "https://apiba.prgapp.kz/CompanyFullInfo"
        goz_zakup_url = "https://apiba.prgapp.kz/CompanyGosZakupGraph"
        
        company_params = {
            "id": {company_bin},
            "lang": "ru"
        }
        
        goz_zakup_params = {
            "bin": {company_bin},
            "lang": "ru"
        }
        
        company_response = requests.get(company_url, params=company_params)
        time.sleep(1)
        gos_zakup_response = requests.get(goz_zakup_url, params=goz_zakup_params)
        
        print(company_bin)
        if company_response.status_code == 200 and gos_zakup_response.status_code == 200:
            # {"company_bin": "070240000158"}970340003085
            
            c_data = company_response.json()
            g_data = gos_zakup_response.json()
            name_ru = c_data["basicInfo"]["titleRu"]["value"]
            name_kz = c_data["basicInfo"]["titleKz"]["value"]
            register_date = c_data["basicInfo"]["registrationDate"]["value"]
            ceo = c_data["basicInfo"]["ceo"]["value"]["title"]
            company_bin = c_data["basicInfo"]["bin"]
            pay_nds = c_data["basicInfo"]["isNds"]["value"]
            tax_risk = c_data["basicInfo"]["degreeOfRisk"]["value"]
            address_ru = c_data["basicInfo"]["addressRu"]["value"]
            address_kz = c_data["basicInfo"]["addressKz"]["value"]
            try:
                phone_number = c_data["gosZakupContacts"]["phone"][0]["value"]
            except:
                try:
                    phone_number = c_data["egovContacts"]["phone"][0]["value"]
                except:
                    phone_number = None
            
            try:
                email = c_data["gosZakupContacts"]["email"][0]["value"]
            except:
                email = None
            

            krp_code = c_data["basicInfo"]["krp"]["value"]["value"]
            krp_name = c_data["basicInfo"]["krp"]["value"]["description"]
            kse_code = c_data["basicInfo"]["kse"]["value"]["value"]
            kse_name = c_data["basicInfo"]["kse"]["value"]["description"]
            kfc_code = c_data["basicInfo"]["kfc"]["value"]["value"]
            kfc_name = c_data["basicInfo"]["kfc"]["value"]["description"]
            kato_code = c_data["basicInfo"]["kato"]["value"]["value"]
            kato_name = c_data["basicInfo"]["kato"]["value"]["description"]
            primary_oked = c_data["basicInfo"]["primaryOKED"]["value"]
            secondary_okeds = c_data["basicInfo"]["secondaryOKED"]["value"]
            taxes = c_data["taxes"]["taxGraph"]
            nds_info = c_data["taxes"]["ndsGraph"]
            gos_zakup_as_supplier_info = g_data["asSupplier"]
            gos_zakup_as_customer_info = g_data["asCustomer"]
            
            
            
            register_date = datetime.fromisoformat(register_date).date()
            
            try:
                company = Company.objects.get(company_bin=company_bin)
            except:
                with transaction.atomic():
                    krp, krp_created = Krp.objects.get_or_create(krp_code=krp_code, defaults={'krp_name': krp_name})
                    kse, kse_created = Kse.objects.get_or_create(kse_code=kse_code, defaults={'kse_name': kse_name})
                    kfc, kfc_created = Kfc.objects.get_or_create(kfc_code=kfc_code, defaults={'kfc_name': kfc_name})
                    kato, kato_created = Kato.objects.get_or_create(kato_code=kato_code, defaults={'kato_name': kato_name})
                    oked_code, oked_name = primary_oked.split(" ", 1)
                    oked_obj, oked_created = Oked.objects.get_or_create(oked_code=oked_code, defaults={'oked_name': oked_name})

                    company = Company(name_ru=name_ru,
                                    name_kz=name_kz,
                                    register_date=register_date,
                                    ceo=ceo,
                                    company_bin=company_bin,
                                    pay_nds=pay_nds,
                                    tax_risk=tax_risk,
                                    address_ru=address_ru,
                                    address_kz=address_kz,
                                    phone_number=phone_number,
                                    email=email,
                                    krp=krp,
                                    kse=kse,
                                    kfc=kfc,
                                    kato=kato,
                                    primary_oked=oked_obj)
                    
                    company.save()
                    
                    if not secondary_okeds:
                        for oked_info in secondary_okeds:
                            oked_code, oked_name = oked_info.split(" ", 1)
                            oked_obj, _ = Oked.objects.get_or_create(oked_code=oked_code, defaults={'oked_name': oked_name})
                            company.secondary_okeds.add(oked_obj)
                    
                    
                    for tax in taxes:
                        year = tax["year"]
                        value = tax["value"]
                        Taxes.objects.create(year=year, value=value, company=company)
                    
                    for nds in nds_info:
                        year = nds["year"]
                        value = nds["value"]
                        Nds.objects.create(year=year, value=value, company=company)
                    
                    for gos_zakup_as_supplier in gos_zakup_as_supplier_info:
                        year = gos_zakup_as_supplier["year"]
                        value = gos_zakup_as_supplier["value"]
                        GosZakupSupplier.objects.create(year=year, value=value, company=company)
                    
                    for gos_zakup_as_customer in gos_zakup_as_customer_info:
                        year = gos_zakup_as_customer["year"]
                        value = gos_zakup_as_customer["value"]
                        GosZakupCustomer.objects.create(year=year, value=value, company=company)
                
            # print(taxes)
            # print(nds_info)
            # print(gos_zakup_as_supplier_info)
            # print(gos_zakup_as_customer_info)
            

            
            
            # print(name_ru)
            # print(name_kz)
            # print(register_date)
            # print(ceo)
            # print(company_bin)
            # print(pay_nds)
            # print(tax_risk)
            # print(address_ru)
            # print(address_kz)
            # print(phone_number)
            # print(email)
            # print(krp_code)
            # print(krp_name)
            # print(kse_code)
            # print(kse_name)
            # print(kfc_code)
            # print(kfc_name)
            # print(kato_code)
            # print(kato_name)
            # print(primary_oked)
            # print(secondary_okeds)

            
            
        else:
            return Response("PRGAPP failed")
        
        return Response(c_data)