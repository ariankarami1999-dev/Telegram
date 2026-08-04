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
<img src="https://cdn4.telesco.pe/file/PSwJLHpxesUkD5ih6mphrrBGB6aQkIzBiSYi8-xxfG0aSiwRDubvV7WnnLyzM6HpOudFGNYwIvNgsCTQ1vU4qBYBqz4DU6picqbjMRVFy15dYXR0hI1sfMCagDmQj1LiTlgVBvpfLbaJtc4TnR6JoyDoAmhtpI2FsmRBQhQ3yi-RjQzb4bH3JgUrUKvLQRV2Bky9E_0ZfrL2V259TukEu6wvRTBiqEYtTWLHD-M5-dc0Z9Hvjr5X4LGKT0pStvxPJ1OIMV_skH56flQiFJi5YSLg3giMgGCzyRVNCFWkG6io7U07YvV1USGb8GF3wao3X6kpg63b-oAb163aqCUoog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 15:06:30</div>
<hr>

<div class="tg-post" id="msg-678389">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LojrIjkyW9UlUKsftb_YeYHQ46GE-RHFRf6GOH5O5PxZWjnDI3ueWSM8Pv8ubpEcaGGKC5bXCg-IoTQ50YPhohY9R2ujFlbFNS7rdHVZMAHMIYtDpt_o5BYEJlKxK-1ncjP6Dj8MPvjqZKbNbfE1H65R0ecrJAXloZbfc7lnbzV5sl5H-QuwwUlQKrqD4EAHUDZl_NQkOu4yY-SdpF6IlMVAC1q3dwfczzahW-qK8zxFF4gfz2SA1whxERKD_c7vJ6dULqQv1_9gmLvBh0gCJPtarrLExf5Z0A-Op__PNZjvyXWX0jwcOIKy24dMgsaaVcRNGPygLk-Ot0qNI0GbjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش فیفا به ادعای تماس اینفانتینو با ترامپ
🔹
فیفا اعلام کرد اینفانتینو در روزهای اخیر هیچ تماسی با ترامپ یا اعضای دولت آمریکا نداشته و ادعای مطرح‌شده در این‌باره «کاملاً بی‌اساس» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/akhbarefori/678389" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678388">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjKszLTFVypRxAwM-mdaXAY6LFf7YkoDILCvAeIcf5Q4Bt_y3DsojUxscKRDxDbvIhwdRWX612UM8LZi5Jmt-TRdaXwWHDQAOj88srZMkGhoBTMDbikxQBLlMTNC9wUSK4gq4Kjm48rqsPaUWjnMddraxvM_MmUR-Cn7aVqH-1MFogQeS0SoGbyF4DdK5L5Lg-oOBY-DH2pDjSL-eE4gFKrBL9q3u1H5OwMYDNmnw8QEGBxuSOlGyryMDboxt74DMG9RaHQaLU0_t2VUl3jYgwv9dZz6hG-kLdDWjsqcTBDm8bSqx7auCokmu1w3Bq2w-R30xctxkudYHsEGrs9CHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ژلی نوآورانه برای بازسازی مینای دندان ساخته شد
🔹
پژوهشگران دانشگاه ناتینگهام ژلی بدون فلوراید ساخته‌اند که با تقلید از پروتئین‌های طبیعی، روی دندان آسیب‌دیده داربست ایجاد کرده و با جذب کلسیم و فسفات بزاق، به بازسازی مینای دندان کمک می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/akhbarefori/678388" target="_blank">📅 15:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678380">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ یه حرم فقط</div>
  <div class="tg-doc-extra">روح الله رحیمیان</div>
</div>
<a href="https://t.me/akhbarefori/678380" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
این چه سری ست که هر گاه مسافر داری
باز هم اسم من گمشده جا می افتد؟
▪️
پک مداحی ویژه جاماندگان اربعین
🏴
برای دل‌هایی که از کاروان اربعین جا ماندند، اما عشق حسین(ع) در جانشان جاری است…
#اربعین
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/678380" target="_blank">📅 14:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678379">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2ff459e7.mp4?token=gXEqgHAfudP7tts3LlMjOayE5X-LnvbL_ZRIiGmydiqEMYEKVRwmjawOArLHd5LgqSXk33oNhC7UjDtmKWvzmNPz-fg41GlwvFt6I57Y7JsSeIMs6Q4U9x5naK2UxdqFD4_SR_CsnyI_pnGLDBiJpxpk8DQC1zruV3MruQYheTB53njOYvX44kHzOJPuiyVMH7vnc105YDVuNn5_Af0xtQdhpDjEDRD3_CNAeliwxybCINPyyeZmTZSTywnTa7gEFPs0ysaEDVGxISQgVK1jP_cPl2PcblAqWLQUiHEdSJkoCu92kaAXjF4umUHsjkrX-1bMC_gu03nR424j5QGUPg1oVswvnkGkXQIIITkKsobLW_9HQvq1odat6g9ZuWIQY2k-AnV-dukg9cYBi_4QOhALNSIFQ5ZxC1I5Q7eRajdBiKmgJJWUGbi-jn7EsSpnuciIROrjUMv9aqzVzBXs1KhQU-oiziYE_JGaxH-MmjvCEzkRCBYABybEX2VJ8xXsVooplq9yl1I1xqwdNUYPpyI_xoOolnleofZsCghz3fzo7sjpvE9VvbFx2Zjhvw-VCTkesiHxFsu0jwY7aOxig5NmsyIacF-lSs3SGp5jnDCPFbqXz9S8yiw1vUcBGdO28JNbeHDwX4eYqbiEkmp7OF_eKv9_22XYA9r4yXyBrBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2ff459e7.mp4?token=gXEqgHAfudP7tts3LlMjOayE5X-LnvbL_ZRIiGmydiqEMYEKVRwmjawOArLHd5LgqSXk33oNhC7UjDtmKWvzmNPz-fg41GlwvFt6I57Y7JsSeIMs6Q4U9x5naK2UxdqFD4_SR_CsnyI_pnGLDBiJpxpk8DQC1zruV3MruQYheTB53njOYvX44kHzOJPuiyVMH7vnc105YDVuNn5_Af0xtQdhpDjEDRD3_CNAeliwxybCINPyyeZmTZSTywnTa7gEFPs0ysaEDVGxISQgVK1jP_cPl2PcblAqWLQUiHEdSJkoCu92kaAXjF4umUHsjkrX-1bMC_gu03nR424j5QGUPg1oVswvnkGkXQIIITkKsobLW_9HQvq1odat6g9ZuWIQY2k-AnV-dukg9cYBi_4QOhALNSIFQ5ZxC1I5Q7eRajdBiKmgJJWUGbi-jn7EsSpnuciIROrjUMv9aqzVzBXs1KhQU-oiziYE_JGaxH-MmjvCEzkRCBYABybEX2VJ8xXsVooplq9yl1I1xqwdNUYPpyI_xoOolnleofZsCghz3fzo7sjpvE9VvbFx2Zjhvw-VCTkesiHxFsu0jwY7aOxig5NmsyIacF-lSs3SGp5jnDCPFbqXz9S8yiw1vUcBGdO28JNbeHDwX4eYqbiEkmp7OF_eKv9_22XYA9r4yXyBrBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخلیه ساکنان در پی فوران آتشفشان گواتمالا
🔹
فوران آتشفشان فوئگو باعث تخلیه فوری مناطق اطراف شد و ابر خاکستر آن تا شعاع ۴۰ کیلومتری گسترش یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/678379" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678378">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b3b9e300f.mp4?token=G1Tb8ohfLvSXx9recP_nG-PRfUIUg3DwTR14Tuxtp6USjRSSU3VqMQPgXAaTWgPJxlFZs0p_yooSfh-dDKBg2neJ-rLalJTUQw5tgsgrlkhYs8rS-BzYb26YrwH5SDWLmSTNc1_CsuCl-kQYs4lML2TwzA_eRhiJEFF76Y5FwAmECChSFDvx0uC3165QEZKDAGCkrCo0-Gu1paQxsfeRBWuxxj_U6Q7f2Rp5dXp7-3qOPK79tAx4EjExHQpydwZPGjBOPvFPgTUAX383TMziWWTmzmR9xm9X3-YzxuVIuiOQsCL9_YcEqTa8dUOk-CegFmkqRFbino6G0BcfvcZjPoteASszNZWkGrqTvQyMb_L0_hTZU-Ja-sv_juhxqpVXrrWvSOCJCCelyiUdpFTew0J15qsTUpxaM_ZKLQj23ADeOIvOmK_tumD_cQDxXhSJP5tt3EOb44l8sBTdKG_N52IFYGSuonCJlt7i7uGtH3dtN5hszOEgFByvpOvTI40bxU91TkzBS1-DwhRU3w_XsYMDf54HJL6CDcrmImb1o50Yt3pZqFvX1Yn45hQwznYDgGGPEikzf3EaBkw8Uba5nwFLb1N_qGZ2cffVRYvCGc_bOzz1cUARdb4sWq3P2TKfjWw3j8DtWnYQut8o_oc4LDbIPToEr4sIc8Ib5LxdNHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b3b9e300f.mp4?token=G1Tb8ohfLvSXx9recP_nG-PRfUIUg3DwTR14Tuxtp6USjRSSU3VqMQPgXAaTWgPJxlFZs0p_yooSfh-dDKBg2neJ-rLalJTUQw5tgsgrlkhYs8rS-BzYb26YrwH5SDWLmSTNc1_CsuCl-kQYs4lML2TwzA_eRhiJEFF76Y5FwAmECChSFDvx0uC3165QEZKDAGCkrCo0-Gu1paQxsfeRBWuxxj_U6Q7f2Rp5dXp7-3qOPK79tAx4EjExHQpydwZPGjBOPvFPgTUAX383TMziWWTmzmR9xm9X3-YzxuVIuiOQsCL9_YcEqTa8dUOk-CegFmkqRFbino6G0BcfvcZjPoteASszNZWkGrqTvQyMb_L0_hTZU-Ja-sv_juhxqpVXrrWvSOCJCCelyiUdpFTew0J15qsTUpxaM_ZKLQj23ADeOIvOmK_tumD_cQDxXhSJP5tt3EOb44l8sBTdKG_N52IFYGSuonCJlt7i7uGtH3dtN5hszOEgFByvpOvTI40bxU91TkzBS1-DwhRU3w_XsYMDf54HJL6CDcrmImb1o50Yt3pZqFvX1Yn45hQwznYDgGGPEikzf3EaBkw8Uba5nwFLb1N_qGZ2cffVRYvCGc_bOzz1cUARdb4sWq3P2TKfjWw3j8DtWnYQut8o_oc4LDbIPToEr4sIc8Ib5LxdNHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
جابه‌جایی زائران اربعین با بیش از ۱۶۰۰ دستگاه اتوبوس در ۲۴ ساعت گذشته در پایانه برکت مهران
🔹
توضیحات علی‌اکبر پورجمشیدیان، رییس ستاد مرکزی اربعین پس از بازدید از پایانه برکت
✅
تازه‌ترین اخبار و ویدئوهای اربعین را
اینجا
دنبال کنید
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/678378" target="_blank">📅 14:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678377">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBfDxK7F0m1E8UP6wEUohRi-f1_RJxSYpwojZvI7xK88kKxWEM3oW1h1SftSijsQLg0ZVWn-90X9gJf3jfWAezw21DTIL4pyMsynR-0wA52BMu0B_E21CCfJDMQ1qcorigIy7r1crJrhUr-87L_oHQfJI2WmlLkcPsrhyDNosLkWNdzKLTzfYLdDIGFSdv0CSVTKTVVvOPoIYIzpvsk1YQ47JI9sOMdq2MuHXktcrJbXw1chow1kkUNnhO7uZdj-nOaDsWY9hzxpdpnPZpeOZoTmjoSBARec-QYz2pvc3oo8jQ_25HCE4VheNpHHf-zVSe_pCjXbIGgSwZE9Uy77dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ربات‌ها از انسان‌ها در اینترنت پیشی گرفتند
🔹
ترافیک ربات‌های خودکار و ابزارهای هوش مصنوعی برای نخستین‌بار از فعالیت انسانی در اینترنت بیشتر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/678377" target="_blank">📅 14:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678376">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/925fb43a08.mp4?token=ruLYndeOlwp90buSaq6aicBSsmr2AfKfVbw8Y5GSwSyQL20Jky1HU-kvnCbuvV_gpSShu1b6kyaE4ebu64ohKvhhU0xVqPOax3M-fqUipBeljN1BNQCTwsk6omteN-sgDgq_P4ad273dlOTYAu47K0bo_JDIUZWz16KbtJqGYRZR5HsjWEiA74HcHosLnMYLnqq-qeiJU22xM5SlpUyjJnVNzFi52UmgYSYGzn22mmPuis_UF1e7b-OHXh3je5sPCP9x5v1I14GmismXU6XyV6wusKDOlSbLttAg0wWXA0SdkRRMiNmMSWlyMUcsjbF7bSIjaIEgNZfb-Kk_7rCVuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/925fb43a08.mp4?token=ruLYndeOlwp90buSaq6aicBSsmr2AfKfVbw8Y5GSwSyQL20Jky1HU-kvnCbuvV_gpSShu1b6kyaE4ebu64ohKvhhU0xVqPOax3M-fqUipBeljN1BNQCTwsk6omteN-sgDgq_P4ad273dlOTYAu47K0bo_JDIUZWz16KbtJqGYRZR5HsjWEiA74HcHosLnMYLnqq-qeiJU22xM5SlpUyjJnVNzFi52UmgYSYGzn22mmPuis_UF1e7b-OHXh3je5sPCP9x5v1I14GmismXU6XyV6wusKDOlSbLttAg0wWXA0SdkRRMiNmMSWlyMUcsjbF7bSIjaIEgNZfb-Kk_7rCVuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
توصیه آیت‌الله فاطمی‌نیا برای جاماندگان اربعین: اگر کسی در این روز‌ زیارت جامعه‌ کبیره بخواند او حتما آن روز از زائرین اباعبدالله محسوب می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/678376" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678375">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای فارس: آتش‌سوزی مخزن گاز در شهرک صنعتی شمس‌آباد
🔹
یک مخزن گاز مایع در یکی از کارخانه‌های شهرک صنعتی شمس‌آباد دچار آتش‌سوزی شد و نیروهای امدادی در حال اطفای حریق هستند.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/678375" target="_blank">📅 14:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678374">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63521f75be.mp4?token=epNd6xteIZAr1CWDHTfv2TSObroUSjvf6QUvdjPUi0nXUjyjhsMkQA-eR7ALCsfaQ53smhFSg8SigGEF1c9TVXXrHP4Oy57W06UM-nTnowNF1tRUmgRKeFYnaKuoy_MBqBNKvui282E6VqKcHifuwVBWTC0oMJHulPJZWkvQQ4jjvWIACNAhOYWN08DkjjTJLlMOdysYPvyE1o2u-5X-bXLWPPOk3ObUTgqq0XsIvuNCDlaC30THv0nwNcZrEwSdPbrO4aEaq2a50gaOVqZnL1DokgvoigSoGUMXubDNZX-0728-X0NYEcz_spkMMW5BxTxHukp8rsXhUOAvKu4SyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63521f75be.mp4?token=epNd6xteIZAr1CWDHTfv2TSObroUSjvf6QUvdjPUi0nXUjyjhsMkQA-eR7ALCsfaQ53smhFSg8SigGEF1c9TVXXrHP4Oy57W06UM-nTnowNF1tRUmgRKeFYnaKuoy_MBqBNKvui282E6VqKcHifuwVBWTC0oMJHulPJZWkvQQ4jjvWIACNAhOYWN08DkjjTJLlMOdysYPvyE1o2u-5X-bXLWPPOk3ObUTgqq0XsIvuNCDlaC30THv0nwNcZrEwSdPbrO4aEaq2a50gaOVqZnL1DokgvoigSoGUMXubDNZX-0728-X0NYEcz_spkMMW5BxTxHukp8rsXhUOAvKu4SyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر جامانده اربعین: آمده‌ایم نشان دهیم مردم ایران تحت هیچ شرایطی کم نمی‌آورند/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/678374" target="_blank">📅 14:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678373">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3ROiWjO8lP5ERHmS9VQ7fHKl6kP2eHIK7Syqi50dnPH48Kczmswto2FyOv15HyY-OvYh-j4YYBMK8XLQXIAvF4zEDzLYUTI9d2WtjxAqB45PIL25RXdi123BQz67gmb5esB03JgvHk9BLs1rVLDbX4gZpu7QhN4zrh6EXdL4GSsltkkKfP0AmB_wAiH4mX9QpoBM9MSgnVS5kXDK5UOZmst2JV9xryGJrf4TcHkH77W3bXfJsMA95y2YmSdx7l3GUImHP3-BYb45Esm9NEO3VN4WDQlkhJN-vkHfaBQ7Ls0uf50xVwO4kFAh6NY5B18JXZJBMnnrxsoy9TrRg5eNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از حضور سردار شهید علیرضا تنگسیری در پیاده‌روی اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/678373" target="_blank">📅 14:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678367">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdf615adb0.mp4?token=dqo-nOqobOFu4itemK9Q5AkTvjeLlsrawtEyQgRKCZFl4HFBwTIO-p7KI6l4zEPqTI853hHE5UV4ZLQMDBd4KBFH1CF_ZgcXGkhLkZDK_O-tDtY80wZvPTX4AblGFZw67AOKNbR30DyygS35VA0biyPnIBThQ8bufLrpagZgI2WcCU_MAeQcEA_6UzKzVc9MAenAdKEU7uGzUIrsP1aeDPmmJYS_dAPJ6UtfHUZBizKXSbSDUspHJzvShhdnSFEqlCX6ON3hWJ6ai-_qRYSZ5r1jD5hXRu72_agEp1OXUVKqDAtoYj3LY9K2jDmRt9Uh37oRqyotdewAowIbyvF7c4Q8iIJQK_EWSPSSfyr9SBA_DtnAMePZW_RBkEN0nUrt4U1PcJbNy3vh-x8O91o0MTs_O-Y-lUdNTblJBBfrDhUxZtcdYEX8BhQ8I2fzmo3FolYoVZunR7vC-LJNRpkhGhz7f-X0XsCtF-2jx9ci-1Uz2aOTQBMh9KQnXpUNX3BvgZvXKIiH-7GJMGbqqbtSa1E_B-xVHeHhLEYeihTvHUXDtqsUUV78Ezw15te9xMq4c5Kpuy2w8tMBH5cCX3y0McsvxsfS4mA7DUYmhUKkZiITjm_TK9b30Z_uSLLbsXA37l-WUg50eig_e8GppcIzAD8iF2yPeuko1vhsRbAAOfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdf615adb0.mp4?token=dqo-nOqobOFu4itemK9Q5AkTvjeLlsrawtEyQgRKCZFl4HFBwTIO-p7KI6l4zEPqTI853hHE5UV4ZLQMDBd4KBFH1CF_ZgcXGkhLkZDK_O-tDtY80wZvPTX4AblGFZw67AOKNbR30DyygS35VA0biyPnIBThQ8bufLrpagZgI2WcCU_MAeQcEA_6UzKzVc9MAenAdKEU7uGzUIrsP1aeDPmmJYS_dAPJ6UtfHUZBizKXSbSDUspHJzvShhdnSFEqlCX6ON3hWJ6ai-_qRYSZ5r1jD5hXRu72_agEp1OXUVKqDAtoYj3LY9K2jDmRt9Uh37oRqyotdewAowIbyvF7c4Q8iIJQK_EWSPSSfyr9SBA_DtnAMePZW_RBkEN0nUrt4U1PcJbNy3vh-x8O91o0MTs_O-Y-lUdNTblJBBfrDhUxZtcdYEX8BhQ8I2fzmo3FolYoVZunR7vC-LJNRpkhGhz7f-X0XsCtF-2jx9ci-1Uz2aOTQBMh9KQnXpUNX3BvgZvXKIiH-7GJMGbqqbtSa1E_B-xVHeHhLEYeihTvHUXDtqsUUV78Ezw15te9xMq4c5Kpuy2w8tMBH5cCX3y0McsvxsfS4mA7DUYmhUKkZiITjm_TK9b30Z_uSLLbsXA37l-WUg50eig_e8GppcIzAD8iF2yPeuko1vhsRbAAOfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨️
‌دیدم شکوه گنبد و گفتم خدا کند؛
چشمش مرا بگیرد و قربانی‌‌ام کند
پک
#استوری
ویژه
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/678367" target="_blank">📅 14:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678366">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52aedd4564.mp4?token=Npd_Z-GN4jjMLg38YiT6ZDw4gh-u_FLo2wLkLwQLayOsp5tpIVlKTd0WxI6_mgVX5eAEvFfgdn_6UvGw6SrNH3fKiEI1LvYldsX34f5eyVa9CTMdgCoQS1QtFEa4m03JIIFH-qDCzjceP6GIhymzyUiqgBuRuyxS4d7aDAnvMIlqgRZNN-oPcjaSd7bRF8_Nco-wKwHMJlW-ecWZFNLMjc2Z87qc6tx4BwwQ-DnyYJ4ZuoPhIcSNj6yzX7By4HkkaTxnkuAMCLM6wauH3sfk0NwMSof6hbkEI2b2GEAaMD6Gd6-qsziATt0FyDOLGSfo_T3PZTTZZU550KVylyS5Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52aedd4564.mp4?token=Npd_Z-GN4jjMLg38YiT6ZDw4gh-u_FLo2wLkLwQLayOsp5tpIVlKTd0WxI6_mgVX5eAEvFfgdn_6UvGw6SrNH3fKiEI1LvYldsX34f5eyVa9CTMdgCoQS1QtFEa4m03JIIFH-qDCzjceP6GIhymzyUiqgBuRuyxS4d7aDAnvMIlqgRZNN-oPcjaSd7bRF8_Nco-wKwHMJlW-ecWZFNLMjc2Z87qc6tx4BwwQ-DnyYJ4ZuoPhIcSNj6yzX7By4HkkaTxnkuAMCLM6wauH3sfk0NwMSof6hbkEI2b2GEAaMD6Gd6-qsziATt0FyDOLGSfo_T3PZTTZZU550KVylyS5Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصادف عجیب در مسابقه موتورسواری آمریکا
🔹
در جریان یک مسابقه موتورسواری در آمریکا، راننده در پیچ زمین خورد، اما موتور بدون سرنشین به حرکت خود ادامه داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/678366" target="_blank">📅 14:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678365">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
صدا و سیما: شنیدن شدن صدای انفجار در شهرک صنعتی شمس آباد شهرستان ری
🔹
به گفته مقامات محلی شایعه پرتابه صحت ندارد و علت این حادثه در دست بررسی است.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/678365" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678364">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
رویترز: ایران خواستار امکان مداخله در تردد کشتی‌ها است
رویترز به نقل از یک منبع ارشد ایرانی:
🔹
تهران در مذاکرات با عمان برای بازگشایی تنگه هرمز، خواستار کنترل تردد کشتی‌های ورودی و نظارت بر کشتی‌های خروجی و امکان مداخله در عبورومرور در صورت لزوم شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/678364" target="_blank">📅 14:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678363">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشستا رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab631c7c2.mp4?token=Xxw7YyISnV1VLiC1oePg4WSH12PmtDrz9O9FaLra1-D1fhjzV6m74OKFBh3nhzfRwdlpg21FnB1hs0gvFG-zI825pnz03CWVJmT3K-7wS1FhYJ2tCYIjw9Lx4VM8yj-5J8Mxz3BcQXcoGlAznFp_Vh7st_hc-4b2pdRfWpkw9y_uXeFLwL7Yc1M8hX2c2vCKYoiPj-mKvqYEqkJrhMnnDpUH5HZ9AFkMdlMAz0-ENQcJEu-EBdmyjZHMG1nqLBkMTvySHZ0XseREAoONLee_81fUwq6gCu_xqpn0eZlDdyAbkkXqBmvWKzUZRjuPat3pWDY9uFW-iSrbpmDKYs6GnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab631c7c2.mp4?token=Xxw7YyISnV1VLiC1oePg4WSH12PmtDrz9O9FaLra1-D1fhjzV6m74OKFBh3nhzfRwdlpg21FnB1hs0gvFG-zI825pnz03CWVJmT3K-7wS1FhYJ2tCYIjw9Lx4VM8yj-5J8Mxz3BcQXcoGlAznFp_Vh7st_hc-4b2pdRfWpkw9y_uXeFLwL7Yc1M8hX2c2vCKYoiPj-mKvqYEqkJrhMnnDpUH5HZ9AFkMdlMAz0-ENQcJEu-EBdmyjZHMG1nqLBkMTvySHZ0XseREAoONLee_81fUwq6gCu_xqpn0eZlDdyAbkkXqBmvWKzUZRjuPat3pWDY9uFW-iSrbpmDKYs6GnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدمات‌رسانی به زائران در شلمچه
اربعین حسینی(ع)
#شستا_کنار_مردم</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/678363" target="_blank">📅 14:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678362">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/242129ae3c.mp4?token=VaX0N6X2q8Cor1p8eM_FwBcms-GrFkfAkTzgFLAUaXdGl0TNOdBUezn84rxSm0y4V__2dIYcg0yeerpC8l01WLnraqGZpbHHb98oa0htrYe5cXA9VcawFF2rzBx1zgh3ca0dB284gNzy09zKGyElGrt-K96pgNBRs22KMQomeub2BocJxOXi9gsbxSg6y0uFbZA48accyVIzutTLub-_tCXhlHiknOdRtgazTPAriVL0zxVGKDIubAz5_a1E-k1msNYQGxXrEPGBZng5Z0PLAptKsZadNWRsK7BZ3ku1h_Zi6DE_PJqsJdBe4vSM_ZTnooxFoZQeV3mm3g6Oxq4DeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/242129ae3c.mp4?token=VaX0N6X2q8Cor1p8eM_FwBcms-GrFkfAkTzgFLAUaXdGl0TNOdBUezn84rxSm0y4V__2dIYcg0yeerpC8l01WLnraqGZpbHHb98oa0htrYe5cXA9VcawFF2rzBx1zgh3ca0dB284gNzy09zKGyElGrt-K96pgNBRs22KMQomeub2BocJxOXi9gsbxSg6y0uFbZA48accyVIzutTLub-_tCXhlHiknOdRtgazTPAriVL0zxVGKDIubAz5_a1E-k1msNYQGxXrEPGBZng5Z0PLAptKsZadNWRsK7BZ3ku1h_Zi6DE_PJqsJdBe4vSM_ZTnooxFoZQeV3mm3g6Oxq4DeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مخزن یک کارخانه در جنوب تهران  عضو هیات‌مدیره شهرک صنعتی شمس‌آباد:
🔹
صدای انفجار در فشافویه مربوط به مخزن داخلی یک کارخانه در شهرک آلومینیوم‌کاران بوده است./ ایرنا  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/678362" target="_blank">📅 13:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678361">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
قطر: رایزنی‌های فشرده برای کاهش تنش در منطقه ادامه دارد
سخنگوی وزارت خارجه قطر:
🔹
رایزنی‌ها برای کاهش تنش ادامه دارد و هنوز توافق نهایی حاصل نشده است؛ تمرکز اصلی دوحه بر بازگشایی تنگه هرمز و بازگرداندن طرفین به مسیر گفت‌وگو و تنش‌زدایی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/678361" target="_blank">📅 13:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678358">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df08a618f.mp4?token=QMmqiLIkfjgcEHPoy3riaDT9UeXGbJzZCYsCmI6fO-GpwQA12AFSxi1CJe45xyvxOJ-tRfPjKwdQoMy7YtGsTPPQv2zHXXP6bCcXnUshnF3uqc4HRDogKRwnj1AbUZgt3STmkqXybSTB_IYeqkcQeINnW5dKZbL58DekBsPfENtaSbDXoUJwdVZFqUuiX7FcoeYIVtw-ft1eIyHivenxnn1syro0X1SBZ2tuTGTuIlBlfXIUu33QQdD0zM1nwJbDQyDedzLCDHVHSgWIucvyJiMN0D7_xnTNQHjjbda_espCRryMkNfJDBMdp0fZVPRm09GfbbZN5eQC1jGcO_LKDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df08a618f.mp4?token=QMmqiLIkfjgcEHPoy3riaDT9UeXGbJzZCYsCmI6fO-GpwQA12AFSxi1CJe45xyvxOJ-tRfPjKwdQoMy7YtGsTPPQv2zHXXP6bCcXnUshnF3uqc4HRDogKRwnj1AbUZgt3STmkqXybSTB_IYeqkcQeINnW5dKZbL58DekBsPfENtaSbDXoUJwdVZFqUuiX7FcoeYIVtw-ft1eIyHivenxnn1syro0X1SBZ2tuTGTuIlBlfXIUu33QQdD0zM1nwJbDQyDedzLCDHVHSgWIucvyJiMN0D7_xnTNQHjjbda_espCRryMkNfJDBMdp0fZVPRm09GfbbZN5eQC1jGcO_LKDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصاحبه خبرنگار خبرفوری با زائران جامانده از پیاده‌روی اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/678358" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678357">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ3jHkeRq4CE8vQhyStR6HtiZFHd1RWew_M7OHKhgPqVmEiPNWczoq_LVeHARkLtH5Ha9leTDz7jZ3_xFH2ujhCHqpbFCNMGou7yoJ9S28KmGA5PooojFEH8jNr4G-eI8GPRyGkYLIqZr_sdOQc_aOzBC7x-JmJPiz9JFC5KGS3g0ZvgInhMC0OlJvLW-PH-vxXgVckDP9vzbo7qutxbQypfe2QkSb6Xphvfg4gpZCM5N9PyWMVr_IpCFIz5yunABQ5sKBgSPD4MXPm9-6UvApwTJeIpr6AHvD2BMcAQD5QuOh5mLFCurgvlnCf24DHhQDyKbY5TaQnRVnB3TUbPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
فضیلت زیارت اربعین
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/678357" target="_blank">📅 13:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678355">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
انفجار مخزن یک کارخانه در جنوب تهران
عضو هیات‌مدیره شهرک صنعتی شمس‌آباد:
🔹
صدای انفجار در فشافویه مربوط به مخزن داخلی یک کارخانه در شهرک آلومینیوم‌کاران بوده است./ ایرنا
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/678355" target="_blank">📅 13:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678354">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2QmYnlyZqivTvYqCmMDjFupJDp2Ro9_mtQcDBld-d-LdLRn2BPsvvB5oHfKtJquJe-Bf7qphy2pQwc6tyQwRN3aGelgkwTD5KCb1TU_tk4AxsxC9JXeQK8E_N7j6ENspLHOzLYW3Me5h1lvs6mKbbCHmlxp-rhFby-EnZAI1RMXlyLAMGr5jSYlRbRHpNp-2s7oiR_-ngXzhBWOhJf7u0EdXi9KEcd4CkxPMxzduQZdlqZHdZ_yAzZuMzkF7HYfHiQ5IulJT-PM637VBkwEatzPINGtGsB5Uqefj0Ro6TndsfniMg77QmY_Vv-gnMP754u-D6OJxJZJtrZhclPIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده تهران در مجلس: کارنامه شهرداری تهران در حمایت از شعائر حسینی درخشان است
کامران غضنفری، نماینده مردم تهران در مجلس:
🔹
در مجموع، شهرداری تهران در ماه‌های گذشته و به‌ویژه در ایام اربعین، در حمایت از شعائر حسینی و تسهیل حضور مردم عملکرد بسیار خوبی داشته و اقدامات این مجموعه شایسته تقدیر است
🔹
یکی از نقاط قوت این مجموعه، تلفیق موفق خدمات عمرانی با فعالیت‌های فرهنگی است. شهرداری تنها به مدیریت امور شهری اکتفا نکرده، بلکه با ایجاد زیرساخت‌های مناسب برای برگزاری مراسم و اجرای برنامه‌های فرهنگی گسترده، نقش مؤثری در تقویت فضای معنوی و تسهیل حضور مردم ایفا کرده است.
🔹
کمپین‌هایی مانند «یالثارات الحسین» و اقدامات مرتبط با نصب پرچم‌های سرخ، از جمله برنامه‌های ارزشمندی است که در ترویج و بازتاب هرچه بیشتر شعائر حسینی نقش مؤثری داشته‌اند. در مجموع، اقدامات شهرداری تهران در این مسیر، مفید، مؤثر و نشان‌دهنده تعهد این نهاد به حمایت از اجتماعات مذهبی و خدمت‌رسانی به زائران و مردم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/678354" target="_blank">📅 13:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678353">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
حمله پهپادی یمن به فرودگاه نجران عربستان
نیروهای مسلح یمن:
🔹
در واکنش به نقض حریم هوایی صعده و حجه، هدفی حساس در فرودگاه نجران را با پهپاد هدف قرار داده‌ایم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/678353" target="_blank">📅 13:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678352">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekunauCYr7HieU75OTqVU7_Pw2swBCfPQM5sbKVOpUuneP0X9fOkOay552BZ8hz45hmP_YE_yF3pGuyK0G8QmGKnP9M5fgs1_-Ipxdb2tR_gJbrK_04__NMvJmusIlf7pfMAGJfUxEKgXfqj3bg0zvQXJuZgnN7XRNfnM0FqF_YhQu__mk3o2GGb6BRSK1-Vzc-4lTY9LW2Gpuy5ozzBQTZ0hNslRsSx2y-l8EmRU6yOYbp43K_OVxxMECzqFb9BWyKQHxU3lpX6fdE9EPfNQdoMeMu39g2bLG7m-Z9_F_gie5UsJOf_v_W7ytJH3BpsXGG7pfJfqF10aEeNYwX0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر کمتردیده‌شده‌ای از لحظات قرائت زیارت اربعین توسط رهبر شهید انقلاب اسلامی در حسینیه امام خمینی(ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/678352" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678351">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3040b11d1f.mp4?token=noxvv7di8Mt1_LbRCDP8TMkyjZ1OYma5jLsO7cTfsPpGQ_zInXezqXkyqe_Rc5e0a_iDE6K2yW4NRwD-OIdmLebZUzAqMPesyfPJl_o92IeC7GpYmiHdgpbmCT6fN7hk3mcdkod1teL_CYeDMLPEqRvRqjJyihZwtpojT7IXc-KYJvFYYZLnHU7Q6k_LMoNZ7IIMQQ2wR1O2CqxmT9Y-BVpQyymHGZD7LIVhxlGN__5tTIBUnYysWCBQbQ2USjc-eQX6m-EQhfIUPvoApMf6HOUaHRvGJ_FgwKyKJp9JKLwhSZUhRRmXVNip-tLKbjNXLMLxaxHrjxg9XY5Nbps2TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3040b11d1f.mp4?token=noxvv7di8Mt1_LbRCDP8TMkyjZ1OYma5jLsO7cTfsPpGQ_zInXezqXkyqe_Rc5e0a_iDE6K2yW4NRwD-OIdmLebZUzAqMPesyfPJl_o92IeC7GpYmiHdgpbmCT6fN7hk3mcdkod1teL_CYeDMLPEqRvRqjJyihZwtpojT7IXc-KYJvFYYZLnHU7Q6k_LMoNZ7IIMQQ2wR1O2CqxmT9Y-BVpQyymHGZD7LIVhxlGN__5tTIBUnYysWCBQbQ2USjc-eQX6m-EQhfIUPvoApMf6HOUaHRvGJ_FgwKyKJp9JKLwhSZUhRRmXVNip-tLKbjNXLMLxaxHrjxg9XY5Nbps2TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تبلیغ قدیمی خودروی برقی؛ اگر همه چی با موتور درونسوز کار می‌کرد دنیا چه شکلی می‌شد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/678351" target="_blank">📅 13:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678350">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/457e9bdb4f.mp4?token=S6h2zVXLtEgH-nFvtrygj2ebhmzUdEYFow4dcpN1uHshHbMclCV9tHx29vYPhMPMTBStq1ZjT_I7e7mOdcHfwUjkhrYiVIWd8Y1I2gBg77yb5uGgxmpVkWcmIIsW65qxqQ3nCCVW7rGHBPWA0mFYnTICccPs3rbasKwkIamUTy19mbqblMmHSLky5paVvUyqOXKoRmGWAaUDi3JEY32zxLHcukVoB0No5ICHBXmC5MiRgYQW9T5NFYOLEVtTZpx8XJdg2vG076viF62ZRu_XB9KDBsup3W8rKn82DTGGDAMnyJcN34PMekHL0HK-OssYHnMmY5PA-qo3Drz3KSwo0b_7S_eIV6yGXMYPmkeIqzoaY6FkHWjyyJzdoTsyWYHnPCImXnIzWmuYsKpLTo0rhdfGfgbmi0Bg0xVQ8krmwmphxLzr-rUhHck52GPgNIPlG0IB8Mgr7mivHFdLrwyH4rrqCmihrutVniwPxZq5yObrhkZ85fV_hv9rpHaPsOkNQIZCoM-yxB6opyHkmUZvyGTphlKBx_slfLng-2Nbta5k6NtJTBtEotwn_mtS9iwnfaN-2WCkKb6sQpTmlsY89nyG1sqNoKPtKUG5fFXR2gB3bvzUEU-piROITFPMu2oPu04FNXztnGXvZyf6TYDHpWvNMe29IENhISJXBSGW9Z8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/457e9bdb4f.mp4?token=S6h2zVXLtEgH-nFvtrygj2ebhmzUdEYFow4dcpN1uHshHbMclCV9tHx29vYPhMPMTBStq1ZjT_I7e7mOdcHfwUjkhrYiVIWd8Y1I2gBg77yb5uGgxmpVkWcmIIsW65qxqQ3nCCVW7rGHBPWA0mFYnTICccPs3rbasKwkIamUTy19mbqblMmHSLky5paVvUyqOXKoRmGWAaUDi3JEY32zxLHcukVoB0No5ICHBXmC5MiRgYQW9T5NFYOLEVtTZpx8XJdg2vG076viF62ZRu_XB9KDBsup3W8rKn82DTGGDAMnyJcN34PMekHL0HK-OssYHnMmY5PA-qo3Drz3KSwo0b_7S_eIV6yGXMYPmkeIqzoaY6FkHWjyyJzdoTsyWYHnPCImXnIzWmuYsKpLTo0rhdfGfgbmi0Bg0xVQ8krmwmphxLzr-rUhHck52GPgNIPlG0IB8Mgr7mivHFdLrwyH4rrqCmihrutVniwPxZq5yObrhkZ85fV_hv9rpHaPsOkNQIZCoM-yxB6opyHkmUZvyGTphlKBx_slfLng-2Nbta5k6NtJTBtEotwn_mtS9iwnfaN-2WCkKb6sQpTmlsY89nyG1sqNoKPtKUG5fFXR2gB3bvzUEU-piROITFPMu2oPu04FNXztnGXvZyf6TYDHpWvNMe29IENhISJXBSGW9Z8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
این روزها با قطعی‌های برق، داشتن یک چراغ‌قوه معمولی کافی نیست!
🔦
چراغ قوه دستی ۸ کاره LED Torch
هم چراغ‌قوه است، هم پاوربانک، هم ابزار نجات!
✅
نور LED پرقدرت
🔋
قابلیت شارژ با USB + استفاده به‌عنوان پاوربانک
🧲
مگنت قوی برای اتصال به سطوح فلزی
🔨
چکش شیشه‌شکن اضطراری
🔪
تیغ برش کمربند ایمنی
🚨
چراغ هشدار برای مواقع اضطراری
🏕
مناسب قطعی برق، خودرو، سفر، کمپینگ و نگهداری در منزل
❌
قیمت قبل: ۱,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۹۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
قبل از قطعی بعدی برق، این ابزار کاربردی را تهیه کنید.
https://memarket24.ir/product/brief/30291/180124/</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/678350" target="_blank">📅 13:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678348">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbLSq63bB_ddYs7T4sHd2BZLXxEgFyAWPbVZobQLu1KWUdK51rWMZQ8pwBv79HgJOZUU5TiFr079pEZ4npvZ_98EEQlKTUrPhWX4zKUeYCUFarAzBcVFw8PF-IxUOq1bM89G7hAcB2LWzcpaNxHjni8LpgBexWySx5OxvkXVpAf-WKtB98vw_LZ1BpxgPQgaVORKG3KFhbZ6DyQ5zzE5HPko6rYKnopBZ-p0SSBPGR2L9RytLudgF24hXAZHgg1kfwlDzbaHOjvp9QED2FsMw9AyMJJwTBDKnaD6X9HBpO_4oVet-Ix-dqjBcVxRpMheN7zKdKi0xkhUxp9cdeHjTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-VuTx89Gqa9cSA8ve_qwIkpiLlq-Yu4Pta-ZBy2ZFSgPXL1fDTFgFgCgjDlyXzcG42XKlwcVDZlbb_477VOFYcwt3MFxaozJsTTxmcovsiBLvsGFwRfCQxa8uGTvsvHmw1qtLPYXT071KLMj2zZ-G5AK1R-BGBoJkgke0MveTrbJxKNbQefuiR1qcZn_lEJ-AFWLSxm0xz7Ok59tc1yB_7IflyEwcHJNgU8QO2vbo3QF1yoEk17GdYBYJabyS_IuItnqF38_c7hTSDHurhIRIDQ1FOsiQS2eRs7T5xuPi98eYGsHC5f2qqJUPAEReORxUKjmOJvPo1YqGZNN9ICcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور سید عباس عراقچی در حرم مطهر امام حسین (ع)
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/678348" target="_blank">📅 13:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678347">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843e1723da.mp4?token=mxXrrS7gXdGOuN9hjwuLuzLYe0QHl2kCJemXtg1dRD-I4z4nkLSsgy8VtFxsPp5MrEok8LDxtpm1EsiiOJuY1awLyl-KgcesfCu9Ub2XzGYH7xui98RZxj3gxVKm76iRNe0-RSNWovPNkgabI7GHd0dGV_pq2riXN9vctBYkfffp46A118hJTrkDK8KGU-K7GV3pY9sB1xklN8blU49dvxiyutyWitkZ0j_4OmtPNw8BwBWrvl1dncwuldjkd5DRxIZWb_srp0IgRJyA3mkWX7WCbBM3PBcBZQE8bdOL012TCc4GI97FyqzPGptqXdQnEy-7GzgfwijrjbDrSQe6mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843e1723da.mp4?token=mxXrrS7gXdGOuN9hjwuLuzLYe0QHl2kCJemXtg1dRD-I4z4nkLSsgy8VtFxsPp5MrEok8LDxtpm1EsiiOJuY1awLyl-KgcesfCu9Ub2XzGYH7xui98RZxj3gxVKm76iRNe0-RSNWovPNkgabI7GHd0dGV_pq2riXN9vctBYkfffp46A118hJTrkDK8KGU-K7GV3pY9sB1xklN8blU49dvxiyutyWitkZ0j_4OmtPNw8BwBWrvl1dncwuldjkd5DRxIZWb_srp0IgRJyA3mkWX7WCbBM3PBcBZQE8bdOL012TCc4GI97FyqzPGptqXdQnEy-7GzgfwijrjbDrSQe6mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری | به نیابت از رهبر شهید در مسیر اربعین
🔹
روایت قدم‌هایی که در مسیر اربعین به یاد «رهبر شهید» برداشته شد.
🔸
الوفوری را دنبال کنید
👇
#زیارت_به_نیابت
@Alo_fori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/678347" target="_blank">📅 13:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678346">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
نیوزویک: نفوذ ایران در تنگه هرمز قدرتمندتر از سلاح اتمی است
🔹
مجله آمریکایی «نیوزویک» در تحلیلی نوشت قدرت مانور ایران در تنگه هرمز به ابزاری اثرگذار برای تغییر معادلات جهانی تبدیل شده و فشار بر کشتیرانی در این آبراه، آثار گسترده‌ای بر تجارت جهانی انرژی داشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/678346" target="_blank">📅 13:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678345">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8a9bf9b5.mp4?token=GqkEkaEAa-4TxjCgoJgV-vh_YfMnVJXvDCYaUVVJJMryOTlht7MQlIHWLZwX0ayZwg9OGhdK6_DRCEBYJunYXnp74KWfbBnW9CxaorxB3rSLVyd1Q897DIN6kBZswX3DTlbrLk0G8_JYSxUILJ45OiiGU2r1xZ2Ai6DjbJcMTOGpVv1M3GUmxgtxhJM34MnOGmfG6FQG_3GWMI4Dq0oBelrpqoZE1kpqCkJ06v9wa0Y91xps0mFJJhDA9rglZdgFPm0tV9xPBWM5gf3e2Sp85JNSQwLy6TPJmz50m6_yuAyV2rO9sH8sME1JF4CB2oC8hwjIfkhUMJ2Et6qRRb1ijA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8a9bf9b5.mp4?token=GqkEkaEAa-4TxjCgoJgV-vh_YfMnVJXvDCYaUVVJJMryOTlht7MQlIHWLZwX0ayZwg9OGhdK6_DRCEBYJunYXnp74KWfbBnW9CxaorxB3rSLVyd1Q897DIN6kBZswX3DTlbrLk0G8_JYSxUILJ45OiiGU2r1xZ2Ai6DjbJcMTOGpVv1M3GUmxgtxhJM34MnOGmfG6FQG_3GWMI4Dq0oBelrpqoZE1kpqCkJ06v9wa0Y91xps0mFJJhDA9rglZdgFPm0tV9xPBWM5gf3e2Sp85JNSQwLy6TPJmz50m6_yuAyV2rO9sH8sME1JF4CB2oC8hwjIfkhUMJ2Et6qRRb1ijA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری در بین جاماندگان اربعین حسینی؛ زائر جامانده: مهمترین خواسته مردم انتقام خون رهبر شهید انقلاب است
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/678345" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678343">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2521c22.mp4?token=FpyyW5mxALdP_J2cuxi0Q0F7Ul-BALWgekf2_oGlQHVz0inyX8r9F3elokJnHIyarEJ8lYeK0eB22A8JuWyxFFCI2qZBsvRCSWcxs5vrsnmsefw6YfE4zoWglPq2XbPNsnsE94XkGtFcfBmOqFAJWYUM0SO6ithF3dz82BotnQ1JOnGpLVn-hFMPmDFFO3QxVNYCv1tX7ElxFdrxBK9oX2DtHaMVHFsuz_8EeoTrNPdBxdIwsUUZhqdx0XbvVwXa1_IxOIKGHLNezBDNalYNaiUQWpmsMtjyF1_Atj2EIFteQNQGhbZaaP8RqtiyGEJocnb5H7P5itHLc0XdNpV3gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2521c22.mp4?token=FpyyW5mxALdP_J2cuxi0Q0F7Ul-BALWgekf2_oGlQHVz0inyX8r9F3elokJnHIyarEJ8lYeK0eB22A8JuWyxFFCI2qZBsvRCSWcxs5vrsnmsefw6YfE4zoWglPq2XbPNsnsE94XkGtFcfBmOqFAJWYUM0SO6ithF3dz82BotnQ1JOnGpLVn-hFMPmDFFO3QxVNYCv1tX7ElxFdrxBK9oX2DtHaMVHFsuz_8EeoTrNPdBxdIwsUUZhqdx0XbvVwXa1_IxOIKGHLNezBDNalYNaiUQWpmsMtjyF1_Atj2EIFteQNQGhbZaaP8RqtiyGEJocnb5H7P5itHLc0XdNpV3gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منظره‌ای بی‌نظیر از شفق قطبی از دیدِ ایستگاه فضایی بین‌المللی
🔹
فضانورد Menon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/678343" target="_blank">📅 13:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678342">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
گزارش‌ها از حمله به یک کشتی در نزدیکی تنگه هرمز
خبرگزاری رویترز به نقل از منابع امنیتی دریایی:
🔹
یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت یک پرتابه قرار گرفته و عملیات تخلیه آن توسط خدمه آغاز شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/678342" target="_blank">📅 12:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678341">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d670217fb.mp4?token=PyZ2Xxl8CyRzONyLcMHCblOZF75ADR7BHkcKtA5cvHBDPlSz7vMp10XH6WMPSR1RqrxZxvDt8ySfShrx1L0Ny3Zsy9nxcMyz2fQ9Lo6bACKwaxqk1rlHigdx6n6KEpa1zOF3AwQVvc2FGHJU1UhIrsTT9BNkPWUmv6cKmq-IwAUIReZZRSQy_9SpZ3cfZr7dNFMLldCSdRT8y8Xf-K7XPbEvabLtqq-6eb0MUiXmKbbqzEXS0iYtxpBvIbXdn3Ttwt3US3tx3knStJUsOOz14115YNE3xuIVpMyOj8-zFEoLTTC0FD8S3eHmzTaKnVIDXHsl-rV2vKzgiTh1YLX3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d670217fb.mp4?token=PyZ2Xxl8CyRzONyLcMHCblOZF75ADR7BHkcKtA5cvHBDPlSz7vMp10XH6WMPSR1RqrxZxvDt8ySfShrx1L0Ny3Zsy9nxcMyz2fQ9Lo6bACKwaxqk1rlHigdx6n6KEpa1zOF3AwQVvc2FGHJU1UhIrsTT9BNkPWUmv6cKmq-IwAUIReZZRSQy_9SpZ3cfZr7dNFMLldCSdRT8y8Xf-K7XPbEvabLtqq-6eb0MUiXmKbbqzEXS0iYtxpBvIbXdn3Ttwt3US3tx3knStJUsOOz14115YNE3xuIVpMyOj8-zFEoLTTC0FD8S3eHmzTaKnVIDXHsl-rV2vKzgiTh1YLX3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور گسترده هواپیماهای سوخت‌رسان آمریکایی در اسرائیل
بلومبرگ:
🔹
تصاویر منتشرشده از فرودگاه رامون از حضور بیش از ۴۰ هواپیمای سوخت‌رسان آمریکایی حکایت دارد؛ ده‌ها فروند دیگر نیز در بن‌گوریون و حیفا مستقر هستند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/678341" target="_blank">📅 12:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678340">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سود آرامکوی عربستان در سه‌ماهه دوم سال با وجود اختلالات جنگی ۴۴ درصد افزایش یافت.
🔹
کانال ۱۲عبری: جلسه امروز کابینه امنیتی رژیم صهیونسیتی لغو شد.
🔹
عملیات انهدام مهمات عمل‌نکرده، فردا از ساعت ۷ تا ۱۲ در قزوین انجام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/678340" target="_blank">📅 12:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678339">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl_XwaLksGYDDv5C1QjrsXwiEHYtTU3jDg_UFWCZUpn5wWnqSfmKb3weKLaZCdrfLqEPFcyiY1_x9-8gw7WB-tQUBRRVKiGQhcUx6bW2rVcNmHHySEVrxadsxveU0zimZjUtitYD_P_NtXrIzjGwlVi8TcOkuUCHWhi689RukFrdLjpgugTlJRPVkzAdDiajztyZqLO0aa6kz5TYywGYmYU3shIeHbxHfs5An9CzizvGwlJCPjOEBIXJ1e7frp6GcXOywcCFL-fK1Ty3-LLOrI6EKYoNHWInM_26DeTMkOSq2J4yU4qhijVGRBP4qEEnO_elOY4HT4ZeRaIW-_AaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو با درآمد سالانه حدود ۳۰۰ میلیون دلار پردرآمدترین ورزشکار جهان معرفی شده است
🔹
درآمد او علاوه بر قراردادش با باشگاه النصر، از برند شخصی، تبلیغات و فعالیت‌های تجاری‌اش تأمین می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/678339" target="_blank">📅 12:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678338">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
حاجی دلیگانی: در حال جمع‌بندی و جمع‌آوری مستندات برای استیضاح عراقچی هستیم
حاجی دلیگانی، نایب رئیس کمیسیون اصل نود:
🔹
هر نوع توافق با عمان درباره تنگه هرمز باید به تصویب مجلس برسد. افکار تیم وزارت امورخارجه در دوران قاجار گیر کرده و از روی ترس و وادادگی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/678338" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678337">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4b55bb3e1.mp4?token=nIRMvKyqHov0loqYP17ohOahsOMe2wcBUS5-s8Rnbh2pQdz99nBEUwN1iu1CEdxAu4S2j-5OtcIP2DYQXsq3OwX_MOgFICYoY_Au55wd3OYkrh6QxOwzTSWCSVNob1zIQwq3CAHREzYxYj36sdok6OJjcUyhjYEVyRoRsai0XI6DGSmR95oXoyY1ZTJqVbAnGMnDhGciXp4eqOv4nxe4DgiMhAW-i2fC4AvSPqfYgYdUeuk1V3cfxac-ispI5tny517r5CQqnWJ1lWWy9elJNOC78l4FHxDXKJKOu6WgFb11v8PxmHViKJdnS0H7ztNq1S6QZVkzWgKyl0f_x2XoTb1wkJT5Zyde9rMRQ5XKSlhJWdOLmPbzK3xfNEvryaTeWS5R4k7sdjIwo-yhKch42A3L2p2jKw6R76mnnUjlIxWoRkhIIDTQc4cVLO7J2D4zXfBcsunCDS593zQJY_GOH9GNGJCfHXEqA6AhHPMuZDFNwsZ-Qwj5yYtq_RbYLPSjV2biXXHkzX44yaCoWHtQmyQPyojH6CglKtp1VFm9D0jObKPUUXnjTaiU5qF4XSReLKuv7nwTortgFPX85f7vdfJZLUzpsj8h5S3HoE0uYkmnOZP2wicO9nOtyjZBCyGSfGR97iTOiaXOIVEhDtptlMMtYWjhxLh5t1U4g9_4NfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4b55bb3e1.mp4?token=nIRMvKyqHov0loqYP17ohOahsOMe2wcBUS5-s8Rnbh2pQdz99nBEUwN1iu1CEdxAu4S2j-5OtcIP2DYQXsq3OwX_MOgFICYoY_Au55wd3OYkrh6QxOwzTSWCSVNob1zIQwq3CAHREzYxYj36sdok6OJjcUyhjYEVyRoRsai0XI6DGSmR95oXoyY1ZTJqVbAnGMnDhGciXp4eqOv4nxe4DgiMhAW-i2fC4AvSPqfYgYdUeuk1V3cfxac-ispI5tny517r5CQqnWJ1lWWy9elJNOC78l4FHxDXKJKOu6WgFb11v8PxmHViKJdnS0H7ztNq1S6QZVkzWgKyl0f_x2XoTb1wkJT5Zyde9rMRQ5XKSlhJWdOLmPbzK3xfNEvryaTeWS5R4k7sdjIwo-yhKch42A3L2p2jKw6R76mnnUjlIxWoRkhIIDTQc4cVLO7J2D4zXfBcsunCDS593zQJY_GOH9GNGJCfHXEqA6AhHPMuZDFNwsZ-Qwj5yYtq_RbYLPSjV2biXXHkzX44yaCoWHtQmyQPyojH6CglKtp1VFm9D0jObKPUUXnjTaiU5qF4XSReLKuv7nwTortgFPX85f7vdfJZLUzpsj8h5S3HoE0uYkmnOZP2wicO9nOtyjZBCyGSfGR97iTOiaXOIVEhDtptlMMtYWjhxLh5t1U4g9_4NfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا با زدن شبکه برق، خاموشی گسترده رخ می‌دهد یا نه؟!
/ تلویزیون اینترنتی مدار
این برنامه را در یوتیوب تلویزیون اینترنتی مدار ببینید
👇
https://youtu.be/t3Lh7QB4jp4
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/678337" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678336">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ادارات و بانک‌های کدام استان‌ها چهارشنبه؛ ۱۴ مردادماه تعطیل شدند
؟
🔹
کردستان
🔹
قم
🔹
هرمزگان
🔹
ایلام
🔹
کرمانشاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/678336" target="_blank">📅 12:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678335">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54260195e.mp4?token=LBD0rF5QVM0rftEpBuw5RQKtA68wRdMyUU44HcEnq_LzOSm2SSFu10bKJq_PBz-bqver9nUH-a9kB1hGrhyb3xdcB5vp43628qQJJtbXfUj9wCZ3f7xzgEcY8UVQqs37svkEa3bl75OHv-QFS7xACpUO2_xwqCpdPhzmQuWPcaxmwkEvJ8PnNU2FZWHYVWebT0ak8EHh99mOLnxcwXcc8WlTVofH3gSBQSxsz1A2u33LoiZch_YAcjAOGnaRgwR18I7Hn5K8oS7nbbDC8H2T43g4yCOJgrOR2w4gaJjvrkGxX3n2Ip3TfWVw8uMNZkrdiAgqW-SRZV8k5r5LnJQwngBDQqffj7mZU2ciSGWnXmuck9i3eYhRpklpyoaPTRoe6ITbvVMxfdH0-4RUAGQmb3C82PL6l-PqpwukbOvGGhDQ2hVUVFnK-HdYPrrvMObN8JfBMhm2wEVS3SoEXfy3y6rt26iIppdIN2u5Ic_c--_M-X_TNJB-EQoCqnhgJFFUZ2BErTbeWM-L3kG14hwPhixwrpGftJ_wY_aZmRqbne9LcQXwvMtFqIZwatnzto7Qgosvubut28_d7gMqtPPv0iFvoMuSK3-mY2dk4Zse1TmCXGGMJ3ipUIPQtb5ABU0QAoIg2aVuDC6SLYjaxTDy7aGwhH3Fdn6pdJ-vvSffFqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54260195e.mp4?token=LBD0rF5QVM0rftEpBuw5RQKtA68wRdMyUU44HcEnq_LzOSm2SSFu10bKJq_PBz-bqver9nUH-a9kB1hGrhyb3xdcB5vp43628qQJJtbXfUj9wCZ3f7xzgEcY8UVQqs37svkEa3bl75OHv-QFS7xACpUO2_xwqCpdPhzmQuWPcaxmwkEvJ8PnNU2FZWHYVWebT0ak8EHh99mOLnxcwXcc8WlTVofH3gSBQSxsz1A2u33LoiZch_YAcjAOGnaRgwR18I7Hn5K8oS7nbbDC8H2T43g4yCOJgrOR2w4gaJjvrkGxX3n2Ip3TfWVw8uMNZkrdiAgqW-SRZV8k5r5LnJQwngBDQqffj7mZU2ciSGWnXmuck9i3eYhRpklpyoaPTRoe6ITbvVMxfdH0-4RUAGQmb3C82PL6l-PqpwukbOvGGhDQ2hVUVFnK-HdYPrrvMObN8JfBMhm2wEVS3SoEXfy3y6rt26iIppdIN2u5Ic_c--_M-X_TNJB-EQoCqnhgJFFUZ2BErTbeWM-L3kG14hwPhixwrpGftJ_wY_aZmRqbne9LcQXwvMtFqIZwatnzto7Qgosvubut28_d7gMqtPPv0iFvoMuSK3-mY2dk4Zse1TmCXGGMJ3ipUIPQtb5ABU0QAoIg2aVuDC6SLYjaxTDy7aGwhH3Fdn6pdJ-vvSffFqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی جدید از حجم تخریب ناشی از بمباران اسراییلی_آمریکایی در محدوده رسالت تهران، کوچه جاجرودی. ۱۸ اسفند ۱۴۰۴
🔹
گفتنی است این محله با ۵ بمب ۹۰۰ کیلوگرمی توسط دشمن بمباران شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/678335" target="_blank">📅 12:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678334">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499a783e28.mp4?token=XDwHB1rjUzB1JikhmS5D5dZ_lJWD_RShIzyKQs12o5BN7bpoxUjzjbmSjslyI9MhTPGwEKZw--qGo3rJQpqOxRMQSNmu12XATkteGsadJGt7SoOpd60HLn-moBFWJspSYtJodG9vjfl4VyvOYD2zGTF2djnZs3yEmT4a9FRxTJdJD0xDnb8KH2imiHIdefmoHg499_e0pdc7Ul39fTIBpBPH-HbQ-dsgbl_nSJ4xqQTR3QUwuJ4h7K9rQ-SqYT7MyChh2albYvLmkdPlHlHnUxJbnfcw3VdpP09IMGx4BeESk2qSs6HG5zRNfYqsQDr78VDjflWxvXcG6wf-zTgI-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499a783e28.mp4?token=XDwHB1rjUzB1JikhmS5D5dZ_lJWD_RShIzyKQs12o5BN7bpoxUjzjbmSjslyI9MhTPGwEKZw--qGo3rJQpqOxRMQSNmu12XATkteGsadJGt7SoOpd60HLn-moBFWJspSYtJodG9vjfl4VyvOYD2zGTF2djnZs3yEmT4a9FRxTJdJD0xDnb8KH2imiHIdefmoHg499_e0pdc7Ul39fTIBpBPH-HbQ-dsgbl_nSJ4xqQTR3QUwuJ4h7K9rQ-SqYT7MyChh2albYvLmkdPlHlHnUxJbnfcw3VdpP09IMGx4BeESk2qSs6HG5zRNfYqsQDr78VDjflWxvXcG6wf-zTgI-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی اوکراین به کشتی ترکیه‌ای
🔹
به گزارش رسانه‌های ترکیه یک کشتی باری این کشور در حمله‌ای که ظاهراً با پهپادهای اوکراینی انجام شده، در نزدیکی بندر نووروسیسک روسیه در دریای سیاه هدف قرار گرفت و دچار آتش‌سوزی شد.
🔹
بر اساس اعلام اداره کل امور دریایی ترکیه، ۲۲ خدمه سرنشین کشتی بودند که ۱۳ نفر آن‌ها شهروند ترکیه هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/678334" target="_blank">📅 12:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678333">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0c04f2544.mp4?token=le8430blX0Rvx7JqWoRS2bN2u0x2A3ULXm-jFjqA698o4FfU2GuaHDKeaS_hAtDQLCFuOYxVgMx7otb5Yxr_Hb-GtciWN4pkLw1nSQOR7iMPuxANcWI8vkvvwvGre8D8PF4V89J6bzJaNJ6xlUg14A63MFGiuEs7QtaxrLN8Nf9Zt6uUJ1SgC5r8_JobPdkkU8MoTRR0aRKo1_Sd8ZkMlss_6YCHCUv20_vMBwFGa6Hzl1ZXv6hNJLRr5kl5I9vNvClKfTmMZ6MNCtdo5vfaJb8Mk38MguL18aOFVd88DAYlmVQSKvTb4SNPHs1juhI2rSKf7bPg8SVtIFuzSxmDGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0c04f2544.mp4?token=le8430blX0Rvx7JqWoRS2bN2u0x2A3ULXm-jFjqA698o4FfU2GuaHDKeaS_hAtDQLCFuOYxVgMx7otb5Yxr_Hb-GtciWN4pkLw1nSQOR7iMPuxANcWI8vkvvwvGre8D8PF4V89J6bzJaNJ6xlUg14A63MFGiuEs7QtaxrLN8Nf9Zt6uUJ1SgC5r8_JobPdkkU8MoTRR0aRKo1_Sd8ZkMlss_6YCHCUv20_vMBwFGa6Hzl1ZXv6hNJLRr5kl5I9vNvClKfTmMZ6MNCtdo5vfaJb8Mk38MguL18aOFVd88DAYlmVQSKvTb4SNPHs1juhI2rSKf7bPg8SVtIFuzSxmDGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین کلاس‌های درس را با هوش مصنوعی متحول کرد؛ تخته‌ای که معادله را به مدل سه‌بعدی تبدیل می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/678333" target="_blank">📅 12:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678332">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
الجزیره: دور جدید مذاکرات لبنان و اسرائیل در ایتالیا آغاز شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/678332" target="_blank">📅 12:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678331">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrcFaHbC3a7LNnBvSqvdDUAtaz9CaXCBO6XkseC3JiluNoFkKLl1MrM1gx8hOi-MCEcSDAoI3in-rpfzNS_ATeOJKtCccBaknuEEPYYf8TObaWZeMOmDuNUtWE5fc-jOUeUx8w1bky2sEU-na5OEegmw-3BhSBwKo0wtqzT6ApwPkIcnR9GDGZ4tPiM-MTZ--PPmEgPu7qPpajld_sQW4EXVK-0Nf1WE2ot74J4uu3Iv-w2WGAVPz0clUdNR63IuNjdlUnihF0P8AeVk_0oaifbY14MoFhoIyeb8qUC4Lp4u_XnWdNrPq3nywP4YB54UIuCLHNoPeCO7-WqaAAIvBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت بلیط هواپیما تهران به اصفهان تا ۲۱ میلیون تومان
رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/678331" target="_blank">📅 12:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678330">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7h5qmSN49ASYUOgCKgs6bO8p1yUnROqIfVnqXO1iPMcfPnNqRrjojigYGSHIa61h2dOB-MpoMfNWnoHWVnilVu1-lsks_xlOysVedEg_D7ZkgK5Y_IojVDN8jD67kGAPRaqiBF0DD_pBhyum24mh7io2ROmqtmPq5OUmAXU5kxNU1GHs2FDuxSJeGVW2k06c1yR_FmSe3ayKiCG8rEPLvU70pjUY2_aNsuNTafhZ_31gTjV_bV30aPHTtChNXIsi_AjFJ33PRa0jXP-JrY2EzuDLFu4H9L69F9knJMNcZMoG54IYctTR-LNVNkWHt1N5iy_AnCTlOxIPCPOdSdnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا رویداد اربعین به پیوست رسانه‌ای نیاز دارد؟
🔹
برای شکستن بایکوت خبری رسانه‌های بین‌المللی از این رویداد و تصاویر و روایت های فاقد اصالت که توسط برخی بلاگرها در رسانه‌های اجتماعی منتشر می شود، نیاز به یک پیوست رسانه‌ای جامع وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/678330" target="_blank">📅 12:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678329">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت اربعین</div>
  <div class="tg-doc-extra">حاج مهدی سماواتی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/678329" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
صوت زیارت اربعین
🎙
حاج
#مهدی_سماواتی
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/678329" target="_blank">📅 11:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678328">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUd0V6QiBd8OcIkfYoXL0mgu4V1FPuLNf13q2xbULKBKKX7AKoX2A5csIwanMG3xJrI2Aq6z9i63osVlFmjFtcht-YRXUcRi6TAQWcfvPN82Kwm_V_j8oISbYZlicLm8wcDVLBVjhwueolxLLYJCnXIf80t7RkE7zllcFXzDVDLDlMVT1BAxoLlkyikESpxT22Ab6xsK3CS572MM82yBg_h2IBHfJjgDWNOHLiVCytJQQe5-TP6RNXFo-tCGxlVRjitmZ6NfqpLKJN3OIhqQadq15x_9uZwYEUu-N2nwgL7gUywj_frmUFztEfLtgH8PLcw0pmCM1BWKp7YGAIeCzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
متن زیارت اربعین
▪️
زمان قرائت: پیش از نماز ظهر اربعین
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/678328" target="_blank">📅 11:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678326">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouV4_YoM2h0AhyRDn7DT0TWXjjNVFOXgJH-fQ2Hsdyxb1Hn0SSa1Oo1I6plr1RAtgULslyN77MazldZvqSgeSwNkopfER1eUAdh7UAzxqAUrVcnjt9qPL-OJyfxvA3Z8yZAlbAPRgfP7NpYtz1cl1lXfMh_G3qgTlHh-SP7jO8DXeSNcbU7C_D3SbTdyuwy4gYNBlyHxgMwnO1-L9K7w2iPSegH1CwhWnNJ-W-76kePvz2zsXuFYm8XlOMKRUsq2AzFipTYG_TYGsJwpoWdlX77cIWI1rnS5xTTNMHROCit5zcg-0F0M0QORM3Z7pCydY-y2nn9nnPvr1luSxU9JRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیتر یک روزنامه اسرائیلی یدیعوت آحارونوت: «تو ما را دیوانه کردی»
‏
🔹
ترامپ: «من حمله خواهم کرد.» من حمله نخواهم کرد. من حمله خواهم کرد. من حمله نخواهم کرد.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/678326" target="_blank">📅 11:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678325">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سود سهام عدالت کجاست؟
یک نماینده مجلس با انتقاد از مبلغ سود سبد سهام عدالت:
🔹
سودی که به سهامداران پرداخت می‌شود، با واقعیت‌های اقتصادی کشور و نرخ تورم همخوانی ندارد و برای بسیاری از خانوار‌ها اثر ملموسی در بهبود معیشت ایجاد نمی‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/678325" target="_blank">📅 11:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678324">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouJyWktcV2VI1ofXT-jWxBvAAjUAYl5400gMwzfVYoNM2dBIn1VZpoL7WidFMTfHKvxsyylM527owuqAUj_9wUc03gllgTb8nC4C0edRWqnURYhvRXSbnXTOSFDe0j9nHIdgZ5DgVvoLX9PKxAP7qhQRu2EytiVV7xHP5nlbUzEnayuN34wGy6THv89fbobKYc6SOAY5a-OvzvZXk8YtNsB_SXk9HQdd8SQTgob5h1r7XMnmOJ4JWNChdx5OM54XHxvsH8UxgXGwVhbGIRJ3kfsQJF3Mr88I5Qmd-WrjVtyAOiYZRqOPNBLKAqqUHk-U_bopEdSwcOjYcszytnx72Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمدید قرارداد امیر قلعه‌نویی در اولویت است و شایعات درباره جانشینانی مانند نکونام، گل‌محمدی و مجیدی صحت ندارد
🔹
تمرکز فدراسیون روی موفقیت تیم ملی در جام ملت‌های آسیا، استفاده از جوانان و حمایت از تیم امید برای مسیر المپیک است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/678324" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678323">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
یک منبع بلندپایه به العربیه: سفر وزیر امور خارجه ایران به اسلام‌آباد به‌زودی انجام خواهد شد
🔹
میانجی‌ها برای دستیابی به اعلام رسمی و قریب‌الوقوع آتش‌بس، به زمان بیشتری نیاز دارند./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/678323" target="_blank">📅 11:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678319">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
حدود
۲.۵ میلیون شغل در یک سال از بین رفته است
🔹
بر اساس تازه‌ترین داده‌های آماری، نرخ بیکاری در بهار سال جاری به ۹.۱ درصد رسیده است؛ رقمی که نشان‌دهنده افزایش ۱.۸ واحد درصدی نسبت به مقطع مشابه در سال گذشته است. در تقابل با این شاخص، نرخ مشارکت اقتصادی نیز با افتی ۰.۵ واحد درصدی مواجه شده که زنگ خطری جدی برای بازار کار به شمار می‌رود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/678319" target="_blank">📅 11:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678318">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7355806b35.mp4?token=fpL124SsZcrFk9lEXw4T7oVi93tUihVWn57GgkMPfxHAqEOHl5hAXswALd6CqU0WDoPs3q8d4l3RzZkhRbR-1xkhmtWZEGq0AD_i_JAOb8H4DXRXTDAJ-Fb4Fg01cG9Um69K7asEjC23yY6vWN16YRttMtsPQ_2zcGQROkHmpYKZsLRtUHO_TWt4xvzmSifSfaGd89YxzyV0Y1iwTd7kFmk7xySrk1_6YoPrJvz4IWefl-xHtNkvd8MfaGDs6k84KBUOfQriiQgGR_Xt9sWxgzqnLS4unOleVRQg1U4AiuMC3rvc6E6pm7QxUuhxidUbla7bzJfQyw3YoUJLUksNXamL4JfX8JJx1ItT10b9b0-IeRu2FCqfZiH5AUjsa47y5ejnsMH1v3BZsPw6VqEXKiIjJmef0E1tJ__LRdw9-PAExllQosnQtOmf49H1MdqG7ge2enq2WF446AvSpbqrmvdFkgAzP4HlaLWeqZbx1MRvU9E8eBCXLp_p_CHgj4EI0JaeYE_DDaypCrZ7AwX_FY9YycnUqgc-DYwPkfaokN8AUi5OSzg_IiQLqZZGaBNyniabYFrtUueCX00qkUJQeFOnIujI6rVXncwPY06dDrBEKclhgPw_SXaEBD6LdwZIp3WMEu7S3kHVppKVqHnOQ5ISxL4qXIOfLb5OCuuxWtc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7355806b35.mp4?token=fpL124SsZcrFk9lEXw4T7oVi93tUihVWn57GgkMPfxHAqEOHl5hAXswALd6CqU0WDoPs3q8d4l3RzZkhRbR-1xkhmtWZEGq0AD_i_JAOb8H4DXRXTDAJ-Fb4Fg01cG9Um69K7asEjC23yY6vWN16YRttMtsPQ_2zcGQROkHmpYKZsLRtUHO_TWt4xvzmSifSfaGd89YxzyV0Y1iwTd7kFmk7xySrk1_6YoPrJvz4IWefl-xHtNkvd8MfaGDs6k84KBUOfQriiQgGR_Xt9sWxgzqnLS4unOleVRQg1U4AiuMC3rvc6E6pm7QxUuhxidUbla7bzJfQyw3YoUJLUksNXamL4JfX8JJx1ItT10b9b0-IeRu2FCqfZiH5AUjsa47y5ejnsMH1v3BZsPw6VqEXKiIjJmef0E1tJ__LRdw9-PAExllQosnQtOmf49H1MdqG7ge2enq2WF446AvSpbqrmvdFkgAzP4HlaLWeqZbx1MRvU9E8eBCXLp_p_CHgj4EI0JaeYE_DDaypCrZ7AwX_FY9YycnUqgc-DYwPkfaokN8AUi5OSzg_IiQLqZZGaBNyniabYFrtUueCX00qkUJQeFOnIujI6rVXncwPY06dDrBEKclhgPw_SXaEBD6LdwZIp3WMEu7S3kHVppKVqHnOQ5ISxL4qXIOfLb5OCuuxWtc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای ضریح مطهر امام حسین (ع) در روز اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/678318" target="_blank">📅 11:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678317">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78abc77a3c.mp4?token=ikTAHsZWPNCc7hnpWx7AhHqvJCrfCdJ4umzkdF7zWyvlglnmynnpyeYD0R6tXdS693Tzuwa19nx92GO66tIcOyrS0Jv93FZEKScoITWcG6zt0djMqJFssuEuFM12NXCRQWz-cb7LRF-ldK49fFu1ndn6QCEVitFezXL7QCGTwSbHED1BeMNqK_l6AQ-3LgKuyp_eXAmY6ZuYxj7QDOsAa82tmybhmpxB7FQEx2tiBykl462dga954mTfJr42P_vRDoa28ZVwo_7ZfbPvJ_vrxdsqRmp2bYrRow6i41fx9lq6mSaw5Y-29AEnYQNMty9xksX8mgXdpUMxh7d_uEm9GzpnEr7r-XeZHQpr9_cCV4z6b-CT_Kn8ClaTMJXj1TfKm3T0WYY8AyueoG02mxLuhzKYDNWzSEOAkK8iyV09FAJgcMUmG4p0pLMdr_JUpOjbxV4BlGM9i_IfeYP_8GWmdgfdgrnI6Nl1M1NUs1ulLCQwAw3YaU_3ggI71kCYQbirrGPPomi6rFbJ-0c7ixUkB6mRyYAOrNq7_noGE3ZWgQ3LxAW1hPiuaOv8k2ucDJ7LEbGv0iZIfY30J8ks0jn6ke87Dx4oSQVuXuuItDHye9HVE8I330xkfPOmz9a72zz9x_H6H_4V05qi_2KKVMJdY0BDZ4w7HLu5YC-_-h1Vz0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78abc77a3c.mp4?token=ikTAHsZWPNCc7hnpWx7AhHqvJCrfCdJ4umzkdF7zWyvlglnmynnpyeYD0R6tXdS693Tzuwa19nx92GO66tIcOyrS0Jv93FZEKScoITWcG6zt0djMqJFssuEuFM12NXCRQWz-cb7LRF-ldK49fFu1ndn6QCEVitFezXL7QCGTwSbHED1BeMNqK_l6AQ-3LgKuyp_eXAmY6ZuYxj7QDOsAa82tmybhmpxB7FQEx2tiBykl462dga954mTfJr42P_vRDoa28ZVwo_7ZfbPvJ_vrxdsqRmp2bYrRow6i41fx9lq6mSaw5Y-29AEnYQNMty9xksX8mgXdpUMxh7d_uEm9GzpnEr7r-XeZHQpr9_cCV4z6b-CT_Kn8ClaTMJXj1TfKm3T0WYY8AyueoG02mxLuhzKYDNWzSEOAkK8iyV09FAJgcMUmG4p0pLMdr_JUpOjbxV4BlGM9i_IfeYP_8GWmdgfdgrnI6Nl1M1NUs1ulLCQwAw3YaU_3ggI71kCYQbirrGPPomi6rFbJ-0c7ixUkB6mRyYAOrNq7_noGE3ZWgQ3LxAW1hPiuaOv8k2ucDJ7LEbGv0iZIfY30J8ks0jn6ke87Dx4oSQVuXuuItDHye9HVE8I330xkfPOmz9a72zz9x_H6H_4V05qi_2KKVMJdY0BDZ4w7HLu5YC-_-h1Vz0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واقعیت غرب از نظر روزنامه‌نگار مطرح ایتالیایی
🔹
این واقعیت غرب است، به جای تقدیر از ژنرال سلیمانی که فرمانده مبارزه با داعش بود، او را ترور کردیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/678317" target="_blank">📅 11:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678316">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b44c7d239.mp4?token=cgchzrc00e3wFfYKedVkx9eFa9BoAvdsNf7qKaJuHdWeu13SvYAmI3sYjgo1KfBMI5qyFjy8F_UmizsAntcH2W3kW-9-mgE7BNG0KW3G0hA2nQ5haQaUL_MQGvEviZYKFOu29uvULaiG7Owt6VE5ch8SgB9_y4JKrFe3lfXiu8D7Jo49pez7cGDTL3stfAbuW_V35KDP3NeQ7ZnTVx6Hf2O_Q9EbIEk509mEjQiNRqn4yl72k1xEkxFQCNHwhb2Kw4cW8gHgRTtLSxCsaimTBkxHR4WMxidMHhSdkq2d3leRz00w5cGqR4QCJYan05nulVTND9VeR9BCMkXXmpjavw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b44c7d239.mp4?token=cgchzrc00e3wFfYKedVkx9eFa9BoAvdsNf7qKaJuHdWeu13SvYAmI3sYjgo1KfBMI5qyFjy8F_UmizsAntcH2W3kW-9-mgE7BNG0KW3G0hA2nQ5haQaUL_MQGvEviZYKFOu29uvULaiG7Owt6VE5ch8SgB9_y4JKrFe3lfXiu8D7Jo49pez7cGDTL3stfAbuW_V35KDP3NeQ7ZnTVx6Hf2O_Q9EbIEk509mEjQiNRqn4yl72k1xEkxFQCNHwhb2Kw4cW8gHgRTtLSxCsaimTBkxHR4WMxidMHhSdkq2d3leRz00w5cGqR4QCJYan05nulVTND9VeR9BCMkXXmpjavw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ۴ پلنگ در ارتفاعات میناب
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/678316" target="_blank">📅 11:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678315">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4ea9972b.mp4?token=Un_TJW3NPB1O_lzaEAvIP_Gr6u5b5VfkyXqyu6cXbi1cKNDVmiwHz1SuDo4R_ehEUrBRjB7b5ekNCbuKOMfB5S4gooHQCJeRopTJW-b0J02ExMjwsUNqc6yjaD-hcpDJaEWhnlu8TKGpdbRykXCdmEajh6OGf0eAdmmU-KuVaNs1cvooqnBiVdyFUvbboxmktifhCg9o_rVqyfz_wIIAt-osf0FIa7fQVjBqPezBA8Z17N6gJYIVN5tWMe-uyZ_1tWmDkgptD4AUGOldJOvXgOxy4jXSpQM7It5I8F2M04An20iczvbgPJ97X_GBaJR-nWEl2AFhX4-LWvI15aOzkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4ea9972b.mp4?token=Un_TJW3NPB1O_lzaEAvIP_Gr6u5b5VfkyXqyu6cXbi1cKNDVmiwHz1SuDo4R_ehEUrBRjB7b5ekNCbuKOMfB5S4gooHQCJeRopTJW-b0J02ExMjwsUNqc6yjaD-hcpDJaEWhnlu8TKGpdbRykXCdmEajh6OGf0eAdmmU-KuVaNs1cvooqnBiVdyFUvbboxmktifhCg9o_rVqyfz_wIIAt-osf0FIa7fQVjBqPezBA8Z17N6gJYIVN5tWMe-uyZ_1tWmDkgptD4AUGOldJOvXgOxy4jXSpQM7It5I8F2M04An20iczvbgPJ97X_GBaJR-nWEl2AFhX4-LWvI15aOzkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اثاث کشی بدون دردسر، در طبقات بالا در ترکیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/678315" target="_blank">📅 11:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678314">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fd5edb2d.mp4?token=FKHOQzmxnOaqoGkRl57CW0XtPED7vAMjeqlVVR3yA8JBrmIOhFMPQmltQ4gYAV3Zf_0j4Fm_Hv5rCTP_q2Cj43JTb7R1ElAxVPt9v9Aps8EgTlNbF-whM0G6na8vMmMtIU-ChRTsJrMcihi-0034zuyzh366pjZht2-6v7cFAXS5MN34F052-l_YeTRpqrYd0JCeQ5sh1iByJgudfVApe6hpJw90cxr1hTFcK3WQ4cnuEi4rT3SkxZp1yt_Q5n5vO-CwLpGKriyI0xUr1vPLyXK0NLlPu8kKvdbQh_7UzeCm_gZoiTGiTHc20dWbJq9SU1YQ2bGusF211img8LgkzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fd5edb2d.mp4?token=FKHOQzmxnOaqoGkRl57CW0XtPED7vAMjeqlVVR3yA8JBrmIOhFMPQmltQ4gYAV3Zf_0j4Fm_Hv5rCTP_q2Cj43JTb7R1ElAxVPt9v9Aps8EgTlNbF-whM0G6na8vMmMtIU-ChRTsJrMcihi-0034zuyzh366pjZht2-6v7cFAXS5MN34F052-l_YeTRpqrYd0JCeQ5sh1iByJgudfVApe6hpJw90cxr1hTFcK3WQ4cnuEi4rT3SkxZp1yt_Q5n5vO-CwLpGKriyI0xUr1vPLyXK0NLlPu8kKvdbQh_7UzeCm_gZoiTGiTHc20dWbJq9SU1YQ2bGusF211img8LgkzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اذعان سناتور آمریکایی به شکست سیاست‌های جنگ‌طلبانه واشنگتن
/
تلفات، گرانی افسار گسیخته و کمبود مهمات، آمریکا را به بن‌بست کشاند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/678314" target="_blank">📅 11:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678313">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c553f9c184.mp4?token=tjoXfjzoi0EYSCuHjFVb7oZVW0zN43iPL8hVEJ3QgKLUTFa7KXEraGRS146HeG7JwfhWCZachlhKPiel9AT_wEhK33MeC7rhgZ9Ieqh2Y9yEGWH3tNRfCoFd1zrecSc_F-7IPA-2PwkhhD2O0X54-lxfpsIyd5DDnI_E9d4fH0MsOHAzuUo0V0Oojdr8w3HM68qdAfP4XdHn29szHjFFfA06QtavVl9JzZ3RGJ8BFy7jkdyAtpyKqGynGOY-_A7PvqgY5cfczCptZ3nrLvwgS8YJBrB3qGMa5_StPV--7qRAbXqXmGyMHMWon0LJ6gQ-8o1A4tWkRtZBa8XuR3TcRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c553f9c184.mp4?token=tjoXfjzoi0EYSCuHjFVb7oZVW0zN43iPL8hVEJ3QgKLUTFa7KXEraGRS146HeG7JwfhWCZachlhKPiel9AT_wEhK33MeC7rhgZ9Ieqh2Y9yEGWH3tNRfCoFd1zrecSc_F-7IPA-2PwkhhD2O0X54-lxfpsIyd5DDnI_E9d4fH0MsOHAzuUo0V0Oojdr8w3HM68qdAfP4XdHn29szHjFFfA06QtavVl9JzZ3RGJ8BFy7jkdyAtpyKqGynGOY-_A7PvqgY5cfczCptZ3nrLvwgS8YJBrB3qGMa5_StPV--7qRAbXqXmGyMHMWon0LJ6gQ-8o1A4tWkRtZBa8XuR3TcRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: همانطور که پای رهبر شهیدمان ایستادیم، پای رهبر جدیدمان هم خواهیم ایستاد
مشاور و دستیار رهبر انقلاب:
🔹
امروز به نیابت از حضرت آقا در پیاده‌روی جاماندگان اربعین حاضر شدم. به رهبر شهیدمان می‌گویم همانطور که با تمام وجود پای اهداف شما ایستادیم پای رهبر جدیدمان هم خواهیم ایستاد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/678313" target="_blank">📅 11:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678312">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
روسیه: ۲ کشتی حامل سلاح به اوکراین را در اودسا هدف قرار دادیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/678312" target="_blank">📅 11:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678311">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-text">🔹
حضور دکتر فرزانه صادق وزیر راه و شهرسازی در قرارگاه مرکزی حمل‌ونقل جاده‌ای اربعین حسینی
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/678311" target="_blank">📅 11:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678310">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عارف: تمامی بدهی‌های معوق دولت در بخش کالابرگ به فروشگاه‌ها پرداخت شده است
🔹
اسرائیل در چهار روز ۱۲۵ بار حریم هوایی لبنان را نقض کرد
🔹
سرعت وزش باد در زابل به ۱۱۵ کیلومتر بر ساعت رسید.
🔹
هشت فعال دانشجویی پس از تلاش برای ورود به پایگاه هوایی آمریکا در کره جنوبی، بازداشت شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/678310" target="_blank">📅 11:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678309">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiQn34uq-Ps1G6dD_Ph4G_F4Grw0mifJPvnGuyf9uy6L-Fypoiv0jV88nXHdmp8mbLwgqTCtNOfENKzFM6j9ahqQ_BTtpQFNbfel4Wr5fTRQKxqOtfZ2DCyczZBXxkcrLvVsW_GUcmfJ3kbcGO_v_gc0NUNrOioe3sFpq3jMLTjffvSFHVGYXCy9Blsj2gZpqeauYwxzkNQKP43Ic2i_l11ZjLgIsIZ4OJBI91au1DIr2ZAzPG3JtcZii1IsbKACKiP3nl32d6yIObU3R8jXiOvPT_dt6eM1RbHJJDQlkdxs42bDMf9xi0jRXfRUBHtLzxTvhAUn4EycEBlXoV8YKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترفند ساده برای تهیه مرغ سوخاری؛ نتیجه‌ای ترد و خوش‌طعم
🔹
ترکیب یک قاشق آرد سفید با ادویه مرغ، آویشن، پودر سیر، پودر پیاز، پودر انبه، نمک، فلفل و شیر تا غلظت ماست، سپس خواباندن چندساعته فیله‌ها در این مواد و در پایان آغشته کردن به آرد سوخاری، روشی ساده است که مرغی ترد، آبدار و بسیار خوش‌طعم به شما می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/678309" target="_blank">📅 11:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678303">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
وزیر اقتصاد:
دشمنان آرزوی زمین زدن اقتصاد ایران را به گور خواهند برد/ مردم نگران نباشند؛ در برابر هر برنامه‌ دشمنان، برنامه‌های مقابله‌ای داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/678303" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678302">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
انتقاد نعیم قاسم از مذاکرات دولت لبنان و اسرائیل  دبیرکل حزب‌الله:
🔹
مذاکرات مستقیم دستاوردی جز امتیازدهی‌های پی در پی برای لبنان به همراه نداشته است.
🔹
از حاکمیت سیاسی دعوت می‌کنم از امتیازدهی دست بردارد، با مقاومت وارد گفتگو شود و وضعیت داخلی را ترمیم کند.…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/678302" target="_blank">📅 11:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678301">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
حماس: به مرحله دوم آتش‌بس متعهدیم/منتظر پاسخ نماینده شورای صلح غزه و میانجی‌ها می‌مانیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/678301" target="_blank">📅 11:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678300">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/681e008124.mp4?token=H-DdQADs2yx_ehil4Foj6VdRyVvoY-gntBsnSvPJNu63zupi2TCPkVYa37AWwR3PUfukQnzwSRq4fiDDH1ljxWhD0pl3FW86FCtXUZGJZyTkBwPGtXxcRtOf5AqT6n1E0kav_abT9jYGNLfQQKXHFGCCdrVlDFEBoVVP5H2lvrhDNZ6xKa2qbVE1NqVby3BzKyQ7ExATPp8V98MMWdyksHTSsmNBnw4bc-iCHQD8J6HLta34vaXyKilH5O-LYtuiftxghZySkhetzcfRBL8EG9JuW-i6yQS_MBt-BYpf0tNd9_eGc6PbgujS0Gy8QX2xDDWAgI2xwOHKcrndat5-MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/681e008124.mp4?token=H-DdQADs2yx_ehil4Foj6VdRyVvoY-gntBsnSvPJNu63zupi2TCPkVYa37AWwR3PUfukQnzwSRq4fiDDH1ljxWhD0pl3FW86FCtXUZGJZyTkBwPGtXxcRtOf5AqT6n1E0kav_abT9jYGNLfQQKXHFGCCdrVlDFEBoVVP5H2lvrhDNZ6xKa2qbVE1NqVby3BzKyQ7ExATPp8V98MMWdyksHTSsmNBnw4bc-iCHQD8J6HLta34vaXyKilH5O-LYtuiftxghZySkhetzcfRBL8EG9JuW-i6yQS_MBt-BYpf0tNd9_eGc6PbgujS0Gy8QX2xDDWAgI2xwOHKcrndat5-MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسن عباسی: زیر جزایر و سواحل تونل‌های متعددی با امکانات متروسازی شهرداری تهران ساخته شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/678300" target="_blank">📅 11:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678299">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTMJc3P_RGKdCtYhtr950tVNkd8ICna88GOoTeANnJQLkA2brLn4BRc3UV5VX0F95ZNa0oZFTzkODJtxD1ujpkKts-aYDQX1aLoeJtdlSkyub3Iy7p4ft8B5Ssv_RwGVVkzLnM982OUfPXnCnIWhMI5ATKCecd9o1dU0vrjy03HCV8vXIG0ZUhQWvh0AplXNFFrJcbQNznyRjrkyk28tqRFj2BAcwFA0IBQ955doW89jtYpgSPzFIYOz4RKo0aB81ogI4CZgxJ3swnwE5v2Hr_Digj0LAQTLB6mWGMcz4A3ma2zVmAVMpnH7nZ3df79cRovjNbAFW4qXWryjXGfoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر در مدارس؛ «ناس» میان دانش‌آموزان دست به دست می‌شود
رئیس اداره بهزیستی کاشمر:
🔹
مصرف «ناس» در میان برخی دانش‌آموزان رو به افزایش است و به‌دلیل جرم نبودن فروش آن، این ماده به‌راحتی در برخی فروشگاه‌ها عرضه می‌شود و کودکان به آن دسترسی دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/678299" target="_blank">📅 11:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678298">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBdp3zp-dGIMVPdLaUIp0iHwtHuKN2xf7yyMUBCEUT9IYZWydNPDdq_-M_Uf9JOs-lbKNxYVK4HRgsMKJiCWbGWvs42_FcNpemRy6IeN_Hs_ZXEE7ZnjwYFUEwDPRA7DMjw7sycEgPtTI1koDLolQOHKJic0fN9dCRT477USJHEwdBSUVqOH_PnWzDD_JVrLlPinmgk2aXEM-LvKD3nbsDCuU3AVkmFb99gxlDNkDokws4umc9zVfg9lBbINdktPJxqmODDlvsNIad1dcC6e-9goF-UVeBiOAtPH5bIMN1AQu5WOD01UjnyvtZL8X0v7CYVm_xAv6sRLlX59qyswhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمار مجروحان آمریکایی در جنگ با ایران به ۶۵۳ تن رسید
🔹
شمار مجروحان ارتش آمریکا در جریان جنگ با ایران به ۶۵۳ نفر رسیده که از این میان، ۶۴ نفر از افسران ارشد بوده‌اند.
🔹
در میان مجروحان، ۶۴ نفر از نیروی دریایی، ۵۱ نفر از نیروی هوایی و ۱۹ نفر از تفنگداران دریایی (مارینز) هستند.
@amarfact</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/678298" target="_blank">📅 11:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678297">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIWv9QzM6_Sj6XibmK2lFkYzZqHWbCgx-ZKdTgM-cgA1sHumqtwhaW6nHnyV1MZULDS4YPRM1S5-XQ4VH0c7fasB9QKkBttOn0QATN2n1ldbfdTGAs1H3J5IsMOzloPBcpC7o4r9acszF6Hhn4eFfNB42e9cSr_1-uu8dv6I68jmsUScMBvDsJufsyNENIEIa-Gu48-kjmRTxzpVqrCjg1TVIM4Gmhn6yVt8_PKx7SBrS0enjgJqvqfOn38JGt6rNiNEjPA_PBcPauUsd4eDVeY8vbE7AmVVFrbcf6Wjax7s_Kgv371KiP5xamSYPaZBBwmVfupNAnfhVabP9yeVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اهدای ۱۴۰ میلیارد تومان دارایی یک خیر به آموزش و پرورش در عجب‌شیر
🔹
یک خیر اهل شهرستان عجب‌شیر در استان آذربایجان شرقی، تمام دارایی خود به ارزش حدود ۱۴۰ میلیارد تومان را به آموزش و پرورش اهدا کرد.
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/678297" target="_blank">📅 11:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678296">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
انتقاد نعیم قاسم از مذاکرات دولت لبنان و اسرائیل  دبیرکل حزب‌الله:
🔹
مذاکرات مستقیم دستاوردی جز امتیازدهی‌های پی در پی برای لبنان به همراه نداشته است.
🔹
از حاکمیت سیاسی دعوت می‌کنم از امتیازدهی دست بردارد، با مقاومت وارد گفتگو شود و وضعیت داخلی را ترمیم کند.…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/678296" target="_blank">📅 11:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678295">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: توافق ایران و آمریکا، اسرائیل را مهار کرد  دبیرکل حزب‌الله لبنان:
🔹
هدف اسرائیل از حملات سال ۲۰۲۴، نابودی کامل مقاومت بود، اما به این هدف نرسید.
🔹
توقف حملات، نتیجه تفاهم ایران و آمریکا و شرط تهران برای پایان تجاوزات بود.
🔹
اسرائیل به دلیل بازدارندگی…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/678295" target="_blank">📅 11:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678294">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/culE-DycCRa0z_m450N3Q8IrFwgml_PMrqZaD_5aOAcvoM4hudaEVOyWWUZM5t6x5naHi6COmDN15NSCDbb5OBVmplrzDP4asSYFXc01-RKkXxrkTq4BxKSjo5bLSSH0OZhpoTxmRSlCC90K2cMPD7hYpVhXZj95GbDhAaty9_QOxml2OzB5_oNEg-UkMBqI5d2SnqLugbAFNQdUMawYpJD07bNb44QqBex5bzPvcLN6i9JgcVzBilpEATLMrSSckDwdGmoOpa9RpqCTGzFb_4a-RRhSrKoRE3t3vQu_mMjAf1kpKeD17IpqROp6KtjA1mou7CZq0dzU4bm57o5lHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیخ نعیم قاسم: توافق ایران و آمریکا، اسرائیل را مهار کرد
دبیرکل حزب‌الله لبنان:
🔹
هدف اسرائیل از حملات سال ۲۰۲۴، نابودی کامل مقاومت بود، اما به این هدف نرسید.
🔹
توقف حملات، نتیجه تفاهم ایران و آمریکا و شرط تهران برای پایان تجاوزات بود.
🔹
اسرائیل به دلیل بازدارندگی ایجادشده، جرأت حمله به ایران را ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/678294" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678291">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
گزارش ویدئویی از حضور کاروان ورزشکاران و چهره‌های ورزشی ایران در کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/678291" target="_blank">📅 10:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678289">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e470779b.mp4?token=G1dxcS5zuco5M21KkIdbqC-6nIC4gQm79-VBx4EIFOg9F3LSZjuuw2QAv_ofF7BaEIq5OoSQUPPfEhf7WbKsWwSpo6WXzbxrLNC9AJPJ1S_hlWtddBVCXcs5qEsFetvYUcAPF1IVRIXS147lnevyXMWd7GdYIPLK-XhqQf1fAmtHAeJP4HG3xDNriygLc-lZCqUqbaxVKt73g5L4QuGW5pCyEBitIKpG-2JBtHCrDpKQecL74OxD7zwsYpZaWC5ca-QsKBMO25f_6ueWRuyIFU6xAgM_RhDY8_b1NmuiqcqIZA7MtxvaLJVkwifVLSEtLPzJAHDQcWeKNr9QI1t0wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e470779b.mp4?token=G1dxcS5zuco5M21KkIdbqC-6nIC4gQm79-VBx4EIFOg9F3LSZjuuw2QAv_ofF7BaEIq5OoSQUPPfEhf7WbKsWwSpo6WXzbxrLNC9AJPJ1S_hlWtddBVCXcs5qEsFetvYUcAPF1IVRIXS147lnevyXMWd7GdYIPLK-XhqQf1fAmtHAeJP4HG3xDNriygLc-lZCqUqbaxVKt73g5L4QuGW5pCyEBitIKpG-2JBtHCrDpKQecL74OxD7zwsYpZaWC5ca-QsKBMO25f_6ueWRuyIFU6xAgM_RhDY8_b1NmuiqcqIZA7MtxvaLJVkwifVLSEtLPzJAHDQcWeKNr9QI1t0wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برپایی موکب‌ شب اربعین در مسجد امام مهدی (عج) تورنتو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/678289" target="_blank">📅 10:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678281">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0236a5e13.mp4?token=t7PVUdB0sz1NBFh0vOVfCGkX_MAT2jd6Jv9-lYSA1Xrlh0C1H8NhI_hDb9998wqjc6P2plgX__gubySSlWGIVOVP81XznMRD8-JknjU9MZeI1IK9QIlbmjHToZeGd3t0RE3rbrHmbZbc2PiGQDH7uTFFfmAPOCdiSW1s4GdRVClE3sb5sC3w_bNVa6zgfCSpJm0NqejLn-SLQW0sOkEsfvYp5RpY9g_3LMuQbOuB2UPsCtvNaFcItylKr3cN00YS6_UsDy-wXHxQi3iJvbaqCPlBQO-78YFKLMtP9WGeBdExJ6hN8-2n-SWiLwfSIV9szTn0QP6yaMvK3ut-1eFUrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0236a5e13.mp4?token=t7PVUdB0sz1NBFh0vOVfCGkX_MAT2jd6Jv9-lYSA1Xrlh0C1H8NhI_hDb9998wqjc6P2plgX__gubySSlWGIVOVP81XznMRD8-JknjU9MZeI1IK9QIlbmjHToZeGd3t0RE3rbrHmbZbc2PiGQDH7uTFFfmAPOCdiSW1s4GdRVClE3sb5sC3w_bNVa6zgfCSpJm0NqejLn-SLQW0sOkEsfvYp5RpY9g_3LMuQbOuB2UPsCtvNaFcItylKr3cN00YS6_UsDy-wXHxQi3iJvbaqCPlBQO-78YFKLMtP9WGeBdExJ6hN8-2n-SWiLwfSIV9szTn0QP6yaMvK3ut-1eFUrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه حجم آب پشت سد کرج در مرداد سال گذشته و امسال
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/678281" target="_blank">📅 10:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678280">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffmLcRFkaiF82H4TI02SCGfjg6a63gsYQfll0_WEpouBWsppJYMR2ThmtLDZZ3ak45puLvnc73OLKt9FIXbgzrJJYfBF4GZPL4YZHbULd9HgIFojauzHGrEE-Pr1yT074Ib7FB5MSL8s7A_mhGEfME-_l0ERp6wCrZr1rYcr9HelIULaQBwQIi4WUXJ5dBRDlBNnzjMp56y5qx3T7zF2EGF7LouFsKGgykPdNmcqm8HljDqcnx2ODeK6kRcRckK2P-Hi3uLPBI_xde87X7WPgdkzwcvhnY67rJ9xW6bGxYxIoqRyImloSOjkdix4lbDYdsWDJ6Spg3oKLUhnZfuRKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه زرنگ باشی با یک تیر دو نشون میزنی
😊
هم ایرپاد هم پاوربانک
😍
🔊
ایرپاد بلوتوثی Newest M10 V5.3 ORIG
🎧
✅
قیمت اصلی: 1299 تومان
با تخفیف ویژه : 999 تومان
🚨
🏠
پرداخت درب منزل
📦
ضمانت تعویض سه روزه کالا
🚀
عجله کن! لینک خرید اینجاست
👇
khabarfouritel.affdn.com/lead/45757
➖
➖
➖
➖
➖
➖
➖
➖
➖
5000 محصول تخفیفی دیگر
👇
khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/678280" target="_blank">📅 10:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678269">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWhQunVe3JygFCNqp7vSWCV6qIX13XW6QWkNhq6uxoBUH38Cdv0wNuW3VgwKs4y4-zQa4tBQBiJPBrxua69ctt2stYezn45Zx1IfTnaxdlevhEqUeEpXcDlU4grSJUmR139Ch5EDSXfqEAqm2bcTheNLRamRFLvqy9FJMismKuyFZNwJh0m6n_4rflnlkXfDhXED3ItKO6jjd_7Kh36hWRA9mCVQGm69lvlpvMT_ZznEbZx0aMSfXan8xiTThg5K50wXhLxqe-pdgRFP74Nm9WMFElIGs2R2cyMUQAGYjZeTPKd8HWyH61OD2RfdaUyL6Rw5i8dlDwXFjuphODkXsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/erVnhBV1veTAP1xZeAgOj1nQNN7VXNKeOdi1osZhW3Xbq5DVpRqMKkUYHVbaaYyAKF3zII14bq4TbfGj1yfjMxx4sQ8tEYp9YpOx7HgQvsk3zqy9S_rmHR8XakamUmmUUzyAtY5rky6cakvHJDpEZuNHgQuG9Kz0pZRkd87gfzVBN04eE8GxjTQGCTASuRATIv2W-1AiOGwf_ve9u_WyAlod8zQPGxCu5NuM8pMtYDlpPyEXXclPpm-tNNkgpiE5IDszeO6cDNpbpLucMHQPloeo6HczexDrTL6ipZJWrMlypgcRLIoJJ7bnzK76M8JQdnygTcH_Nzo5aCNx8OF3wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ge7MAaKFT6cewOuvz7zPB5aFh0HlD5HuEJ39iaWphvQd_8hhY6GvlkrVILggq821KYV6Lil8CsesIjyHFBtF9ei2vSJWVB5HQbySwCSLtw_vJgB0VBvqRN0iYHuzgVfdkoSreroHj6TkjjTh_FcfwmGt_JtlRONEgEL7tHf3v8X3-b1s0eXHrFv-3T8B7EwiEr9432bAjq6lK-P0cTtV0wQ3K-PGxlgWdFHLRjjfinosZfL7I2QJIO_PZb7MrAcg6z-YjYbzgNXZs3X7t4GPNE59EZjYbpq4yZPv5271A-EhDIajxa9Ex56g1UkG8v18DrUfSCM_tJH6MeBvbJ8hYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aXSPtvfNWQAVnE3wc_uubH1OHYYrpFacEGeWgC-LEB8QYneQ8kUh6WCFHO0N5b3T2OM-1N8MdwEPbqQc6_aGGVlTgNZzML4BaMt4GSEnipxwLrvamGt1YTPE7uDFeoGfmooGtiP_0W3N4pj90e7nI3Coo3cRAJ0c3sfOdF_D0xSEShOqDouzarNXY1HhfIq_S_ZcpaRXzYBpRtKwBSJwc174gG9LwkCrG5TYg6oHWW3kBMBZyEJMS6nJp6tqqJ_ZmCOts03WXC-IrsigluvqqcZXSpzG8ylZkrnDKJ9qPrDFUAjAxy54JyIXw5iRpULAoJSUEh-o7NJO8w_Ts-BCpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVDAe-a0UGjHeXe3Elh1vsUybFi2MGvcWQyJ4b0NgvD5cfQdpIiF3bsVoK8jQgVaYUsvZgCs2-gK2PCljoM_bEnYHuOQwTNb4EjkbEh8y6KrL8S_1cY9cl83NS0M68OgX07DKSnZTyga6tYDnjNOjZPWtwH86hhFNyuJCibZxiVH1HzjdiE_91tAFAhWfBCus7S-GPvcj1lLHqiFyOMmk4zi_iYZMfmQzljoOjyki4wFI2gLfrbc3fsD9SQtYxiNmcO69IBBd17OzzCKc04vyw-wPx9EYXTTv6FzJpPMB2lxEnZ49aCdmt349TEHrr3NvuufYVmGadyYwnBz2rQuOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVwm_d3wP3WnE4iifESjbB_dMeYNze-sUIcAVYnimYrEPrBXvaKFHlA1p7YMDPh8l5Ak7bxd-B8fPsSYN7ukcAy3xfRXa1Cl1g5KaV9D8CdswGA0Er1a0PmExPNOXfHyxYjW9QJnaVtjFpd8Sampbszy8dKwDAJEAWpV5pERfjcXYGtsGON2DCSlunGc-i6qa3AdE9Jg9D1uuSSaX2ou7YzuYU2ncwQpPTzaL1QzgAeZ_Yds9cpGVA6urtWM1LykABJYMXPAubEc-v_Yeq3e9ZLlTx9su8jMfHT8NHUZ8mwE7lwoKc7mtBbxIuhA6yjMda-ljXnIeL_jwKsbym2CVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDEV_wFqaloNMEx6l3pFWBrVJgd_yDhspI7JW-Fyq7wZ56FKMaa2GEWIVJAl5IZnmJNuEYNWvYH3rE6cQ432BX0HyMVhcR8gW-mO0AkUDcH4VTQIAx_4xNdj6Ikct_fYqO9GC8C3sS6MhsRN-FYV3Lek3UfCCghzM0od-a4Dw32C29rVRx3fIl6_IoImupNnQd1MxQc4MMMTgwBMw8LGqd3pACzdokw1QKAl02eVjwWAN3u22bYHLNA3phk2eDreei83KEr1oFM_WxQj8WIRgiDbdvsPiFjdNAe9OzgOq-hYpZ2r1TQRDaCI0wahAXT3eXs0fKoTR5fSRjnu1Lz5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J8upUKVKmVIH02Pwfe0IAXWLeeuyfdoI2gIaAob0MjHovZXI66ElGM2PaRUApleqCkgubalJ3GOwpPKBE0QNZcip06Ksfe3VPEcTCJV_CLh5QEchjJZiUeRXpzRyzL-JnnxIscDexf7nY-oT1bRa0W1bWj5m9oeDWDQKJrM29obQOCx4C_He7VxeHqXXHs0DCZypc2YXQw7uIYd_4yeFIyLktzQlnixon7C-g9txl3tABGsYhsizfIKsjJdCZeiFSVGYMzgIKfXeVdAXNGJsQ-2aHY-M45smJMuc0I6IebJp0METM0ZYJQacx68FE1q__0HV7pycqDxgVaQTtnuYjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0l63PtE-aGaifaAYe5n8SydCBgtShyzlfIo4m1KcSzMSVUVb5WiSSdwsBNQfOzpQJSqgATTzHYQizDLA7AtxrFxbZ2LtLgcRrb63HaifS2sVddPlsHiw7nPRhXEoPDXQQlhE4liNnN5h8P-YGf2niwF6NRPeAYrDiCel8bPVnPsDw6ODJA-_F2Fx0rWwS_gqiXZ3VKXlRlESFd9MOl7eviYNxrLDdvK7OLj5qTLzKDaOJDCaxVAHKzJNIgV-tSWOb4MzN0_kjx4Wvm1pE3hgIvyaStDj-gQCd6sn4sJhwli4s7SbnvSL7PsLpJ4bneYdpvfrgZe_5vNWxwZnHAs3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xo4hyyYKrUPOSC4aGc7Xy4hLt3BbmyT3Ng3LyYDsOkRNGq2DI0v-KgPiAjxnQ1EL9D8nt1oWa5FEK769JEm77wCbWaDh03aeQJW5516uw0JH-NfWXgqOjKLPLYlfEE75cIdTneMAiy6p0RWb646zvmyzSgdHDc_KUB5Ar3i4TKBVTiO2iQs3XY-QAwmSqkPbb9L4AKj5hLhSiNWoKqHSLrv9rNVBmNO6Ymb4ZN75YjuC_lOCsMRonwQqOAJJk-AOKkmUd_f72IX-rh8PhfvBT9a2mU-BUEtFMTjo1IHRHBx_RLWnko9Z1Bt1EPl41n77fsdIjf1svcWDNjYUnsW4YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با جوش‌شیرین و سرکه معجزه کن؛ این ترفندها را از دست نده!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/678269" target="_blank">📅 09:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678267">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1e9ea989.mp4?token=KkMkQWWfE0cMYDDs8H7JXxO5sILmcyB2iraPtbydXyY7ao7Fs_xDTneJZ_TMPk_NnqbDtlQEeXJXTOjIfJ-Y9jf9mQnikMzyKyy1XAaXbkxIYYSNCHQ1OaTq1WpCTtEWWUGPfztvlVzFOIauOrkWATuDfycT3v0EWrlwH4UEoeNBihj3c2AvsCUcXmdgx2Y5HeAUVLY1x0gIkv6WeRRWtuT99JU6PqO9OjmLz6vo8FNURzZ-UIvYDhtTod_cBhwnpkkNudwMaBGfy2UCIXalPbvd2kCUyjgkmZCYmlPgoPH8PlnuQXl9fkoCXHvPP6blfTjmJM9Xim_Yp3N2qTHRxiNOeai0D2fS7jTQ-t7_lqbVODKLGKwtI1L4THVLnPS2jcmA4WTPJRmnXH_rLmB0Mj2U_s2dnL4WnrmyxuHhLX1a4KSaukMiLPEBXIys652YfNtPShZ761To4nvOQZ8UTtGZeTam9o4Sh_eVfZ2ONqXmlYv3QAcWtuPsGf8yHKp-0uQo42-CByw3ivBMEIVAUgIGcmuanlWL4mhZKNkFj22soO8nlscHSAfm4t9aGK1lWbaypC1gLxgF6sTEf8e-wIFK3w3C3NW2AT7zLgpSUAJipmzIElyDooBsBo-Urs5JMdsTQC_uLyFA4cunNOd-fO5t8IYldiFJqt55-lQSi4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1e9ea989.mp4?token=KkMkQWWfE0cMYDDs8H7JXxO5sILmcyB2iraPtbydXyY7ao7Fs_xDTneJZ_TMPk_NnqbDtlQEeXJXTOjIfJ-Y9jf9mQnikMzyKyy1XAaXbkxIYYSNCHQ1OaTq1WpCTtEWWUGPfztvlVzFOIauOrkWATuDfycT3v0EWrlwH4UEoeNBihj3c2AvsCUcXmdgx2Y5HeAUVLY1x0gIkv6WeRRWtuT99JU6PqO9OjmLz6vo8FNURzZ-UIvYDhtTod_cBhwnpkkNudwMaBGfy2UCIXalPbvd2kCUyjgkmZCYmlPgoPH8PlnuQXl9fkoCXHvPP6blfTjmJM9Xim_Yp3N2qTHRxiNOeai0D2fS7jTQ-t7_lqbVODKLGKwtI1L4THVLnPS2jcmA4WTPJRmnXH_rLmB0Mj2U_s2dnL4WnrmyxuHhLX1a4KSaukMiLPEBXIys652YfNtPShZ761To4nvOQZ8UTtGZeTam9o4Sh_eVfZ2ONqXmlYv3QAcWtuPsGf8yHKp-0uQo42-CByw3ivBMEIVAUgIGcmuanlWL4mhZKNkFj22soO8nlscHSAfm4t9aGK1lWbaypC1gLxgF6sTEf8e-wIFK3w3C3NW2AT7zLgpSUAJipmzIElyDooBsBo-Urs5JMdsTQC_uLyFA4cunNOd-fO5t8IYldiFJqt55-lQSi4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: استعفا نخواهم داد و خواهم ایستاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/678267" target="_blank">📅 09:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678266">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtodMYEH92orJaclrieSoxoPCnAL0JwhJCMXSMc14X871htPCzw8tNgD39uGSUGE4fdCIkrO-9kHjg4076BZsEg06NmIoVIFKN0BtpgECRXR1KqBn4IxSDUqj_8g7kSctTmoLpxWHWMpE2sjHxL1-blLmvGK04JnEfGzDU6sWglKLWVvMldD1cxfdNaFNr5LW5swCE9ie1cXlphUsiRssSLoXatX_hhwuZPm8hhf0IVIX22M79hO0eN-fb1nqmf6xuT1VJ4OdE93wbzP_mnu4knSLaSEFtfz5m09p51W_qmC0AR16g3FfQsPo7RAZsOiLNIGwcP56btq4grdHHSUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرگ عجیب و باورنکردنی مربی کراسفیت ایران
🔹
مریم سبزه‌کار، مربی کراسفیت و نایب‌رئیس بانوان کراسفیت تهران، هنگام کوهنوردی در ارتفاعات لواسان بر اثر مارگزیدگی جان باخت.
🔹
او که به‌تنهایی راهی کوه شده بود، پس از حادثه حدود دو روز مفقود بود تا اینکه نیروهای امدادی پیکر او را پیدا کردند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/678266" target="_blank">📅 09:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678265">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6d0e66e3.mp4?token=DKQozpppBZpgFKp9ND88u3IjOx61QL-99pmxAYVjPh7Dtws5f5JFjHrBP4rJ5auo9EfCaQTdJEsq2PHkX2-E6uSmqDqjp1NE3ooFLlvloWn9u20PPj1PaJ-x9uQKqUhmzimuDMhg4296-0SUrXfUp2rgwnDNfcgkmbk91DsKmacWhO9A-jRmDx0mVOm8clSc1ALDStMx1XDKS4iwb-Z4fP2Vt42cbhRtvKKwmkwF_Za_pMRbF69pgIImBZNCmarwb4dPCf4DaScNOSDpX4xZQwvtcIEujgFnoGSn1Vb--c1S4nqz6xmLdE0IdBJd1h-08ILVI3wktFTKyMTQdtsXgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6d0e66e3.mp4?token=DKQozpppBZpgFKp9ND88u3IjOx61QL-99pmxAYVjPh7Dtws5f5JFjHrBP4rJ5auo9EfCaQTdJEsq2PHkX2-E6uSmqDqjp1NE3ooFLlvloWn9u20PPj1PaJ-x9uQKqUhmzimuDMhg4296-0SUrXfUp2rgwnDNfcgkmbk91DsKmacWhO9A-jRmDx0mVOm8clSc1ALDStMx1XDKS4iwb-Z4fP2Vt42cbhRtvKKwmkwF_Za_pMRbF69pgIImBZNCmarwb4dPCf4DaScNOSDpX4xZQwvtcIEujgFnoGSn1Vb--c1S4nqz6xmLdE0IdBJd1h-08ILVI3wktFTKyMTQdtsXgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله یک طوطی عصبانی به یک بازیکن فوتبال در لیگ جوانان برزیل
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/678265" target="_blank">📅 09:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678263">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7db3633281.mp4?token=FVH894COvsRlNsGwuUhjZ9xVFr2xvfI9W5jZdr2AApHjfTTHRntBn6rQRjdlYXt5JJWahTWL1eKN5Ac9gYjm7sOp6-9_FevhUDnT4GE84uOAj0xT9C99I7FcBAZHT_faT3wFUC-H_nwHKIObfdt-ZbQ-IwFf2x_616IBp_B9XdDYck7b7eR-5B7sdHtzv_kz254cH61bpCOI_ofjCx6KUinnvVHd8vnVBlEmShy7NRvN13MGq2lMMfXwzx4bmPaBDuaQS3yuYoG3TH8ZySFXoAg3wNJoHgdlgXomrI9OS5ucHAI3VF-U471kUbSLc570Ee3a5cEWWp2S1K0XAl2Fvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7db3633281.mp4?token=FVH894COvsRlNsGwuUhjZ9xVFr2xvfI9W5jZdr2AApHjfTTHRntBn6rQRjdlYXt5JJWahTWL1eKN5Ac9gYjm7sOp6-9_FevhUDnT4GE84uOAj0xT9C99I7FcBAZHT_faT3wFUC-H_nwHKIObfdt-ZbQ-IwFf2x_616IBp_B9XdDYck7b7eR-5B7sdHtzv_kz254cH61bpCOI_ofjCx6KUinnvVHd8vnVBlEmShy7NRvN13MGq2lMMfXwzx4bmPaBDuaQS3yuYoG3TH8ZySFXoAg3wNJoHgdlgXomrI9OS5ucHAI3VF-U471kUbSLc570Ee3a5cEWWp2S1K0XAl2Fvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا اباعبدالله
اِنّی سِلْمٌ لِمَنْ سالَمَکُمْ
وَ حَرْبٌ لِمَنْ حارَبَکُمْ اِلی یَوْمِ الْقِیامَةِ‌...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/678263" target="_blank">📅 09:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678255">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A7Sybg_XEknq_08Y9CsPfOqBbpgKTnzSVQEer2chMpKwhgpK2S9DIj_q_XhlX8cXpry28DaB08ggzWeZbFy3FNSPeRrb9OkNPhmPa6DqqG-bcQIm8lpc_YhJKnkCDnHJ1IVFbII0KStHL-7kHimu2ZKRf71f4zrEpEB5l1Xml1k2LYWU5AcShV8-y9-wWoDKsQCA0-_rXeTgzRyzt7h13bLIcLoDjD0g8XeXv2H1PKWbsz_tzoVOAike1AB03P4D20R6c4YtYp4cbiX4WsAeWgpH8pQpFzDgBgkGEtGB7BlHOrdH_FPxl7RORrn6pVc_aJo3dfJsvpndes7HSz2R9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GS8Mxd5pSqz7UBxunm2bTwk_x4DRVnpBeOzRw2t0tgia9ER4vUY2ZnOtfun_hsrlP-rhDVhcBNZPg9SNzt3qhc--5O08Eco-65wbit0wGJ13F986OgCsb05VAJOtRhReyPBWJHlzNQS3OoR2vfa9UiXMcmIVrBNhGNysqZe99DeAnTaEDaRjZ-N6I5hC2p9w_-qyJU1lTQVR6_IE-6hNN8poMRJEcyHS8BA2RyExvHJpXuGfuFC-90syvQwybMmcSWPMV1tE7RYu7J85KpJbNYMsUC0djMcawjBRDamTz12ILrUzJSFT5yPzLVgPZ6oqFJrIjzEBpgXKygQMjyUxrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طرز تهیه ذرت مکزیکی خیابونی خوشمزه
😕
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/678255" target="_blank">📅 08:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678252">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
بانک ملی: مغایرت‌ باقیمانده حساب‌های مشتریان تا ۱۷ مرداد برطرف می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/678252" target="_blank">📅 08:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678250">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed46a57cc.mp4?token=U4pxDJXk6_7XURj5IU2yYWXv-CG5I9iT38qMcblc8gNNRLvLFNLF_MQZO9pxdT5_hcjalZwA4NgX_ao38uUfB_biGdvu-g2oqC-C0m-MTFlc5KZUjy8Dg75QX-ZzHyN2GO2iS7-3Y6nXU63sSb8uz8SxohFNgo_GIOYgv7ZqrrF71fPOnfVYtEcteZZ-LZNlaJ3Toky1d7OhA_zh6TbMA4A7fH54qZFECVTBarH8rYHG9zYDJ3Jf3x_Zc0Y52S7QCt1UZarnLaSjs8TkU8RD4Pe2AaywCL5Xj7JEKDY4YwFLXnPOwdOz3oTIzXcR5azXjSlX3Yh4-rh49wONpRQ_xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed46a57cc.mp4?token=U4pxDJXk6_7XURj5IU2yYWXv-CG5I9iT38qMcblc8gNNRLvLFNLF_MQZO9pxdT5_hcjalZwA4NgX_ao38uUfB_biGdvu-g2oqC-C0m-MTFlc5KZUjy8Dg75QX-ZzHyN2GO2iS7-3Y6nXU63sSb8uz8SxohFNgo_GIOYgv7ZqrrF71fPOnfVYtEcteZZ-LZNlaJ3Toky1d7OhA_zh6TbMA4A7fH54qZFECVTBarH8rYHG9zYDJ3Jf3x_Zc0Y52S7QCt1UZarnLaSjs8TkU8RD4Pe2AaywCL5Xj7JEKDY4YwFLXnPOwdOz3oTIzXcR5azXjSlX3Yh4-rh49wONpRQ_xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از سیلاب در شهرستان راز خراسان شمالی که موجب قطع کامل دسترسی مسیر ورودی و خسارت به زیرساخت‌ها شده است
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/678250" target="_blank">📅 08:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678248">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoOj-4gaiCeTOnPUIl3MOUuJHK99Imx34mqKSz_a-dgTqbIUlnwlcrQPcWFdNa-chBmRSuomhpHTNEsJN8Z1FoQ_JUDjlDjT8csDAbev11OGZSq5yvJtI-Kj-I1E16kqZrwjFjNsT5VMVGkxqv0HOOdl2GtNe1rj4eL7bDr9tmNLHCLx5FsxHGNGxZ4NR4-aj_jLo0e7LCIT7kA7HWlnAyjKhB1oUib1ZMLfDJYpxR27INRTnxgBjlXhN6VhJYnAtj2fxsnuIeCJXCOh6YpjPuZIfudCPAypw1EhqDrrty4MBlisJmXwSeBhUWCKjR6bPBnjl_rnQUAFggx_SP_QSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لری جانسون تحلیلگر آمریکایی: راننده و محافظان شخصی نیکولاس مادورو در ازای پاداش میلیون دلاری با ایالات متحده آمریکا همکاری کردن اما بعد از پایان عملیات دستگیری مادورو، دونالد ترامپ از دادن پاداش نقدی به آنها خودداری کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/678248" target="_blank">📅 08:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای ماسک؛ از بازگرداندن بینایی تا دید فراانسانی
ایلان ماسک:
🔹
نورالینک طی ۶ تا ۱۲ ماه آینده تراشۀ بازگرداندن بینایی را روی انسان آزمایش می‌کند؛ تراشه‌ای که تصاویر را مستقیماً به مغز می‌فرستد و به گفته او حتی می‌تواند به نابینایان مادرزادی کمک کند.
🔹
همچنین امکان «دید فراانسانی» مانند مشاهده نور مادون‌قرمز و فرابنفش وجود دارد.
🔹
تاکنون هیچ شواهد بالینی معتبری برای تحقق این قابلیت وجود ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/678243" target="_blank">📅 07:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678241">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d0e881a9f.mp4?token=LqaLCY1nkhAKtANT_82L1N2TNFoPpLOo29gfoNRwu6E5q1HuqxyDnD1OdpHcwObf3GPH_5zxBR7ArA-LSXGx1gOCowNeZwUhCJ8rfOi5tPgHeTaby4Ncp3RM1B5IE7vlPsLNAyStQe6kd_DUUEvfnjTqAZcgEb1eiNA9zhAjlXnGwv7NjZCqQ1Aa17V-q2Tp8CTIpUJ8XOPBJyH3ba378KVKvndg38dQEgIMt5pbQx9K_BS3QuRlEU_J4A1_f9JjOTvHiPM28294DnEiIsWz82bhY-pOqz4guKaXhA-8RoadPDOgc4T5-9YF2UkPJ8mSgJzY9UQwHZng1yibSVMMTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d0e881a9f.mp4?token=LqaLCY1nkhAKtANT_82L1N2TNFoPpLOo29gfoNRwu6E5q1HuqxyDnD1OdpHcwObf3GPH_5zxBR7ArA-LSXGx1gOCowNeZwUhCJ8rfOi5tPgHeTaby4Ncp3RM1B5IE7vlPsLNAyStQe6kd_DUUEvfnjTqAZcgEb1eiNA9zhAjlXnGwv7NjZCqQ1Aa17V-q2Tp8CTIpUJ8XOPBJyH3ba378KVKvndg38dQEgIMt5pbQx9K_BS3QuRlEU_J4A1_f9JjOTvHiPM28294DnEiIsWz82bhY-pOqz4guKaXhA-8RoadPDOgc4T5-9YF2UkPJ8mSgJzY9UQwHZng1yibSVMMTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بین‌الحرمین در روز اربعین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/678241" target="_blank">📅 07:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678240">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jahEtPzxX_IaWcFFG-LrrUWRK3GXIP8wSxLup2Hn8RgdKfXfsdDSTPKc7PvtSmGvzau5RpYQoVyvhPCoUwE2XLeJ-R30yTi5eeF4Z8v6jys8F-7f7hoK6E0SWoY6J0i5yRyX9SO64g3NFZhIymDQsM9oUfpakjDSqK9GelaHNi97EtxcRWQ-EK4i4WHJW7N-3fgP6qQcxxknNhCRmRk8Qe-UIvPfjmoaESoPNduQ3IBmUyEMHV1NU6AB9ZW8u2dB5M9kkzSTC6FI35e04ks5Yzf2JIHGA_nmE3pW7nKwY3I49OgDedW08TatIzs-Ze9POCQ7eSs6lCreRcEHWvhuZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۱۳ مرداد ماه
۲۰ صفر ‌۱۴۴۸
۴ آگوست ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/678240" target="_blank">📅 07:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678239">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiWpodYm3NbdDIp8BVBXLVMZIlzdgSm1jx1vAXMpcEwI-pYr6w0GU2jDTrKO9sQWJIH0A1RfG-Dcrm-0uUaJwvEz0vMEFjeyJ0ZtBsaHcdFnM6sEVwTPaxc0cCO3rrBzqf7qagrPM1tQXUj8n8WQU-_Pw3LbYHGYZRUFrlwYl8wTFX1C7ZU2JBSgjXhT2DHVXtadRXIE5qqPauD47vkQohkOcaiSZ5ckMMVF4BansBR578K7lffJBoNp9N6k11qAE0k33njOrxH8w8MiAMtntbVF1DlXqRvi4MPqle2kbkeFDvkfiFzHA0eiZtTkisG-mvBvLtIl8Yw6M5np_THpow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصابت پرتابه ناشناس به یک کشتی باری در سواحل عمان
سازمان تجارت دریایی بریتانیا:
🔹
یک کشتی باری در ۲۰ مایلی شمال شرقی بندر «خصب» عمان هدف پرتابه‌ای ناشناس قرار گرفته است؛ مقامات در حال بررسی حادثه هستند و به سایر کشتی‌ها هشدار داده شده با احتیاط تردد کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/akhbarefori/678239" target="_blank">📅 03:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678238">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
رسانه‌های عربی: صدای انفجار در کویت به گوش می‌رسد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/678238" target="_blank">📅 02:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678237">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e81c4a381.mp4?token=KoTmwnEj7g-lVgEPIelqR50UMKcxKu_L3l7CusVfPB4zS8b9I5hNkpm_SFXmg2PNuWCzDKFhflUdOYDJ_lJl_Fo_tXosDIMocZQN5s785oubfT9Z_Dk7RPPt2eYQhGaljrCjNiFNEwwLXaejCv5HOZF2NIWMVgKXwj4pjW_0sGJGxA4CQ9_tkPkOsz-D7sCaX3BN3C8Xf0vg-TeZrk8OH1JHq18CVYRb8Dw69OfS43aNgGBFxXVVXweoKqOHC5XVAdsNzsemvWtgmyaRxyHNWoT5UJl_ZWKT7tdUhuMA7UpR-0dTDqBnESzgKT7KY6XE0Xj2kkCwdmxPUJPe1lKZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e81c4a381.mp4?token=KoTmwnEj7g-lVgEPIelqR50UMKcxKu_L3l7CusVfPB4zS8b9I5hNkpm_SFXmg2PNuWCzDKFhflUdOYDJ_lJl_Fo_tXosDIMocZQN5s785oubfT9Z_Dk7RPPt2eYQhGaljrCjNiFNEwwLXaejCv5HOZF2NIWMVgKXwj4pjW_0sGJGxA4CQ9_tkPkOsz-D7sCaX3BN3C8Xf0vg-TeZrk8OH1JHq18CVYRb8Dw69OfS43aNgGBFxXVVXweoKqOHC5XVAdsNzsemvWtgmyaRxyHNWoT5UJl_ZWKT7tdUhuMA7UpR-0dTDqBnESzgKT7KY6XE0Xj2kkCwdmxPUJPe1lKZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی: صدای انفجار در کویت به گوش می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/akhbarefori/678237" target="_blank">📅 02:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678235">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
تشییع پیکر بیش از ۱۰۰ فلسطینی پس از سه سال
🔹
پیکر بیش از ۱۰۰ نفر از اعضای دو خانواده فلسطینی که سه سال زیر آوار مانده بود، در منطقه الصبره غزه تشییع شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/akhbarefori/678235" target="_blank">📅 01:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678233">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35651a1e7.mp4?token=BpWAqYpp9Fg-A3OnMPHCzRNdYtjzmIQC_t7-zPapDOTkPd6q8wRrM0vAOE1no8AI-Imjl0EbmlnrMwYj-COmkIAa4ND7KYrvGw2mrUUj2Qwth-dNpv9VEv6z9uw1i2fbkYH63vgNF24jylAjy0Xzmx_wKqDE3R9lkNB19Oh9yMY-7ExyamlELHUHn5NYCt8_DPByhH4_uDV07tKtcPF1KcGWnfn3M1giaCvqy_Oy2gQrcCXNgHBwNUnrr23BQqbXDQ5Ac951pGpif7sxzXvfJu3BzxjxLQUwENG0HKUPVyZRPW0zywSCKsnPnon6mho3rwVAa2YPUMbC49H5eZMAjYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35651a1e7.mp4?token=BpWAqYpp9Fg-A3OnMPHCzRNdYtjzmIQC_t7-zPapDOTkPd6q8wRrM0vAOE1no8AI-Imjl0EbmlnrMwYj-COmkIAa4ND7KYrvGw2mrUUj2Qwth-dNpv9VEv6z9uw1i2fbkYH63vgNF24jylAjy0Xzmx_wKqDE3R9lkNB19Oh9yMY-7ExyamlELHUHn5NYCt8_DPByhH4_uDV07tKtcPF1KcGWnfn3M1giaCvqy_Oy2gQrcCXNgHBwNUnrr23BQqbXDQ5Ac951pGpif7sxzXvfJu3BzxjxLQUwENG0HKUPVyZRPW0zywSCKsnPnon6mho3rwVAa2YPUMbC49H5eZMAjYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری لفظی بن‌گویر و وکیل آنروا در جلسه دیوان عالی اسرائیل
🔹
همزمان با برگزاری جلسه دیوان عالی رژیم اسرائیل برای بررسی دادخواست‌های ارائه‌شده علیه قانون ممنوعیت فعالیت آژانس امدادرسانی و کاریابی سازمان ملل برای آوارگان فلسطینی (آنروا)، میان ایتامار بن‌گویر، وزیر افراطی امنیت داخلی رژیم صهیونیستی و وکیل این نهاد سازمان ملل درگیری لفظی شدیدی رخ داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/akhbarefori/678233" target="_blank">📅 01:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678232">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixPeWd8uLTGIGkriOZGomrQ7SfvTAqg96HHOBOkRD74aVJY4GuLv32MdPLuUXkr8co62vHmUAXoynbmTwCCH-9P4GbctNd4YWrCQ8dIxomFi-iAi0Gvep3ryFT-K2jf4P5qIgkdQ2Yqomvr0trFK-r8eIZ619PDlke4EXwANJSYyuAXnoZoVgWgnsQAt6n_cq6emSk6sGSOX4QacUqGkWdVHS8_F6eBnEb2Ju-Ik5kQR8FcWnhLKOOO55MO-uI90OOc24H09TNK_PAO9JNO9MWk0kgHJwY5EiM-R7CAzg_uX6he_YC4ZFcrX960k49OgkFAqoAGX7-hvjf9o8Mo0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویل شرایور: ایران ترامپ را در گوشه رینگ قرار داده و تنها دو گزینه تلخ برایش باقی گذاشته است
🔹
وارد جنگی شود که ایران می‌خواهد.
🔹
شکست را بپذیرد و منطقه را ترک کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/akhbarefori/678232" target="_blank">📅 00:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678231">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سرلشکر رضایی: به‌هیچ‌وجه اجازۀ بازشدن کریدور دوم را در تنگۀ هرمز نمی‌دهیم
🔹
اگر ناو و نیروی نظامی هم به تنگۀ هرمز بیاورند آن‌ها را هدف قرار می‌دهیم.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/akhbarefori/678231" target="_blank">📅 00:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678222">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I5G-NsNYzf0Qla9OngXNKfAQErBWTtR9_MRn4fIROaPrZp_b9TpbK-MBzD8PBexci96WwW0Oey305wg0Zvxd6iBPywGcAsVasUOnvgRJ5JRQbOK3R6wGGjYN8A1M92c6kVd8wTpw2qEBNJ4L_y93gDb8n0kCAzZkDtkULxiA9vkzQsLWKfoH7GGW7bgJJ_0yeYBrI14rIRXiabyyiHl__zHoh8F4-VYohh635sUC1E_g3G3UC7Z0xZiCXeEKl9ln4soWwJfBR8XLjJJxH9YKKa4rPLYwHP6Zf20aIjSKP3ac1H5ExPhsOxmPVHIAk35lU9PbR0RJWzCUkhWh0SAOOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FE-8qJAVENfhUOusg-Sc7yL4ZONEFGsx8rZeD8uqCTltfHaqS6q0woabSSlllRlgTPz0Czc3bdBS958_JXo5UAdgamKNCuTNwnCWCXwFbCpAeIdMxNxzJ-IWLKIVvuNdMI2H4uSVLVAyG0rBIcVqq16ky95OcPtRXIVaN6ReYGQ0KQaYcOClhYhHzCzC_16DE4B0lJX6rajvXSvd7Rjo914BQ6Y-_yVuyHGlCEAdnULhbGz20aZLZpyDr7xGx81Y6LJNI6DUAwAzE8YbSEM26rekhzkzECg_8PCFNnGoYDqR54yrXDwXCFiNiMHwOZdHtM9qeRRVPrH8F8BebyIvfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IANH7PBdnaYurEBPELhO7OkSG1BHrBADkYl3xqhEWCW4AHZRxZJWLGd7dgHXcLlz5WzqO9-yCAbU88Iaz173kJ8TYBsHs5vcyf9_aJrAQVBx64cDAtzHjQaMygZYeqs0peSfq8Z82QKa-JYR90feeLvdVqDePsBQZiveEPym-sRaNG8kKnGA8uRq3GXw1gqtQZ5luSV-ZAgaiBs8xNxaNvhJvD5BGzouft2UjebRHnWwB9N_JAErgRvyK3oNc0CccwAbBossQ5IntlUf8WbVO4gRhv1VqLvFqkPhln-nRkMS9Xu7dqrVITY-q7RWest7066U9uMccjVNAt0h2iwcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmLXMYoP0dNFUX4UhXk96eMaoN4qU81IBLrvGSwM25EEc1zljpQciaTuK9qlT24cU05I057eg5ST0EgNwTgGB9uc4Cq4ICR1vLTzTl-fqD1qRszv0s1uWZkPXkBwuTznB5-zUtJv5vB82Sg1BNd2zer454LWzPecSjzvvOdy5dEkGG0NKypw5jGChXIAM3nj2dnC0841zGQDk79dO7dRSFrJ2lz9tSgQMSBKF4gIizkRDijuQA7oUrPITpc4KF0NZM5_UlZCJYrsHIfYaQe_XhpePz7nnPwljCMCrfMJjec1JYjMs_wmhfTiKVfTmGQdiOBmg33Ume86HJ8JSFPHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhC2eU9yvq9jbenYm786An0-Q0pRzpMZHPgYnv-mxqmuggbD00OZ_THqmtaNWbMYQ2FGXpn_wOvMQCs7wG9zWgKoKmXgfhTNIKQeXB1RKHI0EBRuaqiqcxiLqUb3Sctlj2BqVGzFPrVS3YxJpfsSYOuaTNISHKhlytbz3riuLaKkha6WGcTpNzSwLKuVYFKbAdVm3sfqTz85PgA7zCMfA9SvyGGLBUySHsWd57XDfQmDLTvGTp1rnRhbry0rx3Ir0bmk8Qc7SR5VMor0Cyged34Zq1OA6NLR7R08CF_2lzPDp1L_IBXpONrcYKsck-6zOiSc9v6hcXMP_fBRZe6zKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eii4MjWcxVc1BovOJXKTdm3s9J-7UoTYKB38blTD3Oj_VK58Vk9uvXrxD5MJmZ7JEht6dU_j_-6VM115B9b73CsVlwBpxzIM45kyMSwfWsZ3PVRVxUxXeaeHLtUNKSx-rmQcAxMDmPSUwsgfWlyMhZbV8vsW4PA-CXIURVU2D-xJx6O9GHUyoqp1OEP6-e5Ke9OUKeGIxFNNMMsDXM0HJAyzwkLJggl4VJyTZcOOpj58huZgjIRIJFkQb3-rekd-asv20lnGvClwJBBITHVw2wWPGIwGlyy3bwZXQn4tzgXRUytmjMAXpwEjNfbOpWvu852l-_dV_8AnRW3ozfGcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gh36pNXqAjaWcbMifKUOumFgElKhv6kmLQUCAzswjDLUH0b5D7B70vlIH-210l9sBsYxanrj3n_wS1v3UEGW004yii6k2JapLaddokfNt6GSS3cfL8WC_H-KDhXNoz9nT4GeNL_XmQGlFHgjw1UIQJTFXDx0JGhqT-p3D_AQfcxrKssmX2mbt43cXfYliT9nPCnUUYO1oFmZf_oW0T6xlWI2iyYmqP78FvzF5RsycbxQVQd8v4aizkViHLS91s3l2c5CPE3szXyVo53mV44BAd0mkIKXuw_IIyDN8-U37phdIxbNK0osvcyav1iEX1Yn9bsBIGHOXxnTQHl0Wlp_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOIZx9X6fu-ogyqklgCg6ZVvV5oO5CL6LbBK8vkemVyZjjiqWYQW0eH9WeFwyVv4Ww9KRdoee9Raew1-Rv9Huhep1HL204mc09E-7qajUhplG7c2hzT3QKKHCiiNQHwzTkeHPs3xZs7jIgdJkHI95lDOdM0C1kOhVF6v_npP6KZ0cGNGKueyIKDzy6qn_snqCNHK99fQEgHfdY1PZZp-SuLvIjme7EG68BMNjZpZjGC_KW1kequ1kulUdW5nZvyvB-7KJ2Xs6qbLZgqoDIkdtzzsaEk8dl-gYMS92iSb-GzhHGXdm3mHPZeLIcwE7-2aWqUJ-GD9MpuZKQC4eaTH2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت یک فرهنگ ماندگار
💫
✨
آنچه از نهضت حسینی در دل‌ها ماندگار می‌شود، تنها یک خاطره نیست؛ فرهنگی‌ست که انسان را به مهربانی، ایثار و خدمت فرا می‌خواند.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با توزیع گوشت قربانی، این فرهنگ را در حمایت از خانواده‌های حائز صلاحیت به تصویر می‌کشد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/akhbarefori/678222" target="_blank">📅 00:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678220">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYQFgktcsYsN0lmf8TvGxCFvW-tVeIDgK93jyyQ3fCL5CzL73uV6eFjKJX4DMe4JXrWXhqcyjiN7gK3VIofqPUeBKObOGiYQw_vfXpzMwUwMxbowykava7u15U-NXT1rpDLGPFpUMcC8eND805j23WLhuTN23XYRdyqgrisArjtgHu4WRi7_YeF0xFCajJFXIEQIl0dr2n_9x6WBp9kwI7KSNeI6-5Yggug3tHzrPAcsZmJQkOEgtGRbI0a5uIMKMCZc9QPYaWEsMAId4l_pNQGFztj-f_CzxkIBdi9yXhHrcWAOEeDzsRCOiBq6ejQLx3gSHReURV0L9Io0IWjXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ جنایتکار بار دیگر از شرکت‌های نفتی خواست تا قیمت بنزین را برای مصرف‌کنندگان آمریکایی کاهش دهند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/akhbarefori/678220" target="_blank">📅 00:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678218">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwYdSh-v9jKspQW1v68-wRePX9GW4LDyHSRrIN_NelK8FGhJffc5TxkFkukHnDeHE2nRzcxeX4_G02pYPUtJSKS_A8gaZ1xpb0KiZ94lV6fQKken1zcO0rtzZSTLW4U9oMfgM6Mrz-7l5Sco7BKCPb5VpKgETQ2IV4tMP_UEhZi5IvlZGC-JMqi6JgXQ2yzLUCrgxFW0anpPOzdacu8XLMv7BvNPWQbN52ycGoO8CgFVT2u35p_RAcWLfsDFtUtmJlj5JOHCUzIQZu2NaiqL2EjQXFNrdoIQZxp7mCRQU7i5MhDpZ_OYBfKJCZGRar_P_1JVLzwYE1-DfLevlnJNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZgsPI89TyGw1VsR2TKOm37dgAWu2EoUlP0YdN7LmbPg7IlKiN0OeBePn9698CW2XfQE9L8zSCehxlCaKgPkBc13vC2Nu7mF0NE-0Xpe3S4f-L8BjF7Z4yNBzwSZomudD3sYqINaFJ8TIf5qq6tszU0MRFTg9SZow4SQVPdRI8L1l2x9HDx8XlhH6GxbxR3UHWtbK3Ap7cC5uSs3jTYSZpNsjdWeIGULLI7pj8GwqXTPw59eH5p3vjTo5A4JVMTxhVZ653XGIEIRIUQyQkw_Y7VT62YRQa39OTzsemBWyaWfUQgRdi3L1TXbBtVW8_7wmsywO83OjNTfRZV7QieKlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فکت عجیب: اگر دو، سه و چهار انگلیسی را بنویسید، زیرشان یک خط افقی بکشید و صفحه را ۹۰ درجه بچرخانید، دو، سه و چهار فارسی می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/akhbarefori/678218" target="_blank">📅 00:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678217">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP2rI9EAA4y3H8kkccDEtb4ZhzNhdQHbtR8VWfFE6J0lAN7870Mj4mOeNMHIb7fCyzPFMO5RbiWI6ZElZb5CJWfXBs2YkLeVt_k7pjB_lb6jFYzZTvYrSyObkEeZCDUDPUeeQI-XyznoreBPeiJi8oGk9TmC1-NEPwuIzbw1qX--KWokroN3P3tL1RKTkBP_Qhy1AKscu5gzWtwtYkFIbb4gfTP_EeuA-Pa2zeuLyhOO3JhrTcnGzkgpYw5ebskywml3yBo9md1dqRiSLDS6gGjZGlQU3V3nMaxGLQ2puCqq2xE8FUqplTyJUaQNGs4fUR_H_eJKVPR7KKxLLj9hqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران و العراق لایمکن الفراق
🔹
اربعین امسال، در سایه تهدیدها و حملات نظامی آمریکا، جلوه‌ای کم‌نظیر از همبستگی و وفاق ملت‌های ایران و عراق را به نمایش گذاشت. این راهپیمایی عظیم، بار دیگر ثابت کرد که پیوند دو ملت فراتر از معادلات سیاسی و فشارهای خارجی است. در آوردگاهی که روایتگر ایمان، ایثار و مجاهدت است، میلیون‌ها زائر ایرانی و عراقی، دوشادوش یکدیگر، مسیر عشق و معرفت حسینی را پیمودند و با حضوری پرشکوه، پیام وحدت، مقاومت و همدلی را به جهانیان مخابره کردند؛ پیامی که ریشه در فرهنگ عاشورا و مکتب سیدالشهدا(ع) دارد.
🔹
هشتصدوبیست‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/678217" target="_blank">📅 00:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678214">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQTGa8mb_x9-Emv9k_yQD0PBQ16S_22MecA9qiHwoFxJF0SePHYkrmN8615bc7U7w-4Usd4yJF6ost4XNE5a_dgOUyuMC9jNTJ4Ai05yaOW6q-vvqbn5I3qJW3BDRI8NiMCmygx0lqURba_S6frWGtBdBeJF1OGDiQzJo5TTgkPBxO95OShA5Frgj_ehaQU0ibA5RAoWNRUAH21b3uE82aXsLjB3y2kTUR6tjxI_AdthjD-free9JeX3PJaZKlpXOGCyno9YviIQ05AqbRQK4rStB-DoUfRh_YnthckUvr-GIP2WbBlY4sKHDrD7RtTH6TlXX3BkDrmH7Q0sKjDClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر پزشکیان: ادعای استعفای رئیس‌جمهور واهی و کذب محض است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/678214" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678213">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuCbXT0UkMaEEf9J09OqShLquEraaoz04XSgqfc3un8as8QVDMHPsDRKxFGmp-AdcOA6kKLAi181F6hj7oUzPkZXlRWNdq9b2NgEBe-I5fmouf3CX6jz7XfJTGha-b5JTjw3Osk01NjNrBkGVo1KuNNSQ1ucvssFYGq9CAxjVuD_IJSdq-axHLetJkZCkdA0UC7z1x0dsKq-H0nRGB5U4Y2CL8c3Eb9vODS1EX_P8fQrRjHQS9RlyID_JgbKa-nX_Vv_kBbN4fwleGeiILIsunQtcV-SJKdWkGPF979siQkraTgQnk7SAbJqS7t8yt1KPL5pG_XVf2rI2N9TCfM0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/678213" target="_blank">📅 00:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678212">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhZFJn3sZ8mBDMJyXav-jBVmTbLZz7J0XljSbsRFBcWaxmoP_dEADsfXGro2OzM339o8F_nxaSFLvhzfwA1BAljISMqxkkvdRCCHLSfhZ48a2-5zFEmJb03OuXjiFYEfdnZ5OMK2qQDanZ-vmACTu0cS9EU2PdC4unQC8mScMAJxnITpcGqoDD1g4mls_xoIyt7xWaJH8NDX92Y_M5TiLMHiXEpSGvNm5ZX3eTlMeGZfXoIYxBo0gRJYumMxMch9e-ewncA87XDDXItJ31hriZdIFWqZi3rbHfFepASxumj3s8vj3noOgLBL0kU4YLFnb-W07pQtLTOMa-ZcDOWTwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الایجا مگنیر، تحلیلگر بلژیکی: به نظر من، سنتکام متوجه نیست که وقتی می‌نویسد «۵۰ هزار نیروی آمریکایی در خاورمیانه حضور دارند»، این ادعا تا چه اندازه مضحک به نظر می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/678212" target="_blank">📅 23:59 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
