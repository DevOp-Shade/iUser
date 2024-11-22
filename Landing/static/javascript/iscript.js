import {
    iLogin,
    iCore,
    imain,
    imainClips,
    imainFeed,
    imainHome,
    imainPortfolio,
    imainShop

} from './iapp';


const firstName = document.getElementById('firstName')
const lastName = document.getElementById('lastName')
const email = document.getElementById('email')
const password = document.getElementById('password')
const form = document.getElementById('form')
const errorElement = document.getElementById('error')

function registrationOfOwner(firstName, lastName, email,
                            password, form, errorElement
    ) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.password = password;
        this.form = form;
        this.errorElement = errorElement;

        this.formValidation = function(){
            console.log(`User\'s Input Name, First: ${this.firstName}`);
            console.log(`User\'s Input Name, Last: ${this.lastName}`);
            console.log(`Title email: ${this.email}`);
            console.log(`Pass Key: ${this.password}`);

        } 
    }

    registrationOfOwner.addEventListener('click', e => {
        console.log(e);
    })