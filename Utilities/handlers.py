class DatasetHandlers:
    #create a list with tuples from the dataset to input the parametrize decorator
    def test_handler(file):
        iteration_list = []
        result = tuple(file.values())
        iteration_list.append(result)
        return iteration_list
