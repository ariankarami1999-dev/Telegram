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
<img src="https://cdn4.telesco.pe/file/RRTaupuqDauoWbi9cfF3SbNaVVYm6TlIOdDsjHS4YI-ONRs3ioEeO4ZAisRTHCMpM-JUZ-RClLNoqXFjNF2dGWXjpNc3KTaKBRFSfWggJFlfrgRy6dM81fbfcfeZXrs4PzKQC9qpJx5nF7Tlm8pKXBfW-wttNP_x8hSUcc9-QLxP9YQWT9i8Q7A0tVmXGhoZE1w67xDKGEA498wGbQ7jzHQ-Wr2lL2p3H7yQNk2wj4RRJrXUrVs6h-bR2zA8s7PHZHLP4GFz1LpzMmDNorTU9LsInhWSSsCwpElx-Sq56kZUe3yVie2fpcmKqlU4-jiXGpM2TpBC6Npmq5_RP51_TA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 01:44:06</div>
<hr>

<div class="tg-post" id="msg-673201">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXQudn77JdUEVpjbQZLUr64b1LCIzfAxQDe22_JDrRvQz6A8HiUJtPjqZpZ0-_73V2Kc7vLl69q6lysuzp-LWUxAi2bXJPIc4UVZw9v6xuxFYrAtTYMrwTYrItIDy4KqUtp8jHjFnL7OFnzKJhRyJppYAyesBXJY6bdo3x-LgskzxH2G7Ijt_Q_l98ZrAhL2MPT7Mek40kPlylb7_Acz8GcqgrFWfDbU1--WkE3Itk_XJ1y1cKCBJ9HPoCPrlbkVg1Vslpaqz_l0qG2kaefnsxUtL_B3_2mG8TJkjbu0aP8LQCVrYxM_GZ_jjkS3n9oy9LOsIosohIyqzIua6_MtOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پوستر فیفا برای قهرمانی اسپانیا در جام جهانی ۲
٠۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/akhbarefori/673201" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673200">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWSyhKc5qjDafQrBeEGsSL2droSrPX4O1Mdgy2Wwzo1bMjl7TQriOnBaRSpYrcyZxp5O_glBM61cJlM8WTPmoYHLaHHHb8a6eR2VlexQ3TW0j_-bGFV5tJp0SrVe-T_N0gWgJCAfovSYsi5kJnrHpS61eTABDlRA_12Pxxi5ibIsltafi71eLnbkDv1ma9Ksp3VPAcl6iARs11gbHWDWepummYUr1cGK8wLwUHhFYeNgdDaCpKImK-rLK0dxtJ3Tmp8TptxCPIC1fODAlJ4FW3dQDysGhWMHcu1AGi1tIZ9M2rul9nuKMzNgthbISFVlSCDEJPREFC44Dmuq4hmCPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ماتادورها قهرمان جام‌جهانی ۲۰۲۶ شدند
اسپانیا با شایستگی برای دومین‌بار قهرمان جام جهانی شد
🇦🇷
0️⃣
🏆
1️⃣
🇪🇸
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/673200" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673198">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5911d00df6.mp4?token=ZV46WbXrB0SqPVdGuTtjbLJ--YQkPcy1lPv3HWquden6cQpITnvHfG1I2Rz1_6G70-XUquzlaWwcc1WbC0D0gzn8f4YECvcZ1AKoa9uGx84NYf6PwLO4xDyRMxwZYHYMq09Sz3rBF0bcYkaN-nh1-OAWcf2dSf-Ui-rhNbUX1urp2peHGhpmG04rIVVgwUWHJvycZCcsDnlaUyxzywfV528NqZ-BvxOam6v4u3oQPDnp8O4HwF9ONfQZ9avjDbLBPZolzWoFbY4dTUAe7wAXBwoIvbXdtd7QBKUFQuR-BnzDUfGwYvGRRcLewcb5WT7xQIcAJWMf54TSoX0oKe3fUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5911d00df6.mp4?token=ZV46WbXrB0SqPVdGuTtjbLJ--YQkPcy1lPv3HWquden6cQpITnvHfG1I2Rz1_6G70-XUquzlaWwcc1WbC0D0gzn8f4YECvcZ1AKoa9uGx84NYf6PwLO4xDyRMxwZYHYMq09Sz3rBF0bcYkaN-nh1-OAWcf2dSf-Ui-rhNbUX1urp2peHGhpmG04rIVVgwUWHJvycZCcsDnlaUyxzywfV528NqZ-BvxOam6v4u3oQPDnp8O4HwF9ONfQZ9avjDbLBPZolzWoFbY4dTUAe7wAXBwoIvbXdtd7QBKUFQuR-BnzDUfGwYvGRRcLewcb5WT7xQIcAJWMf54TSoX0oKe3fUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسرت و افسوس مسی بعد از گل اسپانیا
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/673198" target="_blank">📅 01:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673197">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab996676b.mp4?token=mQ798ShwerRbLGeUxnBRVhCR2O2Q1cAtejAA8XEWY5CNNO8LGPRWGuOp_-hiWBUTJCcUaYjGS9HmdZU5v54GiHZgI0Y8R0y0_YwzCRePmWaMzDRMTrajRVn1YDrM6WI8jQ4JdIFdA7C6tHRCTN2l05lPFZ3P1ggXDuSPH1OajxYc5Lb-ru50zatiE_PXvLhZCLthfogVG4JIDGipdcz3M_KIsU6kPBQWYgXnaQlJeZXAYCqm2ln6IPRvv96pUocQ5Y8iqBXzqz8dwmDTGXWQL529g8oeyFkHKPF-mLKWdhsmBW662UkFYYFwHWqp9sZQGq4lcikAwnpfLy-ms4IQ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab996676b.mp4?token=mQ798ShwerRbLGeUxnBRVhCR2O2Q1cAtejAA8XEWY5CNNO8LGPRWGuOp_-hiWBUTJCcUaYjGS9HmdZU5v54GiHZgI0Y8R0y0_YwzCRePmWaMzDRMTrajRVn1YDrM6WI8jQ4JdIFdA7C6tHRCTN2l05lPFZ3P1ggXDuSPH1OajxYc5Lb-ru50zatiE_PXvLhZCLthfogVG4JIDGipdcz3M_KIsU6kPBQWYgXnaQlJeZXAYCqm2ln6IPRvv96pUocQ5Y8iqBXzqz8dwmDTGXWQL529g8oeyFkHKPF-mLKWdhsmBW662UkFYYFwHWqp9sZQGq4lcikAwnpfLy-ms4IQ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل اول اسپانیا به آرژانتین توسط فران تورس
🇦🇷
0️⃣
🏆
1️⃣
🇪🇸
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/673197" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673196">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
منابع عراقی: آژیرهای خطر در کنسولگری آمریکا در اربیل به‌صدا درآمد
/فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/673196" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673195">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELZR3rW-QVEY5YxSjhX4Wev10xVccOUlY_2x9SqXFhB4z9V-NmpgCOoGCLNPcGc_XyKBPn6qwo3VFqelpEaNUlPBGb1dK_TihKFMiZinLP4UHmgfQutvKcOtFvbNTIMEiELyLSGMa1wh73_M0xcNFXQSBuOfK0p_TfbBjA1aN5CKvW4sYt_Kq0nwqTmTUz2q8ToONMr08KHMlzX_2XtNmgAXKd_nCxnqWZaVDwEDxrLM6D4gKmPRWCy7qXutE_D5Xw1r9t98DBnOdEQshBwwzDTV9UM_xDVrw3gqUaic3y34nDKKoQeWz8SBsASk-gSteI76Z6Cy5nmanfJeCxO1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یزیدزاده
🔹
بامداد امروز، رژیم جنایتکار آمریکا، تأسیسات آب‌شیرین‌کن بونجی در شهرستان جاسک را مورد هدف حمله قرار داد. این حمله تنها یک زیرساخت را هدف نگرفت، بلکه جریان زندگی در ده‌ها روستا را نشانه رفت. با تخریب ایستگاه پمپاژ و ترانس برق این مجموعه، آب آشامیدنی حدود ۲۰ روستا با جمعیتی نزدیک به ۱۰ هزار نفر قطع شد و ساکنان منطقه با بحران تأمین آب روبه‌رو شدند. در گرمای طاقت‌فرسای تابستان، محروم شدن هزاران نفر از ابتدایی‌ترین نیاز زندگی، ابعاد انسانی این حادثه را پررنگ‌تر کرده است؛ رخدادی که علاوه بر خسارت به زیرساخت‌ها، زندگی روزمره مردم را نیز تحت تأثیر قرار داده است.
🔹
هشتصدوسیزدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/673195" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673194">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90474a79f.mp4?token=qX_yzyc1Qbc-bDusWAWfkscVXZE3ZbDm-qI16JwP3BhDnixedSH6JB4h0vikNmBvlfXsS-Ax7zW06r3uz6xPaouEcglkwb95hMVPdYdP11-DxBfFLRVnsNPYveogkcru5EaiCuYc9h_Za9lizZYsq9qOvp3VOGC90HHvrpUxLNPnJFJn_p9_g8sS7mnXZp-9EOFmBPFE6oVFxsvFDsqkxFD5Fft1TsTAXAjGBerfAO5U5n3Xpg17GOqYbH-O1UnzwoMhOWbv6huXnCxbLfLWnFsA6FqVO9m8dhVHLo0Vri1GUdPse32hKMvaKI-Vz29lTg6WqNdxFQPUg9i4138GeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90474a79f.mp4?token=qX_yzyc1Qbc-bDusWAWfkscVXZE3ZbDm-qI16JwP3BhDnixedSH6JB4h0vikNmBvlfXsS-Ax7zW06r3uz6xPaouEcglkwb95hMVPdYdP11-DxBfFLRVnsNPYveogkcru5EaiCuYc9h_Za9lizZYsq9qOvp3VOGC90HHvrpUxLNPnJFJn_p9_g8sS7mnXZp-9EOFmBPFE6oVFxsvFDsqkxFD5Fft1TsTAXAjGBerfAO5U5n3Xpg17GOqYbH-O1UnzwoMhOWbv6huXnCxbLfLWnFsA6FqVO9m8dhVHLo0Vri1GUdPse32hKMvaKI-Vz29lTg6WqNdxFQPUg9i4138GeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل اول اسپانیا به آرژانتین توسط فران تورس
🇦🇷
0️⃣
🏆
1️⃣
🇪🇸
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/673194" target="_blank">📅 01:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673191">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سازمان تروریستی سنتکام: بامداد امروز بقایای جسد ناشناسی را در محل حملهٔ موشکی ایران به اردن پیدا کردیم
🔹
در این حمله ۲ نیروهای نظامی آمریکا کشته‌ شدند و یک نفر مفقود شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/673191" target="_blank">📅 01:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673190">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nyd9Y1XFRc4l3UGE5LfnjFp_aaSnE5xft1zZ5aETjnC_CW_FWeEcyrVJXqJkE1VFIqLo__7WW8I03qC-HEn8ZtdFMs-L5UM_je0iYPzypKE8GeXpvJaFVIb98KiQM_fKq3o13BpVW1R0bTtlSJncqa_7W8SKaMgWotREdVQm3E_c6IphRXmOwAUS9raUXaz3Qb8UbvHJ2z8JqV61dHVTAAzYF1GWvU3eu5v76-NO4hyROm3mkO-LyMDuNDwi22hO_rqaJ2NxHLxmo7qTlhAPv24EbqCQNK3jKPFVfeqVPZF6K2PCwTyvT6uj11kU0wUn_FkE2lp9rw1Eex8TwKd9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عملکرد عجیب آرژانتین در ۹۰ دقیقه فینال جام جهانی ۲۰۲۶
🔹
حتی یک شوت هم به اسپانیا نزدند، حتی یک شوت در خارج چارچوب! هیچ موقعیت گلی هم ایجاد نکردند. هیچ!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/673190" target="_blank">📅 01:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673189">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/802f158a8c.mp4?token=HNmk3ZOuh2mbAOzBjvjIthQD6kxDiFpOLufHKTwMEH0lJMGD2FxlduUAkNhowBC_zPP4JjUsI0KGifJ5jwDrWH8_8IMAfTeH5RGdyhfPMYFBcRaLcquQKtWzAUcesAXzxP28Z5c1LFHuwBsVmu5VQ_44XNqh8dXzwxtU8pp6FQJCIOk5qzrKW9V1xoV9WJQGfktEP5giLdVAp9lDAjOWfOyi6Vb8t-LD3evH3yXnAFOstM6VGJt81S6fNjMGevsk1GKa4rGbf1JA4W-KyN2uygi7vmlXbFu4V9bb6yzaFtBLq_1Ej8TfDig6flI8XHw0ppW3Rn-q25JpZzcCmyLjyk7lihpwGzXSCwMC937_mva6k6bY7IeFkyQP5zI2mXdTQctDY2799xKwNykI8xqMr0sAzkuZq_94UuJC_7wqoOIaGHjgoM4UUVjPN-4_aVzmdLDeYyXrXoj_ketoVNjhE-EcXl2YzvaZprHVaWna77JPLzNj4phfEQGBdx5BQIBUaxOArd7-Clafr_EaAZAjmCM__2vRw1U2Ykc_OuORb-gVpkYVzEPXfnCCb_56rlCRpInG7iIVeEyFhvQiWpaHROefUDhWRPcupqohx6Pd0JHcpDZtv_nVGZrn33PeEucJFbl5EACDSiOceLPP8-v6ek4Zmp28HaJpJTFD6PCFeu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/802f158a8c.mp4?token=HNmk3ZOuh2mbAOzBjvjIthQD6kxDiFpOLufHKTwMEH0lJMGD2FxlduUAkNhowBC_zPP4JjUsI0KGifJ5jwDrWH8_8IMAfTeH5RGdyhfPMYFBcRaLcquQKtWzAUcesAXzxP28Z5c1LFHuwBsVmu5VQ_44XNqh8dXzwxtU8pp6FQJCIOk5qzrKW9V1xoV9WJQGfktEP5giLdVAp9lDAjOWfOyi6Vb8t-LD3evH3yXnAFOstM6VGJt81S6fNjMGevsk1GKa4rGbf1JA4W-KyN2uygi7vmlXbFu4V9bb6yzaFtBLq_1Ej8TfDig6flI8XHw0ppW3Rn-q25JpZzcCmyLjyk7lihpwGzXSCwMC937_mva6k6bY7IeFkyQP5zI2mXdTQctDY2799xKwNykI8xqMr0sAzkuZq_94UuJC_7wqoOIaGHjgoM4UUVjPN-4_aVzmdLDeYyXrXoj_ketoVNjhE-EcXl2YzvaZprHVaWna77JPLzNj4phfEQGBdx5BQIBUaxOArd7-Clafr_EaAZAjmCM__2vRw1U2Ykc_OuORb-gVpkYVzEPXfnCCb_56rlCRpInG7iIVeEyFhvQiWpaHROefUDhWRPcupqohx6Pd0JHcpDZtv_nVGZrn33PeEucJFbl5EACDSiOceLPP8-v6ek4Zmp28HaJpJTFD6PCFeu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به آرژانتین توسط ویلیامز که مردود شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/673189" target="_blank">📅 01:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673186">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fg9_EzhOd00HXaSpfLXMsMflhUicgPxLKeZJW-hjkUVdmyyHszBKcWZDKlOftqT9FCDjdO02Mriyl3cq1Xlu_Cc6hawSETBjEP_PH2MdDHV9ab_rYmlNl0AXY-Uj3iGHeyg9D8mx7XtHOiJTWBXJBhhJ7CvmDhyx-E8raqBHG2vqYV8sGguCV87XFbd6GgT1ZKY9zUo610t0RExe6XyVVB-taVuLrKMvlw9D1De0eShDU0xcFvrZtNZyW-_OQ-kxQQKvjhaQY-XV7cc7Sfwz0vhKzzLHW4c_kzDypmSl3Nvx8bQvNV1kZXmMscWj6g-7__s1m5m1GI-4j9e1A4qAng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2oRNEymNCr60BnCy5AP_3_wa5nmJFkiI1frknjV2tbxLRhutc_9WJl96U98hqG027WOb62euJIvLQ84dU1K_ZWBkr-MHmFRv1Mi7NOg2gvOsqcwSQamSwKnkqwCtM3hAihZcq3gnRUijlX34yRcne0RKyjDhPIQQIlukrSRVY3bCk5QNtxM0xsEgBcju9dpj94gURGunNVd_GB0Dr_QGdEgZc10ZdzOsSKLAXEpjuYCTUvpsMD7yYoDHSAC7_3rpj5deI8Opp9dFrifIDa_wM4EPbxsfnezl1HICEW4ILMxCb5cYgq0Jalb_brF5sipgWenEDE9atDtbBBByz0JyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e88f1b708c.mp4?token=caDvJMtcO27Kbn-cHiLcSMCDDhB9dIb41ir-yp-NeCwAKepxk55scQSg3bDfg-f1yLVjrxz3TZWjFtREWC4j5vpDQ3nnVtoxy0PcrlOMIpyJo4q-G1Wo63GeDpRXspr_HRuV6DiEZykHUSciGEx0yC5maM1bZcCDgPWGZnzDmp8woi8Y_5hDoplSRrAM_FKi711bshpgnGibR5UhHLZSfgo0UYvTPFLYxB3n7a7uxdIKsn3oemLOPhkZedUyB3j3C1_YIES4utI94NjhSCQsT3RJzVC3yIPxNnFE0XxbBmyckwWh4NTb86DhElu7173SpNPVcHfiAAYL-lHLdwGnkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e88f1b708c.mp4?token=caDvJMtcO27Kbn-cHiLcSMCDDhB9dIb41ir-yp-NeCwAKepxk55scQSg3bDfg-f1yLVjrxz3TZWjFtREWC4j5vpDQ3nnVtoxy0PcrlOMIpyJo4q-G1Wo63GeDpRXspr_HRuV6DiEZykHUSciGEx0yC5maM1bZcCDgPWGZnzDmp8woi8Y_5hDoplSRrAM_FKi711bshpgnGibR5UhHLZSfgo0UYvTPFLYxB3n7a7uxdIKsn3oemLOPhkZedUyB3j3C1_YIES4utI94NjhSCQsT3RJzVC3yIPxNnFE0XxbBmyckwWh4NTb86DhElu7173SpNPVcHfiAAYL-lHLdwGnkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویری دیگر از خوک زرد در قفس شیشه‌ای
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/673186" target="_blank">📅 01:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673185">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای شدید در اربیل در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/673185" target="_blank">📅 00:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673184">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
مقاومت اسلامی عراق: در صورت اصرار دشمن آمریکایی بر گسترش حملات خود به ایران، مستقیماً وارد نبرد خواهیم شد و با تمام قدرت و قاطعیت، تمامی منافع و پایگاه‌های آمریکا را در عراق و منطقه هدف قرار خواهیم داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/673184" target="_blank">📅 00:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673183">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-VkHbCSQs1EdgkH_fS2kRcFLmnuogD70W1osFczHkz5YxxpSVrWV-aeeSEucc7cHhQJrZzHn4MIdUk3S51e8iEed7dclVGQfXVwpZmgh94CAr0IaB4jR7KVU-NuUpklYx691LjrDPJpzFh4ZFB_DlQF1RSddaso5TNYNmdLjwKKXaKntX9tAZUpr--Wry_UDEjxon3tei4OYQNcZ_Yb1sZO2wCrGjNn0F61FLrVy_oRg1xp5YOm7IOA2GcRTccF2NGmI2Nv4fcMlHjPdHVJLOnBxXebJRP4tbpyjSgz_mr9ClHnw9Wq2vM-nCeqRrAJpyEDzw5Z_KpdE14iRaIs3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انزو اخراج شد/ آرژانتین ده نفره شد
🤩
🤩
🤩
🤩
🤩
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/673183" target="_blank">📅 00:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673181">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwzBD1OYm1nAkWpf_Cok-OHF7VG2-q3C4T4w-N59jEng8JbH7aXIShUFYkkEzv0xB1oh7hZEBXJ4lBwV5blT1xtpAn-BbHJAr9UN31jT-NK1D5Qz84KvhMh-vbcRxr8-8DaeT5i1gjvGdOkuZnf3e4NZVLxZOAHhUUM6y2UJomhutkQFaqe4rxk1YedtZngPyxSGq1Ik9sBO2yx2fUcTiKiId52nzghilB4rIMod0Uz4YsyH2-ePhBbDPJYrDUQx4AHYZza-_AaoZ1cQIjKC4vBGzE08mDu9DmilHEAINBy9fwr7wgKfMljiyEqE7q8Of40vWCRBhCbn6WJrqldlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انزو اخراج شد/ آرژانتین ده نفره شد
🤩
🤩
🤩
🤩
🤩
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/673181" target="_blank">📅 00:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673180">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای شدید در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/673180" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673179">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
شلیک موشک از نقاط مختلف کشور به سمت اهداف دشمن متخاصم آغاز شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/673179" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673178">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای شدید در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/673178" target="_blank">📅 00:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673177">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
منابع عربی: انفجارها پایگاه اشغالگران آمریکا در کویت را لرزاند
🔹
منابع خبری گزارش دادند که انفجارهایی پایگاه‌های اشغالگران آمریکایی در کویت را به لرزه درآورد که صدای آن در آن سوی مرزهای این کشور با عراق شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/673177" target="_blank">📅 00:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673176">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/673176" target="_blank">📅 00:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673175">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9b75580c.mp4?token=ZTOeT3WZxhrMNuFHofDDsRK4v7aeUTlDMg5xxXrd8fxQ5yRkUlFWuEZU3u0Rkh2g4eh5s9MEzxh-6ZjianNBTcAJrmCstx3a-TKATXXqRmnZzeuEx5nL4SS_GzV8613cWlva1KccTe272Q4rRL1JGpAJ9--4KkTuYCGjui41wCV-W7AWViEmdk77AVSadOB-l6hjUNaPzfrkF6h0A8gOSyRLG_z0X4ONwnG-xpGB6HPS9HN8YOPq3ZFh0rwG4F1MD9YDsqhW6xZyzhKy6rq-sf2i-YNj47jU8h83Mez0rduIATIvVb7p_AcuOG1Wj_ppt_LctK_tm-2N7TQl3D8u7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9b75580c.mp4?token=ZTOeT3WZxhrMNuFHofDDsRK4v7aeUTlDMg5xxXrd8fxQ5yRkUlFWuEZU3u0Rkh2g4eh5s9MEzxh-6ZjianNBTcAJrmCstx3a-TKATXXqRmnZzeuEx5nL4SS_GzV8613cWlva1KccTe272Q4rRL1JGpAJ9--4KkTuYCGjui41wCV-W7AWViEmdk77AVSadOB-l6hjUNaPzfrkF6h0A8gOSyRLG_z0X4ONwnG-xpGB6HPS9HN8YOPq3ZFh0rwG4F1MD9YDsqhW6xZyzhKy6rq-sf2i-YNj47jU8h83Mez0rduIATIvVb7p_AcuOG1Wj_ppt_LctK_tm-2N7TQl3D8u7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
وینچیچ داور مسابقه به طور تصادفی دکمه اسپری‌ خود را در حالیکه بازیکنان اسپانیا پشت او بودند؛ فشار داد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/673175" target="_blank">📅 00:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673172">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fn7m8bQIiGyRTF4u1VjcZ_tqITaJjmcQTj1NI0vvqkFwncTM_nlJy2OeM1aFnDqVkf2FzCD_hxLwpDtxixVMPKRheFkwZfj27xltVUEifDmPWxJ1w1rvc2yhDR-Bn9bix38_7IsWCQG89iITlWHTlqYXPDbT4RI3RQFvESICkBieJxRw46JnDxPNghYlHGe6uAor1qtLAPi6bl3tv7pkAZrHwYb06YsW_JW1i-ruz_7aXOzoIMg_VWLg0a7Nip13dwjIxqk9wNaROBBd90v0qERa5cmcRZma0eZsVZKsxJYTpEPrLaGgcKNdpN9pZL8806n7ZZuC2egQeNw7V43eFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_PgHEpLRk_ibJULpfjaHfCZXlCvgXGBdhzQIsrN98FFdIBOdDUHQyFUnvi-4UiUq2ZhYI8gPMQ3Ink7HxhKJridNcRbhPXEULtfAyYHhSUblus47LDhM_bRzIaF4IpJVw1KdjD_CQl25acmkPD-YjyK9Ttpkev2I-gNkdDAlj_mtPFjghVcJYLNr4Dn-TsWAbY-Yqownde0wH4Tavn78pTn5LuPcgqwbRjA8_EmXDJbAWlyJKOTr6NiSd2WFcPGwrgWm33K_E7U9Lp8eBIHJzyrikH-OhD5Rf1G6OwKaZBufNXTE2Yd8ai1lEyJYBOl7boBOrl5LzK7aDYxWsvEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fyowF4EMX43PSp3G-bKwS7-FyT45mbp-AHXNHCO3E8P4gw47n7z41HNTqjurYq-sDuPN9FCMaX5pukMT4PBE4n8bdd62qtBRD6TJznkH_VaGAlVsKpAqg6Aq_iYQtNRgfmT-wSXNTchkMMeCVPXMLOnWmBa2rxkeG0jnDZqIfcQ1GOFcf59zYo-QoUaNkvLvwtQt5SXEMCVu_Kuj8vtEynaG21i3OyrUU5gRCbQPe02xqLUFIJCgXB7qjU6oF14Su7IprSSBKPkif2Kj2WXs8MQGk_h8263lwEouwlJvtx5fgh72b9068FgoWVKxFk9-_2hyVtUo5ZdjwjC40AZVQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جایگاه ویژه در استادیوم با مبل و کلاه آفتابی و ویوی فوق‌العاده نزدیکه به زمین
🔹
قیمت: ۱ میلیون یورو ناقابل (تقریبا ۲۰۰ میلیارد تومن)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/673172" target="_blank">📅 00:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673171">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
واشنگتن‌پست مدعی شد آمریکا برای جنگ گسترده‌تر با ایران آماده می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/673171" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673170">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای شدید در اربیل در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/673170" target="_blank">📅 00:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673169">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaFlzJxElw-5FgC6biVIIB8kdsYTUyekpzv-Z8mh6ywJbkl7mALlqGBEEEdRPNu7pjLS4h0U9HAdB0DweNBcES0CE0jhWRBNc6JjScqYaZvWnu1iiL6tHPXdMzbUvQflhx4BBMB4tIl2JmBQhXVgRFsucKoFCghgg3IbTbO0x9ma7i-CQabOBW13HYs07Yi7wKooMrFZT3rDq3Xer6fJ3twOhOo46-vkHhFwJBPhI-EvdUyNyXwKhxOT_pmjWccCKG_3ZCexmjlsh-jfAD3Wxlb_yEipFU8dlpUoNGd7CrCBPPfUfO98NuKi_Z5gvK5bqLOB1U8i-k7yGgQA0RPR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارقام نجومی برای بلیط فینال
🔹
ارزونترین بلیط فینال: ۹۵۹۶ دلار (۱ میلیارد و ۸۳۵ میلیون تومن)
🔹
گرونترین بلیط فینال: ۴۹۳۸۴ دلار (۹ میلیارد و ۴۴۷ میلیون تومن)
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/673169" target="_blank">📅 00:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673168">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
منابع سوری از حمله توپخانه‌ای ارتش رژیم صهیونیستی به جنوب سوریه خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/673168" target="_blank">📅 00:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673167">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
معاون استاندار مرکزی: صدای انفجار لحظات پیش در اراک مربوط به اقدامات آفندی بوده و جای هیچ نگرانی نیست
#اخبار_مرکزی‌
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/673167" target="_blank">📅 00:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673166">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ac438237.mp4?token=PwKo-MK0NW_TSf-fbqybyTVo_TmSDafEpl-Wc8Vip1HULpgPU2Dy-IN4UkfM0gb1QjcQMp_g4Od9301QC9qvZW3vV7Iv-9RXPKtOKak_9_KcJTueAaYChnI_dWHvehowOhWBxNek_hRWndynlWIerzPyf66b4BkjYm9xv6Naw0Qrs3YXoq36NogMv17EG0Rhionyccy5a-EN_F-GGZoOCYUEJ-6M63H23Lk2OkpYAshGvcFsAy_3jwlueSPaRdRv4odeIJJbT59IhVUIZFQKZhq6w0QrjMY6mP3joEEN3kvWVeVPvwYwYDlqWCaDc70kBA3wRu8KW64r_i4eFl8uJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ac438237.mp4?token=PwKo-MK0NW_TSf-fbqybyTVo_TmSDafEpl-Wc8Vip1HULpgPU2Dy-IN4UkfM0gb1QjcQMp_g4Od9301QC9qvZW3vV7Iv-9RXPKtOKak_9_KcJTueAaYChnI_dWHvehowOhWBxNek_hRWndynlWIerzPyf66b4BkjYm9xv6Naw0Qrs3YXoq36NogMv17EG0Rhionyccy5a-EN_F-GGZoOCYUEJ-6M63H23Lk2OkpYAshGvcFsAy_3jwlueSPaRdRv4odeIJJbT59IhVUIZFQKZhq6w0QrjMY6mP3joEEN3kvWVeVPvwYwYDlqWCaDc70kBA3wRu8KW64r_i4eFl8uJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری عراقچی از ماجرای تماس یکی از کشورهای منطقه و تهدید ایران: ۴ صبح زنگ زد و گفت ساعت ۸ ما شما را می‌زنیم شما هم پاسخ ندهید
🔹
گفتم بزنید ما دیگر پایگاه آمریکایی در کشور شما را نمی‌زنیم خود شما را می‌زنیم
🔹
منطقه باورش نمی‌شد که ما آنها را بزنیم و آنها نتوانند حتی یکبار جواب دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/673166" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673165">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVzizbgYW8jZ4NeJSuIYPf_0H_TKQ8JGQS983SMYe39LHuN9MedcfmMl5jpS-m17eWHB3wZKsjXwAuX0CnVz4JYBpXTTp0vLmBc9OOpX9bO_DA9yEfWZua0C75-A2sKLTpaZhoR1qVymDrPQTC5cu_61v1USyNJQbmczJb2duY49rCrJ6ILg_gaqBity2ksOTm2uQc99gXjLyIRJfJiNaWZP91AUdOBhUNuaf-a-_rElogZSTyn-k8h9QehXgUosmdxe1lXC_C-eex5xgapCi8Mf4nSraueYPyvWQVQbe0J7_dFWd0a1FHFILeqT11aBsBRp4scpZLZAlyzQ34a2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/673165" target="_blank">📅 00:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673164">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a341f37b.mp4?token=su1Oyz5tuqxge2kyqLL5aBOkss_0XupkeBxz8L2Tg-gdzMW8cEcnXAi-LUZWkVec8w_sw9YVGJ64FIe23H96ch5AE2fOF4KuAGoufktpokcWgNQwKDu13U7TMQTOd54glRu7dZYdfFvSZg97Uqu8u92SG1hqHi7YczeVQ2G-VwH2Y7qy2kastnO3LynE_1Ad_DhyW6J9Qe02HXpSHS8Euzg70GVPPgTVW3HoDHtk7oarna1uv4fz5CfvttWfvpiM5pCrl8dDsZwYEZOopfHcitUxb7EHU2eUZ4a7P62n3vK0cLcZitnlYjUFfNR25aYJjY6oOnybw2qE2HtNymV2Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a341f37b.mp4?token=su1Oyz5tuqxge2kyqLL5aBOkss_0XupkeBxz8L2Tg-gdzMW8cEcnXAi-LUZWkVec8w_sw9YVGJ64FIe23H96ch5AE2fOF4KuAGoufktpokcWgNQwKDu13U7TMQTOd54glRu7dZYdfFvSZg97Uqu8u92SG1hqHi7YczeVQ2G-VwH2Y7qy2kastnO3LynE_1Ad_DhyW6J9Qe02HXpSHS8Euzg70GVPPgTVW3HoDHtk7oarna1uv4fz5CfvttWfvpiM5pCrl8dDsZwYEZOopfHcitUxb7EHU2eUZ4a7P62n3vK0cLcZitnlYjUFfNR25aYJjY6oOnybw2qE2HtNymV2Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای بیژن مرتضوی، موسیقی‌دان مازندرانی بین دو نیمه فینال
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/673164" target="_blank">📅 23:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673163">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39ab21c56.mp4?token=ccg--tpKZADsWAdAB3AGjFp_ANT-LcNKWMk0aV9t1OA4RCCTqm0FzqkA--ZEsst9pIbCmpUolc4xpOw4hohZrc3Yr9nKT-WLmj7qKLDSE_6CllukTPfsWC7A2cXMIGaXPtQzpgL5rVXGk_fXjBtSpueeBCTKGUr2DU0SYWuROfkALR7xbQ-1rcrlyNSDQ-0ydR7eloikmTw7RIQS63Y2Z7yG6lZSFOu0FI3WYG7cQ4jWI5o8Ce4IskCFjiHLyclucyAOuxXjdHKt5n461bfNjso_nlh0C0r30OSuBfwYr9E0tre6Xkqn66T6AOsamOPt6-jzs5wK4c7mDzc2ZZSD4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39ab21c56.mp4?token=ccg--tpKZADsWAdAB3AGjFp_ANT-LcNKWMk0aV9t1OA4RCCTqm0FzqkA--ZEsst9pIbCmpUolc4xpOw4hohZrc3Yr9nKT-WLmj7qKLDSE_6CllukTPfsWC7A2cXMIGaXPtQzpgL5rVXGk_fXjBtSpueeBCTKGUr2DU0SYWuROfkALR7xbQ-1rcrlyNSDQ-0ydR7eloikmTw7RIQS63Y2Z7yG6lZSFOu0FI3WYG7cQ4jWI5o8Ce4IskCFjiHLyclucyAOuxXjdHKt5n461bfNjso_nlh0C0r30OSuBfwYr9E0tre6Xkqn66T6AOsamOPt6-jzs5wK4c7mDzc2ZZSD4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی ۲۰۲۶؛ تدلاسو و دستیارش بین دو نیمه بخشی از برنامه اختتامیه را اجرا کردند
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/673163" target="_blank">📅 23:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673162">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYnQDZpEJx-EiclHOTw8PuPmLIKXtpVRpb5fHJnwZBli6e6ly_OcXYijj3R7Sw8Epa6lsnkv-VyJ7_lgo5QSLufpqXYhz4QY3vPlQa4T_t_UWO-QeiXZB71HJ58jZB56htsWzJbb91VMt0PjgCu8sYqrPVzU0_zmhJYDwPzaY0NDxKn9X01EIfZ10xISfQB3I7lHfBEcINVwjKN1sZoQFp1vlQbm5LgHNFxgYLXmmQ2Gd_ru26wqKSWR_uJa7IVSZC4Cjwd2dYHNVZA0lO_mKY-90nTF3Kbewf8KX8WVtaWopa8J_Unu0HXn1bOqwWHJkFfvNbiWxOwQcwvmviMU4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی زیبا از لحظه پایان اجرای بین‌ دونیمه بازی فینال جام‌جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/673162" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673161">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgd4rBKh-qki0MXoufYE-RESKi1JpqeFrTe_ioStudUHj5Lb99T5U8Qik8sgirCN0N7X_6_MDE9nzQSjlA9i4DlFmtgYka7wRNy17lWTP_h3WxFWS9Hv-9BEnvgRoN4skLOZ8BpSynUG0GgI7HSIBAf8TLUxbUUXfV4H8uMJy9eqzYPE9e1W3PJaWHL3TnxZznMtBEI-hfbdbyAEfSG3bpnsLwDOhkinlReGUgDY_cOSIMiKd1w6coLgFwaEnfs6P4h9NinFTMvpLnekW3lKu85PTfu_C-phZd8zd2UR0YSQDjQF86TK_3mWWD8V9tCNCOTvNZK-FgXTXIQHTNNpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اجرای گروه  BTS بین دو نیمه فینال جام جهانی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/673161" target="_blank">📅 23:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673160">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pscYnQLIu6BG5qR6knmQKx2KUeHLtDFdNaMhhgZnZNEKYOFINeGYFox3TE4cFNj5VT_hn0voNmL5wtHo3vToJtlnaxsEkq4HaFA6GvuJaj3Vr4YOhYxhMzL3gzH76f3XewaXrPW4tm7inavKbq8n0Y26NYGyWL4qpCYlHVMTfLS5a3dJy18XAXBdffz189cGuBBvx15eBpl8jGTFqb5VuxMGNNnVmhRBbF4HmuoFEVGVdb98jxHgFFexwx21rk7sH4eyMRN1ikjuD-IUA_MJap5OwQK49ta1t1mIDZmsBr1Xg5HO0SmsbbwKoKflgj6OtFjIXIjzAl-N6u1vfycAeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون وزیر خارجه: ایران ضمن محکومیت قاطع تجاوز آمریکا به دارخوین، اقدام مقتضی را برای دفاع از منافع و امنیت ملی خود اتخاذ می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/673160" target="_blank">📅 23:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673159">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyqtBgXWsmBWwxTE9HveYYomuDrzUbgSgVVToprZsBDjFbFhtKv740uMLDauvco0QDg3jOMTxBhN3TZGZwQe-se8rQxmtkEyC8sAPWgRJbvOKClVdOKjhpe2Ygu1o3Xdq-s4Rt9vnuZH9eMzA75OBjXjkZOpNe6SNVqCJWuoeVz_GUmjxiLw0Kl5nfIToDDhH7JMyX7xb6rSIdQjcfCGmS_UCUUB2sDWGRGvVMZmvZ1YW7W2KIhoY7OJaH4FYeSnIt0e0VJEMcLLJbGSF6WasSIUdjcCumSj1mBk3FggSbldVAjBJwQoqze5uajsh2E-VHFrKk2VQJbPQFFAvilOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیژن مرتضوی، حین اجرای ویالون در بین دو نیمه فینال جام جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/673159" target="_blank">📅 23:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673158">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
اسرائیل هیوم: سفر نتانیاهو به آمریکا برای شرکت در مراسم خاکسپاری «لیندسی گراهام» در هاله‌ای از ابهام قرار دارد
🔹
مقامات اسرائیلی نسبت به احتمال هدف قرار گرفتن چهره‌های بلندپایه این رژیم توسط ایران به‌ شدت ابراز نگرانی کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/673158" target="_blank">📅 23:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673157">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
گزارشی از هشتمین روز حمله آمریکا به ایران و تهدید دوباره ترامپ
👇
khabarfoori.com/fa/tiny/news-3231372
🔹
مصاحبه جنجالی عراقچی؛ هنوز آقا مجتبی را از نزدیک ندیده‌ام
👇
khabarfoori.com/fa/tiny/news-3231467
🔹
پاکستان هم شاید به جنگ آمریکا و ایران کشیده شود/ میانجی تهران و واشنگتن یا متحد نظامی عربستان؟
👇
khabarfoori.com/fa/tiny/news-3231570
🔹
سعید حدادیان: آنها که می‌گفتند «نه غزه نه لبنان، جانم فدای ایران» بروند جنوب/ می‌خواهند ما میدان‌های شهر را رها کنیم؟
khabarfoori.com/fa/tiny/news-3231482
🔹
آتش بس در دل آتش بس / طرح عجیب قطر برای توقف درگیری‌ها در جنوب ایران / پایان حملات در ازای گشایش ۱۰ روزه تنگه هرمز
👇
khabarfoori.com/fa/tiny/news-3231634
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/673157" target="_blank">📅 23:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673156">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0wSxH287Yg6GHeL9v8omKSbWLbP9y5A2_9PPUtbDFplTo3iyflbnCCLGpWLCrvxoQDewgLskU4ymFl1cx7hvDiZGCFSi2aBwBSlAPC4adg0Mfb4WIKtS60z3tMfVcxGzD6_QkSLM7xBPvA4VY-i13tHlZr2R_3Dmpw1GWih6-NliTPxKNerifI_DOEVMHZ04sEbVzxcJM1UnQ1AH4CPlUZ8FWQ9b9vQD9-Xv1vFlFADfXz0AoAPxZTJ0D3TwlHayRwMp7QSghL_qoSDcMrT2t2_fZOrP5VsljCj1578jz0L8YRXwXi8ht3ryi3cASWYpLj2CV7oGe2LkqdTOO1iZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسی، اولین بازیکنی که در ۳ فینال جام جهانی از ابتدا به میدان رفت
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/673156" target="_blank">📅 23:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673155">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
حجت‌الاسلام کرمی: مردم ما در اوج فتنه‌ها، چراغ اربعین را روشن نگه داشته‌اند
واعظ برجسته کشور:
🔹
این مردم، با وجود پشت سر گذاشتن بیش از ۱۵۰ روز حضور در صحنه‌های مختلف اجتماعی، هیچ هراسی به دل راه نداده و همچنان با اشتیاق، چشم‌انتظار پیاده‌روی حرم اباعبدالله (ع) هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/673155" target="_blank">📅 23:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673154">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIjeo5yioSHSN-U-ahw2GwefubZfotMoYEJvCq2XKTdxtPRd-JP-69V_dD7UEU53Adlctde2_qshtz5Oix3RD0YzoSjjodko0jEl9F9L-bf4dr242Jq_7LrCz9vqgx_Qqaapz1mzPSf24RGL1TGQGzOcEE6fK7Uy05GyXadM9baXiEcmgZUg5yJzevRlq_ePWoD4dMOkL8dahdU7Nk3BPqzp7FnYkH4fVmAWelFAFwtLbbWRZKn2uTysN7w3eBjvqQCOS77GEMNzJCTbHUiq8RNX6HOOHcoCzbFy2nI4GO2BGpBR8UDdrZDmiw8lbo4KKKZBTzZ_3MEEEXkFfEHu6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو هیات رییسه کمیسیون صنایع و معادن مجلس: اولویت نخست ترمیم کابینه، وزارت نفت است
قیصری، رئیس فراکسیون نظارت بر صنعت نفت، گاز و پتروشیمی مجلس:
🔹
در شرایط کنونی، اولویت نخست اصلاح کابینه، وزارت نفت است
🔹
آقای پاک‌نژاد نه به برنامه‌هایی که در زمان اخذ رأی اعتماد به مجلس ارائه کرد، عمل کرده و نه تکالیف قانونی وزارت نفت در برنامه هفتم پیشرفت را به‌درستی به سرانجام رسانده است. همچنین در حوزه ارزآوری و بازگشت منابع ارزی ناشی از صادرات نفت و فرآورده‌ها نیز عملکرد قابل قبولی نداشته و این تعلل‌ها در بروز نوسانات ارزی و اتفاقات دی‌ماه بی‌تأثیر نبوده است.
🔹
اگرچه در برخی وزارتخانه‌های دیگر نیز ضعف‌ها و کاستی‌های جدی وجود دارد، اما وزارت نفت به دلیل نقش مستقیم در اقتصاد کشور، معیشت مردم و مدیریت شرایط جنگی، از جایگاه ویژه‌ای برخوردار است. کوتاهی در این وزارتخانه آثار گسترده‌تری نسبت به سایر دستگاه‌ها بر زندگی مردم و اقتصاد ملی بر جای می‌گذارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/673154" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673153">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65067a3a3.mp4?token=NR3_dqcXTiueIZqBfHNkYVMidakINuZnZqAc3kvU-f6Je472Pwc2GucjchfBz1fa6KZ32WyEBBKZyw2sSoGK_Z7WXosG1lgSrfl5IIEqIaEfFKiMcMAKjPV9qfl48u-QxWeJkMzQ0KZO5rgv8e_pTyAwYyRyRt19Ni1KxNZYRstUj3LfsPYEOkTnsXPzQV4uehbsQ8y-OBIH2U8utSGWVd5kWxJhV6LVCQ1X6QYDrR8HkuwBumiNCf_ssTYcXz3f6U0c1Kco2eqMqWJQMukADmUyztiSo7AZkkJzMiKPMDjaoXmRpnOzAsECDsN8ySDcMmgTv9MtE6qrd-Yljg76Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65067a3a3.mp4?token=NR3_dqcXTiueIZqBfHNkYVMidakINuZnZqAc3kvU-f6Je472Pwc2GucjchfBz1fa6KZ32WyEBBKZyw2sSoGK_Z7WXosG1lgSrfl5IIEqIaEfFKiMcMAKjPV9qfl48u-QxWeJkMzQ0KZO5rgv8e_pTyAwYyRyRt19Ni1KxNZYRstUj3LfsPYEOkTnsXPzQV4uehbsQ8y-OBIH2U8utSGWVd5kWxJhV6LVCQ1X6QYDrR8HkuwBumiNCf_ssTYcXz3f6U0c1Kco2eqMqWJQMukADmUyztiSo7AZkkJzMiKPMDjaoXmRpnOzAsECDsN8ySDcMmgTv9MtE6qrd-Yljg76Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما: در بازی فینال جام‌جهانی هیچ تصویری از رئیس‌جمهور جانی آمریکا نمایش نمی‌دهیم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/673153" target="_blank">📅 23:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673152">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb30f9faa.mp4?token=dDdzzw-TknjzdoMxyGNSGjNNdPLmlLLNjG2OshD1hA4WEuyyWXvVOtotO_CcCzyd6OeZ3XgHJ5CY40g7cDB58ZdS-j_M3iopxfQRYYl2MuK3EecwmzfY4eP8qs3jJph6V7ArT4PjVgimUgAB4fSXbqKzOq3DCeWUM0xNLQ1yypYZl5YPFVqemYByID0l1oc0ZCeLyHYdfreo3-IHjQZVpOAcK6tFfNp5SRXlj2h0MGSmt4gihnV3b5JlNF9F9wbYtiPm-TwRKq33zfOCx6XFGYZN9SqB5xTnQ25mYKFE1jxdRJDMxy6TWuFLlHDjJSElvm7htAcMcBLCIuSshUJnmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb30f9faa.mp4?token=dDdzzw-TknjzdoMxyGNSGjNNdPLmlLLNjG2OshD1hA4WEuyyWXvVOtotO_CcCzyd6OeZ3XgHJ5CY40g7cDB58ZdS-j_M3iopxfQRYYl2MuK3EecwmzfY4eP8qs3jJph6V7ArT4PjVgimUgAB4fSXbqKzOq3DCeWUM0xNLQ1yypYZl5YPFVqemYByID0l1oc0ZCeLyHYdfreo3-IHjQZVpOAcK6tFfNp5SRXlj2h0MGSmt4gihnV3b5JlNF9F9wbYtiPm-TwRKq33zfOCx6XFGYZN9SqB5xTnQ25mYKFE1jxdRJDMxy6TWuFLlHDjJSElvm7htAcMcBLCIuSshUJnmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میرمهنا بندری چطور کشتی‌های خارجی غول‌پیکر را در خلیج فارس متوقف کرد؟!
داستان قهرمان جنوب ایران
👇
https://youtu.be/PkNQz2D9nTY?si=pgrF1QTSxQdPUYkL
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/673152" target="_blank">📅 23:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673151">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dec6e7bf.mp4?token=McZx8eXFy7YHT4meU7qiA5_V_STz03UG4cUu-jTXTra69QFdV0ZktB-iX1ByH0jsPqeqfWMDkScE0eOBEOfKIJJheY2OJEW3DXbR-MMQuF2s-9zPJcgWUfGT35FwCbMP9AR5H8_FaXtc3txpg6yCO68Y4CNQx71qFAd2a4T0V-7qUAmgsc0LA6rHZVq5FZoOiXDzLDRlU5w4bXtqN2RO8hJNuCYxNRHendNGUtU-9U1udLpuBRd0GNMJuSyudJIbI75NFX7cx0JEhlPdNbeE9fmkfmw-zTJPI4tDIkF6dzxs_NP6x9ZIWGrUJjqkL7K3r7GlqAJQSXMJkY9OrqIS6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dec6e7bf.mp4?token=McZx8eXFy7YHT4meU7qiA5_V_STz03UG4cUu-jTXTra69QFdV0ZktB-iX1ByH0jsPqeqfWMDkScE0eOBEOfKIJJheY2OJEW3DXbR-MMQuF2s-9zPJcgWUfGT35FwCbMP9AR5H8_FaXtc3txpg6yCO68Y4CNQx71qFAd2a4T0V-7qUAmgsc0LA6rHZVq5FZoOiXDzLDRlU5w4bXtqN2RO8hJNuCYxNRHendNGUtU-9U1udLpuBRd0GNMJuSyudJIbI75NFX7cx0JEhlPdNbeE9fmkfmw-zTJPI4tDIkF6dzxs_NP6x9ZIWGrUJjqkL7K3r7GlqAJQSXMJkY9OrqIS6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا در تهاجمات اخیر آمریکا به ایران، خبری از اسرائیل نیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/673151" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673150">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKF9SfVAzuF7CSukuPl9IgNou5AiI085mr-gC3HaI2QLebxTJ_v4ldnrENrcOaEYDIwt1Ca_3nEkW4MuwkIJq5wdkQag3O62h1yICm5QF8bKMmKJKtQ4K3LmRbXSQGQ4nePHU_Yyp3XKEeqr91QIN0mEd3So966Y8pW7iaHHuUGTLAZd_Qu091yefSVlRl5f5rSLNxIkPoUGM43AvhKyrD7SsJQBc2o_kDNPxjCaWkjZ3ae0oM8_IHS6V2wzEWMxZdmC56fJ4VydgOo8mLIVYnWaCFoRZnyFO20Vh-C0D-miqpCLErCNkunkZ48JdZ3kdA-e9rKNt33C-qeVhkog2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری اکانت اینستاگرامی مربوط به پادشاهی کویت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/673150" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673149">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a749daded.mp4?token=ZQz0hubwSm2crLu1aJ2_EXSThv_p9euzO05TMs_qzrWEcoqoT6BhejOJ-EvUgMkTKynS5JJVteG1H09q2AEEsaQAdBkQkDYZmhEW5hiFdw1BDLC_3sBetnE4QD_VdwA_3FFZg6ayEEmSAAGTpn0xWI7Z_61j8S7TlFDXBQYo6R_aZ9sfF3ZbGQ2KS_Q_qflNVN5QGwMaP6u7-eI95GOBkMemUKYcc-F9Z2TmPD50ZirnmGDuPL3Cy5hQWPMmBKUTRIlyWwMBr9ubP2lt0FDnTDQIRMbvDSD4De4-XvSM8NeDM-yYv1TDPOoCuBYTsAYtCCBkOMSMzV6QR7oyKif7bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a749daded.mp4?token=ZQz0hubwSm2crLu1aJ2_EXSThv_p9euzO05TMs_qzrWEcoqoT6BhejOJ-EvUgMkTKynS5JJVteG1H09q2AEEsaQAdBkQkDYZmhEW5hiFdw1BDLC_3sBetnE4QD_VdwA_3FFZg6ayEEmSAAGTpn0xWI7Z_61j8S7TlFDXBQYo6R_aZ9sfF3ZbGQ2KS_Q_qflNVN5QGwMaP6u7-eI95GOBkMemUKYcc-F9Z2TmPD50ZirnmGDuPL3Cy5hQWPMmBKUTRIlyWwMBr9ubP2lt0FDnTDQIRMbvDSD4De4-XvSM8NeDM-yYv1TDPOoCuBYTsAYtCCBkOMSMzV6QR7oyKif7bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از آشیانه F15 و F16 آمریکایی‌ها که در حملات ایران به پایگاه آنها در اردن منهدم شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/673149" target="_blank">📅 23:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673148">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHCMcIp7LyEsdYnpeWFnmMWBKgqkUl4tYP-rlLsOy5_UB9Lc9gnCIjzFMLJiHroIXFYTzPQCYWYGO4k3k2em574tFIsMjAzOYZR1ZOFhbKpXfMqxP-7P5ldHom7EhlQCx8si6GeomkaQ7B9z9vddZwC-Y-cfYsPmtGrzmFrsGUBWj8FzaAfAMgRX3Hmg3zYmbHk9tUzkKD35K7rVywYMlnn5VHeiEc3JuGcIr9tl6-2-aoDnlTa-z31Aia1nWT3n3jYZ2wm3coinQPyzzwI1HnZJ7EcowfcF_sg5_HRLJZdS-zARTdYy7TMPHbsirq7j5q85BsB1PCjSGy8ELoQ8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر ژئوپلیتیک: یک حسی بهم میگه که انگار قراره از اردن یک گروه مقاومت وابسته به ایران، بیرون بیاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/673148" target="_blank">📅 23:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673147">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gN4bg_o2gg-ivuNxqoOoQB7djOV9QQNxmPNj4HTr2ZkT1rQ8jFzwjZsufRDciY8CU5Dn8ojFs5-l_6zoM8MAPg99HCS67Z2NnKmeI9KktxL-HLDFlnN8zBQYv5o2l8onR0kbKfXIwp6HTTx21Mi5I72qVm6-3or6U5r6-9ntge5GDc3pNHEbvJ5dXSxKltNLgOr7qsTjmB8T5DaSS5ExoPTw8Y777jbxL3FnG3iMyrRdIdjdJDCwpJSDxJihnLzNIPyygvLw30hxnZcJoN_Q28cHXUXfei88FZyd9yCKNG_MWwjVPCnfHkmHuO51S0y7ctV_jkxHqiUNHdizbfrpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستیار بلوند مرموز ترامپ جایگزین دختر ترامپ در فینال جام جهانی شد!
🔹
حضور مداوم ناتالی هارپ، دستیار ۳۴ ساله دونالد ترامپ، در کنار رئیس‌جمهور آمریکا بار دیگر توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3231469</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/673147" target="_blank">📅 23:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673146">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
المیادین: صدای انفجار در اطراف شهر اربیل، مرکز اقلیم کردستان عراق، شنیده می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/673146" target="_blank">📅 23:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673145">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaKMIXckjHSrGWuzg_SQqhfBPSfhS0IaBGsewrh3bCG2ZyZAHGwWU8LqwJJWOm4uDegH3PobCeaOm9xe1NfEoAMrBhh6dss_mr-iBNXVYrFKYD815MOzfYyYNaq33_z5O6wXFWJPeffOEaSDQtSoBvlXK5upilQaOSIqehVANKuZWm0QvRc-yf1Vw0mq5Mo7GduBeLxz8ho_rumKklNGv-bByOV4XUv970PLhRNLgCL9zaXP6ULOGSdkQwZvo4UzL939QqjNdsaM80aDJPIw-Q3wRaJksy3hcNKLCnhtyTSVkluZD0EUQB6MqnM6xx6O1_xJ5vM9-CpdA1Ej863JEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر نظامی و ژئوپلیتیک: وقتی ایران کار پایگاه‌های آمریکا در اردن را یکسره کند، نوبت پایگاه‌های نیروی هوایی اسرائیل می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/673145" target="_blank">📅 23:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673144">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: کویت بدونه وضعیتش در پایان این جنگ عادی نخواهد بود؛ کویت درس عبرت بقیه می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/673144" target="_blank">📅 22:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673143">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7evvyw3b_jT7cWKo80YQL8CLR_zpwib5A3lWohsZat89k-VIVVZLeqXeaWGHlOqkIFMCLRjQ3feOVSIgIm6uaNLyEZ6rPi7W8b36FZ98FB9TXDz9L8EH7UZOqVgdoCyXCgangr_WylK3lwP1Oym_7AiiQnkO4myBEf5lTRWAk_HEzxk3-qEDY10JiGjcPkqHgxArDR1Ub3Z8sboohdG8sg7E2nxA2ebGeWyN5nZ--bzI57XaXaPm8ZxH5KoWlNE4Rhfl63ffqp5Qha4_SfV6MadomXx87ord9Vdc-2SmD-669GOzU5Sivpsy4-OghTa3_ewD6VH0o6Ko4GbUzMJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کیم آیورسن، مجری سیاسی آمریکایی: بزرگ‌ترین ترسم اینه که ایران با زدن تأسیسات آب‌شیرین‌کن اسرائیل، شبکه‌های برق و زیرساخت‌ها تلافی کنه؛ بعدش اسرائیلی‌ها فرار کنن، خب حدس بزنید کجا قراره برن؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/673143" target="_blank">📅 22:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673141">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZS81E7lAKtUhsEUUk1a_KmU4nvSngMA9PxxaO9aoeZhUz0ozyRW4lKhipsJi6HwKADjYvRGwbdK8dhrYHubuIVC54dqU5RZuuHKOGaeA_bMvUKPScaK9L-3H72LKL_u6OasgP2QjVQNyqulFv6sPgdRl8HS5oBviBN0f0mfPT7ob9ALCVPYAOtxgcOrTEPjdbJE_DsFx12rFRZz3uIJDzaMylXa8x-NAtuATw0g2hq33Sp1_LGrMN1itYXI-tTzkJnOABvavU44zW7TcyLo5pN6zq079nRYfiZltP7aWyboEZ67KrAX8ZKguZGPIrUQlxLfKppTjnbAR8iLNEIP7wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUR7ncnbAEOeBpTudkrjuUxIimnDm3iOI5f1ShHkPgSR36GvCf-VzWjRSoLJlNesR03mHHMCxYwCXxQDATHY9RRUl5gkgjc7lhy7YK6JU3569yOb7QKPs8xOtPYTf3LFTNHrqRBMHrKShdsXIfaNDeJVlLaomBOEHUKzJMz9EN5n4LPe4q9ryuQBkeG62O9mXTQDPMAdDGoEfFr9IOa3t8Lw0pJ0EYMd6EVN7iskkPpKyGon4veNeaynDbaG8eFaOGl7Z7KUZqvkdaGElbrQmX93cNG7JNwDPaBDfBR0siW7ubTh4uj0ZYdLCdIfRZddnZfk1IE_JiC_lJtorbK9Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سرنوشت عجیب پهپاد آمریکایی در عسلویه
🔹
پهپاد آمریکایی MQ-9 که بامداد جمعه توسط پدافند در کوه‌های عسلویه سرنگون شده بود، با کمک یک الاغ به پایین کوه منتقل شد.
🔹
تصاویر منتشر شده از منطقه نشان می‌دهد که لاشه این پهپاد ۳۰ میلیون دلاری به قطعات کوچک‌تر تقسیم شده و با استفاده از یک الاغ از مسیرهای صعب‌العبور کوهستانی به پایین حمل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/673141" target="_blank">📅 22:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673140">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سازمان تروریستی سنتکام: بامداد امروز بقایای جسد ناشناسی را در محل حملهٔ موشکی ایران به اردن پیدا کردیم
🔹
در این حمله ۲ نیروهای نظامی آمریکا کشته‌ شدند و یک نفر مفقود شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/673140" target="_blank">📅 22:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673136">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lQhTIBISBcm_t3xxrmts88ZImApD3vpmZ4HqjDIZzfTZs3z6e1G9QqMvmKlEzEJDBHFL0Smnll1sHzzlBlpZz7lUtaq6eO_zn_ijKzUEFwelaHQvRiJpEtZGN0PjDMgIqLuL7HNANaoHf8i4vPHafuJVtuTq3KJidlOs-qvkil3M6uKRAY9D0nUC2j4yc2bAwZcNynNwCmz7MU8FtxXbbq1al0wSRcMOvVa87aZBbqxGLPc7z7uXyS4fj2rMwMsyioE4c_KjrCJrw3Z97kauKdjGIMdVZTraj2yhPtUhKAn-7BCZAuErYVLhDKqqxV91FwMwI7kQ-nip7ZldY1QCfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpxFiPHEAzlBrdKl1zyOquk7F1Xs5O8q-mq5MhbQHpH66dOWzLLKOABs-lq5_5rsN-jiOOCWeYOTZkm9Pox4LLAqbp4NyQdLlw_SqdGP273kM4abmGQZyp4byRO2ae7zWwVsQYNLjlem2LR-HGEFE5w7ZToNE0OTnbO8UZ8MhbeEoPyYsjvyST2CLOStdo_dmJdCUXw_KXuybXckIvtj52aSnYj8c067hGM457FhQz8NFe2EthB3qqVui-rf01Bs3nbTIps5k8stCziP_DV07L9RF7-ll2b-A_qiCDwLI0dNqRb1-tHV6aOPzyM8GN8lwuEivh2qXejNjr5NqEx9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcPn48FLsoBewg8pZr2O6Jis1k95Ih8xCldYV_dBRoACBeF0GwPBMRJnWGjas4QW-aLG5W2100I7RkQ8ytEVFj--Ibks5ZqaA7oIlDbZGd4O4TK-OeqniTZxk1u5I9uFrEt7ke3ERRRxeX_qNVn4kMQqYcQFMGdzjOpcapiElEnYz_nvpG22DgdVfw6bWNK4oJ0ehKmlTPU6BUCjz9gLEiaJFZCYSWwEvb0Gts7JXl3QNlAbq9ubPAsPXkBE7vB5CmRDW5w2EJVHFUCdvsq97RlAmR2JjXyXA8IXxQaZm7jxNTVf1SjW36VpRB7KZ20YJkGDQQ--H0nWTCnyU-z24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aAmoOiXwZ2emPSqKng5bLCB8jJx6pKI-2SrTgXykjnL2tZ2kjDGOhR--M63nGrWG6AM9Sb3AZqKcGKumibkIF8zdJmgz2ayI4oDWiCwNs-OcrQ4mXZig1q-2DJAifMOPzb9rscPgIVeXT630wYRPowZgAyC1nPj4YcjeeXC2jhD5SydPdbtzimGXooQZzrDR0DiWkT4VsW-pIyNh7qxlELVSFmYsAmOy_TikcBd6H3eGuiFDPwBMWpshQkIhQqEs6RXfjUxiL1BY28sVSVyhef03-4h0tQ3aDPkbvVvRkf1ZkigF5JUHrlSOom7FYXJgmIHDSxfVsyWZ_Txn-NJhHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درخشش ایران در رقابت‌های جهانی ربوکاپ
🔹
ایران در سه رشته فوتبالیست سایز کوچک (SSL)، شبیه‌ساز امدادگر و امدادگر واقعی (Rescue) طی سال‌های اخیر بارها روی سکوی مسابقات جهانی ربوکاپ ایستاده است.
🔹
در رشته شبیه‌ساز امدادگر، ایران ۶ قهرمانی جهان را کسب کرده و در رشته‌های SSL و Rescue نیز چندین عنوان قهرمانی، نایب‌قهرمانی و سومی در کارنامه دارد.
🔹
این نتایج، ایران را در میان کشورهای پرافتخار و تأثیرگذار ربوکاپ جهان قرار داده است.
@amarfact</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/673136" target="_blank">📅 22:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673135">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سنتکام: یک نظامی آمریکایی در شمال عراق کشته شد
🔹
فرماندهی مرکزی آمریکا اعلام کرد هنگام خنثی‌سازی مهمات منفجر نشده یک پهپاد ایرانی که در شمال عراق سرنگون شده بود، یک نظامی آمریکایی کشته و نظامی دیگری زخمی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/673135" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673134">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3YhOhRk2tEujV36MMUTRbwnrhLeEBY6YRND0tGWrGehynnOMJR9OXdcPIW3Z6Fw8t3tOZ-0UlaMplIr-HM9oLjT2SCau_nqSYijBG7xV4r05H1aPJQBqtztIBdMJ9UlEO6Z_k8n06D527UVTZMRNAxcNdFTZgJo4_BknC2S5BoLGNuW8bCXO7I9pc6S7BSlKR1iipqgo_vHH4BOEtlF2ZWyPoSa2JukRRSMedX9R1eaEua_dMAGgzHvSkKBBQJRJ4gQlL-hZi6dMs5VqcCP6TsozO4pFKO26JEhgJozs8rijI2U1yQzwgKkeaGC5r2SmLJrW0mkJTdtFfVXn7pFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای آخرین‌بار در جام جهانی
🇮🇷
نمایش پرچم تمام تیم‌های حاضر با حضور پرچم سه‌رنگ ایران
در مقابل چشمان سگ زرد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/673134" target="_blank">📅 22:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673133">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b5e4e960.mp4?token=rdXSBz7zwVLbEDn9o1WETaN6Tw8a4C_jhTj41l7ctMmCDCxHYy5dCgZ-7CV641NfiTVMtV7ar0zgMDImqLf-_qZmNJAAbK68h-g3pWrb8DcU-LOuaxAAwmclJvNqveGPpma9Zm8o6DjytILDYCnEL_iwB-1TgFuG52G_AYa3ltld_9UNh7A698GAKLzz6Y_USwFIlJ5CXFTOzWyZNjVFJKPudS2upROSqg1oLbu8x-VeimfpIdHnJf8yryOkh2vN8QO5Qpg8Z1vR8ofB3kefAGSbgqT3wbe7sRiLjzBmHFNgclJUj3sNecEs0pBV_qRyXa9whSu_DsUUKgJAMGfQTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b5e4e960.mp4?token=rdXSBz7zwVLbEDn9o1WETaN6Tw8a4C_jhTj41l7ctMmCDCxHYy5dCgZ-7CV641NfiTVMtV7ar0zgMDImqLf-_qZmNJAAbK68h-g3pWrb8DcU-LOuaxAAwmclJvNqveGPpma9Zm8o6DjytILDYCnEL_iwB-1TgFuG52G_AYa3ltld_9UNh7A698GAKLzz6Y_USwFIlJ5CXFTOzWyZNjVFJKPudS2upROSqg1oLbu8x-VeimfpIdHnJf8yryOkh2vN8QO5Qpg8Z1vR8ofB3kefAGSbgqT3wbe7sRiLjzBmHFNgclJUj3sNecEs0pBV_qRyXa9whSu_DsUUKgJAMGfQTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اندوه را با هم تحمل می‌کنیم، سختی را با هم پشت سر می‌گذاریم و امید را با هم زنده نگه می‌داریم؛ کنار جنوب، کنار ایران #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/673133" target="_blank">📅 22:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673132">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea4ba715d.mp4?token=WF8aPJqOC5sjZS9M2AlBMdwv9usY5pAuqx0PNLvcJEFlfndlNuyVvaz1HvqSZGGX9NDMj-yvT4ZcqLzomCK7DhoxuTul1e00Qc106arXgmVr_54UBf0KodVJuC_dJPuvrEJ4yH15vv5MB4Wra92dxJ84FtLRJcbQRJEuaVB-Htr6RltML89xsDxSIXz7PTNptfb-pc7LbkGXtRBNaMGgErGECSnCgxx_4MX7pj-xtky6pzF5KKFGgW9SMxmM3_cUOlhaP46YCYrK0udSgmZjI_iMhjD9aY2YMTWlDE0m8CCX4ZZI58c2ids3mv8xL16dk5yShNydzF2GLrhpZC-LUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea4ba715d.mp4?token=WF8aPJqOC5sjZS9M2AlBMdwv9usY5pAuqx0PNLvcJEFlfndlNuyVvaz1HvqSZGGX9NDMj-yvT4ZcqLzomCK7DhoxuTul1e00Qc106arXgmVr_54UBf0KodVJuC_dJPuvrEJ4yH15vv5MB4Wra92dxJ84FtLRJcbQRJEuaVB-Htr6RltML89xsDxSIXz7PTNptfb-pc7LbkGXtRBNaMGgErGECSnCgxx_4MX7pj-xtky6pzF5KKFGgW9SMxmM3_cUOlhaP46YCYrK0udSgmZjI_iMhjD9aY2YMTWlDE0m8CCX4ZZI58c2ids3mv8xL16dk5yShNydzF2GLrhpZC-LUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحید شمسایی: در طول تاریخ، خاک وطن را قهرمان‌های گمنام اما شریف حفظ کرده‌اند، مثل همین مرزداران جنوبی؛ ایستادن کنار شما بزرگتر از هر‌ جام و مدالی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/673132" target="_blank">📅 22:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673131">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
صدای انفجارها در سلیمانیه عراق
🔹
منابع عراقی از حمله پهپادی به مواضع تروریست‌های کُرد ضد ایرانی در استان سلیمانیه عراق خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/673131" target="_blank">📅 22:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673130">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUz1f8lrrbLtu3sWXpwMC5k0svAjLw8_Qy5RipJyK9SEvsOKBzsM7zXJy_UczgrqKDLLhIFLwyo4gcDh5N_pfhWx9wAbGQgu75vBcZAma2DfD45T47IMyUBsnNXgudA2SdcKJPcvyLsXfHhsBmv8OQDVdlczSRBS8-MzUHr-fZYuY-XNmO4k8FE3rITQAZr7GpWBbHAD4GLaG4-wPvqkY5ni5TclZFi3sh3obZFHsn-HHH6KZYqPlNVL-7bnLHbh1vue1TRux1czqP1RTrFr0su9Fh84UzJ9qV1vdd1f15g0GRvbZ4sgoxPjPiRDAVAlpya2TYIMCN5dySG3gUe7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه طور بیشتر صبور باشیم؟
🔹
صبر و شكيبايى گاه در مقابل شهوت و در مسير اطاعت خدا، گاه در مقام پرهيز از گناهان، گاه در مقابل درد و رنج‌هاى دنيوى است و گاه در مقابل پايان عمر و مرگ است.
🔹
براى اين‌كه انسان بتواند در برابر این مسائل صبر پیشه کند باید عقیده قوی…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/673130" target="_blank">📅 22:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673129">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd7bbfb25.mp4?token=oVznsjg0HJAJNSiFQF7wjKCyvJtotpWyMBduDOIMV4wT0vdNEe-FwFLwnP0FQjqOAPVzZH3i9MmmMUfUwOK7Bq7ZzZpv4797FQj8U48VKhjq9_MNhjE8xqVBOQJSx81PFgcGdrAirj9rnCj_CQNsiTDkwBRQ14p1R8_hxZO0tS0ChGfH0RKx6avfJHsGpyzlQOcJkw_bkeN7XWjhk9zyKCMc1-0_zRkIuJqw5Pm6ctU-HXWEgEkvfbGrgZaTF7m_6v8EnE3rFBtiEpEde4bOlz0SVTNPDZMtykRjvTA7ujFMQNzftpQl5m-3vC81ESX_ZBxh-lWnQRwqUjU8iBxbqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd7bbfb25.mp4?token=oVznsjg0HJAJNSiFQF7wjKCyvJtotpWyMBduDOIMV4wT0vdNEe-FwFLwnP0FQjqOAPVzZH3i9MmmMUfUwOK7Bq7ZzZpv4797FQj8U48VKhjq9_MNhjE8xqVBOQJSx81PFgcGdrAirj9rnCj_CQNsiTDkwBRQ14p1R8_hxZO0tS0ChGfH0RKx6avfJHsGpyzlQOcJkw_bkeN7XWjhk9zyKCMc1-0_zRkIuJqw5Pm6ctU-HXWEgEkvfbGrgZaTF7m_6v8EnE3rFBtiEpEde4bOlz0SVTNPDZMtykRjvTA7ujFMQNzftpQl5m-3vC81ESX_ZBxh-lWnQRwqUjU8iBxbqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امتحانات نهایی تمام دانش‌آموزان حداکثر تا ۱۵ شهریور برگزار خواهد شد
فرهادی، سخنگوی وزارت آموزش و پرورش:
🔹
امتحانات نهایی پایهٔ دوازدهم روز سه‌شنبه ۳۰ تیرماه مطابق برنامه در تمامی استان‌های کشور به‌جز هرمزگان برگزار خواهد شد.
🔹
هرگونه تأخیر در برگزاری امتحانات نهایی، علاوه بر فشار زمانی، روند شروع سال تحصیلی دانشگاه‌ها را مختل کرده و اثرات زنجیره‌ای بر سایر برنامه‌های آموزشی خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/673129" target="_blank">📅 22:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673128">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBank Maskan | بانک مسکن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2887ed15fa.mp4?token=T6jsFZenoIr2mN1XL6RlpdlDKrsWVgr6C84HL51afz6UgyeFGmCs-XGtxCjCejYnpjuSsDCCxUZGyonZpsfNyg4SNZW4o1Iy0xxXLMDU5o7ECAI7ocjJkQHd4FVEfdKhtSpe4lZRkdfH6F3J4C8zPf-74q6kKqe9JY3w8bCHt_iMgJ18L9dC2d1hUk1hCpNSq1S4CqBtNLyrFjzjkXKk2qA2TIP2EbVPAS-Aeq7_WsFua9rwdS74c7b-V5v5DSVnwFeZLwOKNzT0BJLiAZMUeTZplR22XWG_MbVs6i_1G7N04YMmiEdOaNRx08laC7osvSAtoKGYjOD6WoDZ9Ju0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2887ed15fa.mp4?token=T6jsFZenoIr2mN1XL6RlpdlDKrsWVgr6C84HL51afz6UgyeFGmCs-XGtxCjCejYnpjuSsDCCxUZGyonZpsfNyg4SNZW4o1Iy0xxXLMDU5o7ECAI7ocjJkQHd4FVEfdKhtSpe4lZRkdfH6F3J4C8zPf-74q6kKqe9JY3w8bCHt_iMgJ18L9dC2d1hUk1hCpNSq1S4CqBtNLyrFjzjkXKk2qA2TIP2EbVPAS-Aeq7_WsFua9rwdS74c7b-V5v5DSVnwFeZLwOKNzT0BJLiAZMUeTZplR22XWG_MbVs6i_1G7N04YMmiEdOaNRx08laC7osvSAtoKGYjOD6WoDZ9Ju0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاهی یک جمله، آغاز یک تغییر است...
«زندگی در دستان ماست، اگر...»
ادامه این جمله را بنویسید و در مسابقه بانک مسکن شرکت کنید.
1️⃣
کانال تلگرام بانک مسکن را دنبال کنید:
https://t.me/bankmaskan
2️⃣
جمله خود را ارسال کنید:
https://bank-maskan.ir/j1405
🎁
به ۱۰ نفر از شرکت‌کنندگان، به قید قرعه جوایز ویژه مسابقه اهدا می‌شود.
⏳
مهلت شرکت: ۵ مرداد ۱۴۰۵
⭐
همچنین با افتتاح یا تکمیل موجودی حساب قرض‌الحسنه پس‌انداز بانک مسکن تا پایان تیرماه، می‌توانید در قرعه‌کشی هزاران جایزه حساب‌های قرض‌الحسنه پس‌انداز بانک مسکن نیز شرکت کنید.
ℹ️
اطلاعات بیشتر:
https://bank-maskan.ir/g1405</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/673128" target="_blank">📅 22:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673126">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6dpgD-RwsuvqNIw2vWCye3WMb9Y7eI3FZ_2PAJFVnGzy2Y3R1ZLdAmuSSkXSGBus0R2rmuAm6V7hytH2nsuibDHkFFge04xiJ4wG7sUuWwk4rfmFm_4tcZzc6HNVeLFmUlQjjI_-SOELeG731Iox-VI86_f8o6_kYVQW35fo1pYL04C25jPUb6DIGNfWjtBsjY3N7uL15BF6eLU1AQ2gU0wiBIaQEchYnWEX8FN-cxZBBAjSj3aXbxVJ0YP8PQj-N6h519JVNftbXn9_PdOI2U0uOKNEamQQE9KlyjbhsCp0US_RLZN9sY2twmtc3rQ8IxfL_XWtnbXSkUnTEY_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3jxvKwt-R-OGHiUzNeXR0cGE3cW7YDfYo3EuId16-DRdePgbALGGrPT6wpkfX90YdU-j342gQZbhF-6rPDdzLw6Bzy7bE6ABN_BbP_bEocPKqO1MEBlIQuxH3_wFNaCk_QfLYjiF2mLDO0xZIdAWaTE2E0Ftxw6m-E6yAVTDIKY7KNAIP2JBgsc38zVXQ1tVNMxieTGHF35eD185Ixa198OURs5NeVVmDZY-zGOJjW57F22VPO1NgrpGH5IjV3CXc2qE2Ts--pScqCE0BpwIvBV-HbiiRWdZ3Hb976k5aMruwGFqLizbPtwpmsEFzgvXvzNqNlv7dBk0CVojknepA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نمایی از ورزشگاه پیش از آغاز بازی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/673126" target="_blank">📅 22:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673125">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc6300f6c.mp4?token=rXPpaS-2sdMmrCvcn9NRnKPwpX9I1t_bdCYlPHOCC3Eagy2BiuSZ894A8VpWlPbPuCU160pKNr9Qj2I2j_m8S4z95aENy74S1gI0N6rw-_rQgzWRVN35T0slpsAuK6nm0Xxo4T9cm7Dcxj2nKaRlooAKH-KMApqEstDxHtmoPC99pf6r-07Ycf9-hCpy8tF4kt9REj9xbfYEGsSt4p7A87RvvBa3awMAHRkyglgWjLoWs8le7RXv3pG1Slma9CfYjKs45y9KPJQ-kdfpGpcKdq9sxGfgtm8yC1cyhytd7CNrJTs0akCHqVFmCtJRDL8g-gQtDjjGNQCHY-CByPDrTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc6300f6c.mp4?token=rXPpaS-2sdMmrCvcn9NRnKPwpX9I1t_bdCYlPHOCC3Eagy2BiuSZ894A8VpWlPbPuCU160pKNr9Qj2I2j_m8S4z95aENy74S1gI0N6rw-_rQgzWRVN35T0slpsAuK6nm0Xxo4T9cm7Dcxj2nKaRlooAKH-KMApqEstDxHtmoPC99pf6r-07Ycf9-hCpy8tF4kt9REj9xbfYEGsSt4p7A87RvvBa3awMAHRkyglgWjLoWs8le7RXv3pG1Slma9CfYjKs45y9KPJQ-kdfpGpcKdq9sxGfgtm8yC1cyhytd7CNrJTs0akCHqVFmCtJRDL8g-gQtDjjGNQCHY-CByPDrTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود کاپ جام جهانی به ورزشگاه مت لایف با حضور آندرس اینیستا
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/673125" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673124">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fabc038fb.mp4?token=lLWfDGouS1xHyhnX8lAHy6Mm1QH-ZQqODZ0L_hevVPKROe933Nd1EhEVuOiwa4OlGt5C34DER67QhstlOPjZL4hmyM-QgMPUlgjVRZKqbqOsf_4AYf-gpPGO9GEGc7R8pVBuLzOX0xiVHW0Vb5ipELDMxR5Fy7jPVgjfzK_LXtVL4CcvCz2J9IQg-_P-ptqZo5lXuJbOS1Q2ySRXLjUpvEQ_Fb9mmvAkdWqJWZ_S9vl-pshWIfTZiPXpQHsgNyAkryhvxwPzLaY1diBw7-0X44G_VLRkyWniksVDQSke-dZRngzIIlLXRnI_n9vgY3QfVLGOa89EiaDCj1LoYO7mOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fabc038fb.mp4?token=lLWfDGouS1xHyhnX8lAHy6Mm1QH-ZQqODZ0L_hevVPKROe933Nd1EhEVuOiwa4OlGt5C34DER67QhstlOPjZL4hmyM-QgMPUlgjVRZKqbqOsf_4AYf-gpPGO9GEGc7R8pVBuLzOX0xiVHW0Vb5ipELDMxR5Fy7jPVgjfzK_LXtVL4CcvCz2J9IQg-_P-ptqZo5lXuJbOS1Q2ySRXLjUpvEQ_Fb9mmvAkdWqJWZ_S9vl-pshWIfTZiPXpQHsgNyAkryhvxwPzLaY1diBw7-0X44G_VLRkyWniksVDQSke-dZRngzIIlLXRnI_n9vgY3QfVLGOa89EiaDCj1LoYO7mOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینفانتینو و ترامپ در ورزشگاه مت لایف ورزشگاه محل برگزاری فینال جام جهانی
🔹
خوک هار از پشت شیشه ضدگلوله بازی امشب را تماشا می‌کند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/673124" target="_blank">📅 22:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673123">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ادعاها درباره توافق بر سر خروج کامل نظامیان صهیونیست از جنوب لبنان
🔹
روزنامه «معاریو» به نقل از یک منبع لبنانی مدعی شد ژوزف عون رئیس‌جمهور لبنان و روبیو وزیر خارجه آمریکا، به توافقی درباره خروج کامل نظامیان صهیونیست از جنوب لبنان دست یافته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/673123" target="_blank">📅 22:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673122">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9ad63557.mp4?token=Xm3XzzaC6N9-ZxzRDt90vhdLPnD2cZVxhEHdGvO99c3NwAXURdZYpko9AXJNM60I8GDDO5KMbr6dCpvuEGEQoNN9e9QgmH5YH9bHEgC-wgIT2ui1YbplpmndbgzeWDFtaEZWzLlA9D_b3Z2KY9pPk_mm-tu9Nvz2sL7fWTXescroAQnZuU2wJOdNV0wHICPvQ7yOBT53-fZeBqBPmJQyUrG5pWoi2NF9zEaq09poeb_HDMwa79q8tLQPqO-ZR62tO6JQ2cOtOWdbOopU2-ByiBPScx-qmbIFj0sc6qS5tbK4gvPZQUUs66q31l90VcagTqxGnoeMc390EcJG6zGbVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9ad63557.mp4?token=Xm3XzzaC6N9-ZxzRDt90vhdLPnD2cZVxhEHdGvO99c3NwAXURdZYpko9AXJNM60I8GDDO5KMbr6dCpvuEGEQoNN9e9QgmH5YH9bHEgC-wgIT2ui1YbplpmndbgzeWDFtaEZWzLlA9D_b3Z2KY9pPk_mm-tu9Nvz2sL7fWTXescroAQnZuU2wJOdNV0wHICPvQ7yOBT53-fZeBqBPmJQyUrG5pWoi2NF9zEaq09poeb_HDMwa79q8tLQPqO-ZR62tO6JQ2cOtOWdbOopU2-ByiBPScx-qmbIFj0sc6qS5tbK4gvPZQUUs66q31l90VcagTqxGnoeMc390EcJG6zGbVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از لحظات برگزاری مراسم اختتامیه جام‌جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/673122" target="_blank">📅 22:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673119">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRUPfbkBciu3U_kPkb9QQeULg6Ne3K0HfurT0eCtrluT4GqGQsSfwUJqXm9B-Oy4YjliA8sLOwxTTwAyVhN0sSE2uN9gr8DNQJCpv3xR-S3MDM9ScijLtIzWiNlnewvSiP5nMXVwljRt-5JHsJ_AJWmRxvPD3IrqzATekFMrzydHN4yLbDXGT-izdRXS_bxKq_JxBpScSHLfaX3rKice9x9wVuZNlUy3BVgnVoveV5I15dv0RWU50AUvPwLOQqpCQ5PO8ofEXlR5lcxvv-R3RHBJFMIzFMAWPVb-VWs13m5phVGhdmzfhr9C2OgHcJNHuh0mimvPA26dcCS2vpmF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyY0YZOW0KCI4qTb93bQRK5x_WcczQVMhHAG7ISETs60PQAsW_pBC146cleNEqU_7lYLHDmsLK6mQ_XYgSkuhcE7ivA2WzjiUfg5EXhbq0gq8A7t3yBgankpVBQfP1sv-XyFFLA9Qs0eadJn4Nj5pjg2RQKfw202AcR65JMb8qLyOgnjkRh7io3cE-vyxDf1Mtjw0k4bmLgR8O8IhtEIw-znJ9a9nIHramSV9VxZQbhpRQue5Kd7hcpp1KIgO2hykYEGD3TfzfpTvnx_rgR8zaihC2O7zOd0dVijcJvxxNGcmt4sKDgQM5V8t56VrA7JIIGOZolaF2uoD8sWQHhJjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پادشاه، ملکه و نخست‌وزیر اسپانیا تماشاگران ویژه فینال
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/673119" target="_blank">📅 22:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673114">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای
کانال ۱۳ اسرائیل: قطر طرح جدیدی برای کاهش تنش میان ایران و آمریکا ارائه کرد
کانال ۱۳ اسرائیل:
🔹
برای نخستین بار گزارش شده است که قطر پیشنهاد جدیدی برای کاهش تنش‌ها میان ایران و آمریکا ارائه کرده است. بر اساس این طرح آمریکا حملات خود را متوقف می‌کند، در مقابل، ایران متعهد می‌شود به مدت ۱۰ روز دو مسیر کشتیرانی در تنگه هرمز را باز کند./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/673114" target="_blank">📅 22:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673113">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9016aa38ae.mp4?token=CbQIn9hVSjETcAQ0HoK9xiYk6n3o3naSuGayt9WlIM__FopLd_iJuFS-ofhm4foP90rxqorM1TA0H4M-kKcXqcR8Sgt9KHwUUc61sdo8sg9db8QRRKETnvMjl15Ot7GS5hjzFQS8hm3RpLBkZ4N5eQi0zlsv0uJSOWvyIUs4CFe5Hcx43M4XVxruWQdOC2NZKfImB9oW2BKgGkb09AXM7HvFkio69a6FiQhhyMe1pZjKS6BblyQq8QICVk36uo5OUpoF7utVK5PQx_XNk4PIv_fgQrQDyIxPtRxfI_L6Y8pmeh0MD8qNuPE7qHbTxWREpVf3G_kS5jKYy1Pe2USZcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9016aa38ae.mp4?token=CbQIn9hVSjETcAQ0HoK9xiYk6n3o3naSuGayt9WlIM__FopLd_iJuFS-ofhm4foP90rxqorM1TA0H4M-kKcXqcR8Sgt9KHwUUc61sdo8sg9db8QRRKETnvMjl15Ot7GS5hjzFQS8hm3RpLBkZ4N5eQi0zlsv0uJSOWvyIUs4CFe5Hcx43M4XVxruWQdOC2NZKfImB9oW2BKgGkb09AXM7HvFkio69a6FiQhhyMe1pZjKS6BblyQq8QICVk36uo5OUpoF7utVK5PQx_XNk4PIv_fgQrQDyIxPtRxfI_L6Y8pmeh0MD8qNuPE7qHbTxWREpVf3G_kS5jKYy1Pe2USZcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هرج‌و‌مرج در ورودی ورزشگاه مت‌لایف
🔹
مشکلات فنی در گیت‌های گردان، بررسی‌های امنیتی اضافی و دستورالعمل‌های نادرست از سوی مسئولین برگزاری، باعث ایجاد صف‌های طولانی قبل از رویارویی اسپانیا با آرژانتین شده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/673113" target="_blank">📅 22:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673112">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
خوک هار کشته شدن نظامیان آمریکایی در جنگ با ایران را توجیه کرد
ترامپ در  مصاحبه‌ای با روزنامه نیویورک‌پست در دفاع از جنگ با ایران:
🔹
آیا تا به حال از خود پرسیده‌اید که چند نفر در ویتنام جان خود را از دست دادند؟ آیا تا به حال از خود پرسیده‌اید که چند نفر در یک روز در افغانستان جان خود را از دست دادند؟ در یک روز، تحت رهبری جو بایدن.
🔹
ما در مورد دو جنگ صحبت می‌کنیم: ونزوئلا و این جنگ با ایران. این موضوع شرم‌آور است، اما در این مورد، آن‌ها جان خود را از دست دادند زیرا نمی‌خواهند ایران سلاح هسته‌ای داشته باشد و نمی‌خواهند شاهد نابودی خاورمیانه باشند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/673112" target="_blank">📅 22:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673109">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3uMfjqX7fPlxzurlzcqSwigX_p5JCMu2IB0KEmpN650S7dlp3GOQsd7Sc4uPkX7e0G2pyxiA3keMnfiUpj8qhbe_xqyqXIhhxWRW0avN9wIRO6YVCKzRe6Fbdr8jA-QYMQi-T7v6vAEYSgUhTcHWaAfzUJQSZ_jvwRgE0vrmz0HC4JMR_1ITr3siNmvPBz6AcD4w00ub54vRRxlA_25fQHtDXxw2wcEVeIYAmMV-E2EFL_5GmnZlArqWujYX2Haj1L3ZOlz-ai_KBrjYef7A3_6b93SJ0pgjOPS2eQSXVNHHOs_yC0S01njhz1tlXqRY-8IBgiLKg-d1QjLusrwVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAGD7isIp7lqEumz1fXQ5LKbL278VSfOlxP-GXLDnefp8CV7jybiiUn7P_z6LkJLzVXCz9c7Hp3whLGsW57Nl4zdTtMbso3A50m571vYKSuRcDWEl1RDfWufPLe51DgQyUjJSy2-KaRNpmdHJ8_Kx76w5ECHf9lfAlQGbML0LBD0r6LZu2TJAiGheqMZKuC9oEaSfHQmwNRMx8ESqmp3KlB956li6zJ3RQl1rE2rLgaE9GDSnt9vLjNiekKr6XrOfIKvTXyJuTDeegIeUtHb3FEVjyhIkeG3Mpzaa5FaPB7ZrRxref0UtRtqr5-FIKy4-dgFnixBL0Z-8apz7GOjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4pVf_YLfq5ibfqjpzj4Dy-dyD1Q0_nUxsp2oHFUX1C77rMtEzFovxpioCH3yUsC3KZ0Ad6wdJLEY68Zsdn-FTPqX_THG3XNeblk0mPESG9dw7SJb4bmCJYzw4Oe29VId2ZpcSmLgFTY_8QPfqdTeHk-QbthXAdr4c6g49qGiJxSJZBL9n01ceptYXHDlO-8X0HOx-fawuiN037DZBij9Am_EKUwGnxu-kLO-_nGIMFOy60u8IkBcG0dTAV_443QSCum7IFlHinWDtYfmWa8_fu8kAQUOpCXGWEaCKCqq0SndWS3Xm4sMh3sBOzT_zx8uYec0F0CQBXm_uYz3Ta7Vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هواداران پرشور اسپانیا در آستانه بازی فینال
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/673109" target="_blank">📅 22:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673108">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سخنگوی وزارت آموزش و پرورش: سال تحصیلی آینده در تمام مقاطع تحصیلی به صورت حضوری برگزار خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/673108" target="_blank">📅 22:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673104">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_dTeP6M3_aell4o47EkTND7YasZOcRC1n8b-PLnxAmeQ-I03W8qHwGdQcppBMwEyxPqeCZmBwxTZGrOtHErvZ-e8Ep9nQUe_j89KzxrjU3AewA4Jd8nNyDurtix9K_0FhdqVShazd6Iy8l4G0M5Ez0qGT1xCfW_4eWgFcMgKjvFGIlOX2I_Dh6kL5WlZszzCqgNRfYbhcf7kxI-X6VbGsELdYmvbSx91H33dcl4JHhs3TnDYTmSNfKdLRy2NVJwob9dsQH12zYIkJMDHgWrP6y9XoqRAgmTBA2gJeQBPRd7DuVuGymbyvKT0Hq2gXGH_FQ16asekUPKHq8v9CJnKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIoB_y2zbkzjBCFLL3bPLPeO8FDpaTfnZ8cQfWGEwl2EP9YMUAgB68RVtdIYfFmLdOe3toF7mGzrowuEp8JbVmvYDVNpfbpUKUbF-V_9LStLtwBmuHoflrIVou4-64aF-3oMNxqXgtvmsxxK0QKFRn6q7IDdFBtM7zzJHvrnzoSvWVrqF0AnKMoWaqT6EoBXGGNpub0lCb5XpybfwADx9C5UGxHPyfxTCpjyvqXyb3sFSSOr9vJmGd8xt4GEvw6ctfTrpgjjnLDK0U3ivX6Bt5M015BDpLHJXX_EYaiF3qhW5fo2Fmw_0l7vpG0-rimM-gRkwDuLFDK989gLqDRgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aaYbk28v19fk2sX9pemzUYiFtoq3zjd1YxcSB7QDIaCahKZdxYE65v_rP_z4HN-wrH5s7jzO0Y4C8OiZWoGvrEP1cJGJaHMaav2RTFAd8khjQhZtQg9xLIETYXYxEdRgoaBTxC5yYorAXCURDlJFh-iWG_4gtdw3Fp6yQi3oD_pAYhimyy_9TUuiNWT7fiNZYVwXBdYgsnoS9sU4hs_PywDYMC39-25DL9bHHqn3RvCRqALF_3CNSAGJvIA9hMVyb3YmnP3sZ0CN8pzCv1fsUkLCqHolaQa8UDhdgpxUs90Z2-hNFyNi7GDHF5j61JHeD--Ht0Ue9DnVrWCGTsOFyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z13fJItjMqUF3O0Fav2uXz1HKJP8PhW4CX8Mlv7LzsccmGcjuiu-O1gEHSwVyU_-F5qbW7CqwKx4i3GY3cyosAHBkGHpRNd20cuPB3_oAic4eyyeMm5ww2zuPGAJkH93SYivlI2Ukq9DkxXsD6QaehUbpEGjcgCYTOTYUGwWZM0ZZTQG2k49ENvIvgNVdSUPc6gL3Igq69cijL_5n9H4Pq7BPRG1OLXUQk8tH-VK_tqWek3Nvw3_5Kk_KrWp5LPQIZkZTiZKNdS3UONleSUqeA2eA9TZz2sdB5wYcac4Og43ngTo8MJb8eQPnsy2JvMAUt99D11eUT3sF9hNbnJTzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از مراسم فینال جام‌جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/673104" target="_blank">📅 22:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673103">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee935b79a7.mp4?token=s8VSl6JAZ_LJw3dZgpL4I-Z6-W3jmoZwtQi1dW8GxBIpBevAEEs6_WEYW3KbcTJWDpvcR2NCoJU-S0KUt5HZeQ5iAErozwJmBaqbiY8GchAUZ3yuzSXHwGyoefXAhOtKpc3g_ebmxOke18gqMOw8xSVr3P2q8cVCNuQIjJkFvQ47qdbYKStWxRlg-br-RfVnA2arZRdXsB2sp-3uyRrBhawGCve_fj2bSP-pAOL9PLjw4WWjwbV078aqOhg_rd1ku_lgFlvKy5-G87cNI3GONjQSt0JyekqquuxBwZNt4KUDgclrZRkYdBEb8U7-b5XXrbjidGcOvImSUYamf7ij5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee935b79a7.mp4?token=s8VSl6JAZ_LJw3dZgpL4I-Z6-W3jmoZwtQi1dW8GxBIpBevAEEs6_WEYW3KbcTJWDpvcR2NCoJU-S0KUt5HZeQ5iAErozwJmBaqbiY8GchAUZ3yuzSXHwGyoefXAhOtKpc3g_ebmxOke18gqMOw8xSVr3P2q8cVCNuQIjJkFvQ47qdbYKStWxRlg-br-RfVnA2arZRdXsB2sp-3uyRrBhawGCve_fj2bSP-pAOL9PLjw4WWjwbV078aqOhg_rd1ku_lgFlvKy5-G87cNI3GONjQSt0JyekqquuxBwZNt4KUDgclrZRkYdBEb8U7-b5XXrbjidGcOvImSUYamf7ij5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیگ حرفه‌ای برای مبارزه ربات‌‌ها هم از راه رسید| جایزه ربات برنده ۲۸۰ میلیارد تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/673103" target="_blank">📅 21:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673102">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
وقوع انفجار در اربیل عراق
🔹
هنوز جزئیات بیشتری درباره علت انفجار یا تلفات احتمالی منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/673102" target="_blank">📅 21:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673098">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c64c854.mp4?token=I2E1gd9jTUJ77oaPf97JNUlhlcTMewGWwHIPmqnQCaX4CwjyPWdz3ekxx7Let_en9KcIEp9GgJyMsKwxFNJEEOn1ib7GK1rYNbaTJsKR4b7x9DnOSR92VM64-yknBi72aOHXdwy3tfjP7qU0MNEbpxki7cHS2j_GHQb7WoWNjLg--hCUL9gYTQ2XkFQvt645psQdjjRDf2R5BQxAkyMKUYP-p3l-WzEL3TKSr-qeOTtpNJa85YMbdAYcAd3BwtkJswiK5nhvEG1tFY18GN8NgXWx6IOrwP41hLv6kd2yS5luv4CBKPmO4oTq0S-PX-7y7WmGR4A1ytYxVuy82xmH8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c64c854.mp4?token=I2E1gd9jTUJ77oaPf97JNUlhlcTMewGWwHIPmqnQCaX4CwjyPWdz3ekxx7Let_en9KcIEp9GgJyMsKwxFNJEEOn1ib7GK1rYNbaTJsKR4b7x9DnOSR92VM64-yknBi72aOHXdwy3tfjP7qU0MNEbpxki7cHS2j_GHQb7WoWNjLg--hCUL9gYTQ2XkFQvt645psQdjjRDf2R5BQxAkyMKUYP-p3l-WzEL3TKSr-qeOTtpNJa85YMbdAYcAd3BwtkJswiK5nhvEG1tFY18GN8NgXWx6IOrwP41hLv6kd2yS5luv4CBKPmO4oTq0S-PX-7y7WmGR4A1ytYxVuy82xmH8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صف طویل و بسیار شلوغ ورودی خبرنگاران به ورزشگاه مت‌لایف
🔹
به‌دلیل مشکلات در گیت‌ ورودی و بازرسی‌های طولانی، هواداران ساعت‌ها پشت در قرار گرفته‌اند!
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/673098" target="_blank">📅 21:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673097">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbQNbxWcxVcMRb7We_S9tvWIAFqZ64dOCON6zV-ApY3hLsRq0znTgTnvsammV4HsvorwuJxkjrEJ3WLSm6PaPG7rGp3SEUjjOmVyGzsPyEBWMv7j2dsXRNiyjKKloe3SounhRhAm8C1DzUNSjGwAjlNkZFTtrDjqyDmaSDosuB-2aFt9IOOHD4MxEPCBVR3S0r-gdLIgWgL6bvX3z9XWJllskBWXmPNHXPC4aUeXY1HnQHS1m_m597021nOuJcZ5YWrNbT_6byqdiM-soCPFXpPuNEd_RjVTQDENGRcgLwx0Sx99Qtu-w45Dh4kwJhzhO11jXQbRkFqYNEb1fEU_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامۀ «طبیب» شبکه سه امروز از بیمارستان شهید بقایی اهواز روی آنتن رفت؛ بیمارستانی که طی روزهای گذشته هدف حملات موشکی آمریکا قرار گرفته بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/673097" target="_blank">📅 21:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673096">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZDuwDzw_OShMyc2rXGWyJ4Tz32sr_Wl_Oqe1m7_7Kmpr_LkU9JyeswXMVONik91tD62KR4b0TMoMSi7B2jCIbJi2yoOP_Zj5nx-jhHdnGSqEgYSm6NFWbmN0WFRhXHDt-OJmdsN8pf-bKKuIRiA9j1u9v3-GTTxQdyA-78SCwwuPsP0oK6Gw9VLKyxt031Z7sF0AxjbKzkhPGiINgdF2iTF7EQH7r26iMjHjXag8KrlN9fFhPjme1KtaQyRJrQ1gpi4U0AN2zxUS4Cg4OdbLbk3IOrS0UnUWaLldzeENFwThSrQxOfd3_TlmW5Qzz9XuZXnb81jsNFG4f3-8DAXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این منطقه مهم سرنوشت جنگ را تعیین می کند/ ترامپ به سیریک حمله می کند؟
🔹
باتوجه به اهمیت فوق‌العاده سیریک برای ایران، این منطقه به یک هدف کلیدی برای آمریکا تبدیل شده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3231574</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/673096" target="_blank">📅 21:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673094">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e51ee89650.mp4?token=lAKY_TDskDUqIALmxC_USjdMKDX7439PnqZj6FKs8mHC2YJlDcx1Ek7Ga3UAZhyuYtcFw_VuyyWwCAtBvC8FI7kE-1uY3KeH13FE7PxaWdoAbFZKNzUlDj2Wi2qTXn6AkfDIKa9GC9Vu1dlGaoLUoWTTjn-tpdtAcTtpPY4hRm6nCZJg83YVBkVxJtwgpVDfvh5F-GRzs9GLpJpOXhdh4QGuFyQBoEXrVWziVJaZlW5FXEZzAaDAnJKsy75V9pnSViUITMQ8JrUpAFDsx8V4ByMk4748T-sp8R2HlW5A8rIOd5e38Qb2BSDiAahmg7yca6Jk9xFX1XyScWt5vc9LHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e51ee89650.mp4?token=lAKY_TDskDUqIALmxC_USjdMKDX7439PnqZj6FKs8mHC2YJlDcx1Ek7Ga3UAZhyuYtcFw_VuyyWwCAtBvC8FI7kE-1uY3KeH13FE7PxaWdoAbFZKNzUlDj2Wi2qTXn6AkfDIKa9GC9Vu1dlGaoLUoWTTjn-tpdtAcTtpPY4hRm6nCZJg83YVBkVxJtwgpVDfvh5F-GRzs9GLpJpOXhdh4QGuFyQBoEXrVWziVJaZlW5FXEZzAaDAnJKsy75V9pnSViUITMQ8JrUpAFDsx8V4ByMk4748T-sp8R2HlW5A8rIOd5e38Qb2BSDiAahmg7yca6Jk9xFX1XyScWt5vc9LHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: تعمیرات آب‌شیرین‌کن بونجی جاسک انجام شده و در حال حاضر مشکلی در تامین آب وجود ندارد و شرایط به حالت اولیه بازگشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/673094" target="_blank">📅 21:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673093">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ارتش کویت: حملات ایران تأسیسات متعلق به وزارت برق و آب را هدف قرار داد و باعث آتش‌سوزی و خسارات قابل توجهی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/673093" target="_blank">📅 21:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673092">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d17ba9cbb.mp4?token=X-uAnloxuMS6f2Rr8jeQgI6ASnTWUKWorrg8SRHYQPmzgTkSlFTkjCCuL5j6n5VtVthkoldRFxDEJTr3XioMEct2UKANlKfMmJJH5d1T79ApQTtu7Rd3cWjSzYgXs64D3ld4RBzu53Qt3pE_bc7udDw-iFXrxKuT3Ee_I3ETovZy02GLazMWJ6ChVo8BcEezb65hdGTiCkFxKsb7og2Ll6P9SdDMwrXlbbjchVo0Xa6V9MJ56c811UqMJ2KJGKXM9YzFXZYz2XS2mSYunxjR4vhFRc7cQtfjQkOxRTy5eKngF7_nrnGaRY3NwMeN3Fes23rvTc2Wkd4M9re_fLL0WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d17ba9cbb.mp4?token=X-uAnloxuMS6f2Rr8jeQgI6ASnTWUKWorrg8SRHYQPmzgTkSlFTkjCCuL5j6n5VtVthkoldRFxDEJTr3XioMEct2UKANlKfMmJJH5d1T79ApQTtu7Rd3cWjSzYgXs64D3ld4RBzu53Qt3pE_bc7udDw-iFXrxKuT3Ee_I3ETovZy02GLazMWJ6ChVo8BcEezb65hdGTiCkFxKsb7og2Ll6P9SdDMwrXlbbjchVo0Xa6V9MJ56c811UqMJ2KJGKXM9YzFXZYz2XS2mSYunxjR4vhFRc7cQtfjQkOxRTy5eKngF7_nrnGaRY3NwMeN3Fes23rvTc2Wkd4M9re_fLL0WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی متفاوت از طواف پیکر امام شهید بر گرد ضریح حضرت عباس(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/673092" target="_blank">📅 21:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673091">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJtxfjZHlxF-b9TYLcqTIyeooF-n6u59az4AloT70OlPKFnd5oBKUuVb30Icsh6K_adHcsJw2_OqKcI5bgy10NREkez3D3tCOL00BZtUtsqeRubnZTAnoFG1VJY_OyewUMjukI2a6r_nBXmJx9BoBObcQueYM20QEP0Kb-ENNFK3PYi8CDdeEIO1uv004zti-otTKQwyRmvbPPDaahJPpGoAU5hx4i5bW-q-6071_t27EXxD8ARnodyzq2zPtmq4uw18S3-L26rMzo-5mtFQE737ZCbek0S5SFgfIvX6x23okqfDWtUwfRQb8KCNRV-QTD4mwB990tNeq1aqU-KDMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎖️
موتورسیکلت کی‌وِی K249N
موتورسیکلتی که لذت یک سواری هیجان‌انگیز را به شما هدیه می‌دهد.
🔹
249 سی‌سی
🔹
چهار زمانه، چهار سوپاپ
🔗
برای مشاهده قیمت و سایر مشخصات فنی، روی لینک زیر کلیک نمائید:
https://l.nikrun.com/tjy
🏍️</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/673091" target="_blank">📅 21:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673090">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG9TQjBQBAFyow2o0zeLlKorAXM3UN_1agzZLE-qHXomysx9fGLPfi4JKUj1Eq2biVvGYNHwRXR43phYMdc78xYrAVg7pFwgmmTb4aVhuWoGb6dOktWPLVcFrB9Jp0V_v7gJrTawGHHfaKtfo7WoL7sNTEHz352-uf_Qc81LdlWIE4HhKsKeTz89Z0IqfPr070N2z2HP3e1Vu_jRsr3vCpnCLSxPijX1S0u4urGxYctWuN1HfFJmHFDK1YCK1jctsDbY_hF9sgT5dcUhdNTu77HnZBhoenp--fgkbP5CBGdVR1UkuHTgxNseTLOlPvKMQWcYqVIxhsqAnAym4L5GHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت از 4 هزار خانواده آسیب‌دیده جنگ رمضان با همراهی تاپ
به گزارش روابط عمومی تجارت الکترونیک پارسیان(تاپ)، مصطفی زینالی، مدیر توسعه پذیرندگان تجاری ، از نقش‌آفرینی کلیدی زیرساخت‌های فنی این شرکت در اجرای پروژه بزرگ و هوشمند حمایت از خانواده‌های آسیب‌دیده در جنگ رمضان در سطح ملی خبر داد.
در همین راستا و در قالب پروژه «کیف پول برکت»، بالغ بر 4 هزار خانواده آسیب‌دیده در جنگ رمضان، از طریق شرکت تجارت الکترونیک پارسیان و اپلیکیشن تاپ از تسهیلات بلاعوض خرید لوازم خانگی برخوردار شده‌اند.
این طرح ملی با همکاری بنیاد برکت ستاد اجرایی فرمان حضرت امام (ره)، تاکنون در مجموع 350 میلیارد تومان منابع از طریق کیف پول اپلیکیشن تاپ به هم‌وطنان آسیب‌دیده اختصاص داده است.
مشروح خبر در سایت :
👇
@akhbarefori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/673090" target="_blank">📅 21:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673088">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
قطر دست به کار شد/ ترکیه: امیدواریم در روزهای آینده خبرهای خوبی دریافت کنیم
وزیر خارجه ترکیه در گفتگو با تلویزیون قطر:
🔹
خوشحالم که می‌بینم قطر بار دیگر تلاش می‌کند تا با استفاده از تمام روش‌های سازنده و تمام کانال‌های موجود، هر کاری از دستش برمی‌آید برای حل بحران جنگ ایران و آمریکا انجام دهد.
🔹
امیدوارم در روزهای آینده خبرهای خوبی دریافت کنیم. ترکیه نیز در این مورد با قطر هماهنگی نزدیکی دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/673088" target="_blank">📅 21:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673086">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ekxq14PSwivi2pXvji4t40PczBOV0WU9syTvFPfoC5bMcg2DBTUxNAUh-fBz79PcyrCBaUYnujkb2KZQ7CSVMho_a1nbPzLnG0OG8rma9SLWHPURjM16VqwXkMdWdO38bwXJU3obWGnQyEGFVYQzpHOhnYGYPrPbs9Z5OoRuYaCqkDt2JIYkb6Ye7QZhcxWB-tabLOmv4j4qhfgLOJobK7QtiRnMtq-j4e76v6CAEVCuMRTEan8lS2gAwZUGAF9awUhXIx-Z7M7R1IMXxv95ZeDTRTHvOOI8l_TK-XWPBjJx4240e5KOpiKlUAunV5ssN2ejjCLEhc649Wvp6o4wYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریس مارتین در کنار بیژن مرتضوی، درحال تمرین برای مراسم بین دو نیمه فینال جام جهانی
🔹
ظاهراً فوتبال فقط برای بقیه نباید سیاسی باشد؛ وقتی پای آمریکای تروریست در میان است، سیاست از زمین بازی هم بیرون نمی‌رود.  #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/673086" target="_blank">📅 21:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673082">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای وزیر انرژی آمریکا: ترامپ خواهان حل‌وفصل مسالمت‌آمیز پرونده ایران است
کریس‌رایت در گفتگو با فاکس‌نیوز:
🔹
ترامپ ترجیح می‌دهد موضوع ایران از طریق یک توافق صلح‌آمیز به سرانجام برسد، اما تحقق این هدف مستلزم همکاری هر دو طرف است.
🔹
اگر ایران برای چنین توافقی آمادگی داشته باشد، این پرونده به‌صورت مسالمت‌آمیز پایان خواهد یافت. در غیر این صورت، آمریکا بدون همکاری ایران نیز به تضمین تداوم عبور و مرور دریایی از تنگه هرمز ادامه خواهد داد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/673082" target="_blank">📅 21:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673081">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94260296af.mp4?token=SUDGkkePE2HQJj6a1fjl-0U3ejSnWVSvsgeo_NzuxK-mXOgHSpoKaTDGJIpuceZr6-2ZvUgg_q0WbyKy93vK2BdavVcJ8VkLYYt-tHP0P5wEuvwk9mO40AqxFYCZlGEsNhCDE2Y8RmvB4OBt8Wk5HCeN4ZjA9Du5t0svqVwoahkMQSuwO93tXUHVEG3aHYWf1FViFExTptikvIVB3hKKwY_Z9x9oqVYYBfBp3T3ZdnqnPHzadAZbxXz9JLQYTryi8OkO4G-2bg7UQxNbG23NuYD9CKPcwk_SncjHf3mwuGKgu4Jv62DTX9y2mOdDFZJCcsKAhNgMaXMBY95jA9ZaoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94260296af.mp4?token=SUDGkkePE2HQJj6a1fjl-0U3ejSnWVSvsgeo_NzuxK-mXOgHSpoKaTDGJIpuceZr6-2ZvUgg_q0WbyKy93vK2BdavVcJ8VkLYYt-tHP0P5wEuvwk9mO40AqxFYCZlGEsNhCDE2Y8RmvB4OBt8Wk5HCeN4ZjA9Du5t0svqVwoahkMQSuwO93tXUHVEG3aHYWf1FViFExTptikvIVB3hKKwY_Z9x9oqVYYBfBp3T3ZdnqnPHzadAZbxXz9JLQYTryi8OkO4G-2bg7UQxNbG23NuYD9CKPcwk_SncjHf3mwuGKgu4Jv62DTX9y2mOdDFZJCcsKAhNgMaXMBY95jA9ZaoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: ناخدا خورشید (۱۳۶۵)
🔹
ژانر: درام، ماجراجویی، جنایی
🔹
خلاصه: اگر می‌خواهید یکی از ماندگارترین آثار تاریخ سینمای ایران را ببینید، «ناخدا خورشید» را از دست ندهید. شاهکار ناصر تقوایی، داستان ناخدایی شریف را روایت می‌کند که در تنگنای فقر و بی‌عدالتی،…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/673081" target="_blank">📅 21:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673080">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پاشنه آشیل اختلالات بانکی مشخص شد
رامیار قنبری، رئیس انجمن شرکت‌های پرداخت الکترونیک، در
#گفتگو
با خبرفوری:
🔹
معماری متمرکز سیستم بانکی در بروز اختلالات بانکی مانند پاشنه آشیل عمل می‌کند.  هر اختلال کوچکی در یک لایه، به صورت آبشاری کل سرویس‌های مالی کشور را زمین‌گیر می‌کند. در اختلالات اخیر، قطع موقت خدمات اقدامی ناگزیر در پدافند سایبری بود.
@TV_Fori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/673080" target="_blank">📅 21:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673078">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFnK_z-wSEA69iL-CwHPwplAjLPs4HBAZOhySHbfJjTvvXRHDkvd6pgVg-HeuXlJShx0TkO-cip87zWLdIpYL4h0BPkxaZFeiei6LCAG2TE06m7g_tAgv-x4tfYQj0Givdjg3khVGnYZL0CJfa0tYmeZxu_m8PHr7J3aIIO17cSqISkpFQwJiQZ9YDZslTbk6_1dNWqj-NGyLusBKrweC3bhVmK4fuwe9hiAu0YuE23Kpw9iv3tlPO5eAZcEauiOA3YH9hoAeVhUudlJJ2u1K9kRSuGFr-4zT9wH1Jj8tEgrHc6vooRyikcJ8BSj5cJo1TBTqqZ2psVEK9YtOFNuOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اردن تا کویت؛ پایگاه‌ها و منافع آمریکا در منطقه یکی‌یکی هدف موشک‌های ایرانی قرار گرفتند
@amarfact</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/673078" target="_blank">📅 20:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673077">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hW2Ipyg3ooSjS0kCx82Uf0hbDlGrTW3yC-aFEbhTmCNf372cS6OEs7FPfO0Lt0VuZVw_xxNfj6CdM5M1oQWKoPdEm5pXOM2eCMm_7gJvIKsKUPJQ6qV8Hi4zbCS-Yzx5zNaUC6dNlP94mjEKbjqSlq_7A9ySdc0PmgVw_vHQ32z0r8U6ogaS993sGNDV4gu-pOFj2EQOiKHam_3YQMtgQf7YqxeJ8eNT53kj7zESBsWf1I8TpRzyGHYjmH8WPNGuyxE4iaU_DvOJYYevFbYI5pkp3vyOeOXaFUdvkXHWACdKGPsw0tGoo_0K9Y8xIC8hYwjeXxZ2fWaUeWJSq6AVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حداکثر دمای ظهر امروز استان‌ها
🇮🇷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/673077" target="_blank">📅 20:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673073">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/673073" target="_blank">📅 20:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673070">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ffa57fa1.mp4?token=lTbl37SL_Ci9n33decJEehtdQJD3ySFo54QMtOhMw8RoUh6HDjKOkpaJ7oQ6BqNYRODCmzb0Vx_yp6GwbgHgNz68WwidF3dQ8mabDRcIyXY_SEzeY6VfKyi9HnbkNy27DvbzxBjMKPyK6vkDsVBdiB4YH5vnktwZJSHrGwF2SYhj9lrd-kf3JoIoduzkfyO3GR3_K7pCQyuB2fyJKhSM0rvl0Y5S040d42-51FVIQAFBIBjgYvB1l-fjxvz71BvQd4TxKscoYD_OMoBdUFNBiguqU2AQopF9lLkOxwQ1dcLTCaZYjEvshfc9ChtNTyzCangZN_Z6SRE0fXXnh8pYgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ffa57fa1.mp4?token=lTbl37SL_Ci9n33decJEehtdQJD3ySFo54QMtOhMw8RoUh6HDjKOkpaJ7oQ6BqNYRODCmzb0Vx_yp6GwbgHgNz68WwidF3dQ8mabDRcIyXY_SEzeY6VfKyi9HnbkNy27DvbzxBjMKPyK6vkDsVBdiB4YH5vnktwZJSHrGwF2SYhj9lrd-kf3JoIoduzkfyO3GR3_K7pCQyuB2fyJKhSM0rvl0Y5S040d42-51FVIQAFBIBjgYvB1l-fjxvz71BvQd4TxKscoYD_OMoBdUFNBiguqU2AQopF9lLkOxwQ1dcLTCaZYjEvshfc9ChtNTyzCangZN_Z6SRE0fXXnh8pYgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این چند وقت قدر هم رو بیشتر بدونیم
وحید شمسایی در مناطق جنوبی کشور: امروز ما آمدیم اینجا که بگیم ما پای کار کشوریم. هر جا که لازم باشد پای کار کشوریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/673070" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673069">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ادعای الحدث: وزیر کشور ایران فردا در اسلام‌آباد با مقام‌های ارشد و رهبران پاکستان دیدار خواهد کرد/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/673069" target="_blank">📅 20:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673068">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: خونخواهی نیازمند تشخیص علماست
احمد انارکی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
مقام معظم رهبری در بیانیه اخیر خود بر خونخواهی رهبر شهید تأکید کردند و این خونخواهی نیازمند پیوست‌های کارشناسی و تشخیص علما است و نباید آن را با قواعد بین‌المللی قیاس کرد.
🔹
مهم‌ترین اولویت کشور فعلاً اتحاد ملی و همراهی با نظام و رهبری است و باید از هرگونه اختلاف‌افکنی و تشکیک بین مردم پرهیز شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/673068" target="_blank">📅 20:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673067">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eef2a5608.mp4?token=YZFu6VpKwoZHZujEe1v6tnFR1BaEiQ-X9b6oZFC4R9y4QvhEkXl0Pg7LZDHqT0hI2iyJSyEmg8MexZa4cOriMaf9UUGGB0_wFdAvL1N7f0cOOcWvusySlHjHKnC5C_Sm4ppG1eapM8PcQrxmEth4hvmpD6G3n2CSzSbJvwVjOzVHtffcEqTa3ph74Q7rNpCUxl5NsQqRnTppTb8P4q92r24ASNCxhzv7-tgIqghCC5zLqq4Us8pa9F8joeLOZ6y_BUOQYotAh67OCj8p8nxvyIvPI9qVnO1gRzylxtC-KdHH2pCv9j3SNanTGrOzwy1PJxRCTD7HQ3VNaOc2GKrr5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eef2a5608.mp4?token=YZFu6VpKwoZHZujEe1v6tnFR1BaEiQ-X9b6oZFC4R9y4QvhEkXl0Pg7LZDHqT0hI2iyJSyEmg8MexZa4cOriMaf9UUGGB0_wFdAvL1N7f0cOOcWvusySlHjHKnC5C_Sm4ppG1eapM8PcQrxmEth4hvmpD6G3n2CSzSbJvwVjOzVHtffcEqTa3ph74Q7rNpCUxl5NsQqRnTppTb8P4q92r24ASNCxhzv7-tgIqghCC5zLqq4Us8pa9F8joeLOZ6y_BUOQYotAh67OCj8p8nxvyIvPI9qVnO1gRzylxtC-KdHH2pCv9j3SNanTGrOzwy1PJxRCTD7HQ3VNaOc2GKrr5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیلبورد معترضانه لندن علیه عینک هوشمند متا
🔹
یک بیلبورد در لندن با تکنولوژی «لنز لنتیکولار»، تبلیغ عینک هوشمند متا را با تغییر زاویه دید به هشداری علیه «نظارت» و نقض حریم خصوصی تبدیل کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/673067" target="_blank">📅 20:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673065">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
مردی که از کما بازگشت؛ روایتی تکان‌دهنده از دنیای برزخ و دستگیری آقای بی‌دست کربلا
🔹
00:17:00 نگاه ذره‌بینی نسبت به دانه‌های اشک
🔹
00:21:30 دعا و توسل مادرم به اهل بیت زیر باران
🔹
00:26:30 رؤیت بدگویی تلخ ۲ تن از همسایگان در زمان جدایی روح از بدنم
🔹
00:36:00 افراد ایستاده در صف برای جدا شدن سر از بدن
🔹
00:40:50 دست و پا زدن در باتلاق چرکین
🔹
00:47:20 روشن شدن نور امید با حضور پدر و مادر، در تاریکی مطلق
🔹
00:58:00 دست یافتن به جایگاه بهشتی با یتیم‌نوازی
🔹
01:02:10 دستگیری و شفا یافتن توسط آقای بزرگ بی‌دست
🔹
قسمت ششم (نوازش)، فصل پنجم
🔹
#تجربه‌گر
: فرهاد قائدفولادوند
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/673065" target="_blank">📅 20:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673061">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHz6MSYIVPQRP1HfHcrVvvbuUaul1a-KMfqFPFvGTh3TG8mie2Ku3thC2IeAvHN4INMfBKbP6U9pSEalwdqZ_QxfuW-wgw2dRcr8rnRobisG66uj1WCidTdOFP5pOTC9-oxJvk8zdhRAipadRV79KKhF1TU-b7oOt_LUC6at2JH7yYBxBVxQIIJ-Pv_KKW53Te2Nv3vEz1fBWJILqQenG1VLRibWF8Xl3_tcsU35uuOeBMTImxo-gOk4o1jl-jBkrAbXVcoWwmgcxtZmxhfzqWfW5SMpQh_5rqrgfTzhnx-eMSXqJs0tYMYHi8C2zI2h2TmKRgDEBLfimy62J3xKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UoZV9cRKQNd9_OPWxVwF1vJBgwa6eU1xjaCdQTOA9BmkwQo6ENBBCYUObaB38mN_rcTKcCd-vxzKCajiXm7IlxbGcGX2V_n1JT860sV0PpPvlcIS-Vk0QV3kGwGNsJv0RmxKvzopqrbXKBaCZdew_e7DSP6dcQQ0HS352HeoRcKrGmFLLLihSl-W13IoE3hIF1qRAt6C4ZIhQ3s-6H1PMFS3Szj3Jb3mom2T15-buWARvhaUnIxM_cKdbqb5tJx4rFQ4pegru87U7syDO9dFjICAc0M72M4tBP9v4yxr6hdyNXbj9n1E98ACgFRcf53NCTAFQEMZKrZvWgUBGjyBIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gAJevWlxn8zRVEanQFWVNoIfgc1DoXtXddX5C3Ki1zjbkeB038f-mBXssAoWG1binv_iIKlTy2Yc5BbB1tJsVOEYzP9WFJzDDHiii4cmaR8HHuaDKpaPjRxXfo80jLR5aKsPqeXMrlsjPaOT3WDBf4wVEseYK8RLOr6oN7q088sGCZYIU8cFcJP6VVIerBbnJuPR4gS4aaCfXKiUHL2p4OApty8pEhZ1KFRZsIIZ12Lkdy738Eeb-gdEaHBEFQADaNG1fQhU8jXkbc38ZxI0EV6y0WR6AvHMiV4XutyIKkafOSxcnjPPg3vtOKqHqhrE-OPK6lULhMOlNBju3ZAEpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انهدام یک فروند موشک کروز دشمن متجاوز در منطقه غرب کشور
روابط‌عمومی ارتش:
🔹
ساعاتی قبل یک فروند موشک کروز  دشمن متجاوز آمریکایی، با رهگیری و شلیک موفق سامانه نیروی پدافند هوایی ارتش، تحت شبکه یکپارچه پدافند هوایی در منطقه غرب کشور مورد اصابت قرار گرفت و منهدم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/673061" target="_blank">📅 20:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673059">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6519a564b3.mp4?token=PHS1eG1j4L4LOMLNC56z9DX6XHex3nEZRzJer2H1sGoe7pcQUcmjsyAIJBbv6X7dq1lLWkdzukgyMqi2jFUZ9B8rDlYDuf5EssVG7keBMZJT-j2eXfojQJRwuAjrf0gHjfH8GpzagMP-OTBc5kS_sO4KLkOTipQP3PNtCEehQlUtUGifXfh77nR6N5JJWophMMgAcdoHusf-O-UCNhSNjvzsqT23tMHpy4GRyaEb6eaHMWLb0UgubQxhHUQDW4t-S-quVLFp69nIKbBAasFwvoLyazt18jhM9QnKxFh4Z87iqznGuRtqc_3h8_-j24NZPxYzZfBNi0vd7-_0Q5xgp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6519a564b3.mp4?token=PHS1eG1j4L4LOMLNC56z9DX6XHex3nEZRzJer2H1sGoe7pcQUcmjsyAIJBbv6X7dq1lLWkdzukgyMqi2jFUZ9B8rDlYDuf5EssVG7keBMZJT-j2eXfojQJRwuAjrf0gHjfH8GpzagMP-OTBc5kS_sO4KLkOTipQP3PNtCEehQlUtUGifXfh77nR6N5JJWophMMgAcdoHusf-O-UCNhSNjvzsqT23tMHpy4GRyaEb6eaHMWLb0UgubQxhHUQDW4t-S-quVLFp69nIKbBAasFwvoLyazt18jhM9QnKxFh4Z87iqznGuRtqc_3h8_-j24NZPxYzZfBNi0vd7-_0Q5xgp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگل‌های هیرکانی در مه
🇮🇷
🔹
دارابی‌زاده
#ایران_زیبا
#اخبار_مازندران
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/673059" target="_blank">📅 20:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673053">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067baf735b.mp4?token=oFmmWEdCP4Gxco8YA9m5PLh2hrK8vNO1vfXjsmKjcTkjmof1L3nVDB45o1iaNG9ITr29M8qyA4-lb-2arGcNyH8fVsHoGC6CckB0GAJLbVWsr6et5sgQeW8aa-4ZCHSEcPEnqqxogD_KrR3R0U6qnkaGn8Lgy4bbFLiHLua_qxO2tCPPTARDa7kVdKZmDi9npaS5vDxARXcW7_mlJRD39Lq7l_K5DjRpcqhUTSRE1MIFChbASmFvFFvhQZh2sTn8IsuODe8nmGVhYfI3t8lac1ofqBRTNDV1V78jqDdF2g5VIpTTMNj8ussm4lb2svi7q6xgMMyXmwQSnqSJB_UeSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067baf735b.mp4?token=oFmmWEdCP4Gxco8YA9m5PLh2hrK8vNO1vfXjsmKjcTkjmof1L3nVDB45o1iaNG9ITr29M8qyA4-lb-2arGcNyH8fVsHoGC6CckB0GAJLbVWsr6et5sgQeW8aa-4ZCHSEcPEnqqxogD_KrR3R0U6qnkaGn8Lgy4bbFLiHLua_qxO2tCPPTARDa7kVdKZmDi9npaS5vDxARXcW7_mlJRD39Lq7l_K5DjRpcqhUTSRE1MIFChbASmFvFFvhQZh2sTn8IsuODe8nmGVhYfI3t8lac1ofqBRTNDV1V78jqDdF2g5VIpTTMNj8ussm4lb2svi7q6xgMMyXmwQSnqSJB_UeSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان خدمت
🔹
هفت سرباز نیروی زمینی ارتش، در حمله موشکی به پادگان بمپور ایرانشهر به شهادت رسیدند. این حمله که محل استقرار سربازان را هدف قرار داد، شماری از نیروها را نیز مجروح کرد و بار دیگر داغ جنگ را بر دل خانواده‌های ایرانی نشاند. نیروی زمینی ارتش ضمن…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/673053" target="_blank">📅 20:11 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
