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
<img src="https://cdn4.telesco.pe/file/EDjlUR64-7dtKS-Oqj-V1mDVdO_ARXiQr5tJC7WCZfydz_qiYjUmtrfaN6bhScpqZ2D6Zswanz6PZFQ1eGHMXXVnRQXf2Zh0mKDt89u192-qE0o7MYI3UtZA1DDY9OhsOJ_K62ps8A06TLqZrnuE0yegN8gmvR5DQmA06R71K4Sg3Iog_8RZAhkH_K0XkGU826I_st6A6TpRfqcE3aQYnVk88bCY7c5Vr3u4kYb7B2VAdcyRBzMdi4k-yVXZuS3vvIHXbsB5kUKK526cb149NZpsaiiH1A5lVIvMjYiH_vD2aztnb11IL8fXifJnbbKVPuyuhpm58PtskigT-UjP1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 177K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 13:15:45</div>
<hr>

<div class="tg-post" id="msg-76620">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/endSKoAJmW0Xr8vsPE8IaHa3UQSX5qakWrARgeujDvz-8sjM5Ly83mNv99MpXO5TzUAOC5Nw_xsoKPDVFSu9ftELzdpA0RunbemRA_1SvzRdFQ2PpxqeeQ5iJ-oZuqewlob0pWY6WJqfslzHLUm3a-V0oklaCdiMHAtuig93As2mD9sCRmz4LsfSnia_ODkNf2zw-FKlHXKIBDalUYM7IUyrceYPbR7Aurxzmis_Bqlwbi9M0Y2NhFsGdhu8TTKq9gM9Et066TCEIaP9fQvTen6lUwywx81TfyaDwMApW6M5eLjRLT-nJX4rBW7h1H3Z8mMklLspvSjzP-o9PURrhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل دستور تخلیه کل نبطیه رو صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 916 · <a href="https://t.me/funhiphop/76620" target="_blank">📅 13:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">من که میدونم نصف پسرا برا دختر بازی رفتن  @FuunHipHop | ALI</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/funhiphop/76619" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🍓🦢</strong></div>
<div class="tg-text">میشه اینقدر با مزه بازی در نیاری این بچه یه سال تو اتاق درس خونده رفته برا حقش دختر بازیو جا دیگه هم می تونه با اینکه کنکوری نیستم قشنگ نبود حرفتون</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/funhiphop/76618" target="_blank">📅 12:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76617">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هم اکنون آغاز تجمع دانش آموزان مخالف تاثیر قطعی معدل  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/funhiphop/76617" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d5a4fd22.mp4?token=YXiLTmQwjAX1AIh8lAMBxAlGl9foSkbVSWsPYES6LysVTSbL621qRtcnSEl6RfbN8zHYLnKQjRWi3j83pXfbkBfQkdwjozSWnanmuUh2tX4viVSkLNz-NLtJO9tadtA-FhBaub3uoxziPVnfs5XgJ6cOPNAnUo02yErLVp2TPBYOPoh2LTbHXr3jaSA4TfIym03YNeoKpTvXMRAWaooajkbXW_2ANzzw2SDEy9Oc5m-FFT3C6A2r6bGpfvCumB0eBKRuqqyjUqSXlBtHjm3TMD1Y-eZwmvLlTDOlaG-fDRLg6A0CajwupuMcAiMlRzBoKHuuiyWi-4geBG4igL7M-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d5a4fd22.mp4?token=YXiLTmQwjAX1AIh8lAMBxAlGl9foSkbVSWsPYES6LysVTSbL621qRtcnSEl6RfbN8zHYLnKQjRWi3j83pXfbkBfQkdwjozSWnanmuUh2tX4viVSkLNz-NLtJO9tadtA-FhBaub3uoxziPVnfs5XgJ6cOPNAnUo02yErLVp2TPBYOPoh2LTbHXr3jaSA4TfIym03YNeoKpTvXMRAWaooajkbXW_2ANzzw2SDEy9Oc5m-FFT3C6A2r6bGpfvCumB0eBKRuqqyjUqSXlBtHjm3TMD1Y-eZwmvLlTDOlaG-fDRLg6A0CajwupuMcAiMlRzBoKHuuiyWi-4geBG4igL7M-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون آغاز تجمع دانش آموزان مخالف تاثیر قطعی معدل
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/76616" target="_blank">📅 12:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/funhiphop/76615" target="_blank">📅 12:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76614">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYoung Roque</strong></div>
<div class="tg-text">حاجی توافق شد؟؟؟
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/funhiphop/76614" target="_blank">📅 12:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76613">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdruOFXUk0TIiaeG1GWHu8R7-mc9wIdnmDo0Lk-OW0TtDo-ZYdgZYafWckd628HW0FN3y2lyTdSMRG7ZaZp7m98nOsFiXlY1yDSnxe0m0q6NV48wysN98T30TUCusu1HZgiwjYtKsqQwhAmbFyY2kBdZxSmwyr851ia0T3Woq_x8SarfhE-nkc0sXvBT-1aoh1VSDo2p_w9YDvadU_hcLzNTJib_bwDHqlqHYDrNIPgTxSk_3BJlpbPUpX9Igek6MhJLs0m_gZ4-T6ruDHi5BNVkqkpUheeoE3nzIlobJ9AsNhAHpe-Q3zdvlA2BpTUOWjr0e7Wv2c3FNxPdOK3E5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس: ترامپ به نتانیاهو گفته تو یه دیوونه روانی خل و چل هستی, اگه من نبودم تا حالا صدبار کرده بودنت تو زندان همین الان حملات به بیروت رو متوقف کن  @Funhiphop | ALI</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/funhiphop/76613" target="_blank">📅 12:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76612">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دانش آموزان الان در مقابل وزارت آموزش و پرورش مشغول اعتراض هستند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/funhiphop/76612" target="_blank">📅 12:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آکسیوس:
ترامپ به نتانیاهو گفته تو یه
دیوونه روانی خل و چل
هستی, اگه من نبودم تا حالا صدبار کرده بودنت تو زندان
همین الان حملات به بیروت رو متوقف کن
@Funhiphop
| ALI</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/funhiphop/76611" target="_blank">📅 11:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76610">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSAGQ6C9pckAg_N1FoOoejVv5gG1QHxfvLLDUlZik8Erszp83IqqdhZk0uTe-_34pTR66FYCcwXZayLPONOcM02--QupfI_tRcpl_S9PwsJJ0o3QHXWDMhQobOMmJHvVr2gmbYR7Hx6J6MgLZkGM8-ONzGr9gXVz1uHJaE2uRsMeccxDiYIilo8uB_wN8ghNDDqggXfMInzhjG9I1VjGdAT4R-bopg853oc0oB9LGS43IlgHB5NR_AcUUcAVNUKFt5KAe3RnRH0fjr387CwbFrUZXRJ90CznJGQf6nfqZBYX5i0bWm0_7m7AT9g0VsXcj2uv148znnuIu595SrLF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیر دیگه مادرجنده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/funhiphop/76610" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76609">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBbNN6APDtArErh9pF2LaYbRmT8TF-Pt4tgIfypioT88pyghGdCFItbspTw6P4YMvwybqgaScndN1PPzVqZ1YX8R2eVueUmIrlHD1XBHemF38pwHggTFMWdntZ6p7AoAbHmLNYtqB40GOV3-QrKjgVsBcmxRxiZNCcmvLMcfs5mLGrpdhbMrfwZzHTSLmIvegf0fg3on6-iVeCTUJ7hI1bQfyUCsA2bxwC--hh3lziFEe-tykOQXpoWB9K-xPB5qkFiTQS3B1Umabl1LHmvGiihv3rQbceMbqQwxEyvcl1Smmh2Gut3mn7p91RFWCUtq3xJP9bawSBJaqu5bWRktHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون شبی که تل آویو اینجوری روشن بشه روز عید ماست !!
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/funhiphop/76609" target="_blank">📅 10:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76608">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbTQNgGrx2gCL3ODUZ6i--O-h1c6DffhEii81l2U2_fJ99W0C8yXWFSv5BS3s6-t73yqoolDykOE2_Ayn-Rodq3knjQm-66bJi1XonJuzQdIyuZkgwsy25c3QaMlRDJfG-23NPUIk8K7dy5R-6kli2E0FCCKe5jSV-Dv1ZxS2FJnM_ufOxwYqawg5da8r-KO688BD_RIASYFdwVNLp40xgkB8-8cBudQiFsfSJGgsacuBxn-wiijPYJJRdtTZHotKy9pjjlWdidW01YYlnFZl8vVrNDIa5kt-n74IMC7kznwCo5LpGiDucSQue5HCcRM0e41f0-DyAqJ0wGZebpJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت رو بخونید و به پروفایلش دقت نکنید.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/funhiphop/76608" target="_blank">📅 10:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76607">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76607" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76607" target="_blank">📅 10:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76606">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXBDdCnvrs22ZeDsfJem8-o-wUs9T1KCBL6C77LVjMyCAv257S8OUZXC8K_fpPQp5AIecT4AxNBTmvoI2pa-viFfkE-4GsacjKi_6hW6c2w-6sGJU6oMyfUzL_lkvlLKPxN5pzqXbRCNCGsiQe-ZdLJ7DuQBjFzYxnq7m5kxJ-3EHLxCLmzRC5FR8DL25QBl6lf3E0OSrln79ltCv3cbIv9bw4fgwS0mryKjU9t_n6t5cu70-kHF_5ERPYNU1sQfaw9Se6UDms5H7_nxvD-cen3vKKGmKc3tlDi9IjiMLGTt0WV91W-gk9d7jy-JuxcA9s8NwTS657bIu3nSZ36mdw.jpg" alt="photo" loading="lazy"/></div>
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
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r12
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76606" target="_blank">📅 10:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76605">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جدی جدی یه لحظه داشتم فک میکردم بیبی و ترامپ با هم دعواشون شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/funhiphop/76605" target="_blank">📅 09:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76604">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">امشب، امشب دیگه آتش بس نقض میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76604" target="_blank">📅 08:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">م   ج   :
ممکن است طی هفته‌ی آینده به توافق برسیم.
یک توافق صلح با ایران می‌تواند حتی بهتر از یک پیروزی نظامی باشد.
من هنوز با این توافق موافقت نکرده‌ام و هنوز باید چند امتیاز دیگر را بگیرم.
امروز یک مشکل کوچک پیش آمد — ایرانی‌ها از حملات اسرائیل به لبنان ناراحت بودند.
پس من با حزب‌الله صحبت کردم و گفتم شلیک نکنید، و با بیبی صحبت کردم و گفتم شلیک نکنید، و هر دو از شلیک به یکدیگر دست کشیدند.
🥰
😊
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76601" target="_blank">📅 01:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXFuVBt3fNowM9uYqr91u6BfvLF7C5MZFpullQx0Ux4EsJS2TwGr_7zbRVGyqphZRjjt93ANX-1ItvtBCUamSnKsHp95C1tqXY8q-vf2PIWrQN8kcjbhI_4EoAFbPwzF3P0lUkQ8Z35-soTDmyk30aT6eD28veRtgMPWQ21Am1R0Bg7vBSjBAwliEJTH4yJFy-oMnDN24jnqznWUenZhCmk_45Lmjma7SCRDTh9mRWua04FKiLpPTM45jKkL2_uoJ_-x5GK74QiCMhfmQLpA_ngPk7KFQPeRJoh36eLe5J6AdDGxQNi15KBnyI9tY18Vvf1whdfKhknono8CAADjuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع دانش آموزا فردا برای مثبت شدن تاثیر معدل یازدهم تو کنکور
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76600" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این آتش‌بس ما چرا نصف شبا رفع فیلتر میشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76599" target="_blank">📅 00:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حزب‌الله پیشنهاد آتش‌بس جزئی ترامپ را رد کرد
نماینده حزب‌الله در پارلمان لبنان اعلام کرد که پیشنهاد آمریکا مبنی بر توقف عملیات مقاومت در مقابل عدم حمله اسرائیل به ضاحیه جنوبی بیروت غیرقابل قبول است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76598" target="_blank">📅 00:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نتانیاهو:
امشب با رئیس‌جمهور ترامپ صحبت کردم و به او گفتم اگر حزب‌الله دست از حمله به شهرها و شهروندان ما برندارد، اسرائیل اهداف تروریستی در بیروت را هدف قرار خواهد داد.
این موضع ما ثابت است.
همزمان، ارتش اسرائیل به عملیات برنامه‌ریزی‌شده خود در جنوب لبنان ادامه خواهد داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76596" target="_blank">📅 23:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزیر دفاع اسرائیل:
واشنگتن ما را از دفاع از شهرهای شمالی باز نمی‌دارد و به هر جایی که در لبنان لازم باشد می‌رسیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76595" target="_blank">📅 22:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76592">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تشکر و قدردانی حصین از بچهای سپاه قدس که امین منیجر پخش کرد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76592" target="_blank">📅 22:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76591">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏تحرک جت های جنگنده در تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76591" target="_blank">📅 21:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76590">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرگزاری تسنیم: ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند  عزم نیروهای مسلح ایران و تمام محورهای جبهه مقاومت برای واکنش به جنایات صهیونیستها و گشودن جبهه‌های جدید
▪️
کسب اطلاع تسنیم حاکیست که با توجه به تداوم جنایات رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76590" target="_blank">📅 21:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76589">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حزب الله پنج دقیقه بعد از توییت ترامپ به شمال اسرائیل حمله راکتی کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76589" target="_blank">📅 21:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دقت کردید که الگوی آتش بس لبنان هم دقیقا مثل الگوی آتش بس جنگ ۴۰ روزه بود؟
آتش بس بعد از یک تهدید بزرگ
احساس میکنم همه چیز داره طبق برنامه پیش میره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76587" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: مذاکرات با سرعت بالایی با جمهوری اسلامی ایران ادامه دارد.
@FuunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76586" target="_blank">📅 21:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76585">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">توئیت جدید ترامپ:
من یک تماس بسیار سازنده با نخست‌وزیر بیبی نتانیاهو، از اسرائیل، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد، و هر نیرویی که در راه بود، قبلاً بازگردانده شده است. همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت کردند که تمام تیراندازی‌ها متوقف شود — اسرائیل به آنها حمله نخواهد کرد و آنها نیز به اسرائیل حمله نخواهند کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76585" target="_blank">📅 21:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یادتون باشه ترامپ داره یک شطرنج ۶۰ بعدی رو بازی میکنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76584" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرگزاری تسنیم:
اسرائیل از ترس ایران به بیروت حمله نکرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76583" target="_blank">📅 20:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
اگر حمله به لبنان متوقف شود امکان از سرگیری حمله به جمهوری اسلامی بیشتر میشود
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76582" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کان نیوز  رسانه معتبر اسراییلی :
ارتش اسرائیل قصد داشت یه حمله شدید و سنگین به منطقه جنوبی بیروت انجام بده، اما تو آخرین لحظات بعد از دخالت آمریکا، این حمله لغو شد
گزارش ها حاکی از خایه کردن ترامپ می باشد.
@FuunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76581" target="_blank">📅 20:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76580">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تلویزیون ارتش اسرائیل:
عقب نشینی میکنیم
ای ترامپ کصکش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76580" target="_blank">📅 20:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76579">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رسانه i24News :
آمریکا حمله به بیروت رو متوقف کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76579" target="_blank">📅 20:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76578">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اگه دنبال کانفیگ با سرعت و قیمت مناسب میگردید از این بات استفاده کنید داره گیگی 3 هزار با سرعت خدا میفروشه:
@vipamomamadconfig_bot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76578" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76577">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تون مادرجنده از ترامپ غیرقابل پیشبینی تره
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76577" target="_blank">📅 20:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76576">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWY-9Ad2m6j6UFY95Ody_SPP3paznaDeS4r8hRiSRXfg5p-LyWT-1GjOyXKFCNiNMreLy02UsU5eKxOuB2P9pTg7wVPQDN_ssOG8nwY4T03ecwCHjFhaCYBvoWhtfo2L7HBTwQyTkeQGY1VdQzpOAUi28LfrKW9IH1_VqprzA9sPShKfcvWWldQICulzAOmMofuep0LQay161znWGPL3VtgyC5qKZcivhvOGFUjlDHJSju_tAXSI-ta2RtnDrFaqEtnK8OSSOV0xEa-9bDK3tssoQbmH4P1a2uPA0r4wuoN92oH-9khfSts08GQpw6f7aW_rsLhojtqYA63foFY9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترویس اسکات دیشب تو ترکیه کنسرت داشته، جای خودش یه سیاه پوست دیگه رو فرستاده براشون بخونه و نصف مردم اصلا نفهمیدن خودش نیست  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76576" target="_blank">📅 19:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76575">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ولی ناموسا الان ساعت 4:25 ظهر
با کانفیگ علی وصلم و سرعت ایده آلی داره</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76575" target="_blank">📅 19:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76574">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانفیگ گیگی 2 میلیون موجود  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76574" target="_blank">📅 19:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76573">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یکی به علی عبدالهی یادآوری کنه عاقبت کسایی که برای اسرائیل رجز میخوندن چیشد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76573" target="_blank">📅 19:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76572">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">علی عبدالهی، فرمانده قرارگاه خاتم‌الانبیا:  اگر اسرائیل ضاحیه رو بمباران کنه، به شمال اسرائیل حمله می‌کنیم.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76572" target="_blank">📅 19:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">علی عبدالهی، فرمانده قرارگاه خاتم‌الانبیا:
اگر اسرائیل ضاحیه رو بمباران کنه، به شمال اسرائیل حمله می‌کنیم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76571" target="_blank">📅 19:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcheELuedRslSjUVja9CEYbjzQj8vqNIV-jF0IDb032Fa3G8vEq_dRfOzP61rQWK0bVXeRj-RYmoGjhq0sYz9tpkvo4aiOV8wYGfa1H4Xv3LkU4-wmmFlZlbXtk2iwMW3JVQ_ZEUsEZcC1cVuWVxbHGRdy1q0bT1bmvw6uUBBcJHkzRFN3_9hZ7jcV2uKtmQhZuZtxGuiTvAju_2w7gzJ9fQTj5uK9F9qI5YKu4bbm-xltDKIaKFWTzbhdPVfxxWJE9960bdbdZbhwdN-HsJFyglVaEYOm70qz2ALsRxVGa0xDAVaaca-O6JBN-3mg6BzpPzZc72hGIx9Mz2MbRHGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جهت حصول اطمینان اسرائیل از روند به شدت مثبت مذاکرات، الان ارتش اسرائیل برا جنوب پایتخت لبنان دستور تخلیه کامل داد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76570" target="_blank">📅 18:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دفتر عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داده است که احتمالاً یک حمله موشکی به یک کشتی تجاری در خلیج فارس شمالی، ۴۰ مایل دریایی جنوب شرقی ام قصر عراق رخ داده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76569" target="_blank">📅 18:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e1df4a9c.mp4?token=u6Wpw6mX6uI5HuINxK53ZXwlDPwwCJZ0GW0I6fbtUlKgrSWTMrfY9YA6pYAJ5-2FjYmFeDaXHG88sVGx8KmjQ14lLAGvciK224Q_cCfUDD1lT-n8oBL94g-KXHIMzwfIXIIrvoOGB1ni1BXWYSCw2mTVkIIGc9eQkEo01JizEbgvoeuy5MysjrJJQulkmUqYTAXxFHwtj__q0WcoVgWyw5ipxGfb1AFS0czEki315p9PW4eR0mnMYlGwN7oebhUOFhH06G1LSOwhtadDcOgX5XL1bl9PhZonvOK-FOYO5cVu03YK90iv72cYFXJdSdOgpKOy9n22m4IGZJEZNB5lTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e1df4a9c.mp4?token=u6Wpw6mX6uI5HuINxK53ZXwlDPwwCJZ0GW0I6fbtUlKgrSWTMrfY9YA6pYAJ5-2FjYmFeDaXHG88sVGx8KmjQ14lLAGvciK224Q_cCfUDD1lT-n8oBL94g-KXHIMzwfIXIIrvoOGB1ni1BXWYSCw2mTVkIIGc9eQkEo01JizEbgvoeuy5MysjrJJQulkmUqYTAXxFHwtj__q0WcoVgWyw5ipxGfb1AFS0czEki315p9PW4eR0mnMYlGwN7oebhUOFhH06G1LSOwhtadDcOgX5XL1bl9PhZonvOK-FOYO5cVu03YK90iv72cYFXJdSdOgpKOy9n22m4IGZJEZNB5lTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوه قضاییه: مهرداد محمدی‌نیا و اشکان مالکی رو به جرم آتش زدن مسجد، تخریب اموال عمومی، مسدود کردن خیابان ها و درگیری با مامورین امنیت صبح امروز اعدام شدن.  @FunHipHop | TemSah</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76568" target="_blank">📅 18:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فدایی تو تجمعات پاریس  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76567" target="_blank">📅 18:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b05997ae5b.mp4?token=lDCN2vl2R9eWMQNpuIRQor5UNS1COLD_b6uo7CsfH0LTjRRSxsOf0rIn3JyxnfVhInRD4VeSqMj_SS2-LJRk_OGgDwChZz3TI7Ky6NE9RFDscO0FfYi0Y79G9XQlgobPFinLtFWbZ-cMyGdNbx7pbmlzxtgpxwLjzlvGJIz9v5ospvVqD7rLvOhTnevMbn7dtI2aR2rbBYGUxJHe8fOBEthjNZNuTmJ0qnq5g1pdDl3neMPxg4yCIDhRuwyYTGmio8D_v_p_KXnRbZxvenX6Vu0zJXdQwJTPwdwsKumxF55jtSOHZnX0igcGORyWQaQnBD2bIJJM594rF8WEnaGX0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b05997ae5b.mp4?token=lDCN2vl2R9eWMQNpuIRQor5UNS1COLD_b6uo7CsfH0LTjRRSxsOf0rIn3JyxnfVhInRD4VeSqMj_SS2-LJRk_OGgDwChZz3TI7Ky6NE9RFDscO0FfYi0Y79G9XQlgobPFinLtFWbZ-cMyGdNbx7pbmlzxtgpxwLjzlvGJIz9v5ospvVqD7rLvOhTnevMbn7dtI2aR2rbBYGUxJHe8fOBEthjNZNuTmJ0qnq5g1pdDl3neMPxg4yCIDhRuwyYTGmio8D_v_p_KXnRbZxvenX6Vu0zJXdQwJTPwdwsKumxF55jtSOHZnX0igcGORyWQaQnBD2bIJJM594rF8WEnaGX0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فدایی تو تجمعات پاریس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76566" target="_blank">📅 18:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">با اخباری که از سمت خبرگزاری های داخلی میاد بیرون
منتظر پرواز دلار به سوی بینهایت و فراترازآن باشید
@FunHiphop
| ALI</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76565" target="_blank">📅 17:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzBSfnhlUrXuS2yDVm9KB_AkpYFY03uz59h1HTx25ApXtsUk6fg7uBLSUVjk4Xjd_ZNPjSf1_Cli09-m2lWTsSEh_NTW8Spm0LalsvIyB0RSAvtlmYkUWWoELeGtG4WaQABG648IHsG3_nyPHh0-pZV3iNeKcfZnHMqWruTRKEQyS0CqTjCJ5dG41CQD3eGtW41TGNekN8Hhdi-Rj4JkkzmQo54wvaRIoSRfdlfngG-zvkKVdXGUQ5_bHxW9t9cmUQwAG80BYoi3x8wKorIySWWmuKtpYhw-oSUfCXMAwp0RbUOYYXASpqHJq2eG5PgKi-Iqfvu3ya9Ijl4bHdZQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پنالتی هرموقع یادم میاد تخم میکنم.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76564" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76563">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhPujhlD2TEfko7HYl0CX0mu3Vl3n2NvY-7rmwDv5Bem41fB9Lkrq0sdRCfiHl-Tf6__K8njQfW1BQz7k_LJ60b-BRV3FCML_QhadCFZEuuPM48gtu3Jq6jsOv8VhYqJTLAX0Zlgh0Ntw89ebe1ukV_ErOVFCHz4v0pmMx2pcKMmL3FJFSxjvurLhUjkBF8r55PAhSTwlIsKc3ER-3VY9eTPzKGfzvT1-kd_ci5SIyYzeEnGZ8KdsGHDUDxCPXPdjzYY5laq_vuwOwQOvInI2Ytj-vtc7oBiVIrEcNEhow6lF0y1WaN1cXPFf1OHdaYdQ20A4WpLZDkB94NFLHDHZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرجنده چجوری روت شد با این وضعیت نت همچین پیامی بدی؟
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76563" target="_blank">📅 17:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76562">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlY0WKX15eZZrWMggZFrYkekOj17jetatjekjAa_sBa9eGa0dutQ9Q1r3CZq56DADVn5OkDKkV-dWaYFRYCKHt-AxupJdsWqpeseL3tlxivY-q_TrwbvDHu4_LIQ3pN7dKJAGrW0iNVHTZGdq4Ig9o3RfuMeHXjLOeY1pkABU2-DhjQGH-ZWaGXO53EpVZd7kNxBwPSTToeTdMFcF4qWtUbiAvZblwb-tAfX5JvkHqNOA0Of06BunhdbBRqlERE7-98HKFAtmhA0-W0s40EF4VFswlBJ9iO8YNqVyzgNXLJL7U8sbWrA7IG0h-1FV9ps-dCg3PulbUo8OMnkwCLliw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g11
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76562" target="_blank">📅 17:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/islRATZdIZQReX8VD1I3ERQyWi9UnA8jEtpRsazqQSQLwxIFeDfWxNTxfXNhFlUYZ1GzIdE8oepC6eHFEjIibuwBazLzBWvtBdwfB6fbbKx9GUhaFv_YLxMjoO_PCzdDiOSxF1lYcXVjvv_2-C8y3EbzxpsmJr52YOMDxZRY7qTddF66m3P1MbvJ_5DLLUVhnLaavuvvmV8U0JgeAh6N0-I1SpeXDt1rZli50ifqXsOcDh783UdsaSHXhwvGOuCp9WGWma70TdR7dML2YQthodaybUBHrqw9M2itx3G5ncVE7thLsmwHavzHsuBz6zWCeyKl5TEBiURIsqRNXLwjFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم: ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند  عزم نیروهای مسلح ایران و تمام محورهای جبهه مقاومت برای واکنش به جنایات صهیونیستها و گشودن جبهه‌های جدید
▪️
کسب اطلاع تسنیم حاکیست که با توجه به تداوم جنایات رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76561" target="_blank">📅 17:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شبکه 15 اسرائیل:
ایران تو شروط مذاکرات علاوه بر لبنان، غزه رو هم اضافه کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76560" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری تسنیم:
ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند
عزم نیروهای مسلح ایران و تمام محورهای جبهه مقاومت برای واکنش به جنایات صهیونیستها و گشودن جبهه‌های جدید
▪️
کسب اطلاع تسنیم حاکیست که با توجه به تداوم جنایات رژیم صهیونیستی در لبنان و با عنایت به اینکه لبنان جزو پیش شرطهای آتش‌بس بوده است و هم اینک این آتش‌بس در همه جبهه‌ها از جمله لبنان نقض شده است، تیم مذاکره‌کننده ایرانی «گفتگوها و تبادل متون از طریق میانجی» را متوقف می‌کند.
▪️
توقف فوری عملیات تجاوزکارانه و وحشیانه ارتش رژیم صهیونیستی در غزه و لبنان و ضرورت عقب‌نشینی کامل رژیم از مناطق اشغال شده در لبنان، مورد تاکید مسئولان و مذاکره‌کنندگان ایرانی قرار گرفته و تا زمانی که نظر ایران و مقاومت در این زمینه تامین نشود، گفتگویی در کار نخواهد بود.
▪️
همچنین، جبهه مقاومت و ایران عزم خود را برای انسداد کامل تنگه هرمز، و فعال کردن سایر جبهه‌ها از جمله تنگه باب‌المندب، به منظور تنبیه صهیونیستها و حامیانش در دستور کار قرار داده‌اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76559" target="_blank">📅 17:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76558">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">منابع داخلی میگن مذاکره گوز شد توش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76558" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76557">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UePJU7leLVMrcIwOMmXjFb1tNr3uz8kNGfO4iWgXRxlCE2rlqyI3URm3o2LuZiPm5OdtB7Izisjtg-UQMRF_KDpdrtrDeL_pRWX64kw2fdyAkKspjoTcYTjFIu7lHBZtRwe-Db-NNuUYovKzc9nA710HTAxvc0ba2lcffXCRdhwLwFpQG16R4dnGMoc9Nv2hRr8xLJVPmxfANyxvZNA_rgBjo2LiZgAs81N5ec9nFi-_Lt8E9504nzUMIB-Aguua83pjGw8Lp9eGzBvyRP3lkM-UlhzA1CAprD5mljEVIrYk7LgYLmXqtLddMNEaCGUYmgZdN7I2vkzn98D8alQ6TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری رخ
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76557" target="_blank">📅 17:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIezrgMpFEcSuqgDFHZvAGKeJebPZIVwjKy82fCt2alALLO4n3gHsBUXXoycmV8QX4OGpPqEe-A-zYgxxxzn3D6F8oMCBmVWBn9lvH21b2de6FE2hVcv-5b3sXiuexizvp4nWtiiB3mj_ciS8bZB3-G3VsfO2zFkSxbhvCippZDJrXsFiHLfb6s5TRyBfyXE7qpfCoxBtUHADjHKp38nPCpV9LoleOMUpt9-StFBuSlE4LDkFzyVnaFE_WmuslSTcI8cnmD32JLbqahlcawH5kTsfZxqcStTAOAsh2VaX2Gevspr4z9ORVysgpUGAD4F5JyzS9gPzbXe66bsztku7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوزو انداختن وسط کفتارا.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76556" target="_blank">📅 16:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دعوت تتلو به جام جهانی مطالبه ملی ماست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76555" target="_blank">📅 16:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آمار رسمی تورم اردیبهشت 1405 منتشر نشده.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76554" target="_blank">📅 15:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76553">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تتلو بعد از دعوت نشدن به تیم ملی:
کس ننه قلعه نویی
👿
۷۸!
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76553" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76552">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7UlvDIB9aj7ANxENkgTU5NqJ25lZ31PxDmZU9csycd-1ejnVxl4WWmTxlt9NqYERkkUx8d2ohGxT06lHkvqdYyavJme_wmcoSXSRIMaJhHvlJ8w80SsGNqVqlktczyBwmIxft_A2XtjzZlUMAcg_xTLGs2-dFjTxNOQP5sRjwk8ts2W7TN3E3ojvllsLhxLf1HkDiRkZHSqNEAw3WQorZwnAJgBumnMy4XkmjSLCBYWD7tyT43p4MA1ePWvtVtddGwwR21OblvCQMnqjNQJd8v_i74U-CYUkXL-8PmhwKdfbueOzlrnLZoBqshdwjv2lYo2Fg_EREkygGW3uNzEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست نهایی بازیکنان جمهوری اسلامی برای جام جهانی
پ.ن: حضور مهدی قایدی و خط خوردن سردار آزمون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76552" target="_blank">📅 15:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">باقر جون چرا داره یجور رفتار میکنه انگار من پشت پرده لبنانو فروختم صداشم در نیاوردم</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76551" target="_blank">📅 15:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترویس اسکات دیشب تو ترکیه کنسرت داشته، جای خودش یه سیاه پوست دیگه رو فرستاده براشون بخونه و نصف مردم اصلا نفهمیدن خودش نیست
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76550" target="_blank">📅 15:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76549">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyUxJPxoQ7rJpmJUfxuJviOxeMNzhE3mgq465ZE93WxrBDWxUB6gvSqosvFA0qbRa5aTtrY1c1n-TyajJqctroz8WVhaPfNmTTFY6Luhpq55dp_R0xXjJ3vOesAdZBvH60d5AQGWYf1qfk1ViM8_bez096TKZdtCdj_HfaBTHJBjqg9tietlQHXhbjWB_XaGg3ikp0fy6dBLE8HwNJXCYl4Bz8LtlWoYFkmSvERTM5-qqWF3W_vDmiM4mJM-cV3o5n7sGaENXDgTb91qenDlG8QsxiYX9hZyC8x6VnWyJeLkJ3a6zrYEoENZcWp77mMe7vuJpdcn6co-UURGUUpnvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرفسور
عراقچی: نقض آتش بس در یک جبهه، نقض آتش‌بس در تمام جبهه‌هاست
آتش‌بس میان ایران و  آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.
نقض این آتش‌بس در هر یک از جبهه‌ها، به منزلۀ نقض آن در تمامی جبهه‌هاست.
آمریکا و اسرائیل مسئول پیامدهای هرگونه نقض این آتش‌بس خواهند بود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76549" target="_blank">📅 15:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76548">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حاجی اسرائیل داره لبنان و میفرسته قشنگ 1400 سال پیشا
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76548" target="_blank">📅 14:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76546">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hT90PO6jXXfZc8feTnTYSFZGyMrK64kmLqWWJTtzyvB1Z69zPcvwY921OlCuApBmaiGBlMdgp30Ii6YqoMCvXLn3SwjlzF2R4DSFCiS2rPhtq5Zg9siVcezsVVbfifRd1s_lXkuYWvzU5ZjMIWoe6hynFYjAixHcKF25EWMzDdWRlVDI57D-MNgCZ3VJvbJ7XOlLT2ywsnqmvkWZEICSh5_-fSpKhbu_x4fHdCYN6gBUXeWNw0PP1pwwHyobLDx9Qx-oZRJQs1EH-lT6Jxy0ldAZgVmmwa4MKxHiFbD0xUEz0bZ1p2vCTw8kK0aFShnDdXzZ9H2Nnwae_ilgS5WuXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8lnMDmsFNmqG_MUrfSBjlLMWQCa37shyw8mg80V4fPQDCNpwbfYQSbQ3xLbufioJH2SjKjdtz9ZveggQoZZ7LbTghDlXGyVuFrIXskK_L1MYcqntalRO5Gzkvcz6np7CSoAr800RdpV7UoBaDpOnKsSeqFg1hO1bNi5c6oJh79TrhgjxRdgobUpgABTuTuR4I6xjQzE9F-4lXU3AOWlT1gSVqmDMBxJ1HRdnWMrYCxOrLvVl-I89PEWD80wUYhIGnH5mWfEqZI5A-79Sq_6If-VhFyePc6icfqZNnIfEu9b47a2OMBTEl1VXKyBCDrM785xZuwkGvs4nkhPWalTKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همون همیشگی
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76546" target="_blank">📅 14:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76545">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یکی به من بگه این رسایی کیه
اصلا چیکارس تو مملکت
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76545" target="_blank">📅 14:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76544">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امروز تو دانشکده دندانپزشکی گزوین یه مرده زنشو که دانشجو بوده با تیر کشته بعدم همونجا خودکشی کرده   @FunHipHop | blue</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76544" target="_blank">📅 14:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76543">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">امروز تو دانشکده دندانپزشکی گزوین یه مرده زنشو که دانشجو بوده با تیر کشته بعدم همونجا خودکشی کرده
@FunHipHop
| blue</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76543" target="_blank">📅 13:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76542">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قالیباف:
محاصره دریایی و تشدید جنایات جنگی در لبنان توسط رژیم نسل کش صهیونیستی، گواه روشنی بر عدم پایبندی آمریکا به آتش بس است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76542" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76540">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ude_ATd3z4HMNUB4tC8MR_lyGFYx6E_4-75KvusBbnoKG6VKVCCc-xsMwMa2MIHrDQD0VpdDiwhur0fXs-qq6JBdujYWAKfXXSvHeZAnZ7oBBY7Cvux9GOvGnNis8rJu2quNiE93GvYqY3bDREwV2H_62QTkR_p4h2BhfQMtE1lv3yj38bN9Lxkhvv3ArljUwwbcNjpwT3OK6RKGACy12ZazntW2M4EkiKVm0ppMWCqY7a0hAa90RS-m3v8MJgYRvC6Opi8nMeFs3D2hWU_PH0Ycu_opp7f5Lg9eLmM7qN-5BNVhIEANVuX3XPVGZFPNaA_1qAFFajEIQ6kFWTdhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZU7t172-ndxJGMwnqzG05QL8M_IwE8uJuyePAWmKX2a2r5HaT4-MMvCOnovkDj6rDp_lmh_Aze_Q1ng8VHgWo_nVIv_UnbZ5msfnHwnG9w52scxJNgygvM3NOFrBQvtqFJcvNjz7LXZrY4_OZ6earjB01Jt2MDqeu3r8EqU3nigK49yVzoa-vL-pPEeIZxx6BFbiPyjFZr-HiILS-im7xGOhMkJBgmWZutjaiSoV4sV7FnHlaFX-_MKxT8JUvWbN7lgdIeNjUvzILPXXoj1TOojCQM9p1B9XElafLfEW56oWGrYYqnf_nMzGkXj2VPsCIWZcM1nFfmV_XNkJZ772A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هکرهای سپاه رفتن اکانت اینستاگرام جان اف. بنتیوِنیا، درجه‌دار ارشد ارتش آمریکا رو هک کردن و این عکس رو پست کردن.
پ.ن: یه بار دیگه‌ام زمان اوباما کاخ سفید رو هک کرده بودن و عکس علی رو گذاشته بودن.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76540" target="_blank">📅 11:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76538">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">من در کاخ سفید داشتم قدم میزدم ناگهان یک ایرانی از 300 متری به من سلام داد پس من تصمیم گرفتم به ایران 2 هفته مهلت بدهم
آنها آدم های فوق العاده باهوشی هستند ولی نباید سلاح هسته ای داشته باشند چون دیوانه اند و به محض تولید آن را به اسرائیل خواهند زد ما الان جذاب ترین کشور دنیا هستیم به پاپ بگویید کسمادرت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76538" target="_blank">📅 10:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76537">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تهران هم صدای جنگنده میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76537" target="_blank">📅 09:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76536">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noSVo2sjVMha_xHI5-MaYFsbrz8rQkzdgIib-R61I11i7zcE1Nj-aKG7J9NZBZfIt18Ss-K7EZABVu-KtoEYhPPqG-FovugczM1BRehKQsUm6axCxJAORC1GRESE7xcnCWMG8AbpX7s-lRjQXQaUMocJyQxz7HOZAasLth_5k6UNzAxkZUvP4fSC4g1hYiMjqpVHAHExw15CUQwNc9mq0jjMFMe6p8IOJRR3iX7bhocIgYz5T4gwNz0lyJ8NT_WNThLtRVsvGLLAhPc2RlgwvSUsPwcMVceHB3uE4plYVcZ6eEk9X6W9zjn1Gknrd1pq3BSi_6-lzd7HigjsXdBl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه: مهرداد محمدی‌نیا و اشکان مالکی رو به جرم آتش زدن مسجد، تخریب اموال عمومی، مسدود کردن خیابان ها و درگیری با مامورین امنیت صبح امروز اعدام شدن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76536" target="_blank">📅 09:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76535">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76535" target="_blank">📅 09:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76534">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOuf7f2gN96DAyTLIjQgyq-WI8pNwy6DK2QePG_HjVlH4st3fWdGp9lwBIKScgoRkaHUgLShs6BTvoe0TaL7c26Sy_iVvBlZFSAgfkwKCkhtp1vDQCNUfFuYt3n2ZUwmqX_CdqeEfmEY-WGYiA1tT2Dx8Zm0uRA1YY8JR5GjLUjTcva0b3suaQBT0GEybZo-N2envU_KxmXg-4SdiNzRcd9gkq_aR7kNPhUQxaV0J6LlEhx2yAl8krax3HOUeaykrBYiFUoq9ogk7YA07ymjVhuQsa4_tVRfWCIS-JemtR4XxVEumm6EzJlwFBuHgSyIBM3jM-U8xoJ2Foo1nAeqmg.jpg" alt="photo" loading="lazy"/></div>
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
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r11
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76534" target="_blank">📅 09:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76532">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بندر عباس انفجار
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76532" target="_blank">📅 09:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76531">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3286M6pt2CGti8ufpUjbA9QMLjU5Anfy1hsx8WvxJHsdFuQxeD21x76SyY-Ntkqi-id21NHmTP6olCJszlKnAL01i7Hx2o_bBcYXRWuHakSxEhppNPmYFzIrO3g7d0YAlqvFEA-ZmFCdstX67d9ydRpLXmtj5HbLWcy0FF53Y9Yrxt6F7SkgZgWYkV_FG_bWoaR_NJaRpuhdno4E7jaGcDkmWqrBTVM22V3IP4CpIrkfOIiiSyrhg0vuneMVvBb8xlCEoBsWk5h4TUWojodiQat50BuojR0WQECGPnG9nv-BDrnLdy2sDBVrmYhx0SiE3iXkdrh-f7FF_N6IBtWGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ خ       :
ایران واقعاً می‌خواهد به توافق برسد، و این توافق برای ایالات متحده و کسانی که با ما هستند، خوب خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهان ظاهراً غیرمیهن‌پرست نمی‌فهمند که انجام درست کار من و مذاکره برایم بسیار سخت‌تر است وقتی که سیاست‌بازان به طور مکرر و با سطحی بی‌سابقه منفی «جیک‌جیک» می‌کنند که باید سریع‌تر حرکت کنم، یا کندتر، یا به جنگ بروم، یا نروم، یا هر چیز دیگری.
فقط بنشینید و آرام باشید، همه چیز در نهایت خوب پیش خواهد رفت - همیشه همینطور بوده است!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76531" target="_blank">📅 08:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76530">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وقتتون بخیر، امیدیه هستم و صدای دوتا انفجار شدید ساعت 8:33 اومدش.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76530" target="_blank">📅 08:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76528">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سپاه:
آمریکا به یه دکل مخابراتی ما تو جزیره سیریک حمله کرد؛
ما هم درجواب، پایگاه هوایی‌ که این حمله از اون انجام شده بود رو مورد هدف قرار دادیم و اهداف موردنظر را منهدم کردیم.
هشدار می‌دیم؛ اگه این حملات دوباره تکرار بشه، پاسخ بعدی  ما بسیار شدیدتر خواهد بود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76528" target="_blank">📅 08:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76527">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Phy3oewnumhyBTbEOjfSsm6ZEJ-bCS1-DFmyRD_D5nr6Gybk-SMpqNLQNm3MVeN2-x0HsEOQF6PMjg2J_non2q5Nicg4eHHQemTQUmHEiC9FXWo1Ttp1HxoyhaElgqz54R2TR8FrRM--cgDqi8nmqsjKWnfxakHBjPM69usMNhBWqpsAygJAUH7l5ecGqadSk1dEXkCDNRW_uWXnlKN68zN-BNFnZ5USCL2Ndt_g1uZAnGDFWJooM6ts6qyyKcpAhfqwkjCpn6fU6WqzP1AKvbnYpkssbNasfK3EytAoM-7Hr0fnMwxOuq1uJ0gO-OmUWaZZqrQPHJZSBGEC7e6e4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تامپا، فلوریدا - فرماندهی مرکزی ایالات متحده (CENTCOM) این آخر هفته حملات دفاع شخصی را علیه رادارهای ایران و سایت‌های فرماندهی و کنترل پهپادها در گوروک، ایران و جزیره قشم انجام داد.
این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی ایران از جمله سرنگونی یک پهپاد MQ-1 آمریکایی که بر فراز آب‌های بین‌المللی در حال فعالیت بود، انجام شد. هواپیماهای جنگنده ایالات متحده به سرعت با از بین بردن پدافند هوایی ایران، یک ایستگاه کنترل زمینی و دو پهپاد تهاجمی یک طرفه که تهدیدهای آشکاری برای کشتی‌های عبوری از آب‌های منطقه‌ای ایجاد می‌کردند، پاسخ دادند.
هیچ یک از نیروهای نظامی آمریکایی آسیبی ندیدند. CENTCOM در پاسخ به تجاوزات بی‌مورد ایران در طول آتش‌بس جاری، به محافظت از دارایی‌ها و منافع ایالات متحده ادامه خواهد داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76527" target="_blank">📅 08:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76524">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRUjAWR22ZnPImkWUgBQpmfbc_BJ3LCnNiMhiFYhlSiIwPqbaz3Ta1093_cXGLOLi-RJrjsHmtorl-JD5HRxiYajlpzqYcptNEnf1uqAsfEVyYCmuTUX7Y2XVk3Qe_Bb9ecTfx1uDLUxVdNwY5LXvQoFq4rBK5W2PLiPqeyDVMJesXKknBtXO71YrEzZEHqQaf-0zVZT4Cu7wPpiIFl6ZbrUhNcEuMI3p6lZhgOoqCcTIDFOb7qsY2IbWSF4wElQ3ZkDmuVLfRyXXjJWgnlbz6vfThAL8Yaf4y0dI4pecmlkufaMYFu_rUwqlwJXTXw7PDl09nYKam30LuRrG24p3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر تتلو تو پست جدید یوتوبش برا حضور تو جام جهانی ۲۰۲۶ اعلام آمادگی کرد.
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/76524" target="_blank">📅 02:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مرندی: اگر نتانیاهو در جنوب لبنان متوقف نشود، اقتصاد آمریکا در ماه ژوئن فرو می‌پاشد، زمان در حال تمام شدن است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76522" target="_blank">📅 00:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76518">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جدی باور کردید یا دارید شوخی میکنید</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/76518" target="_blank">📅 00:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76517">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝕻𝖆𝖗𝖒𝖎𝖉𝖆💤</strong></div>
<div class="tg-text">مشتی کارت اصلا خنده دار نیست واقعا الان من بخاطر تو کل خانواده رو از ذوق بیدار کردم بعد ریدی تو ذوقم؟
زشته کارت اینجا چند نفر واقعا شرمنده شدن جلو خانوادشون بخاطر تو</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/76517" target="_blank">📅 00:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76514">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromarshia</strong></div>
<div class="tg-text">کیرم تو کونت من اقامو بیدار کردم رفت پای تلویژیون دید چیزی نیست یه پسی زد بهم</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/76514" target="_blank">📅 23:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76509">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krIgyBMGP-cqLBSN0u-tdooTsx3MJSZms1Q4xcPsJgi_c8QTeGQnSD-AgUEqW3t-OJy5rUFCxSug-2D6s_hpv40UW1drnIx5A56mn5LZJQv4umN2E4t9GleSG7n_2r-Ehym1ujp58B1EkwL6pTU6djQxZMIYxyzBhnwRT2wcmeXmnaamqvjI7v_s4bfBWEDO2CGQYyaHtXdLDsizMLRoTBLOpm19dQROQOIHLHBX1qHhGEPFWcwoUw7gtRMsiixAPfSdjSVpYt8Yd2J4taiZkTv5g6H0hjOn4n4LH-fxfpY1gfIYGGXuQlYvhKA7vdEwJGsb286Zhx7QvPps_XHa-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویویویویویوی  ارتش اسراییل تایید کرد  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/76509" target="_blank">📅 23:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76506">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyo5l38XgCWU6iVxHhjilHwlcCn7JwsuO9k3pSjRLrlPQcHMBjbxVLrN3r8WhWGLOPLCgTSBOtsTWn9QamTNsTxCIyDRIhPqAPRVSsvvm9kt2AtTj_rWFxoBYmGvXS96aaX3Jm8gA8UdEtM5WcePab8oyzD0isBb7Zor7QcOVdvtPD3qYn6apcsbMRF-7SCA6fW2sinxVgBTTA7tY-X_7HViwq-MUk8AwyDcvy9hkScHIjpr2KgjuJC-23aZNAGPSHdv4cfHLmNJVcGBKw--Eks2yjAGxUU6RroBUEul2uTBPB-S_-HzQy0U8C_jjHkozAPYnM2BeXctldjUj83cuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویویویویویوی
ارتش اسراییل تایید کرد
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/76506" target="_blank">📅 23:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76504">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تو اندیشه تهران یه خونه مسکونی لوله گازش ترکیده   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/76504" target="_blank">📅 23:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76503">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تو اندیشه تهران یه خونه مسکونی لوله گازش ترکیده   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/76503" target="_blank">📅 23:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76502">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کار اراکی هاست
یک ساعت پیش تو کرج فعالیت جت های جنگنده گزارش شده بود
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/76502" target="_blank">📅 23:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76501">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تو اندیشه تهران یه خونه مسکونی لوله گازش ترکیده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/76501" target="_blank">📅 23:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76500">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جدی مگه فوتبالو مردم برا سرگرمی نگاه نمیکنن، چرا باید طرفدار تیمی باشی که خوشگل بازی نمیکنه، حالا اصلا هرسال ۱۰ تا جام بگیره
جام باعث میشه تو سرگرم شی؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/76500" target="_blank">📅 23:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76499">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_rbBfOkApqN4KYroS63LvNCGZ4zhuL_9PYETn1FERFOfN2RNETrF8d9Ri05PBSGyZhCvQvCluRO4IizKd4kMSBUmUHWMc5j3TJraQj5FnERlIFhCu7V2lsHz5U6gIocEErCCrBgwvs0RhO4odww65A8T7gBTtIgQNuvYxcmr3EeM7Qk6qFAbEoa6oiYweoSzkLMVr5taX1U4m0BZRasbwxVqZJucytx-q0zCDZm40gn-7p55lFhka1zai6PrmmO3XVUnkA-PJldXAKMQEddookfdsFFhIjmHHWVWIuxQ5M2sZaeRVjmWEGB7C3xuphSIKdbmagKhtK5JctwWZlwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرسنال به اولین تیم تاریخ تبدیل شد که طرفداراش بعد از باخت تو فینال لیگ قهرمانان جشن قهرمانی میگیرن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/76499" target="_blank">📅 22:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76498">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پزشکیان :
استعفا از ریاست‌ جمهوری؟ من کارمو با قدرت ادامه میدم و فقط شهادت میتونه متوقفم کنه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/76498" target="_blank">📅 22:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76497">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">😂
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
😂
😂</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/76497" target="_blank">📅 22:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1l3tTO04Kf5aSctyQsRlHOKiqnmBvt6ME-vhWufWSO8GF_cmuLUihbvFPaUtdza4Z7ymbtQi7EO7zuzIQIhSCQvu0vHKloyPn09vy6J-oa7PkmliaWJKkYSwaVoX8dkusN_A2VDLaaQu7bdtw7fUV7oDIdM3R5S0Jz8UMQZzy6R7jEFwUxXNrHJwftmMMzupbivHGczvRuORGrK8bKRwzws-R5fJClqYyBhD9AmTdyDpVIVIIRMj3Dr7uRoZMCUzzvRbfFirf_jKEk5xQH2GFrLpaMWpQ3U5R_V4KsUCOX2EO89cz14VOT9GdqYlZ9TbspPtEGWDMYLmkRpOUvsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
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
😂
😂</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/76495" target="_blank">📅 21:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76494">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آخه فکور (منیجر پوری) گوز کدوم کونه دارید استوریای دوماه پیششو پوشش میدید، خود پوری هم به کیر کسی نیست دیگه</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/76494" target="_blank">📅 21:48 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
