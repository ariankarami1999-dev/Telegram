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
<p>@alonews • 👥 932K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 17:44:29</div>
<hr>

<div class="tg-post" id="msg-131927">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اتفاقی عجیب در جام جهانی
‼️
🔴
گروهی از طرفداران زن آرژانتین بعد پیروزی مقابل کیپ ورد در سکوهای استادیوم کاملا عریان شدند
😐
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/alonews/131927" target="_blank">📅 17:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131925">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
شورای هماهنگی تبلیغات اسلامی: مراسم تشییع رهبر شهید روز دوشنبه، ۱۵ تیر، رأس ساعت ۶:۰۰ آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/alonews/131925" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131924">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEh8kmRRpq28HwXD78HOZhfH-0tgtdp5oNJ2gNB7CAYnfZykmJ8Fk3GXf2snl151Kx8DqR1IU7o4CwDsSlnvMVdr1RMlqWxDwpa5MqYQihNHbNQ5nvzWO1mwBNdJZq4NKug0V-B2RxAJ5BVlc8P4RNSYb__dv9Bl3nd7mN_IHH5j-20YGUzTfaa4YFSdVLGd40fi5oM64MgVqdl7BzehRXDOpLMzbuPYDQn62_Jn7-XkBd_u_qv1Wp_Qx0XXpJzPhsol64nEYL7BzzMTB1SpuPQboDj74Iolixc5K3KCraVgloupDDIAYPyeS9Rm1fy3RQs5ykxjue8HlyLeJ4R23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/alonews/131924" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131923">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/131923" target="_blank">📅 17:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131922">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/131922" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131921">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDMFeM2ZZrpY3EwazNnsULKQIPgBen_Ya71PTL1DNBTtr7ixOkUIUruXN_HkgaTLx3m6Dtuwd0uHYSh1J3r-9knPRzbs1r7ShE5KZAV8cxtQCFw_Zav6LNNodJQr9tkpmdG2Py1EkarSDmAdXAmEivnnslDfbrmYUgilkirjfSTN16WP_ocXNkOrwSQ98IGSvqCoCT7cIERV6itlw-isZo7br_T_i__66mw20KPHeDV0V-NuwW86dz_G34-yORtYZmLmX54Q9Zp4NyifEyEyT2HXPiCUm9LDTA3nbkJ6LJB9_0WsAIDaLT9Y_Nlryd--G-z_i_280WhdE8A1Gg_YnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از حضور سردار وحیدی در مصلای تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/131921" target="_blank">📅 17:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131920">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/131920" target="_blank">📅 17:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131919">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJFlSgNtZZWUcbqjK178pYCYnXHEaQS4zuk9JMuJM9M79ZeKPM8gHvG_-G3KeOBnjIOfsJlNeu2xOh-12vrl5Cwt9IO2BELuQKzgUG_SITvqyuy0r3oAI_ikc7eWbNnPG5ot0kx3jKAd0RMYGiCHZUwulpLd5wPQf7R6Yuj3TAB3iTz-OO1hF1O0ZfdUsM6UqsS4MOcSSYvRGGqG3M46C3CLMfpTfpZ5p9Z9pYaYMWrZM2LsoToZKYWUJCmb-NlRdYnrdhGdtEpFcfMM-C-gYGJWSuGfQobbUCuVARJvKgKj2L8CHaI-HOrvPDVmwQR-ffRWEAYOoGaZNuAV8C_Qtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر برگزیده رویترز از زمین لرزه ونزوئلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/131919" target="_blank">📅 17:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131918">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ : ما بهترین بازار سهام رو داریم، واقعاً عالیه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/131918" target="_blank">📅 17:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131917">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
فارس: کارت ورود به جلسه امتحانات نهایی، تا پایان این هفته منتشر می‌شود. امتحانات نهایی قرار بود از ۲۰ تیر آغاز شود که با یک روز تاخیر از ۲۱ تیر آغاز می‌شود و کارت ورود به جلسه این آزمون هم تا پایان این هفته منتشر می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/131917" target="_blank">📅 16:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131916">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
یائیر لاپید، رهبر اپوزیسیون اسرائیل:  اسرائیل باید زیرساخت‌های ایران را بمباران کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/131916" target="_blank">📅 16:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131915">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
از سرگیری تجارت دریایی ایران و قطر پس از حدود پنج ماه وقفه
🔴
رایزن بازرگانی جمهوری اسلامی ایران در دوحه از بازگشایی مجدد بندر الرویس قطر به روی کالاهای ایرانی و ازسرگیری تجارت دریایی میان دو کشور خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/131915" target="_blank">📅 16:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131914">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فرودگاه بین‌المللی بندرعباس عصر امروز با فرود نخستین پرواز مسافری از مبدأ مشهد، پس از چهار ماه وقفه، رسماً فعالیت دوباره خود را آغاز کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131914" target="_blank">📅 16:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131913">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
بنیامین نتانیاهو: بازسازی غزه بدون خلع سلاح و غیرنظامی‌سازی در مناطق تعیین‌شده،امکان‌پذیر نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/131913" target="_blank">📅 16:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131912">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نتانیاهو: ایران می‌خواهد ما را از جنوب لبنان بیرون کند و آنها سعی دارند به ایالات متحده فشار بیاورند.
🔴
ما به خوبی از پس این فشار برمی‌آییم.
🔴
ما حفظ منطقه امنیتی را از دستاورد بزرگ خود علیه لبنان می‌دانیم، اما آنها سعی خواهند کرد از هر طریقی، از جمله اعمال فشار بر دولت لبنان، آن را تضعیف کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/alonews/131912" target="_blank">📅 16:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131910">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131910" target="_blank">📅 16:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131909">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
آلن آیر، عضو تیم مذاکره کننده آمریکا در برجام: برای مذاکرات واقعی میان ایران و آمریکا، باید به گفت‌و‌گو‌ها زمان زیادی داد
🔴
به افرادی نیاز دارید که بلد باشند همه ۸۸ کلید پیانوی دولت را بنوازند؛ کوشنر، ویتکاف و ونس؛ این‌ها سرشان شلوغ است و مشغول کار‌های دیگری هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131909" target="_blank">📅 16:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131908">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131908" target="_blank">📅 15:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131907">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCTsZBB9a2rQaXwTxwVxTN9OClZLCzOtrH1R8tgCN03mmaPhwRVPn5ZtIMrX_5kSnQ-Xkp0WRzDW8dQLD1o1YYmkTfh1W9iGTVcZVmA--p9T0YND-Jsv7VkVoMaA4S_6wm8vx7avjqq6EF_fATyCKwJst--qrAXFJKnlg4jzxBx7KwPuyITPn8_JfSA2X-5vqqW8O1IhoAxEuP-mOk1C0AcQ2GNlUPW-m3RY6HmxPPcy2AZbbhGiRpb42c9RiYy1oUrYgAefbRbkg3sYOzMthGQI_SR7T--4urJ6X18S3PlXNai20UkBXE1V92sjNejAlqbnmFfMtAQ7RdLLKS0GVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی در سواحل یمن مورد حمله قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131907" target="_blank">📅 15:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131906">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
قطر، تعلیق موقت فعالیت‌های دریایی را لغو کرده است، که در نتیجه، تمامی فعالیت‌های کشتیرانی و عملیات دریایی فوراً از سر گرفته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/131906" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131905">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ریاست‌جمهوری سوریه: امانوئل مکرون به‌زودی به دمشق سفر خواهد کرد و یک هیئت از سرمایه‌گذاران فرانسوی در این سفر، مکرون را همراهی خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/131905" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131904">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FidBA8KGjMSe9J13ACTRnkh1r3bjppUfYFMLBa89LmSXACwylTQfrke-QOT6dsPltQnJlIC2J2p3oO5q6KWQpbn3cL5Zyu6efD8s4jrYAY7ZcM46QSDK1Tg9VYl-QNAqBINcuwpyXxiVd9yiw3ZrNwIQb0GbqIv4pmkfhcol_Y63RCted6-c4Co68SOfiEtF3eVWYi5FpPqzufNjr5LUErmM7PyyyccIjpmxOJIUslEcKWn9ssA-dQixWG-S6WyKIwN5rTFKBoPHWmWi7teut0M9c2TsnpBCbE8-TIhGImZInSLO-ov_omPKFk9R2gk6ZKxxVLwohEGfPSea7N8Xeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست ترامپ در تروث: از زمان آغاز جنگ در ایران، بیش از 273 آمریکایی در شیکاگو هدف گلوله قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131904" target="_blank">📅 15:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131903">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل: تهدید ناشی از غزه برطرف شده و هیچ بازسازی‌ای در این باریکه بدون خلع سلاح انجام نخواهد شد. به ساکنان غزه آزادی انتخاب داده شود تا میان ماندن یا ترک تصمیم بگیرند
🔴
ترامپ از ما نخواسته است که علیه تونل‌های حزب‌الله اقدامی نکنیم و برای باقی ماندن در امتداد «خط زرد» در جنوب لبنان، مشروعیت لازم را به دست آورده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/131903" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131902">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سفیر ایران در چین اعلام کرد تهران پس از پایان دوره ۶۰ روزه توافق اولیه با آمریکا، برای کشتی‌های عبوری از تنگه هرمز هزینه خدمات دریافت خواهد کرد، اما کشورهای «دوست» از شرایط ویژه برخوردار خواهند شد
🔴
رحمانی فضلی گفت ایران همراه با عمان در حال تدوین سازوکارهای جدید برای تردد در تنگه هرمز است. او تأکید کرد مبالغ دریافتی «عوارض عبور» نخواهد بود، بلکه هزینه خدماتی مانند تأمین امنیت مسیر، نظارت بر عبور کشتی‌ها و رسیدگی به پیامدهای زیست‌محیطی تردد دریایی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/131902" target="_blank">📅 15:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131901">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فارس: قایق‌های سپاه 6 کشتی رو از تنگه هرمز خارج کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131901" target="_blank">📅 15:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131900">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131900" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131899">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
روزنامه عبری معاریو در گزارشی مدعی شد که دونالد ترامپ، رئیس جمهور آمریکا، برای برگزاری یک دیدار سه جانبه در کاخ سفید با حضور بنیامین نتانیاهو، نخست وزیر اسرائیل و جوزف عون، رئیس جمهور لبنان، تلاش خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131899" target="_blank">📅 15:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131898">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131898" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131897">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل: حزب‌الله از توافق ایران حمایت می‌کند و توافق ما را مورد حمله قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/131897" target="_blank">📅 14:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131896">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سفیر ایران در چین: کشتی هایی که از تنگه میگذرن باید هزینه ناوبری بدن ولی برای کشتی های چینی تخفیف و ملاحظات خوبی در نظر گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131896" target="_blank">📅 14:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131895">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjYhZRS2ZDfmDXNBuL-Kkaz2L1Pcg_uiRHndrIi4JpKXqcNbY2qW9WNAo7nWsfsV0ISzkb1bg6nt6PwPq3KmXrffZkFfdfjXe6FFGUqeDRad3MnTvHYm3UgXbZN_mAxBCxmhZuJ6CueM40NtuFaR5-eaPnvd5K-wSLada1-AXaGEOLeh0zMU2pFG3QlHemBLaVbmgmxRk-sgFMjZbHyaONdb_OZqkvHN1iHGKaorraa-mEhqVKXKtkDxI6kaRGuiXMCGMBQ_RpHJKdGnhlhb_FK3Q2VuWj0beVG_dQ_qc8FX0qHWVRw0aDXbTHE2r0cnSxodXA9pJxy5_vqgAxAHCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده در مراسم تشییع
🔴
خواهیم دید چه می‌شود...
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/131895" target="_blank">📅 14:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131894">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نتانیاهو : حرف‌هایی که درباره درخواست ترامپ برای حمله نکردن به تونل‌های لبنان پخش شده
🔴
کاملاً دروغه، ترامپ اصلاً چیزی رو به من نگفته
🔴
منم چنین درخواستی ازش نکردم و ما تصمیم‌هامون رو بر اساس ملاحظات خودمون می‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131894" target="_blank">📅 14:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131893">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
محمد مخبر: قاتلین امام به مرگ طبیعی نخواهند مُرد و نظام انتقام خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/131893" target="_blank">📅 14:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131892">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/131892" target="_blank">📅 14:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131890">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
مدودف: ایران سلاح‌ هسته‌ای اش را حفظ می‌کند!
🔴
ایران به جای داشتن یک سلاح هسته‌ای واقعی، متوجه شده است که سلاح دیگری دارد که از سلاح هسته‌ای ضعیف‌تر نیست، یعنی تنگه هرمز، که وضعیت بین‌المللی پیچیده‌ای دارد. ایران نه تنها این سلاح‌های هسته‌ای را حفظ می‌کند، بلکه یک سلاح هسته‌ای حرارتی نیز دارد که همان تنگه باب المندب است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/131890" target="_blank">📅 14:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131889">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnfnWbxC785ei_68b1wEuv3hpJ2QXVutyznogvXaCZd1kCD056r-0_wfY5bg3YleqJn-jTQAKFkglO-iyaxDAvH9Z6q9j1lT9tIJ1u9KQHKzSeCnWZY2MlbIYxIB6qbOUtDp0_-nlx2E9LSqAPfAHclTsu3wqVkbsqrUlAJjRYdElWKYvaoKuW9qtx14CNewe2SryTMTkCc-oX4kuLPLG4t7_OHQST8TQkJXqCnPrCBJD8pw0hbujDknhJlY9e6EQVL4_PGppBwRg29kc65Pghca_Ce9oEem_EzLLk0Egv1IC6U8fcQo3wthHJeeOJ5OWA_qMB2Z3ajHb4LeK4Osdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیرخانه شورای عالی امنیت ملی:
این چند روز چشم‌تان را به ایران بدوزید؛ این همان ایرانی است که خیال می‌کردید چند روزه می‌توانید آن‌ را از پا درآورید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/131889" target="_blank">📅 14:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131888">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
خودروسازان چینی با رشد سریع صادرات و استقبال بازار اروپا، برای نخستین‌بار از نظر حجم فروش از رقبای ژاپنی عبور کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/131888" target="_blank">📅 13:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131887">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
شرکت بهره‌برداری متروی تهران: از بامداد تا ساعت ۹ صبح امروز، یک میلیون و ۳۰۸ هزار و ۴۴۵ مسافر، بیش از ۳ میلیون سفر در متروی تهران داشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/131887" target="_blank">📅 13:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131886">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
به گفته برخی منابع در اسرائیل معتقدند احتمال وقوع یک درگیری نظامی مجدد با ایران در آینده نزدیک وجود دارد.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131886" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131885">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
دولت ژاپن در حال بررسی کاهش سطح هشدار سفر به ایران است
🔴
در پی بروز جنگ آمریکا و اسرائیل علیه ایران، وزارت خارجه ژاپن سطح هشدار سفر اتباع خود به ایران و 3 کشور منطقه را به درجه 4 (تخلیه فوری) افزایش داده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131885" target="_blank">📅 13:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131884">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2zbfMIwEzlvTDY-hHc7Xx5I5kgbTYgTk-oAchVgymVAEHb95OuwnD7yZOF9QMrNjxtpOe7VOYNBv2ixcq_ITohhnZcKRSo9gasOinBozkDbIYNYaniG9ZAs_pVtlabBcGqm-0qsYY7M9my8hv6lAF4GDlgDtvzMByGDWItZM99cjVjXCjdQysN9Mn_Ust2fJzd09nppSsyeAJycegWdHpItYhj-CBPSORCt7Baeb8SVibviaJRlVh3Xm_6jfR1K-Vf2tZBbsNjuGKkWAJoRiRDZdyajJJPXUQMzcCdyNLPU4j4JQuBRfl9ghdtlNqQEI8qV9aQTLDcd4zYhUYm_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت آزاد کشمیرِ تحت کنترل پاکستان
🔴
با گذشت یک ماه از قطعیش، هنوز شدیداً مختلهِ - Nut blocks
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131884" target="_blank">📅 13:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131883">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
تلگرام از مرز یک میلیارد کاربر فعال ماهانه عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131883" target="_blank">📅 13:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131882">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
جوزف عون، رئیس‌جمهور لبنان :
من علاقه‌ای به اسرائیل ندارم، اما راه حل دیگری را به من پیشنهاد دهید که ما را از این جنگ‌ها بیرون ببرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131882" target="_blank">📅 13:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131881">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
العربیه: ترکیب و سطح هیئت اعزامی‌ایران هنوز نهایی نشده و پس از پایان مراسم تشییع، تعیین خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131881" target="_blank">📅 12:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131880">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zqy_hUPeAHlccVQL8S4HliAT1pN4MIeVRtmmdu16KSqsBIpviWP5gnENeerkDkQVk3NwoDoS_ypZG0Sga_U4-EYeyfAxi3bSqrMMXEtMuzC89MbS5iIt0ZTmOZ1WoDmbO6lAlWvRlvlXOkvpECYLVzZZU2g4KHBYuv5SgrLjBOLn9OQktJMBPhU__wi7i2D6UaJAucP3GP2OetKpZNJM15dcGcO4J-F_oiiiVvqolNGnpMH8t8EcdPYaBHw8DvPUh6dCWyLAoxjkB_SIbv88OpQqidevB6GlPTeKcUSx1L_ehN2UeHAxpOm1zAa56d6MJC1xmmdTVE14jrQ_Yq-ejQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکایی ها مجددا یک گروه از نفتکش ها را ردیف کرده و در حال اسکورت آنها به سمت تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/131880" target="_blank">📅 12:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131879">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سامانه گنبد آهنین به امارات ارسال شد.
🔴
میری رگو، وزیر کابینه اسرائیل مدعی شد که اسرائیل سامانه پدافندی «گنبد آهنین» را به امارات متحده عربی ارسال کرده است.
🔴
وی همچنین ادعا کرد: اماراتی‌ها از ما کمک می‌گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131879" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131878">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ: نتانیاهو احتمالاً هفته آینده به کاخ سفید می‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131878" target="_blank">📅 12:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131877">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سازمان دریایی بریتانیا: یک کشتی باری در سواحل الحدیده یمن از سوی افراد مسلح ناشناس مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131877" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131876">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل از حمله هوایی به غزه و ترور دو عضو ارشد حماس خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/131876" target="_blank">📅 12:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131875">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
استانداری هرمزگان: احتمال شنیدن صدای انفجار ناشی از خنثی‌سازی مهمات در امروز وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131875" target="_blank">📅 12:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131874">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
دعوت رسمی از ترامپ برای سفر به پاکستان
🔴
آصف علی زرداری، رئیس‌جمهور پاکستان، هم‌زمان با روز استقلال آمریکا، به‌صورت رسمی از دونالد ترامپ، رئیس‌جمهور این کشور، برای سفر به پاکستان دعوت کرد.
🔴
حساب رسمی رئیس‌جمهور پاکستان در شبکه اجتماعی «ایکس» اعلام کرد مردم این کشور مشتاق استقبال از ترامپ در اسلام‌آباد هستند و میزبانی از وی را مایه افتخار می‌دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131874" target="_blank">📅 12:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131870">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MrnNjYBF4klNQ2r_8wS-chlSSCZdTnwZCf6dZUT71TTpNYkm7hBQEIroJQriCQz88GqYFNtQTMcdx-v4PjMxdMVanYr51ZufK_h6eE29mEOyw3BdaIrCRGObbU__FRGRDhdlsJiuqketDWa_Rom7WR8V54swI8DwXtDtsSixp0GR8GF0kuIJ-9xMUaLDJWkz8s0HbsKIzYMcGkThltQ0VFWtMJxqMygNE8xmgIkVo_SGeBeuREVj8VoVK0OaSJSBSi8xVHKZf4HLqMMS62-OuuBix69IppiyeCusoW911lYJNMaaxRPFTNR1CSYS39aGuRoE_5Hf6QaoGtJdfg_41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJX4itClcFmxRFYqW9tj2QPzHweYhvLcUSPOPTLJlX3qlNyeKo-ZYZjmwCNzeqEWqNbodzmsnV3EmQoaNcM6G3II2U1TJHrb_dNvCzF9YdUNZA6oGLGddZ5o24wmd0ZHXNfzOUqetHocEfvWoQFPsdL4of6YyHax1RmJdF_U7upQcRXZTQMBJeRjXkokKY4MRsGSKgMCyLkzpGjOpMbMFZ2EjnA2A0K-3Eywv3JhAwYipbKV72VSXtI4_fEdjsG1-gMasottrgcrydcEA3Hl8qu9IWO2dNoW4ERCKFJ_yQQhuT6oHZ8QCn_vf7eyOhcF4p-Hr1-IF-pPR19GnAaMDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBjZJcOfJiSmS8NbXdKjl6VPHJTN-tZ0R4CV6qoDATx3Py8VIsGg2koU-UqJEBo_8_25o6ND5SqCwmqM366txaj4SZWqTiVgdsIA5eygcDH72g5O7XQtLF4qQxhH4w2kcKk2DkAHhkLtZF8zcfwJQwR2LSe07JJzsLEtbzu4LK9lclK3gD8V5x5BsOYXXef1up7Ow4027z8f1krJWwFHTqVciTufBIOU1z4enXRJE1PsbAW0SeItGVcSMp-lVGr_id2iSQ9Hjlsyp56L3e5x7mDdWPthuKZ_OJKZKU1L5vxTW_4wpKmU4nwd0q8FcZ3HwWAITaTGKP25wdArKggNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEOiTm4hxRWKpzsDA_PN5hQQGZT9byzpa6C8wJIBYY1LfC1cH8o3KmPwLv68AwB4TSo_GWmPSHA1DjyVLw3_dnGe4U_n3FHngHFWlY3WW8-A8d_xnWF-S68mlh2KjuFkPNKjmxHEMNbOJmdYqzI0_tMdoc-aQVp-jfxDQsHTYACI3L3uvIabxPpia4TK1vignHYMYAXXWo0koVpiYszcVTOgWWmBlFH6wnQlgPvwScBnxVp8XmYWPt2LY9Obkh3cG99FIwBILBArnCKf7o1Jo3jSVfEyyEVRWltlRwGo6fZpN8T547N6nKN1oDDOjioxVNwkYdG-q9VAxG1Nj6l4ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کیم جونگ اون، رهبر کره شمالی، از آزمایش‌ های موشک کروز استراتژیک و سامانه‌ های پدافندی ناو شکن جدید «کانگ کون» بازدید کرد
🔴
این آزمایش‌ها که جمعه انجام شد، شامل ارزیابی سیستم‌های شناسایی، توپ‌های دریایی و جنگ الکترونیک بود. کیم از پیشرفت تسلیحاتی ابراز رضایت کرد و دستور داد تا ظرف دو ماه آزمایش‌ها تکمیل و ناو به ناوگان اضافه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131870" target="_blank">📅 12:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131869">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
اتفاقی عجیب در جام جهانی
‼️
🔴
گروهی از طرفداران زن آرژانتین بعد پیروزی مقابل کیپ ورد در سکوهای استادیوم کاملا عریان شدند
😐
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/131869" target="_blank">📅 12:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131867">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIUvDyJJoqo29hI73qqwT0ciR6GLPEnnIH93Zet_58DvTgmirTccGjy5mnMrSkJA7e7CQaYMUk_B2d3W-RpK5gGrvm6gExEZJxA-D_ec59InOu1Sb70unOcV0bjv3yC2xNUVRrJYPVL_9nY8aKxCHITNPzWCEWiKrSe49WX5D3wknwQooApFuDxkPeBuMFA5mS9Pqhk6RkMaB2oJYDPBMgJ1zv8sNSBIWvutV6MMlFHu0LpacAXD1UJEU_VNqzpDUnz8a3p4HL12v3Eec2iWJYrMLlZ4Px6KK7O0O0YDzAAyfITgOuerdaxKb-iJvRAvK3PL15BQ4cVH5eDn0Reayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YxILHJXPyHHyEAJSTNm6HgfLH0YusLEni9aPTcfWddGi31wdo2D_hgrfxns7MktSHcPqsE_rO357lceB7bxm9lX4ZmUeoU0mQfguCYvUIoebyodplsck8w9grStvFal5Z_sMQFVJEVTPUjMCloJTRfXXfW_ZIaUv32kggFCGMgVWGz3rVlvD0JcGcrGxKzcUMEgAyBieBX7TQbg1a1TanPKh7SVB-WzsWyYnsPu2qPiOv5zbDMxIPrKOBFY4jWfZ3f_f9ZyZ5AdFourJ4I_t3KZn3R_RosR1xybcudft0XYYg_Hh-UzutYRqdA8hLX4bgQyVl_ZkrkR_aYfO5jn-ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نیویورک تایمز گزارش داد: نیروهای نظامی اوکراین با استفاده از حملات گسترده پهپادی ضربات سنگینی را به کریمه اشغالی وارد می‌کنند و هدفشان این است که این منطقه را از یک پایگاه اشغال‌شده توسط روسیه به یک کابوس برای آنها تبدیل کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131867" target="_blank">📅 12:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131865">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131865" target="_blank">📅 12:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131864">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/131864" target="_blank">📅 12:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131863">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa11f8e93a.mp4?token=WP2K35eWYK4JX4rKE2B_-Z6ycYuiOJNlGjQpjRs9sfobdhy2KQkOStuAYED4TlCtzfzHsahFIU22ijNFj-Mi5je6CvTwqVkGmGVpH9tKrNzopk_ekyXMimOEooRc-Onn6kH5i0HrDvt3fexN7TxzuXtzoxC_RmF5fwJmdaSarG8u0GVKg1m0RyztH_c5RX4ScN4cLzAZMUDvqLHtG7GXodv3jNUvTru73B4DMYZJg6LFBac0KB01_w7bz-pADRBs3c-VgjW85T6QGWTA3mCKguGANQDOhwTQLkPCV-OjasxEL_3Z8G7_dMgBsWSLjtE7ImLngmlZeN9dcdi23JZ09w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa11f8e93a.mp4?token=WP2K35eWYK4JX4rKE2B_-Z6ycYuiOJNlGjQpjRs9sfobdhy2KQkOStuAYED4TlCtzfzHsahFIU22ijNFj-Mi5je6CvTwqVkGmGVpH9tKrNzopk_ekyXMimOEooRc-Onn6kH5i0HrDvt3fexN7TxzuXtzoxC_RmF5fwJmdaSarG8u0GVKg1m0RyztH_c5RX4ScN4cLzAZMUDvqLHtG7GXodv3jNUvTru73B4DMYZJg6LFBac0KB01_w7bz-pADRBs3c-VgjW85T6QGWTA3mCKguGANQDOhwTQLkPCV-OjasxEL_3Z8G7_dMgBsWSLjtE7ImLngmlZeN9dcdi23JZ09w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر هوایی از مصلی و خیابان‌های اطراف
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/131863" target="_blank">📅 11:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131862">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
شبکه «فرانس ۲۴» گزارش داد که دونالد ترامپ، رئیس‌جمهور آمریکا، پیش از برگزاری نشست ناتو در ترکیه، با ولادیمیر پوتین، رئیس‌جمهور روسیه، و ولودیمیر زلنسکی، رئیس‌جمهور اوکراین، گفت‌وگو خواهد کرد.
🔴
این رایزنی‌ها در حالی انجام می‌شود که جنگ اوکراین و مسائل امنیتی اروپا از مهم‌ترین محورهای نشست پیش‌روی ناتو به شمار می‌روند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/131862" target="_blank">📅 11:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131861">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b32a145c3.mp4?token=Ne6v3p9NY7FPzrDLthxJTEs7CTCR1RGrdXeg1eLB0AEZEwY-vu0jXw4dWTHXzErZjPKPnP50NoEhRSzJoEyaLtIKMK9Mh705-Cu1ToPedlasA2pYmCOQwnO61XGfUIOKfx-OauDVaoAXbqij69FjFWwGoDDaz2TbTA0XA8neRVuaZOAQd9Ity9_uNTemd-ktrQLAeuc_YTOGIFv2WZdEBkniFEYMbtf_rUgTlCiJA9w2-t8IgNbmUTNVcN52Le42KuJelS2JzgRriauz6mUeClrcrfAR04PtYbAihPnuFXnCOT7tRqBlSXoMGOM2ZLCu1MulZrIoE3mUgQU_oELbzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b32a145c3.mp4?token=Ne6v3p9NY7FPzrDLthxJTEs7CTCR1RGrdXeg1eLB0AEZEwY-vu0jXw4dWTHXzErZjPKPnP50NoEhRSzJoEyaLtIKMK9Mh705-Cu1ToPedlasA2pYmCOQwnO61XGfUIOKfx-OauDVaoAXbqij69FjFWwGoDDaz2TbTA0XA8neRVuaZOAQd9Ity9_uNTemd-ktrQLAeuc_YTOGIFv2WZdEBkniFEYMbtf_rUgTlCiJA9w2-t8IgNbmUTNVcN52Le42KuJelS2JzgRriauz6mUeClrcrfAR04PtYbAihPnuFXnCOT7tRqBlSXoMGOM2ZLCu1MulZrIoE3mUgQU_oELbzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور فرزندان و داماد آیت الله خامنه‌ای در نماز میت امروز مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/131861" target="_blank">📅 11:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131860">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سخنگوی ارتش: بار‌ها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توان رزمی خود استفاده می‌کنیم؛ یک لحظه را هم از دست نداده و غافل نمی‌شویم
🔴
اگر دشمنان خطایی کنند، حتما با پاسخ کوبنده نیرو‌های مسلح ایران مواجه خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/131860" target="_blank">📅 11:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131859">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کرملین: تماس تلفنی ۸۵ دقیقه‌ای پوتین و ترامپ درباره جنگ اوکراین
🔴
رئیس‌جمهور آمریکا پیشنهاد داد که در جریان نشست سران ناتو در ترکیه، برای پایان دادن به این درگیری کمک کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/131859" target="_blank">📅 11:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131858">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXXop4WhGEKg_bzggmvx5NLP5mr3JzJJGt9j0nITMfwCer7iuZCGlv0r9ftP7xMs3u4a_CliKnwizvcneGgomroTfGUQGWbOqHpK6ExW6lixKnahky1xyv_aj2rUEMtwT0kwnYVKruhXfBhsTw5jzdykRP6zXnuZ2fw-VUU-9GgbXZeMDXhOfPD6ptfSSkZ3MtZ_lGMSNuzTXS4SjTE2iUPeygFw0HU9RN9SB1ZEXETKdnzMXX_XjR6aeDW5U_ffRKvXhX2qtYMsiZlbncFVtO6COeIsInvoQbmeL_MxbDAsRZs52TdnVFcOfUxLe1Xzl1vp5unrWQ1Etrilx6bLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هرمزلتر: نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/131858" target="_blank">📅 11:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131857">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت حمل‌ونقل قطر اعلام کرد فعالیت‌های دریایی از یکشنبه از سر گرفته می‌شود
🔴
این وزارتخانه ۸ تیر از همه شناورها خواسته بود تا اطلاع ثانوی تردد و فعالیت‌های دریایی را متوقف کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/131857" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131856">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131856" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131854">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wktpe6yI562i7Xn4EoPB1ikc_vj52RujI_33Qoz8WV_TDO8dCwalOgzAt-UMuNjsk948VVFWt183s-xAJ9lMQmBtbN8W8JNYjLvByg38L_E5gXUdnogE_o47tId86zID909U9XDiPRweODb0LZHwf1HEAPkg8RY3nJzfbe_WyRsEcyd-e6ieLLOOfN6uZ-jjSkmu8sOdel_lUxEE1FcPS_g7md0kWH7QFTbamQjdkO4KKntMiHAWePcOPmVcs96zWd6I3gf3LOCTsvKat8mjG7PjB6mQ4ArfL_Spwr_Mtx5eiQlZubam5S2j5UlKHq6rqjckWmRvNykCYaDVIPKtlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2yDVS9RhtQ4nAssYQK34KVt9eE2fyUq8i3i9VPjpIST3FaDfTcCB8KrCa9ncq7mHRlrzDb_VSku6mrf7pR4O5U2JYPUB-os_8Gm-Lke7LYiRohF0SYovXqy1cPurcrQgOeEMnjRORe-DP6GNUxscsFdkhGqZ6kTBUtu2PH3gaWkgtJ1l7xgw512xZk90uKeLVocRiNaNPZjOSeNGw1P9xtaLQcCwyjhk4pWinNuSnZvfWnKaAj2WAv1X_imvq0ZLan8tisL5v3SjV3oP6B5HsUjSyEpXkPRnIaplCOp6oebaFF6Bc9VCO3rF2ssR2BJbmX-2aSyfbG_taryBpEiJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131854" target="_blank">📅 11:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131853">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/131853" target="_blank">📅 10:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131852">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
گزارش بلومبرگ حاکی از آن است که روند عبور و مرور کشتی‌ها از تنگه هرمز، به‌ویژه در امتداد سواحل عمان، روز یکشنبه به شدت کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131852" target="_blank">📅 10:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131851">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
آتش‌بازی‌ها در واشنگتن، به مناسبت دویست و پنجاهمین  سالگرد استقلال ایالات متحده
🔴
ترامپ در توییتر نوشت: بهترین آتش‌بازی‌ها در تمام دوران
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131851" target="_blank">📅 10:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131850">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
گزارش خبرنگار ان بی سی نیوز از مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/131850" target="_blank">📅 10:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131849">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOG2P87vWSNP_WmgJwkKqCkJVeM5OXVwhgyC-poDTOYXmcDPRRhBKwy3scDJE5Y7jK8i6fGGGysB37YyNaUJq-rv8Vk3pkhqhY2ez_-Uyq5JtzoYiQze2C97t042EC_fwS1o_duK4A5uyXowIsc5rHo2_A0JB6LR4t76k2sABrmeMv0kzFOjtnE04XWfVezwvWV8vxW1Cg4kK5WK9WMBtrsA6q9bxR3aLY7hSRhgJ_p-yrOrOlkqwEbBR5LFdl85lnmY_tzYGFfDnVt-qPGr3jnlO9Pq5aXREGWoHijR3R_PTW8_DAtVXBxcUOuJCiQulG26hzkVyoVP6uPedpO6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست: آمریکا هنوز یک قدرت بزرگ است، اما دیگر مانند گذشته بر جهان مسلط نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131849" target="_blank">📅 09:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131848">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131848" target="_blank">📅 09:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131847">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رئیس شورای هماهنگی تبلیغات اسلامی: امروز در تهران آمادگی اسکان نزدیک به ۳ میلیون نفر را داریم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/131847" target="_blank">📅 09:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131846">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa2c1939de.mp4?token=dvF70D6KhDq8z2G2aZ8qO0ODXWJvWaqG12wpmjFcl3t0f8LtlEUUTsslNCql4j5uQg0Pb-ipcFJGvNNJ9SoHURf8F1rK_jIaAhfSQn-AdYdH2QJxkLEix37_vHkcgiHumhOZqJQHme8ZqmSQWdRf7sBzq7df-rcAeciH1zTMQxhlqhodjaB0fi212mKkXEXp0NydzhxNXrZB7Up9srukB7vNHhJe1btZLK2Vw3SHzG_Nz2sx0OgNrSikvRQwLyrUWUnt-9qxpgjzbQueowjFIMwYPSU-Etfum6Y22c-t-WNnCSyeTX6WBNkDhnm5c_B2n3nzSMY3FiYV2EJBvk8ZCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa2c1939de.mp4?token=dvF70D6KhDq8z2G2aZ8qO0ODXWJvWaqG12wpmjFcl3t0f8LtlEUUTsslNCql4j5uQg0Pb-ipcFJGvNNJ9SoHURf8F1rK_jIaAhfSQn-AdYdH2QJxkLEix37_vHkcgiHumhOZqJQHme8ZqmSQWdRf7sBzq7df-rcAeciH1zTMQxhlqhodjaB0fi212mKkXEXp0NydzhxNXrZB7Up9srukB7vNHhJe1btZLK2Vw3SHzG_Nz2sx0OgNrSikvRQwLyrUWUnt-9qxpgjzbQueowjFIMwYPSU-Etfum6Y22c-t-WNnCSyeTX6WBNkDhnm5c_B2n3nzSMY3FiYV2EJBvk8ZCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما به زودی به مریخ خواهیم رفت
🔴
ابتدا به ماه و سپس به مریخ خواهیم رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131846" target="_blank">📅 09:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131845">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjhPCkg3y5Xtp-cVfi4crNVs5AOdq32VOxE-IZjia0x0BIUsvOKGXYAxpRI52Sy164wecGxL58BCFkwCUSNw2wXZ03PUYDq12Q58hNHVL_SUANauEOuh-K1DnPyBmtZ9uQ6PhqdxTyX8pEfv0b1i1tY4plA_BeXSB2of5K2380Aa4ntZo8HfUKsaib7Qkz0BswTKA5YN61Mz6LNbPCbPsq0PdiUO_lMsuX_TZAGmiueJARB0TQ9b_KzSboT2vniE1dFo5w4Ey5H9WSXX5mmN8ukzYJSwdC5uMmrLFHq7akdd6DelZGjpK9_VrPVkqdeXHOp33FsLMwz_MJECWQs4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از خیابان‌های اطراف مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/131845" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131843">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CU0SYYYptXJF5pZlIkKSW6989aLWVcmVF4P3rs5T2-bU0qaZ5PxWrXyxBcVfmKuMH7Boti7Ie4HnAqiqzpo3d7cSA60XafUcX1R7HGdWEu8K7TibMc5jRMoCNycVtwOryzG9UTTv13jWvDgYXacIWR9c9lDq7g863CNtlutqTjkjGtjyr4bg5OaJ2hXY2_pWJMXKbMwlIq_WfbNpCgMmKws5JXsUIYg51C5vUGSbqH3JnZ7e-3L5AJQ31vUxgztbPno-GEl0r3sS-ZMlu4_Fw9OUYozoRyh8IVfHhWbWjg76i7GsOApDPigILfhSV2WqDEpVhSybTeRQFHQ7ib2ttA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyoaXIFGlnTOQeqUzznJg7eBUhoLHhl_xJaWKjCj75aSL8M2Tjzs0nHmD-GK5igagmu62yoYeF9xF_oTNQmvmYZG7lzD2IWkLiRqeNpDtGOS00AFKbt6wEV_M4X4H-gcb1Y8RICNZuNtcgcGyzIn8F7f16Whl6fzlSvRwt9Q1o9ldrxNzWC4tytk7x00SFaRPpkj0P-HC1T0R35GNJnjCP7MAnLD9Cv8lHJPAkJuIc-QEgDfPiTTxnswFGcwjnctxnB87WJ_4BKSO1QHe1HHbIKPUeaC8dUeEPuiIUCh5lSEzC9Im1P5xWtcVxbfOME2uzyyBF0rSkc3zeK-wsC9ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده های SU-34 صفر کیلومتر نیروی هوایی روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/131843" target="_blank">📅 09:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131842">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
پوتین به ترامپ زنگ زد و ۲۵۰ سالگی آمریکا رو بهش تبریک گفت
🔴
همچنین پوتین ازش دعوت کرده که به روسیه سفر کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131842" target="_blank">📅 09:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131841">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
زلنسکی : با ترامپ صحبت کردم
🔴
احتمال واقعی برای پایان جنگ با روسیه وجود داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131841" target="_blank">📅 08:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131840">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزارت دفاع چین: پکن و مسکو در ماه جاری رزمایش دریایی مشترکی را در نزدیکی شهر چینگ‌ دائو چین برگزار خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/131840" target="_blank">📅 08:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131839">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFtOK0p2gDV3VGH8-I3QE9YiGx3nb59dVuF4qk5iJvRiXfLp9Y0XuLOWFVVClgkDvPqoe7vHsfB5fU_xMztEgwie68Hxu_EWXj5IRUeg78ZiXYm8-MxvD_dZlbuyDiueIGRc_DCuXX7EGPsud_cEGkAyacOozB3tr9UfXd0Xm88E7fkymA4OtAnN81iIgX6VUccx1OSqpMbRkfbjp0mm42Z0ABpxmw6tg1IIfFvumEKe1q5Ywdf2TxnsFcHo10KJQ3_0gs9j3r0URUZtb8Kj8xiio2F1y7DqvG6C4eOtpqxeKAm4QUTgzZ5A4ksDSsUbOa8v2dp1lj6NTsJMicPd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار هیات نمایندگی حزب‌‌الله لبنان با عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/131839" target="_blank">📅 08:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131838">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ:همه جای دنیا تلاش میکنند شبیه ما باشند؛ اما هیچکس نمیتواند مثل آمریکا باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/131838" target="_blank">📅 08:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131837">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
طبق گزارش ها شب گذشته پوتین و ترامپ در تماس تلفنی یک ساعته در مورد ایران و اوکراین گفت و گو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/131837" target="_blank">📅 08:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131836">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c3c08acdf.mp4?token=e-Q-C4bLBBhSWdXsPQo699wVIJaeUIf6524y1pxLBsIbBC1Hdo9aYPBW2QtkgBJ0ibPD_4oiq59hC8ir1szbAW5QbtkXnwFFqL2EeBwAV8spEIXKIuXIk8TvEB0p8dY6kbT6QED7R0lMgnDccNwF9hmZJuQW6cQLREeeiYXzZ8FYFitcSdJrQLyM8t1_tOVWGNcmphDNGOvtuqqGp5cgUjxOxIT0Z9Y_zDOo0MI1VD5p66QLYjGfDsHrt9FEhu5_EshedurY592d4DMto4bYbMS5Zrop3BSR-WHoG8sMN8BDXCbKmB4TWIoUfy2zvFQVR3N1fCjCUUNn8g39z47e5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c3c08acdf.mp4?token=e-Q-C4bLBBhSWdXsPQo699wVIJaeUIf6524y1pxLBsIbBC1Hdo9aYPBW2QtkgBJ0ibPD_4oiq59hC8ir1szbAW5QbtkXnwFFqL2EeBwAV8spEIXKIuXIk8TvEB0p8dY6kbT6QED7R0lMgnDccNwF9hmZJuQW6cQLREeeiYXzZ8FYFitcSdJrQLyM8t1_tOVWGNcmphDNGOvtuqqGp5cgUjxOxIT0Z9Y_zDOo0MI1VD5p66QLYjGfDsHrt9FEhu5_EshedurY592d4DMto4bYbMS5Zrop3BSR-WHoG8sMN8BDXCbKmB4TWIoUfy2zvFQVR3N1fCjCUUNn8g39z47e5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/131836" target="_blank">📅 03:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131835">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=hl9etJmqLdHCDUz8PAd2tzv3PM2X3AB__8bJFa0rxuZt8y0P3O4TTVq0IVnunlL-b3wUVmUuh9JEAaYkrhWnUpU-E65RER-6kQR2PqKzAmlhbAial_oETs7gR_otlbB3TXxt5IWLdhN9UHdzPZ8ANHWjGf0O43FP2r7EFiZ8z1RbYMEqMaroAmLNfn4s_49_w5a5sJ8DTbt1-gTHwqF7Ozcy-q5ldUCQYmqIcVqgmTnNBcTxGQa28seREwS4BJpQI2guhDAoyduy5tmwHV_eFlciIruMyLbT0Hgh69jwPovlwVf6Ca2iDUks3C7ladhfUI4EXkD1COijg35Jb3Pspw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=hl9etJmqLdHCDUz8PAd2tzv3PM2X3AB__8bJFa0rxuZt8y0P3O4TTVq0IVnunlL-b3wUVmUuh9JEAaYkrhWnUpU-E65RER-6kQR2PqKzAmlhbAial_oETs7gR_otlbB3TXxt5IWLdhN9UHdzPZ8ANHWjGf0O43FP2r7EFiZ8z1RbYMEqMaroAmLNfn4s_49_w5a5sJ8DTbt1-gTHwqF7Ozcy-q5ldUCQYmqIcVqgmTnNBcTxGQa28seREwS4BJpQI2guhDAoyduy5tmwHV_eFlciIruMyLbT0Hgh69jwPovlwVf6Ca2iDUks3C7ladhfUI4EXkD1COijg35Jb3Pspw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زاکانی و برخی از مسئولین تو حاشیه مراسم امروز رفتن چلوکباب خوردن
🔴
مردم هم اون بیرون زیر آفتاب، صف وایسادن تا غذای نیم پرس و تخم مرغ آب پز بخورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/131835" target="_blank">📅 02:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131834">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کابینه امنیت ملی اسرائیل، احتمالاً فردا عصر تشکیل جلسه بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/131834" target="_blank">📅 02:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131833">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a14033e54.mp4?token=q8cGNykyxKsVc_ItJDYCgXSrVn47vszCGKmlJLn7M-AJnHULO8dPFzE8uv-3ZDJA8KDVPDC-5sJYDaQfAU0IRqwJFnP_1NW2obuXVFA1U_5XR09Jo56QWlWrH4P39ZU_gfs8iHAAqPsoO2_gtR2vvpBu6i0Ie2CGPXMaXDog-l9fRuUQXr9LUC8UWbwS-67Yh9xzbhbFa34eHLU-cW3wDVrpLZTOw880H_1A_6_LrwtyZUfOVQXXocKGEJY7Q9ellJPGCqj_7pOqRZ8wXA2DcY7Y6NcDtla71apBiggFVg1uXMZsTQ8i0-JCvlMOvhCIugMROyrxafm2PwnNkf_T8z1Uv1g90YSgZN_3kKLj1APLaeL8zdM8ZFPvyiGyY9tyAtTMdmys3seSU4bEQRQ060q9PMIYVH3r2z46luPC3vmE7wu5-oOc7Q2m5aIATuxg-_BaYYQOPwLC5iMzH-VUuHeEOuufEIroNsuODDNN2UqRK_tiNklDNs_5kmWbTnHb2BvymE5ixb0V-8b7hls3zCrN6ldhbbOoP0_HQCZMctJsUBu8Kj52M1rYCJJUMWL5vzcsIkpAaazgMjRx6Uar20LC90us64jMoXmAeKvWeXTTMZJdhcR7POP33qrFaWB5oP55KqAilN4SorH28D-mMO__pSU8oJDbQTswNAi-LEU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a14033e54.mp4?token=q8cGNykyxKsVc_ItJDYCgXSrVn47vszCGKmlJLn7M-AJnHULO8dPFzE8uv-3ZDJA8KDVPDC-5sJYDaQfAU0IRqwJFnP_1NW2obuXVFA1U_5XR09Jo56QWlWrH4P39ZU_gfs8iHAAqPsoO2_gtR2vvpBu6i0Ie2CGPXMaXDog-l9fRuUQXr9LUC8UWbwS-67Yh9xzbhbFa34eHLU-cW3wDVrpLZTOw880H_1A_6_LrwtyZUfOVQXXocKGEJY7Q9ellJPGCqj_7pOqRZ8wXA2DcY7Y6NcDtla71apBiggFVg1uXMZsTQ8i0-JCvlMOvhCIugMROyrxafm2PwnNkf_T8z1Uv1g90YSgZN_3kKLj1APLaeL8zdM8ZFPvyiGyY9tyAtTMdmys3seSU4bEQRQ060q9PMIYVH3r2z46luPC3vmE7wu5-oOc7Q2m5aIATuxg-_BaYYQOPwLC5iMzH-VUuHeEOuufEIroNsuODDNN2UqRK_tiNklDNs_5kmWbTnHb2BvymE5ixb0V-8b7hls3zCrN6ldhbbOoP0_HQCZMctJsUBu8Kj52M1rYCJJUMWL5vzcsIkpAaazgMjRx6Uar20LC90us64jMoXmAeKvWeXTTMZJdhcR7POP33qrFaWB5oP55KqAilN4SorH28D-mMO__pSU8oJDbQTswNAi-LEU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های
F/A-18E/F
و حرکات نمایشی تو واشنگتن برای ۲۵۰ سالگی آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/131833" target="_blank">📅 02:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131832">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuGSlqJxkqL3s8a-sWqnek_vkZrmsVwqt1aF3xKgpB2gBnkuruOud3CRDpotnrHhUwMyg3gyX515gxtYtZ5Y3SS2PeV5KWoKY5FR0Duwf93kgkJ4jp3nvok0R_Mx5UyZtp90nCgmOfX_qQz0tPTKWdmTUzmg9ZSxuH7oQhNYbMH-W6pnDIJcGHVqe2pT1sDJjE0tOiC8JkOcEEZ4NpLzwhfLg9VT3l03SiEzOY7hjAkDnxGdIPpF3aWLMn3JIRUf8_dFMgwGWRxyVuvCRUa9x8tq-xUH2rusVJ603Dy8YUSjfLDBMoDLC1zQlUQkMUpFOaSU_UApvmMswgNpQdX9cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا کامیون حمل پیکر آیت الله خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/131832" target="_blank">📅 02:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131831">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtXQBjtxgot6V94gA_9d3MIFIG9yezJ2dCSiFXXTZO27l0butCwrjU7R3nrJ66M5JsS0AytXLInd-7Yl9oMYqX-DBDRh37Zaa6LDA7c3evOKUr24vhqV736dbmk3Zo5Xw4H6Gs5dbouefkswqzPPdRlXR4Da69OgFEqKkuL4DAoBgkGaJG6AP8m3kc7a9ZCuVySLWgmYl7iSifCTnXmh-eoxfHZIKMr75uSFa5kxWp4XnnxsGybLCfnu9CUnSjMV8kyLtlSxnN_tEJzQdrRX9NuDpB2962zDche2ciooeTT3WkSopjl4wUe_aVTlRKbvZmdz7jc-QqDNGqQM4R6eWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوستری که برای کشتن ترامپ امروز در رسانه ها و در دست مردم حاضر در مصلی دیده می‌شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/131831" target="_blank">📅 02:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131829">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf04045170.mp4?token=hVx4yM7ZJXiBXMFG9FNwvRfxjMdMbDqkisPf4HKBy9OG-FXzMUIIi42BIbUDV-zyfESOwVWYDPywYq6qyeEy9JYcM7u3TaECuVVmFsV2b3euWFohlPUe8pPXE0pZ1Bo-Ccx_2W6pVOH_DPCPGYWG5XBxG-XyAYfKkwXQ02Mc3IMqZLzScvHyUG-ovE2O_xhn2sQyDjx_BNHTsIwJApkPXjz9QQO6etU5tE6NHfIhb10r2uAlhJGCb8lLvUnj6f5_jwqiEPGbQYb5WU0uhaiJos_zq1NXg_tfyIv6KetlVfTNBCI75J8SFuC-37Qok3UYJ0bto4ULyZTwf2Wrd0bZFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf04045170.mp4?token=hVx4yM7ZJXiBXMFG9FNwvRfxjMdMbDqkisPf4HKBy9OG-FXzMUIIi42BIbUDV-zyfESOwVWYDPywYq6qyeEy9JYcM7u3TaECuVVmFsV2b3euWFohlPUe8pPXE0pZ1Bo-Ccx_2W6pVOH_DPCPGYWG5XBxG-XyAYfKkwXQ02Mc3IMqZLzScvHyUG-ovE2O_xhn2sQyDjx_BNHTsIwJApkPXjz9QQO6etU5tE6NHfIhb10r2uAlhJGCb8lLvUnj6f5_jwqiEPGbQYb5WU0uhaiJos_zq1NXg_tfyIv6KetlVfTNBCI75J8SFuC-37Qok3UYJ0bto4ULyZTwf2Wrd0bZFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله مجدد تندروها به قالیباف
‼️
🔴
تو چرا اسم بچه‌هات ریشه یهودی داره؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/131829" target="_blank">📅 02:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131828">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqClDYL4n246SHAE8EUatZEQnAnmnpFDU-O5wnzMrC4zm604-RL6_TyQ0JjE1TktNgaOhhx1sMqHoz4NM0TWh_ROlunhW5de0bttHxQ9GkuUSRdmBDsZWiEGNNsZm9kXz9VKna1oBvP_HuGPSZUyU7uRuXLyO6CS6F8DS6Kosbu6mRF27OmbYX9CudPmFrwQm3Vl6J0Yt0QQ0mmKDCbBJLpiO7JoB1X7ZuiyIUvoPWCGGWmFW2L0umSJPFB9rmdKkjqA8M_WCcKr1_pMsdALr_l5CgmoIyCkVeYz4pJKaTf6CSOJ-OwcLyZTvepL150ldRgUSokepoCumFyuRJhpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: مجتبی خامنه‌ای در تلاش است تا در تشییع پدرش شرکت کند اما مقامات امنیتی مانع هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/131828" target="_blank">📅 01:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131826">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/131826" target="_blank">📅 01:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131825">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2bbcff1e.mp4?token=GwaDlrAWrscTSqlItqpeekI0vQGDSFLZYbXE-PrsJB1GjWBK9UVn4EYVXxdMGVgHOry_IM4DVASD4otvUudx30f9iF1-TctnXZkJFAuYtjlPVthGbrbLFxwV304KP4Wv_OGRTXhehoMhdv5rR6-8ENRu8zoBgQBW2UPk6hOSVPTRC_3f_8mJiK5d4F57qynYN4yCdJYBxcyVsGP8-xaGTSQXuBInAmdBykYlTU82iVRFv6jLhd57tRobW7qZ3ioRtLopSrylOBh_pCecq7Lz9N4j-3NBAZNbgI_TTbkBn5ZPkra_KZiyzbGuwahrcHn_FNKzSC5WPaH-068f6E7Qyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2bbcff1e.mp4?token=GwaDlrAWrscTSqlItqpeekI0vQGDSFLZYbXE-PrsJB1GjWBK9UVn4EYVXxdMGVgHOry_IM4DVASD4otvUudx30f9iF1-TctnXZkJFAuYtjlPVthGbrbLFxwV304KP4Wv_OGRTXhehoMhdv5rR6-8ENRu8zoBgQBW2UPk6hOSVPTRC_3f_8mJiK5d4F57qynYN4yCdJYBxcyVsGP8-xaGTSQXuBInAmdBykYlTU82iVRFv6jLhd57tRobW7qZ3ioRtLopSrylOBh_pCecq7Lz9N4j-3NBAZNbgI_TTbkBn5ZPkra_KZiyzbGuwahrcHn_FNKzSC5WPaH-068f6E7Qyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قدرتنمایی جنگنده‌های ارتش بر فراز تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/131825" target="_blank">📅 00:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131824">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f30f9eab.mp4?token=X0ig68UpRYdgcOtaSBKlhIi1V43o69ZMVbCpDW0imE21JGGv8mUi3wmNHTwuMwO3j33ko2uZjRiBNeWhXoxcBQa9QrZ3xXaek6VO4x6PmmJ6dkPrSjE1W9esUByX8g0mTONPLR7rqcryjQxWNHlTVzJiRxUlMNUBVnNHRXC8neJbsTNkYfFkBk7cXgZDWmVdqgsihNEFIvP6qqRdMTLLkYgoScDujfLJfcNl8YMdeOGEDFWZKkbIYI3Pypbgx_QuRuq1KfBg-wpkxwWbEy3Cftn9kpFut-iXyUFPFerkEkZgy9dye7BX2_WCZ7QmEHcgesT-sAbIsgBUlCbd8PT2cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f30f9eab.mp4?token=X0ig68UpRYdgcOtaSBKlhIi1V43o69ZMVbCpDW0imE21JGGv8mUi3wmNHTwuMwO3j33ko2uZjRiBNeWhXoxcBQa9QrZ3xXaek6VO4x6PmmJ6dkPrSjE1W9esUByX8g0mTONPLR7rqcryjQxWNHlTVzJiRxUlMNUBVnNHRXC8neJbsTNkYfFkBk7cXgZDWmVdqgsihNEFIvP6qqRdMTLLkYgoScDujfLJfcNl8YMdeOGEDFWZKkbIYI3Pypbgx_QuRuq1KfBg-wpkxwWbEy3Cftn9kpFut-iXyUFPFerkEkZgy9dye7BX2_WCZ7QmEHcgesT-sAbIsgBUlCbd8PT2cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه زمان کوچک زاده تو مجلس یقه جر داد که من به عنوان یک ایرانی راضی نیستم یک قرون از مالیاتم جز غزه خرج جای دگ بشه
🔴
بچه‌ها شما به عنوان یک ایرانی راضی هستید یک قرون از حقتون اینجوری کف خیابون ریخت و پاش بشه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/131824" target="_blank">📅 00:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131823">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
قالیباف: اسرائیل رو نابود میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/131823" target="_blank">📅 00:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131822">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VibiyLPHu31QRyOArsrIjZ6-1lGjc1pffzC3MkmOfrwYYOSuYfTMH3hzRc1pPw6Ee1rOAhR6bi3khreLGBsE3qnj1bvGR_q2DvpOn3r215Wjc7wA1lNiHcJfmPRAK_l5aFEoIE9PP_d_1eZL9U6KftUFyu_5J-q2aktANKbw1w1SfDBUfylf5wd64aQSlKRX4rCkhrcnPaSvz9RI3yYvAbiQ-fxN8UqH5Ogs9Fkm5DC7x16V2PxXwYFkElrY7DPR7B21M47pb0SqAKjHLQCIOjttL5VwUp7tACOqspHm1YiMCP6j906LzBbsr8mRF6zxLHyBgCLOM9TudbkY0DFOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیشترین چیزی که ایرانیا تو ۴۸ساعت اخیر دیدن
🔴
هر ۵ دقیقه پیامک میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/131822" target="_blank">📅 00:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131821">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7e4c4447.mp4?token=FftSRPjGpYAhxxLAtstHeGTN6DpZINmh7QGDHXET2bZ04oq3U5PpFVR-15E7Th_WMgAwjTcXjcP3yyBRCop_coSXLsgY3eoYk84W57gEAZT5VsRBQSKLnj5sWH2ssRR104hJJbh2_aC3bm3eO6036B-di2gvqQ4MVjuesJlFn6isZ4NJi_pSS0ihnFH2q0xspMsutXk1WiyJyg2xFCAB6XLPcLx0TER5OKaMFWgIWNuL-sfAIpZRF_lsIZFzMBgmFNdPaoa9ZH5foPfK75VZ8jMINPDym3-xuu5wrDVGXwZDpRpaQ6G1GnybK4zOrG5Ez-__y1dnCAJaM5lmr68Rjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7e4c4447.mp4?token=FftSRPjGpYAhxxLAtstHeGTN6DpZINmh7QGDHXET2bZ04oq3U5PpFVR-15E7Th_WMgAwjTcXjcP3yyBRCop_coSXLsgY3eoYk84W57gEAZT5VsRBQSKLnj5sWH2ssRR104hJJbh2_aC3bm3eO6036B-di2gvqQ4MVjuesJlFn6isZ4NJi_pSS0ihnFH2q0xspMsutXk1WiyJyg2xFCAB6XLPcLx0TER5OKaMFWgIWNuL-sfAIpZRF_lsIZFzMBgmFNdPaoa9ZH5foPfK75VZ8jMINPDym3-xuu5wrDVGXwZDpRpaQ6G1GnybK4zOrG5Ez-__y1dnCAJaM5lmr68Rjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از متولیان مراسم تهران:
تابوت حضرت آقا، یخچال قوی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/131821" target="_blank">📅 00:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131820">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7btnv-1FxtstvZmv-ijJMAyg7S4sgfbiqSuNySwp4zkZfO1vYQOQz1WQXVH9JAimzCQ-PbVmg1uXED0euTbC_DTmIJay6TUY31w617TZpWT4VZOV2HqgVSqcvdFWXQ7_RBnF6VblBsqg3pN3DS3qnTVBaEipZwVJjsCb-A0H7oPi-lTyyHzQpdvxSbn83A9tHzt87Wjf-ZXNMz7udy-AEqb5ke3aIpk-7h-J92dY-kqtHmW7SnscNGi1XmzbSnZD_0_9d9wCSUilkWegqhBrCmLLxJIRr2apJckfIAa8HP5k3FPagdXeZWBgXqSx8lK7ReI01-5Twnqg6oJxPtz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/131820" target="_blank">📅 00:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131819">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AW-V75AmWDyoXix-5SZHrMRHvnOI8VktSOiBqhxnt9Xv4Qqzqyejc_3nOrRImQ6sQkOfML75AuQkC_xevb4ndNVJxz1Ymzc9kAsYS9_QQTABsuJ64pzZEc9HIetsmyKq9zBpUg6sLa8MyWoQ0BaBcOafDrdrXjltIP059ECgLG7pwRO-_dUBVU3p4ir_UQ5R6P4gHFVF5S6dEnNSB96Of-HRyRGm4bJbymTAeVIzjPEbNucTC4GrkfKeP6ICvPIgoxMpQ_ykwvqi96ZXTIZH5WAA6RTVl5jPh5bTPjukhzFO-mxV_u_AKl-lfOvg3OPzjlkzsmZjyTVe38B3dUxDIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای ارتش اسرائیل در حال تخریب گسترده ساختمان‌ها در منطقه حداتا در جنوب لبنان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/131819" target="_blank">📅 23:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131818">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
واشنگتن پست: علیرغم ماه‌ها حملات آمریکا و اسرائیل، رژیم ایران تضعیف نشده است - و در واقع، برخلاف اظهارات ترامپ در مورد «تغییر رژیم»، در حال تقویت مجدد خود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/131818" target="_blank">📅 23:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131817">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
العربیه: هیئت ایرانی شامل قالیباف و عراقچی بعد از مراسم تشییع برای مذاکره با آمریکا به پاکستان خواهند رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/131817" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131816">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚀
سرویس های پایدار  safe vpn
✔️
اتصال پایدار و پرسرعت
✔️
دارای ساب برای اطلاع لحظه ای از باقیمانده
✔️
متصل در تمامی دستگاه ها و اینترنت ها
✔️
مناسب استریم، بازی و استفاده روزمره
✔️
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 30,000…</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/131816" target="_blank">📅 23:47 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
