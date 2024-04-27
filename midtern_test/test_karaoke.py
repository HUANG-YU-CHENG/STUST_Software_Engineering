from karaoke import sing
import pytest
@pytest.mark.parametrize("person_count,expect_result",[
    (2,"以人數計算較便宜"),
    (3,"以人數計算較便宜"),#該筆為錯誤資料 其他資料為正確資料
    (4,"以人數計算較便宜"),
    (5,"開包廂計算較便宜"),
    (8,"開包廂計算較便宜"),
    (12,"開包廂計算較便宜"),
    (15,"開包廂計算較便宜"),
    (20,"開包廂計算較便宜")
])
def test_sing(person_count,expect_result):
    test_data = sing(person_count)
    actual_result = test_data.compare()
    assert actual_result == expect_result
    