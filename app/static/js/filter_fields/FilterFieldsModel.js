export class FilterFieldsModel{
    constructor(els){
        this._els = els
        this._data = {}
        for(let [ k, v ] of Object.entries(this._els)){
            this._data[k] = this._getJson(v.textContent)
        }
    }

    _getJson(txt){
        let textarea = document.createElement("textarea")
        textarea.innerHTML = txt
        let value = textarea.value
        textarea.remove()
        textarea = null
        return JSON.parse(value)
    }

    getDataFor(key){
        return this._data[key] || []
    }
}
