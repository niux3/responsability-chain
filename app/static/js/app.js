import { FilterFieldsController } from './filter_fields/FilterFieldsController.js'
import { TemplateEngine } from './TemplateEngine.js'


(()=>{
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
            tplButton = document.getElementById('tplButton').textContent,
            filterFieldsControllerList = [],
            resetFilterFieldsControllerList = (groups, filterFieldsControllerList ) =>{
                filterFieldsControllerList = []
                for(let i = 0; i < groups.length; i++){
                    filterFieldsControllerList.push(new FilterFieldsController(i))
                }
            }

        groups[groups.length - 1].insertAdjacentHTML('beforeend', tplButton)
        resetFilterFieldsControllerList(groups, filterFieldsControllerList)

        fieldset.addEventListener('pointerdown', e =>{
            if(e.target.closest('button')){
                let button = e.target.closest('button')
                if(['add', 'remove'].some(n => button.classList.contains(n))){
                    e.preventDefault()
                    if(button.classList.contains('add')){
                        addFields(fieldset, groups)
                    }
                    groups = fieldset.querySelectorAll('.group')
                    if(button.classList.contains('remove')){
                        removeFields(e.target)
                    }

                    // ne pas changer l'ordre des instruction puisque le changement de champs ne peut pas se faire si les champs ne sont pas renommés
                    changeButton(groups)
                    changeName(fieldset)
                    resetFilterFieldsControllerList(groups, filterFieldsControllerList)
                }
            }
        })
    })
})()
