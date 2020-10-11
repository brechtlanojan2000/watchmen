const stepper = new mdb.Stepper(document.getElementById('stepper-form-user'));

document.getElementById('next-step').addEventListener('click', () => {
    stepper.nextStep();
});

document.getElementById('prev-step').addEventListener('click', () => {
    stepper.previousStep();
});