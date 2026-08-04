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
<img src="https://cdn4.telesco.pe/file/jG8lb3WrLKFdL9tZMulcP6Pi6-_bKDPMzqvTsBq4TLAj2tALaDJCEtYI27Fpln92udpfY-TVzldOw3twUQWFH6TEQyiMYGtGyvOvsalMrk9Schd5m8AF8o2BD2HjwViiRHoZlsfKIyTA5CymoHdTL6D8vPam_a4Yow9fffSYuyjoIuaW3BZT0wcld-mOOy14uSvCkyNQjWKGFGXK5q6ZctdloOFqwk77motg4-cqnvAzHDYswGtk3OtSOSPhTsxx-kxni0weC4ZCph3j_Ob8GEE-npklHVOeCzC2uYqrr8pFLtkgQDBBWwjfrIeggQq027KdTYCtQr6qI427q48nDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 12:47:33</div>
<hr>

<div class="tg-post" id="msg-678340">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سود آرامکوی عربستان در سه‌ماهه دوم سال با وجود اختلالات جنگی ۴۴ درصد افزایش یافت.
🔹
کانال ۱۲عبری: جلسه امروز هیئت دولت رژیم صهیونسیتی لغو شد.
🔹
عملیات انهدام مهمات عمل‌نکرده، فردا از ساعت ۷ تا ۱۲ در قزوین انجام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/akhbarefori/678340" target="_blank">📅 12:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678339">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/678339" target="_blank">📅 12:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678338">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
حاجی دلیگانی: در حال جمع‌بندی و جمع‌آوری مستندات برای استیضاح عراقچی هستیم
حاجی دلیگانی، نایب رئیس کمیسیون اصل نود:
🔹
هر نوع توافق با عمان درباره تنگه هرمز باید به تصویب مجلس برسد. افکار تیم وزارت امورخارجه در دوران قاجار گیر کرده و از روی ترس و وادادگی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/678338" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678337">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/678337" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678336">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/678336" target="_blank">📅 12:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678335">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/678335" target="_blank">📅 12:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678334">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/678334" target="_blank">📅 12:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678333">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/678333" target="_blank">📅 12:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678332">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
الجزیره: دور جدید مذاکرات لبنان و اسرائیل در ایتالیا آغاز شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/678332" target="_blank">📅 12:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678331">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrcFaHbC3a7LNnBvSqvdDUAtaz9CaXCBO6XkseC3JiluNoFkKLl1MrM1gx8hOi-MCEcSDAoI3in-rpfzNS_ATeOJKtCccBaknuEEPYYf8TObaWZeMOmDuNUtWE5fc-jOUeUx8w1bky2sEU-na5OEegmw-3BhSBwKo0wtqzT6ApwPkIcnR9GDGZ4tPiM-MTZ--PPmEgPu7qPpajld_sQW4EXVK-0Nf1WE2ot74J4uu3Iv-w2WGAVPz0clUdNR63IuNjdlUnihF0P8AeVk_0oaifbY14MoFhoIyeb8qUC4Lp4u_XnWdNrPq3nywP4YB54UIuCLHNoPeCO7-WqaAAIvBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت بلیط هواپیما تهران به اصفهان تا ۲۱ میلیون تومان
رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/678331" target="_blank">📅 12:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678330">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7h5qmSN49ASYUOgCKgs6bO8p1yUnROqIfVnqXO1iPMcfPnNqRrjojigYGSHIa61h2dOB-MpoMfNWnoHWVnilVu1-lsks_xlOysVedEg_D7ZkgK5Y_IojVDN8jD67kGAPRaqiBF0DD_pBhyum24mh7io2ROmqtmPq5OUmAXU5kxNU1GHs2FDuxSJeGVW2k06c1yR_FmSe3ayKiCG8rEPLvU70pjUY2_aNsuNTafhZ_31gTjV_bV30aPHTtChNXIsi_AjFJ33PRa0jXP-JrY2EzuDLFu4H9L69F9knJMNcZMoG54IYctTR-LNVNkWHt1N5iy_AnCTlOxIPCPOdSdnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا رویداد اربعین به پیوست رسانه‌ای نیاز دارد؟
🔹
برای شکستن بایکوت خبری رسانه‌های بین‌المللی از این رویداد و تصاویر و روایت های فاقد اصالت که توسط برخی بلاگرها در رسانه‌های اجتماعی منتشر می شود، نیاز به یک پیوست رسانه‌ای جامع وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/678330" target="_blank">📅 12:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678329">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/678329" target="_blank">📅 11:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678328">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUd0V6QiBd8OcIkfYoXL0mgu4V1FPuLNf13q2xbULKBKKX7AKoX2A5csIwanMG3xJrI2Aq6z9i63osVlFmjFtcht-YRXUcRi6TAQWcfvPN82Kwm_V_j8oISbYZlicLm8wcDVLBVjhwueolxLLYJCnXIf80t7RkE7zllcFXzDVDLDlMVT1BAxoLlkyikESpxT22Ab6xsK3CS572MM82yBg_h2IBHfJjgDWNOHLiVCytJQQe5-TP6RNXFo-tCGxlVRjitmZ6NfqpLKJN3OIhqQadq15x_9uZwYEUu-N2nwgL7gUywj_frmUFztEfLtgH8PLcw0pmCM1BWKp7YGAIeCzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
متن زیارت اربعین
▪️
زمان قرائت: پیش از نماز ظهر اربعین
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/678328" target="_blank">📅 11:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678326">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/678326" target="_blank">📅 11:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678325">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سود سهام عدالت کجاست؟
یک نماینده مجلس با انتقاد از مبلغ سود سبد سهام عدالت:
🔹
سودی که به سهامداران پرداخت می‌شود، با واقعیت‌های اقتصادی کشور و نرخ تورم همخوانی ندارد و برای بسیاری از خانوار‌ها اثر ملموسی در بهبود معیشت ایجاد نمی‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/678325" target="_blank">📅 11:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678324">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/678324" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678323">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
یک منبع بلندپایه به العربیه: سفر وزیر امور خارجه ایران به اسلام‌آباد به‌زودی انجام خواهد شد
🔹
میانجی‌ها برای دستیابی به اعلام رسمی و قریب‌الوقوع آتش‌بس، به زمان بیشتری نیاز دارند./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/678323" target="_blank">📅 11:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678319">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
حدود
۲.۵ میلیون شغل در یک سال از بین رفته است
🔹
بر اساس تازه‌ترین داده‌های آماری، نرخ بیکاری در بهار سال جاری به ۹.۱ درصد رسیده است؛ رقمی که نشان‌دهنده افزایش ۱.۸ واحد درصدی نسبت به مقطع مشابه در سال گذشته است. در تقابل با این شاخص، نرخ مشارکت اقتصادی نیز با افتی ۰.۵ واحد درصدی مواجه شده که زنگ خطری جدی برای بازار کار به شمار می‌رود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/678319" target="_blank">📅 11:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678318">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/678318" target="_blank">📅 11:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678317">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/678317" target="_blank">📅 11:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678316">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/678316" target="_blank">📅 11:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678315">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/678315" target="_blank">📅 11:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678314">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/678314" target="_blank">📅 11:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678313">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/678313" target="_blank">📅 11:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678312">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
روسیه: ۲ کشتی حامل سلاح به اوکراین را در اودسا هدف قرار دادیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/678312" target="_blank">📅 11:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678311">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/678311" target="_blank">📅 11:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678310">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/678310" target="_blank">📅 11:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678309">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/678309" target="_blank">📅 11:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678303">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
وزیر اقتصاد:
دشمنان آرزوی زمین زدن اقتصاد ایران را به گور خواهند برد/ مردم نگران نباشند؛ در برابر هر برنامه‌ دشمنان، برنامه‌های مقابله‌ای داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/678303" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678302">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
انتقاد نعیم قاسم از مذاکرات دولت لبنان و اسرائیل  دبیرکل حزب‌الله:
🔹
مذاکرات مستقیم دستاوردی جز امتیازدهی‌های پی در پی برای لبنان به همراه نداشته است.
🔹
از حاکمیت سیاسی دعوت می‌کنم از امتیازدهی دست بردارد، با مقاومت وارد گفتگو شود و وضعیت داخلی را ترمیم کند.…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/678302" target="_blank">📅 11:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678301">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
حماس: به مرحله دوم آتش‌بس متعهدیم/منتظر پاسخ نماینده شورای صلح غزه و میانجی‌ها می‌مانیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/678301" target="_blank">📅 11:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678300">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/678300" target="_blank">📅 11:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678299">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTMJc3P_RGKdCtYhtr950tVNkd8ICna88GOoTeANnJQLkA2brLn4BRc3UV5VX0F95ZNa0oZFTzkODJtxD1ujpkKts-aYDQX1aLoeJtdlSkyub3Iy7p4ft8B5Ssv_RwGVVkzLnM982OUfPXnCnIWhMI5ATKCecd9o1dU0vrjy03HCV8vXIG0ZUhQWvh0AplXNFFrJcbQNznyRjrkyk28tqRFj2BAcwFA0IBQ955doW89jtYpgSPzFIYOz4RKo0aB81ogI4CZgxJ3swnwE5v2Hr_Digj0LAQTLB6mWGMcz4A3ma2zVmAVMpnH7nZ3df79cRovjNbAFW4qXWryjXGfoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر در مدارس؛ «ناس» میان دانش‌آموزان دست به دست می‌شود
رئیس اداره بهزیستی کاشمر:
🔹
مصرف «ناس» در میان برخی دانش‌آموزان رو به افزایش است و به‌دلیل جرم نبودن فروش آن، این ماده به‌راحتی در برخی فروشگاه‌ها عرضه می‌شود و کودکان به آن دسترسی دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/678299" target="_blank">📅 11:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678298">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBdp3zp-dGIMVPdLaUIp0iHwtHuKN2xf7yyMUBCEUT9IYZWydNPDdq_-M_Uf9JOs-lbKNxYVK4HRgsMKJiCWbGWvs42_FcNpemRy6IeN_Hs_ZXEE7ZnjwYFUEwDPRA7DMjw7sycEgPtTI1koDLolQOHKJic0fN9dCRT477USJHEwdBSUVqOH_PnWzDD_JVrLlPinmgk2aXEM-LvKD3nbsDCuU3AVkmFb99gxlDNkDokws4umc9zVfg9lBbINdktPJxqmODDlvsNIad1dcC6e-9goF-UVeBiOAtPH5bIMN1AQu5WOD01UjnyvtZL8X0v7CYVm_xAv6sRLlX59qyswhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمار مجروحان آمریکایی در جنگ با ایران به ۶۵۳ تن رسید
🔹
شمار مجروحان ارتش آمریکا در جریان جنگ با ایران به ۶۵۳ نفر رسیده که از این میان، ۶۴ نفر از افسران ارشد بوده‌اند.
🔹
در میان مجروحان، ۶۴ نفر از نیروی دریایی، ۵۱ نفر از نیروی هوایی و ۱۹ نفر از تفنگداران دریایی (مارینز) هستند.
@amarfact</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/678298" target="_blank">📅 11:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678297">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIWv9QzM6_Sj6XibmK2lFkYzZqHWbCgx-ZKdTgM-cgA1sHumqtwhaW6nHnyV1MZULDS4YPRM1S5-XQ4VH0c7fasB9QKkBttOn0QATN2n1ldbfdTGAs1H3J5IsMOzloPBcpC7o4r9acszF6Hhn4eFfNB42e9cSr_1-uu8dv6I68jmsUScMBvDsJufsyNENIEIa-Gu48-kjmRTxzpVqrCjg1TVIM4Gmhn6yVt8_PKx7SBrS0enjgJqvqfOn38JGt6rNiNEjPA_PBcPauUsd4eDVeY8vbE7AmVVFrbcf6Wjax7s_Kgv371KiP5xamSYPaZBBwmVfupNAnfhVabP9yeVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اهدای ۱۴۰ میلیارد تومان دارایی یک خیر به آموزش و پرورش در عجب‌شیر
🔹
یک خیر اهل شهرستان عجب‌شیر در استان آذربایجان شرقی، تمام دارایی خود به ارزش حدود ۱۴۰ میلیارد تومان را به آموزش و پرورش اهدا کرد.
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/678297" target="_blank">📅 11:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678296">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
انتقاد نعیم قاسم از مذاکرات دولت لبنان و اسرائیل  دبیرکل حزب‌الله:
🔹
مذاکرات مستقیم دستاوردی جز امتیازدهی‌های پی در پی برای لبنان به همراه نداشته است.
🔹
از حاکمیت سیاسی دعوت می‌کنم از امتیازدهی دست بردارد، با مقاومت وارد گفتگو شود و وضعیت داخلی را ترمیم کند.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/678296" target="_blank">📅 11:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678295">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: توافق ایران و آمریکا، اسرائیل را مهار کرد  دبیرکل حزب‌الله لبنان:
🔹
هدف اسرائیل از حملات سال ۲۰۲۴، نابودی کامل مقاومت بود، اما به این هدف نرسید.
🔹
توقف حملات، نتیجه تفاهم ایران و آمریکا و شرط تهران برای پایان تجاوزات بود.
🔹
اسرائیل به دلیل بازدارندگی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/678295" target="_blank">📅 11:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678294">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/678294" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678291">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
گزارش ویدئویی از حضور کاروان ورزشکاران و چهره‌های ورزشی ایران در کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/678291" target="_blank">📅 10:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678289">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e470779b.mp4?token=WmR5ESsBgVJLDUy7HKeP1R9EVe2-yVEoKYbulb2wlWtaPrikq_HEmPzlWu_KMWwslyIxkHXIZYwGwWiSKotkleZxL6dJhbLwh-ct4SE7tRyYxaUIjuGbS6n8FUes7R7_kL4zeWRSoGKf_NxFCkCPUusdcm1z2x4BQZXJMXtHjaWwY0vPIVdllzuWemLV34aN-5fGgUs4xC33eHWZdFKr9Hpwyc96aHx6PNMN6bCxldoPy-nS76hlHXCcuBQbhY4iaPqrNw8q7YEhcJIYsnTmvo55pzFapt3q3nNDnFnPTyPyNOtbjjWWHMDffN7VxWXJuad9MyxlLD6Bp5_6lezs3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e470779b.mp4?token=WmR5ESsBgVJLDUy7HKeP1R9EVe2-yVEoKYbulb2wlWtaPrikq_HEmPzlWu_KMWwslyIxkHXIZYwGwWiSKotkleZxL6dJhbLwh-ct4SE7tRyYxaUIjuGbS6n8FUes7R7_kL4zeWRSoGKf_NxFCkCPUusdcm1z2x4BQZXJMXtHjaWwY0vPIVdllzuWemLV34aN-5fGgUs4xC33eHWZdFKr9Hpwyc96aHx6PNMN6bCxldoPy-nS76hlHXCcuBQbhY4iaPqrNw8q7YEhcJIYsnTmvo55pzFapt3q3nNDnFnPTyPyNOtbjjWWHMDffN7VxWXJuad9MyxlLD6Bp5_6lezs3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برپایی موکب‌ شب اربعین در مسجد امام مهدی (عج) تورنتو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/678289" target="_blank">📅 10:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678281">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0236a5e13.mp4?token=AOBvtjaMKCS-vC2RM9AJD1Y6kKTFyIBtPdw8YnYkMD2j2YAwA75bPJYXkR6MrGGQg4nB4nNjeXDa9ZIwprEeeuGOXjum0K2pGzUXmrAodXjn25Q8T-PAd9M87OblL0wp3UoMp05f_ZImWGFmWDDN7peKolQePCJ1sKM09fub3S2zvwt8mVnI03wOhiFFVGoIH1h2TwClEYCuARYQ79M8xukRDj_zuBPA-e80jfvIOM8h_IZr8k21t1Xa4N8mCGgQDLo5w2zfaIYcQmMaSZ-cyNnKK6RkZoc3cOT9WmXskCd_XcOCuy-r92BToSqgJ805DjgInlO5BEn3jkJ8IJXsxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0236a5e13.mp4?token=AOBvtjaMKCS-vC2RM9AJD1Y6kKTFyIBtPdw8YnYkMD2j2YAwA75bPJYXkR6MrGGQg4nB4nNjeXDa9ZIwprEeeuGOXjum0K2pGzUXmrAodXjn25Q8T-PAd9M87OblL0wp3UoMp05f_ZImWGFmWDDN7peKolQePCJ1sKM09fub3S2zvwt8mVnI03wOhiFFVGoIH1h2TwClEYCuARYQ79M8xukRDj_zuBPA-e80jfvIOM8h_IZr8k21t1Xa4N8mCGgQDLo5w2zfaIYcQmMaSZ-cyNnKK6RkZoc3cOT9WmXskCd_XcOCuy-r92BToSqgJ805DjgInlO5BEn3jkJ8IJXsxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه حجم آب پشت سد کرج در مرداد سال گذشته و امسال
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/678281" target="_blank">📅 10:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678280">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/678280" target="_blank">📅 10:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678269">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/678269" target="_blank">📅 09:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678267">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1e9ea989.mp4?token=KkMkQWWfE0cMYDDs8H7JXxO5sILmcyB2iraPtbydXyY7ao7Fs_xDTneJZ_TMPk_NnqbDtlQEeXJXTOjIfJ-Y9jf9mQnikMzyKyy1XAaXbkxIYYSNCHQ1OaTq1WpCTtEWWUGPfztvlVzFOIauOrkWATuDfycT3v0EWrlwH4UEoeNBihj3c2AvsCUcXmdgx2Y5HeAUVLY1x0gIkv6WeRRWtuT99JU6PqO9OjmLz6vo8FNURzZ-UIvYDhtTod_cBhwnpkkNudwMaBGfy2UCIXalPbvd2kCUyjgkmZCYmlPgoPH8PlnuQXl9fkoCXHvPP6blfTjmJM9Xim_Yp3N2qTHRxjYe2N5XVVZPxVIHWMTzaPGr49BAVxKrcst1RSXh7p-k-WakDhc5TtdpraaEbzqSYOCO-gtdODCj3OIRIqGl6M-akHDs1UNpkkJFoppQqpH1pw7sQBDKxk58F-PAAArVXdV7smUcAxs1FFS-RHG1vTDN_TFX454MkXIZbIsbXtA9yqo73wdPS9ziwE6KnzUKJlphiwweIboQHZ3EWNum4BA28UsQd97NC_3lOXSmKi0bdTz190cuSE8dbW8SSmgbSRFDQInGujYJKKGgQwJn9oPwII4TB98BCsYyYDfZpa3KrSN-RS7W6XZuujJw-12luAa-6IeR-YvjgG2_NzSx3mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1e9ea989.mp4?token=KkMkQWWfE0cMYDDs8H7JXxO5sILmcyB2iraPtbydXyY7ao7Fs_xDTneJZ_TMPk_NnqbDtlQEeXJXTOjIfJ-Y9jf9mQnikMzyKyy1XAaXbkxIYYSNCHQ1OaTq1WpCTtEWWUGPfztvlVzFOIauOrkWATuDfycT3v0EWrlwH4UEoeNBihj3c2AvsCUcXmdgx2Y5HeAUVLY1x0gIkv6WeRRWtuT99JU6PqO9OjmLz6vo8FNURzZ-UIvYDhtTod_cBhwnpkkNudwMaBGfy2UCIXalPbvd2kCUyjgkmZCYmlPgoPH8PlnuQXl9fkoCXHvPP6blfTjmJM9Xim_Yp3N2qTHRxjYe2N5XVVZPxVIHWMTzaPGr49BAVxKrcst1RSXh7p-k-WakDhc5TtdpraaEbzqSYOCO-gtdODCj3OIRIqGl6M-akHDs1UNpkkJFoppQqpH1pw7sQBDKxk58F-PAAArVXdV7smUcAxs1FFS-RHG1vTDN_TFX454MkXIZbIsbXtA9yqo73wdPS9ziwE6KnzUKJlphiwweIboQHZ3EWNum4BA28UsQd97NC_3lOXSmKi0bdTz190cuSE8dbW8SSmgbSRFDQInGujYJKKGgQwJn9oPwII4TB98BCsYyYDfZpa3KrSN-RS7W6XZuujJw-12luAa-6IeR-YvjgG2_NzSx3mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: استعفا نخواهم داد و خواهم ایستاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/678267" target="_blank">📅 09:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678266">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/678266" target="_blank">📅 09:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678265">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6d0e66e3.mp4?token=MPrb3jLlpmrU2zJsUcfcORQOnQ0YAm4hqujSM5FwUAP4s4vmEzWejFDQQudN0PLeN_pVN-LmHo4q2mtCawAXBoD0F4xBR0TzX2byaDGygq3fghD5-BH7Z6VblMMci9B3PMndpWPbfKxOyPQjhoqKZJ3acqvrN2Q5IZUTBsDyADhAnik2XBpQdxy2luohc0Hb7x4w_iePAMrHrOVDyGEYQAWO1PYZSFDHEa5v6KyZVmVZxWhlyy_9LyGWNcx40JzaRYWqWgkzBpHxEut269tgd_ez2dS55cCtnFaLJ9phRT997zCQj0mcp7Lm-P4a1ALqKhhOa3OvY4ND0iqJz2t4yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6d0e66e3.mp4?token=MPrb3jLlpmrU2zJsUcfcORQOnQ0YAm4hqujSM5FwUAP4s4vmEzWejFDQQudN0PLeN_pVN-LmHo4q2mtCawAXBoD0F4xBR0TzX2byaDGygq3fghD5-BH7Z6VblMMci9B3PMndpWPbfKxOyPQjhoqKZJ3acqvrN2Q5IZUTBsDyADhAnik2XBpQdxy2luohc0Hb7x4w_iePAMrHrOVDyGEYQAWO1PYZSFDHEa5v6KyZVmVZxWhlyy_9LyGWNcx40JzaRYWqWgkzBpHxEut269tgd_ez2dS55cCtnFaLJ9phRT997zCQj0mcp7Lm-P4a1ALqKhhOa3OvY4ND0iqJz2t4yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله یک طوطی عصبانی به یک بازیکن فوتبال در لیگ جوانان برزیل
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/678265" target="_blank">📅 09:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678263">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7db3633281.mp4?token=qz9n3-L_64lD1CEzaJ1ukCZi0VcumKYeWM6dx18-Uxb92PpFrcInqkYx9WUoFfWEb2eLmPMaWyoQOn2rvFxRYUWRB0AfTkkncFoq60uJurkfPTA-Bs0hriDcVIp14dNtebI8sXqfpcGDgBprBSskQZwEKB307st7-bYZMeMeBCQ6ss5BWTgkYEGVAS0uPVRZE4hi62XkEKwZThBsOeldMwerAYVQmqWWmC11OTS253X3EVaXmiyXGsbcE8L6aSfzVCGMhGCkaTWIQ2KkcddFXz6woXgYhRuaqFY6ORKpMLzgQ9IPRlxF792Gqmzy2QkK95voHQmiJY8Fh0zdFYACyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7db3633281.mp4?token=qz9n3-L_64lD1CEzaJ1ukCZi0VcumKYeWM6dx18-Uxb92PpFrcInqkYx9WUoFfWEb2eLmPMaWyoQOn2rvFxRYUWRB0AfTkkncFoq60uJurkfPTA-Bs0hriDcVIp14dNtebI8sXqfpcGDgBprBSskQZwEKB307st7-bYZMeMeBCQ6ss5BWTgkYEGVAS0uPVRZE4hi62XkEKwZThBsOeldMwerAYVQmqWWmC11OTS253X3EVaXmiyXGsbcE8L6aSfzVCGMhGCkaTWIQ2KkcddFXz6woXgYhRuaqFY6ORKpMLzgQ9IPRlxF792Gqmzy2QkK95voHQmiJY8Fh0zdFYACyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا اباعبدالله
اِنّی سِلْمٌ لِمَنْ سالَمَکُمْ
وَ حَرْبٌ لِمَنْ حارَبَکُمْ اِلی یَوْمِ الْقِیامَةِ‌...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/678263" target="_blank">📅 09:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678255">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/678255" target="_blank">📅 08:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678252">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
بانک ملی: مغایرت‌ باقیمانده حساب‌های مشتریان تا ۱۷ مرداد برطرف می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/678252" target="_blank">📅 08:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678250">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/678250" target="_blank">📅 08:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678248">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoOj-4gaiCeTOnPUIl3MOUuJHK99Imx34mqKSz_a-dgTqbIUlnwlcrQPcWFdNa-chBmRSuomhpHTNEsJN8Z1FoQ_JUDjlDjT8csDAbev11OGZSq5yvJtI-Kj-I1E16kqZrwjFjNsT5VMVGkxqv0HOOdl2GtNe1rj4eL7bDr9tmNLHCLx5FsxHGNGxZ4NR4-aj_jLo0e7LCIT7kA7HWlnAyjKhB1oUib1ZMLfDJYpxR27INRTnxgBjlXhN6VhJYnAtj2fxsnuIeCJXCOh6YpjPuZIfudCPAypw1EhqDrrty4MBlisJmXwSeBhUWCKjR6bPBnjl_rnQUAFggx_SP_QSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لری جانسون تحلیلگر آمریکایی: راننده و محافظان شخصی نیکولاس مادورو در ازای پاداش میلیون دلاری با ایالات متحده آمریکا همکاری کردن اما بعد از پایان عملیات دستگیری مادورو، دونالد ترامپ از دادن پاداش نقدی به آنها خودداری کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/678248" target="_blank">📅 08:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678243">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/678243" target="_blank">📅 07:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678241">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/678241" target="_blank">📅 07:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678240">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/678240" target="_blank">📅 07:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678239">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/678239" target="_blank">📅 03:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678238">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
رسانه‌های عربی: صدای انفجار در کویت به گوش می‌رسد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/678238" target="_blank">📅 02:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678237">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/678237" target="_blank">📅 02:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678235">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
تشییع پیکر بیش از ۱۰۰ فلسطینی پس از سه سال
🔹
پیکر بیش از ۱۰۰ نفر از اعضای دو خانواده فلسطینی که سه سال زیر آوار مانده بود، در منطقه الصبره غزه تشییع شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/678235" target="_blank">📅 01:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678233">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/678233" target="_blank">📅 01:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678232">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/678232" target="_blank">📅 00:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678231">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
سرلشکر رضایی: به‌هیچ‌وجه اجازۀ بازشدن کریدور دوم را در تنگۀ هرمز نمی‌دهیم
🔹
اگر ناو و نیروی نظامی هم به تنگۀ هرمز بیاورند آن‌ها را هدف قرار می‌دهیم.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/678231" target="_blank">📅 00:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678222">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/akhbarefori/678222" target="_blank">📅 00:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678220">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYQFgktcsYsN0lmf8TvGxCFvW-tVeIDgK93jyyQ3fCL5CzL73uV6eFjKJX4DMe4JXrWXhqcyjiN7gK3VIofqPUeBKObOGiYQw_vfXpzMwUwMxbowykava7u15U-NXT1rpDLGPFpUMcC8eND805j23WLhuTN23XYRdyqgrisArjtgHu4WRi7_YeF0xFCajJFXIEQIl0dr2n_9x6WBp9kwI7KSNeI6-5Yggug3tHzrPAcsZmJQkOEgtGRbI0a5uIMKMCZc9QPYaWEsMAId4l_pNQGFztj-f_CzxkIBdi9yXhHrcWAOEeDzsRCOiBq6ejQLx3gSHReURV0L9Io0IWjXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ جنایتکار بار دیگر از شرکت‌های نفتی خواست تا قیمت بنزین را برای مصرف‌کنندگان آمریکایی کاهش دهند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/678220" target="_blank">📅 00:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678218">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwYdSh-v9jKspQW1v68-wRePX9GW4LDyHSRrIN_NelK8FGhJffc5TxkFkukHnDeHE2nRzcxeX4_G02pYPUtJSKS_A8gaZ1xpb0KiZ94lV6fQKken1zcO0rtzZSTLW4U9oMfgM6Mrz-7l5Sco7BKCPb5VpKgETQ2IV4tMP_UEhZi5IvlZGC-JMqi6JgXQ2yzLUCrgxFW0anpPOzdacu8XLMv7BvNPWQbN52ycGoO8CgFVT2u35p_RAcWLfsDFtUtmJlj5JOHCUzIQZu2NaiqL2EjQXFNrdoIQZxp7mCRQU7i5MhDpZ_OYBfKJCZGRar_P_1JVLzwYE1-DfLevlnJNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZgsPI89TyGw1VsR2TKOm37dgAWu2EoUlP0YdN7LmbPg7IlKiN0OeBePn9698CW2XfQE9L8zSCehxlCaKgPkBc13vC2Nu7mF0NE-0Xpe3S4f-L8BjF7Z4yNBzwSZomudD3sYqINaFJ8TIf5qq6tszU0MRFTg9SZow4SQVPdRI8L1l2x9HDx8XlhH6GxbxR3UHWtbK3Ap7cC5uSs3jTYSZpNsjdWeIGULLI7pj8GwqXTPw59eH5p3vjTo5A4JVMTxhVZ653XGIEIRIUQyQkw_Y7VT62YRQa39OTzsemBWyaWfUQgRdi3L1TXbBtVW8_7wmsywO83OjNTfRZV7QieKlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فکت عجیب: اگر دو، سه و چهار انگلیسی را بنویسید، زیرشان یک خط افقی بکشید و صفحه را ۹۰ درجه بچرخانید، دو، سه و چهار فارسی می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/678218" target="_blank">📅 00:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678217">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/678217" target="_blank">📅 00:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678214">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQTGa8mb_x9-Emv9k_yQD0PBQ16S_22MecA9qiHwoFxJF0SePHYkrmN8615bc7U7w-4Usd4yJF6ost4XNE5a_dgOUyuMC9jNTJ4Ai05yaOW6q-vvqbn5I3qJW3BDRI8NiMCmygx0lqURba_S6frWGtBdBeJF1OGDiQzJo5TTgkPBxO95OShA5Frgj_ehaQU0ibA5RAoWNRUAH21b3uE82aXsLjB3y2kTUR6tjxI_AdthjD-free9JeX3PJaZKlpXOGCyno9YviIQ05AqbRQK4rStB-DoUfRh_YnthckUvr-GIP2WbBlY4sKHDrD7RtTH6TlXX3BkDrmH7Q0sKjDClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر پزشکیان: ادعای استعفای رئیس‌جمهور واهی و کذب محض است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/678214" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678213">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuCbXT0UkMaEEf9J09OqShLquEraaoz04XSgqfc3un8as8QVDMHPsDRKxFGmp-AdcOA6kKLAi181F6hj7oUzPkZXlRWNdq9b2NgEBe-I5fmouf3CX6jz7XfJTGha-b5JTjw3Osk01NjNrBkGVo1KuNNSQ1ucvssFYGq9CAxjVuD_IJSdq-axHLetJkZCkdA0UC7z1x0dsKq-H0nRGB5U4Y2CL8c3Eb9vODS1EX_P8fQrRjHQS9RlyID_JgbKa-nX_Vv_kBbN4fwleGeiILIsunQtcV-SJKdWkGPF979siQkraTgQnk7SAbJqS7t8yt1KPL5pG_XVf2rI2N9TCfM0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/678213" target="_blank">📅 00:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678212">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhZFJn3sZ8mBDMJyXav-jBVmTbLZz7J0XljSbsRFBcWaxmoP_dEADsfXGro2OzM339o8F_nxaSFLvhzfwA1BAljISMqxkkvdRCCHLSfhZ48a2-5zFEmJb03OuXjiFYEfdnZ5OMK2qQDanZ-vmACTu0cS9EU2PdC4unQC8mScMAJxnITpcGqoDD1g4mls_xoIyt7xWaJH8NDX92Y_M5TiLMHiXEpSGvNm5ZX3eTlMeGZfXoIYxBo0gRJYumMxMch9e-ewncA87XDDXItJ31hriZdIFWqZi3rbHfFepASxumj3s8vj3noOgLBL0kU4YLFnb-W07pQtLTOMa-ZcDOWTwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الایجا مگنیر، تحلیلگر بلژیکی: به نظر من، سنتکام متوجه نیست که وقتی می‌نویسد «۵۰ هزار نیروی آمریکایی در خاورمیانه حضور دارند»، این ادعا تا چه اندازه مضحک به نظر می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/678212" target="_blank">📅 23:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678211">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75331f2505.mp4?token=iARbxPeyiQUA7lVsaflvuYimh_cKVL-8J3y7yrCAtwVyNs7RU-ke6tvfpqz2zkmgw2ssnRtnAVYDABDkorNJqh6SGny44kCA9x_y09z6a-I-Kpvzf7rNj7Q0j2gNENJb6ILUhq09uH0ga8rgO8mBAgkGSyZxOD9NzRMKWprxo-ooqplUaa_yaPCD4DIsjV61LmBiYLBlF3pSvcv3SSkaxk4y3c4I0601wl5ik56WIHgBM4PiBwCrvG05h2uPb9eYVfuuIiJh-_r2JpTECdfCqSU78N2V-ZAkD0sZ6q75xhPSPqg0Pnp75SQg_eZE0SSctNjnDwRw9kVCXCrnYTsdWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75331f2505.mp4?token=iARbxPeyiQUA7lVsaflvuYimh_cKVL-8J3y7yrCAtwVyNs7RU-ke6tvfpqz2zkmgw2ssnRtnAVYDABDkorNJqh6SGny44kCA9x_y09z6a-I-Kpvzf7rNj7Q0j2gNENJb6ILUhq09uH0ga8rgO8mBAgkGSyZxOD9NzRMKWprxo-ooqplUaa_yaPCD4DIsjV61LmBiYLBlF3pSvcv3SSkaxk4y3c4I0601wl5ik56WIHgBM4PiBwCrvG05h2uPb9eYVfuuIiJh-_r2JpTECdfCqSU78N2V-ZAkD0sZ6q75xhPSPqg0Pnp75SQg_eZE0SSctNjnDwRw9kVCXCrnYTsdWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت معترضان به جنگ علیه ایران در مقابل کنگره آمریکا
🔹
تعدادی از روحانیون مسیحی و فعالان حقوق بشر در جریان اعتراض نسبت به جنگ علیه ایران و ابراز نگرانی درباره حقوق رأی‌دهندگان بازداشت شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/678211" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678210">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
محسن رضایی: شرایط کنونی ما شرایط گذر به قدرت چهارم جهانی است
🔹
وحدت‌مان را حفظ کنیم و اختلافات بین نیروهای انقلاب را پایان دهید؛ نباید نقد را به سمت تخریب و اهانت بکشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/678210" target="_blank">📅 23:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678209">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d92958e1f.mp4?token=QHYQHoNxFtOIKCotlRuIMX-zOOBUSjB1-T2LP_IBVlhA-90NtnR-4_xTeLn4b2qOzZMaxf1MfDUlQxXIVdhTtKx10N5ruG8L4l6GpkkL_XqPaQCCdrZ-J5vgo8UN-r24yDJSTDzIxjN_AKH6SewGEf1GK3XUZPayHRoHb87Y2xlnZIX0rxFpMvLTC9uNuddtNqYbxv504NWGIwl81QMDMV24adsX6GbbJn6khbcQBALPRSugUIXW5F8MOKUX2wyb8kX2zBYAMHvxzgoq6mrQy11DNqrtMYjiLzADKe01Io1v4pVD0WDGdKYJ3mhfCw037Kzo9lL8bU5OECOAFmAcKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d92958e1f.mp4?token=QHYQHoNxFtOIKCotlRuIMX-zOOBUSjB1-T2LP_IBVlhA-90NtnR-4_xTeLn4b2qOzZMaxf1MfDUlQxXIVdhTtKx10N5ruG8L4l6GpkkL_XqPaQCCdrZ-J5vgo8UN-r24yDJSTDzIxjN_AKH6SewGEf1GK3XUZPayHRoHb87Y2xlnZIX0rxFpMvLTC9uNuddtNqYbxv504NWGIwl81QMDMV24adsX6GbbJn6khbcQBALPRSugUIXW5F8MOKUX2wyb8kX2zBYAMHvxzgoq6mrQy11DNqrtMYjiLzADKe01Io1v4pVD0WDGdKYJ3mhfCw037Kzo9lL8bU5OECOAFmAcKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سید عباس عراقچی در حرم مطهر امام حسین
(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/678209" target="_blank">📅 23:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678208">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8017aa4184.mp4?token=gWuTjZx8twpQOrtounSut6r0-mjBr2LtRRCRSSHQACUh4hOttrfoQo3N6unYQ4t-iSLSrIoFGWr_Mki1u2eUIofYQgl9fkbr_g-atSLgh1RJgAVzARC62dY7uMjPV6RbX6BJaviM0GJTSUE1N_-1c7XkfD7HR_TMzeCUjgHiKdDHfuHhRZIQoHszS49SR80REa9tIOBlsocjSR8RZ3zE4qjEU_8qjSlh_faD0Fe9z9wr-a9DjPlsHb_BKuUu8n7cbUEa8VbcxyNNpreoLCIeaCTlma3tyzuLNRgQwkceJlA2fc809rvZ-R6yk74e8JOJedXNWBrnJw0-KQv669hPcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8017aa4184.mp4?token=gWuTjZx8twpQOrtounSut6r0-mjBr2LtRRCRSSHQACUh4hOttrfoQo3N6unYQ4t-iSLSrIoFGWr_Mki1u2eUIofYQgl9fkbr_g-atSLgh1RJgAVzARC62dY7uMjPV6RbX6BJaviM0GJTSUE1N_-1c7XkfD7HR_TMzeCUjgHiKdDHfuHhRZIQoHszS49SR80REa9tIOBlsocjSR8RZ3zE4qjEU_8qjSlh_faD0Fe9z9wr-a9DjPlsHb_BKuUu8n7cbUEa8VbcxyNNpreoLCIeaCTlma3tyzuLNRgQwkceJlA2fc809rvZ-R6yk74e8JOJedXNWBrnJw0-KQv669hPcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از حرم سیدالشهدا (ع) و حضور باشکوه زائران در شب اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/678208" target="_blank">📅 23:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678204">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f726e8cb.mp4?token=DQluHcuOiC_6leRffmWTpxFxskbuK9fCzX1Ue4AZjN2DtRwxLFoUvtC5cEsB2ov7lhCmCmQokz6e9Joj3jW_gR_d0RVU1UQHnSd20aPbrqq3AUaoiHInO1MyKGB0TaNXgPz0n7zf7RAnvR6ZaPjpTP1JwVZvtJE5qa06bFPxZh_5pQ5oVqRQAngJ05pyrdgrctfECveT4LdGaclgI1_cDCxczch53JWk_Ezo0Zsn3-MmnvwFyVfQUf9QAMZCKRlE6ZBtjMF9RgNEZNOk8lsp8XTcGPk1FV4RymsxN6tww0RlhkPTAZQ_2YSniVoBSvPSiFn1uhjA4DpkeaIv_IhNh0Lp7onWw-rMYSh7kstidkWxPD4wrfhdWz2TnENT8U6wDoKssDruBGNykQBS-bBPG48sdc_Q3ikL_0d6raphuU1TEu6uWJYDM3W893tIfaNHqguvoZUb0RQ1TpfmsFWXNRy_ZnDcNn_-rNqDWFcf-cb9JoI5-zAvudLeAPN_b9t7mctTEOFhAElSJS2-1JmJIrHBCe65Em1lm_w-K9NmqTJVf8THAcb718dnRVfezUiBjmb6wNBoZdXdzQcPAXJICTFL5bn4civxjI4wOdd1PYBcY1wAgffQqHEW7Dn4IbJHaIZrQ1CKXbdW19ZLsIPjSHSFcKSOx9_TLTpMeSt_qU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f726e8cb.mp4?token=DQluHcuOiC_6leRffmWTpxFxskbuK9fCzX1Ue4AZjN2DtRwxLFoUvtC5cEsB2ov7lhCmCmQokz6e9Joj3jW_gR_d0RVU1UQHnSd20aPbrqq3AUaoiHInO1MyKGB0TaNXgPz0n7zf7RAnvR6ZaPjpTP1JwVZvtJE5qa06bFPxZh_5pQ5oVqRQAngJ05pyrdgrctfECveT4LdGaclgI1_cDCxczch53JWk_Ezo0Zsn3-MmnvwFyVfQUf9QAMZCKRlE6ZBtjMF9RgNEZNOk8lsp8XTcGPk1FV4RymsxN6tww0RlhkPTAZQ_2YSniVoBSvPSiFn1uhjA4DpkeaIv_IhNh0Lp7onWw-rMYSh7kstidkWxPD4wrfhdWz2TnENT8U6wDoKssDruBGNykQBS-bBPG48sdc_Q3ikL_0d6raphuU1TEu6uWJYDM3W893tIfaNHqguvoZUb0RQ1TpfmsFWXNRy_ZnDcNn_-rNqDWFcf-cb9JoI5-zAvudLeAPN_b9t7mctTEOFhAElSJS2-1JmJIrHBCe65Em1lm_w-K9NmqTJVf8THAcb718dnRVfezUiBjmb6wNBoZdXdzQcPAXJICTFL5bn4civxjI4wOdd1PYBcY1wAgffQqHEW7Dn4IbJHaIZrQ1CKXbdW19ZLsIPjSHSFcKSOx9_TLTpMeSt_qU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان مرشایمر: ایران برندۀ جنگ شده اما ترامپ از پذیرش این واقعیت سر باز می‌زند و در وضعیت فاجعه‌باری گرفتار شده؛ او هیچ راهبرد نظامی معقولی ندارد و فاقد هرگونه دکترین پیروزی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/678204" target="_blank">📅 23:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678201">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVup0fv5IYrQgx_n0SWUvSleToy8kX3t5QaRgZIT84--RdJKmcoQjKZUVxinssRkj3GAeK4ZpLViqwodvKsUsb0AJRTkmdw2Sgqq44kfoTBcd2YhEQh7TPxNFUIaxM6z4zfBox4aHrMyNoj9M58E3Sg7HGc_LYXGcwCuP94hJgNLtureBP58Cyd9sjyxtpF4nE5kcAacUyWNgm7KwWaUD1atHEZvLT0uQdDVz8xKJ5nq5PUW1GI9rOzmaMZQq0n8cJGxbOYz-246gGVRlOByxXvkzSrB8pdkPdnTuVKbkMOTX0Mg1apGoM_GQU4wiDJKgo-1Ih5clbzSWxqcGTcxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز یک برنج قدکشیده؛ این اشتباهات را تکرار نکنید
🍚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/678201" target="_blank">📅 23:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678200">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک منبع ارشد سیاسی در تهران به خبرنگار المیادین گفت:
🔹
ایران مذاکره ای با آمریکا نداشته است و رییس جمهور دروغگوی این کشور به جای پذیرش مسئولیت خود در به هم زدن تفاهم نامه، همچنان در حال فرافکنی است.
🔹
مذاکرات ما با طرف عمانی است؛ عمان یک همسایه ابدی با ایران است و تنگه هرمز هم صرفا در محدوده آبهای سرزمینی این دو کشور قرار دارد و آمریکا که تاکنون بعنوان یک نیروی شر و ناامن‌ساز عمل کرده است نمی تواند خود را به عنوان منجی منطقه جا بزند.
🔹
باز یا بسته بودن تنگه هرمز تابعی از وضعیت کلان منطقه است و قطعا در وضعیتی که اقدامات تجاوزکارانه آمریکا و محاصره دریایی و دیگر اقدامات ایذایی آمریکا علیه ایران ادامه داشته باشد، این تنگه باز نخواهد شد
🔹
مشکل منطقه ما، حضور آمریکایی هاست وگرنه هیچ کدام از کشورهای منطقه طالب جنگ نیستند و همه می دانند که خسارات دیوانگی های نتانیاهو و ترامپ، برای شان بسیار پر هزینه شده است
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/678200" target="_blank">📅 23:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678199">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
آمار دقیق از میزان خسارت جنگ در تهران؛ کدام مناطق بیشترین آسیب را دیدند؟
👇
khabarfoori.com/fa/tiny/news-3235347
🔹
کالابرگ مرداد برای این افراد واریز نمی‌شود
👇
khabarfoori.com/fa/tiny/news-3235308
🔹
چه کسی در جلسه شورای دفاع در نهم اسفندماه ۱۴۰۴ به جای سردار رادان حاضر شد و به شهادت رسید؟
👇
khabarfoori.com/fa/tiny/news-3235132
🔹
تصویری از تغییر چهره ضرغامی؛ او دچار سکته مغزی شده بود؟
👇
khabarfoori.com/fa/tiny/news-3235351
🔹
تعطیلی ادارات در این استانها در روز چهارشنبه (14 مرداد 1405)
👇
khabarfoori.com/fa/tiny/news-3235258
🔹
با نصب اپلیکیشن خبرفوری، از خبرها جانمانید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/678199" target="_blank">📅 23:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678198">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سرلشکر رضایی: به‌هیچ‌وجه اجازۀ بازشدن کریدور دوم را در تنگۀ هرمز نمی‌دهیم
🔹
اگر ناو و نیروی نظامی هم به تنگۀ هرمز بیاورند آن‌ها را هدف قرار می‌دهیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/678198" target="_blank">📅 23:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678197">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecccd3a4fe.mp4?token=b1KZ-49fYBvCI2l67MxtiQGbS_a5ET1-4sB7Rno_jFmgvWAHVNQDc62YBMUFYNymX8i5XNkBwFVLLCkY8-hbxMvIhCzo8K9rj0Qq-GV7EHr1rxU13KXon5Il9l7QT3RtM-8K-AAXPrla3E5enh8P4OJEujTlvSsATPEocFGMFPKq7lzCCuk7tXxdCeUNx4OiBV7ZMD-f8RrO37wrJx98czCKYf_ZoVwAvk3KpgR61ByOZFO6BlfbldhzE3t0wThVYBaHA5kL8TnX4LcnbhsPzpFvIUxOmw3NXoX3WDxlcucE0URQaRWYwFBopUHc_mLW70SooErCZU3v1JiKgML4IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecccd3a4fe.mp4?token=b1KZ-49fYBvCI2l67MxtiQGbS_a5ET1-4sB7Rno_jFmgvWAHVNQDc62YBMUFYNymX8i5XNkBwFVLLCkY8-hbxMvIhCzo8K9rj0Qq-GV7EHr1rxU13KXon5Il9l7QT3RtM-8K-AAXPrla3E5enh8P4OJEujTlvSsATPEocFGMFPKq7lzCCuk7tXxdCeUNx4OiBV7ZMD-f8RrO37wrJx98czCKYf_ZoVwAvk3KpgR61ByOZFO6BlfbldhzE3t0wThVYBaHA5kL8TnX4LcnbhsPzpFvIUxOmw3NXoX3WDxlcucE0URQaRWYwFBopUHc_mLW70SooErCZU3v1JiKgML4IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سید عباس عراقچی وزیر امور خارجه در راهپیمایی اربعین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/678197" target="_blank">📅 23:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678195">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
گاردین به نقل از یک مقام ارشد پاکستانی: عاصم منیر برای جلوگیری از تشدید بیشتر تنش در منطقه، با ونس و ویتکاف در تماس نزدیک بوده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/678195" target="_blank">📅 23:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678194">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سرلشکر رضایی: دست‌وپازدن ترامپ ممکن است جرقۀ آغاز جنگ جهانی سوم را بزند
🔹
خلیج فارس و تنگۀ هرمز چاشنی بسیار خطرناکی برای جنگ جهانی سوم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/678194" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678193">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
محسن رضایی: آمریکا باید رفتارش را عوض کند؛ اگر آمریکا به شروط تفاهم‌نامه عمل کند می‌تواند نشان از تغییر رفتار باشد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/678193" target="_blank">📅 22:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678192">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای منبع آگاه به الحدث: سفر وزیر امور خارجه ایران به اسلام‌آباد در آینده نزدیک انجام خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/678192" target="_blank">📅 22:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678191">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
محسن رضایی: آقای ترامپ شما در خواب و رویا عملیات بزرگ‌تر از جنگ جهانی دوم داشتید، پس چرا پای نیروهای شما در خاک ایران نیامد؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/678191" target="_blank">📅 22:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678189">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e83ea2b385.mp4?token=iHEYJwuxHM_1Mshg4DgnrZcv_3zjo_Zon1HQVO20QfSC9cG-J60jdXU3QWMWgbWFkTBiH0XGaJfDLAqCat0kpD6LMgti_LqvY-2wG7ofFpQipIx6s1XI5qgBqeN3gACIxKebXUWLif9nLLFVf27c0V0Umr4F-j7-9wGMefE6zNsZhAk6nhSp0wtpmL6cRvJipBZkm_-HY0J0gz67WnB0x9ojw0-MsdHm3CISx2-9T4YkvUEbKRT27OcCc3_UVq2HRkUIg8tC3Nyb18BNfA-xNHeSew0qZXe-bxT1JXsszbowhQEODw-JXDu2pV-GGM80cKJmYHzQechggmxnwOHhvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e83ea2b385.mp4?token=iHEYJwuxHM_1Mshg4DgnrZcv_3zjo_Zon1HQVO20QfSC9cG-J60jdXU3QWMWgbWFkTBiH0XGaJfDLAqCat0kpD6LMgti_LqvY-2wG7ofFpQipIx6s1XI5qgBqeN3gACIxKebXUWLif9nLLFVf27c0V0Umr4F-j7-9wGMefE6zNsZhAk6nhSp0wtpmL6cRvJipBZkm_-HY0J0gz67WnB0x9ojw0-MsdHm3CISx2-9T4YkvUEbKRT27OcCc3_UVq2HRkUIg8tC3Nyb18BNfA-xNHeSew0qZXe-bxT1JXsszbowhQEODw-JXDu2pV-GGM80cKJmYHzQechggmxnwOHhvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این اپلیکیشن‌ها حرفه‌ای‌تر، سریع‌تر و هوشمندتر کار کنید
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/678189" target="_blank">📅 22:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678188">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
چرا آمریکا در حملات اخیر اسرائیل را دخالت نداده است؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/678188" target="_blank">📅 22:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678187">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f4a2d6b2.mp4?token=oAwnvG8kxoZHhvjaCukJNdP2N7-0l3ne0TwqyCt5a8LLnutTgeFgheB8V6-hzZfGqk76hAl4-nXFMSTCMOPLwArQ7ulKVwwFv8YLmwm_L1QV-Ud1YjX1OreJ1R2uRnj3P-nBDknvJCxNUd-I7-41XStFZlRXEOx2RpWNjE8CqmGfYtsLB3AZ6hRP5bxPHOro6MlxyPgHfio5dSpSvnBay-2EBr0bRxNIybm6aca1SKO_RXt-pCn59laV0ZdgMkRc6iNMlsuOh4DcZogcLBbB6AaDr9Bij877bQB3Q5ItSnrXN1gfKw9hao7IjwzGZF3y0T9IMUpCE7G_oBgsnZQhRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f4a2d6b2.mp4?token=oAwnvG8kxoZHhvjaCukJNdP2N7-0l3ne0TwqyCt5a8LLnutTgeFgheB8V6-hzZfGqk76hAl4-nXFMSTCMOPLwArQ7ulKVwwFv8YLmwm_L1QV-Ud1YjX1OreJ1R2uRnj3P-nBDknvJCxNUd-I7-41XStFZlRXEOx2RpWNjE8CqmGfYtsLB3AZ6hRP5bxPHOro6MlxyPgHfio5dSpSvnBay-2EBr0bRxNIybm6aca1SKO_RXt-pCn59laV0ZdgMkRc6iNMlsuOh4DcZogcLBbB6AaDr9Bij877bQB3Q5ItSnrXN1gfKw9hao7IjwzGZF3y0T9IMUpCE7G_oBgsnZQhRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: انگلیس کشور ورشکسته است
رئیس دولت تروریستی آمریکا که بوی نفت در دریای شمال به مشامش رسیده است در ادامه اراجیف خود:
🔹
انگلیس یک کشور ورشکسته است. اگر نفت دریای شمال را آزاد کند، به کشوری ثروتمند تبدیل خواهد شد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/678187" target="_blank">📅 22:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678186">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=oEKWvh4iAI5eRo-n9mIFmQpm8tTfmcnFZXtekJCmxnTvIKVw7esEYzsmle9kCgXc4tNAPuTR9nX71kIP71OQigOMArs-pupC7W1IjcrSa0T-Ty1RQc1CtUOfviDB-dt4_6wklvuD7OcV_u_aC-lkxj1lwhffnvZ1MHygaAQP-Zq2J4G_9Un1jxfLOmWfk9pD-LuKVmRJZ9BNbhG9D6suvewrsX2UAyzkZ5FOHhpz0_24SZf2iWpG1SI7BIq_VSNzDcrpUROyJVTEYKEs5Ydt8PkW4V49ah1H9rGiVtaxv3SN5uldHgCXOKWRH_qUZbUFy7g0W0cNZS84ITTds1R2MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=oEKWvh4iAI5eRo-n9mIFmQpm8tTfmcnFZXtekJCmxnTvIKVw7esEYzsmle9kCgXc4tNAPuTR9nX71kIP71OQigOMArs-pupC7W1IjcrSa0T-Ty1RQc1CtUOfviDB-dt4_6wklvuD7OcV_u_aC-lkxj1lwhffnvZ1MHygaAQP-Zq2J4G_9Un1jxfLOmWfk9pD-LuKVmRJZ9BNbhG9D6suvewrsX2UAyzkZ5FOHhpz0_24SZf2iWpG1SI7BIq_VSNzDcrpUROyJVTEYKEs5Ydt8PkW4V49ah1H9rGiVtaxv3SN5uldHgCXOKWRH_qUZbUFy7g0W0cNZS84ITTds1R2MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا آمریکا در حملات اخیر اسرائیل را دخالت نداده است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/678186" target="_blank">📅 22:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678185">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003c87529a.mp4?token=eBaW3doIybFFdiBMgqZIWeS5VpBGQpiQy1VPyWAiHCXpdnhhjpWSB7b3_qqbCkZH2fClI_iHXB8spkxMP7m0ucj0Cm9bjz9zCvfUyGNuAXwN5a2mvEAe7SNXIyCv83bgXWwGttnbPbu4uPV1Av64ear2CZQDRdxhn38hPA3NeZxCLePYQ2dnNd2VGBk3KGUeuU52N4u0khARX_VRt_tUnm2Yws6JYXvC8PXZfL9LTNuoNPRI9QVaD-WvWPSjhVYuzKKabE9me5DXVcg3ATsfxLUHmnTNEDo-oP8Z97Y6tHQv9ZuEpDwvGBwc0VI8aupr5WeCGoDtZimGE2YZNFLyaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003c87529a.mp4?token=eBaW3doIybFFdiBMgqZIWeS5VpBGQpiQy1VPyWAiHCXpdnhhjpWSB7b3_qqbCkZH2fClI_iHXB8spkxMP7m0ucj0Cm9bjz9zCvfUyGNuAXwN5a2mvEAe7SNXIyCv83bgXWwGttnbPbu4uPV1Av64ear2CZQDRdxhn38hPA3NeZxCLePYQ2dnNd2VGBk3KGUeuU52N4u0khARX_VRt_tUnm2Yws6JYXvC8PXZfL9LTNuoNPRI9QVaD-WvWPSjhVYuzKKabE9me5DXVcg3ATsfxLUHmnTNEDo-oP8Z97Y6tHQv9ZuEpDwvGBwc0VI8aupr5WeCGoDtZimGE2YZNFLyaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: دشمن برای باز کردن تنگه هرمز میخواست یک کار زمینی انجام دهد/ میخواست ارتباط استان‌های جنوبی و شمالی را قطع کند و پل‌ها را زد
🔹
طرح ناپخته فرمانده‌های ارتش آمریکا باعث شد حمله زمینی و هوایی متوقف شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/678185" target="_blank">📅 22:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678184">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
محسن رضایی: مقام معظم رهبری اجازه امضای تفاهم‌نامه را دادند و رئیس‌جمهور محترم هم امضا کردند/ ترامپ در کنار آقای مکرون یک شوی جهانی درست کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/678184" target="_blank">📅 22:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678183">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
محسن رضایی: با پاسخ شدید موشکی - پهپادی ایران در آن ۱۷ روز آرزوی ترامپ برای فتح‌الفتوح به در بسته خورد
🔹
به آمریکا فهماندیم هم موشک داریم و هم توان دفاع.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/678183" target="_blank">📅 22:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678181">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
محسن رضایی: با پاسخ شدید موشکی - پهپادی ایران در آن ۱۷ روز آرزوی ترامپ برای فتح‌الفتوح به در بسته خورد
🔹
به آمریکا فهماندیم هم موشک داریم و هم توان دفاع.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/678181" target="_blank">📅 22:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678180">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b694f704fb.mp4?token=enwF_IHaFdki5U5h9xhqHiJ2gaGbzqjjXkM7OmKCShyzkXs4LWwGGedtXQKViRFQdzF7eSg1RVFjN26l8E_opQ_94wX-0dmavjV3dA9Ty5oieQ9X7EEx1Tq2cbBIjpWPpA-LK_J4Z8fj2DQWh6qtmjyRYnQSOxWoVJ8cGz9FG2A0wcEKUtzd2A_TH6quJRhJj_yf1NfWzqujdNHoiy5kunnlu7c8C_sZsu1RJe6FefQenHzsHJRfkc2ZpIo7gXVqRrUkN-d-mJqQJsD0NUI_mEdrvTLJut0sDpFcsvyw653xcUPkFkXT_68ia0Xe4IivQKN0jcUAMSfyxFAkOHs0JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b694f704fb.mp4?token=enwF_IHaFdki5U5h9xhqHiJ2gaGbzqjjXkM7OmKCShyzkXs4LWwGGedtXQKViRFQdzF7eSg1RVFjN26l8E_opQ_94wX-0dmavjV3dA9Ty5oieQ9X7EEx1Tq2cbBIjpWPpA-LK_J4Z8fj2DQWh6qtmjyRYnQSOxWoVJ8cGz9FG2A0wcEKUtzd2A_TH6quJRhJj_yf1NfWzqujdNHoiy5kunnlu7c8C_sZsu1RJe6FefQenHzsHJRfkc2ZpIo7gXVqRrUkN-d-mJqQJsD0NUI_mEdrvTLJut0sDpFcsvyw653xcUPkFkXT_68ia0Xe4IivQKN0jcUAMSfyxFAkOHs0JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای خصمانه و گستاخی خوک زرد درباره ایرانی‌ها: قبل از بین بردن و کشتن ایرانی‌ها فرصت بدهید؛ اجرای برنامه ریزی هایمان بسیار دشوار است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/678180" target="_blank">📅 22:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678179">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcFAoyOOri4xJkbJVYMcpx0OXz7zG3v3S6apAG0IWNsRykERLNGTC5BWYmmT5t7aEhpcD9hS7ShKRtuEeWrEfOf5olSlKw9jc0YsM1fj_nNOB_yKRCnhOOIR6KDNEheRwpjcVGwC-DIHbUO89k94qUhsgneoACIi3Nnapv_vYQt5MCftlyF4tbPL2n0aAZakf1tjqRbGM0_kKkGnUbmCZqbSz2pa6KCyQWLUotnvoLK5vOGB2om7gqzsUfBU-LF-0MPCSSaI92uD1VFUUIDXjPogMGStwBKv89C3_SHYfxG4HXuNfRteJnxkgf-mitUwmNCDk8xywXPd8V5WjIwKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرصت‌ها مثل ابر می‌گذرند؛ آرام، سریع و بی‌خبر
🔹
در حکمت ۲۱ نهج‌البلاغه، امام علی(ع) یادآوری می‌کند که فرصت‌ها ماندگار نیستند. بعضی لحظه‌ها فقط یک‌بار از راه می‌رسند و اگر قدرشان را ندانیم، شاید دیگر تکرار نشوند.گاهی یک تصمیم به‌موقع، می‌تواند مسیر زندگی…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/678179" target="_blank">📅 22:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678178">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeef354708.mp4?token=V2Pt6GySOmACanIRJUTzCPaUqBFUSG48eSr8Drl2j0nAz66QhS4lpY0KM8vwgZOXwpk7ICdEVcj4lB8V81yqHjNSAKje5xDnt-oalCK7_UW0roS8OZuis0z0YwNLjX7qHSLh3eKm_PqSWeAw0H_wPwlWoU4WB49s9SgTjSecn_FTSGuc8cB0QDjg1SqAjqmOt-439XQ8qmcxGLOKS8WJ5KTOAeAS6S3NopmEU9UZNMAVqGh9DcI2BYklDmWyE7cji4R2JYA1KtbkboH75ROp4qbH3HjQyE1a8EhmVWFVHYCNhhhXdzQvR0s60K_EBFT3P4S63Bp10jPvGiIRLCVoMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeef354708.mp4?token=V2Pt6GySOmACanIRJUTzCPaUqBFUSG48eSr8Drl2j0nAz66QhS4lpY0KM8vwgZOXwpk7ICdEVcj4lB8V81yqHjNSAKje5xDnt-oalCK7_UW0roS8OZuis0z0YwNLjX7qHSLh3eKm_PqSWeAw0H_wPwlWoU4WB49s9SgTjSecn_FTSGuc8cB0QDjg1SqAjqmOt-439XQ8qmcxGLOKS8WJ5KTOAeAS6S3NopmEU9UZNMAVqGh9DcI2BYklDmWyE7cji4R2JYA1KtbkboH75ROp4qbH3HjQyE1a8EhmVWFVHYCNhhhXdzQvR0s60K_EBFT3P4S63Bp10jPvGiIRLCVoMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک کثیف درباره ایران: به من زنگ می زنند و می گویند: لطفا حمله نکنید، معامله می کنیم
🔹
این حقیقت مطلق است و همه آن را می دانند.
🔹
چه کسی تماس نمی گیرد؟
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/678178" target="_blank">📅 22:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678177">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65010e1c6b.mp4?token=J9TjtN6Q4Yv57OH0NQ3cb0wxe-bKkdo12937rfeW9YrLVGaY3sJnWbQRI4DteOSxieBdS84eyPsA6E8oeRykjXUKkA0wq2TylPBxKh6c38PQViLKk0hXq6avgN9WsQyzfkRfqIJiq4aOC4FB8ErumV65CyqNs--JGSjGAHERSx4xS5iy8gY9pRtZUVCq53bo0WsmEkOfjQwS0o_G0ZV3JBFkR4Htzkdavsd6bgp0Q_3RF-IUL1_np7h-sJqNf_XiBd65nnzgxM2GtIHHFOrnQn4XmrfRAF_rfwiexmqb9eFCdfSrCyQ33I2DDqdnSCYO4aakBGVxAQfJGNM6GCTjuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65010e1c6b.mp4?token=J9TjtN6Q4Yv57OH0NQ3cb0wxe-bKkdo12937rfeW9YrLVGaY3sJnWbQRI4DteOSxieBdS84eyPsA6E8oeRykjXUKkA0wq2TylPBxKh6c38PQViLKk0hXq6avgN9WsQyzfkRfqIJiq4aOC4FB8ErumV65CyqNs--JGSjGAHERSx4xS5iy8gY9pRtZUVCq53bo0WsmEkOfjQwS0o_G0ZV3JBFkR4Htzkdavsd6bgp0Q_3RF-IUL1_np7h-sJqNf_XiBd65nnzgxM2GtIHHFOrnQn4XmrfRAF_rfwiexmqb9eFCdfSrCyQ33I2DDqdnSCYO4aakBGVxAQfJGNM6GCTjuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: من می خواهم قبل از اتخاذ اقدامات شدید، هر فرصتی را که می توانم به ایران بدهم
🔹
امیدوارم به خود بیایند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/678177" target="_blank">📅 22:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678176">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isAqfNhZEddtR09UML9mY3nwhlx1cLY7KODtg3jNMCXwNW6wIWYyapstboQY_uDEzK2kwfwnaX5RCVmnrY6tXA2slKpEh4vGbmWJTCvz6X7xqUwTw2Dn_rNlTpoQ23zpEvLhBRjOJqXNeHNFhfguQAUy6bb2D1apeTEDLszbcwqBkABclyVuo1Xy9D-CfmuqBKIN1GSe--CVBkG7FX12ne-hBejLLDyYVU4FtDyEtIhFJXMqJL0UP6dNsIPJIdIDKPuwb6bRH7L7sRJsJwjaZ3BZeHSBfAcLIitSmF3kwYbyQEb0B67rJrVYYUMGdbieAOwTo64WV0dPDEp17_ZwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نوبت به بیمه ثالث موتور رسید!
یک موتورسوار حرفه‌ای همیشه برای مسیرش برنامه‌ریزی می‌کنه. خرید بیمه شخص ثالث هم بخشی از این برنامه‌ ریزیه که امنیت خاطر شما رو در هر تردد تضمین می‌کنه.
✅
برای اینکه با خیال راحت تردد کنید،
بیمه‌بازار
خرید بیمه ثالث موتور رو براتون ساده کرده:
•
مقایسه سریع
قیمت شرکت‌های مختلف
•
خرید اقساطی
•
صدور فوری و آنلاین
👈
خرید قسطی بیمه
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/678176" target="_blank">📅 22:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678172">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moL1Sk-T4bRRZdfsfdMAXpE3Hc_1QezkgqQpVMqtscNICaWXmQ0A-T08de4z3Sf-UTp9AU1K-ThrWJV8Lphhm7pgPCb0s4s33yhXrnDo9DQVtsXXLNkWZg3rcatfwwPpwXHJ6DiQiKz2MtagcPo9ZVLi7P-SqzOiQNAitxt3Xrer_xigLYTGRqBF5c3euHgfyS1ngwK5yy1lxo4y2zg8TIu1wGK3rr7-4JQRikbZ0c9854hGFskGzv0qhRPuu8SVG6w_jSx9S2O9IeiAaJeQdtzdy8h5Yin9v4m0ysfY31F99Bn2WMyeAdvKfhd1CpwkH1KSpYyILVNkt3alXJH5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زهرا، نوه خردسال آقای شهید ما هم اربعین امسال این‌گونه زائر حرم سیدالشهدا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/678172" target="_blank">📅 21:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678170">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75a71f2f93.mp4?token=XYukc3qgeil8ByitIM6fuGnyZiLAkRF7HAdHMyGfuTbpj2u3ipCJ2TZ9-_t01iw9_Kd_qCmzzD6hHf6yWql9J5U_CmNUk_V8GBukw2XLjprpd_KOtbCWLNms_bPAY-LBquQe1SlvQElz5jOnNVEVCev0n5DzcCKAUExxBNk8Umy3lbxLijGeculZpGAst2JpTcr_3AI9KZv5CUXryNJb3mGY3xIlYXbyaon81y5Yoqlt2xRgWDz5ehFT39JIubjXnUfLGJUa1T3VARYmP9S0AP2w4tDFBSVhhL5r1DCZB-TRdIsEFpSvMKPxIU9CazRLOCBlCsBNvcjyqxtx7PcykA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75a71f2f93.mp4?token=XYukc3qgeil8ByitIM6fuGnyZiLAkRF7HAdHMyGfuTbpj2u3ipCJ2TZ9-_t01iw9_Kd_qCmzzD6hHf6yWql9J5U_CmNUk_V8GBukw2XLjprpd_KOtbCWLNms_bPAY-LBquQe1SlvQElz5jOnNVEVCev0n5DzcCKAUExxBNk8Umy3lbxLijGeculZpGAst2JpTcr_3AI9KZv5CUXryNJb3mGY3xIlYXbyaon81y5Yoqlt2xRgWDz5ehFT39JIubjXnUfLGJUa1T3VARYmP9S0AP2w4tDFBSVhhL5r1DCZB-TRdIsEFpSvMKPxIU9CazRLOCBlCsBNvcjyqxtx7PcykA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک کودک کش: من به ایران اجازه نمی‌دهم هزینه‌ای دریافت کند
🔹
اگر قرار است کسی شارژ کند، این ما هستیم.
🔹
ما کنترل کامل داریم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/678170" target="_blank">📅 21:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678169">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21c4ec7f1.mp4?token=VdgpN52-IzIxOSOznOnuFiaxAbA9poDNrn-ILtU-x1WVs043RQ-u79IiUZGTcnYN6bpBxZuvTjONgwbpAAYuQw3-ojg6kql0oisugKg3lmRVA9Z5e9FUheXMC5xpZDNRl7vicvdg5dFio9pmRbQbcTuW2AuKXEmvnRZRGQRHT7LqQ2x7Jb2gAcwrpYMC-REfOS6ic3e6LDSLeL6CV9jN5vmg3rGRKGEFUzs_GEu4KzfAM_jmYA6TOUGo9dd4Iah5C4r24voANAlENiUuKTHZOQsjB0VD5-3KM95-0t0-T87H3O19JQWeT7w5HW-ENABTMib3X6AExATnqjHKLQ1wyZDc7S_LZbxKOb_OsANSR3LAa5iIWATdnKADWJK2ZMexRJ5xoSofK1CXKR9U_ul7zxiSA3PHORTLh9snUIxTDpNcOK-CVJqoanSRe6Xm-BezyD7erhtPUmLAgZ9DAYXW6moJh6byMKCtaqw0PyCIMZVhKzEhusetxJRnAv5nGxDDlFHxI_8ILEs2YxQbMznLT-Ej8Pexxis3CsdzXP95ELcpBw1rn57OPLkxjScSUbYQ8KkSPLCCZebIh3eNXOTHLnmzaWZgoeAmDwdja3Arlaxw1iqp7hZZvTlv5ocD-PU8RxVaNfzddKaNEHaI5iqFBdjKlWu6Aji5YogW42M48TY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21c4ec7f1.mp4?token=VdgpN52-IzIxOSOznOnuFiaxAbA9poDNrn-ILtU-x1WVs043RQ-u79IiUZGTcnYN6bpBxZuvTjONgwbpAAYuQw3-ojg6kql0oisugKg3lmRVA9Z5e9FUheXMC5xpZDNRl7vicvdg5dFio9pmRbQbcTuW2AuKXEmvnRZRGQRHT7LqQ2x7Jb2gAcwrpYMC-REfOS6ic3e6LDSLeL6CV9jN5vmg3rGRKGEFUzs_GEu4KzfAM_jmYA6TOUGo9dd4Iah5C4r24voANAlENiUuKTHZOQsjB0VD5-3KM95-0t0-T87H3O19JQWeT7w5HW-ENABTMib3X6AExATnqjHKLQ1wyZDc7S_LZbxKOb_OsANSR3LAa5iIWATdnKADWJK2ZMexRJ5xoSofK1CXKR9U_ul7zxiSA3PHORTLh9snUIxTDpNcOK-CVJqoanSRe6Xm-BezyD7erhtPUmLAgZ9DAYXW6moJh6byMKCtaqw0PyCIMZVhKzEhusetxJRnAv5nGxDDlFHxI_8ILEs2YxQbMznLT-Ej8Pexxis3CsdzXP95ELcpBw1rn57OPLkxjScSUbYQ8KkSPLCCZebIh3eNXOTHLnmzaWZgoeAmDwdja3Arlaxw1iqp7hZZvTlv5ocD-PU8RxVaNfzddKaNEHaI5iqFBdjKlWu6Aji5YogW42M48TY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: فردا آخرین فرصت ایران است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/678169" target="_blank">📅 21:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678168">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9041bec7.mp4?token=BY79VNZtkbqSV0OV99yfDSaG7t1R_MaIb5QcNdCa-xBsiLYv82X3YScHE_j503EUnGe7wkO9Z71IIuWF_pWomVgDP5-MvISPIZ-ZZjVlCALWMDuFCO9l8O4ducPG5n8Uk50EOvYyrexWbDdYmtUDwr2fk1Luc20hMvAgu0XxLqe24HqEbuEcvlVUH4UL0gMpPfowAU4MQW-EJ_o1q7Q5uu86bvyPMpLsaQ2b_f-D-GLL3XsZVBnV3MYL4n36ZkvFjQhHTB8tUs1QU0fgbmmLQA_EF03sV4wF9QhAvSmCeSKniOKgKcFMK9UM4nN6XOHel8XwR2XdKLc_Tdp3d4KIyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9041bec7.mp4?token=BY79VNZtkbqSV0OV99yfDSaG7t1R_MaIb5QcNdCa-xBsiLYv82X3YScHE_j503EUnGe7wkO9Z71IIuWF_pWomVgDP5-MvISPIZ-ZZjVlCALWMDuFCO9l8O4ducPG5n8Uk50EOvYyrexWbDdYmtUDwr2fk1Luc20hMvAgu0XxLqe24HqEbuEcvlVUH4UL0gMpPfowAU4MQW-EJ_o1q7Q5uu86bvyPMpLsaQ2b_f-D-GLL3XsZVBnV3MYL4n36ZkvFjQhHTB8tUs1QU0fgbmmLQA_EF03sV4wF9QhAvSmCeSKniOKgKcFMK9UM4nN6XOHel8XwR2XdKLc_Tdp3d4KIyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک پلید: مذاکرات به سرعت پیش خواهد رفت، این یا آن صورت. خیلی هم پیچیده نیست
🔹
ما در مورد باز کردن کامل تنگه هرمز فردا صحبت می کنیم.
🔹
سپس در مورد توانمندی های هسته ای ایران صحبت خواهیم کرد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/678168" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
