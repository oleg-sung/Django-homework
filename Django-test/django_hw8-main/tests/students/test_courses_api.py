import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    courses = course_factory(_quantity=1)
    course_id = courses[0].id
    response = client.get(f'/api/v1/courses/{course_id}/')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == courses[0].name


@pytest.mark.django_db
def test_get_all_courses(client, course_factory):
    courses = course_factory(_quantity=5)
    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_get_courses_filter_id(client, course_factory):
    courses = course_factory(_quantity=5)
    response = client.get('/api/v1/courses/', data={'id': courses[0].id})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_get_courses_filter_name(client, course_factory):
    courses = course_factory(_quantity=5)
    response = client.get('/api/v1/courses/', data={'name': courses[0].name})
    assert response.status_code == 200
    data = response.json()
    for i, c in enumerate(data):
        assert c['name'] == courses[0].name


@pytest.mark.django_db
def test_post_course_1(client):
    student_1 = Student.objects.create(name='student_1', birth_date='1997-01-01')
    student_2 = Student.objects.create(name='student_1', birth_date='1998-02-02')
    response = client.post('/api/v1/courses/', data={
        'name': 'course_1',
        'students': [student_1.id, student_2.id]
    })
    assert response.status_code == 201


@pytest.mark.django_db
def test_post_course_2(client, student_factory):
    students = student_factory(_quantity=2)
    response = client.post('/api/v1/courses/', data={
        'name': 'course_1',
        'students': [i.id for i in students]
    })
    assert response.status_code == 201


@pytest.mark.django_db
def test_patch_course(client, course_factory):
    student = Student.objects.create(name='student_1', birth_date='1993-01-10')
    course = course_factory(_quantity=1)
    response = client.patch(f'/api/v1/courses/{course[0].id}/', data={
        'students': [student.id]
    })
    assert response.status_code == 200
    data = response.json()
    assert data['students'] == [student.id]


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(_quantity=2)
    response = client.delete(f'/api/v1/courses/{course[0].id}/')
    assert response.status_code == 204


@pytest.mark.parametrize(
    'max_count, students_count, response_status',
    [(20, 25, 400), (20, 15, 201), (20, 20, 201)]
)
@pytest.mark.django_db
def test_max_students(settings,
                      client,
                      course_factory,
                      student_factory,
                      max_count,
                      students_count,
                      response_status):
    settings.MAX_STUDENTS_PER_COURSE = max_count
    students = student_factory(_quantity=students_count)

    response = client.post('/api/v1/courses/', data={
        'name': 'course_1',
        'students': [i.id for i in students]
    })

    assert response.status_code == response_status
