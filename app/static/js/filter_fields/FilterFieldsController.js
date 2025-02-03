import { FilterFieldsModel } from './FilterFieldsModel.js'
import { FilterFieldsView } from './FilterFieldsView.js'
import { TemplateEngine } from '../TemplateEngine.js'


export class FilterFieldsController{
    constructor(indexRow=0){
        let dataNodes = {
            'fields': document.getElementById('dataFields'),
            'comparatorNormal': document.getElementById('dataComparatorNormal'),
            'comparatorDate': document.getElementById('dataComparatorDate')
        }
        this._indexRow = indexRow
        this._model = new FilterFieldsModel(dataNodes)
        this._view = new FilterFieldsView(...[
            document.getElementById(`field_${indexRow}`),
            document.getElementById(`field_filter_${indexRow}`),
            document.getElementById(`dynamic_inputs_${indexRow}`)
        ])
        this._engine = new TemplateEngine()

        this._view.selectPrimary.addEventListener('change', this._onPrimaryChange.bind(this))
    }

    _onPrimaryChange(e){
        let [ key, value ] = e.target.value.split('_'),
            translate = {
                'company': 'société',
                'user': 'employé'
            },
            dataFields = this._model.getDataFor('fields'),
            suffixKeyData = 'Normal',
            template = null,
            idTpl = null,
            dataTpl = null
        value = parseInt(value, 10)

        switch(key){
            case 'company':
                suffixKeyData = [1, 2].some(t => value === t)? 'Date' : 'Normal'
                console.log([1, 2].some(t => value === t))
                break
            case 'user':
                suffixKeyData = [12, 13, 14].some(t => value === t)? 'Date' : 'Normal'
                break
        }
        //let value = parseInt(e.target.value, 10),
        let data = this._model.getDataFor(`comparator${suffixKeyData}`)
        if(suffixKeyData === 'Normal'){
            idTpl = 'tplInputText'
            dataTpl = {
                'label': 'Valeur',
                'nameInput': `field_value_${this._indexRow}`
            }
        }else{
            idTpl = 'tplDoubleInputText'
            dataTpl = {
                'labelA': 'De',
                'nameInputA': `field_value_from_${this._indexRow}`,
                'labelB': 'À',
                'nameInputB': `field_value_to_${this._indexRow}`,
            }
        }
        template = document.getElementById(idTpl).textContent
        let target = document.querySelector(`*[name="field_${this._indexRow}"]`).closest('.group').querySelector('.dynamicField')
        target.innerHTML = this._engine.render(template, dataTpl)

        this._view.updateSelect(this._view.selectSecondary, data)
    }
}
