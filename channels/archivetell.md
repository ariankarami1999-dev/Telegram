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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 03:10:30</div>
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
<div class="tg-footer">👁️ 710 · <a href="https://t.me/ArchiveTell/8084" target="_blank">📅 23:07 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 916 · <a href="https://t.me/ArchiveTell/8083" target="_blank">📅 21:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8082">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/ArchiveTell/8082" target="_blank">📅 21:33 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 881 · <a href="https://t.me/ArchiveTell/8081" target="_blank">📅 21:29 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 916 · <a href="https://t.me/ArchiveTell/8077" target="_blank">📅 21:17 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 975 · <a href="https://t.me/ArchiveTell/8076" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/8075" target="_blank">📅 18:58 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/8074" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/8073" target="_blank">📅 22:50 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/8070" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/8069" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8068">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-nQcRPXmfHUEasTt9dreG4OkoyioskEgg4LzflJoZHpQKtaD1-zcXknltcc3RxPsYni4qHohLZ7vRg-OuV4b3H4iSn6gcKv3xcPkUQvMuNJ7-CGpS1yUplqNiqfSLeFPP3qw7lZySonr2sbOF_W44bByuKxxgfdPXQORhNwB3qTs1RBNNJ2FYy9P89DkdSXGvhaFyEhXVt6hcnN4M1OVsgMaGjQq0MCJkuRyh5lpmVIVuRCqx4lzsuxaG3uQDMp98FVD6VcluR0x5quyKEZIO6Av-3KQeaMiVrF6xYy1pkT02nNB0ZObpWSRN8q1H7YTdZm5h7ENmD7Sh87Qsgx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی GTA 5 کاملا رایگان - نسخه وب
https://gta.deloskiyt.pl/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8068" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/8067" target="_blank">📅 10:10 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vVvjJAVg9eJ_0g0P2p_eHi9ikk-6Uew1_DBL7QiVqqzMFk6ZLa7Nv_pEthHXwXYwd5IhsgJQYBo7l5OqyUg5MkwTtgnO05b5v3yWsNcA5IhHLwGqLfV8lOMXB4ihdLyxEDg32f3zDBB2GvND5ADdrXWFChMfQYhX-Mfaq4IGcCXfhTRns3yHT15HCjyi73YDPTBYPsu872zKVD0sUcmkwsKJpVrg6xKurtKeM5Cr4qpfQQVllE0IT-Q9Gc38v0a7VsJTdgYF56hEt2RylZ_fjzpiSoAfYZtGjTWbpbCg6nvZvvZlk53gsf9mBX19PMgx4H7xS1kK67uHJJ4fvJyJSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRgk6KUAg9CLcTo2ookEBb6271DcnRkq7uqzxq3sX_unDFcaxDUf4CL3BbZ9q5cTjI327iWCaYZkYn-KQWbVJqGHhWqGLqesjZal4tQEAPRZpw2jCkIxE_2Ee1LIigcN1gStWY7BxGRM3KhqiabB_cQmu3y0PxLCUfI10le_6KvUly-TiKONwDzAM4DYp40p6uB42FlOjys8yRJ9FcKeib2zW2ji0UHfzNTqhh6glC0BoUzGaDZVsho7L0_I_OpsZbkvuV-BNuMZitC715Yj6HA0gnygxLKuiWDZEz8zfy6stCXwmR9z2uOhW7bXh-_2BzGdijfksvUHZqA_0qlydw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhHs_EJqFB9hZRcB5JGv8rrVQi02fQBiKlpKRsubyhw95_ZGb1VzYHv8UDMKvSODwgl32vczrwhnlqslWQJMfpuZ8UUN_LMVvhxzvb2QfFcmAcV1FUl0Oy07mUR1Faq0eZKHAFE89eWgJMAnoUrRk9RCmLDCzOsIJDcxpPahPv9-7jySTyMNs2Irv1P-1UJO68y05YSivEHV-ZspD8s57X2bhtU-1wuHeBX4NuQm9aNwww6m-hQz24ReOKIQsd-ExK9KVfJ3l7RRcmzAwtO6T08BEve7arm-viKOiaGHnDigzsH0bExNkiP_QXKsbGtmS1dDN86Q-ge7u2tVn7iWXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ls-JUABCqqzWIP_-haOumDcDwtOlQUhhcbK2iiNP2T6RK0Md_I93xaZQ6S09OU13cWxnGY7SaztRRG5JgkeLpL7XLm_0aGiy9aW1sJkD2xaEN5hN3VAwj6EkElqZz4YEYobSslKBTPie5W81EZuZBgA5vTsp_gWs5WKZhTNpFEW2zOAOvAyxj5hU-pC6PfHHkSq0QX6SFSFRFC6wHWZWJr6LD1Ae_JNDO9JqmmC1TgMC4VZFKRNphDjxCzlUA5m1agLFxnXLb8mvi9ElfVCICBBMYl0kxZhj1fkKXH1n87reNBr0KYUKHCsuA6buiqGCn1adod45uScNoVYvaVz7Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRl6v-tmWpq1AQynrQWi3BLwSsvAYJKiOLOpFN8NSnFMCArKpzUdHYMzFHpEE6h9XaQ_3ktr0o74gORJA8zmW-PP0_2XeZ9XnUBxHpG1ClYQqV_qQm2SissQC7IVdTh1OU-iEg8qD0GzJQwPqkfx8QXVTot15EpN3hvrjaPET8Jy9FJ5KxxulxKvB36Rme7yS4NZWAfGtZJ058m3HMMr7nlyTsMaMirvQAxq2jytq8Ldk9Nwl97fKV2KBM3-VjYpzmyOxD-6OFdVe08y1fF9uLFPnLqpoKNzxVUupeQxZGtu7Yuf-07RCueMp9PeVNJQFNZmtC8dwwpWzMRSl4_reA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCHGBQV3PVvldDfH-ihUR2MubVNB7qJ7reo-tkKQF-Y5jA9UAQwxXubrNkrt7SMY3D6yaHNvoOob3MrBsd6vEcdq9WaYNU_ZLTzQ1D5Fl7WeoS6l-ztT9c_RIRnBiu4CWqMWPD_BMwMyo6IIRCW24l5SpAdJs9LB4EAJQm0dcAA282FoOspwR1EvjlFfJN50exNBcFNH-zfT-3J4tAynngZok5CFLHwrwVfbH-6MTMcp-B_t77Db93YZMbiUulFV6szISiR1ajOPnQQrU1Ej_rWt6AfYpIQ9QoHHp5xR2jo8sXIHMhJwsWSvy_7BqlKrEeThav1bfKB9GqZAT5SSjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bo5EwEs4z0Dc4r9awbzu3efzXOf6IB9oKIlkyC6rRAdsnMojXIfNiYTObnPabswpLZgbyIyQ6FF-nq07-9dZOl1IbutFu-cKiJV4J3JBSJAeLQ7sCBiBxf6CNS6w5HIiqBNAaMksk5boJSIkXp0PBEX207saAgq4MQ1FDseO8WcmQ0maJ_70MgJ_aYE52ZNkNlmHkoy4c6tmrDpS73GHCrKVFnkc2u6jtEZpannpF2bkpQmeJ_qGhbMVzxYFDIx5VjEUbdlRH3xecVHIFiEc9SKgHgau2gEVO6-3jMjuoxq3Ges565heSlM3BImffKSVLQ2TUCvNm6W4nu-PXYXyjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaIXPWiKXrdhdSZqWoAyta2Fwv47c58TeQ9-2KTk9Qb7Xv0aSXSZCkWGoccVlQ91UYnWgcDAyfwgZZrdM2OeMFOF3N8wyjEshfm1q05CKZNcWio34Hz21q4rQCzzSUleMXSI_y9rh7NBv_vbFBILLfxdPpohh-_YPe7Y2XXsZRPIg4U2IP6gDrTVxKgqYOgK2FXpkw9MMW0DuOR8UxV8KJTO7tw1FX8IALtNK-9nQAz_X1seujKyNQSM5fItOIAdIfp8cTpEmdAWLdBwBp9ACWUDO14Kez1OUatj36afUnwJIHhQIGNHOTH9zCrr7wU7BOSq_69xvSEaq3zUZCP6nA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wo2jizPGoHfVquhk3CNKYiveCRP7ZQRc606rZEI2bXQD8yDw5zypJAqUMaV5nl2emjBcFPN8V28n3FDyb_InniGxl9X212h_o4cLvvwjK9N-3kNfcbGquHP5cJeUfpiTEKAg8vX8eVF0K87F7DCQW9ePWH5oQgVUkFAxT0dsavE44qNEjNuCq5Uv_ayd_Z1hK5cLWKupPus6shhb7k0f2qt-gt25IcNen6oeSo1rrxxHUPwBohoLIhoNdsroZVzbW4ZWFbk_4SXIEz0gvibkEMlFbDfTCaqPNsqsfQKE1k8gE0scmG7CD2w-knsnw9hIKcNfr8v4m4dhTLYF6R41qA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KMnhQYjQMm3LyPE5F5DY-vLz0HIWewSMGbjQt8Mbo007aBw9SUG7yUXUfyfyvsRtHgxdaIcuilkVCp4_oVeAVwtMVEv-Nukq_QBTOVxdrBKmmB3g5I8iI9f3Ptl1YJSKFhEC_MTUMC8dgFGIU3wUGYBaa7gAFq4nQvntqCQ3oG3wiLvj9ws5U0PDZGIR8-4aAqfq1SbTBLXWupnWOVIdAGP2GA9YCsU-IITFR2jWEu72hLlQzxRyW2ZzniIaBJrfCMsig4wasHwRoJLfcwZ4Njhy3vn7U1QXJwsbjN4bNNbq1ESWThieil4CewS_StfcXA_4J8ipGKXhbWLI3WAM-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rRWmgn_ddpmxSpQXDRVOw95bdyIwGM7FHoBWjA1avHoxLRC389CGPqxMU9V5wAVoU9YIHRfITNuB_N9oScZYj9edXMqZ9ekSIPyml4BjSjB4TilFlaBdlxINwrYC1dh8B2_DGA8cgtzP8kZe5RUNsQInyyLwtEEf-ifFz-azPzen1NEdqh8gM8qOmzKH2VgGdgXGNE322-wgofrsIlSunW_J69yzNLaHYrt5bc_PXsT-7hkMf8gKyfZiPfrm6BoYjAgrm7SfifJVguKcu1jedrVhwq3JvBTf7DUf8aA8h7lExoB0HOwpl90dggXaQmZ-QyfZGwFSIs4-4jJtLcR4rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azYHR7Zn_VSzcm3QFKK01lCINGip_KiGynnFm_Ysw7b_GaCi-12ceJ3BTdTSwo030EuTfRSQ-QWnbDikZZHwehJkCsSnM2QkkEFDCbN13fjKKBpWfMfBoULc2Sp5wEWsi5R5LitPtOtAmmxUzQqNJQX6c0CBDBa8A-LgrZo-IhWDAuL5AAPpiowh6NorEOQboB4tNverBrRc8bocrH2vYJmMOdACE6mkE-wrdEvd_C_wQXDjyPIH0h-HYkdD5MEnhlwKQxu9lFGtXOmWPt-BdLTczVfQ42CG8h9hB6_Y7H60Sm5A5D4OceQ1kSQ-x47hFcCMHcxSml3bPkw-vQEssw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pssh8uS1QK4FeEdlNY9ONIqWFDxYtq3W6luoAlHun-ZnSePamAEoe_9XfObmLaINXlJmASi1UJO6Xj_1kJUUeWPY8Uc3pZ-2O4jcF5ifZY3ZmYoHl_P5LmSuRIhHhes6kZaadfDLppFJcQyC4IXdfm6R9vJ84Z0h-XAjYvDTC4YKpWswU6xs1p10Q3oY5H6YQy1kbMB_4Xuu9Ajd28g2KiCKhiR2yW8vNsHCK_kEvtD8Fl5kbOVm-LCjUopFuhmLZKbpVusprRjAVfPoGAIajo8x_HKxhSdH78C85uWL3MCxTGR1Th9Bwdzb-vza9tu1FraHxOEQwsn4FYJfs8eLoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXzl6v-g4wHh31-1HuEGCS1zYJBEoh9lmHcNkKohlcFzZ0jpfiMWJlJObREnk9vSqwax3N8AdsfC64PpN4jVEdqmDjzCtaJZjUfu7jP5XYE0V9DJEhp87UwGgYSsUHv-l8CDVCljaWUcdTikh0uFxFosa9ur-UwRxayuXgV2ZOMwclAW3Slf5OneCmur9BLZ2ERDUntPWSPlz5D4CWtNWqN_kuz5loD1VMsbEKSz_UR4MBXw3U9QjC74u53LsigJ_cj0RgURY7cMIRWod3XVewvJBvkbpSUILIRJlsirkHVTjN3AjHHCQEHDIoBiunQQf01T5R8POzCO5MywvLMOGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gn35fQPyRSADvtOV7ozTwlxije1xkp6YF5o4eWeGhF1idfbc5aGCpSCqBVA7PmSlcBGggw8bAqfowVnD4u6k_JItjYjbLD7XOstxAu8WQk8_iDeQnHpTRwlLJxtsvYCqU_lUc6n85RDUnsYUqYIuZfJLXihnPKI1MGSkqqSr9ZgscjIyXSa25a9-G1BtI_tb2BQrYpPwBxPcpEwgNNEGcTs3ZE_gF4Wt5FESFosMty3T4q7APs-tUJnYwDonJtTNPwcRjR1spd4KGSiMEpF6FbY3T-ejxV4q0yL7-jsZ0QJNiMQE1Yve-QczbGW7CjgTq-4yojyyVYuIZGJ4W4kzOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shKDZ6St1DX1C_8BnAaIYBYIh_wRvTPOqHbUSygGRuv-da4f0roQKaSIwDpwMn3NSsFq6RrYAmV28ghCeLDr_IO7Lxxbc0-GaNuEpbpNK3JITYlXgUtAoiSR7BFSjtGM3CyoXURLm_D3wLdCFcZXvU-rwVSJVfEHXI4RCJndpWnAniJjovvxthH9X7Ct_DIW4RIVibZ48PUm5ziFlqXIIbHCYku9ML6cxKCBtkey2EcD0L-lf7R324DgjzI-jicx96EbXiOtNhzM2MW74WmB81bIkrJC7PWwljirKBH92N5kEVjNiIFp5gi4Lb5rMhOWnU8jliKt1CjgjJwgqsBN4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXppSrCXuSPSARi8D5mIJNjzTTwmQJdirDwe-qHGhzk4ek-ksDxSufQP0-vOB9mCvKUaUrNy7lymuUhcMoKAgmi1jF5bbQwkR7N4klO1XrBMDIBUJdyEhcgf66b2OF45qZWHoP_VK6OBISGfmotcZn0FYf23lnPIuxr45j4ppYqxH2Sr_LOo2Ekba_953R2Z4c7-wkkjNGMv87Z83IrkZnoMmghR3MYS9j7ORISEYZu5v2Xnky9SzSWYbS-JpvQJ1Bx1tvvNluKN8ujyHL1qkTnfjn-MGSQ51AbmTTgqPfGeMc43veyye8SNogvm1YvY2i7Sja_oE-4LtoHEOlACyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBOrMovgpz0TAaTATyy6VO0N6dMW9f8BCjTLsA26R4xEmok5PPL2dzjJzdVPpqB-7h1xPev86A9-9idO8INPWiWfxoth1IwubBvazfX6GuJnJnD_BZ9udAAPG6-ri5oVvMnRXTXK3gf7hYxdSUB_SrihD4O4qnImpzQkLcC41Z_7lmcFbJRw-wJ-j4QSKcZb6M9R0EkvEUhwiYPH4oLEhVSf-TX2A4aQRmb9-M--gnWp_n0UWHVaB5D7uIgSUDwiFVmoFrwIQd26Hz_GZRecer7UCnWg2n56tWooRrzwI4etxY5274KkOrv7VDdrwc_6McwTb_tXP7602ofolzeNwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxB_4FFX_OofTvA5MCt67YeYZC1jvTTcNR88HSZPg4Nf_Y-16OzIR_QdXcbWr_Jbh7707TDb572jCZq7v808nfsVbQI3cZo_wFb_Ay7hofZN7BZhiyQOMc1NhNRMPYimfmRbiOXFJqBXeaKmTCuf-QqA0b70l-2xyjPuNdn1c4akyTZ3YpMR1Q1S0bTnsJNzsfBpy3Qex-XIrV5eGBO10kiCi3H_WiH1AOkZ2XqHyxCokLbnJD3lAmR8VbJhtwKxKjh1PbY90os4FJbvzcam8_KWuycM5zlrgO8CUvk21w9RLGO9Q6LrJ-89ob4xB_qXAadwtkoVqpfHoZrOW8_Z1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcFBwWBSv5aIwMX0z4UwpoYgeyRhxCcyyliRbxwmLNImYMJeW4lm36IcBIQzmHvyVKOAPEGsQXFm1uy4Mc6gWOxD-MIj592kDLJjw3fRJEBLzmgKQCVC6bTbQtiMDyABcobtpP0K-dx39s-9dFdpzqvSvatskkA2MBGQar2mWMbD-XidbUZsqHfBUEkjEheofJu1XnjG-FmDJynWwCrppUYMWWStY7hDYBULN39gz2XL3fIOqna4t_u6R_y9zR8Wq7KPgj09tFe8sSiC67P2rgosqsB0B_qlxkYTs7FLk7VTVAM5bLNR9eA_vVMUg9qAA4q_-zstlH2rA85auw1evg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUPfgXlirS7YZWOS4TMpAiYuzT6pDwxFnG-nwbeiss4lR48kemEotTgtSH9Qxv-zVo2ndU8fGOFDGjSZQWuhxFos8IqjtE7kS9RSjIv7FbmqEfl4kKSKAo9jJfSJldF5wFfML5R4w9KlnVE4ytX7slDw6YkXxTk-U0Qkfjb7yDD85_j69k4_8Sq29OO7E1PQ-SldueYJBOasumS59nPuGk71xKvawHKfmdhOGUiBEpZ1CdIfXXrcdrdndFBlRWXSf-b6rhW_2yGJ_sR-9TYdOBzairjaS8rgAHW_ce2m7vkRPYGfVY01uNEh317am_PkZPoa4zutbnsbo5d2JB7WfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/koxEsu6eMGlxocmHkY0GVm0fOxJPJPxAo-Hk30piaeWX8X3HGwuWBY440a21Y_mmN_mUYno68ITgAW2YdzfTmFpTz7EU72r51XeqpdDI2pU36QetjFbPMONoc1NIjqDCtS7RLO1x2xGT1wNrpLRMywrwwM6wCv3PypSyBsRIgoWMoHJ1FL8xkfeOIC5H1U5YMy8UJojTQChnvV8dU7GeUli5tOp1n23iaJkKiiYzEppSHDugNBciIeQT223liPfEdi6lxBuT3URewS_-1b9mAFIUZwoX7us57aWe9KdGVmUm_K4tcMjG-a1FXT46cc0RiO75-tbJq-SUnONhjhXJtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEm5Sem9GMhQnqqsbkHjPnh7XKRFJ4IccrTqu7hkAkm-6wzDxOrkiVi-ScRYERT1lAh6Uf4TrDJ81eFL4i57PnoUA3hIruft-snX16qi0y7AgcTcPgAroTOt8yZ7etR1momvo8fU2Itf806dz_7TsCkp4NhR5ZYu3aEnx2F7_pYfXfB_z6pzKIrXOoqhHuW1eOcgwZAeVcYLXGtpJ33y80j5UYQ_boNq4nWYpFZ5Rg5EpZk6Gv306L_2MnhRxLjYBGgf3SJ4lDK0Ab8WC84hZoSNCs56bjePSbOX1T8m7DK4LKQbTL3pzfK-Qe5Ve5_JugJESDcmQl6w91UxzVhjaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkgWQaRe_Wy9JYUXA3CuBOhgIR1rlg6nK_EX6Eo3Wf7CNL1bO7cRuiRMrXMPDD9RpFivVtG5DTV5Rstz1mTqzXMmcLoWWK-jYMhuCpMpAfhsxZ-T44LJhbowdF4VNQsKCIZJbAW1BskWOxTaQZMdwsDXMnAO-FSQBaPFB9KRHXUgk3Ora4UdVi7cks6Edf9PfWnAO0Hq1bzjEmYt_6KccjCMdHQh-XW_9ulSI_Y6d_dAkXguobz02oHr4oyI3CIfiAUMHz3JzsTJVW9pPhct9yv6qEH5UIs_SZB96-wZ5mpYFPIMwFOiAsvrsR_JHBLe0Gwb3jow45_3qUYeOKws1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqNOpereyfltwffQJCqQSWLIhFeSEFHZQo6qEvI3tzDf31bmcWGQYJTLdDizXbrmLqDpRiis-jM8KLiNzdXMOf9ubDnblNfyzlZUjDP_yYqGEk6d-b2JFz4P9ocF-d0TayJ7SU_UFtHiqkrn5co-MAmL_xLxAAgShnk2RAyuc79lXI669Sp7X-UfdFMvVY8TX6URmMOLZRP9lwHgMRhC5YhMBsHVQpGuGk2IcihD3_YbOvTjeuTQcy4FYBo-P4pL22Sl7d9Gcwmtb4Ss0gLsng-pJAmRoh8FYmU0rd4Zt14qrg7JU_eLSB4ayFq2whZomh0G9UNkqfVZyaQuR5DyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZ3MHitIj4N32wC9613oDNbJdCVKIbK92nBwc8pm_cXignleZGIpRRWZbAORI4RVnBYd_yEGdzJFPGEo4RYgHDY5lRn9cXboqcMgqbzEu5vmtQ0Y8Plg0myHj-qBbZwF-MDo0IRt3YzVXik32whg-lOzeNb8ET9OdsvmpmcajF6crIuC9l2W4mkGOg1vBm8RVTH8doqtRnvIKJ16tIZgmrQTA4r3zsqEo0_alw__nxkieyx8PQbzxmnvujPWrijia9j5C6N-M5WUPnv00cQmWKNNUFoZzCdQtE9EJx0XcJQLezXsGjYxMSuE1A5inq44WIR8SmC-mhG4W3FWqLG6NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAXThmedAPEZUHzzbtO38gCz5wfqlFho6XGvPAMmadgF66HBEmlnJFCQJlodWiZYCbNG_ZB_1uwPE_Gt8kzJMZgP2ZQl6WSSLy68gHBln-bqdhSdX-Mgk17adM0rvzYr51oNVsd71OEuXyxHiqVmkvpXq25wgXgSew24q7GnFPodHG6IEpfPslxT2NsMzNP8M_vT7pU0HGysozeRzABcv_myrAdN405dudM5v9QCN1I1t_uwor3LYjeDH5hQHeAplCN7Raens7pa07XzrD06aUEiFYPJE-anNVywCl-V8C1W3Yj0GlnQ8WoFxi2x6ISKWaFwn5kh2SlngiYFXJ8-xA.jpg" alt="photo" loading="lazy"/></div>
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
