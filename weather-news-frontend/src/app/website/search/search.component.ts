import {Component, EventEmitter, OnDestroy, OnInit, Output} from '@angular/core';
import {FormControl, Validators} from "@angular/forms";
import {HttpService} from "../../core/services/http.service";
import {Subscription} from "rxjs";
import {Weather} from "../../core/models/weather.model";
import {News} from "../../core/models/news.model";

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit, OnDestroy {

  Subscriptions =  new Subscription();
  @Output() weatherInformation: EventEmitter<Weather> = new EventEmitter();
  @Output() newsInformation: EventEmitter<News[]> = new EventEmitter();
  cityForm = new FormControl('', [Validators.required, Validators.minLength(2),
                              Validators.maxLength(20)])

  constructor(private http: HttpService) { }

  ngOnInit(): void {
    this.cityForm.setValue('London');
    this.getWeatherAndNews();
  }

  getWeatherAndNews(): void {
    this.Subscriptions.add(this.http.getWeather(this.cityForm.value).subscribe( weather => {
        this.weatherInformation.emit(weather);
      }, error => {}
    ))
    this.Subscriptions.add(this.http.getNews(this.cityForm.value).subscribe(news => {
      this.newsInformation.emit(news);
    }, error => {}
    ))
  }

  ngOnDestroy(): void {
    this.Subscriptions.unsubscribe()
  }
}
