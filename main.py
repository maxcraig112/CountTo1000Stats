import json

FILENAME = "count to 1000.json"

def main():
    # Read JSON file
    with open(FILENAME, "r", encoding="utf-8") as file:
        data = json.load(file)

    user_ended_count = {}
    user_score = {}
    #for every message
    count = 1
    for message in data["messages"]:
        author = message["author"]["name"]
        message = message["content"].split(" ")[0]
        try:

            number_sent = int(message)
            # if the number entered is expected, we're good
            if number_sent == count:
                count += 1
        except:
            # if the count wasn't 1, it means that they messed up somewhere inbetween 1 and 1000
            # if the count is 1, then there were probably messages sent after a mess up that shouldn't be counted
            if count != 1:
                # add their name to the dictionary if they haven't previously messed up
                if author not in user_ended_count:
                    user_ended_count[author] = 0
                    user_score[author] = 0

                # add to their score
                user_ended_count[author] += 1
                user_score[author] += count

                #reset the count, assuming they'll start again at 1
                count = 1
    
    #sort the dictionary from highest to lowest
    sorted_counts = sorted(user_ended_count.items(), key=lambda x: x[1], reverse=True)
    sorted_scores = sorted(user_score.items(), key=lambda x: x[1], reverse=True)

    #print results, this is formatted to be pasted into discord
    print("## LEADERBOARD BY NUMBER OF TIMES MESSED UP")
    for name, count in sorted_counts:
        print(f"**{name}**", ":", count)


    print()
    print("## LEADERBOARD BY TOTAL AMOUNT MESSED UP")
    for name, count in sorted_scores:
        print(f"**{name}**", ":", count)

if __name__ == "__main__":
    main()
