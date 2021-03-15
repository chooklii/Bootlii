gridTeamCoordinates = {
    0: {
        11: {"x": -3072, "y": -1280 },
        12: {"x": -1024, "y": -1280 },
        13: {"x": 1024,  "y": -1280 },
        14: {"x": 3072,  "y": -1280 },
        21: {"x": -3072, "y": -1280},
        22: {"x": -1024, "y": -1280 },
        23: {"x": 1024,  "y": -1280 },
        24: {"x": 3072,  "y": -1280 },
        31: {"x": -3072, "y": 1280 },
        32: {"x": -1024, "y": 1280 },
        33: {"x": 1024,  "y": 1280 },
        34: {"x": 3072,  "y": 1280 },
        41: {"x": -3072, "y": 3840 },
        42: {"x": -1024, "y": 3840},
        43: {"x": 1024,  "y": 3840 },
        44: {"x": 3072,  "y": 3840 }
    },
    1: {
        11: {"x": 3072,  "y": 3840 },
        12: {"x": 1024,  "y": 3840 },
        13: {"x": -1024, "y": 3840},
        14: {"x": -3072, "y": 3840 },
        21: {"x": 3072,  "y": 1280 },
        22: {"x": 1024,  "y": 1280 },
        23: {"x": -1024, "y": 1280 },
        24: {"x": -3072, "y": 1280 },
        31: {"x": 3072,  "y": -1280 },
        32: {"x": 1024,  "y": -1280 },
        33: {"x": -1024, "y": -1280 },
        34: {"x": -3072, "y": -1280},
        41: {"x": 3072,  "y": -1280 },
        42: {"x": 1024,  "y": -1280 },
        43: {"x": -1024, "y": -1280 },
        44: {"x": -3072, "y": -1280 }
    }
}

gridPositionLogic = {
    11: {
        "backup": 12,
        "defender": 13,
        "emergency": False
    },
    12: {
        "backup": 12,
        "defender": 12,
        "emergency": True
    },
    13: {
        "backup": 13,
        "defender": 13,
        "emergency": True
    },
    14: {
        "backup": 13,
        "defender": 12,
        "emergency": False
    },
    21: {
        "backup": 12,
        "defender": 13,
        "emergency": False
    },
    22: {
        "backup": 12,
        "defender": 13,
        "emergency": False
    },
    23: {
        "backup": 13,
        "defender": 12,
        "emergency": False
    },
    24: {
        "backup": 12,
        "defender": 13,
        "emergency": False
    },
    31: {
        "backup": 22,
        "defender": 13,
        "emergency": False
    },
    32: {
        "backup": 22,
        "defender": 13,
        "emergency": False
    },
    33: {
        "backup": 23,
        "defender": 12,
        "emergency": False
    },
    34: {
        "backup": 23,
        "defender": 12,
        "emergency": False
    },
    41: {
        "backup": 32,
        "defender": 23,
        "emergency": False
    },
    42: {
        "backup": 33,
        "defender": 22,
        "emergency": False
    },
    43: {
        "backup": 32,
        "defender": 13,
        "emergency": False
    },
    44: {
        "backup": 33,
        "defender": 22,
        "emergency": False
    }
}

gridTeamPositions = {
    0: {
        11: 44,
        12: 43,
        13: 42,
        14: 41,
        21: 34,
        22: 33,
        23: 32,
        24: 31,
        31: 24,
        32: 23,
        33: 22,
        34: 21,
        41: 14,
        42: 13,
        43: 12,
        44: 11
    },
    1: {
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        41: 41,
        42: 42,
        43: 43,
        44: 44
    }
}