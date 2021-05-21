PARSER_DESCRIPTION = 'Analysis students and rooms'
ROOMS_PATH_HELP_MESSAGE = 'Rooms file path'
STUDENTS_PATH_HELP_MESSAGE = 'Students file path'
OUTPUT_FORMAT_HELP_MESSAGE = 'Enter 1-JSON or 2-XML for file output format'

create_table_rooms = ''' CREATE TABLE if NOT EXISTS Rooms(
    id INTEGER PRIMARY KEY,
    name VARCHAR(5) NOT NULL
    '''
create_table_students = ''' CREATE TABLE if NOT EXISTS Students(
    id INTEGER PRIMARY KEY,
    name VARCHAR(46) NOT NULL, 
    birthday DATETIME, 
    room_id INTEGER NOT NULL FOREIGN KEY REFERENCES Rooms(id)),
    sex VARCHAR(1),
    '''