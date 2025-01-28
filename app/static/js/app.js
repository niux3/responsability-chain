import { AddFieldsController } from './add_fields/AddFieldsController.js'


(()=>{
    let addFieldsController = new AddFieldsController()
    let fieldsets = document.querySelectorAll('.addRows'),
        addFields = (fieldset, groups) => { 
            fieldset.insertAdjacentHTML("beforeend", groups[groups.length - 1].outerHTML) 
        },
        removeFields = target => target.closest('.group').remove(),
        changeButton = groups =>{
            groups.forEach((group, i) =>{
                if(i !== groups.length - 1){
                    let button = group.querySelector('.button')
                    button.classList.remove('add', 'primary')
                    button.classList.add('remove', 'alert')
                    button.textContent = "supprimer"
                }
            })
        },
        changeName = fieldset =>{
            fieldset.querySelectorAll('.group').forEach((g, indexGroup)=>{
                let names = ["field", "field_filter", "field_value", "date", "date_filter", "date_begin", "date_end"]
                names.map(n => g.querySelector(`*[name^="${n}"]`)).forEach((input, indexField) => { 
                    if(input !== null){
                        input.name = `${names[indexField]}_${indexGroup}`
                        input.id = `${names[indexField]}_${indexGroup}`
                    }
                })
            })
        }

    fieldsets.forEach(( fieldset, i ) =>{
        let groups = fieldset.querySelectorAll('.group'),
            tplButton = `
            <div class="cell medium-3 flex-container align-bottom">
                <button type="button" class="add button primary expanded">ajouter</button>
            </div>`

        groups[groups.length - 1].insertAdjacentHTML('beforeend', tplButton)
        fieldset.addEventListener('pointerdown', e =>{
            if(['add', 'remove'].some(n => e.target.classList.contains('add')) && e.target.nodeName.toLowerCase() === 'button'){
                e.preventDefault()
                if(e.target.classList.contains('add') && e.target.nodeName.toLowerCase() === 'button'){
                    addFields(fieldset, groups)
                }
                groups = fieldset.querySelectorAll('.group')
                if(e.target.classList.contains('remove') && e.target.nodeName.toLowerCase() === 'button'){
                    removeFields(e.target)
                }
                changeButton(groups)
                changeName(fieldset)
            }
        })
    })
})()
