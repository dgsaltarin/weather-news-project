import {Component, Input, OnInit} from '@angular/core';
import {Weather} from "../../core/models/weather.model";

@Component({
  selector: 'app-weather-details',
  templateUrl: './weather-details.component.html',
  styleUrls: ['./weather-details.component.css']
})
export class WeatherDetailsComponent implements OnInit {

  @Input() weatherInformation?: Weather;

  constructor() { }

  today: number = Date.now()

  ngOnInit(): void {
    if (this.weatherInformation) console.log(this.weatherInformation)
  }

}
