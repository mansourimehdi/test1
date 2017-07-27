# --------------------------- START CHECK PASSANGER APPLICABLE -------------------------------------------------------
''' check if the departure airport is applicable based on UE261 2004:
1- departing from an airport located in the territory of a Member State to which the Treaty applies;
The protection accorded to passengers departing from or to an airport located in a Member State should be extended to
those leaving an airport located in a third country for one situated in a Member State, when a Community carrier
operates the flight and where a community carrier is defined as any carrier licensed to operate within that community.
Or
2- departing from an EU member state.
'''

def is_dep_airport_ok(dep_airport):
    is_applicable = True
    return is_applicable

''' 
check if the arrival airport is applicable based on UE261 2004:
1- travelling to an EU member state on an airline based in an EU member state.
'''
def is_arr_airport_ok(arr_airport):
    is_applicable = True
    return is_applicable

'''
check if that person has a confirmed reservation on the flight:
'''
def is_per_res_conf(res_status):
    if res_status
        is_applicable = True
    else
        is_applicable = False
    return is_applicable

'''
check if that person has checked in on time:
1- arrived in time for check-in as indicated on the ticket communication from the airline
or 
2- if no time is so indicated, no less than 45 minutes prior to the scheduled departure time of the flight
'''
def is_per_checked_in_on_time(check_in_time, flight_departure_time):
    if check_in_time == null
        calc_check_in_time = per_check_in_time + 45
        if calc_check_in_time > flight_departure_time
            is_applicable = False
        else
            is_applicable = True
    else
        if check_in_time > per_check_in_time
            is_application = True
        else
            is_application = False
    return is_application

'''
check if this person have been transferred from the flight for which he/she held a reservation to some other flight
'''
def is_per_trans(res_num):
    is_applicable = True
    return is_applicable

'''
check if the passenger is not travelling on a free or discounted ticket not available to the general public, other than a ticket 
obtained from a frequent flyer programme.
It does not apply to helicopter flights, to any flight not operated by a fixed-wing aircraft, nor to flights from 
Gibraltar Airport.[1] While Switzerland is not a Member State of the EU, the regulation does apply to it under 
bilateral agreements.
'''
def is_fli_gen_pub(res_num):
    is_applicable = True
    return is_applicable

'''
Main function to check if passanger applicable
'''
def is_applicable(req):
    # check if applicable
    if (
                    (is_dep_airport_ok(req['dep_airport']) or is_arr_airport_ok(req['arr_airport'])) and
                    ((is_per_res_conf(req['res_num']) and is_per_checked_in_on_time(req['res_num'])) or is_per_trans(
                        req['res_num'])) and
                is_fli_gen_pub(req['res_num'])
    ):
        is_applicable = True
    else:
        is_applicable = False
    return is_applicable