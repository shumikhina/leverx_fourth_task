PARSER_DESCRIPTION = 'Analysis students and rooms'
ROOMS_PATH_HELP_MESSAGE = 'Rooms file path'
STUDENTS_PATH_HELP_MESSAGE = 'Students file path'
OUTPUT_FORMAT_HELP_MESSAGE = 'Enter 1-JSON or 2-XML for file output format'

DROP_TABLES = '''
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Rooms;
'''

CREATE_TABLE_ROOMS = '''
CREATE TABLE Rooms(
    id INTEGER,
    name VARCHAR(20) NOT NULL,
    PRIMARY KEY (id));
    '''

CREATE_TABLE_STUDENTS = '''
CREATE TABLE Students(
    birthday DATETIME,
    id INTEGER,
    name VARCHAR(100) NOT NULL, 
    room_id INTEGER NOT NULL,
    sex VARCHAR(1),
    PRIMARY KEY (id),
    FOREIGN KEY (room_id)  REFERENCES Rooms (id));
    '''

CREATE_TABLES_QUERIES = (
    CREATE_TABLE_ROOMS,
    CREATE_TABLE_STUDENTS,
)

INSERT_ROOMS = '''
    INSERT INTO Rooms (id, name)
    VALUES (%s, %s)
    '''

INSERT_STUDENTS = '''
    INSERT INTO Students (birthday, id, name, room_id, sex)
    VALUES (%s, %s, %s, %s, %s)
    '''

ROOMS_WITH_STUDENTS = '''
    SELECT 
        Rooms.id,
        Rooms.name,
        COUNT(Students.room_id)
    FROM Rooms LEFT JOIN Students
    ON rooms.id = students.room_id
    GROUP BY rooms.id
    '''

TOP_ROOMS_MIN = '''
    SELECT 
        Rooms.id,
        Rooms.name,
        FLOOR(AVG((YEAR(CURRENT_DATE) - YEAR(Students.birthday)) - 
        (DATE_FORMAT(CURRENT_DATE, '%m%d') < DATE_FORMAT(Students.birthday, '%m%d')))) AS age
    FROM Rooms
    LEFT JOIN Students
    ON Rooms.id = Students.room_id
    GROUP BY Rooms.id
    ORDER BY age
    LIMIT 5;
    '''


TOP_ROOMS_MAX_DIFF = '''
    SELECT 
        Rooms.id,
        Rooms.name,
        DATEDIFF(MAX(students.birthday), MIN(students.birthday)) AS diff
    FROM Rooms
    LEFT JOIN Students
    ON Rooms.id = Students.room_id
    GROUP BY Rooms.id
    ORDER BY diff
    limit 5;
    '''

ROOMS_WITH_DIFFERENT_SEX = '''
    SELECT
        rooms.id,
        rooms.name,
        count(DISTINCT sex) AS flag
    FROM rooms
    LEFT JOIN students ON rooms.id = students.room_id
    GROUP BY rooms.id
    HAVING flag > 1;
    '''