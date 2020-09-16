/*
498. Parking Lot
https://www.lintcode.com/problem/parking-lot/description?_from=ladder&&fromId=98
*/
#include <utility>
#include <vector>
#include <map>
enum class VehicleSize { Motorcycle, Compact, Large };

class Vehicle {
  // Write your code here
 protected:
  VehicleSize size_;
  int number_of_spot_needed_;

 public:
  std::pair<VehicleSize, int> GetSizeAndNumber() {
    return std::pair<VehicleSize, int>{size_, number_of_spot_needed_};
  }
};

class Bus : public Vehicle {
  // Write your code here
 public:
  Bus() {
    size_ = VehicleSize::Large;
    number_of_spot_needed_ = 5;
  }
};

class Car : public Vehicle {
  // Write your code here
 public:
  Car() {
    size_ = VehicleSize::Compact;
    number_of_spot_needed_ = 1;
  }
};

class Motorcycle : public Vehicle {
  // Write your code here
 public:
  Motorcycle() {
    size_ = VehicleSize::Motorcycle;
    number_of_spot_needed_ = 1;
  }
};

// spot class, indicate spot type, spot_id_ and spottype
class Spot {
 private:
  bool available_;
  int spot_id_;

 public:
  Spot(int spot_id);
  bool IsAvailable();
  void TakeSpot();
  void LeaveSpot();
};

class Row {
 private:
  std::vector<Spot *> spots_;

 public:
  Row(int k) {
    for (int i = 0; i < k; ++i) {
      spots_.push_back(new Spot(k));  // intiailize it with spot_id
    }
  }
  std::vector<Spot *> GetSpots() { return spots_; }
};

class Level {
  // Write your code here
 private:
  std::vector<Row *> rows_;

 public:
  Level(int m, int k) {
    for (int i = 0; i < m; ++i) {
      rows_.push_back(new Row(k));  // initalize each row
    }
  }

  std::vector<Row *> GetRows() { return rows_; }
};

// spot type is initalized interally
Spot::Spot(int spot_id) {
  spot_id_ = spot_id;
  LeaveSpot();
}

bool Spot::IsAvailable() { return available_; }

void Spot::TakeSpot() { available_ = false; }

void Spot::LeaveSpot() { available_ = true; }

// generate a ticket given spots occupied and vehicle
class Ticket {
 private:
  vector<Spot *> spots_;
  Vehicle *v_;

 public:
  Ticket(Vehicle *v, std::vector<Spot *> spots) {
    v_ = v;
    spots_ = spots;
  }
  vector<Spot *> GetSpots() { return spots_; }
};

class ParkingLot {
 private:
  std::vector<Level *> levels_;
  std::map<Vehicle *, Ticket *> vehicle_ticket_;
  std::vector<Spot *> FindSpotForVehicle(Vehicle *v);
  int spots_per_row_;

 public:
  // @param n number of leves
  // @param num_rows  each level has num_rows rows of spots
  // @param spots_per_row each row has spots_per_row spots
  ParkingLot(int n, int num_rows, int spots_per_row) {
    // Write your code here
    // create parking lot
    spots_per_row_ = spots_per_row;
    for (int i = 0; i < n; ++i) {
      levels_.push_back(new Level(num_rows, spots_per_row));
    }
  }

  // Park the vehicle in a spot (or multiple spots)
  // Return false if failed
  bool parkVehicle(Vehicle *vehicle) {
    // Write your code here
    std::vector<Spot *> spots = FindSpotForVehicle(vehicle);
    if (spots.empty()) {
      return false;
    }
    Ticket *t = new Ticket(vehicle, spots);
    vehicle_ticket_[vehicle] = t;
    return true;
  }

  // unPark the vehicle
  void unParkVehicle(Vehicle *vehicle) {
    // Write your code here
    auto loc = vehicle_ticket_.find(vehicle);
    if (loc == vehicle_ticket_.end()) {
      return;
    }
    std::vector<Spot *> spots = vehicle_ticket_[vehicle]->GetSpots();
    for (auto spot : spots) {
      spot->LeaveSpot();
    }
    vehicle_ticket_.erase(vehicle);
  }
};

std::vector<Spot *> ParkingLot::FindSpotForVehicle(Vehicle *v) {
  std::pair<VehicleSize, int> requirement = v->GetSizeAndNumber();
  std::vector<Spot *> occupied_spots;

  int start = 0;
  switch (requirement.first) {
    case VehicleSize::Compact:
      start = spots_per_row_ / 4;
      break;
    case VehicleSize::Motorcycle:
      start = 0;
      break;
    case VehicleSize::Large:
      start = spots_per_row_ / 4 * 3;
      break;
  }

  for (auto level : levels_) {
    for (auto row : level->GetRows()) {
      // std::cout << "start: " << start << "how many: " << requirement.second
      // << std::endl;
      for (int i = start; i < spots_per_row_ - requirement.second + 1; ++i) {
        bool can_park = true;
        for (int j = i; j < i + requirement.second; ++j) {
          // std::cout << "level: " << &level << "row: " << &row << "j: " << j
          // << "Avalability: " << row->GetSpots()[j]->IsAvailable() <<
          // std::endl;
          if (!row->GetSpots()[j]->IsAvailable()) {
            can_park = false;
            break;
          }
        }
        if (can_park) {
          for (int j = i; j < i + requirement.second; ++j) {
            row->GetSpots()[j]->TakeSpot();
            occupied_spots.push_back(row->GetSpots()[j]);
          }
          return occupied_spots;
        }
      }
    }
  }
  return occupied_spots;
}
