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
<img src="https://cdn4.telesco.pe/file/sji9SiE5wsGTNeelQ8Q9JKA8Gc6TOrFE67U7HIX51fofm727SMgGXIV3lcWkDdxdIikfDytfHPeW7cZKWzzPrbcXUfnvSImc5J5Dz9ucey-flJygwz1IMVmznAGp5FomtgXUX7c4lfHqatvzAVwSamE0w8VlSrtPCUMZQbosOg2bb8fRWM1AhbQ9tCoJpCvWVJsuQUGTGU3Wj0O8q-0Ps7K9XtqYOohqqt-ll7VjD5cx48v1Fu-OB2C87njGKjagSdB1E5fVO7f-Tc0qnlspm61-VgxkqV9kUu3qhuLnu1j868j0BAQ6wu-HtwMuYpgTrfdim0KJlQX8ZDBTayd33A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 134K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 10:21:56</div>
<hr>

<div class="tg-post" id="msg-90540">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a27edc87ad.mp4?token=QsDbo9hxqG6b-ef0NO_woSPNg1MNIzPWa7WCNK9tlcTtpIfm-fAMgXGqTEv8dYGlITMt6ZeOBmw85-3TDm0N3fPCHbY0ZYiKUVqVMz3B8AFpE1-iWX9IPqUmbqef6r0ohzVgq77q-iMdseYmaiv4xcLPNZz5DoCNO6IxUpNs5h6wPGpuXeSZyEEtKRjO1-4AbEhu_PkYjKcq-D7V41C3nBaFeIGh-Lqq_6uqUoCGD0r6zXgzlFn36w99W0ZzTcjv1qmD9m5BsxqjCzZoY08eIGGOaRep-jY0MvdvH0kQiDDYA-tXg1zUuKNHX0MNlaZMfMiI3MRy_Y70ggAruD_mpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27edc87ad.mp4?token=QsDbo9hxqG6b-ef0NO_woSPNg1MNIzPWa7WCNK9tlcTtpIfm-fAMgXGqTEv8dYGlITMt6ZeOBmw85-3TDm0N3fPCHbY0ZYiKUVqVMz3B8AFpE1-iWX9IPqUmbqef6r0ohzVgq77q-iMdseYmaiv4xcLPNZz5DoCNO6IxUpNs5h6wPGpuXeSZyEEtKRjO1-4AbEhu_PkYjKcq-D7V41C3nBaFeIGh-Lqq_6uqUoCGD0r6zXgzlFn36w99W0ZzTcjv1qmD9m5BsxqjCzZoY08eIGGOaRep-jY0MvdvH0kQiDDYA-tXg1zUuKNHX0MNlaZMfMiI3MRy_Y70ggAruD_mpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضدحال عجیب و غریب به تماشاگران سر صحنه پنالتی آخر دیشب گابریل
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 770 · <a href="https://t.me/Futball180TV/90540" target="_blank">📅 10:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90539">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLdFWotBQldN8n_r-1kSgMmHX9MIUdivu-qWVaAlsH8F-W6hVrOFSMN3q29sGbns6k0YiKnURv2m8S8T2pjKrDER_CUnGXWKvWh1Ngcb-qlrK70ULTofUTwxC_DbaM1klg2IPYa3Pbh8wJ_FukZAPuG2ZMVmn6CKbXp6sGrlKzFThCKQOcisdXIXfN2HKDeTDUXMRobPHwaGgX0JeY0bTtsLNlsTOZLiSs3EDkZgyoc_mJax8uf0OWlwxdm4TQfQkMTdUvZT7rIJROwqzPUj7oXma_yj-GQRCrD_m7IVIIS3kothoqB63MFjP5TZNZBNU77T7U_A-Xc7QZrWMAEeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رافائل لیائو هم این وسط اعلام کرد که دوران بازی در میلان تموم شده و تابستون جدا میشه.
مقصد احتمالی: پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/Futball180TV/90539" target="_blank">📅 10:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90538">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888a4aa5cf.mp4?token=cDKDFQJBVy-n8o0wkrwxvww63UBQHLRCObDdCmQbw2OcLLPTIY6S4KvK3tzNm79gsopKQco4qrj2W4aCw6n4wTMVFyyMB-aPtGSw4QNuXxXacGJyrWz_ZysafDShMiblJOz-Ej_IlKBreX94xTqR00Yb5y6DRCjQ2sVvOEGJLocJdT8tHE3l5soe5dmQ3tmb7DId-pKWPumt5ZZNe37xHX7FkIXk749zYB0cRRbgTePTg0HPgloeQ3_fWPufSQ1lgYIQY7fM4xDvXQPXOJ_OMKA1bymsqfdNMRJPq7u1dw8C0R-MNncnkrnEQ3MAuzVmyMvesfXO1UCxJueAuMuirg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888a4aa5cf.mp4?token=cDKDFQJBVy-n8o0wkrwxvww63UBQHLRCObDdCmQbw2OcLLPTIY6S4KvK3tzNm79gsopKQco4qrj2W4aCw6n4wTMVFyyMB-aPtGSw4QNuXxXacGJyrWz_ZysafDShMiblJOz-Ej_IlKBreX94xTqR00Yb5y6DRCjQ2sVvOEGJLocJdT8tHE3l5soe5dmQ3tmb7DId-pKWPumt5ZZNe37xHX7FkIXk749zYB0cRRbgTePTg0HPgloeQ3_fWPufSQ1lgYIQY7fM4xDvXQPXOJ_OMKA1bymsqfdNMRJPq7u1dw8C0R-MNncnkrnEQ3MAuzVmyMvesfXO1UCxJueAuMuirg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو مسابقات پایه ایران، یه گلر وقتی تیمش جلو بود اینجوری برا حریف کری میخوند که در نهایت ...
خودتون ببینید عاقبت گنده‌گوزی چی میشه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/Futball180TV/90538" target="_blank">📅 10:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90537">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔥
برندگان جایزه پوشکاش در ده سال اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/90537" target="_blank">📅 09:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90536">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a192f49940.mp4?token=HG9QGwqoh9MN9-IthtStdVtObpjTJkZtb4BTwCvzVidhMTn2myRbBVB6NOakUL0AfU2bgiyzOA26Uh3HMsCvO8j-WTXO5GhvdV3fM1bMxDzNWzvK02Bwa-fHebJ1AhIjN1eJRpM5YVC3NSN79mGUHyX-_SWJklM3205ao2VVSOu4t3i5LfjRK86_2R9nRpCB6HUCI0F9bcH5Z3IwPdH-Pc0tmCd8-tF_qfnvSnMalqTMaXJVHdPuABCHV-8tuTzh4Hos9DWOj37Moj8zhecQOaI3mcw4vlcSz1LwazOPlGIzoAuW1v_VnvDETXYzfzMD4XrEV1XTY3pDJs14ydLzjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a192f49940.mp4?token=HG9QGwqoh9MN9-IthtStdVtObpjTJkZtb4BTwCvzVidhMTn2myRbBVB6NOakUL0AfU2bgiyzOA26Uh3HMsCvO8j-WTXO5GhvdV3fM1bMxDzNWzvK02Bwa-fHebJ1AhIjN1eJRpM5YVC3NSN79mGUHyX-_SWJklM3205ao2VVSOu4t3i5LfjRK86_2R9nRpCB6HUCI0F9bcH5Z3IwPdH-Pc0tmCd8-tF_qfnvSnMalqTMaXJVHdPuABCHV-8tuTzh4Hos9DWOj37Moj8zhecQOaI3mcw4vlcSz1LwazOPlGIzoAuW1v_VnvDETXYzfzMD4XrEV1XTY3pDJs14ydLzjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
چیزی که اینروزا اتلتیکو بجای آلوارز به بارسا داده:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/Futball180TV/90536" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90535">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae10b6cdcd.mp4?token=FyqOBX827So63V-Tld8VCAgiPXiQKf6YfJT9PqQiLMXjhFogmGHj-1VB5pjr_ZvbhXZu-KpdnkRV_FS717UOo73TvenDhCb76MTVTuWWvJewGo1oun21Nt36CUVLw0Re-DxQT5MmdbrS3QqyPGi-QAjvvZfjqj_ToD3Vb1QZy1Fv1B4z6im_7AVnr1mQS975SmprxKnjpvlHuOMlN002fgfIy-4TAshILbrJ6a1ifmRPvEJP6qtWQqa0qudHjI6Xh9iUHtP1cEPXNRi7Dc7kensLOOt-1GxBgWF1suie3S0_pU3TIrwI7qE3oK7NrX2h9_MBOBHPnDBZl0RZttS54g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae10b6cdcd.mp4?token=FyqOBX827So63V-Tld8VCAgiPXiQKf6YfJT9PqQiLMXjhFogmGHj-1VB5pjr_ZvbhXZu-KpdnkRV_FS717UOo73TvenDhCb76MTVTuWWvJewGo1oun21Nt36CUVLw0Re-DxQT5MmdbrS3QqyPGi-QAjvvZfjqj_ToD3Vb1QZy1Fv1B4z6im_7AVnr1mQS975SmprxKnjpvlHuOMlN002fgfIy-4TAshILbrJ6a1ifmRPvEJP6qtWQqa0qudHjI6Xh9iUHtP1cEPXNRi7Dc7kensLOOt-1GxBgWF1suie3S0_pU3TIrwI7qE3oK7NrX2h9_MBOBHPnDBZl0RZttS54g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوتی‌بازی مارکینیوش و دلداری دادن به هموطنش گابریل بعد خراب کردن پنالتی
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/Futball180TV/90535" target="_blank">📅 08:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90534">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5c5d95ce.mp4?token=YEKNqQ7cm__zDXjoxY8lDCHe9leVfLMamswax9gs5DCzVAwGmVNjIllbf0-rG07-muG-uWOjXe9TnsXdip9DVTLFth8XRCMTD16yyuPcs8GcTdRx3VaOvG17_QjWC8Q19uNqvUfJ-_7waeGNKrtvWl4YwhndaimLuKZKMKNmrMzdg4nB7XqVRYAHwCs5cdVbaygaAWNlElY_4Hniz5paez_eNGencQ3IReCBycH7QeNe_bDcjETZ8YU0AioFRNje7o-uIgUZMjSlDssCrWORGWcF5xrsxgECrsmtlMowsC9ecSyGiTXZiOq1LaoVYrY44WCrRRFB7ochcOjiMzxAfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5c5d95ce.mp4?token=YEKNqQ7cm__zDXjoxY8lDCHe9leVfLMamswax9gs5DCzVAwGmVNjIllbf0-rG07-muG-uWOjXe9TnsXdip9DVTLFth8XRCMTD16yyuPcs8GcTdRx3VaOvG17_QjWC8Q19uNqvUfJ-_7waeGNKrtvWl4YwhndaimLuKZKMKNmrMzdg4nB7XqVRYAHwCs5cdVbaygaAWNlElY_4Hniz5paez_eNGencQ3IReCBycH7QeNe_bDcjETZ8YU0AioFRNje7o-uIgUZMjSlDssCrWORGWcF5xrsxgECrsmtlMowsC9ecSyGiTXZiOq1LaoVYrY44WCrRRFB7ochcOjiMzxAfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاریس دو سه تا دیگه قهرمانی چمپیونزلیگ بیاره از اون شهر فقط یه خاطره میمونه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/90534" target="_blank">📅 08:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90533">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">💡
میخوای یاد بگیری چطوری با همین گوشی تو دستت از پیش بینی فوتبال سود کنی؟ سیگنال ضریب بالا و کم ریسک میخوای؟ فرصتو از دست نده همین الان عضو کانال VIP یونی بت شو
👇
➖
➖
➖
➖
➖
🎁
کسب درامد از پیش بینی فوتبال راحته اگ این کانال داشته باشی چون کارش بلده ae9: https:/…</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/Futball180TV/90533" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90532">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiXklXdLj0e4THvjj_OIz_7YBNAaQ1WeV6dnf7XCI8oQ1Xk5yOaPE0HMFhaPAggzrfU6W6hTnKLGPvnPn1bmKb_wnaQX4txqlr6Mp-dAJLGPsod8x8elKwkzrloIbuBNgr4WJWiKtQmE3-betw4QC6aiPemJsgBmAsg3uCwWk1t_RMPPQvqLUBemsk4e1WfGstbliPc6SVYtXCvxSJx2_Gw1Iudytlo0gFQRRwJl5ZOcD42JmKVS7Vl4GDZ-_cI_aQFewVLWxR0xVtX2x7SyUSJ4kLSPN7RYfRs_Y4Xoyv1CrtGFtf1vh2XxZ2r01rOJ_WCICmc5ryEYZa4LMy4qdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💡
میخوای یاد بگیری چطوری با همین گوشی تو دستت از پیش بینی فوتبال سود کنی؟ سیگنال ضریب بالا و کم ریسک میخوای؟ فرصتو از دست نده همین الان عضو کانال VIP
یونی بت
شو
👇
➖
➖
➖
➖
➖
🎁
کسب درامد از پیش بینی فوتبال راحته اگ این کانال داشته باشی چون کارش بلده ae9:
https://t.me/+YwYFluMQ5-kyNmY8
https://t.me/+YwYFluMQ5-kyNmY8</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/90532" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90531">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbXtmMHiUwlaTyvGqyfA6oqEYU1ms7C_Dh_mB-eGZOdcIGslSD0dJ4eOOVTPj8fNxT_0DuzoBhZF2qGQ6OuvAhkXiZlrveMOWAkbRfm6bbY0GcBSgXpP2C3g5zW8ctDLWGeuCjW8AoIQCYdXqAtMQVcVlY19wxLkNfeMMivz7hd1M9kpRYndu3QL9lTkX9ls3SGuCHsmuE33pmho64sFgVT2yASvYnTAg3E37oKje2qLhjNdXz_DJbjre6P1nVuXVbMsUhoSPVS3sOjmTlv96HXZWJxLXg2q4OaJd8qHEr55_BMJQZXbrVK0d-Cgo4q1na1GK2RroKxDZYWkUkazcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
شماره 10 برزیل رسما از وینیسیوس گرفته شد و به نیمار دادن. البته قبلش توافق صورت گرفته بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/90531" target="_blank">📅 00:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90530">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac643b260.mp4?token=WFt8-KMO0UiDrleBACjmsbo_9dgygZojUN7wMXLJYHOyiD5BkIUIRSORBfHIYzlbx012lteBZQqjBDbmjmkqNyG-sH2HzQmQpysOCM0e_hfrtSc-1JHhfFj3lEcHEe-icQVVgQHfFAcWcMeQ-4Yd8oGZLlD4IWd7hPVeIiKUaBYiks1kiRt7fWbhPAprKzwdWkNAYla406bGKnnrb03CNQnP6Zu33l97Q7Z9eMaMi0-0cOsAfx30nG6mPmfPJJkNnkQ_gY3bWWJADVIxNQ4xr931x-dYP9UtOTV5MxYKV4K5uGdXm_jxoYa3lT7KMeeOzECImyX15yP3tGXM9nRlJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac643b260.mp4?token=WFt8-KMO0UiDrleBACjmsbo_9dgygZojUN7wMXLJYHOyiD5BkIUIRSORBfHIYzlbx012lteBZQqjBDbmjmkqNyG-sH2HzQmQpysOCM0e_hfrtSc-1JHhfFj3lEcHEe-icQVVgQHfFAcWcMeQ-4Yd8oGZLlD4IWd7hPVeIiKUaBYiks1kiRt7fWbhPAprKzwdWkNAYla406bGKnnrb03CNQnP6Zu33l97Q7Z9eMaMi0-0cOsAfx30nG6mPmfPJJkNnkQ_gY3bWWJADVIxNQ4xr931x-dYP9UtOTV5MxYKV4K5uGdXm_jxoYa3lT7KMeeOzECImyX15yP3tGXM9nRlJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جام‌جهانی نصف شب با گزارش سرهنگ:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/Futball180TV/90530" target="_blank">📅 00:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90529">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEooXv4bGZQk6VC8ADlhm1mMNPsCmG9pKxrV5wBvcZKGD-zpTYElK6WOwcWNv3N5yDNMm0zcnAfG29KjviX8KUfITBrEJBOzbhIpM7Z6R-O_AMmFyz51twMeUb9_RYzty7EW-YNP7wyp4Pru-Tqhwr6-jAvABSZK0Dfio87zHKJW2LLRsjnTayVm10sa4Bw2ZFSX8SJGpSNU4YBcLJRbUoHNObsJrsaVJhasTeZcOxiY3QgYppDsqBz2NugSAtySf51E29JqosakMxwsLYrQ6M9TRzye9a8FEF41mSqmY_u_VoieXcPEww78nSUtGY9ErSWxtA6Zxb9EoMw8CSLY6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه با 15 گل زده آقای گل این فصل چمپیونزلیگ شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/Futball180TV/90529" target="_blank">📅 00:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90528">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=ZQWBkTb6eASFItgI4q9oThS5iFcSh2xWNgfHwmNEx3sQgkRwyb_s4avY8rzlt9b5dQT3wPwZWuQuSSqwlhn35koS9N1NdBYCE9LZ2czYCfAHl-q8ElO4vu4bEKFrE1s0CBNxOKnGXSIcG-ugDOq71Y85_fFwwicP66gQHoPEZTZNFD0Ybn6rVg5OXg1qI7iEPmOG78uWv13hNDJKYLhmGgasI4YnhqBBlbE_CWerbhYgMAiB8AogPyeHw3RJTkr5Y4jQWKLsD4yNRB2UNKCmYg6FcsT5prlViF6cRQYdtnfx1d8pGSHYtIcW2ZK42oQ0Spr6Ym_NlcRSptBc6WdFag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=ZQWBkTb6eASFItgI4q9oThS5iFcSh2xWNgfHwmNEx3sQgkRwyb_s4avY8rzlt9b5dQT3wPwZWuQuSSqwlhn35koS9N1NdBYCE9LZ2czYCfAHl-q8ElO4vu4bEKFrE1s0CBNxOKnGXSIcG-ugDOq71Y85_fFwwicP66gQHoPEZTZNFD0Ybn6rVg5OXg1qI7iEPmOG78uWv13hNDJKYLhmGgasI4YnhqBBlbE_CWerbhYgMAiB8AogPyeHw3RJTkr5Y4jQWKLsD4yNRB2UNKCmYg6FcsT5prlViF6cRQYdtnfx1d8pGSHYtIcW2ZK42oQ0Spr6Ym_NlcRSptBc6WdFag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل گزارش امشبش رو به این شکل شروع کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/Futball180TV/90528" target="_blank">📅 00:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90527">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEFF6tiFu00JTRKSY0w5Z7_isn02kpNQTEq6tyof-Hd3tqeKELBnx9QbsOqwQXXh6Vjg5kfGs7CJPaEaLYLQAtffBhKF21UNTVO85d1CLNVNOo3o2vTA-cNomcfw4EmEnQJicYR-LzDxMgEWo4HSLSNwSJ1NI8Q41Enaur-lvXlAIuFfPpVKocjAfExXgXuJee9yRHiU2MZOQs8EszTE__pYszfETHQYM96cnjl1dbJ7W4c1QYfnuukwp4tgDNSZ9_QIE8FjKifCRXOXHBTgU2wxLIlEK75Mcqc6iL4oPRMQHshyzgA3ov50EHxzLfXGg0_SPOl1_9tx_bb8qooXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست کریستال پالاس برای ترول آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/Futball180TV/90527" target="_blank">📅 00:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90525">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz7Bfe45kBsvH0QRnb5Hu4anpCBu6l1uROrqoulN-asZYRtYr_WOLXoWM9WDwm7KElkg3PxADiZvjj1vuB9B1Qs7Cc6hXvL5XBXkwivRcvFrAe4TgyLoZw71QttQ-qalTYjZDtixvSHPKL9_M3y4Khtg8W-V-37M02KS4Llkmpgs967q70zWsRngl5f3D-U1EphjngnYOo1zGaeHLHIOSHEZ_KssNOKzHLHEldJxTisSeflQ6EoSH7ha9EiGsp1m2ksrGq6sHxXX5-r6uYm7qOySvAMbr-cpC0LFHgnvV8EC0Mo6f_hg_PcakZfUvBDzh85fKcSI1FiTR8XRxkZWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل آرتتا:
می‌خواهم به پاریس سن ژرمن تبریک بگویم، به ویژه لوئیس انریکه. آنها بهترین تیم جهان هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/90525" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90524">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDUKIyR4akDESRIa4Jn7stYsyejDS55iqPEW3s9slEZgHN5ouR6uQT1NGc-xGcvVGQ6dJAl0PKAhKna3dAjJQ06TfoSSpIaRCoUHyoxFESYeTFCWL2oA8-0keV4CWJ3of-BQFOVItALEYxJLgU5rPlnprbnGvtYo6Ol3WTrQwjmjI_S6LFqbBwjARP18PyrTaM9cM2ZlUyvuKuRYpBAZtl2VvI2L_PaZSHpzQEhM_xupUcnqgd6YQM5xUGYqr3rNR9gMLiNPEWi1HSyJw_OWwIn0u33yf7qSokeDQZz4nB1rza9cuX_GlEFEvReUtN6mk1MOOZIxC4hdEofMczXuRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید چلسی بعد از باخت آرسنال : به لندن بیاید و از این جام بازدید کنید
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90524" target="_blank">📅 23:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90518">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUKwGwyUay_TNZYUh5SwDB7frAlAEP0cfnbmiUxSHwaIb1InBg3P1BREMVH1-gBIwXisMccLb-o_YxxsNLtKbznKoDJnPPlJGtMcc1PzdMaBWQbg017vsQlr5pAiLHZrWL0T3BloFYV_JON7gU7gyMHUlPOCVMb7XKa0y7xhTHQElZoZIQb2JlP8KmubS2LEJFnStVkaYzdI-HzfZK4n7vydcVRuw7CJ1qDT_DoQU-b-_BYy0nc7bu3veagk5KX7QEL5mCzj6lfYO7r6nnP7TDGYo1NmUXKMns9aRD-atJM63kzsx-CVwJi20fkb12deuWTVfljZo0L4JUFewjIE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxW1SyfsabYk9C239zdHP5rT7--fdaMP8P4SpmvB9uPk35R08S8onrGl7pmd-qEnvW5RNVXcImwC39nKb77fixKHaXgplq0Ni1k4xkKvGZqM_ueKxvEQdJm3aHyojaUjoCq8Tc3Kpxt09BQ7NIWeMVVr3nbEbN3GcCNe36hCqzDmHZBjMOkfw2bnUi3iBXk1Cnm3TaenV17bgo7qk_9D9Pp-25LoQ5mlemLq0QH6CJkQ0y7joh28SZhQHN9jTfMS2JnptomMr2C1D0IxnS8BlizVzzEwD9avntEXl6Q61shOgnNdgi2Ln2LIj5RYKuiEqPeNfiiTcuAo5RdSbCkLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QF0gRPgZ3_iGY62BU2NtVtRhzT-EsoJdLrDOWuSfhpDs8A77_IUUbuEXLjh5gwsnu_VTJo38kveqDvb61FvOJog3heJuv2IbhUyRYuzSEBGWZTiQbdvGMHaZWXRBUVJHbWMXN5LsdvaC9DEXWgs1Nqzxdkc3IdJqrF8OspoabljGygDLJN2bX_gr8SebNprW1w41cZVK9490DW8PDYUWj1c1hIuZZW8eSCVwxPb0HBwZRsGHyJqwkxWTs_WYQg2Yw4-034E60oKomY_gz_FabXN4RsFwsyHfHKam5959TEhRSYlWsEjInIotz6Pws_uq6tI-EiJ6MVuWGDIMI8Nhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VScfe9IOJw_3zPjSedJjb0bwJMv_qs5m9CewOlshfM8GAHY1oWUGIINhUduXJEt93-CzkJSXEJTlOtdplnuRcV8_4LzO-GAIGRzAsMDeLNjSiDKSZht8-rIVAHwCil_dqVxk44EOFbG6JXjXBply6EOeYclkno0gHUgm4UKZ0XeWjSIYA19eMT5EBTb7MjPwxLUVt4GGCKXhL1YavwHh-Ucsakqqx_CP5GpxnqMNQxO62kMtnf9GBSzi0KgI56SrH06Byn_HEDKO11vC14AvNAYNNpKM0YEn0eFYnYY_ojMOO8BmTzbtk3bPqoPv8_aHqfHcheGwsUBZoIJ-CY_vRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzZVn9UCo6BFVKN1yx5YzUVfK8AdXbh9aKnstKxrrvTWeaBYFJvYLO1kTAeKa3fwPZ2W8sl-AsaaWGQ5GzuiSkSSDji7HuO0V1DhbhNtZ1_lSGPbjm8tt5XYpKwV4LwAuohNxjohxR-TrZOn4s2ojXGYW_XcREGzKihw0WBpfELQbfCL2FjEpZusKqPCMi4tF-weD6kFGONKSsztTrYnu_XMUCWly6EkAgWCLon5qA6ucUW60IsmoOWf6CCFnw5_jtRkd1YRVOP_1cPFowDuMXnFZlmhUNxTeaF2tfsVSj-x4Ttbm3wMafnKTrfOddARd9-LqHuhI1gttR4Mn2uHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQuH2_ub59R146xfuGdKC-FlabE90m-H4NFA-_mF3Lsp9YPY3gYCQUmvjTKTKMi27DFfCmg9KaI3K4bLYO8TTiUW251LC-XamfsEcTYjsvdFyCDseD-IIiO1wEw7oMcpKjeDz8MX1n7jq8fsqSk5f2ursbFQSU1jhChVHq84XbgZ7SDn_983pSX11YGBBUVaXVSJMwcCAWLVjmqYFGico67s0mw9S-cYzGwNprfQos9oyIfq7pVv4mIS8WTlQeizjsjmypvo6Xn0Ts9qVzfB23DAUUQZwqw31F5uPrw6BS9Rq__vOUUxz7QIH3FHehw49f8ey3WXTtKVWsxA83tNEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از جشن قهرمانی پاریسی ها پس از دبل قهرمانی در اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90518" target="_blank">📅 23:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90517">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">عجیب ولی باور نکردنی!
امباپه دو سال بعد از ترک پاریس: 0 جام
پاریس بعد از ترک امباپه: ۲ چمپ(بماند باقی جام ها!!)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90517" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90516">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elthntzkPkCnSkCqR1dKc3njDAhPO6h5074f5wnbcUfJKr4fv_KWWmRGb76c49tB8O6j5Yxd_0Tyk8Ys4HinUELOHBtJ89LSzJ5sWWQRFofbRubsDmDsIZ7lUiVIgg4o5-XPVIbo2EyYVyPMaEjq1h9s335w9SiyYi3t7ITGHDipgB8gOQTxU_2rN2nnuH5w-5dHb__qIm8aHS-Rz_WuCbMWgJQ6PGgaimP_xUf2mCLQQCN18jH8xMBhU6A2krvHAlaeGaUYj_ZKiZIdh11AXoVJeNZzxTCZgFgnPxhZ07qynwcvwgZ7f6I22GBFNPgJNRCU-duKztnb1DIrmYCUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آلمان
🇩🇪
-
🇫🇮
فنلاند
🏆
رقابت‌های دوستانه بین المللی
🌍
⏰
یکشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه میوا آرنا
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آلمان در
۱۰
دیدار اخیر خود،
هفت
بازی را برده و در
سه
دیدار شکست خورده است.
✅
فنلاند در
۱۰
دیدار اخیر خود،
چهار
برد و
یک
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آلمان
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر فنلاند
۲.۶
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۲.۵
- ضریب :
۱.۳۰
🧠
قبل از ورود، بدترین سناریو را مرور کنید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90516" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90515">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پاریس دومین سی ال متوالی رو کسب کرد و باز آرسنال ناکام در کسب قهرمانی سی ال
🔥
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/90515" target="_blank">📅 22:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90514">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تمامممممممممم</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/Futball180TV/90514" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90513">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گابریلللل زد بیرونننننن</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90513" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90512">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">زد بیرونننن</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90512" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90511">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اگه آرسنال نزنه تمومه</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90511" target="_blank">📅 22:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90510">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گلگلگل برالدو هم زد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90510" target="_blank">📅 22:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90509">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گلگلگل مارتینلییی</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90509" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90508">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عجیبه صداسیما تاخیری نداره</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90508" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90507">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گلگلگلگل حکیمی هم زد</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90507" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90506">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گلگلگل رایس زددد</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90506" target="_blank">📅 22:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90505">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رایا پنالتی نونو مندز رو گرفتتتت</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/90505" target="_blank">📅 22:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90504">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رایا گرفتتتتت</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/Futball180TV/90504" target="_blank">📅 22:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90503">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ازه زد بیروننننن</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/Futball180TV/90503" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90502">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوئه گلگل</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/Futball180TV/90502" target="_blank">📅 22:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90501">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گیوکرش هم گلش کرد</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/Futball180TV/90501" target="_blank">📅 22:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90500">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">راموس اولی رو گل کرد</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/Futball180TV/90500" target="_blank">📅 22:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90499">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بازی آرسنال پاریس به ضربات پنالتی رفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/Futball180TV/90499" target="_blank">📅 22:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90498">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امروز خبر اومد چشمی جام جهانی رو بدلیل مصدومیت از دست داد ولی چشمی امروز در تمرینات تیم ملی شرکت کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/Futball180TV/90498" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90497">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
⚽️
⚽️
⚽️
اخبار داغ حواشی فوتبالی و تحلیل‌های لحظه‌ای جام جهانی را از این کانال دنبال کنید
👀
اگه می‌خوای جا نمونی، همین الان بیا داخل�،
👇
👇
👇
👇
👇
👇
👇
https://t.me/+5NhkIyyAtBhmMzM1
https://t.me/+5NhkIyyAtBhmMzM1
https://t.me/+5NhkIyyAtBhmMzM1
✨
اخبار داغ  و کانال معتبر
👌
👆
👆</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/Futball180TV/90497" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90496">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDBl6DlbbQbn_Az4IZ9ZeQw5V5RFPb1GKH__xybD1kRRqdwh_wuz4UPPC73lJ_1iJUKPzgX4PmnicEv9rzb3m6oNgpmZZ9aTeowkqu7V5e-CPhGyCaslcjfbjv1rz0vyY7ucpXAG_EOeYZQbNLgbYvxXYDOlOta4fj0K-rYlBWsTANQhkVGV0i0qVLG9J4Lum_69vHkMMPBqYbJ28JiZZdpCd9aiTjZGnj1jGDspHlxxhi87OejEFTSY3iXodSS6NxUCdfsGBMXPgzhfb27KJbNmb7-O2Ety5d4mMP6VuMyTYmkgr3EmfI2tihQgpw3aLOfmZ9stHw81wGrTNzJ6aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید یاسر آسانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/90496" target="_blank">📅 21:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90495">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">موقعیت های مشکوک به پنالتی جذاب تر از خود بازی بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/Futball180TV/90495" target="_blank">📅 21:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90494">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پایان ۹۰ دقیقه
پاریس ۱_۱ آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/Futball180TV/90494" target="_blank">📅 21:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90493">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/375a1431bc.mp4?token=k55UZ_Z5VrSnGiB_d-okQ4gqamrtSFGtqqJ4JgjU8X8Cwa2FZrn4Fl4ZydTuc3C9Y8QE6aYVNYfko4h0K4zWTd3B0kTeGHgcwwPR5as7rZITxW3MR5LQLyW0FFdUqH9muagwBUcsyGYvZxGu6smqd-M6mHXz8NmYm-xdYmytQ0KLlfaB_k2gu9jR9PnzYiLpOD0N48QCU4z2COpXlNdp7kuqALsV2uVwLu4wOmDf0qv7KfbV9cwoShJZIk83p_EeVn-52IXfgUzUj7d9t3KFQKumecoWT7OwViuVqhjBaflB0uxOnSapnHo0ei0Kfc4U7xoQBZyqqRpHR3kaL7Mt8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/375a1431bc.mp4?token=k55UZ_Z5VrSnGiB_d-okQ4gqamrtSFGtqqJ4JgjU8X8Cwa2FZrn4Fl4ZydTuc3C9Y8QE6aYVNYfko4h0K4zWTd3B0kTeGHgcwwPR5as7rZITxW3MR5LQLyW0FFdUqH9muagwBUcsyGYvZxGu6smqd-M6mHXz8NmYm-xdYmytQ0KLlfaB_k2gu9jR9PnzYiLpOD0N48QCU4z2COpXlNdp7kuqALsV2uVwLu4wOmDf0qv7KfbV9cwoShJZIk83p_EeVn-52IXfgUzUj7d9t3KFQKumecoWT7OwViuVqhjBaflB0uxOnSapnHo0ei0Kfc4U7xoQBZyqqRpHR3kaL7Mt8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل‌اول پاری‌سن‌ژرمن به آرسنال توسط دمبله
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/90493" target="_blank">📅 21:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90492">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گلگللگگلگل برای پاریس توسط دمبله از روی نقطه پنالتییی</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/90492" target="_blank">📅 20:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90491">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پایان نیمه اول| آرسنال 1_0 پاریس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/Futball180TV/90491" target="_blank">📅 20:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90490">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">چییی خراب کرد پاریسسسس</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/90490" target="_blank">📅 20:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90489">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asa5CulCveMH50O4vJdLzIzmEUengE3JqHAN7d6rVKS5Ze86ykT-Kj6UuYWjQPlVDdKQmpQgeQLWRFIfG0s34LTHosQ3u8U0i0e7t6xwkF5XAaBfdoaGjWxVI8WNZzLq11Dd9aPIWlwtJv7yvB7FbSMWwD8qUnIj3eZQcPjD0S6vZnV4uvh3bjer239iiuId0ds-1JrkOuFHddujOhIBPe_ljZFtykj7b7HqtrcIJe5EAbNjUET4GtlnEkZ_lmNNbiymFC4QPkY1TsdaJXsVlZcOJNVnDPBBxaBJjGq3I4nEstQtfUGCsDq6cEMPXZ20-ljdG15jCERBHJntaoD9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرنه اسلوت گزینه اصلی مربیگری میلان در فصل آینده است!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/Futball180TV/90489" target="_blank">📅 20:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90488">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikwyUXrAuvmTyNnxlfF1o_KUvCgIeeEKrHfbKTGzMEHh_rrNKlOgFjz0kpPQV00sg2tmubYviPzVOdg9D0Txs-IR_-yyzLD_3a8xgNvAslSCpWl4eo6rzi6FFwA4VYIYCKGYHR7r94ZC9vYayorcquTfO6YDfmY5k5SupSck1dFCW0WYuiwiUO-mvhnuQEwK1Y2ysWWCPAP5uGYUEtQW6X0jhtPuFMv6wC-XNN0oI5Drwg6etM6JFdjfDtSw8t1pmdTWvZ8vSLYzI5HIw6TFGDBFpl3DZWVH1psFivsE2IWEqUR8oGU35OcDEOvJxsnbezZAokdEJFzzkbdC7NC5sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنالتی پاریس گرفته نشد!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/Futball180TV/90488" target="_blank">📅 19:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90487">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90487" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/Futball180TV/90487" target="_blank">📅 19:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90486">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quWZ5VMPPnTQ_TOFizvIurCC0fF6jFfRof2Mc5IL8cFms9eceoQfSwaoUYNBn4TZu-oFaQNN22ApQJD5i-d55-rbfiQMkZzusy-oMmlKifixXOYmm9GASUHpcOSLcp_d-O_RgZ7onOPG-XH90ya6u30LpphknIZxhM8rT25WecN2ljSncHPgB2UqZ0lnWu_RT3i6OOOAUv7Y4PWBRsZzS9Uc4B-Uyzv93KURo8_F6tQqeLFLQwFnORIFQuWBKA0GmhhhrV4jmdBC2L5wc6T2i1yHziWqcZBo66oDm7KZgCzshoWFhE4OFepIJiSIY_yCA-H3Vz9a-GT7ECpYv_nf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت G9:
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/Futball180TV/90486" target="_blank">📅 19:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90485">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFWhTnOTjCMTvFNOhCH_m_emTfXI02jZpa0AmteH5qTwiM4mA-T4ppdf5nZviMX9s1OMt4u1zvuUyGe0r8vym9iHkgTbZrQaSSAP-emrx9w82x1ZtxE03WvMMaQO-ECLJNGsjjjBZ-zHSKt_sj_rrsITGJ4p45TZm4jpV4hrrsZVssNsrC5Blw7ydjooI-j0dBd6V-xDZhe9VGMia3AehLOH8ajqetrmfOHZE5uT3XFc5zqoGSwJx5JbHzNYp0aNwmOTh-dn4rOwkbHx1SngfxdBtd5RxEG5TdqZN3ocpWpBdYsASMErHo8DP_t3extCECjtbipEYQrosma8v8mWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنالتی پاریس گرفته نشد!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/90485" target="_blank">📅 19:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90484">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/71e697023e.mp4?token=RRvSBSAcur-SOGrEP5WaG4apj0SNhjPldFEY1oeIFkDvjbOI0BLUYvdaaoo1jaegGRWqbsd83i-TSx2frd_JH6wkq84yFGIbOmeBHVQqeMsIpJnP_1uL1sCVScVpHtfton5iR_V8U8uw0CepJ1xJu4TlK6R063Mgy2FKkPTTuMB-HNqvOlcxtIlPlN9Tp93LbOXMrzZY__UR60Z8pl8HwuuZo6YHUncQUeqA2ldAI7WDJrIdJ7KSs7TvNHqeb8fuW4eo4RF_B63MIUVYrVsupi5EbDvoZSFCl1dmJzXnepU8oqrqJdljOrlVX1ulP8nNT4FHWHoZn35xOdsooG1Dfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/71e697023e.mp4?token=RRvSBSAcur-SOGrEP5WaG4apj0SNhjPldFEY1oeIFkDvjbOI0BLUYvdaaoo1jaegGRWqbsd83i-TSx2frd_JH6wkq84yFGIbOmeBHVQqeMsIpJnP_1uL1sCVScVpHtfton5iR_V8U8uw0CepJ1xJu4TlK6R063Mgy2FKkPTTuMB-HNqvOlcxtIlPlN9Tp93LbOXMrzZY__UR60Z8pl8HwuuZo6YHUncQUeqA2ldAI7WDJrIdJ7KSs7TvNHqeb8fuW4eo4RF_B63MIUVYrVsupi5EbDvoZSFCl1dmJzXnepU8oqrqJdljOrlVX1ulP8nNT4FHWHoZn35xOdsooG1Dfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول آرسنال به پاری‌سن‌ژرمن توسط هاورتز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/Futball180TV/90484" target="_blank">📅 19:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90483">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سوپرررررررگلللللل کای هاورتززززززززز
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/Futball180TV/90483" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90482">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آرسنااااااللللللل
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/Futball180TV/90482" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90481">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلگلگللگگلگلگلگلگلگل اوپوپوپوووللللل</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/Futball180TV/90481" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90480">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvgDtCyBjsjLhIohtJ__Zn073IZxxCvtStX3wxj-l97iyq6uSkm95WGfS1qIiMfh4VQBfUre2PYdmrLnWzk5wXHRmvLhdkILlqC_boovCcuXECE_RBp8Gr9B9S3HSM5a6932SsUYbD8m4gvptrUPonaVRIWiY04tHlznQR1DtGTlIYn1qs1bN6tT5-YzIa1SbkvjJRnV0y3YzNV78zEKgbtQpcLSTFVt21Cpvkk95mzQZpaz_vI0phhuVKEeWqwuNLEf9Xj2umej4AcZfyj_4oZiZOGoePBdvquYtAV0iFQqL7WsyDWqx1WwUx1Yw8wNVF3KG6YZCOmswSl3cCZUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتوی یک هوادار آرسنالی از پیشبینیش از بازی امشب سی ال!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/90480" target="_blank">📅 19:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90478">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pb-9OAGue9OcoYG4tY1SIUU7GRbjzMqixWLgc2X602pb6feSeZUEPbCgFkOQUa_H3rh5ms0RF26YJSg3P9qqDExp5zKmQKcs5c-Z4z9LVLvplOozgztoeDH88ieZOPxZPlktOY0MihSF2pOvolkv06Ioj8m9RVN-OmXp0uDovZOGs0fDnhKVLsjVEa-UojnBLcKrZr1iZB-3-7hZ_Mt39--23R_20FNzU7hjvafdHtHUlhdAFhhf8nNE_5u_eOkkwbz4PNSrlVIE1KsUaxXiTx38GOedJrYLFD1LLKncCt819zdtUvXguS9gTYE3Ziiv-G64dudKfrK5wwy77mz7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuuoF5xZSqH3xRaemvyV_9UoszaJZqaPXZH0F5W-pg5QOKGF9NravdYOCEjrpw7A46JMkBzX1BrrNV1XfiP6DiLP4HIN0ctbcQhEC6ys2Dk0oc7e5acbs4S0GZKERr4FFkdutwDBpijJHE-yy7CyQdxrvPe5SxetmvUqDL8UxXQsZ9kI6AIl1AmnUz7tfl4dugJptaizMKBIU2d_AYaZMX0EWWd-ONwWJ5LRPmv6kxlmDTLBfqXrO0vxZNFOsg9zCWDd_pk2sxUlSnAimFY9dhDfR-TKUS6qM-VhVJD79kXQVIMWUHgn4etpkhI5VUdlSakPb28CEQMe7YeH95Rb4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسکواد دو فینالیست ج.ج قبلی و مدعی های ج.ج امسال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/Futball180TV/90478" target="_blank">📅 18:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90476">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhgMv-B73FDLNWiXM3hZ2jCArF54UU9zeHkmXA3r4C9PEfKUpn1EQlTNMUkqmsNxdAN1Q-uMaVOu2R4OAezhzyo-gfg-sFdv7mc8C3etw6EIHU7B8CGdXIy3dCRhXKFpSfrFpJ7FONuVhq0uzNOQvT6ojortoqKjxfzr6C1kMEGldq-s0Jbp6E_LXTjCb0jSudrLG2ZWdQEBxpQobcE7dqDyB-AhMKeQn35ghMfz0X-uCL-TVLxrc9tSIkdAqMCPELvvdHdPwmBD48sxmLTNI2C87S3nTqtxyC93Tgl8C6Op0KQGQ9R1kOvnFA_y1ODn3BD7UrgdgAuIkg39t8nd4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1MhvFcXu5Lggbm9jH0npklyNTPiFC1HXOOQvf3ruvaUtx0zmzP-ckznUoU7_EusCWKjhpd7fGZJTgdq2HCcXSNXifeGWfXeqX30LLZQxbCqUjqxuPrpVlwKwFq30E6OFHXRb8_FiqGPgcCGgv36cce6zvuwuPUL5_aovu5oho3jgY-4yGZEfQFSO0sZQ3M-ylYS7UB7AwKggyP5UapVTniFq-2neYQKh8e8UhYsu6NjiDcniHpZ8AvSw0wsAMDncCVD1WuGbo9T2xcHSJUPjhGGkMKpyTHvOj2KHv4r9AtOO_WM3zKmgQqHz6NlorWIumxFYQQytDkg9IG3fVEIQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
ترکیب دوتیم پاریس و آرسنال برای فیناللل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/90476" target="_blank">📅 18:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90475">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
❌
🇪🇺
با اعلام دبیرکل فدراسیون فوتبال، لیگ‌برتر رسما به پایان رسید و نمایندگان ایران در آسیا مطابق جدول فعلی معرفی خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/90475" target="_blank">📅 17:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90474">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoL2CRZ3rUshR8tz3_S7LtP2Y0-e_P3MGeqUBoKZXk49br7EsLCGEBCUOIHWsbiwUUIq1frterAXqz8IUBTeTgXh0hG69L0DZlBO6yr7uurFZthyKz2kjNLa6BBq-I0FxtwYPMbmqwtS7ympFo6Mok99D71HO7cfvEmKtv9JPeK9Le73TGXiQVhCkyOoS-qycUJm9glMXjkV3IxwUVDc07GMciMWZWPzy1Nc-kux96LgOUUcuKyrjTA32irdOlTf8i5FxBPV5_GHIpJnBEJeIvPLZBv66_BcPMQ5kplb980H4F9lUJ807VFfu1O-THIg78Cks6P04HEcJrTFhVHNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتک
#FreeJulian
ترند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/Futball180TV/90474" target="_blank">📅 17:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90473">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asDTblSDWPF7zKnbt4HIcYzvzAghUJiRcwbBZBtks4V6beg2XCdftEEvMNmwIo5u2LgeVGKD8JrZ4W7QqaQqjzKAS9Jt3AL_Mez-U7GWXjW_OCzVAd_HoLpbrAtWgLaqU-AaeJ4JVhdw4Z32VQ3OjbTl8nSQkKyR9WfrRobVpVZZw-2zVsRpFmJ3xkUnt5sSnMM4fN641rZD66cSSufvGkuoHX0H-XJ9Pkb7EnEgYESQWai0aazk4YTEAp80mfLZi0ItN_T96HvV5S7vgtrQyjNFePuwAmoBl8ncfMnr15QC9ulHUe_pZwuzllkdZAN_FFDxhmofBnFIXf1xC-8GfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
کوپه :
بارسلونا درحال مذاکره برای خرید گواردیول است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/Futball180TV/90473" target="_blank">📅 17:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90472">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a77e89da.mp4?token=plELs9vaWvZFyadNz0IU4RyWOSON_jRk1_tLanagD5O3eav86IFieI0IimDSebKjpdHGG-YyddLXggwzE8vUDzbGWMIn1bdQHbl6cQDnKRQ6yDf8QjyKmpZ_oGVEVjgddAYHtvFBb2aFvgJG-kvo9PifhArLRWdPJp0W6QhZMatdpFfsI6cwRBslC5DDTtCOTttfrmtH86ByoT6Mn2SCwMAaaH39AWmcTUba_uv5UyB7fvSNmbtjQm-oQWH9uNo2tBryXquk4X2Pg1-luXMlOFKG2GF6cmtpVEiECzu8U5ltvAmNC3v-7inrdDjYBTWZ1xPiyXirmUXsXGxjI_KqhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a77e89da.mp4?token=plELs9vaWvZFyadNz0IU4RyWOSON_jRk1_tLanagD5O3eav86IFieI0IimDSebKjpdHGG-YyddLXggwzE8vUDzbGWMIn1bdQHbl6cQDnKRQ6yDf8QjyKmpZ_oGVEVjgddAYHtvFBb2aFvgJG-kvo9PifhArLRWdPJp0W6QhZMatdpFfsI6cwRBslC5DDTtCOTttfrmtH86ByoT6Mn2SCwMAaaH39AWmcTUba_uv5UyB7fvSNmbtjQm-oQWH9uNo2tBryXquk4X2Pg1-luXMlOFKG2GF6cmtpVEiECzu8U5ltvAmNC3v-7inrdDjYBTWZ1xPiyXirmUXsXGxjI_KqhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای اینکه بدونید دعوای بارسلونا و اتلتیکو سر آلوارز دقیقا بخاطر چیه فقط این ویدیو رو ببینید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90472" target="_blank">📅 16:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90471">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI8VD3qEXRw2c-NGV50fnpQsE8ixjEIN9uEpn2jPtaDLb5jUMeSlchM07UcP7hDYa8W4PNBkYyjUOToC554vKHY9mIT0dV8Uap1jAKpfaN6b7FiMY9zzk2O-moWsyI-YHIp5HqgQm5crJGlPIZ-nIyGMdyvwcHV5K3EwEBn22-bsu3pX1J65waHz8JzthLXA8uZ2vGOMO2H-An7W50tqN3MwhuhYWGoPtdtTRV9yeqrW33R-AIJI-0viXh-2-wklT4w1He3GZayrI821C-R2rtqb3Oq-qGCqrwUkz6jb5amYpFq89QMOPLctBxIhSnB1xAzsZCg3JnTy6-vf0lkhWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی افتخارات ملی لیونل‌مسی در آرژانتین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/90471" target="_blank">📅 16:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90470">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c775485a.mp4?token=Kdx7CnSapr_j2q4qzM4cBmk8_xt1DF9cYEhUz9JuyL5fa75P6caCn9CAi5F6nZNd3Dp616GEUlv0iQXgiVpGU6rsiKs1Dl08jsOKyTMJQ11l6lH9xmHzd1wpUdYdtXSQ0EYuAQPKcoFM3Imr8niv5xMzvrm6UbYT3gbiDkIyZLWteeZAGCvXZIoOtu5-8TdKDixfspGDAMdSKih68WJotGGfD5av8HwxHnh1DOGrPgkA7trr7XqTZhrraimFCSAAddcnWve1vVugSb55UzNLhCin4hQae2NAVVQvFYRJm5EauEB57_NvkiT_Ezx65Jkv3M2zIfMtG3Z0iuOESb8zFoXg-MzuB1Xvyz3_L_4e72vVrCOPLOay9vSVzF8vxB_8WNCxkeWQhSZ80NGpBUP8VaEoRuoYK60cpYKl5bCmdUD4GaBFCoOh4UNvH6KAm6oRcMsKQhQsKZZ9J40cjfbrZZLWvMaO7bvJ2fzsGDy-z56sBA26sD1JLZl59JYrxECcjIgGrFgW3I7tFgzcntjWlZFzIcxwNd_T_9s4bCic5Ds3wLp5t68sKJyts1OafHG1ty5yza6QD9zjWZJCN6ARe82woI9NBVBeSLaJkHkPIteqG74-PgVDhcbpRNhlt0sLUBVhH3AALZ_4kCoH6w1yCWopN5ngZzKPgBr_lcCsgjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c775485a.mp4?token=Kdx7CnSapr_j2q4qzM4cBmk8_xt1DF9cYEhUz9JuyL5fa75P6caCn9CAi5F6nZNd3Dp616GEUlv0iQXgiVpGU6rsiKs1Dl08jsOKyTMJQ11l6lH9xmHzd1wpUdYdtXSQ0EYuAQPKcoFM3Imr8niv5xMzvrm6UbYT3gbiDkIyZLWteeZAGCvXZIoOtu5-8TdKDixfspGDAMdSKih68WJotGGfD5av8HwxHnh1DOGrPgkA7trr7XqTZhrraimFCSAAddcnWve1vVugSb55UzNLhCin4hQae2NAVVQvFYRJm5EauEB57_NvkiT_Ezx65Jkv3M2zIfMtG3Z0iuOESb8zFoXg-MzuB1Xvyz3_L_4e72vVrCOPLOay9vSVzF8vxB_8WNCxkeWQhSZ80NGpBUP8VaEoRuoYK60cpYKl5bCmdUD4GaBFCoOh4UNvH6KAm6oRcMsKQhQsKZZ9J40cjfbrZZLWvMaO7bvJ2fzsGDy-z56sBA26sD1JLZl59JYrxECcjIgGrFgW3I7tFgzcntjWlZFzIcxwNd_T_9s4bCic5Ds3wLp5t68sKJyts1OafHG1ty5yza6QD9zjWZJCN6ARe82woI9NBVBeSLaJkHkPIteqG74-PgVDhcbpRNhlt0sLUBVhH3AALZ_4kCoH6w1yCWopN5ngZzKPgBr_lcCsgjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر پورحیدری: روز عروسی من و منصور، داریوش زندان بود، ستار برای ما خواند!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/Futball180TV/90470" target="_blank">📅 16:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90469">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09651a8d65.mp4?token=aubhYiLg3GAsugDEM2KD8kobaGyNQgeesu1hZWg1cqi6C6CXBihtubZ8d3-E1CCr5ixhQQnT6S0-UncRFUmvpfa4lwB-vct_b483fr7nhetUqWEQ-dj-uDcDC2e5ejGMtDYV-oOp90RaDb4g4-kGYkpUy0BUO9MWQQPTpuygqVc5R2gPo5jjmZE1sez7NTBPZDd6bSG71156CtKEPQdnmIF-KIBVqrWhZJn3Kv5B9s7h9SD-fZ-k4qYgN_hKTS95sg_4ADGGs34Mkygj76ppXRtu6XUtgWtMbL8S3WWLMpy13G4lyodG_e4OYAkvtxc7CLEwntiWa_TCRTo5WGqKrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09651a8d65.mp4?token=aubhYiLg3GAsugDEM2KD8kobaGyNQgeesu1hZWg1cqi6C6CXBihtubZ8d3-E1CCr5ixhQQnT6S0-UncRFUmvpfa4lwB-vct_b483fr7nhetUqWEQ-dj-uDcDC2e5ejGMtDYV-oOp90RaDb4g4-kGYkpUy0BUO9MWQQPTpuygqVc5R2gPo5jjmZE1sez7NTBPZDd6bSG71156CtKEPQdnmIF-KIBVqrWhZJn3Kv5B9s7h9SD-fZ-k4qYgN_hKTS95sg_4ADGGs34Mkygj76ppXRtu6XUtgWtMbL8S3WWLMpy13G4lyodG_e4OYAkvtxc7CLEwntiWa_TCRTo5WGqKrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
و تا ساعاتی دیگر، فینال جذاب و نفس‌گیر لیگ‌قهرمانان اروپا به میزبانی مجارستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/Futball180TV/90469" target="_blank">📅 15:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90468">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بهترین‌گل‌های فصل‌گذشته پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90468" target="_blank">📅 15:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90467">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/90467" target="_blank">📅 14:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90466">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9u-oHvSBybpNi3YxzZaeo2l_qcnhWEs8C3rMXYYggEgtUWTuiBKthKNM8lHKiDal45UKVhemwAbdJxcONKA5Z0f0qSlpXr1taLx_OvM62LInBfIaUTA77YV8M8x_6uxIiHIEj5hlyngHuW1Gxn12H_rhPBYvDtnJA4DjXutTK8vrqGTee65InEr-Z082tHiHCoRgsrGuLfmogVqkEktX-2wb1tkQO9kOb4GTWUiTuYRBBXp98BhV7aU4Ls_2J5C5aG8XmnqmdoeEM2HOEztqq26yxkrKcZSD_JN1O8tQVfZQaL9miAHdOIjI98VayvcYlLJ9UfX-NUYU1v45k0tvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90466" target="_blank">📅 14:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90465">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdZJV-Iax6QFq8e-gIS4R7r5k53g945Bc_AMrIxraQhobCX_8HMBr-pmshHf_XeplQNogpw329O7-FvbDeOoVHB7nxiPLFQGuiXJB0Qv0fecxkBDh9IowGAoruTIvO5MyqNAykufXzT_AyneO_nYyaKC_0fdKLMLKwXhtTBizdY_JSKLZ2iaZ9ptAW5FfhiSpnCKcmmuCvCz_Dvabo40XetPbHSBmf-IUfNTNsVsgsN09EJbQ4jDLi_0VfINja2yM4T_2YtN36-FxhuWGCgAx2Vdof-VqzEJgjsetG75DsVooU-iggQNi2lRSI1otpqGMKPteg_2Cl4j7iOAxC8MkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/Futball180TV/90465" target="_blank">📅 14:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90463">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gf-_rVsdndyOpJhIckgn8R1Mtb_hBfhN8FCATzlrkym0IMzn687P-1RvWuN6SAZ1lXiSkuoLzyCjRnryA3A4fK5N6Jmwpb7S_vFjfb99sB-OJGL8rXJNtMqTCARcLJqM1drc3L7Apf65v3PZT6QQ7Wlt2dM42GuN67gE-QEfg1Mv6efacqlKnm3lELwqgDf4nLQ6gVIhcb51VCYfNWod5AX4f0RW0veytcHZIFo9mirAtaBvQ9Sexi6PS84wI5V_zs8HCm4_PJRXGlSsNil1RdiVNNvXIocvg-5fWGbnYTVKXybDlkIZQkDlsVwO_lJHtG4jp4NjgE32NdK9QTJa2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIud0upmEJDq7aG7zZU4DqwoFOD_DyR5Ri_J9hq-dPfKiTCmVhAE6QmAzmBGax0fh0DekIISFuNzmi0yHSwEF6wc7CNrPQKRhwLTfQvWQLOn234N8QsT3tBWVuQq_HalD3UbJ-vxb1r79v8khYJL3jaMCGB_d_cqgLXuBL_-qF7ztGYxaglWQeUFvmnC-kiCnjAb458Uju06sxSsxxWckgpVkKfTjaIHG-VSlVqEfXFcDFLADfdbVVe8EnB98f-ODQwwBmL-96HecZXC6B7NsnZFxFLRyRLdr-UR2guxQ3a7sWEU94I52SqvMyB9RLZf8zsrKlBtNaF5ffd1o9oGFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
ترکیب احتمالی پاری‌سن‌ژرمن و آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90463" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90462">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ec9fa176.mp4?token=g78Z4xcgjeldb7G0PD8yaBjQOtrOgZqyRhZ0lsPsoS_8kAFKSWQyE6Gmxi_7P6f6bR9DvXL4YuIGlvhVXyzrt5BJ6-36MT9rhfVXlQL2eTGoD68QmHx2u8VFK7kIj5PMKcJFvK9R3BqLpIOAlywsavlWsFWbI4H9o8mpyx7fHraGtf4yFSWcMIZS2FagsqEYSEWHxZ7YcNTI_G4PAB8JZDIXJi9KBNW3z02NngIGxJOrcupdTKfKrAt1mj0NisBQO1jL-PPxYzdDfrE1YCXAEtZxoXBDLGrvJIMUPJ2Xyx-yndDNEUY7YzmcR3qrKm_7GFkdRSQDfOCRgGx7-EQfuY4Cs-stqBO3-nHhobRtYP62uxN7YsedrJx497sDcR-_h9p0RKIPMBDIrNgF-LNoqhHubo7GDcaql7a3Livaw0_x89CGDIa1W-0EunwlLsAKLPLjHD69hO4k-X6g-GhBuSXzJ8tXn6ekH_9xGrc2iPiFeSFEQ4uDefb_kp81iJ0nT42Vw2PG4US6D1FWsMKiQzOWNAzKgwNlkYoD-Lnl4FC5KDjq-4P1ZnCEfZSvUIJXDTeCyYQNNE4DX6oHY92VuRJ4ijRUiBlNB2qXVy6bT_1nzqhk9RF-UIaMc_fH-LepmlPymZG0utCD2_7mKnSDay7I7My-wexvV0PNUtzF0cI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ec9fa176.mp4?token=g78Z4xcgjeldb7G0PD8yaBjQOtrOgZqyRhZ0lsPsoS_8kAFKSWQyE6Gmxi_7P6f6bR9DvXL4YuIGlvhVXyzrt5BJ6-36MT9rhfVXlQL2eTGoD68QmHx2u8VFK7kIj5PMKcJFvK9R3BqLpIOAlywsavlWsFWbI4H9o8mpyx7fHraGtf4yFSWcMIZS2FagsqEYSEWHxZ7YcNTI_G4PAB8JZDIXJi9KBNW3z02NngIGxJOrcupdTKfKrAt1mj0NisBQO1jL-PPxYzdDfrE1YCXAEtZxoXBDLGrvJIMUPJ2Xyx-yndDNEUY7YzmcR3qrKm_7GFkdRSQDfOCRgGx7-EQfuY4Cs-stqBO3-nHhobRtYP62uxN7YsedrJx497sDcR-_h9p0RKIPMBDIrNgF-LNoqhHubo7GDcaql7a3Livaw0_x89CGDIa1W-0EunwlLsAKLPLjHD69hO4k-X6g-GhBuSXzJ8tXn6ekH_9xGrc2iPiFeSFEQ4uDefb_kp81iJ0nT42Vw2PG4US6D1FWsMKiQzOWNAzKgwNlkYoD-Lnl4FC5KDjq-4P1ZnCEfZSvUIJXDTeCyYQNNE4DX6oHY92VuRJ4ijRUiBlNB2qXVy6bT_1nzqhk9RF-UIaMc_fH-LepmlPymZG0utCD2_7mKnSDay7I7My-wexvV0PNUtzF0cI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
به چالش كشيدن اردلان آشتيانى از حميد استيلى تا مچ پايى كه در دوران فوتبالش شكست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/Futball180TV/90462" target="_blank">📅 14:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90461">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xduqks8hYdGuONE7vanm1gB0wZCD2iJ1TVq-gTxuu0h9FNf-qCvl3T2Miu09OSFdaO4aqAmh4AAbUDaS9JGej8nMI9epHkdCT5UuHwW6XKAA-N8U2T_FGhythyrotByW3EN2tkfsDS-DmdDfbo-JXdW7WOo5dOQ5e_XWlFWZo0k0iMY5XI6v0OeAzeunCIiBjZDx95nr2JvXeUPvMwf7CprhB67FMXOBSLq14x-9ChqzRWLTBGPuTBdT2XE7cQpKf-5fZBom6G-oBEc7Ubsm4UzG93BjFYwVtFQuIUQBIbX6mm9oydRLAWNjurenhjb7hOjBHvY8ow4RfONzTQIuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
توییت جدید باشگاه کادیز اسپانیا
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90461" target="_blank">📅 14:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90460">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBl7YZDPYO7VKBw_NTF60Gj9eK_BctSBNOX-pShZBcPHrlstknAmkFWV8ABNgmTbMSYY0e3g7DqlJ7e1KA54d0IHhTxfY-bM707FlK15AUA1RnM7defxuyqQZ9lZZ82J9eq6ehJ5JHQ10mI7RIce-hoYKT-UO8Dh_o7mIHW_WwnvTEKQWddchDgpz8-WKmzgjQCodR6s3zDZerXJVgSJauBS0F7bmXzbxJ7_8wMECrX_WyIGjRk-eOyXWSjfgQqLyKlI51ACFcw8UPiJHTYPwFE5scSe2uEeZrIh-cPheI_kzgG-tQprlzCRzhj5QRHIc1bf2gPmc-Ez2UkXfirUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد فوق‌العاده داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان اروپا؛ رایا در صورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90460" target="_blank">📅 14:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90459">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWAgBzOjFLer2E2oNbv8xcEZmgGL-4GN5JIcBfnbWxxhyJx5NeySOi9WDmzz3ispkuWUzpFqC35X_AUhSvM7VQabOiwcI51h7XuCnk0-bJ7tY0s8VGuUyykRv4f-HG_w5Sr1OB-b28m8imIwcNzkBcMvyxaQtb9agt40GvHyWvATC3hvifbxjviLt16h5hWZNVc81Eh95bUu_lu7T3Ayh7OaawrBX1rNvSaIQykSMCjMxiWkRiBNUyBavQw_ZzFr3O60zTRxWFKIQE0cawDMouC9q4QpcCbTHF9sLudtV0hKKv4Z5OQfBl7ExlJmD49zsYMseG4r6EuS_y6Xl8mrgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇪🇸
آخرین شایعات نقل‌وانتقالات بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90459" target="_blank">📅 13:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90458">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🔵
با حکم دادگاه تجدیدنظر، شکایت شرکت امین‌سیمای کیش از باشگاه استقلال برای دریافت غرامت ۳۸۰ میلیارد تومانی مردود و آبی‌ها تبرئه شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90458" target="_blank">📅 13:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90457">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
⚽️
❌
🔵
#اختصاصی_فوتبال‌180
؛ فرهاد مجیدی سرمربی سابق استقلال بدلیل موضع‌گیری در اعتراضات دی‌ماه، شرایط حضور در لیگ‌برتر و بازگشت به نیمکت تیم‌سابقش را ندارد و شایعات مطرح‌شده پیرامون حضور وی در فصل‌آینده کذب‌محض است
❌
درخصوص نیمکت‌استقلال طی روزهای آتی اخبار دقیق و کاملی ارائه خواهیم داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90457" target="_blank">📅 13:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90456">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKPR2WaOeuua7rhzA1cJ6-WSOExg3Shosexf1ffzuq4irnizyG43L_RcBR8IgHPp_s-BKptpmKwYVpgMep5wJmb8-3qI59G8grzBrxajmE_iRoIOFqS6EWHRlk1raeRn4TkV9Inv375b2a3mBrjIsOpRAQ-mRgq3kwrYLhW70rcd9SKsFiduAvGjdWhaNih6rQn1l-1Vm2CwTFRBEpWzIi2UVAsS3B5aBRyJXawxxfaEzIfbPCbTflfOHAcZqpqZ1tt96C110Q-YU-7ivOM2qLoC_WrQG7l8SAASGAIamXdPhO_IxLrWUOc5MOFYZMrf6v0m9Fqyqn23X19pACV9Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید چلسی خواستار جذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن را غیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90456" target="_blank">📅 13:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90455">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_88ad1M5CYpm3Ydj-Fvh6lHhlz2gkT1UHncGAxG_a_BoGBf3wks7xmcoGdh8guVEKWMYSWzjCMnGb31t2FniatwRK4cOy73UHG5lp86EuctRExrFPFsUynp8-5o22_ww-6LE0ZZP3gwzVUEfDiMy8GHr8MpPuAtgbMHYI34MarKQqkJF8TgKJRVfu5PjMf3S0l0oWxqQGXhBco2Cfph_Y5OkdMd3K1rrlHPdh-BFEyTONwfmY9Hmc6VJQbanJqvySsmAVOCZufYDa2tsrPr3B0tcGXe6VDn27X9VWdWW-W7VmTs2mpOYDvkJkVgJG0CGcohDwMA5lC0hn1Qqg4xyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
|به گزارش منابع اسپانیا، باشگاه بارسلونا در صورت جدایی ژولزکونده به سراغ جذب کوکوریا مدافع تیم‌فوتبال چلسی خواهد رفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90455" target="_blank">📅 13:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90454">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLiGCmKAUrW8ghfB6yXjRp9ZzDh2j64_2ZXmVBSHqwm1DaLor54wfoZAWkD6MI_D8Qyzy1TQ9Y-BhzVeMTZoPvIwQHXuLL3bk3EXf8OhxxoD2wrjXFWwhQNnb-Haxq2WixEpmZgHFWHbcLei_jUE8yVCW_Ixdtxvb9fGjphseUwrawFg56jr0w8KlOJaIsjch0VvX_1_BGmF9-zLOoK_8rl3s_Cqhrx32fgGz9HUJu6VfpojlbOxkIEKCjQnKWQI_fBfI7rxDvXjC2J85aeZ9lMaoG9v51TtBz8QgmXXYpOCsYc4zh9h71Nkc2aJjREaHO5Wbspz7K1h5toBSFgVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد آردا گولر و لامین‌یامال در بازی‌های‌ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90454" target="_blank">📅 13:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90453">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VF427NYm7jaz3vj2G11i-kJ_YFCOc4j9Ksfi4sn3QuISEtfVhvV5Jb7J3dpeh6A6LF2i9BvXoOg22h5QyDuPOSXhk7l_5Wc8y3avYmZGwwAJEyAMUjN34CbY1yG1rLv7obYwd42QH2rfimGPvtlP8ueA-NsDHn6NE5wxLu0peXlHE2TkiFwpj4Rn3MkYvwa13a0r1ntfhbUG6P56Cn7Ctd7xzcbTC8MW0wIAYUxVukqGZZVbqD7O7aMm4Sa75yYwuoIYcQAnoldQcp7Fk24KDg3iQkE3K39AfvQyMkahWI5aLQCvGBTqdj5GzSlCBFkhya8d-TndYUI5O30dwVX0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ ژوزه مورینیو به سران رئال‌مادرید درخواست کرده که یک‌بازیکن بزرگ در خط دفاعی را جذب کنند. از کوناته فرانسوی تا گابریل ستاره برزیلی آرسنال، گزینه‌های اصلی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90453" target="_blank">📅 12:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90452">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2u92BW-dYUSaBR3dxwqxd7uuovIDsRdSTbXM4IjOhoUbi88LghRoHCBH_MTv4DFrRAWIDRrYMquzc7xLLU_vrCm_UBuCT3x820_CwIORSyI9GlJgIBbG9acaHdWeVzsWtAz0k-d7TTJNpJgF5gkSBBUd5JBCVItkjGxG5zdHoiLPRF8zAA83E6LDt43qJ0cs3doFkQDotdCdAowlV5uh2QfxSBUzp6DzYi0w0I0NX0EZ5DzpGRj8J4WgrKPCC1a5-nwtRRcdH1gtDOAma9mhPND7OCVST0x9LqczUeL1j0gJ2lQ8DcooxzrAjctIw5hXjNWqYLReWaDa_PVhNAJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد گوردون و رشفورد در فصل‌گذشته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90452" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90451">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90451" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
✅
🎁
کد هدیه 100 دلاری:
Sport100
🌀
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🥇
صرافی معتبر
🌐
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/Futball180TV/90451" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90450">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lKOPzAytD8c9JLc-Aep6TP1VpZy7ez1dao0whOmYTeZ1Nb2ALw3rp4_i0_uePbo_8gcxiAPoAY5aQfyOQe8y7doDBKtCpA9f3gg3o_VLGb3Q7DU5sJqjXJ3R8l0HhcpVUbsPo3Uc3DXhEE0q0bsS3vqglLpSNDg0rs1MQprKfptjWPD40SBiYFYz7Dr6qLz9k3MxsHdJS4jrSycZjYS14LmDtMnXCCMdf5XmcvIhRN2WLFyxmhdpM_VFQyORJYS2wLSR3WWOytBwAFcIzQI5KcqtiFGqTBmGEjxyi3Z8eHhSgNxyMVd4uKiVSq8Kvb5jor6qWQ6s5NgsW07s2IJL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
فینال لیگ قهرمانان اروپا
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
😍
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/Futball180TV/90450" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90449">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584cdcb707.mp4?token=iOBy4yW-bUtoeXlmI-Bt_913Q6p5ATZij-X-0puqORXwb9Dg0FA0XjjajYHBJiiBg4UTeVGdEzzChyQkzZ8s4fIYUPupz8biJ1-M3oGHSTL7aF4_M4y1IjOfYLBQcsSrDxOnMpnlptXQKKhyDMWZogEURR3y5G4Yp6N7CuwHHcSKtvyMCkABP2eN5B1cVlSuDCpnN-VXZRc_D35B52vgDNWECiNa3r7cxdbFJD64p408TT6G43XKCxsU8YR7YwCCfPQnISwC97M_M5ZX54OguWLHN_hm6F8OQoaYpbJzQ-agmvAoXSvIFV8PK18ytVuiFkWsWh1wisO_5t5rNidrEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584cdcb707.mp4?token=iOBy4yW-bUtoeXlmI-Bt_913Q6p5ATZij-X-0puqORXwb9Dg0FA0XjjajYHBJiiBg4UTeVGdEzzChyQkzZ8s4fIYUPupz8biJ1-M3oGHSTL7aF4_M4y1IjOfYLBQcsSrDxOnMpnlptXQKKhyDMWZogEURR3y5G4Yp6N7CuwHHcSKtvyMCkABP2eN5B1cVlSuDCpnN-VXZRc_D35B52vgDNWECiNa3r7cxdbFJD64p408TT6G43XKCxsU8YR7YwCCfPQnISwC97M_M5ZX54OguWLHN_hm6F8OQoaYpbJzQ-agmvAoXSvIFV8PK18ytVuiFkWsWh1wisO_5t5rNidrEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
🇪🇸
وقتی سال ۲۰۱۱ از خولیان آلوارز درباره رویاهاش پرسیدن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90449" target="_blank">📅 12:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90448">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/628ff40327.mp4?token=uv_dPpE_xGOEP6tKQsujPZtY1K8Mrm2gaXPHp-X06a-JfGTjUwEIgon7ZZrFGtmuJ_qIlgGasdES6yOqFfdJgv0IDQSqvoSUMj6RPQ1p1AWEnKMbWUXvKAvCA-Cunr80kACZzy0kaT-lfjmQ8Bd2FYbMG6HRKW6VG_TDccX4RYoaR-Q3Vp_AAYC5EYe5wwDw8mHceDuCN-xkW9zVC2Qi9j9RNaFSeHofzhB_cc4lvfRWfqiGsWVniIiCS-vXFWKvjX9PZR7gmi2tkwL0B1H1Re_ioLlf7_PSNKIo9BBSgJLvcRV831ZIUWjcrq_m9WvU5FbzP1qJD06ttsAWtJaXOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/628ff40327.mp4?token=uv_dPpE_xGOEP6tKQsujPZtY1K8Mrm2gaXPHp-X06a-JfGTjUwEIgon7ZZrFGtmuJ_qIlgGasdES6yOqFfdJgv0IDQSqvoSUMj6RPQ1p1AWEnKMbWUXvKAvCA-Cunr80kACZzy0kaT-lfjmQ8Bd2FYbMG6HRKW6VG_TDccX4RYoaR-Q3Vp_AAYC5EYe5wwDw8mHceDuCN-xkW9zVC2Qi9j9RNaFSeHofzhB_cc4lvfRWfqiGsWVniIiCS-vXFWKvjX9PZR7gmi2tkwL0B1H1Re_ioLlf7_PSNKIo9BBSgJLvcRV831ZIUWjcrq_m9WvU5FbzP1qJD06ttsAWtJaXOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مجسمه‌ لیونل مسی، با ارتفاع ۲۱ متر که در کلکته هند برپا شده، قرار است پایین آورده شود. این تصمیم پس از آن گرفته شد که مهندسان اعلام کردند این مجسمه در برابر وزش باد تکان می‌خورد و «به‌طور خطرناکی ناپایدار است.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90448" target="_blank">📅 11:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90447">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a196e55e.mp4?token=NRLaL76Z4zNsIzhKt8aSc7mAFv-yB-jBTSHbEH1txLi3LxIZVGNgDnIeJ6thpkWFeQlYGrR5d1GT8SC5HKUotRiO3kcPmmTkcf36l9h4f5OId3_v6c-CDUMzGlyO1gjm3JNs-kS2pjpdkRKfKLWyrk45lmqRqmyTEvTBpyA7BlWabNQf4XXbsF1RXVfNPD5ddpuUr7wrXq-1QzY6HhREpvJeO6ZODzXtlGkP3lvQi0Qz06Z0tQb9sJObmKSMD9FMUQ34xTH17gO5b5MscGcMAUagIt4JKTnIuhR9n3xkqbHOov6rYwvNvsETPobjxpJ7ZWzt0EpTBP9htHtYfGK5uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a196e55e.mp4?token=NRLaL76Z4zNsIzhKt8aSc7mAFv-yB-jBTSHbEH1txLi3LxIZVGNgDnIeJ6thpkWFeQlYGrR5d1GT8SC5HKUotRiO3kcPmmTkcf36l9h4f5OId3_v6c-CDUMzGlyO1gjm3JNs-kS2pjpdkRKfKLWyrk45lmqRqmyTEvTBpyA7BlWabNQf4XXbsF1RXVfNPD5ddpuUr7wrXq-1QzY6HhREpvJeO6ZODzXtlGkP3lvQi0Qz06Z0tQb9sJObmKSMD9FMUQ34xTH17gO5b5MscGcMAUagIt4JKTnIuhR9n3xkqbHOov6rYwvNvsETPobjxpJ7ZWzt0EpTBP9htHtYfGK5uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
آخرش کی برنده میشه؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90447" target="_blank">📅 11:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90446">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8501f73.mp4?token=AClgss0IeYzICpG1LbGWOQpjfLosIrmd_hc-HcZW-8p0tivnVa6m2sILyZQiJzEnhiACJMRxzoeLOID8aZy5E1PQ5FuDHT65B-RhBw5w9yJDMkT04N6zowJUdf35jguLI65oHkOy1GIVP2gRCbeTgknmBvXL5O3CFH-uV_1nRHXA8XhKd5ogsSV_IAjKuEfDLJ_61ssabnUxaJztzLIFm_FqpIR8IzL3K69OtFfdOTgo3pJVkW86q5Ke4ApuLPFN9eviEq3Gqm2jWla9Nht8YUUOWG4lgSmSy5_Xhzpn2LfhnyWTWA61OhpC26di7Nr1CYXYte83N_pPw1Hv-TWAsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8501f73.mp4?token=AClgss0IeYzICpG1LbGWOQpjfLosIrmd_hc-HcZW-8p0tivnVa6m2sILyZQiJzEnhiACJMRxzoeLOID8aZy5E1PQ5FuDHT65B-RhBw5w9yJDMkT04N6zowJUdf35jguLI65oHkOy1GIVP2gRCbeTgknmBvXL5O3CFH-uV_1nRHXA8XhKd5ogsSV_IAjKuEfDLJ_61ssabnUxaJztzLIFm_FqpIR8IzL3K69OtFfdOTgo3pJVkW86q5Ke4ApuLPFN9eviEq3Gqm2jWla9Nht8YUUOWG4lgSmSy5_Xhzpn2LfhnyWTWA61OhpC26di7Nr1CYXYte83N_pPw1Hv-TWAsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇿
مدافع نیوزلند رقیب ایران، در ۴۸ ساعت ۱.۵ میلیون فالوور گرفت!
یک اینفلوئنسر آرژانتینی پس از بررسی تمام تیم‌های جام جهانی ۲۰۲۶، "تیم پِین" مدافع نیوزیلند را بعنوان کم فالوورترین بازیکن جام معرفی کرد. اما حالا پس از چند روز، تعداد فالوورها این بازیکن نیوزیلندی از  ۴ هزار به ۱.۵ میلیون نفر رسیده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90446" target="_blank">📅 11:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90445">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6UVqdPvvWL589f9Ona_c5CR4otvIzVGThS-ps8MUucMYHFTI_9KdxQljodxmpIb1jmJUVwZR4jmcqPOs_oSezuJ9lB56R4KL2MVYbwhpiWeFkzVBY2ZGADU2Z8muIfbtXp0gFpA10mOaCBWMcc-1ELy7bqKwXbqHp3yjG-lEJEE0LMRohep8_zF77tad0Lixb5S9jnHt5nlRSxV5c2fnQa68IKRV3JMwDnnDwyqYoRyZvl6tG0Ow4AXyOCt0jxka9cztezIKilQA0wExTmGFYguoer6CXAprKp_nvy3mg-GG6gNL_zZP3gHKmECmFQj7dd082AwMiXg4sE-Rb2MYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کونده با پلی‌استیشن‌وان در اردوی تیم‌ملی فرانسه!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90445" target="_blank">📅 11:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90444">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
⭕️
کنکور سراسری ۱۴۰۵ در روزهای ۲۹ و ۳۰ مرداد برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90444" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90443">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeOhzwkiqHkiJwVkSzPKeGXKQz4B_G12aNnQU8eKqtpwmiS-DwFTcNwVbRQxScDy-ENxI3-0BmWAYDK5cEm7aP8KCsZ5hQktKwBCYWuDRv9hadY1hmJrl-gcRcXCkstVASqq8THj5I_Z0j96XnUfIOLHIPdo_HNi6TmmX30xr-PpCZfm5JeKhQACZKeqq9MMRj_mowRcavfV2lWcyfffGptb09qi0c5YK4fQw7JJnk-aIXDLLVPvAwPtpPTWsFhAKsVMh7jsLyjPJuk050niN__GuU8lGSztHGoziWclMkHPAiA-3rYS6Lpr3gmJdjB-7IYaW1SPtUjLvvmIBPyDuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🏆
باشگاه‌های
قهرمان UCL بدون شکست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90443" target="_blank">📅 10:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90442">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4bcf8f7c1.mp4?token=TzA5CcvFqpnCFIxq2Y-6gw8bzWq49t_hCJ4c7H6qyts-q0EEOcPlj2jQuJnzonqLVXMkQH0JaFqIHtq6JJiPXLFaB3jYHTljxlUZwh_HPnO74nlrrxOlG7KdrXubvr91Gi_AFnMP6dbFLBdyz6A8uF_H8TWPetx38u2hqOWrBZ3VYa9HHW2WHCfAowDVul0C42-JTmKzSlboOejW3MccNBDlA7GFBl5g0aMKYb-DIRCiMHwS6d3GaqwtzYj-1Xv7stuBkbURDoRHc1XoEWGDT-WYSlj9YF2TKx-Aw3fCGaBA0M4121js-Sih8PDfvuWKULnYutNyrp-Y8pslhcP3VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4bcf8f7c1.mp4?token=TzA5CcvFqpnCFIxq2Y-6gw8bzWq49t_hCJ4c7H6qyts-q0EEOcPlj2jQuJnzonqLVXMkQH0JaFqIHtq6JJiPXLFaB3jYHTljxlUZwh_HPnO74nlrrxOlG7KdrXubvr91Gi_AFnMP6dbFLBdyz6A8uF_H8TWPetx38u2hqOWrBZ3VYa9HHW2WHCfAowDVul0C42-JTmKzSlboOejW3MccNBDlA7GFBl5g0aMKYb-DIRCiMHwS6d3GaqwtzYj-1Xv7stuBkbURDoRHc1XoEWGDT-WYSlj9YF2TKx-Aw3fCGaBA0M4121js-Sih8PDfvuWKULnYutNyrp-Y8pslhcP3VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
اردلان‌آشتیانی کارشناس فوتبال: سن و سال تيم ملى خيلى بالاست و ريكاورى سخته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90442" target="_blank">📅 10:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90441">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCiWZhnuFIzbIJ329fCU-jAXkv03YDrXXnUzGrIDkapxa3o_PkG48FGqPAW5DqNYGlQff-FUN140HUBLW9WDl4oIs-HLVHNi-_BfTl6Cmz9fAoSU4_CrWDiYHJ317mNW8_hwjYInsn2RhFSEjy2lfnX-0ye6WSnOHNnV_AymIkKocQCONuiQrl1BPzi8q8sZmzw_tRxqF9WlEm_C7XWNcL5j3usiI8yvtq5ElESeChS5dfZ8wOSREhytXl_4mTkF9KO-oQOyXJ1rjwMxWLcZqlN0mPbpC7ChynhJb6UCjUUwnLDNm-B4h6I5bY8IrLkCbuuxMyfteiiUxCnwsoUNmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90441" target="_blank">📅 10:07 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90440">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6df1df4a.mp4?token=V2gjLomdtQRkSOWMCguixZaw9Q3t4g04EhnmyZoFJE5Xuc8tACCIDh5Npp2DIwoD6ktx_aVbdejA_uLIYcxPjHVaCeuZvg2a0OTGJZaQR_caCwIZtRIOXK0dSQJPfNOgjN5aZCjhZN_BBg0BOTEau4SnCZAGAaJeTJGRx08ijF5HqoO9gio3aU9PWJ2Zw-4qS5r-thQ039Pb-tzI2EAli_taEsVT3W9dgAEUMeGi_ywHNWDkCFGFPxAOoMjxENfrg8QtJAfuhk59C6xaF1RN3Rn0iUqb3gx1KrKwv_uoaloZpDnhmEomcW8xuU3y8UDifeKo3U944Br-vDOf7lJDVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6df1df4a.mp4?token=V2gjLomdtQRkSOWMCguixZaw9Q3t4g04EhnmyZoFJE5Xuc8tACCIDh5Npp2DIwoD6ktx_aVbdejA_uLIYcxPjHVaCeuZvg2a0OTGJZaQR_caCwIZtRIOXK0dSQJPfNOgjN5aZCjhZN_BBg0BOTEau4SnCZAGAaJeTJGRx08ijF5HqoO9gio3aU9PWJ2Zw-4qS5r-thQ039Pb-tzI2EAli_taEsVT3W9dgAEUMeGi_ywHNWDkCFGFPxAOoMjxENfrg8QtJAfuhk59C6xaF1RN3Rn0iUqb3gx1KrKwv_uoaloZpDnhmEomcW8xuU3y8UDifeKo3U944Br-vDOf7lJDVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
تمرینات فوق‌تاکتیکی آرسنال برای فینال امشب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90440" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90439">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZrBf0rCjY5VzNYV_HGiuCYIjB75M2UMS9n5g4RLNbsd7AHQlgRc_TJp0ZjfgzZFblHi59VrE6nMNX3pSBIqNej6xRsurijaK_O4gFOF0E6JBQk9rBwgAHlUGz-PL4lh_xT44gY2iOe792AFEX22vSVCXZrADyOLNjXy6Oy2v4ocgZoZkJJb3LuGODFEw8KjJanoB_QdlQtdLoMZA7QwYqy5VmfPKN33DDkSdcP3ZxUA3_lOSPGbgo9W4cGSNmKLrE7pwuKcl8FbEMCFluPboezvFKRddqZG62r1xD8DZB21dbsT2HvHn9oNs2A7KpOXhzHMzH8oqx4dsM7y0HlRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار یامال و دمبله در فصل‌گذشته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90439" target="_blank">📅 09:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90438">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q92ECR4iaSUPPWR4lluBulAenxPERlCBObSTMVEhq9gI3B4z0sni2F4GzJ7HfwXDjxY0AntcAiyMAAJMOvYNzBB1TuZHaljrmimSXR4Wm3GgcYLMC115SX7sxKuhOlyRZKFt7_UsRy-IFdtRFFgjEg0owlbyyVxPUkgETR2u0LETR7Y70zNj3HoTkGn0CQl0e_FQYSjzNTSaaoyFeya35qRgJIiMCaiGa0Ju679NSgBqwkxDp0GplvqLeia0QxWTSOhQuZCCVYTNXA0Y2jyiwUUXSwTDO8jce8YMsO4G8I8Wt2exau_anK_E-8VtRM8e6ZqHFZDhb9jFLPv3yCWoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
آمار تقابل‌های دوران مربیگری فلیک‌و مورینیو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90438" target="_blank">📅 08:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90437">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDM1ntXuvx_VBB634udjtbo0TjuH6S1vsxuxq5G4vt1XqZLx66Wc1M9M0wJYUlTyFMoJv5MmuOB8usD6oqBqzu3SkzatKLrIWRDaL6X_rMFXk_JY-_PM6AMWHp46b1TXOB1goXrsaKLX4lYjLnO1KEWtRgUdQXYSKfS2fxMt4M0-n3U_8JQ3HWe-0BQyuhxbXwajO9veZyrA4b96DgyIJugAwnniZy7gvHOrNZwIne3s_LI2pGLjjr9zuId-MGarGDn9BLIXVU2G15oMf14OAfxZr47-668WDLvRAecwj1JNq4Zn0GxBMyu_3y5Qvloo-dIszBpqmjIQCwZWQlQq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار و عملکرد رافینیا در دوران فوتبالش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90437" target="_blank">📅 08:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90436">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90436" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90435">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbByunK0WOIxzVR7ZrKY-xuRcvPSARrD_tC2JTO2qP_7jCTi_3g5LYJvi9C5yEGO1Wf6OhYDZf472Emgg7ahoMoCcggqI3tSm3nsIOJPVYOLMZnDSOOsLvG6K2fu4_uiSCi1NUWoCgJj3WJcmxEItks_tDYmfFwyQHDY0vjjzEFeQu9eqk6lZ2UDMrU71WHdAnTEjMxP59Ymip0Z81XBj-845vr08mDDDulFpmyGWc4IQdoIcZHBiZ5e7HMsNjQVKJ6BkV0-AzgQeWecZctlUZ3apa8oJeVWCFH5_6O1KIUzshfzlisSM4sFml9MXGEgKg_X-__sxLRJEiJ9KXdQFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا
a8
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90435" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90434">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seDgo3KJmP3fokJpe6Ad1_jzs7oUFkbmMkILswz07ZKpd1Au6ulDulPQo6iGXz6-PNHf3SZ4GGMNXL1eF6LsmQ2AG2C4hidmxqb2JgJqx0RjDbpVqR3b3sMqxa7-MhGnEOkoYtJnhjN3GrPACoPrjzlbQzl0UzI1FOonI-3ohG_QIthb-XCsqkx-xKoS5NH5eLEj4brJsmAp2eoU_BY2Q0yt5pQ7tkYhp1KyzgQ2w4Hla4ndVPrQGV5uVyNXRJ2w3WyLoIOPLzQfIosdOVXxrMR4LYC_5_YqfnV-GIor6sOp1WTXfzDskSztI6YihhtmOAdmOAVwGGgYdZ0A5IoxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساپینتو با پافوس قبرس قهرمان جام حذفی شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90434" target="_blank">📅 00:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90433">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مجوز حرفه ای سپاهان صادر شد و فردا اعلام میشود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90433" target="_blank">📅 23:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90432">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avaJikbfUIWAVMYeRbGNOLu3qen5HC2drjANMh3hntPg2GqxDoI2b4H2GGZWOeipuko0MFzayXIb_JwM5kjNMttBXlJKvFCE1RbcXRwzBte-vFUb-jGXWM7bNFW3-JRjF7FNSxv16f36OiI8nI1UV7A9tcokQPekaLkQM93zrwaQaFUyjb_58pvZdfAMBjA8CNtcw9_ExuZ6mAGRizkANhBjTkAqM4HopegIQM3CRc-HRrkTzQVBHQPNQb2p8GwNN7n22-89sxTpdlXUKbTa-dG-HK-6buGxzE9xNNVok8-4qcvq1I1--rjDzCdT-Qtn8VX9KBs00tfMaKkHi4RDAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری و رسمی
گوردون با قرادادی تا سال ۲۰۳۱ به بارسلونا پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/90432" target="_blank">📅 22:50 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
