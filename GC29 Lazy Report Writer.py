import random
students = int(input("How many students are there in your class? "))
comments = ["offers constructive suggestions to peers to enhance their work",
            "works democratically with peers",
            "enhances group disccussion through insightful comments",
            "listens attentively to the responses of others",
            "tackles classroom assignments, tasks, and group work in an organized manner",
            "uses free minutes of class time constructively",
            "checks work thoroughly before submitting it",
            "shows intiative and looks for new ways to get involved",
            "takes responsibilty for their learning",
            "exhibits a positive outlook and attitude in the classroom",
            "sets an example of excellence in behavior and cooperation",
            "shows respect for teachers and peers",
            "has incredible self-discipline and always gets work done in a timely manner",
            "preseveres when faced with difficulty by asking questions",
            "is exceptionally organized and is always prepared for the lesson",
            "is patient and kind when working with peers who need extra assistance",
            "is a model student in the classroom",
            "is able to cooperate and work well with any of the other students in the class",
            "expresses ideas clearly, both verblly and through writing",
            "helps to keep the work group focused and on task",
            "treats other students with fairness and understanding",
            "puts forth their best effort into homework assignments",
            "avoids careless errors through attention to detail",
            "exceeds expectations with the quality of their work",
            "seeks responsibilites and follows through",
            "is courteous and shows good manners in the classroom"]
n = 1
for i in range(students):
    choose = random.choice(comments)
    print("Student", n, choose)
    n += 1
