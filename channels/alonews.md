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
<img src="https://cdn4.telesco.pe/file/PgrcHjsDsPwoEtyTnsbNiYlZod5q46IfzaYKuA85kVY9z-Avmx7rg9aJll6Ls_Jxjsab2EeoNWnBrkFJTTMNp25tEe02z7OcQ3w2sNVdVosCkzBIAkp9Y6Lk1Sbpu8GWJ1G2prr-2QmwhCr139kvIPGV9fATSMNB5mZ90ccG5og415FZaMlSR7yFFhDO8UdezWpoZcRU11Da3sVxjs_P-unnE2KxdZNPANixbdC4Uvk9HKEM8KOz8DklwkeBbPaGeEK28whc0jrPEXZETw63eYhB6QywThkUKEYV7igWDZHyRNF1Py7OjSeKcMQKGe-cQMDl7NFgFzrGKhUB6FY37Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 931K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 19:13:36</div>
<hr>

<div class="tg-post" id="msg-131932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
یک بالگرد آمریکایی در دریای عرب سقوط کرد
🔴
نیروی دریایی ایالات متحده اعلام کرد که یکی از نیروهایش کشته شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/131932" target="_blank">📅 18:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6Gix-asE9kzBEvzEqb-mlgrgbTSKpp588e137vWzdJ88jyOGfIleFBs0-PzO7igDIJQjVb-Jb419eTCYsczvC5PQWGT0Mlqzd5QkqvCpw0JEAjiMv1T9C5QWX0BXgAAAu-XC7REDSSDufRzPWb2k7kyjklb-poXZWDVeisyJbDUaWeO-VOL69gYaZDAeJAV8j5dSTHrpc2k0-S4LvBHeXNdioC0lQ8qO-_vLpxAQqeo2lZkaR7qbdd0P60jDxeyNE0iUW5kzADgfzho1YqdD6WUszatfrFHln4JfACvTavyfrAmLB4nY0cgONa1g7WWO4DqgRJ-XD6cwn6ijbpMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:
پیاده‌سازی تفاهم با آمریکا سخت، اما شدنی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/131931" target="_blank">📅 18:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=rtS7rcwyCZMj7SRnKFGHpiLN13HjBRdLui5Ql9i-3hYjtIoICl6gHNsRarkjt2hSWuqZFkZHDjVvuvY1ysfOq0puDdWPSLEVd-hr10vvvrhCdav2lEFcho5CFBMsHdjll8aRxaWLbvd0IxfFfJ8MtFzbgubBReTxQpTPnPQxegzOu9OVvj3yQjcRMoAbr33WQGuiWOCZ6BbSADCximZZMPDsMOYS5tX_ocuB6iApqXmMpn9sKpvOjrSOvj2M-zVCvMcNqHB3yeM8JdQ4n5Skx9SD4cv3WGjOpFO6pv7jD-cG_NL72yjnA37wwCPlrniZIEMKs-8UKd2BcRVUmHyX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=rtS7rcwyCZMj7SRnKFGHpiLN13HjBRdLui5Ql9i-3hYjtIoICl6gHNsRarkjt2hSWuqZFkZHDjVvuvY1ysfOq0puDdWPSLEVd-hr10vvvrhCdav2lEFcho5CFBMsHdjll8aRxaWLbvd0IxfFfJ8MtFzbgubBReTxQpTPnPQxegzOu9OVvj3yQjcRMoAbr33WQGuiWOCZ6BbSADCximZZMPDsMOYS5tX_ocuB6iApqXmMpn9sKpvOjrSOvj2M-zVCvMcNqHB3yeM8JdQ4n5Skx9SD4cv3WGjOpFO6pv7jD-cG_NL72yjnA37wwCPlrniZIEMKs-8UKd2BcRVUmHyX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی: یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/alonews/131930" target="_blank">📅 17:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf7loJauujROB5QtQkJPTnUMtOmuyliS66-MpHQw82OJ4ByRJX2RT1V_WRY8wWTqRnLryRGBKd0M0fnrfiDi9AthC1Q8iUcjpoVTtgcDPG6ZwGWV-khTB2kWmUpH4a4tomni4yTlImHNNixQ-XAmvNtM9DbOMiTdlh2BXN1zbfq0dUWdwiI_W9fNt8JCB6WFx-HJSGJ1ITwSkicqQIFAiNOH2fQu_Tc5al-vyMXtf993Cl3SV9cpaYKZ1hb85aQmTvHvB2Kbh3zcXOsE0iekelpfomlnEIe1BYVCwx4CAmA6TdGZqGulIOaAPa9EBVhaHyErof2D6iFDtkHelXTXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری پربازدید از نیروهای امنیتی مراسم امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/131929" target="_blank">📅 17:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کارشناس صداوسیما: آمریکا رو به افول است و کارش تا ۲۰۳۰ تمام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/alonews/131928" target="_blank">📅 17:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
اتفاقی عجیب در جام جهانی
‼️
🔴
گروهی از طرفداران زن آرژانتین بعد پیروزی مقابل کیپ ورد در سکوهای استادیوم کاملا عریان شدند
😐
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/131927" target="_blank">📅 17:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
شورای هماهنگی تبلیغات اسلامی: مراسم تشییع رهبر شهید روز دوشنبه، ۱۵ تیر، رأس ساعت ۶:۰۰ آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131925" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131924">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEh8kmRRpq28HwXD78HOZhfH-0tgtdp5oNJ2gNB7CAYnfZykmJ8Fk3GXf2snl151Kx8DqR1IU7o4CwDsSlnvMVdr1RMlqWxDwpa5MqYQihNHbNQ5nvzWO1mwBNdJZq4NKug0V-B2RxAJ5BVlc8P4RNSYb__dv9Bl3nd7mN_IHH5j-20YGUzTfaa4YFSdVLGd40fi5oM64MgVqdl7BzehRXDOpLMzbuPYDQn62_Jn7-XkBd_u_qv1Wp_Qx0XXpJzPhsol64nEYL7BzzMTB1SpuPQboDj74Iolixc5K3KCraVgloupDDIAYPyeS9Rm1fy3RQs5ykxjue8HlyLeJ4R23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/131924" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131923">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f5adc8aa.mp4?token=Ny8fmx3xBjuc7SfOyo1fqjD0JwvAX8yeIIDoFw5Y3ooJXayC43e6I40kY7qCtf-uIkdbAYeOsevEPDjQjWhFb9v8GGwoD4EYEzRl_5Fk45eT8C6oqgyBeNFDa1EtqimAD3Dy1IPY0T2y1DcNA65F3AozkG4F-J-l1s49Xjx2xRZfh3u9PXSsw4R3VwzKxqMpx9aN6ZbuW0y47I4cb0vy2ZCZzBn7WBWhApXc8I6R4D-XzUkg9VDVNxk6VFmnR-kYFaWG_OLc2Jpo3dyedWpNzbCi0LbS2372O4Ld-2IIsY8EuBxtFlFmsx60UQBmdMw3LIlAwS5pIbMoCg_f1gasFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f5adc8aa.mp4?token=Ny8fmx3xBjuc7SfOyo1fqjD0JwvAX8yeIIDoFw5Y3ooJXayC43e6I40kY7qCtf-uIkdbAYeOsevEPDjQjWhFb9v8GGwoD4EYEzRl_5Fk45eT8C6oqgyBeNFDa1EtqimAD3Dy1IPY0T2y1DcNA65F3AozkG4F-J-l1s49Xjx2xRZfh3u9PXSsw4R3VwzKxqMpx9aN6ZbuW0y47I4cb0vy2ZCZzBn7WBWhApXc8I6R4D-XzUkg9VDVNxk6VFmnR-kYFaWG_OLc2Jpo3dyedWpNzbCi0LbS2372O4Ld-2IIsY8EuBxtFlFmsx60UQBmdMw3LIlAwS5pIbMoCg_f1gasFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زینب سلیمانی: شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/alonews/131923" target="_blank">📅 17:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131922">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/131922" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131921">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDMFeM2ZZrpY3EwazNnsULKQIPgBen_Ya71PTL1DNBTtr7ixOkUIUruXN_HkgaTLx3m6Dtuwd0uHYSh1J3r-9knPRzbs1r7ShE5KZAV8cxtQCFw_Zav6LNNodJQr9tkpmdG2Py1EkarSDmAdXAmEivnnslDfbrmYUgilkirjfSTN16WP_ocXNkOrwSQ98IGSvqCoCT7cIERV6itlw-isZo7br_T_i__66mw20KPHeDV0V-NuwW86dz_G34-yORtYZmLmX54Q9Zp4NyifEyEyT2HXPiCUm9LDTA3nbkJ6LJB9_0WsAIDaLT9Y_Nlryd--G-z_i_280WhdE8A1Gg_YnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از حضور سردار وحیدی در مصلای تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/alonews/131921" target="_blank">📅 17:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d57f1ea3b.mp4?token=TRbepTxrtgHW3zI4ZcrPNqU1twM-n7WWf2uD4V0da2NIeRlbmYNpYrasauwIw0hLrLfpd00tJizUf03oljGuN5AYBOKk_8CjQ7yuAD8X0VQd9tU3fJ-X_KM43MaKfYUm70a7nfj0UPitOKPs9s0XYfKciFXERkuWir2bBOCu4OW5CbRsOPQBSBtmLdLIilE7AF784C8Y5MBW3itcIuZjJ9Y_J9q2nXcuwe8qnzoXjwpdanpnPNZnTC9H8eY_ryHTrriznHRfwqX-GxORRW3pO4Qn26nvZSWzmUqIpTxz26vgIVNdLVJlvRxbc-74SmIpjL7kC2I7UUpZjSeWDnJN5ILjl7wGA_JxNjRSrtX3YwyalerJeFMYuyjnvDTiG9106fKOLFMnnXvAGth1BRzfkp9YGxhY91jPtonF1wSGaAaaMMILrrmRC3u7y3JuNzmpWktknX5s2CVCaGkcqBqgFjcBC0sR7g2ESk1fX0BzNIVD6USXGcfypUrv2CAX6uVZOTq3oNs7hQfefgJ_OIFZBeb6Z9zFoeX3GLWKDHfUSQNXqQ11Q76fkaN0ravbX1HeulzQcUXFcIToQgL_slFV_6ky1BfUFQuGyZOsE-ssKONNgKupbCGyFQ3yv2uMshkCFgG9lmFLwAEBwGcZLjluBmZ764Fs00J1mjNTVDO6FEE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d57f1ea3b.mp4?token=TRbepTxrtgHW3zI4ZcrPNqU1twM-n7WWf2uD4V0da2NIeRlbmYNpYrasauwIw0hLrLfpd00tJizUf03oljGuN5AYBOKk_8CjQ7yuAD8X0VQd9tU3fJ-X_KM43MaKfYUm70a7nfj0UPitOKPs9s0XYfKciFXERkuWir2bBOCu4OW5CbRsOPQBSBtmLdLIilE7AF784C8Y5MBW3itcIuZjJ9Y_J9q2nXcuwe8qnzoXjwpdanpnPNZnTC9H8eY_ryHTrriznHRfwqX-GxORRW3pO4Qn26nvZSWzmUqIpTxz26vgIVNdLVJlvRxbc-74SmIpjL7kC2I7UUpZjSeWDnJN5ILjl7wGA_JxNjRSrtX3YwyalerJeFMYuyjnvDTiG9106fKOLFMnnXvAGth1BRzfkp9YGxhY91jPtonF1wSGaAaaMMILrrmRC3u7y3JuNzmpWktknX5s2CVCaGkcqBqgFjcBC0sR7g2ESk1fX0BzNIVD6USXGcfypUrv2CAX6uVZOTq3oNs7hQfefgJ_OIFZBeb6Z9zFoeX3GLWKDHfUSQNXqQ11Q76fkaN0ravbX1HeulzQcUXFcIToQgL_slFV_6ky1BfUFQuGyZOsE-ssKONNgKupbCGyFQ3yv2uMshkCFgG9lmFLwAEBwGcZLjluBmZ764Fs00J1mjNTVDO6FEE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو وحید خزایی جلوی سردان رادان میگه ترامپ گوه خورد وطن فروشا لاشین بعد مثل الاغ ماده میخنده.
🔴
پ.ن: وحید خزایی سال ۹۳ تا ۹۴ یکی از بیشترین پرونده هایه سو استفاده جنسی مال این فرد بوده و بعد از خروج از ایران دائم سایت شرط بندی استوری میکرده
🔴
ویدیوهای متعددی نیز وجود دارد که وحید خزایی به آیت الله خامنه‌ای فحاشی میکرده اما اکنون ژست دیگری گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/131920" target="_blank">📅 17:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJFlSgNtZZWUcbqjK178pYCYnXHEaQS4zuk9JMuJM9M79ZeKPM8gHvG_-G3KeOBnjIOfsJlNeu2xOh-12vrl5Cwt9IO2BELuQKzgUG_SITvqyuy0r3oAI_ikc7eWbNnPG5ot0kx3jKAd0RMYGiCHZUwulpLd5wPQf7R6Yuj3TAB3iTz-OO1hF1O0ZfdUsM6UqsS4MOcSSYvRGGqG3M46C3CLMfpTfpZ5p9Z9pYaYMWrZM2LsoToZKYWUJCmb-NlRdYnrdhGdtEpFcfMM-C-gYGJWSuGfQobbUCuVARJvKgKj2L8CHaI-HOrvPDVmwQR-ffRWEAYOoGaZNuAV8C_Qtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر برگزیده رویترز از زمین لرزه ونزوئلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/131919" target="_blank">📅 17:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ : ما بهترین بازار سهام رو داریم، واقعاً عالیه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/131918" target="_blank">📅 17:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131917">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فارس: کارت ورود به جلسه امتحانات نهایی، تا پایان این هفته منتشر می‌شود. امتحانات نهایی قرار بود از ۲۰ تیر آغاز شود که با یک روز تاخیر از ۲۱ تیر آغاز می‌شود و کارت ورود به جلسه این آزمون هم تا پایان این هفته منتشر می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/131917" target="_blank">📅 16:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131916">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
یائیر لاپید، رهبر اپوزیسیون اسرائیل:  اسرائیل باید زیرساخت‌های ایران را بمباران کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/alonews/131916" target="_blank">📅 16:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
از سرگیری تجارت دریایی ایران و قطر پس از حدود پنج ماه وقفه
🔴
رایزن بازرگانی جمهوری اسلامی ایران در دوحه از بازگشایی مجدد بندر الرویس قطر به روی کالاهای ایرانی و ازسرگیری تجارت دریایی میان دو کشور خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131915" target="_blank">📅 16:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
فرودگاه بین‌المللی بندرعباس عصر امروز با فرود نخستین پرواز مسافری از مبدأ مشهد، پس از چهار ماه وقفه، رسماً فعالیت دوباره خود را آغاز کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/131914" target="_blank">📅 16:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
بنیامین نتانیاهو: بازسازی غزه بدون خلع سلاح و غیرنظامی‌سازی در مناطق تعیین‌شده،امکان‌پذیر نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/131913" target="_blank">📅 16:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
نتانیاهو: ایران می‌خواهد ما را از جنوب لبنان بیرون کند و آنها سعی دارند به ایالات متحده فشار بیاورند.
🔴
ما به خوبی از پس این فشار برمی‌آییم.
🔴
ما حفظ منطقه امنیتی را از دستاورد بزرگ خود علیه لبنان می‌دانیم، اما آنها سعی خواهند کرد از هر طریقی، از جمله اعمال فشار بر دولت لبنان، آن را تضعیف کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/131912" target="_blank">📅 16:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131910">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344ee59971.mp4?token=JWORh92mgh_4Aipbd94HPU3a9R1F_JYEEVlZi3NE6uTOum2Gffageh1opkDt15NidKfJXd3qXILyToWvT1m1JZ7leTZy6UQht8HaV8KvBYGhN0G0wd4ER5SwT6SF-WA5yrEv49VxGtLrAjhKYM9MW4SDMjmArvTeQZooCNLuqF4SBbxcF0EUyIroykXDcIqSuYza9S0L89AW66_LaI6fYYOfxYvGTaudTp253v6D144HaRBK_TQEShHgrYflYbOtWtrLRm-ZQx90cSaqaNUne451PNkqIsKRPcAAuIyxntGq8AaRZrq8JD-eyTCdAgt4XHl0oEns0xJe0gAgt3mGxJx3TbgrYa_ZZHzoJAgItEFvIm_7Rb8Mf5FFMMAuXmR5NCPaO1DvvTbKRM4x90FvWx3MdsxXmxfiwmd2aXpMibp0K5IhjHfiyt9N9OryvhaUNCIZQqzwSQBJ3VtDjs_vfgII1J7_mehIG7hpiQZxg3nAk7xfOur2hvEHEFkPfFdOkb_RkXf15if5PJEAy2hp4KMlrCipwo-KzNOeARju1T3gPSb_g3-i5XoKc4TOnJt8yn-d1URRl4Mjddt5SaA9WkNr2A4HFUUK_ni_4bZw101CFbFk7-UZsIPOL3fd0hjyBtMSLSl2pr10ssQn1h8qp8rwdkXmlvVE_aH8di2GY_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344ee59971.mp4?token=JWORh92mgh_4Aipbd94HPU3a9R1F_JYEEVlZi3NE6uTOum2Gffageh1opkDt15NidKfJXd3qXILyToWvT1m1JZ7leTZy6UQht8HaV8KvBYGhN0G0wd4ER5SwT6SF-WA5yrEv49VxGtLrAjhKYM9MW4SDMjmArvTeQZooCNLuqF4SBbxcF0EUyIroykXDcIqSuYza9S0L89AW66_LaI6fYYOfxYvGTaudTp253v6D144HaRBK_TQEShHgrYflYbOtWtrLRm-ZQx90cSaqaNUne451PNkqIsKRPcAAuIyxntGq8AaRZrq8JD-eyTCdAgt4XHl0oEns0xJe0gAgt3mGxJx3TbgrYa_ZZHzoJAgItEFvIm_7Rb8Mf5FFMMAuXmR5NCPaO1DvvTbKRM4x90FvWx3MdsxXmxfiwmd2aXpMibp0K5IhjHfiyt9N9OryvhaUNCIZQqzwSQBJ3VtDjs_vfgII1J7_mehIG7hpiQZxg3nAk7xfOur2hvEHEFkPfFdOkb_RkXf15if5PJEAy2hp4KMlrCipwo-KzNOeARju1T3gPSb_g3-i5XoKc4TOnJt8yn-d1URRl4Mjddt5SaA9WkNr2A4HFUUK_ni_4bZw101CFbFk7-UZsIPOL3fd0hjyBtMSLSl2pr10ssQn1h8qp8rwdkXmlvVE_aH8di2GY_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ  در حال تماشای خودش در فاکس نیوز
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/131910" target="_blank">📅 16:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131909">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
آلن آیر، عضو تیم مذاکره کننده آمریکا در برجام: برای مذاکرات واقعی میان ایران و آمریکا، باید به گفت‌و‌گو‌ها زمان زیادی داد
🔴
به افرادی نیاز دارید که بلد باشند همه ۸۸ کلید پیانوی دولت را بنوازند؛ کوشنر، ویتکاف و ونس؛ این‌ها سرشان شلوغ است و مشغول کار‌های دیگری هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/131909" target="_blank">📅 16:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131908">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9e3c0b51.mp4?token=fkn5RlKQRFmUKJx69v2FwnDhOxnvhMDrO-KPv5LbuvYi5l4mMRaPps-GPKQG1IqjafUbUvdyfBH1_GOhpY70E6qQDO-Crid0yekv7NSVE24-W3-DjXGzWCGyQZhLb73MhMV_uMJgH12Obs2xqpSXOsJ-ADrS99s-kujJCG2oofPfaGoFwR3lKnIQkX-D-DXF8_fSyzGXXqBlfRhe62kVbpBzS9uUwuSCJWpJfOOU9k6p0BhgyHQd7RwHs8e2K0sF4UWr53qfNvKe2PaNbU25izWT-EHjQTapLZCtnthOJBX_0W_nwGM05Z2nxeOc3P7Ob08HqkDpx-OpbdY25YupaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9e3c0b51.mp4?token=fkn5RlKQRFmUKJx69v2FwnDhOxnvhMDrO-KPv5LbuvYi5l4mMRaPps-GPKQG1IqjafUbUvdyfBH1_GOhpY70E6qQDO-Crid0yekv7NSVE24-W3-DjXGzWCGyQZhLb73MhMV_uMJgH12Obs2xqpSXOsJ-ADrS99s-kujJCG2oofPfaGoFwR3lKnIQkX-D-DXF8_fSyzGXXqBlfRhe62kVbpBzS9uUwuSCJWpJfOOU9k6p0BhgyHQd7RwHs8e2K0sF4UWr53qfNvKe2PaNbU25izWT-EHjQTapLZCtnthOJBX_0W_nwGM05Z2nxeOc3P7Ob08HqkDpx-OpbdY25YupaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی به تخریب منازل در شهر بنت جبیل، در جنوب لبنان، ادامه می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/131908" target="_blank">📅 15:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131907">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCTsZBB9a2rQaXwTxwVxTN9OClZLCzOtrH1R8tgCN03mmaPhwRVPn5ZtIMrX_5kSnQ-Xkp0WRzDW8dQLD1o1YYmkTfh1W9iGTVcZVmA--p9T0YND-Jsv7VkVoMaA4S_6wm8vx7avjqq6EF_fATyCKwJst--qrAXFJKnlg4jzxBx7KwPuyITPn8_JfSA2X-5vqqW8O1IhoAxEuP-mOk1C0AcQ2GNlUPW-m3RY6HmxPPcy2AZbbhGiRpb42c9RiYy1oUrYgAefbRbkg3sYOzMthGQI_SR7T--4urJ6X18S3PlXNai20UkBXE1V92sjNejAlqbnmFfMtAQ7RdLLKS0GVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی در سواحل یمن مورد حمله قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/131907" target="_blank">📅 15:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131906">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
قطر، تعلیق موقت فعالیت‌های دریایی را لغو کرده است، که در نتیجه، تمامی فعالیت‌های کشتیرانی و عملیات دریایی فوراً از سر گرفته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/131906" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131905">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ریاست‌جمهوری سوریه: امانوئل مکرون به‌زودی به دمشق سفر خواهد کرد و یک هیئت از سرمایه‌گذاران فرانسوی در این سفر، مکرون را همراهی خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131905" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131904">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FidBA8KGjMSe9J13ACTRnkh1r3bjppUfYFMLBa89LmSXACwylTQfrke-QOT6dsPltQnJlIC2J2p3oO5q6KWQpbn3cL5Zyu6efD8s4jrYAY7ZcM46QSDK1Tg9VYl-QNAqBINcuwpyXxiVd9yiw3ZrNwIQb0GbqIv4pmkfhcol_Y63RCted6-c4Co68SOfiEtF3eVWYi5FpPqzufNjr5LUErmM7PyyyccIjpmxOJIUslEcKWn9ssA-dQixWG-S6WyKIwN5rTFKBoPHWmWi7teut0M9c2TsnpBCbE8-TIhGImZInSLO-ov_omPKFk9R2gk6ZKxxVLwohEGfPSea7N8Xeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست ترامپ در تروث: از زمان آغاز جنگ در ایران، بیش از 273 آمریکایی در شیکاگو هدف گلوله قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/131904" target="_blank">📅 15:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131903">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل: تهدید ناشی از غزه برطرف شده و هیچ بازسازی‌ای در این باریکه بدون خلع سلاح انجام نخواهد شد. به ساکنان غزه آزادی انتخاب داده شود تا میان ماندن یا ترک تصمیم بگیرند
🔴
ترامپ از ما نخواسته است که علیه تونل‌های حزب‌الله اقدامی نکنیم و برای باقی ماندن در امتداد «خط زرد» در جنوب لبنان، مشروعیت لازم را به دست آورده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/131903" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131902">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سفیر ایران در چین اعلام کرد تهران پس از پایان دوره ۶۰ روزه توافق اولیه با آمریکا، برای کشتی‌های عبوری از تنگه هرمز هزینه خدمات دریافت خواهد کرد، اما کشورهای «دوست» از شرایط ویژه برخوردار خواهند شد
🔴
رحمانی فضلی گفت ایران همراه با عمان در حال تدوین سازوکارهای جدید برای تردد در تنگه هرمز است. او تأکید کرد مبالغ دریافتی «عوارض عبور» نخواهد بود، بلکه هزینه خدماتی مانند تأمین امنیت مسیر، نظارت بر عبور کشتی‌ها و رسیدگی به پیامدهای زیست‌محیطی تردد دریایی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/131902" target="_blank">📅 15:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131901">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
فارس: قایق‌های سپاه 6 کشتی رو از تنگه هرمز خارج کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/131901" target="_blank">📅 15:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131900">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
کدام فرودگاه‌ها فردا تعطیل هستند؟
🔴
در روز ۱۳ و ۱۴ تیرماه پروازها در سراسر کشور بدون محدودیت انجام می شود و برنامه پروازها به روال عادی ادامه دارد.
🔴
۱۵ تیرماه همزمان با برگزاری مراسم تشییع آسمان تهران به طور کامل بسته خواهد شد.
🔴
۱۶ تیرماه نیز فرودگاه مهرآباد فعالیت عادی خود را از سر می گیرد و فرودگاه امام خمینی نیز تعطیل خواهد بود.
🔴
۱۸ تیرماه همزمان با برگزاری مراسم تشییع در مشهد، آسمان این شهر و فرودگاه هاشمی نژاد به طور کامل بسته خواهد شد.
🔴
در روزهای ۱۷ و ۱۸ تیرماه نیز پروازها در سراسر کشور به جز مشهد بدون محدودیت ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/131900" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131899">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
روزنامه عبری معاریو در گزارشی مدعی شد که دونالد ترامپ، رئیس جمهور آمریکا، برای برگزاری یک دیدار سه جانبه در کاخ سفید با حضور بنیامین نتانیاهو، نخست وزیر اسرائیل و جوزف عون، رئیس جمهور لبنان، تلاش خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/131899" target="_blank">📅 15:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131898">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e49482f3e9.mp4?token=MSfKPppzpTHDXmsx0rwmGARfta9TA1m3pgllC_xY3zdwed6kjWO1MoqMJO1FavFu8Ug7dxUL9JkxHyNVNXqdOboCxyJ65FU4NPAMSFUIlXpruZxy3KKi3QUPnrVF3tVpVIvsgfxgclsTIYEj48ohnVAQAPOgNHOxOc7XA-gVNu2iG2Lne1EVIf-xivPj9EVidq-tKynXEPbHWurqtYE6HX82dDg1495vxiILSqA1SpIH4I9pRhZXikZ4tMRlT2r-WDcG8jQwaNj4_h6r0mH93w0551R6nSvFK8OBOfEQxLC8ufj--eyQQ48i0QNAitXh9o954g-p9UxVN1w_UNwYgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e49482f3e9.mp4?token=MSfKPppzpTHDXmsx0rwmGARfta9TA1m3pgllC_xY3zdwed6kjWO1MoqMJO1FavFu8Ug7dxUL9JkxHyNVNXqdOboCxyJ65FU4NPAMSFUIlXpruZxy3KKi3QUPnrVF3tVpVIvsgfxgclsTIYEj48ohnVAQAPOgNHOxOc7XA-gVNu2iG2Lne1EVIf-xivPj9EVidq-tKynXEPbHWurqtYE6HX82dDg1495vxiILSqA1SpIH4I9pRhZXikZ4tMRlT2r-WDcG8jQwaNj4_h6r0mH93w0551R6nSvFK8OBOfEQxLC8ufj--eyQQ48i0QNAitXh9o954g-p9UxVN1w_UNwYgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور ایمان تاجیک، سخنگوی جنگ ۱۲ روزه، تو مصلای تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/131898" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131897">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل: حزب‌الله از توافق ایران حمایت می‌کند و توافق ما را مورد حمله قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131897" target="_blank">📅 14:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131896">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سفیر ایران در چین: کشتی هایی که از تنگه میگذرن باید هزینه ناوبری بدن ولی برای کشتی های چینی تخفیف و ملاحظات خوبی در نظر گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/131896" target="_blank">📅 14:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131895">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjYhZRS2ZDfmDXNBuL-Kkaz2L1Pcg_uiRHndrIi4JpKXqcNbY2qW9WNAo7nWsfsV0ISzkb1bg6nt6PwPq3KmXrffZkFfdfjXe6FFGUqeDRad3MnTvHYm3UgXbZN_mAxBCxmhZuJ6CueM40NtuFaR5-eaPnvd5K-wSLada1-AXaGEOLeh0zMU2pFG3QlHemBLaVbmgmxRk-sgFMjZbHyaONdb_OZqkvHN1iHGKaorraa-mEhqVKXKtkDxI6kaRGuiXMCGMBQ_RpHJKdGnhlhb_FK3Q2VuWj0beVG_dQ_qc8FX0qHWVRw0aDXbTHE2r0cnSxodXA9pJxy5_vqgAxAHCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده در مراسم تشییع
🔴
خواهیم دید چه می‌شود...
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/131895" target="_blank">📅 14:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131894">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نتانیاهو : حرف‌هایی که درباره درخواست ترامپ برای حمله نکردن به تونل‌های لبنان پخش شده
🔴
کاملاً دروغه، ترامپ اصلاً چیزی رو به من نگفته
🔴
منم چنین درخواستی ازش نکردم و ما تصمیم‌هامون رو بر اساس ملاحظات خودمون می‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/131894" target="_blank">📅 14:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131893">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
محمد مخبر: قاتلین امام به مرگ طبیعی نخواهند مُرد و نظام انتقام خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/131893" target="_blank">📅 14:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131892">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589db9025b.mp4?token=JjLx57VdIAminIwNqONlanr6v96_llsBZmBrkiteZEWQQLkZbf2s_Q8DDbkbQhDLj_39LjuZqWRTQuHFlPm12Ffr34byhx--Jtb9MX7T7p2uzyWhG-BdQVLjYFfoLBtfPIyYuGwpgM2iWi1ATljnT4dx_tFAo4heUEaWZJByvsBvtiFbYiu9iVLRdeXlisAL4C89bKUifJSTIiGpkm5_iM7AQrseWr45-rlENI1F3kL0Sy5gdtDUTvvwEs6_f3vKAbX_0L-nRn8iSeAiuwa5zkf8HYCGmPeqPM4axNaXJGrAVqeIRpYE_Ie9jm1mP7gVnWl3mUm38ECbmC33-XvuSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589db9025b.mp4?token=JjLx57VdIAminIwNqONlanr6v96_llsBZmBrkiteZEWQQLkZbf2s_Q8DDbkbQhDLj_39LjuZqWRTQuHFlPm12Ffr34byhx--Jtb9MX7T7p2uzyWhG-BdQVLjYFfoLBtfPIyYuGwpgM2iWi1ATljnT4dx_tFAo4heUEaWZJByvsBvtiFbYiu9iVLRdeXlisAL4C89bKUifJSTIiGpkm5_iM7AQrseWr45-rlENI1F3kL0Sy5gdtDUTvvwEs6_f3vKAbX_0L-nRn8iSeAiuwa5zkf8HYCGmPeqPM4axNaXJGrAVqeIRpYE_Ie9jm1mP7gVnWl3mUm38ECbmC33-XvuSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات توپخانه ای اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/131892" target="_blank">📅 14:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131890">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مدودف: ایران سلاح‌ هسته‌ای اش را حفظ می‌کند!
🔴
ایران به جای داشتن یک سلاح هسته‌ای واقعی، متوجه شده است که سلاح دیگری دارد که از سلاح هسته‌ای ضعیف‌تر نیست، یعنی تنگه هرمز، که وضعیت بین‌المللی پیچیده‌ای دارد. ایران نه تنها این سلاح‌های هسته‌ای را حفظ می‌کند، بلکه یک سلاح هسته‌ای حرارتی نیز دارد که همان تنگه باب المندب است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/131890" target="_blank">📅 14:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131889">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnfnWbxC785ei_68b1wEuv3hpJ2QXVutyznogvXaCZd1kCD056r-0_wfY5bg3YleqJn-jTQAKFkglO-iyaxDAvH9Z6q9j1lT9tIJ1u9KQHKzSeCnWZY2MlbIYxIB6qbOUtDp0_-nlx2E9LSqAPfAHclTsu3wqVkbsqrUlAJjRYdElWKYvaoKuW9qtx14CNewe2SryTMTkCc-oX4kuLPLG4t7_OHQST8TQkJXqCnPrCBJD8pw0hbujDknhJlY9e6EQVL4_PGppBwRg29kc65Pghca_Ce9oEem_EzLLk0Egv1IC6U8fcQo3wthHJeeOJ5OWA_qMB2Z3ajHb4LeK4Osdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیرخانه شورای عالی امنیت ملی:
این چند روز چشم‌تان را به ایران بدوزید؛ این همان ایرانی است که خیال می‌کردید چند روزه می‌توانید آن‌ را از پا درآورید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/131889" target="_blank">📅 14:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131888">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
خودروسازان چینی با رشد سریع صادرات و استقبال بازار اروپا، برای نخستین‌بار از نظر حجم فروش از رقبای ژاپنی عبور کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/131888" target="_blank">📅 13:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131887">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
شرکت بهره‌برداری متروی تهران: از بامداد تا ساعت ۹ صبح امروز، یک میلیون و ۳۰۸ هزار و ۴۴۵ مسافر، بیش از ۳ میلیون سفر در متروی تهران داشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/131887" target="_blank">📅 13:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131886">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
به گفته برخی منابع در اسرائیل معتقدند احتمال وقوع یک درگیری نظامی مجدد با ایران در آینده نزدیک وجود دارد.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/131886" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131885">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
دولت ژاپن در حال بررسی کاهش سطح هشدار سفر به ایران است
🔴
در پی بروز جنگ آمریکا و اسرائیل علیه ایران، وزارت خارجه ژاپن سطح هشدار سفر اتباع خود به ایران و 3 کشور منطقه را به درجه 4 (تخلیه فوری) افزایش داده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/131885" target="_blank">📅 13:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131884">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2zbfMIwEzlvTDY-hHc7Xx5I5kgbTYgTk-oAchVgymVAEHb95OuwnD7yZOF9QMrNjxtpOe7VOYNBv2ixcq_ITohhnZcKRSo9gasOinBozkDbIYNYaniG9ZAs_pVtlabBcGqm-0qsYY7M9my8hv6lAF4GDlgDtvzMByGDWItZM99cjVjXCjdQysN9Mn_Ust2fJzd09nppSsyeAJycegWdHpItYhj-CBPSORCt7Baeb8SVibviaJRlVh3Xm_6jfR1K-Vf2tZBbsNjuGKkWAJoRiRDZdyajJJPXUQMzcCdyNLPU4j4JQuBRfl9ghdtlNqQEI8qV9aQTLDcd4zYhUYm_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت آزاد کشمیرِ تحت کنترل پاکستان
🔴
با گذشت یک ماه از قطعیش، هنوز شدیداً مختلهِ - Nut blocks
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/131884" target="_blank">📅 13:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131883">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تلگرام از مرز یک میلیارد کاربر فعال ماهانه عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/131883" target="_blank">📅 13:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131882">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
جوزف عون، رئیس‌جمهور لبنان :
من علاقه‌ای به اسرائیل ندارم، اما راه حل دیگری را به من پیشنهاد دهید که ما را از این جنگ‌ها بیرون ببرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/131882" target="_blank">📅 13:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131881">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
العربیه: ترکیب و سطح هیئت اعزامی‌ایران هنوز نهایی نشده و پس از پایان مراسم تشییع، تعیین خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/131881" target="_blank">📅 12:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131880">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zqy_hUPeAHlccVQL8S4HliAT1pN4MIeVRtmmdu16KSqsBIpviWP5gnENeerkDkQVk3NwoDoS_ypZG0Sga_U4-EYeyfAxi3bSqrMMXEtMuzC89MbS5iIt0ZTmOZ1WoDmbO6lAlWvRlvlXOkvpECYLVzZZU2g4KHBYuv5SgrLjBOLn9OQktJMBPhU__wi7i2D6UaJAucP3GP2OetKpZNJM15dcGcO4J-F_oiiiVvqolNGnpMH8t8EcdPYaBHw8DvPUh6dCWyLAoxjkB_SIbv88OpQqidevB6GlPTeKcUSx1L_ehN2UeHAxpOm1zAa56d6MJC1xmmdTVE14jrQ_Yq-ejQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکایی ها مجددا یک گروه از نفتکش ها را ردیف کرده و در حال اسکورت آنها به سمت تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/131880" target="_blank">📅 12:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131879">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سامانه گنبد آهنین به امارات ارسال شد.
🔴
میری رگو، وزیر کابینه اسرائیل مدعی شد که اسرائیل سامانه پدافندی «گنبد آهنین» را به امارات متحده عربی ارسال کرده است.
🔴
وی همچنین ادعا کرد: اماراتی‌ها از ما کمک می‌گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/131879" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131878">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: نتانیاهو احتمالاً هفته آینده به کاخ سفید می‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131878" target="_blank">📅 12:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131877">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سازمان دریایی بریتانیا: یک کشتی باری در سواحل الحدیده یمن از سوی افراد مسلح ناشناس مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/131877" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131876">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل از حمله هوایی به غزه و ترور دو عضو ارشد حماس خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/131876" target="_blank">📅 12:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131875">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
استانداری هرمزگان: احتمال شنیدن صدای انفجار ناشی از خنثی‌سازی مهمات در امروز وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/131875" target="_blank">📅 12:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131874">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
دعوت رسمی از ترامپ برای سفر به پاکستان
🔴
آصف علی زرداری، رئیس‌جمهور پاکستان، هم‌زمان با روز استقلال آمریکا، به‌صورت رسمی از دونالد ترامپ، رئیس‌جمهور این کشور، برای سفر به پاکستان دعوت کرد.
🔴
حساب رسمی رئیس‌جمهور پاکستان در شبکه اجتماعی «ایکس» اعلام کرد مردم این کشور مشتاق استقبال از ترامپ در اسلام‌آباد هستند و میزبانی از وی را مایه افتخار می‌دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/131874" target="_blank">📅 12:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131870">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MrnNjYBF4klNQ2r_8wS-chlSSCZdTnwZCf6dZUT71TTpNYkm7hBQEIroJQriCQz88GqYFNtQTMcdx-v4PjMxdMVanYr51ZufK_h6eE29mEOyw3BdaIrCRGObbU__FRGRDhdlsJiuqketDWa_Rom7WR8V54swI8DwXtDtsSixp0GR8GF0kuIJ-9xMUaLDJWkz8s0HbsKIzYMcGkThltQ0VFWtMJxqMygNE8xmgIkVo_SGeBeuREVj8VoVK0OaSJSBSi8xVHKZf4HLqMMS62-OuuBix69IppiyeCusoW911lYJNMaaxRPFTNR1CSYS39aGuRoE_5Hf6QaoGtJdfg_41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EW9IgD5C0Z-N6ueHMsu_Rkw6z7krM0E9qX1oqh1dWtAHW6J5KoxrTR0h-59PDrWff25QKgbY__E2sa-Sd99Z0l-XoyK811AMpSIhHz2UG-s0CNB-mIOzSBA8MVHkwDxpUaPGJEzQFnlg6eZCRXUZblsOQoyAmHolE8W3zKTp15NXXs9kjC06JKPHb9aGHd6YOpVmgq7W-o5C4U6dWbK5oYC0w_xGOXHa4HVZxL2IZcIceR4bTPQicv7RQ9vprQbemMq-x0jUvTnV-D3d62KKQxc-B398mtKdOKgg76LTON6M9RptovxxnyjmaGW45-YffqDo_xKie1bnlBqB8VVmKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBjZJcOfJiSmS8NbXdKjl6VPHJTN-tZ0R4CV6qoDATx3Py8VIsGg2koU-UqJEBo_8_25o6ND5SqCwmqM366txaj4SZWqTiVgdsIA5eygcDH72g5O7XQtLF4qQxhH4w2kcKk2DkAHhkLtZF8zcfwJQwR2LSe07JJzsLEtbzu4LK9lclK3gD8V5x5BsOYXXef1up7Ow4027z8f1krJWwFHTqVciTufBIOU1z4enXRJE1PsbAW0SeItGVcSMp-lVGr_id2iSQ9Hjlsyp56L3e5x7mDdWPthuKZ_OJKZKU1L5vxTW_4wpKmU4nwd0q8FcZ3HwWAITaTGKP25wdArKggNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZeTySh0jUZUcvGn8ndPgdffYMaqHTy1_QbpbpGjfyo10dtZUOImNp2SnCt2jk3DIO1X_TUhsse2d1qnNBIjlGy3IAaQ46cg34H26p5rCj3TgIExSDX977LWojBRXRr6sGKgGqHxXsxEGPnCzM25w-FJ8GIa4LIN9gJmUyjIRIngRnYfrdiOxtX8u7UHWLSYIYZVbIwoLUmxezM6hsyyQVW2ipJRBcBf7ZwQo5KFg5iSNUR7kE_lX0rbErtCZKoorPmcwMDCy1IaiB6-l8aheHK4YJm-tzlsNgmpj5OIIsU783bXtO6ugDO9qaC63DA48-H87aMlqzMQlOHZHDyKwow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کیم جونگ اون، رهبر کره شمالی، از آزمایش‌ های موشک کروز استراتژیک و سامانه‌ های پدافندی ناو شکن جدید «کانگ کون» بازدید کرد
🔴
این آزمایش‌ها که جمعه انجام شد، شامل ارزیابی سیستم‌های شناسایی، توپ‌های دریایی و جنگ الکترونیک بود. کیم از پیشرفت تسلیحاتی ابراز رضایت کرد و دستور داد تا ظرف دو ماه آزمایش‌ها تکمیل و ناو به ناوگان اضافه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/131870" target="_blank">📅 12:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131869">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
اتفاقی عجیب در جام جهانی
‼️
🔴
گروهی از طرفداران زن آرژانتین بعد پیروزی مقابل کیپ ورد در سکوهای استادیوم کاملا عریان شدند
😐
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/131869" target="_blank">📅 12:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cn7bDvVyWLCykOsIZkJwRTm7yauh0uYEi0pSyzEQpxHEPWjQRoRzbRa4aHPDdg0FM80quxufgAPopC9SHgDlQg3O211JbtNHmB1olD6XQC1bSLVSFIlLaqZbjHyvY7AwIhDBBXF1TZmdgZlxOTq5nRRRmoBedAMsYMrnTlc88HHom3ubam_6ZFRIHUZWMlHi5B3y2UHlYaCwNm-hyT3o8zYve4g_mNI3Gm9EtudEQWV0SvQrueoMtFk8X6PNi28pRuo9lv5jlecMPzQXEnEaknaydW6jZnxYOI6YoqlK4UkQIozxs7lLLyAeQyMyhdzk2Djp1vvDfD833Jt_YCe0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YxILHJXPyHHyEAJSTNm6HgfLH0YusLEni9aPTcfWddGi31wdo2D_hgrfxns7MktSHcPqsE_rO357lceB7bxm9lX4ZmUeoU0mQfguCYvUIoebyodplsck8w9grStvFal5Z_sMQFVJEVTPUjMCloJTRfXXfW_ZIaUv32kggFCGMgVWGz3rVlvD0JcGcrGxKzcUMEgAyBieBX7TQbg1a1TanPKh7SVB-WzsWyYnsPu2qPiOv5zbDMxIPrKOBFY4jWfZ3f_f9ZyZ5AdFourJ4I_t3KZn3R_RosR1xybcudft0XYYg_Hh-UzutYRqdA8hLX4bgQyVl_ZkrkR_aYfO5jn-ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نیویورک تایمز گزارش داد: نیروهای نظامی اوکراین با استفاده از حملات گسترده پهپادی ضربات سنگینی را به کریمه اشغالی وارد می‌کنند و هدفشان این است که این منطقه را از یک پایگاه اشغال‌شده توسط روسیه به یک کابوس برای آنها تبدیل کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/131867" target="_blank">📅 12:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131865">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/131865" target="_blank">📅 12:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131864">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/131864" target="_blank">📅 12:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131863">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa11f8e93a.mp4?token=KZJeI6aoY3Gk6bOWr5RT3ubGHL7cHmPQGF14p7oUOrmLdlBnU2nUfXhHQv0ASTUuvMNOHJk1rCWPaeMz__Zf6IY17kXk09mv8d5eJ2FxXD77PZwypZiZBll3abONMDL-cZOsT3GcfT0k17WYX3Q5chw-jUfJFwKEuOnOW2XuBuSjOkSxHzhZGpXa1t11bC6Tpo6G_mqGui2OG4NUI4MpkwEGlcwiVjAo9zaVxLJWwMruGI93y96MeaJG6O2ov-PpqprFzjl0Hh6E4e0yetlVGESv3WHg5uyMiuU_M6P3j_Ib54PmLfgwGBYd8EdpvlMSSVcKemE1KOg-tGgkAXzuwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa11f8e93a.mp4?token=KZJeI6aoY3Gk6bOWr5RT3ubGHL7cHmPQGF14p7oUOrmLdlBnU2nUfXhHQv0ASTUuvMNOHJk1rCWPaeMz__Zf6IY17kXk09mv8d5eJ2FxXD77PZwypZiZBll3abONMDL-cZOsT3GcfT0k17WYX3Q5chw-jUfJFwKEuOnOW2XuBuSjOkSxHzhZGpXa1t11bC6Tpo6G_mqGui2OG4NUI4MpkwEGlcwiVjAo9zaVxLJWwMruGI93y96MeaJG6O2ov-PpqprFzjl0Hh6E4e0yetlVGESv3WHg5uyMiuU_M6P3j_Ib54PmLfgwGBYd8EdpvlMSSVcKemE1KOg-tGgkAXzuwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر هوایی از مصلی و خیابان‌های اطراف
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/131863" target="_blank">📅 11:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131862">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
شبکه «فرانس ۲۴» گزارش داد که دونالد ترامپ، رئیس‌جمهور آمریکا، پیش از برگزاری نشست ناتو در ترکیه، با ولادیمیر پوتین، رئیس‌جمهور روسیه، و ولودیمیر زلنسکی، رئیس‌جمهور اوکراین، گفت‌وگو خواهد کرد.
🔴
این رایزنی‌ها در حالی انجام می‌شود که جنگ اوکراین و مسائل امنیتی اروپا از مهم‌ترین محورهای نشست پیش‌روی ناتو به شمار می‌روند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/131862" target="_blank">📅 11:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131861">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b32a145c3.mp4?token=mPDt4NoMntpNKeQ8QxEjyUdJhzYSbeN08PrNv-WtAWsYVZs5fbiB9VlP8M9ELg-rE2R2qlR6zPWRCj_P7bkP1p1R1E1IG12F0HHR8ocZt0Cp2AGKv9hrdIaXpeqyCcfZboz8bwhEOggSZdjzGzf7_ziZ6ToDZY-miZAeqIPHTMJ3lUk0WqKpJiBXoA9fInv3ItceYjzTx8zhw0g6u6KhAtxn5j5_fWPrTNPBcVO6cOrj8BQcTacypskXVK76xqAyVQMuJy4FW1amBgjI2sOuyEeKJlgMoG3FG29wNT_985lvqBSugR2VTUpPm50-MKU03Hp2c2wAJ4Q7Gdb_NQmYCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b32a145c3.mp4?token=mPDt4NoMntpNKeQ8QxEjyUdJhzYSbeN08PrNv-WtAWsYVZs5fbiB9VlP8M9ELg-rE2R2qlR6zPWRCj_P7bkP1p1R1E1IG12F0HHR8ocZt0Cp2AGKv9hrdIaXpeqyCcfZboz8bwhEOggSZdjzGzf7_ziZ6ToDZY-miZAeqIPHTMJ3lUk0WqKpJiBXoA9fInv3ItceYjzTx8zhw0g6u6KhAtxn5j5_fWPrTNPBcVO6cOrj8BQcTacypskXVK76xqAyVQMuJy4FW1amBgjI2sOuyEeKJlgMoG3FG29wNT_985lvqBSugR2VTUpPm50-MKU03Hp2c2wAJ4Q7Gdb_NQmYCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور فرزندان و داماد آیت الله خامنه‌ای در نماز میت امروز مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/131861" target="_blank">📅 11:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131860">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سخنگوی ارتش: بار‌ها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توان رزمی خود استفاده می‌کنیم؛ یک لحظه را هم از دست نداده و غافل نمی‌شویم
🔴
اگر دشمنان خطایی کنند، حتما با پاسخ کوبنده نیرو‌های مسلح ایران مواجه خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/131860" target="_blank">📅 11:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131859">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
کرملین: تماس تلفنی ۸۵ دقیقه‌ای پوتین و ترامپ درباره جنگ اوکراین
🔴
رئیس‌جمهور آمریکا پیشنهاد داد که در جریان نشست سران ناتو در ترکیه، برای پایان دادن به این درگیری کمک کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/131859" target="_blank">📅 11:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131858">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7sChSgbWSBovZhCGKbuUi4sdEXx58443lXl_jmGl2T1G4JPFFJTPas69Pw7K3eyBDt25pvxLB5CBTAGxmLl8WcInZKUXjD5cHO6_ZqRJ6zDdGlvLhMYSvbERIXFjrS5epA-x8WewpCeihc-ga2_iickEo_S9XmVbyKrHawLB_g6vmRr3WKwu0Q1fmUwc2RBMvQ2isSmpdUgOvLbEXKi6p0Fa0AdfCzYlXL2A6lg9iBhO7I8hRZ7V_UJz7baFHKgtLAIADGFBpARP0xJtryICDfjwV1etNMn6teZRXpQUn5-07jpnAnk93eiI6kZeX-QhM62NBfMp_MuVn_XulRR6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هرمزلتر: نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131858" target="_blank">📅 11:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131857">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وزارت حمل‌ونقل قطر اعلام کرد فعالیت‌های دریایی از یکشنبه از سر گرفته می‌شود
🔴
این وزارتخانه ۸ تیر از همه شناورها خواسته بود تا اطلاع ثانوی تردد و فعالیت‌های دریایی را متوقف کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/131857" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131856">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ : ما هنوز هم پرچمی رو داریم که بعد از غرق شدن ناوگان اسپانیا در خلیج مانیل
🔴
روی ناو فرماندهی آمریکا برافراشته شد؛ یکی از بزرگ‌ترین پیروزی‌های دریایی تاریخ
🔴
همین چند وقت پیش هم کل ناوگان ایران رو با ۱۵۹ شناور به قعر دریا فرستادیم
🔴
همه این‌ها توی مدت خیلی کوتاهی انجام شد؛ انقدر سریع که باورکردنی نبود
🔴
ما قدرتمندترین ارتش دنیا رو داریم
🔴
از ارتشمون استفاده کردیم و نتایج فوق‌العاده‌ای گرفتیم
🔴
به ونزوئلا نگاه کنید، به ایران نگاه کنید؛ ما نابودشون کردیم، ارتششون رو از بین بردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/131856" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131854">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BgK6ywLbn5o70397mmlu_R-RY7mpF9dUf6bazCv11k4LpOeuniyl0jQ0ymsHyA1LjggAlIzeGy30QAhpeDZptnd4CM2e1_Moamwv8UAMoFHXiIMgpNmGEVM60j8CNoJ3VwI3NCbrC29vX6B05BNk7atWAVNmHayxxKN00hvtP6tk8qBabOsUntwmB-Kx-r1ncBYkDpCcxRhwfpNi4BhnSF1OKhTC_KXGNWmtEKBRtW7BYVe8Ho8S00WbDZz8vVhflmE-HIhKp0j2HYiyY1j9gfQ02C9xf9sIg39RnoWA9Lwn73FvRM7cpvvb0MQiKTUgBZw2hNWb3CW78vA6uAqP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJTJ6ZoaLxpZwmNssvCC0FUKidLEIfM6o1P61ZuXge9nsKSRTqunSiIVgBjVgj5Vi0YZGeKsNJAibyoFeJSmMkyawNc_U4qjj7Cau5Yh64gEa2vKRw3iFnvzEjLLl2S4h5lY8Z0fgu1tWEeyvWqny6N57A3DIJMC8_WUSajFxCQtpj8VNNg81g-TLivvyFMMwx3U3XskERRaiqRlwqvk8VjFzeB48joeCKkI8L_tCF0I27JLok1Jeca1SAap2lrpbbsPmtwsWdUVsQmX4lTs6rlrHgMEa_0usA9R_mcmTDFO1UhmLFw64Aq2RTLh0Wnesc0C9tVswaduv4rQUglozA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نخستین تصاویر از بوئینگ‌های ۷۷۷
عربستان که به‌تازگی وارد ایران شده‌اند
🔴
بوئینگ ۷۷۷ یکی از موفق‌ترین هواپیماهای پهن‌پیکر دوموتوره جهان به شمار می‌رود که برای پروازهای میان‌برد و دوربرد طراحی شده است.
🔴
این هواپیما با بهره‌گیری از موتورهای قدرتمند، سامانه‌های پیشرفته ناوبری و مدیریت پرواز، به یکی از ستون‌های اصلی ناوگان بسیاری از شرکت‌های هواپیمایی بزرگ جهان تبدیل شده است.
🔴
خانواده ۷۷۷ به دلیل مصرف سوخت بهینه، قابلیت اطمینان بالا و هزینه عملیاتی مناسب نسبت به هواپیماهای چهارموتوره، همچنان از محبوب‌ترین هواپیماهای دوربرد جهان محسوب می‌شود.
🔴
هواپیماهای واردشده به ایران از نوع بوئینگ 777-300ER هستند؛ پرفروش‌ترین و موفق‌ترین مدل خانواده ۷۷۷
🔴
این هواپیما به موتورهای GE90-115B، قدرتمندترین موتورهای توربوفن نصب‌شده روی یک هواپیمای مسافربری، مجهز است و با بردی در حدود ۱۳٬۶۵۰ کیلومتر و ظرفیت حدود ۳۶۰ تا ۴۰۰ مسافر (بسته به چیدمان کابین)، برای انجام پروازهای طولانی و بین‌قاره‌ای طراحی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/131854" target="_blank">📅 11:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131853">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وال استریت ژورنال: ایران، روسیه و کره شمالی، در نحوه تعامل با بازار ارز‌های دیجیتال، ایجاد رمزارز‌های اختصاصی خود و پلتفرم‌های معاملاتی برای دور زدن تحریم‌ها، بسیار پیشرفته‌تر شده‌اند
🔴
تهران و مسکو از ارز‌های دیجیتال برای خرید پهپاد و قطعات یدکی تسلیحات استفاده می‌کنند
🔴
ارز‌های دیجیتال به این کشور‌ها امکان می‌دهد تا از سیستم بانکی سنتی عبور کنند
🔴
مقامات غربی به سختی در تلاش برای همگام شدن با این وضعیت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/131853" target="_blank">📅 10:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131852">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
گزارش بلومبرگ حاکی از آن است که روند عبور و مرور کشتی‌ها از تنگه هرمز، به‌ویژه در امتداد سواحل عمان، روز یکشنبه به شدت کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/131852" target="_blank">📅 10:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131851">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
آتش‌بازی‌ها در واشنگتن، به مناسبت دویست و پنجاهمین  سالگرد استقلال ایالات متحده
🔴
ترامپ در توییتر نوشت: بهترین آتش‌بازی‌ها در تمام دوران
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/131851" target="_blank">📅 10:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131850">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
گزارش خبرنگار ان بی سی نیوز از مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/131850" target="_blank">📅 10:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131849">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4M8bBHF-zlmKC5nCEzTHfPrj9fBIspUNNKlxmQ9-aDi6d9i-pDQkScj8Y61aB2QpBOZ5gSVb66tIZ6JE8rYGPBYjctic7y08V9Qs_LLznpA_9_Euus3MbFkQozyOBjHtSETl_hOSxHACmNAhz0fuWwaAR_dAiDtAzlsLmNMOzTD5W_HCSdx7RvYxc6PfA-t2QLJvKdtTGHfD4bZRYnDE5tYWlylvXSeP1gArKG61IOFsqF4bGM6tiijvwXp3zsPpoHWGfRsZDnavrJssvExWG28Kw421zSKjNHP5awCRjCTqF42eeSdgTggI3EOjUS9m62FIXXC2mA8aHmaYUFh3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست: آمریکا هنوز یک قدرت بزرگ است، اما دیگر مانند گذشته بر جهان مسلط نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/131849" target="_blank">📅 09:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131848">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترافیک سنگین در ورودی‌های پایتخت
🔴
ترافیک در محورهای چالوس و هراز در هر دو مسیر رفت و برگشت سنگین است.
🔴
محور قدیم بومهن–تهران و آزادراه قم–تهران در ورودی‌های پایتخت با ترافیک سنگین مواجه هستند.
🔴
تمامی محورهای شمالی کشور فاقد هرگونه مداخلات جوی هستند و تردد در آن‌ها بدون مشکل جوی در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/131848" target="_blank">📅 09:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131847">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رئیس شورای هماهنگی تبلیغات اسلامی: امروز در تهران آمادگی اسکان نزدیک به ۳ میلیون نفر را داریم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131847" target="_blank">📅 09:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131846">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa2c1939de.mp4?token=frEuFM-XEYLQgzkMN2XdMqfkSq2rsRZs5WNMIlXw1xAFzZpqlnT0ahjuZ1Q98OIWdsHrnQ535-l5b2018uq-TVIhiuiw-8ps_uiEedY-kit0tNEAXsnJBM312DjcVX1-iRLw_8pIY3KNwHXzBetIU_wgOHjIZ7RPBjctyDlZxyYLIzJAFnrnDslAx1gykKTYQEEtTB4aOC7ER2P86GsTwxdLdH9UwE0MGR69OESAo33BGtpjVPXmA6i4QvqN7-V5vFR3BodPOWLtDJvvE6QyLoyXz6luAU3JuOc7YaD_EZK-xt5DWiPOziHbMFX0BjkEt_bRicRPRTsdkF7fOyE2ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa2c1939de.mp4?token=frEuFM-XEYLQgzkMN2XdMqfkSq2rsRZs5WNMIlXw1xAFzZpqlnT0ahjuZ1Q98OIWdsHrnQ535-l5b2018uq-TVIhiuiw-8ps_uiEedY-kit0tNEAXsnJBM312DjcVX1-iRLw_8pIY3KNwHXzBetIU_wgOHjIZ7RPBjctyDlZxyYLIzJAFnrnDslAx1gykKTYQEEtTB4aOC7ER2P86GsTwxdLdH9UwE0MGR69OESAo33BGtpjVPXmA6i4QvqN7-V5vFR3BodPOWLtDJvvE6QyLoyXz6luAU3JuOc7YaD_EZK-xt5DWiPOziHbMFX0BjkEt_bRicRPRTsdkF7fOyE2ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما به زودی به مریخ خواهیم رفت
🔴
ابتدا به ماه و سپس به مریخ خواهیم رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/131846" target="_blank">📅 09:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131845">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVIL2dJ40hyOn6yBSnz-CsivTIa6QvxTEdWOpYXnZ_qQVqxli-XUQ9LwAlERPfdpq_roIjauSJ9SSjOOi_5SlWnKeqlYB09AzoOzWthw31rPZZhqeelbWUkSrEK_OgKO4MKQyr51QnkCj3XKIVYKBMo45RQkipuh1vn9_jHpuO8aZvNyS9KoH7PZUr6H8ciDPAt1RIwaLvvY2TxcFJr55Kdwnzr172yymOqCSQuNZVAHFtpVXmlFDz-Z_IyFTzWX-GSJ8CIrwLtqc-OC3CzaHQTH0sM4h71xUA0L93jJA3qtllFbEF00BaR0M8ctQ8BPWX3Ub2Zct9PDvBb5P9pVQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از خیابان‌های اطراف مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/131845" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131843">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXRwNeY3Jp35cuA5RL9-qeZGtsOKVdSRIx1j0E8LWsAVb1qWjRrCukPP99sQu23YTt5bRcFENvYkAlx6BKSNs_s1IkCwuE5wk5bN2uDHAmrfeRE2OxbqCRzNFOpgjSMKgnv0ohX_xdAdVw9x1ofDFRZAESgrmCpx7sKErnmu9lTArXpn2YkITllg7l2FZNWhlhZNn9Mve2HDLFyXq35Cvg9YRvV5pCF8E-l6d3Sz2LraEKiNj_I9VCYa9NuC3_UAcoFAofDhN9fR1FfaGGPuxOVZt7IgkIL7OUUDvZY0VsI9wTljIgbG51KX1nTkgMVCO_QPaiR96v-y0iyF6CU_oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lt0ZBIH1K0ts-zJOTbMhFPmWNbxroSI0C98O_XQnFube6r0nBH3DQWdEDfrMd7fUPiszn_KiAT86augz7ZbH_E-oeBsORu8pao83xddWMjSsTmBycUOIxbC4GDsLGAQ_YbC1SvOmiCfmB7FQo793yq8-tMiaiOGxUMgk41fbZnuQ2SJL0VruPBa4mmYg_EeTbFk_YVbzznoV2olnzZQsWnFEOTfw383Y7GYw5NMSFrstYDRp0Ct7cHnZpARZ-gD5AguENoyezAbZbxo95UEqX-L-VyumUwOz_HU9-kBFqvDQ4NPSBsVmBP3aDdrsR40LvtyQ1ul63NEsKKmN_Pbb1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده های SU-34 صفر کیلومتر نیروی هوایی روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/131843" target="_blank">📅 09:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131842">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
پوتین به ترامپ زنگ زد و ۲۵۰ سالگی آمریکا رو بهش تبریک گفت
🔴
همچنین پوتین ازش دعوت کرده که به روسیه سفر کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/131842" target="_blank">📅 09:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131841">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
زلنسکی : با ترامپ صحبت کردم
🔴
احتمال واقعی برای پایان جنگ با روسیه وجود داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/131841" target="_blank">📅 08:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131840">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزارت دفاع چین: پکن و مسکو در ماه جاری رزمایش دریایی مشترکی را در نزدیکی شهر چینگ‌ دائو چین برگزار خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/131840" target="_blank">📅 08:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131839">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYRfB6SWinHUarx0nCzkeX3k8bLcHhHAw8-wuh6LKlu33Lk1EdeWoUSAmDQ3sXYQjYpmNaWyIkeTfJhJNxHba51DSIk7sn4Q1UCMAjCDPb0yBDih-XRS8iV4RgPIiYzXvThDD81r__-RtBnIJioWXt5-YLB6PiCHZ6dwGRJRnEqwXDs2XB0V5hT9rE-cIzLevjsWUFprtN0bqhMshV2PFVfrvLHsdzU8hOPepZM3B4_8x0gOftf1FAV8O29XWz9XXiZa49vMM6J1iS6PxBBtTpgI6OuBjz2MRb3eN3Fvup-cM3ZkFZM1jJtytKpe7zh9SGTXOIUCkacfAqK_2IJG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار هیات نمایندگی حزب‌‌الله لبنان با عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/131839" target="_blank">📅 08:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131838">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ:همه جای دنیا تلاش میکنند شبیه ما باشند؛ اما هیچکس نمیتواند مثل آمریکا باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/131838" target="_blank">📅 08:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131837">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
طبق گزارش ها شب گذشته پوتین و ترامپ در تماس تلفنی یک ساعته در مورد ایران و اوکراین گفت و گو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/131837" target="_blank">📅 08:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131836">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c3c08acdf.mp4?token=In4uDCkOImYxXvKeNyI3NA4eT47HT9_2HCfe2j9dIfzwcP_Dt0VBZeqZbWixHgsIMLAhAN9uAJ0xIsM8aD0_hawPM3-rLfKpbZDqKsOEDUcfrnwuDZlE8piusCMbQpgkABJ8lV7B35GJ28CZCf-BbJdfC1ENeyYtMfxp1uIi2w_ZyRdZeLK4acmFE4XmidI6WY2iKWivbh5wnjMSHJufT-pf6tJ3HhmqcFdpr1DcB65_HWYCU2fLv_Si0znIGVcL7ydbcUyMhVJupdZILufuIfcZorDIjUeOvz4_ondAwHJpo4fjqygrcQRiF6ZKFceo_tjFoANNKnNHv1jgpwu_Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c3c08acdf.mp4?token=In4uDCkOImYxXvKeNyI3NA4eT47HT9_2HCfe2j9dIfzwcP_Dt0VBZeqZbWixHgsIMLAhAN9uAJ0xIsM8aD0_hawPM3-rLfKpbZDqKsOEDUcfrnwuDZlE8piusCMbQpgkABJ8lV7B35GJ28CZCf-BbJdfC1ENeyYtMfxp1uIi2w_ZyRdZeLK4acmFE4XmidI6WY2iKWivbh5wnjMSHJufT-pf6tJ3HhmqcFdpr1DcB65_HWYCU2fLv_Si0znIGVcL7ydbcUyMhVJupdZILufuIfcZorDIjUeOvz4_ondAwHJpo4fjqygrcQRiF6ZKFceo_tjFoANNKnNHv1jgpwu_Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پویانفر
،
مداح
:
آقایون
سیاستمدار، بسه دیگه...!
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/131836" target="_blank">📅 03:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131835">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=cbQE2mHSjMKeNiAW4xpXJQ-KF81QGqvhyNLAEaSNASNs_8QxEoe1R5n70RWIeoR2H0GHfliz9eLTljncdENcVnI6NDUcmimU6nix_FfYi86HzC48sowGEPGtZ-Ya2qptoGl4M6fD5fC5Lgq-thySBFigtM_qAPeEhIc2s23HMVgMTeOSzrsvKq7_NDZs3oTwqqqIQv7-0ts0ZjgXrnmTz8f6WTk5COuSCL2ivWMVy85KbagnDPmx33OaXyZvbF7yFt0GERaX2mKlF7CLbvNSe_YcCqTa1Xiyqts14l3Vh54jLmhXUz51tNuL4yABNSbt21j6C-Az8L-N2KsQj9JkrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=cbQE2mHSjMKeNiAW4xpXJQ-KF81QGqvhyNLAEaSNASNs_8QxEoe1R5n70RWIeoR2H0GHfliz9eLTljncdENcVnI6NDUcmimU6nix_FfYi86HzC48sowGEPGtZ-Ya2qptoGl4M6fD5fC5Lgq-thySBFigtM_qAPeEhIc2s23HMVgMTeOSzrsvKq7_NDZs3oTwqqqIQv7-0ts0ZjgXrnmTz8f6WTk5COuSCL2ivWMVy85KbagnDPmx33OaXyZvbF7yFt0GERaX2mKlF7CLbvNSe_YcCqTa1Xiyqts14l3Vh54jLmhXUz51tNuL4yABNSbt21j6C-Az8L-N2KsQj9JkrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زاکانی و برخی از مسئولین تو حاشیه مراسم امروز رفتن چلوکباب خوردن
🔴
مردم هم اون بیرون زیر آفتاب، صف وایسادن تا غذای نیم پرس و تخم مرغ آب پز بخورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/131835" target="_blank">📅 02:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131834">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
کابینه امنیت ملی اسرائیل، احتمالاً فردا عصر تشکیل جلسه بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/131834" target="_blank">📅 02:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131833">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a14033e54.mp4?token=lSpoovZkElRNnnEorEnqln4hj31cfpGguiIoQIiBD-h9F0KuffHUvSVfwCcLh1QxAH3yXKasy2uPI5znAMlblpIM7MZTJ-9be93xcckn6pYxGKm0QjzfBMxMW5LvdtLoq3-czTV0iMB6OTyR69GCmGwS-ON3Dhew4we2OgdkkFa9i2j-ZTfIw89caWPG0_aBuuLW5F_XfEJwTaN6hQSNeWbkAPrWcZf8Gy_PzJhVt0tU4ltOPNcghuM8cokOdOX_HihfSa-la3S8FhWL3EJHmqdQsianm7TTTQ8rD96luVAxI5A6D5uJ-RxD4cznqp1CNdn-bmV9BQc80yLXhF9N6BQWjXzKW9QP_06hgGLFB83dmIqta2QBYYqJxg16sqI8LBUyLTUNdFrj0lE3ZFZUzEzusUQpxFQJYfYEBuWoUgGXhqAPhgi0TZYcHdun7ONpKtK2gYszL2rZQHrje9ft21QwMYn9_PWxl6EJFa2bZKWv5rv7a6D-6m-wyeAM9JBVRTjXwRdmzhrdDmpK-uZaVw1keZl2fcCoIj4WaRjrz8LA6xM7RD7-36W4nvnOVAZU-ppJr2VeZrMBFsbeRiWku2N7ZV65tL6xFv868B9p7_PMOrAFqU72SfQAXhWGH2bHcdKzoWdQBPER6JHJo5foIl5Zg24-YRb8jtV2_hZxKsE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a14033e54.mp4?token=lSpoovZkElRNnnEorEnqln4hj31cfpGguiIoQIiBD-h9F0KuffHUvSVfwCcLh1QxAH3yXKasy2uPI5znAMlblpIM7MZTJ-9be93xcckn6pYxGKm0QjzfBMxMW5LvdtLoq3-czTV0iMB6OTyR69GCmGwS-ON3Dhew4we2OgdkkFa9i2j-ZTfIw89caWPG0_aBuuLW5F_XfEJwTaN6hQSNeWbkAPrWcZf8Gy_PzJhVt0tU4ltOPNcghuM8cokOdOX_HihfSa-la3S8FhWL3EJHmqdQsianm7TTTQ8rD96luVAxI5A6D5uJ-RxD4cznqp1CNdn-bmV9BQc80yLXhF9N6BQWjXzKW9QP_06hgGLFB83dmIqta2QBYYqJxg16sqI8LBUyLTUNdFrj0lE3ZFZUzEzusUQpxFQJYfYEBuWoUgGXhqAPhgi0TZYcHdun7ONpKtK2gYszL2rZQHrje9ft21QwMYn9_PWxl6EJFa2bZKWv5rv7a6D-6m-wyeAM9JBVRTjXwRdmzhrdDmpK-uZaVw1keZl2fcCoIj4WaRjrz8LA6xM7RD7-36W4nvnOVAZU-ppJr2VeZrMBFsbeRiWku2N7ZV65tL6xFv868B9p7_PMOrAFqU72SfQAXhWGH2bHcdKzoWdQBPER6JHJo5foIl5Zg24-YRb8jtV2_hZxKsE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های
F/A-18E/F
و حرکات نمایشی تو واشنگتن برای ۲۵۰ سالگی آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/131833" target="_blank">📅 02:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131832">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WL7B3E1UWckhzDDz3vjXBWKUczP7TpCBRunw3wcpZybsgUtal26qKycahwi0P63H02NFn7tgjmvntMzVWajjgwMtj7nf1IgQxo6gwcFOuQRuLXhciSz-_uAB5648JDdtN79yKkdB50fWAOAA92pYfCMkTdEFxWmGHYvPaXx3ks10QxGYpDSXhZelFfMRXQSCmOX4WdKLcLJdEzohR5nJKHkU7bZD6KXl5FYg4kyzmbJDOuzUN_vKxrGo_SrTs4-ApZ09xXB3yDLC6P2yXxBiKyQnSOOQsfUSGFkv0zpQzhTeg1orrndTuxr0_VVkZSzb-DVU6E9IFON2yFvr-hAxpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا کامیون حمل پیکر آیت الله خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/131832" target="_blank">📅 02:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131831">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSU1OAp0c65ujxU6MsMLg3yymXO-qh-ktQMKDVTabMr6vj1Yk4dgQ7pNAKtdmrPc0oD0OSXpoaLj1-ajFydQq7L5DH_cG3te5SDpNO9eAveDU6DclQ5PclCLv0fnl55s3Lr70RQkbLt6dWVnAKZ7HZlJUlfuYDwO1hXlKNPtaFe7op3GC686VYdhc8KP_pSIXsI2ng8PMPcffB7TIQwVI5g81ZNJmjU7neJy9HBw1I1_NIR5kMRu6IEkg4zebX3y_WeNRQghMEF1gdXBnaBn5UXicnkKPYbiNLxtTBgYm9gjpwPfut2pvxXOEQZLJtmuO_zf9HKdyWgb5BQW3pV5AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوستری که برای کشتن ترامپ امروز در رسانه ها و در دست مردم حاضر در مصلی دیده می‌شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/131831" target="_blank">📅 02:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131829">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf04045170.mp4?token=MX391appIbVFn0umAHxRXVEVe03nxB_HtpZt9zRWAL10Sr-Fqe41sOkyYVGmhOm39kN8mqcrqEXOni9PUFwUkAL8iyLXFkNRM1TWNVdmyeQutDHCjkqImgUoXV1OQ52n-W910JZ5yL8HiHH5btMH7UZZ-E3Cf8PE1cnRV_4vue_gpRzlOcuiZARS76FEiks7TJIiWIZKGR7b6-IvcTWlrwx7pNFhKqLhlKunlJAjHIwX3Pq0Gt64e6X1aoBqRYWC5d4Hfhic0WVclm8oh5zKCqP5dG0gOKU9pLbwMhekpfd0jiG-LO6ke23BEZfE-aF2UN8lZkGZTACfRNLK0CHVsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf04045170.mp4?token=MX391appIbVFn0umAHxRXVEVe03nxB_HtpZt9zRWAL10Sr-Fqe41sOkyYVGmhOm39kN8mqcrqEXOni9PUFwUkAL8iyLXFkNRM1TWNVdmyeQutDHCjkqImgUoXV1OQ52n-W910JZ5yL8HiHH5btMH7UZZ-E3Cf8PE1cnRV_4vue_gpRzlOcuiZARS76FEiks7TJIiWIZKGR7b6-IvcTWlrwx7pNFhKqLhlKunlJAjHIwX3Pq0Gt64e6X1aoBqRYWC5d4Hfhic0WVclm8oh5zKCqP5dG0gOKU9pLbwMhekpfd0jiG-LO6ke23BEZfE-aF2UN8lZkGZTACfRNLK0CHVsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله مجدد تندروها به قالیباف
‼️
🔴
تو چرا اسم بچه‌هات ریشه یهودی داره؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/131829" target="_blank">📅 02:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131828">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEJrXPeQI_Tb-lVHYRVWozaPZI5wW27WfUYKOgpwtlEnnNPLy_cBwLSeYeG38foe6L-lQacO1xgFDF6z40Fh_IJy2qwx7GStwa6SbIruxFmbPOIptZ4khHZ-ngFRj4Cxl4g0-T9nrBGrQlkct9zTIdBGcuS-_UgOn2UWZh0w88wYo6b9ghLqRrpSX1UZr7IQ6D2dZVwHshgNLKtAruCleDw3kakXw_hYizFquMk7-X8QjN6NGGed874HMMxAoyEOCiAGUaelZ_noinE1-ES80kamEZjBGHDP-kovmj83_iz45ogd5pcSj9BhQJw1thnCoN3m60obyQep-Qa9xYeSxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: مجتبی خامنه‌ای در تلاش است تا در تشییع پدرش شرکت کند اما مقامات امنیتی مانع هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/131828" target="_blank">📅 01:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131826">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/131826" target="_blank">📅 01:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131825">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2bbcff1e.mp4?token=TmFzpt4UXSzojtuQ5V6iO41UBhxZzkAHBhYE6Dmyy0tzVgK_IgtZm8fJrokxbJwmeHVMcTFZn6UHu1VjtWHQ7DNY6e_jPF7uidtxQjbJdfyojThKSNQ9rM9a_Qsirvrg2sNJHoKciJ9IA8Ni0t99uyVe9jnDDhjA9nvECjupOFygYFec5q1qmwyqq54981qyqWOFOW4Cg0LsBC3obAKzwWLx6aoTKAIxWEyrSNyOjyEJKmYk2ZIHbsrAJeIvGgzAV2osraccHaVra28PWqwuqF8-kDTK-R7pxYbpEck0wlAqUpSkeIjy91LzYUailcLgtoWTLQKYwxW5c2wskVzjdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2bbcff1e.mp4?token=TmFzpt4UXSzojtuQ5V6iO41UBhxZzkAHBhYE6Dmyy0tzVgK_IgtZm8fJrokxbJwmeHVMcTFZn6UHu1VjtWHQ7DNY6e_jPF7uidtxQjbJdfyojThKSNQ9rM9a_Qsirvrg2sNJHoKciJ9IA8Ni0t99uyVe9jnDDhjA9nvECjupOFygYFec5q1qmwyqq54981qyqWOFOW4Cg0LsBC3obAKzwWLx6aoTKAIxWEyrSNyOjyEJKmYk2ZIHbsrAJeIvGgzAV2osraccHaVra28PWqwuqF8-kDTK-R7pxYbpEck0wlAqUpSkeIjy91LzYUailcLgtoWTLQKYwxW5c2wskVzjdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قدرتنمایی جنگنده‌های ارتش بر فراز تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/alonews/131825" target="_blank">📅 00:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131824">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f30f9eab.mp4?token=fY38lD_o5LH1p2n3IiJp5WkY_IC_x8FLdGgZbObVNcjIZSX86aYiYqqHP4ZegI2zBxX8d4aOQFPrT2pZMTB_R4pA6nb8D63lSKXSxHbyFjMEKqOYCjhA1_DRt8Kh5L3Miec_E751vgBCR6aTRq_LFloVZLg98SfB49QVrmqQXEVPgecBhCRKzDOOAz7V8wjYd3OhwV6OTaqBxjcFd8eKMaFwdBCGgdzqTFq9ZAN5Y6LWR6Js3kKEc9F0NyXiRRs2wOCUdNu0aneHJKAYAmK2w9__1ScJo4HKzsrWPlhKk_7w5NFQbZg6wKkGVNT6QLAktWgt2yjDFb7txRK9K5S0Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f30f9eab.mp4?token=fY38lD_o5LH1p2n3IiJp5WkY_IC_x8FLdGgZbObVNcjIZSX86aYiYqqHP4ZegI2zBxX8d4aOQFPrT2pZMTB_R4pA6nb8D63lSKXSxHbyFjMEKqOYCjhA1_DRt8Kh5L3Miec_E751vgBCR6aTRq_LFloVZLg98SfB49QVrmqQXEVPgecBhCRKzDOOAz7V8wjYd3OhwV6OTaqBxjcFd8eKMaFwdBCGgdzqTFq9ZAN5Y6LWR6Js3kKEc9F0NyXiRRs2wOCUdNu0aneHJKAYAmK2w9__1ScJo4HKzsrWPlhKk_7w5NFQbZg6wKkGVNT6QLAktWgt2yjDFb7txRK9K5S0Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه زمان کوچک زاده تو مجلس یقه جر داد که من به عنوان یک ایرانی راضی نیستم یک قرون از مالیاتم جز غزه خرج جای دگ بشه
🔴
بچه‌ها شما به عنوان یک ایرانی راضی هستید یک قرون از حقتون اینجوری کف خیابون ریخت و پاش بشه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/131824" target="_blank">📅 00:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131823">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
قالیباف: اسرائیل رو نابود میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/131823" target="_blank">📅 00:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131822">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNEM6XpN8zVhxVUosFHA-Pdp9MPsp8AhV3_K5lMtYbsHk7BuaEs-aoCdjOEoqLE2hWWvbm9Qen1xOyvjxNlZZZ_Uzyv3cGTkHrAs2-JS-2tEheuAwbCMyl17oOv6YHEHlSCnb8Zc2koBUjW5OHzEHoOcHBVBDvp5HyrA0XoXH0kja30eTpHjw0f7VeiRJSLsswPpSkAIb8KdouE7XIum-0Fp3_fgU4M0KiV-sXc1Ns4N4FNUkcWaDucL2O2qif5rPRxkeeZdkuBpdauxttpRKH-dkigwcu7r99kyhVNpWhxvwSl6yR6o_VyAmagASrkmXoVaY63ZyVYBMCn96t6KdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیشترین چیزی که ایرانیا تو ۴۸ساعت اخیر دیدن
🔴
هر ۵ دقیقه پیامک میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/131822" target="_blank">📅 00:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131821">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7e4c4447.mp4?token=nYkzbBoT1WmLATCkFQ5UQ7ITw1icSBmrnv5qeGaRNYVcx_7AqjqDUy8Y3FanVr_FGGwEVPQxYkI7cMUXF8eGphO8SLdFaFsSPnx18p8L8fkhoGmzxG9hQZ6b9KGZ9zyfMyRP4R-D_Z7JftKVnuRdDnaU-_StXr5gDp-9qRxYXUMPW-_bUYylZn4QI3xsDg7Witdwz-dvS21pcyZXHRekRZ8RqG2NYquDiqHgVSXK0ug7B5_IfUHy27MKKwyxp4wLhD80ZJA6f2znD4XrZKTGebWmJ9aoXuO2BS5JuU5LoBK-cwsuSb0WasfvzsaObpEsl9FO8WwUdkynnkPhWZ7x3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7e4c4447.mp4?token=nYkzbBoT1WmLATCkFQ5UQ7ITw1icSBmrnv5qeGaRNYVcx_7AqjqDUy8Y3FanVr_FGGwEVPQxYkI7cMUXF8eGphO8SLdFaFsSPnx18p8L8fkhoGmzxG9hQZ6b9KGZ9zyfMyRP4R-D_Z7JftKVnuRdDnaU-_StXr5gDp-9qRxYXUMPW-_bUYylZn4QI3xsDg7Witdwz-dvS21pcyZXHRekRZ8RqG2NYquDiqHgVSXK0ug7B5_IfUHy27MKKwyxp4wLhD80ZJA6f2znD4XrZKTGebWmJ9aoXuO2BS5JuU5LoBK-cwsuSb0WasfvzsaObpEsl9FO8WwUdkynnkPhWZ7x3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از متولیان مراسم تهران:
تابوت حضرت آقا، یخچال قوی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/131821" target="_blank">📅 00:10 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
