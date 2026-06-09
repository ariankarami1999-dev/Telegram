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
<img src="https://cdn4.telesco.pe/file/qj2z_LIJ9KATlMPj7pry0Pnn1SfbZ2jHkyQxAypfrH6NzFRfQZ4_Jjc2h0AZl9ijfheSneknI7j_VT5lA4lxvzVta0vnSycXceblP6G60uAgKd21SzZpn9k08clo2VqOhfsjQrVLbnstYa4mshxcpwYdfemONtY_t-Txyog0LfRHvUSrJ2p79QUo7TeTEP_IGg1E1Iv4uv-LuS5tX38sv3VDCqoxVSKBpZYLSY2qpnbXslDN_vzVCS5gbH6tSwmoymxInYUdPE7JCutYaqjihcXP_jm51LZOsG06YiiXkYW4F9KjVUTbA5DhgBbLwqvjiOjdHFXLzh7ZHlBRrg1asA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 227K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 16:54:32</div>
<hr>

<div class="tg-post" id="msg-65535">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5vMd16IFSeybtqJZUKK6r-z-rADIZPVqG9QWSzOIwPq_zlIFQGMWcXR2QI2WarrErgeRKDazmkaqv13lY03l91b8tJAUA3GVckLb6ijUtPwGR1qYOUG98i4CCTkRD2zC0eZmEvfWqKhMONbrFKX5HQnZmIhkQJAePRCLi4Vy5QIQO341OOpfNpRf-ENTiO1r-nDbEOtMTYO-Cz_g0YYSpAHTvb6zIGDF2z7yBXmKkdUFq1pCZr0bjmjq4QyfxQS-OhnTQ8Z7frdz6KEUEkqMaGSqMXtlb2Bu3YwIhyLnWHsx6l0lKEir-yD0OzZ9dzLhQpZtVoVGSfEJADoCbvmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐸
خان میرزا بلاگر ایرانی در حمله اسرائیل به عراق کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/65535" target="_blank">📅 16:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65534">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km3egB-XDG_WotW2KUlHjUMDTzJUpn-2dFPNuk7G0IsUwcV15JjsbAGKpErBjadSJ2-Tk-HGIxULnBxbGENjD64etvhJSvspVhTz5HWs3M66q4LKeNRaCsDaNE6ndsKdJqVmWz-jS-Gpl5DnTlKhLK9MySdPnE2YMwsS2xebSWjfJM3-uK35AmyorqFH1EoRL_cva-lIGlP1jWbYakn84AV3bhssWXmk6P4Zrrlg7r_x2_37S37SFtth4hi0w4_CB-qZFBbGB05SipQ7d7X7MTAlTs5fk11ncah7H7BNuOec4_qUfd0_fcuFgarFH8bvwWrCNdnFDvDcprgkMmf8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اکونومیست:
ایران و اسرائیل که برای دهه‌ها درگیر جنگی پنهان با تابوی حملات مستقیم بودند، اکنون آماده‌اند تا با شکستن این مرزها، خطر یک درگیری تمام‌عیار را به جان بخرند؛ وضعیتی که دونالد ترامپ را در برابر یک دوراهی دشوار قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/news_hut/65534" target="_blank">📅 16:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65533">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a4903bc1d.mp4?token=f_sEOfA7e662wv_cj8TgBnCHG5c01mfl_2nH9sY_iQ7q8qqR1VrcdTbbI7LxyoNVbzmMtYoFLz8IbYV6a33BCMMAFuYCWf03ZUkMZnSBXz5OmzojrK29_gcziMk8UeU-X3cs9TR1Quc7gqC8vyuvPiQUOaJWNRNPj25ffAbCxyAeIkR5Px20saywVoOdmicm1K5F7Pn56Dqs0PJApcF1DslzHeCafoXiqE7D2aoKPpR59AJWQ9tHQML5AeMSmhXcfqTz4LF3TDUjkf3Y38X0Vp-yKBUFaayzL8KdXDjmbgrfoUX6codYkbjeAqotRQ0FLYyUUb808oP_PJpq8UaXRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a4903bc1d.mp4?token=f_sEOfA7e662wv_cj8TgBnCHG5c01mfl_2nH9sY_iQ7q8qqR1VrcdTbbI7LxyoNVbzmMtYoFLz8IbYV6a33BCMMAFuYCWf03ZUkMZnSBXz5OmzojrK29_gcziMk8UeU-X3cs9TR1Quc7gqC8vyuvPiQUOaJWNRNPj25ffAbCxyAeIkR5Px20saywVoOdmicm1K5F7Pn56Dqs0PJApcF1DslzHeCafoXiqE7D2aoKPpR59AJWQ9tHQML5AeMSmhXcfqTz4LF3TDUjkf3Y38X0Vp-yKBUFaayzL8KdXDjmbgrfoUX6codYkbjeAqotRQ0FLYyUUb808oP_PJpq8UaXRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
❌
گلایه یک زن حامی رژیم (پرستو) از رفتار بسیجی ها بعد از آتش بس
@News_Hut</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/news_hut/65533" target="_blank">📅 16:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65532">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
نیروهای رضوان حزب الله اعلام کردند بصورت زمینی وارد شهرک های اسرائیلی شدند
@News_Hut</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/news_hut/65532" target="_blank">📅 15:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65531">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
شبکه ۱۳ اسرائیل:
شورای وزارتی کوچیک تصمیم گرفته هر حمله حزب‌الله به اسرائیل را با حمله به بیروت جواب دهد
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/65531" target="_blank">📅 15:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65529">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDR1AHo1D8U9D5ALJtMQptL1yw9Jj62QrAOG_fjL3nVN5D1YdiPzwK72zrQ7tkeUY9gDrYIN54tKIaq4XdRK9yPmNGHChzrO1-HdFo3_PacuOYQqzS0oPORlnmd1RZ7ESjB5Oj-17yVtCHEBTbluRAptDZGwk5JRsrl7qjXy1MZ74gQZPfvm2a2oUyMjiccjZnEXq2Bm-3YDKb6UQ1zIVTGn4OgEFmGnMdSJXmP3IWdQhw0kgLyW0TYzbUNuZ7qRmxLOzx27lONAotmj6VytNDEOnaQYp7Q8R2rAdAwcm6htCMF7jctxy4WTMUL3ceu1eqDF9NgDV_a0OYkQLfWb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHzXqbbY_k8iLZ7j73ooZpKBUFHsRSFNkAeE0qndpevylv3BdyQcR78dzzvjAlcKrqOBGbIlmn4OaFnzrTWW0ONStVvy95WaMo0ZI03i8l15dImOMQnYU96BS6duj6aMDHykEAoaRSAg9eRyQz8_ltQLIuwO0rl3HVQBxnhzbBmW9IvaY8_9OgjDMNFkebkUvNP9uVStpZ0fKeN9CJ8aaWgJvu07AxNJgupW1fi9Zx4wuRQ46gVpH_bGumJTHZUTaYh8AUKoqMzMTg8srzuHxn49jxmRebrQ7U_IWBcUO0L2oeHnC5rLMhwwXG7x3tt2WjbcTeDNUhBjjZj1FXfgSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
حمله هوایی به شهر کوثریه الرز جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/65529" target="_blank">📅 15:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65528">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
ستاد فرماندهی مرکزی ایالات متحده:
دو خدمه بالگرد آپاچی ارتش آمریکا که در ساعت ۳:۰۳دقیقه بامداد ۱۹خرداد به وقت ایران در نزدیکی سواحل عمان هنگام گشت زنی دچار حادثه شد و سقوط کرد توسط نیروهای آمریکایی نجات یافتند.
همچنین علت این حادثه در دست بررسی است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/65528" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65527">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4b9120bb.mp4?token=Fom-W_bIVW0jlqbpwRINhgR6nWteUKojDszlJPDnxjgin26bAJYH1ZnS05RfeCjgGw0vbHK54lre8xl2kN-3aSZr6uPpJNdlFP0c0c5DVdFbk5HpqopjXSmGMuwL-hKGEU3JEFeQRjNrc1VT4TzbQ2lSns-tLhTX53DjM2V7rm5uFDI40Ww57ZtCWFY_C1vuQS7_6ZHVcBt0PRQ_mEAKCxcpIv5PUV_QPXFr3eBhbgEq0hK9hZZ-z9GWpluMOB1wNTYQRfFDvHUHWJJqOe4ebAgdGxrUlbB9E4poHl4T4EfLoNelvOUZtTB8bHtdJWY53ocOdoUW1SDvVJpZb98DuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4b9120bb.mp4?token=Fom-W_bIVW0jlqbpwRINhgR6nWteUKojDszlJPDnxjgin26bAJYH1ZnS05RfeCjgGw0vbHK54lre8xl2kN-3aSZr6uPpJNdlFP0c0c5DVdFbk5HpqopjXSmGMuwL-hKGEU3JEFeQRjNrc1VT4TzbQ2lSns-tLhTX53DjM2V7rm5uFDI40Ww57ZtCWFY_C1vuQS7_6ZHVcBt0PRQ_mEAKCxcpIv5PUV_QPXFr3eBhbgEq0hK9hZZ-z9GWpluMOB1wNTYQRfFDvHUHWJJqOe4ebAgdGxrUlbB9E4poHl4T4EfLoNelvOUZtTB8bHtdJWY53ocOdoUW1SDvVJpZb98DuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید از ساشا سبحانی حرومزاده و آقازاده‌ جنجالی حکومت درحال عشق و حال با پول مردم در خارج
تو این ویدیو به دوست دخترش یک ساعت طلای اودمار پیگه به ارزش چند ده‌ هزار دلار هدیه میده
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/65527" target="_blank">📅 14:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65526">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
حمله اسرائیل به شهر ساحلی صور در جنوب لبنان  @News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/65526" target="_blank">📅 14:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65525">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
فاطمه مهاجرانی، سخنگوی دولت: میزان قطعی‌ برق در روزهای گرم پیش‌رو به میزان همراهی مردم عزیز بستگی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/65525" target="_blank">📅 14:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65524">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0689b8dc9.mp4?token=rzrZ44NUsa55ziP7hUbDTmqgtlLo7dBvgyJm4D47uiPJLZjcGFRB97chKu4ee8iftBfzv8uCSoPDr32SJMzLZ3I4H_cLL9hgyVbyRNR916WTDd5eik94D2-1_T59D4g5Dxz3dLoXIUPFtUwjW1T2fiVJlth0piB2VvsM5Nee25rOeS1F-jsYVmzDON_d0anToM7KDGmjW9iLo5xYx_jnLOoEoFkpoNm-3M0o57S0m5sRODS_CSJjb2Dkh_QpNSjq9hGrb55sX6CDaql2uvHzqchHijLveylzxAS9OEzPhcrs9EGYTE9peOdVQRLgT8c2Z_DaRHfA7BZaqN2GN2DWO0ejYw8LgAE-_J8-uj9n7RfJW_pebnyZbr5-vMkWsQGiahcPKFLzLzqobWTdn_KVtzykusuGsznfOMP0YREkb0AnG3KpbhZbQYyIHbEyob8_yd-eLvThTbtBPgkYccj4t3k12QDWjFAanMaFXjLehl617ju4PZtIHllKL7ISwgl9NJhtvuKpCjaFdZ9lW6GBdjr9g8r2LIKUMtTIXdkeNvy4p1iSUp51NQ-hriaW2Op7n5tV4Bw5-zlgljc5NQyJnFEqSm5YfTch0qbdZviTl3-RxPXH_D5Z0tkmIeMdYVYOgqFCPznyKM-4ZuQIiBX_SZZsoI-KcsH6sATu0knP-j0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0689b8dc9.mp4?token=rzrZ44NUsa55ziP7hUbDTmqgtlLo7dBvgyJm4D47uiPJLZjcGFRB97chKu4ee8iftBfzv8uCSoPDr32SJMzLZ3I4H_cLL9hgyVbyRNR916WTDd5eik94D2-1_T59D4g5Dxz3dLoXIUPFtUwjW1T2fiVJlth0piB2VvsM5Nee25rOeS1F-jsYVmzDON_d0anToM7KDGmjW9iLo5xYx_jnLOoEoFkpoNm-3M0o57S0m5sRODS_CSJjb2Dkh_QpNSjq9hGrb55sX6CDaql2uvHzqchHijLveylzxAS9OEzPhcrs9EGYTE9peOdVQRLgT8c2Z_DaRHfA7BZaqN2GN2DWO0ejYw8LgAE-_J8-uj9n7RfJW_pebnyZbr5-vMkWsQGiahcPKFLzLzqobWTdn_KVtzykusuGsznfOMP0YREkb0AnG3KpbhZbQYyIHbEyob8_yd-eLvThTbtBPgkYccj4t3k12QDWjFAanMaFXjLehl617ju4PZtIHllKL7ISwgl9NJhtvuKpCjaFdZ9lW6GBdjr9g8r2LIKUMtTIXdkeNvy4p1iSUp51NQ-hriaW2Op7n5tV4Bw5-zlgljc5NQyJnFEqSm5YfTch0qbdZviTl3-RxPXH_D5Z0tkmIeMdYVYOgqFCPznyKM-4ZuQIiBX_SZZsoI-KcsH6sATu0knP-j0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حمله اسرائیل به شهر ساحلی صور در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/65524" target="_blank">📅 13:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65523">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
‼️
مصطفی پور دهقان نماینده مجلس:
وزیر ارتباطات دستور داده یوتیوب بزودی رفع فیلتر بشه.
«در صورت رفع فیلتر شدن به دلیل تحریم بودن ایران درآمد یوتیوبر های ایرانی قطع خواهد شد»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65523" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65522">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c1be7dc2.mp4?token=vEoLhJe8LJWHiIM1ELQO-f5-KDkjCSVhzLWC4FAAQ5G_Cxna6zXfRTaAMGMWwPGoddPsw2yApm7cHRGQ8DjS6ssa6nwXcP7SXEvPqS8cDwDrFqmBPnIhFx2UkvIw-MUqMVsTcCRpW50A1nFPKuoMyWlB-FNy7qgvYIaaPT-Ti7_-QYkhdfqw7yd0eJ966GCXqRkhR9Jv7E2IXeYGjr9gdxQEDPM0Biv9ErJZ1ktzREr45j1Bk0X-kbWRHwYcaxafvP-WoNpUfk_tzDAo_iIZYWv8hD39uZZaglFuaCLbs6ptN2xIYcLnCQjl0c_JjzxOQabF231ewazABYllCo3k5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c1be7dc2.mp4?token=vEoLhJe8LJWHiIM1ELQO-f5-KDkjCSVhzLWC4FAAQ5G_Cxna6zXfRTaAMGMWwPGoddPsw2yApm7cHRGQ8DjS6ssa6nwXcP7SXEvPqS8cDwDrFqmBPnIhFx2UkvIw-MUqMVsTcCRpW50A1nFPKuoMyWlB-FNy7qgvYIaaPT-Ti7_-QYkhdfqw7yd0eJ966GCXqRkhR9Jv7E2IXeYGjr9gdxQEDPM0Biv9ErJZ1ktzREr45j1Bk0X-kbWRHwYcaxafvP-WoNpUfk_tzDAo_iIZYWv8hD39uZZaglFuaCLbs6ptN2xIYcLnCQjl0c_JjzxOQabF231ewazABYllCo3k5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون با کفن رفته تو زاینده رود و از پزشکیان میخواد وارد دولتش کنه تا مشکلات کشور رو حل کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65522" target="_blank">📅 13:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65521">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63397f42b5.mp4?token=b6Xeur1mtlxP1BbzxiG-RpvQp0XOZ9HdBJNzTtq-PysJEo3zrWyc9himyb4XtUYHOmdPV1zXQ7A0bEzYWfBrww1f12785BKlKJf8lihOwMxLCvrfo1Bm5K8iM2swONn0Rd7fRM6uQZmW23j0efO_p7WSWFbSPAe7Z3_FhyMo3GyZQqsBqKHVLu6quemv0MZGIPVBGw_u4w9WtiT59pDShvA5Otu3rL68vUckLPZu2fxXZvssQfRjjGc0Of5H_0nV5yIXQPChRWAKlwgd-NUfs9A5TtjJjNPrIWcirz9FG67_v9mdoZeyq3MhCBRzjfAGCcaKVffQsG4xNCtLOVLj_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63397f42b5.mp4?token=b6Xeur1mtlxP1BbzxiG-RpvQp0XOZ9HdBJNzTtq-PysJEo3zrWyc9himyb4XtUYHOmdPV1zXQ7A0bEzYWfBrww1f12785BKlKJf8lihOwMxLCvrfo1Bm5K8iM2swONn0Rd7fRM6uQZmW23j0efO_p7WSWFbSPAe7Z3_FhyMo3GyZQqsBqKHVLu6quemv0MZGIPVBGw_u4w9WtiT59pDShvA5Otu3rL68vUckLPZu2fxXZvssQfRjjGc0Of5H_0nV5yIXQPChRWAKlwgd-NUfs9A5TtjJjNPrIWcirz9FG67_v9mdoZeyq3MhCBRzjfAGCcaKVffQsG4xNCtLOVLj_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آذری‌جهرمی وزیر ارتباطات دولت روحانی و از بنیانگذاران فیلترینگ در ایران: اقدام به قطع اینترنت و فیلتر کردن جوابگو نیست
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/65521" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65520">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65520" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/65520" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65519">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBaYm8qrsGgQr4YaVwUWw1pcmmhHcMUqdWHYVvX4t_MPW8ycwgCrTpqqM99YOjXrY1IbyTNZPFHctga1drP60cAmLLrVavRmvDLqO1uV49tj7ZefnCfA3AJ6HnPAfxlfOSGae9D_zSY7uVHuTY6Mv5_tZzIq5OUhTT1aoO5BpKLXp0t0YvHH2Zt4gOJQq-VkGoUmEnM9I41Y5csBCs0pX3saWVVIt5-PhXfcfKm-tQRnVY1m2MXm0hYrf73_Cth6PkE1iWR1_77pQfJ0Gs1F_dd-xrd7YwTncnza1QwFAmiUmReVH1_pzZyrrMg073XkbJcypcyuwfaCLQdKPIquEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/65519" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65518">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd926c0a3.mp4?token=BbgB484KfhmoFwCTwMC-f8sjNlEygN9MnlxURApQlvHXUGld7uAOofCPp_QWQCJl4fBY6dHX7i1I3zugTyCurd1YwpUfkP1OwnhHYtEXq6tWOMmIHq4k9cSiPAObc8vT35aFUDGa7o073i4agwWKrtyqyJQcerfu_0khU_20OOM5mD6a4v172dOH-kiWAmJk--4aSXbtamLtZIkt2XHDny5cJlEr51BwmYZkNOwNwt35LFoz1BUol0UOhHNGSTZmTpnuC21ThDORO2BaoftFRS7SJpbrPDJ6gbnPeGyW_3vRL7eHIBDCdaMghJkFpyzi8llqVtC_Tb6yJdWIhmNF7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd926c0a3.mp4?token=BbgB484KfhmoFwCTwMC-f8sjNlEygN9MnlxURApQlvHXUGld7uAOofCPp_QWQCJl4fBY6dHX7i1I3zugTyCurd1YwpUfkP1OwnhHYtEXq6tWOMmIHq4k9cSiPAObc8vT35aFUDGa7o073i4agwWKrtyqyJQcerfu_0khU_20OOM5mD6a4v172dOH-kiWAmJk--4aSXbtamLtZIkt2XHDny5cJlEr51BwmYZkNOwNwt35LFoz1BUol0UOhHNGSTZmTpnuC21ThDORO2BaoftFRS7SJpbrPDJ6gbnPeGyW_3vRL7eHIBDCdaMghJkFpyzi8llqVtC_Tb6yJdWIhmNF7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
مقاومت فوق‌العاده یه برج ۳۶ طبقه فیلیپینی در مواجهه با زلزله دیروز ۸ ریشتری در این کشور
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/65518" target="_blank">📅 12:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65517">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارش باحال حمید معصومی‌نژاد تو ایتالیا از آخرین روز مدرسه تو این کشور که دانش‌آموزا اینجوری همو با آرد و‌ تخم مرغ و ... به کثافت کشیدن و جشن گرفتن
😂
اینجا هم بچه‌های بیچاره هرروز بخاطر تاثیر معدل کنکور تجمع میکنن که به هیچ‌جای هیچ مسئولی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65517" target="_blank">📅 12:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65516">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTwiLoIr7DO4cuszYNQUaNj4jMB3Polp0FcwBopFg0q_AWZPphyUKYGSmvqypcwdrZi1-rBg1lXg4_m8xsqNuS6wBKgUMBlO-6XhfbD6IZssXl8HwnbIUDd_St1IFTLU2PjDi42AO2shrhWWtBntPm5MbdHgLDtp2Tn7Gt4ueDjOGuOq5hH4XLW5JAr12bRd23vf07pzmGzfFsPcHn2U7cpgz6WEjGMZw7B8hSZiICy8wuCynu_gSyalHQGnZJUMHBZzTpep_BTyg4lJdef2Dnv-aAP0ivR9UN-99oZhdhgXDqFiZx7S_ezn3Qes3LjSa5AoyfWX56peDx8w4QPPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
سفارت جمهوری اسلامی در بیروت بجای مردم ایران اومده گفته که لبنان قلب ایرانه و خب گوه خورده
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65516" target="_blank">📅 11:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65515">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇮🇷
ستاد دفن و خاکسپاری علی‌خامنه‌ای اعلام کرد که مراسم خاکسپاری رهبر دوم ترور شده حکومت حداقل تا بعد از دهه اول محرم برگزار نخواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65515" target="_blank">📅 11:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65514">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
جی دی ونس معاون ترامپ:
مواردی وجود داره که منافع اسرائیل و ایالات متحده متفاوته.
هدف اصلی ایالات متحده در مورد ایران اینه که اطمینان حاصل کنه تهران سلاح هسته‌ای نداره.
ما می‌تونیم به توافق هسته‌ای بلندمدتی با ایران دست یابیم. ممکنه اسرائیل این موضوع را نپسنده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65514" target="_blank">📅 11:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65513">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد ایران:
اگر حالا ما برویم و بمباران کنیم «که اگر بخواهیم می‌توانیم خیلی راحت این کار را انجام دهیم» و دو سه هفته دیگر آنهارا بمباران کنیم، آنها دیگر هیچ چیزی نخواهند داشت.
اما شما تنگه را برای ماه‌ها «باز» نخواهید دید. اگر ما بمباران کنیم، می‌دانید، افراد زیادی کشته خواهند شد. چه کسی می‌خواهد این کار را انجام دهد؟ من نمی‌خواهم.
ما یک سند امضا شده خواهیم داشت که در واقع از انجام بمباران قوی‌تر است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65513" target="_blank">📅 10:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65512">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا از نتانیاهو خواستید که حمله را تلافی نکند؟
ترامپ: نه، من گفتم کاری را که درست است انجام بده، اما می‌خواهم هر چه سریع‌تر متوقف بشی چون آنها باید متوقف شوند.
این مربوط به لبنان بود و باید متوقف شود. ما می‌خواهیم کار تمام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65512" target="_blank">📅 10:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65511">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
ترامپ درباره نتانیاهو:
به نتانیاهو حمله شد و او هم متقابلاً پاسخ داد و من نمی‌توانم او را به خاطر این موضوع سرزنش کنم، آنها را هدف قرار دادند. آنهاهم متقابلاً پاسخ دادن و حالا درگیری را تمام کرده‌اند.
بنابراین، آنها قرار است فقط برای یک هفته دیگر یا چیزی حدود آن، یکدیگر را به حال خود رها کنند.
این وضعیت خاورمیانه مدت زیادی است که ادامه دارد. اگر واقعاً بخواهید بگویید حدود ۳۰۰۰ سال اما مطمئناً ۴۷ سال است که اینگونه ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65511" target="_blank">📅 10:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65510">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران:
ما اکنون در حال مذاکره هستیم و آنها می خواهند معامله بسیار خوبی انجام دهند. آنها حاضرند همه چیز را به ما بدهند. آنها حاضرند به ما "هیچ سلاح هسته ای" بدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65510" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65509">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
🇺🇸
🚨
🚨
ترامپ اعلام کرد در دو هفته آینده "پیروزی کامل" را بر ایران اعلام خواهد کرد!
ترامپ: من فکر می‌کنم که ما در آن نبرد پیروز می‌شویم، اما شما واقعاً در دو هفته آینده که پیروزی کامل را اعلام می‌کنیم، پیروز خواهید شد.
این یک پیروزی کامل خواهد بود. خیلی زود این اتفاق می افتد و قیمت نفت پایین می آید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65509" target="_blank">📅 10:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65508">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
🚨
🚨
ترامپ درباره ایران: ما هر چیزی را که برای تخریب وجود داشت، نابود کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65508" target="_blank">📅 09:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65507">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8bb28ac6.mp4?token=V2dz-pwYT9q2ABqzyU_k513A7fqrsbEsukPhC1eGZ3cS3uVq8Q-NcN4lOaU8ro_JCFELVzGi1Sy8Gl2BPDLwqoEwU1C6YqnXamv1IFkJHCiOxlQwe-mtq4thcml_QD98fvouctcePtbE5Tv4TSr143HAH5DVfeUUc1LfwTB01rvKW8wVgwl9kK2DIdkby0bRL3EzaAxG3kxrBq-TNqhHK6aVpiGqtTs-xYShCnrz8tlqWObibvyw-k55iLOhu8sSVboRos6Jdc7VU7Srr6o4Cxs2OeynTxpjICW-9NH7DXeIlWhqfNKhnQa9bRomBCuh_6e69tNQ2GU2WsqmA0_UGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8bb28ac6.mp4?token=V2dz-pwYT9q2ABqzyU_k513A7fqrsbEsukPhC1eGZ3cS3uVq8Q-NcN4lOaU8ro_JCFELVzGi1Sy8Gl2BPDLwqoEwU1C6YqnXamv1IFkJHCiOxlQwe-mtq4thcml_QD98fvouctcePtbE5Tv4TSr143HAH5DVfeUUc1LfwTB01rvKW8wVgwl9kK2DIdkby0bRL3EzaAxG3kxrBq-TNqhHK6aVpiGqtTs-xYShCnrz8tlqWObibvyw-k55iLOhu8sSVboRos6Jdc7VU7Srr6o4Cxs2OeynTxpjICW-9NH7DXeIlWhqfNKhnQa9bRomBCuh_6e69tNQ2GU2WsqmA0_UGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چندین حمله اسرائیلی در جنوب لبنان، در مناطق اطراف صور گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65507" target="_blank">📅 09:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65506">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
🚨
🚨
مقام ایرانی به الجزیره:
واشنگتن در پیش نویس یادداشت تفاهم تغییر ایجاد کرد و این موضوع غیرقابل قبول است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65506" target="_blank">📅 09:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65505">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
طبق گزارش
نیویورک تایمز
، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65505" target="_blank">📅 09:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65504">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=nMpcWrfEkaHkEaukRbTHobnH8wGMFKKA9G0jNMHDS3GAItn1Co_BqUBCJgjgrIzbLt0pmznKKrmr73gEJUfCYXialsRzV8sVykt06ta_pVcsFyJLjAe-m3tnPCyGVOmTywQP9-2HJY1xlYpylt2k6HzuKdwTEEovlQhLovo5vPTZZ61E1fmyo4UHsz6QmZdkZ5-nVeUsnqzBaA7ROrPz8uP2Iq8gqREG0NVfYkjG2xDsM6zTeL966etcrx8QOkEC3m6uIaSAAf9IYe1uQzMQHBkuPpFjG8H48T0rySdsMUw2Ol4KFW5eJ1n-ilt522MieS-D43W2leZzyQBkh_hi6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=nMpcWrfEkaHkEaukRbTHobnH8wGMFKKA9G0jNMHDS3GAItn1Co_BqUBCJgjgrIzbLt0pmznKKrmr73gEJUfCYXialsRzV8sVykt06ta_pVcsFyJLjAe-m3tnPCyGVOmTywQP9-2HJY1xlYpylt2k6HzuKdwTEEovlQhLovo5vPTZZ61E1fmyo4UHsz6QmZdkZ5-nVeUsnqzBaA7ROrPz8uP2Iq8gqREG0NVfYkjG2xDsM6zTeL966etcrx8QOkEC3m6uIaSAAf9IYe1uQzMQHBkuPpFjG8H48T0rySdsMUw2Ol4KFW5eJ1n-ilt522MieS-D43W2leZzyQBkh_hi6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
یک کارشناس حکومتی در صداوسیمای جمهوری اسلامی: آمریکا در جنگ ۴۰ روزه بیش از ۷ تا ۸ هزار زخمی و دست‌کم هزار کشته داشته! کشته گرفتن از آمریکایی‌ها و اسرائیلی‌ها برای جمهوری اسلامی کار سختی نیست و ما به درخواست کشورهای منطقه خویشتنداری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65504" target="_blank">📅 09:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65503">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65503" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65503" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65502">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhmVmANRKti-GcOwZr7EwSxfG6X6606yEmTVm6rxBO6lU8AcO3IbYX-yFsGmFFUUNmgdi3ynDB0j-W-wrmi92FQlKtSs2__C_kCa7ChDVwB-kGQMO6YAW8-UXbvMqQ1-cp4fyhx5VAcDkPDokKEx6oflGI08UIP4qlbQExuuiDPm9hvLfGP8oM6dNBo5XrdsrxfdJTlbM6cOOszchWNrK2yNNBmkF3IWxMdPHl2F6R9bMfjt26mhUoQdSZtd0AZKQCz1YEBHuYY82Zi7LnAF2TSwtQA1Z8A2ssGWuhgxsix49IyE3jIzqFvOJVn6OdvAP12TMgYNldo6g7mqOH5ffA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65502" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65501">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN72SE3JcM1JgH0a1lT4pZH6J2zORUJfkTT8i7I2tSYogYtsvoIvvN9v2MIRPJ7PeefxCr63vBzWCmmQAGUM56RhTQwrzEnVJ_cFCwQjUfK2Fo5qz9NvVtPrGDJmBVqRP-cXhFcIjgmEGcFO7uayCnptETZVOqvW5QS2sWf3nSUjx61i46G9TgyoJukfmN5qnkYHNkk_FRg3PI9kHpVBsoCeYjBad6m2iqo58OE8JGP083f_v8uKnBSlEbMstDKfFmhkbTOI8hyGkW_bvzV_8BSExbxBAwE1URlY80v37DU5ju62bidaJMzHdKjK3HNKwc1egPSt_BZggVubRrxU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
اونایی که
۵ ماه
پیش وارد شدن الان
۲.۵ برابر پولشون سود
دریافت کردن
دو فرصت
ویژه
در
سرآوا
برای شما فراهم شده که با بازدهی فوق‌العاده می‌تونه مسیر جدیدی به سوی
ثروت
براتون باز کنه
✅
اگه توام‌ دنبال یه‌راه میگردی تا بتونی درامد خودتو داشته باشی به خانواده سرآوا ملحق شو:
@Sarava_Finance</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65501" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65498">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
مهدی خراتیان تحلیلگر اصولگرا: در ۱۸ و ۱۹ دی ۱۰۰ شهر یا سقوط کردند یا در آستانه سقوط بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65498" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65497">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
♨️
🚀
خبرگزاری فارس: انصارالله یمن با پهپاد به سرزمین‌های اسرائیل حمله کرده
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65497" target="_blank">📅 00:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65496">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇺🇸
ترامپ به اکسیوس: ایران می‌خواهد به توافق برسد و این اتفاق می‌تواند به زودی رخ دهد
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65496" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65495">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7093313be4.mp4?token=S-bscZHxpLs9xsMTxbUNiW-thvQcJqwO5DC3Olo4Sqvi_NuzuF8mufCyEosxFscQSMJ7lkYSmCcKG1C6bC5P4zlGC1NytDyv9W4l5Mhj7H-jnnGip4CUllrDcpM2vij0_4rB6hB_bW988qoQJX7CHNgr6KoPgkkQpnfW_8YuBEZF4LW9D7w-EEf-YDcKNqkWghwK1jZPJFsIUO0hf_KlH-sS_mUWN5EGGnl7NOSlWuLP1GNk3wlyHAfsy6iH2GLSZ1RpOCtGU4bENWJ6wSCSRbu3LuZlFrmI4DO2IAB-S4U-r_TMsf7RFCLQweadTm757i2O7MTREalnIqlBHUIVHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7093313be4.mp4?token=S-bscZHxpLs9xsMTxbUNiW-thvQcJqwO5DC3Olo4Sqvi_NuzuF8mufCyEosxFscQSMJ7lkYSmCcKG1C6bC5P4zlGC1NytDyv9W4l5Mhj7H-jnnGip4CUllrDcpM2vij0_4rB6hB_bW988qoQJX7CHNgr6KoPgkkQpnfW_8YuBEZF4LW9D7w-EEf-YDcKNqkWghwK1jZPJFsIUO0hf_KlH-sS_mUWN5EGGnl7NOSlWuLP1GNk3wlyHAfsy6iH2GLSZ1RpOCtGU4bENWJ6wSCSRbu3LuZlFrmI4DO2IAB-S4U-r_TMsf7RFCLQweadTm757i2O7MTREalnIqlBHUIVHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سپاه پاسداران حملات موشکی و پهپادی به پایگاه‌های آمریکایی و گروه‌ های کرد در نزدیکی سوران، استان اربیل، کردستان عراق انجام داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65495" target="_blank">📅 23:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65494">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a7fe1ed4.mp4?token=hzoeZHq0CiAQQ4IXpPFt_PUryY7_jJHlEaJR9Am9MTMZzeJyTdFg6_O_qDi0rEXYuYx6_d4fyo-1gTfvkyTwXBL6wXGBTeVAFtc5-YNVhLy8OHPl2DhqlK1Jxo_H183koS7h2sLqtJ-VXOR5MwPZXeQWdUSfaLJwGsGTqbWXv66Wweu7pjq-EKJIIU0RhbQIeYQMvwP1rCVaeoD2Lm7SBsJH15pFZQpRKemshjvm8_17zz2pAMfQRvemkTZEK5Ts7DOO0hL_19VxEJHnHp6rF5B4sxMis6JpRXqPUfbRZzTznoErStu9oVccoWwCDnte9AF0FDn5dh9Dx9C5hBh3UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a7fe1ed4.mp4?token=hzoeZHq0CiAQQ4IXpPFt_PUryY7_jJHlEaJR9Am9MTMZzeJyTdFg6_O_qDi0rEXYuYx6_d4fyo-1gTfvkyTwXBL6wXGBTeVAFtc5-YNVhLy8OHPl2DhqlK1Jxo_H183koS7h2sLqtJ-VXOR5MwPZXeQWdUSfaLJwGsGTqbWXv66Wweu7pjq-EKJIIU0RhbQIeYQMvwP1rCVaeoD2Lm7SBsJH15pFZQpRKemshjvm8_17zz2pAMfQRvemkTZEK5Ts7DOO0hL_19VxEJHnHp6rF5B4sxMis6JpRXqPUfbRZzTznoErStu9oVccoWwCDnte9AF0FDn5dh9Dx9C5hBh3UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
رژیم جمهوری اسلامی با موشک به کردستان عراق حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65494" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65493">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
رئیس جمهور لبنان:
اگر حزب الله از تحویل سلاح خودداری کند، مردم از آن روی برمی گردانند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65493" target="_blank">📅 22:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65492">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
قالیباف:
هدف مذاکرات پایان جنگ و ایجاد امنیت پایدار است، نه عادی‌سازی روابط با آمریکا. ما نمی‌خواهیم از طریق تسلیم یا شعار پیشرفت کنیم؛ بلکه باید به دنبال پیروزی مهندسی‌شده با قدرت و عقلانیت ایرانی باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65492" target="_blank">📅 22:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65491">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
نتانیاهو به وزرای دولت خود:
ممکن است به چند دور (جنگ) دیگر با ایران بازگردیم، این پایان کار نیست
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65491" target="_blank">📅 22:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65490">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnriTGykiDe0B7te9kmZl4FGkMnpoWRRvDHsETggA1AukC4lJR_B2x6sSF0zyWMARy3EdTzxqf014_Ro_ZlHCOQre5-LIE_Do-EBofq8j7oAoAc2iiMIAj_xedu1pVp9SSLFBW3BPjSojr-AasSetxyzU00qbo-86JXtw8rpka7nTow-n5azuU0GuS7mVpbA-ySIWm1YBLdMUIp7c7tZcRKQXnUnmdpOq13vv6F3X80E9YCF2dC5f0hUS4HbCkminqobZCczigLeR7nS6zMRYsZzvpd4JGm11DTIB8RIIxTnFV1d3n3udu7BRT2NOCGm-UQf4rYu8TN8ykgBE9buzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرژانتین
🇦🇷
-
🇮🇸
ایسلند
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
ورزشگاه جردن-هیر
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آرژانتین در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایسلند در
۱۰
دیدار اخیر خود،
دو
برد و
سه
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرژانتین
۲
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایسلند
۳
.
۵
گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65490" target="_blank">📅 22:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65489">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNuSTVIh0pmAhVzvP4zKzP5-xSw5fAC4_X5fYEygP-UdJ9EVMO4dsaEdtplJsvXzpRhYIDvJuLAyUzmp3wmNygQlgEpo_-cQoQhQfVn3aGIHpAEiwaWDvJx32zMEWju7PQT2ZZzVY8X1kQlk9YDDx6ENJO0a3stMbIXK24_4vuDy7UuVEOFXfv1bE9X92lKrJyTUiSS3AYEvO89XxROH2NyUOv3k_16oPQnZM3xhGBNJt4HA9ahQ5ze_8fI2OspsEJwr2PvjUhovCyRjroYlIGaa3R8fjDz5Ool0b-BzKV6oGM7N6NAEpeq_yQD0yg_Rz9nl8yLUPHW17GIFOkoloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
صابرین نیوز با انتشار ویدیویی از شاهنشاه آریامهر محمدرضا پهلوی سعی در مشروعیت بخشیدن به موضوع کمک به لبنان دارد
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65489" target="_blank">📅 21:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65488">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
مردم ایران بهتر از هر کسی می‌دونن که تا وقتی جمهوری اسلامی سر کاره، نه ایران روی آرامش می‌بینه و نه منطقه. صلح، امنیت و پیشرفت واقعی فقط زمانی به دست میاد که این حکومت دیگه بر سر کار نباشه.
راه‌حل، مذاکره با سپاه و مسئولان جمهوری اسلامی نیست، راه‌حل اینه که دنیا کنار مردم ایران بایسته و از تلاششون برای رسیدن به آزادی و پایان دادن به جمهوری اسلامی حمایت کنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65488" target="_blank">📅 21:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65487">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی :
این حکومت سال‌هاست مردم ایران رو گروگان خودش کرده و از جون و مالشون برای پیش بردن جنگ، ترور و بی‌ثباتی تو منطقه استفاده می‌کنه. توی این درگیری هم مثل همیشه، هر آسیبی که به زیرساخت‌های ایران یا مردم بی‌گناه وارد بشه، مسئولیتش با جمهوری اسلامیه. این رژیمه که کشور رو به این شرایط کشونده و هزینه تصمیماتش رو مردم عادی میدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65487" target="_blank">📅 21:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65486">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی :
جمهوری اسلامی باز هم برای حمایت از حزب‌الله ، کشور رو وارد یه درگیری نظامی دیگه کرده و بار دیگه نشون داده که منافع مردم ایران براش هیچ اهمیتی نداره
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65486" target="_blank">📅 21:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65485">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
ترامپ به کانال ۱۲ اسرائیل:
به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت!
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65485" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65484">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
ترامپ :
اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن.من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه!
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه من هم با نتانیاهو صحبت کردم و اون در نهایت موافقت کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65484" target="_blank">📅 21:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65483">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
سازمان هواپیمایی کشور: حوزه هوایی کشور به وضعیت عادی خود بازگشته است و عملیات پروازی طبق اطلاعیه‌های پروازی صادر شده (NOTAM) از سر گرفته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65483" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65482">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103c84b28e.mp4?token=QylxJUy_QVr2MyzCvLqx5pGbNwScVuDjph9sgPWBMX32OJnBctdAXCkmHuPVrzXVMifR_hni4xlZcDYzS_CSpBMEDyRtjcfK-4oZfVsKGvMznTGTG3jujuQ-AktQsA5mwcTGLCALyH17dM6ozGaQnZbXFGEMjRJYGxSTIEBbgGuZdVpcY_-ErPspCh0TKhr0E36Z3uodmlFwbZF69aXS0BIU9DUaOmpNqGPDTL5QwwRDwKQck9va_80L21iVFAhmn9wrtYlmsomKMXl4XTNUqgWCebDAnF3sUofd9iLFKfCf74XPJSEfuYSL0Vj3_7kY8Ov65bepaBLe8hrIV6iZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103c84b28e.mp4?token=QylxJUy_QVr2MyzCvLqx5pGbNwScVuDjph9sgPWBMX32OJnBctdAXCkmHuPVrzXVMifR_hni4xlZcDYzS_CSpBMEDyRtjcfK-4oZfVsKGvMznTGTG3jujuQ-AktQsA5mwcTGLCALyH17dM6ozGaQnZbXFGEMjRJYGxSTIEBbgGuZdVpcY_-ErPspCh0TKhr0E36Z3uodmlFwbZF69aXS0BIU9DUaOmpNqGPDTL5QwwRDwKQck9va_80L21iVFAhmn9wrtYlmsomKMXl4XTNUqgWCebDAnF3sUofd9iLFKfCf74XPJSEfuYSL0Vj3_7kY8Ov65bepaBLe8hrIV6iZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فیلمی از کشتی M/T Marivex که امروز صبح گرفته شده، پس از آنکه توسط نیروهای آمریکایی به دلیل ادعای تلاش برای شکستن محاصره دریایی ایالات متحده علیه ایران، از کار افتاده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65482" target="_blank">📅 20:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65481">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbHbDmzk9-PJiB5_FOSVsX56B8nGiE1gLZ6u9LVyDk-Jb8wv00fzgDJ1y92nmLB48bPWoWi8c2y27GCT_jSu5FBKMl0nxeS39x-hC1qiUmfdjxhKp83BIBx_9oD_LR95iwILTTwxD8U7hBIBU3emnqnF1jCLYQyCnkSXQhHH4-z602GpEvd0AMS-FPI5APi0UovqgTTf-4anv8HFxaylzhhG7OwyBiklp4guVr7fL3ihvJe72gvHCw5mroiBJTTqUG216moz0YmaRwdW3pQPhSJn4UJaEv1KeiPSv2CC38yLg_kt0Nb3j0-HFchIm1COHPvHhZoZgpB6CuDXpFNb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده یک نفتکش بدون بار را در خلیج عمان، در 8 ژوئن، پس از اینکه کشتی با تلاش برای حرکت به سمت یک بندر ایرانی، تحریم‌های جاری علیه ایران را نقض کرد، از کار انداختند.
فرماندهی مرکزی ایالات متحده (CENTCOM) کشتی M/T Marivex با پرچو پالائو را زمانی که در حال عبور از آب‌های بین‌المللی در خلیج عمان به سمت ایران بود، از کار انداخت.
یک جنگنده F/A-18 سوپر هورنت از ناو هواپیمابر USS Abraham Lincoln (CVN 72) پس از اینکه خدمه از دستورات نیروهای ایالات متحده اطاعت نکردند، یک مهمات دقیق را به بخش‌های مهندسی و فرماندهی کشتی شلیک کرد.
ماری‌وکس دیگر به سمت ایران حرکت نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65481" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65480">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65480" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65479">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvhn1b49IvJhUJOOx4supcWg_jjsKJQRtTOY_ADiXmQoYS4AnkXnQJfWSWs9oavHhKpvzyl3ANFVMrGW8W_e-fOQy0YaadNmWnBYSSCPQP3s0m0BjekLHWE9mApC0KUkEJuPL-y_vnsao7_OcVeqO_e06ODg8y71_ZF0TrtEh3v_wxgFp6Hq2MpXQH-g7yI038jP61uZtEjaR8FhSeHHoU6cnSf1R1Oy5NAVT8_oy2ccEUYzkQdt57MJPE2mLP_SECl8iRmNYfvCj7dWezJ_0KHHMKxQcujVoJWAOVxlfgr7M4EHenmRMhFILkIgBGpfCilh0vmtAS2SKMs3w7odiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65479" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65477">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
رادیو ارتش اسرائیل: ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
«این حمله گسترده انجام نشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65477" target="_blank">📅 20:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65476">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
فیلد مارشال ، محسن رضایی:
ایران از غنی‌سازی کوتاه نمیاد و در موضوع آزاد کردن پول‌های بلوکه‌شده جدیه. اگه مذاکره نتیجه نده، محاصره دریایی رو تحمل نمیکنیم و اقدام نظامی انجام میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65476" target="_blank">📅 19:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65475">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
ارتش اسرائیل تعدادی از فرماندهان ارشد حماس را ترور کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65475" target="_blank">📅 19:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65474">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران فکر می‌کرد می‌تواند به خاک ما حمله کند و ما واکنش نشان ندهیم، این اتفاق نه رخ داده نه رخ خواهد داد، دست کم تا زمانی که من مسئول باشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65474" target="_blank">📅 19:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65473">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxtQ_JV5WhlZH8PfxiCSvRdvPBcxj_pfG8mt0l9UUQgaAHN0IlGWP-71ZG5NgiJ4meRh5DrR1sxGkUg8Xa0FrRY3un-NXuhhpQQijRqgtfjica90zyUP2ejBeSOBtZlaCDnJO_pGUZMWdi_3dsifsm3B76HExHRoDzfJA7n_VXnzN9dv6Qe0OLx0XRF2NxwIuhCHTcdmcgyW882kcZMt0ERWqPTCdw1ZolIL-ITbcZoJQW8GoQKam2BUKOna6dlQuswVsb2ewFQ23cKjoaEX3YgjZv6qsq9fXQfR93yyheXfVTNPtZQVY50CABEFGRXQt_AhGi923AL8pOvq5voeYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروی دفاعی اسرائیل (IDF) دستور تخلیه محله زقاق المفدی در صور در جنوب لبنان را صادر کرده و به ساکنان هشدار داده است که فوراً خانه‌های خود را ترک کرده و به شمال رودخانه زهرانی نقل مکان کنند، به دلیل حملات قریب‌الوقوع علیه حزب‌الله.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65473" target="_blank">📅 19:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65472">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
نتانیاهو:اگر رژیم جمهوری اسلامی اشتباه کند و حملات خود را علیه ما از سر بگیرد، ما به شدت پاسخ خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65472" target="_blank">📅 19:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65471">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
نتانیاهو در واکنش به اظهارات ترامپ: اسرائیل حق دفاع از خود را دارد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65471" target="_blank">📅 19:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65470">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
نتانیاهو:اسرائیل فعلا از حمله به ایران خودداری می‌کند ولی ماموریت ما با حزب الله هنوز تموم نشده
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65470" target="_blank">📅 19:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65469">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc930bac93.mp4?token=LtwPHKwCcEN8nRX62Ur4kKiPAOoszTdVG2OCJnLytPyheeeiV1FJfEJBZEm77exmDyEy5OMgq48DDEoZU5HFoQIy8h6qV_ieHzrc-u_fK3tyi2GCd-CekGYRXtXdxRu8U-E8K_dN2WymEbN_Mv8OjJhxa5Mpz5CM-auorESWVsQjpxz-8ggYGe0yTgVABmb3CDHN8i40gjR2Of7XGBYiQuar3vq8v8oYhKPHJOo2g9V9YA5InfXaxqWKCcSkAbaCdYve7dK7RgNtiKGtcadWSev85ndsGZAp0l2GCXV0i6iPPtgu8pYFJfxQWCNVK0IEJfcXv--QecrkodKWQAglow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc930bac93.mp4?token=LtwPHKwCcEN8nRX62Ur4kKiPAOoszTdVG2OCJnLytPyheeeiV1FJfEJBZEm77exmDyEy5OMgq48DDEoZU5HFoQIy8h6qV_ieHzrc-u_fK3tyi2GCd-CekGYRXtXdxRu8U-E8K_dN2WymEbN_Mv8OjJhxa5Mpz5CM-auorESWVsQjpxz-8ggYGe0yTgVABmb3CDHN8i40gjR2Of7XGBYiQuar3vq8v8oYhKPHJOo2g9V9YA5InfXaxqWKCcSkAbaCdYve7dK7RgNtiKGtcadWSev85ndsGZAp0l2GCXV0i6iPPtgu8pYFJfxQWCNVK0IEJfcXv--QecrkodKWQAglow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو: ایران و حزب‌الله از همیشه ضعیف‌ترند و ما از همیشه قوی‌تر.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65469" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65468">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران معادلات را بر ما تحمیل نمی‌کند؛ پس از شلیک حزب‌الله به اسرائیل، به بیروت حمله کردیم؛ پس از حمله ایران به اسرائیل، به مناطق مختلف ایران حمله کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65468" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65467">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
نتانیاهو:نظام ایران پس از پاسخ ما عقب‌نشینی کرد و اگر اشتباهش را تکرار کند با شدت پاسخ خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65467" target="_blank">📅 19:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65466">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو: تسویه حساب اسرائیل با حزب‌الله با قدرت ادامه پیدا خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65466" target="_blank">📅 18:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65465">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d663dc6e.mp4?token=l1kSLBTU6Isz2_Jtdyxzd6ztBEdYk07zJy2EflOyz_2WdZ6Wy3MLzz2p6C9OuHYpQL_WMApUk34cowELgTXUdFzUCMRM4EPvsrART6yhNip7HAuj05FKOwkdAojLikTgOuSotwyL81X1VJQZl8XfYUOl4EdvHD2vwThYXconTgbhEUWBn-7nIObAeti0zIUzKkpr4cNFv7Q8Mq5AEzmM3oDBDbufojhvMWKyV0If9TJdPKcPEpftUh48i2tQS17KJYYv1oBbSNR1RCGZicsad63g7gqGACIMkWDri1CN4HXxe2WeO0gWu-MIkH4DFoPagSANuGpcCiMJj0dUnVaC5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d663dc6e.mp4?token=l1kSLBTU6Isz2_Jtdyxzd6ztBEdYk07zJy2EflOyz_2WdZ6Wy3MLzz2p6C9OuHYpQL_WMApUk34cowELgTXUdFzUCMRM4EPvsrART6yhNip7HAuj05FKOwkdAojLikTgOuSotwyL81X1VJQZl8XfYUOl4EdvHD2vwThYXconTgbhEUWBn-7nIObAeti0zIUzKkpr4cNFv7Q8Mq5AEzmM3oDBDbufojhvMWKyV0If9TJdPKcPEpftUh48i2tQS17KJYYv1oBbSNR1RCGZicsad63g7gqGACIMkWDri1CN4HXxe2WeO0gWu-MIkH4DFoPagSANuGpcCiMJj0dUnVaC5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
سوخت رسان های آمریکا در فرودگاه بن گوریون اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65465" target="_blank">📅 18:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65464">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
بنیامین نتانیاهو تا دقایقی دیگر سخنرانی بسیار مهمی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65464" target="_blank">📅 18:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65463">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
وزیر دفاع اسرائیل، ایسرائیل کاتز:
وضعیت در ضاحیه بیروت همانند شهرک‌های شمالی است. هر حمله‌ای به شهرک‌های شمالی منجر به حمله‌ای در ضاحیه خواهد شد. ارتش اسرائیل به عملیات خود در لبنان علیه سازمان تروریستی حزب‌الله ادامه خواهد داد. ما تهدیدات ایران را به‌طور کامل رد می‌کنیم. هر تلاش ایرانی برای پیوند دادن لبنان و ایران و حمله به اسرائیل با نیروی عظیمی مواجه خواهد شد، همان‌طور که دیروز اتفاق افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65463" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65462">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3210944dde.mp4?token=lYKgpRqpZpymwKaXQaDOxa_GlGKWG_fORuHCUNPpJRV4bA0YjW2eesVefyVgWc6ElUC3MmcVSqEPNSsoUjo8SYmQjZqQOML0-GgC0WLwsPPW46CRkq7UNqs4FoHcdGQnOfjpABpqbvmf-VuTCwY5Q4UDnSXRG-f6l6PAUI_Kl56Li27_d-j2ACu81kfQa5iBK-6AAIoLg1Ee6xkY5jmPpQ9Qtc4gw1fluAVb-bI-S7UPjzJQQB20th9aYm-2zG6yHRDjJ6e6XqQo_StboRoOsJqGif1EdyzjrRwgSwXfCkdhWTnYBj6M5BQCT_ajXR9EfFhDteQQc7hck0hzyiooaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3210944dde.mp4?token=lYKgpRqpZpymwKaXQaDOxa_GlGKWG_fORuHCUNPpJRV4bA0YjW2eesVefyVgWc6ElUC3MmcVSqEPNSsoUjo8SYmQjZqQOML0-GgC0WLwsPPW46CRkq7UNqs4FoHcdGQnOfjpABpqbvmf-VuTCwY5Q4UDnSXRG-f6l6PAUI_Kl56Li27_d-j2ACu81kfQa5iBK-6AAIoLg1Ee6xkY5jmPpQ9Qtc4gw1fluAVb-bI-S7UPjzJQQB20th9aYm-2zG6yHRDjJ6e6XqQo_StboRoOsJqGif1EdyzjrRwgSwXfCkdhWTnYBj6M5BQCT_ajXR9EfFhDteQQc7hck0hzyiooaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای از اصابت پهباد به مواضع گروه های کرد در شمال عراق
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65462" target="_blank">📅 17:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65461">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
اسرائیل هیوم از منابع: هنوز هیچ محدودیتی برای فعالیت ارتش اسرائیل در حومه جنوبی بیروت وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65461" target="_blank">📅 17:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65460">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc72e760f.mp4?token=vwHH-3P3soMhO3jgXzUc3qrUeNubU-QFNhqXE0dWg9uMwV3FVfdbkXxIL6LCSRK1m1JIj-U39SSd4NAIqH-p0CGDCuejwqk4ihqlRjiIWBbBKAY5AhQd36iq2NOo5De18FryhwVsbGRsQ4ottTYAKF1iem3RdZPrNqYfAWKoy4qrHfESgydZynGpLo22u0N8yjDV-vl1BqBBPSedhIPl3jysaZ9tPA02KNL0dgHOxkpyordmA94znVqLKItUt44ta0GaAwBOhmBp2AWG53jMSlif-RaEVhF2A15R_cAWWcd7v6_PyLYs0Lp0KdsOKsq2nmGx6Z89_FvCorqEJTdTxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc72e760f.mp4?token=vwHH-3P3soMhO3jgXzUc3qrUeNubU-QFNhqXE0dWg9uMwV3FVfdbkXxIL6LCSRK1m1JIj-U39SSd4NAIqH-p0CGDCuejwqk4ihqlRjiIWBbBKAY5AhQd36iq2NOo5De18FryhwVsbGRsQ4ottTYAKF1iem3RdZPrNqYfAWKoy4qrHfESgydZynGpLo22u0N8yjDV-vl1BqBBPSedhIPl3jysaZ9tPA02KNL0dgHOxkpyordmA94znVqLKItUt44ta0GaAwBOhmBp2AWG53jMSlif-RaEVhF2A15R_cAWWcd7v6_PyLYs0Lp0KdsOKsq2nmGx6Z89_FvCorqEJTdTxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیویی کوتاه از حملات امروز اسرائیل به اهدافی مشخص شده در ایران
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65460" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65459">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLAzbdkhlDhk8wUec5f4CWddry83lEr9smq2tSEKboC-p7Bda2jlvgkoK7FrJQES_IfBZR5rAu2R6JM_jepyVlQO-Tbs7kpAKNQIOuFWNerWTk9l_LKt7_rtGXKrJWs0F4mKHlQzVPbe2WzPAVjuUuVcjSMPCVX6mvQB0seuMLsePUpifJ2jvOUxXV_luj5CLxb03l3WcFvS42G9dwS3zjlmfjPheqmPcZoIqiFs_744EmLoGdvG5mFwiD16rh_0MKtXTKNeK-ZgqC0DwTMTMnrfBD_qHTrNVWl0Zfv-U-ztOFDZrL3FRyjUyRp7yJtax1h6Y_59wtWQvAXMQ_1gZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری دیگر از جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65459" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65458">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYUb7e4IQeKxNsPBcS0D0S3YvsGyFCWbPuaEP99iBUxyrdpCqlArQoLtJvnbfu3ESSlPshAobcbnT-AHB4VmP3vh3i10RynmBhf6Lw238iA3qykJFu7CPO1g_dA9i2B963VqRhnalN64B6UzbtppFsoFKMRDGzjiC3dX6xMac6SFWm2hzGleLJ0kZlTO8QsrFZ2qqXs-KIKck_cGSXKDEnaP92ICeo7_MLkhXOfBNOTAMVP-0TyamFrikSyRx6kKH1dfm3qEEMSF5eqEl9oYVgeXlj8FlDSaylnSAHUTEmh9-nzcbGYvIWchiAF1AV7ISkFy3XR5MVQajwl6fx4Xeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ها حاکی از حملات مجدد اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65458" target="_blank">📅 15:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65457">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gj5oomUIWLF8tPy5P8fcxnDDENO1FOsBZKjlh7IZxcCUYphPR_e9zrY7cjS2QNQBs57qlrGm4PhfcnE_TAKhM2mnZbeujLAnNoKu7Xtb0rBOY4nHdbaQOw2ECoPKkN6QCer5vtOgYCkoIPn0SVmzbpcZC76HSwPgq75LgDeTKSEJla3gyYdh2He5RpNecEH2bgTGD48E7WQX_pW5QDPCDFVRVG_SDimnBNZBXB3AGR0_I913fbrfGV3HIArlLMT3vQqtSom83i__vFlQ8-c18ornx4tEMzJGD6ylzOpnRJxa8O91NBukhBn6y9s2tsQgohkXYmamdBusNLrJKsReOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما پایان درگیری‌های دیشب و صبح امروز رو رسما اعلام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65457" target="_blank">📅 15:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65456">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇮🇷
فرماندهی قرارگاه خاتم الانبیا:توقف عملیات نیروهای مسلح را اعلام می کند. با تاکید بر اینکه در صورت ادامه حملات و اقدامات تجاوزکارانه از جمله در جنوب لبنان، اقدامات قوی‌تر، خشن‌تر و قاطع‌تر از گذشته در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65456" target="_blank">📅 15:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65452">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ff72sYavh9BxCvQ8jxHpZXFxT4qswVuq444ArO4wUH1bhERqZZxuT-BExCxg88QVUX1qS4emv6baVQ3xc-_ACpT6DsLJ10lEBsRh4xqXF-tOtcgc-lm_UeME3jzbsuQhQ_6qrMtxae9j88WYBujhUDfVIakd3lVkga7-BWgD1-Q-Ok5vXogF62L73pilVhBOEXAkiS2bCYZLxqmjg7VIZrb3_MgPV78VLaC2ghKaLfsl1c6_3H2SsQcCNbzlaExc9xjRi3pEeZdOUw10InHNQI69nxQTNtQH8YrBYhfhQCb-mRRxqr3KhbAYCj80RrLRldO_lRcLgCsYFRjWoeVpqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQk2D2vRCUnszLQ2UisbysNl1q6UwM_FiSTiDUPeMWJyvs9O5ihsuT_o6wzPwV9xqNWu5Lc21A-YkeaJfXwZ1_mgyzeagnHta63zVKCu89UJKxnxGKdQf93qZM0ndrIePfY78DoaK_ul2Kg36tbeeJllzzvJvuN1XC62NdBZEd9CrmjPNn976s0r1YzK32wj9edKj6H-H01EX6-LIHOcZZfnjfY2Vcm1S8OwRPnuNGmTJJb4b4K9_GvwGb2QaWVzmml9QnUr0EQ7ocq6EdIJF63Vo55ugFhWYq3uW2C8Dv9roHO-8AHCuXy2Ufc0Nl232jyoCJ5M5bXT-SyJE11C9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rm0PXZ_0ilqoB_WVfR43KEH9fx5D21Bv9y64YTnp3eaazHbidMProDbdo0qEJfYf8xep2Hh-DPbJFc6JChP34U1n_7PQLQWZdAqLzVgEReSlZBOH9KtcL9JHkD0o6fHNxDBLO0OHEusNfVuphi2k9YySTpmB3nX55wnt5BgZnxuYNzRe8LuT7l2nlSsas7MRUarCn4p0F2gNIEnADlmmN8WNtdNEMBa9Gnac_wWeicN7HI6jv4_--kDw5K6cYHr4IQT2EmWLHLY4eIB36zIgdq_pHpQ2p-ZpaWyQuDZ9o0tfq4wrtIY4YkqdQqUCAnWAU-uH9dYqAaPumgJ6SHBhEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t2PN6KS2P3-9WBHRVWu6wXz9D6c-plVoIX_2kygSxZrxh8d19Pvh9x68IbBOPhJxdqciPKsamUvGXNjwC3kLnK3ztMTGe8gOsFSALRVKza70yBwxyI0d6WEQ87KW-3IJ1sYLYqtgONcZMvIs-HI8k72BXfPITUFHaR8tbkkvi-xAjqQNVAk8_1b6NplPNiTTgep27AoqDcclZXTZLr_7PLgoN3sNb4C4FiWk1SqVVnTuh8IDZt9ocRXZ1zWEjsQOrZiM6e4ofova_egKIEV0kf94lfWxm_0vH0lR70XHsu3zZSD2wvzkKideKJOYFhX5Z3EImNFfF6iLQGgPSs6u9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکاس
اسرائیلی
؛ رفته کنار یه پوستر موشک ایرانی که تو اریحا فرو رفته، وایساده و عکس گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65452" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65451">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگاعشون
⚡
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65451" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65450">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX3rGWbrkn58oi83Vo4wmzKWp4W4TKmR-7c8hPhOTqkJXZnXcH3ea06pENsNYjLGTBd_xWLwZxELrFCyg7Pk7IxZXhEtQpiWAaO8xCyWk4INBCFKf5FaQItsUkYWDIYZBXLLZX9hBEKUSXWQx7fs3rh_FFsKsrwm-GfIkuaFEBhVUE7MLw-uDdKpaApumseM66-0PyEYei4Ssxb4jZmLwwRKxLvsyBss75iYTgpxYi2Jfyr3Y5u2yfd77YVefPqZRVHX42LJjdwtE8nWiE8RvXSDGrtrPV2usqu_FMpQ8Rc4DhOULrNKU7AhojfJAoyWW9ubi47lo5W2q8EDCbysrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبانی
🆘
کامل در لینک زیر باز شده است، برای دریافت آن کلیک کنید و عضو شوید
👇
👇
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک را لغو می کنم
❌
❌
❌
سریع بپیوندید
🖱
سریع بپیوندید
🎧
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65450" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65449">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sy8p-0UBZw52ZnMRmT2pgAJmh0ZtZyLDWX-f0fxx_X9idOXehsCmwHP1UUKJWp_CbwWUzMCuxV6rFhHlAslYXdbokRYs94AiX6cwFw8ZbMMMBP32Ez2k-Jd_CkqVVJbReILehrQIIB_GOgUSz89jDQFLZE1BzPwsH4-x6ZAfQoIFS08SMujoUbZo69IfuHYwD3L0kKg35CYziOSSPcGKyDVrRQTh380OOJfSlakFnIxLedqSG4OHM1igT9yz7opbaQONU0o_EffuYeM7xZZvP9bBfLkNRuXLC3ojraAuuBtwi8Y2pkgN-CSTrAZbXV5b7Bg8BjJ0pvaHVERwqxQV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
محاصره با قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65449" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65448">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65448" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65447">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddgZJnpZpY_Jpe2HyEazxAKn1gGu9K5jqO5N-sLrXXSJWAAgJqh3TQ5FwTL4kuKjMGEDo4StS8sHZzPJrxBvkvT-wKKq1d6LPpxYQB4-E8yQclaU9VE2JMf51fjGAswlL---8f2qkM8WvI26trIC69bfAzVBTkFI3ap_SReixxsIJNg5REuCQSyGMNo5vl9MBwSDnCta853w-mQ6h3xCHOFKcVaGuCDN4Q_x5dA-g6sNcoUIcYs70jHjEozbmX-CUj_Yvpn5VNuQxJ7qn8aQd-Vy0VCAFI6zSjuB8EDhSHV2of9a__ao8LKTQMRKzVMPM45UUMQjCWmLheMj3Lma_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
دیلی میل| یک فوتبالیست بین‌المللی متهم شده که در یک هتل پنج‌ستاره در ترکیه تلاش کرده یک دختر ۱۴ ساله بریتانیایی را برای «بغل کردن» به پشت یک پرچین ببرد. پدر این دختر در گفت‌وگو با دیلی‌میل گفت که دخترش پس از این اتفاق دچار وحشت شده و در حالی که اشک می‌ریخته با خانواده تماس گرفته است. این حادثه زمانی رخ داد که او همراه خواهر ۱۰ ساله‌اش کنار استخر بود و والدینش حضور نداشتند. دختر ۱۴ ساله که از دیدن یک چهره مشهور هیجان‌زده شده بود، از بازیکن درخواست عکس کرد. پس از گرفتن عکس، بازیکن تلفن او را گرفت، اطلاعات اینستاگرام خود را وارد کرد و از طریق حساب دختر برای خودش پیام فرستاد تا ارتباط برقرار شود. به گفته دختر، پس از آنکه او سن خود را اعلام کرد، فوتبالیست او را هات خطاب کرد و درخواست بغل کردن داد. وقتی دختر مخالفت کرد، بازیکن اصرار کرد و از او خواست به پشت یک پرچین برود؛ جایی که به گفته او هیچ‌کس نمی‌توانست آن‌ها را ببیند. دختر که ترسیده بود، به او گفت پدرش در راه است. به گفته خانواده، بازیکن پس از شنیدن این موضوع به سمت دیگر استخر رفت و خود را پنهان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65447" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65446">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
اخبار جنگو تو چنل دوممون پوشش میدیم عضو باشید
😉
✌🏼
@Futball
@Futball
@Futball
@Futball</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65446" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65445">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DC5VKo0Fy7c-32giEOHFoSxP3KYH7wvWbSe69kOMMfRzYtImpfl2kHjMpt4Sdlcp7r3kaI1NewBdroSiI1Q8LUGha633UO3m6wdDLxVy2w74uIhxG7kfSjfr_zheMjb4Pz3h0Ljb4YGw3hawEKd-n1s75kJXrLU2S4y8Z5Hj1dWsHsZ3ydmpphIzin6R_H8xnypBn1lGrguTq_JpXB3DKBmB6V4CrE8uYTFRX15GhhGxqAV1qmmopQYRPP7hEAQe1-Hocu16n0PZ77TZtGULcp-TK_BJagdBDVANaUUE87LY5NNov5H1dWuMVLwHUKlsOCNohDahvzbgh5T8UbEjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65445" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65444">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
مارکو روبیو:فقط کشورهای احمق وقتی به آنها شلیک می‌شود پاسخ نمی‌دهند
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65444" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65443">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇮🇱
منابع اسرائیلی: حملات دیشب و امروز کاملا با اختیار و بدون دخالت نظر آمریکا بوده اما سنتکام در رهگیری موشک‌های ایرانی کمک داده
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65443" target="_blank">📅 12:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65442">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c5e38e196.mp4?token=Y0ClQMkeycNDu-cB7EfCwr1T7AfjrKvgYHwtE6EBMQnqcUBO7qJT3g_TeFdpnvFanuGvXMQK8LdGIxW6EQPhpcSTl2VUD-zqCY_fedYi6YxBEQBLAVZzTlb7Upn6g42HwwkEya1bYBuYqmAvZxM4khnmzNAxOi0wCzcksrcQBH8AAZJtxCUpNzK9uaVwYCzuz60BcLIRMkG80tGCtjwKgtjgKl13XU42ThaHUNDusr76uYfsSNpwG_dy2HOTJ6p43cKdpyd7Y5dxr0Kp5_IT34denM-7vfUHOY-ubz1JoiEEv73F4rPNc_--NkRghQ-c6rjvzyWm8Wet4gw7_Dl9dA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c5e38e196.mp4?token=Y0ClQMkeycNDu-cB7EfCwr1T7AfjrKvgYHwtE6EBMQnqcUBO7qJT3g_TeFdpnvFanuGvXMQK8LdGIxW6EQPhpcSTl2VUD-zqCY_fedYi6YxBEQBLAVZzTlb7Upn6g42HwwkEya1bYBuYqmAvZxM4khnmzNAxOi0wCzcksrcQBH8AAZJtxCUpNzK9uaVwYCzuz60BcLIRMkG80tGCtjwKgtjgKl13XU42ThaHUNDusr76uYfsSNpwG_dy2HOTJ6p43cKdpyd7Y5dxr0Kp5_IT34denM-7vfUHOY-ubz1JoiEEv73F4rPNc_--NkRghQ-c6rjvzyWm8Wet4gw7_Dl9dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
‼️
‼️
بدون شرح:
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65442" target="_blank">📅 12:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65441">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=rHoGH6F9KI7mPsjkWaMvjbX10xQBNOGY0nQ6QkfjtqCfValhLVqry_dCGaZpix9sml5byiFKxc0K4jeDO02OgSqUa51Frc_FH0nDsD_VtS-be6vPS-QOuw8dEcHDf4RDXTqTXrNPYtagHxO61qefE-s1GKuzJQhJbqJv6947JgRMGLSVJfJovzkSMdMpjYJ4NwxFdurzUd77G0XITJG8k8Bz3mpvIy2GtBSdUcbI4EIgJ5KlpaXtz2fV3eqU1bJ-gyPvw4KT0stZIKt0UHXn1snXwRhziXsp85DZqiYK9s7riVpNFzNje0aitFCSczmUO5Z656FaoKDxlJngXjbDwy891qV8anBHM35qbmcBFBHNReeTQawF-NhWqBaLSl51grBETLH4dfRjE67zmdLY5E0x4mynFr1rzvv3hUTYBdIcSAFUr-vi0JdxGYoR4Q2a6-Y1tPbzBH7dquVfJZuUUAXFikuhFtFI3xR8Bj9C8w-2CnL0qZpED3WiQS68U8t9XlqXGjtRs3UUu2Kjqr4fumxmRfoDCN6oJAQYMfCx7XpO-HzDy0WSH6Z_wPThi5x5w_aju2txtur56e8kqRc8NP-u_-0lqgCb15FwsogYtMleBv_OlHM98dtiaDf9xz5cn7LvyHkfDcJI_2br8Q83DIqtbtFRImZvDGilz0Yzh1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=rHoGH6F9KI7mPsjkWaMvjbX10xQBNOGY0nQ6QkfjtqCfValhLVqry_dCGaZpix9sml5byiFKxc0K4jeDO02OgSqUa51Frc_FH0nDsD_VtS-be6vPS-QOuw8dEcHDf4RDXTqTXrNPYtagHxO61qefE-s1GKuzJQhJbqJv6947JgRMGLSVJfJovzkSMdMpjYJ4NwxFdurzUd77G0XITJG8k8Bz3mpvIy2GtBSdUcbI4EIgJ5KlpaXtz2fV3eqU1bJ-gyPvw4KT0stZIKt0UHXn1snXwRhziXsp85DZqiYK9s7riVpNFzNje0aitFCSczmUO5Z656FaoKDxlJngXjbDwy891qV8anBHM35qbmcBFBHNReeTQawF-NhWqBaLSl51grBETLH4dfRjE67zmdLY5E0x4mynFr1rzvv3hUTYBdIcSAFUr-vi0JdxGYoR4Q2a6-Y1tPbzBH7dquVfJZuUUAXFikuhFtFI3xR8Bj9C8w-2CnL0qZpED3WiQS68U8t9XlqXGjtRs3UUu2Kjqr4fumxmRfoDCN6oJAQYMfCx7XpO-HzDy0WSH6Z_wPThi5x5w_aju2txtur56e8kqRc8NP-u_-0lqgCb15FwsogYtMleBv_OlHM98dtiaDf9xz5cn7LvyHkfDcJI_2br8Q83DIqtbtFRImZvDGilz0Yzh1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
حمله شدید پزشکیان به رسانه دیکتاتوری جبلی
: صداوسیما هر روز شعار می‌دهد اما باید واقعیت را هم بگوید
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65441" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65440">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65440" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65440" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65439">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJElyiqOQvNmCTkV0ICWzpF_bbbipmW5ZW60OPvdD233fMnP12fHOjz_lQRmbb-06rfME5vrt3US7sPIKM4pFZrnLCDzRvRjtyDz1gYb3x4tpbdTZPQKmV9yk_D_5GwBSh74eKir0ojasNrEEKPA700bcjOy5ZJbwFExh3O2xNwanfaO0lXQvO86XyBB-YwWI6G2ELp2Bv4Wcd7ovgwwL-98_bHvusNVj3jkC0vQ-45dKEAG4BNcdPf9Io8ZgOPw67XgBB4OvnTb7LBcqgRB45fhIbs8F4ZXsOHW1E5d8Mzxj7N27enLlllWy2KIMsXgB_7iG3DXPqzPuxEn9euYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65439" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65438">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری‌فارس: سپاه دیشب در حملات خودش از آخرین نسل موشک‌های خیبرشکن استفاده کرده و تونسته تلفات خیلی خوبی از دشمن بگیره!
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65438" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65437">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8792984a2f.mov?token=tl7T0cq1VHB3nb81XKFClP0-jR4be1hoSCrftPuX-rBHOzDiTq0dhphA3ivFuqsz2jWLGOCgnDVAvpXqaBy9m5K8E9HtuCHzU2qKdiP-5iq4oxSu-bPljPCQT5fhF5AkDgqOITG7V6BULWKFEHMMOPE88zc_m49LmB3gzi95lmvbO2iR7ZO5gXPWzGjcYkf4ApJk4FvFUJbW01ajHNdssiyb7O9rJmTUyX7EIfKReH0fo0qzfl-_v7b5-Cpl4dxZbze9r13B0gW5bKTh33aPI_gxYsPIOYvH5d3OLxN9N-FXj2nusHrk4CHviFHOv8x6Hgo4DBGc35cDZeZ8hnyIuoyzv6RCzktgK6SXFe7pfLU3q17C5cberGheCvkznOnSx8Hua6Q6xattkw1zJa08-Hib4wi-IWGWWD9qEBrpXETmMgdBNjq1yGxVfUz65_ObWkJ2bveGP7I2iZ4F4MnzUlAg0a_JdzNSXx9CSMd5YpuDkrM_5jAqlHlFbwkgpcFHoaULBNufLVYOCMaDczQqzfPe1qDiGkEvBNV9yJRPXJPQumiJiKJ_uA1Q5dNyBJIESeUzalPqxK9uuTYkljAaSlYuZvJO-4uyVeE4NIrAJOQo2gLk56UJcFsQmmr5P6rLO-rFE7F08LWZ3YuJrIirNjoS9CNUXBP_ZH7QD8IhTMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8792984a2f.mov?token=tl7T0cq1VHB3nb81XKFClP0-jR4be1hoSCrftPuX-rBHOzDiTq0dhphA3ivFuqsz2jWLGOCgnDVAvpXqaBy9m5K8E9HtuCHzU2qKdiP-5iq4oxSu-bPljPCQT5fhF5AkDgqOITG7V6BULWKFEHMMOPE88zc_m49LmB3gzi95lmvbO2iR7ZO5gXPWzGjcYkf4ApJk4FvFUJbW01ajHNdssiyb7O9rJmTUyX7EIfKReH0fo0qzfl-_v7b5-Cpl4dxZbze9r13B0gW5bKTh33aPI_gxYsPIOYvH5d3OLxN9N-FXj2nusHrk4CHviFHOv8x6Hgo4DBGc35cDZeZ8hnyIuoyzv6RCzktgK6SXFe7pfLU3q17C5cberGheCvkznOnSx8Hua6Q6xattkw1zJa08-Hib4wi-IWGWWD9qEBrpXETmMgdBNjq1yGxVfUz65_ObWkJ2bveGP7I2iZ4F4MnzUlAg0a_JdzNSXx9CSMd5YpuDkrM_5jAqlHlFbwkgpcFHoaULBNufLVYOCMaDczQqzfPe1qDiGkEvBNV9yJRPXJPQumiJiKJ_uA1Q5dNyBJIESeUzalPqxK9uuTYkljAaSlYuZvJO-4uyVeE4NIrAJOQo2gLk56UJcFsQmmr5P6rLO-rFE7F08LWZ3YuJrIirNjoS9CNUXBP_ZH7QD8IhTMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فیلم دوربین مداربسته از لحظه حمله‌ور شدن الهه و شهربانو منصوریان به حوزه ریاست فدراسیون ووشو و شکستن دوربین مداربسته و درب اتاق رئیس برای ورود به اتاق ریاست
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65437" target="_blank">📅 12:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65436">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b744fd7fb3.mp4?token=kdwe4J3q86L6BaWPdODc22uv-98Kv6zStIfn5IZune6ReTOY_yLVhEZAFfqL9OotTDfFrqEs3oY6k2BloCO8nW5lrncixVt_ORyOFFALY5W1cgM2e8-4zxj-UyStR_y5JxjWzZO90DIqlK8rS0w1rsJdNpUd0GCNUCXj7ELZ424ieLh9ircYDzDt7jrpkksD5CE_9xkKSEVD2p--Ny9k6DPKpp1U3Rao1K-aEiVYQC1ykjqiAi9ddTORbOZGGpl1uOBbszciK-T9hSkM59351Eqsw6oHrvQTnTh9xxsmVdHo74HaW2VC5CJMx_5o-QACiL20ti0ksFos_Pvf0zr9uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b744fd7fb3.mp4?token=kdwe4J3q86L6BaWPdODc22uv-98Kv6zStIfn5IZune6ReTOY_yLVhEZAFfqL9OotTDfFrqEs3oY6k2BloCO8nW5lrncixVt_ORyOFFALY5W1cgM2e8-4zxj-UyStR_y5JxjWzZO90DIqlK8rS0w1rsJdNpUd0GCNUCXj7ELZ424ieLh9ircYDzDt7jrpkksD5CE_9xkKSEVD2p--Ny9k6DPKpp1U3Rao1K-aEiVYQC1ykjqiAi9ddTORbOZGGpl1uOBbszciK-T9hSkM59351Eqsw6oHrvQTnTh9xxsmVdHo74HaW2VC5CJMx_5o-QACiL20ti0ksFos_Pvf0zr9uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتشر شده منتسب به آسمان یزد
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65436" target="_blank">📅 12:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65435">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFUnYp89GlWo4arHUCaoQh8bYOXtRIGu9mDfipRpC0C6ccR-xKpf95haqCYO6lys55VmHKzsMto0cg2S1JwNrHznSNz-RG5J5Cj31O2Y1b_U1zoQiHb7LHWcQ3013MCrCitofUsUSLkxsgX6tpD6OgCGJLG1CaPVdoKikpZKRnCsgmsWK_Gpe8NTCmHpD_N3S8Z5N8WFw_o6Vou6LHluqJqGOYJ1ZMwqGvsDLdulOmkoJt3KGdlOfIb18hfFw9ALvj0XvvFOEN_SX7eixgrPZfj1piIYNHNN0YC8OwXN0ACKIz5MhW_CWHx5oGgd6SVOKuJeVoviuMbY32LG4ANuxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مشاهده ستون‌های دود از شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65435" target="_blank">📅 12:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65434">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
گزارش رسانه های اسرائیلی از هدف قرار گرفتن فرودگاه شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/65434" target="_blank">📅 12:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65433">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ اسرائیل: حمله به‌ نقاط مختلف ایران را آغاز کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/news_hut/65433" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65432">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
صدای انفجار در اصفهان و همدان
@News_Hut</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/news_hut/65432" target="_blank">📅 11:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65431">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
گزارش ها از حمله به دانشگاه هوا فضای عاشورا
@News_Hut</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/news_hut/65431" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65430">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
غرب تهران و کرج گزارش انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/news_hut/65430" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65429">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
صدای انفجار های شدید در تهران
@News_Hut</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/news_hut/65429" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
