INPUT_FILE_NAME = "barefoot_deps.rsf"
OUTPUT_FILE_NAME = "barefoot_deps_simplified.txt"
OMIT_LIST = ["java.",
             "Test",
            "Logger",
             "ZMQ.",
             "JSONException",
             "JSONObject",
             "JSONArray",
             "Ignore",
             "Point",
             "QuadTree",
             "Envelope2D",
             "Polyline",
             "Polygon",
             "Geodesic",
             "Gnomonic",
             "GeodesicData"]

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
                    if "com.bmwcarit.barefoot.analysis" in split_line[x]:
                        split_line[x] = "com.bmwcarit.barefoot.analysis"
                    elif "com.bmwcarit.barefoot.markov" in split_line[x]:
                        split_line[x] = "com.bmwcarit.barefoot.markov"
                    elif "com.bmwcarit.barefoot.matcher" in split_line[x]:
                        split_line[x] = "com.bmwcarit.barefoot.matcher"
                    elif "com.bmwcarit.barefoot.roadmap" in split_line[x]:
                        split_line[x] = "com.bmwcarit.barefoot.roadmap"
                    elif "com.bmwcarit.barefoot.road" in split_line[x]:
                        split_line[x] = "com.bmwcarit.barefoot.road"
                    elif "com.bmwcarit.barefoot.scheduler" in split_line[x]:
                        split_line[x] = "com.bmwcarit.barefoot.scheduler"
                    elif "com.bmwcarit.barefoot.spatial" in split_line[x]:
                        split_line[x] = "com.bmwcarit.barefoot.spatial"
                    elif "com.bmwcarit.barefoot.topology" in split_line[x]:
                        split_line[x] = "com.bmwcarit.barefoot.topology"
                    elif "com.bmwcarit.barefoot.tracker" in split_line[x]:
                        split_line[x] = "com.bmwcarit.barefoot.tracker"
                    elif "com.bmwcarit.barefoot.util" in split_line[x]:
                        split_line[x] = "com.bmwcarit.barefoot.util"
                    else:
                        #exit("Bruh")
                        print("")

                # Insert into list of dependencies
                dependencies.append(split_line[0] + " ---Uses--> " + split_line[1] + "\n")
        
        # Remove duplicates
        dependencies = list(dict.fromkeys(dependencies))

        for dependency in dependencies:
            output_file.write(dependency)
