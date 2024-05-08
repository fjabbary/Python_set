# =============== Task 1 =================
our_routes = {"LAX", "JFK", "CDG", "DXB", "ORD"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK", "SFO"}

common_destinations = our_routes.intersection(competitor_routes)
print("common_destinations", common_destinations)

our_unique_destinations = our_routes.difference(competitor_routes)
print("our_unique_destinations", our_unique_destinations)

not_common_destinations = our_routes.symmetric_difference(competitor_routes)
print("not_common_destinations", not_common_destinations)



# =============== Task 2 =================
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# list of unique customer ids
unique_customer_ids = list(set(customer_ids))
print(unique_customer_ids)