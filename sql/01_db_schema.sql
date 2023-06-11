create table students
(
    id             serial primary key,
    first_name     varchar    not null,
    last_name      varchar    not null,
    birth_date     date       not null,
    gender         varchar(1) not null,
    phone          varchar    not null,
    admission_date date       not null,
    group_id       integer    not null references groups
);

create table teachers
(
    id            serial primary key,
    first_name    varchar(100) not null,
    last_name     varchar(100) not null,
    birth_date    date         not null,
    gender        varchar(1)   not null,
    phone         varchar(20)  not null,
    class_room_id integer      not null references classrooms,
    department_id integer      not null references departments
);
create table courses
(
    id             serial primary key,
    title          varchar(100) not null,
    description    text         not null,
    duration_weeks integer      not null,
    teacher_id     integer      not null references teachers,
    department_id  integer      not null references departments
);
create table groups
(
    id            serial primary key,
    name          varchar not null,
    department_id integer not null references departments
);
create table departments
(
    id         serial primary key,
    name       varchar(255) not null,
    faculty_id integer      not null references faculties
);
create table grades
(
    id          serial primary key,
    student_id  integer  not null references students,
    exam_id     integer  not null references exams,
    grade_value smallint not null,
    date        date     not null
);
create table schedules
(
    id                serial primary key,
    group_id          integer not null references groups,
    course_program_id integer not null not null references course_programs,
    start_date        date    not null,
    end_date          date    not null
);
create table buildings
(
    id          serial primary key,
    name        varchar(100) not null,
    address     varchar(200) not null,
    floors      integer      not null,
    description varchar      not null
);
create table classrooms
(
    id          serial primary key,
    room_number varchar(50)  not null,
    capacity    integer      not null,
    room_type   varchar(100) not null,
    floor       integer      not null,
    building_id integer      not null references buildings
);
create table semesters
(
    id         serial primary key,
    name       varchar(100) not null,
    start_date date         not null,
    end_date   date         not null,
    is_current boolean      not null,
    year       smallint     not null
);
create table faculties
(
    id          serial primary key,
    name        varchar(100) not null,
    address     varchar(200) not null,
    phone       varchar(20)  not null,
    email       varchar      not null,
    description varchar      not null
);
create table exams
(
    id           serial primary key,
    title        varchar(100) not null,
    date_time    timestamp    not null,
    course_id    integer      not null references courses,
    classroom_id integer      not null references classrooms,
    teacher_id   integer      not null references teachers
);
create table assignments
(
    id              serial primary key,
    assignment_name varchar(100) not null,
    description     text         not null,
    issue_date      date         not null,
    due_date        date         not null,
    course_id       integer      not null references courses,
    teacher_id      integer      not null references teachers,
    student_id      integer      not null references students
);

create table course_programs
(
    id          serial primary key,
    course_id   integer not null references courses,
    description text    not null,
    hours       integer not null,
    semester_id integer not null references semesters
);
create table study_plans
(
    id          serial primary key,
    schedule_id integer not null references schedules
);
