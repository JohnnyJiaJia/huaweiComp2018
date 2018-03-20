# coding=utf-8
import preprocessing


def predict_vm(ecs_lines, input_lines):
    # Do your work from here#
    result = []
    if ecs_lines is None:
        print 'ecs information is none'
        return result
    if input_lines is None:
        print 'input file information is none'
        return result

    mission = preprocessing.preprocess_input(input_lines)

    flavor_dict = preprocessing.preprocess_ecs_info(ecs_lines, mission)

    data_dict_merge = preprocessing.merge(flavor_dict, mission)
    print("a")
    return result
