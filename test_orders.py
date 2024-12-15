from sender_stand_request import post_new_order, get_order


def test_searth_order_by_track():
    create_respons = post_new_order()
    track = create_respons.json()["track"]
    get_respons = get_order(track)
    assert get_respons.status_code==200



