from dataprocessing import ProcessOutlet

#outlets = ["economictimes", "hindustantimes", "financialexpress", "thehindu", "ndtv", "news18"]
outlets = ["news18"]
for outlet in outlets:
    process_outlet = ProcessOutlet(outlet)
    
    # Call the specific processing method for each outlet
    if outlet == "ndtv":
        process_outlet.ProcessNDTV()
    else:
        getattr(process_outlet, f"Process{outlet.capitalize()}")()
    
    # Remove duplicate titles for all outlets
    process_outlet.remove_duplicate_titles()

    print(f"Processed {outlet}")

