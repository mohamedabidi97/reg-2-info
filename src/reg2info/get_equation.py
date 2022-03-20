def reg_equation(model):
    
    def term(coef, power):
        coef = coef if coef != 1 else ''
        power = (f'^{power}') if power > 1 else ''
        return f'{coef}x{power}'
    terms = []
    coefficients = model.coef_
    for power, coef in enumerate(coefficients, start=1):
        if coef != 0:
            terms.append(term(coef, power))
    return 'y = ' + ' + '.join(terms)
