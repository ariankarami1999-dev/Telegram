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
<img src="https://cdn4.telesco.pe/file/JVpKHfmKCLddTHUOEZv9EfRD045cHyEL2LCyh48ZVLyjcMFdNOAe10_a2i2-9V6VFhX7W0W66NZyNYf162Jt2sVwQdhLVLGELvXNRSVCw-Sin5UFSuS5nXMnwzeGY-e9nCYr8Exhy483XGFo2LRw6zNVp_DtfzvQv9R0FNZ3o6PZYMniKYCu7oHvu6yg_WmNxFpM9R4FA_UCXItJN5fDWn0DqFJfWWy7yjQYtMtiSuadiIhxWXozI5VoEtVbzqNKhqH59791f_RYwhiYU6Pbh89BQXhrRQi0P3JPc7XbbSCWG9uVbN2T_-n0CYXsmpVXpgxkMeDVppsEpY6dNShCDA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 14:29:34</div>
<hr>

<div class="tg-post" id="msg-82011">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=plGrs7KCWMt7--eNpT73VUTmCUNffvzipxum6l0v6Rza7qWVl8WKOMo6b8v2xBETEFYBdeamKo_wPGHuxmZP1CYYKOKad3TbLxb4640NI_hB2IRWXcumXag_P9yKnC1G-QcPaAESBvydj8XLtpyY2LMgkKYkxElOT9qN4wzAJvbo2nfpIQoiZgyEykJ1fzONs9Ri1xmfNXixAxHwitExGI28MbtrywWcg8FQ2MFeOxMYx30XY9ghg91tcI5FxvFP-jcmAjmdtjgRtDnocvJAQPAEtfoWtiQug9PpfklobIVolBigz3w6ZWoJLyaC9jvawraGxWqUhY_hpLtcQFIQKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=plGrs7KCWMt7--eNpT73VUTmCUNffvzipxum6l0v6Rza7qWVl8WKOMo6b8v2xBETEFYBdeamKo_wPGHuxmZP1CYYKOKad3TbLxb4640NI_hB2IRWXcumXag_P9yKnC1G-QcPaAESBvydj8XLtpyY2LMgkKYkxElOT9qN4wzAJvbo2nfpIQoiZgyEykJ1fzONs9Ri1xmfNXixAxHwitExGI28MbtrywWcg8FQ2MFeOxMYx30XY9ghg91tcI5FxvFP-jcmAjmdtjgRtDnocvJAQPAEtfoWtiQug9PpfklobIVolBigz3w6ZWoJLyaC9jvawraGxWqUhY_hpLtcQFIQKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از کشته‌شدن مداحِ سرکوبگر، حمیدرضا رجب‌زاده، این یارو با انتشار ویدیویی مردم رو تهدید کرده که اگه بازهم بیاید تو خیابون چنان تیکه‌تیکه‌تون میکنیم که پزشکی قانونی با کاردک جمعتون کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/funhiphop/82011" target="_blank">📅 14:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82010">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جزئیات جدید از پرونده حمیدرضا رجب زاده:
به گفته رسانه ‌های داخلی؛ قلب حمیدرضا رجب زاده رو از بدنش درآوردن و مایع منی خودشون رو روی جسد این مداح ریختن و از تمام این لحظات فیلم گرفتند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/funhiphop/82010" target="_blank">📅 14:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82009">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">محسن رضایی جای جلیلی رو تو شعام گرفت
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/funhiphop/82009" target="_blank">📅 13:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82008">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جواد لالیگایی(نکونام) به تراکتور هیرویگو
@FunHipHop
| TaymazROMANO</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/funhiphop/82008" target="_blank">📅 13:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82007">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZXk6Cp1VIm6K0EObxJQ_rN-aiJ4B1D0c1sXb_RgrWhFMYgO-pTIu_xSIPKyy1ARiqdPB4HREy1GrxV3yNc0DNcJSoVqrrEU8WhziZuZByu_h5eOb1eCMUA0-La8NqQDiwsAJGyl1xntxCZeNA2b0LL3qXMj5c16i5WmwVde7uvxLNPZwV9yOon26yrN_5gvjyFLjTvvv8a2-575EwhSp1uzhnNUHfnVasp3XJqP5uoSt181fhHIwKSU9HjdUMRQPGcs5mIXoZoz_vp_HKGpcvHSFGbAn44MoNZTiGcNQcC9Y9GZ3iLd-lsNuFNHyW7GAqkWk1gQDynChCwR_UHFPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرکس سالام
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/funhiphop/82007" target="_blank">📅 12:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82006">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
وا
عراقچی: در حال حاضر هیچ مذاکره‌ای با آمریکا نداریم، همش تبادل پیامه نه مذاکره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/funhiphop/82006" target="_blank">📅 12:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82005">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هنوز متتظرم تا انقلاب نشده آیسم نخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/funhiphop/82005" target="_blank">📅 12:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82004">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWPxLVBp2gMNKUjNnQD21dMBJ7WRu0noUNs4B8y94Wtn60mFrsbyhwmzC0HIAFSX-qrdD4ANzCHrhUhZa3Bp2F9CcQdB9dHkqgBP0o_eEzMp-8vkCAHcWnFj2UNelEwDTmBV8XQ_yDrFVN-jGP-TQpZ07O9XZVsiBo2CA6VzENTHRqQK-boBP8kIklO8iXjioMBgZQR-U5UQYUJf-pCgG8E1E4US3ZpUjLoVbpo38t5VkkPqxvq3fRDq7eu3s1bD31iX7DjJL8dsje-ckKrKJq64ZhHK8K7nsX4Km758grW1uVNep2SuLlIc0-4GsMRh-xwEtYNAK6zKBHHF0NtDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس Calvin Klein صاحب برند معروف لباس زیر به همین نام، کنارشم دوست پسرشه
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82004" target="_blank">📅 11:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82003">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ectVdjwDgtRcEUPGjRPHPXZt99ZuQzcGG9XmEGSJ9hxNPvICprAKcartUQOeeB55gC8xOxM-DJveSeulJvvNvLKri9QfWmDms_-aYqJYNYSXM6EJNbWk8mlWUkhkSuGx61_m4QY1MwtgT_wAILl-SBpLryQRRU3vFJWqO9qzFXDwiafbnA6AB1QHkQsz2ZpTXjE4qufJVBhNoBsJfFgtQTVrDDqG1-eJeWDMnDCYt9J7XPccUy0QQ0z0U5IAejo-zzceHUeQ8xx-0pEADMAuKifonlU7cYNCuy1gqwdVHMu4ih-QalZIVy_gVe4sjbWGeqoPjPrJnm6PPytPyEoBog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏩
کانفیگ فیلترشکن و پروکسی رایگان در ربات بت‌فوروارد
🎲
🤖
با ربات رسمی بت‌فوروارد در تلگرام، تنها با چند کلیک فیلترشکن پرسرعت (V2ray) و پروکسی تلگرام رایگان و امن دریافت کنید و بدون محدودیت به اینترنت آزاد دسترسی داشته باشید.
🚀
سرعت بالا و اتصال پایدار
🎯
کاملاً رایگان
🔓
دسترسی سریع
👍
برای دسترسی به اینترنت آزاد و بدون محدودیت، به ربات تلگرام بت‌فوروارد مراجعه کرده و سرویس مورد نظر خود را فعال نمایید.
کلیک کنید
betforward_bot@
کلیک کنید
betforward_bot@
🅰
r18
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/82003" target="_blank">📅 11:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82001">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=DdMQVHQb4FJ9UzPFvF7XSRTvj8u0fq80Dz68d7Gn8dPpwPKvoHyJmilhHoa6w6gESHLDSbrZ6XDqyxwuB7qsDMHZ_mdMK_w9T9Qk1GkH0vCfL0ay_tY4CJGzZnVL9oEGdnWqyzCM6hs3CZIh-GAQ0q1suJC-xEvGJs_nlAvDCU17S6QnJnB09Gu1GZCn0c-7DSPF5b8adjKCSQOtISdT1Fx7jFiZDLuhYjEt-yciDSJzX7GW5sc5VxSux-GLh-LdOpzdzP_qlo892_dCKx8oosYlKwIJR_pBrhisKMC-1DIehsFI8vbJywguIEDPPLJr6o5Q7-cQMPeVF-xWNwG2mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=DdMQVHQb4FJ9UzPFvF7XSRTvj8u0fq80Dz68d7Gn8dPpwPKvoHyJmilhHoa6w6gESHLDSbrZ6XDqyxwuB7qsDMHZ_mdMK_w9T9Qk1GkH0vCfL0ay_tY4CJGzZnVL9oEGdnWqyzCM6hs3CZIh-GAQ0q1suJC-xEvGJs_nlAvDCU17S6QnJnB09Gu1GZCn0c-7DSPF5b8adjKCSQOtISdT1Fx7jFiZDLuhYjEt-yciDSJzX7GW5sc5VxSux-GLh-LdOpzdzP_qlo892_dCKx8oosYlKwIJR_pBrhisKMC-1DIehsFI8vbJywguIEDPPLJr6o5Q7-cQMPeVF-xWNwG2mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاسر قلی‌نیا پس از کسب مدال طلای اورال کاسپین ‌کاپ ایران، عکس پهلوان مسعود ذات‌پرور را بالا برد. عکس قهرمانان واقعی مردم همیشه بالاست؛ اما امثال هادی چوپان، جوری فراموش میشن که انگار هیچ‌وقت وجود نداشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/82001" target="_blank">📅 10:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82000">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بیدارید؟</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82000" target="_blank">📅 05:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81999">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بیدارید؟</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81999" target="_blank">📅 05:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81996">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/skrxpDSXGnMTluLCtBvKcqErFmM4D_SY_No9ao2Tk5gq0wCoO_36urfDfLyw1JWsatGo4E-vgoLAoVK77gt9OxWDR20Brq6CZXTQmmEMpMpa6kzMoCFLMKX9euHR3kAmGWiJiXxBUH5JsKxAuCZeTQFf3Me7lYpmMCpsRAcEZUVpP2njQ57qgh5nCCYcuypWgqW1b7KFpM1RJcQz_5aOv1_jg-npNFsPr6URPjKgFZhrn7p47hKIizMicyrInhDYJciufaGL_9PdCNYbKTqhSA4mpAGoSbdhtH7qptlHRT62RMFtqUvkkXi7GQ8as0oxcMN5RxY-CwRmBfc608N5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icqDdHlxI88OwbxqdFeS8sFe-QFj3C78CXOriAbZxSR1TGdf0z2wLjiKpgJJByEBINPLfSqHOTctVnfhmzgpa4_bueJoNUVcmhS9ga5S00N0wvc8j5qplD9XKse2gi4zPH_NiBf_uTj6CXsD6SicfU0smu4SKco9LHTGPWY3Ztf2VJz3ZnyRgPUN2HzujeOqooIu0sZKP9COgg_XDyocxHxrVDyMfD9dEIXP54uHItVfEiQISOFk2u9j7ANVYU71An2dc7zmIlDjEkKyiO89aBLw9TfDRrh-TiiZXQ_SK91tqBdrY1vu5NV1fxDRNCImj4fMyvV4HkQiiHZGG9V5ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بر طبل شادانه بکوبید
جواد محجوب ملی پوش سابق جودو ایران که قهرمانی آسیا رو در کارنامه خودش داره با رکورد بدون باخت 0-5 به سازمان UFC پیوست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81996" target="_blank">📅 02:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81994">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwGRdtH0esK5KmqRsJcuAHeclxNhb3czToIivVGIBawbeqNXnfo9N0kbEn8GXsxAH46SNBwsNi8K1C1kcUdXUO3Vbz6PlGkR3rnDoAkVuiLZlhCg729Xen3vfHtAM3q_mplK4zT6P5FU0BbiejaIsabzxOy86oVI5G8L_E_wIAwZUZ6bY1OVov3iyBdyn4nkArcQ6VkvSc4ffAWgiBoC7q9Lnac9htEbzzhHT5aJ0NWdEKTIKDFTiustIN9FY9OWtZKpT6OeUlddzaw_disP74v1rD9Ebcg3zBBj0p4_Ri__AwQPMnlrMrLnARg_0kgePIucdE-H3IgDKmYDWlrg1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کابوس و دیگرد به اسم انگ منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81994" target="_blank">📅 02:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81993">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyzmslOO_oEIVrmN3qbr-7fM-fzpkvYXv3pr0BT0R6BKVdhA5ysDlhWNDRsou9MKDNGkeV1GUnye9NW3ouaPF1xYf1q38PBeSRBW9rHh11KjZl2KZPodGZTO6Hj0SCGFKFuoJjr9Trc8C63FeBeF6gim3DBMDGPtfnHOu2Zu0-8tc4e2NZNSzXJu1R3WsYf_6cHvrLKl6Q3s0pSAiCcqlwzz1V5-w9ubHl9ViukBLnJct_q7KgW4emvJNM80_YvPOCiJy9zXpFWp3r4vzwhurywnvPUhjIs9SOGpKEyikQVXqvJ4pYLko8okmX2ausLSB44sNwcVOrm-ebiLHQjI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از اعضای سپاه پاسداران در شهر مهاباد با نام عمر دهقان در روستای «گاگش سفلی» از توابع این شهرستان کشته شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81993" target="_blank">📅 00:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81991">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این کصکشی که چتارو پخش کرده چرا اسمشونو سیو نکرده مثل کصخلا تلاش نکنیم بفهمیم sha کیه z کیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81991" target="_blank">📅 23:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81990">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwfCwltSaOnAIlJLEM4bMStNy2yAPRN43O6ArQbZApzMr84wUq5RnPGb8mYnB8L94XI1ub3VR7vdVBqc7lMlr9ZHPWOlS2g2WhaGMwMmyvRce76y42qtjuOwxCdv-fLEVbTRL3bxUpfT336pt7Nz9W5pYzF4v74rVsnStRZimjWuKE7_zneBO8F4Ln5tXCjB_Kqqu7_k277JJh0EIEAesAgQTQG5fFAv6lnDTChF8pAua9Irx290OOdgLMoasWflj-VHMH4K5ULAcyl7ui-9g-2fvF3-JhQP1NjlNekVHPDF1LE4tEBar3oMekzVKvh6SJuTGmkhAwzHvxDfm66UiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من که پیشنهادمو دادم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81990" target="_blank">📅 23:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81989">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxvWISlBAtwV95FgxC5uXK2yDTF6dviLF8khgdOMFj2qe2i7ObJO06ppFKt4r1aDOin_QlWYu8P7qtfUuhmQVXftTaQMeqqxpyoj0iSiaHO0rdA2VjQhSQiflRbetgIKBuuXjKZicqc8W-P6IxGfbWYYVnnJHnnICL2OL0Uz3Q7-tD7uTo-QeefUXVb2oVcBs961_YLx_xQNSVB7ErgevLsRPGj5RdXGJQkPsb0o62CUW-sDS6HAtKX3z1HBJvZxPL1-QtL7BSdYqJi7rwBgYiXGRiDZlfZ10v-XF_nQwOXXXt6d2l_QNGpejIwFkIA2Yc5waDKCuDkyQTOSBdcQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 کا اومد به لطف بیف با بشری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81989" target="_blank">📅 23:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81988">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کار به هیچی ندارم ولی تا تلگرام هست سگ میره سیگنال کصکشا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81988" target="_blank">📅 23:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81987">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یه مردی برای مراسم ختم خامنه ای از آلمان اومد ایران ولی موقع برگشتن نذاشتن برگرده چون کارت پایان خدمت سربازی نداشت.
مجبور شد سند یه ملک رو وثیقه بزاره تا خارج شه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81987" target="_blank">📅 23:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81986">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLti7xAz063FWsdDgPOcQg8ABlBjxc3FuH2J4DYWmfcwqliCXxRa_1OO4zWvBLpyXyAIReWj8Udpg_fTOc4FcUbfRkwDZej371qX7WX8tbTOPqz6yi5ybIGFXebge-YyUlA6vRjG7r0k73yGoQI4tR1HsEaNpMW0mbhJP3zn7VHxUsQqB9xjz8mkr-vJqrQ9Vw-7w9MoKZCylvjKp1thN9csTsObNyGsS4p88Y-j7EgS2Q205lxdWThPFOHMGS7Q8n46WC9XSsWCig9_dn_uo3GMmUmskbupZORUChs_35dhTzwpW-8Z7P2-xd_hPld_Sq7QGAiXuzUU0oy8jgwiuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای این فلک زده رو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81986" target="_blank">📅 22:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81985">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFNsFdCMosfxkg_up9NTupiXiDEtQcuNZJsgnNzzDsG0dc8n_wAb6pu3X5mgxGxxei8gIl6UcruQo9deeJb9qS0-_HgV_lX3OkZ6VrNf2DUiExLWyOuAIe94944rL5nLYmWI4NwF8L1SNChStzLLA8xAVSHSR6YFFFgfsOHBi_oRv-YnDz59bfrZ0oR_JCmtZAJiWkTFrCwSwq-305WM7P6pG_6_cBbyGchjzasn7L2lX8qj8LlkWaR4qeteIMRwMl5TVjauQad3SyKYKWLmMqLcZA1XIpvosJkRqCLjgH9N2MnAJ9M4s4pZMdJ0PJLjMqk0Jmwghtw-hvwZd5z4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای این فلک زده رو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81985" target="_blank">📅 22:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81984">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پوری تو ترک جدیدش یجا به مهدیار میگه رضا پهلوی رو انفالو کن صف تو با ما فرق داره
ما؟
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81984" target="_blank">📅 21:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81983">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این جمله که "فدایی موزیک داد جوون مردم و فرستاد زیر گلوله" همون اندازه کصشره که جمله "پهلوی فراخوان داد مردم رفتن بیرون مردن" کصشره، فدایی نبود مردم قرار بود بشینن تو خونه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81983" target="_blank">📅 21:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81982">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قدیم اینجا میگفتی کص ننه فدایی
خشتک رو می‌کشیدن سرت
الان چی</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81982" target="_blank">📅 21:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81981">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWZ9xvjGPftlceBnLRaB3cSO3WJAyqViKtNd50XUgTxGLdwm5EBALor8nOvbl2eaRtllKUf9ufzHOEeh251ES3zkngJXLkM6CW4fYB7u04xmx_6Uahcrk33KFp3hh0TVrQvGnnE1MmqqgPU2PGq0g4i4wBrvWXNkBAma0X4sU1Tyyie1jX4TV3wgkRya0qaSPhVabX927LPsUqzZJGh_uBblNjJ4CGHzII_B6ATzB7TV4nt9Xb_yxTGEUUe9o6s20vBvpZMiqIumXp1cmEEJ3UN43MxMbUyJ5jAwUMYBW1be9M4qx4Q0qHoDuzfqumSGGDo4VN0KJpPMiQRukPf8OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی میگفتم کاگان چرا نظر نمیده، که اومد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81981" target="_blank">📅 21:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81980">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اتاق اصناف کاشان اعلام کرد:
کاشت ناخن در کاشان ممنوع شد!
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81980" target="_blank">📅 21:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81979">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">جذاب مثل بیف آرتا و پوتک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81979" target="_blank">📅 20:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81977">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تنها سیاسی خونی که باقی مونده ویناکه فک کنم با این اوصاف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81977" target="_blank">📅 20:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81976">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خرید VPN فیلتر شکن نی نی
✅
بدون ضریب
✅
کاربرنامحدود
✅
تست رایگان
✅
تضمین 12 ساعته
💎
اکانت VIP   قابل استفاده در آیفون, آیپد٫ اندروید, ویندوز  پنل ها:
💎
یک ماهه (چند کاربره) 25 گیگ : 74 تومن 50 گیگ: 149 تومان 100 گیگ: 249 تومان 200 گیگ: 399 تومان
💎
دو ماهه (چند…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81976" target="_blank">📅 20:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81974">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUQTVJ5oNdS2ZU3TAaGyOm_cmclayJbtCyRKQ8n0XFcYw-1KL1_sDARmZ1C06YBz5z0jCm6DJiRApE0gC-7Cu08DOExDKY-g4krw_n9mfyS1qydM_97IFFOqt7tx4TRMd-BCTC2IyOAMdo9wQ4MeAhUQmbUKr6wQ4ysZVD2B_-GYoRO-SXDbZwYfkX0jzoLPicZWzD-VSFKkF8YEh0tiz_gfXXdFVbxS-rRC-BK3WKH92W4sFJdC9Paaj20xScKyuNL9MJZ1G1bes4oOS4lM4oNUnM-T8KDtrVjcuUcjb9xbLUXjipNc2NZSteRohS2hgoo_4GkKOVGqtYIDQQbIbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید VPN فیلتر شکن نی نی
✅
بدون ضریب
✅
کاربرنامحدود
✅
تست رایگان
✅
تضمین 12 ساعته
💎
اکانت VIP
قابل استفاده در آیفون, آیپد٫ اندروید, ویندوز
پنل ها:
💎
یک ماهه (چند کاربره)
25 گیگ : 74 تومن
50 گیگ: 149 تومان
100 گیگ: 249 تومان
200 گیگ: 399 تومان
💎
دو ماهه (چند کاربره)
100 گیگ: 349 تومان
200 گیگ: 499 تومان
برای خرید وی پی ان VPN (فیلترشکن) به آیدی زیر پیام دهید
👇
👇
👇
@Ninivpnn
» کانال اصلی
@Ninivpn_bot
» ربات اصلی
@Ninisupport
»   مدیریت و پشتیبانی</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81974" target="_blank">📅 20:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81973">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6r9caYadZ_dkDs88bHjpNsZ860JOl-VuEwgalOSF1SOjaIj9umT224Go5UciHtpLm8oLrc733ObBkxECSl_x9imIDSs02cb04uss6krm0vrLdIOr2yHARmx6sDltb7JTs1uBULzRGLIMuEVC2-AkWtv13AQ1FYNQhHpkRaFjuC4QgyRUzqEDgk_8-052qrcFjdQu1h9ePQxEDxBBvRcBbB8NLLvmRMqNU5YEl70ikCD8MlJDE2bAjNV6nNQVFcDIQbLh7x5xq15jC03EbyjXa2M1pmBrMge2C6mBGtZh15Pnae2pMJZkGM_G2DNjnsM6gaNnI2qUrITAdMrUKqjAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک وقتشه بری دایرکتش آیدی دکی رو بدی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81973" target="_blank">📅 19:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81972">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OU8JwyAr2Lx2Cv55BpL0S58AqXobnElS0I3xW1jC_UZiIQvNepASnq8mvIG4-IeUzV5nHGz599Q52PJg0h0E7k9WS8rKMGEumYeZ9K3Om_fFQ-n2hF9aVbbqXRbu9Evz68zXGuGL2ftlJ6cR0eRhogozvPIUO16f863vGSJhKwxja8jUzrvWkcx0iUBL-679qRzHHO6ORsCrwXjb5DspHhFPMqyGZGpmb5Pc1PyVFcQKkUg3adFfmtsNGsadsNioET1V7sYq4PWeQHNnHv_L3XqGbBuCaHPmEmwKj4SellcNFFRkxnO6zHx8i6zOWeqs5qw5RyYlLPy1cpZE9QSWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پوری گفت جاوید شاه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81972" target="_blank">📅 19:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81971">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iln2E2GDj31mRwiW0n4ug9iSoaqKlT_wkT83Cx6_FA1uCyS0aYFmcVwa-FE7DG4TUvyUktj0XjdGLZBXv3IC-EV_tkGo7VS3JV4VB_fdhGjJH3vEwJlr1rd1BZxoVzFOKSGUoR2JDSc7qSlNwdV1xv7c3ogokqH-R96xwwkgI-ViGCL3Ukqd8yqXDwg693FK2bhU9R9gNY3MO8zuVI34Vr_a15sPte8vRI93zW-Y8mPmjAJWEY7b0Wze3WzSvpGTKBh-l0cFU0tvYHV2dmrUd-iNJIgt5WAz2SvtKX6HYhMF2i9BLqH5ak7g1zwpyVIqn38DbX2nbXaFMrcnt6Vc7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس بک قاف به پوری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81971" target="_blank">📅 18:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81970">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssCifRMFL7RC_tMt5MzEA617j6l6r1rfS7BnmC8JsTALmgNNKtybQbNiCwtcMh5aX0fR27LaT0u_7adSRDLuhjNMJx2WWjShEBWvU5igQ-jz-U1hzhXHm5XZG--lOVklrSZMmLZuelO8T97TB44dCyciT-tfa9FedYl85sMOIazPyKp6K3ym-cQG54WHAvQp3HqW0FexxJIQbvbDBanl0OaVmtcKizPJhEvFaFvKQXQU09kUy8pCfg_KK9qJe4TJoflCcvXZuy1lyOuPYsgLjkv-7aH896LgE4F_H4bhBCRfeRi9qtOHwWE_hMjSXQMCiw5FMXftjK3U2NSuOcxtLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پاری سن ژرمن
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
شنبه ساعت ۱۸:۳۰
🏟
ورزشگاه گاملا اولوی، سوئد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پی‌اس‌جی در ۱۰
دیدار اخیر خود، پنج برد و سه تساوی کسب کرده و در دو بازی شکست خورده است.
✅
منچستر یونایتد در ۱۰
دیدار اخیر خود، هفت برد و یک تساوی کسب کرده و در دو بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پی‌اس‌جی ۳.۲ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر منچستر یونایتد ۲.۹ گل در هر بازی بوده است.
🧠
بازی آگاهانه، نشانه حرفه‌ای‌بودن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g17
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81970" target="_blank">📅 18:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81969">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3CoWbRteLEvcnUvqFAtjJwjo6-F1XWqwcXitGnCjoO0IasvNgU6ZBy3ggLjPRV4TgKi21qrEQklAFrShWvFnyoEL419W-BWGcZw96ImM1gXIfUPVUsXucxJVwaPbpX6Z_OSlUTkA5moJhQNLa3D7TIAhJN4q9xzPMJUT-IO1IbHFpdjvuNm9bb6iZaoP7mKZuDiXNgx-tPj16OTopPclsTCNdOFNk9fwR-xRerJRQ8j-8ZsXTJjM37wKbuH_SsxgvdyMtZnZMKv8w-QtrjfbF8-z4Dyj5GN1LrYfQ5hn88TvgTtpDICXn91c3fHRhvv5VHmWUrWN1sjsSx4qR6wBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییتا اون یارو که چتای ملتفت رو پخش کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81969" target="_blank">📅 18:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81968">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4gR8N4hkOen7YuuDvqZi03PXFPcJBkdreA82Yb32yammCQKGhgVr1PqC0p691gVvppFcJrOMbINS4Lc4HNguH4Z2MNkPkyIHYrm05VBiEMhY15JBXQz0WGj-Y_py73GDL1awSYMZtNlX_Q1-2Z-A9BO6aU_hThc1lJiFD1txOdGNJ6w-MS3oEQ-CyVKiAJEgSpf1iqlTqQ_DodURYg4V9NeMqf5ijWzZPZlCucOxehZBiNEyPBQqjizm2IgiFWtGNSsAPB6jRnQUrGKwfXknuf1AvVttPSG7_EtS40khEeUFrzqH81mb7_gaJLYq40PgrkAoyQIL_9GdPghdsjFHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع کار بدجور خرابه.
@Funhiphop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81968" target="_blank">📅 18:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81967">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خدا لعنتت کنه پوری ریدی تو کریر فدایی</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81967" target="_blank">📅 18:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81965">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">برگردیم سر پستای غیر رپیمون بابا، رپفارس اونقدرا هم جذاب نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81965" target="_blank">📅 18:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81964">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA²</strong></div>
<div class="tg-text">فدایی 72 ساعت وقت داره بیاد تکذیب کنه
وگرنه دیگه مورد تایید من نیست!!!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81964" target="_blank">📅 18:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81963">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بعد یجوری از فحشاشون به پهلوی پشماتون ریخته انگار اینارو دوساله میشناسید، همیشه پابلیک اینارو گفتن دیگه، پارسالم برا اون اتحاده اومدن ازش حمایت کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81963" target="_blank">📅 18:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81962">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">چتا هم احتمال زیاد واقعیه، ادبیاتشون خیلی شبیه فداییه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81962" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81961">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">من کاری به هیچی ندارم، تو این سالها هم یاد گرفتم به هیچکس اعتماد نکنم تو این فضا چه فدایی باشه چه کس دیگه
ولی سوالم اینه، اگه فدایی کرج تا لنگرود رو نمیخوند اسم پژمان قلی‌پور انقدر ماندگار میشد که الان داداشش انقد معروف باشه که بیاد برینه به خود فدایی و همه ببینن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81961" target="_blank">📅 18:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81960">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">من متوجه نمیشم، مادرجنده بودن فدایی باعث میشه که پوری مادرجنده نباشه؟ چه اصراریه داره برا ثابت کردن این.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81960" target="_blank">📅 17:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81959">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترک جدید پوری به نام تیغ تیز زمان منتشر شد   YouTube Aparat  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81959" target="_blank">📅 17:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81958">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خوبیش اینه کم کم دارن فدایی رو عصبی میکنن و بالاخره میاد تو بازی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81958" target="_blank">📅 17:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81957">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromㅤАмин.⚘️*</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1s01wOc_6nQmta_RzFd2pnlbNLkJM0vmos7D8bMIaPxm6mViSfGzWv_KpDCo9QSjNpH8C_r9EuEYBRh4sunlQdHz7PdBPMO4LwhgpQEmZt38yUSXYBXMAWoMMVfEnHzNekAS_0ZQqgsVzXydTW9cHLhtxItAYk98PTlasM0Zfjmbuy5fp1LV4IwMA9WL6_-_d0Hc_Av34w1IPiXuCFxTUoh1Jk464PLZhbbI5dnnS755D13Dq5opOjfMtxPtyDal8oRYvRveftYMimAVvhi5oSKTUhZ-V-eVdLAxLfzPTbxAZG_KTTAcPPRatsV4bTqi6pkSNFVpypAiEzMc84W_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81957" target="_blank">📅 17:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81956">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترک جدید پوری به نام تیغ تیز زمان منتشر شد   YouTube Aparat  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81956" target="_blank">📅 17:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81955">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">توروخدا به ملتفت دیس بده یکم بخندیم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81955" target="_blank">📅 17:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81954">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترک جدید پوری به نام تیغ تیز زمان منتشر شد   YouTube Aparat  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81954" target="_blank">📅 17:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81953">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebAfQMz2UV8FcI1xqXHClXqMllexy0VPsQvELaF3oE1lOycJdbkD7SILiERL7Yj-1Ei4unj6VoszqnunRg8HGoKMcywlbAU-vBtBHri47S7zVvcFghVOG9TamcgpkA7h4oEwV_lHFgZsofOsILvg9EkBChvRmjczzRKWqjQfQ7R9rVD-ep96nYyoszBX8204LjTZ-q1MbpD8jVGtdbWYzCMXaLrmMM9UDjWfzD4qZyqkXX1n-k-DIVDRkam68g6U3fpac7P9XmOnXXrz_AocsCE_uH9sprAmrQbaz-grd00Q0h1Y_oArGyEMVoX0rF_izcSztVpixOk-wT9pL0TH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوری به نام تیغ تیز زمان منتشر شد
YouTube
Aparat
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81953" target="_blank">📅 17:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81952">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">توروخدا به ملتفت دیس بده یکم بخندیم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81952" target="_blank">📅 16:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81951">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مگه اپلود تو اپارات نیم بها نبود چرا طول کشید انقد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81951" target="_blank">📅 16:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81950">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خدایا یعنی قراره کی بهش دیسبک نده</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81950" target="_blank">📅 15:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81949">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm8KiK15NuZrRc1n05q4KVagUrT-RfjYMRCzXHPIgURsLQO8bOmtstoaknUTbq5Z-RthbY5mtDd6Jz0zt_3XL88eD4gjuQ5sadHvNlwYijQ_JNFjCwvdxHdnnZsjCMW19eBaiDZ0LogF-uAxrozwOifWlsrYHANiPXYtbe7NEKJNql5CptkNxJosQ2RKdFRudit7eUHHIOcQCv3jr3cQm000-9BXpui8vsE9qbVeDvhIw7tKjIjt0QfD_uYGtP9WcxVB78EwTu0Sba_iDQLlZTGJfsCNbEoeXv9-pRyK6m-cYsVgW2KlJu6HJWEm9sjk0zEOXPVn7re0zjYWX270pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
لینک حمایت از ارتیست
هست چرا یوتوب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81949" target="_blank">📅 15:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81948">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پریود شدی کسکش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81948" target="_blank">📅 15:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81947">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پریود شدی کسکش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81947" target="_blank">📅 15:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81946">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCFRCdKh2w4Bl8DSe9wIcjiL0jUDNW53VttyP82FqApKPjIgRY2uVsAfRLbnWONv0tSR4PPCMTpgjSfBH2gXKlJ4hGyAT5kUaB7aXcMtEAovYW1Vt3F_kCYRTIFFTetEhGA5Qo_N65C31_cKhUG6OyQG7tZ2IVjt2AVMDAJV_LlhsrFHFnqYYe6PMQDLKCY42XIC8FI5F23FcxMFCGo3E0VSwcYYVDY2nskLT2TXbi1Y-fF3XPCKRMxV40g84Vj3rotZ_R_KNQxHFzUxVnpDn21ezDjlrgYP4tWjLQ2m8vMv9FZLwhDlGpWTIVvKzCnGea65lbSNCwZUG5qyUC1IRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پریود شدی کسکش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81946" target="_blank">📅 15:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81945">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKXeNHnQ2NP_zjqcGacd8h42JBrXFrxpOrNNF2hzXori6PtZrc6ZS7DaaQM-QNsUqSyIWox5V8lkX1QCWMbIxBNgP6gI1pQy8uc5wvnKQVhtrL67o-3a9JG1b5NiyEq5PMStpPoyoN9831EZD3TzNoZRghe4WmwWfRu6hD7LZnOqZ0StkDo86lDdAl7fgisi0KAudzqYvt3Cn5DDiE-Gq4K9gLFHmxXV0cMWLGGGr0rWLbnQs9VwK3tJQai5ooD4L4YZUrmKM-vQaZZqmgoY8OL2G8aCjtS5djq825_QIi9rlCbF8xnuDZ-OJkTQVYWRIixeeZC_z9wj-nqys57ZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه مسی، پدر لیونل مسی در سن 68 سالگی بعد از یک دوره بیماری سخت درگذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81945" target="_blank">📅 14:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81944">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبر اومده بابای مسی فوت کرده ولی هر چی چک کردم خبر مرگ مولرو جایی ندیدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81944" target="_blank">📅 14:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81943">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">صبر
صبر یعنی واکنش در بهترین فرصت
نه در اولین فرصت
پوری دوباره اینو گذاشته چنلش
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81943" target="_blank">📅 14:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81942">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edcae0795c.mp4?token=m58rXi5Y_Vf-ueymMqSluvCjVh7QVpgdFejxduKlqknzshiPfuS4Rm8E66o0o-I6jsygNisAbE_PJPS83tRLGDk4ge4zuIincWugcFfbw9JMtHt7DbEzWxS_nlpevCnoMPGIn-I26ZVG80OwsZpip3xm5PXHrAZAGyyhkv4-D-zLX9pEkZldrthjtAIMI0btkxBWY8bu36W41FsNfJEd1D8tnr2jXTkG2-FXb8nQzJqsPiBv5o5hHj34KkOLrXsb02YIExYepPp70J3cQDx0B1GvjPtvWmbQZimqPTLoC6lkHCMHkWVc1IfBCMhQmqyPriHoi9YwrvvJ-2sJgVWg8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edcae0795c.mp4?token=m58rXi5Y_Vf-ueymMqSluvCjVh7QVpgdFejxduKlqknzshiPfuS4Rm8E66o0o-I6jsygNisAbE_PJPS83tRLGDk4ge4zuIincWugcFfbw9JMtHt7DbEzWxS_nlpevCnoMPGIn-I26ZVG80OwsZpip3xm5PXHrAZAGyyhkv4-D-zLX9pEkZldrthjtAIMI0btkxBWY8bu36W41FsNfJEd1D8tnr2jXTkG2-FXb8nQzJqsPiBv5o5hHj34KkOLrXsb02YIExYepPp70J3cQDx0B1GvjPtvWmbQZimqPTLoC6lkHCMHkWVc1IfBCMhQmqyPriHoi9YwrvvJ-2sJgVWg8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هههههخخخخخقخخبخی۷خخخخخخیهیهییهیخخخخخ
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81942" target="_blank">📅 13:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81941">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2JylGOaKVxJPRUZnUMMtNzw9Bx_8R4N9k3qWKHwI0PvOjY1B4FTvJuEeXImi5Q97w6z5j6qnLuT229GIZsU_23xUOYOBcGpWjsNsDEJxErBDocjlFsZrlTsujy94Bhc4zSNwivpCLv0gB8qu-oHelc_hjgGzERDnzU_U0ouOYRyOynvyw8N4WfUmPvWKMwmE2gC__NA5PCM2i1se3SFFhDGnYL4spe8rzMnf-HYDYMhvhhoPuuc_iSijgzUFcWtAswUy6b5Jt8lr6icqkftfDheLXgA5tcD6U42J_nz4XfSHcOnm8bxzrmEJanoSXLJoZ9EOxu7LsBPplR16nahxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمیدرضا رجب زاده، مداح حکومتی توسط گروهی از افراد ناشناس کشته شده  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81941" target="_blank">📅 12:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81940">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEBoQRUY78lGOU-srKhnvYnhMsw64Ws6LgunrC0KE1XZkxZY5D0bg8uuyahIP_5Eo3tm0L-MDrBRHG9rrr_fyTsDJwvx7H7e2-B_ufgp7Ycdn0-2IaAf_qsfEupoZ8o161ZbNLJo-fo3ssPkL4ytEcWk1Gl5raEe_BJ-MuKTvOFGmRjF1T7uj4qqD-GfqUs-LBilLG3PxlJZWwAsJkH3RFarP7o2p4UyGUh7t48KR-B02VNzDIx5QLm6Daeuob-R4Ug-a7bqdYu9ipOeGYFcTuXr5GiFa6jJ_xGiz6ddeE0thidz3bSTTTmVzqs-qX1tQAjMVoCupxzzm8FqGKBPOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ah shit, here we go again  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81940" target="_blank">📅 12:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81939">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAy7p3fUd7GsAvHOYl3woIGVgdQ3vcDlAxis6FuTwQkrhYW4l7CwpCafs6rPjaQTck2JZGa4Xq_e_Ee3GS7s5FsZrR74IAkB8Er0zdRKViGVz-e4riC-6b4tcGCgmBkh8iA42RjJU4GKIuY6dJ4ELtqZdhmuhUJBjtorLRMN5aRjGmxFUDOtkcCNw6wdx82uepWI3lnrgP0T9UhEjBloQZQF8Pw_YYwss_Eu5a4un-71oXFF53tYryHUkychQ8kgyrkNLVfY2e3xVZj2eJlLwLPu-vK51o5Ck8vA-t4E-LfR4fl29AE-8rh2VCaT1hG3RP5YHBWJEczKSkA8kow6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی قوه قضائیه: همه اموال منقول و غیرمنقول ساعدی‌نیا مصادره می‌شود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81939" target="_blank">📅 11:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81938">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktg682xsexDn_nAOFmr_gzrvzdQlOpOAVVp9y7ZRjfCpXzBNl08w4W1udfSmEK2isNmFeYqeHyMKm3bpWxwTwD0MSJunpHZ1yQPUrXxCGx73Ae2YJbNAteHHdi5iTY-MYdmq5eg6ME0R640a6StQusA9rXllTAnUbu5JBQHAzT8C3fvtLG2xGEfSsXzxGX6vmR2f3pp-47vNd6cO8Inpp_DjPM3YI3T_gs0STH3xluZiwAD15dt9B3Z9sg5Jr8AZlPjZ9OuBZ1W7CDGKdq2EI4gviK8jUuaINx8Zu_njAfh4NJq0602r9KCZfUm41CIL2OHvlhdk3cjr-s0uiuW5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پاری سن ژرمن
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
شنبه ساعت ۱۸:۳۰
🏟
ورزشگاه گاملا اولوی، سوئد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پی‌اس‌جی در ۱۰
دیدار اخیر خود، پنج برد و سه تساوی کسب کرده و در دو بازی شکست خورده است.
✅
منچستر یونایتد در ۱۰
دیدار اخیر خود، هفت برد و یک تساوی کسب کرده و در دو بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پی‌اس‌جی ۳.۲ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر منچستر یونایتد ۲.۹ گل در هر بازی بوده است.
🧠
بازی آگاهانه، نشانه حرفه‌ای‌بودن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r17
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81938" target="_blank">📅 11:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81937">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3XOsxBlRQpJuTisTIxU-xuqNMH4V6dCvt1k1vxfp-z9RAX_weJaZIfaB5lACk9vTgbe9ndXj7Sgmyz3AMamNRCcMp1pYMSViCfZGnMAgSB74_YbCMSYL56Cpuyq853xdLIt6RwO4duVvpjb1FjMTSqy-BP71P0KY3vNJLL4UqUPa4P1yCpNVgNA5Xg8c4RerQeX88EA0yWe_dLZbyZePhuizCIrW9p6wCrOIeEiatfUyUzIoN3-fj1TbBOx_LtjtVSWzEgzIQQdR0Hrlq3au0McQBgKkzFN655DbSxdJMQ46unGD-GgOJT0NLR9GQ-FqKIdvbxNmzmKWU62Ee7mbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک لیست و فیتای آلبوم خلسه که به زودی منتشر میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81937" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81936">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2u_MBslNW1MKJZaMYA4JIxnkgU1a72fbfXAu3_7eYZcE2VM8iaiu6JTatc6w-Olgxx0uBtJlHGo-pgot30m9ja1ltjTFTuTsYpEAsfIw68H8oPeXpJ33Z-MIhytEPn4GpAmN2Q0Howxswm2AmExMj8_8xUQlv2pWXtm7fzdp3VgCNEHsmcHs8Ra1ujrIae3A742jZg1-8ZNRe1ITeWM7tJbfGf1899J4qkQeNvpUfZoAx0rjIhHRY7Btoy4s2TIOhaEPq9JXTkAHjGQUQ7ixEJm8Re07OtC2AET1_iefKkZsj1yqp7G5owk76A-O70p7H5PZQLjbzYMI41QBevh3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها حالتی که ممکنه پرز لحظه اخر رودری رو با ۱۵۰ میلیون یورو بخره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81936" target="_blank">📅 10:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81934">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حمیدرضا رجب زاده، مداح حکومتی توسط گروهی از افراد ناشناس کشته شده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/funhiphop/81934" target="_blank">📅 01:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حاجی بارسا چرا این فصل اینطوری شده تو یروز بازیکن میخره تو یروز میده میره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/81932" target="_blank">📅 01:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81929">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KK_Exf0RWtVSvOCgSyLQ356nldL5ZXpZVcHG6rktCJDIHiyowtUC-zVMzSpQJRDCBA8q-P1YdMeq3YL0Q8pPygiGp02B3pTO-sae0VydREAYMHCu_v5TYK_VFjGGPX812UN5kXMaeF0KmB-JUsXzHcY8c1Lv1RZaknx1lrLcwDU3C_AfqY_MHUiSPZZVFAq3LCRV23yJMVU_DVUHeIUA1nyjx0Md_554zNFmuQlReGrrtm0lpRp4A40uxgASU7BdxN9EdQU38izvAyqd4uBhBkeEsyPrectkJH8Lm5glYpWC4gQOkh_i6pj23tizWsLaek0eeJEJxRvPeYOwMXsLoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oEbLqnR74omHnEB9gK0Kqgy5CWx_e6zdRJMqM7YK6mPbg2Ffm-stCKqoCPmoaRSMCIP3Y1EFQxavg-uT_ezDfDvrbAePYi0zwZ6WzTloWvBNy2n_ysMwuszECKPZq0HMW-uzgiOjyXrAtnSIY_KvCaFYJ9KuL6aoepfxvQXStzuLCmnWXoot7ykk9qtaHSo1m3BlgdNdRRYYaCn3vYJwZcdmX5cCKW_EJlrMO0mjig-R0t5eKCfKxWb-MgzkhdpQEAZEVJaXMcNJ4VWP9ZoUqYb9vwQN4u31i_Uef3_no03DV2gBdmq1AsrwA9-HXae0SydZJm2R2UXlnR27o8l-hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رودری هیچ پیجی تو فضای مجازی نداره، حالا فنای بارسا رفتن سرچ کردن رودریگو و رو اولین پیجی که اومده بالا کلیک کردن رفتن تو کامنتاش دارن اومدنش به بارسا رو خوشآمد میگن
حالا پیج کیه؟ اولیویا رودریگو خواننده که پارسال اسپانسر بارسا برای الکلاسیکو بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/81929" target="_blank">📅 00:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81928">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904b3d738c.mp4?token=UYRZ3I0NjByV9rNFihaakrCORd9bC9Zy95E1bSqiKn2DP-z3ZQsRO7rMl80auXwuXbfCc7gDX7mbV-oYQQsDb6TSNYke78KBRbdgc_ZH_CMHNqnoLHb5xA2pzCW-HQXAkBh4sudtWorFNGUSnIqpEtSh-BOIvaLXrgC6prkhdswmL-PcxjzkcRapbz2Ocxr_5jXgebGfM0RafkrKLhdFnRJeyCDDZSn6SA0WPJvl0EYZpKoQT2f3GDmG1vTuzXs9Ic3qqET3pCv1_uT6_GnntTpLf-Pm7XcP15mOS4fy1XeSdr007FcXhf070WxPVgB93rh_sE2yXaMpFaNIx0QhUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904b3d738c.mp4?token=UYRZ3I0NjByV9rNFihaakrCORd9bC9Zy95E1bSqiKn2DP-z3ZQsRO7rMl80auXwuXbfCc7gDX7mbV-oYQQsDb6TSNYke78KBRbdgc_ZH_CMHNqnoLHb5xA2pzCW-HQXAkBh4sudtWorFNGUSnIqpEtSh-BOIvaLXrgC6prkhdswmL-PcxjzkcRapbz2Ocxr_5jXgebGfM0RafkrKLhdFnRJeyCDDZSn6SA0WPJvl0EYZpKoQT2f3GDmG1vTuzXs9Ic3qqET3pCv1_uT6_GnntTpLf-Pm7XcP15mOS4fy1XeSdr007FcXhf070WxPVgB93rh_sE2yXaMpFaNIx0QhUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر جور به قضیه نگاه کنی خدایی این یعنی تعویق دیگه.
ترامپ کنفرانس خبری خودش رو لغو کرد و به خبرنگار گفت هر چه زودتر اینجا رو ترک کنید ممنون می‌شم چون ما یه جنگ داریم که باید پیش ببریمش و برا همین باید زودتر از اینجا برم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81928" target="_blank">📅 23:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81927">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaXebBnyHy1_tKD8CIiaL43OguhUaKXEFkY-PfhCSjbPmQNtHSvwY7jvnve8dvaRxisQuW1bTeU2r_UROEUQk15YfEm4O8T-Xndo1FHuHo1BkEU9mqfU-9OllTH39hHo47bfPLWmjvt0_Pd4FyP4lXeib-brkWlmiG20IqpO1MNyV1z8nmsWLF4ZmvdTw8hknSauqEs1nTJ1i6axUo_qETWDf-G7gJhkNuBuiyoaChl20d0w9Xutj-VSk2EVtNy5xFD3hqAfqfAXc60OlmiLfX_hQ0kkmeASRpmwf5Qu56jXsIKDUyr13K5R191Gp0xptMDmPXzJMN_Qhs_Io-V1bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رندوم ترین عکسی که امشب میتونید ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81927" target="_blank">📅 22:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81926">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">امشب میزنن
بماند به یادگار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81926" target="_blank">📅 22:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81925">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فری استایل جدید سروش هیپهاپولوژیست  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81925" target="_blank">📅 22:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81924">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فری استایل جدید سروش هیپهاپولوژیست  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81924" target="_blank">📅 22:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81923">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فری استایل جدید سروش هیپهاپولوژیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81923" target="_blank">📅 22:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81922">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzhN6o6jP3HlVvzrfpWYvUGLGFPs5WaxwIdkwBN1Oi112dcdy4AmlpkAQ_YLC7rogqICsE0Io4zyRf6gLYG8ajy8wa8rO5K1VT6GLWPfdpBciST6BzVFtVdqYflneFj1-s8216twNN4RsYwR8z8ANWjYyF5FxCzn-v5M1_jmwWDNcoi6YX_wx8yTAaGrdZ-T2Xcsaho4OIqXKRY5ClbBjk2QRxD8McD-4I_tl9RZ9vYV5iuyg2A3g8kMfjoJYk-hSFgTu-Qyy12Hf2jNof-3xw1TMcsi3DJwUoIrKRJyu_tecyVBIsROnsbTMLPzRzk_kNpOaPS9BvjgJTAtFFXBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبل البوم دکی هم بزودی منتشر میشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81922" target="_blank">📅 22:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81921">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTBjiDFYNeBYG51CtLQKnFBSt_n0COSnA5I1lRz11jI-LjIuCa2s_otAnGxYATx7xn1MvnDvkGWs_3XmcFQ2YNv2UREPmTpcSOJI1nrtDjo8a7-yuIIJ45WfhWow5bNEmUICqBwPlY7xHTq8CNGLxL92SnrlVsg5c8wzslY4v7VNhrS-cBP2zRQvlExDLafTGw1YneCcNEGB5p0m11TfomiOBnkGV3d8_MCDNh2UpwHLl8mcK491F3-kG3iBQuZy5SfO1IhYDXupTXJ0S-Z1gj_S3Ldf7UK2mhSBDtFFo0Pm4G4mUE8jW7pqc_kvYEaRZ5RzdBJ8JnqppLAFCwa09w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دکی از نامه ای که مادرش براش فرستاده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81921" target="_blank">📅 21:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81920">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e30792ee17.mp4?token=OrI8AaK4lVIHFMa0p4rbSKP9Jz88hb_RJxQnOQFS1cwYR3UA8DGYec47rTeKmuYEgjEbs2jq28Fl6qZlmjL6NjOhjMcOfSKj9LnwbRMvftSfHF88ZoNeixbP5BTTuCV4dJWc9c85XQq17hQD0NSooKAeIbkflSZ_Dim_EOs4XRwvDcn3KuT77kM0_WFSsOkMdekC0i5nt0biCgxHnQJBhuqgRLwLrXkumxrYR7fBB0tLw_Ah8h8xXRNWsXcNBW6KNe8LztCnU1sMBQR82SJ9B2imxOTUzLLHGyMk9LrHHeqgrCfQ_SJtxc0jWbxFNhzYH9p9wt5bWezE4jiDvyoCkB1RbSTaZdetst8EjwGo6FOb7hLEjzz6v9U7dlcgp8XA3DVnCO3Gn9UPcsGTZFXud5pislIboQcHgsZ4Qgh3NOJv148jEkDyqbWQmCyeCmeCdOw1l1QIpuqYwuMcQ9BEhDQbB6kt3FQrOe1VTpaLVVe6Zts8kXmpsXtLdyWmispkLAvMN8o-3YL-Yn1XriF9PzJAQLBbtKJJz-BAGGCmxCDx0cL4koPsXGs2wcS9cVf_sOWTlY8AF-sXlU9h7ovZkN8vrIJGQqWlmYKmFwBBBxWwHFNCZlWl8r8BnuXEJb5xKu2G-dQYi6DZ8FOq4V4lmY7JhM5w0rKiHdqAxZJ0Fpc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e30792ee17.mp4?token=OrI8AaK4lVIHFMa0p4rbSKP9Jz88hb_RJxQnOQFS1cwYR3UA8DGYec47rTeKmuYEgjEbs2jq28Fl6qZlmjL6NjOhjMcOfSKj9LnwbRMvftSfHF88ZoNeixbP5BTTuCV4dJWc9c85XQq17hQD0NSooKAeIbkflSZ_Dim_EOs4XRwvDcn3KuT77kM0_WFSsOkMdekC0i5nt0biCgxHnQJBhuqgRLwLrXkumxrYR7fBB0tLw_Ah8h8xXRNWsXcNBW6KNe8LztCnU1sMBQR82SJ9B2imxOTUzLLHGyMk9LrHHeqgrCfQ_SJtxc0jWbxFNhzYH9p9wt5bWezE4jiDvyoCkB1RbSTaZdetst8EjwGo6FOb7hLEjzz6v9U7dlcgp8XA3DVnCO3Gn9UPcsGTZFXud5pislIboQcHgsZ4Qgh3NOJv148jEkDyqbWQmCyeCmeCdOw1l1QIpuqYwuMcQ9BEhDQbB6kt3FQrOe1VTpaLVVe6Zts8kXmpsXtLdyWmispkLAvMN8o-3YL-Yn1XriF9PzJAQLBbtKJJz-BAGGCmxCDx0cL4koPsXGs2wcS9cVf_sOWTlY8AF-sXlU9h7ovZkN8vrIJGQqWlmYKmFwBBBxWwHFNCZlWl8r8BnuXEJb5xKu2G-dQYi6DZ8FOq4V4lmY7JhM5w0rKiHdqAxZJ0Fpc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز جمعه شد
زاکانی، شهردار تهران: تنگه هرمز در صورتی باز میشه که تحریم‌ها لغو و آمریکا غرامت جنگی ما رو پرداخت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81920" target="_blank">📅 21:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81919">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSupport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4okhC64Th-0ZhjCYDXlyv5-nnw7gpQ-jCCzUOz7zw72ZwsklowkM-o_hcU-bpeAsYfIH44ZgC7JVquMRXw1I90rqrCxV6obsyzj0maqEr5zSJewP5YN53Ea-wgik1cXklB2meHvsjFgt2xnIBYQXb1Hoy9j4EtPdxZicvWlSQFEgx3sqWO-Z98SCaDEPhZvLpAkxdqzhqeVyil7q6-crUE7Kk4ZwF1ioy2GRv5Uwt-YcGkzaRwcs35jxScaOKcuJW99MZbvOjt5WsKvMaWh9aHOFyWafK9MSmBiWBxAwzGaE-HKiGWjH8_1HkjHAUFgULMpu-heuAtKO6TKYR1WAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اول تست کن بعد خرید کن
🏳
50 گیگ مولتی لوکیشن
🌍
کاربر نامحدود یک ماهه 105/000
⭐
⚙️
میتونید وقتی که لینک اشتراکتونو به کسی دادید که راضی نیستید در کسری از ثانیه تغییرش بدین و از دسترس همه به جز خودتون خارج شه
🕓
💬
پشتیبانی ۲۴ساعته
🤖
آیدی ربات خرید:
@SirenNetwork_bot
🏳️
آیدی کانال:
@Siren2rey</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81919" target="_blank">📅 20:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81918">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سوپر جام اسپانیا این فصل بجای عربستان قراره تو ترکیه برگزار بشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81918" target="_blank">📅 20:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81917">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SY_cibdE7qvOAs3XZ-I9aFIaK16gEQdVnJnhP4_ct0ZMk0pSZ7WkSGZSo_ejy9Fai1bGGRSwai_8gambSvOFeCP0mvPWchpBQRy3Gh4hjacMqgNkANMkJ5wgK9JBEe_t176azzKRauSct6oDCUXvtBEfLFjwffC28_Ca4wppy8Ps3OiKsV1AdmGJvaca7T3y4qQLzTwlb_STZiYaHZc1qYj3uMfLzw2IDdNFNedjkxMlMIno-sUHoHoXHIFXAfIq3iLaCQxsk6NJaejq2dC15s3i79Vlvk0KGaVaNwDmL8Lak0B2HmQtYDnWly55q5qVDgCnla5cLeb6hEZ0Yk-elQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکش این چه رفتاریه با نعمت خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81917" target="_blank">📅 20:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81916">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=SwzIZU4YMPZ6_o14yfQCr06Yu-dqam57TNLsziKPp_L86DVK0-KkyZc6B8Q0jyb_4wTAKxlZHq0y9YTJEzrCcJMKUkHAhPmUilZzLhT-1J_kXsa0b9oCNWwmu61RHtXM2sobNGnQI8kJr0K2py6J8y4A41A7iatTgmR1J06GKwoizD4D5iERS8fChqyOkDNNmTA2h2zVoI8jhZEUsNcQNavxjV7g7TaK444TJOmiiHdxMKr-g9t3wC7DlAA4T3DgQTIZdRoJ0cXAQWokClgUAql60iNhRds3aRkABC6081cMXOoRF8qvLtEfG4YGmldRUMyjGF9Q5ZI_CS2OEG5v3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=SwzIZU4YMPZ6_o14yfQCr06Yu-dqam57TNLsziKPp_L86DVK0-KkyZc6B8Q0jyb_4wTAKxlZHq0y9YTJEzrCcJMKUkHAhPmUilZzLhT-1J_kXsa0b9oCNWwmu61RHtXM2sobNGnQI8kJr0K2py6J8y4A41A7iatTgmR1J06GKwoizD4D5iERS8fChqyOkDNNmTA2h2zVoI8jhZEUsNcQNavxjV7g7TaK444TJOmiiHdxMKr-g9t3wC7DlAA4T3DgQTIZdRoJ0cXAQWokClgUAql60iNhRds3aRkABC6081cMXOoRF8qvLtEfG4YGmldRUMyjGF9Q5ZI_CS2OEG5v3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادمهر عقیلی، قطعه‌ی معروفِ گل یاس از البوم مسافر رو که سال 1377 منتشر کرده بود، بعد از 28 سال دوباره بازخوانی کرد و تو اینستاگرام منتشر کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81916" target="_blank">📅 19:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81915">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo76dM6FvCy4qXrLGdsQNr41ZKpxatnhyBkjvMx3SqQwMZDNcKCvwcjtAnj8Dnob0jBxg3GqRNffmFsoCfagSGxaKKtPa4WIRQcxcOhBzwvO_QiHuv-TLTxzQmrwSicin1KkRAJebHJVOKNOPO7aDqFreiaSj2L2eEhS-9XiFtazdPjaeYF9jr-LA9Z2iOALX3BGAUojJAfaxMGz5BuHb7s0kbu4MVvk24wpAviy_R_I_0oksWnqV3mYOkdeAPx6WGPMXutVgDtczfz_vArBpbA-qDTE6FYBrJwyskFhuYcofU1etwk9QIDTYC-92-eVS1l7YR2uG4T7MN882ytnWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دی ماه تا الان ۹۰۸ نفر اعدام شدن، یعنی هر ۶ ساعت ینفر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81915" target="_blank">📅 19:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81914">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxTGFPI34YdNDY8nSK-X4K30uj7F4lcwwZs4pJPWuIeivrHiWYzgFd8ii9DSKnd_7RDPPEOn5rgKsg-WC6QMtRh-eMEc-djH04hfBhQnvjqRNdbAXQvN1yHYNHZNiD9o52iIqbAVX3biKHmxz3BdtSG4d06P4NMpi0Ncxuz1PzxatJJfgrogEJd3KOJazjJkfb4pvEICbknOmVKwPI7OQ5wXfVTJnKFvEt0jW2aAa_W8AZnGAnh494RicH-e-LZ6fFmjl_ljZ7jHNFUiJA88jHHc4UR5rmXliP3UEAzRlmnDdEOxFJxBXBBmQCUKLS0YXR6zBoleMghEH-WnpSs2Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
میکس روز، تا ۳۰ درصد هدیه نقدی بیشتر
🎲
⚽️
برگه‌های پیشنهادی «میکس روز» را انتخاب کنید و در صورت موفقیت، علاوه بر مبلغ برد، متناسب با درصد درج‌شده روی هر فرم و تا ۳۰ درصد هدیه نقدی بیشتر از بت‌فوروارد دریافت کنید.
👍
برای
مشاهده برگه‌های منتخب، به بخش «پیش‌بازی‌ها» در بت‌فوروارد مراجعه کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g16
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81914" target="_blank">📅 19:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81913">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امروز سالروز درگذشت فریدون فرخزاده
فریدون اوایل مرداد ۷۱ تو خونه‌ش تو بن آلمان به شکل وحشتناکی با چاقو کشته شد و جسدش ۱۶ مرداد پیدا شد.
بعد از ۳۴ سال هنوز پرونده‌ش به نتیجه قطعی نرسیده و هنوزم یکی از جنجالی‌ترین پرونده‌های ترور مخالفان جمهوری اسلامی تو خارج از ایرانه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81913" target="_blank">📅 19:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81910">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ng33JfqZSxS25o3XdFCZPjCaLXHhFzA6qjNWgc64MrjoBt8Z4nwQQhkSXXPTahZpzSg_PRhR6wqRJzyZ6YUvSngXQW1xnhJf30jgd5AKPHhuTAScOvoXIkajakWYYXvIaTMN1c3xUgVOrOFaXV3oH3ayq20Di0fOZU30cnNoNOr9vQLJlGZqxzW8gROKjvB-ZgtZRGGX6Vf2S-peuAhsfNYQ2Z-zaaSiT2KTXmpZ-Ntu1auPcvY1D9l2KSl8JWSGpvPK34C3e96vN63ZBxCIWZZYBLrPNHvDoGr18ra2iO1BsI_5oexUGbmN4NXGCvcaOiMUQWrBhtu5gwVDXUSO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XcXrnhWIuEyBnr_8buirnUv4lANXcalWBO2AoQ5h4HlF6mp8zbfVkhYZpjiH2COtnhh8nNBt-80kcUVAXuc7h-GOqonVGD_TVFsIGImmfiPkQXTs7ja55JPZZAKGWKbMO7Wf5yYlfinm4L2AcSwDjMd_cxCfH3vAt9uBYEbtpAOiMGIqI5VG8tAMQG8b1gDKrBuNJ26-66ZyaYTlq4vvWtq_DSmaLOAHPONEXk2kfR9deMYMaacHzAxgu8IOYnIcTSiv--ozDze_6_8sLlUrVPQX22Z-HlelbaOj7r9SwBH0L56TN8PNRn85a20_SJ8uXcVUeQK-QrJOTSGv_1d8dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از سرگرمی‌های جدیدم دنبال کردن دعوای تیک تاکراس، مثلا یسری آدم با این قیافه ها دارن تهدید میکنن که همرو میکنن و میکشن و فلان، از صدتا استنداپ کمدی خنده دار تره خلاصه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81910" target="_blank">📅 18:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81907">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYLXM_n1yhNrXpw3MQT5OP9juIPb8w5EKA9fIqZMN5_KGzPuUYl29IWaxr4hyATcFziDh25CFJgcpZDJG4y-OAoeGrFje3JPnIgZasFErIEDOpJirOF5UN8NVPOlHNbnlafgk9D-Htxssm3S3wCKn9mwTQ3ZXkKmHDrN8gt0xofZmNVDF-KCLxIZNSz_51KuLHw7fFXbkkuSXLgqss9CCpW7IdOkZmrWOLuO7xgJboo3_G6U8h3vnyDoC64Gn4cfv8-1Effaelj3oo0WxAft9x2zOFOVNwaFOLKP46ed9oC5da9wh9jLXWW-DoYrYDbSerLTTr1QsMTieN1nFGvE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKMk-IcM-DyJF09wSYh6thDgcRGwIqiS4XJ87JP-P61ci1acb5q9tLis9zTEwwonSr8idTbG6YBzKHR9gbWqk8kP_pd7S-ULL9U0L3LSGoStpUdO4sd7jcf7TO2Z79iYFRYIJOIy4SpFGUwSXNvLfm9DtrVXVj5e6XElfD5ZxEdKVv40YN-OcfiRDF0BqeRyrniaoglKxUh7eyXquxBqLx2Op4DDToITT67ftkniQuGb2FqkUQ36D5K9F9IDpO5KPXYBg3eT0lpkJNu-6Vt6zEyd4JpCArUOsYfDpcj6d150i2lDuEhwyu6K-NCji8GJWKbSm7C1ZkR696FFKTJzYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از سرگرمی‌های جدیدم دنبال کردن دعوای تیک تاکراس، مثلا یسری آدم با این قیافه ها دارن تهدید میکنن که همرو میکنن و میکشن و فلان، از صدتا استنداپ کمدی خنده دار تره خلاصه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/funhiphop/81907" target="_blank">📅 18:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81906">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOU7TiBlu2jHs77a7HRtrFRGXKd98io7wKxqToLgP7LpiG5Ze0dsInq7BtGiP8eoRzJDkX8WENZxa6JWYUqncn6repwkULPPmtkGf-8jCeIESkpq3146AnCYO8MGTG5ek5AZ-yvWo7-KS_MqOBqXhoquBkMUGIR121fQJ4snNDLdXXGg3Ljc3CKRG3mZDQtF4DZYsPzIhsmYuipeDxbfkXKFrszLC2mgaoMfkPQlMYVdLMhSJyx54Im5aTn2sDWD2XmqGAwbZUa3BeJtCxu57kYdVHTsXYgMkVZ_KXunJYr31FttnyGp0TA4uyHWXebF73pJUmxEhkGFde1WKZNGXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زبونم لال زبونم لال یسری منابع میگن حال رهبر معظم انقلاب وخیمه و هر لحظه ممکنه فوت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81906" target="_blank">📅 17:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81905">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrQ0CXmC1MW-R0cZb-6m6C-Oww1cKCjwCyCH-Xpt_cpZDfuJ4seCOq-53nJX_n0wSW5JK_GNssvltsSzm4UcvcojXHdesAFcljUwhg4q9MTpmpj3_q1ep5RTnUvWXDlmzsmpjrgDgXCeJVb0e3wnWyKV0g-lFaKbPh6LPbGWitQov3q3kfV6TyxliwrjW2LFRXz9U7G-BDulGZoftbIuq51XHD6NahE_C2_5iM757MjbG_kqQd_UUgS6Q2MMAj9wY0fOHqNtELWeOae-1v36uLZ2M1dNTjhZkI1D--71ftOXQaOE6_edwTDr46wyXZ0Zn-A9aJ6VItoy7fkCL1ve7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیارش خونه ما عزیزم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81905" target="_blank">📅 16:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81904">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">همه این خبرا برای اینه که ویناک طلبش از دکی رو یادش بره، لطفا چنین اخباری را نشر ندهید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81904" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81903">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عربستان، ترکیه و پاکستان یه توافقنامه دفاعی امضا کردن که هرکی به یکیشون حمله کنه، اون دو کشور دیگه باید برای حمایت از متحدشون به جنگ علیه کشور مهاجم بپیوندن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81903" target="_blank">📅 14:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81902">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6XrsbOzIJgaHjyEZ5lE7aSSsN1Ri6lO0TI1lUpEJg4oeLbn0s2vzCO8WqACLti7rp-8UWL6iusu3jm14UjB98Kf7hqOIIYnXIoYdKsnRkDPxQ23dZm2gcefRIjOBmzumG23Vui131WOz1y1QXjGtAuMJGCKdyMopDRwYA83HzMmLxPclyJ7HAEiDb7i72ZOiuTtoXPfsDvKUmR4th4LzO2kbE3a3MmhQ4L4S5X9Wgq0xN2vr6rBl8_vpXQu22C5Sd1s56RbaUuTD4Pn26Crn-BcO9qbWZmqwcFs5DETRzWmDYoX2NEbL1pMBL8gD-l6FfKE7bcYy8qrCakrw9lIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من از خوندن اخبار خسته شدم اگه بخوان بزنن روز میشه همه میفهمیم دیگه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81902" target="_blank">📅 13:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81901">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQMPnqR7LJL3WlGFz5JWRiaDK5A9cn9GvzEgy5Cf04buDJacVm1tWL0O2GZ7anthMyFwSNwbCdUlD2NLpiYekxGlE2tJWqZ4CCkm7LXJRNahhQhIP2-1l4DUbWOQnmUmCHb7lX4F5ldSqGP3stxi1bv6HpoeoDUBZ_PoiIvluPIu4ExTZJF8j5xB6ruocdXt26F10G5DbDrdTbP08DclY35YcbGY4ZI8FXm_tgcRCdF8BsAP5yvuwX9w1egbkP_gIIGs7POu_TFlIY0p0m4I6Nf7oxS6PJPWu9wOQSXHx44WhOcpydl71XUj2muCDM9oZOnZZ4rEb2pzdZTbDzHH7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ah shit, here we go again
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81901" target="_blank">📅 12:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81900">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TL2ya-tS9F25FvO2dWpm_bIoYpn3xTMOEEvqYgNk8j8jYMY1qiwP80mUv4X5gbgStb1mCeuOb9eTsDhO7OkvK1ej8HLCVJlKAUYO23epVW9MaHpODeh-gGVGGelhrJXvV-TGf2WIXy-nxJlUsm7m9_ZqhuhqEyGzdmeqDHoFNBX6hW6-LO6-UgVS6HwELHXoHyRIABqQ6kfDoNlAgkHwOLR9OhzIOuDnQo_JGpk8HalZjjdAfaw0VCf98jCa2NHNbeCiQlL9OAbrIUe3gaEi-pHycQesrVahQZEy5fcB12q4SrPdIb-01GuT7SStDltf4WHhfMFTWkMubQUafFGAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپر ایرانی اینجارو نگاه کن، ایران تو تاریخش هیچوقت گنگستر و مافیا نداشته که تو دومیش بشی، به خودت بیا  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81900" target="_blank">📅 11:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81899">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDQbon6yWtjOP5frZ-bMtpijMpZO45s5l6dT26HfXaFD9Kbq6JfW2cIG3DS36SCx_AMibVG2FzgKqs3a-lCxHcYxZZqaUdMbXC6qOJm1dLxD70LIG-60X1hRbOpt_H6A_tKQzafv6kFEljWEL7tbFAakBzv3GwrflosPEdZrZYlorFVj6yfitWbrrmyXNZmzCOvpGsvGPwZhX9HIwPfdacMZ2tJx6tXz9Q58XBSSz9FBXIroy1hvQ2E2hP4J4OSJ3u29DU-okz3VBLxlS3n9O79S_x0MV9J06aQQ87nfqCqgFmwSmrGc8ld_1HEwzpRnvcNgokBNSdUe5v8UZ9kJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
میکس روز، تا ۳۰ درصد هدیه نقدی بیشتر
🎲
⚽️
برگه‌های پیشنهادی «میکس روز» را انتخاب کنید و در صورت موفقیت، علاوه بر مبلغ برد، متناسب با درصد درج‌شده روی هر فرم و تا ۳۰ درصد هدیه نقدی بیشتر از بت‌فوروارد دریافت کنید.
👍
برای
مشاهده برگه‌های منتخب، به بخش «پیش‌بازی‌ها» در بت‌فوروارد مراجعه کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r16
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81899" target="_blank">📅 11:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81898">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">متاسفانه ویلسون یه تماس تلفنی با پیشرو داشته و اینم نتیجه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81898" target="_blank">📅 11:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81897">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هر بار حرفای ترامپو میخونم دژاوو میشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81897" target="_blank">📅 11:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81896">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un_hWTxKdMjNMHNz8XcBOfZWipxTSenpXdy5LmtkY1yZ8C-px5nvwLIGKSGQtb59Msali8XiiB9N91vNc9nSzGfS5wZ8-IpnpJNmsVx1HONRPjoSy0ta0bJPZx-ffMyhPcNXsl5JHWJ0oP-he0EFdo9-OHO0CoGh3lfhinCq-3sXxOs89eceAxbXfAW8OYHARQW28V5lqPPdYYm2W4kY9SDcgK--coUwoiXfSYCBPblTAbKh4IpcOJBP9l3wQTThUQNwfxUE_yiFh9DqXO9SiPTCvOoiIuzbZ284zUZHWQyavjfqgE6nZaKqo7OQDuzvkGtOxKrvjh8y54keOWdgyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.  @FunHipHop | artin</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81896" target="_blank">📅 10:02 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
