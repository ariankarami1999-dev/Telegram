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
<img src="https://cdn4.telesco.pe/file/mW05a8ZZpjk_bPxMIAO0NUbLo048hqXRttzXM7OowqK_Ki5tMN0dONylivFlObGv3sXVZE3nE0f-0i3Nh_C4wepIgN1mAKPpHwiLI4zaKomcBv-rZfVqrZG2c1EDRaA4HGfX1G3ptqHFjlgn3oQK9a1eC87KPrPS43tW7BXO4nsnszZUffcZZgFOIUXJlBNOalqiz-eQ3uOtZeuz_WCc0zd4ZnGPirkUKz8WPIJ11PjDBUKm0UUt6JuYoObOODQppW8IUeHrBDpa29c0mFu4LHPG8ohRJwyOpuiR7sxlpG1xQ22VTlooL3K-8k7vfSiQ6MV1sLS1XksMEWZWkG62yw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 18:09:18</div>
<hr>

<div class="tg-post" id="msg-19153">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فرانسه کارکنان سفارت خود را از تهران، ایران فراخوانده است.</div>
<div class="tg-footer">👁️ 989 · <a href="https://t.me/SBoxxx/19153" target="_blank">📅 17:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19152">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سپاه :
پس از از سرگیری رسمی جنگ، نیروهای نظامی متجاوز ایالات متحده از موشک‌های کروز استفاده کرده‌اند که از کشتی‌های دریایی خود در اقیانوس هند پرتاب شده‌اند.
با این حال، پس از اینکه آن کشتی‌ها ذخایر موشکی خود را به پایان رساندند، دیروز به استفاده از بمب‌افکن‌های B-1 که از پایگاه هوایی RAF Fairford در بریتانیا پرواز می‌کردند، روی آوردند.
همچنان که مقامات وزارت امور خارجه اعلام کرده‌اند هر پایگاهی که برای پرتاب حملات علیه خاک ایران استفاده شود، برای ما یک هدف مشروع محسوب می‌شود.</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SBoxxx/19152" target="_blank">📅 17:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19151">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ: درصورت ادامه محاصره دریایی توسط انصارالله، ایران و یمن مجازات نظامی سختی در پیش دارند
ترامپ: یک سال پیش، ایالات متحده آمریکا به شدت به حوثی‌ها به دلیل دخالتشان در تجارت و بازرگانی از طریق هدف قرار دادن کشتی‌ها، حمله کرد. از آن زمان و در طول درگیری ما با ایران، آن‌ها رفتار بسیار مسئولانه‌ای داشته‌اند.
متاسفانه، اکنون آن‌ها دوباره این کار را شروع کرده‌اند و شب گذشته دو کشتی سعودی را مورد هدف قرار داده‌اند.
لطفاً اجازه دهید این حقیقت، تأییدی باشد بر اینکه اگر آن‌ها این کار را دوباره انجام دهند، ایالات متحده مسئولیت آن را به ایران نسبت خواهد داد، زیرا حوثی‌ها یک عامل یا واسطه برای ایران هستند، و ایران با مجازات‌های نظامی جدی روبرو خواهد شد، و البته، خود حوثی‌ها نیز مجازات خواهند شد.
من از حوثی‌ها بسیار ناامید هستم، زیرا تا به حال آن‌ها به طور بسیار حرفه‌ای و هوشمندانه عمل می‌کردند.</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/19151" target="_blank">📅 16:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19150">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 11</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19150" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 11
پنجشنبه 23 جولای 2026</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19150" target="_blank">📅 13:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19149">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مارکو روبیو درباره ایران:  عراقچی می‌گوید سیاست آن‌ها «چشم در برابر چشم» است.  سیاست ترامپ «سر در برابر چشم» است.  آن‌ها بهای بسیار سنگینی خواهند پرداخت.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/19149" target="_blank">📅 12:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19148">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q64P2Z5-MjeU0o0QwPAsDjB1edBHDzYLGj48IhUfNPBNUcFRh5Xa3Zg10BtUH95mjgQEpeH8OtjBLxFtjiMaEhYe2gx8JDKP258AHHFUGk3VJeCXwDjnWB19zM0e9ago4obMw7Nz1_jsBlJAJqaZG8ntuWs8bgISgpVce9J0IjTvWUKnam7GX5W3tyLKmarDHw7WuoNxCK-8NSbOqcAMzuA10xSMb_RmPSnwez8i7FiAUMgcQM0LjKqtJ58yhOs8DX9v04zHBDoIw3iz0yHeSpF9J1w6jQWSp9FJyHPR8ZJCgrMcIxHrFq9kLsgPvJPrCefdNtn4IY4AcLU0kB6n2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح بسیار بالایی قرار دارد.  توصیه می شود از تعقیب مومنتوم صعودی در طلا خودداری بشود و برای خرید حتماً منتظر یک اصلاح نزولی عمیق باشیم.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/19148" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19147">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مارکو روبیو درباره ایران:  عراقچی می‌گوید سیاست آن‌ها «چشم در برابر چشم» است.  سیاست ترامپ «سر در برابر چشم» است.  آن‌ها بهای بسیار سنگینی خواهند پرداخت.</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/19147" target="_blank">📅 12:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19146">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مارکو روبیو درباره ایران:  آنها هر روز با ما تماس می‌گیرند و از ما تقاضای توافق می‌کنند.  هر بار که آنها به توافقی می‌رسند، یا آن را نقض می‌کنند یا پس از توافق، خواهان تغییر آن می‌شوند.  احتمالاً آنها هنوز برای توافق آماده نیستند، اما به زودی این آمادگی را…</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/19146" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19145">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مارکو روبیو درباره ایران:  با وجود سخنان تند و ویدیوهای لگویی احمقانه شان، آن‌ها به شدت در حال رنج کشیدن هستند و تا زمانی که به واقعیت پی نبرند، این رنج بیشتر خواهد شد.</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/19145" target="_blank">📅 12:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19144">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مارکو روبیو درباره ایران:
با وجود سخنان تند و ویدیوهای لگویی احمقانه شان، آن‌ها به شدت در حال رنج کشیدن هستند و تا زمانی که به واقعیت پی نبرند، این رنج بیشتر خواهد شد.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/19144" target="_blank">📅 12:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19143">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجار در کنارک!</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/19143" target="_blank">📅 11:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19142">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ایران پیشنهاد آتش‌بس میانجی‌ ها را رد کرد</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/19142" target="_blank">📅 11:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19141">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKTyR5DIq0uC0yg73BYBgVs71SnVzebBR-3kGD2JneV01KZR4oOaKGPa5KLhuR4UZBVBKqGDpa6e0tAxwLv-qTd_kyhh3WclDcd-vVpmmJJzI7eo086K1XiyWg3vxB0rFDEC_v9WInU8-D4Ho9PArftM_XR047_gykPMBcAQQwe2vWu7bVh3q8o6F6c1tPBEVx94-0CytrePlbGH3_p8OIKFfZ6vPZ2hA7x-JI1PnYa8nsEaY4QmhGzU-_UBPdw9auQJIUPwyzfrH9j3VE0C3rvyiyK1EExePREK_KH6TCeiuwN1pvORuGzA4ASWmNd62G2SFOzK-g4F3I7-dgC06A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/19141" target="_blank">📅 11:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19140">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYKs3Dyf-efnpzqrak8w227rqXsJGT1e4g8Tdt9oyHV4XL-DLhdQrjM3Q7WDAc6gzlNKB_kmsXWuAJQ6wMUFSpR9cy9vhzpNvf-Bk7gMjZXHlCIJ-nRhO6VcCJBMxXBbA2W0CXt0v0RWPCTr0E8Biy03S5TdoMkxRzTN7qcQsv3gaNKN_b40k3lBeSypFNoDukA_H0grHNEzKgIqBdy9VhI_Z_lfw6F8eWw286rOFw9XfWgG-Lppf_1TqZqNQMB-uMCpuk6NV5HRxDUEQ5OVbG1mo1uTymfckJmPx7yBDHswK6VuZgmeEkViR6E38kp13_58ZrFnlAi3rCAhiH0UpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/19140" target="_blank">📅 11:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19139">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyViX09DnPtVfX-IxH5R0_MbV_i7FKzkDt6-sZ3CDL-ucfkyyjOwVLBDp7Jpqj6qcizWL4ka6vbPQ9eNGUpp9VqWs-oYUyF-t0M372jq1kFc1UTImIS-6Afhz6czHvv2TEqT48KMhYT-ERyb_TtBTeBoA8xsT6kIO2wHTozmPDU2_lblYOe4QHqxb8gWwjl3pbco-GrRiZj2ebph2qm2v_ImmMblro41hYxN-OnpsTbDc9zruG65HA6dJC8BzfhKm10Y_yzENq3irhVM5lnUfEcEYKDJbDP80oOKSJeBnEW-ruR2stGsnqM-pktIF4mcwzD5SPjskvAP607ccPbobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
هرمز؛ گلوگاهی که می‌تواند قیمت گندم را منفجر کند
تنش یا اختلال در تنگه هرمز تنها بازار نفت را تهدید نمی‌کند؛ این آبراه مسیر حیاتی انتقال کودهای شیمیایی است و اختلال در آن می‌تواند هزینه تولید محصولات کشاورزی، به‌ویژه گندم، را به‌سرعت افزایش دهد.
از آنجا که بازارهای آتی بر پایه انتظارات قیمت‌گذاری می‌شوند، جهش قیمت اوره، آمونیاک، فسفات و گوگرد می‌تواند حتی پیش از کاهش واقعی تولید، زمینه‌ساز رشد پایدار قیمت گندم و سایر غلات در بازارهای جهانی شود.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/19139" target="_blank">📅 11:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19138">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فایننشال تایمز :    آمریکا نمی‌تواند با مذاکره به اهداف خود برسد. بنابراین تغییر رژیم دوباره در دستور کار قرار گرفته است!</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/19138" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19137">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooeUmiiKXZx_N9utrz9dBv1SM3A3-E7zGXSKXH4wjJVJM0BmlD72etJjQ0AOY_TsYoPAPdn62nkWQHhm4WnVtFKfguz6axJNfWpdJs6A2nrQ50fWxhmCHAcMQQixtxYt6nY5jbcD9nuYtjMZF3otPnaEUFZ0h17jS29BpN9JnQZ9fTwI0hpvSwavzbXltyagK1BBgdCjsNYJwQWtZkG7R5U-sgumEP9uMN_d4GDynfSVYuhvKLew_0jJeftY3g5uzBlQOwlH3sSge3tTISHVFzoU4oL18fjEtubpp7OjbY2Ii2MOmR25vCyH9OE9CKZzVf-ABg2LXviPJgPNLvzf6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/19137" target="_blank">📅 10:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19136">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfMUEE_KpMPsNcsoSYvPGm1dtnE14R8-Vuv294kx1_m2g3aC0nmJo_HlocnNegiu1XjIQehN6x-ZNHOIpaPfeBPxVI-_fvYaDopTyux09e0vyZr8Q5TVSp0I-HV_7bMrMLMw_2tFb5LH3tBk87Db9StBMbNj2tM7oVx9vtyuOX0wvcJMF8ymeK3AlSdiBdE76BPkbFfAWipcRe685IsifvSOKSbBa82sxhwWftYtZ_3dkYF6v8XtcrIv8EMinpB3tJeMELumiIcNp_4eXmhsCq5TTmFX_d7sAkuXTFi6z_9UMB4I9hY09fRt7Q2HPYc223UDUFz6PomW2Fr6e6-ztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چند ترامپ می گوید تنگه هرمز باز است اما داده های بلومبرگ نشان می دهد که شمار کشتی های عبوری از تنگه هرمز (آبی) به کمترین سطح ممکن رسیده است.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/19136" target="_blank">📅 10:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19135">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIGd6zrfS-uwwgdCXBRewdpDoaSxfFxYwn8-QM6sZ3EudMz8OrzIGrIyE95YPbDiPzdHbo_TZWVMuu8pUeY31HHq1jXTa6Csbv6flYog3eHTADz8Qn0iR4j_gCjJ1rlUAh7kurNn01L8nzI99pgveSYvAoehYKuty9AxWRaPyAhjgLrHP3-eyPtDqHpdVzAE-BKx9Ur8Rxc3FW8YU19pZYdH7j_FGkEPGrqihFYS409XbGkuQo0OsB88zFvIgxJ8TPh_aMxoZI8b17NKGRvFvLE_hWH81XFpicDDCOCHfpLBEIAfp_p5T_gGxNqEGoRlLLbGF9bHbje85ThnnkO2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان، طرح بودجه دفاعی به ارزش ۱.۱۵ تریلیون دلار را با وجود مخالفت‌های جدی دموکرات‌ها تصویب کرد.
دموکرات‌ها از ترامپ به دلیل همراهی با حملات اسرائیل به ایران بدون تایید کنگره انتقاد کردند و با بندهایی که به تعمیق همکاری‌های دفاعی بین ایالات متحده و اسرائیل می‌پرداخت، مخالفت نمودند.
این طرح همچنین شامل ۶۰ میلیارد دلار بودجه اضافی برای مسائل نظامی است که بخش زیادی از آن انتظار می‌رود برای پوشش هزینه‌های مربوط به درگیری‌ها استفاده شود. اکنون این طرح به سنا ارسال خواهد شد.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19135" target="_blank">📅 01:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19134">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سنتکام:
امروز، ساعت 17:30 به وقت شرقی، نیروهای ایالات متحده با دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند. این عملیات ادامه خواهد داشت تا توانایی ایران در تهدید ملوانان غیرنظامی و کشتی‌های تجاری در حال عبور از آب‌های منطقه، بیشتر تضعیف شود.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19134" target="_blank">📅 01:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19133">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قیمت نفت به صورت عجیبی رو به افزایش است</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19133" target="_blank">📅 01:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19132">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9ur1gjMXMndaSx8Jbg5ivkkdMsYc3ZxbVdwUwuAZFCvjq88dbDTkoY7mSxAzJWr__AL3OIbYAKIf3kUkaxntIHlU4NlDBMhYBt6EwY465PSWfuGHDlz2PKiDmNMGDHSjCB6oqvaymE8Eik8ydd1dMmoUWeiVjQM-Xy9jNc5Ex_7Wy-foF_TecZ6RZGoP_F6QAc5M45Wk07sUBSpq2F4CWXIY57Fdsizx_KtpeGp6fuVKjQ4s77rpeB-f6wfXoyG5M3Vsg_955x91w4PNGQxRCnPZPuZbKI5-3MK2M_1ajT_AoyIc-JG6Kn1616ztS7Rg436_0NBoix25XuftDHY0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایید نشده:  یک کشتی نفتی عربستان در ۷۰ کیلومتری شمال مرز یمن با موشک مورد اصابت قرار گرفت و در حال سوختن است  ظرفیت کشتی حدوداً ۵۰۰ هزار بشکه بوده و مبدا حرکت آن از ینبع بوده است. ‎ #بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19132" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19131">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جنگنده‌های نیروی هوایی ارتش بر فراز آسمان تهران به پرواز درآمدند</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19131" target="_blank">📅 00:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19130">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">جنگنده‌های نیروی هوایی ارتش بر فراز آسمان تهران به پرواز درآمدند</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19130" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19129">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تایید نشده:
یک کشتی نفتی عربستان در ۷۰ کیلومتری شمال مرز یمن با موشک مورد اصابت قرار گرفت و در حال سوختن است
ظرفیت کشتی حدوداً ۵۰۰ هزار بشکه بوده و مبدا حرکت آن از ینبع بوده است.
‎
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19129" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19128">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">موج ۴ کامپلکص</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19128" target="_blank">📅 00:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19127">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجار در اهواز!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19127" target="_blank">📅 00:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19126">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yp4M0Raf6jtZePsqkDeAE-b3y_-kzpyRtRxwwQ__GrjcSrXlgF4LV17rhmW9AHYTdJJzOhrkfNLF2zIfeFGnazlszVbmTS7fI-kHezbDeBgnM5343CqKShLU6nOTMD0DHN6EDp-9JbuWyxv7ooiJvLU4SIi5lQM1kD5BIGtQe478R0DVqNBcmSRribSMxuoNf57nhVlBIvIUxD7YnjRKA6-uYoaOkeJC_nXqBHUwsZvJ_SnjFNb5rhg1LZ3E7yCGuHR6ygnkOe0zFsu09dU7vHXNx57K_hOpr7WZjTbgCvJOUAh4nWPnZx-o31fb7VfHjPCd4jL9ZgopyqoU2HifJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح بسیار بالایی قرار دارد.  توصیه می شود از تعقیب مومنتوم صعودی در طلا خودداری بشود و برای خرید حتماً منتظر یک اصلاح نزولی عمیق باشیم.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19126" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19125">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_T2lJ2UqYU_SMej10tFbdG5V_ykR6EJaRemgKnHC6sRqNHG2wL16MFfFTghKDKVgjO0bI9aC_Tfta2JDaByOE-oCj-8ifVJlDO3v4pS8u-QOOaDnAQ6k6OV8XCnhgZgWk-qIY_Hb6ZlM2TRQ3tiC1dwh08Gj9PzqP2zK_ehPILEqPfBeJBv9TiBdgHRQ0CxSXI1Aha_vGSWFWINVlZ5siBRtOx_h9f445aThhDMSU5nRQb1Hp7gyQPVjLrk1KIYVV8920hSsEdphPEIM6WAZXehRrPTTElrS4YW3akbjozXs2vXayMyZIOMuaVgrGPTtWoEozE_dcFpELKrIDCpVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا قسم همین کتاب را برای ترامپ پست کنید دلش به حال ما می سوزد و دیگر به پل ها و نیروگاههایمان کاری نخواهدداشت.</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/19125" target="_blank">📅 00:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19124">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجار در تبریز</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19124" target="_blank">📅 00:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19123">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇰🇷
کره جنوبی از اتباع خود خواست کل خاورمیانه را ترک کنند</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19123" target="_blank">📅 23:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19122">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">واشنگتن به تل آویو اطلاع داده است که قصد دارد برای اولین بار در جریان این تشدید، از بمب‌افکن‌ها در حملات علیه ایران استفاده کند.
سازمان رادیو و تلوزیون اسرائیل</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19122" target="_blank">📅 22:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19121">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMHrQkNM856-m-xlyozlRa5l0HQOHoaOVXrJk5dU6jkb5DdEgtf9Jkc5BAAK3ymIXckXzPRoG3TjFmWFKLNrqmbKSDW_Myd9TC9LHwD2YozsA6gkfCks61qgCvSzq_NWWwm45cgQeEWj5I5VDhYSQdwLDIMvBbKw-vDA4zHcuRybyUNPH17ymuILI2z2aJ8GYiOpMswME3YfzfT4TvbqfL7KfaRflwsGXNgOhCPlHOK2R55tBVa9HXMJm89otTjHvfzLQxfIfal1SYvqiFDh0KuATdiOUKFAxcRMFZTl2qCI4j06cWPgaKhivDmi6sVq7R5zX2NrzijELsKC76fLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور دیاسپورای اسرائیل، امیحایی چیکلی:  ممکن است برخورد  مستقیمی با ارتش ترکیه در دریا روی بدهد.  این یک سناریوی غیرممکن نیست؛ ممکن است حتی فردا صبح رخ دهد.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19121" target="_blank">📅 21:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19120">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">محمدباقر قالیباف:
«معادله این جنگ روشن است: یا همه یا هیچ!»
«در منطقه‌ای که ما نفت نمی‌فروشیم، کسی نفت نمی‌فروشد. اگر امنیت ما تأمین نشود، زیرساخت‌ها امن نخواهند بود و امنیت تنگه در غیاب نیروهای آمریکایی است.»
«ما بارها گفته‌ایم که وضعیت تنگه به شرایط پیش از جنگ باز نخواهد گشت.»</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19120" target="_blank">📅 21:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19119">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305f8deeb1.mp4?token=rOi53snPA2vMs7YDj25s3TFoshXfM8xpKOXrlYKfcEjNw8m7NVA60AqNUnodAl_dgbeOPDOhVjb28cMhxNur6xbf9WGmxghZ93v_HKmQPA5KseWqzlP7BFlayIiBaRR_UE6McXQXL91hiyQVGooaZbjnhryLiZOBhfQc_JntrnVoL1CS3iyZ0j8hoTTmDAoC_SsgSxQRF5PpLkM_UxYLzL7itk3HUijoygYPjn0_IvMI5-McTdAN-C4Go10zoBPWiWmB9df1rOvws3oN1QlB-t9MPBwb8y4hCY5i8Y5ZErA5EVN2653CYkgfD7KjBbrzQv4DPdPilLrWqrdNNzeJoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305f8deeb1.mp4?token=rOi53snPA2vMs7YDj25s3TFoshXfM8xpKOXrlYKfcEjNw8m7NVA60AqNUnodAl_dgbeOPDOhVjb28cMhxNur6xbf9WGmxghZ93v_HKmQPA5KseWqzlP7BFlayIiBaRR_UE6McXQXL91hiyQVGooaZbjnhryLiZOBhfQc_JntrnVoL1CS3iyZ0j8hoTTmDAoC_SsgSxQRF5PpLkM_UxYLzL7itk3HUijoygYPjn0_IvMI5-McTdAN-C4Go10zoBPWiWmB9df1rOvws3oN1QlB-t9MPBwb8y4hCY5i8Y5ZErA5EVN2653CYkgfD7KjBbrzQv4DPdPilLrWqrdNNzeJoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام وضعیت!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19119" target="_blank">📅 19:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19118">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اعلام وضعیت!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19118" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19117">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اعلام وضعیت!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19117" target="_blank">📅 19:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19116">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzhLKMvro4hovyideuCKsRAT88V8eRXHAtgoc0v2BPF1S52HLdjHJ-BoJW_ptrUMo6QP4z8B4NoB9KZLyrPMfzsiFe09i0yacONEFtGTxZtDSobnRnr6dQcYBcaEcZP5TxY3PMn-WK8d4KIE_IR4xOtG5CPj91Vs8JKfvx-UjBUPz9WdIDTH7IjvBLUIXk7bREdtCP2mEBtVo_vC44d6zQc4kpgZPW6Vb70oLwU8yjCxCS3HV8tJj8chfZ-Q5FoQWexSNsAuoYbujicuXEoKbI9ui8FMqmpmJJ8JW-9NFesP9yipe8iGhzidXxeNpCK9M7FauaQ8O466omo0dh57GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19116" target="_blank">📅 19:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19115">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پدرسگ مثل این بستنی فروش های قرمساق استانبول است که پول را میگیرند و اسکل هم میکنند و آخر بستنی را هم نمیدهند</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19115" target="_blank">📅 19:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19114">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">منوچهر متکی:
قرار بود قطر ۱۲ میلیارد دلار از ۲۴ میلیارد دلار منابع ایران را آزاد کند و حتی اعلام کرد ۶ میلیارد دلار خود را بعداً پس می‌گیرد، اما آمریکا وارد شد و گفت یک سنت هم نباید پرداخت شود؛ تا امروز هم این پول پرداخت نشده است</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19114" target="_blank">📅 19:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19113">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJJSngJnCxa19H_6jUlf84h7S8UGo1_ELcWfVyfOH-hfl8kGxnlagnvULBHACbeNqkzbvRTPmSwT-n4zHfnTHZ6wTOxjRvJrVN4iRdsjjKKARkI9lMWpNQetCca36woHdZrAT1mnO0D-lcUUhmVUGWPFpnpC8wr_InKvcmn1vE6kZzVTBSpXh4LCJU9aBtu6ZAmIYG25Tm6gxOX0Xe_y9YAKpwe1La7jq9immHcTaz_vB1uCtof_aoJ4v8qtc9xzKnUskCkISdGx5-Orjf_Zg9YJR4MsoQ2Erp6KPsk-GTdvKYY3R7tk7gChhgbOL5Kwwun3XVx14RSqewFIAkThCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکل ها یک چیزی شنیده اند!
ده سال زندگی در ایران کافی است تا کارمای قابیل هم پاکسازی بشود دیگر چه برسد به اجداد نزدیک مان.
رایگان، تضمینی</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19113" target="_blank">📅 19:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19112">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsjIuSgYAIvNC9PPHlgK6ABLujiv6aYIa5I_avGLFM-YMzyfXx-QVMT3A4d4BcDmx3yZ2GZWZlqweNyNKxQnHzMX7DqpsoyfBPjKkO7FTF0memZXAq2nhqMrtwEnl0am94tV7cbn8NFMgQCU6L791cOE73F327AydhRlw9noWNeQFH4cg8ggHYmqWO9LpX2IMWMDvbeOguEGjwvt5GHz9JAm3xLjLcyhkyEnomCIcer-xMnaXcIeiDAV4KWYqovIDXawm8fkBlhjjiECtbV3zzRNsVuxNYPgVxYg91nM_gPbuoW3hbs6BL6SAk12mOEzMC4Gcs7lIbUeUZosqLZfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت 12 امروز با نیما در نشست هفتگی به بررسی پویه های ژئوپولیتیکی موثر بر بازارهای مالی خواهیم پرداخت.  لینک ورود</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19112" target="_blank">📅 19:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19111">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزیر امور دیاسپورای اسرائیل، امیحایی چیکلی:
ممکن است برخورد  مستقیمی با ارتش ترکیه در دریا روی بدهد.
این یک سناریوی غیرممکن نیست؛ ممکن است حتی فردا صبح رخ دهد.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19111" target="_blank">📅 18:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19110">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزارت خارجه ایران:   بلغارستان باید در اجازه دادن به ایالات متحده برای استفاده از خاک و توانایی‌های خود برای حمله به ما محتاط باشد.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19110" target="_blank">📅 18:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19109">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرنگار : آیا چین و روسیه اطلاعات هدف‌گذاری را به ایران می‌دهند؟ این حملات اخیر ایران  بسیار ویرانگر برای نیروهای آمریکایی بوده‌اند.
روبیو: هر زمان که در یک منطقه جنگی مانند الان هستید، خطراتی با آن همراه است. منظورم این است که در نهایت، این واقعاً ثابت می‌کند که این همان چیزی است که ایران در ۲۰ سال گذشته پول خود را در آن سرمایه‌گذاری کرده است.
هیچ کاری که چین انجام داده، به هیچ وجه مسیر آنچه را که در مورد درگیری‌هایی که با ایران داریم می‌بینید، تغییر نداده است.
و در واقع، در برخی موارد، آن‌ها در مورد آنچه که به طور بالقوه می‌توانستند انجام دهند اما انجام ندادند، بسیار همکاری کرده‌اند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19109" target="_blank">📅 17:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19108">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الان عرب ها بیشتر نگران هستند تا خودمان</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19108" target="_blank">📅 17:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19107">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ:   از این پس در ازای هر نفتکشی که هدف حمله ایران قرار بگیرد  یک پل یا نیروگاه در ایران هدف قرار خواهد شد و تهران و اطراف نیز جزو اهداف این حمله هستند.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19107" target="_blank">📅 17:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19106">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ:
آمریکایی‌ها مخالف جنگ نیستند.
آمریکایی‌ها نمی‌خواهند قیمت بنزین بالا باشد، اما مخالف جنگ نیستند.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19106" target="_blank">📅 17:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19105">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ :
ایران برای کشتن سربازان آمریکایی بهای خیلی سنگینی خواهد داد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19105" target="_blank">📅 17:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19103">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fw3cfG9lmYJBb3KR1-b0JfUPs59L1hdmvQcUjiG0sDIa-phPW1r4dVm1KSW99IYzlCjT4QesntFQtxcVFK0OfjP9UCQhkLKecJWK0aFMLXmNOhPSneKuvlt96GaLazwROJESwSfqOBY3grjRmWGUq1kSv4rXFocZHEbQhcIX7mXk9LkoF5cPqS283bvCbHGojW_0z_D_Coi3HbYVqlFSQwH7M_1wX7yGdPsihQ_q6t2lS_fnKlVlQHTZytCOvtWGPiR9hi_6C_tavMO8Ft5nE4Z6iOxrcMwAnAAhg3OrOc3nLYA0BoFNQyqLAKMJWvlonyLItLQ2R3sDi9uYp7P0aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
انتظارات تورمی مصرف‌کننده آمریکایی؛ آینه‌ای با تأخیر برای حرکت دلار
انتظارات تورمی مصرف‌کنندگان آمریکا معمولاً با تأخیر نسبت به بازارهای مالی تغییر می‌کند، در حالی که شاخص دلار زودتر به چشم‌انداز تورم و سیاست پولی فدرال رزرو واکنش نشان می‌دهد.
تداوم یا افزایش دوباره انتظارات تورمی می‌تواند نشانه‌ای از ماندگاری فشارهای قیمتی باشد؛ موضوعی که معمولاً از طریق رشد بازده اوراق خزانه و حمایت از دلار آمریکا منعکس می‌شود.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/19103" target="_blank">📅 17:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19102">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مرندی باوجود   حامی نفت کرود!</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/19102" target="_blank">📅 17:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19101">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دکتر مرندی در پاسخ به تهدید ترامپ دوباره دستور تخلیه شبه جزیره عربستان را صادر فرمودند</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19101" target="_blank">📅 17:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19100">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rhih2_CaOkHgTIjeFIMY85ySyRCo9ISYLUFqdhDMXMMmPzmXqqM_ei5ePkvJCcIvZLO22qlzq9R6KznLeYbH6tPZwrPmLj192-iAstCYUt9IfRWSjTudxw1mMRNz1tkKHOphIzW8pjXo4ee05x_Aad94T5M53Bggpea-vLDvjqxe8_tJu9OviCZEI0f_7QZkkEZSSV5gbzDfQliCjZTTbmk_uHUNfPEBwYsWyroPDfUZPxT0UQBRaeXFocGi45oOVFncW63UAS0Hf6Di9zQm02BhdtnWyE4ieB6M4quRf_3q1tzHyJRY6VCFAlzM3KDA7LhI9c24m-hKkSGC_Vw-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   از این پس در ازای هر نفتکشی که هدف حمله ایران قرار بگیرد  یک پل یا نیروگاه در ایران هدف قرار خواهد شد و تهران و اطراف نیز جزو اهداف این حمله هستند.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19100" target="_blank">📅 17:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19099">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ:
از این پس در ازای هر نفتکشی که هدف حمله ایران قرار بگیرد  یک پل یا نیروگاه در ایران هدف قرار خواهد شد و تهران و اطراف نیز جزو اهداف این حمله هستند.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19099" target="_blank">📅 17:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19098">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پاکستان از ایالات متحده درخواست یک تسهیلات تثبیت ارزی به ارزش ۱۰ میلیارد دلار کرده است تا ذخایر ارزی خود را تقویت کند، روپیه را پایدار نگه دارد و وابستگی به وام‌های صندوق بین‌المللی پول را کاهش دهد.  این درخواست پس از آن مطرح شد که پاکستان در میانجی‌گری مذاکرات…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19098" target="_blank">📅 13:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19097">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پاکستان از عربستان وام گرفته تا بدهی اش به امارات را بدهد!  مستراح گدایان!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19097" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19096">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">جولانی اماده حمله به حزب الله می شود  شبکه کان اسرائیل به نقل از یک مسئول سوری گزارش داد دمشق آماده اجرای عملیات نظامی علیه حزب‌الله لبنان می‌شود.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19096" target="_blank">📅 13:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19095">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">با این سبک بازی، چین عملاً دارد ضد محور ایران-روسیه در حوزه ژئوپولیتیکی عمل می کند که پیشتر به این موضوع اشاره کرده بودم.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19095" target="_blank">📅 13:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19094">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اینها اگر بدون پدافند درست بروند با A-10 قتل عام خواهندشد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19094" target="_blank">📅 13:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19093">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">این خبر از دید من مهم است و می‌تواند منجر به ورود باند جولانی به لبنان بشود</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19093" target="_blank">📅 12:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19092">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ساعت 12 امروز با نیما در نشست هفتگی به بررسی پویه های ژئوپولیتیکی موثر بر بازارهای مالی خواهیم پرداخت.
لینک ورود</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19092" target="_blank">📅 11:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19091">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9dRIPu8schgEzhTdeSe1bWMnSajB-_wD_sqJZ8ZaNN3GL529sUBPjg55Uk9tA4oMF5BlTNt0U_txzlqLmRGTwrWnEWNxbgToJjsQtJZW8_kAtRG3WqSNFuRw1qYRJyRMflcX7S8mQkPvJSU80BFnGKvgj6QQ_neCZ93lvyKknvEz6C9bT9XhX1-9yDGRHLSOTkPP2zQSg2Q_cg8zfqUWvTlpfVGGdTIdJAFaXs60FPQmcOuNau_oq_LIctHkGkYgOcuChtUeAK1Sf3R8Ml08z2zFhUoPN8iwJ0wcFeqoPZ7B28ncgxRyLG0CAFZ4NtZ4OM2lFI8FkKX5x-t67g9Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح بسیار بالایی قرار دارد.
توصیه می شود از تعقیب مومنتوم صعودی در طلا خودداری بشود و برای خرید حتماً منتظر یک اصلاح نزولی عمیق باشیم.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19091" target="_blank">📅 11:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19090">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الهام علی‌اف، رئیس‌جمهور آذربایجان، در سخنانی پس از دیدار با فردریک مرتس، صدراعظم آلمان، در برلین، به خبرنگاران گفت که مقامات سابق و فعلی آلمانی و روسی، این ماه، در باکو جلسه‌ای مخفی برگزار کرده‌اند.
علی‌اف گفت که باکو هیچگونه اطلاع قبلی از سوی آلمان یا روسیه دریافت نکرده و تنها پس از خواندن گزارشی در روزنامه "تایمز" از این دیدار مطلع شد. او افزود که مقامات آذربایجان پس از آن، تحقیقاتی را در مورد این بازدیدها آغاز کردند.
او گفت که: «به عبارت دیگر، از قلمرو ما بدون اطلاع ما استفاده شده است.»</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19090" target="_blank">📅 10:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19089">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkKExRkjcCNa20b2ZcUlGGYvsqoOTIATsWL8kZKHo__l83AN6ZosAIMf-hCQG2YSQ-WcQ8sR1FrM4wLEQYFWjglwqfbE-udgEau7CyA_fHnexEQ_ho2y13ICn4Q4FL1eRvF55iLipdVN-lPoQvsZfNBKI-zCUbhiP0xyPMhICeze0dCCJnCknNDmoApETabApvFWXGKV4CRHoUtg413OVnja1KuRXODT5g8eCQj7tG3vLRd-dsIoIdzja02qq2PRqAOI6e-0l8sj8asUsppec1UhFwkw-nAtFRCRrjane7mwPhr6iHIaSJRDQlfTz96lBMYxBIGUjXGR8b6OcCQbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاواریش ها هم یک تخته شان کم است!  در خود مصکو بنزین پیدا نمی‌شود و مردم سوار هم می‌شوند آن وقت می خواهند بروند در ماه نیروگاه هسته ای بسازند !  لابد چون مطمئن بشوند دست پهپادهای اوکراینی به نیروگاه هایشان نمیرسد!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SBoxxx/19089" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19088">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ادامه حملات سنتکام برای یازدهمین شب متوالی</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19088" target="_blank">📅 09:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19087">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ادامه حملات سنتکام برای یازدهمین شب متوالی</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19087" target="_blank">📅 03:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19086">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ادعای منابع اسرائیلی:   ایالات متحده امشب با بمب اتم تاکتیکی تاسیسات کوه کلنگ ایران را منهدم خواهد کرد</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19086" target="_blank">📅 01:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19085">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هگست درباره ایران:  ما این جنگ را شروع نکردیم. ایران این جنگ را ۴۷ سال پیش شروع کرد. ما آن را شروع نکردیم. آنها شروع کردند.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19085" target="_blank">📅 01:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19084">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هگست درباره ایران:
ما این جنگ را شروع نکردیم. ایران این جنگ را ۴۷ سال پیش شروع کرد.
ما آن را شروع نکردیم. آنها شروع کردند.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19084" target="_blank">📅 01:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19083">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حمله ایران به کویت</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19083" target="_blank">📅 01:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19082">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7vMvrjqIG6bd6wsnSS2obOsHqQFdBAzcMw9VhQUU2x-S20qZBqR2Qfv--FnQbyZUx6Vb5gXm5PsxahHAqSsnIFCGJVtKW77V5EqrmUgRYnUtgnTYjzxB6MnTwMNDwA2w5PL7ZU5LinC62-DnfS3SQBuVTOzlCiDXfmcSe7et0q7ux6SV513lY9xBDV1Nal2q-4WSaOJHzwvjYkvLnhIteqnMkUm5QyRcZN8T_1TcS6uYteqI2iyl1mYrT8KcjQcEd6wTnOZuw0dvngub2FLsgsT6t9fD4ntNkn6851vPGNm5OFWXN9aYfxmUneDJm5TyNINnTtOXP7hsTs77Lm7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://nuclearsecrecy.com/nukemap/?&kt=10&lat=33.6506104&lng=51.5503762&hob_psi=5&hob_ft=2207&casualties=1&fallout=1&zm=12</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19082" target="_blank">📅 01:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19081">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اگر بر فرض چنین فاجعه ای روی بدهد، این دایره ها نشانگر محدوده های آسیب انفجار یک بمب اتمی تاکتیکی سنگین خواهندبود.  روستای زیبای جهق خیلی نزدیک به کوه کلنگ است....</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19081" target="_blank">📅 01:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19079">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ادعای منابع اسرائیلی:   ایالات متحده امشب با بمب اتم تاکتیکی تاسیسات کوه کلنگ ایران را منهدم خواهد کرد</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19079" target="_blank">📅 00:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19078">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GakqK1fsyxAK39PG_eaEW90tTHVl3qxtexDJcOSRTgLQoOLqy9vncAiiDmmCzMMPBIHMpTAsFNQeHOizTIkmH8FLjj2GCArN2YCyYN69TlV4nXdsF8N9qiHKkCQron1yoUgFmYEYOzIQEBHzso13nmWxhNxY7-xaHgZCLy62dBvJTkVLf7EKYQB26r8u_UJPBU3Gs4Ip_UHzfduLf_6on3hC6X3tY2pwkC9UrwJc_r9or-saZ38AoqZczJdEkYSm1zyhPeQC2W4gdnJLxcZm7ap3ZitIufJrZLVB0x0S2Lq1zWfgr3_WoF_0rF4qxGne4zZYH8jdkmYgkuKygujjag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای منابع اسرائیلی:   ایالات متحده امشب با بمب اتم تاکتیکی تاسیسات کوه کلنگ ایران را منهدم خواهد کرد</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/19078" target="_blank">📅 00:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19077">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سناتور آمریکایی: آیا ما توانایی تخریب هر چیزی را که زیر کوه "کلنگ" در ایران قرار دارد، داریم؟  هگست: بسیاری از قابلیت‌های ما طبقه‌بندی شده است، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای در این کره خاکی دسترسی پیدا کند، ارتش ایالات متحده است.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/19077" target="_blank">📅 00:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19076">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سناتور آمریکایی: آیا ما توانایی تخریب هر چیزی را که زیر کوه "کلنگ" در ایران قرار دارد، داریم؟
هگست: بسیاری از قابلیت‌های ما طبقه‌بندی شده است، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای در این کره خاکی دسترسی پیدا کند، ارتش ایالات متحده است.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19076" target="_blank">📅 00:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19075">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیتر هگ‌ست، وزیر جنگ ایالات متحده:
«روسیه و چین در برخی از فعالیت‌های ایران، و در سطوح مختلف، به این کشور کمک می‌کنند.»</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19075" target="_blank">📅 00:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19074">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAu1PkBjEpZ1F6eMG-oWsV8PKd4w_8oBQDKO1Z-ypgmdSQdWYuMNlq_eYpysyhRflcZskwUWlLmsG9rbyOB9lpTAeF8VaZ95eTKQf2ZG_5NrmsAs0bdUzcuQykgsNf_mZ5I-t8Kfiv3uc7bBULLouZqKvfK_1vWTxaCi8Uvu00pcj-2bChPyk-O7B2PGIBBwaYPbpQ3xwVWPOXPK4eOsg8XQpemEFOWWi0CwCU3tzpxlvtRtXwb63_Xc3lRyBeDAH1e4WGOBw3KM3jXlaN2fgbxUNb-KbI8vm7K2ZLQasL7vE4hL7tjXoW1-HZFuPTp3nP4WG4xj4KxSTd4Ml5u0Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:   در حال حاضر، ما کنترل کامل ۶۰ درصد از نوار غزه را در دست داریم و دستور من رسیدن به ۷۰ درصد است... ابتدا ۷۰ درصد. از همان شروع می‌کنیم</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19074" target="_blank">📅 22:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19073">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXYZcZHh0F2aH020XSSr7kXp-b7eyCN1052vlWikEFhGezBO4UJzKVaADKIPhOOr8dH4oUszbcjFGH2cjz1oGQ-Ld93ly4cmmt_dEWF3obhhdvGcK2ocgnE4oir0Yn5-6QPwPiJpKlVR2V9OHBmuB9H9S156WyAvs8nP7ZyhS1zhssID9rbAgVv4PQ-N7BReWm_cjUuRqxNgLr23izXZXAr8tw2WNi5Us-MLHbsNadpq-wu66p92jhIH2I3OMq1DYgVic4VuJyRC2yOK4yO7XkosIF11eHRCDGvfUzvpiKFAJLmONdbCluPIOzNw1DD5lr-jsl36j--HbiJCHIGcug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایینی قرار دارد و پیش بینی می شود طلا ابتدا ریزش و سپس رشد داشته باشد.  محدوده مناسب حمایتی 4015 الی 4020 برای امروز.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19073" target="_blank">📅 22:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19072">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بلغارستان از پارلمان خود می‌خواهد تا استقرار ۸ هواپیمای تانکر آمریکایی در پایگاه نظامی Bezmir را برای حمایت از عملیات ایالات متحده در خاورمیانه تصویب کند.  این اقدام پس از جنجال‌های مربوط به استقرار قبلی این هواپیماها در یک فرودگاه غیرنظامی نزدیک صوفیه بدون…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19072" target="_blank">📅 20:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19071">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">️ترامپ:
ما اصلاً کارمان با ایران تمام نشده است،
ما در حال حاضر قصد ترک خاورمیانه را نداریم.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19071" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19070">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ درباره ایران:
بچه‌های جوان را می‌کشند انگار هیچی نیستند، انگار آبنبات هستند. کارهایی که انجام می‌دهند دیوانه‌کننده است.
آن‌ها مردم را به صورت تصادفی می‌کشند—بیش از ۵۲,۰۰۰ نفر—و هیچ‌کس درباره آن صحبت نمی‌کند.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19070" target="_blank">📅 19:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19069">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ در مورد ایران:
آن‌ها به شدت مشتاق دیدار هستند.
تا زمانی که برای دیداری معنادار آماده نباشند، ما هیچ علاقه‌ای به دیدار نداریم.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19069" target="_blank">📅 18:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19068">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کویت سفیر ایران را احضار کرد تا یک یادداشت اعتراض‌آمیز درباره هدف قرار گرفتن یک نفتکش کویتی به او ارائه دهد.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19068" target="_blank">📅 18:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19067">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کویت سفیر ایران را احضار کرد تا یک یادداشت اعتراض‌آمیز درباره هدف قرار گرفتن یک نفتکش کویتی به او ارائه دهد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19067" target="_blank">📅 18:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19066">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWr3yDsAbEdBne6yVgX-FzoR_PcJATiqDmikZOVWKf-YfM0SS1-m3O0rb4WB2gWN-4jCxP1d9xy99OmFwsXSU24Z2kZkWGjgDxscgJaFaHIEoCnAd90orekF1kOe9_HsUtYMeRmn2e_-TGWEvOae4l8GjGk0OKIM8oeLiq56qJnZx5xMW4Cb4c2cexONLbyM9VQVSyPRnAU2Ir2Gd9K2JkEY903O-QpuTRGeTITZqsRb2d4oM3RUQ9yHRsI32UffP--FkV6WPNEFNMu5cZePoEPq0dSGz6PhVVRTKGlooCz6Kaunkm8heKJCQhmMCVVDIh6zkLZo2vm__OIzk5zutw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد تند ثابتی از عراقچی و برنامه جواد موگویی</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19066" target="_blank">📅 17:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19065">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الهام علی اف:
روسیه دیگر به دلیل شکست پالایشگاه‌های نفتی خود، کاملاً قادر به تأمین شرکای سنتی خود با نفت و گاز نیست ‌.
«از سرگیری سرمایه‌گذاری‌ها در زیرساخت‌های نفت و گاز توسط بانک‌های اروپایی به آذربایجان اجازه می‌دهد تا صادرات منابع انرژی خود به اروپا، از جمله به آلمان را به طور قابل توجهی افزایش دهد»
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19065" target="_blank">📅 17:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19064">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده:
چین خرید نفت خام ایران را حدود ۴۰ درصد کاهش داده است</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19064" target="_blank">📅 15:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19063">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19063" target="_blank">📅 15:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19062">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19062" target="_blank">📅 15:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19061">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31dabbbd67.mp4?token=Q_DsvoBlXMLcLqXkOJ6_MzKfJCiA2EUd6C8Rjfow7VpilbQuR7Im2K05lFfZaDsr2P8eaOUwjZfdYHsprWXMmjouaQNy-PVIgOBLdrH79ySB7yWOfBJ42HTCfVqXJYARQ0VN1pBjGZtdmPhnWQWZt3kXKJi7bLyX7Q5Kgbq4zNNu_SQlJMsbBzD__2PfPOBWrofXt-192s4hmEDHMWloPJjjAG6L8k-1w-tR6idKtGdCX-Og4CYv9Pu0GS82xvCh5dTtWmi09R7sTtXMiqTqgjhLNRcJeTN6_HlAgqGiAxrpXnCPnPGQ0eHRwpjvqXChNjvixN0Vycx8srT10o3_-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31dabbbd67.mp4?token=Q_DsvoBlXMLcLqXkOJ6_MzKfJCiA2EUd6C8Rjfow7VpilbQuR7Im2K05lFfZaDsr2P8eaOUwjZfdYHsprWXMmjouaQNy-PVIgOBLdrH79ySB7yWOfBJ42HTCfVqXJYARQ0VN1pBjGZtdmPhnWQWZt3kXKJi7bLyX7Q5Kgbq4zNNu_SQlJMsbBzD__2PfPOBWrofXt-192s4hmEDHMWloPJjjAG6L8k-1w-tR6idKtGdCX-Og4CYv9Pu0GS82xvCh5dTtWmi09R7sTtXMiqTqgjhLNRcJeTN6_HlAgqGiAxrpXnCPnPGQ0eHRwpjvqXChNjvixN0Vycx8srT10o3_-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای روزنامه جروزالم پست:  ترامپ پیشنهاد قطر و پاکستان برای آتش بس 10 روز با ایران را به شدت رد کرده و اعلام کرده حملات به ایران ادامه دار خواهد بود.</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SBoxxx/19061" target="_blank">📅 15:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19060">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ادعای روزنامه جروزالم پست:
ترامپ پیشنهاد قطر و پاکستان برای آتش بس 10 روز با ایران را به شدت رد کرده و اعلام کرده حملات به ایران ادامه دار خواهد بود.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19060" target="_blank">📅 15:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19059">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarket Podcast Text.pdf</div>
  <div class="tg-doc-extra">305.2 KB</div>
</div>
<a href="https://t.me/SBoxxx/19059" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 10</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19059" target="_blank">📅 15:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19058">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP6D54SHa2OEgEwVcCt9AXiqaApLlwWmWGzss7Lzd5tay6udK2WDVeKbsp3xoc1OlJxG47Imtl8j3sHRLJcF1x4DjoaCp8eyDT5zdwHvsjCXxQy_NLRNOx2S28Der00vo6GBHs9hRz6OSJjNTu1JsREK1_xjEyaD0YMxPqjIOX92lCEIxVyMWVKuI6vWqv-5YEOvksi66SD5QOO4L2jATZYzQM0v5JbA4U7WCaGQJPBWM1t8-mZ93cYqYZfKkddi_wSO810Rpou4yEoK4e4PPO2dpV3XQ9UxL6hpDQ_CiGhuxQRxib-wgmXvLMSqUdemz-WavIZO6lpRiEZdtFEiAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایینی قرار دارد و پیش بینی می شود طلا ابتدا ریزش و سپس رشد داشته باشد.
محدوده مناسب حمایتی 4015 الی 4020 برای امروز.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19058" target="_blank">📅 15:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19057">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 10</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19057" target="_blank">📅 14:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19055">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 10</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19055" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 10
سه شنبه 21 جولای 2026</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/SBoxxx/19055" target="_blank">📅 13:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19054">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حمله ایران به کویت، بحرین و قطر</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19054" target="_blank">📅 13:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19053">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ایران می‌گوید که زیرساخت‌های داده آمازون در بحرین را با موشک‌های کروز نابود کرده است.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19053" target="_blank">📅 12:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19052">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شما قدرت رنگ آبی را ببینید فقط که تا کنون این پایگاه کذایی «الازرق» حدود 15 بار درهم کوبیده شده اما هنوز نه تنها سرپاست بلکه بقیه هواپیماهایشان را هم می برند آنجا!  حالا اگر اسمش «الاحمر» بود با نخستین اصابت شاهد واقعاً در هم کوبیده شده بود!  آبیته!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19052" target="_blank">📅 12:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19051">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وزارت خارجه چین در مورد سیاست هسته‌ای ژاپن:  از زمان به قدرت رسیدن تاکیچی، نیروهای راست‌گرای ژاپنی نیت خود را برای احیای نظامی‌گری، رها کردن اصول سه‌گانه غیرهسته‌ای، جستجوی سلاح‌های هسته‌ای و ادامه مسیر نادرست آشکار کرده‌اند.  اگر ژاپن به تلاش برای اصلاح اصول…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19051" target="_blank">📅 12:20 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
