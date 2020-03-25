#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import os

if __name__ == '__main__':
    delte_dir = 'delete/'
    insert_dir = 'insert/'

    term_map = []
    with open('map.txt','r') as MF:
        for line in MF.readlines():
            term_map.append(line.strip())


    for files in os.listdir('src/'):
        file_list = 'src/' + files
        prod_info = {}
        with open(file_list,'r') as PD:
            for line in PD.readlines():
                res = line.strip().split('\t')
                prod_info[res[1]] = [res[0],res[2]]
        delete_file = delte_dir + files +'.sql'
        with open(delete_file,'w') as DF:
            for term_id in prod_info:
                if term_id not in term_map:
                    string1 = "delete from ucr_cen1.td_s_prod_res_rel where product_id='{}' and MACHINE_TYPE_CODE='{}';\n".format(prod_info[term_id][0],term_id)
                    string2 = "delete from ucr_cprod.td_s_prod_res_rel where product_id='{}' and MACHINE_TYPE_CODE='{}' and PROVINCE_CODE='{}';\n".format(prod_info[term_id][0],term_id,prod_info[term_id][1])
                    DF.write(string1)
                    DF.write(string2)
        insert_file = insert_dir + files
        with open(insert_file,'w') as SF:
            for term_id in term_map:
                if term_id not in prod_info:
                    string = term_id + '\n'
                    SF.write(string)