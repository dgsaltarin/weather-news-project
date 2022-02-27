import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {environment} from "../../../environments/environment";
import {News} from "../models/news.model";
import {catchError, map} from "rxjs/operators";
import {Weather} from "../models/weather.model";

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  URL_API_WEATHER: string = `${environment.API_WEATHER_NEWS_URL}/weather/weather`;
  URL_API_NEWS: string = `${environment.API_WEATHER_NEWS_URL}/news/news`;

  constructor(
    private httpClient: HttpClient
  ) { }

  getWeather(city: string): Observable<Weather> {
    return this.httpClient.get(`${this.URL_API_WEATHER}/${city}`)
      .pipe(
        map((response: any) => response as Weather),
        catchError(err => {throw new Error('Something went wrong with the weather');})
      );
  }

  getNews(city: string): Observable<News[]> {
    return this.httpClient.get(`${this.URL_API_NEWS}/${city}`)
      .pipe(
        map((response: any) => response as News[]),
        catchError(err => {throw new Error('Something went wrong with the news');})
      );
  }
}
