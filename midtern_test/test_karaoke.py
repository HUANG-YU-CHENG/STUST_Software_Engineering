from karaoke import sing
import pytest
@pytest.mark.parametrize("person_count,expect_by_person_total,expect_by_box_total",[
    (2,1073.6,1458.6),
    (2,1073.6,1073.6),#該筆為錯誤資料 其他資料為正確資料
    (3,1610.4,1610.4),
    (4,2147.2,2224.2),
    (5,2684.0,2376.0),
    (8,4294.4,3293.4),
    (12,6441.6,4362.6),
    (15,8052.0,5280.0),
    (20,10736.0,7194.0)
])
def test_sing(person_count,expect_by_person_total,expect_by_box_total):
    test_data = sing(person_count)
    actual_by_person_total = test_data.total_by_person()
    actual_by_box_total = test_data.total_by_box()
    assert actual_by_person_total == expect_by_person_total
    assert actual_by_box_total == expect_by_box_total
    