# Create a module similar to `sklearn's` `datasets` module

### Setting:

* We have seen in the lectures how we can load sklearn's intrnal datasets using method `load_data()`. Furthermore, we also know how we can extract the feature matrix and target array using attributes like `.data` and `.target`.

* In this exercise we will try to build to our own implimentation of sklearn-like module which has similar properties and attributes.

### Task: Create a class called `my_sklearn`

#### 1. Initialize the Class with `__init__()` method

* __init__() method should accept following parameteres and save them internal attributes of the class
    * path: str (path to the csv file)
    * is_header: boolean (if the file has header)
    * target_variable: str (target variable)
    * feature_names: list or None (Not required if the file already has headers) (Default None)
    * random_state: int (Default value 7)
    

* Also, perform following operations:
    * Create an internal attribute called `_df` which will store the CSV file as a dataframe
    * Check if the CSV file has header using `is_header` attribute
        * If the file has header then import header while importing the CSV file
        * If the file does not have header, then use `feature_names` and `target_variable` as headers
        * If the file does not have heade, and `feature_names` is not provided, raise error
    * If the CSV file had the header, the value of `feature_names` should be None. In that case, store feature names in `feature_names` attribute.

#### 2. Define `__repr__()` method

* `__repr__()` decided how your class is represented, let's say when printed. Read more about this method [here](https://stackoverflow.com/questions/1984162/purpose-of-pythons-repr).

* We want our class's `Representation` in the format:
    
    `Path: path/to/the/file.csv`
    
    `feature variables: ['your', 'list', 'of', 'features', 'here']`

    `target variable: your_target_variable `

#### 3. Define `load_data()` method

*  **`load_data()` with following parameters and save them as attributes:**

    * feature_subset: list of features to be selected or None if all features are to be selected (Optional) (Default None)
    * train_size: float, fraction [0, 1] of data to be selected as training set (Optional)(Default 0.8)
    * CV_subset: "train", "test" or "all" (default "train")
    
* Based on given parameters, the method stores feature matrix in `data` attribute and target array in `target` attribute in bunch form

**Note:** 

* You can use `pandas`, `numpy` and `sklearn`'s `train_test_split` libraries.
* Error handling

