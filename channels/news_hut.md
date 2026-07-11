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
<img src="https://cdn4.telesco.pe/file/KGnE1t2xKdokcPy29rEPDZdGCJn6q0-XFabDxpFG2aC6HQqM3vCFGSXfwkza5tbNNxQG2nRFEcFscpWwkNqWVc7w1YPbb3xseiIZfsjCaxXwOJCc_BCg_7ozW62QhibYWMm7eR9HmjX6odoOA_oGagmTV4P_qVO3PJf5s2cVmxzqP6vokwDtfhauWvDVSMV_ePJQ40nbuPnVotSTYS1kMJpXl--OjAs4E6T3PXuqByGqKfy1dD9dbI8_75UZQUwSxHAeib8S29UpBcxnr0yljHEOezaEusCaDT1uUGFreSd78QuA1o7lfeZNeKEQd8p8eZhHVFp8G6wF_h6y_-53nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 185K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 05:21:07</div>
<hr>

<div class="tg-post" id="msg-67764">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/news_hut/67764" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/news_hut/67764" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67763">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/g3NsfmONA3q3f-gr-kLCDAnrh7AFM7sxuY6y4Oz70Cq6-qdN8Fn1h4jYXD_xXwk-8QP2aH55PEUev7MzDPufq7tr9mwnFvgcMvW4PjFx0lT_8wdQVUJEoxBvQAWO86MYZcn8XddhkOaqHVWIXgNV3ZhsTPYfMR0Sdq3IKC94ol5S7snmr1t9ol7WlPB6YeecwzX21pDOSimz5U25p2JMe7JOEyOXriMn2sRuZcHv8eGeMhHS_gdsoEfTPQ-gBaVxlYg6An8QhiiQZTg3ATVQNcb4yn7EWhp4j2wLKskWjI-e993i3nF4Iv13EDhNIx0IgcyDT1cRQxM2O0zEe6uEAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
قهرمان جام جهانی ۲۰۲۶ از نگاه شما کدام تیم است؟
✨
با پیشبینی قهرمان جام جهانی شانس چندین برابر شدن بردتو امتحان کن
🚀
💥
متنوع ترین آپشنهای پیشبینی در
لنزبت
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری با انواع هدایای نقدی   روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
A19
📱
https://www.lenzbet1.living</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/news_hut/67763" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67762">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUyaMGNNppORqfQYc7GdnjvzGYnI6nndRHdUiZC2hUQ1_6SdaKmIvbaQewO6B2ZqrL0s7GVJ7ZQooeadaR2mcr6rsr8ekIqon2ZynbbyY3UjsG_cay4-dmBZL00fQTtEZobzxHxexKZGLdZxm4UYFrxwzTd--429gztWvr5UH4B72xk-6ig2j2uP232_UPb_meS5QQwAqI9vg6XYqlYtLOosk_EnfGhyDn7RbaV2ojdXvB4RzBbOWLiBVj0RjOGD9pbRElTSF6s6AymqV4qLgeWNNtqz1iUrN0tZ0LPSs3U4ICL22wsM5KKrXWk_ydhR94o_Xj07zMDvk_CuykRjWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/news_hut/67762" target="_blank">📅 01:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67761">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
❌
یک مقام ارشد آمریکایی:
ایران‌ با عواقب وخیمی روبرو خواهند شد اگر از انتشار یک بیانیه عمومی فردا خودداری کنند که در آن اعلام شود تمام مسیرها در تنگه هرمز باز هستند.
اگر این موضع [آنها] فردا نباشد، روز خوبی برایشان نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67761" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67760">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsiF_czdiv3P_s_KBm5wvDzdsO4Ki5s-i3HsWXIxZUReCNC99AGrQkQxYXp16EA5SFEMZKSbFKqZ_A3hpib4CRDsdZ9APVPqmpmNIIFxBfu0W0Bep7I5WbK0pOJqoPAS82u534NYQbLFMV9x9k-607rBtJZS44doOjZu9eYu40kYdxNIOei37rr9pz5xzblUfcdwrt756TtFT1dJSXt-BT3hXhIr58LdGE7-blJ06AyKj7831TqrHMLs5FEVqKDA74iHb2y2hsd7YLkQDXaUqOV1JnarwdmPMnSSfyntj27Nk3gcgCS5cQYd3xUdg4ZC-d64WLsgzbehuUBky3fWFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته مقامات آمریکایی، ایالات متحده به ایران تا روز شنبه مهلت داده است تا حملات در تنگه هرمز را علناً محکوم کند و باز بودن این تنگه را اعلام نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67760" target="_blank">📅 00:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67759">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کشوری غنی، اما مردمی فقیر
💔
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67759" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67758">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:  ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.  فردا در جلسه ای در موردش تصمیم گیری می کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67758" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67757">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:
ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.
فردا در جلسه ای در موردش تصمیم گیری می کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67757" target="_blank">📅 00:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67756">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=cAgeY62QBhwzSWEWd6lvcBjH6tYUlse0F74HFGDi1QfNUwvk1ZSv7K7hFzmPVJdscEIESB9QE8J8GA9CkgUvg52F8_YEl8gwVQf_5pBtPW_C9l-CSVnuTu4pS3JLBpPnLx7bcHxzDf326vEHMa63mRJKKLLGS984giRT1DtiR05GEEibMNBEJ4ewNKvWbdXyadl0nEEMlzE4vZrdZOWa5ynMcPaQqUy2UqgKlh3ZDcB1GfRZMo6ofm4-C4SYN0-elCNTFUZq0adr-Tzu2gaJPWBAwLVac5O3aBaXNnwNX0Vhab-LMIywb0wzpIca8GXHUoi54EAlbZYPZv0bgOcKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=cAgeY62QBhwzSWEWd6lvcBjH6tYUlse0F74HFGDi1QfNUwvk1ZSv7K7hFzmPVJdscEIESB9QE8J8GA9CkgUvg52F8_YEl8gwVQf_5pBtPW_C9l-CSVnuTu4pS3JLBpPnLx7bcHxzDf326vEHMa63mRJKKLLGS984giRT1DtiR05GEEibMNBEJ4ewNKvWbdXyadl0nEEMlzE4vZrdZOWa5ynMcPaQqUy2UqgKlh3ZDcB1GfRZMo6ofm4-C4SYN0-elCNTFUZq0adr-Tzu2gaJPWBAwLVac5O3aBaXNnwNX0Vhab-LMIywb0wzpIca8GXHUoi54EAlbZYPZv0bgOcKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت امور خارجه:
ایران اجازه بازرسی از تأسیسات آسیب دیده در اثر حملات آمریکا و اسرائیل را نخواهد داد و قطعنامه 2231 شورای امنیت سازمان ملل عملاً اعتبار قانونی خود را از دست داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67756" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67753">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjWXpJrfEIYdzjudKjnBAw3XwumH2Jx-6Yh9BRDYf1g7QnfcPtN3aG0_YB2lgxyaaAt4jULCnpqppQFc2S1FHz5J-AjC6mvD4xLGdY2faO5GZ5WqMC9hiOGIKt6jzlaqPXgnA8YC7W05eRlJ2SqPMvcbOW3IsZk87RU4Byr8wmQ0gFmF4VdEvoVY3ERazBhWQ_tqV4V1_OQB_bavjjJki2L-Oy9L_tMQXPOvbu9t8n_Gw5XolhOVVXkRqkdNedOA5NaC6AVPVAQBxG9TZOCD0er-XV2RHfBW7Y9dJKNXCDntCEMXImfEs2AtC1IMfYjjkVu9Ot95KoPZzBAJQxRK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhHvZwXvtcW6rKnbVk8xW5gdzzZGV2uxGSkNCC4vgMevqm9cdgYLM8PRKCEn9mTI7GMVJI6Jo-kLAByELHzeMHmM85cdJxPtGl00PskrP5tJ00JUlp1W97YMZIWFyfoo0-J5FeDHXAOtIjD1XQPFIdsKn9pdTZfQLGe9nnGJwLL9cEw78ucccum6fSui9WfD3Ya2-me_7hOXCQ53szt8JdvndhQ2_x9qhnGnjvdsfzDiBnFb2Jg-sujLqTJpI0hPl3xYmdwBLvjLyB7ceo5DdL6hxN_Jyezy28AuiOZBucrDdaluIums6WhdYZe4xzg8TJQuLIsn_QummbBZdBM-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONhfIFY-F4rSHol8RkawhITl7MiOpP3Lven9H7aTJdE9qDbTiOZ7Yfw_jeMfFRzGePMQ7y6O4GSuZXfc8aKn7tm06UG3ncWiaCy7f7yOKGs7c6C-ELadh96qMMOyn2hZ4BFna5aV8-W-XdkxGg-5NE3AopIJLWsTHWt96KpJLo_94O4BPQ1qZpvNtJ9YSH3EGwJg54FVS9fPXwT-Pqc0NkdeAxJXm_QI-sUYk4B8MnVhiYUG6ChRjFA4J_2HhqtpMco7p5JYyUk-mE8IssjVcIq2XaFLiZjjB3KdHkwEmcAcoTvwDGOE3mL08LKSzKgS4kJz1i16G1V7JdIst-nd8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
شبکه خبری CNN تصاویر ماهواره ای  ادعایی را منتشر کرده که نشان می‌دهد ایران در تلاش است تا تاسیسات هسته‌ای واقع در پارکچین را بازسازی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67753" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67752">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e999307d.mp4?token=GAQNZFEO3exKfwA3IFl5Lj9bZh4JV1_iv5bxg_aougOqPBefCT78sp8aYfJBxpRD0LTQcucLSJkqB3ID0TRBVw5VQQwmSYiTWdXSM92i2oVxADfA3YdmJ3FfmPVcm7u0dw-OmcHpIz_QYXFlL72x1ZVzfAW1Wtuu3sLG6A8y0XtmxdEABiqzZ2lLrVedn7rOW7gkltq0uOwzHnj0rLsDUDSjPmQ8NXX5M9IScxlFfJvUiutIPqZonQqfrY69r-_DAbzXQBnZp4rhfeSYsjXUhNCvzRmIMAW_8JIee5HSX2Rix9RtbfCNDse4mZX_6bb5QOb2Cf6A_jt1vnJgRqBQiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e999307d.mp4?token=GAQNZFEO3exKfwA3IFl5Lj9bZh4JV1_iv5bxg_aougOqPBefCT78sp8aYfJBxpRD0LTQcucLSJkqB3ID0TRBVw5VQQwmSYiTWdXSM92i2oVxADfA3YdmJ3FfmPVcm7u0dw-OmcHpIz_QYXFlL72x1ZVzfAW1Wtuu3sLG6A8y0XtmxdEABiqzZ2lLrVedn7rOW7gkltq0uOwzHnj0rLsDUDSjPmQ8NXX5M9IScxlFfJvUiutIPqZonQqfrY69r-_DAbzXQBnZp4rhfeSYsjXUhNCvzRmIMAW_8JIee5HSX2Rix9RtbfCNDse4mZX_6bb5QOb2Cf6A_jt1vnJgRqBQiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب ترامپ رو تو مشهد دار زدن بعدشم ماکتشو سوزوندن
گفتن خودشو که نمیتونیم بکشیم حداقل ماکتشو بکشیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67752" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67751">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtNa-OaHDVneW-ap5qGJ_0cE_rLc-1YWUY3cGMB-eMbfwBqOWtowJlpP1wWnbQn7m0ruQLq4mkF3HN9NYgkZ56Ljvq4XKEsbCQy68enGHO2fgQDfuYmC81qYXwOzmlVRwJ6WLPkOsKnh0vzfvCeXzCANWHz0j953z9AsyYXlFADjXtnaXCJbPY7XLPeMwSjjniSFEZv776L26nuWkH6XyMwrOo4_I0d-M4o5MSr9JBUbJIh8Sfrxl7Mgw0QWEm2gSzygGcMb_4a2WyDEOa8sh7WsmdrbFSA047sf6HchxdzcxpEfWzGSExeqxOpb4de3k5MqpHAq3_OaIVWoXqpskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
در جریان مذاکرات، به معاون رئیس‌جمهور آمریکا توضیح دادم که ما به شما اصلاً اعتماد نداریم.
به نظر من، تنها کسانی می‌توانند با ایالات متحده مذاکره کنند که برای جنگ آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67751" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67750">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.  @bet_maxxx @bet_maxxx @bdt_maxxx</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67750" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67749">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnegin</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAEiGawFGl7_cmbtzT2t9OdiKGks9L2_bEyp76OZSz_eAL5_X1o89IwLZ7BS9gelKsS1ph9FTZWISJCj_KMB66FFcX2c777m242SGXpouF2MFEGfT9AZbM4wTx2YOIm-mK5gsLRWCVEcNkZyB813odPoKCe4QxFTCXeF-tPrrcALMwcvD5vi1976ZXTCUxWu3pykYfhtM-V3X5MzoZQmHmw_722stBA37N_idq2j-b6KXKraL_Axmfb2HOi8vbYJMb2D3WXATAGmiU4oLEyADtu8fLoHlYJBQ50uN6x_Z6cqPV66UKkNXyD26pA3xPoWFXddECjyvIchcCjq3X-ZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال
اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی
همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.
@bet_maxxx
@bet_maxxx
@bdt_maxxx</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67749" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67748">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=U2IoC9J0w9VYyIMvBqheL51JrUCgnvtX5sYvyhUJSE63SQxkrToN8zb0KJiK41zIjNDBwnxUNRa17qxDmmWZv7HJwF6QQRR4PYORe3dFH5RJGt0833Fj6OUEBFbCCWRwtDxbW8bbu6aBtImj40uzMGBQyuJqDVSjXvf8SbWgpGHXmdtHRdHb58LtdDeiNcUeEOY-QKDhGdr0neWamPiIRN5aRF73lWmyT5kCYseinl2iLhq7C1OTBWINgN-R63gb4P3PqSooc6vayra73B3PIzBm0apmELCG6rSQSBSa9Ujm0mRH4J6djdK0M3WGvKrSbLuMRNv6X2OT95_AVw7rzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=U2IoC9J0w9VYyIMvBqheL51JrUCgnvtX5sYvyhUJSE63SQxkrToN8zb0KJiK41zIjNDBwnxUNRa17qxDmmWZv7HJwF6QQRR4PYORe3dFH5RJGt0833Fj6OUEBFbCCWRwtDxbW8bbu6aBtImj40uzMGBQyuJqDVSjXvf8SbWgpGHXmdtHRdHb58LtdDeiNcUeEOY-QKDhGdr0neWamPiIRN5aRF73lWmyT5kCYseinl2iLhq7C1OTBWINgN-R63gb4P3PqSooc6vayra73B3PIzBm0apmELCG6rSQSBSa9Ujm0mRH4J6djdK0M3WGvKrSbLuMRNv6X2OT95_AVw7rzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالد ریگان چهلمین رئیس جمهور ایالات متحده آمریکا:
در این سخنرانی، ریگان با یک روایت طنزآمیز، دیدگاه خود درباره نقش دولت و مسئولیت فردی را بیان می‌کند؛ روایتی که سال‌هاست در مباحث سیاسی از آن یاد می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67748" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67747">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXb6QQGwU4YyxWrG_0PGLFXwU1i1QqgwksNtCStxLs-nE88Nw2wFxC3DE8UFMJNQGN__Xo7mhSTmfSLh-OvNFVuJUm4U2W7NZQRINMPVRR-FEYkuAWC7-WGEYRy51ZFEB_zjwaZX_Ampl3jza5YbjkwTDo2QfwqR1_AY8t6qcxmSHWS9V1_NM0qedeMn8z2szRa1XBKn54XUeV3bIyVkBwbhm7fOrsJOP7GmNU8Vm61WirsWQDQpBFhdpM6sNQN76nvMDyY_CicuNIR64gIQ7ngMa7_BC13xQ1irQ44-6lSl-n4C2OrTe0mBwi8kF-NEt4AQTqPZd7pht4AopZx3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل هیوم: آمریکا و اسرائیل گزینه‌های براندازی جمهوری اسلامی را بررسی می‌کنند
روزنامه اسرائیل هیوم در گزارشی به نقل از منابع دیپلماتیک منطقه‌ای و غربی مدعی شد که ایالات متحده، اسرائیل و برخی کشورهای منطقه در حال بررسی راهکارهایی برای تضعیف و در نهایت براندازی جمهوری اسلامی هستند.
این گزارش همچنین ادعا می‌کند که در پی تشدید اختلافات داخلی در ایران، مسعود پزشکیان، رئیس‌جمهور، و عباس عراقچی، وزیر امور خارجه، با فشار فزاینده جریان‌های تندرو و فرماندهان سپاه پاسداران روبه‌رو شده‌اند و حتی احتمال کنار گذاشته شدن دولت پزشکیان مطرح شده است.
اسرائیل هیوم به نقل از منابع خود مدعی شده است که عباس عراقچی در تماس با میانجی‌ها اعلام کرده دولت ایران نتوانسته موافقت سپاه با مفاد تفاهم با آمریکا و توقف حملات به کشتی‌ها در تنگه هرمز را جلب کند.
این روزنامه همچنین مدعی است که یکی از گزینه‌های مورد بررسی واشینگتن و تل‌آویو، تشدید دوباره فشارهای اقتصادی و بازگرداندن کامل تحریم‌ها با هدف افزایش فشار بر رژیم ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67747" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67746">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7q2YCcxvNz_Y7KJ48KJNysT7jB8z-GVSDxsaj-W6wO65DG58YifBhEKCoFhFBsE2yzSFGPNkWi-WAWA0iNPnPAo1NJP6YqmCfzjl3-SkofS_8wVPoBWMmzyeGWE-KOTK5NRSO_txYn-itZ31paHafTNeLe-K1ChXVR9KMdr27OkLiAKvNjS2PPoXQ2CRYPHsz0Jic1vGdRkhBAzLqube6Hu5vtogB3Z9R0vX-0Kd76ij__OawxgsWgX81EHX3rhynyf5BtXcxj5NCY6_RGvYhrFLkoZ2K5gPFkXKCe4kYLzeXYHS5jEcSrudhexgxbT2TsiQvFkpgsYymHqXDD3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باراک راوید:
بر اساس گفته‌های یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده، به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و تلاش کنند تا تنش‌ها را کاهش داده و شرایط را برای از سرگیری مذاکرات فراهم کنند.
این دیپلمات گفت که جلسات بین مقامات قطری و ایرانی در تهران همچنان در حال برگزاری است، "اما واضح است که هر دو طرف تمایل دارند به توافق‌نامه اولیه بازگردند."
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67746" target="_blank">📅 20:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67745">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS_TQaagjmgZ74AAKxBmXwXBOY_B9XsQSxFT-UjW4FPtLHToOLfKZFewi-1ZCEuHfpR0UHhFeAb9CJ-Hp8GLUGin_Wibbtqy1Tl6euJhzXNnDUV2vJ_YBpdENhXkXO8MES0W1E9Y89z0ocipwMHelmy77xBBs2xzxFcy3hP33m8SRyoaALyoSZE9hQsxINzar551KJafFvz9PwHVSkGjiGqDNxtzG9pqOcLXbeaIWc-zE_888v_jQbCV8fr7GGErTVbuaUc_6w5yhDcGVle4K76hQxShcpEn1mhoRO4Ltun92_VIjP7mWxdJKs30dpM0sfDXOOkvHJJF8TEOxeopUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به «نیویورک پست» گفت که دستوراتی صادر کرده است مبنی بر اینکه اگر ایران در ترور او موفق شود، ایالات متحده باید «به‌معنای واقعی کلمه، آن‌ها را چنان بمباران کند که هرگز پیش از این ندیده باشند.» او افزود که «مدت‌هاست» نفر اولِ فهرست ترور ایران بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67745" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67744">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdFEqDwNTxZs2Ii58BzB9q8svz6SgVxULERrn4RA2OTpE8kVst5OljdjfBTAKBu2e1dRED9lLpX27iJDZNH1JpZUCn-KrhTVpr2dR-eJ-zTk9gPDwcJeBPWgelB2PPE_syc2Nmp2gkLcAhVeff212XLJguME0kiao6Xy53Na7pmBGBEziwBdkgCR5z40HY_qbskEFpSon698QroammssZv9ukNCIm50_pEuaX5BRchBEeY7smvDTHf7MasjPyVcYLrotSZGa3QwEU4tccN7y-B1HvB00k_8akO6Hf05xSY_dFbyL2YTBlOt5HfWnuznBMkEPgrdUhh1YskUfvdox6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
ترامپ و خبرگزاری آکسیوس را نادیده بگیرید. هیچ مذاکره‌ای تا زمانی که دولت ترامپ به تعهدات خود عمل نکند، صورت نخواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67744" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67743">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
آکسیوس:
پیش‌بینی می‌شود که ایالات متحده و ایران هفته آینده دور دیگری از مذاکرات را برگزار کنند، احتمالاً در سوئیس.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67743" target="_blank">📅 19:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67742">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=WhZkws8Bcz5B3HbYQb2MvyIN5q2XHURqKVRDjgQ73AJ1zCj9Be8dlj2R0gw23XPCiXe4JMpPYKqCUC9oHIP9ty6OPvPVyX3wnO3tODu0bZV3VNtzCd_NdEWyHpCBJqbkZ0bnwobQyNk0waD2QYMCo_JP35p9zMyOsFa8MBIKDS2DFZG19rkHP2jmnnkPPWFzoe0GUgDpHsFjif8TbQko1MhfWlw0UGmZWAcIXogQq368nDCIOXFbp419Eo9Z7Q_AWbBhr9XrrtIs6AIc1kY9CZRzMFJH1SYRmQ18_TKW_G-TUvQTBuUHg_IQuw0lVfnDyboIVRaBUmLRYX2hUWuCrA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=WhZkws8Bcz5B3HbYQb2MvyIN5q2XHURqKVRDjgQ73AJ1zCj9Be8dlj2R0gw23XPCiXe4JMpPYKqCUC9oHIP9ty6OPvPVyX3wnO3tODu0bZV3VNtzCd_NdEWyHpCBJqbkZ0bnwobQyNk0waD2QYMCo_JP35p9zMyOsFa8MBIKDS2DFZG19rkHP2jmnnkPPWFzoe0GUgDpHsFjif8TbQko1MhfWlw0UGmZWAcIXogQq368nDCIOXFbp419Eo9Z7Q_AWbBhr9XrrtIs6AIc1kY9CZRzMFJH1SYRmQ18_TKW_G-TUvQTBuUHg_IQuw0lVfnDyboIVRaBUmLRYX2hUWuCrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش‌سوزی گسترده در مجموعه اکسین پلدختر در استان لرستان
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67742" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67741">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuHU0bQPTXx84WC3vxRpgMZHTs6woLF85PuswU3Hxo4pF-IFY9AcyPPQHaqfMU6HckEGoKHKS5VsRfwvhl-Vf81agxvmuUdAoGeKvOqqFn5FXwHV5wrVj8luNBFt7nxEMBzTlHsiDmhPMaEsvM4eebYL7NO1twLcM1lHV9Q3t_NDARYDBymOrxNlX4E9Ez0-tlf_n5ghRPzwUvwwNcHtBfqORvSn5iX0ZXQp5iVGZIa4CvfKWQ3RmCjcIGV2gGX0Ne98h9NncHOec9H1EbCYE_kByY2eridc_HxjW3oLATs5zHnSMkl30rARMlowxYFprStnX1FIrzaVFcIu27BKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انفجار در پالایشگاه نفت پلدختر در استان لرستان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67741" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67740">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUsjWXQG5QPbV5o-yPfic5CkmmhYvqUjOvvNramn5dh6wnzC0nLbrvfysb6qPv3lqXdyStrCgIz0FwR2fHRSnl3H399iTYbmD9LaIuMeM3o8PvGrB9Fz6DuLVE-XujUpeUGZMAFuJ8ZjB64M0IKXf_HoyFUTCrv2Zloe1SvVWK0w24aee3yCCK5-gBD17SqmOL6NFMp37YzZ0i2tOo4C9tkg1slQvA1F0uV2Mv8Eu5y_yplWWHVdmbyPyaSeLXlNJKyQBjj55yChmRdhAe-PRTy_wMXCgyoeKXR2NQg5wo4InipSJadSGnzfUC2l_fUpcVbxukxcFth-hjLDE_CSaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بلند شدن دود در کنارک پس از وقوع دو انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67740" target="_blank">📅 19:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67739">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=tj30hDECYs8VKWeC_kVBlgvbt1uW5SKLFtFEBOy6hGJL6Z9nK1zmdZb48Pl5k3IayN6w0aYvxmoRJaHgUfv1qzPZ_a4tjzeVuZ7NWqvKxOJkSsj7rFXxEUcUbDHQp-ZYCZ83p4TW1pzhX0z756gelIrJ3SBhj5brvEWMvVSYi-50lqEri0U45qn95lWr3ok8euNZd7OdrVusLffi4QHKcZW4K29fhB9j56jMISyjI8lPeUqdxY4OWD90dBG1x6M62b7FllYqC1_W2wr5TpsqSBBTvUoJuU9h42Ys4HY0pbfST4HZiQrgZJmH9vbpztIjJC5tWvxAeRHAkeelEVLaDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=tj30hDECYs8VKWeC_kVBlgvbt1uW5SKLFtFEBOy6hGJL6Z9nK1zmdZb48Pl5k3IayN6w0aYvxmoRJaHgUfv1qzPZ_a4tjzeVuZ7NWqvKxOJkSsj7rFXxEUcUbDHQp-ZYCZ83p4TW1pzhX0z756gelIrJ3SBhj5brvEWMvVSYi-50lqEri0U45qn95lWr3ok8euNZd7OdrVusLffi4QHKcZW4K29fhB9j56jMISyjI8lPeUqdxY4OWD90dBG1x6M62b7FllYqC1_W2wr5TpsqSBBTvUoJuU9h42Ys4HY0pbfST4HZiQrgZJmH9vbpztIjJC5tWvxAeRHAkeelEVLaDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صداسیما:
اگه خمینی و خامنه‌ای، زمان امام‌ها بودن، امام حسین شهید نمیشد، امام علی حاکم میشد و امام حسن هم صلح نمی‌کرد.
پیامبر خودش گفته؛ من مشتاق دیدن اینا بودم و حسرت دیدار اینارو داشتم
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67739" target="_blank">📅 18:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67738">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arjnpsJ5xnsaeMh8VZUga0qPWjna1lZNgCGA3KteIt383c0K0UIJ468YE6bjuCi1sxV8-wuhe-W3IJRSSZTuJl8WDExrcaY7UKQf7W4vkzzyFW1PUsg3z3kQvGjxDd5hjvzDwLkHbgzH3uDvkQO8DIgnCithsrwpjxtDQFfW0R9YxpHw8AZRKcERDYm-pJmnVZQktNmF_Pgt7wOReHdPCZxplea_ppnICoSUYWQICK_DYCt3CLz750uNc0kkDgWnm6ckugaSxhDsgDWLAe7NJjKtJBQ7EmtIb9FcZS87aGVxpGC3VkW9VFj3q5SrjHsA9FkTWYQTizxlrcLuV_AjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران با ما تماس گرفت و خواستار ادامه "مذاکرات" شد. ما به این درخواست موافقت کردیم، اما ایالات متحده به طور واضح به آنها اعلام کرد که آتش‌بس به پایان رسیده است. از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67738" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67737">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU9Sctj167KWL5BeATIl-nk7KxxONOc1wIu5Oev-J3wArbgw7XHrar8bg4kzNYUhKFRV5onWtVYYJcfMlAx-CZiHdA3ty9P_rsZKU2rq8sUbA1wUPzg-TN66JvCOCfnyhIXq4Hwby9Bcnf9S6Jg1-PTZVn9yWa3LF1k7Cac94n8kmuEv4YxX6E8uRN1DfhaJyFkMcKnrGO_lH98agkztuaZ1FvXMconYlpgYLAAnfkmzUnEIabPM3eKTEU0h6wvKRAGwd3wPfqPCyjlFg2SPz3gqaUfARiTnkXfB8z3QoH7v3IncCX8vtvyD9TlYbH2tBGB4yISCul1ayCwzmY_oQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی ایالات متحده امروز حضور قابل توجهی در خلیج عمان دارد. یک ناو هواپیمابر و اسکورت آن (حداقل 3 ناو جنگی و یک تانکر سوخت) امروز در فاصله کمتر از 300 کیلومتر از سواحل ایران مشاهده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67737" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67736">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=DXncxTSH-8v65r55Qpd3yI-ISyhEQm1F_Vlf0pNrfNhm9zdJhLL-YfWEW6hWnN9GwQbFRWKyJGfDJQIWmVWp2LDi3vr0TCfU4zKg02em1KPi1TYtvLAN3sPKHWkk-q9EqRnh28x-8FOEEkw6H0E0vH1FMoNFi4_HuENtauHTl7-M7hl4AWAJ3U1ILz3dBv5Zy2EqrBLlBsQTJdEqE-9MqG2aTOUau-Evb_3FkIrIKVl9I2-3LiZVobZ2Aew_cDpxOJyzAgQ2Tt361vRUopk0qhcF_I6Hhxo5HYRn4lnymRDapNhbe4A6x2n_RdeFkSQbsDF-lAwzlbsZ63aBT17Ycg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=DXncxTSH-8v65r55Qpd3yI-ISyhEQm1F_Vlf0pNrfNhm9zdJhLL-YfWEW6hWnN9GwQbFRWKyJGfDJQIWmVWp2LDi3vr0TCfU4zKg02em1KPi1TYtvLAN3sPKHWkk-q9EqRnh28x-8FOEEkw6H0E0vH1FMoNFi4_HuENtauHTl7-M7hl4AWAJ3U1ILz3dBv5Zy2EqrBLlBsQTJdEqE-9MqG2aTOUau-Evb_3FkIrIKVl9I2-3LiZVobZ2Aew_cDpxOJyzAgQ2Tt361vRUopk0qhcF_I6Hhxo5HYRn4lnymRDapNhbe4A6x2n_RdeFkSQbsDF-lAwzlbsZ63aBT17Ycg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو‌ ای از صحبت های چند روز اخیر ترامپ که در حال وایرال شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67736" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67735">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67735" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67734">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mwK8-3gTYdgzHS2ru9B3_LVT3Ve0txOLCGjPzsrzXnFpEE50OI3wOo1WFeGduqkWX3bbMZatGmvGWJwQMhjCE8gK2VNN9eT3ei-IXYSDcIfAP_RRgfUetJkzmZco9MRm2Txt6A8bTItMx9fskj_i3Y7MDmKTw22_Wb35ggcFmfH-PQdkexgi2Un8f9Tm4G3cX52f3kFTmmIt1F3WEDnZwC2VZMuUBSRjKvAUPRbl6ASsI9pxEp9Rdey8ZCeRuZIl8ZWBKrd30Mhew3PQBOmfVfX1nlFNdIZ8Iwx1o62IClsLawOGcL7-TEgkO10BMGF891RO4T1PJaaZKsTfoHbYuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67734" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67733">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=l-mChTT0vnM23FQLByUQXnSXx2e1gpMfnIcno7il4NNNN4yaggBwN0J-RDPyLKUEO378Eu0nWW6r8YqULUvvnUVHrfuoz2pZg8K4fnGaEp91Jbdc1VSxzElBN4WNKAn2y3jrSIcYah_brPzo43YLMmfPe3c3iugS8sORmKGpFR19SMoVYkBRLNCFcGns7gkdAnK9EBY4rvRVq9vvsbmySc_PT6W2iM6g4703DEiI_nOm4ns9OWMDorKIDU7IE0KR4pk81rKluEyijKbsL2kKygDFPMboYx_WGmGKPIlcV9rn4L2ZATh6OYroxUGHcFEHmLuMwYbfPtRQtyx5DFxsSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=l-mChTT0vnM23FQLByUQXnSXx2e1gpMfnIcno7il4NNNN4yaggBwN0J-RDPyLKUEO378Eu0nWW6r8YqULUvvnUVHrfuoz2pZg8K4fnGaEp91Jbdc1VSxzElBN4WNKAn2y3jrSIcYah_brPzo43YLMmfPe3c3iugS8sORmKGpFR19SMoVYkBRLNCFcGns7gkdAnK9EBY4rvRVq9vvsbmySc_PT6W2iM6g4703DEiI_nOm4ns9OWMDorKIDU7IE0KR4pk81rKluEyijKbsL2kKygDFPMboYx_WGmGKPIlcV9rn4L2ZATh6OYroxUGHcFEHmLuMwYbfPtRQtyx5DFxsSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇷
علی خامنه‌ای،22مرداد1397:
به طور خلاصه در دو کلمه به ملت ایران
بگویم: جنگ نخواهد شد و مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67733" target="_blank">📅 17:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67732">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiFDIx6SIWVbqqTWdPlEuWDK1EgV9eIIKw5LqkDp1l4UoE0vmb06414c4JIwNcqYOzEu0IEtEiZKyISeI0Ti6qwoDzlI7XhN6Hh_UfrHmGofkqYsVcHdCtSjfAl1fVGZNZ1vxq88BKbDiXhPOmoOfStHm2TIILRtvYOB3GVD7dQuVcfknJf6DoCrZJQ7jFOauv9dfuTFlX6ktm-9nA8QecvsVzVHn9ywBmpZIsRw3ryjUH8ZFlncEG01Hh3JMyvP5fR8G2RVFhryBqtrpe4o7iihLeCjKFOsNuFcUVPGKBNxhPEgHo-a7qVy6f9GczmB5CGuiMQu1dHgX36v63GHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کارولین لیویت سخنگوی کاخ سفید :
جوون‌های نسل زِد که از وضعیت اقتصادی و زندگی در آمریکا گلایه دارن رو بفرستید ایران خیلی زود قدر آمریکا رو میدونن و زود برمیگردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67732" target="_blank">📅 16:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67730">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY1i3-zYKbvImSsuNGFBGq8AKs_W3ir6QzGRuRbBdHImZghylSoat-5jMd7IIb7sRnOeqK5nt5sy7MiJjpnYHHEZt5NuvHDkoqpo7Y-7EDSgsMzzn478Pq2VQzv-Uc4soIIvRPuNtxg55Jcag5z4bWtBzu1uaKbgHGdtJ7-h5AR0KBV4XRFWL6H5DhSgBbB1XGvbldcKLNoXEZa-daIueYZf-XJa_c1iwh7hAcD_hgLotEXMsJgg-SDTsrShKBIcEICbNICejQo1ad2hVi3AIcEo587kNv9hxoZm3X8VAWmOD7X4NwFI8BGnFQ6A50i3muXQungJKNB3vcsmkJpBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1372691bce.mp4?token=d7mYwhKAtgIVFCD8KFOA8LY8ch1WrBQ-Q0jHUTGI1XEwqBZMzv0ikvLZzTYuiXU_mUq2IXsYaI2NiLcDotx72dg9xJ7l54cxw6i8Uc56yi1nEH-7LmKQoD-MvMjeXMw5SCiYDcwtvD8n3YWRCT0wXMBaB1R_og28xm7vW4vpdUF8hRZ1kRzZlEkjo36IEaeLHdejtFSU3zaDpiOW42Wuvk4CM4ruxeUTptOUPhwxUZ8cY9f-gY6oBpAUSLEu6-D7tMkvaKlyEJktnU6P9FTfQqy1NFEEhUPYqN8jxamZ7gUb-Shcd4fSiTbPv22rOjZmdFjueynNjp_hE6IfrAQq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1372691bce.mp4?token=d7mYwhKAtgIVFCD8KFOA8LY8ch1WrBQ-Q0jHUTGI1XEwqBZMzv0ikvLZzTYuiXU_mUq2IXsYaI2NiLcDotx72dg9xJ7l54cxw6i8Uc56yi1nEH-7LmKQoD-MvMjeXMw5SCiYDcwtvD8n3YWRCT0wXMBaB1R_og28xm7vW4vpdUF8hRZ1kRzZlEkjo36IEaeLHdejtFSU3zaDpiOW42Wuvk4CM4ruxeUTptOUPhwxUZ8cY9f-gY6oBpAUSLEu6-D7tMkvaKlyEJktnU6P9FTfQqy1NFEEhUPYqN8jxamZ7gUb-Shcd4fSiTbPv22rOjZmdFjueynNjp_hE6IfrAQq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دیشب تندرو ها داشتن بر علیه تیم مذاکره‌کننده شعار«مذاکره با دشمن، خیانت است به میهن» میدادن که مهدی رسولی مداح حکومتی صداشون رو قطع میکنه و میگه بگید«حیدر،حیدر».
این حرکتش باعث واکنش تندرو ها توی فضای مجازی شده و گرفتن روش
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67730" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67729">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nym5BvM3Qeb7xOhAmK2uJE0QDeWOiqxQGqYzgyigFMn9OpJ4IB268-Jyaq-Vd55eGGoRl4eTOTsnQ_IIr33_S0iaRP27__OwrEv0q_3JVdzh_Laerz78yxb2EMKaL0zMRTFE_8OTEzBkqvuq8ud8ZX7FOihTEAvfkpHNfiLaPeDLRrQL2Z6UHgeRpYL57RAsmUcxwR2Jw0n0yRSZdCPFpV_JgKDnsaqqO2Q-eJyR4qdOrJKcjGAtJYGlMHXcC1mFYMpI5FBCauH-CchCZwRQ3QEkzN_IFjs7ZIphkEXA4X966-88tufCvYoESivyJiuKtQUZOkYGXpkCUdCPLZykSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده(سنتکام):
❌
ادعا: رسانه‌های دولتی ایران ادعا می‌کنند که عبور از تنگه هرمز تنها از طریق مسیرهایی که توسط ایران تعیین شده‌اند، مجاز است.
✅
واقعیت: ایران کنترل تنگه هرمز را در دست ندارد. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از 800 کشتی تجاری و 380 میلیون بشکه نفت خام از طریق این مسیر حیاتی تجاری بین‌المللی کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67729" target="_blank">📅 14:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67728">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GSINzXHWjiXBv9HILfg3vtgiwshkCcL90_R-gn5gS-vQije_M05oDf8vW25PoIQh-CyVJS709L-rusGHbyKOmdeKI3ttAyv8245QQ9LH52NR7DewseTjEf81RP1Qw3TbVMMR1uLlpwT0QEBn2SgqXDXhtocFQVPvOQ1exNWiNc7IbpeE0OnJCGjVJJgRnGKcRONjyhQD_5DB-0zgI_X19Exwe7cMlBM0_BdIC7OKZU4wE6Wr2BP62ZsAaU_3ZHR9-eZj4HqVOFeIUNDAnZB6yrdVky7pr3dNNRDHXO9I4j3_r96yhrhx08u01a51JazoueI4-MVfMwdnbW7n1LffDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام سازمان سنجش، رسما و شرعا امتحانات دانش آموزا، بدون هیچگونه تغییری و طبق برنامه، از ۲۱ تیر ماه آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67728" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67727">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=Fkv16TlXLDrSQ1oRX1jP4wkhZtXUSibgfYSCBgk06Iebb886OXF5_7oEBwducTvZbzjqvChUMZhzWxZL0R4F-CIS4scOju3JqwV5le3M2BdDvy5_Q2VtpIf7sgF18K9qDvshT_B34HHR605h_tGcB39KnQ6sI8Sb9x8JhYADAl1rUAkDgmDC0e7p-baUIXBC6HceamQ6OeZLiDnG9HcDVfc3qfBK51KhaqwVTytloKjcBYW8j_90GaZ-i0MBQeuHZuRVTtYyNkGm9NqHrNpOO4n10D4MFKs7Jx8AfLerBFev5de4529CyRQwUBGPodn91zRRl2ED8CvpxyHdoqT48g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=Fkv16TlXLDrSQ1oRX1jP4wkhZtXUSibgfYSCBgk06Iebb886OXF5_7oEBwducTvZbzjqvChUMZhzWxZL0R4F-CIS4scOju3JqwV5le3M2BdDvy5_Q2VtpIf7sgF18K9qDvshT_B34HHR605h_tGcB39KnQ6sI8Sb9x8JhYADAl1rUAkDgmDC0e7p-baUIXBC6HceamQ6OeZLiDnG9HcDVfc3qfBK51KhaqwVTytloKjcBYW8j_90GaZ-i0MBQeuHZuRVTtYyNkGm9NqHrNpOO4n10D4MFKs7Jx8AfLerBFev5de4529CyRQwUBGPodn91zRRl2ED8CvpxyHdoqT48g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسِ تتلو تو زگیل ابدی با یکی دعواش شد؛
پسره هم وسط برنامه خیلی جدی بهش گفت "
برو بابا یه ملت روت شاشیدن
..."
+ ستاره همون دختریه که تتلو تو ترکیه روش شاشید!
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67727" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67726">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcE2DmEE7-2L3zCd-46AwvZxBohMFjw4KPq9bGeGB5SmI3XxxxoqIWNTCpM055GvEAYn_LShHVbjLk0gFhvHASbw-uG7d-sJhUs8hV4SpcNsqbYi2K1FsUkNmSMPjac55Dl7F_qP4PInaW8q4OHWFC1a-8jdDp0rgFkg2IhoboYB28PPxwYsQWRKVeUN34m85TAQ6sVs5KmvnJOhwa8AwLEIQD4uFM_8Hq5Af-Pb1FZ4T5HFVIzQxsaWt68hKAOrBEWvY4-5e2tEtUK3ZNhXNTuE0TRE3KkOYGpfnfs1pT0sUJZVBf2iyDMPEnOdIbBIlokKVlfT_3NT0PBGtec6CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
زیرنویس شبکه خبر:
آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67726" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67725">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606bce162e.mp4?token=MjMF8fACwKSr7-7xnwtjYzrcMhBATpXruoJrOFEsxvijebijVWyuNKXg8eCOwHFvvGJKf2DM226XS-KB3Nf6g-JMq9OtjhcnOAc1fesDS4N1UCo93RWXevC5rnOL6ea7RHZ9zpiTj7acNpuohf7BpURkcAdTFxwA6SdyJ-6tBbRIpEDSQU5gxKp6LNBgHTOWFSuOQ7IqUVzjuWb0Uh9JfJNys6bgnhQ4jzgB1Dhbkn1OL_69V7KabBBTdbI5ud8x_TgQY_TWET2-STXAR56_ShRiqbQ4JR2uUeIcV0kB5uNtnY6XYmtsSyjPCsSLG0bP46jmxWOs9uZ4WEPWTczjNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606bce162e.mp4?token=MjMF8fACwKSr7-7xnwtjYzrcMhBATpXruoJrOFEsxvijebijVWyuNKXg8eCOwHFvvGJKf2DM226XS-KB3Nf6g-JMq9OtjhcnOAc1fesDS4N1UCo93RWXevC5rnOL6ea7RHZ9zpiTj7acNpuohf7BpURkcAdTFxwA6SdyJ-6tBbRIpEDSQU5gxKp6LNBgHTOWFSuOQ7IqUVzjuWb0Uh9JfJNys6bgnhQ4jzgB1Dhbkn1OL_69V7KabBBTdbI5ud8x_TgQY_TWET2-STXAR56_ShRiqbQ4JR2uUeIcV0kB5uNtnY6XYmtsSyjPCsSLG0bP46jmxWOs9uZ4WEPWTczjNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی مجری‌ صداوسیما برای ترور ترامپ؛
نگوزی‌ داداش.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67725" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67724">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
⁉️
تسنیم:
مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی (ره) حرم حضرت معصومه (س) برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67724" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
تماشا کنید: پهپادهای اوکراینی شب گذشته به ۱۴ شناور در دریای آزوف حمله کردند، که شامل ۱۲ تانکر، یک کشتی باری و یک یدک‌کش بود.
از جمله اهداف مورد حمله، تانکرهای روسی به نام‌های Chelsi-6، Aura، Sana-1، Ilya Repin، Venus-3 و Penelope، همچنین کشتی Mercury، تانکر Galasar Kamal که پرچم پاناما داشته و تحت تحریم قرار دارد، و یدک‌کش روسی به نام Alfeo به همراه بارج Aphrodite بودند. جزئیات مربوط به پنج شناور دیگر هنوز مشخص نشده است.
در طول ۹۶ ساعت گذشته، پهپادهای اوکراینی به ۳۵ شناوری که به "ناوگان سایه" روسیه مرتبط هستند، حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67722" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I8GVgR-PkEaS2n0XV3T9bPfzcI6VgdvWANya3Wp1NhCNepDuAxS3trn2fQtixXr-rLwPl93WpI1WYfEN7GvrFK-cuJWhHetjAyUpzYZnhG3Yu16mqqw1Hhcx6Xrd46R59UTLMYJ4gOM997GNGsjXNw-XGHqU-5tc_UFgasNt_VbUR8fnjYktuJfCHSZ0BpN3wLmS9UsbWcmpxHlTXWnnahrEd3fXp8a6noB6lFoBB9jXsZvWAy3AdDsHX4tyYIItzh58zgCwqE1Sbftnue2bXcR8zvURvRRKrRaK9uaZsr0WXbH2nUQrVSHN8GQSm4pPYh0BqYytSB1F25eOE1zLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nU0OFW04Qvkp09Rwv2iCZHkC61DlSr-N9Qd2tRlx7UwK2krnmAyZ5NHZHqyNIQ2cv1Dhb2OkhH9oQyZDOqaTb905JHIsLmQEmiPcuNMrV3BXPEUyhRZzgTpRn60aRfH4MDZncwEFuKvmRTq-6SCX_cl2HyXG4hxiVu6eKbU_jjT6NAcpt0QQU25Z9Tefl5fiR3TusrZ83-MyzJe9Vp1FyzkUuFZ9mh2A_rPCMpTdtcDkT-P50wUSNb4i9dhFgK4fuAlsFuMfiVfnzrveeC3O8OrmhKUsZ0XwKjfKh2wE5Verf7wi0YkSBGkLJlaXxNjL5eFnzvHntpuPsLzEcVayqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LAkrrANTlQRnzVhbxsq_1-Sz438ZuMl53EY6Ocz1xgxX2tO0j4d725Ha-jaK4izyloNwDT0cJnAszkKhVahpD7_-PRDg_fVcAHGYsDM6DzkA1HT0hjMCvGyleGAp4yQrs0gSI9CXuzyC-m1WlgZeFp_icqDtapSRLb9NpHJA5T4UkNLkkp2p2F7tgOYoFN1Qlw1ZsvM0yUwkFm0RpkUVMXjm09eUFxYdTfclxfJn66KO3bsQ0hVPMLPlPoFNn4-qzQ031-ShaEX4Z2HRMVFyUSf_EwTfqPA0szcEyFtWS7lu46NIj0Or9JVM9tZeoRICnMRn0h3xo_OTOVfugccrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gcOnc00i4StZlqZmhiE82MhTIxjYnzNenyASWmH6AoiBAOmGBSZSMLgB30am2E_tV8jmjqpcw4NHeSxP8CCsfJf1dmXPwwuC9K1A_Ql-gvcXg1zWdrs8-QKfOZqawSw-WJU0cbWSp8rXQKfXurjA01JCT1uTntiICWVhMAZjVbPWgrvscb_s-qgq7geVbsyZ7v9AAaWoLtcJWcu-MXTZ_QxR6UMfir14iuSqXrr8N4Xy3OCnmOc9PyzVZqBvAHA_SHlD8YU-4oF6yf7PfHACCA17HAZ9lQNNj-bMrJY3kAqDHAzkpTNwMxE5cTShU0b_yuT8vp-yp_SCyE1BBVFSUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_vbG2i5fBqeqnb0XBBKK6oobJdSK-PdaKoqWIRktCQU0sqpaLurmUD0FM1Plk4hMEmc1RwSqsM3e-1ej3RE2YqHIqzslM2yHk5_zc8jzBoIe-ObOtsYmFlJrdG9ATHEDwUhixolZfHLrmHP5BVusGkWw61ItQQ32YEf782Gap-l10Yq3xWG7rQBc7Wrf9Y56Se0P645qgcnh81tZKqjX0c_Lv_HSvJfKGJVvhPPIfBmlK147xp-yexA60T0pLb9srnnNQRlO9usdt8Z2yEQNZDPYo8uuUotU0O4QHw_NRRrQX8D9BcH9RHeMniWKyXRs0yag36jljCLfeCNxXLpZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9U6aW8Yh9RNWR95fyHbDBJ9k3gAuunt6BSBSc-Bhq5XKmG7XmVtpD2_K632p3zokMuxI9kOb8NreoGbEDzuhcD-hhmi8Et5FHVvu57g1BlEGLSosCAmtWjgldsFQ1bDgzxnR1fnLJnM_bIw7vuDceGHt9DXD3_Z7J3XX4DWB0yJydFJTGb4UocNp137OcGpIsIDfvAk5Qv20Oe2IFQrk7vke4SJ3uSF-m4Dzh__qMamJcXy7kzdEXtk7tgmK3QvFnvg120PzvLl6l8tHEuzlUw3AST_cjoG4_WZCLjub72UVqPnHodhOndcoRx_GtwVY-L71worqaTjCYdIXNc89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=TuBML74F26B7fXDtNfN4GrkG2xFlCTgREf9hFCNbKqA158OuAhPIbyaC9tiExEWwGh2QAOYYgx3f1F37mUzglxw4pI-lCXt0ipFCatM-YOp72J7DaKH4JmDRGLz181XRXeGFhmEoumPx9WLyVeaTaglblMaoxpmN8EFdk1KD-IxjRcg5L4NLG78oUB7ULFLlGuXVbOLNDsIbuhmnP0ivy9GXK5XyMKuD4kHGtkTP9Tr5pu54-hSqMBsh6NmDH-u_Fowi59e77zlzsAuL59NmrmX7UmhtKPE_GWLAM9lRAErFEk61FuR7dbTHs7HFrLTgd7tA8x5L55iGD3nO1h0GPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=TuBML74F26B7fXDtNfN4GrkG2xFlCTgREf9hFCNbKqA158OuAhPIbyaC9tiExEWwGh2QAOYYgx3f1F37mUzglxw4pI-lCXt0ipFCatM-YOp72J7DaKH4JmDRGLz181XRXeGFhmEoumPx9WLyVeaTaglblMaoxpmN8EFdk1KD-IxjRcg5L4NLG78oUB7ULFLlGuXVbOLNDsIbuhmnP0ivy9GXK5XyMKuD4kHGtkTP9Tr5pu54-hSqMBsh6NmDH-u_Fowi59e77zlzsAuL59NmrmX7UmhtKPE_GWLAM9lRAErFEk61FuR7dbTHs7HFrLTgd7tA8x5L55iGD3nO1h0GPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrCRXI5PfVreUc8qN0vOHQn_j7sQgZxsSLchb3m31kxf4lz5BjlV968UQI9Q92Sbct0HEJzpjo710zXNchU81orQLhimgX_wRrU7-lrd13EH-m4RRmNXBm9kJpZHBnUtVYeKXsLd0qNIxJCEVW0et_xGMGh9p2PodeQEwt7wJ9QNh5UhBt5WOGzTqLFQO7pw5ANh7qVqevZC2DjaJjeWONWh6SF_iGVxDB21OpI5NvvQxskvoBAqbEW22ztx-mgwlq4HgkjyITb-iXccco3ytMFob7xCB4c1HaobcYyPx-deXk1pex4ED2csvEUMgRryV_Olm_K9ZM7yHcOhObAL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون درخواست زیاد بود دایرکت رو خالی کردم تو ربات ۳ تا پک شد، کلیک کنید
💦
😁
🔞
🔗
دانلود پک اول
🔞
🔗
دانلود پک دوم
🔞
🔗
دانلود پک سوم  @News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k60c6FHUMIC_Z4lPEiDqPLZL-JKXrHbm6tKgeCDDGjjdIpSlC89D7o4rZkYexxzsnklhANshllssqOK_cude0lkQXy2fplgrqZrr-fVPkQhC0E7Y-rScCErw4jRqyo--6ZSFGMvcdCZ4aNsfDEHD8FalQLLj-ZIn1ozBp6nNmfNBzHnXXa3TUXkiVXga-LtXirDYS8j_Qh_99QMOIpPhhmVqyOz_VCYH21Umh8dzlCmNGfAZvVLadY7eqln8T3qsToILB6yAe86Bw9UCGfumdPiKzPbL_FNihxT4e_gsfPc385tINY0lp0ZNUYcJXhx-feExRzBpItrFweuJzgtZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UM12jZlX4SYydD5vd2CgTubD5gU7CNhC0oWsE1Ru-ZOnWyYxJxhYtWnF1JxX5txliF30T5ymPlDV0eBy8RvtterIr4Ey19HRYuj6ueISgBuL5BZBkYtZiaLKd_C7H1kjtWWl0mUeCCrgOW9lWHilSKc9JWj4rW-rLkpdC_zoVnTnxnCQHk9VyjGEmv7ZW_YpI2pU8UMf7l6UUkNDz0cVn0m2igqgfn_KqZpR94brktT27kwz0CsDMxlnz8cuXDpXNgoE_FlpL-gtPo6BuL9WLQttTlMgXsRQaYySsrS_dAzQRCSPiRbuswkvs5H66PbSZO1t9GXJy25FxWUVDhtF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzEHodKj_vxpO5UN8BTki_LCZEoj1TKdNoZop11LA9xmeN9mfzoTXjHBevjvRsGL1EB0k0_cpudy_uiLw93Rgt8qQZMicBGB-T81k5CSOIMuE9Ye4gsedDdNlXD2uiiDNty9v_rg0c1Ot6uQrqp0ANk372pqNeW-ZAqAeHu6tXSBqQUz9mFSGuSTfXBU8WKpeBEe9NcmYZ1Mh-6LaJv0TUp9o5_dPrqWz9IgwtiYRpNdU9YpbZyOJoHju3EA2q2-CDIoGLCZnq8f3_hLD3pD9yzr3BnLrT18Ooio9tXwC4Mrc1aDReHkUN07Y7NPnFz0od-AxTSrQPwL5eOS1QXGCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=j3jLiBfJRXT3_OFqP464BHtwXYEcW2dDlVLTNvPnfPLRlyzRLOA--swK908Fo6M_Q6J75yZfyWFvXgLoJCbGd3pTWE92-8Owp3Zej_UWl4Efd87tHVxmuP4-qUE3wFWo6E_ztkBvA0OxZVFfdiARa0l6jQm_OwAbPBHmil-a9lnPFj4As7-xHmT9dKfkSbksc9jHJErPYh53WkDhO_G8GhTXuFoC0jGxBc2MSSLffGl6QwugSR_B4QRa5YQqnkGmfjp5j5NGIgve6F2IEgiJKpdRk5CTd1fn3gbkQAHW43sT1DZNeBdAbOqSQhm9_f3hKHU_Khwj0V5Pyi_B7VUgaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=j3jLiBfJRXT3_OFqP464BHtwXYEcW2dDlVLTNvPnfPLRlyzRLOA--swK908Fo6M_Q6J75yZfyWFvXgLoJCbGd3pTWE92-8Owp3Zej_UWl4Efd87tHVxmuP4-qUE3wFWo6E_ztkBvA0OxZVFfdiARa0l6jQm_OwAbPBHmil-a9lnPFj4As7-xHmT9dKfkSbksc9jHJErPYh53WkDhO_G8GhTXuFoC0jGxBc2MSSLffGl6QwugSR_B4QRa5YQqnkGmfjp5j5NGIgve6F2IEgiJKpdRk5CTd1fn3gbkQAHW43sT1DZNeBdAbOqSQhm9_f3hKHU_Khwj0V5Pyi_B7VUgaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=hf2U14xDZ_vFyPdPa2E-CfdKWGoE3tuBKSZHBsI909MWI5aOiVAuZMeaI4PSWP3Z-r_8NPLmWeTlZ4NMZsfZQ7M-BskSBKfQ6uPdKVf-32k3AnyMY3GhSZ4q1ABDkJwDwVrlHSBEQQtUXfi72lzIYiI8xR1xFJQ3EHO-iOVVEwuixBf2Wz86zQ1rTvLQsxkOHfpVL4KrBELBIoxDog93_uweeixjlV-AI8QT_lX_1EiwxM_1f-sFScsdR4xnAzad52dMsUfgDW97-4B0TC_AaLsyNofMdA4SNLqGPZpkwLKF8DyNeux81afnoX16PYB5-oC4hVOnqFDR8CuBdJf4eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=hf2U14xDZ_vFyPdPa2E-CfdKWGoE3tuBKSZHBsI909MWI5aOiVAuZMeaI4PSWP3Z-r_8NPLmWeTlZ4NMZsfZQ7M-BskSBKfQ6uPdKVf-32k3AnyMY3GhSZ4q1ABDkJwDwVrlHSBEQQtUXfi72lzIYiI8xR1xFJQ3EHO-iOVVEwuixBf2Wz86zQ1rTvLQsxkOHfpVL4KrBELBIoxDog93_uweeixjlV-AI8QT_lX_1EiwxM_1f-sFScsdR4xnAzad52dMsUfgDW97-4B0TC_AaLsyNofMdA4SNLqGPZpkwLKF8DyNeux81afnoX16PYB5-oC4hVOnqFDR8CuBdJf4eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
مصطفی خامنه‌ای در شهر مشهد بر جنازه پدرش نماز خواند
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67694">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=eH7oOhJD_NiX1NzPzX4hQvoTDo73-pZ3_UYdNgkGHDu4U9NT-2qtjcDpNKlrMHvz4-6bI51rCxCxdtFWMe1P8u7ztE9eSedfbE7E_afkOpFA9Ms3-a4q9UE7PiXF1bmb9PxesI-oIxo5JALZOvsENbj3FeyoqlwBNSXRbMIsmDnnpJ5RzVFSzsUUE-cDxoul4Af0cwsj5rjc15SGccsZlDi5uIJRB4_yxTtkxeacJpdJe7A628YG2ILTcUge_JphU6iouo47sS-H1Rq2CLtd6Sfuu1NX2Vn7Y_uuGkzQXIr0N5fDIT-pn3GfdzP0cL3JfEKsnWWD-vQC_RH5HftnpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=eH7oOhJD_NiX1NzPzX4hQvoTDo73-pZ3_UYdNgkGHDu4U9NT-2qtjcDpNKlrMHvz4-6bI51rCxCxdtFWMe1P8u7ztE9eSedfbE7E_afkOpFA9Ms3-a4q9UE7PiXF1bmb9PxesI-oIxo5JALZOvsENbj3FeyoqlwBNSXRbMIsmDnnpJ5RzVFSzsUUE-cDxoul4Af0cwsj5rjc15SGccsZlDi5uIJRB4_yxTtkxeacJpdJe7A628YG2ILTcUge_JphU6iouo47sS-H1Rq2CLtd6Sfuu1NX2Vn7Y_uuGkzQXIr0N5fDIT-pn3GfdzP0cL3JfEKsnWWD-vQC_RH5HftnpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2d1WsCGOwaKog79PN7IXlUIgxHm-uOQ-2k5E5tDufxzIeNUgbzkHjeLFF61kdTVlAUL4ZWTrTnsLaou3sMmu-DfKE_yZaw9_feRBraZ3Cfs36eoPrB28tP4jPC5ssrv4rXf-JtkPxAtGdwt3dtpNX4opVIEFfGt8jyl2EzdeAXgHAQNmnGJCkVjexxpokp7Yr05XGPM6oufFaF5f22j35U7FIz-YFARX5Qc2-jtko-kM4ksKPgQhAZhIfJ36y9JDe7pN8QHsnACLHUGLiWS8VZHy8Sk6fJDnFMhZ96e6oGl_KMh0pNvspQ8B1GKhXCP3Nv5Bz8bjM6tY_ZdB87ihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJlGQtar2RHSby8SzmL_WDz3i43thrZ_XBopwRmLpZiyqJyi6AogzBKeZCLcghSB5nSTpvUPvhmleAhf1F2CRfMJi7304Nhg4viaWsdMOufPIGoAOQGiMK8Z_140t2JiTR42sEiWzxo0zIfzjDhEl-CCU7w7beynFeqzKugD8n7nfFKALQze8HRpVs3wUuxq1wNUgdyC_2WwlMfdIn13X9QpyqsIPXGGL_oXbH6zwvRYUhxT0td3gyt2NX1bcuv642AhTgeAFn7eOxeC9iTTKZpSpKtge3njclbIRj0cACxrTt6eJipIBIi2_V72lWASPjXSPbXpMj71EpuuHUFsJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=S97ha8mUtizjFnkrScMeg5x9wGOl8S_NhxfijgaJhn_g97O6ihIRqaxYIgXvmivCuLVecaMRyK-pFSEjMU-YIpQXlqo3puBbOb_pGUeM79AfmM_1MGB4Frl0DnC9-p5pB8Bg4KWLGq7fSZOWbHATNzWBLNlMUIMJUD8LqiEsYCePHirUL3HYX2Zca7v-3YaQ8Dy6Jn9ofU-nWkfmJpJGitKhZ-ggjWwcXIInoY-JEI4DVTENRJi-9N6_wy_XLfNQk4oGLETe-Mf8gtkw15DVcN-gseLSTVjJDkzFssCyMQuSlFLjoQObt42qeeM67L7wwfBfmM-vlNsfngt6av4zSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=S97ha8mUtizjFnkrScMeg5x9wGOl8S_NhxfijgaJhn_g97O6ihIRqaxYIgXvmivCuLVecaMRyK-pFSEjMU-YIpQXlqo3puBbOb_pGUeM79AfmM_1MGB4Frl0DnC9-p5pB8Bg4KWLGq7fSZOWbHATNzWBLNlMUIMJUD8LqiEsYCePHirUL3HYX2Zca7v-3YaQ8Dy6Jn9ofU-nWkfmJpJGitKhZ-ggjWwcXIInoY-JEI4DVTENRJi-9N6_wy_XLfNQk4oGLETe-Mf8gtkw15DVcN-gseLSTVjJDkzFssCyMQuSlFLjoQObt42qeeM67L7wwfBfmM-vlNsfngt6av4zSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67686">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
‌ کان نیوز :
مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67686" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67685">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
❌
گزارش هااز وقوع انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67685" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67684">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی: شش ماه پیش، دقیقاً همین شب‌ها، کل ایران خاموش شد و تو تاریکی فرو رفت. ولی حتی اون تاریکی هم نتونست مردم رو خونه نگه داره
به هم‌میهنانم گفتم آنچه شما در ۱۸ و ۱۹ دی‌ماه آغاز کردید، مسیری بازگشت‌ناپذیره. ما با هم جایگاه شایسته کشورمان در جهان را بازپس خواهیم گرفت، عزت ملی خود را احیا خواهیم کرد و یاد قهرمانان‌مان را با ساختن ایرانی آزاد زنده نگه خواهیم داشت.
اکنون زمان آن است که درنگ کنیم، دوباره نیرو بگیریم، و بار دیگر خود را وقف پیروزی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67684" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67683">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=UUyK-9OZ9VJkBbkoFno7JyQgG6_zjCTBqvCXxblnIrJ3ZldGOV4aIod05XaKgrUL7PAPncTkhyzmM-kJH0_UjgEJsaZuoJIvpRkbIiJIMV-03lNqEk4D1rHYRvO-4We7GRHgLU4YGG4VU5iNSft0qu8uqca7Tv0Vefu_zrYKBEct3VT9d-SzWK5xSMoFOahw2HL0Gs2-yjlc0Oh2K-xyGNmQeCEnhQIhVcSCiHm1iAiQiZQX1Z-k65vJx-WOLbvvlPnrP1WF2vACdnA6_iFill4QOxJdEq0RrmgDNuNNijgo5McsVz01LNdPMLifCvEh2RpnW-EGmHIjncRPJXPXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=UUyK-9OZ9VJkBbkoFno7JyQgG6_zjCTBqvCXxblnIrJ3ZldGOV4aIod05XaKgrUL7PAPncTkhyzmM-kJH0_UjgEJsaZuoJIvpRkbIiJIMV-03lNqEk4D1rHYRvO-4We7GRHgLU4YGG4VU5iNSft0qu8uqca7Tv0Vefu_zrYKBEct3VT9d-SzWK5xSMoFOahw2HL0Gs2-yjlc0Oh2K-xyGNmQeCEnhQIhVcSCiHm1iAiQiZQX1Z-k65vJx-WOLbvvlPnrP1WF2vACdnA6_iFill4QOxJdEq0RrmgDNuNNijgo5McsVz01LNdPMLifCvEh2RpnW-EGmHIjncRPJXPXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر اسرائیل، نتانیاهو، درباره ایران:
ما به ایران آسیب زده‌ایم و این تهدید هسته‌ای را از بین برده‌ایم.
این مثل این است که سرطان را از بدن خودتان خارج می‌کنید. اگر سرطان را خارج نکنید، خواهید مرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67683" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67682">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgh8BuVEp82FU_-bWE4ZZAnw_1CVaniqm01jmfhEhuQRfifCdZVU7Jjv96Ja1wEo0sQeVammdPlqd7oyuVhaNvydXSrg8AGPqvs6U_EZKSq7eO644MqOLC4Ciz3CBQ0jdEHLzqzaEkMhZnr5JHraz_M6GwgjgccVCah7TEb8_dkERuVN_6Lh_GYoVDSFSwBuxEeIEKuv9Y-AuYkM6fpvSClIbG2qlZEDdLmhY2AxlPrUrbaPSz5X59Dx62zIRoUlUhfsluVU04CobWZNAPpXToYjS7ZIC4opzgaBD_fl6XouVSX5eXsnqEcKc1ooe8GJgjRqw-UpTHI7_tZ-CjAimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو، درباره ایران:
خاورمیانه در سال گذشته شاهد فعالیت‌های بی‌سابقه‌ای بوده است، به ویژه دو عملیات موفقیت‌آمیزی که ما علیه ایران آغاز کردیم.
اگر ما اقدام نمی‌کردیم، ایران به سلاح‌های هسته‌ای مجهز می‌شد.
رژیم تروریستی ایران ضربه سختی خورده است و سیاست ما کاملاً روشن است: چه توافقی وجود داشته باشد و چه نداشته باشد، ایران به سلاح‌های هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKM9I3EDmmy2OY3v96RtaKLlRmf8Ht8YUBkce-IaiTEBdm0HtcBUIojw3hD2n3Zl_xiFmVfqurh_V8H_U88IHec7drQsgKmbuuDRcZMGhqcSOWPrL316V2c5IwM0LwYqj6P7IqY7KnKRmP8vOfR6gOh9v68y4METVtHRV2Qe1kPxnXkAd9Xpx7317CC1Pja0kIau4iMpXw0R02TxxwFyHOZOF0FfRkLHLkDD0K-v165o9ifvOO3ohAzL_p2gB3iix5hiMRpOrRWu_VZedrbOfKY3pe4RMwgdF5y7i1idGRt1JuqdUG5z0EC3WOiYYQjr7gXbGmpeqwEmSYLY1ew7hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKU6jhw0CqeFPBLlnfjNR2BvXO28zWNIQPGr-Y5aLrf0RxVXkcK8PDYHC92BHhSvOMl9V5GMw25o7rmuRA9kyMQzus-zgbyjI-SN8S3oF_x4lgrfcXiIcZjNy4JWrieMEVAuPOUxobAX_9pN-Y1MNClJVR81ecucw7cCbHQnn6fmP4xyOtYPqvCVWzCTUIcobTsamjWu_nMrRL_05v4A1VbB-BrZW2_npRUk0GDbJmmSP_ye6VQkcsnpL5SIpqk76bH_RohXdFemWoN2jNCNE2Wt-5DsZaPkSPk5_8MsI6sqzO0AsFZAmvnuPv2QB0TJJMmWYJJhrXc-c4sFdkFnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67679">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=prbZrpyo_41dzIksKfW-3BKhBPgQGIVb8rDdIOTynO6M4S-zs_-Tx889Pe70A1xISryjhoc7HiLyQ-pKJx7eci5L4EZMFbg5QAr0iJl0TXTwgzKMfPClX1__8ti3T-eEidptv1zi0Slb-vwLkQGUh0A49CGjMyVwjpXMD7ijAuORcwdio1XUpkd-bHTKJvhvk4CBwdYzvV95e0hVA1E3FnTG-CBL_RcDBOKT6OBtSNWzVDxwn7MwnPxlT9EnCKvQSktQwFxoOIy9JvIXbAno6Qi762IbIhg_UknN_NaOc_U6yCH2LzfG0V3W9kFbuSgQD-qpOcggzIH6oQlSlMFXsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=prbZrpyo_41dzIksKfW-3BKhBPgQGIVb8rDdIOTynO6M4S-zs_-Tx889Pe70A1xISryjhoc7HiLyQ-pKJx7eci5L4EZMFbg5QAr0iJl0TXTwgzKMfPClX1__8ti3T-eEidptv1zi0Slb-vwLkQGUh0A49CGjMyVwjpXMD7ijAuORcwdio1XUpkd-bHTKJvhvk4CBwdYzvV95e0hVA1E3FnTG-CBL_RcDBOKT6OBtSNWzVDxwn7MwnPxlT9EnCKvQSktQwFxoOIy9JvIXbAno6Qi762IbIhg_UknN_NaOc_U6yCH2LzfG0V3W9kFbuSgQD-qpOcggzIH6oQlSlMFXsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
علی خامنه‌ای در حسینیه امام خمینی، پیش از بمباران توسط آمریکا و اسرائیل:
آمریکا هیچ غلطی نمی‌تواند بکند (23 اردیبهشت 1393)
اسرائیل هیچ غلطی نمی‌تواند بکند (18 خرداد 1395)
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277d837de0.mp4?token=NZObqVbO03poCueB5JjRuAdOENQQQ6-60N8zQ0ZOo5hf905rPwTF2IMODBxfkVJAVWaEFTbKTf4GGmat6sV1ZWt_qiYCYxuQjfeWuVHoy8xKUIGU0SkizFXAPJxGm5lNS8ntVJc2QN5orJVRCZMkFJZzZf025yiHKal9fNknw1cE0-3Ar6pCKbgcXk_iLf54v-IK-2qNKPhgK1OM3ANAC0LiIGOpH5fsEo73XDhySApDqp7xMH0qt8jt0beVc6174VyuRivNxAHyBMaYrYzyL9UfQd3BRHSvTqcKNTgJ9lUAuLUJkkctnGu_qBDvaiPAJNlFc2uG_7rJumlpiaUK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277d837de0.mp4?token=NZObqVbO03poCueB5JjRuAdOENQQQ6-60N8zQ0ZOo5hf905rPwTF2IMODBxfkVJAVWaEFTbKTf4GGmat6sV1ZWt_qiYCYxuQjfeWuVHoy8xKUIGU0SkizFXAPJxGm5lNS8ntVJc2QN5orJVRCZMkFJZzZf025yiHKal9fNknw1cE0-3Ar6pCKbgcXk_iLf54v-IK-2qNKPhgK1OM3ANAC0LiIGOpH5fsEo73XDhySApDqp7xMH0qt8jt0beVc6174VyuRivNxAHyBMaYrYzyL9UfQd3BRHSvTqcKNTgJ9lUAuLUJkkctnGu_qBDvaiPAJNlFc2uG_7rJumlpiaUK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیده شده در آذربایجان غربی.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=Q0SVvgdBkYBxnuqmGQ-65W9Sid33oEsdISYjAvsENHLGqUmQo1MlH-ULp2fon3v9qwMEnmiP9bQfvPj-5JXeWPvX-DIgDNZV5do88aEfS4oFnNSoqVLduLoFNhMOo7C3A0pvfQNgHLcwKUAtdqH7Z8spDhwroTY919jUJOB-YAd2NyP2-Idr2V10m2rn3u28a36xvHg4ll7bV6XO2tfTR0JBtR4K_YIan9ai-y0Pad_pNpgCMXiZsoXKIXjvp49Phd00Y6Z9VVji2uiamcmMHW1beaSn7Z6f9gbP_ytheQJgczj_nNPM7fmZ5xtW5h4URcWr7U6YKvaD6m8CnAJpMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=Q0SVvgdBkYBxnuqmGQ-65W9Sid33oEsdISYjAvsENHLGqUmQo1MlH-ULp2fon3v9qwMEnmiP9bQfvPj-5JXeWPvX-DIgDNZV5do88aEfS4oFnNSoqVLduLoFNhMOo7C3A0pvfQNgHLcwKUAtdqH7Z8spDhwroTY919jUJOB-YAd2NyP2-Idr2V10m2rn3u28a36xvHg4ll7bV6XO2tfTR0JBtR4K_YIan9ai-y0Pad_pNpgCMXiZsoXKIXjvp49Phd00Y6Z9VVji2uiamcmMHW1beaSn7Z6f9gbP_ytheQJgczj_nNPM7fmZ5xtW5h4URcWr7U6YKvaD6m8CnAJpMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=o-jMa56wWK4gjyriyUVLMtVEy81nF9nLGGCs2Qro6tKzgfvdQEHD5UxYguugCoZEi0U1xGvpoH-vdkSDZIpEOz1LNjlt1fNHj4kYXof96VijDUbtAb0krV9HAoGWr-iSBNa9nO8ltZlBxgyKiEYQd7UXzEHCZY2KBZqBIMEzx9GeCk2WoUIzcZF-WPTY09Lm_BgcTVXiNzhWzZUWAfLtzCdOqe1GO2ZEg0SuGJVYjbu3-QRd7V3wD_O4gfAD9dc4mJuKBU6v8YSlo0lniXbnNlgTDbhUWcLAxK2BBHbCBsU5gUKsc6PjzwZA8DBWYRybXvQFvOqIuOg3knalT2JCyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=o-jMa56wWK4gjyriyUVLMtVEy81nF9nLGGCs2Qro6tKzgfvdQEHD5UxYguugCoZEi0U1xGvpoH-vdkSDZIpEOz1LNjlt1fNHj4kYXof96VijDUbtAb0krV9HAoGWr-iSBNa9nO8ltZlBxgyKiEYQd7UXzEHCZY2KBZqBIMEzx9GeCk2WoUIzcZF-WPTY09Lm_BgcTVXiNzhWzZUWAfLtzCdOqe1GO2ZEg0SuGJVYjbu3-QRd7V3wD_O4gfAD9dc4mJuKBU6v8YSlo0lniXbnNlgTDbhUWcLAxK2BBHbCBsU5gUKsc6PjzwZA8DBWYRybXvQFvOqIuOg3knalT2JCyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddbrlbApYBivDLtQJlss7f1Dj7FFLQUIFcERqJYYNOG0IfiGfhMTH25VM423KnxzUDb7MLZ5Jm_j9za_gNzXlKR7rUac7IPR4CNgi6rJh_VRqwuyPtf62cpKWYy4D7ma0TOfbJbjA_aKmR7LA1OXlFChZNNm_huG0p-t2YYUyUr42NpgCd-mVs4cv-z8dbb9C7ZOVzv8k1FKzxra3zSkPkdPXU7ju2QzRG1BMk0o3vjze--USJ1HYfyxglWnoy6dKpvOefwVKGOJL5KxtDbva3mqiP_IO1sReMJt_ag93503J88E_PzkUBRadfIFKRrIbJgOo6fY_qeNRXDHmZmMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=JWYOuFocpPnwh5a4EYa6RMcReT4HjBEzwjLDHA-0IFAqsqw01Olk5pephf5bpcDm6xgLfGFLe-0wdcPoq_gX766L4VrgpUQwWscaQKwHbB5byiGcN0UZSM4sBsX-RdggvMfOmAr2vcKitdH83J1uq6GGyr4HeO38iiPG1CTJwZpCgja_m25ELB0VYCj7kf-W7hnq1zQRog40ydrSEYvKo83fd8UuRsdw-2kBpLOoPz3YCcnkji_1CC1GGqqXttFIvIj_kZyE3j4IDuEl_UW9iW9XTbCbwNT0hGHyJG4yvmzBU_hdBoColnyqlq6qah-Yhn5BOlgNTls2Rp4Z2KgmhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=JWYOuFocpPnwh5a4EYa6RMcReT4HjBEzwjLDHA-0IFAqsqw01Olk5pephf5bpcDm6xgLfGFLe-0wdcPoq_gX766L4VrgpUQwWscaQKwHbB5byiGcN0UZSM4sBsX-RdggvMfOmAr2vcKitdH83J1uq6GGyr4HeO38iiPG1CTJwZpCgja_m25ELB0VYCj7kf-W7hnq1zQRog40ydrSEYvKo83fd8UuRsdw-2kBpLOoPz3YCcnkji_1CC1GGqqXttFIvIj_kZyE3j4IDuEl_UW9iW9XTbCbwNT0hGHyJG4yvmzBU_hdBoColnyqlq6qah-Yhn5BOlgNTls2Rp4Z2KgmhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YR7r8R9zl_ZPhmKJx5aVoN8Z5gcDNFcOVNUi-G_dwAM3Xu6_1yoEsFEsHQx0QyBANxy201-mmCrY89urw5yLXQM2CQyMDgsXbZ0ypgl995ZbVp5z5wupBT7ciNB-8Nil3sFWYDpmbrc1iN5ojX-k3j-jJC3oV2XZnJLqi8atMQA_ftByAKsH9dCvxL0sA3Xa3i4MoGYN8e_tD5NonL1FrwHuCK6eG9rVifVWvcM35YxRY2P5WxAoTaVf4rOTz7OsjWeDzsmyDoiRFCiWknwMpn6QHChsGWsRYWX63_lJLSj-Nv3pN3kFl9aE6q5Hm86_RDiVuY30OpY0TIui7AJgdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zqqppqa9gzvl35lNh0rPBEDRVn3h0LEdA8k_Y6MNmJhnUTx_l4hGr0QCZw4VzbTHqXYSGoWb1mbrX0p4EvPUdAuxz8RafFrsq0gWYtTyn38nDDzMOwP-lhVgankQh28ktZiDlWj2l7oRkTul7cnfUjYsHuU11h5BCZBA7uhI8xqhhzPGfi8_2aYzf1I0GfXmhs3xEXTQ7PB5JmbuK-QJwF9we5s9Q_abCaWJDlW-L0qlOxdXY4gEMJVFDsFzNDX3QSfxa3OiFXRseMS8KLJkpSDlAbG431vh3FkbhBAqx-r2Qszb1lFEUVvUM6lh3rLPyh1zCl11ehTdH47yClPdFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFEvnJPcZTdeUx0nNxywErueOdnjx2S18YH5D4m8bgm_BKe-WUEgw7MBqYWDC_wCZP2JgmLYYQ9CLUbPeP_SihY4G9-7MJSzTmSl27DO3-ym9Pgu8_Ub6J74PTdH1wI5uXthMZf1ke1pPUfTZaxe7hsoJeYQv9uydo5OdBOz4xsEsmwliLB_ZfwcvHzXfW86ljnbiHkvwp58_ScECzqoU3phCXYimXmmeyaTFguXAtF6r35l3IdBaAkEgu0AOLDdgCONLrY54QAKuT2wk61OsQoNTSC9jki1NkPIm-E8aKdk1ylV-N9ykvRgxXygvt8mPEs0c47T_oYdiCm3s1fANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWF1-rj-x3cPnkMsrNWyLzRocraxnD_ZwCmMTW27JDs0ABhzLxhqGxg8JRAfb7r_dVGEMgo0OgzYpmwazd_tWVEcVzZWurn6QOYMJ4RG_ahbmpOg6LnsCy29zcodD54YHdqURz-YlH7JzD-bqyxCidU_rUSLJaDdv2iPc0ISvuxKDVsH1lwYLdwhhtYCVn-TRRSh5D5GQE4EpIifKBymIeDdjomiMYUkWnrZsca8-vGQ57BP5KQC94P3rr1h2vOAG8MjcVX8bV_aD0EXWm7wFyy9PIgkKZ12TeBgsdqzLSbRx9cQEuXObQxgmIWuKLjWvh005W7I8KyDWCc91XwSYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=V5XT6qKo2yYaXg3eb-cBnHJgumBDaT21aXFP4LAEqbRmxkHN3zkAaRs7scdf4MX8mZYvMueyxAZLfddWK0T5icmzVP6aNaCtlOBSFJDIcNcKx3hGtiLLkeSC7MdX8jwTKYwMfUamRYJXxNvfIaq75Cgv2DHIbjgK5iRQOCmgXNKsE8uX5sfnLf5IP-dz6_jEZeFYBMHXYlz_c9iEI30mA6dl6lXt75i6Rdw3ysxo8iQbyHpPosR3F7NMKghPpimomW1k9lw-21-ftPEI3MoWvIu7EKgHl4aBt3yXTtPbjoICqaTTI5S4jPlbpsVF8IOcYpID_qUzig8domyMDldVcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=V5XT6qKo2yYaXg3eb-cBnHJgumBDaT21aXFP4LAEqbRmxkHN3zkAaRs7scdf4MX8mZYvMueyxAZLfddWK0T5icmzVP6aNaCtlOBSFJDIcNcKx3hGtiLLkeSC7MdX8jwTKYwMfUamRYJXxNvfIaq75Cgv2DHIbjgK5iRQOCmgXNKsE8uX5sfnLf5IP-dz6_jEZeFYBMHXYlz_c9iEI30mA6dl6lXt75i6Rdw3ysxo8iQbyHpPosR3F7NMKghPpimomW1k9lw-21-ftPEI3MoWvIu7EKgHl4aBt3yXTtPbjoICqaTTI5S4jPlbpsVF8IOcYpID_qUzig8domyMDldVcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=qmhoMSPo1XI782hhDbli8ctqBLUC_gZ30G9upTRQgzy33zsbRCJKdJq6KRFwkMJeZ0_s5Zv4ZFqekZfSosWUgnMoH8ES-tMY1I7A6LMRQG1HzSOVsQ82V1C6CWiX44wyJf9Ip4GWSROHv1UlLW1Ed2YkHRQy2ANWw19dgBgzUSDcXXfeVDcYbtI9p7qpc0zyeLZrtj6vfrPG0M31W2TTFRQyTveA_HUMa8Stqekpf-VXySQTNXExAS8EgIiGR28dNzf3J_sbzyVEUmFg1IeWblIcpHrzvRxlR9iNAzFGewMgVJBdLuoQrJFh1c9RYQs9vPqp3mw6CurhJZfXQCplNw0o0SEWAIiw03ij6qd1C9Zy54nh87PKijJLuQoQVx4GLm2Th9XKI4b4rr0JrBxq7Gi57AjQvAhY9gqyauYxl1mITmjx-9tNPlAThi29slvUPFr0pBSsmO-md6yEyvnrLuX1NpuQ7Wc_bgMMilIqlwaRduPvvZMtO2ORRG4UkNX_yhK7vdkdPcS_kZ7Ceea4oIeupGAO2LHJYCByF48AkEC11bfNO45DvwWG0lHQnEgG8tTEu7RgJ0_52m9X2QTihZ1PKWQxtIeKVj-jmOjH3-MJsfXipMx86RjTozG_qVzhkcEojvV0eQrymXiX1fFZ2wWxBIV3QIUTisIfES7GEpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=qmhoMSPo1XI782hhDbli8ctqBLUC_gZ30G9upTRQgzy33zsbRCJKdJq6KRFwkMJeZ0_s5Zv4ZFqekZfSosWUgnMoH8ES-tMY1I7A6LMRQG1HzSOVsQ82V1C6CWiX44wyJf9Ip4GWSROHv1UlLW1Ed2YkHRQy2ANWw19dgBgzUSDcXXfeVDcYbtI9p7qpc0zyeLZrtj6vfrPG0M31W2TTFRQyTveA_HUMa8Stqekpf-VXySQTNXExAS8EgIiGR28dNzf3J_sbzyVEUmFg1IeWblIcpHrzvRxlR9iNAzFGewMgVJBdLuoQrJFh1c9RYQs9vPqp3mw6CurhJZfXQCplNw0o0SEWAIiw03ij6qd1C9Zy54nh87PKijJLuQoQVx4GLm2Th9XKI4b4rr0JrBxq7Gi57AjQvAhY9gqyauYxl1mITmjx-9tNPlAThi29slvUPFr0pBSsmO-md6yEyvnrLuX1NpuQ7Wc_bgMMilIqlwaRduPvvZMtO2ORRG4UkNX_yhK7vdkdPcS_kZ7Ceea4oIeupGAO2LHJYCByF48AkEC11bfNO45DvwWG0lHQnEgG8tTEu7RgJ0_52m9X2QTihZ1PKWQxtIeKVj-jmOjH3-MJsfXipMx86RjTozG_qVzhkcEojvV0eQrymXiX1fFZ2wWxBIV3QIUTisIfES7GEpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=GSDoQFcge03ewJmT8nq9_vx0ULevD-mF_AM94h2K29FMQ9P2pIVXKMaGTnnVCKFtSVY9OcXSwvT382moYrK_mycKsGznckiSHN1F3JJGvtAX9bcKs7iznMN7B4kebQTHZ0s6HjfBns21Fp1tVkckVrA-VnNUgh6Qq_4ycR7CKMUFJcEUOiwYpDtzTlyoZRlVmaqHvRB-BARbezef-KuBShIj_bu7sDitpXR-7hr-0usRnxeJ8YKJ3d3xVXjZWOZf1sOI5iSwH6MIobNV3z-peyMSfTFdXCO3HayhdW_XpHqikqT_Fb4QuAj03DShk_bvsfzUad614r2LvEx4veuGrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=GSDoQFcge03ewJmT8nq9_vx0ULevD-mF_AM94h2K29FMQ9P2pIVXKMaGTnnVCKFtSVY9OcXSwvT382moYrK_mycKsGznckiSHN1F3JJGvtAX9bcKs7iznMN7B4kebQTHZ0s6HjfBns21Fp1tVkckVrA-VnNUgh6Qq_4ycR7CKMUFJcEUOiwYpDtzTlyoZRlVmaqHvRB-BARbezef-KuBShIj_bu7sDitpXR-7hr-0usRnxeJ8YKJ3d3xVXjZWOZf1sOI5iSwH6MIobNV3z-peyMSfTFdXCO3HayhdW_XpHqikqT_Fb4QuAj03DShk_bvsfzUad614r2LvEx4veuGrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=TmFq_jYcZwDPg4bds0Y3Mxg2OaSVfI6zGIhoXzRYIeN9BHr8rD9mcyRKcqzJkERKZVXMhi1Ba7_t6zypJqLLDj2sgnGOcMgpICvhL3fsYEZsK3AKlvjPHQ6C_gW-ow3EwlxA2lm29yVPUCj8a4v9scrFBG1mfATSREydEzFGROYq4wrPa2v5kVCWIuKoBdAZjsl6IoSmQBRg-jGxwYs5RP8wp71FTHpELFKRq_biSnGEq87zqfas7h-Pi31BpWmQljGVa2E2T8VaAl4WjzRxVmusMIKOfsQXLMcWBQpPE1XuMa2f9LDR2N0lpzzVGj7NmeuoMl-ae_eEAeQM56NFlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=TmFq_jYcZwDPg4bds0Y3Mxg2OaSVfI6zGIhoXzRYIeN9BHr8rD9mcyRKcqzJkERKZVXMhi1Ba7_t6zypJqLLDj2sgnGOcMgpICvhL3fsYEZsK3AKlvjPHQ6C_gW-ow3EwlxA2lm29yVPUCj8a4v9scrFBG1mfATSREydEzFGROYq4wrPa2v5kVCWIuKoBdAZjsl6IoSmQBRg-jGxwYs5RP8wp71FTHpELFKRq_biSnGEq87zqfas7h-Pi31BpWmQljGVa2E2T8VaAl4WjzRxVmusMIKOfsQXLMcWBQpPE1XuMa2f9LDR2N0lpzzVGj7NmeuoMl-ae_eEAeQM56NFlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
