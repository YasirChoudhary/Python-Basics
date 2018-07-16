cost_file = open("costprice.csv").readlines()
prod_file = open("product.csv").readlines()


file_to_save = open("merge.csv", "w")
file_to_save.write("id,name,standard_price,default_code\n")


for row in cost_file:
    row = row.strip()
    
    internal_ref, standard_price = row.split(",")
    internal_ref = internal_ref.strip()
    #Don't do this it will remove .0 but after it will join the cost price and the cost price will increase
    #standard_price = standard_price.replace(".0","").strip() 
    standard_price = standard_price.strip() 

    for row in prod_file:
        row = row.strip()
        c_id, name, default_code = row.split(",")
        c_id = c_id.strip()
        name = name.strip()
        default_code = default_code.strip()
        
        if internal_ref == default_code:
            rec = "{}, {}, {}, {}\n".format(c_id, name, standard_price, default_code)
            file_to_save.write(rec)
            break

#cost_file.close()
#prod_file.close()
file_to_save.close()
