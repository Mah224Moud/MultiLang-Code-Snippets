/**
 * Checks if the provided email is valid.
 *
 * @param {string} email - The email to be validated.
 * @return {boolean} Returns true if the email is valid, otherwise false.
 */
function is_valid(email){
    let pattern = new RegExp("^[a-z][a-z\\d\\-\\.]{5,}[a-z\\d]@[a-z\\-]+[a-z\\d]{2,}\\.[a-z]{2,}$");
    return email.match(pattern) && !email.includes("..");
}

let emails = [
    "lesmouttesttest@gmail.com",
    "validemailtest@gmail.com",
    "emailtest123@test.com",
    "123email@gmail.com",
    "other-email@gmail.com",
    "anotherEmail@test.com",
    "myemail-@test.com",
    "MyEmail@test.com",
    "myemail@test.com",
    "invalid.email@example",
    "space email@example.com",
    "underscore_email@example.com",
    "double..dots@example.com",
    "-dashstart@example.com",
    "dotend@example.com.",
    "email@subdomain.domain.com",
    "email@sub-domain.com",
    "email@domain.c",
    "email@domain.12",
    "ema il@domain.com",
    "email@do_main.com"
];

let valid = {}
let invalid = {}
emails.forEach(email => {
    if(is_valid(email)){
        valid[email] = true
    }else{
        invalid[email] = true
    }
})

console.log("Here are the list of valid emails:");
console.log(valid)
console.log("\nHere are the list of invalid emails:");
console.log(invalid)