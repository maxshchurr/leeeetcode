"""

There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

Important
Please look at the examples and clarifications below, to ensure you understand the task correctly :)

Examples
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
Clarifications
There is only ONE queue serving many tills, and
The order of the queue NEVER changes, and
The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
N.B. You should assume that all the test input will be valid, as specified above.

"""


def queue_time(customers, n):
    # queue = [0 for i in range n]
    queue = [0] * n

    """
            We are using queue.sort() here to be sure that we direct customer to the till with the lowest waiting time.
            So if we will have the customers = [2,3,10] and n = 2 we will have:
            queue = [0] * n = [0, 0]
            1st step:
            queue[0] += customer[0] ( 2 )
            queue = [2, 0]
            queue.sort()
            queue = [0, 2]

            2nd step:
            queue[0] += customer[1] ( 3 )
            queue = [3, 2]
            queue.sort()
            queue = [2, 3]

            3d final step:
            queue[0] += customer[2] ( 10 )
            queue = [12, 3]
            queue.sort()
            queue = [3, 12]

            So this approach with sorting the values inside queue list allows us to add new values at index 0, 
            because after sorting, the value at index 0 will be the minimum
            """

    for customer in customers:
        queue[0] += customer
        queue.sort()

    return max(queue)
