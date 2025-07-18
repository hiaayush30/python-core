browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
print(browsing_session)

last_visited = browsing_session[-1]
print(last_visited)

browsing_session.pop()
 
if not browsing_session:  # as [] evaluates to False
    print("back button disabled")