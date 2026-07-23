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
<img src="https://cdn4.telesco.pe/file/AKt9Hvo8xGK6wy-8PY0z4DYAr7AuOietYKPee0Aq3adwUfx2SvnK_Ga9pn94wE2I-iNvAXWnKNIcWXrTiwHUafeRSbt8e11Xtf7AMOdULoKGLXMmu7IPTHyBwCkNvYDHB8T0ttuUGxOrGvCxHR9B_Uptim6a_DUSvZjz9sL0VDm5QbznyvdXpFc2MLslpamI2t1X6BzZiVS1t9FJuuJBZ3DrGGggDQziwf4uyLosCLZefObMC7x1NA2dtFUM6r8BJ6ishbBX1mFw0mHDA0wwU-5Ziy3Stvh-y1D0_DrwsCjRm_yvfq633S_dF91Utyd4gBUck2fqxZn4I-v8LiWB3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 152K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 18:09:18</div>
<hr>

<div class="tg-post" id="msg-68859">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🇮🇷
هشدار سپاه پاسداران به انگلیس: بیش از این پروندهٔ خود را سنگین نکنید!
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی‌های مردم منطقهٔ ما بوده و سوابق سیاه تجزیهٔ کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت‌های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات آمریکا و رژیم صهیونیستی علیه ایران داشته، هشدار می‌دهیم که بیش از این پروندهٔ خود را سنگین نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/news_hut/68859" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68858">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bypk7hnfNVoiiayhM41YftAGVriNZM_8ak8By9iPavRDC5MD59ZWwwl0bOT3Ub8ht15PvbjQlj1Xn7T2slchbfwhZctV8iPBfealMIJ-h4BGo5YtlqucjxjmWMDHIclBZXbYjXhhBoE10FnVDWGXOQK3U76al2kNGyImB99bywQsoEbCMAccNKJu8iLz4UiOE09oBiCWVW-WuQgNKWOimFI9id94UInjOVYgF9vos8AL0LlS3YXrmr1YqhiJ1eud4ZjvatBKGw4kjjCFH5OtI5A8onhFeGXoxWhBvgfSy2oOsnaD4gUfBglY-FhV_0PsYamFb4ESkaDaP9gMhZZk7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
نفت برنت بعد از تقريبا دو ماه، مجددا 100$ رو رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/news_hut/68858" target="_blank">📅 17:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68857">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTCU1Ypy9gfBDKNr9WwRr0-zmwMzou74ReYwelKDfQwZsjlSPtmPjfKq5M45hAkhyE0I9qj04t9YqnDh5uTKBVlsC3KxvOEoUQdFDoqFIF9wwZXZWbEwPGi4a-3mghhOmF4aqWXSrYXBY9yv9_KR46Cdfkclfso98icy9dVveS0ageTe3qw9jsajkW__oinfBFtPp02dsTbkcdlWl1BgF1cfw4rYk45kIzdBlvwknHEk5iK7d6Hh0GnyibmHmhqOTv-yi3uQdIQhQ_vAAD4yutJEtrMXLi_UKIQpqftyBvrulpLdhFdjEGXepbjMmw579X81H9NNzrmna7DimikQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس:آمریکا هم‌زمان با تشدید حملات علیه ایران، بمب‌افکن B-1 را مستقر می‌کند.
مقامات آمریکایی اعلام کردند که ارتش ایالات متحده روز سه‌شنبه از یک بمب‌افکن دوربرد «بی-۱» برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران استفاده کرد.این نخستین باری بود که ایالات متحده از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش، مأموریتی با استفاده از بمب‌افکن «بی-۱» (B-1) انجام می‌داد.
استفاده از بمب‌افکن‌های «بی-۱» — که قادر به حمل ۲۴ بمب ۲۰۰۰ پوندی یا ده‌ها موشک کروز هستند — نشان‌دهنده تشدید و گسترش قابل‌توجه عملیات نظامی ایالات متحده بود.
هواپیمای «بی-۱» (B-1) می‌تواند در ارتفاع پایین با سرعتی فراتر از سرعت صوت پرواز کند و در عین حال، سنگین‌ترین محموله بمب را در میان انواع هواپیماهای بمب‌افکن حمل نماید.
در بحبوحه تداوم تقویت قوای نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان بازگشت به عملیات‌های رزمی گسترده علیه ایران را مد نظر دارد. مقامات آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/news_hut/68857" target="_blank">📅 17:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68856">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=HJPex4XPbqnJGMftFuYa6OfsO_abN2mHD8CZi7f-ar-h-V_xgO47Pb2q_BA44UR-efdfct5p89vxem9ZM0nXTlP4baXZPKKdEMo0U4EVRfviiYBWUUDE6pl2p74UAuxB6U3DYQoyhVpRcT3V7TE-isa6cTT89RKSiDV-jHuVYuyPYyyPF2AKPWiT9GOEpMu92zlKdMa4KgXK7-TY1V-oO0O5Tqn0xJ-pgF0BTNIMaR5Z4UGyisVtMvmPk-VxzvisbRVEqJYbcGEIKxWADOyOIghuqajViHak8IvaYjkImZMlG1BHNcCuHpC17Zvrg44yV0v3APXCt37fkZqQjrnR7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=HJPex4XPbqnJGMftFuYa6OfsO_abN2mHD8CZi7f-ar-h-V_xgO47Pb2q_BA44UR-efdfct5p89vxem9ZM0nXTlP4baXZPKKdEMo0U4EVRfviiYBWUUDE6pl2p74UAuxB6U3DYQoyhVpRcT3V7TE-isa6cTT89RKSiDV-jHuVYuyPYyyPF2AKPWiT9GOEpMu92zlKdMa4KgXK7-TY1V-oO0O5Tqn0xJ-pgF0BTNIMaR5Z4UGyisVtMvmPk-VxzvisbRVEqJYbcGEIKxWADOyOIghuqajViHak8IvaYjkImZMlG1BHNcCuHpC17Zvrg44yV0v3APXCt37fkZqQjrnR7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاره کردن امضای ترامپ هنگام شلیک پهپاد به سمت پایگاه های امریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/68856" target="_blank">📅 16:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68855">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:  یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد. از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه،…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/68855" target="_blank">📅 16:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68854">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjjP61JdTVCdNw1PgDMAv7-bevs9mmfasvlwjaJxUjnehxQ67O-iQPhaiE8d8WtxiOzhghnvkE7lSXeNOKJ1xgzIb_jgtm14kfG8TsEn_cFboJVYxW6tGwCwzgfmBA1Dqb04dZVhj3E-0XLFYeRdjAdNiObzpac9SZwN4H1s-7KYOqIqiQiiKW_S84mJ7kHw_tY-QReUmCSg7G9_ccyy7s6W6zu5bcGU6NGYulnMutOo61pI7iH6o0JYA5g0nDC0ZG_q0IaCXJHIivGqEKg1CVpHxqrYhI4oM8cRjND6MV9ZfsMhIeD6MhUQg6g0mwtHG6JMgvEQFAKOnJJO4_rSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛فرانسه در حال تخلیه کردن کارکنان سفارت خود در تهران است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/68854" target="_blank">📅 16:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68853">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J97-xMYL7b5M9xmXHkv28t8eAZfEXCLOGHL8yu4Vxg4RXElx-mGnHcHt0ZfsgP3vrx0ds9oCh1glkfDDGPY-i1Pl6Vbomt4VLqOwzJ3AXCsqwDXYmg4IMgRPqbrFrL5h1CO3_d369nOoszxIh9y-TrewScJQ_aXVdaGOMgBn6G65IDUVvME4hmcLwi1gqko_SgPwa0z_YmrNsUZU7etdwj2tge5IQw3HrI55G48dsQnYeagUXNmt3GulCmqmTHPYRZpjgE5JWeuKGEy0cFWVgW-TNxAM22nTm9cOjcZsHqDICXK4Z3XZQKcFZzIzCRZdrHbrFe1m05UkhMOcQWHXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد.
از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه، اکنون آن‌ها دوباره فعالیت‌های خود را از سر گرفته و دیشب به دو کشتی عربستان سعودی شلیک کرده‌اند.
لطفاً این واقعیت را مد نظر داشته باشید که اگر آن‌ها دوباره دست به چنین کاری بزنند، ایالات متحده ایران را مسئول خواهد دانست؛ چرا که حوثی‌ها نیروی نیابتی ایران محسوب می‌شوند.
در آن صورت، تنبیه نظامی سنگینی علیه ایران و البته خودِ حوثی‌ها اعمال خواهد شد؛ گروهی که عملکردشان تا پیش از این بسیار حرفه‌ای و هوشمندانه بود و اکنون موجب ناامیدی شدید من شده‌اند.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/68853" target="_blank">📅 15:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68852">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n08hvWNXbQH5YYz8XqV0iaLbryDnWUYm9ir1-OyrGUSUMevIWHd8o86fSiHOAAGNisaSsQ1bfxZxNqkiRIcvPbdw5N2Pw-3Yr8N-XmnVg62n7YBvNxzRkHE3Ql-errUwuSZdebZWuYNkz03hRL7O6Njfmkwdu1jITs8uvecoFIg8rQ2veSWqnVlJR8spnuHedcnHIvhXmC0x64H50jaCvN9jLwXSPq-VpM05fZLTWrxsc6MZt3WzXyHg97GRlGsaIqNZakj-s5wF5bCKGfTw0-yVtZyTGq-atRzn4P-1r4WbamfVPGht_vDRrbK7zoj5YSNO3PXDXl3R5AAqseHofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توافق هسته‌ای غیرنظامی (که شامل هیچ‌گونه غنی‌سازی مواد نخواهد بود!) میان وزارت انرژی ایالات متحده و عربستان سعودی — که صرفاً به مصارف غیرنظامی، مشابه آنچه ایران و امارات (و دیگران) در اختیار دارند، مربوط می‌شود — تصویب خواهد شد؛
اما این امر کاملاً مشروط به پیوستن عربستان سعودی به «پیمان‌های ابراهیم» است که بسیار محترم و موفق هستند.
ایالات متحده با تأسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) مخالف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68852" target="_blank">📅 15:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68851">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=PsqgkhKq0Opxnc_VRTrIb4U_H6uOXKt5icyj2XBCx-fcQ2PzUAIc0pT_YK2VfWAIV4EILY0G25I9yo5B7Pd1EKO1Kan15tKvBvNy44GJD7XBIAAdYlTGmk61bBg1lQQeK83FVnD3eE-iHm7hMMdnyOkj5fLYORrY2srQejfM_OeAn8UUvwGZC1CImOU59ua46rznuK0Ih46QkSRE5lQHKB-DDzAg0pIjpfzxLpik9oU1tqqAReBiZxMaL5LMf3zwX8Ql3UvJuPq3ddmIQrKZw6IZ9kejZTVNHcC_m-dc4DTOQks2-RXBrCq5Dr3AIDA4BSk1Cr83--Fk85NUv8TaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=PsqgkhKq0Opxnc_VRTrIb4U_H6uOXKt5icyj2XBCx-fcQ2PzUAIc0pT_YK2VfWAIV4EILY0G25I9yo5B7Pd1EKO1Kan15tKvBvNy44GJD7XBIAAdYlTGmk61bBg1lQQeK83FVnD3eE-iHm7hMMdnyOkj5fLYORrY2srQejfM_OeAn8UUvwGZC1CImOU59ua46rznuK0Ih46QkSRE5lQHKB-DDzAg0pIjpfzxLpik9oU1tqqAReBiZxMaL5LMf3zwX8Ql3UvJuPq3ddmIQrKZw6IZ9kejZTVNHcC_m-dc4DTOQks2-RXBrCq5Dr3AIDA4BSk1Cr83--Fk85NUv8TaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو فروند هواپیمای «EA-37B Compass Call» صبح امروز وارد پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) شدند.
این هواپیماها که بر پایه بدنه «گلف‌استریم G550» ساخته شده‌اند، جدیدترین هواپیماهای جنگ الکترونیک نیروی هوایی ایالات متحده محسوب می‌شوند و مأموریت اصلی آن‌ها مختل کردن شبکه‌ها، رادارها و سامانه‌های فرماندهی و کنترل دشمن است.
در حال حاضر تنها
پنج فروند
از این هواپیماها در خدمت عملیاتی قرار دارند و قیمت هر یک از آن‌ها بیش از ۳۰۰ میلیون دلار است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/68851" target="_blank">📅 15:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68849">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlJZWBiESMbE_vFnWeXPCkymoNJgXHUvaLC-fJP_KPKztuzskIgaDCna3qBars49gShT0tV5NKewT3RTJvJqkDGdAhFnNLfqjqjCpjVbxSinAkfaFxq_xkmDbxQao1cHYYFnIJ5rHd12yZsjiEaCxz58qgS-WcD-S-OWLh4TLjDY7E68s0MUrO2c1cjotrNQ5-jXoBQzZ7zFgO1T8xeR-rL_LbrGkrG6Z7Vonq6mw7fSWVEo9bn1EEVCvfvzYaFFw-vUJ96SDiaj_McbHMcWi7kvayKP4jm865ITse4YWCPgjkf56indwhYOQXNnj4Bty48_-Er_O-aUZCyl7t03WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=HZlWrPiePeA1o5hmlCakb-fif45Yz50l8xzO81VMv5p0MuVePoMwwlwcQfXLzEl4NLNcVPeA3YP33DBhsRjtmWKwhRUCoV_wlizfnBhfiesS4_ufZAom9E2Bi_Eprq9k_FCFfyFmrJvvTGdnRu3vWDbem2Y2RbaA_jrYgXAsMclAgmsJYK3soa_GbvYdhJi0q03RdOUUkgaen5U5fMWaemfLsgkNstx8fyzUC7zg7QtOXlTLfY_NiRQpiAurFfGr7qV_DaBrsPezvfEueCsYtT8pvQPSfEz5wrWWMHyJU2yeea40IWxhlwC4i5W7qt0oLYvBgyj2q9GO5RZfzJkySVaN5sbB5f75WiHaJKgbnHIHEnA_ha54xd4GtPixCwhGB9olHzuH4wDYgZtLdhYP5h8UPrWp4KnbYxLZ9YXHSfg38CoZDdIJbHLUwKPOertt9MVRjVWu16lx1OwLVbzbwnmn4KMrjljR5ledlA8oOe_EiLE-oVuyRdxfiwrwU0wxKhuf07mgnPejv4m4RqQyCyNV2QAfKSu7VGO_3FCWbSoMTQNGHlWz2CgblYap-ctS0Sp1HckXrYKxw5z4DWk17jYGUz7c9Ou5Q4DZqU80bls_LJn7haiMjh86UCqJmwhF_-gwYsNwX-iuES4RCvOSJqG5hGEqvLo584bI3yyCwUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=HZlWrPiePeA1o5hmlCakb-fif45Yz50l8xzO81VMv5p0MuVePoMwwlwcQfXLzEl4NLNcVPeA3YP33DBhsRjtmWKwhRUCoV_wlizfnBhfiesS4_ufZAom9E2Bi_Eprq9k_FCFfyFmrJvvTGdnRu3vWDbem2Y2RbaA_jrYgXAsMclAgmsJYK3soa_GbvYdhJi0q03RdOUUkgaen5U5fMWaemfLsgkNstx8fyzUC7zg7QtOXlTLfY_NiRQpiAurFfGr7qV_DaBrsPezvfEueCsYtT8pvQPSfEz5wrWWMHyJU2yeea40IWxhlwC4i5W7qt0oLYvBgyj2q9GO5RZfzJkySVaN5sbB5f75WiHaJKgbnHIHEnA_ha54xd4GtPixCwhGB9olHzuH4wDYgZtLdhYP5h8UPrWp4KnbYxLZ9YXHSfg38CoZDdIJbHLUwKPOertt9MVRjVWu16lx1OwLVbzbwnmn4KMrjljR5ledlA8oOe_EiLE-oVuyRdxfiwrwU0wxKhuf07mgnPejv4m4RqQyCyNV2QAfKSu7VGO_3FCWbSoMTQNGHlWz2CgblYap-ctS0Sp1HckXrYKxw5z4DWk17jYGUz7c9Ou5Q4DZqU80bls_LJn7haiMjh86UCqJmwhF_-gwYsNwX-iuES4RCvOSJqG5hGEqvLo584bI3yyCwUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقوع انفجارها در گذرگاه مرزی «عبدلی» میان عراق و کویت، در سمتِ بصره (عراق)
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68849" target="_blank">📅 14:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68848">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUP5Bp8xcogTptLlrXlfoCYDkVAbYUFJxju5j1cp5gPUSD6URgNT4MmtBT4dl7h-TrL3bJvMIoIbhSnFzC73PNLLfIk9rxSsBCkchgZAF-CAFaa7EM9ikQ-Hjvf4N4QXCm3W_JgiphWNAPBXbMvzjCISi02RePrOK7gjzvVIlfcoCO95y1nAUFgcAJNMKcBg_uqcliCG2v7iKD0MfyXgfwW_vHKFKRZs73aj6y0u-DOR6Wjy1OhCQjwIomPDxzf8Lwsx_DIr_xMGwIaL2V3nHVOB2A-FYjeyI8Yzc3t3G4tugx1EXFpqs-N87dOMPAWaq0rCvggLuTdV5Sa4aEDqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابوالفضل ابوترابی، نماینده مجلس:
دولت مسعود پزشکیان با ارسال ۲۸ نامه به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، برای مذاکره اصرار کرده و او را «تهدید» کرده است.
قالیباف و پزشکیان در «تله مذاکره» افتادند و «باید به عقل هر کسی که الان حرف از مذاکره می‌زند، شک کرد.»
اگر جمهوری اسلامی «دو هفته دیگر جنگ را تحمل می‌کرد»، آمریکا و دونالد ترامپ، رییس‌جمهوری آمریکا، پیش از آغاز مذاکرات «همه خواسته‌های» جمهوری اسلامی را می‌پذیرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/68848" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68847">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=jVXC7mjqIfu0h8Au4swnQ55mWwRVtCZ5Bbgca7zmCt47gQzamjyYLWdF1QyNHlRKY-pzTv5KjwVvkgEaHELUgweYEoQwmsxfebLo4dVidQB7rpACYaOGqYPdZ_gGi2e_opPQKPV4K6BYht1rNxExqTfVOCmtMN8su6OGvtD-UXuPbK7g15btpQMosCuCddwxyYv9Dqpa8y2zXNlD62bH1fxXYfFjLxAT6OPX9azFWXc2qLo9Jbclzp6kfO5aeSMFIsmQEqjScDm4b71S2iQKCNXtdfpqJxF6Tytx1M_yYWtGpI0huqJqyYPKq5mFA9qj33XCi8GWaSygI6aWrn_scA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=jVXC7mjqIfu0h8Au4swnQ55mWwRVtCZ5Bbgca7zmCt47gQzamjyYLWdF1QyNHlRKY-pzTv5KjwVvkgEaHELUgweYEoQwmsxfebLo4dVidQB7rpACYaOGqYPdZ_gGi2e_opPQKPV4K6BYht1rNxExqTfVOCmtMN8su6OGvtD-UXuPbK7g15btpQMosCuCddwxyYv9Dqpa8y2zXNlD62bH1fxXYfFjLxAT6OPX9azFWXc2qLo9Jbclzp6kfO5aeSMFIsmQEqjScDm4b71S2iQKCNXtdfpqJxF6Tytx1M_yYWtGpI0huqJqyYPKq5mFA9qj33XCi8GWaSygI6aWrn_scA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه حمله آمریکا به حوالی بهبهان
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/68847" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68846">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc1jr4YIYsZI4REzId3J4WjZsQbpYewBA1q3I8FMvcGtsUic05GTnoTd-35R34IaC-yW2EBZYQGCDYOc6JVqrH7xaRngohTVXzLoxHmkjvLuliBBLwfVY0CaopdbGnsb3N1u_9kBjbKyqMVnESrdb9wVi8tc4mW_1BTRwZUE9ipuv-cGFSyq49yzPm_7z6P8jIA3qCwE0S-0NuwvDhqUYo0XiAaX6I8s8vyDg-ZTo44b4D2lVQoN5Z8U4toYPjMayg9b4CO_2Uygs9F3U8UZbs6WpsgZoWcq7i_nqzu9L1Tmgml1puGlwHsrSM8HYCJAX2PAOAI_dohDy1Yd4Is7Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/68846" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68845">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇱
شهردار «رامات گان» در اسرائیل:
«ما تصمیم گرفته‌ایم تمام پناهگاه‌های شهر را باز کنیم. ارزیابی وضعیت نشان می‌دهد که خطر حملات موشکی از سوی ایران در تعطیلات آخر هفته افزایش یافته و دیگر ناچیز نیست؛
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/68845" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68844">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=EIDnlQmKwk1xPO5sMStcXWKdiI2ieroIWEAL01veQD6JmEjnmtT1HzqQVqbiiCPy2gf_1KIA2ywQwPKFJa9pUlLUjkF-EnBLXiyPfnmYYF3_ZZe2da-4vRjzDCZY5naF9PMFoCC_uAbqG53sb56jQCV-n4X0zHtPlhE8zH1-ctlOHOij6ShKPDHdLB3E6mBalME5c5MNzt3ss0O9__WqXpDxcqt4SSjZQ5OWGJQn4iJz7j5RZk9L_e1ibz5Mk_wVCTkk74OBpa86_BaitEmHPIAp5yhxTaV91iK-e65HxcWUNHyhaCOyNQc2vtzHx5XokOjeZjF946uqUxBVA0fj3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=EIDnlQmKwk1xPO5sMStcXWKdiI2ieroIWEAL01veQD6JmEjnmtT1HzqQVqbiiCPy2gf_1KIA2ywQwPKFJa9pUlLUjkF-EnBLXiyPfnmYYF3_ZZe2da-4vRjzDCZY5naF9PMFoCC_uAbqG53sb56jQCV-n4X0zHtPlhE8zH1-ctlOHOij6ShKPDHdLB3E6mBalME5c5MNzt3ss0O9__WqXpDxcqt4SSjZQ5OWGJQn4iJz7j5RZk9L_e1ibz5Mk_wVCTkk74OBpa86_BaitEmHPIAp5yhxTaV91iK-e65HxcWUNHyhaCOyNQc2vtzHx5XokOjeZjF946uqUxBVA0fj3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
عراقچی می‌گوید سیاست آن‌ها "چشم در برابر چشم" است.
سیاست ترامپ "سر در برابر چشم" است.
آن‌ها بهای بسیار سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68844" target="_blank">📅 12:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68843">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzaQu3zoy15SukZGy8R50deJP7Jg7X6b2ZXL0NJNg4G12WRzdFrNch1cbzKKDTs7CTKtaE93cqtczEa39t6JzwsuM7oumJ7wJsdlzGq6U3A8bW6DZhTQdeyfOXfoggIJ6AKWPjofhvv1JfsmQ2i4umGQL8ny3uUzjxn_gdAp3xxvSN-95GndkwQbl3ZmZR3EVj0liyl2KTSLK3RF9_6-HpTpFRhzVHCjcLf4AreT9T6ZgG6J3279XHVudeZ0In5POMcqBvEwUELDW39Qk3i54T6lECYIquv8fE36cN8NVVmyY3a7AXZ-1-1rJry6GtOy_JSt02jq6W5wxVdnM9RCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پایگاه دریایی ارتش جاسک که صبح امروز مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68843" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68842">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=pj9Fh6QgpeaziedWtui6weQorZEYwvTfx49Gdu3WM7i_6o9Ks3eOPdEs0iS8m-ZlQjbAokWVDdrR8paaz-tq6_ku17Fs_4WEf2gq9fCmhmy226V-pHGqZ94jrEp6Q2XZJPPKbh82u2t13WBj3x2zqOWUnC5wx-UEZaJASWg9QpzXfIqCisAz1AwclfzszTUAaNOgNImnf9c9p69gfyRY1PmKs83bZVQoCxqhORFsoOba1lrcLZgqS3HCOVM_v_Y5CqPWMKkF7Qeq61HqRdbtQcXqeKSgIzwpEuU5UaEL7YLHGTxhDocrKr9xoyoyXITsHaWeeIiNOUNEy44aETBk8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=pj9Fh6QgpeaziedWtui6weQorZEYwvTfx49Gdu3WM7i_6o9Ks3eOPdEs0iS8m-ZlQjbAokWVDdrR8paaz-tq6_ku17Fs_4WEf2gq9fCmhmy226V-pHGqZ94jrEp6Q2XZJPPKbh82u2t13WBj3x2zqOWUnC5wx-UEZaJASWg9QpzXfIqCisAz1AwclfzszTUAaNOgNImnf9c9p69gfyRY1PmKs83bZVQoCxqhORFsoOba1lrcLZgqS3HCOVM_v_Y5CqPWMKkF7Qeq61HqRdbtQcXqeKSgIzwpEuU5UaEL7YLHGTxhDocrKr9xoyoyXITsHaWeeIiNOUNEy44aETBk8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای ناموسی در پخش زنده
😃
⏺
امیرحسین ثابتی:
نباید تنگه رو از دست بدیم، نباید تنگه رو بدیم بره. شما می‌ گید تنگه رو باز کنیم، مفت بدیم بره.
⏺
شهریاری، عضو کمیسیون امنیت ملی مجلس وسط پخش زنده :
بدید برررره، تنگه مال ننت بوده که بدید بره؟
مال عمه‌تونه؟ مال کیه؟ ارث باباته؟
⏺
امیرحسین ثابتی :
آقای شهریاری ادب داشته باش چرا وارد بحث ناموسی میشی تو پخش زنده...
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68842" target="_blank">📅 11:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68841">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=VMxV5jTxRrnnd0xWJu6hYhn29pfLwhfu2Sabv3RkJbPYgNJ2bkiCJGV0H5HBR4oLzzHhI9F-IoXO9NISMwGzcIHHEF1j9HXQCeQLygq9vne52-KXMRrRsf-H80GkHNMjywIIRPhXHNrBet59MNzvNGEPqOctACgXTlxmQcv-5IEft1Plzq79XgQJLvV11NjJ_CtkVSkQLMUwc-4QgStR3kgpB_wtRZC-jXCsTiuwYWRzWmfexQej9CXFHe3DPQF7nP39TwLq0MRNX06GtS8CwIkLKb7Dyx3U4EEObm3-HseaITt8VtkIrulrE524xCUuQeH727xXo-jHsaay1cvgjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=VMxV5jTxRrnnd0xWJu6hYhn29pfLwhfu2Sabv3RkJbPYgNJ2bkiCJGV0H5HBR4oLzzHhI9F-IoXO9NISMwGzcIHHEF1j9HXQCeQLygq9vne52-KXMRrRsf-H80GkHNMjywIIRPhXHNrBet59MNzvNGEPqOctACgXTlxmQcv-5IEft1Plzq79XgQJLvV11NjJ_CtkVSkQLMUwc-4QgStR3kgpB_wtRZC-jXCsTiuwYWRzWmfexQej9CXFHe3DPQF7nP39TwLq0MRNX06GtS8CwIkLKb7Dyx3U4EEObm3-HseaITt8VtkIrulrE524xCUuQeH727xXo-jHsaay1cvgjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دعوا بالا گرفته بین قالیباف و افراد افراطی!
🟡
الله کرم رئیس گروه فشار:
بهتون اصلا اجازه نمیدیم به هیچ وجه اورانیوم بدید بره.
🇮🇷
مشاور قالیباف:
به عنوان کی داری اینو میگی؟ نماینده مردمی؟ اندازه حزبت حرفت بزن زیادی نگو.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68841" target="_blank">📅 10:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68839">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=oujL-tBepBqIoJ2fAJHSRXc2m_rcilLaFUuIslYEoAK6LtdVMDcu5vdEbWejJSUEYCV6XZtp5g-CqUTWmB6M25ysDQw7kbi7LFtDpqU5eJMh8Ya7OdXVddy-xcCpfDgJZwJBLd9Vj1QtN4a8DE3eaQQpQELJm5jzLevhtyqDmtc6btu37dpu6BBZAzyK_umjlVRtSLFh11BPWTUbQ3_Qg6VRmZ9uphigVz0k4HKd4HW84M0LrJp5wWaQEF-4NBzJbvQvhRwIWafDtbOeCCvyHmJ5ImILvQGu_mydviscvKwsPlYjac664U8GMJgeAOGyLyW3CrdmYswPmxCQww9Bdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=oujL-tBepBqIoJ2fAJHSRXc2m_rcilLaFUuIslYEoAK6LtdVMDcu5vdEbWejJSUEYCV6XZtp5g-CqUTWmB6M25ysDQw7kbi7LFtDpqU5eJMh8Ya7OdXVddy-xcCpfDgJZwJBLd9Vj1QtN4a8DE3eaQQpQELJm5jzLevhtyqDmtc6btu37dpu6BBZAzyK_umjlVRtSLFh11BPWTUbQ3_Qg6VRmZ9uphigVz0k4HKd4HW84M0LrJp5wWaQEF-4NBzJbvQvhRwIWafDtbOeCCvyHmJ5ImILvQGu_mydviscvKwsPlYjac664U8GMJgeAOGyLyW3CrdmYswPmxCQww9Bdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حمله دیشب آمریکا به پاسگاه مرزی شلمچه
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68839" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68838">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jENsILgCH3es4VynhgkbxIr0GWENXEoSW2xDC500Onnucpy8IYycSAGB-vdb5v-HJdb4nP-Z0kSkSKM4_zrBIyrIQYc5vVomgYIOc66DqJd_IZ5xkV_XQbVbS8TuVu2rZi_UmAdObuY0clFzMgtbk8t6m8eFw-2eQqh9ayP5ypczfm2527H_h-0duXDZ1NzFMNC0wunVVZ3o5_yKO-7QZ2_snAda_G6lzs9hCKXfHOoHe1Kk_TUBj-NCrDCJ2HsFNTAUSI6qRsoLAVRv1xYXDL1qvFsP5cZBmnnP0PYU9CV6MQbrWkE7k_98cO74vNTR9uxnpR6Hy5uoWJDHVwtOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس برگه صحیح شده یکی از دانش آموزا که امتحان نهاییش رو 0.25 شده!
در جواب تمام سوالات نوشته:
با این مملکت درس خوندن جواب نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68838" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68837">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQQ0mVdacPstSJl5xyjsAdRDEOGKZLiMkPy8uotTKSOLo3NWWNfINfXITAQnGLAAIUYMK1RqJEA4UtVp6yJ9YT6Fte9NxmiyvKiKh7jbWErmTxcM-UVntmHluqGuPXotRhhi9_Z9jseckevs22Hq7jGwh20Tu4BaGOTD8k-xkW2k_cxX-8KlA3b3IoX72iNGRsLOrF0ZeXVhs-5bFmTwTtg_vfpxev1Oq87hSMJlb-GtNT45iyq9ME1yl0_1y2xpcohUMGZBXrF3ritGnyI4poICouVv3AyqhdEvX1G1WNP5cjs0qb8qpuTvHSizLAVTapTKsYel_KPmwi-NRNaOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👌
وال‌استریت ژورنال: ایالات متحده در حال اعزام گسترده نیروها، کادر درمانی و تسلیحات به خاورمیانه است تا در شرایطی که رئیس‌جمهور ترامپ احتمال گسترش درگیری با ایران را بررسی می‌کند، گزینه‌های نظامی قدرتمندتری در اختیار داشته باشد.
به گفته مقامات، ایالات متحده طی روزهای اخیر پروازهای باری را از پایگاه‌های محل استقرار نیروهای عملیات ویژه به مقصد خاورمیانه انجام داده است. نیروهای عملیات ویژه در مرحله نخست جنگ موسوم به «خشم حماسی» (Epic Fury) در عملیات‌های رزمی جست‌وجو و نجات به کار گرفته شدند، هرچند توانایی اجرای طیف وسیعی از مأموریت‌های دیگر را نیز دارند.
به گفته برخی از این مقامات، بمب‌افکن‌های دوربرد نیز در حال آماده‌سازی برای انجام عملیات‌های رزمی بزرگ هستند؛ از جمله بمب‌افکن‌های «بی-۱» (B-1) که هم‌اکنون در بریتانیا مستقرند.
وال‌استریت ژورنال پیش‌تر گزارش داده بود که ارتش همچنین هواپیماهای سوخت‌رسان، جنگنده‌های «اف-۱۶» (F-16) از پایگاه هوایی «اسپانگ‌دالِم» در آلمان و جنگنده‌های رادارگریز «اف-۳۵» (F-35) از پایگاه هوایی «لیکنهیث» در انگلستان را به منطقه اعزام کرده است. اردن و اسرائیل به عنوان میزبانان احتمالی این هواپیماها در نظر گرفته می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68837" target="_blank">📅 09:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68836">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⏺
فرماندار بوشهر:
روز چهارشنبه، یک نیروگاه در مجاورت نیروگاه هسته‌ای بوشهر در جنوب ایران هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68836" target="_blank">📅 02:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68835">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=XKD75xp8apOeMsSmQ3lXsP6cBE7c7w6p0O9m7Vo2y1Tni6JSgKOXMu1DVl7zXQhpCaUpCiJa3udamItfw0vaKEzTpiSoOhaZdWrSYMOkOYUsX-zQS8y3DtbVZHU58vsvXe722hgWBzB2QDDL2qsPf-KLvQS37rcaMMIeHt2tWUOQDNM0DlPWwXYB8pDLmswSScH7ObBsjTuVc6lTSuNxiyYhfMG441jFU6LSFSbDm-7x490Nea2udE5P_dNcH729WheVH--cD5W7LwnzpLs0og3yR0j33icN1slngN691EXVd-dwpPZt-Jaj-xWkWObViU_xjqUNrz9TUypPbqCWjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=XKD75xp8apOeMsSmQ3lXsP6cBE7c7w6p0O9m7Vo2y1Tni6JSgKOXMu1DVl7zXQhpCaUpCiJa3udamItfw0vaKEzTpiSoOhaZdWrSYMOkOYUsX-zQS8y3DtbVZHU58vsvXe722hgWBzB2QDDL2qsPf-KLvQS37rcaMMIeHt2tWUOQDNM0DlPWwXYB8pDLmswSScH7ObBsjTuVc6lTSuNxiyYhfMG441jFU6LSFSbDm-7x490Nea2udE5P_dNcH729WheVH--cD5W7LwnzpLs0og3yR0j33icN1slngN691EXVd-dwpPZt-Jaj-xWkWObViU_xjqUNrz9TUypPbqCWjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛مجلس نمایندگان آمریکا لایحه سیاست دفاعی ۱.۱۵ تریلیون دلاری را با اختلاف آرای اندک (۲۱۶ رأی موافق در برابر ۲۱۲ رأی مخالف) تصویب کرد.
این طرح شامل 95 میلیارد دلار بودجه نظامی اضافی است که عمدتاً برای تأمین هزینه‌های مرتبط با جنگ علیه ایران در نظر گرفته شده است.
این لایحه اکنون برای بررسی به مجلس سنا ارجاع خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68835" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68834">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0hru1Lr04gM0V5ROdAvYjMji1PHq3SUktopY-J4ywK7ejwlqqXkgwJDgWnMZCBOcutvv1smFexIRz6MDw4cCV_wJyQMGyV_VbdoAXib_8Pj73mjrCJJAD068N2kAmesxSXxWJHQjT0lGTQe8FwSFJp9yiiH-huzGmhShQdzZ1EOrDEKlCnNjyhvP5nle0DfXRI7iRBftgvAGAGFygV3AvfCeiGxvJ886P3SZmfwRj4Qz3X-0hZIwQcVUBJMO_zSiCQRHVu62bxDistTUt_gKWABijX77-H3u-HgK8yamQdJ45e4atW1ZSnbdQs82a3ab4wHoeEV7Is4azi3RRF3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ستاد فرماندهی مرکزی ایالات متحده (سنتکام): امروز ساعت ۵:۳۰ بعدازظهر به وقت شرقی، نیروهای آمریکایی به دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند.
این مأموریت با هدف تضعیف هرچه بیشتر توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاریِ در حال تردد در آب‌های منطقه، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68834" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68833">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدید حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68833" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68832">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇮🇷
هم‌اکنون حملات سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68832" target="_blank">📅 01:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68831">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPYzyLotDAn_M200zMnhbYsfWfySmt_6ZHx0uCz8jDl9dABGNjFXr-HWabeHc3NUnPtzqglMIm6rxl5XO61S8TH33vt84GanG5BhsjziD5QdxJZLPgmjJgYbLo9YBQG9-oFiIo1qYFXJl2_PF9MO6G34HY9woz3fn4ecfU1t1tRSrDSc_Tgr0mHemganqwNNWyT-ecvE7EXWK5aGsxF6C8AHzXr3vbpgN26WQhTBsmd8zF-0BhTisTizmdSoo-9lEQ3SG6LHFGK7B5iJVysytGzV_V1KpjcgDNAx7vzH6TOc1b8RCfDmWFLMBVCaEi89qvQN9jYmapA0C41jYOByhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب تا این لحظه هدف حمله قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68831" target="_blank">📅 01:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68830">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLdTFOhplI4qxCpZwC1duymJFQEBC2VRmQRPe5ghjLAOHmaU1nYGzawBQeO5VukN0wHKdUTObJ6l_4Ga5DNe9lFGGtB8wFVjMEUxeEjffh_MHrHIWF3e1Mrxfb6zjINu3y1ZMDTfcNmDYc1Kqgs0DXhWfxd0VwHxjeabRAiPHOlSOeXDLpo-tdKbwWDiySRox0IyLyBQ3Ggyd6r1URf8wNJ5oGQj3D_npF4oUgPZzlkMUMe5pLiAnY2g1fdgLnSlIVQaQcQwMavSW0iaA5axIt9KYEPL76fZv-FsHGbUMXWceXTenJQzV3o4CYpjZ3kdNkdvmaGE2F7dm3thXETbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.  @News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68830" target="_blank">📅 01:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68829">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30afc95033.mp4?token=MKgS6NHw9XNzkjRph3DsCZeUUJ4W77X9HWcgvt6Hkr6aCUDDoaU--3w9F6KGX5Ps4rfVjsDMdAXs9z3hdm7hbx4iyV-0QaZ_A8zxJcFVkFdoFgWEUzF8kUecIv68IIRTcoln9jLDiYQS6DzAQB_LgrxQ2kpBjmB7fp_aL7fl3UCfjihust1rOZkQk1HcyXF2V-ZK12UjjPAiHyB_zFwTNSVvgw3HdQ0NODex9Gfn1rskaHljVW3abjlCwFeSQysU9U_b9FZNG0eceS0WNI6ppdoEFZPkWYrkQZdA4rh1W-G9rj-lJv1ZjzmuNaE7cdevmCx0lRsM7T9qGjOTILDFkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30afc95033.mp4?token=MKgS6NHw9XNzkjRph3DsCZeUUJ4W77X9HWcgvt6Hkr6aCUDDoaU--3w9F6KGX5Ps4rfVjsDMdAXs9z3hdm7hbx4iyV-0QaZ_A8zxJcFVkFdoFgWEUzF8kUecIv68IIRTcoln9jLDiYQS6DzAQB_LgrxQ2kpBjmB7fp_aL7fl3UCfjihust1rOZkQk1HcyXF2V-ZK12UjjPAiHyB_zFwTNSVvgw3HdQ0NODex9Gfn1rskaHljVW3abjlCwFeSQysU9U_b9FZNG0eceS0WNI6ppdoEFZPkWYrkQZdA4rh1W-G9rj-lJv1ZjzmuNaE7cdevmCx0lRsM7T9qGjOTILDFkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68829" target="_blank">📅 00:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68828">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
صدای دو انفجار در بوشهر شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68828" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68827">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
فارس:
حملۀ موشکی دشمن آمریکایی به یک سولۀ انبار آسفالت در اطراف رامشیر استان خوزستان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68827" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68826">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI8HRQOhYXQZgtZt0k41PQzYGPpg4bT8eZrmHcW82dII0-D9Zizd8Q_UfXf2IZZv83r0V7U1OANpnhSVQoeDx_pMpNb0MUAnBAI8IotqyQ4vDmOdMLfnW2wJz9i9pkUw9cDyUkNRKUViZIjJ3rsYkdpQrmXTvdwrT_caZmVJPh2ofJcqFLVj6XZswy0FDslMt10YimU2v4qQ_gsPKC7z-cQoswjsqPlDoxMoeZWgBAVZqlSrPkMMIhxGIHqDK2Q6ExnWRgrleG3mlVthrf5moPawArzrlKb1SfcS0I5c7jBv7M7EZBCK9hz26AfnCRuCFaekG03ZXSJLJVi6tY0Crg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یک جریان مداوم از تجهیزات هوایی آمریکایی به سمت خاورمیانه در حال انجام است، که احتمالاً شامل هواپیماهای تانکر سوخت‌رسان نیز می‌شود، در چارچوب آمادگی‌ها برای تشدید عملیات نظامی علیه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68826" target="_blank">📅 00:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68825">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
پاسگاه دریایی زیارت در سیریک هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68825" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68824">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
دقایقی قبل صدای چندین انفجار در اهواز و ماهشهر نیز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68824" target="_blank">📅 00:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68823">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
صداوسیما:
چند دقیقه پیش، صدای انفجاری در منطقه بمانی، واقع در شهرستان سیریک، شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68823" target="_blank">📅 00:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68822">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/030860acf9.mp4?token=jxoazNTqMthbWansIcWhv2TDFJ6YmFcRHv2VltqBgFevdWL2jM91T_WS0kgNOt5zmcEpjexzJRKyhrWYo9NqKgLcx7AtgU14S7p_K5P5AGPE4qF48sOnb0JQXTBFL8GY7DH7gXbuxOTt_OM4HbjoXXjAATCz4F6xvuDgRKZ2A7jNgsQ6PEeT_xqb3JqhZPT9LGYuCFcXPt17QySiHGok2tlUW5qT0qh9raKvfUE4ZpmDX82Ub5GO_go8wB2ktpAQpvWTDQ48hLo7t6W1-SxoPxI9QyNzEIhePOAAm9dlxi4ZJUSgVpsXQXLu1M4HeShJ2qxb7WLy0RKZJMcYGtgGIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/030860acf9.mp4?token=jxoazNTqMthbWansIcWhv2TDFJ6YmFcRHv2VltqBgFevdWL2jM91T_WS0kgNOt5zmcEpjexzJRKyhrWYo9NqKgLcx7AtgU14S7p_K5P5AGPE4qF48sOnb0JQXTBFL8GY7DH7gXbuxOTt_OM4HbjoXXjAATCz4F6xvuDgRKZ2A7jNgsQ6PEeT_xqb3JqhZPT9LGYuCFcXPt17QySiHGok2tlUW5qT0qh9raKvfUE4ZpmDX82Ub5GO_go8wB2ktpAQpvWTDQ48hLo7t6W1-SxoPxI9QyNzEIhePOAAm9dlxi4ZJUSgVpsXQXLu1M4HeShJ2qxb7WLy0RKZJMcYGtgGIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه روز پیش که پل کهورستان رو زدن ، سریع اومدن یه جاده آسفالت از رودخونه خشک شده اونجا کشیدن که رفت‌وآمد متوقف نشه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68822" target="_blank">📅 23:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68821">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=QjIdtcdQiunDLnk3E4v3jKaPjV9jMOwGLlJWOl2DRF1lcRiGxL_MCzzaXtfC64WkStvxxqlfqShl3MvDHhc7rSI5ZCsAcIo5Jw-acva9PT2S6MN7M9azELNakImLjVe_s9H2LOn9TQS4RLvI4Wo5_nyQrTo99I5slP3ANG39x3D1ZZqOBAJj8-Fm4qGjKL9eLJvKA_Y6JUZfnCtQ_qf-uUe0J0rfZsiyevbqppeHLTRrOytFsWkyeiyIRn7N7EvYmbPFckDlmXkLYHErDY4hcPe_LopklmXqCpu2gL1LnuNrOEv0AG1juWeh9OneWF535FVnclxq5RolqxgnXaXPTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=QjIdtcdQiunDLnk3E4v3jKaPjV9jMOwGLlJWOl2DRF1lcRiGxL_MCzzaXtfC64WkStvxxqlfqShl3MvDHhc7rSI5ZCsAcIo5Jw-acva9PT2S6MN7M9azELNakImLjVe_s9H2LOn9TQS4RLvI4Wo5_nyQrTo99I5slP3ANG39x3D1ZZqOBAJj8-Fm4qGjKL9eLJvKA_Y6JUZfnCtQ_qf-uUe0J0rfZsiyevbqppeHLTRrOytFsWkyeiyIRn7N7EvYmbPFckDlmXkLYHErDY4hcPe_LopklmXqCpu2gL1LnuNrOEv0AG1juWeh9OneWF535FVnclxq5RolqxgnXaXPTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به تنگه‌ها احتیاجی نداریم؛ اصلاً به هیچ‌کدومشون نیاز نداریم.
ما نیازی به تنگه هرمز نداریم، اما مجبوریم این کار رو انجام بدیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.
من اسمش رو جنگ نمی‌ذارم؛ یه درگیری محدود بین ما و جمهوری اسلامی ایران.
اون‌ها اون‌قدر تحت فشار و ضربه هستن که می‌خوان توافق کنن، ولی به نظر من هنوز آماده توافق نیستن.
الان هنوز آماده توافق نیستن.
ولی خیلی زود آماده می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68821" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68820">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇮🇷
ستاد مرکزی خاتم‌الأنبیا:
رئیس‌جمهور ایالات متحده، که رفتاری بی‌منطق و جنایتکارانه دارد و به قتل کودکان متهم است، بار دیگر تهدید کرده است که به زیرساخت‌های این کشور حمله خواهد کرد.
اگر این تهدیدات آمریکا عملی شوند، نیروهای مسلح جمهوری اسلامی ایران اجازه نخواهند داد حتی یک قطره نفت از کشورهای منطقه صادر شود، و زیرساخت‌های نفت، گاز، برق و اقتصادی منطقه هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68820" target="_blank">📅 23:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68819">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=kQOjgY2Bpu8MPZ7D0HuTbyLZiWIDiODiwMnYJUP2tU7TEUV0zk1QTz5MrOg6ibOaoH5i14ILNhWkA7sBBD6sPt2vOBRXnSvTiYQ6sGsoyiOzeVke-WOqQX0zD8JbUg2DEBCIRArUz0au6BTDycQidGrD6G2DOioPoP1w5OT8jW5CiMJWsAKIINSlWZjMQLZZgx4k1G0vP_H6hhPBcllMO7XFA-N4Yxd__akC_-Z7uP-ft8YN3w7_D86kVnZGMr5C7l6EuiE_8OZ-bOyFS1nFDm8fkVw3U7gUYezAJdnuCfOIYIi9eb4JaWUaL1bnl1Q48wQUN9Q_HddTECvtw6jMKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=kQOjgY2Bpu8MPZ7D0HuTbyLZiWIDiODiwMnYJUP2tU7TEUV0zk1QTz5MrOg6ibOaoH5i14ILNhWkA7sBBD6sPt2vOBRXnSvTiYQ6sGsoyiOzeVke-WOqQX0zD8JbUg2DEBCIRArUz0au6BTDycQidGrD6G2DOioPoP1w5OT8jW5CiMJWsAKIINSlWZjMQLZZgx4k1G0vP_H6hhPBcllMO7XFA-N4Yxd__akC_-Z7uP-ft8YN3w7_D86kVnZGMr5C7l6EuiE_8OZ-bOyFS1nFDm8fkVw3U7gUYezAJdnuCfOIYIi9eb4JaWUaL1bnl1Q48wQUN9Q_HddTECvtw6jMKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو این اوضاع ویدیو های سمی هم وایرال میشه
😔
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68819" target="_blank">📅 22:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68818">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgllIDdXG_fJ4Prj_936Wf-ubS70lnrit5mdkUORlYrethCBKkyM7Wq4hG4J95eoGTZToFd5_O7V0c27sdpR0QnMzYFroYv8quGsDTVsHG6gJwBBm9V0q8owx8AS6TK-HYZHg4tvdu9h3Z-wW_J6sFSwxrdFuiUvDxa80gWkUk7VnwijcKFe_-fq0y2IXYo4OeZa6Yc9U_6-CtnjxfJiZzIPHV3_z3i8s2TT1H5woA0Kae521lAFJuKEVxrKgI_FNyLxg1xV8nyZ-u4eYeniDy_Y4p7nNhlOPybmqrQC_3BgkajMeYWbDA2-3vqKUg3YQBeYnU_6q-eK-_O0oO1mww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مجید موسوی فرمانده هوافضای سپاه:
اگر به پل‌ها و نیروگاه‌های ما حمله بشه
خاموشی برق متحدان و میزبانانِ کودک‌کشان، قطعیه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68818" target="_blank">📅 22:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68817">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=nLU6odq5rI3XPw-iPWiFu_pNNdecorZJOST7D2GWxrfZl7jE7AGOPrwNB_lir0uB9Ix9KiQDfH6zGgCqcXqjizLYigA0Q-iFUHs0DDR-07ucM_OiiqEPWfIo0bEMH4gigB6JH-XHH3J8qLNDE5WAnPz_21wIkdSDm8LgeflAEcRMPICcVVqK8oIcoXo6GlDlp6lUJOcCoxk9XWbNMITi8rLmGq7vrJACXnEtMNkIShUO6Mjyyi274AziSuUBZLhkglofoitfd5fNah9LNksxYcxvis1Pe9jX1TIphie_V-CYuYaz3yza_A9UNnMw6aw-yyCkYcAdtg_X6aIz5DUpEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=nLU6odq5rI3XPw-iPWiFu_pNNdecorZJOST7D2GWxrfZl7jE7AGOPrwNB_lir0uB9Ix9KiQDfH6zGgCqcXqjizLYigA0Q-iFUHs0DDR-07ucM_OiiqEPWfIo0bEMH4gigB6JH-XHH3J8qLNDE5WAnPz_21wIkdSDm8LgeflAEcRMPICcVVqK8oIcoXo6GlDlp6lUJOcCoxk9XWbNMITi8rLmGq7vrJACXnEtMNkIShUO6Mjyyi274AziSuUBZLhkglofoitfd5fNah9LNksxYcxvis1Pe9jX1TIphie_V-CYuYaz3yza_A9UNnMw6aw-yyCkYcAdtg_X6aIz5DUpEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ظهر چهارشنبه؛ لانچر مستقر در تپه‌های پشت اسکله طاهرویی (سیریک) که روز گذشته مسئولیت شلیک به سمت کشتی‌ها در تنگه هرمز را برعهده داشت، خود هدف اصابت موشک قرار گرفت و یک ستون دود از محل برخورد دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68817" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68816">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqdLh209jVsDME92VQ8T-F1wY13-2Hzt8FC1LbzdyF65nn_QqbpwvEMajDuKUaNHPy22LfpAQy18qbOmKn8VfdO2mWf360Yb4OtF1g65BCBBIpw1OHU0_6m3zuZCPbJFXubE37IXesTTIKWNYGEZh8MuCWXrMEMEjU__4ranenn0ffAiTpyVINMZ224oA0iF0h_oCZ6r3X0lQOIl5MMHn8U8ihSkGiS15HC-Z9iqZdZOZM7RkZFN-cjVfWNiaSursx88b12n3LzNEOeEroDhrob9yNHutfWg3YN_BcW4fmINlnpuZhYqjP_y5I2MzMohRu12p--TRnfFOjfCZW6Zig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت.
اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است.
بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68816" target="_blank">📅 21:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68815">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAu6_ioni2ypBcpJ_C5IO6hoP_swachDM6bQhZ8D5zA-do0Zp5CrhOdgsJWUc_3scd5ThEQzt-kDBAb-NvVrm0nUvIQwAl2a-SQ2kL-ik21Kd_ams352UAU5fsbGdJvjU72KQAwhd1U5grKbZgsDGoS2vgSnhIFXbaECYBVmGhPgLWpqzI9JXg6_b6ESxI71NoamqfLR8cyLW0x-XE5DD990P074ZFyv5ZpXZUUxabdlQBuYKTjz_kYi-7DPQaa4ozRnKNpN2HYkdJ2_CMlD_DrXUl6Hn2APshbJDofp9iAgZUdSQ-tIcRj-z7Is280nh9cy4EeNsDa0w5m3apT2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال:
رئیس‌جمهور ترامپ به‌تازگی اعلام کرد که پس از کشته شدن نیروهای آمریکایی، به «سنتکام» (فرماندهی مرکزی ایالات متحده) دستور داده است تا «درهای جهنم» را به روی ایران بگشاید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68815" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68814">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68814" target="_blank">📅 20:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68813">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6jxtGH3GzvOgbaWQJunnwM0qlq7uaV-rIrO58-L6jR7cHZBvSFQ1LxOqKMrB_3FNq1rh501bJit_qeKHuCKVse-X8luogUtMM7XLLWmVYZ30Sanern5-l6jxUN3mJvANcl7wxsnmodTT7gOPFalgDmbzF9mmPJBbnJjd5EhMLieEmceah-W5vOUqXQw-VC0RViu3BHwNtG-AB24i1NqX-Fw8nysklUk2Z3Pw4k_YGsFyplbxiwRUIIe1ASNbyx_KrU1pQb6h3iYOGshUUZ1wfrdaBBRBl8U83ToC_LGb6OawmwIHBAM4XBYKN6qtESuj9J8Ww8bpSkh_SFjtJn4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68813" target="_blank">📅 20:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68812">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3yZWZqoJXAv-qeC-Y5N8S3doevjE3cIUru1899nfnTsO1fSoBLm2R3hSbvqdG58P8QIOgl8CJLxkcV0dIYDGphgVdLossaQlfGPveB-Kgj8tS4I6fucwoB0S4WKy2ZJ1DcrXNjayFi53BR0QcyzT_dcCDIkPVInt_Obr2EBj15Y_38jboXBFS6JdWavOYbev1grCyaw7_5z8YBmAM9TpYvXbFciRGAb6ugPNd94kcMiqr6MHNPWERgokzh03SsxrIadM-JLHWqg_uhJfo43yJxqhLZgdBrg9wUCjC4-lKKuZ1Hqs0zNRJlMLVuXuw9A5zYXDCnjPU33_Il-QaEo4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یکی از حملاتی که شب گذشته توسط سنتکام در جریان یازدهمین شب متوالی عملیات علیه ایران اعلام شد، بخش نظامی فرودگاه بوشهر را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68812" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68811">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4MqTc_xlNokDQAm8P5XibG8Hy47UxCm2-xGY8-q8Py3mG9y8OEaie1mE6zZygmeICdr1eT43E0xu2GUf6qk96uQmlLydUUkx9npJ2dAjpIA7vWt-IGIdp5TNHUEDL51FUKHFMcJsUMXzQlbcdOW5xBaCADAO-xEgTHAmTLO6a9NBKDXUVhGykL_C8KputELyBv7hmiZOj-yedZUEHMsVjIY7GLZh5sA2MDgFs9fbXCH6GdPkVGggYKN_IIm6EM5eJHD1OtIGK35Qc_LZFrnqnEDHGYS9FijchjFu3a5ELfdsD8_nHSLxBDL3wpMqOGxtoWLkEvn3s75g79IznlBbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
قیمت نفت خام برنت به 93.14 دلار به ازای هر بشکه افزایش یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68811" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68810">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbxHZIvIxGyevNOV_vvAWYslygz3929ZnUXsliEkVfRMlpQBANrt5kfvGdipD-cbKBh3zhJ1A1r9AF5HD3xme0Tn-T_Y-s3U9GwHuUAexmVtCwXlLjqU9Ym29qBTYA_KeILHeG1BddjFDxhhb3gPpnhWUnCOme5ir17DwUYm4JyFRBUPRksqRblR3_Kb4xwPObrDS8AADpEHj-h04f08dCptI3ni4dp2ZSeiYBfPA46DDfZ61_7VL38lMGgpNTanHRKsjRMl006ATaEjjMwrOFiADvwnLw3iWnkHtCcdPtzozLCUGis1TCsU0okFVd19LriU2-BeSAbBGhZgw2vwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68810" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68809">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=pWjsPItmob76tz1oAsWXkqCozb0oCHRbHKNqRKx9Z5Av79Akvhto6IqqEr5hbcsF_lYuEL-xNFI6_ghawi3CHbHIwSUtoABzqRGLD_VytrkNgP0UrDIVfDecWfptOdNEWUvdWc_ORZ9hHtG3IyEaaI5a68iOTFrCvVa9OyXUKm1A4pTq9kGT0IkdLHvbZ62QdXFBCKsNP8pYLvVrxjy69BnQJl-nhZOIyA-e7ta1FoQibYW2wskVrnlOk10wMsnvf3SgcMv5tF7UlYp0_R_wOKnE6ePPTciXARuKBaRHsZrSnJKp8GYGGFCviMFGWG8UT4V2MjGmBR5cFbktm7rLrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=pWjsPItmob76tz1oAsWXkqCozb0oCHRbHKNqRKx9Z5Av79Akvhto6IqqEr5hbcsF_lYuEL-xNFI6_ghawi3CHbHIwSUtoABzqRGLD_VytrkNgP0UrDIVfDecWfptOdNEWUvdWc_ORZ9hHtG3IyEaaI5a68iOTFrCvVa9OyXUKm1A4pTq9kGT0IkdLHvbZ62QdXFBCKsNP8pYLvVrxjy69BnQJl-nhZOIyA-e7ta1FoQibYW2wskVrnlOk10wMsnvf3SgcMv5tF7UlYp0_R_wOKnE6ePPTciXARuKBaRHsZrSnJKp8GYGGFCviMFGWG8UT4V2MjGmBR5cFbktm7rLrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس انقد کد کد کرد که
کص
از دهنش پرید بیرون
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68809" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68808">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=CP7iUiEzzKbXmXBAA7FcCEwSqAY8os2E0DDW4n3DltMLAjXQ1fDD0AHlLphEB2v-I9j0mmyDUlNy6I67Fxn9ODb6VjtBI7JCV6qKqK11NlGeUjkKjEvoJGFj-FyEe8HySVzd1FbmTmWojyhz6aPgI7Va2EDSfTukrCKTOrvrvstHsz9aQIr9WOJVC0l14P_d6QqmNc9rpQehGIzoaHEfIRRFhANNutYbskZfDxibZqEVCSXnzL7VVDn3hekr3sqJBdpP36HIqjtzNrovj8CMf7NoF4HpOq407TrkHZlRP9vfJyQGqpFOr_dILDjkOCxzexVTg5iR0NfpXdNyvpVQ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=CP7iUiEzzKbXmXBAA7FcCEwSqAY8os2E0DDW4n3DltMLAjXQ1fDD0AHlLphEB2v-I9j0mmyDUlNy6I67Fxn9ODb6VjtBI7JCV6qKqK11NlGeUjkKjEvoJGFj-FyEe8HySVzd1FbmTmWojyhz6aPgI7Va2EDSfTukrCKTOrvrvstHsz9aQIr9WOJVC0l14P_d6QqmNc9rpQehGIzoaHEfIRRFhANNutYbskZfDxibZqEVCSXnzL7VVDn3hekr3sqJBdpP36HIqjtzNrovj8CMf7NoF4HpOq407TrkHZlRP9vfJyQGqpFOr_dILDjkOCxzexVTg5iR0NfpXdNyvpVQ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
عراقچی: ما به هیچ عنوان غافلگیر نشدیم!
واسه همه سناریوها برنامه داشتیم و کد بندی شده بودن.
سناریو آخر این بود که رهبری (علی خامنه‌ای) رو بزنن که کدش 110 بود.
تو جلسات کسی دلش نمیومد درباره این کد صحبت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68808" target="_blank">📅 18:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68807">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
یک منبع نظامی به تسنیم:
هر پل و نیروگاهی از ایران هدف قرار بگیرد چندین زیرساخت و تاسیسات انرژی منطقه را می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68807" target="_blank">📅 18:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:  بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.  @News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68806" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=Yqf6Bh9u6u15qz2dQnyeet40RJdM1Qiji5nNR76ZXsOnHRN3BPyAqt9uIgMmw7T1qP1PmnEG8Am7q-Kzpo1UJG5GEMgp0GNQ2TJSYFNQPLN-4IJOs1TEmda66pHL6xzz1Qqc4AxMSNy3L4gSNXCVtUiwwumDswov-cA_JZaDLZ33lOobrzjKML3v3x9GV5KojCp38Ejy6kz5VSdx7Srqi0dnks_tf8RmXyqEFyBaDR8HFRa1yRu7yGn5c_gmC0ZZk3SQVMzX3prmTOtjsH7LsEK7AJKpn3GUUWrEsR06ewJYkPtfGNIcg3EZYXxx_XqI1IBivBhUnQXsNHBxM2YBRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=Yqf6Bh9u6u15qz2dQnyeet40RJdM1Qiji5nNR76ZXsOnHRN3BPyAqt9uIgMmw7T1qP1PmnEG8Am7q-Kzpo1UJG5GEMgp0GNQ2TJSYFNQPLN-4IJOs1TEmda66pHL6xzz1Qqc4AxMSNy3L4gSNXCVtUiwwumDswov-cA_JZaDLZ33lOobrzjKML3v3x9GV5KojCp38Ejy6kz5VSdx7Srqi0dnks_tf8RmXyqEFyBaDR8HFRa1yRu7yGn5c_gmC0ZZk3SQVMzX3prmTOtjsH7LsEK7AJKpn3GUUWrEsR06ewJYkPtfGNIcg3EZYXxx_XqI1IBivBhUnQXsNHBxM2YBRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
دونالد ترامپ درباره ایران:
«آن‌ها بهای سنگینی خواهند پرداخت. آن‌ها در حال نابود شدن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68805" target="_blank">📅 17:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68804">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhXtxVtCGOYSKcyX4hgfjzxiJFOFS47V06xSfcAlgH-vFS4hRN37g2-mUkD7_8pYWM5RM7IdrI6ZoNQVUZT2SHJIQAAjuAWnejUjqarKDdhKyNUaFvKKItjN0mzev55eYgsDwXRAuBqyeoZ7T_iSS1Wq9HlyPoDr_B_CkTcSBmSx8mNoWTGp_zvgokcRX3MPd1RqZOySIurgbe0kNdz-QaYWnJoUqJ3Rd9XnYOvAAPkmwNMEu1V5puaqqMMr9UWgXWj1F97ZkpIWO9UefNdXwQwIUJm2fgBsG2cCkTM-onxmHibeo2VbDq2TYBvuL4cCqtHOfzAgKetU5u3zeqt5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68804" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68803">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIrkWgbPh0w0SpziOWH9qBk72Xx0yPLWC-CuTwuVyFClWXz25AOsHYxbXTXOxvvcYaYzqh8DLOfHh239JxP47-2_Td2kCceIirTDU-WNYIqHG_OFF8yszeA99z8X2EPQAyRqREIPlJ6zuh31LzJBBp7NWCPjnCsB-64wbOcrzzWK35G3LjhzJp_z_QgPh91T7OUUc0o8HNOGHvkX8N11lBQtLTBSI_pwUKNxxrX7lP3BVD1s5nWERjAqDBsa7oiyxilTfOGcoFyyN2KI3peQaZwqJ0X3Y4dknexeF4IaG1uIEvKOE0Y1zmV1DkcOQ8mNOFA9rfX_L_7Kwe9lo2QqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه
حتی اگه نزدیک تهران یا داخل خود تهران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68803" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68802">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=jU1WwxciQXaXIxEuMN5REocnHeTfPilcKNGQm32LsmvUkagSkZCBfLSL3-n_FvTimBmaPi5LbcuWIk7pBdW4yOKipi2SRNDN3Sg59lxTk5jTLyYcMY-afq4vfxCioVtDiSQ_ujH9ZEN_wJN12EEA8Ovmi7YTNZ_HeCmSeWwgZ2HfHwlF0HOpUERKVdRlVcUOuLWimY4vNifOjbQwZ_Yi7UjbQuVR7U5vFUEBd6cDMvg-1SSJBhXK17NgUjEIzBegjea2z2Mf8zSyeGKZ1l9YdYgrd6XeKz6c0o8EbNOp7g0dq5Re4Ea3DKnZydP_aPJYVK4bLV7ni4o2BUyk0bEOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=jU1WwxciQXaXIxEuMN5REocnHeTfPilcKNGQm32LsmvUkagSkZCBfLSL3-n_FvTimBmaPi5LbcuWIk7pBdW4yOKipi2SRNDN3Sg59lxTk5jTLyYcMY-afq4vfxCioVtDiSQ_ujH9ZEN_wJN12EEA8Ovmi7YTNZ_HeCmSeWwgZ2HfHwlF0HOpUERKVdRlVcUOuLWimY4vNifOjbQwZ_Yi7UjbQuVR7U5vFUEBd6cDMvg-1SSJBhXK17NgUjEIzBegjea2z2Mf8zSyeGKZ1l9YdYgrd6XeKz6c0o8EbNOp7g0dq5Re4Ea3DKnZydP_aPJYVK4bLV7ni4o2BUyk0bEOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مقایسه جمعیت ۷۲ هزار نفری در کنسرت فردی مرکوری در ومبلی لندن (تیر 1364)
و جمعیت مراسم نماز و تشییع علی خامنه‌ای در مصلی تهران (تیر 1405)
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68802" target="_blank">📅 16:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68801">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⏸
ویدیو وایرال شده از گریه های یک دختره بخاطر مردن سگش
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68801" target="_blank">📅 16:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68800">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏
🇮🇷
سپاه پاسداران:
«اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت»
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68800" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68799">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJc-ulBsShtPAP9jE39f_Mahj6hs7Tj2cuPJoU0PO9KkhzOrQnvmTvp3kyTYBTBDLPvRVpgCcYhLn3w7HuSHfuz0iXSzO6HqiDt6px1F4gHC5sqDM0PPbXwAFMW19LwdUoc4EHEqdmUqNw0rAesppQ-Sa3hHGsjGJcwNKwMdIvaTGo9ds_ay-bHWq18YoiKgG6qOO04XQAMhQ8PUOMB1Pg5Uycm_k31OqYyvKaihUsxCAVFgpwcW3vbJeeReKnkdzHVB74xvU3OqQsBfIETfq4Z3KdQf4zr1j1JkAbkjoQYqcXaBy1cDbMo9rZUdF8LS6sVPmUxlWuvvLFqkwL7shQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آژیر خطر در عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68799" target="_blank">📅 15:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68798">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران به بحرین و عربستان سعودی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68798" target="_blank">📅 15:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68797">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=spkShLW1TP9HOa70jhmbPzXRe6hzp4aPF_ekvAn3ZOizVB52DnE9BjeplGt5jYn0vPjSQQ1fyMQYOx2bTPdMxcHSyGycy7W9JYYEy8QSzvClXidfZtY3GRoAnUrIvruWF07icN2CtnRzmVdBnt1B28LgFwtd8-pJij6Lh9L9H6gQZnOnUkJYsnUb4RqjlF9JclQ4hYqbX1B_WNXcCCmEosqeVccGoQrtPmKov1Sq64shoP-nrxchUfWTmYLVfccBCuYt8vdaB3Ab5l_q5rESP1j3eOjxoAMaq5kOFMh7c4kjjzQAa-TR3qIsNpM1oj4Pf9TE2QsTidMjdaYlacEoZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=spkShLW1TP9HOa70jhmbPzXRe6hzp4aPF_ekvAn3ZOizVB52DnE9BjeplGt5jYn0vPjSQQ1fyMQYOx2bTPdMxcHSyGycy7W9JYYEy8QSzvClXidfZtY3GRoAnUrIvruWF07icN2CtnRzmVdBnt1B28LgFwtd8-pJij6Lh9L9H6gQZnOnUkJYsnUb4RqjlF9JclQ4hYqbX1B_WNXcCCmEosqeVccGoQrtPmKov1Sq64shoP-nrxchUfWTmYLVfccBCuYt8vdaB3Ab5l_q5rESP1j3eOjxoAMaq5kOFMh7c4kjjzQAa-TR3qIsNpM1oj4Pf9TE2QsTidMjdaYlacEoZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی:
هم‌وطنای عزیزم، مردم بزرگ و شجاع ایران،
با توجه به اینکه تنش‌ها داره بیشتر می‌شه و احتمال داره حمله‌ها، مخصوصاً تو جنوب کشور، گسترده‌تر بشه، می‌خوام چند دقیقه باهاتون حرف بزنم؛ به‌خصوص با مردم عزیز سیستان‌ و بلوچستان، هرمزگان، بوشهر، خوزستان و همه کسایی که کنار خلیج فارس و دریای مکران زندگی می‌کنن.
🇮🇷
جنگ و بحرانی که الان کشورمون گرفتارش شده، از نگاه من یه مقصر بیشتر نداره؛ جمهوری اسلامی.
ولی جنگ واقعی، یعنی جنگ جمهوری اسلامی علیه مردم ایران، از 47 سال پیش شروع شده و هنوز هم ادامه داره.
همه مردم ایران یه جورایی از این حکومت آسیب دیدن. نذاریم کسی طوری حرف بزنه که انگار جنوب ایران تازه وارد جنگ شده.
جنوب ایران از همون روزی وارد جنگ شد که بچه‌های بلوچ به خاطر نبود آب آشامیدنی و امکانات اولیه، قربانی گاندوها شدن؛ از همون روزی که جوون‌های سیستان و بلوچستان، سرزمین رستم، مجبور شدن برای یه لقمه نون سوخت‌بری کنن؛ از همون روزی که هرمزگان و بندرعباس، با اینکه بزرگ‌ترین بندر ایرانن، تو فقر و محرومیت رها شدن؛ از همون روزی که بوشهر با اون همه منابع گاز، و خوزستان که قلب صنعت نفت ایرانه، خودشون از ثروتی که تولید می‌کنن سهمی نبردن.
👑
اما ایران آزاد یه کشور کاملاً متفاوت خواهد بود.
با روی کار اومدن یه دولت ملی، کاربلد و توسعه‌محور، سیستان و بلوچستان می‌تونه با تکیه به موقعیت راهبردیش، جوون‌های توانمندش و دسترسی به آب‌های آزاد، به یکی از مهم‌ترین موتورهای رشد و پیشرفت ایران تبدیل بشه.
چابهار هم می‌تونه دوباره به قلب تجارت ایران و دروازه اتصال به اقیانوس هند، آسیای مرکزی و بازارهای جهانی تبدیل بشه؛ با احیای همون برنامه‌ای که قبل از انقلاب 57 قرار بود اجرا بشه.
هرمزگان، بوشهر، خوزستان و جزایر خلیج فارس هم با توسعه تجارت، گردشگری، صنعت و جذب سرمایه‌گذاری، می‌تونن به ثروتمندترین و پیشرفته‌ترین مناطق ایران تبدیل بشن.
✊
هم‌وطنای عزیز،
🇮🇷
این حکومت نه برای مردم پناهگاه درست کرده و نه حتی توان دفاع درست از آسمون کشور رو داره. در حالی که خودشون تو پناهگاه‌های زیرزمینی قایم شدن، از مدرسه‌ها، بیمارستان‌ها و مراکز غیرنظامی استفاده نظامی می‌کنن و مردم ایران، حتی سربازای وظیفه، رو به سپر انسانی تبدیل کردن.
توی جنگی که جمهوری اسلامی به کشور تحمیل کرده، اولین و مهم‌ترین وظیفه شما اینه که مراقب جون، امنیت و سلامت خودتون و خانواده‌هاتون باشید. چون شما سرمایه واقعی ایران و نیروهای اصلی برای پس گرفتن کشور هستید.
دفتر ارتباطات و رسانه من هم به‌زودی توصیه‌ها و راهنمایی‌های لازم رو منتشر می‌کنه تا مردم بتونن امنیت خودشون رو بیشتر حفظ کنن.
آماده بودن و ادامه دادن این مسیر، یه مسئولیت همیشگیه. هرچقدر مردم قوی‌تر باشن و جمهوری اسلامی ضعیف‌تر، رسیدن به پیروزی نهایی سریع‌تر و با هزینه کمتری انجام می‌شه.
👑
پاینده ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68797" target="_blank">📅 14:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68796">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=LJtIGQoLwsulI8l2u9zE-GoJR67VH4YrGHF-C8AaNAiFlrJ1Nb_tiMJ1rP6mtkVHqcdvFpXpypnIVztlW9oPScdwKOdIqk1t5M3wIiHuLTPlAMN5biG2XzrL0DTq-G3KhR-rni6strBdNmwU5VpSULb9Sbd8xK6A2Y8JRcveyxMi0MowX6y3NbfGbcm6_2DTzOu3pMfQIgDgMjj28cXJDISWLXHbrmVf8bQZQGEaEQu5vNMy4ZZOwJBGNfJecPV5Dfip3EABXadktlu22jE4BsYkEWn_J2hd_JqiYfRN7jn_oIMHgurepfJI5Go6sUxuZauLEbb8lGZ-yBqj9q9teA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=LJtIGQoLwsulI8l2u9zE-GoJR67VH4YrGHF-C8AaNAiFlrJ1Nb_tiMJ1rP6mtkVHqcdvFpXpypnIVztlW9oPScdwKOdIqk1t5M3wIiHuLTPlAMN5biG2XzrL0DTq-G3KhR-rni6strBdNmwU5VpSULb9Sbd8xK6A2Y8JRcveyxMi0MowX6y3NbfGbcm6_2DTzOu3pMfQIgDgMjj28cXJDISWLXHbrmVf8bQZQGEaEQu5vNMy4ZZOwJBGNfJecPV5Dfip3EABXadktlu22jE4BsYkEWn_J2hd_JqiYfRN7jn_oIMHgurepfJI5Go6sUxuZauLEbb8lGZ-yBqj9q9teA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تفاهم‌نامه هیچ حقی برای حمله ایران به کشتی‌های تجاری قائل نشده است
.
🎙
خبرنگار:
آیا این تفاهم‌نامه (MoU) ذاتاً دچار اشکال نیست؟ چون در بند ۵، به نوعی به ایران نقش و اختیار در تنگه هرمز را به رسمیت می‌شناسد.
🇺🇸
مارکو روبیو:
فکر نمی‌کنم متن تفاهم‌نامه چنین چیزی را بیان کند. این تفاهم‌نامه به ایران حق نمی‌دهد که پهپاد و موشک به سمت کشتی‌های تجاری شلیک کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68796" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68795">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=PdjXGEOcl3z69guAIIszxmpMBKSIuCMIIZHH3eiEEk1sdLqp9JDCzHre-Vb0qiEygThf5X6U9CUMw3vG0FSw0mDh4gIBUGQArMweij8k6TSaqCTc6e7---_7AJXZAZ5E7MmUx78ZhbMI8yHrNG1qH79pmVo6G0TOlqI_i5_n9V5GXLioSLdP0x7YlQxCWd6gwJHHdQDJfhvSdwXOHi68bTWfrc2ecumOqPMJuwuXeUO-1U97Ov5KuiZHdjS3zW0sNTLgS9fRWHUpPFRXoyB14TFqB33Uz9NS69oemCuNDVGnVEADuobN4WmRAbV1X7bSu8Q8P0GwbYe50CSKsf4Ytg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=PdjXGEOcl3z69guAIIszxmpMBKSIuCMIIZHH3eiEEk1sdLqp9JDCzHre-Vb0qiEygThf5X6U9CUMw3vG0FSw0mDh4gIBUGQArMweij8k6TSaqCTc6e7---_7AJXZAZ5E7MmUx78ZhbMI8yHrNG1qH79pmVo6G0TOlqI_i5_n9V5GXLioSLdP0x7YlQxCWd6gwJHHdQDJfhvSdwXOHi68bTWfrc2ecumOqPMJuwuXeUO-1U97Ov5KuiZHdjS3zW0sNTLgS9fRWHUpPFRXoyB14TFqB33Uz9NS69oemCuNDVGnVEADuobN4WmRAbV1X7bSu8Q8P0GwbYe50CSKsf4Ytg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مراد ویسی:
دیدم مردم به من گفتن عراقچی رو فالو کردی رفتم توییتر نگاه کنم ، دیدم نه تو توییتر ندارمش و رفتم تو اینستا دیدم اره عراقچی رو فالو دارم که احتمالا دستم خورده بود و انفالو کردم.
مرسی که بهم تذکر دادید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68795" target="_blank">📅 13:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68794">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
فارس:
دقایقی قبل صدای سه انفجار حوالی سیریک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68794" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68789">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=rFJEOZ_YtmJzixoDPabJCFvkYRw8xKKKndxAOTrW3-42R90k11TvlbaH7xY1WPmnvnlkQ8yzZwH_JdwsmBRchRPnxDe3rxA6cswoes_oVW4LoG5C1aD-gwvPw7RdLmj71I8FzyUCA8Mu6bJHMvmoHHT3IK-Vgn0-xVezSSrSAO-r67rrrNFIw91fV7Y-0gHH-Zzq4Ef_rNgfz2K12JySKIIuEuUHHMUYXpY-6Xi5K4pldaCuRWE6Xx8vfkgFC8MFfxfyJfJdvMzPCe6kSwboIpSRcrdgnEuF_yRdCc_mc3LA_xTFHd19aCyNiHEvzXEawBYJJs5SQFRrlcU4e7VRFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=rFJEOZ_YtmJzixoDPabJCFvkYRw8xKKKndxAOTrW3-42R90k11TvlbaH7xY1WPmnvnlkQ8yzZwH_JdwsmBRchRPnxDe3rxA6cswoes_oVW4LoG5C1aD-gwvPw7RdLmj71I8FzyUCA8Mu6bJHMvmoHHT3IK-Vgn0-xVezSSrSAO-r67rrrNFIw91fV7Y-0gHH-Zzq4Ef_rNgfz2K12JySKIIuEuUHHMUYXpY-6Xi5K4pldaCuRWE6Xx8vfkgFC8MFfxfyJfJdvMzPCe6kSwboIpSRcrdgnEuF_yRdCc_mc3LA_xTFHd19aCyNiHEvzXEawBYJJs5SQFRrlcU4e7VRFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🚀
حملات شدید پهبادی اوکراین به روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68789" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68788">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=fu1BJBvFQof8vSSnU1d7Pv7CQPyBI5tJNBFjp-GM7tk31I8FMB--63ub4LTMg-LZzIwfwzAzO_DlzBMRxMdklRgImxjP9eHdxREeBfhQ5SCCzfs7rGT8n-aZ-i42CKl-kjTz4gAQzMLJCYugbgKgMR_8SySDZn_-PvIQprxC1hF9rMTDA2Q5yU62dBrfSY6QurD-_TgsGKJWzHIVx2e4DCJP2Tfwtg1Bb20tepnyWJe7Gh49pZTLOb3WGNe4AlYOtMu690I8PRu7Q3hX86PRVGUSV2LfOdx3YPnbOU25Yap6-x6htUBFHYG17mOw3aVRXTLED58htWdXakIuAXTlqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=fu1BJBvFQof8vSSnU1d7Pv7CQPyBI5tJNBFjp-GM7tk31I8FMB--63ub4LTMg-LZzIwfwzAzO_DlzBMRxMdklRgImxjP9eHdxREeBfhQ5SCCzfs7rGT8n-aZ-i42CKl-kjTz4gAQzMLJCYugbgKgMR_8SySDZn_-PvIQprxC1hF9rMTDA2Q5yU62dBrfSY6QurD-_TgsGKJWzHIVx2e4DCJP2Tfwtg1Bb20tepnyWJe7Gh49pZTLOb3WGNe4AlYOtMu690I8PRu7Q3hX86PRVGUSV2LfOdx3YPnbOU25Yap6-x6htUBFHYG17mOw3aVRXTLED58htWdXakIuAXTlqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی وزارت کشور :
عباس چرت میگه مشهد سقوط کرده بود، تو دی ماه من خودم مشهد بودم خبری نبود اون شب.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68788" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68787">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68787" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68786">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXLrVgoV6dtPvIOAYQ87fqJiotdej2BWvwLhIiWPWzWuBTTv6FylK6i_rFoLgaJJS_7SefqpEjtQUT224b2tsYnEM5Vah2c4Z5j1wSSKEtdnmNA1Pk_buyle_AN4YxEf6zJHu6zUWCFc-XTKYpKotSuVRiUep3XlMOsY0QbexJVpiKJ3HyHnds_wiMxWS8FMordp6dQviQt0mTJg8670wX3-jaJlAClWgmVLSbcT65RXM4lmnoHxxw47VicM2KCb_XgWY0vxr3rghBEOZhWPU2PaDSn6MbzmpkaXITh-vnLfnC92q694mQvaSJfpD5_9zTBxbBrSwx4xMygdjKHvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68786" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68785">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=evsYdlv7JeiSscTnqB0N-GOyxRKnbCTw58DUsIWgHzIN7l0mEfyFBj6mx2PbeGPzBk0MNSxruuMvbaaPDbbYBxDqXJgrvHRRKLzL-mq5yxzkCHsvd0O_STMmPSeUzWWsmeiZoLKGtDACHt8w-Rw2MMHXoWoh2-KgswZ75EE5sS3xCEjfXUIte23v6ykuBxIwp2hfXOgskCRgsO2H4hfYBMUwKdcinlEEa3LWjyg0ToSVZBdzEH-4vDU-IHUjIlwb7tEApC-YGtFe9EkD0I1tPmuOYbYRDRD1XZSwO4aqWn-5Numo1h0TYotFXJP_s0Ter1Icf8KgJgYxyxdYfTZzxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=evsYdlv7JeiSscTnqB0N-GOyxRKnbCTw58DUsIWgHzIN7l0mEfyFBj6mx2PbeGPzBk0MNSxruuMvbaaPDbbYBxDqXJgrvHRRKLzL-mq5yxzkCHsvd0O_STMmPSeUzWWsmeiZoLKGtDACHt8w-Rw2MMHXoWoh2-KgswZ75EE5sS3xCEjfXUIte23v6ykuBxIwp2hfXOgskCRgsO2H4hfYBMUwKdcinlEEa3LWjyg0ToSVZBdzEH-4vDU-IHUjIlwb7tEApC-YGtFe9EkD0I1tPmuOYbYRDRD1XZSwO4aqWn-5Numo1h0TYotFXJP_s0Ter1Icf8KgJgYxyxdYfTZzxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این ویدیو از اینکه نشونه آدم پولدار چیه، اخیرا خیلی وایرال شده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68785" target="_blank">📅 12:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68784">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBPsST9rB-EW3pvxM-18L0tL5-g2qtdyTNa3xCBDsizUHP9X5-sA-LCddM-gN59_D4CQjHWJ5zfsyxMEpjQ0l71yi50CtYLuEgVlSnWs8OByUjS6Ehbdw5fUepCAqRX4Y95ytTRGBCGtVLSMxKJ0YjUlcgLZYAlLAy2rrsXvkzamuxH6kA1OP7x7vZtFv8cg1LpLxJpPrDGaGPgrJbd4R7eAepUgRnlAMZMmpHw4gS1MZkXGU9FroMDDd3guMkF2lq4dF8isSR4Lf-f0kS80SCpm_WYQ7LHimtpFVt0TpLiYmxq_JTPtRUdBDZLysqdlBrMDSG1Scdn2aVpnFD192w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
شلیک موشک از کرمانشاه به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68784" target="_blank">📅 11:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68783">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=CmessY4NTOspX_6NPqO_HBYC-jiHeZx9oD1cSyABZUKxdcAu5rMvoi9miNS4-PLm-j_A_ar4LmI5bG3B3hJHFuAjnJ2ugESNU8hQVay040JnA5PE-6pksHNBeSpBnm7ZSwv99-VTcyJc9XqEJ1y-KcBFXzpod9ocmStEXGw_CnmMReFVrYU4Znb5cdSTUoYS_e3KOnALmEE2nc8U2hF4Vcsl9vrKcBZrM8dx02uF7JKp5o1daCdAPW12AvwxHqUNkrOnRkpmvvV1-6qHtqPb-FBKeX6H7ar-VAXUTPZzpIlZTKhwsSWTTbhI-vxQ_fipZfQfqWamaNXDcKGfArgI0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=CmessY4NTOspX_6NPqO_HBYC-jiHeZx9oD1cSyABZUKxdcAu5rMvoi9miNS4-PLm-j_A_ar4LmI5bG3B3hJHFuAjnJ2ugESNU8hQVay040JnA5PE-6pksHNBeSpBnm7ZSwv99-VTcyJc9XqEJ1y-KcBFXzpod9ocmStEXGw_CnmMReFVrYU4Znb5cdSTUoYS_e3KOnALmEE2nc8U2hF4Vcsl9vrKcBZrM8dx02uF7JKp5o1daCdAPW12AvwxHqUNkrOnRkpmvvV1-6qHtqPb-FBKeX6H7ar-VAXUTPZzpIlZTKhwsSWTTbhI-vxQ_fipZfQfqWamaNXDcKGfArgI0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
‌علی‌اکبر رائفی‌پور، ازحامیان جمهوری اسلامی:
با شناختی که از سپاه دارم اگر نظام سقوط کند، سپاه پاسداران موشک‌های خود را بر سر شهرهایی خالی خواهد کرد که به کنترل طرف مقابل درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68783" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68782">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=nUZyd-hwWtaUpnRK_UkKbv6-TkjW2G910JnMg5bTusHAc66PmAHgEVhvMeqSkD1vn42UsDk5XBSwdxJmpuUMKyjFz_wT0JO3tFO5HApFRN-_u1ZWA411WFIygEo9a9kPQH5g0EyvWSeMDFzI8uVLin8wED3aSBU3tbgqHJbLG4brjwxwygahtlxhrWFSA4mjanq7xUCS7EBq0WgMvaalmmt5VPVunESfcGEP9wjbZdKN1wrYLy5YlkNyWq6CJhCDlxWUD9NI4BMTlPeQbW88vnCwtwSn3xJd_Q0DItHEkjnSrnQc0EYWSYC5GFnhg-qBqvKs0DwF83YlI3XMpeHKpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=nUZyd-hwWtaUpnRK_UkKbv6-TkjW2G910JnMg5bTusHAc66PmAHgEVhvMeqSkD1vn42UsDk5XBSwdxJmpuUMKyjFz_wT0JO3tFO5HApFRN-_u1ZWA411WFIygEo9a9kPQH5g0EyvWSeMDFzI8uVLin8wED3aSBU3tbgqHJbLG4brjwxwygahtlxhrWFSA4mjanq7xUCS7EBq0WgMvaalmmt5VPVunESfcGEP9wjbZdKN1wrYLy5YlkNyWq6CJhCDlxWUD9NI4BMTlPeQbW88vnCwtwSn3xJd_Q0DItHEkjnSrnQc0EYWSYC5GFnhg-qBqvKs0DwF83YlI3XMpeHKpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⭕️
گفته میشه دیشب با وجود اینکه پدافندا توی تهران خیلی فعال بودن اما انفجاری گزارش نشده.
احتمالا دیشب بیشتر پهپادهای شناسایی آمریکا، مثل MQ-1C Gray Eagle و... تو آسمون تهران بودن و پدافندا هم سعی می‌کردن اونا رو بزنن.
احتمالاً مأموریت اصلی این پهپادا دیشب شناسایی بعضی مکان‌ها، مراکز نظامی، محل استقرار پدافندا، و... بوده و ممکنه که آمریکا درحال آماده کردن خودش برای دور جدیدی از جنگ باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68782" target="_blank">📅 10:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68781">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=j5ioQYfdE8PdUe8JoOwAiFbR4lIj42WHTJALyXiUjPq58uhFSeaFgzPBxebbZ5uNUIaKoXzc6iwWm-d0KY4F5mpVX9aDF_5GwK_MHfpz_zFRXC0J_PpUaoPtZCnnJoYEbu0FfFLPKr1L35d1yTzZkjhYRB-eIbYzVSMMUJv6PHOZzNtk2RkF3xw8dllZAMBhiGkjT5oDoD5R_xPogL4JGzCT8f3z-5uIX3q8-M0-0_xHQfKe0omwv7YLvDIsId3i8QuEb_O2ycuVgkNpxxjMibCmrlMybEqRr2iLSEJJXIwlYJn1dZ1W_OK9I1XardPcCA8jK0lbU4WgvpwK_oO2lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=j5ioQYfdE8PdUe8JoOwAiFbR4lIj42WHTJALyXiUjPq58uhFSeaFgzPBxebbZ5uNUIaKoXzc6iwWm-d0KY4F5mpVX9aDF_5GwK_MHfpz_zFRXC0J_PpUaoPtZCnnJoYEbu0FfFLPKr1L35d1yTzZkjhYRB-eIbYzVSMMUJv6PHOZzNtk2RkF3xw8dllZAMBhiGkjT5oDoD5R_xPogL4JGzCT8f3z-5uIX3q8-M0-0_xHQfKe0omwv7YLvDIsId3i8QuEb_O2ycuVgkNpxxjMibCmrlMybEqRr2iLSEJJXIwlYJn1dZ1W_OK9I1XardPcCA8jK0lbU4WgvpwK_oO2lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی دو روز قبل یه گونی آدم از مجری‌های صداوسیما ، اعضای پایداری و بعضی ورزشکارها در واکنش به کارزاری که راه افتاده بود، پا شدن رفتن جنوب که بگن ما از جنگ ترسی نداریم و این حرف‌ها؛
حالا کجا رفته باشن خوبه؟
بهمنشیر که تو نزدیکی کویته و 14 ساعت [1125 کیلومتر] با بندرعباس فاصله داره
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68781" target="_blank">📅 10:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68780">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=NEQpPuRyROIRDqFKBpA5vexIbrj5xE51Xj3c0OQtTzEe_4zA9ACqa7QIboNRQWaV7gvuSPn99d5I-FJ5UDZnIVN1IDtyfnowKdnH4LV-ecpOVJc7_2zJj585yIjPSr-0_xnt7AHsY4bt3lSfXu7zYNgZJ-l6IoLLH7m9zwET1pdYPHpL0JlseZ5LRlyRbQoQxkzcwryvynB9rh6p1Se-6WoP-udEZecrmyzIKSXbdgIQD86Pi_iwxxzy_bUvuToIopUJPjQ3AbxgN0SwoEsVihjpMhhUoA4yQwayiZlja4sLfLYB9Z60_wl8djRd05uvYEwdYSvsK1v4TaQCuey7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=NEQpPuRyROIRDqFKBpA5vexIbrj5xE51Xj3c0OQtTzEe_4zA9ACqa7QIboNRQWaV7gvuSPn99d5I-FJ5UDZnIVN1IDtyfnowKdnH4LV-ecpOVJc7_2zJj585yIjPSr-0_xnt7AHsY4bt3lSfXu7zYNgZJ-l6IoLLH7m9zwET1pdYPHpL0JlseZ5LRlyRbQoQxkzcwryvynB9rh6p1Se-6WoP-udEZecrmyzIKSXbdgIQD86Pi_iwxxzy_bUvuToIopUJPjQ3AbxgN0SwoEsVihjpMhhUoA4yQwayiZlja4sLfLYB9Z60_wl8djRd05uvYEwdYSvsK1v4TaQCuey7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
لحظه‌ای که عادل فردوسی‌پور تو لایو فوتبال 360 بغض و گریه کرد...
اپلیکیشن‌ و سایت فوتبال 360 به علت اینکه عادل و مهمون‌هاش از تیم ملی انتقاد کرده بودن، به درخواست قلعه نویی و باندش فیلتر و از دسترس خارج شده و مجبور شدن برنامه رو تو لایو اینستاگرام و یوتیوب اجرا کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68780" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68779">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=EpORvx-rrjd7wokvXMre2SUfMAFJh_4WdHCZVR6GqmRTlopdAinR8ODz_wFxcwAsUXjEJHVWClNp4uilhcYE2j_I-fyJIpk8ZbYOtdKyPXZTxyfAP3tl8G2kDj1_C2C_qOYuxihvWskm-et9IA46SmvwIX3q9iv1TTycrL0e1oQw5z5ZW6WD0S0cAaA0__d56AqXpfPMST7L9YkJlzIhTXu9HwMe22DnJGoPjxfEkg8NjAf-G24mA-UCkzq2yYn11Y_FbNJsXIwxtR4l8W2m06vdcVKd3WgtWeWnfVoE1YaiYnSRXw7uRo-SSXPCCAAzsVrp5c809cBbKltGjgwJzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=EpORvx-rrjd7wokvXMre2SUfMAFJh_4WdHCZVR6GqmRTlopdAinR8ODz_wFxcwAsUXjEJHVWClNp4uilhcYE2j_I-fyJIpk8ZbYOtdKyPXZTxyfAP3tl8G2kDj1_C2C_qOYuxihvWskm-et9IA46SmvwIX3q9iv1TTycrL0e1oQw5z5ZW6WD0S0cAaA0__d56AqXpfPMST7L9YkJlzIhTXu9HwMe22DnJGoPjxfEkg8NjAf-G24mA-UCkzq2yYn11Y_FbNJsXIwxtR4l8W2m06vdcVKd3WgtWeWnfVoE1YaiYnSRXw7uRo-SSXPCCAAzsVrp5c809cBbKltGjgwJzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
نظر مارکو روبیو درباره برجام (سپتامبر 2015)
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68779" target="_blank">📅 09:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68778">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
سنتکام: حملات امشب به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68778" target="_blank">📅 04:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68777">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68777" target="_blank">📅 03:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68775">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=enVPpx-2CS1n-fqF53bceSnTI8LBn0yR0FGoYBJhOAnRay9faRGMstspMddV9W6o_HajEB6z6EJpAX7ysFL_oz0980hKb9yjz66HNxq0PXUsBqG9THrOLEXxh3XhDCZAb_Vx3wuvG9mmHFItlt3Y2ILYZoy04K1lXXKOcaCw6tKS-xyL4M_JcwlRNztMN2OScxa3AQ8PTZRtibc-Lr-wM_OUut3Kao0TkPjU0ntSs5-feJx-GMWRPy1xCirAwIDhn--05bIRCpitWXyLSFK1ZLqQQVMDBeuNlBg5Mw63Uvu2eqZmlqWC9Iti-QKSWr_-9aLBTgE2MK-vArC9XpeKww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=enVPpx-2CS1n-fqF53bceSnTI8LBn0yR0FGoYBJhOAnRay9faRGMstspMddV9W6o_HajEB6z6EJpAX7ysFL_oz0980hKb9yjz66HNxq0PXUsBqG9THrOLEXxh3XhDCZAb_Vx3wuvG9mmHFItlt3Y2ILYZoy04K1lXXKOcaCw6tKS-xyL4M_JcwlRNztMN2OScxa3AQ8PTZRtibc-Lr-wM_OUut3Kao0TkPjU0ntSs5-feJx-GMWRPy1xCirAwIDhn--05bIRCpitWXyLSFK1ZLqQQVMDBeuNlBg5Mw63Uvu2eqZmlqWC9Iti-QKSWr_-9aLBTgE2MK-vArC9XpeKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68775" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68774">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
❌
🌐
امشب ریزپرنده ها در تهران فعالیت داشتند، احتمال اختلالِ بیشتر در اینترنت وجود داره؛ پروکسی های پرسرعت زیر رو داشته باشید
https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68774" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68773">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در زنجان!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68773" target="_blank">📅 03:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68772">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2wyOMX5Fj9vKHGwShlzBKlpB-rkNcfbx0UvR6N-grcYe57EQMJyhF2AGiDbQvR2ScqKYRHFj_vcf3soKPI4Mujd4L2V6P8AarRS4faZpoUD8NCacSv5JzZSEieZ9qNWa0JXSVUYhzXMpcNYMBCZDWHizNDGlnvTzlRTTGmi1oXD6wtq1rKdODWN-y2XYCafmBfkKCyoEY3OKpHqTBF-HyLdTeoaWy9_s5xUdaktg0riOiAosf-Rr9YFq4EPYTLNzRDsOSOI0Xr_YIBp3FDpq9zjXwz7UjgOnbYwAZb1xbgcs11nwTYEVwyBVjjHaoLlex__30ZXAlMUe91f8eqq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68772" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68771">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت پدافند شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68771" target="_blank">📅 03:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68770">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون حملات شدید آمریکا به</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68770" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68769">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68769" target="_blank">📅 02:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68768">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تا این لحظه سنتکام هیچ خبری مبنی بر آغاز حملات رو اعلام نکرده! #hjAly‌</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68768" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68767">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بابت گزارش های لحظه‌ایتون عمیقاً سپاسگزارم، ولی حتما سعی کنید بعدش چنین گزارش هایی رو پاک کنید خدای‌نکرده جایی تو بازرسی گوشی توسط مزدوران ج.ا، مشکلی پیش نیاد
❤️
#hjAly‌
‌</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68767" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68766">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
هشت انفجار در تبریز  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68766" target="_blank">📅 02:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68765">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68765" target="_blank">📅 02:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68764">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه #hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68764" target="_blank">📅 02:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68763">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68763" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68762">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68762" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68761">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68761" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68760">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان  @News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68760" target="_blank">📅 02:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68759">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68759" target="_blank">📅 02:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68758">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در نارمک!!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68758" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68757">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68757" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68756">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGG_K7ZDACLEBeKd3Q7jooTVc-RhhJq9jGU9_BJz4x2aBjQ_jrMmyJWlYCZGIlaU_IWjc0tHiZ6X37OZzXp9FgVj0aYU9Bpa9QJbhCpcoCdP6tmUXaLBGAx22tHJj12CH__YYo7lEdSiXPc5_lQS6EyPFf6_speEQyd8068p9sFPJYLxzY5dP4PcTkWVz-Xl1O1Qf8y1k7aFD6woe7jRZy2BrovhEwzF42xQt0BJLqm5EcN_BZSMR9gmF_aHM5PwrF5hLDsQ0iZsxBEYQudZ7myktRTDmjohRFZhnQONkOLw7QZLmPwREoD1uVapTVu8KbZiNmTuXBaWCLzT99t04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68756" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68755">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=WlTl_tMwu1IvNdlp5B5CIF3b0rS3_ByriTFLCsHZLJfE80fu32sWr5BLv_KqMy4OJKAXp6almIsQVV93Xx-MTmynbYnFy-YlAMA63Xaw5s1u9Yla2SFts6t-dq0XAtaa4PMlI16D9nt1UXt0fM9xesv5iAjsXaxuxaGSgLlGWFJTCJga79YCBdIfWURDeitYuG1xi8qFRP95PQ7d86vDCeYDds4ss2ZieZD2PV22dhLrYf0G1W7yCS_1h3XNQWAS8HOeM9emfKBcqJ2PWXr85B9MKnw5kJWj7QDFlg509LJH1gOIZ3f01rlmVec10m-KLqm8QXY6RSxu0W1HxLPqRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=WlTl_tMwu1IvNdlp5B5CIF3b0rS3_ByriTFLCsHZLJfE80fu32sWr5BLv_KqMy4OJKAXp6almIsQVV93Xx-MTmynbYnFy-YlAMA63Xaw5s1u9Yla2SFts6t-dq0XAtaa4PMlI16D9nt1UXt0fM9xesv5iAjsXaxuxaGSgLlGWFJTCJga79YCBdIfWURDeitYuG1xi8qFRP95PQ7d86vDCeYDds4ss2ZieZD2PV22dhLrYf0G1W7yCS_1h3XNQWAS8HOeM9emfKBcqJ2PWXr85B9MKnw5kJWj7QDFlg509LJH1gOIZ3f01rlmVec10m-KLqm8QXY6RSxu0W1HxLPqRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
پهباد‌های انتحاری در آسمان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68755" target="_blank">📅 01:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68754">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
جمهوری اسلامی به کویت حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68754" target="_blank">📅 01:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68753">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=aa4_zmLXRVUzhO8QDlIZJ--t1CIBM1a6pxwWd_2oS67GrWkm4w5VW3r2L_DJco-_-CzITXdXXpkiSMVHPsBAZIH6z921iwROePjI1KGmeBxD9e45qOKknq6uFysvTD-ae9YDLumTXOJR0dMu-DQGLfU-NXZsNwVhgNwtfZETbmWqUYLBqOlDkdFAv_KLC0Wrp2O4SV5JAUIfY6Ml7piva-CpDA28G1yz9gHui6Fa6ZVpTtYhGP6ghCznOpDRVD4wsdZY2hBDFOopKMZDnyXn08TNUhLbAcYEB6ztxK3n22XHtLrdNtHGdl7zYUatN7mTJBA-rc1QMUjhyrxXjuhvbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=aa4_zmLXRVUzhO8QDlIZJ--t1CIBM1a6pxwWd_2oS67GrWkm4w5VW3r2L_DJco-_-CzITXdXXpkiSMVHPsBAZIH6z921iwROePjI1KGmeBxD9e45qOKknq6uFysvTD-ae9YDLumTXOJR0dMu-DQGLfU-NXZsNwVhgNwtfZETbmWqUYLBqOlDkdFAv_KLC0Wrp2O4SV5JAUIfY6Ml7piva-CpDA28G1yz9gHui6Fa6ZVpTtYhGP6ghCznOpDRVD4wsdZY2hBDFOopKMZDnyXn08TNUhLbAcYEB6ztxK3n22XHtLrdNtHGdl7zYUatN7mTJBA-rc1QMUjhyrxXjuhvbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست وزیر جنگ آمریکا:
«رئیس‌جمهور ترامپ گفت که ما دوباره درگیر جنگ‌های احمقانه‌ای مانند [عراق و افغانستان] نمی‌شویم، و او این کار را نکرده است.
به همین دلیل است که ما سعی نکرده‌ایم جامعه ایران را از نو بسازیم، بلکه صرفاً، به شیوه‌ای واقع‌گرایانه و با شعار «اول آمریکا»، اطمینان حاصل کنیم که آنها هرگز به بمب هسته‌ای راه پیدا نمی‌کنند - کاملاً متوقف می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68753" target="_blank">📅 01:05 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
