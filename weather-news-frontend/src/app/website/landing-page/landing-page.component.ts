import { Component, OnInit } from '@angular/core';
import {Weather} from "../../core/models/weather.model";
import {News} from "../../core/models/news.model";

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.css']
})
export class LandingPageComponent implements OnInit {

  thereAreNews: boolean = false
  weatherInformation?: Weather;
  newsInformation?: News[];

  constructor() { }

  ngOnInit(): void {
  }

  shareWeatherInformation(weather: Weather): void {
    this.weatherInformation = weather;
  }

  renderNews(news: News[]): void {
    this.thereAreNews = true;
    this.newsInformation = news;
  }
}
