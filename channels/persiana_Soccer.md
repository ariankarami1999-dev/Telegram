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
<img src="https://cdn4.telesco.pe/file/hm-X4DZSBnna6Y6cGzKxYnsW1wn3SOqNwJKUoZkgMwxOzVDQEy9M5VEWq75Y90OT6YFuwfsgnqWiTTLGP4PENlZtJn-CLERbRHTIArMiFBqlnk_SxFDDd3Q8ZSoOzMciMa0bZ991uq_lAlgu-BTi_QCEc73SwtHM80CPLp5fEjdtaBxRXJ9Ni9SHNXPAgQZjxdHmdObVmteAFX2HT8pTtN3L9ZFGMKJj-Kj2FMmDftpcere_5akBXv-xGiJVc-Z-jylNSvNKu02PXs2cT7WM9XfDGm3A-Jg6HjbO96ooHJDiBDcEHU8iR-gIy2CpaYAWJfLwVKsZDQ26iPJzA7F6pA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 625K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 19:05:43</div>
<hr>

<div class="tg-post" id="msg-26953">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbiTobUTNxOsGQwbGaRW9dNgztTY6u0awLAjFWXqymO905rFat5F0CBoNpfZJZBCit_GhCeqDwsQm8hQ24MmeHfc5XhLEkGq-zcBj3O2kOeB7nDEpGoGm6ipScPlr_mn17ooXai54xOO-0rSr_CPk0jkA8BtK4AGNrFt_5rlA_0AMYRVbr1SeGYY-LVJx8djHNuxqA1WO4EI7UHQFDQxRYNecyROK7ViaiJkKDyGRU9kOHJPyXQw6Gp-ZyJ3DS1bwjCPwBXvvC6wLVQCsCuQNGMArO80kEmq2bhOHC2-UnKjB5O4oVqkx7Svcs6cGTyxnU6nEf0wkZbNMi1aR17BEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/26953" target="_blank">📅 18:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26952">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=M-CX7UuEGKZIkDbWi0-ciAZ0cEJwCkOhr5ME2Hv5NgAOasA7Y6Ru6vkLj5-OhAl6T9QgWT_TpJET8IhXKOuxN2ZaNpyLdHwNGMHwnSEIFE3KxgY0ejJ16TMv0sJ6G5Imnjv4NQVQjq8MNzfQxiQirzUeZxfzeysJyAxUCskYAM228lYQ1ksY6HkuBBNtPIQUFsgZhZ7As0KyZxHU1Z-acqXN0YSbJxhxCsJxI4ew1GXZms20VBt3VajK44KN3SLoGu7FGyqjgZ0EvMEIBBbX6j1htmc_HE1RCN_XnoIKzoi6GdZpL4NRVKnZNNRmemsdCOAAYYyvvyzxii95uotKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=M-CX7UuEGKZIkDbWi0-ciAZ0cEJwCkOhr5ME2Hv5NgAOasA7Y6Ru6vkLj5-OhAl6T9QgWT_TpJET8IhXKOuxN2ZaNpyLdHwNGMHwnSEIFE3KxgY0ejJ16TMv0sJ6G5Imnjv4NQVQjq8MNzfQxiQirzUeZxfzeysJyAxUCskYAM228lYQ1ksY6HkuBBNtPIQUFsgZhZ7As0KyZxHU1Z-acqXN0YSbJxhxCsJxI4ew1GXZms20VBt3VajK44KN3SLoGu7FGyqjgZ0EvMEIBBbX6j1htmc_HE1RCN_XnoIKzoi6GdZpL4NRVKnZNNRmemsdCOAAYYyvvyzxii95uotKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/26952" target="_blank">📅 18:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26951">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbUwnAscmcO_b8ea0OXyH0-xnoQK-llRi4FmK8yoPeeA0oZdplN2UcBSgqFGEBmgBj1HMuG7irczTukl95DKUoYSIqJORBZe82sQWUYoKjFqgP3rBpzqO_fUREpY04Cm4h_nfpRFUr6tV9KywLqdQvklcNFJLi8lLi-fa6V-srCnBlHpjj-A5gQNckzS4ceyeh_5Qz5VHiLCKkskQEozceeA4071INcHL4KCWAoAB6zpf3OeX5xAw4csOdALbzuYkIde-qbN_tbNgvLSigJ_dAXxPzYvaTPu70Fl3Z4o91QswZNANTC-0o691rqt3P8yOKzWLcLy-ApGKFKXbp7HeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/26951" target="_blank">📅 17:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26950">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=ASTE1FasX188jkZiuyTs-F0FK0BsO_cVFKCQQIB2JUIt_tQfVUTPu3Gt47d7Zb3549furKNZtGxGY60m51wBVdhZMb45vWW2In5pVY539PLV8PiSKxyeHSfM7ViCbxwLM4aAmYjfyJd0bULmZHqDwqGd-c0n48ICABV5XpcJKiEfRGxz_zpT5K49NjFIeQlBqp3r0goPyuxPHfg1bfxa-S6MClOcOG-WfV2LOuY7Pt0vIo4zUTW1OLox4LjJzozUJKbq4rbMqZK7rZHC_FVCEhXiii1DNa3NKaFviq5-_ycqvD7DxJspg1BGEhV5htD4HCpBC9v1_-8Ax765pVlMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=ASTE1FasX188jkZiuyTs-F0FK0BsO_cVFKCQQIB2JUIt_tQfVUTPu3Gt47d7Zb3549furKNZtGxGY60m51wBVdhZMb45vWW2In5pVY539PLV8PiSKxyeHSfM7ViCbxwLM4aAmYjfyJd0bULmZHqDwqGd-c0n48ICABV5XpcJKiEfRGxz_zpT5K49NjFIeQlBqp3r0goPyuxPHfg1bfxa-S6MClOcOG-WfV2LOuY7Pt0vIo4zUTW1OLox4LjJzozUJKbq4rbMqZK7rZHC_FVCEhXiii1DNa3NKaFviq5-_ycqvD7DxJspg1BGEhV5htD4HCpBC9v1_-8Ax765pVlMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی بدنی خیره کننده احمدرضا عابدزاده گلر سابق تیم ملی و سرخابی‌ها در سن 60 سالگی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/26950" target="_blank">📅 17:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26949">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVNPF5ylIfHw6rRcCHblYkuAx1f4tdqALGOwWz-Pv8SmhtVYmHrggrtcwbx6ag1zMuxZFoYVIL3mvHjH5X9IUDKRNqrqwxrq_GZX_jMeyZUYvfQzmATi2X0F4FtToT09G4D5oDzyKehXww3uV5ogHFU2q77wD_gHMACMXveVaNkAZMKNVFbkdDC_lf6GTghalY2qdVSD_ZWjfJnnHgE1VaNEnelZPD1ggXC324BxqiilGr7dGz_aS_pv4shgdxEZQLAHlmfDyB5hiUpfy6Jc-LBz-3ezjuV3XjostusFuISOYqS-whsTfL9mSysDzopvqaUigoZLCBrpvxVQkFajBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/26949" target="_blank">📅 17:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26948">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZYYm4cxJR7EHNVX5PIwxar0KR26YhOYGgdj48kwhD0W10wIjMUX3djAlK3KREUBW3S9gNnC6-6JbWOb8nJdSTlEse-AlWyXbxroOrHs2wEHRzVVVod-TC7KdS5liAKO3_fVu610JRojFFNKe1KuDWqGhyXyjNhejnk3xXspzH7q96DyfJTN6cE5Rw24mHEFaEn-7feUxaBNdu58WzrgCFzUdlBSEjPZNt65yfe9z-SvOyp6C2-evlHQTvPSs4g7k06ddmooWd9PDneQxx4EgYg06Jw9sJ2swJN25bBdgzNwUmRIt0Qf588Vt31G4QHLrYS4QpYe0ve_0PtD7NUWkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/26948" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26947">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3XPZChWv2TYjxTnrvlhhZuuRH4m1HTX_CuZw12ZFwobKCO41195qaQDpYSiMFPYt0g2fHwQP-QRvTrZlXfy9kVU7wSajBvMRTqTr-HYGdYY_B8AzITX0JsuQ-EvOYYjy5bYSedcPSe0pr5csG8WOjT8NnxskyIoMkBwN4IRZfbFFW16jzHji-fOQXRTEIh6FU8AtTc9rTH7b1d9lZEwGLyL_AGz0tghN0zxSwAyTXgDL-XqW8cLaZtAqOW2kdu1Xh7r5R3UEkezwCoPdmoejbD1Uc9h_U2n-_3dL7L705pM_NZI6g8nK58CcSzaE4vr4kIcJaaI7Cc_ZiMbBrEN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛ اسپورت: PSG این هفته از فران تورس خریدجدیدخود رونمایی خواهد کرد. تورس به لاپورتا اعلام کرده هیچ علاقه‌ای برای موندن در بارسا نداره و میخواد شاگرد پدر زنش در تیم PSG بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/26947" target="_blank">📅 16:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26946">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufmYeDQ_5J5LhprzJyRvfl72SXFUICslBSSLJCjcmPZ62x3Mj0FsoHmDmnAhut_9bkp6Wbu-QP0oSFQy2k5HGyak7CDwcmtoReYXb3MDD4XUY-9DfdM5kkHhixJXlk9dsx9RLJw6sE28CnitjxltjqmPIGIBBZUkeEKDtcqcGSykzOCDBNAS75X1NynaUq7nkqbOvzXXMnbSw8Elqz1TVGQna-RUOISXSKqWPn2c0BCxchRfO6UKlto371SseORtAP8V1TqDsju_WtR3xsjutLij4Ifpfz0VsImgSLBr84e7aPNflifC3T8oPx0QCxS6iJGd2X_S2SVTmq3llP17vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/26946" target="_blank">📅 16:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26945">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vev9AcsSR_XTbQoOUH02RttiuAVPsvEikWkpVai-QUIV-4diZEHXMlI82RwofTZfO-5XqcFPZlKuSEstPuNePXfkKhB_6nMPRYM4hVCIKcMLe2vuVqGAeo_n2V3eV3wM__EiieOFm6A8D0LTheZMQ9sm9VMHDuJVqqTj54wgJ0Tm82CHWecbkHBWvmJPXFbFbvuEK5e5rYKwJqgnZXjxDbMp7jur6irm-4PApAZSfKw0h3ns0I9xfvxkrAo6xMOijtIBvVs1-8cAN8lh2uIlPl5v9UooyYolrZ0b1uBPKNGU0IyvYbjYfDmikFZ2inx6PyT9sdP-TmOqXrMKQ5JM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/26945" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26944">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSCyDKaxOarI0GZaK4-PJx9Rz-xiuQ4BSqsi9lks1TefYoPqXKimRKuRyYvOcQu__5LAsoJ5jpI1ZKPi3OPr2OUKbCncY0ZvsXvo-GFqlU67-Z1sttEoHANHhwjx_M5swY8IFoiDVGikyfjIHyMdctw2DTjhSPsL6yHNcuuNt1wowTWe42FplNGWEuMxs0FRmV7i8LiHxthOwO8GYWvnjJCaw8NmC-GfQUEAg3ZWVm7qMYwn59mBbfMbI6rJIAN19im7UNFWz24Rj8R47xcnu4lwQhmLFaj_cXtpVMhwJmPm7rPdfBi5WO0Jq-hQP48uUclMtgNcBP3fH5bCvMcydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های‌رسانه پرشیانا؛ فردا جلسه‌ای مهم بین‌مدیران‌دوباشگاه خیبر خرم آباد و استقلال بر سرانتقال‌مهدی‌گودرزی و مسعود محبی برگزار خواهد شد. مدیریت استقلال به این بازیکن اعلام کرده که با ماقرارداد ببندید و تا نیم فصل در تیم خیبر بمونید. قراره فردا تکلیف…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/26944" target="_blank">📅 15:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26942">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSbXVg47Al8IkjRVuX64CUtBIT_UmUi1Y6v4lRA3KsdyCvg5LbdPOichGJhVK4G1kwovVb-3TdFV3GKwea0sHMyGJO2hDEVZjSaY_bKj5RUZGYWtki5wzsGhHi9ic85U58arGBuIFguwvQgC27M49W8ckzDg5YrvNlKhApY5N4r1GIGz-h0-MNOECYn1cA3cpjb2nzIwKdDbFSHijcrxc9uYl6hDbY0jM6cPyBa-HePahHbx8dwfmjQAnyxIanbuPO2zxkHyiX3moahfhFN6SXNR9-AL5UtJ20ipHagGtjas6cozYoodkiO4SeZgYYxEcL_57aRHoxejW_YX3j4NYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=F4unTLIl0ln5En4Ekxn0QEBS2iSa8gtcmZ8rHDMtG0gFYAyywVRuk1UGrfxHKUTTvyj5tm55AeG2zNg1J3LThHEREzO2wHPYipzEau-ow-gD7Zzhcn-thE6-n6OcKfRNbRbSDBfm9jcZyYUP4MFK47xYZ7c7puxh4r8nBr-Fc0B8PWeU_WNGkL12qN6O7DfnA9lUAiKJYuPiqOAtZe81S1B2kLAR_VCMiSvhiKX4Y1fOALRjhcBGAaH3O0S91aVAeaDsCdEwSNOCjg-rOjd1ULcjvMwxV_4Kq_sXETX1q0tP3mcpTBYl7Co84XsDzdM5I4QV81inVLfVT9kFI-DWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=F4unTLIl0ln5En4Ekxn0QEBS2iSa8gtcmZ8rHDMtG0gFYAyywVRuk1UGrfxHKUTTvyj5tm55AeG2zNg1J3LThHEREzO2wHPYipzEau-ow-gD7Zzhcn-thE6-n6OcKfRNbRbSDBfm9jcZyYUP4MFK47xYZ7c7puxh4r8nBr-Fc0B8PWeU_WNGkL12qN6O7DfnA9lUAiKJYuPiqOAtZe81S1B2kLAR_VCMiSvhiKX4Y1fOALRjhcBGAaH3O0S91aVAeaDsCdEwSNOCjg-rOjd1ULcjvMwxV_4Kq_sXETX1q0tP3mcpTBYl7Co84XsDzdM5I4QV81inVLfVT9kFI-DWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26942" target="_blank">📅 15:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26941">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=qLWzZbkSKUdw4yo-IQv72wWYvFIf-v1kVnmOyKtWpmryMRb1iT-jRSUMHiSAvmd-LXh4969sJYoHL_aILbdYwgJrknai-DL7eiYB-P2CfvZnrOooOZPtl2ciBzKytibs9Bkj-K2LOo3T0UtG51b7c_QSDk8MmlXzaAwBAo9E6POl29MkRt6mrnabQyuRi_vtWUb-cMgfC9FYEsNwV7uzJuMot4yxZ6G_YlK0xXB4aFp0i5bY4Lwt2fnbIgjswxyaOm2H8yhAvcqMj0c1Vji2pFKe8M-iQj4rKRbHKtTLtz4lXkgqKO4pcwFL8afsn1FsLSvB30xkcmClACIwDkwU1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=qLWzZbkSKUdw4yo-IQv72wWYvFIf-v1kVnmOyKtWpmryMRb1iT-jRSUMHiSAvmd-LXh4969sJYoHL_aILbdYwgJrknai-DL7eiYB-P2CfvZnrOooOZPtl2ciBzKytibs9Bkj-K2LOo3T0UtG51b7c_QSDk8MmlXzaAwBAo9E6POl29MkRt6mrnabQyuRi_vtWUb-cMgfC9FYEsNwV7uzJuMot4yxZ6G_YlK0xXB4aFp0i5bY4Lwt2fnbIgjswxyaOm2H8yhAvcqMj0c1Vji2pFKe8M-iQj4rKRbHKtTLtz4lXkgqKO4pcwFL8afsn1FsLSvB30xkcmClACIwDkwU1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26941" target="_blank">📅 15:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26939">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5Kye87fZZaI48VlwD6ZHR2zbbQjH0rOZCI4xs549sG7AkwhnHMj7eJcaMOaKruKheYo2VZj_kRIi0SWRTCBFoVbxWEuihDoi7EFHF1TfLfOEuz0iV1781NgptsqYu9eu2jyZL1RNEbTtG9-SBEj007ZzTa-EG3eTGCEHB4nMpR4uKbsYeq4VNYOR_NzHS7GX2On6kg_Sz7_5LvOa4E3WWsWbsOfhFMKKovXFVnqimJRAJudMEq8AO48jRGH-AyB7-9GD1x5nGUenZCYXoRXdNzshYouvX2B4PEN-vdRXeXaY3PGtQWdLK_odKygrtcpQ87b59SFsyezBo7AHfDsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kojPwKPGswjunlkauR1LyJpQSHY859fod9vDP5utZPb4jsSGEGdPSEf0ylJuFIqkXzet87s17JbV0_vNGzl6beWAkrMYFsaqJf6fXx6hfHhurnBTxxK7Fh1WYJiJWHaEU_eWg6-uV_t2wyh6pwi8K-E2DEUUNqVcrge3CKUBzpOY5b03plUYUg6fO7QXz9pOY1Vx03pBdvtXovTWQxQPGux1fh4ema3x5uvosmUugoE7vkX5vY2p938CkKuDKmFikpvELhFdPJ4Nxb-uaMBYd78aaLHbAStHIUjgBdKiffPnst6tCts1oDETLxzY8W0NQkuwaQRmY_n-iiaKmjSpww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26939" target="_blank">📅 14:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26938">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5mbmXMmvWGHxKi0E1RKzwlktpyCZUVOnHytEF4ToBD3jHUsi-IjCnKvYz3Pi5ysD4xruDieD29fTXKIwKGyJ-NKWBkn9nFtWXGvBs7XchA8alvlV_GihrON545R229R4H8otF7zxBCIt11HakJeXRo-r-D1VgD3m9_GfGufuir81VyZfsAQ7mlY98T8kLkSTtEiQdu0dE5UzjAX15cAy3t1ZyEx_3TRGp-oC4R0xwS5JTzUbulArT8AD2KD94kWuR-MLHg0kS8lFMOnVBqu3xrji4g-XXAxoDMZzWh-Hrr7nn1AYwA_783fW79YALlmLcmmMfFOA4CnizlmU6ReGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
پست معنادار و تامل‌برانگیز رسانه رسمی باشگاه خیبر خرم آباد با استفاده از اعداد تاریخی 18 و 19
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26938" target="_blank">📅 14:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26937">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=m0wOZXNkusOQ06wI-mqHhdXgqx68Q70Mi_Yf-7ugZXsUbybJWfxyTcWE9hi98D3HkFoYu_KByvMdBb6KxIsSe1T9l2cl8vbOxQ4w-RgNtURB8J_D26ZwM_gVvah_q9HYyzudWcevJqxAf0OVavzr-eJe30LIPVI1Otgla4bjltyuvpckl5SvL_muw7qSBpQIY3YLZk2omByFMHorY859BQTfj-eunK4NjxegF1VFGCbboboVzAvQYdHr8C6BbTCqNzlyBV3zqs6OHNwQG5aINYtx4KPWfqW3pnmBFrZKTyyl9UOckstyrU_krjq07QOsg-BenmqPg_txL0gS8kkozg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=m0wOZXNkusOQ06wI-mqHhdXgqx68Q70Mi_Yf-7ugZXsUbybJWfxyTcWE9hi98D3HkFoYu_KByvMdBb6KxIsSe1T9l2cl8vbOxQ4w-RgNtURB8J_D26ZwM_gVvah_q9HYyzudWcevJqxAf0OVavzr-eJe30LIPVI1Otgla4bjltyuvpckl5SvL_muw7qSBpQIY3YLZk2omByFMHorY859BQTfj-eunK4NjxegF1VFGCbboboVzAvQYdHr8C6BbTCqNzlyBV3zqs6OHNwQG5aINYtx4KPWfqW3pnmBFrZKTyyl9UOckstyrU_krjq07QOsg-BenmqPg_txL0gS8kkozg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خیلیامیپرسن‌دارایی محمدرضا زنوزی چقدره که هرچی خرج میکنه تموم نمیشه. این ویدیو رو ببینید متوجه میشید. امکان کز خوردن پشماتونم هست.
‼️
طبق‌گفته‌خطیبی؛ زنوزی قبل از تراکتور خواسته بود استقلال رو بخره که سلطانی‌فر بهش نداده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26937" target="_blank">📅 14:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26936">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eezm3_wEa5GiZ-Uosk4dh8Ymk-tN4y2sAOhlVpe6Kyo6hs-byj9DyeFjPA8CeW9lqbC1emk2W0uTktiox5AQlvQgPj0kpB4O9_9g5O24tVB51pDFRrZP9NukewHzQk-DmCC4eEcRAtfKIMOpFq2CYATvwkPVslz9s_6p2bUtZrLJf3kQZFFJpdsyA3iWK9C9g1-ngfzFUhSstI8VuBCWAy03qJTDWHmcbewgUOsYxvPy5jvVyBN0aXxK-LvAvyOt9z3yr4Gd0rkEkTq8-damWQghTI82eBEAUxBWijb9udrc1FLcIeKeZB_QxYM35maLnnHIT9FGFbVu381DiL2Gyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26936" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26935">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYgq0drOC_FPZJudLX6tn36gsb5_-G0t5uCaog-BbzngD2_XI2Nwm7m-LaHhe8B4B7vKZCZjVWWkaW_4IRH-4VQy6rzSuusccKx_3DH_3ExHCUChiLHQ3nYb_Pm3ARAEsNTB6TWNbKJnh98jqv1wc4GX0IB42-bhc_xbRh6P-poe0TNb_qh2u0lEvGEa4VV_0A5XOHcbbiJBo92oMrIY4ZvOvqYzEJlTFAFTVOIfi1_9MASysw4oM2M7Yx-lGLq1CHxLRJ5kRJcjFjST05GxTmvQLyTkAebQRiWpe7jhsKmATvc9B5202tLnh3uV44_1aEhlGL0CRD8rX2eeprxWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26935" target="_blank">📅 13:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26934">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0a57Uya4TlkNos1NqnnG8B4RzA68Wy-hYRMk68jgtwVhd-2ggs9CN7EKBC41UbDrKVsHK_hkeW6SF82lc6MFzM0V91Gd3QXdV8ljhMaMfz1tuXrMfl19UQe_GObNzxR6ZmG_CAhp6DkcwO34e102bBkjvSHmdyXne2SBeJ-mxJQtmXSChDNuPhUnVKpaVyLk2ZszdXPFyZqX8ROVRWEf6BKHslaEo0vtopoi8oHXE1HfZDZvxnZMuCIf4A7uTUwiENnhl_1XmaeRdr8R8kQwPNE7gnOeQOoe-70KRDcJkFa-UlMWUNMe61__EgOQR4OgyR1b4VHdMg24_tZLllmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26934" target="_blank">📅 13:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26933">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5gxYw8DFPf-pLB3RwsV6zCQB6qLhgEKgAbmcGjg_go-7jW6SFs7qZf7T0_spHQci6UvEY5VlfOxwB_yzOCAoTcBVAMQf7wl8MbDoInOcuM4tN2VzgnyED2_OaHZ1wDBpqzNHca5feUi2ACw_qal2lC8LTVvvuDfNkw5EWf_Ira7jTWllFrjn9mv30eXvUBXCHaW-fwPEsSJVLp1DAOrkPPwNtN9N4eJje8TpZlXTSIN4jtZ4ge7GvgYsKPliT0J7wd5dZvqgVrdCQ5Srb4kS6mSZ6kXu1FnD6V_dFTEJhbjXFKhU2JAMv3FCTk3Sm2yuKRJgTd2-taARYN69mbRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/persiana_Soccer/26933" target="_blank">📅 13:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26932">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq_nTPtigzcTF_Bi5BBoJmb5YAxWL2oxitJmcvbO8uKOnqkj_ArYicPox6wdmeOVOkq2c3SUXZw4uEPqgG5wD8kMF8KWCz9P7pUa3Hin9wxSkig12D0oHSoWPq_a_M1NRENgS4INfMWRrLmKQM2U-XX7i3bheztSHv1j6v2XK8sQ58xQync4GDYBicYcWIGTqg5TDgV6YB_NezUXgcWX0ladpoFoi4U5jofXriB2ApMtHSqSuSrnSMBFh7-5XNG2oIFEI2qFNDBjUE-2pYWgnMgdb7eAacULc7AjcD9AXlzXaxcw3fnQaVgimHZlPqT0DiZnJ34EFY2y57TNJjmJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله تیم ماخاچ قلعه روسیه پیشنهاد تراکتور رو در رورهای اخیر رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/persiana_Soccer/26932" target="_blank">📅 12:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26931">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcHQeIfzsaOA4DvJ5B1u4jFbcBzezLahXc8BsAImFHIvbFufNN1A7fMEqMXb5lz14P8nEm7p9yxvLza96DKegLhncBIEzxmPETNj16A_n6eO9b_NcximpyDl7du659B2-WmjJZdoqWCQ7WeWox9Er_ymy4MzAZeeh4b2QiQQHRBYQLhKJ2V7Ro6bICBVwHJWJkljY67znirQd3rd-KXA407uunrYogSU4i7mixxHvuLx4N5iu2Iwy40qA3hTUXM-UKlBZbWG7O6s23S97pyUE2BSnOJwOdVw0LAC2mcMp5ND5hc2NamA2YdYvPHxUgS7mdMzsZO-M5JcZ6TN9cbghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
نشریهESPN:فلورنتینو پرز قصدداره درآمد باشگاه رئال مادرید در این پنجره رو به 400 میلیون یورو برسونه. تا حالا 200 میلیون یورو بابت فروش بازیکنان‌آکادمی درآمد داشته و به‌سران آرسنال گفته اگه‌وینیسیوس‌جونیور رو میخوایدباید 200 میلیون یورو هزینه کنید. اگه توپچی…</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/persiana_Soccer/26931" target="_blank">📅 12:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26929">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cupPuKfqFkJNNGTPDruIv9JkNCa3Plg199XF9_ukvZVsHsR94p8Uwra-p_j8j81RCDhdQi3G46BnUvzeLJ8wUojBmwTiVdS618XuvnATy0MY6FBkPqbv4M9CbLO5kUlQwmMPkhZOfnKpqDnvz4GNuO2y-2tzKnRBS9nIkSR91YgbB-MGImq6L3XyHSg-77B3URjyR_4kx1fBtMp_vUqcBKweDuUmTXYTmn41vg9MpBbLS_emG-tAyftiT9geEICwCjafmV7ycChuqYpsKNyaj1wONLzUbjOvQXej-1WgU-AdcuFx-Y2TT8D3iULPyV7AyK8bvgBG84alKzqZdMwMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFcKyEByPvrUGAXrqyA-f2Hhg9dFyC8lVTVv2Sv9UbJ3JgnFaTooHZdRkjLI6d5zRabv0AP0HAUQJydoaUdfb7ztBXBAabPgsC8bOVy-Uqi4osxsEHXmGNQmiW8DGML3Mf87Ms2UjTzheDbIyTaFpdxI1MraYw-K1iwCaWLHXAcnEigId1aqFLq2eJbZNDvJaoW3ReBLKu67UNNO8rg2RU_Q_AE-fhCQw5s2pl8M81HIHXKwZ_ySrG_L8BslKD3G0GrQk0GfAGrR2Xm3WVejjn4aVVP7FosxAfQa0vLDsCnZ4so_Ts0xhSBucb9f06nqmoGxKlfW6wGcmdt1o_edGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لیست کامل ورودی‌وخروجی‌های دو تیم رئال مادرید و بارسلونا دراین پنجره تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26929" target="_blank">📅 12:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26928">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0eEmL5r0qCN8Ne4WHQGj8utcTq19IyqEJqUX4E5pxcC4dqh7bOGGdHkd_4nGTlf9JVq9W2QjBDT-AknBtn7Wrs7TKSgKbxGSulXvh26X9oHbw_X60q_8yC04oK_PA-PM8NOjQypyluTYCQ9m2GOWEbMyLYgAkYCA0egTmx1Jh-Dh12S4wrgNrFcGBUAevT1A9DhNGgGk-6bGA2Eti7JlBHZWwEagEiwbqaavKqNNtuFAH4Uslu5JVyDvqtlwdRY25JdleSMi7eLnmJmD_GpD80MVFY_ZRxUlRFoTmbSMMeCso-uOkWsm3CiUQjAS_VnR9kLfiHanpfH_LVEbfPLxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26928" target="_blank">📅 11:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26927">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26927" target="_blank">📅 11:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26926">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuHov7D0WEAGWpEhUiPyoNp6zInXC03SapYCuZs_1aZlgK5WN-sasRle8bVZkXdI9XS4drR8Q-vSsSJfJJVsPjfBAWTsoSYPPfUhYMnL0Mt-q7K1iWkY8NNIoFOmuXiXFTmGLtSWGg8FYZ9IenaX2UTSVRSIvSi8WaEEGvG-DIrhrbzG866GSBLfqL7d4ZaSekp0dsmJ8H0pLaFhKX0CfZ75AJXqiFzGNV77hZIRcui_v_Q8YEq9x2wRiOacSpYVC082emngI3-xq5MaWZHjWpoSO080_1O5FwMOGl2xtPuN8vJWSUaCUVNHx1KHarySO0XSmvrR7Uw36Osv1DbWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
زندگی رو لامین یامال 19 ساله میکنه که تو این‌سن جام جهانی برده، تو تیم بارسلونا بازی میکنه، حقوق بالا داره و صبح تا شب با دوست دخترشه نه جوون بدبخت ایرانی که از بعد هجده سالگی باید به فکر سربازی و کار و قسط و کوفت و زهرمار باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26926" target="_blank">📅 11:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26925">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIeqjoGiiFEnmJWtXrp0KbBmMTGNcClGTzlvKskxvERDEaaF37u-q-4kBYTy9IZkWl-06YMM5CcCi-pKll2F4w-aFcrjt1DIj3B13oJEdOcaL4yZp3i9gQFfbevjbHK-VgU0w4D2Ls7i16tUyxrevz1dRUAmrw6IklfTO1L5g7k4arr4zQjpUcz2Clj7BdfjNIoumHQIzZIupkPIlYuY-2bxPm8LeSYzUvdKf77ghmitd2t0KYEwc4aWbQuGFTnGGn07dGzLnlejdH3H2xCB0LogqZRjwHGubLGqN16KtGM6E7xJIoMcGya-XqsTnZ-Fzc5If64bz0pwntVZZ2tQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛
با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26925" target="_blank">📅 11:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26924">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtXdUlHgGWLPaMMav53mBaOzEh6LVMfYFMv4-UsV45MjDUaFIArMQPFU_PtKxNd23SnGNVAGAIYD1q2tOHbMqLRvJr2erR-WorI_RYY6dCDXAZB-oVpHN29GZR8LEv-JEaJPfHeVq-u2BcIb4mKbRnMCk5FHxCI4M6152FT6w7U_B_Ysp002lQ07bNKRYksjDOrCO3skheQpPUcsTUENAA2gpTYlRO3Fj5-YBCxZTRMbnxUjGyCpmab81rPRdIthAVMegX2SUC18xRIEwvF_lAa5phmA2vD4UIhIUIPm-fmGbLfjUAZCNKio4BjKge91wN0ObA6UDajfQvj-TJID_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26924" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26923">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRB05TqVfC_Au7z2uzprRfIrZiGmt2MCXSOAgO9Q0Ll0y8gbttKH3bjY0qRfKTDI167O_qZbH9o55pSeNhr_Z16mrAEwO0KfAEeSZlyj7k7wTmFvPKq_E9XDl1CTYhJhExebbPzqvBTRgpAQSmFtyRBkJUO0HpVvOSUHsFPIRbk9KfJhOl_qqL5_AqfoJ3F6IE-vS6uGT5Q1H6f0ma66cU_JqpCkMlMWKLwwA_jE9A3XyGa0Hr1gJyPQ62DC8dISqD9WXnswmMB3pZAA9KE_Dr3SciBkJuvITCUgRFPBg4pvuNmH22wTAD7InRM9dIIar-lDL3Wc_H7DzXkgZdTXVdWFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRB05TqVfC_Au7z2uzprRfIrZiGmt2MCXSOAgO9Q0Ll0y8gbttKH3bjY0qRfKTDI167O_qZbH9o55pSeNhr_Z16mrAEwO0KfAEeSZlyj7k7wTmFvPKq_E9XDl1CTYhJhExebbPzqvBTRgpAQSmFtyRBkJUO0HpVvOSUHsFPIRbk9KfJhOl_qqL5_AqfoJ3F6IE-vS6uGT5Q1H6f0ma66cU_JqpCkMlMWKLwwA_jE9A3XyGa0Hr1gJyPQ62DC8dISqD9WXnswmMB3pZAA9KE_Dr3SciBkJuvITCUgRFPBg4pvuNmH22wTAD7InRM9dIIar-lDL3Wc_H7DzXkgZdTXVdWFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
چند تا از شوت های روبرتو کارلوس رو ببینید، زمانی که فوتبال از کسب و کار و پول دور بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26923" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26922">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja3SMauFUpFAw7hPyiHz2Cpmu9H4dCvmsxnea7-GRCFnw3oGxKmfk8XJVP5ckWuY4wk3_d4iSsTq5miEZDbew3IrGOp6FH0nZe34ezQOf7JmwWcU_oGLd8elgSWrEivjbY4shLSU20nY1ZrFs4iqKWOOSyTzKIzCRMSxx4KdkuiMBOMTtouYE2f62I-aWgmQ3GuHrWcr-DUhzxM9jjujDt6B9YlBKXjnEVDgQYvLmzVNF69EJq9zQeMh2VfuaBFXrC1BvyNb1phJ1JS2OGGqLZghkZM77Ugiw0WVMKaBIf1y7FjbWq_esvnSdkjcrZY048Nlbg2obprneAlCwm-smQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26922" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26921">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM1dyE_y1egN25fxHERYoeDPy0Us2WUEFvcGY3gnd1Ly0DW7UjDUgZ2p10YxlrbuX7VJ3Og_MeB3XQzABApnvKGX5U7C5P7Ouku-FNgWf9SAc-ACrSq4Ssxsxg574SPlFweWGzpdiL5gm9c8VjHyGXagJbAb6OGkKjMnsleQplwVXqk5js755QEk6QyEcIoz4e0sls60AkYZFU805EeOcmnU5P9j_OtWxeRwnnMozRVxaNeLP65FIUkXwY2Sohp2C2zS7jtDk5YR66jwaTK7At_3M1Cvsl7fPIzrdjdkgQzOmKOpBtuaowNYXGsFZT9blcFHkei-YQu7SK--63inlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیس یایسله سرمربی 38 ساله الاهلی‌که فصل گذشته این‌تیم به‌دومین قهرمانی آسیایی خود رساند باعقد قراردادی چهار ساله به تیم نیوکاسل پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26921" target="_blank">📅 10:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26920">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Zpg8pOV5TqamFwASssBaZddOD6FZi6KzghcTclNIPPCm4NTA8Xbpr_x_Qi25Q5j1nypx9MNrI1GXKTfhqJ7bP_aUdZIrA5w34kh6wH0YWOh-82NuT35RL3AUU-41WO6c9AYPGIL0HJvDaizCu7QBweOT-PlpkkBh3XWV92xr0ItDiA846nkOMjbh1dwDV_0l7CRWICI59f2wzlkeTSU7Sm8p9yHyYU1EOkfsmsi-eGmVCRDjdSne5Nugde9ccScmtg84JJ7TznB0K2lXg3olyJ7lXLlGunEw_eiQyqAJF-6iqIlyfgNuHAbN5vJ9S8r4nhyIFwg6khFAhjTYZ4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26920" target="_blank">📅 09:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26918">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3px4QhoCn0NQgV0lL113tmyxG8A5PidvKfcyiRUTsPg9rfOQclGEfmRKk82S5gsNzfqv54eeEpez5IeeByRGQP6A18EeTiA9POXeXEv4MW9suqPoK4tQpi-rZceT5_qRv0AbBRelyEE5JMAl879Wh3HWKld3TVez9LWZTxhy3mGsVKIrxJpjXhEpA4yaNkBS9LTZ1KPgP-So-lRL_49omyfdac-fgROH09zKI7kPyohm66vDAzs1eYx46e3ZeDi8MpT-FmhlxI2LLIMLXQlmcNX2bRkufyHE560xuA6WKr_P4yKu7MHtho4ktGgBuP_UbDBeOT7ollGiq4SC0lGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
رسانه‌های‌یونانی: تصمیم‌باشگاه المپیاکوس برای فروش مهدی طارمی قطعیه. سران المپیاکوس برای فروش مهاجم 34 ساله خود رقمی بین 1 الی 1.5 میلیون یورو تقاضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26918" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26917">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrOCSKCUq5AwRswTPzHaLW9TfISO1e1JekS3JLEnLUqFYaqlNKnU3qrTCV3Mky9wCHWCBUI-j4cdO2RzJ127XvrTvsiT27wiFBOdpAu-iDn0oJ8OgrXPk-c69MsILzBL0Ax5uqQcW4YJo2HODary93lEoxI0g0EjhOWG1sRW6DvCplpTRt7QvDhPYu7ObtxWlLAq6b4Cc0957Z3rZ9P29evclREt_BaGiT8tKcWVjwM0qLP0jD2p2cu13z1o3IfMFsjQ1zgTp73hN4OebmM7stE6MxS_rQ87QDc1XZ-IdKOuj0Ep3mxwOVAhV4U0FI-lXPblaxvIEwxUdLdU2beLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شامیل گازیزوف مدیرعامل‌باشگاه دینامو ماخاچ‌ قلعه در گفت‌وگو با RB Sport: سه پیشنهاد خارجی برای حسین نژاد به‌دست ما رسیده اما ارقام پیشنهاد شده کمتر از رقم مدنظر باشگاه ماست. سیاست تیم ماخاچ قلعه فروش این‌ستاره‌جوان با بالاترین رقمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26917" target="_blank">📅 01:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26915">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZy_KKv8_xTw48R1cIjrXtzEuP-D4lX7UttWyPh25-FpSyLCJCOwK4d0as905NQ2_ZQNAHqOgmTuhv7cLcn_Hf5gsXtEDHPqrH_JRzTiZCeqTneWw6h0c58vJzBHo9a7tT7kJWz4zCRaqWNoWyWCYuWt6vdx0GN2_tYcmEVbNGeXxXuuQssYGTxsInyR3eBjgqtAEPM9l6bfUMPWm6_O_8-phGjVjWVHDGCz0uYlG4nuh1YcF-w6RwjvsrB5-lOPFjm94tdT-o2f44RnSjULqB2iDs0JvarXocHVQCNGWFzu7AEv2FagWt8KZq5-cts7R332pPWcyqxYcXqTbJVOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26915" target="_blank">📅 01:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26914">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzqIoAI6tyQboPiUED7uksTaKPagHrKbkP0ky3Of4lmlNQCx1yXGE1cev9cb40Zp0fw_Nqqwe8rarPw-uUbSnrozhyZ4lm6yTyVYofveOZFvkFyvNH5VhYHUKImdP0z9C_QXYkMSZpuUJtZvHB-9fswmS8FmUFruilCWay6VQi9iuJDSGOcgjK910BsPEjzf_CbamEqIj-puHGGqQvw5J08iNzSHRGt0O2IL-DnlYhgspiO-pvQVWkaO7ohftQ8-OvhYmBggJTY3QAyrAmPoCpmpv0WV8rejI3gvO4QFd52KFZ5HsNiI7izsJ-f0xk3iARxEa-l-T1ypXIt1THAFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
بردشاگردان اسپالتی مقابل تیم فرانسوی و شکست کاتالان‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26914" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26913">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucd-goZn5RzXxjI0NNznZHLTTcwaHqaAkNmnlVmVLASUZ5ODX1TVB9w8HITFOgpzPnm90Sob96fnC2U1hTu413-rm8kPwuuPn4ZORMjPr6_P8Pmo2uMJGiJpyrY5kJhLgBHma-zllwgyJU0CbGEpnn-ouqQXx1fEH8rsxAJQk4XTNZT9fxX1YVflm3ykKd9tvNhlQ0CEUVcT5soxxofE-Dq2sR7JHvR0FF1jWcuAu3jr4GlDi5PjWBay8etjOskIzLWvwKMLaE8Cd-1FOeBHI7K0X4_KZh96LZHibSUDK4N3haM68GueZgORGOarx27Iwe6s_jP-Q_LmvlLngx3CLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه آمریکا و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین حملات هوایی تاکنون علیه زیر ساخت‌ های بخش انرژی ایران هستند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26913" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26912">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NouTR0r7ByTgxyBm-WcwnOhMC0YCwXAfSLYYckEGuJohr9W4pGdOPnM9xL3VIvbw3q6gGrozAt3c_0JlOnpDmA_4FxQsyAcaZw7wRjmzQ7zAcoqB6DVn0TmoWowANmFyIE-D97RqsADK_HiKEZz139Wsx5A6mJc5ydSrK9GQ4eBa2LO5wmh_TRvGXzOmPh33dQKi_5stvnnvj_BjBicOrXomY2hItjmMtzD5c6Cn1FiS8tL9jnyR3gQ0cpaeiSbDbko7Z0mLTRI9KOFc8EiqyVZycFuKIRosdTKCXxxOkX-Yg7vdsXB3HOeeI4NaEqA6jR4xfF-abR7CMRggJPPLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
رسانه‌های مراکشی: منیر الحدادی ستاره سابق بارسلونا پیشنهاد باشگاه الاتحاد طنجه مراکش رو به دلیل پایین‌ بودن رقم‌‌قرارداد رد کرد. باشگاه استقلال به‌منیر گفته‌برگرد سالی 1.5 میلیون دلار بهت میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26912" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26911">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flZP_YVipT_xRU8jU1DZ2ZItE2Y-46SGmrGlPEKXkp1pnTa9CHPxOH5HJtnS9TOFBAeyYMFJwOa7qg3ODv7R4UYkXPcwnMfGALsIVwh_QtGe5ldXx7ipGdmKI0tJkdCIxP7Q0U_1oXA4VxskGIMOm2qzcMNUP_Fp22lwymHVhsIb_a4rU1v6ccmbpqadeM2XqJub7QbcRg4_IxGCd2sF4S0EmHPUGAhYlE6Nv6FeRHJ_bZbH-Ol3bWXQ5EL6FpVmgsNt-UPFZk3PpyqqQJPCKNJMiBY4W2KWYUvnxtiMIo55aP5w9ViNjlcPU6NgPbNJM3mhlEXKc72Xl75hdAlPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛رئال‌مادرید بابت‌فروش‌بازیکنان آکادمیش درشش‌فصل‌اخیر 440 میلیون‌یورو درآمد داشته. تو همین پنجره هم 196 میلیون یورو درآمد داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26911" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26910">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDx_Zpevxb_8Bv0V4ASR_ZzADf-5v7GdRZ_2QBvjecruRdkjsJ2onDDxyIleT5IdYGwnZVaJVed6OuBcIRJavyqXY8OhI3T3ceJbHStY7klYU4MflKRzBLSzpJiOhyxXFOGtb28Wl7zVuepbbb6YBR47k1j4m-E4Y3XGmwfoOZ0BuNd0Yi-pSJqTQ1iQgph4VT2EX4LtEmljaQuSOX8KBGDSCNg6GYktmVLrZuTigVQDCgthW6QdlWbjjQEPVf-9K027_mkZqluTu_l0nyeGT6lvNjkFQII-MoDB5pQSFgnvmahJIKyzHqyaSkGTFTAhooPeHr26GXYGRWvvssbDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26910" target="_blank">📅 00:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26909">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAKBkyGMQhZqFVkWvR824LmE53JHl1BRWnUj-D8UYt0nt4ysScykwIJCKViKUvmNxT3GCeF1LvfSGJtw1ucmdWLRYYStmeu_wYFAduHLHhTEYW2NSEOb8s9P9Z8MqujlXerrLbuFk_f1WkLABYlOgeAsidj8qpOAkwZp2GAK5CXpG90r6UsDPSkvvIcqLMPphBpCWw5p3ncWoS4dabPfbTg2ekUlXve6qFIM54m4VAhoFEQIrOkrm0Q6RYBIeqcslbE8aMiJs_kHr67xPHLdrhLxgwqEibrdLHS4VBat3v84aXoJtQVUOQoRXh42dRZvbpwN9ubZHR7HKnmBHrAJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26909" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26908">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1MOJrhXMW88Orxw5asXvDN_CzQOx7L4qWFwR3jziJf6w8DyA4XEKt03JDhmDzADghPnUhpMdInKaKzgLN6PViVlV6N8o-kQ8P38_Kyrh-oMwJXPgpyyzkXBbumhcqCqe4shcRWNqY5IxOHHmxPEj132HCDDNTmLse6d4ZJiGpN611EhwAjKpxJCzrluepf0ZkIZ033E6rwABoIFDV-V3ALIxSE7okBINbL220VerGTCBuWfxPpC_Ze8KZ7U0HxFeOI7NfR-BliVRpX6HyTAqbgP1fb61K0-72M7TDrODAor60Y2mcKMYD3khKR-f4_5E5UI9V5CbryDcuFGxUjbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26908" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26907">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i47RZuMlA9_Yldhyofu4Lbr5Qm_xRfZjzuoLEDj8DLJycyjjZy-5MGwhnIS6EZUAEnF0WeHg1H1G90l1OwSCkSotYLpyV0qqKAun3J0P_2RsOpiP_If8WiRz499q9K6FI_5L_HCLgRcTXGAl1ZQ1ATaN3tdUmkdUJTtsDfVucopCzD5wey0MuO7L6-uL0R64AHVREbw4cFkvPARzmz4gRJ3uLwIoIuUx9ZPCQfZRR_23jPuPF1gVLuYwbQDR28SBjB8s6R2xvVtvqLAU1eD10zOIH7W5eBXkvEtGARKVzYYNMXrhWCWT_ca1L89Pu0GWFOjUYiA8k0D-W-lR_U62hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26907" target="_blank">📅 23:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26906">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇪🇸
خب گویا سرخیو راموس اسطوره رئال مادرید هم‌تحت‌تاثیراستوری‌های‌رامین‌رضاییان قرار گرفته و دویدن تو خیابان‌های شهر مادرید رو شروع کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26906" target="_blank">📅 22:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26904">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBzZH443Fh5-dmQfHD2wn_u24skfpgIxuLYE10oHQtYT_OP-lEost3YOiYUWUK25RfeHNC1FcJMf5F7er40UP-lKcJz9GZYCwM7GmnErAHxp109i8Yf9wAQRvkUszAouMIhbpbXcVGEhL3BHihuhx6iJuMm21dqarYFdWcotOUKdWmfesNutFE7or_nk-ZXBV_YmR3FFk1TZWOtJpCXboYqx73wruHtmkonNEGH8tgY1p8j-iS76EpsWcknaZD1f1cLCYzSx4tIdj0b8j0OIB4uF-wUXy8-OfK6LrP_Yeha7-q4czZ4EQhhV-CVMlgPMECjdvmVaWaA25f6Gk6fF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26904" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26903">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXQUzvgJcYeiRNAqUc2wLmhra7-7DZHunYdYVNN6dyIWfIjZTPytSam-33nyOvEbTdEDVR-EQL2skjgFVyg8kvs3T9uw1eeZK1px0VSaJVKlR5AWMywswpbX8EQduaZvZINLM2FHk1BzD4-nG5Rco0Tk-Ow21U-wkw2trIgjMYxJsT3Uk78iLjU0kHibo56atwW64lolRlU6yzrueZvicspGeGwrD1fp9y6xF5w83EIk6rn1y-5ySjwaj6aFNeR3bJ7mRFzisrBwZQetSwW3FnO3xuoCD9fdrFJLHzi-ldB-N5Yqad4CJAVC8bcOj_LNM3vps5WT2keCE4oVRrE2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شش‌خرید قطعی تیم رئال مادرید در نقل و اتتقالات تابستونی؛ به این لیست رودری و الساندرو باستونی هم اضافه کنید که در نهایی شدن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26903" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26901">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rehKqwJmAL8SAtPT8NFg4HyDwV3Do44xaHk6SJ4jYIGj4Rm4uki4RxCA_HiQKIGw5yv3crmT55EGrwTS5kCAc3jM3VWwFI5FNJZesmjbyRb3kvjSk4TTPvoi8aaiazVhxWvVrEyrNKpOJ12KW7dn7_zVuOGoSaOHUYPFkp2NtyHxgNSu8MXqjhUfb6Eed7ZMXtxBCOzJ_zGFNQkCAoRZ4khJJ1t0J3HgAi7I1WI9hClIhQVI1M6b8hdt7f5hGSf09u3qK-6fcOlNRUdQrVeaTNB2i33v479Dkrteq47K6gO2C_b9SjzYQAKoSXkvMdsX36HJQkK5ymJddhYEaXVf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26901" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26900">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vq2tHdsoQOdbnKDI-vqO56-Nk6aAWc4CRf2ds3vUQTH0zg-qz9X1TzjHMUCt11xG3uPh_9WRmQcESR8HkomX1NUxWm76cQdX2nqT4d0dSryOnG-A5DodX5EoPk4HslYcX5zBdr19_br4-IfZ-jG2Gh_nMciSGXukOpkK9N5_SwcD1RFDTRY3VBxdn5LvOd9Wpvr_hZoIiW_2HVrvsIK81vqaV714DqbsWpPo0nLaoWE4i1xR9VR7f7lqwMqyaxf4Yb2aYay6IXatCKqiAx_kpXC_u85F2EpwD-rsh7NfPXJ69yzE5TdhGALM0OuSddb3bYbWWqaMS-xGt8pIBlTyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفامیشود با بازیکنی که 6 ماه از قراردادش‌باقی‌مانده‌مذاکره‌کرد و حتی قرار داد بست مثل‌ همون‌‌قضیه یاسر آسانی با این تفاوت که در حال‌ حاضر پنجره استقلال‌ بسته و مدیریت آبی‌ها میتونه الان‌ باهاش‌ قرارداد ببنده و تا نیم‌فصل در همون تیم فعلیش بمونه و زمستون به عنوان بازیکن آزاد جذب بشه و نیازی هم به پرداخت رضایت نامه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26900" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26899">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMx4w0okIQDnLB4sRMoJXt9dDLX3qFeReh9jPbC_8TVjOE8zO3InhwDzwfzTMxsZEvJ9XWYA4iDN4PyyTBuKczFFYgyFOjhgfKq4epWmgu5kBP3x4kfeOxibrjyeDrDTctVSNX2ZsVqm5-deOt_CqYDz-rpin3_YO6xb6TuNp1tJXfP2_dVxCWQRcCc22jejmDZTvgqDV6crwGu8c_M-WIUXm3cJrTyYXrjZrLwRSPOitbrh-oumcMa933UqoEvzbNH_PzRM6c1BEfaKUk_ssNEu2Lg-s8aYjaNkNEwWiLT7zGL_d-DtXrx53cJPKBEX-7VnbQE_3_lcwD1DgjSgOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
براساس‌اطلاعات‌ترانسفرمارکت؛ تنها 6 ماه از قرار داد فابیو آبرئو مهاجم‌ آنگولایی بیجینگ گوان چین باقی‌مانده و طبق قانون فیفا میتوان با این بازیکن مذاکره و قرارداد بست. در فصلی که گذشت بااختلاف‌آقای‌گل سوپرلیگ چین شد هر باشگاهی بتونه بگیرتش ضرر نکرده است.…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26899" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26898">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC6OyS18PEVpsnD8aRlccBOlcW8eM0u2VXRyWZL6T6HUBnDfIet1wn0LzEIinBeCYIK97ZeIV87Ud__KdseX4nHf-Je4M95Z8luAFqFUVH9j7ezra0SSHV_SEHhbCxweWkYFBfihwa8Akc9NP5KQTyorUV1lKyAHmFRPYwpVQl-vm9DwyFjtGCIG41yqILXUxCOH9E2bz_7FtLiGdP70V_ZdlXzSFyDY_WFIoCUPsxGxiJjT3U5VY1uQm3t1gCDPk3ZHK4gjyqwbvNFc2lh2XdE5tFi4Xy6T3F6J_fZ9CJIdrjhxSTFKZTwD49ky4uI1VwOhOLophJ9ypDkOnvexdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26898" target="_blank">📅 20:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26897">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0Tb9gAZsK5zidfXYXQQMehNxp0ohnb6QHey5v_AOamhmnlRby0WnsYUXrsRxoZ5w9VKwla4JqVIk_NQdIzRsSEOZGxjbvQJp_gJ0odlLKVoXsXnwRMxRKdpHLQvEBq_jpz4tTXjygEKI8fEDM8Jlxg_DrBOUn96qSNs-Hf37_OMKwX5OCZ4JpzH9nn8xexsNG8sxuxYbxCcuJ94hoDsjAUsJugYdgkR15dUwa9RoVs4VBpAPUhuWaPm3KWAxZZ8USRY298CaNNsYqZjxenhNKv6cHWxfg_U6oJ704oDDvifpN1s20oY_E1b7H1fbPyPmrSIHM27PLPL65CVoVCXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26897" target="_blank">📅 20:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26896">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92aea27557.mp4?token=JMwoPXt1Z6yzzFSLbyPD6-uANtwXWuTwq2aZpjvnUeBUK2k_YLGfhp3GPdqKl_b2JahENlUhKIwEiA-S19cSxJcwiJ0eWX1loeA75FmlmIeJbTln_fv9qLcQqjl36plCvcBAVURwKr_sfIBiwHF_T030U0th1n8YGMEW_xetz2dyUz0e81bUDKXGZHgc0dAXacqs711z_PNbwr1N_-zNdrhSEp0kJVuyKfA012cXLI0H8ax2SjbDA6ERcP40yXR6L8upc2dUbQF3xSS-33F5n39yOgMD1os8VDVNIb4kaIQz-5Yimuflb9c4aaQv65jEEW0RlebomfZynEnraKZzIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92aea27557.mp4?token=JMwoPXt1Z6yzzFSLbyPD6-uANtwXWuTwq2aZpjvnUeBUK2k_YLGfhp3GPdqKl_b2JahENlUhKIwEiA-S19cSxJcwiJ0eWX1loeA75FmlmIeJbTln_fv9qLcQqjl36plCvcBAVURwKr_sfIBiwHF_T030U0th1n8YGMEW_xetz2dyUz0e81bUDKXGZHgc0dAXacqs711z_PNbwr1N_-zNdrhSEp0kJVuyKfA012cXLI0H8ax2SjbDA6ERcP40yXR6L8upc2dUbQF3xSS-33F5n39yOgMD1os8VDVNIb4kaIQz-5Yimuflb9c4aaQv65jEEW0RlebomfZynEnraKZzIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از عروسی نادیا خمز دختر خانم پاکو خمز سرمربی اسپانیایی سابق تراکتور به پارتنرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26896" target="_blank">📅 20:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26895">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiIitueRaLPXI8ToCzvQQ8TMS8ajDVLDjcnXqflMY3xfb2pYoHRlzxtw4jlZ7MIhIxxNzvZergPaSTM_XXVh5pMlLK4HUKb3nX4He3zZ-CH5m0m1wwgurpDn9R9tTCRw0rQYd1uyMENxFQ54qpHwk6qSIxZHNuKTz3L-qYYDAc-E_RY7i1YmYMyh-ZM3l7MdhluFdIfyZq-ZlQtgVH2-veMIXCPGzQaLOYYipIu8UqUDZdjQO8d6A1qWwdSRBxJzp9-b-NhIfcjJhBhfI5XofCKb4ggWHvcB2ltWaIF3RzvpefWCaVR2PFuZ6C-tkGlsbnKQtcui-FCbAcpSFzwnfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26895" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26894">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqb6sQASDvp7jMaBbE5-qdn9Ya-zfNssL7eDtZ5py28fKLgnGe79mXJMfB4rcWMB0vOzKPJJjrGPJpxXwtSNC36IjE2mn3eKyY6ioQmsKFvxvk6kAvhdHTCNO3E2-788TRDmI_Y2kV-cF4CQUiYgLZBaA1e1fJ5hfyyUEt0f0WpAvXNQ2HVHE7_XiD5c_At6WtTJvvOUZZcvgl_9keRkn0ntqB9bZ_u8hUh0GNW2OYBpsNwPLd2rjZZdBiOhFCtvAmtVDfgkyYMnbZgbivC0RYc4TA3mEIFZuPl_Xire-nyMH08hCfBU32m2jIpoZcYfzgukl8aZduKoIDeNsKmVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شمارش‌معکوس‌تاآغاز5+1لیگ‌های‌معتر اروپایی درفصل جدید؛ تنها چهارده روز تا پریمیرلیگ ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26894" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26893">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I07P_gx9zImKwmv9UAwNr50ziTieVA0CtwGn2rqHboE1RHfd_scMPUWGx-9AnOVtBhDVbBY2FsyaUIsRh-0yMn7vW5zt-uikRVQsZfI8wT4A_K_1iaZ2R9FK2RuaAcKATFKSdDh3tgAEmg7fOB60mpY1-SxqFMTkE7PQHX8TNAAIWkdie_LrpX96HbUMdZc2u4F6hVQ02aVQ1fXNnNFMwhviYmm6Gkrhn7AbsHZwAQCQU9WZa25nkWGapy4UQB-QwoUaZvTHc7weEBLpQcTBTRrpVhqOd9ivY-mxL8Uk-AceQ3cfk64ITfU-agdcD6YNkDjN4asDERPPdLmr2MhsRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکرد اشرف‌حکیمی،ژائو کانسلو، ریس جیمز و آرنولد 4 مدافع‌راست‌برتر حال حاضر فوتبال جهان؛ رئال مادرید حکیمی رو مفت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26893" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26892">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9ttpZAGKLIGNe9qgpa2wX1vdX_AN9s24D_ijf7SNeDQ0AayGNUdMZfDQiHv-T4ma9TVj8yVjWKnvN8uF2EfBMxL6bvUiRNOh2AK1Ow9UIyk8nXNys27TKUC8upQ0EO3BYteGbi3twdIglxwQA8r2cdFYKbKMBI9o0r52d2fxsMaDzEZSN2sl0Fhw420MbN4Ku9xuON_1pMoTY6ju-WBu1nJGjgwil0tayxGOFhYAmIrxh3yNcpZaHoT2M6-pgrklJUjOs_j7wRg0kxNhhj4HqF3K-ePxmUgLY1XLcxgkGMIlsZXiA_6lvbtGtYJN4bwijq_kwFs2QWcl44j-faVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیربرنامه آنتونیو آدان؛ این دروازه بان اسپانیایی از تیم استقلال جدا شد و درصورت بسته بودن پنجره نیز قرار نیست قراردادش تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26892" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26891">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgTNY3TN4UnLEekNI7ioV473V5ACcqePVq2leiMHot4fOTY3sPXaUiQyna3el4xjd5w4lqX7lFJfIeJ58r8MeDH1ttjS0y7b9C73O-ZkWNOqGkPZwnNqvbZ0Qg4H5J4HIE-tWQg_ZIx89p7h0PXn4ds26uukB20lRMlwZVLvT4CDl0DUBtYYp6uhCljRm7j3jITP7udNeBbUsxGIy35DztbiI1PIrKCNpDI4fkOF5m14yfJhkLqqiLVCLYt2pJXzxcoDSe3FIiXJi2XBgtD9PoKrvxVRjpv6aXBaC4alMW-9xty76pZiiesXTNK8zkiKVH_Z70XoIWd8f0sZ8qSjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26891" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26889">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbB8AcddGrqGalA3rWI9siQ9GIo0sdFUKHHIDgfO2IMZfUammbPK2RLN-oG8uN3opNEL_qb9bj_tlcc2UTGBPwtpkSdgknfQc6Oy34I2l55Yw8nfXPaAOFKDL_Md7VZHcTkq1zpJPoSWq0A_bU1Hkxz_OnpEu2Fvd-MfmTAN-5lyF6dLP3xyLSinPBOLh8oNq90FnmqeuJpCDhAk3OJlJz5iS08vrTRALE6s1OfRlQjjk5psqSTXvENystVHPxGdcpDMH8MPagVXrUsqGvQgoxT1IWn-C5P79tgjKkXEpYerV32zUOSS9vH6NxS5FUDxSKewZdCoe_SerxwRJjoOOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
همسرایرانی‌خوزه"ممد"مورایس هستند سرمربی پرتغالی سابق باشگاه سپاهان اصفهان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26889" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26888">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSgOyfp_0RP4LKxFyGi5h6B2kGFTkcZfYxSZ6KgfdVdvY7XylZVq9m13RfFLglWhABRZjgiIrhruUzPGEBB_q6RbVSM1VCZz1gc9uxhZVnwhw-3IpQHhJdnW7kuH1ATaAHLWXTFlC6534MsGTwFVptYAQYcB9DZ2-eGfgtoOrq837DTfeDnK8wLT2ngqi9qns2t_Zp2toIPyZ9l6TRIoGUw5m4FXBEdbx8l77ay8cv5zIxESvAFgu7_cTLEPy1QsrArRimZwDZAZ_rtVSf4QG8m0HQf7v0vGy61bmqzdkLi2lPQAq8hhYQWogz5OZpVhJumM8xddqsCvvtLPTpXamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇺🇦
مارکا: میخائیلو مودریک‌ ستاره‌ محروم‌ چلسی تصمیم گرفته که در رشته دو میدانی فعالیت کنه و هدف او نمایندگی اوکراین در بازی‌های‌ المپیک ۲۰۲۸ لس‌آنجلس است. او تصمیم‌ گرفته‌ که کفش‌ های فوتبال خود را با کفش‌های دو و میدانی عوض کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26888" target="_blank">📅 18:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26887">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی از مراسم عروسی کریس رونالدو و جورجینا  که‌توسط AI ساخته شده؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26887" target="_blank">📅 18:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26886">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3GMXMOc1TODZjBPdDnOceXYsIOTywc2EziW-cmEyQnXYGl0VnRtWIFvMm6a5-saL6M4V80BDq5R9yUyFiJpH3ONA74yzwV6Tpcya06EurW0NQD9vspwBMAuA96e5UF-EmepwP6ZL_1it89-JzefwL6n4brbX83bIakY6EprnGRXpuWDw8KB6TT7KtK532_c0D1KTFeWXZbafdo64Z1b4U7sSNvF1T_0IsdpiWvWtdOpnq0z9i-kg-aVwXSNZbkyydfEMzTZuyN8jkHO0FBShdZWfAO-gSMAZloYf7XH7d0w9sTheIy9WAs_B-z9pR2YsZmqHI2cWiQY3bKJwoWg7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26886" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26885">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfeQlN5r26TdVg0SW0C_0rwLixCCyZyYphTX_zGM8VdXEphWnCJuNq8LOcF74S5wyUObmf6EQDGzm3xZdcLAiALI7BbVXiFqitrRBfbpYMxM39o4eOjHgnRh4IPba0sNfy5Gl0hjrj3D7gCVpBBMugNEkhd__D2eCjQHBs0KYMUPyGae12t7AlSmCoY_fUnooZFtw0fG19heaqeYadUsUsSMxCU8cmlbxm0uSLDVJZZP95HLHi3scZbyPsV7mz6QC3493Fz1c2Pxzz3ZKBossW0K1BbsNr2Iqp46qlDwQiR6aQ_QIZ8x2dWuWwqOeMxb68n_BsEE6PjseR-fI9plrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارمعکوس تاشروع‌رقابت‌های داغ فوتبال اروپا؛ تنها 27 روز تاشروع‌جذاب‌ترین‌لیگ‌دنیا "لیگ‌جزیره"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26885" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26884">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7akB0DUAAsBDcD8n0G3eNFybaToO0zTI3uLdk_wescVdp-82dhfdzWZZi2OzuDtHdCgnZrEu-Z8UpBiE4UVI2-y6MRKBp4n0jdYEYAPNNKMoarXyy_RhakfMKr7yyjm1ICsIWLeg0p67o7G0YuYkrwifrlHV-5T7UAvofMbUKQ1yWHvAHhGiBx6rIaxk9gygB7DAw4cpBbHOm0Ph4OzQ26DR6PTsJchokbc5RkPf6_2ZQx1vpJfmquSvNBOIj3UsC3qa3g0xlt9RoroBbJ9km3j_YhWaweUjnaWPOnx4yug4DZODRWB5Rsk3gTGFKiKQ6C5MaWAiOCdrEG8KAFHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26884" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26882">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrXqfxvoAyeRcA5UK-g7IWslmqD9WAL-awUynQk_0DRIN4A3_oxkGJQZVehqkctYl5ocGA-CcZzEY1nBh7JSIKFs_0S2lStH2DTBRpyrJh2d9FFXenvkhoyM5TndMs5VFha2WosiXwfIJttCh0VVA2TGD0sEiVEbibCBEfUUmew6uBFIN5Wdx53kURb366Ng7yM4jW_t1Qv2xUGltTPL8CZDoKY5XnWUYg-568AvUZJ2zjOThkyL0IIn6XwPeXRUWQZ4FBmXw9sm7iXqNtadv28X9pDhKyHn5N8QjENIMWTn_npVIxa38c5M_bB9fYX0hLDL-Dv9lBZBKIxAWSGhEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
وحید امیری کاپیتان سابق پرسپولیس برای عقدقرارداد یک ساله با فولاد خوزستان به ارزش 25 میلیارد تومان بامدیریت این باشگاه به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26882" target="_blank">📅 17:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26881">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT40h3NzjFKmV-Pyez301HUYeJLFoWErgHfTZoxcE0O-cwE09e0yw0l5wmVAVxWNj3DP6P0QbyziZzhH6jLpUC50JJsvWCP_7m4nTjMOwOe1m_aZ2xYvhQMXwYN-PPENOMjtjBeF3R-SiwvCpKQkH49vhdZrxrbc_fYbNPPDkCprEQNMdGwKFDDjajuz_mNViiXgq1qrQTcr-_0IYrXRhJfM-4TOf4EQ92m1nAgcwhPhN8vbjIvID3HBWoH7JyoRGgMZjdBTXztj7_BzA1yitxHacBRFX-XDp4sDwp3422QMrUfQL8wTxgysQTIbqT3LUZTZbk1LuCib7KEwRDpbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوتامندی‌ مدافع‌آرژانتین:
دخترای‌خوشگلِ زیادی بودن که عاشقِ دیبالابودن‌ میدونستم‌ که اونا از دیبالا خوششون میاد، گاهی دخترها میان دایرکتم میپرسن "دیبالا پیشته؟ رفیقِ نزدیکته؟" سرِکارشون میزاشتم و میگفتم:«آره بابا اتفاقا الان خونم مهمونمه! میگفتن میشه ببینیمش؟ توروخدا، میگفتم آره آدرس میدادم و تا میومدن خونم میگفتن:"کو دیبالا؟" میگفتم رفته بیرون مغازه خریدکنه الان میاد، بعد از یک ساعت باز میگفتن پس کو دیبالا؟ چرا نمیاد؟ میگفتم کار براش پیش‌اومده‌رفت‌متاسفانه دیگه خودم مخشونو میزدم و باهاشون دوست میشدم. دیبالا واقعا رفیق خوبیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26881" target="_blank">📅 17:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26880">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e852bLxnA3H4pvm70TdUeh4d98ey7kF0BEezYAYmBYI6gm9rQcFU711WbtETIMhJhBxn7ekUX-wEuG6akgbsiDJBgIRlpeHGS7Q372M5iY3YFxmB8kNnnTMHud8vUR00E4laW7x9jykNhuisfKRn_--krb-bTvkEyAY06gqc4JyZwIQOSDUHa9dURxLnuoDjmQI-Fr8YBFbEF579MDRUbTUJ4C5CDo2nUCVbAD0P9o7HLYLlob9L_PT8nsBkuMQ0_Vc5fd2vQZyCAIZL0RRr2W32WB5ChNEsm28Vnp8qkuRm14rc7HyCcFZwkcYjiors1mpQkgQPV-LjnmF9rcr1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
#اختصاصی_پرشیانا #فوری؛ امیر رضا رفیعی دروازه‌بان جوان پرسپولیس که در آستانه عقد قرار داد با تیم‌ گل‌گهر قرار داشت با باشگاه شمس آذر قزوین واردمذاکره‌شد و به توافقاتی نیز رسیده که به احتمال فراوان بزودی پوسترش منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26880" target="_blank">📅 16:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26879">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=GyJUjKpaPduOroxHL6iUSuwMTHdaAl1Izlyr45zmSoEVKykVnaAlCZTVbG4d3bnPBRwcRccDM3pEgEDQ0nRA-BVrvCLC1nNPHv3xnb6POzbQL7X9Iz97AGgcot7s45zfTOIu_L92WNEZUI0cayTlgPB2t_WZAGuUez-rP3pxxpVXHomcPfgo98XRrAOxoNG8P-QTjIE6l36kj1_AokX_BBmVz7ZNoBgj8V7RLHvea7mjOw6J610gV7Dy2KG8u73ofjppcd2pUtKMadoHjzjL1h3sbih1wljd4VwJF_7LYWJcBmoStrW1v3wPq5hstc-MGMvMmF-Sh0vdXPq5VOOjIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=GyJUjKpaPduOroxHL6iUSuwMTHdaAl1Izlyr45zmSoEVKykVnaAlCZTVbG4d3bnPBRwcRccDM3pEgEDQ0nRA-BVrvCLC1nNPHv3xnb6POzbQL7X9Iz97AGgcot7s45zfTOIu_L92WNEZUI0cayTlgPB2t_WZAGuUez-rP3pxxpVXHomcPfgo98XRrAOxoNG8P-QTjIE6l36kj1_AokX_BBmVz7ZNoBgj8V7RLHvea7mjOw6J610gV7Dy2KG8u73ofjppcd2pUtKMadoHjzjL1h3sbih1wljd4VwJF_7LYWJcBmoStrW1v3wPq5hstc-MGMvMmF-Sh0vdXPq5VOOjIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛ فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26879" target="_blank">📅 16:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26878">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=usgkN3XXy9eJVmfbls6iXRmfaN1xlfIvXGJ2lDSlzxiVnhWGUPeBy3UHEuJFaJDedIb5dk3nhmuxGR0CIUHjzzWIDZmxvPlljzlJgbD7vppP079NswDo8KGKzX3vC3z_Q0bnfqIBVxVSwy4I-LtNSnjJe8PMm7KDD1q6-w-w-RgjuunHSqaXHarfqpbPaQQEFbnv6P5l60mZCNGe3n6Q8HAxp-j5Ev_rw-QkQAHbisnHTgkHKxuj_Oj6hmHMkSRee5bmrS8EptJ_R61G24GKTlPgNuNUjK4kzMfq907DYodRdzbm1xwZMgTDXRUJZZA_QrEymckzHEQisJVV2hwO8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=usgkN3XXy9eJVmfbls6iXRmfaN1xlfIvXGJ2lDSlzxiVnhWGUPeBy3UHEuJFaJDedIb5dk3nhmuxGR0CIUHjzzWIDZmxvPlljzlJgbD7vppP079NswDo8KGKzX3vC3z_Q0bnfqIBVxVSwy4I-LtNSnjJe8PMm7KDD1q6-w-w-RgjuunHSqaXHarfqpbPaQQEFbnv6P5l60mZCNGe3n6Q8HAxp-j5Ev_rw-QkQAHbisnHTgkHKxuj_Oj6hmHMkSRee5bmrS8EptJ_R61G24GKTlPgNuNUjK4kzMfq907DYodRdzbm1xwZMgTDXRUJZZA_QrEymckzHEQisJVV2hwO8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی کوتاه از یه مسابقه والیبال محله ای در زمین‌های خاکی؛ جدا از بازی‌خوبشون و اون دریافت خیره‌کننده‌بازیکنه به‌وضعیت داورای بازی نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26878" target="_blank">📅 16:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26877">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWmaa13DpSKpRgzYVA-qaD_S6gcsdxbSr7_lP8L_bV1URGzZLmBr3B8y4iAv3hIf9fydh9nuN_vFCNYhqUjv1LtokJzwY5Z39n-JGHFN72CilbbUuGLnw5Pad8L0WqYYRPlfciJNytu6vfOTfwt6alBkTewENwpnxMttFvp2g1Cla0_iSMs8Z-Ruu1oEAFUoa3Ty7buzBBCIuw47ZGqIvivGISLNMVKBCplE5dVmM6tafzWFlErp_nJnI691di3AetXDdLIZNylvvIoHskN0jspHfdxRzIeDo4n_3qIObGZYC9BDzRd1ocaTROZxXPltEA9NWpJTlAK8b0-hSrKhfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|وحدت هنانوف، برایان دابو و ابوبکر کامارا ۳ خارجی سپاهان از این تیم جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26877" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26876">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aL_Hoe1Uo-UvY541bjBLI1G5DWQ2VNd-2Ccps0lNrk-aUS8nDYj46SDY930ByGoOJcS5JfyMoQuQO8eLKLnAPEKVuWhK_Ls-ImmaKbJmNIpu08EQu-uyTcqKunX_7N_Ye98Xvxt9YSidwG4uSgsFJDYrDF9WCpCsxox6EZuBWBUQJum6A2Kb2xlltumbw4CEE_BChzRG3Oa6xIRQg5wtj1rZ0QZ2K7xogODCZpYbiClovUpTSrbtg3p9dT69AkqBUwzeNlZ_5YpBh2XH9WgrcpqyQGmswULHyofGwQfy0vPUbDYn_Kbpy4m2GCOnLn_H5Q54y3EKiZsKDDGpKCtVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه تراکتور ظرف 48 ساعت‌آینده‌از محمد قربانی خرید جدید خود رونمایی میکنه. رضایت نامه این بازیکن دقایقی پیش از سوی الوحده امارات صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26876" target="_blank">📅 15:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26875">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=m7P4KYW9bk7l8NhzINVwcSmLI2sulCGqRn15kARiaUML0cf3HQoI3KL4Rbhy7kAbeqwP0Wg_-ZqQt9UEPvX9euNhowfkedQY47b-jjsxcpX36mQdJGbXCB-0ASf7MMhzzSDG9hktZ3TarA2fq-r4Y1VR62OhvVdUCovzfL8-JyuVeN2lULJazrmn-zIQmgT_CF2BaPlFFe1tvkkuyJXjD10rJjBaSdf5AVS44E1XgMi14U0P2uw1VWBry1hx3FWs7iHorIh41cgcnNawSvOc0Ime5J6mymLalu7Pwk9AWz8ZyoR7cVc_iuflt4QDnYtPyif9h4cZzbM450M133UsUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=m7P4KYW9bk7l8NhzINVwcSmLI2sulCGqRn15kARiaUML0cf3HQoI3KL4Rbhy7kAbeqwP0Wg_-ZqQt9UEPvX9euNhowfkedQY47b-jjsxcpX36mQdJGbXCB-0ASf7MMhzzSDG9hktZ3TarA2fq-r4Y1VR62OhvVdUCovzfL8-JyuVeN2lULJazrmn-zIQmgT_CF2BaPlFFe1tvkkuyJXjD10rJjBaSdf5AVS44E1XgMi14U0P2uw1VWBry1hx3FWs7iHorIh41cgcnNawSvOc0Ime5J6mymLalu7Pwk9AWz8ZyoR7cVc_iuflt4QDnYtPyif9h4cZzbM450M133UsUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇧🇷
پوستررونمایی‌رسمی‌باشگاه اینترمیامی برای کاسمیرو خرید جدید خود؛ قرارداد یک ساله همراه با تمدید خودکار به مدت دو فصل امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26875" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxwjo06CHjevcRQFpJiaf8aW0eIqOKEc_PUOKfURghCRt0Jv-DR-z9fJjaCFz-5-95Rnow6lWFDzyxcOv4KwUXvVBFEuZZ2Pt2hV2oA8C4TrayzZTcMRJUa5vYRWLyhs92XA8nY6Nq_NVFunBu40t_-gWhpLKCOTiTNx4BSX9zZXb3kHyZqcyALVyzKt8zyMa20z8xM4SOe0ZF1Rai1EBZ924c11NvY2p3fu8m7J3lTA1GXAm4L9zQAi1lrizVM_pwMEv2chJ7r3su_xEzhaQ2eoii0MoHwzqWBVIcAr4w5crHEDDsQPU2Zc5mpMogZpGEMgsBji_znRLPgtom8JNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiMESEk-0AnwElbCiHtXATedILu766LsKK2ZoTMcoiPmT7G8okolStBlCnzAiBX84eFy1X1CFb0XwVXmBMW2J0huvlltHSC2h5DFcgV2Nlz8kzLOki5z-iOvxEdR4UlsJr7X7vC5pUrLgheszUVm_x31abgQB2UXjKtLctMvBW3womTgwMmiTDq9P8Bpp7FXZ2Zav4P0OvFwuAYD2zj8oTTt45j8GFxsrMSAat5UXydvjUHqiNTk0gjO5AEELXsyuNcS9DeUTym3XugKV_mHd3wC05zfMHY_MdCYKjv8ahHndwaVpnhZ7QtPvUIirqQGKj5-AE6GinLKWnhR2-k4kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=DOxaHsPa9FJh9h1mWceRqoYw84Q3eANdyYLHCrkonsEll5SLblq_JHYkyxQn73yfJVx7B2wPq8F7Mv0AaCkhhiZG1W1q-SkVrDvd4cDuX4oSJSA3G8YGLdltb3o5QmmornvNlMbyzUVYt7jiLa3Ph-1F1bEzaP2DDWYO5WdrJfIBuct5SQk8FSp7mwVDgXurmJGZI6t-XdXJN08kit4Bigu8FWAwRgPqVggj-szvStITVnShBXPp78q7FLRFp47f8_4eL2s74W1g1X963sxQ85LgVEMH2slYTIoNI9bC29Bg1Kr_1PXF1DzAQnsTKsffwyCc0RZYg0YzyInzgomcMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=DOxaHsPa9FJh9h1mWceRqoYw84Q3eANdyYLHCrkonsEll5SLblq_JHYkyxQn73yfJVx7B2wPq8F7Mv0AaCkhhiZG1W1q-SkVrDvd4cDuX4oSJSA3G8YGLdltb3o5QmmornvNlMbyzUVYt7jiLa3Ph-1F1bEzaP2DDWYO5WdrJfIBuct5SQk8FSp7mwVDgXurmJGZI6t-XdXJN08kit4Bigu8FWAwRgPqVggj-szvStITVnShBXPp78q7FLRFp47f8_4eL2s74W1g1X963sxQ85LgVEMH2slYTIoNI9bC29Bg1Kr_1PXF1DzAQnsTKsffwyCc0RZYg0YzyInzgomcMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tb7c4zMeAcsbX0S04YSAtuDCMMh8V5h75Daq8PcHvDAWi8OyCOZSjW4DF3KuzAbWvYG69eDzpFUpPmU3qVweU3FlX-tlwmQ9ikezKRBRzjdkdb6x8a_-dm-OvNGXq_5ZrkWW2sDJDCbRlhyffvufbF7mqbinAHhezdX5XAYEEfzW-YDAXKc5zDgI3Bw6vBLQWb5R_bG5DekD7Vbqu0vJG-w-OCUhlllnzv4qHt0yJ9OGi7ik6rGhGAUyVpLndofr58YG9zpW1T_S1dR6pylAkge8yVVfqiE5EMTLJcveXMLF0VE20e6OudgPLAj8A8GEMhfMSIfp_vJq-RHnDLNjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=g7XafNf6nJXg3VNqQZGO-KjHO2ZNbgwHqkESTVSvfQ_EScOrNx3Qiw-uN2yWmU8s0PXxU3L-N6w4n97OH5E7vMaEl753pAX-8S46EBTetticGPBgGAEbV9WW0AYXJqoIyF1G8nVR8mocnlA7_1rED0jRehIn0xOFHJXmJMWFW-IoWNTO7rlLlrtRUGQgtTzA03Iym7-UuiTvkjhCTS58LdQLkbxqBzlNiny3XnmMEMgJ052l-U6VJ1lSAe_LHjB4_QkmgXZ7QtanMppHoFNz5ti-mS5epyPrz-_BRV_qbXIwdI1c_QjUhsggqPD3ogtDzHA2HURE39Rv0E6H54r77g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=g7XafNf6nJXg3VNqQZGO-KjHO2ZNbgwHqkESTVSvfQ_EScOrNx3Qiw-uN2yWmU8s0PXxU3L-N6w4n97OH5E7vMaEl753pAX-8S46EBTetticGPBgGAEbV9WW0AYXJqoIyF1G8nVR8mocnlA7_1rED0jRehIn0xOFHJXmJMWFW-IoWNTO7rlLlrtRUGQgtTzA03Iym7-UuiTvkjhCTS58LdQLkbxqBzlNiny3XnmMEMgJ052l-U6VJ1lSAe_LHjB4_QkmgXZ7QtanMppHoFNz5ti-mS5epyPrz-_BRV_qbXIwdI1c_QjUhsggqPD3ogtDzHA2HURE39Rv0E6H54r77g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیحات و عذرخواهی میلاد کرمی ملقب به وضعتان چونه درباره تبلیغ مرز ایران اربعین:
‼️
یک بلاگر معروف در فیلمش گفته بود در مهران ماشینش دزدیدن از این مرز بد گفته بود خیلی هم وایرال شده بود خیلیا دیگه برای رفتن به کربلا مرز مهران انتخاب‌نمیکردن؛خیلی از مردم ایلام…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeVtCG8oHsKvwdeYzJdpQRP41s0Piq798Rh9f2rZFdqAPZfDqYh8CUIghSVnFXhxA8EG6Bz6VzTBhtAyr_hMHLlOP-6A_Mc2Zu_irE0i9Krulkx1MwdfKG9JZLLUZdBG9Khp0eg14xVbvuHlqs4IXaK7i0sETOPRlSDPZcS4SEhaVczOXn_8ocQDVtL8kgje_mqj-LC1JebPfspmZn7hDFONNThSBuRuCqWZQvWHC5YHVDvqkau_kW857dcc2liddkvG-p5nEHpXoxdgy2H8AmB3c949UdDFgWy-eN6XblZEDdH1JtLQUF0s6Y1e3X14j00uz6PORgLqUlOTyeUiCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUBFrlmbb1bT5pvM-ew3iA8T2p8tpKIJIwH1NlOMsfyCE0w0_Ee3tXQ43i0ornZpLazvIEPGZtY0Sf4pVeQHPyk4FFbCXP_JwIdpWjVLTL--O3e9jr1XFhQ_v8IN2srfglB03F0x0aFwxLoGv8Qt4pREMgFLuRu5cRmMKCJmaVI3r-Zc1R_5ODHqLn5j0cOQWw-Nw42jTl-3JCnxAGQRCYwtc9EHrNud10NU5EIHLzyGVtyJePbWb80-eTTqZzD5Ebwao6RnYNv3XyrqeskV9tBjYD43jxb2cRj5s87SyIUWwx0_5Npsr8JAcCQXtNbO2CcssgxaXtkyDrkno5w2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26867">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5lzLsxuRZor2oqH-UL_bwz1pH_fmD8nu8_YujxQY6KPARBMwfoPmI3I0bCSmR4ZV7LU9fual0gcQpUupHcVKP1420-MdR7jwF808kypwVVGnF4JooEJup0zgNCQq5Jt1vVdaGtA94iz9sL6M04OIIKYWzyhx9xDNWZRmKwGlfB4-3oerfyHJ-CpNYE-eoJ2w5tGrxRsUv3LcV5UW2NOnCyu0k-58xW2mEDNKL23t_O1B4gSh3Vx6r5YZcFLas7Rd6biWlGnj04aBnq8rSb-GnPA8yT4o72QZISd2tKlu8871qQKjlNNFeo-XRIq4uA2yDsi5vLgDfmOI1b5JJ9A5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیمار داخل یه ویدیو به محله‌ای که توش بزرگ شده‌بود برگشت. یه پسربچه بهش گفت: «من پادشاه این محله‌ام» نیمارم‌گفت: «یه زمانی منم همین‌جا به همین اسم صدام می‌کردند بیا باهم عکس بگیریم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26867" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKhGj6-UXfew9Mybb9w4wqY-VYK1z_LR_kuTCos_mr_3E3pr6V3t-8zOL_n5iLZUfcECzVzSLsT7Xjj4xDRZIV5uMrJd_oQYXoqanDH5RX9oWDU3qhBxTKSfnQ7Z01AIUi-Lu6Sq3poQ7yP5qPcZ2pG165m5mT_qYm_9CiUJjY_niKnryP7CrsP7zo9EREgKcUgJnnOvbPjrKU7h0wSwqaYC7YujOYM9VHKBfPx8FGO5K0d5iJkRF6j8rBtXh_o4-Dou7C2huvaKF06V0j6DU6LTT3xUV_Zk_2nSDlJumP5ErgeTeVruRLDd-0JwinYJxKtxh1mZ66GWuoL7eo76iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afn71SIY9TrSNFzH5Vv-Nm8RXfYZ_07JBZNVwE7Dkqx-YMFYGCvt0xaNp0UntU5TLaTdH03r7npvbNtQv4DDgJt5eUbBhBxVSmblc7vmMEuKx6zl5hYkPottyioylOsB2-TWTl_W0RQpYuXG4udyqE1x0Ei_VPHVdpNz6T35B94B2zjDlFA8VDCPgpqj_Y_3ABTo2zo4cflYcRuDJNdFEVx9byj0KHSVqfAiREyr3hrUyvId4zh5wgchpWo6ckCIOBbMHS8aN5IRP99GGxbKYdVcd4Uak6-325GkSOegeAcs7I_-taSfAa-B022lru14U3qzCebSdBUaHgfvnZcQaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETGFsS3TQOgL-uQnCQZHVlFKldnLSnUkF-uRhfvBvrW3GV1OvPld0Sk9Scx-7ZdIK4TYp2C9C3imyrrdyfclXzsXXsK6yft5FRho9-UvsZfYTOZPAoHtmiotSJGJXk1ubN6LiKZyuFzkYl81C6rrNKI_mflYVDbluph7ZMXSTTJiAj6GBgHsG267dG2uKiE3XmyPpDTT4RplzC8m3mAkQiXsenM6dgiHyXaUdQtU_H1komMLd3Si5q74oq4RyhjgK1AbXUPIFcj4pW1XfluS867sGT2jRPkEbFyJIJkehrv4pWxTWPLaIq2Z6F014Y20CxyQ3ewmGmfTd_nAjEvQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFKeXWvSRG_PRfNobJmDsbwkcazVaFSA_gt4WT9tlzrv4EzBWdMjI4aSKBYvD1oPHjh7kyBYsuIzykkmQ37AKKd1KlXLXui5jZ3lau7O0OLkgC8h_LhmnKw8cyVKjkCd3HroZIn37A-ZTotifKynYG43z_JyKyTeqmzxjVPx8DohzZyT893IV__8fceuiJcgCDbr21UQKf3cTplqk_W8JkCpwq98GHCJjlAErVowhPEpzv3JKizKtUYI-S3g8BgswsXEPg5f_BZaN0ASx9EJ_sgheBPktxAY_4aZKjSSQCIW00otpbKIcV5jZBLVu5E_DSXEfcTdwlCuvRhkprynkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=szhgSDBFtVCs2jsh5VpKxcB2uTVSH76KV_OmGeIZRTzKrflTdnMwUKbUFPl225Qqgqi-RkxZCdbOau7wQvDrAwN7I4bKoMv1yymfmkhu0SOpa20xcLhdHrk_3TXn79bK1_NXeOoSHLRfXOLkKwWJxUxiB1Trge7LhkC4K0sBCpRgdq7q3S3y4N6kvtPnLfi5bBon94Rui2eUWWe3ELSxSFgT9yoiS-VXdzOtW8zu4eFsa1Bm_6-lhKSGeM13QTsgsmXgrCV55iPfcZlkSViPSpjpuoFE9b44E41oYWgAxBjkHL7wXFeOCeU9-W4MgAmyE-If0SglsUIhdljoEzNoDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=szhgSDBFtVCs2jsh5VpKxcB2uTVSH76KV_OmGeIZRTzKrflTdnMwUKbUFPl225Qqgqi-RkxZCdbOau7wQvDrAwN7I4bKoMv1yymfmkhu0SOpa20xcLhdHrk_3TXn79bK1_NXeOoSHLRfXOLkKwWJxUxiB1Trge7LhkC4K0sBCpRgdq7q3S3y4N6kvtPnLfi5bBon94Rui2eUWWe3ELSxSFgT9yoiS-VXdzOtW8zu4eFsa1Bm_6-lhKSGeM13QTsgsmXgrCV55iPfcZlkSViPSpjpuoFE9b44E41oYWgAxBjkHL7wXFeOCeU9-W4MgAmyE-If0SglsUIhdljoEzNoDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwaLzXo5g6rWZSd406Danuufssn5WBedr_DNPu2REGpHNScIArCEfPQldIF0LOK3erXuU4Oa3G-kLG3VPc6epuwb3fyB3OeULNxtuolYBxl460Hr_Rh-UdhLLwxQOwJs98yp4VwuWbwm_qNs1RyWBnPjksuEe9MgU_JnOmENsWhFDxctUEznEPhfMLMEG65Nd0rkzOHKwv8n6kMfdeqh4vOYV7ay5R3WREn1Xux7lbE45Wnb-Zm_e2HIvIl-6RJkXLj10YmTqnSJQmYVEu8ceflRbjfSaI6es0DDRt5v0ew93HSEUZ_IQ-j9pxPRBhPlcZshSYgSS0h8klvadk11Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0CEB53K9H-mpdhkABt6hway8ZtHXF3552Azbpak8EhfLH7VG-Cy2DRNcshwfC54pxTbTTIohYQRnGPExaCKX-qGvx4LmrzGEtwq0e5sWEKsZgMdy-KXb8fK48EIPi9k8fy9a1Q3j7JJ9E3UbdpkTa2Q_23tKIipDGePBDy3DCvK4i56l2yEMZzkxlqKPDnOGk1JisSaRi4pb0_UC4nEyAVm7keXiJR82IzBL8cC8eRcGgoDGWJcTunRbOVyBfc9ZFSMXRqt8tD-OmjjQsbjKIlYy1Cx-jKoxdPBanN-w8v6CL7PbGmL4-EaGXEzxDvVlyMaElc2GbdoMdMsXJNq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sK5Fkqier66wgPo0ltRLDFBwccuRo7cXLj9cc3nyyTrk6QzFjj7DCpqllyulJPBflRnw3IyYrWqOmV_BakSk4C6auJ69Ntvg0uN_riOc0Sd86AFNfZfikGAuP7A3WBFz_boRCCdkReM61VoNXZ5JZylLU2sl2gyiteHOzZ-cE3N7SwjlsQV_4z8FfbwZmIereHbx8CXNHK6JAsx18j9sJ0Zgluyt-N5l6hCOcEOuevAeyQQhG70Oi0-d0SaMoXYVBAHp9zZ367jUxTe4volEpOwxJFITACjjUvWdmNOJ4kM020Ysucm9_Ajsssv7PiNM_4pX4Z0V5qGIhL3ak8EI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26857">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkgB_v4neEaopQttDWyWLGIOmZZoCIMyaZKPvuzp-zg3pmYC8dLTsa8GBIm0EoEw6QxUecgItvWmM-9H_Fe8-GvmNZGUla0Z9_qkUuZcRnSEmEVcY1Rrd3klXKfP5PBLK75trFHS5uiBUJ6prRnoPgGxMlgENdg7cUX9i2Ec4dHyECMPSm3i9a1_SSst4wD4DmlwoAzEaca-3anuWRZi7wGsbbCbYumvpQRAcDLroORw2RdhIQv-g-k2_JXak2wGw7twMEKrT_tVBFOxJUZlo1d-xUdApeMZPWNIzPQ41kCYldkF12X0uCPkTj-_hI38k8sefTANk3GYLbju1YGLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛
فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل به ثبت رساند. سه قهرمانی لیگ قهرمانان اروپا، شش قهرمانی سری آ، دو جام‌بین‌قاره‌ای،سه سوپرجام‌اروپا و ۴ سوپرجام ایتالیا از افتخارات این اسطوره محسوب می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26857" target="_blank">📅 09:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPq_A7b8_iArdKzcZXigJOxx5jKbyE_H7F0KMCxgpzDhP4QSQDacSTjCzQ9uIh074okvWh2-6jJqtVifPGSysKF2Yei0Q6jRWUsrE3FLj61UdeXzE0gDQDvu_p2uU8nqrModoHOjXzjY1Ae22oN5pRlaugPaspJl3PH6AyoMJB8-UsN1KmE1UQPHJeJGLf5Bp54C5q0uw92301GCwgn_yRnO8au-VgqCEzvrRFFjPIBj5j94K_KoBX5CrDvrr5c01_PzOZZnDy4TlgyIj0cHUgCJ7vAYAGyq2vhos2bFjCPgl_7EofsE05MetbN0T0dZZBxOl6Shdw0HlKQmB6F4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IVCshfHXJW7n5td5bv5ZnFzHvrRJa__3PNCkn98Hl3HgDuogR2n45d8QTCt3xSmBpklRFh2_mNP7TjSb3KIfK2WAfUdSxbnmJk058E_mdJl601Fb2BlsciXqQT-qfIYmCiQqHy_jNQeLprnrpNT2Ec7uvw0dv1-123tyLl965BqDNOsCFWNE6fQQqCRn7XJh-fckS6cI6_FQcZ1auWfWQO6T2Ujg51op57J-On463eN0FvShYZUxEzI19TmR6l2H3fvNATSqji1lUwvzsqLXpbVVa3r7v2RyCDTx6GoqRbZ5_1HtmJqMYBMYqsajlOkC9zsZBG88CaBadOhlx_4VLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n5_PgzAFgJxDy80n5Kq-gugxucCyutvZzfJPDOft9bDFo1scqW2Z_GaZxdvgp6Si6bwgHVEXakvcL6GQJ9GlOLxkXh0XAtjZmSQ10oXGo4JSsFhf9VuvZyrpTMNfZ5VRBtFkFZGOuFA3p1LM1ruFFVXG9BUI_QepN2dpjC86gwj1RDRZPKD3Gsw1yUqSgkemQ0bc42yXb07MnTshvAO81kz9wZTdSuJ3EYu0w4WmkwVbOcLwaPfCk7FWC8AWhJsUEX3EnlJUoAWiNH5GPyEyfVTcp7XMFNRoMPgRhPLumVs8Os7wWPnsyYkYpew_tr93ECbeMW_UMAGJ0_JZSV3Ueg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLis7hPIABOWqZbkutWXRly_yeXXwCbkEL02mpm4CYTg4vuw-RgpNgqs_OLvw-mMalp7LxrUo4T9b0JIDh96evDeE1mRcP9MYrVTL-8aZZNAZUDfkGbHcEMGwUmAKt1Pn7XP6Oe59KGC8k1Nv0ll0KZLh88ZgWgioZg9sInm7kQkyc0FcGqB6g7wRvK5y3HU9IJC6Zbv3-Y09LTfBEGxZIeRSNwFkhpMVqEh0cEi3I62IOjN3HON_cQN1ZFNcpuaeYLOspkawNp9rDBd8DZ9S7t-SWUc2ycomxPTBb1gndmzpdSiYRwBCKhMTWmjISyOUjTp0lZoG9KOOK_1njaUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_dXQDUGYg2GB70euGNZ-xmrO-WmO6nVIkHMxRJufjXy56RyKjg4w9Z9pwZg_JNRvqkfnu5vX4HbK6mYbGlRjc_-_zQttr21r-ffbWWUXMfljwrMJPZbpjIyCjXymbCfK_aDAAWAGcdbdIVuvsFEGOCRpjke3dFaEWn-ziSxCaTZJcIOsq__K26Debofv2IUhNLuTpglcJfni0QXrPRPBSDe4lV0Z92zyGzEmQ8kVfXd1rXOAFGI7X1xFNVr5bSg4_4QMHZIs97_LH6seelfWK8pI9uMNebEolq97y16ZbLNwtSzDH3NgU4JdtbLGgbbr7W-L14ywSwlcd1aSg7s4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GArJjLi3Qfjczqw4q7EMWlyNem10ZybT4KRw7OL02FV2RqMc4F3GCQBu8fi-eqBz4n_lTI2ryLhWa4C_NOmq1IYPAUFrmp8aE0lWfvQuqaJPP0QAKuQxi4fB6tuEMzomIfW5WTDJHuuBL9E2-kg8Vk366rC1QxrL0c3L_Tp53L1qXVxHb7AJFvV13kqHK4qtDhTgzU9VVMC0bUVZstb3qsOIqfIUQQDUktkPWeawr88ML9ILHgVcSMezGli9a5RRCDlrXu5CMChJiiQqBCOkhw21l0hkrvBfBOMPpnEXjV--5VRJ1yWL_W74UPocqw_897ICW2cp1EIap6EqxaeFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=aKQXajZAZqCw-7m1wX_a2TCSWQHTlxBlahjpwWrCv-nLSqz35AYBpjVCi1wn85d-ZrwRGx6Lpp1agP2PGwMbJYCGCmUrsUiHihtWq0P4jEgtNYWnZmEPfOL7HZuekMfTWFkCQr7a8E2xFwnkQ1XvPXS6QA5m9NZClQpcsqDH4yFpaNCpn18E0_1xz1YoHL6LTGqf4AhfrsKW_6dDecsUNIi_H4He8pQ-r9BqC8qdkI2fiG6zijWIGqqkDSsddO2EYOLi2b-KbndmWCeZELzwY3SH1IAyfT8qafjTn58YKHWwzlpLcgTHAw2qUZDXlf7ouJhJjc43_CYWW5xpzaHHWUDWy02T6QlrflPgFl1uvbf-EfVUEMWbzlMIfxEVXpWnzIKeQbf8aAt-KRdqg9ZNM6E5VECbnFQIzOdD--L9FDH1LH0SLF7vEZUgxHbHQHY28ACvXxQdsoAIXLmvS0OBLogaDKVKz_7pG_oBLxdDYmhrMSXYl15Pf-p8tAzLVgc6RyFU3xi0ReDBCvhJXcKECaqEGyMfUmCZaLf_Ay-H1AQsTZXobJjuNBi3KhSZYtH6Q_vIoMgQ7eC38mfUgjapMoFghOmX4YovXOqS149oRqQsjfEc-A8Tq8PB_gOxF7Qk2tBTIvrwkADaAingZKTJbK7wa3hxc3VqmXrzE3qKwXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=aKQXajZAZqCw-7m1wX_a2TCSWQHTlxBlahjpwWrCv-nLSqz35AYBpjVCi1wn85d-ZrwRGx6Lpp1agP2PGwMbJYCGCmUrsUiHihtWq0P4jEgtNYWnZmEPfOL7HZuekMfTWFkCQr7a8E2xFwnkQ1XvPXS6QA5m9NZClQpcsqDH4yFpaNCpn18E0_1xz1YoHL6LTGqf4AhfrsKW_6dDecsUNIi_H4He8pQ-r9BqC8qdkI2fiG6zijWIGqqkDSsddO2EYOLi2b-KbndmWCeZELzwY3SH1IAyfT8qafjTn58YKHWwzlpLcgTHAw2qUZDXlf7ouJhJjc43_CYWW5xpzaHHWUDWy02T6QlrflPgFl1uvbf-EfVUEMWbzlMIfxEVXpWnzIKeQbf8aAt-KRdqg9ZNM6E5VECbnFQIzOdD--L9FDH1LH0SLF7vEZUgxHbHQHY28ACvXxQdsoAIXLmvS0OBLogaDKVKz_7pG_oBLxdDYmhrMSXYl15Pf-p8tAzLVgc6RyFU3xi0ReDBCvhJXcKECaqEGyMfUmCZaLf_Ay-H1AQsTZXobJjuNBi3KhSZYtH6Q_vIoMgQ7eC38mfUgjapMoFghOmX4YovXOqS149oRqQsjfEc-A8Tq8PB_gOxF7Qk2tBTIvrwkADaAingZKTJbK7wa3hxc3VqmXrzE3qKwXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcqE5qkMgL9jxj58Q_fpruJxQ0AR-sancfRkruX2Qnspt4nxd8aUAnHoZxx-msdpEfy7NEDfco5GPg_lRGVZW6n15jxlH5JFD2NF3Ghqc63SohY8R_9yfUC__T0capGdWCzWkmdTZBZswYeuP9NIiRfMry1U6NdxKc4KJ58KfkR2QTVaUX50cuGMj07KA5uuC6VxWGdiTa1JrIp2mzSour7C3QKMugdYyAa8a-TU0P2x0Cat5jehICbqwulqsgzWRqVgbm06_mDIHYaxOx8kHAGgvAECQgeTBhXMablbs2A86_cVfilZczNDAJgz0HSNPTH-K0KMFJF0CF7GG5PUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOHOIVVjyFiDii7QLYsCKnvXatHLrCHosY1npO2_gjIBg40oH-ejKILAfhoIGtq5vUv9-gCF4hC9OwWalwLlQcktAYSC8UUs6qk6NCiD1S4kWNpZ03LHuUujiWMQ5bvXweYQMzEybMbKbfxDzyiHp3BAmWWzSpIIlkCUC6A98ZJa5GPqMGEKRjv8XWcJA3-3YOMx878QJ_mWgVd8T3V6J5LHkxVcotA6EcfQ7Fefz71IZU4UHA9ugv7aBOlmgKs-osewm906TGchNHan3oRU-JduTMybcFuRb04yCr3yfQGnLRPl-GFFvZf_DtpLwhjFGUWr8n-6O9ti9-G-x33tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhHWwxvyKVoRFoYrBjOnSWzk9YLhpWfoDBHh2rum-p7QE5xxKysFhlwjRBFtixKIloym5JC-TLJ2tyyc_uQLtNO4V8wNFcD2yWxDzJgY6Gs5oCg02zUjLpGqtcs2xzMJn4DiZU_8F3WlD9q3tpE060XonEAIgaGlqAgI4hbQWXE92M8Z3_ic_0NOQJ_I6lhyp6mAKeJZGHtxuwdsVC3LIexxqzcA3cNoiBr09xfRHwA_SkyFXdjvdLwzrc7W68_YIzFinmCYXANzNzckhWnDEfhEurFC-nhtxEQk2ZxtusdMRwo1Vwh6a7rJsshy_E5BaQTg9DmeHgbRXm_s9VlGgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIsWD8shifSndCtETDD1bcaRmJJjym55ISvE5yFcKO8XtE9ican7DtCtV_ZPIum_S3seu4nHRJpqgnn1cBlYYiesbQnmwi4XoS14COS6ZfD1H-iWIWk5lMsGCofzSMd_cVeyiRpVDM6STkKeOhnwtXOKxVzIt-iozLFaQ4WQ5WGxbYiAZR10TQnGVkp9eZFvftSkY9-pII0A2iC7kgmibBU69hjr5T_UYsn32VCU-J4ulpTM24YEG4Lcva1tDOI2Flgd6gUFTDs0i8nonIzIlAnJC0x89nnPG0LsqAp91ipId5MbGf5UeveKJEjhfaKj9GF_EXgwn0pmTrQe-0NykA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS0huLbhqOLO0ZRT0FrzpBf53P9-N6rpntpMVNtffVYD-Qtn35t9WjwCXjVWNGefii1ma2swFwyum4hslsu16cd1iLIOVCiIxSZk2ycTMY2jkC6_3yQNzUruWKqXC4EbRJjkarS6yUsEZI_brsu737zhyOIYVuCvdZJ1Yj-53qiHbhnQUyTYUv4je69GLOEgR9Dty8fQZaiJ0jZtOqlaw6UzmHFV1pMn99K-HRkv0-lrQKXSBYq40anVzPGyg3FuPkBf544L0c5tpyL-HoLpLKm3gItuvZOLK-CoR0Bgxesw6pwkSOA9zPqHCF-_j6IzpYFzvv-T5vLzDEAuPeo6tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaNuEKrNxz5kMpal1K55DnoE1COJK4fAB2YF3BRGEFm50XjT0gUSkYi1-v5e-hP458OCpMcFdk2Q8uX-jfakpYp_SfQ43DBlIaZaoNpAp-_Ew2oUG1nErMupp70OKWSBazzXp0WyE9cuvhadGoMDvSf6giOkbkXkTQHJFU9PSc7gNWMDKIg7mDaq5XLUZwDs6Wd4OzLajG0tp-1QbuXpDfDDBWKVJDN_FdPJyrKOP85bYwKfhzflafxmNEQkjM8_i0zp7KsyHh_yyraf6gw936eu_9tW0Td3-Yauo6TckVXgXx25GkhS7MqDjfRd1Mab4tpp0iOAQn_E9GGk2V-OoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUcpFGyFtjyiwKJx28e41W0hads1FAhsoMUqpp6POmsUjUcQouHE_iRMZQZ_TYd0agwjym9bRKaNP7XJqIwRWojOiTyB5qMfD9KwDzng-vKk0_oxEnbbVLZYmMRsHO-vjmjeH8dfZO1mkNIkPeNbQY5rcolWOXNVrwQ0duEZgHw6996krkgioiHo8sAfXAmdc_Pt3ULo7aEeCqRZhbf7n-C1DIuY2oWdqprH-Y404rKseSHqmXJWbARXRnNqP0ZUcEsSmY9bp-7uy7F_3poJcOqQAH9wDKaVGLEWdMJzewd0nvcD7ZIuAJJshXsC1GpkFAKa0LN2HSIcVzlN0RrncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTLflXyn7DoM020o1rTaAUY9dF-PGtX9fZA1jqPMJM4a0jBXoEMhFsETNWFO7CdvfwocMwhypjODYpE_u_TiFfMy_CpTzKQhnlrE7p6LogIHSiDF-sPQ1RaOWwiEx3R1XejZ7jkJPtO5FgllogIKX_oUKTWwZuwbmr82Cs_b7MhLk0Y-7IcpC1ntZZjfWpttpveWRU40NHAcabhppfNEsu2bzRih_48Y8yyqEutjdBz2qDEQlNWauOnLUX9e3AlDFdDTLb9E9ncYWJCcfLcVwjdMecmfPH8ypGlaE1U19wEfC7iUMP5x4iIXnwHKayzqAeS2koiWUzh1dqIBmqtPow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
