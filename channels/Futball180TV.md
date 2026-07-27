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
<img src="https://cdn5.telesco.pe/file/lKncEe7zBz7hl2UtJeuPpgnKfuCPXOwvPTzoD0p5IjFq_XCbCXF3ItbfU-zhpyNq1VYevMMacTHrKPV-IBEasGUU9c7oPmmEN5c8vlECoEuB6Xi59ViWFUrTMnXAb7RdruTqKGleeFoMlIHUSOyjv4MO_ffBvFJtxmsUq_yZXD9SoTs3kqLxi9mYM1VK15cd3GMddzAx0yG_B35h0QgFOd0zcucmXMJlfBF81guHVdob8vnnbZL-mGNV6HTpXe2LkXo0zdp-MbJpkc3SkCcCJ8mdu-hKTAob4OZGjS_OfiL4IEiVZNx3lpPJvl1azLkBEWAaSG2pefYKXa6n3EP-aQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 524K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 12:21:40</div>
<hr>

<div class="tg-post" id="msg-102054">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebffP0JjbQ747RbG-W2N4qx4aM0NvdWinoQ9a73MUpQrrkYp-F26pbxoL4SDUJcm0zY69_-qjm4dlhodKuADiW5M99KatHxU_Nl6Ags-bj1_UE3YFosDU8ytZcOk_rzj2OLeGjRZMPktl-xYnvWSvk0FTfh6DZAtPYVx66D3dBDu6ZA5vbCQ4QxBd50stJB3EhNH2xVLy9QUXjPbKBL-5LpjnE1gM6kOUgK7i39hdohPdCibVCM1N2gvgnQ47rNv5Z6X3N4SlZIzcF2QsmC6C_k-JrCElmU1dF_52x6Cpzq3u03u5F7nn0gtScnkFwXSOZy5U1WC00oNCO_5b9q5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
الهلال به کریم بنزما پیشنهاد داده بود که به هر باشگاهی در لیگ عربستان که میخواهد برود. اما بنزما این پیشنهاد را رد کرد. این مهاجم کاملا روشن کرده که هیچ قصدی برای ترک باشگاه ندارد و این خود الهلال است که می‌خواهد او را کنار بگذارد. در واکنش به این شرایط، بنزما خواستار نامه فسخ قراردادش و همچنین پرداخت کامل ۱۰۰٪ حقوق باقی‌مانده‌اش طبق قرارداد شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/102054" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102053">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChWiwSNlUgBsASpCasJpnNAivaqFAflA6zuiz-x7oZGxmXGn8Hf3mzDtZH5B8qZMnN_ysCGgPWD-IMdpLYIcIrWt9YCA8VeiW6TMGR4pmN7Bki_QPeEGp1wD99WfoeUB4784yl2cvm4wTp0JPe4Y9E4RgR0OHIu4JAUkd-Q95GhoCxlNWa1-fpXFtDV_HLKKkmOHCSUa0NC_DhrNaEEAtwzg2ewNO97BCjUf99d6jrBHSfGk1IO_iHbU5ZCOwBhGbhkHwjGf2Y8YVUUW6ET9MuRS9pG6C6q_cT_7MjmhWHsZ7zvVivSg4Kd4WG_ydzLaC02lP_tANHKeu2TNr59X9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا رودریگز درباره اولین دیدارش با کریستیانو رونالدو:
قد بلندش، بدنش و زیبایی‌اش توجه من را جلب کرد. جلوی او می‌لرزیدم، اما یک جرقه بین ما شکل گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/Futball180TV/102053" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102052">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCE4XnxmTAfNmJ5hRr6W3ajuo-_PnjnLMuEFzwhnqAE7HlLSdxcLYYAh2kQDHRLhTwO5NglIBF6_irEhvU4zzxFmyIbWt9L6MCB9S985e2Di5VTLUhgtxQLPQHXvhnNcWRA78RVWNb-VayM0GKQt9p5eCfJwtElfLfsjFErWa512ticBcJvaVhZTzVV2eQM678eJ-O-CsxWw_TAsRWkXMJRSMW_A-ftVPKSMgoQjO1oV9ns-5ndHXKKQu1kAWEZoKJxNm0vwF7Rh5TLFsnh8ZLl3FSjU-DgLLUwy2sNi1k540PhWGGfJXaTidFWmJp3VXiyOvtq_S8ioTo9WD7Tadw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا و ژائو نوس به همراه زیدیاشون تو مراسم عروسی گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/Futball180TV/102052" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102051">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=VouvFJkG23N0HP8tXpaFKUxovjucc050dS3Ddoy7Xri8O4Og9PduEjRwzRrmRIQOQWtF2tuNXkm0km5Qfpu5gJfcayO2jOzsHjp899Sy_jYxLgUyrdLcUfjMEIInQFEKWIf6GKKy6f-IQ5YN2Lk5qknaaQBTSsFndN5HN7fMassbxDdf2X2IeBmnCyiQNnZP0tBziDaPiiltG4rSCzQBoYtVpdn-7d2C5x-WLdyBuU5gvgUWUVBNWA9hGWkT7wq-zX-HQ29toHb3xEJu-id9UaIvjkjaNss9sH21Lfh0uBw1gUWobFM8upBbbXpB_RyALX9D_44zRLgOP7MRPjwipQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=VouvFJkG23N0HP8tXpaFKUxovjucc050dS3Ddoy7Xri8O4Og9PduEjRwzRrmRIQOQWtF2tuNXkm0km5Qfpu5gJfcayO2jOzsHjp899Sy_jYxLgUyrdLcUfjMEIInQFEKWIf6GKKy6f-IQ5YN2Lk5qknaaQBTSsFndN5HN7fMassbxDdf2X2IeBmnCyiQNnZP0tBziDaPiiltG4rSCzQBoYtVpdn-7d2C5x-WLdyBuU5gvgUWUVBNWA9hGWkT7wq-zX-HQ29toHb3xEJu-id9UaIvjkjaNss9sH21Lfh0uBw1gUWobFM8upBbbXpB_RyALX9D_44zRLgOP7MRPjwipQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📆
🇧🇷
۱۵ سال از روزی که نیمار این گلو زد و پوشکاش گرفت گذشت:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/Futball180TV/102051" target="_blank">📅 11:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102050">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfPw_DakiWIuYvgkhOksj-Eu4GrKo0CO1SaCccJc-PMsWUeRcnYHBKlL7vCWJRycWgTBj_HENipSrXXBVd143vflM0Lsqbfr6k1h12TJJ9jE-B2CvzEwgqbfdmvp_CkPjSYVzvMAIJBkUulkQ7OqbSE52s4TBDM8ou4TzhUGUNgatP8PdyzFLl_GD3tclTPzZJpsE1gO65O_D3qiNgq4wqzQLdvBWGq4Z0kB2nrpnkKIQ3YlGotOzYq7aC0QHFDWgc783ez7MKMxq-7CObBVeKGz28J0fr0F-ITSaGUpuRZMyMQr9SXkYSUwIlXjZ2K_RcFPd8zgEOHbXN1OjLwOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
منچسترسیتی مذاکراتشو با باشگاه لیل برای جذب ایوب بوعدی ادامه میده. مذاکرات با باشگاه و بازیکن همچنان ادامه داره و تصمیم‌گیری در مورد انتقال او، یا در حال حاضر یا در تابستان سال 2027 انجام میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/102050" target="_blank">📅 10:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102048">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ie5Uc4jlmGlSqTlO8QPQ2aCpq9qzLSDENCQjm57D5-B1FjT8hxiNl6LRNPoOxMRDOrxMm0gjynQ1ySGYioupVhXhLFohmD8H-OkYGwphfWGUPmtIzai5Sa9XizlIrhplULpAUsn-PqFKB9luL9eMtWGOpkmbZWkbRmG8JFmyJ3lCISIeYFB8wTtqH7b7kcfd9gZ1y9dnCAUaNmobLJIc_hX1kJT0Bcip7YZhIeNM2UohRsFTol4ECRJ12kxELcP9uMblqOx2MnqB0nllEUYC9fJX0eYzi54pI5qwQP8KHMNBx7vesL1Qhc4CNKbyJhtLisZodzXXlBThReafjmNk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5K9UsvBOEJm_xOFDpseRXn35KjlBbJYm0xq3a9dDPyFr3xmIqjzHbIwiHnWFbVA5hEANki65U1E28ywVRVju9VytZGhKnuVpzQxLiov9niHwoOaborVfVhSadf-iwCSWXUc1FLVki5xTRWnQsb9Hthn3s9AuuQJf5vwjE6KGw4nDgWwyuDtWGRbjlwfF3_D8kDo_IcB_sfxsS0FwLn67YeU6vURPjLmQsFy-xZdqgou7ORDtrFm-Alngk70d_K8LZ_TNZHKMJLSeJiKAM5maDuIo84oTKK9dX1kcR2ydzgn_DXTcmKv_YkB2L4ThQtEoExavQpkl-bza6lIYuDLuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جورجینا و پسرخونده‌ش که حسابی باهم گلف بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102048" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102047">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZq4GPifQ83R8SDEnhmqHe7hV3WNVwnqn286fZ1rZoEUOmqEckNJWZ3zPSSDCc_RoJdM7HdoNZmYV3pluFZazIlGAWXQqcwxsg1s0RQC5PeQG66yGHqpm9NejS9hAsHO_8kHd_FwO_xhF5C1dHEq7cr3AQLNo19UVardKnqkPfOFf3XLcOQvhwOmdPwj1Mgcak9G71AT0cYEDQqHPSTs2815IQW8Qt_oYIQJr79SxPJjEB2VBWUHkBe-N-BsfDJjq-aawJPjecWl70WIOBk-_kLQ4h8fFfEIhRYxX1A7J-KK0k-ptoVE1bxsqECIzWHrh2Osex95sl6ELnMW_QgMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الیور کان در مورد کلوپ و تیم ملی آلمان:
شخصا فکر نمیکنم کار در تیم ملی به آن سادگی که خیلی‌ها تصور می‌کنند باشد. من معتقدم مشکلات خیلی عمیق‌تر هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102047" target="_blank">📅 10:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102046">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MV50iwe06tVwV_Y3wtKxEd9oSEqCh21VediSr16G8WLyXw4XERdh2f-bow2e5b7uwMD20g-pe7g4BWPXmoq2xshYGJuJG0_FMdlAO30STRz3-5cBwYTagu6muo8x6rG8qMVnWFXBwxfLFTgd9WVXxqDr7fnp0MgkA3vgHM0uApE2R4QHwXML3kUMycH48HNbbBVbKwvx3jg66_96XQQbjmoP-M8ojRLmNEF7DTxI2LXyf5DyNMgqvH457f19LNxtNGbgwCzTF9BWdKNMMZ8cKEyiN8K04oa7C-Fj1udGlpLF63YQ59-pOx5NDrJYesriyZS8shPo0hGfd6Tz5AapAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
وینیسیوس جونیور فصل گذشته ۱۴ گل و پاس گل بیشتر از هر مهاجم آرسنال ثبت کرد. او می‌تواند خط حمله قهرمان پریمیرلیگ را فورا یک سطح بالاتر ببرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/102046" target="_blank">📅 10:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102045">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ19ttLEK6pG9hIvCKqn4agJrRNORHih7x0Rvc6f8Mcg7PGSl3uO8NjBdZTzeoc_Hdddg-7JuEO23zWJj0IiEvL6e3nv9o3sfWPaWYs-lYk1crfh8Stg3xI1EmXE95eJz0ZKu_DCkZ2w09W8DI7si_I80FANAQgfkUa5vRdaM8S9Hg4IRXbNcsQo85bwAcKgIfaweQPaLr8-CrMcE6ed73sAnkxY3lazFWP_MjesO02WU4tXCdOJYyc-e0FKIvmern4QzZQy_ZUFQgjtDTQuhh2e9TMLylA19X-4a8mPRcboKjeKfmI_X68tnp3hGLth3SfShoXBID6zncUlDrx4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو: پاریسن ژرمن تلاش میکنه بین رودری و رئال مادرید مشکل به وجود بیاره
‼️
🔺
🔻
پاریس از هایجک شدن دیومانده بسیار عصبانیه برا همین با رودری تماس گرفته تا اوضاع رو برای رئال مادرید سخت تر کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102045" target="_blank">📅 09:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102043">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWDV7TT4piyK68Tdr-mJaq6ZVZgzKHFSX8w_ig-u7D2vg2Kj_ewFiF1Wbn1eyxoTOPd2zKD1hzotjdKOxnv-sgzxuFYw0arT-d_m0Px_jKaATa5MvQgohd2R6lKQPeqUst8AiJDuCaCRG4UQBPOc4gEq2iZMO6BnjkH71gaLZbFnXiseN5mp2lmChVosUz_wR9sQ0GjB2P-dH1V-ppdniqcJrDa6fMismmU2qk6QosMT0979JeTiBOBNaPAA-VY8G1tU_CwOGrqJnKVtj6kNtdLRKD9PB1x_wEJb1KDSp92AyolFtSXCmvyzcysqZaWeF2QGI95Yi_w7o9eZnZVEig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3eF6WFMF5xi0w_zhtXcUp5TZLps2j76hX_Ab8Mw-HI5llfFe3WE7qr5Nck6OSQ3ltqlcsQk2_qwsDpSsRpq7RUI3pyi_sas24BoW2zFVBEEuTOXxLJBtt0Tf2oYKhg4rBIUJnRGKcwjvis2bgmWWd-TWnAgxP1Tkxnt6HoJ4OaN5zmWK1epZNyA65GO0TMcwII2vS00aizyvEd892nOwTtHb7Qn59pq3dmxx-tRhDQJ3BfQTvl-vJRB1kHLZ_b6k3XfYXN4q308JSKa8-5OfknDoRHavrxJqRfTCeC4jhEyOeXJxNmbjGOk1rnVIC7IDoyTr90CCUYv7qGxOuzLKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
طبق گزارش رسانه‌های برزیلی؛ نیمار بدون اجازه، کمپ تمرینی سانتوس را ترک کرد و بعد از برگشت هم در تمرینات تیم شرکت نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102043" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102042">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTt9dokoU-A02FqQrxqvVgDT9QXIggcdmC4zGnXQ9v6BvTjbG9AD4ZokiPz7MFHsKtczKYDHnb0fGv7SXXHX-9nTXtQRMw914RBbwv4yGXBKBprxY9-t1qoq10S7-G01BI5zmVmtXk0q2E3aW9vAzPF0tyeJHcKTW-3p_QJkCL8DhUU_fhr-D1vF6eyKLfOviSmp6wUgoaGeKbTLY1M1J-nfBSXRH6mrQ4-FQBNmpsz3S0Wj5Wm-rz2JQ1oihU0gPzFh4mEtumQpqcS_B9ATRFD1Y7US3VKIhY1Iyj0Cw8hBWcdKnZ7RGaRPR4r5CpirXT0nSRCgSJKQZXfo3npz1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولا شیرا:
رئال مادرید آماده ارائه اولین پیشنهاد به منچسترسیتی برای جذب رودری است.  ارزش اولیه پیشنهاد بین ۵۰ تا ۶۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102042" target="_blank">📅 09:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102041">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0tVyRI2F7zwr7B-U4jNYW2iCJi3xEDdNQahxrW4UVZtHFugHnsW1YS8lBW1UmeqwKm4NjfUyKR5th8BNE4Kc625GWXzXYuPkdjB1WmTjEh0AbbfyTCoUHFs7DVbwedtZ6oGZEojViBGsqNRgochDNaUAUxFFqzttocxyRzSl01XQPTPaztN5wpZj0ieolis2JYOlTtn41uwOO9u0rR_FkoWJocn79sx6f2gAca8q5Vm5Ug-6uLyZ3joETcMuS2SyegS2b_ICMTeT7_1QA86nVJW1nqsgL5JRBjbKAbFXIJv6L3r_9w7np7qtY_IzituA8E785dBiAIpSNmHXimGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اوه‌اوه یکی جلو فلوریان پلتنبرگ رو بگیره که ریده به سر تا پای رومانو:  حالا که ما را "دروغگو" نامیدید، شما خط قرمز را رد کردید. شما فقط یک روز پس از آن، انتقال رسمی لوزانو به آینتراخت فرانکفورت را اعلام کردید، و با این فرض که هواداران شما احمق هستند،…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102041" target="_blank">📅 04:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102040">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpdGt5Kgy1KiunEN0iqTlPaeZEzDi0vbGfThTfFvSATC6Q2pEKs0QxgIrBG0v7WwvxvJjnAEDyTbgZ4vPklVpfR6Q23xw9OFWrATjS9mBeZqojcyN4JX68uzdRh-1lZ471T7a6L_1POAN5uN4-F0EcgU482vVLZDDGOCPImX0P3jYF7J-CMPbc7NIxgNEnt8ppLGxnfsxBw4qpQJLsiXqaDvM9g-OSgaaWWqi0lZ7nCZBs_ERXEK8aarmOX6GhjGUw83bQjIIoksk_WBehBAO5CU57SrQKSp-QWHdSGs7aUJFzaK_jIN5QU2qcv7N5sF1JXRdnoiwY2Up8w61T61Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102040" target="_blank">📅 02:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102039">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWAvSnAt3rcVHwKgUAel5StFUy5wf1SxwGLQVYSiVTzDDCyXwlFjusCodkCe9cYeiHScBOUgGpKV1W6pKmXa808QOkJCssNOTt1ky3HeaMMS5huzSVq8HmpyivYPL5GQR7IyrjUdm53RiL7udQPKIsWWHiG4m2MlYVBuDI56f-JvY0uSemB7bg-NZtH0Ar1OEe7g4KmI6QLxspQ8QNgR1bFCllw1wxEpcfMn2O1ltFQRIeDQcSz_ROo9W_s61tfWnCXJsgWlu-KH021w-r6hCf8uyJvZu_pJXIoNUTgiFAk1QkcW6TGeI4hAhb6DaV2XaLS-6kpJK2d_i1-H2atnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری
؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102039" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102038">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWrrbqIYE468t1YJSj3UJjIkHjAGt6cc4J-wcAZqLBCpI6FiTXHn0-nh2_PTRlCpvzAUNSi_B5bBYR85zXKeK-EctyWcrcevL5g_5UV5bm-Ki1F8Vx1cCuM-EKUEo4hjdvsB_MgTrpwNevQ6AQ9B1uJN-i-d1MOw_evAHPNwtPJu4JPHDQf6ypVN1h3CHCCo56syXvBXH8fkaFlBv541rTp-F_yzfFnql9z72--mS2deWDrw9VVv8FtJz2B0mFMqIJi3fo1XhSccQWqoHy3Zsv4dIpsYHVM5Cw5RkWhzcuGCeDiRU0Qa7Ukl4WWIdmq1NkbJWfI3o6xOsqbcyhjXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ماستانتاتو بازیکن آرژانتینی رئال‌مادرید قراره به صورت قرضی راهی بنفیکا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102038" target="_blank">📅 02:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102037">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZL6-zjqfe1m7RIDVYmiolp6PzjPyucY0xcTbQvTuJjNOOWuaanCTyTScKZ1J1OpMBXoMulXfGe0z9OLHSO_xzKRXm95YdMyP3a9wbMOSPAUK3OSr2ft-twp8ERkmcCl3zTVXllCcyJtgC9JAF9O7jTVTnxtVHVOaTgEIzQ2_4YixrvhOao2LTfEAEcQzIGO5wIWrROlVOZvBiR3lUIZEqG0KOZmoNuQVOQL_z-PTIiCnfZoSpdFxQZRoj4KzDpi3Od0w-g-vn49o1nhwXjMs1lf3okR5NoP3EjjSXu-hzjteYuKZU2rfCZLCHlioeYzOPxk5K3cDO90Cx-VcA2HHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
جنگ بین خبرنگاران مطرح فوتبال اروپا بالا گرفته به طوری که دیوید اورنشتین گفته پیشنهاد رئال‌مادرید هنوز مورد موافقت لایپزیگ قرار نگرفته و نیاز به زمان داره و به نوعی گفته رومانو فعلا زر مفت زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102037" target="_blank">📅 01:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102036">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/frQ_pnVqbi2FJYon_dYsXMEhASOhR2pKWD-9-KBNFxJmqDj8w_hBHpjrtdDPYtvxbXTRRxmmbBn4AeubpX7h1u59eCGOMxSZy1U4K8wEOcJEVzR3CCTLa8nfquT5Oas85X87rTUfocB-yS53FKy3WU_7_7BlkuEJI7ej9cEDUgrliRyVSDqXfkGV_ZiF-pZ_hjtjwe3VNWjzen5jB22n2Ypb5nMf3DJH3QyQuf_D-xzsbAZV5D90QoXLIQM897o5M_vpNcOc-GMSgWnTcsdwpdJ9yRWUM7lgSdmg0AxT4ztThP0arYZY0Hy3pQmZCfKWjALfN-z3zRF5n3Nt89D6Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو والنتین خبرنگار فوتبال اروپا: ژوزه مورینیو به کاماوینگا گفته که فرصت بازی زیادی در فصل‌آینده نداره و بهتره به فکر تیم دیگه‌ای باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102036" target="_blank">📅 01:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102035">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNjiOmWmadARLrE-reDA1udY3A0Y7EYxLnf271ANuu9ScwQ2pPSFJ-weLmRGES_L9E04_Fw0EfXLUOaWYzOCEGCPQqInSp1oHfl5WJi8yyFywWBh4Gw4DWhNX6jG6mjPI_cDt2yI5MEYY0XJCoKmIYaZ_KfxSh4UDmALIqEANGD4qBblJAPZmElyCcqfLeozypZqTLoj2obOm2fqGDUNBRnIDo0ENvyIFZ4dW017jLu6U9koToLV-r9A3V5r7VxE-X2LLa_OEuIuhsRo14vT24XlvXUQeZVlkIuP8ccU939eeGY1jnvk-xr5W46jd3rtBvCljfuUCjj2TLpb3esqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102035" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102034">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1wfxSpDixJNz0fbYTrnmQjgqieMonMXvEG18_i_Gwrtd0el2SGREgA8r3kj3LxnDhB4WIANch1vTSisVs1i8V3e5FLcxBJV4f5Q1oNH2NgvG0XCbEjUvLBMMYU1eCvSM12yYpK243vyGbX_Tc57_zLYBjCJw5sd5fVPgS1Bj_Dx1NR8U-XXqd_g1-k2gzWL4ZNG1T0lNEKnnqRX5i24YlDefhy502c3oT_sSgngM-8GAooSSAm01U_geD5X9xY3L8tNvLplg9dmXd7-iPIpKZEcalApo15x32rluUWYWOH_VALh-aSr-wH-rF53IavoJyIKP2FS7g5VY5OBenCCPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تلگراف:
مدیرای آرسنال معتقدن وینیسیوس جونیور همون بازیکنیه که میتونن باهاش چمپیونزلیگ بگیرن و هرچی واسش خرج کنن ارزش داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102034" target="_blank">📅 00:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102033">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=dCZ-T5VzxtsTbZ7By1V1guxkLG12Cjqt1-bSLFK-PaGXf2rLbFPqmB4nkq01XdP1ZoXS1EH6droN2ImsEYiBU3r1ee8iCYLCX3t4iN41nCnc9PkyA4GXUWcBdQKOiyjUIWwKQLHHdgO9_Zpgw-KsJKw6iej0zVeAoKX9zGmDYK1D3LKRLHcafx0e2LGJxvGS2wi02bZkP6p_KlKPMGEfqduO98Vt-hpBZ7Q5iaFnnmzjJmwrJl5jbh5K1kr7yJYDmzyslw-dUCA8FGz-jI5twHcNbySmX9Xg_8q94qj7y_zyHAAYYr-lCBY-O9DcFP4brtOk2UFRyOySjaR1E1KXcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=dCZ-T5VzxtsTbZ7By1V1guxkLG12Cjqt1-bSLFK-PaGXf2rLbFPqmB4nkq01XdP1ZoXS1EH6droN2ImsEYiBU3r1ee8iCYLCX3t4iN41nCnc9PkyA4GXUWcBdQKOiyjUIWwKQLHHdgO9_Zpgw-KsJKw6iej0zVeAoKX9zGmDYK1D3LKRLHcafx0e2LGJxvGS2wi02bZkP6p_KlKPMGEfqduO98Vt-hpBZ7Q5iaFnnmzjJmwrJl5jbh5K1kr7yJYDmzyslw-dUCA8FGz-jI5twHcNbySmX9Xg_8q94qj7y_zyHAAYYr-lCBY-O9DcFP4brtOk2UFRyOySjaR1E1KXcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت این‌روزهای لیونل‌مسی در تعطیلات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102033" target="_blank">📅 23:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102032">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0SzL98f-p1xRc9J3ivfPtYtQiv53Depu0QX44KBvUb3UcsQUoN_M6s3LqXmssimPK7Mtou9mjDza-LHUHAHEEBHughAvZY0uVWeB1xiaem-wspzuJ3YmsO9W4Gkb_tIO2iYSu9zxvOLFZQ0WkG2ZO4zbhbNy20XvS6QIcX_L_MIq0rqzu5nf8bjNLO6CNvDBuI-6CwFdywjKk5__i5rTaS55dakYgI5s8rSsd82-f9jKY6NwPqp0BU2BR7uuU6AUQmGEyDpopvhNNnpFfzPDgHPnDcEte6yT_4oFHCohSvzcvb1Z6X7Hz4JMXRe5EPoqk-h6coyIOJroCuLKJyX3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📮
🇮🇹
دیس فلوریان پلتنبرگ به رومانو: بعضیا همیشه میخوان اول باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102032" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102031">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUxIlRX8zuSMpcS1Ajlm6MLt3Q9Pl4QgU30JfZBLev4xpHQzTZWdcMg1x429Si6trJTywi_u-gybyO2kgICr6fexMdYVHQItv8JaXJgRp8smcKy1Y1sLj4UA1Uydvr3jMyaQ7_zhT6iXMhx6o_EMttg6Ujug_VH3kKtPqSZso5Zml1ocN965qQ1gIaHEG-tI1JLCHuR94V1ZAsVT9JNCS_QCiGDGaotTW9zYDFgidFhqx0ZhL3UmMwS6sGNniJTeWLYUzbSf0gTJA_5y9Gx3JNd0glPZK8d-3DXNO9VeYbrwQEquO3HcP8MnoA2hlQsucadjuRC3c5vEqICi70xGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
فلوریان پلتنبرگ اصرار داره که هنوز هیچ توافقی (حتی توافقی اولیه) بین لایپزیگ و رئال مادرید حاصل نشده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102031" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102030">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102030" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102029">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=FRssKzQhuxaVfBREX2ueCtI_hTuAHubwHFgsqOmU0irBXAy8GP7gC9yBuyf80exXTP4XFJbgBjxK7i-XcTtIyWsQeGRn1Kipg7f7ODtnWEQHN_7iVHq1NZOJK9quhTvciT_Nl7b6kyNAuUt7v2R3qw0B1mvHEMzuths57XbLQM_w8Df9bFPJzk2yZb-kXn6Gr3XmLLiFx-ObGM5IQC50pgfE6M2CrMZFQXL0SpwUnFKgGJmYmE3K4CSzZhshdSrJTIc8zaQOlNvnIyVU0Ca7lpVRH_u3Zi4x2_ngl6i62PtH-BPmYpctHcH5JerLnVTm0K0RdwV1w0BMxgjJ8830Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=FRssKzQhuxaVfBREX2ueCtI_hTuAHubwHFgsqOmU0irBXAy8GP7gC9yBuyf80exXTP4XFJbgBjxK7i-XcTtIyWsQeGRn1Kipg7f7ODtnWEQHN_7iVHq1NZOJK9quhTvciT_Nl7b6kyNAuUt7v2R3qw0B1mvHEMzuths57XbLQM_w8Df9bFPJzk2yZb-kXn6Gr3XmLLiFx-ObGM5IQC50pgfE6M2CrMZFQXL0SpwUnFKgGJmYmE3K4CSzZhshdSrJTIc8zaQOlNvnIyVU0Ca7lpVRH_u3Zi4x2_ngl6i62PtH-BPmYpctHcH5JerLnVTm0K0RdwV1w0BMxgjJ8830Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره فوتبال مملکت علی‌آقا دایی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102029" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102028">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY2JFDMzsbW8L6RRvY2qUxmdkdLjQrEcu_-wjNMgoQ-H1EpXmsmMYpOvR04_WdK53Wekoo2HSiWu_IL40Ytkt14rb1zI-6uxs_z6Jcr1qtA-4y31kmE3bk2FF1ePNuBZ5-Exm7EHQ7qkSwdPHSfjqzcKpgI__5l_W4UkFLFErq_sy1ex53eaXhVoUtWFkP2BJonrzR1ZD4DZG_Rm_iAFdMOG5CfVkPLKa2kQtN15iFlqLMxk8-4I7XE8CNt0-c6_bH5EYUwhRElKHJx_BFRzz3D1Dnhn-cvYuxERj3Lx3lJ2hJwBqizJ6r3wgitJ2wJKlmTys0tNICQ8nJSx8Sv-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👀
رومانو:
🔺
خرید دیومانده بیش از 100 میلیون یورو برای رئال مادرید آب خورد.
🔺
مدت قراردادش هم تا سال 2031 هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102028" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102027">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xt_XajTURcDUD5hbNel_ZBCYMlP-EwDCo5PRi3h1LGZ3GtIUQs76eHvaHOFfqim5DExA8NidvudbtcgSK-2r5Uz2Ys3i1XAjihA-4vdunSOZm-WtM5bO8ItpMabUim870jPYACMWDzOa441nMN7vs4fNUdSTiwaQDQsSAC1r5Wgwd0rON_CQktnqL3ntYR5zh96Go0Cx_bze5cpU9DufD33szDjIL74Bkr631d2hY2wYZXooIKcmdBz8r-jIjw8QH5k7g3wNcBKR8eqKJFXfAzWJdIR0NzjRfYYtR8ZFOcknfPansDoEAa3i6t9WPBvwinwPs6riNn05RKyNspTtHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار پرز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102027" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102026">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102026" target="_blank">📅 22:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102025">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tofSIsTrqfLcoSC9EJsV_ErDB-Niej7QCFYN197iX-b_UDhbQ_0GaEyHTfGdXmspPhuqfBVSjzXtOAcpQ3tvSgxsHV_9gmSxH4KMbEgc45Y0ORLL961rswsPb7rabGOBhU7Au8O6xiqAo2pJi42ohX8x1JHQToJwuvS0aZVooVZ1kAiQf5Ntd5bkvjXj5xC8f0Y1yZckWu-aeQTkWhTZapCe1m0a68k1kqJXRp3Gfa1RbYWQ9U3_hzaMXVz3_ePiWb7XERiMgI7NP4uEkWv0JCJd7cihRb8QIDKjB0V-DAUCcKF4-_MS0iT0aBt8DDmbp2MyTxJ3jnnXbz8k65_3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
اسپورت: خولیان الوارز گفته میخواد یه قدم دیگه برای پیوستن به بارسا برداره و بزودی انجامش میده . نهایت تا ۱۰ روز اینده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102025" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102024">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpA1myXDX3jdUpo6PspsHbMq1k-tqiJpN3mGYBmwD3XoPoJAJKQhj1XYjnnVTHMsOvMCo_oXQIJwxiLPDz1gjIFvRdUf8nJ-fjM4OjjPXlSBv3eVgK-lBBLUixBIYGrkfXYC73jihtoF73sBApDjod1oeeU9JTwrzcvFPMq9vJwkjMNb3JjaWT2VDBYFbM-Ydo-8J3xcdqdCs72GyYoPu8yrXfv72Rw0AnW4SVubAUlpcN_OFT05tIRefc_wQo27ZMC7pVrJIxPwbE0qRHH_8P5NdAoGJ-T8lJEYu7W69RQus2pIKL066_CX75Xi4AkFsGKK91VQ8NdEXZTubJGchg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی
از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست.
𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102024" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102023">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=BbDyRDe2uaPqO9h_XTou3bFQrZ4JUgHDPZdBDaTVkPAxalp9waXzT0xoB3CacwpV2XNSQZ9UJqS_azxz7pVDSw7z6R7PjF8EzwuJ7nFK2dUVvsaHbw0SJ7fUA62T08kmED4XHITlmySChw9bx4dVGtWbW_rn6i_jXeq0K91NQhAf6giXZrj9OJ5v-EOqJY4MSyvuqWoWYWcYm3lnE5I3S1I8hLTMqX1Z413MZhqfmSvDpLYWcsr8TBKFMHr6A3fGsWEHppFmFUnMl0FHsjjg0yDCMPyKnr--Mt8aEVVaUBRl44kdYUmoBF-tJtOlUMlQ1wtcw__jh1vk_LgnKWoWYylSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=BbDyRDe2uaPqO9h_XTou3bFQrZ4JUgHDPZdBDaTVkPAxalp9waXzT0xoB3CacwpV2XNSQZ9UJqS_azxz7pVDSw7z6R7PjF8EzwuJ7nFK2dUVvsaHbw0SJ7fUA62T08kmED4XHITlmySChw9bx4dVGtWbW_rn6i_jXeq0K91NQhAf6giXZrj9OJ5v-EOqJY4MSyvuqWoWYWcYm3lnE5I3S1I8hLTMqX1Z413MZhqfmSvDpLYWcsr8TBKFMHr6A3fGsWEHppFmFUnMl0FHsjjg0yDCMPyKnr--Mt8aEVVaUBRl44kdYUmoBF-tJtOlUMlQ1wtcw__jh1vk_LgnKWoWYylSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
آنخل دی‌ماریا: مسی نشون داد که یکی از بهترین‌های تاریخه و تا وقتی که خودش بخواد میتونه همچنان ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102022">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_ita4ixEJYZOJq6yoLCs--evlJZ_dMw23E7cT2kcRVbaeC5U2EtQHUlmSIOkE57bbkwvdBn8wtEaOdkuO2C88fSJHN4AsqTQq2MElKTinqm3R5-AQyWXiwH0eEc-D7DkiX8444cB-0qBTW-PVkxE7w43-FOjgE3RNa33oxn0lAgeBib_FWyRvqp7KgFAtrqiE7VIBCNUUUJqYvTmEe0RG6jPH1kiPGr4JM0c2sDZechUq6IZ9locLS8T_TQ4TlMKQJzXAcbyJ2V0_6cEcXCVfQf5ButoCwHRXB44SGisQqvcHOJvFt2igOvtT55pRdZj4iOXaWdzEnDgn8ueVSAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚪️
عمق اسکواد رئال مادرید برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102022" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102021">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KC-GqpSn9n8otiyt60-JC8T44SBQrJVBimRxUpRw18xz9cV3Zt7pMy3LuzfsarNFbqJBkyK3_Z9-U0I8uawpK6xq-d2eSilQSgS_8zWeN1fRQCt_pEaPpUC19khUOEkNjB5z4Fgbchn00xu_T_Q7RiegBxW-2QNJWsnm3f1tgISlgCNt5vOVzcSDQ7z-oI2ssgunDUJkKBvwRlo_HyEhP-B5Ik_Xwt16Mbug5jZ74vRzcUE3Y4DDHcW2skb5wOv4HUy3RuETqLbV6Z7UtfsXjrz1jWX5IfqyoZVbI41zTjqLajYY4YrD4OdAk-VyjFWyQAhgDXxt3Z0XBGWIVG22F2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KC-GqpSn9n8otiyt60-JC8T44SBQrJVBimRxUpRw18xz9cV3Zt7pMy3LuzfsarNFbqJBkyK3_Z9-U0I8uawpK6xq-d2eSilQSgS_8zWeN1fRQCt_pEaPpUC19khUOEkNjB5z4Fgbchn00xu_T_Q7RiegBxW-2QNJWsnm3f1tgISlgCNt5vOVzcSDQ7z-oI2ssgunDUJkKBvwRlo_HyEhP-B5Ik_Xwt16Mbug5jZ74vRzcUE3Y4DDHcW2skb5wOv4HUy3RuETqLbV6Z7UtfsXjrz1jWX5IfqyoZVbI41zTjqLajYY4YrD4OdAk-VyjFWyQAhgDXxt3Z0XBGWIVG22F2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
امیرحسین صادقی: وحید مرادی من و فرزاد را در هتل المپیک آشتی داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102021" target="_blank">📅 21:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102020">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZD3ijjJ1aTS24mY_Rygmr4WOXMKvks_TS8LiZB1HPwvMrUGGCAIRcE4dK_LydXoB9vqP9JYK0PHYDsBU-FuYI_DVyy06rQVHvkq4EQmeru2oNqjH_jm9fdWfVVKqiFMgGmiQxT7NW0HDrCBwDd7CuoK1jCHGup2wMGjpWlSMuyryOLj4WzhKrybr3oWdz-jXRD4oqH5MWvgizyh5v4JSg58CbLXZRpb-6j6tZj5ZA4wjMRrNKzuU5YLbTWedS9NUeUOtY543W6Dw5YDJrztmpnnEigaO9wFMGUOPhQEM4WRjA-eBFaqq59CTX_r0apZlS5GEPdqwq4Der2bocmcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
پژمان جمشیدی که به تجاوز متهم شده بود، در رای نهایی دادگاه از این اتهام تبرئه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102020" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102019">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPw1aOMjox-UMnzZshTqh9WMW_7YcLHigq86U-jGYCeJuwmqGBzEhcB8DmhQhMQJAlOZOyRAJSDg7y-6N-zHA5fwa8hm8UVHZTsPljXGilaqkkDPCdXgAovtxUeu1Br3ZqXJqF35bVBG7OZqp7CFvVIw62JuwkvQPF9MYK9zTEQjNDvFguJ1jtVNkvbNAXu2pUrSQfB37nEaUET-TL9BDGRJeYZNsT9kfV9P3pjeseHQD4Uny-MTEcBGFKrlx5tdbWtGNl4P9CDnzNpym1mKUDLuZT9v2YcZALJV0xX1Il3cSgYidJ0PmmbDSrQO5lncA7f4ZtH32PAvVGTCFF4r1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
آرانچا رودریگز: انتظار میرود که یان دیوماندی این هفته به تمرینات رئال مادرید بپیوندد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102019" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102018">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHb3DupinzCjKs9RTEj2uFaUU6B86fV0jz-5D2WGqLU7Z1rT6eoGCI-4Dpf-eiaVJeMfRKTQgguYxnZDupNMX_W1Tf9V5l4OAzQBJQbUt6bsiXsNJjAuLHogAZLIFV6vtsSTsfRZqXpGtRU7ZNgskp_u1wolQwJ8W2ly-QcvPGpzMaCVZKgi6Gc0y09BGZA6ogHmK9P9Ui2QLfKFdU7OnLG9EZ-R_JF-NYlIxThsOtPe9iQ1N0Nk103Z9FPhobfkgvtPeu8-FSsdM3IB-8AOJh6p2FgaCWX1p5A24VlDFddhGp2b1YT0Yv9cM7iGkbNkRXJgEhRHD4YBw67eoA_KgtEuY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHb3DupinzCjKs9RTEj2uFaUU6B86fV0jz-5D2WGqLU7Z1rT6eoGCI-4Dpf-eiaVJeMfRKTQgguYxnZDupNMX_W1Tf9V5l4OAzQBJQbUt6bsiXsNJjAuLHogAZLIFV6vtsSTsfRZqXpGtRU7ZNgskp_u1wolQwJ8W2ly-QcvPGpzMaCVZKgi6Gc0y09BGZA6ogHmK9P9Ui2QLfKFdU7OnLG9EZ-R_JF-NYlIxThsOtPe9iQ1N0Nk103Z9FPhobfkgvtPeu8-FSsdM3IB-8AOJh6p2FgaCWX1p5A24VlDFddhGp2b1YT0Yv9cM7iGkbNkRXJgEhRHD4YBw67eoA_KgtEuY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا سوپرگل قیچی‌برگردون ببینیم تا روحمون ارضا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102018" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102016">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/disIQeNdOJg7MHZUyC71gJkw-IapSdHKNQA7-rTZTOQQSKu9G_wfZGDAi6uESJvWHxH31-_4k5ZX4uba45v_N6Rhf0txg6ypDf5j6fktDinaXmnBNAFjbqOlSJpfi33GadOBQpfoUPoTVTE2C-DHW7WEJyzZ11YvejWdSCTv6xDUq0xNpVPZrny9kpIIfJ4PbEdcEJpAA17WEjRNAm3_veFOotF16FnABl6fZM4DmFjb88oTNVEF8A3b__TQ5GcuYCHRQK6FWFOr0y8tQuIG5ih7y87D-9wEqho1fOAZn6yCDl67mUZvoj-k7ZOPLrrgWSjCQEaNiA0M0oCPnRiYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiSM61rNXzVDBm_uDKlBrFmk7_tJl0MRr2HWVR5dT2VzGk5loe0lIPOmJJ1z7q4XJ9cV-2EuzSfSmHXyH-M6B8raGmvoUrRriB3StyCPPy6KSv2DV4SV709MOwyxElcifDwqLF0OYgjRtKGyAoieZWqfeC00ulob5xp2OcFEbhD3yPZFwb7ln73iLe9BI684_DOudqAoxFspmtLAAs6qJyDT1ev6j5Ea1YcNM0nqA4RvUFCoBtHWnMLzjRITedFlV1ONshKhmIFTc5Ct_V07H40OYV7fWcr5E0DplQDf92L5FCi8L333Dbvg8EUc91s_zJKLb0RNJHk6zeIWwdg7CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
لواندوفسکی:
شاید مجبور باشیم ۱۰۰ یا ۲۰۰ سال دیگه صبر کنیم و منتظر بمونیم تا دوباره بازیکنی مثل مسی ببینیم.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102016" target="_blank">📅 19:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102015">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGaumk_K7w6fdIlq76rrHnLn9LhL-UNL70VNkEXLuO0JiK7WGNqjU3uMO07uhSXFb6viZWDVJSjwed1nhy1N_1sAthqQhZyBQjCTnHEm7jpTzLpLgN-W3VpWQEAYg1qfSCX58X1WfrpAsGhl16S_YoASvbIN2k8ngXjidAWTxySq-Sy1IK_KSY-CrBGFQNlIrJWlLqihHv2FcExslHtvcz0SsPR8nhOsrq-StYzJ5ZpcfASgDDtPT9ZjyNgrvCyCf2CSeZxa9wUhhSNYqcMmEAPlG_8LwztaSq3CqznQi7mB54V2EgzBdpfjvpumyNtsGGqBxRVzMJk8WXDZ0twAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
گران‌ترین انتقال‌های تاریخ فوتبال با در نظر گرفتن تورم:
🥇
رونالدو: ۸۰ میلیون پوند → ۲۹۲ میلیون پوند
🥈
ادن هازارد: ۱۵۰ میلیون پوند → ۲۴۵ میلیون پوند
🥉
آلن شیرر: ۱۵ میلیون پوند → ۲۳۸ میلیون پوند
نیکولا آنلکا: ۲۳.۵ میلیون پوند → ۲۲۶ میلیون پوند
فیلیپه کوتینیو: ۱۴۲ میلیون پوند → ۲۱۷ میلیون پوند
پل گاسکوئین: ۵.۵ میلیون پوند → ۱۹۷ میلیون پوند
مارک اوورمارس: ۲۵ میلیون پوند → ۱۹۶ میلیون پوند
گرت بیل: ۸۶ میلیون پوند → ۱۹۲ میلیون پوند
استن کولیمور: ۸.۵ میلیون پوند → ۱۷۹ میلیون پوند
ریو فردیناند: ۳۰ میلیون پوند → ۱۷۵ میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102015" target="_blank">📅 19:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102014">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=qGdI5Tc5W7dCEEp78-c4_BH9LiLoqcflXId0tLsRI0mGwAKmwcKctEbmKcsj53B5svpWCxxie_PzhmRapNza5eox99AxxWyIDIUVt1GQzPevtdhRaG7a-mrDZI3d_7cuEzC7niE2LNG_MWGxWCC_ZiGU0aoEcidTCwAoMN1g0cep0ngGSJJP1PEW9-yg9pen0cgjvw2IWEIp2KA7rZO9_4F01ryLmUglevmknJ2y2M6cZKG8W9ehTeIQ0nPwI7vHLPtKEi33EjYHXFcFSPbjR6Tk3dSPv94Is32WQIiUrUvrYUhBM02hRouxT25-TD7w073jZdKM4YR3rVidj-fbAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=qGdI5Tc5W7dCEEp78-c4_BH9LiLoqcflXId0tLsRI0mGwAKmwcKctEbmKcsj53B5svpWCxxie_PzhmRapNza5eox99AxxWyIDIUVt1GQzPevtdhRaG7a-mrDZI3d_7cuEzC7niE2LNG_MWGxWCC_ZiGU0aoEcidTCwAoMN1g0cep0ngGSJJP1PEW9-yg9pen0cgjvw2IWEIp2KA7rZO9_4F01ryLmUglevmknJ2y2M6cZKG8W9ehTeIQ0nPwI7vHLPtKEi33EjYHXFcFSPbjR6Tk3dSPv94Is32WQIiUrUvrYUhBM02hRouxT25-TD7w073jZdKM4YR3rVidj-fbAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الگوت کیه؟
دیومانده: رونالدو
رونالدو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102014" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102013">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=p2E521Q6bfDkh8ypl__vUmRRuKTmWEMPkt3ocBe9Yd9XPnzmkoUhSDwZgrd6GB2tyUSLWelMJZOqa-UKk2zAxqDuY1P61_YQAdTHDFVXpn-NY5GMDWH_6Uc1HiXDMR6NFxejrScEK5UKBGXDqkrSzPduONfS5t2NeUCR7qBcKuoT6RJ1YxiPQgCP6xJzdF8JIyFf6ap2krprvByL8th53QunbVBuFRzr-M46il-FIYhYBuhNqo_-OgwO0h5eFgBC2w-Z2S76EgqBru9a5fhIHLBEAg6Yuyrh-dBnd5xReUIY0R4BzJswD538jqmuyhye_8cWQJCcf5VgPelBAaNPAVtb4iE2nBpKm5jVNye_8DkS00RhyWREM_NrhSMi8hh-Tg6IWx27BcFZSyg5fc6nkK7y8HDuF3xgiS_emn-MIG08eAn0Mk1EASNKYcEgD8RQWtDBbtaqsSRBVX6Oh_efL7mIIRZ-NMKlflzwPuA4-TZ7LBIo0b4EzP_EigRrFpMaJuU9OrC2q05LXeyelR3C9zUhGe8ndce-9HTNVLv4d8jIumqiPbvF6MxE5QCPsJxqnCbDsDB1mPu_XQO5V7CZ3LL_tvSLL4e7TYuhIEzxP8fNMk58TJXx80sLG89xWFrD93oBwnDZpwnhYy9OwKCsMb3IGQBL5nX6IKtqZAAhLmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=p2E521Q6bfDkh8ypl__vUmRRuKTmWEMPkt3ocBe9Yd9XPnzmkoUhSDwZgrd6GB2tyUSLWelMJZOqa-UKk2zAxqDuY1P61_YQAdTHDFVXpn-NY5GMDWH_6Uc1HiXDMR6NFxejrScEK5UKBGXDqkrSzPduONfS5t2NeUCR7qBcKuoT6RJ1YxiPQgCP6xJzdF8JIyFf6ap2krprvByL8th53QunbVBuFRzr-M46il-FIYhYBuhNqo_-OgwO0h5eFgBC2w-Z2S76EgqBru9a5fhIHLBEAg6Yuyrh-dBnd5xReUIY0R4BzJswD538jqmuyhye_8cWQJCcf5VgPelBAaNPAVtb4iE2nBpKm5jVNye_8DkS00RhyWREM_NrhSMi8hh-Tg6IWx27BcFZSyg5fc6nkK7y8HDuF3xgiS_emn-MIG08eAn0Mk1EASNKYcEgD8RQWtDBbtaqsSRBVX6Oh_efL7mIIRZ-NMKlflzwPuA4-TZ7LBIo0b4EzP_EigRrFpMaJuU9OrC2q05LXeyelR3C9zUhGe8ndce-9HTNVLv4d8jIumqiPbvF6MxE5QCPsJxqnCbDsDB1mPu_XQO5V7CZ3LL_tvSLL4e7TYuhIEzxP8fNMk58TJXx80sLG89xWFrD93oBwnDZpwnhYy9OwKCsMb3IGQBL5nX6IKtqZAAhLmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگر قصد دارید سفر اربعین را با اتوبوس راهی مرز شوید، پیدا کردن بلیت را به سپاس بسپارید
🔹
سامانه پایش آنلاین سفر (سپاس) با اتصال به همه درگاه‌های رسمی فروش اینترنتی بلیت اتوبوس امکان مشاهده و مقایسه ظرفیت‌ها را در یک سامانه فراهم کرده است تا سریع‌تر و آسان‌تر بلیت مناسب سفر خود را پیدا کنید.
🔹
از ۲۷ تیر پیش‌فروش بلیت سفرهای اربعین آغاز شده است. برای برنامه‌ریزی آسان‌تر سفر به سامانه سپاس مراجعه کنید:
🔗
sepas.rmto.ir
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102013" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102012">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102012" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102011">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCUjXKE_6QSCWDkO5tZ_u1_scJEimc7zdcjulMuLpXlFqhUvxaxyoNiJfFCZob7uJg7qK4LGYIBCAVmpSa3GwpuHnwhzBVCdnHFVYv6F_A5_uiN5ZOG8VrCscwq-QEX330_UiBPKJanuO8AobDNUlSIkVvPDdxakwGYKBRKzIH4rCvL-4KlFvGDxBhpylUJusIfiXacSjiQuskwOmxJExlZmZI_z3bp1iSTpfU6ZMt0WZ6lRYU4KBWXNMKPmn-eQHaYSR-q7u3AUnDAA-akMQfL1ThJyjGMAJbEfqx44FpWYLecCIRXYD8E9rDg1alqiZFN10zrI-U-Xa6t5F1rgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102011" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102010">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746abba13b.mp4?token=mqYdcIYIzVyM9bDqsdKHcKy_xjiGNA7B_L5y_PpEEshQsO6F2aB_Gy7aLImwU0QDoXJy00e8DPqtXuLIF9ZgLcjWojmAMebyEWKrp4lN3UdNP33b3i1Ky-tEFBP0tl5DSVJZKdrl5nXxrIIm-Yr6JrTX_oal_YOji5Bn3m1b_U3Ov8iJ9oj0hY40NiS3nL7ZY8922BnY4k2HRnKlZz1eJbx2koxerZ9hYF2w7YGakhhk6MKWvH7bSTt6fwrldsVnfao0lDmARpmLRLvOJqOa8RhXKrrNdBWEJq1NWalGar5YsSeYTCnJ7OfbRcSUhsnWFtsroakwfH1f-TeAlGXY0kGiVdNHGYr_uHyUkfN0VmJtZSa-3ZdZ2bcvNilky1kx-pWIPxMjkan_Zd_KI3A58bBcwZxWZ9P8oK7QjcDp82-s5b_j1mnd4MOrGtnaXbzYV6FCZOj-E3eavlnkovqOV0apEquP-2t5XAmBErCB2VzeV2eH8lGCeWym3oGjVpb2d0X02sspiA_1xwaypu50f_s66BAb2cuEHWqcI-1v9ra1qqv310j8DJfwdfDdMGS0IEXX0S5KrXjGCzJve3xa31LPKajVab5wNtFXdYJ0sCJL9zzEAcnyETcWMrxw6LyMs6X5OHhhnWJmJ-OisZy1M73sWzMMO78T7FLdFA50Z5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746abba13b.mp4?token=mqYdcIYIzVyM9bDqsdKHcKy_xjiGNA7B_L5y_PpEEshQsO6F2aB_Gy7aLImwU0QDoXJy00e8DPqtXuLIF9ZgLcjWojmAMebyEWKrp4lN3UdNP33b3i1Ky-tEFBP0tl5DSVJZKdrl5nXxrIIm-Yr6JrTX_oal_YOji5Bn3m1b_U3Ov8iJ9oj0hY40NiS3nL7ZY8922BnY4k2HRnKlZz1eJbx2koxerZ9hYF2w7YGakhhk6MKWvH7bSTt6fwrldsVnfao0lDmARpmLRLvOJqOa8RhXKrrNdBWEJq1NWalGar5YsSeYTCnJ7OfbRcSUhsnWFtsroakwfH1f-TeAlGXY0kGiVdNHGYr_uHyUkfN0VmJtZSa-3ZdZ2bcvNilky1kx-pWIPxMjkan_Zd_KI3A58bBcwZxWZ9P8oK7QjcDp82-s5b_j1mnd4MOrGtnaXbzYV6FCZOj-E3eavlnkovqOV0apEquP-2t5XAmBErCB2VzeV2eH8lGCeWym3oGjVpb2d0X02sspiA_1xwaypu50f_s66BAb2cuEHWqcI-1v9ra1qqv310j8DJfwdfDdMGS0IEXX0S5KrXjGCzJve3xa31LPKajVab5wNtFXdYJ0sCJL9zzEAcnyETcWMrxw6LyMs6X5OHhhnWJmJ-OisZy1M73sWzMMO78T7FLdFA50Z5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال تبدیل به یک فیلم و اثر هنری میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102010" target="_blank">📅 19:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102009">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIJgcZvLa0gMwKEiZAkvr1tMRnw1Ltcr_u4hwmDGtYL65hCHatdAshi1vS5X4ttHwW4I7nkuPZ2wMR6VDipfn3x-S4F-Ynv3Sp4O3WJbHCclm_7_VFXuCa8AQENUmSOSHqH8IILfBh5bGveaa1E6ItjE1iNhRQo-9M-9k-fKjsqEC7qO0UlPEKn1gihBHdOq7X91s-LJ77QEw68WvWfdjTui3aZw3XVMcz0YIdoIgDC7bKddCXUX_OAxvGoOBdNLlupsQD2Ervj9FScK4eBO2UDJZJId9lxTB1xndfXX5sOvS0gr0L0QGFKbMn-HGV_YDcEu1F83iZPXCTaMvRhCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
اشرف بن عیاد:
کار تمامه، مدیرای بارسا متوجه شدن که موضع اتلتیکو برای فروش آلوارز تغییر نمیکنه و نمیفروشنش، حالا بارسا منتظر واکنش آلوارزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102009" target="_blank">📅 18:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102007">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZY2DMqis11xS3DKmeVF67eeAO8YO0jaYLXa2MdWVaGfL0bF10-KOV2zFWnKBlKZ4CzWCLWyMSR9ex2uU2jh8_7n1gibvkzqNBo5wc0cwmLwiPuTduPeaX2MmM-y-F5Eecv32RvZV_TJpVf4dIECdEgiw3dZGg2_H3hYh8eHq7XS58pHUcv2WhN4krxIi51RuM73TUe-fI8olG10VypwrmIlbX3xQHT0Ls8GRFMeL83XGQI6LuTzP-FeT5JE4JnhNObmUj22X2H45h67dI-unhuc5fKvTE8nDKNVCTnb_Z3pXpeTbhK4awVJMnvqhqoyXwUGeAqca86u8abDcSKx1fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmLDLWxdx3JUdOAHxkMkVAzYi699Q-Gsvi2-FAIaL9Bmc5dsNj5-RlSG5Rim8cAO5kKO4UzOQ-EcgW3auMuuW8O_P76f8QyFyU18u7CXdeyqOQHiciCtlrNpw5kip88Fnc0_Sa9vxwryd2pmluw146fLZDIcVVDrbBUa_eKa76nSi6ZkuB2QOowfIc0x3mQPJm5pF6QP54FOWejghV1loT5ll2CPhG7e7nmtkNCLaySSjD2tiodMhCdZNnmNxyOi10s4LHGg-zmL-rxFH8R3_ql-nf_mR3G7tVTpVFMwAZYQHLLy0spljlKl0hSlAcr6HGJhC9WggLBUwvKQGPBCGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های وینیسیوس جونیور:
• 2021 —
🇧🇷
ماریا جولیا مازالی
• 2022 —
🇪🇸
اِستر اکسپوزیتو
• 2023 —
🇧🇷
لورنا ماریا
• 2024 —
🇧🇷
جولیا رودریگز
• 2025 —
🇧🇷
ویرجینیا فونسکا
• 2026 —
🇧🇷
ویرجینیا فونسکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102007" target="_blank">📅 18:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102006">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=Jo6T3pe_RQQjMtQ7JzYwwhHuJH6cpbJd97DHtsrXu8q6ADjkdI6sZLrFDyZv9CnKsXCDyKosXrYDjqSM1s4wYgcpIuu2iVi37pRbR58638_OhRMT-sQZiSTZ6fCZ597iNQs6xmaaO3A7e2vfXsrXDy8P1p_NFkXOOEPMXvLvrAykiN8vVbT4L5dxm2kZQTNDv8n9At6oEwD9ZKEV-Wqj2WCTUMs0dT_ApYG1I3ZO1yFHa6nXjQ3HCrqzUtyyxiFUGWyT1gHqWHfuHvSrqr4VEEncpOV0K4hlOncdvTjMarlxjhozjEoiW8YYUhU5LLw6tOoviFdielOJSgNjF_Ha2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=Jo6T3pe_RQQjMtQ7JzYwwhHuJH6cpbJd97DHtsrXu8q6ADjkdI6sZLrFDyZv9CnKsXCDyKosXrYDjqSM1s4wYgcpIuu2iVi37pRbR58638_OhRMT-sQZiSTZ6fCZ597iNQs6xmaaO3A7e2vfXsrXDy8P1p_NFkXOOEPMXvLvrAykiN8vVbT4L5dxm2kZQTNDv8n9At6oEwD9ZKEV-Wqj2WCTUMs0dT_ApYG1I3ZO1yFHa6nXjQ3HCrqzUtyyxiFUGWyT1gHqWHfuHvSrqr4VEEncpOV0K4hlOncdvTjMarlxjhozjEoiW8YYUhU5LLw6tOoviFdielOJSgNjF_Ha2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خشونت بی‌سابقه در لیگ‌فوتسال بانوان برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102006" target="_blank">📅 18:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLZEjrbjYXDs65sHL-Vq5gNHATZwsOorviY5zUBz621DL_sFspkemVCl87P2RBGP0kdSzr-izNSfUsrINA_NV81LaLLwDVVRugT2_SCpBhjPmSF6Zzsqh3GkbjxAR3O2QRoLIL_xMfCpCsCUFMyA-kyoobPgxBmuoPVAy70U7Z2VMo8PKVm8Rk448Tw2Q1LQWkXBsKRRnxLnJHqGTpZCJsOfx76g9Ap_4foUj4qBn8KjaQu0-PULisEWOyJ8u4yy2QsRARsgBjRs7h9Is-hpjUTAU4tygVCdwbDn9RJHwaLNfy5JuOisAbLtqIwQ5y0HonT6FH19Y6aiJbl0tUjsOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇪🇸
رقبای احتمالی رئال‌مادرید در سید یک UCL که با دو تیم از این تیم‌های در تصویر بازی میکنه
🇮🇹
اینتر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇩🇪
بایرن‌مونیخ
🇫🇷
پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw6A3W5ftWWNPz0w47eaJqUR05u71KxD8-FJSyOcxOzK-K_uq-aEtica3m_vclMXzJ7USRv5cS-71n27pWdAACFajSDh_8FIHgt0r655zFjZhs1iAlb_NBHKffFfzIE19Zc7N3Smk05vVQ-bszcQSs3qOGf3OcMt3U9NbTSZGHN-epDpYMFJiE0tPU082ygwkGnhdZq7DPIn5eHV431GljCc3AlilyU9cj0MaBJFOfCTx-fjA90z0U_1wHr4jjlU9Jn8NyhkYtvgBUNe105X-Oax273MEC-zWOU94x7j126PYvxKXk7UGwF68KJn_LCkuewcyk9GD7SYLmn2aPmNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmNT9Hn7o_yCZrqnFxvXqhteA92zCHf5r13mndhaBkC_y-xqbuuKVbkrVWSzd4K-ivt2Tl9IvqjxNXJbmpX4C14yrQdxPley-9hp7xZ0Ps0BUy-XkP0Y-gqdguuhtyHSX5vq1LvG4cX13x3pDBcfXnBZGZZ4YGQ-cmP5P4gjmJ1SuF6Le45XUeX2QZXgCfjmj6qYZobw5G3YND4XUFaWONHoWGXeH1cylAiUQCH4uWYJhXZo6kCnzZ9hdFNBiYNm7i1GfQhPtgVxFC5YYQaGASF0ozNwr9ttCj0m6qsRvpApFKBYsk_GzXeptE1uJn7RLMNXXgv_WVdxnYD4jo_WYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=PwvMlyTbG4qQObJus6uOcEQEvAOlOSmpPSQejVr6MF6j5YMDbyakY6_KAacFBUEoFTp495UfFOqe6u0Y2Za6_zj4z0OB-tugPiNfipKlqzPAmenPLHBoplHiLa9VeGP6phPQnGOd_Bxwl9uqPCh57vxURR-W9XUY4QMV-kBxanL-aczNzmlbQDRu-ZTI6wlKW15rbJbJOMXfH0Eam5uVygDkQfbHjIWIaSXThzYq7p3_fviRCEPeWfNgbDqYGHDKUO3k8_Sc0tsoaPWK3DwT7v7FRDG39TxCB1MFmd1xtOrgxCWWkXIeJEE4zOcJw-mebo9UHCcIHP17OYWtV2UZ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=PwvMlyTbG4qQObJus6uOcEQEvAOlOSmpPSQejVr6MF6j5YMDbyakY6_KAacFBUEoFTp495UfFOqe6u0Y2Za6_zj4z0OB-tugPiNfipKlqzPAmenPLHBoplHiLa9VeGP6phPQnGOd_Bxwl9uqPCh57vxURR-W9XUY4QMV-kBxanL-aczNzmlbQDRu-ZTI6wlKW15rbJbJOMXfH0Eam5uVygDkQfbHjIWIaSXThzYq7p3_fviRCEPeWfNgbDqYGHDKUO3k8_Sc0tsoaPWK3DwT7v7FRDG39TxCB1MFmd1xtOrgxCWWkXIeJEE4zOcJw-mebo9UHCcIHP17OYWtV2UZ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آنتونی جاشوا، قهرمان سابق بوکس سنگین وزن جهان، از آهنگ سیاوش قمیشی برای آهنگ ورود خودش استفاده کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=ZLZO28Dh3zeU9draEWyYp1uZJPykZJrJVRu045gh6ghKeErjQHmNf4f0dvLJS2kbHBXR9Pj7i_FuFZ7LLnWkdGXQzz7WY-FUF8II6GxVEI4afFhBhjk5qWkbT-LrXVz7G-s5e0M_e5VyATrnqz31jy-yb1jPNS-Xkfx9UX1UQfZ8LKPzGN4GxR-8fZGm_YLJcF_-Cv3M-1QR6_790x0Tm40wiP3-F4_9U2vhtY3UjPcSG5DbeDAdl6Y6-zw54uPgcj5-7n6_f12ep_5FO1cluierFyWs2ojUaWw_FFdFlj5RxjlTNmS9YtDb0YxXKLiK9PSW76LlWL6LzwIv2qa5kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=ZLZO28Dh3zeU9draEWyYp1uZJPykZJrJVRu045gh6ghKeErjQHmNf4f0dvLJS2kbHBXR9Pj7i_FuFZ7LLnWkdGXQzz7WY-FUF8II6GxVEI4afFhBhjk5qWkbT-LrXVz7G-s5e0M_e5VyATrnqz31jy-yb1jPNS-Xkfx9UX1UQfZ8LKPzGN4GxR-8fZGm_YLJcF_-Cv3M-1QR6_790x0Tm40wiP3-F4_9U2vhtY3UjPcSG5DbeDAdl6Y6-zw54uPgcj5-7n6_f12ep_5FO1cluierFyWs2ojUaWw_FFdFlj5RxjlTNmS9YtDb0YxXKLiK9PSW76LlWL6LzwIv2qa5kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
قلنج‌گیر معروف ایرانی که با درودافای مملکت ویدیو میگرفت توسط پلیس بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101998">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=a5vx3SOS8krd1wca2a6p6iqRz_orx78s99w_4V-XMxypEiul96mkv4hkteMFze2IEZyM5LwnMR70kJjyCE8uyMf_uW_lVoCsMqUfYcYELHq4XMrWnX8UYA7pGmk-mXmevYCftIZt_4B-rkrVquBFsvfSxpChGMy7tm9IiDa6R6FrAkFwj3lqbCA31wAgI32mDi4y6pwVQ3HoOzR-LSqu8x1M5OJPQvXjCQEJcZ01pRx-tOigaSIMpP6lMDUmD7dv9NyZ7tn3LoKtQpcnkApGmWUfiqdbOPFDKGpn57xMuuIiPcH-dGyW5eEr1uTHOjDyofsp7Zj8d6fgYfEPVA5ZlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=a5vx3SOS8krd1wca2a6p6iqRz_orx78s99w_4V-XMxypEiul96mkv4hkteMFze2IEZyM5LwnMR70kJjyCE8uyMf_uW_lVoCsMqUfYcYELHq4XMrWnX8UYA7pGmk-mXmevYCftIZt_4B-rkrVquBFsvfSxpChGMy7tm9IiDa6R6FrAkFwj3lqbCA31wAgI32mDi4y6pwVQ3HoOzR-LSqu8x1M5OJPQvXjCQEJcZ01pRx-tOigaSIMpP6lMDUmD7dv9NyZ7tn3LoKtQpcnkApGmWUfiqdbOPFDKGpn57xMuuIiPcH-dGyW5eEr1uTHOjDyofsp7Zj8d6fgYfEPVA5ZlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
اسلحه به دست منتظر آمریکایی‌ها
صداوسیما: مردم بندر جاسک به صورت خودش با اسلحه در ساحل قدم میزنند و در انتظار ورود نیروهای آمریکایی هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101998" target="_blank">📅 16:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101997">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5IIOOZMqGArxmlyddT8b9KFJWSfSMotBFQ4ZyvOzEkC7KZ8a0J6cgjwNJz0dAKftJimRL05lIkroCWDr7FL2WthtyVt9yqGAonA9vPI5l3y5jmQnGQJ_EBOVqIiyJ85RX166CBkuuNrj1U0QwzJuopYLylVs29qHhFmyQU6EtsYNnH0A-XuFQf1uSXIP-cAFD4vyYYfsQTrEZVJFzvPw7TNgJ8PLMndL8jjghiDAgYBU1LQj4frXZY01Etj28hKjMQT09rUChtNiDPrZfKF1a2i8S6ESuWnJyY1n1jTldxeY3i97bcJGcbaYXS_OWW7wYoZaX9kIGa8xzZYtAaruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنانی که با همسر یا پارتنر هم‌تیمی‌هاشون وارد رابطه شدن:
🇦🇷
مائورو ایکاردی و همسر مکسی لوپز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری و دوست‌دختر وین بریج
🇩🇪
مسوت اوزیل و دوست‌دختر کریستیان لِل
😀
تیبو کورتوا و دوست‌دختر کوین دی‌بروینه
👀
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101997" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101996">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=j84v1O1-5UDA9SmmLlr2ESJgYR8G0Gj27Jp60Qd8P2vz7iUm6SvvWnsG1vLHR2Zj2LIWcWvw5pWWpjh_cS8ZygSeLZlwUwC16ocSqpv01f74RxdIEBb6Xpht88O_AsDH6G9HzV7Vm3F_W4PRCkvH0dfcGsOocTSSjs6XTBXcRK9vnzDR4T_hIpvtx5WEv8KeCq1l5Fpa33NsC7OZQ7zZIgw2wDFtAONXareylLAMB2WxSEnPfNvZ_QeZ99RlDkpbA6OQfIm5Nk5f0xT1Ku0s1b4uU-HmuAciPEAYpm56CeXqpZbsxSpGnbODLUo3rwUjPVCx9MXEp6p6SFFBb5_Ukg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=j84v1O1-5UDA9SmmLlr2ESJgYR8G0Gj27Jp60Qd8P2vz7iUm6SvvWnsG1vLHR2Zj2LIWcWvw5pWWpjh_cS8ZygSeLZlwUwC16ocSqpv01f74RxdIEBb6Xpht88O_AsDH6G9HzV7Vm3F_W4PRCkvH0dfcGsOocTSSjs6XTBXcRK9vnzDR4T_hIpvtx5WEv8KeCq1l5Fpa33NsC7OZQ7zZIgw2wDFtAONXareylLAMB2WxSEnPfNvZ_QeZ99RlDkpbA6OQfIm5Nk5f0xT1Ku0s1b4uU-HmuAciPEAYpm56CeXqpZbsxSpGnbODLUo3rwUjPVCx9MXEp6p6SFFBb5_Ukg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
علی علیپور: حتی خود پرتغالی‌ها هم کیروش رو گردن نمی‌گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101996" target="_blank">📅 15:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101995">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4Qi7qBDCosFh9mQDSgLEVG46ZPfLyniBSxV65GvYdqKrYVlZodmwuGgBeTPXiJVCn0ri9EOoi5K-k--esPw92VlU9sc2CiuV_3GDSW5AkPhapy6lUHDnjiASwz54vi72m3gfyjQmt90JLF11ZCpcFBjjkiUtIIJo-VpqohctZjzUzq-apegTfuZ-9YuDYDfscbX4BFPx0b5-6kXtQuKx8y4oJiCyrP0eG7svtAHx1ffWXJ3iXDOZPm60_zlHElIj-n8PlnP3XW6jdjSj2DKzOcojZ3wMN0tUfwPa5RvoMg_kU4jGiPNHlYdE_6goDRFC994heCZnff43_0wB6ItGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📉
می‌دونستید؟ فقط چند هفته قبل از جام جهانی، اینس گارسیا، دوست‌دختر لامین یامال، حدود
۲۵ هزار
فالوور در اینستاگرام داشت. از زمانی که با لامین وارد رابطه شده، تعداد دنبال‌کننده‌هایش به
۴ میلیون نفر
رسیده است. فقط در روز فینال جام جهانی هم حدود
۱.۵ میلیون
فالوور به دست آورد. همین رشد انفجاری باعث شده چندین برند بزرگ برای همکاری تبلیغاتی سراغش بروند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101995" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101994">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🔴
فوری از رومانو: لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101994" target="_blank">📅 15:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101993">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZnE2pk8xWfK8kaX1EUhJxXjaFdzzCvaXZhWlo7UrULxUEoPd3XMxlMYXw7DPjqH0yryv1HPIsJY8DTbzJ4eH4VLz8tSZVjIbcFFswFIEW5ngY_44KuS45pz9qkPCPjfiU-V292VaxQL_qqT5yP7WnjONzyJWtqlaH0o_Emtf5Hk-wXGYj__oTVbdq3ufOzBm8r_mFsOvEtSvgsexVmoRFEBi2EW-f-NNIzQqRSwRkV751EQsDG_cZK9aIWD2sY-jI_BQNmxzqxmmEMmV4qoFnRK_Mo8IOiLS-TaHV9-BnqlGWa2PmShTBULP-ruFNiGkBE-dSesgKnLQ3I6k7jLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از رومانو:
لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101993" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101992">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=nOt9HE8_j-dCfA7-t6XFGNN3YqhfReK_0uYWCuGShgrnRSblzaWRlrA0Jb9l_bvyKBJ5i-ssyN14m48gLPjV39O6nCmzW-k5jFcTGGNYFVcR2Zx7qpREGpz-kWE4nh_BdBXpAkdZzhgEzgzrHxcaOg4JwD9fUzLwZ0e4Mew9Ytw1k3nKWKXBbrgVtAGTiizO91b6za0ikzTkL00NRrlJftHn6DsrCt3DaPhfJP6ZDUfSrAjYQ5Oi-KFScQ-X4sb7HZjIMuRE8PxXOhlDKpGkw1XzgCN7C0v2IUJ3UdG-RFjsdfnA3GRJcZMAUUV4mGi5-W7agGLV9RMuyU_LhDjs57aPEVqATYOzz0rFZm4eQV7Viw9fNA8rBCPou3bfTpYDlJu8OaKACQ_O8eUKiY4ptik_Glq2ZcwloTPcDIGJ-cgvimUZDXAarKb3664XR3u5UX2__eeBEFMLwcdTEHM6lYi8JB_tBw0FpC7tBDnefcCGQQ6rX47V1m4e0Ybkk-irXzKzorB76Zk7h4p-R7F3j8T8JMPbC6dmfOMhXVMnQYXE5PO9tAVJWpBgbQkkBSeqDdbaaWa2CpN10NJNOfskIb7ayW5_DPxgyKAypxcsreI0EHeXbsG9G6eG8It2Lg28-xH-MTbQFJye3Wv6buSHGhuBkJ2R064u_qnPUPkP0ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=nOt9HE8_j-dCfA7-t6XFGNN3YqhfReK_0uYWCuGShgrnRSblzaWRlrA0Jb9l_bvyKBJ5i-ssyN14m48gLPjV39O6nCmzW-k5jFcTGGNYFVcR2Zx7qpREGpz-kWE4nh_BdBXpAkdZzhgEzgzrHxcaOg4JwD9fUzLwZ0e4Mew9Ytw1k3nKWKXBbrgVtAGTiizO91b6za0ikzTkL00NRrlJftHn6DsrCt3DaPhfJP6ZDUfSrAjYQ5Oi-KFScQ-X4sb7HZjIMuRE8PxXOhlDKpGkw1XzgCN7C0v2IUJ3UdG-RFjsdfnA3GRJcZMAUUV4mGi5-W7agGLV9RMuyU_LhDjs57aPEVqATYOzz0rFZm4eQV7Viw9fNA8rBCPou3bfTpYDlJu8OaKACQ_O8eUKiY4ptik_Glq2ZcwloTPcDIGJ-cgvimUZDXAarKb3664XR3u5UX2__eeBEFMLwcdTEHM6lYi8JB_tBw0FpC7tBDnefcCGQQ6rX47V1m4e0Ybkk-irXzKzorB76Zk7h4p-R7F3j8T8JMPbC6dmfOMhXVMnQYXE5PO9tAVJWpBgbQkkBSeqDdbaaWa2CpN10NJNOfskIb7ayW5_DPxgyKAypxcsreI0EHeXbsG9G6eG8It2Lg28-xH-MTbQFJye3Wv6buSHGhuBkJ2R064u_qnPUPkP0ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات خنده‌دار از زنده‌یاد اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101992" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101991">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=FXYI7_tmlqJBrExpVONBbqeBeGGLQE8cZVSl-9EyJ3VvB1B5AYscaveq8IF_2C5uXV2iGjmnUJoVBmuiWf7ujJBZwdkMrd3DzjOKXyeM0ke1tPCqXAipKSCF-pKP1mPK2fOf0rxy8cyMTLxCdZ8N9wUjH3zmDS6ti-54sYeMlNOhzfjRp0_rDPpuIJ-jgl0FBDRC7vn7j1_-7AwFh5Ed70oV4BJtPQcHt95GJog3qN0Aq6Q66lqdqcZAhAN5DP39IZv83EUQPMkRZcfSj8PRmWs5rk5gdjABulRk3nA4xBKL0fneTvrTH2_FPH0BrxF1VQzVPXjIQTLmqRhfD60lgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=FXYI7_tmlqJBrExpVONBbqeBeGGLQE8cZVSl-9EyJ3VvB1B5AYscaveq8IF_2C5uXV2iGjmnUJoVBmuiWf7ujJBZwdkMrd3DzjOKXyeM0ke1tPCqXAipKSCF-pKP1mPK2fOf0rxy8cyMTLxCdZ8N9wUjH3zmDS6ti-54sYeMlNOhzfjRp0_rDPpuIJ-jgl0FBDRC7vn7j1_-7AwFh5Ed70oV4BJtPQcHt95GJog3qN0Aq6Q66lqdqcZAhAN5DP39IZv83EUQPMkRZcfSj8PRmWs5rk5gdjABulRk3nA4xBKL0fneTvrTH2_FPH0BrxF1VQzVPXjIQTLmqRhfD60lgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دستاورد دیگه تیم‌ملی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101991" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101989">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPlwMsRqVNeBTMDT2A3yc9j3X4ZE1YIZXwrp9GokZgfi9BM_Ygl3A0RDARRA3n3apbMkoQZpwueO9JTOJEJRkasZ2e4f20PiIL9LfFcCIqHwxRCgacy65P7wp_K9WnalUyA-7DI4QDPPPVe5CePQE6NGyV_ZHcLWReqVylmLTjYVTcmFhhLMR3Rbu0TDeR5iC0XtxMa3XI1weai7nuBcuL4GvUc6oXyNnfP7q31VOzoF91hMZJGoHPJqFBEvyTLcZ50b151RUgNJIwMvmJhU6ygo4o2rP3mluesqi_OP5qgErnUAnTEspnIdcfguKHrJF6i3HxxdHAdY8FJpDo4qtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGA_jezv4vipmckUzCKPoZPRMIlaggerESym9tsewcirkp-pxL4-YIkkcD2aFl2vNDFniF_owAa9IjRMXSr6NTQlDc5T2tXc7-9tDTcn6cmoy3QRnWBUmsVJ1fKnCjUsm7xUIY5rBboN6UFhoLrRT5FUD3QjnGb7rvBRHwU2zg5A6_njwO0vWdX7QQ-ut9-TMMKGNOmWvIW5hyRXF_pxRpmNz6PWaV5k-j94i382AKiHq4N8Le9JdHPe728ZC4MgGISEMSJKYlN46-nxXTy_oka208JhUzitHbGoiJAJY1nukIcEAOn1h6j8SMWp7ne8-KUdW61kfc2wixO_VfpUBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اینس گارسیا، دوست‌دختر جدید لامین یامال به این موضوع که گفته میشد باعث جدایی او و نیکی نیکول شده، واکنش نشون داد:
من به کسی آسیب نمیزنم، چیزی رو از دست کسی نگرفته‌ام؛ فقط دارم زندگی خودمو میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101989" target="_blank">📅 14:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101988">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=NtEw0A_n6NzsC0rTGYdBl-9m6Sofot9v9UhbLr2ZIJTOdLzBYvysAfNYYshp7CNVfruExx0TNdIjnNHQv4cHwLuQOnIBsEr9ccJY9Wn7qXW136uh4Rk4j-WTuWFj_v_OnOyT4U577f3lJpwwiUkfHmzpULwP30vmaR70tpJ7Xo8CDI9wXyBkdT_0xc7rSouX8AXGp_qIsYifq_nWQTVDeUnssxSywhpJO05U5Fir272c4UX8cLPT_nrloWZog4UPI3we8oU_Nloq1q-KOqQ8HI-wfLESGo6MrMpZOOCtHGwruYxKIIoAjuP2wsYdlkKACg5B3zX4D1hLGzyrQG0dsqtNlqtmNcZAerBpS2YiiNdHXfEcQPoEyVgOhjf5aDWqkn9pFuvHxkANAHY1eKcz2yKvQPpg2XP5LyAoWSUXViH9LMs68t9xdfgqe3zRT2HcrR5Qa1-RogIDY_7l0QcYgzR5elqVrwaHgraviEnNTnDYuMlPFoNN8IOgrxqrlz7NJR_b0NVbxVrP6JeP_QvAzs3r4GKye0IP72mEgSXOPVQaOFouo6mZaUeuw180Dd84j7rwpxtmRfPI7jmhS7fxgM2Ldrc20fuDnyhhqChe0-2ZewQVCPs-qnilsftZtqmWtfmbbu-zpWTjPp-rGy9F1TJimBuvYDrBeXwFiBP4FaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=NtEw0A_n6NzsC0rTGYdBl-9m6Sofot9v9UhbLr2ZIJTOdLzBYvysAfNYYshp7CNVfruExx0TNdIjnNHQv4cHwLuQOnIBsEr9ccJY9Wn7qXW136uh4Rk4j-WTuWFj_v_OnOyT4U577f3lJpwwiUkfHmzpULwP30vmaR70tpJ7Xo8CDI9wXyBkdT_0xc7rSouX8AXGp_qIsYifq_nWQTVDeUnssxSywhpJO05U5Fir272c4UX8cLPT_nrloWZog4UPI3we8oU_Nloq1q-KOqQ8HI-wfLESGo6MrMpZOOCtHGwruYxKIIoAjuP2wsYdlkKACg5B3zX4D1hLGzyrQG0dsqtNlqtmNcZAerBpS2YiiNdHXfEcQPoEyVgOhjf5aDWqkn9pFuvHxkANAHY1eKcz2yKvQPpg2XP5LyAoWSUXViH9LMs68t9xdfgqe3zRT2HcrR5Qa1-RogIDY_7l0QcYgzR5elqVrwaHgraviEnNTnDYuMlPFoNN8IOgrxqrlz7NJR_b0NVbxVrP6JeP_QvAzs3r4GKye0IP72mEgSXOPVQaOFouo6mZaUeuw180Dd84j7rwpxtmRfPI7jmhS7fxgM2Ldrc20fuDnyhhqChe0-2ZewQVCPs-qnilsftZtqmWtfmbbu-zpWTjPp-rGy9F1TJimBuvYDrBeXwFiBP4FaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
چنتا سوپرگل نامزد پوشکاش ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101988" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101986">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxPAvG2k8pJWPYqXqt4jkYPLda0ZlRL0jynBPJ_kuSOt668O3dUCn6VSfXpVa0tyToWKqmaipBg6XUJHQyrOczxf6CmChobItRMCkDCY05qAzjK_lnEL330tJYM-cWj07FL0a_ZYX61Y4ed1XBQAgKymwvORQftLkdPqDup9CVggXMkLVYSxiu2A9a9L7-66EUP8xOWEmuEco2at3JnLMZ9iHJPAHGYGW5lhaRiZVj7TTqCd_VvFaZm64n3dDU-EibPZCIQblTRCfU5r7IhceYkleP_nGR3x7joraw5K33jv7_2WaQbysFO2efMlvtPCNIuTzPbGIuTrNeSoLlOVHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETQQQyqNnpFYWW2S6D8525UCBo-3fwXPQYakUHZXWe_AZeQ_2HjrcVMcUHWDoKaYfucWxmI0sUuiaE95Yu176RQfgQ03VC1KohSq_2w1zo-lVuAYN4AzWng1CVChj2hm73K_C2uJzo5hcDisrH3eH2m6ihsaIjL2PA7oi1GJUT2CJFlQGihvSJYe7rIc-WOc_Zz-E38De0ExDxdn_uWppJTh0MzdE65G-sAp4NNDhxFQjubUUBu5lDaJd3FFytLouuVaV7sLv_ddzCeMf5Jw-LyaNZJCk3tBbL4JsnDSAYG93E3uVLSjVK5jf_LqVkKtnsuYbUu1jMRWs2qMhPbb-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های لامین یامال:
• 2022 — سینگل
• 2023 — آلیسا
🇷🇺
• 2024 — الکس پادیلا
🇪🇸
• 2025 — فاطی واسکز
🇪🇸
• 2025 — کلاودیا باول
🇪🇸
• 2025 — نیکی نیکول
🇦🇷
• 2026 — اینس گارسیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101986" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101984">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hd09heBbZTU0d7uIyYJYhlzKVqKuR0mtRC5g5rsW_xhrcRXSutNIhS1-jYIaWsuqMnyytV7gBks_1uhr-jeSyvSi31wvopabu06SZ2ymu4VHNgoCoSGtaOw5eLhhdoy9g3fsZzs-0T-ioTuP-VcKQIixm5IHComak8vq_jpgaGybmMLoz_oETrSoQeALvS5iEsbYLMpxElZZDONjf0A_HnM_iP2hniJrSnplAU1t85QeAED8yDCb2G8qBMtqp6O3-VafQHu5qUXVg2Yd6ctd1cErCXDgKuskU9hqXzOhz10reAdabM84d3XZqTLu_DhzkXPErkLl1vjrReoCPIE5YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvmahpeqR2u3Itx0TnL-mFVDIn2E2FqhYm6srz0AUc7Q3HJjKnZhXdUJTlnLJWSl8Q4M0vAzi6iKZcPBjVDn8ZM0FfhGObfjxr83hAUWJ6zHZcU1z6dRSUDdsE7ekWmrH6_VDxNohmGZj1HX-P6Yx8Epv3djRpvyE1ns9mB49Aa2ElsZcRW69pqozO-UH74CDrU70Heglo-0P1-1G4yquXfnL-wyu1ChybCyMSTf_21ZC-xNwUdcqKddXZVFlnAUDzr6nbBkkCrlf6HDKOe37PN49XgIH6nuczpgEu0O-sKnS8X_Z2zYW8_yrR6mM3CoZuL54Bf51QH0beKN_WzpVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جسیکا توگا دوست‌دختر سابق وینیسیوس جونیور:
این فوتبالیست‌های سیاه‌پوست فقط از نژادپرستی شکایت میکنن ولی همیشه با زنان سفیدپوست و بلوند وارد رابطه میشن. اونا هیچ‌وقت با یک زن سیاه‌پوست وارد رابطه نمیشن یا چنین رابطه‌ای رو علنی نمیکنن دلیلش چیه؟ جوابش واضح و مشخصه! خواهشا این سیاه‌پوستا فاز آدمای اخلاق‌مدار رو برندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101984" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101983">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101983" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101982">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRZBIpZdtyGIRSGkNkTVVuG9OdwZCCrszBWskNVTHZ2oauoQcyD8DMgNmw1zpD8wRT27OXorFjc8u6ShHyVjKYR3HKAj2f7pAkYVQFkFTexyvuFCwNK2F1zWZ-bpD4hrVnIJNq1ZGBYtp0ikZIlblrAI8W6CMK3384RK0VI53FtTaU7SdjYGNDSpItG12nsTovwGpC96EcJmSgkXA0kvJt0lvUjny7whfXz_hx3XebuxAIzQveY1J-_Y_Q8L2PbPwXh-OzK1Y9hj6OehKfnGYrPATIsQdJOFKIlZLo3G1Npa6WxAUEFOVgWsSlDC0Z84I-gKOD25m1UUzEOSYsOM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101982" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101980">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tAjax3xCxJrL8nvP3raU9Gkj1FGN3Vb6trhCWd-c-zYp6eNjrrxYJbNJzo-Sm4NFrXegcJgSmIKKTm8KajnCfvtQFUloPCTkcTw9vRxaeHh2R7NvX5ChaIxMZJ4aqKxfvLmpjeP-ncX1tQo4OvGkrnOMk88_rFv_NUhjTkMOuYUoHrBcluPtdhOAP3jNI9tuX9Ep2UnwXjb5vhsQMFzB3S6JyEcBSKFT0ZRD7Z1JwU2JZDb8D6LvqCNCTpikpQV4sYIr9xuWnMsF8hbkDBuAAKnhY1sqEj8hspADh1L6Duj_XalZLGKGBmCIiBeWJ4I5zdrJteKRSHIeVA4BFp9GFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMYh3p3XtAMlJXieGhzBWbsSJHH9eFyZQNHwLU0EOS7efH5aVIXdHOmaeE2_soIJlgdJmEXhD5woIB8EjIQFNf0Qtsv1iPNB1x5C7dM3wLeQbemqUDbV0LFZW6_T7khZYktipHz7y2RRx2wn6L2-8_-MED47D8h2nxTi4H0RNeY7NhaA5LXzfHdYHrZrG3PEf39aLhwN9AIrQPBCBTwnjI51hjiuS_yVO70K64gxDR5IWu4AHAC0fkMN6scujX4ZUyOS61bMKIeNeEUX0m0F60SNFJvmpZyjj-p2hZEKFReZStc-u74CsG9IluYlrvRR37I-5RhGSS9gPW1SMUvINQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📅
🔵
17 سال پیش توی همچین روزی بارسلونا 46 میلیون یورو + اتوئو رو به اینتر داد تا زلاتان رو از اینتر جذب کنه.
🔵
🔺
فصل بعد اینتر تونست با حضور اتوئو یکی از موفق ترین فصلای فوتبالی تاریخشو رقم بزنه:
🏆
سری‌آ
🏆
لیگ قهرمانان اروپا
🏆
کوپا ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101980" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101978">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gGhaeg1sbbp77lVOlKj9KwTXJGvCz1ZY1TpdX2dZddDhUytA2gAOpavBEZAygPIkWJIAwQxSatRkvaya7aihevmCihtxAgm_hztE6FxbdDwaPtFefyFVOXLx1WDnKEZCQ8ynn7lm-VWumFK65flLOk_pWIJsc6ae_CHZV4oI-sMfo4thjnKNx7pcGRDCjeqDtGMrTTV7XIy9KxCP4OFtPHsSvO6bYM6mUDIEU-OZFCnYV3-tseDJcVAhdzoldPiiOUJ0HoiH7_C8TNxEC7wdHzmjoTPis_C4-3onBtTO6x58dGAtBK8EkT0JjGjqtPE-LyQd-FM5yk0K01K0s_aY0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jzehbBilmgKODLaSUW3ZxIkCQA4sgh_7HSaCeE7-WY-VcOYEiWtaCjftiITZeyIfZqlqokgkQqvBwjQuRhr0yhiaAXn71WfLjcKgToUV9xt6SJ24q02tkNEu_iH3RvAepTa3nrJXD4jANiMp6ZwJwgEXcgAW9FGYfIMYAj4zkqJYVq6Zj8JVg1kQGvRegR4m-SO7C1tljjw72SqCAM2D0FkyjbKcapCGkKMF3M9Qk2pQvlUsmBsIXN4GLp1Ly-WGu9eRfSbhUYprENZgkqdyNyp7YVysjBhTTgdxmZsk7_dz5uCR40GUvsnlfwOWA9bxGbJwzhE1ppmZ_qcRHH2vlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
الساندرو نستا درباره غیبت ایتالیا در سه جام جهانی متوالی:
باورنکردنیه! پسرم تقریبا ۱۸ سالشه و هیچ‌وقت ندیده ایتالیا توی جام جهانی بازی کنه. وقتی بهش میگم ما واقعا جام جهانی رو بردیم، تقریبا باورش نمیشه. میگه: واقعا؟ برای نسل بچه‌های امروز، دیدن ایتالیا در جام جهانی انگار داستانی از یک دوران خیلی دور و گذشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101978" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101977">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pua4rhtvV80sPAdy6IFRNtVSgxxT9mq46jYv4nx6Kq0CvJI8SSXqE38rhVOCxivG6sh_8dwYwQEdH8nMF3rgZKRkKD6dN2C1DPE-TudJ0F1gDIXYBNRwoa-t6UCWHvtv2XOCHV8XEbM751WY2-MKOp13XZupne79iTkH5TwUVax7_hBdGLibS5x0zmeZPbl21p1CUjPGyJXju3fJhO7Z46Zbb3iNjqpN-T4X1bYJihXzuVG6duKI3LCWxbUgpyGZ8y7x0Lbw85cxazAvL_DYw3nqQjO5VrlUJAR8wFHNSnb53by61S2lfSHBNzPZ4vxXXiAVhwOpL_HJaD8AITrKAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
ترکیب آرسنال اگه همه شایعات نقل و انتقالاتی به واقعیت تبدیل بشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101977" target="_blank">📅 12:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101976">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoT0qB41QNgEP_v4TBbkZ7VmpsEqfviCYk15cy22qscXMqvr781rVsDC5R_UnMYrBvHI_4OIl1blaG0Kxc-ecM5qP2ac7zk-wPsjfURrid4GJ3pjJkkTrjALoBi5iw2DYTCyMcBug-JywembgZ-vW2Edg1XU9S6T1_lM-VmZMhbNQ2X9BawfJWFKBcg2U5D-6cyVbumEz5W733lJJOAlaaPg8se0vQBXmpzAK5W1vkW8UXHm0IIvnVozFcExMjDe09T9XDWmlg48oeCgTPua1dnV0BeGePU18Wng4n8-WqIct-7P78IyX1Eu_AkRrBXSucaXeAo0mWu7kMoHmr__pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
طبق گزارش‌ها، بدهی‌های النصر عربستان به حدود ۱ میلیارد دلار نزدیک شده و همین موضوع توانایی این باشگاه برای جذب بازیکنان جدید را محدود کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101976" target="_blank">📅 12:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101975">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=Po93v4Y2ja6OANq8y7WBb5Dtl5p4uHMb8ET_GiO5d96Rxl-InhQWkxa_ykhuQmtxQ3c4J4Wc6_NS8JrlS-l7Uk1vKQGqrgDBp9AzjfSGAXNFJs-8M633MxfX4BI-KmZhWPdJMg3H3udZyn7ToEqv9KySgamJFZQ0HmGpSSHjiI1BmTYLEX9Mx2enkEKnKyQSqIlVGmKMDPVNPKbGtcxcFsJt7jPfD1KVV5iTP4pQeEpfGi1BRB_B8rKWWk29DasCpBwdvkdg5nHkl2TlEkNijtL51cg-K4Q_mQDZ1NLRm9AzjL7h5PZD2DnE7HvOCVFSeNLDppANV1Eg2RH3jMT7vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=Po93v4Y2ja6OANq8y7WBb5Dtl5p4uHMb8ET_GiO5d96Rxl-InhQWkxa_ykhuQmtxQ3c4J4Wc6_NS8JrlS-l7Uk1vKQGqrgDBp9AzjfSGAXNFJs-8M633MxfX4BI-KmZhWPdJMg3H3udZyn7ToEqv9KySgamJFZQ0HmGpSSHjiI1BmTYLEX9Mx2enkEKnKyQSqIlVGmKMDPVNPKbGtcxcFsJt7jPfD1KVV5iTP4pQeEpfGi1BRB_B8rKWWk29DasCpBwdvkdg5nHkl2TlEkNijtL51cg-K4Q_mQDZ1NLRm9AzjL7h5PZD2DnE7HvOCVFSeNLDppANV1Eg2RH3jMT7vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خارکسده جزیره برا ایرانه
✔️
خارک و سه‌جزیره برا ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101975" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101974">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0hvXshgkMLMtMZEKHGo-XSy_vPZ7Wj8ibquBgNSVuakz6R4gt3KGsVI1vu_QztKWe26Cy85EmH4nT-GyMMsmj5ehj5NcvdVkVgDRjrfQEDcPkWz0YyaL5c3zY9bTpLXKeTQQiqs3tN61mwX3S64F7MXwa2Mq_wZAHxifUMdilfandcNU3bxXZpFsQozAyPsLEi04nh_7DsobKOPJDESU3jNGkMBM0PFEajFAsyKD7EjXQfYSQKUpvXoj5f5tr7rx5agNmFcJhIvpm9lbibRZQoIC8ViT8FKvgJFzAki2d433OBv72opWBxuIhRoA4PMt-eDDqJIgbC7ra8xIFyxkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انزو و خانواده تو تعطیلات
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101974" target="_blank">📅 11:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101973">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzvDPfLlNbGq4Dsk6E2KuSDaVhEUAfaR3-x2pRjo7XSQSg6_KJp-Y2nJDFRh0SaaayouffhoPakaZal8h9lFen5WDbeW9XEzzDNNZfyGCp_paGf3QJbSFiO43B1Bz8P8cndOuMTn5uIX-kCqfhWBUjumX-AUrPPCFJq-GmHjGp8QYmx4EUNYIdNP5iDzpZMT6eKgnHQrK5tFJs047-Zq9-gbwfvFfILq2RbfTgsQvJwQcMMlTLnps-87_rzoD3kcS4GoxLSb8PrY--iAAWoC_g2iKkG76SSuwi7Gop3YLV9UsriFHNUicCaSNWswZq-xJTq6hAfAi6CietplQYyVPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
مانوئل نویر:
🔺
هرگز آن لحظه را فراموش نمی‌کنم. مسی بواتنگ رو رد کرد و درست جلوی من گل زد.
🔺
بعد از مسابقه، بواتنگ شوکه شده بود و گواردیولا به او گفت: «احساس گناه نکن، این کاری است که مسی با همه می‌کند.» سپس به ما گفت: «حتی اگر صد سال هم مربیگری کنم، دیگر هرگز مربی بازیکنی مثل او نخواهم شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101973" target="_blank">📅 11:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101972">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=V6uc4_5mdxHORhsBDiZI3lOdcTCma8fdnizFTPkOQmSjS0ThKGQ7tADevNMxVc8K0eCaaJevMgpmjVgTgfN2W4miPG_luvhvj6ZMQTG0LxCzHdEAoBoDFtD5N6A9fIDLyoyO3w4vhhYvT-tJg5zXtr_5TZ9GGLCieh-wRORCyCjCXeMzK0Fp6FCb8xNgnmwGQxZx1AcJGXcc_zB5nojHiSrVMQt51nulYSMJq8-b_nyqIun8azRHQRLu8hRFOh51g0gn8xo_TzjwMVWlGNDkDnghtP0-gQruqaFad_LW9CkbNE0PDf3CWVG-JqTxJrSA_P8_NMhYADRH4JnFIj9noA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=V6uc4_5mdxHORhsBDiZI3lOdcTCma8fdnizFTPkOQmSjS0ThKGQ7tADevNMxVc8K0eCaaJevMgpmjVgTgfN2W4miPG_luvhvj6ZMQTG0LxCzHdEAoBoDFtD5N6A9fIDLyoyO3w4vhhYvT-tJg5zXtr_5TZ9GGLCieh-wRORCyCjCXeMzK0Fp6FCb8xNgnmwGQxZx1AcJGXcc_zB5nojHiSrVMQt51nulYSMJq8-b_nyqIun8azRHQRLu8hRFOh51g0gn8xo_TzjwMVWlGNDkDnghtP0-gQruqaFad_LW9CkbNE0PDf3CWVG-JqTxJrSA_P8_NMhYADRH4JnFIj9noA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزلندیا اینطوری از بازیکنای تاتنهام استقبال کردن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101972" target="_blank">📅 10:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101970">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGIAok3ADxrOyEvWnA40lNzSd5yxnJ_LSPYPE4n3T7KgkgI6-UC1BMkB1_vXy1u_Ifr6Z8F8vFRb7iOJDghc8iTcHLkvSEqOHoiXtOqyBub9bipl5D4QcUE7Hb_RHa1yt9zFby1jddaAYahbOqovTZR2Wd4OjN43snfocAaLjumZQJU4z_5fxo-kl2Mx40x_l4yx4oKjoDMlZNa2RdcayrBrBiO2fevn_Z91Jrp3ZQ1QTqorLDonfV-4ATKv6fdP5OXwNDlbrq4IfyIy7fxRMF7WZmhUlFQ5OmfYPkGoeYyZF9UE-7EdzuBiSpbv1xFbAcCOq0CIqGFJHqTT5UaQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbcEF5wHPyOzgtndzSwH9_FVl7AcaZ-j544z9I2Sd6aN-r7MGYNzrXLRlTLCoB7PRp5q9vRpjKPXOk2p5aSUC9I4Cermi_S8HnoY8lmTSyR_CC_TQ5ovTKcWUM8rBLi9wnkg-74mOCzaT74qJ4jWXDIfUGfhIoDGkLqPwiO1aoz18hQyPDj7aUfIUIRZiOpS12j482N6XalbhzaXI75wyHICrn4L0qo-qiIBHSu1irJE55CJJAiCKQm5216nQjh2k2v-6FHvB9ZWlfxuFbv_EwgFFvMQZGwie27cpKm5OAxHkBfXN6NQMBkeo3whwyGE10jbzxy0OxEkJYoddvD1Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدری داره تعطیلاتش رو اینجوری تو اسنپ چت میگذرونه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101970" target="_blank">📅 10:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101968">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RrNqxVKegitv2Zx2RBb5l0Oo60wh4EdUQqKnqPLgHSB6WHWjZLO2Hvzqa4q1AUwPImSV5B5N9HRESH8J5fij8hSP0o3wQu0WS7Zv7c9G4sx3Mc00dbaiiHFMatcshnr0LwRg-VGDEcdE8vH_yZ0zvRBE6-ojNUlxeZfoPFO19bPwm-UM3GVLSScQr-kGOkKxtrASUtk_PAaIF32vqeKoBR3kq5wye-Y89C8kj5T6Ks7md0QuS_6WiY9JOYgBuWUwPEGygvMea2kpZjLgWwsn3wDly8nGwUvXW0RJ6dX5qfrHld6LF_wUNtH1amJqkgocbqNZ73u2G6x0EUQWwUQoYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/skSv9mgEPNjun3sULeBcN_OLfph8D9rRh3_UYX5BqTeNXrHHQgAa36q3wVKbXNd_T-qcsxIKd8DF6cF3Tawu4N2HdqCNtx3AsQYqAOWywGisP8WlLtlGxeGSglueMSfjPlcrz-tcTdDF7xqGAdeIdJZing6pLyRiZnfcCUsOhpaAyPmXCjNixm71Xf8daIsZnqR6WULNBX2D6AKx-jX2IFCUfpPPcMzAr0OPWxbfeu6eXrqftBRPTmHcPDN6bCEOYq5ahCASL4UhGuVDQGTUg4do671b2VDdzM7CsBvl49lcFV302Hy8dMSUGkFd7GxSK4RwHNEcmUnqPcR5_3aPbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😞
میگن نیکولاس پپه بعد کات کردن با اکسش تیانا ترامپ ( پ.ورن استار ) الانم داره با لانا رودز وارد رابطه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101968" target="_blank">📅 10:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101967">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHsf4Rs8TDbSiWbK9CRZp-CiYYZO7vRM_GE0RdsA8iTnKzzfIXmOMBeOg0mhhxgoIOIHACgHVJkoXS-X5ZDJba-rbD4oWKITS-1zdnp6w4lnRdpPaZBcSOfCtLqdrfTWtmKVf5IUu2tFDxUDLkoxR8OQ5C1n56sjCAkoJHgDvMv5vRxU_CqbuhXkoOu6IzzBMX9vrY2Dc63-76hLQ8tT20Z02l4v1f9j7Sgr_EzwdjgGOSuwfopQjV7ed8HFvzxdkrX6Ur2SCMmPm_PIZZtpvDE_1xQM7-7G4MsIJhTcl5mXAhOz1L5UN2FcjOVjxDrOs16L-sUknNAUrNCm0c31gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
موندودپورتیوو:
اگر بارسلونا نتواند خولیان آلوارز را جذب کند، دیگر هیچ مهاجم نوکی هم نخواهد خرید. بعد از جذب آنتونی گوردون و کریم آدیمی، مدیران باشگاه احساس نمیکنند نیازی فوری به خرید مهاجم داشته باشند و معتقدند فصل آینده فران تورس، دنی اولمو و رافینیا هم می‌توانند در نوک خط حمله بازی کنند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101967" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101966">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvV16cw7MI2Loh5lOKcNFCT-b2TcKv-qwUbQf7AywNIQpdgQrlvmJFITAKRePQ5Y-wXrC3ESDKCreR6K8E2m4tpj_ANNKNM_BYEO9xyfk57J4QqurRsG6XOSu0o1RIINdR4mvAM2FsPiJK-GvucChG294ieBsPLPuNeslV4zjYpySkAgHSyLbJwFCNrMoLu9p2RIuR7LBlYQXgX3MSdWxhqbXY2ja47YpsL74Y03MlxSxJKMtkDy9Ij5ON0HM2MdP8HILKlyFccu8M7dKl-9kdPCa8QnrdJNopAzxpXFD0tWy41n98JbGEHgdHpo-MOt1CxCtN_Nj7YYjQcMGW8axQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
–
فابریزو رومانو:
⚪️
در ساعات آینده، باشگاه رئال مادرید یک پیشنهاد جدید به باشگاه لایپزیگ برای جذب دیومانده ارسال خواهد کرد.
🔻
این پیشنهاد از 100 میلیون یورو بیشتر خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101966" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101964">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcBoGqwIME_bOrbYz7Wo-Mfs-IB7xLlMQugvI9BdIZl7cfYxUzMQMSfwF2bBfK_iy1xJUcrMQ_EehQKMaN2pKkRefcl86Y8iigR-9nFKVWVxj3Nqw66F-uaR6jcUEmldbCWAPsUvre5UVhZtm4tuNWBVVxEC3Us0rQX1kUQ-ofg13rOuHUeCoEypRb_1SPdd9ixWQlZcRMxS8MswWbwdSscG7CpOlxGRXOc2mcaPS-Ee49jr-6yKEqRdztQbhTO8xYvt36TqwHj7KBfcDTmY-BGHTc4NgFFo07La5fb0sIN-zVaSR1aHUWVgzz3qggiIrYwqoH_mU__xfoN57M6wfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1dU7ZG7pzVkbXkIfBmKykwpZKcUBd-AIcYlW6zKDDLbjkUrWe4xplI87fodLoD_oJvUPaRIbONIRMqMhQgx999fECxSJx9-0wawuKQLViJJByv10jy4Sz7eH1S6s46fBisHLVlB1BX5Ez3rVujbgO0Gmb_J_JcANa0zXMH6Moj6daE-gvexVn8mO4lgg7bS0VqJptd85NfFpn1uwzF82YePcEN0XkSHGeDf3otwWCMmh-4Te64jmQLYm28UuN3Q6wNNVtM4q-jmwgoNpfRTFhf-GggUy4AksVyBZqyXaL8Bbwf04_3XdFpPwfQTJ46MbSpsOtx7AXWNjCrnJq4fZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سوفیا رین شایعه‌ای مبنی بر اینکه حاضره شبی رو با کیلیان امباپه، آقای گل جام جهانی، بگذرونه رد کرد: من هیچ‌وقت با امباپه شب رو نمی‌گذرونم. هنوز باکره‌ام و خودم رو برای همسر آینده‌ام نگه داشته‌ام!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101964" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101963">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PO1iD7jJOfGshJMTeZuxezHchHh6u-Jtn2cPd3v5D2yGoxTOAqvD62JLF-CelMoBOTH6v_Z3NpiAOeIqzAbJ37FchCqh52urzyiw7JJYuQr-rutgbk9pXfx1kXL5bJLjk898q8kZqpAcyxO7Hd-t9fJZEGmzp_idtj7IBRR4mUUBsBrFZW3p0hVSWXCcGTeeWMo5oMuBsv8Fsc_6e0nws9uv2z6F6ITgC6Q8E4wgJed6Cwu_mcYPAUXPgg_JzrnCVnyrDhbwUGfbMQ1mH6b8k4c3UtEQK8QEUxuZrgy0cKfxcKwKV_Hv6UK__aM29dUNSyTiST8ibATNRaNrCXUeOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدوی برزیلی درباره کریستیانو رونالدو:
فکر میکنم بازیکن‌های خیلی کمی مثل او از بدنشان مراقبت می‌کنند و این‌قدر اشتیاق پیشرفت دارند. من تمرین میکردم چون مجبور بودم، اما او تمرین میکند چون عاشقش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101963" target="_blank">📅 09:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101962">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=g9c2AefvEGOJxuAA6nUkHOKFSXOHmCbIZ5XrYO1Wkkz38SIJZ8tine500w_wdce6p5uI3RTqyU6EfQDR4VyO9hL3eJZzbnS5gN0hfOYZAR_Bm1Alw0CMNxvHliTTAxPytkd9IBoc57RT3CRBa1Ini8AWguQQeSx0oIqArCpA67EPvbWWuYzQF4J-ABt7ZY9V47AZ1jtgzsBRbDke6Zfen4QKlxGpk3-LHiEiQ9v-Jpu2mKhc3ukDFk1I6B3nw8-Ylrn9w0OpFyzri1JZYzY1PaGB7ugcoOgmyup487i-2byTNA_J6Z_XbJGIw5XJFp1h0gSXVpG8ZjDEdC7pMaNBjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=g9c2AefvEGOJxuAA6nUkHOKFSXOHmCbIZ5XrYO1Wkkz38SIJZ8tine500w_wdce6p5uI3RTqyU6EfQDR4VyO9hL3eJZzbnS5gN0hfOYZAR_Bm1Alw0CMNxvHliTTAxPytkd9IBoc57RT3CRBa1Ini8AWguQQeSx0oIqArCpA67EPvbWWuYzQF4J-ABt7ZY9V47AZ1jtgzsBRbDke6Zfen4QKlxGpk3-LHiEiQ9v-Jpu2mKhc3ukDFk1I6B3nw8-Ylrn9w0OpFyzri1JZYzY1PaGB7ugcoOgmyup487i-2byTNA_J6Z_XbJGIw5XJFp1h0gSXVpG8ZjDEdC7pMaNBjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚡️
بخشی از گفتگوی جذاب بکهام، زیدان و زلاتان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101962" target="_blank">📅 09:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101960">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xt9y3W-McjUb373kl_EvKm9tRrLimJqBJAj_T55Sv_3F7teC7KEDSJ6IZY92v6bfKA5_530OoF3U3eX8SyWy7cSJGQn3Vdg5uTvIGwrVrdHnXvdnD-9SPR2tDNpfdduuXJb6qxpUHcnUM-WEcu6GjPWWNGMteC6oM6fYtC_53SGoEo_qQl45L__Ds4B8cD7Esua9LRDZ-xz9yYVtVGEHcM4yh268cUjRfqPZbbcXOJhBcxkjpyQYgRmjg64H-564v70bxrLfTZdbJiZ9tlB_xBUwEhvZL-fyF5An3pgVF2sjiiRfrza0Pj7nXUGVR1bGVoGIb5PDl7byzwBvQyDYFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cb9YOJRDCSDOnQVGZBeU0KnF1o3k9RYfhxmfnK-ym0Jb21YiiLlrLHqTEECToPBu6nMMA7y4Nii8Z4jAhuTKSKLyYbt9HzHmtVltFfKFcAYsN5RjJ5QdEDvTyhVLQG5cmvPVvmPrBluVdDnguXmw5asvpLjwELjNQj4t30c7fGIIc9RJ2M1U9FJh2KEBNofvUpyI1az11Rn1TgIfCrSL5MMASxCAfOGQdlRDHqDHniHSq7Iz7a9OxgeDcHNIpHj4MZUvs6hi_WzzWzLxgk12MVijDdOwR114I6tAwzQ4lrdkvzQVPv_gUSQ7NzJHtFsYHQ77RFonJ9tgI0TEluw5VA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو و جورجینا قراره ۱ آگوست با هم ازدواج کنن بالاخره. تبریک به این دو نوگل دیرشکفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101960" target="_blank">📅 07:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101959">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vjgn7cOIjiuNyxsAulkEPDciulvXeY92VI3nm07bhtPB2RJEr5g-pm3cxZyNP-PyDnlUY31x2Ouq1K7Ps4swUiaA-3NZ3hMwy-hDP_jazHRS8hy8Isf0jtCTlocNgFrIfXrH9x3hbiMGOfd4tqR0gsHjbT2wFV1pTw4PK-Hj3nMx8iiI4N2nwq8IsKdhnJDopsAjnCFafjBsNUZ1VjJk-eNBQc5_3_yZovgNEg29v_Mqq-fFXxVUyfh9BTtSfzPWQPp9Pykb9AXur2UmxuqRtYz-dArIqGPvpP6k56nXo2BJKjvO0WByASD5hizrBH7afyGc4-_NHLc9WL8Zckm-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👑
موندو:
تعجب نکنید ولی احتمالش زیاده که لاپورتا پرونده نقل و انتقالات بارسلونا رو بدون جذب مهاجم ببنده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101959" target="_blank">📅 06:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101958">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=YqqpfSCiNE68QoFUiGMhsPUiEn5qX6mOQPTtDqe3M9Bs7u_lC_qsYHZzsLMiYkNIXo48Ts23q0Hqu0-ELHTw6nTrPFtKYH4yQzFydACBV-aPQYi2rCQ2utN6j4rgh5O2BU62yfYHzRTY0PHft0WtPoxpzLGQFu5DFUzH_QMwURYhIeRBaOV05XVgf5W5qVKkBXQtmz2a5ZoBA9miyeOf2QmRK_nhFMGwt-22hkBzyTlNc9fitj44d32MI3Dq-Q-tsmBbCFW-bxLNhd3PKfQr3WgA0L5fkLvwEbTECnRBFP5EMsPCDgwfEdmeR06IkrFdQ8QLpv7oDag0g-rH6h03qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=YqqpfSCiNE68QoFUiGMhsPUiEn5qX6mOQPTtDqe3M9Bs7u_lC_qsYHZzsLMiYkNIXo48Ts23q0Hqu0-ELHTw6nTrPFtKYH4yQzFydACBV-aPQYi2rCQ2utN6j4rgh5O2BU62yfYHzRTY0PHft0WtPoxpzLGQFu5DFUzH_QMwURYhIeRBaOV05XVgf5W5qVKkBXQtmz2a5ZoBA9miyeOf2QmRK_nhFMGwt-22hkBzyTlNc9fitj44d32MI3Dq-Q-tsmBbCFW-bxLNhd3PKfQr3WgA0L5fkLvwEbTECnRBFP5EMsPCDgwfEdmeR06IkrFdQ8QLpv7oDag0g-rH6h03qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/101958" target="_blank">📅 06:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101955">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbZchJEpdFzX0QO2AGjQa3C3FFYsXcVYa1bKTakpSPoH2fUdcz5GhEhnfNPIIbZalg5yBN43FJqZbjOixvTutU3OIjkdIBEnv4y_Y6ieLsNE8oTQoCDwfW0dfm9V8HHchBVBiviwMfqInuv-K-E6L1gGMYnKPPp3uGenzo9hsQbV6v962ZHf66PfnUjpU9c5YrNwHXO7_OJ95TDI6GEtVTZjP9hWuBd6HrQEn3WjnX8ZroR2UYTTDGEFaYP3WcK5KvacotJJw8B5QPbkB09H_Z2dLW8MpCgMU4FHJEWD6tLSn2kUwtxURh_UPCCWsK6VWSTNKAJXTxddDboH9ogntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aUGZA9i3nZ896mTLVuHMRxIvc3x8YRoBirFwdQ2TxzD0XWm9eVVQnS9EA3rMWFMobadWK5nstqNWw7bONxEnkODJkQ3DN5GmL7CEaPsPULHY5_yXROpwAr36yr0ltHn4pg9mkEsEdJ-F5lhQyf3zPca3-oLctdyam45Drjiq3fnlnaowjgIqS-jdpU44IEtwhhAVRnZG8w41UrgOeioN4uC02jP5IvOF_4dT2imr9o9c1zON0tKt26BWASPagS_xzEwaZzdeQBQATCau32txsXFFPUny9R_G092tIfPcfvNncQp06LCZrUeh0innEMmeQrbkgoRTBVDcnwGedmuO2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=rkL8WNwlWYyXJyUXx8ziHhQiVq7sTR3EPIdUEkNj8hVMLyLcOrop_Ma_nF0ETriYaoAQWxBxFOrwcRB9BL9exMXZs7huYSONRivdwM90qDXXtKYWgFd4R3iIVWbGEzJFReet-QrAu0QQPOuVYMJbD95A8sjnLKUavIextV7_ICA4tXMwObIegr2_SeF81bw27Gon-ry8L13RfqsEg9o5XR_nSC6n9qoovK-vmHxxHZ3h5q1i8EEvk5rw1ocvxecxXRu-QtPkQwmjmY8Y3DdkEKTf_1d6HeM7zv0zV2VzxFF9O1O-UAfOUB22gA8LaYAXnd_EuS_wummJAAj7975z-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=rkL8WNwlWYyXJyUXx8ziHhQiVq7sTR3EPIdUEkNj8hVMLyLcOrop_Ma_nF0ETriYaoAQWxBxFOrwcRB9BL9exMXZs7huYSONRivdwM90qDXXtKYWgFd4R3iIVWbGEzJFReet-QrAu0QQPOuVYMJbD95A8sjnLKUavIextV7_ICA4tXMwObIegr2_SeF81bw27Gon-ry8L13RfqsEg9o5XR_nSC6n9qoovK-vmHxxHZ3h5q1i8EEvk5rw1ocvxecxXRu-QtPkQwmjmY8Y3DdkEKTf_1d6HeM7zv0zV2VzxFF9O1O-UAfOUB22gA8LaYAXnd_EuS_wummJAAj7975z-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/101955" target="_blank">📅 06:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101954">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tn7YfWI72i3xnc-0dW-Osnc_uHzkCaOHxysgU4fVtNFlUoCnXeDFgudEFH6vApRYGci94mxJQgobxcMm-J4fNWpDWlqpK0BSL8jEALLU2UTo0cxyCRnhpAreQFfbs35gImFJRCwRiWThP-xyyYxBPuny8Iuh82O1FN_JlQvcjbpjNU57wwVR5IqHcr6n1BTGhLxdIfx88-9dyXRUYwyat6UuKKDNEOJNPvbErigw60rzkmiv0EppmLqtT7DWJ9IxbF2hsSe32gzrgtzqfmMl9OJ5a6BIURfOySJkGT3EG8CdntyXiOzZ0I_FqJ1MnkqZ689ZUj7zP8G0iTTJoLnO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مسی امروز اینجوری تو روزاریو شکار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/101954" target="_blank">📅 01:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101953">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu32hyY9AMysgE8f7i5oiD2AXJBO_2LkS1Lk-onKgLRNAIPecnry0TUFZulT_cDp6xb0L5axZcUyVS077TYPl-RKUBDvd6x4-lCjdfwkkdkE89lYA__HztCORm7Xd1eoFgo8Rs24LDpkmHwd-KOnKqZc2F7mvxhFWp4zCoSkgpzcUC1AAh4aUIu6SVRvkaX1CCG2t0EQIcrG1l7tGWiTT73Ufi_rBC7mjyck3MlFO2Msrt8tAndzk4DdcEOSBK2KRj0qA26rD3hGU_nElvevrxr5BBw8pbwogBDiuyM80so6mv-fNAkn80iRC42HEy9X2TgBK5chWdruZSpnoh2MsnTGI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu32hyY9AMysgE8f7i5oiD2AXJBO_2LkS1Lk-onKgLRNAIPecnry0TUFZulT_cDp6xb0L5axZcUyVS077TYPl-RKUBDvd6x4-lCjdfwkkdkE89lYA__HztCORm7Xd1eoFgo8Rs24LDpkmHwd-KOnKqZc2F7mvxhFWp4zCoSkgpzcUC1AAh4aUIu6SVRvkaX1CCG2t0EQIcrG1l7tGWiTT73Ufi_rBC7mjyck3MlFO2Msrt8tAndzk4DdcEOSBK2KRj0qA26rD3hGU_nElvevrxr5BBw8pbwogBDiuyM80so6mv-fNAkn80iRC42HEy9X2TgBK5chWdruZSpnoh2MsnTGI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوکاس هرناندز: «کیلیان، اگه قرار بود یه تتو بزنی، چی انتخاب می‌کردی؟
🔺
کیلیان امباپه:
فکر نمیکنم هیچ‌وقت تتو بزنم. دوست دارم مردم من رو به خاطر کاری که توی زمین انجام دادم به یاد بیارن، نه به خاطر تتوهایی که روی بدنم دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/101953" target="_blank">📅 01:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101952">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnOgZ73d7fi0MSit-v0avYeWoDruWI3V5XDPNhtfhav6yBYGkhCVtzXVjGQQrDMKLUFioQo06xQm5b_Z8JhmdTeVA0pOFj4rh-JW-i0I5aK6NEI_Mm03XMyRgliYdvSW-JMX8m1CuKgYLoZZWeBj0gAZ3LPJPQtXi8AKAzuKFQdigenHkP3hPXJtP07IZ2SmH9QsuYUDU4qR0VxT8lWVXkMsV_b9BZwZOLWVoneWA5LFfXHyU-xWqIHJwK0skRUgwNRvwiJgNmj2BOor1gWlN8OhRrkC4I6aDaltMZtM_yWoY4rz9CqGQX_Mhav0AzVg-fPtWkukZL5N7xhNd8aTwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
امباپه و پارتنرش بانو اکسپوزیتو‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/101952" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101951">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At9Chqk1Gx9fvZ_VLEYoOX93enaFEIz7pDEvWGjUyDHld8rPrkqrYPkMaiCpK9tzIq-B_-AsoF8TYRQVnoRufbj0dJiWJT_kYyAPEcAkP9p4jFCCzn6XEQXoHuZMPlCVQEsS5js-mNIZH6rrzjHV1KEgZQeIUrirUNtKKtMzq6anr1Uym2o5qwn_OA203fJf9D5LxY-fd7yfxcXFmzcbRK-Bbu45J-vo4EEdAj1A1_mAcIYqVH1tDFowMHRyJ9EdjdgW4BtqnaGGf6ls2AnDvZqcG_7LaItgeOoNWl-47DRqb4jxwTk5TMmjTc9u-qZ2jsAomlcLKk8-qmCj4-IYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی خوشتیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/101951" target="_blank">📅 00:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101950">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=aAq24lNX5fizHgHzVEIXTaReuEjuLGgbF0BF_90Nhibr4P96WQz3HJC2k820uEqYXnskO190O6yzHw8ypUd5oZIvPbTTV9yj0Ns2j8AX59bAzq75lKAKejpp-EdGMJZDrr0H2l0Tm1ZBZJA5zITrwDR7kbn-nkD-C4IiaXu41KBeDC28SY-2_2KUhbcjrd1qNhQ7D_lpNa_V1xgadpMSwFg-w9xEqviRa0q-dLArBhgEQIP7edAbPsyk_kv2FqK_uBx5-YW4Y62_eOWHbs3MSuiNM3Ga5HLuQiSf7pDXNnHVKFt5ZCTr8XgBiX5Oo0PdGZNBsZyhjJ_wxqr4_AwLoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=aAq24lNX5fizHgHzVEIXTaReuEjuLGgbF0BF_90Nhibr4P96WQz3HJC2k820uEqYXnskO190O6yzHw8ypUd5oZIvPbTTV9yj0Ns2j8AX59bAzq75lKAKejpp-EdGMJZDrr0H2l0Tm1ZBZJA5zITrwDR7kbn-nkD-C4IiaXu41KBeDC28SY-2_2KUhbcjrd1qNhQ7D_lpNa_V1xgadpMSwFg-w9xEqviRa0q-dLArBhgEQIP7edAbPsyk_kv2FqK_uBx5-YW4Y62_eOWHbs3MSuiNM3Ga5HLuQiSf7pDXNnHVKFt5ZCTr8XgBiX5Oo0PdGZNBsZyhjJ_wxqr4_AwLoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ری‌اکشن هالند به میم هایی که ازش ساختن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/101950" target="_blank">📅 00:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101949">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn8WwYRCU3_HRJ2rdgwJZa8EBSz1kZFGXb8binkMtqsfCN5wRZMEbgiDfFWNg6REA9Y4oAgvqoBxJ_f0D2aFHdy3wDlFoxDjT_Rgb2JsFOsLbApIxGu7VR_hChsm6L2dY0d1te6Ow8U-6TtwwbA9bIa8rFNua-XCtjqWnq7KbNuMWE9y2LdxPyav1wAlsmW8sk73JNw4l8FDE8-W9nLVaoJaFml-8HEj2zcAdVbSBcFP504laCiNEBighDW_Z8kABgcjLZvbLJB_yLCYulPF3HMXRYDhVi7h0RoljA3pVeUNgEpejNq3xxZvPSJMVHvY7GVdXX7JQLreO8Fe2BeB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101949" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101948">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2ImY50ucOpMBSNVQvsgCR9lhrS9qsFZ-CZoaCs3aFpouMklHeWY0tWapW4HV1bFR3qrPr4Awzdyna46tSNfU9ZXCGGYGl2EZkf78YhNu_2JAayg9i-saFDHrL0xPiB1O5hnyiHkLvVSGL8rSGdOXyq8gwrSt1thirnCGHEzQuVWS9nVwD7aNgeyoKOTdPTVNO4hjGNc2nQSy3xU1eS7eWn8fRTimMuhw26a2-R9fKP0iIyT-Fuh8TzGpeqJmsCW6AQfcEZzapCRhKh9l4zl06wZaMdh9N7Ebyvzzncn0DdXC0Mj0KI_X4nCXgojGdN3piuOmBpacfmCsDBzEA0kXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔹
ساشا تاوليری: باشگاه الهلال میخواد مبلغی در حدود 120 الی 150 میلیون دلار برای جذب لوئیز دیاز هزینه کنه! اونا بودجه 350 میلیون دلاری برای نقل و انتقالات کنار گذاشتن و این تازه آغاز کار اوناست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101948" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101946">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XC17u3rmBodeTaV4iYctOmFPLAMRd90SJ0L566wQvSoL1uylJZe5ZxGUdOC042u4palwa3Z1QylXTyY7zkkiBy761lTd5ENTzdewmRXSDxukSURE9RIePf6TmHDc8GbCvHtDlsezmVoAFKpOVtQOL5-f5-oxgb-2xttzc5MxQpCsHA0-rDLFhSwAKCzlN4CxStaIHRGYhJzpoQZXgE8YYmvTgl5_i58rcy1sTbV_ToKXIMBJjdhZpWHmkRlIgWZIjMb_aIKBYejFT1XIhNd9L6b0DN84RqrNNFnFztNQz3KUIQNCf3bmBAMFzqj_akt7ncR9w8UNmS-DrEIraHpMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEk5GUe4DPiKeUHN2ufY5r_Ez2ntrhGpYbxoCNqfSP9kmjSj4ScOhdj__E0Y17Qdnjn5I6YZbSYkbV885QBNq-3veKVvH9A0qzMAOEFabkxPzIfztGSIH3ow1wvKm03vDUGvdMTp7lluVBdzd_ZIThvkv3N9XBNZ1Q42MCbrGzHH2lx-zcvxhnOytrfFpxaok0HNgArC8jnJ4QQfQx9zTJjzRaX0Vy2jO4YLdaGXhwSUK2Nv4cHbXiCMFpMNvhwOsszs4ftts9HGJoHhOIrkP1Z_fAsY6JEmLQfNSdmCu0bwfNYlqc18qikpjGWfBF6neHutyVr3fh0dadiGFpB3sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سرخیو راموس درباره اینکه بین کریستیانو رونالدو و لیونل مسی کدام را انتخاب میکند:
برای من جواب این بحث خیلی ساده است؛ اگر فردا فینال داشته باشم و فقط بتوانم یکی را انتخاب کنم، کریستیانو رونالدو را برمی‌دارم. مسی لحظات جادویی خلق میکند که کمتر کسی قادر به انجامش است، اما کریستیانو این حس را به تو می‌دهد که فرقی نمیکند بازی چطور پیش برود، بالاخره راهی برای بردن پیدا میکند. چیزی که بیشتر از همه تحسینش می‌کنم همین است. استعداد یک چیز است، اما در اوج فشار درخشیدن چیز دیگری. وقتی کریستیانو در تیم تو باشد، همه تا سوت آخر به برد ایمان دارند، چون او بارها این را ثابت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/101946" target="_blank">📅 23:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101945">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoQoEfuMyyPJSonpMFybRONCNAHBB1pyHhDCzSpaDOgy9H5ehwigtlFNKXy4B0ObcjY3TTzv4HAW3OzruAMa0o_eB06cwrHv9pSMPsfRi1dv_3dS8Nuf6qdZzIz3U19vUY_plmAYq9e8hSrYdatk6A9nxxMxXxbMGRZXMd2Olz-RW27CTqUpw6UabdsvVQtk23cBV-Kcw-N6NcIoqUdczq2w39vPZTPHTvEyOk88KqNQ_U9EcW4X7T6MjsEgSgXbWkRzBQw0OBz_cIaHZ05DlrxW7op2Qd53gPQEMLT2mXh4zeLbTAS0pE81RNMXgilrYHSHoOZ3dj9w3W749gOBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
به نقل از فابریس هاوکینز:
مایکل اولیسه تمایل دارد به رئال مادرید بپیوندد، اما بایرن مونیخ درخواست او را رد کرده است. رئال مادرید تمایلی به درگیری با بایرن ندارد، زیرا رابطه بسیار خوبی بین این دو باشگاه وجود دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101945" target="_blank">📅 23:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101944">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQIJAgMxpjRI5fUK630JuBCgK9JtmScaytgOPCEx5u6ttYu2oJErjD4p2fTigLxFdcW_XUJP0yeLpC-fUhXPtfWs8zPE6LB2ciWxoXrG07fO6CaQQDDMOChW0PfHrv-PLBFOauXfjW5y9fl6mR6D1NdBNN7ymVHPYzIhSFbYvwnE2FctpOTGJffdvIBNjL0-tDxbqE79FrJdpSmMfWYfkgOjkHjfp8Zzkn8IYEBT7Kvw_8WPnZr8_Nw4dg02gFjNe9cfsCt5ABIZWh2JL53lp2c-U7ZLDcN6x4Cer_ElzK_qGwXs-MdHCHy7rb-Ax08VoZbJiWazKlwe5bj7GJGRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101944" target="_blank">📅 22:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101943">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh9xNxk9Na7vVKqVkeORNgz_JpWRlR3d19r-yt0q6LCz5jutH-wmTPEZF_30j9lKd95qU8Q9tB4N6H-vf3_NxZvox9AylbjLG3Xut4TPjeumwY-yre67Vm191KPkREqDMxeeMLVu3RLQDdXp6vL7IYRBgWLrhQVpQCHoZvwWkl6S2RIrNI0YYsDXQeMXtBKrfmXXRf8d4e1CQ97KivD3Xv_PZrQ3xjKEJdFClib07JB5rGtsLWuZ3nEan7qHQFvJjuMYPQ4g4oKr7dpLQ4rGbH-VlJ3kfafa8oi9wstzbsVU7kvQf7InHF8__jz2XSYfqBuLRRhdrEwgiLDlSmXLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
رئال مادرید و یان دیومانده به‌ صورت رسمی بر سر شرایط شخصی قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101943" target="_blank">📅 22:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101942">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWdK2zQUEG4jfTaysABOWQSx0vsAf0r0xZ45FhQpYLLM75xivgrAtWnyPfDHc2ehhkk_mXylFZ1OJ-WAmPTGlszXHZUjRc2ofMzrJxBEAXyKoUZSiF-SSHJc_WxFFNdYpqY-owtwBzRdhTI2-tjU0iC2OaKYzW370b4xDhyobjaxfdXkNm99_XSg0XKtXwLPn-QbIIBH5zBEVBwsb1Gp7g_nDzqVCpFL52b3_l18YrCcIuq3u0KiU_WVDlcwPnZfKDlzx70aH-SV7i5iQ0IOdHvJxfD0O5IKeNnFpVh3CTZO9ts6JUvcpHHCZ78bGZLs2hMeyZql8qAYAuyrC07JvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
ترکیب احتمالی رئال مادرید برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101942" target="_blank">📅 22:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101941">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwMThZPH0OtRYeM9LjX4mGvJCnesmbB7-0b_XF3i9HnJvppeIzaMWpsipsXq5L3uGYzd6hVEiq42lIEuJEvcppZ3KD3Nx8uW-q-eps7Buqu3JQtOxilp6EQ4X1W9I3pQbXLMLBn-LRSx6Pa2nTLAyrtUkgw5pyUF2ppMPSbJ0k1Dirw89J1s3BbZabURTB8tysNmbrJahqv3G56poBtehd9jN948ydAsMhlGLo-uu9ICObXie0a14Rxk50lqHPOkH7NPtUn38AfZRuT2NVRc_K3MIVAAtLrZE-lqDIw8btAW2dEDQfzQ-kptlycgvk2W02Qq7DrHuMLPYDN4_CNNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از قشنگترین تصاویر جام جهانی؛ مارک کوکوریا قهرمانی رو در کنار پسرش متئو که مبتلا به اوتیسمه جشن میگیره.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101941" target="_blank">📅 22:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101938">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zt_IlX2h8U_OTzeJstP0C3W-xIR8gDKQxNkjkKmJepplLUkPRN__dVlywVHV6zWVjOkWEdzPILApCsSDPSToiF68-nBbHmeeOaJpeftt-g9MgjBTIPdZ4H3hRAbqNxTLUdTIwAUe811_-kui_MPkm3H_UuCBvBZyhmQEwJp3fL1fm8C5NTno2nfmsAiXaiRbUrCqp-UonVYQc3oFVfV8jd8QnT8fGrEoF_-VMR5lgGTg0tK5oFrQdaYeGris6CgKa5XzHoJIxP8soiWqgtTcHpKGgpXDhLZe1atOL7YBIm9s8hrouCacPGymYOLVg7u5EhArCI3HoknOTMJxh5jvmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i5Ru3vjzQ1B3R2PdhAElNPujclJndv_658XJqa5heGfnZTFQQ0eB_7fM6g-yABA3DsUJaD2VTPCPn9ZHzfj0-RhDXnX2Z7oYNmuAnzyjZc6gqbP7yVSZ7iN8mmCp132E_0X5MVZM2RvLftrTYLx-swmFtCd5lhLJfXDUbQ9QLWyRPu7-Xf_jhL5cwB-c0gQGaUwg-YV9wJJTnFGV6o_pT-n63juyqDBe51BKhCR11MXTF8dn6FWR9lM5TkhezJDI2UMfN0Wnq0pMxd7Llwrw3Qt6QE_cpPfvIhGLNT8G4hc_bdES0CZpapIEYcDU_Y69U8U5AHV9XkohRPLQO62c3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vGLfN0zitIWZsJPPWUI0KLbciVsNEDB93AvKemIFYt20vcSw4H4Kg2hZe1cZC11yIu5Jc5SvV88nUdLlvl95o8bTMlqOtPGSl63C7W72nodU3rZY8Fb6wx7DmLYsar20cYImSYdKtPDwaNfoI1Nuqz2yywm4YLCWQ4rlPU2xFjZUJ-rmXnnHAI40lzIg36UMm0Jp7h6hFG-2OHb3bJqZfeRO6T2wG_JOmx0vNnipNU_BTu3cKSXo36oMkcxYM4S7qKSwWqDaM9w7WkNzwEKHeqLLryPVo--ONOBzu3-8cNV5aIcn7wj94zUPNSeIgoD0W8vFFL3S_HQTSC_0xYvfzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇳
😆
امروز تو یه حرکت پشم‌ریزون دانشجوهای هندی تو اعتراضاتشون ضد نخست‌وزیر هند، عکس امباپه رو هم آوردن و محتوای بنراشون هم اینا بوده:
«دیکتاتور امباپه شکستِ سیستماتیک را تحمل نمی‌کند. همین حالا استعفا بده!»
«۱۲ سال در قدرت، و تمام چیزی که از مودی(نخست‌وزیر هند) نصیبمان شد، نسخهٔ پرمیوم امباپه بود.»
«دیکتاتور را پیدا کن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101938" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101937">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl4o65rZSriXiTrHkgNm_hxoP1x4AiJWDlFIX3OW6dE1DHugcrKmW_C_CHEWR85HI82xzVE9pFv6GxvMNkhwOWIi3DEYF8wWDV4JwzMHPaLyjmJY5Nr_vu0II1OMnYoDn2Zb0igK5_k9Ysys1-X-exvOSL5NtDTGlsDkC_1GBWZuEJsX8n6-lh34s13_5S6gPRErO6p5oy6PWiS0Hb3kXzkm8mKzPyOvX2w-cfo-kFR52c42YRY0e7FM2cs1E7TyOJ9nmcPz1tF1jMs5LD-uH-bAxJEkKxiuNJPTg7enua2JfVTkzrXWTkDT5omdHEtXVu7gJzkKmjYj8O813qh0yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان ابراهیموویچ: "بین این دو باشگاه، این سوال پیش میاد که کدوم یکی احمق‌تره؟ لایپزیگ که پیشنهاد 100 میلیون پوندی رو رد کرد، یا رئال مادرید که 100 میلیون پوند برای این بازیکن معمولی پیشنهاد داد؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101937" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101936">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G562ryyYz5ZWxM-jAnOX4fVX7blFRQP3E1LWGCxPK8IlwQIfeJOiQMVWgXRUFpa8sZZ_F_7S8_s-KI7XKTUxYoVVAtSXar3aNSfel2tw1GGY6r4qIFZ79mL13HVyjTzD1SA5Bxknq_bv35yxO66bcO9o8DualVI9d2ZkjMrHnJ34hWocNTyANvqBSDy562KFBEDDNJpCZrMFLZ5HNgJLgT-xBYaRi4pv6olOXB-yyRQupvggFQ_LxNb2SKDqeG5DmEqMu5QLFeE_F4l-byaxpK2FQKt92THpo-wYNzsMmtN1nGFAUJoDm018BNxv5xgpjvq_pB3oo0jhnq-I39JxEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال
پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101936" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
