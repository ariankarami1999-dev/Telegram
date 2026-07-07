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
<img src="https://cdn4.telesco.pe/file/M6Ie8xSixTc1Aw5onol_Ny4Z6LVAEz6I9lsFxDZW1crsh6AIbX2GeYg89_7fUnrEH4d4IxftbhAVwj8w6QxW8TMVhwiIzyMbsEr06YSKMGkEfqBOe3OzO_xzBlHHFxxbzh67hZB_BzsdAvYRGnxV9AAqa0shOW40QcSmz0Mp1fPK6iRyX09ctWIXIx0W_wkFlV_YIeIFZ9QysLDwBIhSxAmMI5yRE2HzeE6Ir7swtADjiFbvywEfk1twvbybh8ukKTyQm0X8cB6fW-KCOeE6Ap6dgeu1RMfbVj8hUF-gY7w_RgV0_jokmfsm5LhEkFtFCRkR1547hEOU4NV1HqsWFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 926K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 14:39:20</div>
<hr>

<div class="tg-post" id="msg-132217">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزارت خارجه سعودی حمله تروریستی به دمشق را به‌شدت محکوم کرد و بار دیگر مخالفت کامل خود با هرگونه اقدامی که امنیت و ثبات سوریه را هدف قرار دهد، اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/132217" target="_blank">📅 14:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132216">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزیر خارجه آلمان: ایران باید آزادی تردد کشتی‌ها در تنگه هرمز را تضمین کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/132216" target="_blank">📅 14:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132215">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
عربستان سعودی در حال مذاکره برای ایجاد کریدورهای جایگزین حمل‌ونقل نفت از هرمز
🔴
خبرگزاری رویترز: عربستان سعودی برای ایجاد کریدورهای جایگزین حمل‌ونقل نفت، وارد مذاکرات اولیه با همسایگان منطقه‌ای شده است و عملاً به دنبال کاهش وابستگی پادشاهی به تنگه هرمز است.
🔴
این مذاکرات در مراحل اولیه با هدف دور زدن این گلوگاه استراتژیک که در طول جنگ آمریکا و اسرائیل علیه ایران با محاصره دریایی و حملات دریایی مواجه بوده است، انجام می‌شود.
🔴
پروژه زیرساختی پیشنهادی به گونه‌ای طراحی شده است که یک گذرگاه امن برای صادرات انرژی خلیج فارس فراهم کند و تضمین کند که جریان‌های حیاتی نفت از نوسانات مداوم منطقه‌ای مصون می‌مانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/132215" target="_blank">📅 14:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132214">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e076c481d.mp4?token=dCuQoriKNslEcJv6U1DEwkdHPEohce9ODS9c_f3eeS1jPNi_QXItnhcCax1NUsU1PCBVBbj7LITJzUFrXdqS-qD2So65k4ZQN6NLYWDCRitGsnE6xja53AQiNziKRRm587ZwkQsdj1-0QJgB9Xv-tvBpHK9T1k28Socq0gXyEKa4UeNTt1F74G5wv7DoA6itRMIDdmUT1Bsl6lOneN9oiAmyVpnm9OCFZOrrGTdr5JJQYhz5pX_L5KBvqHfUV4D1AhMZGGHHwK4rfqbc2IP3cBFZv8H3igrYNydPA19-BgVgxjD4OoV0bxsDA-tKAjvH7m2MkNLFoCHK77gos__dH52HtAGPfKEeZt-VgmzOQGM-s5UZGM8CdoA5VMwywdr9rio1TVAjx4Rj4fJaeIPAD3LkN_XOkn7pv9IP0Hy5uRC_o2Hh6k0oFcyaEF54fsaQFiO2o5E_DYJ5T-fHn3AB6h_qEVW7fSOMCRG3KY_PyhN6YeiyQ14-fgdydPOtcj9Dz5PnJfH0Y-bR0oUTlqc6164JUMggs8oBJgiFzCKSgjAr7LfdFAFSi1YP-yC-aNAsbi7zvbjj82_wFBPDPSIVT9HVj_9VQVs7JRwl3lrlZSElxp3TU32BxqPnIahOMRznZ87ubz5yOqx-HMYnHUQLfA4vf5JKGrGYEjsWT7ISjm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e076c481d.mp4?token=dCuQoriKNslEcJv6U1DEwkdHPEohce9ODS9c_f3eeS1jPNi_QXItnhcCax1NUsU1PCBVBbj7LITJzUFrXdqS-qD2So65k4ZQN6NLYWDCRitGsnE6xja53AQiNziKRRm587ZwkQsdj1-0QJgB9Xv-tvBpHK9T1k28Socq0gXyEKa4UeNTt1F74G5wv7DoA6itRMIDdmUT1Bsl6lOneN9oiAmyVpnm9OCFZOrrGTdr5JJQYhz5pX_L5KBvqHfUV4D1AhMZGGHHwK4rfqbc2IP3cBFZv8H3igrYNydPA19-BgVgxjD4OoV0bxsDA-tKAjvH7m2MkNLFoCHK77gos__dH52HtAGPfKEeZt-VgmzOQGM-s5UZGM8CdoA5VMwywdr9rio1TVAjx4Rj4fJaeIPAD3LkN_XOkn7pv9IP0Hy5uRC_o2Hh6k0oFcyaEF54fsaQFiO2o5E_DYJ5T-fHn3AB6h_qEVW7fSOMCRG3KY_PyhN6YeiyQ14-fgdydPOtcj9Dz5PnJfH0Y-bR0oUTlqc6164JUMggs8oBJgiFzCKSgjAr7LfdFAFSi1YP-yC-aNAsbi7zvbjj82_wFBPDPSIVT9HVj_9VQVs7JRwl3lrlZSElxp3TU32BxqPnIahOMRznZ87ubz5yOqx-HMYnHUQLfA4vf5JKGrGYEjsWT7ISjm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین دیشب به ۸ نفتکشِ تحت تحریمِ متعلق به «ناوگان سایه» روسیه در دریای آزوف حمله کرد
🔴
این بخشی از فشار اوکراین به بخش انرژی روسیه‌ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/132214" target="_blank">📅 14:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132213">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc22eef9fd.mp4?token=qnoWHhU_KQFOS4bUKj8m5_9MFITVUIKa--ZB00lhHtT2SUS_nCJM58thZJRNkfpfudCwxuM78oqUQkI3DqcPxu7sb_lDmNPD6N0G6Msoz2ewOdR_cNSXVD-2F6edRPio7gR3nhsIv6Gl0GzLyIbw4BdhCAZh_QwIY8FCXvBWGTHn5w3hFmy3yQ84PbJrUaSXKNlP6I1ZphbwHJmW2rCXI1LIsLFwcsxmsxMJhduWwwd7tpF1fmZMghoZBHq7oOIRyRn6BMcs8nAE0C013mYQwhZoA9nNcoBdclUuQY0xADr7BDGum6YefPxk6-vLQoYzqpyP9_hs8_JLjHieOUJJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc22eef9fd.mp4?token=qnoWHhU_KQFOS4bUKj8m5_9MFITVUIKa--ZB00lhHtT2SUS_nCJM58thZJRNkfpfudCwxuM78oqUQkI3DqcPxu7sb_lDmNPD6N0G6Msoz2ewOdR_cNSXVD-2F6edRPio7gR3nhsIv6Gl0GzLyIbw4BdhCAZh_QwIY8FCXvBWGTHn5w3hFmy3yQ84PbJrUaSXKNlP6I1ZphbwHJmW2rCXI1LIsLFwcsxmsxMJhduWwwd7tpF1fmZMghoZBHq7oOIRyRn6BMcs8nAE0C013mYQwhZoA9nNcoBdclUuQY0xADr7BDGum6YefPxk6-vLQoYzqpyP9_hs8_JLjHieOUJJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به آنکارا، ترکیه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/132213" target="_blank">📅 14:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132212">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
شریعتمداری: سر ترامپ را می خواهیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/132212" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132211">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
تعطیلی ادارات سیستان و بلوچستان در روز چهارشنبه 17 تیرماه
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/132211" target="_blank">📅 13:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132210">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مازندران فردا تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/132210" target="_blank">📅 13:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132209">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزیر خارجه آلمان : حزب‌الله ریشه همه مشکلات لبنانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/132209" target="_blank">📅 13:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132208">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مدیرکل فرودگاه‌های استان بوشهرگفت: فرودگاه بوشهر پس از نزدیک به چهار ماه وقفه، فعالیت خود را از روز شنبه ۲۰ تیرماه با برقراری پرواز در مسیر تهران - بوشهر و بالعکس از سر می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/132208" target="_blank">📅 13:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132207">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
مکرون، رئیس جمهور فرانسه :
اتفاقات تنگه هرمز باعث شده
🔴
فرصت خوبی برای پیدا کردن و استفاده از مسیرهای جایگزین به وجود بیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/alonews/132207" target="_blank">📅 13:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132206">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ایتامار بن‌گویر، وزیر امنیت ملی اسرائیل، درباره فعالان شرکت‌کننده در کاروان‌های امدادی به غزه: آن‌ها می‌خواستند من ساندویچ به دست آن تروریست‌ها، آن حامیان تروریسم، بدهم و به آن‌ها بگویم که اسرائیل چقدر زیباست. اما این با من تمام می‌شود. من فریب‌کار نیستم.
🔴
من مربا، شکلات، گوشت گوسفند، میز پینگ‌پنگ، تلویزیون و رادیو را از آن‌ها گرفتم.
🔴
قبلاً آن‌ها چاق می‌آمدند؛ امروز چاق می‌آیند و لاغر می‌روند.
🔴
این‌گونه باید تروریست‌ها رفتار کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/alonews/132206" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132205">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrrFUwtf_JfgsXPmkjG6epcrQmkv0MVef_NZr-9VN1isyUJJAKXaM0sgDBHbBm2Dh0WQh5fx51PAUs_cJqCDyZnQnkdjoGmiwQrrEvr7Y02do96W5KPkLFr-jWbM7KPA3U5ju0zhQSZyJMW8yUa80Cwqj_Z6gwAJ2Dq7jbZ4QJhr3SaS4yn47L8H7Muvm56BQfR5P2O4hGK3MyJhzyJkktHVERIpxqZ5OIidjEtKDArza5-7aZx9XN4ZlKLj2Jpeto7_NAoVzcxbIPn9KO9ka35jKnVy1BzF1Vr24psIALWV_8_VZRJeWcmKub3BsjNeu_VxhDnXYyRM0a7BvuN7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از بازیابی کلاهک ۴۵۰ AGM-158 JASSM کیلوگرمی و عمل نکرده موشک کروز هواپایه در استان کردستان منتشر شده است
🔴
این سومین بار است که کلاهک قدرتمند و نفوذ کننده WDU-42/B به صورت کاملاً سالم به دست می‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/132205" target="_blank">📅 13:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132204">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e9c082164.mp4?token=pyeZVG5ffxOJNtGWN23KEd8sE9XRQNczofeWxWl8e38fcCAvUENOfI1H0WeAnF7WdqgexD0sTBha2vhFManuTUouSVQeekreawjPbCmw1MXH5DFKAP4k5PLwTMKLBjh4daZk43kKm4jQRdR2qZuBG1sIWv84kXqnhmpzsi-qr4DkzSDVtJql25IChrR-OhMwxuLbeVtSfGE_itZMMbZog5tpVBE6wjPK1Px_-sFHi1s0HG1amj3mW6zfXn6GdZu-6Y50tjF7QEbq5QwQkVLezP-fqVd9y-HOcORrGpZ4a7dWj4bTVFRqgbT-uOLdZajRJ_1McFryLfIH-S7NiQZ0zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e9c082164.mp4?token=pyeZVG5ffxOJNtGWN23KEd8sE9XRQNczofeWxWl8e38fcCAvUENOfI1H0WeAnF7WdqgexD0sTBha2vhFManuTUouSVQeekreawjPbCmw1MXH5DFKAP4k5PLwTMKLBjh4daZk43kKm4jQRdR2qZuBG1sIWv84kXqnhmpzsi-qr4DkzSDVtJql25IChrR-OhMwxuLbeVtSfGE_itZMMbZog5tpVBE6wjPK1Px_-sFHi1s0HG1amj3mW6zfXn6GdZu-6Y50tjF7QEbq5QwQkVLezP-fqVd9y-HOcORrGpZ4a7dWj4bTVFRqgbT-uOLdZajRJ_1McFryLfIH-S7NiQZ0zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره ای رویترز از مراسم تشییع
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/alonews/132204" target="_blank">📅 13:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132203">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCiFGVeGxOyIB9niAzP8jflLhXzyQh3if0WCkggmrxOPZdz8Uoto2X7-BzMosxuXWaZABkA1n4akqnw5V-6nMrAidMHbfrXQR7Y654rQQEvPNUm3UlbaZvMMitlDjVM3GYhJg9dO6VlqnJEFPW3v8blBXjdVlgjLCViF8JVs-MlDbtdAJwzRuGdLuHSI_Tbp5QOORTFSYr_sGh91YgiZCcuF80NCFLwIgEDIe2o1rprS4P2qROa2e6_LnXY0VPBa7qdQnbEStRvw-e68cuYzPqtLXPPG-TZITZeE8FCuk3yOBdvhGl2AKi6rQv2jLPe7kMb_FlVOY3l1m0bgEmgaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار مکرون و الشرع سران فرانسه و سوریه در کاخ ریاست جمهوری سوریه در دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/132203" target="_blank">📅 13:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132202">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گزارش ها از کندی سرعت اینترنت
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/132202" target="_blank">📅 13:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132201">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
صداوسیما: جزئیات جدید از حادثه برای یک نفتکش در نزدیکی عمان
🔴
به گفته برخی منابع، نفتکش «الرقایات» متعلق به قطر، قصد داشت با حمایت نیروی دریایی آمریکا از مسیر عمانی در تنگۀ هرمز عبور کند، که پس از بی‌توجهی به هشدارهای مکرر، هدف حمله قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/132201" target="_blank">📅 13:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132200">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
به گزارش بلومبرگ، پالایشگاه‌های دولتی هند در حال مذاکره با تاجران نفت خام ایران هستند و در صورت تمدید معافیت‌های آمریکا پس از ماه اوت یا کاهش محدودیت‌ها، برای خرید نفت ایران آماده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/132200" target="_blank">📅 13:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132199">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97ce01c0c.mp4?token=Q6vh1gaHV9RGK-DT6jGN08sjuKb3iYp963beF9500dVyzhcXXk_mm_jK07CaBSna56BjfDhUEqPioMoLOIEdmHjR5rLwMRtRpjeXDytGNuBn68u6K_j0bYCnEOaJRqC3kJrk4CJ0aM0iMiMvs4CQShBvyvhIafv0P0CdbFQksBVQYYKnVgScqXWwG_V4gN1-eh1EqgGok-jgT_Wbj5_eihka1Pwf8wGuR9N-LUKqhBFJYr4PI05tWQrHdC2SZSabXlK_846v9INyn5q2B3sdSxnnHzAepkTp6LT2xbIzOvZBpWdkhZsOJFyXxltQeC-jbdKXDlX5TYZIw-0Oi1gvQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97ce01c0c.mp4?token=Q6vh1gaHV9RGK-DT6jGN08sjuKb3iYp963beF9500dVyzhcXXk_mm_jK07CaBSna56BjfDhUEqPioMoLOIEdmHjR5rLwMRtRpjeXDytGNuBn68u6K_j0bYCnEOaJRqC3kJrk4CJ0aM0iMiMvs4CQShBvyvhIafv0P0CdbFQksBVQYYKnVgScqXWwG_V4gN1-eh1EqgGok-jgT_Wbj5_eihka1Pwf8wGuR9N-LUKqhBFJYr4PI05tWQrHdC2SZSabXlK_846v9INyn5q2B3sdSxnnHzAepkTp6LT2xbIzOvZBpWdkhZsOJFyXxltQeC-jbdKXDlX5TYZIw-0Oi1gvQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تپه علی الطاهر در جنوب لبنان توسط ارتش اسرائیل فتح شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/132199" target="_blank">📅 13:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132198">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
گلستان فردا چهارشنبه تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/132198" target="_blank">📅 13:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132197">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
صداوسیما : نفتکش هدف‌گرفته‌شده در تنگه هرمز پس از نادیده گرفتن هشدارهای مکرر مورد اصابت قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/alonews/132197" target="_blank">📅 12:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132196">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وال استریت ژورنال: قیمت نفت افزایش یافت و معاملات آتی سهام در ایالات متحده کاهش پیدا کرد، پس از آنکه دو کشتی تجاری در نزدیکی تنگه هرمز مورد حمله قرار گرفتند، که این امر نگرانی‌ها را در مورد امنیت منطقه دوباره برانگیخت.
🔴
قیمت نفت برنت از مرز ۷۳ دلار به ازای هر بشکه عبور کرد، در حالی که قیمت نفت وای‌تی‌آی به حدود ۷۰ دلار نزدیک شد. با وجود واکنش فوری بازار، تحلیلگران گفتند که افزایش تولید اوپک پلاس و احیای صادرات
نفت خلیج فارس، انتظار می‌رود از افزایش طولانی‌مدت قیمت‌ها جلوگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/132196" target="_blank">📅 12:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132195">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
یک روزنامه پاکستانی: دور سوم مذاکرات ایران و آمریکا؛ احتمالا ۲۳ و ۲۴ تیر در اسلام آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/132195" target="_blank">📅 12:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132194">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / مقام ارشد آمریکایی به آکسیوس:
ایالات متحده با حملاتی علیه اهداف ایرانی،
انتقام حمله به نفتکش ها در تنگه هرمز را خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/132194" target="_blank">📅 12:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132193">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUCYE3VFojE1N6Abe2vdnyz6_apUZfjI4Bk0grgW4t4sJdHh6O-K2viKjWaKTZZ0uZHhSw-YTaQcuCzDOyy8lVfMYT1hpqK885JrUfYoLh5RP5zc125vbAtmHBi83dAjYQJT-shHITvKD2wSnrLpx4n12psFA4ZApnOCIvRbOw96kIK3k0fJ2nyqhfBmTCYj1PG40_EKqF8ljiY6ofJTVJ7HK2bF94jPQDmIUcZSa2IkdC8HImQaxrs-LdecL31K_cUynlP9GeP3OTUEAT5Ax5wbUtFbk2jRhZr616FSmDeaNAfK_l-dT2xyWzXpSnEXTgbqtothJxhaZc1Bz5R_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش سناتور لیندسی گراهام به تصویری از او در تهران که با تفنگ هدف گرفته شده است: «حداقل از یک عکس خوبِ من استفاده کرده‌اند.
🔴
دشمنانم بهترین معیار برای قضاوت درباره من هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/132193" target="_blank">📅 12:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132192">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پیت هگزث وزیر جنگ آمریکا یک دفتر جدید برای پهپادها در پنتاگون تأسیس می‌کند که در همه زمینه‌ها ، از پهپادهای تهاجمی انتحاری ، تا ربات‌ها و قایق‌های خودرو های  زمینی ، اختیار تام خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/132192" target="_blank">📅 12:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132191">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c677b2d00.mp4?token=BLwfA7u0EbFFHxdtByc335fVsRIz267lRaJmPqBp7vzbVXRezhyR5SJRB-7o7OstNBNOTWNgEYfyKgwXF5sGHhVA4BiZGcDPY6IIpVvZjxiVeMgUisV6HBtclC_BtcM2iVjX2OqiLC4v6D-ch_Oyteisa_8vfIg07H9jkXCPXDV8YMqd5kA-rLgoxJNbXRHWs0k2SFCQ72NTNCxindW4uvlGLgXQUVTGG9L627RF3QtIWYpOXWMf74NY845EdvAcYLEHfvQRNGPZkqlSTPgSAD6QMuQ_B2NHP1zFsYoNwg1P-NHEsIDGatu7rbMQPpc3MZTy4_uc39Ez0b3tkRYazA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c677b2d00.mp4?token=BLwfA7u0EbFFHxdtByc335fVsRIz267lRaJmPqBp7vzbVXRezhyR5SJRB-7o7OstNBNOTWNgEYfyKgwXF5sGHhVA4BiZGcDPY6IIpVvZjxiVeMgUisV6HBtclC_BtcM2iVjX2OqiLC4v6D-ch_Oyteisa_8vfIg07H9jkXCPXDV8YMqd5kA-rLgoxJNbXRHWs0k2SFCQ72NTNCxindW4uvlGLgXQUVTGG9L627RF3QtIWYpOXWMf74NY845EdvAcYLEHfvQRNGPZkqlSTPgSAD6QMuQ_B2NHP1zFsYoNwg1P-NHEsIDGatu7rbMQPpc3MZTy4_uc39Ez0b3tkRYazA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه وقوع انفجار دمشق در نزدیکی محل اقامت ماکرون رئیس‌جمهور فرانسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/132191" target="_blank">📅 12:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132190">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
تلویزیون سوریه: در پی انفجارهای دمشق، ۴ نفر از نیروهای پلیس زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/132190" target="_blank">📅 12:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132189">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL1kua0qsWlqkqlmTsMABgBdFyrJCV4jLsEYQkqwRLSPIia7S66NOB-RBalQdvqNP-Jz-E8OxlNIMln2Gb84AMk3nLhEXZHlMr_jcXDcbvyjEgd40cy-nGTDhjOb-vWvOMoAmGn5U6GFiMm2bt4jQRPuEF_NT8f2jzlCXw6DDMB-lK0fIzT9U-ohZnI_Mg53q85ReskaJyfDtNEJz7G6UZxrH2ps8qhbMIVb5W7RrlTilWz79DN-i4xE0XpqsNpi_PP5v4jWP6ThvQ1buwKrPdKsxeY_odv2xZesUZHmLbTPMQARGXjUt3Ise_eE8b-hmcGA1abeRstvI_6iI2N2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
پیشنهاد من اینه بازی با بلژیک مجدد برگزار شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/132189" target="_blank">📅 12:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132188">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
افزایش قیمت گاز پس از حمله به یک شناور در تنگه هرمز
🔴
قیمت گاز طبیعی و نفت اروپا پس از گزارش‌هایی مبنی بر حمله به یک کشتی حمل‌کننده ال‌ان‌جی (گاز طبیعی مایع) در نزدیکی سواحل عمان و هنگام خروج از تنگه هرمز، افزایش یافت.
🔴
قیمت گاز طبیعی معیار اروپا بیش از ۴.۵ درصد افزایش یافت و تا ساعت ۰۷:۰۵ به وقت گرینویچ به ۴۶ یورو (۵۲.۵ دلار) در هر مگاوات ساعت رسید و زیان‌های جلسه قبل را جبران کرد.
🔴
قیمت نفت نیز صعودی شد و نفت خام برنت، شاخص بین‌المللی، ۱.۲ درصد افزایش یافت و به حدود ۷۳ دلار در هر بشکه رسید که بالاترین سطح خود در یک هفته اخیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/132188" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132187">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
انفجارهای مرگبار در دمشق ۴ کشته و ۱۸ زخمی بجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/132187" target="_blank">📅 12:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132186">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
دبیرکل ناتو: اروپایی‌ها شروع به جبران آنچه آمریکا دیگر قادر به تعهد به آن نیست، کرده‌اند
🔴
بهتر است اعضای ناتو انتظارات واقع‌بینانه‌ای در مورد چیزی که واشنگتن واقعاً می‌تواند تضمین کند، داشته باشند
🔴
وال استریت ژورنال به نقل از مقامات: جبران از دست دادن قابلیت‌های سوخت‌گیری هوایی ایالات متحده آسان نیست، زیرا مستلزم ساخت فرودگاه‌های مجهز بیشتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/132186" target="_blank">📅 12:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132185">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سرویس امنیت فدرال روسیه اعلام کرد، هشت عضو یک هسته مخفی وابسته به یک گروه تروریستی بین‌المللی در جمهوری کاباردینو-بالکاریا بازداشت شدند.
🔴
به گفته این نهاد، اعضای این گروه قصد داشتند به ساختمان‌های نهادهای انتظامی‌در کاباردینو-بالکاریا حمله کنند تا با تصاحب سلاح، به فعالیت‌های مخفیانه بپردازند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/alonews/132185" target="_blank">📅 12:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132184">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
خوش‌چشم در ارتباط با خبر خروج سوخت رسان های آمریکایی طی چند روز گذشته: این گام بعدی آغاز جنگ سوم است، با لالایی دشمن خوابتان نبرد!
🔴
دشمن در حال افزایش ظرفیت و استعداد نیروی دریایی خود، هم برای اقدام نظامی و هم برای محاصره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/132184" target="_blank">📅 12:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132183">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
شاخص کل بورس تهران با رشد ۱۲۲ هزار واحدی در معاملات امروز برای نخستین بار در تاریخ معاملات بازار سهام وارد کانال ۵.۳ میلیون واحدی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/132183" target="_blank">📅 12:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132182">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
دریافت کارت ورود به جلسه امتحانات نهایی ۱۴۰۵ از امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/132182" target="_blank">📅 11:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132181">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f388689de.mp4?token=q9d4qF23TTtKXEQe4e1BotJ474u59UviTTJEJoEhOd6v1m1Y6IG5QiJ_-eziDZ3hLSfrWdyxoRy4idIHtfCMih41HwJhbiECBJhy9rr6rDOMA2lPf8tGzpxC2A_yYfPCGF10b5djyC74J593GO3xBMXLKgkaKozC2lKh0mvJSW7Tbisr_Ui5hHVIqwomGnVwR_N0bvgxuSUJVnEMIL5daC-TEjoRPOSZSN8Jjh9XqG4v6QQ35zHTG5fq1fQxVDib2Xk4TuffZnF9j-u-naav_NOc_Bi8fnVSYF62Nazm-KeUxJtBZlwlWD1OIA4jdcTVqBviu4_FxJ0tJoaJdFT2fYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f388689de.mp4?token=q9d4qF23TTtKXEQe4e1BotJ474u59UviTTJEJoEhOd6v1m1Y6IG5QiJ_-eziDZ3hLSfrWdyxoRy4idIHtfCMih41HwJhbiECBJhy9rr6rDOMA2lPf8tGzpxC2A_yYfPCGF10b5djyC74J593GO3xBMXLKgkaKozC2lKh0mvJSW7Tbisr_Ui5hHVIqwomGnVwR_N0bvgxuSUJVnEMIL5daC-TEjoRPOSZSN8Jjh9XqG4v6QQ35zHTG5fq1fQxVDib2Xk4TuffZnF9j-u-naav_NOc_Bi8fnVSYF62Nazm-KeUxJtBZlwlWD1OIA4jdcTVqBviu4_FxJ0tJoaJdFT2fYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ناتو در 5 سال آینده 40 میلیارد دلار در زمینه قابلیت های ضد پهپادی سرمایه گزاری خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/132181" target="_blank">📅 11:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132180">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d9e55bd435.mp4?token=jlen8wwMIURiapqoCgO6XrRM7UeEGnTRNV6YeWiiVk7iNWIg1RzjS1zWjzD50B5oa1XxODknrWX7KvIapOJ-jZBwLmhurhGlWphwQEkH7pNVei6af260OsaDfwtp2A2Ko7PIjZEEyKNrLo0ypAJNoTlQx4b1G8aULI7g_rDUjamfeXoCYuRWGJLl_W8MsrNSzr6NZCN45zTEOGH6BaYpf-ly9V_uMD3cykGivjVocsq1jgughnkMbzRx931STcUIx_YSgGnQ1Ja8dZRL8kFV1Vgbg67Stoz9fMVCR5pDItb280wvXLaogup7DhltbkWVtUtUua3_tAdtzvkse4GVfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d9e55bd435.mp4?token=jlen8wwMIURiapqoCgO6XrRM7UeEGnTRNV6YeWiiVk7iNWIg1RzjS1zWjzD50B5oa1XxODknrWX7KvIapOJ-jZBwLmhurhGlWphwQEkH7pNVei6af260OsaDfwtp2A2Ko7PIjZEEyKNrLo0ypAJNoTlQx4b1G8aULI7g_rDUjamfeXoCYuRWGJLl_W8MsrNSzr6NZCN45zTEOGH6BaYpf-ly9V_uMD3cykGivjVocsq1jgughnkMbzRx931STcUIx_YSgGnQ1Ja8dZRL8kFV1Vgbg67Stoz9fMVCR5pDItb280wvXLaogup7DhltbkWVtUtUua3_tAdtzvkse4GVfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انفجار یک بمب دیگر در دمشق دقایقی پیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/132180" target="_blank">📅 11:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132179">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
بورس انرژی: فردا بنزین سوپر در رینگ داخلی به قیمت هر لیتر ۸۴ هزار و ۶۰۰ تومان عرضه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/132179" target="_blank">📅 11:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132178">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
کاخ الیزه اعلام کرد ماکرون در مسیر رفتن به دیدار با جولانی، رئیس موقت دولت سوریه در قصر الشعب دمشق بود و هیچ صدای انفجاری نشنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132178" target="_blank">📅 11:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132176">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwNRcRI2xZGh5M7PkhvqDWL7PTrTNb9Asm0_PDSAnc1JoLzgd335pG-yaDPJhduquyIzVU0XVDhyex3Ua4J-2EZeeKQyGt1iJqI9R4V9eS4iqtYcJE98z-I13lsTnIr0WBMYgFXyBQouOH5o7hUKYxq0RIQVHA0T33q1A4mokK66GjvZO3yfKVOeDhv7qwE7j_ShHqNjjNEsK1FWmKzTGUTyxi99TePpacb_WgVDXMqear3xmX2blBlJ3acR3QI8qgpX_Si8dwed2A9zpX_E2EXJRquQXBaOM9No1arBvhb74Ycj5pXEO_bxbBYALzsTNLwQHqtPlLkXkaDoNAPY8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKKymkDjYtSSWGp0Xd-UGLArphowzzQDc9zFRHx4V0zIv81jBrSrOUceWngkwgZvt49EBJIhWlEzZb9SZcXIONfHZkJx2ZC_MY7gyo7hxbCprEyr0HnDMVv5zpRTNzdy49GaFbD7Uav6FFXT9YQRKz8ufR7J-oSb_kgI72otP8vi_ctmqnnSaQcXkQF6kXYDmrQGtk1St9p_55c7aPL-ygdRoKdH5sUk0IeB1dXGBuVwLEceEw5q0HLlG04jnoumKfBYQ5mrJySzLDX0rlT0V9klKNvhjN-V0j2PgrucMMPq3zDyt2xtzqSNAeEmzYcZf1bYq_fOnyIL9s9TBtNcbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از قبل و بعد حملات مشترک آمریکا و اسرائیل به پایگاه هشتم شکاری اصفهان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/132176" target="_blank">📅 11:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132173">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0c1ded30.mp4?token=pJC2DYgPGjeC-OpMVv_MGOeeykAx1RpwiMiZXzGoM9vJkJmy5LQDe6Cx_O8u9rxhoLvYDU1ChixGTs1G2eLQ7R9MDgZM-FdNDn96HR6dL_l_jTPF2Jf1Si3knS5fIJU_g_cngl3xbXSPd1jjXFH5kk9C0fZsDxiNXUppXsQufFXQQ90vQNAM6H0mGelbTaZZjrYYQfuSaQ9kzleJbb8D6MWEgaDX2njOU9GES-ZBzu9rIcDNjaErNcj7Afn7CiW08gfBsrBRgEJOZ18f6Rin4L9Whr7ikVJB0JVSNlRMhs9uYDPCm1sV63o8038PW03OeCCPVgPSPewSnXOZ09e7Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0c1ded30.mp4?token=pJC2DYgPGjeC-OpMVv_MGOeeykAx1RpwiMiZXzGoM9vJkJmy5LQDe6Cx_O8u9rxhoLvYDU1ChixGTs1G2eLQ7R9MDgZM-FdNDn96HR6dL_l_jTPF2Jf1Si3knS5fIJU_g_cngl3xbXSPd1jjXFH5kk9C0fZsDxiNXUppXsQufFXQQ90vQNAM6H0mGelbTaZZjrYYQfuSaQ9kzleJbb8D6MWEgaDX2njOU9GES-ZBzu9rIcDNjaErNcj7Afn7CiW08gfBsrBRgEJOZ18f6Rin4L9Whr7ikVJB0JVSNlRMhs9uYDPCm1sV63o8038PW03OeCCPVgPSPewSnXOZ09e7Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار خودرو در نزدیکی هتل محل اقامت ماکرون در دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/alonews/132173" target="_blank">📅 11:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132172">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGozmNsWCD1jWO3aWRYZnKqoIpTn-D8btYIziEs76IZIIQ1tvpeNACulOwt2XmNqgRFfIYvOL1zGu7wQlzd_L599AxmcI8ndBXAbl_fI7OGacHaEf20BtLTGzPc_EEBeJKQ1DISjZTnblrQiPr8q4Nq8Zk8n24CIHxWKWhsJpGFBHJ58XX72oxfVzSJ_p9OTpZ3zXzoM5Ka-oERyEJZd5uwQmLrlkS1fVxAXoRvhz3AJmgYBgyozs-dj6yhili_3eg-upGVnl6rrTuVbR8_x-mMfwj27C7brs58ykTnszlv_uVkNx3r_j1Th_NEQZreNjtXhvTwE9e4V96hrVmDHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش پیج رسمی تیم‌ملی ایران به شکست شب گذشته آمریکا مقابل بلژیک
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/132172" target="_blank">📅 11:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132171">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ولادیمیر سالدو، فرماندار منطقه خرسون اعلام کرد که حمله هوایی گسترده اوکراین به منطقه خرسون دفع شده و ۵۲ پهپاد منهدم شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/132171" target="_blank">📅 11:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132170">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gn3JWAm_wLMHpdd-EDeftkMxAgzDkKc4sgePGVc2nVOf2cMdAERm0ot9W5ofyNRHQ11TiHrrGhMS8KLGyKxCfC64SZl2uxgckzeOmlAt3uQuFonCfnVstIvCF293_fjhFp55yQh91QS3LNTzrYIqouIn4hCA8uyMPCuxVniEuaq8AvYC9d91DlHDzTTbuXl5iIAecf6N0Q4wioi6SbfelNA6PMUWFhBbnyqj8kz-QwaDSldbBzUhDm9E83xJ23UQvkWlSafDxLUm3DiyYp9jE-F29DP76xv2LfmfH6C7d6-aJgKZ4O2JtPDf_Fz58VbCyO4VAMy0Kn2A05yYb_dRFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از انفجار در دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/132170" target="_blank">📅 11:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132169">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری / منابع خبری از شنیده شدن صدای انفجار در دمشق، پایتخت سوریه گزارش می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/132169" target="_blank">📅 11:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132168">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری / منابع خبری از شنیده شدن صدای انفجار در دمشق، پایتخت سوریه گزارش می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/132168" target="_blank">📅 11:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132165">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439ee96d4c.mp4?token=HJgQtawPdYsU139AKGuqOdvZbi5mfdGRoHd5lEffwJXWEQ9VKUii6b84A7zMnVkSNs1lzkdeMB7wgPn6MuJbC6-r0eThHbzJiqjv_l8Kp6N28DuPF3h7DO3WCfkzNPhCjuKvnPNJj7UvDvYLbxHxfp4zBgQhL4bjsYbXqVY1Aei_uzLZa4h2VOBzlol0zhMoZStgIg0rVmrl274VFLxpBYgQlZQa_vz2bo8rrVid2mDDENoDHw_E2XT3gjQTn0l4gSdE5wYhrefUVmDN03o_SzENnGXrAdvDhYUEdnsDI0iNjCz_zlEs6EDBI4EyENj3OD-F0oOBXtQhbH29rW8dQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439ee96d4c.mp4?token=HJgQtawPdYsU139AKGuqOdvZbi5mfdGRoHd5lEffwJXWEQ9VKUii6b84A7zMnVkSNs1lzkdeMB7wgPn6MuJbC6-r0eThHbzJiqjv_l8Kp6N28DuPF3h7DO3WCfkzNPhCjuKvnPNJj7UvDvYLbxHxfp4zBgQhL4bjsYbXqVY1Aei_uzLZa4h2VOBzlol0zhMoZStgIg0rVmrl274VFLxpBYgQlZQa_vz2bo8rrVid2mDDENoDHw_E2XT3gjQTn0l4gSdE5wYhrefUVmDN03o_SzENnGXrAdvDhYUEdnsDI0iNjCz_zlEs6EDBI4EyENj3OD-F0oOBXtQhbH29rW8dQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر هوایی از قم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/132165" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132164">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی: سپاه پاسداران ایران دست‌کم دو موشک به سمت کشتی‌های تجاری که در حال عبور از تنگه هرمز بودند، شلیک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/132164" target="_blank">📅 10:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132163">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سفیر اسرائیل: دور بعدی مذاکرات بین لبنان و اسرائیل، ۲۴ و ۲۵ تیر در سطح سفیران در رم برگزار می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/132163" target="_blank">📅 10:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132162">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJHkfYQtOqoKpaIetWaAa4vGwoR9oxiz04-63g9M1snTjKHSDJgKEuJW-XWVpdcw7s0qpBxehH7SK9BxtbkJDwWzawl7rxEIG_DFIMSN-VTfBkGQSEj2Dwx2jnlJsjBMrmQg1RZDWOEcI9ZY8jjPmw1FkBL0pd2tgfXDiSwjwgNEf4JpgyTR0gA-cfpm-6jlMu_DBo35J0Im9XP4x57umayUpm36Ck534ghdwVniHe6A6z4w47uw03fjuh_ZXljdCsyFblGnO9-visVT-9UlrKNdWMXcZBMUrIvLsClkgUA03byoCvXmzuNgWFnDqU4GUPNToijHV449MnKhEAhxHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مکرون، رئیس جمهور فرانسه و احمد الشرع، رئیس جمهور سوریه در دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132162" target="_blank">📅 10:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132160">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6591abe34e.mp4?token=YB231WNMEWijjl9p83jrhQA-HLR9CmRk6Svr2y-rJ2WKR6v7fhcbOwZq00sU9rE08mIzRIZZNtAwamDh1xR2daqsRU7EmSmLwiHy6Nz7TVujr2Z9nJzHrSZowfMLrF64R7nGDsLQWedU-LwZ3qAnNp_ZAZcou6I_OyXW66sqQGh1uhnqqIV-at4jbqD3IA_ucwCyET2CCoHFIikoxMAa79kizct_hAnoMqOeqJNqOOXbA0FF5hsSjUE66AkM8AOyE7E0EZadTZbCF8hMOUbvPkD3JLzVbTMu2CJOviUpY_nXxHZjfJHxWSa1OE1GJMxzbdwFJUnw7kL5IZXey7RAog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6591abe34e.mp4?token=YB231WNMEWijjl9p83jrhQA-HLR9CmRk6Svr2y-rJ2WKR6v7fhcbOwZq00sU9rE08mIzRIZZNtAwamDh1xR2daqsRU7EmSmLwiHy6Nz7TVujr2Z9nJzHrSZowfMLrF64R7nGDsLQWedU-LwZ3qAnNp_ZAZcou6I_OyXW66sqQGh1uhnqqIV-at4jbqD3IA_ucwCyET2CCoHFIikoxMAa79kizct_hAnoMqOeqJNqOOXbA0FF5hsSjUE66AkM8AOyE7E0EZadTZbCF8hMOUbvPkD3JLzVbTMu2CJOviUpY_nXxHZjfJHxWSa1OE1GJMxzbdwFJUnw7kL5IZXey7RAog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک پمپئو، وزیر خارجه آمریکا در دوره اول ترامپ: حکومت ایران عمداً چهارم جولای (روز استقلال آمریکا) را برای مراسم تشییع آیت‌الله انتخاب کرد تا نفرت خود را از هر آنچه آمریکا نماینده آن است نشان دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/132160" target="_blank">📅 10:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132159">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
خبرگزاری «رویترز» به نقل از منابع: عربستان سعودی در حال بررسی امکان افزایش ظرفیت خط لوله انتقال نفت خام به سمت سواحل غربی در دریای سرخ است.
🔴
عربستان سعودی، مذاکرات اولیه ای را با برخی کشورهای همسایه برای کمک به آنها در انتقال نفت به خارج از تنگه هرمز آغاز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132159" target="_blank">📅 10:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132158">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_Fdla1Qz_EE-aXf6pFHW8p0hA-n21EXyAlTckq-2_E4tTCbu_h3MzvdOE0FZS2JDL9C3DNQmHHTK_PgOP78NwkgPxI3GuVsLr0THdhlfJe7kHAxswq6wZXwfEnbKPslXCV7xlpkVaPVXB4EXhzam4sFo0Iq5CBSDnlrwo-X5zVim-DqKbPVPJpPNIuhxCFrgOt_W_T-86H2lpZkM6W-b-N1jb8ibWr5eDTnJIVA23rOocr3E0Owe8jQiA5tkD-qLwP96x2yditnZ30Vy6pxJoYuXlYzkBY8XiBUFIwPp0YO38QN-Ntdm3nfQZe1ZlJvFPlL4lr0sgMftCrkGavDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلنسکی: بدون سلاح‌های هسته‌ای، شما دیگر عضوی از باشگاهی نیستید که دیگران از حمله به آن باشگاه می‌ترسند!
🔴
در عوض، شما عضوی از باشگاهی می‌شوید که می‌توان به آن حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/132158" target="_blank">📅 10:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132157">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
قیمت طلا در معاملات روز سه‌شنبه بازار جهانی، کاهش یافت و پایین‌تر از رکورد دو هفته اخیر خود معامله شد.
🔴
قیمت هر اونس طلا برای تحویل فوری با ۰.۹ درصد کاهش، به ۴۱۲۶ دلار و ۳۳ سنت رسید. قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه اوت، با ۰.۷ درصد کاهش، به ۴۱۳۷ دلار و ۶۰ سنت رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/132157" target="_blank">📅 10:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132156">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نیویورک تایمز: انتظار می‌رود ترامپ به اردوغان اطلاع دهد که مایل به فروش جنگنده‌های اف-۳۵ به ترکیه است، اگرچه هنوز مشخص نیست چنین معامله‌ای چه زمانی یا چگونه انجام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/132156" target="_blank">📅 10:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132155">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCdoxZ1kw3iN50lYINd9LC3HPqGXnl26_5VBC6Zid7mw4guNH-zzWjzVx52CvQsFo4qFrAstPKmzn7cCcG1Xs1cXLlmO_zGMHBbLyVfoZKG2OV1DWyD4uKEDOSGwlWcfEBrRptmnsmvhH8waeKyhfXoQS0PJLk25zV0ghX1-sNRD1OFJBkFE9-lJWgELFewZrZ2uLDgxAcvt8wtosz7-1ihCT--m2qZIBMgfE0HGooLQbrp60fyFaWAPxRTq1K3Lld_dFMN-jvmBWHpQv9_0dor_6Zm86RRjcRRCL-GrxAZJpZ6NtdI9qXF8Zc0k221FkyiAhEp3I6PdoUDeBX5SuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میدل ایست نیوز: تصاویر ماهواره‌ای نشان می‌دهد ناو هواپیمابر امریکایی «آبراهام لینکلن» از دریای عمان خارج شده و در دریای عرب مستقر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132155" target="_blank">📅 10:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132152">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df8a4cb89.mp4?token=fc4qAbzmDs1F0r2sprSUVdCtPO9ilphrOVTW1XlnCWkKj--mLwLvZ_uYHUE_fZS-FC9eXJeb5bMvwzFe54YQ9KQwYpdh8QpEGARLcBaD3Agu_QkELa1nQqv2u5JN8SkDzDsUD4hClH3tPeCGM6h36pG0sF1fwScIgNM7K_EjZ4Kdgm6pPZb1xQHy_YJspfDw63hZ5ukZalC3L2fMx1s_30KJcE71nQr_mm3XXeCCdvNnL_e5CflE4K8rJXJ-OkOkiX3Z2vqTOxDlZS5i1FPPVAQWAsGogQRVqmI3V2o-kHOdbstZ0LgKaag2s3I0xE5Pb8VPol4YDiOqjGBN7CgzgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df8a4cb89.mp4?token=fc4qAbzmDs1F0r2sprSUVdCtPO9ilphrOVTW1XlnCWkKj--mLwLvZ_uYHUE_fZS-FC9eXJeb5bMvwzFe54YQ9KQwYpdh8QpEGARLcBaD3Agu_QkELa1nQqv2u5JN8SkDzDsUD4hClH3tPeCGM6h36pG0sF1fwScIgNM7K_EjZ4Kdgm6pPZb1xQHy_YJspfDw63hZ5ukZalC3L2fMx1s_30KJcE71nQr_mm3XXeCCdvNnL_e5CflE4K8rJXJ-OkOkiX3Z2vqTOxDlZS5i1FPPVAQWAsGogQRVqmI3V2o-kHOdbstZ0LgKaag2s3I0xE5Pb8VPol4YDiOqjGBN7CgzgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین بوسیله موشک‌های سامانه HIMARS به بخش تولید خطوط لوله اصلی گاز  در بلگورود حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/132152" target="_blank">📅 09:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132151">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSyOx6E0nh42GspToaYe10YFetOa2RCyIo2lcb0mB_nF4nmr4Ywz5yKIWYUu2Ii8pHCsk2MQ5KpSm_CCN696oShexSzDrEUgNF4EhIFAVN1ctzQd5gRjeCf37eaCrUgqaER6gIaoVdJYn2Lr8fK03DlxilB51Y9tgG2NUQqft0ytu04L_s8q4eFGfIpcL5XtoI9iEtvOaRp9JcrR6-gQuFVAjZAFeHqPLKUIn6ARo9OjMRDfJbOM438hpEaMci40xUZh9Cqacp9tue7LFQxMni_HCSOuie7EWIiel0vfTpql3DP6jsdrTvrqieYS3tHqS8NIVHK8zNUaNk5Ritj1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ۹۷ هزار واحدی شاخص بورس بعد از سه روز تعطیلی
🔴
شاخص کل بورس تهران ۹۷ هزار واحد رشد کرد و به سقف کانال ۵.۲ میلیون واحد رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/132151" target="_blank">📅 09:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132150">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
عراقچی: تا زمانی که تهدیدات علیه ایران ادامه داشته باشد، مذاکرات برای دستیابی به توافق نهایی آغاز نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/132150" target="_blank">📅 09:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132148">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
واکنش عراقچی به ادعاهای ترامپ: تا زمانی که تهدید‌ها علیه ایران ادامه داشته باشد، مذاکرات برای دستیابی به توافق نهایی آغاز نخواهد شد
🔴
به امضای خود پایبند باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/132148" target="_blank">📅 09:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132147">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در آنکارا: اگر شما یک جوان هستید که در روسیه زندگی می‌کنید و به فکر پیوستن به این جنگ هستید، دوباره فکر کنید، زیرا احتمالاً شما یکی از ۳۵۰۰۰ نفری خواهید بود که این ماه، ماه آینده یا ماه بعد کشته می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/132147" target="_blank">📅 09:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132146">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ: کنگره باید بودجه ۳۵۰ میلیارد دلاری دفاعی را تصویب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/132146" target="_blank">📅 08:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132145">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
خروج چند واگن قطار باری از ریل در زاهدان
🔴
روابط عمومی راه آهن جمهوری اسلامی ایران در اطلاعیه ای اعلام کرد: بامداد امروز تعدادی از واگن های قطار باری در زاهدان، از خط خارج و موجب مسدودی موقت این خط شد.
🔴
کارشناسان فنی راه آهن، جهت بازگشایی مسیر در کوتاهترین زمان ممکن به محل اعزام شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/132145" target="_blank">📅 08:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132144">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
🔴
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
🔴
گفته شده نفتکش مذکور حامل گاز صادراتی…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132144" target="_blank">📅 08:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132143">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری /
یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
🔴
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
🔴
گفته شده نفتکش مذکور حامل گاز صادراتی قطر بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/132143" target="_blank">📅 08:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132142">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a0f3440e1.mp4?token=b-p2mJWSGr4oEKstflab5_knK-370eYtAthQG-q4I7jMOM4QoRRlHh92NOYnXP5c_k7HI2scGjTg9XQxSOdR9GGiyEnnG-uagxiMYSok-yhnb8f0F7Qx8F27a7UyZcGUPqXJcMk5FAAb97aInc_oTJ5ltZUrWZ6pUVsqtH51Jho0QGf2-t6xc02TS9bkXblo5ZK8jTuCyV2a0ifebJva7LNVau4urPqZ_wWPDyPLfAkmycybWUykVgnTiGzS8bt58rJMuOZeVhkZ1f8dz3rWRwZlr8CwBH94S4GxefpRzsSxqPsQ1C-110-oJLGsqvvleTI7vkDQymQKpwkkaR0vew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a0f3440e1.mp4?token=b-p2mJWSGr4oEKstflab5_knK-370eYtAthQG-q4I7jMOM4QoRRlHh92NOYnXP5c_k7HI2scGjTg9XQxSOdR9GGiyEnnG-uagxiMYSok-yhnb8f0F7Qx8F27a7UyZcGUPqXJcMk5FAAb97aInc_oTJ5ltZUrWZ6pUVsqtH51Jho0QGf2-t6xc02TS9bkXblo5ZK8jTuCyV2a0ifebJva7LNVau4urPqZ_wWPDyPLfAkmycybWUykVgnTiGzS8bt58rJMuOZeVhkZ1f8dz3rWRwZlr8CwBH94S4GxefpRzsSxqPsQ1C-110-oJLGsqvvleTI7vkDQymQKpwkkaR0vew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت مجلس قانون‌گذاران نروژ
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/132142" target="_blank">📅 07:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132141">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
دلار و تتر دوباره در کانون توجه بازار
📣
پس از اختلال‌های بانکی شدید، تعطیلات رسمی کشوری و نوسانات شدید اخیر، ۳ نقطه کلیدی خرید برای حفظ ارزش سرمایه بررسی شده است.
لیست سه نقطه ورود مهم برای خرید دلار و تتر
☝</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/132141" target="_blank">📅 01:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132140">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPC5UQ0PG_b6hnEZF6fIyXz1pq27vsPMa3c9ofEZUXCcKJxL4syui70zhTeR6m0nOjPExB_KJCDPcEL74ljF-8cZcpbO-ZryEX6DDvXCxfS0QIALN_pSNSCc2budw_qY-qWx9brvRwS2Z8J1_Ob8zdpSxDssUWiT1WlcAb-qTSOMME_6SPAI4h-6wz95fvsX2vEPftysnuBeSM_vTuKK-ijP4URZ1UQX9-_kUaZfMAs_LG_GTV45Py6RL6uym5i7fk9nptie1iAosN-KQBoeXe-Yj4WV-fhAwMmcMgiC_SRoMKJ6-vWV4eFsu2kQKe5WO2xTXk67jYF5SAHyaPzhVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر هوایی از گشت زنی امروز گروهی از قایق های تندروی نیروی دریایی سپاه در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/132140" target="_blank">📅 01:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132138">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8QRneu50ZYQntUwNBT7oR-0tT7FuWqaz9DMmYCC9V-opI3uZC47t_svqlgfw05FsdeOGj3jbByjrAjh3ZMiGEvBXb9gJOtXfmgs4o74CDaKSSE5VF5ceImalltFz45fq1ybAz5GQfNUVG6eQOfvis4DXIH487UKGBs9nAEffzutsFGt2IyNJmpfTeeDPf0iveyPjZ7Zut0jvmeBLtf6b86R4CtkhPCNrBEaqEb2GofTmdbP9MDS2uLa5HC-mNeNX9BCXAXsH-43FaPEIZgM1-sQqV5nZ2QFwoLrsR3XKsRAYVwpUlgF8AiHj8kE52cSXiFkCHm9mtGcn0QTwHCdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت عجیب و غریب کانالای ایتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/132138" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132137">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHklvmH1nifSOArtbRJxWudnsGBREh4oz07WUqCxxifgJ7Pfb9-ZkymxN87gIJJ6dwFUEEzEeBfLEAfRgWEbIrCvPdYBQVdOfbEwQ5ujgzk3_pvrRZqGp8rQw6a_KRR1trtl9IP9CMQfPI1b_4KIb_nJq_1BIrse1pbvJeOiUgVa8jz_qGKRMchgHj84iCQtl-hTbinOfSTf2mCCDSedYiCRbtoCg0ulgbWW6t0fXEkfLx-FSQgEYTGR7Ma0PI1Zduk0kXL0MvehV6wsfhopB2euRm_4F0bCnYVGrINM1jsNwDmOtHsNpvMtgzDLX7jyQnBOh0gggtPyex4GAxg6Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین رقص رونالدو، پایان یک عصر؛ وداع افسانه در شبی به رنگ زرد و قرمز
🔈
پایان مسابقه - پیروزی اسپانیا برابر پرتغال و صعود به یک چهارم  @AloSport</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/132137" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132136">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fdp20fjbM1lNDxcDNCFfPEkUkJ6O9QmUVHWJTQVJuOKh7DdHbyI_S12zQUR5plXJZZiVd614D7pCGpoTPAD7e04CHRRMpE2VvoJnv_GzXPOGZWryxBniW8kW8GtgW1io2OvTLx-MUGzIdpH6V46ouz07U3QTVIuhB2CRnKfA9bqTjncxEuk8fCBWnJYcXt8kkRRnCA6d_sCVJpi8CCbMMzstmXlBZvarG32B-jIEfMkQULfzsjUiYb8opOdXbdSon5094Rn_Gh8U7ny01jwCN8k-C7c2JyHoJVvQ-VeBSUpJU0R3Gk07r5SPsiSsXEt3kO_lNtEgu-M-yPxyAvGlkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین رقص رونالدو، پایان یک عصر؛
وداع افسانه در شبی به رنگ زرد
و
قرمز
🔈
پایان مسابقه - پیروزی اسپانیا برابر پرتغال و صعود به یک چهارم
@AloSport</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/132136" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132135">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=QdcBaBIveFUT_hkhE6m7hktPlvhK_6Mbzvd-fsBjR594ItIMNaRAsoDs9LDEod9feSCDR6MARQ-oIdAXu_sHTcbaf-EvSDn-GxyzLfHi0-KE0p_pxE__lUwaNA2V4JFZolOly1I1dMv-Hul8keFYbX_MeQ_8lFWfhFIMOnp56MKyvcv_lT_uHNxBq6NKKWx5uiJGp-cqZrDLJwm5vM40uRQVOIf2Glwnx5AtwkZNCwmsoDxccFEKzIzhP6qshsiGxo2_Rq0F4q8SZgoA3IaAwxv6pMyvtJSxsqJAoFs6q58v38wpKtNRQ_Jrb_SVJHq4QZI2FRsHNMUPEqf95HITIhn1QKwCakwsW9t_GbWF4PcOAedfG6ohvJ_yVccpSpNdXIA7YLrmSPZkzo-pDbVMVMICnjvPt1Z6RQoY3cYrTxfil3kztQryhSC2EfcDicvjDgNjCfkEhsEJW-f1HNvUMq_liosfTrkgg2L5PTJg7k6qpyMl62UsstjEQoiJBG3tIanmqxievdB2yhHS_2USn9JfXTRR1PbXBoRh3nib9GmhiCvrNVST1tB6T6OuBDOzf7GW1PrZHKaizVHEjJpL-Xa-RI55FJMF0kvrSR3-wvXRReFSjPR3a20-eVhcTg6INc3mqvYW69rGAgtcxcWjE-qXQ9L_k8R-LmhLBKjOwls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=QdcBaBIveFUT_hkhE6m7hktPlvhK_6Mbzvd-fsBjR594ItIMNaRAsoDs9LDEod9feSCDR6MARQ-oIdAXu_sHTcbaf-EvSDn-GxyzLfHi0-KE0p_pxE__lUwaNA2V4JFZolOly1I1dMv-Hul8keFYbX_MeQ_8lFWfhFIMOnp56MKyvcv_lT_uHNxBq6NKKWx5uiJGp-cqZrDLJwm5vM40uRQVOIf2Glwnx5AtwkZNCwmsoDxccFEKzIzhP6qshsiGxo2_Rq0F4q8SZgoA3IaAwxv6pMyvtJSxsqJAoFs6q58v38wpKtNRQ_Jrb_SVJHq4QZI2FRsHNMUPEqf95HITIhn1QKwCakwsW9t_GbWF4PcOAedfG6ohvJ_yVccpSpNdXIA7YLrmSPZkzo-pDbVMVMICnjvPt1Z6RQoY3cYrTxfil3kztQryhSC2EfcDicvjDgNjCfkEhsEJW-f1HNvUMq_liosfTrkgg2L5PTJg7k6qpyMl62UsstjEQoiJBG3tIanmqxievdB2yhHS_2USn9JfXTRR1PbXBoRh3nib9GmhiCvrNVST1tB6T6OuBDOzf7GW1PrZHKaizVHEjJpL-Xa-RI55FJMF0kvrSR3-wvXRReFSjPR3a20-eVhcTg6INc3mqvYW69rGAgtcxcWjE-qXQ9L_k8R-LmhLBKjOwls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عوستاد
خوش‌چشم، کارشناس مسائل فوق استراتژیک: باید هزینه بالایی برای خون خواهی امام شهید ایجاد کنیم/ کانال ۱۴ اسرائیل می‌گوید رهبرشان را شهید کردیم و هزینه‌اش فقط ۴۰ روز جنگ بود و دوباره می‌توانیم این کار را کنیم/ این بار آقا مجتبی توانستند جایگزین پدر شوند، اگر باز رهبر ما را شهید کنند چه کار کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/132135" target="_blank">📅 00:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132134">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDxbIGCkfiXSQrvpmwIEtfnsxVcXFxBp-Z57lBci4JbTLwjE0jNZ_RIVDr5T38OAaDWBCAusOvb3yYGDI2x34tgLGmw3Kz-8YvuH5u5xAfd-ite6qdpjYmXuP2X4g6Xqs5rqQzoYbJ7F5_Y_SqeWG26XdrGPmIUHq34fY8Et_X-I9k02PLmKgyCqKxZTHouHDUPYIlZqL8BKNVpE-xGlCYl1m19KgCXXY86eKCb2fHkz76j8gX1KURHU48_JaLp_OKqWRNfeGLZ9AGuwbua0m73SXcTyrOFjx71wBLhX1CrgpawJfBSKyKtD0Jz-EzUMl-Z3_YmHGCwHhDTORrkZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دادگستری :هر کسی که بعد از ترور آقا از نظر روحی و روانی آسیب دیده، می‌تونه با وکیل رایگان شکایتش رو ثبت کنه و پرونده رو برای پیگیری حقوقی و مطالبه خسارت تو مراجع داخلی و بین‌المللی دنبال کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/132134" target="_blank">📅 00:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132133">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxhR4apZTbl_IhLJ8yXKlf16-01At3ze4pjW6r6DH8dLh9F85QJAHXDE2LkF3Ik4pR9Fc3ZhZbPdiCdujYHo9BL65hIJXUyZDscV1zhSPLmxc-5wKgbtcjf4C0XYNYcaMAlBEXMydJtsiw-Q9DRJ8IxXneK327CMv8SXXetO13EfPmkDM2nLLw4V2QjzqGeQ70GT0DaWszYPx5AXlG8_qWr3x87hgJ-jTwcftV8IZETC_gJLW3OyZXMTOGwuinjbJmTWt-atORTOagWzoAMKBEEOcIIvcS-xdMKD-o_i5w2QU8w4bwwppINT4Fq_K6uq8lTIknTZB5RmpAvDAPzvFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کامنت هادی چوپان زیر یکی از پست های مربوط به علی خامنه‌ای
جونم برای لحظه لحظه‌هایی که از تلوزیون دیدمت
😭
😭
😭
😭
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/132133" target="_blank">📅 23:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132132">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7guL-z7rzkTbOeDHdw9LRb1dxYM1BZO6TGYXoY8fz6mCEo7GaOqkWCAyHgpNimmebeItjCoknj4rUf6_yJhKeavaKouiEPHCygu7SV89SZlSIwSDORarLQ2aphesvZnY-Q1-dgVb5GLYY5wBx9geg_aqK6WAqY8QxcMWgS5AOqywvrlCsk3Cl_pKa-8CLrcWZjM9WoZtLSuMM7dTqIepiGq11iZynZvC3mMOTD4fSpUQb2KVFkKtl2xGZTQrFxTqvlkJU6SoI1REKsxWtKknfv5nhVRKTlNfIfOrHoEKwzlGpWJIU5_aKTBfxd3Oxn9G6XQw4ZuZvj3O5NaoALrLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو تصویر به فاصله 6ماه
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/132132" target="_blank">📅 23:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132131">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رویترز: ارزیابی یک نهاد اطلاعاتی اروپا حاکی از آن است که روسیه با یک بحران بانکی «انفجاری» مواجه خواهد شد
🔴
بانک‌های روسی بار فزاینده تأمین مالی اقتصاد جنگی را بر دوش می‌کشند و همین امر آنها را به‌طور فزاینده‌ای در برابر تحریم‌های جدید اتحادیه اروپا آسیب‌پذیر می‌کند
🔴
پارسال بیش از ۵۰۰ هزار شهروند روس اعلام ورشکستگی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/132131" target="_blank">📅 23:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132130">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjpqB2C3wBzgnC77HSBFrZ2r-agJHuLOrP_r2Xyl6qHfmcQFNqqk6CtUSSrBfjjtZjj0z_WsGsjo9bKyZOAaSnnLqVRk4W96OypqauSaNTxcpj0PUdZEmZDgKPMsqa4j8LUUPO6yQMNBf--B0WhKapK8bY9Fx8LXnVJiNmb7rr3D0TbFdeSIeU4RSjYHprAq6tRtCQGq8yWGxjLmwO-fLGm1qYlDWuJ3VRyOdgHREVLIYWjduTv1g7pNMQGM7UWNaRecesJnLzC9VmVaZg9WqRf-mO3Wsd9vag1NiurS_lValf0q6r05rvQ1Qs-f7v95xb17GofRunIuxQ4Ui-nD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قرار دادن اتوبوس برای جدا کردن مردان و زنان در جمکران
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/132130" target="_blank">📅 23:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132129">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
جوزف عون، رئیس جمهور لبنان: با بنیامین نتانیاهو، نخست وزیر اسرائیل دیدار نخواهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/132129" target="_blank">📅 23:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132128">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
جوزف عون، رئیس جمهور لبنان: با بنیامین نتانیاهو، نخست وزیر اسرائیل دیدار نخواهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/132128" target="_blank">📅 23:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132127">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b01ad335f.mp4?token=e-KvIctMpwjAD9QGlFdl5tpAOdk8kYf69JKV3tk5VtKkf1i1FmfKMUxZsWrL-nhbwle2vN3yvF6PpjXeOpRIF7F7RwukPIGBgI3Ppr9x6Vw0_xcKAmSyzMOb7FMdhCYccSSYHjyDJsloBWgZZhoEjoujVSBHP_Rl6Nw2eaDKNpJdmHoBQnqtP8MCVJW3PfjgxNyjW0Oxk0ttIic1j4rSD5PFzHyCFPSr5J5WQHrY9A34RYb6Q1PL_4DOg5zC_fsPa5aWi8rWBCCK7H9n_Y7KyI4HknDuIT1A7PZWOABGWxyA5ggAp_QSnDtNIT0sK-16w0o7z_btsNohrX2UrRmfpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b01ad335f.mp4?token=e-KvIctMpwjAD9QGlFdl5tpAOdk8kYf69JKV3tk5VtKkf1i1FmfKMUxZsWrL-nhbwle2vN3yvF6PpjXeOpRIF7F7RwukPIGBgI3Ppr9x6Vw0_xcKAmSyzMOb7FMdhCYccSSYHjyDJsloBWgZZhoEjoujVSBHP_Rl6Nw2eaDKNpJdmHoBQnqtP8MCVJW3PfjgxNyjW0Oxk0ttIic1j4rSD5PFzHyCFPSr5J5WQHrY9A34RYb6Q1PL_4DOg5zC_fsPa5aWi8rWBCCK7H9n_Y7KyI4HknDuIT1A7PZWOABGWxyA5ggAp_QSnDtNIT0sK-16w0o7z_btsNohrX2UrRmfpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون صدر اعظم آلمان: جنگ ترامپ علیه ایران غیرمسئولانه بود
🔴
لارس کلینگ‌بیل: جنگ غیرمسئولانه‌ی ترامپ علیه ایران، رشد اقتصادی مورد انتظار آلمان در سال جاری را به نصف کاهش داد.
🔴
این جنگ هزینه‌های مالی سنگینی را بر آلمان تحمیل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/132127" target="_blank">📅 23:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132126">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ubgtkYh80I_dq1apGLKGzpZXYYhlcu1veu0CO7VhEJVSjApFld2dXES5ZNItjdWMHHTksoD_XhAMqEczkq5-hQ6mM82jZxaW9B4Ap9heO21qRibFDTTDhykeayaa6jhNGVYihCQennflS8iRfoeDFapeCIxlCmXK8JYnOEcysFmoT1awXJygz5Dn9iKWDUCfU80cfh-ggQSPgi2R4qxNBQuC3YUo9OXMHaTZjBDXDwbVW3Wb3zhhWLpGd6c9kTnMV2mcTqTlrOqqP4andkry7vJtDKiayw9pXF-upDAWxSXatMkpWTOVGJtnklQV-z0aaAnbCpc5tpc8OFd7JvtzaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاینشنال تایمز : تاکنون حدود ۱۲ تا ۱۵ میلیون نفر در مراسم خاکسپاری خامنه‌ای شرکت کرده‌اند و این امر آن را به بزرگ‌ترین مراسم خاکسپاری در تاریخ مدرن تبدیل می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/132126" target="_blank">📅 23:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132125">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8yt3ehLWf50O6qu6Qj-nHPjug6DjjuQfP9rfFclw1GuICJACIaxcyqqG-1GlbXdRmYpyHStbZ6iRUOXdB7Sf-LTY0POlPdqRIu2UAvP8n9wUhEUxMK-NvUP2PVPAcGVD_0XO_oqIUfYjcSI7TzSfOo1Ql6uF5MNx33dO1HlnO3EikoVvMKSJ9h8xw9eGXxInb8fmvLDToxY5bpnchNEKSxaRSeoSiDX-NLTz9eJMdN1xYrcm_W_Jn3GEAM3oa2cDeUZDmjLs6T9ESTUTH_oz6vAUzApzYtVSDe787jMml8c-En08LUf9GDBsJamtklZny27J5TpsEzmw4qFmk22qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: قالیباف مجلس رو باز کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/132125" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132124">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
لرستان هم فردا تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/132124" target="_blank">📅 23:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132123">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سی‌ان‌ان: یک‌سوم کشتی‌هایی که طی چند روز گذشته از تنگه هرمز عبور کرده‌اند، مسیر ساحلی عمان را انتخاب کرده‌اند
🔴
از جمعه تا یکشنبه ۱۰۸ کشتی از این تنگه عبور کرده‌اند؛ از این تعداد، ۳۰ کشتی مسیر عمان را طی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/132123" target="_blank">📅 22:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132122">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXaf_5WIgjh6qeE5csK8CvJpgVFkP_f0kunpKPoQOHhYAtZNXIpc3s9NiTZbD3GNS036UPbkri4mAVN1IcYsEoaLBA9W4XqZTrgwxjkmFPRPVq17F1VOrbHZuwomVgcwiTBZAFV1Ur9o0FhQTAwEIQikrG4wH9RWmwYuq-AzxX5lDs11oz0T3rUoTiH0ShKhow9m9v47sqbk4ejcXGUHc4JH9OwYavSSVM3vYDuwrRFMCRoJv19mtwFf_pTb4ne5LCFHXQhpMcycPvuSwFpmDJ_sX0rtCQPkjHxunHBQjeOY8Ssowl971SsuDHqztu3SO0ChIZLBPNBnA7CbyMhX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیر شورای‌عالی امنیت ملی، خطاب به ترامپ : با مردم ایران با احترام حرف بزن
🔴
قبلاً هم با تهدید چیزی به دست نیاوردید و آخرش خودتون دنبال مذاکره و آتش‌بس رفتید
🔴
اگه دوباره با لحن تهدید صحبت کنید، ایران هم متقابل جواب می‌ده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/132122" target="_blank">📅 22:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132121">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7a1205f8.mp4?token=V1UlSfgQCeMUDFy7znQSfQaD4X3ActIXnrBoyHSkS4xzdFHrWYoK5_y3JHc2gw8TkZVXFgVaSOy1LSp2ogpdT1rUampNLcnUFwmzAg7Am4AJ7bfHbSJKrmhRzUs_1-SfNd-GK39P0KUrykgb1UadpHcWSL9YZR6_hKTTN8WQQyK8dn-FQx00n82UN-7OymRsPw8xt3JGSP5Hm7lm3HWHmR0Dk1_hUH1dRsuQB_vEWA7wXgr_TntTUy76ci4p062QH15iJGuLUDPswltzSM-M2wDtmWkgb4brv52ReYjAOrgtfXFi660Q-Ej6xaQQL_X_38_6k2cUtAciZNvYTTsjcw7xbdXvbnXxBLIG7CpcrBqa9aytaOXfbE41EM87urnV-qXPoLHU8sY_-PfHHwqBo72nGNa5uTAVn5xZJ2RU7PrKJwfBhVDrtuWeSyBpNxV4GbZPXYgGJt9XGL-h05tgO5-9c1bGydVEv0b9ldSLTJHr8C5e9ESsEnvFhi2-gFQD9BJVyhjYujicZMhm6GwAxdKWpaBoevKmx_Pul1hrsyEOM_Ted5AndnjsUGxvMZK6oduhdjkn2qqsnz4ekblnPEIgNPYBnT8BwDtjBZuknh0etiXa20ssrB7Tuyy5sxVYllSnkNuM7EpRf_s76OvvXZA9M8J40LmdbLKihpeRJEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7a1205f8.mp4?token=V1UlSfgQCeMUDFy7znQSfQaD4X3ActIXnrBoyHSkS4xzdFHrWYoK5_y3JHc2gw8TkZVXFgVaSOy1LSp2ogpdT1rUampNLcnUFwmzAg7Am4AJ7bfHbSJKrmhRzUs_1-SfNd-GK39P0KUrykgb1UadpHcWSL9YZR6_hKTTN8WQQyK8dn-FQx00n82UN-7OymRsPw8xt3JGSP5Hm7lm3HWHmR0Dk1_hUH1dRsuQB_vEWA7wXgr_TntTUy76ci4p062QH15iJGuLUDPswltzSM-M2wDtmWkgb4brv52ReYjAOrgtfXFi660Q-Ej6xaQQL_X_38_6k2cUtAciZNvYTTsjcw7xbdXvbnXxBLIG7CpcrBqa9aytaOXfbE41EM87urnV-qXPoLHU8sY_-PfHHwqBo72nGNa5uTAVn5xZJ2RU7PrKJwfBhVDrtuWeSyBpNxV4GbZPXYgGJt9XGL-h05tgO5-9c1bGydVEv0b9ldSLTJHr8C5e9ESsEnvFhi2-gFQD9BJVyhjYujicZMhm6GwAxdKWpaBoevKmx_Pul1hrsyEOM_Ted5AndnjsUGxvMZK6oduhdjkn2qqsnz4ekblnPEIgNPYBnT8BwDtjBZuknh0etiXa20ssrB7Tuyy5sxVYllSnkNuM7EpRf_s76OvvXZA9M8J40LmdbLKihpeRJEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مینی تندرو: قیام کنید و بزنید و داغون کنید تا توافقی شکل نگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/132121" target="_blank">📅 22:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132120">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری / هم اکنون درگیری مرزی میان نیروهای طالبان و پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/132120" target="_blank">📅 22:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132119">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: پوتین می‌خواهد به جنگ اوکراین پایان دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/132119" target="_blank">📅 22:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132118">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78086417f9.mp4?token=laSa5PRpSO0aDcna_p0jJWm2T_tb0yTMwWJMoCDvaMyIFbidt8OF1UTBPEPUz4vw9seaTDNW1Ih4ubKRuhFBOQ5mJJ8YKrABSQgi_0x8JOf2hEU17SJis32M4c8Ceh8SBiKAAPznGzG49n-cmMLvq1--Ss8m8oc4lozmdtsyXnSeXEQ6ZrMZYAC6DccHssB_bQnP0owCm6HERCpKdtrOiyy7cOQj-5K99JzASsTuWNUk9Rt062TkS-Llk3Kyonv9UD3HP3e3585OQMPVEFynPYHbee8XJBUGRhnndUlm3kI63cwWCPX9JwlW0vSJsDk2IO_-txG6LIDCSXqVTL92JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78086417f9.mp4?token=laSa5PRpSO0aDcna_p0jJWm2T_tb0yTMwWJMoCDvaMyIFbidt8OF1UTBPEPUz4vw9seaTDNW1Ih4ubKRuhFBOQ5mJJ8YKrABSQgi_0x8JOf2hEU17SJis32M4c8Ceh8SBiKAAPznGzG49n-cmMLvq1--Ss8m8oc4lozmdtsyXnSeXEQ6ZrMZYAC6DccHssB_bQnP0owCm6HERCpKdtrOiyy7cOQj-5K99JzASsTuWNUk9Rt062TkS-Llk3Kyonv9UD3HP3e3585OQMPVEFynPYHbee8XJBUGRhnndUlm3kI63cwWCPX9JwlW0vSJsDk2IO_-txG6LIDCSXqVTL92JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور سوریه: سرمایه‌گذاری در سوریه، فرصتی بزرگ برای کنسرسیوم‌های بزرگ خارجی است که به دنبال رشد و توسعه هستند تا زیرساخت‌های تخریب‌شده در طول 14 سال گذشته را بازسازی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/132118" target="_blank">📅 22:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132117">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚀
سرویس های پایدار  safe vpn
✔️
اتصال پایدار و پرسرعت
✔️
دارای ساب برای اطلاع لحظه ای از باقیمانده
✔️
متصل در تمامی دستگاه ها و اینترنت ها
✔️
مناسب استریم، بازی و استفاده روزمره
✔️
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 30,000…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/132117" target="_blank">📅 22:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132116">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚀
سرویس های پایدار  safe vpn
✔️
اتصال پایدار و پرسرعت
✔️
دارای ساب برای اطلاع لحظه ای از باقیمانده
✔️
متصل در تمامی دستگاه ها و اینترنت ها
✔️
مناسب استریم، بازی و استفاده روزمره
✔️
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 30,000 تومان
▫️
۴۰ گیگابایت — 60,000 تومان
▫️
۶۰ گیگابایت — 90,000 تومان
▫️
۸۰ گیگابایت — 120,000 تومان
▫️
۱۰۰ گیگابایت — 150,000 تومان
▫️
۱۵۰ گیگابایت — 210,000 تومان
▫️
۲۰۰ گیگابایت — 300,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 450,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 50,000 تومان
♦️
۵۰ گیگابایت — 80,000 تومان
♦️
۷۰ گیگابایت — 105,000 تومان
♦️
۱۰۰ گیگابایت — 155,000 تومان
♦️
۱۵۰ گیگابایت — 230,000 تومان
♦️
۲۰۰ گیگابایت — 305,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 585,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 160,000 تومان
▫️
۱۰۰ گیگابایت — 200,000 تومان
▫️
۱۵۰ گیگابایت — 300,000 تومان
▫️
۲۰۰ گیگابایت — 400,000 تومان
▫️
۳۰۰ گیگابایت — 600,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 680,000 تومان
🤖
ربات خرید
@SafeVPNXBot
✅️
📞
پشتیبانی
@safevpn_secureSupport
✅️
📢
کانال اطلاع‌رسانی
@safevpn_suportt
✅️
😍
رضایت مشتریان
@safevpn_feedback
✅️
🌱
سپاس از اعتماد شما</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/132116" target="_blank">📅 22:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132115">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
یزد سه‌شنبه ۱۶ تیر تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132115" target="_blank">📅 22:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132114">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
آی 24نیوز:نیروهای نظامی اسرائیل در حال آماده‌سازی برای احتمال از سرگیری درگیری‌ها با حزب‌الله هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/132114" target="_blank">📅 22:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132112">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
مکرون با عینک آفتابی خود وارد دمشق شد و توسط وزیر خارجه سوریه استقبال شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/132112" target="_blank">📅 22:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132111">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
قالیباف: قاتلان شهدای این سرزمین به ویژه قائد امت به سزای عمل‌شان خواهند رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/132111" target="_blank">📅 22:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132110">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbbae44e7.mp4?token=usQ7UFX0dCGPJ3wZ1eMuOVBG_Bnuxow2FZRKmZzWfU6RzURtAr-kt9I4zgVn_PtL6RUV3MZ6gydfXF2RJ-7xpAq1E-WT189FmgtVqyU2FZcZXrSDe6HuSwAheAZQhWp5Vtx_SAnoee9SKO6gWLXyCFSD2T-2zQ3tzjte8arIgPFPO3GzjGN9AG5m63KdOB8EKMiI98QU7-idNiihPtXwd59KuiFLAUiKYbf1tgqquUNiyity0Ih3zowiHzOd4LLsvBlYOJm4Wa1rGME_rWbqpZB2fTfEyPHTwMui-V6_eISbt3xdHfjZ-_Xz13lBb6gyylWCXE_Tn41JnTTrp8Znow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbbae44e7.mp4?token=usQ7UFX0dCGPJ3wZ1eMuOVBG_Bnuxow2FZRKmZzWfU6RzURtAr-kt9I4zgVn_PtL6RUV3MZ6gydfXF2RJ-7xpAq1E-WT189FmgtVqyU2FZcZXrSDe6HuSwAheAZQhWp5Vtx_SAnoee9SKO6gWLXyCFSD2T-2zQ3tzjte8arIgPFPO3GzjGN9AG5m63KdOB8EKMiI98QU7-idNiihPtXwd59KuiFLAUiKYbf1tgqquUNiyity0Ih3zowiHzOd4LLsvBlYOJm4Wa1rGME_rWbqpZB2fTfEyPHTwMui-V6_eISbt3xdHfjZ-_Xz13lBb6gyylWCXE_Tn41JnTTrp8Znow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله زامبی‌ها به عراقچی در مراسم امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/132110" target="_blank">📅 21:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132109">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رئیس فیفا درباره لغو محرومیت ستاره تیم ملی فوتبال آمریکا: ترامپ با من تماس گرفت
🔴
من تصمیمات کمیته انضباطی فیفا را زمانی که صادر می‌شوند می‌خوانم؛ گاهی از آنها شگفت‌زده می‌شوم
🔴
اینکه ما شخصاً از یک تصمیم خوشمان بیاید یا نه، اهمیتی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/132109" target="_blank">📅 21:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132108">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
حشد الشعبی: نیرو‌های ما وظیفه تأمین امنیت مسیر انتقال پیکر از جاده کربلا–نجف تا حرم امام حسین و حضرت ابوالفضل را بر عهده دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/132108" target="_blank">📅 21:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132106">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
نیویورک تایمز: طبق داده‌های شرکت «کپلر»، در سه روز گذشته ۱۰۸ کشتی از  تنگه هرمز عبور کرده‌اند
🔴
با وجود بهبود نسبی تردد، مقامات دریایی گزارش می‌دهند همچنان حدود ۳۰۰ تا ۴۰۰ شناور با ۶ هزار خدمه در خلیج فارس سرگردان‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/132106" target="_blank">📅 21:18 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
