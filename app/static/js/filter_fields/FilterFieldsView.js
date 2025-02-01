export class FilterFieldsView {
    constructor(selectPrimary, selectSecondary, inputContainer) {
        this.selectPrimary = selectPrimary
        this.selectSecondary = selectSecondary
        this.inputContainer = inputContainer
    }

    updateSelect(selectElement, options) {
        selectElement.innerHTML = ""

        options.forEach((option, i) => {
            const opt = document.createElement("option")
            opt.value = i
            opt.textContent = option
            selectElement.appendChild(opt)
        })
    }
}
