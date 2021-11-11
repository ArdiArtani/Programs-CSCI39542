"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""

# cleanReg(reg): If reg is coded as passenger 'PAS' or commercial 'COM', return those values. Otherwise, return 'OTHER'.
def cleanReg(reg):
    if(reg == 'PAS' or reg == 'COM'):
        return reg
    else:
        return 'OTHER'

# Return the following for the values of c:
def cleanColor(c):
    result_ = ''
    # 'GRAY': for GY, GRAY, GREY,SILVE, SIL, SL,
    if (c == 'GY') or (c == 'GRAY') or (c == 'GREY') or (c == 'SILVE') or (c == 'SIL') or (c == 'SL'):
        result_ = 'GRAY'
    # 'WHITE': for WH, WHITE,
    elif (c == 'WH') or (c == 'WHITE'):
        result_ = 'WHITE'
    # 'BLACK': for BK, BLACK, BL,
    elif (c == 'BK') or (c == 'BLACK') or (c == 'BL'):
        result_ = 'BLACK'
    # 'BLUE': for BLUE,
    elif (c == 'BLUE'):
        result_ = 'BLUE'
    # 'RED': for RED, RD,
    elif (c == 'RED') or (c == 'RD'):
        result_ = 'RED'
    # 'GREEN': for GR, GREEN,
    elif (c == 'GR') or (c == 'GREEN'):
        result_ = 'GREEN'
    # 'BROWN': for BROWN, TAN,
    elif (c == 'BROWN') or (c == 'TAN'):
        result_ = 'BROWN'
    # 'BROWN': for BROWN, TAN,
    # Otherwise, return 'OTHER'.
    else:
        result_ = 'OTHER'

    return result_
