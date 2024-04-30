const Toast = {
    messageTagsMapping: {
        debug: 'text-bg-secondary',
        info: 'text-bg-info',
        success: 'text-bg-success',
        warning: 'text-bg-warning',
        error: 'text-bg-danger'
    },

    params: {
        messageTags: 'info',
        message: 'Hello, world!',
        delay: 4,
        autoHide: true
    },

    paramsToFunction: {
        messageTags: messageTag => Toast.setColor(Toast.messageTagsMapping[messageTag]),
        message: newMessage => Toast.setMessage(newMessage)
    },

    setMessage: message => Toast.element.querySelector('.toast-body').innerText = message,

    removePreviousColorClass: () => Array.from(Toast.element.classList).forEach(className =>
        className.startsWith('text-bg-') && Toast.element.classList.remove(className)),

    setColor: newClass => {
        Toast.removePreviousColorClass();
        Toast.element.classList.add(newClass);
    },

    processParameters: (o, f) => Object.keys(f).forEach(k => f[k](o[k])),

    show: newParams => {
        Toast.params = {...Toast.params, ...newParams};
        Toast.processParameters(Toast.params, Toast.paramsToFunction);

        new bootstrap.Toast(Toast.element, {
            animation: true,
            autohide: Toast.params.autoHide,
            delay: Toast.params.delay * 1000
        }).show();
    }
};