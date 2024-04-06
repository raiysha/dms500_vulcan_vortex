# Setting up predefined expected data

exptdata = {
    'dms500': {
        'activeCond': list(range(1, 97)),
        'passiveCond': list(range(97, 193)),
        'stimA_1st': list(range(1, 17)) + list(range(33, 49)) + list(range(65, 81)) + list(range(97, 113)) + list(range(129, 145)) + list(range(161, 177)),
        'stimB_1st': list(range(17, 33)) + list(range(49, 65)) + list(range(81, 97)) + list(range(113, 129)) + list(range(145, 161)) + list(range(177, 193)),
        'stimA_2nd': list(range(1, 13)) + list(range(29, 33)) + list(range(45, 61)) + list(range(65, 73)) + list(range(89, 109)) + list(range(125, 129)) + list(range(141, 157)) + list(range(161, 169)) + list(range(185, 193)),
        'stimB_2nd': list(range(13, 29)) + list(range(33, 45)) + list(range(61, 65)) + list(range(73, 89)) + list(range(109, 125)) + list(range(129, 141)) + list(range(157, 161)) + list(range(169, 185)),
        'expectRepeat': list(range(1, 33)) + list(range(97, 129)),
        'expectAltern': list(range(33, 65)) + list(range(129, 161)),
        'expectEither': list(range(65, 97)) + list(range(161, 193)),
        'actualRepeat': list(range(1, 13)) + list(range(17, 29)) + list(range(45, 49)) + list(range(61, 73)) + list(range(81, 89)) + list(range(97, 109)) + list(range(113, 125)) + list(range(141, 145)) + list(range(157, 169)) + list(range(177, 185)),
        'actualAltern': list(range(13, 17)) + list(range(29, 45)) + list(range(49, 61)) + list(range(73, 81)) + list(range(89, 97)) + list(range(109, 113)) + list(range(125, 141)) + list(range(145, 157)) + list(range(169, 177)) + list(range(185, 193)),
        'stimAstimA_expectRepeat_actualRepeat': list(range(1, 13)) + list(range(97, 109)),
        'stimAstimB_expectRepeat_actualAltern': list(range(13, 17)) + list(range(109, 113)),
        'stimAstimA_expectAltern_actualRepeat': list(range(45, 49)) + list(range(141, 145)),
        'stimAstimB_expectAltern_actualAltern': list(range(33, 45)) + list(range(129, 141)),
        'stimAstimA_expectEither_actualRepeat': list(range(65, 73)) + list(range(161, 169)),
        'stimAstimB_expectEither_actualAltern': list(range(73, 81)) + list(range(169, 177)),
        'stimBstimB_expectRepeat_actualRepeat': list(range(17, 29)) + list(range(113, 125)),
        'stimBstimA_expectRepeat_actualAltern': list(range(29, 33)) + list(range(125, 129)),
        'stimBstimB_expectAltern_actualRepeat': list(range(61, 65)) + list(range(157, 161)),
        'stimBstimA_expectAltern_actualAltern': list(range(49, 61)) + list(range(145, 157)),
        'stimBstimB_expectEither_actualRepeat': list(range(81, 89)) + list(range(177, 185)),
        'stimBstimA_expectEither_actualAltern': list(range(89, 97)) + list(range(185, 193)),
        'expectRepeat_actualRepeat': list(range(1, 13)) + list(range(17, 29)) + list(range(97, 109)) + list(range(113, 125)),
        'expectRepeat_actualAltern': list(range(13, 17)) + list(range(29, 33)) + list(range(109, 113)) + list(range(125, 129)),
        'expectAltern_actualRepeat': list(range(45, 49)) + list(range(61, 65)) + list(range(141, 145)) + list(range(157, 161)),
        'expectAltern_actualAltern': list(range(33, 45)) + list(range(49, 61)) + list(range(129, 141)) + list(range(145, 157)),
        'expectEither_actualRepeat': list(range(65, 73)) + list(range(81, 89)) + list(range(161, 169)) + list(range(177, 185)),
        'expectEither_actualAltern': list(range(73, 81)) + list(range(89, 97)) + list(range(169, 177)) + list(range(185, 193)),
        'currentTrial_left': list(range(7, 15)) + list(range(17, 23)) + list(range(29, 31)) + list(range(33, 39)) + list(range(45, 47)) + list(range(49, 55)) + list(range(61, 63)) + list(range(65, 73)) + list(range(81, 89)) + list(range(97, 103)) + list(range(109, 111)) + list(range(113, 119)) + list(range(125, 127)) + list(range(135, 141)) + list(range(143, 151)) + list(range(157, 159)) + list(range(165, 169)) + list(range(173, 177)) + list(range(181, 185)) + list(range(189, 193)),
        'currentTrial_right': list(range(1, 7)) + list(range(15, 17)) + list(range(23, 29)) + list(range(31, 33)) + list(range(39, 45)) + list(range(47, 49)) + list(range(55, 61)) + list(range(63, 65)) + list(range(73, 81)) + list(range(89, 97)) + list(range(103, 109)) + list(range(111, 113)) + list(range(119, 125)) + list(range(127, 135)) + list(range(141, 143)) + list(range(151, 157)) + list(range(159, 165)) + list(range(169, 173)) + list(range(177, 181)) + list(range(185, 189)),
    }
}


