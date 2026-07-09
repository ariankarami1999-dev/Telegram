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
<img src="https://cdn4.telesco.pe/file/fKMnCr9Q6qCGF6vrgSyQ65ICG454TEJGbfmQT9z9-LFkyDsyxQ3YoHiaEUomy1vOduTewkxiR3eoPwgUv6JuWffdDRPw5BjoyOY1zk76UN9wAHHxkQo4O8p9iAKINl9tnAKMWCT4rZcJxInxY2f-t1epCRYtvk5rZo_LiXeNXkEQRQKIEG2oMWBVEORrh8ORYywZeiah5BcZ9Asu7ORfoyhHzJ2ZQ9ATTZk_A7s_cZzUEbyCzpDbymzAqgYLngMSoLuwApwzFfFkRgYejeeypBGRywRIdeF-SU-l2FU32N9BQuAhyZ7tRmhZ3nUgRyPWPjCl-ZfEIBCdcBbziccfsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 12:21:09</div>
<hr>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_3OF2rY6rzh__c-2cLGbKmxssqphmgXoqskvv9UF9FlxhZXnkofxUZfK6PcArPfPkLpyhd414-JwZbtnf2pPeT2bKqywQ6LeGEvgh-HrVE--LUhRhSUkYKzq8PTTUHjpX2IE6L3am-2E3l92wp36kJai5mjyA8NGjgynw5vkHH9HMqw5ASjupUwiHokgnrYFRLmlYxmQc5Uq6vT8QVCNbUZH5X20zGNXQjkitxryO8I0E-o3LhpsalPsQ1nP2JVVnWF1wGIFVfhpRNF9H4Uqb_Ysql0bnU6cLKAizx805NfdU8hm3dt8ThwiDnCqqKWfQCqCbVHK_CLFoxMkU-KUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/25266" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tv0-GFpZeBGLxwmTqv6h-H-EluiJ61YO5sgBxGa16_yt2WmniQQg0kXV-lsdFLANJn8YU9_rHksGWTqVDy1Ud43C2yvCX7-lLJxuOsytrQ4jIw9tK7Yw3K3Ts47dFxZqJkKLyhpNlicjFMk7TaEK13DR9J4TmtN1nX96KO26a4TtTIdTn1BoEbliz3FXVw_CQ2HbXYSOQDSWnUHXl8iBVVw7TSgJm80SwEJ-9CJJPeIzuyciE6M6UgfBMK8CeW_tZVQgJO4TBS57l1P6iO65WbkGEoU9o1w5-rIytW1gK5bMunm52e4atyWDxSaQldsjGCxAoHIQkRRv2GrMAGzc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/25265" target="_blank">📅 11:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsyPIUG-A4Gfebxl8JBGHygw2fzdrR1fWzhy5_cqcMBUNgspczQSLE6g6BpvOHxjxVXa-B_VBlLwKBdvQUw0CRdYps0JFIj4N3Hktrr-gUZsYnY_Zek7zb3QpFBXzJz1_Y2M0aWXKy0JRucAcx3QNQU1tE5aQ4RkclgNiv2DuPlXsLq0F7P8LqFm5qAIBcGbmy2y1qeqgiPM-Q10QJ4IVlUUzCRgy6OrBUJkuoeNA2tWZirLLHu8fUlJg2xOwdE1zW8zSR_I4KflZhcmfZmMyxQjeyEJdtAlwF7AzJdeJapyqSBajP3YfIapswwzWB88I6xVAA3iOf5H__XSYfIscA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
‼️
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/25264" target="_blank">📅 10:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=aD6qsJGZuR1tuVTyYLwa8nPgdO9h3KA7z9ynkb6o-tlRr2iy-XyxOcPbRlZbpmNnsPCVoYK_RkwmrDIImT27MB4Ql5DuuizPura0SKXvedtas12xicP-ifyW2yhcNfflLqsdNJwLkZnytvId093NIuGlZSO2P7LEOZoIhKyfytAXE9AojYoWQKZy0J_YXMXqr8OrpUaitmDBbzv3XMZQn_Rn8ZLcMQxyDlUr2SYOg4EXM16pvkVVzSs8_dSh_5e-qQadTsw9UFHhB2y7S4V2IU9OV2e_yTu5idMvMgVkkpO4OdwrO1uc2tMJi5ZiiXQiqRd4fk1p9rIH2-IdKJK3mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=aD6qsJGZuR1tuVTyYLwa8nPgdO9h3KA7z9ynkb6o-tlRr2iy-XyxOcPbRlZbpmNnsPCVoYK_RkwmrDIImT27MB4Ql5DuuizPura0SKXvedtas12xicP-ifyW2yhcNfflLqsdNJwLkZnytvId093NIuGlZSO2P7LEOZoIhKyfytAXE9AojYoWQKZy0J_YXMXqr8OrpUaitmDBbzv3XMZQn_Rn8ZLcMQxyDlUr2SYOg4EXM16pvkVVzSs8_dSh_5e-qQadTsw9UFHhB2y7S4V2IU9OV2e_yTu5idMvMgVkkpO4OdwrO1uc2tMJi5ZiiXQiqRd4fk1p9rIH2-IdKJK3mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس‌خاص‌وعجیب‌وغریب از 18 سالگی جواد خیابانی؛ خیابانی به خداداد میگه تعجب کن ببینم چطوری میشی. زنوزی‌هم به خداداد گفته بعد جام جهانی اول باید یه ماه تو تیمارستان بستریت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/25263" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25262">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFce7TkPocBu01EY1K82vDsPGPP1NOb2W1tAEXqD-EFq9IXe-eeXUZ45_TbA5b6xvNDeXMZ57yeqP2Bi-lN8u7x49fU_27ucGmoXTOtt_v31EcLl5A7mgDHB7ZNMfk0_G3F_Ywc9oZ9_VpaNNLFaqqSptWrGCEEff_GttHjKL7bZJW4g6foyQqGsar4g4Hg_EUQv_xWcsBdtEg2z0aWMmt7dbQXUOeYDzoxLMbXIJ0UfBqGTycbpzPlfM4SJCvjSK9xDFe81cj24xmgYBFMt_n-7rgxgFeUWN7HnwFUqVNL1M_Ln7BJ3hAy9KTiG6CJLTwn_0yfy-KXkIbbka3Tidw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نوع‌حکومت در ۱۰ کشور برتر و ۱۰ کشور پایین جهان از نظر شادی و کیفیت زندگی؛ منبع: گزارش جهانی شادی ۲۰۲۴ و شاخص کیفیت زندگی ۲۰۲۴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/25262" target="_blank">📅 10:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25261">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFa3lGLjnInVlbhpXa406gZYU0stxPOdOW4QLlh_xzRf9mXW3MKz5HRNzpIYs6hrjUnORdEFSzrcHKzt-smGiW5tBP2lv3MxSBg8tQxbHnZizmrz0sX7bG9hc1Be7hyNJsSny-ZaKNAVL6H2Vz4aV7M4wceYeoQzzYphRNQfm1coSQnoaxsYCotglcKJPT1sBFdNsoHfi0Ui6iPhuKKf0apu7ISiM2hZjUzc1k5qSOleUiGRzgREdAp_9ViPoVPsGx6bFU7mi7qZrOA3PzlDc7VQRqTOODq99tbxfD8Xt6zmwM2LBrN-DcSwk_SN2uBkJ-9PYC_R9NnSbuAnkPqhhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/25261" target="_blank">📅 10:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25260">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prfMKpWXmoEGLmXsUU-ZoRba7zPYMH7sthai8jxgw4DLBpMy2s7ob65Cd6FYXaRDfVdBcRqsPZRFDpI5BqYIxkEEVbaCNJbYz-bU7_iG1AcUfTsY_0mwvVaorytgx_IiinW6JyFsnIj-M5qyD5LvsBobbz_9nlFbjsztKuQuFyeHStw1oXdBRm-qxJC4cawZ5EVvXyGftuzEwkFhoUhwuwLsm6Z6QBGzKnRIUp6rwa1KgN6zkXppKVa00Hp8hIfYtROsmJfYy2vFQa6fs4_hLlOibeo-z0rIzOXL9NK1ATkRCjHUetDKDtgMzZnJyF67U_iLdQ_5rQF3cqJeQL5rPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/25260" target="_blank">📅 10:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25259">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXpoSf3xU6JaEvyz5V0ZGZzws-g_xaOZE0lOGzOaOU-ZfAJr2G97ALRZGnrofz22OQHfQcKI68EkPRpTK84_h_IMLi5lXSHeY6L-OA6hsKZh3ZOkg86lajzDFhHJPU2KpgyvcH0FAmd2fCbTvgCijw57Cs4oz8xLvnfWvXtMrI_0RH2Fri5cD0Q0_sKdSQWWIVFqK8PHozxg8PVmdyWFJBbDw8HLUx59i9Lp9ZCfJbl0Ur46o9yTr5lpsOy3OF-LfGai1_Rztc39Atv44gGO8P3QNUCfTCaIYe1lIfzyB_hnxALC3---0RdkR1PrZ7VnVev0Wu4gnUYW6UnkBJ4Kpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/25259" target="_blank">📅 09:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25258">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9IzGpAivKCiSiMAO5OfHrxD_DWow-SaUesgCFHvzxzyZUdN5YwL1nOuOv7m19MTccw-5VTWamJ3eBoKiXqujnd9UMxHv7-V-4GfX2zM2Hwj6cAztW8lIcapPJhbhVK3GPTM7FPcJj_tFi5y8JwABV51XljHx3A9Mr8KV75IQA_OjwDcZiHzSRThF_FsqEbSBy06P2seFBU5Sao_ztjIESBMIrVGBvKrzIiFEawcuRyBgdKP2hgcYB2gaUU7B2J8dwQkBRcpcCA9m5LOwGEUkJvn-i3ywUe1e-CcC5ukjm849JhQpXOr-5n1snS_JTqA3tkkgXFIX7UAi_mPV0ZLyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/25258" target="_blank">📅 09:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25257">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJtXPCK2WOJwrewEGZONlLaEa9ht0F9cQPOei0orvIZzeupbRUGIGL1MG_hnuFrGBZTjaG3G-zVe3cpJrL-SgW-XRRCash5AOoQ00eAoWQItHsawnJgma3GcitrcO9WkEa8Nsckzg42kQduQSK9wPPQoC7TtwZKsEF_OPs1k5ZvYRQgka7WpHuOCkdRkiTOYMKSZdlSKgjYZYWhwEhM_IOz4JciOGCJ_4XNth9dqMLvwoVE70DwylR132xMCjUmePB_6swn900nt1uHne49plQ1oEOi8655DvDuHRzf_JVUeoR7BFkbv9ExX5mHCWxEdjWYdbGO6AT-n0zQATwruRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/25257" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25256">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwM7XRzKzA_8gjcixTpo9Mjz5GDj33fYFCaCiuCpJTiIe7ZVF7MSwldD0Ijlj9aEef2rtF0UsgqNwfcCvUZOTTT00jME7kj2keQMXrvx5KtM4RYE5cJQC1TIfCP_qRcPqcfAz4cMkyWwzituScECoF_XL8YmzF0azzL6QanxI_x8C6lILxPkSFbFy1hE2bVfeuG3AJFN5_khtKwuCq_OVZUl2ISOikI4WProH_xexQt7b6j0XUQHZFM4tUpR9nPTaje4pE6GMgcbWQ6eGoyEncWTj3lC6YHOJ2e-qzfWdunBZ_6sfgFeCObhcVvBG-4B9PzYD-j3gbV3RZZIrE4IKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/25256" target="_blank">📅 09:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=sKaXffP6uUWfeo909RQdNy1H2QMxnXPuH61xDbQSiZ3f3TGHFNZNktaFtpM7MWfc4JsM0IP8Ps2cpe48QoIIc_QefTJbXDYJx5g4TFqwwZZKGAjWnDloQ4xSAPJK5yT-B8IU2acTZJPX68V-nBEsme573FyzDl0BcNiOklDQBxNyMZ0dj26GyXyrA3nxZl3F84Pp8FsoinzJNgbZMYg_MtSombVEHgOtqYBVfPC6QYbbI8m_3KV62rc2gfDLdjt5HKl-AvIMiEqMfP903h09pgCfeTyBma14ZE_3jzSzbgZ8UGpW81IOYZQmPNx2ln7OysETvGrg3Z7oHxgdTY44A5FO10GOZ6C6xyChNtRJKxv2si5ypG8d46WiVqRTbNNOcjRsCt0E0gl0UfhtcOrhSkg4U-oOtSYrYDnEyxew4or6eC8qtYLMURYzsWCLV5kGpd08X0QzvL2NJfXkcvGdHSjZdbZsdTL354Anqz0S2-lQkvOlamD53DmKLu5bWZIPJowRV85Te3GeZEtDYQnU7trJcKuzQup0eLYL-D02yTNkdSR3Px7lWKjMpMjMO9j67RxhcwMmlRDneMB2CUUeF_MQMrGB0_wnLD-Bc98y0spQ0FaISZLAEUn_NmDRVXdqDD74-lKVn-FOVqKrq2VX02SHu33bd6-KDk8maIt9Zu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=sKaXffP6uUWfeo909RQdNy1H2QMxnXPuH61xDbQSiZ3f3TGHFNZNktaFtpM7MWfc4JsM0IP8Ps2cpe48QoIIc_QefTJbXDYJx5g4TFqwwZZKGAjWnDloQ4xSAPJK5yT-B8IU2acTZJPX68V-nBEsme573FyzDl0BcNiOklDQBxNyMZ0dj26GyXyrA3nxZl3F84Pp8FsoinzJNgbZMYg_MtSombVEHgOtqYBVfPC6QYbbI8m_3KV62rc2gfDLdjt5HKl-AvIMiEqMfP903h09pgCfeTyBma14ZE_3jzSzbgZ8UGpW81IOYZQmPNx2ln7OysETvGrg3Z7oHxgdTY44A5FO10GOZ6C6xyChNtRJKxv2si5ypG8d46WiVqRTbNNOcjRsCt0E0gl0UfhtcOrhSkg4U-oOtSYrYDnEyxew4or6eC8qtYLMURYzsWCLV5kGpd08X0QzvL2NJfXkcvGdHSjZdbZsdTL354Anqz0S2-lQkvOlamD53DmKLu5bWZIPJowRV85Te3GeZEtDYQnU7trJcKuzQup0eLYL-D02yTNkdSR3Px7lWKjMpMjMO9j67RxhcwMmlRDneMB2CUUeF_MQMrGB0_wnLD-Bc98y0spQ0FaISZLAEUn_NmDRVXdqDD74-lKVn-FOVqKrq2VX02SHu33bd6-KDk8maIt9Zu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علی رضا فغانی:
دوست داشتم هرجا داری کنم نماینده ایران باشم اماخودشون‌گفتن ما نمیخوایمت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/25255" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeC19FpaPaFa9N8mvwKIt7G2Ud5hZ0vZftlamnMYRpAjlq8s-apwBJkEJA1ygLqx5yG-906baqBXex6xGapY4q7opEBQlcAsbrbohq4DSOfE1OMrSXnixSyBsgF2lPu89gWZOVwRWlQfX9_AWn06_UNmkNysIzYuQU_KmwtXJkXfc6u2LK_uGkdZihvBHuf6JtCBJs188kG8W9DXKylIqtgV1EXpEYlWNpz8qN4vJtizlVlYZnPGOY7XjaCigl9zWgJM7Diza29fY3rjEtvw_5VEYwvsZOAvIQSswXhwrjgmmrWBricKYmmnda0OPf1hvvFT08jENKMgekeBDpQYog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛ آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/25253" target="_blank">📅 08:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snXLpUzWD8DDfeR6RYyTq107KVsBGkxQpDqvcfgD9WlzGvCc0zoPy1UjnSjSOiXARjf8WZMO9yyuO22NEciepHu2beIUp7GV1tCP52X61fWon_W68-WKjjg0kK8Y_kREwQku8N4kleeS7ZXXVBuoIPLILiO5y-aamUiDFcRKDbqRh-bv3DmbH3Am4B0byd2K33yWZBxSzOtjDAMTEB-eK5Jykst_qEAMJrXXDBkBmRdCr65J13lVKIw6QKPU3q3-JOdO57HqkfHrsBJzskXLRBxUNCXLdh8oWQMeaQZ78yWF3hV5ygvSYtb3O4170ZhzhmCKciHX0OW-vKDTdJlpEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
جرارد رومرو: ممکنه‌ طی‌ روزهای آینده کریم آدیمی ستاره جوان دورتموند با عقد قراردادی 5 ساله به بارسلونا بپیوندد. مذاکرات مثبتی صورت کرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25252" target="_blank">📅 01:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVHSLdEEVmLOqwq7pOiBqT4Ot4wRUOhaU1DdcsIDneA9GYS5vRfpHyfM6BthddeE2aNtCk2DyP_DRHNuu9-pN0fNZQg83f1Z_5cnnzXcB2aQPcpDIJJwo0H59foMhhKZDfxYWnxS2tYe5uO1EWGYq8GerW_DOZaK8ZD6gmhs_YVRFYH7cfiZlvwUpZ-LQl4mPkG12sE6JCdjT0GR_Lm1p50mfFvnMo2KJ_UhFEhhV8CKUz2jagVZ55_HJ0tSRpiglEO6jED1DNyqvc0DwfivDHChOpCdUlFQLBA-Y9oCdQzh_tuT3oi_GopXzmCSEix_hPiwV1hmzopLgzgp3OwlRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
نشریه‌بیلد: کریم آدیمی ستاره 23 ساله تیم دورتموند به مدیران این باشگاه اعلام کرده که قصد داره از این تیم جدا بشه. منچستریونایتد و بارسلونا به شدت دنبال این ستاره آلمانی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/25251" target="_blank">📅 01:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25250">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6798637471.mp4?token=qDKfkkrSP5ZadoGiDoYYXWndhq8p-rrBO9n789plne07FGtrWcr44ywEdTEXo73E9Wb8s5IMG8d-24_SXs70ZoKtE5Yfhi9l9hhh0KoWOh41y0yU79dffPinplJqqXp0aAwY6gUlMfHKfi1Qa80SFs5Z_f1jdOmJ2pX9-NZ3Q65p0D1Wk-KrdaWLut_TCLQiQWF4FCqcxFMHoZs3y-v1NJ7QEA2S1RWwX9fUKSAEnQCMvyEcXhDHXJcE7f8NxxsOthX44SfqJq3c1H7acB2zOy9LDAiGI8V6zN_Yb9OcuuCSeLwgVBDPwxCX5PFSTQnWqZMobO6YfcaYDwPlM0T_Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6798637471.mp4?token=qDKfkkrSP5ZadoGiDoYYXWndhq8p-rrBO9n789plne07FGtrWcr44ywEdTEXo73E9Wb8s5IMG8d-24_SXs70ZoKtE5Yfhi9l9hhh0KoWOh41y0yU79dffPinplJqqXp0aAwY6gUlMfHKfi1Qa80SFs5Z_f1jdOmJ2pX9-NZ3Q65p0D1Wk-KrdaWLut_TCLQiQWF4FCqcxFMHoZs3y-v1NJ7QEA2S1RWwX9fUKSAEnQCMvyEcXhDHXJcE7f8NxxsOthX44SfqJq3c1H7acB2zOy9LDAiGI8V6zN_Yb9OcuuCSeLwgVBDPwxCX5PFSTQnWqZMobO6YfcaYDwPlM0T_Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی‌ تو ویژه‌ برنامه‌امشب جمله معروف
"گشتم نبود نگرد نیست رو گفت" خداداد هنگ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25250" target="_blank">📅 01:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25249">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfyBiF7nLozHl_TTRk_JLYyRs8-jx491wFImXUyoj28SUdwHgwhvQRs71GlAMXoPGE7W6jiPf_ytSE4WRC4tgLbbo-E4iO6RRMA3KHBgeuCBND7_fbjkYt4EVxZb-WmKjSWas8egFU8hjwEMt1HGA-01VQzA4vsGlW0IFrAM75VVJRJVCXtcF2I-DJGz89GTVMArZHs5KshLz3lHe-0wJGXum9atP9TOs3_ZMPo1YpqNdNvl5uQfh-6UWosz7OpNmQQGGlGX1t8RnLIYlTpEY-cGq-_62Qm-kO9UdRfd3_eRhPJddW1BxiwMuMjUY4ESBWKPWDXpCn-q5NkEW7fHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خوزه‌فلیکس‌دیاز:باشگاه‌منچستریونایتد برای‌ جذب‌اورلین شوامنی هافبک26 ساله تیم ملی فرانسه به باشگاه‌رئال‌مادرید نامه زد. کهکشانی‌ها برای فروش شوامنی ملی پوش 100 میلیون یورو میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25249" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25248">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aryq-eFvYca65T336GEj8A7sh5trzJVr3NxB7PLdGG94nn8BrF6K06xQ5fjTglVcRz6c1aYK0NdjBqBM9nMiYZmB_rKtl_bX7hwNmBFOrZ5jh0vrfaVPITtzRBzLi74Xj7UJ2gP85gRt7BpBxDGQ6ON1PB6cTzKjWUzmjEpo8_4sSmeOBSBOr9S2tFnhsobpRSXgTZEPgoXYw7Ol_fa7wKrLER1RfQmcH2Af6lp5xzUA7hOmXeNQYWxM_FmJr-9I1vuyoGf_xyDle1SmbnaH-M8a3TdycuEWRyCYtLV3G_Ou7oKDlOOe2hMR1bTFwgxECqk9v018oPI9EnogJ2bprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛
آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25248" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25247">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0fBOOSEWciKGmcB_typ-OUdbTfvKiYrWXBZKPCXtN0qqpkq3T8d_dv7I0qy6zH1gCF_tho---nuef5wfnpJN26St8k9ofvrBYYYY2XcqEOBLZvqfedmSgCCvBbjaCOf6C2HuQm4NAOb6y6oZnDm9lkVmsj-UMsauSbk0y54S9N-Rr1DHLRdR0hjWi76H2Q_hOdakOudG-LWSty1r_Sj663ubQxxOYp9HPkF5Vtr6coU7NVOdeZ0Gj1eLGnWKxiwleeuebAPN2D6gRiUyPkmCYimyXOHuaFHc8RY7GrrFZDMghYVzAIdD_9cgo_t_9dzvEB4Hk_2rrOVOMkaXHJJCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس‌هایی‌که از وضعيت امشب بوشهر داره دست به دست میشه: یکی به این ترامپ احمق بگه هنوزجام‌جهانی‌تموم‌نشده دهنت سرویس.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25247" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25246">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltTdaxveywEqDYQ9FoSJosNlgL1Rov0ecmzpwQ5zxXSnZunPgVuyXPmL36YJXWroaUvdsnEEkJUTYk5Ylt539jnBaxYYx_hbURborWR-jc0yhcM4FfnH8Q1Gs13dyQ_4ptdPDhjVtbhI8OXYVww44PT639IEcL4YY0zF2iVnFsWJswEoYPr-nvW9fsnYrtsrR9VMpYIASnuTjM5K0KFhfIkgrZmn_8xSF1Fm8FaS35aqL2C6mK-bjKOkxXD4Myzueu7xX2L1ZDMqZOCOoz4oej7pmvsXsYkQPum5ZH-YuqkHEkqALUkKqYf5hTpOt8h5ak-2OkGLMMM_r09T4g0Dvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دهوک عراق بعداز جذب سینا اسدبیگی؛ حالا محمدرضا سلیمانی مهاجم فصل گذشته فولاد خوزستان هم با قراردادی دو ساله جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25246" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25245">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giTsCMWGMFEyDbLpDSEgqWcizz7z8pGhsJExIiBkhn68yh-fLPrjDUC50PmOtnS9jawHOsK0ap9wQVFUiI6K-r9NKYuujqUKmOymfmPWi98sJF8EjDlyGjL5Oiq0h_5nuwbCz8nSxiVJZWcYl9Uw6kPnalXyIgLU9MxgxfHcr5l0Kq-J9AKzaES3vZ0Z2TDWjqCA01W5CzYglJcehEBSzHRe1jxDrFpajL8IJdBIPQ1f4D84ir9W2M0rgMOxlSfehb-YogOgrmTCAZ_1KhRloXvktyOQqewdfjv4ShxxGW5hlxml8vATJ2uPy_8QRrsR-IqL6x4cJaRTcIUm_V5Q1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25245" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25244">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7YZaaVZeXVkVje5Fhu2eeZpKVy6hGrG_EpdS_aBHunvpp_5uKDOoloi0dB9eWwhwAPwKgqXgQylRnN24nuf-CdcBbeViRUcNpo-iZNm-X52gNYfpxXQbwEw7wBLPbP9nHOr4Xk44Pg_OGeNilMRzsZzde_CUJIhDO4VpZRngHgEYlVA3eb-CJYjJyOqOVBx1joXOLLWqkx0lXwOyCVdqVFgJlPyPczmd-CZhsIT8-z5zw2spwju13KydZkvYb0yapT1rXe4e9SsPUftkowDrWdePUNs-B6xe9kJRb3YUHss5VKBvjCq4n27zs3O2Y7ikfdohYZ6J1KgQ5zBQ_zzQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25244" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6DTFwFxhPVKJcBUAwxMA4AGbeBKlAidEVL8oe9O4GuS_jvd8wdwPOawdaDuNzN8yUOtPWq-GSPwMfJUiq--VMc19-puYC2zUEvW3wYCQeDMKIL0cwOEufnGuD46Y03cmkDW23xc7oTWdQeUw6mI7hLJ3Ols1ItFsWBw86yBsAqmi8m-MaDm4-vXP4D2JeydwkaVteteyR-2RoDktiuW0sCPjUOOaW1YxAPSS6Hes2VnAiqB3Uw1KZDMAf2z994FgP4YeL_bJEtby5RJzh_cUx4n_SxrkUZicqnxOeH4zm6N9rxn3IlRExt3HzlKZlwtrucGbXBi1Sif04ECDkobWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25243" target="_blank">📅 22:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25241">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJnJDdJilWJwlkMVptV-D7qlSn_MKvHahZq7gB-LrM39rp2Aij_KuiidcznC3CwfzgdaaYXWjNuQL-rUDo7jC4Zli8Z_Logvk5d0PMq7Ou4TKVksJd9A-IrKNhk5yA5ySHw-gOzWPxV7dcQZnfsp2JjhzELql5xccCQ07V1rB1ZhfwDqe3Ouqmy-xTZtrfrr-0Ss-3t6BihQXCZX1rdd60mf-sCzSEpQmfAYC23wjV8kj1-2EJZaYvv-2GKqHyxzbZOPWmkIGe0tnapuU8045lj-6pMhBWTvlHlBf9MsVkmYZKlPY3k5496tQ4BHEYQd07nzWjN-RAy8J0mKacOQew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLGhTnG8L6nsMjydodK3gbmeuJePR-EgAifHmMnhOzze0hdf4VuIUMYcjCige5aWh66PaZG0J-rjAHQZ_3GAz8OPtGlnplBRV3Gsv1Trcmet9efyjK12dPF211DJFuoS9KBUiU0xLE0Qt8v3r4e5EVkdAVkFBJ0dBbJahUwUIV2XBnlN_2O6_QnMF3MEp1G4pV8WlqAdBhToTow8jXfoSfNxXNLKkRIU-SS-K9Bb5juA6xxciH3tWREFXiLvL8ozK4wYPDJd0GqEgM26dsnr1ySvxBsg_cdQMxqv0HIl-bRCI3z5GazgYjmFvjGqQp2nSoBliTYpAOSi8JYUO7J9xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🤩
مجری شبکه رسمی باشگاه رئال مادرید که مدعیه‌کار انتقال انزو فرناندز به این‌تیم تموم شده و بلافاصله بعدازاتمام‌جام‌جهانی2026 انزو کهکشانی میشود. گفته با انزو در ارتباطه و انزو گفته به زودی به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25241" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25240">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=nVasLUnDnQA_BLFq0hcsG0uHnk70Y1KPsBPrIVwn_Wudpl01R3dSmOyC6JJp1GnMnA9xeRCVLU3zBuFJ2GZUcMmuWrnnmPKjfVatdv39bApIZ3ECYmD1fFA2VzrR8UoavSu6yZs5aFbq2q83dWUoKSiaDk4phJ2-mckPjI95Lq6ta73z0ESnAdziH4s6IpeLeCir3_W-I6i1qLuBcmD2N7b3SwZR_xbEe7-VUqirizbohiUNMAsKiVPbuMsl9CNLbh_tdTe0_GekC8Zt7ZPJttsYRWyqFZa8ttMdE8hLaZ2Dm-fv_FfGo2dD29JxGCDW5CH-zVFW2dU1IGI3BzP8Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=nVasLUnDnQA_BLFq0hcsG0uHnk70Y1KPsBPrIVwn_Wudpl01R3dSmOyC6JJp1GnMnA9xeRCVLU3zBuFJ2GZUcMmuWrnnmPKjfVatdv39bApIZ3ECYmD1fFA2VzrR8UoavSu6yZs5aFbq2q83dWUoKSiaDk4phJ2-mckPjI95Lq6ta73z0ESnAdziH4s6IpeLeCir3_W-I6i1qLuBcmD2N7b3SwZR_xbEe7-VUqirizbohiUNMAsKiVPbuMsl9CNLbh_tdTe0_GekC8Zt7ZPJttsYRWyqFZa8ttMdE8hLaZ2Dm-fv_FfGo2dD29JxGCDW5CH-zVFW2dU1IGI3BzP8Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران: کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25240" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25239">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOXLMh2tUanPgaIYSnoOzJQS_E1dRTOuf9Q3SGEBfWOC98FFpVio5DV_TzwGoL2jeoyPLG013_LPFjkPds_ibAOZ3B5Ni1iBJIjquH_N00k6dnXrrtuX6cZBaEimysWXM9HifhWmdx-VKX-Wr5hFr22AmCg0hQx8-lli_2BmVNKP0xXE5vsgrJn0VPZA_wDvVHCVm92aj1cDQiN0Vnz17AEOwAfyfKE4q3Emw9pAeqJIykk7O7hrJJ4Dy_5IV_H-b5DggCn_QRhOMlJDXAGchjxtb2WNq_siBMcmfX9FXcEXEVS785W3MynSfWsf1h_xbTdgEzjv_f8LUC6-8kB19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25239" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25238">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb7b4dbfc.mp4?token=OfoHvYUwuWyMWPYJVtNbcVCGSC_NAeJjxS1k6dtwfYLCa-lsRNGmjA4z6QqaKKVD3Vs3Behmrph7Qp0dF7di8WqF_f54JDIg0M4wuNCltKD9c_UhKF7byK-jsYItO6NkjDjkIL_I7AN-pr8kdWyRoKc1Z3V6q-z3CiX50gRDfB3b7pDYcCf3dZ7nfForZ8X9noKUBVhB1kooNPvh1ulnRtMuMT0Dj9ky0wK3ykEOc1pQdthFuJp6HsEAFUWBVr-b9jSRex86LXnWvawz2Az8CYHvoG1_ca75RewI9FcbhS4t4pRiECVbxx47LB4qILIBsUXdBRFwKlUOh3AauzNMQVMm-Gbk4sHmUk-Qw2o1Oj9xOohEzp4c4vWt8OsEjAXjTULuKOf-oRXOanv5iFI4eHHNfAxWQ-_3KwvTQDXPaaBQpdOMJN_m4SZ0ubO8wn-PBFrHpYqrbqXSsKlv7-47_KBBIeRPzlUg84RTZbL6V1kpfpa1jPDd_i7_SM8ClO409QWXQaCW7X2f06e77bx6YsSZyscE1Q_Ke3XAWadRmNNEBPZuTrBzVTmymsjnXPjKMt5OZ1Ea5FlrDgpo9gjrGdMsyGJHyY10qJgzUKUYVyDRYY2ZCMgmzSsAGxCA7vOYnwj2L_FFVSdQtiSeIKQ5705LMBLzALCbMamW4vFMxAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb7b4dbfc.mp4?token=OfoHvYUwuWyMWPYJVtNbcVCGSC_NAeJjxS1k6dtwfYLCa-lsRNGmjA4z6QqaKKVD3Vs3Behmrph7Qp0dF7di8WqF_f54JDIg0M4wuNCltKD9c_UhKF7byK-jsYItO6NkjDjkIL_I7AN-pr8kdWyRoKc1Z3V6q-z3CiX50gRDfB3b7pDYcCf3dZ7nfForZ8X9noKUBVhB1kooNPvh1ulnRtMuMT0Dj9ky0wK3ykEOc1pQdthFuJp6HsEAFUWBVr-b9jSRex86LXnWvawz2Az8CYHvoG1_ca75RewI9FcbhS4t4pRiECVbxx47LB4qILIBsUXdBRFwKlUOh3AauzNMQVMm-Gbk4sHmUk-Qw2o1Oj9xOohEzp4c4vWt8OsEjAXjTULuKOf-oRXOanv5iFI4eHHNfAxWQ-_3KwvTQDXPaaBQpdOMJN_m4SZ0ubO8wn-PBFrHpYqrbqXSsKlv7-47_KBBIeRPzlUg84RTZbL6V1kpfpa1jPDd_i7_SM8ClO409QWXQaCW7X2f06e77bx6YsSZyscE1Q_Ke3XAWadRmNNEBPZuTrBzVTmymsjnXPjKMt5OZ1Ea5FlrDgpo9gjrGdMsyGJHyY10qJgzUKUYVyDRYY2ZCMgmzSsAGxCA7vOYnwj2L_FFVSdQtiSeIKQ5705LMBLzALCbMamW4vFMxAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۲۰۰ میلیون تومان درآمد در ماه از معرفی دوستان خود امکان پذیره ؟
بله.
شما ميتونيد براساس مراحل آموزش داده شده در ویدیو از معرفی دوستان خود کسب درآمد کنید.
عجله كنيد، ممكنه دوستت زودتر از تو دوست مشتركتون رو دعوت كنه
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25238" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25237">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EghPzcfLeKwaZa8CF7pAyD4qSPOkuuRpzLtxNw5O88Lmx1Lsi3IQUctDhFQUCGlsXlJe2fWKpYRXnwVa6ukpgmiD1bo8d03hpFhgg5AhVji2h1oyg7RxqzzRRM7NBO720JjiOQEKNxESSFjibSVAt8ORe_Rmhv4dB80oFotAGswTeQI2WP-Xt-ddHyKijSM4Y5XDYxWpuxLRrvr9Puw9fEO3BsjCgQp-5TjI8AJLtBWzNrIlvegqYGEZWwH22jMeWUKbJnnlsr9P86riu6MTgeWs_0QmQE5BqHYzpgqcB2od45CR6BJPIlp9vF8Resb5WL-VUANwaagGaq0LlI-04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشکارانیکه درحمایت‌از مردم از تیم ملی کناره‌ گیری کردند: یخچالی‌بسکتبال، محمد امینی بسکتبال، زهرا علی زاده فوتبال، موسی اسماعیل‌پور فیتنس و محمدرضا اورعی هندبال؛ بزودی شاهد خداحافظی جندین ستاره تیم ملی فوتبال نیز خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25237" target="_blank">📅 21:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25236">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY1ueQ4MSP2p-nkFKU821WDkCIYEQLYbURobuVhjZvEBrf0w1FSFv1t99sOoN6Vkb4sJP6kocJIN5aYwZuF_ziqNyb0a08xSvckDCvR3lt4Uj2XGjAq5gtXrZr4IEPTDrtPLECsCClO6QxdUwERwCFvZ0-O8HfBG2ukXPorKuLCSs6TeTpRcG_XDip8j7Tuj3_ff07isHudyryNJ1oUvl2GyqPbT-zDLCx1jpNCPTuVQSMmQYf95Y0d5PGXu57Y0uD9rcrxJD_Yceex9QlHjNYnLwONxX4O4CrNajkM8MB1Ghhgm2sYygAR0Lk1yma7bEj_Wdp-fe39FZlJNP6-QcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
بااعلام مدیریت باشگاه سپاهان؛ گابریل پین دستیار ایتالیایی محرم نویدکیو از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25236" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbl0FotxjX3zfyUiPtZh8DHZ31rTySlOY_6EI4peCjrW73_TT5LSwMWxkkdhoy_CfVlCQUwW1BBZv8l02qExhI4fd6g--hYqxzPkSYWMReSmy5x1GFwRlf2SL390W_GEs-r-WUcM9bPvQOzRdXnMCOkfm4fuhuPjUvDlCi7NeoeryH4vV3_i4B6gpEUMO1h87orey0fymKJtMQAkmdHIeyRYePMkJ305XhoKUxuEGUwfDP0yrvGvtHtdg_hRmGVTzFhHZbcBMzn4zNZ9eO-Hu2yNH0hnDszoWTtsKIxSqckcAgDbBxG-XzA5FF5MqMcQCKuq7SO8G2STfTuvwoZDQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌مثبتی داشت و حالا درصورتیکه‌تارتار تاییدکنه هادی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25235" target="_blank">📅 21:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_76EQ-yVw8T3eLsXzqLkb8-Fay5UKzismMWVC2Aw3dCM6VhwM8iKiGxmz7X2Ui7QM3gYDiFWjIdJP2hD-TTLUgsmbJnoC3yiqBO_3l4k6lgnldRkETq_2351TJBe8-UdPPwQQs7ufK3Hu7yPTrFt3b7QODUIptFvrmXoLtQ_AuAI3V3UhuSdRWxq2TPFuPKOVxK_dtNVjC9hnZ62wMwcJgLmIBdW1fWxmiu-9_4XAihrRBSzd6uGF6-xhpJVshlo095bOxyxcAugmFKxyB-YDdnCVEhx7dKy_ofCnE8m3_bZx9FzYFg7O_aQXk7QqanDN8QooR8vIGhoyk-W9ZfQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران:
کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25234" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzkH80qvDV78ItFubxCMV0aceVq4xTulPod86NMNFPi50sHYjwMzr-eWiOfdqrAld1V6G3_TeQdXUZdB-9Jr_FHHfUYZGHQ9iMd3zXG-p7Y59wsmAukakUjFKErzmvO3SOJooYsthVw2tyKAGAX_2ud78SwDU-TxYiqVWTf5koNIw4IWWYjXeRhKrbeC-etpfNC-GWt2nf-tlS3UuHplTfYPCDaQp1y_vBsQORfcwx2cZIAZN3EZvZPzdLfF_3gUtPfDq1NZ5zjjEuZCR6wSICNMg1gOe8diZ0niLCaQARVC9b320m6ehPTCu7x0_crigIMyrhR9fo5eo4_22Hds1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25233" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ev2hstLi3EdP_hjixdfoEasqEgLqnjQrWMG05iI2qnQCPING-vY7xJUBI6GmRV9lBRxNSZ9LS8vjj_ITlz-l145NYbbtsqQ6VP9sbshbBw4BybIRVh5xysBlkv0rMcZmbxMFKmXE9hsJ_BIdV4onRmrXVmdyNpQ3FX_sTP9FFveSb5apeIYLhiVEzo5ga6AYiVXJ1i-y3mr6kH5_dOdqELSxCXoIdoDrY_JejrvRIyChZCLRNrPZfZmzqhgoEydtECNFvHrN0sSuKtzEEVQKzVY-vHXMgwJfTC02abKwd21DLulRnHdh0lDkFgWmNhGDdj_2R40a2L1cYXeyca5RoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کنایه‌مربی‌مصربه‌مسی‌ولیگMLS؛ابراهیم حسن: فیفا میخواهد مسی توپ طلا را ببرد، در حالی که او درلیگی بازی میکندکه‌فقط 3 نفر آن را تماشا میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25232" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBN4fJHk7TNnKkC0Tom1S9jE1o2aHojgDfLxISlpTvHRligrq1jzQuNHziL1Tykdshxi9OrjqbLVgZ87z7OSt1DKhA_89LdE0G2OMRm40_JyC3Tjom6fh1TomsGwXzyyqbcJ5clDCF5ETnJzewJUIKQN068G8Q4P2o4XZ_Y9Ufv0QlHOyzhcaERFb9hMh9_EvgI_ovTGdwPgkyjvdwhX-vM8duBdCHcZcc9x8OZdCiv0eUwsB0Cn6WTiew46HVLKxVfpxiFDhLIVN5G6Q4mdL0G-fdnK3KLjkkXJsVzG44NxvgYChNqbMcj3sjjLeMB0KBLNerjy0sm6PIwa5OEsBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25231" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So47jyoltQgdnPKEKft-Y856B2PrnIQnK3zDVkewDp7b3i16u0ISlDgBrj7fjcvLBqkB0Rtf0oeunLT1sTAXe-mW2NgS9rW3yU1rImlTaPEFJReK4K9-txG0e3OahT4_R1uuxRpkvQGeOLqNKr74E0Q5fAl0yFMDz-ALfeqexFdwtF51qV3LUeeRUt_5HEA99Cweas_Kwbnb-hhUoSE0drn2xuwpLaUMq_91qvK-gT6smjrsCiqCzemyulORikaAs-SucLzx6WpP-i0S6yixU850eMiEIFu1TuDrSeRuCnJHr9spoZpGPoAEfvEuMo-vgNRtdyRTtOmcVi0fdgAerw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25230" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvnIZ3NcIW7RHnEMJPR3jdqiHvsepREqo4EPhOmePSbN_AYxDcOqus-SWnP8RyGoAO834DYy7K4nVC3wRJL2y6ib_9wNEO_C-tsoEqAaVeKx2dirtSkhxc4eBZt6Hw3jtE4YStuexWYl4PB-PLrj3OX7YIdWskOWomCV23pDsRUSD7mHOEbBKzSj0KPLJBSpMm5G3sAjALyOHvcOmCk1MKrDRuZBdxtUv6INfvvfCRuRJirdZ_iWaidpAw9PmioTYhhGvO1QrkL5BfZr3LtaIGNRGKEBDtSAq561Pv_aknmyIvRPFjz9JncfJJkFeafqo9u7DyNBeao0cF6St0aUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25229" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=S3l0s_Q8MitM-D0RIBVvgjJT_D1CBsDPqDw9DbCRvs9I8Qan4WZ778pGUZth6paKpDNDeMpOa2K1VenAU-mLt78NNdFiXC5YLPI-4ZI4TRRrb4Q77ntgS5sw-4cL3ppJ9yLCf6kX3e1GfifplACaCPW_h2bOR9ioE_eM_evPCiGfo8k2jaFzTZ4TpTG9dnekj-AmSlEPzZPci6fVi6DiBGOTJdETJJXMX916VjTTKqNtCs8SfPxhdEj8e5DOmz1ODMwg2coriY5RrFFan0tzy4EMpmReOl8a8-M6ev4_l_FNAKvPjgCWkizYqNY1eYr9aK2FyAP53Ghdgef7Vz5c4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=S3l0s_Q8MitM-D0RIBVvgjJT_D1CBsDPqDw9DbCRvs9I8Qan4WZ778pGUZth6paKpDNDeMpOa2K1VenAU-mLt78NNdFiXC5YLPI-4ZI4TRRrb4Q77ntgS5sw-4cL3ppJ9yLCf6kX3e1GfifplACaCPW_h2bOR9ioE_eM_evPCiGfo8k2jaFzTZ4TpTG9dnekj-AmSlEPzZPci6fVi6DiBGOTJdETJJXMX916VjTTKqNtCs8SfPxhdEj8e5DOmz1ODMwg2coriY5RrFFan0tzy4EMpmReOl8a8-M6ev4_l_FNAKvPjgCWkizYqNY1eYr9aK2FyAP53Ghdgef7Vz5c4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25228" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsW9gY1TIJGd38J5NPFuMIbjcS0Cx-5lcz56fgR1icHE6Kot1Bx7zgjSc3pMx8DXlQsRZqs3fFiH4d7VlJfxhmzIjeLFhHH8sEtg2icUMSxx4zsjEvRqIzOlc7R_UCARipHsJLr4bK9xCBd3H4nWO2mecdh87lWTISlmC5gO9uIKfl95FcHAhxfvPJgk2R5hbbwIPs9M6FV6veJkYy-G4Hf29GFugiBJwsjIoQmcxWPGlb3Ukf7adp5Z3BDc-4Kh09oAavsHXaQsOpTQQwq0D5BGW3NOp0_nFKaUEPHj9F8wWesdCOke0bEsLlEAyAvmHVe_Rrex5mbXN3-SKAD-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25226">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRULpXcP1fF1Fb1N6bO1XMumb58Els1RlXbGB2dp_uClWWAM7AeR4g1hG9T0jrTxFt0h5vbb7BtwVuSksPumhYSCxwe4o9FB05ibmq1fytc1ZvfNbK5NqOKlzycdM1rk1e7-Vk2tnGV9LGXHvVF1B8cgQeYdMjKqGf2qjGIwjdYucIcW_5tHPJ2ep3qLHFwRbESwFclelKHx5P_j_2URgouSkvK-EhYWsq2Rf5OrpXao9tUH4b-brTApoIv7eOfCRE81zjb34aBXcKzyP2jZHxN2rEu3eRch3ZOLmH5GFwQx_3xBtiRDJtRP-Kp2txj48ZPVcZ6k-MZC_tkXEEH_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب اصلی پرسپولیس که امروز رسانه‌ها تازه دارند روش مانور میدهند سه روز پیش به عنوان اولین رسانه ازش‌ رونمایی‌ کردیم؛ بله مهدی ترابی بدنبال‌بازگشت‌به‌پرسپولیسه و صحبت‌هایی با مهدی تارتار سرمربی‌ سرخپوشان نیز انجام‌ داده. تارتار بعدِ اومدن به پرسپولیس‌بلافاصله‌نامه‌جذب…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25226" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25224">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jhud7uHRogFByurVbXBBY081ezHUNca94zXnWY8y4dlhaGyt21C9f7DADluklHYEAjP0_DP6qB7l1xqhVyQaGU37jzDzIVbGPSZvmiBC1rIt_6nxpl6jOPWECOD3WhIs1okdXbDUMDl-JkgxZk3LmRzyUx82LMVdNpRlLX35QkB3CwKTcN1hKmhGs00Q6-wHi6bCSGg5SIIFR_XK4H3fCRGzYMu7tD8vheCgIcZeozMbSAPd-nDD6QF8d7Paevkbvl1CODQMa0SK1u8epY8Hl0jp7dqAO-_Y9aISQpqex5LfG5e3WjOM6uSYDxn3jAmm0by-lp86sT2YOx-bMZhPLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در‌اقدامی‌عجیب‌ازسوی‌فدراسیون‌فوتبال؛ درحالی که روز گذشته چادر ملو با برتری مقابل گل گهر جواز حضور در سطح دوم آسیا رو بدست آورد اما مدیران فدراسیون پیش‌تر نام گل گهر سیرجان رد بعنوان نماینده ایران در سطح دو آسیا معرفی کرده اند.
‼️
همون موقع‌ای که AFC خودش…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25224" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKvEQVL5Gi6pP_uoc44cyYsb_4ZiPBl2upNy-dj534xA_BIAlr1cV_YyqOfdXS7a6OSU-z726wfNnuf0gF_DiUkr5eVtCQmCqJ6-T2pYl3xMYLHdeXJb5smS32W7fNtkVfKZZ0pVKE8B4fXYQKIxB5tVMxCa5tJo7wGKbCjclHQbiS7g8hIj1QR-ntCiDJjxYRqyv08m7DKiH59tPIQtoohZEI5VPrzCuNwuAiPgwdaVahKPSY_qJ0KYEAwcJucUpR3hBXr2SqR1V6jde15d4UvmWrO-78V-BM1hKWv_VtRbz3OWp2XVv7IYx0DqNrEZUk8WQNCyHjKVYIt2zVVL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در صدر موثرترین بازیکنان هجومی مرحله ⅛ نهایی جام جهانی 2026 + توصیفات زیبای عباس قانع درباره لئو مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/25223" target="_blank">📅 17:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTrZ3DXy9_NbU50_3DY0GvMXcLugy8UEwBgACTHbbhdHvJZukbW20JFHmk1IDqEX9UBYGzU5nmpedMmUKG2JisQx4QXWOMIWZJ5xzqJ4sBZeFU7a5bmZb2chMFbI5mJCkl9xBQbBK26KVDbThchrkmRmDtYGM9VQozSJtfNOtakUsHTWdpzX3BMTJ_vd4NBq3LKSBJW2REDLFoUcrMdMyxllGmzwb1IWNTaUtbqUA-Myq_fuBej6Bq1RpkmhObhmuzwjQ6xxhFsUyaVbxwWFPckVUGHHiB9C1pY9C3_ASiEvVqLRTSDFZM3KpyIQqWqBYSB7qxhoe2zXjFy4AYRH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس ساعتی‌قبل‌خواستارجذب مهدی ترابی و برگردون این بازیکن به پرسپولیس شده و از مدیریت باشگاه خواسته  با تراکتوری‌ها مذاکره کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/25222" target="_blank">📅 17:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9HwrSFXt5kqyjz5fulcjQCK7yUilAVz03ZjBY12jhvtpHvLAeCq8H2H_L0qs07P_tIELzrKo0FDA8lmuTpSxcYHwM61vynPJ9SCsK7GITBYtyiQBPdgOGrbA6EKJ-yL9HTGlM7GsGwczr9DKqjBbypFMP2hoXFMee6RuLKdjxAZlZNbk45jq1iAgCgGBL6ys5aHGc7DpkW1pRhztV24hNgg-JQ3RgXm6WS8GaenMsNBHYIR7V-m55lsdsBS4pk2m7mT6dRhi52MQxQfV8lHTEeh0_nHJd-rmtv8W8SCeeCq5zBgJjhfNHY7KanKJauYPVhcj2i-EcCjADRwv8gAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/25221" target="_blank">📅 16:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0qQ5fRIMR0USYJubn729ga3P84cHuOsy_ErVGwKOpp0AgC9wXiQzh7AZGMruacGumzvbv7GKonpF_VKaqjaWge3os1nYbrlXDpEaznQwaiyB6CZ1SvD-XrfY1cKv1oAbMxSthsjbr1ZH05Lky3S831KEpZl0s2KZZLjo3DMSVFjYrNGGzxltR3Kr28QUVu6ckaWEkQZallLogJrt78TMMrJ6ASCTuWXzzQn2roBt_slzAegVxI4zf2l7vi3BbIjZjDvohtuDcvlsk0dmreG7Knn0LHXi_m1Xi9X-uClpHOZq838SvDMo40NGGQTjygz1KEY67QeG-zWOXOj4jdmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/25220" target="_blank">📅 16:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQowWeplOJImRLRh_oZaIh7Y1C2CO2WHQY7-_g7QKmgLsskFKXkDf1QYPOiRIKnsgzep5rj-FJeK6YTn3-jzV6-l7BWox2mVFSMBguo3kJnQ1FyRQnZNvy2p0iV_shhk3-XuUmb7YJ2_jYyhixBY26NmTOAntPPKa-OK6t8e1BdENRkkfqKLefD49yjj2Xkf5yoR2gfFBmrPkY24WKyoyGV1g8IJ06ubCRRsQPMqgyfurnfV_mB0D7HnbL-zh5bFxFLdLp1mYKHHbTmpGsPjpArrQr6lZAXlNXRa5t95Nk_qntzxJ4I7cDWWmuyT7artG_Fx-gCtYUoi6X8eV5F2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/25219" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f158271b54.mp4?token=viD1SovFzmrZSHIFripmzJgneLuGDvnM3hqi4wudif8IZHoLjFNmI0WE3PkMYi6w3jP8J_zZrSzHPznFJPajAWr21ALSFZ0vxF3UqOr60jSvHaCddOwbNwpPU-DainIAqgrIjAOml8HJbpP5CQC-94PB3h7Fe2bUo-XiSUQVTqhTqb2fLaBRXn8D0AYGYMr4JpRkdEJG4EnzJgs4YFJg5103SNKd4zbjJ_PXo4cXY52SW3VFbghbu6vjO1VGECWKIixofYoc8bLLGZYs4J-dDG_UsBbg3ahnaLeYSWFiKOVFPlAcIGAk8r7sAqaTZj8DdNNqIOIN1G-Ahp1tnlU0PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f158271b54.mp4?token=viD1SovFzmrZSHIFripmzJgneLuGDvnM3hqi4wudif8IZHoLjFNmI0WE3PkMYi6w3jP8J_zZrSzHPznFJPajAWr21ALSFZ0vxF3UqOr60jSvHaCddOwbNwpPU-DainIAqgrIjAOml8HJbpP5CQC-94PB3h7Fe2bUo-XiSUQVTqhTqb2fLaBRXn8D0AYGYMr4JpRkdEJG4EnzJgs4YFJg5103SNKd4zbjJ_PXo4cXY52SW3VFbghbu6vjO1VGECWKIixofYoc8bLLGZYs4J-dDG_UsBbg3ahnaLeYSWFiKOVFPlAcIGAk8r7sAqaTZj8DdNNqIOIN1G-Ahp1tnlU0PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب‌مهران‌مدیری‌ازدرآمدفغانی؛
علیرضا فغانی سال ۹۹ وقتی‌ایران‌ بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/25218" target="_blank">📅 16:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGAKJWw1gOF2Npw48cyVmIU0hPYrqgl_GySc9XXKO_vlfUE4K7UzKJucs9bZrD7YMVdtPWPPE_uISH_a25j0FLlP5K6L7ezO5XIqRxm8yb2d_yv8Fyk62BIl6HIl2E9ur3Tc72m_peSFNQdnH7zpvAoiCI8rpIDZQJHXuKE8K17q0aVokncteKr0nkNiss6ryHVC26TKWLkD9WcVRLO_dS7S_4pO0PcRqtWxA-ZV7pznkvcXKvtIaEyP16LMC_owrZD4rDLHreS5h7_6CeWvN_st9i4ncmu9xAGBHykky-NwnV7NBGrnBF50b5b01Z2jIprqqD5yaGiG1aPVKQWY8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ علی رقم پیشنهاد خوبی که از لیگ برتر لهستان برای علیرضا کوشکی ستاره استقلالی‌ها اومده این بازیکن بعد از مشورت بااعضای خانواده‌اش به باشگاه اعلام کرده به توافقش با آبی‌ها متعهده و بزودی با حضور درساختمان باشگاه قراردادش…</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/persiana_Soccer/25217" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25216">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltK5mycuhiLXKTw_B4beZnr1JKS-f0gBmQd1lmB0FHwSvjkdFN_vyiTlWBEo8TwGmXGQNBXrVhRfim4fL3nzqM1WAEsk6z8dyc7HzQVZrOOChpQD8uGTK5x_MllXo8c9nRY6dJY7f2vUT3eLv5GUl-ZFahSXVQ07nR8xnFBuCTYQQpLGsttL7GMfJNbYDlmKxI01cZFxh0tTP9cfGAM158GkINuEllteZ5P1AVF03DwjvGaBuN7ne6MMFor-tYQziJydYW4i8AYQOqmYiWlus2Ywn5UMnGbgO11syP53CDne3DNZ5MS_eKTCYyDOatN_lno1_M98AqgrmNnUjikVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی #اختصاصی_پرشیانا؛پرسپولیسی‌ها به محمد قربانی پیشنهادی سه ساله با رقم‌فوق‌العاده بالا داده اند تا این بازیکن رو به هر شکلی‌ که شده در این پنجره جذب کند: سال‌اول80میلیارد تومان، سال دوم 110 میلیارد تومان، سال سوم 150 میلیارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/persiana_Soccer/25216" target="_blank">📅 16:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25215">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGzAKxhtLNxB629JeTJL5DY57mnE0W1rkHHBBJHBpYU3RyJ-qGxiCVY3XHiSQt4nv6Um8mxzD3jsdhvmnuYKKw13KlaCgN6paGXqZQ8B3G77GLOF-cQwP8jf-hZyl5_CiooDODK86j9us8Tokkl57ie1-w8sSiyxvVrULN0EClkiFH4xxYncX3TJkPVmGQ59PLo4wsTxMvDJ5uxFpN4UVix-klePixcIbSk3mptbpzKj0tvywISkYkCJKZQ6hYURIGmv2PD0g9v3FfS8JCRwuu81wouW58ovlp6hj6VnWCvoTNcI1c2I2i5OmjSlkRpxOQIYB-YIzIaFaGwNeSmTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ آرمان اکوان باانتشار این پست در اینستاگرام باهواداران‌گلگهر خداحافظی کرد و رسما ازاین تیم‌جداشد. همانطورکه‌گفتیم اکوان از سپاهان پرسپولیس و فولاد پیشنهاد دریافت کرده و ظرف 48 ساعت آینده از تیم جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/persiana_Soccer/25215" target="_blank">📅 15:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adYscTb6iydjbXJ7uII9a5c4Yv5leW4nwFie3fIZx8wJpNn88X25-yrLlDebftFbkc6tHgp6-L8ec9jadxJFntTQEi-ncD3RLoQjl5L6Nmi418vrKTxv72xMbJnjZr5LQdUSj1tkNDBWjqmnTvJyIL56GHPXGoE7P4VU-kjZBh3b7AdPzzAL66S5ImQ0KNLNQW5PZcRtBrHOR9jEWADdpU-KAYkg-pGU0_sb5BLT3cDXSKv_HY4DnW8DlPOLMbc-vYj6FiEl8s1QkFsr_vYjmwQdpO7jV7ni91KNwS66bhE72mopOoCTxC6mB6ohfCra2Ha2guwjW-QfR42XQ56jkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/25214" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=DAqCnEGrLkH06ar9KUi0XedCJzX-8uoacOF8D5xLmV2ztPzvcvjtQN6cAm0SfAz79yjOHQxMpd9W3SvZdg3FBGCbP__ukHo0sFiLBkwxEVtBI9xKI3QFl3LcH1DciDQHJ1gMYdsj6QGckH7whfABN5uK2oLViFWXArPc_jLcXj8R-W7HqawnCxpC8CJOPIaz9IWZSRW36CNouuxCldIzgO9gWmne5I4Hj3HCr-xt4RU0Qur1sDm1CT1JUh-lE8NaxCEEOTAowDgcdCSZF9QPjWM_TcFeZeqqBn8ODqG_peEtVMd3FytilJlnNc2ORCVLW8nDVEz8ZsE-_f4Y9eBAjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=DAqCnEGrLkH06ar9KUi0XedCJzX-8uoacOF8D5xLmV2ztPzvcvjtQN6cAm0SfAz79yjOHQxMpd9W3SvZdg3FBGCbP__ukHo0sFiLBkwxEVtBI9xKI3QFl3LcH1DciDQHJ1gMYdsj6QGckH7whfABN5uK2oLViFWXArPc_jLcXj8R-W7HqawnCxpC8CJOPIaz9IWZSRW36CNouuxCldIzgO9gWmne5I4Hj3HCr-xt4RU0Qur1sDm1CT1JUh-lE8NaxCEEOTAowDgcdCSZF9QPjWM_TcFeZeqqBn8ODqG_peEtVMd3FytilJlnNc2ORCVLW8nDVEz8ZsE-_f4Y9eBAjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25213" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGjU_pq32isvEhjjjBaVyqjYDRnMHsKPp2sWUT3bEvGP1zrceTl-pK-aXevJJ_OILs59Nj7FGOeUt5cA8WiHDvoarWRP4_immGs1gsD17hddO_PLLDNMyCdOREc93FRksHMnPjm1rrv5faR_QYAgVT7eWh2TEHcUUFFRPDVfvs28y2DU-96d4BOflHHKEJGi7W7mT3DgMsAtIeXcZvLFqWSTXSFzQakqnJ6ISvbKkSgifk6YhC1Fbivup9szQFFJj5evDY2ie1RfPlcnJX6_BNfhURT_UCfMpjU_mm4a6Bdl70scVag9AIqzWiuRXxxAfvnZYcGnazUtDhwKipVz4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«
وزینا»همبازی مسی میشود؟
براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25212" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ij5x75u0bTGyVNOMabfy8vufczKuIzkjTJYzLK_Eu9UTjRaa_6zm042045X5jTGZB7nwCX3y1_F1kX3yJlhQA_5rvlOKsPsHXDyVU3CiaxIaBtpxNxxt2cJuFhrED-3nmAPA1DEjnWc5yriu_Jnc9SM3ucT6weADJato3P9T30bdRGTdqV_b2zOf2aPgM9NZGakslERBK1wV5nyPOiAvnIUpS8rncAYP-qjjJDOWt9ZlRUp99erQ4tRgDBTUO-_L51f4vUcl3kKcIfPZb0kbHbWAyh9KaUZn9cDBcZrizMhoVTma9NE0FflTYttvJl_cfgZarfMA1OAaUkgB94XTrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25211" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEkfxam9GN_s05GAWG6Id6rrXB4t4ZQQGcqc6lq4uxl0BmYQ3EYufWb1WMllaX6tJibBc4uwbnLKucbcwzz0C-sL75vslG6Lhs4wL8mRR-HCXbM0EG6Zn-YXQGorMFrCaKwRHBny1RI-Vj6q4Awb2bPGXigJKtR8IopPrHgl4bR8W-S7nBj6ktR28fUW-Sec9gvnfiI0yg9vJzUPHZ3g_-xnk_W3nv4KAdhmXZiZ-3lNQDBSDYuxcsQ6Sw-YH9TMxiogpnZxhysE1uD7pffBfhjQwobh9N7t4YuPP7raAHqAjdUVXRZp-D3tBw9RuGrNNoM6AF9t0E3qZPQuHpkV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل‌ جلالی بعداز امضای قرارداد خود با تیم پرسپولیس ساختمان این باشگاه رو ترک کرد؛ یه عده میگفتن تازه الان میخواد بره داخل ساختمان باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25210" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IImI4nRtJxL8zKSSUmS6u4CmWlydJ_8ABh-Kwp_XoJ2GsyoG1UDIh4NwkyBOHoHdQ2tJXvEbSbvNeldqmLi28ZwNGIJ2CLAHgT6f6NSqKzqZXXpXnoTlgZIE-O8MNl0bfyA0YWNU8t1iD9owOyslbvLHPbUre26Svkclq8veGXNnFqzQLy0vtPMwnLFsvskz8NoQ-CHtfL1OSkyCoLTzkvIbk4AL5OQ5aFvvCNHBbLZyXRD8h3SgWi0p8f2dpi7p_BZwvY2cRn9fgdUphYwGpi4WwwaplBrkrSQxEjOhazDwJgh7Kie2QigbIto6qXdEaXlKOFxAEqtHFVyfkG0tEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=IKbX_3E5_267Ykz8QV0cIsDw1iYbgIazjlWg6Y1jdTLgxRP8_Kz7Tww0X10eW2ySOPRIPgz9Ia3x7-t2OvgUsWESktHIWT6ANGVA-BeAPF7XmgA6bb3tPnOd9mgIqelExKTS4ZneH3bWIKll8avCz1n2Ne_Z5Ks6GVXxKRNIz34pT61-TYYv-VVqqSCmzd5nCtRn99_KK_sSb_Zexd_lYNkTeRrG5uesY6CxG5vzEuR0Q7Zwxvr2bSnT60aS3bmafQOVQQN2ffyz7NF45ZHUHJT66FLrPmFFmd_t6M_4HPvXe9byxiAP0_4HlEGtqK5472qPLjGxS-XhgIE3Qne4VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=IKbX_3E5_267Ykz8QV0cIsDw1iYbgIazjlWg6Y1jdTLgxRP8_Kz7Tww0X10eW2ySOPRIPgz9Ia3x7-t2OvgUsWESktHIWT6ANGVA-BeAPF7XmgA6bb3tPnOd9mgIqelExKTS4ZneH3bWIKll8avCz1n2Ne_Z5Ks6GVXxKRNIz34pT61-TYYv-VVqqSCmzd5nCtRn99_KK_sSb_Zexd_lYNkTeRrG5uesY6CxG5vzEuR0Q7Zwxvr2bSnT60aS3bmafQOVQQN2ffyz7NF45ZHUHJT66FLrPmFFmd_t6M_4HPvXe9byxiAP0_4HlEGtqK5472qPLjGxS-XhgIE3Qne4VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25208" target="_blank">📅 14:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=PGviVT9gmupgH9i87-ON1Rwe8T_LWByehssIqH7-rIYraSyBTp8Ouvgx2HjkXDPGl0eiFjVu5btgkQB3zPOxX-MoOKqhBG3nKuypkrGtmdH_E3qTz6xbALPL9TPn0q88XFbOvA9ONqIYGXXcvl0sSGTlEp-PGUEeASpwPrfA6-9Xo97wp-aMr-4ic8C4r43Js0zKHH6z_7HBjw6DbTC3quBunuejJ05sxrl7xhFbeYURKQeZf0TUNoG8I_NwnxnxibmTm-XJUxXKeOh0dFVrSfbfLotyAcErDXJNPDMPbm322uOlCPS5C_OzbYH2HUQq7a1QUJxEfViSPsmyMC5YSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=PGviVT9gmupgH9i87-ON1Rwe8T_LWByehssIqH7-rIYraSyBTp8Ouvgx2HjkXDPGl0eiFjVu5btgkQB3zPOxX-MoOKqhBG3nKuypkrGtmdH_E3qTz6xbALPL9TPn0q88XFbOvA9ONqIYGXXcvl0sSGTlEp-PGUEeASpwPrfA6-9Xo97wp-aMr-4ic8C4r43Js0zKHH6z_7HBjw6DbTC3quBunuejJ05sxrl7xhFbeYURKQeZf0TUNoG8I_NwnxnxibmTm-XJUxXKeOh0dFVrSfbfLotyAcErDXJNPDMPbm322uOlCPS5C_OzbYH2HUQq7a1QUJxEfViSPsmyMC5YSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری؛ابوالفضل‌جلالی مدافع‌سابق استقلال برای عقدقرارداد با باشگاه پرسپولیس وارد ساختمان این باشگاه شد. قرارداد 2+1 ساله توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25206" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAHaqY-kv9mR5xxh7YHG67NFzPhk--iW8GyuF1wpptR__uPuIdlq7VFkExCq_F7zI8sHwP-TQ8_o22QL3sLvjLIyGNVOMUhHxZXLU0gt8Fjt_eV3lF0y_OuTTwbjzSLB-K0p1bnnwT7yRMHu3pYEbIdaUpBahPh0CDLBetVLaYgvvXBS2JMAcyDbncZjVrP6t6VswYGVMtjUZ6EauwHw_uSqLryQCedw_X27_ZiDAauj5L5OKVhTdgLpSwaJxSMsNm9XG_lDpBAw4wtUdQ7O7pIcXvSrLQaDQWsMbSbi4EKNUxIPrYYQn31P1dBTPLa5zUbxiwrug03CkhniqVcP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25205" target="_blank">📅 13:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bstKIIPn65cCmzxVFxUFFIs239eGqIxaiSfFRc_ErlhCA_h94whfG6ToCPbOJRexSi7G5C-AvbohUY9P5z10W-uFJd8SqUPbkm4alFxWW8zvWbcfCV8eH50FJaXbYbd7exjwnOcBndSrZ7pI8dOka14v4qib8NF-WhQ70Zbv0i3OaWdjXcDWmWrxm-eUBYkoOn5D5_Jwd9psM0y6Qy-BYDzXsisQBA3MQIjTlFD6st-OwmqsdXJlmhhgl2x0SRt58jkQTFRB_qvGkhWflig0zEghc7xtkAzCNqUO8oczzpM5qEGgYq8kR9l8HnWCXYeLKsi_Rq9Bjoo6Txefr6KvYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25204" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=Dp0SeFnQy-yla4tbkHLdvryRvZQrRpw3hzAZrdzcTIr694lVjvy7tBJg42QgY89dEP_MRaU_llLsFsDEipkQjcjEkaGHQfCtzoR39k8abRPjOx6JYsadmItfHwEnOTEmirdrGIAjki_sc6_Xsaixvld7Kk6hy2rAIQp8cjdDnOkWrf1JpdaWYGg4-Fusv8r6BeGS-XaQVsVn4Hyhp0uPLVNpBOCl8aybJPJOReNQOz_BTrqXjgjc1hAVjSemZqplL7odB-4AFfmh_2ByGhxcQ55BICEENbx6rwiGoneaItVIXAHYjQIWSbRykrAutXN-smyCKfnNBfMkGog6iG4j4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=Dp0SeFnQy-yla4tbkHLdvryRvZQrRpw3hzAZrdzcTIr694lVjvy7tBJg42QgY89dEP_MRaU_llLsFsDEipkQjcjEkaGHQfCtzoR39k8abRPjOx6JYsadmItfHwEnOTEmirdrGIAjki_sc6_Xsaixvld7Kk6hy2rAIQp8cjdDnOkWrf1JpdaWYGg4-Fusv8r6BeGS-XaQVsVn4Hyhp0uPLVNpBOCl8aybJPJOReNQOz_BTrqXjgjc1hAVjSemZqplL7odB-4AFfmh_2ByGhxcQ55BICEENbx6rwiGoneaItVIXAHYjQIWSbRykrAutXN-smyCKfnNBfMkGog6iG4j4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو ساق پاهای مسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25203" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=OZQm2w5hxhIsKAPCXSlTZklR9s2lW051IomM416SYdJ3BpUfdYJfMxl0ucxY8evyDttRXf8Xmk5iF5wQhBN3RHYZDr4_HbTc4ER55635WhHf3nCHIdUM2f-15jmyBXD8GL5gScP7ZmBuDEFyGUpc24TrzU1NfKeCknW1iCQv7upOFi1t-gl7xIUa782JLCUzIEiLgJlTCTsB3v4nAC4tcKNuPsdS1OX0LtFbXuj1grlUnqC0VVtJZndsN2XN2JIaG3g7R12XGiFLhvq_AuAeAgwegxdeQW6njPPi18l7DPMCcz-sPN3l71Cmf0Eh2Bu3-Zd2Xu4iozqYwXJrTKKcXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=OZQm2w5hxhIsKAPCXSlTZklR9s2lW051IomM416SYdJ3BpUfdYJfMxl0ucxY8evyDttRXf8Xmk5iF5wQhBN3RHYZDr4_HbTc4ER55635WhHf3nCHIdUM2f-15jmyBXD8GL5gScP7ZmBuDEFyGUpc24TrzU1NfKeCknW1iCQv7upOFi1t-gl7xIUa782JLCUzIEiLgJlTCTsB3v4nAC4tcKNuPsdS1OX0LtFbXuj1grlUnqC0VVtJZndsN2XN2JIaG3g7R12XGiFLhvq_AuAeAgwegxdeQW6njPPi18l7DPMCcz-sPN3l71Cmf0Eh2Bu3-Zd2Xu4iozqYwXJrTKKcXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
محمد صلاح فوق ستاره 34 ساله مصر در پایان دیدار با آرژانتین از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/25202" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkRp-w2GEAyJewoxVMBuxbkGP3174UqiecC7iYewPbp_dpIMxk3J9Nr5sGrXEnF-_ZZepy-yP5um0Y0qY08JxNlu3lTp-QCfTIBXah2V3u-SB01AtkpaTKtL_7WLnfwAWk9hBwnue6CWzEUVYGfSc_Fr_s0Lv_U6rP2ApI-yZ2v_DfLzfwx9h4ZrujzRD30YVt88LZndHRBzzMxheSpVh1cQQAYiEZoNUlZ3G14yWNH--p5Er_YU9uGdA4fgUHthc4SHch1KUxpecGc8enfsiwyLrC2whjKmgkDPTSDvPX_LDl1BFeY5M8ezNCQ31_9pxhp6MoZkqSQfcYFa3Q6PGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل ساعاتی پیش قرار داد کارلو آنجلوتی سرمریی ایتالیایی و کهنه کار خود را تا پایان جام جهانی 2030 رسما تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25201" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4Lybs4UcexUqdhiSYofPvrhJNXvlrWZBzKOsmQPD40VQExW8eAjYSBmlWpx-TS0L6-Brow4JfkBxN8c5TpF4XsikaPZptXwGM9EQ6LigTfH4nYPH-WID75-oaEQkHoB6H78cQTfYfqyijLRcm0g3YymubfStFkWurVReGvBZymuYOEhnH8mP9LmEaHnDi4xVNfFmmceUFuNddM-A6MZIR5TEECPP89NwxEdQzondCTypGnly3hBCTto9DyFg08tO58LNd1q2WOz--G4VsCJ47XbNTDzX4BtO6ehxFGnCvEGrc94sDHHw_53snqdG26Qvy_Asv3CrJh-SHgawBfRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25200" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amn9swNkeIxFJ-XE8JWoY91A_m9WwFo5GL2QD38-D4x8Q_7kPKVNPV_p9IOF9BqpswEWjzihHROG6cO3Yv3PfPx82RxgdK8gkNkUXE6PDwwhxZkg-RL2qqlK53FAP5Tcg6jfthHLZTTwZApNGpMp-NLDerKVr0kUZZsc_3f-uvwVSL2GhjcczK_ilDSncI23kSrRgJMjOFuiZssPOgQZADwoZn6Tax5Tyaa4TcXE0N37MzBVOOnjKkZd1_ayileXNfbUSTnnQ9o2_I0KP82bOJCYEzI9an24PBUYJj5s1hEodZB7yLApXqP7aH5gsqV0T4nHFxiXIQlXLv6Z3SGW8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛سیدابوالفضل‌جلالی شب گذشته به صالح حردانی گفته‌بود وقتی‌باشگاه هیچ تماسی برای تمدید قرار داد من نگرفته و کادر فنی هم هیچ تمایلی برای موندن من در استقلال نداره باشگاه پرسپولیس بشدت تمایل به جذب من دارند و فردا ظهرم قرارداد 2+1 ساله‌ام رو با این باشگاه…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25199" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=rxpMbcNTv6NjYkG7CYNnvRf1p-4jK6l1Y93NQJmeEmSae59o8zkp3ffqaAEkCLfRKVNoT0J9bWALE2f4TKV8G4a1yCVBVu05m1HU9qow3375Q34kNBPJBuGk2_wT-TupSpjkoLtCcqtIfCVeA5__sboLAO0WOMn-UWxod-SVOA-B3Sy9hcLYnTMZcyGGlw5yhaEKVchLpuiH0eDIjLqvRA61Ei3B09KlIsulDMhncw6KzwQCWhoOCb5EmCR7SvFJmll06W4FuhR3MI-3IBSVMOa7JnebSXNtowWvKEQ0T8QM30Vwtx87fuvfwqQ1d7xJTaAG-rFBSDQwq-RXrhF9wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=rxpMbcNTv6NjYkG7CYNnvRf1p-4jK6l1Y93NQJmeEmSae59o8zkp3ffqaAEkCLfRKVNoT0J9bWALE2f4TKV8G4a1yCVBVu05m1HU9qow3375Q34kNBPJBuGk2_wT-TupSpjkoLtCcqtIfCVeA5__sboLAO0WOMn-UWxod-SVOA-B3Sy9hcLYnTMZcyGGlw5yhaEKVchLpuiH0eDIjLqvRA61Ei3B09KlIsulDMhncw6KzwQCWhoOCb5EmCR7SvFJmll06W4FuhR3MI-3IBSVMOa7JnebSXNtowWvKEQ0T8QM30Vwtx87fuvfwqQ1d7xJTaAG-rFBSDQwq-RXrhF9wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25197" target="_blank">📅 12:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=beNxMv1yMX2lV3mqogEKVBrLrfZpaIbc1VrDF2lXdiH_Mhl9Yr5sn3iThEqBFtXNjOrkyGERiGOV6jZ1z-cWCiaVax2YL9l9TnnWJl9brK7J_uIseFtNkKOlN0Hm3NKrKceIqXHfw3shIVhLLU8h8zLOfp_yxEhgRoPluBxRrczHjx_cfSovM-Iqf4vgfPoeN6DjDAdSgPF25jtTqwK-inQhCFzusXZI0Gvt7Z-DNAyVcUl58V1N8GJzgXnOW4IShIX-2rCZkH0no0dvxBzVjmLHZsSZhbsgJPNIaslOYZmjTLzuG_f0altF4talpSTd70vLQPV-a1pLgIRHGsrLYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=beNxMv1yMX2lV3mqogEKVBrLrfZpaIbc1VrDF2lXdiH_Mhl9Yr5sn3iThEqBFtXNjOrkyGERiGOV6jZ1z-cWCiaVax2YL9l9TnnWJl9brK7J_uIseFtNkKOlN0Hm3NKrKceIqXHfw3shIVhLLU8h8zLOfp_yxEhgRoPluBxRrczHjx_cfSovM-Iqf4vgfPoeN6DjDAdSgPF25jtTqwK-inQhCFzusXZI0Gvt7Z-DNAyVcUl58V1N8GJzgXnOW4IShIX-2rCZkH0no0dvxBzVjmLHZsSZhbsgJPNIaslOYZmjTLzuG_f0altF4talpSTd70vLQPV-a1pLgIRHGsrLYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای آلن شیرر:
یا هر دو این‌صحنه‌ها خطان یا هیچکدوم خطانیستن، نمیشه برای یک صحنه مشابه دوتصمیم‌متفاوت‌گرفت. مارک کلاتنبرگ هم گفته هر دو صحنه خطا بود و پنالتی رو صلاح گم شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25196" target="_blank">📅 12:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VE-_vZD3wjypP8Ikn7KK0FezrCnC8hH0zT7OKyJtg6UjrzJgyzaXzlDVlnhfLWmtBZLZkV_IX9rxa_oeXZiaFWBMdG71zMOWK_u1gcey2gaGshLRVCXJfUHK8C98Ou3KbQdyp2DGrE0ur4J5Lry5Wonowue95duzed4Mm0o6MmwMfHwDmYgJQg4_AYbZGRWa1M1LvnTBbHkkZ9ls2EBqW6nZrxA1VKfYZ5cMbkX9C0oVbnr7XvFOZpg-FwG0DxmH7qlaDx-IROcmAMqjs3yUeHJmcsWLnK72roE_FyQRq00rxyBTtWLoeBrQzY3QD04jk3Fr8P0MFtBY3PehYHW9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25195" target="_blank">📅 12:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgH-BErBTCZULiM3HVhfkEWXleXNVkshuI9mWnY14wE41Gr31_9t2AovoLtsEoQ8gpTzzNKXO8Fh55EfTtLmFxOJHW3EFM1GfG8ft7cDqrO9hn4j7vke03_2xdtQdsOXMTyWFdaGuGmPxXyXctI6tnuYq2ONiAS1RPMxa43kj2_a6XkpQel4Uf34IUcI-avYbg3Ma3MhsOniWXCsVW_CtZHfRYb-lQbQ54RqbVxDZkh1LCLcp_D2Vot00ln4Uzy80V5-k56xeZojybVH9kKrPxRB7QWAZLOd4m-A8z_SJ2NAP10jjlQDmqMMLQQjLfCcovFYLqsgvXuY3fynKaV3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛ ترامپ:
دیگر باایران توافق نمیکنیم، آنها فرصت خوبی داشتند ولی آن را هدر دادند. آتش بس بین ایران‌وآمریکا تموم و داستان به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25194" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICLbRiGnMeNNaQhBqiDhLw9-MxS_Pb2lOWK_q1xZEg_HgHXejFTqpMAUahq0XKZDVM6Pni52fJrMh4xRy-I7hr2qg6DnNO_lgqcSsqzXPrzkcjQxntRss5XyAOHIGk_xtUHMOAA_ukJC2b8NLLGsufac26hYx3wltmK7C58_0L5LuU5g-jwWUjKRSUw_EkW0WDiUSOnDfBvPFENeH3hYeYwbldmMDjM1Dffg4FuOpBymIptlSd5E4IakVdSlC6XKehWaPWXxCt0seXOgQxe75dBL8I5-4k5QLDfXS3kbrlRk0oKvz-O5uAZaBgbHV21cLZkBAL5TTXxnEbE8un3G7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25193" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bG5H2rIa2UTSg6LYE4BokeVHf7C-e7XI9r6bwq9IDVhh0479jC5en73eSJvtn-5GOdZFaSN6366mOZcVIxsJxxllhxl_fMP604hDir1cJzC4wtbHKSlurDLA2yXBzDpYr1fDH-aHxCdysDbtUgChGkMMYdbd7j9kqzA4_8QlKHcmVt3QUJjNRsYXO2SkdGPRjPuw1SVgtGCT-B3y2RqRMOD6L0e6zna5NVTNazPxa5QyWP40_oCJnSzz6AQs-psG4XeXeMhedjIFPOqolYDz3yrbqUIKgSJ-dKxxhmZsnED3R5qX3cIlpHp7zZfdRpiUjzwkBPA2syv4rbhnlAx5yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
#تکمیلی؛نشریه‌گاتزتا:سران‌باشگاه آث میلان به دنبال جذب فران گارسیا مدافع چپ رئال مادریدند که در لیست مازاد ژوزه مورینیو قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25192" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Djbdj8iPmx2RY0y1X87l_6MhmOPp_yvPFgFJRww9CaXpUuS6YPm5932TfpcrLVG3_We40EOJwjETGicgOYuzbN0HwHAfZ8Cdx6keJDJS-n3SzU-9oBgy9UOECuU3PXnXtebKQeQtvjF3bWn2tb0T6nYHxlM8AIGayWGvGK0AX3tRwU3YfIIUCwKI8hbn314yEhSf7aPHC3vGYEGFfSE4DYHc-mjw2w7dFlrzSBWxUkHsZbtOGXj0veiXo4Uw0RR-qeDn_S8P4talIPlumw8ScnxwSHd0mgZ9xrMXry8Ihu5K3VUlEbg9mfLoZ5L7CtjUYhqxMtiNFTRxbcuacnogAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25190" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcoQR6cJcWsFDdTTelOnq5_xpwb2qo3Ap1UI7Z3lSbv2Wz1UNYrYOedMpT5q7r2FRmHIcq-kwEswYFZwKUAHanuKnrLU9vSYQ2m9cONUnq1_2qOWUbz7_cL8bE81j1XOfeVq7P9NJuze7Qr-nYn9N_-YjrOJ1WqnLwp5fv1dexxBInwAl_AeWs8A0U0IHRb-fXxQCS0Ut9a9xCY3fwmvzAwQO4mCwbgI1xlySbztQ42CtAMK-NerL06mehDzMbA3qD1MyB01dDg7Hi2RXj4MmIqHKsqjbzm7vtm4NjAc7MUBdsObUkfV5Y0aG19d-z6VIvlsNkn-f8lV5LKiarbeYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25189" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKINLgLwdRRDB2eerPEvvGpUY5EM6bsxR5wFKCXtiZgkPDVIAeP1Lek4MNq1ND02pnV1BOTGZGCOox37dD1lrqJaS8LYhuVByxrEkEPtfvp7YIsJmaMEN9YkUfcCRgtiFwhu5i1zbnvgs-2HS9r3OSTEJi6qUrdg-4B8EY7uqcH_05g-0-uuW6ReIJqp9edN2LWLvuxzPpajk7TNWPPrbXxLI00i2-WBtx1uZJmrqnwVOnvCrwk58YK_axJXECGuGRS7M0C4gjUrnP2Rzxl1PjM0ZC53Clwtufmlg-LXWv_aFUdvhPCpEAKI1-Jq0soiykwtj_JRJ7lGsYH2m2b1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مونیر الحدادی ستاره مراکشی استقلال که قرار بود اواخرهفته‌پیش‌به‌تهران برگردد بدلیل شرایط بارداری خانومش و هماهنگی با مدیریت باشگاه استقلال روز دوشنبه هفته‌اینده همراه با همسرش به ایران می‌آید. منیر الحدادی دو فصل دیگر…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25188" target="_blank">📅 10:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTgPc5hsY20pGe3aqKdAgghLefyr0iRfzxLqnjbp_vfJVahrRHzgaINrja3AuUKtQefZ0uhSWwFkwjECBXLKAWZ6cVB_zV6w9AOK3sv_Ks8Y2Zlwwj2y9rPM5gg5-Gj8OEfkVgKV1N7tC4OMayz-f7Q1Tgp1NjqS_F4A2bOqZq8bkxuVtdvE4-Ygbma6rGjbU8FI2-d76D3lbjtk4pQAh2ikruetx3DWs4DtGh2RrNuN15MssgNT-efc76sqMPi26Du_nXzCDETtMZGjtpLvZado5PSTUFGHt7hNo-T5JnKQXwJSwkufw-67SKFsghMOCGaqvU_wWVLsbSYEEG61Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25187" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=Ob_RYGGeFdg6kZGcuRzD_08yGK4QfS9Kyo4-z5mgyuYWalUshCEUZ1YqXHvNanLiC1NyptYUGq1iGPsx23T2eJSmGy5C1yQWo61m_1vT4TO3QPIo2aXu5pl-ljodjxxFRTFG4Wau_1SlybmAFlucd-gCG1vQOkjFWz_nLYYCB3PmePwoxeQCN2SBoer2cxNw38Rqg3ZTbLMUBRpzUI-EGkYFn68YqDQWaN45QwdYRBXwowWjPsAOZWEM19JoqzlGN72cCiG8CfMPayX2OAZZqMbCkyQ6dZpx3pnzqatXvzsYhdiPh2mLGcnfLhPJ8qZzJgQCO9ZWBANq8JFH7hERmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=Ob_RYGGeFdg6kZGcuRzD_08yGK4QfS9Kyo4-z5mgyuYWalUshCEUZ1YqXHvNanLiC1NyptYUGq1iGPsx23T2eJSmGy5C1yQWo61m_1vT4TO3QPIo2aXu5pl-ljodjxxFRTFG4Wau_1SlybmAFlucd-gCG1vQOkjFWz_nLYYCB3PmePwoxeQCN2SBoer2cxNw38Rqg3ZTbLMUBRpzUI-EGkYFn68YqDQWaN45QwdYRBXwowWjPsAOZWEM19JoqzlGN72cCiG8CfMPayX2OAZZqMbCkyQ6dZpx3pnzqatXvzsYhdiPh2mLGcnfLhPJ8qZzJgQCO9ZWBANq8JFH7hERmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی‌از دیدارجذاب بامداد امروز دو تیم ملی کلمبیا
🆚
سوئیس در یک هشتم نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25186" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=sAZasGvHzARdbaZAEeMEEwZ89-a1ynWLtTx-VDnOJH8fYRaqxZCSisTPTwxPDzPzwcw87kKbU7rpDv87FFbf3m9lmyfEFEOxVSR3QwKT0TsyH2IZMAzULDv4nuJaRkluBr_Z9i2WUysuHFpwyAEeP0k8SsB9-g3QvGoXN5yRGhkkboN3kmy7-fuxOhuPAe_eQAFZNl4ZN6RH-t0fsd-agPc0wlniCrPEFllXgxjnRPerx8YMIIUv78pfjVJDrFd3UK-siDw94C86AEksikWHxsFf5vFMlkQOaK98nUFzP0exXsrKTGexGy0ky48zIZEtfqIkNNckPi1lUKlwJGSuLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=sAZasGvHzARdbaZAEeMEEwZ89-a1ynWLtTx-VDnOJH8fYRaqxZCSisTPTwxPDzPzwcw87kKbU7rpDv87FFbf3m9lmyfEFEOxVSR3QwKT0TsyH2IZMAzULDv4nuJaRkluBr_Z9i2WUysuHFpwyAEeP0k8SsB9-g3QvGoXN5yRGhkkboN3kmy7-fuxOhuPAe_eQAFZNl4ZN6RH-t0fsd-agPc0wlniCrPEFllXgxjnRPerx8YMIIUv78pfjVJDrFd3UK-siDw94C86AEksikWHxsFf5vFMlkQOaK98nUFzP0exXsrKTGexGy0ky48zIZEtfqIkNNckPi1lUKlwJGSuLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی از خلاصه بازی فوق العاده جذاب شب گذشته دو تیم آرژانتین
🆚
مصر در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25185" target="_blank">📅 07:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7V00LJfYcP4W34ckCvpOR7DvzZq5lkGmzvX2N2L2IhiDx2qJP5tdzXKYSMFuSMke23tR1YLzfdZCSz6OY0IE-hRC0dQ7u0sLKw7pGc4kiPAcOHlEMZTGm1qwhne9Wo8ryYT-wuzEJMXHnQbVdA3WM391fE0E8rycfEI39uyY5isF1uRUhPkkKIojTLeqk9a3na2ZSvH1WwY6765MlYqrSQ3eOxaWSCEoviFo1XXfREb0sE6Kdz2oGzZ7Iqb_uCfGilR31OO2IW967SoSEJPkIEOjRxY_CrhlJ_hSXhxWYaXKNagf7ms2PyrsDnq5uA_5mCFn2vCtNTmB7CaQCoknQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25184" target="_blank">📅 07:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25183">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaS4zQOKp0jt8uvE7v4NTUkki5FN5w3tv4E3RoF8OKTUUXnjJVZZL2ovlAg3FGQA1KSk-_avsYH_NVx__FTE2aUWhqp6phEwGhQ-Wgy-jP0N3Hz3DHuu-FCS1CXLGC8E9A7I71yqhEPxPbVOX2JBv8PWvafMNQFQzXUIfpn8RfewuL6EaPYn3sLtT1Ji5U3qWJqz7vHl3aYXK2X_jLgSabufR_jjyI7RIYI6Ntg87BbFBRqV_2wKzZFLSjbIDBlqe1HspuusmL_KXjnWRElyph6XU2a39tuv-gSz0rcXI5dDxUPnvmG3bZJQEiIX52wiSBBfzbsC4oKg-xnrNAqTpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛
از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25183" target="_blank">📅 02:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a56858395.mp4?token=TkYchU3QzVge99B8wo4OX3xXJYr0Z7UR_Lfm3xb811i8BSoY1padsQnnG5H4IAXhhhjTWUfgSkmTO1jmBztPTu5V05IppNTeSgNBWpXy5khSvKAUTR-JJOiovhGMY5nnaRVkFVpDBqx0e1u2gjMtxI32IZ2WOCdLTRDo_JGn42fNFQ2HPXTJ2HTP7Zgxtr_gaOc5-7SaoTxcH0cWrW4PuvRGEcCwuBjHxFC1R3FdWcjd7iBl-olh2SivcK-tE_1-Su8FK0JMuMDl8mKkuaorH6ImtHiSddGWztusFASxo4cfOylDAAvHXg_c3x8N49w9VYrfu0xSYvCrJuDW1Crjug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a56858395.mp4?token=TkYchU3QzVge99B8wo4OX3xXJYr0Z7UR_Lfm3xb811i8BSoY1padsQnnG5H4IAXhhhjTWUfgSkmTO1jmBztPTu5V05IppNTeSgNBWpXy5khSvKAUTR-JJOiovhGMY5nnaRVkFVpDBqx0e1u2gjMtxI32IZ2WOCdLTRDo_JGn42fNFQ2HPXTJ2HTP7Zgxtr_gaOc5-7SaoTxcH0cWrW4PuvRGEcCwuBjHxFC1R3FdWcjd7iBl-olh2SivcK-tE_1-Su8FK0JMuMDl8mKkuaorH6ImtHiSddGWztusFASxo4cfOylDAAvHXg_c3x8N49w9VYrfu0xSYvCrJuDW1Crjug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دو ویدیو متفاوت و تامل برانگیز از کریستیانو رونالدو
🆚
لیونل مسی در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25182" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QF1WAoMMM3g_CpkRS-mT56YuuHNvobPm6jyVMcqz0_ZtdJMqPoxqWDkPsz6Umtv8k5pLtji5dGtpHTFTTGR78XT5wR1wBEHgQVr4vSJp41a6xq2oiKEWwIP4J_lSl6maUJyWkBiMJYEr_X_dAVDzsu01Ohj89KAv9CL01H6eMQlYMuSAs9T2ItsN6mhMOF8nfzJGr4JWu8LXewpooUBsOAf1LD-2JzGUEVrSTC_Um9c-luqZ0V_O2tM6G2eizTWyfBPhVAyRzCjKPh1SmvHd4fcMqJoNBQrQgQMUcScOkyc1WZWXxjVzCCi79H-zji2iHdDLgr0cJjxIwlaD9n3COQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25181" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnVNYFM3AbW5hfWG7ziF8RbQNytz2dCxNqmMBn3c45ux--WEbI-fC4M-5cJS7Zhmb2ywsT9XAeTDtDLtcgQUK5UWwMcR7SSY7ZSGV0zPpWu_q58QzeG2cU-aOlBKUssXKodfahT9PtnI-XfhVrpsVLX6Aw5_u_gFPom71ClgvSP1MHcINFiXceqMQjBfhWy9Y0481_O-X0nxxYgZcZAdsWlCZzEXcM-HZ8tLGS_pfdJvrc1CStiXzYZ4v8_fSRqQ5aLtBzOSjuhPtklqjpKr0SxgjbF68ZwFhqPWEsChlhng5wm6hDg2GLR4MtvFyIrpssoW2e3KaI_hP6YvViBrtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25180" target="_blank">📅 00:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgEn2pwp4Eui3YgNh7LcUajH1iXUh_jDtyygU8Ez8L2fgkLQT9ZexqUeGGQicfOmt7uDKKb4UVv32crEKIq1zEncPJtlMe6wqle_waJRVim3QBzfU94-S3sDX8TWjyB7BZI3e_EWXikeDN5rLws5b9A7Jl3yRIiLHAbcmpkJmC3do00ZK5osnQme3lCJ9dQy5Zh7r_mdV3MEAWD1WfCiNw8L3i8lmahOyzEy_oJNz9R2VnQ1HqDmhTlTlZnccxsWN9LgVgoIeoW1JGIeYzuKBfdfeL0ysDxb4czjZDbYmRBbzgjnELBQ3RetH4tw934CZDd4dwi_m3zl0sVadcQcZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای باور نکردنی باشگاه پرسپولیس: دراگان اسکوچیچ برای یک‌فصل سه میلیون دلار میخواست. حالا این رو داشته باشید بزودی اومد ایران رقمش با سند منتشر میکنیم اگه بیشتر از 1.2 میلیون دلار بود کانال رو پاک میکنیم. فعلا دارن باهم مذاکره میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25179" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmMBydHPiem9_Dpzwl2Oc5RxoPcthYi7HXWpnBvERa0aMcx5J1ya-tDPJ1NTpyh8hgmsBosADb6-BoqGPXUSUuGmD_Ua8NishefKCCedXC1vFqaTXzi2kvdGx1DmRgFypxYafnN3dLtS1sx0yYtFkqmlXFp6zjB7nGYisKuE3y9k-7yjZyQe9fq15vdIjj_C7kYxDL6Jw25d4zIEFr1OTApvXxm4J_-Li_uOoKu6CKLxHjRSnmugunrzEh3w1SaV15m0gvLVTmtUziOkXXGXh_0edpiWaSXceXz4mOUkZzGDc8-SdqHOLAbwyUBVIR63aiKGtnq6KpZBqwZcWB0Fcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25178" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpTeNSn2osSs8Q-KsDsTy6geFkqJ503UFomsMmRkz7DA1qc4wOyIGlHIngO45LNtMFXKjY9Aw_hdhOXeUy-BVsO0aqPsWYzZbTuM_Rv7yGYP9dxHjj3G-1FfVDE_9v9U_ZDuCU1-yZZuHAWf0NVyOT0GioYgSjRwS9so_G0CbvN6J6q6NPusOikk8ZxAEneBr-8q83w1WweopWILevdnVqroY9hbmDd8LAv_QAJZUvLyaCjy8oOPgvCj1wW8H-pKR8ggoWQSKsH5VXNafIMYJG6SWKy0aN_F8BDqrfUQSOE_z7Gr-VUv3Um0-B6dbvfl7J34XBxHJVfBZxncj3ePIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25176" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25175">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7JMsBq0h3nduRRNI4UFppL9rNBObk4opK1DqyXLwcBDgHXkqwtDYqSqvIg0_i6bwJpAxYtQQ9axr6izdUanonmaBrVm6FnXA0PQgTg05WrP8USObIQ0Duo_VeDKfef-7TeZsXnDfWgqnkV5hchzz32tM_1eKXlD2XIPUAaVddVAm88s2xXicWIElQuvh6CuGtOJ2O0SmiGny-0q_RgdngCOM4SPdUs_cuXKSXOyHauivm5NTrjamtLCWgZ2yQj68IE7CXQHml0Bnipb6pjIVh29o4PDS5c-B9mmqIu3vD94Dv_sd6hQ7CV2aspvt9GDhaOLEU7U0hApr34Hmi0K2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25175" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_v-spafMvfFsfbKuBYakhEk9dTkL75SkuMRiBS-bn5nQEwhruDr0PfKvQFViLxk0IYUxMGXqbfwCA0vQ1oxwcBnEbmiLdQNpAwwwdX4OcCsdxy1zJX6jH9gJ20CjyXA3oBMn7FZABZSq2WseN0tOYv7JGb75QospIZfT86ADS_PflCAjbjxJUR2A4FMP2SLHZd60poKzM-2Ga5w0QBjdwYbEpAk03mBsAAW2gxTw3QCPuv3_0rBcWQcI8suW68yBJy8J_tU84mK0dJmvKDUv-svP3OzcXzSaL4NKPAhVYXchlJEc0s797DH64gbUCuagi8WUBLQe2z_yrlJ5xJanQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25174" target="_blank">📅 23:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25173">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfVkIG8439ALj2v77pRAl0DMfQhLnxHGfxXulllluVZQko547-DrBvLAcpDKa-O_R6z4eq9ChAiUB0P1QJ4fDeMqTjcz0qUiuaCkKUYKFPkQVv4lcAklcjaWsq22H8w1YC_w7_Ym_vNENFirvCB6E0GFNTq7nrKBxDFEH4ysAomOa9UD1ZFOYr-xCFboTyOJWzVsZcwpKqyJr2Wh2bVZXjGamMiC-vXjPUUTp2tPhtBKxaF8k__MOwmjhwSXT-tZERnshIIPs-LwIEf45rmtDX4lxh-3VOYdVqIAk5dTQm8R2jv4Zlv_0wrrMHEry8c9ZnhourhtzCX0JJZLVf9pOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25173" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25172">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEc5jATwCW6vSG_M7xVZbV5fBTb-k-ZWt0stc13CqZNrbemnWses4QP68zU6_xk8EV6Rxyfy3nHhtrvnLzk090Ce7mjmtlgaOsC0GpNl26dW9amSgIrnhcFeYJe2vSyO09ZLuS4iCZWA7wjEFhNbMcE2h8u1h3vQOq3LusU7uK1rvAIHhBdclNnA1es7mszcMaq7MnM2_U0gbkMnvEiv3xF1TWMceEJYqhF0epwamHexDYJ9MxJic5S9Hn3dpH8zkeR0G4piP2p1k3LVmZjoPIUdHKZMNPz88D77IyyrPgkCI1CL1Q3QjAHGaK-oE9HvoA8wqD3LemuroZba3iT8Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25172" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25171">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25171" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbr_5CXyyyUuv3GhociKxmNy6O_RCvxwEVknGRJlfrllJltu-rTxozn-uMWj_hphg_2Fhd0JvKW96Z-LpKm0Y9oMNDkB4KsjjJjixwtvMi1xY0UiTiRkm8rYw3GqhYaDL9pn1OvqGZg48L0pRHBFYhNl4I2IzCCctNrRYFcSkonp_1Kjh34Rk1vLhtZatm1ZkLiz5y4x--guLG3JrTkplPq3k0S-2ieTNYl6o80U7nEpu4vOsxw5wNzpkLiqnFiIDbOs-9rIZD220BuLMQ6WLAP57gyMbcAGQ68d8Byv9BShblBvVeyi7LNsuAGnhm2QpYu8Il-qEP-EnGAvR6H4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ لیونل مسی که نیمه اول یک پنالتی خراب کرده بود در دقیقه 80 با یک سانتر دیدنی برای رومرو گل اول آرژانتین رو وارد دروازه مصر کرد. این دهمین پاس گل لئو مسی در تاریخ جام جهانی بود. لیونل مسی در دقیقه 83 گل دوم آرژانتین رو به ثمر رساند و بازی دو بر دو…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25170" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCpEqQkbJEVWuQgz4WV1hgDeBguGDNOe6-L51tHnZIn5Z1Ze1lUoWIy9Uky8cndeABHS_EEvx0btJRv0e10dSGASU2N1BIoXErztj_giSXk3EUGjhs2z6Isd4B_-HNZvUk31NCzW6QwiLTHZYegZyQcwFluy14jCaZTmh9T0vAGJcQwfKnrRemll9a9u5zDSARm1F0RtStQp9yZnADjrVSTz6g4rkPkHl8wM1RBKNCQhrg9yPsuzlS_XhM_7f54BX_4o7_X0FXkAuRggSpzpsKowHY2GNXfVPVc-6Y8W44YOvZH0ym8omZhcatnDjWa9ihyVP8j0jbS3eA5f5TJTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
با پاس گلی که در بازی مقابل کیپ ورد داد؛ حالا لیونل مسی با 9 پاس گل عنوان بهترین پاسور تاریخ رقابت‌های جام جهانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25169" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijz9uI_xX60wuNAqZIY8i443JnbOCxAl4Z5Kqqa13PbplYJwD4w2GSqYVpD2AxMAsEP00z7sSSIN7RAi6J6oQ9mjMx5xCUP8G7yq5lKjtu90b0saX0R28r97Kx47ErQNbniNKS7FEyNimnU-4cpEnBuFGE73bAbZdkmZi01ET8eay-s1Kt34ludIn4jKUuwcp6CL6kqJk6alUY6p4Y0hSRa9su9w9hqAmLAkgJllBz9NcJD7zjTUyVEAo0u1403pa-u2e-Gus3wa15EUC54tpbKuFc9jE46JoGVUKeMYNr37MmG199nmUPGQX_9s9OILQJTwkPqi-zNSe22CeEpemg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25168" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSQ3UIb_0rtGQ_ZbIxa_O52GPJaqzjPJKNFi8vi0Gbc0MrxL5DoIKVU90ZT6C0g6L1F4-giejHk-GC9I8ztCt4xaoMnZ112G-eVAQJhPpdI7OsoJtzcl3cpWH-csF-zlP3n-3XQTxCKFcysH-tAt0CXEwwrbk5pcHVr5-pTfIqQR2kRb7VyNyf9nNVD-wwIBMU8M-Vj55ujf7xlqrtsFufjdUsBPORCoqmJZDOVxbs15mZYTo0QtBXjn8hktrwSgKKBSO09i_FIvJKF9L1lYyrGq8nz9XEkS3i3bvHY1fPWodeSTEdtSQZR6-Y35PO6uP-rIxAFwcsnx0mgIo2jtRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی‌تیم استقلال: از لیگ‌ستاگان‌قطر دو پیشنهاد مالی بسیار بالا داشتم اما بخاطرعلاقه‌ام به‌استقلال و هواداران این تیم آن‌هارو رد کردم و فصل بعد نیز در استقلال خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25167" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0DoxFCfGjOnxLPiDcXsYH5-gx5Y7oi1uPHrN9o89l4OniwfAXrNruZ0yYCjoy7lRFT-SZhDnXah90AXXgngSa6ixU15e11wQWBXBYAGUhqUv0vSzaZIRDsPDWKE-5Vba25NzHaA2CC8dF1fOeL_FzumN09ISSRwWBeZESrNAGDHW9ahWE8gYzcCSDRCDAd7jvCmezh8xdwgsFokYQLyrtqiBUxNFpZ8JfyKRyuIqRT0dru-anYN9poa5dmsDuSyozFSzBnbpLgV1fk2Q2kB1T8ZAwmxeyyQmuBfWRkcwkmJEZu9mSOOHUtxvv7Mfvo6OS790GqVLujwJfLewJkXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیگرسریال‌تاریخی «یوسف پیامبر» درگذشت؛
حمیدرضا دشتی، بازیگر نقش «بینگی کاهن معبد» در سریال «یوسف پیامبر» بر اثر ایست قلبی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25166" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBxtpqStKDX489HPB4losxTap7hPSeGtplpTRS4xGwAsYp6Jt3DTCL9YpccD5M4D8uJlglmRzrSOU40lBgs-Cz5PUtyuHj5OHURmy7pRFnF7J5iemG5k9iFdN7-5ckNgdUsxodhKEeySbAvO4GTfz9_LjzykAqiiLVKIO3pXxEnDIRZmSV5s_ggDsNA8FXefuH3gMqXKQlS__IimHhxzwr6-scQYqJMmC__zLtuy4BY2XJ9odZ1ims-J2l1z3gxSNfsZ4Jzm1X6RxVMjqt4s3H7366yMA76iBkewJ_CyLnxSTGJD0qEH3nNU4wfBmdVc0nEEr-JrgOis2LF1qm3WOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25165" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=i-2_Acmx67A303wc1EzwGRGmngm2zKnKW2UbXiTmKu_pZUCZCfNkWVgyGuSljdWBcNpdQFOAOqUcIG9BuMKaPuqY5n4-FkoABKvwEdQlXiN1EILQ9GGMlxDOtEy2cVwubrHnMEBKQMuXjQU6uMmHi--1312quccgT1-5Dc8QZvZR14mrtWCRhpIgRurfoRNyhFNsGBCqi7ZehTHbVp-1AoN2YFPxtHkszssUBm2kk9LcoyKvy5dEn7yXZlVapmqb7WIATLvw8PleoU63MxnOmDA9srRAwzcZMm7KTtmYzjmcqn0htqJ6a23I8xP85fKczWeycD9Ebiixot0_N1CSpGPJfLh6UDk6ryJwCXwLe-lvTRFm3rXJeFgdh3YtUf0OiZwgAhlMRwRMHhgzgYnDKjjm2soslUfVXp9qTfSXWQi4JJHtggGU4mAxMqDIxL7LuJfDpF6KDt0IEvT0cDkz6btaw9tVfM0j1MXNJNmy6VhGFu_rM05aDN2v3nVfbb5SNWFUwoxmoLkH9UOVp5HnDS8-B4ftXtA6Hcqw8tyXl80msCORSkkouju6JES5JPOM8IkK0p08byzqGe9nT7HgMTsMThrLO1tc1lZ7sdaVck6Jl838h1PrB5AfwiksSAsBunmNE_9wcAOObUIanzh7nzgMZEaJVbw5xpaHBqEl5EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=i-2_Acmx67A303wc1EzwGRGmngm2zKnKW2UbXiTmKu_pZUCZCfNkWVgyGuSljdWBcNpdQFOAOqUcIG9BuMKaPuqY5n4-FkoABKvwEdQlXiN1EILQ9GGMlxDOtEy2cVwubrHnMEBKQMuXjQU6uMmHi--1312quccgT1-5Dc8QZvZR14mrtWCRhpIgRurfoRNyhFNsGBCqi7ZehTHbVp-1AoN2YFPxtHkszssUBm2kk9LcoyKvy5dEn7yXZlVapmqb7WIATLvw8PleoU63MxnOmDA9srRAwzcZMm7KTtmYzjmcqn0htqJ6a23I8xP85fKczWeycD9Ebiixot0_N1CSpGPJfLh6UDk6ryJwCXwLe-lvTRFm3rXJeFgdh3YtUf0OiZwgAhlMRwRMHhgzgYnDKjjm2soslUfVXp9qTfSXWQi4JJHtggGU4mAxMqDIxL7LuJfDpF6KDt0IEvT0cDkz6btaw9tVfM0j1MXNJNmy6VhGFu_rM05aDN2v3nVfbb5SNWFUwoxmoLkH9UOVp5HnDS8-B4ftXtA6Hcqw8tyXl80msCORSkkouju6JES5JPOM8IkK0p08byzqGe9nT7HgMTsMThrLO1tc1lZ7sdaVck6Jl838h1PrB5AfwiksSAsBunmNE_9wcAOObUIanzh7nzgMZEaJVbw5xpaHBqEl5EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25164" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeDoDd_mxkYZ5G0rEUaREstotpwFZtr1LHwFVCtC_2Hx9K2HoEOc1dB2LwHwIUGTbyj0dRmx7UNbqCs2kqx8eu7XLC7jILRnV_E1IVPss-Jvnls9RCOBcbiXMEppBngzLIDkhSjwm6wq5vPOf-ilY8zTp4AEKf_vtfXbvCsLITSv3HyOs5hK1x8As3KZ9R2FMT2YlXMKvlsa9Njy2B6IIgckNgX-VCx-HIyFaVTBscmeJgQHqKYNN20C4sevzu6xOjcqFf-dXBnzdlogeqc5kyZJLKUKU0UIbImyfQ9-C-MmeGb2RuLdPZhkUNpeQFPbTtGagtPmbE39aHBw25HQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25163" target="_blank">📅 19:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cihJ8PARH-DE-rgMJRz1ST3-T72_H-PvQHEZuyvgyzBOeCCWLuiPu1CwEBmeqQBhGPl1JLq1SB5LIBsCwt_T_1OygLUaAqwEub_bCOllnpa49xZBb7VoOU1DNkzpGT9Z7gYXr-49G_tmln0eVYCeQFCm3KDADYP1aZPFUfV08luGAzYzwP8EvLwWNChygqesUssa4yQEYdoEctDkFE-SJLfvoa4abbPzsL-F8iHUI6yrHBsRDmL7uIy-28pI30bXifaKm4HYqvB40L-YiMdqVeLyJZuMBvBvixT_hTv09wWFWgANkXusX_zNjRKwTuzHvg88anmgfmZA6Ch-ZHQ5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مدیرعامل‌‌تیم‌ نساجی: برای‌جذب دانیال ایری از سپاهان، استقلال و پرسپولیس آفر بدستمون‌ رسیده اماتا این لحظه باهیچ باشگاهی به توافق نرسیده‌ایم. رقم دقیق رضایت نامه دانیال ایری رو به باشگاه‌های خواهان این بازیکن گفته‌ایم و هر باشگاهی اون مبلغ رو پرداخت‌ کنه…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25162" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6nagtYE8JayECVC7ZfZe9vnDS9C9iWmWX3HDCg0cudvTH_wwbeVxjVKjRrh7PctPvfJwY_ixCmPqIez6pJP3-4osc_uNS0rwIEwXEy1fgBRosC2tYTTEOsLvRtsiZ_GxjzzRCBQNrQHFaJMk8WLdGCCmnaOdUJTTwrFn3rga9ra4UvLuVHK5h0tGpdE7Gn7BfZFwbk-Jl1kuRwLFjzxRS1MQHcpopthiKVl1Ai8DC68-d5b1HbmhBt3wRsk-cl6pd0e7Ycq_tG2lBTCge4BRqXDM7P2Dbuijt7HsjHm5L2_W6mDCEaUy2H-7NLVmSjPGLyy7d8vZoiK1k7pJZ-2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25161" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=tbPS-ZlhS8etBFWsUf5W7-gLTXcsBuWFABxULElinMd07QhkbUtXnLsjIU8KiowPzq20aOUUS7067vFzHf5kj1IxwMX0G6G_avQLZI79IowfzjfFRRLZYqsshCKciQQM8dSeD7A-mDIwaYMOFuBz7VKJgBV13aGf730GqIVgrrw9GOkhUKF9Xfw8SFjPIZilrxLa9P7e_6dRGmAwVUkHAR65Grkny9BsNS_jxbqDbyG-J2Lc8JWIQchv5PUF20ofI6OQWsIUCwe-qj5N4ga0CA7DuskQZEWkF4py-91bJSOjG3SFN5vaqu4rNIC_h1E9l2TppHlb8_SO8rLoqIZO8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=tbPS-ZlhS8etBFWsUf5W7-gLTXcsBuWFABxULElinMd07QhkbUtXnLsjIU8KiowPzq20aOUUS7067vFzHf5kj1IxwMX0G6G_avQLZI79IowfzjfFRRLZYqsshCKciQQM8dSeD7A-mDIwaYMOFuBz7VKJgBV13aGf730GqIVgrrw9GOkhUKF9Xfw8SFjPIZilrxLa9P7e_6dRGmAwVUkHAR65Grkny9BsNS_jxbqDbyG-J2Lc8JWIQchv5PUF20ofI6OQWsIUCwe-qj5N4ga0CA7DuskQZEWkF4py-91bJSOjG3SFN5vaqu4rNIC_h1E9l2TppHlb8_SO8rLoqIZO8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25160" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=iU54N4HI7i4tcYTMNAzvJrqGAHoddiQbW0bZTSdjNE3B_YBpskdELuO4a5lrEUDzjTC1alRMlWs_mhz409IXxnsVxxQAIDFPVbamZ02NMuHNhj6i64xQp3SD3WXn9WKlY3LN8XiKdmlN4USo_sswXFJs8PHg8EYV_j4070xzZHH2GYAKcu40vipWLjHbhrNAjF0jatR0377VLPdnxcrbYrpqGwC_bTZZupc3SP7wSsNPlB-SMgj9WvRRdl_Cg8MYtKuwLGsbcKdB1uMdFeBiX5aPl1U_AsKpGSc6qWYSH-KJfBnvUXuwAFzpFedAE5MApA3BCn9uemZq1CgLQdtEEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=iU54N4HI7i4tcYTMNAzvJrqGAHoddiQbW0bZTSdjNE3B_YBpskdELuO4a5lrEUDzjTC1alRMlWs_mhz409IXxnsVxxQAIDFPVbamZ02NMuHNhj6i64xQp3SD3WXn9WKlY3LN8XiKdmlN4USo_sswXFJs8PHg8EYV_j4070xzZHH2GYAKcu40vipWLjHbhrNAjF0jatR0377VLPdnxcrbYrpqGwC_bTZZupc3SP7wSsNPlB-SMgj9WvRRdl_Cg8MYtKuwLGsbcKdB1uMdFeBiX5aPl1U_AsKpGSc6qWYSH-KJfBnvUXuwAFzpFedAE5MApA3BCn9uemZq1CgLQdtEEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25159" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
