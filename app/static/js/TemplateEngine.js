export class TemplateEngine {
    constructor(template) {
        this.template = template
    }

    render(data) {
        let output = this.template

        // Gestion des conditions if/else if/else
        output = this._processConditions(output, data)

        // Gestion des boucles
        output = this._processLoops(output, data)

        // Remplacement des placeholders simples
        output = this._processPlaceholders(output, data)

        return output
    }

    _processConditions(template, data) {
        // Regex pour capturer les blocs if/else if/else
        let pattern = /\{\{#if (?<ifCondition>\w+)\}\}(?<ifContent>.*?)(\{\{:else if (?<elseIfCondition>\w+)\}\}(?<elseIfContent>.*?))?(\{\{:else\}\}(?<elseContent>.*?))?\{\{\/if\}\}/gs
        return template.replace(pattern, (...args) => {
            args = args[args.length - 1]
            if (data[args.ifCondition]) {
                return args.ifContent
            } else if (data[args.elseIfCondition]) {
                return args.elseIfContent
            } else {
                return args.elseContent
            }
            return null
        })
    }

    _processLoops(template, data) {
        let pattern = /\{\{#each (\w+)\}\}(.*?)\{\{\/each\}\}/gs
        return template.replace(pattern, (match, key, content) => {
            if (data.hasOwnProperty(key) && Array.isArray(data[key])) {
                return data[key].map(item => {
                    return content.replace(/\{\{this\}\}/g, item)
                }).join('')
            }
            return ''
        })
    }

    _processPlaceholders(template, data) {
        return template.replace(/\{\{(\w+)\}\}/g, (match, key) => {
            return data.hasOwnProperty(key) ? data[key] : match
        })
    }
}
