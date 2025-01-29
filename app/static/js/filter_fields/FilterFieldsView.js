export class FilterFieldsView {
    constructor(selectPrimary, selectSecondary, inputContainer) {
        this.selectPrimary = selectPrimary
        this.selectSecondary = selectSecondary
        this.inputContainer = inputContainer
    }

    updateSelect(selectElement, options) {
        selectElement.innerHTML = ""

        options.forEach((option) => {
            const opt = document.createElement("option")
            opt.value = option
            opt.textContent = option
            selectElement.appendChild(opt)
        })
    }
}
