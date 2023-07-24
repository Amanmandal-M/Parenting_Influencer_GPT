import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  loginForm: FormGroup = new FormGroup({}); // Initialize the form group with an empty object
  isLoading: boolean = false;

  constructor(private formBuilder: FormBuilder, private http: HttpClient) { }

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
    const apiUrl = 'http://192.168.1.4:8080/user/login';

    this.http.post(apiUrl, userData).subscribe(
      (response: any) => {
        this.isLoading = false;
        alert('Login successful!');
        this.loginForm.reset();
      },
      (error) => {
        this.isLoading = false;
        alert('Login failed. Please check your email and password.');
      }
    );
  }
}
