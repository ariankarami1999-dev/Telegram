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
<img src="https://cdn4.telesco.pe/file/Z1hi6J8Mh1p63Eyf9ew1_93MWqiveYcepByzzFMEGrXP_Ga3t9hCDa1fH8yEL8K_6UsPe3XynTU-xFgBvfO9hr2pDH0OJ1GS7C9MFEa38Eu5ln4HrYPoWtPXbu08QPeeVFE6UpG4Lh7maiNAxWDEMz72QZ0-ziuixMkFqLyHFCFnxRhdBJhBX9D4jLi_VypMfIXAZmPBy100o4lpnXTxaLvSzeGM1sQZtwQTIBp4sSmxvZQOz2NeRqTO4nlHSpHa2CD39UHtzqp2Yv4T6OLbbPqzvBepDiK-PrLXpKj6gNxjcPnzFR0B231NXOpUM8buDVQXtcJHHxJ0EFFd2_Wj7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39.3K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 17:36:46</div>
<hr>

<div class="tg-post" id="msg-9126">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hvgy-YahsIcXo9W2K1MK-9_97GuP3XfnYEZxnD-gdCNLg8ndriFhLrQ8-0CwR_6MUIZNhOplVpWhP1uNwlVjZnCTL9vGKMTKsoFXGSOcZRn2VFJk6ZXhsTUrWH63lvy9w4ssasgx3tF7nYC9HZ4E7SuVSb8R43F29U3c5mdJfnwRVu7tnL23xWg-4xEoQmBhbmE7em3OlkpvO2mcwcuXEjcSBTCtS3zjCwA7ycT4tQSZ-gIAgOdssWzZgf25g8so7oQV4JJmafHRdyhd4pBvCN9gCwBwDgxX8QfkBs6t25yzeo-2BNDzdVqJwnPulqOKThUMYquI68o-anFdOIlqoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDFbAPXjXddbbKhlyzNtTt1IDg1kHoQ0Nr05YmNn45yUcMqanyKczyacbIVCt7Cit0McOucbCwB0mFj_ou-PAbmZkYOnEQphce_67Wt-mYlBcRFxpHdP30NXzFFL5WvFauJlnigl7J9Z0INIyNqT9EaL2M5GUqprP00Y9iYl1smdzrZPekBdTZ7wGr7uD0kRXlCTXGal1QU7bJBPJWKtBp2FVaYeBvu7qbkLqS_XRZMhTZGMVCG8_IoWhjscREzweFDsdg7KUXTY2dCzsHCwjqt3xBa4no6MGfHxpSGhL6jTyeveIOY1FkZiTuFtmFZFoGRHEregZVUUey62rPWAhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چین یه توالت رباتیک ساخته که با یه دکمه میاد کنار تختت، کارت که تموم شد می‌شورتت و خشکت می‌کنه، بعدشم میره خودش رو تخلیه و تمیز می‌کنه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 214 · <a href="https://t.me/IranProxyV2/9126" target="_blank">📅 17:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9125">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شما دو ماه بطور جدی روزی نیم ساعت تا ۴۵ دقیقه زبان تمرین کن، هر زبانی. اگه اعتماد به نفست عجیب نرفت بالا حتی اگه لولت اونقد تغییر نکنه،که میکنه . روتین برای یادگیری زبان معجزه میکنه
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/IranProxyV2/9125" target="_blank">📅 13:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9124">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">از آدمایی که دلخوری و ناراحتیشونو واضح بهم میگن و انتظار ندارن که بهم الهام بشه خوشم میاد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/IranProxyV2/9124" target="_blank">📅 13:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9122">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OG08mr5AaHacULPjmnAc1O5IsA1CTtxKtPd1wsoJ4dfI_POAyDwsmf_WdxdDrgxvSUkt-GXbrbuPTwb8VHgjq0DKKliuxrimGqLMSiV-jQgVlRUrHeGa_mLLm0-Y49nt5M1DE7190DvfIkLLrGB_YzSrnxa5T74BaO7by0ChA1E0VE2lrrwycym9ewqZoTq2npsBbLCjlwmQJmjg6VBPvHvnSgiUe8Ln6mY_fv9Ql4ez7iqSDTvEKSP9Utkvg87dqGhO4rC4x7v9Qzc4y7_-Tt7MXPzuv_IKviSgzhzKjyr6Y_KoTB915ksfhYpcC7eNOQJxph9SROUzjKYUYCjujg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrPm1bVZ4FEiRmIcKBlFTJvJ3lshQej5pT1-ALqdOzAm_QYBmTm89I7Qk50c2F6aqSsvRHYoOORyyWklvXTl65uM1gWe0PZ0lSd6EW-rXXRNxDg22yJfsSySz07_GGX1Y3AtWlnJnjjoWZpJ8oSkYN-69mmLxqlvK6cn4Kcbpl8MYl_0JBVHRBGYdM3dwmkvmmD-Sd6oEQVJGtV00yVnkKEb4sXFtug0WUo8lf_PYugNHdPmFYA2ku5l4atnVNed-fkJ_NSrHRclsq086bkEqQVw2c4q5lFSe1VE3JpmNGpqrouDLNi7m77fxUAzzVJEy35-EHk8-c-eppE3AtN8Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیوت بودن اگه عکس بود
🥹
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/IranProxyV2/9122" target="_blank">📅 12:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9121">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">راز رابطه ی موفق یک‌کلمه است :
احترام.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/IranProxyV2/9121" target="_blank">📅 12:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9119">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یکی از خوبی‌های پول نداشتن اینه که همه دارن از مشکلات بانکی که پیش اومده میگن، و تو اصلا خبر نداری
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/IranProxyV2/9119" target="_blank">📅 10:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9118">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">از آدم‌هایی که در رو نمیبندن متنفرم، در اتاق، کابینت، کمد، دستشویی، مخصوصا دهن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/9118" target="_blank">📅 23:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9117">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">100 گیگ کانفیگ رایگان
✅
https://188.121.124.130:8000/sub/djMsNDAsMTc4MTYzNTMzNw2e14b71496
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/9117" target="_blank">📅 22:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9116">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏امروز روز جهانی برآورده شدن آرزوهاست و هیچ ربطی به ما ایرانی‌ها نداره.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/9116" target="_blank">📅 22:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9115">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">میشه به همه احترام گذاشت به جز رفیقم، اگ به اون احترام بزارم فکر میکنه باهاش غریبه شدم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/9115" target="_blank">📅 22:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9114">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏دوستان رک بخوام بهتون بگم برای هیچکس مهم نیست که شما تو نوت اینستاگرام چه آهنگی رو دارید گوش میدید.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/9114" target="_blank">📅 21:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9113">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBHwFKpKkoXpddFaWA-HbG6axGTEqIEVtUGTXbtC6EPb_twYzlhoxv5v5z4PaboR2Urji4f3xDfbIqZfEWAxGqfMuFNUqwHrlY9uD0YJI62PvBAoxDyXy3QdImpyw7RFxtKpbwHgLvE0YLSAadry_FdUCkLuIMUUBa7CiBBEPla-vNzZgUFMsYcYFvW9co2GjhVrX6OGiLyH8NzmrJSU91GMExXl_eAxmhynXvoVOKe142hAkM19L20XjOzIZ8fvTf089PikX-e_NnovdFWCUMsToATC-DAO5uHP26vFtNCUCRFx6hXLcaohjcxBybyW6KBfhTdOXm6eON1B0zZbdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">﻿زوج پزشک ایرانی ۳۱۳ عمل جراحی رایگان را به عنوان مهریه ازدواج خود ثبت کردند.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/9113" target="_blank">📅 20:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9112">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtFGnThCni_eNBUBK4ryMVNoBYdikdyBKOK5Vrx5ZeuLJ-2reCu4UpEjEZlq9lNilB1k1sbLcJSu5vOhmv_5Or3NoueKc3ZvetStOhGNRcYcklLyxtbKYxbwB9eUWhqlz1jM6uL7eYvRd25Ev4B_ToHTaRBoMs6CL4TNSakbUXyIFMbV3QnwxvZBHUPB8w82MNaBgRWRMgmblTwGTaGkzk1_JrZ-pPWOPWNOKCBkx4EuNnBt1hoEZYkxENZsb4Sm9HVsaT2idQMY_HKSxAhMIcRHrMHbMXGG4AlX_W6oQ3TybJPGxIv3y7CIKBYWIKtcFRi776B69hnQOqzpFrslcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/IranProxyV2/9112" target="_blank">📅 18:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9111">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مسئولیت‌های زندگی دارن مزاحم افسردگیم می‌شن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/9111" target="_blank">📅 15:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9110">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آخه آمریکای لامصب؛ تو که ساعتت انقدر با بقیه دنیا فرق می‌کنه، برای چی میزبان جام جهانی میشی؟
آخه کی 5 صبح فوتبال می‌بینه
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/IranProxyV2/9110" target="_blank">📅 13:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9109">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سلام بر کسانی که،
وجودشان از غم این دنیا می‌کاهد...
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/IranProxyV2/9109" target="_blank">📅 11:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9108">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFp09UP8KaL_oxleJMB1lGcP8rh8gDEwZ6-1yyPTHvv3ByO_dyRDxtaps1rd1NKyi0Stc9-4SKdbXVBzjJfGRq_69vNnA-9OWxgvVFcWpw_uB9dfAHfX8LF4wiTyY_YjDhZ7cnxLIX9NUbJrrIUNQZS9iP_58XbjCtny8_B4CLXXam1gBU0XVQhEAEKfMPQ8axKfVHSwfW3iL_A8ldm6baeChWd5BHOec_XiHc1wgNWFpebysiojUGxl0R-gUgjghQqdN7affslQ1GWl8ZvFE5909_l4u_vE6C2a0VznFstGYFBA1POiepoC48Dp4d4hvX_d_OKJjRsLJYsRZa7BBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی ساعت اینو ازش بگیره :))
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/IranProxyV2/9108" target="_blank">📅 03:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9107">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوست باید جوری باشه که هم بشه باهاش بی حد و مرز چرند و پرت گفت، هم حرفای عمیق درست درمون زد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/IranProxyV2/9107" target="_blank">📅 03:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9106">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/242ac19f99.mp4?token=JEwy28qZe4RATnffZfUvrx29-87ioVdyjLMFi77ME8Q4lWn-lXZZo4OEnrOir-ZqA0SawqFdR0hmwRN84Vrqx_2tiDsV_-05kRHwaG4N6-C7lgbaSa4bzRIn6IZ1rw-9f0lrl71cr8gMt25tmBJ4U9ab8UOdSKD87tyCeNBf0f8zBV0hl0wV_h2R5eo9xZattvxw_TwCMMZK3Px0vQiBmV2rMXVr0ZQY1kef0EgC0bW9sKVHBUKeKySf_zrbFObVftKIGRWHtaUOU1peTz6PPq5yXfKTLsotetnGPhSKjNbGZqgqoRMELhihEHTldX6kWgeSlkVBZ02j_qoV3Jcm5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/242ac19f99.mp4?token=JEwy28qZe4RATnffZfUvrx29-87ioVdyjLMFi77ME8Q4lWn-lXZZo4OEnrOir-ZqA0SawqFdR0hmwRN84Vrqx_2tiDsV_-05kRHwaG4N6-C7lgbaSa4bzRIn6IZ1rw-9f0lrl71cr8gMt25tmBJ4U9ab8UOdSKD87tyCeNBf0f8zBV0hl0wV_h2R5eo9xZattvxw_TwCMMZK3Px0vQiBmV2rMXVr0ZQY1kef0EgC0bW9sKVHBUKeKySf_zrbFObVftKIGRWHtaUOU1peTz6PPq5yXfKTLsotetnGPhSKjNbGZqgqoRMELhihEHTldX6kWgeSlkVBZ02j_qoV3Jcm5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر خوشگله core
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/IranProxyV2/9106" target="_blank">📅 03:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9105">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1f1utRfkJ8ZvkvzzV3jeJSZmRzxU56aTLBqhJZbeZWfrNHnVX0pcJpDJH_xCKjoGDiw2ZttJ5V7BmRFofO1ys4nYjFlrYePOTTRlmorkqKpxNEliPTZC--5Dh8UtrsxQQTMQjac3-1PVem-jNuRZoAzCWn74msq78PLJOwr3h7gcRwvKmyAMstWCpa_uKjQb5UajMR5qMfMkVIPV-TOR8p9sXPnOkT308sAVZl-pZTmIxJMezMYJzuWTeE01OHPfdQEsrre7q0vCDlg--bkeFDloyvg-2cqP4XQBLTZ3vaARwxwISiWlQkavh7uwurFXco3HdOFMlRiJiHWhTbT-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و...
فقط گیگی 8 هزار
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=80T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/IranProxyV2/9105" target="_blank">📅 14:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9103">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تیتانیوم 94.npvt</div>
  <div class="tg-doc-extra">52.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9103" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🔝
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/9103" target="_blank">📅 14:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9102">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=87.248.129.183&port=443&secret=ee74531eb0ee43745c6ddb8efe247626cb3132333333332e732e732e732e652e6565666566656665662e69722d2d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/IranProxyV2/9102" target="_blank">📅 14:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9101">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">50Gb Cfox_Server A76.npvt</div>
  <div class="tg-doc-extra">7.2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9101" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/IranProxyV2/9101" target="_blank">📅 14:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9100">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=194.120.230.97&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/IranProxyV2/9100" target="_blank">📅 14:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9099">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSUKEx5nDCdRpmeWE8TKl2NHvbTw4fYN3vnA_h6ee9SpX3xhaDXj3CNKlSs1chRfEDPlyYtwRO-bNBepn0Mm25AihTkCx4qLI1CoAlwKiCdGJWuOOaB5ugjvA_eCb005N84alVRAVA1SJHhJollUNRUJBYLEpbN_k3GuLaP5SOvQUr4QKyF2qx2pP0dXu49CvJUR-lCEgwd61EubbFCAIbNVsIxXoVTL8woSctvRFSkAQu-64ON3ECf29dyVlzxFiJ5XYGw7eqmTi_1iHekVGrdFLBwE3XbGR2JrLN5UdEisQYNSnTsfcnanOlvQzuUmPtwqbCFHWQv7Gq0WSdNIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و...
فقط گیگی 6 هزار
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=80T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/IranProxyV2/9099" target="_blank">📅 14:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9098">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=play.proxyvpn.site&port=443&secret=ee4d0c82ca73f261e6933ec36e5d902ff6706c61792e70726f787976706e2e73697465
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/IranProxyV2/9098" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9097">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">فوق پر سرعت🔥.npvt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9097" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
💯
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/IranProxyV2/9097" target="_blank">📅 13:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9096">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">TIMSAR 263.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9096" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/IranProxyV2/9096" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9095">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-poll">
<h4>📊 بت زن داریم؟</h4>
<ul>
<li>✓ اره</li>
<li>✓ نه</li>
</ul>
</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/IranProxyV2/9095" target="_blank">📅 10:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9094">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🐝.npvt</div>
  <div class="tg-doc-extra">4.2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9094" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/IranProxyV2/9094" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9093">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🇨🇦.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9093" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/IranProxyV2/9093" target="_blank">📅 18:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9092">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">◀️
دوستان این تخفیف فقط تا آخر امشبه</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/IranProxyV2/9092" target="_blank">📅 21:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9090">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❤️‍🔥
Config:
🔗
Link:
vless://d3d046fa-d372-430a-8ed9-083d62c44efb@45.130.125.194:8443?mode=auto&path=%2F%3Fed%3D2053&security=tls&alpn=h3%2Ch2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A1000000%2C%22scMaxConcurrentPosts%22%3A100%2C%22scMinPostsIntervalMs%22%3A30%2C%22xPaddingBytes%22%3A%22100-1000%22%2C%22noGRPCHeader%22%3Afalse%7D&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=ssd.mojaz-persian-music.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/IranProxyV2/9090" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9089">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=51.250.65.108&port=443&secret=ee3a9f22462890489c0bde045048ff9a17617669746f2e7275
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/IranProxyV2/9089" target="_blank">📅 11:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9088">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">فول متصل⚡️.npvt</div>
  <div class="tg-doc-extra">149.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9088" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
🆓
npv tunnel
🙂
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/IranProxyV2/9088" target="_blank">📅 11:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9087">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=zone.nolags.pw&port=443&secret=dd04d2a884220d45de24af8bade64322ac
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/IranProxyV2/9087" target="_blank">📅 21:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9086">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ʙᴇꜱᴛ🇳🇱🇩🇪⚡🚀.npvt</div>
  <div class="tg-doc-extra">14.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لوکیشن هلند و آلمان
🇳🇱
🇩🇪
Npv tunnel npsternet
💥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/IranProxyV2/9086" target="_blank">📅 20:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9085">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نامحدود🛰️.npvt</div>
  <div class="tg-doc-extra">149.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9085" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
👀
Npv tunnel npsternet
🛡
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/IranProxyV2/9085" target="_blank">📅 20:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9084">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes⛱️.npvt</div>
  <div class="tg-doc-extra">3.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9084" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
💯
Npv tunnel npsternet
🟢
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/IranProxyV2/9084" target="_blank">📅 19:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9083">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CIVAX🍔.npvt</div>
  <div class="tg-doc-extra">1.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9083" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پرسرعت وصله دان بزنید
⚡️
Npv tunnel npsternet
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/IranProxyV2/9083" target="_blank">📅 17:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9082">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🇺🇸سرور آمریکا.npvt</div>
  <div class="tg-doc-extra">4.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9082" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✔️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/IranProxyV2/9082" target="_blank">📅 16:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9081">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🚀🇩🇪.npvt</div>
  <div class="tg-doc-extra">1.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9081" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
💙
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/IranProxyV2/9081" target="_blank">📅 03:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9080">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=87.248.129.219&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/IranProxyV2/9080" target="_blank">📅 03:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9079">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🇳🇱.npvt</div>
  <div class="tg-doc-extra">24.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9079" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
📊
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/IranProxyV2/9079" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9078">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot  جهت ثبت سفارش به…</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/IranProxyV2/9078" target="_blank">📅 03:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9077">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پرسرعت💯.npvt</div>
  <div class="tg-doc-extra">3.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9077" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/IranProxyV2/9077" target="_blank">📅 03:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9076">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
چنل دوممون مربوط ب اخبار رو دنبال کنید
✅
با ما اخبار جنگی بروز باشید
@russiamilitery</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/IranProxyV2/9076" target="_blank">📅 01:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9075">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMOthwokSUFoiNrlrKkJmKN-jBNoWUnvSl2zJUTvH-nG9oaCVzBhnimVgdCYn_BR_dGz5OnUbVmQWyo2G_uvLOVJ4D8dQgJmtTV79IK8ljoQ_5ptyw7MttMLEbl4826bVlGKzdvmcaZPSockKNJv_jVGpDcbGfUOc3UpYh1PIUt5Q_M9305oWK1y3MLO9TAQnNNL3FEAVjPj3It34eSHA2KoGb--RlTNW5_BC-5ZlKE7L6TRwvHrAsMHlAIEr46Ut3gYf5I16IyTjLdXP41gRdnMJ7q26peHzwAKRhbXb-Sq2Kv_TWbQWf2jqQe3f_nOacwKnYOIo3u2sjFQSiqPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت اختلال و قطعی نت بصورت موقت مارو در روبیکا دنبال کنید، هرمتود رایگان متصلی که پیدا کنیم براتون قرار میدیم.
🔴
rubika:
@activityall</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/IranProxyV2/9075" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9074">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=157.90.171.183&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=178.105.50.21&port=8443&secret=dd104462821249bd7ac51913020c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/IranProxyV2/9074" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9073">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=north.nolags.pw&port=443&secret=dd9760e74174fb9717de21cc7e17027e34
https://t.me/proxy?server=87.248.129.226&port=443&secret=FgMBAgABAAH8AwOG4kw63QFgMBAgABAAH8AwOG4kw63Q
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/IranProxyV2/9073" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9072">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
احتمال اختلال و قطعی اینترنت بالاست
کار ضروری دارید انجام بدید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/IranProxyV2/9072" target="_blank">📅 00:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9071">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری/ترامپ : به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
😬
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/IranProxyV2/9071" target="_blank">📅 23:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9070">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=46.224.226.79&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=91.98.229.218&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/IranProxyV2/9070" target="_blank">📅 21:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9069">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
ترامپ: شاید نیروگاه‌ها و پل‌هارو بزنم شایدم نزنم، محرمانه‌ست
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/IranProxyV2/9069" target="_blank">📅 19:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9068">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
💣
🇺🇸
فوری ترامپ: ما به آنها حمله خواهیم کرد و بسیار شدید حمله خواهیم کرد. ما بمباران رو از سر خواهیم گرفت. ما حق انجام این کار رو داریم. آنها هلیکوپتر ما رو ساقط کردن.
🚨
ترامپ: ما امروز دوباره به آنها حمله میکنیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/IranProxyV2/9068" target="_blank">📅 19:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9067">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6gTQHAB5_8UyxhVefOz7-rqGQ1x2h_sdp9HWcbP4RQNXMIqEUim37PifGAS_TBKWuaC6qOig3zWlGpBoOOdE6_6rEJAU3I1Vg6bcEK8kOF58dWWtsWYW7e2m_QuSt2l5_kCd_0El9UC6kFa2Vwu-9xLDjNYEEtV13l7KmAxFC2_fP4btXLAp8BqKfEu4td0359aXNW0ulhykwdCcg7Ft4hIvf4N2wSWepj9GaCvS5GJMirUxA8Sq0SrDaIub_rK2vgofP3UlexFp-1-wcnjbIltmeM-tMZVJyK5v0v97sqAIy8wdKsiJRh181lVsnOkwLq95J3ToQpAjlIHiMS1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/IranProxyV2/9067" target="_blank">📅 18:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9066">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تازه نفس♥️🤌🏻.npvt</div>
  <div class="tg-doc-extra">1.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9066" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
🎁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/IranProxyV2/9066" target="_blank">📅 18:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9065">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سرعت قوی🚀🔥.npvt</div>
  <div class="tg-doc-extra">2.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9065" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/IranProxyV2/9065" target="_blank">📅 17:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9064">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دکترنیک ظهرونه.npvt</div>
  <div class="tg-doc-extra">17.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9064" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/IranProxyV2/9064" target="_blank">📅 17:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9063">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🐕‍🦺.npvt</div>
  <div class="tg-doc-extra">6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9063" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/IranProxyV2/9063" target="_blank">📅 17:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9062">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری
-
ترامپ به فاکس نیوز :
به صدور دستور برای حمله‌های جدید به نیروگاه‌ها و پل‌های ایران نزدیک شده‌ام!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/IranProxyV2/9062" target="_blank">📅 15:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9061">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKoS99VY4bjHxK4lmvyYiy_v3kpXinz4K58NbAZPlvQWUCAyNvXvxgtVRp1qds0Tmz2jsJ5TBfBNi7hcZ9X4VlsFKtwrh0Roh3WmjL7k8F7n_dKhNbO1hsrq7JEJVV_How568CJiKKeRdNMlqkDgW_u9wY7zdwz_lGEFXL5JDjXBwHuo_zn4LCL8c7zxBANHEdqddGm15ZK8yAKWbfSpynbvcO5lige2Qbf5i5nMKOiXFs6aGpMjqjLgq1rZ2ejDGQw_ElY4IwQp6SEerIiZP9hPkSxG62bm-vNKqgy6Ug8oMsjjd64G5r0m8QwnlgIKBgzkUfojnen8m6BS2h9KQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری-
ترامپ:
«ایران فقط حرف می‌زند و هیچ عملی انجام نمی‌دهد. قلدر خاورمیانه مُرد!!! آنها خیلی طول کشیدند تا برای توافقی که برایشان عالی بود مذاکره کنند، حالا باید هزینه‌اش را بپردازند!!!»
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/IranProxyV2/9061" target="_blank">📅 15:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9060">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اکثر نتا وصله
🍸
✅
vless://9dbaa630-c895-4883-aa8a-20e8a48ff4b2@fff.oakcup.ir:2052?encryption=none&type=httpupgrade&path=%2Fapi&host=Ip.oakcup.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://5960576d-829e-4d09-8232-0e80121a6fe4@45.130.125.193:8443?encryption=none&type=xhttp&security=tls&path=%2F%3Fed&mode=auto&sni=ssj.new-persian-song.ir&alpn=h2&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://0c09799a-47ca-494e-a50e-828632ef9d81@199.232.78.159:443?encryption=none&type=ws&security=tls&path=%2F&host=bazaryabab.global.ssl.fastly.net&sni=default.ssl.fastly.net&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://5960576d-829e-4d09-8232-0e80121a6fe4@45.130.125.162:8443?encryption=none&type=xhttp&security=tls&path=%2F%3Fed&host=vi.mojaz-persian-music.ir&mode=auto&sni=vi.mojaz-persian-music.ir&alpn=h2&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://07dce2d7-9849-4e22-adb9-36d2763c3b89@snapp.ir:2095?encryption=none&type=ws&path=%2F&host=api.aramonlineshop.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://fc965ad9-bdd7-4815-ad71-b39ec5972dc1@141.193.213.11:443?encryption=none&type=ws&security=tls&path=%2Ftsghdws&host=octopusss4.com&sni=octopusss4.com&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://cabbfe13-038b-4dbb-9c45-5079c829abfa@167.82.0.1:80?encryption=none&type=ws&path=%2F&host=max-gb1.global.ssl.fastly.net#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://8dc7722c-2767-4eea-a28b-2f8daacc07e3@sca11.myfymain.com:8880?encryption=none&type=grpc&mode=gun#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://fc965ad9-bdd7-4815-ad71-b39ec5972dc1@89.116.46.68:443?encryption=none&type=ws&security=tls&path=%2Ftsghdws&host=octopusss4.com&sni=octopusss4.com&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://44b3ee72-cffb-4d66-ab7c-3138b9bdeeef@54.36.162.217:443?encryption=none&type=tcp&security=reality&headerType=none&sni=speedtest.net&fp=chrome&allowInsecure=1&pbk=upTVUrc_t7xF1ULni8pHRDhRES1sT4BDm1r8rugTzyQ&sid=ff815f58c7e77aa9&flow=xtls-rprx-vision#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://e4e7866d-920b-4a53-a8e2-6ae9b2a42fc2@47.77.214.201:10035?encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://ae852d97-85f5-45cf-82a4-254eba345480@144.31.131.33:443?encryption=none&type=tcp&security=reality&headerType=none&sni=cdn.cdnjst.org&fp=chrome&allowInsecure=1&pbk=djH9iD2QV748ocK-wPH7HvDd03lu88zHhS4G-61w6Dc&sid=a120&flow=xtls-rprx-vision#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://d3d59da0-31a4-45da-bf9e-373c6ab140db@62.60.251.131:45656?encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://e0de62c9-f317-4275-b7e5-8da7b7fa9bc6@77.110.127.191:9443?encryption=none&type=ws&path=%2Fpourya#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTprMWRCT21PQjRvcWk3VW1wMzdhMWJR@82.38.31.192:8080#
%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/IranProxyV2/9060" target="_blank">📅 12:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9059">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=45.32.233.182&port=8443&secret=dd1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=mercedes.nine-gear.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/IranProxyV2/9059" target="_blank">📅 03:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9058">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
♨️
مهر:
شنیده شدن مجدد صدای انفجار در جاسک
✅
موج دوم حمله درحال انجامه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/IranProxyV2/9058" target="_blank">📅 02:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9057">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
لیست جدید پروکسی متصل پخش کنید مخصوص نت ملی و شرایط عادی
🇮🇷
https://t.me/proxy?server=87.248.129.106&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=87.248.129.235&port=4455&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d#proxydotnet
https://t.me/proxy?server=protocol.fast-mt.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=proxy.speedbreaker.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=free.feel-fly.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=www.alo-otp.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d
https://t.me/proxy?server=87.248.129.107&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=172.65.104.042&port=25565&secret=7hYDAQIAAQAB_AMDhuJMOt1iaXNjb3R0aS55ZWt0YW5ldC5jb20
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/IranProxyV2/9057" target="_blank">📅 02:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9056">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
پروکسی
✅
tg://proxy?server=5.78.53.137&port=8443&secret=dd104462821249bd7ac519130220c25d09
tg://proxy?server=5.78.57.102&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/IranProxyV2/9056" target="_blank">📅 01:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9055">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=rec.nolags.pw&port=443&secret=dd0603553657b3f54b6bff0d3759e8db1d
https://t.me/proxy?server=5.78.59.193&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=office.proxytg.live&port=443&secret=eed604acbe90be65ddf34629f1e2234f7d6f66666963652e70726f787974672e6c697665
https://t.me/proxy?server=feed.proxytg.live&port=443&secret=ee7c1dc73472aff6b273c603d9713900d1666565642e70726f787974672e6c697665
https://t.me/proxy?server=87.248.129.222&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/IranProxyV2/9055" target="_blank">📅 01:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9053">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پروکسی نت ملی میفرستم حتما ذخیره کنید داشته باشید
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/IranProxyV2/9053" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9052">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مث اینک این دفعه اوضاع واقعا خرابه، از اونطرف صدا و سیما میگ ما نزدیم، از اونطرف آمریکا میگ شما زدید پس باید ما بزنیم، فک کنم آمریکا میخواد شروع دوباره جنگو این دفعه بنداز گردن ایران
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/IranProxyV2/9052" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9051">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پروکسی فول متصل،ذخیره کنید
✅
tg://proxy?server=5.78.48.55&port=8443&secret=dd104462821249bd7ac519130220c25d09
tg://proxy?server=95.216.42.228&port=4455&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/IranProxyV2/9051" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9050">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
تیتر شبکه خبر :
حملات موشکی سپاه ایران بزودی...
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/IranProxyV2/9050" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9049">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
بیانیه جدید سپاه : حمله شرورانه آمریکا را بی جواب نخواهیم گذاشت
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/IranProxyV2/9049" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9048">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">به لبنان که حمله نشده جمهوری اسلامی بهش بر بخوره؛ خاک ایرانه دیگه، مگه مهمه براشون؟
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/IranProxyV2/9048" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9047">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حالا پاسخ ایران چه خواهد بود؟
🦦
بزن پایگاه هاشو تو منطق بگا بده مشتی
😬
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/IranProxyV2/9047" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9046">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
سنتکام اعلام کرد که حملاتی را در قالب دفاع از خود علیه ایران آغاز کرده است؛ این اقدام در پاسخ به سرنگونی یک بالگرد آپاچی آمریکایی در روز گذشته صورت گرفت. این مأموریت، پاسخی متناسب به تجاوزات غیرموجه ایران است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/IranProxyV2/9046" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9045">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
صدای انفجار در بندرعباس
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/IranProxyV2/9045" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9044">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOYzz1LEnnsOk0M2xp4g_fiZPRLSgZJNSVizQQe1kVmzzu0e3LMW_iNMXk-5WrK6ZliFffgJuSuyHqczESs6p8EL4QCuTjwZpunkBe8zdZxwku4mr1dbpn5hfxtY9Io4GRyjx3QLUx1SIEmKkw02X_INE4N_JPE7NUnDs8TPoYn_euy9LRY4NHJJfmHPxz0rq-L20F2FS1P9msL4h8zgwShID5NfOxlHW0ISv4ziXqlAg9P4hcIIjRPdue32b49dyb34_QIp6LFQm5GCRf0vCYlvmHUaC1ZUdEMJ9OFI7-thWcKqtlc5wcnoJmRucMO-J4UN033uzEg87arM7JFbgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/IranProxyV2/9044" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9043">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/is4n8pjSOpedOvOpUm5HnfBsCj-VuEO8T73pdQegMCF7bMGvSM_3TCiAMBaJ9yzktYS0n62VHXS3oYxCoB-nANXqNzo49Z3URCgixadRf5Wdj9Mdy1S3Vn2fTL2JAu9tv69-WkZ-l9xkifN1o4yeMtv0ix7gVDiYfW0UwVzLEyCNSJAdgnkUtiiBPAHkJsXLn7NMstQd852V_KHrTuSWRiLzu8f5DRE4rhjA_IdOIWkGA-KuvqmKQIhnGKMq6_gqEK1gd0uJ_o3XRo6yMeXHX3aWHcNZKXRaKuQZs4jtKUQouzbs0d-XOL6-rZGZYEMfcE78B5Tom3AGLDaS6zxNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تونل کردن ترافیک ایران به سمت کشورهایی نظیر اذربایجان برای باز کردن سایتهای تحریم شده مثل ChatGPT و Claude بدون نیاز به VPN، باعث شده که ظرف مدت چند ماهه بعد از عملی شدن قرارداد انتقال ترافیک، رتبه کشور اذربایجان در نرخ سرانه تعداد پیامهای ارسال شده به ChatGPT از رتبه 44 در اوایل سال 2025، به رتبه 6 در اوایل سال 2026 صعود کنه!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/IranProxyV2/9043" target="_blank">📅 20:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9042">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=5.161.143.78&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/IranProxyV2/9042" target="_blank">📅 20:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9041">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
بیانیه رسمی فیفا :
دیدار ایران و مصر دیدار افتخار همجنسگرایان رنگین کمونی خواهد بود و به هیچ عنوان این رویداد لغو نخواهد شد. کاپیتان هر دو تیم الزامی هست که بازوبند رنگین کمونی  ببندن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/IranProxyV2/9041" target="_blank">📅 18:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9040">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIDmFridO9IZOXlX9gkry0ZCx9HjDajiDSDHxBzK2wXt1Vnz6vScM2FC7QhHiAadPYO46hKWwaZV0OdOUWbknBDIqFps_8-hw9tACI_ghox7GBWyDBM1Msu8-zBTv86pL9UVs-3M03n_MsbsCAA832iH49u1NJi5NDO6jrFvZfJntCrqGaLijfziSopgpja1DalQt2as42sSVnBXTlG3CMRAK5_2NL5WF05IiimGYY4_xy2GFoiVwmqnkSB1R0RTsWKE2xQicX7LQ5mJUHoNDuFv1_xKmpt08daA3cyiE2VC4dPtCgpjX0eCYU6MvVbh44fS1n-IDKht3b7ipFW9hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و...
فقط گیگی 8
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=80T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/IranProxyV2/9040" target="_blank">📅 17:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9039">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❤️‍🔥
Config:
🔗
Link:
vless://d4eb1900-6515-494e-85c5-306bb9594f56@45.130.125.194:8443?mode=auto&path=%2F%3Fed%3D2053&security=tls&alpn=h3%2Ch2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A1000000%2C%22scMaxConcurrentPosts%22%3A100%2C%22scMinPostsIntervalMs%22%3A30%2C%22xPaddingBytes%22%3A%22100-1000%22%2C%22noGRPCHeader%22%3Afalse%7D&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=vo.new-persian-song.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/IranProxyV2/9039" target="_blank">📅 17:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9038">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❤️‍🔥
Config:
🔗
Link:
vless://10a6b923-e349-4594-92bb-d81a6245aaec@172.67.74.10:443?path=%2Fdownload.php&security=tls&encryption=none&insecure=0&host=sertraline.adaspoloandco.com&fp=chrome&type=ws&allowInsecure=0&sni=sertraline.adaspoloandco.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/IranProxyV2/9038" target="_blank">📅 17:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9037">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=135.125.216.18&port=8080&secret=dd112760f4d4ccf54d5c3bc40a6776c73b
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/IranProxyV2/9037" target="_blank">📅 13:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9036">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سرعتی🔥🚀.npvt</div>
  <div class="tg-doc-extra">2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9036" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
🆕
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/IranProxyV2/9036" target="_blank">📅 13:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9035">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">📱
یوتیوب رفع فیلتر می‌شه.
📔
مصطفی پوردهقان، نماینده مجلس:
وزیر ارتباطات در کمیسیون قول دادن که فضا رو به شرایط عادی برگردونن و بعد از رفع فیلتر واتساپ، رفع فیلتر یوتیوب هم در دستور کار بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/IranProxyV2/9035" target="_blank">📅 13:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9034">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7BX3XTZ5qZXwVO1LiL8bhh2PeqALjKCXR7vHFMbdALE_gYETG3SIukYzQsqI2-CrjH8L0nnpnunNh3qdRNz_x7kfTu5GRUXCpsOIYMMmrlY_p4myjqM38Whbu74TYdbmAAuctbNisV05IPqWIStOBVSMDcsGQGCXGFmeB6EVwRv0DmheJLuT7uN5OPYoCcuLGFNtcIRcqhdTE8BiRKDQNR1YksE9WqjMsrN9eRtQ82uS70IUjN1UAXLfG6oQsIlOWKEIVjggG2UE1NHVpNFXOZyxrPkblzkYfNoVKfRzxFa0r0cgDhK8VKLJ5nlMga1TnH0X_WGMxb2Mt1_-QKtcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot  جهت ثبت سفارش به ربات مراجعه…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/IranProxyV2/9034" target="_blank">📅 22:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9033">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMs_cq2AWW2fBJC6qSu22hQblFcsmVMzn0h64-aUV94xRJLJb1Mo9gurlN5qIyGzMc7-S9joYd7jDvIuEu7Vj5mf35pUEdqhjW1uC63sIbbfYP9yJQwc4RFS1KKXkAgkWZ4foImeZfbHmsazaNH31NUCG3eSQKzqpxnbslZgM5xkD0LP1NwKXRKgqh68bhYO6_ZRY5ehu7lFrq91Ay6xd5CCp98kRL40CVcaCX4ubEwDYTeSsJ47WMyqODXmnuu9dhI9Fkc2ws24Oj5UoKdvQNOOu7Km_CDyfZnKUCm0KGUgfWupn2QBXA-BTS3yUjRnoFO3PFoSbIq_qX7v4gJ2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/IranProxyV2/9033" target="_blank">📅 17:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9032">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=178.105.226.182&port=443&secret=ee396219a1e9b2aebf6f245a1495777811706c61792e676f6f676c652e636f6d
https://t.me/proxy?server=orbit.proxyonline.online&port=443&secret=eea49899bfb9f5b061d6213e6f6480ea006f726269742e70726f78796f6e6c696e652e6f6e6c696e65
https://t.me/proxy?server=94.183.221.165&port=443&secret=a252e3eb41417da5e2332193f25bcf34
https://t.me/proxy?server=relay.proxyb.site&port=443&secret=eeee9dfed6b3721e5b2788f5100af2ff4272656c61792e70726f7879622e73697465
https://t.me/proxy?server=5.75.200.229&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/IranProxyV2/9032" target="_blank">📅 15:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9031">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
مث اینکه جنگ فعلا به پایان رسیده، هردرطرف از موضع خود کوتاه اومدن ولی البته یه نکته بهتون عرض کنم که این شرایط فقط تا پایان جام جهانی فک میکنم آتش بس برقرار باشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/IranProxyV2/9031" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9030">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
👑
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:   نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/IranProxyV2/9030" target="_blank">📅 14:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9029">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
👑
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/IranProxyV2/9029" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9027">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=fresh.nolags.pw&port=443&secret=dd691fa48fcc661b68fe4f5200c5b174f9
https://t.me/proxy?server=91.217.166.212&port=16&secret=dd1603010200010001fc030386e24c3add
https://t.me/proxy?server=fool.feel-fly.info&port=25565&secret=7hYDAQIAAQAB_AMDhuJMOt1iaXNjb3R0aS55ZWt0YW5ldC5jb20
https://t.me/proxy?server=91.217.166.22&port=20&secret=dd1603010200010001fc030386e24c3add
https://t.me/proxy?server=91.217.166.21&port=20&secret=dd1603010200010001fc030386e24c3add
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/IranProxyV2/9027" target="_blank">📅 14:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9026">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/IranProxyV2/9026" target="_blank">📅 13:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9025">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
دوستان احتمال داره دوباره اینترنت بین‌الملل با محدودیت یا قطعی روبه‌رو بشه.
✅
از همین الان برنامه‌هاتون رو آپدیت کنید و این اپ‌ها رو نصب داشته باشید:
• Happ
• NPV Tunnel
• V2RayNG
• Psiphon
• ShiroKhorshid
• Http Injector
• NetMod
⚠️
قبل از هر محدودیتی، آماده باشید
💙
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/IranProxyV2/9025" target="_blank">📅 13:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9024">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg8GHTy9EHfy82-lq5v8LpUi2x2uWDbpKZonp8b5bMRM1IWZ4k_zXz9GwfaJeO_gJ-EGhtT66WHw-s2xyEBA4W9vTZVrRwfjY_X8rpF5QZK39D6AN9WkLfsbhAtrN3HqXUAJlHCmDcwNWhltjq7z6nvZalGK-gRCi9XpPCRxum8swSsiTE4ui8m9fRnqCXTDyYuro4fEQld9FYGB2rmDeOzJbCKEcLPrcJWX5ySJSsNDVThD_E2mWOyv8QCMUKHPWsazb0ZO5TWtDRV0h8Xs9yJfueSwtQ4F-1XFmuvYkkn_BHPYL4U4YA0513zFYhl7jKaElEh6MIYY3JcWFmnXLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دوستانی که سرورا براشون متصله نمیشه، ۵ پورت و ۵ لوکیشن جدید اضافه کردیم، لینک سابتونو بردارین، حتما دامنه جدید رو از قسمتی که نوشته
info.russiaproxyy.shop
به این دامنه جدیدی که براتون قرار دادم
⬅️
doc.midnightfits.com
➡️
تغییر بدید و وارد ساب لینکتون بشید سرور جدید رو بردارین
🔹
نمونه ساب لینک جدید
https://doc.midnightfits.com:2096/reza/xxxxxxxxxxxxx
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/IranProxyV2/9024" target="_blank">📅 13:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9023">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=s3.mowork.twc1.net&port=443&secret=ee90872f20ccc37e3aa2681602f51df71273332e6d6f776f726b2e747763312e6e6574
https://t.me/proxy?server=s4.mowork.twc1.net&port=443&secret=ee3e9cfe9af4494731b9a566075ee8c3bc73342e6d6f776f726b2e747763312e6e6574
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/9023" target="_blank">📅 13:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9022">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
vless://a78bf929-6883-48af-902d-7737793eeb17@hu02.sonicsonic.icu:443?security=reality&encryption=none&pbk=z-TKWOWgZLfzQ-wNdwXQqVwaUgCmbchM2Xtrk1NGynU&headerType=none&fp=qq&spx=%2F&type=tcp&flow=xtls-rprx-vision&sni=hu02.sonicsonic.icu#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/IranProxyV2/9022" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9020">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پروکسی مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=imtproxy.ir.imtproxy-ir.info..&port=443&secret=ee16550001232d00bb5190728b72644171706c61792e676f6f676c652e636f6d
https://t.me/proxy?server=65.108.154.5&port=443&secret=eecdf95381f978fb348f233a14b2251e6d7777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=91.107.148.135&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=5.75.206.125&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=91.107.167.170&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/IranProxyV2/9020" target="_blank">📅 13:01 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
