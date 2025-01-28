export class AddFieldsView {
    constructor(selectPrimary, selectSecondary) {
        this.selectPrimary = selectPrimary
        this.selectSecondary = selectSecondary
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
