const validateInput = () => {
    const input = document.getElementById('name');
    const button = document.getElementById('submit');
    setTimeout(() => input.classList.remove('is-invalid', 'is-valid'), 3000);
    if (/[a-zA-Z]/.test(input.value)) {
        input.classList.add('is-valid');
        input.classList.remove('is-invalid');
        button.disabled = false;
    } else {
        input.classList.add('is-invalid');
        input.classList.remove('is-valid');
        button.disabled = true;
    }
}

const previewImage = event => {
    const reader = new FileReader();
    reader.onload = () => document.getElementById('preview').src = reader.result;
    reader.readAsDataURL(event.target.files[0]);

    const submit = document.getElementById('submit');

    const message = "To save, click Update button";
    const messageTags = "warning";
    const delay = 3;
    Toast.show({message, messageTags, delay});

    setTimeout(() => {
        submit.classList.remove('btn-primary');
        submit.classList.add('btn-warning');
        submit.focus();
    }, 3500);
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {validateInput, previewImage};
}