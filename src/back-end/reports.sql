create table reports
(
  camera_id integer,
  date text,
  time text,
  detection_type text
);

insert into reports (camera_id, date, time, detection_type) VALUES (1, '4/7/22', '7:00', 'motion');
insert into reports (camera_id, date, time, detection_type) VALUES (1, '4/8/22', '7:00', 'motion');
insert into reports (camera_id, date, time, detection_type) VALUES (1, '4/8/22', '8:00', 'motion');
insert into reports (camera_id, date, time, detection_type) VALUES (1, '4/9/22', '8:00', 'motion');
insert into reports (camera_id, date, time, detection_type) VALUES (1, '4/11/22', '9:00', 'motion');
insert into reports (camera_id, date, time, detection_type) VALUES (2, '4/7/22', '17:00', 'facial');
insert into reports (camera_id, date, time, detection_type) VALUES (2, '4/8/22', '17:00', 'facial');
insert into reports (camera_id, date, time, detection_type) VALUES (2, '4/8/22', '18:00', 'facial');
insert into reports (camera_id, date, time, detection_type) VALUES (2, '4/9/22', '18:00', 'facial');
insert into reports (camera_id, date, time, detection_type) VALUES (2, '4/11/22', '19:00', 'facial');