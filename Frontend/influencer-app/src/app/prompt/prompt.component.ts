import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';

interface ChatMessage {
  question: string;
  convertedCode: string;
}

@Component({
  selector: 'app-prompt',
  templateUrl: './prompt.component.html',
  styleUrls: ['./prompt.component.scss']
})
export class PromptComponent implements OnInit {
  tokenPresent: boolean = false;
  chatMessages: ChatMessage[] = [];
  userMessage: string = '';

  constructor(
    private http: HttpClient,
    private router: Router
  ) {}

  ngOnInit() {
    // Check if the token is present in session storage
    const userData: any = sessionStorage.getItem('userData');
    const userData2: any = JSON.parse(userData);

    if (userData2 && userData2.Token) {
      // Token is present
      this.tokenPresent = true;

      // Set the headers with Authorization token
      const headers = new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${userData2.Token}`
      });

      // Fetch initial data from /prompt-data route with headers
      this.http.get<any>('https://parenting-influencer-backend.onrender.com/prompt-data', { headers }).subscribe(
        (response) => {
          // Process the response and set the chatMessages array
          if (response && response.data) {
            this.chatMessages = JSON.parse(response.data);
          }
        },
        (error) => {
          console.error('Error fetching initial data:', error);
        }
      );

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
  showSuccessAlert(userData2: any) {
    Swal.fire({
      icon: 'success',
      title: `Welcome to FamilyGuide AI. ${userData2.Data.name}`,
      width: 'auto',
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

  // Method to handle user message submission
  onSendMessage() {
    if (!this.userMessage) {
      return;
    }

    // Prepare the data to be sent to the server
    const userData: any = sessionStorage.getItem('userData');
    const userData2: any = JSON.parse(userData);

    const dataToSend = {
      message: this.userMessage
    };

    // Set the headers with Authorization token
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${userData2.Token}`
    });

    // Post the user message to the server with headers
    this.http.post<any>('https://parenting-influencer-backend.onrender.com/prompt', dataToSend, { headers }).subscribe(
      (response) => {
        // Handle the response if needed
        console.log('Message sent successfully:', response);

        // Update chatMessages with the sent message
        if (response && response.data) {
          console.log(this.chatMessages)
          this.chatMessages.push({
            question: this.userMessage,
            convertedCode: response.data.convertedCode
          });
        }

        // Clear the user input
        this.userMessage = '';
      },
      (error) => {
        console.error('Error sending message:', error);
      }
    );
  }
}
