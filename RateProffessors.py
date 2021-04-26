import ratemyprofessor
import SQLCommands

school = ratemyprofessor.get_school_by_name("University at Buffalo (SUNY Buffalo)")


def updateratings():
    test = list(set(SQLCommands.get_all_prof()))
    for i in test:
        getprofessor = ratemyprofessor.get_professor_by_school_and_name(school, i)
        if getprofessor is not None:
            SQLCommands.update_rating((getprofessor.rating, getprofessor.difficulty, getprofessor.num_ratings, i))

updateratings()

