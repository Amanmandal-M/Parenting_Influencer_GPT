import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-prompt',
  templateUrl: './prompt.component.html',
  styleUrls: ['./prompt.component.scss']
})
export class PromptComponent implements OnInit {
  tokenPresent: boolean = false;

  constructor(
    private http: HttpClient,
    private router: Router
  ) {}

  ngOnInit() {
    // Check if the token is present in session storage
    const userData:any = sessionStorage.getItem('userData');
    const userData2:any = JSON.parse(userData);

    if (userData2 && userData2.Token) {
      // Token is present
      this.tokenPresent = true;

      // Check if success message is already shown
      const successMessageShown = sessionStorage.getItem('successMessageShown');

      if (!successMessageShown) {
        // Show the success alert
        this.showSuccessAlert(userData2);

        // Set the flag to indicate that the success message has been shown
        sessionStorage.setItem('successMessageShown', 'true');
      }
    } else {
      // Token is not present, show the error alert
      this.showErrorAlert();
    }
  }

  // Method to show success alert
  showSuccessAlert(userData2:any) {
    Swal.fire({
      icon: 'success',
      title: 'Welcome!',
      width: 'auto',
      text: `Welcome to FamilyGuide AI. ${userData2.Data.name}`,
      timer: 2500, // Auto close the alert after 2.5 seconds
      showConfirmButton: false,
    });
  }

  // Method to show error alert
  showErrorAlert() {
    Swal.fire({
      icon: 'warning',
      title: 'Warning!',
      width: '25%',
      text: 'Please login first.',
      timer: 2500, // Auto close the alert after 2.5 seconds
      showConfirmButton: false,
    }).then(() => {
      this.router.navigateByUrl('/login');
    });
  }
}
