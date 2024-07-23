def update_file(filepath, key, Value):

    with open(filepath, "r") as file:
        lines = file.readlines()
    
    with open(filepath, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + Value + "\n")
            else:
                file.write(line)
            

update_file("/workspaces/python-for-devops/Day-12/server.conf", "MAX_CONNECTIONS", "10000")
