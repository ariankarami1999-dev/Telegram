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
<img src="https://cdn4.telesco.pe/file/HgkoQVlOyRrj3YgIiyBX1ZAUiF7bDbh8fW_S10At4-li5FNmrdSrgjlxr9heuiCmt-RiJmfAEuC_mJRkXfnL4sIDto9Gpak3xlBY9TSSDwv2vFO9dAKabIqBNsQAr3j7kp5jv_bsWQ3celvuTdUIWti89KTIj4G7HyCTPh21Jx4OP-TLyVWgqoZbfDTXuKUFDVJNCzT_GbA4m9eWSeL7WAxsMoFNw9sEcdYgTwgoZd6UETxmPp2uvIQxBJy5pbw8NjFUJudH_jiwBOdDhfEeHBWMPSWxlkoRHmXWLhrBTPncWLb-TF5dJXjKw2JTDA051HhJJh8RNNGz0eKidst52g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 172K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 16:18:20</div>
<hr>

<div class="tg-post" id="msg-68174">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reX_HdEnuXf3Un24NHzgo9X6ruzriFMWKEsa7QYNUMT0ysAw1R63l9qCF59jUDgssLahTtDCKNnIttmw8u_NgrGd0ULaPq3xEe-tk1q0fQ8vFb3716iZ9yQ6eYqReum5I1wZpDdTSDP6Nw6WzBmeN4LgAWKyd2Ku7y679XNveuxd6juBNIjyWoZZ0kRLeayWRLUCxJ3x7_0z7BosUFLLktV7QYP6E0ayGfUAEG2NlD0LjwDwTOZo_2oY_Ghl-cehM8YtwWK-V7IhenFZyU1eFwbY6EtQMXuIzN6ygXEMW_vgclUoS-yQeXconHbVa-e-dFT_GNP_Hzeme14MSbk9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=wAuTyie6caxrmKj457tUEvo6DmdyHhtHFos7Eo4yVf9TwVXSCMbEnU8Li8Q4qjxPf8s77X5qywfW4BPxDpj6BTuPqCFyhn5q8oNTNotHs5HujCmNrEHheJ8l8mH8s_DXWSu83LcGQTWoVsGmeEMXwSI3Fkii_hL-K5_aPIzj4ryQGRRQNJ2QiMyIyOq7L4sWufBpPlBNWqxO6FaSA-ZjqRCWlK5eIT1Bl62WErPstHpVSAHoFSiSQq7jeuBqnzGq8xO0pfmVKt-AXmwkfwiTc73ksciaGDz96ry0AsfvlkomJPnJeRm6JoTMsjPrzS2YeRdkOg9XzimKgVzZB121wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=wAuTyie6caxrmKj457tUEvo6DmdyHhtHFos7Eo4yVf9TwVXSCMbEnU8Li8Q4qjxPf8s77X5qywfW4BPxDpj6BTuPqCFyhn5q8oNTNotHs5HujCmNrEHheJ8l8mH8s_DXWSu83LcGQTWoVsGmeEMXwSI3Fkii_hL-K5_aPIzj4ryQGRRQNJ2QiMyIyOq7L4sWufBpPlBNWqxO6FaSA-ZjqRCWlK5eIT1Bl62WErPstHpVSAHoFSiSQq7jeuBqnzGq8xO0pfmVKt-AXmwkfwiTc73ksciaGDz96ry0AsfvlkomJPnJeRm6JoTMsjPrzS2YeRdkOg9XzimKgVzZB121wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی منتشر شده از انفجار در چابهار صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/news_hut/68174" target="_blank">📅 16:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68173">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=N4lXkAEW7-4abtyWuo2Doca0JrqisR8H6O6aF8a0Mm1w2wkdRsYRLFzYHR4Cl32bBokf2QLkq8bYjy7NF0WEtjSKXODVVwF3HEnaV4goodS7P9t5JyKJyFRzfaF2LNQD-zZ23TDB3rE3lsxYmV_Tb7u9ZEeU5yfA2C6l9xlik6risOrLT-er9QBjo8tgBfc8zdg1YdmrhggKFZJAyGCfQKC7PFi9JGS0mu4xfxomJgoqt3jaO8EDA87CZXV6D4P_deola93FUfIVcDUImPFH8UvntnzJYRs7QQ2cHbCMFJN-KE8FYei-sHjBjQTztIePQP4MYDNpYkhiuJhNyFopRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=N4lXkAEW7-4abtyWuo2Doca0JrqisR8H6O6aF8a0Mm1w2wkdRsYRLFzYHR4Cl32bBokf2QLkq8bYjy7NF0WEtjSKXODVVwF3HEnaV4goodS7P9t5JyKJyFRzfaF2LNQD-zZ23TDB3rE3lsxYmV_Tb7u9ZEeU5yfA2C6l9xlik6risOrLT-er9QBjo8tgBfc8zdg1YdmrhggKFZJAyGCfQKC7PFi9JGS0mu4xfxomJgoqt3jaO8EDA87CZXV6D4P_deola93FUfIVcDUImPFH8UvntnzJYRs7QQ2cHbCMFJN-KE8FYei-sHjBjQTztIePQP4MYDNpYkhiuJhNyFopRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۷:۳۰ صبح به وقت شرقی روز ۱۵ ژوئیه، دور دیگری از حملات علیه ایران را به انجام رساند.
سنتکام در جریان این موج عملیاتی ۹۰ دقیقه‌ای، با استفاده از مهمات دقیق‌زن، سامانه‌های پدافند ساحلی و همچنین محل‌های نگهداری و سکوهای پرتاب موشک‌های کروز در جزیره تنب بزرگ را هدف قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد
@News_Hut</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/news_hut/68173" target="_blank">📅 15:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68172">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=jJybG_j8CZIMRmM95r6w7_AXS8H4fZZz7oprod7rvGQYHHp4FxZWztIl3xTEB11UU-buAWzrlLaCmrStBj337nPx0gK3OSe5Gi_g7mZtSU7Zzj_A64Vif4pGRZVbNwSpWORrz_eCi0PEN3Fn2vcc7w-kocDOeB752DYTizgX_YV8m7lpwfxQdo40IFkvUMLOGAZTTAOrRrZEMDc5nvRfvlBaZmCb4voz-H0iYHu8wrFOlb5aNlDRLl_r5pj9jFGPq9h3bUMcbjtAr1M5Ye8nGN0Mlt61CiDThGvV5jzboOSu_sFls736oZGKZyzNlJcksVtnqx1bgPnIrJQfL3sZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=jJybG_j8CZIMRmM95r6w7_AXS8H4fZZz7oprod7rvGQYHHp4FxZWztIl3xTEB11UU-buAWzrlLaCmrStBj337nPx0gK3OSe5Gi_g7mZtSU7Zzj_A64Vif4pGRZVbNwSpWORrz_eCi0PEN3Fn2vcc7w-kocDOeB752DYTizgX_YV8m7lpwfxQdo40IFkvUMLOGAZTTAOrRrZEMDc5nvRfvlBaZmCb4voz-H0iYHu8wrFOlb5aNlDRLl_r5pj9jFGPq9h3bUMcbjtAr1M5Ye8nGN0Mlt61CiDThGvV5jzboOSu_sFls736oZGKZyzNlJcksVtnqx1bgPnIrJQfL3sZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جنایت ۱۸ و ۱۹ دی ماه؛
تا مدرسه میناب و پادگان بمپور؛
نام‌ها عوض می‌شوند
اما قاتل یکی‌ست:
جمهوری اسلامی؛
حکومتی که برای ماندن؛
ایران را می‌سوزاند
و جوانانش را قربانی می‌کند.
#hjAly‌
@News_Hut
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/news_hut/68172" target="_blank">📅 15:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68171">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH2YB2xHWxPkLmVM5QmmIqa9C0SUNHL5X9GPnC4_A01lE8ccI5iOqnrfXyoYwjZy0TeAqDUW89PApUftrKvP9iyM6prqZVBa_gULQvvRshlogE7kHVlv6_pC10ztL0efZNKq3V8KI1MJFBM5nI9jCOrlVcu89CtK6w0uZT6LqexBENaWk49SHLzFkLaX-cv4B46jpcs5oPsBLDPS4BvN7n9BBx1kmCQ9TcwgnAwV6s1wDe7lxu4_krXeWNzwoidHvKlGa7K_Pq7twzNmMe73oI83d2l-AfxXF5SnbH9VSUioEQ_Hw6twq0uCWT2yJ7NRqN_mQdaatR0bHQBkvNxyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری حامد‌لک:
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/68171" target="_blank">📅 15:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68170">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9X-czq37V2TTSOYic44sVS16_l0-200VEJF7diyHqlcSEiOMMGrcsHKEEVwbWbVQo9Zv13Ej7QdkY5xFk1MXlTiqaXxDZiiGfmvuCvQUpQe8pxnJDRnwy0z6cw_yLqBCWETR7W-Iolw2nFUnRaGTBYEJsFY7eHXnwBTO96mQsU8QZR7uYz0HZviIdUvYaHfzj0xVTGugaiBRZxWoLouW97gCsMQb6dVC06z8y5XXHRvNmjHhbvD2Vttxufxkyf9AJvFm_xLz9y5SoIPGO4IlZPMVjGh7actWM2PS_XyQJM9LLWlkRt-8xxUSRsy0ul09YdRWYuKXBMlJbh9yxMsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
چهارشنبه ۲۴ تیر ۱۴۰۵ جام جهانی ۲۰۲۶ مرحله نیمه‌نهایی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- انگلیس - آرژانتین
🇦🇷
ساعت ۲۲:۳۰
ورزشگاه؛ مرسدس بنز آتلانتا
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/68170" target="_blank">📅 14:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68169">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
پنج انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/68169" target="_blank">📅 14:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68168">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">علاوه بر اینکه سوالات یکیه و باید همزمان امتحات گرفته شه، تسنیم اومده گفته فقط نهایی دوازدهمیا تو روز ۲۵ و ۲۷ لغو شده، این درحالیه که دوازدهمیا اصلا ۲۷‌ام امتحان ندارند و یازدهمیا دارن!  باید منتظر واکنش رسمی اموزش و پرورش باشید @News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68168" target="_blank">📅 14:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68167">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mob3k5bTCFsYS5Lw6jMlkYTV6BkVwbphH5EpTBWgk-b4FGqv1okbsDBGonMdia6sbs97Xb3Je-Z3KR6njnPU4D5eVlbtHFY_f0sBAcTmr60mcBiTdfy5_sFa7LMwUl3XgzZKBrchtGcTwUcVV5WpEwAUNnra-MeNM9-0StHsfm8dHOtxTwX7w13A94GZa8Cmvq4NXNF99eBVhySHgz50uPzuUYZGBCr05kd5KDdKyPfHokgy7j14RXjGWccxKChn4JSSoVkjkijq13vDq386TNNvRcZkzYDqI4EwSFsBxrIFdGOU4idXjdJFvlm02rUAbYkhNMMRL4x5vDHBrgYd5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری نهایی رو فقط برا چند منطقه لغو کردین، کاش این دو روز کل ایران رو لغو می‌کردین تا فاجعه‌ای دوباره مثل میناب رخ نده... #hjAly‌</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68167" target="_blank">📅 14:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68166">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=gzfBSuBd8qCsD1gm6qjFONEVJ12y7zrp7ruBtSzsfJ3QIos9Yi9KiBpEyxNnuoGEeY-AV044HtlVHEh7Ak59v_1O7QYPtwGejaH7KuRtPb8wLwI6foW3MZAMtSi7lb2IZdqEAW0hT4-yVWprhtwxzPcdLiisFiJkNCVvrPoX81DVulnY-aMjfOGVw3zThs-JmyN5PAQd63LGdyBY174oJuovU2n8n7kMXBXr6_sVlykLVGYcE9JeC6VwSkGFFSOlpvpd_onfAtn3f8d8etbS82E-VM1f8ksrMmJrcUiEV-P6D9KBZ-dFQVH8wBhoOsLjVij7GJZNILzehi3tZ7Qhjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=gzfBSuBd8qCsD1gm6qjFONEVJ12y7zrp7ruBtSzsfJ3QIos9Yi9KiBpEyxNnuoGEeY-AV044HtlVHEh7Ak59v_1O7QYPtwGejaH7KuRtPb8wLwI6foW3MZAMtSi7lb2IZdqEAW0hT4-yVWprhtwxzPcdLiisFiJkNCVvrPoX81DVulnY-aMjfOGVw3zThs-JmyN5PAQd63LGdyBY174oJuovU2n8n7kMXBXr6_sVlykLVGYcE9JeC6VwSkGFFSOlpvpd_onfAtn3f8d8etbS82E-VM1f8ksrMmJrcUiEV-P6D9KBZ-dFQVH8wBhoOsLjVij7GJZNILzehi3tZ7Qhjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خسارت وارد شده به یک دکل مخابراتی در بندرعباس پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68166" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68165">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
#فوری؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.  وزارت آموزش و پرورش:  بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68165" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68164">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
#فوری
؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.
وزارت آموزش و پرورش:
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه 25 تیر و شنبه 27 تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/68164" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68163">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTREpeG0WWP1u_9yHIJyRZ8bnr_v8JluCYPU5_Q1lw_CZHkaH10aTqy5yl5df8DyChhY2HrRIq22TlEE0tvdXB3PWS4NsThBv72xvf1HkCs7WT0w5R-A4co8ja0vYFMvf8Vb2tKaKGcXQ3dInkk2GnZSUUm0_TOZrcR_nB7cw4uPc7vgDO0Rn_hg0aVebKoV1JV-zNHlgSn1eMVTrFDZYeZ0UZkQZRSbyijCOpv9AzqcCrZmL6TTaycIlYtVvhr45H9EinAvNIpxhc9MMh3OXldd9UPaw0xrTRRF2CKRY8EaBLoVN608fO-MLzkC6QjQz8IaEHtBZ-lEcPlYEidDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ صبح به وقت شرقی، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) موجی از حملات را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانمندی‌های نظامی‌ای است که نیروهای ایرانی برای حمله به کشتی‌های تجاری در تنگه هرمز به کار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/68163" target="_blank">📅 14:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68160">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5ulyIA5lgEjKoVDcgr42_Z8UHT8ZC9JOBYKfYRC8cZs1Mjgr8fMVilKXmLsniOXMdySzOiAS5qmaiIhN63P7eV8kIsE_gLahIjdp2yXGW07XlZOWMhTTPg-IHQl5WTQ9ifidtNJuAqRORwPfQuwtuE8b1EGNi-iL_gmm7OkmUMesn5snSEgjvTlGbCNgEYoHMrTbGBfJrBPnCwEZrobIO1dWjXTbxkhhdLbxoomUo0fY3doOWTPviVW_ddqAmMi2rVq3uIREBrIWq2EQlP00zzfpbcGEPKXQ2o_FiBzG0l5XFc8Q3c1vbxBZmzHTY84eniRMStSCRnUGd1DOMoqww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xqq6frW29p1hT0w_pGQZ_gAl48N3MdaG4E2wM_sOuZSirvXNJNBN0zVWyafLktktr2h_Y-b0L-xABv1YfthG0HMbS8tJL-CYCF5HlvG7ujotFl_SAfVvzAJd8WRSL9_MxEB3PyCWvQH3T1x2VW78WAyH1u5porKKxWj5_IXDsQ685wKlR3xmCZHnKhqvLguxhKmnx-QZ0L9JjFq8scyTxYUcYXeS8dXrg4-_7czo3LS2E_H8mZBrH1K3BZ8XNs706rmxZZUIOGtgHxqvVrDGRYzqIA1BOhSfSWRvF6Wq4FcLylDiBmoAmEadP_mo43IFVmczZiFahTkIOVytcYI1lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=qmuglpwepclI_3JhYCaTIMGPcCVPbc7KxpKOjJJSTNezzfFCftgktFwmqa1POlpYn_C0Fa7L9fX-XwizjLX5_sYJiWxNZq3XBc5nDqPoufy70PGjtbhO6qZ1TPDq7NwOwB2RheF-3DKSn9zBcju0tG8KsV5gLrmBSCpC9XAMkOEPMlm7PhEXiZ8sRJE3jhMm_tVQMCYFD8MvX9jh2gIRiEOkwRUP3HcKChd5jY69JhW8iQi1Nc20V54blbeObEqLYD5RpG6XbwCJcvK_R3WmeVAr-RzTwCQ_jZaC3XADDRV5cC3ku0fZdzFbAIiqs_cWohF9Ml9nVC0_rmXJTiS3zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=qmuglpwepclI_3JhYCaTIMGPcCVPbc7KxpKOjJJSTNezzfFCftgktFwmqa1POlpYn_C0Fa7L9fX-XwizjLX5_sYJiWxNZq3XBc5nDqPoufy70PGjtbhO6qZ1TPDq7NwOwB2RheF-3DKSn9zBcju0tG8KsV5gLrmBSCpC9XAMkOEPMlm7PhEXiZ8sRJE3jhMm_tVQMCYFD8MvX9jh2gIRiEOkwRUP3HcKChd5jY69JhW8iQi1Nc20V54blbeObEqLYD5RpG6XbwCJcvK_R3WmeVAr-RzTwCQ_jZaC3XADDRV5cC3ku0fZdzFbAIiqs_cWohF9Ml9nVC0_rmXJTiS3zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/68160" target="_blank">📅 13:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68159">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgl-FE-AId9EfE33vkQmh03MiX3Zm7SO_EeRRybQJJWz4aUOnPc01Uo2TsRpzuG5hmNny0SrOjFS9VI2ZBeqLN-QpZpAvv-tQI2SbVfUPU19CpmgJAyQOcdidJ0iHScYVnYYbPod3XomQxdX2uqIPW4VC2bNX4A5tIgEKRAEuOMgbJ_WH3Q3IOh6vGSY07IwlKjHrSU0jeW5syn1rZAcAcGTEEdZOOBcX2rXkI5ljQnd-ygsWaKtA8p2KxL0tqmteO7Vkf0M-aQO024L2_bmLOEukYV-nhBuAB6sEfJ5TRcT2ascs2rgb0JUVvdVmdbVvtj-OdYr5CIL1jQ7Yfbhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68159" target="_blank">📅 13:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68158">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSb6YbkDsdjsf2xE6FyrG54zwlSnCPYREhjz-fdJWdRPJDmYgyv9WOsCKCd_gFQ770U75nLd3WLtDQHsz5Ve8aGi0rt9DxWtF99o-YqVmuIzpUtGX5e_Ql4rPSXQFqw7xigekGtuJ_HmFgor9mUeYrK1yLXs9VGNT1X4rxzKENXPdvEkrZirNHPkHa7KrmAauZo1a4Lk888E1CEppoCtXVhjjhXwqZAkUaVrcvJvDKeUfN4CDvefzgjiSd1MEQWsoQtleCwDdJvvVqDyAGjy_P3XQl9tMdmNL19TzNDgXIgmUQ0ELAvBIvQNdjp7OGf8-SyYpskqTF7Raaa6fkhFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرِ داریوش فرضیایی (عمو پورنگ)، بعد از تحمل یه دوره بیماری، تو سن 90 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68158" target="_blank">📅 13:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68157">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
امریکن گات تلنت یا همون عصر جدید آمریکایی ها
یک شعبده بازی توش انجام شده که حسابی وایرال ‌شده
👀
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68157" target="_blank">📅 12:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68156">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HigEvfNcOpDvQ8F5xOj1O1a_pSiUeyskrQAejw0ClAQwxuob4r2GpshxfGT-PIhz_-ZVMPUINVux8aTGBk2PbjH4wUuosXJofZlWRjpLiW32WKFnTvrLuryi4iZCJGVYCdBkZDTShgfIeLlTLNWmEN_0gzHSDHsEdNUsYUlK9SeVEedRLN--QKKhyOJnB44qTCjN3wVTvnRcaPIHEGnu4QMZ2V27t-bNhistwy1GXw492uTLwtCRI-T7p3_pCSqHC6WR8NLdiln_XMWcRbyH3MJb6hrkEuJY08svsxyVUD8EESYz36qGeaRueZTCw4rKS43rBqYwTg8A7GfQSFM3RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ا
کسیوس:ترامپ در «اتاق وضعیت» جلسه‌ای درباره حملات جدید و گسترده علیه ایران برگزار کرد.
به گفته سه منبع آگاه، رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای را در «اتاق وضعیت» (Situation Room) برگزار کرد تا درباره یک عملیات تهاجمی گسترده علیه ایران گفتگو کند؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
به نظر می‌رسد ترامپ مایل است جنگ را تا حدی تشدید کند که خسارات کافی به بار آید و در نتیجه، حکومت ایران تنگه هرمز را باز کرده و خواسته‌های هسته‌ای ترامپ را بپذیرد.
ترامپ این نشست را در حالی برگزار کرد که ارتش آمریکا برای چهارمین روز پیاپی، حملاتی را در منطقه تنگه هرمز و در امتداد سواحل جنوبی ایران انجام می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68156" target="_blank">📅 11:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68154">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=cGK3KcLhkagVsxufc7PRp3MXYn-zZvIBTLLC5LCgVFz4iqa0DG5_-Agp7bfaWBxi7xUO_bHfS2Kbdm2E_qxzOhTcLQr08kxqk6s55hV--gLr_xHIsEpfmCC7u_3HHl-09s6Sc8qdQlfkCz9DMpC0aDuuznIqBFDTvUPMMwclrrw0xm_PuMzqViniTBLei3iUqFX16rqqy7J2M4RCSWRAu8HAU9ur11b8zJ24XBCvxLjdT1P1EJNkZNdgLbzAriBpgNuYiQdSaW9rhjFiVJ1IQxxVzQJqrJkb1hdZK8JOH1Qtj9nlsfndliyPoUBK_iHfVJaofSdcsunoKo3WEL852g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=cGK3KcLhkagVsxufc7PRp3MXYn-zZvIBTLLC5LCgVFz4iqa0DG5_-Agp7bfaWBxi7xUO_bHfS2Kbdm2E_qxzOhTcLQr08kxqk6s55hV--gLr_xHIsEpfmCC7u_3HHl-09s6Sc8qdQlfkCz9DMpC0aDuuznIqBFDTvUPMMwclrrw0xm_PuMzqViniTBLei3iUqFX16rqqy7J2M4RCSWRAu8HAU9ur11b8zJ24XBCvxLjdT1P1EJNkZNdgLbzAriBpgNuYiQdSaW9rhjFiVJ1IQxxVzQJqrJkb1hdZK8JOH1Qtj9nlsfndliyPoUBK_iHfVJaofSdcsunoKo3WEL852g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه برخورد پهپادشاهد ، به طور مستقیم به یک انبار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68154" target="_blank">📅 11:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68153">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hafYOvjm1eOj1FWsKpJS8XgfbGRccZ0B41cRwjNNl92hexsT_uBgG701Sg4yWieX1yajNIQrlmTYQ12PJ4oMj_KIWs0LCqj4WF-uBMOQlKRAjzOTrwHZdXLKGFz5i824_nwx16SDymkA3F6C7fKQGokApBkxgKjeWYa-7NMAtGIPwSDGbR7Q5EV4F5t_-FvcQGREBg8vuDQDHVZp4YJMOzw1WbdiOQNPFeBBfPyWsBwr-zh3WWepgWW1MofkqiWIr61VqE-MRc8-Q8O20sL3Dx0RNHj6TqltfJ9ysmkRxfkCYJuB3fc0srpfbJk64HhQ2YTyZ0vtIzMP6MBiVNQ55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:
#hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68153" target="_blank">📅 10:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68152">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=HIXR0dnSR2I7Cfm8gbK_llraoIyrZTRb-4i8T7hMo-x5ySPtOvuNAVIKqvPMexhuH_k0LXVG88JOfqGEIVodXtkS2gtIAAIBCugCyrFGQYgBfQ_xN35ie3eCW4S8NQhDmRdg2V5zLvaHiaWhsipQBfxAYeDn1_iqjselSW_nF6j0pxypF4OmQXd9oZsJWOW-P54PUvDE6_fwx3FHwXlVubQEcS9O-q6yIYMxNFPivuPKM-7WwtMcfWomMUFam6bm0BqwysOY3R8Gs_JfZ9sXwNEO7Ywq_43W1P0sygATFjy-LBm5p8XeuTxjZ9N2zQDHoPrVj_Om3EMCDwMEiUAVnr6_1oNlsFg3jaCTkS_uib8sl0PAD3BKs0LEWvytyHdj9YXKciUlBRy71LwAkggtf94myugIXng4N-6gxWGIaPm-szao88PkEVMYeM2m7z2XnJikyMYcjZleTXbOva4bEf-p2z-RVd8ln0dT3s-Eb9IyqWzg4DwNfYW4SvTnSF5ihYygrPwrFG_uE6YNoXDmVwxFwqVjAywO_xgIhdUg5n4naqjOSkFzMSwRAPNwqbzBgP0VxMWuo9xujrGl3ElqjGgdQgD7olUN0ZfzfsgBBCIJMs-Hbwlta0Q3lnPV3hX_8jlC16A1Tpor3v2zIEwpBxhP2f0RU-YMjKI0EX5CB60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=HIXR0dnSR2I7Cfm8gbK_llraoIyrZTRb-4i8T7hMo-x5ySPtOvuNAVIKqvPMexhuH_k0LXVG88JOfqGEIVodXtkS2gtIAAIBCugCyrFGQYgBfQ_xN35ie3eCW4S8NQhDmRdg2V5zLvaHiaWhsipQBfxAYeDn1_iqjselSW_nF6j0pxypF4OmQXd9oZsJWOW-P54PUvDE6_fwx3FHwXlVubQEcS9O-q6yIYMxNFPivuPKM-7WwtMcfWomMUFam6bm0BqwysOY3R8Gs_JfZ9sXwNEO7Ywq_43W1P0sygATFjy-LBm5p8XeuTxjZ9N2zQDHoPrVj_Om3EMCDwMEiUAVnr6_1oNlsFg3jaCTkS_uib8sl0PAD3BKs0LEWvytyHdj9YXKciUlBRy71LwAkggtf94myugIXng4N-6gxWGIaPm-szao88PkEVMYeM2m7z2XnJikyMYcjZleTXbOva4bEf-p2z-RVd8ln0dT3s-Eb9IyqWzg4DwNfYW4SvTnSF5ihYygrPwrFG_uE6YNoXDmVwxFwqVjAywO_xgIhdUg5n4naqjOSkFzMSwRAPNwqbzBgP0VxMWuo9xujrGl3ElqjGgdQgD7olUN0ZfzfsgBBCIJMs-Hbwlta0Q3lnPV3hX_8jlC16A1Tpor3v2zIEwpBxhP2f0RU-YMjKI0EX5CB60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوندها عُمر طولانی دارند و بیشتر از عمر متوسط ایرانیان زندگی می‌کنند:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68152" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68151">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1084df804.mp4?token=i3RTp0BtuWG-JnRzeXQcAfoanTiSaPlTgr4j2IogXlyB_YrK2XULdymb7JDJCbqkFWqPpBYu8l0TxnplwEQfZSzGg54JXfHm24qn_9i1tLkjm6zjUXXF_w5maaEgxu_m-39eRaIVejfh9wAryzdP5TPfHmhKS7UdSbeHEJz8S2_lselV8nD4aqU77WUzSb0S9b0T-J4tmp_lk05AmTHFVQdnr-eJbUCD6TXqOwvoxSrqujzaY_eblI9Hj2aDRa9oEH7CxMEu3TQyPmR4wSK94Eyss-TU0OFjbeY16WGUhAw4N4Hc1aqzfT_xoWp_De8lri7QdeNqHayEPeh4dyz9SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1084df804.mp4?token=i3RTp0BtuWG-JnRzeXQcAfoanTiSaPlTgr4j2IogXlyB_YrK2XULdymb7JDJCbqkFWqPpBYu8l0TxnplwEQfZSzGg54JXfHm24qn_9i1tLkjm6zjUXXF_w5maaEgxu_m-39eRaIVejfh9wAryzdP5TPfHmhKS7UdSbeHEJz8S2_lselV8nD4aqU77WUzSb0S9b0T-J4tmp_lk05AmTHFVQdnr-eJbUCD6TXqOwvoxSrqujzaY_eblI9Hj2aDRa9oEH7CxMEu3TQyPmR4wSK94Eyss-TU0OFjbeY16WGUhAw4N4Hc1aqzfT_xoWp_De8lri7QdeNqHayEPeh4dyz9SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیش‌بینی پروفسور جیانگ از تهاجم زمینی به ایران
:
پروفسور «جیانگ» تحلیل‌گر سیاسی مشهور در گفتگو با «پیرز مورگان»، مجری معروف انگلیسی، پیش‌بینی می‌کند که «نیروهای زمینی» آمریکایی از اوایل ماه دسامبر در ایران مستقر خواهند شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68151" target="_blank">📅 10:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68150">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XckDtsiGtTUQto-Rogrdam5DkJeUQRS4Xyti8ZIzOvrDACp9ZwfWmUeV7W_UQWnSUsBLAaMO0tKNdQLjA5l-oHMWD4SONSmUof95ctv7-ny1S5tOWSrdafj58oQjzP5z9UEyP_iVTFNg5Nvtvg3axsJ74ypXTnHNDYBfhM2PlunnJRDwwarJOti8Oyn1-FBBfTWMnaHuraGxaVtvIgn0HM92XSwUvEu780r7H9yHL8LSVqJyLQOHOQfVTMW-TutlSI2hjrQQ11JlIoHezYyPSXJLcNJcGG-FlzSnlm7glwIhKYuqv-0UF9RvXz5pfdzz4D-b0oaDWZnD-qzR9MkoSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ: کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.
کلنگ گزلا (یا کوه کلنگ) در استان اصفهان و در نزدیکی شهرستان نطنز واقع شده است.
روزنامه تلگراف پیشتر گزارش داده بود که تأسیسات تازه‌ای در مجاورت کارخانه هسته‌ای نطنز احداث شده است.
این مجموعه در عمق ۱۴۰ متری زمین و در دل کوهی به ارتفاع حدود ۱۶۰۰ متر، موسوم به کوه کلنگ گزلا یا همان کوه کلنگ قرار .
ارتفاع این کوه تقریباً دو برابر کوهی است که سایت هسته‌ای فردو در آن ساخته شده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68150" target="_blank">📅 09:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68149">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=NCqFi2yV9S7g9eYE4-57nJRNXGhifJMhwWcXxiZSNDLOevu9Z9p-Nf2d6_oeYu1nsEpiARa9lc-oPU9iue6iAydbdVUJqMuPpt824wE_TPzmPGh4KATQVczxBXR6cpl8T5yLQyPW4uwcVHaKp2YmP3190BtjHKPIEwP7hsfr6aFl8yfGMe5P3cgqkN53ODTLKoFZYT_4LoW74kxtHrlM1edETmBKZLp1bKK6mKreeaIJAImvLCQpFw2JlCfiV517207qFrQvsjToB7JZWmhu00DzhZkaeBxRWMLmeszSSv8YD6l-ttKPCIWCTT9wLiC6LO-1vwM_8CiMAPdF2ZqLcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=NCqFi2yV9S7g9eYE4-57nJRNXGhifJMhwWcXxiZSNDLOevu9Z9p-Nf2d6_oeYu1nsEpiARa9lc-oPU9iue6iAydbdVUJqMuPpt824wE_TPzmPGh4KATQVczxBXR6cpl8T5yLQyPW4uwcVHaKp2YmP3190BtjHKPIEwP7hsfr6aFl8yfGMe5P3cgqkN53ODTLKoFZYT_4LoW74kxtHrlM1edETmBKZLp1bKK6mKreeaIJAImvLCQpFw2JlCfiV517207qFrQvsjToB7JZWmhu00DzhZkaeBxRWMLmeszSSv8YD6l-ttKPCIWCTT9wLiC6LO-1vwM_8CiMAPdF2ZqLcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رسانه حال‌وش: شدت انفجار به قدری شدید بوده که در لحظه اول حداقل ۱۰ نفر کشته شده است  @News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68149" target="_blank">📅 03:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68148">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68148" target="_blank">📅 03:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68147">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68147" target="_blank">📅 03:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68146">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68146" target="_blank">📅 03:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68144">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=tVSK62kVAl3JAxAYtsgkZJOUQNGEs714xKnngdJD04yuyM_bZ2dR7BK-rlc-Gv2XAjQv9Mw4Fn_jB6Pz5-Y602PAV_5AKCZgYfCbrmRp5H7I_9JN2T0G3l_Nb57nud0mscfDqXeuTGF2h7a-Us4nG-h6kVNb0b4eIfJaKqi57-ROB2nfzgR7Wr3PGpbAKEJ4zRP5COmzy4mWMtNkPQZn55FQrdSwt7xT12fiGO-JLMwmNfw5lDD06iwrqHtEYw8OjBy14-ir8ABwvYm6dvgEavWHFloVBHFppY3bTlcLDJ9LZXAihmKnf5QXXHHIOZ526HiTGW1RF1B4tN83NSP66g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=tVSK62kVAl3JAxAYtsgkZJOUQNGEs714xKnngdJD04yuyM_bZ2dR7BK-rlc-Gv2XAjQv9Mw4Fn_jB6Pz5-Y602PAV_5AKCZgYfCbrmRp5H7I_9JN2T0G3l_Nb57nud0mscfDqXeuTGF2h7a-Us4nG-h6kVNb0b4eIfJaKqi57-ROB2nfzgR7Wr3PGpbAKEJ4zRP5COmzy4mWMtNkPQZn55FQrdSwt7xT12fiGO-JLMwmNfw5lDD06iwrqHtEYw8OjBy14-ir8ABwvYm6dvgEavWHFloVBHFppY3bTlcLDJ9LZXAihmKnf5QXXHHIOZ526HiTGW1RF1B4tN83NSP66g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68144" target="_blank">📅 02:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68143">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حرفای امشب ترامپ رو گوش کردم، یجا گفت فعلا نمی‌خوام باهاشون مذاکره کنم، تهش گفت اگه تا هفته بعد نیان برا مذاکره پل و نیروگاه‌هاشونو می‌زنیم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68143" target="_blank">📅 02:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68142">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">از تبریز دارن اردن رو می‌زنن، جالبه از پایتخت اردن تا مرز اسرائیل فقط ۵۰ کیلومتره، ببینید آخوندِ گنده‌گوز که ۵۰ ساله می‌گه اسرائیلو نابود می‌کنیم، امشب جرئت نداره ۵۰ کیلومتر موشکش رو اونور تر بزنه :))))
#hjAly‌</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68142" target="_blank">📅 02:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68141">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=U9fWYpOhdKEoV8LLAB_jrDJZFjW-PUYLbqKTEqTzfMKaJ-uAX2Q5Y7TGle6s_8EXv_oeLiWDGj-58oMPUYyJzdJbNeInOidU8zi5dqVyzTWzmbipqUKzuJC0pFq1J_Og7gVpduBn501ISnNQBi2ud3jZk6GMekOQsUMlDFyEMpiIFrxFz9pk1CRQJ938UybWXtfIBpGM0ePLIicfE5wODL6CYhHs38oTUEWqfs6VTn4ZUDFEScS6YPopWppy-sxKUSd6Ka5b8Rt0ED6uyqZqYH5c6a5PXEuycvxOz_-sTmdps4pImBZwXnSSXNBZzEwZGaYPbcmmOaj3rJHhGAv4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=U9fWYpOhdKEoV8LLAB_jrDJZFjW-PUYLbqKTEqTzfMKaJ-uAX2Q5Y7TGle6s_8EXv_oeLiWDGj-58oMPUYyJzdJbNeInOidU8zi5dqVyzTWzmbipqUKzuJC0pFq1J_Og7gVpduBn501ISnNQBi2ud3jZk6GMekOQsUMlDFyEMpiIFrxFz9pk1CRQJ938UybWXtfIBpGM0ePLIicfE5wODL6CYhHs38oTUEWqfs6VTn4ZUDFEScS6YPopWppy-sxKUSd6Ka5b8Rt0ED6uyqZqYH5c6a5PXEuycvxOz_-sTmdps4pImBZwXnSSXNBZzEwZGaYPbcmmOaj3rJHhGAv4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68141" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68140">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=aaRGCekMwjqezy6n04xyoXdU-5uBH4lhVh7-tory4dI-UNkGoKRv4hQCdIfI5NhcvqqqqfBgdD-dvSVyjZuOsXUL8YiNXcMrUWC5RVbFCmHq6fYztfw8FDpEHVaRfQBXE-fcyuxXoaELc-t0iPrWAAGyGn8DIQiPGywvmWTqZ1wLWDAS2xO1q5VFUEAqdsG5pEdTS0F173UT5DU-wDe3GMJ9MmvugNI95o0erCXsu6Sg9gikVCAUQ7UzpWzkRcZPMMEFdX5lTy8AIs34BKHHaDz9iXKJDIqhjt_azCuvGK12HCT7RMX1rKq2fdCHgC5NBDhtRp1JIb4KAIDRj5xIMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=aaRGCekMwjqezy6n04xyoXdU-5uBH4lhVh7-tory4dI-UNkGoKRv4hQCdIfI5NhcvqqqqfBgdD-dvSVyjZuOsXUL8YiNXcMrUWC5RVbFCmHq6fYztfw8FDpEHVaRfQBXE-fcyuxXoaELc-t0iPrWAAGyGn8DIQiPGywvmWTqZ1wLWDAS2xO1q5VFUEAqdsG5pEdTS0F173UT5DU-wDe3GMJ9MmvugNI95o0erCXsu6Sg9gikVCAUQ7UzpWzkRcZPMMEFdX5lTy8AIs34BKHHaDz9iXKJDIqhjt_azCuvGK12HCT7RMX1rKq2fdCHgC5NBDhtRp1JIb4KAIDRj5xIMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای دیگر از شلیک موشک‌های سپاه به سمت پایگاه های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68140" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68139">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=OZB5EphMn_S7aVJbMh0m0SYRN2E53VahSTs8s1zoKGIEQqzPhdR4JMrY74u0J1uZrBmfgRb8J3PnRWUkJEw5U9_461XOjEGdIWD6mvhS00k3tIZGPdSF52J4sp8yYYIHH79zGkYRbuXQMtDhMr9Iu2hFF5urhhhMt4-znZn848yS4NUOh6BgHpfnPtkcGmg31v6Z8-TEZTq1dt9zrB1VMdEuCFxQh9JTJnjs0bnRoQZihfE1PnIlAEci88HJa_XScSKYDr4LAcVm-YXGGutlLu7srZLlG1tRg3VKxEsRTXqDi6-fcJIDdEvL72w_vniHNEqZhnrZa9mTBtH_f6pTMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=OZB5EphMn_S7aVJbMh0m0SYRN2E53VahSTs8s1zoKGIEQqzPhdR4JMrY74u0J1uZrBmfgRb8J3PnRWUkJEw5U9_461XOjEGdIWD6mvhS00k3tIZGPdSF52J4sp8yYYIHH79zGkYRbuXQMtDhMr9Iu2hFF5urhhhMt4-znZn848yS4NUOh6BgHpfnPtkcGmg31v6Z8-TEZTq1dt9zrB1VMdEuCFxQh9JTJnjs0bnRoQZihfE1PnIlAEci88HJa_XScSKYDr4LAcVm-YXGGutlLu7srZLlG1tRg3VKxEsRTXqDi6-fcJIDdEvL72w_vniHNEqZhnrZa9mTBtH_f6pTMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68139" target="_blank">📅 02:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68138">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
💪
گزارش های اولیه از شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68138" target="_blank">📅 02:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68137">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682a3eeafc.mp4?token=TV9bjm-eQOYrAvcYOu3Rb0da-iJgETwNYOwgGpgNf5QYoXarc0REEFn0Q10EBkoe00FgRgi7fHHXecKQUhBWwS36YFdcOmo1PCSAVKYajcqQT3RlsyE3L2kmKkAKnOXVlu8iDoaVU4-CsF6Lbmg7NprvfMJL-P7-P9dSovLDUO8qnzd-4m60diTpFLLA8OUYPb8rtPwZGmOxDJLqgvKIwFaGlN6rjLLn7XWEuVvg_nqbg3aNf2vBmrwxIgsXmITisTKnSzEyfwQdJo2i2iLilsUvMcq-LhMeKpOZMlEwhpF_WyFDPEuTLt9GFd3xh80x693vvfN3ab9tLkVvGlWnNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682a3eeafc.mp4?token=TV9bjm-eQOYrAvcYOu3Rb0da-iJgETwNYOwgGpgNf5QYoXarc0REEFn0Q10EBkoe00FgRgi7fHHXecKQUhBWwS36YFdcOmo1PCSAVKYajcqQT3RlsyE3L2kmKkAKnOXVlu8iDoaVU4-CsF6Lbmg7NprvfMJL-P7-P9dSovLDUO8qnzd-4m60diTpFLLA8OUYPb8rtPwZGmOxDJLqgvKIwFaGlN6rjLLn7XWEuVvg_nqbg3aNf2vBmrwxIgsXmITisTKnSzEyfwQdJo2i2iLilsUvMcq-LhMeKpOZMlEwhpF_WyFDPEuTLt9GFd3xh80x693vvfN3ab9tLkVvGlWnNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا همچنان قصد دارید جزیره خارگ را تصرف کنید؟
⏺
ترامپ:
خب، نمی‌توانم چنین چیزی به شما بگویم، چون اگر بگویم حماقت است. اما کار جالبی می‌شد و کمی هم خبرساز می‌شد.
⏺
مجری:
آیا احتمال عملیات زمینی را رد می‌کنید؟
⏺
ترامپ:
می‌گویم نه؛ البته اگر شرایط اقتضا کند [رد نمی‌کنم]. گاهی اوقات به عملیات زمینی نیاز است، اما ما افراد دیگری را داریم که عملیات زمینی را برایمان انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68137" target="_blank">📅 02:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68136">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=RFoFrEsuiwi-m7Ti_dxPbVvpxI4rH2WlVIY6qgv96PvT0t5mJgApjz76bjc0PFbAmMO6JdOe_o78GJ48NoCmQAHfPiNjjvXW5iNWdcp8ogQvzI5pvsxVf1G_lb-_HLXXe_qiHYQoX7I_vowwy7s6WUDF4izDikBWvTY8dWOec1Us_NYlCKnWuRsrJKip3dvxaSoWfUoIWStGw8s7NPRcYSRLi6SM_S0TUIEr-pxW-3-g4k0Y9acWB_ZH51X9XiJH09yZR71uqVAQnMpTwSAtZGPYYfywuYBkUhfCuGy1Wmq4vjxLeGVg5d4JyyHgJ_ZMBQmKcbgoRcSP-wt-xaXRtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=RFoFrEsuiwi-m7Ti_dxPbVvpxI4rH2WlVIY6qgv96PvT0t5mJgApjz76bjc0PFbAmMO6JdOe_o78GJ48NoCmQAHfPiNjjvXW5iNWdcp8ogQvzI5pvsxVf1G_lb-_HLXXe_qiHYQoX7I_vowwy7s6WUDF4izDikBWvTY8dWOec1Us_NYlCKnWuRsrJKip3dvxaSoWfUoIWStGw8s7NPRcYSRLi6SM_S0TUIEr-pxW-3-g4k0Y9acWB_ZH51X9XiJH09yZR71uqVAQnMpTwSAtZGPYYfywuYBkUhfCuGy1Wmq4vjxLeGVg5d4JyyHgJ_ZMBQmKcbgoRcSP-wt-xaXRtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما در حال رصد «کوه پیک‌اکس» هستیم، چرا که گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کرده‌ایم. ما دوربین‌هایی در اختیار داریم که قادرند نام و نشان شناسایی افراد را حتی از فضا تشخیص دهند؛ این دوربین‌ها تمام بخش‌های «پیک‌اکس» را پوشش می‌دهند. اگر آن‌ها کوچک‌ترین حرکتی انجام دهند، ما بی‌درنگ وارد عمل شده و هر اقدامی که لازم باشد را انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68136" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68135">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f1669520.mp4?token=BqB_iTGIMSHXTLIx108o-o8lN859KkIGJtKsdL92VW0GK1hjUE6MFakgzr6JkI5YoX3LJklAk25OhgkmTZYtfaXq0ZuLLdeeD98HpJ54a3XAFxQMzvfyApVdgYk-HXd_93_Bp_6cApLwfIMqfWQDzbBJImoG9iKOniLAE3DGy-8T_j2uJzncpjnzQkbkusvrHzX2H_8jzMgZQPYx08fnShDHCjXJD_1AKX4RgQrhzcxyums7WYTE2drxUK_QXME7x226TgowZGPAkFb7St5F_Ajl1Va77Pp76wJ8CmnsToPh-l-tuTOxDjAhHgND2latb8jqc3hqPjdPD0mG1l7_Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f1669520.mp4?token=BqB_iTGIMSHXTLIx108o-o8lN859KkIGJtKsdL92VW0GK1hjUE6MFakgzr6JkI5YoX3LJklAk25OhgkmTZYtfaXq0ZuLLdeeD98HpJ54a3XAFxQMzvfyApVdgYk-HXd_93_Bp_6cApLwfIMqfWQDzbBJImoG9iKOniLAE3DGy-8T_j2uJzncpjnzQkbkusvrHzX2H_8jzMgZQPYx08fnShDHCjXJD_1AKX4RgQrhzcxyums7WYTE2drxUK_QXME7x226TgowZGPAkFb7St5F_Ajl1Va77Pp76wJ8CmnsToPh-l-tuTOxDjAhHgND2latb8jqc3hqPjdPD0mG1l7_Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
«۱۰ فروند کشتی روز دوشنبه از تنگهٔ هرمز عبور کردند — کمتر از ۱۰ درصد چیزی که معمولاً از این آبراههٔ حیاتی عبور می‌کند. وقتی می‌گویید «تنگه باز است»، منظورتان چیست؟»
⏺
ترامپ:
«اگر مردم بخواهند از آن عبور کنند، باز است. ما آن را برای ایران باز نمی‌کنیم… الان باز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68135" target="_blank">📅 02:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68134">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
مجری فاکس : آیا انجام یک عملیات زمینی محدود را منتفی می‌دانید؟
ترامپ : «نه. گاهی اوقات به عملیات زمینی نیاز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68134" target="_blank">📅 01:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68133">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbabff277a.mp4?token=sM5KE5Xo0OH0-_7tYrzAe5j7BhNBFqMQsOoY7JrhDteCNyjCAx1U29N_CA6ao4vaRoNM1MCZtOpN_4geGe1WrEz7Zt6-3HfvMisXv-au87d6XfeutOVjCQqZqzBsuiQJtF17PralL1Ene4uyCykv359e94Og6b3tv8iaVp14Nj880ZLDkoaHflg88rTsUl2EvqyiJsPodv1GRZt_kSgslVxEyyv3ncM2mCpSCIA8uZo-u_G1RbZTQUPNP40ERUR7aqQTVMWVoTI-2ZpHpxEZZ8MDsBycIRLlLlCeI7ujPG-QPPSgY197jZ08mTHPTRoBp4F-kJMSLKbqYVgCkMFeqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbabff277a.mp4?token=sM5KE5Xo0OH0-_7tYrzAe5j7BhNBFqMQsOoY7JrhDteCNyjCAx1U29N_CA6ao4vaRoNM1MCZtOpN_4geGe1WrEz7Zt6-3HfvMisXv-au87d6XfeutOVjCQqZqzBsuiQJtF17PralL1Ene4uyCykv359e94Og6b3tv8iaVp14Nj880ZLDkoaHflg88rTsUl2EvqyiJsPodv1GRZt_kSgslVxEyyv3ncM2mCpSCIA8uZo-u_G1RbZTQUPNP40ERUR7aqQTVMWVoTI-2ZpHpxEZZ8MDsBycIRLlLlCeI7ujPG-QPPSgY197jZ08mTHPTRoBp4F-kJMSLKbqYVgCkMFeqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا اطلاعات خاصی وجود داشت که باعث شد تصمیم به آغاز این عملیات بگیرید؟
⏺
ترامپ:
ما می‌دانستیم که آن‌ها خواهان سلاح هسته‌ای هستند.
⏺
خبرنگار:
آن‌ها می‌گفتند که خواهان سلاح هسته‌ای نیستند.
🔴
ترامپ:
هر چه می‌گویند دروغ است. آن‌ها دروغ می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68133" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68132">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f31387d.mp4?token=kR7juB6ktstEdEueEJVjjIBgIqUS19Te0HurIYXtkfPq7KUi5zF3LbhVl-i2X0pY79XJCJO5Ft8gcyoLFKoYclG8hKBjRymCyKwjpRM10puehtvGTKh8uf5rJ32gQm7FJeJyRXeoMRENirq_7NcZAfviZ2ixsDDeQlu8rTR6b0hYY893DlC1jW7ppPynyMTmxXr2TcvcHd_SQ35ePuTKq5PyTJoBGTsnPMq-LVe1l2p00Ye4tMHcjeE2kF_xQTLs1vuFifJNwlDP5oS1v5WMw7qkmmTW1v1m2z5CQlLjEaKoPTebiZ9w7DzQB8v0g70q-D6JlZFUEW8NPVIioBKWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f31387d.mp4?token=kR7juB6ktstEdEueEJVjjIBgIqUS19Te0HurIYXtkfPq7KUi5zF3LbhVl-i2X0pY79XJCJO5Ft8gcyoLFKoYclG8hKBjRymCyKwjpRM10puehtvGTKh8uf5rJ32gQm7FJeJyRXeoMRENirq_7NcZAfviZ2ixsDDeQlu8rTR6b0hYY893DlC1jW7ppPynyMTmxXr2TcvcHd_SQ35ePuTKq5PyTJoBGTsnPMq-LVe1l2p00Ye4tMHcjeE2kF_xQTLs1vuFifJNwlDP5oS1v5WMw7qkmmTW1v1m2z5CQlLjEaKoPTebiZ9w7DzQB8v0g70q-D6JlZFUEW8NPVIioBKWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«همان‌طور که می‌دانید، ما پیش‌تر دو بار به جزیره خارگ حمله کرده‌ایم... اما در مورد تصرف آن، اگر بتوانیم توان آن‌ها را به اندازه‌ای کافی و عمیق تضعیف کنیم، این کار را انجام خواهم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68132" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68131">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
حملات به ایران ادامه خواهند داشت تا زمانی که من بگویم کافیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68131" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68130">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f264ca5d25.mp4?token=rBHwfxZEpLUMmavM3TBvPsIfIh7-kL66EdawMLaJZeVigrDrfQccE7Z-a-aNkO3qlBKTbYl7WCfVvpUmByqd_kRZx4hPGKWxQ1Q2LfY8PYOBgauvHeXeqmhaJCjayX2dCEqvfa1Z-LFhE0upXcvn0u4ko4BC-HPzw_t3AK2UO3CQUiMLoYeZlR6S2ZJacAkwkSNm-AXTFghqq-jKKObAlIPC-am7H64B2-rjiZpGqHVTSxmf_Fku14-1MlmoBQfMeOEDcBp6UMycGd6pedEbBkEXQds-dH3P738iZpKafFGJ6TgHjKzhjBJ5nka2TFgYz1c3Rg6H1_oCuhWot23aAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f264ca5d25.mp4?token=rBHwfxZEpLUMmavM3TBvPsIfIh7-kL66EdawMLaJZeVigrDrfQccE7Z-a-aNkO3qlBKTbYl7WCfVvpUmByqd_kRZx4hPGKWxQ1Q2LfY8PYOBgauvHeXeqmhaJCjayX2dCEqvfa1Z-LFhE0upXcvn0u4ko4BC-HPzw_t3AK2UO3CQUiMLoYeZlR6S2ZJacAkwkSNm-AXTFghqq-jKKObAlIPC-am7H64B2-rjiZpGqHVTSxmf_Fku14-1MlmoBQfMeOEDcBp6UMycGd6pedEbBkEXQds-dH3P738iZpKafFGJ6TgHjKzhjBJ5nka2TFgYz1c3Rg6H1_oCuhWot23aAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«در نهایت، اهداف حوزه انرژی در ایران را هدف قرار خواهیم داد. نوبت به پل‌ها می‌رسد؛ هفته آینده سراغ آن‌ها می‌رویم. ما تمام نیروگاه‌هایشان را از کار خواهیم انداخت. تمام پل‌هایشان را نابود خواهیم کرد، مگر اینکه پای میز مذاکره بیایند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68130" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68129">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36032be115.mp4?token=hS3sAn2km4iPx_Uv7S9ksaU5-d20fzLaQI83AFl1Hk6aKwYNzgWYtNkecsJLKG7sLv2c_K4ZHhmvC5pnnXAB7A2McrMywuiFe39Vwln81YutzbmZvTGa-nw2EiHtY2OSx1BNIWb7xY4h7W4K9G2U783XM_OqZLrBwPFVK1czk1WTnJnm0rfXwv53ta7_V5Imj3N313JfBX0SvGB1PrFL1v3GtD35oZrWgOwCV0g2OHwbNGmiR9suZfFCsx8WKDsQAQsUVL8V5g5iovdF-KhuJkA0B-xYfAVNZmDzBcN_t7RFy1ltA4pGv2JEtxy3Q9iZLMxejFvvW39OrRnS-2tzMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36032be115.mp4?token=hS3sAn2km4iPx_Uv7S9ksaU5-d20fzLaQI83AFl1Hk6aKwYNzgWYtNkecsJLKG7sLv2c_K4ZHhmvC5pnnXAB7A2McrMywuiFe39Vwln81YutzbmZvTGa-nw2EiHtY2OSx1BNIWb7xY4h7W4K9G2U783XM_OqZLrBwPFVK1czk1WTnJnm0rfXwv53ta7_V5Imj3N313JfBX0SvGB1PrFL1v3GtD35oZrWgOwCV0g2OHwbNGmiR9suZfFCsx8WKDsQAQsUVL8V5g5iovdF-KhuJkA0B-xYfAVNZmDzBcN_t7RFy1ltA4pGv2JEtxy3Q9iZLMxejFvvW39OrRnS-2tzMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا جنگ با ایران از سر گرفته شده است؟
⏺
ترامپ:
خب، گمان می‌کنم بتوانید هر طور که می‌خواهید آن را تعریف کنید، اما قطعاً ما داریم ضربات بسیار سختی به آن‌ها وارد می‌کنیم. آن‌ها باید ضربه بخورند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68129" target="_blank">📅 01:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68128">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=nhW04mqICzJljz8XRtXUAcg56qvRLIsugnbK0-Z8Mh5RFjm8yZN1Qgm7P_xdJ7veg_6Q6MwB-MSAL-isPHvK2wLAOjUWYcVhWo91myM0AdMQBEBAUoflMQKisg_X5f1fbWQSVQ3Xa8YWcJ5HeOlV4LODfqXqkS0UPlrKuAadkXCelpQlVjtkhSzaWDXo2lZN8nsk-eta1HQtILv5vc9uJ5GL7_R1HnUJCKoZfuQkP82a2mN6tgLvHUJ5xo5Yf5fSqtBZ7koJxQ_H5MvGJeyo1FrwtSuF7Nkj9VmA8U8XlIzFNTmEyHZXaP-4CsZtsDWW2UU70_7nvO8sPCiciqOMsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=nhW04mqICzJljz8XRtXUAcg56qvRLIsugnbK0-Z8Mh5RFjm8yZN1Qgm7P_xdJ7veg_6Q6MwB-MSAL-isPHvK2wLAOjUWYcVhWo91myM0AdMQBEBAUoflMQKisg_X5f1fbWQSVQ3Xa8YWcJ5HeOlV4LODfqXqkS0UPlrKuAadkXCelpQlVjtkhSzaWDXo2lZN8nsk-eta1HQtILv5vc9uJ5GL7_R1HnUJCKoZfuQkP82a2mN6tgLvHUJ5xo5Yf5fSqtBZ7koJxQ_H5MvGJeyo1FrwtSuF7Nkj9VmA8U8XlIzFNTmEyHZXaP-4CsZtsDWW2UU70_7nvO8sPCiciqOMsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‏ارتش جمهوری اسلامی:
در مرحله هفتم عملیات «صاعقه» محل استقرار جنگنده‌های اف ۱۸ و سایت نگهداری تجهیزات ارتش آمریکا در پایگاه الازرق اردن را هدف حملات قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68128" target="_blank">📅 01:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68127">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
حمله به جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68127" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68126">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
بندرعباس و سیریک بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68126" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68125">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=tg9qbEeSTetqvn-v2j_EBfX26VeLAqnhGQy7PCqeRe3PN1GMoUlplWJD6qWX1reXgYouN774Xqu21keHTkl-YpNO0dLel8cG5hrqqcDUo_g11mGOl5WuQl-cC8Nx4DEvWxqgW8fnWdtPLmpAZeJkpgTsX1LO-B0qsEEpcPeAiX_m-ZuWAg7EyPqynwVo_80WbFK5J2y5PM3eCTf7rDyvlvpNJsCIWICx2whFQ0BmPuC1esVZs3e9Tz1Vn3xvUbpODlCkyqn8nuF9fUI5HbvhOsAHWT2W8uawW9Rvjhu_10qGnI92v7j5G4j27ZI7dfklkPgj3pS2i9jE5NXvTaQw5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=tg9qbEeSTetqvn-v2j_EBfX26VeLAqnhGQy7PCqeRe3PN1GMoUlplWJD6qWX1reXgYouN774Xqu21keHTkl-YpNO0dLel8cG5hrqqcDUo_g11mGOl5WuQl-cC8Nx4DEvWxqgW8fnWdtPLmpAZeJkpgTsX1LO-B0qsEEpcPeAiX_m-ZuWAg7EyPqynwVo_80WbFK5J2y5PM3eCTf7rDyvlvpNJsCIWICx2whFQ0BmPuC1esVZs3e9Tz1Vn3xvUbpODlCkyqn8nuF9fUI5HbvhOsAHWT2W8uawW9Rvjhu_10qGnI92v7j5G4j27ZI7dfklkPgj3pS2i9jE5NXvTaQw5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
هم‌اکنون دارلین گراهام نوردون، خواهر لیندسی گراهام، در حال ادای سوگند برای گرفتن جای برادرش به عنوان سناتور کارولینای جنوبی است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68125" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68124">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.  @News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68124" target="_blank">📅 00:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68123">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
انفجار چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68123" target="_blank">📅 00:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68122">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hN_dVcv4-aAiL0--pcvtckP5i15jSOBNRnMy24uDtGxbfHCHvpZerkWFMkY7g3QR6Ge_yGisPhZLfnGM7Q0V-RArdAUYFCLmXonAO0pjbA3Ao0NKCkbwQQzxNwTvO9-aAdFYt3OTw9t3BhF6pmTpV-T9xyMVJEM-FY1KqyVNrOXdpQwU3LTRGifAm13FlIfW14vp26ag2tHun7unqKSHOHBcBbezZJwoGn_aMWnjAUsMgqZnToBWZo5T8qK1rv6fNOhBDygzc91g6M65hdM4ZmupVIjePkXG7YK-aqZulPxu8VbcwUCLXmZCoaSSOK_rQB1tTpWRIcIAwr9RGV_usg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68122" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68121">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=csLT-lAf5AdC5rnpithtiRmA7QGlhnt_h-y850IXV7I0htL8eqEctrnTH8EHCk6iHNynPfqiKHJmP0J-rhkO-8LrJo30GOBoRDTDfsSSvOC-PPYzDwZJXWAnPBgbyBoFMUOEKobHFWY20qpoSNm8lWX77FYXwCrGU9N7xp7RhXdYxtiYIxuJM5bNepNhg7Bg8T5Nu53RlmtZusKAALq28n9MNaz7cwPt5-Fxwd25E-RM7hCYyJxKtKQu0ZyKSGadPOzMsKWUKYabAsD5ieZmrqklVkvulF5RjG4dipAHnKKR7E4sTb3mFGcsXK0ne3trbLK9G9WeyMNBeYwxzOQ6Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=csLT-lAf5AdC5rnpithtiRmA7QGlhnt_h-y850IXV7I0htL8eqEctrnTH8EHCk6iHNynPfqiKHJmP0J-rhkO-8LrJo30GOBoRDTDfsSSvOC-PPYzDwZJXWAnPBgbyBoFMUOEKobHFWY20qpoSNm8lWX77FYXwCrGU9N7xp7RhXdYxtiYIxuJM5bNepNhg7Bg8T5Nu53RlmtZusKAALq28n9MNaz7cwPt5-Fxwd25E-RM7hCYyJxKtKQu0ZyKSGadPOzMsKWUKYabAsD5ieZmrqklVkvulF5RjG4dipAHnKKR7E4sTb3mFGcsXK0ne3trbLK9G9WeyMNBeYwxzOQ6Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران تنها جاییه که بتمن هم به گا میره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68121" target="_blank">📅 00:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68120">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0UOYpvfXwZTXxk4wtKn7EQ1Kl649C8HBIK3y8toYPW3Zy51a32v6wyQ0kjt4xfYAX0cybrjdslqp6W69PiHUZLbndlQy5mucmU3gG63NWYmEN_JVzM1FO9C3-SJsPHDytLvIyZeTCSa2_fr-Y4TBEgFP10eI4NQaUPuKDmk8ALVTQ_mR0_w8bEGWLrRcICUDFzhWcIl2dd9H2ajghehzKNwEa1JYsQO-kjH5ONSKbJiCpL2-mHJ1x9kzjMpLFLv88NoE4FP-sRirfqr4pRxq3j9QD3mEI33FHvVUHc3DrzxE-P_o1rjPVA2F8FDuWjrv4HPvvL__8TCfgCWrKG2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده امروز ساعت ۱۶:۰۰ به وقت شرقی، محاصره دریایی شناورهایی را که به مقصد بنادر و مناطق ساحلی ایران و یا از مبدأ آن‌ها در تردد بودند، از سر گرفتند. در حال حاضر، بیش از ۲۰ فروند ناو جنگی نیروی دریایی ایالات متحده و صدها فروند هواپیمای نظامی در سراسر خاورمیانه مشغول فعالیت هستند. نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68120" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68119">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68119" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68118">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c993da0a01.mp4?token=GzYB4BUgUxwXilwpN70m2gieh1K585vPdcTGBIXIqsNFPP-snRIQxBHuGt7x64GVc4hvNHzzdgFmZzCDpaPYgmvHeNUCbwUkfMMF_LzBkvroQnZ2YoWd80J4gbi3XQw7kxpqsHFBRwRynlK_cOFXjvOHQo1cwo__072fTxroEHafeb-cTKnb72bV1tRuK1dhxS61r1gIXryne8RkMl2waxaP7ubHIhEZqu3RMbrtiZfi6CHRVrwQkKgULWnevqV9c0wm-iZojrq0f35Ab9PQI_igHt9azDpNHNgnPh8IebhaSPHBHreE-z4bXOmsQryAKa8BdxPlkeGqu1ArNIAZvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c993da0a01.mp4?token=GzYB4BUgUxwXilwpN70m2gieh1K585vPdcTGBIXIqsNFPP-snRIQxBHuGt7x64GVc4hvNHzzdgFmZzCDpaPYgmvHeNUCbwUkfMMF_LzBkvroQnZ2YoWd80J4gbi3XQw7kxpqsHFBRwRynlK_cOFXjvOHQo1cwo__072fTxroEHafeb-cTKnb72bV1tRuK1dhxS61r1gIXryne8RkMl2waxaP7ubHIhEZqu3RMbrtiZfi6CHRVrwQkKgULWnevqV9c0wm-iZojrq0f35Ab9PQI_igHt9azDpNHNgnPh8IebhaSPHBHreE-z4bXOmsQryAKa8BdxPlkeGqu1ArNIAZvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
علی خامنه‌ای، (19 دی 1404):
ترامپ که با نخوت و غرور نشسته آنجا راجع به همه‌ی دنیا قضاوت میکند بداند که مستبدین و مستکبران عالم، از قبیل فرعون و نمرود وقتی که در اوج غرور بودند سرنگون شدند، این هم سرنگون خواهد شد.
⏺
🇺🇸
دونالد ترامپ، (10 اسفند 1404):
آیت‌الله خامنه‌ای ایز دد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68118" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68117">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
⭕️
محاصره دریایی علیه ایران آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68117" target="_blank">📅 23:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68114">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fNk5roI5ZB8NCh8FupYB3rTwCpV5esiJXHqL_9bZinKJkmuVKY6uXJKr1XGQws8beZepeakYemuuiJe6ADUt9xrznX_CHIoevdGdwj0zqoAEdBQzNvhCww6m10C3BnYNaHLp10MFtTs1Ake2UCuqXAAWvtQW9eALJfPHklniwqSjyuDRmF3F2SRJZmS0KXwnNAEbWGzDeNHUnET4GCpDCDbpCe5abgoevsJUmVgZvIrQK-wdW0tItwM6fNrRQmtazIv7EYjR7zzLEEeWAYYH0XQDgyYsVienJ6yIBw-lXc8AFJhla-SA_MEeljCr4zT-S0Onn4P_snqLjGiNkwDxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4WEuZtBLmRdgXq7dHTTtMyjL4catzoLBQhmYMqausfa5Vg8Dk4oNUUOcM7DRhuvcCKZmVOfw5ewIOpzLwTWa_H9qAWjmAsKc-n4QaiaSrbm9WfH9HAc5v6M5Okg62UF8kuzpSeybZPa4GMQ264xWdgl1tQAMyz4wd1dztvpIEvVSliazlbiNSjeukn---RC6_dpkoQ5qIxmODDI2gLcADBW-6cJFKXwFVyYC0Quy7-KCZuvdAmectqvGPFhvigZBjj5qkHNI_yE905ZetAYJuYOYZif825Kn1nXl7ba2MQ4SOTzlJ8Q2NwtdhfvgdspnafNCg-D6xXKBOoy1NJYag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تازه می‌خواستیم نودای نیلی افشارم بزاریم، پس هر وقت بابای مانی لفت داد می‌ذاریم #hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68114" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68113">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
سیریک بیش از ده انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68113" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68112">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
انفجارهای جدید در خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68112" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68111">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
‼️
تصاویر جدید سپاه از حملات موشکی‌ش
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68111" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68110">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ماشالاااا اسپانیاااا، اینا بیان فینال مسی راحت تر قهرمان می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68110" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68109">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68109" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68108">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68108" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68107">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68107" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68106">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMani</strong></div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68106" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68104">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⁪⁬⁮⁮⁮⁮⁪⁬⁮⁮⁮⁪⁬⁮⁮ᴹᴬᶻᵞᴬᴿ</strong></div>
<div class="tg-text">مرسی که تک خور نبودی
💙</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68104" target="_blank">📅 22:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68103">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-41OUArSgi1eNzOMkN2QIoA4eO55Q7cSALzoGNGa2Rz2lgEsEYkvVPHFNo2FseyLfCWo2NjGlZ_SGHnSUQacAnopLzfRKk0PStWQdpOPkzcXHQjMujbCReGTYua6YXOxG8C4cdD36prcmcqPwsX9DPTD58juO2ysM123AQCZ_-C2qkKtOkQNPQz3t3xdl2dHho-hBz0ZRfIebyqyk5Mi9m_HxuFgXlrlX195zpnjfgspT1SfS_ZAeqW0M0WEll75PGe9nBLMXz6_Uj2bYfh0s96_6owum5t8SeeizbmXWvxQ4Lp3RVKT6bne0I1xNpAjPbmIFS9hn1sRK6TnGdneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68103" target="_blank">📅 22:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68102">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⏺
رسانه‌های حکومتی:
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68102" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68100">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nLTqShhHLZ8Jkd5aaiI90rTPA2gbZ-QWwFPszQvHh8pldXVjKuCPi6jJe2BxGWW5yLxLm7tYegr7s41CO13kyXd9hpFkLuJgckhrn---NH6zO7KSD4O2L1xt6uYMM0FC0zkQ2aXeXdRJqe1w0BmQvn6uSKQ6tHbflIaor6Y2jYpQtlugNSAlz0CLtxMAiemg30Lqt1zyxT9V9SA2zgJOGmE3bfJNxO3aajdKa1zpW9MWPaWBeQyWMlcJeLjeMZ--Jq_YcNlQTzXY0Jrzqqu7NptPL3iACQ-u9ZL_CXzbfNoOrv_7cNl2_vnpQs0RAetbmFrkcfkurtKr_x7vUK_1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJGIzUPDI4uzVl82N8vJgUtblxmxqJi2pBEVlazfYqX5hLK3Cv0S9bQSgOqIxX1UkK_XeSIFi7RstnPyqXrzULj8dcZ7yIn_aI6xRzDQgAsiH4rxui1wDdj8_zVh4kFg4u2svCAmcZ51dGgWskGGtKnV21VpHyuftyC6uFW52f-sK9uEf98XlZOzzD4VZwH7cS285fyVnQmhfotldlLREYUhp7iff_0SNVtr6j4gKCSMF9_4MinKUwp9a7SKLJmZo4T-xr7t7T3bE1nSEyUoftOsiaNXLNTR8nYvoiErX4JQwpBlAITLsn0N3B7jeDFxLs0e2Xmwc038YMVydMg74w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68100" target="_blank">📅 21:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68099">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kx4KrgbEO4LeaMtVdlKnmWEBBJ0eqHhFdv4Y_PFqJ-ke1Ht8zBu3alA0MGmxsRBHtwyF1CVusjhrtrth3qqS3KKXZJ9DXaNUzEM9A35NT0uTVMJ1RUA68JqadRpeGfkjuUHeJm1pyIESuvc6aT7cs_tqvfsc7aTvPBppJzquXCC4ZPoGbOZU2Tfb18iygXOlX5ObY1nlYKTF-K5S4U_ctSO6yOSuCed_P7UdzxEY6B1KSAFSEXTkw42GZMZ23Kv_n5_vYIxN389x7okjD3VccQqEPlbjP5gtlZGYty3NWjLn1eAfpDXip56VV7ihhT0W8rXsYCGkgzs4TeaKzRRqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پزشکیان:
‏در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است. امروز نیز مردم نجیب این دیار با صبوری، ایستادگی و پایمردی، روزهای سخت ناشی از تجاوز دشمن را با عزت پشت سر می‌گذارند. در کنار و قدردان این مردم وفادار و مقاوم هستم.
همه جای ایران، سرای من است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68099" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68098">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bonq4xEdgZK0QiQJ4fi9mDtPOqlAdBz_SgT-HY4eD7WXHGEiJMN_KDcFgtjCF602FZmwOelpscXHtfqT84ifXyb8PfixAnAZcrHcR6WjwNz_s2jzP-cXSON96ryff27exauua4tVojP5_N5C8xM8V9HhSu_8y9hG92e9RVfO6zAhbWc80lU9eY9xZR2wD3cdyO1DmW5eEdBjn_KoQuQ8BezHw5doiNFh1H-Urv1WFvfxatUrFYqbdbyof2oq1Q13yKWZ4fsyE6-qpRAev-DH0ZZ0X10SyLTKuBV1uQ-hg-rMmAhKh53ETSTkTY3jpggT-Mosmp12HKuwy9edZOBtaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68098" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68097">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=FoyT7MB_9xRnijHaqNh1RK0UFd4_6-nYs35T0f-_BtPm9rd71Z7BKG5H5YLwXKq2l_SeAwSlqwBenny9S6hUb2nVCzA9hnCTHUaqulXhhFrkz8axoytO-yOtOmArDOUXwSKG4Q5rKO16wjiGMnTFdg8yAHyWTytIGjgcdONmlgkKfzMhZZ7PYzrjOLoQIDKocAG8ZSvk0La1rKCgzXi-U_d_icTz88Zpc9IWawAsTr_2_dgWYMQCSsD9im0dIxyYhV8F1INy08i-A2W82Fd6EFc7u_qYppRhzMfoFha3nwcsw77VWpZZyH9X1BKMvx1sUdsLWkOEJm2_vaQj_9ZHbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=FoyT7MB_9xRnijHaqNh1RK0UFd4_6-nYs35T0f-_BtPm9rd71Z7BKG5H5YLwXKq2l_SeAwSlqwBenny9S6hUb2nVCzA9hnCTHUaqulXhhFrkz8axoytO-yOtOmArDOUXwSKG4Q5rKO16wjiGMnTFdg8yAHyWTytIGjgcdONmlgkKfzMhZZ7PYzrjOLoQIDKocAG8ZSvk0La1rKCgzXi-U_d_icTz88Zpc9IWawAsTr_2_dgWYMQCSsD9im0dIxyYhV8F1INy08i-A2W82Fd6EFc7u_qYppRhzMfoFha3nwcsw77VWpZZyH9X1BKMvx1sUdsLWkOEJm2_vaQj_9ZHbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
👈
مهمات خوشه ای شلیک شده توسط سپاه در آسمان بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68097" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68096">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سپاه پاسداران به بحرین و کویت حملات موشکی و پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68096" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68095">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68095" target="_blank">📅 21:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68094">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=egOzS90JSZqdpBpgDDlJcb4nLqO0gzWwx7wtd1TXjJn0_0JY8YrPnvTPWWGLsgQokqd-3NmVps-1x7Bo0G_qI41KERxkNSQ7rZRofmZcBC8lEJuavDoHgk_869PBM9QjEoUAc3v2YMp9q0lutcMWfeGtIuGz8ONDCJxG5UakbWXxyYepfDE8shaWWMOaJr1rbpWmsqZG8Wn8jzadsywXFjSiycRPsQlM0TPk23CiKJ1EVLnHAEi-Ym0-cGxk_qYdDewpqrEzSnmnhbd6YpskUXSjSNsOof_FEIOVHhNQL4PzBFq8Vs70sgyH0YINAfvBNsr2hUYC3wGWu7bMlFw56Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=egOzS90JSZqdpBpgDDlJcb4nLqO0gzWwx7wtd1TXjJn0_0JY8YrPnvTPWWGLsgQokqd-3NmVps-1x7Bo0G_qI41KERxkNSQ7rZRofmZcBC8lEJuavDoHgk_869PBM9QjEoUAc3v2YMp9q0lutcMWfeGtIuGz8ONDCJxG5UakbWXxyYepfDE8shaWWMOaJr1rbpWmsqZG8Wn8jzadsywXFjSiycRPsQlM0TPk23CiKJ1EVLnHAEi-Ym0-cGxk_qYdDewpqrEzSnmnhbd6YpskUXSjSNsOof_FEIOVHhNQL4PzBFq8Vs70sgyH0YINAfvBNsr2hUYC3wGWu7bMlFw56Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سر دادن شعار مرگ بر سازشگر در مصلی تهران
صداوسیما هم چندین بار صدا رو قطع کرد
🤣
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68094" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68093">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=sAYM3XdO80O26wro1-4YSwhQAwpCK05Rd35IA0pvddQQhHfVYr5vJgondb7vvf2I7NEuxI9tG_K55RxKLDdX8fntkpg757Kq8mvpCMGhZuJYVg31fmrCUJlNrmoQfxHERmGPPExs5gwatzqaVTqGWzeBp1zGqM4jeCFLg15iYoWLiVeM_Go0Y1d-2XPJecl8tN1BLfmOtiQE3s7qbi_Lmj_8bPQe1dxPdADZJafcAG_43sWGsNBlVv0YG4La1nPa04N-IRbz3lxnt3f4xtgkc-6X8BeesLQ30fTVhYy3QDppFJ0hsU738YTIAFNM84-XFOmfLoomck0sjADimoMrNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=sAYM3XdO80O26wro1-4YSwhQAwpCK05Rd35IA0pvddQQhHfVYr5vJgondb7vvf2I7NEuxI9tG_K55RxKLDdX8fntkpg757Kq8mvpCMGhZuJYVg31fmrCUJlNrmoQfxHERmGPPExs5gwatzqaVTqGWzeBp1zGqM4jeCFLg15iYoWLiVeM_Go0Y1d-2XPJecl8tN1BLfmOtiQE3s7qbi_Lmj_8bPQe1dxPdADZJafcAG_43sWGsNBlVv0YG4La1nPa04N-IRbz3lxnt3f4xtgkc-6X8BeesLQ30fTVhYy3QDppFJ0hsU738YTIAFNM84-XFOmfLoomck0sjADimoMrNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب ترامپ درباره تحقیقات اف‌بی‌آی درباره مرگ لیندسی گراهام
⏺
خبرنگار:
«آیا می‌دانید چرا اف‌بی‌آی در حال بررسی مرگ سناتور گراهام است؟»
⏺
ترامپ:
«نمی‌دانم چرا، چون فکر می‌کنم او مشکلی داشته... من شرارت زیادی در آن نمی‌بینم. می‌دانم که انواع و اقسام تئوری‌های توطئه وجود دارد. فکر می‌کنم اف‌بی‌آی وقتش را تلف می‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68093" target="_blank">📅 19:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68092">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=T8SW8Z0JMc-bDfVNxMDkY--H4bN3DzwMnXM32a9FVo1UdhKIAfLo_Q32rqQUw9nAQ3d4HshhcfUP1UA9JiUMN7gceGOMPT0hxpZUpp1Zkj-IMxvhElNrXMavYyFEa2naWfcexk3QvSIcdVRZV0URsiwWOzUlD3IReGlUAx-kJ_lFy_EBCWqr4G0dBEWxs5ql4NhI7wkESfTHir-A_OeRFQzeZktnrENRLQjir5c2QjFZBNiPhx19GYXlDhfyKsM3wnt6uK3D4OCnZGeO85TYLTCKxpzK9BifmIP5x6DLmd6z9fJjrmxWEeZhhLAlwVX1PREXYM-dDathnwFOp7NObw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=T8SW8Z0JMc-bDfVNxMDkY--H4bN3DzwMnXM32a9FVo1UdhKIAfLo_Q32rqQUw9nAQ3d4HshhcfUP1UA9JiUMN7gceGOMPT0hxpZUpp1Zkj-IMxvhElNrXMavYyFEa2naWfcexk3QvSIcdVRZV0URsiwWOzUlD3IReGlUAx-kJ_lFy_EBCWqr4G0dBEWxs5ql4NhI7wkESfTHir-A_OeRFQzeZktnrENRLQjir5c2QjFZBNiPhx19GYXlDhfyKsM3wnt6uK3D4OCnZGeO85TYLTCKxpzK9BifmIP5x6DLmd6z9fJjrmxWEeZhhLAlwVX1PREXYM-dDathnwFOp7NObw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره لغو عوارض گرفتن از تنگه هرمز
:
«آنها (کشورهای عربی)گفتند: "ما ترجیح می‌دهیم سرمایه‌گذاری کنیم تا عوارض پرداخت کنیم." و من این را دوست دارم چون هیچ‌کس نباید بتواند برای تنگه عوارض دریافت کند.
«در مقابل این سرمایه‌گذاری، کشورهای حوزه خلیج‌فارس مبلغ بسیار زیادی در آمریکا سرمایه‌گذاری خواهند کرد. این در واقع خیلی بهتر است!»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68092" target="_blank">📅 19:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68091">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
شنیدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68091" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68090">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTvengPI1HVZl_KfDv7pBm8AmgUI-R2b4i7tAbDh2pzulPNQwZksN0SqVk5oTBL152_H-8jXMty9fpQ4796-2OjhnOyLl0JlPCzJ8rcw1N8UaTlnueOUJzYNOvNDrx0qSlRT9Os6UUPnfYpL6uIkHe1tID9ExqKf5mVjmRdHsBDj3vAlBTCMXw9bE5T9qn3X1UpXLyFPDEjWvzu0QrS1BFx1KIwCyDGfI2F1-0bShx3AP3Cpa9p4KpftLjDkK2R56Mtcvf5J3O38XdMas5QbJ_YeceK9m-k74XfY-0VBFT6S0xqIO1sRwGLr_Y4M5Usn4VxBjuJpCGULNPp1WsMM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
به لطف قدرت فوق‌العاده ارتش ایالات متحده، نفت بیش از هر زمان دیگری در جریان است. درود ویژه می‌فرستم به وزیر دفاع، پیت هگسث؛ رئیس ستاد مشترک ارتش، دن کین؛ و فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، دریاسالار برد کوپر. به واسطه تلاش‌های آن‌ها و تمامی اعضای قدرتمندترین ارتش جهان — که بی‌رقیب است — تنگه هرمز برای تردد تمامی کشتی‌ها باز است، مگر برای ایران؛ و این استثنا به دلیل رهبری دروغگو، خشن و بدخواه ایران است که کشورشان را به سوی نابودی کامل سوق می‌دهد. بنابراین، ما یک محاصره کامل اعمال خواهیم کرد، اما تنها برای کشتی‌هایی که به بنادر ایران می‌آیند یا از آنجا خارج می‌شوند، و یا محموله‌هایی مرتبط با ایران حمل می‌کنند. بر اساس گفتگوهای بسیار سازنده با رهبران خاورمیانه، تصمیم گرفته‌ام که «هزینه بازپرداخت ۲۰ درصدی به ایالات متحده» را با توافق‌نامه‌های تجاری و سرمایه‌گذاری جایگزین کنم؛ توافق‌هایی که کشورهای مختلف حوزه خلیج فارس در ایالات متحده انجام خواهند داد. این سرمایه‌گذاری‌ها عظیم خواهند بود، اما در عین حال برای خود آن کشورها و آینده‌شان فوق‌العاده سودمند خواهند بود. همان‌طور که همگان می‌دانند، ما در مقایسه با هر کشور دیگری در طول تاریخ، بیشترین حجم سرمایه‌گذاری دلاری را در ایالات متحده داریم؛ اما این سرمایه‌گذاری‌های جدید آن رقم را حتی بزرگ‌تر خواهد کرد. ما شاهد سرازیر شدن کارخانه‌ها، تأسیسات و تجهیزات به ایالات متحده در سطحی بی‌سابقه خواهیم بود که میلیون‌ها شغل جدید و پردرآمد برای آمریکایی‌ها ایجاد خواهد کرد! آمریکا دوباره در حال پیروزی است؛ پیروزی‌ای که نظیر آن هرگز دیده نشده است. دوران کشتار صدها هزار نفر — از جمله ۵۲ هزار معترض — توسط ایران به پایان رسیده است و مهم‌تر از همه اینکه: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور
دونالد جی. ترامپ»
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68090" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68089">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCrecfwPueiD18gPe_eLA1AyGzao1L8f9B5mNcz-8nqJ4OQPBSXRGj-50UBaFoim9ZVe_62PmhErFfdWgoxTRtQy46etO8XnGZXxZpH_Mct5xyOrH1zmts3sobItSFr1rkYUKGASmobUhrCYqJ5gvsTd7FF8xF8DWa6ShdD4kleFFxLVKzZLgtBkQWY3V9acClPHnE9pTHA4SssoB58M48fp6WsD0szyEqqbLz2_fJVodB3ekWjYlVxGDaQcpVONYCpDS1rG8PoXX6H1bbN_hvFF9aakBURwzQnmsGHiWS38BKqZO9w-L3rEsww2QxKeSznrZitsgzO8locU-HnJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ پستی از کاربری که متنی از مصاحبه او با روزنامه گاردین است را بازنشر کرد.
کاربر : «وای خدای من!
اصلاً نمی‌دانستم ترامپ این را گفته است.
آن هم در سال ۱۹۸۸!
جزیره خارک را تصرف کنید!»
متن مصاحبه ترامپ با گاردین ۱۹۸۸:
«اگه من بودم در قبال ایران بسیار سخت‌گیر می‌بودم. آن‌ها از نظر روانی ما را شکست داده‌اند و باعث شده‌اند مثل یک مشت احمق به نظر برسیم. اگر حتی یک گلوله به سمت یکی از نیروها یا کشتی‌های ما شلیک می‌شد، یه بلایی  بر سر جزیره خارک می‌آوردم و وارد عمل می‌شدم و آن را تصرف می‌کردم. ایران حتی از پس عراق هم برنمی‌آید، اما ایالات متحده را به بازی گرفته است. حمله به آن‌ها به نفع جهان خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68089" target="_blank">📅 18:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68088">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d70b0c17.mp4?token=vousNYv-Ch-aWVj3I_FXn7Z5p52eMUdWYUWymhZOiwxmd_9LWoXtGrMtqdeM2JioMiT1c3n9OPRSl0F2gl3XiM8zqUYOdl6gJx7Tpa8AvriTbRYXjSnUcq31scErybU6905iUBy-AJxJqirZUNc_RREvY_BPQjFzW9XZX6sHJC7bvYm5m97h2-Bli4SGtEwekt6zt2u0Uh_Hm_UMjDtbYm90LdvTr0KeR-qC3a75wglu9U14XnICyUTtRY3YXMmQ0OEquDeErDqwWkciGI1VboB-lJBM--gbMgOW6T17j8aC0YYxMRFtMyZqoFMkmWKY2aw63POGKr1crTuBuIUwoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d70b0c17.mp4?token=vousNYv-Ch-aWVj3I_FXn7Z5p52eMUdWYUWymhZOiwxmd_9LWoXtGrMtqdeM2JioMiT1c3n9OPRSl0F2gl3XiM8zqUYOdl6gJx7Tpa8AvriTbRYXjSnUcq31scErybU6905iUBy-AJxJqirZUNc_RREvY_BPQjFzW9XZX6sHJC7bvYm5m97h2-Bli4SGtEwekt6zt2u0Uh_Hm_UMjDtbYm90LdvTr0KeR-qC3a75wglu9U14XnICyUTtRY3YXMmQ0OEquDeErDqwWkciGI1VboB-lJBM--gbMgOW6T17j8aC0YYxMRFtMyZqoFMkmWKY2aw63POGKr1crTuBuIUwoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نظر مراد ویسی در پاسخ به مخاطبی که گفت باید حرم امام‌رضا هدف باشد:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68088" target="_blank">📅 18:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68087">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به ۱۱ شناور در دریای آزوف — شامل پنج نفت‌کش، پنج کشتی باری و یک یدک‌کش — حمله کردند؛ اقدامی که نهمین روز پیاپی از کارزار حملات گسترده علیه ناوگان کشتیرانی روسیه را رقم زد. نیروهای سامانه‌های بدون‌سرنشین اوکراین اعلام کردند که در بازه زمانی ۶ تا ۱۴ ژوئیه، به ۱۱۶ شناور روسی حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68087" target="_blank">📅 17:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68086">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=F-JyM_UDELUN93DrrVYKZ1fIlycxUcSel4gkXN47DcVQI6vEyp_LoVf2cgN0IYuvmcXC4e3Wf1NTm9C4qXCi1KfHfB7oi_tB58iitcMmihDSrLtgEGA-dyO2pxaXY98_qJCROvArEVR49LojM6DmeXVUlseUQZygbieXhBE9O_D8nTqI4smpotJN181CGnPMPXImpGDzGf9hg4J5EBR7BP8d2QL0XHvNnQoguyeZLVW9bkgU9gTDGncAtfSxp9YzZhfBxUzJeMDfMFn4ZFLgawBiA9jc72ZlHcoo3nynOsx_fa1QJ2alOr2csxKGjErtqRPAYt8qZ-twJ7t9lB9HYz_gYOhN5cJwy2deJqbAvH5ceaqbfxYe8TsYK0C5f6v5TEpFlAPvece-3vqHD46RH35ORb1ZMI8eJi6q2hQ6jmUXNHeT6QXA0au40YWHrOcTsgdreosddkEBmlgvfqD2UMNOvslTHGikiupvEVPuqzK_QodXqKKouL9-yEj3IovwLmagXUjb2rc_taY_L3r5L_MFdoHAr44RhjYqN5L6rEOL3f1KIwQOwgLTEZgx0fSLzT3UlnsG7twYNh_2Fh0xnmFjBUniTxdzQB8HfZ09XdTV_magY48V9s1afUeFApt5LE_SrYfK8YQcl-EZazRP1ez10-kqJzIkZSTEAzgAigY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=F-JyM_UDELUN93DrrVYKZ1fIlycxUcSel4gkXN47DcVQI6vEyp_LoVf2cgN0IYuvmcXC4e3Wf1NTm9C4qXCi1KfHfB7oi_tB58iitcMmihDSrLtgEGA-dyO2pxaXY98_qJCROvArEVR49LojM6DmeXVUlseUQZygbieXhBE9O_D8nTqI4smpotJN181CGnPMPXImpGDzGf9hg4J5EBR7BP8d2QL0XHvNnQoguyeZLVW9bkgU9gTDGncAtfSxp9YzZhfBxUzJeMDfMFn4ZFLgawBiA9jc72ZlHcoo3nynOsx_fa1QJ2alOr2csxKGjErtqRPAYt8qZ-twJ7t9lB9HYz_gYOhN5cJwy2deJqbAvH5ceaqbfxYe8TsYK0C5f6v5TEpFlAPvece-3vqHD46RH35ORb1ZMI8eJi6q2hQ6jmUXNHeT6QXA0au40YWHrOcTsgdreosddkEBmlgvfqD2UMNOvslTHGikiupvEVPuqzK_QodXqKKouL9-yEj3IovwLmagXUjb2rc_taY_L3r5L_MFdoHAr44RhjYqN5L6rEOL3f1KIwQOwgLTEZgx0fSLzT3UlnsG7twYNh_2Fh0xnmFjBUniTxdzQB8HfZ09XdTV_magY48V9s1afUeFApt5LE_SrYfK8YQcl-EZazRP1ez10-kqJzIkZSTEAzgAigY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بخشی از مستند "عمامه صورتی" که در سال ۱۴۰۲ تولید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68086" target="_blank">📅 17:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68085">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=rkmVg2sMxxe8Z2F9ynN5GAhxtzMVIHWCCnKKu94DvQU0rQIdV2wEh7Q3-9J9vuDAgA5gZtHc6LngbiYrUAx5dZqHjU-6U9LrIRGqj7P6Ckh1qnIWl1-e-DZHXdcR3E4tG6p7YE4N-9kuXG80jgrm1C8pMs-UYPfPks8mUmMe3aBAM16bv2ew6El0EdDNUqM8Gegbe5ABXdMY_TKpGP4sA4pIlpMoKepssHGOGreaXEA40OajL-euih-gQaDM8BixwMyi-YpUNKQvlmnUmf4uip8KU13l7-pg2VndLoUmcdNGsTGyZZEU6kjeUE4JfI_2DFYcqrfF0MKagWk1HPAZzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=rkmVg2sMxxe8Z2F9ynN5GAhxtzMVIHWCCnKKu94DvQU0rQIdV2wEh7Q3-9J9vuDAgA5gZtHc6LngbiYrUAx5dZqHjU-6U9LrIRGqj7P6Ckh1qnIWl1-e-DZHXdcR3E4tG6p7YE4N-9kuXG80jgrm1C8pMs-UYPfPks8mUmMe3aBAM16bv2ew6El0EdDNUqM8Gegbe5ABXdMY_TKpGP4sA4pIlpMoKepssHGOGreaXEA40OajL-euih-gQaDM8BixwMyi-YpUNKQvlmnUmf4uip8KU13l7-pg2VndLoUmcdNGsTGyZZEU6kjeUE4JfI_2DFYcqrfF0MKagWk1HPAZzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام ویدیو ای از حملات به ایران در طول شب منتشر کرد.
در اواسط ویدیو نشان میدهد که لانچرها در فضای باز هدف قرار میگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68085" target="_blank">📅 16:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68084">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNk2gHl5PHA9amwEGSAmuJZcxGXagMg5BL6bcpM4kl_mMEzuMPOulY5xVPavZsqvsTO3RfzLkWd0BDszHWxdR78Y7D7jxATJSt5wnBzu38nxb0n_LaYI78aXgnwR0-3zhK2y2eqf8hYEUK3Avdo5t0sCPf651VpBi-CzahCKPbLhiP_qMHdsblZnk6UPF2p0_PfJF68o8YywH0K1_vBtK1t2e63u-NebdB9BXDLcIs1IuG3aBKGdCkB3Jeg_45Sjff1ck6ZNV-36upcFQ8b9oalxSGSo-jhXd4QC7aE-2X9TsoDqOQo7Cgn5xpVQiUFzj44z680Vv5L-34coOY3s3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیکتاتور قالیباف
؛
سید محمود نبویان نائب رئیس کمیسیون امنیت ملی مجلس و ابراهیم عزیزی سخنگوی کمیسیون را که از مخالفان سرسخت توافق بودند از هیأت رئیسه کمیسیون امنیت ملی حذف کرد.
عباس مقتدایی نماینده اصفهان و از حامیان دوآتشه عراقچی به عنوان نایب رئیس اول و حسن قشقاوی از دیپلماتهای حامی برجام به عنوان سخنگوی این کمیسیون انتخاب شدند
.
بهنام سعیدی از نمایندگان نزدیک به قالیباف و یعقوب رضازاده نماینده سلماس که اخیرا در مناظره‌ای با ثابتی از توافق با امریکا حمایت کرده بود نیز به عنوان دبیران اول و دوم این کمیسیون انتخاب شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68084" target="_blank">📅 15:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68083">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311dccf46f.mp4?token=SL4XjcVEVznsMaRYRGw1BLxUDl8xUhqfAlY5us4jCwxAt3df_Gj1eKRQZIjR5WF-3w7s74ki6AXqg0jAn1z2qTK2023iZB64D1_W9t6ueRJQhX2aFmyvXKtqHhvEp67BXxVk1J-3RHZbXookUL5rfOD0e7NIZsjHfkitpsPlKXgaf__IWWLaqveFE8f2Lji7omyDi3fYsW33dXZ4ByP-d-cM35gcNmp5oKa4Pz13_E05pjSVlpWZro5FBSelXExgOfCAlQEezH31Qmgk7IZ65YGg-srKosZGjTyTLbrzDqDUgTlZm2h0p3kzTJhnR541VtTpzPdapYF1H88EwdUUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311dccf46f.mp4?token=SL4XjcVEVznsMaRYRGw1BLxUDl8xUhqfAlY5us4jCwxAt3df_Gj1eKRQZIjR5WF-3w7s74ki6AXqg0jAn1z2qTK2023iZB64D1_W9t6ueRJQhX2aFmyvXKtqHhvEp67BXxVk1J-3RHZbXookUL5rfOD0e7NIZsjHfkitpsPlKXgaf__IWWLaqveFE8f2Lji7omyDi3fYsW33dXZ4ByP-d-cM35gcNmp5oKa4Pz13_E05pjSVlpWZro5FBSelXExgOfCAlQEezH31Qmgk7IZ65YGg-srKosZGjTyTLbrzDqDUgTlZm2h0p3kzTJhnR541VtTpzPdapYF1H88EwdUUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده(سنتکام):
ملوانان آمریکایی بر روی ناو «یو‌اس‌اس جورج اچ. دابلیو. بوش» (CVN 77) عملیات پروازی انجام می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68083" target="_blank">📅 15:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68082">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doWa8gRwMp_DqnUprwxT7s7pSjOy66Nk8j9on29oXgCNcdOHvjsnHYn8NppWc1R5xW1zxlGEKW6ttRhe0nGCzpu2jquJce1CFpBdAcu_qrGlSS2uaLxXyQm-iNwAXNJ5uCUa5gOpI7oIDW-w1ST2_7flpnTH1L0Nk_DnJtJMWwdftOLepKigOvYHhfH-6QdmROEXs--ph7kecCOHuuFbKZl5dXzZ-SGy8BM4-5aUCuneHbdEnyRgeKrlyOrjyKanuxiBMeFFvB5YjUWpxTTag3CygHZ8jBk-vv3H8HRSXRyrGOzMNmxYQp7n7iMcAlCfSRv3GMDtrKaqpDgVjCQvqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لبنان و اسرائیل مذاکرات خود را در رم از سر گرفتند؛ در حالی که لبنان به پیشرفت در جهت عقب‌نشینی ارتش اسرائیل و اسرائیل به پیشرفت در جهت خلع سلاح حزب‌الله امید دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68082" target="_blank">📅 14:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68081">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=koBZb0R8KV7tb9YnO2-UVMMezavCI0NkF7z0lyFxfmPZ85GOSg4hqYdwgAy2cTyVraH1pObVMZ3eXiNsG8ydeopxMeHqUCE7n5_OMmpDfoAlQq_nSTbXQAkVEw0RaYQHzmSHZ8v95jV3jmMrWnU0vJYT6Aya-uFR5quYow0eVr8LRe4SnKs2vv5_Omv9dXFwm-m558vhzz7buksDICRQhVRn1AlKvEl12uuyBgJOCoyPau7VNXSfCf8uqFVvlokstWAV30rFDJ4oTaeOG5XMNWv1WEKwWroCAQbFQOkN1LVuym0ZQBZRT6q5WR_36IFvmsRJPboBkYAgm6ICM5NzIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=koBZb0R8KV7tb9YnO2-UVMMezavCI0NkF7z0lyFxfmPZ85GOSg4hqYdwgAy2cTyVraH1pObVMZ3eXiNsG8ydeopxMeHqUCE7n5_OMmpDfoAlQq_nSTbXQAkVEw0RaYQHzmSHZ8v95jV3jmMrWnU0vJYT6Aya-uFR5quYow0eVr8LRe4SnKs2vv5_Omv9dXFwm-m558vhzz7buksDICRQhVRn1AlKvEl12uuyBgJOCoyPau7VNXSfCf8uqFVvlokstWAV30rFDJ4oTaeOG5XMNWv1WEKwWroCAQbFQOkN1LVuym0ZQBZRT6q5WR_36IFvmsRJPboBkYAgm6ICM5NzIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:  اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد. در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68081" target="_blank">📅 13:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68080">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
معاون استاندار بوشهر:
چهار نقطه در شهر بوشهر مورد اصابت بمباران آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68080" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68079">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8RGmQ6Jmgw8sjSQAyo_fL_31WWTVSoYuT_bnoD7kEYBj_cgly-vMMF2XHQfCze3nCYo5sGsHnHpDwR_-ZgugoojSCv0uOBReKDLntQxC0XTfOlac2bahYq_qjOpmB4uGrPOFRanB-Y9A56jyxZTummhtx1jORrNpQssIcdStuIRCj8dZLml8cGfisyKFg4Demdsl9batg1LlGyf519dFFDgqd4mfJSJf7zcNqwKjMiYs8envrueHTNxTFReq4pE6kq41z3g50ckjdxtQV8J3hIJ8Jqpyn2vzwsrp3Y9kXGZmppxWKoQynnIyR_wyo1VWjy8o_VeJVkGyjnObdb10w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نمایی دیگر از بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68079" target="_blank">📅 13:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68078">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTAHcNueMdbv2XzLvNV8J7Vdv0nXhrCZafLJDPciKs5tIhT6ELWKeM9WXUODElIP1ElXUbzJZdxyoeUqAR1Z3IjxI3Tcnu3mvNyM3lHYV1ZWAlwwFikj1pbiqv6dc66ta4s1df6EpjS8Ijwle3MxeNFMGOQ7LBFfU2Np278twVvdmg9HIsj1hDWFJwKvLyz2uaCxljFcsMG9mKWwA83SX3MGDWn9cXVEWWmowMnLf8MFHF4RXxhvzt0rtI7_ydbqPicSaCXEycLR5HsNATdTkGpuevkafhaYnrus-HfA8I8ZkWv2g6BULbUsZ8JG685ODEEwmrRqAG_Wdm2Eo5-4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68078" target="_blank">📅 12:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68077">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68077" target="_blank">📅 12:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68076">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
پنج انفجار در بندرعباس
@News_hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68076" target="_blank">📅 12:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68075">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید در بحرین
@News_hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68075" target="_blank">📅 12:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68074">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ گزارش های اولیه و #غیررسمی از حمله سپاه به سفارت اسرائیل در بحرین  @News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68074" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68073">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
#مهم
؛ گزارش های اولیه و
#غیررسمی
از حمله سپاه به سفارت اسرائیل در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68073" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68072">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=Keu-MqgVkpTJgEIaYEyRQeJxueTUYOKZl0Y3Z5dsREEpT2Wd4lMDw8mE2uUHLp16wLacl_KjNwPV5OLLubnqJB4IvSXPpnaXSL5rmjLofaz4djlQpo0ELqh_iF5MZGU14dnVabR6WmRfNjUo2xjt_veAgyPKHM3wUXz1tTOQLfJtg88T9he5xgeKEe82hvzO4DxRRvO6LLIQAx8IXZNs3OG-3f99r3qYuE6eoN_zaMseRL3cl8WxkqBH2Lh7Cj3g10r0GmuWuz1SN82f1h02e_XM8gInVgRyDbWq2ODy1sYAt4LRfI8o8M8PYyBF6TljyU3vmcUQ2J88XvqWAM5eDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=Keu-MqgVkpTJgEIaYEyRQeJxueTUYOKZl0Y3Z5dsREEpT2Wd4lMDw8mE2uUHLp16wLacl_KjNwPV5OLLubnqJB4IvSXPpnaXSL5rmjLofaz4djlQpo0ELqh_iF5MZGU14dnVabR6WmRfNjUo2xjt_veAgyPKHM3wUXz1tTOQLfJtg88T9he5xgeKEe82hvzO4DxRRvO6LLIQAx8IXZNs3OG-3f99r3qYuE6eoN_zaMseRL3cl8WxkqBH2Lh7Cj3g10r0GmuWuz1SN82f1h02e_XM8gInVgRyDbWq2ODy1sYAt4LRfI8o8M8PYyBF6TljyU3vmcUQ2J88XvqWAM5eDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداسیما داشت خلاصه‌ی یه سریال رو پخش میکرد که تو یه تیکش اگه فقط صدارو گوش کنید، فکرمیکنید صداسیما در حال پخش پورنه:
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68072" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68071">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=Vr9xh7zTwBQhckl736uuYvzOeBV_JdyXOie5kErRnhlTnFCFhJzgFqKf6SgDQVRJjf9gCV_cfhcIMTfQ8812SeISNJygeoyzijD9n-ZcCgtyJpONdzFlp4IK69jAsZIT31mgW1NKWWOi2v6vnlODFeePPY6Ax4oFuslArmBNfGcWeIkoU5Uk2T3Cps277wrVDPRLiT9KTShgCmvzdWoi0S3TMLY81yCSQBn5PlThWmFBfiQa6FfpP6UG4lIvsrc2Qm1N3KolYBF_aTP-Atx8nDHdy0wdvWhpxj3Ekqh066VRzMtZoCWgNAIWoOyBwFoKeOLsPF1nUPXC6KQlGe2MuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=Vr9xh7zTwBQhckl736uuYvzOeBV_JdyXOie5kErRnhlTnFCFhJzgFqKf6SgDQVRJjf9gCV_cfhcIMTfQ8812SeISNJygeoyzijD9n-ZcCgtyJpONdzFlp4IK69jAsZIT31mgW1NKWWOi2v6vnlODFeePPY6Ax4oFuslArmBNfGcWeIkoU5Uk2T3Cps277wrVDPRLiT9KTShgCmvzdWoi0S3TMLY81yCSQBn5PlThWmFBfiQa6FfpP6UG4lIvsrc2Qm1N3KolYBF_aTP-Atx8nDHdy0wdvWhpxj3Ekqh066VRzMtZoCWgNAIWoOyBwFoKeOLsPF1nUPXC6KQlGe2MuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چمران رئیس شورای شهر تهران به سوالی درباره قطعی برق بدون اطلاع قبلی:
اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68071" target="_blank">📅 11:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68070">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzAvTM7KHj5V8Yy1L_O1Bv-78rKAAuV7dJAaNSyQ8OjJMQSmDPHV76vmfeHMo0jEkJlhSQXpL9CQiQB2Aelmgcx_yTx_ugTY_R-7fC8DTToRYXpbp--5nZL8mPz3syA82LJy1ksXB_RWEbeNqv13M_4uyodznoljQmwRHSOsdR72wX8x0hhEL1j4IiTGOrSPfKXlJZaP0119zO2C6SaU_xWfi0S8MfYylasnhi8ZpmoEIfngNyLYGlw91jfYQGWvzLnIyE5woQfvKDGX9ZiPXfzAxOvKA0VQur46g4AshMSNx_U77WTDyww65rolaHh6oFToaWaNgqrGBnDE83c5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی بریتانیا:
گزارشی از یک حادثه در فاصله ۱۳ مایل دریایی جنوب شرقی لیماه، عمان، دریافت کردیم
یک نفتکش گزارش داده است که هنگام تردد در مسیر جنوبی به سمت خارج، مورد اصابت موشک قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68070" target="_blank">📅 11:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68069">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=Rj1Qu23rmPnAfpxOV0djJf9U6ABcOiixIuWAe2Wly9APGadG-UeGy4Lv8KmhzOT3C_gG1eHlBNPJAx-HKu_9n9l8Dcy1yAOrSsh24yL03CYXNQ4OTdZxWxX_NwyILB0AUCafDQRngtFxk8oi6KXPy6goZLtWqEPBFaxYvptW6romoQKrjffS3P2ohjA7atzU3FpeH_50lZABhSsiUSmgHFdgt_FGl7CKH0m5XpctAIfGw0AzwEt6oiTyKwUr7sBUTjSf_d0HNNUwOdGtWXZ-Lp8z9NGU9mnklK_BofPkFhgB7wwXkijU1sPpSM16Fe5n_6V-FYaZdcd0UXBWX5fpKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=Rj1Qu23rmPnAfpxOV0djJf9U6ABcOiixIuWAe2Wly9APGadG-UeGy4Lv8KmhzOT3C_gG1eHlBNPJAx-HKu_9n9l8Dcy1yAOrSsh24yL03CYXNQ4OTdZxWxX_NwyILB0AUCafDQRngtFxk8oi6KXPy6goZLtWqEPBFaxYvptW6romoQKrjffS3P2ohjA7atzU3FpeH_50lZABhSsiUSmgHFdgt_FGl7CKH0m5XpctAIfGw0AzwEt6oiTyKwUr7sBUTjSf_d0HNNUwOdGtWXZ-Lp8z9NGU9mnklK_BofPkFhgB7wwXkijU1sPpSM16Fe5n_6V-FYaZdcd0UXBWX5fpKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراد ویسی،تحلیلگر ارشد اینترنشنال:
چشم انداز موجود تشدید جنگه،پاکستانم دیگه نمیتونه بین ایران و آمریکا میانجیگری کنه.
جنگ سوم بین دو کشور تو روزای آینده شروع میشه.
اگه اسرائیلم وارد بشه یه لایه دیگه از سران جمهوری اسلامی رو حذف میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68069" target="_blank">📅 11:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68068">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ah6FsABwOPqcpiz-wJwd_LglAai2UIdg6H98uJr762xeMVANqNfnchLQvEY5UC1jNWbfv05Vs7bxROGgxljydG6tCsGkA2sHAJWV0pwl06hpFF_upClZXL5anNhVJ5_X7CR19yERUmUn5s-XM_5lwSvmSAKoWV6LqTuHfJMOFniqoHf8zWn5IFGujng5H2Cuckm6TezHvJjoVqN0z_kyxzLTyxz0g0JJk1zLSdkoW76pBB5oXZlLjxwyl5ak5pVLfNSbWNoiRRFa00de3Zodg8jtEQdTRtVbWo270SqT3Q9R1sj5xJOjPyqdtqL9C0b29koQprcujGkKdzXNd0RW0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) آخرین موج حملات علیه ایران را در ساعت ۱۰:۱۵ شب (به وقت شرقی) روز ۱۳ ژوئیه به پایان رساند.
در جریان این عملیات پنج‌ساعته، نیروهای آمریکایی با هدف تضعیف بیشتر توانایی ایران در حمله به کشتی‌های تجاری، با موفقیت به اهداف نظامی در نقاط مختلف ایران از جمله بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردند.
نیروهای سنتکام برای هدف قرار دادن سامانه‌های پدافند ساحلی، سایت‌های موشکی و پهپادی و توانمندی‌های دریایی ایران، از مهمات دقیق‌زن استفاده کردند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه مستقر هستند.
نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار باقی مانده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68068" target="_blank">📅 10:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68067">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=g5RiAt4oQfna6jM5ENCRKraLYHHePCrWDpfpBiHHNKWgSfjGfMIYdVYxRCDDfQLRmnb_BUCiQENQeqDnkUCFFALLH7jjiEy3YAzI4sqAJRPh-g9bgZWQtm-PPNekKOCYXYq3ZhmW6WMPFwDuX5L6y7a1L0LjE6a1sPru_QQR3VxB-yIL9CkkR39jOAtu30Vkx7lihWsLmKXkWBog7bvb1T09sEkK2OZfsNTfu3bYKQvILuCLr8QimZ5CRmmlvP36oACUQz5Fzd4E5le57ebgeRCv82xMgyEI849tkUpu2AGIRa1nI6Bjs1bnRSYsHwXQ-anVzBCwJWCw8NcX8_qQGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=g5RiAt4oQfna6jM5ENCRKraLYHHePCrWDpfpBiHHNKWgSfjGfMIYdVYxRCDDfQLRmnb_BUCiQENQeqDnkUCFFALLH7jjiEy3YAzI4sqAJRPh-g9bgZWQtm-PPNekKOCYXYq3ZhmW6WMPFwDuX5L6y7a1L0LjE6a1sPru_QQR3VxB-yIL9CkkR39jOAtu30Vkx7lihWsLmKXkWBog7bvb1T09sEkK2OZfsNTfu3bYKQvILuCLr8QimZ5CRmmlvP36oACUQz5Fzd4E5le57ebgeRCv82xMgyEI849tkUpu2AGIRa1nI6Bjs1bnRSYsHwXQ-anVzBCwJWCw8NcX8_qQGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخطار پلمب، مانکنت نامتعارفه !!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68067" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
