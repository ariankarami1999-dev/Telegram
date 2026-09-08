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
<img src="https://cdn4.telesco.pe/file/O09Lk02bvORMsBNhKxcrzcS6JO_t9OhFhUGZzyXHFAaeWk8H75L9eCD6euCTu_RzMCd6EswLcEf8s4pU1TRwG6muryiXD7ynJAKVYrCHPW4cxAsjBNPUrHf8qgSOLeINL6EK19GMDZWL15idwssn-QmBIAIfH8vX2pg_qV-1V6knavnUh1sZ3CyTQS2Yt6ZRrOIR7mHznp5pal8vckfZ5LIenvGbBhTWQHJ-kVaYanqN0S6CYSp6jLsh-2zyE_tN2W9o7jBmw9usF4ILXr5JdZ6HSBAsjbXKLzTpBuHp_n2h2oQjkkvOVBirPB-RBS0mCER6xZzxzt7GdzXXUsnWWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 449K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 21:28:15</div>
<hr>

<div class="tg-post" id="msg-22567">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/withyashar/22567" target="_blank">📅 21:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22566">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S14Gqud64XcK_-Z78XVDWS7Urv2brqqAlqBH_VtJ8q1iLUIZ_bpMA8dAp5lFH_a1UJsa9wN36RgJOFWlN-3EJ9hWZQ9wraorIJiG-BBjFwWJXXhBwjTv619fgKMFwAfPmdIAhwK8_Bst3kj3Vr2L8tqOU3pCqjHCVk-7NdTVzAQK0W6OJoj_wHtGyZOhvqXa0hiAcoHaLlvc3lr1Vvmjw9nGmjPLcC1pYt8-D54OJa3911kfvTBiUQsWOJPnViLGSoMHT8iXJwho7I9uPzxckF0GZ4Bi8Ohsd6EcNi1sWhyrtCHFj4wLkJfIjSuT1mo4DD6OdOTjIceyQnkXKvCelQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپل فردا، چهارشنبه ۹ سپتامبر، رویداد ویژه خود را برگزار می‌کند و انتظار می‌رود از آیفون ۱۸ پرو، آیفون ۱۸ پرو مکس و آیفون اولترا؛ نخستین آیفون تاشوی اپل، رونمایی شود.این رویداد
ساعت ۲۰:۳۰ به وقت ایران
آغاز می‌شود. آیفون ۱۸ معمولی، آیفون ۱۸e و نسل جدید آیفون Air احتمالاً در مراسم فردا معرفی نمی‌شوند و عرضه آن‌ها به بهار ۲۰۲۷ موکول خواهد شد.
نام «آیفون اولترا» برای مدل تاشو هنوز به‌صورت رسمی از سوی اپل تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/withyashar/22566" target="_blank">📅 21:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22565">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c4dcb0a04.mp4?token=F-K9N-oCHWkWpBJ4lSg1LVRkZvyRasEKmRrzcfGfjQZMu6Y8MKJxgJwRe3OoA40BsZuf18jVL_-dPi2xJNk4a0dPkwfr7Tw7waFYyQQfqTynEjuszSM0w1OrhmxWruhcfbf4C5m5IocJWLDBjXG_POn3asvz8IC2lkvzWZWBojiSxLNe420Sq8gXQtTY_MPxD315cW2tMtgDtZZEWoNwYukigVaDWvKvGY_NHLUNn2FZCVNnOSYAKpFljB2kjmanV2COmeWTO0wD9mRIIqWtm8Q1GcItbzOnw-gFrbMPU0ECrVvhPrF5GzaDiKxow3tnOs558q2PCpq-57u52GqaUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c4dcb0a04.mp4?token=F-K9N-oCHWkWpBJ4lSg1LVRkZvyRasEKmRrzcfGfjQZMu6Y8MKJxgJwRe3OoA40BsZuf18jVL_-dPi2xJNk4a0dPkwfr7Tw7waFYyQQfqTynEjuszSM0w1OrhmxWruhcfbf4C5m5IocJWLDBjXG_POn3asvz8IC2lkvzWZWBojiSxLNe420Sq8gXQtTY_MPxD315cW2tMtgDtZZEWoNwYukigVaDWvKvGY_NHLUNn2FZCVNnOSYAKpFljB2kjmanV2COmeWTO0wD9mRIIqWtm8Q1GcItbzOnw-gFrbMPU0ECrVvhPrF5GzaDiKxow3tnOs558q2PCpq-57u52GqaUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : آمریکا نمایشگاه هوایی زده رو تنگه حدود ۱۰ سوخترسان ، پی۸ ، پهپاد و…. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/22565" target="_blank">📅 20:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22564">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoorena</strong></div>
<div class="tg-text">سلام یاشار رفتم خونه پدربزرگ دیدم هی داره پزشکیان رو فحش میده بعد فهمیدم بخاطر پست هایی که مخصوص دارن گرونی رو میندازن گردن دولت پزشکیان به همراه همه این بدبختیا انگار این گرونی بنزین یه پروژه هست دوباره برای هدایت خشم مردم به سمت دولت و نه رژیم مردم باید خیلی هوشیار باشن</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/22564" target="_blank">📅 20:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cadaeb8025.mp4?token=jo2-wqwD8c2JoLIECDSR5pYOoscvyvQ_s35G8pMEDu2iJM6zJPmFekNU_UfXZnEkbheuGCFcjCvTrwg0u87bve9GH5wKIZ-GCAYbsE26JRb35bUUwRl3hjonaNyzGq2k6VU5UwqiRK19Nr6VWB1Q52Q8CZ7iFQlhpnG7tmKgXUsOBVhX86oiMsQaOH0BqTheb2bawuc6lPXOlfqCrOMEzNV3wA1pHZlHN1oQ2kunMYH3zT8mAKg_KGfXIXNGx44TNw8d03YDHPPmsR5h_IgwqBNKiI9BltVPxnlWAsLlkTphvzm4CrPwZF1hkpl5s2nFz6OjMBD9KYOWpy_3A8D_HmR-2T9CQ49w_zqPkRoxOoasal-5_e2-BMnNJI09sSOX-3PXIg8yBRZG3Y5LibCxfYHv_UVgTppUX7Ks_gdfA3U6Bqc-TzA60j3hKtTtq_SELwcwuAOnEXxKAgDyew7XApGJecrmJh8_FODteEJ6FVjzU6EVrXkhVwPnuQW7kKujnWeK2EP5yse0a0JcGVNmq-J8efxWrYL_c8G4KNS-5VQQKpfWfe9S1bwrZqi2F2H1r1-58qtmvi58fNDJSvyFaz-fXvXcbcfpkdhCYw29gaXHHa9Rc-82m2-esLIO6RrLUZWZz9P7q20rLFjh6NtUoexmpVFN78bEUEZhVutxIns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cadaeb8025.mp4?token=jo2-wqwD8c2JoLIECDSR5pYOoscvyvQ_s35G8pMEDu2iJM6zJPmFekNU_UfXZnEkbheuGCFcjCvTrwg0u87bve9GH5wKIZ-GCAYbsE26JRb35bUUwRl3hjonaNyzGq2k6VU5UwqiRK19Nr6VWB1Q52Q8CZ7iFQlhpnG7tmKgXUsOBVhX86oiMsQaOH0BqTheb2bawuc6lPXOlfqCrOMEzNV3wA1pHZlHN1oQ2kunMYH3zT8mAKg_KGfXIXNGx44TNw8d03YDHPPmsR5h_IgwqBNKiI9BltVPxnlWAsLlkTphvzm4CrPwZF1hkpl5s2nFz6OjMBD9KYOWpy_3A8D_HmR-2T9CQ49w_zqPkRoxOoasal-5_e2-BMnNJI09sSOX-3PXIg8yBRZG3Y5LibCxfYHv_UVgTppUX7Ks_gdfA3U6Bqc-TzA60j3hKtTtq_SELwcwuAOnEXxKAgDyew7XApGJecrmJh8_FODteEJ6FVjzU6EVrXkhVwPnuQW7kKujnWeK2EP5yse0a0JcGVNmq-J8efxWrYL_c8G4KNS-5VQQKpfWfe9S1bwrZqi2F2H1r1-58qtmvi58fNDJSvyFaz-fXvXcbcfpkdhCYw29gaXHHa9Rc-82m2-esLIO6RrLUZWZz9P7q20rLFjh6NtUoexmpVFN78bEUEZhVutxIns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، گفت: «وقتی بچه بودم و در کارولینای جنوبی زندگی می‌کردیم، خانه‌مان نزدیک یک مرداب بود. در حیاط‌مان مارهای سمی زیادی داشتیم. اگر سر مار را قطع کنید، مار مرده است؛ اما خودش نمی‌داند که مرده. بنابراین باید مراقب باشید، چون سر مار هنوز می‌تواند شما را نیش بزند و دمش هم ممکن است تا غروب آفتاب تکان بخورد. اما وقتی خورشید غروب می‌کند و هوا خنک می‌شود، دم هم دیگر از تکان خوردن می‌ایستد.
مار ایرانی، یعنی رهبری ایران، هنوز نمی‌داند که مرده است؛ اما مرده است.
»
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/22563" target="_blank">📅 20:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اتاق جنگ با یاشار : آمریکا نمایشگاه هوایی زده رو تنگه
حدود ۱۰ سوخترسان ، پی۸ ، پهپاد و….
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/22562" target="_blank">📅 20:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22561">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/22561" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22560">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دلار ۲۲۹،۰۰۰ تومان (سقف تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/22560" target="_blank">📅 19:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22559">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9ayJyehcckSGDroHG-uY8nnERjR7wZCDAwAeSh9aM8MsksbYGxt0ICJCrQpN3Vjn3uCd4O0BVNlYcBqZPMKiBW6t3d3bSjPE73UZRzipyrRsXauDGC7RQo7DcsWSHD3bBPiQj8mvK5MfBoRAb9I0pz2r5VC1uEDCRuu7A7Y1hs-Dxknuf7xUWr3h2klFLGRXJ4JRfpNH5gz1hN3d2G1XocGFqZX0BS_7oM0Xi7aSyoWCEDz3Xtm2h-QxJ5MEEi098W2tK22iNSfunqYsVyrIBAfUAiK8vZcqy1Whv4LxRVPJR8GB_YyCAlXjzvvRR2nzSpAPcv3ywNdNr1Mj3c4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا اعلام کرد هرگونه همکاری مؤسسات یا شرکت‌ها با صنایع هوایی ایران، می‌تواند به خروج آنها از تجارت جهانی منجر شود + لیست تمام شرکت های هواپیمایی‌تحریک شده
@WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/22559" target="_blank">📅 19:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22558">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سپاه مدعی به دام انداختن یک شناور زیرسطحی بدون‌سرنشین آمریکایی در دهانه تنگه هرمز شد. گزارش‌ها احتمال می‌دهند این شناور از نوع Dive-LD ساخت شرکت آمریکایی اندوریل باشد؛ رباتی حدود ۳ تُن با توان ۱۰ روز فعالیت زیر آب و عملیات در عمق ۶ هزار متری که برای شناسایی، نقشه‌برداری، کشف مین و پایش کابل‌ها و خطوط لوله استفاده می‌شود. در صورت تأیید، دسترسی ایران به فناوری و حسگرهای این سامانه می‌تواند اهمیت اطلاعاتی و نظامی قابل‌توجهی داشته باشد,
@WarRoom</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/22558" target="_blank">📅 19:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22557">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eab716e17.mp4?token=CiYbwUP1RxdwJPsOr9ogGquBbpeD5Y5kypwcOPNXpm5uGGCTAYJXqLtE011UqXUEvh2gw6xWAQlRBmqENNCEa1RLmjGkEM5ge7T71W1l0vDfOY-LRy08HWLLcg7WA02nvXAlTailnZ9TKzgm3frBmg2rmTt0Gsog33vO0uiFuAwWW3J2XDEuYpkSdflLwOcaGM7NKfo2_kjnlTjm-nXm-6t1ThPv2U2Y10fSqFGxFcSeMkQ7POOHcN910-QTunofZJtjdnwPJIHItZAj_e3hzkuryfBdkKRgLMnRmTrYtoUIgYE6kF9iZaY8pF1cnBuXSZoEFTXk1_Scm1r9t28x5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eab716e17.mp4?token=CiYbwUP1RxdwJPsOr9ogGquBbpeD5Y5kypwcOPNXpm5uGGCTAYJXqLtE011UqXUEvh2gw6xWAQlRBmqENNCEa1RLmjGkEM5ge7T71W1l0vDfOY-LRy08HWLLcg7WA02nvXAlTailnZ9TKzgm3frBmg2rmTt0Gsog33vO0uiFuAwWW3J2XDEuYpkSdflLwOcaGM7NKfo2_kjnlTjm-nXm-6t1ThPv2U2Y10fSqFGxFcSeMkQ7POOHcN910-QTunofZJtjdnwPJIHItZAj_e3hzkuryfBdkKRgLMnRmTrYtoUIgYE6kF9iZaY8pF1cnBuXSZoEFTXk1_Scm1r9t28x5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سی‌بی‌اس نیوز: خلبان آمریکایی جنگنده‌ای که در جریان جنگ در ایران سقوط کرد، برای نخستین‌بار در برنامه «۶۰ دقیقه» درباره این حادثه و عملیات نجاتش صحبت خواهد کرد.
این گفت‌وگو قرار است
یکشنبه آینده
از شبکه CBS پخش شود و جزئیات تازه‌ای از ماجرای سقوط جنگنده و فرار و نجات خدمه در داخل ایران را روایت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/22557" target="_blank">📅 18:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22556">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شاهزاده رضا پهلوی در واکنش‌به پدر یکی از جاوید نام ها که به زندگی خود پایان داد؛ از روان‌شناسان، روان‌پزشکان و درمانگران ایرانی خواست برای حمایت فوری، مستمر و محرمانه از خانواده‌های جاویدنامان پیش‌قدم شوند. او همچنین از هم‌میهنان خواست منتظر درخواست کمک نمانند و اگر خانواده‌ای از جاویدنامان را می‌شناسند، به سراغشان بروند، احوالشان را بپرسند و در کنارشان بمانند
@WarRoom</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/22556" target="_blank">📅 18:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22555">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c20f289d7.mp4?token=cp0xAEsqyqfZEHaTKbWHch0SW0Ti6A1CdgiSDynwhpnRpISa-1-tmGoBg2JgSZxtTs3YLbY-y3Y1f1K8oyhL5rggmLue3lBHSSHUid17xbDKDXhJ_k7XwJlnmiyTwCfLVsGF0U9R7eXv4A0GClP6RB9X6VoHIgM1AuBODbJcB2lGFeXB8YCAgNnQ0m_Qq-nVp9rDE0eN74NpFNm6nTclXyzSQUI_ldSi3wurMg2VtgFzIHrNBxg04xEYSuIweGFJ_HOjEIriUiiIJ5VnCDyF_IeF3jinPkW_gPCKuv7AYdLhOUqyXCruttRcgss0AdiVCW9CkBruA0PfKIn6Y2Sl1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c20f289d7.mp4?token=cp0xAEsqyqfZEHaTKbWHch0SW0Ti6A1CdgiSDynwhpnRpISa-1-tmGoBg2JgSZxtTs3YLbY-y3Y1f1K8oyhL5rggmLue3lBHSSHUid17xbDKDXhJ_k7XwJlnmiyTwCfLVsGF0U9R7eXv4A0GClP6RB9X6VoHIgM1AuBODbJcB2lGFeXB8YCAgNnQ0m_Qq-nVp9rDE0eN74NpFNm6nTclXyzSQUI_ldSi3wurMg2VtgFzIHrNBxg04xEYSuIweGFJ_HOjEIriUiiIJ5VnCDyF_IeF3jinPkW_gPCKuv7AYdLhOUqyXCruttRcgss0AdiVCW9CkBruA0PfKIn6Y2Sl1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران دیگر هیچ شانسی برای دستیابی به سلاح هسته‌ای ندارد و تحریم‌ها علیه آن مؤثر بوده و نتایجی فراتر از انتظارات به همراه داشته است.
ما الان داریم می‌جنگیم چون ایران می‌خواست سلاح هسته‌ای داشته باشد و خیلی به دستیابی به آن نزدیک بود.
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/22555" target="_blank">📅 18:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22554">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بلومبرگ: نخست‌وزیر جدید بریتانیا با استفاده آمریکا از پایگاه‌های نظامی این کشور برای جنگ با جمهوری اسلامی مشکلی ندارد و این موضوع را تأیید کرده است
، دولت بریتانیا در چارچوب همکاری نظامی با آمریکا،
اجازه استفاده از پایگاه‌های بریتانیا برای عملیات مرتبط با درگیری با ایران
را داده است. این موضوع در حالی مطرح شده که نقش و میزان مشارکت نظامی لندن در جنگ با ایران همچنان مورد توجه است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/22554" target="_blank">📅 18:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22553">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آمریکا ۲۸ شرکت هواپیمایی ایرانی را تحریم کرد
؛ دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا سه‌شنبه ۱۷ شهریور،
۲۸ شرکت هواپیمایی ایرانی، ۷ شرکت مرتبط با بخش هوانوردی و یک تبعه مصری ساکن امارات
را به فهرست تحریم‌ها اضافه کرد. از جمله شرکت‌های تحریم‌شده
آتا، چابهار، ایران‌ایرتور، آسمان، کیش، کارون، قشم، سپهران، تابان، زاگرس، وارش و فلای‌پرشیا
هستند. همچنین چند شرکت در
امارات، بریتانیا، ترکیه، مالزی و قزاقستان
به دلیل ارتباط با ماهان‌ایر یا شبکه‌های مرتبط با آن تحریم شدند. آمریکا همچنین
مجوز عمومی G-1 ایران برای صادرات مجدد موقت برخی هواپیماهای غیرنظامی به ایران را تعلیق کرد
و هم‌زمان مجوزهای جدیدی برای پایان دادن به برخی معاملات مرتبط با هوانوردی غیرنظامی صادر کرد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/22553" target="_blank">📅 18:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تهران و کرج صدای رعد سنگینی شنیده شد همه نیم متر پریدن و فک کردن حمله شروع شده
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22552" target="_blank">📅 16:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22551">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرگزاری رسمی کره‌جنوبی،
یونهاپ (Yonhap)
، امروز گزارش داده وزارت دفاع کره‌جنوبی اعلام کرد یک تیم تحقیقاتی برای
ارزیابی وضعیت امنیتی تنگه هرمز و بررسی شرایط منطقه
اعزام شده است. سئول همچنان در حال بررسی گزینه اعزام نیرو برای مشارکت در تأمین امنیت کشتیرانی در هرمز است، اما
هنوز تصمیم نهایی درباره اعزام نیروی نظامی گرفته نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22551" target="_blank">📅 16:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22550">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پرتاب موشک از کرمان به سمت تنگه هرمز، نقشه و عکس ارسالی @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22550" target="_blank">📅 16:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22549">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqi6d7c1Eou0jjGJM23HA9QSgODArsUJTCxY-3CSM_4Zwld4bnPn-wZSwJrn1smN0P-0R5epLLGNQ5KcVXHTVrqszCB5oE4uamEGG_1kBZm9r7b8VvGBlnCH0A5n26s9Fvi2GUnxOgWhmOdf8c63E30Vfeqghz4NfevLR4VbVMP1zrYcDA6Qj6MH8V1NNl69TJVK-oE0XmXWra2q7SdpScU43vgrAY5Tb3Z-hge0rmVq1e5ZbDdmJi9Bqj3wtP2_3rJY6s-22XL6ceXghznVHIJ_JlMagJkXBRXrodQzatTn8wO96rzRNJFBpvx-q35YoZz14steneijKScSMf0yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش های بسیار از صدای انفجار از محدوده زندان قزلحصار و هم اکنون عکس و رؤیت ستون دود از این محدوده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22549" target="_blank">📅 15:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22548">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjJu5jRxOq8tO4CploZhH5c_SNvzWddpU-JOOBfdTkMOSisPyZ_jQKpMe7464aNl1cIEw9QiGlgGgDnYC8u5YESwLXi5i3Pcm-58S3nuCBp2d2EztDIkU3nS7VknQ3uGtVO3MPukLH6vv0IbGd64JzB_KdQGHOudts0obMxPOrbt3o5qOBJyJIoqB1SzvEIt6XLFbf_4-nCHbP91-28UWIIF0PBTEnJPLVZztjE_-bV2zm0EQi-eYm-iEYgT6qW0lS8OoYShES6VPfQqGMftgbOENQBF-N-3_sG4FAna-Bj-BkJcwa528mpWzOUtqDqjd3jA5BaxrALn8Mus2K2-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غرب شمال غزه هم اکنون
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22548" target="_blank">📅 15:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پزشکیان: نسل جدید با دستور همراه نمی‌شود؛ باید با او گفت‌وگو کرد
نمی‌توان صرفاً دستور داد و انتظار داشت نسل جدید از آن تبعیت کند. او تأکید کرد تحول در نظام تربیتی باید متناسب با شرایط نسل جدید و با نگاهی آینده‌نگر باشد و حل مسائل جامعه نیز به
تقویت گفت‌وگو و استفاده از ظرفیت‌های مردمی در مسجد و محله
نیاز دارد. وی همچنین گفت آنچه امروز در جامعه دیده می‌شود، برونداد نظام تربیتی کشور است و برخی فرصت‌ها برای تربیت نسل جدید در دوران کودکی و نوجوانی به اندازه کافی مورد استفاده قرار نگرفته است
@WarRoom
یاشار : این نسل شیک پاسارگادی خر نمیشه
🫶🏻
✌🏼</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22547" target="_blank">📅 15:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رویترز : دولت انگلیس امروز قوانین جدیدی برای تشدید فشار اقتصادی بر ایران ارائه کرد؛ این اقدامات
بخش‌های انرژی، فلزات، بانکداری، بیمه و کشتیرانی
را هدف قرار می‌دهد و محدودیت‌های تجاری و مالی علیه تهران را گسترش می‌دهد. همچنین اختیارات لندن برای تحریم کشتی‌های مرتبط با ایران افزایش یافته و
فرود هواپیماهای ایرانی در انگلیس ممنوع خواهد شد، مگر در موارد استثنایی
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22546" target="_blank">📅 15:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXT1i7kCjbtqdbcik5Qmkr3SSz4PuPQXU0gjXg5CDuYReFh5rXele6NzKrNwC28l4_2W1WU5DJ-XgTf56w0VeTcTxMq0KQXtULUIycNOWOhN-vXYnBnv3qbSwRqXiD-3v-qnWyRgoG71PoZpp-GdCEtZkvzuyAv-jI4MduVuZOfGd3MeQ0WG1HVBn7YGZG6I4HRJMU8NmpNUt2HEcO0WQyxXxiUJLPqUj9gsg-wgJw3gO0soqTKXi_Wz3F2ceTUeVHwS5excnwtzgOHsONUBw_b4QCNf5hAs8l-4KqTdfn7Eifc-RlqlpUCoT1rOtxThGnmDyw6qktfP9n0Wjjb6mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پیش عبدالرووف اسحاقی، فرمانده بسیج پارود در سیستان بلوچستان به هلاکت رسید
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22545" target="_blank">📅 15:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1rg4eY0d9p1Ax-0rUHhNJVCOGqUibq3cKVVj9FEEtNLsLGPIOGt6FOWaRHTwMMW0r2U2yw-XpLta9fmLOOCCFFEVtineoIfz6Bir8BmmM20WzT-rbhC9Ix7WeQ17qp8anqhDOPk96uXPQFx_ktj4vsKbOW52BOoLCHC0jgMxdExo6W2CLq18StIzjoT4MH62gSAhqT2WAJ14kX_Ag47hIpyUivCKjfJDNPXR9PW5XL4g9Afahp84c1M_iCgK2R-OFZIJn9_VzVwjyk3LFehLcuhVjLHDAr6j6XT9iYTHpT9Gdx3NdnMzqk5lTCWafu2MZB0FBJUnJUMmPuKFd2tng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک بالستیک از کرمان به دریای مکران
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22544" target="_blank">📅 14:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22543">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXvU7u1bAZJbYaCBpIavk7qfRSxgSDvKETfutl49DnxyVqXzy79UwNRFUi2JZtqk-AOORABhWVsU0XYwHbSi6QtVWpBMDORoe0JLDHntT3Y1bvkVFpvECXc2HDkrAsJIN1jKmN4hYgawkKKe3v5L8Y6tSzTcGEqAt6-j8HikASvlDDqz37g0glWvN3sMLJcpMUOluPYAsRrLLxNm8u_qLj6vsT7SbJhkWPLaoBTg3EcjGZOUP-vEK6dx8VoAltqPrH4m-v1zSpQf8HQqEJdpdhNUx2Bn42Sr_bNtAHbZJpEd6RJtppFA20lo_T7QBBJtzVo3oMsfe-39Co6avqwU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از کرمان به سمت تنگه هرمز، نقشه و عکس ارسالی
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22543" target="_blank">📅 14:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22542">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش های متعدد از پرتاب موشک از کرمان به سمت دریا
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22542" target="_blank">📅 14:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22541">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دیشب اعتراض به گرانی بنزین در کرمانشاه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22541" target="_blank">📅 14:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22540">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c790194bb.mp4?token=X75KLELvOEoRyHyCl0XGl3l1m6ejAQqvX13LjuSdCQ68x4hcSim-jBY1_had2iN7eQZ638u4-IHUdwQsoJ28QU6VpWLJvBAaJAhJamyui1_dk6aRHgBKTdsr0ZkJxN56ulRITsYue-FzwPsmBaK_bLmw7jk20C6oKPYh36oOVNYcoU1KvIp9oKNnAEJbtQ3iqQJM3zBxpFcvxCZt9gvKnjlPTDiMliiKj03zKG-ceYyVZeauLV-koFY7G-sKBtM_oToFvAuj6yzUgEM36nup50QOCZMQsPhpnLgSfz91emB41wE4V_65dYdIgdB3EQVM_llfKer3WEJGcTV-Qk1vk45ahYIvPxD9Cb_aU7M3XgcoRtB8hCzMVfwg25b5z4bTJOMlXo_vY3NBacbcs9z-5nTP6993Zmeu02qlIOkiakUv02hFxo0dCyKknimLtZPiQ4C17wD_CQ9E26nIYekrGH2x-wKBap9D1TWbT2LYe4-QBkMd6MDAfpenxxwWzLZdmOv2lzIgY_8EqwnVloBMi78bOPR9x3RJ65DsDPpn_540JYHsaqjFJU5mdU7MuyAizjEFqIwAOaTTs6atnUHXKc7i2f-kqE7yNWNp48Jm1o_b84vifNlYsKhT7ah3nLSsP17-uBLoF7kfIjJqHOJfNaycAtv83VTlDRcAKDgwgGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c790194bb.mp4?token=X75KLELvOEoRyHyCl0XGl3l1m6ejAQqvX13LjuSdCQ68x4hcSim-jBY1_had2iN7eQZ638u4-IHUdwQsoJ28QU6VpWLJvBAaJAhJamyui1_dk6aRHgBKTdsr0ZkJxN56ulRITsYue-FzwPsmBaK_bLmw7jk20C6oKPYh36oOVNYcoU1KvIp9oKNnAEJbtQ3iqQJM3zBxpFcvxCZt9gvKnjlPTDiMliiKj03zKG-ceYyVZeauLV-koFY7G-sKBtM_oToFvAuj6yzUgEM36nup50QOCZMQsPhpnLgSfz91emB41wE4V_65dYdIgdB3EQVM_llfKer3WEJGcTV-Qk1vk45ahYIvPxD9Cb_aU7M3XgcoRtB8hCzMVfwg25b5z4bTJOMlXo_vY3NBacbcs9z-5nTP6993Zmeu02qlIOkiakUv02hFxo0dCyKknimLtZPiQ4C17wD_CQ9E26nIYekrGH2x-wKBap9D1TWbT2LYe4-QBkMd6MDAfpenxxwWzLZdmOv2lzIgY_8EqwnVloBMi78bOPR9x3RJ65DsDPpn_540JYHsaqjFJU5mdU7MuyAizjEFqIwAOaTTs6atnUHXKc7i2f-kqE7yNWNp48Jm1o_b84vifNlYsKhT7ah3nLSsP17-uBLoF7kfIjJqHOJfNaycAtv83VTlDRcAKDgwgGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب اعتراض به گرانی بنزین در کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22540" target="_blank">📅 13:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اتاق جنگ با یاشار : مردم شریف ایران، شرایط ایمنی حمل‌ونقل کشور به‌شدت نگران‌کننده شده است. در بخش هوانوردی، گزارش‌هایی از اختلال سامانه‌های ناوبری گزارش شده همچنین بعد از‌جنگ اکثر سامانه های راداری نابود شده اند و از ترس حملات خاموش کردن عمدی ترانسپوندر برخی…</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22539" target="_blank">📅 13:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش هایی ااز پمپ بنزین پاسداران و پیروزی هم دارم ، ایست شدید و چک کردن گوشی ها هم انجام میشه کاربری گفت گوشی دوستشو چک کردن و گرفتنش @WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22538" target="_blank">📅 13:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22537">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromK M</strong></div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22537" target="_blank">📅 13:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22536">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcOZZvCq1R6PjEwHmYmvjtez9zCHa5Wf8K3MM6y1oRhmaxluJrEKQOH1a95TjTqiNcPzcgIDqswWceIRxouCaeNhys9EB-wsQV_Hn9QOcY8Z7VKf5FuLb9XLuUyJCZzEIdQ1NIVV4Z34iyM5dcHjjWzABDlrr3LNZsvXm6oSZIDw5P0G75dFLM2h7D9fmdOKU4wWvpx5LGYuJi2YJb_J-i-MTo7zLmkQXsC2HHkvXK0vzs6cnckCsFQrdQ35vZ3fkncgOnDu0onKA9V8Zff9vMNGUgTEZKOaymep11vaO29MF7u8u7BDoT-w16MT12eCwlM1zsZdG4JWXSi3D-m4vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : درخواستی :
یمن وارد فاز درگیری گسترده با حوثی‌ها شده؛
چند جبهه از الجوف و مأرب تا البیضاء، الضالع، تعز و حدیده هم‌زمان فعال شده‌اند و نیروهای ضدحوثی در برخی مناطق پیشروی کرده‌اند. نیروهای دولتی یمن در الجوف و البیضاء نیز مدعی پیشروی هستند؛ در این جبهه‌ها نیروهای دولت یمن، قبایل محلی، نیروهای نزدیک به عربستان و گروه‌های مورد حمایت، از جمله نیروهای طارق صالح و العمالقه، حضور دارند. به نظر می‌رسد هدف اصلی افزایش فشار بر حوثی‌ها و عقب‌راندن آنها از مناطق نزدیک به باب‌المندب باشد؛ زیرا هم‌زمانی این جبهه‌ها حوثی‌ها را مجبور می‌کند نیرو و تجهیزات خود را میان چند محور تقسیم کنند. الجزیره به نقل از معاون وزیر دفاع یمن: «تصمیم برای آزادسازی صنعا و یکسره کردن کار گرفته شده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22536" target="_blank">📅 13:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22535">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پزشکیان در توییتر: با توجه به ادامه حملات و شرایط ، جنگ ادامه خواهد داشت
جمهوری اسلامی ایران همواره با جنگ مخالف بوده و حفظ منافع مردم و امنیت منطقه را در پرهیز از آتش افروزی دانسته است. اما چنانکه تا امروز در برابر تجاوز، دلیرانه به دفاع برخاسته است این مقاومت را تا پشیمانی کامل متجاوزان با قوت ادامه خواهد داد و پاسدار حقوق ملت بزرگ ایران خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22535" target="_blank">📅 12:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22534">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22534" target="_blank">📅 11:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22533">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22533" target="_blank">📅 11:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22532">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به گزارش TRT ترکیه :
آمریکا پیشنهاد جدیدی را از طریق پاکستان به تهران منتقل کرده است
.
وزارت امور خارجه ایران اعلام کرد تهران در حال بررسی آخرین پیشنهاد ارائه‌شده از سوی آمریکا با میانجی‌گری پاکستان است؛ هم‌زمان دونالد ترامپ از قرار داشتن مذاکرات در «مراحل نهایی» خبر داد و دو طرف هشدارهایی درباره احتمال ازسرگیری حملات نظامی مطرح کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22532" target="_blank">📅 11:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22531">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tASEcSrW0RK2O8-_ld-t0m9JffhmgBknHtycUDYHDWAlaKVZH7gEPpKlVWleUNYRD0_edjRDad_C3InhXPxldcto9QfUTv7DN8BLtEqnSf7en1hKR8fk0rP9pbJq4tvoK48kj8LsrJcsUm1sYoCVvHw8yCwwR1cV-C4Jh54taTyp9-JAM6N56eSk9Hbxrmff7h4WwWfaklXMIrk7NJFNXvGuGXA8dkWr6rxwTUXxdf6MR34TM5-XOnqFtDQia8jL34VXfsvBimpD4NEUGgA23CfWLDlkMI_3jjvOwsJvfBLTpbaWlYSyWTKPntjzGa6d20l4_lP-kCoK6gs18W1G8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برنت ۹۹.۱۰$
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22531" target="_blank">📅 11:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الکسی لیخاچف، مدیرعامل شرکت دولتی روس‌اتم، در پاسخ به پرسشی درباره ساخت نیروگاه‌های جدید در ایران گفت: «بدون شک، آنها چنین علاقه‌ای دارند.
ایران علاقه‌مند به گسترش همکاری با روسیه برای ساخت واحدهای جدید نیروگاه هسته‌ای است
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22530" target="_blank">📅 11:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی: دسترسی به برنامه هسته‌ای ایران باید فوراً برقرار شود
رافائل گروسی هشدار داده نبود دسترسی و اطلاعات کافی درباره مواد و تأسیسات هسته‌ای ایران یک نگرانی جدی برای اشاعه هسته‌ای است. همزمان آمریکا، بریتانیا، فرانسه و آلمان برای
ارجاع پرونده ایران به شورای امنیت
تلاش می‌کنند.
نمایندگی جمهوری اسلامی نزد آژانس
اعلام کرده اجرای کامل تعهدات پادمانی
تا زمانی که آمریکا و اسرائیل حملات خود را متوقف نکنند، از دید تهران قابل اجرا نیست
و گروسی باید ابتدا خواستار توقف حملات شود.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22529" target="_blank">📅 10:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تحولات امروز در اطراف علی‌الطاهر
پس از اعلام کنترل اسرائیل،
حملات اسرائیل در منطقه نبطیه و اطراف علی‌الطاهر ادامه یافته
و کفررمان، در نزدیکی این ارتفاعات، نیز هدف حملات سنگین قرار گرفته است. رویترز از کشته‌شدن دست‌کم
۱۲ نفر
در حمله به کفررمان خبر داده است
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22528" target="_blank">📅 10:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وال‌استریت ژورنال : درآمد نفتی ایران در حال خشک‌شدن است
، بارگیری نفت ایران پس از محاصره دریایی آمریکا
۸۵ درصد کاهش یافته
و ذخایر نفتی شناور ایران از حدود ۹۰ میلیون بشکه در ژوئیه به حدود
۲۹ میلیون بشکه
رسیده است. این روزنامه پیش‌بینی کرده ذخایر موجود در صورت ادامه روند فعلی تا اواسط اکتبر به‌شدت کاهش یابد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22527" target="_blank">📅 10:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22526">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fllc6RJ8FjN0751BJDBqOX8Ie_0MXSfQls5nWiyLwKtgL_BFCCAGQ764eMTjUdEZz0trGVh6O2HrmGaH3IN8J_BpNNHlDd3BW02BJLF5KIA-1NlXNBdOfzNOuLm42zhXbyQoFGHZwrGUxNEUDWFkw2YM4auksVM0r80idOX_v7Glg0lhL8EVqgknraXHdddGoSUZ55sUevS5qUw5YtYrdEOnYV5qZf8Tm_h5bNOH2HSg_YldPCMCmc6TgQ6ngVomRaJ6NAdroNW1FIoGjS5MHLKMvphvqUH8aVlZhe1XEQE9CUfc8kUSrtuk1p77ZnPi7v5hplMh5FqWvlQfzXzpMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : قیمت نفت با پیروزی ما در جنگ با ایران، به‌شدت سقوط خواهد کرد؛ درست مانند همه‌چیز دیگری که در حال کاهش است، اما حتی بیشتر! قیمت هر گالن نفت به ۳ دلار خواهد رسید و در نهایت به کمتر از ۲ دلار در هر گالن خواهد رسید. همه این اتفاقات به‌سرعت رخ خواهد داد و ایران هرگز سلاح هسته‌ای نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22526" target="_blank">📅 06:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh2a_g4FfWgeZlBRWVEmm5EdPUHDA7EnhWxJqLSRuSoB4ZDfPow4AGA8PhwfzKfu1MLB4s2dkkVA4dfvM8BCi2NbqdteDOAC5xCyh2cr8XhbHaARFQa0uVCv8HqLQ6kXjAthjc1vPw_H3WVpYIH6PQYU5vwwPu7r6hu9kexkz0f6Sry07VUJDFD2QJEHXTYo4AgBOX2o9j8LMNJ158CF7L0Qb1LPylOGxdL790itD_GjnazO6t92oXaa4v6eKp9jbITL1nLLFguRQsX_59mhFFKT7NbOPf-iFpskDUVqM_i8_PVEE-iDYHHGZ1Ijig9AHyLoC8ZpOYIlQzTg00k61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : نیرو دریای ایران
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22525" target="_blank">📅 01:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22524">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش هایی ااز پمپ بنزین پاسداران و پیروزی هم دارم ، ایست شدید و چک کردن گوشی ها هم انجام میشه کاربری گفت گوشی دوستشو چک کردن و گرفتنش
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/22524" target="_blank">📅 00:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22523">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بوشهر صدای تیز اندازی گزارش شده
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/22523" target="_blank">📅 00:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22522">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش ارسالی تایید نشده : پمپ بنزین شهر ری‌در همین لحظه به آتش کشیده شد
@WarRoom
🚨
🚨
🚨
در انتظار تایید و فیلم ها هستم</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/22522" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22521">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1Fu9jEQIH62zjCKdsvSwkxqz7CA0Y6gaVnIuzy4E0oazKdtnW0oGv_SPp8y5tWBVPJLC2kC8k8YjIvnlcu6Mi0J6FPQFcBr0jSa2-MzC_hI7a-BlffDsSRLCv_2ni0pQo5jXFhkNK_grjs-khts8gIFn5gFK7TMtnB_fmHEmk1ygmhxukURtd33yesMP8EpHuO2LORTCIVzlI9v6YfYCbdIXN9wdgNlE9JvGqqdOhIY9tp2ZFmMwylqZgUuL098Rszvuq6eSnYIJANYSnyNcXMXYmueihIMUPtjz1Iu6kIozw8JzpJ5EJOq9rWDTXL1l2ctvII4I7qvMEyiT262TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک فروند هواپیمای جنگ الکترونیک و تهاجمی ایی‌ای-۱۸جی در جریان عملیات پرواز شبانه، از عرشه پرواز ناو هواپیمابر جورج اچ. دبلیو. بوش به پرواز درمی‌آید؛ این ناو در حمایت از اجرای محاصره آمریکا علیه ایران در دریای مکران فعالیت می‌کند. تا امشب، نیروهای فرماندهی مرکزی آمریکا برای اطمینان از اجرای کامل محاصره، مسیر
۹۴ کشتی
تجاری را تغییر داده‌اند، ۳ کشتی را از کار انداخته‌اند و ۲ کشتی را با سوار شدن نیروها بازرسی کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/22521" target="_blank">📅 00:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22520">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نرخ سوم بنزین, از همین لحظه ۱۰،۰۰۰ تومان شد
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22520" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22519">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کپلر: تردد کشتی‌ها در تنگه هرمز هفته گذشته ۲۸ درصد کاهش یافت و به ۷۷ فروند رسید
بر اساس داده‌های شرکت کپلر، که در زمینه اطلاعات، داده‌ها و تحلیل‌های مربوط به کالاها و کشتیرانی فعالیت می‌کند، تردد کشتی‌ها در تنگه هرمز هفته گذشته ۲۸ درصد کاهش یافت و به ۷۷ فروند رسید
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/22519" target="_blank">📅 23:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22518">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxXaQ-C7AT1JZh2y5vx7AwH1rUefgOfjOrbweBtmf9SnJfyQQXAitCqicbHzUAMtSpU5ByUNuecR-701U89Q78xa28XRzb3SWpk3HpU-OHyb9AaKRdSuDTWKZdvYxqiFIeuGCqACydwFGWAXeAmRAwv3hl5xMYXsv6rNo2up08bKvu6iMa_O-nKZc9hnMYH4Jz8QJR-CJxDHkyADcouIpRA83apyarU4bNQtEEPKvFh3WDnp8Qdo6PUVgKuIQYE03ON0c_CrDRD_FmtMwQPJfKavR3O-y9qlDjeT_w5u6BL8CYD9Kx-zU1m-gBKxugNiFvxMJEOzEydTR_eyg1lVyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : چند پرتاب از سیریک به تنگه و صدای انفجار از تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/22518" target="_blank">📅 22:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22517">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71f020c05.mp4?token=r6Lxg1EFwrxK4C4lL0VhJnUMlF_zZIpFb5VdrXIX0qUrH5E25j9Iqk-yUoyeUyrDoDtY5ymKgiYqyOlo6k6g77G5HP08OIaKXejifOq3VGKBv5rEuSZUWBCQlbTwP-BCWf7sFEFa-I8eygVOMhm0Oex7-ZiZtKSEHfayQqFSQsDhwTGunthHwaCHhljXwVOz23WAZxsXcMsE6aKePFnOSr4gZwsiadT_2iGZouNrX0VNt6-stZxbrPjv15MxNr6wkDRQktFLR1ulenzsAIp-WDENaaayU3aGysh_O0jxONIvRasaG-OJ9iIVbKkxV2dlDUNR-5Zj1JeYRihHASy7tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71f020c05.mp4?token=r6Lxg1EFwrxK4C4lL0VhJnUMlF_zZIpFb5VdrXIX0qUrH5E25j9Iqk-yUoyeUyrDoDtY5ymKgiYqyOlo6k6g77G5HP08OIaKXejifOq3VGKBv5rEuSZUWBCQlbTwP-BCWf7sFEFa-I8eygVOMhm0Oex7-ZiZtKSEHfayQqFSQsDhwTGunthHwaCHhljXwVOz23WAZxsXcMsE6aKePFnOSr4gZwsiadT_2iGZouNrX0VNt6-stZxbrPjv15MxNr6wkDRQktFLR1ulenzsAIp-WDENaaayU3aGysh_O0jxONIvRasaG-OJ9iIVbKkxV2dlDUNR-5Zj1JeYRihHASy7tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : سلام یاشار این اوضاع امشب قشم یه ماشین بزرگ سیاه هم جلو بود پر آدم
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22517" target="_blank">📅 21:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22516">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSina</strong></div>
<div class="tg-text">یاشار خوبی داداش
داداش تهران به شدت جو امنیتی شده من رفتم بنزین بزنم غروبی تو تمام خیابون ها داره موتوری‌های یگان ویژه میچرخه،سره میدان ها یگان ویژه وایسادع حتی جلو پمپ بنزین ها
رفیقمم از پاساژ علاالدین گفت که خواستیم اعتصاب کنیم اطلاعات اومد نزاشت.
داداش تهران منتظره یه جرقه‌است</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22516" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22515">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid</strong></div>
<div class="tg-text">یاشار جان من رفیقم تو اگاهیه
میگه امشب اماده باشن
ک ی موقع مردم نریزن ببرون
😅
😅</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22515" target="_blank">📅 21:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22514">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش ۲ پرتاب از سیریک ۹:۲۰ دقیقه
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22514" target="_blank">📅 21:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه، با انتقاد شدید از اقدامات اسرائیل گفت که دروغ‌ها و خرابکاری‌های این کشور باعث شکست تفاهم‌نامه اسلام‌آباد میان ایران و آمریکا شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/22513" target="_blank">📅 21:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">روزنامه تلگراف انگلیس: رئیس جمهوری سابق ایران ( روحانی) خواهان برگزاری رفراندوم برای پایان جنگ شد
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/22512" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22511">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر در گفت‌وگو با CNN گفت
اولویت قطر بازگشایی تنگه هرمز، کاهش فشار اقتصادی و جلوگیری از تشدید درگیری‌هاست.
او تأکید کرد قطر به دنبال
راه‌حلی پایدار و گفت‌وگویی فراگیر میان کشورهای منطقه
است و معتقد است تحریم‌ها تاکنون نتیجه مطلوبی نداشته‌اند. همچنین قطر چند طرح، از جمله
یادداشت تفاهم
، برای رسیدن به توافق ارائه کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22511" target="_blank">📅 20:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22510">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2ErQrDseLoHbRORTC2L2cbKsDq-feTAsL_h6iOwSXgXBQfGKGaIUzAj6y_exnrAtwKLvcWhnIzOe0LIgSF-VW-qHpiJJ69dx8vv8CbIlaUAebmhzk8km8D4Zy5_Ee3wT-ErqZctgqRsQhdJ2-RJCqf_TJY9coyxMrDb429kIeWr21ACdxgaKB3820YMLs9EUge7RQR2IEsWrNQBhiO-2hzwUUO4rvmCbGNGNUFHrxdj1cMm2rp1w7JtHDKqQ_rp07JoERcHpJQCU6u4qr8E6DAyHbHAH9lsnOi4E3VPxO5e2h99wzzoilPjGyaFl14yXXxLXs6Vy9VdYpssfmnOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث، گزارشی از
وال‌استریت ژورنال
را با این مضمون منتشر کرد:
مسعود پزشکیان و محمدباقر قالیباف
بر ضرورت
پایان دادن به جنگ و مذاکره برای خروج از آن
تأکید کرده‌اند و خواستار تقویت اقتصاد ایران در شرایط فعلی شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22510" target="_blank">📅 19:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ : در انتخابات میان دوره ای به پیروزی قاطع دست خواهیم یافت و آمریکا را نجات خواهیم داد‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22509" target="_blank">📅 18:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688ebf7bb6.mp4?token=lqd4ruI95rYXSNfrzy_oiGU5urBT3rUnFKiMR0PG0oPwI-d-L65CZRzEASTKX4TbMV67fJg_h1SGH5CGHHcrxQ7RLqBO1a_8w0x2Us_gXtchHqcLtvyXgrD_ABlMQpEK3FKjSiEZyjkjTRv7b9scDqOzOMHbYctU_HRzKPkm-v7FsWYyeH0GRv8ktSI7imU8NClbnjNMATyX7fwo2aZ8RBETNmCNvoWnxbF-KGVRS0LmiMBMZJs7p97CwoT2wFviH-l_H3CAnBA-DXZU0Wbean83o9_goBfuthMeeb9uwSP-m2XsGZbI5mSx9BQUSJ4Pzlgj4LcRmh3vg1e0dP9BJnZtkJ7Ey7y5vBJtRPu5YXbDcXhEFkOUt75Iuc2sMntZfStdSQTQhnSSM05Klv-RDTA0NaNUuG3m4-YpAA_N8e2nDE2K3lnahomEaMldkI467qviyfrMixUMhZpuQ3w-TbJcKq23l0Vw08PvPVU9Dq86jPMB77g6Bjat-lv6HlA9XlIYeindV1qIrg8Nm0UkVfA3i-brhXPNudlPi6NpbHppicnNO5nHRbk_lr_wlWvTsx8oFzPtiZGyA31Fl8X_wOJj2Cg3XhEM1YjHYwsTQ6D7X-0zrBrhueWztRyo2PmXA3mF7uO0wuCNQC-hCAQuTsNwQKECXfPm06Wfn6Y6pw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688ebf7bb6.mp4?token=lqd4ruI95rYXSNfrzy_oiGU5urBT3rUnFKiMR0PG0oPwI-d-L65CZRzEASTKX4TbMV67fJg_h1SGH5CGHHcrxQ7RLqBO1a_8w0x2Us_gXtchHqcLtvyXgrD_ABlMQpEK3FKjSiEZyjkjTRv7b9scDqOzOMHbYctU_HRzKPkm-v7FsWYyeH0GRv8ktSI7imU8NClbnjNMATyX7fwo2aZ8RBETNmCNvoWnxbF-KGVRS0LmiMBMZJs7p97CwoT2wFviH-l_H3CAnBA-DXZU0Wbean83o9_goBfuthMeeb9uwSP-m2XsGZbI5mSx9BQUSJ4Pzlgj4LcRmh3vg1e0dP9BJnZtkJ7Ey7y5vBJtRPu5YXbDcXhEFkOUt75Iuc2sMntZfStdSQTQhnSSM05Klv-RDTA0NaNUuG3m4-YpAA_N8e2nDE2K3lnahomEaMldkI467qviyfrMixUMhZpuQ3w-TbJcKq23l0Vw08PvPVU9Dq86jPMB77g6Bjat-lv6HlA9XlIYeindV1qIrg8Nm0UkVfA3i-brhXPNudlPi6NpbHppicnNO5nHRbk_lr_wlWvTsx8oFzPtiZGyA31Fl8X_wOJj2Cg3XhEM1YjHYwsTQ6D7X-0zrBrhueWztRyo2PmXA3mF7uO0wuCNQC-hCAQuTsNwQKECXfPm06Wfn6Y6pw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تفنگداران دریایی و ملوانان ناو آبراهام لینکلن، مشغول عشق و حال در کلابهای  پاتایا، تایلند. @WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22508" target="_blank">📅 18:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ در تروث ویدیو برنامه مارک لوین را بازنشر کرد: در این گفت‌وگو، ویکتور دیویس هنسون ترامپ را «معکوس‌کننده‌ی انقلاب» می‌نامد؛ یعنی رئیس‌جمهوری که قصد دارد روندی را که طی۵۰سال آمریکا و سیاست خارجی آن را تغییر داده، معکوس کند. در مورد ایران نیز تأکید می‌شود…</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22507" target="_blank">📅 18:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏خبرگزاری عراقی «بغداد الیوم» گزارش داده بیش از ۱۵۰ نفر آزادی خواه ایرانی به محل اسکان دانشجونماهای عراقی گروه تروریستی «حشدالشعبی» حامی جمهوری اسلامی در دانشگاه سمنان هجوم برده و شماری از آنان را مورد ضرب‌وشتم قرار دادند. تعدادی زخمی شدند و ادعا کرده پول،…</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22506" target="_blank">📅 18:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الجزیره: ایران به آمریکا اطلاع داده که در صورت اشغال کامل تپه علی‌الطاهر توسط اسرائیل، مستقیماً وارد عمل می‌شود، این منطقه محل استقرار تاسیسات مهم و استراتژیک حزب‌الله است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22505" target="_blank">📅 17:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سی‌بی‌اس نیوز:
وزارت دادگستری آمریکا در حال احیای یک قانون قدیمی مربوط به
توقیف کشتی‌ها و محموله‌های نفت ایران
است تا بتواند نفتکش‌های ایرانی را هدف اقدامات حقوقی قرار دهد. این موضوع بخشی از فشار اقتصادی آمریکا بر تهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22504" target="_blank">📅 17:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dd84c2849.mp4?token=dFRDVteNpSL46fvGYcWaPtM-MEMsYi4n_yt9EoasiCJUqKCCIuZR-7u9sQN7So6W9snm06U3n4916fKrcwJUn4X_K8xzFaXJ2fDDjtMNvL1UuRRpoP7fdFmLKJ-J22PQqbt2npWAOqfwHiD5MMhOq_Q-oel1_yfmAaAiJ33nOUfLf_E-yEfpbUMO7oygmrz_X5WMlC1iVqBQpD5YAyic1X5BWew7RpG3zkl4fZqq_d7DO6zbwSkSEBvwxrKaAX2VKGa-wqd92pbsk0qOE8pvIuZQxQZ_xo6aqDzfPVZFDSi-n8gNCOdq5EUlefCrr9nAk1fIoYjw_He7kCTiFw53Ka5rJEEf_K9S5V2wiHX0dWLhDJqsKyBzC1BPJRnXjHNn37SRtBKxzOAh2f-U1SXUWqO7dUPl5kl194TxRWqtENLyiQY_Cmuj56BiQCoqlbYWQR0UH6CCkEDyDffE4NmClTV0lElkGRJAZThj1hjTVYZv1JgSvUapnNl7eiiAWfNqBEsKUoACi4bBYys-1wxgz3eF2T3j48t61xE-CT46WaGNPDiymFVSPO7twcRWrAlhBZhCFWoKx_hA750ZWmY1ZuDtxn0gEdY-UAJeZwf2ESLGrDXoN1pXO8US_byg0W2FdLuLbe6fnoBfku9OgWH0Jwlv9x9HYrDtipMW1AyrONY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dd84c2849.mp4?token=dFRDVteNpSL46fvGYcWaPtM-MEMsYi4n_yt9EoasiCJUqKCCIuZR-7u9sQN7So6W9snm06U3n4916fKrcwJUn4X_K8xzFaXJ2fDDjtMNvL1UuRRpoP7fdFmLKJ-J22PQqbt2npWAOqfwHiD5MMhOq_Q-oel1_yfmAaAiJ33nOUfLf_E-yEfpbUMO7oygmrz_X5WMlC1iVqBQpD5YAyic1X5BWew7RpG3zkl4fZqq_d7DO6zbwSkSEBvwxrKaAX2VKGa-wqd92pbsk0qOE8pvIuZQxQZ_xo6aqDzfPVZFDSi-n8gNCOdq5EUlefCrr9nAk1fIoYjw_He7kCTiFw53Ka5rJEEf_K9S5V2wiHX0dWLhDJqsKyBzC1BPJRnXjHNn37SRtBKxzOAh2f-U1SXUWqO7dUPl5kl194TxRWqtENLyiQY_Cmuj56BiQCoqlbYWQR0UH6CCkEDyDffE4NmClTV0lElkGRJAZThj1hjTVYZv1JgSvUapnNl7eiiAWfNqBEsKUoACi4bBYys-1wxgz3eF2T3j48t61xE-CT46WaGNPDiymFVSPO7twcRWrAlhBZhCFWoKx_hA750ZWmY1ZuDtxn0gEdY-UAJeZwf2ESLGrDXoN1pXO8US_byg0W2FdLuLbe6fnoBfku9OgWH0Jwlv9x9HYrDtipMW1AyrONY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریس رایت , وزیر انرژی امریکا
:
ماموریتی که نیروی دریایی ما انجام می‌دهد فقط اسکورت کشتی‌ها نیست ! بلکه ، جلوگیری از خروج هرگونه نفت یا محصولات صادراتی جمهوری اسلامی میباشد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22503" target="_blank">📅 16:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4abd87594.mp4?token=CfrATOSi4zF3ilAMxoiiVEOAtYnVZlO2ePjSfaI-kB-pLEdK4afy5ny7pbfO66wjC02Rj83dLpQQObRDLAbNHdVDbd-NBHozx0NcSdLrgh-9jG4wQ5EfNCKgKlBFoKf20_KfGlfoPD-PzbwSfLoSmg6tXFSxDUGuRdUirgLGbOtpX4f8XjUXXnPWWxXK2NsJJOZKQJG2czxCiAszRKzJv1Ivi98w_4Hh9Adtw-hEslbBVY2lJmJbNnyuszEnFL5F6xUBCLO57qL4N-04_mbZooTStHGWffM69fU350v0qtUkRAmrUbMj28mfaNhuZdD47gzT_VrjkdvVNiElUU6D3wrZ66IHLsZ-dZBEdzmzHFYJrJ8uSPqbOnqt-smNR_NnVlt2h_HTQ9V-ljMK-DRigDTTwjG5QKnj_MuX0wrYq67ldiHzVKchNcJU0LGZuJpAXSFMnISf-BYwy3mT8NM_nVxqoH5icxZtxIbQo0Zb-VfiN1mqHsd-cTL_jle9PysHgittfBoZ1rVHV43fVAkfAUC9HThXHCwuDRFg5YnV_1qm6ehzFRyfISFC2WJRipKjt_UE7b5HxAYVujU1PVNZMJYDh7Tpjky5d7A2r2Ky8VapNYFeseWSZSPhjMZZuCj8f1jFxLaCiVaAKp0fCvUxoA8kwHFXc_xikAZ1RvsfJQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4abd87594.mp4?token=CfrATOSi4zF3ilAMxoiiVEOAtYnVZlO2ePjSfaI-kB-pLEdK4afy5ny7pbfO66wjC02Rj83dLpQQObRDLAbNHdVDbd-NBHozx0NcSdLrgh-9jG4wQ5EfNCKgKlBFoKf20_KfGlfoPD-PzbwSfLoSmg6tXFSxDUGuRdUirgLGbOtpX4f8XjUXXnPWWxXK2NsJJOZKQJG2czxCiAszRKzJv1Ivi98w_4Hh9Adtw-hEslbBVY2lJmJbNnyuszEnFL5F6xUBCLO57qL4N-04_mbZooTStHGWffM69fU350v0qtUkRAmrUbMj28mfaNhuZdD47gzT_VrjkdvVNiElUU6D3wrZ66IHLsZ-dZBEdzmzHFYJrJ8uSPqbOnqt-smNR_NnVlt2h_HTQ9V-ljMK-DRigDTTwjG5QKnj_MuX0wrYq67ldiHzVKchNcJU0LGZuJpAXSFMnISf-BYwy3mT8NM_nVxqoH5icxZtxIbQo0Zb-VfiN1mqHsd-cTL_jle9PysHgittfBoZ1rVHV43fVAkfAUC9HThXHCwuDRFg5YnV_1qm6ehzFRyfISFC2WJRipKjt_UE7b5HxAYVujU1PVNZMJYDh7Tpjky5d7A2r2Ky8VapNYFeseWSZSPhjMZZuCj8f1jFxLaCiVaAKp0fCvUxoA8kwHFXc_xikAZ1RvsfJQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
حاوی الفاظ رکیک ولی به جا
,
دقت فرمایید.
⚠️
جمهوری اسلامی در یک تصویر
، خودش لنگان لنگان با لباسی ژولیده، بدنی نحیف و لاغر،خرکش بدون تعادل همه پرچم ها را یکجا را بر دوش میکشد
😂
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22502" target="_blank">📅 15:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">روسیه و کره شمالی نخستین پل ارتباطی میان دو کشور را افتتاح کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22501" target="_blank">📅 15:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22500">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الجزیره: حملات هوایی اسرائیل به جنوب لبنان، از سر گرفته شده است. @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22500" target="_blank">📅 15:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22499">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b12d040c7.mp4?token=JxmNbDbITkFCfSx8Rae-Ax5ljQovb5J5F3EOz5G5W-x5Vv4GTGPn16FVbLK3q4VUmUmCd8oFyNT5XWD-wbmBXKeK-Z5mAbf4dIKY8WQGQ9uwK5XZ0pIR29p3ZAJMc9B67_lm24oVo4mX-5Bpj7X1xGHhtV_4eLyRthTbIXMcidJuohkZLwhhJ0yUxRau22ztmy67Gl128Hp5aj2nHkP9rljEXyP_n9W8q_GrPoITndDltEqQDMasIxOdG93tIqCI6xXgYEkFfErt93Ys5zhefrivAZrVDuv-K-Xu6UoEBJDIwEX-_-rL3K9Dpo_3ysWmuTBKz-Pu14i3tnHNDU4uIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b12d040c7.mp4?token=JxmNbDbITkFCfSx8Rae-Ax5ljQovb5J5F3EOz5G5W-x5Vv4GTGPn16FVbLK3q4VUmUmCd8oFyNT5XWD-wbmBXKeK-Z5mAbf4dIKY8WQGQ9uwK5XZ0pIR29p3ZAJMc9B67_lm24oVo4mX-5Bpj7X1xGHhtV_4eLyRthTbIXMcidJuohkZLwhhJ0yUxRau22ztmy67Gl128Hp5aj2nHkP9rljEXyP_n9W8q_GrPoITndDltEqQDMasIxOdG93tIqCI6xXgYEkFfErt93Ys5zhefrivAZrVDuv-K-Xu6UoEBJDIwEX-_-rL3K9Dpo_3ysWmuTBKz-Pu14i3tnHNDU4uIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ اگه را داشت ماشین ریاست جمهوری رو هم الان معاملشو بسته بود ، یه ایرانی هم گذرموقتش میکرد میاورد ایران دور دور
😂
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22499" target="_blank">📅 15:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22498">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یک منبع اسرائیلی به i24NEWS: مشخص نیست جرقه‌ای که باعث شعله‌ور شدن اعتراض در تهران شود چه زمانی خواهد بود، اما خواهد آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22498" target="_blank">📅 14:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22497">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فایننشال تایمز گزارش داد
تأسیسات نفتی شرکت آرامکو در منطقه جازان عربستان سعودی امروز هدف حمله جدید قرار گرفته‌اند.
میزان خسارت در حال بررسی است و به گفته یک منبع مطلع، ابعاد حمله با حمله ماه گذشته به این تأسیسات مشابه بوده است.
جازان به‌دلیل نزدیکی به مرز یمن، طی ماه‌های اخیر چندین بار هدف حملات حوثی‌ها قرار گرفته است. آرامکو در حمله قبلی اعلام کرده بود اختلال ایجادشده
تأثیر قابل‌توجهی بر عملیات یا وضعیت مالی شرکت نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22497" target="_blank">📅 14:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommorteza</strong></div>
<div class="tg-text">علاالدین داشتن اعتصاب میکردن اطلاعات ریخت بالا گفت باز کنید یا بازداشت میشین</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22496" target="_blank">📅 14:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromyasaman sh</strong></div>
<div class="tg-text">یه دونه‌ای
دلم گرفته بود داشتم گریه می‌کردم. وویست رو باز کردم گفتی زارتان زورتان خندیدم.</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22495" target="_blank">📅 14:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2827c98c29.mp4?token=fFOdge7Kjb-RZ2jR0G5jxbtz6J-VSMYEbDysEHHG0Ig9ja8-iKKbHondghQlVV6YFmBmpTCizfsZxIjdu7GBum0PM-acFnnLU_7tUnsrV4rPV5KW3RPRa-6tg3ZUYXC3U_CmS-TlGWcxZWclqfVTkf6usJ5Lm6QqygYECUoOTchPb-yuWolaBP99re2cgS57PHilhBFBwBWrfsAvujiaSvlUdSwMHaKByhq6JRXZ-2tG32RZy7MBO9VRgmEqjsVnBR_D7h8pXgqG2BWOHS7WqeTr5np-6tf-16AHod2RWASXHclIFj9GgV9RWDaDzPzxsVH003hDlWQAZzU5bm-jpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2827c98c29.mp4?token=fFOdge7Kjb-RZ2jR0G5jxbtz6J-VSMYEbDysEHHG0Ig9ja8-iKKbHondghQlVV6YFmBmpTCizfsZxIjdu7GBum0PM-acFnnLU_7tUnsrV4rPV5KW3RPRa-6tg3ZUYXC3U_CmS-TlGWcxZWclqfVTkf6usJ5Lm6QqygYECUoOTchPb-yuWolaBP99re2cgS57PHilhBFBwBWrfsAvujiaSvlUdSwMHaKByhq6JRXZ-2tG32RZy7MBO9VRgmEqjsVnBR_D7h8pXgqG2BWOHS7WqeTr5np-6tf-16AHod2RWASXHclIFj9GgV9RWDaDzPzxsVH003hDlWQAZzU5bm-jpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : مردم شریف ایران، شرایط ایمنی حمل‌ونقل کشور به‌شدت نگران‌کننده شده است.
در بخش هوانوردی، گزارش‌هایی از اختلال سامانه‌های ناوبری گزارش شده همچنین بعد از‌جنگ اکثر سامانه های راداری نابود شده اند و از ترس حملات خاموش کردن عمدی ترانسپوندر برخی هواپیماها منتشر شده است؛ موضوعی که می‌تواند شناسایی و تفکیک هواپیماها را برای کنترل ترافیک هوایی دشوار کند و خلبانان در موارد بسیار بصورت چشمی هدایت را انجام میدهند ، در ویدئوی تازه در این رابطه نیز یک هواپیمای کاسپین در فاصله‌ای حدود ۳۰۰ متری از یک هواپیمای تابان عبور کرده است.
در جاده‌ها نیز وضعیت بدتر است فرسودگی ناوگان و مشکلات نگهداری به علت هزینه بسیار بالا سرویس ، خطرات جدی ایجاد کرده است. تنها در تازه‌ترین حادثه، نقص سیستم ترمز یک تانکر حامل بنزین در محور سنندج–همدان باعث برخورد با خودروهای دیگر و آتش‌گرفتن تانکر شد؛ ۱۱ نفر در این حادثه جان باختند و ۷ نفر مصدوم شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22494" target="_blank">📅 14:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نتانیاهو: ما به نابودی خرابکاران، پیگیری کسانی که آن‌ها را اعزام می‌کنند و تخریب زیرساخت‌های تروریسم در کرانه باختری ادامه خواهیم داد. @WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22493" target="_blank">📅 13:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نتانیاهو: ما به نابودی خرابکاران،
پیگیری کسانی که آن‌ها را اعزام می‌کنند
و تخریب زیرساخت‌های تروریسم در کرانه باختری ادامه خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22492" target="_blank">📅 13:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آمریکا و اتحادیه اروپا در تلاشن شورای حکام آژانس بین‌المللی انرژی اتمی قطعنامه‌ای تصویب کنه که پرونده هسته‌ای ایران رو به شورای امنیت سازمان ملل ارجاع بده.
جمهوری اسلامی هم تهدید کرده که اگه این کارو انجام بدید، جواب متقابل میدیم. بالاخره از ان‌پی‌تی خارج میشن.
پیمان NPT در سال
۱۹۶۸
برای جلوگیری از گسترش سلاح‌های هسته‌ای ایجاد شد و در
۵ مارس ۱۹۷۰
به اجرا درآمد. ایران
از دوره پهلوی
عضو NPT بوده و جمهوری اسلامی در سال ۱۹۷۹ از این پیمان خارج نشد و عضویت ایران ادامه پیدا کرد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22491" target="_blank">📅 13:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22490" target="_blank">📅 13:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22489">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1_9TwA-Zdcw00HYOLf7OEfYOoA9-u6nkyj5Yc6PC-yAWwzzOcmusLBoFPizE_xGCiqzA_XQ0IYd2vBXf4GurBzcePZZzYnAiRyUo8WsJoc_JXsfeYDVaiEgm_ZGu2hNtpTj42H4IDfKjfzjK02miC00uS6dtYVU8Z50GOb1c1_kfJz69BdPI2rzYRDgu9FMKud1ckFlkMgmHXQXryf1J2kliJLeglsOZEO0r5ADd81b1YrJQX22eg4q6RGfueYLHjDc0TQfI5cPD9t0uUZUzMQrhVCmLjH7IEd0cTFdybNl6ndqqwjTjhlnp2VRO7yFj80j1_TDTNcCaqRhGmZcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث ویدیو برنامه مارک لوین را بازنشر کرد:
در این گفت‌وگو، ویکتور دیویس هنسون ترامپ را
«معکوس‌کننده‌ی انقلاب»
می‌نامد؛ یعنی رئیس‌جمهوری که قصد دارد روندی را که طی۵۰سال آمریکا و سیاست خارجی آن را تغییر داده،
معکوس کند
. در مورد ایران نیز تأکید می‌شود که ترامپ برخلاف سیاست رؤسای جمهور پیشین،
به دنبال مهار موقت جمهوری اسلامی نیست، بلکه می‌خواهد تهدید اصلی رژیم را از میان ببرد
؛ به‌ویژه
توان هسته‌ای و موشکی و ظرفیت آن برای تهدید آمریکا و متحدانش
. هنسون این رویکرد را بخشی از همان
«معکوس‌کننده‌ی انقلاب» گسترده‌تر ترامپ
می‌داند؛ یعنی
شکستن سیاست‌های گذشته و بازگرداندن ابتکار عمل به آمریکا
. نکته امیدوارکننده برای مردم ایران این است که در این نگاه،
جمهوری اسلامی صرفاً یک حکومت مزاحم برای مذاکره و مهار نیست، بلکه یک تهدیدی است که باید قدرت آن از بین برود.
این گفت‌وگو همچنین بر این ایده تأکید دارد که در صورت
تضعیف قدرت رژیم، مردم ایران و نیروهای مخالف جمهوری اسلامی می‌توانند نقش مهمی در تغییر آینده کشور داشته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22489" target="_blank">📅 13:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADgTU3N1U9I2v1nNUlVJc93sj-Ph_NH3eBsuK9YrSQCF2iEigUx2kcl7Nowm6hElNl9mPYmoedbQteD1E_VSoeJMw8N26LTsdhdRSLNweXTFL6kk8h6l-DrTDFOJZiXDkpH_dvtt77ugevjWCz9lRhuTTE_T-xT3CV1KawgYLBU52G6xn9lWuh9-K0N_yIZqWwNuQk1hrLrLwQq978FcJ_86_qbSDc1wWZG4T0ZPZM_MixHKjGkBUy4dINY6h211or4m8UBwB31pyM4Ul7p--sgA25hNWUNPS3i46wPZgOMU6NOZZiqsnXl0r3g3idAbts4kVhEfuhefDN3k5jY-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث و نظارت بر نابودی قایقهای تندرو
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22488" target="_blank">📅 13:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22487">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dbc57d78d.mp4?token=E77vbBjsE7p3gbNXcotvI6drQCI4ceHxg_NMIAaZt5P2jGbkIT8WcpoVCnE14iGI8dXELeAhjwPU_9S5OJ3cmLE_MeJuRIx1uCqLsnf4M669MPnrMqqK9wGybuG4_Z0wcUOkjfZN-LjDxh4hkSBy0CborMN4yzNRApGAhA2Up0gBU-kNzd8Y1WYQJCRu_w7Cu79vgOx8NG8xm6x1u8zvwd4x7xVwagRUEAiFxmvqSD8zB_h-Go3XKTGCi77hs5K2v0nvN7Oz5VPqAq7t8ZH0ZNSKbJoetqjNx_3Efz4VmlKQ_OJmTTzbsVDVTLUm-jS322TqwUo-3HMR1hhK85qF1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dbc57d78d.mp4?token=E77vbBjsE7p3gbNXcotvI6drQCI4ceHxg_NMIAaZt5P2jGbkIT8WcpoVCnE14iGI8dXELeAhjwPU_9S5OJ3cmLE_MeJuRIx1uCqLsnf4M669MPnrMqqK9wGybuG4_Z0wcUOkjfZN-LjDxh4hkSBy0CborMN4yzNRApGAhA2Up0gBU-kNzd8Y1WYQJCRu_w7Cu79vgOx8NG8xm6x1u8zvwd4x7xVwagRUEAiFxmvqSD8zB_h-Go3XKTGCi77hs5K2v0nvN7Oz5VPqAq7t8ZH0ZNSKbJoetqjNx_3Efz4VmlKQ_OJmTTzbsVDVTLUm-jS322TqwUo-3HMR1hhK85qF1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادای احترام یکی از آسیب دیدگان چشمی به ناو هواپیمابر آبراهام لینکلن در تایلند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22487" target="_blank">📅 12:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارش های
تایید نشده
از منهدم کردن یک کشتی جدید در
خارگ
توسط امریکا
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22486" target="_blank">📅 12:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ارسالی : سلام یاشار امروز از تعزیرات اومدن گفتن تمام لاستیک های کهنه که جلوی آپاراتی ها هستش باید فوراً جمع کنن کلا 24ساعت مهلت دادن برای جمع‌آوری گفتن به خاطر این دوباره ممکنه اعتراضات شروع بشه اگه مردم لاستیکا رو از جلو در مغازتون برداشتن و تو خیابون آتیش زدن  خسارتش رو باید مغازه دار بده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22485" target="_blank">📅 12:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22484">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بقایی سخنگوی وزارت امور خارجه: ظرف روزهای آینده، تفاهم ایران و عمان درباره تنگه هرمز نزد سازمان بین‌المللی دریانوردی ثبت خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22484" target="_blank">📅 11:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بقایی: بنا داریم در نشست مجمع عمومی سازمان ملل مشارکت کنیم به شرط آنکه آمریکا ویزایمان را به موقع صادر کند
فرانسه، انگلیس و آلمان به دنبال تشدید اوضاع هستند، حتما ایران در قبال اقدام نسنجیده‌ سه کشور اروپایی و آمریکا تدابیر لازم را می‌اندیشد
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22483" target="_blank">📅 11:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2b940d08b.mp4?token=jCsM2YW8r2JZk6f1IHVOjYLVyG605wAp5NsVJObxhczg5OsW3O1ikY4AFRlcmb9RW1jr93N8slOIcEzkdjAhvUkOaVGS3EEo6khZX5re6VOfEEgtm8KDJ6gBr9_36WNU5m1QpDSRP2L8xoy0AiNEhNeLJ3t7ZWbV9467lDZxvckIVxJ2i619K4gZdOOCtPTaGynjgJOuyLgrUOKrTY5ncYP1_uHBf1IVK1p6Tty4sukmWUG98yNFl3Sg2-iKvN3y0kwxoD2wyWUKOR207-amL8RX7MP1yHmeXZvaMSJNgZFKJ3WElBeQiaMDu_oaqivoAVkqRbrxizk3aGDwX7H4u53m5oONdrqq-dMy98LPHwVJM_IRUY7MyrKCalYjr9wb9D2XLfhEBpNdCJ2X0Cya4fb1NSvP7Tjl-0bkVmf71jZ3lFMW9lds7Xc4p2vLwZ3T7NwVdJEBw1J1nSCM8a_zh8BKXzeBrBmQPlGN_H_Y3hJKsdn4OCDVvepfRpI6MDbKVgXkMrB-XfsaLvc40tEz2jwOJ4Z7oFmJMKNNP29SkrEyc0F3n9KY_Mfd9_LFK1bcmtKXioK6kBHoGiw_00k0DLhVzKTr6JnDACUumOHE8iKPgCv4OSzK5Snkr-4yweoNLArXH4p4eqWWB6JZ6s9TrrFwjBYyzhyMw_s6z-oVKAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2b940d08b.mp4?token=jCsM2YW8r2JZk6f1IHVOjYLVyG605wAp5NsVJObxhczg5OsW3O1ikY4AFRlcmb9RW1jr93N8slOIcEzkdjAhvUkOaVGS3EEo6khZX5re6VOfEEgtm8KDJ6gBr9_36WNU5m1QpDSRP2L8xoy0AiNEhNeLJ3t7ZWbV9467lDZxvckIVxJ2i619K4gZdOOCtPTaGynjgJOuyLgrUOKrTY5ncYP1_uHBf1IVK1p6Tty4sukmWUG98yNFl3Sg2-iKvN3y0kwxoD2wyWUKOR207-amL8RX7MP1yHmeXZvaMSJNgZFKJ3WElBeQiaMDu_oaqivoAVkqRbrxizk3aGDwX7H4u53m5oONdrqq-dMy98LPHwVJM_IRUY7MyrKCalYjr9wb9D2XLfhEBpNdCJ2X0Cya4fb1NSvP7Tjl-0bkVmf71jZ3lFMW9lds7Xc4p2vLwZ3T7NwVdJEBw1J1nSCM8a_zh8BKXzeBrBmQPlGN_H_Y3hJKsdn4OCDVvepfRpI6MDbKVgXkMrB-XfsaLvc40tEz2jwOJ4Z7oFmJMKNNP29SkrEyc0F3n9KY_Mfd9_LFK1bcmtKXioK6kBHoGiw_00k0DLhVzKTr6JnDACUumOHE8iKPgCv4OSzK5Snkr-4yweoNLArXH4p4eqWWB6JZ6s9TrrFwjBYyzhyMw_s6z-oVKAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاخ سفید : در روشن‌ترین روز، در تاریک‌ترین شب، هیچ پلیدی از دید من پنهان نخواهد ماند. بگذار کسانی که قدرت پلیدی را می‌پرستند، از قدرت من برحذر باشند... نور فانوس سبز!
کد سیگنال این پیغام
:در داستان اصلی «Brightest Day»،
Entity منبع اصلی حیات و نیروی زمین
است که پس از حملات نکرون و نیروهای تاریکی به‌شدت تضعیف می‌شود.
Entity به دلار آمریکا، منبع اصلی قدرت اقتصاد جهانی، تشبیه شده که بر اثر سال‌ها سیاست انفعالی و بی‌ثباتی‌های ناشی از جمهوری اسلامی تضعیف شده است.
حلقه فانوس سبز نیز نماد
اراده، غلبه بر ترس و ایجاد تغییر
است؛ و جهت‌گیری آن به سمت سرزمین ویران‌شده، به حرکت ترامپ و آمریکا به سوی خاورمیانه و به‌ویژه
ایران، به‌عنوان مرکز ثقل منطقه
تعبیر می‌شود. در پایان داستان، نور سفید نگهبانی را برای احیای زمین انتخاب می‌کند؛ این تصویر نماد
آغاز دوره‌ای تازه برای بازگرداندن ثبات و امنیت به منطقه
است.
پیام نهایی: پایان دوران مماشات با جمهوری اسلامی، اراده برای تغییر و آغاز روند بازسازی نظم خاورمیانه با محوریت ایران
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22482" target="_blank">📅 11:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مدیرعامل شرکت فرودگاه‌ها:
۲۷ فرودگاه در جنگ آسیب دیدند
که آسیب‌ها در سطوح مختلف پروازی، باند، ساختمان های ایمنی، دستگاه‌های کمک ناوبری و بازرسی، ترمینال های مسافری و...بودند.بارها گفته‌ایم که بعد از آتش‌بس جنگ ما تازه شروع شده است.
بازسازی آنها کار سختی بود، ولی انجام شد، زیرا در بخش ساخت و ساز فرودگاهی توان خوبی داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22481" target="_blank">📅 10:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf4f398265.mp4?token=QmjOOpZLoM0BxKej5y-otl53xPDah_mipa0-Szx0FziymQoy_YSyVdYLGp51Df-X57eD3tcfj-dXGkfUWkaZQt6mdyTV8AetrPUqo1X154eA60zb-uAZNU9ZbRXiZ3rARr5I04gF7QWVMJbijZ4Rvh9m83ripEtu9jbOxLJVvkGes0m2OFDfTm2eDf95z-et3tAPYU_jO3D14-Y9fraPoWvlq35inm7rzeVgEDczhTp3iFDIjMlePOZA9ptBAO_XfJOQ_bS9ApwuZ8J6WDk-DXKrDi20Fe9ZImhG3rGV5p5jAXvOUBj5RQ_dMqPYTrGyUa0FoAf8J_z-Vs_QRfVovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf4f398265.mp4?token=QmjOOpZLoM0BxKej5y-otl53xPDah_mipa0-Szx0FziymQoy_YSyVdYLGp51Df-X57eD3tcfj-dXGkfUWkaZQt6mdyTV8AetrPUqo1X154eA60zb-uAZNU9ZbRXiZ3rARr5I04gF7QWVMJbijZ4Rvh9m83ripEtu9jbOxLJVvkGes0m2OFDfTm2eDf95z-et3tAPYU_jO3D14-Y9fraPoWvlq35inm7rzeVgEDczhTp3iFDIjMlePOZA9ptBAO_XfJOQ_bS9ApwuZ8J6WDk-DXKrDi20Fe9ZImhG3rGV5p5jAXvOUBj5RQ_dMqPYTrGyUa0FoAf8J_z-Vs_QRfVovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏خبرگزاری عراقی «بغداد الیوم» گزارش داده بیش از ۱۵۰ نفر آزادی خواه ایرانی به محل اسکان دانشجونماهای عراقی گروه تروریستی «حشدالشعبی» حامی جمهوری اسلامی در دانشگاه سمنان هجوم برده و شماری از آنان را مورد ضرب‌وشتم قرار دادند. تعدادی زخمی شدند و ادعا کرده پول، تلفن همراه و ساعت برخی از آنها نیز گرفته شده. گزارش‌هایی از تجمع مقابل خوابگاه و محاصره تعدادی از دانشجویان عراقی منتشر شده است. پلیس رژیم جمهوری اسلامی در محل حاضر شد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22477" target="_blank">📅 10:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc3ca6006.mp4?token=rXdgBr4rY2rtKfrrYdRky8e9zey15Nh_cVd9PULQoDvdK8cAelEuU-1IO7FmIXzrzhA6OEaoq8ATYR7pvuTPKlidj3rN9o4nHyoyJ6dqE7qLsgyMhCIoFk7nl0WjSgGMKXcVwdeUdwQB37KmtoxL0NDm-WWxB44DP5iCqtQQPnRqoC_3kTfHoAWXU1PgE2kAuc-MTn0qw8uINXSFQtlkEWRLbvrGsED-tkAjbSqnaI8WlSic398VKTQbjbXKJFxmg0P070kbHI9WU80zBiYY0PVKmHgZXio90cLD3XPoRGI7SroWZR4ShAo_sw6oMI3Wbz7fycBJONkZgEF47fX_ejkTPq57mtb8E6AXfRgWjUR-E_UX1DMOrdYBHY18lcsykkz2_lEEG1OjoHvciJwTA4RsU1OoQWakFsEkiT0RMBC8-AIhGRi_38XOyhXqmhNBjoxfyyaQAFuY1bO9ThTx5ZX9mtWJ08wxVHaBeogt0k1u5WY92dEhIrSzDXL6n80G8UmybzxaTJTCvFx4xXJpd5dNT0lKewLs4m3bOGeFFEqcmBEP7hXYnwhmkVlKIxAK9yq-6P_5vExR_xvo9BCUYMGjWRa3w3DZVgZjOX4eccgKSc1vpCWFn9fmPX9mmCpUunH5TAaSaTxD3RkPhpIFGqB5NBLdn97Ti1m5UCtb3Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc3ca6006.mp4?token=rXdgBr4rY2rtKfrrYdRky8e9zey15Nh_cVd9PULQoDvdK8cAelEuU-1IO7FmIXzrzhA6OEaoq8ATYR7pvuTPKlidj3rN9o4nHyoyJ6dqE7qLsgyMhCIoFk7nl0WjSgGMKXcVwdeUdwQB37KmtoxL0NDm-WWxB44DP5iCqtQQPnRqoC_3kTfHoAWXU1PgE2kAuc-MTn0qw8uINXSFQtlkEWRLbvrGsED-tkAjbSqnaI8WlSic398VKTQbjbXKJFxmg0P070kbHI9WU80zBiYY0PVKmHgZXio90cLD3XPoRGI7SroWZR4ShAo_sw6oMI3Wbz7fycBJONkZgEF47fX_ejkTPq57mtb8E6AXfRgWjUR-E_UX1DMOrdYBHY18lcsykkz2_lEEG1OjoHvciJwTA4RsU1OoQWakFsEkiT0RMBC8-AIhGRi_38XOyhXqmhNBjoxfyyaQAFuY1bO9ThTx5ZX9mtWJ08wxVHaBeogt0k1u5WY92dEhIrSzDXL6n80G8UmybzxaTJTCvFx4xXJpd5dNT0lKewLs4m3bOGeFFEqcmBEP7hXYnwhmkVlKIxAK9yq-6P_5vExR_xvo9BCUYMGjWRa3w3DZVgZjOX4eccgKSc1vpCWFn9fmPX9mmCpUunH5TAaSaTxD3RkPhpIFGqB5NBLdn97Ti1m5UCtb3Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخیراً تماس هایی از مبداء نامشخص
(شماره نمایشی سوریه) با مردم بومی جنوب کشور حاصل میشود و درخواست میکنند که طی درگیری های پیشِ‌رو هیچگونه حمایتی از سپاه نداشته باشند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22476" target="_blank">📅 10:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS.A.H74</strong></div>
<div class="tg-text">سلام آقا یاشار گل خوبی من بندرکنگ هستم سمت دریا ساعتای ۶صدای مهیب انفجار اومد نمیدونم چی بوده</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22475" target="_blank">📅 10:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">العربیه: در حملات اسرائیل به کفررمان در جنوب لبنان تا این لحظه 9 نفر کشته شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22474" target="_blank">📅 10:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رویترز , تنگه هرمز در پایین‌ترین سطح تردد: داده‌های کپلر نشان می‌دهد میانگین عبور کشتی‌های حامل کالا از تنگه هرمز در ۱۰ روز گذشته به حدود ۱۰ کشتی در روز رسیده که پایین‌ترین سطح از ماه مه است. همزمان ایران اعلام کرده قصد دارد یک منطقه ممنوعه جدید در نزدیکی…</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22473" target="_blank">📅 08:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش صدای انفجار یا پرتاب موشک از چابهار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22472" target="_blank">📅 08:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رویترز , تنگه هرمز در پایین‌ترین سطح تردد:
داده‌های کپلر نشان می‌دهد میانگین عبور کشتی‌های حامل کالا از تنگه هرمز در ۱۰ روز گذشته به حدود
۱۰ کشتی در روز
رسیده که پایین‌ترین سطح از ماه مه است. همزمان ایران اعلام کرده قصد دارد یک منطقه ممنوعه جدید در نزدیکی تنگه ایجاد کند؛ در مقابل، عملیات دریایی آمریکا همچنان فشار شدیدی بر مسیر صادرات نفت ایران وارد می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22471" target="_blank">📅 07:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs7Aoe1V9n0FzvRwDJbmEeN6gK7DHbpuIJG54Pw_3wwCWoG3SmJx6hj7AIDhUmgZVeDXzRdu84rgsSfg0CraHRefy-XxM76MQF0x2c77QF7PLn08G2xGtZPhACtHc4Ue1a1GpGmOJu31_HmDBcTzH1IqTcFnbksRJM4Ls0be6kCKVIIJwoxNZCCaqtiVl-d1Nr2suzQDoNPXwGupI-w9BXHqZOGQ6WBctGQHWQL3lli01parqdPjYz0OQVicF1RIceEBl8ppBztBn89MSZTipgheiZ7kVM9GpuA4lmMCg9BJmfTYbkG4IQgoe6IhVp4OY1Q2Wqqu4LwA0peREjsRrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : سلام یاشار جان امشب اینو دیدم تو خیابون تهران رو زمین بود ، به نظر از این تراکت ها تو تعداد پخش شده باشه تو شهر ، آخر این حکومت رسیده و جشن آزادی بزرگی قراره بگیریم
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22470" target="_blank">📅 00:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQzwMSmTOzGtGhvnSI03CHeAfMlHfBh_0Ro0qQwFGNjBbtKf06QWWoiVPCzD3gUKPcBVfdnbLvN6wWHydQ5c-qkRo1tBLGyHueu2MritIRjXKrThtmVXHEwOYgXaGjBriw1dFhRvDW2QUWucbl_P_v2Nc4A1drGJO1ot4ADB_WNuYAHbAMoXUXQb9KcApKUU503Ng6OckZezQiqhKrNypre1Tv-2tLR3rhLpZ6NOaLyhFXVuoNCuA2beq83yK2QHXqVqFt-PgEHs7NX7L12qNpQNUixgL-nYkxye2TY_-r2nfrDJKu9RRuBrddqbfA6TNEs7F39CwemchQS7fy0m2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنی که جمهوری اسلامی او را «شاه‌مهره» می‌نامد، اکنون در زندان قم جانش در خطر است، برای نجاتش کمک کنیم
نازنین برادران، معروف به
«رها پرهام»
، پس از اعتراضات دی‌ماه توسط اطلاعات سپاه بازداشت شده و بنا بر اطلاعات خانواده، اکنون در
زندان قم
نگهداری می‌شود. رسانه‌های حکومتی مدعی شده‌اند او
معاون و دست راست بیژن کیان
، رئیس اندیشکده «صدای آزادی»، بوده و برای
هدایت اعتراضات و اجرای طرح براندازی جمهوری اسلامی
آموزش دیده است. آنها همچنین مدعی ارتباط او با
آدام لوینگر، افسر سابق پنتاگون
و دیدار او با
تام کاتن، سناتور آمریکایی
شده‌اند. نهادهای حکومتی همچنین می‌گویند او در تدوین ساختار حقوقی دوران پس از جمهوری اسلامی نقش داشته است.
اعضای خانواده وی به من گفتند که او قانون پس از براندازی جمهوری اسلامی را نوشته و آن را به سازمان ملل برده است.
اعضای خانواده وی می‌گویند
او از نخستین روز بازداشت ممنوع‌الملاقات بوده و حتی اجازه تماس تلفنی و شنیدن صدایش را نداشته‌اند
و اکنون
کیفرخواست پرونده‌اش در حال صدور است
. خانواده نسبت به وضعیت و امنیت جانی او به‌شدت نگران هستند و خواستار توجه رسانه‌ها و نهادهای حقوق بشری به پرونده او هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22469" target="_blank">📅 00:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Akqkrm3yo3uDGw9USuC3tNKO-8mkDMcwCDlOUPFmNPoqjWSxZXUtK--mOFthSyM6u8eoZ9g9EqMQykYu1ar2mYCOPMG7i4wYdBsWJS-W_oUJEWSZIGYPKx-n-uY_V-gmKPB-iHpsyl011kTRsgwcAIdGbnm0TQQ54D-YHvQOToYOonbYTrRFYNPKNKqheXTkYyHYpGAwTJtj9c2ouB1JrDRpidVI4_wIml5wm6xn3XNg0HCHNnNdAJ5SPkbo0rUgF_g0iD8H5kJ2TnUf0cc8DKGoTl65SMddUWFwOg5z4b2130bBvc97FZcsBdkBro-LOPMumeQEBHo69nbPz544fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری میان نیروهای امنیتی و مهاجمین در زاهدان؛ بر اساس آمار اولیه، ۲ تن از نیروهای امنیتی کشته شده اند. @WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22468" target="_blank">📅 23:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">درگیری میان نیروهای امنیتی و مهاجمین در زاهدان؛ بر اساس آمار اولیه، ۲ تن از نیروهای امنیتی کشته شده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/22467" target="_blank">📅 23:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onCa5S9hxEPnzaQM7rKEaIS5WB8kbIxNAfZq6sNdPBDS0c9aSVe9pWCV05GK5-fzMPGg7S1XH1pLG1TXOU_Z0fXvZK_oxHB4wj7g027USRobx9aqmMTVC1DSuqtVwQ74m8L1AFQkoBvfRaDpN5IbM4kha62u6lZ0Oq-1CsFmpesRtwyu-a1cVWsE8nGJTDk_zqkdHOOyCzqtIVSuaTIVJIvekj6ibVtagNXh9nB_1WXCXTj5WJOD5gKUbm6o-foR3jgJgIb3FP3b3igUl930HcR3W2laI3LuCJ4XjGt6sFyzh5nXtLhCaVKmK0YGbkpYQ871Exp0i0-GHH5PXOrw9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران کشوری در حال فروپاشی است.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22466" target="_blank">📅 23:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMarVvv-djPjeC6_vaC3lDhb_hWv_2NRNxyCLbn2-dTSipinNhKtcf37gJrZmuTbJK7yskRIX2jZl3IJaN-u-4EH-39D2NDp2Mh5ZCMtqcxld92VU_Bd-ep7tRoQOtqO_P_kmy7CdASt_epOcVWYPOSWWXxAIXIeHVtnfN3P3Xt8WcKy8MXUgI9rWNc3D4EfoGEuOlETihXX7rAwPyHM4IY1khS1pha08TmSJSjGARKbrdeZbZhVzU-i7JFe9tcr4hpWPjvjT7upwpeOwzBMdzyhdUexaBWT4mId4ozr0RkIsatZxadG9CqxyuVq6xfVu5FLzQjkHYPunPWLlXRIGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : حجم نفت هرمز برگشته است!
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22465" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
