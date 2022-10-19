# Demand and Diversity Calculations
Scripts for calculating diversity and demand for suite of test case scenarios from Baidu Apollo 
ADS running on SLGSVL simulator. 

Note:
- Code assumes file `DataSetfeatures.csv` located in the same directory; check that the row names match those described in the code. 

## Calculations
Diversity and demand calculations follow formulae outlined by Lu et. al [1]. 
<br />
Distance calculations are set to Manhattan by default by can be changed to Euclidean.
<br />
Correlation Analysis uses Spearman's correlation.
<br />
Outlier removal uses IQR method.
<br /><br />
[1] C. Lu, H. Zhang, T. Yue, and S. Ali, “Search-based selection and prioritization of test scenarios for autonomous driving systems,” in International
Symposium on Search Based Software Engineering. Springer, 2021, pp. 41–55.

## Scripts
`main.py`:
- This file calls functions from `preprocessing.y` to pre-process the data from
 `DataSetfeatures.csv`, write to the `diversity_input.csv` and `demand_input.csv` files. 
- Functions are then called from `demand_calculations.py`, and `diversity_calculations.py` 
  which read the data from the input files and compute the relevant calculations before
  writing the results to the `demand_output.csv` and `diversity_output.csv` files respectively.

`speed_demand_fix.py`:
- This file identifies and updates incorrect speed classifications in the 
  `DataSetfeatures.csv` file.
- This should be run only once before `main.py`.

`distance_plotting.py`:
- Calculates and plots the diversity of the scenarios using Manhattan and Euclidean
  distance metrics.
  
`correlation_analysis.py`:
- Calculates Spearmans and Pearsons correlation for data and writes output to 
  `correlation_output_collision_event.xlsx`.

## Features
The following features were extracted or calculated from the SPECTRE dataset:<br />
(original SPECTRE dataset: <a> https://github.com/ssbse2021/SPECTRE </a>)
You can change what features are included in `main.py`
<p>Table 1. Extracted features from dataset </p>

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">scenario feature name</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">feature_ego_acceleration</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_throttle</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_steeringTarget</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_brake</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_steeringRate</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_speed</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_speedCategory</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_speedDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_velocityx</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_velocityy</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_velocityz</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_comVelocity</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_accelerationx</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_accelerationy</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_accelerationz</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_comAcceleration </td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_positionx</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_positiony</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_positionz</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_comPosition</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_operation</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_operationDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_rain</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_rainDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_fog</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_fogDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_wetness</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_wetnessDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_time</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_timeDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_scenarioTrafficLight</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_scenarioTrafficLightDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_trafficLight</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_scenarioSideWalk</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_scenarioSideWalkDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_totalNPCs</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_totalPedestrians</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_totalStaticObstacles</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_totalRoadUsers</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesAverageDistance</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesMaximumDistance</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesMinimumDistance</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_typeObstacleHavingMaximumDistance</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_typeObstacleHavingMinimumDistance</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMaximumDistance</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMinimumDistance</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesAverageSpeed</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesMaximumSpeed</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesMinimumSpeed</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_typeObstacleHavingMaximumSpeed</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_typeObstacleHavingMinimumSpeed</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMaximumSpeed</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMinimumSpeed</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ObstaclesAverageVelocity</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ObstaclesMaximumVelocity</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ObstaclesMinimumVelocity</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_typeObstacleHavingMaximumVelocity</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_typeObstacleHavingMinimumVelocity</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMaximumVelocity</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMinimumVelocity</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesAverageAcceleration</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesMaximumAcceleration</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesMinimumAcceleration</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_typeObstacleHavingMaximumAcceleration</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_typeObstacleHavingMinimumAcceleration</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMaximumAcceleration</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMinimumAcceleration</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesAverageVolume</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesMaximumVolume</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesMinimumVolume</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_typeObstacleHavingMaximumVolume</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_typeObstacleHavingMinimumVolume</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMaximumVolume</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMinimumVolume</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_volumeObstacleWithMinimumDistance</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_volumeObstacleWithMaximumSpeed</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_volumeObstacleWithMaximumVelocity</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_volumeObstacleWithMaximumAcceleration</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMaximumDistanceDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMinimumDistanceDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMaximumSpeedDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMaximumVelocityDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMinimumSpeedDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMaximumVelocityDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMinimumVelocityDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMaximumAccelerationDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMinimumAccelerationDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMaximumVolumeDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_operationOfObstacleHavingMinimumVolumeDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesAverageDistanceDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesMaximumDistanceDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesMinimumDistanceDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesAverageVelocityDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesMaximumVelocityDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesMinimumVelocityDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesAverageAccelerationDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesMaximumAccelerationDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_obstaclesMinimumAccelerationDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_rain_fog_wetness_time</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_speed_acceleration_obstaclesMinDist</td>
  </tr>
</tbody>
</table>

### Demand Features
The test suite was run using different sets and subsets of features for demand calculations. 
<p>Table 2. General demand feature selection group</p>

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">scenario feature name</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">feature_ego_speedDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_ego_operationDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_scenarioTrafficLightDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_scenarioSideWalkDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_totalNPCs</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_totalPedestrians</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_totalStaticObstacles</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_totalRoadUsers</td>
  </tr>
</tbody>
</table>

<p>Table 3. Weather demand feature selection group</p>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax">scenario feature name</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">feature_rainDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_fogDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_wetnessDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_timeDemand</td>
  </tr>
  <tr>
    <td class="tg-0pky">feature_combo_rain_fog_wetness_time</td>
  </tr>
</tbody>
</table>

<p>Table 4. Obstacle attribute demand feature selection group</p>

<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax">scenario feature name</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">feature_obstaclesAverageDistanceDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesMinimumDistanceDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesMaximumDistanceDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesAverageVelocityDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesMaximumVelocityDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesMinimumVelocityDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesAverageAccelerationDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesMaximumAccelerationDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesMinimumAccelerationDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_combo_speed_acceleration_obstaclesMinDist</td>
  </tr>
</tbody>
</table>
<p>Table 5. Obstacle operation demand feature selection group</p>

<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax">scenario feature name</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">feature_operationOfObstacleHavingMaximumDistanceDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_operationOfObstacleHavingMinimumDistanceDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_operationOfObstacleHavingMaximumSpeedDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_operationOfObstacleHavingMinimumSpeedDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_operationOfObstacleHavingMaximumVelocityDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_operationOfObstacleHavingMinimumVelocityDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_operationOfObstacleHavingMaximumAccelerationDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_operationOfObstacleHavingMinimumAccelerationDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_operationOfObstacleHavingMaximumVolumeDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_operationOfObstacleHavingMinimumVolumeDemand</td>
  </tr>
</tbody>
</table>

### Diversity Features
Table 6. Diversity features selected

<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax">scenario feature name</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">feature_ego_acceleration</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ego_throttle</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ego_steeringTarget</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ego_brake</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ego_steeringRate</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ego_velocityx</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ego_velocityy</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ego_accelerationx</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ego_accelerationy</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ego_accelerationz</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ego_positionx</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ego_positiony</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ego_positionz</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ego_operationDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_rainDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_fogDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_wetnessDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_timeDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_scenarioTrafficLightDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_trafficLight</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_scenarioSideWalkDemand</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ego_speed</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_totalNPCs</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_totalPedestrians</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_totalStaticObstacles</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_totalRoadUsers</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesMaximumDistance</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesMinimumDistance</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_typeObstacleHavingMaximumDistance</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_typeObstacleHavingMinimumDistance</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesMaximumSpeed</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesMinimumSpeed</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_typeObstacleHavingMaximumSpeed</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_typeObstacleHavingMinimumSpeed</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ObstaclesMaximumVelocity</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_ObstaclesMinimumVelocity</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_typeObstacleHavingMaximumVelocity</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_typeObstacleHavingMinimumVelocity</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesMaximumAcceleration</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_typeObstacleHavingMinimumAcceleration</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesMaximumVolume</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_obstaclesMinimumVolume</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_typeObstacleHavingMaximumVolume</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_typeObstacleHavingMinimumVolume</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_volumeObstacleWithMinimumDistance</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_volumeObstacleWithMaximumSpeed</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_volumeObstacleWithMaximumVelocity</td>
  </tr>
  <tr>
    <td class="tg-0lax">feature_volumeObstacleWithMaximumAcceleration</td>
  </tr>
</tbody>
</table>