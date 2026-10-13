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
<img src="https://cdn4.telesco.pe/file/dI0sFeQixN0T3tl4qaWRCb-kFWlrlvgfrqGKS2j6RHshOR0xWfJ1awNhmTw_8SQ8B95usK9CQSsENZYCU-_j-jB49Qa5zZfxyFZ5uEsVoXLrsb-kREdLkxQfUclp2CmaiLuSYl8BRMWQga9VtddBP4wbQbh9d59LU1IVAkzVFTtDYZX9jx4MPfzAlzcgbN2PiGlkBBv7KoovrbsJx7ic_156_59iF2hL8_kymKXYPsjPSRvw-YMLprmGbYKNyyJUgCmLkXF9wPElYdA5D8Jva1jYodiWPF1E06u5OfjtH1GU0REWSWUeJvHxm5JML7UYulUU0_Vy-5NxsgGJeQsG6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌بازآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 15:51:52</div>
<hr>

<div class="tg-post" id="msg-8085">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O64ny_XRRTzS5AF0fYN9HzLQPyEN565SFRStzqfBzy56Yb09h9EmPhoGAQPPwJrYiw-1aFCJ48p85-2DT0bLXibi90yQZ_8_gPFwQY94s8zLWkLglogL5D53zVHbbyUH0ImY2aqanP0KauaVfbxG5Ts8_iIhlJjQJvsYnNYTpQ90QcsfpLCynO7mWJN2MfpN3WhpIlJtpI5aUA0q3oYOPAnE9GjmjaRLiYPh3YE0m4vi7jiT51FhYnvRruhIl5UtiRLzoODW3KGVogeeKTqGZCohVxxDcIJHHKulitofdyNx6w53L3jpWPwxZb65iqrMxTZrtG9K0nq1VkSFhuMI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎖
• بعضی کاربران مدعی شدن احتمالش هست روی پلن پرو هم جمنای ۴ آرگون دردسترس قرار بگیره ! ...
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 841 · <a href="https://t.me/ArchiveTell/8085" target="_blank">📅 14:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8084">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/8084" target="_blank">📅 23:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8081">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIcw-3ofIy0Hz1OwqP6qM27RXxXcS4IxvmmvJZbgUg3Se9O0obIOWfrWWeR4PYBIpY1jMHDXuneUhH6H3VwBbpNYszSG-7pZgi5x3q8LWbbXbj4Q6ty1oHcfd9a5me5kfRDcLZNNmxMiSMeWNq9rSrCvqg9ArPp70WlpUczYMIv0e4I7_z9s75WU8jV-62jhDJmS699Tf8hU1lpbqTl-qenModI4-5oQRUt4GDeogsQbmZA1fkUmqzbldRyHSo-iwayM9oUMOyidoGVeaTc4el9cuzEOMFOUl1JmX0bUj3QFjZb7KdO4EN3pvJ2OGITokzSKKL4yo-8vk_sr2gzc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک این مدل ها در
Artificial Analysis
منتشر شد
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/8081" target="_blank">📅 21:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8077">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/8077" target="_blank">📅 21:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8076">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY4dQpcGktcr4Kh1SRadvCcLuzpB0B2mGU3P80M0ewJqYoPd-SjaUYpE3VwitjlCh8jJdAImsuuvhdAtujJdoIiGn3cP2dY_LHct5yeyH9yEmFxdWpPJXQLIEALgc0HWaTAz0YIAVRVlpZuBC5ozn01A1VmvEQDoITov8zXARaH1nK0Bw1igZ0la7MrsiyrM_OC1Y4fkbLFHt4YZc1WpgzjANSO-VxKnFFyn5tmYdCVHd_ogeFPJeyLb8VaTSdZcbEn6oTMkrrBjLh620WsoD-tjIootT8igy3Imxc8lwZDzHmdax_xgJVF5MqlGL7Pm_PPcBEZRuXM1KduZuSAzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعب
گیم های جدید
https://tehran.velestudio.com
GTA Farsi
https://gg405-golden-gate-racing.surge.sh
Driving</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/8076" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8075">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/8075" target="_blank">📅 18:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8074">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/8074" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8073">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/8073" target="_blank">📅 22:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8070">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/8070" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8069">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/8069" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8068">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjbAVe_Xl23aBaiaaNngBow3MY-SyJoe3GpyfcPa2fytipS-Shqceb17X3xlGonZPZhNwH731rkbzhHHAn1TyvT7ZdTNYCeUdNRTsHDP5rMHhIpXgPoc_C_Su_pIcktPRUeUgjePNyavS97_p_UJ8psbG9xlwjWaKIsZDnIHNPQP-6QzD8BcG5VK8MlzpHPCx_Sgh8bi4eLQY86HlodpVln0arLZ7YeNZ68XUT-ls4pyOufpIA0P8u_BcPs0uLTZVme9627-i2WK7SPzAHoqibPYlSy0tGLizrPdsuGPErzfayvnRCTVHNgTuhzQcbHvwMnaG-ZcFvLYlO9vg2DPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی GTA 5 کاملا رایگان - نسخه وب
https://gta.deloskiyt.pl/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/8068" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8067">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGGHyYeOinSqsJunlUu07N62jwzmID3PK-VCtqmKPOJMsZWpDYTxfZg2YXvzPywgDAGytWLJQZKZ4MPGuUxFh2BHm3FBetvwRH6US3wPoA9SOvkvOl99VzZfVFofcE1rj6I8x0LTUQ7rVdDSzwq77qkXtnsxUAHU7FrqE8hFfeamYCUaOsn_kV1ECgG-3_qQVhlccKES9Y_9IH7xjfGaTWZWT6Tko4E6f3CjYzPYALx1Y3sojwodFFClBCaYF8FQhc5CGrviodYw5RIbdHzPSDMzatHr9T3043AcztFVmQr6M_ez1gcaZNxuqRan_nOdHJRNJoOH5UBvnMI99w9viQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/8067" target="_blank">📅 10:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8066">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsLicV636FSLkXL3QJnVGlTJCDqY7iWftY4x9u87sRCFnJyMfATrU_wWYxsYzkwNLP6D85GnJijBmYQO-P-rH1RSo_AXLUd_QJC4kx6rfBY83MeCfkTAWTUfRoTvrN72uoYiXYCXWg4bBqVORqjeBB7JQ30auR6Y4bZw0AQGsKYrvo16So--5Xtc4VDcsk3UayRKGnPmuEZjTbaxH18TQ4ri4joxmbA6YUtvA9LqBraLw32fwr_0WrJx7jrZ4AbQUPtCKrPe572nfdbaCYinJHhQRD6liGdx3Foul1kflAyHk1GyYWnYFmbfHH2BYKQ3wiIsquVYqsR_gjT82q8wUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8058">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IzNh1MCz6DHhmdrbldRqD-DIMm6DQU-AIgnsCvO3KYWaCRA3KPzlS4mOL3DOWIzx6E2ADunKgCqelazsk90zRbfwIawL02I7qb8Bq0LmGfiKnjeIZBJiokWau0OGGtNM46iZQYN6oOx5fEOUnQUHi11M_guYoUdZAfwS6LcDDsaeSoiBQgXx43uRQ_TzgXi79c1w-669SVIvx-s7MK4QUEmEj5H321OL_hV8moZfFCY4FclaPI2XFTq1GwYA2SqunCXPwIJM-HSZVoqIjb3JCddrBNDn9Yl_3rg-dn7GQsRXSSBGEKd1u7bRooyBiBHsYrBu9GCVcW27gjvoyz2gSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3F-wg4G6FgZPG_JMNU1wHBKZnzT7GMxaaW5LEfryuGyelmhYYlyRJs_C8-SpllJ17OiPleCX8G3LPwJKPfb8lTVO7fxcaraKgNSQe3U0I9ntsiqFMvwpsPnHZN5rGJkXDGVtlOtQ7sys7nJcdg7O_dMnKQS2pxtxL6FAG2OYrRbPbVbAMS14e_mZYwg3KYOXmVA03Uk9JryVl4O5I9EBVWkjM5StqY3Kwexvr4ZeJztaP9qBnEJeuDzpe1aBmP4KRInD4cXvB2psmvkKekOiDRzF93CSkOWWGkNgXL4faJbfnbkdRFiJQL_7hnInnNd1SeF5NiL5tnUd2zx87hlvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iRStYFRQudxsA3y48SKShlVl3JaEqr4rn0ZXglYdMvFbKUmphdB9vZGfbLwVEkI2b_J40coAu4goFFyTcXyT5RKKmGnx-ghJx-VM80imjafq1kYrsUXrZ_7UchxILDjoiJcE-YwNUcPg0g5fLj9Pd_IzeH1fnrxUCeRLPeY729ScXi7K16Ec6Cz1xp0PVnwhi7BWZGG13Xo7_O-cTa_vDUZxwnPwDrHvEhN9T-iIaxd_dHzpjusqNElD1dy04y_ZwnT9ZlEHv0UdjY3Yk1TvaotgX14EsdT3yStejn1kxKhwmWPIkH4GGMiSgSh3d4VAF_M6qXrTWfOJ93FUICnb-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=a2qzIjI0n2aqqrNmIpGXgbwH_kZKUszSAOArZtGL4lWBIcx2MJyizlFrSq-bywPQxblG5oclqwTuYHz1mU-tkYuxW9Vw1jmz-ep-KPPHeMrK5NGwNKgoJ9p_P__Vyw1L6uNp69WLXeUVxfX2udiRAfz3tvcHxWttltwJxeQ4QluLNEkD176wMuIrRhBOkRhx22gp_KXJpF2vLroBVUmVg8Iqx5jyeqEmiMCn6wvpKHu8iB_JQapI1kGQAdPGl4l5z0K4AdjxqL5tc-MnUleEI5_JhBnhZxSZM66Hx_IgbuiEv6aoPgtRtSyOkZD5IkDT7Zr12HfhJpmn4Ctzcw6mvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=a2qzIjI0n2aqqrNmIpGXgbwH_kZKUszSAOArZtGL4lWBIcx2MJyizlFrSq-bywPQxblG5oclqwTuYHz1mU-tkYuxW9Vw1jmz-ep-KPPHeMrK5NGwNKgoJ9p_P__Vyw1L6uNp69WLXeUVxfX2udiRAfz3tvcHxWttltwJxeQ4QluLNEkD176wMuIrRhBOkRhx22gp_KXJpF2vLroBVUmVg8Iqx5jyeqEmiMCn6wvpKHu8iB_JQapI1kGQAdPGl4l5z0K4AdjxqL5tc-MnUleEI5_JhBnhZxSZM66Hx_IgbuiEv6aoPgtRtSyOkZD5IkDT7Zr12HfhJpmn4Ctzcw6mvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/te8kIWcjAy7tPbhXnO__BTypexQqBxgbLsbGwPDs5c8HR3MtAM_b1CqErD9IjVGEEBEFpvlt1iOLSE7NK8UOXIWh0C8lDajf21IfkDrylP6AjQ0ecf2Kp-9vvxGNeYGiRLfj8XtTTAnCj9sQWirw3ftbZxtJ7uQrHE7I_pMjImH-UoupX4V4agIIP5QKng-0Ssp-UYNYpy-jgsv2W21oRuVAmZ5hGricTTG7sSOiXKPr-SHyP5CSjSPpUUkrpQHY-aC-mv2pPPUWSyPVek0UVPMb2FtKo7VtYeu1JYED_rr1_Y_i832zDxQS_ohPgo2zJfhNgZXWoQP-yQ3jK0H-DA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=Ybr2z7kIezuTG9dWu4SGzt9qA9iodCLXE30E2B5P7n-Z3NJVJ9DeBqkHM3MMC1lwj_wRHpOWfN9ElOkDzyhg9KLNLHWmH2H5UBuFpfc_PSM8qzbbZ0Y_zPfkF2Fa-QjyX8lPFmfqD9TCsM3aOOYtt8m-B2NYJIn5TFODSbjl_AOUb6s0SL9opbmKbRYMbNIChJaLTl2ECX4MVymMec3Mql7NKoqD5BUvzUyskZc-hjYIWPPiSTnKmH7Iau1JyaquP_AGkRdujc4NFuEPTY-h50tNuBfhGKeyihyUQFAWXs_trARPMLEMBts9SMf65ZdqR8u4NYwHBgn8OQTqog7YEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=Ybr2z7kIezuTG9dWu4SGzt9qA9iodCLXE30E2B5P7n-Z3NJVJ9DeBqkHM3MMC1lwj_wRHpOWfN9ElOkDzyhg9KLNLHWmH2H5UBuFpfc_PSM8qzbbZ0Y_zPfkF2Fa-QjyX8lPFmfqD9TCsM3aOOYtt8m-B2NYJIn5TFODSbjl_AOUb6s0SL9opbmKbRYMbNIChJaLTl2ECX4MVymMec3Mql7NKoqD5BUvzUyskZc-hjYIWPPiSTnKmH7Iau1JyaquP_AGkRdujc4NFuEPTY-h50tNuBfhGKeyihyUQFAWXs_trARPMLEMBts9SMf65ZdqR8u4NYwHBgn8OQTqog7YEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxR7zNswNdHxsmKTxSXV_AVP0dXfAJgLdE1uUQH7ZnEnXd_2Jy-7rstYoqxFNZmllSkGJ55kHIJfWVjbKS9J9JSSe12vRRuf9Mt4UuLpVlBNXxgc91K2o69OZ-8HabFsNoEtEUpaoP0rYP8Yrab_eEblleUJ8yW0bL6p1LxPsiVxPMXA-IazbE4c1HjuN8UoJBUc0Wtkwa4Gi-UkPwEEk5vxVsmk0_CJNwu9nuSankXt1PAGUU4BTm418kFTkug78jA8Mxm7aSp19HH7AwtS6dLeexS5DPkBYKMzumP2x8btVJdu2rq62k1t-2BxLhlI3Qr3cKA5zAQwxAayZ6Rb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpOd3mSYZk6Dp4YTl7u_U96EedLJLB4JmVgAFXy0Zxiry43UZFl8d8qCBGALCLRjUyhApzxDgo8kmmhIPZCVY7rlKjrKGV_qbZ19tRnMb4AbrMkbzENIBgL3gex7bzh-tjWc0JV4B8EjypfXonLUy85kkOI_iJb-pHaPG2XyzTDqombs5V0pLgefd0bgELqSv9p6_rneCRGFuGnMK347eEvKepdRS_WwgBtP6dU_PSLrcj8hxwpGQ67HFxUpnb_n-eDMPb9cm_1Z0V2vpWKy7FMLaOhaxaUZMxMg5H46VxauBfev8BID6E1J2RtjTrC6KRIGuePQaX8BW_PpxMIhXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKh2RsNiDIA66uRxcmumEhK6jeIzV2oFG7EuSJyVWQNWW2Rx0YqsQZMHRvP_NPW4eROE-moBpYHPv-2-jk6XsVmgDfObLKnwUFmUm0Wk71cGgl0gv-Kyb2K5ohSh48Mq0av2fhr9uaIi63DVypdt9_vZaf7AP8X8tziCZEQDqhh7rSmDDWTTV9DF5BZHyHBhr376Qra6Yn4QiU5XsTUULEvocujbmduD3NT7xqHwKZPlfuHxo5q4nH2SClXFRuaRtiUm38XhOsZA8VN9anIDYGOTHYm1A-lcSmyCTgmNJ_IKc83JrsS32NRxMnji-0Pts5T-1AMAsMaacA1v2TI91A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lL1Ycc6Pa3OLAh_7b1n5wepHTwj1WnKcK0QREIckKcm9LhA_-wZL75SAiofJ5pk-fhl9VZ6y4HZIqkqzvD1TGwmDKOuWW62ORWc8Efo691PQft2AiR0RlulbTv5DfvN09JycpJCBqiS_gj6OiQ9DoSOzHVXYiDswRqqByydiERVznEz7nW70a-P2D1bakAbU89qFtDzCRM4WJSaxblzvDZ4KcfM8Becxf0yLPQk-N54hNQkNewCHS4xnaoGp2jcjwSKkWV7ZWKRvwR_W0X3lMyj2Pr5igoKT7g1Vcj0k6_knlDrTDTcbyuM0bczISOJUUUk42HbowZpwWYiAvvOSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdchEtqr-W30Q5kSPGw5c85XrzQJUnLDARWyzCnyZlOaWe2WmcZke0mJK8ImMYDIy-BiQlUojSOsnZvPVuQ7FhpNK9exCJ37houQC2OGRixhVF6tzegm-rZlUT60deb8QlcAgjEnqe4CmEbumdWczK8Pz3-tWPEL0rGlJPc2vghLDCnAnW56fyg5gjK5mik_KSnKhgWbozztHbPhUM-pyZYSIWGqPQ7gRcYRhi3QyXooYvzOW5MgAXeZv5PsjZIy99OVdTdxR8rpPoT88pxiL5nBAbpsfseQYIpfOBubUNFgWRQ_A1Gw-vl-VueRkjw2lYQ3JcvKjRcq0VM9vTgx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=QYSnSROw75x3-EVgYfKtqNJsXywqXifWyJQL33QaUoekkEUyFbH4Twwlk74z1byD7u8--3zHkflOnTmHhAaHHZNPscfjU_ixryFAG2WsYJN09Y7pclzWBnM0H71bCdtY0yQbQ4yANMo-v4iGOgL8IVvJXTohLIGYB_QhHDWHoLk0LbgTF3-KC2kSw2ergT0jWKRBsThUhH22D_fGbdL3YcvbbY-4Ujw7NXnzcypXib93-_RePdjrDlkVx3wc02Ioh-Sf6bezYZ8OumBTBtqzmlxSdlwRhMp4z3dkCmum1_P0td5CkUySMYhQiCdgt2C9-MDIsjF2Vv-F7KWI5NJ9Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=QYSnSROw75x3-EVgYfKtqNJsXywqXifWyJQL33QaUoekkEUyFbH4Twwlk74z1byD7u8--3zHkflOnTmHhAaHHZNPscfjU_ixryFAG2WsYJN09Y7pclzWBnM0H71bCdtY0yQbQ4yANMo-v4iGOgL8IVvJXTohLIGYB_QhHDWHoLk0LbgTF3-KC2kSw2ergT0jWKRBsThUhH22D_fGbdL3YcvbbY-4Ujw7NXnzcypXib93-_RePdjrDlkVx3wc02Ioh-Sf6bezYZ8OumBTBtqzmlxSdlwRhMp4z3dkCmum1_P0td5CkUySMYhQiCdgt2C9-MDIsjF2Vv-F7KWI5NJ9Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DngszQ3obIfoGgGebOua2wYaaXuY8EdhStjk8Cpsze23mdauFOTxDA3nXpYhWZ3cpOnNshl5nArfClkJQB7WR3k92RI5ZRnaM5byGVVe_d7lGeoeC2JryPeVEttYg3miP1vM-_tqCUzk5mvogxVZjexUI7urOLI3sGqijajyuUTnQfE6lAe-wUlgTrMDkd8lmPAcwwfDYxed95MPAWRceiGycy-Y1mH4NgcPAd4CjZ9ax4AxgY5qYzv6WE9WD32iRtuIu3-v-NALl4UpR0m6D2W_Gylolnwg65xAUWWxHnWlYe70X0uSXYyEDCkIcVw0kFkAGN9FJlTLG8JGFPObGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMMbD5HQiyLUl8hOXJLRWY8oURUbfpyp6_VKC2uHgPf4r2rlnNAw-dv_736mmmpRVqqzFYidIejXfwEgRiTWcqBF1eJ042sKjCLfJUjLIZ-Bx6efeeBLCNS5c7oCgI9OpLZgo8sgmBSP1oIHfpS4rGaJqH5hAAa7Mo5IWSbQ1dBDgKnS0XHhUmFAiSKcpGia_deP3yJh4NhsUKEyD501VV-xWkmBTdkvL_Vxtw3vumKjdmmAqBYKjsf1PcX_xKELhJH6nCfIpUXzqyEXzwyw29kZp0riuYRtdVj2Rz83wbXw3YkAWjuAWlgDUi9suQBWBaRCX_dZdPLFgtP6Shdrqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXbxDHyo-_PJCHfI4H41fuuc1Yr8ygZl3LziUDA_w74vdw4xNhrEXzVcI6OkJQFGNu1I-ScQbHd5iwJjZc94RoZbmKFXP4GNs90YCKlKPhhT13xUyTFWVRhlFiXBIs5QIugtAI8GYljFbJiXC2M0S03mMySaGWisAseGIJcCdRG8cNS6TfZvjn59CUz9Zq5VngLWlkL6OF72QwG6j6tLdDB5jVlmcgQvcI5HytFc7Bqe6OH8jcBHTpCW6mWZQsBR7KzQeQDGBkQZwuCHoph6Td0FuWwY2VaSpCbSBIaqetbcrSvMjgCo9OED4Qvmn8kwtnWUZ-00zVYnKzyxhSR0Vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=eCBjCVm0QHpNXUVsNnQA3181k21KM_-yxq63ES1emMvwP7cXB5dw77_F09sw54-_SwZcV4wyKcvs6kz_QeksYOSINUHBOvYR4vDaPgn2vbNH2ZCN71MDEF_vK_zC2Y_OroQ_s1yp4_zcIlVF9iUObmGENSiy5p2bHUyBwF0pEPeq4cwAcViBqwzAiZKM08qAFbYHSR62_SMOPX--GI_1GMWVe1oEo3rWqotxh8gxpzIs-dlQ9vVnu4b-c1qi80KStsVpGPDrJx6vCcS6azsCJ8H0MiwUBKCWyYEdyAO-ha8XCm6T-txeNAlf2K7h9YxP6fteMqVPA-RRFiJMyQ9c0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=eCBjCVm0QHpNXUVsNnQA3181k21KM_-yxq63ES1emMvwP7cXB5dw77_F09sw54-_SwZcV4wyKcvs6kz_QeksYOSINUHBOvYR4vDaPgn2vbNH2ZCN71MDEF_vK_zC2Y_OroQ_s1yp4_zcIlVF9iUObmGENSiy5p2bHUyBwF0pEPeq4cwAcViBqwzAiZKM08qAFbYHSR62_SMOPX--GI_1GMWVe1oEo3rWqotxh8gxpzIs-dlQ9vVnu4b-c1qi80KStsVpGPDrJx6vCcS6azsCJ8H0MiwUBKCWyYEdyAO-ha8XCm6T-txeNAlf2K7h9YxP6fteMqVPA-RRFiJMyQ9c0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4zbaKIEQy0l0ZTxnI9IL33gD5nkAf4xqP_FShI2CgLVFJzJvxdzXf8_OKSffbPHap_OKfaUldHsLkKAr0lxn0ydFjGbw0iZnuEzS7SiUH7X0jVACSLPJDFB22hla4hwnYWIkF4GmzAxzFhSY5sPO-UsF2y7W7_-2eo0dP8ATDbWJfz3i-CO-kM8uRBKK0TcG09BIuZJZDDQaSuiGBNTXgvZDJuakh8Z7Qu_N8xV5s2Ap6MRAKETSsJY_LRvbIkYOeiETp2iiddDYNDt43utfewXPA_U0rWNtmJf9V2iAtzj_DJdwo48q1wlw1NS2e4GNlnLkFzI93t0Ajc2zWmiCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ssBkq9n-LgGZf_GjKRPf9riYPrRiN6BSFwo8xB5WUMMVGJ-H9-yTF0CrmFsaD8cscSHdoy1eajXwF8mvw6PIPoOlnEA9HzKPBqdn2ogrxeq_-VnRL6qYFu5aSYTMpapHmYCQxzsDc1fqbpbahOgPYNIi6hoPFkSpIKXzX_7I0aJULUYyTIfA-1DLtk78lycII1lY4fTzWx7OM8qi1Nvu_x9paXGD7UgA-WgbORuFQzG5Ku0POuEoROVfUKOxwd88c8L_yewI_8hNskTeddlzJ_EU1JMz9WSJln-jVBF99aIKyAUJL5cw5DDFiHDqOjxhzVse_bW5YzUsotlT92DlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dh68HXkdXP5UApq7aCvXCXTAEKt6digAP-UEkSUzoAD8NF0gfknZ3bfsux1Hu_Y_XPTTYkJpa8LLNhygBPurGUxfySZM2pCaYAVFdwNhPlkxu_s0mLsO9hlnEqux9EFPUf_6ULqceyzOyHWf6XxzhhAmQGV6movL4DQd0NMp4ufGR1Z-0tMA1PJ-Yv39_vRacB2kFIZHabAVFIzPJhgtc5rZ9udEeV382oeQYJckLm9-axusv430uJf3459uW1t6UXfASrn_L7BKi9ZyQoMTjmy7BlN-rJ3yCP-eK7GX4RakdkG1jiHiXGHTxbwfsJHlJ8Nn6jUqnoZ-lq6U9gqj6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhCot4ZlZ5_WTIObCTKaVYyliZiMUQugDENBZQggfiVgqh50siASqdUvyOmV8zPGHDGaA43XqpVo4bSuVeydoJjMPGuHBG7OQHkP81PFbptnQ_5EXq2bJQSydbOiF0xLOcDPpW0bIQ9zClu454o71yk88VaojpI_b3yHwYFOKpg5TroHClhCioKFihWABzbW1NkxitcbisxvNAdjNZ3Bjk8qYiNu6p6v75P2EUSjtJLp-xL-748dQ_if_3AhMs9DkYNJ21izXotJGxe2xriEOvszeyFwVggih2L6Pu67cXNaLklWaEPwguXEFFqULMiK0WsHWjw7FFLfUyHhoIn_oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Atv5NhWw_sRmprQwUH6FGNyokSzwekpWPIQm2JYRlMtRcAdUR2YaxZAdVsWelTd4r0HjnwHYleE_E6_XbhwKBDlpaGQBYzuvnzVOvgOC7LkocPMtU1fe2Q80QTxY7tKaDeJgOX7i82jywz52HFVfQHMcEDUxIjHOH2Ya1uqXYZTukqEKpC7MglV46SeK9AkQGKT-HH2jSP8yja0W27I7vOKM7u6JuFJu9ICmsOVhWzmxDh4jkqE6nqIecYbM5AfBPnhU9u9mYGncRSEt2eLwwusgynOBX6PwbqpxRVzaNpHh-AGfV7k3FX1CSdRYtuFDrWp3G3OGeQ_XU-k94b9vvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dj4BVaZXt6I9TlQ5YWju9KR07k9JJ2GTVi3_eyzgG2TTW_QFbyW1ItWM5sGyr6EmdnnaZXaTYfCa_gLC-7wmuOdHPsDpen17F_Bam8TyAPTqkEQxRlndz0XEW4l4JFXkHk6WINivq181FcoQ8b32vC0ZfKTWDjrcmcHyb5Qpa8AlyznWFY-uNniOzifokQ1wIiPn2IhZiD8p0LqZ0FtvSHwkdfe7GN-5GtFYX0cO_RailwDm-BC1Gk5QMaPkDNZb0LYnVXy9cy6lLyx-BRIjr42mW-JhSJtet31kZPZSUmSo8IeocZyLvyKAF27aqx2pWXZsT2OlTQ2hIzFBSv2lUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CywS45HXzFZXTrep6cnBB05iSuDpgCiQRjCGrgXgcmcHGUtohyfHOcfryebPp1LnJyKQUXOQprW475XHHo7TqFkxgjhgE3eBDrYEsyInJmhgRiqJ_cXRfWEozyRAVvLoVP3NL7WXQl2MA5JDHyiTXDTyU4UnBl1uTpnan1t4G1tik5GTVJ_nmdC_Xthm7VrwLA0zbS5P1Ol-XYgNbeS-64gXSHOLPyyQCE9bwgvRiPOVkeqShQ_rKLbfpmAlmU9j_CwN6gSPI4xnap29NwobOfg5JLiGWpV64RXZ_dR2V2Q4NSqu5XgBcGqX4SA85uJTkFm5tBBOBOtrfyfGOff7Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1H_9nnjSs3rIfwjnTSRqv6V9DEk8JQ7RsDAC8USCglI9mCQDwamSxXelynpoH84hDgxQoPyWnBsa4EbLReuX7vKIBC5TanDKg2GIct7bWqE8RVfopeFLCw0npyVjNjZp4uAamkfQpZ8l0YB1S0bT9_rZpZG8iRPL1Z5gfXkIifQRTUVSO-i5JjFjr_JIYGIWe5DNmSjAT4UrUzhRJns6YmE5tqjVOIfNfA-XffF1HII2LI7GCcCWp8ESEb-zWxaREuYaix5HIg3gEHz6lD-NqhtgK-iy-UuDvIButhfqxM-pbQVf56mHHikzFr_MVpP9ruREGulSKmckIlmr9GrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tjCX0kEAiSxFRjfcWw4_-gDf4GD7Odsc2FUXe-r2xTmgCweDuUL9GkCVBE1SZVQPismkvpbVackQtVIN_koFL9kojy-UtetSnG4B5tfzaP-iu01kSDgNXxAKTGlWJsDgMm6Xa25zWXw19P7T2kWRRY9BzPO8Ryzw5eyqG-t48w4kzT_bUFrq0y_oRE-EGP_PGpefwTKDYcaZoXF_yYVmIa2CElZF1gn0FCk3vucdCqLVfu84yCijS4tAnpZCPqnJIY5-wMUqYG7HeP3of7d2i_3InZJuN2pnO8uWOlR8F1i6m8TiG_-6heycRbm-Tsp5Vb4mtK-reor0ORPN9Gu0gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_TSI7kVaIg0Z1v0xAdLtJQe6KyBHmm8gGEbmudX506i-2zymEiJM7mr2QREnmEgttig0nm_kEGscPGDeR_-aQDbgTjuI-lehlekxjwIX5NJlZNADAkrjI7nbAMGYOI48lnOEJXTEZCdrrocRogrTZBWXFjT8O_f3RnMBSTHV3D4dssB9ATKlYvjsO49xv7L0qzWwV5xaad1u2bN181w4xY7nzLpyuBRmnOJototH-kSY06EjVvELplbA1-GqIH2nW7DGdwZAmxGg1e5o9ucm7sGH8Vbzt6OwwX06cyFFPDgfYvy1unKhyiA4WMwxp7WPlvQBWD1yBDp9FUaWOIzhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkmcAA1GZgo8qjoVBstWPKVC2a5Rq_W8yREdiT6KqpFPMWJE6DaV13jg-16sMN6-wr_TIocqmlcaoBpYUv9Ol9fEw4xCBAudFx6R9r1B_JptHyl-WMXLxDCHzlVy5OxiHREdJUR3q-lPt45mWiI8DhX400mQSPMl0Za062f88MyxWMIgAiV5_2QdU_ICiYsCQ8IjBQYUCGKypgnB6hx_anUnTw8L-iujVR6QXHWtFrwimztFuOjsI6zSaqsSaklNgViL_JTy9cBg1A40Kv3o7E7I0yQ6ytI4XxeMPNKeedT3-Ald5aL1ggGRh15yn1RC0AwzMsD7VUvxUyMjPTWEXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFtREDeCxVW2baU9Dr6Dk1Z-GgDVejDrfVazhKlse7UWxl8YQw9-dm6eAaJva-iWLQvbrEGe66FwYu8bp1MElXAG0x7iZa8Ezb6RXrym75ReJ3V19RUNenZNdgtKBmhr6Xr0vnE16B4lA4pnmgXa4zfN3ZRuuOhttWGfLrH3zUD0ZfGBchBYyONssR8rcPulTili1BWw6DDesiLdV_Fo-SkIzNmjzi7XWgwUBG39iME3DeGoHQkVVusvxlBmwog9cSUsXvU3PXQl4xk1iJvBNCqftGjASadvJjRqGOdvGeNq5I2p6bV6FfMRCZj28_N4-ZVX-QvfZKvQ4Ic5BuJ2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e8xP_zX-F5fxQK4MLshrfJWO231CIcbPGrHVPNBLYYKE6mVOX-Qi6Q4CE0t3Kw_XnuMEAc4wRZqdjXA3yMYQr1GWqN_c79sq5HBSOy0MD9Y9u73M1JwMCt2UDeNy0PEgRNcj1xLlkj8WGd3L6mS2RmgtF_PkrzGeCakK47BiqsbvDsP-4bGHw6Y1x4Aq4PiSxZ6-vzIz_rVP2V1hvpHip63P8SNCbro9jhHtYNAftktfA_wRwyG2zUyiUXKmzaRCAJn3R8VBrQ6ou3h4RDFLxOI4UIxdn4X_N7WRpj77GNGoG_HmUyWKQpB9DvdRI9IJ8EKnprI5Ym5Pam9Ocix57Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnYJLmengt49H9qztem1fI4QTyG01igs0QYnKYFDY7ppiH5Q8jRhBPTAayp1qRBHh0tI3WAiWS70EgX-knWph4M3esOuS_LSyWmfKQioRlbOZ8V-38ND7p9GzIco-jMzOxTGVJ6Vs3779i7UqrZiA0GdDDyKNthXKqviwGdTSI66D0mO_RMji7mRZO57PAlPedxrESFaSIsJw4YYEv7fPuuUmU4ogHuY9MeJIEcd9CNEaAbOYilCYxiEInkNwpYHmwksv6gHq4I93RKyniDGH2hl_uKUEuKqKW61ESRnbu9FlXKbifSYrMP4lekR6H1R3txMqjq8S4z0seEzYA2iiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=fjrEzlIJpuRtRKeDub2TR4vxpwSXWZBkEB4rWykh71S7zP-dygG-KNoskIP6cEteG1hHuOg0gyAgIMYtoz-MhkulITC9qRvD7a-K57GDGNNh87lOklSUgwKxRk7lYEx8--I7zSc9Mwo-EvsC6cIqkKEfzUgJYIZGdfPWKhek8OCp355CNI7QBo_LziH9678pnGYsCHGzK3MSqV5-M3bkLWLVp66XkweOuGlqGU5zNAXfWL2hzez8Au5p5q9eUe2wnsWswnp-6noO60BxFKyQg3d6R5zjj8rPE_fFdihHuGaHNeSNaqzFeED6mbPQ09HpXsQtI6OSWGG0iBtUwS1mTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=fjrEzlIJpuRtRKeDub2TR4vxpwSXWZBkEB4rWykh71S7zP-dygG-KNoskIP6cEteG1hHuOg0gyAgIMYtoz-MhkulITC9qRvD7a-K57GDGNNh87lOklSUgwKxRk7lYEx8--I7zSc9Mwo-EvsC6cIqkKEfzUgJYIZGdfPWKhek8OCp355CNI7QBo_LziH9678pnGYsCHGzK3MSqV5-M3bkLWLVp66XkweOuGlqGU5zNAXfWL2hzez8Au5p5q9eUe2wnsWswnp-6noO60BxFKyQg3d6R5zjj8rPE_fFdihHuGaHNeSNaqzFeED6mbPQ09HpXsQtI6OSWGG0iBtUwS1mTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-TQdVr6LYTs9N2v3B8pwhOtLkViN5rYLG5oRjPNthATOnxpE-vfN2JUk5taKLB65mdDxDi0Re-5XJh6MFWhZAmb-Zv06e0Anws21w3I6pN3c5ONRWJxrHxlMKxlQb5gKiWjRXEBxg4fQLs8eQmjOlEsW2eVeDwAZ5lJzjBQ5gRoQcOfCLzvXllgGxxjeXD3Nc3rTesuFossoqheydenhsIaCwxfXiBZsNDdtg4Rw0xyBsGwPVsLtokwkLENgeBQAJUdjUIx4OOAVIm99ub9fAZB7odHWTXoPkBnhm2hx9l5xL3aBtS06LaKE0p9YKMA7EmfEJ8baWFr3iEhkb_lww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HX5sVGuSR2aACeewnTiFOaAFnf3ONfNegmMKSoTYkI4iRs9JA6jYUjE1T9dNH0w5gWatXUcOsz_3onFhkzj1md-IKMOZFEmiF98Jg_wsivdOiz9PJxYb9oV2DRMP091Uj8gLM2ZAdFe5u9K_LsCkmdpo_5slhvvetLQGHnV8Iw5Ygivt5gAdcldu6PfQKSkp3M5zQlx-fm20V9iFwR5o0W5pXXNDSiX_QD5YtaB2buUhG0S-LQHBmY0afEIGtjJAloeSpLX3W4zAsqGjsV3H5rzRGWRMnza0UNVPjHl8939Tn240F-De0Z0y08I1Be-tcOypMao10yrOpld8JiEQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dIgYg5ieetQO9LqCc62spbRBmsKXKEDZY566uqX0yZYQHgA1mI3gCFPbngVOQYJ9Y1ff8TM8ZBP7AILfQmhZQiP41KFMs8fIJnldjsQtVUo1QlOkirTYI-kcYut-hVeMxnMp1IigeiiIACPc4Db2JKV4Xq3puQuWn440TtIdkrYE9-mGZfHmYWJO_KmqnSVLWzs5pXkaRWiaNDT5zc-7ANOkY5DyVuo5WbQP4abUNL2EBGD-Koxfq4tOs_k3Z7N2ob6k-5T2M_TZqX4oWvsmk9fXZrxt1uuuFZKyk-V0nK5EhZzppYzgT4NKwrmigdykQIbU6h-BJX3ePFQ_cT2_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzqL7SuypSBfamGAZdQ5roNQmYAUS_irdE6UhDwNTUBi4cVjJhA46j4THJ26j1a1DKNq3uH7jG7ElJNnFdkQxCbsbosnZTvSJALiidkTl64u_jK5luVnx-5YNamQyz5Y_cGI7L5Nuck1u1C6bvTnCXoCa2B_TH08izzGdT6R4pujZaETrSBjgVvdtSngDfMuEkTQOYtygzvUByxWXTB8VFA8DTt9oCurkqlwWCJbbO-p6I9kk6EQ2A8Ixl4ihmml2vEAhHOGYk560OyBRE0HHJtm_MLs0t_C4u8U-v4c7uDMuIo_6pW9xdU2aoxC2qqMmVOOxuzKDc5yi2hHQiTDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0MpdzHXDLSPZ6E_Q4Z5KQFyb8HOmc0NfbV6YVSvZvDGXWmtXr45UhUXGmNXSpsRfbyT267AyLOx7_ViTtrvu6CBBVOaYJi2RYOTIRl3H1m22Gnh7xf58LfUxuXs10lwnlOYCh6wxB6K2thlo2Fu1c8VQOeTBuWYy6DI9uz8aY2_NVgyf2qkr6-6L-UAzFBN6anjNIFCDTH5vKNhYyhzmffy_PuH2XBa0VM41L8JUAmoHn95VfHvIqtcrJ4i59qzrAG7aihNeM_bddi5PwKk73OHkKJZoBnG8o5evpgoeakx-9GzBG2GH5RaNgwuAmbCR13LXfBr7ZbxbZ3bWZh2Bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEyOft5wD5LFj_HDhW7pFnr2FSnyJM7qnHQ_SGfVf-M5VKEx6AMHFO8D6jWkMlcAZyfCF1hsSbTvEPnTZAXnX3_FDMlBmT8iFSf-KBupIaJKo0FXVNhm40wVB9tFSNlSr91HnAyEtYU5FaL1UVsW7_KzkdaED8n7zL0OW-NOla5eO9gY7egVkUQQFR17iR989KYJQot2-YK0OENs2WDWMfxkCWRX8SCQfONawoFuTUqDPlCAOzPn_8BhW8MVqYxvAnyphmR4J86p8wR-2zL3Kf8-_VjslnoX8IPgWeTmi_iMVR3d0F22NG9Ev3-CxUxRNfWS_Gg65elARPc6gU-IiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UnbDik_nqT68K1oVUd7ooDm5Htc0WIPUqTVF4BP5m7LvcADc3A6vsPNnWLwEknbLw4VaCGCd-ymEGsrOohdcNVnKY1fqEwNratZw5dsM2_EGf5cQC5ORvBbBhb2oeKWv3COx-gDjTH7IFYY-9MFVV8U5KcLnVkQ6G1Wu9bxesaDTD2lZMEs73-r4h4vVLlyFzmt5WM2hLXxGjcShFFeaGbaBTCSFmkP7YPckoN3GnNLgaCa1gQUob1t5F7WHlb0kFiSP6pNMC_EAT84a3HP2ZPFI6Q6K8--UkZ2yLeGqy3rrfAfl5UcNhh3RZMJask9HOTeI_P0TVS4RkzemRr1XxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IfnbenlTNb6UKUVbNS51JpnQOYTmYAwoDGbqpn0o854zZPnTb0C6qoEuROZTdmGFYPt367dPdCOch3rB5PadFHDG8gTgjlw40hHtbAqdNppEnLP6iyJIODh6Pm_nsxiPNr68cTz3IC4Ne5gpgAL9YkkqaKJlt_e4Hkrvk0kltDcS0jO5Rwe1uOkVEl2k6HFKzHN0HUb19nkGYX_BQzvIYYDr4teSPSPEhfj1z2w5UjnRhEdgu7pPyC_bSqu3bqkqwJ8GfIZTWSmHJmx6R_zF-tg2URK4gblbSlUTbi-piwjaK77apMWXbL8hfNd32wkSw8Ol6YwwnPomWQoNBDFkQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bfr51hZePq6rKSBd0WM0TZ_YoVx_YPHfncbiky8ZPvftbF1CN2jaR8LCrRZosXW90sYc17BvikJMGjlsmgJYWxJMMHFoBfMchR6CAjLkaGAcsWY8__kfM0LztQs6G0-rxAZYB6NEomUbNNiVI0YBLLCRMr39Mq7eYMRItTH-4yIui5Xr9r6Yh4Ge48vPD_uKiNC_l-6LInHd0Hb4C45oMA7sHUlf32RC4bjyk3dkEDa3gIjvg9rU_kMmfK3LLP02bTkcjUxJxdUFWt2u3PNOGCeopeGqi8a_9iVc3_nARZgps6oq_kBNt0XvnBlKopYgr7UT_vVJq8eOnjYWeXL_xQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
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
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2tpMSoHV3wDNWxh8DsurKNSnLZjZk8tzsiCeiYCMf8crsP_7-d2TvvQBKxY0dHwU6SiMCQ5YygiZx-RTblc6xEU6njtCzN4hOZspExUOfUsmnwB918JIq7IiEgS8uCn7BCU7r-NVHrBgWZ365U5vNlDfBP3vl388JMMoJw-xtlSDbdmGFYAnUBDEujy1VsETGwAHXx7Y3_ySRrX_tkl11VjdhbXfVx46TVd1xkf11F-2tPlD-1WDrFYf204T2GqV3i2HrtVG4skF_uIDIp5v1rBv-Ohca6U4u5feCyXMziq-L0WuJjMmmN1sAFVafo3uCFRDWAjrn9ATgviS5rSJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETzleh89vs_xm9CgT1KQLovC1StDvHJzh9qUabWQBt9LbA22ymQbIzi38YyIRUN0U64W0IdkTs3vTyVv5dh-gLUTfNHqIhsb3sQwkXcmae_TWaYHtknC5GYCMYI5WI3mmouIV7Dlc2wpOBPlyfjfYLot_MbBjnwO1QdfP5b0xYDA-5BruNcSn-DfAHULu8FkdoDxVRbKNnwjCwi7lRepHNdTUXK64ZHsGhDykBCWLhVpxyTmevkQTzV6PkgYWkSL0rLZWq6_WXubogg0Dq3qFXIEVuOxSc20aza7sooGt2scN2eHlVYg9AqTMsYMg44BfccWKmDhygEV42yMOyuEYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tau96g2L2ZxvDH8xn63IUnokpFGVyT1qEaqUdwjmTTpEwBxvtbuwIUh-pypv-d-6BnqcFDzPyIK9gGbLxYj7RoXW8LSfl9UwCjUgmUL0YiAzWpij4cU2dQpvVStksUurazFvUCX_O9-wII2sw_I4u9DE3lhq_eSfkdBJyp9CHB7R6_8FnYM7EQxDgDw_cXzQjp8EP1zZUcBhAPHrpsmxKyiuNskNCVLzpbLkHimm2PxLUbA0X7PjEq9-jnuvi-lm_0jdAu2xmi7vQO8q4_CE2c2NOkxnX9wR_0nrvGD2rAP0OF-Ju8Wwbb2LegJcJUCljnUJxAiL0M_pQupFIvPRnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA8bpXGGal8J_h8vHBso7H2uxIu9KgSjxwHczlAgjCoOEzJDO-bhpCpxux3kmW0WIuOe7ABlYuj4K6CupbJYfc4Dg5gvN6JIaiCkMdvf_inY9Wm1ICsz-TqzMA8sbydM_3DwlIeaP8K_wRkABBwO9e9dXIuRo5XoDwJwDU1lXAXOdGGc6iV5aUWIqKRx7fpmfhwJQbssg95zxb98EpbIwpA78zPH5FrRNiilf5kzPlTzoRDFRf-46d8-238s7pexR9K-pfSRE6d4yL6Dz5bwTLpmGRMpzaq2XwlWcX05t_1c5t6pkO67JdC1gsStKYH-vbCRP8qeZ3LOqJsmOQ_NFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZCF8uFH7TYkeuTWTOL0XPAgXklFQZCxoX4lQMfg7-6Ym9jYD4TvBcU5rrl2PEiRZRDlL7EDQZmNyE2sKXfAcd0LbWE1QurT08G0JyG_lAwwR6xmzhr1Q5f-C3drrHNg6b4ut2tV4pAKeAaR9OHrUkXZyzPIhjBQvm5zppaql6KtvBj16-WEz6LvVmd9yUSGgsby4Ael5fUXopRMuv29kKJjOybwdctLGvLVxReFsUpVcAYcPn5bSgZvGLpcnGc-xowlCUNW3dkL2goQapqzhoNhoGwEHzAI-N3j9dUEgHuLkanxp-UsG5U3K4fkmOoeW8JJ_CsOm8XvTJG4JjyUpNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-364cxCave_yzHcv_GSyBV0pBY0h4Dud9eIuraGW4NmItuzmQxig34dg3Q3YStNtXc4xhqnyFQ_eHNIuRp11dnsaiNPggYmw6yraKfSA5u0TBL2tAK_nTZAEWanYz0eRJt9yE6ulIYurTm_PM65-4gWiNrumnwnusZYMXZ3bwXRcN048LZyt5yw-0LtAJE9hs-9Zrdyn7cgQEa28YKg1sa2bKfX_sZScAcYobAsy-c3Y3fMDqccTtNY7Cc9XFBL7LEIpFTFHyxeOr0kEBM_DB3GzroSuKkomPdscUOTMPHfEMErXMy1BO62I02Xkf2EY4SIenml_674iYFZ0BavpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMnlg4jgF3Ecy4LxUl-q3PzKlAVS2r7t49VvgtSbaFFdtMZeA50GW9OreBAWFfGSaHLBGGb5PWSc-gQKV1LA2KNU1-dVjqOBOpMWNhTw3anQE5zrUEmx_if0vvb1y5lnEw3_TbO1MBY9RWsw8t6-qTLRVk30pPbNYfKyGkq1yh6W5TI6sapjm3CQgaiwMN9ciXZm8f4wok68nFmuZXNbvfuI6AeTim2C33wDziek8b3sAkZ4utjxKnO2P0VA2zuCTZoBqpdn-fh6Uihd-j9lkd_ql8jvq5zPHsHi-xImAN5SPU3E5Stu6eHe-GvjhGOYXrwUCqRy_d58MwAN87Luig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjlA24k7_gnImbMuIvH0a0yGR9WxmLmaBbPdoovu_TKMyNrXk8p04tMoAOpivrA5QpFmMUepQnTwSgwx-vAQ3t33CC0VOYCCmgud3HBSyvqLGmDXQmwdBWsNIAfZFxPD-9PfOC3TFh2c_Og9Xz2mPPRVN2DUc0xZ8QxeSyjfzCbk2vQYFKgE76_s9cgGku8kbKgax_tiDf-s-pJx8o7_u9Nb-A4gpahSkt_Ljjc_1DCVOgzE1ijtOlGghAjsMUMvzmAN6U5n6hfky8zX2IvgTee4BsZmRH2khaMUra89jS9CyoSu5awDjym04PifiugTAj4OINikusrIbfBWOZvNVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO76WvR2ILDA7WE5tIh6tK9JHOITuazFvLN4efngBvV0V7zrNtxhNGBCOgIMaX0vwQVKCtKmMHIpAbyjlRUyj7jFgvxgTKFpceUlNMmR4kadVfJFtyNYFq6L-_K-LBKCyX7Owm0FbE-qHD2H7e9vH0iiHF73a-jZwHqfw5-F0z_JBrBhWjr_v5ROV_PKF4ddljUrFWYa-pi35OToSpGdSZLgDybErxZoryQm9i_fmzbL55XW7UAwoIwQLtB353bnQ7zAjHX0QeqKHFd_J9MOE8Tfa96LqAcm2vDKzawr3zA69rvPdPNv65FR41luhK8jhCqE943lq1CNPlQm_e2hfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfOpix1-K3R0vC-g0WKZ8GP0Xa4QJ2TNLCaoIcpmPpX8igO0TpjqqgFlO3uXTOJ_rsS1UL6GvaRieC0Or4gpMkAQjPL_VIqciXK_Up3npMKl4Ht9QDAyxUHogWlarfKsB11GjBCDvrLoqFBH4hqKLvKWpFRstUr8s0dHDdo1trxnf2KJKAVVJFKegShAXoSzzcfjXjRBMkCT2IoVpa5zyyVZPBcGOB-2Ft2ylQDA_Q-DLm8HiXbBpO8iAc-2RXDSXC7pLKt0fK5dnpeGYoq6vCtKTRT3QmYcUEzbTvACDb8x6JVQfhfWAcnUKPiPUJRFw7SOk9TvcDoSP-ZLxGmxBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g6CeCyzl4GjA3gM4fllfw0nc5hS36_LsQctBKN4NxccKbxdVNFisHPPAl-Kzp-gaJRmEBvqvaWyFxKrEwQLWsxkY_PQNGABCnD0QvMG_qd-6S-OocSmeCjdzQrH5lKnG82P1ZP1H9A43PqPw50Ke6hmTuzOgzPWq1cov10Yq9FgKJQLM5_dgkvXcAyxGMGYwz2wEi4-cZpFRChfUBf1_nUFb8kT444A-nD0sAt824T2bNSpENZbcFIf6hYMUiPkn2BqMl-G4sBlwrA-MUBfBxmIzia0QxZx_mOT7GTpQgYFD3PDCNLg8f0fnNQUwbl4Z-CKiF0U67sE2X1CNg4Lu9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bzlnBFjtOYaQGoJs0t_B7oUikT9L6MqBF9Ldy03v1BjxsdHaOejSNXGy5_ItopjNzi34NqwEHdCpICx8NIeK7pU6hVXLJYJhev9tlWQXpY188pCEUK-w7_Uu1QE1UVhyia4uJ2oaA56_KspjrM8VAMh-wgnBl1msazH_raxwgjnwI5bxrGkmcwHPd7S2J0I-8OHWJyKpChL7gEc8Z_IwWHUaQucQLoMDMkSLaiPNljRZTV6Ol4uKK3FGen7ale3mLsWVjRBIKXSWnm9Oub-TVaZTjh8rcCCJeq_hu5qNnQgbHXIiKMp0RuvHLSzeYzjozvysIYknz26s9GvS4dDW1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSRRhDoIOYaGR85QM_Mo_xgzQBfDWOpFUtmA0mcQ0Phn12JqeEunH5bpy5ZtAy7kf_enhIxBNIv1oxnVAqHWr9QaSIt37L-6_i8jkSRuIAL1jQqeGf5M4AdfebjyNwt4ULxpbkuHmwQsJXt_3n1hBC50Op7PF24aU53OMjaCa1Rs-t_s6nxuSOHegkrFELxqEBncUHLz_7QSvk6vBsbYPpfmtLUF5s9Z5DbhMBmg2ohT9ihbs7iYLQJs1599_onKcgDYk3OS3Rr8x2lDXO1GCjeAwNL8IyHDqBshE_nNJn0_Jc8C3Yvrhl8ANU2baE0mh0PMh5KIxBwYfu02X1mw6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc4EVbAZcYB9EtmxvnO8aLDnCSH9eRSd17EfQ78Nf6Usv_kvFlWY4F2hERsFFtUN8EMUrkbHToC71RAVoCUKLmbWx7ypWqhtloFTSIt6yxNTS9Fu4nzKcAu6-K3sM3mr1Gz3-Xzw7OvF5No4A0tPrsm_NhOROCffuba8oD5HxMmZrKAihcIjYikiwhUR67ER71oAOGrg4ebPNY_OMIDZmIBD0c6UYx0ZuugGWgPxNGhZSzBs0H7gZjKtRdLuPJimtnC7RwvWzddwwzSmkmjS4ACU_LMSyNdjcnNTpTeRg12wZSmGGOmZE506L8Rkkzi9uaQnVjTH38Xg6gP2-KHmUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ow_EMS7R2XJelNOrQWgEz2foMpy6RG9kACRUu-FGbVKMnWAtpoWYuWNMmyxMyPimNMUimKBjUDYHGLWoV1OjMxsdp4nmg-ATmCjmwuqtArQqHZontu6vTmIDIsjlBvr6woOoZjhdBjg-dGKe_g2Q9BGPml6t6vbAtAArSQWTwX7venUfojra-DCZ-U3QgE0Ulvz6UmiMMjdmbQjUAaJng0rM_hP07kIms0Jf7XgdwYEYLx98DF77q8TRhPCm6gg_xIGowhoYIDQlnUKf516hN1nE9mGe2WMkmEyTXZDFwqZap_VC0DmVzNW8SRKPluV2vtPeVnAK2jd6NS7J-78N2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5D-1U18cckc_ILYFFBdaUZEqvT6_97vQJKRBJTTz0Gq_YVmn7M6vJ81YeJ6jjasneaCe9ho4rwrDaPgnzdOgkbLa6svfCzTBtpGR3fTwX72Lddy_zifWW5Dl2NNToMyA4pYiS0cwvQXqlFs0s68KU1c7hDm3BbSmEeyi-TOKWWbQj4PZbWU6GSpp-ju6ay7FYPcxb73Z-PyWBhWpfwyuNYQhUGOPsLxM73U4eIyia51BgJRWSP6-1OV_bFoSRPIR-D2fAuN50RLEDg1D6PT_pfxViAkcXXaIIXmFvt08ADWGOVcr8COKsmdPmfblOsg2CfCxAi5WtLYei5a3ZUuCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKmGEjDRnjmWYow3Csx9qUkBxbU18oPaAY9GhDO_wBJiL2U4ikl9o93CRE1wNRyLqiCJLGTi87X3h6u-p722i7KUm_L26aFTSRdtFankPGFNg4aNBKaUFjEN4B0VEuSNNyu3E4qBXroS2vX6tbZp-4rm_SJV1J8oNzQCbtxBJ8B0lt8hH5MpW20LKD10wVxHnBczHz14gW1INuktUoGx8kW5JajGggm5mpeZIULJGr9BSLpTScdtncLyMH2EhxTkxT7tc3jzV6L1D58iyHP9XWJQn_eVDBuyj8cTT63EOfWl7_OS4ty6utClEFWWYW0_exlXe5UJnjMWKzjCOtU7JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLzvL9MM-rpMKX3hFMeE2bVGdgrQ0Z9482uqumSqzfFzys1GOm1BQEmfE8E56YwW6hYlClXU0MCXSvJkv008Vw_5o7KWStNQWctf88CtLR_8gZ6LGSy-80scJ-D2GEdIFoJJ0Edwnz2VaIq22F5tYCEfjpKqnMUJ5yM38sbDIkTMAOXh-_nl6uoSRdBkFKi2e0ytO9CLMu7I7Wvh6ncMQp7kI6LBIyzLaMtEf0dC6Uc3ZagWTX5cDkpnCEQEt0_iRQ8N7gg-7fD7EBVJNRze8lhPbEv6ytenHxNOXbnYiD1QzxBbsc0xaQ8nwPCDK_-DwvZt_qCj01J65BrWXtkNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEv2AREkNfVIjOxRqbkxxqBimn8Rpjm5Rkuxe-Fdvx-mwR7f3eGWlLFkRQApWBVCbrRNGQByVHHkzPaHWu644-SeEoZuMTUeNWQ_NiRceKHodJW2j32uGTwOS-myMqlvVc0LYC9LKCJ261uULzhlINRAqsn1CYfnUPPgCZTH0KDqNqFbal3QbLJYsnvEXRweq1W9fY6grs0lNUSHBpWUOqqhmSeD2IyNp5rT8Q4PwNGS-4toOFPgGyxfRIFDedYPnKxofCd9Lgq0hYsS-4PmB-KvtP5Cppn0aiZdXswCV-ufDTcCzc44obnMb8WSC4sUjipJL1qdhRvl2M0eJmIjZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2K_xsHDmcBMaGyeyyBk9D1C-38DxoiYfb0i53YQ8agrZWrfSeZr0b_12CnrH1PK_i05Q-SvQUG3voUs3JVTCfbrSLOiBezADwlBIhsdu7ja8JP2O-lHroVAdfe_XSg1avXHhLJSlZCO9p-UcRibWzG9k8OrksrqIrvtVcRNUFVJVl8nNCOM1nhKzRkLa26sylURs6a3-Nt2ThDo94jvDd8PZSH0psdx65L3mK0lmmHE56S-VYXgwo8JI0KwciUDEPzTl4Z07R8wnZrSYplcT2taZOqNG2yF0zc_99tKT69UoVEOr2KXRJbjGdU-WsLHlgOYITiXwuCsp6M9Zf1hNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miv64JZwFBuHvMf5ECuutPhrRJGetKnPZS3Aj9HBcZSj5-1A5cqGdV1eCOcgg2w8HV5gyaTJQvIg6Di_nB4ywutkNAMQr9c79pfh5mZjbRK5ks13O90ENu9S4PEYCYs502JSMoHyx4Um76IDq01MBUP67mOy76pK2ajNFJDdxhkO-NLUmL5C3BtGcB9TZ57xupwl4N58O38fOr_D7-jfYCUb3Op6cnHsezdpuc2yCJQbMOYECp9Dlg5NBUvq6U-E4cI1PH2pRfaP5aRVt3b0Av3wynyY_u7WtC8EebKRzdW5UziHjHSYyZJoeusrsn6ZAqEwlTlu0cuOWRP1LccdZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Noz5QamZKWJ9OCOEAOoofX35dKd142hwenXo4fsOV4WnvIR1nkSo3Q03bMvQYf88KJYwKrO_ETYGgbQFjgp4NF6lGUTt0IgEIP-c48HaFOd_60DQgRUkklygTmjhyFiU6ah9K90_ljSfgB35sNqpH93fWPY_Ode8LhB9zXbnyFmfww2igDYMLsk_Ir_gI2Wl-DvvrAQFpVBO4I9R5ADFdUEIP-rpBNm6fNGBjEzxbR1BTv_JamYu_YfRFfy_wAGaZj-22mc7sNt7kbcySw_lWSzyisDMcw320uchlo4MqO5wB1hjf0z-xWjARNCiZZ6pt-iDipf58Npd6a8JHa5AUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vmu19oGovDOlesyNvL8kfkcAnla-8gKyIAloyiLdm2duXyqanY67ayKJCdMwk0ACFF8YPYnqke-gU-d293Z2GG41wnLlnJ3q0QEoxxo8Bte9iPvA_zy3ztGMRmsGXIT_u4iJr7gvRAj7gtEcaKEqQYpYMXiFA7NNpHw1J8Q2zAohnoJF5wr-XtoQdSpu0xOYkJtIWebYELAwVrO7sM260bpzxrGvLDhU-8ZQ2oE8N2xefHvEqyaGr4UYPZEvGEcRUdjjWne5ux9vND-PfWNPNXxNwQM5eoAG_aibMkL_GJ85pVLeRLBLuHa6-kpH8VKofqDBddz6-MzLcq1XYD-nFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2iirKGVVL-A1nGMAzWQETHXGTAN5_HY0xQMhpi9QS60OHaIbIMSsyZShchVVa98NvMrWpst4H5cx5x1039AmIJxJpD4PkLRfCukoM2W6L-Uf2RSCasYEqZz-bqZTLD95yG4brNSz4l01x__Nb743O5OFQlWr0bnq0CzP1w6NcYgMJuHbvlzXq8pzWAyngCvHaScRbg88Y10RPIwD86plm9FBWjXRHrltGgKgqEGPYpKUi3B6zzpR0Rw42Y4Wqcdzcw2xX7vwALWtJ8tomn9blfVseGbC7xeDAyOsDQWdngAu5mTq7ktHYPKIpAZkcx96_maNn2IMTaryKoCom25Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac9QYzoToH37h_mxxcSGJfFu9QtiZzdZO_mPZcyiJt6XUr4Lvyj0HGiI8Q3azmMOiaTDidn-eM5a0vSvAl9haQ7F1QJIjEvPC54wkBoQDnXjIDrPJOKtB-kU_mkLMlR2zl-hu5K1amgEms3CS4bFRQHrebxdgpp5fFlNSC1om8nBJcnqT_sv9QZ5yhzJ1tx_JvLoTNb5bEHS2c8xi0r9Xiy_Ug4uJFe-Pal5pJqu4nf1e5BJaSdBrSWnqzG2WkQvsYOEHj6ld1ClS3P0S3HFUUg4FvBxE1gnP1lZpx7EVILfezuYmX0IjSYvC4Z46tDRTYyGj8KJzhs9_AJ_A6r6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvNJS9QQPkivxZ-DRayk-sRQxkYeQpJaKiCTnU1QzPX-cwk9UpmncQq0fG57seUyM0Cix1dr1jksyQSt-oEIVd_OT_iB6gZfY9WFligfgDwefcgor94pv2wqf4rnghw-riMjmC8sPR8rKkBSjpH64gUT3ye09K16h8-WDCgr0fE6ZM4EwwDDrBwg5S_tQthCl_GlwOX3QJTBW3jLf3F60xIB92rC7n3zekINvdacS2a3ogPWnQ9AqTAAGqme3cnCAxaukHMmIg2gcnIQWjiN0tiUlgfK0crWVhxMzWHxX5GhZq10DqyeKqnX9JXNnTjdc-fcoNdchgiXS--t16ZuMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u4RoKT1KT3CXSQOoCTqEM8XMPDJloqeU_CpogC0fpTUL18Ys40gqcyyj8_tlw08UaV3qdueazZKwvfTlsZcK8elDYU9SdjhEB3jYWrEGI-ODW2Fm9I8fExIdnVqKZNTyU5ipuMnbnLxs3H7lanmu1jr_Zs7cfkG-XrRVJ-X4gXSleGHDq78phByW63NQAfjxMnUdIPMGRozI3ltY0WuXOQxuI13jkhPnK_uTx3pr54YnX0Wd_WEzvWQ4Grm4RrV6-Iq_CRxkG4RHmT6Tl2i2UMYiL3KPifVCOYq95d2Mxs8Yvta9ZVB0JldRTFIF5crxEa3aIHnFIfPsA2CZzxSWqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULRgKWP-2fFuo5UDV1uXGfeXs-YGXqVCsgZV4wy1BZS7_NO8FQcB4JWrZ1hpg7eoCSLKc-nQHy2kHwDCCJ84B3SeyrjluVzWRHvf2NnX9AELZ1Bxr0lKeEhaTjKrsw9cxooRm-l-QQR_ZVgbR59gbgPiWKApQ23tmpBJ1tn8gAmMTBtmrl87vzjnNwqv_Eh9jzknjlbYKFXUvL4BNaEQGzfqs35w62L0G5q5ufmxK_7sHTeUSAtP0dj6GjemZqgMn7t4IUYMeEcT7R0Rl_9WE5DfywHDXO4Wwx7p4NZj6QMj1hnRZyqEgesLSVJSd7Z_EOilrU06Diuzs07zmct5oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-tiwrBmfgfzYnB4w4ol2DLlCNCki-rfOyJ5nzA-tckcdLtsc1SmaiczAMBh1aZPS15dL_oJLULPE6LNlyZAPCaBDbbKlos2oilNIcNoGaFbJdZV9whU6RY8TXN3xcBROHlXquNI5as456lil_QEX8SuFCaFhGp6tfy4vL9WOhy9QvL3Vp0oPJ8GsHKwuDktXNFBhn11aST21Ey2CUTdJIuvovvMHH7N0To5IL0FwSQn72nlY12V8b0PISexIlU7oh7BQQnBtvKM8rTthh7omcpGjNkFPyhPwJbL_9UrKTT7tqSAA-UdpkSlJ13iswe0b4J-hirdf_eFVd4hBTnBlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qghZtPgPt4cG2oxFxX-0FWMurvY9zyJ5I06XsXOFlVhYpjJ5fYtjgblzWSymd39dfddsfOROWwLVutXVyWSxYzhLPJy6HDZeBVbHtv7ZqhP-gTg0Hh0qI_4XLuE1QWzGG2mKyd6-sM1c0o7kYxq73dwFHNWgw3vzKbYS1EsxLQQ8pI-HWwzgGvgl_L3d8p8iknXS61EizJsjFYvgpqNTy4ans1CcD-AYA02ZPtifolHS_gMQ9QshceJXE_KNBNIaG6U_e2XF-Z2aokMo6La4qVoBrdVDQ_MZvgj4AGVE8jnSpCgn_YBkXwCO3zwf9v7CHzegtKrhc5sy40nUT1ComQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afk_5bwbZSDk86fypRc5jUjilp9WRXiXSH85hKNVuXCE4wZjJXechT2fVPs0ePFsq70-F9BD4vaO-oVgWBzDOlB9nadx2YsOZwsOq-rpsSJ-eGhGqzJmDP0Sfoow8mOpQhEwVStjjZ4x0HOEibBKRqnCp1C1cyNF0XDdcWUU6Zqx89eDFh7KublKfCXXHFThvG6_gvxwjbXCH_YCsmx5Kitafp6F6WwGW9B7QGDlelnxhJoOZcQlrZr8u3IY9xXlILagr22xT9cxLyvoVS7REMSBMFfz0l9Zg795gC2wMZKhmttGRhYp2gw4FtWyIaVCDo5lut1WX-_Vjqm7EGtXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ck6WZp_Ws6X7GlT2wrZ-3dNOaoZmTTn_1tYUlqJMAZZT7epI7jSfV3CjA3Hr-U0wJl3DYQw-QZYblYqEV2k4CySaFLLcaBX3VgZZ0xgFVQ998rleOPuJMj4EgyT4HHdaoCj7HnWNk8HUiEuZJS5IsV_T7r-g9MUdq4_BzWUeHY26x0xN7mwUVEBJRpeRbru8FYaqtnZFPA8J-Z2n1TWfS04dScUw08BurXzYee1HFw0o6EW3mbfTXSv_KIxpJ7ie-kliOXv52nIpxEAPXPMGgUoh6BokNqi70kEDNqfybRq1LQRWewRNRm3_yQqaH_oOKrWvGI1SGQA82MTTq6uiWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4oSDtD2Uc1ZH6zNCQLov13Pzme4ZKrbG_hu3G-QZ5hgdF87QYzrPNOzKu0u_53V1pAcQGn26y-FNcIcrUx6QNkE84G3ICQtbeeK_djiYbrxo80ZM8X702OzDtrN12_gClq0dQ-zpjL5jJBelD5P2v122Qds2JTUxs0UaVu3htOcN7aILS9oQnnzUle_1hA9P_KYKxqYUHJ-HrLzm2D65y56e3iNWs-kx0yDO0LChKQwQHAe3my3sY650MmYt1yru1vod05Cb_KVEjCazA0hIiuQjgt0jUMowq0kJj5xa1dWFuZ8G6MzlENU1bvf1bbVNChm-i_kEhKBtkBZW2f6qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rh00UKacT5gT96B2TnJFTbsFa8Y_sBzNHPhfGhQLghStZXnOx-vefgww_We5ZRXrFABqrpuE8k-1CAZYhpgw3fdFc9cFdTwEW-KunKbr0coZsHaxaAkqxt9VgD2pNdhI5DLjF8pgg-cefd87yDsNctZXGtJrXAgrWs_5HaXGqvg_bIQ2Hc23uaWJf9PAKOTOXk3uj3zJ0CoDGJt3GDWQDNSl0EHjOIZeyET7TP4keNGbGyMswqyR5WZt7crl4MExIyjBgtmOHuPUHRzhQQvuLUyF_63MtAa57JlTZkZHv-GXHGW5aOU7F536R_7jotma-04ACAetpjdKsHP5atLlQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWEk520kyIZD4NDgKY3FBlhDA_H7jJ0Z8cvLfZLeN5qPkqzY8w5ce_08cfZ6LplsaP6yJMI25CRD7XZq_xORwKGKN6NF00QKnvhJM-JzC0c0obH1ToqsP_RLkcXpnivismX3kxokZhLmxvjIKxuL63AQUupCvSEWDr8OqVTF-fqFYBMcT7lkBIPYNPc8y25NiPr8scd_Mh9uHwzy1QtdTuYwBWhWJlqdExHsaHt-7ghamjD4VM1U_mIxnaDaL2JoZnrpeyYN4nEMWDPeA0Y-ClvTgRbegUmkD-uprgcxAD39QUYheF6u40vT5TvPgZBVgN5zuyEFgNGrOUVuxO7rRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxiMC6PMf-zO88o2sblKYiuTbIQJ4kSkmH3OD4Xp0EtBmxIK6Vy05ymJmrzVhFmkwT7aV6vY1w9YR4JrM80WJzhhAlqGOb-F5Wp7Nr4zkpKL7-ssSuzU8SJpND1of-qXZEeSReMx1beCkgHQCkDC0sIgOm7eWyoH2hwKGtLmxKBVaodPSvaezwZJ0Z8E7_pLW9NvZ_wq8RaSgpj2TwilvlTI6bUf8Dq0kMMg71CqZpcOCxpnY6Ms_n5sTqUxxATIopG1VvfkPPqawCCsApT0DCXomdP1ruy4i6G-892MMPvCQelmUuSfaF_bAiXRZqEf8-5y8Idjv6036ft0o_Nacg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzcJNiHkNBLKzsyIQAxnugslf6JO5NKqDnxo4hFRlr1K1KZeTLYeouOlru81bTzHvFkuupqBjKhASOPkupWUK1x-LmQ2gcfdJN7yrLIX27JqF0DPrh70R1qFX_6Mdlj0dQMtT9fDe6O_BiQKPBl8GATZTQkBEum-F26SIbnS2AdzdOvVslzZjCmoCxJT7Cn8qS3o_LLLJRezJNrMykXvAiCUu7uQjpqI3ekmIfKDyqhwQ-cHJQGIoSrXfXs0wi95E2MM5iuj8I4t7T_c8cVOgPmByiDMWxD31Ovlb_fj08xcAjGV_hADCZYyJkmhboQEiR05gquFsS1I_0CfJsc7ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqeTsI-6DO4kNEUXpMCtlDbnW7PJGpnkI8YFE8k0MFLgR2IyfIrbJSCKMHonOpSDfivtRsXN86Kqc23VohhB8rTbU05_AJQq3TyQ7Fx7Zl0XvqxSysTxqkVxwQ9NHdeHh7oy3ATmXjQXIw57ZLWy_Orzt3LCSCbJY7yD3SU554AnielTBGd3O1LWzGq6BG8GBsvNO1HiNyU_HvbA8aoO--ldf2SkzkloXcouA6nwjGMAY0Ev8bpzqJbueEawsGx5AZ1pIesDQXRI-PZHUNK55vUG_ScTzjRPkUbpfL7O2NiH-vqkE6wWp8LAV-Dox0itGtTV7YhstVtlTo3sIpZiSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏
🧠
اکوسیستم GLM و راه‌ های رایگان استفاده
⠀
‏مدل GLM 5.3 شرکت
Z.ai
حالا یه اکوسیستم کامل داره از جمله چت، کدنویسی، ایجنت و API
⠀
‏
🧩
روی همون بیس GLM 5.2 سوار شده و همه پیشرفتش از پست‌ ترینینگ اومده
‏ به گفته خود سازنده، بهترین مدل اوپن‌ ویت برای کدنویسی و ۵۰٪ جلوتر از نسخه قبل
‏
🪟
کانتکست تا یک میلیون توکن و ۷۵۳ میلیارد پارامتر
‏
✅
صدرنشین بنچمارک
CyberGym
در کشف آسیب‌پذیری با نمره ۸۴٫۵
‏
💸
قیمت رسمی هر میلیون توکن: ۱٫۴ دلار ورودی و ۴٫۴ دلار خروجی
⠀
‏
⭐️
برای تست بدون هزینه،
NVIDIA
Build
همین مدل رو با کانتکست یک‌میلیونی و endpoint سازگار با OpenAI می‌ده
روی API خود
Z.ai
هم مدل‌های
GLM-4.7 Flash
و
GLM 4.5
Flash
و
GLM 4.6V Flash
همیشه رایگان هستن و وزن‌های خانواده
GLM
روی هاگینگ‌ فیس منتشر می‌شه
💥
⠀
‏
📝
معرفی رسمی GLM 5.3
‏
📊
قیمت‌ها و مدل‌های رایگان
‏
🟢
تست رایگان در NVIDIA Build
‏
📥
وزن‌ها روی هاگینگ‌ فیس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
