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
<img src="https://cdn4.telesco.pe/file/JGuNNZd3XKJENXf6Am7_WNDLrtd-V9UGuk1kps_QC4PJ7BUhSMWHOaW00dJyHCNKyl-ukkgHEbmAHDRvGDbE6vzG8iXv7kGo7cNhJSU6xuE6GaGjYvMpNdDr-s2D6B9ordli3JgATto_bbTxJ5OTmHcquRUDsCovcZrHNezH1mLFzLmhu0hjrcJzIyk1rJ8vtj5bSRp7PX6MoouPjAqBmUryd2bZ-yOrmIqaDkwa10T54c7gh5GtR2BFNraw0pdWAgHfEhP-uDFN76QnXhUEnJPsfdxJbVULsS-fX1POAQOO-G5w5XNdT7HsqmXO7qdfYsPOZoCEpnfIvsObz4fq7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 18:04:58</div>
<hr>

<div class="tg-post" id="msg-17465">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 491 · <a href="https://t.me/SBoxxx/17465" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17464">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/me4OA9SApeGgYRStKf4ntevr7MP57tGXlutev6bRChLcjPHfXFAh0liMD_mGvMQ1qdc2Sk1Daz29LiVyaF2ebQhC3geupnzEAGbmGoEdo1KKOWwGTyf7ZsMXEcYfXkmPUsYS94CBHU7Lni5EHzmUYMURxHmnBbwUa0Z_By9n-mGdkD3RHXAi0qEhI4OzC_Icq2VIFwQTvoJQOzcMKCQJyiUKaEWrzVx-bzxjT0E1iLy4_YVPOdazgwMCohkR_jBrgozrWXv7dKpHgSfIeuz5yL_UKuGl74ZxEeKLlfUy-7ij6wOId3idyg7RJj9g-wNLMXocqkNxywoO8PACvYh4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه جنگنده اروپایی (FCAS) در آستانه فروپاشی!  پروژه سیستم جنگ هوایی آینده (FCAS)، که با هدف ساخت جنگنده نسل ششم اروپا و با همکاری فرانسه، آلمان و اسپانیا راه‌اندازی شد، اکنون در آستانه فروپاشی قرار دارد. این پروژه، که در سال ۲۰۱۷ توسط امانوئل مکرون و آنگلا…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/17464" target="_blank">📅 15:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17463">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">13 و 14 تیر: وداع در مصلای امام خمینی.
15 تیر: مراسم تشییع در تهران.
16 تیر: مراسم تشییع در قم.
18 تیر: تشییع در مشهد و تدفین در حرم امام رضا.</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/17463" target="_blank">📅 15:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17462">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxuphKb3wXAnp28D3F51SR669ALocMb5Pvz-kuXF16n3jWW8rQ6AS9ePNSgDaZEezSWfBa0PRnz6fBWMBz5RTGr0chKt5wL0ZGsFBnZnfRzdonYvBje7-kXQmezlvJQTo_UheTHmGoGOtV5X-Q5hcP6ORCpgWsJ_fN1vXAhrZFVxkUzSZfzayHi82QhxW55bN8osOfZ_LTkt0JtpTPny5DNCepS4inG2w4V0SpRlMUOqhOq_BpeVYGiLJWx5XmWc94MN2mf9LTOT00T9ayycEIKRZG15zW1LgU_OpQnxQST3IMRMtMTknlVvF_OhjbHn4w_L_WgHD3J58B95MuFZcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در جنوب تنگه هرمز هدف قرار گرفته است.</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/17462" target="_blank">📅 14:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17461">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">صحبت های جاناتان پولارد — جاسوس معروف اسرائیلی که در آمریکا دستگیر و 30 سال زندانی شد — درباره جنگ بعدی اسرائیل با ترکیه و مصر و لزوم استفاده از سلاح های نامتعارف کشتار جمعی.</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/17461" target="_blank">📅 14:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17460">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc2b3576.mp4?token=jIYILmrQoQIlBv9oY-crJ4nnhWvP1ZJo4GGmJ2iz_pGDo9tXbqUrBSCvgEYBphWNbePSlzFfeuCyUARzdjuN9AJjoz5nDmw4qYBSg4GQqmLXljr73Ovh-0C7j228rHqx0Ia8uwID4JwWuk-sN1DUkS35KwbRtzMeubWEUHthf1XK_12NG_IsWiU-azAHBnsWMrBlKcfQ01a1bFphJGCncbBU5My6lIrwJLtO6X_oaaKla4n2IpbDuEIOcqbMVYR0maAiAVuAnwlB-CVjm_mJNVAdHnURffmdWWwheOzJcE6cngxuEl4WLvwH9Va4CdzsrDR-T0feCV5fKiQaKRQ9zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc2b3576.mp4?token=jIYILmrQoQIlBv9oY-crJ4nnhWvP1ZJo4GGmJ2iz_pGDo9tXbqUrBSCvgEYBphWNbePSlzFfeuCyUARzdjuN9AJjoz5nDmw4qYBSg4GQqmLXljr73Ovh-0C7j228rHqx0Ia8uwID4JwWuk-sN1DUkS35KwbRtzMeubWEUHthf1XK_12NG_IsWiU-azAHBnsWMrBlKcfQ01a1bFphJGCncbBU5My6lIrwJLtO6X_oaaKla4n2IpbDuEIOcqbMVYR0maAiAVuAnwlB-CVjm_mJNVAdHnURffmdWWwheOzJcE6cngxuEl4WLvwH9Va4CdzsrDR-T0feCV5fKiQaKRQ9zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/17460" target="_blank">📅 14:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17459">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SBoxxx/17459" target="_blank">📅 13:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17458">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">صلح دوست ترین ارتش دنیا را لبنان دارد.  به محض نزدیک شدن جنگ، مرزها را ترک می‌کند.</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SBoxxx/17458" target="_blank">📅 13:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17457">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2fwOcIW7HoJNlwfY1m9bsPdOdv2ea_NF87oHepjBjbdx2-Czjj-ZhtWr9LkUnlTL4wNZb0juUCQSEXQKLYDziFFQioM2yHgRrHNED4ok9gO31n7TdbvqMyA0GhLbpNAbVXPHzTd6-WlMf1dQgcXzbChOjjxmEDo5wEDzqRwRi62Tf1nb1pcL_Ge9ws6D_IorDG92Lp1cR8FXf10E6JnHhPL9TD6_FmAVkdJhvfEwCrHTWLDKwvDLGiDx81cnCArFhYtc2vjFr7bP2wCRo_IN5WQW-qfey9NACUmxBLW6AGi9ky1V2cf3J5EzSPEA9I4-1ybBC3aES0lDkiEU1CKog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/17457" target="_blank">📅 13:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17456">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خدمات الکترونیکی در چهار بانک بزرگ ایران — بانک ملی ایران، بانک تجارت، بانک صادرات ایران و بانک توسعه صادرات ایران — از صبح امروز مختل شده است و این اختلال بر بانکداری موبایلی، بانکداری آنلاین، خودپردازها، پرداخت‌های کارت و سایر خدمات بانکی تأثیر گذاشته است.
گزارش‌ها حاکی از آن است که این اختلال ممکن است نتیجه یک حمله سایبری باشد، اگرچه مقامات ایرانی هنوز علت را تأیید نکرده‌اند.
— خبرگزاری فارس</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/17456" target="_blank">📅 13:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17455">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">در هر مقاله اش ۸ سوال از خودش میپرسد آخرش هم نتیجه ای می‌گیرد که معلوم نیست اساسا چه ربطی به سوال های بی پاسخ ش دارد</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/17455" target="_blank">📅 12:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17454">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17454" target="_blank">📅 09:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17453">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">CNN
:
گزارش‌ها حاکی از آن است که ایران ممکن است زیرساخت‌های تونلی مرتبط با اورانیوم را تخریب کرده و به تله‌های انفجاری مجهز کرده باشد.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/17453" target="_blank">📅 09:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17452">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">— مقامات اسرائیلی به یدیوت آهرونوت گفتند:
«اگر حزب‌الله شهرهای شمالی را هدف قرار دهد، ما به ضاحیه بیرون ‌حمله خواهیم کرد و در آن نقطه، واکنش ایران را خواهیم دید.
اگر ایران در حالی که ضاحیه‌ را هدف قرار می‌دهیم به ما حمله کند، ما پاسخ خواهیم داد و اصل آتش بس در همه جبهه‌ها را نخواهیم پذیرفت».</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17452" target="_blank">📅 09:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17451">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اینفوگرافیک سنتکام از وضعیت تنگه هرمز:  تنگه هرمز برای عبور و مرور باز است  • مسیرهای امنی برای عبور کشتی‌های تجاری از تنگه هرمز ایجاد شده است.  • این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.  • صدها کشتی در دو ماه گذشته…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17451" target="_blank">📅 09:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17450">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETS-DS8MgQJlTNtq1UZDz7TW4T-G_YuttuFvkAIEr3A-M1Dv1sjHJ0q2t2L1DoQ9552e6m5prO87TWAp70cHpICQe7XKWVYk3Jhox0K7rIGS3ctZFJLqmGUBQpNL9VxpWkybmtPQWyyljgknZPGxovGDskWrSewy6xFTwbD3ahvjvyShvw3TI-O1LyQITNLrZqFy0wrxo-2RMVDdVnvkbIiTCFtU5Kn2CLZvefsDfPShmInoR_lbnNf1ikMzT7FNbNRIUhOr_qLZPcF1DaGFXuPUD-b9zrZf18pfyvG-lwn0pUIJUJmO8vS5rkfe8y34_-AzNEwm26yR7UTDPTZw_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی از دیشب تا کنون ۳ کشتی دیگر را منحرف کرده و از ورود به بنادر ایران منع کرده اند.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17450" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17449">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YndG4GrMGASIbankJaYdIqaZpDTHnRhXkiIg0jvNxnVft-Pb1OhZN5_PIL-HZBUJTM2pBZlvpYJ2hzGRDPtD8_57E476B2D9QT_HPon5E-sJI4vKtSwehJ81_8AETolgmgH7ZEW5QBthDuDTFXsB3hrn-IDV4BJ33j5AqDZ6WpoIPhRnDxGkTQ-vmpOoyhvLhqTpDr2IFwYC86hTLfCMVy_FtB-AJofT4jGEGHN0DiSGVY3m2xuc4hA9lZhmyY7Akj3KE1cYZ9EEZpuvN-tIP6fiR3tveHxTwyhXgNt77hFRid0oHJAsJcRBsXiBmLw7nwtCZuODBrDK8cCtKtrYHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای انفجار در تهران شنیده می شود</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17449" target="_blank">📅 03:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17448">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پس چه کسی پول ما را می دهد؟!</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17448" target="_blank">📅 01:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17447">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">امارات متحده عربی اعلام کرد هیچ دارایی مسدود شده ایران آزاد، منتقل یا از طریق این کشور جابه‌جا نشده است</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17447" target="_blank">📅 01:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17446">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17446" target="_blank">📅 00:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17445">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17445" target="_blank">📅 00:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17444">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPTM0YzpTfCuIB4R-WP4c0KZnsjCjRZAArI6sq4Y87s3xxvgRxOhQDDYOT9uuoJFeSei-NcRjrZjzqs47efZxRr0kwfNgJJfTRCpmj0gKSUZdrZgadqqQGQWHK7vCAClR9DQm88dn6UHjLUCgsS7pn9dWY-xJIAoQtlClFyo7efx1e19-dtQlal76tzIKgAw58QAALgZKEDZOo66rUIPDl0HrxMXNS2U15UCy2onqAwy5iram5HMMRH5MJvN9xwmbcG7fg3I9sZflgJoXHvalBamM1wczgKlDOYnqhvUc1bOQ9UlknUN4zSbAv5zzkArqWvlExJZk4jZs5ICm997gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با Secret باش خدایی کن!  با Secret نباش فقط برگرد!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17444" target="_blank">📅 23:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17443">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOX_wuMBJ8RsEWfAPB7AuYd2RcbbOaZ9i6G9MMmfo_RWIFku2h4Txw8W4HKmf6-vLb162DM98NYgmfsrAhtWvx3F5Wp8Lbqt77F4a6xGjEsuWnLjzCBfeOQPpls6uyl5gevCcKcOzOunlcxnDFhXK2GHEzeNh3HD0u84YwzNYUleCvM55MrBD7I2MwpRRtOs0TSr9mFMHtLFtoJ4TcEP-aT5hjT9gHkXUUy2I68wrbymijbQLDhPXeC_yx5FufXmirZ7QDWAQZKN3fLT4LtQc7S1fusoXWPFsIFfJuEJoQ8PeLFDtVGV3zQ6cjyJ6DwrszChIPJ9R97peRfBl90cdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17443" target="_blank">📅 23:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17442">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حسین الحاج حسن، نماینده پارلمان لبنان و عضو بلوک وفاداری به مقاومت وابسته به حزب‌الله:  «ما به وضوح از سوی ایران مطلع شدیم که لبنان در آتش‌بس گنجانده شده است. مقامات ایرانی به ما اطلاع داده‌اند که اسرائیل طبق توافق از خاک لبنان خارج خواهد شد.  ما هرگز بازگشت…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17442" target="_blank">📅 22:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17441">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وزیر‌دفاع اسراییل:   رئیس جمهور ایالات متحده در حال حاضر با توجه به منافع آمریکا، از جمله منافع مشترک با اسرائیل - برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای - در حال پیشبرد توافق با ایران است و ما از او انتظار داریم که این اصل و اصول اضافی را در حوزه…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17441" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17440">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سنتکام:  کشتی‌های جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان به گشت‌زنی در آب‌های منطقه‌ای ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند.   تا امروز، نیروهای آمریکایی ۱۳۶ کشتی را تغییر مسیر داده و ۹ کشتی را غیرفعال کرده‌اند تا از رعایت این ممنوعیت…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17440" target="_blank">📅 22:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17439">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfN33KvvRxU2VrqhxQAHZU1GUkwNy3ipgJr9axnzgOLkpfxtOBqQZxqIPgCVt9k1JaECgbQZGiMdIxz4spLHAa7exLV-lsL_chQPq3erCxotzt8O_N9Od65bkNv32h9d_xMR5tQQKsWLR_8Sos7aDS2QD7cFlzXHTfB6gZAdvM5RXOa9g5BMTf22H2dJyN18gFyY86BjAtxKS8O7UwAnhUBL_bh408d03JKUr_vPrJEuXfNGZcHDN7YuMU4tX9O__BVOBvKva28n9BintvHCz8v4SBZpzNSJHf5NgJJ47YJ-EhnlZ28gu_wq1Max6jI1d6qlKhSKoj9_hXnl1Zxg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
نیروهای آمریکایی همچنان به اجرای دقیق محاصره علیه ایران ادامه می‌دهند. سنتکام از ۱۳ آوریل تاکنون ۱۳۹ کشتی تجاری مطابق با این قانون را تغییر مسیر داده و ۹ کشتی متخلف را از کار انداخته است.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17439" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17438">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">— وزیر امور خارجه پاکستان، امشب برای ادامه تلاش‌ها برای میانجی‌گری بین ایالات متحده و ایران به ژنو، سوئیس سفر می‌کند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17438" target="_blank">📅 21:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17437">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مثل این است که بگوییم شما نزنید ولی اگر لازم شد ما خواهیم زد!</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17437" target="_blank">📅 21:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17436">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDoSRvrL6m-F7DEfBj1AakBJfb9oTMYmFT4S8cYPO_7vl-cf2c615oYhMQsVKZdArqdCoM5Bx-z_IEvjK1WvNEoG01VQf01cgmoeBNKC11yYSYAfV11zBnkV1wxV1UGeqGlEEtygGsfD9biehMgZNTWLLtCy--YMJgEFFll0ywMDuPydum5zcItqZN2aA9HJRVyEau5Ghw3XHf2CSzGqYOwVWBG3W0AcQLuwfqq-7_hOAyEjWxZE65BU7DLWSEZrzwA9FMgAUy-cRRUEVGWo06gKLpoaF8bCSx-gckCU6tJesJjPKQPTKVKZt_c-if_wm1L-PEc4PapgOkggeDkicQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17436" target="_blank">📅 21:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17435">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مسئول ارشد دولت آمریکا:  ایران متعهد می‌شود که برای همیشه برنامه‌های هسته‌ای خود را کنار بگذارد.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17435" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17434">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مسئول ارشد دولت آمریکا:
ایران متعهد می‌شود که برای همیشه برنامه‌های هسته‌ای خود را کنار بگذارد.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17434" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17433">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مقام ارشد آمریکایی :   احتمال امضای توافق ایالات متحده و ایران ۸۵ درصد است.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17433" target="_blank">📅 20:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17432">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مقام ارشد آمریکایی :
احتمال امضای توافق ایالات متحده و ایران ۸۵ درصد است.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17432" target="_blank">📅 20:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17431">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مقام آمریکایی: هنوز به خط پایان توافق ایران نرسیده‌ایم</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17431" target="_blank">📅 20:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17430">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مقام آمریکایی: هنوز به خط پایان توافق ایران نرسیده‌ایم</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17430" target="_blank">📅 20:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17429">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نیروهای  اسرائیل تا چند کیلومتری شهر نبطیه در جنوب لبنان پیشروی کرده‌اند و در انتظار تصمیم رهبری سیاسی هستند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17429" target="_blank">📅 20:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17428">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خداوکیلی راست میگوید!  الان بیش از 150 میلیارد دلار دست آمریکایی ها داریم. آن را به جای اینکه به ما بدهند به صورت قسطی به ما و اعراب با هم میدهند! بعد از پول نفت خودمان خسارتهایی را که خودشان به ما زده اند جبران می کنند!  پینوکیو با گربه نره و روباه مکار بهتر…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17428" target="_blank">📅 19:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17427">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsaWIFlKi3NrVrhNrW5zmJ4ddD1hQSmhkQLIZGxNyApkwBsbCms-af_u-04gRkY2WJeVXNpKFVqJKK9WaiKGvfTnnEiF2aDnVZtph12o4rn_oCFAxsWcH9eqm3lfz7_790iEZ_sRKYrF8-SyVAolV8bXcqQH4zb9m_grXs2OQC5MF9G3eVvd2fhOgEQSeqRCL_Iu2JAkGPTvHbmYCaobnefJEKfMNtXX1UNfLGWQq_DsGo-Lrh3Tgx0be9zjK3yr_N5sHtUuJ8fg6RTM_qyeYxRC2mrUfjC14_UA57nModTUzI7H1O7B1GpufONH7eh6QrqZeFnw42OWfpOD518Igw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداوکیلی راست میگوید!
الان بیش از 150 میلیارد دلار دست آمریکایی ها داریم. آن را به جای اینکه به ما بدهند به صورت قسطی به ما و اعراب با هم میدهند! بعد از پول نفت خودمان خسارتهایی را که خودشان به ما زده اند جبران می کنند!
پینوکیو با گربه نره و روباه مکار بهتر deal می کرد.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17427" target="_blank">📅 19:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17426">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">توئیت جی‌دی ونس درباره موافقتنامه  اولاً، ایرانی‌ها هیچ پول نقدی دریافت نمی‌کنند و هیچ بودجه‌ای صرفاً برای امضای توافق یا حضور در جلسه آزاد نمی‌شود.  این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17426" target="_blank">📅 18:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17425">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">توئیت جی‌دی ونس درباره موافقتنامه
اولاً، ایرانی‌ها هیچ پول نقدی دریافت نمی‌کنند و هیچ بودجه‌ای صرفاً برای امضای توافق یا حضور در جلسه آزاد نمی‌شود.
این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی ایران به تعهدات خود عمل کند، منافع اقتصادی به آن‌ها و کل منطقه خواهد رسید. این توافق پتانسیل بازسازی منطقه و ایجاد صلح پایدار را دارد.
در گزارش‌های چند ساعت گذشته چند نکته عجیب دیده‌ام. اول، افرادی که (به درستی) یک ماه پیش گفته بودند دونالد ترامپ رئیس‌جمهور تاریخی بود، اکنون بر اساس گزارش‌های رسانه‌ای تأییدنشده از توافق انتقاد می‌کنند. دوم، افرادی که می‌گویند نمی‌توان به هیچ کلمه‌ای از سپاه پاسداران اعتماد کرد، ظاهراً به پست‌های ناشناس در شبکه‌های اجتماعی باور دارند.
رئیس‌جمهور به هر حال نتیجه خوبی برای ما به دست خواهد آورد.
t</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17425" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17424">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quwTUoBuubH9vMox9ZVYeTFEhoNDRynzBHX19KA1AwCEsnqK7eA6D5-Fr5K_TXCDBY_Yc94MowGW6-zHM6llUsxeya9X28h1a-d8e5buI_qVzjoDfkl9-gKDZNM_GtWWkVaWsroRYq91EDKeJEi6qOlk3GO-1bpmrWBZXQWhSgPZHD0fuZZr3PBF4IhtUcvn0Ft6-vsVL2HjblIe0ddZXfZvZm3Jg7Syh-6GNDbHIh8KRld6VqrUnu5po42AXc_FRa2EKdYVmgn7r8BBoXHhB_HaAX0mWmjcrlzxbLYxRBgjlwW3be8GkPZoTuE4H91hFHl6H2_T9ezWtNdjqNQ1Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه دیدید یا نه؟!</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/17424" target="_blank">📅 18:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17423">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUOpI7jHeCIITmNJ_tLwlqtCA4IY1k27k1YomfuzRqVDQb64951OLYKD1wESmOx0WkpdNY2OL9JYXYd6R7tQw3ONuFKSbfTPIV37bOlOlyJrARoOvxef8zmXMPIwUCcFwsiSJAOpx9lsPhBkHFiunhf73C1EmoZM5vX1MZhWUasQjIfJSrSMKUr02uTiGTZJsU57eaCVhS6VQZLXEuDx5IK9mK1RY6JZLdv28BRrc-cSS4mfjdPnfHNg7nkBOl0uuxoyoOZXy1HeU9ve918ugs6ybVqOUjJCJWjZKrUycVKwQB6ghNZ9ljaIhPxWgS43QJybXZAAuXtR5NWy9yu6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی ایرانی ها با تفاخر متعفن قلعه نوعی با ساعت ۱۰ میلیاردی اش!</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/17423" target="_blank">📅 18:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17422">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزیر خارجه ایران عراقچی:
تفاهم‌نامه اسلام‌آباد هرگز به این نزدیکی امضا شدن نرسیده بود</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/17422" target="_blank">📅 18:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17420">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فوری | یک مقام ارشد آمریکایی به الجزیره: تنگه هرمز باز خواهد بود و هیچ گونه حمایت مالی از گروه‌های تروریستی توسط ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/17420" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17419">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فوری | یک مقام ارشد آمریکایی به الجزیره: تنگه هرمز باز خواهد بود و هیچ گونه حمایت مالی از گروه‌های تروریستی توسط ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/17419" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17417">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDX0zbt2F3G43E6D_P3nrQrYBjN3AOueWKqwOy1mtJQf4EjuzZT5vgOJuWHg0ZxYak-butbVvS34pPXKkPv6wgekzcnegm_v28f4TJvCe_Hz3zNnegWnD86INcqWQ3dKlirLameFelSfcZXkEZM99lphqeJCfyFjiRJeCZD-GfRY2FBVN3LYdFV_eSNck-mw7HiY9MAwPrd4Ffy2CDVPxwA8nsV6TGQHIptk81p2QaDVOsCm9tW5YJCNZQU__zFKMuewAxO-XU2F66bOKuEEqFYNVxHn9kygbmFkOv5EPcFdXfkrHMpvV2_Bt2s4yBsyzfzuHkbB6rc1sHDTm9uEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی ایرانی ها با تفاخر متعفن قلعه نوعی با ساعت ۱۰ میلیاردی اش!</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17417" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17412">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش سه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GF_eidkcjGt-33OPau38MsALypuxH3u0LxGjp62R09u3_ShMCa6ckznTrEQVe5Y26DVQ8d12YdyLQyVMBHdZr6T7saruk7r2DTfXv53TFA2uXLOSOphcsb0XOY6p70g6SP3eNsEFVHsjTGA_o3D93M4nQlQIdAOkkhy6_NjTbRGhVhQy1r-bhXiQaqav-skO6dwI1d0Hp_0kGUuUQ_JkO-NIfnBZmVZb8f_6SEBsArte455zbfo0Mneq-zZ3n4-RbVybD_KzNRYo1C8pqUClSpze1q8rlPHtKDDayqqNpWtXm8m6YKJX6JJqnkbNRlDGicK3KfQAZeQPPZ72QjVBUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjOUijQsKlEyLqiVJBtMxIBuOORh1duBW8EJk8PGTTwrpSG_UosKOa21w9eXJ08_nlrlDL__k8XOvPwHq35j2CLyF0ypYUQtUl9N3W5YIAJ3NciA9_JZvjHZ_2WOrFA7QCHd2TTxiBlIJCixdPnBJNcy88IgIsbA9X0JeJh8mrgvZgPJLEhsBpseiAoHXSKQn6n2O6y3lJM1VeUcRtyMeqvF1xQJJ5MHXmS1Kfqne5DNA_HIL6YMy5OQ8sULOyu-Cp0gyfSvKBWkjZxhHKWmPpylW0-PFi40L6Rj4zfsVE6xKSlQbBetgu8PTKOHo7yPmEhtiXht7AK48IybaDtvNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCZUYV5T62PqozN9Zpl7TsvNa7VIyNipfwRfRPoWXMbHRf3Cn9rgT1JkiQ8WftJcNRRib0VvoWVUQpLCdXUGYlZ5kfvkY5mJu2pVRi4K1W2Cy_caqtgL04rI6v6casa1xoE9VjaIBVsm8_aGhaw3vvbIJFOafmgnWxiVVrs_LfC8l5e97cVCdUlO-w-Y5fc6vQz2CgjFwHsZ3VCa3HxeHelAU46IPZv5ebnaEBPhOoWYuoGgKvMjAa9uLFIq0224zAPZd69J-GLaAmxnZYYUN9FWvJrAIPFmzPqNmZY8id2-Iy488J7Nc9V1LMgpNEYVtiBWKP0dvbNnI9I7js5DyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9ZeIvlOrObwZFoCsqYbLBrrWnMryV1UUShMbW0ITNf9VNGcIitcMLkzwwtl0ew5_0BsE5yHIbaRrJXqhOTmNuWikSHiYGIKxO3bGWWJVudzXRoCHA2og7EM9cUQCHltr5t4HevN1poLwiHJm0TNA4K6K5SvvwAiGtH1xByKBh7kWGQ2B-hQg3_c2cEMu-WoTgB8Hhmas7TvV9SfXXNA2KL7Hm1RKEob-2JED6z-PFO_9xA-PSKWLESewvWQIQGocekEeDychT9NwDBcRDgwIIUO-wSt2Z7FCD3WTxKd9enLHE6E8kfx75_Aixho70UC-Gmif2Nlp6PizezXPN1iPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/geZeziEp9tYOIk_W5ecU89-GuFbLYvrpLCKZssWqsHCN9P5zprHktIwY8vDCk01IsOLTMY0zEgsGYv_6Q9Vo5coEdOibeoSKYsbK86NcMBVC4wwfl6lARF5NRSFfklDw0cFoWVX--aMU_vYmgQTd_VKOM1DMdIJBREvrEevsPX8mho939borCTvnngw0pQ4w_MiPlEe9rsvH0zu2U501NOpCHr73g7hJNQtGK6jxsRfi5TMa1NDV_FItw1LuncQD8f1eAeM1z7JBSdeLzHMuT3oE24kdaE_gocihWqImfpnZwy7rtQpt1LdzSKHcrbhS-yhG_jqD_LRKkfFowxCC1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتفاق جالب در ژست‌های قلعه‌نویی؛
⌚️
ساعت "رولکس اسمورف
"
چشم‌ها را گرفت!
👀
ساعت 10 میلیاردی امیر قلعه‌نویی در فوتوشوت‌های رسمی
#جام_جهانی2026
سوژه فضای مجازی شد.
🆒
این ساعت از برند لوکس و مطرح رولکس معروف به مدل
“Smurf”
است. به دلیل ترکیب رنگ
آبی پودری (Vibrant Blue)
در صفحه و بزل که تداعی‌کننده شخصیت‌های کارتونی اسمورف است، این نام روی آن ماندگار شد. در حال حاضر قیمتی بین 40 تا 50 هزار دلار دارد.
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/17412" target="_blank">📅 18:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17411">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">امیرحسین ثابتی:   کسی حق ندارد تنگه هرمز را به امید رفع تحریم یا محاصره باز کند</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/17411" target="_blank">📅 18:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17410">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این یعنی توافق بی معنی است:   اسرائیل باید اطمینان حاصل کند که در آینده نیز توانایی اقدام مستقل برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای را خواهیم داشت و من و بنیامین نتانیاهو، نخست وزیر، به ارتش اسرائیل دستور داده‌ایم که بر این اساس آماده شوند.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/17410" target="_blank">📅 18:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17409">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزیر‌دفاع اسراییل:   رئیس جمهور ایالات متحده در حال حاضر با توجه به منافع آمریکا، از جمله منافع مشترک با اسرائیل - برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای - در حال پیشبرد توافق با ایران است و ما از او انتظار داریم که این اصل و اصول اضافی را در حوزه…</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/17409" target="_blank">📅 18:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17408">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خب این نخستین آزمونی است که باید گذرانده بشود. ببینیم در لبنان آتش بس می شود یا خیر.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17408" target="_blank">📅 17:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17407">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/390974dead.mp4?token=OqmjTKavwLgzneF5-DlvFGZRD4cTEuw4kuAX1WYbKZbXsrVUKLTtrE5DEtVreIdUZkYcWAgnP9dP7BDUhO0-0X8NeynHabDapFMuZHYOartdX4wmcMbi2CmWszf-tW2pRJ1u8tPklsyM1a6dWgy0S8vvb0lDszX9DbmJRlto3hNhOaGUTY1jonqm5KAVSDrIMm4YuKe_31yI1mvpDXKeUcRV43woZ9QM8S77sAHK6OQWjuDUDN746dyLa5m4f4zff5EyCOfd2nvY0XmbMm5TChgDWt1feB_zGNLM4ZWKLJ_yTbl-A0-K5CBTa-sL2BUxQ1FvAPi3Lt8ukPsnCHyQMhJ69viMZ9Gi1kLKZQQLTYernyP2ELDq12U2eMhevMLIiiFe2gCYMHh0Q3fw1uz3A3N3_yxaO2sqqB_QF3Uo6SuqheDgFNh8YeEsff3iDVc_1GjW25hClAOK3u00W149mkHzGXM4mTL9_dyylUAL0rSug1DI6457QPJbT6WiSZPORQ74RDbXCGGZR2-0SQre09014XvCmremupYYJmCuz12oKyzaqUfgRvhb6XAqV9apOZrbrd_yN03mOhs0HmyBck6gRvTt7cVwzJA65TEYoHFnT4PWgrNJdDUzyrcp2ZAMaHboX9y58QWuGdcWFu0Dh-sIkZDR694BKZIl1Ah0Z9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/390974dead.mp4?token=OqmjTKavwLgzneF5-DlvFGZRD4cTEuw4kuAX1WYbKZbXsrVUKLTtrE5DEtVreIdUZkYcWAgnP9dP7BDUhO0-0X8NeynHabDapFMuZHYOartdX4wmcMbi2CmWszf-tW2pRJ1u8tPklsyM1a6dWgy0S8vvb0lDszX9DbmJRlto3hNhOaGUTY1jonqm5KAVSDrIMm4YuKe_31yI1mvpDXKeUcRV43woZ9QM8S77sAHK6OQWjuDUDN746dyLa5m4f4zff5EyCOfd2nvY0XmbMm5TChgDWt1feB_zGNLM4ZWKLJ_yTbl-A0-K5CBTa-sL2BUxQ1FvAPi3Lt8ukPsnCHyQMhJ69viMZ9Gi1kLKZQQLTYernyP2ELDq12U2eMhevMLIiiFe2gCYMHh0Q3fw1uz3A3N3_yxaO2sqqB_QF3Uo6SuqheDgFNh8YeEsff3iDVc_1GjW25hClAOK3u00W149mkHzGXM4mTL9_dyylUAL0rSug1DI6457QPJbT6WiSZPORQ74RDbXCGGZR2-0SQre09014XvCmremupYYJmCuz12oKyzaqUfgRvhb6XAqV9apOZrbrd_yN03mOhs0HmyBck6gRvTt7cVwzJA65TEYoHFnT4PWgrNJdDUzyrcp2ZAMaHboX9y58QWuGdcWFu0Dh-sIkZDR694BKZIl1Ah0Z9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط سیس پیروزی حماسی اژدهای بندر را ببینید خداوکیلی !
ولی ازش خوشم آمد میهن پرست است .</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/17407" target="_blank">📅 17:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17405">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">با Secret باش خدایی کن!  با Secret نباش فقط برگرد!</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/17405" target="_blank">📅 17:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17404">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نفت بخرید و شیشه ها را چسب بزنید که ناپاکستانی جماعت کثیفترین دروغگویان عالم هستند</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/17404" target="_blank">📅 17:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17403">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6ec42ab9.mp4?token=gigP3keECbUojIgVGMkmW8_im_dB-sbPpLGSqmZe-fTDo45v_diZ2FnnR9_jxO6oifmmfNadFBtK-ozr2t1FgKTNHuytgWNxDiJl5IeZwGYDJir_w-FMeUuVWmpHHa2Erv7xJesbxzd7d8SIX1t-l0jfKfNx0gHv1B7U-4VF_3YvvI4GhfiILfoZkgD8oxzY3QQ1-X_zqEasiPXquC-YqytjlcTJ3_tYE4YAClM4R5PJEIXh8m1kH4kVTnv28tFOGFzYdHwkFmV7bmB49GTjkcdtFJoVeQCfg-c8h6Nch6X1lDa7hZLS_0ju9cPDqE_gRoG-uUIrvf5v-aAaGbD2WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6ec42ab9.mp4?token=gigP3keECbUojIgVGMkmW8_im_dB-sbPpLGSqmZe-fTDo45v_diZ2FnnR9_jxO6oifmmfNadFBtK-ozr2t1FgKTNHuytgWNxDiJl5IeZwGYDJir_w-FMeUuVWmpHHa2Erv7xJesbxzd7d8SIX1t-l0jfKfNx0gHv1B7U-4VF_3YvvI4GhfiILfoZkgD8oxzY3QQ1-X_zqEasiPXquC-YqytjlcTJ3_tYE4YAClM4R5PJEIXh8m1kH4kVTnv28tFOGFzYdHwkFmV7bmB49GTjkcdtFJoVeQCfg-c8h6Nch6X1lDa7hZLS_0ju9cPDqE_gRoG-uUIrvf5v-aAaGbD2WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب اژدهای بندر به شما نگفت ولی دونالد قرمساق گفت که منشا صداهای دیشب چه بوده!
یک کشتی هندی بدبخت حرفهای کله زرد دال بر باز شدن تنگه هرمز|ثابتی را باور کرده بوده و میخواسته از تنگه عبور کند که سپاه پاسداران به آن شلیک کرده و می‌گوید برگردد  و هندی ها با ندای :
Sepah Navy ! Sepah Navy
!
You gave me clearance to go! Let me turn back!
دمشان را روی کولشان گذاشته و برمیگردند
این به قول اژدها یعنی
نظم ایرانی
!</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/17403" target="_blank">📅 17:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17402">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شرایطی که ایران به اخبار جعلی نشت داده است، هیچ ارتباطی با شرایطی که به صورت کتبی توافق شده است، ندارد. آنچه آن‌ها گفتند، از جمله بیانیه ضعیف و حقیرانه‌شان مبنی بر داشتن یک توافق، هیچ نسبتی با حقیقت ندارد. افراد بسیار بی‌آبرویی برای معامله کردن. با آن‌ها هیچ‌گونه…</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/17402" target="_blank">📅 17:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17401">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کاش جای جراد کوشنر بودم…</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/17401" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17400">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">Buy Oil</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/17400" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17399">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">The terms that Iran leaked out to the Fake News have NOTHING to do with the terms that were agreed to, in writing. What they said, including their weak and pathetic statement on having a deal, bears no relation to the truth. Very dishonorable people to deal…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/17399" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17398">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDonald J. Trump</strong></div>
<div class="tg-text">The terms that Iran leaked out to the Fake News have NOTHING to do with the terms that were agreed to, in writing. What they said, including their weak and pathetic statement on having a deal, bears no relation to the truth. Very dishonorable people to deal with. With them, there is no such thing as dealing in good faith. AMAZING! Also, their totally rebuffed Drone attack last night against Indian Ships leaving the Hormuz Strait is TOTALLY UNACCEPTABLE. They better get their act together, and FAST! President DONALD J. TRUMP</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/17398" target="_blank">📅 17:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17397">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مجری فاکس نیوز در مورد توافق ایران، به نقل از یک مقام کاخ سفید  مواد هسته‌ای نابود و حذف خواهند شد  برنامه هسته‌ای برچیده خواهد شد  هیچ یک از پول‌های آنها تا زمانی که عملکردشان را نشان ندهند، آزاد نمی‌شود  تنگه هرمز باز خواهد بود  ایران هیچ گونه حمایت مالی…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/17397" target="_blank">📅 17:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17396">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17396" target="_blank">📅 17:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17395">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17395" target="_blank">📅 16:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17394">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ایران وضعیت تنگه هرمز را به سطح قبل از جنگ بازنمی‌گرداند - ایرنا</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17394" target="_blank">📅 15:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17393">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17393" target="_blank">📅 13:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17392">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17392" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17391">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">متن کامل:  خبرگزاری نیمه‌رسمی مهر ایران فهرستی از اصطلاحاتی را منتشر کرده است که گفته می‌شود در پیش‌نویس یادداشت تفاهم با آمریکا وجود دارد. این خبرگزاری به منبعی نزدیک به تیم مذاکره‌کننده ایرانی اشاره می‌کند، اما جزئیات به طور علنی توسط تهران یا واشنگتن تأیید…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17391" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17390">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snkdJuJXvkr5gh8dUic67l7gCpQ9OOAtc3k65Y14QPYaUl4mNPeDRQ-GcG6Yt5p4dHgn07hRPcFeLed35-XQYYBN0kZAYkmqe4I85wrcghmBaWAbHEZ1xA3X0vEOcvAkrnQbZ4b_9YOau9kbI9RqdkljEmhEGIs71ktecdKJk6NfhYZJmviztIqWp0iHn1j66hFG9fZmob_idlqvCasQlm9tJ_Cz_kJk0W-kgsHcjdHcpyHIuwBBiu5oLCKfGlA-4CQXvJZqQYMF3nhvYlog6Io0p92d5pSr4eT0F0pqgNTqe0LuXUsU6lENEw80Vv_10k8OIxf3ZYZE7WE_Y05dLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزودن شدن 1500 میلیارد دلار به ارزش بازار سهام آمریکا با اعلام توافق دیروز توسط ترامپ</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17390" target="_blank">📅 13:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17389">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نتانیاهو.pdf</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17389" target="_blank">📅 12:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17388">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حملات سنگین هوایی اسرائیل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17388" target="_blank">📅 12:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17387">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBtF_3TUI8tdq0WjybHOX6MoSY8UlLfZ6-iqEL1EPxrqhCFOxMtqybtgVX8brqXI_YlfOii1E-L6xlVXYmE7Vh1eqWF_xQvO4mILi1of48WBHcFfgOulmTCDJLklHd0dL7K7vUSaMgzPwtENT5qqZSIpJAhAmmrIK2MCOWECgBSPq6oO3eQQkcj5mHhU3_TfblqMIEdgTwbXz6Gcg6wvhqebr18VuU4m6R7789o7rhReQaa2Y9j5pb58HdyghGbtzYf0ULpKdZgDr4mhL45Q4d_ByQ9tTvu68s6S5w3uKSJOXpmC5C28hGqfYQnskhkSdmFvRZ4m9dbjJfoiRJL0Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این نخستین آزمونی است که باید گذرانده بشود. ببینیم در لبنان آتش بس می شود یا خیر.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17387" target="_blank">📅 12:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17386">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اسرائیل 2000 سال آینده را نخواهددید.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/17386" target="_blank">📅 12:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17385">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اسرائیل 2000 سال آینده را نخواهددید.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/17385" target="_blank">📅 12:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17384">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سردار نقدی:   انتقام ما، آزادی فلسطین و محو صهیونیست‌ها است، اما این مسیر باید منطقی طی شود</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17384" target="_blank">📅 12:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17383">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سردار نقدی:
انتقام ما، آزادی فلسطین و محو صهیونیست‌ها است، اما این مسیر باید منطقی طی شود</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17383" target="_blank">📅 12:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17382">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">توقف دائمی و فوری جنگ در همه جبهه‌ها، از جمله لبنان</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17382" target="_blank">📅 12:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17381">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ایالات متحده موظف است طرحی برای بازسازی اقتصاد ایران ارائه دهد، در حالی که مذاکرات نهایی بین دو کشور باید در مورد مسائل هسته‌ای و اقتصادی و بدون بحث در مورد برنامه موشکی ایران انجام شود.  خبرگزاری مهر</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17381" target="_blank">📅 12:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17380">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">همچنین ایالات متحده وظیفه دارد غرامت جنگی پرداخت کرده و از کل منطقه غرب آسیا خارج بشود و ایران را به عنوان ابرقدرت چهارم جهان به رسمیت بشناسد.</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17380" target="_blank">📅 12:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17379">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ایالات متحده موظف است طرحی برای بازسازی اقتصاد ایران ارائه دهد، در حالی که مذاکرات نهایی بین دو کشور باید در مورد مسائل هسته‌ای و اقتصادی و بدون بحث در مورد برنامه موشکی ایران انجام شود.  خبرگزاری مهر</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17379" target="_blank">📅 11:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17378">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ایالات متحده موظف است طرحی برای بازسازی اقتصاد ایران ارائه دهد، در حالی که مذاکرات نهایی بین دو کشور باید در مورد مسائل هسته‌ای و اقتصادی و بدون بحث در مورد برنامه موشکی ایران انجام شود.
خبرگزاری مهر</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17378" target="_blank">📅 11:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17377">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الجزیره:
ادامه حملات اسرائیل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17377" target="_blank">📅 11:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17376">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ برای ۱۴ ژوئن جولانی را به کاخ سفید دعوت کرد.  ترامپ به ان‌بی‌سی گفت که می‌خواهد «حمله‌ای جراحی‌گونه‌تر به حزب‌الله» در لبنان انجام شود و دمشق را به عنوان عامل این کار مطرح کرد: «ما می‌توانیم به آن‌ها در این زمینه کمک کنیم یا سوریه را پیشنهاد دهیم. سوریه…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17376" target="_blank">📅 10:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17375">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فوری | یدیعوت آحارانوت از منابع خود گزارش می‌دهد:
نتانیاهو گفت به ترامپ اطمینان داده است که تلاش او برای دستیابی به توافق با ایران را درک می‌کند، اما اسرائیل نباید قربانی شود.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17375" target="_blank">📅 10:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17374">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ برای ۱۴ ژوئن جولانی را به کاخ سفید دعوت کرد.  ترامپ به ان‌بی‌سی گفت که می‌خواهد «حمله‌ای جراحی‌گونه‌تر به حزب‌الله» در لبنان انجام شود و دمشق را به عنوان عامل این کار مطرح کرد: «ما می‌توانیم به آن‌ها در این زمینه کمک کنیم یا سوریه را پیشنهاد دهیم. سوریه…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17374" target="_blank">📅 09:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17373">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آمریکا: دو پهپاد انتحاری شلیک شده به کشتی‌ها در تنگه هرمز را سرنگون کردیم
نیروهای نظامی ایالات متحده دو پهپاد انتحاری که به سمت کشتی‌ها در تنگه هرمز شلیک شده بودند را رهگیری کردند، این در حالی است که گزارش‌هایی از شلیک ایران به کشتی‌ها در این منطقه منتشر شده است.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17373" target="_blank">📅 09:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17372">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">در روزهای اخیر گزارش‌هایی از تحرکات جدید نیروهای وزارت دفاع سوریه در مناطق مرزی با لبنان منتشر شده است. بر اساس اطلاعات موجود، یگان‌های تازه‌ای به غرب استان حمص، به‌ویژه مناطق القصیر و نواحی مشرف به دره بقاع شمالی، هرمل و عکار در لبنان اعزام شده‌اند. این تحرکات…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17372" target="_blank">📅 03:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17371">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">در روزهای اخیر گزارش‌هایی از تحرکات جدید نیروهای وزارت دفاع سوریه در مناطق مرزی با لبنان منتشر شده است. بر اساس اطلاعات موجود، یگان‌های تازه‌ای به غرب استان حمص، به‌ویژه مناطق القصیر و نواحی مشرف به دره بقاع شمالی، هرمل و عکار در لبنان اعزام شده‌اند. این تحرکات در ادامه روندی قرار دارد که از ماه مارس آغاز شده و طی آن دمشق اقدام به تقویت حضور نظامی خود در امتداد مرزهای مشترک با لبنان کرده بود.
مقامات سوری هدف اصلی این استقرارها را افزایش امنیت مرزی، مقابله با قاچاق و جلوگیری از نفوذ عناصر مسلح عنوان کرده‌اند. با این حال، اهمیت این تحرکات در شرایط کنونی منطقه فراتر از مسائل صرفاً امنیتی است. مرز سوریه و لبنان طی سال‌های گذشته یکی از مهم‌ترین مسیرهای انتقال تجهیزات، نیرو و پشتیبانی لجستیکی برای گروه‌های مختلف فعال در منطقه بوده و تحولات جاری می‌تواند بر موازنه‌های میدانی تأثیرگذار باشد.
همزمان با ادامه درگیری‌ها و تنش‌های منطقه‌ای، دمشق تلاش دارد کنترل مؤثرتری بر مناطق مرزی اعمال کند و از تبدیل این نواحی به کانون بی‌ثباتی جلوگیری نماید. هرچند تاکنون نشانه‌ای از آمادگی برای عملیات گسترده نظامی در داخل خاک لبنان مشاهده نشده است، اما استمرار اعزام نیرو و تقویت مواضع مرزی نشان می‌دهد که دولت سوریه تحولات مرزهای غربی خود را با حساسیت ویژه‌ای دنبال می‌کند و آماده واکنش به هرگونه تغییر در وضعیت امنیتی منطقه است.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17371" target="_blank">📅 03:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17370">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
🇮🇷
- دونالد ترامپ:
ما امروز جنگ با ایران را به پایان رساندیم و آن‌ها توافق کرده‌اند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن اصرار داشتیم. این همان هدف اصلی بود. این ۹۵ درصد از آن بود. و، اوه، آن‌ها این کار را به قدرتمندترین روشی که ممکن است انجام داده‌اند.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17370" target="_blank">📅 03:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17369">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فارس:   دقایقی قبل نیروهای جمهوری اسلامی ایران اجازه عبور یک نفتکش متخلف که بدون هماهنگی وارد محدوده تنگه هرمز شده بود را ندادند و همزمان سه انفجار هم در سیریک شنیده شد</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17369" target="_blank">📅 02:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17368">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ:
بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل و تأیید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی شده علیه ایران را امشب لغو کرده‌ام. مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات کامل، توسط همه طرف‌های درگیر از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران تأیید شده است.
محاصره دریایی تا نهایی شدن این معامله به طور کامل ادامه خواهد داشت
— زمان و مکان امضا به زودی اعلام خواهد شد.
دونالد ج. ترامپ
رئیس‌جمهور ایالات متحده آمریکا</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17368" target="_blank">📅 02:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17367">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99919094c3.mp4?token=vzXFVeaMzIyIPHkb7C4FmdXxQErnnEb1vh493fZM6uQa7PvP9WBwNQvASbJLq77DQ68vd-xteArZ5ImxfPkHq3KZe89K_boGNTfwZQeFfjMvK9pmzmsqjTUjDY-ldSqiWRD9dD0WO-8rNM1YXbTIwnSsHW-_T-lDWaWeE5uXfCAOeA4Jmi1xxUzGwbHKxp9_d8VL1Yg8qz2FVPTQGoqbyM0odiykOji56stHw7iiimQhKUmZ91At5oadj2lHGTKO1987BzNemZ9LC7ebeE1muG6p-AN-WPvnGpNXt45IwVxvX-I8ICX_12beZXPbGUEzcj9u3FuBnyLr7ePRNdV6OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99919094c3.mp4?token=vzXFVeaMzIyIPHkb7C4FmdXxQErnnEb1vh493fZM6uQa7PvP9WBwNQvASbJLq77DQ68vd-xteArZ5ImxfPkHq3KZe89K_boGNTfwZQeFfjMvK9pmzmsqjTUjDY-ldSqiWRD9dD0WO-8rNM1YXbTIwnSsHW-_T-lDWaWeE5uXfCAOeA4Jmi1xxUzGwbHKxp9_d8VL1Yg8qz2FVPTQGoqbyM0odiykOji56stHw7iiimQhKUmZ91At5oadj2lHGTKO1987BzNemZ9LC7ebeE1muG6p-AN-WPvnGpNXt45IwVxvX-I8ICX_12beZXPbGUEzcj9u3FuBnyLr7ePRNdV6OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به نظر می‌رسد که شرایط توافق با ۱۰ شرطی که جانفدایان میگفتند خیلی شباهت ندارد!  از توجه شما به این موضوع سپاسگزارم !</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/17367" target="_blank">📅 01:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17366">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ایران تمام دارایی‌های اقتصادی مدیریت شده توسط ایلان ماسک را به لیست هدف خود اضافه کرده است و شرکت‌های ماسک را متهم می‌کند که در حملات دیروز ایالات متحده علیه ایران کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17366" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17365">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فارس:
دقایقی قبل نیروهای جمهوری اسلامی ایران اجازه عبور یک نفتکش متخلف که بدون هماهنگی وارد محدوده تنگه هرمز شده بود را ندادند و همزمان سه انفجار هم در سیریک شنیده شد</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17365" target="_blank">📅 01:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17364">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارش های تاییدنشده از انفجار در بندرعباس.
گفته می شود ایران به چندین کشتی که حرفهای ترامپ را باور کرده و قصد عبور از تنگه هرمز را داشته اند شلیک کرده است.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17364" target="_blank">📅 01:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17363">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رسانه‌های دولتی ایران: انفجاری در نزدیکی ساحل سیریک شنیده شد؛ علت و منبع آن نامشخص است</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17363" target="_blank">📅 01:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17362">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwV2ISMj1yEeLkWAXwC5YnBm4aMPVADDh4lnuCRATHQ_DLo_u9TpslnOIAFvfL8lavwFZB6LKvLbuYmBPLaMh2CXm__37VDum2rK0pN5ISbAz7tR7gEOki1WB-9KiQUPNuNRBbwTcLXDFZgq8WoSvG7rVIpyMqYt6jtGxyaihm0OymI3afecIrGvm8fcx1NaJbQBJVqRtNLxYNhYe-U_9hMgmN5dul5ULrw3_IE9gVR3bP91oYtUzKcBiptEwC6xfS50lTKjPUXrFCETeVC1qes5OMuQ8Ck5NgimXKf79ID1teaUHYt35riLkqtost9rS4SV8lIllCECalZrm836zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضایی (ب) قهرمان | امید هر مسلمان!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17362" target="_blank">📅 01:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17361">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📡
حسین اژدهایی ؛ خبرنگار ویژه صداوسیما در بندرعباس:  در قشم و چند شهر دیگر صداهایی شبیه انفجار شنیده شده است که هنوز محل آن نامشخص است</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17361" target="_blank">📅 01:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17360">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رسانه‌های دولتی ایران: انفجاری در نزدیکی ساحل سیریک شنیده شد؛ علت و منبع آن نامشخص است</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17360" target="_blank">📅 01:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17359">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کاش جای جراد کوشنر بودم…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17359" target="_blank">📅 00:23 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
