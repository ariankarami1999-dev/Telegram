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
<img src="https://cdn4.telesco.pe/file/tdn0nNdQz1I-CRPn6gpL4ftYOHYtPunv4G84ObMTusyPIA4YKEfQs2t_CkkPj_bDR8O9lPJcotI3hyY219t-45s64ebtXNg2AbSICPhrp9E4lZfvz0hGPTDpcj-0mbriKuzbtvzlHoyA17VTchsYLFNA1kjh6kIgWk9SAP5y6-CC39pLAk6mUwEssv-ln6JqaTIcW7hw7mYEfYCSfm7of37GOErcym20yquEQHiRzkupaJUq8Z6InLkjz9vjjSHjDkQyXQn8_d61c31-GskcUv7n2Mm31dyhScHtppgiJRda2fQtiK4rm-UMzp7HPEA2PZe2FO0psAl7kELalLz-Eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 946K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 09:59:19</div>
<hr>

<div class="tg-post" id="msg-129962">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
قالیباف: بعد از جنگ اخیر، شرایط منطقه متفاوت شده و باید با نگاه دیگری آن را دید
🔴
در گذشته برداشت برخی کشور‌ها این بود که نیرو‌ها و کشور‌هایی که از هزاران کیلومتر دورتر وارد شده‌اند، می‌توانند امنیت منطقه را برقرار کنند، اما بعد از جنگ اخیر مشخص شد که نمی‌توانند و خود از عوامل ضد امنیتی هستند
🔴
باید از این نگاه جدید در منطقه استفاده کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41 · <a href="https://t.me/alonews/129962" target="_blank">📅 09:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129961">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
نخست‌وزیر قطر: ضرورت ایجاد یک خط ارتباطی میان تهران و واشنگتن در دوران پاک‌سازی مین‌ها در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/alonews/129961" target="_blank">📅 09:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129960">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نخست وزیر قطر به فایننشال تایمز:
مذاکرات سوئیس (ايران - آمریکا) زمینه را برای مذاکرات دائمی حل و فصل بحران فراهم کرد و کار تازه آغاز شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/alonews/129960" target="_blank">📅 09:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129959">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EE1sQPtFg_5pmZRENTlup6RQ4-uIielyNcbIDhWH6P2zZAvkSSs2mAOz-3JCeckvgsPdquCKTifTQ7Z9GVhf_VYg1I4oAJkPmeniw4FoFVQ__wFUG94an-qKIT8M2J_afgB9a8c3x-Z-RzUhIbmapEbqtvqSLu9ydyz4FwBntSg7VtfWSsB-u345f6Vi_0IX1lfkNux-lMeJyXdjDdC3JnvRJdLa_XajB6g0kW0nnsshimu19V6ny9ycqbv98UnEdziLX_HjSHrRt6BnpEYbSV3-W58yx9lTY0W_q7caJzChgS7ofCNUxTOkFjjP-9hsKcni0mBtbj-y4nUeeeeURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقاد ترامپ از پمپ بنزین های آمریکا: قیمت را با کاهش بهای نفت پایین نمی آورند
🔴
ترامپ در شبکه اجتماعی اش نوشت:
شرکت‌های بزرگ نفتی قیمت‌های خود در پمپ بنزین ها را به اندازه کاهش شدید قیمت‌هایی که برای نفت می‌پردازند، پایین نمی‌آورند.
🔴
این قیمت‌ها مثل سنگ سقوط می‌کنند! به عبارت دیگر، مشتریان «سوءاستفاده» می‌شوند.
🔴
من به وزارت دادگستری دستور داده‌ام فوراً به این موضوع رسیدگی کند. قیمت بنزین باید خیلی سریع‌تر از چیزی که من می‌بینم کاهش یابد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/129959" target="_blank">📅 09:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129958">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f466cb2cd.mp4?token=gXwu7weUH6a5RsqpHbzzostTgBKQFKkPBtbiXV_8fZmuKWJhlsM1VzKIp43mQa-AXjzoM7S5M3JI9VxqwWHSJJYckARoA0TQdEbEsRI4X6zbg8lJ22XkV2oxwyFueN1ouvK-O1jy-MRUnvsbynBkW7ZGBZGcREfEOlauT-yN_7tK_jxEi6ObhCRF_M4SRgrMwZGcGSDpn-UytNntTtACQIaMb5aZ4f5Tzm_TVTvl8nnxskt5szGS76MOKQbxC1u0lW9BXEaEJkzBTGKg7LqWA4H2q4VHJ-yeFLbqpQlgJBGjNPJX_aOWNGjfxWacbXiSqec-IRkOTYk96hR38XrU-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f466cb2cd.mp4?token=gXwu7weUH6a5RsqpHbzzostTgBKQFKkPBtbiXV_8fZmuKWJhlsM1VzKIp43mQa-AXjzoM7S5M3JI9VxqwWHSJJYckARoA0TQdEbEsRI4X6zbg8lJ22XkV2oxwyFueN1ouvK-O1jy-MRUnvsbynBkW7ZGBZGcREfEOlauT-yN_7tK_jxEi6ObhCRF_M4SRgrMwZGcGSDpn-UytNntTtACQIaMb5aZ4f5Tzm_TVTvl8nnxskt5szGS76MOKQbxC1u0lW9BXEaEJkzBTGKg7LqWA4H2q4VHJ-yeFLbqpQlgJBGjNPJX_aOWNGjfxWacbXiSqec-IRkOTYk96hR38XrU-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: همسرم به من می‌گوید لطفا نرقص، اما من عاشق رقصیدن هستم
🔴
رئیس‌جمهور آمریکا در ادامه گفت: همسر بسیار شیک‌پوش من به من می‌گوید؛ عزیزم، لطفا نرقص! این در شأن ریاست جمهوری نیست. اما من می‌گویم مردم عاشق رقصیدن من هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/129958" target="_blank">📅 09:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129957">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
اکونومیست: نتانیاهو در نهایت مجبور است با توافق تهران- واشنگتن کنار بیاید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/129957" target="_blank">📅 09:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129956">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpBsy2YOMlvP_oowzgOZJNCH-xMsw8o5KN2IuwBkZnANEhT1LiYGgxYfN3SLgVI5vTj-BcL_B7Lg5ACrSSeVdP8rZw-NrDCEZlGIc77qekRXwAmfSqEF1lwI3LHrUv6PYg1RGxWP-ll2nOHt8i4Yo8AgwpzO8Q2-7aJ7ubLviipIhhJP-gWuCBtlSIDvqFY-BoVxNx_48GKlQlSgW8OlA0d3l93fwqAsUmKOVic61sCloK4lyUtbP4D-eDaCrlFBgqrFDQB2Rqgm_ROEH6JYgMCK6L0ZPs7yO9g8Q57dgaydF2pdj3vihsQVHjaFq-LJB09W-yNvlGeYj0OmIeN-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش سناتور برنی سندرز به تصویب قطعنامه غیر الزام‌آور اختیارات جنگی در مجلس سنا: کنگره بالاخره کاری را که باید ماه‌ها پیش انجام می‌داد، انجام داد: به درخواست از ترامپ برای پایان دادن به جنگ با ایران رأی داد.
🔴
قانون اساسی واضح است: روسای جمهور نمی‌توانند به طور یکجانبه ما را به جنگ بکشانند. این مسئولیت کنگره است.
🔴
زمان آن فرا رسیده است که کنگره سرانجام مسئولیت خود را بپذیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/129956" target="_blank">📅 09:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129955">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نخست‌وزیر قطر: امکان سرمایه گذاری کشورهای خلیج فارس در ایران طبق بند ۶ تفاهم نامه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/129955" target="_blank">📅 09:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129954">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
مهر : اختلال خدمات کارت‌محور بانک‌ها رفع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/129954" target="_blank">📅 09:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129953">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
لبنان و اسرائیل امروز هم مذاکره می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/129953" target="_blank">📅 09:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129952">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
لوفت‌هانزا: تمایل شرکت‌های هواپیمایی زیر مجموعه‌ ما به ازسرگیری پروازها به ایران
🔴
بررسی و برنامه‌ریزی برای گنجاندن این پروازها در برنامه زمستانه این شرکت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/129952" target="_blank">📅 08:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129951">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dae873392.mp4?token=K-VetWJIl-VQDmzpaohLmTM45ely4QviWON65JYIlSxBu2-j1ITt0hfjNTFNvq_2STG2i6UFEzW-6xJuf_iPqFXj-bWy9wxj84XTj7JQ-DjqDvJSLWrY3ZC-Z6yJv5CVrOpneIJ33_4rumA3ypOfmoZyStcTWv5stXaCH2PPnlEqPWPxiiRvhF6q5ifYnp0fpdn6-rnOlQeHCcUz_sc5RgE607dmpYQgcm1zt27FxTHqdgcJp5Qf_yNfqrsPMQ3FBjXkr6kmyYN-rzSyf1aWLzMn95u5L1yzsN_pgkVyn1kaHjxPOEprygY6LdnKznFrusvwqyWvQseZE1TkaLbUgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dae873392.mp4?token=K-VetWJIl-VQDmzpaohLmTM45ely4QviWON65JYIlSxBu2-j1ITt0hfjNTFNvq_2STG2i6UFEzW-6xJuf_iPqFXj-bWy9wxj84XTj7JQ-DjqDvJSLWrY3ZC-Z6yJv5CVrOpneIJ33_4rumA3ypOfmoZyStcTWv5stXaCH2PPnlEqPWPxiiRvhF6q5ifYnp0fpdn6-rnOlQeHCcUz_sc5RgE607dmpYQgcm1zt27FxTHqdgcJp5Qf_yNfqrsPMQ3FBjXkr6kmyYN-rzSyf1aWLzMn95u5L1yzsN_pgkVyn1kaHjxPOEprygY6LdnKznFrusvwqyWvQseZE1TkaLbUgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از کیروفسکه، کریمه، در میان حملات پهپادی اوکراین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/129951" target="_blank">📅 08:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129950">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pu_2EOt7t65fcgTz8HIHZFVJZUSUwjVC9P4lFzmICwHOjIQdL9kU1d_7xfCoxay2iFgZCfPef25QDyddfQMwWu5FBlBGadQQI9BuzmvMbLZ8Tm-NbShYT7YPX4Naok0oI6NYDmJXhWDzOiOb6GUZ1TKa4TAAjr2bN4j2LmdMQ8FXwgmQOefQVrGxxCBwYQdgq7nkJWaPkmOwIfBcFToYMPsWFry-YVIMyUQMRooENn5nHw-OQSsEhMV76TESI8HNL7TdJBiZHoV4DpLLHDTrzR6xrj7n8ghQ70eEMCY9oI5xJ-xx67n-4SelMtBSKKIb8FbLfJXkwxXPAge-EVlsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه ایالات متحده، تحریم‌های اضافی علیه «گروه مدیریت کسب‌وکار اس.آ.»، یک کنسرسیوم تجاری متعلق به نیروهای مسلح انقلابی که اکثریت تجارت کوبا را کنترل می‌کند، اعلام کرد؛ به‌طور خاص بخش‌های این کنسرسیوم که در بهره‌برداری از ذخایر معدنی و فلزی کوبا و بخش‌های مسئول انتقال دارایی‌های مالی و فیزیکی نقش دارند، تحریم شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/129950" target="_blank">📅 08:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129949">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cy90u-Fh000jiFEQp2-1pxpjbzFeszObsXRQzanNhHHBajKTaURE8UX-OMoLbhpq_BUJOC8m7Xmw83HVs377tVjY-rV9bnyMlIdtu7nRkTBzCII2vku2mo6gMXv6Nh2USJofInbxSKsptaKyDcFc7CeoFPnnpJC8FOPUiZBDbe_eA6NabvnNFtPDrXQfIlyAiXURnY_pHztRgY-RSGNCjtrHHSEvZCU9L_Sz5CXpgmqK01eu-qzBg2zRj2SfbluCUG7YplTC4Lyv87HP_ZtXepu4guhssOjvLqbzTBnO9nKm4nqpEBgdaDyodgoMTwC8V-f6-fKAPMe5SBGFiAFgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش ترامپ به تصمیم سنای آمریکا/سناتورها کار مرا دشوارتر کرده‌اند، اما من به هر شکلی که باشد آن را به سرانجام می‌رسانم
🔴
ترامپ: من ایران را کاملاً در تنگنا قرار داده بودم؛ در آستانه تسلیم بود، حاضر بود تقریباً هر چیزی به ما بدهد و برای نخستین بار در دهه‌های اخیر، احترام زیادی برای ایالات متحده و رئیس‌جمهورش، یعنی من، قائل شده بود.
🔴
اما سنای آمریکا تصمیم گرفت در زمانی نامناسب و بی‌معنا درباره قانون اختیارات جنگی رأی‌گیری کند؛ اقدامی که به بزرگ‌ترین حامی تروریسم در جهان این پیام را داد که ایالات متحده از کاری که من با آن‌ها انجام می‌دهم راضی نیست و باید متوقف شوم، و به این ترتیب به دشمن کمک و دلگرمی داد.
🔴
چهار جمهوری‌خواه بازنده همراه با دموکرات‌ها رأی دادند و ایران از افراد من پرسید: «همه این‌ها چه معنایی دارد؟»
🔴
این سناتورها کار مرا دشوارتر کرده‌اند، اما من به هر شکلی که باشد آن را به سرانجام می‌رسانم، چون همیشه کار را به نتیجه می‌رسانم!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/129949" target="_blank">📅 08:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129948">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx3W9txESGCg9AbYbgOqy4m5pGGMF6gTx9aXNS3x8Bl6UaMXv7z_mLQ7_raeVG1NcQ-uvoiCtEQV_Ohxbt-NLFEAF_cWgQ2gMMZrVsWqfdv4VXY9mXJX59mYU6BjVmVktxr1Xx5TcdzRUm2SUxCnmNokcjr7Vfhnu7cLfaiqv7Ax5g1XX6kSnWgFTn7dyNSmYnswrXcitRtP6RZi5sNCQQKpmkJMV3g-cpW_vcnUaVudwXMUD6VkxGe2kXSTB_F750jxnjFqylcZm4WAaWipOzMa9pJrKdKRe-08H3jMh1h7wHnVR-ejhF0akpAnxh_f_sZUXNhyxlf3Ke2jFMDVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیم جونگ اون، رئیس کره شمالی، اعلام کرد که برنامه تجهیز ناوگان دریایی این کشور به تسلیحات هسته‌ای مطابق برنامه‌ریزی‌های انجام‌شده در حال پیشرفت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/129948" target="_blank">📅 08:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129947">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWArXsGDMyEd7kvRCVvspM6uf6wXAq5-KehG8vSEqSLuS457YELIfodXLL-PBJatotaFa5VbC13TKii5Ahx7by0xHAWjYV0iV0qVeIT1z-bAzclLiczm-mT8898QNrcTYy6vfCnaLaMxm8UJGTBIkgsFdzpJASz8EDZudO3uhr3HKaebVv-3tDshUUtFGQjIVBJXaHPsgwA83aCUiiPXoVBbssfxq9-PkzF-mO3UlPSA9KZMx1w_dEVOVq4UXktNnGb6yJgVLvPLLff_cRBnLEOkF1EMhws0YpvsF_bWfNS7vbve30T7Ci1JRmBgVCUHELu8-fo7LNqYkhtnWnfMcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آای هیمتی:
اگه ذرت و سویا آمریکایی کیفیت خوبی داشته باشه، چرا که نه! میخریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/129947" target="_blank">📅 08:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129946">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drg4yf0awbNGm0an0k_T1UOfEfkNbBtH17pZgF997Cd-kjrrFy8N0E-0vujXi6VgIhpE3gOE85aMQf_X2TVfibe6NlJedIVYTHWadmPDEbJfUl6h354sntsVC0rWdkJbbwI9HveeTcqUJ4Pw_rGS8GacFbQt5YBuoyI12O2zu37HzhwqNYPknBeGC-br-wMia-VIgQzGKsYygvWKi-ISF1aAbGa_Pdnj3lIHBNZXoLCMVAaz-UncCNhfXTT2-zpnG02Ham-8bPmIalWdp9A6BGLh-d5g89vQfFsPpu9D295fntBbuKHpAz15EYtEpS0b4JHqUpsKJn2kjKU3RmJIAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری دنیا جهانبخت از حضور در مراسم عزاداری.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/129946" target="_blank">📅 08:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129943">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTkBiGp_TSPUXqqOQbxGWprpMaWMLQuce0afgtL9Yr9wHQZBZHvflqHOxb05cgr5g3DmjfP9cLsNfwVERYXnfXg4dF9mX4vFd1P_MRR3cREwSrFDIJ3WTUfbFqZf7y2jzdd5QVVJeI-n6J2iIM90nyKs3eri7cEeqwZv1z7GevwPayMo4w6XturC44DITshpbZ2tQQPSy6I2uviObbLOU35eDYQmH6BHf49VjdFeip64QYLrNiXjTn2kj8XXYn9ioBhRgHJTDBl8fW5YYYONkPse1h_avV4LAthLUrcSfb4Hg_ALz5fHr81G9wpXuWegr11opstu-wZW9UPZZEf9Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3qXTH4wYg9_CG8FacsxeXN7ZN9bEf_lJ3Qo4PCe9FgPmHGEbkwrDIQIthYSjCpnFl9HZyp3Ie-zYRQvpCqNtOx1Al325exOZCtppkpUSxQd-qfhggXLMAbc2UzHQSSyHY0Cizjidr_mrdYzyqeSmSuNWbEq2qboCeo8j5WkGRzDxwk_i9o0ujZR8BZ6--jxQOtqsv2FTb-XzJG0JCwLYR88ejag-4zI4VqKD5B8njQ0sC8TkOBy9_P-i1obBj2y2mHxtSQ915Enjek_Ny5-y2qe7BafygiFlqEl5Z0Me4RNcirQns5HyVIiLIC-n8hKF107iFapJrwmo8EBb2korA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNY2S26n6vFqjbQ2P_ypF1QuTJjjl2Z77ro6q7nECzsZmxdm2-Xn46b9I-vgQlbOqzb-eokbXMNiv7KTsJklbsSjK6HcBKXn-u-ZUoLSrMBMhEQc3FfrXTA2K_HLErdm4TCzwkan3wtshjWtU75ql_Fh6fl6pkZw1F7r_AYGxKDo3OevipMqetJ7YULSrGU4WjIcA1M3O4yui47msVAZ-alO2azGrvATuRW5bUTXnMN0CZLYOC5YsY_BihHPaRlZkWGk9bhWXXB8tORB5AsBiSvsWxiZYBjRZniXarU6keRfiFLXXFK7NXars8-lReZ720JFvtb0Vjbt1e4-j_szMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش اسرائیل به چادری تو غزه حملهِ هوایی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129943" target="_blank">📅 01:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129942">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCUIWWOLyyoVGlN1ODnYQ5GCZ4XyBWQruDpL-eTr30wceLRD3mMo8sLKxDr7kj1nnjgcPin60zDnQo94dylERjjNKiiCBUVbpzpSzjQ3BPYFJvymV29ENYQ6Eio8wcn9pUpB7MEx09QPFTAp00mvO1XXAb7aJJAPzza7D093BK1Ex6UbvdiMLOKjF9CGnpWBEVJnn27MV_NH4mHXk4C7VusZLJqkssn28ak0rotYQHYxnxwyEKoyx-9Ix7VEpI8jlAkBNGg9nNwpFa_qByMd2dGQ6ZyBZMKydQNmdZ0UqnaZ1TY6c3sneC9nbxFJM3vHTDbp306AqV7lD6Ja62-Y5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: این روزا همه چیز عجیب شده...
🔴
اون جایی که باید بسته باشه، بازه.
🔴
اون جایی که باید باز باشه، بسته‌ست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/129942" target="_blank">📅 01:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129941">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
فرماندهی سایبری کشور:  اختلال ایجادشده در سامانه‌های کارت‌محور برخی بانک‌ها ناشی از یک حمله سایبری هدفمند به زیرساخت‌های مرتبط بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/129941" target="_blank">📅 00:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129940">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375b61eb9b.mp4?token=bsCAD9X7BOB2kjzgqtkQkVZVggDkTgWGuOqRe0TTe7XYtzb7M7aHMs7gBiPR2GTTCn3pMizJpNVLO4TqPQzmqPDwFmkzpNaVsKOyVdiOqPEPD2sCY72AHrZ52AhAacayFSiwlBvYTlHahkTsH0uVDy0V3MiqQEhGThEjwMgcdX6he_LZzO8U5KkayIV_f73KY3_vBwKnhSvVQM4odfRn1U3dZcOAShb_eX8o8Yrk1R2l2o4Aswqkixqbkm4sLvqubnj386mZe1IeBsDG6j_1WF7qoO4t_vqTLHllmaSQr1TGdqdGHFUSOcnJHJ5TBSxMBHLU0GlQwvealmTF1f0oxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375b61eb9b.mp4?token=bsCAD9X7BOB2kjzgqtkQkVZVggDkTgWGuOqRe0TTe7XYtzb7M7aHMs7gBiPR2GTTCn3pMizJpNVLO4TqPQzmqPDwFmkzpNaVsKOyVdiOqPEPD2sCY72AHrZ52AhAacayFSiwlBvYTlHahkTsH0uVDy0V3MiqQEhGThEjwMgcdX6he_LZzO8U5KkayIV_f73KY3_vBwKnhSvVQM4odfRn1U3dZcOAShb_eX8o8Yrk1R2l2o4Aswqkixqbkm4sLvqubnj386mZe1IeBsDG6j_1WF7qoO4t_vqTLHllmaSQr1TGdqdGHFUSOcnJHJ5TBSxMBHLU0GlQwvealmTF1f0oxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهباز شریف هم نتونست مانع بیل زدن پایان ناپذیر پزشکیان برای کاشتن درخت تو اسلام آباد بشه
🔴
شهباز هی میگه نمادین هست ولش کن اما مسعود ول نمیکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/129940" target="_blank">📅 00:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129939">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کانالای ایتا: ممکنه نهاده‌های دامی آمریکایی آلوده باشه و مردم مریض بشن
🔴
پ.ن: احتمالا ارزشیون جزو دام و طیور هستن که نگرانن
😂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/129939" target="_blank">📅 00:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129938">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhTe4dP8txcqwAwbo6-LS2i_B3w6CWQ1WlCCTHf4WCOudumW5TtoHia8ZxVMslBczYMYUZTOrvEwDoyiUnL-If9sY3WKRP8hk0ntlfL8GheoBR6s2g0mY8NufskpHN80ZZyDRbKpZze3Xdc519niwRSMZDIO1dM4EPA4or0CHkNQz8so8utQXQxzEm_sPALqCHRrEEDQrCrsDROtmv89pD7ltr4YHyO-J2qhg_AfbMdyhSzlLHy12LvSmHOipcekjmgjpRAAIutvZesbrQLMBIqzbd7K8s9FP3_0ii2ndhAyzpi3eTokLvhiUmecXQ75dnb-54eTu5JChWhXQtxqRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تقریبا 320 تا پهباد به سمت روسیه پرتاب کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/129938" target="_blank">📅 00:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129937">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
امیر پوردستان رئیس مرکز تحقیقات راهبردی ارتش: چنانچه مصلحت نظام ایجاب کند، ممکن است با انجام عملیات‌های پیش‌دستانه در عرصه‌های ناشناخته، دشمن را به‌شدت غافلگیر کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/129937" target="_blank">📅 00:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129936">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ: به توافق صلح تاریخی با ایران دست یافتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/129936" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129935">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c0d36b14a.mp4?token=dPpFf6FCFKPASm3XG21l1Z74DKcgMbBMSGWyfb1ZrLvJ4ozUyZbHiOMcIFL0c84zLp-A-dU-NxFWKZ98-fFuuX1tDZ-wXGSiO0wd6NQn6rlmvnxztHa8Gys5AxbS7n7vuAe-j9XbofgjI58EMpmAkgXYHrlsut8j_exsRt1m2phLxH9IBvVRGHCwUxzFffrk7By8ZwcCynryBjcktfNgDVOzgIyRuXoRR7lji1P-59kcZHOz_bE_j7n4LrauNcclM8NZDRj7jPmjzLc8cJP8Yi2oGHSLNXZC6BrIKVLxVVejqyGd30n9MK6ROe6pEv9FnWQl8ZPrcT67YPREDBGJmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c0d36b14a.mp4?token=dPpFf6FCFKPASm3XG21l1Z74DKcgMbBMSGWyfb1ZrLvJ4ozUyZbHiOMcIFL0c84zLp-A-dU-NxFWKZ98-fFuuX1tDZ-wXGSiO0wd6NQn6rlmvnxztHa8Gys5AxbS7n7vuAe-j9XbofgjI58EMpmAkgXYHrlsut8j_exsRt1m2phLxH9IBvVRGHCwUxzFffrk7By8ZwcCynryBjcktfNgDVOzgIyRuXoRR7lji1P-59kcZHOz_bE_j7n4LrauNcclM8NZDRj7jPmjzLc8cJP8Yi2oGHSLNXZC6BrIKVLxVVejqyGd30n9MK6ROe6pEv9FnWQl8ZPrcT67YPREDBGJmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ دوباره تهدید کرد
🔴
می‌توانیم کار ایران را کمتر از یک هفته تمام کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/129935" target="_blank">📅 23:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129934">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d170582e.mp4?token=d5ucqB00wBjzyCz3Qvwxglq0_Ok3pIhXatZCdazuBxC17ZGTrGex9ipDlZLdWkEZ2ZEyz3VN3thAd54oEUYYDlmwuIq3JuGA_p2EyTTf65jwBZKYSYt8gi07lf0hV-KfOB4rkQahZhXyZdokFt3Sbh94j7IMyHzqmVEmW8gJZETwE0qV9C5Nm2hPF11I2Q5WvYByJJfS7LEEOTDa1sxaVFQK15vwRMhQRkecPW3K6M1NB2s95BuquGzcl-tq_9mrmuFbn8oBEs75FADR7O0pEafxr8cEejl9iS87lJ0djHON6uOY-VrbA7UhVqQK9dwXKJ9k2lHcaYZVfaZAXEz3MWmvmlGq7scitFsDViQkNmn8uyN3Z_aJw4FlLvzRxWJbSQMbsyX4PIc6dKc25AKsXw-OLccZn_Ck_nrCk5BhtB8vPGbAR_3vmWe57-Gln2sphrUMqTcZasSe-K1KmkCjbibZab_sNhBHfOLVvoNEXEKCrcg-6XHOk-F6UU6gMuJaj7rOEsDqo_Fll7NUSJqoiHhvmkJY_7GmWjPigXo8Hv_N7eO7s9FDsI1acZ-iCWWcZdpMY_UprP1RZT6Vp2KfUVWsFlZ95pORJQJ5YgO_nQ3hfMqmOlMgLZ1EHuaqbKPxi7i_DUXDfrPa3Zo1o9UxE-6yY48iC6URm7eSsfjADBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d170582e.mp4?token=d5ucqB00wBjzyCz3Qvwxglq0_Ok3pIhXatZCdazuBxC17ZGTrGex9ipDlZLdWkEZ2ZEyz3VN3thAd54oEUYYDlmwuIq3JuGA_p2EyTTf65jwBZKYSYt8gi07lf0hV-KfOB4rkQahZhXyZdokFt3Sbh94j7IMyHzqmVEmW8gJZETwE0qV9C5Nm2hPF11I2Q5WvYByJJfS7LEEOTDa1sxaVFQK15vwRMhQRkecPW3K6M1NB2s95BuquGzcl-tq_9mrmuFbn8oBEs75FADR7O0pEafxr8cEejl9iS87lJ0djHON6uOY-VrbA7UhVqQK9dwXKJ9k2lHcaYZVfaZAXEz3MWmvmlGq7scitFsDViQkNmn8uyN3Z_aJw4FlLvzRxWJbSQMbsyX4PIc6dKc25AKsXw-OLccZn_Ck_nrCk5BhtB8vPGbAR_3vmWe57-Gln2sphrUMqTcZasSe-K1KmkCjbibZab_sNhBHfOLVvoNEXEKCrcg-6XHOk-F6UU6gMuJaj7rOEsDqo_Fll7NUSJqoiHhvmkJY_7GmWjPigXo8Hv_N7eO7s9FDsI1acZ-iCWWcZdpMY_UprP1RZT6Vp2KfUVWsFlZ95pORJQJ5YgO_nQ3hfMqmOlMgLZ1EHuaqbKPxi7i_DUXDfrPa3Zo1o9UxE-6yY48iC6URm7eSsfjADBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ پیشنهاد می‌کند که ونزوئلا باید در آمار تولید نفت ایالات متحده گنجانده شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/129934" target="_blank">📅 23:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129933">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فرماندهی سایبری کشور: اختلال ایجادشده در سامانه‌های کارت‌محور برخی بانک‌ها از جمله بانک‌های ملی، صادرات و تجارت ناشی از یک حمله سایبری هدفمند به زیرساخت‌های مرتبط بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/129933" target="_blank">📅 23:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129932">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نخست‌وزیر ایتالیا: ما باید سیاست خارجی را به عمقی که سیاست خارجی به آن نیاز دارد، برگردانیم.
🔴
نظرم را درباره رئیس‌جمهور ایالات متحده عوض نمی‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/129932" target="_blank">📅 23:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129931">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری / سنای آمريکا طرحي را تصويب کرد که به دنبال مسدود کردن اقدام نظامي عليه ايران است مگر اينکه رئيس‌جمهور ترامپ مجوز کنگره را دريافت کند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/129931" target="_blank">📅 23:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129930">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ: ایران عالی بوده است. اگر ایرانیان هوشمند باشند، منطقی خواهند بود؛ در غیر این صورت، مجبور خواهیم شد کار را به پایان برسانیم که احتمالاً کمتر از یک هفته طول می‌کشد.
🔴
اما فکر می‌کنم همه چیز برای آن‌ها خوب خواهد شد. آن‌ها کاری که باید انجام دهند را انجام خواهند داد زیرا ما می‌خواهیم این کار انجام شود
✅
@AloNews
خبر جنگ
﻿</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/129930" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129929">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ : ایران با ونزوئلا خیلی فرق داره و نگاه و ایدئولوژی متفاوتی داره
🔴
در کل هم طرز فکر و باورهای مسلمان‌ها با کاتولیک‌ها یه سری تفاوت‌های اساسی داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/129929" target="_blank">📅 23:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129928">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری / سنای آمريکا طرحي را تصويب کرد که به دنبال مسدود کردن اقدام نظامي عليه ايران است مگر اينکه رئيس‌جمهور ترامپ مجوز کنگره را دريافت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/129928" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129927">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8dc387a22.mp4?token=j4CmVU2APr4tfVDQcNSuirT9kycVqukSU4eZwOsB3bB3k_ES-4ypPrJbZNwyOeRaztaNPXQnumhqdJKPUtvdWiBxQLWtTEObr4qfODEXtIk25Gj5DgyTrieiYFAZmaKhqmE7ICXohLTkzI9Yl7CijD7riDbShHblMKP6TtJ6eZX2toHXLvwlej_dLLsfQm1w_m1IQMvHWNhQo3FV2hndGj6wJ9Ci28xnkZG9OL_kJPwVeH0Vbbo8hstkMAZZH0RJrYLnQebg3ah1ON7NLrl4xgRu2gzY42gD_v7lwu4EF-RmlLJshJqgr-mFmwrTLysYOf1nrck1njMfvROcuYw2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8dc387a22.mp4?token=j4CmVU2APr4tfVDQcNSuirT9kycVqukSU4eZwOsB3bB3k_ES-4ypPrJbZNwyOeRaztaNPXQnumhqdJKPUtvdWiBxQLWtTEObr4qfODEXtIk25Gj5DgyTrieiYFAZmaKhqmE7ICXohLTkzI9Yl7CijD7riDbShHblMKP6TtJ6eZX2toHXLvwlej_dLLsfQm1w_m1IQMvHWNhQo3FV2hndGj6wJ9Ci28xnkZG9OL_kJPwVeH0Vbbo8hstkMAZZH0RJrYLnQebg3ah1ON7NLrl4xgRu2gzY42gD_v7lwu4EF-RmlLJshJqgr-mFmwrTLysYOf1nrck1njMfvROcuYw2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در پنسیلوانیا
:
«کدومو بیشتر دوست دارین، جو خواب‌آلود یا جو فاسد؟ آماده‌این؟»
🔴
جو خواب‌آلود! تشویق حضار
🔴
جو فاسد! تشویق بلندتر حضار
🔴
«متعجب شدم. من خودم "جو خواب‌آلود" رو بیشتر دوست دارم، ولی ظاهراً "جو فاسد" برنده شد. البته هر دوشون خوبن!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/129927" target="_blank">📅 23:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129926">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15aaa27354.mp4?token=mhwW4-O37-qZmXefe5SukzDfNp81fV5apAlD2ZqZdoq4f2pYdPKLMFHO-l5CUi1sT8QoCXjrAuUd5hDYiBXGLH2FYqFNxZb6FriOgPAoyde1bOeU9kbm2BupNqQlMf60t6BXMGSE3re4CGC1venZjsn9KMV534NezymectJM-KNhb_ajKNu_lkxL1EFepKQpAXTmERL-o2wGmKMHM2cWmNsbAr_YsUHsPNyHIf8kazZXDGv4522zPvyRca2qh0GIlh_YjeY_P06fb1aoGs5PjxWMqCi-Lcg0qjkNRrTsHOxeT4Xp5D_mMmAW-PNlfjdwMRt2YP5ng7K6PafDo0T7Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15aaa27354.mp4?token=mhwW4-O37-qZmXefe5SukzDfNp81fV5apAlD2ZqZdoq4f2pYdPKLMFHO-l5CUi1sT8QoCXjrAuUd5hDYiBXGLH2FYqFNxZb6FriOgPAoyde1bOeU9kbm2BupNqQlMf60t6BXMGSE3re4CGC1venZjsn9KMV534NezymectJM-KNhb_ajKNu_lkxL1EFepKQpAXTmERL-o2wGmKMHM2cWmNsbAr_YsUHsPNyHIf8kazZXDGv4522zPvyRca2qh0GIlh_YjeY_P06fb1aoGs5PjxWMqCi-Lcg0qjkNRrTsHOxeT4Xp5D_mMmAW-PNlfjdwMRt2YP5ng7K6PafDo0T7Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسحاق دار، وزیر خارجه پاکستان در مصاحبه با شبکه العربیه: براساس برداشت من نباید هیچ هزینه‌ای در مورد تنگه‌هرمز وجود داشته باشد، فرقی هم نمی‌کند چه اسمی داشته باشد و وضعیت پیش از ۲۸ فوریه باید احیا شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129926" target="_blank">📅 23:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129925">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ در پنسیلوانیا: ایران قلدر خاورمیانه بود.
🔴
و اکنون ما ایران را بدون نیروی دریایی، بدون نیروی هوایی، بدون سامانه‌های پدافند هوایی، بدون توان موشکی و بدون برنامه هسته‌ای ترک می‌کنیم.
🔴
ما در تلاشیم تا توافقی عادلانه را به نتیجه برسانیم.
🔴
ما باید این مسیر را انجام می دادیم. باید به ایران می رفتیم.
🔴
شما نمی توانید اجازه دهید که خاورمیانه و سپس ما را منفجر کنند، اگر این امکان پذیر باشد. ما قبلاً آنها را می گرفتیم، اما آنها اسرائیل را منفجر می کردند. آنها می توانستند کل خاورمیانه را منفجر کنند.
🔴
آیا می خواهید اقتصاد بدی را ببینید؟ این یک اقتصاد بد است. پس به یاد داشته باشید که نفت ما در میانه این درگیری کمتر از جو بایدن خواب آلود بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/129925" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129924">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد و این بزرگ‌ترین مقدار نفت عبوری در تاریخ این تنگه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/129924" target="_blank">📅 22:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129923">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452666b6dd.mp4?token=NnhMMEHFl-3YxQHcbUQItklLSZeBkfxcb7p3XQjNEd3drH57ZZ0GtDHnYZFygmc6liDnG4Tg9ILBXFsQ-MJdE1YfY5GlnbG9_IDKUcLLBpwhF13Wfg-dFpgAHzwIIMp0LScD-2zZACH9eczVJWRjB_DpIGyqBH0xUyKjfhlw-a2FPFRiUgAfyxH517TXKEPPcQWucu2GgzXBfZHlZRpf4tfyEpG3z7DVW2nLdKu1GiudQhrs0c73pxcF18EgB0P_GGQJS-giZt1w7CO4UuVirMV7Ei3E2x7a__V3z956b0p4ztW7OcvBmHNDuHcMj6aGMtf4O_WRX3A5x7D6BUTV0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452666b6dd.mp4?token=NnhMMEHFl-3YxQHcbUQItklLSZeBkfxcb7p3XQjNEd3drH57ZZ0GtDHnYZFygmc6liDnG4Tg9ILBXFsQ-MJdE1YfY5GlnbG9_IDKUcLLBpwhF13Wfg-dFpgAHzwIIMp0LScD-2zZACH9eczVJWRjB_DpIGyqBH0xUyKjfhlw-a2FPFRiUgAfyxH517TXKEPPcQWucu2GgzXBfZHlZRpf4tfyEpG3z7DVW2nLdKu1GiudQhrs0c73pxcF18EgB0P_GGQJS-giZt1w7CO4UuVirMV7Ei3E2x7a__V3z956b0p4ztW7OcvBmHNDuHcMj6aGMtf4O_WRX3A5x7D6BUTV0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
ما می‌توانیم هر وقت خواستیم بر فراز تهران پرواز کنیم و هیچ‌کس نمی‌تواند کاری با ما داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/129923" target="_blank">📅 22:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129922">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
پوتین: احتمال بروز درگیری در مناطق مختلف جهان در حال افزایش است
🔴
کشور‌های غربی آشکارا اعلام می‌کنند که برای جنگ با روسیه آماده می‌شوند؛ آن‌ها هنوز به مرحله وارد کردن ضربه مستقیم به روسیه نرسیده‌اند، زیرا می‌دانند که مسکو پاسخ خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/129922" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129921">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
پزشکیان اسلام‌آباد را ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/129921" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129920">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXn6pXYqyLf7sTfETIK14_1PGxE0akU4cqB-qEMc6rRENmHM-GxOsjNT1aKZIza1qCAvfPeo4yiKY2f7tRm5yogmDbe2uD7ufsFcAxUB9IaQmN3WqoG7lnd4LVy7GO5InAbU1hOBrS6Dz6L9sV7trPKrm6J-0Q1ebedlV6IRvThkqlD8h8NkdqVQya0VVWWVWNZSGO7tm7WbYXSWX7flsqcKLJDKAWQXwqtRqz-Rayzmb4W-ul_GNH0EnEem1IWOhSJnq9p4l3wV-lCcQuncWeFb67W_IQXYj06ZYZxERyzZr0kbI4x9Kz2vOvY0CKmoGyClCEyDnhn3Wr01C-A0rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک خیلی منطقی و یهویی اومده یه ویدیو از محرم پست کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/129920" target="_blank">📅 22:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129919">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3245b245a.mp4?token=JxykG2SW2VBnD7Z7_KpFY1c5SETkvUkhIaXawSxEsgi9-w8gN-WectWPcfcAJ4ID7TlZtl8vDw3-fvCUqAtioLjiqHTNLnOVOe7lCM8c4BunLlTRdM6gkUo6fpEunQhNTQKFWpUau2-avwiGIMH94SSV9CRLrti9Y8nRki3tCbCnUEs5cBfhvZNVc6XdDh49IxMrqOe2QtomPy5-hI5XV3UdSJ1K7Wi0j5ImZse-mMXXERgLfNSur3tic09lMQu5y-9uCHrzLaqZKCgfCxFQx4XD1bK5nNzYjV6de2zJzjKEAwRQ_q3mdwW8Rla_HpZvugB6HxygUIdwHZD23u4dsUmn10P2TOjECYfNmbQ4SnYt1SbejXlMqk9Jxp8THDstemhg0U0N9F-r3gj8nwTl9Mmw6Tzf4V0sQSf_0-InUuVqXntbsSx4vd57pM2wwCQbDOxmoY1Ma5hogvsRutR338ZdpfZ1hNVhUc4emwuMxMXCUtBr9Wh_72ze5dfwfrk7HG4s9jCGCXZ5LpwZsuijAg9pNbheHEW0WJvk3_VZD62GxRBGiL8LyMMLyEbNEVuqVuBekqfZI120GHEjLjmVqFR2WtonXhR0JayKEoG9HJqc4C5HGBE4Z6GZtporWZznr12G6ca042U7sKZOQhU6ftH5l2H5ox7Rl8VJe18KlD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3245b245a.mp4?token=JxykG2SW2VBnD7Z7_KpFY1c5SETkvUkhIaXawSxEsgi9-w8gN-WectWPcfcAJ4ID7TlZtl8vDw3-fvCUqAtioLjiqHTNLnOVOe7lCM8c4BunLlTRdM6gkUo6fpEunQhNTQKFWpUau2-avwiGIMH94SSV9CRLrti9Y8nRki3tCbCnUEs5cBfhvZNVc6XdDh49IxMrqOe2QtomPy5-hI5XV3UdSJ1K7Wi0j5ImZse-mMXXERgLfNSur3tic09lMQu5y-9uCHrzLaqZKCgfCxFQx4XD1bK5nNzYjV6de2zJzjKEAwRQ_q3mdwW8Rla_HpZvugB6HxygUIdwHZD23u4dsUmn10P2TOjECYfNmbQ4SnYt1SbejXlMqk9Jxp8THDstemhg0U0N9F-r3gj8nwTl9Mmw6Tzf4V0sQSf_0-InUuVqXntbsSx4vd57pM2wwCQbDOxmoY1Ma5hogvsRutR338ZdpfZ1hNVhUc4emwuMxMXCUtBr9Wh_72ze5dfwfrk7HG4s9jCGCXZ5LpwZsuijAg9pNbheHEW0WJvk3_VZD62GxRBGiL8LyMMLyEbNEVuqVuBekqfZI120GHEjLjmVqFR2WtonXhR0JayKEoG9HJqc4C5HGBE4Z6GZtporWZznr12G6ca042U7sKZOQhU6ftH5l2H5ox7Rl8VJe18KlD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر ایتالیا، ملونی: ما نمی‌توانیم اجازه دهیم که رژیم آیت‌الله‌ها به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ویژه با توجه به اینکه آن‌ها از پیش — و به‌وضوح نشان داده‌اند که — موشک‌های برد بلند در اختیار دارند.
🔴
و من فقط درباره ایالات متحده، یا کشورهای نزدیک‌تر به مرزهای ایران، یا اسرائیل صحبت نمی‌کنم.
🔴
ما نمی‌توانیم اجازه دهیم. ما توان پرداخت هزینه آن را نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/129919" target="_blank">📅 22:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129918">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
عضو رسانه‌ای تیم مذاکره‌کننده: هیچ بازرسی از تاسیسات هسته‌ای آسیب‌دیده انجام نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/129918" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129917">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
نخست‌وزیر ایتالیا: اگر اجازه دهیم ایران در تنگه هرمز عوارض بگیرد، وارد دنیایی خواهیم شد که هر مسیر تجاری استراتژیک به یک سلاح تبدیل می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/129917" target="_blank">📅 21:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129916">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4723480403.mp4?token=FWfxethf2f63TAAk8-uOLb4af2hoLtacEV1UuMWDGs3x94oM6xrizCxK5J-eFWYtiuu4R4ITv2NpAtL1B-W31ZdmEjWlv-T_9PLz1zdUS5_JPj8otXH0gniGdUjyt7H8O4opWeft07FMob9ILiRCDOnDqP2VkZ2uqpQYohLhDFoCO-sBBLQXvD1ji8a8vuSTzahezxDMFd0TdA-hsMC8EpgQ3hQB6NbWHEf4RscFXK7s2j8me4qRVRHLybveNq9gBxTZ7C4Exhe_N1tWG7ueBv3ehBdWLPS8jY2w5HTALZcrFim1JXtqVojfPJdbRRwn7mImnq-THN7TZTFENzBxiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4723480403.mp4?token=FWfxethf2f63TAAk8-uOLb4af2hoLtacEV1UuMWDGs3x94oM6xrizCxK5J-eFWYtiuu4R4ITv2NpAtL1B-W31ZdmEjWlv-T_9PLz1zdUS5_JPj8otXH0gniGdUjyt7H8O4opWeft07FMob9ILiRCDOnDqP2VkZ2uqpQYohLhDFoCO-sBBLQXvD1ji8a8vuSTzahezxDMFd0TdA-hsMC8EpgQ3hQB6NbWHEf4RscFXK7s2j8me4qRVRHLybveNq9gBxTZ7C4Exhe_N1tWG7ueBv3ehBdWLPS8jY2w5HTALZcrFim1JXtqVojfPJdbRRwn7mImnq-THN7TZTFENzBxiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی این روزا میری بیرون
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/129916" target="_blank">📅 21:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129915">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ریس کل بانک مرکزی: در مذاکرات با آمریکا دو تصمیم مهم در ارتباط با بخش اقتصادی این تفاهم‌نامه داشتیم
🔴
یکی مربوط به آزادسازی منابع مسدود شده ما بود که در تفاهم‌نامه آمده بود و در جریان مذاکرات به تدریج آزاد می‌شود.
🔴
قرار بود ۱۲ میلیارد آن ابتدای کار آزاد شود و بقیه منابع در جریان مذاکرات.
🔴
با توجه به آن که در جریان مذاکرات ۱۴۰۲ موافقتنامه ای بین ایران و آمریکا امضا شده بود، ما مبنا را آن قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/129915" target="_blank">📅 21:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129914">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBc-436Imb22LOYE0mjJuctvZMhXD7LeDj5WoPAUH1oWW0E0FMTdAg2gm5e-VmH3_q6qZwB-7Yj3H3ZIc7LK8SG9lFIEtRQobGfOMpV_Cv-hDGh7NLXw7a-Q0ApJuOmRWUiXyrpYGNMblfB-a_564L27WGE0BspCnO5mAwQu09d6LwL4ffsnZ8Ct-7L7DHyvadoko5JS1WJUVvjgXwbYxet0_kkwN8vy-u_ueyKJfHgLg-yWo6WFjUA9XALv6dsphTXkx6dEBpKjjxBHJt-EsUhr9u7gdvXxpXjE4Sgfv8VcUJy4FlkxWrVZuQSVDB2OCcF1r5Lt8t-njm_31y8Yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش آکسیوس، تیم ملی فوتبال اجازه دارد دو روز پیش از دیدار بعدی خود در جام جهانی، به ایالات متحده سفر کند.
🔴
تیم ملی برای دیدار سوم خود در سیاتل (۲۶ ژوئن / ۵ تیر) مقابل مصر، می‌تواند دو روز زودتر وارد آمریکا شود. با این حال، تیم همچنان باید در همان روز پایان مسابقه، کشور را ترک کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/129914" target="_blank">📅 21:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129913">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06aba58df.mp4?token=RfL0NnrGuEqaSA__mbj_bAJtarywEMF2dHR1D-EauDboOxnj4B2c9Of3KD3zZOGFpBcjBcDCMenbm4CixCPlFnVRpmnx1thFzfmYCnbVdVRFhFKf6P3Imm7DKyP05oYli6qVLS3bO2mXtDwD6LnBs28OprzVO2BJOSiS9iIn3uRGWCGREYdL-gKBbDYgxpP0klVuCtG_faFOhaFY8DgJwOAjO29WfTEMfYXcX3WOdVWC7Ep8nvqFQD90X9tDCL327fpdW7x1tlJpEDF-UIGQP4uV1fws_xjadQpcB85snVd4pOzr922StfSx_Kx_9VKPJnyriqBBVDrKJ_tdCcZekQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06aba58df.mp4?token=RfL0NnrGuEqaSA__mbj_bAJtarywEMF2dHR1D-EauDboOxnj4B2c9Of3KD3zZOGFpBcjBcDCMenbm4CixCPlFnVRpmnx1thFzfmYCnbVdVRFhFKf6P3Imm7DKyP05oYli6qVLS3bO2mXtDwD6LnBs28OprzVO2BJOSiS9iIn3uRGWCGREYdL-gKBbDYgxpP0klVuCtG_faFOhaFY8DgJwOAjO29WfTEMfYXcX3WOdVWC7Ep8nvqFQD90X9tDCL327fpdW7x1tlJpEDF-UIGQP4uV1fws_xjadQpcB85snVd4pOzr922StfSx_Kx_9VKPJnyriqBBVDrKJ_tdCcZekQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهباز شریف: برنامه موشکی ایران هرگز بر سر میز مذاکرات نبوده و در تفاهم‌نامه نیز ذکر نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/129913" target="_blank">📅 21:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129912">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نخستین بیمار تب کریمه کنگو در اردبیل شناسایی شد
🔴
معاون بهداشتی دانشگاه علوم پزشکی استان اردبیل گفت: نخستین بیمار قطعی تب خونریزی دهنده کریمه کنگو در استان طی سال ۱۴۰۵ شناسایی و تحت درمان قرار گرفت.
🔴
سعید صادقیه اهری به ایرنا، ایرنا اظهار کرد: این بیمار، زن ۴۶ ساله‌ای است که با سابقه گزش کنه شناسایی و بستری شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129912" target="_blank">📅 21:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129911">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJOYO8t8EK1TE016sg6IQ9yMI0Hb3tADcj0Yz5hnY9Pi4O8sawP4S8s507uWQI_VSOellLAKC4Fm1DdOibnbnYpj0GQbkTiRnckswDNU-FJyxzQ1zHxghloXaY_-xEfYcLdRdn0npCVun1xnUqKpvc0vKYrfdZSNKv8SIGPd0bP8ZM2wHg5KTTuDJqZeAnIOVLBZCEVztrt-QNA14j5izCt1-I02x5oulrefMAuDXffUgisq4faLcXWM-dWk8qrqB-AHY8gv6KEXWgXiKu3UL_MOixvxoe7qRbChAhy1O4m8VRBA5AvvricLnC84r6z5GRgTfUvXzh3JHUlLM02zvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه اسرائیل : حزب‌الله با حمایت مالی جمهوری اسلامی طی سال‌ها(صدها میلیون دلار) شبکه گسترده‌ای از تونل‌ها، انبارهای تسلیحاتی، سایت‌های موشکی و مراکز فرماندهی در جنوب لبنان ایجاد کرده.
🔴
هدف این زیرساخت‌ها حمله به اسرائیل بوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/129911" target="_blank">📅 21:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129910">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ: اوضاع در لبنان خوب پیش خواهد رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/129910" target="_blank">📅 21:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129909">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ : ما داریم یه توافق فوق‌العاده با ایران می‌سازیم؛ داریم توافقی می‌سازیم که کشورمون و دنیا رو امن نگه می‌داره
🔴
چون اجازه نمی‌دیم ایران سلاح هسته‌ای داشته باشه، و اونا اینو می‌دونن، و باهاش موافقن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/129909" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129908">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
خبرنگار : بازرسان آژانس کی قراره برن داخل ایران؟
🔴
ترامپ : هر وقت زمانش مناسب باشه، عجله‌ای نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129908" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129907">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
خبرنگار: شما در حال صحبت با رانندگان کامیون هستید. رانندگان کامیون در معرض خطر بالای از دست دادن شغل خود به دست هوش مصنوعی هستند...
🔴
پرزیدنت ترامپ: آن‌ها نیستند. شما نمی‌توانید شغلی پیدا کنید. ما بالاترین آمار شغلی در تاریخ این کشور را داریم.
🔴
ما آنقدر شغل داریم که در دسترس خواهند بود و بزرگترین مشکل، جذب افراد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/129907" target="_blank">📅 21:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129906">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها تو این چندساله گدا و گشنه شدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/129906" target="_blank">📅 21:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129905">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: مهمترین چیز الان این است که ایران هرگز سلاح هسته‌ای نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129905" target="_blank">📅 21:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129904">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ: هرکس که از توافق با ایران انتقاد کرده، باید آگاه و توجیه شود، حتی اگر از دوستان من باشد.
🔴
آنها مشکل گرسنگی دارند. آنها مشکل غذا دارند. آنها مشکل دارو دارند/تورم آنها ۳۰۰٪ است. آنها مشکلات زیادی دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/129904" target="_blank">📅 21:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129903">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3dc624529.mp4?token=tXreyml4gW-j_j2xuO_LhQjC5wujHNKgXd3w4aIxCcJ61nKM2mtZP36Dl9vKRZpfZ3y4dTNnurBisU-dmRfUsLukMjeyD3hluyCFvWYm7dPljGpSlo99fhxtg7XlC1IgGD7fe1MH-UQR8ZdR0kHH36p893_WjYsJ5fAzoaCBPVYjGtqwXrAxoDgb0dVEA78MmSBxRL0YO1mqJlFGcKM1Zay2yWYr2AM0WPxYbbTkuagNorLASz-BTz_thHQRC2SOADr6K-Xg70R3Dm-x6HRDRM61r7Y8sfaizEXRzPOLJv6D1-QLGnue7Ui8UZej1_1d_6-AXvDkCGQyZKgv1Zt5ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3dc624529.mp4?token=tXreyml4gW-j_j2xuO_LhQjC5wujHNKgXd3w4aIxCcJ61nKM2mtZP36Dl9vKRZpfZ3y4dTNnurBisU-dmRfUsLukMjeyD3hluyCFvWYm7dPljGpSlo99fhxtg7XlC1IgGD7fe1MH-UQR8ZdR0kHH36p893_WjYsJ5fAzoaCBPVYjGtqwXrAxoDgb0dVEA78MmSBxRL0YO1mqJlFGcKM1Zay2yWYr2AM0WPxYbbTkuagNorLASz-BTz_thHQRC2SOADr6K-Xg70R3Dm-x6HRDRM61r7Y8sfaizEXRzPOLJv6D1-QLGnue7Ui8UZej1_1d_6-AXvDkCGQyZKgv1Zt5ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران با بازرسی‌های کامل موافقت کرده؛ اگر غیر این بود مذاکرات را لغو می‌کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129903" target="_blank">📅 20:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129902">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66355597a0.mp4?token=ueD-9BZUk9V_O5ieOSdw-K_A4QtdHHYoLAuhD-jmpO3j7BZPtT298L7qPPr9CQqESy6ZvTcyOhsMDcws2wYWCaxFs76LfoCvmiTOI6mzzn_BbcD5RABfIEEwmBAa24djTUn7WPKwoN49_MlrvCNYzMY_FOtSvlaGUEWRHcpYWunj9RxgpH4PHpuC1gKMvCx4W-cmZNSOMTdw2aDH_4xAZXWfduxDcjKFTQwmtC4Qc_LF1q-zbq3q4OXAMpgH7VlIzcKWtwzUqdd7HzlDmYKt6b4qzCO7U0Ksu9QSi6m9_HEOyztm4NBQ94AhOcVFnxNzA76FlLPfsvmxGnk2XjtSSII-Jom2DvL_47UgjDbb0ojkpNdR_2cW9r8Uaq7i2fMH0CB5Qb8-2vHOcO-qkeZvj_cJQ-1dXdciLMAH8SXeAWhAL1BFSnrsjrrmWcMTn72uIxakvz-x3YVB-4omq7CeF98g0Wwo01-6fP_LtdX3LglSwmQg3T0s116Lt_ctJQV3Qo3T5WD7i3dcQjjXTHUU2a1-9D262DwHYdowOGUJ3IhmxjrWMNPkshZ_nfL3uTkiDrxsFb0XnIRvG-pC_ojmfWLiyk1sXVpHDfso1YXvYn_gkzlqOs5zGxHKvX3rFugZuaB56573DpClHmSm5ZZ7-D7J2oLnTnhkZvLjZf0pQVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66355597a0.mp4?token=ueD-9BZUk9V_O5ieOSdw-K_A4QtdHHYoLAuhD-jmpO3j7BZPtT298L7qPPr9CQqESy6ZvTcyOhsMDcws2wYWCaxFs76LfoCvmiTOI6mzzn_BbcD5RABfIEEwmBAa24djTUn7WPKwoN49_MlrvCNYzMY_FOtSvlaGUEWRHcpYWunj9RxgpH4PHpuC1gKMvCx4W-cmZNSOMTdw2aDH_4xAZXWfduxDcjKFTQwmtC4Qc_LF1q-zbq3q4OXAMpgH7VlIzcKWtwzUqdd7HzlDmYKt6b4qzCO7U0Ksu9QSi6m9_HEOyztm4NBQ94AhOcVFnxNzA76FlLPfsvmxGnk2XjtSSII-Jom2DvL_47UgjDbb0ojkpNdR_2cW9r8Uaq7i2fMH0CB5Qb8-2vHOcO-qkeZvj_cJQ-1dXdciLMAH8SXeAWhAL1BFSnrsjrrmWcMTn72uIxakvz-x3YVB-4omq7CeF98g0Wwo01-6fP_LtdX3LglSwmQg3T0s116Lt_ctJQV3Qo3T5WD7i3dcQjjXTHUU2a1-9D262DwHYdowOGUJ3IhmxjrWMNPkshZ_nfL3uTkiDrxsFb0XnIRvG-pC_ojmfWLiyk1sXVpHDfso1YXvYn_gkzlqOs5zGxHKvX3rFugZuaB56573DpClHmSm5ZZ7-D7J2oLnTnhkZvLjZf0pQVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: مسئله لبنان جدا از ایران است زیرا لبنان کشوری مستقل با دولت خود است.
🔴
ما قصد داریم با دولت لبنان مذاکره و با آن برخورد کنیم
🔴
آینده لبنان متعلق به مردم لبنان از طریق دولت منتخب و مستقل آن‌هاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/129902" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129901">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه امریکا، می‌گوید پولی از جیب مالیات‌دهندگان آمریکایی به ایران نخواهد رفت
🔴
این سرمایه‌گذاری‌ها در ایران از سوی کشورهای دیگر خواهد بود، در صورتی که ایران رفتار خوبی داشته باشد.
🔴
آن فرصت‌ها می‌توانند شامل سرمایه‌گذاری‌ها... سرمایه‌گذاری مستقیم خارجی باشند. این پول دولتِ ما نخواهد بود. این موضوع به پیشرفتی بستگی دارد که در زمینهٔ مجموعه‌ای از دیگر مسائل امنیتی حاصل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/129901" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129900">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa349112d.mp4?token=OeknRrsRfEjQ2L9XOFsUV7xNfDYAm27uKIU82YVqMPavOf3mB6G0VfoxMMvSI_Mpk0JARTu7Jhsv6OWw4y1zR_ys4jIOY9C9XfLGv7WtHCXGf2VjdUsWB4Podmxsb1ZKl0zJ75K0JELJ0d-k9forzJ-hxkiwqgHudo7umRA4pd1e16UufrdXUU24KOo8KIxTWopmtwyYCovSseX6iAHpO97UiPi404obwZp1QT5HdBT8g2Gbv62_WYIDGwX743jXyIb_pKhZD6QE358ledeORzpTBBJg7tNeu-90cH-lpUrOLgR5wUou97-BY1PzWXQ0o3GkRVKec1N_bqM4q2OvLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa349112d.mp4?token=OeknRrsRfEjQ2L9XOFsUV7xNfDYAm27uKIU82YVqMPavOf3mB6G0VfoxMMvSI_Mpk0JARTu7Jhsv6OWw4y1zR_ys4jIOY9C9XfLGv7WtHCXGf2VjdUsWB4Podmxsb1ZKl0zJ75K0JELJ0d-k9forzJ-hxkiwqgHudo7umRA4pd1e16UufrdXUU24KOo8KIxTWopmtwyYCovSseX6iAHpO97UiPi404obwZp1QT5HdBT8g2Gbv62_WYIDGwX743jXyIb_pKhZD6QE358ledeORzpTBBJg7tNeu-90cH-lpUrOLgR5wUou97-BY1PzWXQ0o3GkRVKec1N_bqM4q2OvLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: اگر ایران رفتار مناسبی داشته باشد سرمایه‌گذاری‌ توسط کشورهای دیگر انجام می‌شود
🔴
مارکو روبیو: این فرصت‌ها می‌تواند شامل سرمایه‌گذاری‌ها باشد... سرمایه‌گذاری مستقیم خارجی. این پول دولت ما نخواهد بود. این چیزی است که به پیشرفت در مجموعه‌ای از مسائل امنیتی دیگر بستگی دارد."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/129900" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129899">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
احمدی عضو کمیسیون آموزش:
تدریس هوش‌ مصنوعی از سال آینده وارد مدارس کشور می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/129899" target="_blank">📅 20:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129898">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
روبیو : یه سری مسائل هم خارج از اون توافق (MOU) هست؛ ولی باید روشون حرف زده بشه
🔴
ایده «پایان کامل درگیری‌ها تو کل منطقه» از نظرشون عملاً شدنی نیست
🔴
چون می‌گن تا وقتی گروه‌های نیابتی ایران از عراق موشک و پهپاد می‌زنن و در درگیری‌ها (مثل حماس و حزب‌الله)…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/129898" target="_blank">📅 20:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129897">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce086fb77.mp4?token=evuTRqVeebdA-iwN9yEkjo7yRTj8YlMO8E2W09wyg0ml_tMJgtzA2QjtSfEMaeyg8L1PAQ-5qE7xjd4WpLbJm8qgxpxyPmjd1aTjjevAyAoc8xTTR6ANZT-zqCkKg4_8iUfXxTMPCTu0aDV1JvvgQd11mm6WjZrQG-3HnIq_ASNH9vMf-k2Ex2Pbn2kUcWDcWTgMUNVvZeyZyZxWWx6UfaulY1m0mFj2JdvAThAWT95MfWIdIHhTd4DR5oH8VZD4iuceftW6VBKApDAEPwZ0Bx_4TGEK7ZTtvWWHKpovHenxlZ_-jc0wQ3uHX_09aKER_THZWK4j5pO3AfQ8bMQO3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce086fb77.mp4?token=evuTRqVeebdA-iwN9yEkjo7yRTj8YlMO8E2W09wyg0ml_tMJgtzA2QjtSfEMaeyg8L1PAQ-5qE7xjd4WpLbJm8qgxpxyPmjd1aTjjevAyAoc8xTTR6ANZT-zqCkKg4_8iUfXxTMPCTu0aDV1JvvgQd11mm6WjZrQG-3HnIq_ASNH9vMf-k2Ex2Pbn2kUcWDcWTgMUNVvZeyZyZxWWx6UfaulY1m0mFj2JdvAThAWT95MfWIdIHhTd4DR5oH8VZD4iuceftW6VBKApDAEPwZ0Bx_4TGEK7ZTtvWWHKpovHenxlZ_-jc0wQ3uHX_09aKER_THZWK4j5pO3AfQ8bMQO3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: بحث موشکی در تفاهم‌نامه نیست و هیچ‌وقت وجود نخواهد داشت
🔴
اگر موشک‌های ما نبود اسرائیل و آمریکا ایران را مثل غزه شخم می‌زدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/129897" target="_blank">📅 20:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129896">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed9cc22773.mp4?token=skMKXcfh5jcD0J72ef7nKKwHnSEZQUjMzgb2if4Dfty9OuUCWFy_yhmFfWg-KWS8U_o_LCYVPKfDUJ2kihf6TFxrr23vNJM8HIdpfvfJ5bJx1gVdaSxuyO8yn9vvAJvBtV2tSOSPcsRMl0x5BKJKXS0NMf3Jtk6ThX8dp4TpXviD4bgzUEpe0icUNdSYTH6chKYp0nT9U0x8-6E-32A753hvnincq0mMDQsKXjhpssQ3GJvXdMhzSKaMxi3V2-kF4BKm7_3B-8WFiq-v1u_8YNpRVcRz-CYF9dcyJX1yA_3YDjsIgZySw4b1XNqGtPXKl3Kr1nXsA0iVpxdLtoeBQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed9cc22773.mp4?token=skMKXcfh5jcD0J72ef7nKKwHnSEZQUjMzgb2if4Dfty9OuUCWFy_yhmFfWg-KWS8U_o_LCYVPKfDUJ2kihf6TFxrr23vNJM8HIdpfvfJ5bJx1gVdaSxuyO8yn9vvAJvBtV2tSOSPcsRMl0x5BKJKXS0NMf3Jtk6ThX8dp4TpXviD4bgzUEpe0icUNdSYTH6chKYp0nT9U0x8-6E-32A753hvnincq0mMDQsKXjhpssQ3GJvXdMhzSKaMxi3V2-kF4BKm7_3B-8WFiq-v1u_8YNpRVcRz-CYF9dcyJX1yA_3YDjsIgZySw4b1XNqGtPXKl3Kr1nXsA0iVpxdLtoeBQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان دکترای افتخاری از پاکستان دریافت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/129896" target="_blank">📅 20:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129895">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
روبیو : یه سری مسائل هم خارج از اون توافق (MOU) هست؛ ولی باید روشون حرف زده بشه
🔴
ایده «پایان کامل درگیری‌ها تو کل منطقه» از نظرشون عملاً شدنی نیست
🔴
چون می‌گن تا وقتی گروه‌های نیابتی ایران از عراق موشک و پهپاد می‌زنن و در درگیری‌ها (مثل حماس و حزب‌الله) نقش دارن، نمی‌شه گفت تنش تموم شده
🔴
برای همین این موضوع هم داخل چارچوب مذاکرات می‌مونه و بعداً روش تصمیم می‌گیرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/129895" target="_blank">📅 19:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129894">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیر خارجه آمریکا، روبیو : موضوعی که همیشه مطرحه
🔴
اینه که الان یه مسئله مربوط به ایران درباره لُبنان وجود داره و اون هم حمایت و پشتیبانی از حزب‌الله
🔴
این موضوع هم بخشی از گفت‌وگوها با ایرانی‌ها خواهد بود
🔴
اما درباره آینده لُبنان، این کشور متعلق به مردم لُبنانه و باید از طریق دولت منتخب و حاکمیت خودش تصمیم‌گیری بشه
🔴
ما هم قراره با همین چارچوب جلو بریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/129894" target="_blank">📅 19:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129893">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36127e8772.mp4?token=g442y_qPDggp1PGO9Bu4Kk4B4ZIdMbW287oOgjlVAbt7hdr1ZLpUYEoXyyYroLdJ3AaV2P1xce4kvtic2chVCodTlvaM3GJBgLJSpfHA8NU1cNiSCPk61Qb-MzS0GkZXvgLKgIJw_5TMOvAbGweGdS-cm17MnlL2Zy8phFtyT0wP4NxVfe45DmUpPOgdmNu7sGsl-P0SeQ0TbyvWqPo7SIf-bRXtinbsA4Kjd1vwwN3EXRImRMdNSDDXpTHFFdICWrx44EkoxgL2mqxrWz1rLCPihKhUncIk-NgBjtB1zQ16uPSEzdPrpv-JgqWVepx_IzhxDjKMgu1hOGUX49I5Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36127e8772.mp4?token=g442y_qPDggp1PGO9Bu4Kk4B4ZIdMbW287oOgjlVAbt7hdr1ZLpUYEoXyyYroLdJ3AaV2P1xce4kvtic2chVCodTlvaM3GJBgLJSpfHA8NU1cNiSCPk61Qb-MzS0GkZXvgLKgIJw_5TMOvAbGweGdS-cm17MnlL2Zy8phFtyT0wP4NxVfe45DmUpPOgdmNu7sGsl-P0SeQ0TbyvWqPo7SIf-bRXtinbsA4Kjd1vwwN3EXRImRMdNSDDXpTHFFdICWrx44EkoxgL2mqxrWz1rLCPihKhUncIk-NgBjtB1zQ16uPSEzdPrpv-JgqWVepx_IzhxDjKMgu1hOGUX49I5Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعرخوانی شهباز شریف به زبان فارسی در حضور مسعود پزشکیان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129893" target="_blank">📅 19:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129892">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شهباز شریف:
این تفاهم‌نامه به موشک‌های بالستیک اشاره‌ای ندارد. این موضوع هرگز در دستور کار نبوده است؛ هرگز در دستور کار قرار نگرفته است.طرف ایرانی هرگز حتی تمایلی به بحث درباره آن نداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/129892" target="_blank">📅 19:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129891">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: آیت‌الله سیدمجتبی خامنه‌ای، رهبر ایران، را تحسین می‌کنم که در این شرایط حساس ایران را رهبری کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/129891" target="_blank">📅 19:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129890">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نخست وزیر پاکستان:  کارشکنی هایی وجود دارد که می خواهند تفاهم نامه بین آمریکا و ایران را از مسیر خود خارج کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/129890" target="_blank">📅 19:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129889">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
بر اساس آخرین گزارش بانک مرکزی، رشد اقتصادی کشور در سال ۱۴۰۴ با کاهش منفی ۰.۷ درصد، منفی اعلام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129889" target="_blank">📅 19:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129888">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان: تفاهم‌نامه امضاشده میان تهران و واشنگتن ظرف شصت روز آینده به یک توافق بلندمدت تبدیل خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129888" target="_blank">📅 19:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129887">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/187ae17961.mp4?token=BH2fUWcICTqi-DggHmj3egvlrh0CsKhQW3n_auSDNvZwjgiaEu7Zf1M-TN2kwCj6ZsA7Tk7-QzWtdYkRfak2SAiFUGjGFn67qaGzfTWLgDrepPGvBP37zJNjVImftbrHNCMpzK4Bb2br8JX2eOq8vqTHZz-PolnlcRYkZ2EHgQ3EGZurpAa1OTM2RGDpRjDHsVZVRRpugzNLL4GSpSscoiPYxbqG8L3rc9fHPZsylRBnIbxx4rqyVD8o1KeQKkpfZsq9dsksjHjt1grLgwsISOi00kbMZcN0RY5iwURZOYXuqNxPQ6em4VPR3RleO55zZCVN0P2nou8qPHPt6eOPJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/187ae17961.mp4?token=BH2fUWcICTqi-DggHmj3egvlrh0CsKhQW3n_auSDNvZwjgiaEu7Zf1M-TN2kwCj6ZsA7Tk7-QzWtdYkRfak2SAiFUGjGFn67qaGzfTWLgDrepPGvBP37zJNjVImftbrHNCMpzK4Bb2br8JX2eOq8vqTHZz-PolnlcRYkZ2EHgQ3EGZurpAa1OTM2RGDpRjDHsVZVRRpugzNLL4GSpSscoiPYxbqG8L3rc9fHPZsylRBnIbxx4rqyVD8o1KeQKkpfZsq9dsksjHjt1grLgwsISOi00kbMZcN0RY5iwURZOYXuqNxPQ6em4VPR3RleO55zZCVN0P2nou8qPHPt6eOPJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ثابتی: تنگه رو مفت باز کردیم بدون اینکه هیچ عوارضی بگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/129887" target="_blank">📅 19:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129886">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نفتالی بنت، نخست‌وزیر سابق اسرائیل:
ما در دیپلماسی عمومی بدترین در جهان هستیم. اگر اسرائیل یک شرکت روابط عمومی بود، قطعاً ما را استخدام نمی‌کردم.
🔴
با احمقانه نبودن شروع به کار کنید!
🔴
بن-گور چیزهای بی‌معنی و احمقانه توییت می‌کند تا قوی به نظر برسد، و سپس من باید در یک دوجین مصاحبه در سی‌ان‌ان و بی‌بی‌سی برای پاک‌کردن این به‌هم‌ریختگی وقت بگذارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/129886" target="_blank">📅 19:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129885">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ریاست جمهوری لبنان: ونس و وزیر خارجه آمریکا تأکید کردند که آن‌ها پیگیری اجرای تفاهمات مذاکرات سوئیس، از جمله تشکیل یک کمیته مشترک متشکل از ایالات متحده، لبنان و ایران برای تثبیت آتش‌بس در لبنان و نظارت بر اجرای اقدامات مرتبط را ادامه خواهند داد
🔴
آن‌ها گفته‌اند که ترتیبات مربوط به حوزه اختیارات این کمیته و نحوه تشکیل آن، در دست بررسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/129885" target="_blank">📅 18:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129884">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvVMOQCRK9wO2JaZNBFASKRSv6VrCuX4QuecPLP_Bq8oLeeYjLcNPg2ZwKw4zaN6bLIn_PrpagDabSOapmPrtxEegQVS6387Xu13UNuwbynmNk3o6km1PZaQI0yv2G_w4rDHhX2vfrfCevFWXCadPP7tqncSVjUyghZngitbYnkcaT7v__0mlJM8cqRPPOS8dyE7ctSM0LD1PLrsmdLQMlCLUsuq9gsGOcdwS3MowLp1dCs5G-J4CnrmREPPXqPRkjmFM3oCPcO-aKiqgo0C2ouhLah1g13xCHaNNs3TNRaBtwjZkJfofcJKy_Qr6GQc_s80Dch3dUzmgdW5ncD-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: مردم نگران نباشن، یکشنبه قطعا جلسه مجلس رو برگزار میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129884" target="_blank">📅 18:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129883">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
به علت گرمای هوای ۳۲ درجه ای در فرانسه 18 نفر جان باختند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/129883" target="_blank">📅 18:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129882">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYr3dkrPQc6Q73Y--EGCqjgOEImbTuXQjSCW4KwWmLg3n7BGBairmXC0rr3lHbl5pFt4bMm0TSvYxCFiVunRAf6uE3Z7Es6Y2fEKguWMv6my-d3OIPKSBzN3SXO5ULgLhf5rEx2zq7DCNXOixDBVUc3pXajy8XoHpL8N9nzij4QQPD2lEizXwTZ7ZhkMgewHaCtZYIHh8CcQklqrfNw2OO0UTbV4fWNfw2P2kmqIaSbemJPiQvZfLDOYgrW62ML-bJABEdUXf1mbrdmxEG41vX2ZwxbseCyddNA4EvxCfLUQW7iVFAfChS75YpiUBmw2J82uaNvAZPSmgc2JBWSe9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی: رهبری با مذاکرات مخالف نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/129882" target="_blank">📅 18:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129881">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxHWuNXg-2KZ7nUKmnro-5cYQs31qQGEtlejUIGrOk944hQ5RcnT1DJKwAb_nt6zDuDSbY1S2LzFc9JbuQhe21oI2OkRaW3H5_-wIRzJlz9GgEMRNFvvAVR2OmWuReUh9d-wy6C-a68xAOKFmcgq6SgJURvqUqks3L4zl6u60qISEFGN1hZGIDsEyFhOtxQLhlsMDu9vGImiT8n0WAzvq2nYixF0IjWPNHaKGJtn5z35gd1ldAorxggYBzR6xHAxbf8f2k3MgQKk_GY6Z-nnyL2q8HaW-43__gkhw6zaxySZ4rkLTAvxYuDDv3wiDsACCEquRAoFVMD5md0ugkTNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور لبنان، جوزف عون، خواستار پایان «اشغال اسرائیلی» جنوب لبنان شد و گفت که کشور او «کمتر از» خروج کامل اسرائیل را نخواهد پذیرفت.
در بیانیهای که از سوی دفتر او منتشر شد، عون ابراز امیدواری کرد که دور فعلی مذاکرات در دستیابی به اهداف لبنان، از جمله بازگرداندن حاکمیت کامل بر تمام خاک لبنان و گسترش اقتدار دولتی در سراسر کشور، «تصمیم‌گیرنده» باشد.
او افزود که «تنها انتخاب ما حاکمیت ملی ماست» و دولت لبنان باید به تنهایی مسئولیت محافظت از تمام شهروندان و تضمین حقوق و آزادی‌های آنان را بر عهده بگیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/129881" target="_blank">📅 18:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129880">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INR7hpkUHYAoTPs3gl1pYw17Zz3V9UKptKcSAG4SBT5sWga93Ldrctobg1zJF8ozLnOu50q3k2aQfC0_RU4LfM0ayWploqijCRIWTLn3aYW_6kl7ez7jlm5hefsxpft9tRKKM4omu3prISYsbkydEPxyz0N38YqZ3dFJMZB4RxDMj_Bx_uPyqH-0Tlbfvb10KS5sJZDShG3ncP7rddEb7kgPN84ZH9bpp_lChAQIKt8Fx6mHl8NRYo9-DYoGa0vZJE9UUzDJvmFbSV06G0swDqJ54KYjiksa2lT80poPCMbmFQqdruzP-y5PeakfkyU8lVsZX4NNEgOcF7O1hQxYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
ناو هواپیمابر USS جورج اچ. دبلیو. بوش (CVN 77) در دریای عرب در حال حرکت است.
دو ناو هواپیمابر به فعالیت خود در خاورمیانه ادامه می‌دهند در حالی که نیروهای آمریکایی همچنان حضور دارند و هوشیار هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/129880" target="_blank">📅 18:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129879">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
فایننشال‌تایمز:
با وجود افزایش سطح تردد کشتی‌ها در تنگه هرمز، مالکان همچنان سردرگم هستند؛ این وضعیت در حالی شکل گرفته که ایران کشتی‌ها را تهدید به عبور از مسیر نزدیک سواحل خود کرده و آمریکا مسیر عمان را پیشنهاد می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/129879" target="_blank">📅 17:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129878">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed01390a1c.mp4?token=pYUzNMpz-gnjzp--nwiuj58j9kqGJDZWUQT6tFbVhjc6PGVEmNjgNUmXkCmOudMDfLyJVPzYRuREuv4W1AkwHVlcS2UPsfapeHcEOnQ5tlCxtRuBxBBC-XICejtODa0kYkZ7hf0u36nPWQFOM5AtkC_6NwV3EWCRizpYj8ukYIBapH2MS1hddxNT3o6CiFqoI6sSHcOSimdme0XwrMR2xdjVzszSAZiLzP3KGERHjyU3CKGDEvND89jJNw1tiaczbts8J_tEJ8N5h43718Oq-B1X69Hv6kz6pk8krrH1PaPvRBitq2xhhWrvBI71ZC0ow6YsCPjtTYXDYapoaM249w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed01390a1c.mp4?token=pYUzNMpz-gnjzp--nwiuj58j9kqGJDZWUQT6tFbVhjc6PGVEmNjgNUmXkCmOudMDfLyJVPzYRuREuv4W1AkwHVlcS2UPsfapeHcEOnQ5tlCxtRuBxBBC-XICejtODa0kYkZ7hf0u36nPWQFOM5AtkC_6NwV3EWCRizpYj8ukYIBapH2MS1hddxNT3o6CiFqoI6sSHcOSimdme0XwrMR2xdjVzszSAZiLzP3KGERHjyU3CKGDEvND89jJNw1tiaczbts8J_tEJ8N5h43718Oq-B1X69Hv6kz6pk8krrH1PaPvRBitq2xhhWrvBI71ZC0ow6YsCPjtTYXDYapoaM249w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیت الله العظمی سید صادق شیرازی، مرجع بزرگ شیعیان: در دوران پیغمبر و امیرالمومنین یک نفر کشته سیاسی هم وجود نداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/129878" target="_blank">📅 17:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129877">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
عاصم منیر به دیدار پزشکیان رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/129877" target="_blank">📅 17:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129876">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
واکنش تیم مذاکره کننده به مذاکره موشکی: خلاف است و از اساس تکذیب می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129876" target="_blank">📅 17:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129875">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb7Yh7C68GnD64Doy5VKyK1HN2ufZbeeaPg_hgLwG-qhRTq0qRuZZbK1uKAPPZnaT7i9PP8EkBZWUVP8CJ7GtQw1EbmoDMH1h9icAJWi5EgSLV8Y6DLmN4XEkGCw87No0SJhikUGsdTkvtswpacxqX1PWeBVvK18uR4S6Rt8jdnDX82VcSC4OWdLLuf-vSTfzc1ng0A8PN5mZRyMIF9yrir5Sb64lx2UZY7CNmYZnKtlxkuXfcWzCHzJT5jjPK37AKAuAyFQSKP9Fl-EsPTxSb1F8ubj09ejYVlOZZYW_9F033ILVd4ppaNQB8URPAJkFDDIJ7ME6eza9wl1hB2wPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت‌ها در بازار طلا، سکه و ارز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/129875" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129874">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AadpCUku4RkIgi2B7EQ5I8wXr5MXNLnlfU70bR9JJIzKqeYh8Fgnf3O-o--hFPr3Auy8RHsGTbkQ2IPRjDhkKXOq-grpvQJqQODApf5E01kXR5VVlp9Sa6vEuAJLypM35pce7s0zPXHdABpE5F4_l1cD3qgIBNhq9KF4EJqBIk5qnOZQx5855Z5dqPaLdWtqJJTA0MTISDdNIOKmJXmbF2kx7oWa-9uwxlPphu2adZK6JwCgGhSDl_sudbSCn96D8sE_W8uQ2L1BeIOKh2cTY45Kn__NjxhKAYq_7-0thc3q3217XrenOxxN40geFRJl3DQS_adaHVeDEIJ2T0HcSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست در تازه‌ترین جلد خود، توافق ترامپ با ایران را به تمسخر گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/129874" target="_blank">📅 16:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129873">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
العربیه:
"سعید ایروانی، نماینده ایران در سازمان ملل‌ میگوید انتقال اورانیوم غنی‌شده ایران به خاک روسیه، یکی از گزینه‌های روی میز در مذاکرات است."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/129873" target="_blank">📅 16:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129872">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQYNC_jVt8YcmYFJ2UFtNTBfeGG_7TSlqW59F7JXpp4Ikpr1wjP3vnlLxEAcOGIcYJgFTj9qbtiEIX0vGQd7jWsTSoKrnE_RVPHFm9BOU_ouwPPenbz1iPo1JAxeMRU6dw8HLyRkdQGKf-Kza0EPOvPkofAHzE94fOYkcE_Uxtz_cQHV20qirBgXHyBmhthdWfi7QE4WY6BVI0-j4WF0cNHa70ltd9h8VEPlwnoHmW7u-vtcIgkEGuPwHGV0qps6mEdpQmjOQWQu1cft5CE1v8cDDCCYN-i01VOGimpftoeWXY5xmncSjEaczQkYtqXhR9prhPh_b1Yu5TRBW-Vydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجلس از عملکرد عالی وزیر ارتباطات در ایام جنگ تقدیر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/129872" target="_blank">📅 16:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129871">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16bfcc9aaf.mp4?token=MAJo-iDmbBVnPJPc9iDfiHgh7L8wftHc5gppkal0xLZydalrSLjcD9ppuVUYdM67wq5upcai_dJpKsusHf2xzgzbSQhZ1YNb_Xm7deXgYiYmIrbW8k7CT9l3F4b_AF0w2g9Rf2Tq74NvinKcnlZjaW4K1XT-LrbYE067okT4IF3TP-rvxWlpPqXpFEHlJFxenatWq4Y8Tsvuct3XoRGVgtI6jysl7KTuyonXZ9PIFVqcWAZOgFKbi3eWEvKa68qBi4k1YH5JKtXJe8xKh0OyqVHnYlmqo7snw5IAcmZNg99tN6xcRX4bDBr_mSKKXZZzTZQTUQ44w835qhq8mvjIbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16bfcc9aaf.mp4?token=MAJo-iDmbBVnPJPc9iDfiHgh7L8wftHc5gppkal0xLZydalrSLjcD9ppuVUYdM67wq5upcai_dJpKsusHf2xzgzbSQhZ1YNb_Xm7deXgYiYmIrbW8k7CT9l3F4b_AF0w2g9Rf2Tq74NvinKcnlZjaW4K1XT-LrbYE067okT4IF3TP-rvxWlpPqXpFEHlJFxenatWq4Y8Tsvuct3XoRGVgtI6jysl7KTuyonXZ9PIFVqcWAZOgFKbi3eWEvKa68qBi4k1YH5JKtXJe8xKh0OyqVHnYlmqo7snw5IAcmZNg99tN6xcRX4bDBr_mSKKXZZzTZQTUQ44w835qhq8mvjIbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی دوتا دسته میرسن به هم
مداحاشون:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/129871" target="_blank">📅 15:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129870">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزیر قطع ارتباطات:
تا زمان عادی‌شدن کامل شرایط بانک‌ها، خدمات مشترکان تلفن همراه و ثابت به‌دلیل پرداخت‌نشدن قبوض، قطع نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/129870" target="_blank">📅 15:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129869">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
لیست بانک‌هایی که همچنان با اختلال مواجه هستند:
ملت
تجارت
کشاورزی
ملی
صادرات
دی
بلو
کارآفرین
اختلال
❌
نفروختن دلار و طلا
✔️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/129869" target="_blank">📅 15:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129868">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
شهباز شریف: توافق ایران و آمریکا یک تحول خوشایند است
🔴
نخست‌وزیر پاکستان: پیشرفت مثبت بین دو طرف، نه تنها برای خاورمیانه، بلکه در سطح بین‌المللی نیز یک تحول خوشایند است.
🔴
توافق ایران و آمریکا گامی مهم در جهت تقویت امنیت و ثبات در منطقه است.
🔴
مذاکرات همچنین…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/129868" target="_blank">📅 15:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129867">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
زنده از ادمین ارسالی به کربلا/آزار و اذیت شش امامی‌ها توسط دوازده امامی‌ها در حرم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/129867" target="_blank">📅 15:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129866">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc6uyyC1YTQU8YSk0HmQhSjCjghmCgmJiwGZolPafD9YGHNdxkcQOrgecKYnKJdw-xBoK8BNqavNAwdN5xyghwxuAxp8Ku6anwMkag8_5iSTVhqDSOHfAB3SHp315R4xqM36Ja0Lpw_vr-_K5MOd1yqAlbcIHoKH-3J2CQ54PuHkciXjvStjgaVrLH6hwszDoMR13bLBqr9sHJT0-z16onPNZmHn34o81omAOGGW6s0T8atD4wsuwhqKHnCobCnMyz7yfUNZ-GvRd8XWFO83Znq3K13ExvXDnLsRRE6o3YFc_Tvuyi-Xa8TWYSCJ0bxsor8TvorWN_G5gYwpKaMSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لحظه ورود عاشقانه پزشکیان به پاکستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/129866" target="_blank">📅 15:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129865">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=RmSgShCdJR7_XwiQRKqUvddHOUeihQuVNU32EsMoXqyTGvaVzpnpfE24Pwjp6UQJbWiqJ9h_yljDBwA13d7UJ9TkMxrd0YTZA13M08ECjDwzY2By-mbogs-fCLOk4RyjLFtTrbr6_3vEaWQjJz4zyGbOHH92jYMBcG4aKvQ-Gmr5GH_EMO751AHPxENztOxQeRwRgFQnEwLI7klTRKGsrTfgTGB5rHvCWHzFjXPEJS3pUeRZ707Ul3Za7B8bvZt9JQ3VECP_pKX2DhEwlsZUUcClSDribbT87FCDvUEw8YYNzneT8wIsym8yRAZg4GxMhj1hkRRG-m4UnHJ65zbHFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=RmSgShCdJR7_XwiQRKqUvddHOUeihQuVNU32EsMoXqyTGvaVzpnpfE24Pwjp6UQJbWiqJ9h_yljDBwA13d7UJ9TkMxrd0YTZA13M08ECjDwzY2By-mbogs-fCLOk4RyjLFtTrbr6_3vEaWQjJz4zyGbOHH92jYMBcG4aKvQ-Gmr5GH_EMO751AHPxENztOxQeRwRgFQnEwLI7klTRKGsrTfgTGB5rHvCWHzFjXPEJS3pUeRZ707Ul3Za7B8bvZt9JQ3VECP_pKX2DhEwlsZUUcClSDribbT87FCDvUEw8YYNzneT8wIsym8yRAZg4GxMhj1hkRRG-m4UnHJ65zbHFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن
🔴
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
🔴
فقط اونجاش که گفت الکی الکی رفتیم سمت دروازه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/129865" target="_blank">📅 15:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129864">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4XwEMuOlZNvomy9uQ9DZDeQi7vxSdv591TDMRmLNnTMchXruKyxQhvZoYNayZVZXE1z5lzElxq9jTY2ddWS2ZwDqDnkTpUlUKzGCfrBM5sC4yf4EcZTk95I5P5fpd9-HgHVC2OWRYoOQlPHa_kMFPRNn4-MZrHK0RZmy0Smfvl9idX_MbqAMIcjyHDHNuHDzbTbwaoDvXW2Qi2En57H303aq8xzWVWfL2EF8EkPzPVHDDkOPTXHtXvSOoc8wxUndZtYDNipGKF_ULDiAqPmr_CL5snB_J2ooev27fF5tK-FVQpWjrZjCEBuD1ZHilS1Iz1sd5p7fxDUV1ZBpuQyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دیروز 19 میلیون بشکه نفت از تنگه هرمز عبور کرد
دونالد ترامپ در تروث سوشیال:
🔴
«دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز خارج شد که یک رکورد تاریخی است.
🔴
قیمت نفت در حال کاهش است و جهان مکانی بسیار امن‌تر شده است!!!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/129864" target="_blank">📅 15:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129863">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
زنده از کربلا/بیرون کردن شش امامی‌ها توسط دوازده امامی‌ها(اکثرا عرزشیا)
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/129863" target="_blank">📅 15:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129862">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e336ac3a.mp4?token=N1vHyyC8o35ClglHvEZ4ADVRLDnHcZQGB3mgOAnqUgHwWhJtfhaFo5NFOUXf82f5EbL8NqbBbHZsAQbyvtvGv0muDfIwIFjn2bR7nInkF5n5dasZ-SpWQZ7urbbfLE0woqzu6fKWZgGRmCrxaUC2uHzm1BJ9j2jTzpuraSn209s-vMfMkkIatt0sSihAc2W8qhP6KtlK32D8-jMJ0YYCcd1MOy53h17bio3rPNJpjgil2Tyydh2Kd5Cbqp-LKtWJbO_KngMdHmcvJp-mYVQ47d-VjYGiW8VijpgoFZ0thB_rTR7jTLkkqfT8ew8EnVfmeydAkpNCju3eh5WFnfw1wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e336ac3a.mp4?token=N1vHyyC8o35ClglHvEZ4ADVRLDnHcZQGB3mgOAnqUgHwWhJtfhaFo5NFOUXf82f5EbL8NqbBbHZsAQbyvtvGv0muDfIwIFjn2bR7nInkF5n5dasZ-SpWQZ7urbbfLE0woqzu6fKWZgGRmCrxaUC2uHzm1BJ9j2jTzpuraSn209s-vMfMkkIatt0sSihAc2W8qhP6KtlK32D8-jMJ0YYCcd1MOy53h17bio3rPNJpjgil2Tyydh2Kd5Cbqp-LKtWJbO_KngMdHmcvJp-mYVQ47d-VjYGiW8VijpgoFZ0thB_rTR7jTLkkqfT8ew8EnVfmeydAkpNCju3eh5WFnfw1wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زنده از کربلا/بیرون کردن شش امامی‌ها توسط دوازده امامی‌ها(اکثرا عرزشیا)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/129862" target="_blank">📅 15:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129861">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7TMIMtn8KuccdF1UhFzBT4Jya4-JbEFb2ad50cPBJesnFb60BFqJ8VFxghh5mPYo8jxAI12Kf14vH3Vcd2LiQAJiDBpJ8NEn9weP7aPDLWebYbk6WxLBAjhdtPacP8noL1S4XFvUI5IAoL22ZEzUcm4e_ZfLOIDwntmH_W4UMi5O7r2bS_tQfmb8TaiZSful3vrIcJafszdFnMbVaqsGyoR57mR7A7DBYDWMRxMdw07u3OhkR9EvlKv21hnBhGtotRajAAaah3dBX6Ns_xUOPlvPEMi94yk0ZD78iRgHl3C11NM5BSc9iZ6xRmsk8sjgNXJriKMmus6EBoZmrQY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: با وجود اعتراضات آنها و اظهارات نادرست درباره‌ی خلاف آن، همراه با تبلیغات گسترده اخبار جعلی که تمام تلاش خود را می‌کنند تا پیروزی آمریکا را هرچه کوچک‌تر و بی‌اهمیت‌تر نشان دهند، ایران کاملاً و به طور کامل با بالاترین سطح بازرسی‌های هسته‌ای برای سال‌های طولانی آینده (بی‌نهایت!!!) موافقت کرده است. این امر «صداقت هسته‌ای» را تضمین خواهد کرد.
🔴
اگر آنها با این موضوع موافقت نمی‌کردند، هیچ مذاکره‌ی بیشتری صورت نمی‌گرفت! بر اساس این و دیگر امتیازات بزرگ که ایران داده است، من موافقت کردم که تنگه هرمز باز بماند، بدون هیچ محاصره دریایی بیشتر.
🔴
با این حال، همه کشتی‌ها در محل باقی می‌مانند در صورت نیاز به بازگرداندن محاصره، که در حال حاضر بسیار بعید به نظر می‌رسد. پول و/یا تحریم‌هایی که خزانه‌داری آمریکا آزاد می‌کند، به صورت سپرده مشروط تحت کنترل آمریکا قرار می‌گیرد و برای خرید مواد غذایی و کالاهای پزشکی، منحصراً از ایالات متحده، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما استفاده خواهد شد.
🔴
این‌ها چیزهایی هستند که ایران به شدت به آنها نیاز دارد. این یک بحران انسانی است و من ضروری می‌دانم که اکنون کمک کنیم، قبل از اینکه خیلی دیر شود. مذاکرات خوب پیش می‌رود!
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/129861" target="_blank">📅 15:00 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
