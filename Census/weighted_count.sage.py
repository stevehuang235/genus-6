

# This file was *autogenerated* from the file weighted_count.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)# This script computes the weighted sum of the number of F_2 points on generic curves of genus 6

import sys
import ast
import os
from collections import defaultdict 


def weighted_sum(root_directory1, root_directory2):

    curves = defaultdict(list)
    # Iterate over each file in ./data_unfiltered_updated/ to create a hash table for the 
    # F_2 point count for each curve
    for root, dirs, files in os.walk(root_directory2):
        for file in files:
            file_path = os.path.join(root, file)

            if 'genus' in file_path:
                with open(file_path, 'r') as f:
                    # Read all lines from the file and store them in the dictionary
                    lines = f.read().split('\n')
                    if len(lines) > _sage_const_2 :
                        if 'generic' in file_path:
                            for ele in lines[_sage_const_1 :-_sage_const_1 ]:
                                tmp = ast.literal_eval(ele)
                                curves[tuple(tmp[_sage_const_1 ])].append(tmp[_sage_const_0 ][_sage_const_0 ])
                        else:
                            for ele in lines[:-_sage_const_1 ]:
                                tmp = ast.literal_eval(ele)
                                curves[tuple(tmp[_sage_const_1 ])].append(tmp[_sage_const_0 ][_sage_const_0 ])

    sum = _sage_const_0 
    for root, dirs, files in os.walk(root_directory1):
        for file in files:
            file_path = os.path.join(root, file)
            if 'isom_class' in file_path:
                with open(file_path, 'r') as f:
                    lines = f.read().split('\n')
                    for line in lines[:-_sage_const_1 ]:
                        tmp = ast.literal_eval(line)
                        ord_aut = tmp[_sage_const_1 ]
                        curve = tmp[_sage_const_0 ]
                        point_count = curves[tuple(curve)][_sage_const_0 ]
                        sum += Integer(point_count)/Integer(ord_aut)
    
    return sum 

# Replace 'your_directory_path' with the path of the directory you want to start iterating from
directory_path1 = sys.argv[_sage_const_1 ]
directory_path2 = sys.argv[_sage_const_2 ]
result = weighted_sum(directory_path1, directory_path2)
print('The weighted sum of F_2 points in ', directory_path1, ' is ', result)
