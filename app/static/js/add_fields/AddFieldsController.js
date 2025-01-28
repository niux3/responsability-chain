import { AddFieldsModel } from './AddFieldsModel.js'
import { AddFieldsView } from './AddFieldsView.js'


export class AddFieldsController{
    constructor(){
        let dataNodes = {
            'fields': document.getElementById('dataFields'),
            'comparatorNormal': document.getElementById('dataComparatorNormal'),
            'comparatorDate': document.getElementById('dataComparatorDate')
        }
        this._model = new AddFieldsModel(dataNodes)
        this._view = new AddFieldsView(document.getElementById('field_0'), document.getElementById('field_filter_0'))

        this._view.selectPrimary.addEventListener('change', this._onPrimaryChange.bind(this))
    }

    _onPrimaryChange(e){
        let value = parseInt(e.target.value, 10),
            dataFields = this._model.getDataFor('fields'),
            suffixKeyData = ['created', 'updated', 'birthday'].some(t => dataFields[value] === t)? 'Date': 'Normal',
            data = this._model.getDataFor(`comparator${suffixKeyData}`)
        this._view.updateSelect(this._view.selectSecondary, data)
    }
}
