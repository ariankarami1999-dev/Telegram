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
<img src="https://cdn4.telesco.pe/file/JnD4FpKP6RkHAVy2jSvlN67E1sV3MadOIrwXHe85QaKX7q7bSXUjy15wVVIiSGBUb7LuI4sy60XT9pOzx80W4bBLmexS36nshkVsyHHIQsjrevv2vXlZHnURuvInzAiup4AW1Y-K-rJk9Xwf4ckNr2yI7PlQWoCe3vyXM4y2yeyCfIKEd3e2PDTAsBlH5hXQDZY4fpSY6aXK_cW_cltUtm0vreX0nqd6sR2X0ByoHkkrzVhAl2dFHTI_89WOgN5tUfNendZNp29xg4bEZrlPwrUonJy7M5nAmruvmJLAtjPrtfSQFPl-cjwwmDmvArXW3jHy3B5iAyEYs00mt-fcTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 965K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 11:44:08</div>
<hr>

<div class="tg-post" id="msg-141451">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msl9Sw0pn0OlFd00K2cfE3r6VADkZXl1reCR2tFLU1Yhb0cDuWYxa16U3zCE4bYhhs9Rrml65QyT7eqACWTozJdHpP8MHzIzstohrpMi8HxCt6iPirmkRwNb89epe03UZ9K23K6n504B2D6gX5ce4NUtJBHOubovGer5fkPdOMuoaz7QFGbXuXjelWZ6OOgQ-Hdjv1UpsBy2zdb8AkwS4OYCzergXtmL6W3zE64m_jhwAU95crOr0HLQddkiostZe1qOsQtPF42aqPIrzjNx-9f8xwq_w4IUF9ucyqmyXDvqPLPaa0IUFgNg695vjrvKBpUbxIXSWpLEHVyK8LTnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یورونیوز: نفت متعلق به کشتی تحریم‌شده «کارولین بژنگی» که به روسیه وابسته است، به سواحل عمان رسیده است. این کشتی که نزدیک به یک میلیون بشکه نفت حمل می‌کرد، در ماه ژوئن در نزدیکی جزیره قبیلیه منفجر شد و روی صخره نشست. مقامات گزارش داده‌اند که آلودگی در راس مدراکه رخ داده و جزیره مسیره را تهدید می‌کند؛ نشت نفت بیش از ۶۰۰ کیلومتر مربع را در بر گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/141451" target="_blank">📅 11:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141450">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d7922013.mp4?token=ejV33beWrLqCRP8HMGyxuYP_HemxcJgRtSOUG33TDfPW_hQuGZHUZ5Cd_cuN2g3gNr_g6gaZmHLmKfHbbUdIMjxdPMkYcT84XRDeGgDOFbKx7oJ6LJ44ZdbcC2b5lFOCOSX23MNyYN8ygZXH0Cbn-bV5Q8ZTF1_xVq5LxS2x62gUmNdYaxWQz3o6jPMcpWyKMNgx8T7PKobWB9SWQ4IUFv_7ZXCEip5eZ0sJgIPyTAUYynGXprUzfV8Djp7T2XyRsDWue3r9oDJf3JvWcYZyckqJXoRHS4d12rgM5-EBx5S9yDEVUiDJ_H_kH026SzCjJTQBjFR7Rr1ZmP7d5yXScw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d7922013.mp4?token=ejV33beWrLqCRP8HMGyxuYP_HemxcJgRtSOUG33TDfPW_hQuGZHUZ5Cd_cuN2g3gNr_g6gaZmHLmKfHbbUdIMjxdPMkYcT84XRDeGgDOFbKx7oJ6LJ44ZdbcC2b5lFOCOSX23MNyYN8ygZXH0Cbn-bV5Q8ZTF1_xVq5LxS2x62gUmNdYaxWQz3o6jPMcpWyKMNgx8T7PKobWB9SWQ4IUFv_7ZXCEip5eZ0sJgIPyTAUYynGXprUzfV8Djp7T2XyRsDWue3r9oDJf3JvWcYZyckqJXoRHS4d12rgM5-EBx5S9yDEVUiDJ_H_kH026SzCjJTQBjFR7Rr1ZmP7d5yXScw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه کافه مذهبی با آپشن‌های فوق العاده توی تهران راه اندازی شده:
اینجا آمریکانو نداریم، فلسطینو داریم
نوشیدنی‌های خارجی مثل کوکاکولا حرامه.
موقع اذان، توی محوطه کافه میتونین نماز جماعت بخونین.
پرسنل قبل از پخت و سرو غذا و نوشیدنی، حتما باید وضو داشته باشن.
کافه، نزدیک مزار شهداست و میتونین دیتِ خودتون رو اونجا ادامه بدین.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/141450" target="_blank">📅 11:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141449">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/141449" target="_blank">📅 11:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141448">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای زمین حین خورشید گرفتگی اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/141448" target="_blank">📅 11:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141447">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ny0p6QLTEmZDIbxJMEIpuNnaGxtk2bOPXoZuhlq20qMiPLZKRi6BOVOJEpKa-6xFDoNW4RQZkmhWie-H_O6CVvbGAGrqJAbc9l1Z8SZeWOvMX43BUrJ9zqlIUrg9ShN9ptPeQphNmBCuRmScdfMnEIe63kNUJyyrREGQCwDlrKC1xygbixFRJZDXhyHFrXuAaGwCcgdbcSWKD-PDoFNBayZCcNq3l_PLW0heHi0QwdCD1eSRvpkT-VLntAhsChAKRJ_EjQh61IdRHB3ynXPJa1gM3qLJ1IA0de8eug71QAVioi6klF5A2Fa9jjT0nW23ENSZwsTOwZohUEO9rKFKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کلمبیا رسماً به ائتلاف مقابله با کارتل‌های مواد مخدر قاره آمریکا پیوست.
🔴
این تصمیم پس از دیدار پیت هگست، وزیر جنگ آمریکا، با وزیر دفاع کلمبیا در پاناماسیتی گرفته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/141447" target="_blank">📅 11:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141446">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2711d095b9.mp4?token=nJHxoo6GJWoIxkcMvyIYxvtAdel-EVbfKJYWFFdeDG3tyKPTMs4PLOwc3BBMeC6Gzo8irvFhrY5um6rXleXb-YtYUPmIFfxiuwEscHsSsGAYnTFNpQjFxbPjzlRSwyDgoVLTqJjEsBBAzXckfFvNMvRY0b5QlYwviMF58kYFSlNsunrlll5k4zSuC07yyT7P03uwMgYim-AF4_jVFreadfBbY22zRjWrXVWU64raIVQCeJ3Fwlap348cZt3W9ClHFDgPh2KH-7yeWY-p5-USfEvbru-Tz9U3uccD6WwlAbzwhZ_hQIEu0P310PSo7yex5gdGugGVmzKdVmH44g8sSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2711d095b9.mp4?token=nJHxoo6GJWoIxkcMvyIYxvtAdel-EVbfKJYWFFdeDG3tyKPTMs4PLOwc3BBMeC6Gzo8irvFhrY5um6rXleXb-YtYUPmIFfxiuwEscHsSsGAYnTFNpQjFxbPjzlRSwyDgoVLTqJjEsBBAzXckfFvNMvRY0b5QlYwviMF58kYFSlNsunrlll5k4zSuC07yyT7P03uwMgYim-AF4_jVFreadfBbY22zRjWrXVWU64raIVQCeJ3Fwlap348cZt3W9ClHFDgPh2KH-7yeWY-p5-USfEvbru-Tz9U3uccD6WwlAbzwhZ_hQIEu0P310PSo7yex5gdGugGVmzKdVmH44g8sSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
👈
عضو هیئت رئیسه مجلس : ما حریف مافیا خودرو نیستیم استیضاح وزیر هم چاره‌ساز نیست
🔴
محمد رشیدی عضو هیات رئیسه مجلس در گفت‌وگو با رسانه تصویری «آن»: با وجود سال‌ها قانون‌گذاری برای ساماندهی بازار و آزادسازی واردات خودرو، موانع و تعرفه‌های سنگین همچنان مردم را مجبور به خرید خودروهای داخلی بی‌کیفیت و گران کرده است.
🔴
ما حدود هفت سال برای اصلاح این وضعیت تلاش کردیم، اما صراحتاً اعلام می‌کنیم که حریف مافیای خودرو نشدیم؛ حتی استیضاح وزیر صمت هم در گذشته نتیجه‌ای در این زمینه نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/141446" target="_blank">📅 11:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141445">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DznwD4N0n56nZy4kqa3NzGuBxhJEvnhDpOw7LA5pgm3fisCojAu57MDPYAxL9_1gxXNjUVI-1EaGJZifIBOLlESCtKSVyrhxOzEoY8T9xBBVlaGV2qau1QbvbyWQaabgN_ZVzGqsL6evWqVsdyNoHZH1m-I7rUPqidzfyuoTLQaTDihKQemf04c8FDr5mE0paSVdOUukqeqjnwu8c-HcBtM8pdWoz-_nnpPWzWxhuw10V4z9IbjLg1CvDqGux9-8OBAtVoSSFhs53BA4yE1qwUbZXry-PP7lqEuovl7slsmMARRNYQVxRgwwRjNGfzticksI9ybvvsVKGNPtmYes_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتورهای دموکرات خواستار تحقیق درباره وضعیت ناو هواپیمابر آبراهام لینکلن شدند.
🔴
پس از گزارش‌هایی مبنی بر وخامت اوضاع تا حدی که چند ملوان اقدام به پریدن به دریا کرده‌اند، سناتور ریچارد بلومنتال نامه‌ای به پیت هگست نوشت و نگرانی خود را ابراز کرد. سناتور روبن گایگو نیز خواستار بازدید رسمی هیئت دوحزبی سنا از این ناو شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/141445" target="_blank">📅 11:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141444">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
فرشاد مومنی، اقتصاددان: ابرتورم در ایران رخ داده و وارد مرحله فلاکت شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/141444" target="_blank">📅 11:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141443">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff225435fc.mp4?token=VnSxKCAvmDKJzPiZjEDL5VPUbNb7IahKQuK2QwsC1WoDiSk4Ahl-F0-U3WpaaZnWwFD2ihoaLzycwGp1_ce5lfhk90cdUisYj3r8r_7wJI3aSOIf3FH2u1hQHs7UndpyKjI949CBuqe1tJsv5_PhrUoHVlf05Zurtc15X5MSYQFBCJ73DBis4KgLqCLALw1E8HbGeMrvjrQPFC0a1L41uk8VHSK75JdZyS5lToZjjor9TrLEG3XMLLx936MJzJs-ZIy99NQo7Bix8H-A3BgXg2ur4pzqdGBFg6FD5udFA_8iUcbRa4IaK-Fpv6f-QimKRHv67EFOGxaGd5nuaLecGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff225435fc.mp4?token=VnSxKCAvmDKJzPiZjEDL5VPUbNb7IahKQuK2QwsC1WoDiSk4Ahl-F0-U3WpaaZnWwFD2ihoaLzycwGp1_ce5lfhk90cdUisYj3r8r_7wJI3aSOIf3FH2u1hQHs7UndpyKjI949CBuqe1tJsv5_PhrUoHVlf05Zurtc15X5MSYQFBCJ73DBis4KgLqCLALw1E8HbGeMrvjrQPFC0a1L41uk8VHSK75JdZyS5lToZjjor9TrLEG3XMLLx936MJzJs-ZIy99NQo7Bix8H-A3BgXg2ur4pzqdGBFg6FD5udFA_8iUcbRa4IaK-Fpv6f-QimKRHv67EFOGxaGd5nuaLecGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
لحظه‌ی خورشید گرفتگی کامل در تاراگونا، اسپانیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/141443" target="_blank">📅 11:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141438">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwIwUOu_ZWuiFyOKW_fnmOArvwHzuvA0T7yu8_FaskH1gaiv7IOfFogLH9aI26NoZf62mYOiajyXePDhDnS9v4qUbT50oMdVhcq7QY2Qz8mPnLOOPcOX-FKoZ5PY9ilo11_xioEdYZEit8PN2PHT83Fl4G0_hZ1xVLKcGcToI8LtABazDxIqvMXuX_QrS7AktfQXs8nw3NLL9JDuxgYsE_I1j7WKeuUPIBh-D7k4qtydhsuew360PVBFnQDPHH3uRCsYgTVgRGQ0lLIHgiqqiSAIkvy1krP5KoIa6J2PGgb8_WJGn0-1SngmWIT93LWFQMidOoPesKa2sQd2w4XkKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0vaaRA7aHQ04SPHSmZA3sBsCAoAbmSptmQW_k-atvmzlkPuWrLIOmutTzJeAMWGN1a4ZEj0JNWluwR_6I73T6mDM5NLtQTU0-UvMVwSRx9yTgh2R8DHuzqlMkUdTDH6o7iKTEJ10CSiqlxHBuyAVlL_AqoML7qmAK8n4uV1oRdnA77x5XHZSumx8ah6zLwulQPU9_9VkkOYrjktvGCCABS9wHPuj9DyBbeFYILetG_j121uP2wu9VASIgCbriiXvU46yE0CrfeZPwDuPaaLbRNS49Md0oLKAXR0fOkl1abBeU32qBl3skMlOqUq_qzLAIYYEu4Ma_umACY3QZReDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAMmxw4kVivwQ1Y0Omb1oZIOk3H6-fSLtgeDX7vMLDpN6x6owPo076xhg6AQ3X9qdCHNEhZ4JWQ9lQuwQX6Rvx0Sy2-1kUinMn8tx-8jCT8EQZzY52xYAlYEsuIlwHz_dzPQDBl3fZM8oULKB93CiizUd0Ph1xgkWduGePX1czoerCTUxqwAM77CcxngNa-OwJsOFhMCaiNEhya8toR8QOsQTB1TcE9H7kJ3LnndZZZxx04OXdKY7STW_l-AJSppDFZTL47ciDP1p8E9zGYBBoOmw92Y57c9_Gtr2UMyxenKybc2oxbzZhUadNEI2lk5ar4PR-R4EEnT9kugag6EJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XbiLZAzqbAcflJLyIdYMuVv9F8rTRLI6Q0o2HYwvDWGG7cmMfOjb2VUrg10OEPi__HawrsCDP5kLgqNlelaRpvj1HDMtq1hd025FDW_T0iv8uiPO7OjYmxWiXNptPFtl51ttJb_AJk9WuHzip4ZalZ93E4730KrUkThyBb76CUE6Uj3sxIk2RsJZ9pqcsa-S6rOr_pZ3KWG5edGLDYE3GwNIiSx3dzXDPjMo-40RSJ2MkZspGU5Vx8qPH3pCMoxsJJgFuINux5jTMvQ4iitwLM5OT3iQKotqjBwvrjKWen6nvl9-zHI2u8UzMttfvoTUZmsh-qgfc46nU7TGH4g7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KScl5IgNBX0nTpP22FjbT1INOQKPonqEia49aiI_8E2tvrlrPXlNCcdbE_Uw2Oz0By34xJ6V7JlT3925Z8hFrFshHKIhLOAUU3pqIe40U5yaeL-f1lPk5-VH2gydl393cfV7XRlVbET5V28ypbweF-jfBVGiR5BX3ZXQLNGN5TOvbHRN3GPZygIzTmFNgC2TOsTx2AytyhptLFJoXbgl8_wCMN25uTreJWd_lbohJNivpPts9qfSw_m7-xTqULKFejPSgJgJ7cMiUo0HeYADbo_pxJBMYtZT4rrGGsnU3ZqSaYS3o_lvl_42US_kddSuEOROSLObjqRYPvOze5IrRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از خسارت به تأسیسات ذخیره و بارگیری غلات در نووروسیسک پس از حملات شب گذشته اوکراین حکایت دارد.
🔴
همچنین، یک نفتکش در تأسیسات انتقال و بارگیری نفت نیز هدف حمله قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/141438" target="_blank">📅 10:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141437">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏
👈
هواشناسی: گرما تا یکشنبه در بیشتر مناطق کشور ماندگار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/141437" target="_blank">📅 10:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141436">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7nMd1gvXARKkrcbXxZYrOmGlt34KzIuqyrdVjB9_YW2gRC3_d8r_IjFix1gxaYZp5HDrjuTD9JxaGUL7EbW2DblID70ztXPJ3tZJjBRl_mdGB_HihTYYJmB74eyM9v323R_lQl46c1p4-Y-MfMo25-QYtq_C0aeSFwSwy-33rvRI1iiHHGYdBtczxfaQ47Ekh6UrX5YyUmuJRlopQwRj4yhrLnFMGcaX-7bqSmILoNzcccPiUdCdxqIB1mjsI4oqI24WAfYDxvSA0vDlBlwyXUhhvVNODkm3Lk2pxxtOPKyGSAP8-xSYfKR60vns4eAuvQlSiRCtN7_5aa1tKkmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست: همه گزینه‌ها درباره کوبا، از جمله اقدام نظامی، روی میز است
🔴
پیت هگست، وزیر دفاع آمریکا، با اشاره به قدرت نظامی این کشور گفت: «هیچ‌کس دوستی بهتر از آمریکا و دشمنی بدتر از آمریکا نخواهد داشت. بهتر است با ما درگیر نشوید، اما وقتی مشکلی پیش می‌آید، ما نخستین کسانی هستیم که وارد عمل می‌شویم.»
🔴
هگست همچنین درباره تحولات ونزوئلا مدعی شد: «قرار بود سامانه‌های پدافند هوایی روسیه از کاراکاس دفاع کنند، اما کار نکردند. محافظان کوبایی نیز قرار بود از مادورو دفاع کنند، اما نتوانستند.»
🔴
او افزود: «اکنون شاهد اخراج کوبایی‌ها و روس‌ها از ونزوئلا هستیم.»
🔴
وزیر دفاع آمریکا در ادامه درباره کوبا هشدار داد: «همه گزینه‌ها، از جمله اقدام نظامی، درباره کوبا روی میز است. آن‌ها قطعاً حریف ما نیستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/141436" target="_blank">📅 10:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141435">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزارت دفاع روسیه: سامانه‌های پدافند هوایی ما شب گذشته 362 پهپاد اوکراینی را در مناطق مختلف کشور سرنگون کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/141435" target="_blank">📅 10:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141434">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
‏فرماندار جاسک : احتمال شنیدن صدای انفجار کنترل شده مهمات  در جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/141434" target="_blank">📅 10:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141433">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
به گزارش برخی منابع عبری: امارات ۱.۵ تن طلا که از اموال بلوکه شده ایران بوده رو اورده تحویل داده تهران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/141433" target="_blank">📅 10:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141432">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
شرکت امنیت دریایی امبری: عملیات نجات یک نفتکش آسیب دیده در سواحل عمان
🔴
شرکت امنیت دریایی امبری اعلام کرد: ما در عملیات نجات یک نفتکش آسیب دیده در سواحل عمان مشارکت داریم و کشتی‌های نجات در مسیر رسیدن به محل حادثه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/141432" target="_blank">📅 10:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141431">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نقص امنیتی در پل ارتباطی میان XRP Ledger و بلاکچین Coreum باعث شد مهاجم با ثبت تراکنش‌های بدون پشتوانه به‌عنوان سپرده معتبر، حدود ۲۰۰ هزار توکن XRP از ذخایر پروژه خارج کند.
🔴
تیم توسعه‌دهنده اعلام کرده کد آسیب‌پذیر شناسایی و اصلاح شده است. این سرقت طی ۹۷ دقیقه انجام شده و موضوع نیز به مرکز رسیدگی به جرایم اینترنتی FBI گزارش شده است.
🔴
یک خطای نرم‌افزاری کوچک، برای مهاجم به در خروجی یک خزانه دیجیتال تبدیل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/141431" target="_blank">📅 10:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141430">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_QbSBUbBElBsLqi0MNb8fKUfWo57iewUU4atloOqPHhL_eb5zMTdt3YojRU-zSbbY0MqboMaqzzvP_GvzEToBQkUkMtn_cjg2KJjLHns0LuecA7multfj9OTMeWQ8-a8YNF60a92J54l_ZNCNet1jtJ63YpnP_Ci4Uybs_HWiwGA5zfxn4rGzO8xXkFYo-55LVifLIMaZwkmIWofl6IQQeNjVU1a1BK8LoYIeMAgo93KYkKmW-shJHR0k6QCmNqu7YEHirp0Y--4AltoBOFV_Q-PjebX5W_Vz6c3_H4RPgaDzSeCLoyIPsz4ufkBsfAup_1VnvBXToUbvbnwO2QNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
تصویر روز ناسا؛ خورشیدگرفتگی کامل در اسپانیا
‏
🔴
۱۲ آگوست ۲۰۲۶
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/141430" target="_blank">📅 10:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141429">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17fcfa2fa.mp4?token=Z7zqaMde4lIgjsU1bHXYkNUXm7XQlQ8gkIMnMtXs521tBFv_jK4TvEYR_4t9PNXykw5wxuWIrbwqbtZ3sR9J3v2aAr1qbH-1MHB-2RzlpCS5eBtGv3h9ev6b868civJY49svbnwooX-h3jPgQR8-pccb-8mr7Bvi6vt9TA3pIpXGqW_2R4wc9MFdTxHfhutr5naMrUNBvj3dEn7BsA8n3R1jWN-ePTBZaa6op1I5v3iuscHtStNS8YRpgyVPEIXZ9qqy_L7yMGRmUFEwurHAqb4w2FY526mgl408HZHIwm4Mkn7gKANNh2sou_9uQNPfXgKvKVsTqLPMycyH36O8hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17fcfa2fa.mp4?token=Z7zqaMde4lIgjsU1bHXYkNUXm7XQlQ8gkIMnMtXs521tBFv_jK4TvEYR_4t9PNXykw5wxuWIrbwqbtZ3sR9J3v2aAr1qbH-1MHB-2RzlpCS5eBtGv3h9ev6b868civJY49svbnwooX-h3jPgQR8-pccb-8mr7Bvi6vt9TA3pIpXGqW_2R4wc9MFdTxHfhutr5naMrUNBvj3dEn7BsA8n3R1jWN-ePTBZaa6op1I5v3iuscHtStNS8YRpgyVPEIXZ9qqy_L7yMGRmUFEwurHAqb4w2FY526mgl408HZHIwm4Mkn7gKANNh2sou_9uQNPfXgKvKVsTqLPMycyH36O8hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عمان و عربستان سعودی اخیراً «کریدور سبز امن» را راه‌اندازی کردند که این دو کشور را از طریق الربع الخالی به هم متصل می‌کند.
🔴
این مسیر شامل حدود ۵۶۴ کیلومتر بزرگراه در سمت عربستان است که با هزینه‌ای حدود ۵۳۳ میلیون دلار ساخته شده و برای کاهش هزینه‌های حمل‌ونقل، تسریع ترانزیت کالا و ارائه یک جایگزین زمینی که گلوگاه‌های دریایی کلیدی را دور بزند، طراحی شده است.
🔴
پروژه بیش از ۳.۳ میلیون ساعت کاری برای تکمیل نیاز داشت و حدود ۷۵۰ دستگاه سنگین که به‌طور خاص برای شرایط سخت الربع الخالی انتخاب شده بودند، در آن مشارکت داشتند.
🔴
ساخت این پروژه نیازمند حذف حدود ۱۵۰ میلیون متر مکعب شن، پهن کردن ۱۲ میلیون متر مکعب مصالح محافظت‌کننده از شن و استفاده از حدود یک میلیون متر مکعب آسفالت بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/141429" target="_blank">📅 09:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141428">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
واشنگتن پست: تحلیلگران سیا «اعتماد کمی» به اطلاعات اسرائیل در مورد توطئه ادعایی ایران برای ترور ترامپ در ترکیه داشتند، اطلاعاتی که سرویس مخفی را بر آن داشت تا یک عملیات امنیتی فوق‌العاده برای پنهان کردن خروج رئیس جمهور از کشور انجام دهد.
🔴
یک مقام آمریکایی گفت که گزارش‌های مربوط به تهدید جان ترامپ «از اسرائیل سرچشمه گرفته است، نه ایالات متحده، و اعتبار کمی دارند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/141428" target="_blank">📅 09:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141426">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdb171b134.mp4?token=TeIutK9BmQ1WbtFBe4lNI8vjkIO83fIQk_tRe04Ymqe6cnHX_BOtvx7lFztadzwLeHVhKB_9ojgVdAgenlDvzuntBIjX4u3k9IaZDDcj7KtsV7QS-qJR3Sg2JWPTwLVp97G7XCXKtoLJ4DoFDLSls_w8XwEojzZU90wzELT6IX6DjlZ_tcV1bm7XokR8_6Hdu97vdIqf9vTDkJ8UDuvAUu5HTKb8Ic8K6ywCEMmdGgp09vFZw6FcKCoQorQ1vJKH5xP7s8e5RpUBXnEjyK2yItzb9xobhV1Vf6OuT9jVf4ICbQ_PynAOLVJ_WJfD4wjdSiIdt7LkL_Kr-g95RdAZSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdb171b134.mp4?token=TeIutK9BmQ1WbtFBe4lNI8vjkIO83fIQk_tRe04Ymqe6cnHX_BOtvx7lFztadzwLeHVhKB_9ojgVdAgenlDvzuntBIjX4u3k9IaZDDcj7KtsV7QS-qJR3Sg2JWPTwLVp97G7XCXKtoLJ4DoFDLSls_w8XwEojzZU90wzELT6IX6DjlZ_tcV1bm7XokR8_6Hdu97vdIqf9vTDkJ8UDuvAUu5HTKb8Ic8K6ywCEMmdGgp09vFZw6FcKCoQorQ1vJKH5xP7s8e5RpUBXnEjyK2yItzb9xobhV1Vf6OuT9jVf4ICbQ_PynAOLVJ_WJfD4wjdSiIdt7LkL_Kr-g95RdAZSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه ایران، اسماعیل بقایی، گفت که حفاظت‌های زیست‌محیطی باید بخش جدایی‌ناپذیر هر چارچوب آینده‌ای باشند که تنگه هرمز را اداره می‌کند، با استناد به آلودگی‌های نفتی اخیر در سواحل جزیره قشم.
🔴
بقایی گفت که شواهد اولیه نشان می‌دهد که یک کشتی باری خارجی منبع این نشت بوده است و آلودگی در سه مکان ساحلی و در بخش‌هایی از آب‌های اطراف شناسایی شده است.
🔴
او گفت که دهه‌ها آلودگی و فعالیت‌های نظامی باعث خسارات زیست‌محیطی به ارزش تریلیون‌ها دلار به مناطق ساحلی ایران شده است و استدلال کرد که تمام طرف‌هایی که از حمل‌ونقل دریایی از طریق تنگه هرمز سود می‌برند، مسئولیت قانونی و اخلاقی دارند تا به تعمیر و جبران خسارات وارد شده کمک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/141426" target="_blank">📅 09:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141425">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj4jYU_4JX7vdvR2c3axM06Rq1A3b2eZad209-UFXhqXgYyvuS3s6TADYETEDUS0PaH2n9Lgyk70S5Xl7LHqCpYIIRx1EW5egqiZmguJRM8zNNqpNflPdnuBHEGBwCYUM4qFRTs4fCjqoctv5LNg9gN4OHJBaMWVTiEBF6hdRr3BfcmdwiipO1r5Wu8Qq5clTGEXtteKUGOxxVW2T2rMtJcdwD7bho6Ce1Dka8FVmweoBv2G3jeT983IjUUwPiHHaOGpFL3thIJl-H8UUznkHcJil-b0xzuiK7IxiaBx7um-4ymY0LI2PTBdqOyl9ctrz0d2IPtLCzK1B-Lt06_SZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مرد ۹۹ ساله ایتالیایی نامه‌های عاشقانه قدیمی را در یک کشو پیدا کرد که نشان می‌داد همسرش در دهه ۱۹۴۰ رابطه‌ای خارج از ازدواج داشته است.
🔴
او درخواست طلاق داد و به این ترتیب پس از ۷۷ سال زندگی مشترک، به عنوان پیرترین زوج تاریخ به طور قانونی از هم جدا شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/141425" target="_blank">📅 09:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141424">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA2f-24nT_ssg8G-XqOyOi29QjiERuUq5bQVZEZO2xJOFk19RALOZxnWn6fzctCNNv9UTa3jRbPvQwWmA3jZm36lXFhj-JUW7OsLnwdCrd-_TnbKowHRrfCSXalfl7BtCJZKjzsMOyaSVsYIyn1ZOH372HZrJEFLu6wvA8o93X9wrlVsXP7rIEuQIiF2YSBd02_RH6dEUMeoXd5MbiaKdKJSl1-ox_7N15i5W9PWIO_Q-smBJtICFH2f8EaFuViInaNuYBzUGxffxlw1lFSIJBPJj8UjLqHQjLGpwd1B8OYfvNhhtPXgwoWFLPCr0nUFGgst394SiP4GLvsOAI10uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت حمل و نقل مصر:کشتی "تهامه" (TIHAMA) که مورد هدف قرار گرفت، در سواحل یمن قرار داشت. این کشتی قبلاً هرگز وارد بنادر مصر نشده بود و در مسیر سفر به مصر قرار نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/141424" target="_blank">📅 09:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141423">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsBuFSw4rY39-NYTbQe05aLMvC3zKsnyxpPsb4_nGmjERnRx8TEZemGf0hpWB4NkHX2jbxh0tUdeguOtWAI3-53Ayyv6l99neNrpAtPOYQrI5Xsf1vwSieTEmwzQk8J0ywsxYX7l2JNq2HoH_-hQguEHFdDWuqXVJoO3aZ4llPmSITxfrth3TVq5sSxdWZ4cPldPnrFukRQEOIOjdHCbypLbxvfN_L4kxC0kuNZTO9AgqukI5chXZYMdkmj2xY33uOhE-2gqWCQQqJhlPDSBYrbVUwCeoxjtTNzOWUUiROD9gPEs9SjQ7dQ5WtXKBg2e7KCPYdFTyfnaiOWn5pCkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آلتمن مدیرعامل OpenAi:احتمالا تا 6 ماه آینده، Chat gpt بتونه صفحه نمایش موبایل شمارو ببینه و بخونه!
🔴
به این صورته که کارایی که در طول روز با موبایل انجام میدین رو میتونه تحلیل کنه، مثلا وسط چت با پارتنر یا رفیقتون، کمک میکنه چی جواب بدین.
🔴
یا اینکه سر کلاس آنلاین، جواب معلم رو چی بدین؟ حتی می‌تونه تماساتونم ضبط کنه و وسط مکالمه کمک‌تون کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/141423" target="_blank">📅 09:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141422">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1mn-67bwFOyWRSX8mlvL5tEMNTlBiVc9RYGAstmgV3JDHShwSpjzkbcYZMhW2YEBM63xy2EWcEGKupcv_DGgjjn5Yt_jLRdiakhv8vBEKEDivxUHi8uWRizOLDM5L-i8yWQZiHNB1-4x-R6QfEFd_OVpZELrZnY6BSQcI5NzcDoT8nyxGYqsTLzktn35XJ5YKkXW8XJ5ejMU2DsXZyT1HlmU-H-TfGn0gE7pdiPpCWi1h1Cv46z3vfdD6Fr0yKfikvpcJ8iblk0OxyfWS2L8jBBIQbWvXO2Hz_lkaVaUTgahlOhcbS9LJlDu66ydBenl0NQNPOEz17wYZBuMtRVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلتفرم ایکس حساب یحیی سریع، سخنگوی حوثی‌ها، را مسدود کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/alonews/141422" target="_blank">📅 09:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141421">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
الجزیره: قیمت نفت ۱ دلار و ۲۹ سنت یا ۱.۵ درصد در هر بشکه کاهش یافت و به ۸۷.۶۹ دلار رسید
🔴
این کاهش پس از آن رخ داد که به دلیل جنگ علیه ایران، پیش‌بینی‌ها برای تقاضای جهانی نفت در سال ۲۰۲۶ کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/141421" target="_blank">📅 09:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141418">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/po3twxY7K4FB3yRCShkeYQ2kCzWdRwyMlgzGGB4jSE4apXLmUukP6cIwid3ClE47rN-1ROvAQkoGh2nQnzhT0P3JxuLCRg27WUrJ3YUOJzDKYeDP7QBiuwbD1MpvbmyPGxg2YPGVU6KeF7ZETKJ8qZHy5LRlYOC6WJzrpNr3avLDc8r58ZxxFBqv5Jvrgftvdg6q_YeKSmuB4f0eBy91yLnEdCqxWIOp5H6cQ9lSdrQFl7wKPFAziQJelv0iY9c-NvCQEXpDv5tV_dONabI8P_mfyzVgjkg929KRj-pxtGdKmGFV0Ih1lJMJnHq-nXkxB3SDHPSKnTR8CgCuU2PZAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ReZckfzGEbtGtRQpSv7mbPKhvAwUYt6mIYtDedKY7RlCJ0EjCE28xz4g410Hx0Z2CqS-fpAg9MI2TclJyKoXHKfCnw3Bn2pfIRDqDdJK2SRd15vF2T3W1vYCDjN23OKSIp38lY3GyXhsOhh1E3iQQN1OSeL43vZRWWz4KtObK9Uauw9JIZTRQRDXS_p4EN5jscTylemio63ewnUHGMMXACkTIXy6ZR5RcUF6SmXA-EyTViCCU8kxiLIZ7GWAYfssgzvNgRX5ZKNud8GZMQIdg0KgchQ3zDEdchmQqVKRfDKVWZ6e3s5D_jEwJr7JlAuaCaYDeiWfnKADTcF9aynXbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8342b1a3.mp4?token=f4i6ErK-7RLQmKFAH5wQVqahkcvDXVfehkgyQVWsSWXoHXJ_DRcubmU2R75Lo-xTqCIhuna7LrVzTuF_iUI1GKDgi6C35Oj2d8akIvWZFs1lYYK5CflOqQ4OYVCiE3Sn_g50gmjQw1PflQBA1gBE6W-8s-THSxkde9C__4F1irYLGYmRDLzpsi2_C36Rx_n9r7faWYyd0gMkM7FWsqY1_AX129Ik8xa0EAoiUwbXxwNXi7GrPq9RUXdn6z-2ILgQcyRC-5uBkwse3hvnu0TrubUWUFTXkfM1kIOBmI0uErOtJy0hPV1DpfbcjEOCggDxwVhFIh_OX38RyCKAYdZnZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8342b1a3.mp4?token=f4i6ErK-7RLQmKFAH5wQVqahkcvDXVfehkgyQVWsSWXoHXJ_DRcubmU2R75Lo-xTqCIhuna7LrVzTuF_iUI1GKDgi6C35Oj2d8akIvWZFs1lYYK5CflOqQ4OYVCiE3Sn_g50gmjQw1PflQBA1gBE6W-8s-THSxkde9C__4F1irYLGYmRDLzpsi2_C36Rx_n9r7faWYyd0gMkM7FWsqY1_AX129Ik8xa0EAoiUwbXxwNXi7GrPq9RUXdn6z-2ILgQcyRC-5uBkwse3hvnu0TrubUWUFTXkfM1kIOBmI0uErOtJy0hPV1DpfbcjEOCggDxwVhFIh_OX38RyCKAYdZnZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ی زیبای خورشید گرفتگی کاملی که امروز در اسپانیا و آلمان رخ داد :
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/141418" target="_blank">📅 02:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141417">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس:
دشمن قصد حمله زمینی از مسیرهای غرب کشور، خارک و قشم را داشت که با واکنش یگان‌های نظامی و نیروهای مردمی، این نقشه در نطفه خفه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/141417" target="_blank">📅 02:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141415">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UR01sAU1uoX3Jg1sL0Z5rn0RaOAjI_OMB6FrDDq5d0QeIKGZ4tt-mXwtQcbyQPG5wWHvDH_zymJN0-jPHG621ByT5k4wlb7ej2DvMVCQnx7GtBGy0k1OL9zf1dXa3gjfjguSfcg191lHbI3R3oiZWYYoFHUkjLWDdMtRI2r3izeYvRiq3cbikWepxwjgI04aQ_5bvXTOaMq4VXWrw8nQ0g7a4xbLl0hV7bsSBk4z2wnhL1SoOyUxU3pNkZP7nILFGjkj9xsnaioTCeZnt6bVRPOBNyCynDNPhZprA49J6OagBBFWmJ3aKK_5QlHR5HqXScOh0B87xLdJj0yHLOyW8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfh5VeCVL32ozQYOvVSxTknEgcfgu4B-BtKn7V9Z1jCn43k9jw9ydhRIP_Ymc2AD_zrk-iyMS_x84t4qYmOB4nA28YFyrSNxYsNvEwwHoYBPOOMSS10QM781MGvLIndgYAm7Mnmctwts6tRorpLlmFEZaGmSLFyHF1IJEBIFYN9Bgau0fw9Xts2IKfXdNj8vuuILT7srL75DuZzCL7HzLkb6CRbWfbk0pEU34eCwyJmRP27sx8HPDXNhgGGf9OGX5mlpDgC6l64XJ56MfWW2ykRcXyr20Zv_sTUQgFbnrazOubkPr99Dk-xLQxhKHdriNJtTH1GpDlT-PfFn8i6Dhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ رفته تماشای بازی‌های پاتریوتس؛
بازیکنا هم دخترای نوجوان بودن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/141415" target="_blank">📅 02:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141414">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
دخترا حواستون باشه تنهایی شب بیرون نرید، تو این ویدیو ۴ تا حرومزاده تو اصفهان دور یه دختر رو گرفتن و دارن اذیتش میکنن.  @TitrDaily</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/141414" target="_blank">📅 01:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141413">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZmEeZbQQMqshFUNVUwDNfL6eYKRbrLDvCA2GPsnNHMLSMM61juzvks6yKjELTbhPUx2QNZOnw-U5hBg46uAz1a3vqxPliH9hTrV3nyZ3VBltOb5lqYl-ikKBPp0lUXaFUVbBASGBNBATpTjeGukvfCePxGDIEi4lX835x35tF3YZH827CgQVI2645GlGeR1hkX4KzM693Y3YsAby-gBVL7DaEt87qPWAtjaE-ZyaJ0AzycXtJBULlFtovzBV8bz024zPXbh2Adly9g5tQq7MNwwr2PdXmtwoWmz0MRtUbsWW59eQnGE9rOgK-JBdRwpxRn0hy75i8WDV4RuevJCn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری جدید از فرمانده نیروی دریایی سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/141413" target="_blank">📅 01:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141412">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJLzXMiFZ34a8r6RmIB9_u8eFIAKLmQGqzC78QFN7F7xB8WFs2XpdcAiW478xZBI1CuRn46FmaEMS3iXdWTDxOq3AEuO7kMmwYsEdYxjkLClGdLI5fnBv5aWEM2j4dh2ad6ov2hjq25RXrJ8A3Q1gp-o0YVJa7ylkcEwjOpn-dxobxjD7ZkvG8KNS6HmRghd3mjAmAqxmhAJlaGfEX48xUfxDTw1f257q2QpOMAkGomFi2W58uA4RGOmlVD57eOxTTQhQ7RpF1yS9z1L_w11zs97zSUOQT7MN4CIF-ORSyFliicaie7rEIV4aHk9Jn9agmXAzQWRndNN9o0YouoePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری هندی شبکه خبر: باید تا هروقت که نیازه بجنگیم اگر چندسال هم بشه مشکلی نیست و مردم راضین
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/141412" target="_blank">📅 01:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141411">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2686734c.mp4?token=mlOoROdQkhsiKTPS1Lbm5Cw0UEesjUuw-KGvtdX--aZoOgRrpZItJ5KQZbMrGDOEaZLXKfURLpl9T5Lz3bb4evSoyXV1pddFrDNRuDL1n09ih3I9gm4-mNllSXT6JDnd5C5sV06heO4kTOuVE4or5ry5KSh-1UBRUr1K2nGbXWb5xbvUhdg3wj4qYLqk-Xe5EBQo1_hWHNhzL9duPs2Vxh1jiV6RQ4QJJwQdhNJga0_8aQ5l-mF9xQ_GJtVfQYHnfnWgtM-zqoEmYhLW0HVS8H7EyV3go56AtgYbIAXLbrpxU7OOg6aoljXr9amwfkGdTf51ap7pvHPYGTnj3SC5lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2686734c.mp4?token=mlOoROdQkhsiKTPS1Lbm5Cw0UEesjUuw-KGvtdX--aZoOgRrpZItJ5KQZbMrGDOEaZLXKfURLpl9T5Lz3bb4evSoyXV1pddFrDNRuDL1n09ih3I9gm4-mNllSXT6JDnd5C5sV06heO4kTOuVE4or5ry5KSh-1UBRUr1K2nGbXWb5xbvUhdg3wj4qYLqk-Xe5EBQo1_hWHNhzL9duPs2Vxh1jiV6RQ4QJJwQdhNJga0_8aQ5l-mF9xQ_GJtVfQYHnfnWgtM-zqoEmYhLW0HVS8H7EyV3go56AtgYbIAXLbrpxU7OOg6aoljXr9amwfkGdTf51ap7pvHPYGTnj3SC5lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یالانچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/141411" target="_blank">📅 01:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141410">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
علی قلهکی: طرح دولت برای افزایش نرخ بنزین تا چند روز گذشته متفاوت از طرح اعلامی امروز و مبلغ ۸۷.۲۰۰ تومانی در کرمان است که البته همین هم متوقف شد و دولت اصطلاحا عقب نشست/امیدوارم از «آبانِ ۹۸» درسِ عبرت گرفته باشیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/141410" target="_blank">📅 01:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141409">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/141409" target="_blank">📅 01:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141408">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed091c1703.mp4?token=QC18nd2IcAt4lovBrKDa1H7ESbsDVulU8bUbMNZdPti8hRTdGYg9Mqury0yr45tCK688L9Gu-lYQUEwff1957K6K9rqNnEyXZ0qRIw3qANuE28-WPSPsi-ZaD0SKgdE0wI1-r0uLFVPKqo-NwJM67zsg5cB8Ns3iQmew1yiIWc6Dz7uQGrq8_T0iwJANOAD2zaHKpN3SGH7ryg692VYJP-6h2Ld7sLXpr52T-aYJhnASx4qSIAkg6L05MvDm-n8cFLQhOeagCt93fADcIjBBer_D9EsUd3n43v5gOwPT9lcHUCriPqKq-fsR5R1NgfHyMsfNdbRg5FusdUjfD9XI7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed091c1703.mp4?token=QC18nd2IcAt4lovBrKDa1H7ESbsDVulU8bUbMNZdPti8hRTdGYg9Mqury0yr45tCK688L9Gu-lYQUEwff1957K6K9rqNnEyXZ0qRIw3qANuE28-WPSPsi-ZaD0SKgdE0wI1-r0uLFVPKqo-NwJM67zsg5cB8Ns3iQmew1yiIWc6Dz7uQGrq8_T0iwJANOAD2zaHKpN3SGH7ryg692VYJP-6h2Ld7sLXpr52T-aYJhnASx4qSIAkg6L05MvDm-n8cFLQhOeagCt93fADcIjBBer_D9EsUd3n43v5gOwPT9lcHUCriPqKq-fsR5R1NgfHyMsfNdbRg5FusdUjfD9XI7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دکتر موسی غنی نژاد:
«یک ایدئولوژی التقاطی مارکسیستی و اسلامی، در دهه ۴۰ شروع شد، در دهه ۵۰ تکمیل شد و در ۵۷ به پیروزی رسید؛ که "پیشرفت مادی" را مذموم و غربزدگی می‌دانست و ضد توسعه بودند. حال همان انقلابیون اکنون در راس حکومت هستند و مانع گفتار و گفتمان توسعه و مانع پیشرفت کشور هستند...»
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/141408" target="_blank">📅 01:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141407">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/141407" target="_blank">📅 01:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141406">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
دادستان اردبیل:
بی حجابی مشکل اصلی کشور هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/141406" target="_blank">📅 01:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141405">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b5aac12.mp4?token=bedjN70u9K2Xj-zRydS8jd4_FiMT6VFI3BtjVceSexJQSQEN0FM_iqWHpdFTGv_5Wn17xuPOKdfpS42uWTQCRO3gdWoIvGoMs3GV0Z6GKT4UHs7DJB0spKWhaMdT-yXqI8rrA51NYuDv5HoKVLFOM9enpV8uaqcPKxx2eHmj2brSqpdt6OmyJvJryuLAsyceKukGjqrMDhUMcYJYzg-sM-oQA8Q87Q-UPGhLbLgtKulc7VrwaCF_zOKI75CluTnEL1eLND6KlnRx2hJRseUR9-BHmoOgOe-7vmgggtVqnfyCCbXkKqD6c1Rw7ee1A37a3jei59DBJd9Mqps_XUG09g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b5aac12.mp4?token=bedjN70u9K2Xj-zRydS8jd4_FiMT6VFI3BtjVceSexJQSQEN0FM_iqWHpdFTGv_5Wn17xuPOKdfpS42uWTQCRO3gdWoIvGoMs3GV0Z6GKT4UHs7DJB0spKWhaMdT-yXqI8rrA51NYuDv5HoKVLFOM9enpV8uaqcPKxx2eHmj2brSqpdt6OmyJvJryuLAsyceKukGjqrMDhUMcYJYzg-sM-oQA8Q87Q-UPGhLbLgtKulc7VrwaCF_zOKI75CluTnEL1eLND6KlnRx2hJRseUR9-BHmoOgOe-7vmgggtVqnfyCCbXkKqD6c1Rw7ee1A37a3jei59DBJd9Mqps_XUG09g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
یک نفر بخاطر لایک کردن پست پهلوی و کامنت گذاشتن بازداشت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/141405" target="_blank">📅 00:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141404">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
فارس: عرضه بنزین با نرخ آزاد پالایشگاهی توی کرمان فعلاً متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/141404" target="_blank">📅 00:49 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141403">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
فارس: عرضه بنزین با نرخ آزاد پالایشگاهی توی کرمان فعلاً متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/141403" target="_blank">📅 00:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141402">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: آمریکا کنترل کامل هرمز رو در اختیار داره - فکر می‌کنم همین کنترل رو حفظ کنیم! محاصره دریایی ما رو همه «دیوار فولادی» صدا می‌زنن و ایران هیچ کاری از دستش برنمیاد  - ایران دیگه نیروی دریایی و نیروی هوایی نداره، نیروهاش حقوق نمی‌گیرن  - سپاه هم نابود…</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/141402" target="_blank">📅 00:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141401">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
حمزه صفوی: اشتباه کردیم که مسئله‌مان حفظ بشار اسد شد!
🔴
تهدیدهای بی‌اثر انجام دادیم و باعث شد باقی تهدیدهایمان پوچ به نظر برسد
🔴
در ماجرای تسخیر سفارت آمریکا؛ ایران قواعد بین‌المللی را شکسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/141401" target="_blank">📅 00:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141400">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
تعدادی از صرافی‌ها مدتی است که از تسویه برداشت‌های مشتریانشان امتناع می‌کنند، در حالی که دارایی‌هایشان بلوکه نیست.
🔴
زنگ خطر کلاهبرداری بزرگ از سوی مردمی که دارایی‌هایشان را در صرافی‌های ایرانی نگهداری می‌کنند، نزدیک است.
🤔
این موضوع را جدی بگیرید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/141400" target="_blank">📅 00:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141399">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b87629e01e.mp4?token=TYQbvf1EuuixVVbMwrhFgXI9eetWEZZjuwrVHjuNeQ2PNi0wgHUISCGoCLSEbcvvJaEv4z4nFBYivdnwrs71Blcdp2dJ7kA22FNA9GGn5EJbHtddbTAaA-sbV2-neRjiIgXufNzgTchCDugFQUhd6TbDw7DZB2tkKV3v76Rf_Xs-Mj5wdot515mWy5_sAIbfr_6nr1bGMlxRRmKE76lI5rlreB5nBCKLUCpnNnOvH2UPNi2tz-9jt51i16-1Op2NR_OMwnGvk5gJVdPTRdjeVT7fiREz51po69awL97Et75BqdJJ0tUCrT_KUyDwLktQJAktmrYjvpagqCS87ZdHTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b87629e01e.mp4?token=TYQbvf1EuuixVVbMwrhFgXI9eetWEZZjuwrVHjuNeQ2PNi0wgHUISCGoCLSEbcvvJaEv4z4nFBYivdnwrs71Blcdp2dJ7kA22FNA9GGn5EJbHtddbTAaA-sbV2-neRjiIgXufNzgTchCDugFQUhd6TbDw7DZB2tkKV3v76Rf_Xs-Mj5wdot515mWy5_sAIbfr_6nr1bGMlxRRmKE76lI5rlreB5nBCKLUCpnNnOvH2UPNi2tz-9jt51i16-1Op2NR_OMwnGvk5gJVdPTRdjeVT7fiREz51po69awL97Et75BqdJJ0tUCrT_KUyDwLktQJAktmrYjvpagqCS87ZdHTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاری که حکومت با مردم میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/141399" target="_blank">📅 00:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141397">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
از عجایب دنیا اینه که تو کشوری که از وفور نفت، سواحلش نفتی شده، صف بنزین تشکیل شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/141397" target="_blank">📅 00:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141396">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
معاون امور استانداری کرمان گفت از بامداد روز پنجشنب نرخ بنزین بدون یارانه ۸۷۲۰۰ تومان به ازای هر لیتر در کرمان خواهد بود
🔴
پ.ن: بزودی هم تو کل کشور لیتری ۸۷هزار
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/141396" target="_blank">📅 00:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141395">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POZ54Rg_qTzMryxvUHfWQiTP-GYn0LTlQOF6zkJNm89VJ-QJudZT_3eqQWGZWSmc5tpDMBihVuyu9TJw5H49l0AtxZ-h3nPV8GNFGoHQfxhWRpzhpT5v3tBIkxGPgsjE8BqdF0rz2DWcR3eQF4JLq5tNrfQPBRxiqHWs7xIEz5zYGXxZ_YR03Rs4Uh7Bm7rPiGXmoWhrf5CubMVn7rz-YpUMCuFGNQO28cTZSkGZLyR2BgjqhULbX8DiJ8vWiMHpVqQUQm2IfS_sKH29yy0BDoOplX66EJs7D7jnj3jQWCtcBRXQ8yyje-NosohpAsAcxOJ6HIZS27nTdM-MRUUA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: اسرائیل و لبنان توافق کردند
/
چهار کشور ناظر بر خلع سلاح حزب‌الله می‌شوند
🔴
رویترز گزارش داده اسرائیل و لبنان بر سر فهرستی از کشورها برای نظارت بر روند خلع سلاح حزب‌الله به توافق رسیده‌اند؛ انگلیس، ایتالیا، سوئیس و اندونزی در این فهرست قرار دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/141395" target="_blank">📅 00:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141394">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
جنبش النجبا، از گروه های شبه نظامیان حشدالشعبی، از تحویل سلاح های خود به دولت عراق خودداری کرد و از این دستور سرپیچی کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/141394" target="_blank">📅 23:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141393">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ میگفت تورم ایران ۳۰۰درصده انگار راسته
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/141393" target="_blank">📅 23:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141392">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
تنگه هرمز تنگه مردم ایران رو گشاد کرد
🔴
تنها کسی که از ناامنی این تنگه آسیب دید مردم ایرانن
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/141392" target="_blank">📅 23:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141391">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8e_iuCDPsltuTKLP0NwCUKvuG5mRjxMlzP0ptT7u46s9Z_0gt8pEXVYataR4M8J3t8rwOWDBQMDawr1MEtVVDNQkmzOQX3_75n-1iiQLLIGqhlLRmYvfs8mzCGv18eE5rsxjx8ny_q7HMqaC5kc9eo9VjnfzxHZduAlrMGJvjTK8gMjfV171uyHtGms6ggSsNCRdDNnEIssclXyt-xbGYa7djCpB-jd-M58-ZCED19L-9WiISJjMxpeaj-Yd4JIwzBX1kE4NQbzGRQ0t9pdZiseHZiONvIue6P6q6gZcbqU7P0B-J0asWQkz3ZZY3F-2oxKyFzzZ_Q0vgs4Axt-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
این وسط گروه هکری عدل علی تصاویر برهنه و منشوری مسیح علینژاد رو منتشر کرد
😐
😐
😐
😐
😐
🚨
مشاهده فوری عکس‌ها</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/141391" target="_blank">📅 23:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141390">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سلیمی، عضو مجلس: ارزش تنگه هرمز بیشتر از بمب هسته‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/141390" target="_blank">📅 23:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141389">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbQ8HdbbHvCG5rDgPYjOx07T7z8dwSJWlhMxznW8M_Libi3Cz8icwwWxlFWgx2gp8mnTr1G92fLWV_KLkpMUeWCU2dRxsxdBa-gro_QOlCTKpQpnmdDW70KKNMLoPtNSCu6iTrMIRkEWZUAiiZa8AFxljhwYmsuomQrXnQ1WNuRc4Sk1YHSk5cqnJC8XhxGO8Nr3rOgyJc57TaaLXJw5eBU9JPWEam5cqZEpw1XRA4ILzDaK-JZPj3YCzwo7F3mFebCGmlCGRDE-Frl9FWgG62pzs_Fhh0PISYkvI6102lEr5fDPEsWCSKhPJE9PFP4KPzlvaw8Ss1OxPqHqLK6yKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد سامتینگ
(
قالیباف) فروردین ماه خطاب به مردم آمریکا :
دلتان برای قیمت فعلی بنزین تنگ می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/141389" target="_blank">📅 23:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141388">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97c70c4eb8.mp4?token=OutyBfpOaHNrYdutROGoYbDHXhGp0wZ1K2FRpz18xvL9bpkfGu9uLXgM1ob3BxVzVHs3hcm1YGQrrxBMrTF72nmqXooP3WYHgUscF-ytzDrfBiVCm31nA-GUhpV2evR_MITWGoS1r68oiON7vNF1bNYSmNQxDMzORUdeqaoZq-Eq79sh6DWIWXnhVuepquAFTnvEYYPWh3DEWN7mjvTop9O8fhDIGfA-hdg7TdlyI-xyAj0A-raY00XkzRR5K8hwMFj0IA9GduDo2MLxSbA7IGKbD999bIucoed7mEJ7xUGVb6eBhkyvIcdC4hVsp2USYeZ7L93zLGUFzTpggzRvfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97c70c4eb8.mp4?token=OutyBfpOaHNrYdutROGoYbDHXhGp0wZ1K2FRpz18xvL9bpkfGu9uLXgM1ob3BxVzVHs3hcm1YGQrrxBMrTF72nmqXooP3WYHgUscF-ytzDrfBiVCm31nA-GUhpV2evR_MITWGoS1r68oiON7vNF1bNYSmNQxDMzORUdeqaoZq-Eq79sh6DWIWXnhVuepquAFTnvEYYPWh3DEWN7mjvTop9O8fhDIGfA-hdg7TdlyI-xyAj0A-raY00XkzRR5K8hwMFj0IA9GduDo2MLxSbA7IGKbD999bIucoed7mEJ7xUGVb6eBhkyvIcdC4hVsp2USYeZ7L93zLGUFzTpggzRvfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف پارسال: بنزین ۶۰ هزار تومانی برای سال آینده صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/141388" target="_blank">📅 23:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141387">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhRxCxoJ4rmhnjLUxcKjm4C8-BBjwWUBHYqdLRYS3b9utiWqo5KNo1v6tIPBCLD6pL9rqvhh1aMq-5-W-LZ3Fq50XUuJTiSgAGhNZ9bJp3pcQatiUsOrb66UFHjvDOPOrH3Z_7J7KyA0W1wFErrbnnnQufZsDGiRr2AGSGt_ELYTi8QFGXSGLGM0tKK5_tJG8Lo5Z-q8ybqjg7IjuU_P6GTZq0mkHd8STbmOY9M8L-59LESvOhrR8mlbDR8ZRe1-7ErlMaBDIksKyGDrj5LfOdfUtciCO-OvEA_62j6sWGu89ahvf8W9gMiuRXrR2np_7wOt2BZy4VOurZ-fzwOCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ اعلام کرد که کارولین لیویت، سخنگوی کاخ سفید، در پایان ماه آگوست از سمت خود استعفا خواهد داد تا وقت بیشتری را با فرزندان و خانواده‌اش بگذراند.
🔴
ترامپ گفت که لیویت همچنان به عنوان یکی از مشاوران برجسته و یک چهره تأثیرگذار در حزب جمهوری‌خواه، در فعالیت‌های انتخاباتی این حزب برای انتخابات میان‌دوره‌ای مشارکت خواهد داشت.
🔴
او از لیویت به عنوان یکی از اعضای کلیدی تیم خود از سال ۲۰۱۸ تقدیر کرد و او را یکی از بهترین سخنگوهای تاریخ کاخ سفید توصیف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/141387" target="_blank">📅 23:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141386">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc94e5e813.mp4?token=BewbIzECXzVzX8eLDzfO54Pfa8FNau_Y6NmufsSgL5eLiteoKYfYCoc5AWCPotKwNoKfjYrAYgZpNCceU3eIQtxFn4TFZ0MQdflUV5iauBXODtc5AmvsSXb4Zd3OJcAXN4SXjJ3MBZKl_80WKF_-EqJebx9pbRtBUuacJ2Ve-zprDlN6yrFELWYEMkFHjw2bro8jOHR43S0AkZpPp0t31C0XSrfCsTvks5H_3DKppFlzvpcmZAaFDiFl9v46ITRDmlSkEwLiYDFZLxiAv6dEMy4HGJGmtwVy6uCCDT1WYq0lOMieqmbBU3aR1Sk95m-eORJg7FZBEBq4Vlv_35IRyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc94e5e813.mp4?token=BewbIzECXzVzX8eLDzfO54Pfa8FNau_Y6NmufsSgL5eLiteoKYfYCoc5AWCPotKwNoKfjYrAYgZpNCceU3eIQtxFn4TFZ0MQdflUV5iauBXODtc5AmvsSXb4Zd3OJcAXN4SXjJ3MBZKl_80WKF_-EqJebx9pbRtBUuacJ2Ve-zprDlN6yrFELWYEMkFHjw2bro8jOHR43S0AkZpPp0t31C0XSrfCsTvks5H_3DKppFlzvpcmZAaFDiFl9v46ITRDmlSkEwLiYDFZLxiAv6dEMy4HGJGmtwVy6uCCDT1WYq0lOMieqmbBU3aR1Sk95m-eORJg7FZBEBq4Vlv_35IRyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنزین گرون شده ایرانیا چیکار میکنن؟
ایرانیا:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/141386" target="_blank">📅 23:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141385">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
تو آمریکا بنزین ۰.۵ سنت گرون میشه
صدا و سیما: فروپاشی آمریکا نزدیکه
👈
تو ایران بنزین ۱۰برابر میشه
🔴
صدا و سیما: به قله نزدیکیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/141385" target="_blank">📅 23:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141384">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بانک‌های پرخطر VS بانک های کم‌خطر   مطالبی که اینجا می‌نویسم رایگانه؛ اگه فکر می‌کنید به درد کسی می‌خوره، برای دوستاتون هم بفرستید تا استفاده کنن.
✍🏻
آموزش خرید انس جهانی طلا بدون واسطه از صرافی خارجی
✔️
@mahaneconomy</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/141384" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141383">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f753625931.mp4?token=HBu_-CygnD0q0PLolCE72EP_-974t-dicZMHag-MK6hM-EJCV0zFAoCWXTUSP80g8zsMzrTsZmIuR5RUzhEUKR8vFEQhEV-yUPYcMw8PY_eXllD1nHzwq9DUaM0-Yx-ojS1_cqRHV-D6YdZwtjd0YJUbxzsNQVa7IA43btTVZjGAX0SprYbR8sX5hNXP_Vdp5ZixVU-ndghASJWBIJ2cZQFzGflisjyGigJbgq_Z5HkyUKs_lI_QTFU1g6QDoT6UpK47c-7w3WbOYKTNdiVBgLyBIEx5r8raDpz36QOqf1hKOWAfqqSaJLhMH3qkvjKDBL4uQypMqI0C8mLrCxa2zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f753625931.mp4?token=HBu_-CygnD0q0PLolCE72EP_-974t-dicZMHag-MK6hM-EJCV0zFAoCWXTUSP80g8zsMzrTsZmIuR5RUzhEUKR8vFEQhEV-yUPYcMw8PY_eXllD1nHzwq9DUaM0-Yx-ojS1_cqRHV-D6YdZwtjd0YJUbxzsNQVa7IA43btTVZjGAX0SprYbR8sX5hNXP_Vdp5ZixVU-ndghASJWBIJ2cZQFzGflisjyGigJbgq_Z5HkyUKs_lI_QTFU1g6QDoT6UpK47c-7w3WbOYKTNdiVBgLyBIEx5r8raDpz36QOqf1hKOWAfqqSaJLhMH3qkvjKDBL4uQypMqI0C8mLrCxa2zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خانعلی‌زاده شیشه‌ای: افزایش قیمت بنزین در آمریکا ممکن است آمریکایی‌ها را بی‌خانمان کند و آن‌ها را مجبور کند خودروهای خود را بفروشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/141383" target="_blank">📅 22:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141382">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تو آمریکا بنزین ۵سِنت گرون میشه، قالیباف و ... توئیت میزنن که لذت ببرید و اولشه و ما بردیم. اینجا یهو ۱۰برابر میشه هیچی به هیچی</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/141382" target="_blank">📅 22:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141381">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxAvb2Kwa9J-wTSoPKkhAW8oV4jVgi6AF3Adwav2OwZ2_u8XykfphUget_G7s0m_SbYOwmWehWf4KKfyLLWn5VBQVWZ4yIR92ljJJcBw2Zod8GZ1VwW-OnA4rWfETV_57hxUBEMrONZPvPy3beBmhOQxCuwWj0KbtlpU-RWob_yOeThNW9j29uhNxRxXmD-xtuuQixHSdkQeNX4dBlipmvWM6FDVTItZfcJeXdEz1Hqdsq9nWTda6vP-kLIJ0W_aSheSAaq63IlDMDyRyw7td3A7EEseJeCvj88LBzCZ48Bre7mRqeIB5hND8y0Ys0HR5ZhLBthZXqXWAme7AJdLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام اعلام کرد که نیروهای آمریکایی مسیر حرکت ۵۹ کشتی تجاری را تغییر داده‌اند، ۳ فروند از آن‌ها را غیرفعال کرده‌اند و ۲ فروند دیگر را بازرسی کرده‌اند تا از رعایت مقررات مربوط به تحریم‌های اعمال‌شده بر بنادر ایران اطمینان حاصل کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/141381" target="_blank">📅 22:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141379">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
شما توی ظاهر فقط می‌خونی بنزین گرون شد، اما چه اتفاقی میفته؟ هزینه اسنپ و تاکسی چند برابر میشه. هزینه باربری کالا که از تولید کننده به مغازه میرسه افزایش پیدا میکنه و در نهایت جنس هم گرون میشه. افزایش هزینه حمل بار، وانت و مصالح ساختمونی. افزایش هزینه ارسال…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/141379" target="_blank">📅 22:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141378">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0947d4c92.mp4?token=f5dfHFy84uJLYtM3qwrMK6rY2L_hbGRVTyayiDumK3Y0X9VvmfG1dYV5fn4BaANuHxZvr7ekZXV-yk0LnYsoyNkaBya2jF4Pa0NaypLD1lGtvZwDTXSilWNFqmAdb7Z00oF6yd1vw-orDvU3TJe_wYk0PT_-mUl00hb4lGQAFTeVbuhull4aVNK3rSoxRCLy57uI4cdn6lg7WOXxvfTjiuUk1HToQJB6mN_v4JRLm5aQ-9gAMnWprvJAt0s-kyJd_xw15tJbqFpa7BprQA5nHICRpmbsdw38uE-Lpy-qJQBJ0Rxa1LSgz1LT2Tw9W5SEuZfQJulP5GqtMi-h028aAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0947d4c92.mp4?token=f5dfHFy84uJLYtM3qwrMK6rY2L_hbGRVTyayiDumK3Y0X9VvmfG1dYV5fn4BaANuHxZvr7ekZXV-yk0LnYsoyNkaBya2jF4Pa0NaypLD1lGtvZwDTXSilWNFqmAdb7Z00oF6yd1vw-orDvU3TJe_wYk0PT_-mUl00hb4lGQAFTeVbuhull4aVNK3rSoxRCLy57uI4cdn6lg7WOXxvfTjiuUk1HToQJB6mN_v4JRLm5aQ-9gAMnWprvJAt0s-kyJd_xw15tJbqFpa7BprQA5nHICRpmbsdw38uE-Lpy-qJQBJ0Rxa1LSgz1LT2Tw9W5SEuZfQJulP5GqtMi-h028aAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شما توی ظاهر فقط می‌خونی بنزین گرون شد، اما چه اتفاقی میفته؟ هزینه اسنپ و تاکسی چند برابر میشه. هزینه باربری کالا که از تولید کننده به مغازه میرسه افزایش پیدا میکنه و در نهایت جنس هم گرون میشه. افزایش هزینه حمل بار، وانت و مصالح ساختمونی. افزایش هزینه ارسال…</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/141378" target="_blank">📅 22:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141377">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
شما توی ظاهر فقط می‌خونی بنزین گرون شد، اما چه اتفاقی میفته؟
هزینه اسنپ و تاکسی چند برابر میشه.
هزینه باربری کالا که از تولید کننده به مغازه میرسه افزایش پیدا میکنه و در نهایت جنس هم گرون میشه.
افزایش هزینه حمل بار، وانت و مصالح ساختمونی.
افزایش هزینه ارسال بسته و پیک.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/141377" target="_blank">📅 22:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141376">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DabZRWvOmANYgXlS67y9PaFk03HNMonC5c0ou2NJnFYBFA69iutJXWcrK7ihUUgTi0mdj4ISSs2hkicjnnV6O1UHkhSQXMnnT-uedO02E_z4d_GFYSXFNa9iIrOSSKzH2iuRBLxyeItYomyyLwJemP7_DmBOLu10tHQwQnccKbC_BQbuwYWk_wNFcVgfTTgFFqh7lLxMxE9fP01U8QK1_Syk-wfxyUKdhpqyreJJwPRGy6bgTnPlg4icOQfZqWloZmN-Xl8M1nHS-xXaYeOtyzfvyroGLvYWsBN6u3batV-wmoRm8Ll3xx5jHjcFWbPvnzogOrrHUiRTjlF31_9U6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بریتانیا، ایتالیا، سوئیس و اندونزی در حال بررسی برای اعزام یک مأموریت خارجی به منظور تأیید خلع سلاح حزب‌الله در جنوب لبنان هستند.
🔴
این طرح ممکن است شامل بازرسی از روستاها و خانه‌های خصوصی باشد، اما هنوز مأموریت مأموریت و آزادی عمل آن حل و فصل نشده است.
🔴
منبع: رویترز
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/141376" target="_blank">📅 22:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141375">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_pZ3HUWYN68-KOAp-E5wc4Zp36-v66kXqi0ylSzc_L4nOpvFO7Lxo4ai5EthjI2vuNy0JLK71weK1yPDZ56Jxvfhc3hzO0xNWxRs4h_RVxI1fKB7uZ38nE6_haT1dNA0KjDEq491ArC5cl1b7YH9e8Uqj2Bbjaohc8c5yjLbfaEga4w9zdZ4gCzFSv2GYXEi96Be_ruF2O0YV39YCHNl1BqkdTh7jN77fFrWNgxOVCXoukGCip7q9a0xWv3-g5FCHoFfh4w5A90jcYCFaBSet64Rj2Rgu5Y5Fdy2xOpSFcoYgskGeobtzEwQ2IraN45XOeFSqWj8R-8j2CFnbC5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت آبراه خلیج‌فارس: ادعاها و توییت‌های پیاپی مسئولان آمریکایی درباره رفع انسداد تنگه هرمز، واقعیت را تغییر نمی‌دهد؛ تنگه هرمز همچنان مسدود است و تا پذیرش شروط ایران بازگشایی نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/141375" target="_blank">📅 22:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141374">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXaNpl4_X9m4X3NyQvAyKKJQwVei3eeooS5jibO11NeIFnMsS4jfYx1SpgzXCHzVX7TaJQeDg7s2elWOBeRm086HClUZYVhAinEFUOKZjitfl2Av_GnOX4vL-O5-4ktuOchVopjAmB7SEcVsceylUFF4BCrzgue5ZqxrsVvHvyYiLnnTW2C8XeG1zHkhrn1DehwPmLOnIsnQJrr2mg6uLMw2SsorLBXN9iZMdKuEeVusgLZpccmHiLZSzGV_uoXqKQgVP4jkHrmuNJnjUIYV5Y90brjQB2qC-qqsJELsUWmb_k_mAfzS6LrnC5A6JIJqjxgrM4C5jsfXbpyUtwU4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز مرموز هواپیمای دولتی امارات به ایران
🔴
برخی منابع خبری مدعی شده‌اند یک فروند بوئینگ ۷۳۷ تشریفاتی متعلق به ناوگان دولتی امارات، طی دو روز متوالی وارد ایران شده است.
🔴
براساس این گزارش‌ها، هواپیما ۱۱ اوت حدود یک ساعت در محدوده تهران توقف داشته و ۱۲ اوت نیز در فرودگاه پیام کرج فرود آمده و پس از حدود ۳۰ دقیقه ایران را ترک کرده است.
🔴
هنوز مقام‌های ایران یا امارات درباره هدف این پروازها و سرنشینان هواپیما توضیحی منتشر نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/141374" target="_blank">📅 22:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141373">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WibXexYHeP3eLAFtaisfubp4R9BBNWggt8T6YfSnJxIGtz53DVSAoGukOc_IADs4rDf6XXN3Tg1LGKUB89Bg5PAPP200bH9tI9RnH8UzCWq-aaZ46REZk7vpq-l-BJGXw0gXGgPWV1VcAJ-pK-s0Fydi78PEgGNVr6m7XGT2Lt-pyqLH5MBgiLicOcFDtGosOtB_EUWn5CFDij6wjrGJLqDpe84OdTvRGQzAPyYTLF_c6asnXCJk3jjj1vjCrz7ae7nGFA4mEbFMa5HMvWxV0e0leOPQJkKb1HBcKjtAnqfsNoVVtLI4mskkE6AehRjx5dvFE6FztOhxJR7lKBgCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بهنام صمدی خبرنگار : آقایون اگه قراره مردم بنزین رو به قیمت 87 هزار تومان و به بهای تمام شده بخرن، باید بتونن ماشین هم به قیمت جهانی بخرن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/141373" target="_blank">📅 22:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141372">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فووووری/شلیک موشک به تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/141372" target="_blank">📅 22:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141371">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TO3jJ73LOLik89M9Vcd7NkbV41JYl_YCLMxLpmw21ZMRacA5NnB1YEYZ_Ti0VZCUSjJxDDgQS6xL6b-eRtwXfWwVdxZMX56nOc01uq_4GhERiyhHGB3SXDZlnIIJ97zWvn7Zu6EyOb39NCWyzY7ysKxO8TKBCCRbmKHkq8nZ8ASvyTqWmourJ-QdvwA23dEpmfKvLc0ImPb3_PUNXnva4gY9AE3QmLJWo2SC-AXoeWp0sd9pkC0vv6v4Ywp4X_qMqJt0sAYMPBSqRxhul2pUn2NuYXnqz40n7lruEYBn77LleO3Iq_2ubGIzNw5dRBWVWHA_eyXprLYJQxZGHxdZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خورشید گرفتگی کامل در ایسلند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/141371" target="_blank">📅 22:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141370">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سردار نقدی: از پس حماس کوچولو هم برنیومدید، دیگه ایران که جای خود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/141370" target="_blank">📅 21:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141369">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
الجزیره: بحران تنگه هرمز قیمت آلومینیوم را شعله‌ور می‌سازد؛ قیمت‌ها به بالاترین سطح در ۷ هفته اخیر صعود کرده و ذخایر جهانی به پایین‌ترین سطح تاریخی رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/141369" target="_blank">📅 21:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141367">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
منبع ارشد ایرانی به المیادین: تنگه هرمز باز نشده است/ اخبار فیک ترامپ برای کنترل قیمت بازار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/141367" target="_blank">📅 21:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141366">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رویترز: دولت لبنان ممکن است از نیروهای خارجی برای نظارت بر روند خلع سلاح حزب‌الله دعوت کند.
🔴
لبنان و اسرائیل بر سر معرفی بریتانیا، ایتالیا، سوئیس و اندونزی به‌عنوان کشورهای احتمالی مشارکت‌کننده در سازوکار پیشنهادی برای راستی‌آزمایی خلع سلاح حزب‌الله توافق کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/141366" target="_blank">📅 21:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141365">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAloMedia | پخش زنده ماهواره و مسابقات ورزشی | اَلومِدیا</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BpU52udGS0PyhqBIbK6x60hFWdNtds9KqIEdy3clrJ-xxHUlOyKjKOrbltwbLKjUyNvcydoGlTpfNfq0gADE_LfcOA31HbQTDIJ1Tj4AWASASQiO32z1RJukwwgYZQUOVU_L5V0S9mjaOdzPgwnkt1W44hlbc3eBOE9r1Ogp-d5UCJSoqOA17wtwPfg1MDDJSLyOjp1MrmqJh86KiW3UrOlEtknrtJoAyUxnasXdeDVGW81IM8XtYvpiIrd-Fh1au-awJXRWYE4wFVE2BOC1vlChEb-BKKRERaru_mrJjW-DjvQbJBdecPrAywhLnSL6uBqkIesFFmrk_pPIXAfPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پخش زنده بازی‌های امشب
▶️
رایگان ، بدون سانسور ، کیفیت FHD
🟢
شروع پخش زنده
🎁
😍
۵۰۰،۰۰۰ تومن شـارژ رایـگـان، هــدیـه‌ به کـاربـران جـدیـد
⛓
همین حالا ثبت‌نام کن</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/141365" target="_blank">📅 21:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141364">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان:
اسلام‌آباد به دنبال بازگرداندن تهران و واشنگتن به میز مذاکره است
🔴
طاهر اندرابی، سخنگوی وزارت امور خارجه پاکستان تأکید کرد که کشورش به تلاش‌های خود برای بازگرداندن تهران و واشنگتن به میز مذاکره ادامه می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/141364" target="_blank">📅 21:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141362">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUvF1DnvmAuVG32-BeJTBn-Pz2WERfwq8uefWulnXe8Q-irXzTmTk_VW_Q-6LmCeR7lfqXmsPyTYLGpKLmoqrbdEkxWe9CDPL4TLgn8GjarRK2IvCz2MJmXp610Ijol2rM0dRyzh9jNF7MzhEmNSwWNdttUv3MzdHDlZbMWazRFP-w5ekhfEuglT_iHdd9BX1ESbJXMANoZJwi2ytnylL7BZVeM5AiiSpa2ed6vwRjb88t2QbPZpnwRT_0M19IdojZ-UJzGf5BrlNAP7B9EyNCAOYsihdcyPa5O_nh7Lf7S0J3hSpFRyA9dhA57hqMguHCJ7NsDvCeYr2xzhC5MlDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نرخ چهارم بنزین از راه رسید
‼️
🔴
نرخ اول: ۶۰ لیتر بنزین با نرخ ۱۵۰۰ تومان
🔴
نرخ دوم: ۵۰ لیتر با نرخ ۳۰۰۰ تومان
🔴
نرخ سوم: ۴۰ لیتر با نرخ ۵۰۰۰ تومان
🔴
نرخ چهارم: ۸۷,۲۰۰ تومان
🔴
گفتنی است این طرح هنوز به طور رسمی در کشور اجرا نشده و فعلا محدود به ۲۰۴ جایگاه سوخت در استان کرمان است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/141362" target="_blank">📅 21:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141361">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
اتحادیه اروپا و ۲۶ کشور دیگر با صدور بیانیه‌ای از ایران خواستند اقدامات معناداری برای تضمین رعایت حقوق بشر انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/141361" target="_blank">📅 21:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141359">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سفیر پاکستان در مسکو:  سفیر پاکستان در مسکو تاکید کرد اسلام‌آباد هیچ مخالفتی با پیوستن ایران و مصر به توافقنامه دفاعی مشترک با آنکارا و ریاض تحت عنوان توافق مکه ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/141359" target="_blank">📅 21:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141358">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6shTVWDaQV5wOY8s8snZ-8d6fDa-_aFZjkcFVJ4EQEnheHYh9D0MXUVQ2BWUwUFtrgeHH4WYrjk2OPHOEpscotU_w-GcWbWyb2FnW-QFZh5741bAr8xuJ1RdKuva072ndUHsPXZBGmZwdnYjxgFwPi1wI5b3hoDLQmuY2MUlNhfV7aRPob90M3H3wdNVncSPkCMtnntOYEEmqs9gH1nKlYUBKBgBklJQOaaQwk-SKBnEw3nRPIH3QqGnhoyY4b_e5K_VVsVga61JMy9NyVHEjtwohRrQZg5BMgzSJAIHZ86vtTjAXebYND0xnX1-q_73qK-gEyPm2rLHUo9I00aaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: 2 تا 3 نفر از خدمه ناو هواپیمابر آبراهام لینکن در اثر فشار روانی طولانی شدن مدت اعزام این ناوگروه به بیش از 8 ماه، اقدام به خودکشی با پرتاب خود به سمت دریا کرده اند که همگی آن ها توسط دیگر خدمه یا نجات یافته اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/141358" target="_blank">📅 20:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141357">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
به دلیل درگیری و نا امنی در تنگه هرمز ، میزان درآمد کانال پاناما سه برابر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/141357" target="_blank">📅 20:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141356">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iykp7bUXz9tvryYw5yNJuj_SSFPdqYvps76oJVCkEDWfJdH06YTIiwje6c6Bz3DVelObDmzhsZwGBi5JJSX2ttYFLvNPZuCYM_9P1dbCDkcix45keITNXTD6lAn_x6kMhJ23fA4qh5SKmxQuL-OeY-gK2VMqqodNJ6SPzfoiaTAkoApuQTg43okfUjBUjEJIOqdi2uR6iDYA1tPez2mAolZAedqokfl46S8FcPXvBHSYg9mo1-gpygYr-Bv2K36_UWT90K8e0hVbarArtIYmImcaca12kByulmu7uwqjaKa2E6E8Um5CPxgGf0_C-65lBQ3SMcdPNg5FA_gEN4ILQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین واکنش احسان خواجه امیری به درگذشت پدرش
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/141356" target="_blank">📅 20:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141355">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadc935aa1.mp4?token=s2aUueezw8aeeS_J4Q5xIH0PWClyDDP-YhcA96yL3BMSgGOwrgRa-w4_YJqZ7r7nNXUZkKl_p67vuq8pXk3UGdimCmtM6kE-C5Wu_LXZfZBtyVFrDvr3CWkg7DDGjl3xgQSIsiFU5fqQkTnRNv2EQuBfZVc8GLZArTUZADVmUimhjoRK5ouBZ3o79zkLXPwgvgSvG--l-EdkCymCoodzkeEgo9qJUWO5fCWvvwuf8_Hg5o8EZOHL_I97K0-eOWKOi2gIHGf5P4Hyid8hfI6ZKyWdkmKR0PaCUOgvAuI79rS3aBCS9y2PdOUtJF1mCn3j4xxqGmI2Moi0yBWM-F_MfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadc935aa1.mp4?token=s2aUueezw8aeeS_J4Q5xIH0PWClyDDP-YhcA96yL3BMSgGOwrgRa-w4_YJqZ7r7nNXUZkKl_p67vuq8pXk3UGdimCmtM6kE-C5Wu_LXZfZBtyVFrDvr3CWkg7DDGjl3xgQSIsiFU5fqQkTnRNv2EQuBfZVc8GLZArTUZADVmUimhjoRK5ouBZ3o79zkLXPwgvgSvG--l-EdkCymCoodzkeEgo9qJUWO5fCWvvwuf8_Hg5o8EZOHL_I97K0-eOWKOi2gIHGf5P4Hyid8hfI6ZKyWdkmKR0PaCUOgvAuI79rS3aBCS9y2PdOUtJF1mCn3j4xxqGmI2Moi0yBWM-F_MfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر ایالات متحده در اسرائیل، مایک هاکبی، در مورد  ایران: ترامپ نه تنها ثابت کرده که مایل به بمباران آن‌ها بوده، بلکه همچنین مایل به ورشکست کردن آن‌ها است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/141355" target="_blank">📅 20:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141354">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
بلومبرگ گزارش داده ایران با بازسازماندهی ساختار نظامی و امنیتی خود، به‌دنبال ایجاد نیرویی تهاجمی‌تر و آماده‌تر برای درگیری‌های طولانی‌مدت است. این تغییرات می‌تواند نشانه‌ای از آمادگی تهران برای مواجهه‌های نظامی آینده باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/141354" target="_blank">📅 20:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141353">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b1765ff5a.mp4?token=H32y7gf5cJdcYmJEX0V5R1jZhxvYUjkzUUyQj5EpXadeaJjxHsYDTk9BWrOq_MJDjyb233bXQRU-UUBd5lr9D9E9VnhNruzq41kC2fZqP9Z8yVcriIfOqM-yTkMO0Px6I1qoLGWiPJmJjmNpLq8qEQS1fUn2jN4VRxYhvlNkdNvrz9CjAnd2WQYSFx6XcUL5ZFm7r9sxMkyrZCZEJLBwCQwGwJfjH247znOPLi-gqVYZ09LabL6u0nHzxrBOgpIb15apQEiDsDl2XDj_JuC7rRJQ_MWRMh5e6zYC2AgtPSCTwa1OyJ9T-1SagqEpOPnVDFzzJS6Aawu0RE_9fZh-GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b1765ff5a.mp4?token=H32y7gf5cJdcYmJEX0V5R1jZhxvYUjkzUUyQj5EpXadeaJjxHsYDTk9BWrOq_MJDjyb233bXQRU-UUBd5lr9D9E9VnhNruzq41kC2fZqP9Z8yVcriIfOqM-yTkMO0Px6I1qoLGWiPJmJjmNpLq8qEQS1fUn2jN4VRxYhvlNkdNvrz9CjAnd2WQYSFx6XcUL5ZFm7r9sxMkyrZCZEJLBwCQwGwJfjH247znOPLi-gqVYZ09LabL6u0nHzxrBOgpIb15apQEiDsDl2XDj_JuC7rRJQ_MWRMh5e6zYC2AgtPSCTwa1OyJ9T-1SagqEpOPnVDFzzJS6Aawu0RE_9fZh-GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بوریس جانسون ادعاهای مبنی بر اینکه سفر او به کی‌یف در آوریل ۲۰۲۲ مذاکرات صلح اوکراین و روسیه را خراب کرده است را «کاملاً و بی‌شک دروغ محض» خواند.
🔴
او می‌گوید هیچ رهبر غربی نمی‌توانست مانع از جنگیدن اوکراینی‌ها شود.
🔴
و پیام او به زلنسکی ساده بود: اگر می‌خواهید بجنگید، ما همراه شما خواهیم بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/141353" target="_blank">📅 20:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141352">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از شرکت کپلر: نیمی از کشتی‌هایی که در ماه اوت از تنگه هرمز عبور کردند، مسیری را که ایران اداره می‌کند، انتخاب کردند.
🔴
از میان ۱۶۶ عملیات عبور، تنها دو کشتی مسیر تحت حمایت ایالات متحده را انتخاب کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/141352" target="_blank">📅 20:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141351">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
فارس: کنوانسیون خزر سهم ایران را از ۲۰% به ۱۱% و حتی کمتر کاهش می‌دهد!
🔴
همچنین امکان بهره‌برداری از میدان‌های نفتی مشترک مهمی را از بین می‌برد و دسترسی ایران به بازارهای شمالی را با مشکل مواجه می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/141351" target="_blank">📅 20:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141350">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/141350" target="_blank">📅 20:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141349">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvNxpApsoITvFiiuuDdpS8Rd0CWAncdWDXSMEDIv3MayvcPl1_FOS3zEVra6q0rbliiYQI9npTmhe-vnxKCqJGZRvZEC0PREHLoC6VvCHiVL9ecg4DB8_WJ4SaHGVucjAqK0C4k_5X3r8lV9hJYi6HM7fAsoR-GPA6Quk1bLYYPJkFbQdN6pjgwUNb5gPDGHIB_6uzx04PN8cZXcJhL2bJha58CmLFyXMTZchl_ihdThjO3PN2dzX19ReKuqRKUutUsEi5U4FF7tuzOAVuK-oSd6u3X5c8C_Uv7h3KZsdeZna83aXpkBW4mKRrBVY4YTIrNEcvYA0m7z7SQmwCoUug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/141349" target="_blank">📅 19:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141348">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZM1Lh2Q6s7svYJdR4_w1IK8sF63rvbnYe6jffOV8CqLsnZjSF0sW3SUPOkPHa1HgGe4CbjcDmNvF6OIly0_dlW4OKzU-FKrjUrNpvTV3spXpPdDCyOllFmxci03goFZE0GzLndUQ0_MKkiotCajtUF9bZHPpPWE1SUqA3UaA_Kl89agCUhuy4a4plvb2OJ56xjXogl5BSrwj92SIBHRo4mBppw2Z26j9iRC0Ajdumg8iP8EoPxmPtgSxeChQzqj7olJ0G14VO5wol3eI16hYmNlf2MpXUsF2mbX3SvlP3dh8nScgEjF5aSK4O8GwRyqGXY2xI-tqSleWQf7RrXEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی فالح الزیدی» نخست‌وزیر عراق و «براد کوپر» فرمانده سنتکام در دیداری رسمی، بر سر توافق کامل و نهایی جهت پایان دادن به مأموریت نظامی ائتلاف بین‌المللی در خاک عراق توافق کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/141348" target="_blank">📅 19:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141347">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سازمان محیط‌زیست عمان اعلام کرد لکه نفتی ناشی از نشت یک نفتکش به گل‌نشسته، به سواحل جنوب‌شرقی این کشور رسیده است.
🔴
این نهاد رسمی هشدار داد آلودگی نفتی پس از سرریز از نفتکش آسیب‌ دیده، به نوار ساحلی جنوب‌شرق عمان گسترش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/141347" target="_blank">📅 19:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141346">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مشاور ارشد قالیباف: آمریکا و اسرائیل برای یک حمله نظامی پیش از انتخابات سراسری در اسرائیل و انتخابات کنگره آمریکا در آبان ماه، آماده می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/141346" target="_blank">📅 19:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141345">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
العربیه: میانجی پاکستانی برای تمدید ۶۰ روزه آتش‌بس ایران و آمریکا در تلاش است و نسبت به آن ابراز خوشبینی کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/141345" target="_blank">📅 19:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141344">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
شرکت آلمانی TKMS: در پی جنگ علیه ایران، شاهد افزایش تقاضا از سوی کشور‌های خاورمیانه برای ساخت شناو‌رهای نظامی بوده‌ایم
🔴
یکی از حوزه‌هایی که این افزایش در آن به طور مشخص دیده می‌شود، فناوری‌های مقابله با مین‌های دریایی است
🔴
همه توافق داریم که روایت و برداشت امنیتی در منطقه تا حدی تغییر کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/141344" target="_blank">📅 18:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141343">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
فارن پالسی: پیمان مکه، نظم منطقه‌ای بدون ایران می‌سازد
🔴
نظم منطقه‌ای مورد نظر ایران، بدون حضور خودش در حال شکل‌گیری است‌‌. تهران مدت‌ها خواهان همکاری بیشتر میان کشورهای مسلمان بوده است. اما پیمان مکه چیزی نیست که مدنظرش بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/141343" target="_blank">📅 18:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141342">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ee4191cae.mp4?token=hYi1Nd3s0F7_lbAMUz_r8sbv6Pj7h4FgCeqyYIojVjI6uORDXyMIs91fj9p5z4yS3pWM0qDQZnfOCvf8tKehI0V4Q13ispS-KwIRwrr32fm7F7zGWhk3NTuhSSsrjA6AjWlkpptQ3wr7TbNKnNaL03eu9muLPiFFy2pJ_Am4HNyh63Ae9vuxQySTrDFz2-xIBZoXijgKheVWaXenycRLyl0em4mLZ9sxtvcbTL2FdvvD5X5fHYeR-KZRgtFQf6gEhVQZhAEm3HMaDy7GJ2YMTv0Dk3Zu0K6iOveHyL5MQHvxZY_s7E_ulhAtDDMIbcNbtHrMYfTwh1gZ2OyFcfz5dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ee4191cae.mp4?token=hYi1Nd3s0F7_lbAMUz_r8sbv6Pj7h4FgCeqyYIojVjI6uORDXyMIs91fj9p5z4yS3pWM0qDQZnfOCvf8tKehI0V4Q13ispS-KwIRwrr32fm7F7zGWhk3NTuhSSsrjA6AjWlkpptQ3wr7TbNKnNaL03eu9muLPiFFy2pJ_Am4HNyh63Ae9vuxQySTrDFz2-xIBZoXijgKheVWaXenycRLyl0em4mLZ9sxtvcbTL2FdvvD5X5fHYeR-KZRgtFQf6gEhVQZhAEm3HMaDy7GJ2YMTv0Dk3Zu0K6iOveHyL5MQHvxZY_s7E_ulhAtDDMIbcNbtHrMYfTwh1gZ2OyFcfz5dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فوران آب پس از شکستگی خط‌ انتقال آب به بجنورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/141342" target="_blank">📅 18:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141341">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
نخست وزیر عراق: تصمیم برای پایان ماموریت ائتلاف بین‌المللی در عراق در تاریخ ۳۰ سپتامبر، تاریخی قطعی و غیرقابل بازگشت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/141341" target="_blank">📅 18:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141340">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqqHhHUEvrZRgq6HLxMwDGpBUpCEUAXmIeZGWU8vSQ2gwd5ZFTGwKqIG_KYijFTMi8Q5D6a7mkMpUT2zxBUpkQPogyZsXMFvjHAWO6BcoVoGV_Kb4wywSEQEN1w_GfPgsgVfxUcv9yerRDc_zEXjUTbnM4VzXUPs8FuAJiChA7P9ULI8DWVU1QT_X_k8EVFK92PXY-H3wdw41EN_MB9XNoeaehUGvD3MNyEb03F0zr-vtLCQAGFojvKVelougM5xCZ7pYWsLPVO3z9uQNXV171AHvh9YSw3ND5sMokYeUR-YaifuAytMghXK_LF3oogVfCNLCVQ-Lqp--QPscnNYrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۳ اتفاق نجومی قرار است همزمان در آسمان رخ دهد: خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/141340" target="_blank">📅 18:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141339">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سی‌ان‌ان: وزارت خارجه آمریکا سفارت‌های منطقه را برای شرایط جنگی آماده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/141339" target="_blank">📅 18:22 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
