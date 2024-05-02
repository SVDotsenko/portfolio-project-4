const validateInput = () => {
    const input = document.getElementById('name');
    const button = document.getElementById('submit');
    setTimeout(() => input.classList.remove('is-invalid', 'is-valid'), 3000);
    if (/[a-zA-Z]/.test(input.value)) {
        input.classList.remove('is-invalid');
        input.classList.add('is-valid');
        button.disabled = false;
    } else {
        input.classList.remove('is-valid');
        input.classList.add('is-invalid');
        button.disabled = true;
    }
}

const previewImage = event => {
    const reader = new FileReader();
    reader.onload = () => document.getElementById('preview').src = reader.result;
    reader.readAsDataURL(event.target.files[0]);

    const submit = document.getElementById('submit');

    Toast.params.message = "To save, click Update button";
    Toast.params.messageTags = "warning";
    Toast.params.delay = 3;
    Toast.show();

    setTimeout(() => {
        submit.classList.remove('btn-primary');
        submit.classList.add('btn-warning');
        submit.focus();
    }, 3500);
}

(typeof module !== 'undefined' && module.exports) && (module.exports = {validateInput, previewImage});