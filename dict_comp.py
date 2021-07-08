
def dict_comp(stop, step):
      if stop < step:
            print(" 'Stop' must not be less than 'step' ")
      dict = {}
      floor_div = stop//step
      remainder = stop % step
      factor_of_4 = stop - remainder
      list_of_range = list(range(1,factor_of_4+1))
      output2 =[f"items-{n}" for n in list(range(1,floor_div + 1))]
      output1 = [list_of_range[i:i + step] for i in range(0, len(list_of_range), step) ]
      counter = 0
      for iter in output2:
            dict[iter] = output1[counter]
            counter += 1
      print(dict)   
      
dict_comp(10, 4)   
  
