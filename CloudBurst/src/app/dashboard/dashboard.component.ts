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
    temperature: 0,
    humidity: 0,
    windSpeed: 0,
    precipitation: 0,
    pressure: 0,
  };
  prediction: string = '';

  constructor(private cloudburstService: CloudburstService) {}

  predictCloudburst() {
    this.cloudburstService.predictCloudburst(this.formData).subscribe((response: any) => {
      this.prediction = response.prediction;
    });
  }
}
