import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import Swal from 'sweetalert2'; // Import Swal class
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss'],
})
export class SignupComponent implements OnInit {
  signupForm: FormGroup = new FormGroup({});
  isLoading: boolean = false;

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.signupForm = this.formBuilder.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      gender: ['Select Gender', Validators.required],
      location: ['', Validators.required],
      country: ['', Validators.required],
    });
  }

  async onSubmit() {
    if (this.signupForm.invalid) {
      return;
    }

    this.isLoading = true;
    const userData = this.signupForm.value;
    // Replace the API endpoint with your actual backend URL
    const apiUrl =
      'https://parenting-influencer-backend.onrender.com/user/register';

    this.http.post(apiUrl, userData).subscribe(
      (response: any) => {
        this.isLoading = false;
        this.signupForm.reset();
        this.showSuccessAlert(); // Call the success alert method
        this.router.navigateByUrl('/login'); // Navigate to the login page after successful registration
      },
      (error) => {
        this.isLoading = false;
        if (error.status === 401) {
          this.showUserExistsAlert(); // Call the user already exists alert method
          this.router.navigateByUrl('/login');
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
      text: 'User registration successful!',
      timer: 2500, // Auto close the alert after 2 seconds
      showConfirmButton: false,
    });
  }

  // Method to show error alert for user already registered
  showUserExistsAlert() {
    Swal.fire({
      icon: 'error',
      title: 'Please Login',
      width: '25%',
      text: 'User is already registered!',
      timer: 2500, // Auto close the alert after 2 seconds
      showConfirmButton: false,
    });
  }

  // Method to show general error alert
  showErrorAlert() {
    Swal.fire({
      icon: 'error',
      title: 'Error!',
      width: '25%',
      text: 'User registration failed!',
      timer: 2500, // Auto close the alert after 2 seconds
      showConfirmButton: false,
    });
  }
}
