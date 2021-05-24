function getChange(price, tender) {
    const changeNeeded = _toCurrencyRepr(tender) - _toCurrencyRepr(price)
    const register = _toCurrencyRepr([100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01])
    const change = {}

    accumulateChange(changeNeeded, register, change)

    return _fromCurrencyRepr(change)
}

function accumulateChange(changeNeeded, [currentDenomination, ...rest], change = {}) { 
    if (changeNeeded <= 0 || currentDenomination == undefined) {
        return;
    }

    if (currentDenomination > changeNeeded) {
        accumulateChange(changeNeeded, rest, change)
        return;
    }

    const numOfDenominationUsed = Math.floor(changeNeeded / currentDenomination)
    const remainder = changeNeeded - (currentDenomination * numOfDenominationUsed)

    change[currentDenomination] = numOfDenominationUsed
    accumulateChange(remainder, rest, change)
}

function _toCurrencyRepr(amount) {
    if (typeof amount == 'number') {
        return Math.round(amount * 100)
    }
    
    if (Array.isArray(amount)) {
        return amount.map(x => _toCurrencyRepr(x))
    }
    
    return undefined
}

function _fromCurrencyRepr(amount) {
    if (typeof amount == 'number') {
        return amount / 100
    }
    
    if (Array.isArray(amount)) {
        return amount.map(x => _fromCurrencyRepr(x))
    }

    if (typeof amount == 'object') {
        const newAmounts = {}
        Object.keys(amount).forEach(key => {
            const newKey = _fromCurrencyRepr(parseInt(key))
            newAmounts[newKey] = amount[key]
        });
        return newAmounts
    }
    
    return undefined
}

const price = 12.47
const tender = 100.
const change = getChange(price, tender)

for (key of Object.keys(change).sort((a, b) => parseFloat(b) - parseFloat(a))) {
    console.log(`${key} --> ${change[key]}`)
}
