import pytest
import os
import binary


bin_sum_two_data = [
    ('test.bin', [1, 2, 3, 4, 5], 3),
    ('test.bin', [44, 11, 13231123, 4, 35], 55),
    ('test.bin', [0, 0], 0),
    ('test.bin', [41, 392], 433)
]


@pytest.mark.parametrize('data', bin_sum_two_data)
def test_bin_sum_two(data):
    # noinspection PyArgumentList
    try:
        with open(data[0], 'wb') as file:
            for num in data[1]:
                file.write(num.to_bytes(4, byteorder='big', signed=True))
        assert binary.bin_sum_two(data[0]) == data[2]
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(data[0]):
            os.remove(data[0])


find_person_file = 'people.bin'
find_person_data = [
    (3424, 'Иванов Пётр Иванович'),
    (7, 'James Bond'),
    (54353, 'Чичиков Павел Иванович'),
    (11, 'Табуреткин Егор Артемьев'),
    (4, 'Тестович Тест Тестов'),
    (2, '')
]


@pytest.mark.parametrize('data', find_person_data)
def test_find_person(data):
    # noinspection PyArgumentList
    try:
        with open(find_person_file, 'wb') as file:
            file.write(len(find_person_data).to_bytes(4, byteorder='big', signed=True))
            for person in find_person_data:
                p_id = person[0].to_bytes(4, byteorder='big', signed=True)
                p_name = person[1].encode('utf-8')
                name_byte_count = len(p_name).to_bytes(4, byteorder='big', signed=True)
                file.write(p_id)
                file.write(name_byte_count)
                file.write(p_name)
        assert binary.find_person(find_person_file, data[0]) == data[1]
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(find_person_file):
            os.remove(find_person_file)
