import { Component } from '@angular/core';
import { CloudburstService } from '../_services/cloudburst.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  formData: any = {
    date: '',
    temperature: '',
    humidity: '',
    windSpeed: '',
    precipitation: '',
    pressure: '',
  };
  prediction: string = '';

  constructor(private cloudburstService: CloudburstService) {}

  predictCloudburst() {
    this.cloudburstService.predictCloudburst(this.formData).subscribe((response: any) => {
      this.prediction = response.prediction;
    });
  }
}
