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
<img src="https://cdn4.telesco.pe/file/Z3Ch8Y_mxb-anIyJIR8PBMgI8u5-UGKPWkvQCO4lOV6FJjib6ZQRPAHMIcHj3V_iBPdm8-IpO5Iy_wl1WKkOt-qEjJNWPAtX-J1Yu-yz4WsfBDUK7iebyBfDN3KFs1jW8_7mOXGuAM-2Amx_K-aQO2NrZ8B8q5-Dfdjg7QGNsCOvvWF-NltI8nzsTCcUVATD9QYsCPVNlYoX1dtYkXejt75ldGGjW5Bnt-Z62iqvTQhz6ddS8Yc6OBN6NRgUeUe0J5Q_S8kCXKH-qXDOfpqvpHwuwDxKpJfZHfelfVUPxYXB2kibrO62yLtSdFHJmlVpM-aLou-uEkfevvKaeLT1CA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 612K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 10:58:31</div>
<hr>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN4XLSHvtvBLsXKH8UCu2yhZvaggDImoB3mDvmvLc2TjQ52HdlK6jNHBc3NYqycm9bVS0szv4Xm8B2Fj1k-1Jw0CWoGfJyK3-2Zi5b8WmMmO5YC5VX9naIFYXI3Xg8C_aOb1RzyLMgEu51Tq98fV1ydRcgqnepcvALwuoX2XtJ5MNsFdlySi8nPROIN5XIYnxaPZZEL4Y-s7y7Kd6JBfAcMbZBwRuh0Cz9zPVgjMf4K1pzo0uDb3DL6wj1jmii-TasdRm1thkKylS2w25IaBrH3BIEc2araDnws8z7c0ra9KeFrNtwK-gh2CVCDctWhyPCAUQ_V7ogYKhyrOFD2Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7LhOHECopCBunuZXulm-XmUww9iv-6qDXYY9_40uBMP4tH9BLaEguQ8dsIqrh2XcOvs7dZqxd0Qhkz2ENw8Xvp0IKw5qnHTYqC-kmgXmBeQ6yY6y_xL5OFwhLfsIRWxBYE8LalIY2Tg9rDsUZUfuHmR4pGlea0vylHOSwF5tipNRJ_KpNjZ_I8YfvDXOVP31dbtSRAJ3IoUb4NSKCrUdnn5mrN_zUTR6j89dMu06txU0lRQFfIK7A7zScMBEd3QFj6MWewK5J7HuzTOBk5xunGUkeRREzUL4NtfSB15haXJLC3ospK5f2f_SglcTSBg7G_g8lnkhofl68BUITjCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoZi6PF7VZJWzMFzkZKh1qn9FsssHnQ2Bqxhs04kqfD6nFywy--emJ3MFsuRAW4DV_8ARMPuXnRZ4npC7-tSqQWWL9OINw6-28wPVUb7HOB3cFyAHAhZEkOV8xidQ8m9EjoYvugoFeMsOQh0Qhe9rbf432EhQR5fIywhNsQwSRG3mfA5j0Ef7VmN_m6DlwsGYPimajwzJWoDhJMDJReUf_-j8AlXJeK1PNd7sXKr00QxmKAFWAEujgJ9lxuRwgtkayB1rTH5etuDayOD2JLEuM5-BAgDvPhW9Qz2ye3hTeCtRcZ-CzXixNM1HqCetFfMyDEJgwNzl53hFCbTL5zVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UikECKDFSrKlAb3urrHBCyT5tFNVx29R-tDqJ2lr-vgT1e4rDf09UWIzG99YRKVPD--hF7NZ7_r7DVO0kaG_Do-RJ842LTY6jRiEMlsqnn_3p4AFREQg1Z4Q5WFt9uG23j_HUtmqz7jwvpM-gMbf7Obkr1GK6jCF9jAcCORAggfW1zYxIab4qhZD2cW18PKtxHNO4HakPrYJtfBvvRVZRnVQ9KJ0PyQNsfHcfY0zqPEyXXoKJcOYsh7Q3zmiIBTmAtLfayRicuH1-PpxFRFMqo3wGP2MyAijWrV8Mw8O4XT7SUsO7IZQLQ7eqiR6hgkOfB9NeyX6350BN3gdKWJsmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=bCn7KhNtg7NpJEdPrN7La-2xapoOKAq6Z7_hpo4zF5vcg6zA2S5x_MddrpVCoKvMwnKdJorA76XVdveW0ip_V3jXHVPGyaSTDGCC00E_gZKxROMNc01cdCG2cQTeNpJDNG81d170RdxNSfvwHmE7r43tDGmxE1yNUbBSTf8d-GyMAOgW9E6ig4bYsYDV8iiVGe4ipWu_4xG7zLk6s63feZTgTKB3ERTXTVJQQ4hG8ghI9gbf5o6WWeGkFL7fQR3gFRr1Pyt4YF44P7sQdESF3iELKR3dS5aLhbn6BakcbFJyn3UgDgojdDu49AB-IY0L6olpKh1hVtoY_uGz3DeokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=bCn7KhNtg7NpJEdPrN7La-2xapoOKAq6Z7_hpo4zF5vcg6zA2S5x_MddrpVCoKvMwnKdJorA76XVdveW0ip_V3jXHVPGyaSTDGCC00E_gZKxROMNc01cdCG2cQTeNpJDNG81d170RdxNSfvwHmE7r43tDGmxE1yNUbBSTf8d-GyMAOgW9E6ig4bYsYDV8iiVGe4ipWu_4xG7zLk6s63feZTgTKB3ERTXTVJQQ4hG8ghI9gbf5o6WWeGkFL7fQR3gFRr1Pyt4YF44P7sQdESF3iELKR3dS5aLhbn6BakcbFJyn3UgDgojdDu49AB-IY0L6olpKh1hVtoY_uGz3DeokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqXzCkLIMtXGKhY1O97RiCxHAooruwT1CcydwUKIGR7c4kzrrBavHDWbMtLLTzR2tzxQdWMZ0fWuHxP0y0pGK4coEfeeeO3F1aCMUvC-FIPU0-urBOZvPgulxdWVdxrv-hOSWdXYXEz2C_FoqTYBNn8dz5HVZuPH24nYC_WfPaa3XurURkApQHkOmC2a4efCI2NvJISFrd8anb1Mnx9VWdxYixmCeSrpPcfgHeVCgqmBiohzf2NF5xFxBhZSshqxXWWGYpIUntpXAqnzl1kT-xpGkIHn4BOEuhtryABfgPR7BPMWm6hrUQO7HQLFKMO4Xm-WswM-y4ZU7LvCDYmXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZKLAlL-ExMUGqoAsMb5D-v1kRt4HxjhzSKljxcWCJZXjRFCBhlm2gqXHzfRlpwPVv6GohTe9mIG33ONT4D0gtlkaNQSs3EIn3ltzS58iQLY3vLb5oul18wZ9f2Bkh0KJ6Yv0OmOVV2raLhkcBhMFWjKuBQLarQsfQbeFTstkAqXsvk_BFv3Q-Y-Unhvl6LgBD5ikwuyXgBlPTs9nV1g_6LiJFaoM9xiOWpy2FPDr2dZvhfktSZrpmHtfaQ4UQ1NkvHlcAADss3my_qyyDIbNPUmHAFRxs8lEm3-DQDIZfgJcNY-ejKCmQR3AqMD0POElobLEcDL2zEM5E9cnso4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26790">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAl5Kmib6uheLTBuyPIoMfYKKg3GdJjXj2Ell-N30o58IV1RWNpKqcPELlCLVWfBQdbIRwNCqKfMByjtXq8qe2htt2gQR1gbqJDH7ZmYLy2KfW3EKFQwXE1yZN8DhVC4Iql0-ZOsi-90Kd1MB0yCdb3U2gnhD7ffp-ZGRzYdidYX3zUx-GVG-5pVa4ZvUD66Ti9GVhUk0dnWDE1B6ba3aJZ8ym8Bl6pg5UptKMOD1gyKW_CJbckqbQReR4jXj9SOOgq5_kJ4PssdWc5X2Sa4qWY2HTcNQIKtn4JyfPDsO4KnMxdrOV6Ay5u81kPGWQ7NeKxp2RyM7qrmDcbY-uV1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/26790" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4HoJ6m5_qruuKxpO3Lnp1nyXDdFHOqijscSsCV1Z3cIJ_cO8Wyy2AQs7WmN4CHgcdcuCmTJWOSE1kLEQ-mHse6bdEttgohjXYmEOQ7O36WRDcpraF-K7rA3BioLgd_7DeKZNdz5phiBR33Bfp7QMOGc2JUHhdQ9tDEveP5oiY9ZefyOSJXr5wKzYYf14f2z_qo3NDshZnBAbiyFGwb8sVdK-n9u2WQn551aQOIlmBflamwosMULxmbT_feZL6gI0LxEWHaG3fsVXL0809h9hlqv167D_eZI-J7lbcWkgjDXIrJwJJeaeJJVRRSDXZgAiPLDGNM5e1O_OA7Dg099Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wie6JgANgoom_Avx6vLpS7p1oZ3mO80-tZKsFuHPjHewAKJa-do4LufBgpbrbsA5sNkmONJiWSsUgXkoQpQfEH8G9ZyjZ1xgssGcHLKtp3mmIO7lfmVPDQWECpVCETddFxIiSaNokaZ3I5I0tc1PcCqyJ14MM0J1clnpcmbZjTIggne1rg5XmjugCNX0QchUVY6Ev2gaoZ6K0edn7y2K-g0QBX-dNfLX1ayOEq7ecrofYmwh_IcO62T5nOded7QoieaeBX6qrQh0XQcH-oLq5dQDXQFd37q3iG1jrBnJ8yidc3EVmZ6tDTkM_H5MwCXBmmdjgzwsHWs5RA7mJwYy5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=UdI6MwKVjvpUCMZA3fRvjf8BDu8uUPonAciwD4uAqUSjU30sfQoaagnVdzTebzynTLw5MRZNZ3D0gNYEAxAOIKSaoLgfY9YvNo_xG3qo0LtR7vCxzJgIcttqwi0ZCH0kQX6ooCi26aD_giD9KKpobLjD-zoIi_ZLbnUd3OVUaTqsWiEfRNvRf0hT4TDwqmmd6JMM60y_MD5p2ESpviug8BhlIF_OAAjGiJKbLEGW-Fil9UGgag5VY8j8J4Wwedi6Mtv26mhtnVpe9xxjpBUp7qvYqDxr-6sVxMUZ6cORrbzNgaym5UPSkVERTUA0jjEjR-shqB2F0TAlGrVmod4fGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=UdI6MwKVjvpUCMZA3fRvjf8BDu8uUPonAciwD4uAqUSjU30sfQoaagnVdzTebzynTLw5MRZNZ3D0gNYEAxAOIKSaoLgfY9YvNo_xG3qo0LtR7vCxzJgIcttqwi0ZCH0kQX6ooCi26aD_giD9KKpobLjD-zoIi_ZLbnUd3OVUaTqsWiEfRNvRf0hT4TDwqmmd6JMM60y_MD5p2ESpviug8BhlIF_OAAjGiJKbLEGW-Fil9UGgag5VY8j8J4Wwedi6Mtv26mhtnVpe9xxjpBUp7qvYqDxr-6sVxMUZ6cORrbzNgaym5UPSkVERTUA0jjEjR-shqB2F0TAlGrVmod4fGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=rmqUPhk8ymmFZv3cofUrkQs0rrievJuY5-VxQpsrc6hnRYnVuRUTPxa6bLsIgjXKg64Dy49g7g7m6lqDdHYm71EUyOrKNHo0j7k097CaqOWFT-r6Q-vr3OWN2sQSfeDrGstPoKpD5x6jDDRTTdWEeD_XrSSJZxOUYZUC0mBTHl5DSmEHGvCpDTQVvDQxmRtEDdtHQn8L6TpLLrcibSNiNJGobXwO7b814v46L5zU2OP8opQRAOSp3f8rDUp9rZ8F9EdLDyriONWpdYwL0_qIi9waleE0a7L9uE9QaP0DufG71ElVYIeBj359AkgVaECmjam1j5zf1qQGatX7OYTrzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=rmqUPhk8ymmFZv3cofUrkQs0rrievJuY5-VxQpsrc6hnRYnVuRUTPxa6bLsIgjXKg64Dy49g7g7m6lqDdHYm71EUyOrKNHo0j7k097CaqOWFT-r6Q-vr3OWN2sQSfeDrGstPoKpD5x6jDDRTTdWEeD_XrSSJZxOUYZUC0mBTHl5DSmEHGvCpDTQVvDQxmRtEDdtHQn8L6TpLLrcibSNiNJGobXwO7b814v46L5zU2OP8opQRAOSp3f8rDUp9rZ8F9EdLDyriONWpdYwL0_qIi9waleE0a7L9uE9QaP0DufG71ElVYIeBj359AkgVaECmjam1j5zf1qQGatX7OYTrzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GswMRoobA8GYonPTH4oHbCoe6yezwLNzbhfFqwXfX87e1xwTNJ9ZppJBVNez2v8kMCmuvOJ4hxfA8QLz7AeUS4HzY9baqZch7YGGHUuRtMlwojURWya-4ahPILku56Rqy-ch-Qza6jIZLE-xc9PvSxlNb6KlMBlynb2EiVXnkUEkj4lsNK7wwG7jeUCzijdfGuX7T0EwkyYa50dsCHstLSN7EyYRL70aUd4v4mIgOYihDxLr8bhpLwK9BhOeCv-OgJQaiGLTgOEbUa7ZgV8TY4VGAQYqVihgYYpxZIth1e-g1tM_a_360iqpjH1asF-S3MWIyQvFcuEI8BQ9btD0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJmTNGFdA9fpcR1jWhaSfqZnSfHboihMhmR6TcmxB01FPHTyIM7yD7Y85Fqx8e5yHYFaOSlGUWnBSrUy_OYA4adXdoBA0RIZGt3gIA1uXnfivcfW0ZEiuj6rO_D78p27JWtsNiAF0js-ELF8Kr8extCa8ITjwZcJ4Sd8W0XAB84UA2EqJFXxSKlYGH8toeoFJKCDGiNaeAVQmnSGMmlN87CcZz4aMKBsvH2rbdxtlN-XhZw3KAMSI7JHoyluBrV0jt5KJil9yZuzMhIitou46ApVk3nEvdTY_IdjZ6v3bSFj57q5kA7Arw06NNq6iUaWKCXWBBHqSFAx_UnSx2fPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=rJNR9u1BC7fd67qQMnxdy4PqTVSWdPyFk9mGzgufTTm5_5hZHN09f7qVQj2CcqoIOw5IaUBIXL3LPVc2Ngqy_kaycdevBuyCJRjaWko-Cp_GFTM1QvW2sBE5oY09ENTP2F32UAHDVLACoq_unJ43vsajs9vd6rDBibJZruFE2bZeCwwiT2IafX8YvnJ-KdaKvv9TKpL6HD_g2mz8VqTIId1CYFpTQ6Bomntwzev-_x8av6ArSq8FF4PnA1PmW9s0uMZ9opAhhqzmguXNGiq5WEviK2WGE_-y5RpWNZxynr0z0xWSTpVEO1zwa997kWViD2tTK02qVhEfr7Obujqoig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=rJNR9u1BC7fd67qQMnxdy4PqTVSWdPyFk9mGzgufTTm5_5hZHN09f7qVQj2CcqoIOw5IaUBIXL3LPVc2Ngqy_kaycdevBuyCJRjaWko-Cp_GFTM1QvW2sBE5oY09ENTP2F32UAHDVLACoq_unJ43vsajs9vd6rDBibJZruFE2bZeCwwiT2IafX8YvnJ-KdaKvv9TKpL6HD_g2mz8VqTIId1CYFpTQ6Bomntwzev-_x8av6ArSq8FF4PnA1PmW9s0uMZ9opAhhqzmguXNGiq5WEviK2WGE_-y5RpWNZxynr0z0xWSTpVEO1zwa997kWViD2tTK02qVhEfr7Obujqoig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=Epx85H4WKTggt0l4kDwMlCUfUShoDFOlUCKRNJyttXoBe1IR65kFxAhx19OrdBqEp9NO72DvJtRWH4U-atehfYIdVfIy3EQxJKQPE_vZOCPvOwpXa_X2Otg0kBW7P32rUlem_py2SqGn2em69TLnjUQi9d2NjYUQ568MKDdJBRhZajAfMq4Lwlcd87WZrNaeJLSxX6R4UgKBpe2H8O1pRLAwlSOLMOdqdnB3fw2HQKC9RC_4j79pN-KCEtb5rJDdCrHnH85bn3a2o9b53xi7X6c8tYxO2dwtHu3PdvvnwQ2ALahU4FgEUw2eAafBuhmbPqoG8-cOceo773YYh20cl64ixnjcrg6nMc1H1soPLkLqYSoyNOdJzKP0EkZizXYYCSpRh3zEGEmxV0XsHGxiKa6jjIfIKnJ_slaOEOKiUx63U2jdoD2osAC6tSuiI3kkK8zOMJFz6lDZHlR-iPaoD8siSl1tbSDw23WH2tcdA-Y5c0BtZFuf-MAsYUy887G77XbjpQeDbrIzAAJgi33h4qzO9frIi1WCPUyaHYzI12U15GuOndl5w-VR1V-9o7-4-2O83blhLwS7ZgCgQLdGK7NqmNChCAR3IB0L4hvvPiB42wzxvAf8pXeFBRFwZL5EL_JbwMaPDZBKzprgtMJpDsYd7B1xutoFa-VvFfMxd9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=Epx85H4WKTggt0l4kDwMlCUfUShoDFOlUCKRNJyttXoBe1IR65kFxAhx19OrdBqEp9NO72DvJtRWH4U-atehfYIdVfIy3EQxJKQPE_vZOCPvOwpXa_X2Otg0kBW7P32rUlem_py2SqGn2em69TLnjUQi9d2NjYUQ568MKDdJBRhZajAfMq4Lwlcd87WZrNaeJLSxX6R4UgKBpe2H8O1pRLAwlSOLMOdqdnB3fw2HQKC9RC_4j79pN-KCEtb5rJDdCrHnH85bn3a2o9b53xi7X6c8tYxO2dwtHu3PdvvnwQ2ALahU4FgEUw2eAafBuhmbPqoG8-cOceo773YYh20cl64ixnjcrg6nMc1H1soPLkLqYSoyNOdJzKP0EkZizXYYCSpRh3zEGEmxV0XsHGxiKa6jjIfIKnJ_slaOEOKiUx63U2jdoD2osAC6tSuiI3kkK8zOMJFz6lDZHlR-iPaoD8siSl1tbSDw23WH2tcdA-Y5c0BtZFuf-MAsYUy887G77XbjpQeDbrIzAAJgi33h4qzO9frIi1WCPUyaHYzI12U15GuOndl5w-VR1V-9o7-4-2O83blhLwS7ZgCgQLdGK7NqmNChCAR3IB0L4hvvPiB42wzxvAf8pXeFBRFwZL5EL_JbwMaPDZBKzprgtMJpDsYd7B1xutoFa-VvFfMxd9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOiSCF02LdkNe7XeUEA2OX8-fI_9HdyCUxMvf-adhWYKxDYDzOv4g0s396P_Dxp9k_CRDGIAbG_K_fIuLMx-ps3JxqU6wvEvpyHfFM2WoVOkYvYZ2qRfoU7WN9jz8EslTQHHxzE57sdn0INz9DwNEaa4EfMv2x7sAoD-UVsIJLeO1i8HDl4uE7XquBKi1JwJv0BrNXMLOnDF1zgtrb6rbtLuQnaMxO-Xf5x-WfBGqG5RCdnZgOGBriPBSpgZ_bAjBicY5g7e8roM71C4ymBaQPlNiDmEC-AVeuHF74x5K_tnyoaJR8ZVNAvqIZb5IXDU5vypKsZSQuyuCCOwYr_i0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOxe1LFexCbOHlVa46EMKe3whmsUYawgjtFT2tnZ0H5u_SsCUIIeyZ9DwdSgvwgLwq8ccuDkTwfpeY2igQyRYbTv2kH-zgQrQ-u6QdZEqUnPT0inNnZjBlgmirQACuZ72H2Xk47gOkABq6Ho-Eq1mmuGoNPIi_YCa-q4ZhCzil7fDmSzFx54TMFqLuAN3npiFgMkmGemJwczSKi7JW4dHAVOyt8eZzCsk4WhxhTDuXvuyy0W7l1XjkkliyKr3hkYXu2WINXuHCFeJO4Ax_7pJtH2RnlG6E4mImtbvXjIKdwAHisI9fgDGldCfToDMxtdDoLwcXuXsmuwSQvrrgVIgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbR00GFTRWAt3QXqCJhSjEOMiBNkyuRXHx8Z2Ay1ZnOxvWhgGyU5aZD-GaZRWbOBs0mPSVgcy0Tmo0L2yCRlGPIlmDbpsp6nMQW78gK0FiXMB1uOl7mJeXZk17jidD7YWS8Ipv7gEBt5JL5O0m6qWFZyxFR_h4-aYwfjU5kqj1PiXP83PMo-jDQL5USA02D3mppjKtaiwK138yO_oF-vphHPkO6G2FHuF4885zUGsKu_LEPm83Qghbz0nYi8KrXLtHkKKk-prhuKbLuxndDH9wft9m4ndydh-JhltHEEDdjvBmue-9WSF8CPrzwsjemRWAcR0feVPVPK6K1Cl-RcaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi-4SOOeMmEtmquHY5lqGqFJlbqG1N1rotZbFboVSDgjt6Z5bf2gNPVqGp8RnU3hedYUElT3bmyRMwJi48ZY3rN4usDjUdYKJVW82se5slxSgOp8JcSsbBye8iTjMZuN2ES1rsuOiWmEFRqi1QmDG301W3sFhloiSe2vTbiBwhQgEzG-Dg0e7QiUfCUTo486xMSbDyJReodhhrjtcAmzHzQR0d4oqW2pC3dDTSMjfeGg-YC9UKkZxXuxdSNL_3iTv1OD6PEDf7vc095YYpF2XG-Gp-JJdMjpKX0a44XAyuDYpgkzFl-bmRduz6FR1P4fJCJR7waQXEF4zZbKjSBCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEYuUktl0rcezwmTOJfF0NLqzkxLfKLLd_hSwkb4PjxZTRB8i82cyjbr2svo5rqybgRHaNwJ37svPvTFZgBwPm3nm0EaZIz0Ct7Yi21Q44-yCcqGKqYp1bPi-3wXKyurxihNPNEwRfpXMnodYo_s2_6-yfUDtZh514MXlirbSx3JoA0pVjG-RiPiC-AxuqVgxNh-oSNsKo-mtEVZ22X-tqXd8vzbI9duW-sKltZ8O22K6_b4_2tdRfxSUpngxXznqbGvdTfUS_NdxKMb9x4dFSIqEhjqOD3ATU2qmwS8Sduy3GxeCCYnVc8EJtVtxVHuKwVD3S0wUbeNDiVT19DN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWzOFoFdeadkCYEQBbuiMg2C-4Y2fAMF8BP7SQhpyZ7N7tubH4A3kZ9TqHEer3Yi-evVfK8-6drIARVWAzsCHAtUJSbJK-d3iSqOPSNDhgFGV4-4k9m01bRfqtOZxmWwlxIvP7pbGgXoNM974OnSw-0rXx9bdmIamEI5n63gWc7Dax7YMMau7XH-kZiXE1CqixXbssB_J8OXuZVf9ZLgq_JvRZUxW5BGjfmogLA3xBouuoU9fUoTgHPHXoDlOY-6f26ZnUa1a_DRzAbBWcsV8mnwl0O8nbGBzaWKSXpyiqiENUfhR2VmzZtmPcu6q4F3w-kPoENWU4Wk6w01d9ch5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ANkwv7BWnrIBf0tv-infjyV76zmTEqi01www669_nk76SIu57Ubm4zvwqXczAO3M6tTofnqMmAwJ-EMqwXMigt_rWVzwLPQIn-T4ErtgF_g1mYqTDq9fzLlIJ2aP07lu-20LujymAOLN4PFLTItBf5A_W1CEn7-V_2--IBHCAyagakZ9F3rT7XJClCzMf7a65qC2LvCg3fI9FGIvBMIgnxlWn5qTA3nb9OOmhf__l5BwcThe8jHoNRUPC8hqtDZerRe7sPbGkXnSFcJ_1_v2x2v-ZYmsW9_lPBlaz_yVbkIWMyy4ZXEgFLP-cQZv0sfCQhJA3TWlqu1ox5VYp5hSqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ANkwv7BWnrIBf0tv-infjyV76zmTEqi01www669_nk76SIu57Ubm4zvwqXczAO3M6tTofnqMmAwJ-EMqwXMigt_rWVzwLPQIn-T4ErtgF_g1mYqTDq9fzLlIJ2aP07lu-20LujymAOLN4PFLTItBf5A_W1CEn7-V_2--IBHCAyagakZ9F3rT7XJClCzMf7a65qC2LvCg3fI9FGIvBMIgnxlWn5qTA3nb9OOmhf__l5BwcThe8jHoNRUPC8hqtDZerRe7sPbGkXnSFcJ_1_v2x2v-ZYmsW9_lPBlaz_yVbkIWMyy4ZXEgFLP-cQZv0sfCQhJA3TWlqu1ox5VYp5hSqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=qO-TmDosqF87CAZUdEOrT_cMkRg_A1JWBinvqE1lONoNTP9BErHdMKVtnSpM5XZyIBoHlPHEaXHncBa7IKYpaO0Ro1FaKcHogvossbB4Xou4s0Sn9lAdOgffs5xopfGfxrHRKEVwpVJaMfMJymHBSsbOrt19Sib5BgZsfVK9CO3XVEJMm1hJla0TZhAD-EwKaN3a5Aasjv2ylYUYOnty240GZKENYiiX4pm48k8agW6yvt1N4DNr9wTStyApblqIleZjyloO2-9lJtpq2FvJj0iAL7qT1BJ3PkfIfNQl1P8n8q4xv0Kwcmbp8VZW9Jo4M3nCcepCFkOvSWShWcfSdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=qO-TmDosqF87CAZUdEOrT_cMkRg_A1JWBinvqE1lONoNTP9BErHdMKVtnSpM5XZyIBoHlPHEaXHncBa7IKYpaO0Ro1FaKcHogvossbB4Xou4s0Sn9lAdOgffs5xopfGfxrHRKEVwpVJaMfMJymHBSsbOrt19Sib5BgZsfVK9CO3XVEJMm1hJla0TZhAD-EwKaN3a5Aasjv2ylYUYOnty240GZKENYiiX4pm48k8agW6yvt1N4DNr9wTStyApblqIleZjyloO2-9lJtpq2FvJj0iAL7qT1BJ3PkfIfNQl1P8n8q4xv0Kwcmbp8VZW9Jo4M3nCcepCFkOvSWShWcfSdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhPEm4GfwBGNvOgC-cWcee2XiRZQFIaM2k_VJDa0PUt0PPunEfG0hFY4vpBZj7_7EhUBatX4PlkWCpam4rs_HKtuhrBzlwR5cfVFgOzZVpnWSVgbJ77-SLJ-3iqjlAV2ayKmxz4DssVEtNEia2pICH_zyuNTkqxAqsiz_lHesyKv22u52mAVp0ZdpyQgS-CI9J1YVDtshL2rjKdhBnqHYg8jlwERe51peSj2FdeASlGi0zyyiLFvVFIQXRMvWXk1uAhKnGZQclikKoMiVGmm5SwyD-_kzVzyIX65TG4mat5CA2zUxCFGz-js7G9Bfx58q29yd43ZU17_ppkMbJ-DeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-_yEyu3UHNpDbgVpKGUoQNbTr3QiYDo7rQFYGgf0v8Ni-Gtr2LdEwH8Es9hs6LGMfySuZceKY3L355KeR3KG6dsdX2ixGk1Q9hUm-sUeuP3ttfdFn00U7mwvJCIT5ZnWuuXzEzxcI3btemFFsDFoNXVHewrMLsnHO3q0sC4qn8Nz4aPGN_vXXhGAI9ZZCnXT2wagPwA_ZHtC2T--jWA2xP2v35x60WCBF0iI3t31uWJO3XGiyrTfExVPtxSwc26qkeboB60sd-CS0qXlf2hNpwMEGNwjMIyJLgC_kQEQRBa6G1BA9dS8_TjKCMlc2tRsR52uDqXUrkq14zd_nMRxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=YNIegXpTOhkGOk6_wFaZ_zJxlQdw4djI7kgQM7YF-UcW21vkvxBI_QEw5EPuedFDZ6ZwhpUETgRNFmQeeyJZGZ2ORocCVYDVMjTx15rHolExjgzETjuJ118ii_ZdolRwdvOLvdI52l36GsDEekch7PKET0yyJp1vcosIoWz1AxIJFrZXlJh-TCYfnxaa8EmDOWBaPegCN3j0iBl6OsMAHyrADfyDDVF1GscsPoj3uZ2Dmj3QnYSI09p15Ag6-mZbIxL2hPTERWvFSt3DtFYyqF-w4qVZVNJWlQLiB1RURlJ8MSysUIyPxa8lVBY25yFytWMmfSwQQd7lqt1xphQTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=YNIegXpTOhkGOk6_wFaZ_zJxlQdw4djI7kgQM7YF-UcW21vkvxBI_QEw5EPuedFDZ6ZwhpUETgRNFmQeeyJZGZ2ORocCVYDVMjTx15rHolExjgzETjuJ118ii_ZdolRwdvOLvdI52l36GsDEekch7PKET0yyJp1vcosIoWz1AxIJFrZXlJh-TCYfnxaa8EmDOWBaPegCN3j0iBl6OsMAHyrADfyDDVF1GscsPoj3uZ2Dmj3QnYSI09p15Ag6-mZbIxL2hPTERWvFSt3DtFYyqF-w4qVZVNJWlQLiB1RURlJ8MSysUIyPxa8lVBY25yFytWMmfSwQQd7lqt1xphQTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujiVCUmRHR50pJ5Pz4_-iCo--g_U-Y7zqjcN0V0pTjkM9Mo3Mum_IrqnDDtv0YwMjwHJX6GrY9pB2DVRjcVttnFmO9dlf7Qm_YxgnKLL_Uk3LGdqc2c2D2fpzdl82-tWJYVV1R3q68VEvRfkFVjBTwIZ8mYjCUaV2cfkbUSn6wIkKDxOL-hr_AcvWa-yLGRbpYxw7I77Q6_nfwc8IyyKq-18YUOjDiLz2xPlsKs5k6dfzmJgiby7mrvGzozTHm672xbwfa6obaa5AziOxFzrOIlOL7YjDsM3K31vXbuEuy8GqakFIbN-7-s0ciEsaocJY-5GDHf4nPaoLe6F_rxvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPu0WBbdhEffOdbCexdbnOYSlHhwury2RBeKNjtMiO_-Ix6byhE5iQz9o9yhB--zgKGrGMB3tnIiNCENhpHweJAl9CpyqXliQNNEAXHr_agtNfm_3nbd3YJmFkXHbBhe4nD38JQTSKshCFIZF5Viyq2mJ1ecNZ7GQPuhS85_A3I6byQ7mjnJd2DLA9rzP8Rb3ZshuzKoa-pMUOGdnO4xpF9eSu4lj9FUPt8DqKylKB34oouhmLMgYryZqsj3ZN-uIP5DociTEjCnhPpTSRtTVPCZTkT4_EPa3cFE5mW2WTD0-LPXd2MRdOrKk3mS9LDIWgVdh9f8JEnCT0KBDljzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=c6ZN0vfxEd3sqq5CDMgIrj0pgwZnoQCm3LG2rXaQ4H03ciSeBHQFVDO7CthTLKc0-bU8y53hdmZ9yTxBlhwtN930JMsknfJYmNjfg_TOXjjDSip5BAn8Z7w_o8fdP_4F6GgdsgXKCseDZ3VOc5j0ZcvA46ap_lMQI69YVs3NbMIKvcS1gzT5kFKfPc-hHyqSJ8AlRZjxgiI7LpU4stRmawjvREo9oH3UKRPZ9gMN00k1W2FiMqRJhiK_0kwZBWf7ZIRoKgrl78NGXm5ts5gWy0T72Du_WWRSH71JPZs1Iuyy12x9ipmagQ2ExIbiBqOXGAQdCOXOhDMVtKogkdbkKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=c6ZN0vfxEd3sqq5CDMgIrj0pgwZnoQCm3LG2rXaQ4H03ciSeBHQFVDO7CthTLKc0-bU8y53hdmZ9yTxBlhwtN930JMsknfJYmNjfg_TOXjjDSip5BAn8Z7w_o8fdP_4F6GgdsgXKCseDZ3VOc5j0ZcvA46ap_lMQI69YVs3NbMIKvcS1gzT5kFKfPc-hHyqSJ8AlRZjxgiI7LpU4stRmawjvREo9oH3UKRPZ9gMN00k1W2FiMqRJhiK_0kwZBWf7ZIRoKgrl78NGXm5ts5gWy0T72Du_WWRSH71JPZs1Iuyy12x9ipmagQ2ExIbiBqOXGAQdCOXOhDMVtKogkdbkKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3lB2h8HXbW-gyZvzMR4nJhvaAI8g5kS1alWnvB0pDrgZrqTsA4wvBM_wbI8Cf_vlbtRmL_zgLfhq5eYJbxpSMOFzJkFJvuvsOcYvMxnTl0yP-DzD2ZETzIB_QDo9OCV_UCkfjTDo3VdJlzaCU417mFmoadZ47qTwLPTBRyItx4HcekWJWsVQLskL6WgGaIJ_1C2s_D2SYwmUHkDPfmKTh4wOxAZzsVO2rJLzBVbUkI0nD8yAl_JAF-VtYapq4q0koOaz5cdmewm6G4gje1azzTxHZN8lGFLLqrUzzYAtb1Q0dk9pTw2eVXjtvDbVO177E4_uhfQ-7vcHp0-a5wjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqpiTTot7-N2bcDHdN5ttwKoDvm4KTzNmDKYjQeF0iW2ZsMOjHkhC5ZzrY72bfeXByC88eLhiUdj_zt_DQhgEige8R-XUGA_FUhZ_GSnO_xKSWdXnWt2_Qwx_GuFSI2wBZpwaW09_YbldtLJahT6GbyPQmU69HrYiVBqeAppzzWYvWvQJILSH9mUn24ZJhFoup38ORIdTWhnLLzIfKiA9RwATk7Y7DT_aTC21K2Lx0738aopqh5JR5Kx0DyVYc-XaHap-04NCaZ6hiEX34RP8KYFnUcHdSgt2CNR0fvPNKRK43_az54nOI40PCrOUko2QxWld1GhJeMDOMN_E5-EZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=uWKPxEQq-bjGr4FjW9q23ajGh-Vp1rDp10NXHNCxgR86Y58acY7M6-N7ji-yxKsh_w7yhZsux0A9rbOU2BbA6HTHDRl6QIrCiCIqELltP0QdHqTZbssq7_gFY8H693oJL_Ums4iaO2kjCZA5xmaYVAhTka2djXQ8pidUuwaeRiD_9WLWJ-gdNfBQ2E0DYvkq8YL4cAbFmLbPqeHGiVcdQ-4-HYCr1f7kO0FyRGLO3KAUV-TnhkUBcnMBy2IDdB1E1f4zDODwT9-iljLAHh-8jEgV82_jXhkOXhS3FiJNNjlR-v-5ASjUYGrOim-TY3PQecC4aHZfrbWkzx6sf0zpnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=uWKPxEQq-bjGr4FjW9q23ajGh-Vp1rDp10NXHNCxgR86Y58acY7M6-N7ji-yxKsh_w7yhZsux0A9rbOU2BbA6HTHDRl6QIrCiCIqELltP0QdHqTZbssq7_gFY8H693oJL_Ums4iaO2kjCZA5xmaYVAhTka2djXQ8pidUuwaeRiD_9WLWJ-gdNfBQ2E0DYvkq8YL4cAbFmLbPqeHGiVcdQ-4-HYCr1f7kO0FyRGLO3KAUV-TnhkUBcnMBy2IDdB1E1f4zDODwT9-iljLAHh-8jEgV82_jXhkOXhS3FiJNNjlR-v-5ASjUYGrOim-TY3PQecC4aHZfrbWkzx6sf0zpnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivmS-FwcCJlK4nqwkDJPQoxMhNsgIAxWfvWI2k5lOXVtXdxKYRkTLumpSH7rCKRC6tCX1hdasGVn0igtjjvjy6RBG4WtuVxD67Hoa-0PLeyYd6-qqE2bSlVzjIM1PQHTI213Z42E78uZB33Edu9V7eIyHT7O7RbTlqaB3KFx_vGp3tFO_BBeN3aLCiS7hN_CbSAq1o-ySH-bE-OoGDRo9LoJM8MlK-dUgqFQtv9t-alFRWOqe8LFd5kUpZJidsvHF8LVv06hGQ4hY8_CcdtCoUnM9xSZa7wqwjw5fhA4TuZNI-bldZuZ2D93utOzSeOyr4dWsJP4uThOwNLNngBfvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzfLErNOGS93aEHwdLuh8L37TZF89CGc9X2vczmvaynGlioOhbM9M7LANcFaBnf3Mu_N2MNJzEsFa2GgsChda2-QQdWlQY6rucFc6xzt4nfdzrhe2jW2ocRg89qhxz8Jwz3Z2ij-cV3tjF10t2QqPLFqEmJ2oOxth784asJNHfPaydCPXVx35r4k7_HV8p_LpVxwUYvOgagfuVuWBrtMvk0GEl5tFGMU7Yphh6qe49j5ZByEb6JwW00TMcVNQVHmoHFsd58T6YV-5xdD0iVdbGjI-Em_4v4gmVbh6q3qID-u89KHrQQCw61J76RZ9xRyy5IVomCm5y_uIkHr2H_I5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnb6Gxx3JVum60zVFvTjqiq70crjRrpEsq3Zv6NRn3FB9fi-I7f7Yw3jO_aup56umclhWVzPXXLqRTkoi0TIM0EawQ5131dMMDXfSVNrUwuh7Eq9awIrVamygVPhERnMxcD2l0xgS2loSYmmVTrP7iDPVSX5uCvz1yHn13i5LKRLhbEYZcfuScgZwBzhtQBe_taeL72ItGICfHk754KeDPctyGSfthKFnEQatAJUx6Hp4IPNo52lxSg05pxSkiRT5oH9chLhq0jS0kKRjmhfgqXajnvt1kRsfNpqEMyGixxVwuHYCvTUc5vjr72vzjlx1Pc765hSWqO33rLckVoHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcTZxAP5Xh4wyHQjos2URJARMyfYvyKkIOROyxrSQX1OB5zQwGBsV_wguccngDpXeSKMtigf28a5olXwWRv_eX_dIjK_jvSM-xpDf63sWDfCLojiIUyUoXoc44SdYegq44_wQsT26tkEG_Cu0smLdlYKoakg23i3hqZRWNbmCl55Z6wabDtNeUYbPkZYKUDxlUu57Cto7gaaK6_SlVjnvmEiG44V-_8pphfgQez7XPUxeYnSMn-D1qyoZW9A77XfKg5zhhWbd9iTkwR2ZYaN4p2YIYBkuk17YgNfFZA-SX4U8Irr8QVZmFBwZQbuzKBvgmutI2AkutLzTwKdaHrqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FL7PzUJ3TcJkTLq8yj-MWzHp5qQRdCXE8mkYbppWGBM2EVKBa0JwiM1Z8ijctk4I1s0-elkdOTGoh7QRSyzckqY3u-dTuEvMqwSIGFA1N0Ci3eKKjttCe-eLYrxRtvM_-jz6qiBSligXWvZse3tEdcQnuKdE3bG1oHnH1I1iP90lPnO6zOsJ6Q9kAb-aUiOZDW85hOSFnM3YEe70VR5pT5RIClsajzi3ZenrQdUjPiiTqOuUaxcizGWyeyTNWgQ0FefgSZq6Y2mV-3WXsrOD_4qEj1RiGurCofq_x47-9ZzDBhr38jLQCKg_jtzMqbxKMLWf1iV5Lnj54GasCsVJyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTdT7a2m6-vtt7IJi0JV7JA7d0cA97owgofunyAlUx3b9F47Dip4bw4c9tjdCk6j1fZYTIP-CKVMV_sICSUkChAKPG3cu1ZsnnFaIPrEDHAqHrYZtj9x7EqgCGvTCAid0s2fPq55nF1OzTul_wSe-NhVtlIaqvQAjRjYuPdTK4uUjjIDdNBBwoPYUoCJbFH1YPkokKVcJT_MzOwOmVGXgVLBp74AZ8dCsJlcvdKLUCpesbhCklnOpdHQn3CGTNnvxkHYVHdBc_QsyxH44yJYsLQ3O2HNiMlm2r4-GOONAaQbEtHvKJn6EiXX1QN4VYOpFyvYPk9xYhIAMVuD7wAftA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=g3nlmhfWwdtdXy0xpi-kpWQMKKp2S4t3Nthruiad7bnZs_jNKK56rMjaqPWWRbxyRDHB2BA7Sbt9Bg9FyzbHfoGCWcGhBaZQMz-i7yUMEMr0hHpMMUaIcGl2zHha1oZbf_3PbzpNroIiME0lJ0qSl8f-hGFJTwKl8BHsJ9PYhDaw_fg6rPY91cv0iHusRc-YnHU5wDfb-WECOTYkpcHVclyzu1LAMUZxtO-anfcIs0NCL8foDUB5wO9jHz1dn8Nx84ov_-wnSahKpcgfq-cITovq2CY-mZF-sLeWKPv3mJT2Z_2sBAi2hrQqSPsqNwdFj6ET9rXUbjqOX34x2jDqJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=g3nlmhfWwdtdXy0xpi-kpWQMKKp2S4t3Nthruiad7bnZs_jNKK56rMjaqPWWRbxyRDHB2BA7Sbt9Bg9FyzbHfoGCWcGhBaZQMz-i7yUMEMr0hHpMMUaIcGl2zHha1oZbf_3PbzpNroIiME0lJ0qSl8f-hGFJTwKl8BHsJ9PYhDaw_fg6rPY91cv0iHusRc-YnHU5wDfb-WECOTYkpcHVclyzu1LAMUZxtO-anfcIs0NCL8foDUB5wO9jHz1dn8Nx84ov_-wnSahKpcgfq-cITovq2CY-mZF-sLeWKPv3mJT2Z_2sBAi2hrQqSPsqNwdFj6ET9rXUbjqOX34x2jDqJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I58jMt6TaFNJgbyEWL78M2wo9bVbyFZFlNJY9NUuFWSR01msx3QPEUnmtSanAGACAzYDIT2fv88SDhc8x0iFY2FZvhX0krZ0UtljUWjwfeygDRJ8IhSHH3qgr2wq3Vvgd5JBgzQ6eWPFzjESnt7QUvho75b-Twyb4G6bVDGdp__OHwDe3BDK1AVQe5qG5eHU1vUbXs40sX_SYQCEn2buAF1t-YpGWTHpzyBktaFGVepP9Wb8EeQkoUth-oyxnr7pzr6KszY6ZJcCaIQWhIpI55CkFhTQNYffXV1Vaw0qCHdw5yU1omKK5hEhHTqd14HiIXlgyKrKkYv3Br4M-GHvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bo1h7SMdpHcSy26dbuTTcFnuM3Fnh6u9ts8xux1YQLJ387gZBpnQ9daB3adXfx46l2uLcRBTz3QSKhfYAEcVFQthLuH_WthoMw2CDqqjDehdEficGpLnh_mkMV_MldGM269YOyGoD3meHzCuzPOHhXFzftI3hm1saaLAEF91pjOROA5j7aCcjv_KkAwu3e6zstZpepjx_G448pXWDgvZ27SwFRIITZ1qfYTmZGjLmNC8KbbduydxqMCVnFXT058jXUfgtVWgEUNB2uhIBA9Q_NqgBMedh1VqW53H5ti_EG1CmXbFuvEO00V0tUu14qdzplnyI99SF0LdX3GmvN7PUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=lEO2BdUceWT-MQaBn6Hkf1jPjTZ0fgGEgtW-dT-YI0DgxEYOf8IaG6hVuSVtxggdaLr5P7zFG0SJ4ug1jTLpemXG31wYnMSdRj2jqW0kRBV2IW8iDycfXr919j-RcD7dYjp9WJNuJlfHe3pxLQykEnVBhzM_4RwPBZM2R0nkIDvjzSCJE_w31ehxDtFnfgejghekbHMBr9GR25IwiHVrYGPIUUmBQ43KO7PPAKnOfPn3Ltc1m3e-kdoOWKM2I14aWttaS0oQNbUtJXYs32vwyJ_gD25ShwzH_RERIVXmXPF1LoSA2bFr2Y63ojZEICbVvBMjw9lblSkuAsDYgC1cbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=lEO2BdUceWT-MQaBn6Hkf1jPjTZ0fgGEgtW-dT-YI0DgxEYOf8IaG6hVuSVtxggdaLr5P7zFG0SJ4ug1jTLpemXG31wYnMSdRj2jqW0kRBV2IW8iDycfXr919j-RcD7dYjp9WJNuJlfHe3pxLQykEnVBhzM_4RwPBZM2R0nkIDvjzSCJE_w31ehxDtFnfgejghekbHMBr9GR25IwiHVrYGPIUUmBQ43KO7PPAKnOfPn3Ltc1m3e-kdoOWKM2I14aWttaS0oQNbUtJXYs32vwyJ_gD25ShwzH_RERIVXmXPF1LoSA2bFr2Y63ojZEICbVvBMjw9lblSkuAsDYgC1cbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntz0VHEdSmnatTIwhqcw5UL0YUnH7bcRNr4cYsH-jwr3yhZb6M7YOlNY7ECNyZaoGCK6Cuov5crYeFSFHN5Dei3Slb9KibH-D0m7e4LbZaiO79MNMLfYqH-_bE2DvoDXseNBCcE_KI0O6W2NBfRZGQdb92NZ_a6UgrBDA8P3M7gC8Nez1c9W4XUc-ak3XV_KFiKGzUEuRF5xD-SRah541mgLa-6mw_nl8Ml73MDIaLD9tldOaiREI06bO6DMsWfJqhRQYap56JSTeTmGg1NPN9w0Yu98kZHKgnsQBi4uvdHWPnBFsxHlkX7Z6MCxKYkssJB_d-escHhj0FyOaOL2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeFw0pDQzdmxXKXSRNEONG1m5bb-ApBojSRYKQb35bp1q6MPiey-xXoXEgYauqnpEhy9yaHCU7Gom9b7bEgRiq8vqKd7au6iKoxLnxVjV4qotXxBXIB2T-YMKlpu0zLh4uQJbX3f8x4IZFFQwZdYmAKxAWKtOi4opZGAnHG4WE05x0rmuTAoQPculJrSMrTkDkHMQ9gBzNLbVtc5ZnTUVTtBFC3Vqfe_twk2IeT9Ph6qiqDDxSXuFdqZptS5xrloAB0z-cNYmZcUQbw_pV4WJW80qO_hlcZrtcUJ-qyRpt9kVpUWEoDfrp6WarBLMgYp6rojD8niH6790iByiHR4JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqvo0R20cnVN935g86M-TILnjJvaJPZmW11KaO6u4UguSByIGQEtgcyD30jFke0Nmccx4KX3OP8XcG55zhNzTcIrlrVSZ09Lc3ChE9yiFLqJ1BPxE41L2dYFBpQ_ZkWXuBoiN4RvDga_CJFqyXpXkVUODwQ0R131blL8SrddYemwrnuL09X0ApXGMev6f1WJxUwS2iDQW0whiQXh_ie-0XtxaIOhUAaJZRM1Ric1D_yQ4h9vhsvg0IsfLTfvg_esQK6YYWUVm4h2pHWbVJwjQWcNriZlk39USnK6xjhUJnrwHgRrVJB-HD_o-pa4myVY1kkd6P3_yK4EoAt2sXo2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R62FYYtc5CQSTKj7oW0wM2hDs1tCWd1ibQyM7xtwH0cbo2LlNI0wuT9bIHIEtEJfHyUSDx1fspWtIlqk9b_00F4B-_FyYocadO8zkVXrHtolyO6FXiQ7O-fCVeqMnqxor-zbl9nyNM1dk8b4qwrkH4czQ7YJwGZu0LvhLCZWuylrAQztfG48fONR8B22z9Cnhhf4I8YDl49cr_2YFsoXcedAgvexK7G0e7lVg-i74vd2OEkTWxGh09iuIuoMzW6w-oefCUhsB4m19JrVPu_H3zRSA4bTzYcQNNdCyrMvU4PHO7uZma9UVJpyhqMHdyUhz-MZbdvHP2PYD6-jXj__ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDs-aKNCkUOzC-SxO-MesQnDrdSoeR_3QOJ-Dx0IEAdv9Q52ak09bI6ee3H5sDRLny4P0FAeDfWD5dOu_GtvEtbCBrvgRafLAo8EGNyZxrNGMxfIfJGYiOnmXvN0HQD4vb80tn3FW0D6UyNlneRXuBse7nJpj1PyCiJVKv5gwfnk3arOoyS5XAuQZJkcamb82HUjUdDt1x6-AJondLV4rRyORJI765R05B0aFxPrIoDGoM34M1znMYiqk6HJqxlOtACEIKf3MZQzKKPC2ITfceJilhlA6zCDeH6X-3PoEA0aTaznft2aDIFPtCmFfXbi9A5CPvx9XZVdpwvjZxs1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=o4JqVda_WGkRyk4oQEFg3-fWeFv_lIifOfWQ6PX_NfZoDWsocwiBn_0cbNyvv2GbEzLM3nyx6GA-lYNKaBLms5WQLND09DoxKSrAYi-OXU0tQQxS1tqnVrS_-RChDQcl6ZNlr9FG2ToqnALZASB7fc20nLGqoTItidqcLAsnRLOLQWdTM-eTk4fRrfHPHdHGi8nH1lRd2FrqO5fwBbKISW9MRlGThkWBKzhcuowrAqtqISjWWrgkNMP-faOSYV81b2uqDVLw9dyb9OHowflpK1uPgyK5QrAzc9nPzYxxHJF0ccSrMi0LQVjUlndbPilG9RFO2kmzK4MBQSdJy23K9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=o4JqVda_WGkRyk4oQEFg3-fWeFv_lIifOfWQ6PX_NfZoDWsocwiBn_0cbNyvv2GbEzLM3nyx6GA-lYNKaBLms5WQLND09DoxKSrAYi-OXU0tQQxS1tqnVrS_-RChDQcl6ZNlr9FG2ToqnALZASB7fc20nLGqoTItidqcLAsnRLOLQWdTM-eTk4fRrfHPHdHGi8nH1lRd2FrqO5fwBbKISW9MRlGThkWBKzhcuowrAqtqISjWWrgkNMP-faOSYV81b2uqDVLw9dyb9OHowflpK1uPgyK5QrAzc9nPzYxxHJF0ccSrMi0LQVjUlndbPilG9RFO2kmzK4MBQSdJy23K9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0rpDkcvfQp2AGstm_tx-KppiFYNyk14TK_PyeDUKebI2HLWU63i4nT5CMRBw8nVfO6kEPBOjU8fcnpXRGYbelDvZ-Ur2KaZ-CHgQbONJpVO36b92ibgadxwKb_flJnXpVRgbNy9uXnO2skjn34pjozMC-CrFseLUCRNrZcMHKceEtjJNSI7K3LE7Pkt56Hm95eXG4IoUYW6pcOYPek16fXJVBYTOpty0kWToBGoURfneaE_afDUF6uifftIAbeZiud97aBFRgeSMrgoCLu_L5iwps3-OU2NDDjhI8Dtg7Po3a4WSOL8JYWD3-yFwPoO7QYZ2bl-BTYpC5utWg-jjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVXbv7VbZmb8zR2mgxBbDOWnX1Vj8jCsiSiDAmMu9fNDjf5CnocD0YLXk12byxrzuLFd5kOACdGqt8GBRFR4asoMayolnTqKHYyl26R8cXFhs2DiG5AWKAU9SJFks1erWWY_QnXLdb24UqhU5hgaoYgJr_oXBpKPWRjnVv6viPrVz79U8PRW-2d9MNLFdFHaD6jDmJoTAlVszxdBDlT3OAxg-Iew6LDjLrkLKOGjST_ZzykTd9vYnWT6U8oUvyARFM4fSnYCFcKbze4KdDtIj-UWkBuD-CrLJ0IWvZOdNFH82qcfo3u5UkdNVVrfv4Gz7yTCaP8J9oSBSJJiX8sDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=QrUQihmxdaWXzNozZ8oo45sev2CSMKbR7V_tMtx-5vFtEN7GYWJv0QVwyuk47UgI9OKKmLWOLzFgaTwYKy08Fq8aEMkYOKprUMvykWNUP14xtNzcyjr-ooAyJpfT9XXOxhpLipfJULFAqyfk0QBHdlFdwXnkS-JMiCouOJjUEBf1TGDXIr7f0vIt0-QssTVahyE-BLf2F18zICvizMSR-Ie7NVSSJ2fRceHExEyUcHWIz8xNwPQkvfVp1jKEUzSRiFNiI44HnnguB8oRqzrQK9y9VjoBKX3cm6SDgoYbFhJOLdbuGwuGCCw84_HBGW-ZhEwVUwPJ_yUxv8vXWYztu0rvvToR2w-Z_jhIHm0Dg-emVaqXerrwaCUUcgdNDsLASPubh9fnOeNaz_emaO3USUd7qk_tSP-5pMITo4ZYBcsNSudOcfMMJ0cYEEQ7vLxJ_L3vU2yMALIxxxEQUnlYeM3StYF2u-QS2u0pG026PssnYi7pwcMFjIIyjp4u0Y6nfhfJKn8sNE2FqWF0rD0pQbShZz0mbxQFWGvFxB5ApgBfFg0WC3BRWMKuMI77Upr3B8iz8r0fLTbRhYrFW7lfY8__R3-4dVwckoiglL9lNX4vQbpt1gpbhcvVV0Q11G3VtSqpTS8hXQsLtSYORLLB4DgDPEso7NyIoemT8qQmW9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=QrUQihmxdaWXzNozZ8oo45sev2CSMKbR7V_tMtx-5vFtEN7GYWJv0QVwyuk47UgI9OKKmLWOLzFgaTwYKy08Fq8aEMkYOKprUMvykWNUP14xtNzcyjr-ooAyJpfT9XXOxhpLipfJULFAqyfk0QBHdlFdwXnkS-JMiCouOJjUEBf1TGDXIr7f0vIt0-QssTVahyE-BLf2F18zICvizMSR-Ie7NVSSJ2fRceHExEyUcHWIz8xNwPQkvfVp1jKEUzSRiFNiI44HnnguB8oRqzrQK9y9VjoBKX3cm6SDgoYbFhJOLdbuGwuGCCw84_HBGW-ZhEwVUwPJ_yUxv8vXWYztu0rvvToR2w-Z_jhIHm0Dg-emVaqXerrwaCUUcgdNDsLASPubh9fnOeNaz_emaO3USUd7qk_tSP-5pMITo4ZYBcsNSudOcfMMJ0cYEEQ7vLxJ_L3vU2yMALIxxxEQUnlYeM3StYF2u-QS2u0pG026PssnYi7pwcMFjIIyjp4u0Y6nfhfJKn8sNE2FqWF0rD0pQbShZz0mbxQFWGvFxB5ApgBfFg0WC3BRWMKuMI77Upr3B8iz8r0fLTbRhYrFW7lfY8__R3-4dVwckoiglL9lNX4vQbpt1gpbhcvVV0Q11G3VtSqpTS8hXQsLtSYORLLB4DgDPEso7NyIoemT8qQmW9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSBRl8xS_D62Kz_uVgJJ0s5_fwGNbgGzwD6DfOplGNSfEJE4ahuTKx3DBJXZ6mppwj4es45SNbLANvBT_LgLzqxfvGw306w52xI2AqcRF3VZ1aWaAA60LjnTIzCglNCMcmwjr1NkZ3TFmWw04U_ivMhxsaAAwxTat8k_E908_hCPE9r7h4rhPkyVeBKGEpMaqJWrM8YWlwQ_ST9kAYG1c5ey5GGWxMqAuAdp_xqNs-sFDFCENYUl3ZNlCprqsEXVQxe-IFAsqUfwwG9R5tXTU23o9_BxVirFroH7tFxGBVjuSzd6grTbAgPA29WRuiwg0ujUsD4tfy_NYEvv4nDtMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3NE6XgWLJnJl1oQq9oizsMbh16IZfna_SRBaDC6HO8EMYu60wFa4mdcwUvqqTeb6kiwM2Fc60UuwyZFZgye7vroZU31DdkF9X6ZZ2xQuOWVRU-q7ekmgJWacoz62GaUPeZnLBBGaH-e837FowGEYOLVF9Dg-3UJv1e54EA5ARO_2ijWN_7PMUtjv79GmHXo-0fS86jawr4qQH78f2JZGKd6IInyzUYMZpG_6rc78sTAVZu4BaUb9BC64tDsyLc5MInRFCx6fcmG4c0s9CcMUzVBAdCvOSCa91YkiYNowLs323Jg4QeOCtg5GAcyZTOj-6u8b9WR1R6VPuAm9-gVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=tPsCkyig4-FnmFMxXpYIdpdAuA6h48LBT1iqE8vtpycXr6cGDi0i5U4MwdGUuuDkGWHcgjtqkTLYeCwmavPZVG2ltb1ycGm_PuXxLnMfT96peDYzGN4rR1gqgGtqCL6ee2o92c2qDOEaaKyiTk7r0oI_10LmkukCmIPBNADMllw7CRGrXVwLWHkF61jXoMPadODV2fQnaeXXpu1G6NRAvEUXPSKuDCKZWGmhQchC0wRzm4Nlhi11z6_Gmzp4-X_jsbCPgHWsnXCmDFHjjM_58ZdL2WSNTqeQFf9BPML-_uIdld9Z3kRoav0LjHM01qZ-ye7IOT2nooVlpQZGioOqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=tPsCkyig4-FnmFMxXpYIdpdAuA6h48LBT1iqE8vtpycXr6cGDi0i5U4MwdGUuuDkGWHcgjtqkTLYeCwmavPZVG2ltb1ycGm_PuXxLnMfT96peDYzGN4rR1gqgGtqCL6ee2o92c2qDOEaaKyiTk7r0oI_10LmkukCmIPBNADMllw7CRGrXVwLWHkF61jXoMPadODV2fQnaeXXpu1G6NRAvEUXPSKuDCKZWGmhQchC0wRzm4Nlhi11z6_Gmzp4-X_jsbCPgHWsnXCmDFHjjM_58ZdL2WSNTqeQFf9BPML-_uIdld9Z3kRoav0LjHM01qZ-ye7IOT2nooVlpQZGioOqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=Uzx7rmjRliaXf8BvX5qPl1v3KHnlEJkwLfWSYM1rt18VPHqfb17WOQTLqA5ooAWCH9obuuekfElAIc3-I_FY1qr-A-8dvoHjkgGFyZ1ay05hCQNsi6pmphr1niBT-13TzbMODOkIcQHNcCgm0lxdRe0Znwz1rZ1i0dbWQLNokhX3sqOp_3gcqIi7R6x3RT-AW1Eecg_EkvEwpahNvZKZ8d4D3cef51qruE2zakGKSPibAtzE3tNNRjcZMB8njEkWALlpG1Ggom3Q4AYq8GymUSc8M6UAjSAnIAhD48ZiafXOH_yJOOiY3xU52uudNSfGOVvH0RBuW3LiVAhCq9X09A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=Uzx7rmjRliaXf8BvX5qPl1v3KHnlEJkwLfWSYM1rt18VPHqfb17WOQTLqA5ooAWCH9obuuekfElAIc3-I_FY1qr-A-8dvoHjkgGFyZ1ay05hCQNsi6pmphr1niBT-13TzbMODOkIcQHNcCgm0lxdRe0Znwz1rZ1i0dbWQLNokhX3sqOp_3gcqIi7R6x3RT-AW1Eecg_EkvEwpahNvZKZ8d4D3cef51qruE2zakGKSPibAtzE3tNNRjcZMB8njEkWALlpG1Ggom3Q4AYq8GymUSc8M6UAjSAnIAhD48ZiafXOH_yJOOiY3xU52uudNSfGOVvH0RBuW3LiVAhCq9X09A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmS_g9Wdw41LR_rD-vsSyYt6dAcqyjVBVGss7UBt5eUzZLBaVj4N7dSbfiR1_aYGDqOwQjWcEDaDlgOF1D71l3FyJ58HfmBRWBVlpQn2WRp7aKc37pWaZsUI1lbabXK6L5y7-oHybWZa0UxmbBgENS4QyyytpNFVGfrZ7C-L4NwvzJ8nK8OlB7UwsNBtNb_J8pScSvwbcQA3ZBQuGLq1TtpobTIJ_j30gjhwzPmpabCWdllqJcxHYkVuXU9mnfUM9hFv-5FQBFv7zwm61Q_nGqTtdNzchPStLv41bGSQunVb1OPjSunaIhNBOHpiov9xOd6gzW48Ien-IMgxkBs4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx6Ti0dMSqx3y7Z-WXMamLYQT-_JCQWragyZsKKAdKUe_xZf0DCi5IeWDGuVC8N_ZyDxKVioevbDFAEbFw-WMNEG18WKXFcVw1eY7L8yQJR00oR00X35BtUHFkWQMbB_j7LYCsY2MObYH6Tz0SDGslCXkFZytzKg8vqQc1QgRlUo6sTAVAxHQN_trtlBgq4ULbVfSp_OaR3oSVDDGNO6f2X2DP8f2-ky4uFq_g4WAeDMJqcU4h2rEbolh9W4fbdlEJ_9CA7TcRipFW2FjxbrDvFJcFVeBrfVhRlwf4btWtNCVu7nZx1ILBlzDpcqSlofQ0vrJ4Oq9us9ElAWQRLQ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq7I5Iu1f-Z74Isj3-xEbSXh-azxzR8B9T8SYXcy5DYxLXYMraA6n4xgjyI1P3odeIgvp3mfX8uJDEiDCht2xqQIpds0CEMCg2aDJ8pbXl5_FhIRUhi--AcW6RvN2cA86m_EcplrHMQZVhlj-Y-EjIANRAZDZBOmiWSb6w9kvdzEYwHd6t6UvO-eqbvH9uT6LU1ZNL8lR4lEDl3Lm3SWMeewb_TuJDQDtOai09PbGx_ZUCyW_j79catyErgDFa6bIUoMXyrfOVeVkgjyE1lEvw5qqTVr-sT4ikWwfs2CoalpRW0DfyBCDOHucyXE0vxcaF-yIMDdL5TWH1CIuQNWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=IWalAUDWOQcxLor9zI0y5HeonRzVJ_3Dzds3d68gt-k_mGU_z3_NqwvSOvr-kvl8uV5-O1tPr8ZrL3R_qujOaXqSiFENMkh_qdVfSrS9uOV4ObRttlvbbxhD0eGfa7pag8gd13_YdHOx7U2sxwimbZyAeejt2kb4DjmOipd4LAINqfLj3A-scknT3v5KPXwb8JyiRFSaGDQjpsP8olTJCxba97tTBE2tB0DtwKjKgB2nYmabZ3xrTXT-a9_8geYFVc6_ZSaGHmotpNIiu8wiY8CsXex8Fexa_oSP8D0qZYtqpA8ZGlDT1dl-iirmHn4EcKh05p_P4ULEAI0hcNsDdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=IWalAUDWOQcxLor9zI0y5HeonRzVJ_3Dzds3d68gt-k_mGU_z3_NqwvSOvr-kvl8uV5-O1tPr8ZrL3R_qujOaXqSiFENMkh_qdVfSrS9uOV4ObRttlvbbxhD0eGfa7pag8gd13_YdHOx7U2sxwimbZyAeejt2kb4DjmOipd4LAINqfLj3A-scknT3v5KPXwb8JyiRFSaGDQjpsP8olTJCxba97tTBE2tB0DtwKjKgB2nYmabZ3xrTXT-a9_8geYFVc6_ZSaGHmotpNIiu8wiY8CsXex8Fexa_oSP8D0qZYtqpA8ZGlDT1dl-iirmHn4EcKh05p_P4ULEAI0hcNsDdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=s9qBnPYFTpGG_j0wlSsk7K00OpuMLANvKbZOUm2ursV-WRvyPDADVmqI9Nw5kwMZW5SZX2w8UxDi3h3qCyj7NX2dTPhiFL7ofedbIODxEa2-Vjfgr92c2v-brRh9weVCW5yBeDZPUgzgfx5suUY3V5cjoG2j5pHJeK3GUo5m6pYYqmy683uCXx_8W8Tm6vd83ghYX0mhtnRD76sRRny00vQom6NgzlYzbty-Ad3dMzrOZvzYXUuPhxwrLD_sLTYJo7QOpPvTKYCcadO7DENquDh3Yt3CGN_HzKVHMNxsNhOckQ_GNQtdJbkljZP8C0Pf2n52HdNvDvKJSF9EKpPYlXjSkTCL3qa6dM2zCL_XiIjjlsjavzBJ1FW7sPgy0iCdhC_IGCEsavKY3VzYQEXJvyW6ZeDzrXHpeIBhfEvctioT8RvonXAZ2mIDmSItuo7gDHsyVAomyklSIE-zdITFuCIEpgHljbQRrv6XNzL6zgT4fCauRAM_lMlzLCgmC3_xiEc02xG9KZ8jEzja0k9wVRIorDeFUlkKt4fBjQusUSy-Q2icssen8XFb3LyfsgCAgTcf12GS6Uyl9B0p1cN7bz-yxtuq-bB0YJRKlSW_sucivKEPhyG0IbOuvRxYDDEKEBuowJhopVEutP7vL7CheoZHsHagznB8KkNF_erm3J8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=s9qBnPYFTpGG_j0wlSsk7K00OpuMLANvKbZOUm2ursV-WRvyPDADVmqI9Nw5kwMZW5SZX2w8UxDi3h3qCyj7NX2dTPhiFL7ofedbIODxEa2-Vjfgr92c2v-brRh9weVCW5yBeDZPUgzgfx5suUY3V5cjoG2j5pHJeK3GUo5m6pYYqmy683uCXx_8W8Tm6vd83ghYX0mhtnRD76sRRny00vQom6NgzlYzbty-Ad3dMzrOZvzYXUuPhxwrLD_sLTYJo7QOpPvTKYCcadO7DENquDh3Yt3CGN_HzKVHMNxsNhOckQ_GNQtdJbkljZP8C0Pf2n52HdNvDvKJSF9EKpPYlXjSkTCL3qa6dM2zCL_XiIjjlsjavzBJ1FW7sPgy0iCdhC_IGCEsavKY3VzYQEXJvyW6ZeDzrXHpeIBhfEvctioT8RvonXAZ2mIDmSItuo7gDHsyVAomyklSIE-zdITFuCIEpgHljbQRrv6XNzL6zgT4fCauRAM_lMlzLCgmC3_xiEc02xG9KZ8jEzja0k9wVRIorDeFUlkKt4fBjQusUSy-Q2icssen8XFb3LyfsgCAgTcf12GS6Uyl9B0p1cN7bz-yxtuq-bB0YJRKlSW_sucivKEPhyG0IbOuvRxYDDEKEBuowJhopVEutP7vL7CheoZHsHagznB8KkNF_erm3J8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2fRzpQs5YrOFo1ggNlCWyY31I_daPCQt-298zxO8ohXSdbFwj5-piIoNn3HHEfaO1hXE5_Iwe1xTe4tq_gZgiGpuCPfgEiDhTsTUsqtdbEGymKx23eCHNE6Y_0PLA-aF14YK6B1fFayF7qKj0LArzwLMGswhe-rOtjAMqdRXYJWDE5UjkzxgqS__AoB0reEomnwMXnr0ywCs6nsx6vlN_kq5RbLG4DMBrnUl6XnPoTuARjbPzIWyuB1whMGnR9YX99EP_h2KZpYzgGmIz5Svjo08ozPiTEU02tg7A2DZEx7ompD1CGPrhXo-Ae3XYXtcbk6CNQZ4QPQTgeSxMsbhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKTjNB3vnL1DPm_0EcD4cdiiqMOC5zLbN1Qb1E9WBUceg3EEYLxSrChEXVnhrRnlOpTPc_X0MsTbPeRZOy1GI4vry8iw8H4ze4QAhPdI35HM9FqbinZ7tE7crvMfq1bI2H4oPZkmtajailzaV0_bzAqIbLYo2kt9CnqXjx6TWaWuOcV3YG1dYeULF17fmSpQ-26bQMTj4d0jpKx_eEnLdb9_DzHLOoEFHEfg1Z-es6nKZvBnO-M11ebBO54Wtap5Ar2iEi6b1LmRB-Md10qyU3pGycBfc8pdrlrvjqQOuV4fQnayFjURCpuyLIo-JHhPXBaCZblcYSSnDzF6vMRvxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26728">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nog42GEoTLx8eZZkEejkO7h8002n_aCYAagtvzkjGTxuSp_ofEtmgztszFla2i3H-oaKr27ajeh6MFrkuAOtde4vRVDA8LaoYJc6lU7GKIp1PcmIzHQCoDfkEIzRvXyMUCvTs-CA93sWHCC7BIPq2RoxgxKhDgRJ9BPPCMZxH0lE1Wno7-glMSic_OV6utnCW39pP79hhmKy6gHGIp3ZpHfuPg-GSuPipxlMMxqJIzZHBqchl55Ao-ZEuGllSjYjJKdAr9FSPBPr-653xqaBojPdtPBIxhJeTidVfCWr3tnfSwwmVyxKMBeJUahWz1oQb4FmInqGQvoBeKFryS4b3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
برتری شاگردان آلونسو بادرخشش‌ژوائو پدرو و بردآسان سفیدپوشان مادرید مقابل لگانس با ترکیب دوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26728" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rgc2YRfIekxHKUoyULUplurrZmcDMiqnmHbBWd2YKuuyN5zuEy1y_eSRlZeH0Wl_b8-SznI5GgrRXLO5yvxP7aSe1_-iFcTc_b1Z16UCZQAwf39FPtx2kO6WsGyT-0uBr6hcIMz1l3SAQUK8_Z51xjW7H1Ge33lNHVWhLEVWpXYhqjkb7hn2PKtrARRaHnjDKNondhvE80SYpgmz4BN3MCXe3mWYEa2Q-IjsyqS8NeQzgm-shgLRg7hiK3TH-nJVLarF5Cya-6gY_QdCckktgH9GLNhIZqdnNlSfQDM9g1v7FyBPRggVH5yjuMAV5u31iOh03bO_I9yRi2lkH5pnOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CY-SaGYKvjXNlRLN-VQ-GPNcgHp7PrHM_uuntUlom562mNA6_aAW7_XiUs4FL7QVixcKVS18tZt-Tk8vQv0Js125S7F9gZbETzyNtQRDvLElhIHmX7kHLoMtdhXnfwrKJVanc7vgEwSBfFHwXGp3cZH_lgk2sw4F1GF1tvNcJNyzLdQiwZQA7_X_XbLjRmQQHNQzTVv53rYXLXGtENDxr8LLqBLnjxKXZo97vqYZ-4RdDyW9qlwsArqmUlLsB1F7FFT0Z5tEkImtPN_Qcyie2Z5JMHjn3R4Tr-sYtlEO2fCfLCreRs-uXahVwgkKCU5hRcOQZZHkVLdmvz-4yfNlgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J34KOsfD8vDlkk85Nm3r6KkIRY4gG1GhnNn5PwyFQvLOA8wcKUKQMJG7Tg63ibt8Un5vWT2PL8CbB-dkfE_Pa3KIGEYx3bziYzqFBY5Y6jKYyic7JjVmxfha8YZutrodoTLZqv6TDYKInEYhLY3p8Kt-JKXyP0p666266XDZnuYZuiR8CL9AawD2tHnj8OmrAGuhN5HUxnRskk8P0EHDbnUf8ZpLsvmk7kxYMrRSLw25kJgM3QqTP06AjTxI9FVHeHFrMXbeldsiHhkVzjjnMn9nO0AhtNQ424s_Hfzp1OyW-ZP9ou9pouX-DfTU199mrYlcsXWnOVVWDLlq7OacZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJAQOogcqrGbLr1be9B0Gcc0ydpcntUaaY2iTfGyxOzKk1g1SOyQahuaHIOPTX-nbZiq-G2wnrBQx932YpIs6cd3rzlKJ5OvemJwnk-0X3_o0VFbofaq3jqvQjioNTVsMeTHwvx0VAPdFLaLf2YC58kDMSNm8n5XkAN-TZC86BOvHEqcAF8dkI6fOiuNZeyFPN4khRVW5Tfq8OQG5TCFQecADN1SKeT1Qv9ibksGZUqlJKeZqG5ZA4olU6-ELHVy9w_-xGNaRvEyaQWZFoiIHTwe3gvRk94MiVjQIfDouLsBv4Tl0VX97Fcw6fs0fg_bkvuOTHq6CZjT0hO6Ao_I3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26723">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=gOXfqcxLkTfMTWiyYR9dzaR77rUsWU0_7FYarPyM9gIhFYUqRIZjP8ArIUlF5I4Q8o_IZwrbOEazXmX33IFXf3rzRrK3ByYYiI8UmJT8Yeb4fzUVZzLbiXcbd9W1zTZYwkBtSWqxQF0tHudAkirJUBqcMHbUVwie3UvUpQEaVBCRbalcCNyLB46JAPaDh84SjSqvxgxazAV6n0_QKnwvlhHcSm62ZJXl6RbVtfUqpVuz6DdpnO90hlrPNDC_lPAMfqymtFp7otFF3ecv5mokSqH8gzDzdQBg67anCarGAqwIrFDXjUvK3E0-6F0r6CLeZZCpX4pqXoWf6qfO8YdKqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=gOXfqcxLkTfMTWiyYR9dzaR77rUsWU0_7FYarPyM9gIhFYUqRIZjP8ArIUlF5I4Q8o_IZwrbOEazXmX33IFXf3rzRrK3ByYYiI8UmJT8Yeb4fzUVZzLbiXcbd9W1zTZYwkBtSWqxQF0tHudAkirJUBqcMHbUVwie3UvUpQEaVBCRbalcCNyLB46JAPaDh84SjSqvxgxazAV6n0_QKnwvlhHcSm62ZJXl6RbVtfUqpVuz6DdpnO90hlrPNDC_lPAMfqymtFp7otFF3ecv5mokSqH8gzDzdQBg67anCarGAqwIrFDXjUvK3E0-6F0r6CLeZZCpX4pqXoWf6qfO8YdKqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
یادی‌ کنیم‌ از شبی که جود بلینگهام بابت پاس تماشایی تونی کروس به وینیسیوس جونیور او رو تشویق کرد. بهداز خداحافظی تونی‌کروس نه تیم ملی آلمان روز خوش دید نه باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26722">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNIN6KslioKdKCWii7SA0_3OYbIWMBVlC1bwfqnll9rpE81co4zlkvCuoGGOANj2CVFHTQYJIG_n-7U6DJ1k39qMaMKqkjML9AkdNdDbK7muL2OdWpKbXt1jkwS8C7UpmfEQMsRNpf1sGmYOGBLHOO8eaw4kXK992caH7ZRh3ezP74a-clg4125UXf4FZlPLzmGPtO0wl3B4Ca9Wkeaq_2c5TrcAUZ_6Qa9ZZ5Lh2Yq-Rg59_z1yr_3o2LgiUaISnnVNhInzAO_qlTxzovOG_V59YfYlb0XImmsVf8onnxXcJoG8VM2JPpHaSct5Jd-RDarMFjArSoSOqz_tJrka6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tm6326K5dss6cGBXP4BwQG8yynZ9aHbVq6YORPrUcjSpt6Yyw3aZiUshyRz4ZdORYogNBxNDXlv5bBHECHA0cGMDq5PgALhxAW6tYu6hKMNOopxfLo8ZXiHEXq5G5FVBBAq_sd_1Gu6yQaV7uobZXFoSXEQGZtQmd3zueFm7GtHqFMeaOjzJwBTrDBIFFywu9_Kaw1092yA6jfxoLytcsOWkxcc47unQc9-bOmLGSxRTC5eaNIpzX7z-XHkJ1v6Xpumq1PlKye57wtzKqjy6YrsY4Wodxx6IMnfP6FgfKo1hg4RMpk9K5PDp1Mk4udYdv-RqiUBu8XvvY3Pndoq2Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26720">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btOaddl3vp07Mbu_V9fFNEqEcWtlQ9NTEpwbLJ3XQ3wMTMRPVR0WdrO2CVbEJIcvDi8aoqAgNg7km7640s_cGp47TZ890j-OUptjQ6__AgOeTel3tpIHSdLJ80Y_7HWhknvrFC9LQxksW6agbkclXoynC4qZ26KTmuzD0iPj71tcASAC__alX9blNxS_Ydijfpofebt-j1hCXm1n8x1ZY1pv-P1ynIKkvY4RG-HmpUN1-Lp4hpfJDn8d1xl21gPX5-D3lM6UToGsEcjvCT6tfZ8bEO2CEvVFgewJwYD4dqjyQ0T0vFdx_LM9Z4D1fhCqxmNnS-oE0TM2mXczkohdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/26720" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26719">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owEi_NwPoOp3s0tjDEQQmpJJ_snJLU08XjcNid4P1ejnZuQaH1yXZCj83b4dlMWZBZAza2qr9HXWPyly3nTKo23BSqwEHLpQlyEbBFuZExTOK-XW6yq48YK_X2oRG4hMge2xDdObwc_IChKNFYOrT8A5f40iKa6TcqkYMh0YejcrSp5FkdyyUCGDSldUR6nVUgJe6pzt2e2VGDqHY8bErCAQsw6tOj_4VXF7kUUC4JUVUEZIvF2zMaV078hTiTbWdwaU8LDqG9W6YZsm_Sxq3BopbIY2MLATymhs3R3LB_X9RxdzOu3BtUIJZzlXxMaC4bLuOLMQFxCnxu5d-PNPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکی‌نیکول:
یامال‌ التماس‌‌میکرد باهام باشه‌هفته ای ۲۰ هزار دلار بهم‌میدادکه باهام باشه‌. یه بار بهو ۲۵ هزار تا دادگفت‌نیکو ویلیامز منتظره برو باهاش وان نایت بزن که من‌قبول نکردم.میخوام‌از یامال شکایت کنم و به زودی اطلاعات بیشتری ازش افشا میکنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26719" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26718">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=WILln_wiebo3DplNE95Lpy1HdrmKFyPExqvcXWSiYgV3ELUDr5EFKBd6W6bALNwBqswF_wq6-Tuwmlh8AvC7egtXIA33HYJocWJNVau4rLSJBQhNOef3m0hVSWvnVScFrHySzIzJW8bLHGeNC1FouXr7X7IKcHzJh33rbLbOfzx4grqJnV3Ak2BuuOwL1BKsaICv-f7i_5dYA0agZhgBaF0mLyaRNvuhNaYxgX_gdUxalgwWOQy2kWGucpOfZXfq5DejyjU7iT-rqEfKwNk_7xnV2FoZyyAlP2ev1Cr6Lp748eedIrBJg2HRtYOZd-_r9n7D5n9D8tPJ8L1lbn7bxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=WILln_wiebo3DplNE95Lpy1HdrmKFyPExqvcXWSiYgV3ELUDr5EFKBd6W6bALNwBqswF_wq6-Tuwmlh8AvC7egtXIA33HYJocWJNVau4rLSJBQhNOef3m0hVSWvnVScFrHySzIzJW8bLHGeNC1FouXr7X7IKcHzJh33rbLbOfzx4grqJnV3Ak2BuuOwL1BKsaICv-f7i_5dYA0agZhgBaF0mLyaRNvuhNaYxgX_gdUxalgwWOQy2kWGucpOfZXfq5DejyjU7iT-rqEfKwNk_7xnV2FoZyyAlP2ev1Cr6Lp748eedIrBJg2HRtYOZd-_r9n7D5n9D8tPJ8L1lbn7bxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26718" target="_blank">📅 22:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26717">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbE1pN8YnwPN2fVtQoDrbkqE0ubXJUT3Hnx7spDtID9YLONyqfK9fAxw0besYTZmAtff8jGCviYZECn-5X5WZlPTEQa_P1GcCxR5igBWzq_dFAPDfqBsc_rUEEc3vCO-PnCZIseVGYJW-YKqoxQMTy7HBkQoM2wCCqxT0KBiJJuRS4EvWJs93fAGrYiuwUSnKjv3Ku0LHIMFH0hm2VXgbKzBkyalHwwpPLghp7ZZJDMyjvmmD6teFwM-SZL5wGlHbsc3Eq8OOcnvj7XB1yPILleHHr2xJDL5YQUFf_HURD6xWNBTqCFrZYo-bcozv3xhaJaco1pjwxxi_2QeEq-gCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/26717" target="_blank">📅 21:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26716">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyFHw5MkDx4cVwpZDsx3xhTL-fM_Jio5EOAPWfotrxriX9t19hA10bMUdtE-NxgjpCHTqGKYZ1LSHUZxolBjMjPlIcm4JACwN_wcDBeW-qiq5CFET02inR3GVBbsjot74FazM_R0nskigKXS8jfIzdDjgblt-jfKUvHSkCS6R3Bp1xz8IKrGvX9Fk-9agB--G47PO6pUmy04FG_5jC5Y_uujzDTmrYNMKvlCnaz_a58JzKjKmt-GPnd56Vv9gYJFLHcFWjY2OznT99vD6jhQAJjLlGVKUjM9CKPLAxv6GLZuOW8YU7s6lVPjxt8hti0ONxYoNI2yvoFUXrm1Lgeiew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه نساجی مازندران با انتشار این ویدیو از کسری طاهری از خرید جدید رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/persiana_Soccer/26716" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26715">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pigkk3JtlqgsT0kTPV3znMEFARDXCqnielbpep35vliidD3-LnAqPgcgcJZOaU0EWQ6ktR-G8rb0BhljhR30MZ4VyQRnHEJl5uzEpxImVTDcz4r16kaXT7QAOeoYECqox0AjUzlnY7KBza04APRdKKs8WNdrqfKGycjHz_m4JyivG8QhugGqB-ya2HGMJ0sX2mNLdhjObydVIpIKzhbA9nAGkbupEoNekqJtzAqml3RcgYsdv0PRYkTRM_QhwhR0F6lsD1_M6jyDtS4po02Hl8TJEMS7axVusNJpvlW8kAQSJ7zHkJUDNiWF0hSrJDoj7kwUwi385YjUvFiw8EOi7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟡
👤
#تکمیلی؛ امید عالیشاه کاپیتان سابق و با تجربه پرسپولیس ازطریق‌مدیر برنامه‌های به مدیریت سپاهان اعلام کرده 72 ساعت فرصت بدهند تا پاسخ نهایی‌خودرا به آفرطلایی‌پوشان بدهد. عالیشاه‌ امروز هم با مدیریت فولاد خوزستان جلسه داره درصورتی که‌پیشنهادمالی بهتری‌نسبت…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26715" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26714">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=BqBFe_8v6qal7Zi9_sMaH6ORMf4_NCG7nW-W7LXNMnE4PhhdI7Nc3Ptn3isGzYPcRLIp7YIUtsOzL6i6Qd_coCxNf0-6sze_Sl5MEp-k1OyLb7feC8P81HKHDQUZoFeilqRmjXUeCtWVb99CXSIOzk2RKQjZJax728s3wGfDB7Pq6xSJLIR4RtNOprKhqmLJbL1goF8pa0gUiqI_5Lg9EffsS0604Jrl4HQZQqRQlkTb_o1LO3nn9SNaf-Wu489vW9cY2TpgAieK70iNSu7L7SSTWi0rYWrpsGPdMYXlYmORObqf5_J2ugIC8xDvkkwePzZCdgEnbB3AeSk3_yqkyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=BqBFe_8v6qal7Zi9_sMaH6ORMf4_NCG7nW-W7LXNMnE4PhhdI7Nc3Ptn3isGzYPcRLIp7YIUtsOzL6i6Qd_coCxNf0-6sze_Sl5MEp-k1OyLb7feC8P81HKHDQUZoFeilqRmjXUeCtWVb99CXSIOzk2RKQjZJax728s3wGfDB7Pq6xSJLIR4RtNOprKhqmLJbL1goF8pa0gUiqI_5Lg9EffsS0604Jrl4HQZQqRQlkTb_o1LO3nn9SNaf-Wu489vW9cY2TpgAieK70iNSu7L7SSTWi0rYWrpsGPdMYXlYmORObqf5_J2ugIC8xDvkkwePzZCdgEnbB3AeSk3_yqkyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26714" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26713">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=HGyvM4BMACCTe8ONYkuF9wkyJxQFuwKZECUUaTOjszeJnhBHABP42lYXJhnQYF9o5zNTe42p-GfEa_0I3xH_gEPsQ-Y1oumb_Vy9Si7LnDRnwceYgTNAZdA4W0WIxH4ccmZk0xBi2DJPmRQ4f_UitsTMFlLmJ1k4koCyxeL00S40naQ_LNHpSKoklquLXxN9TqbMiy-NQpUZ5J_c7NRmaV0GhrWCEJ-gpbzJNoVzMcAOHaEbLaZ9SLdY0eKIHTxekmtcB8RQt7IfBOJ8EShJ5pBtcaDnytztIPcSDOc7gLQvT_Lp-31yeFmhwuFv46J6_IBjpdgPwScGY6G-XPWdhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=HGyvM4BMACCTe8ONYkuF9wkyJxQFuwKZECUUaTOjszeJnhBHABP42lYXJhnQYF9o5zNTe42p-GfEa_0I3xH_gEPsQ-Y1oumb_Vy9Si7LnDRnwceYgTNAZdA4W0WIxH4ccmZk0xBi2DJPmRQ4f_UitsTMFlLmJ1k4koCyxeL00S40naQ_LNHpSKoklquLXxN9TqbMiy-NQpUZ5J_c7NRmaV0GhrWCEJ-gpbzJNoVzMcAOHaEbLaZ9SLdY0eKIHTxekmtcB8RQt7IfBOJ8EShJ5pBtcaDnytztIPcSDOc7gLQvT_Lp-31yeFmhwuFv46J6_IBjpdgPwScGY6G-XPWdhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پست‌جالب‌مجتبی و مصطفی بلاحبشی بازیگران نقش‌رحمان‌ورحیم‌پایتخت درصفحه اینساگرام‌شون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26713" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26712">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcQIu_pDUSfYH_b3DRkxvhkSRsisHYHSYOE9RRlapBrSpgMbMJj8QyQ7bJWPaBy5jk0bYzc4vVN9mKlDwWSQTEy6bMCzR2K4XdU3EHw1i0ZjbTuwgzAfcp4l4Hd3O1wUg-RbrhbyZMptF8woy_8UFf75kACWls_LijbVqZYIW47t9UAy5Xq_BN0LmltTk5_b6b0h-KkciOYPdvcxOj0JVCZMXes3mUTyFfhyaA1uKsRMC3NWL_YfGpUu8hFOh-H_2pnNaOjUSOvNMDJWib_O_2p_ZxYVmXwGZHAwpY5T67Xvqce-Au-ZBSfzvXNoycBzyL5k0kwIDTpq6WqBDDnBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26712" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26711">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUl8i1KzhI0XSHn83GtzsWc25ShOSXBZ9wIy67B5qporN9wtZXe1bNSGSTG98whnVOEpTZKGaPIw59U7F22B5btWSFmozM66d3O3mJHC-KnDdKger0TwlF0hXnndSYBiNrmHrcw2d5u8JtxgJMe2EDkYUn37c6wZqLJQ4KhKgKWmiaUVNBNn14JWxgN9ZqajCV0PrrbndwpzBdX9Jhs8K8l3hCzpfH-XmABUStdzstGxj0OOch99Zg-ElGEncIv2gLA0OWPPdbzINNGd0jyoOM4JP5J_tptNu6AkU2M6y9Ud6FbnncwyDEl4WcEs9554_8Z8BIjL6W6jvF9YJ5I4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26711" target="_blank">📅 20:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26710">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=bS6hVXGGwLwlupYt1HVjNLf_yHmWoAUkCk2oFqIRsMPXVQfsWTMimh2Hx6L4ErY70Ju8Cf11pxXdhHTcMAj9wj_bngT8XGrjtFEAR-AA7gJ4Wa6OJpLjNZjA0PbfWsEUKHqmrFTGjaJbnGU7pmeKxgG7RhHk1mIWrCtlBlryC4g0RoTFrmGlfpk_TsrjmCaAeIgI9yez1qgcf7IvAGOurQxkiWCnhjaNf0Y3UGv0NHbikUR0rXVyuTXaCDryr0ZzXFy3g38i3krlLjofS_Fy8tvqEPd0gtQh3dHmNbCme9-ekzIJLTwlhI4pNEPgNTSHNxrBK2J4TZYQHAkGjDgePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=bS6hVXGGwLwlupYt1HVjNLf_yHmWoAUkCk2oFqIRsMPXVQfsWTMimh2Hx6L4ErY70Ju8Cf11pxXdhHTcMAj9wj_bngT8XGrjtFEAR-AA7gJ4Wa6OJpLjNZjA0PbfWsEUKHqmrFTGjaJbnGU7pmeKxgG7RhHk1mIWrCtlBlryC4g0RoTFrmGlfpk_TsrjmCaAeIgI9yez1qgcf7IvAGOurQxkiWCnhjaNf0Y3UGv0NHbikUR0rXVyuTXaCDryr0ZzXFy3g38i3krlLjofS_Fy8tvqEPd0gtQh3dHmNbCme9-ekzIJLTwlhI4pNEPgNTSHNxrBK2J4TZYQHAkGjDgePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26709">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP5afdD00VFGdw_vIuoG4bSqdJd1z4WpTJrFUXcDtZ5iTJ2VY9dsng0X_wDzrNBSdWNxEjfXFNehYHq9GW5J5Zgcsj_ZwHRaaLhcG81ivsO6oKT8vIYzjdontEbw7H36vkdKOET59kCeJLJcfw25UTLCbeeE-L0nG95rCvZIfEweX2c6rQRTQY-YxK4wZhnE82ekFWPT-cJUBo9_1rQiFIHa5AodCvlLvhYZZqF6KReN1x2ms60YnixIFwsIH7XLOZn6wW16za_uZ0MXxqVJUj5v3xDhZaDvX9Om1scBXUty4K_9tzw9lGxw_vBrYAZyZ5d0rSfUGSj6M4lvTZR3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26709" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26708">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3yAUxIVbbWgss0lJen2tYiXrJmheIKfE2Qy-BJWvCUzdrUszeTcH3uqSRJWB18D-hIVyAz9mELnvAsp1KAMHdxGj9HLcNjr86wINLjY1lmyx9timMq1yTuBTiQwV7Eeixm_9dcPczjZnymBUE_eXegD4Zw6vCKxGdMw3JvoXdyMOCFDiEKc6t3Td-2qO7J-HvaZ32d7vJqhvvx359FCca4GD4yU5Ord-whTZTA2EQ6kSSbiLqRK0EF1Atmp_IHGyhRh-uUAYvbwCJZwg62hYKKZjRDGbeN14D4FrDyvWPOUSl-KU8sLk9lEaQLusWu2PTibYVTabGaemy7h582Z8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام سازمان لیگ؛ لیگ برتر رسما از روز سه شنبه 23 مردادماه آغاز خواهدشد و روز 2 مرداد نیز قرعه کشی این رقابت‌ها انجام خواهد شد. البته همه اینا منوط به آروم بودن وضعیت کشوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26708" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGusUPd-y4DjhBC6lp7qIpdvTWvvUy_0TEwpCLFQdb7y_f0ls1T0-PAMhT9g-OGq6HioFA7iPrdqFvg57XRs8qgypPSz8Wp_M1hXtBmex39Mjmeq32SUtWGvlugm1xEnMLjLmcqxpUQLx4MPYezV3SCw1u-4kIs03hddBYOCFjUjHmTtlTfgVPdIay3g8jPrYhyCtud0xDTJJHPqAWwuu2mYf4qj-fmoPl8GQdeQZunEyFLG0jX_hFu9DU2byRXvtQewWfvc5T8KfYOGv7fHioUDKkL2soAV5XT__-j5SMvuf_3zPVyBH4HSaPAzIQu2l3RP59lOxMrrwsaTlN9epw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26706">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn2AiY-eQcfYKWko73bfZfyo7VjocH8zkRRwBriEzvY_h3P4SLneViIYADOEzOcCTyY5r3jAkAFqSYslUDifDt79sNuSZg9Ak6d90sOxHlk5DXPQUibNAnzfPeBOjN8-1Wh3YCwKbZ1Ha-y5g7FZyn33gtFe7fOZSeIssUJ9Wau1cvPwTZn16Hio04VQT9ArgQy94o6HiYkoqKkdMTLhyYHl4O2iPx3nrfl-sStdQ-CpRvEQtDABgTTmIn3c_iaCjnRv0K00zQ_Umd1SZk6IJoCGOsBDgeIrBgxTxH6DXlifQ0Cq67s8LJ6pXv3FEzfZaqIq8vqU1qfy29jLHOtjWdxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn2AiY-eQcfYKWko73bfZfyo7VjocH8zkRRwBriEzvY_h3P4SLneViIYADOEzOcCTyY5r3jAkAFqSYslUDifDt79sNuSZg9Ak6d90sOxHlk5DXPQUibNAnzfPeBOjN8-1Wh3YCwKbZ1Ha-y5g7FZyn33gtFe7fOZSeIssUJ9Wau1cvPwTZn16Hio04VQT9ArgQy94o6HiYkoqKkdMTLhyYHl4O2iPx3nrfl-sStdQ-CpRvEQtDABgTTmIn3c_iaCjnRv0K00zQ_Umd1SZk6IJoCGOsBDgeIrBgxTxH6DXlifQ0Cq67s8LJ6pXv3FEzfZaqIq8vqU1qfy29jLHOtjWdxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنتونی‌ جاشوآ بوکسور سرشناس‌ بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه چند شب پیش خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی وارد سالن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQJk83w0bP2PaS54ZPlwuJ3Jtl63Z8suhvr8OPqazumf3eglISNoSsThMXIdEM1OQFlVKtY4IcBEQoPT0aPZKVgguFG39CT2cfHZrm6BX0yZfWK6bqPIicrP7lz-tN56kEZN7w0YkQA76LR-mMBQPmumAjmmya_ZL9R3gx1SwoFcHacJzBdoAi098AxOxtReFoAyYL_qlKqmOtto3opOtdJobHbZP-pCrfLlB_yTNU5845Wnd6RDS0gZi_5jcbFLt8ozk-BYs71I4pahqKT330xVdzWB6ZPuB9lr5biAkXRLNJrcy4oobWT96-JFuhMQfO25Mb5Ju0crTzVXdt7jRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26704">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/persiana_Soccer/26704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
این هم فایل برنامه کامل فصل جدید لیگ برتر؛ ذخیره کنید و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26703">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEXfNxETY4mslsfayboWcpMQN97xrnhkvcWuftxLFj4Jt-_estCf5silix0VJipY-kVAfQnplqLfqprAtwgtz3xuyWepjHntTuDQLiBPkHyWuhNaJ5cQtzSrVZx_hRE5SrmGuPZU9yTwaLOwFjxxT1K4BHYDSTQE5WiyHJ-u0GdknwLSHS8S3kXVkOdU4t3S5a1CB_P3iivtjFWNMROLYPFRCYnRdWMq46pKSWIenLvx3Ez-meGv676V80WMHjGXtGfB5QagfSI0rNhcUyTeGAvMTUbAjYjOjsEAF4Tht2U4k4-_CtHNWIrgObcJtUYny6-t_kqR3cWOlOC5dHg2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دوئل‌های جذاب 4 تیم مدعی لیگ‌ برتر
🗓
هفته دوم:
سپاهان اصفهان
🆚
تراکتور تبریز
🗓
هفته‌سوم:
استقلال تهران
🆚
سپاهان اصفهان
🗓
هفته‌سوم:
تراکتور تبریز
🆚
پرسپولیس تهران
🗓
هفته پنجم:
استقلال
🆚
پرسپولیس؛ شهرآورد
🗓
هفته هشتم:
تراکتور تبریز
🆚
استقلال تهران
🗓
هفته‌پانزدهم:
پرسپولیس
🆚
سپاهان اصفهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26703" target="_blank">📅 17:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26698">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-2v0BPuJ-W5MWyO6V5m781rsjmr7KZzho1QhU61ednsA8RenxvoDhgnileoJjicsEaXllEyi7e6NxqHSfy5zryLiYo-j3bpE70R6CcapGn_ARTmWC9E5TmOS6Y7gcHCWpxn8vyBv2tWFaLXImZFglVxkWL6TOVcdaL5VDU7yHVZulBcUe3syznYdpTtDbWAtdWqAivEipHjCJo3vJEg7NSTYhEQsCc15WBCf7T8d-lJBWoiZja7_yiesyFLJJgciKtKF7jjd5yvYGixo8W1vkid2CgR2bg2SKmKXStWhXwFcnmg9eowqx6oP4GvoXBi9W8ej5ROOffx7hLrtZrSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWJ1fObN2RtNi2bIfqISm0qzuTMrijh_Aw6813dI3-tPRnSUMowbEShzv7artPiHgE32nzQbUK59caxzAhso9ZfJZovfWkro208BYdyNJGW3E9kM6wi8virAYC8JPgiEgYNE1iuVu5fpvlOmtdxqkJTzOv10RZA3Ox3iA5TwuNiIMbmmM3DCk_KO22cf_y7y9gUtM8j4ZkE63L7sM1AZMjBUwda4fCF3whG0Gng69N3QT6Zmx_naVTLVIG3cb3xVj7f6ztRfnMf2zsuKJkFbNZH6y9m_xn6Ja4sLW1xJMokInGpNb_N2mXF-PRUf0Z3Tie9VUOjeFdXqPATcXhr2CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26698" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26697">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6AHclmO8KJfoE2HUoEeWxds9XgBUOdp4f-a4mM-FRseumA6A6_ykzBFBrr87YXFUY1FzFe7H24TKrAQEA8rZtD0TbGSr9lkJCZdzGsWnZIyfRClGXl_eP6IAJ4bq4YpDfCwdu3lqjdblS66ii9O212AEXXPg9vJrbd0hJy6C90mvJ1ISHZIa-R8aCO7MjGIHD9Zqybqn9dKM8xFnDqTfXaawv-jEh82aD3uLKnK52CXT36sUaUaMOc3vkCfSDpL4k-u2eYicVhheYAJGhs3W5W00Ru-WRAlv6_9vXwZlMyVCfrJQ7zI3nivwoD3DM3-L5bDGaXu6insdNIpf4Hn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26697" target="_blank">📅 17:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26696">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH1naQMYayNhVOuFkqJf_wFF7vGCBuKWD9t3fVXy0NVeCRpY0kjPp_fAAkU9ANqC5zh6S-0201N1HnfF3FS7p61LN0j70Rq9MSqsZi7n0gBv8VIh1K3vlZ7ZnRd9VE3i_SQSHB7KzpHJyzrK1ukp2mLMyJZnh7qqTjAcpygv2s0NH75qNvrSnl7pkWRSmuSetklisjFC8FYy-BAgTvU7rRyPUKJIhC-xWSNL-PlJ9oj6drDBwWH6YUzKOVUmfI29XFk3Pa_a1C60UkGVYIqyI0NQkjfCqIT7HuzaJSWo-KYSJDqAPOkvOQTppqFglaBtuxzqUQTMfts_WQo8zTvtHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26696" target="_blank">📅 17:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26695">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLOQiXZQu0zdTI0dXwsfr1lTzzzSRneOMJQ_xQaITEJBXqS6PRu7N_M0uwqYNq_i1qnqeWcKPVPvMod4ePngSFy_RiBZa9rs5kCvXe6KTEtcmrRn-FGq8gAzp0_4U2-tC52L17Ee6liz6twetziOW9W6GGk0Sf6g2FbB_pHFfqDWN4GnNs-I0eT_v1Qw5avWTeDf45NdJeDdD52AC8QCfgeJzBeOSUJsgz-99PXtzUK_4n1-QLjkPqjsluiHkhvtT1UnmFDTK6a_NcV8SQ4TG7F1G54FvUbu8Xu6gTdnSYsulgBmwk8m2DxEQGH4ajRlhVlYEfsmBxX_Ak_Mjobv-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26695" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26694">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31211ab420.mp4?token=QFcW0O1W5o21CtkuehT3EVLnJ1NmycSvqpKwmFLd3HBwceECXn6bUI5l80B27XOpnDWKadECQHmx94ftTX0GVImiAObkLVtuXBFYmm9lgwVrDAL7NlyfmbqvdiWvVBE1GcRL3P2Tk9EUy0dfz-xvU6O9rCC7_JRaHk_WA6IONcODLSsdkgcbrGR_C00VKu1ng37Kr-BcRGFaqe7rRmccT4jzlEXtVqwTNl5k5hpx-7Q6qg113szCm_AxSah7R6pEdHGqn9qA4ExDi8JpOtVMmeSGnfTVvs03wVfobsOh6WXMOnf-7qiFEHXF9oUVrZXe_uFaCHP_XB-l87DATQjDHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31211ab420.mp4?token=QFcW0O1W5o21CtkuehT3EVLnJ1NmycSvqpKwmFLd3HBwceECXn6bUI5l80B27XOpnDWKadECQHmx94ftTX0GVImiAObkLVtuXBFYmm9lgwVrDAL7NlyfmbqvdiWvVBE1GcRL3P2Tk9EUy0dfz-xvU6O9rCC7_JRaHk_WA6IONcODLSsdkgcbrGR_C00VKu1ng37Kr-BcRGFaqe7rRmccT4jzlEXtVqwTNl5k5hpx-7Q6qg113szCm_AxSah7R6pEdHGqn9qA4ExDi8JpOtVMmeSGnfTVvs03wVfobsOh6WXMOnf-7qiFEHXF9oUVrZXe_uFaCHP_XB-l87DATQjDHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26694" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26693">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0LgZxmo1vH4ji6Q0tM1XYsNwoDpWzq8pK5nZ1dyuMRYNAjPv3o25_96FvIsBhhziWCBePFp1LkaEvoF5IDbzgkmcn_hAzh9tmMHe1k62mqdYdJRglm0c9oQRYz9gGejcM6OTH6W-WMMARzzijLCNZ-mEBdHmRqXMGjhU7hNA1KvO_IRNo33SVMNe7_wt3VNfS7bJGt43RkKaZ_7g3QFXxHsAWe-1LCJ4CIH-fgX_mm-YPoiBBnl0hXko1dNNREhhGCguYYmJiqZXDOxU0BqWzjfs_DV2ZhjaVRvKzD2cJZrJuvN54s836afdElGS1eKixzwkSZjiDNLgCw__XDafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26693" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26691">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q20QaDYl4jU2mjhURMyecJes4fZ-8XjPH1talLXhoilOCvtDzg7fyMu5PnPZqWxte7KnX54eqSS9Q1y89htqhflqL_XvgpKAOUO-IBheDHfWG3o54475u35U5Lefpzf7XHkAbGGtwbgr6kWSy5oa4BUS0CDLGkKFfoFOZ9PrBWsUMtSFc6eYTiSmjfkzScMdZV2XuafvjThDFJV3OIvqD1HtASkLMGc7O5qfU-gHwuZiwdZf5Mixgjv3mA2lD-Llq-v8kG8_0BgSFaBSpd6GahJ8LHpuq4cYSZWODtFFxHQHWxIAxXaciopD-Xvdwcdpw2Le0PhG_fa1UORNj_U0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ محمد مهدی‌ محبی دقایقی قبل بالاخره قرار داد خود را به مدت سه فصل با‌ پرسپولیس امضا کرد. ممکن است باشگاه امشب یا فردا پوستر محبی رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26691" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26690">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ybnoh2oXGatagR10ruNUP9sgBMA1i8GnxGPYwbhgHu2VgHpxXlj63eG1c3Di4oso3VVraKDL6W0YEecl9CMurNCQ1JM_DApcFqL86sUbeGsnTJH50z0on-r7JrD2xM6mTD89mHKvUNFPTVCMVY3Fn-uJn1nfKQzkO0VW74T1qUTvWOL46YsSVgmduXksT9itgB5PXqmfCloo_ppDPgoHNIui4Ra3YovYGiVJiR9FvZnhl9jKEKcTlvLVH89hVyqJuji-njBuX0yK4ERgp5cnM7pY2WyA9PzlWswuk1kwWhxd0AyCcQJXKrnJQAZRqcmenigvagdwWDzzScZ_Bg3gaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌عمو کسری‌طاهری ستاره تیم نساجی: مهدی تارتار به بانک‌شهر اعلام‌کرده با وجود علیپور، سرگیف و شهر آبادی نیازی به جذب طاهری ندارم. تارتار سر انتقال 150 میلیارد تومانی شهر آبادی به باشگاه پرسپولیس 35 میلیارد تومان به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26690" target="_blank">📅 16:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26689">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=btMU5C2PAXmuISCfxII3KUZza9NOnl9t0mjlJbbc_ktW0l3nNzdtoimWv4mxhRM5I71CfG_fJWj-s6_hQVDtN1V1D64LDkrhKeAq-b-KTMP2cACeJV5y7VnoR9NRxnD2lIVjdB4flRLltz271h30STYxd1Noe3qRNiEHFlQsESKIHFyOlzeFp7fd0yHF8B_YrEoR171fu6Z6e2TEX9Yz2_f2UEFH7iYEIxNC6QSdI6sKul8Qqo-dnVt2kk83InBjuM5x1729f8AtDO4GgvZnPxsgJJUfF6SdAekS4f3_uZMdmPYh2xE1VIn0HNGqYyv3pX9OL59KGunPXD31ejDLXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=btMU5C2PAXmuISCfxII3KUZza9NOnl9t0mjlJbbc_ktW0l3nNzdtoimWv4mxhRM5I71CfG_fJWj-s6_hQVDtN1V1D64LDkrhKeAq-b-KTMP2cACeJV5y7VnoR9NRxnD2lIVjdB4flRLltz271h30STYxd1Noe3qRNiEHFlQsESKIHFyOlzeFp7fd0yHF8B_YrEoR171fu6Z6e2TEX9Yz2_f2UEFH7iYEIxNC6QSdI6sKul8Qqo-dnVt2kk83InBjuM5x1729f8AtDO4GgvZnPxsgJJUfF6SdAekS4f3_uZMdmPYh2xE1VIn0HNGqYyv3pX9OL59KGunPXD31ejDLXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هر اثری هنری دیدنی یک کپی بی ارزش داره؛ در نقاط سخت زندگی فردی به دادت خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26689" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26688">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1DOpq8N5-OoZ6PONTBc7QI05U07QCtE6I2j4BiJiVoY9JmxkLY3uPv0W46-xBeIYkWtmRd61QSnwMUY647mWzNca8DKBZU0j90w01arvY9LlrVtmOV-OeYVqRr_ks34uj7ELklY17w1AsADMJukKKpOaPSbowvha3tHHaq0TSHDqM8-5kVld-3k3MjBWhQRIlPGQ4BelhhOlJeVmw1yNneWxbx02uDRLDaAhqe76wBzhTmwmUhFkHlz7tq4jv_xc7UH2043qhJPIyKVer6n1ee82WABT36tqZ7aNEd1nKIVkfG-YMzWXgNoNVcgE14d6rbkv8zWEhVLfcXcVwXM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
مارک‌کوکوریا مدافع‌تیم‌اسپانیا: اگه قهرمان جام‌ جهانی شویم و همسرم‌هم مشکلی نداشته باشه میخوام که عکس دلافوئنته رو روی قلبم تتو کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/26688" target="_blank">📅 16:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26687">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_cLIkL6dgounRP5NoPCQdxkmaCY_WXz-aBAF7jBKsks_VcZcHr7sJe8rLqgzec9aNFSooWoY8_BIMtl__dQIbgQnkFS21U4PAjqGcp5g8kndl2czx7NB1aGyqdi7WSFZ2FBnUuCU-SKxYQNXsdYlj_zqzb85mMtS-asW5B_S9OOYjygVJosl1JFigd562tyEMJkTJ3HgDPRX-ma5jjf3Gzu1DvPelTu2oMVG4fFCLc0SiR9sSyPEPrJZmgHQqJVpg0yAGA7F-eFy1kQj2dwVMk4GAkTRVzGbyVQ4RZEhpHPUjiTaHTm8wslhpT1fS_GFnbxY9i3vqwCk2fKllBmxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26687" target="_blank">📅 15:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26686">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7sbaKvcIS5m32-VCzx8flZ9CHYTk81-v8O_XW00I2jojzJ1n6GWKdozV0hFZo1Vp5Yii5D2u3IwxDVWDSM1C2swdfO2wW88J1bs-8gQe5DTrLuPqteF_kZjVIejT5s65H-8NmhKdVVm33kMjHpU9SigKJafSAOT7arxKgWTp49AvaZfG8nlCikEuIt288f_sBAo2X5pgdEIXnRJcp6Z0H6hi6FP73SCZka3k3Atu-TtEHQXhcDK8bbWTdSUEHdb8FLy34-l6Lrpy17NXm5G7ee2IOFWO620g8gOxoJchiORyvxvtZsTURCtTI3BFhZzxYuIRjciR-PKrr43PvpnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛فیفا درروزهای‌اخیر رسما اعلام کرد که ازنظرحقوقی‌هیچ‌مشکلی‌برای پیوستن کسری طاهری از نساجی به تیم جدیدش نداره. هر باشگاهی پول رضایت نامه طاهری رو به نساجی پرداخت کنه باخیال راحت میتونه باهاش قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/persiana_Soccer/26686" target="_blank">📅 15:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26685">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZFXgIxgLv-pHhy0VbGCP3JR_IvZWlvtvbMcrTUXqiZUpmS70cw3BLxRxQvNfCdxQjlZGLFFS0Mo73_RsLDuR4FeERGP5uvHfwXMv3B4ObNRmD-4zl09xGGVbQNX_2F7kCWH2P4uUYP8IJEhIbngOWrVnI835t29ZDJ92RBKFHoH5czvxknsDefrKlpLvPA_m0fjhg7937HkIubsEYivWv_fxlSF_uYtmc41nLGV-9N50Ld4YSsCGgM0Ff-y_rPjUUBCVuUt1DQ4DHDz-ClSLw_f53maOboKxhgk9QEmE-JtClFYqqrFpAnLTGsAUWT0qjvbNKD3-hKETeWJKsOEwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس:
برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/26685" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26684">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBU-umw7MoHJsRiwT-X_gnSPJ8dPBwZu_3dO3lO2feIACTtleLbXfQghOFSgYVPMg1lxWeGHrot50C-bijIVvtrL0w31lADdiXiQ53H5B3DIRBwcrltWyPX_6MGWl7QZxgIe9Sqnyb-cbueWwnw3XvTUssazoZYyKDbJ5lJZKVGuCR4l8TrHpyFRBauCZdA6VpkICltsAYdXCInVjmKd3OfmLmsBbbWU2ag_Rr4Lm13y-sJRvEkzcQ8uWm4bPb7irlb_Z7hHycuIcAx6ladMKbITKAO907mfeur__QVaS12UEMJ8_Bg-KFPOZ3k8V0iA4EpQ0qA4wdXVGK4n2DfkSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگاروگزارشگر معروف ایتالیایی: فدراسیون فوتبال ایتالیا به زودی روبرتو مانچینی رو بعنوان سر مربی جدید آتزوری در یورو 2028 انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/persiana_Soccer/26684" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
