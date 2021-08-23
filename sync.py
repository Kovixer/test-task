from sys import argv
import os
import shutil
import time

source = argv[1]
replica = argv[2]
interval = argv[3]
path_log_file = argv[4]
path_log_file += "/log.txt" 


def get_list_of_filename(path):
	l = []
	for root, dirs, files in os.walk(path):
			for filename in files:
				l.append(filename)
	return l


if __name__ == "__main__":
	log_file = open(path_log_file, mode="w")
	source_list = []
	replica_list = []
	s_l = get_list_of_filename(source)
	while True:
		source_list = get_list_of_filename(source)
		for i in source_list:
			if i not in s_l:
				log_file.write(f"create file: {i}\n")
				print(f"create file: {i}")
		s_l = get_list_of_filename(source)
		replica_list = get_list_of_filename(replica)
		for i in replica_list:
			if i not in source_list:
				name = replica + '/' + i
				os.remove(name)
				log_file.write(f"delete file: {i}\n")
				print(f"delete file: {i}")
		for i in source_list:
			if i not in replica_list:
				name = source + '/' + i
				shutil.copy(name, replica)
				log_file.write(f"copy file: {i}\n")
				print(f"copy file: {i}")
		time.sleep(int(interval))