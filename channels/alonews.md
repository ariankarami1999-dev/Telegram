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
<img src="https://cdn4.telesco.pe/file/U7qvtq72NWbF3y0_-ZK86TGkaJa0r0jGvHfUpRDvlKwJ_7PCf6nBuwVaOkyDPOl77B7Xdvror99B8W0BummUJVxpgwKMoMzZt5g7Y3zHf_MspIdZXxnM7iqXbCyZ01D8jRHjOVpdj29mSQHn5h9UNYEXzWuKd485g5F4ZQCOXtCTVjBrznmJ0ciJcCiT36aSpE3QYEFTGZsBnnkvPaPr6_JtCDptZZGZBJzHzIVihMAluzuIuPd6XDhI5gYC6y23C5t1bU077zL1CYstXH_T0eBiEKNjxw695y6CC4IDBSs9dp0vPkzIVzPLf3WoiO4soPEFN057piWRWF4gQZftmA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 959K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 11:47:27</div>
<hr>

<div class="tg-post" id="msg-129311">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFSmpW3dAp3Y_R4TA3S_DJ36O4D29Q2wr4cbidNgtTYsusroXweE3EMFOnsjdMhlqBJ96aFBlkBVYkTQXevst9phycJKqFCIyYtxwnH-yDJg9IGMlzrWJjGpDdGNg1o5-OSUfa316N-PYqiWanWmNvSW90mdAadSES18oaegeJZITLc0AW8au3KLzJAqwsoppDT6Erjl2IoRndBWT4hO2wXV4l41T3V7okFpLDL8uVE11aPCmvuzlBZueN9MtfeiSXaspdmX6-3uQW7eGdf0SId-fkEHoYKld_2MEEe--G5Ta1_aT4e9JfJ0JxRvInv_eDQtEQ6QSIABDwN6qZsE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با افزایش ۱۸ برابری حجم آب دریاچه ارومیه، آرتمیا دوباره شکوفا شده و فلامینگوها بار دیگر به این زیست‌بوم بازگشته‌اند
🔴
پیش‌بینی می‌شود امسال بیش از ۶ هزار فلامینگو در دریاچه ارومیه و تالاب‌های اطراف آن فرود بیایند؛ برخی از آنها حتی آشیانه‌سازی و جوجه‌آوری را آغاز کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/alonews/129311" target="_blank">📅 11:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129310">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7sp73zrJQijTFSrHng368fsGRKD8K_Jho__IGTJkELCbv9uVg4XkEda3fpazJKZ2-6DPYnaI0WqrVaucmqCTGABRH5rExjkOLTFLn3lJFJYACOXDcpYCh8YnxIAycnFLjEmaEk0paRXCMzSkE1IniPmZlbXQq4ajQMJiuNy_Sr0_vT_GB3lslxqeXXKSpAMQcIARsKaZPiePffZADwhI0mkkDswC0PsbDMAaDzF-ZorA1xM2JCY_qIl8sML627y0loK-3QtQ8Yep3CrkhQLo70peHY0d36v9_0ulCnjB9VorSb2m82fdOv_KOxZkUM45gCpiYrsXQcX9nkVIzzylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم:
قدرت داره از غرب به شرق منتقل میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/129310" target="_blank">📅 11:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129309">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
جک کین، مقام سابق نظامی آمریکا:
احتمالا در نهایت با ایران به توافقی دست پیدا نخواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/129309" target="_blank">📅 11:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129308">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">محرم امسال یه فرق بزرگ داره
امسال حدود ۴۰هزار زینب داریم که داغدار قتل عزیزش است
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/129308" target="_blank">📅 11:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129307">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
دولت عراق به‌طور رسمی مجوز فعالیت استارلینک را صادر کرد تا سرویس اینترنت ماهواره‌ای اسپیس‌ایکس بتواند خدمات خود را در این کشور ارائه دهد
🔴
مقام‌های عراقی این تصمیم را گامی مهم برای توسعه زیرساخت دیجیتال، گسترش اینترنت پرسرعت و پوشش مناطق محروم و دورافتاده عنوان کرده‌اند؛ مناطقی که هنوز دسترسی مناسبی به شبکه‌های ثابت و فیبر نوری ندارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/129307" target="_blank">📅 11:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129305">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نتانیاهو: ما در حال محکم‌تر کردن در دست گرفتن حماس در غزه هستیم، جایی که بیش از ۶۰ درصد از قلمرو نوار را در اختیار داریم.
🔴
و در لبنان، ما تهدید یک تهاجم زمینی علیه جوامع ما را پس زدیم و توان موشکی حزب‌الله را شکستیم.
🔴
هنوز کار بیشتری برای انجام دادن در هر دو مکان وجود دارد.
🔴
ما باید منافع امنیتی خود را به قاطعیت حفظ کنیم در حالی که ارتباط مهم با دوستان آمریکایی خود را نیز حفظ می‌کنیم.
🔴
ما ادامه خواهیم داد تا مسیر خود را با خرد و قضاوت سالم طی کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/129305" target="_blank">📅 11:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129303">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4e4cf8f9.mp4?token=Ob0ZQ7FZTx_lsKXJZHb9owauh84bmO2El7-wcLiduGydN9orqaMWh0SolEj0hZTfs2T_fB0qtnFHxRHUoH0jjUFCl3yd1cHjC7B36LAenzVQfG6ef-XYRQE2vRnLcj8oHiFF3vRREXVwILp93M0xh1OOER4dGrdn6ZcMYTYBQtCSg--WYjoE76OMvCLnrGsfZ8PNwqjXCAfBSDDwI34uFZju4TTHEPvxergZ5KM7kN2E4xQbHIBv6dejFeUoc1A-9QbH6Eh07W57mNri4wuYEKCSgIaWL01lh3t90mnHXT6yww_ynqpBBckfNqqeKo8iAguEJ6MOHrK6PVaFr9ueHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4e4cf8f9.mp4?token=Ob0ZQ7FZTx_lsKXJZHb9owauh84bmO2El7-wcLiduGydN9orqaMWh0SolEj0hZTfs2T_fB0qtnFHxRHUoH0jjUFCl3yd1cHjC7B36LAenzVQfG6ef-XYRQE2vRnLcj8oHiFF3vRREXVwILp93M0xh1OOER4dGrdn6ZcMYTYBQtCSg--WYjoE76OMvCLnrGsfZ8PNwqjXCAfBSDDwI34uFZju4TTHEPvxergZ5KM7kN2E4xQbHIBv6dejFeUoc1A-9QbH6Eh07W57mNri4wuYEKCSgIaWL01lh3t90mnHXT6yww_ynqpBBckfNqqeKo8iAguEJ6MOHrK6PVaFr9ueHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: مسیر ما هزاران سال پیش آغاز شد و با کمک خداوند تا ابد ادامه خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/129303" target="_blank">📅 11:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129302">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67043be620.mp4?token=D_Pb8PjMbjdLMh6J0oLWReplXAgfvu-LLNRpNCOs5FphhlgW1eAHFjdZS9QjQu7GNeH18tznhyAhBgE8sRQSKzP80ecjwCjq2cQn996Z9X5_PoBQMjwVhXeohzA3EuqH_nOvB1iKLURQNFzgrSb6KbbcXLLRcCpWo_8R3IXqHxTZD7UeDz2hR5hGYK2zjJXaMA8f9yAJ7DbNorpULyQGT8Dbj9PDcubEZbroHdBuZ6ZxF9XDhAyvWbIb8BFCGofKKoGjCc81IElg_hi4gjykqeqfnfpi9tqXqakhi1OXPOLvu3hheLAMTPo1wjRgNOGomgRa_UqsyGnol5VNuykn_IXxsV5p4-ctywRuiH9z37yLKGoI9hGeJnlP8k075xSUJ8eLPAZy5EI1165mDagmWlQ3O2EHuD4Va44y9dfoW3lk4OtN_HN61Pw8Jr59s9x-_j3ao38qSjA1xO6tNaoaffySgkyf1vKpC56bXkkIZ3qiheWWKz0yTDzNZfmnOLZlnrTJwsoLvM1Mgf9tFi45BZ78B91EhBpGk6wU41bH1VEMAYUDSc7NEK4gwL0ZTzYbArpQp_pdAMOw7PkbVs0dCJfdIWWAA-QChkpDnDmOLwoDEMxd-atQ6n1SKMWgNonrOMl2Oet-Hv9Lnu1kEk4HbI9dutq7q0UVG-gL23t7xKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67043be620.mp4?token=D_Pb8PjMbjdLMh6J0oLWReplXAgfvu-LLNRpNCOs5FphhlgW1eAHFjdZS9QjQu7GNeH18tznhyAhBgE8sRQSKzP80ecjwCjq2cQn996Z9X5_PoBQMjwVhXeohzA3EuqH_nOvB1iKLURQNFzgrSb6KbbcXLLRcCpWo_8R3IXqHxTZD7UeDz2hR5hGYK2zjJXaMA8f9yAJ7DbNorpULyQGT8Dbj9PDcubEZbroHdBuZ6ZxF9XDhAyvWbIb8BFCGofKKoGjCc81IElg_hi4gjykqeqfnfpi9tqXqakhi1OXPOLvu3hheLAMTPo1wjRgNOGomgRa_UqsyGnol5VNuykn_IXxsV5p4-ctywRuiH9z37yLKGoI9hGeJnlP8k075xSUJ8eLPAZy5EI1165mDagmWlQ3O2EHuD4Va44y9dfoW3lk4OtN_HN61Pw8Jr59s9x-_j3ao38qSjA1xO6tNaoaffySgkyf1vKpC56bXkkIZ3qiheWWKz0yTDzNZfmnOLZlnrTJwsoLvM1Mgf9tFi45BZ78B91EhBpGk6wU41bH1VEMAYUDSc7NEK4gwL0ZTzYbArpQp_pdAMOw7PkbVs0dCJfdIWWAA-QChkpDnDmOLwoDEMxd-atQ6n1SKMWgNonrOMl2Oet-Hv9Lnu1kEk4HbI9dutq7q0UVG-gL23t7xKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: مردم اسرائیل به خانه بازگشته‌اند و مردم اسرائیل برای همیشه در اینجا خواهند ماند.
🔴
زیرا این سرزمین ماست. متعلق به ماست.
🔴
ما بازگشته‌ایم، به جایی که از آن آمده‌ایم بازگشته‌ایم، به مسیری که پدران ما در آن گام برداشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/129302" target="_blank">📅 10:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129301">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
خبرگزاری دولت: وزیر کشور پاکستان برای دیدار با مسئولان بلند پایه ایرانی، عازم‌ تهران شد
🔴
او در این سفر «پیش‌برد مذاکرات» را پیگیری خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/129301" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129300">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رئیس‌جمهور ازبکستان خطاب به پزشکیان: یادداشت تفاهم امضا شده، نمادی روشن از اراده برای تعامل سازنده و احترام متقابل است
🔴
این گام مهم موجب کاهش تشنج در منطقه، ایجاد زیر بنای پیشرفت و گسترش همکاری‌های اقتصادی و بازرگانی خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/129300" target="_blank">📅 10:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129299">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d84fa59c.mp4?token=aCAtpba7dB_2AOCuGIYq0mxBzcRGs5XrKRo6uP7ODePuTWOT0gPg75BKnkbzN2NCu_FgpwNoBqANwdmJn4KwzVlsfgZ4LFKW_hqIMFikJ04JsXHMts-bXjZkSURvpJgaxkWdbEoxJihLrLupCt4l0v8EtpVRkGyIsPcB0juYAWaI5rs0Kq_iHUTLcgvTGYk6QlGv9Rd4lcsavvVHgWc0eGjqpKoLk1TWf6lY5rALuni0GPKQjfnw8aerLSq19LCZcO2vvU7gnpKkd2tXigwOIp3qkJgdSRwbk-Fc-KbZMQhi2jrHyoGVW89KSQ3OhuxjroaiWXJkw3T2JhJ1tKeugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d84fa59c.mp4?token=aCAtpba7dB_2AOCuGIYq0mxBzcRGs5XrKRo6uP7ODePuTWOT0gPg75BKnkbzN2NCu_FgpwNoBqANwdmJn4KwzVlsfgZ4LFKW_hqIMFikJ04JsXHMts-bXjZkSURvpJgaxkWdbEoxJihLrLupCt4l0v8EtpVRkGyIsPcB0juYAWaI5rs0Kq_iHUTLcgvTGYk6QlGv9Rd4lcsavvVHgWc0eGjqpKoLk1TWf6lY5rALuni0GPKQjfnw8aerLSq19LCZcO2vvU7gnpKkd2tXigwOIp3qkJgdSRwbk-Fc-KbZMQhi2jrHyoGVW89KSQ3OhuxjroaiWXJkw3T2JhJ1tKeugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: در سیستم‌های پاکستان و قطر، آن‌ها دقیقاً دارای اصلاحیه اول و آزادی مطبوعات نیستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/129299" target="_blank">📅 10:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129298">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزیر کشور پاکستان عازم تهران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/129298" target="_blank">📅 10:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129297">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی دولت: تفاهم در این مرحله، هنر تبدیل جنگ سخت به نبرد سیاسی و راهبری چالش‌های سخت با مدیریت عقلانی منافع است
🔴
هرجا باب گفت‌وگو گشوده شده، امکان یافتن راه‌حل نیز فراهم آمده
🔴
تفاهم به معنای پایان مسیر نیست؛ بلکه آغاز مرحله‌ای تازه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/129297" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129296">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ: اوباما تمام پول ما را به مردم بخشید. او صدها میلیارد دلار به ایران بخشید.
🔴
من پولی به ایران نمی‌دهم. من به ایران پولی نمی‌دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/129296" target="_blank">📅 10:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129295">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f72466c840.mp4?token=WKCOzrDWh8-WoVtXKCP4wTOGX-lTlb8_4S77CETYVhFt9Cwbc6HNBd9hqFPNBc110SW8mup-LDAKHaUl0BCM-vxq5ouzZw-vm9GEigUwjuFNr9p3coxVTJBEBBGjdvJLhGPqLPetf0hJ8nb2HK5r1D_2HniePm7JM9IBI4llaULpChQsL70Y14Si2vwePT35CigG73PTNquGPR3FdjTIYY89gcUrxvi6sdxB3IFr0XqPNSXsIG2sUp3YZEQ6SJQHgq5ZXykgxPCrZmnHdRs4jmTKXeYrqsV32EAZ7YB6TjlSttzVSldUamlqR5ZMwpEKT8OMTia4mFTnOeyMQTzVzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f72466c840.mp4?token=WKCOzrDWh8-WoVtXKCP4wTOGX-lTlb8_4S77CETYVhFt9Cwbc6HNBd9hqFPNBc110SW8mup-LDAKHaUl0BCM-vxq5ouzZw-vm9GEigUwjuFNr9p3coxVTJBEBBGjdvJLhGPqLPetf0hJ8nb2HK5r1D_2HniePm7JM9IBI4llaULpChQsL70Y14Si2vwePT35CigG73PTNquGPR3FdjTIYY89gcUrxvi6sdxB3IFr0XqPNSXsIG2sUp3YZEQ6SJQHgq5ZXykgxPCrZmnHdRs4jmTKXeYrqsV32EAZ7YB6TjlSttzVSldUamlqR5ZMwpEKT8OMTia4mFTnOeyMQTzVzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کشتن قاسم سلیمانی: می‌دانید سلیمانی قصد چه کاری را داشت؟ او می‌خواست پنج پایگاه نظامی ما را منفجر کند.
🔴
من او را یک هفته قبل از آن حمله به دست آوردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/129295" target="_blank">📅 10:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129294">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20faee2d60.mp4?token=giVYIAKGSM_-c2U9GBQE24MCpsvEYF33rUWgAmUWZTDzbhcsEJ9BztQQJ3CguIwTpzQGs97BWSaUiIbxKBDQQl7zfGPA_bgBUQiSoj0SVcvfaSx3tYzJTAsoEbfRMlnFwgugaFu3Pp8862b0VKFpi0_aFShfDvVC8q748AYiLp5br45Mwz_095uUVWxnuAffIaeMLkoPYkf7bQR42vRSifp-5PEePuoPrAACTr-Y_JN8IakTrKZwkvJTYineNR6tL0YjxqQNiucX-3P8a7YZS3NlaENgc9oPA0cD9WoB9ehfWL4FZxqDg9TvXgO9sxp7fLEEduJwu-IgwXkixyPz9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20faee2d60.mp4?token=giVYIAKGSM_-c2U9GBQE24MCpsvEYF33rUWgAmUWZTDzbhcsEJ9BztQQJ3CguIwTpzQGs97BWSaUiIbxKBDQQl7zfGPA_bgBUQiSoj0SVcvfaSx3tYzJTAsoEbfRMlnFwgugaFu3Pp8862b0VKFpi0_aFShfDvVC8q748AYiLp5br45Mwz_095uUVWxnuAffIaeMLkoPYkf7bQR42vRSifp-5PEePuoPrAACTr-Y_JN8IakTrKZwkvJTYineNR6tL0YjxqQNiucX-3P8a7YZS3NlaENgc9oPA0cD9WoB9ehfWL4FZxqDg9TvXgO9sxp7fLEEduJwu-IgwXkixyPz9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد کشتن قاسم سلیمانی: کشتن سلیمانی یکی از بزرگترین لحظات در تاریخ خاورمیانه بود، زیرا او ترسناک‌ترین مرد در ۱۰۰ سال گذشته بود.
🔴
حتی آیت‌الله‌ها از سلیمانی می‌ترسیدند. آن‌ها همگی از سلیمانی می‌ترسیدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/129294" target="_blank">📅 10:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129293">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfaa82c92.mp4?token=oGZta9aHOpr63hj2x3wyQ_eoXF9KQpMoww6a1Eu-SCN7jObQLRnbUFmRe-gjTl8DRNco07CC1CWpPxuD-bKaZFY2TF0d4YOf7iS37yFtTViQskBQtDB8u1KvJMEh0fZ-CP3z--i218riJpjTbwS--kH76BokNpHgiXkoN-ywSomCJYtlU4ADXpgSVFCPMWrAwrl-1Sh8Rr8xz-LVApf5u-ti5afO8eWVIztg8Q1oJu-YIWRfkd3Ug7L2h480RGXDtA7bHAw5Mj9Vti_wNh0NyXEKv8pSeBR7dSHFzwj93LGhuKF0_F1nxRBwgcb7ND-TiLj37YnYcAZsxouCVeYWbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfaa82c92.mp4?token=oGZta9aHOpr63hj2x3wyQ_eoXF9KQpMoww6a1Eu-SCN7jObQLRnbUFmRe-gjTl8DRNco07CC1CWpPxuD-bKaZFY2TF0d4YOf7iS37yFtTViQskBQtDB8u1KvJMEh0fZ-CP3z--i218riJpjTbwS--kH76BokNpHgiXkoN-ywSomCJYtlU4ADXpgSVFCPMWrAwrl-1Sh8Rr8xz-LVApf5u-ti5afO8eWVIztg8Q1oJu-YIWRfkd3Ug7L2h480RGXDtA7bHAw5Mj9Vti_wNh0NyXEKv8pSeBR7dSHFzwj93LGhuKF0_F1nxRBwgcb7ND-TiLj37YnYcAZsxouCVeYWbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره قاسم سلیمانی: وقتی سربازانی را می‌بینید که بدون پا، بدون دست و با چهره‌ای نابود شده راه می‌روند، ۹۶.۲ درصد آن‌ها از ایران آمده‌اند.
🔴
از سوی سلیمانی بود. این سلاح مورد علاقه او بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/129293" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129292">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
الجزیره: ۴ حمله جدید اسرائیل به جنوب لبنان
🔴
۴ حمله هوایی به شهر النبطیه و شهرک النبطیه الفوقا در جنوب لبنان صورت گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/129292" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129291">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ در مورد جنگ اوکراین: وقتی جنگ اوکراین شروع شد، پوتین صدها تانک داشت که در حال حرکت به سمت یک بزرگراه بودند. یک بزرگراه بتنی، بسیار خوب، محکم مثل سنگ، درست به سمت کی‌یف.
🔴
او می‌توانست در سه ساعت آنجا باشد، با سرعت ۵۱ مایل در ساعت که حدود حداکثر سرعت برای یک تانک است. آن خط بزرگ تانک‌ها را به یاد دارید؟
🔴
و آن‌ها ژنرالی داشتند که احتمالاً دیگر در میان ما نیست. او تصمیم گرفت به جای رفتن مستقیم به سمت کی‌یف و پایان دادن به جنگ در روز اول، از طریق زمین‌های کشاورزی و از میان گل و لای عبور کند.
🔴
و چند روز قبل طوفان بارانی بی‌سابقه‌ای رخ داده بود و آن تانک‌ها در آن گل گیر کردند.
🔴
و من به آن‌ها جاویلین‌ها دادم و آن‌ها تانک‌ها را نابود کردند. من این را قبل از وقوع این اتفاق گفتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/129291" target="_blank">📅 10:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129290">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIgDrtE3G--ymz9tDtnVzLCqNHmmHhLK2ofhISqgxeRypN3k_LhKUAfILPdK3efwGd6uJDBBl3DpyxUdigyxqjNYYcCi1WZMqm4KWVCsQb2aY2K_wk3AGP06cU_Fm9u2os_iLnA9CEkTiAv5pb0FxG558TjS1tIZYLy24udL9w5FiLAzSu80hQImeOFIs3RRIi-fv2sqfnN-r9sdM8olUfhuFtT50bK9po9NOoM1OZJTS8W0OwH55F9RpLDtCE6EEmnWTI_kcCQrbd0uHHwls61VRngwXkul8YSPmg2GQD2AI4aXqILIG4bFG6F85yQ38fi2npwU-DaoMOhaEYv_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر یادداشت جدید نشریه فارن افرز:
«ایران در جنگ پیروز شد اما ممکن است صلح را ببازد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129290" target="_blank">📅 09:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129289">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J__AUQPpr0iFCzgRhKzrL9PbJ_sidOL2HoOPxwwIo4mrCuwp2i8Wov8kss3Hc60KzGaHnWjZS8CwkC3WJTzcWGvk7zdmskH63JBB217MQWykh9SoCrjDcw7OtUYdG_v2BL4wh8RgcS0W7TewkNPHz3_lWNHTUZ2b9t9JxKpzBEtS05tMTusKn40VLCU6jDj9MOfh49R7DjznctiYnQpOP9PowCI9fzQJZ2ttT7uNMahnAlyrV0XJJI1OKe6RSpAWhER_SJyqHTGdNnH9O8vON1aBQarqa-7U5FVabu3mLo4or08-iDEwDhOOKvLlEUkwxjtfx36xjQS8EhqpeSg50Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: یک منبع به من تأیید کرد که تاکنون، خط اعتباری که به تهران اجازه دسترسی به دارایی‌های مسدود شده‌اش را می‌دهد، همانطور که در یادداشت تفاهم تصریح شده است، فعال نشده است.
🔴
ایران معتقد است که ادامه دور بعدی مذاکرات ۶۰ روزه مستلزم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ یادداشت تفاهم است.
🔴
تلاش‌های دیپلماتیک از طریق واسطه‌ها همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129289" target="_blank">📅 09:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129288">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
معاریو:توافق میان ایالات متحده و ایران و اظهارات رئیس‌جمهور آمریکا، دونالد ترامپ، از جمله انتقادهای تند او از نخست‌وزیر بنیامین نتانیاهو و درخواست آمریکا برای خروج از جنوب لبنان، نگرانی‌های جدی‌ای را در میان افکار عمومی اسرائیل برانگیخته است.
🔴
۶۳ درصد از اسرائیلی‌ها در پی تحولات بین‌المللی اخیر مرتبط با این توافق، نسبت به آینده اسرائیل ابراز نگرانی کرده‌اند.
🔴
این نتایج در نظرسنجی‌ای که روزنامه «معاریو» با همکاری مؤسسه «پانل فور آل» به ریاست دکتر مناحیم لازار انجام داده، به دست آمده است.
🔴
این نظرسنجی همچنین نشان می‌دهد که تنها ۳۱ درصد از اسرائیلی‌ها نسبت به آینده کشور نگران نیستند، در حالی که ۶ درصد دیگر در این باره نظری ندارند.
🔴
تحلیل داده‌ها نشان می‌دهد که اکثریت قاطع، یعنی ۷۸ درصد از رأی‌دهندگان احزاب مخالف، درباره آینده اسرائیل نگران هستند.
این درصد شامل رأی‌دهندگان احزاب عربی نیز می‌شود.
🔴
با اینکه اکثریت اندکی از رأی‌دهندگان احزاب ائتلاف حاکم (۵۱ درصد) احساس نگرانی نمی‌کنند، اما بخش قابل‌توجهی از آنان (۴۴ درصد) از آینده اسرائیل هراس دارند. ۷ درصد دیگر نیز موضع مشخصی ندارند.
🔴
دکتر لازار معتقد است که این داده‌ها نشان‌دهنده نگرانی‌های جدی در میان بخش‌های گسترده‌ای از جامعه درباره آینده کشور در پی عملیات «غرش شیر» و پیامدهای آن است.
🔴
به باور او، این نگرانی‌ها احتمالاً در هفته جاری و پس از انتشار چهارده بند توافق هسته‌ای میان آمریکا و ایران افزایش یافته است.
🔴
این موضوع در شرایطی مطرح می‌شود که دونالد ترامپ اعلام کرده است ایران حق دارد موشک‌های بالستیک در اختیار داشته باشد. همچنین معادله جدیدی در لبنان شکل گرفته است؛ وضعیتی که در آن این نگرانی وجود دارد که اسرائیل مجبور شود تا مرزهای بین‌المللی عقب‌نشینی کند، توان بازدارندگی‌اش به‌شدت آسیب ببیند و یک معادله جدید در منطقه ایجاد شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129288" target="_blank">📅 09:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129287">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وال‌استریت ژورنال: آمریکا و قطر در حال برنامه‌ریزی برای آزادسازی 6 میلیارد دلار از دارایی‌های ایران در قطر جهت خرید کالاهای بشردوستانه هستند، این در حالی است که ایران برای توافق نهایی صلح، خواستار آزادسازی 24 میلیارد دلار از اموال بلوکه‌شده خود شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129287" target="_blank">📅 09:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129286">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bc3683da.mp4?token=pF_4UkKo5wGgvCchWMJYFJJ4TIMU-1hsZA5daAFwAJTL-VWfxqYxoulkyxlIPwQ4nr3ojPs1Lo1kQ2Pnh3jAOf8Sx0cek8h5hUDvmrdh-t_9wi7zcGn3rwt3w_9iZCy2MebuQ6JKpCeJu_kresi-ccg8bBwe_FdTtnXDUjpWH_CsrrO4waE9Bs4Isa-N-BXzOfISV0lcrBYSqCKCmRHfB33qcuEO_Ka3ISYY97e6uivE8U3z2lt-2_f2bg7-VtdKr_er9btQV5VA3JCyuhDs-rSlKkCiw4m_8e_kAYUSIb4lGIk0W0FjMavCj5iqIP1VM3X0VvTgYC83dWhZsJRIbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bc3683da.mp4?token=pF_4UkKo5wGgvCchWMJYFJJ4TIMU-1hsZA5daAFwAJTL-VWfxqYxoulkyxlIPwQ4nr3ojPs1Lo1kQ2Pnh3jAOf8Sx0cek8h5hUDvmrdh-t_9wi7zcGn3rwt3w_9iZCy2MebuQ6JKpCeJu_kresi-ccg8bBwe_FdTtnXDUjpWH_CsrrO4waE9Bs4Isa-N-BXzOfISV0lcrBYSqCKCmRHfB33qcuEO_Ka3ISYY97e6uivE8U3z2lt-2_f2bg7-VtdKr_er9btQV5VA3JCyuhDs-rSlKkCiw4m_8e_kAYUSIb4lGIk0W0FjMavCj5iqIP1VM3X0VvTgYC83dWhZsJRIbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از شب گذشته تا امروز صبح، ارتش اسرائیل حملات پهپادی و موشکی گسترده‌ای در جنوب لبنان انجام دادن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/129286" target="_blank">📅 09:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129282">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCyfMCqCHUU4py-h3ol8MBhl2t8D1VR5YqosbbZ7bLcaX2MHrx-oObnzWRZqP6_dimq-VfgrHEINrGqO3g7j_SjbXYW3I12h4TEZuqPUrRzLLj-xXebgkfRvSyJQMkzoA20CUTL2HqmhJn4UEl8K0gO3k--f0DJShniNmFgW_dtp0UGRtqzva1Zc4hKgnlKKH_8RO_0sX3VXlwEZGIewGV1xFAsM5ThzXweUM95didWUlgG1pWmzqh0GNRTdpG40su6erio8sTOiuK1YzffZHH63_6l2kES1VGUnLaSpOnlgxUhxbYmrTUPcwHIeV4k1Bg1XPqlvaGaWz_WK9HnosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pj_JmlHKWyvGYEwIVNvfCF7KAXDB2jOca4fazEYve9XnZa9bCjyl35t1p3LDJ1W7f9m2yeLIbyjEGOS5g-WSIfw6uYfheTcOCgPmxMHIpzT8SGi2YdAsPUzPggHXCv85TOcLDtQQKoWKVEwW5NgRVnRK3ereytV5yGKy3kyyhf41Ki6tEZIgQVZXpojjqWJpjIb34hnMrWwkupOMSQ8psKBBDH2LMOTPUdb5idKgrM2vq1mgx9h7KPwR2EPNld75zMKm9hq5sUONY-A2VlwTzVuDBM6WZ4j5pnc0AJ4aNf0oyQXJkQCYdQZbT5qo-iPZg8r07hT0u58FZgGsOT0BVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0FTEDeYG9Fk9s-Q6U0AVXvU5Js8n1skzWNrTdb9marrUYUhJqUoosfHcGe8FkJCEY9CQg4RwjmbMcgih-kHc7Lf7T4wdo3v88apfrerphCDmmcc2Ioz9zNOUxHWoRDFdr90-LoXMGovQzx_3ETVQutbu2xdhNkv8Fqsr74ypCjAReLsYCCp3fe2ocurG6_AvH2YBzJD84xqv08dNxH8GUyD-I1yogs97lUVMWXQRd7ykv9tcI1hKCbY-lo504ZSAVhX4Pf_ewb76kY84P9FFgit06YOpiVi2pcXXFaR4T9MRe8acjXXJUsIeVi7tWzz-jNbpih_bRPJPbWiHIlecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C0UXxiETYbQZtrnOk3BhkQMcban_N_K5cxrFRFofvHlC6WGRgrtKKATFpvXaARCZSYxISl22Odonto6yVz_Vg1_4cOcMqNjJ0RlBECHkRxeuQblS9WOhW_00ayuo5UL9eIgz-_m2B3kIeVAW4XJngOAive4WBQ9TZKDV0VC8zWlGEGGdSyo8r-bcX-Y4pUih8vHlZQJ9WgkuapPhy0o5FD63qkYvV60ar_xO5s_t8FnYoaT9EKiBXZwcV0AH-WgABoDYIQXPYFHNp5Vyel1aPLcId-OJu2zczElk2Ng3RfKieU2GvY-oZ7zWu62uQrbRREjSqFejpG_JiySzbrkSww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات صبحگاهی ارتش اسرائيل در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/129282" target="_blank">📅 09:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129280">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHD0f_sV5umJNg7NmjQb4WwJBw0cwQCnDHxHg9Ii7wi_g8I_IcJnOSYQINkMANAdu7I5I9gc2H2B7UNd1J7yypXzUe_jqQ3RV6mrxbc_OS0UNk5zzKvi50P0eFGM4F-8G8vo1OptwvIlW09S1B1iIY4KShz2gw8KwAQzPcFA-yFh9iGPKYikOirVrCpjGOQjgpwtJMglVk3nkd7KQl12i0vPQ_LLW2_qV-wXNoPkgLU6dMTQeovCRArL26SqpKgSVSADC34mqKZ_PiMPUevMo0J6oWyqG1zTskkmaiDaQLKUSwXM9zDR0e-Ll2slpwB1eHOYWWZnabJn8HE38q_9wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SpFR2gYbDt3E04AURGD7ZiT3H8s1SLEoG3Iwm3FVnx593IDwwlkgHMYF3RvQriReNoWlVBh-jMDDzTI35tW2kRWvqa-PjRx4-PugDvFxGNyPXU1yWKSB80PBkSsutZtuC_PSG6W_y1yQ-grcU7Ffd2MdkswF5ZHajpbJoB5WQFHMzeVvzo14lY-2djEIai9z5BawjZkDHzVk1e9jEWCAR2Zj7NmpDzxpIA4l4uwuvRP9Vv9IeAGqIoINjS8MY-fSv_42q3IjLjkDg3pFgjgiKtZFeBCxg2BY6W7UCaHO1oUZVJDrqRFkDUTDr6_hJZz-gLH7ojPIvLXgZYCjRuFavg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بمب های فسفری که دیشب اسرائیل بر علیه حزب الله استفاده کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/129280" target="_blank">📅 09:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129279">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سپاه: احتمال شنیده‌ شدن صدای انفجار کنترل شده در محدوده‌ جنوب اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/129279" target="_blank">📅 09:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129278">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری / آکسیوس: عباس عراقچی، وزیر امور خارجه ایران، در حال برنامه‌ ریزی برای سفر به سوئیس است و این تصمیم هنوز قطعی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/129278" target="_blank">📅 09:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129277">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
قائم‌پناه: دارایی‌های بلوکه‌شده ایران به صورت کامل و تدریجی آزاد می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/129277" target="_blank">📅 09:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129276">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
به گزارش رویترز، در نتیجه لغو تحریم‌های ایران، سپاه پاسداران آماده است تا از نظر دسترسی به صندوق بازسازی بالقوه ۳۰۰ میلیارد دلاری، «برد بزرگی» کسب کند، ضمن اینکه از محل معافیت از تحریم‌های فروش نفت نیز درآمد کسب خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/129276" target="_blank">📅 09:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129275">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ونس: بین ترامپ و نتانیاهو درباره چگونگی دقیق پایان دادن به جنگ با ایران، اختلاف نظر‌هایی وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/129275" target="_blank">📅 09:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129274">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری/ ونس: خروج اسرائیل از لبنان بخشی از مذاکرات با ایران نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/129274" target="_blank">📅 09:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129273">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
منابع خبری صبح امروز از حمله هوایی اسرائیل به یک ساختمان مسکونی در مرکز شهر غزه خبر دادند که در این حمله ۳نفر کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/129273" target="_blank">📅 08:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129272">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MfFCo3z5D5F6eK823vCqcdOaA_zq8kVYeUKZishkn0JOtrYrrttNkqsMTYEOyL08N802P2US-vAdwo1PSdSHL_4pVBM6eNuy_mPdeEimuArdxF-MvLEWariy63CTGgJw6HyTEHagrQl8FdbdNI_ks64p6EZIxbKqqp78NLNfSwmIxWPY3uL11VkNeOouCJOMGIxobbopVHpKmQKuU-G3X0eibCRkfK_JnekdFixYebC62A0Ei4_ajBUpQXNwaHM-GD5qdi6w-jZ8mF6vSDIj3gFNTBL2H9Lz1_tLBQQbZshzFd0B7twaTbH4ynUHdd0KR8eUmprmuAawp1I1Usujrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب ائتلاف بین‌المللی به رهبری آمریکا، یک موتورسیکلت را در استان ادلب در شمال غرب سوریه هدف قرار داده بود. گفته می شود این موتورسیکلت توسط مقامات ارشد حزب اسلامی ترکستان اداره می شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/alonews/129272" target="_blank">📅 08:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129271">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
خبرنگار الجزیره از حمله هوایی اسرائیل به شهر کفر رومان در جنوب لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/129271" target="_blank">📅 08:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129270">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249ce5af71.mp4?token=MBYL8yH_RVRh-GF5dIpF0O0pYmUjl55wxULREndDMyY_jtc4fh_Q_nCBedeQkW8f6Lq-N-Vbhs8l_ONzWh7luXSMamOEcHcMY_giihaehlkTFsh_NPTPD2eyQT_iKwU5MbeW08jxe0s0IDTtd76ad2jDGy3kn8HQTzAEBQl3SJMGQK8cTOCxMu7NtPZexxpATQ6nBckDezku3mz_xVu08QDkLEg8TIdhiOFF4TG8-fz6N2CsdpGKL68JvsjzZhnUXaqMJT824ObnJwYOSXEIbKrRduxZJEsZqHg_ojF_WQ5Tq6iiksUT0T1AN2wsHpOxvTVDJS3Iv6iOyHlw9aiVsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249ce5af71.mp4?token=MBYL8yH_RVRh-GF5dIpF0O0pYmUjl55wxULREndDMyY_jtc4fh_Q_nCBedeQkW8f6Lq-N-Vbhs8l_ONzWh7luXSMamOEcHcMY_giihaehlkTFsh_NPTPD2eyQT_iKwU5MbeW08jxe0s0IDTtd76ad2jDGy3kn8HQTzAEBQl3SJMGQK8cTOCxMu7NtPZexxpATQ6nBckDezku3mz_xVu08QDkLEg8TIdhiOFF4TG8-fz6N2CsdpGKL68JvsjzZhnUXaqMJT824ObnJwYOSXEIbKrRduxZJEsZqHg_ojF_WQ5Tq6iiksUT0T1AN2wsHpOxvTVDJS3Iv6iOyHlw9aiVsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی گسترده در فلوریدا
🔴
آتش‌سوزی‌های گسترده در منطقه اورگلیدز در جنوب ایالت فلوریدا از اواسط ژوئن تاکنون حدود ۸ هزار هکتار، از اراضی این منطقه را در بر گرفته است
🔴
گسترش دود غلیظ ناشی از این آتش‌سوزی‌ها تا مناطق مسکونی اطراف نیز رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/alonews/129270" target="_blank">📅 08:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129269">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MsGRWnOHi0UO48KbtZytkGkq95cl4z7YM1xxU5rYzA7HUm_hcdofkOsOClt_wejvhzNuHC0Hw0YsQx1Cm3LkaYu3UqwkaCqwoWsGFMHKLKkzO2XOhmjCRCAVQv-3rwLJ7s9OUh9wJhkEi3E47qhHmLLSPeNKMswtGeMgNH8d_cxBK6aOPmclqFLPGSxZhcM0_yYxUdiqtAt2Ac0aMLallYzhADZ8bV3y5KN9stwbBCZyul6eysmbJP7l0hjZXuzKmiSiZCyZlu7Q_PIReV4XeYW0m_zpJFIhBXG16guwW-9bpXQMiDT0veSDs1LPgpRm669BZPcvnSdopHLfc8FWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌ای نزدیک به میریام ادلسون، «اسرائیل هیوم»، از توافق ترامپ با ایران به‌شدت انتقاد کرده و آن را «خیانت به اسرائیل» دانسته است
🔴
ادلسون یکی از مهم‌ترین حامیان مالی ترامپ و تاثیرگذار بر سیاست‌های او در قبال اسرائیل است. این انتقاد به‌عنوان پیام فشار از سوی او تعبیر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/129269" target="_blank">📅 08:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129268">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
هاآرتص: نتانیاهو وارد «روزهای پایانی سیاسی» شده و این وضعیت می‌تواند برای اسرائیل خطرناک باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/129268" target="_blank">📅 08:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129267">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5hysvJ0k5tZ2YA8r_T4YYPFIc9eiPIUkThzQHzuagyFzZL7Tsl2tuUSKyt7sMUsW67WtJgOqrihsITR5bx-dJ8A7PfnwpcXcjAD_6oRPGpxPBNZDSlSeMXh-6te2H7WiyhqJeRI2JupUm8H7dlKiInmkq7jytEpJG-KwUii7Qru49EDI6KpVz9pDLRpp8ZAr0qCsJd3JWweH1qRwKzBbtACY23GZojLeEYxOLLPG-tkGP3rLhNyZB7_3UI0ZdYyfIPWZca5VITrsELTK5AkUyQ5gsbVsoDc6tU6Uwao6uWhJvDhn7wEVNnRdDlpTwXuS_Ns2eRlYARz1YJjt8CluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرکت 10 نفتکش ایرانی به نام های؛ دیونا، قهرمان، سونیا، دورنا، آمبر، خندان، برف، هدی، استارلا و دریا عمیق به طرف چین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/129267" target="_blank">📅 01:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129266">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZypzbCpD05amA8i33YSDSi2V0p5nVxazSJtlaze4TWv1vY2jY41QegE2T2m2BROQcTTzV6xIB9wO98UIgdSteV-MKptgNNUB1ZFWMrz-Tqjp8lucN7gyjKv0CcjFJAGG7-aW1AbT8UypnM70s67otwCpO57iHUOWB9XRVz_Ac0ooFyIJmKgQ7Lk8zYiy8sTf-zEegfIWCXrncnoY28F3JpKOTlsGoJC2_ZLhy_KQeVsBGufV_OftlSX8_vlsZE6EK5J65cA1Y7QoyMQyuikd2S8m5bg3O819ufsZo9UQriCupfF-6291gP9HOMR4ReFUUNRcoRwH8hEwJZwX9D9R-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی :
دشمن اگه غلطی کرد باید تنگه رو ببندیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/129266" target="_blank">📅 01:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129265">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfVj78LQFrA2OBV9_fjX9V44SLUq2PNKcEGdXkaKnP7ttReuUUIdWIbVSU6qAk1YEMn2PpAPJFe8KdVMg_zEtgtOv3Y_nqW8fnFR4gh8pMzjsYCJ2lnqPIvmzD432PXoAF5dnt0Ngb2RfhMVYclJ_zoKXkD8hNmdsViWUQOSLnU6Xe7auh8AB7noyJqV0xKEvwHchApiAqxU5yzNXOACKJ8x503DZC_BnnLxIJuZs50fT1rp-HiJY208eO5Ix1Kw8sKlvH4NGHC2wzxzbViYeJe-DErMlZpVWRPz7TxwaWDG1dTl5EW9BF21gjkBzhseeUp4LyeTze9pCO0UiGOp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی آمریکا هم به عنوان دومین تیم به مرحله حذفی جام جهانی ۲۰۲۶ صعود کرد!
آمریکا 2_ استرالیا 0
@AloSport</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/129265" target="_blank">📅 01:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129263">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dda595df5.mp4?token=GTJiiOXftFwWJWoQ6awJPDOLAZSC5nnsgR6MucDRIG8WC5Bthrlh8GdcXVucE55yxfWZi1-4OqkZoARj9k5Miqnghhkr8-a-xLOCxxEtLGxwmhN7ZbmK63HEKd_QL1wSxc1R1RMDPA9HgEw6WcrEtwPvWTjt90wGUN6BzEQmhpEhcDFso69Tn-ztve8MPvJeS2hKStDnqVDtNm-cLB5cp2YiMHrMklK4urb7VL3Mo1rIn5_qBODkx0HsAaByuuseMK4PwN43Xb6XtM0WnCWuG6re5DQtZB5Vs6_kC-ZvmBvgJGf0xd_5ueCDXK-sLJM0lD78wFxeD8rNHmOT7z9mag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dda595df5.mp4?token=GTJiiOXftFwWJWoQ6awJPDOLAZSC5nnsgR6MucDRIG8WC5Bthrlh8GdcXVucE55yxfWZi1-4OqkZoARj9k5Miqnghhkr8-a-xLOCxxEtLGxwmhN7ZbmK63HEKd_QL1wSxc1R1RMDPA9HgEw6WcrEtwPvWTjt90wGUN6BzEQmhpEhcDFso69Tn-ztve8MPvJeS2hKStDnqVDtNm-cLB5cp2YiMHrMklK4urb7VL3Mo1rIn5_qBODkx0HsAaByuuseMK4PwN43Xb6XtM0WnCWuG6re5DQtZB5Vs6_kC-ZvmBvgJGf0xd_5ueCDXK-sLJM0lD78wFxeD8rNHmOT7z9mag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون درگیری‌های سنگین بین نیروهای اسرائیل و حزب‌الله تو لُبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/129263" target="_blank">📅 00:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129262">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78535e623.mp4?token=CoUxV78672lQp0UMLXD1ceq0S7nPFHYLBkF12m7n70OAkH2OTKjwe5fd2KYS2CIkJNubY33n35TWwpNEBmOh30M7pbz-AEJqXnq1VydAERbTATE1-odqq-dul54gGHhsXIFX7BpjPlGZfSRKYNdCAbiqlRxovcrgrjz28gND4ww_YmYx6G5wI5u_Xkty8D9q-nHI2SfvnhHuzIH-cXq_VQjXSuBAHoIsULTX4tEnv2ZcRGGqMIrgkgyVeT9Yc3XngB6arak6DPJbdVkedQomGxKbztZEoMbBWWY1af39h6qCiu9LfFPMQVpP4FXC_84Eyf7t329kmtVwzBuenr3ECA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78535e623.mp4?token=CoUxV78672lQp0UMLXD1ceq0S7nPFHYLBkF12m7n70OAkH2OTKjwe5fd2KYS2CIkJNubY33n35TWwpNEBmOh30M7pbz-AEJqXnq1VydAERbTATE1-odqq-dul54gGHhsXIFX7BpjPlGZfSRKYNdCAbiqlRxovcrgrjz28gND4ww_YmYx6G5wI5u_Xkty8D9q-nHI2SfvnhHuzIH-cXq_VQjXSuBAHoIsULTX4tEnv2ZcRGGqMIrgkgyVeT9Yc3XngB6arak6DPJbdVkedQomGxKbztZEoMbBWWY1af39h6qCiu9LfFPMQVpP4FXC_84Eyf7t329kmtVwzBuenr3ECA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مداح دوزاری، پزشکیان را تهدید کرد
🔴
پ.ن: مداح‌های بیسواد و کودن چندسالی هست که تو تمام مسائل اعم از سیاسی، اقتصادی و اجتماعی نظر میدهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/129262" target="_blank">📅 00:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129261">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c909e237b.mp4?token=qltdHlZihCqz3RdzwfayzmDaJHVPFSp-4C-q12aiAwFMTqo1_6eMUZRpQkdZzfcF7iIbmfP_Ist0U3ZmG2fqfRQnm8NQDOS0AkjJ6-s2VIIkwpUsW0jIgscrBe2L3213qlRuJDF89LTa_PBVrGglPG7kLiY6DgrJC4A_QBVIJTQ2L9qMNb7r4bE7SrhcNAc7IgwaHuROfOPmfKVF8p82c9JlD0qBWB5T2_8bHB8EEi6uYgxPElqmJNURMNpN9YgJx0BJ6juXDtTlD0EFBWl6je1OhcG2ziutirLlBiJI4iNBIMRG1UiiE-TaYjtBmE0WsY6jMnidZTXPJrt7OZ6tiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c909e237b.mp4?token=qltdHlZihCqz3RdzwfayzmDaJHVPFSp-4C-q12aiAwFMTqo1_6eMUZRpQkdZzfcF7iIbmfP_Ist0U3ZmG2fqfRQnm8NQDOS0AkjJ6-s2VIIkwpUsW0jIgscrBe2L3213qlRuJDF89LTa_PBVrGglPG7kLiY6DgrJC4A_QBVIJTQ2L9qMNb7r4bE7SrhcNAc7IgwaHuROfOPmfKVF8p82c9JlD0qBWB5T2_8bHB8EEi6uYgxPElqmJNURMNpN9YgJx0BJ6juXDtTlD0EFBWl6je1OhcG2ziutirLlBiJI4iNBIMRG1UiiE-TaYjtBmE0WsY6jMnidZTXPJrt7OZ6tiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برنی مورنو، سناتور آمریکایی: لغو تحریم نفت ایران به نفع آمریکاست چون چین پول بیشتری می‌پردازد
🔴
«ما اکنون به آنها اجازه می‌دهیم که نفت خود را بفروشند. این چه فایده‌ای دارد؟ این به نفع آمریکایی‌ها خواهد بود. این باعث کاهش قیمت نفت می‌شود.
🔴
و چین را مجبور به پرداخت هزینه بیشتر برای نفت می‌کند! و همچنین متوجه می‌شود چه کسانی نفت چین را می‌خرند. بنابراین ما را در موقعیت عالی، یک مذاکره عالی قرار می‌دهد و در نهایت، من به رئیس‌جمهور ترامپ اعتماد دارم که تصمیمات درست را می‌گیرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/129261" target="_blank">📅 00:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129260">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ: ما رابطهٔ بسیار خوبی با اسرائیل داریم؛ نتانیاهو یک جنگجو است
🔴
اسرائیلی‌ها باید از نتانیاهو قدردانی کنند، چون او واقعا کارش را انجام داد. ما واقعا در کنار اسرائیل به سختی مبارزه کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/129260" target="_blank">📅 00:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129258">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ درباره اوکراین: خیلی چیزها توسط بایدن به اوکراین داده شد. آنها باید هزینه‌اش را بپردازند، اما این در برنامه‌هایشان نبود.
🔴
هیچ‌کس از آنها نخواست که پرداخت کنند. من گفتم، چرا پرداخت نکردید؟ آنها گفتند، هیچ‌کس از ما نخواست، آقا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/129258" target="_blank">📅 00:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129257">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ درباره حمله دوباره به ایران:
به یاد داشته باشید، اگر این کار را انجام دهیم، ناگهان نفت به سرعت از تنگه خارج نخواهد شد.
🔴
افرادی که مالک کشتی‌های میلیارد دلاری هستند، دوست ندارند موشک‌ها بالای سرشان پرواز کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/129257" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129256">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd6c2692d6.mp4?token=NUZn9qIWdlr4-FzT7aV9Hne3NQlmt1UU7ueRIbjo-pAdEfiT--dcsZHv4pAQvqNYTp8kE1kTzq1W1Pyak2_UJioQVg4rDKWhLY67oFEkOE57QB3ozbBSXqivnMHSYq2ak0WZBMAGk6BAXvbTB4OPJM5SRzwBU9O1dB5X3OWcALDpjdABUo_wBIWbQkssH-fqPGHFvIKsXsoGCNlA7HXLGV6oMKxRR4ArYfr6IkKn24zYJS-oPOOFXlsdpyJZWc7pOvat8jKpjCYYoBsQbD0OYhMlCPME7hbJvJiKuFALCfybjuV3C3OQeLf7_wt56B8Q7e7w8kI0pXoVb8bAvMcKPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd6c2692d6.mp4?token=NUZn9qIWdlr4-FzT7aV9Hne3NQlmt1UU7ueRIbjo-pAdEfiT--dcsZHv4pAQvqNYTp8kE1kTzq1W1Pyak2_UJioQVg4rDKWhLY67oFEkOE57QB3ozbBSXqivnMHSYq2ak0WZBMAGk6BAXvbTB4OPJM5SRzwBU9O1dB5X3OWcALDpjdABUo_wBIWbQkssH-fqPGHFvIKsXsoGCNlA7HXLGV6oMKxRR4ArYfr6IkKn24zYJS-oPOOFXlsdpyJZWc7pOvat8jKpjCYYoBsQbD0OYhMlCPME7hbJvJiKuFALCfybjuV3C3OQeLf7_wt56B8Q7e7w8kI0pXoVb8bAvMcKPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: پیت هگستث یک فرد ذاتاً بااستعداد است. او نمی‌داند چگونه ببازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/129256" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129255">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5mPcz5Ov_7f8NdqKq28gZLgiFCP4i2uKk_7jPf7uNRCFI6pmN7eRf2ODKsnGJY0rIMV0wbR1XWic7OdswwYngqfYLUGhOt0nDLedD8xCiZB12BN0AWX1KOp2RJF7CHNg9NosExecpqzGhPXCHLDJAx-GuO3fiBEV58uBa6XzO1Hl7IlzE3Y6YgpUVQPzYZUKc1X0n8FyvbtG8xhmF4jHatjdAH78mcKe7iiOaEaOHyjIqwqObAgZxsierm4337_Je4Ren95afPu8Hjj8kw7Kt6PQXkILzPsViJIbCZ9QwT8Z8mTsVNpxku09jMfMUEcZvLXygRDaJ_kOXha-gaDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی: ایران به نقض تفاهمنامه پاسخی بازدارنده خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/129255" target="_blank">📅 23:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129254">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ اعلام کرد: جنگنده فوق پیشرفته F47 برای ارتش آمریکا در حال ساخت است، پیشرفته ترین هواپیمای جنگی در تاریخ بشر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/129254" target="_blank">📅 23:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129253">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
صدای چندین انفجار در استان ادلب سوریه شنیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/129253" target="_blank">📅 23:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129252">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aYFS9q6D_ovsLvZjHuROwRl7GowJc2pQx1NTzoR929u5fplxmV6_KKgiY73Lk9AXVgJ7TYpKbl_YUV1ekLvlLLRpRYN324cFbmnSTjAwsSlOYSL2CkAfuCoB_aq4SzyGcs_Lec-Kb4fQMjEqQs10rGDsff5pEd8qsQtzJNlkii8YA0kgMg4PsSyR-CWu8hKqchwsw_L1wGDN8dnRL8ocr5WM0rLOu43dPSAl5LVtubThFzgMjnuWpYaz_av2glFksfR63DnVYrFVHLs_zBNfx1p5CifpbSgmBv9bYUogprt4bkdX7TDmMtrJIdR9GnS3bAX6F3Ph58KvURrOSsk26w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای زمینی ارتش دفاعی اسرائیل بار دیگر در تلاش برای پیشروی به سمت علی الطاهر، جنوب شرقی نابتیه هستند. حزب‌الله یک بمب کنار جاده‌ای را علیه نیروهای اسرائیلی که قصد نفوذ به این منطقه را داشتند، منفجر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/129252" target="_blank">📅 23:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129251">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d97f24c8e.mp4?token=Bwg9Y6q9b1XLyvJvwBCQKLbW6AoBUn7elNvUBcaO7E9--Z5oiHeg6UAwYkDw4RL37MIHKdzp9NjSosRMI09HzcFm-06Dy1pgY57dfPjEFB1wPtNF6Fs6BZaAgICOCVMyrrRjl--BO4sqyFwlwooPFEQazk5toYAzGkBIOUoi2CSnzkxz6LR9eAlqhv8GDnLfdGMmt4OhMwN5DU_SyrPJAvcr-0TQ18tJ2Yy_-wcDSTOWEJYbUZtAhzaU_h98R9N92KCngp_Aizit8NyL2ts0YoJCe8nE8Ew66-D4MkuqSSR7MYcpKQs3gYTAhrjP2oKiR90zpvREZzMPQvp9FbLtSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d97f24c8e.mp4?token=Bwg9Y6q9b1XLyvJvwBCQKLbW6AoBUn7elNvUBcaO7E9--Z5oiHeg6UAwYkDw4RL37MIHKdzp9NjSosRMI09HzcFm-06Dy1pgY57dfPjEFB1wPtNF6Fs6BZaAgICOCVMyrrRjl--BO4sqyFwlwooPFEQazk5toYAzGkBIOUoi2CSnzkxz6LR9eAlqhv8GDnLfdGMmt4OhMwN5DU_SyrPJAvcr-0TQ18tJ2Yy_-wcDSTOWEJYbUZtAhzaU_h98R9N92KCngp_Aizit8NyL2ts0YoJCe8nE8Ew66-D4MkuqSSR7MYcpKQs3gYTAhrjP2oKiR90zpvREZzMPQvp9FbLtSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما سفرهای زیادی انجام می‌دهیم. به ترکیه خواهیم رفت.
🔴
در مقطعی، برای یک کنفرانس بزرگ به چین باز خواهیم گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/129251" target="_blank">📅 23:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129250">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
شورای اروپا: آماده حمایت از اجرای توافق ایران و آمریکا هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/129250" target="_blank">📅 23:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129249">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: اگر با ایران به توافق نرسیم، کارهایی خواهیم کرد که آنها را خوشحال نکند، اما فکر نمی‌کنم این کار را بکنیم.
🔴
توافق هسته‌ای ۲۰۱۵ با ایران یک فاجعه بود
🔴
من با رهبر جدید ایران صحبت نکرده‌ام، اما او شجاعت خاصی دارد.
🔴
من از موضع قدرت مذاکره کردم چون نیروی دریایی و هوایی ایران نابود شده است.
🔴
کشتی‌ها به طور بی‌سابقه‌ای در حال عبور از تنگه هرمز هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/129249" target="_blank">📅 23:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129248">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: حدود ۷۰۰ کشتی از تنگه هرمز عبور می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/129248" target="_blank">📅 23:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129247">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv_DbSdEu06fQKqf-F40NbPP3fs9PhxdAelm42YWMAKb6Ts4pXqJGRJtnY6xFYPB_Q-IFodT41UZ22Rj0nL1k2zeOcpjm5n4qx6CP1SOmqIjQHYPf3LZtyYTMgBry53tK1PoVb6oRId6uePDCq4QP0mhCneu9_Es8uuw3ogL0aGf7RirYHUWf8GMjnqFkmK5um7QYDUhReSa1d_emcH3dELjiZvDcEH9Vn_nbd3r0moqv-XnHn6yzyMHrJogd-hZ3IgfYhhMBdBM90GWBjJ2qhxCNYUekWVi6yx0BqZ5ggybcL_FkfFUqYUxnWpXkPUKWefo70msni3w_A4yUPHqXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از هدیه قطر رونمایی کرد!
🔴
ترامپ در پایگاه نیروی هوایی اندروز از یک هواپیمای موقت جدید ریاست‌جمهوری رونمایی کرد؛ یک جت لوکس که توسط قطر اهدا و عبارت «ایالات متحده آمریکا» بر روی آن درج شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/129247" target="_blank">📅 23:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129246">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: کشتی‌ها دارند از تنگه هرمز خارج می‌شوند و نفت صادر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/129246" target="_blank">📅 23:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129245">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رئیس اتحادیه املاک: نرخ مجاز افزایش اجاره ۲۷ درصد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/129245" target="_blank">📅 23:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129244">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سناتور آمریکایی تد کروز: دادن میلیاردها دلار به حکومت ایران که شعار مرگ بر آمریکا سر می‌دهد، ایده بدی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/129244" target="_blank">📅 23:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129243">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b39ccf54.mp4?token=gKd2-iAOWfQ7lc8l1V_MLo-WOpmnc5mJjf8NtaUdrX9s1rFaIkczQGY7esCo8UaFengaY3KXJuX-_ST2KOqfmBVUSe_rylxA117p_tiOvB6LF4NN9GWfYokEHBlAxwYdPw8QP5R36CYUr_RinJSSNLcIuW5eWwS9sY2GarA_jBr5AhP4OkdaHu6U2LKkkwanXfjt-hWX-Ly1RnbV71ZTKPJqZOE2sDrGbXdeL1zchQ0fg1LjfyYEjvGzUp00d9k5heKswRJB2Z8_Vw8LUbOKTniiDezZzQ8adgUrIx4ThVWAKON4HrZWne4Xo3oKG4X1-UdBwOcTkmU9U13Xdy_TyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b39ccf54.mp4?token=gKd2-iAOWfQ7lc8l1V_MLo-WOpmnc5mJjf8NtaUdrX9s1rFaIkczQGY7esCo8UaFengaY3KXJuX-_ST2KOqfmBVUSe_rylxA117p_tiOvB6LF4NN9GWfYokEHBlAxwYdPw8QP5R36CYUr_RinJSSNLcIuW5eWwS9sY2GarA_jBr5AhP4OkdaHu6U2LKkkwanXfjt-hWX-Ly1RnbV71ZTKPJqZOE2sDrGbXdeL1zchQ0fg1LjfyYEjvGzUp00d9k5heKswRJB2Z8_Vw8LUbOKTniiDezZzQ8adgUrIx4ThVWAKON4HrZWne4Xo3oKG4X1-UdBwOcTkmU9U13Xdy_TyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه ای که ترامپ وارد نشست گروه هفت شد و با شوخی خود "من رئیس هستم" جو سنگین نشست رو شکست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/129243" target="_blank">📅 23:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129242">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc24435ec.mp4?token=XiQBDHeyJxStPDCMGGgtL4C7As15AdYX5jjN6ztwAyYnLE5X3kLIfrImZXuzzzE0waSCF75QPWHvfQO_Mh218yu_jJVg5Vay7OqcHPoaOArC0hpmZO9J0Cz-pJYm7NP4Dne0EXmTQeG_Wthn0paVeMjBdIsHSL_2wvXtye2rLkbiV0nJg8C1DppWpIv76_KqYLAINtWacayM1w54dfBk-kTirq0uUVLFfvSdsIHEny9lZ_vC6BK-pCRR8EFY8cnaSGt4xDaVla7MQ9gVvIgqZGLRN6fkxSQVBr0T6nO-YwLtKajk58nV_4ZrSvE_4uaQHC6wVWkT-q0P2uauUJJJVKIPLrhU6nr1dYuC8_t9kv08yYjoisriKprz1k_vglW-GcSCnnaUez3v26WuoTYXdg3kkwUG7FTqYhp0z4Le_qDengJqCRiDUX_XO8OwlcausHV5CCxrS4Qf2LJrZpcG4Plm8_SJoxcPJvPQ6_Pxjm_qlnoqIN2KoUto_BQdF-Ul8JPwufGQlTz8cQebCX50KkYCAeMENRgEZoh4nBStriLKY_aTkO27-tXTurDPC9yC2qiqvlCQPOiC3RtGftGT2B5ylwYYBwYIZn3VbAo_Vk_iOQWFvZWKSs1XtuVEh_rrZ-rTodfx4QpZD94I_5eLtM6PDNO4hTKpmi4O6bB5YCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc24435ec.mp4?token=XiQBDHeyJxStPDCMGGgtL4C7As15AdYX5jjN6ztwAyYnLE5X3kLIfrImZXuzzzE0waSCF75QPWHvfQO_Mh218yu_jJVg5Vay7OqcHPoaOArC0hpmZO9J0Cz-pJYm7NP4Dne0EXmTQeG_Wthn0paVeMjBdIsHSL_2wvXtye2rLkbiV0nJg8C1DppWpIv76_KqYLAINtWacayM1w54dfBk-kTirq0uUVLFfvSdsIHEny9lZ_vC6BK-pCRR8EFY8cnaSGt4xDaVla7MQ9gVvIgqZGLRN6fkxSQVBr0T6nO-YwLtKajk58nV_4ZrSvE_4uaQHC6wVWkT-q0P2uauUJJJVKIPLrhU6nr1dYuC8_t9kv08yYjoisriKprz1k_vglW-GcSCnnaUez3v26WuoTYXdg3kkwUG7FTqYhp0z4Le_qDengJqCRiDUX_XO8OwlcausHV5CCxrS4Qf2LJrZpcG4Plm8_SJoxcPJvPQ6_Pxjm_qlnoqIN2KoUto_BQdF-Ul8JPwufGQlTz8cQebCX50KkYCAeMENRgEZoh4nBStriLKY_aTkO27-tXTurDPC9yC2qiqvlCQPOiC3RtGftGT2B5ylwYYBwYIZn3VbAo_Vk_iOQWFvZWKSs1XtuVEh_rrZ-rTodfx4QpZD94I_5eLtM6PDNO4hTKpmi4O6bB5YCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: اگر لوکاشنکو می‌گوید که نمی‌خواهد به این جنگ کشیده شود، باید حداقل با مردم خودش صادق باشد.
🔴
زیرا او کسی نیست که بتواند به جنگ کشیده شود. کشوری است که او در آن زندگی می‌کند که می‌تواند توسط روسیه به جنگ کشیده شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/129242" target="_blank">📅 23:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129241">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGobNT2yRPFodzNUXkUqBispPD4kI7gN25-15j7ULrq7aYLQktP0S-yZwDnbGqO63d_eXa9xSnL1xBtdmkSLqGSnHYED7ljUWRu-7bOtB47fpTAxtZgM41rFXj9uILLBuKIdSae212QdOrCced2lD1jHdQPCs1wygE1eCDfZ7WKYRqPRxEklsCdG6Gv_uJ5iNmrsq19qraAiYOFM8q3xWNztR9GkqcDW8ss3lDnoBg-5m6ee4j8w3RNanUyeDODeL_kTP0wPxq-nQUt3VBzFn56ZF2sTh0ndM8ziHiy8DnuZM1SVPC6G4ncV3-5enGg9mQMSUj0mJwMNtLQMpn4rpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزیدنت ترامپ با انتشار نظرسنجی ای نوشت: توافقی بسیار محبوب، به جز برایِ فیک نیوز ها و شریک آنها، دوموکرات ها!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/129241" target="_blank">📅 23:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129240">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
العربیه: ولیعهد عربستان سعودی یک تماس تلفنی از سوی نخست‌وزیر پاکستان دریافت کرد.
🔴
شهباز شریف از محمد بن سلمان، ولیعهد عربستان سعودی، به‌خاطر تلاش‌هایش برای حمایت از دستیابی به یک یادداشت تفاهم میان آمریکا و ایران تشکر کرد.
🔴
ولیعهد عربستان سعودی از دستیابی به توافق میان آمریکا و ایران استقبال کرد
🔴
شاهزاده محمد بن سلمان به شهباز شریف تأکید کرد که عربستان سعودی امیدوار است آمریکا و ایران به یک توافق دائمی دست یابند
🔴
ولیعهد عربستان سعودی تأکید کرد که این کشور خواهان دستیابی آمریکا و ایران به توافقی دائمی است که ثبات منطقه را تقویت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/129240" target="_blank">📅 22:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129239">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMmhzYIwjS6I9-uqyIucDcDodFsJE2mPW-AdW-hCukK3rlXYYKEiHrVLAovEJME-_O2B8odzNTHpSjBDUzrsRysHiCh3M0BqkSBk589McD6k4lryGrH60OBE_PY1sk8k2TmvxUuuQq96B8YAcgqu30eVMEaNaNAU2K24g9TyLwv_vHGiJLM4_H_7UrYlIWrY_117w29iz6rsJ4b5_9jyHTbj8P_xbkFdfWWKB04PSzHlGa70SjKigC3uLG0XJSYGe2p8L5Ox2is_ncggchs8WMljVpdpnnLPXG848yo7qgSL_ZqWUVbMrhBKDQq31Mli3iGTsUTMPbADfZRslewh5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه انگلیس: درخواست "به آتش کشیدن تمام لبنان" یک بیانیه وحشتناک و نفرت‌انگیز از یک وزیر اسرائیلی (بن‌گویر) است که به درستی توسط دولت بریتانیا تحریم شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/129239" target="_blank">📅 22:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129238">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فیلد  مارشال ، محسن رضایی: جبهه مقاومت از همه کشورهای منطقه دفاع می‌کند علی الخصوص کشورهای همسایه فلسطین و اگر جبهه مقاومت نبود این کشورها به اشغال اسرائیل در می‌آمدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129238" target="_blank">📅 22:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129237">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8ef44e0f4.mp4?token=WxmM6ta-AygoVUQCutlJuCEa_fEsaJBo0FiZTUqtt6xIEhX-tclCGoYwsgi-taijf_Wk28tDXLJsavd_jl8mJZildSyXGu7FkjgQWfFiTNb7bdC54ru7r8zClsooPZ0V4HiGwcUddFoijISWwvaa-8xwV5-QRV0spZDpyB2jk6FHrhBq5FpWRw0qdBMdhurx28Hyr3FrbaqM3t-cPn_ibZ4i3_qnLrHxXxG3LXLDtpO6jbbKG75jzhih4fSfQvqt8igFCPjgv52lTBtqIwj0GklXJXif3Tox_lMahKyYjkDZSASfHFjnrLu6tK6R8fpb_t0WXAptwXU-oSaDBHt8Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8ef44e0f4.mp4?token=WxmM6ta-AygoVUQCutlJuCEa_fEsaJBo0FiZTUqtt6xIEhX-tclCGoYwsgi-taijf_Wk28tDXLJsavd_jl8mJZildSyXGu7FkjgQWfFiTNb7bdC54ru7r8zClsooPZ0V4HiGwcUddFoijISWwvaa-8xwV5-QRV0spZDpyB2jk6FHrhBq5FpWRw0qdBMdhurx28Hyr3FrbaqM3t-cPn_ibZ4i3_qnLrHxXxG3LXLDtpO6jbbKG75jzhih4fSfQvqt8igFCPjgv52lTBtqIwj0GklXJXif3Tox_lMahKyYjkDZSASfHFjnrLu6tK6R8fpb_t0WXAptwXU-oSaDBHt8Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره ونزوئلا و کوبا: ونزوئلا نفت دارد. کوبا ندارد. کوبا املاک زیبایی و سواحل خوبی دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/129237" target="_blank">📅 22:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129236">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c77fc55c.mp4?token=Wj3Pi28ZoyZTXRvaEbGDp4Ciqt7nZ1pxq8m5ecOKp732bC-AKn4bSDp3yWSoTmzzFH9raVr1O4yDozZlbUEKnuAxDwj7kLfVr3x0Z_IKYnAxDbE1DxAemPyyw1xtsmKZ-WD4f9cO4iiwUqBpx4Zl7QR51SctbKTG71tvKMcLoYsXgNQNIHKGSCqBugSMJp8DsRQLeHpCs68JTd5XCbj8O1JzLyl0BKO4d3zjTJhy82OQA-02uXFiwpGElkxA5FHTDsaSrYKFWA5rq66R27JeoZM_CeEs2CNB-1whP-WHGJCzqP_T3AkPvHG7N-Z7e3zFuh0-QEiZcKaZSGZ_26ia9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c77fc55c.mp4?token=Wj3Pi28ZoyZTXRvaEbGDp4Ciqt7nZ1pxq8m5ecOKp732bC-AKn4bSDp3yWSoTmzzFH9raVr1O4yDozZlbUEKnuAxDwj7kLfVr3x0Z_IKYnAxDbE1DxAemPyyw1xtsmKZ-WD4f9cO4iiwUqBpx4Zl7QR51SctbKTG71tvKMcLoYsXgNQNIHKGSCqBugSMJp8DsRQLeHpCs68JTd5XCbj8O1JzLyl0BKO4d3zjTJhy82OQA-02uXFiwpGElkxA5FHTDsaSrYKFWA5rq66R27JeoZM_CeEs2CNB-1whP-WHGJCzqP_T3AkPvHG7N-Z7e3zFuh0-QEiZcKaZSGZ_26ia9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ: من اعداد نظرسنجی عالی دارم.
🔴
من هر نامزدی که دارند را با ۲۵ امتیاز شکست می‌دهم
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/129236" target="_blank">📅 22:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129235">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده می‌گوید که «گفت و گوهایی» درباره برگزاری مذاکرات با ایران در واشنگتن دی‌سی از ۲۳ تا ۲۵ ژوئن داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129235" target="_blank">📅 22:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129234">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ : تجهیزات دفاعی و این چیزها رو داشتن
🔴
ولی هفته قبل نمی‌تونستن ببینن، یه شب ۲۵ تا کشتی داشتیم، یه شب ۲۲ تا، یه شب ۱۹ تا
🔴
یه شب ۲۱ تا هر شب همین‌طور… همه اینا. برای همین مردم می‌گفتن : این نفت از کجا میاد؟ کسی خبر نداشت
🔴
ما ساعت ۱ نصف شب حرکت می‌کردیم، همه‌جا چراغ خاموش. و نیروی دریایی‌مون هم فقط نفت می اورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/129234" target="_blank">📅 22:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129233">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507cc3233d.mp4?token=LdMKkIRkj8H3H12L0wlN2wnIWm74Hpyn6Nashb0u7XF7evaKT8cG0tzKBd3LOQYZ2j110I4eUaCe56b1Mazh8A73pXKxVklA5m9dQvwgbYNCP2VD_TyWczvsp4BEfaZeXn1Q-XBMKmBRm8_nRubsy2Eiin106Y196AZnR0xLmg224B286HVM3Oc9y4u-UtLMuLbUWp5MdaxKCyuemGSPSsPe80W6WufkXA8i418tIAOn4SVFkHnuAVFjDkFufJSyHnhURGbaW57zJoW_9y3gHFYBhoZ_a0JeUelo28RAjLkxLRJW2EwvYyti6cSK4viLG1eg0qpCY21dKCxtau-MUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507cc3233d.mp4?token=LdMKkIRkj8H3H12L0wlN2wnIWm74Hpyn6Nashb0u7XF7evaKT8cG0tzKBd3LOQYZ2j110I4eUaCe56b1Mazh8A73pXKxVklA5m9dQvwgbYNCP2VD_TyWczvsp4BEfaZeXn1Q-XBMKmBRm8_nRubsy2Eiin106Y196AZnR0xLmg224B286HVM3Oc9y4u-UtLMuLbUWp5MdaxKCyuemGSPSsPe80W6WufkXA8i418tIAOn4SVFkHnuAVFjDkFufJSyHnhURGbaW57zJoW_9y3gHFYBhoZ_a0JeUelo28RAjLkxLRJW2EwvYyti6cSK4viLG1eg0qpCY21dKCxtau-MUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره بایدن: مردی داشتیم که نمی‌توانست از یک پله هواپیما بالا برود و من نمی‌خواهم در این مورد صحبت کنم، زیرا اگر کمی لنگ بزنم، خواهند گفت: «آها، این فاجعه است.»
🔴
خوب، ممکن است اتفاق بیفتد.
🔴
اما نمی‌توانید هر بار که روی صحنه می‌روید لنگ بزنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/129233" target="_blank">📅 22:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129232">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا: روبیو به جوزف عون تأکید کرد که ضروری است حزب‌الله خلع سلاح شود و دولت کنترل خود را گسترش دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/129232" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129231">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ درباره تنگه هرمز: ما الان تنگه هرمز را کاملاً بسته داشتیم.
🔴
همه جای آن مین‌گذاری می‌شد، و موشک‌هایی بر فراز کشتی‌های میلیارد دلاری پرواز می‌کردند. آن کشتی‌ها هرگز حرکت نمی‌کردند.
🔴
ما برای ماه‌ها نفت نداشتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129231" target="_blank">📅 22:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129230">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
هم اکنون پرواز بیش از 9 هواپیمای سوخت رسان آمریکایی بر فراز تنگه هرمز و خلیج فارس.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129230" target="_blank">📅 22:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129229">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: طولانی‌ شدن جنگ علیه ایران، جهان را با رکود مواجه می‌ساخت
🔴
طولانی شدن جنگ علیه ایران برای جلب رضایت تندروها در آمریکا، ممکن بود به رکود جهانی منجر شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/129229" target="_blank">📅 22:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129228">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a5d29a6e.mp4?token=fTumd5bWCrS2vARU2cO-NHfGHZDhX0CN2ZwM0jQcXTvHSDWVhcIfaNgohgcAF7jKFLsHuXsZvNRT2dcFqq5r489fDvkBtRsqmChUKm6AsvxDbmVNaJ1PcD-X76arznw3omS96eR-7ZNqMkVUhe1KJZz9x2zL45afZ07Ot38aYjR6-pvzC5balGF3EbHimCTWjLDYzUz7jkxPa4T41VzV6-9h4eREQeh01vjI-PD9TrrOYHS8HPqm4ownFrwsFEukNhYGOiGNQrguQEcrnCK_S9GfX8KptzQ7JVmpkihFE4aIoINq7u-1ESUYoGncWJ4j5ZIMJfFTgHC3cWDTYe6IpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a5d29a6e.mp4?token=fTumd5bWCrS2vARU2cO-NHfGHZDhX0CN2ZwM0jQcXTvHSDWVhcIfaNgohgcAF7jKFLsHuXsZvNRT2dcFqq5r489fDvkBtRsqmChUKm6AsvxDbmVNaJ1PcD-X76arznw3omS96eR-7ZNqMkVUhe1KJZz9x2zL45afZ07Ot38aYjR6-pvzC5balGF3EbHimCTWjLDYzUz7jkxPa4T41VzV6-9h4eREQeh01vjI-PD9TrrOYHS8HPqm4ownFrwsFEukNhYGOiGNQrguQEcrnCK_S9GfX8KptzQ7JVmpkihFE4aIoINq7u-1ESUYoGncWJ4j5ZIMJfFTgHC3cWDTYe6IpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک کاپوتو از اکسیوس: این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
🔴
ترامپ
: خامنه‌ای جونیور با پدرش متفاوت است. آن‌ها افراد متفاوتی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/129228" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129227">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8850d1df.mp4?token=Bc1yEHIvxpDILzRB4mEIJFQneUatBURO7ghqC_RC5h23bq4SJ619TWrni2EyQxqCW0FgYbGuy4Ibi60Mh_LRn4vaqJfDs3NhwSuot9QmuoQ1c_cQapN0KHcoWHk_oFcKP0Y4sClYP4XilPPi1YlbQP51n9thtv2-aypJQt55hdzWAdT3QNTaOksKro_b-Bjnv_8_QvrRtf7U2kmxhUp-y3v6hRouB45a4GXxTAU7MI7t-zdKNjmY5zCBB46PI-dDR4jdKZ3xG9kTadnV3wj5pZj5CxKEO1pZiBWehViRCqd89AtzxyGknHRAOJx8UA5X3L-aS-dfYx_MCE76s5Urxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8850d1df.mp4?token=Bc1yEHIvxpDILzRB4mEIJFQneUatBURO7ghqC_RC5h23bq4SJ619TWrni2EyQxqCW0FgYbGuy4Ibi60Mh_LRn4vaqJfDs3NhwSuot9QmuoQ1c_cQapN0KHcoWHk_oFcKP0Y4sClYP4XilPPi1YlbQP51n9thtv2-aypJQt55hdzWAdT3QNTaOksKro_b-Bjnv_8_QvrRtf7U2kmxhUp-y3v6hRouB45a4GXxTAU7MI7t-zdKNjmY5zCBB46PI-dDR4jdKZ3xG9kTadnV3wj5pZj5CxKEO1pZiBWehViRCqd89AtzxyGknHRAOJx8UA5X3L-aS-dfYx_MCE76s5Urxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره حمله به پل B1: من بزرگترین پل آن‌ها را نابود کردم چون دیر در یک جلسه حاضر شدند. آن‌ها گفتند که کار خیلی خوبی نبود.
🔴
آن پل، [همانند] پل جورج واشنگتن آن‌ها بود. آن را در سه دقیقه پاک کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129227" target="_blank">📅 22:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129226">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938ae8cd57.mp4?token=EE0OoXyyRtqNgIt026iZlRL2MwZ8mxZg8i_VO7RTC577GeIkiu2avCZVdsuma_F3IRd3VPZ6qydFMeGxT3raB9ru8YqsN1q4OsVkrNa-jXFB-KgAGm5pICywEq8wP5hpVOXJCD3tIXoFQ6m7z7o0RiuD6no5HXSBAgpY6RqrKxaZH1HwWp6g7adSdDYNDb0o3U-ZnBBC4fca4wqO1ZjgSUfjXCuvZtRPzuM6pRlsSf0-yp-ZBlJZDK8dfj0ekzAy--51pSV6JgKnNzemGhfvNLWdfrlfB5Eq29FIY8ToXlh_sHGBDBzDxEsAbNpYYdNOwJPsg1q3WizIK5l2ePjqWCMi50uHZ0INfKIbBADHG-FwgXQ0FHPa8zvz4QwKKppvqsyWKZoAxVYKi7n6vv_qZrzgjRJz6A2hTqvBM_t-on1fdeJLXoSGVeGLO6dyC3YObAN9b6xrNcgF0bXdrc3cH6UuvDkaDUH4w5WFwWE4e1q-p5NPbWjs7KVeQk16k25KwlSyzPy2yNU5vmrIj4J-e-dr3gl43-pHaR7OIng5HwuKPLuUXIGgiUoFrEQwSH54ZWkRVIja0-EVNYvInZ21s08PyG5OoCKwBINxKwmtglBl0csyaH-iTqCvlh-mDaevyDiTMANZGoLhX4EldXekXD8p6HJzUebh8EUWoBKYkQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938ae8cd57.mp4?token=EE0OoXyyRtqNgIt026iZlRL2MwZ8mxZg8i_VO7RTC577GeIkiu2avCZVdsuma_F3IRd3VPZ6qydFMeGxT3raB9ru8YqsN1q4OsVkrNa-jXFB-KgAGm5pICywEq8wP5hpVOXJCD3tIXoFQ6m7z7o0RiuD6no5HXSBAgpY6RqrKxaZH1HwWp6g7adSdDYNDb0o3U-ZnBBC4fca4wqO1ZjgSUfjXCuvZtRPzuM6pRlsSf0-yp-ZBlJZDK8dfj0ekzAy--51pSV6JgKnNzemGhfvNLWdfrlfB5Eq29FIY8ToXlh_sHGBDBzDxEsAbNpYYdNOwJPsg1q3WizIK5l2ePjqWCMi50uHZ0INfKIbBADHG-FwgXQ0FHPa8zvz4QwKKppvqsyWKZoAxVYKi7n6vv_qZrzgjRJz6A2hTqvBM_t-on1fdeJLXoSGVeGLO6dyC3YObAN9b6xrNcgF0bXdrc3cH6UuvDkaDUH4w5WFwWE4e1q-p5NPbWjs7KVeQk16k25KwlSyzPy2yNU5vmrIj4J-e-dr3gl43-pHaR7OIng5HwuKPLuUXIGgiUoFrEQwSH54ZWkRVIja0-EVNYvInZ21s08PyG5OoCKwBINxKwmtglBl0csyaH-iTqCvlh-mDaevyDiTMANZGoLhX4EldXekXD8p6HJzUebh8EUWoBKYkQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره آیت‌الله مجتبی خامنه‌ای:
من آیت الله را کشتم و متأسفانه آیت الله دیگر را آزار دادم.
🔴
من او را ملاقات نکردم. من با او صحبت نکردم، اما مردم از او صحبت می کردند.
🔴
اما او شجاعت خاصی دارد زیرا به شدت مجروح شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129226" target="_blank">📅 22:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129225">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ درباره گروه هفت: باید گروه هشت را حفظ می‌کردند.
🔴
اگر این کار را می‌کردند، احتمالاً جنگی بین روسیه و اوکراین وجود نداشت، اما اوباما نمی‌خواست پوتین آنجا باشد.
🔴
قبلاً گروه هشت بود. اگر آن را همان‌طور حفظ می‌کردند، بسیار بهتر می‌شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/129225" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129224">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b68770a38.mp4?token=acclOcrLFvmOIJAIpQLpuvehTDdDIjgENSGI6Ty9din_jRgQZRh12cZIYing-KmTnjH33PPZgc5LgHoiVSID6Uy7dEVgrmfbGeEgMCiZgrS6_vOczYVRfAfWK-WN0TRGOWyrZs86ovYY3FfbpADWxEPqgQ06W7XXesRvJiPO7lT19iQHUnsPNG4GTxR1FBoeyRw-U30aE_PJ03Znx92eNqsM1nYd7QqRne55Q1UA9UP3XPSfNkyMMzGLl8nIY_HG6b_gcTxEouuzvj_G8NNLDuNdoyx300_FIzI2mXZFTN34B1Xbb8uYNpQMyg5eKDoIF6RJPGAIb4ocYeinlXEW45qESPplCsmScnMMwIHgw7PL5Wzgbvu4cXJOlN57ddO04DXqDFApluub90gYmTmvB0wlWXk5OoZrlPnQ7KCXeM7qXvY0POTkZpvtEfCq_xDfN65IK6BZNM63NoYYn2F8Lo0X5WAASJBFtzepHhr-wM4naLKsJ1bohH6aQ5w5XBQUZtPDuDoJW-iRbXm0zWsLxGCiPJre8-8An70zq4IUsBHjNkGUpmLxqYZbiXLhiKDQdE0Ba3c3GsCXy3VDmURGzRuF8tpa6NucwTxnXxADMYtad1XeHLelFUoG1j-p-XF1FI5W83svQlRYJlcPfbEqpLpxqM3Pul2aV_M7Sh31s8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b68770a38.mp4?token=acclOcrLFvmOIJAIpQLpuvehTDdDIjgENSGI6Ty9din_jRgQZRh12cZIYing-KmTnjH33PPZgc5LgHoiVSID6Uy7dEVgrmfbGeEgMCiZgrS6_vOczYVRfAfWK-WN0TRGOWyrZs86ovYY3FfbpADWxEPqgQ06W7XXesRvJiPO7lT19iQHUnsPNG4GTxR1FBoeyRw-U30aE_PJ03Znx92eNqsM1nYd7QqRne55Q1UA9UP3XPSfNkyMMzGLl8nIY_HG6b_gcTxEouuzvj_G8NNLDuNdoyx300_FIzI2mXZFTN34B1Xbb8uYNpQMyg5eKDoIF6RJPGAIb4ocYeinlXEW45qESPplCsmScnMMwIHgw7PL5Wzgbvu4cXJOlN57ddO04DXqDFApluub90gYmTmvB0wlWXk5OoZrlPnQ7KCXeM7qXvY0POTkZpvtEfCq_xDfN65IK6BZNM63NoYYn2F8Lo0X5WAASJBFtzepHhr-wM4naLKsJ1bohH6aQ5w5XBQUZtPDuDoJW-iRbXm0zWsLxGCiPJre8-8An70zq4IUsBHjNkGUpmLxqYZbiXLhiKDQdE0Ba3c3GsCXy3VDmURGzRuF8tpa6NucwTxnXxADMYtad1XeHLelFUoG1j-p-XF1FI5W83svQlRYJlcPfbEqpLpxqM3Pul2aV_M7Sh31s8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مکرون: مکرون کار عالی در میزبانی از گروه هفت انجام داد. واقعاً خوب. بازی‌های خوبی بود.
🔴
او حدود یک هفته قبل از من دعوت کرد. گفت، «آیا می‌توانی به من لطفی کنی؟ آیا به پاریس می‌آیی؟ ما دوست داریم تو را گرامی بداریم.»
🔴
من آن را به عنوان احترام به کشور در نظر گرفتم. اما او گفت، «من دوست دارم تو را گرامی بدارم.»
🔴
و او برخی از بزرگترین افراد اروپا و فراتر از آن را آنجا داشت و ما در ورسای بودیم و من نوعی قصد انجام آن را نداشتم، اما او ضعف من را می‌دانست.
🔴
آن‌ها شام‌هایی در ورسای برگزار می‌کنند.
🔴
ما شام فوق‌العاده‌ای داشتیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/129224" target="_blank">📅 22:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129223">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7148359604.mp4?token=jYKS6Qik1D281ltY0HLlE_cGbMwBugj8Bw8J7iQuGoQYwhmBqe7rNBNZGoi2v0GfkvWPplAITALQAnWSLUtBpwLKjHyizSAKL1MKcnfKRSCKelCXh8FAbV984YbmzDhDlTZpRsPgmdHpKpTm59yb2ufI___gww-uROSRbm67ta6ZiDJCw4KYje0t1FzOmo-kFtGp5AC97vJL6MT9H7Y7ILytjngas-PpCrOrM2QSRvsedqdpIbyuPHCoAIAHNMhp8rtTvIGV97S7IzK8gwUUkwAbKShfFebAyU2xjEryqm-iDB48wtxTz6xYOKzC0SqZUbJ_wKdCWfLs9MCRAfgw-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7148359604.mp4?token=jYKS6Qik1D281ltY0HLlE_cGbMwBugj8Bw8J7iQuGoQYwhmBqe7rNBNZGoi2v0GfkvWPplAITALQAnWSLUtBpwLKjHyizSAKL1MKcnfKRSCKelCXh8FAbV984YbmzDhDlTZpRsPgmdHpKpTm59yb2ufI___gww-uROSRbm67ta6ZiDJCw4KYje0t1FzOmo-kFtGp5AC97vJL6MT9H7Y7ILytjngas-PpCrOrM2QSRvsedqdpIbyuPHCoAIAHNMhp8rtTvIGV97S7IzK8gwUUkwAbKShfFebAyU2xjEryqm-iDB48wtxTz6xYOKzC0SqZUbJ_wKdCWfLs9MCRAfgw-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره پاکستان: در پاکستان، شما فرمانده کل قوا را دارید که عالی است. و نخست‌وزیر را دارید و آن‌ها با هم بسیار خوب کنار می‌آیند.
🔴
مرد نظامی کاملاً به نخست‌وزیر احترام می‌گذارد.
🔴
دیدن این موضوع زیباست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/129223" target="_blank">📅 22:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129222">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا: روبیو به جوزف عون تأکید کرد که ضروری است حزب‌الله خلع سلاح شود و دولت کنترل خود را گسترش دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/129222" target="_blank">📅 22:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129221">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9501f33214.mp4?token=njFtNPw_cZCJ-I5Vkmzumf2qwtpTh8gpTUsXnIowg72MEtswmXO4MUE5qYzAJ1drbvsiYIPL7CgMCSsd2WKgmmAJEaxAB1ebYlwVlkbCx2Y9jQ7a9pUwxrXII3nMnJKsW1qu_-3q700jkuH6QGNn-4xpanhfHb25fq2vxeG9S3nGYg0eNuT4jYUEZ09H_fMrRZLymY8uw6fQT33PBWCkmigmnwNmbYbMnmQn_yAHDRq0xUwEbb4cZkcxng7qLQkSZfqSIcJsOexftIr2axyc3R6nCX0BsmQJM9YGWZ34JUtlH9zlEcAxqrZ8EZ1D6tS2Eo6V_pTi70olDwLlE-fZ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9501f33214.mp4?token=njFtNPw_cZCJ-I5Vkmzumf2qwtpTh8gpTUsXnIowg72MEtswmXO4MUE5qYzAJ1drbvsiYIPL7CgMCSsd2WKgmmAJEaxAB1ebYlwVlkbCx2Y9jQ7a9pUwxrXII3nMnJKsW1qu_-3q700jkuH6QGNn-4xpanhfHb25fq2vxeG9S3nGYg0eNuT4jYUEZ09H_fMrRZLymY8uw6fQT33PBWCkmigmnwNmbYbMnmQn_yAHDRq0xUwEbb4cZkcxng7qLQkSZfqSIcJsOexftIr2axyc3R6nCX0BsmQJM9YGWZ34JUtlH9zlEcAxqrZ8EZ1D6tS2Eo6V_pTi70olDwLlE-fZ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من برزیل را تماشا کردم، رهبری که کمی او را می‌شناسم. او فردی بسیار ناپایدار است.
🔴
کاپوتو: شما طرفدار لولا نیستید، اگر اشتباه نکنم.
🔴
ترامپ: فکر نمی‌کنم درباره او فکر کنم، صادقانه با شما بگویم. واقعاً درباره او فکر نمی‌کنم. برام مهم نیست.
🔴
اما او اکنون نوع متفاوتی از فرد است. بسیار ناپایدار. تماشا کردم که او سخنرانی کرد. بسیار ناپایدار بود و اشکالی ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/129221" target="_blank">📅 22:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129220">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ : کار فوق‌العاده‌ای کردم؛تو دوره اول ریاست‌جمهوریم
🔴
ارتش رو از نو ساختم و حسابی تقویتش کردم. یه نگاهی هم به ونزوئلا بندازید؛ کل ماجرا تو ۴۸ دقیقه جمع شد
🔴
روابطه‌هاشون این‌طوریه، و ما هزینه‌ی اون جنگ با ونزوئلا رو چندین و چند بار دادیم
🔴
الان هم داریم میلیون‌ها بشکه نفت ازشون درمیاریم و حتی داریم کاری می‌کنیم که بیشتر از قبل براشون پول دربیاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/129220" target="_blank">📅 21:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129219">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2593101003.mp4?token=Bfw9i6pCNt0xl04r3brLoNEE8UoAyBnjhL5sTV2nyjfBvrJ8W_kX7TJj3o2Q97X2DKIV7MmXLo10p10Uz4dGrpl0cNxMJDZi1n9-HEe9_In6wnvtq6Qkd2nnwNpfHAh2d45xGOJTygbSlYcjY4KRUB8l_0LMYms8Ja7Zg5bizGCZEawLLhJ1lgra20IMnpRCyCTdHNIwnfb9FRE4faJ-F7y8SQZMSckksVM3KQhYxE0WbnXzmhnaaqOFO8-OYGo4nApy95uMpsptM060eiVSeGMjW_GAh0eKj9PQ6ptsA750MYod7N2LYXf2L6BWIFzDqF0PRk5OozX6XoxktrmASA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2593101003.mp4?token=Bfw9i6pCNt0xl04r3brLoNEE8UoAyBnjhL5sTV2nyjfBvrJ8W_kX7TJj3o2Q97X2DKIV7MmXLo10p10Uz4dGrpl0cNxMJDZi1n9-HEe9_In6wnvtq6Qkd2nnwNpfHAh2d45xGOJTygbSlYcjY4KRUB8l_0LMYms8Ja7Zg5bizGCZEawLLhJ1lgra20IMnpRCyCTdHNIwnfb9FRE4faJ-F7y8SQZMSckksVM3KQhYxE0WbnXzmhnaaqOFO8-OYGo4nApy95uMpsptM060eiVSeGMjW_GAh0eKj9PQ6ptsA750MYod7N2LYXf2L6BWIFzDqF0PRk5OozX6XoxktrmASA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره نیویورک‌تایمز : کمی پیش حقیقتی را بیان کردم. گفتم: «اگر (مقامات ایران) پرچم سفید تسلیم را بالا می‌بردند و می‌گفتند: "سپاس خداوند را، ترامپ بزرگترین رئیس‌جمهور است، ما در اینجا تسلیم می‌شویم"،» نیویورک تایمز می‌نوشت که آن‌ها جنگ را برده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129219" target="_blank">📅 21:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129218">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d60f7b5da.mp4?token=JA9KpakMXpOpZH_r7tUztSEe44pizdc9qup_3wffta0fUEFT9BdYQD5AjCcllPUhEF3Tt_e3ZeclpWaxkc4QcWlmN4dD_sSDFdjXGiQF-zk8E99N6OxnBJzbchewTo0vy6PfkV1EG8uHv8g-dTJRVpYwAlTdIvZbGKS4tCEUmQbn2Qq29FaZjLCCoXKD96NTf_cD01ygu97KpbFx8WG-1vBpGk2o--OQ15aYaJkzXVW9ZIOZRVqMIFQWqpgznkQpp-iEiLXCjMzDKcBEvlk5SKX8B0a7x2bW6F6O799uOGAM-bJJFGsqW59ZHjlcklEEj9MPDeWwrLqDnxJ-AojTAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d60f7b5da.mp4?token=JA9KpakMXpOpZH_r7tUztSEe44pizdc9qup_3wffta0fUEFT9BdYQD5AjCcllPUhEF3Tt_e3ZeclpWaxkc4QcWlmN4dD_sSDFdjXGiQF-zk8E99N6OxnBJzbchewTo0vy6PfkV1EG8uHv8g-dTJRVpYwAlTdIvZbGKS4tCEUmQbn2Qq29FaZjLCCoXKD96NTf_cD01ygu97KpbFx8WG-1vBpGk2o--OQ15aYaJkzXVW9ZIOZRVqMIFQWqpgznkQpp-iEiLXCjMzDKcBEvlk5SKX8B0a7x2bW6F6O799uOGAM-bJJFGsqW59ZHjlcklEEj9MPDeWwrLqDnxJ-AojTAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره رسانه‌های داخلی جمهوری اسلامی ایران
:
اگر به ایران نگاه کنید، آن‌ها ۴۷ سال است که این کارها را انجام می‌دهند.
🔴
آن‌ها شما و همه دیگران را تحقیر کرده‌اند، تمام رسانه‌ها و همه چیز.
🔴
آن‌ها در برخورد با مطبوعات بسیار خوب عمل می‌کنند. آن‌ها رسانه‌ای جعلی(فیک) و عالی دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129218" target="_blank">📅 21:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129217">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5a6eab44.mp4?token=UoGI0cjKxrQrdFEWmIf-jVdl9iNgpeSF3KyzuARw4TkCGRhB-UzjxdNvH6AgWAYxxJkNmUCIfFbpRsrswc0ZzSdVLfTQSdxtSszSPPEEAs7bxE_GzeA-x1sEHCme-jJ_MlptTJK-vCG11Rzf-x4fN9gZiF03jdg-qdB5GYA8VZf_eXu8d3O2QMhR1W8vxpZI-dwRU-9MTiqczl3wrQPNKF54o17l0Gr3Pot6ZnQ9-hMW0-7TiNgCs5kx5kyuLs4sRb1ZEU9xaI8Ym-BtXaPYmMZXkNvdlkKE2yV5aijPp-3vyCpiafrTb2lscmqWw0Yg1o1cOiQoCyX4X2Ml1ITAU2xlG-rFhMkjo4CHB2zrVP6Hdxl4HxBZzOylQI-12txQusmgG84fkZfE06zThwH4wKqPuIZLfS5C9_KphEfqexXNbYd5byGKKwAOrPvz6pJpr0QDIMtOyNj08GJngzrzqIQjZMCoKM_4d3OYAMdgdAbGob6JpDagDOMXiFisjn1G4SD2xYMYA6qBth18umje32VVWrqrpcFYBPApV1uq8GS-5V64yLL0exYwWMdxr93tM6O5ws2RNdkavWSJ7kFUGMoRedodAJKuJGatTE8sBZeDMKbqoJa1V_Rrev9Id7psE2OpcyNdF2L4fUloVf45AuwG2m9f4D-tzOgiHBX62Vk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5a6eab44.mp4?token=UoGI0cjKxrQrdFEWmIf-jVdl9iNgpeSF3KyzuARw4TkCGRhB-UzjxdNvH6AgWAYxxJkNmUCIfFbpRsrswc0ZzSdVLfTQSdxtSszSPPEEAs7bxE_GzeA-x1sEHCme-jJ_MlptTJK-vCG11Rzf-x4fN9gZiF03jdg-qdB5GYA8VZf_eXu8d3O2QMhR1W8vxpZI-dwRU-9MTiqczl3wrQPNKF54o17l0Gr3Pot6ZnQ9-hMW0-7TiNgCs5kx5kyuLs4sRb1ZEU9xaI8Ym-BtXaPYmMZXkNvdlkKE2yV5aijPp-3vyCpiafrTb2lscmqWw0Yg1o1cOiQoCyX4X2Ml1ITAU2xlG-rFhMkjo4CHB2zrVP6Hdxl4HxBZzOylQI-12txQusmgG84fkZfE06zThwH4wKqPuIZLfS5C9_KphEfqexXNbYd5byGKKwAOrPvz6pJpr0QDIMtOyNj08GJngzrzqIQjZMCoKM_4d3OYAMdgdAbGob6JpDagDOMXiFisjn1G4SD2xYMYA6qBth18umje32VVWrqrpcFYBPApV1uq8GS-5V64yLL0exYwWMdxr93tM6O5ws2RNdkavWSJ7kFUGMoRedodAJKuJGatTE8sBZeDMKbqoJa1V_Rrev9Id7psE2OpcyNdF2L4fUloVf45AuwG2m9f4D-tzOgiHBX62Vk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به اکسیوس: اگر دونالد ترامپ نبود، اسرائیل کاملاً نابود می‌شد.
🔴
ما کسانی هستیم که اسلحه‌ها را داریم. ما کسانی هستیم که کل توافق را داریم. ما کسانی هستیم که بمب‌افکن‌های بی-۲ و غیره را داریم.
🔴
رابطه با نتانیاهو... خوب است، اما باید او را کمی عاقل‌تر نگه داریم.
🔴
سوال
: آیا می‌توانید از حمله اسرائیل به لبنان جلوگیری کنید؟
🔴
ترامپ:  بله، من می‌توانم. آن‌ها برای من احترام زیادی قائل هستند و همان‌طور که من می‌گویم عمل می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/alonews/129217" target="_blank">📅 21:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129216">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76380d5ba7.mp4?token=BxdJSbBWLHqoqcP2-BN2r-d79MPDBNqEZBUvZRuLd_lc8jUpZyC7e72OU9zANy7Dtbab2AT3csCf9NksSMg2OffJhYYYHKV5doPSUnoSw_oZdxvGBJmbtJedS-3QeRv5zZmcuDjHvEPQDzbAr3vuGR2_R_TwIinH46jsPfV9fY_3dwjuzUgPiRthg9vmRUOZ1hIuieJjlXCdH7h6xt3F1c6HA_EDJ1-bPJzlVj5uv8YdWa6ofH_F_UAZ51V1wwxUkyiF2mdedeKjNngaiU5h-Hc7Nirvg1uWSvGv-ca31GSnGJgdJUYzyAqFewizuxG9rUYYjfEkA8YPD0k1fFm8iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76380d5ba7.mp4?token=BxdJSbBWLHqoqcP2-BN2r-d79MPDBNqEZBUvZRuLd_lc8jUpZyC7e72OU9zANy7Dtbab2AT3csCf9NksSMg2OffJhYYYHKV5doPSUnoSw_oZdxvGBJmbtJedS-3QeRv5zZmcuDjHvEPQDzbAr3vuGR2_R_TwIinH46jsPfV9fY_3dwjuzUgPiRthg9vmRUOZ1hIuieJjlXCdH7h6xt3F1c6HA_EDJ1-bPJzlVj5uv8YdWa6ofH_F_UAZ51V1wwxUkyiF2mdedeKjNngaiU5h-Hc7Nirvg1uWSvGv-ca31GSnGJgdJUYzyAqFewizuxG9rUYYjfEkA8YPD0k1fFm8iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره شی: او مردی قوی است. او بازی نمی‌کند. او نمی‌نشیند و نمی‌گوید: «آها، چه روز زیبایی. به خورشید نگاه کنید.»
🔴
هیچ‌کدام از آن چیزها وجود ندارد. همه چیز جدی و کاری است که من دوست دارم. فکر می‌کنم عالی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/alonews/129216" target="_blank">📅 21:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129215">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427ccd23df.mp4?token=ptDl_m0uirKzuQQ_djR0OyMwF_OsDzOa-9eRBSH5VAMggi5CoVRvAQvugkYVIfoggj9LlYcyCKU-1mm6_81we-VW-pAj0eZ1TgMJ-ZfyaCpQdhfZGGoxQxXDHUkePhywd6y0qPx7GvEw7Dl4_C52vapOFBATiLXFyohJPLYGIUMINGnmrLQErzojzdE8jpiF7H_EAw9iuUeznMdqtGORvD-Kaqd49sIY9HPKmuoeXMRLagyBstvGPusjVnyXDGWbpnSC5PVyepBiI-5dYARa87h3GRyThCevFfnTkYiwnq0qwoncyN9nUkoAZwRnKnj4ekUADXYONODBRYLbP-z5PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427ccd23df.mp4?token=ptDl_m0uirKzuQQ_djR0OyMwF_OsDzOa-9eRBSH5VAMggi5CoVRvAQvugkYVIfoggj9LlYcyCKU-1mm6_81we-VW-pAj0eZ1TgMJ-ZfyaCpQdhfZGGoxQxXDHUkePhywd6y0qPx7GvEw7Dl4_C52vapOFBATiLXFyohJPLYGIUMINGnmrLQErzojzdE8jpiF7H_EAw9iuUeznMdqtGORvD-Kaqd49sIY9HPKmuoeXMRLagyBstvGPusjVnyXDGWbpnSC5PVyepBiI-5dYARa87h3GRyThCevFfnTkYiwnq0qwoncyN9nUkoAZwRnKnj4ekUADXYONODBRYLbP-z5PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
اگر ما آنها را نمی زدیم، آنها یک سلاح هسته ای داشتند.
🔴
آنها از آن برای اسرائیل استفاده می کردند.  شما از آن در عربستان سعودی نیز استفاده می کردید.
🔴
تقریباً بلافاصله موشک ها به سمت این پنج کشور دیگر (قطر، امارات، کویت، بحرین) پرواز کردند.
🔴
گفتم چرا این کار را می کند؟
🔴
و میدونی چیکار کرد؟
🔴
این پنج کشور را به دامان من آورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/129215" target="_blank">📅 21:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129214">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a75bf31b4.mp4?token=q_f3-FEzSB7JrRoPVcnWEuCPfrLm_zHP0eL68WUBpVMm7SbrC4CioLlvG65M39S4r0VL2KGm4Uu_Hcbd1jIrKGwjNhPyduUhuUPwMf4zpSAk0sXm5tvKXth8l22BYmCsAuFrlA1UDzcYGiYS-NOn-CpRBP1xscqBG4SHIEdIFykIJK6XMI91H3voUmnGLbYGuS1zImW1C6aB3ihBc31i-bdhUK7PvQpyqvDgL4DOF-SrA5y5J69_i9j6gCkdRQ42av1JH6hMHs1UVvRBKl44o62EPQgV_TeQd_Qh7c9l17Wwv2Ze6V-lxlFF9b1q4yuzzO3V1Txuc8kumUFbkoHOQa-cf4KVlM_k3mmPEtazKgyE9MjwiX7HDOC4ZvKOAforTcK8nt2TgvTmb6VeTJ-wafop1IQcL2jge1q2HNhUCVE3oH_kSGpEio-fALdKwxr360AkvwXu_lRwl4qhRdjbNopP2ShO42X4WPyMn5MrgIrJ8G0fABW5Dw_-re6wB3QIZxARaWaJ9TnEMbxvSbO9pyLIq9b5XNT83iwdl3PJcIUgJniajHa7YAXKA_c1yBmGGCWHoo4ScuRtvmumpW_arrHvP5seekqQW21ihZUyCBKMEC0vRvN2UBIk1x-IzBnJF6DHcqH6hJK8CIoyvZD0Y7FpltDIG2Hi2xNVjvcrywI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a75bf31b4.mp4?token=q_f3-FEzSB7JrRoPVcnWEuCPfrLm_zHP0eL68WUBpVMm7SbrC4CioLlvG65M39S4r0VL2KGm4Uu_Hcbd1jIrKGwjNhPyduUhuUPwMf4zpSAk0sXm5tvKXth8l22BYmCsAuFrlA1UDzcYGiYS-NOn-CpRBP1xscqBG4SHIEdIFykIJK6XMI91H3voUmnGLbYGuS1zImW1C6aB3ihBc31i-bdhUK7PvQpyqvDgL4DOF-SrA5y5J69_i9j6gCkdRQ42av1JH6hMHs1UVvRBKl44o62EPQgV_TeQd_Qh7c9l17Wwv2Ze6V-lxlFF9b1q4yuzzO3V1Txuc8kumUFbkoHOQa-cf4KVlM_k3mmPEtazKgyE9MjwiX7HDOC4ZvKOAforTcK8nt2TgvTmb6VeTJ-wafop1IQcL2jge1q2HNhUCVE3oH_kSGpEio-fALdKwxr360AkvwXu_lRwl4qhRdjbNopP2ShO42X4WPyMn5MrgIrJ8G0fABW5Dw_-re6wB3QIZxARaWaJ9TnEMbxvSbO9pyLIq9b5XNT83iwdl3PJcIUgJniajHa7YAXKA_c1yBmGGCWHoo4ScuRtvmumpW_arrHvP5seekqQW21ihZUyCBKMEC0vRvN2UBIk1x-IzBnJF6DHcqH6hJK8CIoyvZD0Y7FpltDIG2Hi2xNVjvcrywI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ مجدداً از شی تشکر کرد: شی در کل ماجرای ایران دخالت نکرد. می‌توانست دخالت کند. می‌توانست یک کشتی نفتی را که توسط ۱۲ ناوشکن احاطه شده بود بفرستد و ببیند آیا می‌تواند راهی برای شکستن محاصره پیدا کند یا خیر.
🔴
اما رئیس‌جمهور شی، از او پرسیدم و گفتم: «واقعاً ممنون می‌شوم اگر دخالت نکنید.» و او عالی بود. دخالت نکرد.
🔴
و فکر می‌کنم اگر شخص دیگری این را می‌گفت، فکر نمی‌کنم کسی حتی از او چنین درخواستی می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/129214" target="_blank">📅 21:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129213">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ
:
ایرانی ها، مردم بسیار باهوشی هستند. آنها نوعی نابغه ابتدایی هستند، اما باهوش هستند.
🔴
آنها اسرائیل را منفجر می کردند.
🔴
اگر من نبودم، امروز اسرائیل وجود نداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/129213" target="_blank">📅 21:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129212">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/821720cf8d.mp4?token=gR07FM1ovo0_P_fDNytoJS89FUNXPlC74m7-W4O-nKdUGyijqgH0-LSYo0ZBt5mYIufNxJSxfrM0Qrejf6px9odNuuPY2c4pUv4TMQNPaYRO3-pfm5LdKPDtF6QrsZpJQdz57KDF8IJ66pPJrE-YVjAVhrO6fFMkZ6wtMWMiWRuQUtvvUZZh_L9lT7Ld6ocSuclFqAHDye4K5z2rnquFDLoRP8ZM-irSEjJEB1NmqWeoJIXQ1Bf3og8QtoV-FSBY3p8qRHEa0iml7wslnuNQmSrjeYTk0hyWIR5NoeE6oLLmGoQtJb8QCzEGIFkaa0L8RzxpTw-zHh4kv6MipT8CYYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/821720cf8d.mp4?token=gR07FM1ovo0_P_fDNytoJS89FUNXPlC74m7-W4O-nKdUGyijqgH0-LSYo0ZBt5mYIufNxJSxfrM0Qrejf6px9odNuuPY2c4pUv4TMQNPaYRO3-pfm5LdKPDtF6QrsZpJQdz57KDF8IJ66pPJrE-YVjAVhrO6fFMkZ6wtMWMiWRuQUtvvUZZh_L9lT7Ld6ocSuclFqAHDye4K5z2rnquFDLoRP8ZM-irSEjJEB1NmqWeoJIXQ1Bf3og8QtoV-FSBY3p8qRHEa0iml7wslnuNQmSrjeYTk0hyWIR5NoeE6oLLmGoQtJb8QCzEGIFkaa0L8RzxpTw-zHh4kv6MipT8CYYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مودی: مودی بسیار خوب است. او از جنگ‌ها دوری می‌کند که هوشمندانه است. ۱.۵ میلیارد جمعیت دارند. هند در واقع بزرگترین است. مودی رهبر بزرگی است و ما تجارت زیادی با آن‌ها داریم، اما اکنون تجارت عادلانه انجام می‌دهیم.
🔴
آن‌ها قبلاً واقعاً ما را کلاهبرداری می‌کردند. من آن‌ها را به خاطر این مورد سرزنش نمی‌کنم. ما سیاستمداران احمقی داشتیم که اجازه دادند این اتفاق بیفتد.
🔴
اما اکنون تجارت زیادی انجام می‌دهیم. آن‌ها از این موضوع آن‌قدرها خوشحال نیستند. آن‌ها قبلاً خیلی بهتر عمل می‌کردند. اما مودی عالی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/129212" target="_blank">📅 21:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129211">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سلام، نخست وزیر لبنان: ایران زور اتش بس آوردن برای لبنان را ندارد. این امر فقط توسط دولت و با خلع سلاح حزب الله محقق می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/129211" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129210">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4536cbb7a0.mp4?token=VZEvjO8UVJnO37Mgz6MzPiaAti61Eplw8-cFxDS9IOmluWCtK36NAdwSHCulUa6K2FnucEcjx4xy2rL2y_N2EWXgVDaNE3yDkoBXzcCPiTFE9NU_z_cny8UgXL8CfXRryrS-fNWDiJ2ItpyZ5n0KkhoCeeHpZUugMAOGjVdeHE_tqKbqMpavCMaJCXaMa0Vlfyaa2DwdnGO1AD6c0-eBsHbtHEdniq3XXQn1DB4y-q2bAVSZf3lpnxeKn4YxC-9YTNRy1DzjiVTtXzP1pixNgsJ7BXTwT5e8eWDyz2Tj0_o0QNvVyzo3vcYIshAmuR1D6_gEgmUq0r7n3QUIbFEmdoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4536cbb7a0.mp4?token=VZEvjO8UVJnO37Mgz6MzPiaAti61Eplw8-cFxDS9IOmluWCtK36NAdwSHCulUa6K2FnucEcjx4xy2rL2y_N2EWXgVDaNE3yDkoBXzcCPiTFE9NU_z_cny8UgXL8CfXRryrS-fNWDiJ2ItpyZ5n0KkhoCeeHpZUugMAOGjVdeHE_tqKbqMpavCMaJCXaMa0Vlfyaa2DwdnGO1AD6c0-eBsHbtHEdniq3XXQn1DB4y-q2bAVSZf3lpnxeKn4YxC-9YTNRy1DzjiVTtXzP1pixNgsJ7BXTwT5e8eWDyz2Tj0_o0QNvVyzo3vcYIshAmuR1D6_gEgmUq0r7n3QUIbFEmdoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس در مورد توافق ایران:
منتقدانی از این توافق بودند که می‌گفتند ایرانی‌ها هرگز اجازه نمی‌دهند تنگه‌ها بدون عوارض باز باشند.
🔴
در دو روز گذشته، ایرانی‌ها به هیچ کشتی شلیک نکرده‌اند.
🔴
دیروز، ما از تنگه هرمز نفت بیشتری نسبت به هر زمان دیگری از آغاز درگیری خارج کردیم. و حتی یکی از این کشتی‌ها عوارض پرداخت نکرد.
🔴
بنابراین، منتقدان این توافق در مورد برخی از آنچه می‌گویند ایرانی‌ها به دست آورده‌اند، و همچنین در مورد آنچه ایالات متحده به دست آورده است، اشتباه می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/129210" target="_blank">📅 21:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129209">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
اوباما در مورد توافق: توافقی در حال اجرا بود که در آن ایران توافق کرده بود که سلاح‌های هسته‌ای توسعه ندهد.
🔴
این دولت — یا نسخه‌ای قبلی از این دولت — از آن خارج شد، که باعث شد ایران در آن زمان ظرفیت هسته‌ای بیشتری توسعه دهد.
🔴
ما اکنون جنگیده‌ایم، میلیاردها و میلیاردها دلار هزینه کرده‌ایم، فشار عظیمی بر ارتش خود وارد کرده‌ایم، بسیاری از مردم کشته شده‌اند و به نظر می‌رسد که به جایی که قبل از شروع جنگ بودیم بازگشته‌ایم، شاید حتی کمی بدتر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/129209" target="_blank">📅 21:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129208">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e467c88758.mp4?token=A2LMOgz1jRuHD1WH69CF78hXhPIcDKZt2iA3vwpB84HQV65VsjtM0RW4VA8gDbCmKse4Ut0F0srQhIUMnrUG5xJnC83RZhxU_RFhz1ZtfWZnP2MM03qJy2Gv_id2UjMXJFqgrqa5tYFQ1AWv2HsRyB5L4wY1ruG8aR7aZS2fSIQKceJwV3ibqzmpstoDFmEvPspATZFxXKApOnb8r3GVYPLe7qghoFRA5UNFqmkoBseC3_P15Gv2cKW1rpQtKEkYAwS3IIdqpOsM_taYoBkDwf6CLOhDXVl_oXnBjH8ZBgWOQDB0wv654Vb1QkU-Bwl5rvHQ7JeMxxWxyy5oBlnlDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e467c88758.mp4?token=A2LMOgz1jRuHD1WH69CF78hXhPIcDKZt2iA3vwpB84HQV65VsjtM0RW4VA8gDbCmKse4Ut0F0srQhIUMnrUG5xJnC83RZhxU_RFhz1ZtfWZnP2MM03qJy2Gv_id2UjMXJFqgrqa5tYFQ1AWv2HsRyB5L4wY1ruG8aR7aZS2fSIQKceJwV3ibqzmpstoDFmEvPspATZFxXKApOnb8r3GVYPLe7qghoFRA5UNFqmkoBseC3_P15Gv2cKW1rpQtKEkYAwS3IIdqpOsM_taYoBkDwf6CLOhDXVl_oXnBjH8ZBgWOQDB0wv654Vb1QkU-Bwl5rvHQ7JeMxxWxyy5oBlnlDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس : باز شدن تنگه هرمز دلیل این است که قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار امروز کاهش یافت.
🔴
و همچنین دلیل این است که قیمت بنزین، همان‌طور که صحبت می‌کنیم، برای اولین بار از مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، زیر ۴ دلار است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/129208" target="_blank">📅 21:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129207">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
دبیر سرویس امنیت ملی اکسیوس:
یک دستاورد آشکار ایران در جنگ و مذاکرات این بود که بار مسئولیت مهار فعالیت‌های نظامی اسرائیل در منطقه را بر دوش ترامپ انداخت؛ این خود به روابط آمریکا و اسرائیل آسیب زده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/129207" target="_blank">📅 21:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129206">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
جی‌دی ونس: ایده اینکه اماراتی‌ها قرار است یک میلیارد دلار سرمایه‌گذاری کنند تا یک نیروگاه در ایران بسازند اگر ایرانی‌ها رفتارشان را تغییر نداده باشند، کاملاً مضحک است
🔴
آنها این کار را نخواهند کرد. ما اجازه نخواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/129206" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129205">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f65e2d930f.mp4?token=fa5Wm2wslQIsbBjbKVWpeBG_U0oq5SDzJR4mkhK7K2qpMjLx7w58Yw50yHTP-htK8JE7_wg-x19qIrGq4xTnh1IuH4Q6KHSRT86545_Bmsr8LpK3hNDIm-OcaZ75ZQe80smIT2MPa-LOcU_o7p3lRDIwgRfiokfN3d_wUrGmIsHwOGGWMiEaR5Juc8eI4Iq1iaM5ZUSLzHTCNsBQmzyiYkLg-EEkI4R7Mri04QR6YY9viETRti7Cvz2jWMg0Rg_0VWpEDrRhNNwEUoyLsYx2oOZm37l8zNHenFI6dhCuBogRBxsmCP3LuTnm2UwhzqTnMYxvHLnB2d1PjUgAh0XKogXH2FrK5uUsUSNynqU9eWvTaEY-PlRWA7mMGzbd28C63B0PqVpmygx0HCk63OVnPVR0LnYTxnyMLb5hbf6tE2n7DqW4yMv0J9F1OBBP6GU9GtZ18cuOamNny0hc3J9dxQ4SXxdlRZrNHSK7SfAIZMzcBnqq4O7FXyM9GRpaFCREsGFpZytcoOESmqTuwZKEdc2V19YegLkUBz0rCTStYyeifuWHapx9W0V7hpjT1Po12U8lf_3Nczf9veEbIeVbwYlAkS5MVZfgWulPZS7Mon_YERNxppZpLbW7ESfytO3cHoNkJLqxynFwVFp7SOdsIlsInkmA-z46e4tIJ3sI4mE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f65e2d930f.mp4?token=fa5Wm2wslQIsbBjbKVWpeBG_U0oq5SDzJR4mkhK7K2qpMjLx7w58Yw50yHTP-htK8JE7_wg-x19qIrGq4xTnh1IuH4Q6KHSRT86545_Bmsr8LpK3hNDIm-OcaZ75ZQe80smIT2MPa-LOcU_o7p3lRDIwgRfiokfN3d_wUrGmIsHwOGGWMiEaR5Juc8eI4Iq1iaM5ZUSLzHTCNsBQmzyiYkLg-EEkI4R7Mri04QR6YY9viETRti7Cvz2jWMg0Rg_0VWpEDrRhNNwEUoyLsYx2oOZm37l8zNHenFI6dhCuBogRBxsmCP3LuTnm2UwhzqTnMYxvHLnB2d1PjUgAh0XKogXH2FrK5uUsUSNynqU9eWvTaEY-PlRWA7mMGzbd28C63B0PqVpmygx0HCk63OVnPVR0LnYTxnyMLb5hbf6tE2n7DqW4yMv0J9F1OBBP6GU9GtZ18cuOamNny0hc3J9dxQ4SXxdlRZrNHSK7SfAIZMzcBnqq4O7FXyM9GRpaFCREsGFpZytcoOESmqTuwZKEdc2V19YegLkUBz0rCTStYyeifuWHapx9W0V7hpjT1Po12U8lf_3Nczf9veEbIeVbwYlAkS5MVZfgWulPZS7Mon_YERNxppZpLbW7ESfytO3cHoNkJLqxynFwVFp7SOdsIlsInkmA-z46e4tIJ3sI4mE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس درباره تنگه هرمز: آنچه ایالات متحده توانسته با موفقیت انجام دهد – و به همین دلیل است که قیمت‌ها شروع به کاهش کرده‌اند – خارج کردن مقدار زیادی نفت از خلیج فارس با محافظت از کشتی‌هایی بوده است که در حال حرکت بودند.
🔴
در بلندمدت، ما نمی‌خواهیم حضور نظامی داشته باشیم که از تمام این کشتی‌های در حال حرکت محافظت کند.
🔴
ما فقط می‌خواهیم ایرانیان مانند یک کشور عادی رفتار کنند و از شلیک به آن کشتی‌ها دست بردارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129205" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129204">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی گفت: من همیشه با نتانیاهو خوب رفتار کرده‌ام، او فقط باید گاهی اوقات آرام باشد و از عقلش استفاده کند.
🔴
من امروز با طرف اسرائیلی صحبت کردم و از آنها خواستم آتش‌بس با حزب‌الله را تأیید کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/129204" target="_blank">📅 21:11 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
