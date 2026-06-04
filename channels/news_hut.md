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
<img src="https://cdn4.telesco.pe/file/IneErGZv4QmiBZWoqkdC5QVDewi_CXjRNhA98r2ou6B8t6Zzo3rYfPodQlbVVtnesRz3XrJQ6X-er5cMu_nUUs_jLnq8qzitOg1BaCX14xfKcIaxbqx187YvQ-E08lFOXZ3KXqqxGg8zj1danBEYZXkSQ9Nm7igGUyY3Ne4QKIDOkkJ0gv9r59GpUwiPLrUtY-tFL0WzD3PWC7W0aRcKkx3DFTg-nOhA4Fhuy6xOBIqZArF5JE4NU-4pnLgi5sH9y4lVBWyWJuQ8u7H_1DrEUl0qB32z80IG5LVBZfuU68NYFMaeTEU0p5SBWnLLJ3ZLx1-yIjmg-17RN4qVcR9StQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 20:17:37</div>
<hr>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt7nduve4exKx4-lsPAwZVO_ec_yezO0Z21lqvcdXt7xXLOPhwIXzfmBJdvjRwG95rhZfAfApO5d_gC6bm3v4-W-OFYHB8bdfqhbL3rXRUzBOHN1QUhkqEe1TYqpRK6h9bMotPOlViZ6gsAbx3TdNYTxJqo7qbApxeY0hZfmh5I5lAF2DFPbAR0znmbYcUzIkYbSQ3h99SuX6S1_Z9_kA_TCFmLoOnAvRXu0OJ4Cn2o5MFezjVE9_18HDzyN_Ca5wlRzCCZqBwoC2Prtys92eOG_pEXuBw_XyA6tUeOiwXprGFSxNve8xUL5ymx759mbBvHbQ_nOYrjVWTvw8P7K6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlWqJHnUTJwIsAfpUOBHQyiFV2V1C_8PcQtZ8KHq6mAmN-b5Y6nlzvUIVVN0TL0JRtH8yjxTH2NIEKVu3GshZMh1oOhc5yqaVZPT_9_b055v4QOCnD6u2ohZjOsLgNWU8EGqFb-rzRqkxxH_9pdlrpr0XvIKDNhMchYXLfkrmHKgPvI8fjQf5x8sMdP1rsLY3zAdClK6ptpvRBnTDpEJoa9INACWRQEcFIOoz1Q8OmzEstyvrPnNocTbRREAEPqba7Fbxa9cddfUE3b4CGKuJt7Jg-7F6G9tByXvOXlWKFrnMW82AHVwAbokZsyCo6sTWTPN_4cJH5ML4HilZE9PRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=p4Pm88pMnIS2Rqqcdg0CDRhtWE3agT47hTLIciGZ6Td6AY-8htw9pFw1ngcD0LGMsa4JVQIINty88bzRzU63WKqol7dpsLO3EQXe62HEz5A_evIrwR5D75CIvoEyMtX7pi_RdTBToo2ySbuPc8X0s4WafbEKR-9cc70AfsNa2Z0we-U98YmFUUK0y6Lh3ZEjufoN9MmF4D0DDmga96uJv1KP4R1nNJarpKTkrf24OD2fNhgYfaxyhcV_sphKYRENsyIjuh2fYS0p44jsgWAjMsKbsMfcsuP6B0kpSuUZK7gMZ05C9nzeVaC_5GDr1llw4BWZMGkhna-irSzU_Zhfmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=p4Pm88pMnIS2Rqqcdg0CDRhtWE3agT47hTLIciGZ6Td6AY-8htw9pFw1ngcD0LGMsa4JVQIINty88bzRzU63WKqol7dpsLO3EQXe62HEz5A_evIrwR5D75CIvoEyMtX7pi_RdTBToo2ySbuPc8X0s4WafbEKR-9cc70AfsNa2Z0we-U98YmFUUK0y6Lh3ZEjufoN9MmF4D0DDmga96uJv1KP4R1nNJarpKTkrf24OD2fNhgYfaxyhcV_sphKYRENsyIjuh2fYS0p44jsgWAjMsKbsMfcsuP6B0kpSuUZK7gMZ05C9nzeVaC_5GDr1llw4BWZMGkhna-irSzU_Zhfmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=kuRFKVI1ubI9vVZ_Dz4w_OUBuKbJDnc_YV4oSUFN6MCWLAvz3QN5fY4t2MzRef4oCIsgdD1oP6cUkXXtCBZqqIsrZTwv3AHTulGbF1Gbrue4Ey-6ihiSAh8XW73EHgB4r2USAsq3vt89Od-lXC-1TGH3MC_tbqE34Q54BkqCR0YA7dm8XfA1KFQkaFjWOrdidKLeBm3Bg2uquJLgcDDATT1X1bD-Z_Rcv2O4p9dan9ZJ47UsHA9lmdnMXsSvOXCgMsYkJUXZdamufERkQa_wsc_XEumu_zIe5yEYuwfZbW_y60jYJdDTA0QQzaInSt74q9gbFCuDF4M80znTlVxoOjqR4m7oHKahVvhP2gqcGoDptuFTMH4zPqRWbNUv9zMlr8AWi8b_rZznhy4lFPN9oRBZMS4R7C4ucnrOzGWHu1ZqXXKq8YlImSXLtdegJkoOJ_bow6WtocoaXzMVhW9rJTia2kOmfTzAQ6-ISc3EeZ35CRs1yl6g4gghUyQ2bM4LXqHp-fodBQ97-3C4tZXdYFbH50S8DVG4zRlbeA8jAg8cilRPQA6MbxmCv9FzC9cRceYgbXKsjpGvTx5Icj4ZhTsTpB9Ta30K29FCZD4vAujAX-carFlPcLqsiKMQRyWDkZgEByETYE5Ep5Gaz36siFyY1T34Y7E6Un9PsbTcAoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=kuRFKVI1ubI9vVZ_Dz4w_OUBuKbJDnc_YV4oSUFN6MCWLAvz3QN5fY4t2MzRef4oCIsgdD1oP6cUkXXtCBZqqIsrZTwv3AHTulGbF1Gbrue4Ey-6ihiSAh8XW73EHgB4r2USAsq3vt89Od-lXC-1TGH3MC_tbqE34Q54BkqCR0YA7dm8XfA1KFQkaFjWOrdidKLeBm3Bg2uquJLgcDDATT1X1bD-Z_Rcv2O4p9dan9ZJ47UsHA9lmdnMXsSvOXCgMsYkJUXZdamufERkQa_wsc_XEumu_zIe5yEYuwfZbW_y60jYJdDTA0QQzaInSt74q9gbFCuDF4M80znTlVxoOjqR4m7oHKahVvhP2gqcGoDptuFTMH4zPqRWbNUv9zMlr8AWi8b_rZznhy4lFPN9oRBZMS4R7C4ucnrOzGWHu1ZqXXKq8YlImSXLtdegJkoOJ_bow6WtocoaXzMVhW9rJTia2kOmfTzAQ6-ISc3EeZ35CRs1yl6g4gghUyQ2bM4LXqHp-fodBQ97-3C4tZXdYFbH50S8DVG4zRlbeA8jAg8cilRPQA6MbxmCv9FzC9cRceYgbXKsjpGvTx5Icj4ZhTsTpB9Ta30K29FCZD4vAujAX-carFlPcLqsiKMQRyWDkZgEByETYE5Ep5Gaz36siFyY1T34Y7E6Un9PsbTcAoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
فیلم جدید و ویرال شده از حمله هوایی آمریکا به پل B1 در کرج
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-XPh0l_IM15R_0h3Qw84Kslmt0VUVNibWhrBr8mZ5iHEDBSSd35pH2zYhSIjhLAlFsrSRabRwGthyBxNMsofw1r2nYWkHtRd-JXEpHNkd09JakrhiIcrQV4TpMyK1lF7D_jXx4dTspQNiV8mPIeyLcGYUIBC3r-Dq-dOW-UW9sxI1QaQB2EWjMGJQnuZpiuU0HNlcSmepiM-mLE7SDJ1VWGgIaYRbl_jsozxJbzorqQqkBaE0oEQceSPlOMy8N7Sj7GF_fIhe73-qE3CmtqwInf9HONtE05aOp89MM4tMl_w1JYFh-zPoR5Q9KkbKL9ujFPKoTI1G0MXhsmUlV9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=iYqUgHKr2IfeX4B5PTHOrZUiZAE930c_t-IluMrx6_yjVv6q9M3029qS30WXi8BFuVNyW07dep-vBCKCaycq6e-0O0PCtmZ5hEXoMWcsN1GunfjgZhuiGTZ6npNUTotZM9yVycdeVKxgud6eINoRu8Li9eZMlm0hrsoI_83lTPCFSbh3ppkO8aO62WkcD5NtWVFUntQGf3rK8b0k-e-SkkBt6DajA4zj3kBlnbYO4FYYc1nS03UqDvpYeVEnwqbdYHvVV8_W8UqFuFjT2Yzx03X0sEILwV3mxjlksPBbNdIFs2ho75m8mHYciy74UzMELSaQAB3qr3i678viSM8w8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=iYqUgHKr2IfeX4B5PTHOrZUiZAE930c_t-IluMrx6_yjVv6q9M3029qS30WXi8BFuVNyW07dep-vBCKCaycq6e-0O0PCtmZ5hEXoMWcsN1GunfjgZhuiGTZ6npNUTotZM9yVycdeVKxgud6eINoRu8Li9eZMlm0hrsoI_83lTPCFSbh3ppkO8aO62WkcD5NtWVFUntQGf3rK8b0k-e-SkkBt6DajA4zj3kBlnbYO4FYYc1nS03UqDvpYeVEnwqbdYHvVV8_W8UqFuFjT2Yzx03X0sEILwV3mxjlksPBbNdIFs2ho75m8mHYciy74UzMELSaQAB3qr3i678viSM8w8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gngehLb536bd5d7zN4l0GqiWdfwLwLV_DvB5zfnH3S3gbLR6gyEg0jg_GYz-2Vv8BEGSQhRs-TXzUI9RWUpYdiYkctPpCWBODGab0jPQPw6P5zGotcrB2cGdrF2vEPavdP0_qCLtwBW0Lo3zlhseq3BIGgDl6yBtGxN74gSh1thAGPHOKxygE62wfbTF8Tny4Um1QrWUDCn8VbvhBcOVIu5QskHkPw_27RRV4BsTZigb6O8EbCwT0gYNVyIxPL8pedVn_fd4BkI02IsOsWQpk4mRvLRL_wGyyMq_mKH1lysVPyefTOYtPeiE4fXnbLCEciVONk00LUB-GFTEjCp0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=ERH5cqv82efEExSUNs1_5cc5OmUKWqf-8yK7f4lJRTJ2MSLlAXxnR_A3r5u-xS7wqzJbY2AbKQiHncw6bAHAGNFGu2EKUqD1czGKGTY21kAeHvzX4fJxbEWFEpjqOtxJUR7EPaOd9sv-aghIZEkj48Vb_iXbfOi4NPWCLxJ5-ekUSWaqECHKb5MOQZru_cPQq4s5iWJLBHayPzPx7XtsjWPp-BMDmrF9L24ODCbdQJKwu1s09Lm96zz7SdENUXOgbC2f9VVJVTvTcidhmQ4X2212bGVSk5OEM7_RtK7jhjgekBJAnVfUbR5gNdqqrPBwcDI_BP34dxqRvHXYVxXdLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=ERH5cqv82efEExSUNs1_5cc5OmUKWqf-8yK7f4lJRTJ2MSLlAXxnR_A3r5u-xS7wqzJbY2AbKQiHncw6bAHAGNFGu2EKUqD1czGKGTY21kAeHvzX4fJxbEWFEpjqOtxJUR7EPaOd9sv-aghIZEkj48Vb_iXbfOi4NPWCLxJ5-ekUSWaqECHKb5MOQZru_cPQq4s5iWJLBHayPzPx7XtsjWPp-BMDmrF9L24ODCbdQJKwu1s09Lm96zz7SdENUXOgbC2f9VVJVTvTcidhmQ4X2212bGVSk5OEM7_RtK7jhjgekBJAnVfUbR5gNdqqrPBwcDI_BP34dxqRvHXYVxXdLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce5X2rIXdp0Ty3x6kiXL9QQelw70iE6pjNynlEBWJ6hZFyWPHpf8KRkqyGfMV1FRwBCtCufvgiRP63PbII_fHPjcznroR_OSrTBRKCbtkBaBf-EAirTPLwkYzyLU7tDDm4LYVHLryMUAl8a5aUoZBxITXp8vhoBmmab0qRHlFVz9v4sVijBk0Ds3RDQHsLyx0JrW-jLW8-HID4RNgeS6VaYOEtHxfozi5gP6CrN5J6dLSwk0SeTgco9INXWgeVDhccHb3V5r5_oORbYmwQ4HulJam3Ri_21XETDZNb503vg_T3j6Teb6UvlSLlyEFfr5m_P6EgslktJd3rMsNWT6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Vertigo Vpn
⚡️
🔥
آفر ویژه محدود
🔥
♾️
نامحدود تک‌کاربره 739 هزار تومان
♾️
نامحدود دوکاربره  879 هزار تومان
💎
سایر پلن‌ها
🔹
10 گیگ
⬅️
120 تومان
🔹
30 گیگ
⬅️
299 تومان
🎁
طرح معرفی دوستان
هر 2 نفر که معرفی کنی، 10 گیگ هدیه می‌گیری!
✅
سرعت بالا
✅
اتصال پایدار
✅
مناسب گیم و استریم
✅
پشتیبانی سریع
📩
برای خرید و اکانت تست پیام بده
@VertigoSupport
➖
➖
➖
➖
➖
➖
🫆
@Vertigo_Vpn</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=GhcgLByLADbWnWwS9l4YBdIaVG-1pLCEPF0shwOkwmNSdE0Xm_iFGKfLS0mWZrd24l_UM_OLseh39D-VrjT2Hn77I4D2Mx3tXo2I_ilJBFTCxGfD5dwG1qfkYEVMek-fygCTdU-OtIQMy37lgl90PaUldb4dmCPtfj8KSJDSbfA0P8JaNP-SoNbAoJYGx8tZHnxnWQBQ7n9eBYUdCT5jJAyh5z5gEx95F-E0QZ9yxEmzfNoMntXfPHTlhMG_KIKQ7jL9IXoW2eEcWSmJQ_DNZeBZ_nGvUygUmdZwySTu-785dVtzGUn330PWQFYfMla1G3mB_9uIwXj5ren2TQzDzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=GhcgLByLADbWnWwS9l4YBdIaVG-1pLCEPF0shwOkwmNSdE0Xm_iFGKfLS0mWZrd24l_UM_OLseh39D-VrjT2Hn77I4D2Mx3tXo2I_ilJBFTCxGfD5dwG1qfkYEVMek-fygCTdU-OtIQMy37lgl90PaUldb4dmCPtfj8KSJDSbfA0P8JaNP-SoNbAoJYGx8tZHnxnWQBQ7n9eBYUdCT5jJAyh5z5gEx95F-E0QZ9yxEmzfNoMntXfPHTlhMG_KIKQ7jL9IXoW2eEcWSmJQ_DNZeBZ_nGvUygUmdZwySTu-785dVtzGUn330PWQFYfMla1G3mB_9uIwXj5ren2TQzDzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=oLlnEW5sBTvlrz2y9sATniQzhJDSZCvvRxB2gNJg7qt55aGFQp1KD53l0h7dxhtTggupzBSt7atM5oKHcuyGNMlLLJdcR3takABNi-nSaE385ygDUyFL8O1x-Sf0vNhyD2_gCCqeKVdWz1nAxoXWUhVJsDjSqeUCEkCOVOJdKKW5pvaKj3RDsa-LKUPaSACIlFkoiu3Xfb3Y2XINaucWECTvcauNfEh2fx87F6rwnkIBzPwkNwRFTE8Lzw2tjIcfLUMS-a3PZJ2O2pVZ_nA3XaH7GpDrQtwhualDdrSrZUm8HADFuSOt2TBsJainTIYEBjO-pu5DEuZprcl8Bseg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=oLlnEW5sBTvlrz2y9sATniQzhJDSZCvvRxB2gNJg7qt55aGFQp1KD53l0h7dxhtTggupzBSt7atM5oKHcuyGNMlLLJdcR3takABNi-nSaE385ygDUyFL8O1x-Sf0vNhyD2_gCCqeKVdWz1nAxoXWUhVJsDjSqeUCEkCOVOJdKKW5pvaKj3RDsa-LKUPaSACIlFkoiu3Xfb3Y2XINaucWECTvcauNfEh2fx87F6rwnkIBzPwkNwRFTE8Lzw2tjIcfLUMS-a3PZJ2O2pVZ_nA3XaH7GpDrQtwhualDdrSrZUm8HADFuSOt2TBsJainTIYEBjO-pu5DEuZprcl8Bseg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBI0WcjaE_syMQSrkLGGORbIwldp7Kj58J4qMh3VZRSfoU6RQ8Vqr1q4XEqAig_xfeT_riXzXmEjMcnSm-WR8FlHN6yfeVO8Xq3-uhb7HYP8g6igo4hBHhSWShj5wb-tOU9sW_mEd1g12_7DDKUIQfoYWfRyZ5sPnP2xYN-seTl-pvonpNObcuV1gMEV2CNMST2EaX32gtky3FKfygCtHYJTZZJ814bvFAw3GrWXgYF8THBzVhXFD79wUm-lFeEn9ILm2FPVt5IkQ_jOFJLDKuA29sCwJoJncZOcHQkYgeoXAuAa7PDpjhup7xZwJyLA4af-DCYYDGVyw4JJxwDmZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=a60lxCdTzmoe0nJ8TckZ38V6J5-L1F3coUwF4wW91bl5FydrR2TOdTITQ4oaCkHqLl704a0tAQ8r2BBPeYm29diDAAbJJB-igXSJ2L0QHBboVUVIdGc0i-Pa5VJ94S8YW__m7D2CG6-feZth6TIVbwEFYa9-7U4ZIGavSLfLDFpUunro2EtZ2vwO-VPfL9XbqPVTAZSMiym8O4f8lftHyMtJ_M0E_TmqJ2x0BLHuEgmYDqIPqzaQl97dIUGjOaDxvE38A8bOSNhm7tIJ_kQ3sVLr14UVH1aBGHrHPIekbZoOkf-AEZpEg_VExGu6nLKtSa0AvVIl66kQ8MAZCyWoIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=a60lxCdTzmoe0nJ8TckZ38V6J5-L1F3coUwF4wW91bl5FydrR2TOdTITQ4oaCkHqLl704a0tAQ8r2BBPeYm29diDAAbJJB-igXSJ2L0QHBboVUVIdGc0i-Pa5VJ94S8YW__m7D2CG6-feZth6TIVbwEFYa9-7U4ZIGavSLfLDFpUunro2EtZ2vwO-VPfL9XbqPVTAZSMiym8O4f8lftHyMtJ_M0E_TmqJ2x0BLHuEgmYDqIPqzaQl97dIUGjOaDxvE38A8bOSNhm7tIJ_kQ3sVLr14UVH1aBGHrHPIekbZoOkf-AEZpEg_VExGu6nLKtSa0AvVIl66kQ8MAZCyWoIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65273">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCB05YnHxNSzcIynJW2Od0o5FOhqEQ_n14IQ78JV3cWcvBakTopEpY64MKBb_qMEOWRFaMmCNTc3QgIvo-fJlSOXsgindcU05pJkx9yOaxT4Bfv93B_c9CneehY23UjLVVrOpfapyZJ_rUPiXEj3er31RgVnNLvzCU1nMa7Hg3BvkUW7iIsgvQp2N55PeczO7_rYynSqdKWvY65BkcBEmcWQ-ZL1SPO-ZKosqx5BF_HDBLpoSLKazYEo4CTYGS-jrMW4ZulHbramJV0tS7v2nDcuJpkhTtiTxApU-BsUXCv19aG_DvtUa7IirfPv14vhQYyORyoVglTFEUdcEYR_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇮🇶
عراق
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ریازور
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپانیا در ۲۸ بازی اخیر خود در لیگ شکست نخورده است.
✅
عراق در ۷ بازی اخیر خود در لیگ مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اسپانیا  ۳.۴ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر عراق  ۱.۸ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از ۲.۵ - ضریب : ۱.۲۹
🧠
پس از باخت، به خودتان زمان بدهید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65273" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fapL9i97oPPcxuF7b_ULQTDmnEz1ZTYDj1u6USZri8Kj6a5MkgpCKzNqP6klmYm_HtZOzEzSx9XlTC4S1m3Q7IHVAistgRXiJJkdI1Z4JsKueg8-O3G9gnFbkyA18WzvGIM16tOkDWUOGDE4JGafR-BRw35-GOxFsc895-VIaji00jB1-z9i8zL5wp6uiAgkWXyD5NDr0KkeTo60_DMeaWGot3sW3KtALBBTLWBZM1O_874nkEyuV7xY84K323lHCfpleSQS4Wfj40dW-crV6ItyrrY2VfAVNT2bP9mrYovhVervww5HVpD9sMvLB7RkUIX5S_DdFj2vmEDDd6iJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=XuEtVr1SbR2LeE_bXW1sdoc0dJIuuLmjZ0t9qfvSiIYeBNl9St50w2Sik-qOxWN6z7RWz4Ct3TaIC7fiaZyQQA3ErmiHtmoXfKHUG4K7WT7nSVat2etzf0dXQ6sY1yOlJXWKVisIGc3fUC3jdrxYZ_g1ZFj2jj0rcj0gypXAxgc-6iyDWtnWv62DdRThgB7WYh2_relACHjiIcvG03oQ2FqDqyYQ5VHpqVmHzm3v1a2qYgHw6JKSeLes5rcc7PCU84K8nv3NhiJxRLxcMi5_MwHB07JJZhPGUsM90czRRX0kwLUhVSWNtOYvABcvSYpULv-8K9_8yjbWxJBf2-OHDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=XuEtVr1SbR2LeE_bXW1sdoc0dJIuuLmjZ0t9qfvSiIYeBNl9St50w2Sik-qOxWN6z7RWz4Ct3TaIC7fiaZyQQA3ErmiHtmoXfKHUG4K7WT7nSVat2etzf0dXQ6sY1yOlJXWKVisIGc3fUC3jdrxYZ_g1ZFj2jj0rcj0gypXAxgc-6iyDWtnWv62DdRThgB7WYh2_relACHjiIcvG03oQ2FqDqyYQ5VHpqVmHzm3v1a2qYgHw6JKSeLes5rcc7PCU84K8nv3NhiJxRLxcMi5_MwHB07JJZhPGUsM90czRRX0kwLUhVSWNtOYvABcvSYpULv-8K9_8yjbWxJBf2-OHDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
🇮🇱
نتانیاهو: چرا این را می‌گویید؟
🎙
خبرنگار: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
🇮🇱
نتانیاهو: این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65270">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65270" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65269">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fmk5cgUn_AMHA5Hng2RGClqu7Iu7fw0BIjxEbD7wAhWpm5yFkq83yGrSVCSQ_zbaMKKwcWspXin0TxEDElu4y17IO_GjD-EVqS1C3CjmjsJZaemsdClCHfimtLZ6fR6-Aua8G1sgJLKVHAs7jDZveYHkq93jz1962naRvDzPjcvgRZxxlCVsXZxW2nZ-xZ7phpq3AZzwTtZReqLHmYjfxi5biVLZC_-QguFvVYi7hGqgmogHj6j5z4NaSdLvclnUODK1y8t6kq3bgvekOs97q2BCztzrQQrgPqfohqYmjDNyF9i0abZVd6SS9iG3YOg2T81cMO7_MQ2tGFXXHGyVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65269" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=MC5VOEOKW0aNTBcoIYUnOdlBasdsa2Zp_BQHazUY5T923rX53In2hHbats-ttr9qGcITz34swbW1ChIn0C9KLrq1MNaW_ZFeA_djxrC2xA-PQmMQj6e0o84uhg2qfaEqahSyyeyujOT-eFZbmNdCeEzjLqiVJH04Y6F_6ky0C1eYVsK23hvVcsIbowLGjGbZhOFEOjlkuIdFa6z1t-aEgUJv5bGyJh3Ys54wkdqfO-y6zUTfeVWfB_mKtMqi28Ju4D67wlB4ZLq9PzkQEnlXT6TZdsVhsh1k-IDeQcI5eJd3IWZKhxC8veYRZec_dCqkfKJGJ4Hu0sG_RJskgtr7rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=MC5VOEOKW0aNTBcoIYUnOdlBasdsa2Zp_BQHazUY5T923rX53In2hHbats-ttr9qGcITz34swbW1ChIn0C9KLrq1MNaW_ZFeA_djxrC2xA-PQmMQj6e0o84uhg2qfaEqahSyyeyujOT-eFZbmNdCeEzjLqiVJH04Y6F_6ky0C1eYVsK23hvVcsIbowLGjGbZhOFEOjlkuIdFa6z1t-aEgUJv5bGyJh3Ys54wkdqfO-y6zUTfeVWfB_mKtMqi28Ju4D67wlB4ZLq9PzkQEnlXT6TZdsVhsh1k-IDeQcI5eJd3IWZKhxC8veYRZec_dCqkfKJGJ4Hu0sG_RJskgtr7rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=tbEhl_myQd7M2gDPk7yIw5Khwb7wqTttPQrMonuxyzwiExjSSJq3nM6TNiiSrR-S8bKcRXXSuVdAooe7iHKl5TiMPsjZ3d6YQwsdxR-brA3zXTviaulp84vDkaeSerxPYizROjSP3L0fWXfPY3XpmCNK6uIojujxDeP5LhWfXESWvTgrsOHtWh_NRJuXAyAMLIT8hcrdU8oUsGsERGcpubx_VjLnYQL4QhR_TssOqKazNSqEYQsECzyN1H_tM-izyacmyHWk-2QLWuyG0qM-Aem9lToAyNfP5bzzr7uV1uEN8z1ir2Uf6TkKL46EBYISfaQ6rKRn4nd8uPeOPJcDZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=tbEhl_myQd7M2gDPk7yIw5Khwb7wqTttPQrMonuxyzwiExjSSJq3nM6TNiiSrR-S8bKcRXXSuVdAooe7iHKl5TiMPsjZ3d6YQwsdxR-brA3zXTviaulp84vDkaeSerxPYizROjSP3L0fWXfPY3XpmCNK6uIojujxDeP5LhWfXESWvTgrsOHtWh_NRJuXAyAMLIT8hcrdU8oUsGsERGcpubx_VjLnYQL4QhR_TssOqKazNSqEYQsECzyN1H_tM-izyacmyHWk-2QLWuyG0qM-Aem9lToAyNfP5bzzr7uV1uEN8z1ir2Uf6TkKL46EBYISfaQ6rKRn4nd8uPeOPJcDZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=axpyImkamK7lgxqSaF2PgR_VGV13FZUM5-aCiEzQZHjRXiw1_MzAK1ljak-xRBSGyuOvFc84ScaJoSOHE5-0UM3LGp_EgvutfDqIoCO81f1sAeWrblie7LSTI5vmTEJTOFYN9vWqo3bVvQaOz2Vu-d43ZctHRfdsycannNovJM3RQugdfHiw1Eg_jiySdTLwP3AhZOCe_KoB5hTtVzfmHPOFl9etIq17oQ9o0JQr8zRuJpRZSv8zEl1vx76fYD1abUxPzcaey_bfL63F9OgSYsSA6lKQHXHGMoMkVpwGNOa8OxGscyuc8dU2_LnepJpdu-azgvHCsyZJuhdPNVEd6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=axpyImkamK7lgxqSaF2PgR_VGV13FZUM5-aCiEzQZHjRXiw1_MzAK1ljak-xRBSGyuOvFc84ScaJoSOHE5-0UM3LGp_EgvutfDqIoCO81f1sAeWrblie7LSTI5vmTEJTOFYN9vWqo3bVvQaOz2Vu-d43ZctHRfdsycannNovJM3RQugdfHiw1Eg_jiySdTLwP3AhZOCe_KoB5hTtVzfmHPOFl9etIq17oQ9o0JQr8zRuJpRZSv8zEl1vx76fYD1abUxPzcaey_bfL63F9OgSYsSA6lKQHXHGMoMkVpwGNOa8OxGscyuc8dU2_LnepJpdu-azgvHCsyZJuhdPNVEd6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoHoROY7B3IQRJtgOGuAO6hmqLFyOaClNvmGP-NGGcO1_wLEwa8BAH6wXYhk6nu-fNAkXTK9rg8T8IaZp2UOOhLOvsPBocny1JyU46dn5b7GU6S1Cvrnr4omLtRgGd2vXLeojxFMRexv0_fwj2vVbL3vue221zv5bsvIxJ_47y7adDBwry9q6EcxhOU1-wXi7H_IemyOilEI02hLCmnyeabFybZWovAPybbm_0ZEbDaeOTfiEPUWS6rFyKQlVhkb4XRmK__ygSSnzETwQ1R4B2vSnbXkyRfGGBRDEVmEjMIwJk8jC-AXAYuvnG6T-N4pO80I7YUIqPqXLqjFv7bcIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sUhs6Odb7VwKGpLTmfM_s9XfqhM_k3WBF2UIv7tmBdKWDcLRHKggtu6-c4ApVT9jcywpVan9s82sUnh5J2y-LdllEOfyRaD_Xo3GHOuhHpVrQsdTrP6Nt8zWBj1XlruwrsIj6Or__aCkDfUMiW2qhMstpAoQBcuEz3Rfyz2cXBJPHrwiGTqKdMZPnxqvaXgKREc8hMS4Mro54j6DPej1bgc27x17MgfYziPHYton4jvD-tL2WQ9RK90QlL_oswHVC_sVizYFX79rZPVAiXjTEowDv5NI7ifj1kNwRwMHyo0-o_6h0wlnNpPPQmTaOGY2dHOKixD5D6R38Nu09rwzbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEDzC8YpyCtxekDOFhuckKB4AQS0I7m-aA_uv9Jl0MXNGHvN6bXc14pZ6F9uWYSeFEnCPYJ9g7y_LCKqsteRk4Y2sE0ybI3lsdBmSyRYU1B_DFZBeCM3OByUu0x3_2evMCE3j7AOuPveav_aKpuzfBhqHS_UeIxfZZ4r1hLWsdScw2dhhRi3SGleMnINIFqzG6Saz5lgDBlwUjDmWsLd2IuR8i8fupYbBa6DgXIIxHyh0e5EgmP9bAaAs4TT1iC7GXHG9hR77dndgi4VEH9j9HlvSkry72bP1dJwq53YZ-XBaOkJxkB4OSekMtKCaCvkOE-0GKlMw0OJM0aF0kq5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-PAIpwecH599j57xQNR0yFtUcwk50WM9vLnldriu4c3YF9m53JCTbeDI9zD0kGjkKT04lppCgRXIOySALuG2P2rOlCAgrF2kG3gVyXtRl5qGRnReiCMQHZggOXdzG9u-Z8njoJ1eNxHK7QX6TY4mBgZkUpU8-1Nnf8nq3ImTU5EwRM2FxKSwxMBMwHADZJrAdXrDw_GaNPzBapIL9xxxNkBrgj4W5hRuCBrJR1Net6LHNyXd3bcDNDccjfZqviu1ZpOTAcTxoaVeSu56tYFliv3sEgCZA0r3Zxx4FIw58Bptn4PwMmEkO2HA61KrOrk8q7EotjVj8pJqhRjvJfTxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSOUquIaWvC8Szvb2HtUH51DmSaFK5eXq9GGlapR4ICLyJ225YhTx4UZwqFZg4W0NEX3x8FshDMPkqnPpUkc-4fHOxYuoRm7luk8pHcFh9HKqg2t1zcK5RdhhjlmhzQx20Fug_LSxUp4TSLQgz0O1VlQOcMhxfP18nnGC0Am6IZ6riS9lQ1im7Bc2V5ZowRv4Vd_gugDibnPMjcC6rGA7EK5X22mOJToR8-Uwuf5yv_GEfPB2iz0ZclMdnlyNvKtuTb2AVKI9A6sHAt3rs0t5f77zDK_864HIO9XQHDrJNmvdDKx_w2kOJ5Cdistd_cABra4x6AE3K0uKTBfCjFpBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=VGoxHatWl3zQ97o4kYaleaPodybheCKGFB7qSLSvt9DNHdU-b3ORIaTJrt92uYvepeaHhoaGMLqgKs4cAivcd593LhZhbKzbks5SHPAhxJVLPK8UwjFsPUW3raVb8GIKPWHMQvMX_4uP0OAZmsVizdAgZKnDK4y5sx438QOd_OLmC-kv-A9XXaioaM-5jZX1E-OfJhY2A_sFbt7lOUCYBsSn_ExxcCvDYMKyJzQ2jGym3eVvKNVzbF04f2Qw-etZ8BTE72QPs02unlyZBjGCeooND62tORe3A_0bFv48X-lVaRHz9K_uY4zEaQReSkeVdG57rDlXGNo0ffg1m2FQ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=VGoxHatWl3zQ97o4kYaleaPodybheCKGFB7qSLSvt9DNHdU-b3ORIaTJrt92uYvepeaHhoaGMLqgKs4cAivcd593LhZhbKzbks5SHPAhxJVLPK8UwjFsPUW3raVb8GIKPWHMQvMX_4uP0OAZmsVizdAgZKnDK4y5sx438QOd_OLmC-kv-A9XXaioaM-5jZX1E-OfJhY2A_sFbt7lOUCYBsSn_ExxcCvDYMKyJzQ2jGym3eVvKNVzbF04f2Qw-etZ8BTE72QPs02unlyZBjGCeooND62tORe3A_0bFv48X-lVaRHz9K_uY4zEaQReSkeVdG57rDlXGNo0ffg1m2FQ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNH7QdYDaGoCNaVxNjjjdYidPnXIN5Z6eCqVzCHL3ty3T7zzqNd2n1HqJ0ZYGliQLXa8dzZblWl6a6i_iWJD-xHO0bn0HBz7ERa2sH_7OETnHi_t4kCd_glSuIl6r_Fxe7aQ6hH-jnieXjugFR9hpepoZHWJs2BbLMuCyFv6mp263MKIeYaCgBCBDdGLzBvq3tzi6SDh4uXQD_RAfoqLr7XAptTmOw4MMTJJOzQ74A9KuCI0g7L121tfLlEVNNfatuUlD8sT7uea9aU4vVeLe8EXfbzVJDXtvM5OGHl_ScLcR1Sst1gQTRkC8mIi3sHjqk3jYIeyeCI1mjYDMCVS0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PuQLsd7PlJJd7yGR8fFvdKr0oUskqu6b3Zyk5DKMTA19GezfLuxG6qYbpE7gbHJBnouGi0I5lAE3Mtp22iWcWGHWtUPDlhq4i0wb06Ge8DnH3MxtaaaNGcgKdxBxRraycrg6gAkTUdyP23qssEEffmYYDHsxufP5Bqk6NwBpDAlRmgJbjeM6ZioaGy0yJGqzIiE04WzRREdbXxXp3QDE2TyZlySZew4q5M7Gk0OAUOW1L5z7IJhAFTHpvT1dEEfMFcAn1pGyt_VT_-C_HuKq1xufBnw8cR53n4nnR6PruxNcdmAVhkIYuVV9hxmpD0EiPvztR6naGX0_wx7IbVye7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcoRU_7kXv-vYvq_ZJ55V3dst18SbNi4c-CqLQ-nfW-iONuIYj4PsXIKViNOnKqk5igav6BRrriCVgD6PoS6b0lQSXE7ic0X3nnS2kMqvp7uGRqleOHaNmQTXPYbx488RrYNfnvL1MbnxFeKdkIDFqmguThCG6gAiCoZjnbqxqGan0sFQ8FWDoZiIvNO4BsktXEqs-w1zAvTWl9eDwjW6oocuG_YW1ugTdMJycg52ayxk-VUUs5Dq1p6gnDRt-yyz-mu9Rc4iMwXelCFv90bgUeY56QpbaBZHFF8DZ4i8UmTFZNbJr8DJ51hylmd_UatkuTgZM-au8KTTakrdTEmNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxUBTBOAvfRMNWSquU3sJ4uJjunUVyrj2ySDAZgeSzWGx1eViHSHK59W0u93x-nwnauuRoKIWDZPjivy3_MUbWV-YvYa-WP--K54zQuNz-M-sz4Zok-_5GNjUr_X2KGMe69yVifK8ivy8n4v4sK1Kg7YuEwBfibBF4x5M_2OhYXUOtV0R9i27cqp7_tkUV8NNwpwu6fr60s-QY65sicinqavFulaJ2Oq6P4kW-WzaKwBE38Jh0cgMdrapdneX0c4vIrpcdZJNBa-iHE5mS_konifdrvXiz2QGY-0G7jsDi5FZ1KRG8Vmwou6IVjLB7_ZZINEHH7P7zHrTSZzzBjcFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbVsSvwMwIkS7ep-GO9Sv5Rpo9-6yo_ew6ZZAmnDaDmgegvR_U5gtm4x3kHANmDA-feWHoyrv5TSBcmQGfLeIy-GIkW_SBR30UmB-ROnJcPcZGPdlxq5wsPw22mSRo-ZUjd-HQn0g0h_1iseK5EdZ9LupZcSKKzIWb72AEvkczDF5M9BBrIT8W49ff79xpZEf0697zErNLwqqU5hQan77XZCUukPB_L0XVKtcHn0BYam6hIlSx-8U3f-2wxN5mC_4up5fcdj6yO2LNARBjvNec4952Bs6OTbNnO1dP1fOeoiYQAQlwZuJqhmFkkELlg2t9SKPMsJZGEFslR99aIHaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz_EU4Um8XJN3P37VRXdiP_n24PuyFKlTKhbfh_uxs93moB5s7oPAlFNe7sy85beYnC6Wsvulyfpp-wI1-d35U4xbrMRMbU1g_XXymiX4o7-9s1yVFgHnL9SobHnr4G6Bk6bT8h1CnBIuLbNHg743es1Xf1_8V0QL-baYUu22d4DD8DIYryY7uZenWiJIwTZi0uDhRD3PuwE7SpOyfjZCyIxHfWHGTHfb1rpul1dULeZtb6t7R8znGS5Cle9DxxMfnnp8mIgpoBhNEyhriwuIqAohnKx9jq6Q8Hi-kvfWsdYMgNnPOISJBV15LFexHpI5rCtx5RTokP6PNztO1hGaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=K0oqnUF_C4aFmOkRy5GoiMYrIO5JMAv0UJNpKngviJeC5bGiRqaHiUYx3uOGOOv5MD5dL-w6_Z_Nfc1PpkulGMn582FXI0DcaExYdhs9MQUfVn2J6jbC8qK-Rlj72p7OaWrpuAymMI6zdV64FH7_n3Zxlr05muykX4pTgPlymbZt1YFaK15sB804M_gu6nq9C1JorFkD_YXcbeqnkTVOfNhBV3I3rIfNzHetkLKeOtaeUaO1gKthYO-kafwUpWM_-sVZaUOip_lQy5o_UK-sUCl94fqeLL9KHzkHX1AXhO-cGtLwvdm7KjU6abqCr4PLi6-ztMhZnYc1UmnVmx-lpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=K0oqnUF_C4aFmOkRy5GoiMYrIO5JMAv0UJNpKngviJeC5bGiRqaHiUYx3uOGOOv5MD5dL-w6_Z_Nfc1PpkulGMn582FXI0DcaExYdhs9MQUfVn2J6jbC8qK-Rlj72p7OaWrpuAymMI6zdV64FH7_n3Zxlr05muykX4pTgPlymbZt1YFaK15sB804M_gu6nq9C1JorFkD_YXcbeqnkTVOfNhBV3I3rIfNzHetkLKeOtaeUaO1gKthYO-kafwUpWM_-sVZaUOip_lQy5o_UK-sUCl94fqeLL9KHzkHX1AXhO-cGtLwvdm7KjU6abqCr4PLi6-ztMhZnYc1UmnVmx-lpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=IuhDch5Bs7d2rnXGk9F99XjWXMIazQ37oTUlkQfZCYej4NoB-_UM1ywZYaokjA1-Cphzv5XabwAgPnf6QAvL_9udNq76jGkAZiezwU7xJ_nwPFPHp1-lgtjqDfULO3hBEJ8iNK6GXq6mTBFGqrigMmrVZ_EOIF31trMFw4mXqFzT8jwtTT-EspOQmTm1zfb--Vtx9YW2gL8-32dGMD_hvQg6wXVxEWPg2nXOJQ2jl1PlWQE6Lh7Q9KB-LUh8IBJnx3lOCv5wMQwJ2HDEC6ulCQqOB5-x9z3Sp2qpiNm-kImTpt6ymTIZDXioFJYMJx1xAGlQhIXwhjlsvVy2rbWWYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=IuhDch5Bs7d2rnXGk9F99XjWXMIazQ37oTUlkQfZCYej4NoB-_UM1ywZYaokjA1-Cphzv5XabwAgPnf6QAvL_9udNq76jGkAZiezwU7xJ_nwPFPHp1-lgtjqDfULO3hBEJ8iNK6GXq6mTBFGqrigMmrVZ_EOIF31trMFw4mXqFzT8jwtTT-EspOQmTm1zfb--Vtx9YW2gL8-32dGMD_hvQg6wXVxEWPg2nXOJQ2jl1PlWQE6Lh7Q9KB-LUh8IBJnx3lOCv5wMQwJ2HDEC6ulCQqOB5-x9z3Sp2qpiNm-kImTpt6ymTIZDXioFJYMJx1xAGlQhIXwhjlsvVy2rbWWYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=rAgoFHDarYP46eqRlDqQWwKnC_0iY4dsLdcDyJDlMGTydADMl-P-vztK2mSLDYCdU6AJtLI4c3hnPvTAe0-zBeOHT11ES5bkAGk4dKnzbsFmGD-PNSg-_QEIRyV-mX0NRWgZUCdJXEMT0q-leDzpcrqdSw-WWmrtbfL2iUwJSFrOSFoHARFd6U46s7BaS727OfBSdxURFEQyNEKZN9gfiiqvDlGGNiBr4daR0wAW5cFs7j6O4pDFqWsSU-ztbWvFvBNRSErstk6eJbXrNN5H_0LLQubxCuNdgMnUwe4OeyvPV3nv54B7eBQL86GLdq8ymVWU4SGkS-FoUyeaCVSn-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=rAgoFHDarYP46eqRlDqQWwKnC_0iY4dsLdcDyJDlMGTydADMl-P-vztK2mSLDYCdU6AJtLI4c3hnPvTAe0-zBeOHT11ES5bkAGk4dKnzbsFmGD-PNSg-_QEIRyV-mX0NRWgZUCdJXEMT0q-leDzpcrqdSw-WWmrtbfL2iUwJSFrOSFoHARFd6U46s7BaS727OfBSdxURFEQyNEKZN9gfiiqvDlGGNiBr4daR0wAW5cFs7j6O4pDFqWsSU-ztbWvFvBNRSErstk6eJbXrNN5H_0LLQubxCuNdgMnUwe4OeyvPV3nv54B7eBQL86GLdq8ymVWU4SGkS-FoUyeaCVSn-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmuHk4N70zkIzwfBvdryWk6J7xHzpeZjalYvxfWkU2Fst0jB_3gCNHf-cl3mon3yTk319cVM0uRR9Wxti53RK0gWUxeFqg9oI3cjIEZRM0oRbg84pZQyyQ6kLExaQGOTttCqgcwFIC-3MpQa2hwzxrLJyp9XUDKhYILs7QEoPdqTpnE3k168ReelTPfG4fNrJNvYS9HzqnXMq-rTFupBWT1WFtHsoEdDoIcgPoSVtEdvh5QPxyDT8VOuifuK9T5Y2MoLbwZAk3l_XN0vcFfOzeQOad-c1ahoQEixLJF_RG7qgOB4IREwcnmE4utjvtYZIH_yV1hyZMAVPzfCVoCVpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=IFBteijwXfNpQty-HS3BdhIjQ2czKhKgmCeUocjZvozsuE3A4QTfZvbNPw8prJdoYmRIialhqRxicSbsyC9nRAPU4zuEmTAsP4b-qKnOF5y5izaPrem_KXJUMTzDksja45IQXFlI4BbUV8jw8sZeAjbI1mq1FlyRjtn1lnauEb3Ymde249iSK6ct65BRvIJ_cSlepDK3nhFYOm6mjsaBZd4D0MVkgFS4gMG3nC-OJk62-4teZptES3Z5LvO5Rz6luq2l1koGX0axAHrZ4W5KN0Wer-R1LQqwr_RK1BxnD_RxZwqSmnkQyvGtOfcHVK_8yrZXokJYNqteolG3VsApOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=IFBteijwXfNpQty-HS3BdhIjQ2czKhKgmCeUocjZvozsuE3A4QTfZvbNPw8prJdoYmRIialhqRxicSbsyC9nRAPU4zuEmTAsP4b-qKnOF5y5izaPrem_KXJUMTzDksja45IQXFlI4BbUV8jw8sZeAjbI1mq1FlyRjtn1lnauEb3Ymde249iSK6ct65BRvIJ_cSlepDK3nhFYOm6mjsaBZd4D0MVkgFS4gMG3nC-OJk62-4teZptES3Z5LvO5Rz6luq2l1koGX0axAHrZ4W5KN0Wer-R1LQqwr_RK1BxnD_RxZwqSmnkQyvGtOfcHVK_8yrZXokJYNqteolG3VsApOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=KDM62W9jGaKzzACNIn7oMZZnsXR80LSbRSQNSfH_mxsols3zxBGZwOgXxr-0GbDRZY1JEgGhJoYpOXKI3crq8dbbkBZUq9H0M2y8PUBjzXimrddap5VJJJBFmm59QHj_at_UEiMqPWKzU5QwvW_wSbtaDmwP4zwmXmep-GcckPAebu-x0NYaGZlh4VFWyXGfqcI0MIEg-13lSL5uR98BQsyUApg1w7XNhObLsjDwG65Ya5TcARvpi38mjNywrsdeL_Zm5nN96xbRMH4yWPd3IrMQXmKNCAJp5SEWfMEHotcFK4RfuY_rYdDKTWh1jWcQcsF0uLGbRMu15XQlZto-LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=KDM62W9jGaKzzACNIn7oMZZnsXR80LSbRSQNSfH_mxsols3zxBGZwOgXxr-0GbDRZY1JEgGhJoYpOXKI3crq8dbbkBZUq9H0M2y8PUBjzXimrddap5VJJJBFmm59QHj_at_UEiMqPWKzU5QwvW_wSbtaDmwP4zwmXmep-GcckPAebu-x0NYaGZlh4VFWyXGfqcI0MIEg-13lSL5uR98BQsyUApg1w7XNhObLsjDwG65Ya5TcARvpi38mjNywrsdeL_Zm5nN96xbRMH4yWPd3IrMQXmKNCAJp5SEWfMEHotcFK4RfuY_rYdDKTWh1jWcQcsF0uLGbRMu15XQlZto-LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=Gv2cv5FmUjRUF91-kGjUiroXvpSU_x1XPdWrqq39VwFe5vnfVonHQt_iN4YYjLjDGeDzJgb56KEJv0bOWLJikVt3RwTEowFj7rxD66Xm3YVL8xMCAoYhWY_RzwhnPUdM6GF0lXkCc1B6wqXcEgkg-aHshgB0dYW4E0wnzQaZ_4ijX95zEhTWUrkArMrqH2IyMLN6KEZ1ol4OokxmZOft8HP8Vd1reU575X8oVaSkSrkvEbYUACkIyD3jI_gI3kwJrGdpbBmhl9b5k56VLCZ6xekMTway_OObVyqScwUA8CPi6NY3L2DssKUdCMbrdgVj9GSpTIBFzrdb31TFMFeZgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=Gv2cv5FmUjRUF91-kGjUiroXvpSU_x1XPdWrqq39VwFe5vnfVonHQt_iN4YYjLjDGeDzJgb56KEJv0bOWLJikVt3RwTEowFj7rxD66Xm3YVL8xMCAoYhWY_RzwhnPUdM6GF0lXkCc1B6wqXcEgkg-aHshgB0dYW4E0wnzQaZ_4ijX95zEhTWUrkArMrqH2IyMLN6KEZ1ol4OokxmZOft8HP8Vd1reU575X8oVaSkSrkvEbYUACkIyD3jI_gI3kwJrGdpbBmhl9b5k56VLCZ6xekMTway_OObVyqScwUA8CPi6NY3L2DssKUdCMbrdgVj9GSpTIBFzrdb31TFMFeZgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=qk0jxCk-PYkNAtgc1Y-fP7GHuv_NW86u43SXpi7sX70oDlHxjQQxyOmgskaBayHVD8MPZwH_D2DxPVw9Ma4cG46rnigHZl81SbeUlYEya3xZA5BKc757ct5EvYGyKtJWzxQYyz153-fEnsiurUMEk6bqLUlPBGTecrwlmxBS_J1BCa9l2xWJbtsokK3KsQd7T3MhYyweb3PZZHy2dSwuZdx_u1iZuNYcAlQGwa8G7xIpQuiN2wIvV8htesf6pR4aHJRql7fWVoC-ErEoscmDuCK1PrdeH-Qq3JQA2nAkAYIcqW6W6QBC5uUJVkjFD9QFhi_Pj0xZnqsG5F5dzg6nbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=qk0jxCk-PYkNAtgc1Y-fP7GHuv_NW86u43SXpi7sX70oDlHxjQQxyOmgskaBayHVD8MPZwH_D2DxPVw9Ma4cG46rnigHZl81SbeUlYEya3xZA5BKc757ct5EvYGyKtJWzxQYyz153-fEnsiurUMEk6bqLUlPBGTecrwlmxBS_J1BCa9l2xWJbtsokK3KsQd7T3MhYyweb3PZZHy2dSwuZdx_u1iZuNYcAlQGwa8G7xIpQuiN2wIvV8htesf6pR4aHJRql7fWVoC-ErEoscmDuCK1PrdeH-Qq3JQA2nAkAYIcqW6W6QBC5uUJVkjFD9QFhi_Pj0xZnqsG5F5dzg6nbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLpMlg6YiVCCl_HAy6zEjzDjbs7o0OH7FfGgpN2R79Xu_pvqmcv2Km88n716GRhUyG2BjFuFYaav-1nw5hs9JmQXqf0Dhi7pbOTfJXS7a7RkHIvFEoFujDqRzVquQaQtIqp0E5WZ_i5SDNh5S1MpaCo8gbw_eeebGOLKteujc15nfyyDknMyMjVytlwrK4RW2pVlGvq419XhcUzJLD-JCMkgw2Z6QJkpdR98TIYmK6nQRNj4AD8askTf0kDwn_vTpNnAvC-VQjOczfTj4ysNakneoyhmkSOkCyvO570pKvTDZcvVn4A4kayNSpphEIs-DbrwEdZYKX_D1c-BdzsEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WPEaVc428srO7iG2mDKO3dnqUcw_lXeEBHVRW3ZEHpaUs81PIU_qHowTy-7d0Vcfed11vifwcx2qVDwGf_jkK5l5I0z0faPItg6mp-m9EORgfkSPYtJJVdHZwyfytv4PCu4igTf4BSpvqd6iOxWg51Eoa0DXtHSTjXwF4FUwgMUxg2vSImuQS-sQANPTV1z74W_QmfzXr28W46mig9e6xZBXka8S70bPN8d0_F99QzDy6KXY5EAzqiJs_MZVwLgZFXRpQbPSoMFmbkzQyDlu_0xKB0mvWRfEFBrZCdNmfGzBA6MGHUE7ti6W5ehg56Z2DMyfSZKafVMmnlu5ibirWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1LlIuehyLKNFfeEbC_Yg-qfk0VPRmPDgsnCcmVWSO673BsR6-BWY1Z4C6P4y9bos-MhE_4ACsOVTUPLnDnTgrm2q8B5y3E2wgY2QbxYaLxseHzcsadU-fGJCHwgC_7pmNY0fpnEs0BPyDp0tXRCbGN9mD2C065O6bGvxAea98n1PqScxcINNYb7ZDCLDgqopbgo33ly5sc8tbPK9e_DhzRSTsd1gq7cYD-MCR9UH7IDQ-cJr3F-Yb7L4HH2WhpbhD57WGhTD2kD7d1vqkBd-XxN69UC2Z1OWSjlw1oz2JcNKuQub9fq3-jCBG_VS629JDoA4Fdg1DjG06MLGkOP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oa9HaZcehTpLJgqj5PCHecjHzlHO255ZTG-VhcUOr1PWoE6PcgJp8XX1OgzNeNbSPyx4m4xJvOIszfT6Mbu2BbcM8zxxrbRcODE_yLjNOrYk6fCJJPikPM0h43VmSqJOkqhNJNIqNwIBh-5qMCg2TXgMcewq8kmCsYFOMgVlRArE0ixIzXQAGCvcihL466Ny1lh9uyaIFZnUCXyOCHc-IyBCDjVRKM38RbBTLBFat5lRyANvHUZQEgCxhr6MHwZVjWe5XD5kcdclh3ozYTk_BCHEzc4UkG_cyXmYIOQpYXZ6rHMZMQyYsjBkEGQiRQlGBZjK-NO1U9SEYHyJPRrT3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cue6KmSPGf13y6ZaVQBrXpYi55HIXjQ_Wp3ppZUNEBCHGwdnXFb1oK2i1Q2lCh8eJ5we4hVL8scHsv9kc2iCoaBM8hMEMoDHiTo_ehvo9RTldHy-H7_u_2zDfSXd9PlRsmPFl2q3_ltFhh9uMXDZ7WHbAeHRhhezKFFaHMMRnxTyd_YFKTt5bgWqkJbM1QXI3f6zwggkRD2v_TbvHF4EiNa0eM7456M1e--EFz424kfnGIEL2-aMN4mp8oBFHORPSa2EvGiJAzmwVQdGrIbJcKJZg93JirhsXfBhqCVlwvyLjpk5R05Bq3kwXJo-ZnoLO9x31_WgCNsCNKnRKeGZLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hO3fPIWtMXf5pkqci2k2RR0pe0izmSfQ2ezMpshR96fTlStvdrniN68oRa_7ae5ZlGIOg55AeW2Qh7fWE19tT3Pr4soFAkwJBgNYAF_4kyYwPp7KzeoKUuqcMLRUt_cv1tn2846FJyJU2sbhnDsDJt45ElXN2idrLvM2nJTeVCurpFcDtLmi-05S55LbbiiRI-3Wx1o5vfllIOrtVR3f1MeVzqNA3BJUbcz96F-ANpd2cbP_H0FxRCQ0UtfBDUnxm0FHwMLsh23xbR5lt628PtaYAURnAF982xOiHcwG5kBlBM-LkZ0vZlF_E6dys6Tudo_eeYatzGZDkW1jS_UxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apblNdguQ-wNSDjGz9CpSHdoWflYqLHJBe8XsfF3mz2djIZJsLq7dgU5XfnFo3KiIN2dqalz8ufC3Fd7-m22HGwfFqeVYkvQrhs872GSnSNIAvCBkRvA36spUttqUbW40dGEk7EVYj9HjTck7OTkcgBPMCziXCNGbYoa-R53z4--a6RQf2AiHLkgEBv6XFG2iKYrHMb0f_0kBT4xDooOV5kOr04_fL-Da6IWP7xSUp74SxYQiqJjt188LFF8iOF_iDOMsdekxoATgDLIMSBNjdIlrDxDgVLwg_-UKjTOxAh9ggYzSDhZf-_sqpho7yrE5WSfSUGh05sTFLPjxnLPtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7ef3on9DQ2dbJuT38aHHBr7bfIGMiTT7Yw100UibGon25vGS3X0Bki3GjZGKoH8pEnbB6kIQsnjVs8GIGExwQsQmOhQ-_iI8txYbYdCYBnLoVIr5ET2pkMMamibmmds7HbbPKu78BDUxghgFIhXp9D51_oZGr3gPG72sPMLe2_dR5TEylk3Y4HIMiVB-f1EqZdsxJNrLj3Ml9q_pdc_V8aUBAk9tZGjEsP9hzpaqmu_JeQr0IxKQhxBYZhq1RZTCS97r1CUx78X7QJAKTapkxu5y3XauVUrIMRLQLrM7nVTHmDS2Rvu0E9jqxFk23SraYWOjTod8LGGaCnr-n7NcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1YcivN2jJ4wVPKJO4SswyXOzBs3_Y5kSqL9pI75jmW2z8pH8daLAzfyIAYEdq8_7iLqK2-omNU63pKMvvIQ_1uCBrVLnClDxxZT2vukyS9yx_f8ZCfe_xCV27yuqO1zHTxfuDc1hnlY42iF4bAi5L9z2pJBdbrO0EzBtwmecEF5WqYg-KIs3okGZlw-7qr_YT8VAd3ILQf0-6vL2t9GoVOH9HsGLd5aRh1ARpvJ7QPLe28oFmYEpFR4qtsk9zBPTk6hCxynr1ZakXVudqi1cIC7fk-9pP4_H0bPHz9dCB9Uyrtgf8-Uian657jKPdqosWOS3vZEQYZfgZ4sYKUvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=LnWoJUJXD7DsUzLF4xquRpC9zHKrnjPfR0D7Rk2gj35hdy2xEAKdCeQI0lYVWwhop2C-c6uwsH1uBvC5TAxug2scjqgrNJxObx2mAMfB-DURd4FqCG3vtQbTRhhFbJzsztLK_gIVlCu2yts3lnc6YNVmy3-TKfYuDRHtLQgIZExsu9lcfS_NidrvGBUq9JseQyUtaOkxM64pDcGD2VqTQ3sttxt_PNR9dL6lHdfJyWag97zt5fJpP1D49IcAmAfhHw7TYaEyIsmpVLYcLafq-pcS5dbU5-NmRS7Rrt4sVR2aBPc1HRMx3YFpGJ7fhu8kEeAoREf47HQn2LpHNJeeCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=LnWoJUJXD7DsUzLF4xquRpC9zHKrnjPfR0D7Rk2gj35hdy2xEAKdCeQI0lYVWwhop2C-c6uwsH1uBvC5TAxug2scjqgrNJxObx2mAMfB-DURd4FqCG3vtQbTRhhFbJzsztLK_gIVlCu2yts3lnc6YNVmy3-TKfYuDRHtLQgIZExsu9lcfS_NidrvGBUq9JseQyUtaOkxM64pDcGD2VqTQ3sttxt_PNR9dL6lHdfJyWag97zt5fJpP1D49IcAmAfhHw7TYaEyIsmpVLYcLafq-pcS5dbU5-NmRS7Rrt4sVR2aBPc1HRMx3YFpGJ7fhu8kEeAoREf47HQn2LpHNJeeCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdMrKqgrJBneaTl6HjdHchkGXpf5lMskBDicjkdv-YtAADiA0iZQ1tUdFAjzNkLkFsrLhOQiAcEq5VlwKpub2AYqcvJeRrr3tKhrxzl2BmPEdrmLHPdC6pdVQM3Cyhp5Is3DpCuFHvf4F_9ZDMRL4xPuTq8QlmRIytjJyoyEjNuga4JA4LpNP9kWZT0ayC-X7YaFnvDcZoiZ71J07w3Z-3UTjhGG1vbx1nC9GidyIlP5KHJEeosox0B93GCwt0dYwTggSgrqMDcxJZuD9XGh6EqeRLuTesov8dAB5nVdU1zIMQfTSADd1cPscVlqNy7z4qivrzPrWwoE8X7SAPXhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjmlU4RNNTS8A2LNRDIGsPtJlb8ATdcs9C2gYjytYTxORXH5sE2no-mznZ2XCGZdjiYmcVsrZc286hCuMbXWO-3F5zXj5xbidDD1PnfpduOLY9LyS3B5xWuwkG8MfZ9889PZcvnjC-kSPiZepTy6u0lNaU2b-LZovjitxRWjInBBEktXJ-A1N41lYAk-2KXbURqPbhOV3XNIKEzkMvHiXK7taaG2MKYjXLYmvdnahv_Xb2f7YxnWnPk08guaNHY8bUwkngXza3QsPMoyTiqSf1eZ9bDeXQvc0BWXOZrzpPshcG-vHlhYNnpmL8GplGmdtbRpxXseg076yve-xgO95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgBRAnb8xQyL_U9JGFU4pct3HGeM1a34ggZHgJUvyM7rucvn4EoEoXjEErpUEnayKUxQ2f_qXxq40qFT90paAc6KdHpKAxgQx-jHW2apoiMrJ74H9Y8CUHuj7jz2JyBX5Edx8Ui3RdfbpmPAUc2t9wf6X8Dm2CieJw7fLQ5B0oWKbcUAL1m06eaVJ1Xs6nRgRNwdHXy7Vkmag2WwpJIPU2Cn3bZsw8uho2BuZjIjeY1M99rXz3SXc6XmDUyj-EDPljRiFOlbzjevzWLVBE3bP1kBa8WkpyE6_3Qy2I0JGTYwE-o7FMAi8LdY-C_Wv4hVKvun8fIuzRvvyssoBXHeZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHGkZm6emXvZZCT5sZ6in5N4dibIn885H2fTLtcalbM8KuTILtc6iQm8TwxpdLy-gJTvuD943-75e7R24BRu5_9miAYY8N3z-d9xcH66EG8R_n2FW6r-GFvxz5QDZOb8DVsisXB0C8ULYqwGE0n3kOE5Cx05pqFfci2dpDf78hKNODAxcqi0Uspx_ttVSkZ7K78DNIYV0UXp_RP0L1aIwaQaF40F-4Q7CYim8DAB7MKSpLLBR4ZLzY9CaRhaGsjJ4tuZqB6LbIpbKiMxI2rwiHMJfhyVtRrQBo_BznshCBgfpiunr5rPNM57JiiIMILbWUskQ6kZnbsSR7j7ilBC6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=mroRcAVAF3GrU-4E7LdHDpugjgpS2jCsP4gegvBT5lpOyF68Wth_zW1IMGFggJhMjeBSs1arrT9Q6h1R_F7ZZBXVAtcvyZup3ueTRffjGaFrxXcq0IM2TWVlIQI4L6KseVdVHbFssRpvUk8E84VD08TLpOcEK519Irw4RdOvn_4moizlJrhIuPeb6VP_Rz4-F_sMDze7Bs4WRg2GlU02Z0OuV8yERXxs3TTsvVREa5DZeiXAu3gonAfWotBv_VYzcT_fZxL4FVUNRCe_sAIVT-rC5A-MVmD4Hy-Xir7WfQaiJGqYpSGNwhI0Oi9G2a_IH8DYQWzJt_OXbPNppRcHpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=mroRcAVAF3GrU-4E7LdHDpugjgpS2jCsP4gegvBT5lpOyF68Wth_zW1IMGFggJhMjeBSs1arrT9Q6h1R_F7ZZBXVAtcvyZup3ueTRffjGaFrxXcq0IM2TWVlIQI4L6KseVdVHbFssRpvUk8E84VD08TLpOcEK519Irw4RdOvn_4moizlJrhIuPeb6VP_Rz4-F_sMDze7Bs4WRg2GlU02Z0OuV8yERXxs3TTsvVREa5DZeiXAu3gonAfWotBv_VYzcT_fZxL4FVUNRCe_sAIVT-rC5A-MVmD4Hy-Xir7WfQaiJGqYpSGNwhI0Oi9G2a_IH8DYQWzJt_OXbPNppRcHpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuQXNLfNEa0JAMFi2kHywUmuc6SoShOrtB_PoCpYWXig3EusKVnMd4PG0ltGxpRYD5F0CC5oRHGJ1l3WaOkrSrAtC0ubyl8CemquxmcOrKPyoejazi9F6BKNfbUbkFWJiXf7vjMDIb4UuL-Mv_NBEqBr27rROC0Yo1VsLF5ohQgIREo68uK6UnwK6iu6AGHKKNrK2OM4T4myAoj4pNqaEbwnsM9auQWkhUpA_ZUEAOwLDBx-6aRiOCW4LRN8BiH5iV_6czHOP5GAkvmJFXGZZOqxGMqmcyx_4poI6CVfW9lb5E1To4uyG0QjCX55hA0b-AedbzMOeq285aumxCGFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=l2TLkqvPaTpN289Xt3geGIu8wLotHXun9YSpNCVB9cW8V81W8n-0BkU50N57gNZzVfVXCUwHWKoRNxoXHPadjkdFKFw0GQ4oS6WjLl0YO5Ak1cHbzBfkIcs21njM8IBxvgLxnHqTeS9Qu1dtda0D3VhfJVKmhoK3b4TR8ze69i-MaljA7dJymObYpdnc7-uY4soztHdntD0YR2maAKnU5I-rNboaXuQ-oTW4ztyAV1aLG3DfQ9IQ9zuHp4xXSDLVyXlvXaVUr-Ao6bP8N5DhEB9pnji-j3zsykYhaJT9qNvKP5hEcJXtQR0sKkH1lhR-hpHH-cxUly1qMo3kzoIegg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=l2TLkqvPaTpN289Xt3geGIu8wLotHXun9YSpNCVB9cW8V81W8n-0BkU50N57gNZzVfVXCUwHWKoRNxoXHPadjkdFKFw0GQ4oS6WjLl0YO5Ak1cHbzBfkIcs21njM8IBxvgLxnHqTeS9Qu1dtda0D3VhfJVKmhoK3b4TR8ze69i-MaljA7dJymObYpdnc7-uY4soztHdntD0YR2maAKnU5I-rNboaXuQ-oTW4ztyAV1aLG3DfQ9IQ9zuHp4xXSDLVyXlvXaVUr-Ao6bP8N5DhEB9pnji-j3zsykYhaJT9qNvKP5hEcJXtQR0sKkH1lhR-hpHH-cxUly1qMo3kzoIegg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQza6VtI8F1KFSsF_O_lkvOuHpAz9UqTQuo9iBYCu7RvP0jsI4-ed4RsSF0HXWAKQuRJ1y_h0GyftuvZRHd_S3C6sm9cp5RCL8MPKO02SATqjuFTa394dCW8GdZ0voQgMI_BK_cC1SpzslyzGOWlH6PTxn8A1KRrClgj1YvUN0gnG5QBm6FcRvWemaTF-bQyKk71-nhjv7bhUg5IsKSwxBpzJ8uJdBWnmN64DG8h5qzlBgB1YRi-mNKUqOTx4z9aRaNVZ0bE_K0CiZeS9ZhPRrm85dXtJEwVsBNr0cBUnCVl91ON1Bq3Smg_rn64X4uU2dzoMzudbRjxxfyuK0ofKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=plp0OPvcGaSXBxXMqeDk5dBQImOnRxfY46ji19IxDCMEIAQSewqWn8FAczQzBNJnEp5eo5jOY0baYNVxcH59Rq8zlutXhKIOTbjPqTrBmJNgZ5LSKKbdQXbnc9R-6giMeJwhSC_JyD05hRI9icYSFmhklnNrX4CmqhJ7fQVWKTMtrZuWprn2frbEv8Bzx6Aj2bh59gIr1le80DazguCYGV2IzpIZ5ZfirAeY1q5JfL1HgkOSh7R0cI2jzSsz98zYyEK58haS6s27S5-C2OJygV9OwE7Ug1F5X-DS-M5MbnWpYyXcQtVoJFtqm5vDVZsn9GvVGzr01HkLbFgPi8B0aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=plp0OPvcGaSXBxXMqeDk5dBQImOnRxfY46ji19IxDCMEIAQSewqWn8FAczQzBNJnEp5eo5jOY0baYNVxcH59Rq8zlutXhKIOTbjPqTrBmJNgZ5LSKKbdQXbnc9R-6giMeJwhSC_JyD05hRI9icYSFmhklnNrX4CmqhJ7fQVWKTMtrZuWprn2frbEv8Bzx6Aj2bh59gIr1le80DazguCYGV2IzpIZ5ZfirAeY1q5JfL1HgkOSh7R0cI2jzSsz98zYyEK58haS6s27S5-C2OJygV9OwE7Ug1F5X-DS-M5MbnWpYyXcQtVoJFtqm5vDVZsn9GvVGzr01HkLbFgPi8B0aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=hk_tZ1oTRW58dfBCT-9PSo0VQJ7ox_EXcvWTeRLl8JqLM7b95Xaje9PpbvuMIkjf_aDmtu6X2q1VRHkF_dWqAbhbv4uhPb15jlCTjp0hSmJvBncxLu8A2QDARzS94EzkuGgn2RltZX8r0f0veLin2PgomTXFKgMy5shE-cHYPAZwIg6d_E0Cg5TMoQ94hNcHT8uNziFMZKJFFN4BxxYvClcn1gaLOtrnxjWg5M6bZppSnEa8m07Vk1OyFfU1EbdXlwufS_s2tVrruh4E2JvwxGjk6j3Yc5gg95b03Z6WQrEKc-p7w4__JDqmAkNX7K8_SatdfZjpfMStm_OlQM6fZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=hk_tZ1oTRW58dfBCT-9PSo0VQJ7ox_EXcvWTeRLl8JqLM7b95Xaje9PpbvuMIkjf_aDmtu6X2q1VRHkF_dWqAbhbv4uhPb15jlCTjp0hSmJvBncxLu8A2QDARzS94EzkuGgn2RltZX8r0f0veLin2PgomTXFKgMy5shE-cHYPAZwIg6d_E0Cg5TMoQ94hNcHT8uNziFMZKJFFN4BxxYvClcn1gaLOtrnxjWg5M6bZppSnEa8m07Vk1OyFfU1EbdXlwufS_s2tVrruh4E2JvwxGjk6j3Yc5gg95b03Z6WQrEKc-p7w4__JDqmAkNX7K8_SatdfZjpfMStm_OlQM6fZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=sOKnAKcBTpJ9XoYd6_XhI0k1mPhRkRjUWnEDrStlov6wlRWK8P1cXREY3PckV7jurkHR8ClCKriLBAcA6u6Se47yIQtG-zTCscYDXw6KJ0QA2DBvURTDVU0uddQ5bhP7_FAXbVuAf39v1vDu8LukdLXWWbR3xLt_p54dI4GVriYjeAmyJS_e-n12REGwYlkJfy1q7B3RPgUjkw-Zl_MvnU00jv7TIbi-w9gagMBSMjlmXA7wSezf68iL_bhGkbOlSPGyIfbWwAupCFC15XDy0Ae6RnbEpaPL0Bxk0ntMe7heQxoiWhpNMrULpdRAwlAR4gIVWk2Ix4COeMqgbJzkKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=sOKnAKcBTpJ9XoYd6_XhI0k1mPhRkRjUWnEDrStlov6wlRWK8P1cXREY3PckV7jurkHR8ClCKriLBAcA6u6Se47yIQtG-zTCscYDXw6KJ0QA2DBvURTDVU0uddQ5bhP7_FAXbVuAf39v1vDu8LukdLXWWbR3xLt_p54dI4GVriYjeAmyJS_e-n12REGwYlkJfy1q7B3RPgUjkw-Zl_MvnU00jv7TIbi-w9gagMBSMjlmXA7wSezf68iL_bhGkbOlSPGyIfbWwAupCFC15XDy0Ae6RnbEpaPL0Bxk0ntMe7heQxoiWhpNMrULpdRAwlAR4gIVWk2Ix4COeMqgbJzkKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JyqCtqUPHsAYNGshcezT11rYB6Rp2RgBO46LCq4EDr_IgspKfbO3iN_40uTn5eNMIbMup54tJyiT6Cr5jEsBQrifW8MyQu7brdNo8EiuIlZfjg9ROyTLNiYMJazn8kAHI8LDU6yDEgr3oBCwYxwmxHXtb8IlC1P20xQ3Iaq23zH7ztADcE_0Dp_bwVFg_nECaNRw4NxzngN4RKgU4yzY3HKSoRmzwXVeQKObozVQoRPFCTLVG1N7RiNyQgrrb1Fvrlwu7Gz3FyB9zuZaBxKhSLdsrPxpWy-UpBGSkkyhH0z-roTHOl_NZyhYqMDgH5YiC-WJo-F2P0_pVwAUOvwuPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eP42I3QiPWed8L93e-WfAPsNy-DcHznC1Qg3kKQP_g9f3QaxoepBC7j6Uj8jaCiMmIE8Lvx_Vh8LkvYD4OYdlnC8W-r6XNsL8FtYV1Z0YmS4wwV72fCr9MBUIW5RL3nh2WVxcp5glG2MTXca5WiCtr91Qmn07k3DBtIAhA4BhE6WnusX9RHIDmrlMkbpNx7Zz0zFnneB1w49at3pzO8Q8uTRIupEeWd9w06DwVaBiaR9QRzVf6uk2i2QjakS3CgIxY4PdU7ZwVm0DAm_ul729uVSziofUKy_CKvYdYvjRohqwzLDMxVdonmIIHPdKFhQleLRKtOe1YmFkdiNdUrIgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=PHY-F_1QvrZ7-pvF8goMoOxgarvI9Eqe2HH1OmlZLqQQNuhe05oESyEmmr0i-xPtm_NPHzbRZuJnlBU2FnZfPGWHLoX_4jVK09WYvsdPBT0xqB2JYcyowq0Afm7VUwnGn_EyuOvud6Z0s1oOA8n_Oa_BA-XLh4qM8nXtNhW7ZgyGsaYN_OLyzMIYtRE3tjFW0AE8kYPNnK9rx6IqTyEDH4OqbuVxF13AwveX0kmPiECd4zTVsSxiPk1yNbFM0Hv-2FgU3bMK_2X6AKlPJeOBExItRcM7BQ8GcfWAdCM0ln_YiQ88s5XD3uaqTY6issh_LwJqdPE1QoRuVMNtUsXNoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=PHY-F_1QvrZ7-pvF8goMoOxgarvI9Eqe2HH1OmlZLqQQNuhe05oESyEmmr0i-xPtm_NPHzbRZuJnlBU2FnZfPGWHLoX_4jVK09WYvsdPBT0xqB2JYcyowq0Afm7VUwnGn_EyuOvud6Z0s1oOA8n_Oa_BA-XLh4qM8nXtNhW7ZgyGsaYN_OLyzMIYtRE3tjFW0AE8kYPNnK9rx6IqTyEDH4OqbuVxF13AwveX0kmPiECd4zTVsSxiPk1yNbFM0Hv-2FgU3bMK_2X6AKlPJeOBExItRcM7BQ8GcfWAdCM0ln_YiQ88s5XD3uaqTY6issh_LwJqdPE1QoRuVMNtUsXNoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=HYMNDDz2i-4jmMtNsvaRV0bcfYNGNMA6bN0Ocb5aCPMNZfDsN5umpipD9_KGmHtSVSCQqYSgi_d5PCwOcP1SuHZ5TzQzCNDLF5A7CdnoPuAx-F12R5bOXgxPeyRokqeK_ZZB9qkFKf7ghQD_7CCWcyx_YnCQ0iRJ6bnt3Xu__eUzczvlYoAnwlKH_VnGixBEiUJ9LLzkQSXOD7MpxekJIWWfpSIxbgQZftbvxD_ZKQW5AmmoEbWXFu_ZMHzRdCB7zn6CNkNHSaWx7Drb5LdU5-j1hOvb1oW-XaX3_v2RBtA_9rfKPsw95a-sfM-vGVTOn-Ycs6vuP_HeEmiLyOEgUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=HYMNDDz2i-4jmMtNsvaRV0bcfYNGNMA6bN0Ocb5aCPMNZfDsN5umpipD9_KGmHtSVSCQqYSgi_d5PCwOcP1SuHZ5TzQzCNDLF5A7CdnoPuAx-F12R5bOXgxPeyRokqeK_ZZB9qkFKf7ghQD_7CCWcyx_YnCQ0iRJ6bnt3Xu__eUzczvlYoAnwlKH_VnGixBEiUJ9LLzkQSXOD7MpxekJIWWfpSIxbgQZftbvxD_ZKQW5AmmoEbWXFu_ZMHzRdCB7zn6CNkNHSaWx7Drb5LdU5-j1hOvb1oW-XaX3_v2RBtA_9rfKPsw95a-sfM-vGVTOn-Ycs6vuP_HeEmiLyOEgUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AU4iXUcyZvHbL6GFDScFSSD-PyTtfyrZGWwbehkxI7ZEroFO-t4t8X20mwObPxO1BBqDRX-5dDMy9JkMAe9DX_WQE9qs5dScDa2rliQIo4AUtIHJpECwuHLuH5H3WgaHzRXpt9KMfpOnlKL-bxRj3zIuWjVdWckwqwHCJzGGo5wcUdWr_HAnk4_3E-yyUm0NdbGMNbl5xj5NsIJIHJtIZ0E-ACP-KiF7gCPwkyPhikAOQcPVCqqaZLtFipVJiFhcQSv6xqemlu7PVtjQdU18LEuAzxd44vYF9WxcCuD22N5vUD9pZ77vt7LEIsyyAzD7DQUgIJeIixHIUzF3cCcz-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIPmoTozErJZ82UyDdhiQ9hypZrJpgMH6HpcuoSwY02pqIEVIBTShybWU7VAcxM6DUdVeZ_k0zjnjuymM88x9LMR6a4nukzNRd2vAReePoUXmdyCvWkpe57VGB0wSnq2GI3ToSOyqbH_VSYOijt0BCuXKNvUr0TihhLYSWfnJFcN0Rpr_njW0E2K4byoQp049W_Fsm0Awe5QRifiaVliLqU6KUYmhnLZZPoKUPnFtCazV3uFKuGl4esFLxpDE-omHc9bM4SmgIxGo6dPcJDuj_KIOTNeGkjHKYl-Eo2PP2jJpMOSwvPntZB1-Qe3YcjaLXrELNsWyT4PjhY36C5IJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BshiAVP2f7UDCOO-PL-OTe37xRR8FKXXnZK2amJJ02ct6EtUYD1a7ecpOIjk7I5_3vR0nCYeO6zkfjQauZuUZFRi4XkYIzRLsd7bdKzRYzNDlaltpvz_uo_nVDjN-GCZ9o4z4W2TMK97C8Jh3BBE32mBvosDLmYwFYi0qRCOeeg_s3RS5VTKmSKJOUoYfN1y8Pry9WpRrKRPXajPldiY6Ky-vX7fHvfQpaUikRqesMSwYZczd974G7U4h0BNo5TD2hotcyQPTILkUPi_EK9xxN7zWz_BE3pgECw6GBnB-cDi73ncAc5mIqct7PRQYEKDH9Zgnmf7SaHZxwYlvcKadA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
