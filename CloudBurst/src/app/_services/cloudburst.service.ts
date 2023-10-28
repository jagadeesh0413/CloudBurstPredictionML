import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CloudburstService {
  private apiUrl = 'http://127.0.0.1:5000/'; 

  constructor(private http: HttpClient) { }

  predictCloudburst(data: any) {
    return this.http.post(`${this.apiUrl}predict`, data);
  }
}
