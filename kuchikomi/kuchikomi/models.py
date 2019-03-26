# -*- config: utf-8 -*-

from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, SmallInteger, VARCHAR, String, Date, DateTime, Float, Boolean, Text, LargeBinary

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"), encoding='utf8')


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class RettyKuchikomiDB(DeclarativeBase):
    __tablename__ = "retty_kuchikomi"

    id              = Column(Integer, primary_key=True)
    restaurant_id   = Column('店舗ID', String(20), comment="restaurant_id")
    kuchikomi_id    = Column('クチコミID', String(20), comment="kuchikomi_id")
    kuchikomi_url   = Column('クチコミURL', VARCHAR(100), comment="kuchikomi_url")
    customer_name   = Column('投稿者', String(50), comment="customer_name", nullable=True)
    overall_score   = Column('評価', String(20), comment="overall_score", nullable=True)
    review_comment  = Column('コメント', Text, comment="review_comment", nullable=True)
    tags            = Column('タグ', Text, comment="tags", nullable=True)
    review_date     = Column('投稿日時', String(20), comment="review_date", nullable=True)
    num_of_likes    = Column('いいね件数', SmallInteger, comment="num_of_likes", nullable=True)
    num_of_interested = Column('行きたい件数', SmallInteger, comment="num_of_interested")


class RettyFacilityDB(DeclarativeBase):
    __tablename__ = "retty_facility"

    id              = Column(Integer, primary_key=True)
    restaurant_id   = Column('店舗ID', String(20), comment="店舗ID")
    get_url         = Column('url', String(100), comment="URL")
    url_pre         = Column('url_pre', String(20), comment="URL_PRE")
    url_area        = Column('url_area', String(20), comment="URL_ARE")
    url_sub         = Column('url_sub', String(20), comment="URL_SUB")
    area            = Column('エリア', String(50), comment="area")
    store_name      = Column('店舗名', String(20), comment="store_name")
    store_kana_name = Column('よみ', String(20), comment="store_kana_name")
    num_of_likes    = Column('いいね件数', SmallInteger, comment="num_of_likes", nullable=True)
    num_of_interested   = Column('行きたい件数', SmallInteger, comment="num_of_interested", nullable=True)
    store_popularity    = Column('人気店★数', SmallInteger, comment="store_popularity", nullable=True)
    description         = Column('紹介文', Text, comment="description", nullable=True)
    description_title   = Column('紹介文タイトル', Text, comment="description_title", nullable=True)
    recommended_rate    = Column('オススメ度(％)', SmallInteger, comment="recommended_rate", nullable=True)
    num_of_persons_went = Column('行った人', Integer, comment="num_of_persons_went", nullable=True)
    recommended_rate_excellent = Column('オススメ度　excellent', SmallInteger, comment="recommended_rate_excellent", nullable=True)
    recommended_rate_good      = Column('オススメ度 Good', SmallInteger, comment="recommended_rate_good", nullable=True)
    recommended_rate_average   = Column('オススメ度 Average', SmallInteger, comment="recommended_rate_average", nullable=True)
    recommended_num_of_people  = Column('おすすめ人数', Integer, comment="recommended_num_of_people", nullable=True)
    dinner_budget   = Column('夜予算', String(50), comment="dinner_budget", nullable=True)
    lunch_budget    = Column('昼予算', String(50), comment="lunch_budget", nullable=True)
    budget          = Column('予算', String(100), comment="budget", nullable=True)
    nearest_station = Column('最寄り駅', Text, comment="nearest_station", nullable=True)
    genre           = Column('ジャンル', Text, comment="genre", nullable=True)
    regular_holiday = Column('定休日', String(100), comment="regular_holiday", nullable=True)
    number_of_photo = Column('写真', Integer, comment="number_of_photo", nullable=True)
    number_of_reviews = Column('すべてのクチコミ', Integer, comment="number_of_reviews", nullable=True)
    reviews_for_lunch = Column('ランチのクチコミ', Integer, comment="reviews_for_lunch", nullable=True)
    reviews_for_dinner= Column('ディナーのクチコミ', Integer, comment="reviews_for_dinner", nullable=True)
    business_hours  = Column('営業時間', Text, comment="business_hours", nullable=True)
    street_address  = Column('住所', Text, comment="street_address", nullable=True)
    access          = Column('アクセス',Text, comment="access", nullable=True)
    store           = Column('店名', Text, comment="store", nullable=True)
    reservation_inquiry = Column('予約・問い合わせ', String(50), comment="reservation_inquiry", nullable=True)
    remarks         = Column('備考', Text, comment="remarks", nullable=True)
    phone_number    = Column('電話番号', String(50), comment="phone_number", nullable=True)
    home_page       = Column('お店のホームページ', VARCHAR(100), comment="home_page", nullable=True)
    facebook_url    = Column('FacebookのURL', VARCHAR(100), comment="facebook_url", nullable=True)
    banquet_capacity= Column('宴会収容人数', Integer, comment="banquet_capacity", nullable=True)
    payment_card    = Column('カード', String(100), comment="payment_card", nullable=True)
    online_booking  = Column('オンライン予約', String(50), comment="online_booking", nullable=True)
    party_correspondence = Column('ウェディング・二次会対応', Text, comment="party_correspondence", nullable=True)


class TripAdvisorKuchikomiDB(DeclarativeBase):
    __tablename__ = "tripadvisor_kuchikomi"

    id                  = Column(Integer, primary_key=True)
    area_id             = Column('エリアID:g', String(20), comment="area_id")
    facility_id         = Column('施設ID:d', String(20), comment="facility_id")
    review_id           = Column('クチコミID:', String(20), comment="review_idr")
    get_url             = Column('クチコミURL', String(100), comment="get_url")
    reviewer_name       = Column('投稿者', String(50), comment="reviewer_name")
    post_date           = Column('投稿日', String(20), comment="post_date", nullable=True)
    post_area           = Column('投稿者エリア', String(100), comment="post_area", nullable=True)
    number_of_posts     = Column('投稿数', Integer, comment="number_of_posts", nullable=True)
    number_of_likes     = Column('いいね数', SmallInteger, comment="number_of_likes", nullable=True)
    title               = Column('タイトル', Text, comment="title", nullable=True)
    review              = Column('クチコミ', Text, comment="review", nullable=True)
    traveler_type       = Column('旅行者タイプ', String(20), comment="traveler_type", nullable=True)
    stay_time           = Column('訪問時期', String(20), comment="stay_time", nullable=True)
    total_score         = Column('総合評価', Float, comment="total_score", nullable=True)
    food_score          = Column('食事', Float, comment="food_score", nullable=True)
    service_score       = Column('サービス', Float, comment="service_score", nullable=True)
    price_score         = Column('価格', Float, comment="price_score", nullable=True)
    atmosphere_score    = Column('雰囲気', Float, comment="atmosphere_score", nullable=True)
    post_useful         = Column('役にたった', Integer, comment="post_useful", nullable=True)


class TripAdvisorFacilityDB(DeclarativeBase):
    __tablename__ = "tripadvisor_facility"

    id                  = Column(Integer, primary_key=True)
    get_url             = Column('URL', String(100), comment="get_url")
    url_area            = Column('URL_エリア', String(20), comment="url_area")
    area_id             = Column('エリアID:g', String(20), comment="area_id")
    facility_id         = Column('施設ID:d', String(20), comment="facility_id")
    area                = Column('エリア', String(100), comment="area")
    store_name          = Column('店舗名', String(100), comment="store_name", nullable=True)
    overall_rating      = Column('総合評価', Float, comment="overall_rating", nullable=True)
    number_of_reviews   = Column('クチコミ数', Integer, comment="number_of_reviews", nullable=True)
    rank                = Column('順位', String(100), comment="rank", nullable=True)
    price_range         = Column('価格帯', String(50), comment="price_range", nullable=True)
    cooking_genres      = Column('料理のジャンル', String(100), comment="cooking_genres", nullable=True)
    street_address      = Column('住所', Text, comment="street_address", nullable=True)
    phone_number        = Column('電話番号', String(20), comment="phone_number", nullable=True)
    business_hours      = Column('営業時間', String(100), comment="business_hours", nullable=True)
    number_of_photos    = Column('写真', String(20), comment="number_of_photos", nullable=True)
    award               = Column('受賞', Text, comment="award", nullable=True)
    food_score          = Column('食事', Float, comment="food_score", nullable=True)
    service_score       = Column('サービス', Float, comment="service_score", nullable=True)
    price_score         = Column('価格', Float, comment="price_score", nullable=True)
    atmosphere_score    = Column('雰囲気', Float, comment="atmosphere_score", nullable=True)
    cuisine             = Column('料理', String(100), comment="cuisine", nullable=True)
    meal_hours          = Column('食事の時間帯', String(100), comment="meal_hours", nullable=True)
    function            = Column('機能', String(100), comment="function", nullable=True)
    menu                = Column('食材別のメニュー', String(100), comment="menu", nullable=True)
    location            = Column('所在地', Text, comment="location", nullable=True)
    nearest_area        = Column('最寄り', Text, comment="nearest_area", nullable=True)
    official_site       = Column('公式サイト', String(100), comment="official_site", nullable=True)
    very_good_score     = Column('とても良い', Float, comment="very_good_score", nullable=True)
    good_score          = Column('良い', Float, comment="good_score", nullable=True)
    average_score       = Column('普通', Float, comment="average_score", nullable=True)
    bad_score           = Column('悪い', Float, comment="bad_score", nullable=True)
    very_bad_score      = Column('とても悪い', Float, comment="very_bad_score", nullable=True)
    reviews_in_english  = Column('言語英語', Integer, comment="reviews_in_english", nullable=True)
    reviews_in_japanese = Column('言語日本語', Integer, comment="reviews_in_japanese", nullable=True)
    details                  = Column('詳細', String(20), comment="details", nullable=True)
    travelers_type_family    = Column('ファミリー', Integer, comment="travelers_type_family", nullable=True)
    travelers_type_couple    = Column('カップル夫婦', Integer, comment="travelers_type_couple", nullable=True)
    travelers_type_solo      = Column('一人', Integer, comment="travelers_type_solo", nullable=True)
    travelers_type__business = Column('出張ビジネス', Integer, comment="travelers_type__business", nullable=True)
    travelers_type_friend    = Column('旅行者タイプ', Integer, comment="travelers_type_friend", nullable=True)


class TabelogUserDB(DeclarativeBase):
    __tablename__ = "tabelog_user"

    id                  = Column(Integer, primary_key=True)
    hotel_id            = Column('店舗ID', String(20), comment="hotel_id")
    kuchikomi_id        = Column('クチコミID', String(20), comment="kuchikomi_id")
    customer_id         = Column('投稿者ID', String(20), comment="customer_id")
    customer_name       = Column('投稿者', String(50), comment="customer_id")
    number_of_visit     = Column('来店数', String(20), comment="number_of_visit", nullable=True)
    get_url             = Column('クチコミUR', String(100), comment="get_urlL")
    night_total_rating      = Column('夜評価', Float, comment="night_total_rating", nullable=True)
    night_culinary_rating   = Column('(夜)料理・味', Float, comment="night_culinary_rating", nullable=True)
    night_service_rating    = Column('(夜)サービス', Float, comment="night_service_rating", nullable=True)
    night_atmosphere_rating = Column('(夜)雰囲気', Float, comment="night_atmosphere_rating", nullable=True)
    night_cp_rating         = Column('(夜)CP', Float, comment="night_cp_rating", nullable=True)
    night_drink_rating      = Column('(夜)酒・ドリンク', Float, comment="night_drink_rating", nullable=True)
    night_amount            = Column('(夜)使った金額（1人）', String(50), comment="night_amount", nullable=True)
    day_total_rating        = Column('昼評価d', Float, comment="ay_total_rating", nullable=True)
    day_culinary_rating     = Column('(昼)day_culinary_rating', Float, comment="料理・味", nullable=True)
    day_service_rating      = Column('(昼)サービス', Float, comment="day_service_rating", nullable=True)
    day_atmosphere_rating   = Column('(昼)雰囲気', Float, comment="day_atmosphere_rating", nullable=True)
    day_cp_rating           = Column('(昼)CP', Float, comment="day_cp_rating", nullable=True)
    day_drink_rating        = Column('(昼)酒・ドリンク', Float, comment="day_drink_rating", nullable=True)
    day_amount              = Column('(昼)使った金額（1人）', String(50), comment="day_amount", nullable=True)


class TabelogKuchikomiDB(DeclarativeBase):
    __tablename__ = "tabelog_kuchikomi"

    id                  = Column(Integer, primary_key=True)
    hotel_id            = Column('店舗ID', String(20), comment="hotel_id")
    kuchikomi_id        = Column('クチコミID', String(20), comment="kuchikomi_id")
    customer_id         = Column('投稿者ID', String(20), comment="customer_id")
    customer_name       = Column('投稿者', String(50), comment="customer_id")
    number_of_visit     = Column('来店数', String(20), comment="number_of_visit", nullable=True)
    get_url             = Column('クチコミUR', String(100), comment="get_urlL")
    night_total_rating      = Column('夜評価', Float, comment="night_total_rating", nullable=True)
    night_culinary_rating   = Column('(夜)料理・味', Float, comment="night_culinary_rating", nullable=True)
    night_service_rating    = Column('(夜)サービス', Float, comment="night_service_rating", nullable=True)
    night_atmosphere_rating = Column('(夜)雰囲気', Float, comment="night_atmosphere_rating", nullable=True)
    night_cp_rating         = Column('(夜)CP', Float, comment="night_cp_rating", nullable=True)
    night_drink_rating      = Column('(夜)酒・ドリンク', Float, comment="night_drink_rating", nullable=True)
    night_amount            = Column('(夜)使った金額（1人）', String(50), comment="night_amount", nullable=True)
    day_total_rating        = Column('昼評価d', Float, comment="ay_total_rating", nullable=True)
    day_culinary_rating     = Column('(昼)day_culinary_rating', Float, comment="料理・味", nullable=True)
    day_service_rating      = Column('(昼)サービス', Float, comment="day_service_rating", nullable=True)
    day_atmosphere_rating   = Column('(昼)雰囲気', Float, comment="day_atmosphere_rating", nullable=True)
    day_cp_rating           = Column('(昼)CP', Float, comment="day_cp_rating", nullable=True)
    day_drink_rating        = Column('(昼)酒・ドリンク', Float, comment="day_drink_rating", nullable=True)
    day_amount              = Column('(昼)使った金額（1人）', String(50), comment="day_amount", nullable=True)
    review_liked        = Column('いいね件数', Integer, comment="review_liked", nullable=True)
    review_date         = Column('訪問日', String(20), comment="review_date")
    review_title        = Column('タイトル', Text, comment="review_title")
    review_comment      = Column('クチコミ詳細', Text, comment="review_comment")


class TabelogFacilityDB(DeclarativeBase):
    __tablename__ = "tabelog_facility"

    id                  = Column(Integer, primary_key=True)
    hotel_id            = Column('店舗ID', String(20), comment="hotel_id")
    get_url             = Column('URL', String(100), comment="get_url")
    url_pre             = Column('url_pre', String(20), comment="URL_PRE")
    url_area1           = Column('url_area1', String(20), comment="URL_ARE1")
    url_area2           = Column('url_area2', String(20), comment="URL_ARE2")
    area                = Column('エリア', String(100), comment="area", nullable=True)
    pillow              = Column('枕詞', String(100), comment="pillow", nullable=True)
    store_name          = Column('店舗名', String(100), comment="store_name", nullable=True)
    overall_rating      = Column('総合評価点数', Float, comment="overall_rating", nullable=True)
    night_total_rating  = Column('夜点数', Float, comment="night_total_rating", nullable=True)
    day_total_rating    = Column('昼点数', Float, comment="day_total_rating", nullable=True)
    number_of_reviews   = Column('クチコミ件数', Integer, comment="number_of_reviews", nullable=True)
    number_of_photo     = Column('写真', Integer, comment="number_of_photo", nullable=True)
    menu                = Column('口コミに含まれるメニュー', Text, comment="menu", nullable=True)
    nearest_station     = Column('最寄り駅', Text, comment="nearest_station", nullable=True)
    genre               = Column('ジャンル', Text, comment="genre", nullable=True)
    night_budget        = Column('夜予算', String(100), comment="night_budget", nullable=True)
    day_budget          = Column('昼予算', String(100), comment="night_budget", nullable=True)
    regular_holiday     = Column('定休日', String(100), comment="day_budget", nullable=True)
    awards_selection_history = Column('受賞・選出歴', String(20), comment="awards_selection_history", nullable=True)
    reservation_inquiry      = Column('予約・お問い合わせ', String(20), comment="reservation_inquiry", nullable=True)
    reservation_acceptability= Column('予約可否', String(20), comment="reservation_acceptability", nullable=True)
    street_address           = Column('住所', Text, comment="street_address", nullable=True)
    transportation           = Column('交通手段', Text, comment="transportation", nullable=True)
    business_hours           = Column('営業時間', Text, comment="business_hours", nullable=True)
    method_of_payment        = Column('支払い方法', String(20), comment="method_of_payment", nullable=True)
    service_charge           = Column('サービス料・チャージ', String(100), comment="service_charge", nullable=True)
    number_of_seats         = Column('席数', String(100), comment="number_of_seats", nullable=True)
    private_room            = Column('個室', String(100), comment="private_room", nullable=True)
    reserved                = Column('貸切', String(100), comment="reserved", nullable=True)
    smoking                 = Column('禁煙・喫煙	駐車場', String(100), comment="smoking", nullable=True)
    parking                 = Column('駐車場', String(100), comment="parking", nullable=True)
    space_facilities        = Column('空間・設備', Text, comment="space_facilities", nullable=True)
    mobile                  = Column('携帯電話', String(100), comment="course", nullable=True)
    course                  = Column('コース', String(100), comment="", nullable=True)
    drink                   = Column('ドリンク', String(100), comment="drink", nullable=True)
    cooking                 = Column('料理', String(100), comment="cooking", nullable=True)
    use_scene               = Column('利用シーン', String(100), comment="use_scene", nullable=True)
    location                = Column('ロケーション', String(100), comment="location", nullable=True)
    service                 = Column('サービス', String(100), comment="service", nullable=True)
    children                = Column('お子様連れ', String(100), comment="children", nullable=True)
    home_page               = Column('ホームページ', String(100), comment="home_page", nullable=True)
    official_account        = Column('公式アカウント', String(100), comment="official_account", nullable=True)
    open_date               = Column('オープン日', String(20), comment="open_date", nullable=True)
    phone_number            = Column('電話番号', String(20), comment="phone_number", nullable=True)
    remarks                 = Column('備考', Text, comment="remarks", nullable=True)
    original_contributor    = Column('初投稿者', String(50), comment="original_contributor", nullable=True)


