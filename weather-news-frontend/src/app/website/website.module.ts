import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { WebsiteRoutingModule } from "./landing-page/website-routing.module";
import { SearchComponent } from './search/search.component';
import { WeatherDetailsComponent } from './weather-details/weather-details.component';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';



@NgModule({
  declarations: [
    LandingPageComponent,
    SearchComponent,
    WeatherDetailsComponent
  ],
  imports: [
    CommonModule,
    WebsiteRoutingModule,
    MatGridListModule,
    MatInputModule,
    MatButtonModule,
    MatCardModule
  ]
})
export class WebsiteModule { }
