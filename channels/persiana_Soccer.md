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
<img src="https://cdn4.telesco.pe/file/ke3b3Gc471rX_h0QW-7LvCQQIhGdjPTTFbT9vtWB-DVPMhbzrA_OG7pX3TxZoD5X9oSv8QZX08TOIblWwfUkBhCNPxfOcP_QNoL5QIFWFJ1jA65qG9oiXk4bQgj56OsJJ9Ve-UraBGRC--1hu0jT0SjtvXkoMh63rKTXfiQ1-b6NotS6pE84nyHVC9JIF_GeHEtzy8ZgtQacCd0I8cpCQHwNAJDjesPJl76r_ifUpMbhGhTJEjTAQsxvuYkqvCuFA-MhGoyfLEeHmCBGkWOsTJpaQi19Y8ygkBFhCbLFin_yV4Fv2yqWtI-kOWTg4h6ybrqZYIQwC5Icfh2bhzMgEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 168K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 23:56:59</div>
<hr>

<div class="tg-post" id="msg-23083">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8NnlobTVtP38jBfCiSwojBEw-tg1KADprRcAnZB_MpR7uReafHbHjOU4-c_-kICrGdsaX9BxjbBeigLPvwXFAcQe4W9POOMjiqfz9jca7tIPsxNEARntfmzmrcnvA-RT4qAkxVSpd_xauUmGHZY1ykUWFnT1g-ZQ7JFiENr39LAXY6QSMfA7mhi46uzM5FxowoQ_stF_gvHUm4qWd6bjfxl8ulbSAmZIv1NX5D5Pwt37xqlFnzaCe6qZCxAcUB-ZVADx_9hTDddtrP1cHek7tOPatS4_2Mm1MSP0buo-T3m62MQln76exJPZRD8IYuKD7Wih5zFMRl2RNx1JsoDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ لازم به گفتنه که نماینده و مدیربرنامه های آریا یوسفی و محمد مهدی محبی ستاره سابق سپاهان و فعلی اتحاد کلبا امارات یک نفر است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/persiana_Soccer/23083" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23081">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAh6RKnCrrvLOXBQtQCnK3XQGOUrrUB-J87LqMU5nFW75xi01zPojgY2bIp1I0h2aoVwRcLiGtbxq7z22Jj3CRvN94jJGudylfwAY2fx0GSHFddiLSBMskCM26RBp6hCTn1yNnZE_nbEn9kBeYstZuI89VjZG42sX8uFmfEYM10EmG5PZluaKXY6CnF2aWOvFRMz0zZjdmo-uHuqS-0M4eo8RDvROq8Amr-8Lf-_kMbNn9LF-HS7Hn0TWW8e1Rwh71H2eB5QdTEa7syRi5DO_MZNQf4Mg356d2JpPoUlGXNaM2eOPODDD-pZityUhRl8j06BQ0ylBAP2vJGAKeEjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/23081" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23080">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye3atitMNV0WY-XZq5shaSOjS8QA5HoLqWlKs7gOOI91xY-ULMo-Wuiydu0v_3oasepdc-vm1o1Ttj-Gprw9MtfpRFzYlWEmrjh3OfAVL1KR0CeqCwGRyQIrcCeA-XJ8IYD7gVn9GWqeRKd8OVaVJIYCuSIHezrO2yDS3ThGO_vXg7ZFVKOF6auuz-YLK8eRvcYqi4qkjsm9VmXBV-8V6sagoim3JFmI5BxCMmAWwccJYMM7zzIumi27o2L4nkxZH0PNbw2iiLxtLAL7SWNq-7NoWOdqmZvkn2Rqv5whDHPbfUedNN4n0kbeFG9C8u3G6g2xeR3rThFnbI8iow0o7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق‌اخباردریافتی‌رسانه پرشیانا؛ مدیربرنامه های آریا یوسفی امروز عصر جلسه‌ای دو ساعته با پیمان‌حدادی مدیرعامل باشگاه پرسپولیس داشته تا شرایط جذب این بازیکن رو برسی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/23080" target="_blank">📅 22:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23078">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Plqo5dYzzZn7C0XERP1tJjpRAE7fNuxvzIrzLkeqba4ol3peoN5tshFzSu65oL_qATS6q0ki2Ftjp727Geelz7XaqpIsGk6ML4K-Ux4mmikM-gI4T9eZkpUPiY8ebcumEJKTwraT5wP1kh9Tb5qRYjUp1cYYTWYx1AMIR4qxI3y-F8EMcDQBQQ23oImcDsIEF0TDFZttlcHcssZ-1R5SlU4rL7ZnN5oRwvY-NSXKaNgSYJ_oXnKLzr_MnQo-y7oeZhH-wd0VrmGOl-O3ZJf9hQJXAPrIecKJn66s18YlywcyddLFwBgdOPg5QoPse2gYjkpzii1REqGnqvC2_dtMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLjS6iW5XOmFxeKOiR4Qr_MJ3N7LeMaeOwzTDWBhIcJ2SaEgPEWCFDvKgjJ2g2nu2sVnhMTEk3UGFDHlc-9no-y2zfAV9SfIkJXNCl8B57GIO8kT-jkXHNm-tWjcq0Yw0zSDTIlSV_ZOlf0giTgtKSW6IXmPCJOo9TP2rX_H3dUOzlFA7aGW8R0kLIjwupvDZJ7Hibaaz-nFqrruIFUvHeBdBA8PVf-9deBdkb2KejT_iAseyo0kV8CyAAZnazpOxYin8FSWRTSXCQcLVDIE8l3VqfgErbKmZxiJ-7e_IkaBSXkY9OjjTOLcLEtoM135itOWypxSGO-CN3sUl6eF9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
نادیا خمز دختر پاکو خمز اسپانیایی: علی رغم‌علاقه‌ام به تیم‌ملی‌اسپانیا؛ اما بخاطر اینکه کریس رونالدو رو به شدت دوست دارم امیدوارم پرتغال قهرمان جام جهانی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/23078" target="_blank">📅 22:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO843QxLpW9tiA2D_1aYkZQSz-6q--JIEMb9MuEYsEcD88nPOgh_egqKgwltuFc5u3eSpr_64VKHjTcm1L0h5ujTQKa5nRUAnV5A8PZ3DJtvu3UuPTHGhO1yo85y0dhAbklw0ElDDL4QMJo4zO-Z2OfH_oyM4nza-bSB08hV_EnhB2qHQZ_NE3mMtuQPITBMjS2SXTFfrN7FFuvlk94vvTbsFGF0laofJOTJ6yWyMqhRoKWj2D_JJUEB9Ng0aWoVLvVZrHkc3ZAZg3YyO5m4qgJBha916xzyl-4aQocxFK_iiDqtyVndLJZEqc8rO6xErWwyYNGgZpGTklWf92WqQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ آریا یوسفی مدافع راست سپاهان در بین نزدیکان و بستگان خود گفته که بعداز جام جهانی یا لژیونر خواهم شد یا به پیشنهاد باشگاه پرسپولیس پاسخ مثبت میدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/23077" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER3FZL4ywMZE5rFgqrSGpx9UzGaiZhYSf2QEO4wG0u9x5YLaNGSNTdG5ImyJottFklcDg97tP9FIqDpu1nqzUOhNWRcrSVl_AvatwpeV0AqNUvJMOsYOOH8MKt3IroItqIstSk78PPTHeH2z8z9BgYaSfwLYIX8m--cSdxnvyb7WlzUggk9qSgwqv1-Wrg2PWE81q00lq16E-09H7x7ucSzLaewe24CWjKSU5fYAzLXI_96TQ7EVz9iL1WdLkxC-B6HFUKTyNThq2HmzYhXdGW4I9hAO3vY7b_OK_rZGfNcMQbU-6XH46yBdkeJtbZEJFW_wmbcxudXIVf5Pf22l7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/23076" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23075">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUXHXJennlwGp3PUUgx0uPtspOTR0zFxEoAoO1SyzDGDjS-7so32S50sYr_gr_Ct3wtIbEG5_1fHtrjYqn6qefPn9aQnxzasVsqGHqiw9ym2hyPAycB8ur25QfY9IaQgIJtFIGpe6R-t2NFr-gvkRvl6w_ZH4oHYEKuijfvgjl0r6XuMQdNlGZJ007XAbASiHr2EzF07x1AslMoT00UeFRLiBnKoWU_wRcHHCSRcephSHAH10rFrQgYb1nTsXijJO-8BedlqLLoAMI0a5rYjGjRZzavUfJbzeiS0ZW6qMYIp-q_JQwZ_B9t1J7Wbt0zKFJRTof5LMffTGfXdFrkuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتوجه به اینکه هوا داره روز به روز گرم و گرم تر میشه این جند مورد رو سعی کنید رعایت کنید تا همیشه خوش‌بو و تمیز باشید. در کنار اخبار فوتبالی چیزایی که بدونم مفیده رو براتون مبزارم
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/23075" target="_blank">📅 21:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23074">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAdZGmKire8HXQYUqgfjTNTsy4OXXxZKkKL2HjBuoywfYDXiUFBZnpxXzJhCwzBXgWFhNWr5venFSpinDQdNXmJxiLZQMjSrOTSIFYGcwnyVntyWcupoKFziboS72B6KwBWpgYpakn4LT819wTq5jpOvoR8FneF7AevmeLZivIx_CybHZaGkB8XSvanie9-77QG3nMEczBK8CJR6ZlIuaimIds2h_v5PsMRpQLkDt4kDvu3R0OqbHHAd5ppROymfsL-Da_Q5TukKm0tEOKM7_2NXi0l0Hc8AGRqZWrAYyC5WL0YO2ddgNocc3ITxXi7Bqjmtl9F0S9hmTQDuoh2p_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/23074" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23073">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ikw1YtQZ3l2N3Pgo9r4W_3I919zdAusA5RJ7zQYsLTEnH8cvADpN_99Q6SA9Cl2m5P1IRMZlb2ZAnJf0IDT5LDgdRM8ELEd0pTTA7YluswZhxE0aUcOWLFjgVIRhJQwXkG_sDRNiYY0tB-FIUeR-pE7e22j1-v-0hV5mVFb6Oe8o7fkFhhBci3OaYFiwxLjbRWDa2LVG0CoPJBnoJBSBZHyGNXiXYRTthXkmRU5ixMKyzmUEMpm--_qTw08HV9TombBx7AjtslgUby12OjsVetKUk8jlnl4E0z4qs7wsBUm5J-Ruund0FXxJoZSWiOJU4s0X4yxpL-NMxZUjZTkfTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/23073" target="_blank">📅 20:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23072">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJXhW5Hj9-nlvwYpTbquMS1InRozyf-0CvB1XlvZ-fZgyWM4ttc0bDcmDkhVfw-CjdEbz2l1PuAUkIrNi-DyH7UbADbNi1x4EaHn5Y79QR-sj3Fssv_SylujUg719Al3kh9_7e--KOYbKi5vDAIiOIsVknPYByPhTQVlcZ6eAlreD7ENHsG_A1fsLRgTSm-DAyrCGRgy6dovJi5zbgVS0XkWzAnG3GKD3GPvU_lCd1XcoGTryr3Qj0iOgwXCrTFbSDaPhHmTMYe3K39CQ3sFn83d7ZgCOkF0mnggkeQLLvdkkNcVNo3m3HA3e5XC5soCsQQ23AGrSEsAGxcd86tprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
7 زوج‌برادر درجام‌جهانی2026؛ دراین‌دوره جام جهانی 7 جفت برادر درتیم‌های‌مختلف حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23072" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23071">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=psf6Pmx-bWHNrPV0sgSZ4-jGbRqV638OXJrHkfzR2RxDJJ2zcKyhY4DBFD0lB7hWDKLH-KHaVop8gu5CE8z0D7ns3gdEPbsvsqUtTbDOt10Bnr06wTJbzOIGa-ilmNVXrLCb-Jvg7AhZmKdb5hoFoT9wobT_j8BPNeT5BcyY__JUqTQXe_aeQeS96zrNjZWEkC7kA72jk2fvl_kW1Yl0T8k7MeaX2Zfo3stBC46MIlJoCaimrgYpYuYUbeNj7GupHhkxvuZEBkQl_yZDcedGBiwldd7ullCzvhmvA30nZOYr746SAXBe7rHrpImmW9K-9l2c6KxJ2CLAfSV89cW0yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=psf6Pmx-bWHNrPV0sgSZ4-jGbRqV638OXJrHkfzR2RxDJJ2zcKyhY4DBFD0lB7hWDKLH-KHaVop8gu5CE8z0D7ns3gdEPbsvsqUtTbDOt10Bnr06wTJbzOIGa-ilmNVXrLCb-Jvg7AhZmKdb5hoFoT9wobT_j8BPNeT5BcyY__JUqTQXe_aeQeS96zrNjZWEkC7kA72jk2fvl_kW1Yl0T8k7MeaX2Zfo3stBC46MIlJoCaimrgYpYuYUbeNj7GupHhkxvuZEBkQl_yZDcedGBiwldd7ullCzvhmvA30nZOYr746SAXBe7rHrpImmW9K-9l2c6KxJ2CLAfSV89cW0yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سوپرگل استثنایی کریس رونالدو به الخلیج بعنوان بهترین‌گل‌این‌فصل لیگ‌عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23071" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23070">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJhnBDPI5iIM6C5gm2rD-56UlQDdJazck37kZ0RqTrfnYlU_zCkG_6SkqwNRexll87dcUsmhz2tx7N7jqLQDgKyO9HMmm3Ew7fw-uKkhVcyYuhSEk0iisP3k1wxtMRZPiZz39JnSKi-NyNeB0ocThvxyQUng08q4j871VXJEDOBnpqsVGd2gkLVALslCAw2mebAmuC9Mprrwu-e62VAw11ig1wl13vNFOCd8PtMkM5KWAqolSMS5SH-2Ek8XDMYLsi6krvTGIFYkSCq9jq47c-bffgSQNkjKutKKTWCqH1BnnZA3-jI-1aOwduVbt8go9QhVAzmDeW574Y4UnemP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: برناردو سیلوا ستاره‌پرتغالی به یک باره‌نظرش رو تغییر داده و حالا هم میخواد برای انتخاب باشگاه بعدیش تا بعداز جام‌جهانی صبر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/23070" target="_blank">📅 19:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23069">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=T08t_pUkHIYdbzCh5yNJYfHfCM3NqB6AwjfdtiIv5Ai_ydzvELSu1H7A396he6yzgTaPMXAD_j4ZzFMTNytsdfG5wXPS1Uf7VQJop5EFbOmwfgfmd9qZKc3d-q8o4qnOITOaI0DUjsYf8JW36fq8QNOYoPxP8ETTJROeh7wfDZq_IS-pbpLC4jYwCdER5ZisbncrNUtPOAqEXG1IO8wKC6ezM0tSKmI4cJD6G30ucPFRX_rRI-Ob-YSUrSsfs4BWHCnhRkl-VnFVS7FSOT-yC0Qp3bqtF7FxCf_8hIF86bk0rIgZeCkYZ8Z15OmPhwBY3qqDY3Led_iSELQGDy5YLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=T08t_pUkHIYdbzCh5yNJYfHfCM3NqB6AwjfdtiIv5Ai_ydzvELSu1H7A396he6yzgTaPMXAD_j4ZzFMTNytsdfG5wXPS1Uf7VQJop5EFbOmwfgfmd9qZKc3d-q8o4qnOITOaI0DUjsYf8JW36fq8QNOYoPxP8ETTJROeh7wfDZq_IS-pbpLC4jYwCdER5ZisbncrNUtPOAqEXG1IO8wKC6ezM0tSKmI4cJD6G30ucPFRX_rRI-Ob-YSUrSsfs4BWHCnhRkl-VnFVS7FSOT-yC0Qp3bqtF7FxCf_8hIF86bk0rIgZeCkYZ8Z15OmPhwBY3qqDY3Led_iSELQGDy5YLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ؛ مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/23069" target="_blank">📅 19:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23068">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5NXqAl42yoLBK80Q-OdoGd1zuheAsu2yE5NE5Fnk5cUiioEx5_5dMH3l1SW-9IYeq-zMd-XWtAsLqQfT3bA0m-KeeReawGLj_My6sX51V63ctDoiw1F1bBpqNOWUBtvNh8Q5y0WmTswNzjmuAK6c3PrH7VjrwYjt7xbV_v6sHtZ4iGodVCauqUjcxBklRgglJu3FGFuZ-1Aqd52Artyl_tj-t67QRymBND8Bm87e0y-5eEq1IkQYvGi2WVy9rpZBqDvnSbl5z3OBG0qUhLpvNRN4vXkTgBIWzYcIbEqLerg5l_-tvXZTbFdjE514rV0vpPri99t519RRInyXIIWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا: فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/23068" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23067">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUpPcmgf9sxhx4C2q1xqYlGfzsohmO4roNTOku2X_UjcHcV98Q2QwaLs8_B0ZfrtK3AB2tKPV0hF514ySnVeuVFmWvnhDTwi1QoO5gAfbOvgZAvX-f2sGdj9pu3GZy3jF8W6o4faI6D7a8EZeIJZrmqaHYF0SsKkGhYZuCLUZlUgCHJIurWIOaXzZN5mFygP4Y-QKjuOcvNcvnzP5lhRikHTkSndB1UfEFlR4vdhatxoripJniLFQQ6-dyZ5t9pc61Q-cqP_Kngi7T_3mzldFMj0xTcIeopnX8eZUgdG6rTdkIPeln17IvTMKmx1pYcdud38FTLgKSz2YMxHqsG_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
با اعلام حجت کریمی عضو هیات رئیسه فدراسیون فوتبال: تا آخرخرداد اگه استیناف نتیجه ۳ صفر به سود گلگهر رو تایید کنه گل گهر مستقیم میره سطح دو. اگه تایید نشد، ۵ تیر پرسپولیس با چادرملو بازی میکنه برندشون با گل گهر، ۱۰ تیر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/23067" target="_blank">📅 19:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsF4ta2b8NiaVBaZC-7TS6WPMJR-E6kII_i4vCxRfpCj2CNJGt_8e15oEDLwgugjhZhqnWgRVw-beNAy90b9lD2-Oj_vCRE07wyV5lG1W-WEgJqu9n7cFZyo15zgJsKMwGIB8xjR8BMMk15BBQyOlLwX62SIWe2TJ00lQYiWFPmxt2coRQuwVrMTC3BL4jrqRixxAdFv5GWT2D6rMr9PIbKbYyQkzLwxLFGNRno2alOJWKjWBVX7bxx3b0uXZ1jO3enIr61cOApZV6qpnB4AsQfNXqgqiHwPsyQlD6oWQTvIQuUkhLz3KHEoIY32iM9_xrIaO9L7jezTQnVgEe84ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیست‌کامل‌بازیکنان حاضر در جام جهانی 2026 باتجربه‌قهرمانی‌شیرین و ارزشمند در این تورنمتت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/23066" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuPSBR8UKVCJIKtyEEEpY1w4aCTdP3HigiQ7ocSCETfcFhcAkRZqirq3lc3-ymZHRbIDR8_wGLtBAiys92v3xqeMIY7vVMLfUeXdeu0nFYKielemlVaxaENI1LNdV7-Gx8uYdygEIRyXcP7nHZ2uqSVEfOF4G3KwLywgzjuETXXaTMqYEe1r189wkMXzPXmje030u5xTmGpFXlc61KqZEVVrHq-I8bSpv7JcGPGsU061PLsn6O1d1OvxnzY8bsbEmHu-Irv0KN51i0AX0za3leA6MVhc5ovtYX1fPcBFJ3Bk2FQH2OVlsDSLfCUs9VypefPNlpx0GY5uW1tejYQJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23065" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzLKiMLJ_AqxtovkpbuiiFgRVNKCT0ST644VGydxJPQdhHgTffwlmlYNPLsFNBGaRvvsUFgqWdvdSwjbjmkBjqh2T7SU9QhAM5DK-e0i_ehnIqhTB7-rfEpVXJT7qBVlPdkOP7229ykCFm1v2Jnl0pO2IL7t3i7b85U-NJyuTjNA3-U64gkrI2yiN9eUeul02bOrP_G0avFBJUnZ8anvKjx0kJsfUgNqmCZP78ulFbdT5ifMCgJgkH-Bx79n-RPDZRpNSqL3Nj-0S8K8ZoW9BCWZp7jxakwN0eWkbCXHV-x4pbSoX4mIt-yOOj08UiVhEl3a98jOuQwDpl71T7OhBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/23064" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23063">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbeo5SUk-3EwfvE7C2Bbd4GQRYCS4IH9oecbldJKVY6tuqiiXPOlLRp6jz75RWaP6JHNPYPIPpHjOOr8SWxNTpZn2gyErMSztHrE2FJIqowuNCtk7sKAf0dZCmgQQEyvccEAErhQH1E1QKveT_FQ4MsVV8xaeElO8CObW97kXVnSZ8UYZ-XX6qWimVFwqI0wW0TDMH6dNHIbIrSjhb3ordt31DbmJ6lG3WX21mw7AkLa7hoq2uK0sq4qZD5VZALAFSKON5Ak6bCORhjXJRk4Y08IDi-rpTm52GW5_Nc2S6xpDWlfkfZ3jlMXgXWPykxK90hu0aNRFYxsmqeeLmQrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eg19
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/23063" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ucx_P6uuYS9GwoLfxMfV8GaKQ5oEwjO6zgbQn696GdCZyDK-nPze5mrRaS-RtWcP-6q8vOsnXYmkskb5aTy98lgM6gwoBCZEHAV6sP9deT2TdX7a45DOl48G6RSjCX9O9TKp0ATmGEVqrggrT8EGOiARRF1PS_1gz7-_lqTpT-QeT5AD-GEIkX8Dzw8z_6ZxUligHlMPYCl-mBtAI3_lPi2muQAdW9idtV9iVdttF4hMbbQuGTzJ6_Y0kEdM7TJNa81Ac7TAklVyLhHXv-Oh7xPGoUloENBqxIQXMus6H7SW1waFUznBR99s_V4DdJkg-U_QnzaQGqo5vsKJmjHHJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/23062" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23061">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49850c982.mp4?token=b-yqmNC7_E8w8oSBhHwjAqYg_nUnjhoMRYBAZPWZ0uSsWfrLLtyyDsSxyA498W1EjZhJOge88vGzTfnKqNF36hZgbKvLgCFPqcqV91vQVQ_At9eWzIl-rYROHMHVejBalFS7LbF2_wNQTAzbzGrqLyrcINY3Cf9oALnhqV1waV1ZJerep3w55wBihPu3dQnuWAj0K45zlM7K_M60mGecAsV1_MQTJtcIZI4HfHxuQMvNBc0Y2FTKKBrQ2NBBiHKZB9Fh5r7LAOT80v0EquPGJFOwaHPCK2rn0XJRMtxt9xdKFiMr3M_bR_snWewMmxIl0-VOoKjWbz6epWSUcKReNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49850c982.mp4?token=b-yqmNC7_E8w8oSBhHwjAqYg_nUnjhoMRYBAZPWZ0uSsWfrLLtyyDsSxyA498W1EjZhJOge88vGzTfnKqNF36hZgbKvLgCFPqcqV91vQVQ_At9eWzIl-rYROHMHVejBalFS7LbF2_wNQTAzbzGrqLyrcINY3Cf9oALnhqV1waV1ZJerep3w55wBihPu3dQnuWAj0K45zlM7K_M60mGecAsV1_MQTJtcIZI4HfHxuQMvNBc0Y2FTKKBrQ2NBBiHKZB9Fh5r7LAOT80v0EquPGJFOwaHPCK2rn0XJRMtxt9xdKFiMr3M_bR_snWewMmxIl0-VOoKjWbz6epWSUcKReNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇧🇪
کم‌ ترین انتظاری که هوادارای رئال مادرید از دروازه‌بان‌‌ تیم‌شون یعنی تیبو کورتوا 34 ساله دارند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/23061" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23059">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERp8XB5qR0oFodPRNObpV7G5V0EFm1w2RNRcUe1J6bvW0vLRKkJ9WtOt3ukjsz0OA8i8FKkfrYVG7Uhuy5Emwfad9_UgexF_0-NkdURoCgR9AtxZE9ETTNxNkKW1Wd8vX4W3TU81DTgsWBZN7EMqugn9cBNigEyghW5mB8VRyj5FbGNaDYEBZLwjm3nnBwD0i0S54d9wKKFPZDBW40EG5tRQXSPFdoCb-Fzp49hqb3XMjOuy_HaYXRiYcorQM4G33L1ssxcyaD8Rww1EjJrZK81fzxz-r9h7jPBroFp_5rID3aWeUprSbXI-lLYwi_vawrnsiFP0spkbDFlfeodZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-rCjhbE14Wf-3MftN0inCCbV8JdsfMnx0RlUjwOnY0yBdlIUcJoc77besrwEqQzmaBoqk0Z51UJ5gLZsYpvTQSmKLZzsDB4tHJDnx5P7ZcZRNKb6Eu2BPGpUz3e223PY1YP1lSoX-dLy_dd7XROEJ7UdLH02ysDAqAL6YnfsQn-steD3Rkq-GrJPTeO6OF1drX_tzLSbRxxFJuB2oD7XXtF7lDmkhPsfldBZAMmQ3syEEYDaSo10a6bWHc2j4kagtOyldpXT3-2wjN0GMwDAZadp3X_ETeuT3zUQJo7MIPg1BgNw7qISQBNA_lebBbMv_jKmCHzxB2Yhy674bSt4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نادیا خمز دختر خانوم پاکو سرمربی‌سابق تراکتور: از وصل شدن اینترنت مردم ایران بسیار خوشحالم. بسیاری از فالورهای من‌ایرانی هستند و در این مدت متوجه‌شدم که به اینترنت‌دسترسی ندارند. پدرم یک سال درایران بود که از مردم‌خوب ایران به نیکی یاد میکنه. برای همشون آرزوی…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23059" target="_blank">📅 17:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23058">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYuriZaOrGO81Us0O3t3A3L8-wAr3V0MNhZ4VFh7kp5UP4KmkoaSpzDkE5fpelga41IiN7ZmoKIZYDaQYaBJCDpenOIZyY4RGTBT3y8ZWefQ1D3KNHwf2pl9CWs0MyQvVHL-b7qwp144xweLuhDSPRsjBqQ_Oprr7a9mYbrTllI7-AK8MIRqRdfbDzXQCdnheKP7W9MhuAwiWi9dG8NodR1nZNFoubU3UJ84n-FjfEO9HlHwJqbhsg7WZqyi2G50y8Ce5PiEhar0K-glNFRuwsttmuoNb43FQn7olxtFwprV14cbTobAH5eUTwlkWIztoey_YA7aYh3Z1D9OLPPDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23058" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23057">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdYrajnCPnIm4W9BaYf_j75yD1Y7x7uVfljqWS80B9xKi1XTmebUPRQgxGK8q2xSB5fhc5HcgK3bL6VbxZE9F06eya0oEWQRj56WkEhuZALsA2NptWj0oZYJBUTTHsFnc0a_clMincfe_i4cl9pOgeDi4IxRMnMPLsKnOfZsIBA5TybDwOlv_upqs_YXBl5Zoeis2jOlgUfAVJ3TZucGQ5KMr6DxdOrltg7fRx1csoPucqCif32ALLlPR2Qvpa35Q16rNqgl3vcJNmNZLt4GkLDmvO4C0vfYw3YVrdVNS1aew7G9qaXJk_I4tLUlQWSqy_DF8Scv05YFGINMXRvkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بمناسبت شروع تورنمت داغ جام 2026؛ سریع ترین گل‌ها ور تاریخ این رقابت‌ها رو مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23057" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDKEXbwrP73nV1zpDd7UsaS1Oi2IuvU88z2fxotFTvLkpDwOKbXfTlqKn0fRfyZpYDLrqiKAMw_KY9MPPTH_jGavv8MzzK6WkqkJLqQGESjLBafdLmuskMtc5PomsB9p3qlMj7tItRRsLleMwHuY8WI69HFGFjHMPUG_YOXSGjY188-OyGVihvczrC-MUGhhXz9FSGruiWCP7BoNyoRsuE3vNNbL1Y93ZSm5pMZrDM8C-4XiObgfBgRHE-7Bi7p02OrMkJjitD280tvHaLhlRSxBKxiZVaVYqmpJ-nG3Y0wfltCHyum4tODknNdvB01AoWbVkYNyiuNephljiLWnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فلورین‌پلتنبرگ‌خبرنگاراسکای: علی رغم تماس های تلفنی با هانسی فلیک؛ خولیان آلوارز ستاره 25 ساله اتلتیکو مادرید از پیوستن به تیم رئال مادرید استقبال کرده و گفته اماده این انتقال هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23056" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVt4e-We8f5fJOsYq3ZVzQzi8staSJpS_BMoXe5ke4W40oOnPwPcLJmcUIexi5I6gHx78VA2xUtwiCm5cCbRpDKM0FhEH9crTOSrB6GOeLd8k47kIuO_kI5nsaGK3uvQ74hV3hszZI0GzQcpZo1wJDzCNb9B-EA5G9jplJTKOi6NhirjOPG4V0FwCRYXLA71a2TcCIR8gv3xmhSQM7_EtaC7Ez5w2OpQlDu-yLNFAD3XaqOTwDa0nBwSzYrr7d2zdEmuxJudRHTE9u8qnRVDhgi_NKgj30R-QHkSeJYF09ji6yUV77wi-i8a9l00gruaSMU_D3gJjJUolKhDZIGeQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
عدالت در میدان، هیجان در جهان؛ جام جهانی با بزرگ ترین تیم داوری تاریخ‌فناوری های پیشرفته VAR و قوانین جدید پا بمیدان میگذارد از شمارش معکوس‌برای‌اتلاف‌وقت‌تا اختیارات‌بیشترکمک داور ویدئویی؛ همه‌چیز برای‌تصمیم‌های‌دقیق‌آماده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23055" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYzKcbgHGpNxCmhlzRWoc5vVQwS7bkwLAVwajYj-K9Y5FhiT9QGncRhsQfqON9hNGgPu_w1znwu4CPV8k3zpXRdbnmMl3W5HvtaCLJIKI4J03o_ivPFLfdaGNy42azuJ_SdQyu3jewpPZjQi9u5i_n16oQUH3o_rp3XdqktAFB9R2xkcMb_1FAj2EIYcLBhDKFpEuOwA5DrBg9Oh010qoFne3DoFaRaVZ27JDFNuP9XAhhKwbSyrzzR3Dm7ergQZqfB936v7TmvRyS9mJKPp6FS4swNopP_zR49fhdJs2rofas-aU_QA_9N_R8hCIvXalY0Q27Jlo_5cPKPHSI5FlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/23053" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=NR0ZuIs-LgNwQ3eKDgjcw67yGZ6FIah8RXvpW6lHZasJ5tGKvJ4nxV15iY2HIyeXLoTTowqvaTE_eRkDWBLh7R_maeJt_NBV5Fbd-srNskknSOdfDW9ncjwhAREO4Jmo4k2ZcLtoYDGYHtLK1cZUKG1n2ul6xTqzre8X5Hub4Aw1PHOt-7v62hthC09gpm29r860tvH4AUJa1JqtSvZppucgQOtz16idyS0lJvaishUfBNVtr5M5ygLBMr1BLFHLU_cQj7lE-xpUr81ykrqKggeJMCB2ifFUT1J_kIRudKRjmnahpBHYpdWitrMcigT5IWbpL81usI8jJSiSESBbmoNJ7Hq0ThXaxr2ZfNpbGzRz2ITEOvwLMXhH7RbvfMnW_IgTs00ktap46t1SUe-URxe-UD1YLz0oLek-6Na_B7kPYi4qZhrCGD1yezgOLjThHd38KaldsKEC0Fc-I7bZ7CGLRYe-alXVkL5iZkffJcQjMqZzmfORaoe-hU-pBUfrfJmbM9Zpl_WX4vpaIOpjBgwYHsK51viywh7menGIhrWUv6v-66F1VmkF_ZkRL8DB_80l3G4hicFOkslvPm7PB_ChGMtwPTCa9Umt03nmFOfbV7p1YRRQN10OgWvmK1eCs0h_mJKVhHpbtD9zysj6kGS6krsD_WxQFxDhl_yLn0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=NR0ZuIs-LgNwQ3eKDgjcw67yGZ6FIah8RXvpW6lHZasJ5tGKvJ4nxV15iY2HIyeXLoTTowqvaTE_eRkDWBLh7R_maeJt_NBV5Fbd-srNskknSOdfDW9ncjwhAREO4Jmo4k2ZcLtoYDGYHtLK1cZUKG1n2ul6xTqzre8X5Hub4Aw1PHOt-7v62hthC09gpm29r860tvH4AUJa1JqtSvZppucgQOtz16idyS0lJvaishUfBNVtr5M5ygLBMr1BLFHLU_cQj7lE-xpUr81ykrqKggeJMCB2ifFUT1J_kIRudKRjmnahpBHYpdWitrMcigT5IWbpL81usI8jJSiSESBbmoNJ7Hq0ThXaxr2ZfNpbGzRz2ITEOvwLMXhH7RbvfMnW_IgTs00ktap46t1SUe-URxe-UD1YLz0oLek-6Na_B7kPYi4qZhrCGD1yezgOLjThHd38KaldsKEC0Fc-I7bZ7CGLRYe-alXVkL5iZkffJcQjMqZzmfORaoe-hU-pBUfrfJmbM9Zpl_WX4vpaIOpjBgwYHsK51viywh7menGIhrWUv6v-66F1VmkF_ZkRL8DB_80l3G4hicFOkslvPm7PB_ChGMtwPTCa9Umt03nmFOfbV7p1YRRQN10OgWvmK1eCs0h_mJKVhHpbtD9zysj6kGS6krsD_WxQFxDhl_yLn0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی‌از آندرریتدترین‌مثلثهای‌تاریخ؛
شاید اگه بیل فکروذهنش گلف‌ نبود و ژوزه اخراج نمیشد، چن جام از جمله قهرمانی در پرمیرلیگ رو بدست میاوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/23052" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO3c1LS87v8ayKCfwlTJxL32XGyPxzLg3rs6wwSbH3g5D8aJxD3dT3h5NhbrfSGfTKmYC-PN00tKOK8a6NwYUZNrqmIUTFHxowVakYctRY0kgAQaXv9wUWULkgsHnTSZ6z6OvwSbDuV5phouCXM7YNwZG3MJzkP1bFfDkpwNbQCuPzmgL_mXQhHgOkoiurck3Mjuj5BL41OnPO3yb7u5c0YMcF2nPVXCEzZ0IFgMptimLjWHnKhwSR8JqhLiHZzJYc36ktWcplmfXtXZJ5eUtzE1yOgsnLFTdC3bf8n8fK79bjALlbofhtnXdz7lZRyZLAmEeW5NAgiGtqlnbNKDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23051" target="_blank">📅 14:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23050">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=gIUeQJPHvEWq5sAzal3cTmseIXkuy-WzJD21StscH7kLtQ2iNDr9I0qydWgqS0qABi-uRKSvCvO6EbYFtB41Fn-3BpSUqfnrz3ZIn5ye01y5xTPMPrPn_tFco5zfFYg9bRWTVcicO7bLToanIylkS8jVbHKvUWUxbLSyIvdFYbnqnc6T1MtJhSpQ1AOO_UqswP8zVp7AU5kAhSBJABPEkstMOG7XT6brxcurcvXqyqrri6EhEKW4b6icOZCnNRAh0TtggbWWo3XCMwBdHQYvG6pgAlPSes8E3g4Y8C8MRRuSYlrxXPyQR1oPn8dBIYAe5TDINnKDiWzaQ3_-McOovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=gIUeQJPHvEWq5sAzal3cTmseIXkuy-WzJD21StscH7kLtQ2iNDr9I0qydWgqS0qABi-uRKSvCvO6EbYFtB41Fn-3BpSUqfnrz3ZIn5ye01y5xTPMPrPn_tFco5zfFYg9bRWTVcicO7bLToanIylkS8jVbHKvUWUxbLSyIvdFYbnqnc6T1MtJhSpQ1AOO_UqswP8zVp7AU5kAhSBJABPEkstMOG7XT6brxcurcvXqyqrri6EhEKW4b6icOZCnNRAh0TtggbWWo3XCMwBdHQYvG6pgAlPSes8E3g4Y8C8MRRuSYlrxXPyQR1oPn8dBIYAe5TDINnKDiWzaQ3_-McOovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
تیم برزیل در جام جهانی ۲۰۲۶ با هدایت کارلو آنچلوتی و باترکیبی‌ازستارگان‌باسابقه و جوان، فقط با هدف پایان دادن به انتظار ۲۴ ساله برای ششمین قهرمانی‌جهان‌واردمسابقات شده. اندریک قبل از آغاز ماجراجویی‌هاش در اروپا، تمام دوران رشد و شهرت اولیه‌شو درکشور برزیل و بویژه در باشگاه پالمیراس سپری کرد. اون با درخشش در فوتبال برزیل به یک پدیده جهانی تبدیل شد. رسانه‌ها هم سر شوخی رو باهاش باز کردن و روز تولدش رو با پله که اونم ۲۱ جولای بود و ۱۷۳ سانت قد داشت مقایسه میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23050" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23049">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Drl8c2Svz-uxXHKL_YiGCI3ppRZguUoJp1jLmD71ey0Os3B_WZso3SquWekFIo6JT7HnktfYjipMFeb8wIPeS_yYq3GaJtPcP1ZOpSWuByrILPGiWDIkwd4OswsPZePusjA5yyvspySFJvGnxYNgiNmQ1PYnRR7zZKBdsxrIBR_28YvAomnh-RgwONs7O41SQuBm2w5FhzmHJpDPZ7J-2D-GmykNVrjY6T3ZQALF_TYwtdDe1GcMg1OzAHone9T_VjXMcnRYBzf8d5Xtm_Xh8WNRPZlwI6SC9PRs0RGFm_kqjQh5JH7UVhELr4-iooVvEAKJ3tAT01MSHKzXbfHx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23049" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23048">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raOT9FYrIOyjAHSKjaWBBePTG-9H_6Wk-tYe2kpwn9Fuk5qsJ856UuwljyehdA3UG5F3Q2206pTeKIq_7UNRiKlrPiwOeDes7V_dbrIo3jjPfBplGON-lK21jjB7mHle57gCutHX4Vfau-ZpysVNMUpousts2eNGuL0YWphyEiq8p8qX_SDxiHxz2iFAjON59kUaBAh_e9eNuM_CgZgFWBenVObcoSn6HaxHpLDfzL90sIkoHcHfyq5dhUngjhrP5OxLkGPaH5_BTYZIbC2_nTmPi9ZXV49XVvIMtTYUGWRs9X1IlaDbNPr9f59EeTiLeY4cpYbh_bgNw9jz94p28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23048" target="_blank">📅 14:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiXlXP2e-QCKQrDwvxcmNkJ0K3M1Rw0QpyN-RoMXWimphkqQhM2OflhhqNojwWtq73X6KLZe62pCnimWr4MVq7EVFTpyRns3SOfFftSm41o4ZG23ypCX-sb15l9jhnav5j7gC-dg-YdlgNJbm7Nf3o6YCSq7o7mUsfIe5-01XETtvHk_xVXApokjaywIodcfUG315p4dlS9h2u74Oidec1UZ7JhYEY3_3EU9xSTFFS7eNK9ipWtooECaO1KmjTWsDl7X-FJUBMPy13yzd-lj4WQGyEGksbnfCNk2ufOO4ikL3oISsOcZZ_NKjXmImzF_pffxod_Y5GsW7duNE5SWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
باشگاه استقلال مبلغ رضایت نامه عارف آقاسی مدافع 28 ساله‌خود را 80 میلیارد تومان اعلام کرده. گفتنیه باشگاه تراکتور به دنبال جذب این بازیکن هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23047" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQs0F6Qx7jA2n9PJKXKcy4iV2cgOpcUG5T_uM8qhjxFtevTA5-41y6ZW4kLPZ25lj3IVXcvE0tSvhXctcsIn8ZxctmtGFRrfOhndJ7r0nTdmAG_hY1qmHb82rpv6BLTBr4S_3To5oo9_xBjHvGzKIfzrjF4PMZ3i5ZxwB8trlgzBIyxZkEX4-8jQHRe6cn2vs2jx62-CuLzETlOIHRI9eER031QEj09uB64W-FIMl3hMSMEC5RVzp2hqk3nBEFAe-ghtlWpGvy5J9AaLc9rjAZ6xYd9AaxUbKitTw0MQ1SdTfxwKosfPALc1HMyNJFuIivGu9wI-Sh_oqviJaHXpUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ‏گویا پیام‌رسان واتساپ در برخی نقاط کشور رفع فیلتر شد. از یوتیوب، توییتر یا تلگرام به عنوان هدف احتمالی بعدی نام برده می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23046" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23045">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=Z2xDhqaDyWewhD6WHGyqUPCV21GkKgzoQK78mZdlsQ1UMCu0T4SvtsRxTwbeTwndWgTs_rE9FDalBd37DW240Fn5dF6z_cPJ0eDDdkr8reXEXFqL32LvWja61zaYTpikb3_zCKQLtPHCcwwSioMnGpe9PdVv-ewbd0BpCI3I3vd1q1ysLX11gsXqMt60_FBsk_a9kg3NgEq-acRTufRGjrAo9ROAFBwIQj5Z1zBnrVNkh48hTlYyfO-MdX2OQzQ-sCQDqqHFH7x8_brkc-aLaDbjZrpHrLLgGmsMbthM9k9z9VT0xzfCZsdnZbYA-wXsjB5-8Vf-g6yl4ojNH5SW6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=Z2xDhqaDyWewhD6WHGyqUPCV21GkKgzoQK78mZdlsQ1UMCu0T4SvtsRxTwbeTwndWgTs_rE9FDalBd37DW240Fn5dF6z_cPJ0eDDdkr8reXEXFqL32LvWja61zaYTpikb3_zCKQLtPHCcwwSioMnGpe9PdVv-ewbd0BpCI3I3vd1q1ysLX11gsXqMt60_FBsk_a9kg3NgEq-acRTufRGjrAo9ROAFBwIQj5Z1zBnrVNkh48hTlYyfO-MdX2OQzQ-sCQDqqHFH7x8_brkc-aLaDbjZrpHrLLgGmsMbthM9k9z9VT0xzfCZsdnZbYA-wXsjB5-8Vf-g6yl4ojNH5SW6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
انتخاب آنتونیو رودیگر و لروی سانه بین کریس رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23045" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Omusz2zw4liPJGlJnqCqo6wIlPBj26GInKGX-R-YI4G9CQzBl8iN7HzUASIK7xlWd5dIFj4ubZHcpHQGUlrWNpGYhyYDoh-R5YhNQsmBCAFlA-rK_QxpLmjxlK1uPYg8iDc_p8uadTkREKOhJKbV_eWxJ6Tw0eocEGrQkJ91BQGhlDF3wcxQRPBoqab6TDjgCptGuaxG-nDP8DCaSon8gDJFqT3l_5pp60s6KUQwaYHhlicQ6m0HsGj-xVc1SnneM8wOgHeoYuNJLb6Ao-XkKemGNsJekgp82S6YhlsAy5yrCrZYp3SaoHABXt8N_Loh3W-UJ6ufeYAToOz-3rrT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: خوزه مورینیو از فلورنتینو پرز خواسته هرچه سریع تر از بین یوشکو گواردیول و ریکاردو کالافیوری یکی رو قطعی جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23044" target="_blank">📅 13:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23043">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZaV7WStzTu-j0B_ubLMcjgpPdWrPcjsRciuyZdAYL6kRr2bScSYxC0yRF7SVGxmpQA566VXj0sUx2yzWPk0g3fewR80Wx4yqKo7lOeGxkXK3t82_TfiYE-jxgsAw0Zihuvki-STx6qfgnL2A3X-UFsNxHbkJfGCSAB4roleJDVStWLbS1hbib76GxMDPVO7WDqvu-S4cEPr7mhbNrcLAKlpdO1HrHvtj2ZvbDaIlgEZq1VwD5VetJKvVkndlrbCNULQz_arutVh0JHVw1rEj-AlceuNIlzw830qq7qoIEfzuzM3VGIoj6F0ZFDp0wIS6TTsPp1yWYQmhL2fjxHNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23043" target="_blank">📅 12:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIQgBcqy9AqGxGBYld0uPy9Q1alHuywwNlAQDorOFN9tW3SPF0X9wFwPRlYr7FSJntWOjFvZkjBiQbLIV3hr7oCJNSRJfbFSUVP487XI9AyEBtBfelth9nXFISWXtFuQjRbZo0PVETSacv8vokeAVlLXh7ZifKXN-k7yvuoBEikypTaBjCMOVtar4HEnXtjOzkKVeGPn54meWZgWtLRHSyl_8bNzNmMC77W7nCbQvQzeKmCihnj2OHgn8thvUtn2YEkj737HXZE1naaRWodR07iipyPxBugCC4_V9IAuj1xiIBVCmIe61p2MhYF9sXLCt6Hgtg-7ijFLkeJFdyJwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23042" target="_blank">📅 12:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hydf6V-S42bGd2pwH_pCZJvoqHPoQTrPdkHr12-PQQ4RYGG20xiOVcPAevz64ldqomtfz_cyZFULT-LrBehiSn_agQXWfVcW3lIaSac3_w3ccssimCwcrx-XNq_KyPwSwQon-G4KtDFr85MhsEei_ZuSo8EB4vFjDOcqcjnSHuEUtrmXeu_c6RkMER4XEeqyu0X-zfaix2KqgrBKnYrOLjmcbthJdf26uM5CMbtciYFB842cI7HG0umsfwIAPJteTfAEJYVsctl_w1hC2qsi0MzVIjLrwh78N7rjVWPY1ZiMrxtxGbjcifPDcq85HRdxTvLyqdr_BfFw881S7PyH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23041" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23040">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiWqMVfXBMKmOjRFgaJLfLdkqWw6Wm4RWeVZ_ALp-cEli-bSfSUVUshIv94mHqGimVJP8jKIwXleknD967Woe1hyKDZX7EnWdDz3tuYZ_BXiZYOGYtjmxzn-XiN0GYGBewRBB9-KtByaAkE6qB8dz3mXP_1b51QVlw9vHfqbFx8Ucb8h2qwa51uGqviVydxsSguzJU-PyODWVkucq-XEYyUR-RAOs6lWKAKc6HINLtSZyWTODgkarbQBS02oPYVZC2n78L3dXlIUY2yXGbt3BJhLfxyYeBTWqvVuF0q6MOII95R80Mk9OJEwL9KtRLpLlLS0HtIv23Bl8DE7N4Ti3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ ایجنت کسری طاهری به مدیران باشگاه روبین‌کازان‌اعلام‌کرده که این بازیکن برنامه‌ای برای بازگشت به لیگ روسیه نداره و قصد داره ادامه فوتبالش رو در لیگ برتر بگذرونه. باشگاه روسی‌ هم اعلام کرده هرباشگاهی یک‌میلیون دلار پرداخت کنه رضایت نامه طاهری رو…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23040" target="_blank">📅 12:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23039">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4860b42130.mp4?token=o-r2-jD6DhTNxWBj5gvmMFSdHB1LeZtdC4GzEyZobgZ1LK6aTq4ql6PM6lcloS2NRq5LZTZoHi6thkB6nLshZfClZBW1YCbv6dUL9E8CvpxvhjTaGdXybqwfFz0XRvQTD5D_7b3dHvFzGbvlaUbGIr3CoWnWDcKRrhNr0A8ksKkurbs_x0TqgRcqcBWapmmu4PsqPuj44i9dF9EAOSCC23HbmGmYD188J544OoVwNX-DrAObNSvoPsf6hmAgkhgjSbICxAHL5ws9naUrbNpbzuZln2erHV5pxawb5RNFis1_CCHWSwXIgvqBqm_TroyvowBpfFqtD15ggHPzltjJ3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4860b42130.mp4?token=o-r2-jD6DhTNxWBj5gvmMFSdHB1LeZtdC4GzEyZobgZ1LK6aTq4ql6PM6lcloS2NRq5LZTZoHi6thkB6nLshZfClZBW1YCbv6dUL9E8CvpxvhjTaGdXybqwfFz0XRvQTD5D_7b3dHvFzGbvlaUbGIr3CoWnWDcKRrhNr0A8ksKkurbs_x0TqgRcqcBWapmmu4PsqPuj44i9dF9EAOSCC23HbmGmYD188J544OoVwNX-DrAObNSvoPsf6hmAgkhgjSbICxAHL5ws9naUrbNpbzuZln2erHV5pxawb5RNFis1_CCHWSwXIgvqBqm_TroyvowBpfFqtD15ggHPzltjJ3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویژه برنامه جام جهانی با گذر زمان؛
از عادل به یک مجری وسطی بازی بدرد نخور رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23039" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohw2KGNZqXtgaKg64SSBVdNlamkOsaT6zMuw0QplV30p9x4yCZ-_z0f4IP0T_HBD_DrTPA_jYgcnxqz-pcbVmLSWQeBWFcwvMUW1Wj_i1X4mVLcgwLlJfjbm7HNIPAOwkEQs2kXCh-ifDHLDDYQwkgbEUlB6-tqHtoBjyPv8Rs3yKG3H2Sk5IJAMVNni1QqSKLd4wPcU-ZH09vJodApPf6up73hUv-GTYYpk1HRpcf0g4mUM9SVTyb7E2nP4ZSVcTkQPrrjuTl5HrrUIuyvSAiGxtbShn6cU4s3x-43gE5EWBnsA1PXZMRKLyPwe87l04SHo1RMx5xXI0PEu3K31ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تیم‌های ملی رکوردار بیشترین تعداد پیروزی در تاریخ رقابت های جام جهانی؛ برزیل در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23038" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23037">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVDF8aGK2973YkaEJpe-Zpr45L6gNem4bYzcEfiHNFhGkaupUWf0JFC3sKLloD0a3ZeIksSQ2NeCe9s1rLs127rYXfNmMW8dWBxp9HLMD3aSNsaogqEl8V3JtgpyJSb389VFBQVVHBzlg2DaESGn3Befw_GUxuBcwK6AfQsMGXTwW008a672Rld0KYkP_5TO36HGlKyufgdpFU-D1YkBDgSbXIehBB9JuidtKGXCh8rbnFgrnc-JAUc8cdmYkhs8DlyQX8SbN8Yu8Eq10WwHCUZ0HQ7vv2RNb_4M83gIN1C7g53GizBqVjccFpBp0xs8Gf1_8OAEilVWvdHbxjM2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد.
معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس‌اضافه‌به‌ازای اولین واریز
💰
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا er19
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23037" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZWKDmSFHGaXTfjzx0WQYgu2I8hg2uGXVUmwGikvZJMUFJtcm6S7NPlvuthvhsAR_zst3cEfASv2zB180d9wBNBmkYl04M94XOP1thQWze4xpgB9wu96edGqoHqJTFCn2xXEhcr84LT7a4x_CxPBXkxX6aYa8xm8C5XiAs1-_q01u8J-xTtmqpKYR311GUTFZU232TcfIGPZ5dXFCKoHzNz69Iwc6NtxyRYWXhEKU7jXXDiitZtdTDsc4qeAiWNtixQ6cUbejv0nKXEk3baJFxNva26chVi6lxK8wgFKTM2ucY-A46Nvx8Mv6nCBKalaPP5CNCSTbdI-LX3fI7m6Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23036" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkfI1GaXuSPjfiKz7vvmFz8IialZPB7IzNHY_5gy3-vp5EdyM8YhSeP4qRN2fni80ydmwEi9NNzABXx_Fu15Zz7YNce82cIZcVaKk-jeNQg0xntkL4ZwLaWAXYIqUFLnZEu2IyZ6568naViKyrIiaP5MGRF1tM1xuKF0uDlGzjZJSHu7WerryEFtOhmYo1MBpIBWJEl7kQxaYooqgyjei57EAIqZu627fgxdZTlaGlvlCQa-BH5FY11Kg5P_vtTILjVMr9W5MM1Az-pxkmy6DVbDfPfsCU2GXxCNNu201NLWSCXItXmj7AX9VarzMejDGki0YSHAz-ww4h_DV6CKNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23035" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKxQrMp4SshVL0Ft-lvc7G5PcdOIHs2Nch7Rq0s71YBkso6hRanqgkn5vu3ebTG72wqOdSO4gRqq4yYAbxtKUbDgvkq4IP6t7lp6A1Re1VKqLDTkSqkyhtMVCXRnkpewLCcNglqxRu3SZHrn9KcDTXlWz6_bKT43OF9tvtvkg1H0gqlNby9-sYTzozEUs0-TSNL50jhXvq8fv3zdHggOyOwXyqOgRe5MhBerbS23Vk6Y4sIS1aB7DVqbQ2X1ji_aGxLNMANY5VFxuO9sI_Wdy3mPvdQze7EiRfhC9njujMmpS7BXtTP7-2oRb3kCPzAAvhrohF3DSkFz4UczED7emQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|دیمارتزیو:
فرانک کسیه پیشنهاد تمدید قرارداد 12 میلیون‌ یورویی الاهلی رو رد کرده و میخوادبه‌رقابت‌های‌سری‌آ ایتالیا برگرده‌. یوونتوس علاقمند به عقد قراردادی سه ساله با این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23034" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCBBa8hC6OjApFjl-QI4-oyl3znO7_3ykUuu-PneieLSB5lTpay571jyTtycRtTg8C17elQris5h5Uth0_psMoNqrj8rl3NcQDocrbdW_Jj8BhYA-5DCXsRKDs7FFkV-8FI4BWrfBrdOzzXuP-BBJxkVCoZ3phjFJdI8NqO-va5dHa7FTOOg73TcBDsosJoEAVQ-a-lql6Cj2uRsVcxvrmeuEb-6LYfER3uICGAolxlzVTJEMOrvOVCTv0u_lw7xPIOJcnAsz8UlrnlZ8Bns3LEWHl4p2NamCk6otTxGYK64k9q4CVAkIKz_82y6_2wm3mmwNTXSv4uJbeM13h8duw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23033" target="_blank">📅 09:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_cqILlfox_pqfgiQ_fxt8CvQp1JzyGcGRdNJa2qUXFYd_ON8lkWIp0FeL59CwBabQX0f472JejZhJZLn5KdE_IN0uaol-JSJNvn4W8TzuSC61AV3ZvhVbImVClae3S1QLtpu1IkDL0HwuaUHXeQqapzihtIsuWu7Jl6KcF0feJdGEs3NJ_F6B1c_LJpuMNp8AYm-vjdz9kxSghYNBPXqektBuLI1gZSvpNXg4rF9Y8Y_RJHLKoiGWazXI3YcZ1lr6DoZ6YZAD24iaDV9olNtwY0udlA9nCGbnJQ0KuRDkFJE7eF8x8gVejGerz4R-FDP7Wa8TkLSgU8eAIE6j2Y9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23032" target="_blank">📅 01:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSpnTPmiIY2i9-ENKxJolYPaETURuNGcraPBk5oXz-p-LiSlnXuLhUOw7JnAgOWvQcnedbmwmG_OBJ5RMwmIWBpp2p6DchqgaFhbAPzv2epzsOpHgPw07Nspw9fikL4uCGEVCKXQ8CTV8sHlVWfB5pjsrGpMk_0p-ntfNG0l0GFFG72rU_0khqxoMfx7O-RIpo9asBGuHRsIE6CUeL2tzkRNJLgSi06t_rNldboj08GoeWChsTtQoctu453GBYfput6KvMbn73ds5o7VvPZ8_2jv_iYU3kwAprD_NULCXibZFZ7jS607TYg0ir-NAEu8oi0bgEMUPkN0_1FmNEjpYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌دیدارهای ‌‌‌امروز؛
نبرد تدارکاتی ماتادورها مقابل تیم ملی پرو در صبح امروز در فاصله تنها 48 ساعت تا شروع بزرگ ترین تورنمت تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23031" target="_blank">📅 01:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWYDQlVCItNwXRshbAVYnmFp0jfRDT9Plgp6uvwSHQW7O0Kv6teZhO4QirvPXT9fUqnta9PLNJkvtM5QUoTa2HraDCSKdHw4t06PJUjxGwmyhufzSPgpjBcHQshpMkWk4uYn7X_jYXJHJLznsFx1RWxBI5fQuy-qaP5S5Z_RYW4G7UX5aCRm_KAMVSrk3gANOZPmOLgUu0AuzNfK7Hc7LxmOaJzGAHdUC7gragQgZYQ-ijs22_J-hSZh1BrKqvYhefk2ZGBv3VQr7ELFitJmYxtWa6BzzWSVKn6QTvAabkPnH5NrGgg7Er1ZCim_VmkoLru0hO1nk7lUE2Gjo46HjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
ازبردسخت‌هلندی‌ها مقابل ازبکستان تا برتری خروس‌ها در شب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23030" target="_blank">📅 01:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=qIPmszbTrbwD2dOp5HftN61O2LWvDiWALXNf6qkfBRi4Vsiggiqgbtza_GZCCJY26HGhUqk1qaSgPluW_-85KLJr2vW5bA4ZrE7mZBNRg0JT_BUa803JPFj9-HI0laUzorMUBlVGDTUlU22LuxwM43ISO5-VvW9D1PiP1SP8cWunHv5fbyDLGfWD6FYbHFoisxhEbu-EZS1l66ZrPieaux6MA3anuc4R5oawaXoRw8nF9_ieeF4JDsZf4ki8H--ZLU3R4wr1ZBjzeWN8T9TanRC9ttXqo-U9UnJZSFrjmpT_141GQ1mAnurDn-84hbF9wk-_YAKq_OcClvAPpkbVJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=qIPmszbTrbwD2dOp5HftN61O2LWvDiWALXNf6qkfBRi4Vsiggiqgbtza_GZCCJY26HGhUqk1qaSgPluW_-85KLJr2vW5bA4ZrE7mZBNRg0JT_BUa803JPFj9-HI0laUzorMUBlVGDTUlU22LuxwM43ISO5-VvW9D1PiP1SP8cWunHv5fbyDLGfWD6FYbHFoisxhEbu-EZS1l66ZrPieaux6MA3anuc4R5oawaXoRw8nF9_ieeF4JDsZf4ki8H--ZLU3R4wr1ZBjzeWN8T9TanRC9ttXqo-U9UnJZSFrjmpT_141GQ1mAnurDn-84hbF9wk-_YAKq_OcClvAPpkbVJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23029" target="_blank">📅 00:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23028">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXNMLa6U5AexqCDgp8RqYEq4tAi4FUTcTYkI95deHxfe3mfG5G2sOXQE2fytHk_VOk8Ha51stUz5wRUOllH1B8h70H1coqQpgZlc_Jh1_vlAHokI8iWJaFcPnm_cFwzLMWrdRPKErh4bcJTcw088QcyMimxkvkMWJZNKH8Tm9OgRrCrDyQlmhi45mYVCJpjEaNLkh3etiPyWlZqZEFC9WcTlKlMd2MN0PbI-xHoCiGeXtTqHJYWUuOduwJs6cuO5sITSeQrIjYZXLoGPBABeB9S7D9Ioy6smycvIaSN-4PbqL51WPxSs8TJb4IndZu5bphAGAL1KAmEFs_5fHBjCLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا:
فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23028" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=R4bpOh6DYtyCHjCAX_3flb_kiOwHE10LSBBrAZdGPnUqt3wXSDMirz4X0ySR8MptOCTcYDMzxIYiR0SjDTN1w55DFshoFQpTKahc9c_CKBaeMk_u1yPeMv-IL5KGTwpYoqrPileoNgCzIbj_AaiFroW_qcga5wQuihp26w_4LLzO9KmB-hgdop8cVg5c_IRExmx2TDoyGzQVVuTtjnIDNAKu4zaJEeJiNbGS07DzWzKgJUEApaocrmQRpGTASYHiav__Ch-qGdk8m94wwDf9ALDgBNeClQ3KnTzK7O-cRw4IxTt14_3jsF9uwxBiwWM25tQzCQ6-3haCHYxxijDGyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=R4bpOh6DYtyCHjCAX_3flb_kiOwHE10LSBBrAZdGPnUqt3wXSDMirz4X0ySR8MptOCTcYDMzxIYiR0SjDTN1w55DFshoFQpTKahc9c_CKBaeMk_u1yPeMv-IL5KGTwpYoqrPileoNgCzIbj_AaiFroW_qcga5wQuihp26w_4LLzO9KmB-hgdop8cVg5c_IRExmx2TDoyGzQVVuTtjnIDNAKu4zaJEeJiNbGS07DzWzKgJUEApaocrmQRpGTASYHiav__Ch-qGdk8m94wwDf9ALDgBNeClQ3KnTzK7O-cRw4IxTt14_3jsF9uwxBiwWM25tQzCQ6-3haCHYxxijDGyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
باتاییدرامون‌آلوارز؛
مورینیو سرمربی فصل جدید رئال‌ مادرید برای کنترل‌کامل رختکن تیم رئال، پپه رو بعنوان دستیار خودش انتخاب کرده تا بتونه حواشی بازیکن های داخل رختکن رو کنترل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23027" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=cxeOb9GpqMk_7MjqOZkpDUNZTn6o8FU5gDPpIMiJ5GdV776iDfbaZwzJJI5wuvwdTlJqsOGfGXjitva0B_J-B9YSRlCQTkaFlYVMY4CRPpn6pmXGVn99-v7MXz-UsVCJyhHmmIcsoNyDDfU-XDGfxzk4RLnteyHH4LTcolPJRukonC56ZhrgzFscZ8eGctR1FUpH7G1B5je6WqzeUBSl1eJyWALAEvkEvGn2LA9NL6dHxX1DqGCbaH6ZC4hB6hsEEq_X8qhVE7C6wHp8f5f5wLPGwER4bHHpbUPaensQbHH5O-ZdrOekvsnN-VoW-cRR2ZF1SCLhfmWhSyOOEB-puA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=cxeOb9GpqMk_7MjqOZkpDUNZTn6o8FU5gDPpIMiJ5GdV776iDfbaZwzJJI5wuvwdTlJqsOGfGXjitva0B_J-B9YSRlCQTkaFlYVMY4CRPpn6pmXGVn99-v7MXz-UsVCJyhHmmIcsoNyDDfU-XDGfxzk4RLnteyHH4LTcolPJRukonC56ZhrgzFscZ8eGctR1FUpH7G1B5je6WqzeUBSl1eJyWALAEvkEvGn2LA9NL6dHxX1DqGCbaH6ZC4hB6hsEEq_X8qhVE7C6wHp8f5f5wLPGwER4bHHpbUPaensQbHH5O-ZdrOekvsnN-VoW-cRR2ZF1SCLhfmWhSyOOEB-puA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
خوزه فلیکس: فلورنتینو پرز در کنار اینکه 150 میلیون یورو برای جذب مایکل اولیسه کنار گداشته؛ 150 میلیون یورو برای جذب یک فوق ستاره دیگهه کنار گذاشته. پرز میخواد این پنجره دو فوق ستاره به‌ارزش 300 میلیون یورو برای مورینیو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23025" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FmZ5YkgD2eP90XcBBwT_98J0RVa36bzODZZfdieUwaUY2GJ8edtS5ASxsVUeje5cZcAYPEPrr_tUN-9fk_S2jpz042H0mDlQE9BH9sMgQSQ7lBY2YiXMsOUC-LtCwd4ZHZedkuUBE_nCbfNl17P9BYOLA-Gc0x4TkFTKfBDszBf_mE-yOrDo2YCygEateWRSX4KCU9EIJ-V6i79nGOuck6zC6c00gIBc9FdlubtNbcyakcy3hfAhD3fAlC9xYeIMyYKmkF4ZtBrlLFH0Dw0f2uYpACCvelmTQtHFvgjXUWmDM4aV0NZjoQw6dyT6PaWroHaKVkeBgRZTz8KTu9Jr2GU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FmZ5YkgD2eP90XcBBwT_98J0RVa36bzODZZfdieUwaUY2GJ8edtS5ASxsVUeje5cZcAYPEPrr_tUN-9fk_S2jpz042H0mDlQE9BH9sMgQSQ7lBY2YiXMsOUC-LtCwd4ZHZedkuUBE_nCbfNl17P9BYOLA-Gc0x4TkFTKfBDszBf_mE-yOrDo2YCygEateWRSX4KCU9EIJ-V6i79nGOuck6zC6c00gIBc9FdlubtNbcyakcy3hfAhD3fAlC9xYeIMyYKmkF4ZtBrlLFH0Dw0f2uYpACCvelmTQtHFvgjXUWmDM4aV0NZjoQw6dyT6PaWroHaKVkeBgRZTz8KTu9Jr2GU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوخفن‌ببینید اززوج‌های‌مخوف‌حاضر در جام جهانی؛ مراحل‌حذفی‌قراره‌بازی‌های‌جذابی رو ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23024" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHP7lZ06toWUKqJhHp5UDTSLGVGPNG7L0cCtli7BsO-CLkiDMOygmXdr7Tmi_EU18nqtut2I9jGvTKe-Nbzoegw7zCpe8cdYKB49jo-ix_bbEVIWED2All6n1FHNrjrjiatml6IAU88ULUZBiO20IvqfuQYr1AgeBMBX9EVZCd7gzc5ZNbtaOaKTw9fHrPWDLHUbym8FKlQeKd14cIewZNbdUj-7n_iyVkoOE2Hn5lc-erXfaiqT157OlTMud0NYb1Tv5wb9OW-n3zw5rzVgdA2uiMHXmB2DrOa_NSntM0MMOuRKwEk47LW2ligh0sWz43WP6S0rBPutaTj236Yhwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی‌فوتبال‌قراره از 21 خرداد شروع بشه. لیگ‌ملت‌های‌والیبال هم از 22 خرداد شروع خواهد شد؛ برنامه‌دیدارهای‌هفته‌اول لیگ ملت‌های والیبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23023" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL-d_GwzswzdLRNDV4PGjRy9Pi_Yysd6J6ZghKQvz6unC_D_COnShMQRR8OSzQj6v-DAH1VyZg9EKQ9ObUU_KHxmRxxrMjiuqEm5ndHNQHScRYlCHF3THIl_yzsNKt4LQNrDwLAQdO8tBe2aMVRYrZ8aicOA9N3eNneujxARrTJHg7ss2oSFPQZst1Ee6XvRHmsgMh0Xb3ElnY_ZNShi19l3TT41kIMv9BZ1Uvgby0zqeyaMSb0M-oRH_Ogw0rFG9tgE_cu5UKZL8Nuwi4DcviUbdz1yWN-aBohUDy6qPetqg-mzXmMENZhhl7WYeLD85LCAnBSHvYjPU45lw8blLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23022" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJg2SwBztidQqzZHHSQZ3xO4dA1hDgr8G55hsOEu-8gGsHuvNYyakACwmV43x8n6dQF-PbBUS0ajF8jMbrJFuwyEO2E2MHZQQ58CIoazXwdXvLlohVZFDKLqOKqFT618Y8PE8k5taRtDeYXaqbIEdpSd4cGspknia_TEkoi73djKhs0vPCAOpkzyzgEtwyAu_tjdvS1MZVJssJlaOwI5giFPWNuaF-89JeM7ws4O29tDiwKx2P14a35LjY-xNetiwICvqgSJcO-LWD1bd4DTYaos0zTE9_uW2ATwGgYHk452husehNzISqFPHmi2o73BYqRCaxGBZNAQyleYDi3ACg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23021" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=F29Vw1bGTcblKISu7akbYamHbPIdyxxN-cPFm-Dyln5gvEXdF4SdBNXGenROFv5xZEiOLp3HpfEed00o6ufcUvfzLKMKhL8QrjOZfgV4aHPvf9c-r44vBXRl31nBKCuvfcyGXy_t6E4mNuKSxlYaAJS5P4gg5-4tt17l_L8llZ6eqlK6kJowSIIKq0oni1xtcGMQKNdn6MausJcLu9nXH41MY37iE55qADAAfSxYzkXh4-ZQjiK2u4bTebDuD6kluA9uecV2KmSN9lJhFyvbxY8RKY3cbDidLjGbBDZvuREJYlLUc5QJlmXqJ8JZq8lRMs2wGMrONLVe0w1b39y7aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=F29Vw1bGTcblKISu7akbYamHbPIdyxxN-cPFm-Dyln5gvEXdF4SdBNXGenROFv5xZEiOLp3HpfEed00o6ufcUvfzLKMKhL8QrjOZfgV4aHPvf9c-r44vBXRl31nBKCuvfcyGXy_t6E4mNuKSxlYaAJS5P4gg5-4tt17l_L8llZ6eqlK6kJowSIIKq0oni1xtcGMQKNdn6MausJcLu9nXH41MY37iE55qADAAfSxYzkXh4-ZQjiK2u4bTebDuD6kluA9uecV2KmSN9lJhFyvbxY8RKY3cbDidLjGbBDZvuREJYlLUc5QJlmXqJ8JZq8lRMs2wGMrONLVe0w1b39y7aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی‌پرشیانا توسط علی تاجرنیا رئیس هیات مدیره استقلال: وکلای ما خبرهای بسیار خوبی درخصوص‌پنجره‌باشگاه به ما دادند و تا هفته آینده پنجره نقل و انتقالاتی باشگاه باز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23020" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roYd0UfwamyzfyRIGX8vYTRIdpsk5vDCinFd5WeRfOQvz-Fj-OoQbtg46vdE56oJLwSX4FyC8NDhPAIWG84W_u5fDe1QbImsiNbe6Uq6PpAUJCLRtyLEv6qguo8xgZ6IS2DCQkFcn6VTQk7qdwEQWKHLCrJDO4OHyfuWPqQWHnU3b_Z3H1GEjr9W5ZJS5SOh8IfAk96Ob2rihC_QYtLmdZp6vszype-wGEKy6eX6MloQdW7XKSFhQmhsrvBaj8gGRYsQtKp4-2v_cuksO9YQHWupZ2gXLwsrm3RLfPRTny3BeS6KgtTtWwLiXptQs-b3LJAqV4RXmLdWXfLgjXToQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛نشریه‌مارکا: فلورنتینو پرز عزمش رو برای جذب خولیان آلوارز در همین تابستون جزم کرده و میخواد بزودی 150 میلیون یورو به حساب باشگاه‌اتلتیکومادرید پرداخت کنه و این فوق ستاره آرژانتینی رو از چنگ فلیک و آبی اناری‌ها در بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23019" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPPCpAvpCyykWZkHhvf-PSckno9fAyk-0GCxjaienQQx4GOEeSecgh7D2Iq7e-yUDRExJBDZQ5zCj5KelCKxvn_hc5JDdZRGzc4psnDqTssMPC3DxHY9t5cCs2mKIwvwk5UxuWoK3f4mMmd-kE5Awi-QNAKnYZLvPIzZKHfLE0icyn5fHxU3hNQfi-ns_9syw63LuJvZSWOnaFo-fXH5uxL8v-e_Nf_Hg1OyUj2bpCNtUlNW7CMwpS4uYUrdHFZtcUTrwTNEZBteRjmNqwKJy5FMe8l6k2TFfNy-DPc8umLc8_EIdXXX86EcPYIUl8Ef02M8fKeziv97aJBH4B62TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23018" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6nuPR6DJ2OamSCO6TXQrUGMwECM3FBNhOeciqR3LWhJAqltGYFsN_WBEhnjm-7Oj1cl-IUxsmWgFKbzLaeKqBRzXjXvqOIhFoNx_NyfABpikqhETTn4wFAE3UVNWU5teqRaOUirqGTo_e6MenvspP2fNGld_Z6h0xg3qDbqSsc41Rue_L-EdDdPgyfhLqZkqhAdQIuyf8pHmVlqawAL6Goblrj6cSn9hDxaVmG_GBdpD0VpZGdmnU5_qMiKEWDcKN7m92sy9rWp6Mu2RVAtqISogO1lWXt7ElmvoqsFYcKOSC5Ow0-OpNU2lNgkgB__ipBdQQ48RLXt49XtoQX1Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇷
جدول رکورداران کسب بیشترین تعداد جام دربین‌بازیکنان؛ لیونل‌مسی بااختلاف درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23017" target="_blank">📅 21:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQVCJtbUkU2R1z9CNYDhwLj4fczlJqsoL_7UJYp4rq57YjjQP6hpNve-_R_XDIOG0htL_kCdpE4M5p7Z5kMkdPADHTgYFYKiLjUZHVaxArEc2diM4ib8PF73OlnTLpxvGRvaF1hz8NoiP4wiYQWmhr9WIEy8dzl5mFCGJMohvrXc5-gAZA26zi8CZeHLVA0BOzy2JPXpCyfFcTp2A-RGVgVvE6txm4OsmHmxI74n9PtTjrwlyk4SVg-DJBpArVGnSRZo6dQD8a6onqo3xGMAnJxwUmyVtl06ON0Qdy9T9YUDazZE6VkaR-zcFNYui069f6D5dyZkqiFIcQrBZVjfmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23016" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNgokB_6bovLyl6Ssod0yz3-esQ00CqNBHK5p8L0XpiQblawp3FLbT7zNMd5A4OStJrWTJRqF6GulQKS_Oi4eoPNJbsNn7RsyklaBmWaGKF9p4qt4y2wFrccUBYgEisDCnPqv-UP1LIFYSGTwifWdPOHVNUBQf6ulIIMHZNe5c_zSyyOrtt3Cd_vHBaKW_IRjMfjcO2U3Qs4Fb9Vcf6k8cplBtWbiSF3Kqhcsg6sww3DS_-1uW_o8Owcncvlaumpf9lfLNAM8EiKFzgN1MXsiKRfuhvP9_yi2HcQjqEHys2DZYMjHyOh_SGEF3P_PTdLASP_9sNL7Th7qYPUT7AWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23015" target="_blank">📅 20:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23014">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=vm2d4eVKxI6_l4wumSVa8FL8kHns1w6uoZt7ppopc6Pzf84zGuDNAhsAQKtnpnyH3ac5CsmLMvcPvpl_QbOjH-LSOF74-SOje7fcUppoLBdxNO4Ygku93Fu4hlUvU-HHeeKpUlrMGpkFoz21wODRdib0txv72jpXSaTe5YhoK9qr0GOl-tqeRkTPPKhryzviyIw6ApgSr6WKDXU7vqRv6Fc1bJ4O9nGgxjk35bHt84rtPPLHAH-N11Aoh1rUsGyxbzNS3cwQQz8rkS90ueQDF4YU9D5smImKsasgRH1vUv8zbquaLPYxmf3Iv5VUAlYVys9zMTm2IW0nCKB9GFUpZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=vm2d4eVKxI6_l4wumSVa8FL8kHns1w6uoZt7ppopc6Pzf84zGuDNAhsAQKtnpnyH3ac5CsmLMvcPvpl_QbOjH-LSOF74-SOje7fcUppoLBdxNO4Ygku93Fu4hlUvU-HHeeKpUlrMGpkFoz21wODRdib0txv72jpXSaTe5YhoK9qr0GOl-tqeRkTPPKhryzviyIw6ApgSr6WKDXU7vqRv6Fc1bJ4O9nGgxjk35bHt84rtPPLHAH-N11Aoh1rUsGyxbzNS3cwQQz8rkS90ueQDF4YU9D5smImKsasgRH1vUv8zbquaLPYxmf3Iv5VUAlYVys9zMTm2IW0nCKB9GFUpZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ما
مردمی بودیم
عاشق فوتبال، تو فوتبال هیچ دستاوردی نداشتیم ولی باز هم عاشقانه دنبال کننده بودیم و دل‌کنده‌نمیشدیم‌حتی وقتی هربار بعد از یک شکست‌جمله‌کلیشه‌ای "این باخت چیزی از ارزش‌های تیم ما کم نکرد" میشینیدیم. بامردم ایران که در جام‌ جهانی 2018 روسیه بابت خراب کردن اون موقع طلایی مقابل پرتغال اشک ریختن چیکار کردین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23014" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRP9hdAzIDCaxzT3emMrklLdvFwpf09wi4Em5uvpgP24L-UXCt08R-WNMDP840lKdgobBmbE_zmWH3CYiYbj2KqmUNR3nxP_8IndLfvOCL1sGejX30NEI5xHR0KmAhgsxDEUMLp_Ak8WTxEzzoBkXvn2VaUtDVS97M1OafJeiDf7G4I73FFO4OI0GXP22u0vqA1fGb1itMkpUww-ICU65smn2dfSnt3NypWwOvUbiPba7oOBnrBxAImEccdriPt6xLXAp-jFVlfLGK3PGks_CbAJCqn_r00q1DP9B1b52lFI1qTCpjrW5B7fpJLnRqh3MMBAXCk0WN4CRbkFUrAVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23013" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA_UXx_5CeB8XTJUNKBjwQ2SGY9UUaTAjRPSVEHTvB9zjJu0FNfRr44cWeKnoehuLm-4B2ntWxAKFtJOAWtw_kVU3lGurDflkPhRPRRxJX6571Y0gB7FAkBXkTaOEZ62QEAHvWqdAG-4zPVwAH0VVQvIv0L0z6Jb262qZ4Bw7cZFD_XBnmbeW8Fv1ySs8hzsjgMvDy7gDAVsp-N-3JLs6Rmd6MN7MTVhzHYwsqQJ_YLKKQlRCiu48PUGBTSGtBO99Gt7qsLHbWAo-NmFgdvxzqN0QPm2yVcELcxHxUKtaGt5mJ6ogSVxMUJYUMWYcB-aXxll0NwmhZ03TeHMHKEvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23012" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29259cd165.mp4?token=JaNlfPdXm2sijWs1Ooe4VwTa21rCk1mXZJhlNA1vqkKvqfeOUJhDFM0M7oKgQfkBfshJqCj4e0g1CM-QSDPZlJuBZBmM665JMKUQoQJ1geXkfgWFWlriXEavAtPECwxzbRj3gufy26oio60vcPVWE9-IQqzBquOBGM-sCMOpCs-CpZ2AYROzPyu7NUcQXCP00eDecrDPAoJKb6zWsdnLyeDcZ_-I6bBzDgXa4tM_goX9PB2o3RLDJ9M1ySv1rkrcIqI4XT8RSHMb-mArpx6P7OttrWge2aIZ3ttkhoOVgC4X_ozIgUxOnB7Y85VFu1sBtquLwvDQh-fx2BZmQikXbYk2EKQe_Ro2Ks_IK78iJtVK54EX1n3swlXynuwBe8f_mVDssWmqZ6PsfiLqHxODs76Ie0Qs9ck8-RKQ687Yg8oGrl3cOveiyGxXrm9GR-AQN_N7Qnq4tVoG353o9U5Zwwcs94CMoVpt_1Tz-pCM9UjbNzlPEHnV6glttKpAaeCNGOBI86UpvbSR80pzb4mBGusRmk9Gew2rwX-3ac54pA792kLxSA7BFEp8oWHlONMAnidmCCkyMaqkFtKOeilzLMXUqpTTndEGU9lTuWll_jYsNY6HHzSFLdT7GcNmqqjMCqkz5Eya_tDlpz4E8vWWDmg9Su5ppVueI0Vr9Ohee0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29259cd165.mp4?token=JaNlfPdXm2sijWs1Ooe4VwTa21rCk1mXZJhlNA1vqkKvqfeOUJhDFM0M7oKgQfkBfshJqCj4e0g1CM-QSDPZlJuBZBmM665JMKUQoQJ1geXkfgWFWlriXEavAtPECwxzbRj3gufy26oio60vcPVWE9-IQqzBquOBGM-sCMOpCs-CpZ2AYROzPyu7NUcQXCP00eDecrDPAoJKb6zWsdnLyeDcZ_-I6bBzDgXa4tM_goX9PB2o3RLDJ9M1ySv1rkrcIqI4XT8RSHMb-mArpx6P7OttrWge2aIZ3ttkhoOVgC4X_ozIgUxOnB7Y85VFu1sBtquLwvDQh-fx2BZmQikXbYk2EKQe_Ro2Ks_IK78iJtVK54EX1n3swlXynuwBe8f_mVDssWmqZ6PsfiLqHxODs76Ie0Qs9ck8-RKQ687Yg8oGrl3cOveiyGxXrm9GR-AQN_N7Qnq4tVoG353o9U5Zwwcs94CMoVpt_1Tz-pCM9UjbNzlPEHnV6glttKpAaeCNGOBI86UpvbSR80pzb4mBGusRmk9Gew2rwX-3ac54pA792kLxSA7BFEp8oWHlONMAnidmCCkyMaqkFtKOeilzLMXUqpTTndEGU9lTuWll_jYsNY6HHzSFLdT7GcNmqqjMCqkz5Eya_tDlpz4E8vWWDmg9Su5ppVueI0Vr9Ohee0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23011" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVUCIG37sCVG8Gr89uz3-BZUKBi01pRI8OxnOchljOyZsmOtwVmzbReDALh33VGrW3w3qUZdakMOVNWxRF5fymCSjAD1KB4IIXsOHeLUDgHIMcUsfzCM53Cd-hsikAAS1cNO3sX2BtusSXcgtykDrx7sN56ShIbd_ttRX0YZCpHO1U5_Wb7bg3NmueBfUhPRVgpj4VdQ-no3BLdzowY58yJQV76wc2VgmiNxzxeIFpWFR0aEpinrmQEDZDvW93rhGwHmWG4PpW0m309VX9LDeLSRHFUyGTfep597FD1Ggp0wxb46yFa7qKrkoBM4qMZglq-Cw0EqAtLTyrYSG6iPGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23010" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB9Me9XMEXruRNRyyBfQr4_bVZcdcOqy4ZWrO0tETzNQreH52GdU2uc_nlqtNLYjavMk5kYA4_GB9ncTVLafxcFYGEUhmJSH534scv7F4AQipobU1EORI6Qw1TswndHMX5XXQFnm_BOXoMfkZrHK1LkZWa9ayZkYjrX1tIR8OtND8qhAR0Jp7URqgvD8LWEqx1Xbjcs9V737aMozWpgA5MYW7s4NVhpxdASPOsoaCKxO7-UoL5xqkUyTNecr_V9RoLb7LeS_lIRyWvv0Yck-gnnR34e_-8VgmO_T8ORpFamuQclLLCIcqRrIMeVhByPJi5q2vo2sqnH1jZCSR2OHJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیست ورودی و خروجی مدنظر اوسمار ویرا برای فصل اینده رقابت‌ها به دستمون رسیده و بزودی کامل پوشش‌خواهیم‌داد. علت اینکه یه چند روز صبر کردیم این بود که همه دوستان عزیز کانال به اینترنت دسترسی پیداکنند. ویو کانال قبل‌جنگ 65 70 کا بود الان با وجود اینکه نت وصله…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23009" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=aJ-7cHsOeQrIwpFPDD9Qhz6d1qp0oT0UuDdJhfyMC4QWcyjR3E6DYnAqD38laH_oCHCQYx4MV9c7LZTofZutJgD-41Gu2YAMblf9h-vs3Tm64OXYEITSM9P0fCcU3egD-Gyp95QzngIhqTA1LWst-0TzVowd71icf7eU6girFmkvZfQaYjFlP70ubMJyWPxRxfh10Q9rOjd35Au0uyQhKz7Ibq17OrgQe-Q90_jtVhPLY5Nt3olsyHygF2b5ybploZzFZJOLHZRidEFGvC30tHYLtP0bGk7OEw_Ucv36alKktfsa2Hqoqgk8__Tyz_yEbdCzWsXE_JmmuJNgDau2ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=aJ-7cHsOeQrIwpFPDD9Qhz6d1qp0oT0UuDdJhfyMC4QWcyjR3E6DYnAqD38laH_oCHCQYx4MV9c7LZTofZutJgD-41Gu2YAMblf9h-vs3Tm64OXYEITSM9P0fCcU3egD-Gyp95QzngIhqTA1LWst-0TzVowd71icf7eU6girFmkvZfQaYjFlP70ubMJyWPxRxfh10Q9rOjd35Au0uyQhKz7Ibq17OrgQe-Q90_jtVhPLY5Nt3olsyHygF2b5ybploZzFZJOLHZRidEFGvC30tHYLtP0bGk7OEw_Ucv36alKktfsa2Hqoqgk8__Tyz_yEbdCzWsXE_JmmuJNgDau2ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23008" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBX0rWToZL_FgjjCHpt0S24bjV7IBvZdFrNlGMdWT2lL-1eIq0oWsOaCXLoT8vajR5ytPdY94RBQjmSc3xtEnxs4TWSraNW4rIFaNET4JbHs-946nTUz7d6ns64401WObjJHFPEI8XdJMbAzz1x-oCSKQetjzuP1yOaeUF20KrSDAStjSIIPpHMurhabma5N3PqW1i8E-36Xw9Issw_rBaF-najVt93nm4HrWvqnt0xqXfCELGDcA2v_cPYeZlFvg3WMZPOe00Lh2INPCsOuYU_fBPUeWq2QxXRZu7KbY8QNL_kV0SMfHa0N76Ii-xbYVEQxODrDYe8RuK-Tt0_rpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دبل اولیویه ژیرو ستاره39ساله لیل در بازی شب گذشته این‌تیم‌درلوشامپیونه؛ ژیرو در این دیدار نمره 9.0 دریافت کرد و بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23006" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZBM9EykpATkeuRMfYB8iaR7QXMLWq5KwoUgw39is7amvVdbCuoEPklkMG6wfAQhkCn_-G-xt9z-xg5p0p1bDNy_i9VtjS7Z_AJkx6AfA9-9z4YBrOaY3i9QE149S5V4YCYK7X4ttR1IKq5kZlulI2J5Vymh94tnRG0l0ut6wpo0F9zbdbyE-TL8wqXgu4HmH1sTZA6ET0z5VAn11cnOz4hqMbjSoENZHRIGzezugEe29f68dRJOY1-_h-PZaB5H8Db58UZw2ptxfj8GtRRhCOBsoRETpciyrmHe-rqeXUBy_VEOqmvQ-9eJdidfXYea5P4aSFQ-Kf8ShZE4ZJ2iVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی فیفا: دیدار دو تیم ایران
🆚
مصر قطعا دیدارافتخارهمجنسگرایان‌خواهدبود و به هیچ عنوان این رویدادلغونخواهدشد.  دراین دیدار ارزش های همجنسگرایی را به جهان نشان خواهیم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23005" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=WVrheC7wQ9OVVgx2eb9DGsMOVVKZOZf2QqCt4TVV026XpPSWV58OP8ZzRU7idfYozfm5WhsxFjt2bnHE98Gzo5ZNOCLLQoESJVAKmDxpZIOo1mS_Wr3uHYOiuKyzltXIS3G3rsYTDrjdhsZIaCrUCL96pw24Hsl0RPdRfQ-hD0HZBsRs0CNX41ratWsPp9cP8LzzyTKGWR2cUnAIHT0VPzN1ExvSmQuO-c9Asc58uKkAD_lYrgV_XCOFoqsdaISBTI7xbpeOELFcMrMewZ1n4XzuS88GRqrSHHumlIr2_SdP1HaQb4EDCWD8eSsQ2L5jmQp6MdsIvAuDZHCQ3Rru-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=WVrheC7wQ9OVVgx2eb9DGsMOVVKZOZf2QqCt4TVV026XpPSWV58OP8ZzRU7idfYozfm5WhsxFjt2bnHE98Gzo5ZNOCLLQoESJVAKmDxpZIOo1mS_Wr3uHYOiuKyzltXIS3G3rsYTDrjdhsZIaCrUCL96pw24Hsl0RPdRfQ-hD0HZBsRs0CNX41ratWsPp9cP8LzzyTKGWR2cUnAIHT0VPzN1ExvSmQuO-c9Asc58uKkAD_lYrgV_XCOFoqsdaISBTI7xbpeOELFcMrMewZ1n4XzuS88GRqrSHHumlIr2_SdP1HaQb4EDCWD8eSsQ2L5jmQp6MdsIvAuDZHCQ3Rru-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیووک اوریگی مهاجم31ساله سابق لیورپول ساعتی‌قبل‌خیلی‌زود از دنیای‌فوتبال خداحافظی کرد. اوریگی با اون گل تاریخی‌اش به بارسا راه قهرمانی لیورپولِ مدل یورگن کلوپ در UCL رو هموار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23004" target="_blank">📅 18:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=UKGYnXLPjxdXgeoAWlfboxUuk6kgdlNKAiD0q59FVKR2_Zy6sGjHYiu2XMyAxkLHnnymgl1TzFTRA6iMJDy_YPR82HiU7GKNUsEVg44p-7cJIk3KnfgTkXGiXqYaMxq8N3j6dIYZs9nnpc9LMbc58hhbr1fqkzGEMpx1dYFgzQO2tjREIfdqejB7BF5jeWtAyhsk7OHs5xHLQRo9IZwsTjYMwIAAb7JmyxyP6_W4wgDOw_CD0uAcITE7OiHx281eZqXz1yxZaQTgTwAe3d4fYGqxxPyooOZ1dlAmfacall4RHLAxa0kbpatqI_zZQgAD4VGzfWx8LvTHoS5blGjLAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=UKGYnXLPjxdXgeoAWlfboxUuk6kgdlNKAiD0q59FVKR2_Zy6sGjHYiu2XMyAxkLHnnymgl1TzFTRA6iMJDy_YPR82HiU7GKNUsEVg44p-7cJIk3KnfgTkXGiXqYaMxq8N3j6dIYZs9nnpc9LMbc58hhbr1fqkzGEMpx1dYFgzQO2tjREIfdqejB7BF5jeWtAyhsk7OHs5xHLQRo9IZwsTjYMwIAAb7JmyxyP6_W4wgDOw_CD0uAcITE7OiHx281eZqXz1yxZaQTgTwAe3d4fYGqxxPyooOZ1dlAmfacall4RHLAxa0kbpatqI_zZQgAD4VGzfWx8LvTHoS5blGjLAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
رحمان عموزاد شب گذشته در حالی که مسابقه اش‌رو 8 بر 0 از حریف‌بلعارستانی‌خود عقب بود در نهایت با یک کامبک تاریخی 17 بر 10 پیروز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23003" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW_YOZHgX68YikjYUNDW2EOvNvbOJn7BMmdebMm3N1A7wrlljFiW4SRrwlpc1ImheE-Woi_VRbPeP0lyalY3LbVWfnboHPJm_4FGkiGaRl3DGJzLpTOfmhB6HaSJqHS6XxKzc9z37V0S2NrWTrDpRjyQhMXhe9LFaxLTxJ9wPj59hPsCXw_QEFIGwt0loqcy-WVMUlwPmE9LK8LgIdqv8gH76BukxUkrWKzgeFTk7F8m3QeFd-TLauv_JU3z2z7Z0I05a2_huLQlwSFfGwT4v_zdk1EepZu2B0X7VAavNqGKLfEB5iLk-V7-eYxktwojLlz5kXxcLs2RdkZOYeoeyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
پُردرامدترین بازیکنان حاضر در جام جهانی 2026؛
کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23002" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUeXUAXQwVB5yrkBqcduX2OvYG2JMjvlNXtFBxBsx8dwNlMSkkaZYM3g5WFOK9BQTu6HgTcVKMqssDEUXUG-y33RT3ETdkkyn9nTo18UeYSyzowLP9gPrxKmKXjSXZkkbEWzmUby-YQJ8PZxbDiLVxDxHPyclLWJxLLbl03DihpiiDMIBUxNq1yR_zd75DEBpyDdNWT_yhpejlQu6AuWqwUhcY4JdPb8UifVhy6BmQdx8HzR7jphRPSr70r6cwqHto0Jeo-pnlVW12NlMClPRfbK7T6HuBt7yFtR95hs4-laUe331OMQ9xUC4f5E6EMtFT11fOKP7cSzMFklWF27zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌پرسپولیس‌بزودی‌باانتشار بیانیه‌ای جدایی مجتبی فخریان و یاسین سلمانی رو اعلام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23001" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIxFWEqCBrUHlL0ajoIFpb8iYpValV8OYTYRVedE_wgxnpgxNbfsAei8lT4amsHVdxyGxkcV5r5hlGrYqTcIYlhdM3AZX4m9Wi0lw6hMD7ahXHJDjYtWWOUoiupg6ziS3-o08RVarm2qfjKhTbYFr8oIbU6MWaQ-wkLwuuausNSRW85WzTIQTsBaZLgQZCAr8utN9GL9uBTCGoUumItJvDmoUnazfB2md2BPdr5gWKjSQXvGwS9dLEdglLNz3dvMqQb4zU_hP6xXnr52VibSIFhPXzVUDiFMGndXQGObocjmYyxt7rlo6eEPpeDkexzuHWrM8ZH0LoGFh7uxdvE0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در این تیم، همیشه جایی برای پیرمردها هست؛
ایران و پاناما پیرترین تیم‌های جام جهانی ۲۰۲۶
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23000" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzx_hLuV_FIOdaJPIPwhFwbWKxiHZMaDq9741NXpWFr6zBv8j8piv-7bQHnmIlJWPcx2bcQSiIaxWVDUyA6jgXNuD6d-YC7WaBjCuw5AHx--VBCebeyaxR4dOS-SovPNMcRA0eSXjJqw7UjgvDSHbGjEpSqt5wzOt2DxWKVL82OCAUjKL7_2VZlqCktOT9b4PAdpMuYv7Sqt9N_SmS1WeuBpa82mLJwXv3qMWEvhYP_Byr1wFmS1n7IlkZ0QABH05-xGaZhuoWxRCJYI9hbdwMNknrry_4G8aKODUpyOCuiNKbauUByxjR40ZcvYLSSzeM0tEKP6OqJRIyAuCjXC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22999" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rz2H0oXg-JI4YTYDap_ki2JmgygPR5SO6p9Myoy_5dnglyvwVLCtlOKimGG1aqT-YWFgslw-mub-lgIE5oLTmw4BIhxuMHrIy2dvNee3OSpoUEfuWmJN9jOkMNzAWYTD5fsw_8BOOd94uBjkn8twYCCK00xJb4STtzeMzyMSvPxVCYchqWdb-1zVhcvqFBgtmaWHLVj_rYFrZc7nkzs22F05vrpJPHOasHIC1hPKYZUJU8F-By-8zWRADrv-XpcwZRlSfBI1kfAT6nwwj3vWcbwSEqWRufBG5yDUPDLD8T1h7OfIpC90cvgWSzQ6xzguamJqUfDADfa_xhXaTz2hGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/22998" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORGuRkBxna-HHvj-BFekC6PWJHfIJShOt3LcQJDw6oX-4RmWieGoTUS6J14rYZL-gGfsHbbCkLlG-5yn3y2B3v_LTA8ScUh40Gi4J2fvWFSZh6B8Xw9_9EjgXDvvf9QCOkFop4iR3-WaOnF52CedCYv6MqI4ZbU-3QUexrABUq9SexIisTpEKn5irIKGmrHMpn4yWw3O4MQT2-Zakegin28YbMfV55sHUo9pJPOU0zkNix-ue_aU5qAIMJ_83ffHCbmzBBj-1fJOZbH1nhcjx8B9GlXmshAo_g6JHbRa4Vgen1Ru20jTGJppjbnILGOO8rnt89_4q-oYa6OesRm9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22997" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=JCcWxEvrJq0X1GtJ3xVEpqkfN2in0P1Lfr1mGIi9MvapYJDXXkBXmfGj1uugNstFgc6264PzAkDKKHSbziZud7ZVHUVH4zky7hdioc3lshEcBWazQegrnYRWrB5X3okIDds6hl4rkzmDh1THo_2EddHrWDJDY6c5Q0JLnZclfjgjAtdYouCaI6i4HNyG9CT0ATR1IEfNj3y4GSyuLdnqdmHe2wb1BaBfIITuKxaXXXzu-XTrmXP7YSFUSIFv6Gz45szMwCzGsvkwpcMBvyVXBTRLlisgJLx-9v2tYZSq36TKWNy3IE1uLncURH3KP2tCJ0kyAmH928yGr3vOJrzLhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=JCcWxEvrJq0X1GtJ3xVEpqkfN2in0P1Lfr1mGIi9MvapYJDXXkBXmfGj1uugNstFgc6264PzAkDKKHSbziZud7ZVHUVH4zky7hdioc3lshEcBWazQegrnYRWrB5X3okIDds6hl4rkzmDh1THo_2EddHrWDJDY6c5Q0JLnZclfjgjAtdYouCaI6i4HNyG9CT0ATR1IEfNj3y4GSyuLdnqdmHe2wb1BaBfIITuKxaXXXzu-XTrmXP7YSFUSIFv6Gz45szMwCzGsvkwpcMBvyVXBTRLlisgJLx-9v2tYZSq36TKWNy3IE1uLncURH3KP2tCJ0kyAmH928yGr3vOJrzLhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال ستاره تیم‌ملی اسپانیا و بارسلونا درباره دلیل بستن باند روی دستش در حین بازی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22996" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOyZphlEB1k5gNXjDmH-0BJaw-OUQK6GNNZhzRAbdMgBwsioI3QdCp0kADIK8SOlJh8xaOB1yZPdpdttr-swAYodKjmL4eZvsWKew9NfQPOSuZpGmYMdv3Ww8uw_xcx5FIYnKgrR9jEhz0GphtJHr8YeGHXi_A_zpNdhC-Yggk6CoKCqYv5gFbPaArBz9-q4mE4AFcLQdt2MFTw6sFPmoULozOjCyk8v_B4gr3Ta2EE0AO9OP4uveSMdz9AlU9dtAveQ86eOfEIvB5M8XE-vBYlA_O4h59oMD_cjfr0IkkJQScaSeJQ10p-X5MSjqbgvMcjiOQTj3oo0dM1sVXUyUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نقل و انتقالات تابستانی امسال برخلاف تصورات بخاطر بحران‌ مالی‌ باشگاه‌ها؛ بمب های بسیاری زیادی ترکونده خواهدشد. هم پرسپولیس هم استقلال و هم تراکتور و سپاهان خرید های خفنی خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/22995" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=HsBADCCcFZoRrjiYNHQfddg2Qu_r8q6DFtLjyQnguUy8sLSciuEIKsD-_XV5Wy00aOC7JcVAVipdeZzPOggbLQVeW20GPMeM_Cr9kLIJ0wZRSQ2oRDm4Sdqtoq5fAMxCKXxP_YfWPEJuCShU2Wwb5Q8ELd8XXeVyxlxMVaivHWsPj-KS3HJGLaz5RbpNsAZ-DmxQc_LktfGgfHtdcn2dQ9szH-kz0x-XUMRjz-uQRsSfTREuwWAO7K-LbKSEsh9diNNTlzk4q0-IZGA4E7y1akGCuQ7eAuFCKZq5VYezJdcAUSufjsAs2R6rJauC1IdkEvs-Gi0TxqaJE8jMxubAPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=HsBADCCcFZoRrjiYNHQfddg2Qu_r8q6DFtLjyQnguUy8sLSciuEIKsD-_XV5Wy00aOC7JcVAVipdeZzPOggbLQVeW20GPMeM_Cr9kLIJ0wZRSQ2oRDm4Sdqtoq5fAMxCKXxP_YfWPEJuCShU2Wwb5Q8ELd8XXeVyxlxMVaivHWsPj-KS3HJGLaz5RbpNsAZ-DmxQc_LktfGgfHtdcn2dQ9szH-kz0x-XUMRjz-uQRsSfTREuwWAO7K-LbKSEsh9diNNTlzk4q0-IZGA4E7y1akGCuQ7eAuFCKZq5VYezJdcAUSufjsAs2R6rJauC1IdkEvs-Gi0TxqaJE8jMxubAPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازیکنای تیم ملی فرانسه بعد دیدن اون عکس و ژست سمی رایان چرکی اداشو درمیارن
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/22994" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sml-eQNeK8152TegzBxP89v7qUTTd_e0RD4fHL1WR_xWf5qaCVpWcYELa-946WxIzhyht1NpkTyrZM_BBhLwsjREbL02BGQgC1cQkmucE2Bwi9bM7XHaxluEuTFstpHiljdPFDwCU5WVunx-t4bPv-WRNfoRwdYQIdPILt4tL78Jk3rVlt86-l9qjea897t82M4Qlpyha9eU8XgT5g9H0JvAsfO53jG-uH5Ko7ZQFomTiAgpNle8daU0yQRAwIKekQsypphoDU-GxGQbmkquGVcpPCMABtdTIppi7j1Kjpl1WzPc-7YESqUAC9LTv7ILfXHfgCTTSX3gKBi5Qog8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/22993" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ58X0hkC3h61gBxmeAqs_VY1lLUuBLOE5WY7WS23b7W0US2iTPyxwYLMcLHt5hnmTM2O0XlCQja41upMxPCzrqiMl9z4Fsn1WCkkg9zudB6fghJDLFEvTZQVDdcZ0MUefdko9TlLxIJfDM9-ePKMkBW69_zmKvHTbKPVI9TJcB7XSRoHFdk0R6dNt4pijqIFYsFJ4yppPo2tYzpe4xuq4vsdJXIQ9pkBN94pYXHJ-2dFcc0D7fO23ek3GVYz7h0JSHNi_nj1yN65iCAubzixF2BEg2jBknoO0FHpGnbELcKitTr7CoTcUOnkYLefXQDaxgsIq7lpMj4yJ3h3ffHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/22992" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=om2xf2HUEx9g8nYcc55o4i15bCpLZNMOIlhIOAHlf8KNAznbBeS73GhUDJUMjF-s0S3Gyzxb0nLf5g-7ku0fEK_c5jlbOdCgWi6O55DwgxT7RczFCHqdnOcHlEHmOiBPuW8IuyVj0QP37KiJoOpk0c2ZPfUQN6Anf7kOiE4PyuUTIGfw9KxOiHDfhUUEEhBm6y4ks-1typt405skl-ZYNBvuRV3kcMlus09JG3n-PpU7j2wIL-oViY7oj8Jzz_InIAI0Lwrqan8TuQBASYbZpTRBf5quUo7IKU4lZJG3N1HfqIQ4XtIeEijNuoG84x7bkaQ7RBSCj0Gqz0xU-DJg1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=om2xf2HUEx9g8nYcc55o4i15bCpLZNMOIlhIOAHlf8KNAznbBeS73GhUDJUMjF-s0S3Gyzxb0nLf5g-7ku0fEK_c5jlbOdCgWi6O55DwgxT7RczFCHqdnOcHlEHmOiBPuW8IuyVj0QP37KiJoOpk0c2ZPfUQN6Anf7kOiE4PyuUTIGfw9KxOiHDfhUUEEhBm6y4ks-1typt405skl-ZYNBvuRV3kcMlus09JG3n-PpU7j2wIL-oViY7oj8Jzz_InIAI0Lwrqan8TuQBASYbZpTRBf5quUo7IKU4lZJG3N1HfqIQ4XtIeEijNuoG84x7bkaQ7RBSCj0Gqz0xU-DJg1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرد البرز که بهترین خط دفاعی لیگ یک را دارد و هیچوقت دریک دیدار ۲ گل دریافت نکرده بود. اما فرزاد حسین خانی با چای نبات و شاگردانش در مس کرمان موفق شد در ورزشگاه خانگی فرد البرز به این تیم ۲ گل بزند و ۳ یا ۴ گل هم ۱۰۰ درصدی هم نزدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/22991" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHHqAzvMiC-2GX6DyiziVao_VN68FFIlSyNbZv52V-1U9xJtvbJUvVNdrgTijzX4CzmWOAvf8mJ1-a4WtAX3hARS6EqbXr_AI6pIkpuHJeYeekdhGPBe8kkVcI0kVKOsZsdAjuxdBy945CnQ21zwrHUl7tphJL_Pf7VG1TG_wDhQlCDWMOdr3T1lu3Gnwnq-StNNFLfjuhWFN5ztvONkAms1H3mT5NYj1-LG2osQvYWLpv8gM4z0Jh27tIpUOG5E91v9o9cDmOJe9ACTrUdJY03pvRTfbJg6vDVOPB3WXocjrMjuSDW2jCgXazV_VES4XkxHrDEm8Oe_o6Rs1vCvFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه‌اتفاق‌خاصی‌رخ‌ندهد؛ اوسمار ویرا برزیلی چهارشنبه یااواخر همین‌هفته‌وارد تهران خواهد شد تا برنامه‌های‌آماده‌سازی‌پرسپولیس‌را از نزدیک دنبال‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/22989" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdlTDXNniWPiyHJUdaKnpZw5mrYhBjS950_zi5dxdtsaMoGeiIXJbpAuKeXKtFgXFMG6slvi7Pr8o8hqMMtarr6YogKZu_DpgTggQPmnfuUHeVimI0gKld6iBT137Lr7N7PBNJ2c3-v-eSIee5W8ASTql6AbTOOG_AZf8x1w8UY5_vp0YdidqiH1E6fHHb6_fYtGoIOltPamAHrU_kuXAyzkDqVRUxc6jjQG-NZw7gVgSrSkzse8bHAcFvQTCo2d3pm0feg-Q4lstByzbHccevdMnfUv79FeUW-L454HEZYlU_uI8wwbf6mu6fb9KktcM6xlgJVJlm7gC4Hrv5hdKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/22988" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=dYowcz6B6wEFrFUsDoBnyvLAgtN2TN3JaMvpbMwFEUZEdu7NyC_XPry1pvZXEAoUwYYQF4sM5I5nPQUS1DXIGYPQ-B7-OXMbcomKiDlUyKJg4Mp6tIE1Bej9ulRxDzf8-z7EBBEIma3tpiFITw-GCt8XQWjif3KcPiIT8OsJaNPnkbCwl3fmFxMWS166Kk_j-YanxWOgmPHYcbQpFp-Z4wTIYQHdHKb96yzDUn7FfArX01oP3AE8HnJGu8IeYDaykPVAUS5EACthfxNmuqi6I2h8kpbXQvA7i9tA9nLyanhHd4WCzu7hppiI1XtQCxk_t0ZgfBj4sRAoqjOhYn5OwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=dYowcz6B6wEFrFUsDoBnyvLAgtN2TN3JaMvpbMwFEUZEdu7NyC_XPry1pvZXEAoUwYYQF4sM5I5nPQUS1DXIGYPQ-B7-OXMbcomKiDlUyKJg4Mp6tIE1Bej9ulRxDzf8-z7EBBEIma3tpiFITw-GCt8XQWjif3KcPiIT8OsJaNPnkbCwl3fmFxMWS166Kk_j-YanxWOgmPHYcbQpFp-Z4wTIYQHdHKb96yzDUn7FfArX01oP3AE8HnJGu8IeYDaykPVAUS5EACthfxNmuqi6I2h8kpbXQvA7i9tA9nLyanhHd4WCzu7hppiI1XtQCxk_t0ZgfBj4sRAoqjOhYn5OwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نه‌داداش جبر جغرافیایی توی پیشرفت آدما اصلا تاثیر نداره؛ محمدصلاح اگه تو مازندران بدنیا میومد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22987" target="_blank">📅 10:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=F8-oY2ehYpGyJi14LIdjJlFnBvB80Qc5-Z7SVLZ6cBFHSWoWJnMyLAyX1GXu3cmNQLoQLzKKAzbngFEwog6QgJOlCpNdYAPWCTfHJbWhj6_0sYgGizgvRJt8OouqrQZLtbWZmlqo_r18lVWBQxtyZSXifD5ms1yi-1gVHt9ky7meZjvS4O5RLXPOFOvlvP4ZRqLksEzv59oBq67CIbf9TRNS_tiEdUolAw2WIdfcw698CgQr9tYksj6aXOpV3scat7hpzffBKWOlzBbWZ32PiDGx0NzEdSMtHwlcinFtlc2McRh4hsWhyJHKY1TW1Xb8T-1bF4TxssbIwpwY6vHLiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=F8-oY2ehYpGyJi14LIdjJlFnBvB80Qc5-Z7SVLZ6cBFHSWoWJnMyLAyX1GXu3cmNQLoQLzKKAzbngFEwog6QgJOlCpNdYAPWCTfHJbWhj6_0sYgGizgvRJt8OouqrQZLtbWZmlqo_r18lVWBQxtyZSXifD5ms1yi-1gVHt9ky7meZjvS4O5RLXPOFOvlvP4ZRqLksEzv59oBq67CIbf9TRNS_tiEdUolAw2WIdfcw698CgQr9tYksj6aXOpV3scat7hpzffBKWOlzBbWZ32PiDGx0NzEdSMtHwlcinFtlc2McRh4hsWhyJHKY1TW1Xb8T-1bF4TxssbIwpwY6vHLiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ
؛
مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/22986" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dt2AMCfrzDYm_ubENlsszjZjLSHDOpWauMDaB3NTDyVJNSNJzLcIiaOjWxcNQm1G5JKQ0j524xTJLH0RAqdnYUQS0l4f2nsmwdFpL_pW6JVTOgx50BRWxfOa2z54hVJXqbG14tfs5a8f_-zUVKVvl5y38s7FaMUzt8X5jBz402C3PSeaPm73rvboeIiRQup4nPFeFRZXoUp0UEICf0KPaORJV2qmCwDhWjSeeLO5ap8fPpKuHuKsX0C0TMIomziHpqu4AfB9nP9x-sof_L_1F25srdx2DyXbqZAnXqDC2S8577ILpaaLQ8H3zf4ecDXJQUGL-LSdFG5fyjut0HfdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWMCB7gpc05YpHc71QpVZxk8TcXt7QdJ0XVCnTEBHQv4qKLPX1Az7QrktQakZLPdvgglNCWQ2WMRXnHdl3J4ubpk9HM4HXmnqwHQLzoswLY6km7h91C6rs4CNCKj3Qzl7sEIpEJCyrPwdAkDJyoG3eDf0kKkUFOIAMkR5RvrOJJFpMV26LhY2HUVNu6aPnuPWqnSLFJd0ljWjo5lLH7UkwNrSRugchPOmfgEWODoaLwm2RQBG-Cfc9B8MdDPBu8XLJzkEUUkNARiRPntjXpd4fxKP0r4KvQgm5a6J1Jb5cTusxgjG85vLa9enQDDXw8FFRxQZtR0mPsSaZ1TIVJkQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.  مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22984" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=ZYyV5qpGbuyc25_jNzA394O3wocUzbtjlpttJYmnaB10t4QULYjyVWu0Ru_Q0q0olgxe5lttNHatzX7ZufBD1AhqGBzMrcAS0UmGaHi0s-eoOtvvIGCdTlCzgSebaqKkfizLLDNXKiRajqqgdFG4eZxbBs0rLWS0zJHNv4DxqPQP4jqWkIQhL0Z2cWCEBRs-QUYLEXLfPpa7EdYz0PphOB5kjOs4flNU2SDPY953YVz6h_0w8zLTG-5VENvfbnRPP1bo0S_7vVet7S-lYipCxO_uSpOhgZHljull0oPVRIadGuuMHZoTo3-8YzGMubRznDqlNtJYW47UDrmkrqYEGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=ZYyV5qpGbuyc25_jNzA394O3wocUzbtjlpttJYmnaB10t4QULYjyVWu0Ru_Q0q0olgxe5lttNHatzX7ZufBD1AhqGBzMrcAS0UmGaHi0s-eoOtvvIGCdTlCzgSebaqKkfizLLDNXKiRajqqgdFG4eZxbBs0rLWS0zJHNv4DxqPQP4jqWkIQhL0Z2cWCEBRs-QUYLEXLfPpa7EdYz0PphOB5kjOs4flNU2SDPY953YVz6h_0w8zLTG-5VENvfbnRPP1bo0S_7vVet7S-lYipCxO_uSpOhgZHljull0oPVRIadGuuMHZoTo3-8YzGMubRznDqlNtJYW47UDrmkrqYEGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epmcuI0bPw5xMxuJNFxSmxQIsoanzInI13_Yhd9RrYAMi-K_zfbnmciJBhcfxVOUngm-r7oCqzww9yitZjOCNcsbBc7eawewCgaT6jRzSsu3AKNc3yUHWrZlu75DzIhfBD2U15mRgjkxUWF5Jav3nOYXRuZ8NEwMFM-CEq_6WXDsj8-_pF2RDfqsdMckZ43Hx8xu7CTXFZSziF6Hus0tMcfaK0hoCoZc61u0USjbN77RPmZfvzXQDyoCCre7wC7EcHG79YN7ioP2ALpTcJR0Ahjl9hQvBv26Owx_quxMdx4lUn853jaKvIipTSo_AALv3DEX2zFFUaMbnT1ROC7CtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22981" target="_blank">📅 10:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL5HGyXjfzEz4yzBpJ--Y6hwIWofxv9Yps1-B-6BQzvhkAYIFo3rwhaPlsGJPGnrAWHF6d6xcJ8GVcEfLUvj0JnsjnBpo9SENx-sTc1eX04WcWuS-PDmUfueEIjgioaU5VEVg8-EBvUS3-8r8nPxdhaxe9nnVSLXUPLhK9gzBq6hZmYR69m-1SJlB_R16LH3sLcnc2pAGC7btFJ167imOu5uAZWFxiCZq7_X-LWoEsSGntIJFSO5M8vJfar9XCvlTgXANfhj3rf5JsrYFntBHofwpdOJA5LPLEuOctiLbzlxjKmBQvwX2d0F5-1W25zAqkUH8tpkZUhIFeuiQJQNLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات
|موندو:
مارک‌کوکوریا به سران چلسی گفته که دراین‌تابستون‌میخواد از این تیم جدا شه. اولویت‌او بازگشت به بارساست. چلسی برای این انتقال حدود 50 میلیون یورو از بارسا میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/22980" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usQ3OCtuWDrEt8_LHcpx4gSvdO82h7S9exPrm29QUIPSBcYffR-DvCfdS1DZR67hzFrvbTz5-dpsgprGzeYrIcOLUjeG_TOOG6XkQyjiQVy9hgGjJfWkBxe5LR6mrC7Eu7G9JgQ4zdjebQ062YQkfdI1DfC-UITU1kNgt8N-zF7nJLJ__Dl2V2-kOkEr4s5zNIz1Guynmk792mn8BlltbiFeZI3lFwSgODoQTcS_ahvAi4W2t5qzIw30Dk1mN68anXom5rhJr3uDt5B3-Ezg8o2EFuRw3arMEi8poh0nLjigSVAu9MjehbBVrgpbrDa-DIw1OohDmV6M3YSLwfcaTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تموم شبکه‌ های ماهواره ای مختلف که قراره رقابت‌های جام جهانی رو با کیفیت پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/22979" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeBh7qTEgkJJoKuM45pnpyR37AdExXBMcH4CcvKIj3JgLBVfUyGEw98hJnz6EMEYSj1w7m5Qiqh5LqnHkLWWIL-O9iDVbUqemXGkpnzxknjq2x3jOEyM--0xPRsBPhSyDiZ-ZCFs4iB1G6f5jNcr04xN51Z2cphmOxHkOQnb9sfkh2-GZ6tbksXv6LnD0hLdAed74Sano5enq2_gxiwKYalcbC97UTYK-E9pFKd3HRCOpmqgOGQGzalq_beMLh_ec0Y_ZHALAMCQHregU77gYpvMSEFmbugQD1Ot54ArJ_-2uFbqI68N27v5JyU5M0GuP9xhzcBJhxQVzmlSPxM8sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/22978" target="_blank">📅 02:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ap-OLIgTy6aDAAu-amSegtAI_NIDvk9B_xpZaS6yrYZtYnQmisShBLw7VD6XsCPnBeXpZj8yfj0F4XBw76fxS1rtiqRhVOIkSHEs390j-ItT4L6iqdqbxduNpQuRqTyS4TPmsWyREbQiX5w23EyrBHgyYz8gnNN4eT1txIo6ZdC9q-MBBiZrcE3zqWdWdsa9ei2sClTxUbdK79_qj1-_K28SEao9BAuRMcQ2mmz5W81BwNJ0dvBTU3OooBPCiZSwk_-HItKLgZMN4vv9lYthlg0DT83wJ7NYKrKyb96BVDgP3OXirirJ49xbUHRF_mVUtQKDDM7dmlPQl950-kCg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/22977" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwdLXkOGtbKOmrOiDOeHIwtXbRJKB_T6WYJIS5peloCkHj20aLR9PmBqvFUxexH2WgXq71S6y_dX7Pg3EbB85CWd4V4HCq4scs8fPcUXt1ElqV7RlJTHUT9WP2CL6DqsI1DtrBfcIrKYSPMTO6VJQFi1xIlhhLi3deP0Gd7S-Yy51zaFc_a_XbBPgSni-nf-w1j2jM6HMbYpcw98K3VddnqgWaj_ICYCstZP6CunGNOhDtIW_LW4SLXCWWuBTdyT_5fd-IwzE1TsKRD41aQs1uBQuG9HbkecrgjZizL1JYi7kNDrWnLyoALVLXN9eeCRYN7McICjQ7YMk1kKGPtlyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛پرسپولیسی‌های‌حاضر دراردوی تیم ملی از آریا یوسفی مدافع‌راست سپاهان خواسته‌ اند که برای فصل بعد راهی این تیم شود. یوسفی از پرسپولیس آفر قابل توجهی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22976" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghKaqW9yfEHZN4l5z6tUuCWL9cC7g8qe6_4KS6b7ajNBlg3yxLTwff5r9W3AGLppxKPwwpAuqb0zyzGOqUhv3WCFJr5ewT0eRgbl1OQ2kxzqeX3YMsuM8f77Eszt3IuISnNYqhEQ0scBv-0BemUKhClYbS5Z1lyBO4c-6ORO3JmmJUBrwFkcM_vs6w9fAJpImfR8a4v-qJN3gXb97Hr7U-DXlWBOT1BzPfPaQz6b17CWUlVyABSUJiPMRz2WGAgVlmfGWn310cOR0EH93miODEbZRE0uoR-dlI76LombSTwBGKPs46L0c6yPc8oHdX764bBzk6K2oVwZ16-scQYyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
از دوئل تدارکاتی شاگردان کومان و کاناوارو تا آخرین بازی فرانسوی‌ها پیش‌ از سفر به کشور آمریکا و جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/22974" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
