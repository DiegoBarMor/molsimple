import molsimple as ms

# //////////////////////////////////////////////////////////////////////////////
class Atom:
    def __init__(self, data: str):
        self.idx = data[ms.SERIAL_NUM_START:ms.SERIAL_NUM_END]
        self.name = data[ms.ATOM_NAME_START:ms.ATOM_NAME_END]
        self.altloc = data[ms.ALTLOC_START:ms.ALTLOC_END]
        self.xpos = data[ms.X_COORDINATES_START:ms.X_COORDINATES_END]
        self.ypos = data[ms.Y_COORDINATES_START:ms.Y_COORDINATES_END]
        self.zpos = data[ms.Z_COORDINATES_START:ms.Z_COORDINATES_END]
        self.occupancy = data[ms.OCCUPANCY_START:ms.OCCUPANCY_END]
        self.temp_factor = data[ms.TEMPERATURE_FACTOR_START:ms.TEMPERATURE_FACTOR_END]
        self.element = data[ms.ELEMENT_SYMBOL_START:ms.ELEMENT_SYMBOL_END]
        self.charge = data[ms.CHARGE_START:ms.CHARGE_END]


# //////////////////////////////////////////////////////////////////////////////
