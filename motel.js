const MotelCustomer = {
    name: "Jack Morris",
    birthDate: new Date(2002, 10, 3),
    gender: "Male",
    paymentMethod: "Debit Card",
    roomPrefrences: ["King Bed", "Pet friendly",],
    mailingAddress: {
        street: "16 Eastmeadows Ave",
        city: "St. John's",
        province: "Newfoundland and Labrador",
        country: "Canada",
        postalCode: "A1A3M4",
    },
    phoneNumber: "709-765-6155",

    checkInDate: new Date(2024, 3, 11), 
    checkOutDate: new Date(2024, 3, 21), 


    // method to calculate age
    calcAge: function() {
        const today = new Date(); 
        let age = today.getFullYear() - this.birthDate.getFullYear(); 
        return age; 
    },

    // method to calculate how long stayed at motel
    calcDurationAtMotel: function() {
        const millisecondsPerDay = 1000 * 60 * 60 * 24;
        const checkIn = new Date(this.checkInDate);
        const checkOut = new Date(this.checkOutDate);
        const duration = Math.abs(checkOut - checkIn);
        return Math.ceil(duration / millisecondsPerDay);
    },
};
// list for console
document.addEventListener("DOMContentLoaded", function () {
    const custInformation =`
    Name: ${MotelCustomer.name}
    Phone Number: ${MotelCustomer.phoneNumber}
    Gender: ${MotelCustomer.gender}
    Age: ${MotelCustomer.calcAge()}
    Room Preferences: ${MotelCustomer.roomPrefrences.join(", ")}
    Payment Method: ${MotelCustomer.paymentMethod}
    Mailing Address: ${MotelCustomer.mailingAddress.street}, ${MotelCustomer.mailingAddress.city}, ${MotelCustomer.mailingAddress.province}, ${MotelCustomer.mailingAddress.country}, ${MotelCustomer.mailingAddress.postalCode}
    Check In Date: ${MotelCustomer.checkInDate.toDateString()}
    Check Out Date: ${MotelCustomer.checkOutDate.toDateString()}
    Duration of Stay: ${MotelCustomer.calcDurationAtMotel()} days
    `;

const customerDescription = `Hello! I'm ${
    MotelCustomer.name
    }, a ${MotelCustomer.calcAge()} year old ${
    MotelCustomer.gender
    } who prefers rooms with ${MotelCustomer.roomPrefrences.join(
    " and "
    )}. You can reach me at ${
    MotelCustomer.phoneNumber
    }. I'll be staying from ${MotelCustomer.checkInDate.toDateString()} to ${MotelCustomer.checkOutDate.toDateString()}, which is a duration of ${MotelCustomer.calcDurationAtMotel()} days.`;
    
    
    console.log(customerDescription);

    console.log(custInformation);

    document.body.innerHTML = custInformation;
});