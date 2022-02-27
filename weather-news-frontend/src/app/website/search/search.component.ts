import {Component, OnDestroy, OnInit} from '@angular/core';
import {FormControl, Validators} from "@angular/forms";
import {HttpService} from "../../core/services/http.service";
import {Subscription} from "rxjs";

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit, OnDestroy {

  Subscriptions =  new Subscription();
  cityForm = new FormControl('', [Validators.required, Validators.minLength(2),
                              Validators.maxLength(20)])

  constructor(private http: HttpService) { }

  ngOnInit(): void {
  }

  getWeatherAndNews(): void {
    this.Subscriptions.add(this.http.getWeather(this.cityForm.value).subscribe( weather =>
      console.log(weather)
    ))
    this.Subscriptions.add(this.http.getNews(this.cityForm.value).subscribe(news => {
      console.log(news)
    }))
  }

  ngOnDestroy(): void {
    this.Subscriptions.unsubscribe()
  }
}
