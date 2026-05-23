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
<img src="https://cdn4.telesco.pe/file/KhMOWGOoMRsXjZHHI0sGMIGRT_VfO-9Tcv0vb2q8nVZs4m-fuoof4Pdn4qcNnCbry1cPyqkGUYJqPK7ooJeLKT0uRaRYqawSYrZ-szeKvjEsPLM9yEoAFmjjdMAGNkguZ5Qhuzajl-eHWxewtlPu8oHQvidW6VNFYE2xTzunFc1lntIoGUFXd1hT3KNsjERQIivdCdRjJWjQLX6y7lV4dut9hE9ivIfTO4Aj-ASyeFj3rHjnZnecGA556SYD6jEv0m77mCL8osoj-r7Oj8mjFJ8ngYQgjN9AWrn2rP74lNHk0BSW2nQMRVQlHcqLo5PzGLNHwXIAd0rd246A2QhK6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 01:42:52</div>
<hr>

<div class="tg-post" id="msg-437562">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5nxQmgTwkdbGkVebfqBYIhb_O73BWT9pVX9gnvy8Mqo5nS_6eMMOrgcbm531i8KoFHEHBCpBzocBfGeShFKSKjgxO60KORqOD_YhHVskv577PJFUckaJo8qlLNMdSaCOf4Ws_g4F9JODe3nKaR9fJOxQYFG35RUzj4zCnoWE6qptlNduP5W1pInmRJvVPdzoIaRAtiONEMLNcOhJmhKrUnjRFSE4UGa9sFKGYh-w6dLzQtYsRGNPgXSrKXuYIrDvWlNLfweBEN9sqkWanESXro9hmwB_2UlDhAVnTT_VlzQFvmmxBLXm-SP0jZnIrG2VLSMovdN0M8wS61I4uvdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصادف خودرو ديپلماتيک جمهوری آذربایجان در محور مرند-جلفا؛ راننده فوت کرد
🔹
رئیس پلیس‌راه آذربایجان‌شرقی: در پی برخورد یک دستگاه خودروی سواری پلاک دیپلماتیک با کامیون میکسر حمل بتن در محور مرند-جلفا، رانندۀ خودروی ديپلماتيک که به‌تنهایی در خودرو حضور داشت بر اثر شدت جراحات وارده در صحنه جان باخت.
🔸
گفتنی است، برخی رسانه‌ها به اشتباه از فوت دیپلمات جمهوری آذربایجان در این حادثه خبر داده بودند، درحالی که فرد فوت شده رانندۀ کنسولگری این کشور بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/farsna/437562" target="_blank">📅 01:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437559">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ: جزئیات و جنبه‌های نهایی توافق ایران به زودی اعلام خواهد شد
🔹
دونالد ترامپ مدعی شد که درباره بخش‌های عمده توافق با ایران مذاکره شده است.
🔹
او همچنین درخصوص تماس با نتانیاهو گفت که مکالمه با او به خوبی پیش رفت.
🔹
ترامپ با ادعای اینکه «تنگه هرمز طبق توافق…</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/437559" target="_blank">📅 00:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437558">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MK0m_1606I-DnLD582VKRN0edzAxRjMYHdQKqyxQwkef2E6coAittKf7Uj8noov2qdJOEbvmtlTPQHFlR_sPBdh8dMahgeGcuWwyWCtekRzhp448kok6zstz4S1GfI0YbbGbNC_l2IgiS8XYdJmY7JwEFr76dwBFO8dJCqPnsed-w9FKEcFx3qZNsOM6lWlnfGDqmSTwDmS4iWauNbAWXLeGwg24fcKYMcyU8hX6FLhSoEEDVW8_KFmhOtOnBF2WjvGjFE8es2e0GP0U4LjR_3u77X-tpFPSwcAe5pDlv5_RfkgKx089AZA_gcwMrxMDrdY7M1yGVKS6jThL9pXIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشاگری گاردین از برخورد متا با مخالفان سعودی
🔹
گزارش جدید گاردین نشان می‌دهد شماری از پلتفرم‌های بزرگ شبکه‌های اجتماعی از جمله اینستاگرام، فیس‌بوک و اسنپ‌چت، حساب‌های مرتبط با فعالان آزادی بیانِ مخالف سعودی را در داخل عربستان محدود یا مسدود کرده‌اند.
🔹
در واکنش به این موضوع، شرکت متا اعلام کرده که در برخی کشورها ناچار است محتوا یا حساب‌هایی را که طبق قوانین محلی غیرقانونی شناخته می‌شوند، محدود کند.
🔹
این ادعا درحالی مطرح می‌شود که این شرکت حاضر نشده تحت قوانین ایران حساب‌هایی که در کشور باعث خرابکاری شدند را محدود کند و در رفتارهایی متضاد اقدام به مسدودسازی حساب‌های دیگر، از جمله حساب‌های طرفدار فلسطین کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/437558" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437557">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ترامپ: جزئیات و جنبه‌های نهایی توافق ایران به زودی اعلام خواهد شد
🔹
دونالد ترامپ مدعی شد که درباره بخش‌های عمده توافق با ایران مذاکره شده است.
🔹
او همچنین درخصوص تماس با نتانیاهو گفت که مکالمه با او به خوبی پیش رفت.
🔹
ترامپ با ادعای اینکه «تنگه هرمز طبق توافق باز خواهد شد» افزود: جزئیات و جنبه‌های نهایی توافق ایران در حال حاضر مورد بحث است و به زودی اعلام خواهد شد.
🔹
ترامپ افزود: با رهبران و مقامات عربستان سعودی، امارات، قطر، پاکستان، ترکیه، مصر، اردن و بحرین در مورد ایران تماس خوبی داشتم.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/437557" target="_blank">📅 00:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437556">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KU8HjAnFDT0t5wWgNejG6t7c0vvdmux38r7noBYkizDaqDBkWip49i_6Tz7rJ_kbjUuBmobyUxwpgyU76GUOQSP2zIs8viNS_NTg0z5BsuRDaKKlNIBOflR5A14UxDnjfXRNH-5oLrHEzjGbMiy0tiZ-fZ-JRxi30dkK_1QF_I4iM7mSfjBJCLBhltE9D54b2tHXi5PCCN4mAts_Us6l4_iV-hPJAro7NgbmPlH4fWToWuNk0aECNkzAFul5aMsz4LPE9ueKXPm8YNOSzyfGwpK26dUcg72iByoU0aqJ29b6iIIXj66Ej871XRVw74NkVzkrpANW4M4eO1SFe3DcXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ ماهی و صیادان
🔹
در آبگیری دوردست و سرسبز، ۳ ماهی زندگی می‌کردند: یکی بسیار عاقل و دوراندیش، دیگری نیمه‌عاقل (با‌هوش اما کمی تنبل)، و سومی نادان و بی‌تفاوت.
🔹
زندگی آن‌ها آرام بود تا اینکه روزی ۲ صیاد از کنار آبگیر عبور کردند و تصمیم گرفتند با تورهای خود بازگردند و ماهی‌ها را صید کنند.
🔹
ماهی عاقل به محض شنیدن سخن صیادان، وقت را تلف نکرد. او می‌دانست که نباید خطر را کوچک شمرد؛ پس بی‌سروصدا از راه‌آبِ باریکی که به رودخانه بزرگ وصل می‌شد، گریخت و خود را نجات داد.
🔹
ماهی نیمه‌عاقل پس از رفتن صیادان تازه به فکر فرورفت و با خود گفت: «افسوس که غفلت کردم و فرصت فرار از دست رفت؛ اما نباید ناامید شوم.» وقتی صیادان آمدند و راه‌آب را بستند، او خود را به مردن زد و روی آب شناور شد. صیادان به گمان اینکه او مرده است، از آب بیرونش انداختند و او در یک فرصت مناسب، خود را به داخل رودخانه پرتاب کرد.
🔹
ماهی نادان همچنان بی‌خیال ماند و دست روی دست گذاشت. با خود می‌گفت: «هنوز که اتفاقی نیفتاده است، تا پیشامد بعدی خدا بزرگ است!» او هیچ تدبیری نیندیشید، سرانجام در تور صیادان گرفتار شد و جان خود را از دست داد.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/437556" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437555">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c853019a85.mp4?token=c_cqdA8OdG4u1Apdq6NVJ808SJ5i5mR4DD3I5Ijfo1qyrm541DxY3qQdIT457z9GeADu7i4mexlKlP9b0y6fkniZRPaMWfpGzGGCvnQmJ-EdmmqCTG0wR1Uik2ronz3eTFyd3mSaJV-lbBALQoJjuzzQhwvAcC_v_HSHG-vSaNz1S_ksq3T7KmhxbD2luX3eoyc6foiMYpbJQI9tmWK0P4Jh9cbwWecfMG9lmZersY-FO9Upoqk9peIGBDQDKxc4aR3S_ngGQyjjEWehZHGRDtTO2hiTYlmPq3y6ZYaH4C6WBg5jwqmUk-xnHvzEvTKTS2eLsvzDMTZ-72IhU5A1IWbS-pPE9mbFoPSwwKqc-stSgRBTE0w9Abm0ikv0LOJ-oMz8qgHSE56jW5TDatU_cinEf459Von-9A1CjH1eV4i77i0RHJrYBit9htEwcCALc8406KL5nmVopc7B_6zgpaG4n8yDACNjGbYSroHCBJZmiisLP0otI3yEn_cCoztmqUUjHqRVdjCLA_3hfrCVy-qAKG9bTXJLrx3DXnVT-Cc58Ffr1H26W_QDsyNR4z_bDY92cp_b4eX4CAcPYALUV1syvlgFvVFYQNQQ5N31PHiHA_yNgrE6S6JjNgxjKYtyxGw12aZ6Qr5wF23VCP1hYPsVSANoeiG4FTWsl6Vg2b4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c853019a85.mp4?token=c_cqdA8OdG4u1Apdq6NVJ808SJ5i5mR4DD3I5Ijfo1qyrm541DxY3qQdIT457z9GeADu7i4mexlKlP9b0y6fkniZRPaMWfpGzGGCvnQmJ-EdmmqCTG0wR1Uik2ronz3eTFyd3mSaJV-lbBALQoJjuzzQhwvAcC_v_HSHG-vSaNz1S_ksq3T7KmhxbD2luX3eoyc6foiMYpbJQI9tmWK0P4Jh9cbwWecfMG9lmZersY-FO9Upoqk9peIGBDQDKxc4aR3S_ngGQyjjEWehZHGRDtTO2hiTYlmPq3y6ZYaH4C6WBg5jwqmUk-xnHvzEvTKTS2eLsvzDMTZ-72IhU5A1IWbS-pPE9mbFoPSwwKqc-stSgRBTE0w9Abm0ikv0LOJ-oMz8qgHSE56jW5TDatU_cinEf459Von-9A1CjH1eV4i77i0RHJrYBit9htEwcCALc8406KL5nmVopc7B_6zgpaG4n8yDACNjGbYSroHCBJZmiisLP0otI3yEn_cCoztmqUUjHqRVdjCLA_3hfrCVy-qAKG9bTXJLrx3DXnVT-Cc58Ffr1H26W_QDsyNR4z_bDY92cp_b4eX4CAcPYALUV1syvlgFvVFYQNQQ5N31PHiHA_yNgrE6S6JjNgxjKYtyxGw12aZ6Qr5wF23VCP1hYPsVSANoeiG4FTWsl6Vg2b4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد یاسوجی‌ها: این آخرین قماره، جنگ ادامه داره
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/437555" target="_blank">📅 23:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437554">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69febc6574.mp4?token=H3eVeHY_LOOXHxaNLfVzTqhi5xL0Jfya4FsTu_ak6SIJx1xRmPVIokKWN0xHwpTFllkMW2FnZxJl7Hkh8l59oRoXgAxNU3M_qOWnk6jOTtP931p_nZNgIIDCTqH8M0oZcpJots8j7iqsa86zHRMiMwSQ_dYLvNUlNvrY8SKU9elvMHBYhTKZtVbb3lhbIP5s7uEPvVSfv7QnsX5L__hp4LTUAD2QQ2LE-0tNeOCuIub1b8As-M-y0974ecpYXsd52uVLBxE7Maf--0FTCE8GsMnI7Tw-2401a7T9GKxHMHpGyqr9TFjFBqqzYcfEHrzBUHgAWTK4PXYRdu6n2aU0UDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69febc6574.mp4?token=H3eVeHY_LOOXHxaNLfVzTqhi5xL0Jfya4FsTu_ak6SIJx1xRmPVIokKWN0xHwpTFllkMW2FnZxJl7Hkh8l59oRoXgAxNU3M_qOWnk6jOTtP931p_nZNgIIDCTqH8M0oZcpJots8j7iqsa86zHRMiMwSQ_dYLvNUlNvrY8SKU9elvMHBYhTKZtVbb3lhbIP5s7uEPvVSfv7QnsX5L__hp4LTUAD2QQ2LE-0tNeOCuIub1b8As-M-y0974ecpYXsd52uVLBxE7Maf--0FTCE8GsMnI7Tw-2401a7T9GKxHMHpGyqr9TFjFBqqzYcfEHrzBUHgAWTK4PXYRdu6n2aU0UDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
«انّ معی ربّی» فرمایش امام است
🔸
در دست تک‌تک ما شمشیر انتقام است
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/437554" target="_blank">📅 23:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437553">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5327365d67.mp4?token=qVzQWD7taXtHBB0GiYJR4GXoIpuSvxB7vc9mYuQYynAK1tx0w4Ar-5rzEvRK_a9-mORWN-ZxVaCPhvC-fckmSpQ90tuouYZNPbwqRX9PtDJg_PKCwT93L87B9HlWTaTyGDDmFqY9-HGC4fBZAatLbaxt1kimkn2OBhlmpYg6K9j7OYrhYf00VWLe-pN42rrP_M6OZLPIVsBCXRUrCjEIptPohzfTnlPdsGZppt-r1Q-PlsJP2uXiiplsP9kOsnAlOeXAb11zdRNTOQzWqt7HrAE668JxrFzUvGKhcQ84nIiVrLKRrkCOiWsRo6k-ruXF5GwFQIrf5yTzczEBEIKFcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5327365d67.mp4?token=qVzQWD7taXtHBB0GiYJR4GXoIpuSvxB7vc9mYuQYynAK1tx0w4Ar-5rzEvRK_a9-mORWN-ZxVaCPhvC-fckmSpQ90tuouYZNPbwqRX9PtDJg_PKCwT93L87B9HlWTaTyGDDmFqY9-HGC4fBZAatLbaxt1kimkn2OBhlmpYg6K9j7OYrhYf00VWLe-pN42rrP_M6OZLPIVsBCXRUrCjEIptPohzfTnlPdsGZppt-r1Q-PlsJP2uXiiplsP9kOsnAlOeXAb11zdRNTOQzWqt7HrAE668JxrFzUvGKhcQ84nIiVrLKRrkCOiWsRo6k-ruXF5GwFQIrf5yTzczEBEIKFcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از حضور مردم در شب هشتادوچهارم
@Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/437553" target="_blank">📅 23:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437552">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f9598ef8.mp4?token=tgolUtR1ukIyf8IrT2fIgovhfBeQcZixTEnjtGGkgZZ5srUlc-Fk6Q3KVM0DYatl70CdQBR2K9hZmz-4I7TJX1mjGIyFm7z8mpcFBzRDXxkhdgg2FH5oJFIfz4w83xV0KoPqDsXn8cYXFPXVcjAn2v7t1DbQate0TLAhgCTYpIlRvP8w3JKC1A-xfAsgc5sU_bw3rMtOc3q7a-IDfBCD2FGxe0bIlW3qndWMNdsP4ebeDR4QXzQdw9Y_1jae0_PdDVj7rSix2y7mEDTPWHbQE2gfJvQXvBOgjTMhJuLlgJNVz68N7OTshtKwGQmLc3K0TmVSjbDAWr6Ob7m4yfsmP4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f9598ef8.mp4?token=tgolUtR1ukIyf8IrT2fIgovhfBeQcZixTEnjtGGkgZZ5srUlc-Fk6Q3KVM0DYatl70CdQBR2K9hZmz-4I7TJX1mjGIyFm7z8mpcFBzRDXxkhdgg2FH5oJFIfz4w83xV0KoPqDsXn8cYXFPXVcjAn2v7t1DbQate0TLAhgCTYpIlRvP8w3JKC1A-xfAsgc5sU_bw3rMtOc3q7a-IDfBCD2FGxe0bIlW3qndWMNdsP4ebeDR4QXzQdw9Y_1jae0_PdDVj7rSix2y7mEDTPWHbQE2gfJvQXvBOgjTMhJuLlgJNVz68N7OTshtKwGQmLc3K0TmVSjbDAWr6Ob7m4yfsmP4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه ایران شده جان‌فدای حسین
@Farsna</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/437552" target="_blank">📅 23:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437551">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f61c8c0629.mp4?token=JRhs_wJ6neqSPV6eZMOHlabBQqDUvHrxDjZoVJ1T3sn2RTS8VVQHlQwQNjzFZm8iS3bi0qqJv-o5i9bxm8Xo5WQD-3OYuahLCieBcca58Mf61IJPYn7h0WmNWiSM31pyt9uQAxb_W8x7UcwCudtyPJ8dBn5NvBDtDQqdLqWiPhfMyjABRDefWjpD3sFq6r3IZ6HYYdPxtJwzTl_h6cDxhaArs3FI4lTuugdRQ6b6y5hNpz6EJKiD3ihNeRY0-uu4rUK5G8hjocHbPUu9m-Ka824AtecEyipaoO0zTP6WSv596pOyUP7Za7epa-a_4OKmJzDcLDilznz9gipHzdi8Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f61c8c0629.mp4?token=JRhs_wJ6neqSPV6eZMOHlabBQqDUvHrxDjZoVJ1T3sn2RTS8VVQHlQwQNjzFZm8iS3bi0qqJv-o5i9bxm8Xo5WQD-3OYuahLCieBcca58Mf61IJPYn7h0WmNWiSM31pyt9uQAxb_W8x7UcwCudtyPJ8dBn5NvBDtDQqdLqWiPhfMyjABRDefWjpD3sFq6r3IZ6HYYdPxtJwzTl_h6cDxhaArs3FI4lTuugdRQ6b6y5hNpz6EJKiD3ihNeRY0-uu4rUK5G8hjocHbPUu9m-Ka824AtecEyipaoO0zTP6WSv596pOyUP7Za7epa-a_4OKmJzDcLDilznz9gipHzdi8Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سامانه ثبت ادعای مالکیت املاک راه‌اندازی شد
🔹
تمام افرادی که ملک و زمین‌شان قول‌نامه‌ای است، ۲ سال فرصت دارند مدارک خود را برای دریافت سند رسمی بارگذاری کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/437551" target="_blank">📅 23:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437550">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd89a3dae3.mp4?token=hMTV3Al1vuWwDkc7KStQwId-tRH7BRat32G_KCD7F-DNHg23r5nD8VKVxe0V8uqo4pPwzQigVSrrv4ukOKQWJfMmaOXmJJhdAzfRdLrhfg8lq7H0RgyCqtn1B6frehyWxwLAsmKrTSmbE6fdLPgPYTb1Xlxvt34qM9wdqqvoMnpWlAnnNyoZZ25L7cccmEsmWnbG2v5oe5JRtNIrwfvs6lm7Z0YrePE6_WTtnG6Al089UkOg7_21iElGlOWFOoQugszqP6jTpbv5WhoyCh3vr7g8PLi5GtQi9SAm-UJadNARqOy8F4R-HOLnO0jPMPG6-Yb_37u9G9kJqMm3E-GVvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd89a3dae3.mp4?token=hMTV3Al1vuWwDkc7KStQwId-tRH7BRat32G_KCD7F-DNHg23r5nD8VKVxe0V8uqo4pPwzQigVSrrv4ukOKQWJfMmaOXmJJhdAzfRdLrhfg8lq7H0RgyCqtn1B6frehyWxwLAsmKrTSmbE6fdLPgPYTb1Xlxvt34qM9wdqqvoMnpWlAnnNyoZZ25L7cccmEsmWnbG2v5oe5JRtNIrwfvs6lm7Z0YrePE6_WTtnG6Al089UkOg7_21iElGlOWFOoQugszqP6jTpbv5WhoyCh3vr7g8PLi5GtQi9SAm-UJadNARqOy8F4R-HOLnO0jPMPG6-Yb_37u9G9kJqMm3E-GVvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار لبنانی در شبکه سه: حزب‌الله بر روی نابودکردن گنبد آهنین اسرائیل تمرکز کرده است
.
@Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/437550" target="_blank">📅 23:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437549">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c58b5e1b46.mp4?token=YWjHhp18tz10WvYWSWX2aQs15cxhRiU1sRCSGnlr36lgJsIwZYzMk44SRnptHJ6vE6ljBWxxGYFVBifU20p-Cmal1XUxqasO_xsL6QS1KluM6zo6HgovETw3_rjpRc8fStDtb_HaX3qnXN11JAZa5y_-_FbF-PAwYzemsKpBAmgGn0du6r0tm_943hep8RfRDHCxoJJUywZEd6NXFjlRaB7T30Aj6QwhE_Tekjl8OfCZ-mMWovehEEmFr6dfBgwDg8cZj2d9N6NTQ_VEzwnqLvwIrR3dtDoUV3WKBH6hvpqgJPylgCN2jOl4T9aVQyP0VTiGEzyQ2FGaQwjOU0wj_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c58b5e1b46.mp4?token=YWjHhp18tz10WvYWSWX2aQs15cxhRiU1sRCSGnlr36lgJsIwZYzMk44SRnptHJ6vE6ljBWxxGYFVBifU20p-Cmal1XUxqasO_xsL6QS1KluM6zo6HgovETw3_rjpRc8fStDtb_HaX3qnXN11JAZa5y_-_FbF-PAwYzemsKpBAmgGn0du6r0tm_943hep8RfRDHCxoJJUywZEd6NXFjlRaB7T30Aj6QwhE_Tekjl8OfCZ-mMWovehEEmFr6dfBgwDg8cZj2d9N6NTQ_VEzwnqLvwIrR3dtDoUV3WKBH6hvpqgJPylgCN2jOl4T9aVQyP0VTiGEzyQ2FGaQwjOU0wj_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تقی‌پور، نماینده مجلس: شبکۀ حیاتی کابل‌های فیبر نوری جهان از تنگۀ هرمز و باب‌المندب عبور می‌کند و ایران می‌تواند این کابل‌ها را قطع کند.  @Farsna</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/437549" target="_blank">📅 23:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437548">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9662ebde8c.mp4?token=tEbpBkXes4uoCAI8YiN2y3agu1QczNH9x-7cyzORZY8LuLU90N7evmsXdy5L-jKvf_kp-bPuCLawqqqAcytej2ceOoNK_-ZmmHbJ87FBe6iaUCeIp5Joz0XY3kbz8-M-NoRiZL1k8U0Ls2BI0BCJvO8ei4uDYfFbBQDpf5r2fdKd97bQaifJI0uBEWk5ruwNBSMCaf6MrvhYm6k2A_lo39nzhT_vEFGyWV2A4njC1p8y_M049Nl2Qd3iV714muxcP7w0JdAvMY2BNbMohqZuhEvnaV2mChNGd7pnx-voJxULcy1th2aHcZMqRHNvoKaMNT-KMEwfAsk-4OQgK1tp23NlwcldEjCj7oplgg8eubWTl5y73hiQaWQxJCl9CYONkhAEzU4t9-gnDn09fC1-3KyV65eZFR3bIo12Nps2VSfgYQ7y9fJThdTWeQSmrba0CDlX6ZoRs3m3Oi54v3LPa9lNAueCMiLrQ0eQ6JfSTJ4gEBjyJ1PB8_nWi-DpCltBjN2l8FL1_Lt06dNYDqXIOhOqkIFgkH4xGRyiSfYpBRP4hKOeFzmIHfnpjPU3E9Il1cAGPLC9N2SkDAzxwh1VCAD0PuwOyRRmhowyHV2qlQuBj7K7Zq8rg0j8uT0uw_oFF99CiN-cXo6e7nWICg5iNj1VudQrjYI3PN9Dlxw_1yE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9662ebde8c.mp4?token=tEbpBkXes4uoCAI8YiN2y3agu1QczNH9x-7cyzORZY8LuLU90N7evmsXdy5L-jKvf_kp-bPuCLawqqqAcytej2ceOoNK_-ZmmHbJ87FBe6iaUCeIp5Joz0XY3kbz8-M-NoRiZL1k8U0Ls2BI0BCJvO8ei4uDYfFbBQDpf5r2fdKd97bQaifJI0uBEWk5ruwNBSMCaf6MrvhYm6k2A_lo39nzhT_vEFGyWV2A4njC1p8y_M049Nl2Qd3iV714muxcP7w0JdAvMY2BNbMohqZuhEvnaV2mChNGd7pnx-voJxULcy1th2aHcZMqRHNvoKaMNT-KMEwfAsk-4OQgK1tp23NlwcldEjCj7oplgg8eubWTl5y73hiQaWQxJCl9CYONkhAEzU4t9-gnDn09fC1-3KyV65eZFR3bIo12Nps2VSfgYQ7y9fJThdTWeQSmrba0CDlX6ZoRs3m3Oi54v3LPa9lNAueCMiLrQ0eQ6JfSTJ4gEBjyJ1PB8_nWi-DpCltBjN2l8FL1_Lt06dNYDqXIOhOqkIFgkH4xGRyiSfYpBRP4hKOeFzmIHfnpjPU3E9Il1cAGPLC9N2SkDAzxwh1VCAD0PuwOyRRmhowyHV2qlQuBj7K7Zq8rg0j8uT0uw_oFF99CiN-cXo6e7nWICg5iNj1VudQrjYI3PN9Dlxw_1yE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم بروجرد برای امام باقر(ع) در هشتادوچهارمین شب تجمعات شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/437548" target="_blank">📅 22:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437547">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnvP8-bGkpwiFbGvKW0LJXvkPDPT4OpQTpbhP4CDmij8R7_SNPP33OmajuTlf7G5ra-UqHO4MKwK3v5JkUKU1KvipQjClMLSP1eY78vN9C2sSU2K8tXop0pm1iRLO1kWpG3rnR1RqbT3xEb7xwywaM8kgkxNbFOsMxGvo3YbxgVnnYPiExVopP7dfyWmhQhG9MmE7WziscjLxEhtZWE0TdkakrTQ2OhkkEWIstUIS_OX4Yl4qB2XoFHmysrWpxquiHLlv5K0faKJvzYTky11J9GBUmmdfEtZMmZ9vBXBIZwSk5wiQAS4k_sBbN74n-t5Cyg4arrT22VY0ZBk6bsjRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار امنیتی سفارت آمریکا در اوکراین برای حمله احتمالی روسیه
🔹
سفارت ایالات‌متحده در کیف: اطلاعاتی دربارۀ یک حملۀ قابل‌توجه احتمالی ازسوی روسیه به خاک اوکراین دریافت کرده‌ایم؛ شهروندان آمریکایی آمادۀ رفتن فوری به پناهگاه باشند.
🔸
ساعتی قبل زلنسکی، رئیس‌جمهور اوکراین هم گفته بود به اطلاعاتی دست یافته که نشان می‌دهد روسیه خود را برای یک حمله موشکی سنگین به اوکراین آماده می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/437547" target="_blank">📅 22:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437546">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c759e7ed29.mp4?token=Ec5SqxGYn9mLytIIsEz5F5ahxiCslI4NyU2A3AEbiSXZxoVK0xFusO9CPLrUdEB4Ef9YKgjOinBSkxAIBN0_mXuiOmY6KFj1Xrig2h7E_ecEmvQsDYQCHXBhclJdDANhkP-M9qqoRqXor-pYfnoaQMJYHN_zjyO0ar_xIm1SJAckoM58TwpHlyr-WWjXKgYmD6N_zYZs4DW_PJVvgusGbxDDiqe5yEGMM3U5fBhiZA7oJUtrKFHlLgWPB3yJMQ9XmaGH3rwSLHqFVL9YaDAu_W1I3Ze6Znw_bHAA9PsLUdW4E4hc1i318rcs66Rv7WdUeCokFQjYxkQmWr5WyglD_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c759e7ed29.mp4?token=Ec5SqxGYn9mLytIIsEz5F5ahxiCslI4NyU2A3AEbiSXZxoVK0xFusO9CPLrUdEB4Ef9YKgjOinBSkxAIBN0_mXuiOmY6KFj1Xrig2h7E_ecEmvQsDYQCHXBhclJdDANhkP-M9qqoRqXor-pYfnoaQMJYHN_zjyO0ar_xIm1SJAckoM58TwpHlyr-WWjXKgYmD6N_zYZs4DW_PJVvgusGbxDDiqe5yEGMM3U5fBhiZA7oJUtrKFHlLgWPB3yJMQ9XmaGH3rwSLHqFVL9YaDAu_W1I3Ze6Znw_bHAA9PsLUdW4E4hc1i318rcs66Rv7WdUeCokFQjYxkQmWr5WyglD_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور  آهنگران کنار مزار شهیدپاکپور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/437546" target="_blank">📅 22:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c03480e0d.mp4?token=VFJPy30CLENoNE7wVcZyutHSUkxoQhkzry4nT2HIoA59_AkOq470l0mVAp52rfgZUJ_XzhddTlCjJt7hmfgul_Y1OOiDIi3r3LGBwz5H6oWxdn8Q6TTJybyKbfV21rTBxeoRLXj_q_mkYcG3PzirEWdyq95gT9PS9IfKa02SJEQVZZgJYagXbWgM_nI-SFKPtvQkdIgOW2aafWYdVTwYzx2JwImpaD9Q3wFJ85ltej91ph0uSBoUE5PaaqnmNt-KfCTQ4fo4H7XUFDWrsvXNzoJHagCReNHlJeAtWR66sspHWRDP4xdBlUOpNvepjU2pfVnIdib6ycXzJ1C1oKo6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c03480e0d.mp4?token=VFJPy30CLENoNE7wVcZyutHSUkxoQhkzry4nT2HIoA59_AkOq470l0mVAp52rfgZUJ_XzhddTlCjJt7hmfgul_Y1OOiDIi3r3LGBwz5H6oWxdn8Q6TTJybyKbfV21rTBxeoRLXj_q_mkYcG3PzirEWdyq95gT9PS9IfKa02SJEQVZZgJYagXbWgM_nI-SFKPtvQkdIgOW2aafWYdVTwYzx2JwImpaD9Q3wFJ85ltej91ph0uSBoUE5PaaqnmNt-KfCTQ4fo4H7XUFDWrsvXNzoJHagCReNHlJeAtWR66sspHWRDP4xdBlUOpNvepjU2pfVnIdib6ycXzJ1C1oKo6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نیرو: موافق اصلاح ساعت رسمی کشور هستیم
🔹
تغییر ساعت رسمی حدود ۱۰۰۰ مگاوات کاهش مصرف برق را به‌‌دنبال خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/437545" target="_blank">📅 22:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437543">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c92e8dd2a6.mp4?token=WFb0GWro60603dg60EiENYnPQ933q3JgJwoeKzHrghmVxlfE-NjXqq3i04ujGB_UGwiMy5ICtLrCUza9O96kKytM6fGCHuo2bZurVIcD-2OgjUzf2dMTB5vPKt6E2q2zprBC0dVohPualk5Y5dKT3NJcQxnUL8IWQpXfEAQ0kVK7MbhczviPeRHv-xm_A3uBOKOXXC-lVqvbPsWXJ5I0aA6bE5tkTEhgP3AEIBHVsLYzU5DLl1kqOtopkHuwGmRIMe-y0c78NeXFxYrjj3eClxL79qrarZoGcaRAGu9S3YP0DsZTSW0_ESrc4wHnFnnBI2XbcYlvbO86E3d9wbPQiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c92e8dd2a6.mp4?token=WFb0GWro60603dg60EiENYnPQ933q3JgJwoeKzHrghmVxlfE-NjXqq3i04ujGB_UGwiMy5ICtLrCUza9O96kKytM6fGCHuo2bZurVIcD-2OgjUzf2dMTB5vPKt6E2q2zprBC0dVohPualk5Y5dKT3NJcQxnUL8IWQpXfEAQ0kVK7MbhczviPeRHv-xm_A3uBOKOXXC-lVqvbPsWXJ5I0aA6bE5tkTEhgP3AEIBHVsLYzU5DLl1kqOtopkHuwGmRIMe-y0c78NeXFxYrjj3eClxL79qrarZoGcaRAGu9S3YP0DsZTSW0_ESrc4wHnFnnBI2XbcYlvbO86E3d9wbPQiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از وقوع انفجار و آتش‌سوزی در مقر کومله در اربیل عراق خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/437543" target="_blank">📅 22:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437542">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21852932b1.mp4?token=TdLu_E19NXZHw47ERxt9wW4JXLwbd9FZZjSUl1jUGagE9u6F5jefkz5iQ4wnwtP0maQ7ZYPzD1gfXIJuv0gFO8gc5cVJqKbqtfSNvV61D-dAVYMGveOV1Eq7Kqtni1kxINFzIlqqAoQoU895X8syQ0vlid_N5oXaittO6eAyiZrxR6BPyNc6LW2sjQmS-eQdweGWtMs_LGUqz3JU8sfbM8ecdzLKZR6GAxfj3ks2AdC1afUPP3mBQjRcudL9MRh8EnVgqjFm8oJU53SDBVx1Jx4lwVRCegQm0lb_uGpRUbm7MVm5MwNOl3SlO-5NToDQhypZgJga_lDxInEWdqzEPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21852932b1.mp4?token=TdLu_E19NXZHw47ERxt9wW4JXLwbd9FZZjSUl1jUGagE9u6F5jefkz5iQ4wnwtP0maQ7ZYPzD1gfXIJuv0gFO8gc5cVJqKbqtfSNvV61D-dAVYMGveOV1Eq7Kqtni1kxINFzIlqqAoQoU895X8syQ0vlid_N5oXaittO6eAyiZrxR6BPyNc6LW2sjQmS-eQdweGWtMs_LGUqz3JU8sfbM8ecdzLKZR6GAxfj3ks2AdC1afUPP3mBQjRcudL9MRh8EnVgqjFm8oJU53SDBVx1Jx4lwVRCegQm0lb_uGpRUbm7MVm5MwNOl3SlO-5NToDQhypZgJga_lDxInEWdqzEPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: هرگونه تجاوز دشمن با ضربات جبران‌ناپذیر مواجه می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/437542" target="_blank">📅 22:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437541">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f65c39bae.mp4?token=iDS91fHnyG78KeTVYeWzt20gSZR-wKuRY1ORf8GWwERx1SpJztfS7uzkBcGxf92RBkHU_lg3ENtvkKom6uE0nFpLK-ooKyEsDxY24L05P9ntWSoROlqr21p00asdfF83Gzla1_s5l3QzcKs39K1kfhDyBbn_MMjS57TkGb4sikijcBVtB9nByv7_8S9iBDqirvlX-kVGoZHrUJmkzgtk4AsKkifkdEVuc20NR_5EndpNTfrPj1ATCRB5XBlWq-c3nVvMy6yEM7S00ajtig9wH71A326rhLSdXAtDkTN2Ntkfe6D55EWJfnMjzSObTO_M2694OKPIkKXVanCwzG3EYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f65c39bae.mp4?token=iDS91fHnyG78KeTVYeWzt20gSZR-wKuRY1ORf8GWwERx1SpJztfS7uzkBcGxf92RBkHU_lg3ENtvkKom6uE0nFpLK-ooKyEsDxY24L05P9ntWSoROlqr21p00asdfF83Gzla1_s5l3QzcKs39K1kfhDyBbn_MMjS57TkGb4sikijcBVtB9nByv7_8S9iBDqirvlX-kVGoZHrUJmkzgtk4AsKkifkdEVuc20NR_5EndpNTfrPj1ATCRB5XBlWq-c3nVvMy6yEM7S00ajtig9wH71A326rhLSdXAtDkTN2Ntkfe6D55EWJfnMjzSObTO_M2694OKPIkKXVanCwzG3EYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار ۸۴ مردم بجنورد با بزرگداشت شهادت امام باقر(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/437541" target="_blank">📅 22:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437540">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">۷ نماینده کاندید نایب‌‌رئیسی مجلس شدند
🔹
علی نیکزاد، نماینده اردبیل
🔹
عبدالرضا مصری، نماینده کرمانشاه
🔹
حسینعلی حاجی‌دلیگانی، نماینده شاهین‌شهر
🔹
حمیدرضا حاجی‌بابایی، نماینده همدان
🔹
رضا جباری، نماینده مسجدسلیمان
🔹
علیرضا منادی، نماینده تبریز
🔹
پیمان فلسفی، نماینده تهران
🔹
انتخابات هیئت‌رئیسه مجلس دوشنبه این هفته برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/437540" target="_blank">📅 22:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437539">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyrS0d-rTyiXFqFSzCdx-FOZcsx5uOhQwnUDZp6CbNF_A9G1PQKWaNj3h9UT2nyH6ZL3jJ03ucZVWiRbozOYMATERZUh7AEENsbfHZzKbeT6DwTRItMFNRrUDuKtyINI3RzYPU1hZWN0FCO0A_Yy7y74zhClkW6deTHnhQ9AJzGGti5mfkmLzwBZC1tAnVvwf9KLKJTiL5VcnsOBgmGCxySC0hptdM2YApQWckfNnTT77x5I8lolfUMwmTck49CcXtwKv8yrvhkVtwG5V-SiDrlXyTR8iHTIW7IA6u3TbDCvDE_2x8X_YuVt8aipB4VHd_AYxxl2vmI4FEHlK0EkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد پرسپولیس: تورنومنت ۶جانبه برای انتخاب نمایندگان آسیایی برگزار شود
🔹
درپی مبهم‌بودن وضعیت پایان لیگ‌برتر و انتخاب نمایندگان ایران برای مسابقات آسیایی، اختلافاتی بین باشگا‌ها درباره این موضوع به‌وجود آمده است.
🔹
پرسپولیسی‌ها اعتقاد دارند نمایندگان ایران…</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/437539" target="_blank">📅 22:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437538">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0151919d.mp4?token=HUazb3UZnAVXjCYK9HG1n1Yy5BSSy79Na08r932f-SEhmw5-N6Md8UfEvKefIfgnYdd252dKxHqLi7WUBoIxkRLGVlxBck4lQFGlIjbzFf8ECY3GVyEH3aKT2hcqk02Es5iDMpPXy4Jk1XDflk2EWz0D1De9bDj0kkLOwcaepiCmNUXH5P33yPc9ybYJVSJ8iVvK8RYUaXFPhYvBO-S1EraC2iJx1C6SsFA_3Qwh15DKG2qhFHoQcLmjUF6HFGIYtaMjBwYTOgpoiDldoww9W4OwF-N3CkwU9inyxK4iHdi6sgwII5ovtRy4KRGHRvN2FvlkMYLtG8ML5fVuyjdHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0151919d.mp4?token=HUazb3UZnAVXjCYK9HG1n1Yy5BSSy79Na08r932f-SEhmw5-N6Md8UfEvKefIfgnYdd252dKxHqLi7WUBoIxkRLGVlxBck4lQFGlIjbzFf8ECY3GVyEH3aKT2hcqk02Es5iDMpPXy4Jk1XDflk2EWz0D1De9bDj0kkLOwcaepiCmNUXH5P33yPc9ybYJVSJ8iVvK8RYUaXFPhYvBO-S1EraC2iJx1C6SsFA_3Qwh15DKG2qhFHoQcLmjUF6HFGIYtaMjBwYTOgpoiDldoww9W4OwF-N3CkwU9inyxK4iHdi6sgwII5ovtRy4KRGHRvN2FvlkMYLtG8ML5fVuyjdHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار تجمع امشب بندرعباسی‌ها: ما هم ابرقدرتیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/437538" target="_blank">📅 21:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437537">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcbc0e5dea.mp4?token=FYVi9y3sjWBPvI2icbSAKxmyjMN_UFPuCMACBFeHT4Q6Kddk_TXfKDfzl8tA3oGHr3M2Gi_cM1mXqYUYG2NBNkjLYuQpjiipZbfwk7JleHSFkaou6ivZVvFZNSuPJggeBUb9lh9QwCxUbD-Vf3GUY4R4Lm7XUhsi8TvdnB1qwOUugcKbuFOEI5cS-VJEBnWxIepVEAsR9N5hmRoFPXmB1YniEewGGyNUIwBeFb-13eVtZ4HEU_T_H0-KrPbVpFFIiLxl-JDlJiGUnC-YbEpb9y9o-0GksFbs9-wQ-EwDv5k_1CZOlOil1T1cImM7nyPnV-Ey0RiqhswKB5vUM_EpGnPBcOsSxlA_TWdeqDnWrU_fXt_0HI9IdAo051ohFxHNVSGvEsd7-ZENinzqI-sxyYJD9QMtKCs3xKhzyfmR3HWcNagT4vSbMy3ObUbu0b4HdHTPTjI3UFxNLYaHuhaTksBSxpNl9m9Hquj-M2t7OJDBSGTR_7R7zUCWMXF9a4M44UJeOAe8SFp40mChTRZHV0ouBPfscoSp5A0dwlu4_dAzmzoVJO3-Cyt9X9wugE2fuAGJgFpfx6UMYvl0MZtxSlT6J1kLbXbYbdxL9kLfz0yvU3CEHpeEvOij44mCEUkzYunx_U_vcq8HvYl9W_wGheKPsQFEHa5Ww2_Ejk0JMes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcbc0e5dea.mp4?token=FYVi9y3sjWBPvI2icbSAKxmyjMN_UFPuCMACBFeHT4Q6Kddk_TXfKDfzl8tA3oGHr3M2Gi_cM1mXqYUYG2NBNkjLYuQpjiipZbfwk7JleHSFkaou6ivZVvFZNSuPJggeBUb9lh9QwCxUbD-Vf3GUY4R4Lm7XUhsi8TvdnB1qwOUugcKbuFOEI5cS-VJEBnWxIepVEAsR9N5hmRoFPXmB1YniEewGGyNUIwBeFb-13eVtZ4HEU_T_H0-KrPbVpFFIiLxl-JDlJiGUnC-YbEpb9y9o-0GksFbs9-wQ-EwDv5k_1CZOlOil1T1cImM7nyPnV-Ey0RiqhswKB5vUM_EpGnPBcOsSxlA_TWdeqDnWrU_fXt_0HI9IdAo051ohFxHNVSGvEsd7-ZENinzqI-sxyYJD9QMtKCs3xKhzyfmR3HWcNagT4vSbMy3ObUbu0b4HdHTPTjI3UFxNLYaHuhaTksBSxpNl9m9Hquj-M2t7OJDBSGTR_7R7zUCWMXF9a4M44UJeOAe8SFp40mChTRZHV0ouBPfscoSp5A0dwlu4_dAzmzoVJO3-Cyt9X9wugE2fuAGJgFpfx6UMYvl0MZtxSlT6J1kLbXbYbdxL9kLfz0yvU3CEHpeEvOij44mCEUkzYunx_U_vcq8HvYl9W_wGheKPsQFEHa5Ww2_Ejk0JMes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاشیه‌نگاری فارس از پنجمین تمرین تیم ملی در ترکیه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/437537" target="_blank">📅 21:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437536">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8lSDENN7ZfHB3v-5e2ZvQMtF1yH-1Ek-E0hhzI4VjBOUvRB129W4Q93BSDqVLQKHYIQfoJEvQVyKfewZq1_oPw4dUvoUgpY6kq1SX0IysgYeyFZBP-WzfTj6T33Y1v0ifv48BegoQyq84czc7-SgxbxDtFmCeJUhQCwqdgdpeW3ML792RrQ8HN4DjoHT2T1Ud04SNvVnualR0NSnKKJW_1DMF2-9DWNqNSwJ-F9cg10TVpBgSZ96aD8pIumUjYh8GDvlPS1sBNwkzCWUaOHZy8NYdBAZU6dw2dFhisxgKieRFI0Xjjtgk_qZcdtM056x2bEek3zVdyY3ZSsFr1JSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال صهیونیست: ایران در جنگ پیروز شد
🔹
گیورا ایلاند، رئیس سابق شورای امنیت داخلی اسرائیل:  سناریوی بهتر برای آمریکا، بازگشت به روال پیش از جنگ در تنگه هرمز با رفع محاصره علیه ایران است.
🔹
ایران در این جنگ پیروز شد، شاید پیروزی با چند امتیاز بیشتر اما این یک پیروزی آشکار است؛ آن‌ها می‌توانند از نتیجه جنگ رضات بیشتری داشته باشند.
🔹
آمریکا در تنگنای آشکاری گیر افتاده و در نتیجه این امر، اسرائیل نیز در مخصمه بزرگتری قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/437536" target="_blank">📅 21:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437535">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
آمریکا زیر بار هزینه‌های جنگ؛ ضررها ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/437535" target="_blank">📅 21:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437528">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAYQFYaCw9MSMD4uOaDTWT0hQ-bS_NKcAZyydRSEdsyp470TVUFZgDNRT_yfe4Ipk1vfYmmMqXTyjcEueiXw33wvNamLKLUpa4HmK7r5VdRss9iRG0GdtlIvesU1EENXMc0VZLHBTbM90DjDwvifRsiVtiUsSVPVGOS_TxU6V-4MjK2Z36X96lWjkA1CFQmm1SXWc6ouCk2o_EeDOtgVFVA6ri84tsz5Pf3OMpYYZ9uyrJFp87c1sv43-EAQ5Geh8-zTRgXwGKP8vl6ufJFYvzvbUqr5VhbdfOOS9SI1kcXZP-I5N9e5cPkZ7lDD0y8LuhebVhmnydM9V8rse5QS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1sJoGPvQouELgC7YNo2g3QpG5UsomRVzwswoE_W8fRgJAF7cHb2mrETEhXEPOuLkBsXQdI46-2rcCbkUz_wOTP1lzS7AXMq5cvLfqLnlor4FsGK5kMyU7HVfnpDUjCGc98XwsBGdSvI7qg8KUAF48acvaIOMAzLx_kOCJp9RW-8hjcd6rlW9DCCsMBSVga0HC4ju4x85BTBaWdy3GvOXdhGh4RA42TzzxchyeIMadcU0oONnvqT0iU5-kX1A2HBvP2TcJA97pUgqZ9m1p756MQU16jsbBgtkOsKBuMybDRGMXfpg9GeRMdl0RrO5CC1-cU_HSQQGZt-odVpeOckyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9ebEWu4TiD2C2RUbxf8NNQ2HOYVr-G_Mp7gIB855yNmx9Ws-q7LWMV4VQ-qNIpBNg-A5Awwps2sPLNxgPpIqkIRMoQfmTxGfjmihK-vdUvq2aw2Wy62QAcADHdT-epPVpXoGdgQ-eZqXYTXNatohiLutwaVRusj7uUkWECrLoFkTOfjiYT8ZTytiWANByhHPCBBkNd6lYAbYF_ZSL29E4wF0PO4BBcewH7VFXhBH29WzC3QpgOtMLWW_70TEvNJAOVUrtpZGLy_0aQUcnmWss7nz7ge_UHkk7pNEEqNakoaamM4RXtmhx3-52BHsUXig2N5C1T3IfeXPAtFq3O_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNpAoiiBymldUaOHNMgypqD6qysfCb2QqmLT5UrHObILHT-UEHCYLrZqXjLLmc4mZctMnpFJO45djVmYuqWU6goa0mlu1UxF5biYPhX85q3CJx6dHTajVKh4K1g3ZF-8oXutQhhhsmcFvuDVNjiQs2tQfAOMF9Bwd_3enHiecmrNu6dc4UBnN0xJMkmCTA1GzQAWu-te3HFDLwbXBApEMZh-bRZf83eGKEhhOTbG9Oag71okrMp29eWMEQTKdeIuS3dgl1kQtxn04C-rfp-gpYTNZA6rvfFOS_sBd_YenTZu5BQkBtgW9OT8c8I5QMlNaz8NHS3GqP23kvBExje9jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ln0w_zv94OFsEN-c7-GObYREY_RGkrrtq72EfpPHO2B76_YADt_B-QDQe7L2HCuiLdm7SxH44A-nk5T3h5d8jckQfuT7dm8U17Ni2Z7cWAh-F_yEE-l0RfmAXY8rXUQP7Vbd2Odzx1CGrADduDfV-qIizUQSUScCGRImzNSVxaq1WIciqJrkhRupzpyya8ZHKp9daKVgYiR4-Zq_6gJq663f392T2dF5L09k9Pd4D54tC-QTORuCJm-zR7656kg-uAqCCPwxoO4sIvSC1TSsVM0fzYP8yWmtsVTS2wgF589jusigIRFxf54ttyqv0ds4Lcgl5zlx7iGS5r1uC_pGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FtpfGI9FSGabCu5WMcpjaKpWGaxXc9wTpOT5kqqGuswicEu_oCsowxy8ozsa8HjzHTaFTuA3bSfR3gniaeKJh85A_F25XjrMbFE9AbI7T_i4wAPFSFYi8kuyqAz92kgiVHvC87lX-N1j5aXYUWfOeTvOdQgy0gVTe-osLjE4PXIBPUXx3s6kkdeRWQe606EkxpmLSN1KtBaGdhPTPltnYgThHxz5BQ53GL268QRsiNYo4P8p8R76SX1eLDqExoxKMc7iPUM29dw_E2HAsBcSbqFiX_oDdHNo6BUB-Hki4nIyuMpZegTgKpYS6iSSRjxLPEVc7V4T-8nWkRomYKaFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MPZg4rijt__HSToI07e_R9e8v77FHg-0lVoUJa3vbtHiuIzq7U2SJQZwq71pKykLqz3dVDAIdPs8B_CsJ_Ndk0_1HQkNizhSRFbqkPLijUnTa_jA8-KR6V6KFPov4MBm9H7rVXOACYmaKL5j_33cMmyKfvd6DYq-ryHIa1uwtQ5geB2JzJrhDc1Hx1qv1IKWhwmEuXSBGYTccjSyFOoegbxEoVheKIGNmbOdkpHQVhkD1aTvtzXjDqTffmYaESjMGu_JmmMphBPNPOxVUfYVhAwsd08jykKmO45GV4gxk_Ypc_fQTHEpezHROsTvqPBEwpziVyvTRDlMlBg9PJCdKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازسازی
کنیسۀ عزرا یعقوب
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/437528" target="_blank">📅 21:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437527">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTEHsNSXQZRl5E8Qdrr8tq2dGjviwWP1K3ZB9xVue1JE6lcp-9fWSilJINFxELsZRq8u6643GN3H9KUWpPz0IwRsThfNFsStPwDCa1RGFZjRZ2Wp1A3qjdHGiKGOuNbapDFEO8gyhjlOC5bIXXErDhbghNhBO8AMu2SNilQyh_7X_5aBtbIEjxGYScM5cyR6pNQbNm8T5Tgzh1Z4IGdARNfj9D9rRqhCRQuceigMUma8sd87b4GUFIKnqjUj3OlLLFlR2-yDC5DT8ScpUR_6hozmKV2msWJIFMvqZyWGk3B9wHRr8yUX3y3sL59ZoxJLqLhaxpCOcUjh6ZRSXzbkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ملت ایران، تجسم داستان‌های فردوسی
@Farsna</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/437527" target="_blank">📅 21:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437526">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0m1aFlFUXAGXhtMKHf04cPayYknWRCKXWgdnKkzXPA_yETfK6OC2Z3yMmv1xfahAvvs0MCUqjk-SnptYbwIkg6KkD45FY2o25umwf9wasHCtkCWBTNyRJKou0opHBCfYpYLxVemk-qGgm2Nhfjp49PiH5tDIwvpUgf9ni1Rwp39Wl6GiQKcNwRnB8sElCkc7e0lxO-j8QoIm8BOnPOfmdwF0GBQ-WaZySaymolMeTm7dIgRPxPZIEYQCoMq6kldEeJJfD9fuLnmT32_sfgMxJEjuPCCG1GkkdQFIMtWtyEG1Il44YGfYWwEClDq0mxL5aCOpEiABXbOnF1A7HTISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در مصاحبه با کانال ۱۲ اسرائیل: اگر توافقی برای اسرائیل خوب نباشد، آن را امضا نخواهم کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/437526" target="_blank">📅 21:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437525">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رسانۀ اسرائیلی: تفاهم میان ایران و آمریکا به ضرر ماست
🔹
شبکه ۱۳ اسرائیل: صحبت از مذاکرات پیشرفته میان ایران و آمریکا درحالی است که مسائل حیاتی برای اسرائیل، در این تفاهم‌نامه وجود ندارد.
🔹
اگر آتش‌بس بین ایران و آمریکا به مدت ۶۰ روز تمدید شود، این کاملا با آن‌چه اسرائیل می‌خواست در تضاد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/437525" target="_blank">📅 21:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437524">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎥
امسال صاحب‌خانه‌تان با شما راه آمده است؟
@Farsna</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/437524" target="_blank">📅 21:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437523">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iglnke4HmFiwHkoel9i28sQSg7WbLFIvTXsXxcXngWiuVnSnx7fySAtbZmjpQ2Ap7cZdSstBPYn46LH4gIUXTMsd6r5oTzMP1aJmYZMR3WnYS0jfe-MLHc62t-s7jXE8Huf7BjX6ZDVwDHNeETd1V87BEN8Opdd5y5q07llMX45rQNpNZMsvU7ix41XTLiarDUY-mUUyNrgP2PdnXjLnuJ0AqkRe2F9H5IITyqySubuUM57ZJbWjY5gHxqrmnKIiPWRd7ghMZfRL_Zb9ZJ_bgBIFB-2p9UNjkuRF2IGDQ7gmrYdSI2g8l28qDnFJjtw-citjr820LloRiWGSbCZNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گام بلند بانك ملت در عرصه تامین مالی با عرضه محصول جدید «تیما»/ ۵خط كسب و كاری مهم كشور تامین مالی می شوند
🔹
بانک ملت با عرضه محصول جدید خود با عنوان «تیما»(تامین یکپارچه مالی ملت ایران)، گام بلندی را در عرصه تامین مالی زنجیره تأمین برداشت.
🔹
تأمین یکپارچه مالی (تیما) به عنوان یک زیرساخت جامع برای ارائه خدمات دیجیتالی اعتباری مکمل فعالیت های گذشته طراحی و عملیاتی شده است.
🔹
تیما پنج خط کسب و کاری را شامل تأمین مالی مصرف کنندگان در عمق زنجیره تامین(تیما لایت)، تأمین مالی غیرمستقیم پروژه ها (تیما پرو)، تأمین مالی از طریق لندتک ها (تیما لند)، تأمین مالی در عمق زنجیره تأمین برای صنایع سنگین (تیما پلاس) و تأمین مالی شرکت های توزیع کننده و پخش (تیما پخش) پیگیری می کند.
🔹
تیما با تمرکز بر نیازهای مختلف زنجیره تأمین و با هدف حل مسائل مرتبط با زنجیره های تأمین عادی و پروژه محور به بهره برداری رسیده است و افزایش قدرت خرید مصرف کنندگان، کاهش تأخیر در پرداخت ها و کاهش ریسک نقدینگی در عمق زنجیره تأمین را به همراه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/437523" target="_blank">📅 21:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437522">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#ببینید
آنونس معرفی منطقه آزاد ارس به ۸ زبان زنده دنیا
همزمان با روز جهانی ارتباطات و روابط عمومی، کلیپ معرفی منطقه آزاد ارس به ۸ زبان زنده دنیا با حضور مدیرعامل سازمان منطقه آزاد ارس رونمایی شد.
این اثر توسط اداره کل روابط عمومی و امور بین الملل سازمان منطقه آزاد ارس و با هدف معرفی ظرفیت‌های اقتصادی، سرمایه‌گذاری، گردشگری و ترانزیتی منطقه آزاد ارس برای مخاطبان بین‌المللی تولید شده و گامی در مسیر تقویت دیپلماسی رسانه‌ای و توسعه ارتباطات جهانی این منطقه به شمار می‌رود.
منطقه آزاد ارس؛ دروازه ارتباط ایران با بازارهای منطقه‌ای و بین‌المللی</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/437522" target="_blank">📅 21:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437521">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/437521" target="_blank">📅 21:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437520">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee30731dcf.mp4?token=QnbeV9Gt3e8geBeTQRlkzDJVLyMJhX4yRgjs7FjYOeQhY0dgxx9z6qE9Q8WDpjpBX_Q_lmU_4qubzwgjI0LrxzX8ZROFDaIVdjDYdnthDAst4Aac7ttHi6bVb9fJqhcfw1vFNoyx7TZA7mx1xtC93AS7mxTrNrR-2Jql6d_VCFePaP_F-OmZeNjRS0Kdu1IVcF1cv48yl4UD8YSAmOjnFn1aZY08Dnn2GcZBXYuZ8sgtuxpAhYaEyQ_aEYka5CiJIuZ7H4FKojnm-rnNSDdkf1tJp6M8j52D2kvhxHp89SYZuqx6m_pJWqY73Ht8WHpITQ8uJ9xa0cBB-nMnGvANAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee30731dcf.mp4?token=QnbeV9Gt3e8geBeTQRlkzDJVLyMJhX4yRgjs7FjYOeQhY0dgxx9z6qE9Q8WDpjpBX_Q_lmU_4qubzwgjI0LrxzX8ZROFDaIVdjDYdnthDAst4Aac7ttHi6bVb9fJqhcfw1vFNoyx7TZA7mx1xtC93AS7mxTrNrR-2Jql6d_VCFePaP_F-OmZeNjRS0Kdu1IVcF1cv48yl4UD8YSAmOjnFn1aZY08Dnn2GcZBXYuZ8sgtuxpAhYaEyQ_aEYka5CiJIuZ7H4FKojnm-rnNSDdkf1tJp6M8j52D2kvhxHp89SYZuqx6m_pJWqY73Ht8WHpITQ8uJ9xa0cBB-nMnGvANAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس فدراسیون فوتبال: کمپ تیم ملی به مکزیک منتقل شد. با این اتفاق مشکلات روادید حل می‌شود
.
@Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/437520" target="_blank">📅 20:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437519">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎥
محمد قربانی: به‌عنوان سرباز باید برای ایران بجنگیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/437519" target="_blank">📅 20:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437518">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎥
جشن تکلیف فرشته‌های ایران در میدانِ خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/437518" target="_blank">📅 20:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437513">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IckWyR1f_f37vLIswlhdFbeK6SdUsCa8d_I6qKgvxX-gRYJme7DfabGWXDwsZxqQxTD96_1w4PGZ6EC68xOD5VYubzDRnwVPsr2BKiIPHdMRVVfmbZ5g9Q1fxuyfBFxqJQE3nHCFD4igJihkBMPK6bWOdVA-NS7DUOX96W3IMNa7L89Yk0nwfvh6_CYF_iUTPNFHEDAIQUpF2J5f9KQk_Jg_CxwNSfzKyqlQQdOz_Lc4S8H1UGDmbI4N6G3cJLxuI7yvmrlfj9FVyLm0aTZkz7pXoNpqX8Pd2Q3rrq2IhPhBq_AGWfz7BEZ_oTQNdFM4CwsQBlDz7eQ3rqCLgiSITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avEut572d2-NLFoMj4O8fGmzldRUEo0cbOngACF7L9UfaRNiu-ubdawAH6sSAY5q4wi-8QnHiAWuyIWYQDnqXtgBiPiFxigbwEUy4nL6a2pP01zoSJYRodafGC2WCgNOXivu88-nt1sGtzIMuczObEpmn5hbR-Fb8YmSyJkieb8OAKSEELj17VzTFz9f0gaM_YLXyN6J0zQ_Qp7FjW8JqFeK9WvGSAAo0fl1JrkqR4OVHQ2lCDgAj1O73HN0IxMmRI-dqD0fgorS9VpTsVH8RcFks2irWh0kQ5_zMpBdiboFZy7JKkgBOg7aDeSz9fZgdAwV55j_GfGVabQmL9hlHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgfSGRgzsW3ydTb_jk5zbpyJGS6JGh1Uth9Tti3sdKEfX3leNol2ZzZU9dfB3L5Op9fQSW1bymnL-DHAMEZvz0R2mATJIobpxWlaTqfR-TIFH7er_hKYR1PboE09u3M8fdI6XJRKPbJyB4GvAnx2o-tU16gLlCr2ZUpXwlh5Ze7zWD70-WwNypQ_VPUhtbhy1q5OClFX04hdH0tsiQONtpQWkSyyzwLvyl7kh848xEgYcsh8W4CsW84EnuI8E2gXXQLKnufL9k6AEl1eZJlNol7DOpRNNXJLKNwY1CEpLQ946Ee3xusGRUHmeoEAXe6BjdWOtUFS8Nys8th97SlrtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tno35a_gwGcIUMcvtr98uy63lNvNNWDzNisjqlIB9iQukqLCfMDz_KoZPhi36D_MEHtJqf1ucvCEKEZDgNsLjUuxrGSZeXM83vFlGRwHSQZsMv4SnoOrwNOCcuBIWC7_1K7Vcd5VMTjCSwAFmTJi-Q-RelVHBfr6CViKKjWS1ZfW8zTrQw6YuKER1RoxK8cydE9JThDSzFPShACwVWIAuxRxbygVC8W0VRe1uPzutRf4fISMn5yryXhtXuYcN_NZ9Fh_lDngQlU-pU5HLc3P9DY6QoXF1cTiSmcwNOYUcrToILqJIvsKT8jBTSCUZm8GpJL8dCjde3AmGm71Nfo07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsskEcJ5oEn3BcAsC1RhGNbGzVjlcp5sJPOL0PoTIU4QJZu57ScpjdtSnWzaXw0iunpjWF6uyLdYRbkUXfKIxpB3XpIcd1hbadrlsHYGCcL596M0WqkxA5513Cfko_IvC7fkF1Iy20s-kukXTJsRt3Y2-EeGPhiKLYNuDTYVvJUrDOpN2X99oWxL4BTFZh-Bcr2nQUpy6-w-CYB6d254tDv7uAKSHDWGhOEtlBWYjZnbmgNCVcAh0RLXUWNb1gk2W3Lg1XOZHgfoN_JJ7YW1NyeHgNu3UCtuoTEMCDcpXC8aZ12WspcvDo8noIpztFhHEerR7Tf4E2lMo-mTbrrfCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت حماسۀ سوم خرداد در چهارراه ولیعصر(عج) تهران
عکس:
محمدحسن اصلانی
@Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/437513" target="_blank">📅 20:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437512">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00dd641236.mp4?token=Ix-3tjzt1S2OFy0FYIIyb11pQ0flhkSD2TZtiIPHBU3taNXSTM0dO22Pl4EGYTt45JUEpy_oR_-UnfGlCJziv5Ysgpv6RHiewTf_yx2XWvF6PBWYeX1eCvDMPv5m3HTnz2zDupLdYm0mCJGb3wpjmt42GdaIolgyuUnT_I61OI4_-7-ejue3v80loBsC8-7WnsM_qi8ijav3ohCOdBPZ-1uzuzU2nEK5zJ_T8tD10htI0mJSppzlaRBCXXY9MtMnWplysuogfQMbJ_o53nlBT0thkkohf9az3cfRPqY4OMntgzHyd6xrEklIioA2BwBe3VNKZbW9bunQOhOFH-jv5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00dd641236.mp4?token=Ix-3tjzt1S2OFy0FYIIyb11pQ0flhkSD2TZtiIPHBU3taNXSTM0dO22Pl4EGYTt45JUEpy_oR_-UnfGlCJziv5Ysgpv6RHiewTf_yx2XWvF6PBWYeX1eCvDMPv5m3HTnz2zDupLdYm0mCJGb3wpjmt42GdaIolgyuUnT_I61OI4_-7-ejue3v80loBsC8-7WnsM_qi8ijav3ohCOdBPZ-1uzuzU2nEK5zJ_T8tD10htI0mJSppzlaRBCXXY9MtMnWplysuogfQMbJ_o53nlBT0thkkohf9az3cfRPqY4OMntgzHyd6xrEklIioA2BwBe3VNKZbW9bunQOhOFH-jv5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدف‌قراردادن خودروی فرماندهٔ تیپ ۳۰۰ ارتش رژیم‌صهیونیستی توسط حزب‌الله
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/437512" target="_blank">📅 20:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437511">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Djymox14ks9KyXG2Ql3J6dkdp5vcVvE8LsRG3tfVqhaBfPKMnAhTNlRAdjg17mVgynCL8OZTafMgrTMRkJwL3HBgTjk8TRHkO5w-h2TjkZrykD2WEcU-I1XCB-7YdJ6mCZHvMikLWAi1_4XoLMaEJWyoVmKlA-nNUcmWIWWOcX7QtmUPBfgjdf5Hilxam1EuS5GCaGWa_6zTtSNb5f9bKJ-Xxnwf3KhjBK7vWKx0GwQrJvv3hA-KUXV4yhm6leOrO8ks4Tp-KgkR--fXBPJepStLGFQ4ziQSJgcKn9HYgVKkMekZ8dg_h3PZSplwCnjwxGyTw6sUUY8lHh2rcUw1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات آمریکایی در مذاکرات با ایران: به توییت‌های ترامپ کار نداشته باشید
​
🔹
شنیده‌های خبرنگار فارس حاکی از آن است که در جریان تبادل متن با واسطه بین ایران و آمریکا، برخی واسطه‌ها و نیز مقامات آمریکایی مرتبط با مذاکرات، با واسطه به طرف ایرانی پیغام داده‌اند که «به توییت‌های ترامپ کار نداشته باشید».
​
🔹
این مقامات تأکید کرده‌اند اظهارات ترامپ در رسانه‌ها صرفاً مصرف رسانه‌ای و داخلی دارد و موضع او در پشت میز مذاکره کاملاً متفاوت است.
​
🔹
بنابراین گزارش، ترامپ گاه‌به‌گاه با توییت‌های تهدیدآمیز در تروث سوشال سعی در جوسازی و گرفتن ژست پیروزی دارد، اما آنچه در مذاکره واقعاً دنبال می‌شود با این لفاظی‌ها فاصله زیادی دارد.
​
🔹
در همین رابطه یک منبع آگاه به خبرنگار فارس گفت: موضع اولیه ترامپ در بیانیه موسوم به «پانزده‌بندی» اولیه، حداکثر مطالبات و آرزوهایی بود که حتی در جنگ هم نتوانسته بود به آن‌ها دست یابد، اما آنچه اکنون روی میز مذاکره قرار دارد کاملاً با آن مواضع اولیه متفاوت است.
​
🔹
به‌گفتهٔ این منابع، ترامپ متوجه شده است که ایران اهل باج دادن نیست و موضع ایران را درک کرده است. از این رو با واسطه پیغام می‌دهد که این اظهارات صرفاً برای مصرف رسانه‌ای داخلی است و نباید به آن توجه کرد.
​
🔸
گفتنی است یکی از ویژگی‌های ترامپ، استفاده هدفمند از رسانه در مدیریت و فشار سیاسی است؛ مسئله‌ای که مسئولان ما معمولاً در آن ضعف دارند یا نسبت به آن بی‌توجهند.
​
🔸
اما این لفاظی‌ها و ژست‌های افراطی که او در مصاحبه‌ها یا شبکه‌های اجتماعی خود مانند تروث سوشال انجام می‌دهد، عملاً به مرور اعتبارش را از بین برده و اثرگذاری واقعی خود را تا حد زیادی از دست داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/437511" target="_blank">📅 19:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437509">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71bd7a603.mp4?token=OySjp1YZDYi_lSGV88wbWBEgXSieaTyu8_yh3Rxa2Xsjw60go6KwducpjMbePNa8KY7qKlRdb_1Sd0RBveadKY3mhKRkZcaDq6O0L7pHJTsJqMg9spwz20Ly6f5Y9-u1eAkBjgEqgCZQNoFOdk_tJsunkPyydVHcc6rWI1NpVPfZ9RyR5yRsi089tJOQK_TUg2FGbZZ0CXJjmLXUkVjcIBCnpbUw1r3HW8SGwVuy2mkeE-r3deTmwVhm-xrJghCDrQhQh09ZiDipkArAaBnDAl71wJmVtHDYd5BNxCP304ug5qMBjXxvNUrt6OYL43GFe5KJ6k58HXo6OwinPZaMfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71bd7a603.mp4?token=OySjp1YZDYi_lSGV88wbWBEgXSieaTyu8_yh3Rxa2Xsjw60go6KwducpjMbePNa8KY7qKlRdb_1Sd0RBveadKY3mhKRkZcaDq6O0L7pHJTsJqMg9spwz20Ly6f5Y9-u1eAkBjgEqgCZQNoFOdk_tJsunkPyydVHcc6rWI1NpVPfZ9RyR5yRsi089tJOQK_TUg2FGbZZ0CXJjmLXUkVjcIBCnpbUw1r3HW8SGwVuy2mkeE-r3deTmwVhm-xrJghCDrQhQh09ZiDipkArAaBnDAl71wJmVtHDYd5BNxCP304ug5qMBjXxvNUrt6OYL43GFe5KJ6k58HXo6OwinPZaMfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکار ۲ طلای دیگر در الجزایر توسط پسران پاراوزنه‌بردار ایران
🔹
علی‌اصغر ابارقی موفق به کسب طلا در دسته وزن ۹۷ کیلو شده و با ثبت رکورد ۶۵۳ کیلوگرم به مدال طلای مجموع دست یافت؛ مبین محمدی نیز در این دسته موفق به کسب مدال برنز شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/437509" target="_blank">📅 19:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437505">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تازه‌ترین اخبار از جزئیات مذاکره: آمریکا انعطاف نشان ندهد، مذاکره شکست می‌خورد
🔹
یک منبع آگاه و نزدیک به تیم مذاکره‌کننده: آمریکایی‌ها اگرچه از رویکردهای اولیه خود عقب‌نشینی کرده‌اند و بسیاری از مواضع ایران را پذیرفته‌اند اما همچنان ۳ موضوع اختلافی جدی پابرجاست که اگر حل نشوند مذاکره انجام نخواهد شد.
🔸
اول: موضوع هسته‌ای
ایران اعلام کرده که در این دوره وارد مذاکره درباره موضوع هسته‌ای نمی‌شود. تنها در صورتی که طرف مقابل شرایط اعتمادساز را اجرا کند، در دور بعد درباره مسائل هسته‌ای صحبت خواهد شد.
🔸
دوم: پول‌های بلوکه‌شده
پول‌‌های بلوکه‌شده باید واریز شود؛ شرط دوم و اساسی برای ورود ایران به مذاکره این است که پول‌های بلوکه‌شده ایران ابتدا واریز و آزاد شوند. بدون این اتفاق، اساساً وارد مذاکره نمی‌شویم.
🔸
سوم: کنترل ایران بر تنگۀ هرمز
اختلاف دیگر بر سر نحوه عبور کشتی‌ها در تنگۀ هرمز است. آمریکا تأکید دارد که تنگه باید کاملاً به شرایط پیشین بازگردد، اما ایران می‌گوید فقط خود را متعهد می‌کند که تعداد کشتی‌ها به وضعیت قبل بازگردد. معنای این حرف آن است که ایران با مدل ایرانی خود، تعداد کشتی‌های مجاز برای عبور را تعیین می‌کند و تنها به تعدادی که خود می‌پذیرد اجازه تردد می‌دهد. این بدان معناست که کشتی‌ها باید تحت مدیریت ایران و دقیقاً از مسیری که ایران تعیین می‌کند عبور کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/437505" target="_blank">📅 19:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437503">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ستادکل نیروهای مسلح و قرارگاه خاتم: برای فتح خرمشهرهای پیش رو آمادهٔ جانفشانی هستیم
🔹
نیروهای مسلح مقتدر جمهوری اسلامی ایران در پرتو توکل به خداوند متعال و با حمایت مردم غیور و همیشه در صحنه، بدون کوچکترین تردید برای فتح خرمشهرهای پیش رو با تمام توان در برابر دشمنان آمریکایی و صهیونیستی آمادهٔ جانفشانی هستند و تا پای جان از ایران، ایرانیان و نظام مقدس جمهوری اسلامی دفاع خواهند نمود.
@Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/437503" target="_blank">📅 19:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437502">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f382a16c0a.mp4?token=RXdRnfTk_Nz5KznlwHuKn_7g6vg2M8nJAHdlP8vQSA0OWY234cE23TabO_2KIlJTZ0tQ5iNW3LCDJSAn-Jj4TZyT0Ck41Ab1VREn0bTVn_OwPbE7eb_JOz4LNOY6nunao2GHYqc_sLncBcH739wCNM2c0OErKOYzEYcaa0pZ1iok7k648SwU07z18PDHrJqmGvgskocTww9AP_idEaO39Cip5G0oTNKRQ1hAP5rRb_Az4301eu22vQUFHGOqni3jSeHxGsn6ftDBzm6yW3JMQR36ghKzsGaJ8hrq5ej98J4Ccy9roqN0KXK2lcJ77ynMLD_c83b8curpQBIaqDxIqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f382a16c0a.mp4?token=RXdRnfTk_Nz5KznlwHuKn_7g6vg2M8nJAHdlP8vQSA0OWY234cE23TabO_2KIlJTZ0tQ5iNW3LCDJSAn-Jj4TZyT0Ck41Ab1VREn0bTVn_OwPbE7eb_JOz4LNOY6nunao2GHYqc_sLncBcH739wCNM2c0OErKOYzEYcaa0pZ1iok7k648SwU07z18PDHrJqmGvgskocTww9AP_idEaO39Cip5G0oTNKRQ1hAP5rRb_Az4301eu22vQUFHGOqni3jSeHxGsn6ftDBzm6yW3JMQR36ghKzsGaJ8hrq5ej98J4Ccy9roqN0KXK2lcJ77ynMLD_c83b8curpQBIaqDxIqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آذربایجان شرفدی، پهلوی بی‌شرفدی این‌بار در میدان انقلاب تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/437502" target="_blank">📅 19:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437501">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
ترامپ به آکسیوس: شانس توافق یا از سرگیری جنگ با ایران ۵۰ درصد است.
@Farsna</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/437501" target="_blank">📅 19:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437500">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c39a99ab7.mp4?token=Zl2Dal5zz_2CEHDRjo9O9r1ov5eHbpQ6AatAXiozwc9YZ0NxaVP_6OqE2KlG-mHp8a4ztxSc2CIwPyUkFAJaGgu4DLtamUogHGW_JNqZIeGvqiDmq7WeMfrvMuoJw6I000W-mBfvWM5Q25iJf3gLdGgP6xj1_0C1qj_FBuysvV8B-quNN0g73JAN_DV3VMYVL4fDFlrkHRI30WXKYkbDAYs7ckdTOhTriXzeji6eVIlkgAPz8KUkzafqc16gz8Xj-3iU8o6XaIanCPYOPjwgrvnH3UJXaFTskbPndLdIpg0WYxGVibZMPQczyT0qDgyGuaPwsTuHelrTrmblFyQDZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c39a99ab7.mp4?token=Zl2Dal5zz_2CEHDRjo9O9r1ov5eHbpQ6AatAXiozwc9YZ0NxaVP_6OqE2KlG-mHp8a4ztxSc2CIwPyUkFAJaGgu4DLtamUogHGW_JNqZIeGvqiDmq7WeMfrvMuoJw6I000W-mBfvWM5Q25iJf3gLdGgP6xj1_0C1qj_FBuysvV8B-quNN0g73JAN_DV3VMYVL4fDFlrkHRI30WXKYkbDAYs7ckdTOhTriXzeji6eVIlkgAPz8KUkzafqc16gz8Xj-3iU8o6XaIanCPYOPjwgrvnH3UJXaFTskbPndLdIpg0WYxGVibZMPQczyT0qDgyGuaPwsTuHelrTrmblFyQDZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش سی‌ان‌ان از «ستون فقرات اقتصاد دیجیتال جهان» در تنگۀ هرمز
🔹
سی‌ان‌ان در گزارشی توجه‌ها را به چیزی جلب کرده که کمتر دیده می‌شود؛ شبکه‌ای از کابل‌های زیردریایی که شریان پنهان اقتصاد دیجیتال جهان محسوب می‌شوند.
🔹
در میان این مسیرها، دو نام بیش از بقیه…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/437500" target="_blank">📅 19:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437498">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMrKWPSSjkW1oNhRQxaWJC8kSVVoI84BP1L1ltsVNVFaZHGgcHCc_S9YC4J--etmautEfEWGBmhZJmb7Sk1n4N4NSLiD380RwWU3hVMfCgb4vAjOGF9jTqX7Jx_wB4wt6EcbEpDtxYIPTafKLfNwHBTgKU9_oVTt_Q2tCbOMYZ9XAPC5O3MEORxRyDVbhptQIBiTZ10wzNmFAY9g-Ys3SQeFrgKWeA1NO3NHwWeEZ0V5PTq38KTkCcVy1M_heSa1DiCZaihbU90SuA2Oz1o9zmT_CsuRCaKnriXyd_4scoy56HHwmuMGtFie3cd9CbXLMoOQ-F5JAE3qpd3tPsksSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامهٔ هنجارشکنی‌ها در موزه هنرهای معاصر
🔹
انتشار ویدیویی از تک‌خوانی زنان در رویدادی در موزه هنرهای معاصر تهران که یکی از مکان‌های رسمی وزارت ارشاد است، خبرساز شده است.
🔸
پیش‌از این نیز فیلم «تهران کنارت» با نمایش علنی رقص زنان و پخش صدای آنان، گامی را برای قبح‌زدایی برداشته بود.
🔹
از منظر جامعه‌شناسی، این اقدامات طبق نظریه «پنجره اورتون» انجام می‌شود.
🔹
در این نظریه، جریان‌های ساختار‌شکن رفتارهای ممنوع و تابو را ابتدا به بهانه آزادیِ هنر به سطح «رادیکال»، سپس «قابل‌تحمل» و در نهایت به یک امر «عادی» تبدیل می‌کنند.
🔹
برخی معتقدند این رویدادها با اتفاقات سطح جامعه تفاوتی نداشته و برخورد با آن‌ها حساسیت ایجاد می‌کند.
🔹
اما دیگر کارشناسان می‌گویند «قیاس ناهنجاری‌های پراکنده خیابانی با اقدامات ساختاریافته در نهادهای دولتی، یک سفسطه آشکار برای خلع سلاح حاکمیت است، رویدادها باید فرهنگ ساز باشند نه مرعوب اتفاقات خیابان.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/437498" target="_blank">📅 18:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437497">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poEm3GUWwom1WI3MHnoO_97jkKuoMXqcmLnmVyvmT9-Kox7UcoOsV030tFrqvNZdhujg1fNM-X5mKJOhlm0gkCzeINkuGmtQ96vlL5tg-WcpDuWImyQTzaRshaqs519kHMU7iCQw126bMcwvC6JMagOhOoArqUtCS3OojJUpHU6-heLcpjxiQOdBQnrqGcnwr2SCEllhr743VPJRJM8UcB4gQ0zXFbsTxeB1Atqr0KaCXeDjK4mu1C2uM1sP0bvUi-9VNGtXxEEU0gkXpmYZyReZyeMQBjLB8WvHiVYt4-tW5BCp5oVd_8UxPcwAyM-knpWVwYLEi_WZo8nRQq_ivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف لاشهٔ یک پرتابه در چهارمحال‌وبختیاری
🔹
محیط‌بانان منطقهٔ حفاظت‌شدهٔ قیصری شهرستان کوهرنگ چهارمحال‌وبختیاری لاشهٔ یک پرتابه در ارتفاعات قیصری را کشف کردند.
@Farsna</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/437497" target="_blank">📅 18:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437493">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در بندرعباس به‌مدت ۳ روز
🔹
سپاه هرمزگان: عملیات خنثی‌سازی مهمات عمل‌نکردۀ جنگ رمضان از فردا تا سه‌شنبه در حومهٔ بندرعباس انجام می‌شود؛ مردم نگران صدای ناشی از این انفجارها نباشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/437493" target="_blank">📅 18:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437492">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WduLIStrIju6YxZgBGnCYiEo3kHHtukmD7BcNWZxpv38BgU7QZIzC4I7Qo87CdPOPB2I8l6TAgC3rEcYspBfWfzsPA3A0s9F1xbMifydHjVDjdzRS06utf0-8UjYB2dqZ0NW_qG3Ay9kmy5xVh2eSCIw7uXNpwlMv98vHMGfCH22dgcZw-FrspVqKHOz41YeTR_nAtWvfluH59ZAPQEDmxNHOwYwyYkaKmbb_N-xKliabDeyFxc5XF9QbgrnGQ5GVvl6SJWG1toSHraAowZZhKpEXDxk4UPNQoXaVXRKxu-j-YFwUDbeEZgrDfUbqfZ3RpDRQ4GneulV19QBTkslgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۱۵ پرواز روزانۀ خلیج فارس هنوز به آسمان برنگشته است
🔹
بررسی شبکۀ الجزیره از داده‌های پروازی ۷ شرکت بزرگ هواپیمایی عربی حاشیه خلیج فارس نشان می‌دهد این شرکت‌ها روز گذشته تنها ۱۶۸۵ پرواز انجام داده‌اند؛ این در مقایسه با آمار حدود  ۲۳۰۰ پرواز روزانه پیش از جنگ علیه ایران، کاهش ۶۱۵ عددی را نشان می‌دهد.
🔹
قطعه قطعه شدن مسیرهای هوایی خلیج فارس، افزایش زمان سفر، لغو پروازها و کاهش تعداد مسافران از پیامدهای این بحران است.
@Farsns
-
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/437492" target="_blank">📅 18:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437491">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-44.pdf</div>
  <div class="tg-doc-extra">5.9 MB</div>
</div>
<a href="https://t.me/farsna/437491" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-43.pdf</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/437491" target="_blank">📅 18:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437490">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8gv0NkzrR7cMfY8cn87hV-ifBiEROxvp1zTnklJIeJbW7jm3Tgp8lDVeHu_I9DrpAjDU6qZ0j3sjCRzPXz_1KlJllDpOsGM2pcZDLXr30QAu_TtOSqirZnAKiFTd1JzTyyY0X9cYcHDtxeO4-ASYLlVAD0_IJXyH8hY1GCpK496TvOUTZg914vWcjmnRp5gwMdQc2pLQZqkMnZakVOGCPwBin3B4FkHt4jHAHtVdcchJTYOjHndan31EAA-YLE-0GixMX0-jOH_OSFgatFexcUhMuiKKT4OM3Puxl7_rUmnpO5o0uUIqJrzHO0t6X-M-90EvCBRwZeN9wllnXA8gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انصارالله یمن: مسلمانان نباید از سلاح تحریم کالاهای دشمن غافل شوند
🔹
زمانی که ملت‌های ما برای نیاز ضروری خود به غذا به دشمنان متکی شوند، به برگ فشاری در دست دشمن تبدیل می‌شوند.
🔹
آمریکا و اسرائیل به اهمیت سلاح تحریم پی برده‌اند و آن را در میدان نبرد علیه امت ما به‌شدت به کار می‌گیرند.
🔹
دشمنان از فشارهای اقتصادی و تحریم علیه ایران، عراق، لیبی، سوریه، یمن، کوبا و بسیاری از کشورهای جهان استفاده کرده و می‌کنند.
🔹
بخشی از راه‌حل‌های اساسی برای وضعیت معیشتی و اقتصادی، حرکت به سمت خودکفایی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/437490" target="_blank">📅 18:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437487">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iU08ZahGt7NL4Fw_2dBN7X7MYFhuge6MVoDUHsFgTrvQPXks-p_CFkPpec13JaLu2hSSoAGwtdHdubxUavW0SHN3axnrJeNVbEMFvm-mu5ildWW1PA4ApNO8DsoRm0XbI6KHqoYlzG-q17dPa01DqeHC3amZymYtcEsB7Te3BDTUTYkCpO8We0aFf98FE58s-1sAGoD5DQlLHdnhl-fqXbQgWTHNyMW1D613uKzvQD48f7wi8ikdT-Vr6m59auGXL8gUDbwOasGnCPQxvUOsw-xCq9Uf45jeSlAZepKuaBPC7HyMvj_3yQqRu25oqtxOdI75BML8mrxNBEBiT3oY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7ySf1a0W9fN-oloEZOxTRNeARG9RWQT4wj-OqvvqWeotT-EcIgVsmaf2pmej3qLlQXy2oPsymN6asOd8FJarNntwKfzmzImaj6YY4o_qY4okcIBQHaK4s0mnmBwAHjxke5l9F1sgPQEE3aIouTmKS9J6t0Bp0gBMTvDTdnpzvwIleCvfYVgXUStvgT-9RJJU4tV2-7rUj3HIYstFlL4oRMPDoptuWM8ygKaiOa5_5Lfk5lkvAVecM_dmk0gvmYc-k9qkl-YiggSWSGBPuQIDuHKFCd7Y4RmP3F1u2JHo68W9JJY5368igElCxXigiASgnhHSS4K-6qbxCQMmZIPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plHH86HIfKOznULaww3tXOGO9CDVrqy2UD_7jSmX4WXnzxXnH3si2EDG_bGHwy_V2JeiYBiX1_mIn3dP56o71TRMy9ump96qzVPlzvH_Vs-wK0zzKpzZ8xiC3nX9LSRuxr0kC0Sl2ii0iQjfoO2vUq0MxifGETb_CM1t1FhMi1uKwz3hxkV6uRowPxmu0s3jclNhj8e_xKtntoYXRRhS6sDc7Le9bS_RBtr86mmnsbjahXHlkApmS_Tt_BWjo8RYiariA0mI7DuIGBNzs4NlTY1VY95UiWdJqUIw4rCLEuAuuN9rl2xvSxAZ8BNlnpvt9Brw6K_tQh5MYHALPsHMiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حرم امام حسین(ع) در آستانهٔ شهادت امام باقر(ع) سیاه‌پوش شد  @Farsna</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/437487" target="_blank">📅 18:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437486">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">۳ عملیات حزب‌الله لبنان از ظهر امروز
🔹
حزب‌الله: ۲ سکوی گنبد آهنین در پادگان رامیم را با پهپاد مورد اصابت قطعی و یک خودروی مهندسی ارتش اسرائیل نیز در شهر بنت جبیل هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/437486" target="_blank">📅 18:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437485">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp2wXsXzgGudFZSYPVC3JkBVfjYN-t7SKJ9U2XtCf2SF5lnG_zstgD7eFMjdPY4VdSd6EdG1MXKuiQzXHq-2eFutBkRpXdQAZS7Mm0AsAiSR5QfgIAkNLFwKulLOyAhe69sPt7l769z-hnPFXPgjFgrZTwO7EZ7y1HpYqGX-7WpuJ8qPoWSNLEslOZNqCEECQiQPSqAuMg2URpeUidxKalW2s_scqjgxU4PrWDU63N6LCTg2E13YbIPWWZ45cYam-9U6rBazRE7KoiDSm6Iq4x1zZcPoaey3q9_j-3pcEXi7Ml0m17CG63Dv2K2XsWbehQNSZYmXYTRwz7qP3mpmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر ایرانی ۲ طلا در پاراوزنه‌برداری ضرب کرد
🔹
در سومین روز از رقابت‌های آزاد پاراوزنه‌برداری جوانان الجزایر، عطیه سادات حسینی ملی‌پوش پاراوزنه‌برداری کشورمان در دستهٔ ۶۱ کیلوگرم با کسب مدال طلای این وزن و با ثبت رکورد ۱۹۱ کیلوگرم موفق به کسب مدال طلای مجموع شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/437485" target="_blank">📅 18:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437484">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jbh4VjZKIXJVMYcgtLMZm6ZYl7R-N4x6dLXZh1QCAscsj_yOTbP6qbFfzU_y3ty2oaWVnd2eLwjvu88iCFQnzLfbcw9Z-GEJCCIA5SBHJcWHq8z_h1H69MHFevSEBGOVLT5ykCYeNcpmnTh_A5Kz46BJNelhbllfA7nBUbmHYj9VCGIiROKrNV4lP2M0juIHKozEN1z_nuX26OIr1Mq6jwmtD0MxC-llCo17ZUsMlKzRsO68dtPNWG4Af3qrK2Y5rsb9kWYFbtsn-z1rJPJMjYPhB4CcrQmZRncX7sMo6QQCIf0egM5_-8cBIxhKGcwq4U_oK6vfVB3UsPTBoopuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فائو: تنگهٔ هرمز بسته بماند، جهان با یک بحران غذایی مواجه خواهد شد
🔹
سازمان کشاورزی ملل متحد: ادامه بسته‌ماندن تنگهٔ هرمز آغاز یک شوک ساختاری در نظام غذایی جهان است و آثار این شوک طی بازهٔ زمانی ۶ تا ۱۲ ماه آینده ظاهر خواهد شد، به‌طوری‌که یک خانواده ۴ نفره در اروپا برای خرید یک قرص نان باید پول یک وعدهٔ غذا را بدهد.
🔹
افزایش قیمت انرژی، قیمت گندم و برنج را نیز بالا برده است.
🔹
کارشناسان پیش‌بینی می‌کنند در ۱۲ ماه آینده قیمت نان در جهان ۳۵ تا ۴۵ درصد افزایش یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/437484" target="_blank">📅 17:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437483">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6f158d4c.mp4?token=lPLv66iMdLujPPl_H9kSWEqH4XgRk1hCrYBO_RBTj8qsYs9g3vVNA3b0ViCm6v0w2duaDzJsyLisLZhni4ovGSVW8OIwfHs3KVeb4VYsMuwQmcY5BazZMFIwQg_JNKDXjFUImtom5y4Ud5CtF5hoXYF_Fyq3j4vCWhULnYfNbtM8sbIULNN6EmsQEjP97YLFbsdTFdmgbUMH3FPyrMu9DStqWtl78_ouMS__ujaiVQ6R-7f0hbf0QmKoosk0k-XPnITBFA0jJHKV4oQjqkDinHOffiPaI07RfeENnCjIv-yKlcTHvwhV5dfuMSghkqPL7P3nc404Al1rOAxkwYiqoo3a9_Otgnz9ewTvfQHU65ybcdMLjdsg0iNjjC-YKyVxx8pDee19A0luCVfmw0NxGpkkPNxT_6Tgj_2Vx3cJY7Oe5u75ZJVfz7WnTz_-ntGgRrVW1bdoROHSat-IaPFGEednafTj85wSmF4gx_a4nrfgb08DDI54ZUMQoqfBrd9KdaWn29Fzh90cab9VC5yyFW3EyfHcDjM9_GyqSCa9utE9QNget4q8vk-T1_NS-PGV-ZNcm8ROQXbI6Ems4BSg1pkl9-sUkh5GzUD86P83K4mUQMT3dLWH9ccGuutJ1mRK4wnGpQeoSnjfeqkvJQ4dmBLAwYkQlyREPRn-H5QJ9J0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6f158d4c.mp4?token=lPLv66iMdLujPPl_H9kSWEqH4XgRk1hCrYBO_RBTj8qsYs9g3vVNA3b0ViCm6v0w2duaDzJsyLisLZhni4ovGSVW8OIwfHs3KVeb4VYsMuwQmcY5BazZMFIwQg_JNKDXjFUImtom5y4Ud5CtF5hoXYF_Fyq3j4vCWhULnYfNbtM8sbIULNN6EmsQEjP97YLFbsdTFdmgbUMH3FPyrMu9DStqWtl78_ouMS__ujaiVQ6R-7f0hbf0QmKoosk0k-XPnITBFA0jJHKV4oQjqkDinHOffiPaI07RfeENnCjIv-yKlcTHvwhV5dfuMSghkqPL7P3nc404Al1rOAxkwYiqoo3a9_Otgnz9ewTvfQHU65ybcdMLjdsg0iNjjC-YKyVxx8pDee19A0luCVfmw0NxGpkkPNxT_6Tgj_2Vx3cJY7Oe5u75ZJVfz7WnTz_-ntGgRrVW1bdoROHSat-IaPFGEednafTj85wSmF4gx_a4nrfgb08DDI54ZUMQoqfBrd9KdaWn29Fzh90cab9VC5yyFW3EyfHcDjM9_GyqSCa9utE9QNget4q8vk-T1_NS-PGV-ZNcm8ROQXbI6Ems4BSg1pkl9-sUkh5GzUD86P83K4mUQMT3dLWH9ccGuutJ1mRK4wnGpQeoSnjfeqkvJQ4dmBLAwYkQlyREPRn-H5QJ9J0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریاچهٔ ارومیه با ترک‌های عمیقش خداحافظی کرد  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/437483" target="_blank">📅 17:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437482">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎥
تشییع پیکر مطهر شهید جنگ رمضان در بروجرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/437482" target="_blank">📅 17:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437481">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/431f4e1b52.mp4?token=JRoPPuWp3COEG45kgR0F7-7YeOBEQw43ftSvWq4Cu73eHTNmiAoWRZW0uPXJApsOfPvA6OjVo8yefC9JrvtF6EKvYfcg-2X9OAEw4L53vPQCE8baMM_uRYo40j0-myBKxUc7JMorNwB1uh3dH6QfvmTrsN1Jv2eS2sSDyjV62hCGoe0jE5878BQXMToKpNTAv6TK1X1vaYm7uww944TxcinnG7LfCguAkseKdnWKzHyZnOvolgkl3AITSGqY1HPLlc6GQvym--NfLXIqdijtIjmnohauOORwGEhnnzDYzcD6R-e2t9EXh8wMvM-04-4q3DYWi0S1wzytRvlPMd_S4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/431f4e1b52.mp4?token=JRoPPuWp3COEG45kgR0F7-7YeOBEQw43ftSvWq4Cu73eHTNmiAoWRZW0uPXJApsOfPvA6OjVo8yefC9JrvtF6EKvYfcg-2X9OAEw4L53vPQCE8baMM_uRYo40j0-myBKxUc7JMorNwB1uh3dH6QfvmTrsN1Jv2eS2sSDyjV62hCGoe0jE5878BQXMToKpNTAv6TK1X1vaYm7uww944TxcinnG7LfCguAkseKdnWKzHyZnOvolgkl3AITSGqY1HPLlc6GQvym--NfLXIqdijtIjmnohauOORwGEhnnzDYzcD6R-e2t9EXh8wMvM-04-4q3DYWi0S1wzytRvlPMd_S4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: در این مرحله دربارهٔ موضوع هسته‌ای مذاکره‌ای نمی‌کنیم
🔹
اینکه در مراحل بعدی در مورد موضوع هسته‌ای یا سایر موضوعات بحث کنیم، از این مرحله جداست و تمرکز ما در این مرحله بر اتمام جنگ است.
🔹
تحریم‌ها قطعاً جزو موضوعات مذاکره است اما با توجه…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/437481" target="_blank">📅 17:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437475">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTUjxCDTrW1uY54_88u2gNIagR-LWMU8FktLh21zK3bqXgeXfnFCrAVJrKcbXIgWVxglVK8NUco910CoYf8SDrIVqPWGJXn0-5X5wHvCYdDiYzf63g_xCZgpTAUoQiU1eu4Se_ClBU3soODyO4tNqwVWkJc1xXhasKdsZSgZFZg0Mf1iG9SUfbGjc2Db8Jf87TVHhn3OeiITBvw0YY2UZSrdzmRkz4OBMmpxOzoZX7bCg2GBpn-Mkz1HMzf_L07CfO0Nc23Rs_m8RoaL0WD5br5Cgz1ExP_-tGYeGvxNvOIp3BBaX6VI6kJmgn4Wj0dq421QM_Eynoz9q9Ym8nH6-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShKtnzM9KjygaPKXELDJptssue_bfu1zTWJdrs7mjXu-kKUPk8Yehm3fZVy2Y8YKiClkRAS9uHGysuWfqi_ywBa_os3MNu1Vi0yEoGCy-aHQtB1Pde2bGi4xY0wWvMfpZy3OacvjtWXq1tYEsWsV5m_WMSoRI8jwIc2HzvxAsRuDVq3N-Z5DsA9wEIhnNsAPp8Qc8BQhXCLz-h8qOKRm0mNxxAkVAQo-IaLdd_7hVU5qhtDMgtOICg6QiLzhg-OQHunWDnAadK7o2dhl5umhntTiVprh4H6mg437F1JzPmn_z1F_x7ZU9lBl2W9bjVWMR8bi74dR1f1HrRKk5bIGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBJAULocxWtC5cVJ61uGCQdSqYyKpx4AZKh2fnMzFSwOm3RrG2yxAjRt1rkRSlywV1Ec5NsFwW1XNz2PfGghwDlr_nlD4RIcEPF20VeEExwAjQncBZj_JgFmuUcuCztGjOopzGE6HFa6vyjMgKD1et_ZPGl4LRRXxbV8MtEd4NkgaMxiSuW_UlLRUQdg2ze2YC71iYu6frdI-rJMyGqd2zYie6J8iatuPacCM_ip8GDf_x_udaO59-t_2lVtYoclv5APY_fFN550xYfvyNqBFupAeDy1OhufXEJX5lh8OpOf3M-4Bmy21LQ9lPJQCwYaUpxMbHQqIegh2QlPZVYTqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYckG2Zt7Uk5BRUJgDA2ructdq0CVwOvsdQdmlVyMULtR9yVzH0aRfcDDx-ClTqf6E053yzOHlOhDqBtZjrKFa7ahomDLlvz2x2biIK8Fcto9t-35Enu7v7-pt7wDf8oCINggXXnKDbppVNzwfNeumb6cKj0L88DIlusYBRfZAIdP5jMaVjc3dA0icHx-h2IoryEmenAc6N-eaYv-cM799GQHa1zVricOf1NLMjQzcCPxL5U-CSUOhLGYMLRLp2b_IOMoTCuhM5Qajz0WRVE0OGkQDfGU7eR7yHNMDOG0qNxIXF7jD1yd3Ao-NMWvNh7_ywh-lVk4YfrU_RuXW47hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6ml9v-Q-TC1RCp-sOZJQ_5jMwx5W2frlnOZXc8HacGqykcize5apBJVYAvrsYGvYZP7cTFUwx3vDbbBD8nCgoyxGoDJze04rRIg2IisGw_qbrjK49tCsNkpviuzNz0KhNx1EAWte4mqI4bMzdrpdmFC1bTEAMxwEgio738VAbSu-LtyTyvEda78W3X2EQItHZeiQ-gzG93AMxtJHrnORow4CRJ8WrazBuLwhPFDwO1r8BLCedR9LubfoRpHhq5-AgSEKY6JMM9PHZmv0hsYJbn1MHFjk-GscK-kkTQtIKiAzhK-IiKE7Xc9OgJUtc4KUjvnOXHX34gXPQWOgtNhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4TQ8-eq560O14Y-C_uD3Ef-zJvw5x9331eYhiC6PLwBD6muM91Do2YFl_B67RJkNDs-ZRqGylUOYXPd7AVySTyAh8f0xKFgKfBUFea1QcTz-Z9Y5o4em7nHYojBd3bTlT7gJn4CxFSLaX-gLAH80sWxO480KANfextLIJU1o6atAoRc_rcSV5hdbNeu16YaPCQ2gEAkkKM8fcPTQXtvfdsoePH3F2J0A7dtIEEBsRExErYAphBS9PvDLBIQ7HFs7b3XVwfXALnJd09r5ggVYLd42y2CQwE29pVfVRN6--alb-tAf5W143Dvu4jm8z1gS3Xp9JMqOGio-xHPxQT0XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
محفل القائد المعظم، یادبود رهبر شهید امام خامنه‌ای در میدان التحریر بغداد با حضور میزبانان برنامه محفل
@Farsna</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/437475" target="_blank">📅 17:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437474">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b2f025d5.mp4?token=PB2qA1tT36gWR_mxtiwbCwzj0w1ulZLEwEZs-RaHM0vooab2oGw7jVxtTsGOicIgsFDRI6zYhzNByZ_tNh4Gb4PK0c9z43ORjZ8jVcALFVb9yHpv56iytlx4kSNIdohrnqZantkuktzy06VL0JoZZbX4vf8REe_oQPrQ-2CZ6TbSFOAcrUrUZbxQrxVQk4uqvDXHL-OXUNrY0hQhVkYEyvcF7pAAoQCKKSFSj-o11K5gPJQNBpI19Pgdb_A935UzKTdJa_7uHo8s-bGBGsYT2ROCDyb_YBYMyDQUcOnfE8C9RRWAozrBHt_RGua0Tksd5i0xiIdnwlLPd710VmrZ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b2f025d5.mp4?token=PB2qA1tT36gWR_mxtiwbCwzj0w1ulZLEwEZs-RaHM0vooab2oGw7jVxtTsGOicIgsFDRI6zYhzNByZ_tNh4Gb4PK0c9z43ORjZ8jVcALFVb9yHpv56iytlx4kSNIdohrnqZantkuktzy06VL0JoZZbX4vf8REe_oQPrQ-2CZ6TbSFOAcrUrUZbxQrxVQk4uqvDXHL-OXUNrY0hQhVkYEyvcF7pAAoQCKKSFSj-o11K5gPJQNBpI19Pgdb_A935UzKTdJa_7uHo8s-bGBGsYT2ROCDyb_YBYMyDQUcOnfE8C9RRWAozrBHt_RGua0Tksd5i0xiIdnwlLPd710VmrZ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مسئلهٔ تنگهٔ هرمز به آمریکا هیچ ربطی ندارد
🔹
در مورد تنگه بین ما و عمان باید سازوکاری تعریف شود و در این مورد چند نوبت جلساتی با طرف عمانی داشته‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/437474" target="_blank">📅 17:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437473">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/717ef30b5c.mp4?token=Ww7RZKE1guPi_tQvIV6IGlRyGrI_qWwWSw1yVl1uFwEqax2bod4CuxBDcd1PyOkk4V_RCy0q9PE9pfy4alJiHS1MxCik7sx_8adbR6skovfWlVgC3xQm_FaawCCtXnVIsKqDsy5eLjbKGjUZXre2DmI4nf7Ga1JeIQQmu6RYAuPGMmh5H1tLE8redv6N8ElT5GrkF_LOO0tLdaBl7rshfo-g5jC3Y7MMsEHv8tI7Alv7Deo3COyTUiVAGUu806DHGr70MHuTQFz-gkVZ7StJFr4lxQMzlGAnerZyUhAh2Zj12mPcvTcgDPldjXc3DI2HIfSaeunn9blSmBf4d5fq9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/717ef30b5c.mp4?token=Ww7RZKE1guPi_tQvIV6IGlRyGrI_qWwWSw1yVl1uFwEqax2bod4CuxBDcd1PyOkk4V_RCy0q9PE9pfy4alJiHS1MxCik7sx_8adbR6skovfWlVgC3xQm_FaawCCtXnVIsKqDsy5eLjbKGjUZXre2DmI4nf7Ga1JeIQQmu6RYAuPGMmh5H1tLE8redv6N8ElT5GrkF_LOO0tLdaBl7rshfo-g5jC3Y7MMsEHv8tI7Alv7Deo3COyTUiVAGUu806DHGr70MHuTQFz-gkVZ7StJFr4lxQMzlGAnerZyUhAh2Zj12mPcvTcgDPldjXc3DI2HIfSaeunn9blSmBf4d5fq9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: بنای ما بر این بوده که تفاهم‌نامه‌ای ۱۴بندی تدوین کنیم و در آن مهم‌ترین موضوعاتی که لازمهٔ خاتمه جنگ است و مواردی که برای ما اساسی است گنجانده شود
🔹
ما در مرحلهٔ نهایی‌سازی این یادداشت تفاهم هستیم.  موضوعات اساسی این تفاهم‌نامه چیست؟…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/437473" target="_blank">📅 17:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437472">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32041f34fe.mp4?token=q65IdA3IKgaz-vNOFDpe-IZRFyP2qukB239n5JrsTzYgsKQug2GOhqcx6yLwopETD05-5NS5oWIWvTU0ZYxPs6sMd22CToKsOB2npSFj-pH00sPG7reICLXXPmySxopzcqFL_E0dfedLGLkYc-MB7DHY7YPkpjgKF2hwwTGKIRgtSK6hAI1bFYNbK0iIQtsVhxkJeyU1rIJKgXIK2eHSwZ6fSsPzIzZnaHRjOCZmeQhRX57caUvCJ5dnS0U0Y9N9q3_QeRCyQl7MLV7GVrBwzdYXAH6GLB85tHxvplxZ7anC1o3KuqINVVkSWF-YdoaKQFK0ff8A-w6PR_vAGwPnBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32041f34fe.mp4?token=q65IdA3IKgaz-vNOFDpe-IZRFyP2qukB239n5JrsTzYgsKQug2GOhqcx6yLwopETD05-5NS5oWIWvTU0ZYxPs6sMd22CToKsOB2npSFj-pH00sPG7reICLXXPmySxopzcqFL_E0dfedLGLkYc-MB7DHY7YPkpjgKF2hwwTGKIRgtSK6hAI1bFYNbK0iIQtsVhxkJeyU1rIJKgXIK2eHSwZ6fSsPzIzZnaHRjOCZmeQhRX57caUvCJ5dnS0U0Y9N9q3_QeRCyQl7MLV7GVrBwzdYXAH6GLB85tHxvplxZ7anC1o3KuqINVVkSWF-YdoaKQFK0ff8A-w6PR_vAGwPnBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما تجربهٔ ضدونقیض‌گویی طرف آمریکایی را داریم و نمی‌توانیم کاملا مطمئن باشیم که رویکرد آن‌ها تغییر نمی‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/437472" target="_blank">📅 17:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437465">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riOKBXP_PuenD27xlA3C_2PE4VDhldHwA_QA_ZHJ12h_WQ5JJ_3BRpRc_Fo4lOE-B7bN-30JbJ1esXMecSsS4JpnuDxD64vuzBV8Y28EdzXBV6TlP2jk3l6gHiJFNbm7HACvjKDlrKkAXZVZkqYpkCgYrgwenwHtGzuOzgwZreIe97DsG_69J0My0-kK0v2AizdUWju5nAJgB2HFZ91zhaNpW_zCM7f_sCQQg80u9VmWHSk7Mid833Yr1C9Zcb_80ENMW1ALf-GbT5-RzCWimaZnWjgLFLZORcs6aLjQazirtDWtUNqrBaO3XSkLJIZo5P4Zl_y4Pn8qytz6qMPYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcmyvieL3pzpFOs3v0w4Rg2r03S0MaJm71v1IiWWHTM5Fz1QF1nh7cHB_oVxQs3NuiFlMsEsp4cK-5FTqt34OV8gPPmscAUdSWnswp2UEyp2zH6xQFsCaUETi5vEcGg8Lk0iCfgjTYBQN9NVd0HYM7HapT2_MqErggtbbWOISrg6etuGMKpJbF5cJAAFu4Csbl5jZ1SCILPbV_kiXHEEVWwrb6ccN6BSmuP688razXmbkC0BW9jaienat6AF1A6D2P4EvOT2oDmEu5P6h6K6_BB_5XL9BUhKOikHNSBE810aWPxyOdCjnOhagEHj6nQnoLrgBbZ0z6cBgs9zJuRwuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWsuzA-ZEqom1RDjNlXMa7tN86zq1PldRpU7fvmWvAdVEVMknqIp_-VHONcSkkd1k550QJtT5gBoxGCi3rKOMr-IUrfyGhT8RZNYEFyPRDqEEJgEbfaeLo4H9xbRpBVSeou6QLXiwGZNGz-eYdhUpV5ixt2eVChookHXr5Qwo0J_YSOlq-T9MVgTYNMZD7KfjGj-qcnS-bR40t9RwdUUYSU6DKv71qBm8-TboSWvYyXjMxSwW4OFl8xG-yD3S6TB0FFbMh6Wupa76y7kLSYLXEq6xrez5Faz12dsyo0__AP4aVnn3c3dFEMQl92i46sLQmQS_xhTkKnvoGcMPJwndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xq43-t4DB5xfrNRBDND0lTdxO8uKQlr5EV-AMGyM7H5NX-iZMZSIqmU7836QjmIx8Ky5BDFLOILAgSH9RdFxDb8fVS_XEqc1RnNbBX7nEyvNMAnNeg-bouNLwFQf3wVnsw6XoQLTi9aTHpOcFWFmd8eJj3Dvz3usTMm4zQ0umyFijYFyeqgpFp-hG0NfE86iqiYocBwrFHVgy4YyWwwfdcFAWnfYNVLBM6HSSEttKzepvAunQkb3l1d4cYD71GzZnUWqMhnZ9yw-IKq0p8fFMH1FJ-zQ5CCEVlhSjz5eIcAcCLYRrCRFBU2tE2DRxO0M4iJ5uIvuRbtU5TcX-N_76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-PDZ3hn9UB0P2r-_J_2UbZBtiN14dMiHK_giHaqQpLgzFa3Y-m4cg67ayE_nPhzXwHQGnJ3wvob2BPLwCW8c0Kd-KDUaGx8MqK9stIw3kIXxhLFWxLBc5qlU3zKiAV5CcKyUil9lsaSHwOczrZTx-0yLvA8-2hqZ-mfXoBQYeOgucEWlCZkkKZjqCIwNL23Kc7kMfZUhGMIG1e7hRnKsvQx407RWG9r7cU85UHdFO23fXNUwg6kR51RReSo4SfJ0wx-ECPAK-ydOd9dAqSDbRiYjp4E_kASBp96dqIlf9lse6zoNMogTiIN7lWnvOf8WCI0Gb09PVR_-yQcRY5UWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mo5RT8TsSCjwIESkAlrHt0WrYCuy1flX00StbYy4OeFrOfQjqO74l5eY7i5BEAyIW0pCWfe8879nwZIM2Z6L8vvXZ9llDiklPpPx5s8Xg_DtZTlpxDvhcByAxk_F8u4obDsLizFwjiqPzdnFaDQuYt3o66CKPZUsmFwZDeIVC_WEk1C-VDkAIpbIN7WaOVTlg_PgYyvg1rWAigOJCjcweZ5SSGrnXRzs7qQo67qMa3r_BxyWjRn9BF7cuqySIq6SwAbZxWSjSsw0euSJTXmk2EBQfaHNVX3uZQnSDzblDVkABudex1ZdACfwRjqLpXKD1_7GXGKWWF0LAVjf-EP51A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyBEuTYP8QX78aX-4nxzVAfQ0xI_KcuB1yppEn3piIWCm7rcCSJFuqCpgP5ZYT2t3Oq5YYsqhqu3Lz_caaYc-Mx_zWHKVAms2BZitOKtt3vvrqu4E-oStE-v0eYjjpdm37M9tqz9GhTGvfZejjCy2HLUP9WLvexuJ_s6xigxRMh7BS94wIBlgOLlgcenazc52IygTLoI0TPh5l3hArHU3G_je9iC9_1EC0nu5vpbFMcahtuUGVWVZUOMu75MmYugbkkNtF5_8PNLfHMlw-KSuA_yNUUpo-A-2UKE5Fu95b_w73kNrolbEpmlg_FGWkgJ2zc951vNtscfVkrDWjZBfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌عاصم منیر تهران را ترک کرد
🔹
فرمانده ارتش پاکستان که عصر دیروز برای دیدار و گفت‌وگو با مقامات ایرانی به ایران سفر کرد بعدازظهر امروز تهران را ترک کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/437465" target="_blank">📅 17:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437464">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ni1hsUTc588jTGuVXBKeNJg5Y3osPqs5BEprZ2GLkzJkMR2OfuxPMOACeF0ZFlt_rirerQF_u-7DeRw_KnI3JJp-e-4FXBNY8NwxOyTaI5_tRNIliyoGZK21rHlK-V2aoTAoAO9FohKG88jC2M4-ZgJ9j1ElcKXZfUFIZRxDz0JL48Y5B0cwg-WFUI1PU_AfcBrgq2W3timCq14DtGA8haFhqf-3Dr54OngFAhAAFq5G00nmtsT_L2mcGOKd2cE7ZiMqnAhyBLSsYF3_q_zpEStYz6SomqNJ37IYg5MVaIah06fGURv6k6fczSjs8GOpIrTI-yzaY-WEQScWvc37wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوران جدید آغاز شده و پویش جان‌فدا وارد فضای عملیاتی می‌شود
🔹
شرکت در پویش جان‌فدا با یک پیامک ساده برگزار شد. همه تقریبا شرکت کردیم و جز یک کار نمادین وجه دیگری نداشت.
🔹
حالا پویش جان‌فدا وارد ابعاد تخصصی می‌شود و قرار است به صورت گسترده آموزش‌های مختلفی داده شود.
🔹
وارد لینک زیر بشوید و اطلاعات خود را تکمیل کنید چون ظرفیت این اتفاق در مراحل اول محدود است و باتوجه به شرایط مشخص نیست تا که چه زمانی آموزش‌ها ادامه پیدا کند.
🔹
آموزش‌ها مربوط به فضای جدید جنگ، مسائل درمانی و در مجموعه توانمند سازی مردم و استفاده از توانمندی های جمعی در آینده جنگ است.
🔹
همین الان عدد ۲ را به ۳۰۰۰۱۱۵۵ ارسال نمایید و وارد فاز عملیاتی جان‌فدا بشوید.
@Farsna</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/farsna/437464" target="_blank">📅 17:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437463">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a911ceb49.mp4?token=F5gcbuk45H33fglYnSEjNOgpOSrrKUHMPRRUJdGQJFqyZXxsLLHUjU3DIapBVL9DKFk0dyyHqlRQEQSEaEbeZBXyIuDbNa_ABfw55qwj_1XXWEcEZcZc6KuBMZRWE9oREyNaj99QKKuZ2wnLQqp1BQUECIG7Dr4Y1-EN_y4V9t9q2GCJskSu9MJOuLJ-7HDVO2ttJCderEmOufyIb9tg5rmlKND-YJe5BMMqkepvgEJM33b5QwdikwWpoZhhRIdmSjzDWrTdOBVFRHVUa4OTZXfZv0iztbV-8qIc5fce9DZOaqgDMSU027G1HYqZMlOCNxnrsw_K_BBCnZccSY25og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a911ceb49.mp4?token=F5gcbuk45H33fglYnSEjNOgpOSrrKUHMPRRUJdGQJFqyZXxsLLHUjU3DIapBVL9DKFk0dyyHqlRQEQSEaEbeZBXyIuDbNa_ABfw55qwj_1XXWEcEZcZc6KuBMZRWE9oREyNaj99QKKuZ2wnLQqp1BQUECIG7Dr4Y1-EN_y4V9t9q2GCJskSu9MJOuLJ-7HDVO2ttJCderEmOufyIb9tg5rmlKND-YJe5BMMqkepvgEJM33b5QwdikwWpoZhhRIdmSjzDWrTdOBVFRHVUa4OTZXfZv0iztbV-8qIc5fce9DZOaqgDMSU027G1HYqZMlOCNxnrsw_K_BBCnZccSY25og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ نظر بقائی درباره توافق: خیلی دور، خیلی نزدیک
🔹
سخنگوی وزارت امور خارجه امروز در پاسخ به سؤالی درباره اینکه توافق نزدیک است؟ گفت‌ که خیلی دور، خیلی نزدیک و افزود: ما تجربه ضد و نقیض گویی طرف آمریکایی را داریم و دیدگاه‌های خود را بارها تغییر داده‌اند.
🔹
اسماعیل…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/437463" target="_blank">📅 17:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437462">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WraiHr5or8jvjLYlS8goASSj1NiGHPaCYx10U7S9fPNbq62OZ90ZpCs_YTyckfLW8Na7mAypMwo26nJ-xJb9e9cs4fSBSiFLgE0OLxgl3YkaiZ7267lgCK9aFqD1uRcOnVVWozcxED0ppyHvlJAeLF1w_fwn0maw8moRbmNvejqPBrrqe5FY5oswCgDbVw__jafHeYEkCBtqaHDze-kA8nwtjJZCPigt_Ha7GVJse6_kUjHAEKQkADCHqEWQqBlktJOnqiz3hhLNs8X0KAbCcPG-bu3Y2BhYamuqURfHbQdci3GRJnPEsapF9L2k6neE3saN7eJOq1bFkZQ44HQW2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نظر بقائی درباره توافق: خیلی دور، خیلی نزدیک
🔹
سخنگوی وزارت امور خارجه امروز در پاسخ به سؤالی درباره اینکه توافق نزدیک است؟ گفت‌ که خیلی دور، خیلی نزدیک و افزود: ما تجربه ضد و نقیض گویی طرف آمریکایی را داریم و دیدگاه‌های خود را بارها تغییر داده‌اند.
🔹
اسماعیل بقائی درباره سفر عاصم منیر به تهران و رایزنی‌هایش با مقامات ایرانی گفت: هیأت پاکستانی غروب جمعه رسیدند و از قبل وزیر کشور پاکستان چند روزی در تهران حضور داشت.
🔹
پاکستان به عنوان میانجی نقش مهمی را ایفا کرده و هدف از این سفر ادامه تبادل پیام‌ها بین ایران و آمریکا بود.
🔹
تمرکز ما در این مرحله بر خاتمه جنگ تحمیلی است با مختصاتی که کم و بیش اطلاع دارید براساس پیشنهاد ۱۴ بندی ایران که چندین بار رفت و برگشت شده و در خصوص بندهای مختلف آن دیدگاه‌های طرفین تبادل شده است و در این چند روز راجع به برخی نکات و عبارت پردازی‌هایی که راجع به آن اختلاف نظر کماکان وجود داشت بحث و پیشنهاداتی مطرح شد که همچنان برخی از آن در حال بررسی و اعلام نظر است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/437462" target="_blank">📅 16:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437461">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rs0o4HlzyyMU0HnRbA6jzeiI0v6VRwKFRxyOA1H3NxmF9_PvEce7hsxgOBPEOUWYVf2B2udRQDYW7jEkCjnrSz4cSRQ8BxoYgeEq_ozg89_IBWVDMEaWZhI5xB_fSNS6-7doz8yFfBLf3EeJcJjqw5utbaEvFghcHGtwN8F3m0ywcSgAmW6YkIYtscO_mMgEz2TJrMJrl6ZCF8Fed3WlopbbaoM1jO6Nhe5VCJuLgpnYlP-n-hn-miyasUSfKBXlb7-U1nnXtxogFLBfk8H7MQbaGS5_P5ktdZ-PSflzB_F7g1mBGk1PoOCQqcCXMiBrrF0_Kb-1tIadGG7073ha7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر کشاورزی: امیدوارم سازمان برنامه و بودجه زودتر پول گندم‌کاران را پرداخت کند.  @Farsna</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/437461" target="_blank">📅 16:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437460">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5724f03e5.mp4?token=ha1pavFmi7r4XTEm9AoljuM4YoTRaR7lhNbk3-nhQCwWaJTp1PQUbTwd_RzDUbWb0Ob0TKSsmGQPE0R2tHX9U0YvE0HKvT1rLafgeTNtGQm0F0MJmD-yZDoJ25OiUGzaWsAVsj-zuQGpLI3ySJF0zwCuB9ze-gys5pIsX0tSfgNDS1ywIktIhve72XpXdD9yrTpp7kCm5IH_UjR-S8cLOP76RE9h2g7w1bGMRpbhLgLGB4gPs3wQdjrU6iuoQ2cUCTjfbKw7SvRXcJ3p_sG_61DuKYWVT38nW7YQdUOo1DRcHmsZ0mZ_2RmCfCjtly4kR8qMyhj2ArRFKj9eA8P7Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5724f03e5.mp4?token=ha1pavFmi7r4XTEm9AoljuM4YoTRaR7lhNbk3-nhQCwWaJTp1PQUbTwd_RzDUbWb0Ob0TKSsmGQPE0R2tHX9U0YvE0HKvT1rLafgeTNtGQm0F0MJmD-yZDoJ25OiUGzaWsAVsj-zuQGpLI3ySJF0zwCuB9ze-gys5pIsX0tSfgNDS1ywIktIhve72XpXdD9yrTpp7kCm5IH_UjR-S8cLOP76RE9h2g7w1bGMRpbhLgLGB4gPs3wQdjrU6iuoQ2cUCTjfbKw7SvRXcJ3p_sG_61DuKYWVT38nW7YQdUOo1DRcHmsZ0mZ_2RmCfCjtly4kR8qMyhj2ArRFKj9eA8P7Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت‌هایی از کتابخوانی رهبر شهید انقلاب
🔹
«من در دوران جوانى زیاد مطالعه مى‌کردم. غیر از کتابهاى درسى خودمان که مطالعه مى‌کردم و مى‌خواندم، کتاب تاریخ، کتاب ادبیات، کتاب شعر و کتاب قصّه و رمان هم مى‌خواندم. به کتاب قصّه خیلى علاقه داشتم و خیلى از رمانهاى معروف را در دوره نوجوانى خواندم. شعر هم مى‌خواندم. من با بسیارى از دیوانهاى شعر، در دوره نوجوانى و جوانى آشنا شدم. به کتاب تاریخ علاقه داشتم و چون درس عربى مى‌خواندم و با زبان عربى آشنا شده بودم، به حدیث هم علاقه داشتم.» ۱۳۷۶/۱۱/۱۴
از کتاب‌کرایه‌ای تا کتابخانه آستان قدس
🔹
«نزدیک منزل ما کتابفروشى کوچکى بود که کتاب، کرایه مى‌داد. من رمان و اینها که مى‌خواندم، معمولاً از آن‌جا کرایه مى‌کردم. آستان قدس هم در مشهد، کتابخانه خیلى خوبى دارد. در دوره اوایل طلبگى - در همان سنین پانزده، شانزده سالگى - به آن‌جا مراجعه مى‌کردم. گاهى روزها آن‌جا مى‌رفتم و مشغول مطالعه مى‌شدم؛ صداى اذان با بلندگو پخش مى‌شد، به قدرى غرق مطالعه بودم که صداى اذان را نمى‌شنیدم!» ۱۳۷۶/۱۱/۱۴
کتاب‌خوانی در خدمت نهضت فکری
🔹
«در دوران مبارزات، کتابهایی را میخواندم به قصد این که ببینیم به درد چه کسی میخورد، یا کجاهایش به درد چه کسانی میخورد و یادداشت میکردم. جوانانی که با من رفت و آمد داشتند - عمدتاً در مشهد، یا در دوره‌ای که مشهد نبودم؛ تبعید بودم - من اسم میدادم که این کتابها را بخوانید؛ این کتابها هم متنوّع بود. الان هم می‌شود این کار را کرد و مجموعه‌ای را در نظر گرفت.» ۱۳۷۷/۱۱/۱۳
ساعاتی که هرگز هدر نمی‌رود
🔹
«بنده چند جلد قطور از یک عنوان کتاب را در اتوبوس خواندم! البته قضیه مربوط به قبل از انقلاب است که چند روزى براى انجام کارى از مشهد به تهران آمده بودم. وضعیت و فضاى اتوبوسهاى آن روزگار براى ما خیلى آزار دهنده بود و نمى‌توانستیم تحمّل کنیم. دلم مى‌خواست سرم پایین باشد و خواندن کتاب در چنین وضعیتى بهترین کار بود. ساعتى را که به این حالت مى‌گذراندم احساس نمى‌کردم ضایع مى‌شود؛ چون کتاب مى‌خواندم.» ۱۳۷۵/۰۲/۲۲
🔗
شرح کامل این گزارش را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/437460" target="_blank">📅 16:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437459">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvDLH3XWQmGJp4s6EF3doLvfeoSjTMpT1yKZFV4pPa2mtdSdv8OO0ZemUwptCnftGs7gEnCtcJmaC68EE9DZoZknb--sGHNaEaGHGa0EGlOr1NKzrUAF6pGtejPclpQDhpaNJCgmwEGxc1lOHYR2tWk2g-qafNwOCEBde4obMPCBLYGlMYpvTA6w37CojpUPD-xT9vbzsVKfLD2bEbMmcuiGWy1OCBHd_c5tj24bYvJa69flETExwz7Ou_IcxxYn_9r6wrCHTp9jAJC26rj12oQ51O-IqDm18gYEStL9lE4V-mdl-XMzcG0zjpjS_wgHqbWCdpB9VZpXlZ1b_Vds0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: سابقۀ مذاکره با آمریکایی‌ها حکم می‌کند نهایت دقت را به عمل آوریم
🔹
رئیس‌جمهور در دیدار فرمانده ارتش پاکستان: ما صرفا به‌دنبال احقاق حقوق حقه و قانونی ملت خود هستیم، اما سابقۀ و تجربۀ مذاکره با آمریکایی‌ها به ما حکم می‌کند که نهایت دقت را به عمل آوریم.…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/farsna/437459" target="_blank">📅 16:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437456">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awlSa19VU9oyBsmDSJyVY--jvCqnfi1PNAKCEt7tgQXoRSYZdCgK9l67try_Hy_qPZe4V9ljWa_kj2L9I_A9mtknaqH4tXf2bkowsqkswQ-e_d13w_F4B5fr1Li6XBmEAcW6r5f1O3InYu4AZEd4cm4PyKNO8Rpo-J2uBr4bW3J32JcK44es1mlvADLhcig5L1tbh_3mAL0i5s1rnczwQxeMUwFLMsDNv97sLW6DVlqIdzYDxklvOl2spr21VT4MHQUeFbYQXjcbCdP5Y2bXs4jMm-lFKgFQBzzdSXCWt2-ImYjFzTKkFsao3BixlpGBONVM2C_C-itcd_PTEQ-YbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8snhKgxfrVfxFjQZ9DgpkOe6e7xvatk00uCLCgOoBtCS3AsI3fazQoB3YC22WmqIb93ifDM3ytliDkvKLV3CyfDBKyET5NIs0f9ce1kN2ypGHtJdP78ppzIzim6f4kKu90nuJsgbfVNVGzkKZy6Cd0XMOojF6EzucQ2JrhsAX1FDUxQQDZO7TgeJhF3XPOI76balVnqAzna8FOJwHeRvVPi2lOcw_2X4PL-BVlM93mF8clD1yKI4fI_rVr8XGqVtiBgodGSFMAKdkN1KXaamhxydaD6HIL_-AKu7cqHgN14XhrY0HAupof7HjVkOretmTuDOIQfALEVFK8IXS-L4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
فرمانده ارتش پاکستان با پزشکیان دیدار و گفت‌وگو کرد  @Farsna</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/437456" target="_blank">📅 16:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437455">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ارتش: آمادۀ مقابله قاطع با هرگونه تعدی دشمنان هستیم
🔹
بیانیۀ ارتش به‌مناسبت سالروز آزادسازی خرمشهر: فتح خرمشهر، ثمره ایمان راسخ، مجاهدت خالصانه و ایثار بی‌بدیل فرزندان این مرز و بوم بود که با تبعیت از رهبری الهی حضرت امام خمینی (ره) و با اتکا به قدرت لایزال الهی، توانستند معادلات دشمن را برهم زده و مقاومت و ایستادگی ملت ایران را به رخ جهانیان کشند.
🔹
ملت شریف و نیروهای مسلح ایران، به‌ویژه ارتش غیور و سرافراز ایران، امروز نیز در پرتو همان روحیۀ جهادی و با بهره‌گیری از تجارب گران‌سنگ دفاع مقدس و جنگ‌های تحمیلی و ناجوانمردانۀ ۱۲ و ۴۰ روزه، در راستای تدابیر رهبر انقلاب برای مقابله با دشمنان، آماده و هوشیار است.
🔹
ارتش با تمسک به آرمان‌های رهبران کبیر و شهید و تحت فرامین حکیمانه رهبر معظم انقلاب، با عزمی راسخ و اراده‌ای خلل‌ناپذیر، خود را برای مقابله قاطع و همه‌جانبه با هرگونه تهدید و تجاوز دشمنان آماده نموده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/437455" target="_blank">📅 16:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437454">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Okt5xWWw5upUwfAOXsZL4d8dq3LPRptPJCoHfn8pjjmIQinI0Dr5_ceMPFWDG-0VRuN0fLWrCcuPWtK0dPSuQOiriZ7wYRPAgzAY2FegCTGkfF51JaYGrxeL6D-_yg7CXRW_-d7yskvmYIt2jpdIMaotLCaRu9qe7iTZRg8kDjD-p-7M3fiivCqBKTTwCsVwuLngQa23v_4qUe51vV1S3D2TQcMylszk9aySKAyiCRBBHO0qLSUJcCpiP5mkbAl0frh8w1EhPOd_LZuUws-PGxTYUH20n6mmvx4hjtRdTPRXSF1y-mDn5VRPUqXHZZVfB6AVA5Uw9teOiYwPiM1ZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه ورود بن گویر به خاکش را ممنوع کرد
🔹
وزیر امور خارجه فرانسه: به همتای ایتالیایی خود می‌پیوندم و از اتحادیهٔ اروپا می‌خواهم بن گویر را تحریم کند؛ وزیر امنیت داخلی اسرائیل از ورود به خاک ما منع شده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/437454" target="_blank">📅 16:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437453">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PilOIhelNczQDb-aj_2Mqxba-SLYm7Wjxr3LaZX2BZGzEvebd5zwJtw2t3UhVhOb9RrEcuX2nKrwJlJcJQK3vi4xE_Axezg9iKQ482tJgaI_gNs5Hb_56cbyM4fCXmQorc1cie_wPq1oa5LyxREECAPm2RZuWhy5m3zrDgTvoths0LzfUe-zfPfArUaODn2EBmIh3KC8pNmS_60V648sv-m6T6tIoCbQfbTKHEGR4AlcwC9R3TEjr3Lz8OnIQQYQwQ5oHvXGZXPhC6yK6tbe-U4Isp2XSN3fi2IAAax5orewoASPArFRZxOAR1Cdv60ByiYaxVWu-Jr6lHmAJN1nJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجهیز ۱۲ هزار مدرسه به نیروگاه خورشیدی
🔹
سازمان انرژی‌های تجدیدپذیر: سامانه‌های خورشیدی با ظرفیت ۵ کیلووات در ۱۲ هزار مدرسۀ سراسر کشور نصب می‌شود که سازمان انرژی‌های تجدیدپذیر تامین تجهیزات این سامانه‌ها را برعهده دارد.
🔹
هدف از اجرای این طرح، توسعهٔ انرژی‌های تجدیدپذیر در بخش عمومی و ترویج فرهنگ استفاده از انرژی پاک در مدارس کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/437453" target="_blank">📅 16:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437452">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mlw0vKlPBYDJSgiinzVy8kVtCx4NhOE5K7iqL1uWVhdJgLXmuo8ZTbTZoNRGBsMpXBVEesx7KX8Z1VLe8KfwHSfp5NzzfVDJo1cfL6HflpZAMWuz5kJcNfJDXJcAu9fLEF4zwEvXRgD5XSaDA4HyCb8UuMIFqVHY9Pna-j0Ho5Onfrsokmj94j-ExKK5yEcUGQ31PgAY28vyAwL9qC6DahaBkZwy6rg2ZO0EzLmHC5UxWnONV2a8vqjxcV8mA3LTJjVUlF071A7FsrS36CsMFfUlAdcd3PGp_BQH_nDnGNU7eYeZdSDKLbHwVtxRg8yeQ1DFtdiZRcLRtuULV432nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عاصم منیر همراه با عراقچی از محدودهٔ تاریخی میدان مشق تهران دیدن کرد  @Farsna</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/farsna/437452" target="_blank">📅 15:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437451">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZlZo-JL8G94gYdD7TulQPG64cpqNqmOu0BfMl2YyyW68tZPkffj1v9EoJeA7uQs1ntsR-Shhr99HTDeb8NbiLPQcsRMHd5GE8paHYFkA92RJgGAmXHlGoKaramSclo9JwFMuBN7lLWjlfEnS7CCLi5Gjz2n9kOXLT6VWn4VQpQhO5HAj9tGUHN-Kq349_4GwbN2b5UJft7gyh5dI2wjaWzuUlnbhzIvjAiDX0xffIJHRaebjS_IGraJUxLn4dCk6A6zOf8JsbwA2XPhw9B6MaFUv8GX8Q8Mc1kzMNPpBsLAFlxQJSYKufRYQTiJAq8v5qTor6vcoH3i9pJ99N1Exg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۴۰ کشتی در انتظار اجازهٔ ایران برای عبور از تنگهٔ هرمز
🔹
تصاویر ماهواره‌ای نشان می‌دهد که حدود ۲۴۰ کشتی در آب‌های خلیج فارس و در پشت مرزی که ایران آن را به‌عنوان منطقهٔ تحت کنترل خود در آب‌های خلیج فارس تعیین کرده است، جمع شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/437451" target="_blank">📅 15:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437446">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bNwH4m9kbfBKi0QWmfRSpNSqiGfWyBwMGieXTxfJ4X-bbpkF4AI1mWl9j93t2iV8LZTiK7o1-tiNpr9qrte95rNG03dB-Hel4JiF-l8mcp_CCz2uIIp_NysQdTZnqOVgNFVtRCNYrcVquj0_Nx_Fyrn8DGptktSdLY2lPgwp1_h2MnlWyPwAcWHBer4ghgLLkL53vOhrHGyoTANRgVDK8usJHnF4tU7u752WvTEO0s4-5JE3qr5jYmpsWbMDmNIEEdzBQCWnPIkyjaJ5H9F5H80Snl5HmFuRbD5h8TklyZn425AYigOTQLN8DAgUvnakUOt1FVb1dFun1ktXhHgz0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JY6O5WSUOb5in97xY9GXRiEkkPCDwk2bATxdvVJwxP47ReOGiRCu_BOPIeWA7DWbplKgRFvLINsiSD9GMlHyzSAX-oEqpzAFJR8k4PNk4Xz5Bp-D0xaJkG2z0bNHIxnvW5nkEj-NEh80wLSrl6-ZGmXnmAypCdnBiVWi3kMvq-uMAGEko857IIn-Q0s2i1opXlfYthmNGm-XYzoSUKV2PAaMC-GOk-IS5RjosFu5OJnpzKpgrENUgRFczN85RehtSg7N958__DLmP_l0mrC0I2oVm3ZNpcUz_BXT6SQD3qdyv1wb-4FsSTdohf2yGP79izpo8IOJmVTYLNQeQLVbwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7duxi4oe-C37bipYPqA-7mXc8m2VGx7XYgCNbrPU7wEJaUhh67EWGda55V0G8TkvIzb76p_BUG3duDOW422_7dYgWkjpT9Jo9gxLt_uvo2VbziigHJGYuagBeHs6xTjNNLxuuIcNQuRTMqfZQPsn0UktIA6NexGAa8L1FRWH_LWchNFkP5GZv6OdFLswN0kNzzBDcVzsLrQCfOfYyHRozdcuJC2ee4FjWWFNBwOzPFmKHqP5QU5XLZDA_BiTnuIS8s9zZC75M_mee_ngcY3EXfOSAIv-yftdEPElUgJ-dTAxg5vn7GM8WHO6JIbxjKl4nqsbH1Ai5Ffy0gZwm1hsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHQgQ90L6H0buxZCeamYu1Qp523oJQof5G5ExmGB68bBDgtUXnDhBH_g28tLsEva9l-DlWQZP-zEgJmfp-r4wL2O94x99Ie96FnA3MEVG6HS1laifLUMmH9niHVf9aVd0pGwa0d6Y1pp3VEj-2th_hc0w0xrO1JBTujfvnGAP-7nbc_3DmjI-lIiuDDj17sbaeqlt7KngmCz3pBdgznraQL5-_RvFPWop3NZteZc9PO9UfUeh38oGE7KLC73SlFqh-UQN-r9k-0j9XmDitQXrDO6F7ayRPTv-ajDJOMqZtplEwFAQsFrlthoUEHTBpgPIPcFy3FV_57zc_fc6427fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avpRnSigI0Qyp3E4Bahe1T-r-iZX6NslPgHSH_HzpQ9hOzUGDtanPfpBPU6rLFayE0hw4jum6k_k0hFH0lTVFc6f3zUYP03gT-2FZZJkmvHR1RZru3Mi7CxDALPr-UkquKoXEiz0OSXYLebVDsre6xxu_uta8IkT--Is4KEYGMxIhbY1zhJx4zX4SwBoesRbefv_9hhG_EqeJ2X8zxha898TbKTOf-AkBtInPVpCuyExENMYX8x3jJLCOUJd7yAVW2fxRQZHjLJo22Ekr7fg4ZyI1kIL1dcV9K3RsYONYYfr2wzMmDXjvyKk_c4u9VLUfDRSsm5QnUrfMqD9nnIxBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرمانده ارتش پاکستان: خوشحالم ایران توسط افراد هوشمند اداره می‌شود
🔹
ژنرال عاصم منیر در دیدار قالیباف: دولت و ملت پاکستان بهترین آرزوها و دعاهای خیر برای آینده ایرانیان را دارند.
🔹
من و شما هر دو سرباز ملت‌مان هستیم و سربازها بدون لکنت و با صداقت صحبت می‌کنند…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/437446" target="_blank">📅 15:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437445">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCynmQJaftQ45_yCopWb5_ezlkSlh12X_wQzA3GrPIBjAe8q4X6WDODs_gO_vjQ6DeRMrGBeEfKWhWUD5YIz7uanQ4niTqSdxIXvEHV5pM_zEe5Q3YW_fyuI0jEKtns0d-VSd_AfdctVXoMa04RT1-88FOHFeCMZJGftqTaZpg7XWdtxtLLOslr0co19zI3XIV-B9IqiO0-DNA_ogweFY8Gh7Am8Stx7QcOqN85dmNrdia2DW5GuCPCOTN2vS93DGjN86POQEbgF7GyLGCeEpAjlCPsMZjOtGnJ6gkdGGwIFlcHaAFgssPlNs_aunQ3UHHJVwRfy8xaJ2fCv0nlN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخریب کامل ۴۰ شرکت دانش‌بنیان در جنگ‌
🔹
معاون اقتصاد دانش‌بنیان ریاست‌جمهوری: در جنگ تحمیلی سوم ۱۱۶ شرکت دانش‌بنیان آسیب دیده‌اند که ۴۰ شرکت به‌طور کامل تخریب شده‌اند.
🔹
میزان خسارت شرکت‌های دانش‌بنیان در این جنگ حدود ۳۰ میلیون دلار بوده‌است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/437445" target="_blank">📅 15:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437444">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
فعال اصلاح‌طلب: اعتراف می‌کنم در نقد به دکترین دفاعی رهبر شهید اشتباه کردیم
🔹
علی باقری، دبیرکل حزب عهد ایران در گفت‌وگو با فارس: رهبر شهید، معمار بازسازی قدرت ایران در جهان بود.
🔹
عملکرد ایران در جنگ‌های اخیر و مقابله با قدرت‌های بزرگ نظامی، نتیجه دکترین دفاعی‌ای بود که رهبر شهید طی سه دهه طراحی و تثبیت کردند؛ دکترینی که امروز قدرت نظامی ایران را به واقعیتی غیرقابل انکار تبدیل کرده است.
🔹
مهم‌ترین میراث ۳۷ سال رهبری ایشان، ساختن «ایران قدرتمند» است؛ کشوری که توان ایستادگی و مقابله با دشمنان خود را دارد.
🔹
این دکترین سال‌ها از داخل و خارج مورد نقد بود و ما در جریان اصلاحات هم به آن انتقاد داشتیم؛ اما جنگ ۴۰ روزه و پیش از آن جنگ ۱۲ روزه نشان داد این طراحی دقیق، هدفمند و کاملاً درست بوده است.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/437444" target="_blank">📅 15:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437443">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwTW_aLVzA8rcItEk_nV8NlV8bF1QTYEIXiiPPcmnnBBSWxti3Lho6I48cXq3vOXDr7C5V10gA0aWuEQVuXd_eIl2BfS_sHFWQo4QQ4iDZ5WMCyTNdER-eQ8aC2lQTjT980qzCHWOyZs4O5desWm_Ng31mAIE8LihYhRUV-b6iDolwl8gDiBhxAQtCcgIJup-mlARfxJY_RJ5wbyDyvLGvDN_BKUY-JkLU4rc7Msz7tkfkEkxhaLMiMpSZyHFT7mzqHze3bTBbr1M2cPGP-ONdrVlCQuKFeBTCW9FpwtRMZ3ohdVxt-w5yNRGyOLS_A78anMvU-JOnWdMLD5mRPkTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام ودیعهٔ مسکن از اجاره‌بها جاماند
🔹
با وجود افزایش چشم‌گیر اجاره‌بها در کشور از ۵۰ تا ۷۰ درصد، دولت سقف وام ودیعهٔ مسکن را حدود ۳۳ درصد افزایش داده و خبر می‌رسد که سقف تسهیلات فعلاً تغییری نمی‌یابد.
🔹
امسال سقف وام ودیعه‌‌ مسکن در تهران ۳۶۵ میلیون، مراکز استان‌ها ۲۸۰ میلیون، سایر شهرها ۱۸۵ میلیون و روستاها ۷۵ میلیون تومان می‌باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/437443" target="_blank">📅 15:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437442">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed0ba250bf.mp4?token=o8UbmckNwiQwDfhcRDd9k5-xJsyrV97NUnjejCS1sMwJEzeKKlJfmS0FlIH7J5hDQ6RN6PxLVzTmzszIoVwsj-h30HRnfWRJNd136sIB0NXguz9MTTZLbol-d1TqeyRLUJ2dePiZmRQBnz_4vEMh6GMjwSeWgUO1RP-FIK5qHRxy7H2Or99wCTwanpEmtIj10xnDvzpJ59MQyvJit9yE8JJksdiif9QLZofJ979hteQGuW7r9rUqm89wweBdL4Hk-IZRd_L453OCMVaXkjk36a2x_Ib9S39Nm7VthRlI6VDA4oXCTnI2uVH4XSHRsHFX90yiu6z7ygv4q_EXa48-r7d11-3d6qfcMu7RSKL3bGSNV3SsOj92grgiHXlzIP8L2ybL2A2CoRZEt5WczkjAMjphizq3IERTx7IsVf9OndqHkDN73VX4xZlxhpNW9jN2RZ97YkG9wWPF7qBTQFq9S7HeJUnBLgFYjasat8qU7RGoIPNeM9j7cZNH2KkRU6tHUl8Fa0EaN2kMAJQcYI3rmSjAOdUJEvvYV2YBecscVseK7_88BpqmS-4YF8escXCT0qPp5vXJG7rKhuZMyX4BbLhduW-7wKJe0QtdtaxGTx2MMsdTxsN9sCVF4SiGeJuZjBgtqlXp5ifGxbd-TBHCGNGFJS93S2xRk7jAhzsKZG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed0ba250bf.mp4?token=o8UbmckNwiQwDfhcRDd9k5-xJsyrV97NUnjejCS1sMwJEzeKKlJfmS0FlIH7J5hDQ6RN6PxLVzTmzszIoVwsj-h30HRnfWRJNd136sIB0NXguz9MTTZLbol-d1TqeyRLUJ2dePiZmRQBnz_4vEMh6GMjwSeWgUO1RP-FIK5qHRxy7H2Or99wCTwanpEmtIj10xnDvzpJ59MQyvJit9yE8JJksdiif9QLZofJ979hteQGuW7r9rUqm89wweBdL4Hk-IZRd_L453OCMVaXkjk36a2x_Ib9S39Nm7VthRlI6VDA4oXCTnI2uVH4XSHRsHFX90yiu6z7ygv4q_EXa48-r7d11-3d6qfcMu7RSKL3bGSNV3SsOj92grgiHXlzIP8L2ybL2A2CoRZEt5WczkjAMjphizq3IERTx7IsVf9OndqHkDN73VX4xZlxhpNW9jN2RZ97YkG9wWPF7qBTQFq9S7HeJUnBLgFYjasat8qU7RGoIPNeM9j7cZNH2KkRU6tHUl8Fa0EaN2kMAJQcYI3rmSjAOdUJEvvYV2YBecscVseK7_88BpqmS-4YF8escXCT0qPp5vXJG7rKhuZMyX4BbLhduW-7wKJe0QtdtaxGTx2MMsdTxsN9sCVF4SiGeJuZjBgtqlXp5ifGxbd-TBHCGNGFJS93S2xRk7jAhzsKZG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فوکویاما: افول آمریکا محصول مستقیم روی‌کارآمدن ترامپ است
🔹
نظریه‌پرداز آمریکایی با انتقاد شدید از عملکرد ترامپ گفت: او آمریکا را به یک جنگ غیرضروری در خاورمیانه برد. گویا ترامپ تصمیم گرفته هر کاری که می‌تواند انجام دهد تا آمریکا را در برابر چین تضعیف کند.
🔹
در میان دوستان و رقبای آمریکا این توافق وجود دارد که آمریکا به‌نوعی به یک دولت سرکش تبدیل شده است که به بی‌ثباتی و بی‌نظمی جهانی کمک می‌کند و همچنین به نوعی مضحکه تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/437442" target="_blank">📅 15:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437435">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGMDQbKp8-KkbVsNqUZsKP6ds67FNaP5ARo23GlLRtNMI6mKzRp5qt3KxBpczZ5QtgUH4NiWy7TfU0EASN5hf9NpFAMLH89YCb1gu3KYAlPpELliuva0MW7VgZhm8HLJTA9ls61bTSPWVeuNrmctTnPFGvcvspHWuusaXClIU3gqgTH2KRuF-e57MLnixouhEinDk9cPPSYRDnxPiKOJRQHYSIO2lasIniEJDc0PjCyinQJBL6t8JOiM7gHTOkCGAnY7b6xeDXTT10AcPjC5ZRAs8REDx9sXgKNc5-OEaLMVmpUGjiY858I-j2A24Lx75lWaO2LQ2QqFLH3JR769Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hCzq_YlE39CB-g3CMlLTaaAuDTSDHUTG3v_j7u1ZasKzaLML-5uQDfG8-yAFQq1b88mNWnz39uciCKFJ124XUP0dL721_nIk06qblbMWr9ApEqTVgguhWZz6LLuefz7s8rcVKRbyUIEQWu4AcnATaS-uGA6_8QyyzbsslWtLZSIsS_9se4e6lzKkxO5vda_fobN79x2tZ9E6vVdtCoCI5tOS2sHvqZaaDBoZI4Yl8SFLIqSwIpJEVZ0PH80YjY5Xm5utrUAjU3VBSOVXFfR4iEffbV1x6G69Mtpl2kyuUUpl7FIsvZpEg-1qvHxVBrXi8BleUyS3W_87WY23MXkDHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kbg4M3rE1C9MSAd8CiIfcSjFKxIHFp6E2ZW8ELYG3kzCiDxwm6Wxyv0oM4jA5gnnansIOKIbDwoQ1hEdYkmTSugsewYQmCxuuhiBJAnX1_tLBwmjBwWgEk_abe9mo5rUppIAfBXQdB10MM5dJ81MvML4P8MwsgVvwb0txDGJ65l56ZNkm0ECqirLFiOF-FSlbgVeHKh3iR0jNrWdiqU41EygbynhtIQHIO2J65nuST31lyf3IwWpMBZiU2iFScyMcK3upGvlN7TR676xch_0nlCBc4VhBx7hheGbYatRjPSfzm4Q3VKNRxeC8ylGCwFEOTBesxnMbSnlGU3woIyGgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oDZA1UuCXzh-FZqCG1773cwvAG9zderqehJkqEKuKKkMSLVQzYP5BS2NaY9qbAJ4JzOgt9a5UVPiRH6mXBULSqIn5ECN0M1DFeVLYT4vy-YHt7sxHF-w0tUQvFU8QCEEH25Ci-Q0R3TzkHtgu-7595wKr5_JbryojWPvtZzsSjEnOvDqBfElXEHpLMGitR78L-6iKzUfDru-4zFXWDF-_7oBWdolyw3bsu3_hEcrBzmyGbi_hvth4gSR7tpClIlTCeUO45TUd1adKjXahKVmKU7GJfN8yBDwFK8FK37A4Prv6_pih-rRyhZzrh2crVwoejLkww8lsZG3NHBLbR3IEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCwipgACoLi2cLIPE935Ttu4S7Mn1pZXTRKjBIDh0qP5ZARCfVwG3B0lyHHxMVE_62kblclZjiMRFdyZCGpseTcf2kXwA9Ka-OIEfmWzyA6Wf9K6fFgFJWjZKzOPUq7ZTrbNU0k2ucrlz95QHbHXdRMicwRIGAdmFiJKmsejxiyfYhXzDJRstX0PejLWySBjP6SM8w0V9KrWW01X0efQlnhsxOyN7LbZ7mNtId9W1riziHpxNijtH5pObgUGAep_c9-ZhzoPc-t0-TyE1kh_WF7qq1Q6eQNOCV-CEuYNNlQtSbbuwDM_LPI66yeSvfzTVZ1_mxhfN6macLpHMkkZaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bAh5s-qvp_TnzUmZmaP1YMr6xUfihLXVDriNyNP74b7AfUkK3LwoR6rML9wQPDcCpLfCGfRgmRA9sB19RHDJQfx2FkFJu6My2xSF_3jGFE5vszGl9-JP-F7xmGatS8DzCUTu5Q-EXvJi_U7OzaBGKPNA8Nu7ikZjXrxINEe8eRhVqeStrcNEMiEIVGp2TU4vb-vgLkNq5y3Koaauk6DPYzewUORAQBYBBuOVrOLGMsZcNB5KfUYXe6rO2Y8Td8baHtmryPhpNB470rZs79OSEULBBKxR09ZneysY-K9o3B0LGEcroZPcos-4NPlTZEv7UuW2fbI9V59suxSo-Fs-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAKFamMK65ASCKkhsFm5ZLsi0XyxZCHQDwitQG7JjbExdoPTQ0sUh6uFsSO7X2XqFON18XWew8x9J715fFjQmnCiA1PpqGco3VcAW1JK8I7Jf2O_33k6ddYAxhagzKnho1m39Wbf3QxHKr15L1ksHzggXZwKhIBcS50RkTZ1YKcvD82r-8P9HVUxOEf44r75pnIRMzxJ96LrxHOY5WrD44TrrRF7tUXhu9nzLdkALlvI4CWXYI8dJKG_aQV0Dg17W_ObS0QZNXEWkfDM5vM1p4YsybS8Gff8mW99LJA4zYTfVqFQQyGR85a8G8-3sttAtRAzj4QKMwo1kaQ8wMe8kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حرم امام حسین(ع) در آستانهٔ شهادت امام باقر(ع) سیاه‌پوش شد
@Farsna</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/437435" target="_blank">📅 15:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437434">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yiq9Ge20GiCkFNm58Kj_Hcd2qdM6AYsF6Ccb8rdHEylhhrpka8AlzE-t0mOVIom_XsP8LilmEDtk7T5E430dwgjnNcF7Pq_zfdeYT9Nqf92bdlH_lgeo-myCn99zCeJLnDE27VPVqyi_UW0a26rrNAqlMQ_aCPV4ywWsxWmrxRI5HzYDDyXasRR0uzDtBRAxemx-6mf8NEQq7zfKx8W2q-FIIIZOlABXBUtr5Xo2KbSG3gPGdimmKUKdLCRVVR0JLik5Y80anZr9Kj5Od26YnlxOmsH64nsOpsk_yX7D8TbqLLH3ouXFZ6fmDMGdtlDgw6Hwd5OnQ3fYrloxbT_Lvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیر رهبر انقلاب اسلامی از میدان‌داری مردم سیستان‌وبلوچستان
🔹
هیئتی ویژه از سوی حضرت آیت‌الله سیدمجتبی خامنه‌ای، رهبر معظم انقلاب، به عنوان نخستین مقصد استانی برای قدردانی از ایستادگی و حضور حماسی مردم سیستان‌و بلوچستان در دوران «جنگ تحمیلی سوم» به این استان سفر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/437434" target="_blank">📅 15:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437431">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jkYMfokpC-idnejYFAikDk4zq7IcTp86Pq-LxHmtZUijSYQqzr_ceIcYq8nP_wi-KYAphq1vreiEOGWDbMSY9WGP-_XvWhEET21kpfshl9kyOoHhUptzNVF5eIqzgno03wIe1qFpmxziqCXvkDv7hQmXciUoxhJoksVurtBvbfFad721KYKUvVm9iN57t8Z_ZJp7XYbNsYdwdbGw7AGpKWyu0XfD6cVJcbPZKnroN_rziHFe0s8vFyI2B32o6TBubD3FDoxgLSqExZSYMrYFqD7H4YTCJSA4vCFbz-xb4vWd5F1OBx4AnXK9nURyRvs9cweKZtJ4JbB-rXijGb7jUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IczHxmAu22SkCRMPceHRseXA_Liqx1IMwdar7McEpE1tfb4MhqpTK35c6jxp1DYqQ-h0-qmwdQ0fx6xF1ZePhdFeWxZrw-C0uSzkUruwxDFdBzQKRPjOUf_Sz_tKJHQThDk_G2uDh0HmGrEM0-x1a8SVMgshex7eRNcnwEA63Ebj2BUtFvDbGPP7nTYddkuqbYO_k4R6wxxb_Xvoxl9zWAVnGjeWg_5ZMuro2IyQOYcx_TVkZCsruAJmW65mpRTV3X__crl-EDCNj_A6ZvH5U52Q_d8vSa935iFCp663Z_sd7RLySIDEwqqPc1a0vWIO3k6E6M_N8O7ilhKGtwFnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ILx8TPTI531PSKaQmMqQJtGuUrok-ZKtbILdcZShBapoYBfko8YMiX_CVZMygaGcVyqVqwmMdMqHrcicq1G697k50Xk7JFP3RmSAxJg62PgGTzoMUprToGnXaDn8LYn_f-dashI1WxCzaVNLPcbM0N8pPgdcr5CWtThb4BAodtU4rO3LlsVt1aROFkV_cHZYcLCzFkfFjU0uU-PwWlWkZ2RYBkq5HAf6gfdSa-1RPooh5DtDG7copk0tpx1kbBIrbjIPIEc1MZNFftF8ImqggDLsBrm3VpiEc09WEMOvTe3doPkGgf51k25kdtAypxV8psJ9S2rFBjvNC8krIDbZSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🔴
قالیباف: در صورت حماقت ترامپ پاسخ ما کوبنده‌تر خواهد بود
🔹
نیروهای مسلح ما در دوران آتش‌بس به نحوی خود را بازسازی کرده‌اند که در صورت حماقت ترامپ و آغاز مجدد جنگ، حتما برای آمریکا کوبنده‌تر و تلخ‌تر از روز اول جنگ خواهند بود.  @Farsna</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/437431" target="_blank">📅 14:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437429">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EG5RgHjbGV-S_EmhGSKwI3XxGquxZgqZtftWyDHl1BxBpR3HDrTLcXS4wOgAgJnKWi5F6XTgz4XB3zz1pUR-phfTu1hcBssRwpiq0RM_oASn-3BK3faA5Glgj-5moF6Yh3U_sA__Diz7-v2r0Hci2oIymFhPZ1yXs-etFVi0QuIdPcWCzoWItcfSQ0Q7MLlI7nguoRAriQ2YOTYjURciz5sAZLROXOczqPasXATfQejol9PdnM4HPJ_wkdAR8jx1kzzXfi55_woz3vHJO-eYJEfev8xZhaYzALXyOdAYzKF4ZnX_RIV-pCeEkHVY-Ukp59SvQowKoeKLlY_J1tX6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPLGuMp3N6T2JLQr0i3eF1GlwCeSHts66w32_YORQ3lOyJkUY1Wz7tee6Delh-RdYmfpprYoh9K8droLvRa46aCrU52MCcILJ4NPFi1D5Yi5b0a4fOztlrxPBdiHN4BEbTSp0WTpiSVDSqvd9Psw_wKlGcAn3yO_YslXkPllYhh1soKbfosxB7XJZABxWbSIrOjmlUa7YlRgrVclfqh09cK1GY_DGB9Yk_qKZ47Hf2YlJwhuN83b2zeOVuy2-iEQwbK_ajCWbQAUzlGh20GO7XoWs2eifVoA7YY50aIKb5TQpp8qNyYwK2o2iyWIHT6t9kHPo-h6LBPgVyix-xU1SA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سقوط بالگرد ارتش هند در نزدیکی مرز چین
🔹
بالگرد حامل یک فرمانده ارشد ارتش هند در بخش مرتفع واقع در شرق منطقه مرزی مورد مناقشه با چین سقوط کرد؛ سقوط این بالگرد در منطقهٔ مرزی لداخ تلفات نداشت و هر ۳ سرنشین آن از مرگ نجات یافتند.
🔹
ارتش هند به دادگاه تحقیق دستور داده تا شرایط منجر به سقوط بالگرد را مشخص کند؛ ارزیابی‌های اولیه درحال انجام است، اما علت دقیق این حادثه هنوز مشخص نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/437429" target="_blank">📅 14:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437428">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
حزب‌الله: ۲ سکوی گنبد آهنین را منهدم کردیم
🔹
مقاومت اسلامی لبنان: ساعت ۹ و ۹:۳۰ صبح امروز ۲ سکوی گنبد آهنین در پادگان برانیت را با پهپاد انتحاری مورد اصابت قطعی قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/437428" target="_blank">📅 14:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437427">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‌
🔴
قالیباف: ما درحال مذاکره بودیم که آمریکا جنگ به‌راه انداخت و حالا می‌گوید برای پایانش مذاکره کنیم
🔹
در آتش‌بسی بودیم که شما واسطه‌اش بودید و آمریکا با نقص عهد، محاصره دریایی کرد و حالا به‌دنبال برداشتن آن است!  @Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/437427" target="_blank">📅 14:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437426">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قالیباف: از حقوق ملت و کشورمان کوتاه نمی‌آییم
🔹
رئیس‌مجلس در دیدار فرمانده ارتش پاکستان: ما از حقوق ملت و کشورمان عدول نمی‌کنیم، مخصوصا با طرفی که اصلا صداقت نداشته و اعتمادی به او وجود ندارد.
🔹
ایران همان‌طور که با شجاعت و اقتدار در میدان نبرد از کیان ایران…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/437426" target="_blank">📅 14:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437425">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrUnhVuKi0jQtbueJjQf_nGYkVT2tFVyMtEGofoJK0MDoS7itWz92wAEiJuktPAtpShfLxxe6RbI6OWjd-23LmYdOLbyRvbmdmGLMCXH259DzgaCxoOJ-Wt2p-wviyT49c-2YxVyuN-C89hIGEp1vujVS3y5kiOEwaWW-fsR84sL-tZm_SY1tepLwwqDR8a7SD1DlFxdQ_UgbKAE6HRChr8u_cdHE84VRuA_JX6juf7yIjUO6qm6yTsOwqsubDuvFYzpO5sSgrqsc2Tse1YjhZRzY_l8HE7tjVvp4sBFVv__EG759IicoB7i02xtuisGm1zUmOtXZysPfnpaicDcRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عاصم منیر با قالیباف دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/437425" target="_blank">📅 14:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437424">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">احتمال شنیدن صدای انفجار کنترل‌شده در شرق اصفهان
🔹
سازمان عمران شهرداری اصفهان: به‌دلیل اجرای پروژه‌های عمرانی در شرق اصفهان، احتمال شنیدن صدای انفجار تا ساعت ۱۵ در این منطقه وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/437424" target="_blank">📅 14:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437423">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR_d_euR8798mk_6bdazRy89oGN__CRo6sejb7x4Jp2kzWKp55jq2odYpwltI6H-4GjVJ-boplWErlo74zhOty-ESr6MEEJspBLuODnMmhD9RNKYNkKd42dEpObcqojhxvYrg7-P5jEu3fAV4euL5gdomyrbD_1ErD8LG37AMqL6ZuejhDhbEbdlfYQtthTA10QtFTWP1fkRir5MxoQWH4sUgVrJ40GIPpUe0E7JJiitaHVMdVssN_VdE5cuNCh_IsDr7Y0GKbmqenqnNUdLYLntpB9FsasHNacVEjFOAxOe4OXMSErbQj8SvQVUdsHlIVZ4ZBKedllTuYTSw1SRdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در آستانهٔ یک ترسالی بزرگ
🔹
بررسی تازه‌ترین خروجی‌های مدل معتبر جهانی CFSv2 نشان می‌دهد پاییز ۱۴۰۵ با آغاز یک دورهٔ ترسالی گسترده در بسیاری از مناطق ایران همراه خواهد بود.
🔹
از مهرماه با عقب‌نشینی گرمای تابستان، سامانه‌های بارشی غربی وارد کشور می‌شوند و شمال، شمال‌غرب و دامنه‌های زاگرس بارش‌های فراتر از نرمال دریافت می‌کنند.
🔹
در آبان، تقویت رطوبت مدیترانه و دریای سرخ می‌تواند بارش‌های سنگین باران و برف را در غرب، مرکز و البرز رقم بزند.
🔹
آذرماه نیز تداوم ترسالی در سواحل خزر و حوضه‌های مهم آبریز کشور پیش‌بینی شده است؛ شرایطی که احتمال بهبود ذخایر سدها را افزایش می‌دهد، هرچند خطر سیلاب و آبگرفتگی را نیز بالا می‌برد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/437423" target="_blank">📅 14:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437416">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gzpt1aqf2YYUhelY0rp8kPYBtWQHrRWqOeIzf0e_YLyl-_FQYfEGp8CLO2VP8UwjGzgUwEZXXw95050iVa5Y95flYv35AtvqiHk1KdiEY_z5dVTD2rQYE7Z62ufOWFQs6puPt9eXryONh948Qw0tiO8KuwgRR6SxeSWFH3pQ7xh2hzEbUX0FzWDTFBY8iOyWpuYJOAZkkAWaQGixWTbg4NKbHOIUJ7vvU-T-k8yjRcS0Dx8ixpjual8hdfHLH-qgZwo7kgxpyDgXVTR2ZjJojk0mvJTKQYyJ9TRXiI1lpbrf9G1_MJiWVnzXJ1kuqD_APJnSEQ8PamhCewdhHiy8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2aHMtr-6B9G_CuqXIYMFnwnN0HnQsraGpxFmFMieL-l-Wh3xU2uC9btP64vIzYGMddVvJRq9uWAcqM-xD-gma7lx8hpxoPjwTcKhQzExAqmluucoZNFyyusDkEK1l1MnEUkrT2joqHiS-q3hFOq9EhwY9kDZxnfXYy0_Ht460kNx0t3QsEBR3UvMrp0aHGH1uIQf5EATwBmYOdqim1MWE9O7lyVoWncs4Lw8W0fo05G8VZnzLKuuyVukBmis8Y0HBndqw3HRd1LPbzZJGg91ggOoMAo3ZTx-3t55f0ibTBFxI4EIizYjl4COhJPpJCZmNIBBRgarNyp0zrZJjO-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DVGuL_POg8Hm1gR-oMqMdNzpDkkfWVm_0UciAOAjt1OMvrTZ3qxEsXZTwRJQ2qGoGm1PHVRtoOkV6D_3upSWrKorr61Y4WavCXZbhASlH5YbaOPHbj52n09UasENEwZyHtFn_6Ysr4JjK6Z_GLhRycGCQbAkKgsOrbxb-BtXmvKjvKyvMfJaxgdh3CxXJsSHBJ3YBXusbREfuLGOeXaOgVCcZGbwatzyivM2gAtQXW7CZ6gx_x4UnNompVl7_AS6NB9gVA0OrynmUSZnOuNqbtDNJR58OYXICYJuaSBurxtrAC5-2fWdMnVYONBCptn7DKOd7cVb0L4gqjxpnkIveQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itYFdgYKBL-au_C0l_FuN1OhAzh0sGSJdNkLDMu5hCdNnIwuniR4rD16Gr414raNIIRqbY0FOG6wlDe5i57SpIFbxfgBG57kNb_zfptNuutCetErhNkEOK1eK9Qmg31P-1WCBGKt-wqOf_JaR2j7Q9wA-hnOsKRfzDdn2d7uVojLGbt-EcQsGhpuQLrGkT76ecgwVj2cBRSL_TgANcIwd5Cz2CsCswWXhVAOBFuxkBWTR7sKy7dDPGxyQ21RVTlctW2TFU4yo23L34uLnbtEcsU8OIRiHNioPA8blVhsKA8Z9c34zHqFMBfZOZDxdIHrPdLg3rAZIhk7eRrkgZhLLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGPSJC7mYSEBbmdJzfZfGTCv4o-eiWRC8gM-5tBkFZQXIHIGBMT39-xcRFmNAL4TeuF7U4y6zlTH9ZJad5fkWWuph86PTuECNiDIzXrs50qCn-kHF_jq0avZ11pwtFfzygliFf9DlZ94Qh731MrE1Dxcnd61mqP9Ts6pwQM8Jzk2FCakWFitcWWUOGup_Lt33sKavHBh2mRd4Qlm3XKqXZqywXlV-WjTvM36U8nYA3j7H6HSfOfaSnlEZzTqHi5tXyGqEuQMul7IMGLe_8_nYpulh1GBThiGZMtCss7WQ0s1jqS8i0EkBhLF5ucu_E4Bkcxczyv4uixCD1t5U1U6XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAeuttkPS8rriQJi42_pKeY58mMoUdSYgD3tZ7Ig41iEmoZFu3CaLO0x3KSnMzsCZq-apNUzmxOLwp0d7vDQLFtjbrL1noz-yBZds0GkLqsyfhhOzrZdSJtXdOKrUFoxZKnMSOf9OxJ9wi05I07_lFP7ixrzWb3rIF6E2AYf9sZFEDBdZWwLqY9X1iLYm3HeVu1oQl1Dvip_cu3sjrkEsIrPwdI2lIeA-_37BdWO3eo2xqAP-4i-heL-rmWRkc7iMEvB-USRuXxjzOLXPt5iP60zJMqrjEu-nyGU2WEQrMJSi4XZwhj1jCOQyTx9nmo0aHZZcMuUoPUR3d7qbXpong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/beoapVvSj0XjgitltoEvdWeZC2VuQZD9sfGwP2lqfOpgJ_reoY9H5XFsD2OJHeVklt6bofKw1uDh_6uAMBZG2Gl7mN0rewQ8NAC-2FUjs4zbR2WfdB6sizffnAWB89wEJJ_8xgxmG-adQ93rJmjY1A3gzq16r7h0PME6JAkgyJD4pmRrK1yaNu6oIdOyzJOFmCLo6n6e1hYU5eGpiriXlRqgMAZterxRLQbV3Ji9BhUB4_6ZAnyWvy6Y1XvAX5WQdbawnJZXd-vVSsMfTRmNzrcvzWMwurPLS5Ph-t6k5Kvwt8pJJHC0fbyBe0smL9C3fBgwkgxuZ3a8Pe41EWJFgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کارگاه موشک‌سازی در همدان
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/437416" target="_blank">📅 14:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437415">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رهبر معظم انقلاب درگذشت مادر رئیس جمعیت هلال‌احمر را تسلیت گفتند
🔹
حضرت آیت‌الله سیدمجتبی خامنه‌ای در پیامی درگذشت مادر کولیوند، رئیس جمعیت هلال‌احمر را تسلیت گفتند.
@Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/437415" target="_blank">📅 13:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437413">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDumkzOnPCyUS_nX1z7WMQsF7T9uzSDM5sOkQiWWm6cKYzZTzxfxFqNUrHxn6rcsej67xNOzFQ1Vx7uj5ZKLchMIbZJsAAn8HP2ZcAmhm9_xSSr8_JPlMerD9EPOydVEzp-5pE-UhfO1Cmi9vtIGeZ3zrLLmHevj6QxyzKcsZAoYgIA6pPwETP1HCP1Lt8GEnqVh3RP-8SVF4Sfxgbj3Q0M4Ru7XjknstLYbikO_V3n99DM8uH9rFXBTTaIF3wYc5WP1KEEWfzSpyoGPBQqM_xrDNa1eTt5GmwJURdk2HNCEQjxy1KVYKus9JvYDYateghay1cdXHNPhqCNMJEFVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUHh4C5SouytAsRpLmknQUMxNnMLpg-hxpqsO3SqJl0yZn3NR8Jl7pUIWiLLazfnyIGOy1Sm5TkNzIXPt3cfdWfNfJ9LbxSmGS1B7nfoUJpeXOO2-MhBf_tnliLYQCrWNR3wuS6ddL5Km1s-2TAG-o71T01W-5G4v0Bp1iJEHEmyoJyMSbv-zsI2iXBPKW29szKuG4wq9zTjpRZODGOlnqUIBBAmOpIaP9ANCXD9wvO2-4xFaaEGDGZp2-ssBOaxSjDsvJ9J18GSAn9EiKCKQJama0Js9G1zuTXTHSZR3rNL9kKVNhsSILp7jbzD_ulliLAei1CVEMyjjrdizjIDhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عاصم منیر با قالیباف دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/437413" target="_blank">📅 13:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437411">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSE8cSLA_B-u7BSq1wa_I1Gq6Jwl_prAa2rBu8mt5KVbBMZY7yoybOoQcGh-gsXfy-eD5MtSAzNoGhyTOf1McJfinNz66t37ZKNCEgfDzmKdTg_BYzz8bcDk1611UnC-zsb5HuTjMaYXtQXSnD-HSB0opzLcin9g-_SIs727uQXpKHM93i2LiUU_mn4Smmt2hvSrsBNLySWcUj09BNY-fJITAu_Yq_SLHYwyD7l0WiURU-syIOPOiiYAqRKq0W6h8D0ddkIuFlxAT1ghnehmZ8fUPR1GTgmkie-9qPFPJwrVbZPqSyDuo51F1tNHqjTi3F9rlx8mFtRKOxQ_RQ5u7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBtipVJLI5pJ-ILsVQSKlXkTgeqrMcNQI-K8a-w-YTZYSLSI0QIisec55UxhyMubX6utMWtzfUxC9YFlFPfWQ37JO4GmlAgW4xwPlxBtdAazw81LYQQrsoccNDYnqlSlHnBocUwO8Vsj7WDAlX2IlTGsyVqWxe_6bZ4WlvCBdGEnJ9kM7IfYb1S7Am7PXvzVQV-h_bbHHxeOW-LpbCfxNEMSF0Ipz33IfWtECNW-ozZp1OEyYghOnEWeiM-NNq1bI1Kuj8VVubqEx15PsgNAopkPaSXycJDGGgA3mbZ703KH-Zp8C9vJQwOC0asN0CbVTuyizO4i-cVfINYwH9ltmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیدار فرماندۀ ارتش پاکستان با عراقچی
🔹
عاصم منیر که به‌منظور رایزنی و تبادل نظر با مقام‌های ایران به تهران سفر کرده، دیروز با وزیر خارجۀ کشورمان، دیدار و گفت‌وگو کرد.
🔹
در این دیدار که تا پاسی از شب ادامه داشت، طرفین دربارۀ آخرین تلاش‌ها و ابتکارات دیپلماتیک…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/437411" target="_blank">📅 13:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437410">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPb5OsSFm1oCBuTcfbUS5fCWhZ_bsq04zvlWUGYsie5j07Cs3atle2f8qy3_FTcsHT-bCkRCiycoJmmnQhH3nmo2xYFvUiqbg9yre-HltwgS-vWoS4cU2tWu9ncOcwdBjjSQweAtaQCdzzRRpmm1TSmxSrTHDoVI4d5eo7hgE47owhqX-hrEVsDff4cIaJtocSbteBGXLo1fT6rizCdEqnMbVSOnPzwSQS49U2Q2lOq1VEospCLrygpo05cHRCAA2qvMNvvxZLmgOYEp_Te8cBen66-eozyEQXhSFP98N7_o0CwJU3Ktl86TQ3nKykkuUubdfwE98WRwcCee-UkAAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ۷۰ هزار واحدی بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۷۰ هزار واحدی به ۳ میلیون و ۷۳۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/437410" target="_blank">📅 13:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437409">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUB4XN_ijHNpbA8Sd2hiPSPjKbl3duKxdid911D2oT3fpSEZJXq8bJmItjdy4rDagYE8nZtujUAePX7K6HxY51cTgmJWy_nR1Pabf0evHzlkYlpSrUQNUKQkT2cMcfUe0maKg7imQHpCQOFRTZ1xNfbYyDpZ05GkAZsML-0lzO8IIC7sqfo_uxqcbqk9ZK0vLHPzivSZ1PsQD1j1dhD0hwzJz-DTBoG-OHvx0O7aejvK6zTzMV9wn4jAtBMLcF-sP0aMc-5EpqURgCp9VYhWjCGKtAvd8YP87hPWNQJIx6TR7stFWmiwc9cXlVRG6memA4CyKlgY5RZSndWCgDIItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش متری خانه در تهران آغاز شد
🔹
مدیرعامل سازمان سرمایه‌گذاری شهر تهران: عرضهٔ آزمایشی خانه‌ریز در تهران آغاز شده و از این ماه کار به‌صورت گسترده از طریق سامانۀ شهرزاد شروع می‌شود.
🔹
قیمت خانه‌ریز معادل میانگین کل آن ملک است و افراد می‌توانند از چند متر تا کل واحد را خریداری کنند.
🔹
قیمت‌گذاری برای این املاک توسط کارشناس رسمی و در روز تحویل ملک انجام شده و به مزایده گذاشته می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/437409" target="_blank">📅 13:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437408">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">محکومیت
۲ عنصر همکار دشمن در سمنان به حبس‌های سنگین
🔹
دادگستری سمنان: ۲ زن به نام‌های «لیلا رمضانی فرزندکمال» و «فاطمه ملک احمدی فرزند احمد» که با برقراری ارتباط با شبکه‌های معاند و ارسال محتوای تصویری و اطلاعات مورد نیاز دشمن برای هدایت اقدامات ایذایی علیه ملت شریف ایران فعالیت داشتند، دستگیر شدند.
🔹
علاوه بر محکومیت به حبس‌های سنگین (۲۶ و ۲۷ سال)، مجازات‌های تکمیلی قاطعی از جمله انفصال از کلیه خدمات دولتی، ممنوعیت مطلق خروج از مرزهای کشور و محرومیت از عضویت در هرگونه احزاب و گروه‌های سیاسی و اجتماعی در نظر گرفته شده که درحال اجراست.
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/437408" target="_blank">📅 12:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437405">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada4667039.mp4?token=D-g0cEt2jMGTEUpYaIZEtX8EEys2adg3TOL3T1CL7TEQ_VTbolH_5Lem5RhcY4fmD8SJwZzBqYB4YJQmitjcRkTvcD4OYGoiwIr8IJtt1lR1noAjBNrQbTnM7SkUirDu11c6kGDjyBMDUZrXMKCV3qIyVHohLzYzIcGKHDKmomDXVq5BfPR91XKx_E9Z6P-bMsdX5FKDjxbeEOHh0BCGmmTX79z_DfIIxDLk1i8bFk3WuOy20jddYPG7jzG1E2FC26FS4RyFhiZ5qIRBbU3iP_G9MPdUQ4fv_20GZU5P35Kkw4ZkwONN3OnkhDx00PtJgUr0OZF7kxteXy4CyCZT7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada4667039.mp4?token=D-g0cEt2jMGTEUpYaIZEtX8EEys2adg3TOL3T1CL7TEQ_VTbolH_5Lem5RhcY4fmD8SJwZzBqYB4YJQmitjcRkTvcD4OYGoiwIr8IJtt1lR1noAjBNrQbTnM7SkUirDu11c6kGDjyBMDUZrXMKCV3qIyVHohLzYzIcGKHDKmomDXVq5BfPR91XKx_E9Z6P-bMsdX5FKDjxbeEOHh0BCGmmTX79z_DfIIxDLk1i8bFk3WuOy20jddYPG7jzG1E2FC26FS4RyFhiZ5qIRBbU3iP_G9MPdUQ4fv_20GZU5P35Kkw4ZkwONN3OnkhDx00PtJgUr0OZF7kxteXy4CyCZT7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌موسایی طلایی شد
🔹
مهدی حاجی‌موسایی در فینال تکواندوی قهرمانی آسیا مقابل نماینده کره‌جنوبی قهرمان المپیک و جهان به پیروزی رسید و طلایی شد.  @Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/437405" target="_blank">📅 12:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437404">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عبور ۳۵ کشتی با هماهنگی سپاه از تنگهٔ هرمز
🔹
نیروی دریایی سپاه: در شبانه‌روز گذشته ۳۵ کشتی اعم از نفتکش، کانتینربر و سایر کشتی های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند. @Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/437404" target="_blank">📅 12:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437403">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c569f870e.mp4?token=XpZ3Sof8l-32ohHvSQcQsm9mJ6yL5xnE95HI_mT8OX64_lECCau6NEbAhpMT6hV7MxeihEEvhDyr1UNqFRA3DCpFmNs-PBLsFbb52tk3hD-2t3xrdLs8JkQJEI3fr_Mn_h78qy4Y-VjpetK_uRvRBcxLi_dIAjlJ3CuHTEogT-_22z2k6bnVIqV6pGTtlVpUP35BtQLP9hp4xxp3-d9Y_pD7l4dw09WUcBJNAEF3oAj3-O48sWmfSpANGBHqZ8IjWAImvH0tOJkpEE0c3081vI2EFqkKiqfkuwofFP-Un985WltIPLR4wKUqQlJj-XWJCcf2KwwXCBInEOyd-RO2xzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c569f870e.mp4?token=XpZ3Sof8l-32ohHvSQcQsm9mJ6yL5xnE95HI_mT8OX64_lECCau6NEbAhpMT6hV7MxeihEEvhDyr1UNqFRA3DCpFmNs-PBLsFbb52tk3hD-2t3xrdLs8JkQJEI3fr_Mn_h78qy4Y-VjpetK_uRvRBcxLi_dIAjlJ3CuHTEogT-_22z2k6bnVIqV6pGTtlVpUP35BtQLP9hp4xxp3-d9Y_pD7l4dw09WUcBJNAEF3oAj3-O48sWmfSpANGBHqZ8IjWAImvH0tOJkpEE0c3081vI2EFqkKiqfkuwofFP-Un985WltIPLR4wKUqQlJj-XWJCcf2KwwXCBInEOyd-RO2xzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرکرهٔ من‌و‌تو باز هم پایین کشیده شد
🔹
تلویزیون من‌و‌تو، شبکهٔ تروریستی فارسی‌زبان مستقر در لندن، در اطلاعیه‌ای رسمی اعلام کرد که به‌دلیل محدودیت‌های مالی، ۳ خرداد به پخش برنامه‌های خود پایان می‌دهد.
📌
این شبکه تاکنون با دلایل مختلف ۳ بار اظهار تعطیلی کرده…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/437403" target="_blank">📅 12:27 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
