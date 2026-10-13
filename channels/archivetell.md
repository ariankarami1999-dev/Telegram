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
<img src="https://cdn4.telesco.pe/file/NyyQXODx296Ul0I2fe8VnDpI_XRWPIvsSadZj3VH2RgQ_lsAIpsETtXTwoSkZ2uIVOvQXsXqo7sPf9Ch0Pw2iSwBTpizLjjxjoeTcTU0CzHxEl72fcaX91f0ULKcdLlW62aPseQCCvUf1E7ZB1XpGYOja1lcARX6Wt5LuXLT00KkkerU2whwt5AS2vNCJmRMINAp_RqXMx8oPlS9Yqb9BIlE-X_NjOfJtD2pbS4-bM8AaiJs6CzWTOPgULr4PLPsQBUHLrt3jiBvlJE6hWXItothLRiZa3FZZGCxn-7aSbDo5p4VQXmSeM_wndMETVaxQHOxwg8voTlJ7hLf_6R4jA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌بازآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 08:11:45</div>
<hr>

<div class="tg-post" id="msg-8084">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctAh-mHmPvgCXrWTonvNRCuaorq7KclPaL-lhAvPus3Se-c_J3oOhidmDOJ4QgzDW3QjGftw6b2z5ySnd8x4nBRSCT_Gl720gvF0JoHc7amP-GOT4uRg3BOuBrLxGogOHLNJt6l9seOay5RoVj0q7mCebDox-Xu6jrPRlt_XAGeRIRke1cIDSnI2r_e1vqPzTAx2vXtSBu9EAq3wLnBl41L9fcW4lQatfa1_Ps-tEqZbY8t6Vk1BrqjmwQkPunCF_RhZJUtzUtfWgGqiEU1_IBkfE_xsnIQL4aarHkqpq7UbOpBncgRg0yeJC10gzhoWdfJKR5_UXKDf3HebZnI03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧹
ابزار Ubuntu Cleaner برای خلوت کردن اوبونتو
⠀
‏کش و فایل‌های اضافهٔ اوبونتو رو با چند تا تیک پاک می‌کنه و جا باز می‌کنه.
⠀
‏• پاک کردن کش مرورگر، کش بسته‌ها و پیش‌نمایش‌ها
‏• حذف بسته‌های اضافی و نسخه‌های قدیمی هسته
‏• حذف نصب‌کننده‌های قدیمی
⠀
‏رایگان و متن‌بازه و روی خود دستگاهت کار می‌کنه؛ داده‌ای جایی نمی‌ره.
⠀
‏نکته: روی اوبونتو 24.04 بعضی‌ها از بسته شدن برنامه موقع انتخاب بخش‌ها و نبودن گزینهٔ پاک‌سازی هسته گفته‌ن؛ موقع حذف هستهٔ قدیمی احتیاط کن.
⠀
‏
📦
صفحهٔ ابزار در گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 844 · <a href="https://t.me/ArchiveTell/8084" target="_blank">📅 23:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8083">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙎𝙪𝙥𝙥𝙤𝙧𝙩 «👨🏻‍💻» پشتیبانی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruMZLRmzIa_E9BmPbC4zP_bkKk4D1nze6MLkC_mXZVkKS9kzrJBBzbJ6QQZUzDODhQcc17VPmUo5Jp3moalbDGm2DEoOodrNCVoNO4-2cdOEnHXDh3E-GYN4vOfYChp_Nd3EYQXxjn_fOttluHL2EoCxnC9zmYn32CiahlQvIxS0GucrimRhrMgysKN63Q8-UcQ-SNK8A5xZhReI_nhG1OeZzz0H3DDQaYv4gQQ4zJLO1WKfVjHFk4kA674tKP84n1ntiX-XrHVyhjUfmuaaOoBbZQsWfGaYPuWGc6xk5I8zUElOZ7l7TorGum7XQ7L-7LEvPMWp8JUUA_z6C-DJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این متن رو داری میبینی
یه نشونه‌ست برای آغاز مسیری جدید از زندگیت تا یاد بگیری که چطوری،خیلی سریع به موفقیت برسی!
💸
✅
اگه میخوای درآمدت چندبرابر بشه
💰
اگه میخوای لایف استایل زندگیت متحول شه
💡
وارد کانال شو بهت یاد میده چطور دلاری پول در بیاری
اینجا میتونی روزانه درامد داشته باشی و سرمایتو چن برابر کنی.
لینک عضویت کانال وی ای پی
✅
👇
👇
https://t.me/+lrPbGswgqLQxY2Fk
https://t.me/+lrPbGswgqLQxY2Fk</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/ArchiveTell/8083" target="_blank">📅 21:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8082">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/ArchiveTell/8082" target="_blank">📅 21:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8081">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIcw-3ofIy0Hz1OwqP6qM27RXxXcS4IxvmmvJZbgUg3Se9O0obIOWfrWWeR4PYBIpY1jMHDXuneUhH6H3VwBbpNYszSG-7pZgi5x3q8LWbbXbj4Q6ty1oHcfd9a5me5kfRDcLZNNmxMiSMeWNq9rSrCvqg9ArPp70WlpUczYMIv0e4I7_z9s75WU8jV-62jhDJmS699Tf8hU1lpbqTl-qenModI4-5oQRUt4GDeogsQbmZA1fkUmqzbldRyHSo-iwayM9oUMOyidoGVeaTc4el9cuzEOMFOUl1JmX0bUj3QFjZb7KdO4EN3pvJ2OGITokzSKKL4yo-8vk_sr2gzc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک این مدل ها در
Artificial Analysis
منتشر شد
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/ArchiveTell/8081" target="_blank">📅 21:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8077">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEIjjVWyvT_9N7SVfd6FFXzNgd79LRIiHEqDcGS9z0VRlq9UNr2NsoXk9VviR38hV4vun_l01uczTfnuYwx4Q6Q5x28Gyqid3C3Wg5IIMddmIjvq4v7H9AjILooT1SNBeMOQl5ivA60xMrkW66fRwGktFWmzlSorCKpvDs1BundsmXuU2JcomNoCjjjSp_bSAZbdkl7ljEzD5MZlqPS8R14SLRI9vGwQcuE2kF0T8_A0-igRWE1P3CjYoCOc_VOsmHQa0bhakkNPfp64DpZ4Qa4lFldRDLMqgWjeDMqkJs7pLbjVo-L6nw_lPIJaHTIVPPnA_bHvLqECH95QHWRFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHqSoFOpuy-zMWmbo4yNyfOHIbvSkW1b2OzTMxk7lcKQGBolDJn7THXJgjKM9qXm19nT6dKnnq6koE3AK4Y6qGgFbtkG1N3UNSfH0UGsgmQisyoAgCeU_vf5k5pueSg71JZURK5deEdeJjUaWuz2mvHMU8lN6nJfhbnT7aEGM7rxfW5aP3NUcWMJoyqD5rJUXes63tMr_GV5ME2VypaDIPAokr1EJ29QLwy7fskK2yvpb1_OB2KVwkyspyzgbAlH6LN2wW57LKoU3KBYWCkAWToGh6XIlVlB6EU-r4HX4DB31zb--LSKIN6aqdViX6mneWyC0KxqcZLA-7BKgbaMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JV6n8mS0SXHE6ijBRr_H1-kLKymNxe9j2YoteKSTkl-_B9-nBzRSgq1hIPshQKs_d79bFoREUYqxOWWyP_n_XQ6FVhbc0GrQKgl_3IZnsyt-cIKLkF0irUmIR1G3C0gDvs0hgSOqNwj-4QhyKSGWbRk6TGQexb28FtKxEiB5nmPOviKrTf7aDasH3opN229JZBpB3r8Zpmb6UdDbjapneuN6TSYlcpHCbXOKypGL3j6_JCtqTFHVtC4rnNkXsjDe7HlUDdidCkUZaIcCFq0TEgTVeqAzOXlDJEm3Doa1JCXrig-WBzKOud1E27z8pejvZAwCwnnV-cY_YyuyGMnVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDj3HYq6IHiO6ZYxSp1b20KFPphXKJHjAA8oZFltNQjqnJgHLccseMww4RF8neReb47-avu3wgup837d6bWN6A0SzYBCvmdk5CbinadKEvmfegnr8L69SEOupfVg50ma_Zbr6r53SWs6dM41dKvrH8Y7xfbnpZGD8sAeoK6GXfYX7Pn3xiNqpOASTHgdMe1JTZJU7diXEpw_jWXQM1zmb16NsCHj5YxPCKXpp6O2WoSVnGb8tYlOcPBFSXE_GEl6tA5WOh28rK1jyvNQgvbkH13D5_QevqPmG_IgnSlthuboLY0xS2iT9Evv0AOn0hyoaEc40WxIG6IeUzdPYkxdKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🚀
معرفی مدل‌های هوش مصنوعی Muse Wonder توسط متا
‏⠀
‏متا از مدل‌های هوشمند تازه‌ش برای انجام خودکار کارهای طولانی و کدنویسی رونمایی کرد.
👀
‏⠀
‏— یادآوری خودکار پیشینه و جزئیات گفتگوی کاربر
‏— کنترل مرورگر، حل بن‌بست‌ها و تایید گرفتن قبل کارهای مهم
‏— حل بهتر مسائل پیش‌بینی‌نشده به لطف پیش‌آموزش قوی‌تر
‏⠀
‏مدل پایه تو Meta Model API و ابزار Muse Code در دسترسه، اما استفاده از Muse Wonder Full فعلاً فقط با تهیه اشتراک ممکنه. هزینه این مدل به ازای هر یک میلیون توکن، ۴ دلار ورودی و ۲۰ دلار خروجی اعلام شده.
💵
‏⠀
‏به نظرت مدل‌های جدید متا می‌تونن رقیب جدی ابزارهای کدنویسی بشن؟
👇
‏⠀
📌
بیانیه رسمی متا
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 990 · <a href="https://t.me/ArchiveTell/8077" target="_blank">📅 21:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8076">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY4dQpcGktcr4Kh1SRadvCcLuzpB0B2mGU3P80M0ewJqYoPd-SjaUYpE3VwitjlCh8jJdAImsuuvhdAtujJdoIiGn3cP2dY_LHct5yeyH9yEmFxdWpPJXQLIEALgc0HWaTAz0YIAVRVlpZuBC5ozn01A1VmvEQDoITov8zXARaH1nK0Bw1igZ0la7MrsiyrM_OC1Y4fkbLFHt4YZc1WpgzjANSO-VxKnFFyn5tmYdCVHd_ogeFPJeyLb8VaTSdZcbEn6oTMkrrBjLh620WsoD-tjIootT8igy3Imxc8lwZDzHmdax_xgJVF5MqlGL7Pm_PPcBEZRuXM1KduZuSAzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعب
گیم های جدید
https://tehran.velestudio.com
GTA Farsi
https://gg405-golden-gate-racing.surge.sh
Driving</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/8076" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8075">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6lEds4Ss1Oe-N7WszB9Eyp57Gn5Eao0G6ZaLRFJcDYCv-lO1_pIS-_dry-6m7_X-_kODSi_vDpm9hrYItWCcvX7MB-6nh_DD5F5CD_Ob7YACXkWqXlcxUVY9YcQB08B9MClcywPlfTChQovLahk7E-T61QR0hexDEs31Z_DDOLmapqOs49dTLpAkS0STaShkM7YVXO-xthro-qBPlpMeDUnwG2dawHM5yJCTzuZQD9Xz4EuuWqk6zVn1Hwgwihc2j-OE3834iG41zYrxAwv-0p09yIiXmQiiKW-Eber-tr2lo1PhnoLbBx_VSmvcA220eEkN_6mDMyJUKSf0f_CuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💬
چت تیمی EdgeChat بدون نگه‌داری سرور
‏⠀
‏این سیستم چت متن‌باز کلاً روی زیرساخت کلودفلر اجرا می‌شه.
‏⠀
‏• گروه و پیام خصوصی و صدا و فایل، با مدیریت و دعوت اعضا
‏• پل دوسویه با تلگرام؛ هر طرف از ورودی همیشگی خودش استفاده می‌کنه
‏• نصب و به‌روزرسانی خودکار، بدون نگه‌داری یه سرور همیشه‌روشن
‏⠀
‏نکته‌ی حریم خصوصی: رمزنگاری پیام‌ها سمت سروره، نه سرتاسری؛ پس به محیط اجرا و صاحب کلیدها باید اعتماد داشته باشی.
‏
📌
صفحه‌ی پروژه در گیت‌هاب
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/8075" target="_blank">📅 18:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8074">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRDiMlxMNFugli02ImZaXc3yuNmEgJTQsVxLLbAvLoObi2hzlX07bDsFzxzpneWaZboNl7rwYt6T7s_gZ7AVQfd-8ag_j1pfSNwIJwrWbFvX5ALhkOB7biRTmj-ZNY9OWKm_A7eKjSY8ctAAKHm81Y37vdAvzmM5Vm55vMiKfiz3hiARfQhvHQEAdHPOj7huZKBa1pkIxqdy6IYvqB62YqfSGk0FJsV3A26lhXwORY9pIoqJaPNkO9D4PdoCPp9kDJ2xoPNqW-V3mshWFFo0Swv5lIScet6YfeMof856HZ8eD3glRPt8UyzbDZdGetvL24FYylJpSRdHPoQl0xMH-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اپ‌ Gander‌ برای باز کردن همهٔ فایل‌ها
⠀
‏اگه گوشیت ده تا اپ نصفه‌کاره برای باز کردن فایل داره، این یه اپ آفلاین همه‌کاره جای همشونه.
⭐️
⠀
‏• ده‌ها فرمت: ‏PDF‏، ‏Word‏، ‏Excel‏، ‏PowerPoint‏، عکس، ویدیو، صدا و زیپ
‏• بدون هیچ مجوزی کار می‌کنه؛ حتی دسترسی اینترنت هم نمی‌خواد
‏• حالت شب برای ‏PDF‏ و ‏Word‏، جست‌وجو داخل سند، ادامهٔ مطالعه از همون صفحه
‏• حجم فقط حدود ۵ مگابایت، روی اندروید ۸ به بالا
‌‏Gander‏ متن‌بازه (MIT) و همه‌چیز رو روی خود گوشی رندر می‌کنه. چون مجوز اینترنت نداره، از نظر فنی نمی‌تونه داده‌ای بفرسته بیرون؛ فایل زیپ رو هم بدون باز کردن، مثل یه پوشه نشون می‌ده.
⠀
‏
📌
ریپوی Gander در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/8074" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8073">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JJ1z1ua5NDt1KAOD6gTQBzjjRTDs57tO2b2WCk9hCPIzRxgySayjK4gUeh9nT8qCe9176LcOjmngWnpiqjEYYowbQJQbq-I6rUNstmeXtlRaUB9yoNNg42EGORYtBh-IL7ICDWCChjJ8H0bCWgblcUtoV4Ti84-2f21EX-a3-PQtYGjCMFjtO5zbL80KnGXsz76KnCETEjPSAT95Cy9xKI3nFpbXzUzM83__OjJyQvnCprGGnNGQJrzqzArNYdY26V51hlz-y_mnUk2d_SMRa-1DOiVfiYrAxK_QGtTSe-_mDEeb74P-fA0wyxQltuP4d16pFlQE_8kikCVqVhz0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🐧
خالق لینوکس از هوش مصنوعی خوشش می‌آید
‏⠀
‏لینوس توروالدز می‌گوید برای کارهایی که در آن‌ها ضعیف است از هوش مصنوعی کمک می‌گیرد و برنامه‌نویسی را برایش لذت‌بخش‌تر کرده.
👾
‏⠀
‏در گفت‌وگوی اجلاس متن‌باز اروپا تعریف کرد که رابط پروژه‌ی سرگرمی پدال گیتارش را خودش نوشته بود ولی ظاهرش شبیه دهه‌ی هشتاد شده بود. خروجی اول هوش مصنوعی افتضاح بود؛ وقتی کد خودش را نشانش داد و گفت چه می‌خواهد، نتیجه بهتر شد.
‏هشدارش هم روشن است: برای کار واقعی و مهم باید خیلی مراقب بود. با این حال سبک کدنویسی با پرامپت را برای تازه‌کارها راه خوبی می‌داند تا لذت ساختن را بچشند و وارد برنامه‌نویسی شوند. این‌ها نقل گزارش گفت‌وگوی اوست، نه توصیه‌ی رسمی پروژه‌ی لینوکس.
‏⠀
‏
📌
گزارش گفت‌وگوی توروالدز
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/8073" target="_blank">📅 22:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8070">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">samsung_root_guide.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/ArchiveTell/8070" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💎
آموزش کامل روت کردن گوشی های سامسونگ
✨
فقط گوشی های سامسونگ One UI نسخه 8 به پایین قابلیت روت دارند
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/8070" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8069">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpqdNIkw2g7PQbwroLUCjw7B9D7Rpb7WFHhbQIfoeHHjS5aOVIjbvuKzVpye_-VxiUADfZDJKP9p3T7qYgHbxIGZxfERyDKrdoyQA1AiEmLdBk2et9bIjpI7etiFOti_nbWrdKDM_cnXROiDgiHb73iPSvL7ucHZrREtrFk3nmf_2x4aUf5UGXq_PVCuKg8nTOok4YO9XMv5VyK33-q7mmYqJAcG8W93rGIVLtQShK_NaV45Ba20VXxqItk5jxQIASzWaJ_bD8XKEMgPNl3WenTOtq_6xrvUo9T_JPqClaPKB7GZAouqoTzw8PE11eC20xmMEKtI8Dfk9tOznfTDbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
دستیار هوش مصنوعی شخصی‌تون، فقط روی کلود خودتون
با
Talorys
یه AI
Agent
متن‌باز و کاملاً خصوصی داشته باشید که روی اکانت
Cloudflare
خودتون اجرا می‌شه
قابلیت ها :
😀
چت هوشمند
😀
حافظه شخصی
😀
تسک و یادداشت
😀
یادآور و اتوماسیون
بدون سرور اضافه، بدون جمع‌آوری هیچ داده‌ای و کاملاً رایگان (روی پلن فری کلودفلر)
نصبش هم فقط با یه دستور سادس :
npx create-talorys@latest
😀
لینک پروژه
اگه به حریم خصوصی و سلف‌هاست اهمیت می‌دی، این پروژه ارزش امتحان کردن داره
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8069" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8068">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-nQcRPXmfHUEasTt9dreG4OkoyioskEgg4LzflJoZHpQKtaD1-zcXknltcc3RxPsYni4qHohLZ7vRg-OuV4b3H4iSn6gcKv3xcPkUQvMuNJ7-CGpS1yUplqNiqfSLeFPP3qw7lZySonr2sbOF_W44bByuKxxgfdPXQORhNwB3qTs1RBNNJ2FYy9P89DkdSXGvhaFyEhXVt6hcnN4M1OVsgMaGjQq0MCJkuRyh5lpmVIVuRCqx4lzsuxaG3uQDMp98FVD6VcluR0x5quyKEZIO6Av-3KQeaMiVrF6xYy1pkT02nNB0ZObpWSRN8q1H7YTdZm5h7ENmD7Sh87Qsgx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی GTA 5 کاملا رایگان - نسخه وب
https://gta.deloskiyt.pl/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/8068" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8067">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GimF5x4u1Gvu9u1oXZqnXugDi7x4ORvYmuxggHaglAkmkDvUPtopIOzTyLsKAb0xyIqE4aPkUYVSgwDmrYnndzAAUlr4m8p0t4hgg5BMPDlM95ij57ommH9UMuE3Wrk3y7Oke8MQPuFyP6k0FoFnvguuGSk3Bi60Xl_D5Y4_gl1hvvtQuLuDNyNy1QBkCGBCXvkYoxepODaK0NgBPp9uzLHNbqx2oaEmcLa42eaj4nth3lcD1iTJtEpcKx-aNT-7gCJ9fW0DG-CSIwjBUR0VOyG6ttMnsUPyr2OlUDOhz3tkxlWkglFckA8uJSKIh_LCecl0743Eu8qq6oMgt1ydtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📰
پشت‌پردهٔ عرضهٔ عجله‌ای دستیار Muse متا
⠀
‏نیویورک‌تایمز می‌گه متا با این‌که از مشکل‌های امنیتی دستیارش خبر داشت، برای عقب نموندن از رقیب‌ها عجله‌ای منتشرش کرد.
⏳
⠀
‏• به گفتهٔ سه منبع آگاه، زاکربرگ تو جلسهٔ ماه اوت و با دیدن رشد استارتاپ ۱۴ نفرهٔ Instinct‏ دستور انتشار رو داده
‏• تو تست‌ها، Muse یه‌بار بدون اجازه رمز کاربر رو عوض کرده و یه‌بار پیامک‌های خصوصیش رو خونده بود
‏• از ۸ سپتامبر منتشر شده؛ بیش از ۶٫۶ میلیون دانلود و روزانه ۱٫۸ میلیون کاربر فعال داره، طبق آمار Sensor Tower‏ گزارش شده
‏سخنگوی متا ادعای عجله به‌خاطر فشار رقابتی رو رد کرده و می‌گه انتشار رو چند ماه برای اطمینان از امنیت عقب انداخته بودن. ولی این ماجرا یه یادآوریه: دستیار هوشمندی که به پیام‌ها و حساب‌هات دسترسی داره، اگه یه لحظه از کنترل خارج بشه می‌تونه دردسر بزرگی درست کنه.
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/8067" target="_blank">📅 10:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8066">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده: ⁮⁮ ⁮⁮
🆔
آیدی عددی برنده: 2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل: @ArchiveTell…</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsLicV636FSLkXL3QJnVGlTJCDqY7iWftY4x9u87sRCFnJyMfATrU_wWYxsYzkwNLP6D85GnJijBmYQO-P-rH1RSo_AXLUd_QJC4kx6rfBY83MeCfkTAWTUfRoTvrN72uoYiXYCXWg4bBqVORqjeBB7JQ30auR6Y4bZw0AQGsKYrvo16So--5Xtc4VDcsk3UayRKGnPmuEZjTbaxH18TQ4ri4joxmbA6YUtvA9LqBraLw32fwr_0WrJx7jrZ4AbQUPtCKrPe572nfdbaCYinJHhQRD6liGdx3Foul1kflAyHk1GyYWnYFmbfHH2BYKQ3wiIsquVYqsR_gjT82q8wUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-GnMwLvd5_4H54RSJq1t6dP_EInhaLc2I7d81qTUo24hMkjkfmzwFhHubcTeazyVHOvec7bC0qISuQscaGOwXXQ9zponIkokGYWZhYneCHnchNwocZ5gvtBXYsRBLS22bq_dNpDaw-_R-5t6d6JNSWiX1JPY7E9eWOpbmo6q87rqHj3Mh_cRRYAT9sbXB7i_BEmB82__XtYRJi09iFuU7o-vLbUDg3NPUo2L-LEL2f1yiSxGjbDzmnKt61KFlEQK0cnYHf5yZlP11VlHnIzd-BZaWFMOla-17G_xOwRZEoryOCC8NE7k7YrNlP2403Qw6yW56ejaf41MvJLPWn9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNzHxbMUHL63ZqzCBzSMSUIuVZiRb3SMMaGFHxKjJaTb8oiZDCLAPhfU8qGxHFF4cBeddTP-kNB2Rn73w6PJwc3HYpyhdb73qHPKIeEu7Qv_7VTVFo7jjf3XeiAt0jP7Xgfx0UXzPDjYofaTP74z9WWClhL2mvdmY-T67KUfFMUMMgzCfkLZIyA4WbV6BMm3NzxWwbEcoR9su1s1fL_aqp-WzgRdlC5qNGTzUqcRuqY2GVhNwahQm1K9itrBM8zaRLr8Enb95hyOddZcC9O2l9mcovtWN9zKm7MMREkAyIcpq5MEdpd38eoe4hh5zjSuPLnf5gTqtSGRntg4ZDVUNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
آخرین بنچمارک منتشر شده از جمنای که تونست رقبای خودش رو پشت سر بزاره
- این بنچمارک توسط خود گوگل منتشر شده و معلوم نیست چقدر راست یا دروغ هستش ولی اگر راست باشه واقعا آتیش به پا میشه رسما ( چند وقت پیش هم openai خیلی روی مدل هاش مانور میداد آخرشم چند برابر از مدل های انتروپیک ضعیف تر واقع شدند )
🤝
- توی آنتی گراویتی هم مدل های 3.7 و قدیمی تر Leaving soonخوردن و امکانش هست هرلحظه جمنای جدید منتشر بشه
🪎
- طبق آخرین اخبار جمنای 4 آرگون فقط برای پلن اولترا هستش امیدواریم نظر گوگل عوض شه
💰
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8058">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔥
مایکروسافت مدل Decision-1 را معرفی کرد — یک مدل هوش مصنوعی نوآورانه برای تصمیم‌گیری که Jev را پشت سر گذاشت!
پایه‌ی توسعه‌ی این مدل Qwen3.5-9B بود و شاخص‌های آن واقعاً شگفت‌انگیز است:
🎭
دقت به ۸۳.۵٪ در ۳۶ بنچمارک رسید که از نتایج GPT-6 Luna و تعدادی از مدل‌های دیگر پیشی گرفته است؛
🎭
سرعت عمل در وظایف تصمیم‌گیری ۳۵ برابر بیشتر از GPT-6 Sol است؛
🎭
هزینه بسیار پایین است: تنها ۰.۰۴۲ دلار برای هر میلیون توکن ورودی و توکن‌های خروجی رایگان هستند.
شرکت مایکروسافت از قبل این مدل را در فرآیندهای داخلی خود پیاده‌سازی کرده است. به عنوان مثال، بخش Xbox بیش از ۱۰ هزار بازخورد از گیمرها را تحلیل کرد: Decision-1 این حجم از کار را ۱۴ برابر سریع‌تر و ۲۰۰ برابر ارزان‌تر از GPT-6 Sol انجام داد.
این ابزار از طریق
مایکروسافت فاندری
در دسترس است و انتظار می‌رود به‌زودی در OpenRouter نیز ظاهر شود.
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QFQlqDb26ZNQ3EJEfF_FCR7x_9p_04GIbcirzDes8IUYbVybe89WTvDMq2ZjLZH-HQlSTcxwfId_MsbAELyIC9BXG0DZpT6iWwCsJY5uieXZy1_u2JWLhMhjn0m5bGoJ-5qh25MGjjMkw0hWf-4Xss2_LtYPfS8t28lC1ef30666OLq7OiypFejEPZkP6gRr5bbrnORMsHYgdSVy5VqVVwSc1Vt2gPSEFLVwEeuvw-5FOXi3T9TJMNWiKqABKu9ZK1AVPq6TcZJsFDC3T-wWeri1nUOcVnNezkxgY04KKHJdMhy7Jz2k974o1omuiRmhjURw8o_VfWn00FcUxzccmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
استرایپ OpenRouter را ۷.۵ میلیارد دلار خرید!
‏⠀
‏استرایپ بزرگ‌ترین خرید تاریخش را انجام داد و دروازه‌ی محبوب مدل‌های هوش مصنوعی را تصاحب کرد.
🔥
‏⠀
‏به گزارش رسانه‌ها، این توافق در اوت ۲۰۲۶ اعلام شد؛ در حالی که OpenRouter فقط چند ماه قبل حدود ۱.۳ میلیارد دلار ارزش‌گذاری شده بود. طبق همین گزارش‌ها، بنیان‌گذارها حدود ۱.۵ میلیارد دلار می‌برن و بقیه به سرمایه‌گذارها می‌رسه.
‏این پلتفرم صدها مدل هوش مصنوعی و ده‌ها ارائه‌دهنده‌ی محاسبات را پشت یک API واحد جمع کرده و استرایپ گفته محصول و نقشه‌ی راهش بدون تغییر می‌مونه.
واقعاً چرا یه شرکت پرداختی باید بزرگ‌ترین خرید تاریخش رو توی زیرساخت هوش مصنوعی انجام بده؟
🫪
‏⠀
‏
📌
گزارش تک‌کرانچ
‏
🌐
تحلیل معامله
‏⠀
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کد رفرالا میوزتون رو بندازین کامنت با هم دود کنیم
یک میلیون توکن هردو طرفتون میگیرین
https://muse.ai/join
5UYP1O
50KIY3
EAWL0N
4RUYCJ
5GD9TV
8809GX
9XQLZN</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ug-xAZFWUOA4Vh1sOFV3GwTbKPKXoZZL_tS1QWig-atBINOs9oIigQBYzTEW8QMFcPSwvvePP0X4BLus3tboDOPjP_U-5MQoiEDNZCIR8bwiIZmdDg6WSkr64zAFpFqqYFGlm52GAK2TAmp5ETIYp-piPMOvaBpRUfQPJnyNWtSrq8J_E433th4ylgxS1fsM1gfjZg8SfOSf0Lk9Wd2zNcmER_qbonoZfuSxSW9S-iJIr-rDVZzT8_rFRbJYr5kvDr9qposyhuv3UYNW_ImwoRt0Z2nFVLDWsDe2VSEJMuP3hF9OKyoW_lDsjpAjNDgy_wNjt-YRuRTld3EaQIKkmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
ایمیل موقت رایگان با دامنهٔ شبه‌دانشجویی
‏
🔥
بدون ثبت‌نام و بدون کارت دانشجویی، یک ایمیل موقت روی دامنه‌ای شبیه دامنهٔ دانشگاهی می‌سازی.
‏• بدون ثبت‌نام؛ ایمیل‌ها مستقیم روی سایت خوانده می‌شوند
‏• صندوق مهمان ۴۸ ساعت زنده می‌ماند
‏• خود سرویس می‌گوید صندوق‌های عادی‌اش بیش از ۲ ماه فعال می‌مانند
⚠️
این ایمیل دانشگاهی واقعی نیست و وضعیت دانشجویی را تأیید نمی‌کند؛ پس روی تخفیف‌های دانشجویی حساب نکن. خود سایت Boomlify سرویس ایمیل موقت رایگان با آدرس‌های نامحدود است و ثبت‌نام لازم ندارد.
🖱️
وب‌سایت Boomlify
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AWk6CJFssd99Ea_clFnr6XtdQ7x5OGK8b-h9pyJ51E2JGLB_YQKzc2mo68LfAHonjSt--FsS3rGt0D2GT3h__-3CfgBgcvyhQEy9b_JUmFBYc7yJUqVhxeYcCEw_Du6KptM8Cyk6JNSkB1unmTVmYKIKKTZPjFGRjbbxE8nINvcZjs2bjSU1QLvtPMYWi0uec7-vRRZNVXiU07BbW5C34QpCJ_qsdwaqrXyfQ_02VXDgZesom2Ra2cHS3DscjWXcyRP0lxtKmdL2xSeXKcuUenWStHSdrqCuVgcCbLZRgDm0L-4-5Ha44DSu3zdmSzfxm6YU_LScRzY8wewfuM8_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📰
آماده‌سازی مدیران هوش مصنوعی برای سناریوی فاجعه
‏به گفتهٔ Axios، مدیران ارشد OpenAI و Anthropic در جلسات خصوصی سناریوهای یک حادثهٔ بزرگ هوش مصنوعی را شبیه‌سازی می‌کنند.⠀
‏مدیران ارشد این شرکت‌ها از جمله داریو آمودی و سم آلتمن روی سناریوهایی مثل حملهٔ سایبری به بانک‌ها، اینترنت و زیرساخت‌های حیاتی کار می‌کنند. نگرانی اصلی‌شون موج خشم عمومی و فشار سیاسیه که بعد از اولین حادثهٔ جدی هوش مصنوعی سراغ‌شون میاد.
‏سخنگوی OpenAI گفته این مانورها «ابزار آمادگی برای نتایج محتمل» هستن، نه پیش‌بینی قطعی یک فاجعه.
⠀
‏
📌
گزارش کامل Axios
‏
🌐
خلاصهٔ فلش خبری
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=EMqrzzkCNvwqEgIhzP_qeRur_2ujpfM3_jV0RM_1P-pNxL9CgSLLhSuy-_fvKFPTb-qWqr7ERSpS5wimSMjRF_3WyJGz7kpPauq59p69YUokz4yaoS1ATRTrI1QBsYpH4h64xEWkpeqiNEW0hRh5-AUBaOigRbVcz2GdUXvu88xAMrMxkf35NyP70Mj5jNQiYxvnFUuvuZdQ5Ounh6rtf28wk0AGSPoiBibnbl7GbLWxt2e5o-vlBKD7G3196CAiEdUFthurWj-XqmTFjDKJne7fc6LhlqVarNZnzdAg3OWuuUBIqBxK_nIIMeT1oicNW35kP31ArBTQJqfmYTtjOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=EMqrzzkCNvwqEgIhzP_qeRur_2ujpfM3_jV0RM_1P-pNxL9CgSLLhSuy-_fvKFPTb-qWqr7ERSpS5wimSMjRF_3WyJGz7kpPauq59p69YUokz4yaoS1ATRTrI1QBsYpH4h64xEWkpeqiNEW0hRh5-AUBaOigRbVcz2GdUXvu88xAMrMxkf35NyP70Mj5jNQiYxvnFUuvuZdQ5Ounh6rtf28wk0AGSPoiBibnbl7GbLWxt2e5o-vlBKD7G3196CAiEdUFthurWj-XqmTFjDKJne7fc6LhlqVarNZnzdAg3OWuuUBIqBxK_nIIMeT1oicNW35kP31ArBTQJqfmYTtjOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
✨
ویجت‌های وب داخل پیام‌های تلگرام
⠀
‏طبق گزارش‌هایی که از نسخه بتای تلگرام منتشر شده، یه قابلیت به اسم HTMLBubbles پیدا شده؛ پیام معمولی می‌تونه به یه مینی‌سایت تعاملی تبدیل بشه.
‏پخش‌کننده موزیک، محیط اجرای کد و کارت محصول، ‏کارت پرواز تعاملی، نمودار زنده، دکمه و فرم ‏همه‌اش با HTML و CSS و جاوااسکریپت داخل خود پیام رندر می‌شه و دیگه نیازی به باز کردن پنجره جداگانه Mini App نیست.
💡
هنوز رسماً معرفی نشده و معلوم نیست کی به نسخه اصلی برسه.
⏳
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9vEhjZKCO2dOBPqv4BH9KHHNZv-I7sOUYNs34LtxDoQpLeno6OM96-tLatfWZkegOrt7m_-FxHClMCJQtW18HS2CjD8FuVorsFe6MIXMewOAzP7kwc5RV2XO77ioccLVB-P6omAXhkILc0Ym67spc3S6GF7ifRNiqP1-RaMSwp1aRWFAcnPezKSVeiigumb3fuEHhAa-6y9sNlSoLe-ARfeKa0IrFzZ0z-KZhQ_KDrgfXB4kfEkpcHq6R3boosj0ryI3fnI_v4pj309w2Sw6Hes9axdp7IKdgrG_BdmvFrWMZ7P_305OVDfdBgDHj5X-aNc5npLfO-20J_V2rN_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎹
آهنگ‌ساز رایگان و متن‌باز Tonefold برای همه
⠀
‏بهش بگو چه آهنگی می‌خواهی، آکورد و ملودی و درام را به‌صورت میدی قابل ویرایش تحویل می‌دهد.
⠀
‏
🎼
آکورد، ملودی، بیس و درام در پیانو رول؛ نت‌به‌نت قابل ویرایش
‏
💾
خروجی MIDI و WAV و استم‌های جدا؛ افزونه‌ی VST3 و CLAP برای DAW
‏
🤖
موتور آهنگ‌سازی با Claude Agent SDK کار می‌کند؛ می‌توانی از مدل محلی Ollama هم استفاده کنی
‏خود اپ با Rust نوشته شده و برای مک و ویندوز عرضه می‌شود. قبل از هر تغییری ازت تأیید می‌گیرد؛ یعنی چیزی بدون اجازه‌ات نوشته نمی‌شود.
‏نکته‌ی حریم خصوصی: برای آهنگ‌سازی از لاگین Claude خودت استفاده می‌کند، پس متن و ایده‌ات به سرویس مدل می‌رسد.
شاهکار هاتون رو حتما برامون بفرستید ...
❤️
🤝
‏
📌
سایت رسمی Tonefold
‏
🌐
صفحه‌ی Tonefold در Product Hunt
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=DU4dWsve-baO193t86DvqmBfvEQZz_qdjjDp0DXbjL80HHR5DPcVte3FtjqHubnPvPSHaDqlt3hdInzlhr_gYuYhf163zWJkmT4B633BhXKPwZ3yhMJFmxSGvB3Ndli9BMjXiEKE_sjdoDWzg06HDtGpCjrOkrq0W3DM6jyzBhKoAsW2jjPIOu48DmMbw4ZjLL7vDd4175-4861y8UOGnb4FLTL82nclpkQnsbDq1Y5QzkGvfqIDK9UYGnoaueBEtqpbI-97cLOsNWPUQ2L3pETz1GR-081b8vLvkaOPPEBf0tw4JMtifAT0e3d0MvH8LtmWnSdOYQSe1pDU7wfm1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=DU4dWsve-baO193t86DvqmBfvEQZz_qdjjDp0DXbjL80HHR5DPcVte3FtjqHubnPvPSHaDqlt3hdInzlhr_gYuYhf163zWJkmT4B633BhXKPwZ3yhMJFmxSGvB3Ndli9BMjXiEKE_sjdoDWzg06HDtGpCjrOkrq0W3DM6jyzBhKoAsW2jjPIOu48DmMbw4ZjLL7vDd4175-4861y8UOGnb4FLTL82nclpkQnsbDq1Y5QzkGvfqIDK9UYGnoaueBEtqpbI-97cLOsNWPUQ2L3pETz1GR-081b8vLvkaOPPEBf0tw4JMtifAT0e3d0MvH8LtmWnSdOYQSe1pDU7wfm1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪐
سیارهٔ تازه‌ای که با کمک کلاد پیدا شد
⠀
‏یک برنامه‌نویس با کمک کلاد کد و کدکس، سیگنال یک سیارهٔ احتمالی را در داده‌های تلسکوپ ناسا پیدا کرد.
⠀
‏شعاع حدود ۱.۴ برابر زمین و سالی کمی بیشتر از سه روز،
‏دو هفته کار بی‌وقفه و بیش از هزار اسکریپت تحلیل داده،
‏و هنوز تأیید نشده؛ قرار است تلسکوپ تس دنبالش را بگیرد.
⠀
‏اولش خیلی‌ها فکر کردند توهم هوش مصنوعی است، ولی چند پژوهشگر سیاره‌های فراخورشیدی هم گفته‌اند می‌تواند واقعی باشد و داده‌ها برای بررسی بیشتر رسیده دست ناسا.
⠀
‏
📌
پست اصلی نویسنده در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvpcs9oxWrt0xF685Be3dYvCZfG6yot3unC-yVOyFqU_VNhbsv8xBKVQB9zRPC9Tl6rvvEjH-reW1jqETTzyAd89M5XWzEDa1m110Qyc79u_dytUjClJk1QEseiweIpA9SFuNsBfrBtdhs6Sm-g5932ZNGNcTpUf9FOy1ZyU-IZST6MZSl6URiZfNnRF-5ZC-p-w4iLkmXrMTt65KaAmJZnCtN22OjMcHerQtPGUjhXq4isthZ-CfNg4KNRqneQxVBE7OS5bjkW2zGbWRNVQRLu-Epnf4Yrdw5x_jzsr1xsZJKmny-Usk5ti-j8jpHHwaGg3R4SBx18-AimELPN7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LReQsw0P6PhLKidt7YoICMT_zhbbLeX6utsSD423RK4OxZVQtFg-qWOA_ScJpGI9UZHeKkgyA7gYInMkIXPPawfbKb9tccOi-gIlrvSQKhyaHCOEqbFBPY3ZFo0jr_S_KHYBjOUcyihmI3aF4IQYaKJqb-nNiiDaNY5oBwpGNUtZoH1k1Tlir07D6UT1u1m0g6rQNNfaWQmCwZaaUvg90-4d7UsEGTXUIJC5vMulAfV9wixdXpA5_az5rluuT4EwoJWpPva9eu2bukSW6dQGukDdk5XCsZFLmbRfqYtuGZYtINCXp6_J0vIFp1ccjupNxBuDkiEPJo3ZqnmJpqysPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptDSGqKFb2D6BzXLHjzx0V2K7PzGWZBZ7ux4YUmvo0nhC1q2n9zuPb33X-_qlnRaqP-vQ7I71mKKlGRFXR-_fT5fmii8rPkZ9qslFK9SSufYw4vORMb9hIGF6atN0j77TaZxS1qeijSxDCiWr3Kq_mqwqK4SC48v3BjaMjgWLHg-4YH-eETNkIuYesQk_doZ4ML87sFPn3cnnqNGquuG0xYfN_hf_E3F9dzMB-zmODR8Ne_DKAAP5Tus36mnZPwrK7rb2vGbM_8kr6c65GVk0TPSpQQ3dAA2b4Ix5o6EwwKuHs_GB8UoB2KQqdgeKSevmbdFmGzSw3nwiOrDSj7qMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
متد حرفه‌ای تبدیل PDFهای طولانی به Word با Antigravity
اگه تا حالا سعی کردید یه جزوه یا کتاب رو با SI به ورد تبدیل کنید، حتماً دیدید که بعد از چند صفحه کم میارن، فرمول‌ها خراب می‌شه یا پرانتزهای فارسی به هم می‌ریزه.
ما یه ابزار
متن‌باز
و کاملاً خودکار توسعه دادیم که این مشکل رو ریشه‌ای حل کرده:
✅
فایل‌های طولانی رو بدون خطای حافظه پردازش می‌کنه.
✅
فرمول‌های ریاضی (LaTeX)، جداول و متون فارسی رو کاملاً سالم و دقیق درمیاره.
✅
خروجی نهایی، یه فایل Word مرتب با فونت‌های استاندارد دانشگاهی (مثل B Nazanin) بهتون تحویل می‌ده.
🚀
نحوه استفاده:
فقط کافیه فایل PDF رو بهش بدید تا صفر تا صد کار رو خودش انجام بده. (پرامپت‌های آماده برای مدل‌های دیگه هم داخلش هست).
🔗
لینک سورس کد، ابزارها و راهنمای کامل در گیت‌هاب:
🥹
https://github.com/faithsaly5-stack/Antigravity-PDF-to-Docx
⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jy_dF7v0m9j4q-0VR9CKbQuaL-ix-BUiZYD8TSvicejxmA5t5dw7R_lH4x_CRV0DHBIWOEJghjO-cOiT4le_LQ4Q3RSUmAkV3yKJvCxXJHG6SZAqEGXoP_XGEySOLWtMeFGUvf0IKBcKAIydjOCr13btwqmIsQRgXhD-1VaXYJCXEkYE9aLAXAyQ9gSI7P0FhYsXbD-_BKtZx6xdDrxLEVsTum6F6-z1DrWhUav8zE5BHWSG2qgX8E3jdz0g6GL_ssaUByTOWDpAD1cLPxF__zA1zvS2Iu_OCaJ4WKWnDHzVcC_uWANYOTFJMbmfTnvlcNuHaa8zH4L4YEE1TBXlpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TocFXkF-s0i1xULVgctJfjebdPleNeyHbSUB7dL-TtCgBo_j18GllXvFyPO9Ak7EbFGIfDCLO8q9W65JFfQUqesdi0jBB6xoeUaKjMdDgStSu0AsnKbLGB8nveS200anhbZhE5mNC-KCC9mlr-JpPXd95REJSsjtKdDz8lSUUoP3FrKKcqxQCPDrBEpAZeGCTOKa00d-NsNt6F50pc-SHEmZWhRtJffZzbCRpIZzUEWZ6MEQDz4S_gn4nyn7380wiqtu0vQOdcQssf8Ptq5pHgc9XlNGwnxwjWE5po-i2W61uZRVPggHxaEm_B6mo7bg4TbIJxpTjliktgzUwK5bEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#حمایتی
‏
🔐
برنامهٔ غیررسمی FoxyVPN برای ویندوز
‏به گفتهٔ سازنده، فیلترشکن فایرفاکس رو بدون اشتراک روی ویندوز بهت می‌ده.
‏
⚠️
غیررسمیه و ربطی به Mozilla نداره.
‏
📥
نسخهٔ 1.0.0+1 از بخش Releases قابل دانلوده.
‏
🔐
کل ترافیکت از این برنامه رد می‌شه؛ اول کدش رو چک کن.
دولوپر از بچه های خوب چنل
🚀
‏
📌
مخزن پروژه در گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=t2XbNoLCQeN-YIpsPuRyjydBjkGnVfQ4m_-3dR40jdGIZZEWEXUVtwd2KdamP6gE2DVktI3L55yLnNsUUc08R8TUzvXJ1LXBk9cXWHQRUlIOpelwvIbJJHbAXjKktICf3cGJ9cYTnoec3PKoWceUcB8xIYVC4XSZ5FVUunDayBiUVBaSQYdv1_skGvZJ0I-zLeuUUMW5QtawL8sznrDxxkjxVYnEPgUXIWMM5BG5pj2QHzIcmWnnwVf6N4f2f98ANX2OtPWs1qjm8Ve_SsbGUBMW-6Frl82a_fYBuKv2Is6U7P2iV8NN-_x4nhkvivGhOLGYMcmGkGSziICewx_duA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=t2XbNoLCQeN-YIpsPuRyjydBjkGnVfQ4m_-3dR40jdGIZZEWEXUVtwd2KdamP6gE2DVktI3L55yLnNsUUc08R8TUzvXJ1LXBk9cXWHQRUlIOpelwvIbJJHbAXjKktICf3cGJ9cYTnoec3PKoWceUcB8xIYVC4XSZ5FVUunDayBiUVBaSQYdv1_skGvZJ0I-zLeuUUMW5QtawL8sznrDxxkjxVYnEPgUXIWMM5BG5pj2QHzIcmWnnwVf6N4f2f98ANX2OtPWs1qjm8Ve_SsbGUBMW-6Frl82a_fYBuKv2Is6U7P2iV8NN-_x4nhkvivGhOLGYMcmGkGSziICewx_duA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftt8fxSKAYOihSFlvTNSjzA88SaSCC7rj6lLAvKcBF2pFhVwaNJHU30nD9HvpQehGum3EQx_fvLR7ao6OQ95mnVJB5ySBIEPtvFzLGSOUho_JKN7AOefM82lr-wZiYLUVy8ltqNw18PMKdk5l2d_tI2Ff9iXTOIqRKwNSDHPZJR2Tpw-y30iA-UfQbp8XXo0pTkD7S8tss7ZnuXmPE83Izb0HzfPgVSuTKqG4WP45PsBNVEeBe__KZO9Bf3GTQsRIyLTAC7UDEe0YZKYViAIQSgUcn4VVJsTPRgE0hpzyJBoYYvIDkmatSTPNBSrMTVOBpKKfNkqEWM97hYjRR2sPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪙
ای پی ای Tooken Club برای مدل‌های معروف هوش مصنوعی
نحوه ثبت نام توش خیلی راحته فقط کافیه ایمیلتون رو بزنید و از کپچا عبور کنید ( یا باید تصاویر مشابه انتخاب کنید یا یه شی ای که خلاف جهت بقیه حرکت میکنه رو تشخیص بدید )
‏
🤖
کلی مدل داره که میتونین استفاده کنین چند تاشو مینویسم :
claude-fable-5-1
claude-opus-5-5
gpt-6.1-sol
gpt-6-astra
glm-5.3-flash
grok-4.7
🎁
10 میلیون هم توکن میده برای استفاده اولیه که بنظر کافی هست ولی برخی مدل ها ضریب دار هستند که میتونین از بخش  instructions بررسی کنید.
Base URL :
OpenAI:
https://tooken.club/v1
Anthropic:
https://tooken.club
‏
📌
سایت اصلی سرویس
‏
🌐
کاتالوگ مدل‌ها
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gypeX7LKiR784WQWyZxfrJCOseN3VdrBt-6h3H-p6pwaKBVRf-FhTn-wINGM4PPpXTLJHGg6_-AZOniYF7KS1c5_LVXA7JKgFjktXaanYqPPnor1ozJVSuJVbEI9BRZyPy8DEkSiW5h21G0hD_YNoIjdwmPnHfEFtKgqFnyfT7YnHf3jHCW83VbYmblI84ZcdOIa0Yrhdpv28GfZTBI_16zPLaTOIuop4oxhtwt8W7cYmjmUTvHeDK7CSz85fZsxhAptckaO_ItogagJRol1gLzIYg_biRv-CAfOBxNTt-PI1qt0z7uPNJyEOBaV5bqSEBhb-i5OqRGLRstHG1X1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0MU_CXvG12bU_AHxsRtsx2EYF_-1E08DNlQFZEBd8VwCwORjGYwVN3pdQ1qscxaDqcDGWRMi4u_t20HAMMKBso8zLPSinnyO6ds53scpj5g-xQjGPnmCGjMAuDVMEAGVGzVrZSPLTE64s1ZFL_XV5NXCAUyTvmrZ53zMzXZPICa9So1z8gfwMIhNeQO6etwmiKVaarBhcfzwA6V3gJ72ynZArQ-hFSBUYRR6o_z9IoUXkVsuie4eeCOWfzoToboMWj7IxiBgrIVrDZmq2U7mavADZevmTGEXHxsWx9V748J-w4YWAgv9OnDDpENO_4vPeXX9W1ZvGjbMNb_j3umkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها
⠀
‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده.
⠀
‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه
‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه
‏
⏳
اعتبار ۶ ماه بعد از تاریخ اعطا منقضی می‌شه
‏
🏷
روی اشتراک‌ها اعمال نمی‌شه
⠀
‏این اعتبار فقط روی API خود Anthropic کار می‌کنه
⠀
‏
📌
فرم دریافت اعتبار
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=YQMDkeH0QpJiU4ZEsUvmnxl818WG2NnvC2-5I-NU6w4WYvKTsU_9EBY1txR8opMvkXH46HAaJRKgVcJ83cZCgbaF4yJkR_ONkY1tRKtiJwrTV9NpDQdCX0HE6_EOeFwMM7BVs4qVcdKTMESKa2GZy-dZatCkGbLd6nZwah74Mc9FVyVuOd7AHzPa62ZJuwaJlGVQzPS70j8I--05wEoyliczN26IAct6lO87UbyX3gIp5_rDhPIvuzGfo-qrtoUaguqxR9w6gQixooGSjdUCZ98kyF0pk8mr_kJeeZ8vzjKPF7SE7VlljLAGHp4_4zte5iCCROnAiQi00-hxgjc3LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=YQMDkeH0QpJiU4ZEsUvmnxl818WG2NnvC2-5I-NU6w4WYvKTsU_9EBY1txR8opMvkXH46HAaJRKgVcJ83cZCgbaF4yJkR_ONkY1tRKtiJwrTV9NpDQdCX0HE6_EOeFwMM7BVs4qVcdKTMESKa2GZy-dZatCkGbLd6nZwah74Mc9FVyVuOd7AHzPa62ZJuwaJlGVQzPS70j8I--05wEoyliczN26IAct6lO87UbyX3gIp5_rDhPIvuzGfo-qrtoUaguqxR9w6gQixooGSjdUCZ98kyF0pk8mr_kJeeZ8vzjKPF7SE7VlljLAGHp4_4zte5iCCROnAiQi00-hxgjc3LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ10OWLV9-iRqUIOxxWrlPFs9gtQBb4McEIyapmBOXfo95Euq345OyvSrmuM038br3GTtiPAROD7IDg5r-c815ames20LLPUv8SoJXNFON16iqnQpxSWr6bOf2DI4fssCoGZXeOBj7whkU2Y73b7xV9oM1DBRSIBDWve4YksqVtUvpH9ZtXFA-q3iv_8rfXX7QORl2DABYFlMfjLiUIdnXBDJRkf9fe82TBpGgJjO5APnELOhTFqGseEW3tysHtwGZCU_ynTzSz1ODXzPIQiaU78OYgfARm0IluouVXBhHN4OYitrkUd4tVSvWzcMngsCiATbbKaZZiovhl233iiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نه آقا ببین ai که حس نداره، نمیتونه عین انسان حرف بزنه بخونه
❗️
🤣
همزمان ai
⭐️
مدل جدید تولید صدای Elevenlabs V4
⠀⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/erd8ghkJHakBQnMgxQ83kRGey5xdfqOtDRRuAg312f-ztHARfxjhGsREvUkFi7VcXaYD525Sxn3YBZJ5S7kqimB73N6CpHszdb7LaPGrBDTg-7dNpa5i5N9kt7ZIJr440mIzLE4HiyS0loFJ4GKNQzfbRl3cjvSgUVa0ss2ehZSapkRgVDCx_4lhcmwJyX10S_s3qxwTvw6_l53w2kq7s609-apJUkjaxnJIiOLQnRatALpXCa1G6siD_G80yL7gXYiMAklkPCRb192iQzCaCuQeiT1MRYdImSFZ2wMQtw_ql3XjXx-OrMSHELeQ0EpxVleRLI6euBXPQgDLT24a-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJTMRL5_F167q4J5bf-eaOhwV0JaDfCZ6QpFSQ7FH1FkZ_vMX0wlhQKRjJi-ASgYlKUIYjcqDPWNunTCIGQ6yJTifhL7UvliPe4BzD99qTWWZTzhTGT-XaVuhoJbU6iagkKcQ5qRamqYb-88BcdJPud1Q3Vpt9gV09-TFAD_0faEnx049OmsCbRRetkR2W126DupnEcVdRV_tnq3oW52naC2f-kjWls0u8BV0MynAWi_wM3iA2Bze87I4cuyuncf0TxLU0nbsGNZOECej1yFqrGhSX-M7PXFC1cD0Rcszny_vk93vfRMSEGlJ7R1dlOUmDVeefLtx07j6X6fyCEbDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpHg2VFfrcWkkwdpsuXaU1NBTZ0zuii1tUfgE0PJOQFpq70Ws4Bj-lmssrd5sg5ZSAERbs1AspC4XMBjFOdF696J7_e3Zd26JQ_Vvx60QbXaJXWP8Q4eiSf-JQCHLka9a_7CydiRKDPH9gtcup0Dz1U6E_u7oc2sTk79Zgc8vuMPiBc6dPOdsFkkyBRNQIkEQgROVL_XubGcv4oNo_5vnrZkgi9oLQQQC0ET1iX3E5AMDUJWw8sRkIChPvLbdZj9x7UjsiOF0akW2y1xLWNCoOtrr6wlLGFaxLfKS3wmpBfxSkoZSK6H8xp2yEveRPEnXQzGh-umOAJX2-XD_W-wbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sS19TJvSqrDrDvL4Bz2VIMd6rOAq2iLNI73C56xkcT7ETXm-wK-AYx8l4zhcFLDPufYC_qs-8xYLhrjyGx-TlDa-4D2lfikMBTlTYhyZZAZL82pJHw_VZCgap9slkbWnTAP5jTmGraZ3rSyNCzjZsvF1dKGyIsoR9o6KUsH_JBxjrs8Dtqw4TgCT3NalTADMiGmtptWuIo2XsDEr2echrpYuScWp95JUYr_SAqL8x0FHU-0rJc3XADdymTx2iPFn4_nwUkD4n4r70hwjRGwq2qYe-5MIw9bAGy0ExozPXyCiwI1-rGwNIhLF_lXH7rVjcUDxANlEdYuuo0ti1VCG3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtJWhZtyTda-oGzX6uHbZTXuujotXA7i8Zv5xaoCyPf6brXRSFqv5d5IzlfbOfeDjpNFFQK2QRO-ex7R46XYNZzOJpolEmyxX2_s5WlQY-Ph96gyUp-KIS_31S0RciDnRN8-qsf-eJYUgQcbbeKrP5vLr3PptAjtpBzEJ755UTQfgAr0wWKiJhFhSKPXlhIvtHlxCXGnXlfXXVEem5goxsW457bP-7l4TcpMNoAW-3bBvQm80IE1i1yUc6fX11lkBlmyvvKzxPgn2vVuZTY2sad6Vzi6ZZ_-QE9y5TpDfDWJmTybzSx43kOlUL4csdOfClLS9OjlDXceaFoYcEhWug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5MAlxDWAbAmYggHAY7BTsP3VwSAuU4pKLGIPoTSCQcbE0GEysDytjukLkkDBBx3l5rfrOLKk4dCzcLvGlt5Uu6xIixWGNCocaNG0FvxnOozJnnlimaVWowyqaKk0uz05GImDpNlQTs6NHfyUaeMPVrVuLlHIZ9khQjN-QXuGiqd0b1mbcGKz_KjNiL2aGhMeazYGt3m9RaZirhgUY3REDCdVlzUTx95NsusikWHmsPvcI_ihi_3_8V3oDlsGn9OeifmhwgNjZq5nIk-tIS9uFaLZ-Wyq919GzEP8LHU9PQOaDgw60MxQKadfuYaKd8aS0vKzDx_1qfVWB7EAIi40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fauxo9wZ8FdbwUtY11J2j2HSZj8KPRLQS8w0VU7LgvV5SwsXFUzsfeZHZTTErlWNdQJ4eYylVEHQaHnBx0fSsGSwMdMWKoy53rP4b6_PIv6ezEZnUpoLjllCDjEs71GySaYYyiT-j9ENGEJdTPGi0yHH6EHHUj4BtXQu8xl6WppmAjW-YMw20Ndz8kC9HdoPkjRfhsBiuat0IZcHMR2Ox04oZhgQmXRPLHKvRAF4TDV6wksktq8B9ewAoelhVUhUrzx7f1E46rq9F4wD02t8kR3tXbKmBhKh6k5Hx7r7t1T8ROn9tH29uhjT8KYbne3k_31P1BsFqSLyg9RcdhpTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W2w3u0tcP9aoefU0NnEy2Oe7puLU2GTApfoTW4EPl0xhTxKzwhPucRopweC-QEHknR3XaO_Z34TGWpDGfRDNAs5UBbTDWn80MQrL3kf_aXwFjwFwJ1rncEFCDlbW2_vjjue2Z_gEbtj5DxZNiqcrE_uDl3WB7saKNRHHsxJmcUJGM7MraCMmZ7pkT1t3xQPKqw6kousLtDMfuWBODG32nGtelnaZw50H9A5oMc7hA52OODCCbagVyNCxemhwZF83wQLrbplylWi-4cjgfQ6SFFs2StwQBSdxpi3TtseMmUQU6jKlH5Wd3_lvR7bZbXB0PmEPiGM5lFzAbPQlli7Z9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PcYAxUK4a5jBLa_1gco3CAFnQqOhK6wU7BzF_-A0biqySsz2wiKMC6TmhPEi1qrJr7ezZsywbZ7WxnjAYICK95MikZVF1C8Cd9zXBGfOuihGn7hgIgOvtpuqxBeSxK_6qsTAD_TyAiUu_yf3gy8scfFhNebdIdsbcx0FyICrBLEuvNloWZcm-EQoBAALuGPZeZJ5BjMQrGbYtjiYuv6upxuYd1mCk9o3izryxhLnbiAerjWQHjAidnydrCLrc8kcLIMnLRyoiffgniJZM5WLVJ2gwaJt1_yhLwd42hUbnOC7VU0B-31MWx9PNxz3ypr3ORm9NThktwGc1ljroM7yeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxxfjJK2h970U1DhydGD7Pl2pgIrFqndqbag6Qo-dGDX3TRT7jYKiqhPkRkcpKL0bAdrBwxkbWblV1mFyuQTnPhw7jBMuWSEPoNqv2ufQb3O-tn_kBKTNES1rNUjLotqNwTk1Y7BewVNYEj3Sw3KZGhqs8upcrh7HynOfvHq2YZEhzowKrop4FBWZvGYi-GjxrpkBl0yV_1xKqOWGMo2zz6okabDcsnT_yGiaNq_SSJ9Sm4rfbH16RmWp0YY_cKIBaSWdCEqd2dQaTAxPYY_yITHhs62hcoXMz3-27-eURRpxUmQv6brcrW4nX8KuxFNlifDZ6cU-mAVmMPUaNJ3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✨
بنچمارک مدل Nano Banana 2.1 برای ساخت تصویر اومد
‏به گفتهٔ منابع خبری، گوگل نسخهٔ جدید مدل ساخت تصویرش رو بی‌سروصدا منتشر کرده.
💡
به ادعای گوگل، حالت Thinking توی اینفوگرافیک دقیق و حفظ چهرهٔ چند شخصیت از Nano Banana Pro بهتره
‏
⚠️
هنوز ممکنه چپ و راست رو قاطی کنه
‏
🐞
موقع ویرایش گاهی روی ژست تصویر اصلی گیر می‌کنه
‏
🔤
متن ریز یا خیلی طولانی تار درمیاد
‏این مدل روی Gemini 3.6 Flash ساخته شده. به گفتهٔ کاربران، توی اپ Gemini‏، گوگل AI Studio و API در دسترسه و به جستجوی گوگل، Ads‏، Flow و Stitch هم اضافه شده. به گفتهٔ گوگل دانشش تا مارس ۲۰۲۶ـه، ولی منبع می‌گه عملاً از ۲۰۲۶ چیز زیادی نمی‌دونه. گوگل هنوز پست رسمی براش منتشر نکرده، پس این جزئیات رو با احتیاط بخون.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL5lj8VbyVqI0Y3DelyonT5wnVOukfPwtOAguq1v0Qj5Y-8-8y4GYKaQtQbKYGnyopsKFPVhxtlGY6qAy8e4m5jTw-SUU9CT0kXqgpv8ScF5INY1QfSuaIoyXqQaxPt-kQV4rko-0OTfhiYZPK5s1Qz_E1-8YeKwxLM2t_o-boUfOfPaxLP7UCZcah9pvX5joKgDZ9yEZ5k381UJURiA_IZ2cQXmTJN6d8u6qYxKhKwhIkymsyTzFhWPWPBeR63s8n3YuzI4G5zywa8s9kFLLDR93tLKHZ4cuRpiTqitiZSzWuMytUm4r45f4JbY1hhLNZodjekuxAtH_zb20C2irw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BnKLKj3-vtmS3YCTG2A1MEloZwMiHPJeavPGi7EpMUFJc9NXoiLrTwonOlZ9QUYmMZ-io_9TCLH9OpOUqy4Wt364Nuu34ZS6NXslPpCVJr6_feMuYIyWiClzwHHAhntQGGjbRNcV-HncrFyJi-vZjzY4Xj2VcMGsK67VpiCy48L7aNfvOgsVHF4svZaebqb-OeYqs6-IvlV2wAk-UbRKCKo67iWYVsBcBzIc-LQjPBwuFQHtMtg8QCRmZXpzw_AjVk9U4F2UsnwLWpagQxqHvm-yLG_acz9PrMnIvGStfeQcU8-EsX75gsdzvPvugabQQ7cy_EZoO9zg0yRXH42YwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚖️
وقتی هوش مصنوعی خاطراتت را لو می‌دهد
‏
یه زن تو فلوریدا به Claude می‌گه می‌خواد به دفتر کلانتر حمله کنه؛ فرداش پلیس در خونه‌شه.
⠀
‏کارلی میشل هلر، ۳۰ ساله از فلوریدا، ۲۶ سپتامبر توی چت با Claude نوشته بود می‌خواد به دفتر کلانتر «حمله» کنه؛ فرداش هم نوشته یه اسلحه‌ی جدید خریده. خودش به پلیس گفته از Claude «مثل دفترچه‌ی خاطرات» استفاده می‌کرده.
‏فیلترهای امنیتی Anthropic چت رو پرچم‌دار کردن و بازبین‌های انسانی خودشون به پلیس زنگ زدن؛ زن بدون مقاومت دستگیر و به اتهام «تهدید کتبی خشونت‌آمیز» متهم شد (تو فلوریدا تا ۱۵ سال زندان داره). نکته‌ی مهم: چت‌های پرچم‌دار ممکنه توسط انسان خونده بشن و سیاست Anthropic اجازه‌ی اشتراک اطلاعات با پلیس رو توی شرایط اضطراری می‌ده.
⠀
‏
📌
گزارش Cybernews
‏
🌐
گزارش TechSpot
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzCre9W_mG-uI6jgRbQPyG27qNfrFupOopOOOQ8DiXw-0ijmBuDLxjZ5_IRi1oswz6VIC6KDKgxL7-9w6OgQPW6ofL2gCKMywx-_ePFzQez9URvi3pEnGnDDpMoPe_dGjKT9PIUgt942nPcpqCu7hE4233HTqEcdU8cYcCN9ZYpWuGXc0JJ-S7S5Y_W0Oz9j1CUZJlIIBI3tjUcCBkCBkr5lW0pNNzW9xhzDZ5VP3R0jueZcl0oJ6e8fNi5JkUwWmOPmMbGLdgQkeOQoT_Zj8y3thblkfNku5O7IHJvPecW7JZDon-QFokPTTpFEcJQ-Rwe--yQLYgYwwGjfXDFIzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🕵️
هوش مصنوعی رمزنامه‌ی ۲۱۷ ساله‌ی ناپلئون را شکست
⠀
‏یه نامه‌ی رمزی به ژنرال مارمون که ۲۱۷ سال هیچ‌کس نتونسته بود بخونه‌ش، تو ۶ ساعت باز شد.
⠀
‏این نامه مربوط به مارس ۱۸۰۹ئه؛ دستورهای ناپلئون به ژنرال مارمون، درست قبل از جنگ با اتریش. خط اولش فرانسه‌ی ساده‌ست و بعدش ۲۴ ردیف رمز: ۱۳۰۰ واحد رمز با ۱۵۵ علامت متفاوت. کلیدش هیچ‌وقت پیدا نشد.
کارتر چرچ با GPT-6 Astra اول اسکن صفحه‌ی یه مجله‌ی فرانسوی ۱۹۶۹ رو رونویسی کرد، بعد رمز هوموفونیک رو با آنیلینگ شبیه‌سازی‌شده شکست؛ کل کار حدود ۶ ساعت زمان مدل برد. حتی وقتی متن‌های تاریخی ناپلئونی رو از حافظه‌ی مدل حذف کرد، به همون جواب رسید؛ یعنی رمز واقعاً حل شده، نه حدس.
⠀
‏
📌
گزارش کامل رمزگشایی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=f80c1Dganjj3u5TXojoJHiIpw_7oYGQOQjO_LDDMgTyrOCwbuL40t-Ku6G-0IwFExsT0Z6L0xYJetIKzOpdxX-d2Ac0vfYGzfIZAlJLw9BdhqyWt63p44DbHFGueQt1t3RtqxGcvLWp39WP5f344lWQ29E_AzqNN5PMrqdargswwDXcpuQOg9b39nyN6ZQsNfta5wwkHYOUfUUWYHOqfjuAKpE-1yZdqtQAS79FqUuXKLgHYiZyhDcQI6Dqy7c-BvI6Cxhfj7ILqsZrRbTHN76PR48VW0qNJBZvZK6j765k0X4xNsCE1WU67hEtJC0AN8KwufS4qJNB5pjXUC5s_1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=f80c1Dganjj3u5TXojoJHiIpw_7oYGQOQjO_LDDMgTyrOCwbuL40t-Ku6G-0IwFExsT0Z6L0xYJetIKzOpdxX-d2Ac0vfYGzfIZAlJLw9BdhqyWt63p44DbHFGueQt1t3RtqxGcvLWp39WP5f344lWQ29E_AzqNN5PMrqdargswwDXcpuQOg9b39nyN6ZQsNfta5wwkHYOUfUUWYHOqfjuAKpE-1yZdqtQAS79FqUuXKLgHYiZyhDcQI6Dqy7c-BvI6Cxhfj7ILqsZrRbTHN76PR48VW0qNJBZvZK6j765k0X4xNsCE1WU67hEtJC0AN8KwufS4qJNB5pjXUC5s_1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLjuQGdIZ1u13oP5RE_FRHEdjTytcw9IdmAW4JBB2wKBwXuXsYERgR27C-oz01833YXflTs-fNSrylbybyPe10dSFryHtTRfQRFi-INN3pC8RjWSuLtbzMXPlawQL_4RMWZvUa3UGA-ZPITnJuiYjAGpKK22hw4obu09-NYN52ir3jx-q0EJ3hFzMqzZD0-CDd6cCJZ6SxnYvurFUXWYM3ABTSnU4jBXHyKi0de8FTg4hg6THiv_bC7nOTQJ1_1EryQAUo8gkuFUHY3-UX5rrqG3VaPyP6qhmnAmRh3V2GVeSkxX3kPrgkHDbit5Bc-dMOiBCSeBR9ZN6LgUAEONXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1mmUUWU5fM6zZ566OerCdfGq4NXz4nYPW4TyRn2TtT3vsIdB2uSnlIYYG2GUMtYDH6g5CewYOG1_D2sTGO5L_GNUwWd_7jOytP4uJZ0I8Ki7QVXEDsW9WYwaCxn7Z_9I8OkTeIT4pbDAtTrQFT5CJntF1d14krUpxEwI98p0J2YuNN3eFY8vjwMEez_O23B3L2-ikj0DrfqCje1fVYcl0ghcgixzS7mBuGc_x5NSKEBpHz7jnqZpswRqYDl6gZEvLqJ9dxjfYVV22PnzJmFrKHBj0S551QFoZpCyvTxpEphBXqNuhw5-tfYqRlY-4gYfPbuGQj-IEx_p2DbdWr0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BptuiyUKNDSfPAIrPbmqLmfQnjpbdx4fnCSU53ylcSij_zKrt0TQRZrpo60kTX245fY75RyEvUQgPJGlY79JjB-6xVKR40xC_0q_eG0vMzrQjUjLKEUpz8yIDM44Wg-oy4TMIg-bRMeduQ2qBU4hjHuev8gn8dkcYVj40zMu0f110n0g2AZWaLf5sqxol5FOptmYkV7rAO7uUxLXsaU4_ddk0SM_LZqEQzIlILShqKu9LOMaASVyhcCEF2FbzC69pY_PaKxtZzTVMkVPvPrvYbvvKQHxBDb7o96IqLGKyzj61mMBw265FJlahGt4a0tktcg_xVefkF8c0SdUI2Pnvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BWRKWOZE8MGSfUP4TFgid_iuPfne3ZIofNMzM_ov4Ae_dsW4rkN7EDOUmm3f3-Kh-em56o4-RHGgWEkXbC2Ik2vndURhLyM-Txp9yX082rzZZ2H7GlnVCmbYJehOJ8apHfRac_0VwNomYve32_5CnqR97-TqQTq_SsSnHgGRVo_nFvTtsXcai4angrGs-yYC18y8W8nmRn87G2Ja-oLf1KG1Cwjlh1E6M0QkqWdjkN4Jjij9dj--fgQ7aacm0qnpwEwBQW1d3kKMYZnLT0P-ryyMf7pebYTep1tphd3eARuiz6l2kdfPGJgxlsBaUq-9LsdvGhgVOUte5QwYW6XBKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IIT54qi5_fwCnela9B8P4BkYyclUrnrcUvErhCXt3QsO1GMaHxFBkI0aisK9dsctAIeRoMiFaxc51ENeTg1rZAI0fSa16wBNHUHyVvJ91Z9yeJY0-4fpxgfskNGOa90F02TaVsy8bL-6FpQ8AtK9LZVexNmeyc1hglbM2kYv8JUdU-L6Sc2KJ9Z4tCAX9ThYOLzAsb-MSpJ9I8_Pq-elzt7VREqYp2oZA7Fp7M8GsO121YXM9nj13EjgLuelJc2jGPBJpAD5P4Ae2XBe9sUkR0eODUo0OmvzRthJeXSD_pKZiK6AKCVCseIj6FHjJ3-cwQmw8jGhD3mj1oPi3jpMhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🎁
فهرست اعتبارهای رایگان هوش مصنوعی در یک سایت
‏این سایت پیشنهادهای رایگان، دوره‌های آزمایشی و جایگزین‌های مجانی ابزارهای هوش مصنوعی رو یه‌جا جمع کرده.
‏
🪙
اعتبار رایگان، دورهٔ آزمایشی و تخفیف دانشجویی سرویس‌ها
‏
🆚
جایگزین‌های رایگان و متن‌باز برای ابزارهای پولی
‏
⏳
مقایسهٔ سقف استفادهٔ پلن‌های رایگان
‏
🔍
مثلاً دورهٔ آزمایشی ۳۰ روزهٔ GitLab Duo که مدل‌هایی مثل Opus 5.5 و GPT-6 Astra رو داره
‏خود سایت مدل رایگان نمیده و فقط پیشنهادهای بقیهٔ سرویس‌ها رو فهرست می‌کنه. بیشترشون سقف مصرف، زمان محدود یا شرط ثبت‌نام دارن. به گفتهٔ خود سایت هم این شرایط ممکنه عوض بشه. پس قبل از ثبت‌نام، شرایط رو توی سایت اصلی هر سرویس چک کن.
‏
📌
سایت nopaywall
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMfna8a030Rg69_iZ2o194-DR8u3UF58cW552BjMFVJGqxnnoTZ6zfp7DJ3h6eMjUF7RycqV1FOT_8juFh1i7DGAcC0ISRXXqH_UagSCpEWD2NybUtpOLYD5C5DNY13M6ctFQ8UFDsjaiN1hUe4NUWPQND93oEw2tgiP_LF1KbhBHZg2ghEyQZDESCYVEr_KXIZWRTwMV0P9jNjZ-iGxjAYqXaCh_xg41mgyBtV69KtwtNsOCrNl7K1CD1PkNyfejr2hX8CMWMmFQgfQU7H-t2dUoM1zBdcfo0dAr5huzDQuooxKB8NlgQZ689ck7hN8syBlHzyVbTqWjcER4_OHmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚀
تبدیل هر چیزی به PDF فقط در چند ثانیه!
دیگه برای ساخت فایل‌های PDF نیازی به نصب برنامه‌های سنگین و مختلف نداری!
🤩
ربات همه‌کاره ما اینجاست تا هر محتوایی رو که براش می‌‌فرستی، به یک فایل PDF تر و تمیز تبدیل کنه.
✨
این ربات با چی کار می‌کنه؟
📝
اسناد و متن‌ها: فایل‌های ورد (.docx)، اکسل (.csv)، مارک‌داون (.md)، متن (.txt) و حتی فایل‌های کدنویسی.
⚡️
عکس‌ها: یه عکس تکی بفرست یا یه آلبوم کامل؛ ربات همه رو توی یک PDF مرتب بهت تحویل میده!
🗂
فایل‌های فشرده (ZIP/RAR): آرشیو رو بفرست، ربات خودش بازش می‌کنه و محتویاتش رو توی یک PDF برات ادغام می‌کنه.
🌐
صفحات وب: لینک سایت یا مقاله رو بفرست، نسخه PDF اون صفحه رو تحویل بگیر!
👇
همین الان وارد ربات شو و رایگان تستش کن:
🤖
@Everythingtopdf_bbot
━━━━━━━━━━━━━━━━━━━━━
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KW3dIbMBjeCKwJn1Cw_2EaDcHNzfRbEUxC0dsdvKQQv-Sb7tneNS-P-PsWFoVdbbYVvL_ApnoHWRAuVaDdwWladasidI7w1zA9_DerBWAOeOU5wi677V6HeUOOrExeXdBKk_QjEZMcvTOMAyn0wx9yVedMRqg5Z4Lrgg1YdlTrEfEMimjKtZQOZW8lqOjFINaMyfmAf_b0DHuKAC-R6bcDI6bATDP2D73w57mp38ThDhLS-wXCDP8NMZq75FHGG82Y4KSNASziaG8IfxkEApIHkTKU0efi2L_aEJKD0ydlrzwNFmuwMypzjyxRwO-TFaHp2E98ujmgXLcN8nU7gepw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎨
کلون متن‌باز فتوشاپ با Rust منتشر شد
⠀
‏استارتاپ ArtCraft نسخهٔ متن‌باز فتوشاپ رو با Rust منتشر کرد و ۶ ابزار دیگهٔ جایگزین Adobe رو هم وعده داده.
‏اسمش PhotoCraftـه و روی گیت‌هاب با لایسنس MIT منتشر شده؛ حدود ۱۸۰۰ ستاره گرفته و همین امروز نسخهٔ ۰.۲.۰ اون اومده. با Rust نوشته شده و از شتاب GPU استفاده می‌کنه. البته هنوز نسخهٔ اولیه‌ست و نباید انتظار پایداری کامل داشت.
‏نکتهٔ مهم: چند کانال نوشتن «هر ۷ ابزار منتشر شده»، ولی طبق سایت رسمی ArtCraft بقیه — VectorCraft، FilmCraft، LightCraft، PrintCraft، EffectCraft و DesignCraft — فعلاً فقط «به‌زودی» هستن و نسخه‌ای ندارن. پس فعلاً فقط PhotoCraft واقعیه و بقیه وعده‌ست.
⠀
‏
📌
ریپوی PhotoCraft در گیت‌هاب
‏
🌐
سایت رسمی ArtCraft
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L_YdUFGO3_PJVhY5971pluVuiHeNug4XjY6V7VkgsgEJdKqn4ZN3qhN2Oslrd1f7Ckq3p04NpENuOptapj63aa3weUsPnks_A_mHwHhb-JK_LzutE9G1F9aDy2jLlWOa-tHS6PEN329sqsEnO0TVGEaymIftLnJV-nCluQCiaQFfEJ6trO9SPQ-10SoYq9dhhnDFn86WFXmEAsFUTZcOJy4iDTSQBxua6knmhXF4_jx5sgx_URwCGdLbHAHaVYjz4hl5LZi6u3GQkoYZE65GmxmZ4zZ_ENgmvlwrFpx8W_L2HrJwEmQLNiQjDExNSWL4mZROQNxcdKdJeTX0Cq6t_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚔️
هوش مصنوعی بدون دیدن صفحه وارکرفت بازی کرد
‏⠀
‏مدل GPT-6 Astra بدون دیدن تصویر بازی، در چهل دقیقه منطقهٔ شروع وارکرفت را تمام کرد.
‏⠀
‏به‌جای تصویر، بسته‌های شبکهٔ بازی را می‌خواند
‏خودش ابزار ساخت، مسیر پیدا کرد و استراتژی چید
‏از یک باگ نقشه هم بدون اینکه بداند استفاده کرد
‏⠀
‏این کار با فریمورک متن‌باز agent-wow انجام شده که هیچ منطق بازی به مدل نمی‌دهد؛ مدل خودش سیستم ادراک ساخت، اطلاعات مرحله‌ها را از دیتابیس بازی درآورد و با برنامه‌ای که خودش به زبان C++ نوشت مسیرها را حساب کرد.
‏⠀
‏به گفتهٔ گزارش cnBeta، کل این فرایند فقط با یک پرامپت Codex شروع شد و سازنده می‌خواهد بعداً ببیند یک ایجنت می‌تواند به‌تنهایی تا لول هشتاد برود یا نه.
‏
‏
📌
گزارش کامل cnBeta
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jjyVqKcwk6RXksfjxRQdi9vRllOR_1LdBI6u1xCU0_g_LJenkZDEaecyc-Xi1OH_hhB3SzsmS2FU-U69ZqkiI43vuf-eLRXlPYUnOg4ESBMIarr3lEffpgmi959A4kKXSDRbhVje3cNY3mTnfhU2grumHYKpSiwdDpjGrgISmEhpr_KJscZ7rnEfkZcYEGDgrDc6eWE4f6V3FgqCdlp9vESk3Hv3Vd6D7B02-NsskQUpOhR7rqIqg3qvV1-ATH2asO6bNuO7j1XpNs5hQpchUio_TzlzCXBYyNET-xuydoarBrdiC9oSEtcpRiHCevmp7yJfZEPK3EhRsH9CWw3eLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔍
اسکنر امنیتی هوشمند و رایگان برای دولوپرها
‏یه ابزار امنیتی مبتنی بر هوش مصنوعی اومده که بدون نصب ایجنت، آسیب‌پذیری‌ها رو پیدا می‌کنه و جایگزین ارزون تست‌های نفوذ گرونه.
‏⠀
‏•اسکن آسیب‌پذیری بدون نیاز به نصب ایجنت
‏• تحلیل و اولویت‌بندی یافته‌ها با هوش مصنوعی
‏• کد اصلی پروژه متن‌بازه
‏⠀
‏سازنده‌ش می‌گه چون هزینهٔ پنتست حرفه‌ای رو نداشته، خودش این ابزار رو ساخته.
‏برای دولوپرها و تیم‌های کوچیکی که بودجهٔ ابزارهای انترپرایزی رو ندارن ولی امنیت رو جدی می‌گیرن، شروع خوبیه.
‏⠀
‏
📌
ریپوی گیت‌هاب
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده: ⁮⁮ ⁮⁮
🆔
آیدی عددی برنده: 2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل: @ArchiveTell…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel | BOT</strong></div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده:
⁮⁮ ⁮⁮
🆔
آیدی عددی برنده:
2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل:
@ArchiveTell
🆔
آیدی چنل:
-1003718102196
🎊
تبریک به برنده!
🎊</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00  قرعه کشی انجام میشه و شماره مجازی تلگرام به…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uliyCaOazouXs7Ud_nlZlGb3yl0Ymsr0vJEpz9Fii3UgrLMWfZbNnqcwaD7TikqiWYGmR15CYWHezecZs6iM9qyoqMVi73Ws5dVeCiQjV4vAmZ42mB4RwUZDdLUP05pIP59Jt-rxZ37WXm4Kx4u7md-B5KdI0O36dWZL4_DxE-OCMI2aUb2quueu9l30OyiMPlCWLL3lsVcwTPHQbhDNdAXQ8s8EsR5mNT9VQ6uqrNaer-a4uF4xzrRP22yWq4shuvS3qQKvplcnFjJt_LDs-qCxIFMlsIGLkxBm0q6TFPhzyedexOy96lJ_66Qfv6aUnCokSBrDzHrm1Hiq2wzMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF_tVRm-uPDDRYVAtl9WSumgcMoQ8kMdemPg3Tf1BhzG6dIWULaVtqdNCqyRZWG0CbLrYfQnPn1MTf4Jn4p74CX70KJAa431mQlq3MAJusl5Lw74lXMBhRUWtdpR1rxXypt03pPdZcRx8IZcH-ioQK7o9YJGf_sbT0LwTIKtjgrQVD1J_Cz35tl9m0KVSwITSkoXC3U4u6dBtW9nw6Yi-6ut7F7hxkJxGSBFYkKdk_KFmqtuXwZnbSdUabt1HYk-Xexapx1ZlEsKHJo4WC-EVmpU2aNy6tHHvgryovfjWX4HRHHGUp8AA7EuFCVH5LQLHvO7Y4gYS73_Nod39L067w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📥
دانلود راحت ویدیو با Yoinks از شبکه‌های اجتماعی
⠀
‏این ابزار متن‌باز به شما اجازه می‌ده ویدیوها رو بدون تبلیغات اضافه و مستقیم از آدرس صفحه دانلود کنید.
⠀
‏
🎬
کافیه آدرس صفحه رو از یوتیوب، اینستاگرام، تیک‌تاک یا شبکه ایکس بهش بدید تا فایل اصلی بدون معطلی روی سیستمتون ذخیره بشه.
⠀
‏
✅
چون اجرای برنامه داخل ترمینال انجام می‌شه، فایل‌ها به سرور شخص ثالث نمی‌رن و خبری از تبلیغات آزاردهنده، پاپ‌آپ و تغییر مسیرهای مشکوک نیست. به گفتهٔ سازنده، بیش از ۱٬۸۰۰ وب‌سایت مختلف هم پشتیبانی می‌شن.
⠀
‏
📌
مخزن گیت‌هاب پروژه Yoinks
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlBOyK4G33VVbRcKJRid--2kGA-wWCTdZqh8QjHVY4iiE5S5oi-CjgtSV9Hz_qkqZbMwJlJFifpvE-oyJMP0kxv8dlQUqP8L49JC92Ufdz0io_q2OYfhNAYwkimNVuyXfzvuVhk29SiZ5f6xy2qqXnDRlMD-dadzpeiky2UEZV0QqJBzBmwsMRlrOF_9exfRV99oFITATANGP41keeaTmsy3C8Qaxqhu-3e-zHbUrdVjg1aQ_kJoddgrSy13h-P1JFhkQH0hZNJT7neyBOMSIo6J38Woem-IP0FTWPhm1MKxWS8i6FCpr-9wRqRVmo9A0bHSeVrAZUsU99GoIljxiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
ترفند فعال‌سازی Opus 5.5 روی Gemini Pro (آفر Jio)
🔥
اگه اکانت جیمینای پرو رو با طرح Jio فعال کردی ولی هنوز مدل‌های Opus 5.5 و Sonnet 5.5 توی antigravity برات باز نشده، اینو انجام بده تا بیاد:
💎
اول یه اکانت جدید رو به عنوان عضو خانواده (فمیلی) اد کن.
(دقت کن Sharing رو اکانت اصلی فعال باشه، و ریجن هر دو اکانت یکی باشه)
برای تغییر ریجن این پست رو انجام بدین
😱
بعد با همون اکانت جدیده لاگین شو.
تست کنید ببینید براتون فعال شد یا نه؛ تو کامنتا بگید
💀
👇
⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9metvMWXpE_q7txKA5dIYshWYwSNv79e4WY8Ugpe3G7hG50JzFbYn8y6MjsQrxLBLB7nHfvvePtmJpx-jFR831dSYjz5fLGvtxFEnoveA8q3lsvp2y1kxpn-WW4ix6I-gEziHFheuX73ZGYsykbM6p2k0nJtvIMjnMsCr8Kr8rgLwfHJku76FR_Zbjl3Lar-jjqabCzSiwmNB_ZL7vB1UHb9OCmdA-o-epPUGq_rSsdk6CrOiPUZjvKeOc8I77L-bCPaKnlH29BCMVYJ8A15ZlNen0hzudq23RdBF6N7UkP1P9gf9cYNrEjH6kpeqo9exb5LjqJVn1gtiXhNlRB8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cf3Ye7mAxC2q0PjdgZ6PW-FWevpdxCVd83IkZxsEXlL1MbwzBttk0PEqDXVyxD69TgxsAUCXB0XvSDofL688KDP7BkciAeapMFPIUKD0odFs6-KZYA1CpFSp_L2cdg_7gfKwhsqHqlHIZwp9v1HUdgy_6MHnr1RSS1CsXCtTyuva_DRGn-I6pqsZ7QqbNStEh-6xoFk4NFABgspDH9jTWIBtMB_jpiEGgImzKgBNhZ8aRqP-VxiXnANaZuBMGeRb0dN0TK2V1bh03eZzBFQVi163grw7fhIEoJVzFcbojpH032MdQ45DqTVCnP6mSev2cMgAV0IH4z6T7inAwVRmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
☁️
اکانت تلگرامت رو تبدیل به فضای ابری کن
⠀
‏یه اپ دسکتاپ که تلگرام رو به یه فضای ذخیره‌سازی تمیز و منظم تبدیل می‌کنه.
⠀
‏• مدیریت فایل‌ها داخل Saved Messages و کانال‌ها به شکل پوشه
‏• پیش‌نمایش، پخش ویدیو، همگام‌سازی پوشه، WebDAV و REST API
‏• ویندوز، مک، لینوکس و اندروید؛ همهٔ قابلیت‌ها رایگان
⠀
‏برنامه اوپن‌سورسه و مستقیم به تلگرام وصل می‌شه، بدون سرور واسط. ولی دو نکته: برای ورود به api_id و api_hash از
my.telegram.org
نیاز داری، و فایل‌ها تابع محدودیت‌های خود تلگرام‌ان — پس «نامحدود واقعی» نیست. نسخهٔ ۵ دلاری فقط تبلیغات رو حذف می‌کنه.
⠀
نکتهٔ امنیتی: اطلاعات ورود تلگرامت رو فقط توی نسخهٔ رسمی از صفحهٔ ریلیز گیت‌هاب وارد کن.
⠀
‏تو تلگرام رو بیشتر برای فایل استفاده می‌کنی یا چت؟
👇
⠀
‏
📌
مخزن گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYx1qe3CnAxAzgSpqEQWRSG_Cy4qUPMTt9V1WNxppuO__jWQsOcWUj9LsG1vbwY0xJgQf-94pJ7JE43PkakeDtCxaVMQhaLB-BPShSiA0AwI3jt4uUGbkjKJ4cSeH4CYBmcNV_LYF6vMSE0ClFSHfP-t8ZIBV9-HzGAlG1hZq24O1ldFDi9cyHOf87ULboEvAk30t7SH1e_hbAhZW1TPPJ-lQ1NJGIxj9E2kJkR-wJr8fx4DVn4xM0V2SGQXPypK9Frjk6oYhTI67THVNqR7x3n8bQBM82Ub_0za3oDOv8F9_ylSQh7kUeGaTogFYMUp0pD8V8wrc22ISUjY40ddGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش
‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.
‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری
‏
💸
کم کردن هزینه با prompt caching و compaction‏؛ به گفتهٔ اوپن‌ای‌آی ورودی کش‌شده تا ۹۵٪ ارزون‌تره
‏
✍️
پرامپت: هدف، مخاطب، محدودیت‌ها و معیار تموم شدن کار رو روشن بگو
‏
⏳
کارهای چندساعته: عوض کردن دستور وسط کار و سپردن بخش‌هایی از کار به agentهای فرعی
‏تمرکز راهنما بیشتر روی API و Codex هست و برای کسایی که با این مدل‌ها ابزار می‌سازن مفیدتره. قابلیت multi-agent هم فعلاً آزمایشیه.
‏
📌
راهنمای رسمی اوپن‌ای‌آی
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j56n2Ar-bHV4mBKgnlZu7rWcuNWNr9uBL198_CWdDIZfKrqZfUs6BwOxwctd-J-K2tw92iq68mwZBdwChoXGZ4kf8d7sxOlq684lSS9QFfNJLBSGOE3LqBnRV5wxTbBWS7NCyYLQhvFlV_XuPxYUP777fIPCDyaajuCnG5n_JdUF0AOOdmMOm8HjVFiw_ddDWHwNjASFXZoHOaE4bQCyUeKhEzS5rQCzKcSJbT7YCY2whLqJgs4Lm1zLtwfTvVk4QG8GaIzPlDJlGv73OB4h93agpy8OJUJ_1_rgH7i3l0OMU0H-Ys4dNHyiqnQ38-n4FBVAk4YRJAW2D798g-LLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚫
انتشار Grok 4.7 در اپ‌های گروک
⠀
‏مدل جدید گروک حالا توی اپ وب و موبایل هم در دسترسه و مدل پایهٔ همهٔ حالت‌ها شده
✅
⠀
‏به گفتهٔ xAI، نسخهٔ ۴.۷ روی یه مدل پایهٔ بزرگ‌تر ساخته شده و با یادگیری تقویتی طولانی‌تر، توی کارهای کدنویسی چندساعته و خود-بازبینی بهتر عمل می‌کنه. پنجرهٔ کانتکست ۵۰۰ هزار توکنه و قیمت API مثل نسخهٔ قبل مونده: ۲ دلار ورودی و ۶ دلار خروجی به‌ازای هر میلیون توکن.
⠀
‏
📌
یادداشت‌های انتشار xAI
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnwcAOKu4acMMVRnpms1j7qkwOt-8oozXNocp2G2JMnchokh3lTEyqWKoy2upBSSb_8rP4FB54Yhd3qy0zcxZdI4R-NxNo7a6SkuFNnXA2eMnvBHneh55Ee9S0exle61idoWqsbMwOGyFZXtdnh7eD1i_uplNAm_B90lCefyUiEKhvy1Yoz-NXwOTzuvhq6uIQs7jpWNXBiUDqDDu2hD2GMGnZ_lH6edm-B7QYkUDQ6cM9jhb9D-dan03I_0jFa4e_jJ2f8aMUK2IsgNbBovM4wLkjcrQjgiFbHStp-JMt-5UkUGRuwoHFQhQZj__rth9I4F20CxgNOnrYC-I7jfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان و ممبرهای عزیز آرشیوتل،
😍
ممنون که تا امروز با حمایت‌ها و کامنت‌های قشنگتون سرپا نگهمون داشتین. سعی کردیم به قول نیچه «با خون بنویسیم». راه سختی بود، ولی به لطف شما هنوز زنده‌ایم.
ممنون از ادمین‌ها و کانال‌هایی که با فوروارد و تبادل منصفانه حمایتمون کردن، مخصوصاً تیرکس نت. دمِ توسعه‌دهنده‌ها و همه‌ی کسایی هم گرم که تو روزهای قطعی، اینترنت رو زنده نگه داشتن.
تیم خفنمون هم که جای خودش رو داره:
احمد، که داره به مو می‌رسه ولی آفتاب شکوهش کانال رو نورانی کرده.
وگاس، که تو روزهای قهقرای من پشت کانال رو داشت.
«اس»، که با اینکه گوگل‌فنه
😁
یه متخصص واقعیه.
محمدجواد، معین، ایلیا و همه‌ی کسایی که سهمی داشتن.
خیلی‌هاتون دیگه دوستای نزدیکم شدین. امیدوارم سایه‌تون بالای سرمون بمونه و مثل همیشه با لایک و شیر پست‌ها همراهمون باشین، تا روزبه‌روز قوی‌تر ادامه بدیم
❤️</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzkGwxVLiWFrhLQPlbC1Q_wdWunL7Yf6tj23UIiMkzpmdRRJWyHjjGcu31gpvZEXXcvIAKPGp1cZmVpt2kbVI2dEgyWj46c-3NtaerJ7_3vP9gOy6q1JsRoimTVSLU-U58m5oPjuPoUEgyxOo_GYoxEwc5wkzoxAOz8EU7gATorfC2soDHHIc4VmtzqJ9u446vkwYvBAL1LYIE0PDsgx9y9roFHjFB8v4UO0RPnco8Yv4xWp2lyzgtAb2hhqxO0vbpXBIrukn4vIatkIcx8gFoALECqgbVuSzRqpve5ogpGi6EWRHSGZpL7k0IHZe2eh-kLczOuLm6l4CrdblTaP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کاربران رایگان جمینای فقط فلش‌لایت می‌گیرند
⠀
‏از ۹ اکتبر به بعد، کاربرهای رایگان جمینای فقط به مدل فلش‌لایت دسترسی دارن.
⠀
‏
🤖
کاربران رایگان: مدل‌های فلش و پرو حذف می‌شن
‏
🤖
مشترکان AI Plus: فقط فلش‌لایت و فلش می‌مونه، پرو می‌ره
‏
🤖
مشترکان پرو و اولترا هر سه مدل و قابلیت Deep Think را دارند
⠀
‏به گفتهٔ cnBeta، گوگل سیاست دسترسی حساب‌های شخصی جمینای رو چند روز بعد از معرفی مدل پرچم‌دار Gemini 4 Argon تغییر داده. خودِ Argon هم فعلاً فقط در اختیار سازمان‌های امنیتی و شرکای گوگله و به کاربر عادی نرسیده.
‏گوگل گفته زمان دقیق اجرا برای مشترکان پلاس رو با ایمیل اطلاع می‌ده.
‏این تغییر در مرکز راهنمای اپلیکیشن Gemini اعلام شده و کاربران AI Plus زمان دقیق اجرا را با ایمیل دریافت می‌کنند. سهمیهٔ مصرف از ماه مهٔ امسال بر اساس محاسبهٔ هر ۵ ساعت یک‌بار تازه‌سازی می‌شود و سقف هفتگی دارد.
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgshmAgAEw2V-RDRZGqg0bPOh1ybPd__86--5bUEIvSnxWQ9eJM2e3z3efX4Nn9xCBhb1MCuzzycXWlZcLbDC427Ar6W48n6dIKyI5BdFaTcO8usHU0oLEboUTT5ZGlo4z6sKTVjbbMeaYaHHBVzQPX65Una2eY1X8YkTcNdFeJP3QJI9oBUyRrOKX4olDudFXgj_zGyrd4SfxjFfsZq8KTi8VOCX2G_d5Q6rdFXt2SahHz02QzGP92TFGkZm5pLv7Hfe4dAJ8j4xhtGb9wpAVbl_NX-G37IcN2ycnzr9-3-XXnNg-Y3BgKI9ChC_rvRiY5NOrJrZmdqVvxfM7bSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🟠
مدل‌های Claude 5.5 به Antigravity گوگل آمدند
⠀
‏در محیط کدنویسی هوش‌مصنوعی Antigravity حالا می‌شود از Opus 5.5 و Sonnet 5.5 استفاده کرد.
⠀
‏به گزارش سایت appinn، دو مدل «Opus 5.5 Medium» و «Sonnet 5.5 Medium» به فهرست مدل‌های Antigravity اضافه شده‌اند. Opus 5.5 برای کارهای پیچیده و طولانی طراحی شده و Sonnet 5.5 برای کارهای روزمره و کدنویسی است؛ Sonnet 5.5 نسبت به Sonnet 5 بیش از ۳۰٪ سریع‌تر است.
‏نکته: برای استفاده از Antigravity باید با حساب گوگل وارد شوید.
⠀
‏شما Antigravity را امتحان کرده‌اید؟ این مدل‌ها را تست می‌کنید؟
👇
⠀
‏
📌
گزارش اضافه شدن مدل‌ها
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fQjbp81M2iNy11eCuM6Shh7kv91relcbPcTkHFGiNbJmEgCezkW_pZSwwHJKQgfmJpfWy6PHTBDmJG_VOt02GfQOgBr_dajNhPYBHYnGRxIAwnPpLPS1-pS1hniwBTJA7ENuB1QdpK8JRmlyVjrHTGGdP1Y-JQBf9ZAp962y_Rxu51T1N0QqdJK65tjaYlSujt5ktG4PrvA1UcxaS01J0_yrbKzDlhtUp9ky4-Pi7JLjxoYW641nSEHuXjRPPgKtlfbkxo9fZ3fmKI_pC-_9gVsF88sIHym_AKTU_23AwASnI9wKnrMiwvXfNmAP6f2UwJDmwE4Pix2R46bsWBpanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
مدل GPT-6.1 Sol اوپن‌ای‌آی رکورد زد
⠀
‏سم آلتمن می‌گوید ۶.۱ Sol سریع‌ترین رشد تاریخ مدل‌های اوپن‌ای‌آی را داشته و مشکل کندی‌اش هم حل شده.
⠀
‏رونمایی در DevDay؛ هوشمندی نزدیک به آسترا با یک‌پنجم قیمت
‏کانتکست حدود ۱.۰۵ میلیون توکن و خروجی حداکثر ۱۲۸ هزار توکن
‏ابزارهای جست‌وجوی وب، جست‌وجوی فایل و استفاده از کامپیوتر
⠀
‏به گفتهٔ آلتمن، این مدل در ساعات شلوغی کند می‌شد ولی حالا «باید خیلی بهتر شده باشد». قیمت‌گذاری‌اش هم برای توسعه‌دهنده‌های ایجنت جذاب است: ورودی هر میلیون توکن ۲ دلار و ورودی کش‌شده فقط ۰.۱۰ دلار.
⠀
‏نسخهٔ Ultrafast هم در راه است که تا ۸ برابر سریع‌تر جواب می‌دهد، البته با قیمت بالاتر. نکتهٔ جالب: قرار بود نسخهٔ ۶.۱ آسترا هم بیاید ولی به خاطر نگرانی‌های ایمنی فعلاً متوقف شده.
⠀⠀
‏
📌
گزارش عرضه در DevDay
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qx1jxGi-w4VeNTOQGtf8h8T6c2RueaQCuK1bddrdxcI01-3hmgfGN0qHwRk4rPdkvWSg0KTog7eTtYJ1o-UE-Q2UZknb1YKQphTR0m4Ld81mtg_N6W4W5CCiLrWZodbEVexXk9_WJ1Lck0RysrNnUy6xpG23PqRIO7T7jwpLQ8qX-zuNjwplLb4zjbGXw1t__90wfToeFrrO4BneSpA_6NuOV4bZWB9zZ4PIk3P8sxBvPknjvtkkyioG7fQc6mg4iIrqxKFLXtOYK5OmH_6DdWR8bxTt-Na1lVeHEjXha6DdkDgJ6P22pDaViKEBz6g9HSENTBzZRo1BG-q-UveXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔢
مدل Muse Spark در حل مسائل باز ریاضی
⠀
‏متا می‌گه ریاضی‌دان‌ها با کمک مدلش شش مسئلهٔ حل‌نشده رو پیش بردن.
⠀
‏• شش مقاله در حوزه‌های احتمال، معادلهٔ موج، نظریهٔ گروه‌ها و جبر
‏• مثلاً رد یک فرضیهٔ ۲۰۲۴ با ساختن گروهی ۳۸۴ عضوی
‏• و اثبات فروریزش در زمان متناهی برای جواب‌های معادلهٔ شرودینگر
⠀
‏نکتهٔ جالب اینه که توی هر مقاله مشخص شده کدوم بخش رو انسان نوشته و کدوم رو هوش مصنوعی. البته خود متا هم پذیرفته که بعضی از همین مسئله‌ها رو گروه‌های دیگه به‌طور مستقل حل کردن؛ پس این «کشف انحصاری هوش مصنوعی» نیست، بیشتر یه نمونهٔ جدی از همکاری انسان و مدله.
⠀
‏فکر می‌کنی هوش مصنوعی کی اولین قضیهٔ مهم رو تنهایی ثابت می‌کنه؟
👇
⠀
‏
📌
گزارش RuntimeWire
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7XpUxPXBEX68QEsGGLpUAgkFdW0_zZYCoVCRPX1GbVSqaCFH7rAL9wPi_aR8a4_ZxFod8N4nrpUPitrME864ubdHKi4Eo78X3iVMm_sCs565ElJYyL0JOhPbcCfIxS_JifctarmVX9eK7bRb1a6Ihm1PWhOCCOMqnVz0TLFOjdwPChhpqmMLk4WMKr8vx5SZt9BLi17XrCqI-ZF3F8VLogChnuAP_qGcN79_AnmwiVjmsrbGxAyZiwdR8mDDmf3QZtX6xwPcJY-8eXAwXUpWOnT4oh3Ps2kwWqpCfpZ9-k925rKQpg8vKfEC2F6ZHgf-YfclpuREfZufdIkdSTM1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📨
ایمیل موقت جیمیل و اوت‌لوک رو با temp.tf بگیر
⠀
‏یه آدرس جیمیل، اوت‌لوک یا هات‌میل برای ثبت‌نام‌های یک‌باره می‌گیری و کد تأیید رو همون‌جا توی سایت می‌خونی.
⠀
‏
✅
نه ثبت‌نام می‌خواد نه رمز؛ آدرس رو کپی می‌کنی و تمام
‏
📎
پیوست هم می‌رسه؛ عکس همون‌جا باز می‌شه و بقیهٔ فایل‌ها دانلود می‌شن
‏
🧩
یه API رایگان هم داره، بدون نیاز به کلید و با سقف ۶۰ درخواست در دقیقه
‏
این آدرس‌ها با plus alias و نقطه‌گذاری جیمیل از حساب‌های خود
temp.tf
ساخته می‌شن؛ یعنی ایمیل‌هات مستقیم می‌ره توی حساب اون‌ها و چون رمزی در کار نیست، هر کی آدرس رو داشته باشه می‌تونه ایمیل‌هاش رو بخونه.
⠀
‏
📌
سایت ایمیل موقت
‏
🌐
راهنمای برنامه‌نویس‌ها
‏
🟢
سیاست حریم خصوصی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7m2HXsFS-sd9avF9pz8PmBYKYpFT6GiOGPb6BZLb2CpQ25tCQJlW9sDTMrZeoOs5eYDq42lhlaFkEu1J_jrH4KBasu0zAMZVipbjLPrGJbmLkkv3ccjqIA2PUwWEQchTaORSJMF1m38vdGHJ34I22HbQ4K-X-wBzymAJnPogctzbm3CX5qzCJUwTiXUCSepW7QRuE-OQgStMDQZs3xobScXUzNwsph1tdhwvw6TWUV8KCnX164oy_DwILpdzPCZ9F-HjkpuCUj7y4SapxYBBXmSH4YjTB59aONTL08s8-e29vUdhgd9dT3mDJR5ufAlXrtJWVSJ5DuHT5DerczfHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های قدرتمند هوش مصنوعی
💥
🆓
GPT 6 Astra | Opus 5.5 | GPT 6.1 Sol | Sonnet 5.5 | Gemini 3.8
✅
با این سایت میتونید 7 روز مهلت برای تست مدل های بالا رو در پلن Max دریافت کنید
🎉
🎁
⭐️
قابلیت ها :
🤖
چت با هوش مصنوعی
⚡️
تبدیل لحظه‌ای صدا به متن
📢
تشخیص و تفکیک گوینده‌ها
📖
پشتیبانی از ۱۴۰+ زبان
🗣
تبدیل فایل صوتی و ویدئویی به متن
📞
تبدیل تماس تلفنی به متن
📝
تبدیل جلسات Zoom، Google Meet و Teams به متن
⏲
ثبت دقیق زمان هر بخش از مکالمه
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9AgLCKXBKouey9j4Ut1vEGT19-jVUcO3md4SSc2ItgrPCy31ZAeETQuZfLlReV8MwRuV9j2eeO2QZnqUCltzg_Uh86OlLOHeAOxnxdCz4yvU-95gHgIYj-P3uVDJ0JlvirKBWhdz31bb7ZRlxkhwWR6BB9nphW1MYKjk7vt9W411hXWACJ7q7dY5tj7SWF-MQvRev48hhTuuE70h62ZAzsLkUpINSzhEwkKsGcb2vxEi1hf01e3C9TY4paOT-wdn-DVfoKXvmGaf5krce9FkwA5aLnDBR7PQtPj3ST8obdchlpT4GLR4qu-8wU3bFb_o9ZMHdo9cbMXjZE0W_td8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFKmtSrzLzekCZawHQ5Wt0O1K6gxJ8Qgn88jzWl1XpDJ8GkJRs06dW4gn4kuPYiHAhOmnN7bpHZyD4FKjLNaJPCpXkKduDw5MamuaP9HX2YJZceLTnhqZr7f-hNICdkdREBrEVp9tXpnKp8bi1X5jQOCnVR3ZvQKSq9gqE5kKuK99AXBX_Lr8EMdwyJ_J7EnrQ3a-S22nTW0KunWEQddirwRIUUENqVmTLpVQBU0-JhCjvcTXXPp6ScZCJPwvf6AfUNT328P6qlQk40IBQEICbj_nFEyzQ0Ud-8ZCdZDmy5RySfKVI23CEFZNcOHVXX2Ewvui1Icjfwgohr8iG-bbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⏰
سهمیهٔ ChatGPT امشب ریست می‌شه
‏به گفتهٔ مدیر OpenAI، ساعت ۲۰:۳۰ امشب به وقت تهران سهمیهٔ همهٔ اکانت‌های پولی ChatGPT ریست می‌شه.
‏
‏این ریست ساعت ۱۰ صبح به وقت غرب آمریکاست که می‌شه ۱ بامداد فردا به وقت پکن. Tibo همچنین گفته مدل GPT-6.1 Sol اوایل عرضه به‌خاطر بار زیاد کند شده بود و الان سرعتش به حالت عادی برگشته.
‏
‏
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vk62RNwvOC7tpYtmYzX18NJDvGhO-QpIPpwqesbW2eFDx8iGrxUtmxJ7eauq3nHQrPqElDwV5-Ay-y4HYa3OucsFKrbKWAQBq9jrMkEsHDbhUxKLLkgSiVcOul7VjHCfLHaXyPcZsPOtitkepdn5S6win8cdVcph7R_umf_Ir3RxlrzEZMEa7pZN4Kt58u91vxr1rzbqtnROzmF3KLJ-CYxjE0Uz1IhEF5dWs1E3cp0z8Mgwg9ViBSQyDvOCjjdOi5gmurVqi4XTpZihmgR4yP74YG2Dxec8vDh-I4Me_dnkXtRBbN8AZh2iv_dDl2aTCDJU6Hnril_1pDQqdk-8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
ابزار InkGist برای خلاصهٔ صفحه‌های وب
‏لینک هر صفحهٔ وب رو بهش بدی، تو چند ثانیه نکته‌های اصلی، کاربردها و کارهایی که باید انجام بدی رو تحویل می‌ده.
‏
🤖
مدل‌های Zhipu و DeepSeek و Gemini پشتیبانی می‌شن
‏
📚
خلاصه‌ها تو بوکمارک‌های ابری چندکاربره ذخیره می‌شن
‏
🧩
افزونهٔ مرورگر بوکمارک‌ها رو با یک کلیک وارد می‌کنه
‏
📷
از صفحه‌ها نسخهٔ آفلاین هم ذخیره می‌کنه
‏
🏠
می‌شه روی سرور شخصی نصبش کرد
‏به گفتهٔ سازنده، متن صفحه اول با Defuddle به‌صورت محلی استخراج می‌شه و بعد برای خلاصه به مدل زبانی می‌ره. پس حتی تو نسخهٔ شخصی هم محتوای صفحه برای سرویس مدلی که انتخاب می‌کنی فرستاده می‌شه. نسخهٔ نمایشی آنلاین هم روزی ۱۰ بار خلاصهٔ رایگان می‌ده.
‏
📌
مخزن گیت‌هاب پروژه
‏
🟢
نسخهٔ نمایشی آنلاین
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsGcF4JRaqSkGC7BakCXsFGihnE23HWYi59PrxYEKyhpFS3MjSbyothwEzt70Wc7wQYG_L6xOB7QX_jQt2TylUimwmVSBb9V6vUHD-anXPL1EoyKU96OGqkIM_5y-8wakq-ORHXowdp9bUD0yt2tzft0zwZn50lyZPSn_M7p3gjca4Re3iu6xa91qGCEepdq9XZv3DmolDHbwBRCFuyvNkAz951jlHsN7ybUB1YJJnWnMcECLDlMAI59vUzNEbip4KXSSjGmrMGadxkMxEPPM3UOoWQ9dpDh8O-xsTIeWG7qXrsla8SzV9MymgbCcFmbbX3WcJQCdXV6SutvSXICaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YukRnDsEspmn4KiSsgfr1qJ5WewxBWTlsH0g8aa3J6rB5fIO5I8uhDvsglLkCYBciyoRv9cnn68hV9GNJoI74TksH_8GarwqdHrQtu9NolW-qrfw2k2z0TMcEf-HNB3aJMY9EektAjd_uJy4zsqKFwkOyQ3xU7ZYywwuFdtKO_gN-27tosYDJao_mfqZ_V6FyeEChvMrPc_JpMHCAKd1oysU5ytR4hFjucCv4ddGZzpMiK2bdT49lVRQYTq5Per8dVj3FPyavshn1VWFYx7lPPJbect_cTzwE7t5RMg3lW2u6KJk0DhXV9XdR14ye71WGA9tatud5ifI2QmzdL2QjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه
‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.
‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد
‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد
‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه
‏به ادعای Anthropic‏، نسخهٔ Sonnet 5.5 بیش از ۳۰٪ از Sonnet 5 سریع‌تره و هزینهٔ هر کار باهاش تا ۳۰٪ کمتر شده. این عددها رو فقط خود شرکت اعلام کرده.
‏برای Haiku 5.5 هنوز تاریخ دقیق، قیمت و شناسهٔ مدل اعلام نشده. حرفی هم که می‌گه این مدل از Opus بهتره، فعلاً هیچ منبعی نداره.
‏به نظرتون مدل کوچیک بعدی به کارتون میاد؟
👇
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o94nFe_E6KKa2QRG1eua_f8G980ZjtHMaocVGiiCVnb5lSddzNHKPrFGYLKasO9R_OIR6hXWCHgtc5uBSnsG8XiYI0W0lG_OgfxI2g7fyLuTwTrfkqEikMP6kYROYuBdC6tQ6EknjJKkcpQoSr2OmXvovpC9tXwPTYsiKKIGrEaeSpOJOtMc8fXLKTyseRsQUcaaIPwwetVqCKNKpFOxK_WaLlP-hd7Wvb6nYBK0nGgNsh3cz6bzUWB3kZdsMFfvy2BD6N9oZnT6W4wQynQ4EuGC4PqL6lrVZPK7ni4b6_a9g2YzfAVDKQFmCPhecuvuBq1cUCCaNXUV0uVe27l-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Claude Sonnet 5.5 روی اوپن‌روتر عرضه شد
⠀
‏به گفتهٔ Requesty، مدل Claude Sonnet 5.5 با قیمت ۲ دلار به‌ازای هر میلیون توکن ورودی روی OpenRouter عرضه شد.
⠀
‏بیش از ۳۰ درصد سریع‌تر از نسخهٔ قبلی
‏هزینه تا ۳۰ درصد کمتر در بیشتر کارها
‏پنجرهٔ کانتکست یک میلیون توکنی
⠀
‏این مدل دومین عضو خانوادهٔ Claude 5.5 است و به گفتهٔ Requesty در کدنویسی و کارهای ایجنتی نتیجهٔ به‌مراتب بهتری می‌دهد؛ قیمت خروجی هم ۱۰ دلار به‌ازای هر میلیون توکن است.
⠀
‏مدل هم‌زمان روی پلتفرم
B.AI
هم در دسترس قرار گرفته است.
⠀
‏
📌
اعلان B.AI در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bs9WUPDySjPKKrK92Qz0ZuVEH96n7wn_FdptMMpysQOfUD8R_Cb6-cCCK9lZGgddSnmxV4a-AH4hi5SmBdHWwbEsTPEAz33AbaDo9pSu7UysglUJOwKBvgPn-m-V1wPJkGr1fIkhxOL1as6nk-4s-Hu0LeG7Y7FGE1EVd02KZiBGLx8WwEPNTgBZHARUamGLSrOOVPSDbl87o3zdAyCrV2xBYjUkzoRKKluUJxM7dl3waiLmh0g3bCN_V4cw0fn4fBFTHuIFMubE9JGiDMPYIYuhBDqgN1U-OMjDjlmZ-cDt7hEpOU44Rx73jDeBkgm9wfMmkKsEOchJz9KRXdzTVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
همهٔ دستیارهای کدنویسی توی برنامهٔ ccgui یکجا
‏اگه کار با دستیارهای کدنویسی توی ترمینال برات سخته، این برنامه همه‌شون رو توی یه پنجره میاره.
‏
🧠
موتورها: Claude Code‏، Codex‏، Gemini‏، OpenCode‏، DeepSeek Harness و چندتای دیگه
‏
🫧
یه برنامهٔ دسکتاپ که با Tauri ساخته شده
‏
📦
نسخهٔ مک، ویندوز و لینوکس طبق صفحهٔ دانلود
‏
🔄
آخرین نسخه روی گیت‌هاب: v1.1.0 در 28 سپتامبر 2026
‏کد برنامه روی گیت‌هاب بازه. ولی ccgui فقط یه رابط گرافیکیه و خودش موتور نداره. برای هر موتور معمولاً به حساب یا کلید API خود همون سرویس نیاز داری. کدت هم برای پردازش به سرور همون سرویس فرستاده می‌شه.
‏
🐱
گیت‌هاب ccgui
‏
📥
صفحهٔ دانلود برنامه
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyLBwfXyiyNPmvVmVWqisxwWPyLUXs38uqbXoKnVeQkp3YnY9VEABy0DSBWCWRPkhvMEvwfTws04ZlYa0DJGrP9hyHvZzPxPNAfbWBQcPZXKAKi8U-TTPWzyylG0UE1FAWhJ9GryKoi0-YSvRgAxlf3LJ9v5vAQkNbij_3EUZ8InYDcxNWGapoE0WZ5cGJ-6qn05w5j8ECRn-58Opzuwvu9hRHQJ0dh_QtjFVeygvx08j48gA_bzffpMYGhqXzjsFxembX4KuRJ0VgvhRJbnJk8Drn1XNjpt14tB98ltD5MUVdxrxm3y0PGg78vjzsyHv0m8LfAvn0vGMJpwY8UUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LV8DV_PNQ2LKgj18FIjob-YiyiIrGtIDQWKoD_e2U2CIqk1-3V0hK0ABgWzzugTI68qQjRArD2q5Qn91k4Z062x_Z8f1MNbiKiUcQ9eQ9V9olr3eUFM613L7c6XxKeJywntLJDw8Qs68PjKsunJQeHv9dJM6wC8mGZhdezi4MSS4hFsk8pOol4QhmmSZ50dy7mkqwVTKKn4fWnciRoKYmtVtk987ygUirmff8KNnjnb_UQLaLxbVKlaqdsnsXaAtaz5U80SxS-ZwbnCw_gQMPGc4QOpUQIUEEo7yXUJvZfA06WVpeAEoecvJWgBpzPY6NeAWCwkIudU8E0orRTsEEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Inke3ArJ0_XJ5_zqrzj__OD9BWfqhifyoFZ-l3_Du-O1Qq9hHH8xtlFVRuldodS8bMQT-F05Lcs9b0UMc-s63YC-ZEDoq5t_P8G7C3TdCcrX0TCC3UKFiLMgiMTX5h8EycqicKGjhRjBGnSgTYbEwfaI-V6LXdEllEj_no-0BYVX8LWriLy5b63bBfK-FmcjAMR34d-FCveOuV51mCaJUpNcM-wLI9pRT76ECbfXGtYX9Wj7mOK6QuW2W841_aVFGiv9M-tvXfoPePGAG6tFQPOs14HCD2B-CocB7H7Z3g1upcXAB66PBGeOmfW4jTVqVxmeYqJtVb09VGtgIVyYlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVeliCbtc_XSLdimh6bIiqBXFDvDlMd1Wu3x0B-IDBBVX6BJ7SDN7hyyDGqV29tGuvYYFb9dTbHQGK4wqIpx6FjegaNR1Dr7hBnZGYtSpO5SqenEk_Ht2UAyde42SWghjIKjJJsZObY1jmAHHEkF5zms_sFj6kIDqpdrNvCIhqsL0zC7y7T7BvgvM2k0sYnXFw0ccTSedicMCDLtFJY7pB5-F3QeOlvTzAGfLLwchRdeCONi_vlK9H0R0CyhOgurDmRIApKykJnBDQ742F61WNj_J7h6ma3vjc7QbSSxFAWg4pMzI62YOp-u210k-M-Am9BCm75XihsRzWxWrpdN9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WknQbQyb_YU1T6Ck9GElOhb8gIhXS_4Rp-nWT5cWTuRRD-qrSkIqv5kGMDYPm7pCkbOAgTD4qy9wZTrlQXiHKppOcIDtdGoCH2RJ7kZb1XIy4ZTNzg5XcuzJELHj3MvegedmH_8gOdvuEvFNyFWG_aqCvSUH7GstS0YCoV3wjt8Xoyf1_RGKL5WMjU9jmkAMs-AgwjYtVOcPv0wuGIuLr4CKDm7aw5igTPrUuU4T4hteb6ik4Bf4KmARjMZn_fpwMws06Tt20qV8u8QMmSosTjisJPZ9sBUkwwq-_Pp8YJ7i9VX5TsSwnjgCECFXhltDOdsT1s48Z56W5zjqdbNEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vGHBMvJCaJPTailboAyVy95JSt8e7OAe_fyfRWrxp7t1BnV-gm5G7c9kUK8_bbCCbzTqNSfQV5wNM3t_aHkTeHPDZos7t12S07FcqYHZRqdZCH4l377_RO4v4qgYxsx7qGIG1IOCTLDXfEeh-lspKTXPr56kf5KNuhGBM3vCWQY4yAhMam6nuBWiICnWEtYKBorQ1dPugr4wqYvG-ALejxKdGdNjIezru12JEEJz51esgDPTd7SEbLUF9Da5q5JQG4udXE8xQt2RqjcXITWvySeV2I_MPbSruo2EL9wLo8VWNgRyqXBHT-Tuk9MB4Taek6kpW4TMcey4ezKIPx-Q2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkZbD--XD3uKMUxzxBLmzKRHw7n9pce3rh0X9GdM-9349kv7EyCY64dYQacDc9zQ9gIMKH8K0BP56V3NbPS62pD4hOWgfqWAVcUJf-NLke1ZY1q4uHF_AqibcCCsmyOXGtjErPzmlOj3HKjRL14qLRiHOMrrZL2mF1FI8DJ_bZHTC8AjI7ZYAqfJ1GfafgQ3pZEjQWh7Z-yHu8EB1zMlLZ_7ScC1m9XXXLVWOZ8aToDZslob8hBrI5hCqZEPMtXPBJT7igQW83osn39gcXBadPUdzLzdRLuwLlzo4kXlQfqjjl1m8ndjpibQhMF-9OXiK5LkEgNJI9Sz3OT_8BxP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
اسکیل‌های Gemini برای همه رایگان شد
‏⠀
‏گوگل قابلیت اسکیل‌ها را که قبلاً فقط برای کاربران پولی بود برای حساب‌های رایگان هم باز کرد.
‏⠀
‏
🫧
با اسلش در کادر چت، دستورهای سفارشی‌ات را سریع صدا بزن
‏
🫧
جم‌هایی که ساخته‌ای حفظ می‌مانند و از ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند
‏
🫧
فعلاً برای حساب‌های شخصی بالای ۱۸ سال است و انتشارش تدریجی پیش می‌رود
‏⠀
‏اسکیل‌ها نسخهٔ ارتقایافتهٔ جم‌ها هستند؛ به‌جای گشتن در فهرست بلند، کافی است در کادر چت اسلش بزنی و دستور دلخواه را انتخاب کنی. گوگل می‌گوید جم‌های قدیمی‌ات هم در مهاجرت ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند.
‏انتشار هنوز برای همه کامل نشده و ممکن است دکمهٔ ساخت اسکیل را نبینی؛ چند روز دیگر دوباره سر بزن. ساخت اسکیل به حساب گوگل وصل است و حواست به داده‌هایی که وارد چت می‌کنی باشد.
‏⠀
‏برای چه کاری اولین اسکیلت را می‌سازی؟
👇
‏⠀
‏
📌
صفحهٔ ساخت اسکیل
‏
🌐
گزارش نئووین
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1ZshPjM7spiyb1rciLWbcUNKobIEKOHFtVhk7CXEDhf2MMj04K9aDBa8D_k0yJ4LGPdudYNdI_Yt2QxIh2Uq86UOsIDhBCjJuKw76reciYIg6ChEVig2SG2c_v6hLb7pxk7pVx6InR8O9UO_axt7daQIUCvf1b6WXOGTgPPsgHhmCaRJnGadjgQit2lh52zW2OHRNxdolBC_YG8x4mLDJX5ig9kjp5k5j8JdY4ZUEoATDCDoxHCJ6UWQQHvaUTd8kcuWMyG9H2X7L0n-LCJRCThtKEEpX3_O8nC3Wme4Pyc5mr4XHupiBwCF294iqlVSJA5MPONe8OvPDhqrxUczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
آخرشم بلدین دیگه تو Routing rules بزنین کل سرور از اوت باند warp رد شه
هسته و پنل رو یه دور ریستارت کنید اعمال شه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfpQ2JA-uyw1GG_x9Cpdsndf7Aea-P8sT-RGdLkKiIQ0BXoMdu6cmUwhm4-2hf3C7Ba76RacFub5IFLp_vZFglgKCukwMsndjNEJ4_fc1INGbELm1Z0copcwLocNcVg3FiL9i7419xjmCS7jOSC8ISuvLFmh4f0e5rR-iXV9rqAeO_1N0eC5xAA2wfNJk-o1P8FQctqTKOYUomGcvaKhq_R7sdbD0jT-9bfZkQsZleKXiXX1nWI0lRCzpeYlmqLVOr2n3ClkS9XpkRaPl2ClgoBlegBvOa889OUDEPvLlQvU9yS44udzKIA4f8TgOhydxzvcuYv2CgBJki9vZaqPEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmUhULNvVY3DIzo5v4voK4HoszzGeiFhpowJcrFQrgnHvPSWDAJa7Kj9k1B8JitJFwuttXAW5MgT6MEFfHJHlEa6pbPthGOb21IG_H9mvgeL3KdfWccmrwdeTDA7yd58B4PheHUYaLxqqzobk7iQ3CvJsT7TSaUboZdmvTSCW7jTB86MHx674a721DA1kafd2B782pdQUaUxkr_bZ_Xybw8Ir_YgBpFx16X6k5t4MDLOLWNjJhxy_EJ6Hq__c_rkw46GXT3EVYEHPv11x_rc3vaESj_-amQk4FWt78RFOHh07IgLH2bSSQYPhd3RuESJoM-Yc9awV1mXGbxJP-m7ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQ9UQqOgYYxxOAY0rpwyHZpokOZu3zoqO8MWL8nDJYZPZT7eaNdkidlAESpkEqAA5Apg9FByf6akfE_lqrmocVrBkj6GS_hDboUyWhsThty7RovO7Rm5vPqz_gl3GW0McAyyks_AHekC6oUbZgJmCJWoCYTd8kAmxKLpV4KZyALkuhueLcbYCYV3Ttg2f7g2JLofNM6inOpvWflDPH-cje6vRdTj89Cgqe5I84E_uGJytFaKynoAUwBBoq_x3b8jrROx_q9qrJOXECWgRmA0sFlQN3BEPYcQIsok4wZgT9QJDD7mD46aeYkIV6NapeEHnKuBDUPMorkWw6Vmt7LyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G95szbxApEeQ-XaE1Jg6u80k4yPidrXU6J0BhNSHVETsL2qFcmVa_1uyv00C94GEgESkom5G2zfU7fJYkfJc-ILBUxTGlZRUdJUk1IuSnup3PCyIYuly0KY8z80a4UM3I4EgxEzrwV_WIPXkfUhHggjchDO7XI8IsPlmrQT3oKOyNqE-0TZ6vT7Au3srdlxkKYQB9XYClsygmIgzr9riyt5qE6UICpAUTSUA8qiJkGWaDxH2NXLWMn3Aql0N-l714hfLCL6_HRf9ai7RqKAJFeJvEnh3AG19JvcFA4Dy0ohvYdxulmQQZpdfSxrNmhyUzstwqT1oPD60ipyWKSuXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v9Nn_bZQ_jF5YF_AfAtlYdjrQOGt-kBCZVOLFPZzMWMyhebBwBl9Bg1ZgzSSsWZhtyz7pZN470GyPbsFF9pRx26YNiVpvzNSMd5P0BqWuOpbngbz5d57IWiiSxxjMuJqzzM6TMbh2I0o-5iEIKreaa-XNhbj7viDFhzlZFZEk5KJxymO4QUqUPCObsSNftYdmQRzn8syPqwQuJqfoVPQ-sTy4LeSWSdIZncuuuE9jjwtaCTWaoTOYSy7leQFI6dqlmGyDcHJue17jLHRyQ8DqKpSy7JOiFGKByO8teeeF3j2Z0WQMsN48Vr_Ej699GhsBQsBK-PVRqPVjJWh_Ci5Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5qAL5oBDPVfMg2OdGlwtj0t8MeRj6nb33nrFgqpBvSTI4Zilq3Wu1IyDMc1a-Gm-sSoItThKg0xNMQqk-MJs9bI0XdHEuz41jZokWrTkw7qf3typmUXGxuyjedB8Cc7zCxaEC699NThHtWIx-HtHJl9cCMSwknxNB95aYE_jPb3n-UmTmB9jjSgkoDmLw7_cZMsrjtdd_Vox_32hrA8oBHpkw70n53D2V4GbWDR1jUI673XqexeAVUbfSXkk2wV8On5VoLhjHpiFfnLlCHzjrm9QnsO_5bvlkBcQhlTf_B2vEQVsIg4juF_j8Gzz62cZ7wWR-bL6lTxVJCMNE6DPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lShGtxVmkTsJCEc_7N9ZtCcej_jsAtAT-O384gearUcrsGbPLqcBBCaA87XqTcX3u3bw2GkLiAyt_E1HvsaJP3WtwYzGwp2V25NMxvvmyHGnNoVO8i1IRrR_0M2W9Fgj9LvVBORiEZf6Rlp317uMFJzUMkj49PJyCwlwcCOVtbZp9GhleTBvHgik0P5_zTvalTnj3BqXQGcCVl2pbND9MT5wVA0NMMQWqzT3DxXMtVR8PBe5-jzhpAJ-xUcWTeSB5-I-xNNWgo4srqdXmgJWJ9r0WYxel0bdPvTR_w53by4iarqdLu8RajCscNnINCHVyJldLPCFimliTdXdtw5lCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره
Exploit
با نام
Relapse
برای
Jailbreak
کردن
PS5
منتشر شده که
Firmware
های
7.00
تا
13.60
را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJaUayv4Ybm69CVXCaIJvm0g31v2tSG4gXc3FkUumQJWYxxVGTXLbJiLrbiCdCDMXQ2JyuxQSDFQq3WLwzIIOEMdkkR6eJu6MfVv23sPekRweM36VMCu8Jh6N3F4-1zX7Kq_Z-UpHrMS_AstRdWHa_GJyd-230Lgq8yK_Q6nol-6o5Ve-nmed8CoxQmWDA3bt4eYyLu6ydpShhH2GkpYBtt9dl6UEvb83hjGrfkEx2KpTWMs5LlORBPfhnq9CHRIBO_0l_PXVHhdaYjU2Y8nhVF1f7o7hXxKsY3vgrddXaz_aYtLEUTwNm6SzBToAPBQSsmmhq7UgTPgeRfvWyQQTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های زیر
💥
🆓
Opus 5 | Opus 4.8
✅
با این سایت میتونید 100 دلار API برای مدل های بالا دریافت کنید
✅
⚙
پیش‌نیاز ها :
اکانت گیتهاب 1 ساله + یک اکانت دیسکورد
💵
هزینه مدل ها :
ورودی 2 دلار خروجی 10 دلار بابت هر میلیون توکن
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAtP7J69aMbIRvKBkhLlYzSfVQrxGGhWjYAylpgsFL1_9Ignfm7SgLixZaNTl8QoLLC2tvLEOhKYK-5vfbuyLUJq5fTzGX-SrPG1Zd1ZlzRkNrmWwllPxQt9DqESD0G0WoXgnf94dwaGQmzn9ORJ3wkxIYd6BGqPEJo9dlVzvxLUb8WHYuNimL92tnxTrTtSSfX8ae9FT0duMBuy16kJETsun0xaoBp0PHbrhsqhvxy5nplv-gKUj5Z16K5Iv_oJfN-O6sMg9o_K7JVls6rKiXVNoAfA1tjcsu7jVWI-XRjIWONx57avT2OW3FmjbFpEqKi1X-kEHf1SO40yqqNc9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلودر دسکتاپی deviload برای یوتیوب
⠀
‏یه برنامهٔ دسکتاپی که yt-dlp رو پشت یک رابط گرافیکی ساده می‌ذاره و دانلود رو به چند کلیک کم می‌کنه.
⠀
‏
🎬
دانلود ویدیو در MP4/MKV/WebM و صدای MP3 و FLAC با انتخاب کیفیت
‏
📃
پلی‌لیست، زیرنویس، SponsorBlock و تفکیک بر اساس چپترها
‏
📺
ضبط پخش زنده و رصد کانال‌ها برای دانلود خودکار موارد تازه
‏
🎛
ادیتور Devil Cut برای برش، ترنزیشن، سرعت و تغییر نسبت تصویر
‏
🔄
کانورتر با هدف حجم مشخص برای دیسکورد و واتساپ و ایمیل
‏
📱
فرستادن فایل به گوشی با اسکن QR روی شبکهٔ محلی
⠀
‏لاگین یوتیوب و اینستاگرام داخل خود برنامه انجام می‌شه و کوکی‌ها همون‌جا می‌مونه. صف دانلود تا ۸ مورد هم‌زمان می‌گیره و خطاها رو خودش دوباره امتحان می‌کنه.
⠀
‏با Rust و Tauri نوشته شده، yt-dlp و FFmpeg همراهشه، تلمتری نمی‌فرسته و رایگانه. ویندوز نسخهٔ اصلیه و مک و لینوکس هم بیلد دارن.
⠀
‌‏
🐱
مخزن پروژه
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
