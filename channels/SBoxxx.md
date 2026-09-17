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
<img src="https://cdn4.telesco.pe/file/du6gIwcWbp3FYkPm2DLHZUxHKEEH7LOJfG1PgsUtVC7_DxQ4qDZkbe4HCJqzIoOdG8jcEGI_eBxhO-FkYAXpUl15YxAEZr6rErw5K7Xu_FXn6Q849ao9rrjdvr7XQPIYX1dpucucioUAMv7rpKTiYjZxcMgDU2qE8WKgXObvRPB0MbpBH-GzeVLHG5VjjrSRy5jzN6Vu3GESAlMHnU8SCRVtw1b1hsHn_LugKQLe8ZgjU51S1Cd0WjdJwZpB_u-7QQyAesS83P5GyFvWyMnlWmGsHOB8m0bqbp_5cGbYcu6G5hX0rhmjJsKwcuVlQRVBbwQLXpyKGpNBsLJW_lcpJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.8K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 18:02:50</div>
<hr>

<div class="tg-post" id="msg-20952">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">#FairValueCurve  شاخص FVC اکنون سقف بالاتری برای طلا پیش بینی می کند و لذا فضای رشد فراهم است.  در نتیجه انتظار برای یک اصلاح تا 4300 الی 4290 و سپس اقدام برای خرید برای امروز منطقی است.</div>
<div class="tg-footer">👁️ 290 · <a href="https://t.me/SBoxxx/20952" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20951">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نخست‌وزیر اسرائیل، نتانیاهو، می‌گوید که اسرائیل رژیم ایران را سرنگون خواهد کرد.
«این رژیم سقوط خواهد کرد.»</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/20951" target="_blank">📅 16:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20950">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/20950" target="_blank">📅 14:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20949">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk8De3DTT8CqIKw3zWX_hSpCBGjn5ow93Gzrq1x8rSsGwJ_ohEKSma1NP1KWg5GW8bJIZtZE1JzxzSo5NO85g_0vqmPcBzz0-rQRkqfFGlKSzrHMNfa60GpHRiXA6alkgLZEj9RtgcpmkEP1xi5ySd6reJLp0SJBlvSYvECoV2J84KnU_kFeetU2hPoRPtJkBwiGrY-_svLc8rFJitqepORWD8vH7oKOe9thGZ7a41sAmrLteuzbyJmhJm1Xk4bcVs_wVvOxaz62kGeUu_WDYhe3T84fs2rBNul_glLwtfIKVfw5XsR8-BefFIkokWjBDP3_y6YVthWrBHftnaD1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
شاخص FVC اکنون سقف بالاتری برای طلا پیش بینی می کند و لذا فضای رشد فراهم است.
در نتیجه انتظار برای یک اصلاح تا 4300 الی 4290 و سپس اقدام برای خرید برای امروز منطقی است.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/20949" target="_blank">📅 11:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20948">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6heC1XzxYLQd8wt0-DC8_ZdZCE9nuO0uq_HdGF2aLRbg2BpovSJrNo78gFtxi7EyA8W6uwFnPGj9oW6gd7hRHCxR0-TUYadHMuu7Paz9krLzywYHv1CM6gJer3Hc269_0Z0HMdS6R2b9WSLyZAx1TpTtdPVu572WiHWb2tuj1-e5kUH_T3UkRQkHECrif4Eqt11bAXDPYNjCBWWxsCce71kCMUx5XWOv1qxGBnlpkLQTGX68R2_WDfmA3PYYzKW4TN9UCmd9Z5wMU0tVvhLlD2yaYrr7zwtaxki-hAxPfiVWbZgDsCohx7KdpfnTWztBk5Hs91jz-4w21rZybj3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و انتظار می رود یک اصلاح نزولی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/20948" target="_blank">📅 11:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20947">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/20947" target="_blank">📅 11:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20946">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMaBdz-BRH8OLUnQB1WVu3ePcFmCYRh0ErlqSo7I9wXGo8wI9p1yFaM5Psxuxtb9cjr_gUJUzPbFr_Q7mSQ9g7lByHptOLVrCNvGq-tbn9OnWTihWAP1uSVJEWWHXKErFDxJ4biubVvsHPXRMe3IgUYTs7mINQgC16kNY3FWYV7CIo2qPQxmoO2eLLnoxYwt12F6aFYJTtqrVNKBUcnCUxS9i0k-jW8aEamEEJm_PemDOEqZnUjLYbnYHy4HbtWdWjw7kFHcm1ANr0NDchni-Aaqw4ZHCtvxBCtnEObHMvRsSjYgS8CWyZtqCoM8H2yt-WvImLGsnWUuzKG6U5I3Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین توییت برگ افکن دکتر قالیباف</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20946" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20945">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شروع شد:  اخبار فوری: کاخ سفید افزایش نرخ بهره فدرال را «مایه تاسف» خواند</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20945" target="_blank">📅 00:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20944">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20944" target="_blank">📅 23:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20943">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCrXN-2ZUznAAlWZKI9kJD9dgzjmR-X3dqUWR4NXDNmhB2Sk0jciOl9FmiZasPDYqTUBkmcDql2_bazC7py7myXQkASor9sxee-87-GQ2M3SfjUzFLusNCM5CM2gIiQIiur90H13Zd3q37UTqr8oHMzu9yDqRgDHz8d5XGkzsquRmjGIaTlmSptnXSMelxsC3MEvy-9kDbot39wMj7bb8xoJcbwNuPv3MDwwzzzBc5lrBEh-cJwwl0TT8sIXw1-WBPalIALKlbPCA13Z3LkGr9MnghcJtxLH2cQYLe0LREgFm83pOqPov1jPDGFIh0IICKniDHuOdTv59Rj04qmYyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پوزیشن دیشب برای همراهان ما ارسال شده بود.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20943" target="_blank">📅 23:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20941">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20941" target="_blank">📅 23:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20940">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqAjCtZMmwIlkOYaCs5cFlsARRaXiMZ8hVB2mWLGuIdNRLbiitBxQ6WzsaVy0TZgK6Oz1mFR-Sn16HOdsgT6990kDFr9UlsFKoX_w7VBbVvvZ1amzqWwcojOOgJMw1ZP80mB3BiSNR4jXHSrcwmFjVOGjc6MSbR7mAUiatK6xOvLYOjEjtSSmMoWgkaTyp_8gTgP7tEK8hqsnnZTAFeL7wMbPU1Q2FULS0W3iwCUq6OYL0MhVf4mA0EH_KolcURDEgCxcXpaLW6pbVeiwi6ssz2AvVhZEEJe8GqmVWGELs3CTNAJH7dy4wxga0IrVONyqBXQBt1wzkgerwKKyPUh7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20940" target="_blank">📅 23:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20939">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20939" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20938">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20938" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20937">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شبکه کان عبری:
مقامات عربستانی به نتانیاهو اعلام کرده‌اند که اگر اسرائیل جلوی پیروزی یمنی‌ها را بگیرد عربستان سریعا با اسرائیل روابط خود را به طور رسمی عادی‌سازی خواهد کرد/کویت نیز بعد از حملات ایران همین قصد را دارد/اردوغان نیز با محکوم کردن یمن پروازهای ایران به ترکیه را لغو کرده است</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20937" target="_blank">📅 22:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20936">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20936" target="_blank">📅 22:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20935">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20935" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20934">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFIQtACTg4hryQDAU8OP0VXT0LXNJLmmjKA4rpdYCXpPQ2TSqJJvBz2yFAULL-1LYoW-DNBnz41uMd6OA3SQB8W6Vjry123LdrXkOdnjcYFnN8wFIcY1eeskWsowSch64oijLzeS7ELTkNcPvtE4EOTr4OYnwXpenh8uenotnxEW5zZmm1SCuwrcXlBoyk6thTq1S5dGVS1yHYz2FIYJ35IGDiqKaBHDnyU0fbNH_CN94Lr57E7snZZKVi2ZmCjB37dFEu8dEjzA5OXP72rL29yi5BymXN9iCuzsoHLoKVj3eA3viXK2bDwVb5DXUHwH1CepJpmwUdy3wiTcw-Zftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20934" target="_blank">📅 22:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20933">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGOkeQ7seQZ32kIy1k307wgHLQVnSUG5EkXG-0oBI7OtNWSdPVaMtO91Da6QREzvlmC_I0qVjsafJIicI_jlkZB0T8kc1Bgvw9dn1M4vGKRWkEGjzAdde02WymsEcNy7zN8YBFpe5QsGfhovV9VUPCmAVXn2waj9Y4QaxOgtR9L3L2TNh4fVIwGeaSxA2gTciV8eRNOmmAdmruRRsf8k46_8Npy83hbaqigKzAktbT9LbbysT4MhQIr9g6zjVvD3kFbjFBr4HefvHJpbLRU_AMpdHuTsH7Mkfps_rhBxFfcpt_s76RvqCtDknRX8J3Ki313umvyejvzxxIvlNLTpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20933" target="_blank">📅 21:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20932">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0hqF-WVy2_-CTOjLpwnW03JDRn3ob3RXPESfp70K_pz-17H9-pPlUypLaZGHdp5-BiQx5bwUc_l7mKERAgJaiT8TwB1hLHK5z8UPP9cXtwlKDdWcTwhx9MSalTk_EZ8KUJJAl72ZxcY4NE0lWwVy6iGferS6UdAh2BDT-qDz9U3e-ftOhSZdFDnkhL2m63ad-1cbZp4Y2LBYNlQYOoRVDw0MNhndMHNY8zm9V8OJsxzAw_ltBRg3FIdfJdbWBkjDyWt79uzncmxwCOcv6aF408w_1WLvHBe2hoANk-e9m9w2H1CjwenGSW1FncCITTUr-twGexpxZXS4VrS4wzlHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20932" target="_blank">📅 20:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20931">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=u3ir81tDpW8nnrSof93C0ED7daYiV73oEIFwZsQe6uup15jDSQ5xrtHwhgJ-lxeH5d2J7TXigtiYjpH-iAXBE24uso6L4pR1h4aWq3liUWWPpaUD_FpFUIax3z2NtxOSusdrdUEBqRtgaFlFVksIvsT_n-nj_E04oFEkwCGzQPl7tdK4e0H2g-gflpmSPUYvrRzkI7o8nXzm3k0KkczwkT6kQ9N_Ckz1DS3nRdh7KfZ-9Q4vAr6OyK4Q3zD8GFSQu5Czo5IyxsyW3oltCYtqIPpYEuj9jw_f8UnCKnDB8fbYro_mAha0UhPIT0exfV9pqxlsvKNMBJuNP-XOR2AStA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=u3ir81tDpW8nnrSof93C0ED7daYiV73oEIFwZsQe6uup15jDSQ5xrtHwhgJ-lxeH5d2J7TXigtiYjpH-iAXBE24uso6L4pR1h4aWq3liUWWPpaUD_FpFUIax3z2NtxOSusdrdUEBqRtgaFlFVksIvsT_n-nj_E04oFEkwCGzQPl7tdK4e0H2g-gflpmSPUYvrRzkI7o8nXzm3k0KkczwkT6kQ9N_Ckz1DS3nRdh7KfZ-9Q4vAr6OyK4Q3zD8GFSQu5Czo5IyxsyW3oltCYtqIPpYEuj9jw_f8UnCKnDB8fbYro_mAha0UhPIT0exfV9pqxlsvKNMBJuNP-XOR2AStA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایید شد</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20931" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20930">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_3utVKLhGc0LrV_QYunr200WHW9vwXhdT2nupAYlSOvqNa4NOQnCRy3BCUCyF8m1yf8xmySCAvyEKrC2D8BKFsSg7_t6B9g_rY5uzE97X8cOz4-VoBorBTzMsZrYK6YxeviqEmaxQn8t7-819uAUezDCty7gKnx5v4xRc7y50-lVFvq2AVSxAEK78zeG3v9metvrjmIGeN44CZOkRfjc3wbLP3zVfAtoTny6f6rFHBwMxKTcdGnZcDh6WY5KXuoz8P3Mv3mHBOgtCuffrL71-68y9xIKT0WZtbKgrASt-pDbNC4rG4UDvtkzQZIBXQHyh9pUOmbB4-nT_NbMiR60Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20930" target="_blank">📅 17:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20929">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MR-RxzqVrIE2RXcY97nzplWL_l_mnZ0oOQd2BrlYDXp1Ba7TdTKmSMktW7mi9uQHCQ6HDKbXXZ26BeUOHQJEQfqO55VHR8wtkF3bQT7lhf6dgUYRxz2wntsfEzPKdNWqMatc9A7ctn26WtEuoUdFDg59-ThhW4GSUvMMZdt3DNMscshVU8tydcDtrtbbW3IaEl7KJA-GcodLohvxIsPL_MWwuoSLOObiF-78w5Bu8B5scvonGpFT8h2qB_3JjRWzR7-a12Q_5JENvgw8Ya6cSW6Sbxb3npsOVFcQCXdlnWvoUTxEyyTz8aYte_P7Yg1vjvIpsMFIwTDRR1LcCERzag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20929" target="_blank">📅 11:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20928">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-GtYvGmlfiWZoA-68SLP1oj0LAL3NtmTO-oFi0a7Q2fMYA7fiqctewa6ZhO-LxdvFwTrFzpJ_gOTw01fHiwb9zQq9pW5e4DUy_wKHEdfb-SLdt7VruAK-1Lghnu0YG4nuzZ8Tu0rJ1r4kKWHpn_3xaaAStXYWSXA65I_LirTl-_dT_EG4faMj6VCdRUKpUS0NO5PTsxf5tqaWaWISaJP4ql1ZTzE_3eEl5VVj0sURA_RwUaXBIifnDPVUNnU4kun22gE_7jyX7ZVQ2QUbRyGBcV9nT9poc9im_BdJuHOEOHcfVU0jM8A2HwYMGs3lBjWd8ogQmNh-WbnPIhSw3bxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20928" target="_blank">📅 10:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20927">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=MThmgxdfTk_HHlYagRZClVo9d5YytoMrw3AgT9ojOyLWjtjWWjrzyqBF1kyV9WVErEfPYoEYE96BzgkTg57w3XbiJ_ErPYy9Dl_T_EihtK-pYxCl2I4zApClOI3otq43lY7HOVsYH8quuswHBxVsWusUykN6APgS1DGaeq6TEgfcqMH2deRW6GAFRK3u2GNtjYblcD63UWbLqRiGGHInETJAJRnDXT7xswJIaVmRiOryVZL-u8j5HyHGhADGg5-w8HAIKA2AS_PAvy9mj8bdxZOkUoyf1OrQkOPIW8vPJBkbZ6EjmDtygvrEuDORT4jLpiA_WOL7kwQl5JeJrjnKPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=MThmgxdfTk_HHlYagRZClVo9d5YytoMrw3AgT9ojOyLWjtjWWjrzyqBF1kyV9WVErEfPYoEYE96BzgkTg57w3XbiJ_ErPYy9Dl_T_EihtK-pYxCl2I4zApClOI3otq43lY7HOVsYH8quuswHBxVsWusUykN6APgS1DGaeq6TEgfcqMH2deRW6GAFRK3u2GNtjYblcD63UWbLqRiGGHInETJAJRnDXT7xswJIaVmRiOryVZL-u8j5HyHGhADGg5-w8HAIKA2AS_PAvy9mj8bdxZOkUoyf1OrQkOPIW8vPJBkbZ6EjmDtygvrEuDORT4jLpiA_WOL7kwQl5JeJrjnKPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20927" target="_blank">📅 09:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20926">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20926" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20925">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20925" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20924">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8k0mrt815BiwHuoB2DBvQDKvFLA5KJMFrr-d7DFu-DEcmWfu84dFPyJSzPq4ww6zPYgCaR6w_tNwxcVaUGAWE6I50PS78pai-CPwA1rHhX2z8eHkHgYcra-RcpbzzE6AzUYBQH2YzFJGzl-y-futgq-PerioL18ENpI-CfQUQ_CN3cg1NGhDc6jahAt3pxSaw5A9aejXfXK9-6vPhtcGGwke1CFGjqFnAvmwCJY_l-AhwQFbU7aWEAadtnji0tKHzvZLlJZkyxXydJqydtvYqSQ56Zaet8cGYj9o6pWdCFyptzuhv5ohiWHQH7IMD5GdQZj_tcraYGQaTWmnBZIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتر گفته بودم در عصر اقتصاد دانش بنیان و هوش مصنوعی، تنگه بندی و راهزنی شاید در کوتاه مدت نتیجه بدهد اما در درازمدت نتیجه عکس خواهدداشت.  (به پست ریپلای شده که حدود ۲ سال پیش منتشر شده نگاه کنید)  اکنون این ویدیو را ببینید و دریابید که چطور بسته شدن باب…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20924" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20923">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgGSSANVvcfwzF-oi5LMXUYrusfdRwPRjhqNmzQ0Zq4Vz6rve9PYoOVwXV3uea0eCBZtIinM9PBaMK3c-yjMtnbrVgvhhxkcYhvPaakwSY346oKxMrPaw28IyMj6zUHqUuCMFMN5Lczj05Ow2DbbuGpDl48knwvqjoklSAdb9hLP-sgzOiuxhopaAHTccsRYBz3TK5iscMaKuuV190XxZEj37lbpgO58UUaE6fsMrLJxQzcGdY8fev5GKdwZeBt5GarihVWI2-PjWuuLePJTj6zm26tza_3AAP3kilCgUJe3Z3GPbUmKZ_kIRkYLU8RHneNxxP1HaWytC3P-8m7hkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20923" target="_blank">📅 00:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20922">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPAbeFY9zuMzPBEyMqERlUY0EOUuHxjNjwaTK8DZKkdiuuj1OSW9RkYoAVulfZxQ55CrLQ9CXDFYRZPkARZA1AXw-ZX5l509O_dyXYUNaNucGpvn8qTxWjihUhzvcY5fah7o_IfXU1YNZXx61H0OpuFnQy-HNyMYkg6O6b7RXQ-IiN-5jEoX3UharRKYcbF0GfOnvYq1fAIouywoM-UQbcaNTBV7NMLcu6OsMa5VsyEmEg6HCiBdyFYHGbi809uzIfbEJglNP5npriuCy-RkXyHtvjO4RhHn1XKfEUX5RnmBbpUGFSexa2HQEpBJHLHa7Xu5DgLEiU1VXqmlP9Pvng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 27</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20922" target="_blank">📅 00:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20921">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nug6u766rgN_OsU1hLUpDtr07U5QgNGSGtdqwCspDyw4AygtSCpOKwj-3Bv1EFnAMEr6ZmeCAMTcQses54MTlXiZ4Fshrq51Vdyvx87hU3FotMEHoKph6F7lmKPkZcWnJjqS2xALeh_TnYbrsYRGZ8zgFsamgqP1v_zLB39hCxFAX3aci5me0cm-zWdw-AHRP9nMzhWR966Tk3Km1UEyndS3E3AkwO25fr_5aC_8s08-TVjRW4Fara9ek89tlv7Wp-7x7SxI3JIwvuJdcFyoKA0jNslf-BNe6azTBIXp8OhFzCtRrhFRsCa7a3kN2IomFEwQRs_MUFltNe_qhCt34g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20921" target="_blank">📅 00:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20920">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20920" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20919">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20919" target="_blank">📅 21:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20918">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عراقچی فردا به چین سفر می‌کند</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20918" target="_blank">📅 19:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20917">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آکسیوس:
یک پهپاد آمریکایی پس از تلاش سپاه پاسداران برای توقیف یک پهپاد نیروی دریایی آمریکا، دو قایق کوچک ایرانی را در تنگه هرمز منهدم کرد و اکثر سرنشینان آن را کشت</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20917" target="_blank">📅 18:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20916" target="_blank">📅 18:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20915" target="_blank">📅 18:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20914">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20914" target="_blank">📅 16:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20913">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20913" target="_blank">📅 16:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20912">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqh58_WP-EX6VYqZTqg7btc_J2UVm3mDYPlQ7RSN3JpGa15M4limeXWFi_DD7M-Rrsx8goP0jcsOoAc20COjxigksXsAG_jwrPjopykDohWaMG-WgQ6XNJKp6Pj33TLCIDeu4Xrid54W35F1QJFE4aueLZ3lNw5mZXlmr6JHZooBiY_6v_VYthZoHVb5asD_VFcOqs6n_Vcnw7uEN4GSp0PgvpRBgdsPMJdHPutve8cZML6QDAvz1uvdqZKy-xpjBXhnJQGU028XmMiFLEI4fN2dy8ishO86pzREUJpAmn-cXs6zS-3P3c-ixZEaZCTGstyLDCQeGZFLfYUxSx330Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سخنگوی پویش جانفدا :  جان فدایان غیور صرفا برای اهداف نظامی به کارگیری نخواهند شد ، به زودی پیام های جدیدی را به این عزیزان تقدیم خواهیم کرد</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20912" target="_blank">📅 16:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20911">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20911" target="_blank">📅 16:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20910">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20910" target="_blank">📅 16:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20909">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">به نظرم بین اسراییل و ترکیه و پاکستان یک تورنمنت سه جانبه بگذارند ببینند کی می‌تواند برنده شده و بیشتر گاو شیرده حجاز و نجد را بدوشد!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20909" target="_blank">📅 16:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20908">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رسانه عبری والا به نقل از منابع:   تماس‌هایی میان عربستان و اسرائیل با میانجی‌گری فرمانده سنتکام انجام شده تا از طریق ارائه اطلاعات، به سعودی‌ها در دفاع از خود در برابر انصارالله کمک کنند</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20908" target="_blank">📅 16:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20907">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20907" target="_blank">📅 16:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20906">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">در سوریه با گران شدن سوخت، اعتراضات مردمی آغاز شده و آشوب ایجاد شده</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20906" target="_blank">📅 15:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20905">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 27</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 27
سه شنبه 15 سپتامبر  2026</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20905" target="_blank">📅 13:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20904">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20904" target="_blank">📅 12:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20903">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20903" target="_blank">📅 12:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20902">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hn308bbHf7aHeGnGp2dhXLnhYocDCYGVmj3g0BdoZVEEABLaROYAD3uObHtdaFA6LXXdJkK4Gzkbr0nZevR0E8ks-wilxGARHxkmAv6QGUkuOS7vvI5_OjdpDwNKpUH0Zh92fMuJ9gMcG_BI6nV4hcLGRAnQyuwf8vO5P3XohjRV7IL6ufoONVYdgxeRIMNIltN99GVeosfgnXBovsI6q5gnjlRnfRuPNj9_lH19FHdLM4puzeJ1DERjYLwbfBRtpoydO0h7SnWeVRe2uwNQCWVjbDXnrNsS6au-LmxFIoUQ0dkYj15Jv7WI372jqqw-YwUUA9GMYiUX5m87PyvLdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20902" target="_blank">📅 12:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20901">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQErq77Vrs-668EhjxgBkmut94QXiJ3gr-ScJnnaNmZHmoPFU_kEvdb9tRJmor0fbQK5HSrm0-zHg3f8wjZ0tT_8Ys-olN4ODHxFzyXyR3MbFFvIBG7szAX9SVsNk6fn4FTkZvEj_HAi_jW5xOGNdWRxenQAeqW87d-7EsKrD9NYFCyuRUFQ9iRxbj1tw2fGgch9_qQ4LS5vOXQzM0lC3n_CwZtPHO4egk3Yb_4jReFqqwFKNkFZvRy0BlrlZSD-6TbdzWCl4jZGw9vtLhACI-IUB5xjS8cHWFJya2BtzP0fEpxqvdLC3PJXg7nBPOln00CSjZ_FFxc0XmrRVZRCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال: کمک ماهواره‌ای چین به ایران  به گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی می‌گویند ایران پیش و پس از حمله موشکی ۱۷ ژوئیه به پایگاه «موافق‌السلطی» در اردن، از تصاویر ماهواره‌ای با وضوح بالا از منابع چینی استفاده کرده است.  در این حمله…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20901" target="_blank">📅 11:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20900">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKqgL_ZiL4CHELOeDRvEQxz4kEXoMivr-M0EzcCTFRTtpOcf8q0oiBQQ0_W73nMFhbXRCsr2VXGTYkGa7PKJ9-Kk4SFhfmL-P7jSfHlQhHcph-cyGNemX_t9hR0L2fEg-BMHzPBNcIzeM8YpH04k-SgUIVyo-028BwSp7Y2hFuTsRawJiX6GZLPy-nNGTZCNAQNhiuEt2MRgDYQNfvEdvKTC_tiN-T8IWEUfx4b2Dotp3_r8Z-gUxLUY4guYpzBBC3qaFlrbZsXWnrkoiougu9SZ_5l9sy8NduTDr67VPBs4JkDmtAfEqngPdo-5o0KNZtg10mZhO6F0VIJCAAnPjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20900" target="_blank">📅 11:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20899">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJQpOlhV1SQx2S-x8i69cSsw9HJLNI1E7QMizNMPNh_HjMui_ut-jBimoD_n2bZjuzznCzVQsmv5ovs97zaKk4HgQxIzc88zy4Q23qFjgOcq8Usp3XnNMoHAiFRMWIEgn4z7RyEP6qjPjUMAz-KM3r8FAwt3A2h4-AKqdWTj-1b8i8wqluK2F3eM2mXp9UqkVEzklIBxO5OhlxTtAQWtxir0tdaORDsFkcejkYL3iNoAxc_jyARJym1jE4vM5Ig8oOztn6x4jS1lcu6nlBbxcc2XrYVpeMp_N_H49sTilbqRPFFjcS76BO7OFISAYq3d3pBQ_fFXhBnT7gHnuZ2yhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.
بهترین محدوده خرید از 4280 تا 4250 می باشد.
نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم و پیش بینی میکنم این هفته طلا سطح 4400 دلار را پس بگیرد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20899" target="_blank">📅 11:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20898">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6XHMDZir9J7kjFiaBfzGLHh_kExVVhosGajjpb0OKJeAhTO0c6lzP8iKxNt_DIJni9XdYbrhmZwWJds0wDGjL_4g6AOxctmETylhu__qwm0J97Jd1fcZCInMcLxNUGqtYNR4w4sR78mMN-u8cny9dgcANfPHWmoSwF5GdLs-BhIn1DqFdals0NVxvpNByJuvh2G8bTB7VDHYh2fEj4bN6XuBYVpL_tNcL4xpSGMUCwEk8dfxXPe9h9aMxwvFUIe3qM5cgmgyBKuXY8APDQ7eJ6a59sQIWE8tzpbgH6iZ3PWT40xnp7GekqEhCNOCNS_7D1Js8hjVOurXO1K1PyH6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح نسبتاً بالایی است و احتمال فراوان هر بالایی فراتر از 4300 فروخته خواهدشد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20898" target="_blank">📅 11:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20897">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5b2DQtZFTdEfrVDK55aYLtTQ-nZvb1WKwQPGsy6k02Rtn6bgVze2j5_y8CiXCBNH0koeo_0vDJS3uq3PnpFZnGTY1QeXaa34M-uPQpN10lCS6q_pldATn6x6BPktDvUAd0ea2aXrnC3EBzCBy9oWWBHqGuCewn_7POVqPr2DIerhyKMwUWwYcyVXrY1heJC9KKNaz9lGx8v7Vjutt29dH10bgN3LxKrJ0f0T3qwmtpSIpsB1YYS9OfmODd0f4ih0XuvVjeFtTq-_NtVaLOXJqTUwzg0Bai2uW2I9Ek5ePC55EuZRHviUNLhQBjHM3-1sN5TPC6EO6kFV9QGZT8KEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله حوثی ها به عمق خاک عربستان در ۱۱۸۰ کیلومتری مرزهای یمن!
و کماکان از متحدین پیمان مکه (عثمانی و فاکستان) خبری نیست!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20897" target="_blank">📅 09:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20896">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جمعی از نمایندگان مجلس در بیانیه‌ای خواستار تجدید نظر عضویت ایران در NPT شدند</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20896" target="_blank">📅 09:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20895">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">درخواست کمک عربستان از انگلیس برای حمله به یمن
بعد از مخالفت آمریکا با حملۀ به یمن،‌ عربستان سعودی این‌بار از انگلیس خواست که در این کشور مداخله نظامی انجام دهد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20895" target="_blank">📅 09:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20894">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک بار از یکی پرسیدند تا حالا اتوبوس هل داده ای؟
گفت نه ولی یک بار تو اتوبوس هل شدیم دادیم!</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/20894" target="_blank">📅 01:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20892">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آن‌قدر به ما گفتند ترامپ تاجر است که قبل از جنگ به آمریکا پیشنهاد همکاری ۵۰۰ میلیارد دلاری دادیم!
- حسن قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20892" target="_blank">📅 01:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20891">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKNpzpEnwDxYtMFssSPQre4HfKedFU9ovjqkug7i52kkbiDzryuSyL5UGMnOpaPBncigVwp1vEy6pkFBGnlyejiegJIMgiX9oeB8FCDBQwWvqVUDJdoVNkKWpqd6v3oef6OgNDjQb0T1fN0gqT7_qjxWdqO22TDlC3KBL_qF1-2hPz95xeP41bF_RsTTDDfgQB_dpinO1VlZVQF5o7jThHtQY9yt5BFU1SDA4vq6SoU3CQ1RcfDGlzLo7YUXwMiTKl-aR5RVKdVNbwX-vURWVdZGQQdKhXvzOwUmvkQC5G5Uh8Trl_BHRXPcazaBLVFBxv7Vv7fwrO2U3U9l4kY32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
💙
😀
💙
😀</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20891" target="_blank">📅 00:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20890">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">برنامه ریزی آمریکا و عربستان برای حمله به مواضع تازه تصرف شده ارتش یمن در ساحل غربی
یک منبع یمنی وابسته به مزدوران سعودی اعلام کرد آمریکایی‌ها به عربستان سعودی در مورد مناطقی که مزدوران عربستان آن‌ها را از دست دادند و مشرف به باب‌المندب هستند، فشار می‌آورد تا این مناطق را پس بگیرند
در پی این فشارها عربستان سعودی با کمک نظامیان آمریکایی در حال طرح ریزی حمله ای به مناطق تازه آزاد شده ساحل غربی با نیروهای سلفی و سایر مزدوران است
این منبع اشاره کرد طبق دستور آمریکایی ها به بن سلمان این حمله بزودی آغاز می‌شود.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20890" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20889">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پزشکیان:
برخی کشورها در خفا به ما می‌گویند ما با شما هستیم اما در عمل از آمریکا حساب می‌برند و جرئت همراهی با ما را ندارند</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20889" target="_blank">📅 22:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20888">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پزشکیان:
آمریکا چون نمی‌تواند رهبر ما را پیدا کند درباره سلامتی ایشان شایعه می‌سازد</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20888" target="_blank">📅 22:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20887">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.  سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20887" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20886">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.
سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه مانده و این نفتکش اکنون کاملاً در آتش می‌سوزد.
آن‌ها تأکید کردند که تنگه هرمز همچنان بسته و «تحت کنترل هوشمند» آن‌ها قرار دارد.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20886" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20885">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گاردین: طبق گزارش ها نخست وزیر بریتانیا در حال بررسی اعزام ناو های جنگی برای حمله به حوثی ها در کمک به عربستان سعودی می‌باشد</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20885" target="_blank">📅 22:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20884">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">روسیه و اوکراین دارند با پیشنهاد ترامپ برای تعهد به نزدن تاسیسات انرژی یکدیگر موافقت می‌کنند</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20884" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20883">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20883" target="_blank">📅 19:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20882">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ادعای ترامپ:   ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.  من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20882" target="_blank">📅 19:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20881">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ادعای ترامپ:
ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.
من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20881" target="_blank">📅 19:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20880">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20880" target="_blank">📅 19:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20879">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اینها تغییرات بسیار بزرگی هستند اگر خوب دقت کنید.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20879" target="_blank">📅 17:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20878">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20878" target="_blank">📅 17:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20877">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6BLzjsQRtWkj2_8omzhIpOQ0IHbypG72oT9RVv4SiZq-JFXzQeC6VQj7Uyl66XatP3vZ6QqJFVVdTN2k1IH7526FbFazjwPd3POOxHQVkkzTS8025z75PhimfcTCrzCLm9d7le9E1yylnViINa_zdabqFh7nevcsS1w_VnFDK06GPxeOsUhWUqxKVKG6ue__ryTFn4YOEMvsgBHfqD0B4ZIOpuRA-5p9LWiCCKas-jMtighPBmqi18eFqYeRgteFkLweCC42xeyLUqRpISRm3XmA2AehzdzhOU7eJVK7ed47RFjWU6U9nG9Tc8pv1Hb_E73Nu-leBlTk3xdkMffaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی احتمالی دموکرات ها در انتخابات میان دوره ای نوامبر عملا مبتنی بر یک سنت تاریخی است که در دهه های گذشته بارها و بارها تکرار شده است</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20877" target="_blank">📅 17:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20876">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBIkgocOHr2M1vX6rbFBoAvYoILeNd6RfAV8YEXk83S-lDgPXaVrulj44KzesYWb09v4NN0XXXLdzMjTlvk7XPYv_y7oDmpcpE7tIYlgY5r-N1HpV9dSa62nIz8Qkr40f7iF3Bmc6xUTCrd9eLC-itSjBeCoh7M2GmV58D4Lyns7-C01u6rDHGi92QZQ7_Tg8owVsK9hEzxQT782piInCH5KPOgiTFPWyjpkBp3W2bayGM5LULhIg9yIipQQQvMg_jRer65tfTD3ED3oWQ_8QojvkaRDoTrnZc0lYJKlVNojm4wufEwy-7EfQfxr19TVSM6NlIQIXsIQ1_X0u6gtaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20876" target="_blank">📅 13:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20875">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20875" target="_blank">📅 13:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20874">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNHgvhL_DDxtDyP5CDY6PJGNdxbKlgu2k8mfNunXa0dhOaG4StICQRitmAeuvz86hCkXJ62HI7U-n3kymWdX2_y_ZJM1jz-tUOY7wRBZol1dLiCM4qfNzceRZm76DGpY9CkkVJyJjRKKEfnoVtCo713N67BH_hpcE9C_qY-Ln9nKhJRfvtoK3-Aqf_eRvEfBsKo9KHB7NJDxG0VMQa7sc0ja3IxVYfOoXNWmpK48k-i7vZG-uv0eG-ScH90U6nhoxDnf7dy54K6RlkXhAVdtb-q6WY_s8K_THBfnU56VUGwDln2cGGZijHdJ92_TOwjl1o6ghOmrMoWpcqy-arQkrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20874" target="_blank">📅 13:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20873">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک آوانس برای براکصه در آستانه سفر رهبر چین به آمریکا</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20873" target="_blank">📅 11:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20872">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0GmXrRRuc3MdvqldjuedV7oOJb2c1Y8FSXMmKTkECQQeodB3X2d2SXwtVTvxYf_2Me-GLzGeQCoJMtkQm5jjcpP6Jgn4zc9p7mZAXmgUke1LM-htrDk0U90jV9AKKSbVerkuCzPCPdpxW-VYciT0A7TYkVEMD92otO1Cb0POQKDuVWdhbcjYDR9ujRYUsVK1RntNGgeuzO2F2X7j8LRoN8fq4zw4LTXTL7vOdK5cgHWj8qCF4MiG90g1FqGZHIZ3nYuBhGp78zy3QmYfAXyiyxgRsyiw4Rfl_VGLkhlH_KwjGvZzU-cvxeJE2SjvFO9QKZgw38J7ssxZk87-ISOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20872" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20871">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcB7YpzEQRkGKuR989VeyFyid1gINnkEbE6QxKvdRVqn64oZWGYeOgskcDInjoHLYlW7aW9hrWAmXqCJXQa8z42SUisbk62AvqY0zjvBM1mmA90g5IQv9cdbINczHHbrfjw6MKNx8-r3kuPh-GnIrDu2Sx2gRVKEx5QSmYxyJRiVzz5VNiJsYUDvBAgEPLmxN4BrXOodUgQaSzZZT6hJ8-Lx-JVinvvXQKWgC8fTngCvtO0kNuzfe8-z0TbgHbl4iPGIyvHH7UwFRsDtCTk_U3VMkr9UuVuePWZgseJT-pP1T1_JW_uCdpuI5G1JaX_ucjq7iWARWcq1BGVwvadQcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای است و نظر به ریزش طلا تا الان، انتظار یک اصلاح صعودی می رود.
دقت کنید که رشد طلا «اصلاحی» قید شده.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20871" target="_blank">📅 11:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20870">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20870" target="_blank">📅 11:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20869">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20869" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20868">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!
محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20868" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20867">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8Bp0MYGkoaeAWCdKmnfSyISwZlj1XHluHIpNdZrqLg8wUShZYkOpBHxCtAstQv4hASs5vp2VFvjKUDp_HUnlLvcIgoniKWy-eYB7UX_5Wejmg9veEWW4WzNXiOzb7ZRFlbHvztt61Aubloi9m_0iq5duQHHUHHcicQljWdN8NRpeeLtDz8mlpkhnNwff3zeA8acqAm0RtjXn3__g5QvbM5MLg1mObln4xF1IvDRVQI1oKRPgZzBLrysj00S4E9WTT2vksgZlkCzp1a_7O3-ujiBpdJkDdWj1PK5BrhKnYMYPa7j2jM4b6Z8wtfT9uuR1NpaF07Nvy714TgOjqJgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت تحلیلی | سناریوی اختلال کامل در مسیرهای صادرات نفت عربستان
یک سناریوی حداکثری برای بازار نفت، تخریب خط لوله شرق–غرب عربستان، بسته‌شدن تنگه هرمز و هم‌زمان بسته‌شدن باب‌المندب را در نظر می‌گیرد. اگر هر سه اتفاق به‌طور هم‌زمان و برای مدت معناداری رخ دهد، بازار جهانی نفت با یکی از شدیدترین شوک‌های عرضه در دهه‌های اخیر مواجه خواهد شد.
اهمیت خط لوله شرق–غرب در این است که به عربستان اجازه می‌دهد بخشی از نفت تولیدشده در شرق کشور را بدون عبور از هرمز به بندر ینبع در دریای سرخ منتقل کند. ظرفیت این خط حدود ۷ میلیون بشکه در روز است. در شرایط عادی، صادرات نفت عربستان حدود ۶ تا ۷ میلیون بشکه در روز است؛ بنابراین از کار افتادن این مسیر، وابستگی عربستان به مسیرهای دریایی خلیج فارس را به‌شدت افزایش می‌دهد.
اما اگر هرمز نیز بسته شود و خروجی دریای سرخ از طریق باب‌المندب هم امکان‌پذیر نباشد، تقریباً تمام مسیرهای اصلی صادرات نفت عربستان مسدود خواهند شد. در چنین شرایطی، ظرفیت قابل استفاده برای صادرات نفت خام جدید می‌تواند به حدود صفر تا ۱۰ درصد ظرفیت عادی سقوط کند. البته این رقم یک برآورد سناریویی است، نه پیش‌بینی قطعی.
اثر اولیه چنین اتفاقی احتمالاً در بازار نفت بسیار شدید خواهد بود. بازار نه‌تنها کاهش فیزیکی عرضه را قیمت‌گذاری می‌کند، بلکه «ریسک عرضه» و احتمال تداوم اختلال را نیز در قیمت لحاظ خواهد کرد. بنابراین افزایش قیمت می‌تواند بسیار سریع‌تر از کاهش واقعی تولید رخ دهد. ساختار بازار نیز احتمالاً به سمت backwardation شدید حرکت می‌کند و پریمیوم نفت فیزیکی افزایش می‌یابد.
برندگان مستقیم این سناریو، تولیدکنندگان خارج از منطقه خلیج فارس هستند؛ به‌خصوص تولیدکنندگان آمریکای شمالی، کانادا و برخی تولیدکنندگان آمریکای لاتین. شرکت‌هایی مانند ExxonMobil، Chevron، ConocoPhillips، Canadian Natural Resources، Suncor، Cenovus، Petrobras و Occidental می‌توانند از افزایش قیمت جهانی نفت و کاهش وابستگی بازار به نفت خلیج فارس منتفع شوند.
در طرف مقابل، خود عربستان با یک تناقض استراتژیک مواجه می‌شود. افزایش شدید قیمت نفت از یک سو ارزش هر بشکه صادراتی را بالا می‌برد، اما اگر نفت فیزیکی امکان خروج از کشور نداشته باشد، افزایش قیمت نمی‌تواند به‌طور کامل زیان ناشی از کاهش حجم صادرات را جبران کند. فشار بر درآمدهای دولت، پروژه‌های Vision 2030، پیمانکاران و بانک‌های داخلی نیز در چنین شرایطی افزایش خواهد یافت.
اهمیت ناوگان نفتکش‌ها و مسیر SUMED نیز در چنین وضعیتی افزایش می‌یابد. در صورت بسته‌شدن مسیرهای سنتی، دسترسی به مسیرهای جایگزین و ظرفیت حمل‌ونقل دریایی می‌تواند به یک عامل استراتژیک تبدیل شود و نرخ حمل نفتکش‌های بزرگ، به‌ویژه VLCC و Suezmax، را به‌شدت تحت تأثیر قرار دهد.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20867" target="_blank">📅 10:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20866">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رقابت عظیمی میان ترکیه با اسرائیل برای ایجاد هژمونی در غرب آسیا شکل گرفته که بجز جنگ با ابزار دیگری حل نخواهدشد.  بزودی در قفقاز هم شاهد تحولاتی خواهیم بود که نقش و جایگاه کشورها را عوض خواهدکرد.   اسرائیل به شکل هوشمندانه ای از دهه ها سرکوب اقلیت های قومی…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20866" target="_blank">📅 10:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20865">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fODcHCVVfGK4n39KQ0piFNP0cDP6kfmcFGZU4B91idvhqQnz89SN_QiYMPo1_NE8V5ZZRqbvE9G--lHJvH0b2TB09Muwxx78oXnvjVx2JVmIrUkZhJCD5_AYcP6lXFsIMYmcbsfBXw9FFf8FiCFEw2SL2VqT4Ww0jaSGl0zRU78Cr92WaGMerW0r4vfLWijlW0fP_fRHTFfcQwQccCy95ALzk_tYsZigW9K8kspOlct5MkpF45eYnqiDzTj8VmO1wYa5Eu5-bn3GFCsBr3n3Agzl4n455U5qLezusJS872usAF4mvVYHj3bG7YJit-StvujZLHjosxj90mazf-cwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ نفتکش‌های VLCC به شدت افزایش یافته و در تمام مسیرهای اصلی به بالاترین حد خود رسیده است، زیرا جنگ ایران ترافیک تنگه هرمز را مسدود کرده و جریان جهانی نفت خام را مختل کرده است.
هزینه انتقال از خاورمیانه و خلیج فارس به چین به حدود ۱ میلیون دلار در روز رسیده است، در حالی که نرخ خلیج عمان و چین در یک ماه ۳۰۰ درصد افزایش یافته و به ۵۷۱۰۰۰ دلار در روز رسیده است.
این محدودیت فراتر از خلیج فارس در حال گسترش است. نرخ نفتکش‌های غرب آفریقا به ۴۱۱۰۰۰ دلار در روز رسیده است که در یک ماه ۲۸۰ درصد افزایش یافته است، زیرا سفرهای طولانی‌تر اقیانوس اطلس به آسیا کشتی‌ها را متوقف می‌کند.
موسسه لویدز می‌گوید که خرید مجدد نفت خام چین، ترانزیت‌های خطرناک تنگه هرمز و راهکارهای ناکارآمد فزاینده - که اکنون با تعطیلی خط لوله شرق-غرب عربستان سعودی بدتر شده است - عرضه نفتکش‌های موجود را بیشتر محدود می‌کند.
با توجه به اینکه حاشیه سود پالایش هنوز به طور غیرمعمولی بالاست، اجاره‌کنندگان تاکنون می‌توانند شوک حمل و نقل را تحمل کنند. دلالان می‌گویند هنوز "سقف مشخصی" وجود ندارد.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20865" target="_blank">📅 09:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20864">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Miwpxvn36xjWT7UmdG9cuUZo7oV7n7PUKnuemQMZG7Q6FNg5EZ1hxkOW4h3FDnFnmRO6vEEA09IeLMNylbNyJTqNLPxUygYv3h6EgRzdDsa35mtaTXcqP6c_wWBAZDXTjkgQ6nZc9wOqMWQ3aXaFumO04Q6PiZrW_TYEe-_RjaehPf4zE-vDqowYVxfOrArNbFgO-sy4iZpk-gmPSh2NKbgIbrk6fVRnuk1tsUDZIEu-ouYoRGpEeHGugUUTegA9YZ7NhndnLiRrpZnrUN5V8zZmD0U-Ud6WTuSUXZ3xuxvKqUVwuW4we0A0tgYvmmhqqyNFP0jn_G09ohyxi2vDug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی ممکن است تا ۴ درصد از عرضه جهانی نفت را از دست بدهد اگر خط لوله شرق-غرب آن به سمت دریای سرخ در عرض چند روز
راه اندازی نشود
این خط لوله پیش از حمله پهپادها که منجر به توقف آن شد، حدود ۴ میلیون بشکه در روز به ینبع منتقل می‌کرد.
منابع صنعتی می‌گویند ینبع در حال حاضر فقط مقدار کافی نفت در انبار برای حفظ صادرات به مدت پنج تا هفت روز دارد.
این منبع زمان مورد نیاز برای تعمیرات را فاش نکرده است؛ برآوردهایی که رویترز به آن‌ها استناد کرده، از راه‌اندازی مجدد جزئی در زمان زودتر تا ۵ یا ۶ هفته طول می‌کشد.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/20864" target="_blank">📅 09:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20863">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_yR14mpV4q3Bf9l4mrPcg33ml4YRZDewml5lgb_z_dgzasPitOG_IN9qBrM150SuOnknhPoqwP8FfGGGAtdpkp0_JoK6vzoq2pL15QJ5mJQOx8xmHuKlrOT1RgpfS3B7vG2KOOeTNBZa9Oo-vlpjZLW4eDFAMx31nipOjBERzAu3u6N5LeDexXDxszdZjOiOcSxED8b1RZKDmnwG4nZF34wxu9B2PDVR7ME02jf2WPlMTeXGGikmHDe4CQLvB4waa8S9jF1KIIpPa9kzMP7Ux6fTbDlxvBP1BV0lPHELO29tnWNkv8v6PhqdE9qiOaJaLUqk8JWoDKCrCDwtoGJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه عمان پرچم  شیر خورشید ایران رو گذاشت
😁
@Piknikanalyst</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20863" target="_blank">📅 00:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20862">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نشست فردای ایران، عمان و کشورهای عربی سر تنگه هرمز فعلا لغو شد</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/20862" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20861">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شلیک موشک از ایران به سمت تنگه هرمز</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20861" target="_blank">📅 23:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20860">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BjFcpb_6cew9zCHmKFCx35qcWkHtyAsHB13ZFfxqfNejbOT_kHnD6Y83NJyaU4rddiztTV35QSLuGnGV2rsliCKL_UhP8M6BGXzp17WThRKN7EXvGTQhxND9TMi6SNyZcjhgX_S2uGHLuai4dLsm0v-8EnSKmkEE64xn0Sbub4QL_mpxdPYET5KjTavHZiHQhdYPr3kq1P66gVxmBEPJhw_uzeP3dK7Ze1FqmH5-TduA8cBVqpflcRJgPW4PIW8hnQ7FsVkKb3h4zyRTu8K8S0KEiKHM2_g9SKPNCQVrKzx2zGxbB_lPGoCjU_AOqWVckq7A-9fQwh1KCgdFQuUqIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه عمان
پرچم  شیر خورشید ایران رو گذاشت
😁
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20860" target="_blank">📅 23:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20859">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">توافق ایران و عمان برای تنگه هرمز به معنای باز شدن خودکار تنگه نخواهد بود   منبعی نزدیک به تیم مذاکره‌کننده ایرانی به تسنیم گفت: درک چارچوبی در مورد مسیرهای کشتیرانی «به زودی اعلام خواهد شد»، اما «فقط» بین این دو کشور است و مسیر جنوبی هرمز را بسته نگه می‌دارد.…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SBoxxx/20859" target="_blank">📅 22:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20858">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vf72uJWpS6YFD3xwjBKrhHjrNdcvD_y5sWG8yCCklLlImg1UIRkD5S09AbCF2-e5hfaHpLrOyhZrtuQ6Bn3I18EqpHak2p1TXR0I_ap6KL4tK_qYCv1PUWnMypjnc0I7ApJ36QViUwj3ICmA07WYi8P-KidF56RmH1IxRiUCaUgj2CnX_niJwp4zCYeHOswgs_AEVHdJ3wjfjdagQeUjfVP5l8W5kpfMar1e99IjfQTLedCbO83DdvzH-PK29HwojOOd1vyz9A-qv2GfuKYWujTOvj_SKoynIfioIDgaAa27PwPC_9YnBo7OX70RPMxMnfCUQDvckHhiywKGYXYx5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگنده J-10C چین: نیرویی جدید در آسمان جنوب آسیا  جنگنده J-10C چین اولین پرواز رزمی خود را انجام داده و نقطه عطفی بزرگ برای صنعت هوافضای چین محسوب می‌شود. پروژه J-10 که در ابتدا در اوایل دهه ۱۹۸۰ تحت رهبری دنگ شیائوپینگ آغاز شد، با هدف توسعه یک جنگنده بومی…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20858" target="_blank">📅 22:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20857">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فیدان: سوریه می‌تواند جایگزین مسیر هرمز شود
وزیر خارجه ترکیه گفت:
سوریه می‌تواند با اتصال به اردن، عربستان، عراق و ترکیه، نقش مهمی در ایجاد مسیرهای جایگزین تنگه هرمز ایفا کند؛ مسیری که قرار است از طریق راه‌آهن، بزرگراه و خطوط لوله عملیاتی شود.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20857" target="_blank">📅 20:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20856">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDuwHgHXfEAadHUhKhBQwEucVQvMNu4F6ziw7QSm44dRXpGKElh0TowdoWZFj3FnccIfGiDv0M03LNpZQl7FUYnIOdD4R1lnC7-earVEAMvE1Ao72rsPRe6VjNjrEdCSCuPKN6K8UFXnY8cmSXUEN0NHjzbhbhiPkv-v8bCP1G-I6-qYke8h2t9K_ZplDHKUMYPXdt7VDFAipOlD4-RqJIg2-VM3TapJE_37ZYeKnwsJVf3Q-U6c_DiAf8vP-JqvUieBzrSJTwq3z_E0FsFOEyHvILDerwjtLW0HaOqHo_Xqj5CF9-EblqV-CbqAs8w-unF2sEAFGRSOlma_MWwFlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشیال تایمز:
ایران از روسیه درخواست پهپادهای اصلاح‌شده «گران» را کرده است
بر اساس گزارش FT با استناد به منابع امنیتی غربی و یک فرد نزدیک به کرملین، تهران به مسکو برای پهپادهای مدرن‌شده خانواده «گران» روی آورده است.
باور بر این است که ایران قصد دارد از آن‌ها در درگیری جاری با اسرائیل و ایالات متحده استفاده کند.
این نشریه علاقه تهران را به توسعه سریع اصلاحات جت‌ساز روسی و افزایش قابلیت‌های این پهپادها از نظر برد، سرعت و هدایت مرتبط می‌داند.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20856" target="_blank">📅 20:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20855">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8C4g_D4BR9sWasZHL7fXQsQy_kX0CXoUXGeTbvcrP7FgaPkjtidF3oh3-p2sMvWuxNTLwAstbYRN8tl3i7WLctKUBOMVrqMx9ZrkOHJWhbF8g0rHCQeNjWDcJ4e08WAB-U3sVcQCx83Kw3OL9TQ16A4UgHbXUDpv9JcMbqIv9vBbfvNXSKjpLTzDl_VxMhJxfz0J09oBbXPWzSlq-Al7oiOnuwl1Cq2MlsmfCAYdDBvnfWSO98glp1m1f9EghA1HLQmo5O0c1hl52C7p20Nfw-4IHaRTaQOo0Ot4-ky-3MyR66dCLik59PrdgNLPWPyTU0K0TfZAtI7JHIyJSoCDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
نشریه شماره چهاردهم منتشر شد
📌
در این شماره می‌خوانیم:
✔️
طلا؛ دارایی‌ با بازدهی پایدار بالاتر از تورم
✔️
واگرایی میان فدرال رزرو با خزانه داری
✔️
وضعیت رشد تورمی در اقتصاد آمریکا
✔️
چرا طلا یک دارایی راهبردی محسوب می‌شود؟
✔️
و...
🔗
نسخه PDF ویژه دسکتاپ
🔗
نسخه PDF ویژه موبایل</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20855" target="_blank">📅 18:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20854">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجار در بندر ینبع عربستان</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20854" target="_blank">📅 14:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20853">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هم میهن:  ترکیه به جای دلار گاز، غذا و دارو می‌دهد همتی به استانبول رفت  منصور بیطرف/ روزنامه‌نگار و تحلیلگر اقتصاد  دو روز پس از آنکه مهمت شیمشک ، وزیر دارایی ترکیه اعلام کرد که آن کشور - منظور ترکیه - پول گاز وارداتی از ایران را مستقیم پرداخت نکرده و بر…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20853" target="_blank">📅 14:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20852">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هم میهن:
ترکیه به جای دلار گاز، غذا و دارو می‌دهد
همتی به استانبول رفت
منصور بیطرف/ روزنامه‌نگار و تحلیلگر اقتصاد
دو روز پس از آنکه مهمت شیمشک ، وزیر دارایی ترکیه اعلام کرد که آن کشور - منظور ترکیه - پول گاز وارداتی از ایران را مستقیم پرداخت نکرده و بر اساس سازوکار توافق‌شده با آمریکا عمل می‌کند ، عبدالناصر همتی ، رییس کل بانک مرکزی ایران وارد استانبول شد
به گفته شیمشک، مبالغ مربوط به خرید گاز ایران در یک حساب به‌شدت تحت نظارت و تنظیم‌شده نگهداری می‌شود و ایران فقط می‌تواند از این منابع برای خرید اقلام مجاز در چارچوب رژیم تحریم‌ها، از جمله مواد غذایی، دارو و کالاهای مشابه استفاده کند.
سخنان شیمشک فقط درباره پول گاز نیست. این اظهارات نشان می‌دهد که ترکیه در دوره فشار حداکثری جدید آمریکا فعلا حاضر نیست برای حفظ تجارت با ایران، ریسک قرار گرفتن نظام بانکی خود در معرض تحریم‌های ثانویه را بپذیرد</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20852" target="_blank">📅 14:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20851">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJ8pYzsWtyrhE8FwsYC1lZ1n5ax8p-Z8FxeUMkcuN4pTkdqI_JrMvSWDs5d_dGNoJNo2hvb5mjN6ImqFsePEMCbWEyCg5LRkIEXASyf6ezh6LuRRzSge4E-0VlfsHG0W8fyM_Ev-SPL05mRcq5Np1v5bUaqb4QBJa7pJlHOvo89uvjd0LEFsdBXl9cA-_TqIBhkcX8FmD9YbjOH5C11JEbLlzLP3hkXhQ68izCcoY1nsPZUZ-sZk3acHWZz2hpoqvW36JBXkEtLgmGifQesk51PyfSyP0zKbZVko6YKbXFfLica7-uDr29ech8csqrSGYqR93bB2shQY4AB3wpwq3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشیال تایمز:
حوثی ها با هوش مصنوعی آنتروپیک موشک بالستیک ساخته اند!</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20851" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
