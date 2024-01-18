import os
import glob
import pickle
import json
import yaml
import jsonschema
from jsonschema import validate


class DirectoryOperations:
    @staticmethod
    def check_dir_exists(dir_path):
        if os.path.isdir(dir_path):
            return True
        else:
            return False

    @staticmethod
    def create_dir(dir_path):
        try:
            os.makedirs(dir_path)
        except OSError as exception:
            print("Create directory failed: " + str(exception))

    @staticmethod
    def create_dir_by_file_path(file_path):
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
        except OSError as exception:
            print("Create directory failed: " + str(exception))

    @staticmethod
    def search_last_dir(dir_path):
        DirectoryOperations.check_dir_exists(dir_path)
        return max(glob.glob(os.path.join(dir_path, '*/')), key=os.path.getmtime)

    @staticmethod
    def find_files_using_pattern(files_pattern):
        return glob.glob(files_pattern)


class FileOperations:
    @staticmethod
    def check_file_exists(file_path):
        if os.path.isfile(file_path):
            return True
        else:
            raise Exception("File does not exist.")

    @staticmethod
    def get_file_name(file_path, extension=True):
        if extension:
            return os.path.basename(file_path)
        else:
            return os.path.basename(file_path).split('.')[0]

    @staticmethod
    def read_file(file_path):
        FileOperations.check_file_exists(file_path)
        with open(file_path, 'r', encoding="utf-8") as file_obj:
            file_content = file_obj.read()
            file_obj.close()
        return file_content

    @staticmethod
    def read_file_lines(file_path):
        FileOperations.check_file_exists(file_path)
        with open(file_path, 'r', encoding="utf-8") as file_obj:
            file_content = file_obj.readlines()
            file_obj.close()
        return file_content

    @staticmethod
    def write_file(file_path, string):
        DirectoryOperations.create_dir_by_file_path(file_path)
        with open(file_path, 'w', encoding="utf-8") as file_obj:
            file_obj.write(string)
            file_obj.close()

    @staticmethod
    def append_text_file(file_path, string):
        FileOperations.check_file_exists(file_path)
        with open(file_path, 'a', encoding="utf-8") as file_obj:
            file_obj.write(string)
            file_obj.close()


class JsonFileOperations:
    @staticmethod
    def read_file(file_path):
        FileOperations.check_file_exists(file_path)
        with open(file_path, 'r', encoding="utf-8") as json_obj:
            return json.loads(json_obj.read())

    @staticmethod
    def write_file(file_path, string):
        DirectoryOperations.create_dir_by_file_path(file_path)
        with open(file_path, 'w', encoding="utf-8") as json_obj:
            json.dump(string, json_obj, indent=4)
            json_obj.close()

    @staticmethod
    def validate_data_schema_dict(json_data, data_schema):
        try:
            validate(instance=json_data, schema=data_schema)
        except jsonschema.exceptions.ValidationError:
            return False
        return True

    @staticmethod
    def validate_data_schema_dict_of_dicts(json_data, data_schema):
        if type(json_data) is dict:
            sub_json_data = json_data.values()
            if len(sub_json_data) == 0:
                return False
            else:
                for sub_data in sub_json_data:
                    if not JsonFileOperations.validate_data_schema_dict(sub_data, data_schema):
                        return False
                return True
        else:
            return False

    @staticmethod
    def pretty_print_dict(dictionary):
        parsed = json.loads(json.dumps(dictionary, ensure_ascii=False).encode('utf8'))
        print(json.dumps(parsed, indent=4, sort_keys=True, ensure_ascii=False))


class YamlFileOperations:
    @staticmethod
    def read_file(file_path):
        FileOperations.check_file_exists(file_path)
        with open(file_path, 'r', encoding="utf-8") as yaml_obj:
            return yaml.load(yaml_obj, Loader=yaml.FullLoader)

    @staticmethod
    def write_file(file_path, string):
        DirectoryOperations.create_dir_by_file_path(file_path)
        with open(file_path, 'w', encoding="utf-8") as yaml_obj:
            yaml.dump(string, yaml_obj, default_flow_style=False)
            yaml_obj.close()


class PickleFileOperations:
    @staticmethod
    def read_file(file_path):
        FileOperations.check_file_exists(file_path)
        with open(file_path, 'rb') as pickle_obj:
            return pickle.load(pickle_obj)

    @staticmethod
    def write_file(file_path, data):
        DirectoryOperations.create_dir_by_file_path(file_path)
        with open(file_path, 'wb') as pickle_obj:
            pickle.dump(data, pickle_obj)
            pickle_obj.close()
