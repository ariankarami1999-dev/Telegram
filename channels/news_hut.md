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
<img src="https://cdn4.telesco.pe/file/X8NG3rU_VPDH4CQ8f8kwC71K2QnnyQN67trcyFtZwgo_RqpdHEOn9hjksb_PHK0m89suYa3t0TN9O585AMzNXfMAHoAiApcTlkWlRd8zUn8Osi6VJO0Ak8W8HwsGcxLsJP6_NjTe9mQzFmqdrPFw9QiRniDYEEtlPSN-hW08tSpB8HwNT0t95WbskzwyYs70iyuEBhzs8OuMb-692oq1eyAwjcsTVRwx8aT5s92qxA_1d4eRQUFSHP0uPy95vhrNYIU9LWYQFYKQ0qRn1m44RWmuatPrv8eDD3PiHHkOVY6DeFYy5WhXoNrtg1jpgDzNHktzfixmVJU9yx1kwM2Q_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 17:08:24</div>
<hr>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlWqJHnUTJwIsAfpUOBHQyiFV2V1C_8PcQtZ8KHq6mAmN-b5Y6nlzvUIVVN0TL0JRtH8yjxTH2NIEKVu3GshZMh1oOhc5yqaVZPT_9_b055v4QOCnD6u2ohZjOsLgNWU8EGqFb-rzRqkxxH_9pdlrpr0XvIKDNhMchYXLfkrmHKgPvI8fjQf5x8sMdP1rsLY3zAdClK6ptpvRBnTDpEJoa9INACWRQEcFIOoz1Q8OmzEstyvrPnNocTbRREAEPqba7Fbxa9cddfUE3b4CGKuJt7Jg-7F6G9tByXvOXlWKFrnMW82AHVwAbokZsyCo6sTWTPN_4cJH5ML4HilZE9PRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-XPh0l_IM15R_0h3Qw84Kslmt0VUVNibWhrBr8mZ5iHEDBSSd35pH2zYhSIjhLAlFsrSRabRwGthyBxNMsofw1r2nYWkHtRd-JXEpHNkd09JakrhiIcrQV4TpMyK1lF7D_jXx4dTspQNiV8mPIeyLcGYUIBC3r-Dq-dOW-UW9sxI1QaQB2EWjMGJQnuZpiuU0HNlcSmepiM-mLE7SDJ1VWGgIaYRbl_jsozxJbzorqQqkBaE0oEQceSPlOMy8N7Sj7GF_fIhe73-qE3CmtqwInf9HONtE05aOp89MM4tMl_w1JYFh-zPoR5Q9KkbKL9ujFPKoTI1G0MXhsmUlV9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gngehLb536bd5d7zN4l0GqiWdfwLwLV_DvB5zfnH3S3gbLR6gyEg0jg_GYz-2Vv8BEGSQhRs-TXzUI9RWUpYdiYkctPpCWBODGab0jPQPw6P5zGotcrB2cGdrF2vEPavdP0_qCLtwBW0Lo3zlhseq3BIGgDl6yBtGxN74gSh1thAGPHOKxygE62wfbTF8Tny4Um1QrWUDCn8VbvhBcOVIu5QskHkPw_27RRV4BsTZigb6O8EbCwT0gYNVyIxPL8pedVn_fd4BkI02IsOsWQpk4mRvLRL_wGyyMq_mKH1lysVPyefTOYtPeiE4fXnbLCEciVONk00LUB-GFTEjCp0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBI0WcjaE_syMQSrkLGGORbIwldp7Kj58J4qMh3VZRSfoU6RQ8Vqr1q4XEqAig_xfeT_riXzXmEjMcnSm-WR8FlHN6yfeVO8Xq3-uhb7HYP8g6igo4hBHhSWShj5wb-tOU9sW_mEd1g12_7DDKUIQfoYWfRyZ5sPnP2xYN-seTl-pvonpNObcuV1gMEV2CNMST2EaX32gtky3FKfygCtHYJTZZJ814bvFAw3GrWXgYF8THBzVhXFD79wUm-lFeEn9ILm2FPVt5IkQ_jOFJLDKuA29sCwJoJncZOcHQkYgeoXAuAa7PDpjhup7xZwJyLA4af-DCYYDGVyw4JJxwDmZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65273">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65273" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fapL9i97oPPcxuF7b_ULQTDmnEz1ZTYDj1u6USZri8Kj6a5MkgpCKzNqP6klmYm_HtZOzEzSx9XlTC4S1m3Q7IHVAistgRXiJJkdI1Z4JsKueg8-O3G9gnFbkyA18WzvGIM16tOkDWUOGDE4JGafR-BRw35-GOxFsc895-VIaji00jB1-z9i8zL5wp6uiAgkWXyD5NDr0KkeTo60_DMeaWGot3sW3KtALBBTLWBZM1O_874nkEyuV7xY84K323lHCfpleSQS4Wfj40dW-crV6ItyrrY2VfAVNT2bP9mrYovhVervww5HVpD9sMvLB7RkUIX5S_DdFj2vmEDDd6iJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=moWV7jYC-8fjQdQvBOzH_dHg0RtrVs46AdjvBKS7HcqIy_IIJKYXSP9Ev3SqFXZTP0EjQgsan5zqtKJd7B866FnUVWhS6e9cSQHlDdtxMAudZ1BVF_QBouU9hJQq58TnJUWKs36iXOR4V1DIqHyjSoLRD-OWsG-mbgnJBT0Qfazl_WhLk38NBqfBfolvnmSTBWMhEUXApeTqxPmAqkHDL2lZe7ucQ0_N4rlYytcXm6w_ky7UJYbKcIIscHCzxS8x2MVAdfn7RWOupX5_52wKdKQj-9bDQhkBb3JPtzZMmiKFpJ-ttv2UaveQfSUvPp8zzUuPMoeg9R5FvNlthGI9kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=moWV7jYC-8fjQdQvBOzH_dHg0RtrVs46AdjvBKS7HcqIy_IIJKYXSP9Ev3SqFXZTP0EjQgsan5zqtKJd7B866FnUVWhS6e9cSQHlDdtxMAudZ1BVF_QBouU9hJQq58TnJUWKs36iXOR4V1DIqHyjSoLRD-OWsG-mbgnJBT0Qfazl_WhLk38NBqfBfolvnmSTBWMhEUXApeTqxPmAqkHDL2lZe7ucQ0_N4rlYytcXm6w_ky7UJYbKcIIscHCzxS8x2MVAdfn7RWOupX5_52wKdKQj-9bDQhkBb3JPtzZMmiKFpJ-ttv2UaveQfSUvPp8zzUuPMoeg9R5FvNlthGI9kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65270">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65270" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65269">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB76IeXPa1lGkgHpHQxLsJB2QTSRHyEqj5_3XW33SeHClwtHQetTF9Y8rLEw30udtq_7DL1AxjqIKSLoTjTZYnbX80FaWbqA9xO6uIAEKvhqD-KFTdufnOv_OVwN88c1UrvH02ajbIbyIVJkfrSRpSoQw612xKOqdCUtd6tdfkaAubYhJUy7AsARQA29FLUJ0ObTN37ZGVBWTBjG_a6gz7AdZ7Gc9YwTymZBXc3yzx-LvyzqZty4Yj_xbWc-baijckmT-xJ5ZuGcno6CHJC6ThCHG2d50KWD4h79KCBBAUpsef56-A0cf-fZrRnZPe-im6Zn_kJngMU_Eph2xds_0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65269" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=E9KnsRmQVZmbSe2dcElnjZ8Er6glqS8WgtBwPjZTmu9EAGrXpNMphXNg64ZYwKfTXovKcwyGTZOaHKwHwMUj7NyxSX3B5PmavneLrcV7PcirXHIvuSqupg0RWxmkr4aGTf7CN5_SpbzIqDtrPRj1DaJzRAAgO-d4xQyqKstX18pUXYWok59rKXnzEAk5-yV4lJUJwXfAeHSavkms56Asc1UT2uNf17TfsQZ0RzuefCIRvEm7V1eLN1TZP8aSsFCSN14ey9GF4HJZ5SG-EOxg2lmXab1oPKXiZIPzi_0StdEZg6nXSUSlIJp84L274IFsvsTvqF4oLvhOxvLwUUHW_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=E9KnsRmQVZmbSe2dcElnjZ8Er6glqS8WgtBwPjZTmu9EAGrXpNMphXNg64ZYwKfTXovKcwyGTZOaHKwHwMUj7NyxSX3B5PmavneLrcV7PcirXHIvuSqupg0RWxmkr4aGTf7CN5_SpbzIqDtrPRj1DaJzRAAgO-d4xQyqKstX18pUXYWok59rKXnzEAk5-yV4lJUJwXfAeHSavkms56Asc1UT2uNf17TfsQZ0RzuefCIRvEm7V1eLN1TZP8aSsFCSN14ey9GF4HJZ5SG-EOxg2lmXab1oPKXiZIPzi_0StdEZg6nXSUSlIJp84L274IFsvsTvqF4oLvhOxvLwUUHW_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=dBslBvrYhEK_CWGJiQy89UiUuxAEMvF-266Z32t7rB2lPHrQ_0RCKPvDCuzp6q3kFLSNo8fbWdrTULZCXF2Pa030Fal3dsJ5vPn4sKV9vAI09PxdN8WbTUZzFBSn4HTCXeOoSD36Cr7PY2hMJttrzTYtqY8kKpWLGmiwYuyQx-QzdsBIt8YTEqsZFmW6-aHSRwus8T0xWFrjw1z78j1sZrpEhk4JOB37WSPDChkh6rMDjGNGrPkZsLK0sWI8_VIzLhwqHlJqsAXEIaZw4_5qu5ObIDeYMv8ezTrIDIilvr5vJVqnCrRKrfPr4ES-32MmwOyfwrVOpBJLeXmtygqAbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=dBslBvrYhEK_CWGJiQy89UiUuxAEMvF-266Z32t7rB2lPHrQ_0RCKPvDCuzp6q3kFLSNo8fbWdrTULZCXF2Pa030Fal3dsJ5vPn4sKV9vAI09PxdN8WbTUZzFBSn4HTCXeOoSD36Cr7PY2hMJttrzTYtqY8kKpWLGmiwYuyQx-QzdsBIt8YTEqsZFmW6-aHSRwus8T0xWFrjw1z78j1sZrpEhk4JOB37WSPDChkh6rMDjGNGrPkZsLK0sWI8_VIzLhwqHlJqsAXEIaZw4_5qu5ObIDeYMv8ezTrIDIilvr5vJVqnCrRKrfPr4ES-32MmwOyfwrVOpBJLeXmtygqAbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=Ix2A1RhhjX0xBkN6g5__C2lTzHTTikhQ-9oCXZVoATkvuhAaL7mCHXn-zenmuW-9Q_BUoCwGdqKp9L8VaGeEGa7J_dhcSuQcGVUZfNe5Z0iWGy6_SpZVnNR8TYvbRXgt_mKKSn8Bm9UuIDynr59dJBvZFnuZODyxvKYXxAaotBxSRUPw8ztdmtRNM6l2odspdmeIsxiZD3VelKFjWMgEPhfBE4dOFKiRYC2Ofu3Hpm_3q1siTFF6ODg9v-IF3ZEuPSPnGWGHeH9Iik5T6aMayVDqXbInaQJE8cmYg0TnIb1Ud9so1WZSYY2yQsGh47486doivQP6osu-MdK8Vcxcdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=Ix2A1RhhjX0xBkN6g5__C2lTzHTTikhQ-9oCXZVoATkvuhAaL7mCHXn-zenmuW-9Q_BUoCwGdqKp9L8VaGeEGa7J_dhcSuQcGVUZfNe5Z0iWGy6_SpZVnNR8TYvbRXgt_mKKSn8Bm9UuIDynr59dJBvZFnuZODyxvKYXxAaotBxSRUPw8ztdmtRNM6l2odspdmeIsxiZD3VelKFjWMgEPhfBE4dOFKiRYC2Ofu3Hpm_3q1siTFF6ODg9v-IF3ZEuPSPnGWGHeH9Iik5T6aMayVDqXbInaQJE8cmYg0TnIb1Ud9so1WZSYY2yQsGh47486doivQP6osu-MdK8Vcxcdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mH3KX3eyUqnTaKDZxBBy_PvOixHxs1YPexzyoZCPA9jR-gZOI-GUsK7I0jCZuFPqpdQOqvLHTqRU3f8S-bxQhxv-sca2gM1L_A3Z6FIFR4XIBsoWleV3jVuUrGzl6tMYfNoAGAIoI5DV_nlHVKnnPJaNpQNGoUk_KqRFiyv3cSu83iU9PMpF5BnU5nQFgb24ifyeY6z6C64kZ6Izjvsmwqu8bYVN3VQ2DDN9TtaUqaz_e0C3ac-dUn1I06vns82roGFQ4ZMr17vfudlwjHHw_Mvps7yQA4wHb_sI-12XtrpMfByYdDv7xrIdmtCPSHIa_sNjt8fo4INko2Zr9nV-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Majr5nTQxI4Kz94shkDIOoI3aYsVUVeE8v7nAh-EMn-N0rGKWOe-CYdnt5NLx1Z5RUSk24O9zmRLtzkh_wuReSwQJAuoQG1hrB9abfzYn6pu13BervoGDkS0cJ0UDWEHdQvUMbTCK2IjlzzlcIYJmjCp2t0v8yjHGh7MjjUQfEcSC1zE-kGA11M0-tjMl73Tnd34M5hv9qNkcqvjchlWtspeL3c1x0tV3jvM1a150GFaskq8NjRRfw6SKrwVsC8uyLotB5Zk0mv1w3npiSMSmwE4EGX_OMU2b2RSdK-Gis4pdifydSby_J8RXFd0MN-SSxy8aXhP6fKXxpD3vn3ODw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ef4TzFOC5vwiYGE5M9tetvqNUGjbihoC_Cx7WS-grCllJJCWQ-d5CXPsL82QBZ-CSu91XRDyT48Sx5nC239y78a4rLeKwGsJdCE6-D8zoMfVU8SR-AZqcpCdGadfTTWS5t47mKuWQOO8pPR4wFzyhw4erQ1yU-AfF2xKCTQKExMWMmv3ThuqYgVahDL0-xhYtidY29tsq-j7rGVrEotdrsy76R_QQT1b1No-wKbkiWMaxVgz5W4B8KCo7Y38F5A3Cln2Akmf0rrg0hEzuM025OGzMpn59iasV96txI37jzORsbcO_Ios1zkFdv5im3WFhr2AdkLYgNJk2WDVZS_p1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEREMV5j1GfqoIwqMkbUIjW5J-DNyDGo92lTiOrAWs5YkcKYLn_Rn6Zcq4Q0-CzqS0I7xt21yuIarJn8PX2t0lTEQMNlkGMmSxLhcBMlXpbJ5S6yB6i755oakm9jGFQsjPw-5nspTLnn92k0LPk8_LlytfDEDEs5MKPeyPdQCa_Sdc-cThb0J0GoQJ3J89t-mtbB_fZmaf_7JBkSB3eh2Qif1UhGG8rorpNdjH-0ofXU0J7wrpaXhX-mbs2dgUVECcdVgrePvD12yf5xw6s_PM_nWLay9P6MyuNA6akfeyglXsNolUjXSfinXuYo4gX2yrunxMHIoe-Uj4ZGe8EiFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov47okgl0i5aL1_5AbVNubseiIfM-j5OWPNEJvBt4d46IfMY7sl-HdyRBwsdezdXF0wENCsCz4kkx8erXrtSNkEbhBdCuQgUo1N_k38rmnFQhR1eBnUcN2E3Nkgr5SS7FZZss3XASuCt-0Vf0w6BkfP6nhZ5y7xpKJgBRMW4gj1M6xifFaWsmj5QqWSxvQ8KKpZ-oHPRTGpnc1LVfas92Ids3Z-bhHKtUpANVyl39VcGVhe_uHIqD5zsBEYCwO5STlmBwJCo5IDj13yNMA3M6LoPmxvhxq4I15K0snN2PmdPL11tN_Izo7MvUFdI038Pe-fhm4mLs3okr83lT6jx3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=aC6vnKnhqZ_TIw_ZPeWRXb1QCffPQrpoAawEsuuNt_jgKefoYWSpsS2ZBIASxNXpop3FHpeY-6RqT2wavsHZW4iKKvAJEEfRogJBOmPpLCVYT-fKfUDdiqFiFfifOXm5v2rPWXXgF24XoVjt0L9vPFalTjh6afA327_s_u_d4kYdh7F5IGSkh9xtR7X4lrm83p5eIdCAFmSyWpi6NAOMeQyfCdr0lrMXvkwWuBbB0Ljx-HNy92fFy8Mh1qhtb052RQvbFdtlzBJDVklvEgpaujwi9IPvnn7u-GEquyC7DJQUHpln-bnlTUZE5SmJxFdVRZBG7nquE5wquI8-qYUDRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=aC6vnKnhqZ_TIw_ZPeWRXb1QCffPQrpoAawEsuuNt_jgKefoYWSpsS2ZBIASxNXpop3FHpeY-6RqT2wavsHZW4iKKvAJEEfRogJBOmPpLCVYT-fKfUDdiqFiFfifOXm5v2rPWXXgF24XoVjt0L9vPFalTjh6afA327_s_u_d4kYdh7F5IGSkh9xtR7X4lrm83p5eIdCAFmSyWpi6NAOMeQyfCdr0lrMXvkwWuBbB0Ljx-HNy92fFy8Mh1qhtb052RQvbFdtlzBJDVklvEgpaujwi9IPvnn7u-GEquyC7DJQUHpln-bnlTUZE5SmJxFdVRZBG7nquE5wquI8-qYUDRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGLFmy2yuddjhltI95dnq7kgmxiFDAQK9YorZ8FfEDMPAxB3DoF0GlastFeT8YMJDamL4pcr0O1vujt1npCaJiSgimAeMmrUoDTEi0Nopqt2pHmwVg-VtOk_3S5rp5Q7EmPodEnVpl1Bq44oC6-dO83rgXvgcbGe1sJlshDhb0rV7gvYRmNeoGntk6HTmH2eLsc6rpYGMIuOaNpsangTer8tb8YvoJGKdh6SV5ELBduqWzclGTg6izY75QUGRsn2IOTooKrMpYBcSv1AggiAtFNKafShm_eZiyx6Ed4cgUSf7HYZ9LzwE4kvcMaF5wKk0_7PlLlfG960r7uAQwihRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z79UWi6keyZbAoFsDE2bDS3L-Yv8ce0N_qYufHYQc3ABjOJayqMv2hrN6R-PhWwVQJg1W92rrnitndVr7IeDviE3QcJTzXVm9IoO16Paq-T7Rcd0J9X5ZLvuEPr0xiGH3rM9tDVWJ-g1XIFciixxzdA0VQIwbBSlv-I2kjru7BUBRd1DLRel2cj-qtySw9Qcs5ln831ogVvnxydamgLv4ckyhFJ7OZ_IB3ZtIsli3bt-9ebxtB5k_ePtkGu6O-0DL1HTTy-ArhdVy9EPfGvLVLiFXBpvXdBZNbxN8lVQlmbN7tbLsavPASPsxT7dJmvh4AQfKG-TFIPG0JBS8rdRkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtDFH7Vi7OWC5qBQht0BD-UzHFg6lNVtzGthFWFCCUiUdzutRowqXPDqJ-Vz2Z5_-PU0-tgMsvRkxqcT5pr4Q8znA4hRYFR10MmgDT6HSd9-nig0Z4VlS5m6FCtndeRRa5o2acw_MEWzvPl6LUAVe4FhYYmCyC79YPowVgC79lX82B9oKXdaqHuQo8XlxIt6qQXfjkhFELU2xGVvOHWI6Thx4yKfQFl1ug-3Xsg81fZfukAUwDj4rzq23MfqTvMy_KrOkS7yGONXZlx5z92JJnaZy_0j9ADUgMsyVtc21F33JC04gBgnSLebT2aOAGEzDWPGSG26TunH9uNl9LFrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdFkkmdQqsg-Clj2EHjwDXvY2UV819y3uR8kRNRvapxvX3UrZ5-_eI6esd_IGXaBdjdfZ07W4_X-gUsHFhqP2JonNAeZhDV-r7BwcGdJx9KKzEoyR2MEeL73mwQHsqsGZ5hyw9gmFwEKN-6WLdwA0z3gjIuMmYCtjkE8dPyUkau4-w2QFXhrHt9kXBGHCeR1aMRt5aEOlrtYK9h_UY2O4HSKhdD0nQyZDKVu1lUiqyLRGpNRsSegHNlUggVxBcT_3IjllJF2tKL9EKPEOSRujcTXH-y5QaaFoVW8ab8U1A-t3bHXkUdo9nCSoBDma7t7Z2EGflYcltRt0yP6LF5gtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgB4At4_3tmFgSEgV-gM0lC0bV28jtPJoqR_QNK32_q_Z7rD8BjD5RoBAlsjoc-Mjiv5o1CusJxAkUSGiQaulI7dUa5HTE69EWoajy-Hg4R-gEXLdZtsjt4s9_LgxvGMexB0Au57ixHmZldpHM9A5cblBSb3vzWWXVHuMHGHPmnFg3liFdEfLh6_jLnrQLluNoZnHUeuPBzq0qmDk6dM8FgwqcVP1cr4YiON6yPtV6qU1A09EYBjoNTV8jwlKLY_CoQdaR5TDp1dZE-gxWuLKbKweDkRMtwiw__G7cssicIo1Kkzw6Cddm1kbnTFykFvYAa3bp-FPtpykPD0hnsfQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp4j6Y7ozZch88nEFPVY-kFF1rspL0pa9QOrf9rTUfaN2ElCF_i8KGAGMlW1XPSzs3PQR9SJoc8bkyWN_U2p872HZn1ygJjnrnrLVmzA39sJsrSH5LaROAyYKd9tzzN-1JX2gOjqta1k0KhUsqDOfj9gFFexr37n0rugALouAG2fw5rVSdv50X5ySXeH3EFNsxixZa0zQbiSQ75RLpRXD6QPfbU5KbhKDOnBbTRpaskP8WdPlIJCC4EsfCsvPGY6kjbOTfXwlrYbBixnpcrxdd5kd8Mt91mJBPIjlICMj4GyPmFqEOCdvgNFfjNtP8t1m0KImKhSp5qsJdRCnQlftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=EyEoLum_jy6xLtjnKN4KLEfPqk4AxrCcidSwPWyVtxnqgzh4F1DgUQBFaivxmwxLZIYdgnIGhdYrC3chXHyip3CsnRYs3bu0PCGJkS0DvnozOSsgFSc3prJBNqF-Q6valDgbZEGpWvvR9HpDui75kdl4mh48Tt6VFJLzQ1hHVncX7zL9kih5ELHvqha7gtl5m7Ml_ycKf_U2GSMmCaJkKdKUTyhUV822Nm2yy12lnffV0kbDz1Efmgo1bOT8SNllhNpIIzWzN0a0Ezysb4-wbLd5hMZ5Ng9d-CXOCSAie8q1e8gcPgDhES5dr_LkClNJeaqasFf6n3xSEKs-lpEkyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=EyEoLum_jy6xLtjnKN4KLEfPqk4AxrCcidSwPWyVtxnqgzh4F1DgUQBFaivxmwxLZIYdgnIGhdYrC3chXHyip3CsnRYs3bu0PCGJkS0DvnozOSsgFSc3prJBNqF-Q6valDgbZEGpWvvR9HpDui75kdl4mh48Tt6VFJLzQ1hHVncX7zL9kih5ELHvqha7gtl5m7Ml_ycKf_U2GSMmCaJkKdKUTyhUV822Nm2yy12lnffV0kbDz1Efmgo1bOT8SNllhNpIIzWzN0a0Ezysb4-wbLd5hMZ5Ng9d-CXOCSAie8q1e8gcPgDhES5dr_LkClNJeaqasFf6n3xSEKs-lpEkyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=cKiGa9E7aVxrnV6MUFLB8taUwddu3KCRp0QR3XsjldiquX0MlxqD4xVsdAJkf7FjMTPAT0LIulX1KoB61nOPtDQLQahdM205m48Y-kFx60rpf05UvC9ytCfPsJGvBbTsjMzGrBhvHK1uUHBPjcJGfzHIOyv01-pabjcRIvQl2drTVQLxwStpr590WQCZIOiuzKwHyNMgyHlwufJw1aF8E-N4f0cGFFnI_jKzh-wVVNrhfKmF17FTjVJMAXfpKGwQWQpY2j5GgetKaFMTLnhrTTHZn6X9ELIxGDAxtyI8rfloI4mg2jUgM_WBp2J6pITdvtq_3ZFDnipjtKS-iompug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=cKiGa9E7aVxrnV6MUFLB8taUwddu3KCRp0QR3XsjldiquX0MlxqD4xVsdAJkf7FjMTPAT0LIulX1KoB61nOPtDQLQahdM205m48Y-kFx60rpf05UvC9ytCfPsJGvBbTsjMzGrBhvHK1uUHBPjcJGfzHIOyv01-pabjcRIvQl2drTVQLxwStpr590WQCZIOiuzKwHyNMgyHlwufJw1aF8E-N4f0cGFFnI_jKzh-wVVNrhfKmF17FTjVJMAXfpKGwQWQpY2j5GgetKaFMTLnhrTTHZn6X9ELIxGDAxtyI8rfloI4mg2jUgM_WBp2J6pITdvtq_3ZFDnipjtKS-iompug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=k7pprI-Xm05oRlEwR6JP48okI8sY0YUZXNiT3wEfMpRtN4-KvO4_kGw7sbfX2GnGBQ1e3XHQi96CH5jsju2VH-m54_w9_FPK0s-3dCcTSrsM20DFb8nqOVbtF0uZyzZqsPcoSs-AvMhaQILsKWMb6YAdtkieDf_JD1g76I23OdtMZ6m55Ga0xlGP4TaPJkfmYM-FkgWbZ0vDsaGWuZZaj7XOmINslojM1qYTuPzAdU1k-ctrhm2HYRmVZ2ke48eqt7h6x8-yrZMoQ9U8D9VOk-KuxHEZJp1lg-RBuKViJWR0Sz2VHCkHNXewMUybxIZL7GWWhyu26et_o3MhiGtsKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=k7pprI-Xm05oRlEwR6JP48okI8sY0YUZXNiT3wEfMpRtN4-KvO4_kGw7sbfX2GnGBQ1e3XHQi96CH5jsju2VH-m54_w9_FPK0s-3dCcTSrsM20DFb8nqOVbtF0uZyzZqsPcoSs-AvMhaQILsKWMb6YAdtkieDf_JD1g76I23OdtMZ6m55Ga0xlGP4TaPJkfmYM-FkgWbZ0vDsaGWuZZaj7XOmINslojM1qYTuPzAdU1k-ctrhm2HYRmVZ2ke48eqt7h6x8-yrZMoQ9U8D9VOk-KuxHEZJp1lg-RBuKViJWR0Sz2VHCkHNXewMUybxIZL7GWWhyu26et_o3MhiGtsKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcEFuHw2PaL00qF4aW-vZN6Dxax42tTd0LuD4D726-xad5kBCtUEquA5zTu2Q_QB8Qt4rg8KrJe2Rz7Z1XuLp7uQGAqnWl_H7e-Oj8-o7ul9EGChwfEKvwoFFMr6FacdHqv1G3Vw77z2ZBplZZP8liuj5KkIbmGpu-VSfLV-vrrKQSgConItTimKpyQGC4XRdtUrCCxeind-L79LyvmPfu_XbsKv5iQoGVdbLrF96zIDS6QOCms-UtWf_C1xM5za7Cyd72YEvt4XLFZDcTsZ79469c6Bdd-IE38o6CekPOHwrUrj_xIY7Vjx6wKmkGXzmhO-NE9caM_FX36MHXrmtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=Gg4SpwBETDp-VaMOJ4vRt-iM6ZgjePfR2W-dA0jCNXvmT1BAXoLfsOUbpBtfqXuGV5TP72tTbbCjIC_kOEkt8eZRM6VyOK0mzfQjSZ1X-0p0PIygIx-ESq7ncbhhrpm-62Ysp2MY8fI1Luw8lMTPs_eRCd69Or-9QJl6ZYS4fapjpXCAVHj2MwlWgg-conyHQMbnBZhLEcZiXf7ue8O363RyHN3YpzAfivUKmV_GKx3cBfTbKKkNW2v2CcT_gu1e7fDZj_JpAA3XJOcFkPfoXwwsHpu3JQLcYPRhgxj8WD01Rz5Fp0MlPROoxFtqsI24nfWbTGw79RNEwQgaAUqzOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=Gg4SpwBETDp-VaMOJ4vRt-iM6ZgjePfR2W-dA0jCNXvmT1BAXoLfsOUbpBtfqXuGV5TP72tTbbCjIC_kOEkt8eZRM6VyOK0mzfQjSZ1X-0p0PIygIx-ESq7ncbhhrpm-62Ysp2MY8fI1Luw8lMTPs_eRCd69Or-9QJl6ZYS4fapjpXCAVHj2MwlWgg-conyHQMbnBZhLEcZiXf7ue8O363RyHN3YpzAfivUKmV_GKx3cBfTbKKkNW2v2CcT_gu1e7fDZj_JpAA3XJOcFkPfoXwwsHpu3JQLcYPRhgxj8WD01Rz5Fp0MlPROoxFtqsI24nfWbTGw79RNEwQgaAUqzOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=hwTIHmDQDT3U7VL46QCCP2jjt_kgVOrGtvEMVXl9khxOl85WcM1P0JQ6sIBPYcNTCtVnYORvm5rHwBPG-J2bcs4qsy9eYPYA3tITXihMnZYdw0B-VU24bx7xdjCxvMle7SeIkvSVLgvWXo84qY7QhiZY5okb4vAzSRJHDPjYlduZPP9P0lw9o9Ie5yQiMDhDfmLVHe-6K2WkOiEEC6LL7vAIVgduU2ZhcMQO66D2Lb05raj1SxadUfgzFYYHU3tCT6NiDpVbzHlVP6LgMRnkL6_6vCAECMYaKSzcx3rGY_IBCi04VqnzeTXsUWLfsSTdV8FtHD6_at1HQ2aZ3GOQag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=hwTIHmDQDT3U7VL46QCCP2jjt_kgVOrGtvEMVXl9khxOl85WcM1P0JQ6sIBPYcNTCtVnYORvm5rHwBPG-J2bcs4qsy9eYPYA3tITXihMnZYdw0B-VU24bx7xdjCxvMle7SeIkvSVLgvWXo84qY7QhiZY5okb4vAzSRJHDPjYlduZPP9P0lw9o9Ie5yQiMDhDfmLVHe-6K2WkOiEEC6LL7vAIVgduU2ZhcMQO66D2Lb05raj1SxadUfgzFYYHU3tCT6NiDpVbzHlVP6LgMRnkL6_6vCAECMYaKSzcx3rGY_IBCi04VqnzeTXsUWLfsSTdV8FtHD6_at1HQ2aZ3GOQag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=EHkH-DDTROXJ_CUP4tQHuft8xfLiP5hWj12dyFRyTBXIGadibmGtdnbim-DCIZs2MYELHu1ph6giRyO1MlOPExtYmYKRu5e_WMzHrcBRcXm_JNuh10FFQL8Sajm5Y7M16yy-myu0Xf5fOCjfJ6HiGO5SCpS7Fb8wgv9jTWWkxDooKV4zaHCvD-zkDKfQo1T9B4gTRZ1JVbhB2xhVmgzQzHc2RSgMp3003yeWgjPH8dg1MxUEUEe9AxMOmmh3v2ycNmitDJ8nR1pLYcnQETXew4S0L5L1TGD4ouoGEwGA_Ov_cyoRnxVD289WBUVdORj_REXiQ_HYMIaoD4YA_y8KAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=EHkH-DDTROXJ_CUP4tQHuft8xfLiP5hWj12dyFRyTBXIGadibmGtdnbim-DCIZs2MYELHu1ph6giRyO1MlOPExtYmYKRu5e_WMzHrcBRcXm_JNuh10FFQL8Sajm5Y7M16yy-myu0Xf5fOCjfJ6HiGO5SCpS7Fb8wgv9jTWWkxDooKV4zaHCvD-zkDKfQo1T9B4gTRZ1JVbhB2xhVmgzQzHc2RSgMp3003yeWgjPH8dg1MxUEUEe9AxMOmmh3v2ycNmitDJ8nR1pLYcnQETXew4S0L5L1TGD4ouoGEwGA_Ov_cyoRnxVD289WBUVdORj_REXiQ_HYMIaoD4YA_y8KAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=Gn7ALzhAMM2xVkoaojTm1GmpE-q485alDwwE-djkSX7HSN693QVCKMNOM2SWYMWZXmidUUlLbigacD_Go16i_ge15X4N-cwtizjdY9YKXovzqFZcVYTXIa_AYDMI1WCoCdoSHRAHFDXur-YRBe-zNEmM01ktwRVJTQ3vNuYiAih_sPlMeikeMq0-kGDsyvZ3if9UkZPFOa4vXR4vUw21J6IUu_1IccJos0u6keRa44QaHxV3QVPm68xS5_gWZLoXcn3J62bRDUcMLspyqaVeWAQOjG-T2JgXBilGKf45mLFQ1joFvnUczH5fJAfYnvJkYWrB2WuavrsMqkXUE2mHGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=Gn7ALzhAMM2xVkoaojTm1GmpE-q485alDwwE-djkSX7HSN693QVCKMNOM2SWYMWZXmidUUlLbigacD_Go16i_ge15X4N-cwtizjdY9YKXovzqFZcVYTXIa_AYDMI1WCoCdoSHRAHFDXur-YRBe-zNEmM01ktwRVJTQ3vNuYiAih_sPlMeikeMq0-kGDsyvZ3if9UkZPFOa4vXR4vUw21J6IUu_1IccJos0u6keRa44QaHxV3QVPm68xS5_gWZLoXcn3J62bRDUcMLspyqaVeWAQOjG-T2JgXBilGKf45mLFQ1joFvnUczH5fJAfYnvJkYWrB2WuavrsMqkXUE2mHGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwL9Oy1qKOdeiZz5pf2_Oa_OPH-OyQ42ZjyImKgXIvWyS5lsAMAjPhSNe05E-5BQeR1r8MoODiTKwEOhpS02LWHpzpX4707MzMUOZnYaM0XthUB7nHj2bDO6q8pY6LK386Hj-r46Iusg21D53Un3aMM46Ay4dL4m1Q3-UmdoC9oblFADymv9RVZY4l-PTpE_qIufkKz36e_aG-1FhQ7M-s6HX0CvdyIKyJVrhhD5A624oD7AJzcJ1VU_HRVmRCY_35Ei4yjUcDS5G-VAXXMs249G5TbVTvxNlDu-mXYsz8ZlAOgUIkibiNeThpMdb0tx1Kpr7llyMArfp4ALlDKd8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pZ-8Esmfvle9FQUeA-xcG1ieKwlCcXqNElBSC675e4My3hVy00IpXRP0ijQjGkc7qpE7ZeJE1dyrX-F8jWJ28R1ruHaJlpsqr8bY044TdaI-ahDjUUqUFELEWO0_itBnVHiIOou0l1p8d15mYSGkuTlmrpcLdonFo0VE4aTto6WqRwJ2wI5FxgpGvCUF7RpGVSMTdYoGpO3zUkgd7ZdZrb97byvBhXiyXiEalVBL9Dho0GMbE2ya_y8SEg3xIgekWGnFJIskO3lD35vfIFpflBs12e3CVbmuwsz2oN2587oQdLVKTh_ek9Wm7BDN0VzwKRmIsTZ-QayrsIqLrYV6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toLxqr-HEkC0ERuq9tuHnIu5P7TysXYCptyqVHOa666E_B-m7vPlXLpgDNTbD6XqxYwf3u0tkKi4J_L5JXE776X9ONGB7TSKosBkT5FjyYRsi06YaeHJ00UfqhqXQ3njd__ZFb75AMiweqZnSoOHQegPK7-gRJ3VWNblw8kxt5HyG1HNkpTd5iXMGUBLEFlb45IXC4hwVVeU3SOGYxr7BQD4G9rV2ASu_DurIgK4l4KPTfbR7HmU1IoE52CiC8dYdFIP2_SIREk8rze3cC5-E6RDJpzLLSug8p2QS1bthrCjDYcfoy4-K-NmH_8BUhUMIiNkbi9TQ9cLxO0omz4kGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DnOusj2DxQlR1r64kGtt9MDBbQo0JofwefACQwTe92WABGIFM2kPjNbvE3V78eDrzso-4a3NBYnH9q4xM6wtpIl_q7Rs0VdhyFmr48yhI1PpDSBJuPEJz-1rzs-semlnlMBrIjgdCb1QYXcUOimdqibhm8hZakwRl385dO8_988ty2zgcU6vvh8wF4PrUtD0TGmvivq8dr98oLCPCfl0vfaP3NMtnIGzEB4a5a73BXoKond9yXBWLhOiGX0pKaDD_VJK2PXyKzc6tQkXgf0f6jUo2ac51CXg8e2mdo0IqlhsWI72i5yDkM0htC7T8bOomHAayXiLBK8EL33lGs09QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmpZ_EKa0mpITPexwwAU7lW7rNudSdpy8w7FEj1_eImhEeMbz-qG7USnqfDlXyg7N2-FrU9vTfkt6JTZ1_-hkrQHqpEQAo9Od1ucQYupPtA66ze6Zwr8d0EyegYQwq4pi7cOC9p7402lfI9P3eGSMeR8uOMU08NShs2MOzRvcN-ubDMTxCoypp4TBD9XI4HZfzxm8ZJKczNqwY6nxhaN6IpXZXna5FyYT-1ecn6p6GgDcPnUDfZdcC_bmhaeSxk_GPkRjFf89VRxqst8qlptPom46Jnbt8mXe9MEuva-7rNMeSM7oSJIEP0aEM6QgXAWY0Z173ZbnAPQbJY7EnY0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3XTWPEGIGU-zfnySmhKd-SgAKBebJd7DR2x5i3ULqVrWn1GxWOeKI3YhbLJE8UzSOQuO5OPQOY1Rld-KGXit-g0i4TTgnJ4kRkwc9-XDUvINP3-9WsyJC-lvdC7AcwkcHUeHB52ud3GLerfXWJ2wfIXq8hKSOxuq5fiID2-UOfXXN3AMnzkPn308U8ir9yIl_mztWruQ2pMxZgTIWpqBU1NTKMa5xnnlwwaZnkY3fOHeZuhRXqqNJg5HmMBz38zCTKETxv9mBDHIuEcJI0_C1WxYdNUNE1OoYaxlAaqftNOojMiH9Hir7ELD91uToJ-NduYI363OGDnRL87K4N-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1Fd_y7wL9klW2gkRHI06uLChAcu8ydxul4p5FIFhBwqafaAhIrHTwcI24Ds5kJ23Vu_TFMaw077dpjbSevjMzAmo494mrRncEAzR8mOA1TVojCXgT350B3Uf3_tZVb5fF6m_p_ko8V6zFUPMdsOP4niK4JtUIxzEEYqcb_mUBAjLnHk2oisyE_6mejGivN0hMHFvIuDXm8WdZKYgY-CJgGPjqnoptsIVevET_jVL8L6s9noPM6wPJatmwg9EufnnKOLzvVkh0HU38XkfvGtyZ57LiL0_exjrjD5z99Z661AISqCzx4BOlYv-yDwc5Pk_Q1-Ih-LbcOOdUhlBHxgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vvt4kmOTP7H_LwRpC9t749i71zM32KMR8ja7POwNMpQZyVPfxUWQUSOvs7SNn0z6kLhaYLkwdhFANIU2an2KV5JdPkezjdnszobeN9LJJMS3G7R_KAJxGMbIqU-T6-kbgx5VtuJsrhvZKIWWDqDBvAHRazLrWEcGF_ckGSrbb-99lz0zfU46i96vYiaPqNI6Ss7ciQIVWYbW7t08M0AzjEFl4UE0sF0QMdzq_ear5_I9OJTLrXOOPoVKIWRsX5lOke-9LnKaFI3it1aaFV52MRsbj1B-iRPMwMrd5NqcP1tDRGDd2_FDxa2lFAUZQXm3TneNw-zLj68v2kkiHVnuog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXRDvxS9ax7F7YbiG0kV_Emotqt_rEvuXxBEI8yhIrt1bTCnY36ESeR7FnPCkVETciSM2EgFQZGpQxjEryjJhmVt1-Wfaah2IZgJFsQ3WfkBb1aw5Fy25PtSWdPEjHqbTGJvl1QgeuTau758K2cRQD8lOdGeHfWedPF_FKYaWk4P-kUr1Rp1_L5FSf1Tfyt_lm_s7Ff0AzbVlIxfId0mMgnhF9W-QQlzfi1jq8h3eePb7jm5FvqtXh83ERg9i27Bvv2yh3eZ7EBTxhTN-v_KAaoGYhbf22oFtGO8dTMm0YQ24iGgL6FAKOE-bTAFdsrjt8SPtEQqKGQ_yNmPvqo-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=HQniTDU2epjYQX8tvbdW2vM9tqdvUvP2hNe_k9mRZurZ_eLqDHVj9Ofi66AAE455ikn2LPhg-ZLJH85Q7G4UwOnptTohe4c-0ju09MRbbyizn4aHwVyvL_R6u1cLGsr2akjJShjCsISQo0oSd9gwzWQmPzaA4xmlBVIm2ybWSKybOXT68I_P6l-4Sk-yTIS5vJsnTelcnGs6AuqUC7R9_hZTD2sDHzmG6Swn2OYJqwB5ZvC637YNre3QCFcXpwGNzO9T7_HvcflRKUb4gW5jnyk2fjlGqmSNfkOZDcHeM4Upa0WzT9-AZSDMM25ygYyMSE_LXFhoX6vbNfg2Q2Lqzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=HQniTDU2epjYQX8tvbdW2vM9tqdvUvP2hNe_k9mRZurZ_eLqDHVj9Ofi66AAE455ikn2LPhg-ZLJH85Q7G4UwOnptTohe4c-0ju09MRbbyizn4aHwVyvL_R6u1cLGsr2akjJShjCsISQo0oSd9gwzWQmPzaA4xmlBVIm2ybWSKybOXT68I_P6l-4Sk-yTIS5vJsnTelcnGs6AuqUC7R9_hZTD2sDHzmG6Swn2OYJqwB5ZvC637YNre3QCFcXpwGNzO9T7_HvcflRKUb4gW5jnyk2fjlGqmSNfkOZDcHeM4Upa0WzT9-AZSDMM25ygYyMSE_LXFhoX6vbNfg2Q2Lqzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsJFWV1JK4N4O2-_yt6o_-xKr0cNGD8GcpDHxaRqL0-ttx5cxgHhQRuqrTNAWyJlOeksQXiD0cMxE8bMvzNFkQ_lR9N_wLU7CjWOxs8xTGh3WtyFYWUy1yA2GZ3fp5tJ3-eh5PGUYFpicAL6SKd-MQkMV90DmQ6It9aBgLpq2LEADauOifmm2mOrGSk9poxTYyeUeo1dbWBI-XEe1udN0K-kUttxXoVszDtHogvh-I-KswJOKg7uyF46eO54AZa85txjI40yoKVzszc5WmIH0PLfOI6MzUHyqaBRaeRj6f8jYtRH8CCK7MthiWqDuHRoBK3494gBSO77QRCf5NwbIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVFXXSgIS2eXfQy2s3YSQq_TwHlRJjnnkIaHJgN-247RRYnbOCDoeJAne28pNLx-XmOrkga9oR2-wFGLAbwnV0YCmoj4On7AUp_tg_LNyOOSLwE8ZY7364K-LIbJja_zTLNR_Xho2IIaXX7sZHP16aKV3kteoFC3pHTBZvW6betn_JIjLXyLosQThDQteoVCdBqUYHqL9YIxeueCq5c5zJLALO7MaEKpbK1fRpRh7Vns27aSy59GLOYxKCKGadGLWt9AvOEmCBsPON_nQjp6wY7Pmo7adLQHEPL-1CiOZ_ERvu08qhCsJqTGOo5CpOScYog5RbaFcsbBx_fcJQOrlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OxQNoYjB60XUxToS__y8Szzg7AR-_mmIbfeKtgkvF3SXpvmZE21Zt5MZZvpsr-MZsH3hMSbYi2ewlnttq1pmeyE6RKdMc-otYBX4ReqH-EfayBR2sZDCBE8CeB20W-mJ0ZR_nI-kIlJH8M346o4IK6WNnl9UPInAIGT_y7aK-UPmufbpC2HjzaBEwHSwmP7r7IyQs-TxvpUEBMhQa0FstY-jg0YKM8Gw9Wew4nJvchyjtZngDKSqde6BCN_7TBgsV4mJJmKGZ0cAfdNIdRaQuoMCrtLj3CNOhv77o5Uk0OLRkmp7MJjoE_hyRSGg-NReKS2leGRVIbkFgpqGU6WEVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYODRJGDYuiPceoXHLao33c2NVH5-hjZzKfCGQyh9nslhL5LZORiLHIfxA4b0GhC-pijJ3EU0SQqQB1lkSBhtdpVM0aRl_KIIQCI1hoOeSXK3UsurfirFImJEx_dYVVAM6JsR10ZfmFrKwm_nBRgZXmbrsb1op41REL_jJPg71Jtgfc-_IV90QqZmBqgC_a79CbU3_CHbtr1Tw-x-8zrA4kz7rKMcWAzINE7CFkPwLVpapojVwkmrTec0FOMI6FQ7mwbeFgUSESC9dzzfVxgfTLYskzGDm50lGA30nGTprzDtaxWvlos_sEz27zX6HbKYdbooVjILEdsde0HJe1nzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=bhOKS-R2x8qKvTmR7LWP0kUzPnau5ve2BU6iXT5eN_Q5Wr8UbXvFSg_55Rsqgcmzx7xOceJ4AtDwunNnVY8A6dv4aJ5u1VnGEk7zjHK0v_wDIJuOf0cBJkF4q8KBA9WN7YMxJN7FxotpVi-6ViJiA0Q52mp3VI02ppq_VIe4DpwoGLSDa6XORMEzshTnoEjAqfz-daTK6W-SZNqVI4sze6p_1pafi_oiyr_pZxs31m1Vnr56dQU_1wgiI2l4Cml5o44i01kzRp1F-ArWcX-SpqskQTcJubICurz96_L6I4ArPKO7qWDL9nmybHhVLwpa753Zz7lmmOwpmLWsTa3Dog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=bhOKS-R2x8qKvTmR7LWP0kUzPnau5ve2BU6iXT5eN_Q5Wr8UbXvFSg_55Rsqgcmzx7xOceJ4AtDwunNnVY8A6dv4aJ5u1VnGEk7zjHK0v_wDIJuOf0cBJkF4q8KBA9WN7YMxJN7FxotpVi-6ViJiA0Q52mp3VI02ppq_VIe4DpwoGLSDa6XORMEzshTnoEjAqfz-daTK6W-SZNqVI4sze6p_1pafi_oiyr_pZxs31m1Vnr56dQU_1wgiI2l4Cml5o44i01kzRp1F-ArWcX-SpqskQTcJubICurz96_L6I4ArPKO7qWDL9nmybHhVLwpa753Zz7lmmOwpmLWsTa3Dog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFSeE6I9TjxFTWfq1_2oIZczUQr2y19ET6Ij4sKjjNL7-oh80yvLJAb4liFLvBPpw3c5Fbv4uUWnSF7vq-e-dUanthn6Hjn2EFwZ3iPHzo-aA--ze0zd_im36rgRyO26udbmZiueEC5ULcAef-qRrCB_CjbeT-LwTJw-CCdUMreCc_9Ewo6-bpqkqdoIbzN0tFMg46f8E04OGPScLKX62T5rzFGMhux0OFyoq00ggJWm452qtE3b8lxqF4Vp2Tb3WEbtkOBSzer7SVSIgp6fChWrQ1ZNDUCvyYwYJoPgP8v0di8AQqV196Jg9VRhppXMu09OzTiJsgIQMF8d1lEduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=rBz5KsVfo07LVFQF_hKGllkPmXoQ2qZJGHMb3XPs7kvMZW1zwyCz3EU_CHoI1h64-44VLKgcQx1i2kYYiV4Xbk3c3TtHxLCTAGfpeOHuugmEhsJzeK-knTR8CHVCI0bwAm_npvFtpdR76JSzhQ5V_m2Lc-lD1b5NL9rACiXMvT_xdAM1oUFI-ErYnJhalEx_ESMpVqdobTO9Hfxky5mSDIql9oUng3PJAQgpS_GJcz80ojS8FDHOiQ7uZYysaEUpsqamlMkhqun1EtTVjfVpntTRewPu5q8IjdZzfHEbPcwn-aAhGW_Ei93hOpFR4dt-DFvrMw-nOQp6b9DCv_HWeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=rBz5KsVfo07LVFQF_hKGllkPmXoQ2qZJGHMb3XPs7kvMZW1zwyCz3EU_CHoI1h64-44VLKgcQx1i2kYYiV4Xbk3c3TtHxLCTAGfpeOHuugmEhsJzeK-knTR8CHVCI0bwAm_npvFtpdR76JSzhQ5V_m2Lc-lD1b5NL9rACiXMvT_xdAM1oUFI-ErYnJhalEx_ESMpVqdobTO9Hfxky5mSDIql9oUng3PJAQgpS_GJcz80ojS8FDHOiQ7uZYysaEUpsqamlMkhqun1EtTVjfVpntTRewPu5q8IjdZzfHEbPcwn-aAhGW_Ei93hOpFR4dt-DFvrMw-nOQp6b9DCv_HWeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwkfS68JP3scFf3XfcnBD8eZJa-bipIf2WQXZ3hgRHtPFWc8yNEVb1dFXVd7sRoHDOIZcwDpSeSgpgg-irz2lKKXvnSdkZRHN4MKKuoh46rGC_V2wNzGCo8OKtz3b_CoNAROA3mLiVt79QTYAPXZeZunTXLQSR0Cg23eYiyYh85loEsPV7d3QVVgI5D-oUHj0UzoLWJrbElCNAdPGVSHUtBCBG6gkouPAZidVtKTTtKnPUEXcXf5wF0J_pfiIdir-pWr6Vf-hrq5Eqt1zCrhxNmuEkcj10_NTycs-1tfMhPnA1E9qXxIezb9iGk6G1LmeY26OFWr6DbYT1uYZFyt0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=cavPkSvFZKznmvn4k-JMunOaSV84eFTb6vWRLL01y6zEWwfmDF6e7_yQEBqyR6sPdCeArldAnXY0FO1BMHj6zJ_gR5xuB-uaZqy4x_WQ39G1cwSr70dW1sdKMSV4G4HZFiJ4OtBqOv_HSOg0mCvwEurm-H0P1Rp8DRy1zW2X003hdI16qNHmKft8OT47YYCm9TTOwmIo7fZt9XCZSVXFu46d-2t2a_2H7Na9gYqQatS7pQg1pMNvr7hkmT4xm9PKRu_62zKyaXt3oAg0M82M5Z-CMfGgq-Ag_L7fD_n4lirC5PNhA05UiqyJgODSMqLg1lMAFkS8u6iPz3FYJawSrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=cavPkSvFZKznmvn4k-JMunOaSV84eFTb6vWRLL01y6zEWwfmDF6e7_yQEBqyR6sPdCeArldAnXY0FO1BMHj6zJ_gR5xuB-uaZqy4x_WQ39G1cwSr70dW1sdKMSV4G4HZFiJ4OtBqOv_HSOg0mCvwEurm-H0P1Rp8DRy1zW2X003hdI16qNHmKft8OT47YYCm9TTOwmIo7fZt9XCZSVXFu46d-2t2a_2H7Na9gYqQatS7pQg1pMNvr7hkmT4xm9PKRu_62zKyaXt3oAg0M82M5Z-CMfGgq-Ag_L7fD_n4lirC5PNhA05UiqyJgODSMqLg1lMAFkS8u6iPz3FYJawSrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=YgZMXXglo7PRlaN8lV_kmp1ggl508Ed2IDNn76uhQELhOt23ZBAUwmEccDHB0cpX_KCUVK9DMgAvnPlldEdg6c3b6RedyM8U0fOn9sHcj-QF13mVlm6pcJeX89yEaSsS4QK8M_ZNOzjOyVyitbutUEZn_GTiOJizbMe8GkaZoNNtJ-aPtNcMgXfP0JaMvB-WoHUpkOfphp9wW4e67nCjpfGmBV1qPw8tXZr1A9mDlwxcJVIRkk4w6cn0tYQpLjWZgzkXXJkfSocThkvwawT0wgJdlJOubQJ_79SyFJWPHiYrkcKYvZQAcqAcbUknXTid6-lF3Sa1KgxHD9PFrSIT-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=YgZMXXglo7PRlaN8lV_kmp1ggl508Ed2IDNn76uhQELhOt23ZBAUwmEccDHB0cpX_KCUVK9DMgAvnPlldEdg6c3b6RedyM8U0fOn9sHcj-QF13mVlm6pcJeX89yEaSsS4QK8M_ZNOzjOyVyitbutUEZn_GTiOJizbMe8GkaZoNNtJ-aPtNcMgXfP0JaMvB-WoHUpkOfphp9wW4e67nCjpfGmBV1qPw8tXZr1A9mDlwxcJVIRkk4w6cn0tYQpLjWZgzkXXJkfSocThkvwawT0wgJdlJOubQJ_79SyFJWPHiYrkcKYvZQAcqAcbUknXTid6-lF3Sa1KgxHD9PFrSIT-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=lm6rg3SCQJHoaw3KkaSQtKpromBjyB8knEOxFmW8RzVUEgTAHpbNdiZOvKhWadONv63LAbI6DCjJwVZn36oPsF6hbhBt5x0iubnHeOUToXDJRolI3R7OF23EzMyEAg9f5d82TEF21pBqFBU7sd3irLwOFJHuv0e3A04g8-o0L_aKcm6-yyuQn7I4yI-ymAlZywPjAAg0ppGx_NGG5ghPysqDNKSoqmf6VS015Zt9xQHgNwVz0fGxPc_rtaRCiG860NbzXI1I1DsTXEH4MSygR40-9EtFVMmfxzOPn5KppPL4jI4LthZBbpD7HK3cqAbOGh1jkrLCkSNVyRTa1TJ02A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=lm6rg3SCQJHoaw3KkaSQtKpromBjyB8knEOxFmW8RzVUEgTAHpbNdiZOvKhWadONv63LAbI6DCjJwVZn36oPsF6hbhBt5x0iubnHeOUToXDJRolI3R7OF23EzMyEAg9f5d82TEF21pBqFBU7sd3irLwOFJHuv0e3A04g8-o0L_aKcm6-yyuQn7I4yI-ymAlZywPjAAg0ppGx_NGG5ghPysqDNKSoqmf6VS015Zt9xQHgNwVz0fGxPc_rtaRCiG860NbzXI1I1DsTXEH4MSygR40-9EtFVMmfxzOPn5KppPL4jI4LthZBbpD7HK3cqAbOGh1jkrLCkSNVyRTa1TJ02A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tPrrGNgyWDwEHspMsptctFNAdJKikam4GQA2VU-jgIdctDi8O17UVG8yG_TBi88Rj2rKATodqzdEFG5dDnBHJMkg3Vr_Gj4ZW0fXH4nNDq36wt_6_n9Unoq_MaEVaGVQPrq549tc1GxiKzj5axawno6mbQvL85vcXbrzNa3CHEc7oM37gb45YsWQBotES12ede1KOdJfwSIuxipSrZvGEDuOOHyqCRvvUT6BWQ0pZ_4x49AnqzOzDh7gqHnlPDQH-fT7WxorVJeLxGZSyipVvxp9RDBOrGZUOI_AdOEXgz9XSYs0GlBWI_i-SR--gjWBtzTiRV3xbgG81rDrxqya-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ks8_5EGWwdA4Vmzp6QtWQxaBrWcl0lgfW76MnRswbRwiO0KQymcOsEvkoOgV_N372vp_pcma9GwLJCM4y-_8JcS8f02KthBZzqmQymf0nKnTgGLXBqHK5uDe0vLKIHjYOftT1oLOfuGxYZaosi8hLyOnynNqysZ8j_V-ziOEc_q-KKL_IjRfmjCbnABgUauBDsWf29aVY9b0eXTw3SWlTS8T2gHF5MdfTjpv-5LvRehrumXxgoW0SBzLs3oC3NdS6bCs94Xd77dTFBDPHFe_bnY558kDx_IhKIbUogqihaeCp3ANd8IiwBXKWHXX-zfUdGgLH-7Bre_jsIziTbJqxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=URE7tBftCtmyM3R0CL630YABOuoe6UNxyOHja80-2mXMEdwL91RTmUCITu8fj8oTqR7Ztj4yLP7zXvuCTdvrckYnCIFKK-lsfPvn8HPoP9-mww5_hMc4a5k_KuSN2UsT6nQEtLAVdGunCFlMGxbDy8a6mQXXKwNVnI6bwQgmM0rzABay5m5bJj7FW7r0ZwKeaY3EPowKWQIvVR-R5gDIscQu-2pteA6Tr-pTwknIXWD9MCK-dAiF-D76UnB8qi_KLdc3W7jGVS5g5vUopv-rZvvFR26GE1Eac9ORdEcR3XSgHL8dESJ8taEWlPSmJhG_aPRURLavYPyNSvtJMypKjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=URE7tBftCtmyM3R0CL630YABOuoe6UNxyOHja80-2mXMEdwL91RTmUCITu8fj8oTqR7Ztj4yLP7zXvuCTdvrckYnCIFKK-lsfPvn8HPoP9-mww5_hMc4a5k_KuSN2UsT6nQEtLAVdGunCFlMGxbDy8a6mQXXKwNVnI6bwQgmM0rzABay5m5bJj7FW7r0ZwKeaY3EPowKWQIvVR-R5gDIscQu-2pteA6Tr-pTwknIXWD9MCK-dAiF-D76UnB8qi_KLdc3W7jGVS5g5vUopv-rZvvFR26GE1Eac9ORdEcR3XSgHL8dESJ8taEWlPSmJhG_aPRURLavYPyNSvtJMypKjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=s_2QLs8inle57zFChANB45JoEmK34AwJT5mDuIC1DR7Cwkrad7qp9nISyf9j9g0tWN3F7zPtDGKMNIgUQ90ZKPKUFmup8Vn2Rj_h_nyetqXfR6u8kHaYiNL0xAStz99O_awBt96JmCCdivq9h_kK59RfYW0SXDj2xLuGkd5OCj7zgaFQ4jQ_9qF2nzAzcHf6qQ_NnEQLXNKxhWfPQW5f_lvsIx19XqxboBFda36dP4TUXjDTxlFBX86iinUbs8QAseiBdt-JMwV1shT8vTU1_BD6oi47ooOIcLpuJDg-y6sZQDBTrtLHLaO0k4gTAo4blVug8HDRgJqw4H4L_1tIRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=s_2QLs8inle57zFChANB45JoEmK34AwJT5mDuIC1DR7Cwkrad7qp9nISyf9j9g0tWN3F7zPtDGKMNIgUQ90ZKPKUFmup8Vn2Rj_h_nyetqXfR6u8kHaYiNL0xAStz99O_awBt96JmCCdivq9h_kK59RfYW0SXDj2xLuGkd5OCj7zgaFQ4jQ_9qF2nzAzcHf6qQ_NnEQLXNKxhWfPQW5f_lvsIx19XqxboBFda36dP4TUXjDTxlFBX86iinUbs8QAseiBdt-JMwV1shT8vTU1_BD6oi47ooOIcLpuJDg-y6sZQDBTrtLHLaO0k4gTAo4blVug8HDRgJqw4H4L_1tIRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiOrhEQmpaSsTXbh9IW9iIxpWimuKYa-b4tTqxHNsVwgboDZMjVphPMCFieHyCmck4wEyeJQvXgYRHwL7HM_ZwxatQBOsoln-f1X4tCks_PwqNua_Fbt-wvhm4IuSnWjSYu2yymsqompdFJTTXcxMAGZRK3M6D8m9MbzZBTG-3p1XeR3fcv18Wd1wHdE2xu5upstfh4aa1ooEgpvVLjvA9JhFkpemzSspEUsEFX2Jm7h-eaXu4eGmkaXERsb9-qYXIoeAO3WONJmQ4whH7qFoZw44CwFjUdZViKT1qGHCdNyxAuQAZBePkzl8urcZNcAqWr1isN0-BMMDnPvBMq-jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEpR0PbMSmsy0PDKL62FKYQli2_LIDzhcUYkMD7Fn2HZIyVKHWKfc9MiaQpGcMg-9fq60K4y2WQj7-I_AwaeMNUufTwNZI_itwGIY5Z6UDGkUwak-UPBW5sLwDEryXLtwq9ij0T7Mlnk-j55VApNkECDBl4H_-Qqsntnb36ijrSNbSmyS6JL01lHlr-ei8wFZHDKAI1IGribj7aYd2KAFZepyxWeMBkJiAAQXNzVfovD9lMBX_v0PdAKVUs2vtRFqInzm6G4HlGTKTMG-PLMhpfPUScimSBbOjywH-ttLWY1FH_bXpMA7tLXYTMPuTARuCOzc6D9huAeeS2ads3A2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dZfkA-_F4hxgMzEbqlMMdLZNtVXimiKFBYkHPVnMWdVUrzqGBlmxH8XHk8hVbtWTNjn0G2-rbC7cMvSRS5dXAPF8y55jckIqA1yuoKYz48ua7tpl7XLQ4ViVZG2wlpLxn4eCinZofAQOGK06ev1pzmUCRwGey0iure9ZsNL8h9wLceh9Zkmcnnrgzmn21UjSkpqQrlw7imT7API47mYNJrSsHAreFWvGMQLVp95bywcfbMFDj8nD3XwtFvBF4KpW6CW5R6rj6CV0f-FF_jVjfqfgKPacj5sq1UZlXzOxlVzufy0Zy_YUXei80T4ezsK1Lmzn4W89j0JTga2QWpBzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4YFWTr3F47z46dEr4gKqmSLu2UwlxnJS5-lVc6UdzuQryR2Lu2f17yLNoJEqWfdKgmLZMSL2d_I5NejAkN-Siy1VAfBoJbUGxP1BTCiq0RK65FUSuIueTxWVBuU0zcdFsIdzD9W6g5KbW1g9gy-ToXRpBdfNxGZE0fcHbZtlnM7k2OKoJbqN558K28NRGZzfrVTBLzoSI3Jpak0SEsA1hq3hNCiKnrpQYyO7TDWCNiUbgtzUhFAikwEP_KVlWQWWXG5sd1DunFzVDmHBXqghHGR6Y2_99IgNFjg33ug4fV6zvVbyFomUDU9-Kb42NqncY9ySJhij9yNwHQ0hb8-CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oou7nUFWY4co1GZ7ZM4EZZQiMjA64qckUdUz26Fh5vlP9WnPbc17pPTGy5V3tyhrFWaCCyA_rO7JiF58VGM-VWaQuzk_Zzu_jxcpVEqfLNcU9s98MHin4-A38HtLOcclIwDUAGSaVXDqzKeRzPyjzkh9npLxFdaA1SOfrukG88i6zniKfgg7DFBXZtgUL1DBPvR-F7CRjewqI8-14WfxdIcwDOjf_xRUwnicTugJQqb_t3sJ5fCC-57ONiOMpVQMocCXizzd8BJIRJdrV1-OvOByOs8961tqtzjS9m_fS7YJs0tmBqhmjMN8hTasPR7_uA6zKpWPwhXaZOUtMWWocw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OEF2kt0Z96-3KQSKRTqGGDwZw_qToh7WuNkQ4gENcOolrd730ubp7O_k329y0mUDUQrvfCJNFC6omYB4plELAJgXOW5El60_dtN2yUDgVJei0SURAC9SHkXwbVSichxoQwCzwbO2jeqAQ0bLrtAw5jb2uQl9m4b_KvUcB_XjEE_5R13eVJNtRTJHiaJJOVWQUbYiw8yu9T0PX7N-ZQqON2l3oOMzbcyBnnuqn4Y5qGyulI3IOCK-vt7549eoxTSXHtK2EfEG_-MS5Ki0cPX4Crk2BnPhTWpsE-zYtdFtxGUdjKdhtHDgbZ5__-xrvTOWiGMh1fusR9sKGEB5pLdXEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
