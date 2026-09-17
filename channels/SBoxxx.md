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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 03:29:40</div>
<hr>

<div class="tg-post" id="msg-20946">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMaBdz-BRH8OLUnQB1WVu3ePcFmCYRh0ErlqSo7I9wXGo8wI9p1yFaM5Psxuxtb9cjr_gUJUzPbFr_Q7mSQ9g7lByHptOLVrCNvGq-tbn9OnWTihWAP1uSVJEWWHXKErFDxJ4biubVvsHPXRMe3IgUYTs7mINQgC16kNY3FWYV7CIo2qPQxmoO2eLLnoxYwt12F6aFYJTtqrVNKBUcnCUxS9i0k-jW8aEamEEJm_PemDOEqZnUjLYbnYHy4HbtWdWjw7kFHcm1ANr0NDchni-Aaqw4ZHCtvxBCtnEObHMvRsSjYgS8CWyZtqCoM8H2yt-WvImLGsnWUuzKG6U5I3Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین توییت برگ افکن دکتر قالیباف</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SBoxxx/20946" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20945">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شروع شد:  اخبار فوری: کاخ سفید افزایش نرخ بهره فدرال را «مایه تاسف» خواند</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/20945" target="_blank">📅 00:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20944">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/20944" target="_blank">📅 23:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20943">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCrXN-2ZUznAAlWZKI9kJD9dgzjmR-X3dqUWR4NXDNmhB2Sk0jciOl9FmiZasPDYqTUBkmcDql2_bazC7py7myXQkASor9sxee-87-GQ2M3SfjUzFLusNCM5CM2gIiQIiur90H13Zd3q37UTqr8oHMzu9yDqRgDHz8d5XGkzsquRmjGIaTlmSptnXSMelxsC3MEvy-9kDbot39wMj7bb8xoJcbwNuPv3MDwwzzzBc5lrBEh-cJwwl0TT8sIXw1-WBPalIALKlbPCA13Z3LkGr9MnghcJtxLH2cQYLe0LREgFm83pOqPov1jPDGFIh0IICKniDHuOdTv59Rj04qmYyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پوزیشن دیشب برای همراهان ما ارسال شده بود.</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/20943" target="_blank">📅 23:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20941">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/20941" target="_blank">📅 23:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20940">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqAjCtZMmwIlkOYaCs5cFlsARRaXiMZ8hVB2mWLGuIdNRLbiitBxQ6WzsaVy0TZgK6Oz1mFR-Sn16HOdsgT6990kDFr9UlsFKoX_w7VBbVvvZ1amzqWwcojOOgJMw1ZP80mB3BiSNR4jXHSrcwmFjVOGjc6MSbR7mAUiatK6xOvLYOjEjtSSmMoWgkaTyp_8gTgP7tEK8hqsnnZTAFeL7wMbPU1Q2FULS0W3iwCUq6OYL0MhVf4mA0EH_KolcURDEgCxcXpaLW6pbVeiwi6ssz2AvVhZEEJe8GqmVWGELs3CTNAJH7dy4wxga0IrVONyqBXQBt1wzkgerwKKyPUh7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/20940" target="_blank">📅 23:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20939">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/20939" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20938">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/20938" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20937">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شبکه کان عبری:
مقامات عربستانی به نتانیاهو اعلام کرده‌اند که اگر اسرائیل جلوی پیروزی یمنی‌ها را بگیرد عربستان سریعا با اسرائیل روابط خود را به طور رسمی عادی‌سازی خواهد کرد/کویت نیز بعد از حملات ایران همین قصد را دارد/اردوغان نیز با محکوم کردن یمن پروازهای ایران به ترکیه را لغو کرده است</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/20937" target="_blank">📅 22:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20936">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/20936" target="_blank">📅 22:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20935">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/20935" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20934">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFIQtACTg4hryQDAU8OP0VXT0LXNJLmmjKA4rpdYCXpPQ2TSqJJvBz2yFAULL-1LYoW-DNBnz41uMd6OA3SQB8W6Vjry123LdrXkOdnjcYFnN8wFIcY1eeskWsowSch64oijLzeS7ELTkNcPvtE4EOTr4OYnwXpenh8uenotnxEW5zZmm1SCuwrcXlBoyk6thTq1S5dGVS1yHYz2FIYJ35IGDiqKaBHDnyU0fbNH_CN94Lr57E7snZZKVi2ZmCjB37dFEu8dEjzA5OXP72rL29yi5BymXN9iCuzsoHLoKVj3eA3viXK2bDwVb5DXUHwH1CepJpmwUdy3wiTcw-Zftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/20934" target="_blank">📅 22:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20933">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGOkeQ7seQZ32kIy1k307wgHLQVnSUG5EkXG-0oBI7OtNWSdPVaMtO91Da6QREzvlmC_I0qVjsafJIicI_jlkZB0T8kc1Bgvw9dn1M4vGKRWkEGjzAdde02WymsEcNy7zN8YBFpe5QsGfhovV9VUPCmAVXn2waj9Y4QaxOgtR9L3L2TNh4fVIwGeaSxA2gTciV8eRNOmmAdmruRRsf8k46_8Npy83hbaqigKzAktbT9LbbysT4MhQIr9g6zjVvD3kFbjFBr4HefvHJpbLRU_AMpdHuTsH7Mkfps_rhBxFfcpt_s76RvqCtDknRX8J3Ki313umvyejvzxxIvlNLTpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20933" target="_blank">📅 21:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20932">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0hqF-WVy2_-CTOjLpwnW03JDRn3ob3RXPESfp70K_pz-17H9-pPlUypLaZGHdp5-BiQx5bwUc_l7mKERAgJaiT8TwB1hLHK5z8UPP9cXtwlKDdWcTwhx9MSalTk_EZ8KUJJAl72ZxcY4NE0lWwVy6iGferS6UdAh2BDT-qDz9U3e-ftOhSZdFDnkhL2m63ad-1cbZp4Y2LBYNlQYOoRVDw0MNhndMHNY8zm9V8OJsxzAw_ltBRg3FIdfJdbWBkjDyWt79uzncmxwCOcv6aF408w_1WLvHBe2hoANk-e9m9w2H1CjwenGSW1FncCITTUr-twGexpxZXS4VrS4wzlHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20932" target="_blank">📅 20:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20931">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=l2v-gJPrMw9cQ9pYHMwq2fsTGpEQ0PHBnGxkdkkeQ86vCbBTox5TchO7s8hEERbK1cwj5fqm8gwvGwDjBfYUl0KVXWLxmBMJmIh4E0ahmQvlBa86WEgw5Oaq9T3pdk6ySj2lyFbTcoVtZ5d_-mE2KZ8WVxN_AuIrsQ4gIsqPJtvk2-snHNcSLILrSFAZehZZZ4hWUTDaxpoZ0JfXlpsXj7d6EvCNEBxbh6CXPmQ-mfmV3_o4Tochor0o3Gbt7-cvhouKJyLqfgbQt9HR4v7X8lImXbjQ6Uahv9U-xRVF63nk4b-n2JI5zINRNZVOWYrHshILrafIqTodIu5JZdtxEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=l2v-gJPrMw9cQ9pYHMwq2fsTGpEQ0PHBnGxkdkkeQ86vCbBTox5TchO7s8hEERbK1cwj5fqm8gwvGwDjBfYUl0KVXWLxmBMJmIh4E0ahmQvlBa86WEgw5Oaq9T3pdk6ySj2lyFbTcoVtZ5d_-mE2KZ8WVxN_AuIrsQ4gIsqPJtvk2-snHNcSLILrSFAZehZZZ4hWUTDaxpoZ0JfXlpsXj7d6EvCNEBxbh6CXPmQ-mfmV3_o4Tochor0o3Gbt7-cvhouKJyLqfgbQt9HR4v7X8lImXbjQ6Uahv9U-xRVF63nk4b-n2JI5zINRNZVOWYrHshILrafIqTodIu5JZdtxEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایید شد</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20931" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20930">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZyzU7hzl6CvUfdFjXEeDnWrsHXXKbXlDiezHU2wNGXDtZYnPezxK8ij2xbwqBeItXYAQc32VgOUM0P930ysUcESCX2PPs8asrrz7bF0l0TW1j-Xw0RoGkpuU5xAmhPPRn03sojC5du-Xsnkql-jUEwdqwgWar1IW-H-0is114PELgUP_aGORCr0YWBxCpQM6PURGhs5VavaFTvoPXFq52fin_UtkYWriuQUZYB5QhKvAEiEVOieWXGbXyfa1u04bRnFnhfNOaD0rOHoyZwS9P-fVg0SK_cOsihHTiahTJR3YQIpSfOwbfGDrAF1X3n3raG-nYNgs6mhRlXkFSi8sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20930" target="_blank">📅 17:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20929">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VevfXrQs0WNygxejkG-kOKdRTt6fyY6GHkWQV0e1DmVhu_21zTJzceW2mpWwkBD8CTHDTnvfVuWy4ycrx739DJX9gpEp0SHY-nl6SSPdXRHAKF6UJ3SMYtlEFz05zhAhjRShqcQuLJ63miesfNbzFaxMmKmNCt7DEyRu6ORLk4SJ7M1f2lH8bow6Yi3x7Hqt5a-jejl14JUIBovF7i1k7hBYqe5jiBhS7BpaX4LaiJiCwN9mRNKhixIHM1CD9DWZP7FoolQqZtjQJTc5zZEpv1YE5_bzckYdoIfaZe0CSGrR_pldxX3cgmjpSLv597vtTKp_Gy_9IL3jdpMm2uJW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20929" target="_blank">📅 11:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20928">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQKuuc-KCzcnrOT75v4mvgKN0t2QraSHIYL3hPDA-Q5TVADvV1TBKTb2qKk2hrRfPRnUoSJDzdPO-QY0ECHzSjQ-DTKQNCtKIgipCYNavJLUsdk5guWv-P2yJB7LID911tGReq9mkM8RyK2CS46NO3OQLpWvcPagPJhGnYQGbmyDYb42SX9SCOS7KnCCF7ONAnmgxtlmp5FkIRvxydVq1Vf_6b41mlfEmcwR4a3D4tksMYJvcWZBZdZdplQ88jIl9CSZarJkveMUT-e3-Rq5T7izD51bcphFGAk8Lp1_kbzMK7DoN92jhYLHYnmOTZVmZcNohGZoaw64hc3h664FyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20928" target="_blank">📅 10:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20927">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=ii3gLb6kqaV1-t1TP3U0d5tuIn6dSml_VGGRHaR7t3_ftTO3_4bjTTIkCuQhBXobE-H-785HDehdbCaPqJuDpkTMtg50JjUy56Fv1ShV3LcSbRBCkukuujzdKL1hXjQNjS43K_kUupvsNNWgJ3ZOhEuIxESWorEC1P0QmZEAwced8ZlW2aYYJnt4Dx0T-QSX1HYgyfgM07OzHMqEh1Und3GzjKgq7HKcmLJtCi-4pwzzpGXYGXB7ERncXsw25A0XokNyPf0DAYli-joRFdN747G1z9x_JjnoeJLiXRq49_iy81TeT-EANa3u6AonJWTuOAAEf7H3XDwZ1lxKCD6yfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=ii3gLb6kqaV1-t1TP3U0d5tuIn6dSml_VGGRHaR7t3_ftTO3_4bjTTIkCuQhBXobE-H-785HDehdbCaPqJuDpkTMtg50JjUy56Fv1ShV3LcSbRBCkukuujzdKL1hXjQNjS43K_kUupvsNNWgJ3ZOhEuIxESWorEC1P0QmZEAwced8ZlW2aYYJnt4Dx0T-QSX1HYgyfgM07OzHMqEh1Und3GzjKgq7HKcmLJtCi-4pwzzpGXYGXB7ERncXsw25A0XokNyPf0DAYli-joRFdN747G1z9x_JjnoeJLiXRq49_iy81TeT-EANa3u6AonJWTuOAAEf7H3XDwZ1lxKCD6yfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20927" target="_blank">📅 09:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20926">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20926" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20925">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20925" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20924">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJyF5-Qat7q6CfFuDDkk4TqicM1rZAjMpr8AR9fz5PyLoiLG-DkKz9HB2Ndp8NzVP_Ba8XlWtnvPJCRucvQ4zoBL4rUd81odTu5hyohWxnIxKoJ8nvzbU9mY6bddEPGOzSOvPyO5kyMZ8Kj1OoFBghqzm9HJJDYS67RPHvjRucbOKpoVCLkiVB3EhNqYP6Ipwi6QSpqMn5yPo90GhIK2UXAtK0HPDc5ibW6kszEPL1DvrccCEjILpvQ3KJMWI_vFzFceOvADICRq1tRg_5By4UGq04s22KJpGnHGF-TeEgeU8DV118r8g-_SXNPgrqlF0mt2uOoX8clwO-Q55kdzbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتر گفته بودم در عصر اقتصاد دانش بنیان و هوش مصنوعی، تنگه بندی و راهزنی شاید در کوتاه مدت نتیجه بدهد اما در درازمدت نتیجه عکس خواهدداشت.  (به پست ریپلای شده که حدود ۲ سال پیش منتشر شده نگاه کنید)  اکنون این ویدیو را ببینید و دریابید که چطور بسته شدن باب…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20924" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20923">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuGRxjFhHOMtvjkYzRXGEfZKr8HffOAMvTA5bv-RFgxjrLNkRtnkpj3hawMnGBmn5TjWIacLYK9bw3v-o4-5tQ97ChwBn_NAJz4P99KZxb1lu_d9oYyZ0UsicG8MClgDpNVanBRjro3UuxKfLudGgRLEJi45EO-StB9lUDOs91QKVKv8C9FVyNYX-H15hw5iWw227a4QWOI8IhFYWWzeyZ3us6_gNQIn4Y2Sx2hlRuzsAIopCLjBYEeVptYpX8fhRr6m_-LD9tS64UWe2aLditIMbuG20yMpb2mScKRZ-YIUHlml4olgtwwEZw4LaZClcdzPPEpKUiFRErm9YenUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20923" target="_blank">📅 00:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20922">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sn8Au7_zvspl5szDrcEEk8kNlDwpiAuARlA2zWElVCh3Ibm4aYbqCv5bOa0sgmQV2kEovYXWXKFuKIRGtQblYBFRg3-2OBB53n3idzsmfSO7P1D7EiIhKbRJFh5RJw0W9ZZIEhdFSbFYfu_9CBNDcSBLxmt9AHWS8uPF5eEBWGriQhc0yJm1BwrzXdyajODHlTrEcMmuiuZwyAwg311Da76kq0ttQfp2YIvlHQEvsW7sfO1Y4VN2bSCSGAYsEyeAYWxN-sx4PURprUhLuRegzOHRSkXCh_wcb01pNJ4uc4SeOAZ-wYdjrF6CD9FsaWh4FLQNodVlDjfjc3vxk9iebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 27</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20922" target="_blank">📅 00:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20921">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCFXjgz7Q_5LllcSPOM57ZcQLTbkc5lKEIupYa2IVTfapg49GQgnY741VsxYv32Ba-CvT2YPsNx7V2ISA3hJ2-mJHcnpKhJgsopne3rZxm1kz0VY12b6SY6TuTFamzTNG5HfBZhQDHRl8ZihFRWeSaF7yBS_ucIEP8eY6IvHt4xSSZuJ1MDI7AK7UF4q-fFynDKzS0gNMbYJk8gCZC9VkLe7RcMIbsoABi4TrF7Ae3tDAHPt40E4ju-GVa3W_FDlEvM7aIRHjbaroQnsToTOvMHHuU2F-cYz9mDwNF_aDN1flA93HAZieF2jaIEOOAIKNiTgCzFttN4pV8sKFCdoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20921" target="_blank">📅 00:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20920">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20920" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20919">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20919" target="_blank">📅 21:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20918">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">عراقچی فردا به چین سفر می‌کند</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20918" target="_blank">📅 19:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20917">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آکسیوس:
یک پهپاد آمریکایی پس از تلاش سپاه پاسداران برای توقیف یک پهپاد نیروی دریایی آمریکا، دو قایق کوچک ایرانی را در تنگه هرمز منهدم کرد و اکثر سرنشینان آن را کشت</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20917" target="_blank">📅 18:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20916">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20916" target="_blank">📅 18:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20915">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20915" target="_blank">📅 18:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20914">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20914" target="_blank">📅 16:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20913">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20913" target="_blank">📅 16:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20912">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byiSlGQHZtaYnQ0gIM0DidmKkj1pzo3ALAfeLo-7d9WF6cUMUSWmIDBxXoYLDhhyq8M1jfxZt4jlyKTMPN1drPdfYTMmvpZka-p4Ipd4REuylQj9SOOfoR0FVBm5lcJpxrpaGfspiFXoJrlxxO036O0IHeffqZahzLb8L64GJOzVGlu9NnaN2P_fgBgZn9puxUSkPRQguFr3dEUlI8zoU0fLAMlJnx7aq9V-quK2Uu_nr-j5icwIQw69UYelEHWnVLvoxELx9NWX8YxvkXJOILfTVxKAbdO1GjFX_K6e9j9N8e2MM-7uj1s_BzNlRMrlRcCLXx5ymZvBeGcH3XATvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سخنگوی پویش جانفدا :  جان فدایان غیور صرفا برای اهداف نظامی به کارگیری نخواهند شد ، به زودی پیام های جدیدی را به این عزیزان تقدیم خواهیم کرد</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20912" target="_blank">📅 16:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20911">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20911" target="_blank">📅 16:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20910">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20910" target="_blank">📅 16:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20909">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به نظرم بین اسراییل و ترکیه و پاکستان یک تورنمنت سه جانبه بگذارند ببینند کی می‌تواند برنده شده و بیشتر گاو شیرده حجاز و نجد را بدوشد!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20909" target="_blank">📅 16:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20908">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رسانه عبری والا به نقل از منابع:   تماس‌هایی میان عربستان و اسرائیل با میانجی‌گری فرمانده سنتکام انجام شده تا از طریق ارائه اطلاعات، به سعودی‌ها در دفاع از خود در برابر انصارالله کمک کنند</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20908" target="_blank">📅 16:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20907">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20907" target="_blank">📅 16:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20906">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">در سوریه با گران شدن سوخت، اعتراضات مردمی آغاز شده و آشوب ایجاد شده</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20906" target="_blank">📅 15:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20905">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20905" target="_blank">📅 13:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20904">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20904" target="_blank">📅 12:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20903">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20903" target="_blank">📅 12:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20902">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C30JcfRe_P_NNeADhUaJd2Q-9DYWBOSe7eNAZZ0FX_LtTUjJVi9RqGQufCJphuc_qAUOq957g2oZLe3j3nuhN_qHMoLdLmDwB6VRdAz3nGSukYls_BOKLleeJoS1fBw2fPFJXuzX8vUdHQTgP0C1WNl_N-mXKpS4jIeUHenD8Rh6dT0vR-k097XPhxFxGtODwxQ8OLnIJeA6uu0JTwjz9TnbLtGRbBvvgWjsfJzUDoykhnH1qjC-FfB0jUiO2GTrOZNp0JoCNGUBMHIpfnCFbXAQX8VNH9vhWP21xReJF7Se9IXTWXjl0fqkrIIO-azDEIea_lKm8uqhiqoYvVnijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20902" target="_blank">📅 12:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20901">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZ_bqfAEdQzsM1DoJeTMcbjEh7l7WpKN9tCT4a8pVOsrKCLF2LOKaFN0c1lP0OWlsFSeUcX-LSfJQhrEQ5C-90ypm912icgzFsdg_YBIG_8M4Hsg_19D4zH8NfcWhChjRtkqU7Bjt3BVbCL-qXFNE5_u4lNdubwfMgwS2RfozGk4Ltd9uzGl3pNaxLnS1Sd2FMfasxKLKCDCcd23fGJj90-j_fUQUfGkunQBHikBQXefC4KwmClMpYKRDRrq1chMqjqh_9aLB0kwEEubXRPRIO9mi4f6t_YrzNbJCFg61vg52uwX1TiZyET65FPxyPTsh8n8v1s3gAK303Xn9aebtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال: کمک ماهواره‌ای چین به ایران  به گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی می‌گویند ایران پیش و پس از حمله موشکی ۱۷ ژوئیه به پایگاه «موافق‌السلطی» در اردن، از تصاویر ماهواره‌ای با وضوح بالا از منابع چینی استفاده کرده است.  در این حمله…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20901" target="_blank">📅 11:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20900">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_-0jPcrKpCHgeVZonpZRFo1-fw9R7AUWNJVGZLmdDrVE1mElerE5ve2WFiYp656hwil6-j-3jkOfQ7hRMoX8FHor2tkArXJlQaLYQl-e6gaevnSy17BicTTdMRMm2Q15XVc37XUDFgahC334ty-wLmSrHh4OmIWCKHS1GWt-fXUOxJCazOPA69WD7zcAVcsk4qQpO9zACE5kLdpnmR52-iF6F_T4XuHMluDg5KfoCg0XsKrSmlt2lLmqWGUjj0uY7xlq2Q1TIkzalCP6vTVGPV3_x15MRIm35q1CX_XRAJwLScHGZd1zcHgsixPN1rFRMhQk-2RUE82CpsNZbrxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20900" target="_blank">📅 11:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20899">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCnLrImiUJesJpZB2iwDr1nyLAidokrSMkIX1ldnI0oGI6hqSPw6QezFUpVfUiSdTlgy_sD2KW7_sgWOtVcpxglMCAM190mpeC8qvvCHloMY_YCkbeQJ8Hx0u49exm0NOhWEc-Vzwun0OAdNaG0BRKvqmSZhP2PLPJsSKPO9e09UotdRzx41uFaKT1UUiRuAKNXBBy-7noXDyPGXBCaMx-Z4QyZAKlMfrzot0DphGukGURmNSKeB-x-VbFLvucKhuUlmXzxyQb9vLfU9Yf122ueBo45H2Ue5nQDMtvl9GMkWWusgZ04uH7PSRBx0nTMF1z2zMI_yaLkrjHMsm-5YJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.
بهترین محدوده خرید از 4280 تا 4250 می باشد.
نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم و پیش بینی میکنم این هفته طلا سطح 4400 دلار را پس بگیرد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20899" target="_blank">📅 11:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20898">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC28jwqHmh9hikNB-t90el-yM5wxjDk52lv2eBtJ8XWOO2GPQkU64ueB6UyorwpdiIs9OODOOAY6ZQSt0JXziGVvx_dbiz13WSmlH89LQtQCZBMkfAapGpTiCqmzGMjPQcSZYkwA1PoOSJ5ScXYcc9Xks9fVwW3KE0IBRfL0FXEllPcf-hL_SWbHwX57hCQ-O1EUokwZ74L_frCt9LiXskH1Foj1xwNiE0l-hszg2LcMB0PKphYh3tEfIUoHW8GnU1E8U87XProt88dhHx-axJ5HycKTRAEBG4nLmElphC64M-CFqGhUbiRhaQm7CO7Y6hCnJ0wxNcd6KM5tyqf5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح نسبتاً بالایی است و احتمال فراوان هر بالایی فراتر از 4300 فروخته خواهدشد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20898" target="_blank">📅 11:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20897">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV3yUoToZZ7xxpdclzLC5B6DYclqcCaLJkLDiEXKy9sB-tS6rG9Wc6RwczzBBSWmyHTFyEgB0JfsyfcQ7wUYGoka4-U1QB2oMhJm4oSv7ruaZvZ4m_ECUjxObyfV1nL0VlUrQfGWGjOuaMHvkhZxNVYw5a0XZgJCwLShrdyrQENymR7BR6VGb4__J_gG1u8ZLtVIU5YszMVR_Uxaeni9h9rHb7qx5hJo-SSzwW83dNwuVqKIUmLWpH0XB4IW03n3SE10pD-oCwy-hG88lJ-BfY2-j3d1uSeWMoJOt-v4n_l_r4dQd1n15of4xrmRkn4cfIurB6ZMYrpw6PWXie0jcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله حوثی ها به عمق خاک عربستان در ۱۱۸۰ کیلومتری مرزهای یمن!
و کماکان از متحدین پیمان مکه (عثمانی و فاکستان) خبری نیست!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20897" target="_blank">📅 09:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20896">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جمعی از نمایندگان مجلس در بیانیه‌ای خواستار تجدید نظر عضویت ایران در NPT شدند</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20896" target="_blank">📅 09:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20895">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">درخواست کمک عربستان از انگلیس برای حمله به یمن
بعد از مخالفت آمریکا با حملۀ به یمن،‌ عربستان سعودی این‌بار از انگلیس خواست که در این کشور مداخله نظامی انجام دهد.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20895" target="_blank">📅 09:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20894">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یک بار از یکی پرسیدند تا حالا اتوبوس هل داده ای؟
گفت نه ولی یک بار تو اتوبوس هل شدیم دادیم!</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/20894" target="_blank">📅 01:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20892">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آن‌قدر به ما گفتند ترامپ تاجر است که قبل از جنگ به آمریکا پیشنهاد همکاری ۵۰۰ میلیارد دلاری دادیم!
- حسن قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20892" target="_blank">📅 01:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20891">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8MN23zIQH8AOARlXJA_SA_dgLi9nm13YSFCUdZPsU6Mq45rTlomKZlV_862bVetmoCc-SjwQh1OyhB0yvHX7NAZuDNQaLria8OqZp7Jnpa0B0uFp9keUsw6oy7HmuiteaG1NxyijZ7VrN-ZeN9ItMWEahiNZqa4HmaiABA5nEHCmQsJ75Ypz5NfXPcVd6kYO8glESNAMHBWvsU3ss0jKBu63GZdH-Zk3cehkejgt8Gss3K_95Jb_OYx7A64eOLokpmBJBGe3KGia9qcF80dyvRW4ns3LCrBEsIiAZKXx_damZwEjkoTV1MQYCsa2N05qJ8YZiloMee99iavFcnmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
💙
😀
💙
😀</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20891" target="_blank">📅 00:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20890">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">برنامه ریزی آمریکا و عربستان برای حمله به مواضع تازه تصرف شده ارتش یمن در ساحل غربی
یک منبع یمنی وابسته به مزدوران سعودی اعلام کرد آمریکایی‌ها به عربستان سعودی در مورد مناطقی که مزدوران عربستان آن‌ها را از دست دادند و مشرف به باب‌المندب هستند، فشار می‌آورد تا این مناطق را پس بگیرند
در پی این فشارها عربستان سعودی با کمک نظامیان آمریکایی در حال طرح ریزی حمله ای به مناطق تازه آزاد شده ساحل غربی با نیروهای سلفی و سایر مزدوران است
این منبع اشاره کرد طبق دستور آمریکایی ها به بن سلمان این حمله بزودی آغاز می‌شود.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20890" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20889">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پزشکیان:
برخی کشورها در خفا به ما می‌گویند ما با شما هستیم اما در عمل از آمریکا حساب می‌برند و جرئت همراهی با ما را ندارند</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20889" target="_blank">📅 22:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20888">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پزشکیان:
آمریکا چون نمی‌تواند رهبر ما را پیدا کند درباره سلامتی ایشان شایعه می‌سازد</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20888" target="_blank">📅 22:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20887">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.  سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20887" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20886">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.
سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه مانده و این نفتکش اکنون کاملاً در آتش می‌سوزد.
آن‌ها تأکید کردند که تنگه هرمز همچنان بسته و «تحت کنترل هوشمند» آن‌ها قرار دارد.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20886" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20885">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گاردین: طبق گزارش ها نخست وزیر بریتانیا در حال بررسی اعزام ناو های جنگی برای حمله به حوثی ها در کمک به عربستان سعودی می‌باشد</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20885" target="_blank">📅 22:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20884">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">روسیه و اوکراین دارند با پیشنهاد ترامپ برای تعهد به نزدن تاسیسات انرژی یکدیگر موافقت می‌کنند</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20884" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20883">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20883" target="_blank">📅 19:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20882">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ادعای ترامپ:   ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.  من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20882" target="_blank">📅 19:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20881">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ادعای ترامپ:
ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.
من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20881" target="_blank">📅 19:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20880">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20880" target="_blank">📅 19:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20879">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اینها تغییرات بسیار بزرگی هستند اگر خوب دقت کنید.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20879" target="_blank">📅 17:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20878">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20878" target="_blank">📅 17:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20877">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3zXIj6P6vJb82wRC9FXZT1uIIm93WjPJ1NZyqK3-6aUOSGzNUX6ZTXJTOeIcnnVHlZstabAtwEStyRQquMFVKeXGC2gH45Iuq7hHimQ2wecv3UnF1qL6ZM7XfE6RLn9G3YQMlGxUxiggwZcto_i429Bask8fmLzeBNgBBYGt_NQJBSiebPCzsaRFqKaEdRCr1pqCgnf-oRPqaemv0Bt3mSnxARel-WuwflRQ9pELcu8Ty3w_FgJFzmVzXuW9DRmolZ2aUdrgkvdAUifioZFnk9ftY43Mxql4JyGM5QHmr_SgRYAFhUflbDI6R63pikAor8UsCwxpIxu2aLc91wgGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی احتمالی دموکرات ها در انتخابات میان دوره ای نوامبر عملا مبتنی بر یک سنت تاریخی است که در دهه های گذشته بارها و بارها تکرار شده است</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20877" target="_blank">📅 17:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20876">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3Bb-GjFFourb0bDK9uUToUe_b1vwPAu_gGg6U2__PLKGI0r3koSOsxxPfzk8TwnEyYu0Qpe0J3239JJHqbh7Ri8Kf-mHnhS2nwuXS6r3UjrKjHUcQuzJs78FWZVNCJiIGT8RPPIUJaza0ahmZ4TiWOxkveVugAHF3S4UGabufE1274uY2eEj1ME-wE0UpQqCmiuoTqozWjQbwd2pYhBUNBpam48ux0LcSVSBjDzaHwSqfnv5fK5Fp3SduZzTeAI5gVNZvR4JsZ24uuUfdo-A_YiuWjPo8CwV68jlR-0a6sZzk-UMmhZSYsK7xngiDWHgTx7GGV0M2JS9354AXFlzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20876" target="_blank">📅 13:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20875">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20875" target="_blank">📅 13:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20874">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNHgvhL_DDxtDyP5CDY6PJGNdxbKlgu2k8mfNunXa0dhOaG4StICQRitmAeuvz86hCkXJ62HI7U-n3kymWdX2_y_ZJM1jz-tUOY7wRBZol1dLiCM4qfNzceRZm76DGpY9CkkVJyJjRKKEfnoVtCo713N67BH_hpcE9C_qY-Ln9nKhJRfvtoK3-Aqf_eRvEfBsKo9KHB7NJDxG0VMQa7sc0ja3IxVYfOoXNWmpK48k-i7vZG-uv0eG-ScH90U6nhoxDnf7dy54K6RlkXhAVdtb-q6WY_s8K_THBfnU56VUGwDln2cGGZijHdJ92_TOwjl1o6ghOmrMoWpcqy-arQkrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20874" target="_blank">📅 13:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20873">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یک آوانس برای براکصه در آستانه سفر رهبر چین به آمریکا</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20873" target="_blank">📅 11:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20872">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atH1QurJvEW6iBIOi_SjHEB3pTCakSt47SNTAhNAmg6OXQPbJkQgpb_h65CsiLWxjF5oZ63Mik3kdpw3_XEdM2asd80abuRC19HZ04d7O1u7zapEsgZeyzmRUSFwokzWXMR6Yg7U121F3-jsYQuEDfO4D2QxNTYOzggIxM6ycY9swpeEeMzaDwopuUI2FtKntk7ILELoaMokT6RKso0tKrjuEUhfmfQfOzMGtFCOFwdz2o7En7Xjk_wBooAJ8vJ0_g-y8yNmBZwEiJQOl1AwZp70-0ea6cat6FUTDDGxIi1grGIEtlwrSu3p-Q1PwOKITxg7hbL4Jv0FZI2yvJF2Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20872" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20871">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1u4SdyeYgo2xk2YulhTsk8W97fCKW_wO79ULbtGADhG8yABjJlnPAEBEmgFPscktxy-8gUvMsc22riQuKn_P6VdIeYdAlRzyZkmTxJFzB5agk140apRWRTD4tdoD3FVWZ4UzBxCoCrozxfx1I4K7rUTYKDt4AL6AMNarGaQCg2H0HM1TZ8xAEfCz3-80BRfT1cfn4Nv08QyZSqVaCXHL4SJofAhuZCyF49ypS2U3F3v2ep4p4E-fjQNv5f9flWms4r5h2WxizUEyusKp79NtI8D7aClcpkVZ2iVq_kmUop1aOPvHbyN-8c1Mrf2gHbF4OAJirHd6uycbr3URRa3gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای است و نظر به ریزش طلا تا الان، انتظار یک اصلاح صعودی می رود.
دقت کنید که رشد طلا «اصلاحی» قید شده.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20871" target="_blank">📅 11:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20870">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20870" target="_blank">📅 11:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20869">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20869" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20868">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!
محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20868" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20867">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLDzYuNgFE6tqbAli7nxarvDduJph6uUxY0KjgzCDvKYKe3yji5qa0R-PA0GGrdtGyAr7vn_I4FQwWKZaCuFtClJ_KyYVsmjMutK2P3Vsjr8W9uCpKZnykr6XVhn3v-t3EWhRD60G71zliSBoxxspkw_rN8mAga43GSF69h2-FMvAdHRtl62M41wIjmaR4m-ivRLxxJ3QPhqVRVz6oVQ_940cQjoIi-6NiW8ys2dw-a0_ezE20TSGQwoQtyDC2cXY0Dukkol1uAspUUbGivTSJpw3Yt64xyrmv5eu7Xzm_9EY6D8bZfdfmeq5lfZLMAz3tLHBXYhHmxap19IPW9A4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت تحلیلی | سناریوی اختلال کامل در مسیرهای صادرات نفت عربستان
یک سناریوی حداکثری برای بازار نفت، تخریب خط لوله شرق–غرب عربستان، بسته‌شدن تنگه هرمز و هم‌زمان بسته‌شدن باب‌المندب را در نظر می‌گیرد. اگر هر سه اتفاق به‌طور هم‌زمان و برای مدت معناداری رخ دهد، بازار جهانی نفت با یکی از شدیدترین شوک‌های عرضه در دهه‌های اخیر مواجه خواهد شد.
اهمیت خط لوله شرق–غرب در این است که به عربستان اجازه می‌دهد بخشی از نفت تولیدشده در شرق کشور را بدون عبور از هرمز به بندر ینبع در دریای سرخ منتقل کند. ظرفیت این خط حدود ۷ میلیون بشکه در روز است. در شرایط عادی، صادرات نفت عربستان حدود ۶ تا ۷ میلیون بشکه در روز است؛ بنابراین از کار افتادن این مسیر، وابستگی عربستان به مسیرهای دریایی خلیج فارس را به‌شدت افزایش می‌دهد.
اما اگر هرمز نیز بسته شود و خروجی دریای سرخ از طریق باب‌المندب هم امکان‌پذیر نباشد، تقریباً تمام مسیرهای اصلی صادرات نفت عربستان مسدود خواهند شد. در چنین شرایطی، ظرفیت قابل استفاده برای صادرات نفت خام جدید می‌تواند به حدود صفر تا ۱۰ درصد ظرفیت عادی سقوط کند. البته این رقم یک برآورد سناریویی است، نه پیش‌بینی قطعی.
اثر اولیه چنین اتفاقی احتمالاً در بازار نفت بسیار شدید خواهد بود. بازار نه‌تنها کاهش فیزیکی عرضه را قیمت‌گذاری می‌کند، بلکه «ریسک عرضه» و احتمال تداوم اختلال را نیز در قیمت لحاظ خواهد کرد. بنابراین افزایش قیمت می‌تواند بسیار سریع‌تر از کاهش واقعی تولید رخ دهد. ساختار بازار نیز احتمالاً به سمت backwardation شدید حرکت می‌کند و پریمیوم نفت فیزیکی افزایش می‌یابد.
برندگان مستقیم این سناریو، تولیدکنندگان خارج از منطقه خلیج فارس هستند؛ به‌خصوص تولیدکنندگان آمریکای شمالی، کانادا و برخی تولیدکنندگان آمریکای لاتین. شرکت‌هایی مانند ExxonMobil، Chevron، ConocoPhillips، Canadian Natural Resources، Suncor، Cenovus، Petrobras و Occidental می‌توانند از افزایش قیمت جهانی نفت و کاهش وابستگی بازار به نفت خلیج فارس منتفع شوند.
در طرف مقابل، خود عربستان با یک تناقض استراتژیک مواجه می‌شود. افزایش شدید قیمت نفت از یک سو ارزش هر بشکه صادراتی را بالا می‌برد، اما اگر نفت فیزیکی امکان خروج از کشور نداشته باشد، افزایش قیمت نمی‌تواند به‌طور کامل زیان ناشی از کاهش حجم صادرات را جبران کند. فشار بر درآمدهای دولت، پروژه‌های Vision 2030، پیمانکاران و بانک‌های داخلی نیز در چنین شرایطی افزایش خواهد یافت.
اهمیت ناوگان نفتکش‌ها و مسیر SUMED نیز در چنین وضعیتی افزایش می‌یابد. در صورت بسته‌شدن مسیرهای سنتی، دسترسی به مسیرهای جایگزین و ظرفیت حمل‌ونقل دریایی می‌تواند به یک عامل استراتژیک تبدیل شود و نرخ حمل نفتکش‌های بزرگ، به‌ویژه VLCC و Suezmax، را به‌شدت تحت تأثیر قرار دهد.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20867" target="_blank">📅 10:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20866">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رقابت عظیمی میان ترکیه با اسرائیل برای ایجاد هژمونی در غرب آسیا شکل گرفته که بجز جنگ با ابزار دیگری حل نخواهدشد.  بزودی در قفقاز هم شاهد تحولاتی خواهیم بود که نقش و جایگاه کشورها را عوض خواهدکرد.   اسرائیل به شکل هوشمندانه ای از دهه ها سرکوب اقلیت های قومی…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20866" target="_blank">📅 10:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20865">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiOcsgj6sNPrxOxpoKJoy9gsGDu2xepIbW74tXLjSz54iYaYNG3PwntPzcIv_tbtl17SsVzTAA1gh6PMnczmKSqkZaPJDCCqdcnXQmOGar3gwWBVGm1InQNlY2b7lrbfI0c4CvsFcwynTBIHcOpokzkW4j93FzTRpkMPfatJV3OjoAwpckruzX1jEDvq4HxsnmBxj9o2jrx4OMp8EU5Vv5Zus4q1oV9EklyatHKI_9ADdRRGrNrfwYBk42uLp0Sx8kKFSG2qQw6S_sNHEiEHSYIya51CnfFvxjmz6Dr53EvPfym4fVCskmpQfkWMiwc_fEcCPKZagKjH_vFYMguMcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ نفتکش‌های VLCC به شدت افزایش یافته و در تمام مسیرهای اصلی به بالاترین حد خود رسیده است، زیرا جنگ ایران ترافیک تنگه هرمز را مسدود کرده و جریان جهانی نفت خام را مختل کرده است.
هزینه انتقال از خاورمیانه و خلیج فارس به چین به حدود ۱ میلیون دلار در روز رسیده است، در حالی که نرخ خلیج عمان و چین در یک ماه ۳۰۰ درصد افزایش یافته و به ۵۷۱۰۰۰ دلار در روز رسیده است.
این محدودیت فراتر از خلیج فارس در حال گسترش است. نرخ نفتکش‌های غرب آفریقا به ۴۱۱۰۰۰ دلار در روز رسیده است که در یک ماه ۲۸۰ درصد افزایش یافته است، زیرا سفرهای طولانی‌تر اقیانوس اطلس به آسیا کشتی‌ها را متوقف می‌کند.
موسسه لویدز می‌گوید که خرید مجدد نفت خام چین، ترانزیت‌های خطرناک تنگه هرمز و راهکارهای ناکارآمد فزاینده - که اکنون با تعطیلی خط لوله شرق-غرب عربستان سعودی بدتر شده است - عرضه نفتکش‌های موجود را بیشتر محدود می‌کند.
با توجه به اینکه حاشیه سود پالایش هنوز به طور غیرمعمولی بالاست، اجاره‌کنندگان تاکنون می‌توانند شوک حمل و نقل را تحمل کنند. دلالان می‌گویند هنوز "سقف مشخصی" وجود ندارد.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20865" target="_blank">📅 09:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20864">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2n8lojPIqdrEZbVCUmUe7AC9RDXm39ZzfGW0yCR7zeq4l6XEtsVlfDaS3ZlvWLSChJYP01a9iQoIrhWiuzZGyQSD3iyKzer2HXXH_tuYZZ9Qj2mC0-OAq4QFL5AEXlFk6Y_jevCfD6FlUZAZC1WYRsyywCvprGjgDgiYgGcJNiYh8_U7f9tIZ6pqEUx4JZYGao08RxzqpF4x3J_zolfbFiqSzKSwWMgaOX3dkBxN6HbVQN_VSYwDIC_nl7oi2LFQqV_ygJlVKN9uY6Yx9Z4hjDZo1dbh6_rmwMTPR-KZ9BWk5lA6F33vAxPXlYSn8tTHdCga1qs9NIcfPo8lpyKBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی ممکن است تا ۴ درصد از عرضه جهانی نفت را از دست بدهد اگر خط لوله شرق-غرب آن به سمت دریای سرخ در عرض چند روز
راه اندازی نشود
این خط لوله پیش از حمله پهپادها که منجر به توقف آن شد، حدود ۴ میلیون بشکه در روز به ینبع منتقل می‌کرد.
منابع صنعتی می‌گویند ینبع در حال حاضر فقط مقدار کافی نفت در انبار برای حفظ صادرات به مدت پنج تا هفت روز دارد.
این منبع زمان مورد نیاز برای تعمیرات را فاش نکرده است؛ برآوردهایی که رویترز به آن‌ها استناد کرده، از راه‌اندازی مجدد جزئی در زمان زودتر تا ۵ یا ۶ هفته طول می‌کشد.</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20864" target="_blank">📅 09:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20863">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N52cb5jY06Wg3MTYOaRdo3LMW01nlzzInYSkeBderW1DqAAH39qI-udiOsfdJ9ef9QqdsPikJBaqjch1vkTWhOa4Hf5v1h41wagkORAldeTvBsrSsxi5Vdkg8MXM8Kw00MvManlwRbszBePJMqDtsFJiFoTeyZ6aXk5aSSy6_aFKxYaQ0m926GhF0lYF1vgD0VkmUNsQ0NBadHoZnhoU5O18HEHSW3xi3IZXsoxm6PoP7WurjmBw_CQATKhb7BxRsyFxI6j-9--T1M-J0aR9_yWkxnUNHT-jkoLJn8BnPJkZreuMWq1EEL2jNz7dsP3lg0tEdXbVwfQFtm9vd744kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه عمان پرچم  شیر خورشید ایران رو گذاشت
😁
@Piknikanalyst</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20863" target="_blank">📅 00:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20862">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نشست فردای ایران، عمان و کشورهای عربی سر تنگه هرمز فعلا لغو شد</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/20862" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20861">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شلیک موشک از ایران به سمت تنگه هرمز</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20861" target="_blank">📅 23:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20860">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KL4T077SMKQOnkoyUxnlm8fLDe7bOqJPQDJlRmO_B_7_2dsV-pRIrYAkfN1rgO-zqLwlCbD9yTxVWczI8HUv6jfaMuleZKF7nCa8ffdVkrc5C_ZFvDiP7Sr6SP7u2JAjkI8Cp2oOl07osEssG6jWD7gqM2NFtJPdXGUEWCd4L4DYxRZ6GxHW_LwSeXe15JveGDUND26pz0C0Z0fCo3uDRKpUQWhQFxiM2nuk2Bm0Pc-uWk4nCM6KlqixdfkKJ6pl_uQ6k6YnlCQ__rltOs8ilBkydP-6Uk_shrqsaDwm0fULZo7O9oha6kPG374LbZHL9q6zLdYRxfsMWiIut2P_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه عمان
پرچم  شیر خورشید ایران رو گذاشت
😁
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20860" target="_blank">📅 23:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20859">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">توافق ایران و عمان برای تنگه هرمز به معنای باز شدن خودکار تنگه نخواهد بود   منبعی نزدیک به تیم مذاکره‌کننده ایرانی به تسنیم گفت: درک چارچوبی در مورد مسیرهای کشتیرانی «به زودی اعلام خواهد شد»، اما «فقط» بین این دو کشور است و مسیر جنوبی هرمز را بسته نگه می‌دارد.…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SBoxxx/20859" target="_blank">📅 22:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20858">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJKTaqSbKSH3boHwm-_gKocDEvy2fuRZHpmRCrMtu6M_UT3lSZoffNl-y_UFRg1O-hZAbK7dogAXphl7v19A7MnaSGisqnO4u8pFp4VPLY0Nk6kEjBGX7r_ZqhX_1L9mt9nDb_g2C2rY6D_fah728bDh5yoUbdvQ3iQtWW-vnIW-w4U7R1712tvwlFZo94WAiy8RokT-8MOI2Vznm11jviBLqQH54YHBEdlzNsunew555w7AWLNmCekOov3GwXfINrEHn-RkftzX-vCp9PhIPtU61-TZZB6luvTSBmZpTKawgLaWU1zKXtth9PtjKMpcfgC_I1OOWMvARRfFXl2B_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگنده J-10C چین: نیرویی جدید در آسمان جنوب آسیا  جنگنده J-10C چین اولین پرواز رزمی خود را انجام داده و نقطه عطفی بزرگ برای صنعت هوافضای چین محسوب می‌شود. پروژه J-10 که در ابتدا در اوایل دهه ۱۹۸۰ تحت رهبری دنگ شیائوپینگ آغاز شد، با هدف توسعه یک جنگنده بومی…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20858" target="_blank">📅 22:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20857">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فیدان: سوریه می‌تواند جایگزین مسیر هرمز شود
وزیر خارجه ترکیه گفت:
سوریه می‌تواند با اتصال به اردن، عربستان، عراق و ترکیه، نقش مهمی در ایجاد مسیرهای جایگزین تنگه هرمز ایفا کند؛ مسیری که قرار است از طریق راه‌آهن، بزرگراه و خطوط لوله عملیاتی شود.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20857" target="_blank">📅 20:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20856">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVWqZzrjwORAkR9FiFa5zVvXYFvQPbpXMwQsT9Scl1o3vqt99rWB_KiFD6nhbcanx4iH6vn9uCmPvf2xxoYxKEwzFerRipAt29T8iNPAc8Yf6y_1KIJSNelNg6E1YYkgfzAnswnwy-bzrcujaIKsUT7K6k2wF0df96ShUYo6x6bwmtZMhZX8wBsi0Ia793TcTGNqzzaWxSlqN_sQNYkqaNI38Du21yQu7dLTte2zLAx3I7CbiMiwwSIUyWszB4M8xzCDoyrJaaLuiPK2QmFqRCLOgxizZFxqpEGQHXR7RYKt8TANhTsUAuTBNZb0z3TrFzVRe9MCUN1EWHxMXzl2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشیال تایمز:
ایران از روسیه درخواست پهپادهای اصلاح‌شده «گران» را کرده است
بر اساس گزارش FT با استناد به منابع امنیتی غربی و یک فرد نزدیک به کرملین، تهران به مسکو برای پهپادهای مدرن‌شده خانواده «گران» روی آورده است.
باور بر این است که ایران قصد دارد از آن‌ها در درگیری جاری با اسرائیل و ایالات متحده استفاده کند.
این نشریه علاقه تهران را به توسعه سریع اصلاحات جت‌ساز روسی و افزایش قابلیت‌های این پهپادها از نظر برد، سرعت و هدایت مرتبط می‌داند.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20856" target="_blank">📅 20:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20855">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SG648kGW4ztlgrSBjKMcdBS8uDzJ-YhtbVhvlzl6MQKzTX0qu01DG0tF0-FcVJzTkei3cDoRtzx-wM1498ve6nreIgDAbClzTX1LHrC_19c8ashoBcNH-2uNDvVFtblf8JeXzi7NceoJlgeQ49wRbcxnIBJTzMXCdmxDMe-6kmVt7PFQg6UMRivtzuCkkaIEl_-gfZYRxkuqX8vc0sYlTGIQp-cXvvhD55UFCxq-Ts_XgqGD2qgz9oCjOC34gqRJGoRqcg3gLogmZfSkGcY6zLitoh6oICZzskONEnRGEqJnSV9-X7Bd0c9asjxLMxxgxe4f3nnyg3M-E9bTBaQOrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20855" target="_blank">📅 18:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20854">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجار در بندر ینبع عربستان</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20854" target="_blank">📅 14:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20853">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هم میهن:  ترکیه به جای دلار گاز، غذا و دارو می‌دهد همتی به استانبول رفت  منصور بیطرف/ روزنامه‌نگار و تحلیلگر اقتصاد  دو روز پس از آنکه مهمت شیمشک ، وزیر دارایی ترکیه اعلام کرد که آن کشور - منظور ترکیه - پول گاز وارداتی از ایران را مستقیم پرداخت نکرده و بر…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20853" target="_blank">📅 14:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20852">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هم میهن:
ترکیه به جای دلار گاز، غذا و دارو می‌دهد
همتی به استانبول رفت
منصور بیطرف/ روزنامه‌نگار و تحلیلگر اقتصاد
دو روز پس از آنکه مهمت شیمشک ، وزیر دارایی ترکیه اعلام کرد که آن کشور - منظور ترکیه - پول گاز وارداتی از ایران را مستقیم پرداخت نکرده و بر اساس سازوکار توافق‌شده با آمریکا عمل می‌کند ، عبدالناصر همتی ، رییس کل بانک مرکزی ایران وارد استانبول شد
به گفته شیمشک، مبالغ مربوط به خرید گاز ایران در یک حساب به‌شدت تحت نظارت و تنظیم‌شده نگهداری می‌شود و ایران فقط می‌تواند از این منابع برای خرید اقلام مجاز در چارچوب رژیم تحریم‌ها، از جمله مواد غذایی، دارو و کالاهای مشابه استفاده کند.
سخنان شیمشک فقط درباره پول گاز نیست. این اظهارات نشان می‌دهد که ترکیه در دوره فشار حداکثری جدید آمریکا فعلا حاضر نیست برای حفظ تجارت با ایران، ریسک قرار گرفتن نظام بانکی خود در معرض تحریم‌های ثانویه را بپذیرد</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20852" target="_blank">📅 14:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20851">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSZqRnK0EKmzr_wlfnRfovps-Y4msJTg-jwvY-6MPj7IqYG8qBEHtTNm8YY3k1LniXcuYdzref4SqM4roAwB547hmNwuWHR1psYI8VJnqdea66Y-2Galo4QTpa-uAHuQrQ836gjuYS5VWMmaIKg9FOEQpXKkD-tDan1knB7msX6mL0Za5Q4WddyFqbq9Os0J2iGq2J2EAeRxskIbuJCyRbfHKoS331EJgGWNTnluWoVWbJgCZ_xZSoAQZFI8Dl29mf7YIn4RERrDUJprRgxRL4MIo6tNvSk6Hca26M3OiIzzWEWYcuq3R19vNDIKnrelc2tsf82GtOZ_2UOVVZANAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشیال تایمز:
حوثی ها با هوش مصنوعی آنتروپیک موشک بالستیک ساخته اند!</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20851" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20850">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پزشکیان:   نمی‌دانم مشکل آنچه در پاکستان نوشتیم چیست که آمریکا می‌خواهد از نو گفت‌و‌گو کنیم</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/20850" target="_blank">📅 12:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20849">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پزشکیان:
نمی‌دانم مشکل آنچه در پاکستان نوشتیم چیست که آمریکا می‌خواهد از نو گفت‌و‌گو کنیم</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/20849" target="_blank">📅 12:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20848">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خب امروز و بعد از ۹ ماه تارگت ۲۴۰ هزار تومانی دلار محقق شد.  بعید نیست مدتی رنج بشود.</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/20848" target="_blank">📅 11:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20847">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">— یک کشتی تجاری ایرانی در نزدیکی جزایر هنگام و قشم مورد حمله قرار گرفت که در نتیجه یک نفر کشته و سه نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/20847" target="_blank">📅 10:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20846">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">احمد اروزان کارشناس ترک:
خلبانان اسراییل برای حمله به ایران در قونیه ترکیه تمرین میکردند!</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/20846" target="_blank">📅 02:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20845">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">معاون وزیر خارجه یونان:
ترکیه و همه در منطقه می‌دانند که یونان کشوری بسیار قوی است که جایگاه بسیار بزرگی ژئوپلیتیکی، دیپلماتیک و نظامی کسب کرده است.
و من مطمئنم که هیچ‌کس هرگز این قدرت‌های یونان را آزمایش نخواهد کرد.</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20845" target="_blank">📅 00:39 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
