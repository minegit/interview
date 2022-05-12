class ConferenceRoom:
    _building = None
    _floor = None
    _cid = None
    _booking_slot = None

    def __init__(self, building_name=None,  floor_name=None, cid=None) -> None:
        self._building = building_name.upper()
        self._floor = floor_name.upper()
        self._cid = cid.upper()

    @property
    def building(self):
        return self._building

    @property
    def floor(self):
        return self._floor

    @property
    def cid(self):
        return self._cid

    @property
    def booking_slot(self):
        return self._booking_slot






    
    


