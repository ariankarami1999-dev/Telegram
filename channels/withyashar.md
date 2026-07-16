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
<img src="https://cdn4.telesco.pe/file/p-hI0ly1lm7c1VTKhaMth0gzLXHUlV2A-BH9E1cVMZJK35nMFBEVenufJqyVytgmMiKiMhSZw-8PipeW0OL4AsvSVTv4DKHUa4RDSIxQCltaRSvTzgS_mK-Y_kttN_AMOMJgVfwjnaLvbwxmhK7t1rDAj2_jZRvwg05tfLR6AyFWyXuz17WZhZo_F_84oiu7uPfagKdlVb0YlG3Ot02ftgh_xjncFzG_IMKxnVuggt2plHyAvbNfbzX9HElO_Cmu7UKR-tRxw6i4kf0iuOQn1DKAVvChCu1ER4wvWlxjZQvUhQruY2DltzEUVWSErjShU8GgIe0tNHUhTPsuuDBAbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 394K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 04:26:11</div>
<hr>

<div class="tg-post" id="msg-18327">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1feec959.mp4?token=STN_eKlm0oGj392Sa7SyaGqrzRimlN0LWJWT4O9kMfPqn3Z0KTfLuFhRtWS589hpbLYj5TnMzSoBmrS_HKVTB5FT0R8lZ_ImE3FxD1-zhFBusp2Pkg193AYzNPOEOFiIA7RafqeyAtN9BbMEpyywTuIXzJJ0G-P4tZ35Te6K4lZoj-rZ5BiQztr7lgC21273FrNOwsOgzmJN3m8DDzQ6flDlZXU0UKS3DjKs_Vm-diC9I5r-m94bEpKly4USAg461uvs-R_kgPCoQhpiuSS54DMZGdcLUNSJbxJ7vs3mVFDPWI8g-DHm5qlI2Jm0ummNTsC4s2w703bnwA9Ofuq9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1feec959.mp4?token=STN_eKlm0oGj392Sa7SyaGqrzRimlN0LWJWT4O9kMfPqn3Z0KTfLuFhRtWS589hpbLYj5TnMzSoBmrS_HKVTB5FT0R8lZ_ImE3FxD1-zhFBusp2Pkg193AYzNPOEOFiIA7RafqeyAtN9BbMEpyywTuIXzJJ0G-P4tZ35Te6K4lZoj-rZ5BiQztr7lgC21273FrNOwsOgzmJN3m8DDzQ6flDlZXU0UKS3DjKs_Vm-diC9I5r-m94bEpKly4USAg461uvs-R_kgPCoQhpiuSS54DMZGdcLUNSJbxJ7vs3mVFDPWI8g-DHm5qlI2Jm0ummNTsC4s2w703bnwA9Ofuq9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند ثانیه از اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/18327" target="_blank">📅 02:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18326">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قشم و سیریک هم گزارش صدای انفجار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/18326" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18325">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بندرعباس رگباری دارم میزنند دوباره
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/18325" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18324">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آغاز حمله جمهوری اسلامی به پایگاه های آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/18324" target="_blank">📅 01:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18323">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سخنگوی سپاه: دشمن تصور نکند که می‌تواند جنگ را فرسایشی کند
عملیات‌های ایران فعلا متمرکز بر انهدام زیرساخت تهاجمی آمریکا در منطقه است. سپس گام‌های بعدی آغاز خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/18323" target="_blank">📅 01:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18322">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">همین الان پایگاه هوایی بندرعباس رو زدند
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/18322" target="_blank">📅 01:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18321">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بندر صدای انفجار
@warroom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/18321" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18319">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پدافند شرق تهران درگیر شده
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18319" target="_blank">📅 01:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18315">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18315" target="_blank">📅 01:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18314">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش انفجار های قشم به حدود ۱۰-۱۴ مورد رسیده
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/18314" target="_blank">📅 01:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18313">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">استانداری هرمزگان تأیید کرد که نقطه ای در حوالی سیریک مورد اصابت موشک های آمریکایی طی اوایل بامداد پنجشنبه قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18313" target="_blank">📅 01:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18312">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/18312" target="_blank">📅 01:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18311">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بازم روستای «‌مسن» قشمرو دارن میزنند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/18311" target="_blank">📅 01:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18310">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پرتاب موشک از شیراز
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18310" target="_blank">📅 00:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18309">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قشم رو خیلی زدن پشته هم ۷-۸-۱۰ تا همه ریخت بیرون
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18309" target="_blank">📅 00:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18308">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d120a1732a.mp4?token=QtUOTsryPWXWWtSPQz0iXYDvvRQYtWafzVoER7MuIl-gTR7Qbi_KK6tzUqYmEGgwYV3C5IjNYOEXDCv3ooKMWod4Oq-ps-0Lkx9uAW5ZB5jm-e9KYsnhZZz5I767F5hvrVEqYIocTVZR0dFluNLvBmr_JcVuRJjWqnrBHI1MsICLLj1YNHIVeaZk5EE8LFtaAvquX5wXgh4tPuYiouH26j4HJ3Cc0xOoCniMrQWIvJhmkyxms6Wpi_O1VI-Cmr4g2mkYAFMQUyF1Dn0sGorP0BEx9Yl2da4IQHabXOXoJ5EBb_yCw2IVg2WitdktuIFzzcEGisMgpPz9SBq16oacby8F1wo2oyuUDplPBFqctlHbUC_6qwAcEe6b2bmZFreodFJKcM7mUbmGW1go-jDBWfx5K7XHv6u-_mq1LP8h9IVonUuyM1UtZau12qK680zHxQ_5UJNpkPn9tfTH-WmuQGtafnjecgT6X9JlHzdgsNH2KEKoJ9vTklL7keQKZJ3ZS1-Jzb2jvF8c61gN2tMbCl83U9sJhSUq9-BJ9nXnO2L1DAM0_OygLzsxvCHdGs2Yk9YUHL0hyH14c4G54xYylymmORH3_MlIYgzGAufvUiAF6GjYZmAUqI-1_dFGinSeHxeukQv17xMhgs_3x5AaKutXQft9huhwDJ3D7n85tM4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d120a1732a.mp4?token=QtUOTsryPWXWWtSPQz0iXYDvvRQYtWafzVoER7MuIl-gTR7Qbi_KK6tzUqYmEGgwYV3C5IjNYOEXDCv3ooKMWod4Oq-ps-0Lkx9uAW5ZB5jm-e9KYsnhZZz5I767F5hvrVEqYIocTVZR0dFluNLvBmr_JcVuRJjWqnrBHI1MsICLLj1YNHIVeaZk5EE8LFtaAvquX5wXgh4tPuYiouH26j4HJ3Cc0xOoCniMrQWIvJhmkyxms6Wpi_O1VI-Cmr4g2mkYAFMQUyF1Dn0sGorP0BEx9Yl2da4IQHabXOXoJ5EBb_yCw2IVg2WitdktuIFzzcEGisMgpPz9SBq16oacby8F1wo2oyuUDplPBFqctlHbUC_6qwAcEe6b2bmZFreodFJKcM7mUbmGW1go-jDBWfx5K7XHv6u-_mq1LP8h9IVonUuyM1UtZau12qK680zHxQ_5UJNpkPn9tfTH-WmuQGtafnjecgT6X9JlHzdgsNH2KEKoJ9vTklL7keQKZJ3ZS1-Jzb2jvF8c61gN2tMbCl83U9sJhSUq9-BJ9nXnO2L1DAM0_OygLzsxvCHdGs2Yk9YUHL0hyH14c4G54xYylymmORH3_MlIYgzGAufvUiAF6GjYZmAUqI-1_dFGinSeHxeukQv17xMhgs_3x5AaKutXQft9huhwDJ3D7n85tM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : بزن زنگووووو
🔔
@WarRoom
رکورد جدید ۱۱ تانکر سوخترسان در خلیج فارس
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18308" target="_blank">📅 00:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18307">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش انفجار های پی‌ در پی قشم
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18307" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18306">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">به طرفداران ارژانتین تبریک میگم از جمله بی بی عزیز
😂
من خودم که فوتبالی نیستم ما دنبال این توپا نیستیم
😉
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18306" target="_blank">📅 00:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18305">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9690f3c84.mp4?token=Jdjpr2skKWwU0l0hP-JNd5JifqLj1Idg-7SFPTuffkxzeH0O8laQIn9_lEIGshcR3PSU16GU29qPU-BT1LYhWLlCD6gukQdluHyd4jBUAt_JucKC05YOOtVc6Kw1QWKc_Eo1LV1Ov-_80DaC-BYIiLuIszYT3BcAofC3WA6n-SAr5soi504_q_K4nVMPH98K8zXzzycIDRsHd1uuZN7c8d2NlJfq1lQJ1k3G7cVeX1rYHLVw1XATThBb0mggbpUPICntB_wV5UMtF23XQHlt9XwaoCXvL-KGJZEkRQOra7blVSAZu-JSD2y7r72SXwpTmacWAb9mFHWOKr87hEsBjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9690f3c84.mp4?token=Jdjpr2skKWwU0l0hP-JNd5JifqLj1Idg-7SFPTuffkxzeH0O8laQIn9_lEIGshcR3PSU16GU29qPU-BT1LYhWLlCD6gukQdluHyd4jBUAt_JucKC05YOOtVc6Kw1QWKc_Eo1LV1Ov-_80DaC-BYIiLuIszYT3BcAofC3WA6n-SAr5soi504_q_K4nVMPH98K8zXzzycIDRsHd1uuZN7c8d2NlJfq1lQJ1k3G7cVeX1rYHLVw1XATThBb0mggbpUPICntB_wV5UMtF23XQHlt9XwaoCXvL-KGJZEkRQOra7blVSAZu-JSD2y7r72SXwpTmacWAb9mFHWOKr87hEsBjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد نیروهای آمریکایی در
۱۵ ژوئیه
و در چارچوب اجرای
محاصره دریایی علیه ایران
، یک نفتکش خالی از محموله را که در حال حرکت به سمت یکی از بنادر ایران در خلیج فارس بود، از کار انداختند.
بر اساس اعلام سنتکام، نیروهای این فرماندهی نفتکش
M/T Belma
با پرچم
کوراسائو
را هنگام عبور از آب‌های بین‌المللی به مقصد
جزیره خارک
رصد کردند. به گفته سنتکام، این کشتی تجاری با وجود دریافت چندین هشدار، تلاش کرد محاصره دریایی آمریکا را نقض کند. در پی آن، یک هواگرد آمریکایی با شلیک
موشک‌های هلفایر
به دودکش کشتی، آن را از کار انداخت. سنتکام می‌گوید این کشتی دیگر به سمت ایران در حرکت نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18305" target="_blank">📅 00:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18304">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جی‌دی ونس درباره ایران: «ما قرار نیست فقط بمباران کنیم، بمباران کنیم و باز هم بمباران کنیم.
ما تلاش خواهیم کرد از نیروی نظامی‌مان به‌عنوان یکی از ابزارهای متعددی که در اختیار داریم برای حل این مشکل استفاده کنیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18304" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18303">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انگلیس ۱ ، آرژانتین۲
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18303" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18302">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18302" target="_blank">📅 00:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18301">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انگلیس ۱ ، آرژانتین ۱
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18301" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18300">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef977aa121.mp4?token=oZ15KL4WoLPAjqHrSVyOPomClmQWCjmTvmpshSLNdQUYdiK2G8W-79M0BExe732Im-AetHMqKecrZzW1iED7ZbuRn8eYYx98d3CiAXuNaTGMaNihmPyNE5y0qOVw4g_g34x5-r86zGQrST6tj6OMt8iaFx2TZekPvDcoHWUN_vqZq4VTlxDfEGJKSfRH4zbL_5UTEq9qyURWqbbBNbVUJXJeF7TqQb1QVff3hVp5iNrSYnq1cPsXxPe_4aa5hG-wvyL37qaA4sAjxPR3M8HHTGzIiz3kw-_TRLgqGUJeu_1Cdy5iSscMctS86cSd8g_SMLodDmjLOgrz2XwGWiPdnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef977aa121.mp4?token=oZ15KL4WoLPAjqHrSVyOPomClmQWCjmTvmpshSLNdQUYdiK2G8W-79M0BExe732Im-AetHMqKecrZzW1iED7ZbuRn8eYYx98d3CiAXuNaTGMaNihmPyNE5y0qOVw4g_g34x5-r86zGQrST6tj6OMt8iaFx2TZekPvDcoHWUN_vqZq4VTlxDfEGJKSfRH4zbL_5UTEq9qyURWqbbBNbVUJXJeF7TqQb1QVff3hVp5iNrSYnq1cPsXxPe_4aa5hG-wvyL37qaA4sAjxPR3M8HHTGzIiz3kw-_TRLgqGUJeu_1Cdy5iSscMctS86cSd8g_SMLodDmjLOgrz2XwGWiPdnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما وارد خاورمیانه می‌شویم و آن(تروریسم منطقه) را از کار می‌اندازیم و بعد به خانه برمی‌گردیم. همه می‌پرسند چرا این کار را کردیم... ما بزرگی و عظمت بدست میارویم مثل کاری که ونزوئلا کردیم ( همه شوک شدن)
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18300" target="_blank">📅 00:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18299">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارسالی : شهرک صنعتی زنجان تمام شیشه هامون ریخت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18299" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18298">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ درباره ایران:
بسیار زود شکست خواهند خورد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18298" target="_blank">📅 00:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18297">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اقلیم کُردستان: ائتلاف بین‌المللی به رهبری آمریکا، 8 پهپاد انفجاری سپاه را بر فراز اربیل رهگیری و سرنگون کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18297" target="_blank">📅 00:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18296">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7046544db.mp4?token=dVKPB3qRXLPGmGhhseCSPWbfr2tVsgL7x0wqXNwmweUTmCaFNf0f0fFsoU8NI746PV30KIgsYx1AgvdJTUr7ObjT8mHgtkGI1_LGah977GBjdGw8iYRMPZo6bpfAvsHXlcoveGw0mWakMOPXOqzooUQhcrJwNUV4FAUHNNaTHfGC-5zm-p1YItJl5I76R7IzDBRM3qlAwfdWCquy9c2t_JaPMpt3Lg_DPEEO6rSTyJ5PSCGi2lGE4_-9hxpIlefKg3JA8s2rZsS-F_3jtoSQ3UwBo_oIKllu74GsghbwU4tlmAr-u0ARjaa_Hko4eXwwWxfEKpARIQB09A5sIqjqfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7046544db.mp4?token=dVKPB3qRXLPGmGhhseCSPWbfr2tVsgL7x0wqXNwmweUTmCaFNf0f0fFsoU8NI746PV30KIgsYx1AgvdJTUr7ObjT8mHgtkGI1_LGah977GBjdGw8iYRMPZo6bpfAvsHXlcoveGw0mWakMOPXOqzooUQhcrJwNUV4FAUHNNaTHfGC-5zm-p1YItJl5I76R7IzDBRM3qlAwfdWCquy9c2t_JaPMpt3Lg_DPEEO6rSTyJ5PSCGi2lGE4_-9hxpIlefKg3JA8s2rZsS-F_3jtoSQ3UwBo_oIKllu74GsghbwU4tlmAr-u0ARjaa_Hko4eXwwWxfEKpARIQB09A5sIqjqfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18296" target="_blank">📅 23:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18295">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اهواز همچنان زیر حملات
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18295" target="_blank">📅 23:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18294">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انگلیس ۱ ، آرژانتین ۰
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18294" target="_blank">📅 23:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18293">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">@WarRoom
حمله زمینی ؟</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18293" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18292">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=l8AXSmBfHTADvlh0VdWhxZ36n4M4wkQXboH5LajFL94ZqmqedWmP_m2_t0Ou0Z9sS9xBU0hXZ1TfYn-NJDV6trru19QaZjKqupJV80qtzrho-voqSvEgiYq8K-OzThX4tnfJlioD0pVOglPeNqeaKrRju-o0anq23YqpZ9A9qIVj2TuMlv3z7OWC1CyXTixn6O-MF6OLzH3ijU-0v_veIZAQHFwWPC0lGwmSTelson6-1XCBzoHpRcxGrX865jpK9VCLrzpPWZmiEqnOgmAQECNNIyKOjusckHXucK_f4s_e90_MdBILxaCJZU21pL4WgRUQ4CJpYOvojvxc4VNFkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=l8AXSmBfHTADvlh0VdWhxZ36n4M4wkQXboH5LajFL94ZqmqedWmP_m2_t0Ou0Z9sS9xBU0hXZ1TfYn-NJDV6trru19QaZjKqupJV80qtzrho-voqSvEgiYq8K-OzThX4tnfJlioD0pVOglPeNqeaKrRju-o0anq23YqpZ9A9qIVj2TuMlv3z7OWC1CyXTixn6O-MF6OLzH3ijU-0v_veIZAQHFwWPC0lGwmSTelson6-1XCBzoHpRcxGrX865jpK9VCLrzpPWZmiEqnOgmAQECNNIyKOjusckHXucK_f4s_e90_MdBILxaCJZU21pL4WgRUQ4CJpYOvojvxc4VNFkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18292" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18291">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f335c33224.mp4?token=INkkKzS4WH5H2FwYL_EgN_tt_1gguqm1IYXA87dgYsd9ioAfZ7TlYoRTjkhLFqPUEyZV079rIFYAqdoamGJpsf4OP8oyXgwDRJhgBL9wLg0T2iQDM8j8hUXldt36aDIs2GuXmGXX7WUXHhn6neZud_9liUwi3603w20dOq8kHCGjyI3rF_0C7gjW_R4tECMx2iZKYFqO4tcG0yKrGDo1T-AOoC4BwI9QfI4NvAG0eG4KHuHYutwChRuAGL43bkhrf_wF-10nBGWOEpPgMJ1v3VEH2tWOJ-c720LjZ2LkF-xsvUIyat62mOqic9SjvWkWD8C023lTUeLfH3SA_MqKZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f335c33224.mp4?token=INkkKzS4WH5H2FwYL_EgN_tt_1gguqm1IYXA87dgYsd9ioAfZ7TlYoRTjkhLFqPUEyZV079rIFYAqdoamGJpsf4OP8oyXgwDRJhgBL9wLg0T2iQDM8j8hUXldt36aDIs2GuXmGXX7WUXHhn6neZud_9liUwi3603w20dOq8kHCGjyI3rF_0C7gjW_R4tECMx2iZKYFqO4tcG0yKrGDo1T-AOoC4BwI9QfI4NvAG0eG4KHuHYutwChRuAGL43bkhrf_wF-10nBGWOEpPgMJ1v3VEH2tWOJ-c720LjZ2LkF-xsvUIyat62mOqic9SjvWkWD8C023lTUeLfH3SA_MqKZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز، جهنم شده ه ه ه ه
معلون نیست چیه همینجور میسوزه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18291" target="_blank">📅 23:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18290">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پدافند زردشت اهواز مورد هدف قرار گرفته
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18290" target="_blank">📅 23:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18289">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">۵ انفجار استان کرمان
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18289" target="_blank">📅 23:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18288">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7aa831776.mp4?token=LdC_CneiznVOxVw6mbZtTmAbku_DqRR52JPeL8YXRva6fWMQp9SISmiEiT4VA6PONXMHzK6rDl--pIlsMblcpOFyVb5S2hWkhm6tXnWZrfBpUtXhkMgltgo_l921j4pwKyLXsdFiJmHSYUrsAIg0_9mhZg2mQoz7eDV1qz17yJZwlTitV7q7KJeM-PcxpyxJL8wxlvP4tDH9UxgJmoydWfgOGSMg3fDR9OpDehtgFcijK0jqFfNBqW0VKjkBi7bxtpWzznrNDRNNEXE1dPP8lKKya7VV77ZCfANqmzf3BotHcpoy8MMy48SQA8k8Jh8rOECojg2eTKcRmCb8fau-oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7aa831776.mp4?token=LdC_CneiznVOxVw6mbZtTmAbku_DqRR52JPeL8YXRva6fWMQp9SISmiEiT4VA6PONXMHzK6rDl--pIlsMblcpOFyVb5S2hWkhm6tXnWZrfBpUtXhkMgltgo_l921j4pwKyLXsdFiJmHSYUrsAIg0_9mhZg2mQoz7eDV1qz17yJZwlTitV7q7KJeM-PcxpyxJL8wxlvP4tDH9UxgJmoydWfgOGSMg3fDR9OpDehtgFcijK0jqFfNBqW0VKjkBi7bxtpWzznrNDRNNEXE1dPP8lKKya7VV77ZCfANqmzf3BotHcpoy8MMy48SQA8k8Jh8rOECojg2eTKcRmCb8fau-oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلشهر ، چابهار
@warroom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18288" target="_blank">📅 23:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18287">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارش انفجار کنارکککک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18287" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18286">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دقایقی پیش ترامپ: به این نتیجه رسیده ام که نمیتوان با سپاه پاسداران انقلاب اسلامی مذاکره کرد. خبرنگار: آیا یعنی ممکن است همانطور که با داعش کردی، آنها را از بین ببری؟ ترامپ: "بله، درست است. خواهیم دید چه میشود @WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18286" target="_blank">📅 23:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18285">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دقایقی پیش ترامپ: به این نتیجه رسیده ام که نمیتوان با سپاه پاسداران انقلاب اسلامی مذاکره کرد.
خبرنگار: آیا یعنی ممکن است همانطور که با داعش کردی، آنها را از بین ببری؟
ترامپ: "بله، درست است. خواهیم دید چه میشود
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18285" target="_blank">📅 23:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18284">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انتشار این پست و معرفی من در گروه ها و تمام دوستاتون تنها کمک شماست
🙌🏾
🌐
instagram.com/Yashar
🌐
t.me/WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18284" target="_blank">📅 23:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18283">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش انفجار بوشهر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18283" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18282">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">️تسنیم:
پرواز جنگنده‌های آمریکایی بر فراز سواحل جنوبی سیستان‌و‌بلوچستان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18282" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18281">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اهوازی های عزیز ماشین بازن ، به چیزای خوب فکر کنید بعد آزادی،  پیست میبینمتون
❤️‍🩹
قویییی‌ باشین
🦾</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18281" target="_blank">📅 23:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18280">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اهواز سفتتتتتتت زددددد اینبار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18280" target="_blank">📅 23:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18279">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هم اکنون پایگاه شیخ عیسی بحرین هدف موشک های ایرانی
@WarRoom
هدف نه اصابت</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18279" target="_blank">📅 23:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18278">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اهواز بازم زدن
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18278" target="_blank">📅 23:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18277">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🤯</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18277" target="_blank">📅 23:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18276">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b902c0e83.mp4?token=bD7PP93Cg1za-mlG3Zxc6MY3V2JXKFoeslrKmgxJlvU9C2U4m4-Wbyn8046YzId1jqzkie6Lhb5kIpBGX7DA9N8MqVjI9NwWSkLJ-vWc8f8uSv0Y6DuFlmwl_L0tBMRcMtQojtCcOVKPvLzYNCzFUDnmDCOMhKEAgpiBTU6Y87v_o0E2igZzpC6QzJm4LDT48V8PF7mDPQwnTJpgi_UGEN-wJbXhKXMNZ8hafvqK38rBO9Iz6Eb_gbKpsIfDt20Y6-WZZYn7VYXQIXBoiU860Z6klkYHCuSBtfEvmcX0BZ3VpFJYwAyYhyAawC2z_ezNLE5s98AZ8Ah6HoClE9W0_IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b902c0e83.mp4?token=bD7PP93Cg1za-mlG3Zxc6MY3V2JXKFoeslrKmgxJlvU9C2U4m4-Wbyn8046YzId1jqzkie6Lhb5kIpBGX7DA9N8MqVjI9NwWSkLJ-vWc8f8uSv0Y6DuFlmwl_L0tBMRcMtQojtCcOVKPvLzYNCzFUDnmDCOMhKEAgpiBTU6Y87v_o0E2igZzpC6QzJm4LDT48V8PF7mDPQwnTJpgi_UGEN-wJbXhKXMNZ8hafvqK38rBO9Iz6Eb_gbKpsIfDt20Y6-WZZYn7VYXQIXBoiU860Z6klkYHCuSBtfEvmcX0BZ3VpFJYwAyYhyAawC2z_ezNLE5s98AZ8Ah6HoClE9W0_IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان پاسگاه احمدریزه چابهار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18276" target="_blank">📅 23:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18275">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اهواز قیامته دیگه نگمممممم</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18275" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18274">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvZWTm51n3QpPGE-YEZhwJ6ANvDF4EksLpAz7j4sSVDcvixZpNuMq2mENbg_hjWNHtSOICiDUH-MTMkw7faV97gbYB2kCYhbcATkOxJbWswhEtVLnJHyecSffHy5lreLBrkcT8X_23swiSoz4gN6M-osG3vrYQoThFJU495XDHwLq64tzgtzEl7-7IOWeMXs83vl8I73RgMSlq3yHcW1nPFe6S1zYyqfSpkhBIpw0UJT6pyJCGp6ur8_H-CuvVbKyJQsLgsFHkbkWZsInrHQnuFptu_2jN4JOu3LVAUBFwn4DY_KcmgcPFarcWw3eF_QvCDDpl-N3HpxWmPD-1SCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راسک سیستان بلوچستان زدن
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18274" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18273">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294a418fbc.mp4?token=ki1PHAYuqyInm0BRDoht24tcRK-DC73uQ9nXJ4XzS5tCgYWmD_swyKynGHcDPoDvYqGIuz0JD9Ikb0aj7oi3tczMY107kXWjl3Z8A6uHcARbpEDM3N4kb5fOX9KUHEbTeCA0QouucETmLnrJzzlsVBXGv0qXmqBk2UjY-oMJ_lC6Ocd2aY5pfM33hZyYK219h8pS5FwMzr9O-rm06xEG1Mt1-pL3HcJUMtm7hdPp-8eDuawbHXlytDIFyTx71_1vuiyzV4kW2wV6Eu35lsGPOrx9O9y0W9dzgHgX_bvub3kziECkPx9lsG4k3rS-XJQ3ICN3IDnogHAsEoHWxBSU2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294a418fbc.mp4?token=ki1PHAYuqyInm0BRDoht24tcRK-DC73uQ9nXJ4XzS5tCgYWmD_swyKynGHcDPoDvYqGIuz0JD9Ikb0aj7oi3tczMY107kXWjl3Z8A6uHcARbpEDM3N4kb5fOX9KUHEbTeCA0QouucETmLnrJzzlsVBXGv0qXmqBk2UjY-oMJ_lC6Ocd2aY5pfM33hZyYK219h8pS5FwMzr9O-rm06xEG1Mt1-pL3HcJUMtm7hdPp-8eDuawbHXlytDIFyTx71_1vuiyzV4kW2wV6Eu35lsGPOrx9O9y0W9dzgHgX_bvub3kziECkPx9lsG4k3rS-XJQ3ICN3IDnogHAsEoHWxBSU2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز الان
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18273" target="_blank">📅 23:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18272">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اهواز رو همینجور میزنه کلا
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18272" target="_blank">📅 22:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18271">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش انفجار سنگین بندر عباس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18271" target="_blank">📅 22:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18270">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سنتکام : در ساعت
۳:۰۰ بعدازظهر به وقت شرق آمریکا (ET)
(۲۲:۳۰ به وقت تهران)
، نیروهای ایالات متحده عملیات
دومین موج حملات
امروز علیه ایران را آغاز کردند.
این حملات توانمندی‌های نظامی ایران را هدف قرار داده است؛ توانمندی‌هایی که به گفته آمریکا برای تهدید کشتی‌هایی که به‌طور آزاد از
تنگه هرمز
، آبراهی بین‌المللی و حیاتی برای تجارت جهانی، عبور می‌کنند، مورد استفاده قرار می‌گیرند.
ارتش ایالات متحده اعلام کرده است که
به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، ایران را در قبال این اقدامات پاسخگو می‌داند
@WarRoom
یاشار : دقیق نیم ساعت بعد که گفتم شد
💥</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18270" target="_blank">📅 22:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18269">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سنتکام : شروع کردیم
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18269" target="_blank">📅 22:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18268">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجار سنگین در اهواز حتی از قبلی ها هم سنگین تر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18268" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18267">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دوباره چابهار رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18267" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18266">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxxYR_zCbq76yxQ8yF9yE39uyxWaBB0Fq6-_NfdYVGd2-Q9GVU0GWXDrAgeI3coET2fFj3FMcS7oJWMge_9QOqiF7h_Lw_zUlyw3cidaTfT0zMHMWn-hmHmyJTNq6KwAuBeC9BD8OkuhdpVyKjQlWYqE0biaDCcJAztYv0jkoIV47ik0BAFmn0QcYQG9v5GjNG_hlPPV4keQgOHZ4JO_CEU4twwWvsv_NitJyndfCh36llVJfQJAfWtY6sgY2nq4QFiymBACkHYKCMXqtSIx8HJmMkUExS-Zj6LcmV4VDYarUkqG0SPBOFPUWG_tUOEDjLHxrLVzg9jvj3g5dnps2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوجان در کرمان  پایگاه سپاه رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18266" target="_blank">📅 22:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18265">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجار سنگین منوجان در استان کرمان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18265" target="_blank">📅 22:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18264">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">در مجموع ۸ انفجار شدید در اهواز گزارش شده
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18264" target="_blank">📅 22:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18263">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">۵ تا دیگه اهواز رو زد شهر تکون خورد
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18263" target="_blank">📅 22:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18262">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">۲ انفجار شدید چابهار
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18262" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18261">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش انفجار چابهار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18261" target="_blank">📅 22:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18260">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یاشار دوتا دیگه زدن اهواز خونه داره می لرزه صداش ۲ برابر دیشب
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18260" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18259">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یه نیم ساعت دیگه سنتکام بیانیه میده شروع کردیم موج ۴رم
😂</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18259" target="_blank">📅 22:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18257">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">۳ تا سنگین زد اهواز و انگار زلزله اومد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18257" target="_blank">📅 22:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18256">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجار‌ اهواززززززز
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18256" target="_blank">📅 22:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18255">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ :  من از تعیین ضرب‌الاجل خوشم نمی‌آید.
@WarRoom
یاشار : نیست خیلی هم رأس پایان عمل میکنی و۴۷ بار‌تمدیدش نمیکنی.
🤒</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18255" target="_blank">📅 22:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18254">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش دو انفجار در کنسولگری آمریکا در اربیل
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18254" target="_blank">📅 22:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18253">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گزارش صدای انفجار اهواز
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18253" target="_blank">📅 22:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18252">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18252" target="_blank">📅 22:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18251">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0279bf2042.mp4?token=BCZEHc0BW2DkfTm401G4XxcS5tnys-lkr2xM6QyIm-NnLPZbi8CJGV3v16WrjauqiLey6cQBEnMmxMgz4XfoMuqWiATd08wqckXYXtF8Ta2zrnmbAyuRLEJ8HuNhPZCIagfsa7VuqzyzPOb_9KPo4Gdun2fI1icVdhPPdCL6EWrR49hQBSaE4HxYhgGf7DJqZBvpXoK_WhVM6BF33jmX-uaRh1OfBsWePvgmSGLMhTECbVuDuBolpD2PMN0TF_lTjC4WKV1n3dgxHdo0XhCjwPMhcu0-xsi-6OHQpA1csod2y5HWO6Qjal7SAPo0FjBu3Do3_9QQ5E1zhnp7q_sEtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0279bf2042.mp4?token=BCZEHc0BW2DkfTm401G4XxcS5tnys-lkr2xM6QyIm-NnLPZbi8CJGV3v16WrjauqiLey6cQBEnMmxMgz4XfoMuqWiATd08wqckXYXtF8Ta2zrnmbAyuRLEJ8HuNhPZCIagfsa7VuqzyzPOb_9KPo4Gdun2fI1icVdhPPdCL6EWrR49hQBSaE4HxYhgGf7DJqZBvpXoK_WhVM6BF33jmX-uaRh1OfBsWePvgmSGLMhTECbVuDuBolpD2PMN0TF_lTjC4WKV1n3dgxHdo0XhCjwPMhcu0-xsi-6OHQpA1csod2y5HWO6Qjal7SAPo0FjBu3Do3_9QQ5E1zhnp7q_sEtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ  : همین الان اربیل عراق ، درگیری پدافند آمریکا با حملات ۳پا
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18251" target="_blank">📅 21:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18250">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1SNLvFXz37CKUY5gc6-y1KFMdP03o0miNgS2rA7Az6sUSRWm8FMH5vuqBYfRX-L0NM37UsivJCxZ32XI6FQwFn1AOs7aKdy2kAqgXKmw1p-jRIKYeewgSIrL4E_NyMSrpvM9gANiOlGcNx7Rgbj2VBrATHuxTE02chU2Q67YCY-UUqckZLUjdfAKuWQWADlL8euI-Qv9UBNiHt_qfaBu0IdxPpNb9TCK0MgjeN3czgzPgnPqDGbsXBMVEZuo7ol8AH1jKoIqvgqtp-nL8p5u2WpIVDZ5tVodLix7guc_yEoTmV8ufP6g7BKU6CrbHkt-5BcBviOHWXR_mexrLVWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا اعتراضات و اعتصاب از پاساژ چارسو و علادین شروع شده و حسابی شلوغ شدن @WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18250" target="_blank">📅 21:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18249">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش انفجار بندر عباس
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18249" target="_blank">📅 21:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18248">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سپاه پاسداران ایران در حال حاضر سامانه‌های پدافند هوایی SAM ساخت داخل، S-400 روسی و HQ-9 چینی را در نزدیکی خلیج فارس، مرز عراق و تنگه هرمز مستقر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18248" target="_blank">📅 21:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18247">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ بار دیگر تهدید کرد: هفته آینده بدترین هفته برای ایران خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18247" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18246">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">قالیباف : انتقام عمام را میگیریم
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18246" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18245">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قالیباف:
تفاهم‌نامه زمانی معنا دارد که بندهای آن معتبر و درحال اجرا باشد
، در غیر این‌صورت
اگر قرار باشد جمهوری اسلامی ایران از این متن انتفاع نبرد ما نیز براساس سیاست چشم دربرابر چشم که قبلا گفته ام، دلیلی برای پایبندی به چنین تفاهمی نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18245" target="_blank">📅 21:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18244">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزارت خارجه آمریکا:
از تمام شهروندان خود می‌خواهیم فوراً ایران، عراق، لبنان و یمن را ترک کنند
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18244" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18243">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک مقام ایرانی به المیادین: تهران پیامی خصوصی برای جی دی ونس، معاون رئیس جمهور ایالات متحده، ارسال کرده و در آن جارد کوشنر و استیو ویتکاف، فرستادگان ویژه، را به سوءاستفاده از اطلاعات محرمانه مذاکرات ایالات متحده و ایران برای منافع مالی و افشای اطلاعات حساس متهم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18243" target="_blank">📅 20:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18242">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرگزاری آکسیوس گزارش داد: به گفته یک مسئول کاخ سفید، سفر نتانیاهو به دیدار رئیس‌جمهور ترامپ در هفته آینده در برنامه کاری او قرار ندارد و باید منتظر باشیم و ببینیم چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18242" target="_blank">📅 20:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18241">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18241" target="_blank">📅 20:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18240">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEXN_qFiPlmiKdS3bSUgvgQJmOOthtKpEvWTL3niSDU9EmsPasm5w7XttTIgHp9qtok6Gb-CMx_shWAXGTOySUXfKXtPQEA55bwwSa_vppOoFSNnHfnlQSe6tZMGFwzqSu0_2ll1ULIB_xMGshe0Se23ECPtQAl2e8xKbwKF4mMlC3WBPyaigIYnrmvprS8IkPgSco1NjQzk9qnBzJUEiz58QuCBy4b7WDwnFDHL5_RuVtVllOxG0NzpRdmrJqDWSmoO8ukiYFcZkHQE1wYEAboNAxOqZqcvEfUvz5TgX1-teFs9v7K_2fvfRwedvSasLTQIhqk4cmepVKDEdcrtgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ۷ تن از سربازان ارتش ایران که در جریان حمله نظامی آمریکا به منطقه بمپور در جنوب شرقی ایران شهید شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18240" target="_blank">📅 20:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18239">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حمله ۳پا به کویت : انفجارهایی اردوگاه پیونگ متعلق به ارتش آمریکا در کویت را لرزاند. @WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18239" target="_blank">📅 19:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18238">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حمله ۳پا به کویت : انفجارهایی اردوگاه پیونگ متعلق به ارتش آمریکا در کویت را لرزاند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18238" target="_blank">📅 19:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18237">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRZhkGYWisppIFRJrgUlM7cCIATrNGA8t1Nd-grHjQFEwueTVnsLgu56oYq81RNtWhrJmjqyT6MGus_AEBbjdwjWY18K5wmPhn5XDs_2Yxl_bXxWOxDRXVhOhur3Ri-KYQ5ly4_4jbZnpOJOA_ZQ5ZX-4ANXKBYE7N6Iw_eDV2D-oyRfHgHoA28jAeUDv3UmYG4ID166AopVG89H34Flj8gXWj80OhxI48oyQdSGEla-b_QIkRnCFwHMhTulum5lizU-inZmMUqp6kDHk8qdspKmhzDW9ozhwiHDh2wD_M3tU_5BrgII4lHAEoRcPh1Ike5x85q8ajzlJQ7FswgIPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یابی سنتکام :
ادعا:
رسانه‌های حکومتی ایران مدعی شده‌اند که نیروهای ایالات متحده در ۱۴ ژوئیه یک سیلوی ذخیره گندم غیرنظامی در هویزه را هدف قرار داده‌اند. این ادعا
نادرست
است.
واقعیت:
در ۱۴ ژوئیه، نیروهای ایالات متحده مواضع نظامی ایران را در
بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک
هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را کاهش دهند. در مقابل، ایران غیرنظامیانی را که در حال عبور از تنگه هرمز و همچنین در کشورهای همسایه حوزه خلیج فارس بودند، هدف قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18237" target="_blank">📅 19:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18236">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اسرائیل با بمباران هوایی، جنوب لبنان را مورد حمله قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18236" target="_blank">📅 19:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18235">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزارت بهداشت ایران: از آغاز حملات آمریکا به جنوب کشور، ۳۵ نفر کشته و ۳۰۰ نفر مجروح شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18235" target="_blank">📅 19:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18234">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ به فاکس نیوز: خوب خواهد بود اگر اسرائیل در لبنان حضور نظامی خود را کاهش دهد تا بر مسئله مهم‌تر یعنی ایران تمرکز کند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18234" target="_blank">📅 19:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18233">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارش از اختلال شدید اینترنت
🚨
😔
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18233" target="_blank">📅 19:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18232">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اوفک، چهار فرد و سه نهاد را به فهرست افراد و نهادهای تحریم‌شده اضافه کرده است. بهروز نمازی، شهروند ایرانی، به دلیل ارتباط با سپاه پاسداران , دونیا اتایب، شهروند ایتالیا، ماریا سلینا و وادیم دروژبین، دو شهروند روسیه، نیز به این فهرست افزوده شدند.
از جمله نهادهای تحریم‌شده، شرکت ایرانی نیکا جت، شرکت روسی آوراتک و شرکت ونگارد تاکتیکال ساپلای مستقر در نیجریه هستند. وزارت خزانه‌داری آمریکا اعلام کرد این نهادها با بهروز نمازی ارتباط دارند و مشمول تحریم‌های ثانویه شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18232" target="_blank">📅 19:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18231">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجار جزیره هنگام
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18231" target="_blank">📅 18:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18230">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش از اختلال شدید اینترنت
🚨
😔
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18230" target="_blank">📅 18:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18229">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دور مذاکرات بین اسرائیل و لبنان در رم، ایتالیا، به پایان رسید. مقام اسرائیلی گفت که مذاکرات خوب بود و قبل از شروع مراحل اولیه مناطق آزمایشی، به مقدمات و توافقات بیشتری نیاز است. او ادعا می‌کند که این امر در روزهای آینده محقق خواهد شد. در همین حال، یک منبع…</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18229" target="_blank">📅 18:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18228">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">امیرحسین ثابتی
: نقشه قطعی دشمن ترور رهبر جدید ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18228" target="_blank">📅 18:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18227">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59153729d1.mp4?token=EOHGYl2DRPwTQfluKuyntKoAW3u_4k4Gs0LKPU1IEC2Y2UeKN7CbKv5YOOWT8o6kaCdRIImcNglXmNGd9aXBhcwrTkk6xLiyfalKpWHjmS7Ex82sD5W0zHgI428QynfHZBt6u_uDoYPI_PMuowlH2hkgj7Ozy0XhKHPtIRdIiqTVT0KBVep5s85MdcLI_qKl8zMseZ6hYqRW2DUYkl42kmW0DXJ30cUO25aMZP66c0pXD8vWDAIPpa9lee8ej6pR8ckS2JjF8QdfJMexhng-8Ai6peXZVcmiQhE0Im_qMH4PXQYn4Z8mwCiesrsa6kok98qK1y_IliH6bVr_oaYI0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59153729d1.mp4?token=EOHGYl2DRPwTQfluKuyntKoAW3u_4k4Gs0LKPU1IEC2Y2UeKN7CbKv5YOOWT8o6kaCdRIImcNglXmNGd9aXBhcwrTkk6xLiyfalKpWHjmS7Ex82sD5W0zHgI428QynfHZBt6u_uDoYPI_PMuowlH2hkgj7Ozy0XhKHPtIRdIiqTVT0KBVep5s85MdcLI_qKl8zMseZ6hYqRW2DUYkl42kmW0DXJ30cUO25aMZP66c0pXD8vWDAIPpa9lee8ej6pR8ckS2JjF8QdfJMexhng-8Ai6peXZVcmiQhE0Im_qMH4PXQYn4Z8mwCiesrsa6kok98qK1y_IliH6bVr_oaYI0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: جولانی وارد عمل خواهد شد و کار حزب‌الله را یکسره خواهد کرد
او این کار را به شیوه متفاوتی انجام خواهد داد. فکر می‌کنم جولانی دقیق‌تر از اسرائیل عمل خواهد کرد. او ساختمان‌ها را تخریب نخواهد کرد.
جولانی خودش مایل به انجام این کار است و من دارم به چراغ‌ سبز نشان‌دادن به او فکر می‌کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18227" target="_blank">📅 18:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18226">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تا ساعتی دیگر ممباقر قالیباف درباره جنگ و تحولات کشور یک بیانیه مهم می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18226" target="_blank">📅 18:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18225">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجار جزیره هنگام
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18225" target="_blank">📅 18:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18224">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ: ممکن است تصاویر مدرسه میناب با هوش مصنوعی تولید شده باشد!   فکر نمی‌کنم هیچ‌کس هیچ‌وقت بتواند بفهمد آنجا چه اتفاقی افتاده. همچنین ممکن است آن تصاویری که در اختیار دارید، با هوش مصنوعی ساخته شده باشند. به نظرم هیچ گزارش قطعی‌ای درباره این موضوع نمی‌…</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18224" target="_blank">📅 18:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18223">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f54be6fd8.mp4?token=mTaR9xkWAHMkS2FIN3ScxElojKsXQDetFTFHtO10G48zeTTrHJtPGXSO6NiJ6BsKyL2JkF7USZDCDTOgzKelWKudJThS3JME4SmVN3w0sLN2quOiYpYICrUPnRvTIVv2zu6zJcWMzlr1oGA_h_Jy7vTVU_IWRmKiXT0VddzsdWwtVCQS7JA6NyAzGFPboveA1SCJJX2sGEmZWKRItk88lK9z34Z7JJrNUST6MawhIjlcG64ENnfLpK6nBwxCBvsSzv27wiTuAvUcr_bwbwtUyOQ9-t_oELVwbSA6lc8VqIqDPBrGlPw0RUU04vWqDpjVQFCBcMaOy3CIvSoVGV0uRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f54be6fd8.mp4?token=mTaR9xkWAHMkS2FIN3ScxElojKsXQDetFTFHtO10G48zeTTrHJtPGXSO6NiJ6BsKyL2JkF7USZDCDTOgzKelWKudJThS3JME4SmVN3w0sLN2quOiYpYICrUPnRvTIVv2zu6zJcWMzlr1oGA_h_Jy7vTVU_IWRmKiXT0VddzsdWwtVCQS7JA6NyAzGFPboveA1SCJJX2sGEmZWKRItk88lK9z34Z7JJrNUST6MawhIjlcG64ENnfLpK6nBwxCBvsSzv27wiTuAvUcr_bwbwtUyOQ9-t_oELVwbSA6lc8VqIqDPBrGlPw0RUU04vWqDpjVQFCBcMaOy3CIvSoVGV0uRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوه قضاییه با استناد به این ویدیو : محمدامین دهاقانی رو  به جرم آتیش زدن فرمانداری و تخریب اموال عمومی و فیلمبرداری برای رسانه های موساد؛ صبح امروز اعدام کرد
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18223" target="_blank">📅 18:03 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
