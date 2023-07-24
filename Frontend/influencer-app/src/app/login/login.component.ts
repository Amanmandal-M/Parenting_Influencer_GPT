import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import Swal from 'sweetalert2'; // Import Swal class
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {
  loginForm: FormGroup = new FormGroup({});
  isLoading: boolean = false;

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
    });
  }

  onSubmit() {
    if (this.loginForm.invalid) {
      return;
    }

    this.isLoading = true;
    const userData = this.loginForm.value;
    // Replace the API endpoint with your actual backend URL
    const apiUrl =
      'https://parenting-influencer-backend.onrender.com/user/login';

    this.http.post(apiUrl, userData).subscribe(
      (response: any) => {
        this.isLoading = false;
        response.Data = JSON.parse(response.Data)

        // Save the user data in session storage
        sessionStorage.setItem('userData', JSON.stringify(response));

        // Show success alert
        this.showSuccessAlert();

        // Navigate to the home page
        this.router.navigateByUrl('/home');
      },
      (error) => {
        this.isLoading = false;
        if (error.status === 401) {
          this.showUserNotFoundAlert(); // Call the user not found alert method
        this.router.navigateByUrl('/signup');
        } else {
          this.showErrorAlert(); // Call the general error alert method
        }
      }
    );
  }

  // Method to show success alert
  showSuccessAlert() {
    Swal.fire({
      icon: 'success',
      title: 'Success!',
      width: '25%',
      text: 'Login successful!',
      timer: 2000, // Auto close the alert after 2.5 seconds
      showConfirmButton: false,
    });
  }

  // Method to show error alert for user not found
  showUserNotFoundAlert() {
    Swal.fire({
      icon: 'error',
      title: 'User Not Found',
      width: '25%',
      text: 'User not found. Please sign up first!',
      timer: 2500, // Auto close the alert after 2.5 seconds
      showConfirmButton: false,
    }).then(() => {
      // Navigate to the signup page
      this.router.navigateByUrl('/signup');
    });
  }

  // Method to show general error alert
  showErrorAlert() {
    Swal.fire({
      icon: 'error',
      title: 'Error!',
      width: '25%',
      text: 'Login failed. Please check your email and password.',
      timer: 2500, // Auto close the alert after 2.5 seconds
      showConfirmButton: false,
    });
  }
}
