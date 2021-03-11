INPUT_FILE_NAME = "lib_deps.rsf"
OUTPUT_FILE_NAME = "lib_deps_simplified.txt"
OMIT_LIST = ["java.",
             "org.apache",
             "com.google",
             "javax."]

dependencies = []

with open(INPUT_FILE_NAME, encoding = 'utf-8') as input_file:
    with open(OUTPUT_FILE_NAME, "w") as output_file:
        lines = input_file.readlines()

        for line in lines:
            if any(x in line for x in OMIT_LIST):
                pass
            else:
                split_line = line.split(' ')
                split_line.pop(0)

                # Process split line
                for x in range(2):
                    if "com.pixeltron.mapquest" in split_line[x]:
                        split_line[x] = "com.pixeltron.mapquest"
                    elif "com.pixeltron.maproulette.models" in split_line[x]:
                        split_line[x] = "com.pixeltron.maproulette.models"
                    elif "com.pixeltron.maproulette.responses" in split_line[x]:
                        split_line[x] = "com.pixeltron.maproulette.responses"
                    elif "com.pixeltron.maproulette.servlets" in split_line[x]:
                        split_line[x] = "com.pixeltron.maproulette.servlets"
                    elif "org.json" in split_line[x]:
                        split_line[x] = "org.json"
                    elif "fi.foyt.foursquare.api" in split_line[x]:
                        split_line[x] = "fi.foyt.foursquare.api"
                    else:
                        exit("Bruh")

                # Insert into list of dependencies
                dependencies.append(split_line[0] + " ---Uses--> " + split_line[1] + "\n")
        
        # Remove duplicates
        dependencies = list(dict.fromkeys(dependencies))

        for dependency in dependencies:
            output_file.write(dependency)