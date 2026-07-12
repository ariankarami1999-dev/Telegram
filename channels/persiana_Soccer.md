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
<img src="https://cdn4.telesco.pe/file/UVE4kDOR6uh7OvvoDUfGIXEaULS_ae5vGc8mSAzYrelbWk1gt4_Lc4dK_Rr_yDCzocEo25LoQyOLjVAyU1R35VACJl6sb49IaOqOPRmvPtjufM001mHfI4nK3wWTiflKjiaoGUNTZ-sVu5ACHdu2zJGmuB0w6Du8iZLx7Pr79RTH5lxF9y6BMNvDQIio6Fok9ztIyK4CygvczkAORQVu7jQ-vToGBQcbPCuJdLrFFkeXGu98o74J3R-RNXoTaAuEulT9JcrkIomqPTiVADI7p5KjSJstfgF9lzQNvi4Ain8vB2HrVO7Yd-hS5UOXTyr8aqVynL-fiCHC5jrWiE0Zsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 435K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 13:13:50</div>
<hr>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkZ1Ldb1GlfROK8STbZawO7U2kpYNA8Hr-weRwtjf3ib5dT3JpTvtrRWk4LwsOg3aqCgGyfgErdgrJC-iw9ghIlVHvNqRNTsKpiUHxPUNKDRtAQZH2Nae0GMO_aFSHBgPGDPLjTNvWudSCtnZ8cNT0j-WRq3OH370synbj5T1Y7a7NFTlIAUfTGA8OfKdmDwxv2PzC4LOhX6MRJBJa9jbzixBIWfzqhzPMbIJgELmsI35fPEWCtnVg_aN-4XRzbO9HTCJOt-Ao-HWfeUt0cX4bvZCWOgQar-DAmTcQ3e6_6edpSYVMFblxFKfoz0sP18eXOW0wzD2J4nIR1xL33S9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErXHRkzj1mAxWJQ_ujYPoMLm0TdgFWQ_W3ek6GjauM5JCEJWNz1_HcsKEX2oH4tREVkskr3RmORCtyIq3xpIn2SjsAevKvq-Bk1LGP8HLHPWBgFZbtXViLqN6cwYtpagNQ4XUOiQpBjn14Hs6CsvzPLuzo0_MxOJr1Gn2xIqYiL0G5_sUKJbdwzrfJTnAxrxi45EfMkLtv2WODo82cbPyt_gUoGs9X3Kl9TyXDMRsqMHchFZTK7DxZYOhnlNlg4vvmoRXqLPnPwyu_LTbVRrkzxpnMUj4FeiVgVqLGZmsc2CV5D-ftHXbhD95YngJp0NQmJD8acDms1ddjLfFRLEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3yn-09Esruwb5e6Gqybdc_8FsQJRfidqMVtdIGxHeD-wqTdqAKXl2GUzUlXGfDdmWwDs39dNFiHFzbz_UYb8ysFXo20zhs2IgW5D-XZLFM-K_THQ71dSGUWOT-vCnqRJlj7HobrHeQtQp5jyyCk7CFRFSw92ZMMjL3BvJIJYERDv1TbJgMlRHEtnoTDv81smrHziog2JfY8-5oxGV2ohoRE9RqEl95OBZKQxgjlFHDPNRBVvdHgXwJ6KmQKRimVFJlf2fPyjGVvsAAkXRTPFRU7cw4m5-HTP4fzNly3lGFZ0EGsQ896PJ1t1A52UzSYQsv80JSg5vtKyCYpVHzYbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6pirnEhanEAfdU1fFgMrlDSrHTWqVc9_8CX53tnuyVivvqxBNwVT59aRqjAxaQ3z1nNDHZv_q6gqS4DHE4E925jLKZv2EPdYWXGjaXa9z16Ekk2bviYc67MKKkEMaWlzEyCqPqR7yGjShx_Ca-t1Aeudy5vkljMhhjnGsAA2hw-6c9yExYQIIa91AJT9AJHwyvklPzk1N6K-0c6UmIGICYbC1QXlooidCx8602rrpoO7LAl5xwUzdZ82EHmh16xv-Dd2mHY3Ga778z-k7BacvvDz3ACqSdyFVFiuEkAdRxjPdfaz4JDU0Qbwe7tIdZQux4cqg7svitn8QYZ8vWS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا
#فوری
؛
سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=I80nTItZNdTCKkfuSLXF8wcSU3FnQl5Feis8oFZZVxoKFCjgDmxdAtmJN-QB7Dg1ZV-3QsTRbX7KHLrFpn_7vGtN3Me2zCgmupIUrFRqJ1KBH4WdCjp7M6DV3cQZkZ44LWT2cznpUfnZaO1p3flpz0DvcAH7Zn9P_A2SU_OhFdgpjZ7c1zYIPGILWATPIJCK2hexTXt-zhvojkPq9DdFAEfh29sMCcpGlT9HSZCt89DolNZ-oWsXKjrBUk2Ay5d1yrKqQEt0_MXsXIRXy8csBWrr0llyz3UiX8v0aVAglAKth_CrcmnLL4SC8dvdQbFVqGlw0R1I8Crkv6vImf-B_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=I80nTItZNdTCKkfuSLXF8wcSU3FnQl5Feis8oFZZVxoKFCjgDmxdAtmJN-QB7Dg1ZV-3QsTRbX7KHLrFpn_7vGtN3Me2zCgmupIUrFRqJ1KBH4WdCjp7M6DV3cQZkZ44LWT2cznpUfnZaO1p3flpz0DvcAH7Zn9P_A2SU_OhFdgpjZ7c1zYIPGILWATPIJCK2hexTXt-zhvojkPq9DdFAEfh29sMCcpGlT9HSZCt89DolNZ-oWsXKjrBUk2Ay5d1yrKqQEt0_MXsXIRXy8csBWrr0llyz3UiX8v0aVAglAKth_CrcmnLL4SC8dvdQbFVqGlw0R1I8Crkv6vImf-B_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIN5sYFGN7LxeDxtyjk4r0VxcfOGKcmWH9o7brbG2Obdw_ZzFq20G3yDVsM5evEuKz5xVXFZjnfVGeaYauFkXf4iiH9pkrRFf9HyVK7T9Zhf6ssCjsxaFe1FmWJoryD_xYjJHIeGfWUkGLgr4fiWjJeDiNvnzH5cuTvwW8KM8JP2DWugOrSj1PeAh_rXvTywr4vr05f6xksVR1-3is8i6GQIXlWc8dbiErfB0hm3t_sxedKo_DYGDMsl0mQ_zlhmRuUd9tJlAFh2fbwlI_f4KVSU8hS6_gCNKAWHgojqO6knzefD4UUnBLCIxs_hadnX0CpkPXG7N-51daOQ0m0dpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjs5bxTjsfcFshbPqq9BCg5u6eOW6GOx-hsPflui3N39Zlh9UbNwsktDzrbecJmsJ9OBIT_ROIhdjkz7DDOSDu4jxaA2U8XiQVUNXBqU07bASFXexGfeOVvywAn2ArCEqd18YDN30IwQ2TIxQ1aw3Fr2JxQiuml0_IJetemYwBWnU6psXQLBpOssK_IxE79Nz1pPu4aWmwnC2q9__geMP1JmfXCvGmHQUfGbCnCRG8rG8VH1wW-F80j-EhkXG70nifxoN4edUFdpcteEz6WoW-esrc90iN68vlAJM9Q_Vh90hl5tH7Vc4HWw5ltb3_c_luSiVVzoCG4Bh7XZ_7WHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=JK3WHqBfwYN4gj_TR7N7vm2a_Kw9qpeWi62HkJlilACXSsn5p78PAB8RYrjlDsFZcNrnL2fsmHOsFe98sOBygHSylDU-moR7X38ZsBkqH283aXbGGmVinMAf0mB1qZEgf51Hyp1brcEh72MIqQJB04mZh_y4XwJ72I6sTS4u7BeX6YUqDaq7nXnrw91AhpMNARA2F4WOdQG5dkHZxPFGwH_w2sI8XjtEwixucCn4FQV7i-HWAzsDp_fuyfOCShKRKXpNBCrsngGSYcuDaOh-1QN-JppYEI29lSgZg2Te8ZrKldacnMhc0uhaqLYmSq36G8c3fi5sd22J-1bF7z-0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=JK3WHqBfwYN4gj_TR7N7vm2a_Kw9qpeWi62HkJlilACXSsn5p78PAB8RYrjlDsFZcNrnL2fsmHOsFe98sOBygHSylDU-moR7X38ZsBkqH283aXbGGmVinMAf0mB1qZEgf51Hyp1brcEh72MIqQJB04mZh_y4XwJ72I6sTS4u7BeX6YUqDaq7nXnrw91AhpMNARA2F4WOdQG5dkHZxPFGwH_w2sI8XjtEwixucCn4FQV7i-HWAzsDp_fuyfOCShKRKXpNBCrsngGSYcuDaOh-1QN-JppYEI29lSgZg2Te8ZrKldacnMhc0uhaqLYmSq36G8c3fi5sd22J-1bF7z-0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsc7_WqgsnCTNwdAUYGxmBWY55pE1AomIYjgbVSmBqOrhDNC8uk5h46_QChUy4PrYuyqt2kH3JwWXS2TVV47Qe3wDAGEB3m3Cg3m2Eo_4qxKQln6yzIFmh2wlaVQ2xkPvfDw9NfUtbbGiuLL5yCzkHmOni0AGEC34lmqhSLf2aqymrHOtpehmjIuH_eEQt57q9Q105p2CzoYJYo4wSdJvjZX6Qg8Q-SjJ28_4u6P_hGjAXJ9PddkFHTxXXMzIQ2E_SZMgrCGJqBUQWQiHDklkCn8haW_35EOzSksdTf0BSPwmDlW8fUWBOgEc98rTRjXnafxG2FcF6yzGdISelWPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=Giiw11oOwBugb-O7_1HAixbwjxkxMRpLIcNhwlBYN6bgqIyt9hy30gJ3n46aGMQUtmE7Tumz4vxYqIFFRw-Eea_E72NHRZiv-vP3ZAqaoYC_nnu8c25ahhpekVbhD-g83Km-NMcZrMa6nUEfQuv0s170KRX_MUberzWXErFU5j9zYWp_bbyq_s5_aqzOUlIr0D2FkbYAG6O47kKzxWmzPelzumoq14gsYLpK3kEy4b4tROKRBoO5FvVHHxtZ1ccY34nbrSWivgcnK8IKuHJp-u6sVfO2ijFS0roYCy3BmLIBRTLBi6agBsQIIGfhtcddcFT9ZBaoRGszSf6oC9nrcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=Giiw11oOwBugb-O7_1HAixbwjxkxMRpLIcNhwlBYN6bgqIyt9hy30gJ3n46aGMQUtmE7Tumz4vxYqIFFRw-Eea_E72NHRZiv-vP3ZAqaoYC_nnu8c25ahhpekVbhD-g83Km-NMcZrMa6nUEfQuv0s170KRX_MUberzWXErFU5j9zYWp_bbyq_s5_aqzOUlIr0D2FkbYAG6O47kKzxWmzPelzumoq14gsYLpK3kEy4b4tROKRBoO5FvVHHxtZ1ccY34nbrSWivgcnK8IKuHJp-u6sVfO2ijFS0roYCy3BmLIBRTLBi6agBsQIIGfhtcddcFT9ZBaoRGszSf6oC9nrcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1HiyRluZ4h5anybNnolz0FOwTte-vkFoFRBKmZD7OIJvSibUTsPrtUFCoYCLjfc5IvmFFWzu4Y4pfBP11veo7DpxwdxjxCh4vuqvzv9zix6EY1Zy0-k-zfQlujErOticqYAAYahrDBZLwd0oY7iDv02Etj4S7UCXf7vpa4NFD4FNYsyKgew-OyLkl7EzVbYuJ09KPKqC5Te72Gi1jK-asMwMPJCS86SXO2qFv9f5V2XwnlIKT2HXFrowIlzSQATJJtqYSxPw4JhtBjab-7wpS0yhAgQJhl1ioQ8ctC9VAkXDr4M7tWPFavF_k5zzYu02C32riK7eIbR9R45oVayRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAqn_FqBQkc8pASUX7A3Gya4EGqekPhx8T-2MFQu3Z7oJO-xkCMZUyFAxFsNzYvGQZHvEO0msBXhvAejcejpXwpeheMUWhu8rtiArmOei0B2-FqOe9Ycgq6N-npig5HVWG3cLuFSlqJ9eQjTI0LORLyDgxLgxKkoARRmnAXAwuJcCX_14fPp7leoW1pWsOE8y7n1ukbYzMJztuVZ7mPtWnPw6hwVfBWHvLkLeRWu30hnuOQ8Jp_Osol1YJOWqcqBAXHuILUrCLaDjN7m_tgRmS4myUuLoBeWNb2wJ-kvU_Fg3JifLs6c6E8yFZKXpZ9YFUMlLORwBaof2TiocILW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=Jfp8QO_FYyNUIA6g3BRbLf1ZhOlYPnKGM_VvctUXKCHzb-AHcAzsFkobU55jfdYREWZgZZZP3urR8LAAsjFGt5orkRjLm4EyfYbbJ7HBRy2j4yqwOPyLryGlk8tVGJzZpMChXcqvOC_u8q_PzZZyoz9GFY2bBdhiTvkluMq-6jiQBgWQRUmhplvlN22yJey6o75EgGif_r0z-Yb8cmlPdS5er-Nu6ISmAIrjKD077ysTpuY6vgLifJ-uNMKBFjwDnI5ALPdJbQQeJ0QSrCVWKhRrMHKLZQ6VgnH0L_Z3Y7gZ5xr0ErTTzpXqH5zA4y3zC1n4ACGXZTNhDApUidTh7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=Jfp8QO_FYyNUIA6g3BRbLf1ZhOlYPnKGM_VvctUXKCHzb-AHcAzsFkobU55jfdYREWZgZZZP3urR8LAAsjFGt5orkRjLm4EyfYbbJ7HBRy2j4yqwOPyLryGlk8tVGJzZpMChXcqvOC_u8q_PzZZyoz9GFY2bBdhiTvkluMq-6jiQBgWQRUmhplvlN22yJey6o75EgGif_r0z-Yb8cmlPdS5er-Nu6ISmAIrjKD077ysTpuY6vgLifJ-uNMKBFjwDnI5ALPdJbQQeJ0QSrCVWKhRrMHKLZQ6VgnH0L_Z3Y7gZ5xr0ErTTzpXqH5zA4y3zC1n4ACGXZTNhDApUidTh7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25496">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ0fFUEwtXThD_Bv9YSbe00ozW1FlX2VHDBEO0xAlk0YHKOG_TlOMgaZrt8Mm1A2pEDNdl2sYV689lDIRRTS5aRAPEsWLziZoOFWZ6dbY1hY43PnIwD5zvT5C0aM-mXo7Dr4-jjbHu4l-P8zbOGICd6Vlco1U0ArtFktsDAWLB7LBX5MzQcNBPhVVr-vHI613p2cijbpRmSTgu5sPUJPCG9nFVkoZD6xYc6Bga3mCijBULOh52KmjUCNYy6zGWnGBdPOrD_jLvSgFg1qAgb2XSQgT3yLggiy8ATWePHnXEZ0LBC41YEJt0bhHcbACwUo3LDF8TsnuvGCQszfqzCuKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری بت ویژه ی فینال ویمبلدون
🎲
بدون ریسک در وینرو پیشبینی کنید و از تماشای تنیس لذت ببرید
🎁
🎾
فینال تنیس ویمبلدون
🎾
🎾
زوروف
🇩🇪
✖️
🇮🇹
سینر
⏰
امروز ساعت 18:40
🚨
ورزشگاه سنتر کورت
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
بابیش‌از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr21
📩
@winro_io</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/25496" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=KgXG4BM7cQfr2otAxhJT2U7jJSwZf6qFvKaUr4UoOBKMiWjqbYkERwtX0pb3pwrzh53TieTbOA0jNvDzwGrUssjxayiwwinoj1KTA7td6c2zWzPcQWmfisSFtP7tCLW__YY1Lu9zYM3WdAJWCFXRRlubC0-jLU6DQp7PvYozvSFDBfk513J2KoEkYiyKA0Jmqunrq9etJQUUtrNLTo8qR8YqVeFXGCIPfn13B1C7LNsSDNxIrHGUWxxJ_XYw_p6MPPmFFyucOwv6mBFjDfEoxBq6CI-A933ir0x9DgfhQJg3EVWQxRKJzAIQ-LcyulBlBnZN1FCtRUIljDcx0u7XEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=KgXG4BM7cQfr2otAxhJT2U7jJSwZf6qFvKaUr4UoOBKMiWjqbYkERwtX0pb3pwrzh53TieTbOA0jNvDzwGrUssjxayiwwinoj1KTA7td6c2zWzPcQWmfisSFtP7tCLW__YY1Lu9zYM3WdAJWCFXRRlubC0-jLU6DQp7PvYozvSFDBfk513J2KoEkYiyKA0Jmqunrq9etJQUUtrNLTo8qR8YqVeFXGCIPfn13B1C7LNsSDNxIrHGUWxxJ_XYw_p6MPPmFFyucOwv6mBFjDfEoxBq6CI-A933ir0x9DgfhQJg3EVWQxRKJzAIQ-LcyulBlBnZN1FCtRUIljDcx0u7XEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHzX5qbytv8r7vor81kh7ev0yq2p8HD6K-375Wpu37JYyMKFGulSz29efNMArGHk3athr0tOj65QJF3wdIaXgTnOdb7Zz6S1jNu3DKQrGoea5avRQmu37XF0sE4zjhJOwMrlcji5k7Q7ExHrxcHFD0NCCSZYwdrftEcZlewNchIEy7YXTXHZPbCqgqDmuEnVJQyMFRXTli50QMF42X8Wscg8g81oq-8UgaqlRADRZMTDAdRt3Ah411QluJrAt0xm5GfSfpsxjyfJ4ITQx9CJJ-BL9uaHDY-cir8fHQzl0BYwJqbQnuQ41AcjjU41WsI5tvrArFaQG0iu29G0S5vgdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjkYM5kNqZ8OfF1LA0-dxlE35i6stmGFjVQNP8G1XR4NQEE3-x0FaIb8xTMfRnyCTfWxSUdL1LCC0z6V0rn-KPrN0AEVobb9ryCuVjavuuYd2c3W9M1q4D7csxaK8nWPy300mNYcSlBwZ070tw1wCZJqxEUk780Ac5TzbF-UMecUHvF6qJXZfP6iyA8RYJHyu9a4PhmOUgNmVoMJBD-T59WnUaqV3eXIKd_T9YwAjZOnZnTSvLA_FsKMeNRbLoRCII-39a1GnqVgyAJmUoh9NfMw3Re4I7u7J63qwL2jAhgAX87CbsOVRL_RZedaJIAjdzjfnkwy5CnftfCx3KgE6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=OxS5pln_9WuVipuUEKlr8uI_lJaRgPz45eQkwylKSYvXRzvaOIzbhhYWQfXzAJCteq5T3k0mMuD0raItEi5AdBMB_fgoYy1RxCF4ftSTF7leK319AYh7na4r5CpIuJ1ThN_AOc0bpuoSHMpbRcuGSRG0ppgECP4nB0CUQJmRC_v9AWLG2jW0rqy-hkBxWMocjbxuDAbry_Wgqm_VayiRSLNeKIuMNxuOcg8MAxDUXDw6WJI-X1mGkFYdTgwUFxhVGTb9iHACdQtRk_htzK7tRTLVDxH-dUPOoxbpQgnoWsGc6mqQQxYaps3zZTB-uZMwVlaoVYfFghIWihk7g2FWaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=OxS5pln_9WuVipuUEKlr8uI_lJaRgPz45eQkwylKSYvXRzvaOIzbhhYWQfXzAJCteq5T3k0mMuD0raItEi5AdBMB_fgoYy1RxCF4ftSTF7leK319AYh7na4r5CpIuJ1ThN_AOc0bpuoSHMpbRcuGSRG0ppgECP4nB0CUQJmRC_v9AWLG2jW0rqy-hkBxWMocjbxuDAbry_Wgqm_VayiRSLNeKIuMNxuOcg8MAxDUXDw6WJI-X1mGkFYdTgwUFxhVGTb9iHACdQtRk_htzK7tRTLVDxH-dUPOoxbpQgnoWsGc6mqQQxYaps3zZTB-uZMwVlaoVYfFghIWihk7g2FWaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_j_kptCKXSiPEEGiIf5YYdSrSnqmgR13RFH5h2gyLTCXUV78C28v1erYj1vvq-QEQ_JOGqj71vgSZ7B28jtDsAEwE5p50TZIT5J7fqpxVCIs7MPH4mepvn56wgGWIYMQXIC5iowtfn97kND4YJ26ETiKY58IKJZ3jxUM0JRxRw8rwHyWcSzArpVb4WMC1qIoC4RADcgo_MPj6jqYaQVxE87OeVryBs4ShzDOLhTLEhSdBsgRS4hiG9-eioKecf29_fPp26uMQIK06jMnjJA2o5FbDdMViyYD-8Un_LAAitP0YaS_EkG34ycfbGDV7EsgbOVH0Z-gKvbUQVkCiqiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1-RgkumQMhyONcM4YamG7DcL5gQbQjD5kcV35QWp3m6MuAi5FkonpYilB6f9mxlN14ZDW9RRqf7XQu5ewJ1XLnZksHPTkrPCXYAzyr_DE3XMQlVQ49LmjJEPkS9ISADPb_tcS_XA5xIxEkcC5hv0GtmpXEvsN5Q0zn2pjgupG9nf8SeLTItCI9ajovyKGepjwZLM0StTleW-Ce-bCCtEjulnEL9mBssQxt63BiK3LriP-egxYbr5HHkS68-QH7ZzoCNJWYdvBdZtNW2rMkD_DXH1ZIrAERL6dYZoAmX1dNLmfGZh9hrgSxFjXAmmyNoN0qZXZmPR4WHnh_DiB88jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iipIDfJor0R5Jk99q0-b8TRx6xpnuPY8G5BIO9_qDTsJpS-XtMaRJFJy-sfaYgxh0DkZTixX8-aqlARPMIR-ZDe4GWWoX3C-HaAhYfAC6N4-1X_RP6Ob5G9rjrPx0WuMRUVDn7RMRcSIvtEwjo5mHWjqLaNk2ya-Ci944aceD3B-K4227NqOc0jKqYJFImBq_61FLlSUMQGl_SjzR-LvghBsDC8uyUGADvVmLVYJzCMGcfaABWjmAmkDCrsV10o1rRQ_Y3jyeixiklcIHqa0hgLTIHAJ5I4-qiX4B_uB0hECISF1NbexT1lbxNAM94SLBkzWMpIGZagBx5hkIdvFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQMZ3R5UQaH0wfKfqi4f16GdHEIb28jVFdJQJ7vhmDkvhnktN1VFHWpmgfEiQmuydj7fay2FSg2jvhH8cjCCWx1CXETtG8TyXOaoQ-IqaJO0xKPGT2B8WIi07yyYxpii0zyLlmWJp044nguWa6_PS_YaRWKqp6P_FufrI4xJ8OMNcQSbSFxXQnhvmXPGRaJLQQjsqFfHl6-KOrVVt5rsG8dn_FSqcDaDVsgo2T7CcZRH0P2_Y2ca1HX_YWSsGr3kjhvQzcPjFaRrqeQD2oRE4fts0vpXfydsZipupD_DbJfXuA4HHcKvA1Sx5CSIhYqDCK3_-Rgyt6-nUf3D2tXkAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv8eXNPDwZnyd9cVwcWY3iMaKXOrqiAPfa6ugB42c81GX_8riL8UTr2LW-euuIWnLM81BDiwa23dbCKu3PjvB1q6DD2iZ3ilSMzNLtY9qammof2DlS-K0SyC23RTRADgo0r0AivI69ihrJ2qFPwj00mwLmIPETX8fa1ybHzgvgVWA_FUH_Nej-RqBEBS4nZxY6Uh6jGTpdv5Y-zHczY2mRJFGGzFQL_ih_wv9iG-QtD5hnIuTUs41JnnbSHMqEbUnCXRiEYP1ToX-G77NT5EeRmX7Fr975WJnwNtAFuZUlqbWY_2e5LCT0v_tMBSvX2n83F5oy1OI0Y2zmebSIa0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcR6_mOgBqhmIbQicjw1J6gb8yD6_gpOstgH-R4PTvYY094kvb2PiMrh3Qi1zbLUxFF_E-Fssrk8PBC7fxZ3FkLy77teYRYIW8LIM_q60vhVTy49_2k29bnuwdd8ni7frxYV-iRCNrpPjT-nX9wu3192X21NnoNZdnvCcj6ikypz49azy7tTr-q7amkCDdnMrGgHL7O7k-nyz4aaLnlbq2tkmAQ-Hmjh5HJjBg0DMGckJEOu8i8BYCHFUAYso0zmt_pLmClII-bTOVePh19316-rzJciX35d8v4eyKAR_IG_mvfBgPBHUqejUqpsTLM_stajbh3VXbCxaXRa1HicCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=v4FSpkFmIDmJloFBBWI-DfWb1b4OiycuwJJNzWI1SH0DawPexdcXNQzapOxIl_GqwqHKGHrsbvjKu6wmdOqZe08iup7inWYfkYB7VK7ETRjV-DAhnhR6F0MExt_Jusv3ZJzvCJLpQ9Iut-vZ5ayCDjmfkmd-QuWVY_ZmWhtv1xBibAWuYpaFjmcO8lF20JI1f0_7QekNHS83pKmtHO4uHl_3QDnE0mznWs5-2JktOBoYoyDo2XiPn7T9zMZumao6BXcYv-u7tijRrdKtbPdfWMobFp6vAW2VCLE1-BY_MivBG8Oh_Es8yeLS_52z-huAUIVv78zrSqPvYoyNwVbRFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=v4FSpkFmIDmJloFBBWI-DfWb1b4OiycuwJJNzWI1SH0DawPexdcXNQzapOxIl_GqwqHKGHrsbvjKu6wmdOqZe08iup7inWYfkYB7VK7ETRjV-DAhnhR6F0MExt_Jusv3ZJzvCJLpQ9Iut-vZ5ayCDjmfkmd-QuWVY_ZmWhtv1xBibAWuYpaFjmcO8lF20JI1f0_7QekNHS83pKmtHO4uHl_3QDnE0mznWs5-2JktOBoYoyDo2XiPn7T9zMZumao6BXcYv-u7tijRrdKtbPdfWMobFp6vAW2VCLE1-BY_MivBG8Oh_Es8yeLS_52z-huAUIVv78zrSqPvYoyNwVbRFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzFonxsK4vUcOz0JzUipuu9hVybiWlipLJihSNzXwaEGlfuhFpBgwxnxdcJyIhkbYySxg-mWU9oYmCwLypqBA1KKHhhbIv2rdtAxpizUEi1cqH4XCtNmD1v0sImlFm29rcdopaf2WvqwSnpU4pBOfeO7ZKMckQnXnGwZAGaxSVc7KiBUDtFtzdHDW7jIK9YsnRK0MthVisZryxLCQsmkdqi78EPWQ84UsT0hUUYMzVQhwnzuBdVVLLhj5Zj1ETB6XPktk8qRFCn91gDlIrZywoKznMyruafsuGIcWTrIJ2YQeym3wv-mzp77UDL8gUFEVDVRDyFu1TWt0yRFC9F98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBP2cGe2Ute3TaLKj2OpkHLpm2r3-Ff0kG0nNW0r3wtapuO_xUEkaqYd-oLGIQj0oKu3J-f9eCFL4uDJja-8_3MqKzXFn6MEZQ8SBCbMs0zmMTcCVrqfqC3JY3aFAty9iSRMqb-99hQdE1xgRIjwgIyx9aazGeppzPZPY5c4W2POR2rOAAv9w2GhGQuYNdb4ZIdOcN7TMyjdC3WjWs2uAI3ucsI_nR_Nq1lrdNFapYi0XJd-45-rNJ_5mIdxbbph3Iru31JjuuIjacwcDxzOSBhNHcNNLe9UeZK-h_BzYww8o2H5qju9rK5LqB7tqP4myifV8tdX5rgCSBUrFZOzuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkIluWuBZpGCELiKr4s5xe59PKN5Lh-Vamdst0RkWE2V8vgInlQ5YwPDrgYqx-dDtEFeJBxWeRYxSBP_nrNzOanI1xo2VMofTLWbL4lbUp6FcYug3um0icwrcQKwq_yMcv0eCRnOl9BJhLc2ezB-39kEC5hNeLmfvrsnb-0wu71xi9mg8clDrZjkBSM4Fa5VvkVGKKDmOMHOgEmqiKnnD5OvkEKvrJ8qYxk9hJJOEaWfnZJkuGIGQqJkwJ6MIq50o9pn2RWdY2DS3RFRPBjrmeAlTY7ztO1JlfKaWxnb6IgZNTXSdjzk0dphVKKAjbtfffO_rSJKjCAAI7L8ZD7lXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDhaYoaGEXDiQ-ZxW0dalYXKlzbz_XCYAJvA7yGRBrpf7Hhvi8PCUej4pI6UPLXn7vYaEgBCPPxFT5IjERsMp_cTCBkOT1QirmebaADRH5HtfSyDD_UspC4NMX_X80PpBCRuVVnTYe_bBOxf5dbr9_6jEelmZ1C8RE3kMrREggCGsaLWmuDjQD-U7X0b9ef3Qs0To89dmTyEB0nN3k_zdOLfxGupa3oxlzjC_5Ubn5XI5_JNfkSgqJCXU2o8dq2EHigPDz1AgeO7NHNTIxUViO-IjZ2lit3z-dY5FhYH5RuUaHdD6DWzEr22yvMK0LeLRcnHACZOHFtWoc3zh3OpbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqh9mOl2zxL--vTcjeypvvfF8d2wbbIawLLjeyFEHwog9DjjwyqYrKYCk90vY_WtVii7RHq7Dzlnd7NWzJLbNYrCccJ3z0NuIwU7BrHGMXsmQ7k_f3nW3a0Dy4C93sKf_mNYGvFk8LxsIzdzQ8niAng8v5BsR6jIhbhcALPGYkrav-LAt74arBMQGUK7VlyNCL198w6r2z21Zr1K-eoh4F52MtxzHQ-i4mD4u7L1yUNcRMeh_vZoa051f_431UjN3p2vGHkNFnkI1v10v6nRGR-vVCwnpZTAwdnzHg8bqjJWvs1y3buThGBSY_ilbMJv-6eLRS551JQXn8jtsGFzTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDCeXFh-WXwEJx9hG_a_7A23JlXOEd-txANV6nF0uPRlPTBsqqo8IQWhjtrqGXGnnbVKxDJ3klduxkBDOHDCpC_b6rJhoDMZQ9ekS3ui83GXboX8WXh5AIE-dKtmcFqnbhM6m4uGnWWqRIwLvY9KE7zfO5ZMJTDGLusMM8avzbPXKffogmuDygLq-Nkr5iqgtjN3Jhl3d3vYeqHXuqgsmEKtay5KJfjGR0nVAysH3WbfbM-zEJsS-glgUz7UGViX2jqbuuB_CHcGvSfxw6pghWR-An9Z-hAykT8olAZ-e6PHqzB9jCJGheslgXG6l2uA7xmxbLd2fEJWeDTa0OL3Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBQijvQiAimFheTa4ZOqWNHU5Qb2K12G7LixgNAyu790KsI147g3XN_dkuR9MDGKx3-98dBFeIgSUM__uB63H9MtFn5gSDupzYAiqpzIutgRahtG9E97ImvRyQ07dYRHCn06hFfiCHogacYHErcvnJSz24zGUmLYiBW8jhnhqNhPJugJpZPSo2FmqN0rYg3sIcifvvj91AwjZO88fwt5lGdGz1wsro2Qdt51dCbM6-Z298iJOuibLs8z9I_TK8o-PizlXJAbawKQ9v15O9gW8FAc1J5xjDjpFwnZ3Q2Yky-EG4xiXXrRgPoJ49KydgCo_fTv6xzceRDifu8U96c4GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQ5_pNSx4TzK0901NWJRW3aVOBUqJ5h6MYg4k_5W1K45YoN9riZUJksGzewHq1OQCChMdEWOvPDmAXjsfZ_QlDO6OBjEXb0kBe5u27ix8msbgt8ieLO_qXj1LEYyy3-6TXPcnaII8kZ7U8kjLkmlP8k9W6ctmwVRGh70IypaE5ifOHO33i8s2VWXH0VG126WO0hc1XKOqJXQSSSZsM_WdXI7Uvqy4ZtDVh1BMgAwirxMXl9HPfIZ0qiQRVSpxneDSeepqbW11T5LGfyXODsPP-MirohmvPJLptJQvoN2W1hEC-rtGESrWZ6-lHq-MZUOb3dlRhrmn-UdlQ7-4ioyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgWWykA0ZCeGZFo9kWl4dI-Vbxtr_3S3mgyJmU1hsvef_TxX5cN4QoJxXAkIpCfy7whTN15--XWxxMcfQpR6uEOWntMs0v8SJxWN9w3MiakZfKi6I_3i7QkX5X6S2guY7lIYrxREKKmmIGxJv7uWBnGrnZfIkCO48dYnYuYCSpRxRNy6K9x3Er-JH05OskAjpvc3G6vAsdmGVexyOhnoLD4TQSgzlhtMrLmcr41OrwROax7JK3pWPUXwe2hL-3L2XcRFjNNn8cDVdek7yxaa98a7CGwRXiNfH7iZyikIIiY_E_t233I1aa-7iuXE97iCyGSbwDgGsg5kvSAzZ-bDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=QV-nSGZqVNwkzKwQuEvp2onstgVcI8a_YbL3NPiRIaaIVL-_dZtRgzb87cUqf8DVgqRc20Jc5rs8khBZSoKPCG1EnP6IbRL90aVnGmqVcCH6-mDDCpxq1hscj14PywSjfRsxb9KXPW5cT0r85VbyhKnhiYS2s7n3qsrKvTYI2FOI_0FIkIO-4IVuN51tPUNj4XwIto6lXeplrGJa4pf15tf0_ZBLJ5UAvoCPnIEQWWLp3uhnGLOyY2KnMUdmNwSSWZUOuJOhiNTrQ7WzmwBIgFrYmInaIptt20xeSKVL-Bsi42fQSECdkUITPRl9Dg9KIIyatmYiyHrZdjFiaVijzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=QV-nSGZqVNwkzKwQuEvp2onstgVcI8a_YbL3NPiRIaaIVL-_dZtRgzb87cUqf8DVgqRc20Jc5rs8khBZSoKPCG1EnP6IbRL90aVnGmqVcCH6-mDDCpxq1hscj14PywSjfRsxb9KXPW5cT0r85VbyhKnhiYS2s7n3qsrKvTYI2FOI_0FIkIO-4IVuN51tPUNj4XwIto6lXeplrGJa4pf15tf0_ZBLJ5UAvoCPnIEQWWLp3uhnGLOyY2KnMUdmNwSSWZUOuJOhiNTrQ7WzmwBIgFrYmInaIptt20xeSKVL-Bsi42fQSECdkUITPRl9Dg9KIIyatmYiyHrZdjFiaVijzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTnOUspDB5r2LT05rqEJPH1HHGpWhMn8s2ATttclqA4mY1k5bbFXtDQLIBsLJ7TYpwxQJ10ix_sNyQ_3c5sIRMmx7KbzEidngQmZp4UskzsrYW_ny-DTCHJUELXV4Z64EzpxiIhto3xlax2BkUIlMJSL5xXoefBT5QqJAmeZ-u3txSnyQRilC7NOxWXYxZhswJPIFhijojtcC9wyz66sP33DDQHvl5GyFK2000Cr9kMG2-v2ajABy2RK3rzTz3Zd5PbbAshqeqyeEz-lOB02qrBXqYL5C5KwS-nX2VRxPSKCW2UpEAFwhBb0_oVsV-eSV3xXkOwFdu_cguCSoLzBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=eLLrgbvxgmoiWaILcuk0VACLYyOnBAFsqVEJwEl4b-M7JD4mfPRm_jSZ1mc7dcrfhfAc4lnKsHQCTo6xc_caFD2doKU2eM8tGq8Ho6FikFOr4yVfdMc7HVdmNUnQ801kU5y_u8g3EC3CxGVfprirmDBbu7motI7ct77a8dA7-3Fs-km8rZEohu7Z8ZgHuGKWvxbX4x34w4ySSthEdR6cRhRBprljzR_hCvjo6z9jXDNAj2s1-VO6L5Jri5WWhkpNV994-ZJWA4ve91MKa2Ly_lJb80E78__oF0rlWRNkMqVLJEywypxJs7uJIPAPxBTVYfuVw9x3ng5Sjn8_gKKwWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=eLLrgbvxgmoiWaILcuk0VACLYyOnBAFsqVEJwEl4b-M7JD4mfPRm_jSZ1mc7dcrfhfAc4lnKsHQCTo6xc_caFD2doKU2eM8tGq8Ho6FikFOr4yVfdMc7HVdmNUnQ801kU5y_u8g3EC3CxGVfprirmDBbu7motI7ct77a8dA7-3Fs-km8rZEohu7Z8ZgHuGKWvxbX4x34w4ySSthEdR6cRhRBprljzR_hCvjo6z9jXDNAj2s1-VO6L5Jri5WWhkpNV994-ZJWA4ve91MKa2Ly_lJb80E78__oF0rlWRNkMqVLJEywypxJs7uJIPAPxBTVYfuVw9x3ng5Sjn8_gKKwWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
صحبت‌های‌ندیم‌امیری‌بازیکن‌افغانستانی تیم ملی آلمان در رقابت های جام جهانی 2026؛ این بازیکن از دو تیم آرسنال و چلسی آفر دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCtGxnidm1B5oXH4TbZF0ucvtqD9A67aLbA3uFVfNw1nhIV0YIbOnYxI1W0Fds4SYULMLsrJO-F_4iq6qo-VM1caMCmxbb46TygBm6wkk0KpQ8JlMBwtrplCz5FFPvCEGR1vGdF7Xdq1bGxR7v-yNrB5ur-4oNoRAZKXPrD_EtiMyuL7TaTPvFkXhAl0ousp_dESIMflDMgKwfkF_p2qJdVMF-cvewreIXdrlt3bGHoPvJfDiMpFarhUJXqHA7wDZwvjtFfTTChPADzOwP7HBbichSfthzS0blw9zXzBekYq4CGNK-bxxFOVmxSkRyGXvKqCPmEkG9yQ0_5mlZixwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قدرت پیش‌بینی‌ات رو ثابت کن!
⚽
🔥
دو مسابقه جذاب:
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🇳🇴
نروژ
🆚
انگلستان
🏴
🎁
500 دلار فری‌بت
بین تمام کاربرانی که نتایج را به‌درستی پیش‌بینی کنند،
مطابق قوانین سایت
تقسیم می‌شود.
🤖
پیش‌بینی خودت رو از طریق ربات تلگرام ثبت کن:
👉
https://t.me/betegram_bot?start=p6_r4EF37DCE
⏳
فقط تا قبل از شروع مسابقات فرصت داری!
موفق باشی!
🍀
⚽</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2t8uD1vQ1slxmhdwC1fgc_Xsgl9g_sCOajMhTDSrXAIifv1ySE6UhPA6MvX5gk-LiZ8b1Ry1LSu-wEqrvmTz-9iB4YRmVFu2LjwBUcDCxQj19qkcuJcLQvvkL0QSsHcYPcwXXI9PaYaU7kMkpLeov_k0HHJgvNb7mG51GUhWWAHhXnzA2JvU6wfN0NE99K29-S7P5hnySNC7H4RaLrCKnF4WEsvkthDMqfw7vq68So3aQKvsDVmJiTv-Vl0u7Y2D89yUlExtod9YFNy2wYijMjYHC4QLR5-4AVIEVSZnfuq5iwqIl49hWM6XQXY66-3zFXpPt8VO06pBCok6YN0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XS2gAIResTXJjIQKfsv3RXXqVIEKRm4tyr3C7_MjlxYCAX6ly5l9tT4AV0sgrQB5DKMxF9Uh4-7z_BiSfFj-HbVNO5fuh4Sgq873wH4YdgOGrCjSBqRpzvtl8z-n5Y4gbGUTH2WqKdA2lmuQeX74mvxwdXHhkhGYXx-VbPel-xTSab1Yz-EMq5NbJuApw5xLrL509_ByDbCUMIN_xhG1-GEJOvsgmrtpc41vl3AcV5WIog3fa36zo5eSFmskFDvi0fNPwH_XjzgnP6w5wpzF5hadz-5WuyJvqtqqzgN9YccXrM5qcndx6rgNe7olq8KBcjZiGXUgVGDI7ar_bmsFwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=nrVUGGeLWKeHPxd2KYP8FubwkhHVDprxvsSQmUlsCvpcJ4crvRSpOD9aMulLYyd4n7eYzBxdMBUyzrio5gXGGkJR3lv7Lb-F-Q2KOzan7-eriOF_uKEJ1_ND43_2Va5_kNu9DRmuOv-YuzJ8vemmet1E6QNTRNwh6m7TPpzHOGqon39TtXPog6z0jDwxmC_QYUjO1ufchCJnTbTydeepcOjUS2OGb0fjOfn44Y1NZ_SyzxLcBmb9tZvqhk8fzWvVOAPkX98w7WmR8MTCEo6k5IPxYmff3RBFuhKiF467GRC6Z0BxGQvZjh2xL_EuLZpXCsLdCJ4tV48AfEKVR8PyoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=nrVUGGeLWKeHPxd2KYP8FubwkhHVDprxvsSQmUlsCvpcJ4crvRSpOD9aMulLYyd4n7eYzBxdMBUyzrio5gXGGkJR3lv7Lb-F-Q2KOzan7-eriOF_uKEJ1_ND43_2Va5_kNu9DRmuOv-YuzJ8vemmet1E6QNTRNwh6m7TPpzHOGqon39TtXPog6z0jDwxmC_QYUjO1ufchCJnTbTydeepcOjUS2OGb0fjOfn44Y1NZ_SyzxLcBmb9tZvqhk8fzWvVOAPkX98w7WmR8MTCEo6k5IPxYmff3RBFuhKiF467GRC6Z0BxGQvZjh2xL_EuLZpXCsLdCJ4tV48AfEKVR8PyoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3FdtNyarYvNaim0QAkpa-Bi5YXq_6ZW3OpnKTJgBoXdKMPjX0Wrx1orowB6815RmOR5L-b-bHLJlOZaHIBx9DTkDqZ5qijdCz_mUSlShV1SKS9urdpOAJmP8MMMW8hkOeE_AboDkskEXrdQwoP2JD2pYcgqsrK7dd0ME7RAr74LC4l3bIxDsfS1TXcGHudGcK0zs6BgK78sR36F1m1q7vPcw7mhHUlA0W8VB-L3CRlDsWl7PcBXJ87TgsvAVMKs_zCtQsadEwFEfyrZhi7bP-M-FKABmIAvPPGkA_VYyW3X8rTF44S7etekIT4vhljzGeX7BKlebgiex2w91xV4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it-RGAlmMjjx5DF2FItXtSXihYCOQinT07bWLP9SblD1fAt0YZ4Kyi8AmG_UTmpj4pknMdueB6A4CgNKHRfG6Df_6MPjoNqpmrVKIaZUl5FwiHlcutP1KFkUk3ytZZBeBbSS-0PWU8h1TiwZt9Iy_-3WNaupmAESgAbCLSmlaPNSI2SeqwgLWiXOClOu4OlSIDY9_4ayd230DE0hPeAIfLOyWbDefh8Izptriz02lGGaVBUl47JbfaHABNvs-LvItI8juU6ttH9TrSFyj6Ny3yRWESxDwf-Zd5BrAMBPmClZkQmDpeBA33bEvWnAfMWy6UMXnpj4lM0hAVJW3EMIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnU3HI9ETX-x70ixZequPC5atGV-0GvsgpVBxakHDEJNwFFIq2nPKViX_ZgOBHpWmVuqcCtuxVtyr1MljEtp7dKN3xzKr-E0sRCEWvFJiBzU4YXIKqCcTWWtbnVA1BB6GNbeciA28aym-rsd0tGvl8nQR6x1J1vCAIr9Eiy-xrGmWwZYXsM0pzZzY3HsvqmzDbxBzOzJCeDEEoqSzdUjJOhRbq1taR5fnQoTV1rqKtLpWV7XEjg5RUEYpjgasssq7GvKTUkV_YOt_qXRFkhBBU-YEk78GtVKKrt_-oR-C5Me7Z8OFmbFsT3z8LGmmw59EIEgiXrxXnaWyXc2bht3ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGcWEhmBwk0viOS865PcKGZWbJq_ySyROARLeKYpfWwdLdp6L2LBf9W7e2RcZ_wUzPcOQk6oh52yXrcI6JT3C4oplZlA5_1RNzYR23SSO7J10VtVgsvFGXgZ1kAdK8Pc5Te2TpGxuhvLpjy6aYzqvF3nzibFQxVG0NIBKXci4TpE_J4I617CAIBxGqMOo3rujRIz8iUnkXR-Edwaa9pfY0-N3wgyAVpnKAHaQZo_MoCqiAtCl6HdMxHfqD0j-qLN2Kmr-uXXo5YJkpIPdEKS-Ud4H-yw_5IqOllozptqTjiAqkRWyhl78n_xhLIBMiw4OyHSIv7FvzZzdXFDF3GUPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayAvbqA-qRu5ALOMxxOqCh-t3Y7tcLLwEa5HTqBjnZ14Gzi_R2FwGo8LCovzydZuT09KdMvVwmYaZhifA0kY6-lGgaoUBfry7ca_NEsuzc423izZtHqaaPLyWQKnrz-9hULPIcNR2Gtdl3AjNGXpZtvzkx8IC-Ong67EOdrBoaiqdyq2_lKPa5aGUTVJ0uifFz9EQ0E0L9x4eEnmpgH-feFmhkP-JfLM9jrmbQTVn7xx2MU6aOeaiRI_FppUveC0xob2HL8AYjSUf4qo9y3heJxR_sL-IMr2dSWnzsZo8QtIC7pS3g8KoENL53inmHRrMxN1NjvSxAtTGMV0UNEksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoYQEm4QdRUh4iyoaL-iixJOAaF6np4y9P693S_tDZmpqqBfM2G3v6RkFmhInqPKnseoBI-sc-N-avHNjICnIgh84m4rS6cpl9k0yj_HRix-hBqnVyqEcBg20c90mz0NQfakznUTi2ZJva328JE8P3pRsLFnKaoiVz0_QGWm58BK-6lxAAWgjt0nIlac4_c9Jr0f-_evSdITKKfS8YIGY_2YYBLNeiBozyfTS8rc_K7jb8MlcH1azo4wwk4XResUuSkJmCYq67JPSzf9bD7LB8yUwJ556Kg1iqoVF7JEeX4zcPSOf-qi8TTWDVbR5uART1Eww8zqbyi1eqrNJd4qoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEJMaT7KE0uyruXKSVrvNUtG49-g4AuI4oncuRb2bYqdMziPlbVD22IkWSvIIuE9H3VpOack6xsAPZMunmxSdRU-sOV6c-C8Te0ZFRAYFjc2br5992KMv_Z077OnZhh7Y8dYjPe_5wQ9Tf8xOBn2_kluSPJxw2nPTTdv7msOEC-sn-OAs-2uExl6-rXOAIfjkgX9MJ8grjkIVVmSLZOe9dne2Cd5xwSFdBZjIvqkcktV7kgX5DZmFFPv7ht3iBUEeTuYLfhDCbHV1oyhunJwTKuiB0DRVHJJw9QGPJF97PoYyXzGp1v9weKXK-OTOsUpjNNzb6NyxxDbHubWIOp3LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfqLI87A32QuNz7VWTqVY7DiVVO-D8bq3e8G4jYBdtpD6z8qvW9IAYzF4L1HHrraY-VBNbLDXe0w-CXzJCdYwuFy4BjwpzCzNl8Ub-iUfc-Y6seMR42ntJKaYta6HG1hGBsqktAiLjtkH_bJn-CGW36q9b9HroGERJKCsZWNDQc15Nhw9TBjgyz5NaLaID8BAR3ko2V2hQSyt0diGdQQryyNRxizaDgPrVddg-i-0JzZZb0oIYWpcsKUaz63k8X7ImAMlmnbzwEhhld4Sxu3YG0KwOiUlsHvX-wmsCimcV_k2N2SHSlpTtYeKwiPXEL0Gn3vNRviCsnAzf9PoVUaqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=ACXu1gNrFnhz8tLe2kdu7q307WWbM1SZKm4MaaXBxeTlW2wmlSDZJnXVHXrxzZfbVQAJXhdLrRnji7EFzZmTivmDPFume2LoaZdYrz3-r6rqPhiFecGxaQ9R9JauoRarmlZSPP9xU7eZDua4OQiB5WPY7tJsnMIOKx44KZrA-tdiS-XXyiPgvMyK-uvOe5u3h-NfJjqUEiDLtMtQgfU9T0NxBX8dTEtQ4X2PCsOW2EcQdNdTPnj7B2NotgoA4L4s81YfvpbYdlvY9xXrjwkMpgONZsFgthznaIaXSf0KFm680kcgSDzpy88tpRwoU1XNgfRKbG7Fj-iGzjppfsbCSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=ACXu1gNrFnhz8tLe2kdu7q307WWbM1SZKm4MaaXBxeTlW2wmlSDZJnXVHXrxzZfbVQAJXhdLrRnji7EFzZmTivmDPFume2LoaZdYrz3-r6rqPhiFecGxaQ9R9JauoRarmlZSPP9xU7eZDua4OQiB5WPY7tJsnMIOKx44KZrA-tdiS-XXyiPgvMyK-uvOe5u3h-NfJjqUEiDLtMtQgfU9T0NxBX8dTEtQ4X2PCsOW2EcQdNdTPnj7B2NotgoA4L4s81YfvpbYdlvY9xXrjwkMpgONZsFgthznaIaXSf0KFm680kcgSDzpy88tpRwoU1XNgfRKbG7Fj-iGzjppfsbCSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5Cr-rk4fZLncQyOPUQU8erDEdERlmSzf82SDWSUUSl4uKTMknt6DALXGXSDANtjyDnzyDeqrtdb1pECd-VPmi-b_wnaHOV2j-ccXsunTsT_W7auaH0jC4Q6m7D2FgFwaBvqiuMKyfVoa44Wz2RWOba756Bj4k8-t3XVfKpXtgFSSKSjkdW6MAmYLW_KvLHbFy5dWxhRvyfR6r3Xde9Ydecpbe0HaHKonuaPDtfnFzjEw5xmim4IkoDjiEc8untE-zFuLHNADnvqXW9TVIu35r3yMvrZTqml3qO6uz9am-94XMoaTHuc8i8JdJlp5rqrdZLJ11hPjjONt86BIwL7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hbqxd8gLR0WWTtzPETIdik9O7pjn7eFQayRRVF6oDMOgNu0GpNEbrHCwNK4GC3eY_s-wnk9AJrXBPEtOpFUPA2ZvV24fT_LiPfi96KcsounhxgnvxzjPeanFMoJQ7_eBITnh3d71NBwCmRr1L6jqKWfrd0Mpd30UQBLg4NcP7L_-vn_3H8pFeApwQ5ODHKjRL5KuQwpASYjw21qeiwHerfoaGy4vgSlR86IQ6zBSvpQkwS5aBYc4B6fCgB6R_5rLBdMhiiRz-yRW7ux9PcKxgUzluXtVGUYFW8Kd-xLZ_ohgawoK9nUGonP1KtV7Y26E9C3M_FJhEcG_h7I9hX00Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOb1ZuG5jvthMMkXLAYIT9knXbrxDC1_5AsWb4HibL9fDCOdjzHLb0g3gS-5Wf9LKXK32P4iz3P4gHozA5jsgJfd4BeJlbI-YwUoXdP7pJPvvZFBn33a-_wJKW80xbSy6wcL9JJ3GttIVPqr2LAzPILP29dzuus2HMhPV4GlAxOWKGayagIV596kqPd3ILmYDpqfHVP2-zVy1eiyd30_XOJjUi2XaAgEzFo_P0BBaSQdJdJXkQaChvY9HT-47dnwpghsdtnrOfzGRkMOD5YGs7STYORrVq0VktaQWMGqc12boWnryw5OTQOnq49u-2wLUc4tcXhIMSktijdWQTLJ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VskC9ccT1WFyA_uPa3wnxFEGjZetOEMb5ZXqSzvVtPojppdJRxGub3lA7lNBtP8xPoWqEc59Q_DzDl04HwQ6tX1BEJWcK0uTt6YyLSpvr84jpsCCgFDTMeXqtzG6Y9NcpyZ1z8Y1Ubt5QXF2_gIk4InYvMpHHrGajoCIH_GyuIFeZY1SwkNLoBrywn7Kin3s1CKAIg_7Nd84yrqIhzRA8CKZzIVenGOgqVikl9j8K6kRp9kqSWYiuNbnoI_beJL8XQm2z26LbjL9MrBh_t_87pDOj1KkqKxzi2KLdLFrM3TkK3skpw-b8rD_DO8-3wYH5XfAM4vWelvc-xMyyRU10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJS8p1rKBqPQO6jnt5UqTxi7ObGXnurwbPVXJyLFD1cljiZt-QVQEyPgMe-8yrrAYURymvczBu4kyOuu5JG4zbUfQdm9p_mZvTCp4EgxuoPmZmenZ4_67ZWJiIeHlJ9vyfaVV_d9TOWTphq0dTE4KC3aSJDW7l7N-zOfSEmw7AegzN0pfVOSgCUKWjtDkVa69G3M0u-AFnHmXP7vSzalRTzuTDpklbQxyE3BFwYgl0ep-pMhhqSROslyE7oBHzVWeyX7-nplziNNMBp-qqmnaL-_eeJ9eTxRHA1ARDQCTZtqSr_WUdr2kDIsdkfLfPAzVyjHjg2Em8ZLSm3qAmvNXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzjCRDNsLyoavVWjGlDh2VpKFsUlE0uPef0Ug6ITtjPuMUxYwksgBo1EiAYbcqWA5iYQwI30aKK12e2UKQQfQBQjFhJ2CBdJdRl11O5f523IU8ortNpp0d4YwJbLwnz-b_eJ7Vjk98LFnN-V3ouomdqDRfFoTZ1TXZ57UQPsm_xQBtp9Q21Z2YteOG3b3Ex13i64T1Wbp_Ls3smhvJxYO4NOSRWgTfeoCO4S8UdyQyAiwYqCbtqCTb-4qy_9H1aCBWT7BmoFfjlPiHeEI8ysqXymSXwQT-RYnQrZLzeAZ3KAQN2mIKskUm8PuX_V5-1RCg4YP2_oFSmg3_ctI2msWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNLKB5uz-XbM6ppV38SUsfv8dzrTbdfoZbN8oOAoJom6vQKn5IzPKsl9za23KC43haGvE6HbBT6XfN-E8ZsBSVoV9jW0aju7h5IJUuK1BbUM03W9WuV8spcgIhcM7JXAM0ugxUIF-fx8o0XkXgCqoKzkXU-mSn0RWl-oeRI3hG-sRL9gxyUh0fY98StR0ZhWHqcWd9xdAC04po2kOcUFEj4nCznsTTg2tHERtfmWTh7QbT7ihWTcKZXRt4VvcJWYQsL-Wap0ZgpiSNsX4km5pELmySy29UiUI8D4A7WWOb1jxRbyRdAEdOIheWmohFeNozFCkmzKeKi4Fv-oW63ppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYySBErFMvHI3FX9jhN5TzqMWow-eTJ9gkgNeJfWsplG4Ked2_wXUPtB57G0obUg08aJtGYkRW15LhVb55dAi2WjhtitwVD3YFepE7Nbbmbuj_1yGXNhEV3dksowxnJtSTKgIEMuV1FEx4aoYkhgl1Y3WTBCZ-kP1-f7ku-LFkV3NJsy3lsI-Ars3ahzajgLi1Da1wopD8qEjych2RRGy3iJ3eIgSDyZGRBvG38Ep26RbswKlP6IW4mA3NKv1maHNllYl4tGG3TS_-oe64wokLz4YlbhU4yRKov0eseFA6lUEAw4f8aoiAssMOvRi4kEiYqnKnrWiWdpHZ60bL5kFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#اختصاصی‌پرشیانا
#فوری
؛ باشگاه گل‌ گهر بدرخواست سیدمهدی‌رحمتی خواستار جذب ضرغام سعداوی مدافع‌میانی 20 ساله تیم استقلال شد که با مخالفت کادرفنی آبی پوشان این انتقال انجام نشد؛ بختیاری‌زاده به سعداوی گفته به.سبک بازیش اعتقاد داره و در فصل جدید بیشتر بهش بازی خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNvkEVmGlHocKFG7D5REA9z10ZhhgpzX8dgDFbbaK1HFWCDH7pFjyP5IOgeMvnzabbIqJ4AaEzo6j9M3uq1qdRcs4RnIeMrKFTl4JjnpJCPx_q-_Gk9J-29DD2HL3YEqDkJXK8xoOPd9a7E_ErdOZq_3gRocnbKP5fiEnn-z_DRRgnp08xMiO71Z8kj4E4c007uXCd7Gdk6D-W4Gu_NyFQATW_7u18InvP8UP_sXB3H-IDccSj6cYET9FFUx56qRbOFxxCrnKTp4dWM9AoOCHPD6EvRu7SpTFcVkOZU2Dzk0JqCrmH7-ZV26Yw-PFaQl6kVQoZj69CnPzom6qitF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEQQuETDUV0uKV6O8mMmfdPTavwqSIYlAhlXnHkMDgU3hpLcHmc-nYCOJXRHjFX_GbsClSqb4MNFC2E1NjvUh5OS2bUz2fTdL0brEk2zXM2j6k2FqYjSyDX76F7DtH5y6taO515vePAcvYAjuXFaGUxi9lu4Mo19jowZYjjHbsHZw7YA_PpZ9Aywo7gTOrgA6I5Yu9teGbDtn5aFR6fpHjuFIbmmsu6DZhpLXCoVXmG8rT1ymdVBveiWXeogaEaPTF4g6s4Gu_wkmAjcg6JphDAO6XXl3b5N7XZeYU6rtoXFJTmhYNU1Xid1zireR006XuH1aLg4B_0DuuJy0va6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IktZV1WPiAqVubSD-iT02ecAE68l6fDdPmo1hRUX-vH00WVHP889PGibJdW9WyoI-W6Px0kQlWoXdECkOpJKOUeOPrp6w8go-yJvBG56oAAZZUhskksg6RbLczbCu4Xk5-mZVlqY_5umKp2VB38ed0QDmltsHjdWo-TM2YM3en7EYbte-4GozmhDs7C2aHa0qqClNTdSsB-xlb_tweVXddU_OqsmiVZLSzjLfUyfji9zrAK4z9y7Pm57OiwDOyZmJGNKW9M8yGpd1krOrtx15NDTc5zghfuiCWwpDLFjyJBK1bTHmurlu4sfJEj6jfjGDRehmxAq0JKiDHAWNgumOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-qJ_LoAUUuvrvFA3QFlFaZWl5FWQHM7Dm9KU7TBW7UyXGxk_oLBSKCkuJCi8lm5v0XGIq68z6xRJKQ7vNpZv4ZWmQhNGNNF-bIMRhAV28-j20Lv2Mfd6-fT-doKidKf6NqEcOggeZH9lOiQrrtX3bzSkk75N9lV3-tL07XFOHFJ5PFf0DCyOGZ9-nN5GjA4aBi7dM-u1s0zVMNkLl2UkXXvTMW6Li0VvYVYjJhXrGmi-Nx2mGTFBD9tWXZIu8UESxs95I-9pBGP_KEgefZBXqmSkZAC8FV5NPkQT6iIRVwVFEljtXD9fFXtsF1p9Yffisrfo042mjjRE54p4wxwYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxmrR2VJbzmPpwSH5jhspzqGby6gNDUc3sBxbndwFJJprXvkJWQEjInUjHS6OiO6qCyR8W-aVVhFfVtNru-5XQXdPz__Ri4GY9qq16JkgIWMN-rdt-WgiBH-mvv441xjaO1ak-HlRR9XkN-Vi4QcZ9IMGV1bk8X-PBRXk3ilxOy6U1Nl0inLIhqqdIqPwIT-VDg7pCuC_SKAxk7mXa9kmS4nwoIL0X5FpowUpA-lYXi-mrFWl5RI3_YkRE8j4A3uo_qIuMUfQlBTFAC3ad-IErTJpiaAH1jz5jE-yVhdWQTlslnCuqCItzZS5n8dpCEk2lZJwbuXAc5ZDYfD_JKGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LytFThvw8f00ulOtCG0oM9ekrKcUDb0n2-aJQ3DMQC0FOz0rwYtIyIV1PImhSqdALqomofNtQa-R6S-P2A47L0jT4xImS_AHvwEa910SV1NYqW8VxCS4wx6JeGkMMBZ74TqTxCwA1l-lw6ffow1fKvMGmiS0jzvxae5qRN1o4zXmyW56RFq3zqLG9gdFb8jjzOFtRiGHNCwW-mmWz6oopY_qckuwlt7QRIVO9wSsjYdXQCfwGSEA8o6cXF3eddIF2qgwqruDVFxW76gpY6jfRVCd0ASIkMsEVvqFduYHbj407CaAFrOcfR-uw75P8MUaJI8lGq8G6d5zl86VM-kJJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=ApQ4kXJdatumAWSRo10RIFnZ3hUcUmw-AZdJyknz0xR-3kN9ZVPuSLjTskL_lMQLp7erH7RqvCBzxJjrmSerGv8TV8KjhNlKdPbI2t1tTXgWbfV-xjjJnH008r28YLmM7qxyB4Z2GH_yekE-8A9H-Bamq7-dNwKBiM4tkv5sNboYvdBbRNBzNwuQAwXnXhw7Uon9FtQegyGJ1Nv-bZhkrMtZxocPog0uYNPhhlCC1BFJ3rWI_SC5Uxgl2x1jpi4NnEt_Em8Pkj2HcrBfht25ui6pk1XbRXx8hCn-_x-nbZpuGEIO-NYy2UOzqIVkG5Te3SHW0hYzxlin_sD-KGcKCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=ApQ4kXJdatumAWSRo10RIFnZ3hUcUmw-AZdJyknz0xR-3kN9ZVPuSLjTskL_lMQLp7erH7RqvCBzxJjrmSerGv8TV8KjhNlKdPbI2t1tTXgWbfV-xjjJnH008r28YLmM7qxyB4Z2GH_yekE-8A9H-Bamq7-dNwKBiM4tkv5sNboYvdBbRNBzNwuQAwXnXhw7Uon9FtQegyGJ1Nv-bZhkrMtZxocPog0uYNPhhlCC1BFJ3rWI_SC5Uxgl2x1jpi4NnEt_Em8Pkj2HcrBfht25ui6pk1XbRXx8hCn-_x-nbZpuGEIO-NYy2UOzqIVkG5Te3SHW0hYzxlin_sD-KGcKCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
خواسته‌تموم‌پسرای‌فوتبالی؛ روزی‌بخوان ازدواج کنند و بچه‌داربشن، بچشون‌حتماباید اینجوری باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szkV6OVvhRPwhvTa8wG8tl89AgwNkvdCzum66llyFcViiWIEc-syoXxiYO96LTgve348rZALLZqfyjTp3_wTEcEqRkVySC5WHAQWGlvNUEa-ZatLI_wBu-s6tau_GrgzQZYd0IZq8hqYxic18yWo3LdEuM1MqFOcXiOuJTCsQgW3QJN1a24kobhogH7rDIK3F2Xpe90BvAAJcisu7U7TldaRUI0ypdN6Df1ajl83IfMnEbGv553E_QWr2A2mMJaA1Vr35nCJJDAxrGFB40wqbEVCODsXzn8NtMCBSyQ8T-GkkH88pCCADDPfaa-CYrmiu9fiTIO061byX30rBSS4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huhMPCr7vWbm6jdDCvJ71KycKf3L08dGiqQeB3Fy5ZQxfYU-Q_wK8D8wiVBhwYkY83lvqcEypBPWVMtbKJqpyBeE3BW3bKYkuuUVWsb5i3rNbqe_KpCwd6J3KQYr0eG9yjFBVmfvsLEy_1td3M3bLxWBpSJRPKZdE2dXQlvSdecnOLPbBzPgrsUVM7IUYGLlKw_H9KgY2OTIbgyS4wjTdc6KnWXB9MS6U8FVExn5OXG0_savqF7afyJO9Mtv2rIXmljbvwtkostLXH7J_VwyOoy9a9ajTmU523RBYl8CaKLfo88gmBR2jj2Nlk285tV4yZzPI35qqhOeDKdUJl9RKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVz--14xEDy0JmQ-gJ5Aw3qlozgxrWdhONgd-mi0STWHZdfi9kBXFhwb5jQPwzNKW-8SD00kLbuj-jmdrI4uedgxQ01FUBwqYZKWh8L6OqXlH_kYFBfo_iP9C8ten_Ade7Ew7RfhRERkgExgrlrutWGXBVgBR-5Y_4caNuScAiNlCdtLihqWFNevR-Qa7LOD0ffs12oEljISE9Yk42Ock13YM_ddcl_3XOBsQrZ-PalosN88tHEUqttKWZTWJa1Q526y8oNp1XBjhA2j6Kfi1P9P1L9yHlVqkbw_91LL0g1yqpusqNimkukHw0UWy-3OJSEzFEJiSo9PI4xnfRmgMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkLc37kjS5DJYTIcfXpWYdoGrbe1yjHvxTa17klmQKOODMAPmkKRlOwT_QFG2cw2qKy0jojzRQMUFT3KRMi82unFGhGALdQBPZ4arak0HKjgg1_1Y6iuzxUzOUnGHlbmk6g7tpF_53THeToiDC4oB9CmBPU66H1mEiP185__ZrhP0zY6NEU8_-iqiO7iqHrWpXL8GLYpKeBw47_CbDxuN5k7nXXukwvrsQPZi3WVwepCs7cFmy1YGWupgAVSnEj6Wum6Dq9B6wxZ2Wcbk5hnRggcmWQk_mW1a8Ni7zGW24mcBU1Xb8XW8DvjxpWFtv4RX3a9DKF8vKwkbVi7et4chw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULDA7rQmP4Bde1BvCOiPWKpghlHZC_Zr4K8bkkGG39ChGZrUSeIUu0Gk37soDDwMYNPb946DQOauG9UaAt_AZGe1SxJ24NrRRAhT0lak89yH8yNu3NJbMvLtsqPqf6vqRrYtrTudNeuceXEQF_OUft_-arjTA-KrCEpTQXurwf6Vkfr2NCnjCQxM-rP_3UKCiyS_DI8jyDTmpnvD-98RQP64_GqQrAiSK_KQ0z-0oklMrD1SjtVpGipbDQt_rhyA1ATOw3_yZwqB5uS6zrYYr0bs3yOQKa4s68Vr9n3NUHBZDZapWtYxbwT25BOVJQLWMHBM-M0rEEqF01Uyv4x7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QbJ_F2xeHb5MYrTcbvEsyB1Dd5hJg4C-HK-NQD2qHFUKmrmKsCIiN0ZFQ5YJBWf1EPE57wk4faVGROIbcWagb_NlPXs5rarWrTj-xSjBwr6fgsYd1ECe3pElm7mx3-2uOecKflEkq8gjms6zjk74_nwjr4W6ZN9TtSauI0WL5svFyfhDDiKwg5r9s6i3W8Df7hh3zwDwdxQ3AMbkPqYx7cdYukGwq13yQ6Gt6U6thY9NiO66Vt_NUtVSheyxhAKgA2WNRrE_2HQv0gLvizOmXCGl73hpWZhYKhtwbCWiivRA3EVGDZ2zWqi5NgeF0dmRqZkYZG-AK_v-Abj2L9Hs2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=DcBSyPxMaqY1r0BlVTQ05Jt3OOvGCTyCHHbO3M5W0dW_EfCBM5JprUuelmXVvo1p1UsHzaM2QTgO7EhQP6jktVPBheyg8hLof6GFZ66wHmRTRj1ITp1o4Zmi3McrU7MnHcuLKGKqUiM_EOiMR7RQvxdjkAA8k1NyQN1zCeqogP3UYWq9_UUjlG7oNiZIxjzMHK_i7R1_Tosk5z5-N1YaYYDLQ_J7yIw6Ec7-DN0qCkqL0L7ZUhT-Q6J7VSCFWta8sDNs8DW8KFvrbBP5uZemD_lznuVfHah2l1027CwHImanZrReQm3rQqU_UQUCWUky-GKABmstw1v2Pr4Jp_ZmLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=DcBSyPxMaqY1r0BlVTQ05Jt3OOvGCTyCHHbO3M5W0dW_EfCBM5JprUuelmXVvo1p1UsHzaM2QTgO7EhQP6jktVPBheyg8hLof6GFZ66wHmRTRj1ITp1o4Zmi3McrU7MnHcuLKGKqUiM_EOiMR7RQvxdjkAA8k1NyQN1zCeqogP3UYWq9_UUjlG7oNiZIxjzMHK_i7R1_Tosk5z5-N1YaYYDLQ_J7yIw6Ec7-DN0qCkqL0L7ZUhT-Q6J7VSCFWta8sDNs8DW8KFvrbBP5uZemD_lznuVfHah2l1027CwHImanZrReQm3rQqU_UQUCWUky-GKABmstw1v2Pr4Jp_ZmLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IydTEAczHjxjuV247HhYPFFSJXiAnumP2YS_gFdeSsVhN2-kUCRTr2jd04IIBd6Nbd7F-vaufX5liskLufRdGhTRxmRzwBAsOLfTbFALd0E-MryDAEYyJVfnAS6n4jVNF8tk52qOudTEUojCbS898bFohvU2uH5PoABdT_yI5pT65UxgTJvMqzip1jfJURmC_RM8JB6m6VsCLXlRN2uzqHdHy09J7vtHpFQlnV4FBAC76ihOuOtPjvNdkZIG-j5sjpKmdj_p-nkxc43SiZldd0TYfHuoWoOgVgQuVQ3hqOBE1GBT5O1hTaVxAtYcaCHhA-b6cCmnn91CnY9WlpRyRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZME_PLAbGD0uFKcR_zzfNvQY9uW6n_AoThMPWFdFMpQtdZ6ESQoUSEY3nzZgwTWQ2tykC1L6LA1W-JKqZVWR9O5GKvE5fd7xo0TW9T6UO9-v22O4IX4WMSKmPGTafzjTZO1AYcIhFYKfqlN3BnqMyrlMCWu1p3j-W6YbpHHrN1YXrqemCbVkK-W2iYA262ik8e5GZvcgSpb5uWPHxvKDn5xPmEmezS4AhyIPqUlAKKp5WuP_2iEVS9_yNeqmfkfCtMTTk53fVCjFKoYSyGPE5toZVjX6MbBOYBGcl4X9suj8L2bPZ2ud88sH_yfol2IuVPk_EvpFM3N5g-HriMq3ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eahsZikZU6n4l35_qEu18OCJkEvVe6NmmHEv-rvqhN2teZencpZJOLvBfWc_ppsHQSLtZCC19bK-YlNogRisRVpn0IjjaI7tGAf-6FsoXc7g4RIGTlCo1u8s6I5HgsixAl1MRqkrUvqxMMUGVEzhGue8_JOD7nNRWPyi1YzRtK1ZcVJQzTn-R299kRXIecm2AvM-TPZ7QKPj_YciVQVgia1WRGacCYiDygRYvSuZ-m5Rc13a5Xg0idLRu-YKEeuJXbTh9xgXXH_aSW26uB1A0SB87zV0Ycp-YC7kEidY2y07wpU6VccgzOyyvVPO-knoAZCZToFANQHzboZdOpUJww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWEAn589c6IR91wyAJdVfGjagKpu-yabjTK2Ks9_OZ6XQSmLfZnvsJxq69M6Z8u9ah3e1QFBaaGdT4gmJ3Iz1MjTuTwx7dzbN88bLwKPWOa-ZLJW8A0hIdMBZVVLS7tb2AA8kW2slREqxXOTaBW0-1sZlI68c3WnoCBMM_g5cD8YVVGWh_BhxMyfhNJHnfQbhEkEOY7uicMHOyjCJJcuP8OR7x6mTl3B8rAqzbK992uMSQQDh9ivcqwJkeXgWvHhwC644yn7LFKT_MYYI-dncwkEwnd-z6daFc51zf6PYLQ_yf6wTmq-PTrUKZf8IhqbnzelNP77sbb1Klwx5t0Uxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO2p3L4VacfiTZqFYdmF8xj178FhlE4St0bXJlN-4_OZ1F-ajstNeHarsXhMhGjPUbVIfel6GEU3658BOfixekfdffbbm-uNw4R4z5N-r_cevgdijInz3uyg8-SKlM53HBNPFFGEMX2aJDPu28KFDI9wl6MMQaZHZdmjHzHMJ6tHN2dfGgkgUKQFpo_vbwPubrvf6Whm2S-q-Tt-BP-t-ODXkHzwtmKqKumZPBHfpswTay0YmK0yLRwxjMEkPCEjtPD983TwsrKL8rk2nJGX2RjoIateKgV_LDawbHrw3C9MvjNzDYF_qQDK8FKMiOj04n4iU5-wYkvXF_iwXEgBUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ7-_v8AUCjI_9wBIXNdvHvk9J9H3ZS6hKhcY_B6k2Aml44epkDPhZkVIkeTJa_oYs2m3_7TWP4qpyBdGJs4l_PplcRo83O070awFRJrS9BTQMafzgl8Qa_vcgqnV4C2ESqJcfa9aEXjmDS5F2RMrdGxsaJHhfKTIU7LwIK2RttF6uL3eAEwxJrpVCVVav8gCgB9vawvgOfZEVDh8kR6QLhKDv2v_MkviroqH7JGk0dLMyB7elj_cODdyr6Z4_1fuT3Gwc6N7CdXoNqJ8CcBP_WwZHGhqkxj1uFFAEKDj3CqzZm8NCPClOlguAakh_hY-3ad6AfjKqVux5gu0BGLEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq41pJRuz0O_1XS8eLEcmQTC-9T-LL3pfYF9HjRMdR0ZJTbFSOXs4ZTbM7M5HqZyPC2LX7jMJPI2gNOy2HUGv4RXXyCdY1OuaI_SahBhalFVuKu7Y365WeltDW43LRG4r90uF9mTF8_bV9q61Y2xE5M_30Hd01bo_dwvzIkPN4Ho9ZQc4O-Ra0g9p6vVwfCTWffo6c1mLtUCw1CBgMlnuIfVXB5hURQZatqBeR4JicT4DVHFC2-6wZAXeWkhEXM_xXtO1I1Xq75RarRpQy9P8a-INfErwSyFbb6M3qwb5Lz1jAts_VxFlmHsktgqBEgrupkG1l-_2CIE7DodZV_kvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=pJpIxWz6vZQRWU8ovBHC2L0XahvS9TsaLYHIhi0n7qHmNLhxCcJIjAiFrE_TnvDXTgn6GnW4qtgM5AT5o0XglK95mCvBFHT4tW0c1uzjykRQyghJ_mZwLZyL-QziXEetLXvnjSOVz9x0trh9HqKJxcH-g1TMtSIX9F9bl0yIm7iM4qnwPzXx6UaeFHIqNOVDH4PvwweHPzf3Ez9IBLmvAnzdSy4xs3H-nyk9vaQkr9xEvcfxjEoA9kYMghP2y1yP1-UhbIJnxNhvZAWSZ6lMedpaE6Nm_Q9NqpyKJXlDSOcuvaeng-6y0Z_7DXTpQVv4GOBtXJdQCMr3FVP-bj56Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=pJpIxWz6vZQRWU8ovBHC2L0XahvS9TsaLYHIhi0n7qHmNLhxCcJIjAiFrE_TnvDXTgn6GnW4qtgM5AT5o0XglK95mCvBFHT4tW0c1uzjykRQyghJ_mZwLZyL-QziXEetLXvnjSOVz9x0trh9HqKJxcH-g1TMtSIX9F9bl0yIm7iM4qnwPzXx6UaeFHIqNOVDH4PvwweHPzf3Ez9IBLmvAnzdSy4xs3H-nyk9vaQkr9xEvcfxjEoA9kYMghP2y1yP1-UhbIJnxNhvZAWSZ6lMedpaE6Nm_Q9NqpyKJXlDSOcuvaeng-6y0Z_7DXTpQVv4GOBtXJdQCMr3FVP-bj56Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌باشگاه‌رئال‌مادرید به این شکل از کیت اول این تیم در فصل جدید رقابت‌ها رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892129455f.mp4?token=VgxzQVL95Z8TXEaHABw2ntcTHUnPUh88TGnLXR2aBLty7Tyzj7UCgCYUYtixfkUALjw-OVbgiAxDa9K-3zNJvXp07Xr64j4pTm-vMihn9LRtAxVKdPDPMqz04gG5f1k7DGlVP3S6wUFC5aFfmqesXVshsqz4bSGx2YFLm70mhwn8xMfqegEAgFp4VNeEgyz6dW7o1E_yHl9yKmSogpwJNBiGDudUQGlPVO9tUKemS6ETakEiuZsYjFTvANt8TLFx81Hy9Z_gwz5wJSJ-FNk_5PQiMetMOqe4VtlFcrtpvzni0dsB25oEMYjUM4idYU1n2J-KWxv--Vi6cztXg3tFzrl6wqRbnRtDQgai8MmmxsB8UW1ksIsq14fiys56QI2zTlA-Aelb56zl93ov1R623HQ8gDiajyEpG5ahLTY9u0w6MQYTpej7WL2oxxSReNFi69Fe4M9U9eNkmABSuemfEd6Edk6RjHhyVYMzH2wssO4IyVhUYl_esaHhQGkOL0NVML6BbwXjgV8Lh3ak_rQG2KB0c-pjIYCTCc7vxgQy6LphUdm9WILfqF0sVaZSyDSjGzZ73eBdrxt2A7Lx7nv9nNDpB_lLSd31QCoWUWaMfwXWj_dkh3IbdhiByhygzZdtSC4YpFYKjljKOJCZM3We3duci1_b1GR0drNePP56aOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892129455f.mp4?token=VgxzQVL95Z8TXEaHABw2ntcTHUnPUh88TGnLXR2aBLty7Tyzj7UCgCYUYtixfkUALjw-OVbgiAxDa9K-3zNJvXp07Xr64j4pTm-vMihn9LRtAxVKdPDPMqz04gG5f1k7DGlVP3S6wUFC5aFfmqesXVshsqz4bSGx2YFLm70mhwn8xMfqegEAgFp4VNeEgyz6dW7o1E_yHl9yKmSogpwJNBiGDudUQGlPVO9tUKemS6ETakEiuZsYjFTvANt8TLFx81Hy9Z_gwz5wJSJ-FNk_5PQiMetMOqe4VtlFcrtpvzni0dsB25oEMYjUM4idYU1n2J-KWxv--Vi6cztXg3tFzrl6wqRbnRtDQgai8MmmxsB8UW1ksIsq14fiys56QI2zTlA-Aelb56zl93ov1R623HQ8gDiajyEpG5ahLTY9u0w6MQYTpej7WL2oxxSReNFi69Fe4M9U9eNkmABSuemfEd6Edk6RjHhyVYMzH2wssO4IyVhUYl_esaHhQGkOL0NVML6BbwXjgV8Lh3ak_rQG2KB0c-pjIYCTCc7vxgQy6LphUdm9WILfqF0sVaZSyDSjGzZ73eBdrxt2A7Lx7nv9nNDpB_lLSd31QCoWUWaMfwXWj_dkh3IbdhiByhygzZdtSC4YpFYKjljKOJCZM3We3duci1_b1GR0drNePP56aOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkhJBbmVl3nslwOA9nGdkzbtC1TOnYLZVRVlwV82gpugAUOgHgDPVKTpR-BNU64vHDgyvjCCKyPtohmrE9AewHenYCNrsUugVbMrGH54aCxxEeCD7HiV165A51XJ6q5eSOaTsDbJRq4xZXOX2UH_wFPXJxmDz0TYI2uOMIOgk069p2PaNpJ8nLBgsR4YlEkR1vqyizAldo8PiaO6pntFYs0FmrpeT8ZrYGojKpB-C_pQrZt8t1OYbJHJyVh5Sj_ykUS4V5Mp3Kx6DwyEhToKghIkUd9il8LHcWLIsyyOHh5QZKXWCfH-Ga61q6wDjAJYaxp2Fu4JQ7AyUz0OyNVFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1-kFuT9B-GJgUJeh06lJQw8mdijSwi7xEk8gmTvAyuy-9d2gdBw5zR6FY1LGkaP5jlu4fCkJcz5XJrd_9ZNWmvrEuxU_ACwOetwg-C7yLUVwFgo1dwGSnwZNqZ69zfUawC-QkTEJtJt4xPSvXI25o4lP-1V3MwHkY95pN603C3hhqn0d0korFL5CgAjd84ktpKE65k6cl0047PmbAfDuL5XYODWLR2V_mH7p1jNwvyRSbPrF2SmRtLXj2NznmfQCTp9L3tanelfsof51miCpsLcx6r3JmgswLgQEbA-Q0FqJQkZVt42S0bPtsMiz6_IVZEZf5v0mnupsGYZj5RCuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=TQP0dV3YTWpgbHy6ZI-DAA9-mX-LOphrO4xxOZBtuFnawaJRoMBSUK61HDt6WWV_I_4YMw22s8uPJVEbSU5KUdR-D0d-I5X0BjaIX4YaXKrjDPSUKKyvn4BPYOucHjCstuL_xXceSxvqIgeOX14BfK5NWFGI_Om1kixfQMF9E1y7HbmyS2HalZyvRBS9WpbLTFO3ugGTkImlbS2lOL0WdsseAE5WAjRrKy0ILkZBsk2igrxs-TIGFqYHcCuJgj0WiFO6gAlkNQs89R1tId1-7rQgjQWmpt4d3v9ymDL5tkqs08jY-wM-roYX6LCwcjmAZZx54EqWbU_2VIYTjc8HYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=TQP0dV3YTWpgbHy6ZI-DAA9-mX-LOphrO4xxOZBtuFnawaJRoMBSUK61HDt6WWV_I_4YMw22s8uPJVEbSU5KUdR-D0d-I5X0BjaIX4YaXKrjDPSUKKyvn4BPYOucHjCstuL_xXceSxvqIgeOX14BfK5NWFGI_Om1kixfQMF9E1y7HbmyS2HalZyvRBS9WpbLTFO3ugGTkImlbS2lOL0WdsseAE5WAjRrKy0ILkZBsk2igrxs-TIGFqYHcCuJgj0WiFO6gAlkNQs89R1tId1-7rQgjQWmpt4d3v9ymDL5tkqs08jY-wM-roYX6LCwcjmAZZx54EqWbU_2VIYTjc8HYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bviqL3-5a7xKMBKoU4Br0eMyOSRUKHcGxfy7ykvE7Q1xqH149lxMVQ5qYCSWIYFwWPqq6lxpxW0TuhVZ8B1ksfjrfMGmHLxzRbw2v6egFmAS2zzP9K1VgxgydBvLEMYXurZVUFIpBrTSs-2QwOo9AF7wQ6FtP6rK_MpcYmItvC0jw5hkxkDPqcVfaxCmr04GrgEDVXWxQwjE5U1mf-GDLhpEdjnWt9Acw4ieu4EBRblgqfEm57cT4GAgVWCLaVeHBLsth7vjp5ckzyEPuqizSiUCsLvaJKkuP_rqSTbEJVueoFOKzXBuXV-7hFswi2toiTN90v8X-1N4bwjbsSHIyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-XiH9clbkjZwqSPE9BX9WSx3f9XQUL5YIbVUpRR_IW5fprefQ0oabmqyIFDUJA_ZoHE2H1leombV67zuSE-tQgTmUOzMe1ep0LoeZwrLrLM6vWY1ypOa5TqRsB1_3HqI0yxclIvf3ZpsWlM9agkC7IyIr_jsYj1D7GXe-jfxbMXnqsXfDL5L2U9LxZ8tTImzRaWhnLql0dtup3MBauarfd4uCt_Crtrhu3g_eaIrEeGYzz5u2NGykz0QpmgAfhiF8qiMMGsYeVEiaBgrYbY2_FTNESEAwHY5mYySN0P9vPTqjlHsl0RZjIhJbZd8Q3YEiD4sXP-K462UaDp-K25JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf45jGdLJxz5z9lbTRzbz22wia4mnwe7WvrQiqr7ZDfyNcyEtizbCsPvtyEbibREhofFFgcp24jDZtmc0xwxCxRFHtwdKBNTXdn9pBaZPwxU-JQn_10H89OujZKpo1DMwZHnzH5JjrzRo2_XXv70JYEGkCA4-3fx_IwQumrbHXGeJwIzhoP2gEuhtmch63egLk-SXPv1k5Fk_N3_lum3IxuMTvBu1DvojiTwQVHWu2BsMykHiu0tFH5C_MiqhoShLfBatKmOj0NmsGyFZ_sQ6BjYvGNtfvZPLMZZV0uzg_48QhHvSN6Tx8cgPxAiLTKOlhQPpdek1RywXAL0h12XUEH1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf45jGdLJxz5z9lbTRzbz22wia4mnwe7WvrQiqr7ZDfyNcyEtizbCsPvtyEbibREhofFFgcp24jDZtmc0xwxCxRFHtwdKBNTXdn9pBaZPwxU-JQn_10H89OujZKpo1DMwZHnzH5JjrzRo2_XXv70JYEGkCA4-3fx_IwQumrbHXGeJwIzhoP2gEuhtmch63egLk-SXPv1k5Fk_N3_lum3IxuMTvBu1DvojiTwQVHWu2BsMykHiu0tFH5C_MiqhoShLfBatKmOj0NmsGyFZ_sQ6BjYvGNtfvZPLMZZV0uzg_48QhHvSN6Tx8cgPxAiLTKOlhQPpdek1RywXAL0h12XUEH1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های‌تامل‌برانگیز این داداشمون راجب حذف تیم‌ملی‌پرتغال از جام جهانی؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucM6BPp9LO2s0fgSkAS2HE2TsmWMUfJz493FHMb90WzgcPUGEUlRHbeoqi98b3iG8U1auX8vxw2mVU2DOlY8yimu3algLb7O9blUrZke2msIesI0lQKavDPkOEXUVf7gw9Y6Vg1kIqMC5Fa2KlEH98q-HzWtC7qMZ04S53fDYGpMtEp_vFfI27yYmLBqZaVVjbheN00pw7sztKQ3UqPPXEAyWy-Q3V-Wa7D0wrWs5NeyA_utBpb6KowsQweCxeqAH9OsCgSRuXaSAX1cP1-rW_y_QJ-nE6-b241873t_lQT5XM4ow5rSVG4Hd3lhGtlAdPWYk-dJI5y1J-JfcbbOcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmuO8lz-2xc3VykF4LRBS4fn8q0XMgVcxp5kiOYOpMUiATNOjwvvFVZQIxQJWFm_xMBiEoYqeY30I_dXcvnAh3rKxAjtbCj3k_oyEiY6Hv-p6oOTKTn9PIVM1Jw-ZTYGXvcv7QXkHQxVFR6fZFEi8tcN7Vnf9hBhtH1wIBxiTuK4yDcsqtBK2zFtHBWxf6WzuabpUx0Lbz5UBouZbt7HMYqWLXQfrfNAuZfqzs5z75JYz4IBRhMoYQx8LyZF5c8SSvfGkidScSb0NcN17w8OUbfSL9wCdXfoTHTeOhxUlp_QOmykVQGU1jpxJaCdFe4rL8lj9xqTFYH0BGi3BsXSHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nszDU5uqeDjCWiub06toaAnnzm8UWZV6lpWmv4Ddj28W-6mghfmo22kk03T4CewuqjHf0fSATBRl_E_pO0Qwe1BGjGPUYvq6T6ngGeoD7VMY_cM0wyjUm9g4mxLqrZqvol1h9FuQcUPWK8mYUbNTael2Y5HAFIGOJXs9CbPOzL3wavaYBxh_bkiq0--zDWSi8GkgMqf5a5eQr-AVKIlpk8_8AnUWbsYRyu26-LoA61PCQgoVDeXhjJAC-q12pXnJSqmpuWkX3uEn0z-6Yk14hhTrKcNAwUFtuSlAvTESQiwHH0NUqXjmIYbLepph0wJMy0lu2RnpXR2jLMpKgK7wYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ 5 سال پیش در‌چنین‌روزی
؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=Fm1Ob_fKLoqO-6rcpv8nAHTv_nyBbvbYwC6Ls-aS_GUC8GgZv7rozLv-vbDdOe9YgJLMmW-fjgF2Dbk_dXUcHTQXstVZf45XLOpraxz3z0so1Y7yNbQq4t0RiqD8JlWNyBDgmXtk_XHr6g_3aXPZgffWpXKZNlt_ADaB5-TZIjDtSjRwxC0Rvt9fumZwmAMzvqkD8qlG1m4B3uGlW51Ts31mWzIgLKwl9HC16S-oMuAHthL9JQ83r4Smk3S7ygSkcdfn5h-jm4JxmS3aIhgXeOVpos6-eCB1GdyNnZmGr2LeglFB0HrsVAPqRfUNgCHL5wnMPAi_N-Dl-8mD3jVelw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=Fm1Ob_fKLoqO-6rcpv8nAHTv_nyBbvbYwC6Ls-aS_GUC8GgZv7rozLv-vbDdOe9YgJLMmW-fjgF2Dbk_dXUcHTQXstVZf45XLOpraxz3z0so1Y7yNbQq4t0RiqD8JlWNyBDgmXtk_XHr6g_3aXPZgffWpXKZNlt_ADaB5-TZIjDtSjRwxC0Rvt9fumZwmAMzvqkD8qlG1m4B3uGlW51Ts31mWzIgLKwl9HC16S-oMuAHthL9JQ83r4Smk3S7ygSkcdfn5h-jm4JxmS3aIhgXeOVpos6-eCB1GdyNnZmGr2LeglFB0HrsVAPqRfUNgCHL5wnMPAi_N-Dl-8mD3jVelw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آدرس خونه و محل سکونت بعضی از بازیکنان مطرح‌فوتبال‌ایران؛ هرکدوم از اینایی که گفته خونه‌ هاشون کمتر از متری 500 میلیون تومان نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=ExZJqkRZ2rFUJxx2OV2WnIvpEy586AG11_eXcu54whfhyuhTybgQlkPLNBfGvAAa9sGxZXqxKfZaVoPsN5WseNHd4xq0m6Sr2COByC1wq3UxcQaphkk3gIwZ0nVOacPFLitG2codPr3cgzz4qNBRYX_eb44gpyTJrY2e1Xj2OhYoV7ICdHobg2Tl47axdHlP8TR8EbF3Cl8WQ6T80mYS0_UYsCFct86lWnf0Mu7zIxFkxYMjqIFdl1B3bfYDOZ0_InffsapgetAm4ODXMtuFRnz61fj9fUpbdGIokYW7bK2U-qyaIa_eNFgsgP-hRBLIHs27mFH-5_0s42FKOYocoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=ExZJqkRZ2rFUJxx2OV2WnIvpEy586AG11_eXcu54whfhyuhTybgQlkPLNBfGvAAa9sGxZXqxKfZaVoPsN5WseNHd4xq0m6Sr2COByC1wq3UxcQaphkk3gIwZ0nVOacPFLitG2codPr3cgzz4qNBRYX_eb44gpyTJrY2e1Xj2OhYoV7ICdHobg2Tl47axdHlP8TR8EbF3Cl8WQ6T80mYS0_UYsCFct86lWnf0Mu7zIxFkxYMjqIFdl1B3bfYDOZ0_InffsapgetAm4ODXMtuFRnz61fj9fUpbdGIokYW7bK2U-qyaIa_eNFgsgP-hRBLIHs27mFH-5_0s42FKOYocoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دابسمش‌بسیارجذاب‌ازگفتگو اخیر جواد خیابانی و خداداد عزیزی در ویژه برنامه جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBs423njfOEhiTl5Kf6xHutbuYPGIFsibx38PASzvzfoHvW3-lBMigdKwv9KVP2tPmqo0b6ecEQYJn6_8kiNBWzpWhvr33Xx5d-IfxjvijYhgEdqyBBkZ3-cKWWA0p7Y_VLriOneYygs8DRHeshOO7fcuOUg-hOkSdAFHM9VRshkEFsGjfzLc6EvAWNxS7t0yTUvTOgRlFroZeYCiqQxE--l26essL_KJDJBHHnsvcza9x2wzvOYdGwDpJI2n2V3JCZpTQGbgOhrj1-_TvkPy_XnWpss6m9SM8xnTZLhsSmfTPKQkP3JN1MM0qQtWqKcJ353eDXvey-s0NUDmjfTfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/df7pnM1ESwEv9bMVxwtZ7ucbDI4oZJorN8MegVBIUgfTg9yaNegpTZtqr3ol_4MHVoqowCvxFdQZCsq94PpUwLsWrimdRGPve-P07hxXbAhcPEr08CVLnaDJMYUuXoJp2vKYYcHvMnFN_LOQXGPAB0-fZl42rB2wk-xRhcmZNjjqDrJ2OHoMbkLn9wLkTPBoOhI5zy6wn-LTNbtb5u9TbHNdxE_TS43cinsBGtwR8OezxjLnbJ-taau6YvtODWh7tJGR2Yd9cU02Xv22nagyqmhj2Kcb7_D_oSEnwEz3gf9Kgd9SMSDcoGryBxgrPIAf0Sr7dzps1lDrFqos8LgQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=rrm34Krk-L_1earLQUR7-MS5ExyyN5frMjzqNMQvl8pPbTf5uxlVR5M0rAkH31YAy6N9X_bjJt7cNKHLUoaw0ojt7UcaF1gUIjooMVIRZT6KqaPs3yciBO9YfW7BTsyWTXbqHHjywWAb8vWUKrUX7-NV70mhgvJhmBZWV2ZzVtBhgg17JeGIGmwFtmk6ZZIzIEGbLajjS-uC8U_Ebhe6Hnua2yjEf-CStLeuS4I2IwlbStqDkTOs-Ok9SWMmqjgNU5BU_WBKstbW92mNcomvXPX88aUsC4A16WZh5-i_wWZNqLQtgsL_SbCk4xrtJDZ8IZ2GIZ97zrCae5_TEzV7sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=rrm34Krk-L_1earLQUR7-MS5ExyyN5frMjzqNMQvl8pPbTf5uxlVR5M0rAkH31YAy6N9X_bjJt7cNKHLUoaw0ojt7UcaF1gUIjooMVIRZT6KqaPs3yciBO9YfW7BTsyWTXbqHHjywWAb8vWUKrUX7-NV70mhgvJhmBZWV2ZzVtBhgg17JeGIGmwFtmk6ZZIzIEGbLajjS-uC8U_Ebhe6Hnua2yjEf-CStLeuS4I2IwlbStqDkTOs-Ok9SWMmqjgNU5BU_WBKstbW92mNcomvXPX88aUsC4A16WZh5-i_wWZNqLQtgsL_SbCk4xrtJDZ8IZ2GIZ97zrCae5_TEzV7sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9mUHGsClvl_lvOYO8AWHYgV9PzDThP_z8G-zNQa_2h4SZj3Lpm_KuCHpcxdW6C0BpUZrGmaUcD4f5nUOPFsrKrAbgxj6NeHiFdALgTdPEtM2bN5ACyuAwxLxBV3IzbsCCLWObLyf8RGygRHh1vgcBCYFs6mMHtvFdNq04qYxRvRVswCxsZPPYshdVlR16-EUMSHJwvc4cqubq0BgLhA4ktOqwjAlZpv5I8Dw446JDHX8WHSlQxj6GxAttwW6iHgHk_tPSzlpm3S4xrZ51sv8yVuTF6aN2Fd7fuyps87bOarHZFhwV-9LQ_6e6jW23AgAEutHdfpc-uW1OUuCbNVAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUGOEDOr4TO3QrIiqOtMbu9dky47VzO8oOahXf50D_uH7t9xtp8MvNzP1G_nRMjRGpon4pjy8HlIhLRTOGl4kJ2KeOsj_hAPc7jVOdYNjNADgs3VDzb_0pBvOYQbK4HdBC4FpYq65UAWJ8SL2f4EUCqkIAZiYM6g7d9NTt-FE5urYd8j9hdzqMX9hz3SBzx8HEQ87gKoIsUn3sQZLe6_zX2-1nU3GFEI8wKH3ArqdtmI1CHMRtRyVIitfIxxfO3X89dokBpAoG3onTFf6uq_2MDjwDEBJdA2XtryzymeEac4HKz4vn5XZF5zN_tImEVvRyzHnaFEfUZ90Je6YKssKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM8YWZJ2GvngvlIcXbFvikz1wYhs62W64RhrKjNT8mzEw0zmy95rSna-726BJ8BUQwn4Q_ysKr9Vr3aqH7m6IIgqhTtMixU1WmDw_upXfNqHoPU0ddEqaQxpYD8iO8kNZvi2-di8LZpPSX413m6P3tqRxcQYF_Jm409Goc4h-LrTGO9Suh4KSPzNwvTsrbBO6T1VzHBIJJ0B1TvGyLJauAxkm8dSQZZuVXHP9YHQod_fVGOJhPqFq3Y4hPcM97ikfElKp8OaKS0ZLjBUnPVyFFSAnsXEgHIRjwVk58yySppKHs766QkKyeguPmvVjNnFzCy90w2QjANq7hhSsBs0fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛
از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRX-vU84tmU2jj7cLmEVgp8B6VjeOmqJ7E9miSHnqU7Qwt88ULrZHyhx8BR5A6pZSQjjAuoTuE1sd3V2NTtMFT6f_LYRpUBTE5oiL8UlFpqa3BsXixrsnAh0VvNPBL9tyy7v474p27W-Y-28-02nRc204ioR5NizV4hpXL8Zk90x1QymnshVHcWhSYaEzFx0IxT5UorI81GK0GT5n6G7WoDpGtT1eKu6TrXyNGgowy5DPFhkGzGeXIacQqOT4CGf2VSj_cDauQyym-CMMaNvMUDP_GT0ob0-CLgTh5NCwRrU6CHSEJq4A8zEmLe1gxAoMLz0_MkjrrPfppjokBdkhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lznUIsrssPNiGhPRNbIESl4ag6NJfP1TKi0odcKsD2qubJHgb3pkUSxWX7dpTT2o3LyoTEoLfUA-84fFyGxFvPXOCR17ANWGgPLJh8QIX0QLtw8tMUH8n7UC7FkV5Fhpk3hSXk3BnVVwdLmVf0OUE2YGpXwZC98mme_8Q8TOZXdDehx9ZeVjVeeV-3lpDRDD9grnPoDhNEaMsgL850k-6dwI0uySd7tZBgjh4udcGqWqOByNwcweTXz7CBFcilg91vfUYE7kfL5pA8lvRKxxoTVkrERBdUjL99hXzzUamJpn1YUXkLyumwOM1IWEPUsexnNPwP6aKHtxvsOp5E-L9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6re3asseiYgHQWaFxBr7Q5dkZxKie3_oNxkdjPBBuTEkRzFa99Nb5rjf-w9ZIO4JQrPAt5X1klPGyZzMxDFqgSga6gpzyBJSvbnWQFNdmp0ashZg0eLs1kAESrEAGGUldTJPaTo7I26KzfVbsw05kwcF2lTGSRHcuB5QE3N2z-N_Y2pz3dPCOZIYhXPN6VWGkmnSOHDVnr_x0DVHk26LHbBIImQuAD-MRxr9aJECn-HSI-8hi0UaoCgLJ7vP-Btd3RtH03NFOXqNcLvhTBs1UmHsEjeOohm3ByMexDfNdY1u1ONW7d_XsOPL7qpsnkpzykY-BsjkGe1-ZXOZIU43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGFvYJQbnkNG8L7GYikgpV6YMIRULDHoi62Jxu1zE7FSebOLsED7vMYT7fuUVUfPlSSPD3pEHPGjvQhTKt4ihn8v4hPh8gOwpeJYNHggkwDTXb0WXD6Mbjl8Vhviqq1VZjGVHmt0IqL_6_UD_Cg34HAowv8uVXbiHZnoxsq3UlA8obSVmhljtevIjmXQjc0UHO7Oor3nMtecgJ751sMu7ojnZ8QgxjaxNKe6FwIBF65ZrI2KUwdLiQslAo73DzctQBeNquVyOS-oCP-OijWbgRx9dj-WWSOitTdiiMNdRIqtIpQJwCKVzldVUKKsfHRziOa9D0bA2W6Ftn2hXktgMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI2VO9Bq8pcV-tMNDh1GPUlp_GjNIsRLZeXJW5ZqtwzGdzMjK1Q-Mh58-MdCIiQiXgHHji9X8GBexbqfo2M4_BJbVn4xWpLekg3kuPEfgPXFJx2rWVLhlcJ85nSD0VmcPGK0Y3tJWnPkLc8MWYSs3lwWiWWBgbMLoYnwYvOMDXr9y2TyZ33Oqr_cvGuHxkdz0MiLT2q4j9o74y-FfNpwx3GDRjxBKCoHX3M8Fisx4xhgDDIB1qJqY_-2zTISDgh8tkU6ICCwswGEs75eG2Hq0gqX0-yK0o-z9hzceUd_3Qm-mAWMz6YVjmWFqG1SYkwRQWyeDyB7iXFwKgXPTj7PkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛
صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
