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
<img src="https://cdn4.telesco.pe/file/P1B9SJAAZxVwbOAq3Hb5KNL-aJBwx1esg_xSw8cjnLOCJcjtAo76HMA6oiEh5aX6wVNHMHf7K57fXaZI6MBDOe-4bQHo2p7V-3zBBtbUtoZm67NoJjetmb9iNGW6ZlLsK2o2EQCgjZNxcQzkHl1jkGGtmGW3g2jMbiiNzUKFaeX-rdtUui6fA0TH8RVKXMq3_-a7O0xa6eBmJQGagIcoxj1997Uny7saeneMya3-3H9CMe7pfZkpaYXqboJMDRAjBKPa2cFJOvJKz_3VQ2yWr9icVBWKdjs3YrEXgxSJdGwuM4D1UoslxmqEVRY8dOAKZhs42rmFCmbas3F-Us6reA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 23:31:10</div>
<hr>

<div class="tg-post" id="msg-465919">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d70034ddec.mp4?token=uEVNbv18OLKRJDKx4NqcGpyH4Fw9PB12AMofnYLw3SkZdNDUxpKCkP9DuW0lMp6ubO8N46hJzVMgeJs6YaHh9WFZBPQmMxzDnopekJ99gKJA9y_uEaaafVxROGI1sHdOLjIOSIbWVidpw6fyB9k4o70akNVKTnCkRFcQITDkF_1P1kPz9gKi60J61LhEvcFjTpUHKkljyibC8uzMJCG8owTwWk_cMEHmahJf9Awnq4k_04ZNIrnP4t4HIXu8PoSmRUZ7Bs87DWHCVbqxKW9rjgK-Tp3OCvDWG9lIqVASgRd_MmmakhMn_3q6w7FHi5AOT-wM7bOiOkayIs_4QyzDHYrU_DZlQYMhQr8_etOEs1fK3NzysmcLWI9gz33rcEmHsXzXrojRL8XYJGd2B6Ncv5fD_Umcz7qJWQfHjXJvIUwcdl3QDLRMKCr0prDwX_GuJLc-MjLpW9jJB31jcmRLE_YTKjNi5bwzEyTMFy7iPGGUJKdn20y0kG07P0IE8n-1FNnGhGm7BUDmhEtgypN_MQn7XLFb4DuaKO1V-tQFQdTvt2i-jEwiX0aSECWr6OYSX0lXk6Gf47G9msRevkLWcnXIpueHLglPmlWo1vn2wJDa68bma2YcV1tHOrcENV5Z5p-3BzjW5MEhspDyTpzJ-xGpdMImqCVVqQ5v7o1_Idc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d70034ddec.mp4?token=uEVNbv18OLKRJDKx4NqcGpyH4Fw9PB12AMofnYLw3SkZdNDUxpKCkP9DuW0lMp6ubO8N46hJzVMgeJs6YaHh9WFZBPQmMxzDnopekJ99gKJA9y_uEaaafVxROGI1sHdOLjIOSIbWVidpw6fyB9k4o70akNVKTnCkRFcQITDkF_1P1kPz9gKi60J61LhEvcFjTpUHKkljyibC8uzMJCG8owTwWk_cMEHmahJf9Awnq4k_04ZNIrnP4t4HIXu8PoSmRUZ7Bs87DWHCVbqxKW9rjgK-Tp3OCvDWG9lIqVASgRd_MmmakhMn_3q6w7FHi5AOT-wM7bOiOkayIs_4QyzDHYrU_DZlQYMhQr8_etOEs1fK3NzysmcLWI9gz33rcEmHsXzXrojRL8XYJGd2B6Ncv5fD_Umcz7qJWQfHjXJvIUwcdl3QDLRMKCr0prDwX_GuJLc-MjLpW9jJB31jcmRLE_YTKjNi5bwzEyTMFy7iPGGUJKdn20y0kG07P0IE8n-1FNnGhGm7BUDmhEtgypN_MQn7XLFb4DuaKO1V-tQFQdTvt2i-jEwiX0aSECWr6OYSX0lXk6Gf47G9msRevkLWcnXIpueHLglPmlWo1vn2wJDa68bma2YcV1tHOrcENV5Z5p-3BzjW5MEhspDyTpzJ-xGpdMImqCVVqQ5v7o1_Idc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور متفاوت دانشجویان کرجی در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/farsna/465919" target="_blank">📅 23:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465918">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F30FWR7hNVeIMvOZ4kX0K16YMVUOlHAuViCXAQ2Y0_TE9ik6Wuw-8Ons0e6wYZytLUiW0jr1Va59fe9flQgjEIzLmDhBwEFsSZ60UHyF7YZv7zQdJRLxLhGUXTy3XaX7LV3lCbG6DaRQ9o-zlXgFPDbBPbQiJ-f1mTExnDE5zbkIEkRM1nEmsAOPMrvJWUCKqYJR23syjfvsfKk6tOJ6Vspb1whAvgmCZAymoPe-7Sxy2sWpYXB0QiKnyr0snBUPdaIes_02Bge5-R3k11KMWMBEmydoH1E7gGgWeHAmQobFH9GfFriGYDLUy9SC_RpkFDARlku1dMFMqDpsSR67Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای رویترز دربارهٔ تدارک عربستان برای حمله به انصارالله
🔹
رویترز: عربستان سعودی در حال بررسی طرحی برای آغاز عملیات نظامی علیه انصارالله یمن با هدف بازپس‌گیری مناطق ساحلی و خارج کردن تنگه باب‌المندب از کنترل این گروه است.
🔹
منابع منطقه‌ای و غربی گفته‌اند این عملیات ممکن است طی هفته‌های آینده آغاز شود و نیروهای یمنی تحت حمایت ریاض در خط مقدم آن قرار خواهند داشت.
🔹
عربستان ۲ گزینه را برای این عملیات بررسی می‌کند: حمله‌ای محدود به مناطق اطراف باب‌المندب یا عملیاتی گسترده‌تر در چند جبهه همزمان در استان‌های البیضاء، مأرب، تعز و الجوف.
🔹
در صورت اجرای طرح گسترده، ممکن است بیش از ۱۰۰ هزار نیروی یمنی برای عملیات بسیج شوند.
🔹
یکی از اهداف اصلی این عملیات، عقب راندن انصارالله از مناطقی است که این گروه در ماه گذشته در امتداد ساحل دریای سرخ به سرعت تصرف کرده و در نهایت کنترل تنگه باب‌المندب را به دست گرفته است.
🔹
همچنین یکی از نگرانی‌های اصلی عربستان در صورت آغاز عملیات جدید، حفاظت از تأسیسات نفتی و زیرساخت‌های این کشور در برابر حملات پهپادی و موشکی انصارالله است.
🔹
منابع منطقه‌ای گفته‌اند ریاض از چند متحد خود درخواست کمک برای تقویت سامانه‌های دفاعی کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/465918" target="_blank">📅 22:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465917">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_HrdVhJrrSJpvutSibvxAjbBazguj15SjIZ2pVWKk6XQsngcIAmZJjYg16xgLHVhjXg21OieO0_77gmAPnz06d_xSjpzt_LOVIQydZoGjZrZq1GVc2he_-jS07MrT71UXv5WcSEjnVM8bsWxpO1pmB8gynn1DCyIQYCh2-D4ru4u_FTf1ttj1QW3SfFOM94bh1-TFEm1spQoRdMFW0SpdzioyU6GsGV7Jm30HTwWAXc4RQ543j2BSK53PYjNnikcwg-nmZ6kJtCg-oKxyWEazANeauEeAgIqTlXnRBkmZS8V_RmJigHdyVTMqJ1bxFeVu5bD45OOebK9W57TPfFhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر رفاه: دهک‌بندی خانوارها به شیوهٔ قبلی نیست و براساس سطح درآمد به ۳ گروه تقسیم‌بندی می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/465917" target="_blank">📅 22:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465907">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/euFbZj2BDbgOTrxotW2qO698VrPhMiieLwjdNp_Al09ZP7IQuz1GAQNUW4BQPG7JkHp-f39UFcQdclm0-FoICblR4Ar2DtJvW2OJn-55tRo3IFivAiy7fpP7p3-_MLEgcM3hpXeLncz6a09orIzBPzN4YIIkgTB1i1cwl70D9V6SGrpq0Fiyt9wKotIs4Yq8ftGvTHgaG84Uz2-yW1qwDTM4jKtsd3TZDuPFwy0fC8jUCTt_Nq2SZfwpI66_eNJQO7Npf-QoTVHws4dBwhrU7RhKiN7UFDIqYcAjm1X1tOMcLIyWJ9eYjQpJXVHGCYKTv3GyuIvDjsaHH82H86t1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sy9MBCz7rIgTN-h9jI2YKgzI-I1RdFbR5kDMD60W5cNgw9iTbZ6CaxhXWYpbZHoAtPOl6q3Dl9saoiA9RTkHN8B1d3yl4p3VZdTQ-FB_PZUJs81-QWROWyzOeK4WNF_v0fvCmgFHG7XEP5FcvP_YSWMN8RNm-xEI3oVyPbY-dh68Ukv44h7lu-NNHvi5EwO-YpaU6EgoRUx9pxqcGwoAzrQ2JdddqK6u-kU4KBjkGdL6glGZcxqA0R6sLKklJfKDRJa71qxF-Png54-ATKVii9CWJ5DnVuIYasbpazVspttcRhBiUNhLCT1ZBQBS3qNZRrN4uPUA3Jms68TTpbSWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTrfiACYMJxi1NQlXeTiQyhuHFvJsb-zyLFDNE4GuT8s6W7IRey5bBiztjnOiR9wnvgPr1eSjepZdBBcsqVHZSGkiWnwtCY8Rd-rf-icOW3jlaESL6B5rlZ2ILu2QYEkcQK-zDhKovKeJnIcZgX4IFfaC9b2pUSkEgx21KNWomsPIQiMd4JHdqdE9_zHZqwA4ObVE5MJylveHWlXl-EjU4P28dDbPfcHKpfNjxNd_Q5Q7_zfmOK0ugK6W911I_EKKSanix3rqeYQNnU8duOLDhU_FYCBPuvwvI70BlZoqu0md2MZeTGA-bnxyZb_Ow3fvOM2UcUigAriGlSUIu0J3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdeCDPsHWV55lQyXXl-pUvtk9ctdNxp1LSOvFODldknhQpB9g3vEzV8oN8WV7Pl_Iuid8E04BolHmzWqgp52oeKeekgdiOG9c_lLiI6bWKJoLeKfzw_Ysjwoeq2V_zPGhIXbwmuXGxKjd02NEpqZohLogulMCeMAf5WlMXcaQOeW-2J0lx-Txxy_ljyTkoh45RpleFC1yumiFcqvcRwgEGCKi1hQlZDUaAmmFrAu--jx8c03XhsGVDI8vQqHqvcCHQLOFOYm3HtiSnQiGJT74YC7Yij7CgJc5bubb8Wrv58GfV0gUTQLoTkekGSA76NkeIU2rxsYoTMCB_OpOxNQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUisVw95ZWb4pDoHTMJCCDWu4V9keTrp_ov2xVrkEcG0FrFbK8G1NBKXt8yzrUg5hDXHrMLXMUZCQnz0ebyJCsrW72QuoS9fztkLsxl6S0kjqHzkR3vGpjPjw6qGBjKsjvSV5Iit-rkbAm67L7wtrUl2eqpyHP8GiYaf-P-kPrmmoFmhuveyoQFCIthfgQ355EGJK-3uqmBppSDwhf3Ji4Nkx9eQSnjR0Q2iFDZ940m01qjJ-qzIUN5dp2erxUID9XI3nxItVTvpLR4BMlQTprppPTR2sDiKXUk3hlWpztfuFPApx3OEKoDOTzZLUbaEdrkdACsMN6Wm_7tz-khpMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z6GQ0mPvoOnBiT2l7epW-I_G49PLODCBTueacFF1dueCQfow1b8hCwiSIqyi5M48Qss0C9ywPtYt9QXLjQiqRHCDegex-oYOOdVrCRhwA6U0eRmXuIGF3Y-K9InGeohw1ZA8rNcF8L-nx8DQpnXJXCwsdaRXGgXv29cTnO2Ifr7IbvfekHU2ULG656DRAD-lHor2srZqbjWjvj7Azq3XCVIfKH9dgmyIoHKOLagbeNdezLXNcRjYu_7rt2JX4BJm50ENkvCyhtJQqBz-ibLrVTXidaB70_ZVjUrlOZPzfTRgx7usXe_EJcstHnGqX9G1noDdI0t-mUF-rfPPLyCu-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuJuRlEU-gDrwJkhAlgAtK7vQeKrZMljQsgxNQ6Rg9x8eWUnQ83883ym39UFNh8s7CsT7iR6AJE0oasB6UU42m9f9ALN29z8O7RiZ13tm5MEeP-VZ5r7WRE6q_mitaqRZM2M0p8MY7xuKeoPHi2jmdfuAL2xCP7C_MtfqUc5pa2LzUas_YVl7hn0p7In0ckLPmR9cmAROtC11gKC74SPaF2BNbRU9GvBbHJY05Nx4XOqjiFF-TLPNFNXQEQ-6UZPFv6e-175UN4uyJfWPjqnU1LoOxHud3e6qzRX_FJAP47ziqau1xh1AeGCsZHiH26CIb1yGIreNy9oqn1y61ES6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/od8dWnyrwUWXTDaBNHDwwu-ASbn6cXavgr-xLK1_fk9WJaQS8e3kemFZYmDA4LUsyR90hP_FGhZ-r72h4FqtStvSXDVvwWKM0E8gNcEOTXG3lsg3XhtkRNPz4EWLYj_iXhCpPd1upW8k2J0qucLmheu19INlz9sV-TmT0VkPxGHTRAEEk41VBeu5Haxux5bcSj1NPuz5n24Dz3yYmFTKjbbAPQsNExHBgxQciXtih_chBt0XR_c6_fIvgiZD2NPk7z-zBrBaDBRfUUK-dqNE93aOXClom5Jn-hCpzRnJi9K_UVoSRWBd4w7qXCQZ4Xhn3rN1bGR6WWYImZRy-3On3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1RHsG29yZGw3AyKsYQB8npHnY9hN9V1jhJmtUenuyQ1u6qN0G7sLj6_M1DbqkrNRwzRWCihie4ahQu306Ot67B2jddrhyCiVW9a9Pi5esrQ_R5lAgnGTSEky6babgwlJzPO31-VdluUWPr988NL8YCMmOwHzF9ayG-7RVMKhHUe5UnaQGNmbvrSEqvssFGahejrM5N5_VSb1g18zPkP1dEW_rST3e2wj42m45Wi6c1UZBs47uRhj0ifBJzGWSbbvmJx2vqTKs2VjuC70aW7LpC5muCaZsXEB8PbZsIJ1LHa7kXsW03xzMlls9rWQktfIQyWfuqYpoGwbBUIm_7_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQOUxF-ygnQxwtW98cj3i7ea1Jox93P5egMZGxovVsZY8PB7OTMFubUtlF6zvR-xe4XqXad_ByV9OxBZfeEnac2HJenb0-_KbqfycclqWU4T1iWzRnj_BCBC_bZrVGlOEvaYkdsxR6DKnC3BsLKX1YcNY7oTKIc41ng564LEnTKQZjaRcWTjt8tF9boSTMMeBexvEQzApji32e2ULVStCvlSzt9VlsO6wRKkLCSsyrIlUdUYGpjWiqxOEjtTsj3cfyM4YYrcbT9V46fyhnDXpxLIcR3sAEIWmfCK5DIAdlsEK0kUx5hJ3Tj08-BCm5mPdokY-ThhSl5XZdqscsk-gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اجتماع باشکوه جان‌فدایان البرزی
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/465907" target="_blank">📅 22:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465900">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgAbneBs-EF12pnHaGbBTmB5YItRkI2l5vMVy5GKj1nysYajeiuXCt44xzoaEv5qZhNgNPU6tPrAcIjly4CbMStMFTT4KGVr1UwWwZRnNSbOpwLv-ik1KCid8LvJTbRicX3diXnZqjNYLyVOVFLg7J1Qc_9HN602VeMtRe63trwU_W34ro2RmUM0PY8nsUSS7I_qOjeJTT8pWD9stmeyyIb59UeGRMLfI2sDjcPyqeyT1wFa2ZPKtT9t4dRlosnL53ENf3glHZSpn385YDIsh38f1dpAdY9ugwkKNnPEvqOIQLOTD_7XRrPZlgBq4wqEIkGF5I1vhNqhU2NqhtGaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohcTHynNDFHlv3qKiZ3nIOq-Uqw8RfH1FKiawKyLO479v77uGQBQKdmzUtm45PI_pVpPjJ8NzYquSu_GP0q6khjgTiwuEPeeVj-YKtvbp6fbq-qUoMdCKe4-2OXMzpKCMyNDNNT7vFGYviVkhkJW3m8Gg-fk-9l9h_7CCR82PJ1d2TKXUwHjsO9Qyzkl6DXUIIK8gI81woInJ1sgmrIQRJC4LZdRlqPj8kFvWHAWkJb29z47uHr0eWdZxB6lUODVmJ5NeR_r9LL3dS31odb8eJWp_DEyQuJHfm6sf2XdHBYsoNkvyVhGyCj1kcqSZt08ckhWab8DBnLb4r_4Ts9_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UftyUsmD8rwYu3HnpxJJoBlfiJl5SbTu6YljEUTOABFkUZ1FmBG_K5la22IJ476wK0Uq5MsbJpar6W-070UpLBh3ef5suxDi81n1kXRRmx9PZ9blZXIW0Q3JBvj5I-6j_Mx1Vu1IxzxnL42HBSFSDUBESJl4aMVYNGm0kInGKi3KdBpvxdKveOoapvU8Ax2hOFcg7kwit1GmnytVvUxRHs3c0P8Mb_dvhVKBfDZr7z2oqZ-MnFOYC0J5A6fy1vS427bxTfasF4h5O8fwj4RjGH12U4GFmdj9ocTKTTG1tW0PdUVdUy2aYpj-Ef5yNhxpp1chLZTpPI-ZbLyqpTzQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SOPQc6e-IevozTGbLWekjapkd8KhhovNVxFV2TwvNUEMGMlvjUBekM9dT8GgWGTmRywTGQ2IZc77o5jswYV2mp4_bbWS_nPYK-X2jIYIoA7NWdUth-dLT97Z02UC2JAv0l2_kPb12xp7QobOs6rBcfl9vVg_dh9OxkQSdQ2nSZIp79IYSmTTcFdks9wJezED3QoTJDH48368Xi6LivMSCEMJ4AEg1Wv7jllkd2nGemAGhrGGX2Eb8qB5TOUs1R9GeBlI3A82gV8Q2gHkfHVn062pvHwowAR--q8DjsFl5M2ikF_wNS1UAAtFz2zIoZlGOPkd9e2OJH6n4k91f1Mm0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7BcFJSOzN5Y0-4496sJI5hIrx7otxpOoUmgwZE8YBVds4f4Q_Xd8VcIC_Qbxyj3Fetc4jG7cb7laE4i0HfQRxt3S-AaPxb1JifEskaaZ1gA08QRoL8c-WGZVO_HhrOwQqAbJMAuOgZnTVt5IVizDl9nOiaaxgSrszBcBPr5Rq749EDo5W5hms7TcU8Gzx3EeKtStcYkx49cdDp0ubUIQdN3KQOWDehf3yaoVr438Ek92QSPlEZjZCiBehKSDQFbMvkylHEhT5bLQs0Xra5xJs4DJ6a0KHXj409teMZIAP6LjyjjdlGPImDmPc_U_ARnWPo7VuQan0AxoCpqzRR6oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3kAyhCV0e2nR1gBq7WS81UOsnLMYOAuQTbIT2MBpJ8Q-u26TAP1cfzxTH_BzONOtIit8goC5hANd0CEZqXob9louCDRVh1Ha0noW-TtEZiYMKDNwwavLsdKE24Z6TLDzcNfzQdUL3JRpy-Zg_YsuD2e0nbPvkofhxgvLFnktUJZfbn6aOAAXIj_MimPS180Mmo0TVqKgNFVrnZk1mn4Ihsq6JHMjV_4sbsbJtiyaYWHXxAWzLdpiLxABXnsU6IY8NuikYcgFM7Z_aSKXm4xRJy6A54-fKS45F9Mf0jQFvAI3vXHmYddaRGl-Fq2FK-sNwCktVmfI-TLMp3mHykwPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUBWcfdcSMnpcy5Hp8mxzNWRBX8gv-OfPXVf69qsR8VvJihUjbJShUyCfKkWxGt9RY6E2q0nB5a5a6Y1x-nii8W2eDo7hcoXo1rzCoq6fTQjan9x94ysMDMyGzTaXEqRK6VwXXNkkxqLCj_PTNw0huiChmrpwwD_Ka1g-drmWtwk9ogn_lW_NVqJZEatncdhZze_Aq0oFdh2Uwgn8ql3OLJXRJTkFhPt6GyF1gcrvKpAqHOBELjVuIeuOGuQxdH6ItrofMrhH5FAXN3gy2jKv5LcOpizLrT1zWlFqjXw9JZCmiWXDh6NvNbUW0R8CObGfEDdqaegVto_y1XPa_JhUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت دومین سالگرد شهادت سیدحسن نصرالله در حرم حضرت معصومه(س)
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/465900" target="_blank">📅 22:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465899">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
۲۱۶ شب گذشت؛ خیابان هنوز در اختیار مردم است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/465899" target="_blank">📅 22:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465898">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">جام حذفی حذف شد
🔹
جمعه‌شب، سخنگوی فدراسیون فوتبال گفت: «تا این لحظه باتوجه‌به فشردگی که وجود دارد، امکان برگزاری جام حذفی وجود ندارد».
🔹
سال گذشته جام حذفی و لیگ برتر در ایران به دلیل جنگ ناتمام ماند. بدین ترتیب لیگ برتر امسال تنها جامی خواهد بود که به یک تیم اهدا خواهد شد. این یعنی از آخرین کاپ باشگاهی داخلی که به تیمی اهدا می‌شود لااقل دو سال می‌گذرد. آخرین جام حذفی در فصل ۱۴۰۳-۱۴۰۴ به استقلال رسیده بود.
🔹
باشگاه پرسپولیس با توجه به عدم حضور در رقابت‌های آسیایی و ترکیب پربازیکنش در نامه‌ای به سازمان لیگ اعلام کرده بود که باید جام حذفی برگزار شود. همزمان پیشنهاد شده که جام حذفی بدون حضور بازیکنان ملی‌پوش انجام شود که هنوز نتیجه آن هم اعلام شده.
🔹
حالا علوی، سخنگوی فدراسیون گفته که امکان برگزاری جام وجود ندارد. او درعین‌حال گفته رئیس سازمان لیگ در حال تلاش است تا در این مورد تصمیم گرفته شود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/465898" target="_blank">📅 22:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465897">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO6JEaXpe74dXCw6EbwcdfbvELHkqjgDtqNL2QN2uegfzRYzpQsTP1q519QtcEUiJbf0qp_28qni6ePX9UOfIqhvHFmcVUJWx8RzyLWcodthd8lypZndNTQgqq79OQc_6HmZNfweDmFUAVKJIqDWoGvfb0fDFNvr_Q7Ds-YpCy1uZvsdg_XPhgK7YxMq9waYFnfnCA6XHWmWNzFIo7vtq_eq3Duf_LpL4dJCmNEfa2e56y4r1S_du8YhahTEk8pHpNZr0cCYc5Fo3HPIwAU0XZdpsPTqM2aw8DgHTB4yH9x2RlTcPSmx0kDMGl0D8bDlmSyb-eXo6jn0l1JcMevxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر متفاوتی از سردار قاآنی در مراسم «نصر قریب»
🔹
مراسم «نصر قریب»، بزرگداشت دومین سالگرد شهادت رهبران شهید جبهه مقاومت، شب گذشته با حضور فرمانده نیروی قدس سپاه پاسداران، خانواده شهید حاج قاسم سلیمانی، خانواده شهید صفی‌الدین، خانواده شهید نیلفروشان و خانواده‌های محترم شهدای لبنان و ایران در برج میلاد تهران برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/465897" target="_blank">📅 22:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465896">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
ماجرای هالیوودی پرواز فلای‌دبی زیر ذره‌بینِ کاربران فضای مجازی  @Farsna</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/465896" target="_blank">📅 22:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465895">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa1a7af43.mp4?token=EM21qzW8P2wI2kRgQTEDLk3g0pT9gB-rXouIjYDjhIFMaMOTElXWYTbSpFUfTng4zyxDznP6qC9XMYHx1epJQJxn-ry1H7u3QUDNHFZNXp0LD0TkITm0PM-uUU2ewGdbVVTTCYEJ1FuZE1qz0AAkSsPbY1NHTBGvNknI4gO3NbmJXkmfOpvfynXUF3A58l5SyEEibz51xRQn6SXKdcllzhr4EyqyZUCfWm3mrBBDO5NEUkz-dyDCmQwq8Usmd_mGUwX5G_8s33KDHzAoWDW1IR4NhOjsZyjvMFQnZOE32TwFTKc0B3bIMNITbCGjHZwn6HIT89rmt4QGf9z4_7Q9Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa1a7af43.mp4?token=EM21qzW8P2wI2kRgQTEDLk3g0pT9gB-rXouIjYDjhIFMaMOTElXWYTbSpFUfTng4zyxDznP6qC9XMYHx1epJQJxn-ry1H7u3QUDNHFZNXp0LD0TkITm0PM-uUU2ewGdbVVTTCYEJ1FuZE1qz0AAkSsPbY1NHTBGvNknI4gO3NbmJXkmfOpvfynXUF3A58l5SyEEibz51xRQn6SXKdcllzhr4EyqyZUCfWm3mrBBDO5NEUkz-dyDCmQwq8Usmd_mGUwX5G_8s33KDHzAoWDW1IR4NhOjsZyjvMFQnZOE32TwFTKc0B3bIMNITbCGjHZwn6HIT89rmt4QGf9z4_7Q9Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کار: بدون نظارت و حمایت هم‌زمان، حاجی‌زاده‌های اقتصادی تربیت نمی‌شوند
🔹
در حوزهٔ اقتصاد نیز تا زمانی که نیروهای صدای جامعه نتوانند دو نقش نظارتی و حمایتی را هم‌زمان ایفا کنند، نمی‌توانیم افرادی همچون حاجی‌زاده را در عرصهٔ اقتصاد پرورش دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/465895" target="_blank">📅 22:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465894">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77717107eb.mp4?token=eSIQWuEijWXru9jhc6EIsIfmD5mF6jsLhpdXnKw76P7SamweLJiVWGSCMO09-kFkOj1qMVlUyYJK-T92fr72o0NcFb2Wq98lAJJ69u8jefO7GZVlSgiHNkHCj00bYnypcnhLTZNWuHKrs_J67FxzJh9ATRp8VzCrb2sJSWxTlaDjDoxtZFHJ-l6LIaoF1FaMDaYKuOZI0xJRJetjGg_4X5cQibunlUjWmhDgFjz8e2MWc51BgOQw80al-TouP6nBubP8_rH8z2zPt55D-g7gPUqksLrxk49kQXzrxJ1M50zwmk6QXGFoye64LyUzHpvUeB0nlojfydxL6jDxa84fpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77717107eb.mp4?token=eSIQWuEijWXru9jhc6EIsIfmD5mF6jsLhpdXnKw76P7SamweLJiVWGSCMO09-kFkOj1qMVlUyYJK-T92fr72o0NcFb2Wq98lAJJ69u8jefO7GZVlSgiHNkHCj00bYnypcnhLTZNWuHKrs_J67FxzJh9ATRp8VzCrb2sJSWxTlaDjDoxtZFHJ-l6LIaoF1FaMDaYKuOZI0xJRJetjGg_4X5cQibunlUjWmhDgFjz8e2MWc51BgOQw80al-TouP6nBubP8_rH8z2zPt55D-g7gPUqksLrxk49kQXzrxJ1M50zwmk6QXGFoye64LyUzHpvUeB0nlojfydxL6jDxa84fpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای لو رفتن عملیات وعدهٔ صادق ۲ و دستور شهید سلامی برای ادامهٔ عملیات
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/465894" target="_blank">📅 22:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465893">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14248f3224.mp4?token=eGknVcW5wITxZFXr474fqWtmKKwZAi8fDSSUWAqhdg6yZY9iuD7rx3fa8IzganfvnyNYywetHONJRplVJEiGMNe8WmENCh4DzKYPc_kO8ulD3176R61f2zy49hzTvyxjh7xtcRx0te0Nz2945afmXajPYf6_ZIkmal7949T1ligOtEo67vLIDJ5MOREL5KxxtGxbxGaA0gsElrwqAKN_vHAzyEAwpWeR0iiYmVK4AvH8kOikL-UG0IE7NAkZqaLRXJN_1qh3OfLZQVYlItf9xnBqaEM26QFDWMQyRBBNFhH87SkQpWW3SJbFNikNSvLkbyfAV8wVTreUnjgLWm4DnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14248f3224.mp4?token=eGknVcW5wITxZFXr474fqWtmKKwZAi8fDSSUWAqhdg6yZY9iuD7rx3fa8IzganfvnyNYywetHONJRplVJEiGMNe8WmENCh4DzKYPc_kO8ulD3176R61f2zy49hzTvyxjh7xtcRx0te0Nz2945afmXajPYf6_ZIkmal7949T1ligOtEo67vLIDJ5MOREL5KxxtGxbxGaA0gsElrwqAKN_vHAzyEAwpWeR0iiYmVK4AvH8kOikL-UG0IE7NAkZqaLRXJN_1qh3OfLZQVYlItf9xnBqaEM26QFDWMQyRBBNFhH87SkQpWW3SJbFNikNSvLkbyfAV8wVTreUnjgLWm4DnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ملتی که ۲۱۶ شب، خیابان را به میدان حضور خود تبدیل کرد
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/465893" target="_blank">📅 21:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465892">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74ed80517.mp4?token=eNCvikBG2IAUmj0t7VOJ2nO67UlKEkICG4xUF5-jiy_oljHx-8meZzLxUydhz6LQBJCFQz4ApvDI0SgFFFppJocFESrcaWG83jkYqhePtdLlJ2dn8cs5CxrsfP2FIJobBwxrTqmjwiqOqa4HIYAJyaKi6tYhbGOU_mIJ8EhnjkTGqzKZ1N00XAL8jqLeGPMI2Hyti9PvEsqzOtZTlhrRTh9bffO4vxC8MQZHLzf2SMyPDgAdil9w5BNWpf7q1b4NcD-X8SaplShW648o_oUfBmMCMGhPfZYFY8u6wSfbGps7z1-Xw2GcXv1CvDrt9yEuFLc3zciZaRhWJnIt-_W6Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74ed80517.mp4?token=eNCvikBG2IAUmj0t7VOJ2nO67UlKEkICG4xUF5-jiy_oljHx-8meZzLxUydhz6LQBJCFQz4ApvDI0SgFFFppJocFESrcaWG83jkYqhePtdLlJ2dn8cs5CxrsfP2FIJobBwxrTqmjwiqOqa4HIYAJyaKi6tYhbGOU_mIJ8EhnjkTGqzKZ1N00XAL8jqLeGPMI2Hyti9PvEsqzOtZTlhrRTh9bffO4vxC8MQZHLzf2SMyPDgAdil9w5BNWpf7q1b4NcD-X8SaplShW648o_oUfBmMCMGhPfZYFY8u6wSfbGps7z1-Xw2GcXv1CvDrt9yEuFLc3zciZaRhWJnIt-_W6Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نتانیاهو به‌دنبال بهانه‌ای برای ربط‌دادن حادثهٔ هواپیما به ایران
🔹
نخست‌وزیر رژیم صهیونیستی در واکنش به حادثهٔ اخیر هواپیمای مسافربری «فلای‌دبی» به‌دنبال ربط‌دادن این رویداد به ایران گفت: «مشخص نیست این حادثه به ایران ربط داشته باشد یا خیر؛ ما نشانه‌هایی…</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/465892" target="_blank">📅 21:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465891">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/490dab02ba.mp4?token=H92wkh4gGj6rvGUFVtA1HbfrxxmtmL341XTFWJbAbHn-wOnUC2cz5JvtIofq0zAUvjJiZnH8Vc_Qyusxu70fGEy7SbIAl71giCPVoQG91frJi2OHiYbaJSi8ETO4sUoSDfUpZ7qpxkMplztw15bW77duvAs1YSrv1UskWtlyqi1-IHGOZPJyMriJt79LII1EMeVTSczQYhjocADBvwYklSo08ZRxRk2QHd1RV6NO_dfdGQ5nXHpaPgA2J8VXOCyiNBQhofiqb_irtHi9PeoczcksVIopbd4cbRuBWWDDvKkCgOMDqLQZzGdqwGWHnLJ4y5wJq_ZWnTRO1nVfqxWC6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/490dab02ba.mp4?token=H92wkh4gGj6rvGUFVtA1HbfrxxmtmL341XTFWJbAbHn-wOnUC2cz5JvtIofq0zAUvjJiZnH8Vc_Qyusxu70fGEy7SbIAl71giCPVoQG91frJi2OHiYbaJSi8ETO4sUoSDfUpZ7qpxkMplztw15bW77duvAs1YSrv1UskWtlyqi1-IHGOZPJyMriJt79LII1EMeVTSczQYhjocADBvwYklSo08ZRxRk2QHd1RV6NO_dfdGQ5nXHpaPgA2J8VXOCyiNBQhofiqb_irtHi9PeoczcksVIopbd4cbRuBWWDDvKkCgOMDqLQZzGdqwGWHnLJ4y5wJq_ZWnTRO1nVfqxWC6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واگذاری سهام سایپا به کجا رسید؟
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465891" target="_blank">📅 21:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465890">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حکم حبس الناز شاکردوست در دادگاه تجدیدنظر تأیید شد
🔹
شعبهٔ ۲۳ دادگاه انقلاب تهران، الناز شاکردوست را به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس تعزیری محکوم کرده و به‌عنوان مجازات تکمیلی نیز ۲ سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری برای او مقرر کرده است.
وکیل شاکردوست گفت که موکلش به‌واسطهٔ انتشار یک استوری در صفحهٔ شخصی خود در فضای مجازی پس از حوادث دی‌ماه سال گذشته، به این مجازات محکوم شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465890" target="_blank">📅 21:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465889">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بازداشت مهندس وزارت انرژی آمریکا به اتهام حمایت از انصارالله
🔹
اف‌بی‌آی یک مهندس برق شاغل در وزارت انرژی آمریکا را به اتهام تلاش برای حمایت از انصارالله یمن بازداشت کرده است.
🔹
مقام‌های آمریکایی می‌گویند این فرد در سفر به یمن، اقدام به خرید موادی برای ساخت مواد منفجره دست‌ساز و قطعات مورد استفاده در پهپادها کرده و تلاش داشته توان ارتباطی انصارالله را ارتقا دهد.
🔹
شتون حامد اللبودی، ۵۱ ساله و ساکن ریچلند در ایالت واشنگتن قرار است روز جمعه برای نخستین بار در دادگاه حاضر شود.
🔹
براساس اسناد ارائه‌شده از سوی اف‌بی‌آی، اللبودی با هدف کمک به بهبود قابلیت‌های ارتباطی انصارالله به یمن سفر کرده است. مقام‌های آمریکایی می‌گویند او در سپتامبر سال گذشته به یمن رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465889" target="_blank">📅 21:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465888">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b75d5430.mp4?token=D0RDBjh9mrwKMwdO0n8TsKAaLZPjygoL6J-0HGH_RqbCWoa3NsLVuEEpufhOfDpxyUznXDhTPR5nlkfJn2xGVwMJfLtWAaRbwbrNpzFKyLtE77bxDylKoJOf2BadDEOyQSom_A_z7DmRRzf-aRw-qrYMuZOfcgQyU4DI-xvGB5eqCSdfWFcZT0KumDZ2EADUyTG7N3PnWnYRPpgCgZNZKUwFPDh9aFl3Yzp3pP2ytEjfqnt1_XkFWMrml4TBXfwimCFvC0AJm8_RiTuKxWf6uWkxQEyJQ_btTIm130cBTb6EdnvgYQT7yhVdcolXZcRp1-wbawzUBvEIuEQpWIm5Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b75d5430.mp4?token=D0RDBjh9mrwKMwdO0n8TsKAaLZPjygoL6J-0HGH_RqbCWoa3NsLVuEEpufhOfDpxyUznXDhTPR5nlkfJn2xGVwMJfLtWAaRbwbrNpzFKyLtE77bxDylKoJOf2BadDEOyQSom_A_z7DmRRzf-aRw-qrYMuZOfcgQyU4DI-xvGB5eqCSdfWFcZT0KumDZ2EADUyTG7N3PnWnYRPpgCgZNZKUwFPDh9aFl3Yzp3pP2ytEjfqnt1_XkFWMrml4TBXfwimCFvC0AJm8_RiTuKxWf6uWkxQEyJQ_btTIm130cBTb6EdnvgYQT7yhVdcolXZcRp1-wbawzUBvEIuEQpWIm5Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در شب ۲۱۶ صدای تکبیر از شهرکرد به گوش جهان رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465888" target="_blank">📅 21:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465887">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc5177fc9a.mp4?token=g-lGImIvwK0e1-2Ns3Y4Fmtf_VasmU96AlEjgXOYABVY6CtDx8GseyjDzeJSz9CXQnQ03lWqOIsPLazGypN9c30l11R-iq21z0H-B66mC6YlVEpEZs0SmtAt7r_ab78w5Zy6X6kju-wiC8-6gqKA0s5xeydqujBMRIhxAgocd_fpTEcXTfPSRQ8tKLjwWnkPiOwgGtyK1AIOkcb3VskNooT6zheEkbhFXsz-UkD4sUdPmAKLuERsKyItd5ctMp4UWhcpvkpjHJ7qMESjmxZPSDnIlTQtGWmJIJbc750rhvdyvqPjQ80nP0C2ZH0BtSdEgqnGIbD7wJ68SfHYzTgySqghMCwLPI9Mj7Pdr3poIEXixMRgVJxCi5nYkwpV4J7Mb-VEswcGWAOu7qi2Z1IeERKcZvdTcquUfUN6-9SUe_yGFmTI3qW28zLq5eeWEEHnXO1WAy33DMBKfZc-HHMAR-XwICcuxCFLQBy3kXvp5EKYYfrSHHoBUkAqSgF5KIAFtr7dYASmKzUcX6H73SaiQ6abKVIKhQT1ePViKII3y4jiZ9DyasscJPb6Du1mvqTzm8EdvM4vzSWFuP5aaMH_2136kRM8_GkB737axW4PUvr2L7tkhlEdyJPWtliNBOv0riWUO9Oe0LnQz6IraSXMUHKBlK85saVfukmfQ1z6ERQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc5177fc9a.mp4?token=g-lGImIvwK0e1-2Ns3Y4Fmtf_VasmU96AlEjgXOYABVY6CtDx8GseyjDzeJSz9CXQnQ03lWqOIsPLazGypN9c30l11R-iq21z0H-B66mC6YlVEpEZs0SmtAt7r_ab78w5Zy6X6kju-wiC8-6gqKA0s5xeydqujBMRIhxAgocd_fpTEcXTfPSRQ8tKLjwWnkPiOwgGtyK1AIOkcb3VskNooT6zheEkbhFXsz-UkD4sUdPmAKLuERsKyItd5ctMp4UWhcpvkpjHJ7qMESjmxZPSDnIlTQtGWmJIJbc750rhvdyvqPjQ80nP0C2ZH0BtSdEgqnGIbD7wJ68SfHYzTgySqghMCwLPI9Mj7Pdr3poIEXixMRgVJxCi5nYkwpV4J7Mb-VEswcGWAOu7qi2Z1IeERKcZvdTcquUfUN6-9SUe_yGFmTI3qW28zLq5eeWEEHnXO1WAy33DMBKfZc-HHMAR-XwICcuxCFLQBy3kXvp5EKYYfrSHHoBUkAqSgF5KIAFtr7dYASmKzUcX6H73SaiQ6abKVIKhQT1ePViKII3y4jiZ9DyasscJPb6Du1mvqTzm8EdvM4vzSWFuP5aaMH_2136kRM8_GkB737axW4PUvr2L7tkhlEdyJPWtliNBOv0riWUO9Oe0LnQz6IraSXMUHKBlK85saVfukmfQ1z6ERQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رزمنده‌ای که داغ دید، اما برای دفاع از میهن ایستاد
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465887" target="_blank">📅 21:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465886">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f7f2b5305.mp4?token=WtM1iePkPh_4ps-_FUhnv5r_jfil4wY67PcYjQT0phbJAuVyjLbddR6NM-gdP2-O6SrTsnti8ySmdUjMhK6PPzREJ830uBGto7yPOuOtdg0SgYx5ezXqSVVOKlB0-Onv2B2VrRIU8er0bs-pWmAp9OPxXXv-eFj082mpOlaVjPTaz906sBP5P-ybjJECZKupy0H0tEiGTDyMXAJ2JvtR_kNxpi7PbxhEoZXkwb1m59lGYpJ_a3ReHDQvC3qPbkQl1l5ztEfAhwXA4f8NgQmgjt33UqlN_Agfpi71i1qrGp72e8YXzOD14MqyZn3UhoXaf9s_OJ0ErEXnR-NUevCYQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f7f2b5305.mp4?token=WtM1iePkPh_4ps-_FUhnv5r_jfil4wY67PcYjQT0phbJAuVyjLbddR6NM-gdP2-O6SrTsnti8ySmdUjMhK6PPzREJ830uBGto7yPOuOtdg0SgYx5ezXqSVVOKlB0-Onv2B2VrRIU8er0bs-pWmAp9OPxXXv-eFj082mpOlaVjPTaz906sBP5P-ybjJECZKupy0H0tEiGTDyMXAJ2JvtR_kNxpi7PbxhEoZXkwb1m59lGYpJ_a3ReHDQvC3qPbkQl1l5ztEfAhwXA4f8NgQmgjt33UqlN_Agfpi71i1qrGp72e8YXzOD14MqyZn3UhoXaf9s_OJ0ErEXnR-NUevCYQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ برای کودتا در ایران دست به کار شد
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465886" target="_blank">📅 20:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465885">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران - خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
اولین واکنش رئیس پدافند غیرعامل به حواشی استفاده از ساعت هوشمند
@TehranFarsnews
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465885" target="_blank">📅 20:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465883">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎥
تصویری از جنس ایران؛ کرجی‌ها قاب ماندگار ساختند
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465883" target="_blank">📅 20:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465882">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0977608af.mp4?token=M3Mfr1YOblleYGMkPiuUUC2Ynf216kNnfRHxv23KKTbr-rXdZA4sBrw7WdDCk14Zin6_54GJXGohBsX1u_ts6SQaa7ScuacML8woKmxpXvKjSe4T_UCWOwaRy11mAlL1EFyQmHRv4GhJoLx_GCUmbkn0oYosq3xVsX5rrkBqaF3QNQpTSq_-j61vlpme_o3wYTsoDmGY-u2bvA3nZm9YzZj-PCo1w029QLsSALTdobVSXsa1iRe64GdRNMBTu89TfNc03azZMpxXs958O7Ntp7na_CxOoHTKDYDTVPnpeh5-OJBcEh3wimo7FwWEYnLj7ZjivLVObghHd7FVCquFJjn1u_tGoWELrm7DqChoyxVnUqShI-A5NZ3lUQ4kWBRLkmE29uPyhWJR69XFqqyClTvR4FqWXY2pMWI5sHujYKtM9pHOPtE72MRRSoEs2u29o82ynfdQVExuatoXYmGj9LApVNS4nl9d-VuOuIX1GkL3f2aXJD39ynHMynz4DHYGXV97vq1W1QwZxiK8PDPLWktO_zxqcT_GG1GoRIH1WQXwivbFWmKhvqaOu3XTWaWwakPZbz1FpyfhXptW5vQeyTw-ZPYYzRpZ4JCj42PF5ubOkEGYKSptWGhtW4sggHCxkrzjCNOQmvfamkgBoIHpps9-f3W8zdJyplOd2RB6Id8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0977608af.mp4?token=M3Mfr1YOblleYGMkPiuUUC2Ynf216kNnfRHxv23KKTbr-rXdZA4sBrw7WdDCk14Zin6_54GJXGohBsX1u_ts6SQaa7ScuacML8woKmxpXvKjSe4T_UCWOwaRy11mAlL1EFyQmHRv4GhJoLx_GCUmbkn0oYosq3xVsX5rrkBqaF3QNQpTSq_-j61vlpme_o3wYTsoDmGY-u2bvA3nZm9YzZj-PCo1w029QLsSALTdobVSXsa1iRe64GdRNMBTu89TfNc03azZMpxXs958O7Ntp7na_CxOoHTKDYDTVPnpeh5-OJBcEh3wimo7FwWEYnLj7ZjivLVObghHd7FVCquFJjn1u_tGoWELrm7DqChoyxVnUqShI-A5NZ3lUQ4kWBRLkmE29uPyhWJR69XFqqyClTvR4FqWXY2pMWI5sHujYKtM9pHOPtE72MRRSoEs2u29o82ynfdQVExuatoXYmGj9LApVNS4nl9d-VuOuIX1GkL3f2aXJD39ynHMynz4DHYGXV97vq1W1QwZxiK8PDPLWktO_zxqcT_GG1GoRIH1WQXwivbFWmKhvqaOu3XTWaWwakPZbz1FpyfhXptW5vQeyTw-ZPYYzRpZ4JCj42PF5ubOkEGYKSptWGhtW4sggHCxkrzjCNOQmvfamkgBoIHpps9-f3W8zdJyplOd2RB6Id8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بردسکنِ خراسان‌رضوی درقاب ۲۱۶ شب همراهی مردم
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/465882" target="_blank">📅 20:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465881">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8fd25655c.mp4?token=BrBWhRqpeZTLnexygM2LdX0LfNrE9xI0YbUAsQ7D9PpZlj66m6rlPpPVmVtUH2RiFKxvAP9M4E1ksNZVdnnPPElT3-HH_sY9im7-XeHQvIR36PUzYbsD40WryjARL1CycGFUfNqB2nERdINE40c4ssoegSnkWgz-CnJz-53Cd6H2I4Xdze-z1y_PY6QYQdUuTqtSXNqO8W_I9xf7n_U0pCbCHukBB-Z_OO1Oh8YIY1WDqQFIfa1-qPn0ySLQYKmNFjx_7HnNu22PM0Hj0ROO4EKPYlRanXxB7FMyXtZ5rIQAMAFcnbHf65mGTse-kmWQLXexrNn8xy3xck3aHdaeaRQqBnrcuxs-vmHInJ8MU4MEbEgyLAgK4BMSfoHzkv0DWpYqMH1YJRJtXEvCNbyci22b8X24CLmskq0OM1rUFoFiMtKJdOG4JHxpBnCJ38dW9ZNpHmec0lq6aPjHiGVOD5_BdnX1iPVPxAk8i5D6w8BArbZJxQXM3mCEIQU8v0_en8-5QCSOxHqjipoG3ZUHA-skq9Ipr3EXdklq0qELB4zOV3CgInvPp97VKPZea2Oo-fIIUFTjK36iR-7BmXW47j-J0ujdpbUxjUBHTCfIfoIDUPlftzjpDnxlTMd-rqplUvgPf6x9prI0VPxXjdPXBbxwjkHGjdjpG6qVr64wr4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8fd25655c.mp4?token=BrBWhRqpeZTLnexygM2LdX0LfNrE9xI0YbUAsQ7D9PpZlj66m6rlPpPVmVtUH2RiFKxvAP9M4E1ksNZVdnnPPElT3-HH_sY9im7-XeHQvIR36PUzYbsD40WryjARL1CycGFUfNqB2nERdINE40c4ssoegSnkWgz-CnJz-53Cd6H2I4Xdze-z1y_PY6QYQdUuTqtSXNqO8W_I9xf7n_U0pCbCHukBB-Z_OO1Oh8YIY1WDqQFIfa1-qPn0ySLQYKmNFjx_7HnNu22PM0Hj0ROO4EKPYlRanXxB7FMyXtZ5rIQAMAFcnbHf65mGTse-kmWQLXexrNn8xy3xck3aHdaeaRQqBnrcuxs-vmHInJ8MU4MEbEgyLAgK4BMSfoHzkv0DWpYqMH1YJRJtXEvCNbyci22b8X24CLmskq0OM1rUFoFiMtKJdOG4JHxpBnCJ38dW9ZNpHmec0lq6aPjHiGVOD5_BdnX1iPVPxAk8i5D6w8BArbZJxQXM3mCEIQU8v0_en8-5QCSOxHqjipoG3ZUHA-skq9Ipr3EXdklq0qELB4zOV3CgInvPp97VKPZea2Oo-fIIUFTjK36iR-7BmXW47j-J0ujdpbUxjUBHTCfIfoIDUPlftzjpDnxlTMd-rqplUvgPf6x9prI0VPxXjdPXBbxwjkHGjdjpG6qVr64wr4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله سیدمجتبی خامنه‌ای از نگاه مادر همسر شهید رهبر انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465881" target="_blank">📅 20:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465880">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8jNij69LmafIjDa4rlVcUSpGQsaRevYv2Lqf5BmUtSpTSs4nYuIY65VWWrHysvV5sChKDc-ZmpFaM591GRJRJlDidQWaR-iuiEIlWaZ_6f0a-SGD_Z4DkCaOLo_0ndjYdSXE5pygeho9JEXYoT8VJh_Io9LviF01deTmSzkk_ucbzFjOsc1Pr4ePsmrqUbH45vT3kMDkIQfk46PBMwmA2b2C3wlpyhEzdZJq4XiHhqBHBD2dUJzXHhsxrl9TAWeZ753kNu2pPy8qg25fe26aFqw0DCk1pwKFJofXyJxIFqoitIt0yMOlRKxCUVCvjsN9oAilNloe7DxW6qFyA9gAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی انگلیس: یک نفتکش هنگام خروج از تنگهٔ هرمز بر اثر اصابت یک پرتابه ناشناس آسیب دید و دچار آتش‌سوزی شد.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465880" target="_blank">📅 20:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465879">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec41398a0.mp4?token=f3cj0h-uANj7FcMy0Eh5VYScfnq15Yn_HyP6m4W8DZwwFrPX-tQn6n-MrGv1LLRmS5Mybx-hQMV6W16p6D_SGM2AOtcP61T1Fu8G-tVCOev7OrEdHhYjVaJNwNYAdfK9T_2n0R66laaDaQ1K_c_SlN5k2YTKOVxw9VupkyhgMzLrzVpjloiXkB5laq4Zl_Kf1wHgYZU0_d5EMciThHnYbzN_lZN9r-PqJZeDaJPip6boNYOOtI-CMfdCcF-cwHYXtGKArCfmWSyT1ihdXXcB_on-sUfLEcHgpQcpvwJ_oioYH3llQvTl109Rb4umJY11dGbxnKP72A7LWBMy_51QPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec41398a0.mp4?token=f3cj0h-uANj7FcMy0Eh5VYScfnq15Yn_HyP6m4W8DZwwFrPX-tQn6n-MrGv1LLRmS5Mybx-hQMV6W16p6D_SGM2AOtcP61T1Fu8G-tVCOev7OrEdHhYjVaJNwNYAdfK9T_2n0R66laaDaQ1K_c_SlN5k2YTKOVxw9VupkyhgMzLrzVpjloiXkB5laq4Zl_Kf1wHgYZU0_d5EMciThHnYbzN_lZN9r-PqJZeDaJPip6boNYOOtI-CMfdCcF-cwHYXtGKArCfmWSyT1ihdXXcB_on-sUfLEcHgpQcpvwJ_oioYH3llQvTl109Rb4umJY11dGbxnKP72A7LWBMy_51QPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله سیدمجتبی خامنه‌ای از نگاه مادر همسر شهید رهبر انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/465879" target="_blank">📅 20:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465876">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فلای دبی پروازها به تل‌آویو را تا اطلاع ثانوی متوقف کرد
🔹
فلای‌دبی که روزانه ۱۰ پرواز رفت‌وبرگشت بین دبی و تل‌آویو داشت، به‌دنبال حادثه پرواز جنجالی چهارشنبه گذشته پروازهایش را تا اطلاع ثانوی تعلیق کرد.
🔸
روز چهارشنبه ۳۰ سپتامبر، هواپیمای فلای‌دبی از دبی به مقصد تل‌آویو با ۱۷۴ سرنشین درحال پرواز بود که درپی درگیری میان خلبانان در کابین، مجبور به فرود اضطراری در فرودگاه تبوک عربستان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/465876" target="_blank">📅 19:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465875">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac579fbaa9.mp4?token=MukpIkbGvB_fdBa6o-vZlxHM18JkZtiVHgieQZ79c5rzkgbOK0HR6_VIzN2a2vbvvRCgXdLdF5FYx7tRC9A8PVTNeJujcHUmcBAUleWr2b3GtJoFvxSZ1XcMJyugLLqmNcKBJdieK3sM_j3XNQoYJc4MFPL5Qz2Y8TpcPpMfFIU_4pEKzgp6OZMe-KMjyh_5GicoxfkyfbQU5DtkWpDzgm33StZgzbCRKptES2DiEVw_7LRK0q22NL5d_-Dxc72Knwczbmwm-q8545a3-P0wA1L3WFKyQglCXdUtesWBJreK8fmJ3GMT8SF5Lg8QbY2hTmkuQy2KHHfnNJacxzfL6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac579fbaa9.mp4?token=MukpIkbGvB_fdBa6o-vZlxHM18JkZtiVHgieQZ79c5rzkgbOK0HR6_VIzN2a2vbvvRCgXdLdF5FYx7tRC9A8PVTNeJujcHUmcBAUleWr2b3GtJoFvxSZ1XcMJyugLLqmNcKBJdieK3sM_j3XNQoYJc4MFPL5Qz2Y8TpcPpMfFIU_4pEKzgp6OZMe-KMjyh_5GicoxfkyfbQU5DtkWpDzgm33StZgzbCRKptES2DiEVw_7LRK0q22NL5d_-Dxc72Knwczbmwm-q8545a3-P0wA1L3WFKyQglCXdUtesWBJreK8fmJ3GMT8SF5Lg8QbY2hTmkuQy2KHHfnNJacxzfL6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یامین‌پور از سفر به لبنان و نقطه صفر مرزی در سالگرد شهادت سید
حسن نصرالله
🔹
مردم مقاوم لبنان، مشتاقانه درباره حضور مردم مبعوث ایران در خیابان ها سوال می‌کنند.
🔹
ما حامل هدایای چفیه و انگشتر متبرک به دست و دعای امام سید مجتبی خامنه‌ای برای مردم لبنان بودیم.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/465875" target="_blank">📅 19:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465874">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">برقراری ۴۰ پرواز به صورت روزانه از ایران به نجف اشرف
🔹
خبرگزاری رسمی عراق به‌نقل از دفتر نخست‌وزیر این کشور گزارش داد که به شرکت‌های هواپیمایی ایرانی به‌جز شرکت ماهان اجازه‌داده‌شده روزانه ۴۰ پرواز رفت‌وبرگشت از ایران به نجف و بالعکس انجام دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/465874" target="_blank">📅 19:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465873">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26710743e8.mp4?token=ZnSRmaR_ZyU0guDMc_a01iyNBJx9i0WeaLay8z8ax_YHiQsXWDs6JtmK92FBStN-GeABsBHrcFujxFByJLX_HwSlPQqs7YWkgw50AurK5qC9iEX3vevpTZIsLdsanU47TWgKE_EWfoZv9KiRZe2I5uf5KaemBqNtP_2gWi1cyG21jeeVMxGtJlVieh1Ow4x6fzygceDVRQJ1sqppGCYCkCd8nn5OzwHzxAgBRMtPwoCgQcY-2z_ruNwket_PZF0wJtPAkTxpgEoj1vh2xZOgzoqGPJ-DbNbYFYF0SKO7JJ5xDy6D_k18b4DverYRbaRfNOzPKc42TXiRAwOKTb5jtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26710743e8.mp4?token=ZnSRmaR_ZyU0guDMc_a01iyNBJx9i0WeaLay8z8ax_YHiQsXWDs6JtmK92FBStN-GeABsBHrcFujxFByJLX_HwSlPQqs7YWkgw50AurK5qC9iEX3vevpTZIsLdsanU47TWgKE_EWfoZv9KiRZe2I5uf5KaemBqNtP_2gWi1cyG21jeeVMxGtJlVieh1Ow4x6fzygceDVRQJ1sqppGCYCkCd8nn5OzwHzxAgBRMtPwoCgQcY-2z_ruNwket_PZF0wJtPAkTxpgEoj1vh2xZOgzoqGPJ-DbNbYFYF0SKO7JJ5xDy6D_k18b4DverYRbaRfNOzPKc42TXiRAwOKTb5jtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پدر شهید زهرا محمدی گلپایگانی در رواق دارالذکر و اقامهٔ اذان برای نوزاد یکی از زائران
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/465873" target="_blank">📅 19:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465872">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25728690cd.mp4?token=UKS4c8LfR3wHYxFij0pEgyxtq3DAiTA57tK2GjJYoKfkZEjnfcRHQJzVXTsD4uG0IuQSZ1bD_5DCNXmuVGB3KbKjn9ygrCahHl_AzcpbBxSgMIaocDPDITvjdwP1et9CRYMAz107Lvi7TgDm7zyCuoQHnxyix6E_eUZHutPsjLdqv3xBIEeBDsjVgjw-py6-qIg6ZH4J2sQ3PkmhitTgmWpZXBgcbilLNVbQQa6p6zAwRwF-AR-MLoQ1z0U9oy9LRsoK7TZ-6uYwyx-WG-dwHoBloIZvKZ_s21oAMTKDirW2X_zOU-PkybqaJe6EFr4OXG-ouALgeKs2DCDYgW9KpJV2vEhVM2hF03ORvEpjMureM9J6kwnR0J-hgszrI1ZDzhsMsbjBxfaOp9N4GMRUrXBWkR-Av3D_ql4EQzrFkhM2nn2DUwP30JcNaDFYwsze5TCrtKXmGv5sYwYoAT3gyjFdcDiW1pWFcHKQEmnpv_7f1lurWjyGHW7cKHHpfOl_fvw89ELCVh8Dy_AF7JCOQXLBxvO6WKjg9SqgELM5GVldkSekwsAS4qdmunPWPT5-HZJu08Pa-_g9K6nsJ4OIQnKzn0QkoFT55T7F_N4ds7tTENm7n5odcZ7Ug34q22IByEyZukUMo0UGq_QyniXpgMCJUL5w1CSd8waGso8pJyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25728690cd.mp4?token=UKS4c8LfR3wHYxFij0pEgyxtq3DAiTA57tK2GjJYoKfkZEjnfcRHQJzVXTsD4uG0IuQSZ1bD_5DCNXmuVGB3KbKjn9ygrCahHl_AzcpbBxSgMIaocDPDITvjdwP1et9CRYMAz107Lvi7TgDm7zyCuoQHnxyix6E_eUZHutPsjLdqv3xBIEeBDsjVgjw-py6-qIg6ZH4J2sQ3PkmhitTgmWpZXBgcbilLNVbQQa6p6zAwRwF-AR-MLoQ1z0U9oy9LRsoK7TZ-6uYwyx-WG-dwHoBloIZvKZ_s21oAMTKDirW2X_zOU-PkybqaJe6EFr4OXG-ouALgeKs2DCDYgW9KpJV2vEhVM2hF03ORvEpjMureM9J6kwnR0J-hgszrI1ZDzhsMsbjBxfaOp9N4GMRUrXBWkR-Av3D_ql4EQzrFkhM2nn2DUwP30JcNaDFYwsze5TCrtKXmGv5sYwYoAT3gyjFdcDiW1pWFcHKQEmnpv_7f1lurWjyGHW7cKHHpfOl_fvw89ELCVh8Dy_AF7JCOQXLBxvO6WKjg9SqgELM5GVldkSekwsAS4qdmunPWPT5-HZJu08Pa-_g9K6nsJ4OIQnKzn0QkoFT55T7F_N4ds7tTENm7n5odcZ7Ug34q22IByEyZukUMo0UGq_QyniXpgMCJUL5w1CSd8waGso8pJyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانوان جان‌فدای اصفهانی خون‌خواه رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/465872" target="_blank">📅 19:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465871">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6fa95a31.mp4?token=X6LtBjBUjQEWwPCHi6_okkdDu6peMTsfI6LSXVh-ZOedIS8KYuQ31UweSoWqmii6bzQxACcmWwh6u1GBV8uxYSCUB3_-gjEbvzarm9U8uKKj2GlrWsIFXksCjw3h4y_NBBs7LYUw8xGMhwDU7L_yAxmuYtb5eXuGDEjgZZsDgQDWnEGyYA-EigjQLc2Tuyv2xBlKKndGkPz3h-CiBltxsyrsWGM7tctgGEw7Ehe0lRHN5BN5XyFkc0ZwabTi3bFEdUL63K7VZI8unljKRdg2OxWawm8F8m7CEgmxTsLNxL0xcmOlNKM4hB9Kyoaz7NdOL9_uWEh8pg9CSXBHQvYUTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6fa95a31.mp4?token=X6LtBjBUjQEWwPCHi6_okkdDu6peMTsfI6LSXVh-ZOedIS8KYuQ31UweSoWqmii6bzQxACcmWwh6u1GBV8uxYSCUB3_-gjEbvzarm9U8uKKj2GlrWsIFXksCjw3h4y_NBBs7LYUw8xGMhwDU7L_yAxmuYtb5eXuGDEjgZZsDgQDWnEGyYA-EigjQLc2Tuyv2xBlKKndGkPz3h-CiBltxsyrsWGM7tctgGEw7Ehe0lRHN5BN5XyFkc0ZwabTi3bFEdUL63K7VZI8unljKRdg2OxWawm8F8m7CEgmxTsLNxL0xcmOlNKM4hB9Kyoaz7NdOL9_uWEh8pg9CSXBHQvYUTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور ژیلا صادقی و راحله امینیان در خانه شهید علی زنجانی، از شهدای ایرانی حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/465871" target="_blank">📅 19:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465870">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38a1db01fa.mp4?token=VxJjTwTy0ZYNAngXZ2h0aWmteEZzgTBOl17yH8yiMbEX6H_Ns482knaM3gjAn_ugCqjW3QJ0Umy1hxGY8esUpp0v8y4xprseZxbI9r6UZ8nU8WOsfi49RZfUdkvlz3kmCqshsAhfx7qPlNC85qN2GXbR-VN5jLgyXGsQhfFk7NxxRfDjuvaWyzmtdYxSGrdL_GIbbwa1YPoT8fEeJ_Ky7zHJ9o-4F-Z9MVU5iodwJPueGhE_0bA5OhvE3M8lYWn7SW_0BgAaF67HixT6VHvNPrlAMXDTnfOZ6uv4C657qZ2clIiKkTTr3MTtftuoR2aaVBVZNbablPBNDjvbwkj8hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38a1db01fa.mp4?token=VxJjTwTy0ZYNAngXZ2h0aWmteEZzgTBOl17yH8yiMbEX6H_Ns482knaM3gjAn_ugCqjW3QJ0Umy1hxGY8esUpp0v8y4xprseZxbI9r6UZ8nU8WOsfi49RZfUdkvlz3kmCqshsAhfx7qPlNC85qN2GXbR-VN5jLgyXGsQhfFk7NxxRfDjuvaWyzmtdYxSGrdL_GIbbwa1YPoT8fEeJ_Ky7zHJ9o-4F-Z9MVU5iodwJPueGhE_0bA5OhvE3M8lYWn7SW_0BgAaF67HixT6VHvNPrlAMXDTnfOZ6uv4C657qZ2clIiKkTTr3MTtftuoR2aaVBVZNbablPBNDjvbwkj8hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانشجویان در میدان «جان‌فدا»؛ حضور نسل جوان در رزمایش البرز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/465870" target="_blank">📅 18:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465869">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c247275233.mp4?token=R0e_9glt3e4_TSTLtYXcGTXO4usHqcB0p3fTP9O7xi_mX4lhNKA14AZeW-MyTnx1rjI2pz3A223y98KGVspTk1TqaTbz9LClMY6BoA4RGPWF0_SCAKawUeqeGU4W6wfye_L3AFB6m4jjPYocHc79y0FnZh2sjyeWBSYsRVy3L3j-pAAkHW1qF0widjsw03mgGB1HGkpHT7ctJVuQGs2ULQLVFxn05i_MfSPueoLJz6IunMNqZMs0NRSXuc-2LVj6JB6DU-3xSVWrlW9SXgAGSJMbp0fPxXS-bAI_p06_HwY7C3O_begPPISzRbjfCP1Yz7goVRjzLcG8YwmVAFQkRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c247275233.mp4?token=R0e_9glt3e4_TSTLtYXcGTXO4usHqcB0p3fTP9O7xi_mX4lhNKA14AZeW-MyTnx1rjI2pz3A223y98KGVspTk1TqaTbz9LClMY6BoA4RGPWF0_SCAKawUeqeGU4W6wfye_L3AFB6m4jjPYocHc79y0FnZh2sjyeWBSYsRVy3L3j-pAAkHW1qF0widjsw03mgGB1HGkpHT7ctJVuQGs2ULQLVFxn05i_MfSPueoLJz6IunMNqZMs0NRSXuc-2LVj6JB6DU-3xSVWrlW9SXgAGSJMbp0fPxXS-bAI_p06_HwY7C3O_begPPISzRbjfCP1Yz7goVRjzLcG8YwmVAFQkRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واژگونی یک دستگاه کمپرسی در محدودهٔ سد نرگسی کازرون
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/465869" target="_blank">📅 18:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465868">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
حواشی بازگشت بیژن مرتضوی و فاطمه معتمد آریا و خالی‌بازی سکوهای طلا
🔹
در قسمت چهارم «پشت صحنه» گپ‌وگفتی داشتیم درباره بازگشت بیژن مرتضوی و فاطمه معتمد آریا، خالی‌فروشی سکوهای طلا، باخت فوتبال ایران مقابل کره‌شمالی، لغو پروازها و تیک‌وتاک الزیدی با آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465868" target="_blank">📅 18:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465867">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">متلاشی شدن یک تیم تروریستی در سیستان‌وبلوچستان
🔹
روابط عمومی قرارگاه قدس نیروی زمینی سپاه: با اشراف اطلاعاتی دقیق، یک تیم تروریستی که در ارتفاعات غرب شهرستان راسک مخفی شده بود توسط پاسداران گمنام امام زمان (عج) شناسایی و طی یک عملیات غافلگیرانه مورد ضربه قرار گرفت.
🔹
درنتیجهٔ این عملیات، ۲ تن از تروریست ها به هلاکت رسیدند و تعداد دیگری تحت تعقیب قرار گرفتند.
🔹
تیم یاد شده اقدامات تروریستی متعددی را در کارنامهٔ خود داشته از جمله در اقدام تروریستی اخیر خود، عبدالرئوف اسحاقی پاسدار بلوچ اهل سنت را به شهادت رسانده و همچنین به ایست و بازرسی شهرستان راسک حمله کرده بودند.
🔹
این تیم تکفیری تروریستی همچنین برای ترور عزیزان بومی حافظ امنیت استان طی روزهای آتی برنامه‌ریزی نموده بود.
🔹
لازم به یادآوری است از مخفیگاه این تیم تروریستی یک دستگاه استارلینک و مقادیری سلاح و تجهیزات تروریستی کشف گردید.
🔹
قرارگاه قدس نیروی زمینی سپاه اعلام می‌دارد خدشه در امنیت مردم عزیز استان سیستان‌وبلوچستان خط قرمز بوده و تیم‌های تروریستی تحت اشراف اطلاعاتی قرار داشته و در زمان مناسب به سراغ آن‌ها خواهد رفت و از هیچ تلاشی برای انتقام خون عزیزانمان دریغ نخواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/465867" target="_blank">📅 18:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465866">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599fd9e125.mp4?token=l51kfUL8r2iSp0yFlxN4W0A7W44OPENwa8zGKpin5-PAkpG8rPnENv5eZUYeIPm9XZw0UQi5cNKC5zvqmKKPToHhWy_goIBY_vI5JxIOK7-lU8lcMrRJYB673nHOU4ZXlwXsrBAs4sWuYIuUltBu94--kegD0nULUrnUyy-rrwevP36lhxPsuZanAn7s_EXh6pQ7BiFVaaTeSFocWzE_H69GNNHDVvRufUAeM3hLyI3DUqzLrEwel9U9diOUuQVh1knudLnKyVAePRsvUrZovnWJ3U7Yxm8cFWq9ZSzEvHrDr54CB3iOMIh-nwxvXzo1sa0GE7FNRXkYSUJJFCGsKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599fd9e125.mp4?token=l51kfUL8r2iSp0yFlxN4W0A7W44OPENwa8zGKpin5-PAkpG8rPnENv5eZUYeIPm9XZw0UQi5cNKC5zvqmKKPToHhWy_goIBY_vI5JxIOK7-lU8lcMrRJYB673nHOU4ZXlwXsrBAs4sWuYIuUltBu94--kegD0nULUrnUyy-rrwevP36lhxPsuZanAn7s_EXh6pQ7BiFVaaTeSFocWzE_H69GNNHDVvRufUAeM3hLyI3DUqzLrEwel9U9diOUuQVh1knudLnKyVAePRsvUrZovnWJ3U7Yxm8cFWq9ZSzEvHrDr54CB3iOMIh-nwxvXzo1sa0GE7FNRXkYSUJJFCGsKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راحله امینیان در ضاحیه بیروت: هرجا رفتیم، اولین پیام خانواده‌های حزب‌الله سرشار از محبت به مردم ایران بود.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465866" target="_blank">📅 18:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465865">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PARAyUXq9FFTTEBjdwBGUc4g-bLdc-rEMlTVVe268G9x9dgab80hKJvws0Qt4v5G1pUWjnM0XwjS8UScYJufaexB6Fahr_ZrWAQy-VO3kPH0szPwZDIhicXVk8giwe8eEmYYVdk4zaHzXqT4iCnPsRew_MEiOURTqoy7JnP-IzVa_JeQXvSxLors0alDeAPRWRDBlrN8f1Udl6hp4bLxP5aqG3DD1ljeT2PNikdS5_MRiFtpHFnnbH5c4x71YVr-ykd5hXkj3s-mXdo1lDU4ew-mdWG83DOOB3OkEjSpmkrEXhI_Zl_lEbW0QmK7ha7gRRm9STPV9xPP5Hx_IIy2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف محمولهٔ سلاح جنگی در کرمان
🔹
فرماندهٔ انتظامی کرمان:  تکاوران پلیس با استقرار هدفمند در ایستگاه بازرسی پنگ، خودروی سواری پژو ۴۰۵ حامل سلاح را شناسایی و طی یک عملیات ضربتی متوقف کردند.
🔹
در بازرسی از این خودرو، ۳۴ قبضهٔ کلت کمری به همراه ۶۸ تیغه خشاب مربوطه کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465865" target="_blank">📅 18:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465864">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv1yxLjhbWCtHMP-4YW7uA15pnlJ3VPu0TcUxiFvbdtOVRQfZ2Za7czVcJzo_GuuDUP3IxhgbrBt6f08p1Ov0O_kNLtxsOxBT0xBzKx4xin7MCiOXk6TFjgJXSK_f4o7m7KOnY1qcKXQJF2BOLEXSEKxAvSe2KR-JqYbFQGTGh9XpsLcpTRA5iIIYCrW7eNsbzYBjEb0pEI-N_KZWjK2jO2H5QOopg8M5S9dwXU55aFAVhcdXQpBiX-dQJNqSVZM0MXLiUd8tmgB0EBvtA2-40N3tt5HNdtBoImNNN_NgI-7y8HDg15eAy8RTgD9ylqKsCi9owxY1GRuX59rGyfdqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از سرلشکر شهید محمّد شیرازی، رئیس دفتر نظامی فرمانده کل قوا در کنار حضرت آیت‌الله العظمی شهید سیّدعلی خامنه‌ای
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/465864" target="_blank">📅 18:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465863">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d2d934eb4.mp4?token=oLKtSap61fLawYbMePh6YyNFbxy-iidDgae1fBsRn0BTYciRLnaqkDoUOMm_VrFax-wi3_aKAfJm87rWrsC-Da70cA4T1RBnVgJZo6X1qXlwt4sNRS4dPjmxN5rJFHxINjjDWo8frsDRBpLlI7rUe9UI646lFpG_-FLfpDcQHYPVafcluaja43mdvWX8IvwcRqstOBL2JFwwZxzed2Z2PifQM15XL29fJ8n5NgKQcBqic0KoCTlAhrTWmZp-_YlIlVZ_vKCsfRpCjMlGj67eB20e9bRtq-yzgC4thRXmZ2m7420jI9XDViKvnsk9cW_TrgnmE0QiRoZf3yp9uPIrlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d2d934eb4.mp4?token=oLKtSap61fLawYbMePh6YyNFbxy-iidDgae1fBsRn0BTYciRLnaqkDoUOMm_VrFax-wi3_aKAfJm87rWrsC-Da70cA4T1RBnVgJZo6X1qXlwt4sNRS4dPjmxN5rJFHxINjjDWo8frsDRBpLlI7rUe9UI646lFpG_-FLfpDcQHYPVafcluaja43mdvWX8IvwcRqstOBL2JFwwZxzed2Z2PifQM15XL29fJ8n5NgKQcBqic0KoCTlAhrTWmZp-_YlIlVZ_vKCsfRpCjMlGj67eB20e9bRtq-yzgC4thRXmZ2m7420jI9XDViKvnsk9cW_TrgnmE0QiRoZf3yp9uPIrlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت یامین‌پور از دیدار با خانواده شهید هشام عبدالله؛ می
‌
روم انتقام خون آقا را بگیرم
وحید یامین‌پور نوشت:
🔹
شهید هشام عبدالله، گفته بود زندگی بعد از آقا را دوست ندارد، در وصیتنامه نوشته بود: یاصاحب‌الزمان میدانی از رفتن سیدعلی سینه‌ام چقدر تنگ است و چه اشتیاقی دارم برای پیوستن به او. نوشته میروم انتقام خون آقا را بگیرم.
🔹
هشام اسم جهادی «قنبر سید علی» را برای خودش انتخاب کرده بود. ۱۰ روز بعد از شهادت آقا، هشام شهید شد و ۱۰ روز بدن ارباًاربای او روی زمین باقی ماند.
🔹
پدرش از همان اول اشک می‌ریخت. می‌گفت ما همه در همین خط شهادتیم ولی هشام زرنگتر بود.
🔹
گفت روز قبل از شهادت هشام، خبر شهادت برادرم را دادند. چند روز بعد خبر شهادت دامادم را. دیگر توان نگاه کردن به چشم‌هایش را نداشتم. حاج سعید روضه علی‌اکبر(ع) خواند. وقتی گفت «علی الدنیا بعدک العفا» انگار حرف دل پدرش را زده بود؛ حرفی برای گفتن باقی نمانده بود...
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465863" target="_blank">📅 17:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465862">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu1qpTAMwNNGE8lb2kOLAw8yW8kybpL6CaWwfwVLxxTQ0dS8_CijJkeOB2z3kzO5l84eQdweZ2MfY0j7u0hWPN8KvRKJle-VY8qGuqUjtKh9GWqp4gX2Yw_dQIoEO8E_It8wHAe876tV0Ep4vzuCxH18YP8s-Ut2cIE9jktikoo4Do3rZYri7g_Ds5fxnxK0PL5jZltAEBggNxJWwkD1OekTpC8w__1BgmLGeMxXCVrulQbvxLVTrzCso6X9gVxnbqOKK2NhOgnY2MCs4cLjnlGKrLhreL0x3P5cfbejE3tM1UDeKhvFFRbqSlNElPXNdUCDrPVHsm-0psaq95r3LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای کاهش قیمت گازوئیل دست به دامن اروپا شد
🔹
دولت ترامپ از آلمان و فرانسه خواسته برای کمک به کاهش قیمت‌های فزاینده سوخت در بازار جهانی، بخشی از ذخایر استراتژیک گازوئیل خود را آزاد کنند.
🔹
دولت ترامپ تهدید کرده در غیر این صورت، احتمال اعمال ممنوعیت صادرات…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465862" target="_blank">📅 17:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465861">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3v0FatsvtlHIHFCWBn-Bndh8d1SBugoyO7MBXeuiXVsVo8YbPWRgOi_kqol_wzC_67I_4dmwXRq7B9p1XALPYai6MvymvDNAF1t03CnvCIPp9Kk0wcWOkfh6PArnRIlLw9Q0td8ho2DbU5Hi2WZZNwYua5IaRJub72CwWAcVt2rqQNrJ_kZXxsuayuC34VINmR6OhkQjWrc3ygy4MV55ohpXVoq_1QOg4eqhhA2zUfu-2MvCcvgXTBoyU2bpem6s2u0798itKnuSogdC5c1Bwde2hIVCii4I-Wz0wSUI18O9jJX9VqIJtwmxrW_vaxq_LVikbRgPs7JO2yC4sxrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توهمات ترامپ: ایران آمادهٔ تسلیم شدن است
🔹
رئیس‌جمهور تروریست آمریکا مدعی شد: ایران آمادهٔ تسلیم شدن است؛ ما الان می‌توانیم به راحتی پیروز شویم.
🔹
من معتقدم بلافاصله پس از انتخابات پیروز خواهیم شد، اما شاید حتی پیش از انتخابات. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465861" target="_blank">📅 17:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465860">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UemRI4LfinBOgLcQJsV0hnG6wXtNUbZHwgkTnyKufpjF3IgXJxh69kfpt3rVpay9sh7qWGHb2hFy3-qBOVG96V5b4PKNfvfSknLDn6qFosjzm_N6pauld1iI-PvY4aKq7h9fdqHwhEWTyi5uDjGgtr4qIvZalsafcG4hlDI8UuiJ_hfEfPvBvCPLRJTfBCkX2p0rgIryzQr7k5sIqYNBJfsrpJEnWyqTq2IL6rldzHMpMwacvlB2I71nxfsgPBomvzHBO_iqJvZ1Z2XWUqVCDdfl1jy_nVhajdPXuVb7LByohv4MHDBkFinQ9WkTfb2DTlIAXyY1wGS50BZXcvIuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بوسۀ دختر طلایی تکواندو بر پرچم ایران
🔹
دور افتخار ساغر مرادی با پرچم مقدس کشورمان پس‌از کسب مدال طلای بازی‌های آسیایی. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465860" target="_blank">📅 17:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465859">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XieAjr2WSLasn7S5akgqDbgt3PRbxBjo7-30mvDdK4NyDp-_MpEmhllRgR0-Uffey3SjauzESPUZ3RbaSZxGuEdEzXjK5EKIRgKj5OkMOI8cuDorxbfbJJ8t1TOb5i15X8wtHdiAxhEBf93MUb6keLyptA_vFa89FRIVd9rwGqaCAgd73XKPmG4n9xQBDLWTZLUa6YcECIDLBYZwtX7AFvMyjAZLfTaibeGsAFkNderghGD9hq2t5DfmHRLR2x8H5-phmA_r1ym-RqHg4CXmQJgccxHIFn-oR9ypEovk7wDGd3TwleKv1DK4pFLJsDvhUI6t6cnMvylthrHylVQ-Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این محصولات آرایشی و بهداشتی را نخرید
🔹
سازمان غذا و دارو با اعلام فهرستی از محصولات آرایشی و بهداشتی از شهروندان خواست از خرید و مصرف این فرآورده‌ها خودداری کنند.
شامپو:
🔸
Loreal
🔸
Moluoge Oil
🔸
SUKIN
🔸
DISAAR
ماسک و کرم مو:
🔸
Pantene
🔸
Moluoge Oil
🔸
ECHOSLINE (Ki-Power Veg Mask)
🔸
RESTOREX (Hair Mask)
روغن و سرم مو:
🔸
Pantene
🔸
Loreal
🔸
ARMAME (Keratin Argan Serum)
🔸
ENZO (Hair Serum)
🔸
LOSSOFF (Magic Complex)
روغن و سرم ماساژ سر:
🔸
Max Lady (بادام، شترمرغ، جینسینگ)
‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/465859" target="_blank">📅 17:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465858">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwmrJsS3dM7deCJCaXMBdkwZ5PF_Nwk3NvWsaJnG5aCQjO69bJNIpQ7JELt2rkT7zxEKDVIqbQ7wOlIjkNjhWjxXNWezyd3iZrBM3tE6HFd00M3n2L5PyA8vau6veXHj8BICvfQWUab7tb3ikEU2RbknDHa5QnwQrvU06MaTaHlXsXhPDGFnlAKfPcrZqpoYx2T9__Lx9rViZ6-6AhqAS-0pwX-RnNwUn0UfOD7wAqkvud3DK9vWGOHoQoJ0tJ-7bBMQaYliF76QzhpBgooPOiCi6jl05c7pky6Cp8auUtrtw8po_9Eqzdh_ITaa8uRjmxDaojGxhrjEJLXRUVe0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراهی پاکستان با آمریکا در مسئله تنگه هرمز
🔹
وزیر امور خارجه پاکستان که کشورش مدعی میانجی‌گری برای پایان جنگ تحمیلی آمریکا علیه ایران است، با موضع واشنگتن علیه تهران همراهی کرد.
🔹
محمد اسحاق ‌دار ضمن مخالفت با کنترل ایران بر تنگه هرمز، خواستار بازگشت وضعیت این آبراه به زمان قبل از جنگ تحمیلی آمریکا علیه ایران شد.
🔹
رسانه‌های پاکستانی به نقل از وی گزارش دادند: «عبور کشتی‌های تجاری [از تنگه هرمز] باید نامحدود و بدون هیچ گونه هزینه و عوارضی باشد».
🔹
وزیر خارجه پاکستان در بخش دیگری از صحبت‌هایش درباره «پیمان مکه» نیز گفت: «کمیته راهبردی، سیاسی و دفاعی تحت توافقنامه مکه به زودی در ریاض تشکیل جلسه خواهد داد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/465858" target="_blank">📅 17:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465857">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e6b308b97.mp4?token=MbfMul3nB6de7aSGzakAq_Hm7mZ6xsn4Itm2jrj1f-nckGd00U5gGMG4m8y8_u3I6Ih5q3LG-ILRC6kD2nLaYNl60P8tAJpMgFhWQqcTsJ-8vuISDpUg9tEp9rwqMDmGxJoLaVDtsSpPra_N7SG5TRBKBC61X4RwkB9nwu73TQ1QoxU_IWVhMTTsNLS8kMdkh_PstJU_4Oq3qbB-F2zGb1xlE_0xUZfNjFF6kJdB0z_v1xmwF00Bt4qHhREVwf683-GL35CnkaLb94oKQ4ksn6YbxCEUwoHg-82TcQakmwHDQyCYsCW3rR6lALR-X5HpzFD_8v5-1aJWSDTEECszPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e6b308b97.mp4?token=MbfMul3nB6de7aSGzakAq_Hm7mZ6xsn4Itm2jrj1f-nckGd00U5gGMG4m8y8_u3I6Ih5q3LG-ILRC6kD2nLaYNl60P8tAJpMgFhWQqcTsJ-8vuISDpUg9tEp9rwqMDmGxJoLaVDtsSpPra_N7SG5TRBKBC61X4RwkB9nwu73TQ1QoxU_IWVhMTTsNLS8kMdkh_PstJU_4Oq3qbB-F2zGb1xlE_0xUZfNjFF6kJdB0z_v1xmwF00Bt4qHhREVwf683-GL35CnkaLb94oKQ4ksn6YbxCEUwoHg-82TcQakmwHDQyCYsCW3rR6lALR-X5HpzFD_8v5-1aJWSDTEECszPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سالمندان از شنیدن این کلمات ناراحت می‌شوند
🗓
امروز روز جهانی سالمندان است. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465857" target="_blank">📅 17:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465856">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
انفجار جدید در تنگهٔ هرمز
🔹
شرکت اطلاعاتی امبری اعلام کرد یک نفتکش با پرچم پاناما هنگام عبور از تنگهٔ هرمز «هدف اصابت یک پرتابه قرار گرفته و ستون‌هایی از دود درحال خروج از آن است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465856" target="_blank">📅 17:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465855">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKWiRmA3laQBIBEW8-vwqLjWVKaaEOyl2wxBT50FJbgpyccAZe0ukibk75qszWFl16OuiXKkZWpGNdcTiLMz_QenYZDlwvZBD7ZPCfta4atoz6gyFJbFNfXbj6ExvUN9dx6UUJa8auz00wU1Z0_NEE8rw1MdRxwYuNM8FoOGE7WZu1xf9TjqDER9ysma7_bvwiTXFJhP40i2UilcdbcBiurX7TU26CLjC0gQZcU5CtSUnEgjga-Nbb3YZX-4EN73T93dVW9z5BVCFbrwW6aQUdhS9VVCWg3C71VCY-QHVd-qRcSWffvTxVowURE1UxWqoktqpjjQ6ih1l7mwJggv4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای کاهش قیمت گازوئیل دست به دامن اروپا شد
🔹
دولت ترامپ از آلمان و فرانسه خواسته برای کمک به کاهش قیمت‌های فزاینده سوخت در بازار جهانی، بخشی از ذخایر استراتژیک گازوئیل خود را آزاد کنند.
🔹
دولت ترامپ تهدید کرده در غیر این صورت، احتمال اعمال ممنوعیت صادرات گازوئیل آمریکا به اروپا را بررسی خواهد کرد.
🔹
این مسئله یک دوراهی دشوار برای کشورهای اروپایی ایجاد کرده زیرا کشورهای اروپایی از یک سو برای مهار قیمت سوخت داخلی تحت فشار قرار دارند و از سوی دیگر باید ذخایر کافی برای مقابله با احتمال تشدید بحران انرژی در زمستان را حفظ کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465855" target="_blank">📅 16:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465854">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzbmg89AhmLpbkoqhaFD13vIIvUBgRbMQJJL-Q8uqOXeXFRygIO0u0OauGClvtrGgQ7LqRgKD_7iMw01p-Z71R5xOEv-Bi3xJIp5Et-nN3HAjCHaU0zvKXpNKzEaKjCV9vQyZK8gqLTTV3OGYRcb_mpnKCRSvdGh_Y6vVuzRepLKfA7A8K3cYdOPP25TR9nFj5xzTvDM2RNWH2cwDZvdAwSVIyN4jyACE3NfIw2uL6tGAdatoiEIoT-RzlHu3AfOILhskhR5U4g04QX9tXcb6wPGvXzcvd4wZgLwyO8Jm3NY2R3GhnNNSh9TXxB1PldSwmaiwNrDPtmuDQhAPFNwRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبض ۵ هزار دلاری هرمز بر کالاهای کشورهای عربی
🔹
با تداوم مسدودیت تنگۀ هرمز، شرکت کشتیرانی مرسک که بزرگ‌ترین شرکت کشتیرانی دنیاست اعلام کرده برای حمل کانتینری به کشورهای حاشیۀ خلیج‌فارس تا ۳۸۰۰ دلار هزینه اضطراری دریافت می‌کند.
🔹
براساس اطلاعیه شرکت مرسک، این شرکت برای محموله‌های مرتبط با بنادر کویت، بحرین، قطر، امارات، عراق و جبیل عربستان و برخی بنادر عمان، نرخ اضطراری تعیین کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/465854" target="_blank">📅 16:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465853">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWAqAY6Bm4morkkWOmRuAJ3e6fVGpLqaCsMHUMuq0FLDoZM99bw0IfRfXPYYw-qHMevtk3cSvtb_M5m7CRXSWjIUh0wL-DEEH0Djs65vLD0iNvRsoQpp7-nh5ko0B4Q-Y_yiFOcDtPVBMEZ0h3jl0QQabTPIGW8julzKTceRpOfHe-wDFIRUXq-z1GgBWyFMHF44ZlFXXNnTIB0pAqiSMwmVzD4mYxrV1v_Pqpb5POKwcQmoIDFk_vHd1NJeZ-Cb6J_75GRgH8msFMroQf2DLu-DYGUCPnrTp3NTF83JdhMzcpZoLn-no11Ng_Zg96z54QwJgmj7smFExCxK8SUZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ کمک‌های نظامی عراق و چند کشور اروپایی را به آمریکای لاتین داد!
🔹
با وجود مخالفت نمایندگان دموکرات کنگره، دولت ترامپ ۵۲ میلیون دلار از کمک‌های نظامی اختصاص‌یافته به چند کشور اروپایی و عراق را به کشورهای آمریکای لاتین واگذار کرد.
🔹
به گزارش واشنگتن‌پست، بر اساس این تصمیم، ۵۲ میلیون دلار از بودجه‌ای که پیش‌تر برای اسلواکی، مقدونیه شمالی، تونس و عراق در نظر گرفته شده بود، به پاناما، پرو، اکوادور و کلمبیا اختصاص می‌یابد. بخشی از این منابع به‌ویژه برای اسلواکی و مقدونیه شمالی در قالب بسته‌ای تصویب شده بود که هدف آن حمایت از کشورهای اروپایی آسیب‌دیده از جنگ اوکراین و تقویت توان دفاعی متحدان آمریکا در برابر پیامدهای تهاجم روسیه بود.
🔹
حذف کمکهای نظامی آمریکا به دولت بغداد در شرایطی صورت میگیرد که علی الزیدی نخست وزیر عراق همواره تلاش کرده منافع واشنگتن را در اولویت خود قرار دهد؛ راهبردی که در داخل عراق با مخالفت و واکنش‌های گروههای سیاسی مختلف روبرو است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465853" target="_blank">📅 16:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465852">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYPoXImg5nar-BvgYXpM0RkTiyq6TMBy3J_Ib0nLQUATTcP3QG61hVzQCJnKh7BFkfrAsUN0qnYdZHintTEcy2g-AC68HjGhfyNd-tFzEUu2nfvLrTy1BqzM6vi2xWOUbvFY_80gyiivWhqGlbEr4lfXCokSxFKaD_wDCnaCqyeph_AUQCLxJCs6uUZqVD2amb7Qul7B8bxOrhaAahXGA4ugMsUXBs11GLM_4_K6qT530KG0sD0rgAacqHOAZzwIBYZ9bDHKieXeLwwuOBfMvCh46WXX2sl9_k-a9NosXPy3CQtPCZNj985ogKJxBQj32li8rartu5YPTdIs4ghDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به التماس افتاد: اگر به من رای ندهید دموکرات‌ها مرا استیضاح می‌کنند
🔹
ترامپ دیروز در جریان سفر انتخاباتی خود به ایالت‌های تگزاس و اوکلاهما، از هواداران جمهوری‌خواه خواست انتخابات میان‌دوره‌ای ماه آینده را جدی‌تر بگیرند.
🔹
ترامپ خطاب به هوادارانش گفت: «لطفاً تصور کنید که من نامزد انتخابات هستم، چون واقعاً در برگه رأی قرار دارم. اگر پیروز نشویم، آنها در نهایت مرا استیضاح خواهند کرد».
🔹
اظهارات ترامپ در حالی‌ است که حتی بسیاری از جمهوریخواهان حاضر در انتخابات هم تلاش می‌کنند به دلیل عملکرد ترامپ از نام او فاصله بگیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465852" target="_blank">📅 16:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465851">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wlme9tbh_UrH_oxRHt1KipHkg7ze-kWgcxwWccDh4LmbFMJ4-LET7aiYNaqB9CHM4bSthrrvHFBiMoA2epFmAMEiu_40SmKupqjTtT1rlS32wB85b7O9Zt0xOmUKFjvQXkGuq5eDizjsm6vbo5P-EC74n-iUgzBkVP4H6UNJD8BjEs6Ua-uLESuiFxmg7vYEvuQCgPn70ymUbVafzVGXOceI8XIG7uoO9xIR0u83vW0DwwB5G8KmDT-6qtTEUgjiWOLnKeIjy2F9svYXG49ZEb6tabg_R1P5FtlFDAEwK-0NArzAxttUNXMfT_Tf0aj3NkiWRICB3i2qyBakCA0oZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: طرح «تورم صفر» با ۱۲ قلم کالا آغاز شده و قیمت این کالاها ۶ ماه ثابت خواهد ماند
🔹
برای هر قلم کالا متناسب با بُعد خانوارهای تهرانی سهم مشخصی تعیین شده؛ برای نمونه، هر فرد می‌تواند ماهانه ۲ کیلوگرم برنج با قیمت ثابت خریداری کند و خانوار می‌تواند از میان…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465851" target="_blank">📅 16:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465850">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98c8bc66dd.mp4?token=HK5ybBb3UvwTs5ioagkBS6_KdKnbnOE43c46JqG-MIaJzUcKsF8cgafZgHIyktklUxIBBI-M_plwNONiCbBSvKPAHmiXVx57nW-6cX65PjzioS1ipLUpZAL-TWjtJ6T88EXGfNXWfQO_I-T8NtNzDVGhcdCZrXiRjxjUH83vp7HIG2wal7Qa8tWIBlOD7o-c_4c9YwdFXZKuO3ipVOvEr-EJdxsFty3VZSBVOvdpfxmM12UX2TgPSpcf0M4qC8UsG6X9ZVaqk8EjrVuZdn-BuJN3Xt2fdSKY3mufJeIW6Wr4IjmDAbYx0Dc4pjicQA_LDZwe1vZOFo8pgdmbLkpztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98c8bc66dd.mp4?token=HK5ybBb3UvwTs5ioagkBS6_KdKnbnOE43c46JqG-MIaJzUcKsF8cgafZgHIyktklUxIBBI-M_plwNONiCbBSvKPAHmiXVx57nW-6cX65PjzioS1ipLUpZAL-TWjtJ6T88EXGfNXWfQO_I-T8NtNzDVGhcdCZrXiRjxjUH83vp7HIG2wal7Qa8tWIBlOD7o-c_4c9YwdFXZKuO3ipVOvEr-EJdxsFty3VZSBVOvdpfxmM12UX2TgPSpcf0M4qC8UsG6X9ZVaqk8EjrVuZdn-BuJN3Xt2fdSKY3mufJeIW6Wr4IjmDAbYx0Dc4pjicQA_LDZwe1vZOFo8pgdmbLkpztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر ایزدی: غافلگیری‌های فناورانه برای دشمنان داریم
🔹
جانشین فرمانده‌کل سپاه: نیروهای مسلح ما به‌ویژه سپاه پاسداران در عرصه‌های زمینی، هوایی، پدافند هوایی و دریایی یک خیزش بلندی را برداشته‌اند.
🔹
نیروهای مسلح از انواع فناوری‌ها استفاده می‌کنند که برخی از آن‌ها در صحنه مورد استفاده قرار گرفته شده و برخی دیگر نیز در آینده مورد بهره برداری قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465850" target="_blank">📅 16:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465849">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmFxpBPeM0CnILhnJSTaN_UCHR0UHdZE4GO1UBHELZx-2PLQtwPFa4BxITWqeipMDAPEQICCTBv5zLwB80Vd22TONIf8kfXL-9_l2AAY8TEGF5aCGMvpoGkLx4FZjIHYHwvRbQsaiMd0KdEBUwi5T-A8ekaoqsjJtX8UT4X53JZwqUTnm7Y9DNhiLt7xDNtcV3zGxALeF2rAqb5E8WKdKH0VlUtZcLzQV65vr723iZcpN5tNmbAIDvz2mbYml60bZ7KqY4SgtayNI0EaI5sxaru9NAypdzTYH5PLdLc2flZG2eyGolbuPgP4gO7PEIE9DjrggcpY6wyR8ozGi9cllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرائتی: در مساجد باید به سوالات کودکان و نوجوانان پاسخ داده شود
🔹
هم در مسجد و هم در مدرسه به پرسش‌های کودکان و نوجوانان با منطق روشن و رسا پاسخ داده شود.
🔹
تقویت حس پرسشگری در آینده‌سازان و رفع شبهات و تحکیم عقاید آنان از لوازم تعلیم و تربیت اسلامی است.
🔹
امام جماعت مدرسه باید با رعایت اصول روانشناسی، ارتباط صمیمانه با دانش‌آموزان برقرار کند.
🔹
سازماندهی امور اقامه نماز در مدارس را می توان به دانش‌آموزان و پدران و مادران آنان واگذار گردد تا بین خانواده‌ها و فرزندان آنان نوعی رقابت سازنده برای میزبانی از نمازگزاران در مدارس ایجاد شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/465849" target="_blank">📅 15:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465848">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMl2hZcA1MGRALlpMXcKY9ot4ElRI3_aGmt5HkdUKDWkk68x0pCq6h8UUwktoOJO5mzmuo_XdwwlOt5Q0E-M3Cphkjr4KrrL3WFsffCOXsG8Bj67oEf1qZL5M4QU8rwxrmSBZjRscFftmH6D8L8ZEqp8DS_KdjB8DD1GHp0vZ-q7VU8yFzw8P0tkzUDQJkbRLZGxxwiUdlWPcqZ1HWUU9wWCAWhoOLD2ilDcwY2ATG5xQn6JRcroKUfJ7BIPI9Q2vEcde2KkPJQlOhlay-6Rzjojh-0S8ryOec7ZrtmKcFe1m1MvCPRd8HKvURUeOxUzlX2CPj8hasFKISiyC5fU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب ‌جمعه تهران: روند پایان حضور آمریکا در منطقه آغاز شده است
🔹
حجت‌الاسلام ابوترابی‌فرد: مقاومت ملت عزیز ایران، محور مقاوم و ملت‌های قهرمان افغانستان، عراق، لبنان، غزه، فلسطین، یمن و همه جهان اسلام، آغاز پایان حضور ننگین آمریکا در منطقه است.
🔹
این جنگ پایان تلاش آمریکا برای تسلط بر منطقه را رقم می‌زند. این نگاه تحلیلگران هوشمند جهان به این جنگ نابرابر است.
🔹
ملت مسلمان منطقه و ملل جهان شاهد بودند که دموکراسی آمریکایی برای ملل منطقه چه ارمغانی داشت و چگونه خون پاک صدها هزار مسلمان، زن و مرد و کودک، در افغانستان و عراق بر زمین ریخته شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/465848" target="_blank">📅 15:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465847">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c33znEM2FzF7M_HYtmXFIeW-kNJcTe-JLR_kjOFTB1Fda1AoqE0buSdBtafGQTkXsojGe8gGjSJaLH9IXEeFg0VLSM0Jsz952922PP4zKqzHxl6ffOgDVccdcZ2QAJKzY0bgv0wDBaFDwE8P8d51QrrpunEOt10ztVzVmBRD9Iiah6RqsAdeUbo2kV3GDzTPnDeTw76m0mYtztWtPhAMfe0femIN0R3YaDPGbK9P_LbfMOr707AvD4pRlInzUJIlKyQMQEHRJA5axI45nXYhK2AwInBsoMGm716vx1EimS3ku-z3XSTkoHmlJVDcX3dWRCr7ZHsatsyL1UEMLPRVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله علم‌الهدی: مسئولان طوری رفتار نکنند که آمریکا تصور کند به مذاکره محتاج هستیم
🔹
آمریکا امروز بار دیگر در محاسباتش اشتباه می‌کند و فکر می‌کند مقاومت مردم تا قبل از نوامبر تمام‌ می‌شود و تنگه هرمز باز می‌شود.
🔹
مردم ما تحت‌تاثیر فشارها و تهدیدات آمریکا قرار نمی‌گیرند و امیدوارم عزیزان مسئول ما نیز متأثر نشوند و این تهدیدات در آن‌ها اثر نکند.
🔹
متأسفانه بعضی از عزیزان ما در مراجعه و مذاکره به آمریکا، ژستی به خودشان می‌گیرند که آمریکا آن را در دنیا پخش می‌کند که این‌ها انتظار مذاکره دارند و به مذاکره و تمام شدن جنگ محتاج هستند، نه ما.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/465847" target="_blank">📅 15:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465846">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124c9623fd.mp4?token=r-jMeWktm1ys2kloqz5aWxs99vAcchAWFzT7kSy_rLvNv_mAi8SL4Aqt_YCLbH1GhQdde6hw4BSlJ0QoYTH-k2Ai6Rjb8lddxo7vSGxMSO6ITKDtLGV1yrIk3WF0N3P_hlXMbERdnGA9CxXxO-CGdXOs_E0WUGTgd0UAUTYLyk2_totLEMaJe60WWcLR6XgdOd0NIsaF8EH05GGIWqrw2M5kI3rme2EZr9nw_QHH31N7ym37ocqvKZ0WgUhIxpxlcxBP3VYvt4WF0rLf4WHFoR2P7PMItWORBDl1mRQz4nURbOxUdB12RWu2_U-1lmZMgOBhHg_aXyZF5DzvIIPK1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124c9623fd.mp4?token=r-jMeWktm1ys2kloqz5aWxs99vAcchAWFzT7kSy_rLvNv_mAi8SL4Aqt_YCLbH1GhQdde6hw4BSlJ0QoYTH-k2Ai6Rjb8lddxo7vSGxMSO6ITKDtLGV1yrIk3WF0N3P_hlXMbERdnGA9CxXxO-CGdXOs_E0WUGTgd0UAUTYLyk2_totLEMaJe60WWcLR6XgdOd0NIsaF8EH05GGIWqrw2M5kI3rme2EZr9nw_QHH31N7ym37ocqvKZ0WgUhIxpxlcxBP3VYvt4WF0rLf4WHFoR2P7PMItWORBDl1mRQz4nURbOxUdB12RWu2_U-1lmZMgOBhHg_aXyZF5DzvIIPK1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت رزمایش جانفدا در کرج
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465846" target="_blank">📅 15:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465845">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gynPG-3jjGEku9qIxxSFrSJ6yuMGtOudNNLRZHjDu3gRd8cfZJzS3z7JpL84NnjWSaE7QY9BHGTGRBA2faPCADTJ-lt8V57xob2M3_RBEP3cS6diqBOsq_06_92Ce-3Kfdx3pHSiwj8fiXmwa6E626U_xv0Z3kejJtTK_NIv6t4kK45uHLj9eBnto1dGzcpr0F5GBkrJgUGkZ_mD290FFgNsxSn1YW1DTCTAa6_0mnhjwbabCmEA77P8xkmLSK9bTkR4HIHAHqFRTJhNyqpuDryji2Oy46in1mKRgyyE5xPqwdAIdID_1dzk7axhLLnzV92qrSREAqzW5vuqPWuC6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخیر‌ۀ گاز اروپا نصف شد
🔹
آمار زیر ساخت‌های گاز اروپا نشان می‌دهد،‌ ذخایر گاز کشورهای اروپایی به کمترین میزان ۴ سال گذشته رسیده است.
🔹
کشورهایی مانند آلمان و هلند ذخایر گازشان تقریبا نصف شده و به ترتیب ۵۷.۹۷ درصد و ۵۸.۸۹ درصد ظرفیت گاز دارند.
🔹
در آمار کلی هم حدود یک‌سوم میانگین ظرفیت ذخایر گاز کشورهای اروپایی در ماه اکتبر ،زمان اوج سالهای گذشته، خالی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465845" target="_blank">📅 15:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465844">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee0d567c2.mp4?token=q9b5zjkOfbdL-RhqjarVhNj1cLKbeajG7-gTRXYR5e9aJh08kvK_MBITRxTEz6EUEfsrRAWiRdmxsUrwPYPNsTbb5HaYhV-l7452oO5Dxrb5mPFUes0Pc84uHwKJYeSucqDKPzO4cS_cnBnEG4Qz-X3fu-sF6nGxqw8VjVspMoQyaRSjreC1doaSYIFGzYR7aARKQJtp7alGqVdIj-8Ii8zCttBhwhjQcDzbvD5DX48ryC18Hp1lVPwWS2EGh5iEJiiW_lVErru-cIvuIuOp1834UNcKT9Vze8xniv5jNLqZ3DVy0Ew-IGcy_99Qk-Dw2d53ngBY0jaRCGoj0TIfVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee0d567c2.mp4?token=q9b5zjkOfbdL-RhqjarVhNj1cLKbeajG7-gTRXYR5e9aJh08kvK_MBITRxTEz6EUEfsrRAWiRdmxsUrwPYPNsTbb5HaYhV-l7452oO5Dxrb5mPFUes0Pc84uHwKJYeSucqDKPzO4cS_cnBnEG4Qz-X3fu-sF6nGxqw8VjVspMoQyaRSjreC1doaSYIFGzYR7aARKQJtp7alGqVdIj-8Ii8zCttBhwhjQcDzbvD5DX48ryC18Hp1lVPwWS2EGh5iEJiiW_lVErru-cIvuIuOp1834UNcKT9Vze8xniv5jNLqZ3DVy0Ew-IGcy_99Qk-Dw2d53ngBY0jaRCGoj0TIfVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آئین سنتی-مذهبی قالیشویان در کربلای ایران
🔹
این مراسم که هر ساله در دومین جمعه مهرماه در مشهد اردهال کاشان برگزار می‌شود و یادآور شهادت امامزاده سلطان علی بن امام محمدباقر(ع) است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465844" target="_blank">📅 14:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465843">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شهادت یکی از رزمندگان اسلام در سیستان‌و‌بلوچستان
🔹
روابط‌عمومی قرارگاه قدس سپاه: تروریست‌های مزدور دشمن با کارگذاری بمب کنار جاده‌ای در یکی از مسیرهای مواصلاتی استان سیستان‌و‌بلوچستان، اقدام به یک عملیات تروریستی کردند که درپی آن، یکی از رزمندگان اسلام به فیض عظیم شهادت نائل آمد.
🔹
روند شناسایی، تعقیب و پاکسازی عناصر تروریستی و مزدوران دشمن، با قدرت و قاطعیت تا نابودی کامل آنان ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465843" target="_blank">📅 14:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465842">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw_bRwTqBIDoYKugIgT888CVcd62mMLDBLdRavy_VS9M2NbYd1aBZcndnd97pxSIM41NaEBuKBT6jRDdbAS4sdhtJ_QsrPD7z4hNWQcmBoQA9Akc8F7bZXbAZOYDeOJVQW8nlYttKwBPLhdV-R_as7jJniZ_70e5bg0LKxReLg_guMuS9KxqdhQWy7JAeIQqDkSdXdLszRlRmEwJSlhDwOYrN42FhUkJjWtZfRxC6KwO_2H7rfGmIVPiUwnq-u6uZiG47y4wAe8C_HYYA0HcFp-n9-82_lEnPzsIGyf6Ju0X-0f3nbb6tyKTDrJQfouZJV_SgJYFBjtYW_Sr7LiCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر درگذشت حجت‌الاسلام قرائتی نادرست است
🔹
پیگیری خبرنگار فارس نشان می‌دهد اخبار منتشر شده در فضای مجازی درباره سلامتی حجت‌الاسلام قرائتی نادرست است.
🔹
این استاد بزرگ قرآن هم‌اکنون برای حضور در اجلاسیه سراسری اقامه نماز در مشهد حضور دارد.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/465842" target="_blank">📅 14:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465841">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b367731d2.mp4?token=P4MNPJ_NQCvJXbUF8ehjDOkta7Pge6WnXAb8iGsoWXlbTrmCQV5quln6zRUbKIILeKKF51S7_Gdbx0RKmOHHWrK1c3Q8P902zQIQEdw_IHQjfy5UewgbJVYkeMm7em9g4YH3rCjBg9QU8qu83zRBOu6Kn5BuNKLTsL5-_9qNhPozfkk-BhAWEf0DE6nq3I71YD8XJQgKH2JG5F2SDjt-A9YglXp1wqMbj07U3OLM3F-9wDKLmcuTeGNK1xWTHa-4FUI_mOooQ0PLApAPP8PlCjQNBqTZnIH4_wa-qNfdPXzzNeAnkToLvawFx0vDQUof9AcxxU-he2gBIKZphKga4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b367731d2.mp4?token=P4MNPJ_NQCvJXbUF8ehjDOkta7Pge6WnXAb8iGsoWXlbTrmCQV5quln6zRUbKIILeKKF51S7_Gdbx0RKmOHHWrK1c3Q8P902zQIQEdw_IHQjfy5UewgbJVYkeMm7em9g4YH3rCjBg9QU8qu83zRBOu6Kn5BuNKLTsL5-_9qNhPozfkk-BhAWEf0DE6nq3I71YD8XJQgKH2JG5F2SDjt-A9YglXp1wqMbj07U3OLM3F-9wDKLmcuTeGNK1xWTHa-4FUI_mOooQ0PLApAPP8PlCjQNBqTZnIH4_wa-qNfdPXzzNeAnkToLvawFx0vDQUof9AcxxU-he2gBIKZphKga4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ تکواندو هم طلایی شد
🔹
ساغر مرادی، تکواندوکار وزن ۶۷- کیلوگرم در فینال رقیب ازبک را در دو راند شکست داد و قهرمان شد. @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/465841" target="_blank">📅 14:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465840">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6aa37163d.mp4?token=Xn0yI9EBHevOMGaLrlPfWnVW0yFw7dy_B0w1xVexBu9k9GDU-YvHDkyiQOkwvdYqY0fwQOm6WQHsJ36mh7EV952JSmdAr7pVkxxD8ra2DXlc2c1y6sIffHBMRE9VUnwAWtOxakSLmmm4opQIf5QaCHLFP0L-gasx9qpZKLJIXdH101kZwgh9jUiaf94wHZua-qbNcDjXTEJgcz_wthQw2EJ9YM1egBSqqj-0OUtvyAMD3_unOz8HD3SQDRsciwntX-UBXvsjoedRTPhAVuLn8mQXIsUU_U5OrTSkO0vc_gTgPopSqRMljQlOMmFARnR1ALhdyNEecXpxsMk58165lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6aa37163d.mp4?token=Xn0yI9EBHevOMGaLrlPfWnVW0yFw7dy_B0w1xVexBu9k9GDU-YvHDkyiQOkwvdYqY0fwQOm6WQHsJ36mh7EV952JSmdAr7pVkxxD8ra2DXlc2c1y6sIffHBMRE9VUnwAWtOxakSLmmm4opQIf5QaCHLFP0L-gasx9qpZKLJIXdH101kZwgh9jUiaf94wHZua-qbNcDjXTEJgcz_wthQw2EJ9YM1egBSqqj-0OUtvyAMD3_unOz8HD3SQDRsciwntX-UBXvsjoedRTPhAVuLn8mQXIsUU_U5OrTSkO0vc_gTgPopSqRMljQlOMmFARnR1ALhdyNEecXpxsMk58165lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
زارع در آسیا هم تاجگذاری کرد
🔹
امیرحسین زارع در فینال وزن ۱۳۰ کلوگرم کشتی آزاد حریف ژاپنی را شکست داد و قهرمان شد. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465840" target="_blank">📅 14:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465839">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌
🎥
زارع در آسیا هم تاجگذاری کرد
🔹
امیرحسین زارع در فینال وزن ۱۳۰ کلوگرم کشتی آزاد حریف ژاپنی را شکست داد و قهرمان شد. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/465839" target="_blank">📅 14:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465838">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8165271cc7.mp4?token=LkCLs-GBlg0rLRmGwxtp_UJvzC13wmOMN7YeCChadwQMxPr__iGC3Sx6U32nN8pmJReaqukCg6NxwK3NAPbDpu_cjhkEYstNfW09rbf7eg944RfoHJPGlQG5XlXuL4V0EovFmPcCh4mPMtFGIiqf9IFjDrwxoKMguvAVftG_rstzZK-4YjyAxjZDNMIsCPVXI4fX3Jp34AfSAUtYYfPSWoTIR_P8VVuTgcyNsXgwXUQx-dRV7QwvJ7RfupYS79Ip3sIfNYqf-vNUlFDxxuyFAS0tHl_r20rSZBb6LUjTJAQzWvaXO_BG2xSnZddu15KYrJN9s0TDMozqw_iA5K0WwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8165271cc7.mp4?token=LkCLs-GBlg0rLRmGwxtp_UJvzC13wmOMN7YeCChadwQMxPr__iGC3Sx6U32nN8pmJReaqukCg6NxwK3NAPbDpu_cjhkEYstNfW09rbf7eg944RfoHJPGlQG5XlXuL4V0EovFmPcCh4mPMtFGIiqf9IFjDrwxoKMguvAVftG_rstzZK-4YjyAxjZDNMIsCPVXI4fX3Jp34AfSAUtYYfPSWoTIR_P8VVuTgcyNsXgwXUQx-dRV7QwvJ7RfupYS79Ip3sIfNYqf-vNUlFDxxuyFAS0tHl_r20rSZBb6LUjTJAQzWvaXO_BG2xSnZddu15KYrJN9s0TDMozqw_iA5K0WwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخودی برای ایران طلا صید کرد
🔹
محمد نخودی در فینال وزن ۸۶ کیلوگرم ۹-۶ مقابل هایاتو ایشیگورو، نایب قهرمان جهان از ژاپن به پیروزی رسید و قهرمان شد. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465838" target="_blank">📅 14:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465837">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsxHRX4bRkubnNQcOwXcs8tag4hDerPZcjkyFHeecFt7lnPSbtP8UnA470qa7wQOX4Lhm9AL0TW_A2SJvqc0Ec3RkmC7U_P0m4p2q8B38rf6Bk23MzRRKPnQcOY4mRh49rO06LYEe0KkBzD4YBbSaxR2iV2FIrRfY0WiIywXkpRGz-8CnX5IVxyhDcVny239M9crds30TMRpecpgZLCiiCoV7YGXloeYuotnhsirHeTNDvnIUiYCsAocKJiKJzIbGMzFzw1AfqwVO_DFCQF6TBCRMdV4y0W5gDAwOTbxfGowaNyN5pciVPQ7UdcSwmR2hokEQnMVPScyRUvBHIyKyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نان ایران یکسال بیمه شد
🔹
بنابر آمار وزارت جهاد کشاورزی، امسال ۱۴.۲ میلیون تن گندم تولید شده است.
🔹
نیاز گندم نانوایی ۹۰ میلیون ایرانی مجموعا ۱۰ میلیون تن است و تولید ۱۴.۲ میلیون تن گندم یعنی تا مدت‌ها هیچ مشکلی در تامین نان وجود نخواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465837" target="_blank">📅 14:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465836">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVmEeiOh0XF66eakjU5QmOOTxYKfjBqTjz4-xzBQI-E4cnskiX6ejtYZpims7sQX82bNJHfZXDtWAK7TMWkMUd0f_eGqm04fPjjLNwXyFw5yrDle1dUFBD0jvW82frS3Rmg5O35njv8byaPG8tHI-uuBo9kELoV0nQ_88fZ69-yHXm89F3uufz8t9mCNUzWGpz1kuSIW51SaSYoxLaNlf-CPmeL375ZOqBjmR0bwLP4hjcoYxE6nZ_GM4sJqW9Wl6gX1ijGAeBT4OUXQILKiiuVXLSQd6OCMvURYfZ6kRjUYtP0IXu0Q4CP5L-76HsBmIJD88Th5LcJfBojgvM0eCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجتماع بزرگ «إنا علی العهد»، امروز تهران
🔹
هم زمان با بزرگداشت دومین سالگرد فرماندهان سرافراز جبهه مقاومت ازجمله شهید سیدحسن نصرالله، شهید سیدهاشم صفی‌الدین و سردار شهید نیلفروشان، اجتماع بزرگ «إنا علی العهد» امروز از ساعت ۲۰ در میدان انقلاب تهران برگزار می شود.
🔹
در این مراسم سید محمدرضا نوشه‌ور و علی‌الرضا عزالدین از کشور لبنان به مداحی خواهند پرداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/465836" target="_blank">📅 13:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465835">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucFS_F8Pe6qFmDYv14R5XeBBSOKJY9GMY_IJZy2PyEZGXr-KCF2S8oHq9K4bwCxCf1IhDVIzbwiC_TYN383HCQj3GqE4qcI-4QseOX6SWxVRXbKlDarQXHE57fLlJWPYYeyjz8VKfTLgPLEY0AuiQgncX3ChMbsy7X_tR26H4p3OcWOrxd_KelZYK9lLF5ZF9bwcB-TlB_S7WdAiTtaBvIExD-_PG5I9hY8TA4tFYkQ4fMWdPPee3f-2iwCSNWtnAiu-rXRXi5jRVo4ZRr44m5Ba5lWomkP8cAWXtSxZtaBbzDuxOJCSoy06uOXfdEAvItu2jz458UiC2C-gEa8ssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زور ابراهیم‌زاده برای برنز  به قهرمان المپیک نرسید
🔹
عباس ابراهیم‌زاده در رده‌بندی کشتی برابر کیوکا قهرمان المپیک و نایب‌قهرمان جهان از ژاپن ۳ بر ۲ شکست خورد و به مدال برنز نرسید. @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465835" target="_blank">📅 13:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465834">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJgOG5TD6yDZXHBkfeFyag_habLNaUZ53lCwRCUg5C491C8P80msOBly3T7WyDpfHlzqvKeQg86aeJkRxiNDVdYa8TKUBHd_o9kJfuA4y4XUuwJNqzVO16LngkPt0o3qML9R2wwE_oe3TkSzq3zKmP9AyNLA1qxH_xVckA98qGJufpLBPLA2e98XH3939U7GWbMkbv4etpr5Sktip4OoJ_f4bRh2RlhiI7322SxIpZfefr1V_dcus0HTpeC6WGaaz1dIFupaM-5gVO2zxmjFpc7REBCpJI5wbxHeVJ6z6rFYr0GRGPJiH52mwoyvlyr-zkXTxr4AXqANMvPYrIMqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوشنر؛ مذاکره‌کننده صلح غزه، سرمایه‌گذار جنگ اسرائیل
🔹
گزارش تحقیقی شبکه خبری سی‌.ان.ان فاش کرد داماد دونالد ترامپ در زمانی که برای مذاکرات صلح غزه فعالیت می‌کرد در شرکت‌های مرتبط با ماشین نظامی رژیم صهیونیستی سرمایه‌گذاری کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465834" target="_blank">📅 13:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465833">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">امام جمعه موقت هرمز: تجاوز از خاک کشورهای منطقه، اروپا را هم ناامن می‌کند
🔹
حجت‌الاسلام شهدوستی: رژیم صهیونیستی با این عملیات طوفان‌الاقصی آسیب‌پذیر شد و ملت فلسطین با ایستادگی، قطعاً پیروز نهایی خواهند بود.
🔹
نیروهای مسلح ایران با اراده‌ای راسخ در برابر زورگویان ایستاده‌اند و پیروزی از آن رزمندگان اسلام خواهد بود.
🔹
اگر خاک و آسمان کشورهای عربی در تجاوز به ایران به کار گرفته شود، نه منطقه روی آرامش می‌بیند و نه اروپا در امان می‌ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465833" target="_blank">📅 13:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465832">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff724153a.mp4?token=KsfwA1sNui3QdmhDLwfytjkk90tAPw-An9k13Z6zlD28-SQXdp5Bh8LmEo8zWaqEOw0P_XBybqqwo1AV_BbxpO0rCbubewM18iA8C-C1riy6Z65BZ23A0DU0UryPJ3N879jTgr4fucywug65z4YYiACCG9ZN5YVOj7FDQRDKY9bO2e3jE7P2dusQhfva5QjavntDHtc1S-tTrcNet4tlwCLLV1x4oZj7MLu9Ipr9osP3BdPLWoZr2_8WY6ht0046RJtLROOv0g4amaJCnqfeXTYhNlbpQcUcv4wwa_R6_OSObA3yywla4U-3DewJa3BYPuhF1A09_jMS0wg71GMspA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff724153a.mp4?token=KsfwA1sNui3QdmhDLwfytjkk90tAPw-An9k13Z6zlD28-SQXdp5Bh8LmEo8zWaqEOw0P_XBybqqwo1AV_BbxpO0rCbubewM18iA8C-C1riy6Z65BZ23A0DU0UryPJ3N879jTgr4fucywug65z4YYiACCG9ZN5YVOj7FDQRDKY9bO2e3jE7P2dusQhfva5QjavntDHtc1S-tTrcNet4tlwCLLV1x4oZj7MLu9Ipr9osP3BdPLWoZr2_8WY6ht0046RJtLROOv0g4amaJCnqfeXTYhNlbpQcUcv4wwa_R6_OSObA3yywla4U-3DewJa3BYPuhF1A09_jMS0wg71GMspA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختر تکواندوکار ایران در آستانه کسب مدال
🔹
ساغر مرادی، تکواندوکار وزن ۶۷- کیلوگرم مقابل حریفی از هنگ‌کنگ به پیروزی رسید راهی نیمه‌نهایی بازی‌های آسیایی رسید. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/465832" target="_blank">📅 13:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465831">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktZ78AQD5cHnubbS6zSJiuqLz5LHTvgYJpEjcYy7Kx85zUG0WxA5uTQAtUTZbKkMtuV--Nz42UNUBssDq3snAjVsybeeoKeJGhwtZJptQYsUVTYlNxydqq3M72SQ_0CuTlhZWJRt_rkr1VDo5E-JoY5VwKTsAh-BzP8Zby4qfjgmzfCOWwacbdl9vDrO-nbALO4h_hy212JyLmqU8dRi9GeZ4luKcPpYS0pQwF3BdPE5ihXY1wJr4ToTWfDI6KMRzqi5iFkbKfS3Ze70_GDyEIpvb1MhpbLqhNpUvDYXPkhN1ZXsgNe23-OL6oRJaYNjSyFjlLGGaqz8XfAEadEMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
والیبال ایران مثل آب‌خوردن به فینال رفت
🇮🇷
۲۵ | ۲۵ | ۲۵
🇵🇰
۱۳ | ۱۵ | ۱۱
🗓
شاگردان پیاتزا فردا ظهر در فینال به مصاف برنده دیدار ژاپن و چین خواهند رفت. @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465831" target="_blank">📅 13:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465828">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTAeIZamuer9rfhaDB3umqTxmP6XA7fNGXQdBWQJe20hRV0x5ir3qvZ4bYTWFwNTwil-sf6zvzPpvdXlSxQ51GFcnRSUrwWiocRCVbDHp851EZS0hkATAobv5fljG4dalLYw1PxFd1UcnqYCcCy9NSF0ueBlTnwUSi_AyitZ2ynFYZRuzUnv6N_1PUrC4EDwXTulZR8mQO8NngB9WPK6mOmfR6SvQltzMTOhWrAWKg4OP_gURT2LScZBGIAYg0K8G6k_EAC21NtHk_MOKk94ABngb4z-Kp1KmnRhUzhVDDFPokxpBBJ7F2stPhlsOxXnpWIaraVMIKkQMKYFRYEKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ فینال ‌و یک رده‌بندی در روز اول کشتی آزاد
🔹
ایران در‌روز اول مسابقات کشتی آزاد ناگویا ۳ نماینده داشت که از میان آن‌ها زارع در ۱۳۰ کیلوگرم  و نخودی در ۸۶ کیلوگرم به فینال رفتند.
🔹
همچنین عباس ابراهیم‌زاده در وزن ۶۵ کیلوگرم هم به دیدار رده‌بندی راه پیدا کرد.…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465828" target="_blank">📅 13:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465826">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-text">✅
مسکن کارگری؛اولویت وزارت تعاون کار و رفاه اجتماعی
🔶
ساخت مسکن کارگری از اولویت‌های وزیر تعاون کار و رفاه اجتماعی بوده و این موضوع مهم به مرحله عملیاتی رسیده است.
🔶
گفتنی است در جریان سفر احمد میدری به آبادان تفاهم نامه ساخت مسکن کارگری با شرکت‌های تابعه
#تاپیکو
شامل نفت ایرانول، نفت پاسارگاد و پتروشیمی آبادان به امضا رسید.
🔶
همچنین یکی از محورهای اصلی سفر روح‌الله شهیدی‌پور مدیرعامل
#تاپیکو
در سفر به بجنورد موضوع مسکن کارگری بود که در دیدار با استاندار خراسان شمالی مورد بحث و بررسی جدی قرار گرفت.
@tappico1381</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465826" target="_blank">📅 12:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465825">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKDCczBbK4MZ7cupgZn-xM62kCvewlwY2iUvu_vWI4I-QfIl8sb_alAGYyk69JiehO1oSCzOtcL9z0epfjA_Fk704od5z1lWVYNZfLtt-Y4RCWvkQPnwIsiZhGZpZhJhYGZDhqJmg7IMoGPD4fhPlILO_s6X0RdAjwbPPmn_8Y9vgvdAc14o5H2UNbxvHYNeLaukdF4Yrv9t8mqDkt4pNiR6aStF6NZP32z_eon8nyPwseVUmzMxa2Axx4rlS8bjkuPH5vKa-_R3sbXD6um9ESwjLO6fITQyC67iAUhodJUYFmDbbvxCfdE9q-p1BukFzvcgt32rwKC738tgbjV4_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465825" target="_blank">📅 12:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465824">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/465824" target="_blank">📅 12:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465823">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrbZ5IHRTFjQdPH3aNFcGOYPcl5alVMYv-Wt2uVbVuORRCbkyAryIJOa7FkUX8F_BN7i0ApviCaXA7RKhCqUbn4VMR4fnxaq0dBjLDwm-7re2woc-NAclzBEDKWhq6pGp4m7UcNPEOwnqj8_5kWTwL98FHq-vm_ZxSiaOIH2-1tEoIpMlihshk3AJ3ggbrRXtTW0VQpO0Et85LOVmx9iHd6FZzAvOJBtLiMvYdIQ7l_3hsSDkpPzPBnU9sq2RHpuTMPgAiQvLXd2HRDyPiRdABusweeY8Y9Ob8Akc3cx62Zn_L9xsN40RqlMNroCuj5ghz-4fycrnzSLlsQP5bZqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یک کشته در سقوط هواپیمای سبک اسرائیلی در شمال فلسطین اشغالی
🔹
کانال عبری «حدشوت بدون سانسور» در خبری اولیه اعلام کرد یک فروند هواپیمای سبک اسرائیلی در نزدیکی وادی قرع، در منطقه وادی عاره در شمال فلسطین اشغالی سقوط کرده است و نیروهای امداد و نجات در حال عزیمت به محل حادثه هستند.
🔹
منابع عبری از کشته شدن یکی از مجروحان این حادثه خبر دادند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465823" target="_blank">📅 12:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465822">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvZTQHEtRqq6h73YtxLOYRu1T94erQUibiXu0b6_gRtcVdzFrSJXYos11_7X4qMJABfQzGGIuq8XPD7ER0B0LkBfi_Y2NlmndYIGXgVCiaqDnnJRyHMdFPbmR3jRvXCAMq3WLl5sJ7rps6CtO1wRTbBJ2wC8jQKffDIwhPxqHcNSjx1mANFoXn5lwdfsfVqZsuY_RsSnlbfZrixM-emaM2QPWf7-eHqmwptbP5yL8Ckuy2lTQIMiSYz6b8PL1yc8s9rcNnF53IFg2ghWJeHt8GUF7DGm4JM5IphuNzZ1nYCRnOnJKsknDsgMSRLgHf9PWKp6EekX1y5WAcee3EEWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
والیبال ایران مثل آب‌خوردن به فینال رفت
🇮🇷
۲۵ | ۲۵ | ۲۵
🇵🇰
۱۳ | ۱۵ | ۱۱
🗓
شاگردان پیاتزا فردا ظهر در فینال به مصاف برنده دیدار ژاپن و چین خواهند رفت.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465822" target="_blank">📅 12:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465821">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
عملیات حافظان امنیت علیه تروریست‌ها در راسک
🔹
یک منبع آگاه در گفت‌وگو با خبرنگار فارس در زاهدان: از صبح امروز اقدام عملیاتی حافظان امنیت علیه اعضای گروهک‌های تروریستی در راسک اغاز شده است.
🔹
گزارش اولیه از هلاکت تعدادی از تروریست‌ها حکایت دارد و این عملیات همچنان ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465821" target="_blank">📅 12:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465820">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oimaKR5wBcbkpW-ckmSztAqJ44Mc0zOd6FLDRCd5X-LWDMfoJpL9HJv8j9p6ZrfwS8YHQo4NUDSMV2LYdkf53hqYTuOqzowYZAtDTdqBCLu8LdxWQtgFdtR4GTUWflt1vL-OgrztFR-tKt88nlwMyTt5e18oTHYIZ-9_XZcYkQrilQCauwFkg3bJE_J7Qc8zR3sBFQuMWXihNH4bFJB7_ek5jRYcHGYsdY2lBp3wFdBjgaXN_27g7c6UWrPt49OLOIxDwTYgyWFm9eqz3f6_7UmiiLAcXOtFFRSCFb1-f4tsuVF2nuz8iDn06WxUd3f8-Giy3y4d635LfVdT3OuRFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت فرمانده ارشد مزدوران سعودی در تعز
🔹
شورای ریاستی دولت دست نشانده عربستان در عدن اعلام کرد سرلشکر محمد الخولانی، رئیس ستاد نیروهای واکنش سریع در درگیری با ارتش یمن  در تعز به هلاکت رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465820" target="_blank">📅 12:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465819">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a43992abfa.mp4?token=KyXwTPpNEieIgXUt3_IFBe0qq4fZ6QNQwRL9y_pzl5d_ok_7hdzApNjA3oIrPF8KWUrUX27bjPNNoy2BxKNIlxqIufzYY0Ks_X2TVgjyFRfDTIcncQWv2Ss_PucXxfze4dtt9PXxHuPVndx5a7pVC5Ha-eqSy0mY4if9hqOYPHT7KvRFQ8PlWuxpCP9UiX2QN4h6VuKQ7RkrcgGKeEg6y3kp_uUH8e6lV0vi0QoXVNuMudv8afCdbfLs_fe6sb5BTpo-rxx3LGJ7lRoMCVSj0TRismeMJ0Md_VZ2AZROKXFwkVfAPozNuh79qJkUGUn5oFVlbdZizkIqTGWu9BySzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a43992abfa.mp4?token=KyXwTPpNEieIgXUt3_IFBe0qq4fZ6QNQwRL9y_pzl5d_ok_7hdzApNjA3oIrPF8KWUrUX27bjPNNoy2BxKNIlxqIufzYY0Ks_X2TVgjyFRfDTIcncQWv2Ss_PucXxfze4dtt9PXxHuPVndx5a7pVC5Ha-eqSy0mY4if9hqOYPHT7KvRFQ8PlWuxpCP9UiX2QN4h6VuKQ7RkrcgGKeEg6y3kp_uUH8e6lV0vi0QoXVNuMudv8afCdbfLs_fe6sb5BTpo-rxx3LGJ7lRoMCVSj0TRismeMJ0Md_VZ2AZROKXFwkVfAPozNuh79qJkUGUn5oFVlbdZizkIqTGWu9BySzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختر تکواندوکار ایران در آستانه کسب مدال
🔹
ساغر مرادی، تکواندوکار وزن ۶۷- کیلوگرم مقابل حریفی از هنگ‌کنگ به پیروزی رسید راهی نیمه‌نهایی بازی‌های آسیایی رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465819" target="_blank">📅 11:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465818">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcmP6GTOMIsqMo9YkFMc4N3utddzbKJTejApkbnrWZ6gg68lEsJ5tp70WguIAuoQxtQo02vpSwGDBYifNrHco2ustEVQeK0svsosi9BMTqjvovziea_d8lF4sk-SZ4dhbN5Ri4jHxbbKYWrOoFid4vPSS_KRRSsMv0sUoIngLs8lpPqrj9WeoR5DCECmeEH2EZto15ULvQci-lGtJ_KVPYcsIJTBCi8KlM10NZbKKLr1kBhYM9r25lu-X9NLDPOtusp2mGMcCmehC0C9gZo4OcVdefU7eMGygfdFyE34hCbXUzxURu7X9FWvPjADYiplkVLz7pvmi-7fN4OvDfRxKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوج‌گیری مداوم جنگ پهپادی روسیه و اوکراین
🔹
درگیری‌های پهپادی میان ارتش روسیه و ارتش اوکراین شب گذشته هم در سطح فراگیری ادامه داشت.
🔹
وزارت دفاع روسیه گفته پدافند هوایی ما دیشب ۶۴۶ پهپاد اوکراینی را در چندین منطقه سرنگون کرده است.
🔹
وزارت دفاع اوکراین هم در بیانیه‌ای گفته روسیه در ۲۴ ساعت گذشته ۸۸۹۱ حمله انتحاری با پهپاد در جبهه‌های مختلف علیه اوکراین انجام داده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/465818" target="_blank">📅 11:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465817">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">۴۵۰ ضمانت الکترونیک در تهران اجرا شد
🔹
دادستان تهران: طرح «ضمانت الکترونیک» که با هدف کاهش بازداشت‌های کوتاه‌و غیرضروری اجرا شده، امکان انجام فرایند ضمانت در حدود ۲ دقیقه را فراهم کرده و تاکنون در ۴۵۰ مورد اجرا شده است.
🔹
پیش‌تر اجرای فرایند ضمانت چند روز طول می‌کشید و در این فاصله شخص در زندان می‌ماند و این بازداشت غیرضروری آسیب‌هایی را برای فرد و خانواده‌اش به همراه داشت.
🔹
با اجرای این طرح، اطلاعات سریعا استعلام و پاسخ داده می‌شود یا وجه لازم تأمین می‌گردد و از بازداشت‌های واقعاً غیرضروری و کوتاه‌مدت جلوگیری می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465817" target="_blank">📅 10:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465816">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnX_0vTFaqFc-YnQkKTDcL9eSHK_HGD8turWZ_CXE6_CE_GSRincK0blPM4qMblfBlnbaYaBptheyDLXc67axI1y329FW8_4Ua7mu8brhbcQxucU4wCvYlRjQawL0pKOc5iJbDosh1x4r3izWfqfMs9SIRCTbpl7gm9D30AWS344k2BxHUUo0axFbgCQf6bir63qvjdk-um0uF9w-zbM1FU7_-NoDCyNIbim3k6FX5i4MtdfUbJDr6aGniCr7AASEmmCNGWnB28BiONCmzOOz_yAkwWPUljWCEBvGmRevbTe0fhyeLN2L33kvw7-sXM7U1eSY4P-rDMqQ_VBE8XJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نخودی هم به یک‌قدمی طلا رسید
🔹
محمد نخودی در نیمه‌نهایی وزن ۸۶ کیلوگرم کشتی آزاد با نتیجه ۳-۰ مقابل شاوایف از قرقیزستان به پیروزی رسید و راهی فینال شد. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/465816" target="_blank">📅 10:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465815">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANWTAh0GcON_ALUK5YL7wpmjHI_23HlNzNQvjkHuiUUpCLsr3w34jLkmufYNNTX4_9tNnLhTkaDHgzJYIpBnd1cwcAG35Ut1PH21CLo6ux_AVdFwsyZgoSaVCIYtL2IzRXzR1fUX2nxPHA4YdyVEc6JEnZe-P4zD-Ywy2ebZIhxxMx5QIZ_CNvVXsdcS09QOQu-6rotKpn3akhqS9l7mGRHFM6yij5pslOHYaW43Ni8eFJZN7nbsyGqzbihM0x9hDKIhwv3p8Q3IOD_FC49ALVl4s3GFa_100I6F6xqTCJge8VXWB0fECLSzF52Bvz5I8PvEsCNj48OnNgA3KR3GiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: عربستان صلاحیت اداره حرمین شریفین را ندارد
🔹
وزارت امورخارجه یمن: حکومت سعودی که دیدارهای محرمانه با نمایندگان رژیم صهیونیستی برگزار می‌کند، صلاحیت اداره حرمین شریفین را ندارد و امین مقدسات اسلامی نیست.
🔹
رژیم سعودی اماکن اسلامی را به پروژه‌های سرمایه‌گذاری تبدیل کرده که اقدامی توهین‌آمیز نسبت به مقدسات اسلامی است.
@Farsn
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/465815" target="_blank">📅 10:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465814">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR9l0hAu0C6AzsMpBY6upU8XFi4vCsMupm2G6KZlq8QNGGd9w5qPqffR-IpEFnFfrC_Qgbg-48lCCtC5aF-ueUbhDFjdT8MD_5DgsP3Gea9KsEZKCah_x4PNmCaRHB5WUPepuyCMP1fzh-6sVetcELmXra1fHdPgaxJW6NMz_bmiuwmjCJcWkk3ZPzEKJmlNy9QfQsL0f9IAMvYpmNj04CnvX57bzQe2hfpY9ZaKwjvf_MaP60dDEnEPQ8fd2aQvsH49CWoLOFEF4m6VEVhdAyBJnNi6nwxo0BBoJ1WoVT434h247vt-mgGGutB0SDouGtaVVzGnr3DPz-EUETWTIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله کره‌جنوبی به اوکراین: زلنسکی می‌خواهد بین ما و کره‌شمالی جنگ ایجاد کند
🔹
رئیس‌جمهور کره جنوبی اوکراین را به تلاش برای دامن زدن به جنگ در شبه جزیره کره متهم کرد.
🔹
جائه‌میونگ امروز در ایکس خطاب به دولت اوکراین نوشته: اگر اوکراین از ما عذرخواهی نکند ما اقدامات بیشتری اتخاذ خواهیم کرد.
🔹
رئیس‌جمهور کره‌جنوبی همچنین نسبت به اظهارات زلنسکی درباره احتمال وقوع درگیری نظامی قریب‌الوقوع میان کره‌شمالی و کره‌جنوبی «عمیقاً ابراز تأسف» کرد و گفت چنین اظهاراتی می‌تواند به منزله تشویق به جنگ در شبه‌جزیره کره باشد.
🔸
اختلاف میان ۲ کشور پس از آن شدت گرفت که زلنسکی، در مجمع عمومی سازمان ملل اعلام کرد اوکراین ۲ سرباز کره‌شمالی را که هنگام جنگ در کنار نیروهای روسیه به اسارت درآمده بودند، به کره‌جنوبی منتقل کرده است.
🔹
مسئولان کره‌جنوبی از این اقدام خشمگین شدند چون معتقدند موضوع انتقال سربازان کره‌شمالی قرار بود محرمانه بین کیف و سئول باقی بماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/465814" target="_blank">📅 10:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465809">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4wcrS73h__uRmXqXRu1NZUjCuJU6askZqkM8MpfDpRh-Z3_iFRXxTSzZfONqP7aRZ9LMTkLrTgCzaggZ8kiwF_IEcrLU41pyyQTFNQgFC67Tigmq8eMzlAsKJK_tZAQ_DmcuTm5Uo3DK8jMzZwWDqHGAbf3joA3NfRiKWplLj88ANSlcv2K0nrFPbxfdpuBl22CkUOfEzjfaR1l3_7g9q9BTk5QO2hABN3EI3UwM7pZTn65u2a2v6k5ekpeLxz2Sjd37gQaWm-6h-pr6rFIdiwclJpaGso3HrkgETU4AjZTDqy9ZD8hyh0lhJ73r5Ky1GraJK667oKeO_giLc-nWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X71Ro6eadmxu8T4UqY2gJAMykh8AV1j4VHv9_phGvLPr-NOO4Ny97_bCeAB5ytXfeq2Q0E0LrY7cDARfO5uEGBQP-7Ogxq66P7O-4Wx2YAgmH-m4MS1IboFf8-SvfMkB9mbmN6Hgzx1Qt1SMWJ5_0jvv4OaPDs3AWC8JaHqdoF_2mO_d86yu47XLvCQMQX2pFLZNi7cdZAXlw7qcs386iRrSeaJRkPjKEAKvSnykC8Q_r5sJeWEXHHpkhPwoJ5CqbwNiX76141dvMkkO82Xaidfm_xnD8wqoVvGuwji8aI_onhENxrG5GypGHpgMSHkfKBmjqlTsviObwpsPn2C2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/br2nnx3AMIxO2sLEMCxJ1B7_Gp4Z49tdkL8y7gTTyZp7BFPK65wDN31r7vswxocWIeG7fXFFzIHOtCv8Vc5A_dPpClPquoXT-fhhLHwVNx5QfITDaQQHYM0sPDiUU1JIBjhpx7_-3A3rFR_Y78oQmweulD9bbMEOsazQl-Fvdn8VZBirl63oSsR6ZUse4nn0q-swv8CpIleT11eO3p3uLqwLA2q1arEPPwA91d8cuS2wDQ7l_RB3PQf6bgOPErvgboJ-8MYRX3N_bWdSdRVTULtHUn95uQ32DRyzAEqtQyJ7Mmd_XpP6gGDUsgCwBd8RgyRTiwwkuOas68FbvK6Jzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWExiAqwHRRLSdUbAKu8Pe9wBvtvCk6BvJS9bgN0UN26Y2HUs-XiLpV1ZW_QigGnELUtGW2V-MO7qmymJV5AjtC-OjU5CDErA8-lYlpFxR6poSh5pnZ12Gz66hxHMbNOCHl_Hy83kb1ycbQ0L7R5zeZey2CxaGzjpwqyRQB3ng3bVw35dJiP2NCoq0lvEuTpB8AHLbVZ8XZWHB8aO1lLNQJKL_FOu7rxL9dA-zPY5NdoGywxri_7OeCRFXL3F-LAOCcc2UZm9bS6agfcs6bmdwA-CMfKA_-U_j5RK4QTEDFYehW8Poczmmeam7tm38wUPLkXOImTJsfCy7e759jyBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlouhPeAMbHhT8McKnc9hz2nOTMYPO8F8ESC3D4Q9OQV4RR-rnEQs6dHuLoTTPDbjQ5XxqbAoSh-gV0Zr5R5Y6Pe_BNxq59W1AZI4fINkZKZP9isG8UJmSObWSer9dGqN2UKE-9zh508GVWCS-sGzJylToAEoBgKJiBQs_oQdeVqQAAZQ5Hg5uZfNiLSN4vUECzrQDohQgironmCQVHJxMydkACY92k2cJqYnWbZqiVedH5A-WbNW2CG_6oLKRakNirCApdT_wMBIl2keE1sIWT2-CaIXjCTh22i3SZZchiT8RldiBIngtrvAIu-ZsyvH77CINm5I1iqAY9U_3dPsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پل سنگی «هوره» یادگار عصر صفوی بر روی زاینده‌رود
عکس:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/465809" target="_blank">📅 09:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465808">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f25116db0.mp4?token=VHX7IEB4ILIXw2GB2N3uuKYnAAt92vR2vlXmzxIHaNQGrTKNqWCh6Ks52N8stsoDZKqg4vXWybllT62eqfxdSogsrUvYfpig5DtJpNE09fQWZmR0PFlvVrM_jijU-JzPRA56tACIZUSBXHULDeoo8vcMwQSVF3mlkv443Ks3_KjjGK3CMEupEAgnbHKzv49keJ4_oHBIItSoQH_D-mTFxDdL8-QUcrqumesnQZjUEVDTuPlbWbij-kDeOqO0bj6eurMPgmXqFEw2Nd4Rxsc-THenO-XiOwMhdnyd9Sx-g1_bxuOzshanLcDt1s1rhMXrtv5Ff4W5wIXa-jQNvscNww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f25116db0.mp4?token=VHX7IEB4ILIXw2GB2N3uuKYnAAt92vR2vlXmzxIHaNQGrTKNqWCh6Ks52N8stsoDZKqg4vXWybllT62eqfxdSogsrUvYfpig5DtJpNE09fQWZmR0PFlvVrM_jijU-JzPRA56tACIZUSBXHULDeoo8vcMwQSVF3mlkv443Ks3_KjjGK3CMEupEAgnbHKzv49keJ4_oHBIItSoQH_D-mTFxDdL8-QUcrqumesnQZjUEVDTuPlbWbij-kDeOqO0bj6eurMPgmXqFEw2Nd4Rxsc-THenO-XiOwMhdnyd9Sx-g1_bxuOzshanLcDt1s1rhMXrtv5Ff4W5wIXa-jQNvscNww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عربی با انتشار این ویدیو از انفجار در فرودگاه نظامی تنفتناز در حومه شهر ادلب سوریه خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465808" target="_blank">📅 09:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465807">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d97cbf38a.mp4?token=JxkKpfKTW4zs8HCXVePuFz5XUtO07Zyr33HACh2H_0B9qXBiSgbyFq-WA36YKPNs2A6TistiaucHcNoyxrKhazVXx9_88ceV6MvYWaUd73Nkd8JHotpJE8_hBqVg2uqkuVBPHuvFqJ8TKwiLlsnI7zd43VTOLPxcOm5SMrFt_htMwnkEHhUVIU6ud-MnVx3fN3rvZ_w8-zCxKkfxiV5fhtwi0uIqvkznGRnbeRJiwYpJPd5HFxEHNsFvYTPZSTT6I-01hMBexP9bB5GFWZ29m-9j9NGmfHUGDOtxnyTmgje-bV9gYvwyTWGF_247UBgRUEKqAAa6Vv5gew5C-tVzXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d97cbf38a.mp4?token=JxkKpfKTW4zs8HCXVePuFz5XUtO07Zyr33HACh2H_0B9qXBiSgbyFq-WA36YKPNs2A6TistiaucHcNoyxrKhazVXx9_88ceV6MvYWaUd73Nkd8JHotpJE8_hBqVg2uqkuVBPHuvFqJ8TKwiLlsnI7zd43VTOLPxcOm5SMrFt_htMwnkEHhUVIU6ud-MnVx3fN3rvZ_w8-zCxKkfxiV5fhtwi0uIqvkznGRnbeRJiwYpJPd5HFxEHNsFvYTPZSTT6I-01hMBexP9bB5GFWZ29m-9j9NGmfHUGDOtxnyTmgje-bV9gYvwyTWGF_247UBgRUEKqAAa6Vv5gew5C-tVzXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلتنگی پدر برای دختر شهیدش
🔹
پدر شهیده فریده مختاری، معلم شهید مدرسه شجره طیبه میناب هر روز با کوهی از دلتنگی بر مزار دخترش می‌آید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/465807" target="_blank">📅 08:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465806">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d261efb5.mp4?token=QNN0fKe0JYWur1UME6-ymux0bYicHT5M05waMMif9foV2GD1fOd82NhGVgGG93hkbSRp44agNQlNJK6WOHUOVhsnxf_NX3mfaUwcZhzLZabLhcdH1AmF0XxLDp6uirAoQllHhAdUX7EFjpS67-x2CCsmXAu4UhCZjUiapZrIiP50HTuV27AhDfGlh_hYmPj-Lpy2W4fmYINADhwx9yPLyd9CvHQG0JkuS_hKWgv789BTgWHObpVO4lo_Ul5b65PVRY8-9xJlIWt5_jG15JItDmvw5FAHQnrb5uYhSAnuyY9saLxwb4_0hEp7z0hp9Lb_u8ls4n3ZdTdABsAEZiDgIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d261efb5.mp4?token=QNN0fKe0JYWur1UME6-ymux0bYicHT5M05waMMif9foV2GD1fOd82NhGVgGG93hkbSRp44agNQlNJK6WOHUOVhsnxf_NX3mfaUwcZhzLZabLhcdH1AmF0XxLDp6uirAoQllHhAdUX7EFjpS67-x2CCsmXAu4UhCZjUiapZrIiP50HTuV27AhDfGlh_hYmPj-Lpy2W4fmYINADhwx9yPLyd9CvHQG0JkuS_hKWgv789BTgWHObpVO4lo_Ul5b65PVRY8-9xJlIWt5_jG15JItDmvw5FAHQnrb5uYhSAnuyY9saLxwb4_0hEp7z0hp9Lb_u8ls4n3ZdTdABsAEZiDgIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارع در ثانیه‌های آخر به خودش آمد و فینالیست شد
🔹
در نیمه نهایی سنگین‌وزن کشتی آزاد ناگویا، امیرحسین زارع که تا ۱۵ ثانیه به پایان بازی از حریف خود عقب بود با زیرگیری تماشایی در لحظات پایانی ورق مبارزه را برگرداند و فینالیست شد. @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/465806" target="_blank">📅 08:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465805">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7051dc5c.mp4?token=AkyueV5lfe3-AtL-2pSfVOh7YVtjQzPLJSldxqrfc2wEcKM44XiVVYGVW4HK0jG1yGrjhYlPXws_5BXnKzyY8ZHZP8QRAvyDewdUQWb6awccxJerUGWKZvA7ifCEZpFfsU8nYVl8u0_X4OjP74dVeaBKudE4SSN13213tc2Lq7wPkhhRuNH824E9sn9fXFP7IuhwQEQDYGHZBaCLXyKgYXonRDuk-zv0DKpnNNdtvHc-J4PGWz6uYngz261XqfUFAMBiJFVwD5_j9Ry3Oo-A3iD7pBMlKKi5sAHwVwDvUhorbOvvKbvDn42N1--CF-LmEXbmkFCWVcjs2viehS2HLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7051dc5c.mp4?token=AkyueV5lfe3-AtL-2pSfVOh7YVtjQzPLJSldxqrfc2wEcKM44XiVVYGVW4HK0jG1yGrjhYlPXws_5BXnKzyY8ZHZP8QRAvyDewdUQWb6awccxJerUGWKZvA7ifCEZpFfsU8nYVl8u0_X4OjP74dVeaBKudE4SSN13213tc2Lq7wPkhhRuNH824E9sn9fXFP7IuhwQEQDYGHZBaCLXyKgYXonRDuk-zv0DKpnNNdtvHc-J4PGWz6uYngz261XqfUFAMBiJFVwD5_j9Ry3Oo-A3iD7pBMlKKi5sAHwVwDvUhorbOvvKbvDn42N1--CF-LmEXbmkFCWVcjs2viehS2HLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ زارع به نیمه‌نهایی رسید
🔹
امیرحسین زارع در دومین دیدار خود با نتیجهٔ ۱۱ بر صفر ساپاروف از ترکمنستان را مغلوب کرد به نیمه‌نهایی راه یافت.  @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465805" target="_blank">📅 08:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465804">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شکست چوپان مقابل حریف ازبک
🔹
امیرعباس چوپان، در یک‌چهارم وزن ۹۰- کیلوگرم جودو مقابل حریف ازبکستانی ایپون شد و شکست خورد.
🔸
چوپان باید برای رسیدن به مدال برنز در شانس مجدد رقابت‌هایش را ادامه دهد. @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/465804" target="_blank">📅 08:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465803">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ابراهیم‌زاده هم پرقدرت شروع کرد
🔹
عباس ابراهیم‌زاده پس از استراحت در دور نخست، در دور دوم وزن ۶۵ کیلوگرم کشتی آزاد با نتیجهٔ ۱۱ بر ۰ مقابل حریف سریلانکایی به پیروزی رسید و راهی یک‌چهارم شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/465803" target="_blank">📅 08:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465802">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هشدار هواشناسی برای استان‌های شمالی کشور؛ مسافران مراقب باشند
🔸
هواشناسی گلستان: از ظهر امروز، وزش باد نسبتاً شدید تا شدید، رگبار و رعدوبرق و افزایش غلظت گردوخاک در برخی نقاط استان پیش‌بینی می‌شود.
🔹
هواشناسی مازندران: رگبار باران، وزش باد، رعدوبرق و صاعقه…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/465802" target="_blank">📅 07:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465801">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هشدار هواشناسی برای استان‌های شمالی کشور؛ مسافران مراقب باشند
🔸
هواشناسی گلستان: از ظهر امروز، وزش باد نسبتاً شدید تا شدید، رگبار و رعدوبرق و افزایش غلظت گردوخاک در برخی نقاط استان پیش‌بینی می‌شود.
🔹
هواشناسی مازندران: رگبار باران، وزش باد، رعدوبرق و صاعقه از عصر جمعه ۱۰ مهر تا عصر شنبه ۱۱ مهر در نیمهٔ‌غربی استان پیش‌بینی می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465801" target="_blank">📅 07:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465800">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هوای تهران «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۶، و در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/465800" target="_blank">📅 07:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465799">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بازی‌های آسیایی ناگویا  نخودی هم طوفانی شروع کرد
🔹
محمد نخودی در دور نخست وزن ۸۶ کیلوگرم کشتی آزاد با نتیجهٔ ۱۱ بر صفر مقابل ربیع ابوعریاله از فلسطین به پیروزی رسید و راهی مرحلهٔ بعد شد.  @Sportfars</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/465799" target="_blank">📅 07:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465798">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V24DHBRqqarDUyS6ZSlRiwzlRUEm_hn4nejf8mh5IW6hzZC-upExwWaDICxW4s1TDFW-IElgNIoI-JxTU328zYwh42zZ0XdeaLE84Ks97Jq6EDNeArmjJvn83TT8wt2OL_3ZDou55utfDXV40HHjRe35m3_PC5dncPBa7JO2uY1hs50TunUbbQVNVH1FCDy-ZdWKxJKfhVGd3cqlfAECCiuBBEOPssLwReirtDqMGksXHLC8TDj5g5VwTfGPJC1bAorgcFq83dIdrRM7wGIKoRWxEkli91WoAqWRIdryjU4yY7LfiCcgiD-7-ph7cn2GZWA0tu5GLUXTyl6-HxTs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشکار چینی با دندان به جان حریف افتاد
🔹
در اتفاقی عجیب در رقابت‌های جودوی بازی‌های آسیایی ناگویا، جودوکار چینی در مرحلهٔ یک‌چهارم نهایی وزن ۷۰ کیلوگرم، بازوی حریف ژاپنی را بیش از ۲۰ ثانیه گاز گرفت و با تصمیم داوران بازنده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/465798" target="_blank">📅 07:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465797">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdHdie6W1bnkUl-PPlj0JreYvbPzODKxn9L1QfsO3v0ZJ1B9ToTchq1PzlKe9ZkUkvrRBcEW8Sb3YTsk52L3K9gsZCQq_deNtiGZ_oJtKM1iMCTeRTyFiKMw_MIGfuXt_8naxaiLpiApdLnP6jlzjTvKvMu0XJAmxBElGKEzZhzYMeM5XkoqO_D9GiQpfLd965pQk5pl_NpnJISabeD1UnK4UYKndngQvfGuEBcjnqqSJ9oDgNsXhbVveLpO_o51oFfcJj7gjx2tJ5ow9Su8MgpSsodXTDEBC5khInnaJZ6A9pE9qnJftY6smStIhhBFTbTU04K5nhXtOo-ffcWn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست چوپان مقابل حریف ازبک
🔹
امیرعباس چوپان، در یک‌چهارم وزن ۹۰- کیلوگرم جودو مقابل حریف ازبکستانی ایپون شد و شکست خورد.
🔸
چوپان باید برای رسیدن به مدال برنز در شانس مجدد رقابت‌هایش را ادامه دهد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/465797" target="_blank">📅 06:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465796">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">برد مقتدرانهٔ زارع مقابل حریف ژاپنی
🔹
امیرحسین زارع با پیروزی آسان ۱۰ بر صفر برابر حریف ژاپنی راهی مرحلهٔ یک چهارم نهایی شد. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/465796" target="_blank">📅 06:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465795">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ابراهیم‌زاده هم پرقدرت شروع کرد
🔹
عباس ابراهیم‌زاده پس از استراحت در دور نخست، در دور دوم وزن ۶۵ کیلوگرم کشتی آزاد با نتیجهٔ ۱۱ بر ۰ مقابل حریف سریلانکایی به پیروزی رسید و راهی یک‌چهارم شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/465795" target="_blank">📅 06:44 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
