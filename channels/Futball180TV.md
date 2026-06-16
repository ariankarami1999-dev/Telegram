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
<img src="https://cdn5.telesco.pe/file/UBNIVpxf4FvS2rIN6QVoufTh_hwWFV9w9g0GpKpalLqYCMZwloDseJscb0f--MArqt5Yq2DYNeFQXq50mppWj0BrcpfnsPElqi-ZbomdYoELk_0nUXRbylUjLT41ka_Yedtpj8FmUTd4Ema1zOd7RsfJ72PdGsK2p_NgVJpKuE-5lwNjywTjr4fYRM1AJK_QFqetUonKFtJlW3Ean20XeJoA-NOnDtS6_4UewVd0XTxhIKgq78koBs23bbdVtKoVEhh0FuFkwjJgoG5DZU9KwQiIpZHqL4Ox8Sqp37VxmyQKuycyrYfFGp4wh0XG4l3H9y9QkODK8OU-hnWYDfb2DA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 607K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 21:43:22</div>
<hr>

<div class="tg-post" id="msg-93679">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Poy6prfORc_D1wN23bELEFoGbjcHnZ10f7fT8W1hU4w7wsr7ZIWEH1sceBjFntSsJlrBvWKHZggAH6NOUrDuahiRLSPQuHgvT5wH481-5uJoQkBVOlf0TUAAXGHUrCD3wNadS3WsPyMMsQ7PS2eXaXjx4eh0XI88O_MO3PZmT6GtSN35RcUwZcejgIgQH9QjX24S5nTLzMScuDdj8PiI47DMrdx-e36SMsmX7RBM6MFkCp4kMtN0f4Z6soSN3tvr6Ip7zwBMDgGFTsKRka9Myw27MY9rKUKsaBMhmukJ2iVqy3cMXMOmNVNKCT3h4kk8kug0Tn2ZG9-20JBOF_ElIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
سادیو مانه قبل از بازی سنگال مقابل فرانسه:
«راستش حس نمی‌کنم این یک بازی در جام جهانی است و بیشتر شبیه یک بازی در جام ملت‌های آفریقا است.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/93679" target="_blank">📅 21:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93678">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU9SdDWb49p90RfE6hmVFSHdYiotc5aSvS7JJXiXTuBf77lZ0O0dAQ6zNDreFiY26B1Fvt1-9rMKJgrI0OZZX_O9qJXDs_KQTXgd1HjleuvjWZyA73Db-xeXGTmzJCxQVi4_CmMOBqWiobyy49ZxgZs2k-MDNlHaKR6Xxl5YuH9QBvLrhQ180Wn9HlPnKeSWHT1cJOzgHiGWsw5DhcdFFLnWOKvtW4-groIBV9AkK9GrJDPPp23sgWD6nG0RGd9tFuFgfsvBie5gVxtgDen9SN77aqgOQTJHJrt9FzXK23AMMAPUn9e8r1zxfuv9c8ODt5gRtIgjr4QGIVNBgSXMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نشریه‌ معتبر ESPN:
علیرضا فغانی که‌ داور دیدار امشب سنگال و فرانسه‌ است اصلی‌ترین گزینه فیفا برای سوت زدن دیدار فینال جام جهانی ست، و اگر اتفاق خاصی‌ رخ ندهد علیرضا فغانی فینال رو سوت خواهد زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/93678" target="_blank">📅 21:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93677">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaFSRjNNP8iNOQam-oDkyDNtwoZiUHJ3awpDiz2wrnxEyqs18yMRBh2qG1ulMtQWYDiahvdqTXLE3cvzqRJdQ0QmRdu4YDB9y9fJhlZysZr9RogelyGtUHLplUl98v0Ue9mqE60FI4XMC8hBdWfYfohsLAakGF_1OGRT8h8fkBniMfydtiWaPOrUt00-dSEAVy4BBeV2pJEe7-EYCwPhzKZ97nNE9-NorWaChleAX6ksAgm2kolE8GZotCiUHkjE0giN3lBco-0G_PZKjSpVpTriurt63dmiB7D_l9g1SmHPL6lJKKJL4dM_uwkcd50j5jdwfa1Z44PgQxhYL0uy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار هم بالاخره به تمرینات برزیل برگشت
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/93677" target="_blank">📅 21:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93676">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baa7c65311.mp4?token=JoH7At80ZXyf2UhcvXpcUfJJRcpe6E9ePmiYO-ygxTxqs_igxEhifw3UrnQ6bffO4I87RldfzmaEThD2wJmgz77e2sZmOOsG3qSc8erJj6FdJerQ-2S2pRwrRE7_IhEMYbg5Fv89N7ZqIUpxjcf4h_xyvpJEi44oHaFdwWW60jQdRJUKsz6aCmvmUJV5vwrOXSv9hT-Stb54Paf8xTiRpfTy1QDZGSYaxXgNXE2E0WIzM2Egv5_K-1SaKWlT9jtEC5EFqg-vjHipInFj1K6uQ-NitohCUsqXOEw6v65lhoKt7PK-keTFKz4NHYo49ZsMqbFoSZE2LDkfK3NeSOInYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baa7c65311.mp4?token=JoH7At80ZXyf2UhcvXpcUfJJRcpe6E9ePmiYO-ygxTxqs_igxEhifw3UrnQ6bffO4I87RldfzmaEThD2wJmgz77e2sZmOOsG3qSc8erJj6FdJerQ-2S2pRwrRE7_IhEMYbg5Fv89N7ZqIUpxjcf4h_xyvpJEi44oHaFdwWW60jQdRJUKsz6aCmvmUJV5vwrOXSv9hT-Stb54Paf8xTiRpfTy1QDZGSYaxXgNXE2E0WIzM2Egv5_K-1SaKWlT9jtEC5EFqg-vjHipInFj1K6uQ-NitohCUsqXOEw6v65lhoKt7PK-keTFKz4NHYo49ZsMqbFoSZE2LDkfK3NeSOInYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط سم جدید طرف رو ببینید که مشکلات تیم ملی اسپانیا رو براتون حل کرده
🌟
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/93676" target="_blank">📅 21:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93675">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحامیان جبهه اصلاحات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx84ZjWErqitjUbsrT2ioe_QGo77VVNTJRFmF3RWsSEuZhFjDnMBP5jXT33fOYcIGsn8QkyAuau5zzpfWL8JfgPk_OO2DNE5-vOUUqaYbDQJV6uMHmSORlnVx7E3X0i2iEeeKXDieJD6ddWoa-ySlUYitWEEbnWDM--VgRKhmbwFP_53iCNrSB8ifR1Lo7336ksSN-xkK1QlEG11PXBMdIN5Gcti6NxsbQ3Wy_Wk86mQa4a44jZhuiEn5qHqq4jWQzNj2OoPTgYnWkODcgwioO85ILl_QIeF1OgKKxVcfGFKdnEgwg13w-YAryyKf7iHTVf7ncD2-_EP1cw9g_LsjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرح!
@iranwprldnews</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/93675" target="_blank">📅 21:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93674">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-kQrjyBfwoI36M-yE986pRnp-TcDjO6hRiytYB3JNnDRVgrqzHEc9bNYiIHOWKqCTkhWOVCuWIMtmRfACXMWe138BaVYo3I2bkJo42r75aq55g9gzIsNPQhq7rOscOI-fWlWrMLsfR9zUK60ELDJ0zUb4QUW7l1XCwpvoJLSeP1equjgoT5gBJ_wMpdf6wzynt5cn50I7Q_K5hubRORyaLUNR9ivnLMIXhOPN7IqLIZINj51oAgXyagBIo5eVnuJVWYHuSXBZwPmuTsJIGxh1X28Tage_r05c_LSr3AW9ZWZQwhlMvwle4YRSJj2uQnVEmEVcziBxpfki2abpnBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
؛ منچسترسیتی با الیوت اندرسون به توافق دست یافت و حالا مذاکرات با ناتینگهام برای تکمیل قرارداد درحال انجام است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/93674" target="_blank">📅 21:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93673">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4x_mkBzWhdTWeXgCARZYCCAknDQ_F_Zr8DvqkbyplQ9yVWjxaQJWY_OZ36T258EikCzfTfxq7gHqaNxW59I713XlAUg4d4u6SQN19YXq1c0Ld8pb2xlcBfvlg_b4TbVwI3LSWiTUO0laLRZ-GDYA2_x3eR2cbiacc6TY_IhSCOcpEl6ZoJTA6jLWzyPmeeUwmNy_JoijaCuW2G9HeCxU-P7t2qjhDt5PodBs09DGDcDVZ_zxHdsGWkuwIpWBSuofcyzbaZL_LfIOe5rAkjnRy3XGJuWzoQps-QIUgBlu2lGrYXcIsX9rsWyW5R7_DCVTs4q0YbV8SI0M74TuZWjSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
امباپه امشب نود و نهمین بازی ملی خودش رو برای فرانسه مقابل سنگال انجام خواهد داد
:
🔝
🤯
96 مشارکت در گلزنی
⚽️
56 گل
⚽
40 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/93673" target="_blank">📅 21:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93672">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIQAqUJNcGrSOi9GnOlF_M3Dxe_c5u-r1oxexiWpBBnqT5YULrp20qkVrBJ3R07YcTL5-62pXy0uzWm_3V-hV5Mns3_pCADIgXIFQ1menDElyINv5lZUF2hRYqbg-FEk5N_fpA6iCFuS-yyR7c0D6RVgIpzJehEXckMKNDMNNcXM_LgvXA4mj1eoTthEguN68xCxJZ1vvVLbbqAPnqm_rvhizJul5vIqOD5BDRwDqM241gqyPFpO4i_3sbiF01NC4ROzLT1T278sQC1Cg91lg3_VCvUP7xxufxGlJqvGdnkhPfK5D8e8cr60uDkIxbx_oqs5EGaX6wxb3rzq-R8ZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب رسمی فرانسه مقابل سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/93672" target="_blank">📅 21:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93671">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWamgFwCSPqOgWC3b4X7C3NT78PAqOjvD1fYgaoLsb_IptrGZXxtqB4N0mLUQGCU7N8PBvsSfDiE2snGpWXf37TXqeC0Amocz68Gu4gPJH6klMEdNySg7T9RlNPxEzvQEmrDgQqm_fd85DAjPRkzmTAtkyml1KuL6V6rqOvieBqv9LfJeSC2zGApTLp9HB6DTuiEgN75eG0KTbkNz3FVB6AuDsLTgoHoOh4ypQdJSCiwa3aa06HpbCCLBu_yY3VCKdr9fHO7rqQwcxvYu29Ysy-J9FORLKfeo8kZAl3e-JjShbZv4BqLDBpXE3Fv1vEloGUhxjOc9iPlK317TPTrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب رسمی فرانسه مقابل سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/93671" target="_blank">📅 21:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93670">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNqBvNVfX7DSDgBsWuD3jjvvhqP4eND0JGXOzcpeIJGFyG-hPFZ3K_yGhwt8-wTbfEPdljIrGRk05qImJDXYUBBKPwaDBYh3wxooTiDRYE_nvpgRyXgC6OOXAVdM4Lc1OMSeLVGul4c14piZhmxGZbce6k2zkBm6CjQVUY-gYgKzZBI21Q36mTx1tM2kF98EfL1itxokTadAWVup8tmG9G1OFKKXvYpdTSTCvcsMyYp7L9JvD2XMUQQ1aEzTuZnpMiNPnOzPk0KSw6LTuVaDy25PoYaeBzB9ziU8ZpG-rGLEv5vLsSH_KJ3LSNvlkN8QUuIRjkEzQOCK0SWuFgDW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب رسمی فرانسه مقابل سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/93670" target="_blank">📅 21:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93669">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TiqC7n6AMnt7vwy4Y59_Thh3wF44G8WPYtdf-0-9xL24hxkKO-gLVr4w9R6v133tkHtFZ8E-UWOzHDa4Hnkpcp7tCwjoo1XfZGSrSOIohb3Jg7xeIaYfBjMndvjM51Q_m-A4-oLebOeTLnrQ1fYXjRrEui_o2todiCB9cbWGaiOOpiaR6LNtyhZUizkPsKD41PtkS68pW0zk30AaWSbwWxLmW_5Guf8b_e2h9iJ61M6gclgsQ8WslRDyyGwZoqX1m40z8w9hI3amWbdjYOw4J8oz0TBu09-vA8AVJt0m7McYojfovVBNIzFAG9-i6YvCNuV671qZv6Y0DSdS_PbJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚠️
🇪🇸
آقا پشماااام
🤣
🤭
🚫
✔️
این هوادار اونلی‌فنز معروف اسپانیایی قول داده از این به بعد به ازای هرگل اسپانیا یه عکس یا فیلم رایگان از خودش آپلود کنه
🔹
🔞
💧
🔝
👅
🏆
عکس جام جهانی قبل که خیلی سوژه شد رو داخل لینک پایین گذاشتم
👀
💥
🫦
🖥
🔞
https://t.me/FoootyHub_Bot?start=VjSpmD5b
💧
⚠️
🚨
🚨
بدووو عکسو نگاااه کن تا پاکش نکردم
🗑
❌
☝️</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/93669" target="_blank">📅 21:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93667">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TrSL0A8zECJw3aGnoeGZ2A28E-hcBPo1VdSVvxd00EIkvigF-IWHLU4l7Qej01HbULLiBGzz7mzQ20ZM_pHB0VWOwsbXP4yUDC-sgm8cn9T5YEZsKZV8yuz5XpJFZycvgP2cuth_464c-3KNtfJCeAqSt2Nuc5LZT0bbpmo5vSZZFCp8yvLB7ZDU37pOcylQpq1LnJLLzi37ATmoUHeF9KTERfejhTC74hiQUJqvn8tXI7VJzBWtrB0my8Jf9YpFxpQyYhpz31l9Mj5mtpe7iNlVcQl3JiosdF8mpfxjAhV6ysFeIJT7pEGouABE26JKJXLllRAHGRXH_X18_Wtb0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOHHhxWvTsV8CCR1tCuO9U6Dwbp1pSKfQj9lS_026ReWBfKIF0Wi0aso16bkEs8nGx4C7-uH62QzlM5Ck4XIle5muPLHq-PDWqEci5RceKEXHkR2BYPNF8g2Q_RLtZKgd0SFeMzVxCqCGUL46CMQtCtwT0xsY6pE08bUavFE4dA58DmkTWcLuWqer8GJgnl3_K00zCwfWByq_AoXNvIz4U_svK_irdNNdynlreyxbyvJWkCt1auLy9nGK51wz1hBsdwH2Ekp9tnK6yZMyapnOEbO1fk4uXgclRiF6TpOCt7bsa9sHIxzg-pcZuhyRese9E0g2QvgeZyAS49oKohp_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جاشوا کیمیش: «دیروز در زمین تمرین یک مار سمی دیدیم. در آلمان چنین حیوانات خطرناکی وجود ندارد، اما اینجا هر لحظه ممکن است روی یکی از آن‌ها پا بگذاریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/93667" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93666">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpxgsvDfVA0E7gIAl9BgB3J0aEOWdo8pSr_JZxbDrXegQPWsXeEu_cfxNpWQwdp59ivGF27LI99ezHOq_uOp2pNYin_FiiBaUo2sd-riadGVtBbAndob3Y5QH6QMZq6R7uM3OGn4yCUoYmGTRLy0wWFLKaddQWSGz5EhmXIFDFudaY-tgGNBp7GlEfvcc7KcUVFjulW6pG3DmOp_WuPRtL9HfzSU-qLKlNSjuM8JwbZo1Er7fG4NJn8zolkJbu62s0hjLHKeISMaVX6C_olcb8dkNdNum5mVLFjCfWjEezGKNecwtoUoi9BQImyK25u8thYyDVrn_ippNZziZRcepA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فووووووری
؛ اسکای‌اسپورت: فلیکس انمچا ستاره تیم‌ملی آلمان مورد توجه رئال‌مادرید و ژوزه مورینیو قرار گرفته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/93666" target="_blank">📅 20:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93665">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a295b95196.mp4?token=ne35GPzToioSfe21L5IAP5l34ombYHactZ2QkWBts-jy18ERr1ZSgkawWTY26QP9QxL0-TPZDkohGN_v0s8_ECXF3Pc2RBGROqpqeh7CLBSIGE6cd00Q4Tz4jMKoXakI6fk44lc-ypNsDnd0auo3CrwtVhfOIVa1pKWALIRCCi1nyidPHSKlWNf8zuP5AUXMF0ZVFcC6vxXbxZ1b_6YgXORp2j_k1Izlze6jHF60W8AKEUS7TrfeQCsR9jH9cMdZORMHLoIiwJ1fFvpWHfSf2WuZgPEnmr1D4w4KFnK0x0Rx0xBXYlDKuLQ6a1_T90HF2dGeVGZZAuZ0bUzzJCdGvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a295b95196.mp4?token=ne35GPzToioSfe21L5IAP5l34ombYHactZ2QkWBts-jy18ERr1ZSgkawWTY26QP9QxL0-TPZDkohGN_v0s8_ECXF3Pc2RBGROqpqeh7CLBSIGE6cd00Q4Tz4jMKoXakI6fk44lc-ypNsDnd0auo3CrwtVhfOIVa1pKWALIRCCi1nyidPHSKlWNf8zuP5AUXMF0ZVFcC6vxXbxZ1b_6YgXORp2j_k1Izlze6jHF60W8AKEUS7TrfeQCsR9jH9cMdZORMHLoIiwJ1fFvpWHfSf2WuZgPEnmr1D4w4KFnK0x0Rx0xBXYlDKuLQ6a1_T90HF2dGeVGZZAuZ0bUzzJCdGvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇫🇷
پل‌پوگبا قبل بازی امشب فرانسه اینجوری بازیکنان کشورش رو سوپرایز کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/93665" target="_blank">📅 20:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93664">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BS3Rub1-cGv6AefqNXwuFeC2D4c0JaxVamx63alVfFPaF23LdQ8Un6rxC57HI2VCUZe9RouhXtANOx62U1jzsMw50iLu97fCf7YmlPlbz3TSnNc4anhcNphtviWR_wcb-olyNXxcULdC_XTHChuweJNc6kDf9BnDdm9XmMXVVXf6wLRQWJ6YcUlS_MsQ7dPo6ykELKRC0ckXsnqoRuFAOjunA4sz_bHjTSSWErI_apkPux83V6rPj3X7qnUnlACdh3BdjcR-hVG1YdR-dFNaHeM6bP5zZ9yPkhN7nzoIjHkH4auqdiC3kFm6RpVHu859OKNIBagUaOeD9O2YXdhGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
استوک‌های لامین‌یامال در جام‌جهانی با پرچم گینه‌ استوایی و مراکش که برای احترام به پدر و مادرش هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/93664" target="_blank">📅 20:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93663">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab33a3bc9a.mp4?token=FQHzMm34THCGFc3wKgcbTCTXM2FsDwE0gOW5qTQGb9CzxNHIa-PRihd9xkC9UrkrlXVCnWownJ2doslU06_Htsb2MSy40wH2J55POnfL7yrUKBcDfHutXr4bP_PNU9n7yvQnu8Qu9Otn_KfndXk4NYTrrxC8jWQuZaa79v1lXsLJEXykFrFTjwCc7cOlSH4iR30CRXKZE0STLsCNIxsX2Wf4BlDU1bulZpc4nqgQOXrkHA3QE2J8bbcryXstuW7fobtmeflGmAakaGKaDAkJM5MoqUnJ7KDcjYB2Oh80GGMefMvxkJ8i7bXvPP4M5l5V5vAYTku0DvOrk6OneoyGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab33a3bc9a.mp4?token=FQHzMm34THCGFc3wKgcbTCTXM2FsDwE0gOW5qTQGb9CzxNHIa-PRihd9xkC9UrkrlXVCnWownJ2doslU06_Htsb2MSy40wH2J55POnfL7yrUKBcDfHutXr4bP_PNU9n7yvQnu8Qu9Otn_KfndXk4NYTrrxC8jWQuZaa79v1lXsLJEXykFrFTjwCc7cOlSH4iR30CRXKZE0STLsCNIxsX2Wf4BlDU1bulZpc4nqgQOXrkHA3QE2J8bbcryXstuW7fobtmeflGmAakaGKaDAkJM5MoqUnJ7KDcjYB2Oh80GGMefMvxkJ8i7bXvPP4M5l5V5vAYTku0DvOrk6OneoyGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇬
ناراحتی محمدصلاح  از تعویض مقابل بلژیک که در رسانه‌های مصری جنجالی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/93663" target="_blank">📅 20:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93662">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7qxhu3KxA2FBMn_uvkKekjROgBXktFbx8M4tTHh_q5OI7e05vAJlexswTPIX5Z_qeuERaFoU6q6A6ZvJJ35aFjzCJQCvu4rpefYtSUirLu71GwMX1FLFaRVi76q98IQVHYxWLpcGH71fltqQC32pLmUcigTW6GCmlUddQsJ71V5Q86HdhYBDOxMsZ6dyTlTLzA2Qs1-CidRPIPjKWHUCVU-YFV3YNb7i4VgTU3GIwRkJY5jTd6JsCyUYcesmIRM5fHLXDBItVhn_gFYrm2536OAsbSp6uQwCzHWRXHqre8ualE2vYjooqvYd-fxyp_LYfYDol-dF9D_MFTAM6NZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
🆚
🇫🇷
۲۶ خرداد
🗓️
۲۲:۳۰
⏰
فرانسه
🆚
سنگال
📌
دو تیم پرانگیزه از دو قاره متفاوت
؛
جایی که یکی با تجربه و ستاره‌های پرشمار برای تثبیت قدرت وارد میدان می‌شود و دیگری با انگیزه بالا و روحیه جنگندگی به دنبال رقم زدن یک شگفتی بزرگ است.
⚽
🔥
فرانسه، نایب‌قهرمان دوره قبل و یکی از مدعیان اصلی قهرمانی با ترکیبی از ستارگان بزرگ و کیفیت فردی بالا
در مقابل
سنگال، یکی از قدرتمندترین تیم‌های قاره آفریقا با بازیکنان فیزیکی، سرعتی و روحیه جنگنده که همیشه خطرناک ظاهر می‌شود.
🚀
⚡️
آیا فرانسه می‌تواند مسیر قهرمانی را محکم آغاز کند؟
یا سنگال با قدرت و انگیزه خود، یکی از شگفتی‌های بزرگ جام را رقم می‌زند؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/93662" target="_blank">📅 20:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93661">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4yYjoXfpiHF3uhDt6-0haWLmcuDaN_JLeu7_OmE6la8bzGoHnibAksqgex-U6qrTjEFiNdbrEEIsPE6ErMrZwjq01dmc2tRR-M5HTQaKdA__5LusBXPD0W8ORgjS2zbdCQSXTM-e4WenCm1k2T4AVF3gJHv44w-UeVM_pTFPcMYtU1qeLwkxsHCIj8ycIMuF1VvSlSFkJwn0UMvo0OYlXR-LGbP729aFHX5uml0qqZ19cIBfmAlzaJ1sce0NAIuzXshNbwPzR5FMOe3W_gLolovBgfB0FBk9G2HZ_j7YGQNh-e7xZHbHIgvTtk0qT-bgbalQCGeXzHzh6Ni5TRTpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
ورزشگاه بازی دیشب مصر و بلژیک واسه خیلیا آشنا بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/93661" target="_blank">📅 20:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93660">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA-iYr9jAsPN2PdvPyUoGoHOnpecF4Z8Rmg8RMfjZVD8Cenr2-fPKMeGqvHPLrRtbuTlnyn5Er-eaTjI8UFVrcy-42MPWNvIKpuHej95XGv8KZM9-EW4EQiczRQBOMUZ0GHCNIWm1IG_vq8EUA3DvGD_Paan_URUKQQlPfhOpesyfYdJ2-qpkZUrHPnzTlmHg3p-DxIMosjn094uZAl0aF-7VqM2N-QFGO2PPCsEJWep_ieTx4xE6K1K7fXaWHBhCgFs3NPdhUnLFUuyOYm3zk78r0okmqeNdHSbmh7qwW2neSS6Kw1kElM4ya-Xrj_VJhFyuwTdZ0k4vyuzpmMnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
بازگشت نیمار به تمرینات برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/93660" target="_blank">📅 20:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93659">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6713aa8d1d.mp4?token=Ia6voMxKUGSxcR4SVbh15uSRukjDzSGoEMc5uLgruoHW4q9U3Bn8SUJXdTZe9eUzhOJjRxAljDZuzNbCQaycYti-g6to4FLQn9m_EcrYta8_O9wHMJ0wK0rz8YsDurx1bxZQKIvuE-v5HigKkXBver9e8NG-1XKNgoIHmk5eu001WKVufejIFzUJRS3qU16-HSr-BUkvLVq85besH3oRyCXtOcE6Bj6xRPni0o-RHwzJV_eTF2M2x0GZy8MG4GvgQgLcdYxQnh4wAz3j9ezUesU0KAN8_8ecZmimTt4NRuIyDmJJACB6sCv5ZUmeWgK8hEHOfc8Pz_wjePt8gdohhYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6713aa8d1d.mp4?token=Ia6voMxKUGSxcR4SVbh15uSRukjDzSGoEMc5uLgruoHW4q9U3Bn8SUJXdTZe9eUzhOJjRxAljDZuzNbCQaycYti-g6to4FLQn9m_EcrYta8_O9wHMJ0wK0rz8YsDurx1bxZQKIvuE-v5HigKkXBver9e8NG-1XKNgoIHmk5eu001WKVufejIFzUJRS3qU16-HSr-BUkvLVq85besH3oRyCXtOcE6Bj6xRPni0o-RHwzJV_eTF2M2x0GZy8MG4GvgQgLcdYxQnh4wAz3j9ezUesU0KAN8_8ecZmimTt4NRuIyDmJJACB6sCv5ZUmeWgK8hEHOfc8Pz_wjePt8gdohhYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
✔️
🏆
وقتی زبان فارسی در قلب لس‌آنجلس درخشید. نمایش شعار فیفا به زبان فارسی روی نمایشگر ورزشگاه سوفی و طنین صدای شیرین فارسی در این استادیوم باشکوه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/93659" target="_blank">📅 20:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93658">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxpwyNKP6_R7y04BeqWq5exMGRzxCRz98hSHhd9kDpZWhmyXY7xqcAD12J_6Vh3X80J93CY9K9HpgMeaNL0hNgy9X_N906DY4abpxwXEIPcGg42aEI-0V0P_q4qOr-SXonezg2v-FBiXKd5LPvB_-mP-phRqKysM08DjJQk5hHhRLBf4LGSA7APn0P3ZqAk_zGQ53C8v9rSXqVy2wb3EGIUgCy3oVQsXXdXqDzJS_rfJUXoUNPIvHiMK9b_SPRj1HGBMsWzIQJXPTgMC3ET7NoLMHKgeBWR2lmrXVf8trQdfiD-0HsYRPFTIIG4UokiVuzxu_5dNI0mpcd8DvogM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
جان اسنو از خوبای طرفدارا مراکش در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/93658" target="_blank">📅 19:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93657">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🇵🇹
#فووووری
؛ بن‌جیکوبز: روبرتو مارتینز سرمربی پرتغال پس از جام‌جهانی از سرمربیگری این کشور کنار خواهد رفت. مارتینز علاقه دارد که در پریمیرلیگ به فعالیت خود ادامه دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/93657" target="_blank">📅 19:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93656">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDwz7j49Y4cQg-srlTBYMHfhXHSB1ncVDhNFv2Oe97cD9dW4-haoWFBdYvFMTk95qd75XB2E7WmqkhQcLBoPwuVV9s4sWQnNUmn4cCMxZMr0hJbWxGgN2RD-tzcXog8Ilm_K5yZo-qVaigEHT6J0vRVvxI47KuRtmNDJgF4ENjDWyby81bYc8n_aOHpIA7Xe9DcFdXJ-Z7uru3qZQ75SHQzFGBmG_bBl7XZrs-2NXRwRz96-K_2xkltzMtptPhruffqvfkI3dnvk9L48QoM-Zz-T_4Xn_NALSLpjXRhBPrfPKwURV81fTLmDxp5VocOHHCSaFJ8Hd1jWJZ5sZ5oCRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#رسمی
؛ آموریم سرمربی تیم‌میلان شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/93656" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93655">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f3c97c7e4.mp4?token=FWWx2mAV5Bm99Quh5jchiJkLp6obGfXmhMOsPsoxsiHfkLRf4OOwVaNjvWvI-XvL6VqGz7Y3zT88LKT9YnTtP1XJj-11v9lsjEab3BaPsBkD3TreXGnlDTJdvX-y48KLzDi6ShQhjnrL4rdMRIhw0IUeb-b4vv_xVeM_3zkHgssjn3sVdXNqzaFaknpkL9xJLqmH3ETNOIg-xBCa-XupJeNpkAEval06HywdkyF3UY3Ow0Fjxaa_wcQUGFpjPoWSe0nvy091Q4QJpjNJNPXERZaeNOE3pm7zPmvXMsUD4QAHdfvm0kDxSeQeERyHi2kQZ6yoCQZghF3dO8jm4Zg_zIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f3c97c7e4.mp4?token=FWWx2mAV5Bm99Quh5jchiJkLp6obGfXmhMOsPsoxsiHfkLRf4OOwVaNjvWvI-XvL6VqGz7Y3zT88LKT9YnTtP1XJj-11v9lsjEab3BaPsBkD3TreXGnlDTJdvX-y48KLzDi6ShQhjnrL4rdMRIhw0IUeb-b4vv_xVeM_3zkHgssjn3sVdXNqzaFaknpkL9xJLqmH3ETNOIg-xBCa-XupJeNpkAEval06HywdkyF3UY3Ow0Fjxaa_wcQUGFpjPoWSe0nvy091Q4QJpjNJNPXERZaeNOE3pm7zPmvXMsUD4QAHdfvm0kDxSeQeERyHi2kQZ6yoCQZghF3dO8jm4Zg_zIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
همچنان از درگیری آرژانتین و الجزایر که یه وضعیت فوق‌کیری رو وسط آمریکا ساختن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/93655" target="_blank">📅 19:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93654">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkipDYYlU19Rd5gD5K5Rd6pC1V7ILmc0xIjsB1XbL_dsxAOt_dLHdK3X6_0er-1K6vZHQv7HIeFKopNP85TlflRBkrS_Sv_SnKTHYgLgrmH6pnSPdtbKmlXYZGS1AjLBm0smuAoYyFQAmgBvVDwQGUJjyLVNO72nuSOpVtHHi8i1rHxv813rfCsgX5DLL-4R1m95n_c3q5h43iwuxb5tzbaPrPAqRLUs7bDdi4wK58LL9zv3EmtlJZoAONXzfHhWyZew6nUxPmntlkRMIN5r50QC4lEQwjNV_zR_uq6arjXjhGGqtyeVaSdsovlPMXBrFhYXoZ8UkhemQsGSDb0UWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شات جدید از درگیری بین الجزایری ها و آرژانتینی ها در میدان تایمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/93654" target="_blank">📅 19:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93653">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🔵
گلوبو برزیل: الهلال قصد جذب رافینیا رو داره و میخواد شانسشو برای جذب این بازیکن امتحان کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/93653" target="_blank">📅 19:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93652">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91abdfa63.mp4?token=M24oqolXUXqybr5H6DbXgQ_eUvBjy2LBAz8QpOsTODsd8QhUSBk4NENvNKqV_lRpufseJKTX-8zqGWM2W2CG4eDdhRGBj_4SxjiK1MsaHZz4RCEOS807ab9zp7_96GbCeBfwjQE2OQi6iAEUVofYrVoCjKZ2Q3cd9rIdcXXIGVmKeX11hwDLGpLwO0w2rOyZ7leEtdQ3FDlJloF7zsqtphWw1Y-esE32ccHMM4Zjezme-307k1EHu-fd9P9iTgNutso0jQ0srJEjg9WA7AgYjJwx59qQ1BbDZrJuyCGuhx79Heu8c9KsafoMviPJdIshKKsfcdqcJ25wfDGAaNTgYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91abdfa63.mp4?token=M24oqolXUXqybr5H6DbXgQ_eUvBjy2LBAz8QpOsTODsd8QhUSBk4NENvNKqV_lRpufseJKTX-8zqGWM2W2CG4eDdhRGBj_4SxjiK1MsaHZz4RCEOS807ab9zp7_96GbCeBfwjQE2OQi6iAEUVofYrVoCjKZ2Q3cd9rIdcXXIGVmKeX11hwDLGpLwO0w2rOyZ7leEtdQ3FDlJloF7zsqtphWw1Y-esE32ccHMM4Zjezme-307k1EHu-fd9P9iTgNutso0jQ0srJEjg9WA7AgYjJwx59qQ1BbDZrJuyCGuhx79Heu8c9KsafoMviPJdIshKKsfcdqcJ25wfDGAaNTgYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
🇦🇷
🇩🇿
درگیری شدید هواداران الجزایر و آرژانتین در آستانه بازی بامداد فردا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/93652" target="_blank">📅 19:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93651">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7_X6FMapp24TFozvEih0PU7HFGthwu6bH4B8FhSQy0R3LPQEdg8njJ3H7i5_FVYQ_BNs6WyKPAwOCa8FnOjvZlLGutHJZr2oVrOYmBS5N1lP49flnYeIRNiDVq2ArYaNhIF3IRr-1ESNEmULo4350vMWL6cLE_cpP628oC3_ycdoz6aGJZWNn_uFrka37k6pOslNU2Un7Lx-4j2dgWLEPP2vD8aMRVAbz4pvEi9cJLx2_3Syt7hjSjF3_EZxqrVoONG-GfPFhQ7QLVA3IoWybdEeEJ3OnDb7HUd_Z4kQQC1oZwDwjLy2eH6xn2f31sKELI84mn30OBLPVoJzf3IBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🏆
۳ بازیکن از فهرست فرانسه دارای اصالت کامل فرانسوی (پدر + مادر) از مجموع ۲۶ بازیکن فهرست هستند:
—
آدرین رابیو
🇫🇷
🇫🇷
— رابین ریسر
🇫🇷
🇫🇷
— لوکاس دینیه
🇫🇷
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/93651" target="_blank">📅 19:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93650">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/93650" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/93650" target="_blank">📅 19:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93649">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnvvCdW9LBIRMjJINYnFsd5P0LEUyBn9wuAh0qJqeCdUuYTQzrkG8j6bVws9rP-kfyYE15R2eSVZjryU9SV_d_mTOO_lq4YfS3Vr8XbAO4Tai_iU7HFRlH9gvXEaAVr-_fj_c3_lZFlP1Urx8iAJAUE6ojwvAjHk06d4rZxJM39zORagkrqb3ibbgWpB9t7XkeaDmB3sgU_aZm62LSHEG2pTQG0gPdRqgKXy8kaZHEGsn5ysS7w0sDFdOGPCH5JxpTlZnz0zVOuHzzETv13ThTqVyufFZhmQTUUwWdsUl19N3pUDWwGXh2L-f18yYT9PbGvQmT-1js1LXnezPCnq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/93649" target="_blank">📅 19:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93647">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90ce77b46a.mp4?token=Fwh_U79QUzgQMM2Aae1Gq44iP3gwJr01M_QkcBl3bUjqESu5wwUgGN951iUdAqJ-rk0sFIL6IKdtA6qxZrhTPRJ3AMlQh1GDL9dgULGoGEBXEBenkS7YkwdfkVfU60dulSO-wY8d41au1Vl64nyzwOIEtNZZv-GnzaUvIulLt4laWGgPbRQJieXaklZyqvbptxTadjv1cout_krd_KP0779fyQBvJQisRRmHMajXfC9kPdV_1iLrfwOPUtIkVMMKcgXD2tUzWtYA8tM1Jxo8h4p32uXDbM5sQ3Vg3roKVZ1sx6r6_dL8xU2UEIfIAtwdoUlzfvvo41Hq4YcRKzoL6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90ce77b46a.mp4?token=Fwh_U79QUzgQMM2Aae1Gq44iP3gwJr01M_QkcBl3bUjqESu5wwUgGN951iUdAqJ-rk0sFIL6IKdtA6qxZrhTPRJ3AMlQh1GDL9dgULGoGEBXEBenkS7YkwdfkVfU60dulSO-wY8d41au1Vl64nyzwOIEtNZZv-GnzaUvIulLt4laWGgPbRQJieXaklZyqvbptxTadjv1cout_krd_KP0779fyQBvJQisRRmHMajXfC9kPdV_1iLrfwOPUtIkVMMKcgXD2tUzWtYA8tM1Jxo8h4p32uXDbM5sQ3Vg3roKVZ1sx6r6_dL8xU2UEIfIAtwdoUlzfvvo41Hq4YcRKzoL6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
خارجیا بعد بازی دیشب رو رامین کراش زدن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/93647" target="_blank">📅 19:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93646">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaaE_cJ2C0JSxyGbwPEdz_-novXp1pWwdzAGUv42Uu-s3SNih5C_IXGy5vcA-oCboo3jOGjYcaXCP9j_nBv_bvW5MWaV1UzIwVPq_FwZHcGLzXe5Z4x1TWeFvOTvmlz1DDButD3yG_Ers2xzo8haLuKXPyhvEIKV6CE7ue9eXDpZzb1MJOaVvZMrGNOcHFnVLQGC7V-Uj1Cig3eKAAC-vcyUfli_pac1Mp1c413Zcfg4bhNT2iZFoUAreVWvY0Wn8sgLlUb3QmSdAkj_s89hCWbSsTZ56zliYdaxmDDFL9vrLLSrA6T9hmIbYvvUu3US2CLiUzTCXublDpFNPEpUKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇾
اروگوئه هم تیم خیلی خوب و بزرگیه.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/93646" target="_blank">📅 18:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93645">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHAyhh-9o_fNOJVzOT_Q2n8tREBcdab96x6TtUxhpcWxf9C0xgAg96n_ERsYhcwklSziSQlJYb0LCGQao2s--EQ3hJQkfXKPj0LG_RUMGcFhZSwA7kf1SQpqjQVUDeTUcQr_exz0jzjByb9Xg2jPz2Ix2cP1F8C_wW4TApaoLxN30Emluugn8bpycBMVXGoHgqBNC2L4t018Kv5PxAGklH0GmEo8nH6RdIUCSyxQ343r-xzqAqdAuu4O6PuYZotoMuVlMVGAQOkXexc8t71mSI6CpCdjhXBkcC9BCTZJTk8BeBupon452rk4awL_qO9MsEEWOpzCMhvYyviicJ4jRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
🇨🇻
کامنت جی‌جی بوفون خطاب به گلر کیپ‌ورد: به تو افتخار میکنم
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93645" target="_blank">📅 18:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93644">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYd1xBJqsdspaTfYWInjdYQgYYiEmK_oEZghakLFsDi7MHFVXngWllnUu5ks1QRJY9FcOD03sUiyiN2LnwfCHXU6tgkbdaWzRypqtRlULQzxSK6r0tsuPvSezwrNJ6EhWgPqOXy4W7sCRWuKwAECmXsefN8bXIj3Kv9t4Npuc9KN-38KLUjWq4eTktQXFwt72LeCmon3pWO9fOk0CmV5YgWy-ZdAz1Go_c6ct4L9csmvTbWBilx4oNJKZ3oC8vWzKQEEuDFgtwT58Nj-S4gxrH28Q7U41KPEQisTeCqp9gp-SQnbHiJ8wdzoL6thK3sBFNfQDTk22T19sHSo3LZk1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تعداد تماشاگران جام جهانی ۲۰۲۶ از مرز یک میلیون نفر گذشت؛ اونم در حالی که هنوز هفته اول مسابقات تموم نشده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/93644" target="_blank">📅 18:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93643">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbeb3adf9.mp4?token=LQvujjMXizCnZ0_-zPxKA0grhp_nnXlz7Y_Nxckhsw8m6uRSvh-d2_-Odqp3M_yDR-4V0QVZ9WRRceNhObti7Mt5k7W5lZ3ICXiv5zBRw6CfbpSybCxOXwHQhPUZITDDiUpjFAX6klgblauy9NprW5M1yCbVzDffnA8Bp-bVpucQW4dMgS0YaiaqL4M5E22lEAXstbJ2UmC_sYJuP2RgPtHM1ZcWcsAplQBIHySQOYyU3M2AijVZk0ck_Hdw_H4lKDnsXAutYMi1K5LrxLMadqpHFy6EtSdXUPGwVUFBWmSZiliQuBEy4Ldut4GZU1bo6DrtruY0OO3NXFNn3AmrEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbeb3adf9.mp4?token=LQvujjMXizCnZ0_-zPxKA0grhp_nnXlz7Y_Nxckhsw8m6uRSvh-d2_-Odqp3M_yDR-4V0QVZ9WRRceNhObti7Mt5k7W5lZ3ICXiv5zBRw6CfbpSybCxOXwHQhPUZITDDiUpjFAX6klgblauy9NprW5M1yCbVzDffnA8Bp-bVpucQW4dMgS0YaiaqL4M5E22lEAXstbJ2UmC_sYJuP2RgPtHM1ZcWcsAplQBIHySQOYyU3M2AijVZk0ck_Hdw_H4lKDnsXAutYMi1K5LrxLMadqpHFy6EtSdXUPGwVUFBWmSZiliQuBEy4Ldut4GZU1bo6DrtruY0OO3NXFNn3AmrEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خانم سوسن پرور شما حرکات تکنیکی انجام ندی هم تو قلب ما جا داری خواهر
🫡
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/93643" target="_blank">📅 18:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93642">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCbYLgjHuQMkbJbZswbOLsjLygmuixlIYa_whbyA_YeTj_ljRoqopuBp7NSHq-HZ5eiCw3DmXQIky56m8h6QSvPYv7HAC2pHIyIJuEbNxWzyIUPAq3XiLP6GgYkYcY1T_2RHXy-tn-JPqXCUw80qM7OiNPuFDM8Udud3km9GTHQJxTmNV_TjdPx1LH9YEfrRxWeSxebj0_l4K9xQQAlDgy5M-Ut6tSZm0s0HFoOhcm7xiIMGCxOZLQxGxZ72MRiWjdjGNMpsa-hTwBlDphemr7vqo-Rs6h_Iq59wk48R1aAnUwcE4OdjqYHCHE7SxV_f-mL0FtrmBkB6CPgTtTiHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیرمرد ۹۷ ساله اهل آذربایجان خودمون که تو‌ تمام دوره‌های جام‌جهانی در قید حیات بوده
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/93642" target="_blank">📅 18:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93641">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb793D2QtOpAs2Z9hg8fqR3PYLQIb4DMr_NENsNnGZf2VwxNL-Vgjc2GFyL10rFhti-XEEEtBdJRMsVrSIH6ffweAD_E2MQf-WoSxjvztDBU0rQDTpu6RGMM-CCinrIEEjpGUVPxn99sI6ElcWPTZ_SLFTGPwK3hwG2fVG8KBRZOtCE1rSKkAp761N-ekLjRjop2C7-I4oSGg0MtobYzYu8OVHnVBPFBg8DKOOYR_rgcV6vAJ-ppdXr9-UnGqFAQoFNKEpzdPehTfkgfqxJrVkHlkQQVfdw0jFx1ZkoFuhm4OxX3TRLswPCTLBh1ubWPeBmGmWQ-KPV3xCiAbP1S7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇭🇷
جوردن‌هندرسون پیش از بازی با کرواسی: قصد کسشر گفتن ندارم اما لوکا مودریچ بهترین هافبکی بود که در طول تاریخ فوتبالم مقابلش بازی کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/93641" target="_blank">📅 18:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93640">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4lChbatuocfytCuNu_LEGhEeHEGmCHu87KyRLuNZ67Fs-IZzId0M-OxfdYQsgtq6mf1NadI9bZimWb2iKlpFvH5MoCMCJcqhyTYPT-qt0-GbfsFsAAYsKVWv5hHmqp7OoAMOGsktUVLZ-UzWIBXElD6a78nXVo3u78kTM2y0P1vTXeI6jwLhOFfc6UfkuVM4Pkyj87bS-kRsIsSDqhAG77tiyWaCm0xlp8J-LsXbZDSBdgbksj1UMqgRDHFouUhD9XKYmsj8YL3Nzm49d_XdJv1bGaiCHaWU3Lw1XTBqH0Y62PYgF3abmlbDiUx_-tWTwP8SkfUWcLxBikv9BEYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی رو پیش‌بینی کن و جایزه ببر
🏆
با ربات تلگرامی «نتیجه‌باز» می‌تونین بازی‌های جام جهانی رو پیش‌بینی کنین و جوایز نقدی برنده شین.
😎
۶۰میلیون تومان جایزه برای نفرات برتر
⚽️
تازه امکان دعوت دوستاتون رو هم دارین و به کسی که بیشترین دعوت رو داشته باشه هم یه جایزه ۱۰میلیون تومنی تعلق میگیره.
فرصت رو از دست ندین و همین حالا از طریق لینک زیر وارد ربات شین:
@NatijehBaz_bot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/93640" target="_blank">📅 18:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93639">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av85s-pe3mUw2_3QES3cAwAlpIN8XRHUarJVzrdNhb5la8M9G6kJ-d0vk63pBBOtKisTDt5SdQmKKEpHQ_GIT5gQQKgUrmAih0S6hQVzAURVOQym2UeJXmJYNqrSUak_H7UfR2OQEokF7PYro9gIMWHEv-sU-fXc45lls1A3DM4ngKGtZHtWqnlY8LSRFJMMewSsv83ran8Mzsx2ly58cHM6bFAr28HbFzPZA72DJ8QutrmG49CKag5rpzdDllwl_RYSJGVy5mcikWwWOKhIPYwpqafgsHRFjRXKi_nNpe34r_B-6MlK3Q-2XOls3vmGzibr-ZmuuJcF5qav1d5yTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
۴ خرید رئال‌مادرید
⬅️
هفتاد میلیون یورو
🇪🇸
تک خرید بارسلونا
⬅️
هشتاد میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/93639" target="_blank">📅 18:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93638">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeaYV47C6JPghSOV12mZB_RLFif-wKxCEbE_R3QTWhVQKT34jPQA_NDKAj-K8m79VZ7YrotYx2rLxQEuCLp2nA7q9B9Ecc5TodOxUTFPyfi__9Jqh25jJf4-kGsW7wsvEnH7htUJk6QE_Hbii3lkq94FqT0sl1RNc-6ZoeybDIVq07ygjAVyOr3YHwWNFSVKlKZkikDQnQYQRuNu6j3NdSWHIgSvRfqeNEZE66MbMdkSQuKKkuWPRJ2yGAP2QRxPyxFuLhtlzRPa1eMvaH6Cu15prKhrc2iU1MMWoHAIfi9Ggx2N5VYyVexjF84LT6_Geez_z_aFpK5YxalfSkWqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#
فووووووری
؛ ژوزه‌مورینیو درخواست امضای قرارداد با روبن‌دیاز ستاره منچسترسیتی را به فلورنتینو پرز ارائه داده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/93638" target="_blank">📅 17:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93637">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh4n6yiEl_Ds-n-lBQrr4aig1jmDCWBhvFpP_OymhXTCsFnXjIVlCoHK_9fGpJSceNi4AEu4X274dgrBrkcw-lVtT9KaFHB335cPmmvUJct7YInmp1e5Gf6BNm6uE3lh8dtMdRdiEIO1VuL0N7G49HmgtXkaNkP4UHrsxRsOJBKAfU7Ojad9Kc_3M0A4Z9Eplb9jS8vlLlCWSTggaMgfkPpE8MJKED7sxV5mbArzWA7pMORT1YGulFMYMpe2QNBW2BnbFYKweqaKnWpNfgBcvQcZOwp6TqTesv7hhIM_zM4Sv6MUpK9I-6oTEZ6f8oDITtF9SmV8JUOQ-eC9kDPOpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🎂
امروز تولد یکی از دوست داشتنی ترین مربی هاییه که دیدیم. تولدت مبارک کلوپ دوست داشتنی
❤️
🏆
آمار و عناوین یورگن کلوپ در دوران مربیگری‌:
⚽️
• [۱۰۷۸] بازی
✅
• [۵۹۶] پیروزی
❌
• [۲۴۴] شکست
🤝
• [۲۳۸] تساوی
[
🏆
]
لیگ برتر انگلیس ×۱
[
🏆
] لیگ قهرمانان اروپا ×۱
[
🏆
] جام باشگاه‌های جهان ×۱
[
🏆
] جام اتحادیه فوتبال انگلستان ×۱
[
🏴
] جام کارابائو ×۲
[
🏆
] سوپر جام اروپا ×۱
[
🏴
] سپر خیریه ×۱
[
🏆
] بوندس‌لیگا ×۲
[
🏆
] جام حذفی آلمان ×۱
[
🏆
] سوپر جام آلمان ×۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/93637" target="_blank">📅 17:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93636">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYaBq518o4dUpyFESXdcUTtoG6wK_UYtOaLvW-PIMfh371On1HgOh0fM3thjdNdlpG98S_ziglSTkp_dVd0vxShm4-7eWHhqiBRc__TEnOwLRksz2TY7dCSz51WKCRc2SW-eRPC5y5PgDt44aAUdWtC8QU9jipOzbaJEMYUc8vvK8-qbraFfGqvVXBaz9NFRi_991ctRQmAgatz3RnQXp8VJ9nrPaNOXEZ4QGvwcoxLZMIWzR0cKUq3yIfL03IJ9-0BSA50NTCLatHkkSAoAJMp0Sg2OXWommeXXJI8q9jHevOZ2Q3ktWBJaUH-8v4Zg6T6EwleXPGtfZRiJH-Sufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تب جام‌جهانی، این بار با شانس روزانه یک PS5
🔹
هیجان روزانه پیش‌بینی مسابقات جام جهانی در کمپین «همراه من» فقط به جوایز نقدی محدود نمی‌شود؛ هر روز یک کنسول PS5 هم به شرکت‌کنندگان خوش‌شانس می‌رسد.
🔹
کاربران با مشارکت روزانه و ثبت پیش‌بینی مسابقات امتیاز جمع می‌کنند و هر امتیاز، شانس آن‌ها را برای قرعه‌کشی روزانه PS5 بیشتر می‌کند.
🔹
یعنی هر چه بیشتر در پیش‌بینی‌ها شرکت کنید، شانس‌تان برای بردن پلی‌استیشن۵ هم بیشتر می‌شود؛ ترکیبی از هیجان فوتبال، رقابت پیش‌بینی و جایزه‌ای که حال و هوای جام جهانی را دوچندان می‌کند.
⚽️
پیش‌بینی کنید
، امتیاز بگیرید و شاید برنده PS5 امروز شما باشید.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/93636" target="_blank">📅 17:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93635">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22977ef03f.mp4?token=tBED2imCu26Wpm0TrMt3w9onT3p0AOp24K1kewmzoybfrddOIlNs0jXc3Kznbmy58omXTY1EMC7ytZ9_S9Chb0inp0MZ0qjx-La5ApzSycg0H42svUBPndXfyyziwXnyq8vVzO0i9xgag2TTQiqtMAAuMqYFYVt5xgm47jsL84rGVRF5QpKPrjGAFl05cnwuL6jRo9DFwYX_szWJDFjUDfZbfDKDBDpQGRtQxKEsvW0WHxvr56Uncf8BhVllmfTG1MDU3lEP6sXiKgG821dKrgXIrJDPDgIrr27KqWk6PwuhoIs9OJwpAL5BO8cc0jDMtCTt8VLvRls6QjP2_a4-EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22977ef03f.mp4?token=tBED2imCu26Wpm0TrMt3w9onT3p0AOp24K1kewmzoybfrddOIlNs0jXc3Kznbmy58omXTY1EMC7ytZ9_S9Chb0inp0MZ0qjx-La5ApzSycg0H42svUBPndXfyyziwXnyq8vVzO0i9xgag2TTQiqtMAAuMqYFYVt5xgm47jsL84rGVRF5QpKPrjGAFl05cnwuL6jRo9DFwYX_szWJDFjUDfZbfDKDBDpQGRtQxKEsvW0WHxvr56Uncf8BhVllmfTG1MDU3lEP6sXiKgG821dKrgXIrJDPDgIrr27KqWk6PwuhoIs9OJwpAL5BO8cc0jDMtCTt8VLvRls6QjP2_a4-EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
همچنان از سریال‌های نمایش خانگی ببینیم که روز به روز داره عجیب‌تر میشه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/93635" target="_blank">📅 17:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93634">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1408b8a004.mp4?token=vQQpuN7hc-tpnAHjHH0bzm_APkHhULqyrmQLr-XKLujlIDr9JG5UYdNhf_EnKRVTCb8JCvsf8mDNPk7dWeR8MKQxQz9v04zi1cwxe3einXtnLFY8HFNstnTEcUjsTKUeLqBIhvK3oD596ycNqT7b-fwSVF_qGp0rBUeHWzBVy7QDERecSiDLh8HjdIcPtAsaGLO8RIfIEQW2nZAXgISScyiVN0Gc9gRHeiCB1rNpJlOEX2D5_bGkb_uW1aswe_jS6ZGJ_F4e48yLq8Qb_tsixf4xN9hGvM2BaFNogu1WAXBVgDD-s8kAMH9pgVmGVtzgtES5hczv6VX29gSeoBzpVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1408b8a004.mp4?token=vQQpuN7hc-tpnAHjHH0bzm_APkHhULqyrmQLr-XKLujlIDr9JG5UYdNhf_EnKRVTCb8JCvsf8mDNPk7dWeR8MKQxQz9v04zi1cwxe3einXtnLFY8HFNstnTEcUjsTKUeLqBIhvK3oD596ycNqT7b-fwSVF_qGp0rBUeHWzBVy7QDERecSiDLh8HjdIcPtAsaGLO8RIfIEQW2nZAXgISScyiVN0Gc9gRHeiCB1rNpJlOEX2D5_bGkb_uW1aswe_jS6ZGJ_F4e48yLq8Qb_tsixf4xN9hGvM2BaFNogu1WAXBVgDD-s8kAMH9pgVmGVtzgtES5hczv6VX29gSeoBzpVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
‼️
🏆
هواداران جوگیر عربستان دیشب بعد تساوی مقابل اروگوئه: where is yamal؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/93634" target="_blank">📅 17:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93633">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eed399e62b.mp4?token=LCI3Vw52uou0s9nfoo0RtLUe3dOFLV020hXzZx0PPgmFlU4CeRwfG0Tvh8VwjCALv0Ovj9WDDyBF-X2nPWEH6X-JOJVSWP7vjQuzg9qOlZTr5sB7ARirLJN6ph1SufKi-RzW5yRqOEArGlIa91bdEZhhPD4ovO4SworN1qoOMt5pYFPdapbvoovFTQ0yq72XuiAcSe1eNkXcvrjMI0hRcAARlTxujJH197MRppfjod8rF2Y1V-dzpriaVv_Gqsha7Zs4JSmUHMjqHcvaxQzSIOfIQ_XjR0zxvYTa7-1CaJ65zaaM4VBx2W7PdMO0jcSxaNVFrhdEWYgPCA0cNgugl5X5jLNB4i9fl45A3aIe1YlE-Sa_1hGXhkZ1J3w6RWxWs3n56z8h74GUum-0t-fBAl-qiq2YDO81A_VXulAcER2UfZ7rNvBCm7o7b-BOMsxNTQz3AY5WuzXCp0MZjYucw8k42XUREDLJ90iRK9LvGpCjDYTPdANW2f7GJCWVOjIOpACmkpnDMKkAdDeSNk0wFy7BvOfnEJn1XQwvhllyGRAdIivLd-1MjQDEicry3tlA6-wB0BT8tfhvH5bNHJZ93dJqk3pF-9Y09NaAIlaOfA62EwTPQdlK53-jtrLV_gpO8klsec48tcQ9UlpQp0oANeNO-nk-4M5NJQ4rTeT_Ms8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eed399e62b.mp4?token=LCI3Vw52uou0s9nfoo0RtLUe3dOFLV020hXzZx0PPgmFlU4CeRwfG0Tvh8VwjCALv0Ovj9WDDyBF-X2nPWEH6X-JOJVSWP7vjQuzg9qOlZTr5sB7ARirLJN6ph1SufKi-RzW5yRqOEArGlIa91bdEZhhPD4ovO4SworN1qoOMt5pYFPdapbvoovFTQ0yq72XuiAcSe1eNkXcvrjMI0hRcAARlTxujJH197MRppfjod8rF2Y1V-dzpriaVv_Gqsha7Zs4JSmUHMjqHcvaxQzSIOfIQ_XjR0zxvYTa7-1CaJ65zaaM4VBx2W7PdMO0jcSxaNVFrhdEWYgPCA0cNgugl5X5jLNB4i9fl45A3aIe1YlE-Sa_1hGXhkZ1J3w6RWxWs3n56z8h74GUum-0t-fBAl-qiq2YDO81A_VXulAcER2UfZ7rNvBCm7o7b-BOMsxNTQz3AY5WuzXCp0MZjYucw8k42XUREDLJ90iRK9LvGpCjDYTPdANW2f7GJCWVOjIOpACmkpnDMKkAdDeSNk0wFy7BvOfnEJn1XQwvhllyGRAdIivLd-1MjQDEicry3tlA6-wB0BT8tfhvH5bNHJZ93dJqk3pF-9Y09NaAIlaOfA62EwTPQdlK53-jtrLV_gpO8klsec48tcQ9UlpQp0oANeNO-nk-4M5NJQ4rTeT_Ms8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
دیس امیرحسین‌قیاسی به خواهران منصوریان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/93633" target="_blank">📅 17:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93632">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyShXYPjQVf-u5ha3R4JCetee39ypXFsdiuEsoGjX7X8ZApu_yEMpB2b6QBEQ0A7bsfcyLI5KdaoQDexjShLuGQDYMpBlog0vvcbIGHUces9thYTNw0KGpjrPafi5wg2-aBKWNtL-56fKdDVsnujBPWh6qViO1DwpszSUoEJsrsFIixQ1VsOxALL6aUeXiq3mOyi1DoEKW-Bk_nmaAjqM7gb7v7IZF1LYJ2Tb96kbQK94h168ai_7JZfYQKfAq0L30G_ZhwRsoMnfcmMlqvk6YJTXPUFQoGliJlb1sYfXLhbggUs3kfR8JxjT06u7xgYC2md-l1DcBjzM1Dge0H1Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
باشگاه‌هایی که بیشترین مشارکت رو در گل‌ها در جام جهانی ۲۰۲۶ تاکنون داشتن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/93632" target="_blank">📅 16:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93631">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe2321092.mp4?token=ByvfqKe4otftZBMlhPBmWD9MNHIC9BCUB-eSojsyMsJLvkYy_dydq9yk8_W8Kcid1jZrC6OxeEmpFpTpR3NtJP_gIh29LZdPtfS7XDmSLT2RcGdQOPTApqx7Ywuvliq4R__NjJ1fnckgCkS8Y06bhgPq_NfAuiXaacD8jYDKs5wJJm6iuWrwJqhKUxdCFwTE8-W8fZyLFGuBtEcya5x7rAp1UAr6gaYTYYWN5ext6zeeXZd1UNtIRYnYZH5PeO1IklDfwF8TlmhrFU2ntl-oDes2AbGSAsA3gMWnaAmoh6xnCZKg_MsHcyylr0lQU3OrvdGdnkxlC9CF_v7P12kVmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe2321092.mp4?token=ByvfqKe4otftZBMlhPBmWD9MNHIC9BCUB-eSojsyMsJLvkYy_dydq9yk8_W8Kcid1jZrC6OxeEmpFpTpR3NtJP_gIh29LZdPtfS7XDmSLT2RcGdQOPTApqx7Ywuvliq4R__NjJ1fnckgCkS8Y06bhgPq_NfAuiXaacD8jYDKs5wJJm6iuWrwJqhKUxdCFwTE8-W8fZyLFGuBtEcya5x7rAp1UAr6gaYTYYWN5ext6zeeXZd1UNtIRYnYZH5PeO1IklDfwF8TlmhrFU2ntl-oDes2AbGSAsA3gMWnaAmoh6xnCZKg_MsHcyylr0lQU3OrvdGdnkxlC9CF_v7P12kVmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
تلفظ صحیح اسم چند تا از بازیکنای پرتغال به گفته خودشون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/93631" target="_blank">📅 16:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93630">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/93630" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93630" target="_blank">📅 16:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93629">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WV3fPQBJ8lxOGAumtw0sga25Vd9LRZcgYxwxTS0e6fKLH_9fRqpNmr6vi8qg_yJYwtnyed0Wq3cS6ym1yz-l1tOdzh3EiYgFpwAylhikkNgzaSkuCxtZljoyJpC13cifloFXV6fNN7cOFsQT1SnoRPhwAatdx2IimFB-jRcTSqbzuqv7SHL5bLBt6j0PY6OhUBYKvsGxJlHK4J0DsOASBpHd8U5wynxJ609HLLGXp5e2YFWnw_BgS_hbO3W3wkC347-nGskJxHCAUSpTi463pMge8SBg-WfGajxlmouuEhiYLKvRxhqrdq4363QrJKYyJXj2MlvNhIy4vMoQkiREoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/93629" target="_blank">📅 16:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93624">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qeKz5jCAhq00XYTlmRuwo94UnsiJpEdPGdyDe8eDAia0etBv9iXIzmoAgYgRGpBXIaTaUn9Rk_4YzoByFNeD_Oa1pbHo7HTtdO_zN_khRi9COs5hQ_dlsxT8kdPKtptUrg-7f7dyvkPRwKtKl9IGPvY6C-6J6ZZWc3J_c0h6MD4S8vhsNyLmJywXmx8Sj9HtJxKVwZqU1ecFIm4GI6_E6tFzFFCogLEn_3StgHzXmmQaGR32_v8dE_nMMqNSSwUMFGzdGpXSt9m8T5K08tZrkiIZoba9A1hi-UMtLyLNs8zfldkVRbs_vx0wWu10s4QZcQ3TJA1Q-3QupePbgCbFiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2SG60999SPYHrnwSzCuE4anr0ifscrC44kbtho7ZMGsG_DoUAioHEmjT778zNauY96L5acO0hNvBRSZqXOtfpm_ImHwcswodNLFwbj8SLHGL2nxXVLG_30Cjvh8nConLqBIE7BSuXr1saQRebfvZxXqXyInHz8wJ2Qx1-xMQ8ja0nKZ6xmOziI3MRlgEBTmCaXGTlkfetAQjZmNaY56DP9anD1JCr6x7M6vtHYVlMFkeZ3H3SdpElWJlGjhaNIehYzUrYyYjob1isDWD_jKPSLSUMTTqdHg_MSKEhkG6C4b47X1g959nOUk5FJ3Ot3g4bnG6-TsNrpxXinbTDELoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4AOBYV_YHVMIMK9xIQOXxyJEqmchkV0hpLiZuudGGUnSdScWgbRzYzitBnOvmHj7c8gkdwL8VpyhdgRmiCagg4qD53KDfkbB3MlBC5y2Y1VdtKVXEV-4FOai_RuYkZ1xyUub47RTH_7vHTVk7s3ZeX09rYP48OuLiC8M1CCdUPuLRV9mBNa6vKQ9JgMtdYQaeJnJkNfC7QPYyJk6nIDT__TQCn1HohoD-x1h1Gjarp3nbtqdIfe-Jyh8w0ClHDzmQIgfbAjdaWNNZqvRmVxFcrM3klVRUirXGmMhoVM2XBg2bluXpKrF3R9VpMtHAyn6Z8j0AISZ_XXcS4oprHwkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j9O9YZvO4F4N_McckXaWxue_GOXBdpfpxc1WPI8-FMd3TytF4j3BrQoGD_AtG8XAkHjFQoWV9362DUdENTYZv-37oljFK4GLoxu20B3lR3_8sVoulffP1W2HpRj3HxVl6wN5y5IT0ufdVgpZtMOP3GYY-cIfDfWH2vgIno4tniLPvXKpcCtBAJynzbSo3Ty8OT7i-RxPNjEF_Ej1R1BJtLzVmnY_jmn9jEVJhZ7zxGlvTFCRyHl7RT_5vh4jT5M_BdBJsDa7v-IGa3tIBhZU107t72jVEtrA23h6odSiEvrIAZTiOg0DsQYNUDM-yuETWfof2MMqhSota4fmFx1VSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق خودم کیت هرینگتون دل‌ها (جان اسنو) بازی مراکش و برزیل تو استادیوم دیده شده.
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/93624" target="_blank">📅 16:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93623">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51044e08bd.mp4?token=PlHL_V2_eJyUr7y1OQhFypvpe4pn_joyOVA_PVu7YQ7sigPi5gjotPV91G5zgA9ABeXwwYGgMt7hkZikjNQuHXo47GnDelz9NMKY-NAMltBpqhUUExjH_4HkPR2DjS74lcwC9N9CSf7sJomYwBfFFxS6_RW1VoCUwgiPKOKnrpgIbzKaltacxop8uPmDm9Mf58uN105MMH9Mwrx4_E2_5M5oXb4UTNHLJLemt_ZxQuq3nQ6IeRZF_5GVl8jBtFJBmoowKExRNUXXrZ40XHaWyauJyXPzfRQjfYuVsV3_8wtaw559UTw5n80mCFcdt8fPvziKUakGQdEUopzKMCQr-jX2wosAi4CSMDEYFM3bYhQaNWpJlaUJAF8n8jVorzD4LPsT50zKstQKMVQ8EbNU1anEr4pptCConhyVF56J9IjIk3JHhZU3HGGtuW1-4TkII7OPQ5YAasQJVDVMJEXgq-1MNig_eU8r2tHFlyT6vnO8fDzM3iz2b7ePSocbyGhJho4rWtq9L3RRmul3vx5fmvWVOZBY3rfeGfGb93t0bBtC-8c_IpYq2X_F6eA33OKtzIuqwOcbb5EAVVqxFeJN4JKRX3sKNMLYESgj26pcjg-3oStnsJax_VpuOFyHdnf7ZTjUI-kMn5EjysGlHth2zHeXvQYCRP1sQk827yReiD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51044e08bd.mp4?token=PlHL_V2_eJyUr7y1OQhFypvpe4pn_joyOVA_PVu7YQ7sigPi5gjotPV91G5zgA9ABeXwwYGgMt7hkZikjNQuHXo47GnDelz9NMKY-NAMltBpqhUUExjH_4HkPR2DjS74lcwC9N9CSf7sJomYwBfFFxS6_RW1VoCUwgiPKOKnrpgIbzKaltacxop8uPmDm9Mf58uN105MMH9Mwrx4_E2_5M5oXb4UTNHLJLemt_ZxQuq3nQ6IeRZF_5GVl8jBtFJBmoowKExRNUXXrZ40XHaWyauJyXPzfRQjfYuVsV3_8wtaw559UTw5n80mCFcdt8fPvziKUakGQdEUopzKMCQr-jX2wosAi4CSMDEYFM3bYhQaNWpJlaUJAF8n8jVorzD4LPsT50zKstQKMVQ8EbNU1anEr4pptCConhyVF56J9IjIk3JHhZU3HGGtuW1-4TkII7OPQ5YAasQJVDVMJEXgq-1MNig_eU8r2tHFlyT6vnO8fDzM3iz2b7ePSocbyGhJho4rWtq9L3RRmul3vx5fmvWVOZBY3rfeGfGb93t0bBtC-8c_IpYq2X_F6eA33OKtzIuqwOcbb5EAVVqxFeJN4JKRX3sKNMLYESgj26pcjg-3oStnsJax_VpuOFyHdnf7ZTjUI-kMn5EjysGlHth2zHeXvQYCRP1sQk827yReiD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عذرخواهی ابوطالب حسینی از علی اکبری بابت قضیه توله‌شیر معروف این شخص
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/93623" target="_blank">📅 16:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93622">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP6HGutUg3dAnLgD5-aPJzECWKtsgdPsUWNgf5nk_Xlw7uEit0P6RpajI2eE-96Jpl_VDkYz1okSm1AqURjZoFZ-GLwBNmNThHiA_MEDgFFEDG7NlG0YjayBXjUSRpDf8l4kv0F537VWzq-okDc90BN_AzJ3jcNxd7ffaWc2LHs7OkmuRvob-CCJ98wQ2wOZmtBJskJjEPhHQfTvjwNQPSfXMDFgWNJaYwgROIDMgDMKDolksLuqJ0FHrtWo2anlaOKi0Dv4qrIvZaaJLcAo8HYTVXQaQmdQ6BfPY29vPplLUk8CxM2eVLmfl7L6rcVVD-gUJiPllxdici3Sipa44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یکی عشقتون هم دیشب تو استادیوم بوده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/93622" target="_blank">📅 16:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93621">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coHQ6vgJHMJNo6adK_ERwUwEm8rc46JZxMxQLHuNAik9V4H-0N9WjqEJZjnioUyjEORyCGoAzo5iB-UNaVP1Nw6RvEZJy72YE219CjqyYgEi-cnDRJ3S6b3tki6oprydX_ARSwZLNkFiBeDPk1EbjiIKCaBlbM177OLRmgdbvlq7G-0mnC3gHtelmr7QE0RCEO8u9silyBf3jAI-tuDCYXk6SElMz7VYcdcGzgqAJAt7I9_qgqpUys_IWqJ8x2MbWrXvj_KialFIStz_NUN6oOXZ3TNh5wfVBGm9rPqqlGPfX1ceNF_vvwM-qA4GFAHS739sy3dXNTCoVri8wbGc2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
گلوبو برزیل:
الهلال قصد جذب رافینیا رو داره و میخواد شانسشو برای جذب این بازیکن امتحان کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/93621" target="_blank">📅 16:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93620">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9081fb593.mp4?token=V_ho4aezVGrW7_ASPVLC1gBh-znOGEeXACC80qo7t3nCsobqRIGbwIcz5_ywCJiUPPmj7jIyvWsjCQsKooZRXS-j5Lmc2puobcrx1hqRobP1ExlIeSs8MbJW8Ilj4bE6mls42qSCx2xRuCdCkoiF1OVKjKW300r7fwVJbLV9nzUyfb9Yt2ZjnfSSGy3trTpqMZsL2RD53WKKcfrp2OWI8zaiCED1y_M7XQfMyKFTqO_l5dkx-G6xSrbI98ada9gQfXYGaiSa6-wsqD2jnYRjP9O8FiYFCRcGyrwd15wnoibCSifsCxM1n8i5A98JsYrNS43UqF27EKLlpBbqwVlZiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9081fb593.mp4?token=V_ho4aezVGrW7_ASPVLC1gBh-znOGEeXACC80qo7t3nCsobqRIGbwIcz5_ywCJiUPPmj7jIyvWsjCQsKooZRXS-j5Lmc2puobcrx1hqRobP1ExlIeSs8MbJW8Ilj4bE6mls42qSCx2xRuCdCkoiF1OVKjKW300r7fwVJbLV9nzUyfb9Yt2ZjnfSSGy3trTpqMZsL2RD53WKKcfrp2OWI8zaiCED1y_M7XQfMyKFTqO_l5dkx-G6xSrbI98ada9gQfXYGaiSa6-wsqD2jnYRjP9O8FiYFCRcGyrwd15wnoibCSifsCxM1n8i5A98JsYrNS43UqF27EKLlpBbqwVlZiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ابوطالب‌حسینی این‌شکلی از برزیلی‌ها تعریف میکنه. ناموسا عالی بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/93620" target="_blank">📅 16:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93619">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54665bfac3.mp4?token=MZk9hjDxPrYFMlCDduIac-NA6AJHwc4q5HZoLPo_F9IO1P3CvWO8_NW8jYVHCsbI6iud6o5LJSwo1lFlWxhSjeWABG9EUJR1OG9DjYVwKtQFkcpYYmSjwvj_qHln6izacMnFtc7yyeZpbo3-sBLmGim8ebDQeYhN1pgxhAL1jABQZFp2B1NuS-AEIbB3Iq-khcVL9W9Q1tnryqy-ZpkY0tleogPtr2DZQEs8yyBrP3P4ka7a8vAuEJJzy79wppUx2hRhiCWIeLsI9tYRnoN3q0V817czETfvpnizu91maD9i9L25p6OTI2-Rz58jNtw7eUDKz13kYpHKpDe1L7FxgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54665bfac3.mp4?token=MZk9hjDxPrYFMlCDduIac-NA6AJHwc4q5HZoLPo_F9IO1P3CvWO8_NW8jYVHCsbI6iud6o5LJSwo1lFlWxhSjeWABG9EUJR1OG9DjYVwKtQFkcpYYmSjwvj_qHln6izacMnFtc7yyeZpbo3-sBLmGim8ebDQeYhN1pgxhAL1jABQZFp2B1NuS-AEIbB3Iq-khcVL9W9Q1tnryqy-ZpkY0tleogPtr2DZQEs8yyBrP3P4ka7a8vAuEJJzy79wppUx2hRhiCWIeLsI9tYRnoN3q0V817czETfvpnizu91maD9i9L25p6OTI2-Rz58jNtw7eUDKz13kYpHKpDe1L7FxgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇲🇦
از داف‌های مراکشی حاضر در ایالات متحده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/93619" target="_blank">📅 16:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93618">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcpPD_SdG03_YK4ps1Spe6S7yAGckBdRKxCyylQj1GAmJot4cwHrvLA96ynj9UMgjp0APtF6hErcIRK-IYKhXrpjytOZrSrRr7OJNgz0WvSkauV6AruOB6sFEIkX6Seor0Mvl_IYJ3JylT0sBa-u5vOldHTSeZiIZsp9YkjCGezW4NUfPANp5nDZXuvFl_TlwDPrt58fgeinoZzeXCNKqTknyTnvm2Ere_noJRpwFcuSdipwguDmxaYmv-sfx-hBTgiPBcZur7R1Dhw74ExUJIDq7ZHR_b_XgVzM90P4LcM85qW_syk7sB5gSJTF5PyYIOgI3BLvKRybKzCNt2QYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری - بیلد:
دورتموند برای فروش فلیکس انمچا در تابستون امسال، بیش از ۱۲۰ میلیون یورو میخواد. رئال مادرید هم یکی از مشتریان جدی این هافبک آلمانیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/93618" target="_blank">📅 15:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93617">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSk2r-kPclP1rnPK4cSTYwWAv0Qrx1oYFHTzX-QoLxJgdi-dlN5YhIU7rh0h2Nw8c9ccXQwY7oPnW7lpDbnHWKKQTIO6-uacwT1RNTXEWD6U7Zwq9KgCSTbv2tenQ9oA3f2TgfRgDN5iK1iUvoxYPyHG3i047w88Fss3hA7OVFXtWQZPQUOgzeYipV2Cn1DnkNwmpXej3vAhhrYU_irULu8iWd-0DGvaBZjlN46hKWsOtNant2oZ0niDQdeA2WkRgA2iaQ7zFOoE8LJmRKUVACZ_yI81vO6rzE8yGhcBDD9VrxHcyiqzJZTWhhpnUETOAZPb6HGiObywZGT5zYq-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌های آسیایی همچنان در جام جهانی شکست‌ناپذیر موندن! فوتبال آسیا تا اینجای مسابقات حسابی قدرت‌نمایی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/93617" target="_blank">📅 15:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93616">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5e6f229bd.mp4?token=IOijtUIkselSOdTYJIc3L9F3mQoA_DNJaS4rX8iVV9bBTzq0aunuFuaCXPJiCcOGlQax9EnOWsDGY2SwoLzRdrRWIUKgOktP9oio-m--_LuOi6h1a4lsB5RHIhFnX28aS91Rf4sUAyxOAkTmQBbwMWs8H_wqhM24AsG_hz2a1FaMjL_UgGvxJZHf7DTIb4Y8BxbJalK1zu5EnrnMOu_M40YccYNDSrc22pgJX8fa2iNEaGIElU9p98Z9RbrpYYiWHdW5Q1ZZGKokHt6LgFJ73NY-bFmugzu5B4cC4ic6HKfWnrI1KwBlN8h10LBYLpBnwlH8yfte3_dRvzQOTqxeUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5e6f229bd.mp4?token=IOijtUIkselSOdTYJIc3L9F3mQoA_DNJaS4rX8iVV9bBTzq0aunuFuaCXPJiCcOGlQax9EnOWsDGY2SwoLzRdrRWIUKgOktP9oio-m--_LuOi6h1a4lsB5RHIhFnX28aS91Rf4sUAyxOAkTmQBbwMWs8H_wqhM24AsG_hz2a1FaMjL_UgGvxJZHf7DTIb4Y8BxbJalK1zu5EnrnMOu_M40YccYNDSrc22pgJX8fa2iNEaGIElU9p98Z9RbrpYYiWHdW5Q1ZZGKokHt6LgFJ73NY-bFmugzu5B4cC4ic6HKfWnrI1KwBlN8h10LBYLpBnwlH8yfte3_dRvzQOTqxeUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
با یه بچه تو شکم انصافا خوب چالش جام‌جهانی رو رفتتتت
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/93616" target="_blank">📅 15:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93615">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc3061863.mp4?token=PwSxnCbiMW3yN0_8CmSVs4_jpBQ5Qp7yAfEWsdHRRHIBU0QVuyfsp4Iv-ZmBtlE9XAgt92TH1kRLR5PcX05QQygze4DjkyOYyZpqrnoA8axZ7lQJVx7Jp_PFB2hcbyg0nX3ovBt3Z8pOywWSwXouilw6jdLFj6Faq2eWoL893bOyAlgZ1MSOMJkUFb2L7h7UXu9Y2E-w2jYatYOve0sWGx0dJOqtywSqn8Ua2H0Vb-WuWZE7ZXBrT2saH6LTeFnQ0gifj5oRMSkUVWMULVNlRwinaIvcTv9NndgBuIbuXMmMzpqOKjibwMone5qZrcUefyZOuNuy09lIprl1nm3U8od-2caDbwOt2Ida_FkMR4Q7svu79G8pfndEJpXynpnJFoDVqUhiOh3TISjnh_VJHpDFpXGU_5clYN5jECbZbRF-N-CrbnrolwMCV-razImkEm2hD2nZgK1l52hBnGiqVwLuIxHAIR0W4UTN435Z7mLSNeUJylI_5C_vu12w0xbkRWgldLgON2FCv3du08GPNts3AR_3aZ8tUqVp97WS11nZbIj-uAFrs3bkotqHeo0ZAafWANzI1MMd-LuGTXwM65dwtGhMNBPAygD7FYVidj6JeG5E5zFaRyiwPp0yJFyLpDhbmkjeLvACAP3fWeTddrPLJE6ws9-MdrBndVJ7r7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc3061863.mp4?token=PwSxnCbiMW3yN0_8CmSVs4_jpBQ5Qp7yAfEWsdHRRHIBU0QVuyfsp4Iv-ZmBtlE9XAgt92TH1kRLR5PcX05QQygze4DjkyOYyZpqrnoA8axZ7lQJVx7Jp_PFB2hcbyg0nX3ovBt3Z8pOywWSwXouilw6jdLFj6Faq2eWoL893bOyAlgZ1MSOMJkUFb2L7h7UXu9Y2E-w2jYatYOve0sWGx0dJOqtywSqn8Ua2H0Vb-WuWZE7ZXBrT2saH6LTeFnQ0gifj5oRMSkUVWMULVNlRwinaIvcTv9NndgBuIbuXMmMzpqOKjibwMone5qZrcUefyZOuNuy09lIprl1nm3U8od-2caDbwOt2Ida_FkMR4Q7svu79G8pfndEJpXynpnJFoDVqUhiOh3TISjnh_VJHpDFpXGU_5clYN5jECbZbRF-N-CrbnrolwMCV-razImkEm2hD2nZgK1l52hBnGiqVwLuIxHAIR0W4UTN435Z7mLSNeUJylI_5C_vu12w0xbkRWgldLgON2FCv3du08GPNts3AR_3aZ8tUqVp97WS11nZbIj-uAFrs3bkotqHeo0ZAafWANzI1MMd-LuGTXwM65dwtGhMNBPAygD7FYVidj6JeG5E5zFaRyiwPp0yJFyLpDhbmkjeLvACAP3fWeTddrPLJE6ws9-MdrBndVJ7r7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
یه‌کم دیگه ادامه دار بود این عروسک نماد‌ جام‌جهانی همون وسط لخت میشد و ادامه داستان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/93615" target="_blank">📅 15:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93614">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_mZkkCJK8fClxS27gaDWBao8PxLZMcdxrGzOwz7YIjcQkCxIyt4H3H6PRLhjDdK1DqdkC6Xo8qm4kpEpf_4BV4zsMPrNIhGvfYDpcdtZ_dChx--w9Wt0Fs9u-oXzmstW1bKBdl5yNgxEhlLzYhxjkIeiHULj2wB-imfqhM4ed8Aj-E2hKkWjaVfstt5N7mX-VMvx9be_g1MBSKLSmgB3D68VLfO1IEFkGxGkJNCI_pZkd0ex4R0wbyU26rNwA_A_guP6zVaLKtsjahdv7qfNIo_fQj_YDZbRjOJ_WtPOkabdlXVAV7pjImxooZp3evVblEnk_BjQivIh4PDt-eRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویتنی رایت قبلا هم به ایران سفر کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/93614" target="_blank">📅 14:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93613">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BhZeMUN_owuu9hkmK52GgQFPoIqN4kNPt62XMaDdBL18JHRqt40_rMLUAUfKs7LfwJFRB84bMKg0Eh7IMZVoFJhxAxfQSOCyZjn0aRZaWMQ7IoswO9pE2KxJWU4VJRXZGwcJ1XbDQvJ1L0sxjGNbzvDoOMHm_Q-0ID-ikBefU0udWZ3V9lq-NVY1m-j2e7KJUi0PblEIkpvREgJgsq0wzU8RbjQ35se9k2Wn-5EOp0xtLm5LBKfG8y8oI1t-nT6JJhfvEHWpRsNwtdX2kqR_Z06HwMMHUVHFqBbQlDibfEE6G9JPIxfTgcv0cIBd15f6u21yMrWPtqzm4ETdL6tbYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇹🇷
در اتفاقی عجیب، شبکه TRT ترکیه، گزارشگر بازی ایران و نیوزیلند رو با ۳۰ سال سابقه بدلیل ارائه اطلاعات غلط به بینندگان حین پخش بازی، اخراج کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/93613" target="_blank">📅 14:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93612">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Os3XfUvVMf08GOapQ8wJDCR_1HSDmHK7R2YyfdRnQ-rk2xkbaNKmYZtYLk2OilPC-EAhEIIDQKMkjh0rWbzHdvy_cVT_-UMKxS5E0W4R32oEHyX1OhWZEEzEXcWVpMv11Rs3kQWdx1CDOHvv_erYaYuM3Lnp_nWJg5SYRVJYmvOn_J8ZQKZqbs0a-M8WICWBPiwSzR0g4Io9OCT1EG_JvROyNnalUlI4ytemqYmixa8T7tCYgEJrSx-Kg0FsggdIim8Y7KbcXmLIWthGaWGt08ag_Bd-2dBDVleugUqizu8rpjvsGMDmX6nLYk1_rnTRJbYdupcmIzAgKGyYaXk-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
📊
🏆
👏
در تحسین تیم گمنام و شگفتی‌ساز؛ کیپ‌ورد در بازی دیشب مقابل اسپانیا درحالی‌که مالکیت لاروخا ۷۴ درصد بود، تنها یک خطا در طول بازی انجام داد که رکورد کمترین میزان خطا در تاریخ جام‌جهانی را شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/93612" target="_blank">📅 14:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93611">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🇮🇷
#فوووووری؛ فدراسیون فوتبال ایران درحال رایزنی فشرده با فیفا برای صدور مجدد مجوز و ویزای نفرات ایران است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/93611" target="_blank">📅 14:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93610">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووووری؛ نشریه لکیپ فرانسه: دونالد ترامپ دستور مستقیم ابطال ویزای برخی از اعضای ایران از جمله ترابی و طارمی را صادر کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/93610" target="_blank">📅 14:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93609">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTNu7Jy6CnF6sdzVTuN0FDulJCFbtpkJRTvaGi0fV0Z8X22V3hqj87iYZo8peNWnO82EGvU-S29nR8Bn0_1UHpz_ycxm8yGOy6UyZGE3xgJ1SI0Bh8gUGZZK9qBmtfzIBHg50NYhEUDI70LsIEmB_GNuaXrIVRjMnHhJDb9OB0f0_lmntur7tRFdUUK6be_YVdQU81D3uc8BSWqUpWDyphUzDLClldcDVILF-slARgLd3ZfQLAbG5I2sFOWV5QCSBCSh0zD42LWC-CYdd8iLU6WCRlCnk1mbrIbWVJ9LD20obm1yjJPYp6NQjDHMcJljvv_xq-31MbX1lHzHk25RNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری؛ ایالات متحده ویزای مهدی ترابی را نیز باطل کرد. دلیل این تصمیم رفتار بازیکنان علیه حاکمیت ایالات متحده اعلام شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/Futball180TV/93609" target="_blank">📅 14:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93608">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووری؛ بدلیل اظهارات دیشب طارمی، ایالات متحده ویزای این بازیکن را کنسل کرد و این بازیکن نمیتونه ایران رو مقابل بلژیک همراهی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/93608" target="_blank">📅 14:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93607">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qY4NeoyAc3rg7VxrXjFv5twE1tdEIxcu6qDrU7OXrkI0X87pWAFym_SLUF2mzTPhg4-r7mfgL3BJPGkrvMwux3-XuIATh5ISsCqYDDx-oLZrJSdzupPyRUbKoddkTbqxe_-Y4vWf7KaP7Ld35is5yf-dYHGu3uXvUAlSgH3TW9HIv6iIH8J2CLx2T0j4qoxjLNvXw0ZT1DGJReCGWonE7Fasj8B_DJKbdezA9PzqpV2IPlKY_A4Amc7GWC-rwASAUsvo7BDBS4BgtmpXKJ7WMxI2n1Eilv4Zke4RhsAE_qrAKgU0vanhRJcnipexxh75CgmWpzDDQSkhtzxD9HW3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووری
؛ بدلیل اظهارات دیشب طارمی، ایالات متحده ویزای این بازیکن را کنسل کرد و این بازیکن نمیتونه ایران رو مقابل بلژیک همراهی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/93607" target="_blank">📅 14:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93606">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01d8ca26c.mp4?token=E1cSnY0O2oJlpVBCUHtsbNLOPltc8VhA1Gj4fUmxfk2g74p0x8it0Ojne5n7MtvI__EEZICyJCfKkyc_PvOVZ2maL8vxOHvsub0SV9RD2ZlSNZrp0QItNr8MaXdfcl2AI2-jzUBfZAe6mumyD1KBHNXyBUfGBtABmRycq6xgpbbPTlUZ7BY_Pn28-p4edXLx7pMhyx7SjOd69tPr3ruEtxPQ-c42cle7ngkRPV_jTfQOhjl-cUkjQTq462M3RPhom-zUM_EZ3EdjPMUYPmjGMERe2lmhIFY5UFIyMuFYH5dYsbbdcHxIpGaYctuNorKpBH5ak3BpcUy5TQTW35uL5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01d8ca26c.mp4?token=E1cSnY0O2oJlpVBCUHtsbNLOPltc8VhA1Gj4fUmxfk2g74p0x8it0Ojne5n7MtvI__EEZICyJCfKkyc_PvOVZ2maL8vxOHvsub0SV9RD2ZlSNZrp0QItNr8MaXdfcl2AI2-jzUBfZAe6mumyD1KBHNXyBUfGBtABmRycq6xgpbbPTlUZ7BY_Pn28-p4edXLx7pMhyx7SjOd69tPr3ruEtxPQ-c42cle7ngkRPV_jTfQOhjl-cUkjQTq462M3RPhom-zUM_EZ3EdjPMUYPmjGMERe2lmhIFY5UFIyMuFYH5dYsbbdcHxIpGaYctuNorKpBH5ak3BpcUy5TQTW35uL5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🏆
هوادار جذاب عربستان خوشحال از کسب اولین امتیاز در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/93606" target="_blank">📅 14:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93605">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67027c74d2.mp4?token=XYWVD2xD_UNozinfCno0tZ-oSby1sDti1ZhMS1T2Inl20un8tiXjLAew8CK2HnQv_OQLgbZWykuCtT6uC2JhI79GGum53_8Jev7-6HaaIrk9paSpNtiiSEEDGa63zempsm_EMNNUZWhful9drwV3eNgwpbpDL4SntnDVrzt1_yCawFsGk2FyfRFNGuYCI0jxC-MVf5jKJ_myK0RPwzdiur-51PXpcM3Hcdure9zFsafeKiCj4CTm1Ap2YMOQosju5Wc8VLZErdMoXAOS87q1CxniIdZP-Sdd_logN-bS6c02vCgK3UN7ZNk69stAThH2npkdBk2RS1pKju1J6p0Q3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67027c74d2.mp4?token=XYWVD2xD_UNozinfCno0tZ-oSby1sDti1ZhMS1T2Inl20un8tiXjLAew8CK2HnQv_OQLgbZWykuCtT6uC2JhI79GGum53_8Jev7-6HaaIrk9paSpNtiiSEEDGa63zempsm_EMNNUZWhful9drwV3eNgwpbpDL4SntnDVrzt1_yCawFsGk2FyfRFNGuYCI0jxC-MVf5jKJ_myK0RPwzdiur-51PXpcM3Hcdure9zFsafeKiCj4CTm1Ap2YMOQosju5Wc8VLZErdMoXAOS87q1CxniIdZP-Sdd_logN-bS6c02vCgK3UN7ZNk69stAThH2npkdBk2RS1pKju1J6p0Q3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
خلق حماسه‌ای جدید از دکتر علیرضا بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/93605" target="_blank">📅 14:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93604">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec0210a91.mp4?token=DFdWyL5WGvQWDyj0Aehr2noisQnunbIXhXxcT3_9FfntXHLhGhWPEZVAiFdceR8Yk4KKy2lsUUA16UYt58klo3bv3o_flJotZeAC0OhMN6B4pQ1ZyoNk_WpmCoYU4bWP5OA34bMXnbPeiIS0r9yOzgRHN60dHEAYaZZySYyELBFDZ3nRyIsnMGoMmv12g8y6dZWMUI39En1AaJP6dKu4w3csnI-1OHKvdludi-tlGYrF2t7zGRy9a-_kzcWxu6BanriMSdwEvaORc8QNq3hisbVrSdhF9zDYDbpcXutBc1yq9A35H05_fUgT3yZDX3VvY1DgTYgm_gWkrbglyBWz6QXvhrF-k7bOfs1zRpQdFJtWlvOWGG2qYsZGK3VhD7oyVsWjmPOzrHnH9ZiWStJabitJkR7TH0gxir91mMtC8JA_koaReUO_5nbl1vlYD5DJIJoNTeA2gsALlhePSziLBi8oURVonTZ657YZqXBC-vbK-IhvPet6mvo3maNnFMgxVqXXwOsrbbdVvtPhliRN9tiHpKJEvkHqcyW89XbGEE4tEr9RO1QpsdB893D1pB5qgZnHSlyIePswWI35T6IUqLTjEFUi27tF1RS-QD52OQf0zfN2HdUaMcDSYADnw8FYOrM73xgWGTB5aQtcmZbuEOy7-RXdIVU-MpxBiF2aE_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec0210a91.mp4?token=DFdWyL5WGvQWDyj0Aehr2noisQnunbIXhXxcT3_9FfntXHLhGhWPEZVAiFdceR8Yk4KKy2lsUUA16UYt58klo3bv3o_flJotZeAC0OhMN6B4pQ1ZyoNk_WpmCoYU4bWP5OA34bMXnbPeiIS0r9yOzgRHN60dHEAYaZZySYyELBFDZ3nRyIsnMGoMmv12g8y6dZWMUI39En1AaJP6dKu4w3csnI-1OHKvdludi-tlGYrF2t7zGRy9a-_kzcWxu6BanriMSdwEvaORc8QNq3hisbVrSdhF9zDYDbpcXutBc1yq9A35H05_fUgT3yZDX3VvY1DgTYgm_gWkrbglyBWz6QXvhrF-k7bOfs1zRpQdFJtWlvOWGG2qYsZGK3VhD7oyVsWjmPOzrHnH9ZiWStJabitJkR7TH0gxir91mMtC8JA_koaReUO_5nbl1vlYD5DJIJoNTeA2gsALlhePSziLBi8oURVonTZ657YZqXBC-vbK-IhvPet6mvo3maNnFMgxVqXXwOsrbbdVvtPhliRN9tiHpKJEvkHqcyW89XbGEE4tEr9RO1QpsdB893D1pB5qgZnHSlyIePswWI35T6IUqLTjEFUi27tF1RS-QD52OQf0zfN2HdUaMcDSYADnw8FYOrM73xgWGTB5aQtcmZbuEOy7-RXdIVU-MpxBiF2aE_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر زیبایی از یادبود شهدای میناب در رختکن تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/93604" target="_blank">📅 14:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93603">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180؛ #فوری
🔵
با نظر کمیته فنی استقلال، سرمربی فصل بعدی آبی‌پوشان سهراب بختیاری‌زاده خواهد بود اما برای این مهم، یک پیش‌شرط مهم قرار گذاشته شده است. اعضای فنی استقلال به ریاست تاجرنیا از سهراب بختیاری‌زاده درخواست داشته‌اند که یک الی دو دستیار…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/93603" target="_blank">📅 14:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93602">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8207116ca.mp4?token=FUpQbLxyD67Ftlhcpp37DQ31T25oEGMeELwjwYhHaQDkMDH14ivNakV_HQFHOWVw3ZkDgvI-9az8O8M_Dnc-uX1_qKGpmgjd83M-MQBmsyujMuvIWvSCRQBD1m9xoypGGm_q5HirM4d28Qtr7n4q7GaNTwJAVFmQ0GMZeuh-zrH6_kItFtKWHEh_UZb1HSOPK6KNbJxLA_ELt90ZLANPyTGlNe357mFQAydwJ7Hd5LN6JeX8U8CO7urKPJk-6hlOiL2Bo2y1QIdImjIOxckYgmtv4xVlrOZqIFNgDDjcjuFmX5ROK1nI8-h52lNA5RwE2Gpz_KGllcsf9qV5hnxgHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8207116ca.mp4?token=FUpQbLxyD67Ftlhcpp37DQ31T25oEGMeELwjwYhHaQDkMDH14ivNakV_HQFHOWVw3ZkDgvI-9az8O8M_Dnc-uX1_qKGpmgjd83M-MQBmsyujMuvIWvSCRQBD1m9xoypGGm_q5HirM4d28Qtr7n4q7GaNTwJAVFmQ0GMZeuh-zrH6_kItFtKWHEh_UZb1HSOPK6KNbJxLA_ELt90ZLANPyTGlNe357mFQAydwJ7Hd5LN6JeX8U8CO7urKPJk-6hlOiL2Bo2y1QIdImjIOxckYgmtv4xVlrOZqIFNgDDjcjuFmX5ROK1nI8-h52lNA5RwE2Gpz_KGllcsf9qV5hnxgHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
کراش‌فوتبالی رویا میرعلمی بازیگر سینما:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/93602" target="_blank">📅 14:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93601">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArjhEOVbhKPN4bUADeIhW5o9xcI43PdlZAEKLPvdQAhHLIVbhnJ3FDvwb2H1YJSpa0B4xKJN6kFjzL2Bbri4WuxfysfzORHfQH7JmcPbwz8QW2XModyN4Jdp9s2KYTUWJcRXhAMkMbRvQ1Wx1uySjaMzQIqGFs3U3BCxx406BhsYNc34VlviSrQOnETciHnBuebtvqllKNMSmRFwjkK7TqH79GyJbOR6zIEkzEfN2a_Tu1H3Tgovz-WPRIveUhb70hqQfQY-JWo1UBRq7d74DOOF-6ehNCVWLgu5hkY2oKKc0UBDcKEu5eC4ttFYzfep23xgJPs4nffLFFIyFoLmvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس تیمی از بازیکنایی که نذاشتن الی جاست و کریس وود هتریک گل و پاس گل بکنن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/93601" target="_blank">📅 13:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93600">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
❗️
گوشه‌ای از درگیری دیشب ایرانی‌ها در LA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/93600" target="_blank">📅 13:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93599">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/422fafe762.mp4?token=Csmc8eJjFFII9gBRPZw5juSYHGDMSQH2tiAd88eZDQnF9427rylIKk6tGB-aTAn1tkZyELaLsbJK571DbIOWhLSzdJ4xtE5nVSQy6kHyH9Q91ufCbqu5x2hp97M6PuY4oYRTsy2EWdxF8t55J0kVpJikGTFoiVlwrXHrR3VCWLGj-2kkO8A_9OX_BjMIJ128KitBgsphFL64uqbuUCH5ZUh0bh4k3XemIlUFy_4Zw5Rbx3gt4lAVkUAazbF-u7tj4MkeTjEHa6ZxMnCeF4aq1sUjFbx6FunutIY5VipAUkNFFNlLejpZ3l-yZvdT9ofKdmT0K_vigKjm2XmLQA3_Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/422fafe762.mp4?token=Csmc8eJjFFII9gBRPZw5juSYHGDMSQH2tiAd88eZDQnF9427rylIKk6tGB-aTAn1tkZyELaLsbJK571DbIOWhLSzdJ4xtE5nVSQy6kHyH9Q91ufCbqu5x2hp97M6PuY4oYRTsy2EWdxF8t55J0kVpJikGTFoiVlwrXHrR3VCWLGj-2kkO8A_9OX_BjMIJ128KitBgsphFL64uqbuUCH5ZUh0bh4k3XemIlUFy_4Zw5Rbx3gt4lAVkUAazbF-u7tj4MkeTjEHa6ZxMnCeF4aq1sUjFbx6FunutIY5VipAUkNFFNlLejpZ3l-yZvdT9ofKdmT0K_vigKjm2XmLQA3_Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏆
تشویق جانانه علیرضا بیرانوند در بازی دیشب؛ صداشو کم کنید درتون نره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/93599" target="_blank">📅 13:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93598">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-kShMDc2wUfd3XgimE12x-URLDAY__zLJM7VbW8GXwcJ-RSJ9wJxfn034BhIslwD3_1UzB-mIG0H8lJeIv4FEYRxJW8ibx4T6uc_mNtF1ZTzD_KWcTVFFCKKa5nAp45TsD--K9Bkqs4owES7sF5Qw4kO0yfFrlFt9kK1VCH0iSkUJM5Y_0Jiupp7TPcVX-yURDuWKIwfk2nYO8edyW0xtR1fKcaK9LImilo82VPP_j-3JKhEdKAMFWU3PQyjp13WeUJm542w2rG3S0d9V9yQbTEKJRoyFOfJie0JkBzYmQQZ-_BzXIBMZBcGBi5FTm7_HMIgCNmsOGx13Nfb2W9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
هوادار اتلتیکومادرید در پی‌توهین نژادپرستانه به وینیسیوس و با شکایت این بازیکن، امروز پس از چند هفته تحت‌تعقیب بودن، بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/93598" target="_blank">📅 13:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93594">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DpvCtgb8TUMX89xGHnDVRK2mV64pjXIUciLIK-O0uPdRj-7L7BMVZW6_1f8aigk7RLPBbqauQ2WYSRymuKguApE8wWx1HO_ZIQNWS12X6qSnkE4TwW9d_UlykSw8UskqyUbYQqVWkBB2lzLgFoIR0IdJCwRbgiMelHHlPjO_VHlB8dclahgmwwiNEgzXJ0-LrqyR3eOJZa3I-aYV1TG6KKqkdeq3BBi9qijmSfYl5BC5HTH_WQwTcReVsfykbG85JFAY68LHHzXUEIwpgfhDlWZDtNbXm-D395atLZMCn-ajflFBLy4FdHCUIPZrH_606px0W7BD9U5UFM9T1gKM-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8piAo7xywJGVbtJpMjZyuEE1AMZNCuZgDh2WKJf0f5tzzslLW920tQiNBx9x53XxYLxYFe2vB_nAOiMfgDdk4s2IXNAc8vny0ASieAHBwaDsmpyIPTIza2MAwiRmHdbvMEEP1zaUPxNKI2JSx4RXRNxe8kypAysnWqybJNmfOwhbV1jFs4LCQFDz80phBCBrypXub6ob_yGwcIpdQl64OuabsZzvSXMa3cci99P297JVXQBAlw-0Ex0m7b-Sg0aK6P8uPlpoY0wYfULleLbPdOqbRV_ULWx2dd0hkVDIhifpBqUpCiK54oVoLFmuLL6u6uxUzsg03r__pEsEQ7wBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbaPu7rjOPKrL6tEvP8mHYZxafD8cClSZYM7T3Q313FQUFlrSZx7JIskUj3ZdGMneehYwYdK2I6HKk4lz2AhPvb-dC7RRXhT5q9woTJlgPu_DDdvQFF29et1YE0gAvD62SbhSOkvJBXJrTzzqxvmOqHoLP_1uezdwKKoNOvTN3_PIS_RFkyoVPG96Puy3Z4-74uQiH3Lmruq4jtzSk3kr8cUjWfx-C28I73hF77L3SeiswYnhxsPSNbyJjfXdwqPsFtxZWhcVOed2f8D8Ih89FuAZ1nDDoPSn9-PZ2YQLUqmM3A7w8HIIuiQuUohdjh-Lf_rol2ymAHdOugMtyLvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k95_j_i0inVsHSBMO0O_pP8JISdutbzgoC0DtZ5VmBrccAY7aDoc7PM5RRveotf0qlHY2Wib3LoPrbh7v7pe6rCJ_LUs7UFhIb3yuIKapI9URfy2Fzi1u4ka6RbujpmA4QDOyCUg3X6njcP7llDHuPMwXf-GvJI9Yqvu6AUKzbld7lM_nCa3-Uyiyld8Jxk4tRYPC8rLxU74Wl2H3jfgs4lMVV4xn1Wr9_KRMbaLfatIBedrVTq4agKcJja2mgL6Wl-26uqrAsMBKaJKXFC0cXCxWzzmX2P-RYQDP5Kpr3A6EpbLMOQ38KJx70nzVdPxKP9d6H12tc29Qml9MPnLNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیشب بانو ویتنی رایت پورن استار محبوب آمریکایی که اوقات خوبی رو برای جوانان وطن ساخته برای حمایت از تیم ملی تو استادیوم حضور داشته.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/93594" target="_blank">📅 13:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93593">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzKDY0VJNzy45ajfGWg6pMpinwpuTeCJPw5ZbUMqIpZiJF4PxDHcFegANBSDSHovE-LPFMoDDJLp9AHko8lMAo-qILS7o6Xo9HBwL5zUqre4Qh9I9XQg1jGDtqwq8LBhXRSH-4KapOPBsEMaPDLxc1pVZLSYQ87NXcrXtVwas2getcPtjmqyBvhKyYzye_JPB2zkpADzennY0h7560YlEWop5L8pfVCjWyJX-mxCpuVy52bvnll7TRacNsDv9naBCSYzpoBst8chC_yr6l2LjriGUQg5m2EPlDg14TG9XiyIkOagO4aSsIsYUrbaXTI0Qzp7CaNCiuMEjYDnG4f7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
◾️
آ اس:
چلسی به جذب آلوارو کارراس علاقه داره و رئال مادرید هم با فروشش مخالفتی نداره. از طرفی مورینیو هم مشکلی نمیبینه که فصل بعد مارک کوکوریا دفاع چپ اصلی تیم باشه و فران گارسیا یا آلوارو کارراس نقش ذخیره و جانشینش رو برعهده بگیرن.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/93593" target="_blank">📅 13:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93592">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGIr4p96CJ_jlTK2yKoQgVsV3Ejc_bpmsEZr7e5Fm27aYjuhWzFCyUH4YEk2iVG1jGaUWFjwjYyJqMnJmON5PG5-Zjmb_MNBeR6d8S9xDqDUa8K-uY7eYkDjHPHIPxVGa1ey3X6enERckVmIA9KAyyvPupzrkMZdYXgz_Cf5PwBeYbrdP-W0ovt2S_v2jzuyRdwxpifNw4kDpAie1Fqsk_7KkWAqCVKUUlXABaw6f9Rp-UFpOjL57kFU0xF2sWnMpE76YLxMsbQo4k-n1UKjaLJzw_XVMbtk_UBD29GT1sp_HuAN9zBwFgI3HwwY5oRC92dFC3UUEyIxDpOXZG8kag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
گییرمو اوچوا که تو بازی اول مکزیک هم حسابی درخشید اعلام کرد که این جام جهانی فعلی آخرین حضور او خواهد بود و پس از آن از بازی‌های ملی خداحافظی خواهد کرد.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/93592" target="_blank">📅 13:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93591">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTrspxW1mUit_Kkjgt5kyzES8_baPN2nc13AuTS9vhQm1l-6V8qZGmyFy1CmHfbHybLKYjsPMBsukCg7ybzTL9UP5MN37Mqnokp_HxOVJIj32rH0AwIsaIyL7wuSZJbhMdlqlGaU4qnEtR3GAIlshbuAKlzWGk8fUI2K5OHXGkU2Z_PUYsY-Gn8mSKqCmnRhc4qxQ-sWVqMdm3i2ZciKL6CiIswSnbFC4IgV_syPyeeGsPvKuBBi7EzCsm2xbt2vw1m1VqMchTrkHtdPAhmqpitnPAobr0B0ERJ5q3TgFR5lWVpFnftFJzQUkltBOPDZZlUa4dlqSFi1A75dFCFfTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
توپ لو رفته برای فینال جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/93591" target="_blank">📅 12:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93590">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1eb0b0af4.mp4?token=Os9FzFp2l1RsTE74rInlHhSsLpdN06dk5RRcykjNeVfpRe-PFUZ-n2C13BISY7b4vonK_UIyxDxU3hhwQLIaovUs3IQgMREBAnAUs74AGJDYkh2iNxi_R6xyfy26OYTRDo_Xn_H00rDlvoVMNXdeMyKrMOzRVSiVLgfH8_I7fJJn6dwgNWVWGYhLkWvZrIc_TpI6k9l0pzK6PzuyDiRDTnTTUP4-fnBjEQwy332Su5ljlIAjrLekFHvRTA6LwCbPeqVuORSLf4xmGkhyAQJNxktyGLYESR0nzz1VGFDLAMFqTC8-A5E9tHzBHIyLWBBEtcJUTAs6MByjXtFweMk0Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1eb0b0af4.mp4?token=Os9FzFp2l1RsTE74rInlHhSsLpdN06dk5RRcykjNeVfpRe-PFUZ-n2C13BISY7b4vonK_UIyxDxU3hhwQLIaovUs3IQgMREBAnAUs74AGJDYkh2iNxi_R6xyfy26OYTRDo_Xn_H00rDlvoVMNXdeMyKrMOzRVSiVLgfH8_I7fJJn6dwgNWVWGYhLkWvZrIc_TpI6k9l0pzK6PzuyDiRDTnTTUP4-fnBjEQwy332Su5ljlIAjrLekFHvRTA6LwCbPeqVuORSLf4xmGkhyAQJNxktyGLYESR0nzz1VGFDLAMFqTC8-A5E9tHzBHIyLWBBEtcJUTAs6MByjXtFweMk0Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇷
خار خلاقیتو این برزیلی‌ها گاییدن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/93590" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93589">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjrjnhkft1P7crMAo7gRSZRRtD8QTM0H5ETY-5O4qCExvG6j3tbD0toR3DUFJBKudcDU3lV662nDlJwapc92ZWyS7zlr35jxeiy98yBipmTitCJpd8U4e6S1f-1JVW4zz2b9rdArOia71revhXE5C56tupG3CBEUydL-jfmJAC2AuAPfLDO277M_p2PvwN9Z7Qlyu8PzJK6Kj3pgcNkmauBw0v7l7hVMe7DGZSLo22rAV0Asa7kM34UmZBADBHtKWQbu7Kt306PVNAzhGwitlL9MIb8jKwC5hDsmlX8cTDoWOhgGSyvpGtI7F7v7ZhOzfgA-2Hpearg9gujI8-M06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رئال مادرید از تمدید قرارداد آنتونیو رودیگر تا سال 2027 خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/93589" target="_blank">📅 12:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93588">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a46feaa24.mp4?token=KqBojaKGiZNs0aXucODxzHmuaBa_xNtt0oln5IzplPAJW1xwQF5u5fm53ydYfDCieHSDO5oVX6h2CV-yRSUmPxWigzkzSLkLLoBS0-DuAxgZnySo0NEukGcln_j8-KY8R26wYSWaitXDFSl9Z9q6ymlDHtT3VFBDGrzlqifJvpq4LBpVKqa1juKINhXSfIZhK2DrKQh52FkpS_2KJAXZ_X5nkIX-8lztrUh-EmWERDADhrH6aWUSsPRbW2wMMVz7WiaKztU3a2ey03EYbnWE0tp30b5k6B3r8Nst2TLauYv9UxSrjpCGZMz_l5cCfAVrjejFOZYMtGoKB3EzD1ZI-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a46feaa24.mp4?token=KqBojaKGiZNs0aXucODxzHmuaBa_xNtt0oln5IzplPAJW1xwQF5u5fm53ydYfDCieHSDO5oVX6h2CV-yRSUmPxWigzkzSLkLLoBS0-DuAxgZnySo0NEukGcln_j8-KY8R26wYSWaitXDFSl9Z9q6ymlDHtT3VFBDGrzlqifJvpq4LBpVKqa1juKINhXSfIZhK2DrKQh52FkpS_2KJAXZ_X5nkIX-8lztrUh-EmWERDADhrH6aWUSsPRbW2wMMVz7WiaKztU3a2ey03EYbnWE0tp30b5k6B3r8Nst2TLauYv9UxSrjpCGZMz_l5cCfAVrjejFOZYMtGoKB3EzD1ZI-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
مصاحبه جالب گلر کیپ‌ورد بعد پایان بازی دیشب و درخشش جلو اسپانیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/93588" target="_blank">📅 12:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93587">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f49a9fe65c.mp4?token=q3V3rZCUsHYw54MdI_yer0AOO21QKWMwOZal4P3YC1vye7kFfWucO5ZoFcsazW2MCUg5-coCqmJHLYaQyqIFxy7xTGHXPwsmEy_iIjXOGXUEQMQMxUygov-gtjk8s-2ysYcm7bbpHW3Hsi_QmZHZgpeykqjw6MU4bCbPUqllfJu5RYtl-nn7k-AEfUVGJ80diOOyv2Cx-QSdHe8aE_KGUhwRYBlFTKmsHi8K5zAEkCOaPrrKOypnHCZIiKDzyQLUGma5YkaPrHQ2uPGBJlOYdiPbKbShNE0SgDi80Fja4GZvLGlkmFrzrMK7oqVytPJHLrq63tGUAyrjfNUAGfR25Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f49a9fe65c.mp4?token=q3V3rZCUsHYw54MdI_yer0AOO21QKWMwOZal4P3YC1vye7kFfWucO5ZoFcsazW2MCUg5-coCqmJHLYaQyqIFxy7xTGHXPwsmEy_iIjXOGXUEQMQMxUygov-gtjk8s-2ysYcm7bbpHW3Hsi_QmZHZgpeykqjw6MU4bCbPUqllfJu5RYtl-nn7k-AEfUVGJ80diOOyv2Cx-QSdHe8aE_KGUhwRYBlFTKmsHi8K5zAEkCOaPrrKOypnHCZIiKDzyQLUGma5YkaPrHQ2uPGBJlOYdiPbKbShNE0SgDi80Fja4GZvLGlkmFrzrMK7oqVytPJHLrq63tGUAyrjfNUAGfR25Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
🇧🇷
برزیلی‌های ساکن آبادان در جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/93587" target="_blank">📅 12:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93586">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a638ae04ef.mp4?token=FDsKI6_ePIBZ__UXli_wfKqs1GW65cOni9hOzi3yHFAzaL9U-Csu8Kv8RKxMct7npr64Igse_zG8Cn6ZctrXagUxTsxBRCbEL7JqwYvAc3Gxzjffohgn3vVzq4vZLQqi4RiR6JFa22Tv3F23DgPH-Eqa2vKHl9VTpGVdcyqYUMRuoFc4cyeCkvQs8HiJ2m_AeQbuwiulbZKo8FmdfzoLIYazLpUpwCJX15yXJtMzvFS-FdE3nZbFMES76icZYi266Wn1xzsuDy06ipUPB_eCNTqhM0x7OdzTzEgFpFq5mNfogcfQjDXd8cLlwdvYERRREPR25g1idgHsfbkcwtE3uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a638ae04ef.mp4?token=FDsKI6_ePIBZ__UXli_wfKqs1GW65cOni9hOzi3yHFAzaL9U-Csu8Kv8RKxMct7npr64Igse_zG8Cn6ZctrXagUxTsxBRCbEL7JqwYvAc3Gxzjffohgn3vVzq4vZLQqi4RiR6JFa22Tv3F23DgPH-Eqa2vKHl9VTpGVdcyqYUMRuoFc4cyeCkvQs8HiJ2m_AeQbuwiulbZKo8FmdfzoLIYazLpUpwCJX15yXJtMzvFS-FdE3nZbFMES76icZYi266Wn1xzsuDy06ipUPB_eCNTqhM0x7OdzTzEgFpFq5mNfogcfQjDXd8cLlwdvYERRREPR25g1idgHsfbkcwtE3uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
پاراگوئه با این سیستم هواداراش حیفه امسال شگفتی‌ساز نشه و به مراحل بعدی نره :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/93586" target="_blank">📅 11:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93585">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYIt76jbpb4VQGmu0tacVuWrUQ67iGyLqM6IGLNx9WT2pPnFlCEF_hkm7JVVJyXDUuoifCmk_RgIr1q-Gz7QtV8GNLqt5ncz7X6oFiCJi4d2RJrcqSEpcK1vudH8_FUVjxja_o_ldnZ0VkQICZsKLzhDMzzHkf7vc0PQxK0KSaOyquKp7tn0XcD8bp2OR5zD4cVvhaj--khzvsvW19V-x5YwlU6RZTG2dMYRFYFLnwONR9RfO99CgveB96XsscLciS5bGTSK6OF4qCGX8sRK4uGY8mGQrjdn6Q2NCoCtqtwhCMMW2_NEizuWkwjv4SunX7nMtbPDiRXA4a6j-up7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
پشماتون بریزه ووزینیا بعد از درخشش امشبش جلوی اسپانیا تعداد فالووراش از 50 هزار تا به 1.6 میلیون نفر رسیده و همینجور داره میره بالا.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/93585" target="_blank">📅 11:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93584">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15c36b833.mp4?token=mvXYn6P-OKf73WGSuLQoCtTIGkksWCWOsomqrdV5tPWd7M-u6ucccTSCzUtynJgSNgrD_zuIT30neWalkvfjZ87onGmIKXjKCotroom05-dEtxdxK0vw7abT_iEFhijfiwxfpVuOEKxHRI0nWPvq3skd7L1TlQrQ46yfz6T-LVfYsDfZMJ_q6yJnZt6Gi-x129wihzNeh5bwuIDu5YYWVks7q88U3LhZtlpftpC7oCMTxjCPiZ67PUtDEyBvPvTv9QTM_Io5G1X19YHBFQUlUC4JGzuXgcJIS1lsJIGudBe6bk1ajnytuikwNwMSiqVkgeWI0E3mflHLvzPXcqhOTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15c36b833.mp4?token=mvXYn6P-OKf73WGSuLQoCtTIGkksWCWOsomqrdV5tPWd7M-u6ucccTSCzUtynJgSNgrD_zuIT30neWalkvfjZ87onGmIKXjKCotroom05-dEtxdxK0vw7abT_iEFhijfiwxfpVuOEKxHRI0nWPvq3skd7L1TlQrQ46yfz6T-LVfYsDfZMJ_q6yJnZt6Gi-x129wihzNeh5bwuIDu5YYWVks7q88U3LhZtlpftpC7oCMTxjCPiZ67PUtDEyBvPvTv9QTM_Io5G1X19YHBFQUlUC4JGzuXgcJIS1lsJIGudBe6bk1ajnytuikwNwMSiqVkgeWI0E3mflHLvzPXcqhOTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
توجهتون رو به گزارشگر کانادا جلب میکنم.
مهدی گاییدی
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/93584" target="_blank">📅 11:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93582">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K07xfeqxUt9fKE6PAZ3y8hDdgmp2D00W85pp6kovANAb298wwbnUkcI_9qrOnTZtIcPGaH32-g-g1yMPFDh2rWHLmKpqemS9pAtDL_G4bgRr7Ie5rdHNcB8WrC6xoWnkQJsqhHLTSJd_NUsdXcIZTBFNSEOk4hEmoiKBGkguH0NtpEdTCTDQ3nx_lSap16a3_OnQLMJs0MAwr_RthlTZRcnee9q0z07qSITcib-1JYOzpvC_z0GqyAfyejEV0mOQOnXVEsYcY6ZNTbxXdfjJ1oj5bQs1_wenYr561uHCZmITTpsrUY7KwoMQAFShLb06X8UOmxD_58a9CRR0J5z4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tzv4qXwkT6Q_r02PRErshK4hPuOuRfrA-G9VSAiYcjf-k1lODJ16wPDQqD5R-x2-qw2kZUvi7mVR7vPRxN62IQBoFj-w8tlRMfXtuAqEPyvCMAk9g7av0Huh8OGC9Fa7j5-o465QKa0Qdv4IrjlhHvdO8X6ZDwsayKjX12vHHTWiRmQYS6bO7lPOecmZ2e4d2TwZ2DsrHVlufy-S7W6UAjyDQ_GaivNk3iVX-fTtq-nW-sUfYDihnC4bCTcbMRfWblzyefZE7rkrh6igqYQ_MjiDRFypz2CApl9bqqT430gUbQgf88WZ078w7Kyf1cS3SK-xuu4kQRk_YfkV_9wSXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
گزارش اتلتیک از گزینه‌های باشگاه رئال مادرید برای تقویت خط دفاعی:
◀️
نیکو اشلوتربک
◀️
روبن دیاز
◀️
الساندرو باستونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/93582" target="_blank">📅 11:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93581">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCCKB_BCF6ENArddNTOIZbiSzoian-yWs6PfoCzGBtxppMWBtkZbgPz_tTkwymBKD_uzm9hkuyDcgGMGda6IjH-BFXWzRkvm6-On_ycVrsk2f4xEDAzG6CSD4J9uh9vt0eZ3Pb2g8e5HsVVZZCHcEtaK2bvEnNR6WTilBMiPtjvvnSEkCcN-uMqPfmQJh6pEqHtMCJBgE2xasx_cJpsYyzwDBuwyTAKVjeau4CYhRHRHMOSNs4-u5nVW18JsWNJddvRRbTU9CsaTA2HhFQKuF2rBb3DCULXIP791GQBSP1O7HQZU61zY_pjsRy9hf_-OYc5GzyzWsy3qekNAety48g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
گزارش اتلتیک از گزینه‌های باشگاه رئال مادرید برای تقویت خط دفاعی:
◀️
نیکو اشلوتربک
◀️
روبن دیاز
◀️
الساندرو باستونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/93581" target="_blank">📅 11:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93580">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7db3cbe5.mp4?token=ZSrcMbRs-ujq_YViPkTDWfzZqWgzUOm8_2xaopNTZes1sXSosCQAWdYetZ6oWMdzCFIEQhMEigvPbphYxT5jWwRTDot022Z_0uhWS2GtxJlD35-hKl5QmfIMfQLkSQ0SIjtQboEzFf8SXzhRhBpxE27ED7WrLYVRlFMjOo4-uKo8qvwM5XCGyQ5QLmGWQgL7q5LCtz_EX6eCFPYhsVjtmODmbt4AeA8Y-wgxp_4oMFPipDRe1jCjF__cg5KA5VYbaK3oKE00KpM0DSASpCq8kTBidCv3L_9wCKls3MWre_R9h2xFblZkuHk5xZ-SleRbCBCzO64PCX19oGGtelMPfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7db3cbe5.mp4?token=ZSrcMbRs-ujq_YViPkTDWfzZqWgzUOm8_2xaopNTZes1sXSosCQAWdYetZ6oWMdzCFIEQhMEigvPbphYxT5jWwRTDot022Z_0uhWS2GtxJlD35-hKl5QmfIMfQLkSQ0SIjtQboEzFf8SXzhRhBpxE27ED7WrLYVRlFMjOo4-uKo8qvwM5XCGyQ5QLmGWQgL7q5LCtz_EX6eCFPYhsVjtmODmbt4AeA8Y-wgxp_4oMFPipDRe1jCjF__cg5KA5VYbaK3oKE00KpM0DSASpCq8kTBidCv3L_9wCKls3MWre_R9h2xFblZkuHk5xZ-SleRbCBCzO64PCX19oGGtelMPfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🙂
کل‌کل بامزه ابوطالب با امیر علی‌اکبری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/93580" target="_blank">📅 11:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93579">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLB2U3xRGDVk09tLNKS4DZBOctPWjnSflrPOh2sEWeLiSMI-xFUtk1q3ovet-M0FbM5FQgckCFsr3XKonliRZe2hB-IaM9eu3Yu8Df5lMU2NdH5NVNtIqj_YaW3oUIZ-HvXvzBZmPN8blJDfDHb6LUAvc2Qshd2C10BEGByYDdziPUFN7hlWEy06VyNgP6Z2XBQWYjYxdBPY9xM9y2poAtA5BNAaYi9EE7CaoC9LVL2KFRLrhb4Vo_PRirc8j_p8EeA8rYcgXjo4BGtUUsAZiS_DxT6gDdEb9wlZEKmGs-1vKpZqeZaeUX6Y9GsZhGUngoDYunLNvm_T-r70-GdoGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇳
فدراسیون فوتبال تونس از انتصاب هروه رنار به عنوان سرمربی این کشور تا پایان جام جهانی خبر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/93579" target="_blank">📅 11:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93578">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_TFUM4e_ceYf9dnu7_3VY5otIvMZpT_mtgOOtvBgcB04wy1MAy3r0lnXRpuwvVpE2hVHV1XZsoISPfnM3WgMsmopE8xC-7p02VNQUS8SjEcfD2v379wjd2a4BtMJZAj9VBqBygQ75-oKkwRomv07z8LkQDpxggsO2bS9zouNlvsRjsE6RJiHR6Nrb_8SaV0yZBmJ6AxrUktWVu7MTRgJqKQiBDrecdtS2E0sbX_W-_8PaEGv7YGLyQBItrNLdvx0BBXYkiZsgzj0VBW6G8xGe2qLWhgdmHh9Tpo3Cumd5mlSLc2axK3pGqIpncCDDWekQRjcY2AGBoXX0rDNSM7Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنبد کاغذین:
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/93578" target="_blank">📅 11:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93577">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a7c2e1de.mp4?token=aicSgmH-aKK3U61L_qVqii-XzVRRBkhWKyN6VSHl8-ed58NURuUY902BJBb1bxhfczdesxtHkXRGMe0VxGabVp3I83bfTosWwq_nZa6ggO-6w5akLVr5UMOmQGFikt5RniYyQJbkGMBjLyf0Ss_tN5oriZgeZklb4-xfXOz2ZqSXdAWyO9Oys8ObuDfOtOn_ijm0jQM4ZI08-BhwGJpshmfQ0hadb7TJVeTxNmLs3eQFcz4D6GS6UFCUv1QlGHuwEd5ae-BvWFOeDjH3cdUTFMFBFpQ6Wd7muEKIp76BQKQcNRP1ngw-axcNAfJoasTa1ILNBc9BlIFnx2i5fMvHcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a7c2e1de.mp4?token=aicSgmH-aKK3U61L_qVqii-XzVRRBkhWKyN6VSHl8-ed58NURuUY902BJBb1bxhfczdesxtHkXRGMe0VxGabVp3I83bfTosWwq_nZa6ggO-6w5akLVr5UMOmQGFikt5RniYyQJbkGMBjLyf0Ss_tN5oriZgeZklb4-xfXOz2ZqSXdAWyO9Oys8ObuDfOtOn_ijm0jQM4ZI08-BhwGJpshmfQ0hadb7TJVeTxNmLs3eQFcz4D6GS6UFCUv1QlGHuwEd5ae-BvWFOeDjH3cdUTFMFBFpQ6Wd7muEKIp76BQKQcNRP1ngw-axcNAfJoasTa1ILNBc9BlIFnx2i5fMvHcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇸🇦
🇺🇾
عربستان سعودی در بازی سخت مقابل اروگوئه به تساوی یک بر یک دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/93577" target="_blank">📅 11:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93576">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31883b78b2.mp4?token=DhPrZ0blsnTAPRC1bjpiF99W_7rpWKcORYn3Az-yZBPkSeCFbl_nCv4AdNNfz_0jAC1jXS1_AMOVRxHUvogxuojswU4RtXkHnFIT4k7WPakx1S6kn_VivjCws8v6z2lyv411_uANLYLCNOq78EdBMsoeQsBCsH84okA4-TkFFBFjC42xwRP671-IPPOrtJljqkviEkPkG1mnjU541nW4-sZcSJkVBjzDQ20d9aG9L2sSrPc7am-OdztqLvd_ETxjgYExJLySTjsxQAu23cXk4Yxpf0uTyq1fP8Ds_9zEQ9pLDxXWm_6iUuOZL_zngOJl-RYPFoo6g8tiGpQXQR8-tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31883b78b2.mp4?token=DhPrZ0blsnTAPRC1bjpiF99W_7rpWKcORYn3Az-yZBPkSeCFbl_nCv4AdNNfz_0jAC1jXS1_AMOVRxHUvogxuojswU4RtXkHnFIT4k7WPakx1S6kn_VivjCws8v6z2lyv411_uANLYLCNOq78EdBMsoeQsBCsH84okA4-TkFFBFjC42xwRP671-IPPOrtJljqkviEkPkG1mnjU541nW4-sZcSJkVBjzDQ20d9aG9L2sSrPc7am-OdztqLvd_ETxjgYExJLySTjsxQAu23cXk4Yxpf0uTyq1fP8Ds_9zEQ9pLDxXWm_6iUuOZL_zngOJl-RYPFoo6g8tiGpQXQR8-tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
فیروز کریمی: از اینکه ژاپنی‌های رختکن رو جارو میکنن بدم میاد چون خودم شلخته‌ام!
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/93576" target="_blank">📅 11:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93575">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUwasNKIiMCU237MWNNK5XGfffN3z5RplP514RtrtgSeY9pijohLcMwRMPLJLnvKKj6vYT1FlG1ql3DyrbnSSUiJ32l8pEJY8XazhxDLPdcvMoLrortd1xFYnmVEsa32rr5rau-Eya-ribJ3JF3Gpr-_4sHJhHO-LeD8S6eHKNnujhrdlXDvzJ2Yr_SlrHpt8eTmW8RRkogSKKEwQL92su8l8VyjF80xBcfPpVTbzYtKJPFpTtiA5US-vXpabZRBQKtfakjyGInJattwW-s6CeV5Dx0kxx91Heh4wR85z4_FmCNV0fosh6LwBJvo_qnUSG36oF4nfDUJK_v4illF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
#فکت
؛
پشماتون بریزه که کیپ‌ورد مقابل اسپانیا، بیشتر از آرسنال در فینال چمپیونز لیگ مقابل پاریسن‌ژرمن مالکیت توپ داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/93575" target="_blank">📅 10:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93574">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f4a62cae.mp4?token=B1pao5H0xuDadBqlYaNvBJ8D6kcgFfCPIqsZjXKo14bW7ew-XHOsRlzIdH4LF16hTLnajLPKjEkHr1hm-slV1UHQrtEaySNdTpGts2Uc91ljOg5jLiiUehuUbeFRtdiTGIWhHYHJFTfawQeCzApuE8RnPHsfEXf_lwhe73gAD66GTdxVv5K5u_oih--y4UlpdgwZutSk0XW_vxvcxCDL-XTtODrccE2a8JfRVWgKd589HtmK72-DBhh55ttNaZGQ2iP7ijCwv4SCZ6DVN0fw3--GC5D44NWEaKG0J0JhvuxXJkkbTOSIjIEann2X0IeD3kUhoaKMkukv64n3y7UC6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f4a62cae.mp4?token=B1pao5H0xuDadBqlYaNvBJ8D6kcgFfCPIqsZjXKo14bW7ew-XHOsRlzIdH4LF16hTLnajLPKjEkHr1hm-slV1UHQrtEaySNdTpGts2Uc91ljOg5jLiiUehuUbeFRtdiTGIWhHYHJFTfawQeCzApuE8RnPHsfEXf_lwhe73gAD66GTdxVv5K5u_oih--y4UlpdgwZutSk0XW_vxvcxCDL-XTtODrccE2a8JfRVWgKd589HtmK72-DBhh55ttNaZGQ2iP7ijCwv4SCZ6DVN0fw3--GC5D44NWEaKG0J0JhvuxXJkkbTOSIjIEann2X0IeD3kUhoaKMkukv64n3y7UC6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
بررسی تساوی عجیب اسپانیا مقابل کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/93574" target="_blank">📅 10:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93573">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49803c87d4.mp4?token=AKNtnvOF3oqf28aRj42eZVwA8JQ0EGE1Wot8jwFAiGQIe6LsDfFfGiaCkyiBCSWS4WDXOTZpUv6e1HPGMyurpMx2Ay3dGKpM8tW9PL86yJ0FQMs_AGawhQQRe8wBugGK91bQ0BdCj2fd8MFpqka28w3PEfwO8ihe-zRY7UoKTnUMVKybd8PeAC8dFmDm8Nxpv5xA7iMZr5ERetjbmKpeL-FiBMqdlRQgiPEvAcnqoPt-jVhLkNj-6oREU6T6z6rrA5Ju308MAmdXWe-rvZ_SCPBgezPBAjz_ZYhmOZvIuBAQj_F8H52IR-oUHfMkoPi1Jehp88oHuNrf_S2VHvzAtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49803c87d4.mp4?token=AKNtnvOF3oqf28aRj42eZVwA8JQ0EGE1Wot8jwFAiGQIe6LsDfFfGiaCkyiBCSWS4WDXOTZpUv6e1HPGMyurpMx2Ay3dGKpM8tW9PL86yJ0FQMs_AGawhQQRe8wBugGK91bQ0BdCj2fd8MFpqka28w3PEfwO8ihe-zRY7UoKTnUMVKybd8PeAC8dFmDm8Nxpv5xA7iMZr5ERetjbmKpeL-FiBMqdlRQgiPEvAcnqoPt-jVhLkNj-6oREU6T6z6rrA5Ju308MAmdXWe-rvZ_SCPBgezPBAjz_ZYhmOZvIuBAQj_F8H52IR-oUHfMkoPi1Jehp88oHuNrf_S2VHvzAtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⁉️
👀
سوال ابوطالب‌حسینی از امیرعلی اکبری: شرخری میکنی؟
😂
😂
جوابشو ببینید عالیه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/93573" target="_blank">📅 10:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93572">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPYLtBRyHuAhK2BJESr0sJBoCDlCGZ9aGeA3KadlHPwRuBH4he6honlnWyWtNlMNg6x73t-vfvYMgtciIQyd9G09yQmoVVR3SvmHdUiCh-_CN4CuNH4b1jvyaKRF_f7HagZFosoOu8FhRi-O3ciizU0kjHFAcdMv89rCkU4auXw-tLcLPyCLnZ1-i2esSShVfksxkpfyfJscQv_JfvK-xuqCtoGpTb5Xc8yYrzxh3r4aI99njtOcOt2G3K0Z30tfUmeq5Al9-fxZisANfjQEGupBhg5_qiNHhPsW8565zyP6v36h5ies1eh1QdhCyaq_WwGwFX7Rp9lubZunhDxNqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ویزای مهدی ترابی یک روزه بوده و منقضی شده و اون دیگه امکان ورود مجدد به آمریکا رو نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/93572" target="_blank">📅 10:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93571">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trjGUsgk7glZTmoNtbrS30leQGRyE-pyEZblwurkh2m3AKHocw0Y7rXej5UFSpR-WN3D0CTDaETpQ5yEdJwyR09Swek_Eb-zXUJ0SLOuoabgJt6II4aXr6V9-ARAxAhajIB_xbpv_tnqsYmCFoxgMUc5GY594uXgJMIUWmw2cHIZwhAvInQcuCW7QPS5mlHudY1GF1bsIv6U2DGn4vwAyT74aWXy1cDknvSiSZQKmjJ1HhSVyiYGWPoFn_t1oqOc37viWrl00TQ5RslNC7gtJoF50OkalMxlje3CfKJeSVyqJTcbKzx_qlRXbow1h65RN1bRj-66lR4k4MypEkTDuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به دستور شخص اینفانتینو نمای کلوزآپ یا همون نمای نزدیک از تماشاگرا تصویربرداری نمیشه و به همین دلیل برخلاف بازی تیم‌های دیگه که تا نوک ممه زنا رو هم نشون میدادن این بازی نمای نزدیک هواداران ایرانی حاضر در استادیوم خیلی کم نشون داده شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/93571" target="_blank">📅 10:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93570">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd4dbbaa8e.mp4?token=rwMzUWdSrsUamm_AkjX6iHh3kA8BPGZli5SOvclRX-YkCQ7J3IhqAxrINialUVn5baaq66k_wSMxa-Ia-urng-NGYTAeMjC25Q4lzWwaiQlVui9MCV03jdQZA3qvBXZUGrh6rEiiGFCQ1Gqb2k6EfB3vuJPYd4hK_7OMejKE5pl8-o4sHdke4UIYx5fS4-8k8iKSddQksfa4wBB4PY_eQ8lP7S8Xi1ZamWtZ8Ff6xcc9WLh5zTogjXWPeSkpwA8xAFwVeVZb9EaNFRUX5WKEguheE0QQLEsXusmVkvg0c_CScC9Jwe3SCkCbyGOJCyEFRRb3x-ilzPhwgotraZpbFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd4dbbaa8e.mp4?token=rwMzUWdSrsUamm_AkjX6iHh3kA8BPGZli5SOvclRX-YkCQ7J3IhqAxrINialUVn5baaq66k_wSMxa-Ia-urng-NGYTAeMjC25Q4lzWwaiQlVui9MCV03jdQZA3qvBXZUGrh6rEiiGFCQ1Gqb2k6EfB3vuJPYd4hK_7OMejKE5pl8-o4sHdke4UIYx5fS4-8k8iKSddQksfa4wBB4PY_eQ8lP7S8Xi1ZamWtZ8Ff6xcc9WLh5zTogjXWPeSkpwA8xAFwVeVZb9EaNFRUX5WKEguheE0QQLEsXusmVkvg0c_CScC9Jwe3SCkCbyGOJCyEFRRb3x-ilzPhwgotraZpbFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
😂
حسین‌ماهینی بازیکن سابق پرسپولیس: تقریبا همه بازیکنان قلیون میکشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/93570" target="_blank">📅 10:02 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
