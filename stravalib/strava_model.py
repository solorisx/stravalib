# generated by datamodel-codegen:
#   filename:  <stdin>

from __future__ import annotations

from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field


class ActivityTotal(BaseModel):
    """
    A roll-up of metrics pertaining to a set of activities. Values are in seconds and meters.
    """

    achievement_count: Optional[int] = None
    """
    The total number of achievements of the considered activities.
    """
    count: Optional[int] = None
    """
    The number of activities considered in this total.
    """
    distance: Optional[float] = None
    """
    The total distance covered by the considered activities.
    """
    elapsed_time: Optional[int] = None
    """
    The total elapsed time of the considered activities.
    """
    elevation_gain: Optional[float] = None
    """
    The total elevation gain of the considered activities.
    """
    moving_time: Optional[int] = None
    """
    The total moving time of the considered activities.
    """


class ActivityType(BaseModel):
    __root__: Literal[
        "AlpineSki",
        "BackcountrySki",
        "Canoeing",
        "Crossfit",
        "EBikeRide",
        "Elliptical",
        "Golf",
        "Handcycle",
        "Hike",
        "IceSkate",
        "InlineSkate",
        "Kayaking",
        "Kitesurf",
        "NordicSki",
        "Ride",
        "RockClimbing",
        "RollerSki",
        "Rowing",
        "Run",
        "Sail",
        "Skateboard",
        "Snowboard",
        "Snowshoe",
        "Soccer",
        "StairStepper",
        "StandUpPaddling",
        "Surfing",
        "Swim",
        "Velomobile",
        "VirtualRide",
        "VirtualRun",
        "Walk",
        "WeightTraining",
        "Wheelchair",
        "Windsurf",
        "Workout",
        "Yoga",
    ]
    """
    An enumeration of the types an activity may have. Note that this enumeration does not include new sport types (e.g. MountainBikeRide, EMountainBikeRide), activities with these sport types will have the corresponding activity type (e.g. Ride for MountainBikeRide, EBikeRide for EMountainBikeRide)
    """


class BaseStream(BaseModel):
    original_size: Optional[int] = None
    """
    The number of data points in this stream
    """
    resolution: Optional[Literal["low", "medium", "high"]] = None
    """
    The level of detail (sampling) in which this stream was returned
    """
    series_type: Optional[Literal["distance", "time"]] = None
    """
    The base series used in the case the stream was downsampled
    """


class CadenceStream(BaseStream):
    data: Optional[list[int]] = None
    """
    The sequence of cadence values for this stream, in rotations per minute
    """


class ClubAthlete(BaseModel):
    admin: Optional[bool] = None
    """
    Whether the athlete is a club admin.
    """
    firstname: Optional[str] = None
    """
    The athlete's first name.
    """
    lastname: Optional[str] = None
    """
    The athlete's last initial.
    """
    member: Optional[str] = None
    """
    The athlete's member status.
    """
    owner: Optional[bool] = None
    """
    Whether the athlete is club owner.
    """
    resource_state: Optional[int] = None
    """
    Resource state, indicates level of detail. Possible values: 1 -> "meta", 2 -> "summary", 3 -> "detail"
    """


class DistanceStream(BaseStream):
    data: Optional[list[float]] = None
    """
    The sequence of distance values for this stream, in meters
    """


class Error(BaseModel):
    code: Optional[str] = None
    """
    The code associated with this error.
    """
    field: Optional[str] = None
    """
    The specific field or aspect of the resource associated with this error.
    """
    resource: Optional[str] = None
    """
    The type of resource associated with this error.
    """


class Fault(BaseModel):
    """
    Encapsulates the errors that may be returned from the API.
    """

    errors: Optional[list[Error]] = None
    """
    The set of specific errors associated with this fault, if any.
    """
    message: Optional[str] = None
    """
    The message of the fault.
    """


class HeartrateStream(BaseStream):
    data: Optional[list[int]] = None
    """
    The sequence of heart rate values for this stream, in beats per minute
    """


class LatLng(BaseModel):
    """
    A pair of latitude/longitude coordinates, represented as an array of 2 floating point numbers.
    """

    __root__: list[float] = Field(..., max_items=2, min_items=2)
    """
    A pair of latitude/longitude coordinates, represented as an array of 2 floating point numbers.
    """


class LatLngStream(BaseStream):
    data: Optional[list[LatLng]] = None
    """
    The sequence of lat/long values for this stream
    """


class MembershipApplication(BaseModel):
    active: Optional[bool] = None
    """
    Whether the membership is currently active
    """
    membership: Optional[Literal["member", "pending"]] = None
    """
    The membership status of this application
    """
    success: Optional[bool] = None
    """
    Whether the application for membership was successfully submitted
    """


class MetaActivity(BaseModel):
    id: Optional[int] = None
    """
    The unique identifier of the activity
    """


class MetaAthlete(BaseModel):
    id: Optional[int] = None
    """
    The unique identifier of the athlete
    """


class MetaClub(BaseModel):
    id: Optional[int] = None
    """
    The club's unique identifier.
    """
    name: Optional[str] = None
    """
    The club's name.
    """
    resource_state: Optional[int] = None
    """
    Resource state, indicates level of detail. Possible values: 1 -> "meta", 2 -> "summary", 3 -> "detail"
    """


class MovingStream(BaseStream):
    data: Optional[list[bool]] = None
    """
    The sequence of moving values for this stream, as boolean values
    """


class Primary(BaseModel):
    id: Optional[int] = None
    source: Optional[int] = None
    unique_id: Optional[str] = None
    urls: Optional[dict[str, str]] = None


class PhotosSummary(BaseModel):
    count: Optional[int] = None
    """
    The number of photos
    """
    primary: Optional[Primary] = None


class PolylineMap(BaseModel):
    id: Optional[str] = None
    """
    The identifier of the map
    """
    polyline: Optional[str] = None
    """
    The polyline of the map, only returned on detailed representation of an object
    """
    summary_polyline: Optional[str] = None
    """
    The summary polyline of the map
    """


class PowerStream(BaseStream):
    data: Optional[list[int]] = None
    """
    The sequence of power values for this stream, in watts
    """


class SmoothGradeStream(BaseStream):
    data: Optional[list[float]] = None
    """
    The sequence of grade values for this stream, as percents of a grade
    """


class SmoothVelocityStream(BaseStream):
    data: Optional[list[float]] = None
    """
    The sequence of velocity values for this stream, in meters per second
    """


class Split(BaseModel):
    average_speed: Optional[float] = None
    """
    The average speed of this split, in meters per second
    """
    distance: Optional[float] = None
    """
    The distance of this split, in meters
    """
    elapsed_time: Optional[int] = None
    """
    The elapsed time of this split, in seconds
    """
    elevation_difference: Optional[float] = None
    """
    The elevation difference of this split, in meters
    """
    moving_time: Optional[int] = None
    """
    The moving time of this split, in seconds
    """
    pace_zone: Optional[int] = None
    """
    The pacing zone of this split
    """
    split: Optional[int] = None
    """
    N/A
    """


class SportType(BaseModel):
    __root__: Literal[
        "AlpineSki",
        "BackcountrySki",
        "Badminton",
        "Canoeing",
        "Crossfit",
        "EBikeRide",
        "Elliptical",
        "EMountainBikeRide",
        "Golf",
        "GravelRide",
        "Handcycle",
        "HighIntensityIntervalTraining",
        "Hike",
        "IceSkate",
        "InlineSkate",
        "Kayaking",
        "Kitesurf",
        "MountainBikeRide",
        "NordicSki",
        "Pickleball",
        "Pilates",
        "Racquetball",
        "Ride",
        "RockClimbing",
        "RollerSki",
        "Rowing",
        "Run",
        "Sail",
        "Skateboard",
        "Snowboard",
        "Snowshoe",
        "Soccer",
        "Squash",
        "StairStepper",
        "StandUpPaddling",
        "Surfing",
        "Swim",
        "TableTennis",
        "Tennis",
        "TrailRun",
        "Velomobile",
        "VirtualRide",
        "VirtualRow",
        "VirtualRun",
        "Walk",
        "WeightTraining",
        "Wheelchair",
        "Windsurf",
        "Workout",
        "Yoga",
    ]
    """
    An enumeration of the sport types an activity may have. Distinct from ActivityType in that it has new types (e.g. MountainBikeRide)
    """


class StreamType(BaseModel):
    __root__: Literal[
        "time",
        "distance",
        "latlng",
        "altitude",
        "velocity_smooth",
        "heartrate",
        "cadence",
        "watts",
        "temp",
        "moving",
        "grade_smooth",
    ]
    """
    An enumeration of the supported types of streams.
    """


class SummaryActivity(MetaActivity):
    achievement_count: Optional[int] = None
    """
    The number of achievements gained during this activity
    """
    athlete: Optional[MetaAthlete] = None
    athlete_count: Optional[int] = Field(None, ge=1)
    """
    The number of athletes for taking part in a group activity
    """
    average_speed: Optional[float] = None
    """
    The activity's average speed, in meters per second
    """
    average_watts: Optional[float] = None
    """
    Average power output in watts during this activity. Rides only
    """
    comment_count: Optional[int] = None
    """
    The number of comments for this activity
    """
    commute: Optional[bool] = None
    """
    Whether this activity is a commute
    """
    device_watts: Optional[bool] = None
    """
    Whether the watts are from a power meter, false if estimated
    """
    distance: Optional[float] = None
    """
    The activity's distance, in meters
    """
    elapsed_time: Optional[int] = None
    """
    The activity's elapsed time, in seconds
    """
    elev_high: Optional[float] = None
    """
    The activity's highest elevation, in meters
    """
    elev_low: Optional[float] = None
    """
    The activity's lowest elevation, in meters
    """
    end_latlng: Optional[LatLng] = None
    external_id: Optional[str] = None
    """
    The identifier provided at upload time
    """
    flagged: Optional[bool] = None
    """
    Whether this activity is flagged
    """
    gear_id: Optional[str] = None
    """
    The id of the gear for the activity
    """
    has_kudoed: Optional[bool] = None
    """
    Whether the logged-in athlete has kudoed this activity
    """
    hide_from_home: Optional[bool] = None
    """
    Whether the activity is muted
    """
    kilojoules: Optional[float] = None
    """
    The total work done in kilojoules during this activity. Rides only
    """
    kudos_count: Optional[int] = None
    """
    The number of kudos given for this activity
    """
    manual: Optional[bool] = None
    """
    Whether this activity was created manually
    """
    map: Optional[PolylineMap] = None
    max_speed: Optional[float] = None
    """
    The activity's max speed, in meters per second
    """
    max_watts: Optional[int] = None
    """
    Rides with power meter data only
    """
    moving_time: Optional[int] = None
    """
    The activity's moving time, in seconds
    """
    name: Optional[str] = None
    """
    The name of the activity
    """
    photo_count: Optional[int] = None
    """
    The number of Instagram photos for this activity
    """
    private: Optional[bool] = None
    """
    Whether this activity is private
    """
    sport_type: Optional[SportType] = None
    start_date: Optional[datetime] = None
    """
    The time at which the activity was started.
    """
    start_date_local: Optional[datetime] = None
    """
    The time at which the activity was started in the local timezone.
    """
    start_latlng: Optional[LatLng] = None
    timezone: Optional[str] = None
    """
    The timezone of the activity
    """
    total_elevation_gain: Optional[float] = None
    """
    The activity's total elevation gain.
    """
    total_photo_count: Optional[int] = None
    """
    The number of Instagram and Strava photos for this activity
    """
    trainer: Optional[bool] = None
    """
    Whether this activity was recorded on a training machine
    """
    type: Optional[ActivityType] = None
    """
    Deprecated. Prefer to use sport_type
    """
    upload_id: Optional[int] = None
    """
    The identifier of the upload that resulted in this activity
    """
    upload_id_str: Optional[str] = None
    """
    The unique identifier of the upload in string format
    """
    weighted_average_watts: Optional[int] = None
    """
    Similar to Normalized Power. Rides with power meter data only
    """
    workout_type: Optional[int] = None
    """
    The activity's workout type
    """


class SummaryAthlete(MetaAthlete):
    city: Optional[str] = None
    """
    The athlete's city.
    """
    country: Optional[str] = None
    """
    The athlete's country.
    """
    created_at: Optional[datetime] = None
    """
    The time at which the athlete was created.
    """
    firstname: Optional[str] = None
    """
    The athlete's first name.
    """
    lastname: Optional[str] = None
    """
    The athlete's last name.
    """
    premium: Optional[bool] = None
    """
    Deprecated.  Use summit field instead. Whether the athlete has any Summit subscription.
    """
    profile: Optional[str] = None
    """
    URL to a 124x124 pixel profile picture.
    """
    profile_medium: Optional[str] = None
    """
    URL to a 62x62 pixel profile picture.
    """
    resource_state: Optional[int] = None
    """
    Resource state, indicates level of detail. Possible values: 1 -> "meta", 2 -> "summary", 3 -> "detail"
    """
    sex: Optional[Literal["M", "F"]] = None
    """
    The athlete's sex.
    """
    state: Optional[str] = None
    """
    The athlete's state or geographical region.
    """
    summit: Optional[bool] = None
    """
    Whether the athlete has any Summit subscription.
    """
    updated_at: Optional[datetime] = None
    """
    The time at which the athlete was last updated.
    """


class SummaryClub(MetaClub):
    activity_types: Optional[list[ActivityType]] = None
    """
    The activity types that count for a club. This takes precedence over sport_type.
    """
    city: Optional[str] = None
    """
    The club's city.
    """
    country: Optional[str] = None
    """
    The club's country.
    """
    cover_photo: Optional[str] = None
    """
    URL to a ~1185x580 pixel cover photo.
    """
    cover_photo_small: Optional[str] = None
    """
    URL to a ~360x176  pixel cover photo.
    """
    featured: Optional[bool] = None
    """
    Whether the club is featured or not.
    """
    member_count: Optional[int] = None
    """
    The club's member count.
    """
    private: Optional[bool] = None
    """
    Whether the club is private.
    """
    profile_medium: Optional[str] = None
    """
    URL to a 60x60 pixel profile picture.
    """
    sport_type: Optional[
        Literal["cycling", "running", "triathlon", "other"]
    ] = None
    """
    Deprecated. Prefer to use activity_types.
    """
    state: Optional[str] = None
    """
    The club's state or geographical region.
    """
    url: Optional[str] = None
    """
    The club's vanity URL.
    """
    verified: Optional[bool] = None
    """
    Whether the club is verified or not.
    """


class SummaryGear(BaseModel):
    distance: Optional[float] = None
    """
    The distance logged with this gear.
    """
    id: Optional[str] = None
    """
    The gear's unique identifier.
    """
    name: Optional[str] = None
    """
    The gear's name.
    """
    primary: Optional[bool] = None
    """
    Whether this gear's is the owner's default one.
    """
    resource_state: Optional[int] = None
    """
    Resource state, indicates level of detail. Possible values: 2 -> "summary", 3 -> "detail"
    """


class SummaryPRSegmentEffort(BaseModel):
    effort_count: Optional[int] = None
    """
    Number of efforts by the authenticated athlete on this segment.
    """
    pr_activity_id: Optional[int] = None
    """
    The unique identifier of the activity related to the PR effort.
    """
    pr_date: Optional[datetime] = None
    """
    The time at which the PR effort was started.
    """
    pr_elapsed_time: Optional[int] = None
    """
    The elapsed time ot the PR effort.
    """


class SummarySegmentEffort(BaseModel):
    activity_id: Optional[int] = None
    """
    The unique identifier of the activity related to this effort
    """
    distance: Optional[float] = None
    """
    The effort's distance in meters
    """
    elapsed_time: Optional[int] = None
    """
    The effort's elapsed time
    """
    id: Optional[int] = None
    """
    The unique identifier of this effort
    """
    is_kom: Optional[bool] = None
    """
    Whether this effort is the current best on the leaderboard
    """
    start_date: Optional[datetime] = None
    """
    The time at which the effort was started.
    """
    start_date_local: Optional[datetime] = None
    """
    The time at which the effort was started in the local timezone.
    """


class TemperatureStream(BaseStream):
    data: Optional[list[int]] = None
    """
    The sequence of temperature values for this stream, in celsius degrees
    """


class TimeStream(BaseStream):
    data: Optional[list[int]] = None
    """
    The sequence of time values for this stream, in seconds
    """


class UpdatableActivity(BaseModel):
    commute: Optional[bool] = None
    """
    Whether this activity is a commute
    """
    description: Optional[str] = None
    """
    The description of the activity
    """
    gear_id: Optional[str] = None
    """
    Identifier for the gear associated with the activity. ‘none’ clears gear from activity
    """
    hide_from_home: Optional[bool] = None
    """
    Whether this activity is muted
    """
    name: Optional[str] = None
    """
    The name of the activity
    """
    sport_type: Optional[SportType] = None
    trainer: Optional[bool] = None
    """
    Whether this activity was recorded on a training machine
    """
    type: Optional[ActivityType] = None
    """
    Deprecated. Prefer to use sport_type. In a request where both type and sport_type are present, this field will be ignored
    """


class Upload(BaseModel):
    activity_id: Optional[int] = None
    """
    The identifier of the activity this upload resulted into
    """
    error: Optional[str] = None
    """
    The error associated with this upload
    """
    external_id: Optional[str] = None
    """
    The external identifier of the upload
    """
    id: Optional[int] = None
    """
    The unique identifier of the upload
    """
    id_str: Optional[str] = None
    """
    The unique identifier of the upload in string format
    """
    status: Optional[str] = None
    """
    The status of this upload
    """


class ZoneRange(BaseModel):
    max: Optional[int] = None
    """
    The maximum value in the range.
    """
    min: Optional[int] = None
    """
    The minimum value in the range.
    """


class ZoneRanges(BaseModel):
    __root__: list[ZoneRange]


class ActivityStats(BaseModel):
    """
    A set of rolled-up statistics and totals for an athlete
    """

    all_ride_totals: Optional[ActivityTotal] = None
    """
    The all time ride stats for the athlete.
    """
    all_run_totals: Optional[ActivityTotal] = None
    """
    The all time run stats for the athlete.
    """
    all_swim_totals: Optional[ActivityTotal] = None
    """
    The all time swim stats for the athlete.
    """
    biggest_climb_elevation_gain: Optional[float] = None
    """
    The highest climb ridden by the athlete.
    """
    biggest_ride_distance: Optional[float] = None
    """
    The longest distance ridden by the athlete.
    """
    recent_ride_totals: Optional[ActivityTotal] = None
    """
    The recent (last 4 weeks) ride stats for the athlete.
    """
    recent_run_totals: Optional[ActivityTotal] = None
    """
    The recent (last 4 weeks) run stats for the athlete.
    """
    recent_swim_totals: Optional[ActivityTotal] = None
    """
    The recent (last 4 weeks) swim stats for the athlete.
    """
    ytd_ride_totals: Optional[ActivityTotal] = None
    """
    The year to date ride stats for the athlete.
    """
    ytd_run_totals: Optional[ActivityTotal] = None
    """
    The year to date run stats for the athlete.
    """
    ytd_swim_totals: Optional[ActivityTotal] = None
    """
    The year to date swim stats for the athlete.
    """


class AltitudeStream(BaseStream):
    data: Optional[list[float]] = None
    """
    The sequence of altitude values for this stream, in meters
    """


class ClubActivity(BaseModel):
    athlete: Optional[MetaAthlete] = None
    distance: Optional[float] = None
    """
    The activity's distance, in meters
    """
    elapsed_time: Optional[int] = None
    """
    The activity's elapsed time, in seconds
    """
    moving_time: Optional[int] = None
    """
    The activity's moving time, in seconds
    """
    name: Optional[str] = None
    """
    The name of the activity
    """
    sport_type: Optional[SportType] = None
    total_elevation_gain: Optional[float] = None
    """
    The activity's total elevation gain.
    """
    type: Optional[ActivityType] = None
    """
    Deprecated. Prefer to use sport_type
    """
    workout_type: Optional[int] = None
    """
    The activity's workout type
    """


class ClubAnnouncement(BaseModel):
    athlete: Optional[SummaryAthlete] = None
    club_id: Optional[int] = None
    """
    The unique identifier of the club this announcements was made in.
    """
    created_at: Optional[datetime] = None
    """
    The time at which this announcement was created.
    """
    id: Optional[int] = None
    """
    The unique identifier of this announcement.
    """
    message: Optional[str] = None
    """
    The content of this announcement
    """


class Comment(BaseModel):
    activity_id: Optional[int] = None
    """
    The identifier of the activity this comment is related to
    """
    athlete: Optional[SummaryAthlete] = None
    created_at: Optional[datetime] = None
    """
    The time at which this comment was created.
    """
    id: Optional[int] = None
    """
    The unique identifier of this comment
    """
    text: Optional[str] = None
    """
    The content of the comment
    """


class DetailedAthlete(SummaryAthlete):
    bikes: Optional[list[SummaryGear]] = None
    """
    The athlete's bikes.
    """
    clubs: Optional[list[SummaryClub]] = None
    """
    The athlete's clubs.
    """
    follower_count: Optional[int] = None
    """
    The athlete's follower count.
    """
    friend_count: Optional[int] = None
    """
    The athlete's friend count.
    """
    ftp: Optional[int] = None
    """
    The athlete's FTP (Functional Threshold Power).
    """
    measurement_preference: Optional[Literal["feet", "meters"]] = None
    """
    The athlete's preferred unit system.
    """
    shoes: Optional[list[SummaryGear]] = None
    """
    The athlete's shoes.
    """
    weight: Optional[float] = None
    """
    The athlete's weight.
    """


class DetailedClub(SummaryClub):
    admin: Optional[bool] = None
    """
    Whether the currently logged-in athlete is an administrator of this club.
    """
    following_count: Optional[int] = None
    """
    The number of athletes in the club that the logged-in athlete follows.
    """
    membership: Optional[Literal["member", "pending"]] = None
    """
    The membership status of the logged-in athlete.
    """
    owner: Optional[bool] = None
    """
    Whether the currently logged-in athlete is the owner of this club.
    """


class DetailedGear(SummaryGear):
    brand_name: Optional[str] = None
    """
    The gear's brand name.
    """
    description: Optional[str] = None
    """
    The gear's description.
    """
    frame_type: Optional[int] = None
    """
    The gear's frame type (bike only).
    """
    model_name: Optional[str] = None
    """
    The gear's model name.
    """


class ExplorerSegment(BaseModel):
    avg_grade: Optional[float] = None
    """
    The segment's average grade, in percents
    """
    climb_category: Optional[int] = Field(None, ge=0, le=5)
    """
    The category of the climb [0, 5]. Higher is harder ie. 5 is Hors catégorie, 0 is uncategorized in climb_category. If climb_category = 5, climb_category_desc = HC. If climb_category = 2, climb_category_desc = 3.
    """
    climb_category_desc: Optional[
        Literal["NC", "4", "3", "2", "1", "HC"]
    ] = None
    """
    The description for the category of the climb
    """
    distance: Optional[float] = None
    """
    The segment's distance, in meters
    """
    elev_difference: Optional[float] = None
    """
    The segments's evelation difference, in meters
    """
    end_latlng: Optional[LatLng] = None
    id: Optional[int] = None
    """
    The unique identifier of this segment
    """
    name: Optional[str] = None
    """
    The name of this segment
    """
    points: Optional[str] = None
    """
    The polyline of the segment
    """
    start_latlng: Optional[LatLng] = None


class HeartRateZoneRanges(BaseModel):
    custom_zones: Optional[bool] = None
    """
    Whether the athlete has set their own custom heart rate zones
    """
    zones: Optional[ZoneRanges] = None


class Lap(BaseModel):
    activity: Optional[MetaActivity] = None
    athlete: Optional[MetaAthlete] = None
    average_cadence: Optional[float] = None
    """
    The lap's average cadence
    """
    average_speed: Optional[float] = None
    """
    The lap's average speed
    """
    distance: Optional[float] = None
    """
    The lap's distance, in meters
    """
    elapsed_time: Optional[int] = None
    """
    The lap's elapsed time, in seconds
    """
    end_index: Optional[int] = None
    """
    The end index of this effort in its activity's stream
    """
    id: Optional[int] = None
    """
    The unique identifier of this lap
    """
    lap_index: Optional[int] = None
    """
    The index of this lap in the activity it belongs to
    """
    max_speed: Optional[float] = None
    """
    The maximum speed of this lat, in meters per second
    """
    moving_time: Optional[int] = None
    """
    The lap's moving time, in seconds
    """
    name: Optional[str] = None
    """
    The name of the lap
    """
    pace_zone: Optional[int] = None
    """
    The athlete's pace zone during this lap
    """
    split: Optional[int] = None
    start_date: Optional[datetime] = None
    """
    The time at which the lap was started.
    """
    start_date_local: Optional[datetime] = None
    """
    The time at which the lap was started in the local timezone.
    """
    start_index: Optional[int] = None
    """
    The start index of this effort in its activity's stream
    """
    total_elevation_gain: Optional[float] = None
    """
    The elevation gain of this lap, in meters
    """


class PowerZoneRanges(BaseModel):
    zones: Optional[ZoneRanges] = None


class StreamSet(BaseModel):
    altitude: Optional[AltitudeStream] = None
    cadence: Optional[CadenceStream] = None
    distance: Optional[DistanceStream] = None
    grade_smooth: Optional[SmoothGradeStream] = None
    heartrate: Optional[HeartrateStream] = None
    latlng: Optional[LatLngStream] = None
    moving: Optional[MovingStream] = None
    temp: Optional[TemperatureStream] = None
    time: Optional[TimeStream] = None
    velocity_smooth: Optional[SmoothVelocityStream] = None
    watts: Optional[PowerStream] = None


class SummarySegment(BaseModel):
    activity_type: Optional[Literal["Ride", "Run"]] = None
    athlete_pr_effort: Optional[SummaryPRSegmentEffort] = None
    athlete_segment_stats: Optional[SummarySegmentEffort] = None
    average_grade: Optional[float] = None
    """
    The segment's average grade, in percents
    """
    city: Optional[str] = None
    """
    The segments's city.
    """
    climb_category: Optional[int] = None
    """
    The category of the climb [0, 5]. Higher is harder ie. 5 is Hors catégorie, 0 is uncategorized in climb_category.
    """
    country: Optional[str] = None
    """
    The segment's country.
    """
    distance: Optional[float] = None
    """
    The segment's distance, in meters
    """
    elevation_high: Optional[float] = None
    """
    The segments's highest elevation, in meters
    """
    elevation_low: Optional[float] = None
    """
    The segments's lowest elevation, in meters
    """
    end_latlng: Optional[LatLng] = None
    id: Optional[int] = None
    """
    The unique identifier of this segment
    """
    maximum_grade: Optional[float] = None
    """
    The segments's maximum grade, in percents
    """
    name: Optional[str] = None
    """
    The name of this segment
    """
    private: Optional[bool] = None
    """
    Whether this segment is private.
    """
    start_latlng: Optional[LatLng] = None
    state: Optional[str] = None
    """
    The segments's state or geographical region.
    """


class TimedZoneRange(ZoneRange):
    """
    A union type representing the time spent in a given zone.
    """

    time: Optional[int] = None
    """
    The number of seconds spent in this zone
    """


class Zones(BaseModel):
    heart_rate: Optional[HeartRateZoneRanges] = None
    power: Optional[PowerZoneRanges] = None


class DetailedSegment(SummarySegment):
    athlete_count: Optional[int] = None
    """
    The number of unique athletes who have an effort for this segment
    """
    created_at: Optional[datetime] = None
    """
    The time at which the segment was created.
    """
    effort_count: Optional[int] = None
    """
    The total number of efforts for this segment
    """
    hazardous: Optional[bool] = None
    """
    Whether this segment is considered hazardous
    """
    map: Optional[PolylineMap] = None
    star_count: Optional[int] = None
    """
    The number of stars for this segment
    """
    total_elevation_gain: Optional[float] = None
    """
    The segment's total elevation gain.
    """
    updated_at: Optional[datetime] = None
    """
    The time at which the segment was last updated.
    """


class DetailedSegmentEffort(SummarySegmentEffort):
    activity: Optional[MetaActivity] = None
    athlete: Optional[MetaAthlete] = None
    average_cadence: Optional[float] = None
    """
    The effort's average cadence
    """
    average_heartrate: Optional[float] = None
    """
    The heart heart rate of the athlete during this effort
    """
    average_watts: Optional[float] = None
    """
    The average wattage of this effort
    """
    device_watts: Optional[bool] = None
    """
    For riding efforts, whether the wattage was reported by a dedicated recording device
    """
    end_index: Optional[int] = None
    """
    The end index of this effort in its activity's stream
    """
    hidden: Optional[bool] = None
    """
    Whether this effort should be hidden when viewed within an activity
    """
    kom_rank: Optional[int] = Field(None, ge=1, le=10)
    """
    The rank of the effort on the global leaderboard if it belongs in the top 10 at the time of upload
    """
    max_heartrate: Optional[float] = None
    """
    The maximum heart rate of the athlete during this effort
    """
    moving_time: Optional[int] = None
    """
    The effort's moving time
    """
    name: Optional[str] = None
    """
    The name of the segment on which this effort was performed
    """
    pr_rank: Optional[int] = Field(None, ge=1, le=3)
    """
    The rank of the effort on the athlete's leaderboard if it belongs in the top 3 at the time of upload
    """
    segment: Optional[SummarySegment] = None
    start_index: Optional[int] = None
    """
    The start index of this effort in its activity's stream
    """


class ExplorerResponse(BaseModel):
    segments: Optional[list[ExplorerSegment]] = None
    """
    The set of segments matching an explorer request
    """


class Route(BaseModel):
    athlete: Optional[SummaryAthlete] = None
    created_at: Optional[datetime] = None
    """
    The time at which the route was created
    """
    description: Optional[str] = None
    """
    The description of the route
    """
    distance: Optional[float] = None
    """
    The route's distance, in meters
    """
    elevation_gain: Optional[float] = None
    """
    The route's elevation gain.
    """
    estimated_moving_time: Optional[int] = None
    """
    Estimated time in seconds for the authenticated athlete to complete route
    """
    id: Optional[int] = None
    """
    The unique identifier of this route
    """
    id_str: Optional[str] = None
    """
    The unique identifier of the route in string format
    """
    map: Optional[PolylineMap] = None
    name: Optional[str] = None
    """
    The name of this route
    """
    private: Optional[bool] = None
    """
    Whether this route is private
    """
    segments: Optional[list[SummarySegment]] = None
    """
    The segments traversed by this route
    """
    starred: Optional[bool] = None
    """
    Whether this route is starred by the logged-in athlete
    """
    sub_type: Optional[int] = None
    """
    This route's sub-type (1 for road, 2 for mountain bike, 3 for cross, 4 for trail, 5 for mixed)
    """
    timestamp: Optional[int] = None
    """
    An epoch timestamp of when the route was created
    """
    type: Optional[int] = None
    """
    This route's type (1 for ride, 2 for runs)
    """
    updated_at: Optional[datetime] = None
    """
    The time at which the route was last updated
    """


class TimedZoneDistribution(BaseModel):
    """
    Stores the exclusive ranges representing zones and the time spent in each.
    """

    __root__: list[TimedZoneRange]
    """
    Stores the exclusive ranges representing zones and the time spent in each.
    """


class ActivityZone(BaseModel):
    custom_zones: Optional[bool] = None
    distribution_buckets: Optional[TimedZoneDistribution] = None
    max: Optional[int] = None
    points: Optional[int] = None
    score: Optional[int] = None
    sensor_based: Optional[bool] = None
    type: Optional[Literal["heartrate", "power"]] = None


class DetailedActivity(SummaryActivity):
    best_efforts: Optional[list[DetailedSegmentEffort]] = None
    calories: Optional[float] = None
    """
    The number of kilocalories consumed during this activity
    """
    description: Optional[str] = None
    """
    The description of the activity
    """
    device_name: Optional[str] = None
    """
    The name of the device used to record the activity
    """
    embed_token: Optional[str] = None
    """
    The token used to embed a Strava activity
    """
    gear: Optional[SummaryGear] = None
    laps: Optional[list[Lap]] = None
    photos: Optional[PhotosSummary] = None
    segment_efforts: Optional[list[DetailedSegmentEffort]] = None
    splits_metric: Optional[list[Split]] = None
    """
    The splits of this activity in metric units (for runs)
    """
    splits_standard: Optional[list[Split]] = None
    """
    The splits of this activity in imperial units (for runs)
    """
