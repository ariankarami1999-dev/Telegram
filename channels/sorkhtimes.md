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
<img src="https://cdn4.telesco.pe/file/SbOpPtLB0rnrLv_RXxKeWzyrbwmiVPw1i3ViWlroa-4cbN7HoBb1uP_tCik65-BrPu772Sl3Gw9XJDMM3NOGJ1lHkvA45ZvN8clMUiQ8xpjj8taSvldogSErnB4Rti0L2QBweZ0IVLW1cC6MZ_5ybuM4vwq6RmEsrZyfCayFBme878uoiZ51COZepCW20vgmfwatvGElwVrJJAPg908A091ZyqpOO5vU_7UGYL2iAzSjLhmkQcQNAHkL3wfe6in-VDLy0i04fXubcJv45DoXXvXCtpfvNgUzLj8AtQZ5qZ6ZC0XGCw65KpSTV-BMKVkHKUNOFA-sy1u-7OzCQP5LgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 21:30:46</div>
<hr>

<div class="tg-post" id="msg-132659">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🏆
رونمایی از قوانین جدید جام جهانی 2026
🔺
مهلت پرتاب اوت (پنج ثانیه): اگر بازیکنی عمداً شروع مجدد بازی را به تأخیر بیندازد، پرتاب اوت می‌تواند به تیم حریف داده شود.
🔺
ملهت زدن ضربه دروازه توسط دروازه‌بان (پنج ثانیه): در مورد تلاش‌های عمدی برای به تأخیر انداختن زمان بازی هم چنین چیزی اعمال می‌شود و این می‌تواند منجر به دادن امتیاز کرنر به تیم مقابل شود.
🔺
تعویض‌های محدود به زمان: بازیکنان تعویضی 10 ثانیه فرصت دارند تا از نزدیکترین نقطه زمین را ترک کنند. اگر این کار را نکنند، بازیکن تعویضی حداقل به مدت یک دقیقه نمی‌تواند وارد زمین شود و تیم باید با 10 بازیکن به بازی ادامه دهد.
🔺
درمان بازیکنان در خارج زمین (یک دقیقه): بازیکنانی که توسط فیزیوتراپیست تحت‌ درمان قرار می‌گیرند باید به مدت 60 ثانیه از زمین خارج شوند. البته استثنائاتی نیز وجود دارد، از جمله برای دروازه‌بانان، مصدومیت‌ها و اگر حریف کارت زرد یا قرمز بگیرد.
🔺
پوشاندن دهان توسط بازیکنان: هر بازیکنی که در موقعیت درگیری لفظی با حریف دهان خود را بپوشاند، ممکن است با کارت قرمز جریمه شود.
🔺
بررسی درستی ضربات کرنر: اگر VAR (کمک‌داور ویدئویی) مطمئن شود که کرنری که به یکی از تیم‌ها اعطا شده درست نیست، می‌تواند دخالت کند و آن را لغو کند، اما این کار باید سریع و قبل از شروع مجدد بازی انجام شود. این اما شامل برگرداندن ضربه دروازه‌ای که باید کرنر اعلام می‌شد، نمی‌شود.
🔺
بررسی درستی کارت زرد دوم: بازیکنانی که به دلیل دو اخطار از زمین اخراج می‌شوند، می‌توانند کارت زرد دوم‌شان مورد بررسی قرار بگیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 354 · <a href="https://t.me/SorkhTimes/132659" target="_blank">📅 21:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
25 گیگ 300
30 گیگ 350
35 گیگ 400
55 گیگ 500T
100 گیگ 750T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 795 · <a href="https://t.me/SorkhTimes/132658" target="_blank">📅 20:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132657">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PI-WgLoNN2EsZmh-msTeGdpvS4JkkVoEOm2333i7LvVdpRECdIo6xPbPEVeR5vsE14HYArkGrbQ3ANKAd_n9Eeje0Jt_E-9Uz3ajn3MhsS4UXYT_zk9nYl7rx8EeNN7nUbhPTDIdTXGXUyeO8YCYfRNHalge7DRDnpWnyY_iNA79xdulEiE1uRbM14bnO6X9HlfDPRb80wBETYjbJuB0KhzqZavYc_x_l7G0pKrFIGORLqWhxmNvg5x_7OS-96RLi_TDcCdOibaoQkLdnd8DzQ9mI888bkK2F4m1rYmcQZlEEv7lPKQ4qisWJyaj84nDFhrsaF0EG5_vLjWAwAn_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⛔️
معمای بارگذاری مدارک استقلال برای آسیا!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 758 · <a href="https://t.me/SorkhTimes/132657" target="_blank">📅 20:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132656">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">▪
︎با این وضعیت اینترنت،
ربات تلگرام وینکوبت
خیلی کاربردیه چون براحتی وارد سایت میشی.
▪
︎هم ثبت‌نامش سریع انجام میشه، هم کازینو رو داخل خود تلگرام میتونی بازی کنی و عملاً کل سایتو داخل ربات داری.
▪
︎پیش‌بینی، بازی، واریز، برداشت و همه‌چی همونجا انجام میشه و خیلی روون‌تره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 828 · <a href="https://t.me/SorkhTimes/132656" target="_blank">📅 20:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a6eda933.mp4?token=bi5gzQ3Tmt2eNYZkYo2TBpvvbMwm-KypLiqKnvi4t6LUCO8qNCsiPo6i3b8vwmw6O_XZDpoexUUssy8CO-K75WQTJXeKMhfIKZqeVr8uzhtEStxR4VT1sTR8dFKMfVrL7xopSdpKht4PnFUAKERoFVIwa2CcRVrQ29z-TwGGUJurEMxlt7aIhe1d7HC7jJbBxQeMx0If_3ZxHRlOOAp1sAPEzX6xQ8Rv5StvFOpWwWmEb55IIFG8nULIOdQ9MIuSr__6ExwnkJnIQKglGE7ajQRr9F3q_yk5jIU6fgJNrG83RZ3qZP-qti5F-_3cX11L9UclWQJ3CDkEvuEqP3TgxL9PlQiN0HXINuRgUmRW-p8qEwBATcGgU5tvOoRjkonCwr36Tg_oBPx_7ECbwQZpuuS073XQvWlO8UO9NSjLKgB7q6-01YtdkkzkYfyCuLzamSdrMGWkmn8HyUd-JuwEdmSNji_AwqLbBcDRzptBCXGNeKVQwOe18pX8P29VdLStywnWSCSFszO7-ZudHAzCIMitEv1b5qqeVwdnyU-UgrOgw72esAOaBaiCPMfnjVA_7q_jzkNU5nnz70Bx9iSVRFuJBZ3wO7d4jQM1_lAPY9Vl7uH-52FwLqBHJ-5XaaCCPC5HklbOpOdtlAmGGc9BzCSZ-YZmnOhpcmvrib4USlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a6eda933.mp4?token=bi5gzQ3Tmt2eNYZkYo2TBpvvbMwm-KypLiqKnvi4t6LUCO8qNCsiPo6i3b8vwmw6O_XZDpoexUUssy8CO-K75WQTJXeKMhfIKZqeVr8uzhtEStxR4VT1sTR8dFKMfVrL7xopSdpKht4PnFUAKERoFVIwa2CcRVrQ29z-TwGGUJurEMxlt7aIhe1d7HC7jJbBxQeMx0If_3ZxHRlOOAp1sAPEzX6xQ8Rv5StvFOpWwWmEb55IIFG8nULIOdQ9MIuSr__6ExwnkJnIQKglGE7ajQRr9F3q_yk5jIU6fgJNrG83RZ3qZP-qti5F-_3cX11L9UclWQJ3CDkEvuEqP3TgxL9PlQiN0HXINuRgUmRW-p8qEwBATcGgU5tvOoRjkonCwr36Tg_oBPx_7ECbwQZpuuS073XQvWlO8UO9NSjLKgB7q6-01YtdkkzkYfyCuLzamSdrMGWkmn8HyUd-JuwEdmSNji_AwqLbBcDRzptBCXGNeKVQwOe18pX8P29VdLStywnWSCSFszO7-ZudHAzCIMitEv1b5qqeVwdnyU-UgrOgw72esAOaBaiCPMfnjVA_7q_jzkNU5nnz70Bx9iSVRFuJBZ3wO7d4jQM1_lAPY9Vl7uH-52FwLqBHJ-5XaaCCPC5HklbOpOdtlAmGGc9BzCSZ-YZmnOhpcmvrib4USlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیا پرسپولیس به دنبال جذب لیموچی، ایری و آریا یوسفی است؟
🔴
پیمان حدادی: با هیچ بازیکنی مذاکره نکردیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/132655" target="_blank">📅 20:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132654">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1124c640f.mp4?token=M0HWItkrSiqXZzlx9s_tNUMMenfqJEN7V9o8E-i90FZ1_a6JS_L1L06Qb1gRL3rA1PQ1fTbcjYS1QAnQM3BgNE_8hBDX9wEjL8zAJ1fIwosHl2Cnjzf2ujJGILdBe3-HmU1_ZYFiNOy_iKnAw-0BEhw2Mcyk7DmRWeWUPg-IBWocnBMIQqSfJRmdY9W-X47Vrd25ML9YEPR3rJMCQqIGaeFtcnfWdrKHS6YXoqITvuzCmISFSsjohm76ZJVmPjep7qVjSNRPZDTbGl0ljcD1qRgggsgAOrO4-jI0nN68MxOaAEf-7qQ839M2A0w6wQGS5_QiCu6xpLfiMqtIgUIeJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1124c640f.mp4?token=M0HWItkrSiqXZzlx9s_tNUMMenfqJEN7V9o8E-i90FZ1_a6JS_L1L06Qb1gRL3rA1PQ1fTbcjYS1QAnQM3BgNE_8hBDX9wEjL8zAJ1fIwosHl2Cnjzf2ujJGILdBe3-HmU1_ZYFiNOy_iKnAw-0BEhw2Mcyk7DmRWeWUPg-IBWocnBMIQqSfJRmdY9W-X47Vrd25ML9YEPR3rJMCQqIGaeFtcnfWdrKHS6YXoqITvuzCmISFSsjohm76ZJVmPjep7qVjSNRPZDTbGl0ljcD1qRgggsgAOrO4-jI0nN68MxOaAEf-7qQ839M2A0w6wQGS5_QiCu6xpLfiMqtIgUIeJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل باشگاه پرسپولیس: از فصل آینده لیگ دسته اول تیم پرسپولیس ب در این لیگ شروع به فعالیت می کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/132654" target="_blank">📅 20:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132653">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
پیمان حدادی
: با هیچ بازیکنی مذاکره نکردیم هنوز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/132653" target="_blank">📅 20:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی باشگاه:
🔺
ما باشگاهی هستیم که به خاطر سابقه، به خاطر حضور هوادار، به خاطر امکانات، به خاطر شرایط حرفه‌ای سازی و موارد دیگر حق خود می‌دانیم که در فصلی که نیمه‌کاره مانده بتوانیم در رقابت‌های آسیایی فصل بعد حضور پیدا کنیم و برای موفقیت کشور ایران در آسیا بجنگیم که نفعش به همه می‌رسد.
🔺
ما در این زمینه از حق هواداران پرسپولیس کوتاه نخواهیم آمد و تا آخرین لحظه از حق خودمان دفاع خواهیم کرد. خیال هواداران هم راحت باشد که ما اجازه نمی‌دهیم تصمیمات خارج از زمین گرفته شود. همانطور که بارها اشاره کرده‌ایم، از نظر ما پرسپولیس می‌توانست در هشت بازی باقی‌مانده شرایط جدول را تغییر بدهد و به یکی از تیم‌های بالای جدول برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/SorkhTimes/132651" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SorkhTimes/132649" target="_blank">📅 19:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132648">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uinC8hn7KwByG5bA_7WkIJLZ9AmUCg85bgfewpBbwggprL5DPXuFmNNhaI88MiiRRnpvhHZZXvYcBCvLXDm6cw7A_kEpXB_kpHSs4O5TrYkKIkYCO8FNVQgDCmJgNdDWCv8ucrET-6QOccnj4khcphM0rJWxMdsIxGfj5qTGggTAQhBEbfFVIUJskpnCAlfsiuuMoaS60d3SbFnKIE3HpKN2UFC62DNFWhBylUkslatWdLqsMWDmkqKSZYhd9rxqGyWptGpMmwCDpaEcPlX9SQ06i6dSrjzx_XzEePA2aurAC5yRTl5KHLkI7Ntwph4dkhNVqZ2UY0tbDntmFJB91A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
گل محمدی هنوز تصمیم قطعی خود را نگرفته و می خواهد پیشنهاد تیم دهوک  عراق و شرایط موجود را بررسی کند و بعد تصمیم بگیرد.اخباری از سفر او به عراق در پی پیشنهاد تیم دهوک منتشر شده است
/قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SorkhTimes/132648" target="_blank">📅 18:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7awmuOmpZyKHAJk9v6oVpxZs_Ba-SJSbF2XZ1COI9-jbvCXe0CmQjAjujAChL5umeEsVr6TBdYdN7Ck6mzTGzi7nYb2OzfU4CQFNNVlzZH1us6QZPZcAYaxY2uTLmHCIG0BSe8IVPTUwNVnxoGF6cLpQk4A1pIwaV1EvtTjUjML9BOBktG4-NnoNW1-X3yRMdvAqoDmrLR6TqEo6PgxUMndv4NfJjy0zppF3MlWZ_dSjw7SNpUyeDoOF4tXRraQdGcGDpx1JAYZYw69JeBuvGn2sgG91q67ECaq-dgnZog90jaRhLS7X5PRUF24Vt7VpbDexQ8CFaD8OkR64kbYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
برگزاری مراسم تجلیل از مربیان بازیکن‌ساز آکادمی فوتبال پرسپولیس
⏺
باشگاه پرسپولیس برای نخستین بار، طی مراسمی از مربیان بازیکن‌ساز آکادمی فوتبال باشگاه تقدیر کرد. این مراسم با حضور مدیرعامل، معاون ورزشی و مدیر آکادمی برگزار شد و از مربیانی که در سال‌های اخیر نقش مؤثری در پرورش استعدادها و معرفی بازیکنان به تیم بزرگسالان و تیم‌های ملی داشته‌اند، تجلیل به عمل آمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SorkhTimes/132647" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
روبیو:
🔻
ایالات‌متحده همچنان در حال گفتگو با ایران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/SorkhTimes/132646" target="_blank">📅 18:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
🚀
خبرگزاری فارس: مذاکرات با آمریکا به بن بست خورد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SorkhTimes/132645" target="_blank">📅 18:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vky8rIHcWpS7V2K0XjTJHb68yiN_ohuGRQFM5r5p99a11wkeY3O2v8ek1pr34djnb_IL5rGI33iNpLnwS9miskSSo3RGvHwUwQoCcUbH8UmQcIbR0GI_KZxgUYLzakwtueAtjoGPdasqKGgvuva4EwAuBbRFqECgssu6XZGBLYflMT3Pr2UAWKcU7qfjZzhJSd0Fy1AqIDEQRg9UGYohaDRNEVp3WSBBIb9mrVdoDzz8RznM5ASPZjajjFG3oKbPayftw5tYHCBaDyi09i2VXyM-IKL7YLJ9luYSRxuh_hmpH2ze5vYxYYOL79OQdVhRjeiCP9lSP_SMMLvoGBmNow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توییت مهدی روزخوش، مدیر رسانه‌ای باشگاه پرسپولیس در واکنش به صحبت های زارعی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SorkhTimes/132644" target="_blank">📅 18:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
🚀
خبرگزاری فارس: مذاکرات با آمریکا به بن بست خورد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SorkhTimes/132643" target="_blank">📅 18:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxvCENunENTakEqvKGW8k92JVZKxZWnnOJXjXfABb_DHz-1yuXPCt6XOrT77dXr1A3KxY8ZfNN1p1qXhXL7Y8x9o5QayXauHFvIvkBTH_hK0Iqbea2VIYmU4bwAIHcOgI8desFvCJy0D0xNuvcHniWxImqTNK7kLcshwT0TvAxf77WBaR_UIufsh5oBtqDbAJwPjTgAhKhk0SIuQASHinktddSmu44W6L9gzyv0wQeWrP0aMjWcMMbTMpANPp3JgiehWGDeBcjDTGdqtp3RGiROof38NwIPNsCKoxTB-GXK9yw1allWV6mSk8WdzWYwvz399y0glXqGKrWHielPztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با مثبت شدن دوپینگ یک کشتی‌گیر روس در مسابقات جهانی 2015، ایران به عنوان قهرمانی رسید و قرار است جام در رقابت‌های مغولستان به ایران تحویل داده شود اما مسئله اصلی اینجاست که ایران باید کاپ سومی که تحویل گرفته بود رو پس بده اما کاپ سوم گم شده و کسی نمیدونه کجاست
😐
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SorkhTimes/132642" target="_blank">📅 18:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132641">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
🔴
امید عالیشاه، بازیکن تیم پرسپولیس: در روزهای اخیر خبرهایی درباره سهمیه‌های آسیایی شنیده‌ام که واقعاً ناراحت‌کننده است. از همان زمانی که آتش‌بس اعلام شد، ما خواستار آغاز دوباره لیگ بودیم و حرف‌مان هم روشن است؛ نمایندگان آسیایی باید در زمین مشخص شوند، نه پشت میز. فوتبال باید برگزار شود تا تیم‌ها بتوانند حق‌شان را در زمین بگیرند، نه اینکه بیرون زمین برایشان تصمیم‌گیری شود.
🔺
واقعاً تعجب می‌کنم چرا در اردیبهشت که فرصت کافی وجود داشت، لیگ را برگزار نکردند؛ در حالی که بارها نامه زدند که مسابقات شروع می‌شود و ما هم بر اساس همین نامه‌ها تمرینات‌مان را آغاز کردیم. کشورهای منطقه هم درگیر جنگ بودند، اما لیگ‌شان را برگزار کردند. چرا ما این کار را نکردیم؟
🔺
تا جایی که می‌دانم مصطفی زارعی مسئول صدور مجوز حرفه‌ای باشگاه‌هاست و نیازی نیست درباره پرسپولیس یا نحوه انتخاب نمایندگان ایران در آسیا اظهارنظر کند. تصمیم‌گیری درباره سهمیه‌ها باید بر اساس رقابت واقعی در زمین باشد، نه حرف و تصمیم‌های بیرونی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SorkhTimes/132641" target="_blank">📅 17:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132640">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
اولین بمب تابستانی پرسپولیس؟
🔴
ادعای سایت هفت ورزشی؛ اگر اتفاق خاصی نیفتد آریا یوسفی را باید اولین بمب تابستانی باشگاه پرسپولیس برای فصل آینده لقب داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/132640" target="_blank">📅 15:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132639">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552e7d620b.mp4?token=nAkyShml6osWBSGZf2iTLKu3xaxwzGIKhEPHIeiSpAVIj64AuOCABjaGJEPiTya3FydP1gCaPkDFOcl5cSXUErSmibjWROyoy0UtJvH-RnyPLGz-NIPTctnAFXYO7zC2QarGBo_zMxNv4OBoDG88ki1rl3E9rmsvm85D975N6zQx3RzO42znDdRqQWvVnpAGdkkoolJw67ipKK546cqvCmelnM089pQgsy4sLMDVg9lwtxk4GQVgn4RM1G0vOnBD44N8VEfZ94yqpoJ51xyRrZE6xuvbEf_h00xtrRTFbs-wlGsTC35PKR29RKVDkzZ68pW6AyT80GutdRFe5x98Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552e7d620b.mp4?token=nAkyShml6osWBSGZf2iTLKu3xaxwzGIKhEPHIeiSpAVIj64AuOCABjaGJEPiTya3FydP1gCaPkDFOcl5cSXUErSmibjWROyoy0UtJvH-RnyPLGz-NIPTctnAFXYO7zC2QarGBo_zMxNv4OBoDG88ki1rl3E9rmsvm85D975N6zQx3RzO42znDdRqQWvVnpAGdkkoolJw67ipKK546cqvCmelnM089pQgsy4sLMDVg9lwtxk4GQVgn4RM1G0vOnBD44N8VEfZ94yqpoJ51xyRrZE6xuvbEf_h00xtrRTFbs-wlGsTC35PKR29RKVDkzZ68pW6AyT80GutdRFe5x98Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
واکنش مجری تلویزیون به آسیایی نشدن پرسپولیس؛ آیا یزد و سیرجان هتل 5 ستاره دارد؟ باید میانگین امتیازی سه فصل اخیر حساب شود که پرسپولیس بالاتر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/132639" target="_blank">📅 14:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132638">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
الهویی، مربی تیم ملی: امیرحسین محمودی  به دلیل مسائل غیر فوتبالی و شرایط غیر  عادی کشور از لیست تیم ملی خط خورد!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/132638" target="_blank">📅 13:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132637">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
مبارک اونایی که تن به ذلت "اینترنت پرو" ندادن. بنظرم کانفیگ فروشا باخت ندادن چون بازم برای اینستا و یوتیوبت بهشون نیاز داری و تا الانم حسابی فروختن.و اما تویی که فکر میکردی خونت رنگی تره برو با گیگی ۵۰ هزارتومنت حال کن نفس
👈
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/132637" target="_blank">📅 13:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132635">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
باشگاه پرسپولیس از زارعی شکایت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/132635" target="_blank">📅 13:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132634">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=JtG3djLRvpCTyoY_Dv-KsXYa1M7hUTtT1K3px8UtyCXBzsxkxiSCTE32pxASwlqhNUimMYGqb7mc7O9CpsFA8ZO0mrjj6SvVcUav8A9Ty27NUB64BzifYzqWZafzysfqzoJL1bXKya90zDb0nCCd2PLNiUvFEu58LDZ46pVOfZoXK7FEM69LP_oMDGXF1zw5r21TgnmsgU-tA16S0qaZVB-hogo3JycsWekUCO2lNMeypvZN27KQgu1YE6ry3k0-nXxBlSLsjMHzUMOkYFQUbmN8O3YFX6z8kFI0L3g2Cut2L9BGHz0ZOeCpSVahFzNss76OPbddJ1usCaB9R96KOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=JtG3djLRvpCTyoY_Dv-KsXYa1M7hUTtT1K3px8UtyCXBzsxkxiSCTE32pxASwlqhNUimMYGqb7mc7O9CpsFA8ZO0mrjj6SvVcUav8A9Ty27NUB64BzifYzqWZafzysfqzoJL1bXKya90zDb0nCCd2PLNiUvFEu58LDZ46pVOfZoXK7FEM69LP_oMDGXF1zw5r21TgnmsgU-tA16S0qaZVB-hogo3JycsWekUCO2lNMeypvZN27KQgu1YE6ry3k0-nXxBlSLsjMHzUMOkYFQUbmN8O3YFX6z8kFI0L3g2Cut2L9BGHz0ZOeCpSVahFzNss76OPbddJ1usCaB9R96KOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- همه اون لحظه‌ای که سایت نصفه لود میشه و VPN قاطی میکنه رو تجربه کردیم، مخصوصاً وقتی وسط بازی یا ثبت پیش‌بینی باشی.
😑
- ربات رسمی تلگرام وینکوبت کارو راحت و ورود به سایت رو آسون کرده:
👇
-
🤖
@Wincobet_bot
-
🤖
@Wincobet_bot
- برای کسایی که بیشتر وقتشون توی تلگرامه، خیلی کاربردیه.</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SorkhTimes/132634" target="_blank">📅 13:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132633">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
زارعی رئیس کمیته صدور مجوز حرفه ای :
🖍
پرسپولیس به هیچ عنوان نمی‌تواند آسیایی شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/132633" target="_blank">📅 12:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132632">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فرهیختگان: پرسپولیس از بین محمد مهدی زارع، دانیال ایری و مسعود محبی، یک مدافع رو میخواد بخره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/132632" target="_blank">📅 12:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132631">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKXXJQruLNIsGMjm5Ql_z3FWpoUFYcLW_QqPxtKaOB9xh2ia-rCeta0YoipJhEhn0WJtFEQBE5RuwSCA45-nyvtQw7TwQKtKhQFQwwap9U1mODCRlDO_QqCVpL1ZCLUgKeNdPDxVyVpJgU8C7j5T1yqxS7WdqzeHKsRH4KXWv_ez9GhuHj4sH1riCcVz8P2xuE11H0sgMebTt21Omh6Li9JwEA-jjMHkEyyLpbyppoEZrk5N8tYnu0rR-yyKMmhD3o4L3C0wwrW7SU21mvWeZKo-7x9DcW90q75Gs8gNdJIZ9xkBz5_lKY5SpXQaFn7oxFfnKM4gb_LCCRNIKFdT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه شایعاتی منتشر شده که اوسمار
شاید برنگرده و جدا بشه که امیدوارم دروغ باشه وگرنه دوباره وارد دور باطل عوض کردن سرمربی می‌افتیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/132631" target="_blank">📅 12:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132630">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gE0zUKzv8mnErpYho9Ty9dZZNo9XaGxA-T-Z-bb1r_3XMrL2cBFUpvXaOe_bQIyScIQYgLFDBK29u6TqCGXIZGFfpbCvRcXw36T-9Szk1RMwUB7zsTgvjtbaCCuOiG3wyWXgCRUrmT4-g2dlxwurb_9B5klt_33NJXmNFr1NVNb3LRM73JPny_sqln2wBWlaV5nxz2ZLEStwzd9XGaIfPbNwSliN4GNv1yKQwvk5nHWvyW4kxcGrXlFS48ngIR4GYXTHPXNUdmtY4_ty2-sZTLmhJ_jQhDCmIpLOHGhCLDKYiiu1gZ0F7AzbTAF4uvEgGnKzMr0a21UbTAXwiifoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
مدرسه پیرمردها رو نوسازی کنید.
🔴
#فرهیختگان
: پرسپولیس با ۸ بازیکن بالای ۳۰ سال و میانکین سنی ۲۷/۶ پیرترین تیم لیگ برتر شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/132630" target="_blank">📅 12:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132629">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
اوستون اورونوف و ایگور سرگیف در لیست نهایی ازبکستان برای جام‌جهانی قرار گرفتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/132629" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132627">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
سر تیتر روزنامه‌ گل   پ.ن پرسپولیس از خودت شاکی باش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/132627" target="_blank">📅 10:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132626">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBOnNs11iGW8BsUjsuc791yECAzZOMNowR9WC-1seBqZ5_r2axADHKks0XIoxa0lIeb5RKI1nNea7iOKTCZoZpaQ1zo2H-sT-z-0YW8G3t_YRRYaoe6T2tozu739r-xUZAxNHRz2dMEjO0kJdEOIfxbpF2AsLDKSRKzq2pcFbr-QpWvR7ThYJ0sIifXRsWr_GlZ_ACt-AUhGkIMuYhlO6cUhJvN7F-yj1V3hMavJ8eNR4TkflSVtIhfKkHGUH_3foTUHGt9H5qS6AF8j1fli5Q8-x9aDUGziBXPBy7ICma9CaDe9sr1sBivlBvuhlA6SMU6ss5USDgWqD5i3WIL62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سر تیتر روزنامه‌ گل
پ.ن پرسپولیس از خودت شاکی باش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/132626" target="_blank">📅 10:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132625">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
تسنیم: مطابق جدول فعلی گل‌گهر، چادرملو و پرسپولیس در رده‌های چهارم تا ششم قرار دارند، تورنمنتی برگزار خواهد شد تا تکلیف سهمیه سوم و جایگزین سپاهان روشن بشود
🔴
مشابه این اتفاق در پایین جدول نیز اتفاق می‌افتد و قرار است تورنمنت چند جانبه‌ای برگزار شود تا دو…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/132625" target="_blank">📅 10:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132624">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/132624" target="_blank">📅 10:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132623">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=BX0--y8GIbOrS51Y50tAPU0iRkO6CR_AYxbOAYy34pUKNTXAZi0WCIpWZZNTCgqlEpse_7p8ppt9LHFdxVqWxKLvXYUyOXQM1KRIcymwXFg9KDxc_DVY86cdd67QfZYfFOSMO9L8910kb_VgaQTVKPb2AXpUetIZyU-1D5RmIGiUG7XP8UC1VqxvMpyp6Pr0ZuC17R2aZzaMUUr-W5nvd_Y0DEJsDitrM9YzaHBXiXsJlmOKCRj-Mk9qEpGTffi_CI7dT7M0jVbS2F24CJhxh4CblFcyqxGK8RakLS8_MQIilXSNYAAcuWMtFm77Dhkj1rTAPrPO079E2Q7vwKu3Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=BX0--y8GIbOrS51Y50tAPU0iRkO6CR_AYxbOAYy34pUKNTXAZi0WCIpWZZNTCgqlEpse_7p8ppt9LHFdxVqWxKLvXYUyOXQM1KRIcymwXFg9KDxc_DVY86cdd67QfZYfFOSMO9L8910kb_VgaQTVKPb2AXpUetIZyU-1D5RmIGiUG7XP8UC1VqxvMpyp6Pr0ZuC17R2aZzaMUUr-W5nvd_Y0DEJsDitrM9YzaHBXiXsJlmOKCRj-Mk9qEpGTffi_CI7dT7M0jVbS2F24CJhxh4CblFcyqxGK8RakLS8_MQIilXSNYAAcuWMtFm77Dhkj1rTAPrPO079E2Q7vwKu3Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132623" target="_blank">📅 01:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132622">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
تاج: هیچ مشکلی برای صدور ویزا نخواهیم داشت
بخش چهارم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132622" target="_blank">📅 00:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132621">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
برنامه های تیم ملی تا شروع جام جهانی از زبان تاج
🔴
بخش دوم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/132621" target="_blank">📅 00:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132620">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
فدراسیون فوتبال: در صورت تمایل امیرحسین محمودی رو جهت حفظ روحیه بر خودمون میبریم مکزیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132620" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132619">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28a044344.mp4?token=baIdN7uDARGxSopbV4-xvKRM448siDxunmz_-9zGMFQ3jTZfTOzWYKk5IW-YL28OEHLgp_PV__RoYUn6CMebw_98HDR1uTMJxuCwFV8XFyBrZk376FY-Ci8z-7JUne5qCP3dw70b1rC2V27AmHtEFzPAlezgRbX6OEoD6GZJ_txJzLZSSpeoZiFfnETKf1edJH_yhK1LLYiyaB8FZw3eVxgWEmqsOy0cBqyVH_npjjL6SaLh4gTcTyCnd7hO3Is814EAVgss6osGURKBO3FMVIGUUqcLtTEmtJ2srJO1MdB_0xqfZBxr9U1ItXWUPp-Ln3i0IIPS_enCQcFqnmVJ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28a044344.mp4?token=baIdN7uDARGxSopbV4-xvKRM448siDxunmz_-9zGMFQ3jTZfTOzWYKk5IW-YL28OEHLgp_PV__RoYUn6CMebw_98HDR1uTMJxuCwFV8XFyBrZk376FY-Ci8z-7JUne5qCP3dw70b1rC2V27AmHtEFzPAlezgRbX6OEoD6GZJ_txJzLZSSpeoZiFfnETKf1edJH_yhK1LLYiyaB8FZw3eVxgWEmqsOy0cBqyVH_npjjL6SaLh4gTcTyCnd7hO3Is814EAVgss6osGURKBO3FMVIGUUqcLtTEmtJ2srJO1MdB_0xqfZBxr9U1ItXWUPp-Ln3i0IIPS_enCQcFqnmVJ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
واکنش تاج به ناامن بودن شهر تیخوانا: کاری به مواد فروش‌های مکزیک نداریم و نمی‌خواهیم هم اصلاحشان کنیم!
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/132619" target="_blank">📅 00:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132618">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2531fbac09.mp4?token=o4ZslVOOsMhsc00lARpJLsMosMHmoB-15KTuCvG9JYbpCBThykVT9Z0TMY3HphcvCcOokEuZ5SRcSW26TBm0RnlGEJ3FReiYwG4W-XyR2qD6i5DMW4XWAFfzClB7ucjxp1vTsNn20MhzP_I7Ij9pYJR9cheTibhf9uRvzqfWZQHQKmJMVXtveIyTfs01Kn4LKQrEqevjSgN64ZUdnF67mRfFSHo6IEQdvt0ioj5W7EiDUIgQf-y6vPowwGcD5e4z5LolJbHC4NtKsgGlJRrdAaAR3TKtDgYbj_VxlJ2ONkyqnfD8aEQ05zxHR7xvA96FU-NrG-klqF0RODFI9q96MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2531fbac09.mp4?token=o4ZslVOOsMhsc00lARpJLsMosMHmoB-15KTuCvG9JYbpCBThykVT9Z0TMY3HphcvCcOokEuZ5SRcSW26TBm0RnlGEJ3FReiYwG4W-XyR2qD6i5DMW4XWAFfzClB7ucjxp1vTsNn20MhzP_I7Ij9pYJR9cheTibhf9uRvzqfWZQHQKmJMVXtveIyTfs01Kn4LKQrEqevjSgN64ZUdnF67mRfFSHo6IEQdvt0ioj5W7EiDUIgQf-y6vPowwGcD5e4z5LolJbHC4NtKsgGlJRrdAaAR3TKtDgYbj_VxlJ2ONkyqnfD8aEQ05zxHR7xvA96FU-NrG-klqF0RODFI9q96MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
با اعلام تاج امیرحسین محمودی و مابقی خط خورده ها راهی جام جهانی میشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132618" target="_blank">📅 00:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132616">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988a98ef48.mp4?token=p114WB5nUaNpClavtnC0e5AePJoSj1IEt24Pj98lObIwKw_NYSvtjPyzVLmLYM0wcQLoP88YH5V5DMkN3WOFLfIbeX_0WcRhAYmm2WSmvqdjjcd-qXEu7AqQihyA4ATPiIM29a1nq2SGTimoQuV29Vh0c6DjreNFAvW7XNu5JNxIkajVDQwjNM_cX4drjkMzdNVWU2Qf_MazAOMRy_NEMMRZA2hvgG2wa9W8afTEkEPD1reXCBIf4BbjH9xsh35B-VrIuKs9N8mqIrSQlp2_SBflgM-yhPUGxp_WNvi7DwHeJ-KHUqQ5t3RNYl3-xfY85uaficqIjGittiZ9b8A9Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988a98ef48.mp4?token=p114WB5nUaNpClavtnC0e5AePJoSj1IEt24Pj98lObIwKw_NYSvtjPyzVLmLYM0wcQLoP88YH5V5DMkN3WOFLfIbeX_0WcRhAYmm2WSmvqdjjcd-qXEu7AqQihyA4ATPiIM29a1nq2SGTimoQuV29Vh0c6DjreNFAvW7XNu5JNxIkajVDQwjNM_cX4drjkMzdNVWU2Qf_MazAOMRy_NEMMRZA2hvgG2wa9W8afTEkEPD1reXCBIf4BbjH9xsh35B-VrIuKs9N8mqIrSQlp2_SBflgM-yhPUGxp_WNvi7DwHeJ-KHUqQ5t3RNYl3-xfY85uaficqIjGittiZ9b8A9Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تاج: ۱۰۰ هزار دلار به مالی برای بازی دوستانه پول دادیم؛ هزینه پرواز و هتل‌شان را هم پرداخت کردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/132616" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132615">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/132615" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132614">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🟥
بانک شهر طی اطلاعیه‌ای از تاسیس نئوبانک جدیدش به نام (رد بانک) خبر داد که تمامی منافع این بانک متعلق به پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/132614" target="_blank">📅 00:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132613">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e411950a.mp4?token=naYCNpqz1aE7oSBpgwDwjp9xafk8NLlB9xGedT8vEWJxUJonoQgdPPD7eNuFuMOkOn8ceWxDiurtM6CFVb1NphkuZiad3Z3Ysqa4Lxdd9NTi4cdrXe4IyzLNWjqQJn5zrea_lE989mUSk3KFX2L-Cgmi3adRGnFSOXgBRADJR9FthN-OHETNbksibsjuFmIm-RAgv6E1ojgu_vru1cetm-hFqjNc_AyrZfZSWNM_IU0N5synTRanxW6Ox2mZg7OaOIh-bcDvdG9QMXNmaeYk7WLWE-DvR0h7Zurb4_QAklOkt0mGu3KcckfyoNLG4TgJz5w-DdneVyJfVswwR1nHhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e411950a.mp4?token=naYCNpqz1aE7oSBpgwDwjp9xafk8NLlB9xGedT8vEWJxUJonoQgdPPD7eNuFuMOkOn8ceWxDiurtM6CFVb1NphkuZiad3Z3Ysqa4Lxdd9NTi4cdrXe4IyzLNWjqQJn5zrea_lE989mUSk3KFX2L-Cgmi3adRGnFSOXgBRADJR9FthN-OHETNbksibsjuFmIm-RAgv6E1ojgu_vru1cetm-hFqjNc_AyrZfZSWNM_IU0N5synTRanxW6Ox2mZg7OaOIh-bcDvdG9QMXNmaeYk7WLWE-DvR0h7Zurb4_QAklOkt0mGu3KcckfyoNLG4TgJz5w-DdneVyJfVswwR1nHhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مسن‌ترین تیم‌های حاضر در جام‌جهانی؛ ایران در رتبه سوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132613" target="_blank">📅 23:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132612">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
حدادی مدیرعامل باشگاه پرسپولیس: سروش رفیعی همچنان بازیکن تیم پرسپولیس است و با شروع تمرینات باید در تمرین حضور داشته باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/132612" target="_blank">📅 23:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132611">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:   «مذاکرات با جمهوری اسلامی ایران با سرعت زیادی داره ادامه پیدا می‌کنه. از توجه شما به این موضوع ممنونم! — دونالد جی. ترامپ»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132611" target="_blank">📅 23:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132610">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inWUl5acQ1BUFfyMN6IP8rJojTUysWzfBOBgmfEYxMOZTVy5uB5P-Jtt9zfffc2QQnRvczIMVmtr7aIpEXZJ5OQiI8p_uK2QtrO3jJRCjDmIoPIzAv2gDhGG7OGM8Jf7n2lhJXSp0F6Onhb0GAm2ceBxdgzHn_oqz1TtptmzGH3_LsivDugC47Pzn50HaeAw5tbqBCLJW2itfKAmrJtcJi2m6ayWwHxlA8yTnsALpHCVht-CbSKn4c7v4f0M0bwfL2wGu8IueDbTIj1NRSQnM0_4RDltx9Duu24liRMeaZMJUJpACBuR479x1Zf4aboaToyNkP9FogtkZUfP5rkzHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
بانک شهر طی اطلاعیه‌ای از تاسیس نئوبانک جدیدش به نام (رد بانک) خبر داد که تمامی منافع این بانک متعلق به پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132610" target="_blank">📅 22:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132609">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6LElCC9wjknDCRssu24HjqkOuXJzOJfk_mgQK1vVjxMYdPH9becoyMtMK9TH5-Cw-qpgs4SoNxzYXsQCFJ12YdB1IafWjcXD4xhjUsTZyCO2KgirthpN7yxiFdV5ZVGUnxDdOE98rrYvAbLOLw8CHqEKbiza-om9dXGpbM2sYoi2kEqd5oYnbBhPG-A26-mTfGD1W7e_1YNJOXIKS7rnDNlmHFvqjxanmWrcagUVpuVBsshv6hkfUbYNsqnSym-wzCuVpRYU7LX-dD-ayJd02rlDans-sAslwaRXMdNsy_DwX4DaGMI4Abtom5TpbhO-K9BXe2jVovd91WJFoswZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
«مذاکرات با جمهوری اسلامی ایران با سرعت زیادی داره ادامه پیدا می‌کنه. از توجه شما به این موضوع ممنونم!
— دونالد جی. ترامپ»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/132609" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132608">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🟡
سپاهان حذف شد
▫️
گل‌گهر یک بازی اضافه داره
🔸
چادرملو از بازیکن غیرمجاز استفاده کرده
🔴
پرسپولیس برای ۳ امتیاز بازی با ملوان شکایت کرده
⁉️
باید دیگه چه تصمیمی گرفته میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132608" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132606">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
هوشنگ نصیرزاده، وکیل بیرانوند در دادگاه CAS: چه قبل و چه بعد از جام جهانی هیچ چیزی بیرانوند را تهدید نمی‌کند. اغوایی توسط تراکتور انجام نشده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/132606" target="_blank">📅 21:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132605">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">💢
ترامپ: من یک تماس بسیار سازنده با نخست‌وزیر بی‌بی نتانیاهو، از اسرائیل، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد، و هر نیرویی که در راه بود، قبلاً بازگردانده شده. همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت کردن…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132605" target="_blank">📅 21:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132604">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BO6d_gDQhNodGbM6sP60p5rh3R3LGdbIZFAnN-d00pupoRVZnIwHWkUr_E88WVKPik3sVdOW510f_uZma4jhhweDLU0o9R01tcSNMK-FPihOofWZVagEF1iJq1u90lc-O8KQgrDYz7PlDBLHzY3ecZfDP2Wp8VbMtmWyKIJIHn4dHLBBDayht4FsGsLfs6acuZlHtgt0jnYWd5HTjV9ir8to_zBPvbIwi4e6OIBzas4kNtC0Sg3Yyr0RLkaos2acS9b8cYHZfyMzleZm5ZvPXQUpBAGZUPf7GfWH3uIz80L8Na7BmjIIuLfeivmVY-6k23r0dYckkl05NiaoVZI63w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
ترامپ: من یک تماس بسیار سازنده با نخست‌وزیر بی‌بی نتانیاهو، از اسرائیل، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد، و هر نیرویی که در راه بود، قبلاً بازگردانده شده. همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت کردن که تمام تیراندازی‌ها متوقف بشه؛ اسرائیل به آنها حمله نخواهد کرد و آنها هم به اسرائیل حمله نخواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132604" target="_blank">📅 21:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132603">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
ایسنا: احتمال برکناری محسن خلیلی از پرسپولیس وجود دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132603" target="_blank">📅 21:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132602">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فرهیختگان: پرسپولیس از بین محمد مهدی زارع، دانیال ایری و مسعود محبی، یک مدافع رو میخواد بخره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132602" target="_blank">📅 21:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132601">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
لیست خرید اوسمار به نقل از فوتبالی:
🔴
اوسمار برای هر پست ۳ تا گزینه معرفی کرده و حتی اولویت‌بندی هم کرده
✅
دفاع راست
✅
دفاع میانی
✅
هافبک
✅
دفاع چپ
✅
مهاجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes ‌</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132601" target="_blank">📅 21:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132600">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
از جدول ناتمام تا شهرهایی که آماده میزبانی در آسیا نیستند
‼️
چرا میزبانی این دوره از تیم‌ها در قاره کهن امسال برای فوتبال ایران مهم است؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/132600" target="_blank">📅 20:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132599">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK2iL8n-WHa5E0qBkWGpYHCaaRQafg5joQ7cB0AHmRTBx7qEnzNQymkEB96m60ST5y6tket9f-wSWAe2dCvalGl1VbIIZj_0tkgSn1hMIWs3NkAQNGEQ05ZDv5ufO5x9GvJ6h3IYDcHWweHQo8Pk4hZlWohSr-SKNdisqs_aiVDu8Sn1wAeAqyilYwZRWt9cqklLTb-6eEnyAHjXvMhTpSxTRspuLXWqS9sBdyY1yRVYgCJVoxyY-5arqdEz2Op1IE63Qlx09VyzXpFi-C8kc42osc4Q7ACWo1FhlU9Er94yNTAA129YiJrQs44oE0IH5LmBFGlLFNoMauiUCpq8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/132599" target="_blank">📅 20:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132598">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
محسن خلیلی: باشگاه پرسپولیس حق دارد از حق و حقوق خود به هر طریقی دفاع کند
◻️
متأسفانه در روزهای اخیر شاهد آن هستیم که برخی افراد از طریق مصاحبه‌های رسانه‌ای و به صورت غیررسمی درباره نمایندگان ایران در مسابقات آسیایی اظهارنظر می‌کنند. این درحالی است که طبق…</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/132598" target="_blank">📅 20:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132596">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚩
ترامپ: فقط ۲ چیز از ایران میخوام، تنگه رو باز کنن و بمب اتم نسازن، بعد ما میریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/132596" target="_blank">📅 20:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132595">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejCySO6lgwY8zU76wHNsoyR5snjDXvzV_jNm2Sd2JwFw89_LihwjynqfLhY0K8NGePrIhsBVE4NkEB8oGqLxaVmWOMvhq8JNz7GwcY38jNDYkDRayDuLfy0HldrxGtdUw-85IDX5Aoq0iCSxD1OU4dKdUmQqo6TNb-aUrXojrrOoPEBG01vrCxzO16eBFAGIiy4AOk9wLzDqcPyXJ9JkTB3EjE14BtWy0ZttMoV3sUWPkrIDNwRI46K6MUbpNmZQICmW64tMnjP8Vx3zvkEq9L5Kf6ZFEcZvAHHYV8KAsu66WQlwN8nVY7FMnzjcOGYYqc_r5ujsBtkPUjvyHza5bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
آندرس اینیستا با قراردادی 2 ساله سرمربی گلف یونایتد امارات شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/132595" target="_blank">📅 19:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132594">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a1bce686.mp4?token=azWmixJ4a5vEIJ2qgkNRyq4KmQAr65zY08Zx6WlBE8P1b5qxLxgLmQMZqH_kologZb9UUrbRuJ2hP_D21m-Oh38I4YLSIEMkRfEwh7evozY05WCmch5pH5RzDkV0czGEjbUKaFeQn_SP19QpkUQEvMsc1X7FOlrm_E3RC1LpZKJDt5kHPk7HqfUUBgd46dRGR0P3Ue_mNCcRDWagOUaDjaHObK8QYf3cusHAsHfD9nkirBvGtTPpG5SdYE-ofqHkvpBuTM0y0QisOrUZWsK5nPJvTktCq42cwKihEiLgxxR7o4Wg7yrWoWEw8ZSvjPkcE1K5g9HU6kIa-X-eFQGjiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a1bce686.mp4?token=azWmixJ4a5vEIJ2qgkNRyq4KmQAr65zY08Zx6WlBE8P1b5qxLxgLmQMZqH_kologZb9UUrbRuJ2hP_D21m-Oh38I4YLSIEMkRfEwh7evozY05WCmch5pH5RzDkV0czGEjbUKaFeQn_SP19QpkUQEvMsc1X7FOlrm_E3RC1LpZKJDt5kHPk7HqfUUBgd46dRGR0P3Ue_mNCcRDWagOUaDjaHObK8QYf3cusHAsHfD9nkirBvGtTPpG5SdYE-ofqHkvpBuTM0y0QisOrUZWsK5nPJvTktCq42cwKihEiLgxxR7o4Wg7yrWoWEw8ZSvjPkcE1K5g9HU6kIa-X-eFQGjiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دو سال پیش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/132594" target="_blank">📅 18:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132593">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132593" target="_blank">📅 18:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132592">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
مهدی لیموچی با ارسال درخواست رسمی به باشگاه سپاهان، خواهان فسخ قراردادش با این تیم شد.///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/132592" target="_blank">📅 18:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132591">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/132591" target="_blank">📅 16:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132590">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132590" target="_blank">📅 16:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132588">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
خب سپاهان که مجوز نگرفت. گل‌گهر هم بازی اضافی‌ش حذف میشه و چادرملو هم فاکتورهای لازم برای مجوز AFC رو نداره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132588" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132587">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/132587" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132586">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/132586" target="_blank">📅 15:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132585">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiplZEngla9DpfkQGqdtMzLFk4rFtS2XBigvtCUVml-fyjEfWpwurnU8D84_Bf5HPKnp_Z26EGQrwtjUa4gk5w0NaY6v9Qhiny6IumjsHp9kh1M1xal2jfE1qIQ9Z98K_5ZOQdgbN8wnbn5RMG-sVqRzHH96BNKv-w_Hw8Rn8Wk1ZU44K1Gqo_XdPtSNRUDslTzRGRIJgxo_4WrDMDr88Pi3uL8wnUAmxtQGWPwR6azFEaPerhGbMWMxY-zA_sFxBLua_sRprQUvAHRLWusA5HDDuJdAWfIlXrvVnTE0RxesR4Qh8XMMaL6ijZs6jT1snSYEYRFhoVb8CUYGT3qeig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132585" target="_blank">📅 15:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132584">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmYYrnpVBrPfDaxG6NXCVna6uZUit8NQ7Y0VRCMS4x7Ok7DORv7Rq-1bZfa6t-VputTBPfOg0Kt8vA-cb4QuM4UAp0_2nkMvi8qf1gYY5CPVreCWGIiBY7zHPAVrO0dsZYuBG1GJxiNi2zq-dons7AQ7kuBbw0nfsDg8OXZ2AIP-7BbJuxTaTIubTfsDjwSJBjKZnzaVkhcQIyQzajAQ3MjhvE5-4tYs8Ogy3x1ZtwRGL7z3VLaLFHUgHKyLg_HqdjRcKd66BulBqbzWdIu4ovHZB16xT5-i9lNLBQxeamWF8WbRCb_D_JPJ_19pCnQt9HXC22yesrL9_HpWV4MjAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مراسم معارفه مصطفی میر ابوالحسنی به عنوان مدیر جدید حراست باشگاه پرسپولیس با حضور پیمان حدادی، برگزار شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132584" target="_blank">📅 14:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132583">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky4Hgysm_DGa8epWNeg1LNGNThaxg24itvKNw-vh3eXUtPEXNbXr6_SnrFQpe8QuWnkvcX6BFOVZxV75v9q7EHWbcou9BBTxI3tEkSf8inrMJx-My0yUbNHsGMrDpbS_YBOfSWzPUgt9Lrrlh67aGAQ8pBVY7_Lc21lXL8hOSfru3Dl3jbEs7Q8ln5d6NmnUdh6gwMrngTN3qig5WGQa42gaUTCZZPH0tx6_9jdwe9AemdLOziutnrcYNkymB9DVJ0-UyCrcTpPGCQdQ3Pq6pnkiBXVHYNy_POKa_Efqq_aBuytIFfTMxBW8FLVyue8d6_HV-hKgzAwyq7tfxD0O2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/132583" target="_blank">📅 14:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132582">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
لیست مازاد فعلی پرسپولیس به ادعای تسنیم:
🚨
سروش، پورعلی‌گنجی، سرلک، بیفوما و گرا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132582" target="_blank">📅 14:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132581">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: افشین پیروانی قرار بود به یک کشور دیگر برود نه آمریکا/ او برای رفتن به سفر از من اجازه نگرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132581" target="_blank">📅 14:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132580">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
فووووووووری
🚨
شانس پرسپولیس برای آسیایی شدن زیاد شده و ممکنه با تبصره ماده پرسپولیس راهی آسیا بشه/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/132580" target="_blank">📅 14:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132578">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZTAyxuD7IY6Z-ZWYbWeCnwYyjbbDelfmMYYHaAuJJXiBWLH5uBNdegCSWJC0E9Thwji_CAskIz43pKjFX2EUJPJ2yyUFn4Jaa73nxMVfECwUiwwDi_jy6pnulTPQ20QiYqZKd9jW0AzMlzVftg3P4Z4pPVYjVlohuRsc_z_03nMznzRtleKf0Kh2UI9ja3aFXpRLMrgUwz8qHCwxMOh0L3RgHIPCWUm4ldaUqXnxkuCM_nj3-SnIq_0bkz-ZPNgIgljBCgav2un07L0VmdhLTFqHL8xmt_wEQTMmXOhiLgV73a6UrvEsIz0Z0JMMpwrcqB38bzUueOZVT2DmQneCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💭
تقویم مسابقات جام جهانی ۲۰۲۶ در ماه ژوئن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132578" target="_blank">📅 13:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132576">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPvb_CiHl40UcHtAVytx_y38LxoASkTjrqu4d200EKzoE9rkRkaZ0YvWaYlPPZNIkLujd3lxldGUHS1uzOIn_B3z7Vpnh5lbeDOdeEexUwzeiyZmLpO8SpO8vLYOybkRD5CTld0eq52niUQ1vqWIThZe8q0TYVM6-DQCjOKCHl5PZe1Kuy2A20XcD3pj3Js9nxtXhSfleWFJwAeYZDBDGdKv3_ZoXERvCNXs1Z3Yqm47ye_6_gU-Yz6Jhw0NuLNUyexnZ4H2twoItax2H2qoZ7P17m6P9elWKJUizXrwNTQ0pLCZhFj3LFbrGFddXEI6rjCa104KxpyLGh9Fngu2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه سال پیش توی همچین روزهایی؛ پرسپولیس قهرمان لیگ برتر شده بود
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/132576" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132575">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFh3ahls96Z6NI58bFfT6h0C5I9o5VoQ-SLnTl97oK23EiS96wzPBri6VrxP4J1NlMQyvkRIn2mpib9XHoh8h_de6jDfh7rkOeljkvCUtBjlmunQhi7EYZtsICljNYPfh16MPItS7QicL7vuvJsPW8L5me_XYZJeO-8Tu-4DoTLr5UNiIyQvkyEONLL0-rb_VIeB0sUx0AoKfa2j2SxFVLEQs4jmfJv47jrwVccEV36iX4peLXp-JYDkaGNuYRup2T2lFF-k9VAierdM3vTCC7XXzEdsp2J27_4DEkEEfP6b6e3DzNeyqDgLgsbffh1ZZVWTTZ2oNAtI7hs9ykwiag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
❌
۲ پرسپولیسی در آستانه خط خوردن از تیم ملی
⏺
شنیده می‌شود حضور پیام نیازمند، محمد حسین کنعانی‌زادگان و میلاد محمدی در لیست نهایی تیم ملی برای حضور در جام جهانی قطعی شده اما این احتمال وجود دارد که از بین علی علیپور یا امیرحسین محمودی یک یا دو نفر از لیست نهایی تیم ملی خط بخورند.
✍
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/132575" target="_blank">📅 11:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132574">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD_DsYVUC_VSPPDqTU9yUTkEtvzRxOiiuHLIJwsGWh-f54Ht-lGT0LDLMCMh88Ag8iocb7Fzrxy6CdtTu4NqP8wnpNfvPSgmRdcNphkrO7ajdK6ki-is3GYY-SI95MDZl59t5-hch0Xzxv109oxMReoEGU_Z5YfMzk7nAWrXU_RhvwCNuF6KtHzJ_GiaIYcqLp0gEHHckTflx6AYd0dnCafRIOR8CXF_knviag5i4qJmywohgdSfr-OaZ7u5oXuljox8dBaxsBG6mlMziSbi-sWruxvMrIAQiYSWuAnbw0g9KZCWkLYSv0CANbEHPo9P9vV8RuZKldkQihMlsZV43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست خرید اوسمار به نقل از فوتبالی:
🔴
اوسمار برای هر پست ۳ تا گزینه معرفی کرده و حتی اولویت‌بندی هم کرده
✅
دفاع راست
✅
دفاع میانی
✅
هافبک
✅
دفاع چپ
✅
مهاجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
‌</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/132574" target="_blank">📅 10:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132573">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
ایرنا: مدیران باشگاه تراکتور با مرتضی پورعلی‌گنجی، مدافع پرسپولیس، برای انتقال تماس گرفته‌اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132573" target="_blank">📅 10:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132572">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/132572" target="_blank">📅 09:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132571">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLar6oY9KG-Eux2Pt3NKslCen8nsDoREODE4UWcfrhEe6Z6DxS9WGCsZpiUZbXOJGf_fpesRG54i625Zk_qMxDFIRgGkrKa7OSCUbFNXGxaMMK4Ys01fIY-WZS2VSz2kdBdctfCql9uJmUQFvODPRCQkrBM0k-q5OB4OobWYUZwRVO5pyZj_MiqxI5oCc7bkyYz_dyJTmqppET6-iDukKum2PwuEAoFtunoC4lJ2lBqTmoGUnSYH9zNTo36NqqOOwnfFygfB7q4up9L4s9yVNurk_Y8EQtTnuxmeTP944Bx_sWnjewEvzNsrWgX2rmKxhnZyt9tZo9Dfjfn3IO4elg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
‼️
هواداران پرسپولیس حواسشان باشد؛
🔺
برخی ایجنت‌های نزدیک به اوسمار در هفته‌های اخیر فعالیت رسانه‌ای خود را افزایش داده‌اند و گفته می‌شود با استفاده از بعضی کانال‌های تلگرامی در تلاش هستند فضای باشگاه را تحت تأثیر قرار دهند و زمینه را برای جذب بازیکنان مدنظر خود فراهم کنند.
🔺
بر اساس برخی شنیده‌ها، این جریان رسانه‌ای از همین حالا کلید خورده و هدف آن ایجاد فشار روی مدیریت باشگاه در آستانه تصمیمات مهم نقل‌وانتقالاتی است. به همین دلیل احتمال می‌رود در روزها و هفته‌های آینده شاهد افزایش شایعات، اخبار جهت‌دار و حاشیه‌سازی‌های مختلف پیرامون پرسپولیس باشیم.
🔺
هواداران باید با دقت بیشتری اخبار نقل‌وانتقالات را دنبال کنند و هر خبر یا شایعه‌ای را بدون بررسی منبع و اعتبار آن نپذیرند؛ چرا که در چنین مقاطعی معمولاً منافع برخی واسطه‌ها و ایجنت‌ها با منافع باشگاه و هواداران همسو نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132571" target="_blank">📅 09:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132570">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
سپاه پاسداران انقلاب اسلامی دقایقی پیش به کویت حمله موشکی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132570" target="_blank">📅 09:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132569">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
به تیم ملی جمهوری اسلامی واسه جام جهانی قراره ویزای ساعتی بدن یعنی واسه هر بازی چند ساعت ویزا میدن بیان بازی کنن بعد سریع باید برگردن مکزیک تازه این ویزا فقط برای بازیکنان و کادر فنی صادر میشه نه افراد دیگه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/132569" target="_blank">📅 09:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132568">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NK1BK_U-5BecyNjt__BJnowzMcr7UZe7Rq_4AUKdD2kSHbMEw-ccGQd0bUjIPVctQo4Bl3vx-2lO1lomUu5nF6r9VatZ5F8n-cShyn01DuXbbZI9v9-vHChW7vnMydcVleSmKtJBSUcrpbdJN_CRdGfx6yNvSCtHAhsE1Xsg68frk1nxWagbgIWBRkzYQsmdkfE8A9oCM0c2YhVLMOptFZ4GzpjYEgw6uVfLOUnqw04o1vcmq3rdLJm1zJs8uplB9sgVruvGykjJmfwKWX8QcmeyeuRZNNEmpfAZC9uhq3XWiTSVKu-gRgtwa7qxg5uxUYSlU5bpASIHt-aPoATjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132568" target="_blank">📅 01:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132567">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132567" target="_blank">📅 01:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132566">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaMcLldpe_JjpgGb0g_hldgfKdiFR68b80aTTjpd6ApY0kg4E7yiXtLYlzyJI7lp5gqPFBHsc4X_eIEG-9rxJw7g7G_pI1qbE4Q1BzlZYsgfj1a52cS42X29ibVhZkGLBVHeXwVz1VJuLA7Ru1ANnj_FaSdMwNDzqcFVf16OoBodFhoh1A59F9AzqeMctzedB0SuIoKRtpxvAZSxzOXUFK_KciF6ob6T9flijfEYyozoL_FgkhhTKzF6xFy7Ns3n6d1dF5uCMc5XCBSBeuiUECimDMxQUi_73wOqFRNbqZ94UyKRbaSE01X5e89oDVbxqWROgmqQze1LSAN9bT40yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یه سایت هوش مصنوعی اومده تیم های صعود کننده به مرحله بعدی جام جهانی رو معرفی کرده که تو اینا ایران تو گروه خودش دوم میشه و بالاتر از مصر به دور حذفی صعود می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/132566" target="_blank">📅 01:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132565">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⛔️
پلیس مکزیک گفته بازیکن های تیم ملی بعداز ساعت ۸ شب بیرون نرن چون ممکنه لولو بخورتشون..
😂
🤧
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/132565" target="_blank">📅 00:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132564">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚪️
مهدی تاج:
فدراسیون فوتبال دارد تلاش میکند که سپاهان از آسیا کنار نرود و اگر سپاهان نتواند پنجره‌اش را باز کند طبق روال جدول لیگ نماینده ایران به آسیا معرفی میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/132564" target="_blank">📅 00:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132561">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
شنیده ها :مدیران باشگاه پرسپولیس با مدیران‌دوتیم چادرملو اردکان و گل گهر سیرجان تماس‌ گرفته‌اند تا رضایت این دو باشگاه رو برای رفتن سرخپوشان به آسیا بدست بیاورند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/132561" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132560">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
لیست مازاد فعلی پرسپولیس به ادعای تسنیم:
🚨
سروش، پورعلی‌گنجی، سرلک، بیفوما و گرا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/132560" target="_blank">📅 22:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132559">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
خب سپاهان که مجوز نگرفت. گل‌گهر هم بازی اضافی‌ش حذف میشه و چادرملو هم فاکتورهای لازم برای مجوز AFC رو نداره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/132559" target="_blank">📅 22:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132558">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
امید فهمی مهاجم جوان سابق پرسپولیس به پیکان پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/132558" target="_blank">📅 21:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132557">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
خبرگزاری فوتبالی: استقلال داره لابی میکنه که قهرمان لیگ اعلام شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/132557" target="_blank">📅 21:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132556">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
ترامپ: بهتر بود اصلاً وارد ماجرای ایران نمی شدیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/132556" target="_blank">📅 21:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132554">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
اگه تمام نماینده های پرسپولیس در لیست تیم ملی برای جام جهانی باشند چقدر پول گیر پرسپولیس میاد
⁉️
🔴
نماینده های پرسپولیس : اورونوف - سرگیف - نیازمند - کنعانی - ابرقویی - محمدی - علیپور - محمودی
🔴
یکسری از رسانه میگن که الکسی گندوز هم اگه بره جام جهانی پاداش…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/132554" target="_blank">📅 20:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132553">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
ادعای نیمکت نیوز : مهدی لیموچی امروز درخواست فسخ با سپاهان رو داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/132553" target="_blank">📅 20:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132552">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
توییت پزشکیان بعد از خبر اعلام استعفای آن توسط اینترنشنال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/132552" target="_blank">📅 20:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132551">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAl4P0g_G1VWJTp6aAHEEaTUTI1bxinakb1AHRvI1LvEeR9avQZJLy7DrSLsu28Hp_t5s-B8wxlYgZb09KWl2RkmtkewW_hev87as5WIOVfWFFfsoKND9bOWJDxHl5VPwkeFQ3DOybmOJypQ0udpgDeYTCkdf8z6RKVa4XcdoR7S1X__BXhYGNqvKkMIeamGZLka_zS_QDr6DK8JsnOHXSB6OMiO9Q0dmaFovGgM7i9uufwBlMMP93vFBM18ytHpaQ_vsBk-oyLcU4DGlGyzt3pF1wqeFnfGSkkb-6L0OSn2y-LpwtFVDrC3MVzPhH1lMVhgS26Nb-bgqW1JBfthFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
خب سپاهان که مجوز نگرفت. گل‌گهر هم بازی اضافی‌ش حذف میشه و چادرملو هم فاکتورهای لازم برای مجوز AFC رو نداره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/132551" target="_blank">📅 20:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132550">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjbBfPxyRhPREiB0-UJPYKJpRHu1utpk8BSwG-XZnxXXeMOedlCquz1xWtix7P6pBMY2Dc-CB9t28jIw1HAhrq2QATO1jnNwSYCqxFqddpvqqvbfVaHi9rohfKfvyPgw_wu0Mk30rPDjmmIbJgcFtIUrl9toNgp6FxtOdaSJKhHfVeGskgDOW4dlG8tMUJPLN5DO51Ixih1CNjcKi0DG9aphR7UGdo1VZ4krgSZdaPPFgDAifOAHuN5mCNct2yQ6CEtghMDDDcDl_0dyfhp3rT8xvdIebqTlSxf5X3h3Ofe2m0Yu3JGD3tx1jxHfvI0L9gWw2IRr55__FArz9qfkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توییت پزشکیان بعد از خبر اعلام استعفای آن توسط اینترنشنال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132550" target="_blank">📅 20:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132549">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🟡
سپاهان حذف شد
▫️
گل‌گهر یک بازی اضافه داره
🔸
چادرملو از بازیکن غیرمجاز استفاده کرده
🔴
پرسپولیس برای ۳ امتیاز بازی با ملوان شکایت کرده
⁉️
باید دیگه چه تصمیمی گرفته میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/132549" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132548">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
طبق جدول لیگ برتر؛ گل‌گهر با یک بازی بیشتر ۳۶ امتیاز دارد و رده چهارم است. چادرملو و پرسپولیس هر کدام ۲۲ بازی انجام داده‌اند و ۳۵ و ۳۴ امتیاز گرفته‌اند. در صورت معرفی گل‌گهر، قطعا هر دو باشگاه اعتراض خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/132548" target="_blank">📅 20:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132547">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIxhmnXwihPifRzwMM91RzHDsBDGj-Pq_SRbf5A_xydTjWQZMT94Nb6gmiv1DQ8bydqc8tzNxxRczsnk9KOl2FuUKcbUmQ8TLvekLsouiKTyvgXR4eh354qC9zpj0rE1LOswO13EYYMZ-nXqq7v6GPhYcdoZoBNb9dyDUJEbSY1lKyHRC5yHcIQjeFdPc59cr21Nf477mN8NMnCQ9WXFPKQ5u85-PMV_OEFOXm_DxODZyi1a6Yum4Z_Z4-ZGGZBGaxapqrRuGgh0JHd_F_fBnnockFUrn2BJC53PL0mDmXpATjYi2_Pbb3jWy7eGooMlNCN6Ytx_FenEGlWNK9RbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی سریع و مستقیم به وینکوبت
🟢
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی انجام می‌شود:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🟢
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132547" target="_blank">📅 20:32 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
