import {Location} from "./location.model";
import {Condition} from "./condition.model";

export interface Weather {
  location: Location,
  temp_c: number,
  temp_f: number,
  condition: Condition,
  humidity: number,
  feelslike_c: number,
  feelslike_f: number,
  last_updated: string,
}
