<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn5.telesco.pe/file/gykUWV9XQUAdp5Fx016ugoCslTVVqdkFyOXxBLquj_Viia63rMxXvTnjrMv9ljaeEOmcuJUn8JbWb9ZfFO_YTFiD5q6TQocY4hy5QHS7x3srDT_tDN3Mh_Vv4wWh2KY3ev0HKy06nJuQ3f-93v4vMaX7h1Qb67crqMVNMpBduw8UzFMm0UDOzI8Nn8juyXGB797GlFwlkABSk0xHpWxXdsP9JwfwVPBK6YC9nLMHkoUOFc3xJGzcH1ZMshbCJMsm1VacUf0R5qDT4hNaksgXUPYdszyi-Usddt9gbG_4kDF_StvhSibv6DNP48i6ToN5Dzq_W28j7yzOec6UXpQdDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 383K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 11:20:30</div>
<hr>

<div class="tg-post" id="msg-108657">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bfab0b19.mp4?token=vBN5EDfZjWyYkrkt5hM0gSa_PvZMDSVrm9vO0r1lFzI7_ho9omCfQTjWJTfvM7EgUfXqaxWGeNnLRDfE6ArfAjSFUAZ70lqRHFiNlXwKClZdzwJBiUydWradhu0FXMGykxCeILg3wt1KwfuhSXOs7SMjLSCLqbRDHMKt9ZTu6s3yByOexRTsJ_pPHqLZW4JifOhGULHiAYInHl4venY7p2D42wOvqMs7KAIVKu5M0FK2Olq4ee_DB-TZ-Z6hANtDyzWvAQJHOX7cPB_-Z8IS8tBPxLW_BBww9gtVzmsfBSjurGpDQzw9dHdgiH0qbXpsXMEDjodXqsQIJU_pbzkXnU5uTUeLe12Fn3fz5Hy8yqoSDlz71cmSCgjIdmejnyTYm_j98F5aBW5jx7hyMJHq1hkMKd4CGjVgN96aaWHH18XfwXxUUw3otrm-QyUnmlojCRi-Mlom2xOnsEOlhPpORbb-V3wA-jjgq73ynC4Q6NpKvq-zCjEJZcMw6n6tkRg2hj8i7rG41HOh3rzP2QYGTu1GW1OQJKzwujUrVWYWbMvN_rBNOvRu3FVaj6xS5UeEVPm9tT8sD68oq85dx-VBhCp9ojZXzv3ifjEnLS93YxRgOw6PbayxHfBj2RESnoHmzjr71cfRGWafQCqObPETshkLK3yCjLskbwM9yo-gtVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bfab0b19.mp4?token=vBN5EDfZjWyYkrkt5hM0gSa_PvZMDSVrm9vO0r1lFzI7_ho9omCfQTjWJTfvM7EgUfXqaxWGeNnLRDfE6ArfAjSFUAZ70lqRHFiNlXwKClZdzwJBiUydWradhu0FXMGykxCeILg3wt1KwfuhSXOs7SMjLSCLqbRDHMKt9ZTu6s3yByOexRTsJ_pPHqLZW4JifOhGULHiAYInHl4venY7p2D42wOvqMs7KAIVKu5M0FK2Olq4ee_DB-TZ-Z6hANtDyzWvAQJHOX7cPB_-Z8IS8tBPxLW_BBww9gtVzmsfBSjurGpDQzw9dHdgiH0qbXpsXMEDjodXqsQIJU_pbzkXnU5uTUeLe12Fn3fz5Hy8yqoSDlz71cmSCgjIdmejnyTYm_j98F5aBW5jx7hyMJHq1hkMKd4CGjVgN96aaWHH18XfwXxUUw3otrm-QyUnmlojCRi-Mlom2xOnsEOlhPpORbb-V3wA-jjgq73ynC4Q6NpKvq-zCjEJZcMw6n6tkRg2hj8i7rG41HOh3rzP2QYGTu1GW1OQJKzwujUrVWYWbMvN_rBNOvRu3FVaj6xS5UeEVPm9tT8sD68oq85dx-VBhCp9ojZXzv3ifjEnLS93YxRgOw6PbayxHfBj2RESnoHmzjr71cfRGWafQCqObPETshkLK3yCjLskbwM9yo-gtVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
با داغ شدن دوباره بحث تخلفات منچسترسیتی پس از برد قاطع این تیم مقابل لیورپول، مروری داشته باشیم بر دیدگاه یورگن کلوپ درباره این پرونده؛ پرونده‌ای که لیورپول و دیگر رقبای سیتی از ذی‌نفعان اصلی اون به شمار میرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/Futball180TV/108657" target="_blank">📅 11:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108656">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbwvOiPXXvkTEkZEYnGmZfxzAJHl1VKtoXFRayKIY-b4749xaSGEGscpWsKAHnIj9jip0j2kNVrT_TRamK-8FiEmiKatWelxD_zS5RvsPdYK8UI2DPRFFZjnvs5yFM05FTaaOsfL58H18TOZhjKofOcISmHORa0H2DCqFuoiZOeS2gRNz87ZxDc29UHBwyGKE-VCC-0ZB0v1p8LIpV-BrjwtmFyKAQxmcmyzfTl7pQHi8VXh31pRI6VezuDt2MwCOIGIDHhQD4SabJVxhEDsz3H0JP2UqtnA9VJzP2qs0uwqaTxQAVji9RlWE1idXnGs5YljoWs3NVnQXy7sEMizjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
براساس آزمایشات اولیسه، رزاقی‌نیا هافبک استقلال بدلیل مصدومیت حدود سه هفته از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/Futball180TV/108656" target="_blank">📅 10:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108655">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9746e98953.mp4?token=CmsXpyEIHkJY5z0ChrKKvoHcUE6lpeHASeI48KMGdHawOsrQYZ6YxsLvfX2E2pCGYPqkhKllp-RO-L9Br8eWPPOdizc9x9Zf79lW-WyZ-utLquW600x8fxS-ZX_OveQnAg5hVDPW2gBoqM48mwb-mIUgazKiJq6-lmJIIR9YC0WErUVs_FUiLnaLqYqCHBSKPWKXPcE864QCUODjgaEFtr6GIERQEK_D744sWjT9RMmwniikHcT_TLPguxZYDT8WgT4o8oJd5EyI-jQ5RlGoYbOHAyk5dqtvD9qEpGR4Ul4rj3qg_8X0HbbUIcnWWKPYsRA0ArEkeaHu9Zy10Z5YGznHQGCwMOZxHsejTLHCHX0iVKpOkIZvZoevSgeCXrqL3Vapq20luXlFx_ESaqgwJ3hEw2J394-ptxBZmuurWktor4aCzQ4yzJ7gb8Es13MX0L9ExYgfx3XCGBLHDV9kyZF9zxH51ytRWZnUhJMVhQUxYlOU7VFkZskJ-rqoeBr0H1We9AANTzQk3WaOekm1uhbOsU5HK5q3ApnDihEV1rjML4zzuZ2j57cuN_CE6pil5iUHux-yIkgdqw70Sq5lF_kqEsLmcsf7oXQ6ayyGfIF6DfUrmEeCMDnDSXoDqOz1Cp19P1eZOXs1KEabnW8pkeGe-XDtlSpdsffhJ8DkNjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9746e98953.mp4?token=CmsXpyEIHkJY5z0ChrKKvoHcUE6lpeHASeI48KMGdHawOsrQYZ6YxsLvfX2E2pCGYPqkhKllp-RO-L9Br8eWPPOdizc9x9Zf79lW-WyZ-utLquW600x8fxS-ZX_OveQnAg5hVDPW2gBoqM48mwb-mIUgazKiJq6-lmJIIR9YC0WErUVs_FUiLnaLqYqCHBSKPWKXPcE864QCUODjgaEFtr6GIERQEK_D744sWjT9RMmwniikHcT_TLPguxZYDT8WgT4o8oJd5EyI-jQ5RlGoYbOHAyk5dqtvD9qEpGR4Ul4rj3qg_8X0HbbUIcnWWKPYsRA0ArEkeaHu9Zy10Z5YGznHQGCwMOZxHsejTLHCHX0iVKpOkIZvZoevSgeCXrqL3Vapq20luXlFx_ESaqgwJ3hEw2J394-ptxBZmuurWktor4aCzQ4yzJ7gb8Es13MX0L9ExYgfx3XCGBLHDV9kyZF9zxH51ytRWZnUhJMVhQUxYlOU7VFkZskJ-rqoeBr0H1We9AANTzQk3WaOekm1uhbOsU5HK5q3ApnDihEV1rjML4zzuZ2j57cuN_CE6pil5iUHux-yIkgdqw70Sq5lF_kqEsLmcsf7oXQ6ayyGfIF6DfUrmEeCMDnDSXoDqOz1Cp19P1eZOXs1KEabnW8pkeGe-XDtlSpdsffhJ8DkNjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
رویانیان مدیرعامل سابق پرسپولیس و رییس پلیس سابق ایران: راه حجاب، گشت ارشاد و برخورد فیزیکی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/Futball180TV/108655" target="_blank">📅 10:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108654">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0060865794.mp4?token=oib_dkmp6cU0wenbgIKAKEd_U24qTW3-ZQbpL2x643gtI0kSlNq0WdwPCI77AAZ70J6iypjmjwR7UoLcrW5ydlGwpwZHbbhwvWPuC8bNyMPsC2Q4iaYiRcMe6WplTGP2Kul_jhhrSHUyxUJ1OPoOGj2B0Kpq0qCu-M-hPu4QPLxQgr2L5ccNMwFf6wen9Q7j4DKSn1k6vvdLE_VFNlvuCRUqD2oMq-CYqlw5cS0pUDgg40dVOZWGOQ6COPzWR3AQroN4hr_9EPWWbwSDSjWJZfVJxtkkkBNjcV-LvonFp8SALzoBuEg5QOnsLxd14CNhIcMU6LJw9MTufb5dJALfUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0060865794.mp4?token=oib_dkmp6cU0wenbgIKAKEd_U24qTW3-ZQbpL2x643gtI0kSlNq0WdwPCI77AAZ70J6iypjmjwR7UoLcrW5ydlGwpwZHbbhwvWPuC8bNyMPsC2Q4iaYiRcMe6WplTGP2Kul_jhhrSHUyxUJ1OPoOGj2B0Kpq0qCu-M-hPu4QPLxQgr2L5ccNMwFf6wen9Q7j4DKSn1k6vvdLE_VFNlvuCRUqD2oMq-CYqlw5cS0pUDgg40dVOZWGOQ6COPzWR3AQroN4hr_9EPWWbwSDSjWJZfVJxtkkkBNjcV-LvonFp8SALzoBuEg5QOnsLxd14CNhIcMU6LJw9MTufb5dJALfUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشتِ احتمالی ستاره های منچسترسیتی در صورتِ سقوط این تیم.
😕
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/Futball180TV/108654" target="_blank">📅 09:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108653">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1661f71c8.mp4?token=ToQHgdsnlfLF9dehkTEytlMXF8Prg-B1Cpw7vDLk3VtTxP-Zm8TFJXRbKiFhTvTWo-7I68T4eFkFRZT9OkgQ1q2Sz82v0hI4dpptMExH7fe9wVYrpD1fkqxDYkJwTXRKrcjI71aABYCoVWvR0DdOrnu13pLwnIyLFVQSzIHSZhfDIy4d1WhLGpEhFERTqOpdTrxOUi3WfsLEBy2NtAg5aEw-I5VDg9Tg3tE-KLdG6Gn3NIsXYhXfiyBBb4OCZGz5CmTomaPmZAyouorgJj5lFgxmTfjV9Our7CrNo8T2yRfSXopi8YqJqGRINvL_vX-3da6H5mg_hsUp89UHBKV1eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1661f71c8.mp4?token=ToQHgdsnlfLF9dehkTEytlMXF8Prg-B1Cpw7vDLk3VtTxP-Zm8TFJXRbKiFhTvTWo-7I68T4eFkFRZT9OkgQ1q2Sz82v0hI4dpptMExH7fe9wVYrpD1fkqxDYkJwTXRKrcjI71aABYCoVWvR0DdOrnu13pLwnIyLFVQSzIHSZhfDIy4d1WhLGpEhFERTqOpdTrxOUi3WfsLEBy2NtAg5aEw-I5VDg9Tg3tE-KLdG6Gn3NIsXYhXfiyBBb4OCZGz5CmTomaPmZAyouorgJj5lFgxmTfjV9Our7CrNo8T2yRfSXopi8YqJqGRINvL_vX-3da6H5mg_hsUp89UHBKV1eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سامسونگ هم داره آیفون می‌سازه؟!
👀
🔥
طبق کانسپت‌ها و شایعات جدید، گلکسی S27 Ultra ممکنه یکی از بزرگ‌ترین تغییرات طراحیچند سال اخیر سامسونگ رو تجربه کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/Futball180TV/108653" target="_blank">📅 09:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1136457e.mp4?token=TA1WQEjQ-FlUIc5sKTbNeq6u8DgQo7W5Ne603_ypc_4Ut-TUTzq5OR21q_frfkewpg6m5IvaRflJ9AhnoIXp-bLGA3BomQFuZFOVVjZFZDfZkiYU92T-CNf_yEFJ78CQ7m7x1laTob5uOfXJtrYEy0XvuuWfH4Jo-G7a4C_MvQgPHx8hOXSxMjdP3qnm1oIDK6eemeHmQkiq2X8Ee4X3ovlK6ANQA2OkgYFMPziwxtltHo9eABgwc38kjxZ5hcu5Bii5Zy0kIYBIM9-V3wENvc8NVkQgkUNnGK_-QUrzY0KLzpRfyYq0d2MjQc6LtPGkyDjovWnhZeLli03ExNF8c1GSCBxmr1Ewcb_Y4N9LdhgPUPohZrqmBGphLW6btTD1oYxvb8xEoBoz5YOFsc3orb9q88Oa6Ju12OmQVOLeNf35aOCa15KVN_7DoN4Q3EghImxHQ_zbJKaNOUZ4nq5Kl3CSESfVe-PvV1iQA0FAVH-8vaLPKnB18OBhdd5_4kMeq-M6nzeA5eJpfyHra6coNKPHGfC5ZGw0jLHuiZE1TMUytgrDs8pTfCd7Mm10IxgnY2bz0pTzPwqeRiFghq7XthfrQSQZuHRoN1vI6KQIaMXe5qT7DYo6TCzHIcOZLqVj1UtAJ-THeYGT1TP_9Y_aeJfMvH8NrdFaNOELC74uADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1136457e.mp4?token=TA1WQEjQ-FlUIc5sKTbNeq6u8DgQo7W5Ne603_ypc_4Ut-TUTzq5OR21q_frfkewpg6m5IvaRflJ9AhnoIXp-bLGA3BomQFuZFOVVjZFZDfZkiYU92T-CNf_yEFJ78CQ7m7x1laTob5uOfXJtrYEy0XvuuWfH4Jo-G7a4C_MvQgPHx8hOXSxMjdP3qnm1oIDK6eemeHmQkiq2X8Ee4X3ovlK6ANQA2OkgYFMPziwxtltHo9eABgwc38kjxZ5hcu5Bii5Zy0kIYBIM9-V3wENvc8NVkQgkUNnGK_-QUrzY0KLzpRfyYq0d2MjQc6LtPGkyDjovWnhZeLli03ExNF8c1GSCBxmr1Ewcb_Y4N9LdhgPUPohZrqmBGphLW6btTD1oYxvb8xEoBoz5YOFsc3orb9q88Oa6Ju12OmQVOLeNf35aOCa15KVN_7DoN4Q3EghImxHQ_zbJKaNOUZ4nq5Kl3CSESfVe-PvV1iQA0FAVH-8vaLPKnB18OBhdd5_4kMeq-M6nzeA5eJpfyHra6coNKPHGfC5ZGw0jLHuiZE1TMUytgrDs8pTfCd7Mm10IxgnY2bz0pTzPwqeRiFghq7XthfrQSQZuHRoN1vI6KQIaMXe5qT7DYo6TCzHIcOZLqVj1UtAJ-THeYGT1TP_9Y_aeJfMvH8NrdFaNOELC74uADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
آنالیز تاکتیک جذاب این‌فصل آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/Futball180TV/108652" target="_blank">📅 09:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f591d52518.mp4?token=FfL7zgWiZAwMi0pEUWPL1jW9Nl8Zu35X3cHZJtqzQRqGV-o41hNfdQE32Wxrc8NfWFVmkdJy1iEJa09bfF7T8O9njlxBOkuVVncdFZgSuBCzWkL2ZTA7JEdvSgH6OikJ5I9IeHXrjU7lrVwPCDuNlegkAQrmP8-6V9fB7zyQM1Fo7FIjXpMHQRatHmA-PzRZsmim52-wuV5UNNr8YLDUZfSVXy8llbgAT3tBfanwNP7prDE05Qxi0UQR084_8LXMeDdFcxCRoOapYvKR6XrDCMe3f8_Q6qRoulMngPXz1bZeIgwilpu4-1LG0HF-evi8tH4ClQXgNBbeSl00kXw7Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f591d52518.mp4?token=FfL7zgWiZAwMi0pEUWPL1jW9Nl8Zu35X3cHZJtqzQRqGV-o41hNfdQE32Wxrc8NfWFVmkdJy1iEJa09bfF7T8O9njlxBOkuVVncdFZgSuBCzWkL2ZTA7JEdvSgH6OikJ5I9IeHXrjU7lrVwPCDuNlegkAQrmP8-6V9fB7zyQM1Fo7FIjXpMHQRatHmA-PzRZsmim52-wuV5UNNr8YLDUZfSVXy8llbgAT3tBfanwNP7prDE05Qxi0UQR084_8LXMeDdFcxCRoOapYvKR6XrDCMe3f8_Q6qRoulMngPXz1bZeIgwilpu4-1LG0HF-evi8tH4ClQXgNBbeSl00kXw7Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مرور خاطره گل عقربی اولیویه ژیرو به کریستال پالاس، با بازگشت اسطوره به امارات⁣
ژیرو: من آدم متواضعی هستم و اشتباه برداشت نکنید، اما فکر نکنم دیگه مثلش رو ببینید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/Futball180TV/108651" target="_blank">📅 08:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108650" target="_blank">📅 01:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q9Xp9ZCFkMMFSyjNT1snvDM76XMThrv0bz9EEOnnq6jRkgL8V_2OhkmKDDdJPZd5mGcSVlrMfkg47TMnY6MUFlMpd48cPuSPFcxZd2P0HkqVUxFvBhELXYgBqiwyyL6P1AMqyqMsMpiufUQfJqhKHH6OoIDzmYR671rV_nLz2mgyPtHKlui3cQyn4_SEO0jbWHBvkApAsNtBLqNkv4NBswO0tkcPhEv2FpnhSK8pGtBVvJ1SeIKd1NlDCc3AGqqf7DEPbXmm2Dx5DIOiJe8NRd-0_Mv9YFHbVK5OyNuq9jLD5tGzXw417OGUFtM0Mzkfam9HBPs7L2LlInKzKKdBYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108649" target="_blank">📅 01:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108648">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108648" target="_blank">📅 01:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umsottd_yq9PLsI2BmyNIcj_dwqu8GQOL7Sp_Z1uhWRRRJBpaQVlKZ5eVCHI_82ziszezUHot4eENmt6n1IK0U2l3uSSkqSizVKLvq_gyQBcl2ykN0QnlQookB6Msy7jTVWy-pFlDI9qLXFoZniu_i9A1KXOq9RvekzV5ewU291fS-QSSGuIX4W7xGsNGpxgEExvmjD7TUUTe6g8uK_G3hjNiw9M6fDVQLuxaNHk-Zy3ncB8Hts6_yf4uV_ivJqTFINLXMHjDdB49h1B97h7cCn0J0PxZuKh5pyYSF4vKKYoACXhBl6zvzILPZklCBT4-y6fCZNH52GNzHMJxgVwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🏆
هفته‌دوم لیگ‌قهرمانان اروپا؛ دهمین برد در دهمین بازی فصل؛ جهنم استانبول هم مانع پیروزی پرگل شاگردان فلیک نشد
🇪🇸
بارسلونا
😀
-
😃
گالاتاسرای
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108647" target="_blank">📅 00:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDhyz7jYl0odsp3u_Bl_U3h4p9AhtOgRSsk25Iw-E4kzh508EB1DPyg0YnvT3q3uIDbMgebbX9-bhKE5rGqOtsxNcIydK9P-o6aW7-bVwRoDfzYfWv-ZzkfZ_Q9xCHB-yPZmMmKLZuE_XKc8bA0d6Tl3hOoRxjF2uEfxMBhdKf9bXhdn8FGlFoHN-5oAp14JpL-FqTRqYFmtD_DHtutNrxy3O7GcsZyBFVS7uwYTz14WDpP-r7CdoA6mOz_CtNgRmADlnRJJPq_64NtjADLqWk8qPcIM9A5wxeJPGNKbYt-7jbQbL2H4AIoiAnHkdLmsMv-CznggoNRI-IkiYG6SMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108646" target="_blank">📅 00:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOEDo-mtGJSux_gGu1mY6UsQsZw6JwAkNQYjtgqss52y1pRKosPWQPZL1Qtg51JsH2LSNSN6FO5-QVcqLBWDEiJphjE_mpH_qYqhYz3knoHCwClrATSmOxHqRabl9qk8a0ELNTFc9LoygwNJw4rNxZEYzv8s2C-gLvWrvCBl1Ip_EegGWrm9C6Yvs7wHUUzClnYaNQ5XT7KRFoC3G827upBCFe3PoXZKh_mC72hrrM5hudC_kaShel2-4Q-pIg7wxTamzAkT9eWkIjozEdkP-sU7DsHXNOJqED8y0qBQ3-4g0QWB8hrbGSi1EcN3-UFsTMR_L0Vafmuk793GYDPFWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
لیگ قهرمانان اروپا | در همان ثانیه‌های ابتدایی غافلگیر شدند؛ وضعیت کریک در منچستریونایتد بحرانی شد
🇪🇸
اتلتیکومادرید
😀
-
😏
منچستریونایتد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/108645" target="_blank">📅 00:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk72JtSFBnmotXM4RxiqNO71kmhhyMiQBM3hsgAEv0syWEvGOSqu_OUtQev7aK_ABmrV0x6G2JOgCSpwkyOlfzWfIA71YPlAJXxgoKhCXnmN6K4idWywRnDnvFTE1vUbz-tnfy9c_9G0rWuZbnbPHhXeEU9MxJ5nkRqwKWhcbZvzeAIVmSlzJH0R_qv2zPpefUJcy7ViOoX41-ceYvXmRUejfd7Ym3pGcaNR7GOmuQGECzXmEy_rzuWABQPkbGtddy59uBXMJnfh-gzemp_h0JU1_YYCXAbTsZ1kaEKuoCe2-uPjjfACaKuH_T2yfYtEE4GOTxxipiTspqObnfEJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
لیگ قهرمانان اروپا | تساوی دور از انتظار بایرن‌مونیخ مقابل نماینده نروژ؛ توقف شاگردان کمپانی در دیداری جذاب
🇳🇴
وایکینگ
😆
-
😆
بایرن‌مونیخ
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/108644" target="_blank">📅 00:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKwDeJ77CXYpFwzmH7NCv53ytCmruglOQyQHATOcelMzlElhlBLBfGQczbJ8qAE5fSaI_ivBt5wpG4hpkapKnm4Tw8lqLns6HV6GpJ_sNw4ASAGBJxoQBc80RnUP99GcxKT9EdKsSV-UpkoHPiOIoeLzbMq3cH27VKcFM0uNOM6JrbnflNIPJYn7b92NZ00JB20WtHeFZK-Z12EbvAvxF_hk-HHhvWVLo7R4sReqAOjGvKof3_7wzaTFlZI1IZ0tgSSjAm5PH0awiW4-Edu7Fg4XQM4WXcBxdtywY2veqeL3AA3PC93IJ4I1_rBAjqu0e2AVtIsec-hqyRi_Qbu7Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🏆
هفته‌دوم لیگ‌قهرمانان اروپا؛ دهمین برد در دهمین بازی فصل؛ جهنم استانبول هم مانع پیروزی پرگل شاگردان فلیک نشد
🇪🇸
بارسلونا
😀
-
😃
گالاتاسرای
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/108643" target="_blank">📅 00:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/def4417737.mp4?token=oPkUa_DQt-FlPRzp8p9ZioCEgKUez70GReE0XUUTQJgyFJ_xQelSdH_FHeD3-Cr19bouL0A2k-KGoyZEUSeTWR8mrINrkmAlazKH_UwpTfvu4EVNgJUjfv7FDWSmmheimNXffoslhs43nIYIMixBlFyJWN-B0ANk_ogFvbS7-cpbJOFvgKCQJlB77neYIY8boIOEryrze7xJgObNS8qQK-wdzQ_q24v-t-TpheL8QT_chyEQYRQUzOt_44oVxKMT7u_znVjUgxV-u7NHNYJ0Sjmtm0uMH4mLnZZ4KswZ-qt3hCF6kwNA1EooYTi_aCWSlVSpNHrkT9IXg_4BYvE7KLXP1oABE24ImzQedoktiVxIt0ua4TN9TlzyYDijuB_gpTaaceLD4Sf8HRkFFXiOxdIn6WFQfy4Mz1tTvKz4J1yKnFcZShFMeha_BTGGcp4nLoeufUXNSZhV69a7Is-XefBX4Y_rz1XrHXww46lXXsaEcHaONu98y4yK1ehJ_uLmz8SWc58QhvF8TNxAbUuPYeiL1fS9hO8vSeNMBNYctU96OJEj08sLFcez9mMEaAnt9TCAMY9HM3P5UjlVVgGrdJCvSZcXs_ly3AWTv0xXVk-h9qLCuEAWgK2qEsqW1w8chuo8Ogjx1XFd7yROCFftT6K8YwZ6UGNUepdHH8W0Gw4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/def4417737.mp4?token=oPkUa_DQt-FlPRzp8p9ZioCEgKUez70GReE0XUUTQJgyFJ_xQelSdH_FHeD3-Cr19bouL0A2k-KGoyZEUSeTWR8mrINrkmAlazKH_UwpTfvu4EVNgJUjfv7FDWSmmheimNXffoslhs43nIYIMixBlFyJWN-B0ANk_ogFvbS7-cpbJOFvgKCQJlB77neYIY8boIOEryrze7xJgObNS8qQK-wdzQ_q24v-t-TpheL8QT_chyEQYRQUzOt_44oVxKMT7u_znVjUgxV-u7NHNYJ0Sjmtm0uMH4mLnZZ4KswZ-qt3hCF6kwNA1EooYTi_aCWSlVSpNHrkT9IXg_4BYvE7KLXP1oABE24ImzQedoktiVxIt0ua4TN9TlzyYDijuB_gpTaaceLD4Sf8HRkFFXiOxdIn6WFQfy4Mz1tTvKz4J1yKnFcZShFMeha_BTGGcp4nLoeufUXNSZhV69a7Is-XefBX4Y_rz1XrHXww46lXXsaEcHaONu98y4yK1ehJ_uLmz8SWc58QhvF8TNxAbUuPYeiL1fS9hO8vSeNMBNYctU96OJEj08sLFcez9mMEaAnt9TCAMY9HM3P5UjlVVgGrdJCvSZcXs_ly3AWTv0xXVk-h9qLCuEAWgK2qEsqW1w8chuo8Ogjx1XFd7yROCFftT6K8YwZ6UGNUepdHH8W0Gw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بایرن‌مونیخ به وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/108642" target="_blank">📅 00:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108641">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گلگلگل سوم وایکینگ‌ها به بایرن‌مونیخ</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/108641" target="_blank">📅 00:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108640">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdfe06f9c.mp4?token=TXBLzMOoE3jdWlPwbhSJz1ED_FSZ_c3FeOsdItl92gEEvNYXYDHCFNiq_S9_pe7UDRYlOSxAG2qKX4P3zYzmc1mJ7ZImPV29hPb5rjote-TDW2iV2n1xOUo_5f5kCz0pSICkK914l0Fd9mTW6byEr_DmXaeSHcLhIHZFWgdOdn-EzZMOnG_OtfikYHqN3bPuxKbqppa_arCv427Rw6F5U1CSZm2rO_zrH7VRuBBR0oNj09BWGGZGZ5NSBcpe7Vxv0w-EjOl2XKDRKFCMKj-RIdx6DMZ7BCmCJkvYqgVa6sVjngvVL-ht1OBNPHT-Vz1g8H3je2bR0z9IFveHuYqRFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdfe06f9c.mp4?token=TXBLzMOoE3jdWlPwbhSJz1ED_FSZ_c3FeOsdItl92gEEvNYXYDHCFNiq_S9_pe7UDRYlOSxAG2qKX4P3zYzmc1mJ7ZImPV29hPb5rjote-TDW2iV2n1xOUo_5f5kCz0pSICkK914l0Fd9mTW6byEr_DmXaeSHcLhIHZFWgdOdn-EzZMOnG_OtfikYHqN3bPuxKbqppa_arCv427Rw6F5U1CSZm2rO_zrH7VRuBBR0oNj09BWGGZGZ5NSBcpe7Vxv0w-EjOl2XKDRKFCMKj-RIdx6DMZ7BCmCJkvYqgVa6sVjngvVL-ht1OBNPHT-Vz1g8H3je2bR0z9IFveHuYqRFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم اتلتیکو مادرید به منچستر توسط لوکمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108640" target="_blank">📅 00:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108639">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلگلگگلگلگلگلگ اتلتیکومادرید دومیو زددددد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108639" target="_blank">📅 00:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108638">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d76e2a5b60.mp4?token=MzHsEGS4MkDqSPF76hr1GMaP-_sFxx0XwVlH9hAYoKSQtlKl13MxruUfihUNM0zApKnxnfWqT-QyTa2cnrs0y6uwKL0GQiZXvc4fxkDypeUAUbWmTdt2IVaV5FxcTFeVF5S61bAe6mnKbtbWjPW7kmWVBZEnkVvdwbaRedRCZP_tujvC8QBZU2ggcoQ9ZIXujUdZ5JS6L0OJrgDMqJKFJB_WMG5r3Xnry0FyfdN-c28rXNGqFZXiyIVzX0s-4pirFc6U-WqiD58-xu2MB7VmL15zmp1Y8kD5R36wFbhUV4_jWepvr7A9_SWBMD172yy1e0pX6AK3MnWqomoZMDOLwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d76e2a5b60.mp4?token=MzHsEGS4MkDqSPF76hr1GMaP-_sFxx0XwVlH9hAYoKSQtlKl13MxruUfihUNM0zApKnxnfWqT-QyTa2cnrs0y6uwKL0GQiZXvc4fxkDypeUAUbWmTdt2IVaV5FxcTFeVF5S61bAe6mnKbtbWjPW7kmWVBZEnkVvdwbaRedRCZP_tujvC8QBZU2ggcoQ9ZIXujUdZ5JS6L0OJrgDMqJKFJB_WMG5r3Xnry0FyfdN-c28rXNGqFZXiyIVzX0s-4pirFc6U-WqiD58-xu2MB7VmL15zmp1Y8kD5R36wFbhUV4_jWepvr7A9_SWBMD172yy1e0pX6AK3MnWqomoZMDOLwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بایرن‌مونیخ توسط لوئیز دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/108638" target="_blank">📅 00:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108637">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🟥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لنی‌یورو جلو اتلتیکومادرید اخراج شد</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108637" target="_blank">📅 00:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108636">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🟥
🇩🇪
مایکل اولیسه بدلیل دریافت کارت قرمز بازی هفته بعدی مقابل آرسنال رو از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/108636" target="_blank">📅 00:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108635">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گلگلگلگلگگلگلگل سوم بایرن مونیخ به وایکینگ‌ها</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108635" target="_blank">📅 00:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108634">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b2a48903.mp4?token=o3HcMvOgCAaxhCuibBPndT4r-nOzVWm7buwshPpUhX96JVv_IFhDjV9BFJsY_536Cc5ERIoIfQOR29wCqcFpTWVZQ6nmm5u1jiUpZ7pk-lE9ZoRu5_0ASZdYI3e_Xksi7kNqLkuj4_K_VGKzL7iJnrZG0iezQYqUsJUf9bPVZNA8vIYh9u8xGVPPzwOy1R6b2auhTV7RZVi58CVnY8SfwxaILJs2QtIC_bajBW4Qe-gk1NpRG0gMLQeMu9CVNKnJp4UH8r6LqWCi6h5_zrYuWh5T_ugORi1pve70lff68xw-OY0tUNvYFDuDlMwnsBnppcysik-YV-wtAbBSBe8s-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b2a48903.mp4?token=o3HcMvOgCAaxhCuibBPndT4r-nOzVWm7buwshPpUhX96JVv_IFhDjV9BFJsY_536Cc5ERIoIfQOR29wCqcFpTWVZQ6nmm5u1jiUpZ7pk-lE9ZoRu5_0ASZdYI3e_Xksi7kNqLkuj4_K_VGKzL7iJnrZG0iezQYqUsJUf9bPVZNA8vIYh9u8xGVPPzwOy1R6b2auhTV7RZVi58CVnY8SfwxaILJs2QtIC_bajBW4Qe-gk1NpRG0gMLQeMu9CVNKnJp4UH8r6LqWCi6h5_zrYuWh5T_ugORi1pve70lff68xw-OY0tUNvYFDuDlMwnsBnppcysik-YV-wtAbBSBe8s-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌چهارم بارسلونا به گالاتاسرای توسط آدیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/108634" target="_blank">📅 23:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108633">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگلگگلگل سوم آرسنال به لیل</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108633" target="_blank">📅 23:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108632">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پاس گل از گابریل ژسوس
🔥
🔥
🔥
😂</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108632" target="_blank">📅 23:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108631">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گل زیبای کریم آدیمیییییییییییی</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108631" target="_blank">📅 23:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108630">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گلگگلگلگلگلگگلگلگل چهارم بارساااااا</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108630" target="_blank">📅 23:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108629">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگگلگلگل دوم آرسنال به لیل</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/108629" target="_blank">📅 23:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108628">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeoZSwv2hzf9q7CyyL0f3aF_blvsDhmYwKyTPgqfJjhfQ-LMlS7XI6hhzo8y5ty3oVVvqnaLolRMUI13pJ4-wHB1GumFjYouXz73YdW6RV3IeQS7ysD_-KrhB1WD8b5no8BVO-sKVzxncDXAuw_PGnWCBGYqmI9zTgmhlpsF5Rl2QXVZOcClPx9P24BrOuwLjHrbnk3ZYIXPXwaL2gpdpySasjdfnFJOCO8amvH380ZdGQPEPYlt51533aPlx2AKTYpSqzCMz61xVoGj__5T-ixlvsAwyX1Elx3DMiVFIcPLD8TsigqUqIO966t5uLZioKkobyUZdXvzLkpibAk_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
▶️
🇪🇺
نتایج بازی‌های تا این لحظه</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/108628" target="_blank">📅 23:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108627">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگگلگلگل آرسنال یکی به لیل زددددد</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108627" target="_blank">📅 23:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108626">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf53f669cc.mp4?token=DEpXi532pjSlesqTsmxhyhUlZEQ6655KFqljxNlg4Mj7Xc55fxBgsjIW1ZuDqhGrtAohhqfPHvXhXxvGUgPzim082HKTlcvjccLUDk2zD2mu3h5NtLl5FH4PPsorpb9yVIB91kvDFPn4-zjZIVaRhu1QTuTu6EvW4_SzDqnVnOYnphm0x7g9lbZ90Z2VoD5ZB1_VWPjzO_I14XHXrSKBh_qbwJ3I4hyjcsmmRVDn76t5_w3bIX_ToxKwVU4xKnA2fa37JxvisLLm7JVZd29J3rLBDIe4Z5ZNK4w8p3kNvMrVqUZA05e36RSPKDz81aYuHfS0mDUsRqn-H-R2rUZOg3bJ1DfPnLcYCHwAxdP8CVr7o2Un8B9UGG-AwHCK1Bo8cEzo-nrgDMf7s1PYwX9FfJCXpPZwloe4FctLZXPArF2uQRDvLVuVFXh5jNZ9e5BhtS2I0UCdvdLcqJR5OKhehXPEbdifcBWPUIxTcuWnQg6tUPwuyGJdqXjDI5MSVYjW5YojMdFwwqsdWoMY8UCaMkC6KzmeTYfIk9uztbAtdTA0EwleVy0NVeHdRQ6Xyt4RgxB1p0n3anrRngujsSLwH-gNk4hCgc2I6hK0k1qV2yfkAP84sPoeQdixaZhtRRJQLAWh6QSw6vV3xbEmxMLp0P-ZLB0SiTmY82zTHP7kRJU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf53f669cc.mp4?token=DEpXi532pjSlesqTsmxhyhUlZEQ6655KFqljxNlg4Mj7Xc55fxBgsjIW1ZuDqhGrtAohhqfPHvXhXxvGUgPzim082HKTlcvjccLUDk2zD2mu3h5NtLl5FH4PPsorpb9yVIB91kvDFPn4-zjZIVaRhu1QTuTu6EvW4_SzDqnVnOYnphm0x7g9lbZ90Z2VoD5ZB1_VWPjzO_I14XHXrSKBh_qbwJ3I4hyjcsmmRVDn76t5_w3bIX_ToxKwVU4xKnA2fa37JxvisLLm7JVZd29J3rLBDIe4Z5ZNK4w8p3kNvMrVqUZA05e36RSPKDz81aYuHfS0mDUsRqn-H-R2rUZOg3bJ1DfPnLcYCHwAxdP8CVr7o2Un8B9UGG-AwHCK1Bo8cEzo-nrgDMf7s1PYwX9FfJCXpPZwloe4FctLZXPArF2uQRDvLVuVFXh5jNZ9e5BhtS2I0UCdvdLcqJR5OKhehXPEbdifcBWPUIxTcuWnQg6tUPwuyGJdqXjDI5MSVYjW5YojMdFwwqsdWoMY8UCaMkC6KzmeTYfIk9uztbAtdTA0EwleVy0NVeHdRQ6Xyt4RgxB1p0n3anrRngujsSLwH-gNk4hCgc2I6hK0k1qV2yfkAP84sPoeQdixaZhtRRJQLAWh6QSw6vV3xbEmxMLp0P-ZLB0SiTmY82zTHP7kRJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی بایرن‌مونیخ به وایکینگ‌ها هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/108626" target="_blank">📅 23:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108625">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">لوووووویز دیازززززززز</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/108625" target="_blank">📅 23:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108624">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">لوووووویز دیازززززززز</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108624" target="_blank">📅 23:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108623">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلگلگگلگلگلگلگلگ سوم بایرن‌مونیخ</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108623" target="_blank">📅 23:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108622">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هری کین دبل کرددددددد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108622" target="_blank">📅 23:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108621">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بایرن‌مونیخ مساویووووو زددددددد</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108621" target="_blank">📅 23:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108620">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلگلگلگگلگلگلگلگگل</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108620" target="_blank">📅 23:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108619">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/93ba7eabbb.mp4?token=jzi8ZMA0-cVCVrHswgu35PWwC-B1lM0BgltlL4ulpmepDzOjzJ-TPhw9gsI0ej98CCR1qpML_qXT9BQsh0_RwiJYynnF63k0RZfJkEMzjAev47iyG8eUG62lsCW2s-QqkrmYfLLa3uD1a7qQTTkQIoQB6Uke967DmULCmxaCipbhpp463DJyqSCgZBML-Lw3ri-OGBiiiqmWlxpm_Q8kNHa4eCMcVTV7pQQ8K6KG3ycudOziFZRqHpnEl11k2IAaUEg0bJ0BpebwfFFG4RXmDah4d-jTHv48Wch347MWR-QbnjZQwlfGFlZFsb9GWf2pska9-m-mNjWtiG463k-Uj45Xo0YMGDQZjALIWeJShb3Y3jTxUzRs4PnsF08w9XnuaCf6dzPdnW8IpfI73kJqP92yagarCGTWN_fIlFHevQ8XLGC3SZq7lSLNsffNP3faqItIu59eJixsGL3GHjrDmKh3kCvo9gq8za8Fr1TCM2fAh_h2UeDCpLR09JcBSlqWsHC0gSaPsjpqw8gVclMtkzpebolCADyBGJh8dLSDbLWF1WkyGmBST-65aZiPRhYhqgV8wQt-CYKjPLH1L77c0lGfVZsvuMHKbam3vOoKa-vIgJbUrcML_RssGmLgM4Kr9bhoTVFQvt2KbCIXYzUCDNhOPKP5Atnq6SmEkEDZGnU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/93ba7eabbb.mp4?token=jzi8ZMA0-cVCVrHswgu35PWwC-B1lM0BgltlL4ulpmepDzOjzJ-TPhw9gsI0ej98CCR1qpML_qXT9BQsh0_RwiJYynnF63k0RZfJkEMzjAev47iyG8eUG62lsCW2s-QqkrmYfLLa3uD1a7qQTTkQIoQB6Uke967DmULCmxaCipbhpp463DJyqSCgZBML-Lw3ri-OGBiiiqmWlxpm_Q8kNHa4eCMcVTV7pQQ8K6KG3ycudOziFZRqHpnEl11k2IAaUEg0bJ0BpebwfFFG4RXmDah4d-jTHv48Wch347MWR-QbnjZQwlfGFlZFsb9GWf2pska9-m-mNjWtiG463k-Uj45Xo0YMGDQZjALIWeJShb3Y3jTxUzRs4PnsF08w9XnuaCf6dzPdnW8IpfI73kJqP92yagarCGTWN_fIlFHevQ8XLGC3SZq7lSLNsffNP3faqItIu59eJixsGL3GHjrDmKh3kCvo9gq8za8Fr1TCM2fAh_h2UeDCpLR09JcBSlqWsHC0gSaPsjpqw8gVclMtkzpebolCADyBGJh8dLSDbLWF1WkyGmBST-65aZiPRhYhqgV8wQt-CYKjPLH1L77c0lGfVZsvuMHKbam3vOoKa-vIgJbUrcML_RssGmLgM4Kr9bhoTVFQvt2KbCIXYzUCDNhOPKP5Atnq6SmEkEDZGnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول بایرن‌مونیخ به وایکینگ‌ها توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/108619" target="_blank">📅 23:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108618">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c86178bbb0.mp4?token=bs6uJ4WNEGSUI7OPcie2Rqr2vAvDjGb-mHIozxTIErCVwPH3vON5gfSxTzyBgu_IpbnHGe6XxQ7qC-gEcYryYPSpeJZlESo_hrYDMtVeB-wawczW3I1Q52M6vzGqZMnmjuLUEmb-lx_U4dbVQwifksopkzWE_caN0FMDAwzfpuP5bNNKYWdhBJ1bgSn_OZCGnJKo9L6DkqQ0N13qAnQj9oECstKkRDpzWI6I5O4Czy78MKUwdduJracgsN6ZnIE5meMgUDtyR6nAlcSXQSg2gTZTv4TX3JAlJ7Rc0OfHzyUdRoDEMFAG02h-sxG2Gh8SwGpuoj84wt-vLKQEhVfT-Sqvn_SSqzzBZZBxTDi5LreroUiPaeWFIN1ytgzFofwADFiTr-Zmx4KunxZe7pEwrwGHNCZ31Trcw2aduZmWyECLSiuXd7YAsCIMPQiS_D_gLqEPOVadeUO4J9sA9NPMcMlCGCiSc3yNnRFhPD_bJ_zdZKu8cGj7tfIOcej1U-Lg_2rThQOzyzmhkPvBCs3X_lqv8Cqw5Umq7fY6MMlUfL9B8AjVb97f8zY5jNjAdmVTsRACc4fUaZ1M7xU8itl57Ebi80KaAKbW9C9i1ZmHWFz7v4YbUN5AQ3hxN9istD7WoZ7ETCl-FtMqUglV-IWIqf9MkaXqt726LmcEJEujg48" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c86178bbb0.mp4?token=bs6uJ4WNEGSUI7OPcie2Rqr2vAvDjGb-mHIozxTIErCVwPH3vON5gfSxTzyBgu_IpbnHGe6XxQ7qC-gEcYryYPSpeJZlESo_hrYDMtVeB-wawczW3I1Q52M6vzGqZMnmjuLUEmb-lx_U4dbVQwifksopkzWE_caN0FMDAwzfpuP5bNNKYWdhBJ1bgSn_OZCGnJKo9L6DkqQ0N13qAnQj9oECstKkRDpzWI6I5O4Czy78MKUwdduJracgsN6ZnIE5meMgUDtyR6nAlcSXQSg2gTZTv4TX3JAlJ7Rc0OfHzyUdRoDEMFAG02h-sxG2Gh8SwGpuoj84wt-vLKQEhVfT-Sqvn_SSqzzBZZBxTDi5LreroUiPaeWFIN1ytgzFofwADFiTr-Zmx4KunxZe7pEwrwGHNCZ31Trcw2aduZmWyECLSiuXd7YAsCIMPQiS_D_gLqEPOVadeUO4J9sA9NPMcMlCGCiSc3yNnRFhPD_bJ_zdZKu8cGj7tfIOcej1U-Lg_2rThQOzyzmhkPvBCs3X_lqv8Cqw5Umq7fY6MMlUfL9B8AjVb97f8zY5jNjAdmVTsRACc4fUaZ1M7xU8itl57Ebi80KaAKbW9C9i1ZmHWFz7v4YbUN5AQ3hxN9istD7WoZ7ETCl-FtMqUglV-IWIqf9MkaXqt726LmcEJEujg48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌سوم بارسلونا به گالاتاسرای توسط گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/108618" target="_blank">📅 23:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108617">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c2159385.mp4?token=kzJDp11S8lTGILVIei4WUaH9fZmZz_Y_KrKAAHSDW1qtx0DzDPGUmUwjXoIKBKBIa154wfnLJfRWuvm6MhvDLJcR8DHJLUkCKLcgHIHAU43Ba7Ni37Lb70yiMtUsKSWf74iqeBQjSygniXl4gPW76TnltpF0QC8UaWjt5O6Aslt-o4yqAiNrB5BRbzKsRhjm8cLouSs1lyfNSQgjC7JpqLallaG2DrS76ngwZLqH0B6mB_zf6_HT4_aswL5zk4P_fNAGyhq_YYhGxFZkr8lM6pXpB40AMSXc7ASqguDb78iutmgXIYmVsiHWAaxQ65Ybll0u-YQ2MP3tPtQ7o4Krzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c2159385.mp4?token=kzJDp11S8lTGILVIei4WUaH9fZmZz_Y_KrKAAHSDW1qtx0DzDPGUmUwjXoIKBKBIa154wfnLJfRWuvm6MhvDLJcR8DHJLUkCKLcgHIHAU43Ba7Ni37Lb70yiMtUsKSWf74iqeBQjSygniXl4gPW76TnltpF0QC8UaWjt5O6Aslt-o4yqAiNrB5BRbzKsRhjm8cLouSs1lyfNSQgjC7JpqLallaG2DrS76ngwZLqH0B6mB_zf6_HT4_aswL5zk4P_fNAGyhq_YYhGxFZkr8lM6pXpB40AMSXc7ASqguDb78iutmgXIYmVsiHWAaxQ65Ybll0u-YQ2MP3tPtQ7o4Krzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم بارسلونا به گالاتاسرای توسط لوپز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/108617" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108616">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سوپر دریبل و حرکت فوق‌العاده یامال فقط
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108616" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108615">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آنتونی گوردون</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/108615" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108614">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بارسلوناااااااا</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/108614" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108613">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگ سوووووووم</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108613" target="_blank">📅 23:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108612">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلگلگگلگلگگگل بایرن‌مونیخ یکی زد هری کین</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108612" target="_blank">📅 23:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108610">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سوپر پاس گل لامین‌یامال
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108610" target="_blank">📅 23:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108609">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فرمین لوووووپزززززز</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108609" target="_blank">📅 23:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108608">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108608" target="_blank">📅 23:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108607">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گوردون دروازه خالی زد بیرون
😂
😂
😂
😂
😳</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/108607" target="_blank">📅 23:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108606">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSuQO8bpxeoPbyVEY26dy4ec3XjW2duChquyk954lseqRuMWsYTZmLgp3nu2AqVqFBzhAGfGcZTDFSRAX7MDn56UdgxZA90eIBFvdgqjTU4NbGL1oua43WJkUz_QhxeD6Gxlu8MGnVXrp5HVXVaqBRfAme2voJYUx6cDwoITVWhM_BCI9LMrPBlQJy_DQWgnHU6HdpR5h8ZW01VHr7hLzZYs3fApiyaA5ZrOVzs3-8czpsgpDFAxGPcc9HX39pcL6Kz2KETUTriMfk1yMK9m_o_K_X1oT-yLowv7LT2t4SuLpEwuo6eRRdh6V03pDdxk_xwFOYm73h_gD3KOPTs-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج کامل نیمه‌اول مسابقات امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108606" target="_blank">📅 23:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108605">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلر گالاتاسرای ۵ تا گل خریده برا تیمش</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108605" target="_blank">📅 23:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108604">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78ba46272.mp4?token=hpC2RqokiX0kZcFxnDVQ3pzzK2UhXLzCLbzE9FZmEFlLk1P7-1KbvkYzeeqVXGbHw7okimxkmACQ5UNSkLA4FDgdHa8FPmVD3BavSDaGaqoxrRp9d-WmNNKgb2E27Bt1cEmElZ9iLDaSU7S0L1ujB3L8DYG5an0SPwyxHGyTP6RwtKqbWfbwRwy5qERV1eOM69V5YNyrGBiVWiqTbA_EC926L8rfbXftVyb1Q51qt7CAWAAKM7-JjbUf_jBnNt7DggR8o4aPAFiac18bq_dsRFjZtaEFxjdR2fO5XViZ-EqOGE4AiKG_-OsX5RcIJLoCjQ18AECMYpF6Bq6OxGoWSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78ba46272.mp4?token=hpC2RqokiX0kZcFxnDVQ3pzzK2UhXLzCLbzE9FZmEFlLk1P7-1KbvkYzeeqVXGbHw7okimxkmACQ5UNSkLA4FDgdHa8FPmVD3BavSDaGaqoxrRp9d-WmNNKgb2E27Bt1cEmElZ9iLDaSU7S0L1ujB3L8DYG5an0SPwyxHGyTP6RwtKqbWfbwRwy5qERV1eOM69V5YNyrGBiVWiqTbA_EC926L8rfbXftVyb1Q51qt7CAWAAKM7-JjbUf_jBnNt7DggR8o4aPAFiac18bq_dsRFjZtaEFxjdR2fO5XViZ-EqOGE4AiKG_-OsX5RcIJLoCjQ18AECMYpF6Bq6OxGoWSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول بارسلونا به گالاتاسرای توسط کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/108604" target="_blank">📅 23:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108603">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اتلتیکومادرید دومیوووووو به یونایتد زدددددد که رد شد</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108603" target="_blank">📅 23:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108602">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگگلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108602" target="_blank">📅 23:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108601">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رفته وار داره بررسی میشه</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108601" target="_blank">📅 23:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108600">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رفته وار داره بررسی میشه</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/108600" target="_blank">📅 23:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108599">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اسطوره ژائو کانسلوووووووووو
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/108599" target="_blank">📅 23:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108598">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بارساااااااا</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/108598" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108597">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108597" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108596">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d28a95756e.mp4?token=gKOptxnmLS-iKfFPHdsRTRndo14lVgzXsadrEU9Bgl9Hh4BaddemOpdk4QER0uRu2FEkt-NyNU86uCRJ-JdlnWIw0elIe9W7QQIf8uFb8BvSvc6aWh__GDIVrpQCSWSOn25Bxr6oldquNVGYyyDcI1ItVa9P6eCDJHS1sRB9XCJyaQ6QSIrabuGVDm64iZHCQTKqstYyP5Ek5N_I4lohE7ow33ocWh6sqs769LqNBzkj_3ZKQlE3UumwZVvL1DYk527e60FKkkHQqEtHBopfn5UvoRsf-H8RtjwmmusDx8dglYA8VSSDz9L18HobKochCGKL4QaeZfE4R1sORYnRfx4DdZgALfj_2dPJ2GDMjE5rWxIwG3KY9CF8k0Jnd-yJBp7vIj7qshM5KeWaowaIwqSKJhJS3GICgzY8nRbYSnkEXMWsPdTBOjJvlbFSO_8EoAoK0b0skPdkGta3BEb2WiPXqsxYOL32wJtaZBB1cIuB52HwwQoYKgaAHCvP08zLtdbHyshcMla6MjN_NB5HVeNOFGKZ0f_pCuN6aIExExYvttEdwTjM8wsNw_Qdf3f5TVPcDyly_Kx7kg4zZ5mVcCIWFP0ikyyGJAx87kurjXu0wZqew5Vxswc4PYt3CRcny98IRBQSGHilqHZ7OK0q-SFhBCUgtNt8LnSLx80PDp4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d28a95756e.mp4?token=gKOptxnmLS-iKfFPHdsRTRndo14lVgzXsadrEU9Bgl9Hh4BaddemOpdk4QER0uRu2FEkt-NyNU86uCRJ-JdlnWIw0elIe9W7QQIf8uFb8BvSvc6aWh__GDIVrpQCSWSOn25Bxr6oldquNVGYyyDcI1ItVa9P6eCDJHS1sRB9XCJyaQ6QSIrabuGVDm64iZHCQTKqstYyP5Ek5N_I4lohE7ow33ocWh6sqs769LqNBzkj_3ZKQlE3UumwZVvL1DYk527e60FKkkHQqEtHBopfn5UvoRsf-H8RtjwmmusDx8dglYA8VSSDz9L18HobKochCGKL4QaeZfE4R1sORYnRfx4DdZgALfj_2dPJ2GDMjE5rWxIwG3KY9CF8k0Jnd-yJBp7vIj7qshM5KeWaowaIwqSKJhJS3GICgzY8nRbYSnkEXMWsPdTBOjJvlbFSO_8EoAoK0b0skPdkGta3BEb2WiPXqsxYOL32wJtaZBB1cIuB52HwwQoYKgaAHCvP08zLtdbHyshcMla6MjN_NB5HVeNOFGKZ0f_pCuN6aIExExYvttEdwTjM8wsNw_Qdf3f5TVPcDyly_Kx7kg4zZ5mVcCIWFP0ikyyGJAx87kurjXu0wZqew5Vxswc4PYt3CRcny98IRBQSGHilqHZ7OK0q-SFhBCUgtNt8LnSLx80PDp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم وایکینگ‌ها به بایرن‌مونیخ
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108596" target="_blank">📅 23:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108595">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بایرن‌مونیخ دومیوووووو خورد از وایکینگ
😐
😳</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/108595" target="_blank">📅 23:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108594">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/108594" target="_blank">📅 23:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108593">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
گل دوم مردودددددد شدددددددد</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108593" target="_blank">📅 23:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108592">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">صحنه رفته وار بررسی بشه</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108592" target="_blank">📅 23:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108591">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کوووووون فلیک داره پاره میشههههههههه</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108591" target="_blank">📅 23:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108590">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گالاتاسرای دومیوووووووو زددددددددد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/108590" target="_blank">📅 23:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108589">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108589" target="_blank">📅 23:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108588">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a56bd8725.mp4?token=Qa90pFGv95O9srEnYnHvD-8TrUk0moQSqoJo51GbyZygCVGWdWhzjUPB3Y6paHDECCE5TCEvBLu85862dcM3hHlM9ybSzksj6ohSC3V5bmyJheJR54SS1rYK_wIVpo-8tq9RhqZCs8J9RDVS8AheRLa_v1TUE3BdbXvqG0E5j3MRb_XVjO5zY7UcMLaxL6ekcApUzcDxTUR1sBMLDf5H4PtPMqSilNj_uMDKzPBYGfp-jDShuAXiJzxRQw9V8YwrcaWdlczKRYh9Z6W7QV5W3qey6gURoTQxujzDinhWvJeERrfpR5wJ2Fz03rYsj112-a1B_d_S67QAsWB2B7B7xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a56bd8725.mp4?token=Qa90pFGv95O9srEnYnHvD-8TrUk0moQSqoJo51GbyZygCVGWdWhzjUPB3Y6paHDECCE5TCEvBLu85862dcM3hHlM9ybSzksj6ohSC3V5bmyJheJR54SS1rYK_wIVpo-8tq9RhqZCs8J9RDVS8AheRLa_v1TUE3BdbXvqG0E5j3MRb_XVjO5zY7UcMLaxL6ekcApUzcDxTUR1sBMLDf5H4PtPMqSilNj_uMDKzPBYGfp-jDShuAXiJzxRQw9V8YwrcaWdlczKRYh9Z6W7QV5W3qey6gURoTQxujzDinhWvJeERrfpR5wJ2Fz03rYsj112-a1B_d_S67QAsWB2B7B7xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇹🇷
گل اول گالاتاسرای به بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108588" target="_blank">📅 23:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108587">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گالاتاسرای زددددددددد</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/108587" target="_blank">📅 22:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108586">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گلگلگگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108586" target="_blank">📅 22:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108585">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">لیل یکی به آرسنال زد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108585" target="_blank">📅 22:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108584">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">لیل یکی به آرسنال زد</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108584" target="_blank">📅 22:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108583">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گل‌اول وایکینگ به بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108583" target="_blank">📅 22:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108582">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee25b8b605.mp4?token=V7Pplt24joZwCtUDBtZCh5YnGq4NeY_Fk5aQlWkGZPRed8WFD-d-nXS8o2Dx9EpwCHEhyPnSCEEFlolGzv4Ufr19VNi8sH5uDPE0XLGquKZ5N7JPo6iwsgJDK7OLzTksZVZzP72xKlieDMLtby0ZorAGrguZebP9wKsth4OvjsP12FZM9cQirFX8v74ioDSGAEeJm-6DPWQI6oC87Rqp0_erRixq9oj2s7Gf3Lfpn4ExKKhk16THjaGYBETfH-cRvLL2TOETD2vlLpcDRBCB7qOW8Avmr4IPUGjVO-TlPRpGGj7XkpNz66Q-ZRhsNhn0Dm1_swCrClQxAMhflW1RgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee25b8b605.mp4?token=V7Pplt24joZwCtUDBtZCh5YnGq4NeY_Fk5aQlWkGZPRed8WFD-d-nXS8o2Dx9EpwCHEhyPnSCEEFlolGzv4Ufr19VNi8sH5uDPE0XLGquKZ5N7JPo6iwsgJDK7OLzTksZVZzP72xKlieDMLtby0ZorAGrguZebP9wKsth4OvjsP12FZM9cQirFX8v74ioDSGAEeJm-6DPWQI6oC87Rqp0_erRixq9oj2s7Gf3Lfpn4ExKKhk16THjaGYBETfH-cRvLL2TOETD2vlLpcDRBCB7qOW8Avmr4IPUGjVO-TlPRpGGj7XkpNz66Q-ZRhsNhn0Dm1_swCrClQxAMhflW1RgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
به نام خدا و گل؛ گل اول اتلتیکو مادرید به منچستر یونایتد توسط باریوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108582" target="_blank">📅 22:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108581">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گلگلگلگگلگلگل اتلتیکو یکی به یونایتد زدددد</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108581" target="_blank">📅 22:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108580">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بایرن‌مونیخ یکی از وایکینگ خورد</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108580" target="_blank">📅 22:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108579">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108579" target="_blank">📅 22:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108578">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">برررریم سراغ بازی‌های امشب لیگ‌قهرمانان اروپا</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108578" target="_blank">📅 22:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108577">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
خداداد عزیزی سرپرست تراکتور به مدت ۴ ماه محروم شد
‼️
امید عالیشاه نیز ۴ بازی محروم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108577" target="_blank">📅 22:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108576">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_BVzNIufY6vgVsp7SYvXoBMOMCnKP29te2dA0K_14wubnKp0W-ZH-7lT09iGQpEA5hfaYMBZNV7nZK1aa-OWnYVb3Vt05C4ELyEkUfSLvuvzLtR3BQ7mPhGc0cldKCVfuxstIsi-3T7KdBe-o9RAJzcIK6XNm1sCOSdTjc0d032r9BWdAgzUiZVpQboPfG4YD6rE8XSJSmy4jdM8JV09e1KK8gixxSqzgk-X7XrpXBrLWq-z73QYWukFpJnpZ1N5nCSo-PwIVqiQxj3HLObum9baEEOUlTO3vaVzWiTGFEGFb8KQ_ksPg85udC2dKiWkqn6KoIkCIS7t90_cDrf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب آرسنال مقابل لیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108576" target="_blank">📅 21:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108575">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaJ0DGBh2SvFYNh_gXdzenrzuVXBQM1luQHOoFLv86cfEzmFT_R3gbBDcCwyLMxrzdkxhNTwgiS8Dk87EHlIBP9dF1aTjwXlSxKVVaphUwvaBbGwecXxCQSNl87htBInFTN35YkPN5Wecbfo9UjD4_Jkv8pI0gvPFID8Fl2hw89XFkFSfhkOb4V001GsxgRcpWkvW0weYSPd-Zf-KoWRT-VFAz0nbl-kQhOpmUA4FO-vHJkE5NhcOYpb4l5wV2rx3P0ia7wRuqRfwfas8BXMAFPjmTBDrrtw9iAW0ZTEE2Ck3aovz-Run4AuXNa4Lcy3-8GVkGDb9x00z7t_yEgmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇺
ترکیب بارسلونا مقابل گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108575" target="_blank">📅 21:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108574">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13c928814.mp4?token=YRqBrn7WguCFrV1evWM2guaYH1pmyFG30wRD62G_UqbwUVrMBaZ6a6u7HUrNhtmYLgGmK2cr1CTewn_juMi5yGTyGFb3qS5eMWcTmIOxe261uU9HuFcRX2DEyBIQYyYJMtovE6uELWLFiYW6ynoHJPKk7x5ps2gnFd10NPfe4W_xKBvlqR3EZgD9IXU3sULEpj45xHZscDF5C3eUW8ENamjxx4dbhxUNaYksy-Jw3nBd0NSU5BrU0OAEl-uYXSnscAxwV3_7dNS2--Hv0StjhG9fHNFLxk3GJ9-6D8tIEZ_yfGwxDK2AUkCd1NQcLuDSUOAWWguFr6ak9-gmyPMMDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13c928814.mp4?token=YRqBrn7WguCFrV1evWM2guaYH1pmyFG30wRD62G_UqbwUVrMBaZ6a6u7HUrNhtmYLgGmK2cr1CTewn_juMi5yGTyGFb3qS5eMWcTmIOxe261uU9HuFcRX2DEyBIQYyYJMtovE6uELWLFiYW6ynoHJPKk7x5ps2gnFd10NPfe4W_xKBvlqR3EZgD9IXU3sULEpj45xHZscDF5C3eUW8ENamjxx4dbhxUNaYksy-Jw3nBd0NSU5BrU0OAEl-uYXSnscAxwV3_7dNS2--Hv0StjhG9fHNFLxk3GJ9-6D8tIEZ_yfGwxDK2AUkCd1NQcLuDSUOAWWguFr6ak9-gmyPMMDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇮🇷
آسیا محو تماشای یاسر آسانی، سوپراستارِ آلبانیاییِ استقلال.
😧
🔥
☠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108574" target="_blank">📅 20:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108573">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY34i6--16jbIEIGmB2Cu7Z8WeBA3DSvZqk75CbdbPTbXJXUbPEXd5Qt425gTIyXhO0dfR4ePjksL-U6JSllggLZMpQt3T4FXxjHZXFRp9PQl_-EYttA3OecL4UPWyoDYC6ALGNAh3u-ye7yUhp8lthNJWQLJD38_5Nggq_xJuZTJLAAJAj2IiGTdBA8km-Aks692SOAA_ji1WDo4eHsRwRKt66xbF8etL8LSFKSmcZNkXCadPm4jtmmimosGL8eJoBDQvM2Vvq1OkjkqMdh56Vm2_H6fA-61C2J7a0DgPgknrqHT-B_j0WW42H5aB-NMr08kNVtt2pupq_xhlWxuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اسپورت: دنی‌اولمو امشب مهاجم نوک بارساست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108573" target="_blank">📅 20:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108572">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94fdeb1527.mp4?token=aeXQAqgLS2bRwh8acat6yavenanV90U7Q-UPVWGL7dgkrgk06WbZCb5WyuDiM3SdQ7zjSJibRMJv9VNZixH0L2N9h_0tFmE2RKI6k7kOGiWKRbzbtlnZe0kOizN47L_Ex27JCSlZX8X8eix3iIcj6ir1sG9QRpEHGP4me8rbOXgKXpR094yOgG7LcR2GlkNa6DTQ5f7i1S5YmoRta-8CkbiTDcLhKWWGQ4c_pIx7sE5KkLHItwKRgRHRS6EjTsU64OnaTgB9ODpoBB2U_mb-hE7c67myxA6aApALeJghune9F39HymYfXPvu8l5IIpvHrbzoZYVia764KOx-OJ5SnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94fdeb1527.mp4?token=aeXQAqgLS2bRwh8acat6yavenanV90U7Q-UPVWGL7dgkrgk06WbZCb5WyuDiM3SdQ7zjSJibRMJv9VNZixH0L2N9h_0tFmE2RKI6k7kOGiWKRbzbtlnZe0kOizN47L_Ex27JCSlZX8X8eix3iIcj6ir1sG9QRpEHGP4me8rbOXgKXpR094yOgG7LcR2GlkNa6DTQ5f7i1S5YmoRta-8CkbiTDcLhKWWGQ4c_pIx7sE5KkLHItwKRgRHRS6EjTsU64OnaTgB9ODpoBB2U_mb-hE7c67myxA6aApALeJghune9F39HymYfXPvu8l5IIpvHrbzoZYVia764KOx-OJ5SnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوبه که فرد ذلیلی نباشیم
😨
😨
مثل مسی اسرائیلی نباشیم
😳
😳
دوشنبه؛ ۲۰ مهر ۱۴۰۵
📍
میدان انقلاب تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108572" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108571">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7ec7a32c.mp4?token=ctrrOsEopA7Vz6lWhIsOzcTHwwDvoC3DYEJKAMmh5zWLwbil40BfigKDiVz1nleYc3itkHtaJbFmT7iAPcoNAhU0rfSV7jXtT5rZlWglwomJv7UaM7cien8oacebTZjuBG9ILakmgR2OQmP1U-f75_cppbIGkIhGaFIlV4Ji_EtcjjsMWkRBgzKkt9rOePKJge3LavGSH125a8M7S1xqSQuLnwtr3VegdBDHyZwJP39MtHlsmdk7RlwFrekBF3AHndlZy-UbD0h353PpeokB5AObjY4prwYvgHXEndB01vt_AR8eOwPidXtjf9Hy4QXNPrH0sxDhEcAPRS2jXsg56g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7ec7a32c.mp4?token=ctrrOsEopA7Vz6lWhIsOzcTHwwDvoC3DYEJKAMmh5zWLwbil40BfigKDiVz1nleYc3itkHtaJbFmT7iAPcoNAhU0rfSV7jXtT5rZlWglwomJv7UaM7cien8oacebTZjuBG9ILakmgR2OQmP1U-f75_cppbIGkIhGaFIlV4Ji_EtcjjsMWkRBgzKkt9rOePKJge3LavGSH125a8M7S1xqSQuLnwtr3VegdBDHyZwJP39MtHlsmdk7RlwFrekBF3AHndlZy-UbD0h353PpeokB5AObjY4prwYvgHXEndB01vt_AR8eOwPidXtjf9Hy4QXNPrH0sxDhEcAPRS2jXsg56g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوبه که فرد ذلیلی نباشیم
😨
😨
مثل مسی اسرائیلی نباشیم
😳
😳
دوشنبه؛ ۲۰ مهر ۱۴۰۵
📍
میدان انقلاب تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108571" target="_blank">📅 19:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108570">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75009e0b9.mp4?token=I-s4r8MYDXDVCXOdkjcmzD8n-51WKmQuJb2fbeN9xN6ZdmOgKcuzTXO0cnwTCfyn1v74Gzm4ZEj0HuUNrG5InqBxnurd8SL1KgIRiaweHFgm6h7GvdCacvQV4tr0r_PVlwJb0xXQEIYs1BTFl-uiKWKCLJ-9LDh06q0loihIiyUxZ4zNu6BmJD_MB90jzT5TDLW6KyTBylcFYCXv10bxronQT3qq2fZNa7PzmWq0A97uxD5--_rMj79I0f9oSVO7D9lI7OXe4YpzriXAYJ9uuYpiaWjYNllN4ULJ00fMLsMbaqX64_2sTdoMFVWNWBJ1NOhyixJzlKXw_1i_tX3kMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75009e0b9.mp4?token=I-s4r8MYDXDVCXOdkjcmzD8n-51WKmQuJb2fbeN9xN6ZdmOgKcuzTXO0cnwTCfyn1v74Gzm4ZEj0HuUNrG5InqBxnurd8SL1KgIRiaweHFgm6h7GvdCacvQV4tr0r_PVlwJb0xXQEIYs1BTFl-uiKWKCLJ-9LDh06q0loihIiyUxZ4zNu6BmJD_MB90jzT5TDLW6KyTBylcFYCXv10bxronQT3qq2fZNa7PzmWq0A97uxD5--_rMj79I0f9oSVO7D9lI7OXe4YpzriXAYJ9uuYpiaWjYNllN4ULJ00fMLsMbaqX64_2sTdoMFVWNWBJ1NOhyixJzlKXw_1i_tX3kMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باند سفت‌های استقلال از یک فلافل شکل گرفت:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108570" target="_blank">📅 19:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108569">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9aa2627f.mp4?token=v1eUnFfTpEJTIHBMfGTmsjlaLuG20Qwyhwi_BBC-DzjLn9yisYBEVbMMdn3Pm69KfJZbQ8C2Hd4eIkHsZTvKnCoXY9Ywumuy9HuK4D683upePImno8qivmuYUh8WupKQnlP-7erNXwb72fQrp2vAVQ28q1FuWInm6NSauob0ukj73jgMIfmiV53jtqZwhsBhc6M9T0oo_Zp6MIVH8YELZAyBYiVLnXDrkKyQHGhfKdGdUZF013UrnpOne-smhmzrZms7eAmLnwuTp9NJm5_DTHvIYTiR7dZdaO2VLEkzaIEfur76pvzhZGDn41Spu-osPPO2zwYd3MEX9aG7vtoJyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9aa2627f.mp4?token=v1eUnFfTpEJTIHBMfGTmsjlaLuG20Qwyhwi_BBC-DzjLn9yisYBEVbMMdn3Pm69KfJZbQ8C2Hd4eIkHsZTvKnCoXY9Ywumuy9HuK4D683upePImno8qivmuYUh8WupKQnlP-7erNXwb72fQrp2vAVQ28q1FuWInm6NSauob0ukj73jgMIfmiV53jtqZwhsBhc6M9T0oo_Zp6MIVH8YELZAyBYiVLnXDrkKyQHGhfKdGdUZF013UrnpOne-smhmzrZms7eAmLnwuTp9NJm5_DTHvIYTiR7dZdaO2VLEkzaIEfur76pvzhZGDn41Spu-osPPO2zwYd3MEX9aG7vtoJyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
روایت خوبان‌عالم از بخور بخور در فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108569" target="_blank">📅 19:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108568">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce5d2d95eb.mp4?token=KctGP-oH5tySVrysqL9569QYbNZcoHVs5oWo3kzcv0uY1TNIUnk6Bvu0mZxlI-KJGI-kSz-i1Uqqv59KpLVcWAaN2SNmDNFnPX0QIYECxlXKujxq1WGBErXKo4orEHqlk_3ui37k-Sl3t339ahy069yU5NJXyWY8ebvwUhMuQuLSYljQCf7W6o-qutT3ImTZVmsHWlK2W8gTsJMhp5wdQREiao37EtIi21DvUE7c7r34jchfuBR2wSRFU30ZgZQwtqh6j9MU58I3dR4fzIhgMTNM8H35yhoC1nflXsp70lT6a6xCQ_OBhaHgnZt0mvpmyMQJ6uqS6C4HbSYEfi03BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce5d2d95eb.mp4?token=KctGP-oH5tySVrysqL9569QYbNZcoHVs5oWo3kzcv0uY1TNIUnk6Bvu0mZxlI-KJGI-kSz-i1Uqqv59KpLVcWAaN2SNmDNFnPX0QIYECxlXKujxq1WGBErXKo4orEHqlk_3ui37k-Sl3t339ahy069yU5NJXyWY8ebvwUhMuQuLSYljQCf7W6o-qutT3ImTZVmsHWlK2W8gTsJMhp5wdQREiao37EtIi21DvUE7c7r34jchfuBR2wSRFU30ZgZQwtqh6j9MU58I3dR4fzIhgMTNM8H35yhoC1nflXsp70lT6a6xCQ_OBhaHgnZt0mvpmyMQJ6uqS6C4HbSYEfi03BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
⚠️
شوخی سمی ابو‌طالب با کات‌کردن آسانی و زنش و احتمال کامبک: واسه خودم اومدی یا چون که یاس شدم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108568" target="_blank">📅 18:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108567">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mdrp5dhJUUf4_pbuMFnsIil-2C5jvKxpYot7-LZz06JtG3frOTW_7gdUlIkOZDkLEQ82CPOD2lsyhAeDr_bMt_4hjfNnBmPdIPVrR-AfRx50telSxqlqSx3H5vnot3cmHsMYrdvcPwJQtmuDh0M61jNFqPc7KhKaig9F18FFbE_F6jf3h21ks4gf7LUoF2Wjfb9mkGRKQK-5_hajdbffMvAry2cDYdO9Oaw_QHSUh1LIJCPGLwd40A0mlPxBIJ_NolDF1s2_rncIPYKSkn5TSVWRYJ9XG5hf3J787HUqoh-BqyfXqzvexIjDZbPBXoMBDFvZ9R6_An8aRot_mBnCjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
❌
لیونل مسی قرار نیست در مراسم توپ طلا جامی را به هیچ‌کدام از برندگان اهدا کند؛ چرا که برای این کار از او دعوت نشده است.
❌
حضور مسی در مراسم توپ طلا هنوز قطعی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108567" target="_blank">📅 18:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108566">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa1WngsGmgnCl5xVRCH8yF99Qv9AKRP4TbiQX-x9e9PTqDW5ZMF9cGfHx8NB_34JrRRXWEdYW6O7pxC4KeJtWuxE3Ng-At8yJGxsJxYgWtvfcMcwjWYN5RWu5-T3QCLu4VjLrp6UZV-ORmD5LWz4XhgMGqZQhtpQTrUpkfQxNBZxhGKz59cJe72ogklqKj5ans6FzhsmFlQ9Y2nsBgK6YUu1mDXPVbAxVu3FvFAdj-RGkQznTQ_2YNxXYca--EZn_rivUrdUG-5znx1S7k_xHc05scPMytsyjcTE0dzye0nC1t6t6AVdlky-yvSoTLGib9_YzxPIYBNABo8MA95pQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیگ برتر ایران|سپاهان فاتح دربی اصفهان شد
🔸
ذوب‌آهن یک - سپاهان دو
⚽️
گل سپاهان: محمدمهدی لطفی و کاوه رضایی
⚽️
گل ذوب‌آهن: امید لطیفی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108566" target="_blank">📅 18:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108565">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108565" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108565" target="_blank">📅 18:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108564">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0CPBDrkk9oMO6faAd8t9H6zDHfC8L23Fe-B51b4E_lzJd0hEF5wx8Eo36hD6iCb8g3gpz7vtJT8kvci6Pgc9SsE5m_4rxJ_VdXoWx1HrtGpXwX3UGwhv6c8EtaGgE6Zyfar-gawmGHE58rCx5vmGl5TO_vy6k2RQuW_1nDZh-TCdtvIgFRikgtx376IHuZYnmSIhwNFMIk32vCLtZzzDAxmJZF11qK96uEaM75drWNvA0wi5lV29ZGWdDxfpS77f23zdRWr3lx2YppHZlJdVZ5m09NNhGUhWAw25Ml-UKDIXO_PT2yEG9WFQRApzcgtqEePLBkLUG4WhZTVAkelww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منچستر یونایتد
🆚
اتلتیکو مادرید
🦖
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۲ تیم
در ۵ رویارویی اخیر :
منچستر یونایتد : ۱ برد، ۲ تساوی، ۲ شکست و ۷ گل زده
اتلتیکو مادرید : ۴ برد، ۱ شکست و ۱۲ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108564" target="_blank">📅 18:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108563">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19588c007.mp4?token=E_AVJO7zN5C1fruap5FXYzbm1Swrj1xZm5dJMYFJQbXz6h3jHcp_Q2IEhiF5qJRSfTWdZ8v-ALTvbNGIKTVyRf4NZHKRfm8rBLXi6bhEIli2MRZ1TOa7lp3T-PUOg95j9PoJ_fYWdDwRHqIKo0M4VOB0_N1uNVshXlmugQf-7EeyQBKtuRALUt4fDR4ECemanGo8mYS5xg3lMgWOu05vF1dINQodoRrTebyPPqSJQasW--WFZZgHwyrlBFR4lBySG5eF_CwypLpfDWkOx24C77DpitGF0NHnf5LuX1Y4zDHy45vivxcBqI1NrHyGt_LMqTV9ElgJzEYgt071NVYxgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19588c007.mp4?token=E_AVJO7zN5C1fruap5FXYzbm1Swrj1xZm5dJMYFJQbXz6h3jHcp_Q2IEhiF5qJRSfTWdZ8v-ALTvbNGIKTVyRf4NZHKRfm8rBLXi6bhEIli2MRZ1TOa7lp3T-PUOg95j9PoJ_fYWdDwRHqIKo0M4VOB0_N1uNVshXlmugQf-7EeyQBKtuRALUt4fDR4ECemanGo8mYS5xg3lMgWOu05vF1dINQodoRrTebyPPqSJQasW--WFZZgHwyrlBFR4lBySG5eF_CwypLpfDWkOx24C77DpitGF0NHnf5LuX1Y4zDHy45vivxcBqI1NrHyGt_LMqTV9ElgJzEYgt071NVYxgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
هالند و یک آمار عجیب؛ او بر خلاف امباپه، در تله آفساید گیر نمی‌افتد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108563" target="_blank">📅 18:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108562">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a34457cfa.mp4?token=qrk7pm9_I_vucUxM9gdk9UbK-zlkoGVZ3u32m7RF4hYGB29t4crLzJhDhBIs3qIQ_3JEMMAVvm99nsGdOwwo93SZQIohl_NYGvzysKkc4otauQvblHU1SS7ljq7tUpO3Eg26B6WgO3QLpK4KcY25xt_2evSNg1XmvLsdCMCuBrEredenIDN48vFqaUhJ2YZxFTuqebBizyJw8KU6WSHxFLBdng7OrIM1GfJGlSyHa7kECNgynDyZw-PfuX4FY4jq7S-vnn6tq7w89aNktz9miaMkMJhthlZ3k1uP3oXcPzjJKbGZODwgREEFIuSvcWD8hzjpnFnwXbuYRmlp8Gfw6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a34457cfa.mp4?token=qrk7pm9_I_vucUxM9gdk9UbK-zlkoGVZ3u32m7RF4hYGB29t4crLzJhDhBIs3qIQ_3JEMMAVvm99nsGdOwwo93SZQIohl_NYGvzysKkc4otauQvblHU1SS7ljq7tUpO3Eg26B6WgO3QLpK4KcY25xt_2evSNg1XmvLsdCMCuBrEredenIDN48vFqaUhJ2YZxFTuqebBizyJw8KU6WSHxFLBdng7OrIM1GfJGlSyHa7kECNgynDyZw-PfuX4FY4jq7S-vnn6tq7w89aNktz9miaMkMJhthlZ3k1uP3oXcPzjJKbGZODwgREEFIuSvcWD8hzjpnFnwXbuYRmlp8Gfw6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ده نفره گل زدند
⚽️
لطیفی دقیقه ۸۴
ذوب‌آهن ۱ - ۲ سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108562" target="_blank">📅 17:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108561">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGL0VqNZgrHHUk8852gmn7LsOUgie41o6rqE3xn2QEYwXJZwo6bcNKf4RZg_jlef4y_QbcBUchXzzw3zRFbr5-0arcSA0V-oloSc22dpY6Vj_uektFN34EphY5iF-6AfZjpc-98if5uV8b5kewW3QHrGLR4HQKVuNNDGVOBHKCgj4TX7e0-vP39erDhlV_-mAN1MdLzZaJcp3TOg4ep-Fq5PqKi2vntF-eNm3nRCdbRvNMuyIWzNIyJmtNKfhFKIWL6DQocI5-UfoiT-pf9cGvKDU3S6cmqCq6rJLIEmYd2HqS0K5IZ5rWBJc-De-yiaaIodDqBctN5_W8BYklnPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نسل جدید خط هافبک منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108561" target="_blank">📅 17:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108560">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57b850047.mp4?token=RBhCfFZmo_OoUTeF-4-j7iZ9W3sggslI8Y8Pk0BnjwGp4qqo582XovWrQLdUR9dSFrZkJbiK12FvkasMA9HKrRKUevgycjJjqYdJ5Q4UYcwI8q0iIZIdy5lhy_ZDWlc7_WMBk1goW39boAx2aVQPplhTRo3GfYyyiy1m1lgM3SS2_AKxp2aQbwHyL7RZhbDbMAhA4BHrlZbfkHxpU1J-us7vyAgAFMaNB2c1Vnh7jMdBcwumg-jUOvzxYV_cHxkBtD4tbJ6r3LqDnYPMidTtXSBhxgsEhveMUSItRQCykvN8OofhNMZvejkoXa1NdKJa1ndg0x7UWoOfCd3C_9gF2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57b850047.mp4?token=RBhCfFZmo_OoUTeF-4-j7iZ9W3sggslI8Y8Pk0BnjwGp4qqo582XovWrQLdUR9dSFrZkJbiK12FvkasMA9HKrRKUevgycjJjqYdJ5Q4UYcwI8q0iIZIdy5lhy_ZDWlc7_WMBk1goW39boAx2aVQPplhTRo3GfYyyiy1m1lgM3SS2_AKxp2aQbwHyL7RZhbDbMAhA4BHrlZbfkHxpU1J-us7vyAgAFMaNB2c1Vnh7jMdBcwumg-jUOvzxYV_cHxkBtD4tbJ6r3LqDnYPMidTtXSBhxgsEhveMUSItRQCykvN8OofhNMZvejkoXa1NdKJa1ndg0x7UWoOfCd3C_9gF2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
صعود تضمینی برای تیم اسپانسر داوران
ماجرای عجیب صعود آرمان آفرینان به لیگ دسته اول نوجوانان با حضور در رده هفتم؛ دلایل فرافوتبالی برای ۱۹تیمی کردن لیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108560" target="_blank">📅 16:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108559">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ca58a516d.mp4?token=nFFIkLtE--1WF1ZDyAc1QYJ9JAhpz5OMoFrlBtF4Tz8Rsd4HcfjQguf3D5HQnhUkvIjalnoOijGKrtvPD9B4-wJoDSXVuxeINnhA7ulymKe_G7IgE76QylM_ScOz5ab9THPYtOjVNWxOgyppCcKHxtzayoXHbkMsEmJ7DOrTehfSJrTb1tj6XGK8fxvUtNf183EWZS5DWfQxSdBOqYsm3Vbj1stZO95NEmDemxvEet5n6rQXEBNe3DNYI4MhDEXdlMb_B7o7ehtyjG5cAwjYcyBvijBig9_7Is5mB_JdTTN9VONZohIPNzg4DmmSgYpJTLD-KfU8Xecl-eK4JDo6cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ca58a516d.mp4?token=nFFIkLtE--1WF1ZDyAc1QYJ9JAhpz5OMoFrlBtF4Tz8Rsd4HcfjQguf3D5HQnhUkvIjalnoOijGKrtvPD9B4-wJoDSXVuxeINnhA7ulymKe_G7IgE76QylM_ScOz5ab9THPYtOjVNWxOgyppCcKHxtzayoXHbkMsEmJ7DOrTehfSJrTb1tj6XGK8fxvUtNf183EWZS5DWfQxSdBOqYsm3Vbj1stZO95NEmDemxvEet5n6rQXEBNe3DNYI4MhDEXdlMb_B7o7ehtyjG5cAwjYcyBvijBig9_7Is5mB_JdTTN9VONZohIPNzg4DmmSgYpJTLD-KfU8Xecl-eK4JDo6cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
اخراج محمد حسینی و 10 نفره شدن ذوب آهن مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108559" target="_blank">📅 16:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108558">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54bb3822ea.mp4?token=mV6ROKB6EWe-MQTe86fxj6T867rZCRU-ORxTBp9wW7_0O6IKYL0veChcBDM-eRoFBCl1RDu80S4PUSslQ9piAnL0tJxan_T9mg_FxWYlsxZqbWRGtvEsj0lPTN-LqFTU1cgF91JlAjavWDklocM9Ms1nlZJCfaDCJ36n6ST23AQjVobMG0Q0dzC9SgwIsUIc7WqxUirP4CMp9YHkcaDTcq-F99mm4vgFJm8NQTPZcK11Uidt8rlCAgKN2Aj6W6VPxex_cQaKsleEpl6v8cFY4uqi7-2Skr4oaG-0YzbNxU2jncoS59yTGzIu76WKpFre9USubg07FKYr8Lj6K3AmyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54bb3822ea.mp4?token=mV6ROKB6EWe-MQTe86fxj6T867rZCRU-ORxTBp9wW7_0O6IKYL0veChcBDM-eRoFBCl1RDu80S4PUSslQ9piAnL0tJxan_T9mg_FxWYlsxZqbWRGtvEsj0lPTN-LqFTU1cgF91JlAjavWDklocM9Ms1nlZJCfaDCJ36n6ST23AQjVobMG0Q0dzC9SgwIsUIc7WqxUirP4CMp9YHkcaDTcq-F99mm4vgFJm8NQTPZcK11Uidt8rlCAgKN2Aj6W6VPxex_cQaKsleEpl6v8cFY4uqi7-2Skr4oaG-0YzbNxU2jncoS59yTGzIu76WKpFre9USubg07FKYr8Lj6K3AmyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🟡
گل دوم سپاهان | کاوه رضایی '23
ذوب‌آهن 0 - سپاهان 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108558" target="_blank">📅 16:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108557">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108557" target="_blank">📅 16:34 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
