-- 1. Выбрать всех студентов, обучающихся на курсе "Математика".
-- студент - группа - расписание - программа - курс
select s.id, s.first_name, s.last_name
from students s
         join groups g on s.group_id = g.id
         join schedules on g.id = schedules.group_id
         join course_programs on schedules.course_program_id = course_programs.id
         join courses on course_programs.course_id = courses.id
where courses.title = 'математика';

-- 2. Обновить оценку студента по курсу
-- студенту с id = 555 обновляется оценка за экзамен по курсу id = 111
update grades g
set grade_value = 5
from exams e
where e.id = g.id
  and e.course_id = 111
  and g.student_id = 555;

-- 3. Выбрать всех преподавателей, которые преподают в здании №3.
select t.id, t.first_name, t.last_name
from teachers t
         join classrooms c on c.id = t.class_room_id
         join buildings b on b.id = c.building_id
where b.name = '№3';

-- 4. Удалить задание для самостоятельной работы, которое было создано более года назад.
delete
from assignments
where issue_date < now() - interval '1 year';
-- удаляются все записи, отвечающие условию.
-- если действительно нужна только одна, можно сделать select ... limit 1 Только какой смысл?

-- 5. Добавить новый семестр в учебный год.
insert into semesters (name, start_date, end_date, is_current, year)
values ('осень 2022', '2022-09-01', '2022-12-31', true, 2022);
