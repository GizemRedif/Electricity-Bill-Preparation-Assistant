INDUSTRY_SINGLE = 3.053828
INDUSTRY_DAY = 3.091833
INDUSTRY_PEAK = 4.909037
INDUSTRY_NIGHT = 1.625171
INDUSTRY_DISTRIBUTION = 0.647998
INDUSTRY_ECT_RATE = 0.01
INDUSTRY_VAT_RATE = 0.2

PPS_LOW_TARIFF = 1.912220
PPS_HIGH_TARIFF = 2.828414

PPS_DAY = 2.858616
PPS_PEAK = 4.588843
PPS_NIGHT = 1.481941
PPS_DISTRIBUTION = 0.878175
PPS_ECT_RATE = 0.05
PPS_VAT_RATE = 0.2

PPS_DAILY_AVERAGE_UPPER_LIMIT = 30

RESIDENTAL_LOW_TARIFF = 0.482187
RESIDENTAL_HIGH_TARIFF = 1.132271

RESIDENTAL_DAYTIME_FEE = 1.157700
RESIDENTAL_PEAK_FEE = 2.083645
RESIDENTAL_NIGHT_FEE = 0.417225
RESIDENTAL_DISTRIBUTION = 0.858883
RESIDENTAL_ECT_RATE = 0.05
R_VAT_RATE = 0.1

RESIDENTAL_DAILY_AVERAGE_UPPER_LIMIT = 8

RESIDENTAL_FAMILY_M_V_SINGLE = 0.061590
RESIDENTAL_FAMILY_M_V_DISTRIBUTION = 0.582521
RESIDENTAL_FAMILY_M_V_ECT_RATE = 0.05
RESIDENTAL_FAMILY_M_V_VAT_RATE = 0.1

AGRICULTURAL_ACTIVITIES_SINGLE = 1.653096
AGRICULTURAL_ACTIVITIES_DAY = 1.704822
AGRICULTURAL_ACTIVITIES_PEAK = 2.800325
AGRICULTURAL_ACTIVITIES_NIGHT = 0.771882
AGRICULTURAL_ACTIVITIES_DISTRIBUTION = 0.721579
AGRICULTURAL_ACTIVITIES_ECT_RATE = 0.05
AGRICULTURAL_ACTIVITIES_VAT_RATE = 0.1

LIGHTING_SINGLE = 2.595835
LIGHTING_DISTRIBUTION = 0.841099
LIGHTING_ECT_RATE = 0.05
LIGHTING_VAT_RATE = 0.2

# control input functions

def control_zero_or_bigger_zero (value):
    while value <0 :
        value = int(input("Enter value 0 or greater than 0\n"))
    return value

def control_bigger_zero (value):
    while value <= 0 :
        value = int(input("enter value greater than 0\n"))
    return value
    
def control_current_value (current_value,previous_value):
    while current_value < previous_value :
        current_value = int(input("Enter value equal or greater than previous\n"))
    return current_value 

def control_str (string,list):
    while string not in list :
        string = input("enter one of the desired characters\n")
    return string


# statistics calculation functions

def calculate_percentage(numerator,denominator):
    if denominator == 0 :
        percentage = 0
    else:
        percentage = numerator/denominator*100
    
    return percentage

def calculate_average_function(numerator,denominator):
    if denominator == 0:
        average = 0
    else:
        average = numerator/denominator
    return average

def calculate_daily_average_consumption(total_usage,total_days_between_previous_and_current):
    if total_days_between_previous_and_current == 0:
        daily_average_consumption_amount = 0
    else:
        daily_average_consumption_amount = total_usage/total_days_between_previous_and_current
    return daily_average_consumption_amount


# fee calculation functions

def calculate_fixed_pricing_usage_fee(total_usage,single_time_fee):
    usage_fee = total_usage*single_time_fee
    return usage_fee

def calculate_two_stage_pricing_usage_fee(total_usage,daily_average_upper_limit,low_tariff,high_tariff):
    if total_usage>daily_average_upper_limit:
        usage_fee = (daily_average_upper_limit*low_tariff)+((total_usage-daily_average_upper_limit)*high_tariff)
    else:
        usage_fee = total_usage*low_tariff
    return usage_fee

def calculate_multi_time_pricing_usage_fee(total_daytime_usage,total_peak_usage,total_night_usage,daytime_fee,peak_fee,night_fee):
    usage_fee = (total_daytime_usage*daytime_fee)+(total_peak_usage*peak_fee)+(total_night_usage*night_fee)
    return usage_fee


def calculate_taxes_and_invoice_amount(usage_fee,ect_rate,distribution_fee,vat_rate):
    ect_fee = usage_fee*ect_rate
    vat_fee = (usage_fee*(ect_rate+1)+distribution_fee)*vat_rate
    invoice_amount = (usage_fee*(ect_rate+1)+distribution_fee)*(vat_rate+1)
    return ect_fee,vat_fee,invoice_amount

def calculate_invoice_amount(usage_fee,ect_rate,distribution_fee,vat_rate):
    invoice_amount = (usage_fee*(ect_rate+1)+distribution_fee)*(vat_rate+1)
    return invoice_amount


preferred_multi_time_tariff_counter = 0
multi_time_tariff_loss_counter = 0

total_invoice_amount = 0
total_revenue_amount_municipality = 0
total_revenue_amount_state = 0

industry_counter = 0
industry_total_electricity_usage = 0
industry_over_than_10000kwh_or_100000TL_counter = 0

pps_single_time_tariff_counter = 0
pps_multi_time_tariff_counter = 0
total_pps_consumer =pps_single_time_tariff_counter + pps_multi_time_tariff_counter
pps_single_time_tariff_total_electricity_usage = 0
pps_multi_time_tariff_total_electricity_usage = 0
pps_total_electricity_usage = pps_single_time_tariff_total_electricity_usage + pps_multi_time_tariff_total_electricity_usage
single_time_pps_days_between_previous_and_current_counter = 0
multi_time_pps_days_between_previous_and_current_counter = 0

residental_counter = 0
residental_total_electricity_usage = 0
residental_higher_daily_average_consumption_consumer_no = 0
residental_higher_daily_average_consumption_used_electricity = 0
residental_higher_daily_average_consumption_days_between_previous_and_current = 1
residental_higher_daily_average_consumption = residental_higher_daily_average_consumption_used_electricity/residental_higher_daily_average_consumption_days_between_previous_and_current
residental_higher_daily_average_consumption_invoice_amount = 0

agricultural_activites_counter = 0
agricultural_activities_total_electricity_usage = 0

lightning_counter = 0
lightning_total_electricity_usage = 0

not_residental_higher_consumption_consumer_no = 0
not_residental_higher_consumption_consumer_type = ""
not_residental_higher_consumption_used_electricity = 0
not_residental_higher_consumption_days_between_previous_and_current = 1
not_residental_higher_daily_average_consumption = not_residental_higher_consumption_used_electricity/not_residental_higher_consumption_days_between_previous_and_current
not_residental_higher_consumption_invoice_amount = 0

total_consumer = industry_counter + total_pps_consumer + residental_counter + agricultural_activites_counter + lightning_counter 
total_consumption_amount = industry_total_electricity_usage + pps_total_electricity_usage + residental_total_electricity_usage + agricultural_activities_total_electricity_usage + lightning_total_electricity_usage



consumer_no = int(input("Enter consumer's number\n"))
consumer_no = control_zero_or_bigger_zero(consumer_no)
while consumer_no > 0:
    is_single_price = False  # To distinguish consumer types tariffed at a single price(residental(family of matrys or veteran) and lightning consumers)

    consumer_type_code = input("Enter consumer's type code\nIndustry('i'/'I')\nPublic and Private Services Sector and Other('p','P')\nResidential('r','R')\nAgricultural Activities('a','A')\nLightning('l','L')\n")
    consumer_type_codes_list=["I","i","P","p","R","r","A","a","L","l"]
    consumer_type_code = control_str(consumer_type_code,consumer_type_codes_list)
    match consumer_type_code :      # to print consumer type
        case "i" | "I":
            consumer_type = "Industrial"
        case "p" | "P":
            consumer_type = "Public and Private Services Sector and Other"
        case "r" | "R":
            consumer_type = "Residental"
        case "a" | "A":
            consumer_type = "Agricultural Activities"
        case "l" | "L":
            consumer_type = "Lighting"

    if consumer_type_code in ["r","R"]:
        family_of_matyrs_or_veteran = input("Is the consumer family of matrys or veteran?('y','Y'/'n','N')\n")
        yes_no_string_list = ["y","Y","n","N"]
        family_of_matyrs_or_veteran = control_str(family_of_matyrs_or_veteran,yes_no_string_list)
        if family_of_matyrs_or_veteran in ["y","Y"]:
            is_single_price = True 
        
    elif consumer_type_code in ["l","L"]:
        is_single_price = True 

    if not(is_single_price):    
        preferred_tariff = input("Enter consumer's preferred tariff\nsingle time('s'/'S')\nmultti time('m'/'M')\n")
        preferred_tarrif_codes_list = ["s","S","m","M"]
        preferred_tariff = control_str(preferred_tariff,preferred_tarrif_codes_list)

    previous_daytime_usage = float(input("Enter previous daytime period meeter value(kWh)\n"))
    previous_daytime_usage = control_zero_or_bigger_zero(previous_daytime_usage)
    current_daytime_usage = float(input("Enter current daytime period meeter value(kWh)\n"))
    current_daytime_usage = control_current_value (current_daytime_usage,previous_daytime_usage)
    previous_peak_usage = float(input("Enter previous peak period meeter value(kWh)\n"))
    previous_peak_usage = control_zero_or_bigger_zero(previous_peak_usage)
    current_peak_usage = float(input("Enter current peak period meeter value(kWh)\n"))
    current_peak_usage = control_current_value (current_peak_usage,previous_peak_usage)
    previous_night_usage = float(input("Enter previous night period meeter value(kWh)\n"))
    previous_night_usage = control_zero_or_bigger_zero(previous_night_usage)
    current_night_usage = float(input("Enter current night period meeter value(kWh)\n"))
    current_night_usage = control_current_value (current_night_usage,previous_night_usage)
    days_between_previous_and_current = int(input("Enter the number of days between previous and current meeter reading dates\n"))
    days_between_previous_and_current = control_bigger_zero (days_between_previous_and_current)
    current_year_total_consumption_electricity = float(input("Enter total amount of electricity consumption in the current year until this period(kWh)\n"))
    current_year_total_consumption_electricity = control_zero_or_bigger_zero(current_year_total_consumption_electricity)
    total_daytime_usage = current_daytime_usage - previous_daytime_usage
    total_peak_usage = current_peak_usage - previous_peak_usage
    total_night_usage = current_night_usage - previous_night_usage
    total_usage = total_daytime_usage + total_peak_usage + total_night_usage

    final_current_year_total_consumption_electricity = current_year_total_consumption_electricity + total_usage

    if is_single_price:     # to bill lightning or residental(family of matrys or veteran) consumers
        match consumer_type_code:
            case "r" | "R":
                usage_fee = calculate_fixed_pricing_usage_fee(total_usage,RESIDENTAL_FAMILY_M_V_SINGLE)
                ect_fee,vat_fee,invoice_amount= calculate_taxes_and_invoice_amount(usage_fee,RESIDENTAL_FAMILY_M_V_ECT_RATE,RESIDENTAL_FAMILY_M_V_DISTRIBUTION,RESIDENTAL_FAMILY_M_V_VAT_RATE)

                residental_counter += 1
                residental_total_electricity_usage += total_usage

            case "l" | "L":
                usage_fee = calculate_fixed_pricing_usage_fee(total_usage,LIGHTING_SINGLE)
                ect_fee,vat_fee,invoice_amount= calculate_taxes_and_invoice_amount(usage_fee,LIGHTING_ECT_RATE,LIGHTING_DISTRIBUTION,LIGHTING_VAT_RATE)

                lightning_counter += 1
                lightning_total_electricity_usage += total_usage

    else:
        if preferred_tariff in ["s","S"]:   # to bill single time tariff
            match consumer_type_code:
                case "i" | "I":
                    usage_fee = calculate_fixed_pricing_usage_fee(total_usage,INDUSTRY_SINGLE)
                    ect_fee,vat_fee,invoice_amount= calculate_taxes_and_invoice_amount(usage_fee,INDUSTRY_ECT_RATE,INDUSTRY_DISTRIBUTION,INDUSTRY_VAT_RATE)
                    
                    multi_time_usage_fee = calculate_multi_time_pricing_usage_fee(total_daytime_usage,total_peak_usage,total_night_usage,INDUSTRY_DAY,INDUSTRY_PEAK,INDUSTRY_NIGHT)
                    multi_time_total_fee = calculate_invoice_amount(multi_time_usage_fee,INDUSTRY_ECT_RATE,INDUSTRY_DISTRIBUTION,INDUSTRY_VAT_RATE)
                    
                    industry_counter += 1
                    industry_total_electricity_usage += total_usage

                    if invoice_amount > 100000 or total_usage > 10000:
                        industry_over_than_10000kwh_or_100000TL_counter += 1
                            
                case "p" | "P":
                    usage_fee = calculate_two_stage_pricing_usage_fee(total_usage,PPS_DAILY_AVERAGE_UPPER_LIMIT,PPS_LOW_TARIFF,PPS_HIGH_TARIFF)  
                    ect_fee,vat_fee,invoice_amount= calculate_taxes_and_invoice_amount(usage_fee,PPS_ECT_RATE,PPS_DISTRIBUTION,PPS_VAT_RATE)
                    
                    multi_time_usage_fee = calculate_multi_time_pricing_usage_fee(total_daytime_usage,total_peak_usage,total_night_usage,PPS_DAY,PPS_PEAK,PPS_NIGHT)
                    multi_time_total_fee = calculate_invoice_amount(multi_time_usage_fee,INDUSTRY_ECT_RATE,INDUSTRY_DISTRIBUTION,INDUSTRY_VAT_RATE)

                    pps_single_time_tariff_counter += 1
                    pps_single_time_tariff_total_electricity_usage +=total_usage
                    single_time_pps_days_between_previous_and_current_counter += days_between_previous_and_current

                case "r" | "R":
                    usage_fee = calculate_two_stage_pricing_usage_fee(total_usage,RESIDENTAL_DAILY_AVERAGE_UPPER_LIMIT,RESIDENTAL_LOW_TARIFF,RESIDENTAL_HIGH_TARIFF)
                    ect_fee,vat_fee,invoice_amount= calculate_taxes_and_invoice_amount(usage_fee,RESIDENTAL_ECT_RATE,RESIDENTAL_DISTRIBUTION,R_VAT_RATE)
                    
                    multi_time_usage_fee = calculate_multi_time_pricing_usage_fee(total_daytime_usage,total_peak_usage,total_night_usage,RESIDENTAL_DAYTIME_FEE,RESIDENTAL_PEAK_FEE,RESIDENTAL_NIGHT_FEE)
                    multi_time_total_fee = calculate_invoice_amount(multi_time_usage_fee,INDUSTRY_ECT_RATE,INDUSTRY_DISTRIBUTION,INDUSTRY_VAT_RATE)

                    residental_counter += 1
                    residental_total_electricity_usage += total_usage
                        
                case "a" | "A":
                    usage_fee = calculate_fixed_pricing_usage_fee(total_usage,AGRICULTURAL_ACTIVITIES_SINGLE)
                    ect_fee,vat_fee,invoice_amount= calculate_taxes_and_invoice_amount(usage_fee,AGRICULTURAL_ACTIVITIES_ECT_RATE,AGRICULTURAL_ACTIVITIES_DISTRIBUTION,AGRICULTURAL_ACTIVITIES_VAT_RATE)
                    
                    multi_time_usage_fee = calculate_multi_time_pricing_usage_fee(total_daytime_usage,total_peak_usage,total_night_usage,AGRICULTURAL_ACTIVITIES_DAY,AGRICULTURAL_ACTIVITIES_PEAK,AGRICULTURAL_ACTIVITIES_NIGHT)
                    multi_time_total_fee = calculate_invoice_amount(multi_time_usage_fee,INDUSTRY_ECT_RATE,INDUSTRY_DISTRIBUTION,INDUSTRY_VAT_RATE)

                    agricultural_activites_counter += 1
                    agricultural_activities_total_electricity_usage += total_usage

            if invoice_amount < multi_time_total_fee :  # To compare profit and loss situation compared to other tariff
                profit_loss_situation = "Profit"
                profit_loss_amount = multi_time_total_fee - invoice_amount
            elif invoice_amount == multi_time_total_fee :
                profit_loss_situation = "equal"
                profit_loss_amount = 0                           
            else:                                  
                profit_loss_situation = "Loss"
                profit_loss_amount = multi_time_total_fee - invoice_amount
        

        else :      # to bill multi time tariff
            match consumer_type_code :
                case "i" | "I":
                    usage_fee = calculate_multi_time_pricing_usage_fee(total_daytime_usage,total_peak_usage,total_night_usage,INDUSTRY_DAY,INDUSTRY_PEAK,INDUSTRY_NIGHT)
                    ect_fee,vat_fee,invoice_amount= calculate_taxes_and_invoice_amount(usage_fee,INDUSTRY_ECT_RATE,INDUSTRY_DISTRIBUTION,INDUSTRY_VAT_RATE)

                    single_time_usage_fee = calculate_fixed_pricing_usage_fee(total_usage,INDUSTRY_SINGLE)
                    single_time_total_fee = calculate_invoice_amount(single_time_usage_fee,INDUSTRY_ECT_RATE,INDUSTRY_DISTRIBUTION,INDUSTRY_VAT_RATE)

                    industry_counter += 1
                    industry_total_electricity_usage += total_usage

                    if invoice_amount > 100000 or total_usage > 10000:
                        industry_over_than_10000kwh_or_100000TL_counter += 1

                case "p" | "P":
                    usage_fee = calculate_multi_time_pricing_usage_fee(total_daytime_usage,total_peak_usage,total_night_usage,PPS_DAY,PPS_PEAK,PPS_NIGHT)
                    ect_fee,vat_fee,invoice_amount= calculate_taxes_and_invoice_amount(usage_fee,PPS_ECT_RATE,PPS_DISTRIBUTION,PPS_VAT_RATE)

                    single_time_usage_fee = calculate_two_stage_pricing_usage_fee(total_usage,PPS_DAILY_AVERAGE_UPPER_LIMIT,PPS_LOW_TARIFF,PPS_HIGH_TARIFF)
                    single_time_total_fee = calculate_invoice_amount(single_time_usage_fee,INDUSTRY_ECT_RATE,INDUSTRY_DISTRIBUTION,INDUSTRY_VAT_RATE)
                    pps_multi_time_tariff_counter += 1
                    pps_multi_time_tariff_total_electricity_usage +=total_usage
                    multi_time_pps_days_between_previous_and_current_counter += days_between_previous_and_current

                case "r" | "R":
                    usage_fee = calculate_multi_time_pricing_usage_fee(total_daytime_usage,total_peak_usage,total_night_usage,RESIDENTAL_DAYTIME_FEE,RESIDENTAL_PEAK_FEE,RESIDENTAL_NIGHT_FEE)
                    ect_fee,vat_fee,invoice_amount= calculate_taxes_and_invoice_amount(usage_fee,RESIDENTAL_ECT_RATE,RESIDENTAL_DISTRIBUTION,R_VAT_RATE)

                    single_time_usage_fee = calculate_two_stage_pricing_usage_fee(total_usage,RESIDENTAL_DAILY_AVERAGE_UPPER_LIMIT,RESIDENTAL_LOW_TARIFF,RESIDENTAL_HIGH_TARIFF)
                    single_time_total_fee = calculate_invoice_amount(single_time_usage_fee,INDUSTRY_ECT_RATE,INDUSTRY_DISTRIBUTION,INDUSTRY_VAT_RATE)

                    residental_counter += 1
                    residental_total_electricity_usage += total_usage

                case "a" | "A":
                    usage_fee = calculate_multi_time_pricing_usage_fee(total_daytime_usage,total_peak_usage,total_night_usage,AGRICULTURAL_ACTIVITIES_DAY,AGRICULTURAL_ACTIVITIES_PEAK,AGRICULTURAL_ACTIVITIES_NIGHT)
                    ect_fee,vat_fee,invoice_amount= calculate_taxes_and_invoice_amount(usage_fee,AGRICULTURAL_ACTIVITIES_ECT_RATE,AGRICULTURAL_ACTIVITIES_DISTRIBUTION,AGRICULTURAL_ACTIVITIES_VAT_RATE)

                    single_time_usage_fee = calculate_fixed_pricing_usage_fee(total_usage,AGRICULTURAL_ACTIVITIES_SINGLE)
                    single_time_total_fee = calculate_invoice_amount(single_time_usage_fee,INDUSTRY_ECT_RATE,INDUSTRY_DISTRIBUTION,INDUSTRY_VAT_RATE)
                    
                    agricultural_activites_counter += 1
                    agricultural_activities_total_electricity_usage += total_usage
                
            if invoice_amount < single_time_total_fee :  # To compare profit and loss situation compared to other tariff
                profit_loss_situation = "Profit"
                profit_loss_amount = single_time_total_fee - invoice_amount
            elif invoice_amount == single_time_total_fee:
                profit_loss_situation = "equal"
                profit_loss_amount = 0
            else:                                  
                profit_loss_situation = "Loss"
                profit_loss_amount = single_time_total_fee - invoice_amount
                multi_time_tariff_loss_counter += 1
            
            preferred_multi_time_tariff_counter += 1

    if consumer_type_code in ["r","R"]:
        daily_average_consumption = total_usage/days_between_previous_and_current

        if daily_average_consumption>residental_higher_daily_average_consumption:  # Information of the consumer who consumes the most within the residental type
            residental_higher_daily_average_consumption_consumer_no = consumer_no
            residental_higher_daily_average_consumption_used_electricity = total_usage
            residental_higher_daily_average_consumption_days_between_previous_and_current = days_between_previous_and_current
            residental_higher_daily_average_consumption_invoice_amount = invoice_amount
    else:

        if invoice_amount>not_residental_higher_consumption_invoice_amount:  # Information of the consumer who consumes the most, other than the residental type
            not_residental_higher_consumption_consumer_no = consumer_no
            not_residental_higher_consumption_consumer_type = consumer_type
            not_residental_higher_consumption_used_electricity = total_usage
            not_residental_higher_consumption_days_between_previous_and_current = days_between_previous_and_current
            not_residental_higher_consumption_invoice_amount = invoice_amount

           
        
    total_invoice_amount += invoice_amount
    total_revenue_amount_municipality += ect_fee
    total_revenue_amount_state += vat_fee


    item_seperator_str = "------------------------------------------------------------------------------------------------------"
    consumer_seperator_str = "******************************************************************************************************"

    print(item_seperator_str)
    print(f"-Consumer No                                                                         : {consumer_no}\n{item_seperator_str}")
    print(f"-Consumer Type                                                                       : {consumer_type}\n{item_seperator_str}")
    print(f"-Daytime period electricity consumption amount in this period                        : {total_daytime_usage:.2f}kWh\n{item_seperator_str}")
    print(f"-Peak period electricity consumption amount in this period                           : {total_peak_usage:.2f}kWh\n{item_seperator_str}")
    print(f"-Night period electricity consumption amount in this period                          : {total_night_usage:.2f}kWh\n{item_seperator_str}")
    print(f"-Total electricity consumption amount in this period                                 : {total_usage:.2f}kWh\n{item_seperator_str}")
    print(f"-Total electricity consumption fee for this period                                   : {usage_fee:.2f}TL\n{item_seperator_str}")
    print(f"-ECT amount to be transferred to the municipality this period                        : {ect_fee:.2f}TL\n{item_seperator_str}")
    print(f"-VAT amount to be transferred to the state this period                               : {vat_fee:.2f}TL\n{item_seperator_str}")
    print(f"-Total invoice amount for this period                                                : {invoice_amount:.2f}TL\n{item_seperator_str}")
    if not(is_single_price):
        print(f"-Profit/loss situation compared to other tariff                                      : {profit_loss_situation}\namount                                                                               : {profit_loss_amount:.2f}TL\n{item_seperator_str}")
    print(f"-Total electricity consumption amount in the current year as of this billing period  : {final_current_year_total_consumption_electricity:.2f}(kWh)\n{item_seperator_str}")
    if final_current_year_total_consumption_electricity > 1000 :
        print("\n-You deserve to be a free consumer\n",consumer_seperator_str,)
    else:
        print("\n-You did not deserve to be a free consumer\n",consumer_seperator_str)


    consumer_no = int(input("Enter consumer's number(if there are no other users enter 0)\n"))
    consumer_no = control_zero_or_bigger_zero(consumer_no)



article_seperator_str = "**************************************************************************************************************************************************************"
item_seperator_str = "--------------------------------------------------------------------------------------------------------------------------------------------------------------"

print(f"\n{item_seperator_str}")

print(f"Number of industrial consumers                                       : {industry_counter}\n{item_seperator_str}")
print(f"Percentage of industrial consumers                                   : {calculate_percentage(industry_counter,total_consumer):.2f}%\n{item_seperator_str}")
print(f"Average electricity consumption amounts in this period               : {calculate_average_function(industry_total_electricity_usage,industry_counter):.2f}kWh\n{item_seperator_str}")
print(f"Total electricity consumption amounts in this period                 : {industry_total_electricity_usage:.2f}kWh\n{item_seperator_str}\n")
print(item_seperator_str)
print(f"Number of public and private services sector and other consumers     : {total_pps_consumer}\n{item_seperator_str}")
print(f"Percentage of public and private services sector and other consumers : {calculate_percentage(total_pps_consumer,total_consumer):.2f}%\n{item_seperator_str}")
print(f"Average electricity consumption amounts in this period               : {calculate_average_function(pps_total_electricity_usage,total_pps_consumer):.2f}kWh\n{item_seperator_str}")
print(f"Total electricity consumption amounts in this period                 : {pps_total_electricity_usage:.2f}kWh\n{item_seperator_str}\n")
print(item_seperator_str)
print(f"Number of residental consumers                                       : {residental_counter}\n{item_seperator_str}")
print(f"Percentage of residental consumers                                   : {calculate_percentage(residental_counter,total_consumer):.2f}%\n{item_seperator_str}")
print(f"Average electricity consumption amounts in this period               : {calculate_average_function(residental_total_electricity_usage,residental_counter):.2f}kWh\n{item_seperator_str}")
print(f"Total electricity consumption amounts in this period                 : {residental_total_electricity_usage:.2f}kWh\n{item_seperator_str}\n")
print(item_seperator_str)
print(f"Number of agricultural activities consumers                          : {agricultural_activites_counter}\n{item_seperator_str}")
print(f"Percentage of agricultural activities consumers                      : {calculate_percentage(agricultural_activites_counter,total_consumer):.2f}%\n{item_seperator_str}")
print(f"Average electricity consumption amounts in this period               : {calculate_average_function(agricultural_activities_total_electricity_usage,agricultural_activites_counter):.2f}kWh\n{item_seperator_str}")
print(f"Total electricity consumption amounts in this period                 : {agricultural_activities_total_electricity_usage:.2f}kWh\n{item_seperator_str}\n")
print(item_seperator_str)
print(f"Number of lightning consumers                                        : {lightning_counter}\n{item_seperator_str}")
print(f"Percentage of lightning consumers                                    : {calculate_percentage(lightning_counter,total_consumer):.2f}%\n{item_seperator_str}")
print(f"Average electricity consumption amounts in this period               : {calculate_average_function(lightning_total_electricity_usage,lightning_counter):.2f}kWh\n{item_seperator_str}")
print(f"Total electricity consumption amounts in this period                 : {lightning_total_electricity_usage:.2f}kWh\n{item_seperator_str}\n ")

print(f"Bornova's total electricity consumption amount in this period        : {total_consumption_amount:.2f}kWh")
print(article_seperator_str)
print(item_seperator_str)
print(f"Number of public and private services sector and other type consumers who prefer single-time : {pps_single_time_tariff_counter}\n{item_seperator_str}")
print(f"Percentage of public and private services sector and other type consumers                    : {calculate_percentage(pps_single_time_tariff_counter,total_pps_consumer):.2f}%\n{item_seperator_str}")
print(f"Average daily electricity consumption amounts in this period                                 : {calculate_daily_average_consumption(pps_single_time_tariff_total_electricity_usage,single_time_pps_days_between_previous_and_current_counter):.2f}kWh\n{item_seperator_str}")
print(item_seperator_str)
print(f"Number of public and private services sector and other type consumers who prefer multi-time : {pps_multi_time_tariff_counter}\n{item_seperator_str}")
print(f"Percentage of public and private services sector and other type consumers                   : {calculate_percentage(pps_multi_time_tariff_counter,total_pps_consumer):.2f}%\n{item_seperator_str}")
print(f"Average daily electricity consumption amounts in this period                                : {calculate_daily_average_consumption(pps_multi_time_tariff_total_electricity_usage,multi_time_pps_days_between_previous_and_current_counter):.2f}kWh\n{item_seperator_str}")
print(article_seperator_str)
print(item_seperator_str)
print(f"The number of industry type consumers whose electricity consumption amount is more\nthan 10000 kWh or whose electricity bill is more than 100000 TL in the relevant period: {industry_over_than_10000kwh_or_100000TL_counter}\n{item_seperator_str}")
print(f"Percentage of industry consumers                                                      : {calculate_percentage(industry_over_than_10000kwh_or_100000TL_counter,industry_counter):.2f}%\n{item_seperator_str}")
print(article_seperator_str)
print(item_seperator_str)
print(f"Consumer no of the residential type consumer with the highest daily average electricity consumption amount in the relevant period: {residental_higher_daily_average_consumption_consumer_no}\n{item_seperator_str}")
print(f"Daily average electricity consumption amount                                                                                     : {residental_higher_daily_average_consumption:.2f}kWh\n{item_seperator_str}")
print(f"Total bill amount for this period                                                                                                : {residental_higher_daily_average_consumption_invoice_amount:.2f}TL\n{item_seperator_str}")
print(article_seperator_str)
print(item_seperator_str)
print(f"Consumer no of the consumer other than the residential type with the highest total bill amount in the relevant period: {not_residental_higher_consumption_consumer_no}\n{item_seperator_str}")
print(f"consumer type                                                                                                        : {not_residental_higher_consumption_consumer_type}\n{item_seperator_str}")
print(f"Daily average electricity consumption amount                                                                         : {not_residental_higher_daily_average_consumption:.2f}kWh\n{item_seperator_str}")
print(f"Total bill amount for this period                                                                                    : {not_residental_higher_consumption_invoice_amount:.2f}TL\n{item_seperator_str}")
print(article_seperator_str)
print(item_seperator_str)
print(f"Total revenue amount obtained by the GDZ corporation : {(total_invoice_amount - total_revenue_amount_state - total_revenue_amount_municipality):.2f}TL\n{item_seperator_str}")
print(f"Total revenue amount obtained by the municipality    : {total_revenue_amount_municipality:.2f}TL\n{item_seperator_str}")
print(f"Total revenue amount obtained by the state           : {total_revenue_amount_state:.2f}TL\n{item_seperator_str}")   
print(article_seperator_str)
print(item_seperator_str)
print(f"The percentage of those who made a loss despite choosing multi-time tariff in the relevant period: {calculate_percentage(multi_time_tariff_loss_counter,preferred_multi_time_tariff_counter):.2f}%\n{item_seperator_str}")