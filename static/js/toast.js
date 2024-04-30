const Toast = (() => {
    let params = {
        delay: 4,
        autoHide: true,
        messageTags: 'info',
        message: 'Hello, world!'
    };

    const messageTagsMapping = {
        debug: 'text-bg-secondary',
        info: 'text-bg-info',
        success: 'text-bg-success',
        warning: 'text-bg-warning',
        error: 'text-bg-danger'
    };

    const setMessage = message => Toast.element.querySelector('.toast-body').innerText = message;

    const removePreviousColorClass = () => {
        Array.from(Toast.element.classList).forEach(className =>
            className.startsWith('text-bg-') && Toast.element.classList.remove(className)
        );
    };

    const setColor = newClass => {
        removePreviousColorClass();
        Toast.element.classList.add(newClass);
    };

    const paramToFunction = {
        messageTags: messageTag => setColor(messageTagsMapping[messageTag]),
        message: newMessage => setMessage(newMessage)
    };

    const processParameters = (o, f) => Object.keys(f).forEach(k => f[k](o[k]));

    const setElement = element => Toast.element = element;

    return {
        show: newParams => {
            params = {...params, ...newParams};
            processParameters(params, paramToFunction);

            new bootstrap.Toast(Toast.element, {
                animation: true,
                autohide: params.autoHide,
                delay: params.delay * 1000
            }).show();
        },
        setElement
    };
})();