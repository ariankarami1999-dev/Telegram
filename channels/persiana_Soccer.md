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
<img src="https://cdn4.telesco.pe/file/F1dfKESAjAemtbSeg455lqDthi_uu8Sv7zOHVzes2MYBco25llZ6V52_JhjEBXRbxIH-ExbRFAYpNg_RzzYorGzVPPW5fqdXNgz_WrIcUKUEKDqfKF1Jx2PTGnsmt7cmis3qD71IFCaqI3JTjKgatYhu3rrWsjXFV0QFpUwNnnlqOfTS3OpeukYbaHpRgGJ4qx6M8gC5BDbu74k7i1FfNVc97SyiaXn8xz6K1llL3eiNbGZ08yVa3V2v7IvvRrc5UQgaWATUjlfWadVydeXIvhnVn4T5P28iNlUS0c0oOtS9VFyIszuDKdbTzE8YOthZa-I1AjQ9OY0a99_fzlEUbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 359K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 23:28:44</div>
<hr>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLLNuIuDQuHeA9_cNVA2TU2NzWe7jGhOH997aZta73702QU3nfycN7rlQW-OQIa-N73hI8VEibjrvZqTF-qzfCggJ3N4llda_oCU9fE0li7uoQnNpGXLTTHTyFEZU3QnBNe6oT-4-rCl6zVJ1E1dV48EtK7USY590T0upZabxWSPoqwEKT6jskrepc8TGjlrZIUw4ph3crVm_8rASDak8fHx9fx5UsMTWQ4etbSreph-R8xQ4kQVzDw5bXAFvrmIY7uelY42WHytL4uFIfbvyMF4Ei87_02PI4qfGeRz-1hYluXtyEx3FI1Ak9h6GRO5lYH4CGteDJA1lcShFVM2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=bizl5PlOMNGG2lynmSeobky986No7w85ZilC7IAypxAbU-5nGNQ3BXOjkdL5DyZELStDMxvqGUvL8BqL8n2GXqSrQOlpUjbAoqwS-UUUQ8RmqoqLrtn2FmTPJ8F-YW53Hf-f9RQAQvSLX1PR0pIrGq9_Nb9K9Fc935Zu8t_FtZl5oOY2RHEXSWlwe7ozdLdby0Fx8-mLvyzJ2XhryfhUk_aLzohqPGSHzI5jh0FTg-XE9GTGWVaQ8Ikm22XVyasxbXM_GjaWOpooDcjx2sTzsOSdXbTvcDjQX8BsjwC6XTcXYqpaUESYfDWuT0zUS5WBKRTOBlJs3r1V2ZIb0wTjvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=bizl5PlOMNGG2lynmSeobky986No7w85ZilC7IAypxAbU-5nGNQ3BXOjkdL5DyZELStDMxvqGUvL8BqL8n2GXqSrQOlpUjbAoqwS-UUUQ8RmqoqLrtn2FmTPJ8F-YW53Hf-f9RQAQvSLX1PR0pIrGq9_Nb9K9Fc935Zu8t_FtZl5oOY2RHEXSWlwe7ozdLdby0Fx8-mLvyzJ2XhryfhUk_aLzohqPGSHzI5jh0FTg-XE9GTGWVaQ8Ikm22XVyasxbXM_GjaWOpooDcjx2sTzsOSdXbTvcDjQX8BsjwC6XTcXYqpaUESYfDWuT0zUS5WBKRTOBlJs3r1V2ZIb0wTjvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره کریستیانو رونالدو در یورو 2016: از برد مقابل کرواسی خوشحالم، اما چون برادرم لوکا مودریچ گریه می‌کرد، نتوانستم جشن بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic9v7ryG-wSYgI_BHdv7LznsCkMYOBQPnexzB7qk2KVcBZ6r5I554UGQyvYCb11NzafAMWlshMG-Popjg82qcI_pdk0ZrpvONVuhha94cZ8_sfcJ6-OSFa2rtz8mPCo8kXC2Ou_HYNHwOOP8Jn7jFXjV8HIPqdGSzKxEn_EaAxfCAaRoBLPwTKjGizUYh6ttkoizQeL12SL-u77UMlYKF4tR2dBz2rsBpfi1AD9aZ2qJKML-FnmaGsBph9ZpTKDDX8N3o6UYHqI1-0MAiWW8LE4SJ9HkVSg_ArdVTg2ytIJ85bLxZRS6oz9Lm4CWn_-Fs0ctYlyfQ3UmzBchziYPXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvnP3TbPIKGfn55KonGhMOkYespjZj_0uirOO_oLMleKBB8jNJ3tp-Viah299LaOebIXs6Mwqnfv5s1ml9uVnlXT7u4bS2ntgAeyGKp4SilkQq8_w3lC77SJb0YZXvhWFuVgkFTu3uQPA6RRBl6wv7G0HqhSYtner5DVsE-5ecTrRD3sFBBK1R0pC0_VTj_qf25mkJ5o37t3CwRn2_bTONBWDo4TEcTc-iB4nra8xAeS4c-FUE-4IH0Ki-SoPmONb8w_3FyH1XTdlu23z8y3SU4BiGxI8d1NNBAy63gneBNyhDvVs6aUmiW58bYaviF8iB-biPhAWWFEzj5KKGfMpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdB-I0YVe5p7hQMHTM0GARecNw96Du1NRy9XVtMdYhwJeKBZX_-LAPNvcXaZSfVQxKf6i3xEaZNncowFAq-C2FCMjoHsMPDy_Tbtmb_ehwj1gML6bqjRgUyzcB5V54VrO0XiURD1faSaLqHpy8pEl4pUiiGhih7IF-hGk3lt9rRAWMzhl-ZcgXFt33krifMPdjS_uGuVZt1LrH9l2FyorNf0mgQfLM5YRW6Ki6sJVgBbGtkhQMhFW76zO2lyxQJ8h4KTB9YB1Rq4OK1nbdmoC7OYauuvTkr_DN_vyrJxBFQUMIIrMaMBSK8TZlwsMQx14G-yGngtewyQaNRLEX2oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/24822" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24821">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtDRFVBi9ijMOGpe82BCFVaihCi_UogxchFj78rB_b7oyyOlky65f7HKxt1jtQ-LWZ2V5EhrOtW3iOm5931juyUKvqksN_6GV_0IylZ5_BT09_93aL3hRPbv3DYTFbWd3YfEfq2UxpRY-Vuv025VxdShVUvV3gTNFIaxMuMMyULBb-wVkDxBU2P7rGzpBw4nx5nHDEsT_S-8TWKcm48LQBNDPsKkOvFV9I8LrcVJDqepnVBbuLMhuNdkv1myK2Xqtog7obXXWhWVCQh2RAo2CkVhqA4-G5mFkKIqdyK_RcWyvcZ8Qf7COCU7GRoy_nqdnTTuRWpkvdV3GtvxoF_tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/24821" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaw3tZvzTc_bI10qtXn1WVEnhEEC0FJVob2Idj9iiX2diBkHvbp0uwZ1IrKJyajtSnO4S2n-FRzkpxfabci4c3ANZT6SoQwoTNh0ffcwYg-cSQ04fXfV-FWat1GD2ifsh-0RfEwTdaiN-d2BbBsGKhpEfywO7HifGFamWoFUL3ZT2KHA6aR5xr5AFYJdmomeGhX4_uCS8ARpXDT-vO1ciPs3gwL98URDOHW4IZ6eFaCaqwRADsmmuBgjLLeoc24VVNj88ZEP7XpPq4SKYC2uZefStv-DjBW4eTB07knwLGX-B5OBodtQv63xkiQcSNuoZWHiaITki2XcPFsoDqWqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا 72 ساعت به‌باشگاه تراکتور فرصت داده تابه آفر مالی‌اوپاسخ بدهد. اگه‌پاسخ مثبت باشه ویرا بزودی بار دیگر به لیگ‌ایران بازخواهدگشت. همانطور که دیشب گفتیم قرارداد او با پرسپولیس فسخ شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/24820" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gar4xpOZGhJYAuX-f1Gl3-a6AmFFJ73xTSrtu5ZFCE6st3mXDEEmvTkNe-urFvmgUKcmK0NH9SRCqTm1T_5U5oDg8_gCJIdtdmfuDwUqO44e7vd1OprBDZUVFmLPYoTcWjXg7gPqkIlollKo5dCus_q9yoUhZKA-V6-eEHQMbwBoR51j3xWGV9xYaBtefK5YlHAN0o0jDSvWuUPG4a1oI9LYN1VxLaTNXqG_e3R97LbTlDe9pqBh6PGaMKAJks-azs8NxIghTiZ4cAbBdgtdUNEAnz8PdaAXmlKH86V6l03XVlfFl4PuVB8zL8dwdoIHnsAKH5jATEOjaq9igsl1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حجت کریمی مدیرعامل سابق استقلال امروز به عنوان مدیرعامل جدید باشگاه تراکتور منصوب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/24819" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyyxxXJL7HyHqd0CFUMqC8u_IFAR1nvSWzV1GEXWJfOpWrNFAHZ7TNmP7EbwNBm8Y88KFxHsfrtpF8x8oi7cJh6pSw2Xft8GRT5LQK4nU50roqcVGIYeYjAC2AfsghhDVeO21NYtPn35Mqe6Ftv8GDfGmFIl1i5n11PpnstZ9SPCc3OgPtugHcpFvLCy9f5xzWpaXnsI_5w1E3LF2aKiA-xMCrvT1oIuy91-RzPm2NO9gSay2Divf7IV7DoGNXawNTyIGTS14hBzPTfqWNlc6-aWfBW2nXxTywLqbB2dQltBEOBWf3k8AYSwkyctp2LsehQhnzwjbZZxx7FtzRvcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امشب یکی از این دو نفر آخرین بازیش تو ادوار جام جهانی و احتمالا آخرین مسابقه ملیش رو انجام میده. شب سخت‌برای‌هواداران باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/24817" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xe21vmr-q31DsHyv1vehiOlwZbQEa4FgGaQToYW-ahqXrfP7lvUnz6zaUMTCm309Atq4tSnTEHqZKy-EPpK2UVIDqoF9IzpGvsh-VWQy4Nu5ika8vb7_OtaDnTehQfmNuTnoGVOcJ19Y6ev6BXAznvh1hYJABlFO1dEbyzx6ZLoYkuWIvMj4zxO9q1neQ-qBJxboGJTvJMzSymc2JkIr6CubSbiP5f0Gm231JgZDMQO_OAw43eVJWokMEkadsK8HA7gPTZlGbpk1RcPSeyIzBOMtZgkxZihsqcCRLtFLxZqQn01ymDkD_a-2U9wEyEOL9iSKUmhCZojBFLtO786qlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یوفاقانون‌کارت‌قرمز برای بازیکنانی که دهانشون رو میپوشونن رو وارد UCL و لیگ اروپا نمیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/24816" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvQj232-WEVJV-xHqf-arVtTaJ-Sl0YQBfyr2_I5I48nROqyGqvfXLfMBtVPwlnV_d42y_KxJWmh7b1_CjzAB8y82EcxPq11XvsvxfNnisDmcnl4dortBNE2c04Ny7SsZCY4mINpaUuoAEszS6wBrRcWJSTN9Vm5bSGBSAC6nP3Dr1iTvk4EjZyF7iFF05cUclRc28DFNEJT17fX89jLnipi24q1XDlvzhoz8aVAvI4_3gGLBJo-vgpXEIlkeqklSOMNpGXURy24Cv3buGFQ2Ir3XSYDa7rTrgMIaefq4ESQUlvN-b_JjIwebB9PHBYizd2IA20aAi4IAr57h5O-ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/24815" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzV3KgsJpliiDQg_9zQfHapo3l9OICgHhzeDIx_UebXN-J_GXoPVOENCHmrgfUyB4w8Moije1u77OnvKeAXI4O3ARH5fFVZ_JJdGWCDPTeN5iaqSNAq0ja1jmb-D1Q454lrEgrprdmkx10KYRKz5nMWEg0rKh_pXoZnJU3DOsoEug0O18jxTdQAo3j696_yAuZovODE3PP1aiqVsUU8wwe0bYnwRoPv61RBMQ1gEQzmcra3NXBKIIwEG3VN4xyP9evt8aJcA1v7oySxbTKf_ULNMlgutqgexdNbW52cQJpJXMeFFLSQfFyqucgUsC-jKarhr_1pKZ8vGH1o5Ok5voA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی
؛ شماتیک ترکیب اسپانیا برای دیدار امشب با اتریش؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/24814" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixYhyzY1v-06ImtxFBg1B36MXDN15TWCgku8QmkMSlfSF7GEeiUTUTE0ZgLO0XdgZRlsKvUQg7-NNhDSV0HSgJdnYB1Ujk_4dfClLMMx9OcEnCN7QAeg83Sn0ugtBTDhMq_KHJr8HCxE3Jay3t4MOeRS4SlDOwHOkOUdkQNBW9bxSKBcV1AQeTJr3hHAbKRAlk5glyq2RV889FDJ8DyPOUpdaLi-HsYGsDYjqetjiNSF4hJhGjxtWhy7DP8IFqFgMMRL91ZX0wgibMEHUWXtppRnNE2xNU8N75wmV1btKk8PeaiS9-PNqwEVzJKTuHxBOq-4KgaqKa5Hg38KWpO0IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/24813" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTEiAlGioQIygdXPVYaXgTeo4uyy6JZuE6bkrrS8rZ_t8XT_30sBKYIrZVfmmVYECJxASz9DWdD8pcBLU-6VADV1NaJAa7O3EeGatN4CpRTmqpyIqKFPt5CxX7xbYN3sZapRgzkp_gHKpcP2I6ZxEXTNUtDF9WStmgH5ewg5IdaU9tmYOyMl-D0jJKS_2dgzbCD057YhUYBw57Umj3XBBfrCprElHCuLJVs_PZVmaf8LoyElxF3INARipBjkzbjqhkaiT0MHiIxOSQbBuVzJ8XM0MblyIeQqCk_Cm6wq52Tpx7nfMUewd1MNdtn1-EmCkWWCTSIRxenjlgu92KX9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYJapWBhNYeDSkQ2AFYhPHUcyAKr9Rr6bTpURQd4SgrEdxOLtUTx3TPBgu1XYrnHX0xhOxiwvj_6e9U9rzVMDLQL5QEp60B8w2dHpCmm2bTTa5ZYg8cer7pNv_HiomJEK1Vobu3y-sBKb73gL6namCxQJlxteIb5G31AgnK-zOG5TDr5Tb9I-nUvLx0-CStaeDgODrO2QDirtIaC6tCnu6d34YuP1V15ps4UVzrcALSbLpd1CQ9n-5415fQbQb_veMwav7Ec_CUvIkeeNQ30AzBQeFr_L4R-VHy_vVgFV1dSado32gTSAJd97WRDK_HJmuf2UFcgfITIj-Idel-2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FE7QS4O6i0_a8gP8hMpBS6rBb_QH3pS-LpRm61WAa6T7LRarxvCAnvR4kWY6rFTqPMvNGMGT5phR9Odd65F_jdLJzWeVOSQDJHxffxycsJY7C_qKBvLUozLwPiP5u4P4HW_oQCM_-uzG_kMoN8MIpTQJO9M26b67qbWyxjC9j15KSWYPvFHKR-Llh5l2TZbjbw9b8Mx898E8eOgmL1LwWuJlzF8vk750W_IFWAmYY2SJ6MkJLLNWGemOiZDPrqQAbCipo4NkpmnNw6wuN0P39CUCPbZtyBwzAP9tlYzFYhCInh2egvCklFbJHGsafk0WWShkGn2QzllEC8Tc9vbfow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oa_eezBZMs9eSDKr47gjaSXyxpsgc3dEWt-eW57WtYuBLNcQm6-XgNNU_QZknwBj48tpIxItqFqpt3G8N3SLyN1dqCFR1JJtYba5bVyuAVWpUNvRM48j3Tqf-P4tTiVe0JZAGiBb7Hj5M9dE2RYhCRqP8wv7QgzNYuqPN2wLf4GsECft1Bxv9a7Voz5O2mj-5McEfzLAEi3KFH20QnxdNf5N_ks6vDGXP6nHyA6dTw2PK1fbJ2I3tB-0OXZzlIkHCFoccK_2wqn5dTGZDMV99wqAQcbqTiVLdFWxkVhXBejC80y4gXZaSlR73JliFZ0qcrdWXiF6daq_WokIg8gU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxGjkm19LTVLDhuxs7ri8Jmz-gZwWKTdwGIJqz9ec2v2qxmdbDlZSk7GmQNDs5Qn-9WO7EgL66aQKoxP4PAvKDxAFy1SgQJOew1yRn3SZDOiGvlTFRJBvO3IRAmjfHaOsbtrbK61N1OfIYaRD7ns80dKsd3xoq_cIAO2onX7p9CT6It3MBDmqxAveQ6DHCyi0jlVcgmsh8fIgU3dEqLR59YQ7LGOD9tbY3P4JucnaAJvyEgP3rDPQz8vmzuQYxSHOGXBoXcuZdBQJRtbrjgKpokfhd81UTKub6hb8E9JvSPd4qEL_5ZZeFVyRzTCzv6h7_cRav8KFSdWKrcADd3EGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KawBcu8T16tx274cXDLHPgKAWOyNWrBZlc6J_efq3KDx4ef4BqJ2wZKao6aAkRbP5jVvN0qY7BeF0symkw65usSF1BWe3xD749IAC2kCHHpw0h5LyUIqYkd3U6gTiRqmDfo4CvfG6JyKVDk2n8Gy9eK_3A763p8BS6jDVY7UoKRUNVkE0Xk04FVO-_JX5I8TW3jfaySxz2bu5edxOs9BhMEhzFR2lNRxiwHnz1DsQNUQXmRNHkYdTXug_Gvs-SJqYAnjXF7lf5iH_JqXCMqZ_nVEnU4p60z42JbDSUMzthBXNGtnKVSMvjpPwxAB80Avc4KhyDKqZTOIi0UXbk6Iaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=egvHbA8jf-Is_m_Q5GkvcqDhkKtOfy6wJgPdQlddHiAdoV1wqjngo02yn9E0Dix8ZF-lnIwkmuLik_d6AHwx9G_gdQCDGhycP8ecxE1vkFqCd_F9r2b52ELfnkcpOkeqdmNWCTbNtzliv5Npq32Yh_p5FIlnM7LEGAqKlbUltUm5fhxOgMaPbiEBGhnRhQVi6QGF7z_vB3HOAna-b0mXIf2aLZ_BPTwt_fmk_t1ivwS8y5t7g1WKp7yzezli86Q1KEQ0EgpOB4vlzPQURjNrXxGzlFdc2-_w7m6AasmY8tRt-znuOskTF4KjQpoWN3ZPlhPs8xdwtNnrRwBgmGW3qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=egvHbA8jf-Is_m_Q5GkvcqDhkKtOfy6wJgPdQlddHiAdoV1wqjngo02yn9E0Dix8ZF-lnIwkmuLik_d6AHwx9G_gdQCDGhycP8ecxE1vkFqCd_F9r2b52ELfnkcpOkeqdmNWCTbNtzliv5Npq32Yh_p5FIlnM7LEGAqKlbUltUm5fhxOgMaPbiEBGhnRhQVi6QGF7z_vB3HOAna-b0mXIf2aLZ_BPTwt_fmk_t1ivwS8y5t7g1WKp7yzezli86Q1KEQ0EgpOB4vlzPQURjNrXxGzlFdc2-_w7m6AasmY8tRt-znuOskTF4KjQpoWN3ZPlhPs8xdwtNnrRwBgmGW3qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6n0uLxmmVZ74ca0Wp4Au7_R6Am_fgl9GJv98NLKZL8tR2A8auH7k6_tB9dfv7G8d38WvIU99OikuR_PC-_s8Tk2aYTQWGUzXJT7za27T_5zeFeVtkIHyEJ1k6OTheiukvWvtIdf_NApb1u9OUJokqXgCMe7xE7MZlpew7Fyajnp4O58AOGk77cNVh2ou4roh6GuyzducRGXBXZuWQEUEZdNP8kNoFxPTGCR_QC_XKHcuKvIcIwJf4tCrGGvgRSAI8O0Q7FsbMrTM9eoGItlw5KeHIHzimvwLo5i_oi_-FHvMHEYTODhOSyCYiDucsqkwsVbS7lgeSdtabqj_DKcDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل در یک فصل در تاریخ فوتبال:
🇦🇷
لیونل مسی فصل 2011/12: 82 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین فصل 2025/26: 72 گل
🇵🇹
کریستیانو رونالدو فصل 2011/12: 69 گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=otiOJRiz9Sswf40YAiP8eJJLk1-BVE2oSADagtMXJ_n4VPV4kDvjhP3Uj9BYhfK2xsAqfDLKadgAaJ0fztxVcQrMZv1779u2nW5yBCnIGPZYCZ1QLaDtjroshAmqBRqSu_9bg9xPxaDOWASODuuA8AEWT14QfA8KKpceWmcHBs2t909ag1tpHuoz-KJDdHGcEE_7KU9dkeGv1KRPx29lZriFhaLyBRxzdN2g-hVoAhWZvm9HLjaT4OxxX1ysMlgUkXXXcq8x8QEgBr6qthzg2Fvll9QiwRL0R7J1h0JI6B_C0kQaSj-HjYAo2eLLoyMSz4eAoDkk2OrXz6ypnYL0gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=otiOJRiz9Sswf40YAiP8eJJLk1-BVE2oSADagtMXJ_n4VPV4kDvjhP3Uj9BYhfK2xsAqfDLKadgAaJ0fztxVcQrMZv1779u2nW5yBCnIGPZYCZ1QLaDtjroshAmqBRqSu_9bg9xPxaDOWASODuuA8AEWT14QfA8KKpceWmcHBs2t909ag1tpHuoz-KJDdHGcEE_7KU9dkeGv1KRPx29lZriFhaLyBRxzdN2g-hVoAhWZvm9HLjaT4OxxX1ysMlgUkXXXcq8x8QEgBr6qthzg2Fvll9QiwRL0R7J1h0JI6B_C0kQaSj-HjYAo2eLLoyMSz4eAoDkk2OrXz6ypnYL0gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyrSigv_HDdjmkwuaLRJVFhZ5nThInxClJe1K1IZm9STjtV0ICfsT6dheX-cSVcBGuirIVJZ6GVDhlE7sNzifCtOeEJjgihueFXShiBKSoFy0Fy7vPQlY26TkxVeiI8w9I-Dfs7FLtWA-Ea8POxDx0PVyr6lzyMWG_Xd7FdSSYspdXzIEJSArEeKJt3o441ZWI9DWph2g8EXLaCtXrI6HCwr8VEm1Vh0k1PReBU8ZnzWa0lmXMXIAlOQBSpFLJBjN5dN8wYXBDZxWvBJfOILqNAgcnKvvaJSUhkZtKuSLtkMKbyrcsVgpnoI5UW399otOzZoyOlR0eHiAkMHLHOKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=vjq8zW-Nozhl1HL4pDUMCkVko4oHoLRUo7IiDK_G9AN599Hv5GEX2WjdyYSnorcAI6hHeBGZKzx9uw-M55xdVipGRj8bIBXOGOoz2wCAJSIck6GJ4Byx7WGeRCel7laXtNcSnguiFfVqaqY50OD5RcQn-973rurESKBo3y6UFxoq-Cz3BfKJ4bpA-QJuNS1H-QDB2zSqR_97uYQkWVLgt7hJYy6Q6LptPZV-Jytii7ELoKGjcS650xrCdIkGePo7IY2xkwtGnQYF6GyzfpVxFfm8S-FtGbuzQMkqpBxi6UuaSdKNkKTyOY470BeIbec-qISgxC_RSGGDQAspCIOBTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=vjq8zW-Nozhl1HL4pDUMCkVko4oHoLRUo7IiDK_G9AN599Hv5GEX2WjdyYSnorcAI6hHeBGZKzx9uw-M55xdVipGRj8bIBXOGOoz2wCAJSIck6GJ4Byx7WGeRCel7laXtNcSnguiFfVqaqY50OD5RcQn-973rurESKBo3y6UFxoq-Cz3BfKJ4bpA-QJuNS1H-QDB2zSqR_97uYQkWVLgt7hJYy6Q6LptPZV-Jytii7ELoKGjcS650xrCdIkGePo7IY2xkwtGnQYF6GyzfpVxFfm8S-FtGbuzQMkqpBxi6UuaSdKNkKTyOY470BeIbec-qISgxC_RSGGDQAspCIOBTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آقای تونی‌کروس عزیز؛ مگه تو چند نفر بودی که بعداز رفتنت نه آلمان روز خوش دید نه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8EgLi-0D4KBTNr5nWn3i-qkuCwLCkCcOa_5PHDqe0r3IBu9YKr9Kk5kSglZphEvYgB3bkAfqlGMrQtxpP8ERgSYxtvBbUY8JxZQ1Kufw5r-Ek18FynpI4poH-T4rdLbk3tKYvOU__AnZTgAb6Cyet6PuZ2NhcOcAtwJ5zHoaMw9N5xkb-QVknndpq85yRshitYkru7RjGFg8T7TQZhJuaHOhobxejCfqUB66D4HI-xwnDtrWBdJUFZFRkTUbU4gpMnwzcIA_n010V1KfmJ5Seq03M0qFZv0IOMZ6iz1b0XJ1W4WPP85TS9N8kW0akH_0nN3qAZssloF8AINcEzY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVx4mGPuQ6VLm0fXVPxMijLd_LwjXpEJyYT_do0MqmMrJiXguyrs8fuZjH7I61zm-rS1juiqxN702lSguJxRvzPovimALRSgj3V4MOxmjxx2QCxTxslm59wuOBhieD19Sr9P9cfe-ydscVtY8_WMEm6YcL66R4KBGWj2zXn9m6v6hH35ofi3MxQuCy2FjhluLQZg_Eec1iBzcEjXmBm8_NcFsu7KrKiz6DUARjmkQHLOzUe82owl8sprFL75S4NZAmQ0SN5nS9Mf2Ak1taHrXGcSum1l0fQqlFfoDzfia8U0QMcKl69T8AaywnMwiVQSGOqfYYrRDgFbIioHNkSvKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-_YS1f924PRXZJMro_kvNM9NpVdoJpgux0C5Z7PzxR0Ri9jKM2KFTjEsj-Ga-gPVlIzqCW3DB2lpT1e_AoBuOjui2xz6cfPJNxMsFBGZcqwo608DDkpXYgJcoEO7R3zljoqoW_LlOohw6imzm6TNKJGxLYNlWgmLvKQyoWSdwTjmQdh41MYbWEEof2BX79PLfrzZ21kAIJiA2cvXJiJDSWgQL1ZcXqXcKlN2VqNZl4wTT1eOLxfrzZtEB-gh4bzccnSCbwmBB8XJnuEUdGGRdyFzd2qz_7jCp5Vn6JOrZVsdLc2gQFztjDMxITEwH2dW8EldywsOgNtqZyNUzsx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=TmkWmg97gcR9lvLMj8nOZrffaIoqXC1YzWQJR8e5uBnyDCtgqcp3oV9c12nJI61z71pzEgkszKhC03DTbYV-wjIbz4HH3MPY2lL9R0SAhpPXtTEPgBLnaLTpfjnA5XdpTX0DB8MaRhIsM7NfKqyotQMH7Ux8rGGZDhhr6aB0eFrIpIT8ET70nT_Qcbf2ZFEmkWvyXzWNg0Jv1k06qYx-gseIJGMa0WK12GjK8XapEROslpYVmxqnYp6Aa7XmNHpx_pSyBJuWnQUAepbKEw0PrGNn0oh7vwmW_jPQrCbNfQ7Fehu8b9QzMfiNbR2fZ1X6nPhBZLalBhYVxqY7W5_3LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=TmkWmg97gcR9lvLMj8nOZrffaIoqXC1YzWQJR8e5uBnyDCtgqcp3oV9c12nJI61z71pzEgkszKhC03DTbYV-wjIbz4HH3MPY2lL9R0SAhpPXtTEPgBLnaLTpfjnA5XdpTX0DB8MaRhIsM7NfKqyotQMH7Ux8rGGZDhhr6aB0eFrIpIT8ET70nT_Qcbf2ZFEmkWvyXzWNg0Jv1k06qYx-gseIJGMa0WK12GjK8XapEROslpYVmxqnYp6Aa7XmNHpx_pSyBJuWnQUAepbKEw0PrGNn0oh7vwmW_jPQrCbNfQ7Fehu8b9QzMfiNbR2fZ1X6nPhBZLalBhYVxqY7W5_3LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIokwPS7kSuo16nvDGQjCT8HwY7-vuHGJPnnMe5awpEqLrQjZKZ1pR4gU3AlCQmXJ6e8qH4J1wi4m0Fd2mz4iMdmXr5AIRxoBY_hrGNozCr8JZZRmkMOS5Qs-HscDJ18BuoZO5biNT9Qs0CAFwqhZkyQr101qX6m9945blee6xSzHXkzw1YQmLBT5n1Q3TDg5q6Z499NJAr1b1GX-_HBQMZemFCHEoh05YMUa21cdcXKqTBFvBuHw-QVR2ikkw7-8NqmCVkOPH2NOEJ2ZgYgtMIuSfmSbJQcpltrJni96YD4_AlUGfhBij0UaZUWhqYHCYsv8xPnDRPNL_fkBTeQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9G5DZyrdAlP_F7Qt4sNiZqHS0O0V4PfN-Rnb6mF9vfvfaiZMmeVew4CETXb2k8_fNP_x58RBNse5-01RqiuYAnM8hiHIXLjr45wcqXWRDfJf051ff8cIkfTy614Vyf4eoMpHTSM_HB6CjHghz5VTbfeQb6m8R9aM-6NbqPD32L-ajiC8rI199_nHKcLxZOb0_EbvC4q3ZXVXc1zwaJ4za_nZqbbjS-xxCatRRwRmv-vXE_riDngg5abjhlxebzPXqXKpYh8HBS4RQwsbt9WJXv3wohiP0cehVMtugRZ5BraWzfH3gZT37Y_jGXzSPmr0MVlWalof2oHPjKGfgIrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDAupG5wP883gbffodbhRc-GQ0FH0mSn3xPxNLDvPWdPsg9K1R8cZq88dgcDPtowwUQeNy69j5d00RPW6XQZivELgOpl-2-tzPdkAP1RRj8W6BBYOBpyKnoPVWZHcMyjjSxQgr7hOyWiU1p-bOwuwWF2y32jO5iak375EDogaDCzbwFNiJ7LTQMQPYPBAPtG5tN8s1QNn7XOkTA7J_oOmnvwBJF3kTXKIGiK3EBlLspxGoOkrbteIc5rXchGIIfjjrUuidAtPbIkBzu4DFQMJ322a9q321I4cIlPyZfpFTadCLaEuIRR7IGanz58sogTkcdTRkeyibUC2NSzKLVyGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXSkz-gnkM58152Tlktpvn7zoW-3TrZ7OB2kZWcn96u-d6HzlqJePfr1-ff5-TrEg9SYl5B2XXVKa9pgMSx2q1voOVV1ozr0SRQedDiLVM1SdTMscPz-ApO_B4hRmiKMAE5nie8SL2fEERR87xIiXrcOkF-uReamwBcZDoEkLh0K5rFcRn1_yUAAcrc66NgqS2slFCMw4XGvgwdacBT4os9a015aq2Mb-g4sp7z1hUA-mhJ0jXxctihmlP5nBSLpda7w4ashNHZrf28UlYsiLHXagc-780togtcL7dY2x0ZkGNClj7gylHnGOEdIjNrMn3zCPIAVdDpWX2-Z5nOA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1gLnPp5ubZrDDf9CDvLlwdMmIB7K1HDBws9JEB-88zJ5OpUnnaxDXoKtEvYmuboCgC7zEYj79LnT4sz52_gVGyTEmUfEUZZInbf25G8nCUrw3daAzoYJFj43aeEPTX3V5A184pol8T7GZSuZ-BgtH1Y45d0QyXrPWAw_9Xh0cOJPONB0_rVoqAZNaQ70Jd--XFxkVuoS6Nz6MwC5fE7PNwpXPnmQq4FSH9YbnWWB_N8Td6VwxcUDTard3OnxurPCJmsjjtUNr0Mg87YXa86AqoCV7uJv2cdRBBxZZItn1oHtMSJc45ZaKMj0X_qIrXHOEaUs1ifaVvivqgkj_p72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlOGANgJ55qqUcR6kwHYOINN7cT1XFp3-CZqtffXhYhViBVMCt07FctJF9B9hmrL4qw3v_HItx3EV5mJlyjGw3X01jMnCAt0pF50JAT7haFWgL53_ZhndUpQ6dKN6_WGQRvLdOkYjJdgeVJQ4_zuFv3lsu4yEBxcvkEKaq9H9FZxnGArruX2Oa4ckMDIFXKo8X8-sa8Mya1D66QacoUEXtmu8_n8p5N3zwHfDgkZ4HqmezfveY-ty3D6Es079_n2egXOdZ_wb8A-yYdTm5RozpObE4cwnZIQbI5MkZjhisgacBx-aKjcGshdQQ1o9tqF2H9uHANNerloiU0rk9FFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l96hcElqLAg1z50djgda-uCKO7uF84o3YwUPPSAcolQPddFYdl59_P4Nwjg9_eacBdmn2tlDFfyQqVNfNpHaGilWxVYUYawXikbdCQYTn7pAtPJuGtuIV-zxDZUyfxhonBY2kaYWmZEDXHZFtcH1LJKzIDUbduB09YCkcMoi96kdBwPQy2Jgjz-KZXzF0Mk73wteVGV9vb1fBiJpW5fGdKQTVlyTAMkr4_NQSdh8hRZ-KxCPznP5P9_I4yJZGGKDur-5yklC5y7i4KwNKn0mKqkm_c9Gv8zlZ8ObrTj3TW6Sgaqo69-JX03WHNUkq3qj2RihmEPZNHdSi81YffLi4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cD2Yyv_XZpnuvoDurqOma5SdqZyZ5Wh9Rwabe-Nk_O96mpuD3ppT-r_WXfTNWIjuWzYTJXZzNsPvgl_V9QiQB-qghn3IjP76b3qnnXcpsh1eg7sk8l5rwTVV7PQY85l1Zf_hBTMS8WK2sxbH-fZ0BtR_jl8aWrE5ffi3t7Vc1qfCcHjHQdDZR64EYOaTgkZIhtOG145MQPBoSjy94Rvbbmmw_KeSGm-nLhD-9XbHh69m6q-rrqlWxDQekTbeDMLRWWzCUjmQCJkpiEq5szIw812BbMVeBdXOrgcHqK4GMLEQ1VEGO_8cy7hlpnVPq2ZlpksuRTRqTCna8Cr7hhCDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=bVGQLBcOJsypTz3lkLpcZDg-xedZ8haS4TI78BPMxgZrP7SQANLCK_cWjl2HrPme5bCHV9ng_uTtr8gpn1A4rEfCRXMBPsLiaenRXIKlvuOFLpv6exjgy3rHwKpjYyMoOgLMnTPW448JQS5XUcKmONPgqDaWpbnX1urHKvSkIhltk2us7twM1Jdvb7_TqJvBzvpAeYYiW1fL4cCn8E_UzW6b7t3U4kjeljip4zmBAiC2u_1e_1ickIJQO6iHeridK8dUpH--oY5-QMAj3qqu_R3pvcTWZxF2Xp8X2jvUVf53XJATJ4q4bpfQtZhzTvHaBLtgpOSMkQv8aANxhfJKwXrOdKy1EQzYc7XHncqC7nf3gtbKbRvvGc1C4CSqdZjDFjFJcfd0QeKsfHzhbpRqmjwsg8ercHzoCM6Z4WSQxWhhEnZqTIF2iK9Y7CodeBQLehzNixieHnEDhO9wiSdl_kqbaXJzqtC2Qzhv_F2cMrxG02AtqCyN5Jwe491afB8qADkgAIFLdyevpk0Yb9P0sadrEaIrykyyl-EvaFYqOp0pw9oW2gM1IcwgTYl2diYNoXWazaaeQGACn3YPAE7pAHubLVIu6RHbIku4KCCl1HbUNQ6ou1_A_2KKbaZePRCuG8y5jpQjH1dga10PDzwSYop-MilzcH-W5niQvdXTbWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=bVGQLBcOJsypTz3lkLpcZDg-xedZ8haS4TI78BPMxgZrP7SQANLCK_cWjl2HrPme5bCHV9ng_uTtr8gpn1A4rEfCRXMBPsLiaenRXIKlvuOFLpv6exjgy3rHwKpjYyMoOgLMnTPW448JQS5XUcKmONPgqDaWpbnX1urHKvSkIhltk2us7twM1Jdvb7_TqJvBzvpAeYYiW1fL4cCn8E_UzW6b7t3U4kjeljip4zmBAiC2u_1e_1ickIJQO6iHeridK8dUpH--oY5-QMAj3qqu_R3pvcTWZxF2Xp8X2jvUVf53XJATJ4q4bpfQtZhzTvHaBLtgpOSMkQv8aANxhfJKwXrOdKy1EQzYc7XHncqC7nf3gtbKbRvvGc1C4CSqdZjDFjFJcfd0QeKsfHzhbpRqmjwsg8ercHzoCM6Z4WSQxWhhEnZqTIF2iK9Y7CodeBQLehzNixieHnEDhO9wiSdl_kqbaXJzqtC2Qzhv_F2cMrxG02AtqCyN5Jwe491afB8qADkgAIFLdyevpk0Yb9P0sadrEaIrykyyl-EvaFYqOp0pw9oW2gM1IcwgTYl2diYNoXWazaaeQGACn3YPAE7pAHubLVIu6RHbIku4KCCl1HbUNQ6ou1_A_2KKbaZePRCuG8y5jpQjH1dga10PDzwSYop-MilzcH-W5niQvdXTbWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZc5bsn0Lrz9XyGVFACi8X8wtAnVjDG2s9DEFs6NM2oC7o-E6O3rdYEF01Inw745fWA8pM9o6x84625loiFm_QuHzrBGQM1J5cEiuqcoVL84T3PJhGZ6tSTaJC0Y6ORoALvyTViBkKXb7A2aKB6LOCmhWBWKDy4VXanu3PR_1nd7cGA1ZHdpozzDYBe2HVDUQca0AjYTrBE8OXBrFmWIewOg6EEaQ7N6cVv-T4s-zmSMDahSQrbRk_q6HCkWkGWF0zGaiE8SFRlKiOk8xgjWc2Kgv4uCD_hyQObAtzHykdZWd730CPVC3YW1mf5lq-XnrbIKTc787hWIg7AhkHUZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTxMrX4RJWPsBNLiqp7F7kKWDaGOPE5SN9Cdket9jhkXhcRSjObbXneddJ7WmvV31bROxSiFT35zkYrcXyA_HIhLa1VEIcutbzBf8RhxKlZcYPzkCCTzCK_KJ13UHge04u5pv2aBCu6raJxN-xJw997wZFRcp7Ns0RSbWwWOmtH0ns0t48sVr92HXiXQiShJ89vLlUraan2ke4EMMCj95L7h0sxUMcmaxVsGGM-7kVbPwEByaYPH5g_XMDsC3ddFndn8ZLE8o0pZMUDzIpAeWQFJOOCB81E8x8dBI_ToxEwSBUQDWtZI1P_BY0Aeny-8EHt0LjPNvc2kzgHq1dIJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=PKIAwxdqty02ZAtKqQt8mXLVa9Lbk89VyYq7WJ33swb5CDeR4nfynWy6czjc2ggi-KZbRJ3v444CHAhMXJgCtwT8MElRzWxqlgsBFpOeruCTSrpTpPcCPZD5wExqKI29oIJI-306h9gaE-UBAMI1Bj8LtBhITjzaQG7bkaqUbHAsUxEIZpS6o8P3qc5FyU4ZZIax1lmQxJF1N20DInKPylFGb36OrpDHXnglIlAYWgl3D60CkBeYyCFQjqGp7UjLyOwHTqBeoViDN-oICz3Jd-fKZ85Wjn9Oq3zYqRLYmLM0hsQVBXbQhbuTHv58X6q11AsRzpFhpBOw2fxLhh7r-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=PKIAwxdqty02ZAtKqQt8mXLVa9Lbk89VyYq7WJ33swb5CDeR4nfynWy6czjc2ggi-KZbRJ3v444CHAhMXJgCtwT8MElRzWxqlgsBFpOeruCTSrpTpPcCPZD5wExqKI29oIJI-306h9gaE-UBAMI1Bj8LtBhITjzaQG7bkaqUbHAsUxEIZpS6o8P3qc5FyU4ZZIax1lmQxJF1N20DInKPylFGb36OrpDHXnglIlAYWgl3D60CkBeYyCFQjqGp7UjLyOwHTqBeoViDN-oICz3Jd-fKZ85Wjn9Oq3zYqRLYmLM0hsQVBXbQhbuTHv58X6q11AsRzpFhpBOw2fxLhh7r-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulEmoFdkYqxm7vAS0kK6A2JcTZy5TEssbDiHCuvivbRGf70rrB5QoT3zitU7Vq5rtLW7t8k0qStLhSrIX4HTORIeCsiJy_LJ80J86jNSEG2N33ImoBicGYbK2laT7BsITUuKqmGkgnl9-fhSNjlrNROe1bBPphskPKwKIwU5vITDKXaH0LtvM097ZXe3e9SPO6gxgTYAax0WfArb6d_5gHAXOUIm_5yaKKpNE2Zq05yAx6uCi4Z2SIU_hUVVgs_BpXLoq4qlt5xVScj-vOkunG3d_BIbb5X_jqCje3UAErpTbUMphFpNBt3vlEnFreqfnC2g8gqp52ZYERAXPDDZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVBx6BeSi8t49ffh5dklMOihJ8aQvCSoL_UMUVWAJVAjzPacTuNJ_jMW6N3zj-QZRDAyuM3xDZNizYh0Ia_3RIav5ZprJjPGnaz_sub2R5SYgrLQZ9s8Ij1pw_hdV_MN-nDpBfo4_QmzjInGUXb2dxGXhjVMYWxdfZ-AkvAZxCkiA7IFMuGSWQZsGMLdHGA7TZAhn9PTf7Y90-73g1lEhbtod_Nr_xgss1oFWsHj2nCF3HbEA3_McDyomrIo3ziPfrpsfyepHPahy5qw7z7-MOvMUW47BJ3KRpWGHG7QOVuHan3hZG91pNtu7Dmx7BGpRsn0KWaLlgfyXYPUYC6HnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24780">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8iIZQNLNhfM5vGWW8RX2HXaRNmeP2RZD3mEUpnJzLRba-LAUlgtBXkHC09F_pEdM09z_j3sRcS4Q67hc0QDBa4sgmpovZgk65NwiXTtaNXrnLDA7B6FKCCoC7tzBloXx0mnLs2QnG84v0PJKBaMpDNcoPaE0w3lfF-zO0sP-vSKWSKDw1yYEo_8IJL95a2mMBfOMZR81jn34ybp1XbnWyneBE-vb0zCUtlICeBd5lypnJfC81SIK-XHJDgI9FD8t2Tu37D0JvHwoPU9FVa9Ts3bQGK-dGAbucJzWoVUs7H4Szo5OW0oEyY5Jhbr1UcgLedwE7aWbBqpWvOEMhRTNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
پيش بيني رايگان ورزشي در لينك زير
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24780" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=fZLeE5ktAcRuT33GYkVlB_lKev5dN5ocNVRAMYZE2o8_DwZpY2pmQVblP4tN3apwnJh3VcqLPQmjgknXqmxkrPBxEs1RqhuOetrvli1cZ2eOkuyqjnOtJASRkmSTgQlRENqMMe5-_pOQRAMXtl69w_f0b8utideJNvuZLgu9UqyrxYTpgU_sMRNrbD0MFMxhohEuyhQa8zID-MBFXudZ8HD99kzu-r53YCdZ5JBDrr80Fc30OI2WD1LnngGQGVlrTDek_ArtIjGt7u2Pho5tq1otyYeWehlOfp9Rn8DsEU72NmO5N9sJ6VvmZRpOU-USexHzgK4_k19ihEZ7B_VTYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=fZLeE5ktAcRuT33GYkVlB_lKev5dN5ocNVRAMYZE2o8_DwZpY2pmQVblP4tN3apwnJh3VcqLPQmjgknXqmxkrPBxEs1RqhuOetrvli1cZ2eOkuyqjnOtJASRkmSTgQlRENqMMe5-_pOQRAMXtl69w_f0b8utideJNvuZLgu9UqyrxYTpgU_sMRNrbD0MFMxhohEuyhQa8zID-MBFXudZ8HD99kzu-r53YCdZ5JBDrr80Fc30OI2WD1LnngGQGVlrTDek_ArtIjGt7u2Pho5tq1otyYeWehlOfp9Rn8DsEU72NmO5N9sJ6VvmZRpOU-USexHzgK4_k19ihEZ7B_VTYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfTMX_wsip6qj4D-6YQvKG_XRKYrnRl22gGwuG7IQe4zKm3NZ7nBQeZ9AVHpoeh7InqT81BQoF6TKzVZn4d9RxqxzLK_e4Xj9TVSUE0l6IcMmR7QrwfSChtdvvEPvqoj31ifxFK6cZSDSKqIbsr01fS2fwmsdgMGYPTNp0RcRY3bVFXxSoeCvhYZ-IoscaaN6mwdQei1Z8SV907RYffBQaCmHX7mXGHFeoxtpY_a5ppr02Dtogw824jGyiPLFJCQRTOvkNwqc1xEUi-lVfvffTq8x24VK6DfyMSI2yICF74nE7u2coAm1mSbtQtfEXwZljgAwuIXGE3N2i4_DeAe4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=jytbmdTabNkm49gu0rMTEitQ6ScPWgny2zXxgJHh6xVBgMWXWjWeZRHfvJ3XyKsr2qmf1O0noGAsYBiE2vUpqORXKnAf2L5MloRIqf09CrmJK4XRFsLq_04v8QFLlEFi0LEL63EpzvIP56Sm_YQGHRjVzxPhh201QRbzYldc1x3f5M5AnEoYQRa7J902miYUu5P1nyBZx62zpS3QARpjNHjVEkdTrQJ7Yzb-fswfNC_2JTTpV5DBhnS928ZJ7NcH6jQjpDoJfeKdgNvAxtdIOLNMtj6VF64RJhR7spHALKWaCifDG9lZYzTem4nhXaRs7AMIRuW9gMQkAbYSZM_Nyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=jytbmdTabNkm49gu0rMTEitQ6ScPWgny2zXxgJHh6xVBgMWXWjWeZRHfvJ3XyKsr2qmf1O0noGAsYBiE2vUpqORXKnAf2L5MloRIqf09CrmJK4XRFsLq_04v8QFLlEFi0LEL63EpzvIP56Sm_YQGHRjVzxPhh201QRbzYldc1x3f5M5AnEoYQRa7J902miYUu5P1nyBZx62zpS3QARpjNHjVEkdTrQJ7Yzb-fswfNC_2JTTpV5DBhnS928ZJ7NcH6jQjpDoJfeKdgNvAxtdIOLNMtj6VF64RJhR7spHALKWaCifDG9lZYzTem4nhXaRs7AMIRuW9gMQkAbYSZM_Nyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aI1wEKQ8-6k0EF4sEq-s0HFt-RjHV_o2gm-S36Le3K0q0SnvTObL3kB5gwRWOXLa3LigxrT7P3OaVl11lZcflWmcWxCeN_XXwZIrhN3F967pZo5Q0xbAeqxv7vPFH12uGMsrsEjK445BcHrIuMw9aj7SbmTImsZ2DxnlXM9yd8n_FpmKHjya-936Hhys416Z9TpFq2huqr6rlIeLLD-2fYIWNR0Fpwo85txqhOGEwOvDQTqU3B11Xl_vp1zbZD4GRDJslWyKP9reYOnkYwejZFBsK5fSZkoQ8C2oMtN8e4Wb0tc5u3RFh2RBvr_v6TPzAclI_DOmS1yyX71iZp2GDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ripo_7T-T0_yi57c9kRHZF2oJG0FnR2KSlRmauNUKmY2DHApNMF0uyUHyldOVeeBgggc06khjbtWg1GEuyfxitXC-OouJSHHqunbZXTzqfIio5SJIQ-jf8R0De3kEG-bX6K6iUqXK5dS6PPBG4jyy7aD2Q2FIxrPEQSyQ24vDtdmPTSDW9yefRW6X3so0QeFOdidWxhdk6HJG5FstydUMSbhb5vqWjpWBG9jjLTL_re9f3mz66kiy6gBx1psIyox4Wq9mKvbvG9Cowj3DdjZ1rpzr8nLTYQMufdXmoibFZXmj8YjPWeCtevUm8sWFVvdfEwjiTLtvonbhqz361Fp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=UmGa0wxuHEynqxlrZ2BgyGqYAHRKsKIe6WixhGky6Wi2aB5yafnAKj_fbYSge4XpPR_g05iJsauDd0X7IPWJg3Yl609iX0FWNpVkLCDferLH-dLTPMCQcFMRxabZP1ovoElC3ic5kTyjdAG9ftVvtQKcWvOj7aVYDj8-jCe8Kq20SjwgkUdIbW1ICgRb8IN5zKDiJm6Oog_c0z6I0brJlKrPIe6azaRZ42UICEIZsE3j8JLPVLaD-2h_GfrD8hxXzOXFVjejklqwHKx1NYCfnq-_WNouaLsx8Xn6ZT0PbiMd_hiQIP3boZPV4nd5L761nzQeU_mYdF7ryHZibrZIYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=UmGa0wxuHEynqxlrZ2BgyGqYAHRKsKIe6WixhGky6Wi2aB5yafnAKj_fbYSge4XpPR_g05iJsauDd0X7IPWJg3Yl609iX0FWNpVkLCDferLH-dLTPMCQcFMRxabZP1ovoElC3ic5kTyjdAG9ftVvtQKcWvOj7aVYDj8-jCe8Kq20SjwgkUdIbW1ICgRb8IN5zKDiJm6Oog_c0z6I0brJlKrPIe6azaRZ42UICEIZsE3j8JLPVLaD-2h_GfrD8hxXzOXFVjejklqwHKx1NYCfnq-_WNouaLsx8Xn6ZT0PbiMd_hiQIP3boZPV4nd5L761nzQeU_mYdF7ryHZibrZIYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=QO_h1JvN4G281vvOrpZGQR6rMBmStJjStB_xWPyEX_pLEYxQkY0oRxGNqA8NQfy7hM7r10Ta-5A0f9l56pJk34VneHHRchQtjBzJq8umjNR-wuWXGduqfjZclhImos2mOHZFzMFyJ1Lk-1wZrmkuPIHwg1ARbq7FEK2lwjjDF0jYmIt5JOrpgWqgJ6BMEFXxAoEF_PCFNkzpIcPMIpR3twVH7nWTg5Bxi9n3wPvH6BPpV-6f-k2Gt_EDL7yErUKwjryS0OTGNgJjgA6rXbsAbUzN1Ibb5dwP7CAcp7RkQUDfPfysx40c2vQEDaIr4YF7doF3ZO-fUYJZorYJ7v6BFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=QO_h1JvN4G281vvOrpZGQR6rMBmStJjStB_xWPyEX_pLEYxQkY0oRxGNqA8NQfy7hM7r10Ta-5A0f9l56pJk34VneHHRchQtjBzJq8umjNR-wuWXGduqfjZclhImos2mOHZFzMFyJ1Lk-1wZrmkuPIHwg1ARbq7FEK2lwjjDF0jYmIt5JOrpgWqgJ6BMEFXxAoEF_PCFNkzpIcPMIpR3twVH7nWTg5Bxi9n3wPvH6BPpV-6f-k2Gt_EDL7yErUKwjryS0OTGNgJjgA6rXbsAbUzN1Ibb5dwP7CAcp7RkQUDfPfysx40c2vQEDaIr4YF7doF3ZO-fUYJZorYJ7v6BFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9mKDt74R7xzCWxCb5QuUXvMawF8Ly8Um8YgQBKi8YQGO0Iz2r6y63k96UQQ-4pYPfzI_czFJLfR2fLdvWydkTADqnfJIXlEQiTRLHFc0vDKnztcvP06Y67EID0ljGlpHa0kyVx3rXLA6OpDOAZb63IaELe3ykqfZBrvQqrlbBMEbJYf_Grx0IJc0NS_GBKu9U1ANYqXGt-LIX2pkwrGr40Ome6_4_OLSZiUt_zoLJA65KYQz2piIVzFdm4G4JaDg1RJW1QRzxju4bCks--cP3Z3atn4ZXP75sLJsJET9tG2oyxVTOBP_mHBmaqLhnWzr4CrUBY1BLpcCfyOQ-3uOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crG2gGU866mSenG_JJ4obzjcGMWE8bZe933PQqL7nj7BQi4zX-gjyrSBpRBgQiwcaIFH32eOjR5GG5q5nmHObjIPFsnHMssJQyPI8ATF04QTXP2bnkO47H7-4kkb7s4jNJtWlrw4fj1DoOhYoDvnu6Jwkyo6vsM2vUpeEAtIr_oZDrR9MN33quFEWNwsE3kO8y-RYxHO8U0Lm2_ABk8wYDGhUlTdYKdiVJhEOWTTQQnvsmtJRNKuVE9MQRdHg461Te3c9m2MkPW25MuBfjEGio4q5DwtwWBzMeq5cr_K2cSnl5ZSIvNpVXGRRdjWQ7Xejz7WIZl2yCvQy6zGYxZKQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6RASTF6dveK0U7wtT41UtchmIfPV6Cnd4VkvyDz-3_tciFcpVtODHT9RIO5baq8PRB7DNkMR1J3lzklPZ8qLFTdZUniwtGLd0gSYCy8rN-EFFEAXmAYADEHvQXDSqD2DokSgD3IKxd1CKiJ4YL0Yitg3BtB6OyDfl5oIgthiTM_99cJdzptZRef531m6ambl83oVETbPzQFsVHB_mE71mW9TH38Fre2YLfprimctNJCzm-H6tUWPzpIb6E-s4JdN-b-V1vEyTBd7jrlG6o-MCfLyPFTC7__TDPYG172dKV66A6s1VJxLNhj_AQT1cpq-aHPFIKRKGxPxt04vr2uAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=TEgvilmoPRvJGKPygeoySdvmkg9cZ-huI7fqE-aQIBG3PYR0u1trRmRKb-QHt-fgY4LI9T-DDrx5JHZh7flCVTb3lLVuIsEPy3TiDL7jdnaRhAcS3fxJRQyp7LTADw_owR6Fz32sGDt3C_hQbLBCAmIKl9BrLtjY4vuoYKYmjqy_p_eBMig6n8fCwEUxSwtJtTXYAkm3I-q3Xvij3AhsK0cnyfB35eAJogdkG7hmNQvXijYtiaLq52JyCxMuIIlPlMeCeWTDg8ujH7wG7VjTw35vqJ0WeFIXYpq7OJHKGE9h_iwgd4vob94aS7Jgtt7H0zrpgEEf7t0lNsdsY7mRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=TEgvilmoPRvJGKPygeoySdvmkg9cZ-huI7fqE-aQIBG3PYR0u1trRmRKb-QHt-fgY4LI9T-DDrx5JHZh7flCVTb3lLVuIsEPy3TiDL7jdnaRhAcS3fxJRQyp7LTADw_owR6Fz32sGDt3C_hQbLBCAmIKl9BrLtjY4vuoYKYmjqy_p_eBMig6n8fCwEUxSwtJtTXYAkm3I-q3Xvij3AhsK0cnyfB35eAJogdkG7hmNQvXijYtiaLq52JyCxMuIIlPlMeCeWTDg8ujH7wG7VjTw35vqJ0WeFIXYpq7OJHKGE9h_iwgd4vob94aS7Jgtt7H0zrpgEEf7t0lNsdsY7mRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWfHHe5Mb7rsLWOKJy6kT27u4ScvpkBQNSYqz6eJdcGwiuG9ed2Mi_Q0FdUipggbB7aBCxypc76KvDmHhjxSU6OcogWuO9oRIefe02JEp0OfmV98dYv3UzXYjmaFizFp90fCdH0Mz3EEtwEZV2tp3OW7JmgN8QJfUO5qlNpMQKV_lh2GYOdSP5xqpn6QX4ojI14psNzJx03bxTpUM0PUzORybTxnIlecVA9dzd_bbkxwxYbZN2ATIFAClrpDDjD3WSI-N3e5Z44sIPLdQBK4hvvmXhOdgMzKsa5jvsKMH_HX421CW-fVN_jVobdSqA4d-K9-_kUGM78ziTWneApy_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=WlS6iRFEEiaKLsZz_gfaZp4KQxHXnhvrtMMNZqDtNGlu1ppzYlFJRSJQ1mGLl_jOkKMLK8-nJMrNn4WnuZE5DaJ7V3gqomkel4LI_P6SEYgqxhsSOdZwuxpPFyZD9eSccx48dDq6qiWkDzbQPoR5jZvPVSZ0Ga9GhnlOxxTcQrvwOuT4Tdlilmzyty9x_LfmTTllIRYr33RKIm_scrjsKuBVniw0kxxMRnAstiXOzJM71g1cn8pZsT-q1IiSFEZM1rrdy0al9W1GnDSvbXXRqklc2PMIHIvrhnVfoBXQK0rjQfT3fpWUNG9dPnmnbRZxTlIf8H7PAOBYfugJ37rlmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=WlS6iRFEEiaKLsZz_gfaZp4KQxHXnhvrtMMNZqDtNGlu1ppzYlFJRSJQ1mGLl_jOkKMLK8-nJMrNn4WnuZE5DaJ7V3gqomkel4LI_P6SEYgqxhsSOdZwuxpPFyZD9eSccx48dDq6qiWkDzbQPoR5jZvPVSZ0Ga9GhnlOxxTcQrvwOuT4Tdlilmzyty9x_LfmTTllIRYr33RKIm_scrjsKuBVniw0kxxMRnAstiXOzJM71g1cn8pZsT-q1IiSFEZM1rrdy0al9W1GnDSvbXXRqklc2PMIHIvrhnVfoBXQK0rjQfT3fpWUNG9dPnmnbRZxTlIf8H7PAOBYfugJ37rlmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Er7AMVAdKc86X9hS5vku1nTaf0sYMQDZl6JsStZ5AO9X50siExnQUo3ejEAkeSxrUNcHLt2SBEZejN4ApAuHP8__DGb7mWzvZEgCtLvhVrvdbxnbdq1GRnhMaP5rpo7hLUBDi8kL2NYdyFDwj_0srTdf0fJkaUo2DVJrqHnqOt1m_d37Cex2qv7N2u6v8ftU2IeRtdnJQoyGbwCLNcRpqfCutBNG3cu5YmyOU1yHzujqq3WnERn-VwSa27xiM_8Ccz0y60GJDIsMmEBD86qtkJOZh4lPoMWOnYpDz219vavBg0cXTbH0-hsYqWy-0Onk1lZIvz6Ew5Zx7W_U61VDBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=ftp-_1CO4fTLs9UMf3zZ3dQ8h_oBzPiq6MnH1R6bPBxGUqg1spjdP2BbQQ4yMpTZBQmkUkYJF3xfZtSl1JFIkTjOW5iugkt8amGueUDXufR0gdNCMqF5M5QXnE4IXIaqnWu5epzmrms6fsDD_TqGqhS02x_fSaq4VmhuqnRC4uBp39eJDSGGBCBx1tZO_MhPfEbVNb2PpKk5JW0TxVOugola4Z7TmhgUfJWBpzlqkb7MX7VbuNNtgZSb_6h-jfIEsIGZzu9w6bChUy4C8z6g_QsqS67ky2xzTYCLGhwvUdymBgk4icYCgzO2jfc-lBka4G3BLZxRm6fzbdvJuCfseQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=ftp-_1CO4fTLs9UMf3zZ3dQ8h_oBzPiq6MnH1R6bPBxGUqg1spjdP2BbQQ4yMpTZBQmkUkYJF3xfZtSl1JFIkTjOW5iugkt8amGueUDXufR0gdNCMqF5M5QXnE4IXIaqnWu5epzmrms6fsDD_TqGqhS02x_fSaq4VmhuqnRC4uBp39eJDSGGBCBx1tZO_MhPfEbVNb2PpKk5JW0TxVOugola4Z7TmhgUfJWBpzlqkb7MX7VbuNNtgZSb_6h-jfIEsIGZzu9w6bChUy4C8z6g_QsqS67ky2xzTYCLGhwvUdymBgk4icYCgzO2jfc-lBka4G3BLZxRm6fzbdvJuCfseQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6VnJWFp9IUnjJ--GfN5RZYkDVeojYa5lvfw7GnaJIu_uGg3zRe73D5XA1_py4us4pN4ApFDqLSRzx7sXDLFSTpWZ4kB8uiutDYJYF1gjXcFyOKs0KEZzInV2wVLm6O6uEF9Ci9OKzKZXsUOyvoAa643oMkFjr5b3YQnl8hf-Do-SzkvDfbHmIuTVhgMvGMwH1LJ80mhBvdCZ4sFVwxWVpRMjJ0Hsk91L1siLaczn11448GzY-LmfiL5DrpA_9Rf1ojqsidC1zweHsi-TxqcgoUV94ZUsrMTCQ76xIMJoJ-mgiDLmAtX9FUNDX9F_x3yr7xR9_Wc7r-5LGHWtroXuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxdXVS6FujNGqzbIg22eSi1BAw-Bw3Td4RAqRoYu_8U_OTymiZJ14Z1EKQWf9zQSQ2yCJ3-4MdvsWZuhU4lCHEyG1RnmpJyyH_fuLPCaZCvRI3I0Kk_-9ySOFULbLROu_iKQpfBblgLXkn5Z5yL3fxO0AhnvN0zQc2MZLG_8UnYukYIS7QsgxIraYj9fjJiJAAsk3sxL-EFmN-tnHg_1dWsZ5N3VVBRNEyEXqjWYQwNU4MpanRw85Tf1XhpdnQucGZZQ4gDwXWLnDbR2_rXAzAZtl9OT11Sm6ikdHFcsuQsw1Mk-fuku6Y5tyBJx__EVO5Fn1ethYRH2jr_wZ4XQ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oy28GqOjAFrJN-38MDcl_Ad9yvIzr9MouHyPzZXEXaWRU1LLc2kfZpsEW8_7eAi630kgh34SvyXcmpwqzOrdjNyzwgdDz5h9r7Tn6ORITOTjlN120d6Z_LU-r0N8la01sKvmKKa-5FEfsYk2oLcFukhybpF3rfXVuXKjP4MnLv8lxNHGaWqvNGUHnTpEspqibRPf5VlFNVVInvqTNZckGjPxbGH7er0t9MUn_TdE3a2McfwJg_s-9VBF6xtNg939XAI7VD6gQ7rF5js9gTncer6B6p53cj-IQRZ4QjavGPdJ16CE5BJSPJXyNH7-tktE_XkeaOVdurqGYkkn2b35mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5mdJpsrrVIawTAsyleiJf7mHvyrVilRtuSr54kISMHls-4EBHiRiVWUnq_5gicmDTWB4RjHzVQvsV3NdZeaQfOz4EX7s2XZ8XMKv2w8l2zP3rsyaOa4Ec-b7ykFndxtQbE1xglgEhn26pHf1k3RxnBanD6ubC705QOeM39LOR1RD0_43iM11kJdDguCoY-14NSWYDgERWZj3eFGYEn5OH0c6Jpo8M1wubUshz_5qwDZYr9W7Vmj5-Svzwux350RrPpCBcOdDN-7R9MCu7f4brqfq6FK6VXtaGZpHI-oV3ZpZMo39OejyY01i9KbrnO0ZCPTU-twer7DsQz-yccUmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM4Ic5h-0CuEVcwg6eacmyDRdCFkuueV1dH-bCTQRzYrGUlojeqPTiUmqpJZFARqwc_OFjTMxhe7wsi8wzC_2RFISsXa3mcbT3YU5fxPvGtpfwArHa_MXzRgEna5jfwMebVb7IE-Gl1LtzeICFO69AxMuOMQxUgoovT3dDRJd6VTk1s0xwqLvR5Oge_m8EltvTGBWYn2OXPkI8W25_9AOrHACVLF-1lpOrxT3pUZEutYOQKvwNUopp1GzKYT2f3JFZtyuhaD4cWRZUwU_Cue3YSX_AkRJJS_ITxdM91lQw5oSaOrJfqnW4L2VLLAM15N7IOnLSS09iRuOwQZ_0NIEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=hWqRqJmcyMKOxSBLNBGdopomXGmUVOSFJ3uH_WSRWtBGrLJedntwOmTnfhZIPikblPygBHun2lN9EcU1_HXDEgt8iwFwMb7my5rw34lJWGeNxnX9JUJ5dYCVRGXGaAqomZrCMDVbw_0LQQk6AhLrAzhyFnqRS2dK8KxRJPq1GN0kCj3xDlxTeJta6nvFTM9G7rmbgXGU_fN735M0ERaqmZkmnhQvYUMTfhPXaUHF8c5LJAyl_MKC6eqq_ieYQi2rwjyzmscZBJpuBF4XoRsMm21Hy62MMICqZNszb8ycF6uKz72pj7iks3OhExIry0nvUaQfCx6VlhMjyV1M9zA-iiI0Ln17NYFL25DQw18nTzqwRg95xTtpeGBRVelA1QNwyi8l2yXd9Czv3wh3UD9pfHnm-SbyyccsixaD_qWyf7NRkLQ-eV88hzNHu2kh8BchVpBrrD_m8cy85Lvj1afPhnbcrb97STgJBsmVeZj8tuglQOo63dSGQcl5gpA0cRu2AFA0dEFjAmCXRvGGkqT8yeJGkFvKQ4Fx5QoPQAuJ9WC6glR2TeD-VrqIFKhrKlFkeXBXuMWCx0cKnbk3zMyHrvpFdbJAqylVB5QP1R30WL_wbdE4MqiGIKZI4HvaWBMraPxeEhzJ4LnhQvifkBLQ598o3I9vCVtperl6KGS3yoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=hWqRqJmcyMKOxSBLNBGdopomXGmUVOSFJ3uH_WSRWtBGrLJedntwOmTnfhZIPikblPygBHun2lN9EcU1_HXDEgt8iwFwMb7my5rw34lJWGeNxnX9JUJ5dYCVRGXGaAqomZrCMDVbw_0LQQk6AhLrAzhyFnqRS2dK8KxRJPq1GN0kCj3xDlxTeJta6nvFTM9G7rmbgXGU_fN735M0ERaqmZkmnhQvYUMTfhPXaUHF8c5LJAyl_MKC6eqq_ieYQi2rwjyzmscZBJpuBF4XoRsMm21Hy62MMICqZNszb8ycF6uKz72pj7iks3OhExIry0nvUaQfCx6VlhMjyV1M9zA-iiI0Ln17NYFL25DQw18nTzqwRg95xTtpeGBRVelA1QNwyi8l2yXd9Czv3wh3UD9pfHnm-SbyyccsixaD_qWyf7NRkLQ-eV88hzNHu2kh8BchVpBrrD_m8cy85Lvj1afPhnbcrb97STgJBsmVeZj8tuglQOo63dSGQcl5gpA0cRu2AFA0dEFjAmCXRvGGkqT8yeJGkFvKQ4Fx5QoPQAuJ9WC6glR2TeD-VrqIFKhrKlFkeXBXuMWCx0cKnbk3zMyHrvpFdbJAqylVB5QP1R30WL_wbdE4MqiGIKZI4HvaWBMraPxeEhzJ4LnhQvifkBLQ598o3I9vCVtperl6KGS3yoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=KUdT6fddUfYsaqAYaPuu__bsO_7nl7yxqBvd-wYEKDupc7GODml-17zM6m4mK_TlxHgEyXOXX3H5bhDiBW8Sh_SVWwu-m1kQxICXjxGbZpK0BNNF012Mg4p9VOOUPWCbOFFcpzxot_8daQCbZ7WXYubm-DdIGjiow2FDQWSJCqI3OVd6e8f2LbCMFQkOs6qpsnYNC9I57ZMHFO_nTmXbhcxK27hRkkTyXSG3IqfwuCPi2I2b44NjnwKLHnTfdTvodeeCIjkQPhUtXH_pk5jE5Tzebh-IYvJj3tOuGaQnCg7ljHWgn5LutYwg8GIOwSQ1mAqcUefT7ewRtZmYg3Ag2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=KUdT6fddUfYsaqAYaPuu__bsO_7nl7yxqBvd-wYEKDupc7GODml-17zM6m4mK_TlxHgEyXOXX3H5bhDiBW8Sh_SVWwu-m1kQxICXjxGbZpK0BNNF012Mg4p9VOOUPWCbOFFcpzxot_8daQCbZ7WXYubm-DdIGjiow2FDQWSJCqI3OVd6e8f2LbCMFQkOs6qpsnYNC9I57ZMHFO_nTmXbhcxK27hRkkTyXSG3IqfwuCPi2I2b44NjnwKLHnTfdTvodeeCIjkQPhUtXH_pk5jE5Tzebh-IYvJj3tOuGaQnCg7ljHWgn5LutYwg8GIOwSQ1mAqcUefT7ewRtZmYg3Ag2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxA5I_VVN2Qm6Ma0PVzD9iWoEiymmkk21-WmY22CUwr7R8FAiIh7meBi88ad4PbQhqrMYSNzCGrIZ7GT1SL8U4__poCPsu0AKfNioR-jTIcy9W013k9FhdahnIqU9zekpFz-igmo7u4_0N8R254dnxffKzPr6fhBLhlW5FQMaXmxJQcQAX2mb8kMJ3sDGJXCRPFqR6HLSJWC6Jeag99bsAvz5BNpXcqSycIT84bKeilJZx3DQul2irCnc74gmFE5N5VK5o_Iu7Tn8nsScx-z9_glJM7JdnQxd8cbIVFp43OCbnsqt3-8M_sA1ryHmz0g1uvBuMA8TPAaAA7nyF9L2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=H0JCH0weluFAR3H6YSEXaYn6U3tYah1QOxDihF-MLx6pa0mQhMJKd__A0VSGQFBd7sLabhH2bN3N9WYXEHujZQg0OwO02SzzSOn8c8fzt151ZZSiGBhyFI7gOqiwCIEVozVw_vIGlUiWtD0hQXMy4xZ608LkpDnhXFEMQRzB9p5LzXToi4CpP7kG9zjLrO5ctIJVJhAEIiiVM58jXSswZveiaKOJs8IVLoCOpjFYZDry8Cr1qUMB1m2uV2tUBBUBBaTn5uvYtZQS7icOnrXk6SYMzdTKyAyqCU58ZtXgd1m7Yf7FeyOtx6IZD2A52KXMbB8jOHmjICEAO9VMeWtW5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=H0JCH0weluFAR3H6YSEXaYn6U3tYah1QOxDihF-MLx6pa0mQhMJKd__A0VSGQFBd7sLabhH2bN3N9WYXEHujZQg0OwO02SzzSOn8c8fzt151ZZSiGBhyFI7gOqiwCIEVozVw_vIGlUiWtD0hQXMy4xZ608LkpDnhXFEMQRzB9p5LzXToi4CpP7kG9zjLrO5ctIJVJhAEIiiVM58jXSswZveiaKOJs8IVLoCOpjFYZDry8Cr1qUMB1m2uV2tUBBUBBaTn5uvYtZQS7icOnrXk6SYMzdTKyAyqCU58ZtXgd1m7Yf7FeyOtx6IZD2A52KXMbB8jOHmjICEAO9VMeWtW5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=BlIahqL656E0HlJ9-KulgHcUo5h8xQ6jnaHkO-_ZHwe6Pt910zFcKluxVXN6kQ_pLLgy9FbfS-iafmv8jEfIwdHgs6NL7DER3vYSpL9RCPZhk399Nw9YrJPrLHnhl0map4xOB6FAr09YG0rKBKChUF0PuvHioyEbj2dCFLQGCsiJ84LNeFS0JUJQRUSKfqWkRWXXgEepUDIG-_emZpye0CdpXNxmTI7UrJOGOwvuTbRaO3vhNdfGYOkN14HynevFI-VWF8IMQDFn0SCSSRUO49yumuj6JWkpMrDeWA9Tz-Ux7FzGy84cR-59ebChUK0CgSbM3Xw-uWCH4xmzvgZ9Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=BlIahqL656E0HlJ9-KulgHcUo5h8xQ6jnaHkO-_ZHwe6Pt910zFcKluxVXN6kQ_pLLgy9FbfS-iafmv8jEfIwdHgs6NL7DER3vYSpL9RCPZhk399Nw9YrJPrLHnhl0map4xOB6FAr09YG0rKBKChUF0PuvHioyEbj2dCFLQGCsiJ84LNeFS0JUJQRUSKfqWkRWXXgEepUDIG-_emZpye0CdpXNxmTI7UrJOGOwvuTbRaO3vhNdfGYOkN14HynevFI-VWF8IMQDFn0SCSSRUO49yumuj6JWkpMrDeWA9Tz-Ux7FzGy84cR-59ebChUK0CgSbM3Xw-uWCH4xmzvgZ9Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ6G4qxWkqdh7K8Tjc1tMUPEO6mGZPEvtmQFu-OFHlxDjGHNJz41MsVW_xOz0mLuDido7xKd-UdHETdBttLilvOYsqDq5djHT97YI9W7K0ys89RUz6nF663P1viQ8iaRilVKhz8Xlgd57QkrOqImswUe5KcR1SveCT4cv2ingrZHjlAF8atJA1xUVqyJDECxOoKvVlKQeCl3-EiaLqrsSxPVE3h_XxsCRUNGCCaxTdhXjaaqF44mvkao_vRNzSb0Hp_Vsnf0KqkD4qIHPXppSnlcKs4559A5fZcPBw6XUd7XWZXcpKf2ufA4pLAUp9yxVti_ldSGYdsjjQVlgKxnVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtRcDAOwcCaHKboiiPHzj6_Agj-uaS-DSjg4y__DRAtkp7rWpoLTpfx4h0JBkLT-hTPW2Dhfg3NUfmGE0LAfNzBSuEC_E1ZNRkN82jEYPkE57oVK1We0jXMPzs-UCYtk2yftkv3IEHXoGzpHgUEOFVs4KPX_DwJUFtHH2llT1jaV7_zWNHvvTI0zlJZQp3gg3LHlQZKmngj6VrN_2nlN6Fym-rMII4fbTK4IyhPsRcwr0xyreK-8rsZEUoQNrBmHTF78JIp8ipUaJX7MPeW0LWH9YDofBHJ-Y7QR_f6ZAh5wb1nuVRUzvsPLUEr-jo7E6Sfe1oVtHI9uucMxbc3J8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUEJTRF5q2lTVZXtgyICPZxg6n8tFq3-noXim87_BpSgnieiXLWH5eokcelPI475FjMq6cbQ3etiW3LP4ncBvQNGlldQGY6xUbViqdRZ4EByUhcYfqgiBppshUgdSsZo5JkfIMCgN70PlIfVX9MwCyP-lRB4BYKlmb8Zv665cTxae0hsYOwBByszDlbW3kqDayombT_wXJ74JLNgZhZRsYbuPT4Q4BxuMuE6HAZGYTg0mGGBos7fYv76JLmCI61sZA5MqnmzNyS9eicq3nsEqMXXjEWVdDPHfUWK8-gSRRlOKtYcaOTO4sn8qG-LTQaUZTQXSEKizccs-JfunMZ40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mtp-Kj1H7MMXRs7ZghXKtUedshIk0vn8Ja-8oeRpFXYOxf0-x9_E7zA3WLaM1g6-Ph9RVY05qudoPsyZ1eHC8qsOOWcFmwP-9TWr7-88jsYEkISwlQhzU3AhI7Jgn0RgMyQuYyg3caNJiGBiORQk3UMVvnuWwkoC9Sa6qMdODiDB6-iO1lHou8YglfwpPgLD6etwX7suffUA9QcT0voMItAO1reezcaxqGGb1FQzZZWaLSjYgwGdVy35hntCD8jgypqkEuzTnOqgtp5XhYSPP_CQiuEVtZXw_rQbIFOlei6DAYdHSxFDbVfU75EA8A92L8idpE9YV5Fb9Ca5PQTBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=PUHG25EO5s1r7bR2Jr98qNTHSzQk2vygUI5rK43jEhWr6VlmsirmivUtI1bSb0OYo0h-UuQh2Qzf-17BRFHPN4VuATD8HZEm5ckd-ceEIqrSzoZ9f2sIFbKuauwxf2ty_-yHagnKTITIZz__8QVNz0f49LSOKdrfgovnAW7imVUAN-pOxqV_aHseqbriyJuMthdkkSAvlRDIOYoeXOsYWjSagJ-QLWRjGgdJWIYQ67awd0JSkIcGAGWaXZUpssoYdHZBUwtOFmhlijdMsshL_hf7Hi5S2OGPqIlLRPvdmQQ1IXyC3b7Fqqqij0OC1evV47OMK55g1mUtEwBuFGEOmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=PUHG25EO5s1r7bR2Jr98qNTHSzQk2vygUI5rK43jEhWr6VlmsirmivUtI1bSb0OYo0h-UuQh2Qzf-17BRFHPN4VuATD8HZEm5ckd-ceEIqrSzoZ9f2sIFbKuauwxf2ty_-yHagnKTITIZz__8QVNz0f49LSOKdrfgovnAW7imVUAN-pOxqV_aHseqbriyJuMthdkkSAvlRDIOYoeXOsYWjSagJ-QLWRjGgdJWIYQ67awd0JSkIcGAGWaXZUpssoYdHZBUwtOFmhlijdMsshL_hf7Hi5S2OGPqIlLRPvdmQQ1IXyC3b7Fqqqij0OC1evV47OMK55g1mUtEwBuFGEOmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap7PhORQb2sfoK4B2ejbVfDxGknWcLglSUuvlhOyZ5ZtGLItpCMhLTUgWCz4NnExj6Q5d4hjUeoPlg9abvfJ78IkI-Ye4HvuYC68FBauu5PxKWGPH0lmdmBG77amUtZOcnrv0NqSjbRPkrDjMSAcLBPjIG-b82geJUsql-cx8m-l_SQIBS0oGTP0k9gqO4s2at-NyfFmtKrPpWqMtebVOGuDNt7IPuBD8KTcVZelFc3hht6-ywOMD_zL5ghmfsD7SZF2J17eCmw1x0SxxNC8bt6JpDbthCOYJsb2P98fGreMb6x-P3Ms5cHcqwTlJoymnlKAdTMd_NhsBgUdXoaYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmW8Trnf7Emuxdej6DB-pBqEuI1FjBvQ4YGuPu0SWjjbFJ6-9897FWqo6g8x-zq4RwGnLjXfJbCG9AWJSE0po1fA6S89ba6En8a1od6s7rQxpVOMnYTePnShX8xo8j87H22524-qTpFA_c7du2qwVKvpluQxnmUK9PignoQu-G1h3MbtFGLHLy92jEw0TXvL3vgoMm_nKpzIf2skv9djiJrdHvbiq7IVCMZI7GtgdId84IgU2J9cgJpA-NnNWbo5_0jWY8TbXma_Ie5JiC2_E6Gz1ru8NM2VT0YMYzk3-5s9EhNempz6VtSthu4yMjWvRP-dpCz40hv9jIlDTx13YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=fRF3uhZQiZBHs6oROQp9_vj3xv6uGFYuKmbKeQQW0UPkl8P4BvnRVr4j4Oabj5TZxuK4IzJ4gnUFCIrn5YaOmd50VqOdRpgTfdiJ8nODOz63T3J3esv9iLbow4QNkn2JowroxXBo6vkWl2lNg_VsOxmYazLMaWk0XkMcq7pKmpyOduUIplIeI35WRyVw1u-9673pXsJZ5pZPygKSEU0UUDKjSX6tmUz69JeM_9rS21RhoYuhj47kjXM-8BlYD9cecRqb_aqRxRF_dnWmGDe50OqbyPi3mirUehNcgdvNsy53TSW122kvTgeeNQWXoQI_d4lzJvozNkrOPfw74xL8Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=fRF3uhZQiZBHs6oROQp9_vj3xv6uGFYuKmbKeQQW0UPkl8P4BvnRVr4j4Oabj5TZxuK4IzJ4gnUFCIrn5YaOmd50VqOdRpgTfdiJ8nODOz63T3J3esv9iLbow4QNkn2JowroxXBo6vkWl2lNg_VsOxmYazLMaWk0XkMcq7pKmpyOduUIplIeI35WRyVw1u-9673pXsJZ5pZPygKSEU0UUDKjSX6tmUz69JeM_9rS21RhoYuhj47kjXM-8BlYD9cecRqb_aqRxRF_dnWmGDe50OqbyPi3mirUehNcgdvNsy53TSW122kvTgeeNQWXoQI_d4lzJvozNkrOPfw74xL8Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMw12qonq2BG4-vMw4ojZFkw3a8m19JALop6nG_TmtGx1qWXadH-Q-9cmcin01zgI9VUcWeRp5CgzweqHOiGajs3DOUEsHrJNjJHkdHBvpxtspAsG-UOP74OM1uExZOyQPr8aZYctoAxR0NpFc2n_7cO9Cdyo4wlnurXOSPMUIU75NwxoBku5OhNaWSYejpmcMU9HwYscYpd3LdA3O-21dhDOXsLOoGT4wOhO2nZlf7eDmWAsC9hbMqALv-hTyL-aVHhUlxzpBn1yhbkFzquLifwpMKyPHrCfElZu5lBvjgHOF-CSp9ywjBZ02oVM6H2-vQQyQZM6y7XpyUHmG8SMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOm2WpXILpE52iNoWJ7iw6bkfszF3YZL6wKlZvZ3bLesSbUQn7gVQ_knKUNvHO5LtHS_0KVgQUKcljw2qJ8Plvs1TrMYrJFkRmJjLvQjTBU9XTxZUKKjth5gmKYu4qdH6MuRbX9UVJb2d3NnRIKYLNpXJE0-JbuIaUea__XCSeW76PDEN2zsxysHNBY5_hKtqHzyE5MAFpGQ18wMP1eGB0VJtOxZQct6dPf44Uy_0uOclOVKX22NP-OLY56QV0QQo16nh-C0THDp0I185NM3drNc78eODrRziFBx-rQm-AfhBszHf0GMee0aRS9uYNvcAs_wOoS4k7eeT4F9qs_2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fwy6XibGGq5Fh0cOKcrSBOWne-PBlJyVP2ZxLTMUZzFee2hQb0DUcNTai5IfmA6tvAQ2RZOduC_hd9rgHtjGyD9icdo0upvV_CHe0s3t12d3gbQirzKyJMfC4uulieFmAOLEUrctpi4GXA0N5MOrgrd9oQwfWlxs553iJWbCy9qvpnjE2PFcnjW_M4yieJ1wWhTNUPV4kSQeb9NlTWaHx6f6VKOIDHdwGZoQSiqWHtERCXQ7FxleQsEoHYOwMXS8OKtJksOi4kov0P6m9JQPEhgyTAikFzLE0Gv_BJvflmWXGNM3ZEEI4j-wkRlWXURkDkghzzsSM8bDddqXQQY4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHyZEkZtTb8ETbhpzFx_VvHoW0KPjiCeopClU_J09a-ESgFujdDbqc_-BrYSgFML5z1t7lBwdeaai9qgLBtkwagdNFCBCxZHZIQ67-kWnGWks8Hc8ANr1SxfmTPFDYF_aHR9JmI4gI3QcFowVLVmGglukTGsCDgVCG9chw4ThYv_z8sPmC5f0RNvfleRVKuSGfJggqZJtRmo45-YQUXyW0cj4tS3Pus9Yonxhkfj-lEOuWPv0RkgSL-WRX1uC__dux0pneeQdSkT61WnRr3cHQi2FtYz3l1hPVKrNOB7L7c2HThY5jWhO9AyaiHohs3rMukaj_svs2O09in3ABhCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=G8xu6GaMthBBkPW3MZ6SUTuqrmtl_ifA_5OvUlTFLLZ0L8xqG_zlhi7EAQe_bLAFNfn4HmlyhqzkLmHevKwx6SXbphgsW4BVYQqKD4NqUsEIv-Yt14pHF_1ju7ykLqJ7T7GiAKasj6An-O53idxwB8J9pwixeAcnZxytH3VT32Q4I9eFThVQWaVbnZWFB9-Aoc4I30YmzoRICxLp6dZGNXsSjQss0ZUtIxpES_3iCKzGmP_rOlHzW8VXWNCxgzlmMbyUMk8DS0zkrWnQeu1tlorXuSxJpPQcFBpoWNhLotgzV0RYKAeIgO6AadLpGEI_iR9dgm66hkWVisb9jEBiTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=G8xu6GaMthBBkPW3MZ6SUTuqrmtl_ifA_5OvUlTFLLZ0L8xqG_zlhi7EAQe_bLAFNfn4HmlyhqzkLmHevKwx6SXbphgsW4BVYQqKD4NqUsEIv-Yt14pHF_1ju7ykLqJ7T7GiAKasj6An-O53idxwB8J9pwixeAcnZxytH3VT32Q4I9eFThVQWaVbnZWFB9-Aoc4I30YmzoRICxLp6dZGNXsSjQss0ZUtIxpES_3iCKzGmP_rOlHzW8VXWNCxgzlmMbyUMk8DS0zkrWnQeu1tlorXuSxJpPQcFBpoWNhLotgzV0RYKAeIgO6AadLpGEI_iR9dgm66hkWVisb9jEBiTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=uUk4TjZ_T0ATYKMiDvOn8Xd6eSwPO5DVTihWd4fO29BvLk-Y0qSOwirGMauTKBCe1LJiEWrxgW6X8Ehw99nfqBJ8Z9GIz2CwQmSSVcTlrrbLYbBzkoZoieqJHkFAsynDF3uyMtCLoQlhIPwLb-OCoq7vDSCTOyNO-wHFqWjVCVaI4YgUiEGz7T8JAHROkHdoF3sDJl2BuSn_2k_GBr4W7cW8UEleLnoTeH5oK-fYLdRPJ9SeeGbYIOw86ViIpfExIlomIjKuote0CrirUdsXD-laHA7Sb-CPjCR9Ae5uPizTzbhZPsK0DmlhMn_Rcq5dfK-YyfNSC5MiayckQEJm3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=uUk4TjZ_T0ATYKMiDvOn8Xd6eSwPO5DVTihWd4fO29BvLk-Y0qSOwirGMauTKBCe1LJiEWrxgW6X8Ehw99nfqBJ8Z9GIz2CwQmSSVcTlrrbLYbBzkoZoieqJHkFAsynDF3uyMtCLoQlhIPwLb-OCoq7vDSCTOyNO-wHFqWjVCVaI4YgUiEGz7T8JAHROkHdoF3sDJl2BuSn_2k_GBr4W7cW8UEleLnoTeH5oK-fYLdRPJ9SeeGbYIOw86ViIpfExIlomIjKuote0CrirUdsXD-laHA7Sb-CPjCR9Ae5uPizTzbhZPsK0DmlhMn_Rcq5dfK-YyfNSC5MiayckQEJm3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVXPpfW1-yxrz1Y1rPRZE6TBAmUQVcjHUqMxFWZRHG-o4FTZGJ4UmxZ8h_Dc85gMO3EkS55qhe99HZnEKQyxufS-dmXUrzC96Vma_VvB1YQRevYwcDi6m6TQqkTCugcJdu7buI1jup7TJAd2-gFbKucwRQUW8oEgzOqPy_d1G_KszCaxolXyAGjTLYSF3jV0LX3B2ZI-YtmmJPCzFSAirZWIKJksRtRUkiA37DB34PJhpG4DSVry2ynRlR0zF8bm_7Uphkk5yXla5diSJ9bK9kGcR6NGoaaQmphOPsAhVmxrB9gB-z9lyDopbUYQOBLZx0dsRZ-KgXIHEZgpd53kOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=a8mzIHdBUzgSkEId85GFnqbxBsI2jQmEhqppgdlEFGCG-94Gd4NaI4MYxXkvYmjS01jrBU6UAKO1ymicsf0NIUo0ajPZI6SOui1AZ3rFL9UTqeHKBKfPox_AGRFr7x7FSSvmjRHFu5WS0yT_xiDXUZV99ZPF_Va3_wZMGkwGJJbnaG7PnsYjOZ9lcpelqiy1vMZaIbeUIb1zYdVAFSfTZ-hJ_u6CeljixKAKmsdBRrJ_9Qjk1L8mInm74scsPq-k-5RELD5GtQ3OitLCS0QhjvCLg_fIY980yRsY9kv2_NvFpOOn-mK3wmQ4GjRa7C_bcaWXrbfEFuT6PDqABn_ncw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=a8mzIHdBUzgSkEId85GFnqbxBsI2jQmEhqppgdlEFGCG-94Gd4NaI4MYxXkvYmjS01jrBU6UAKO1ymicsf0NIUo0ajPZI6SOui1AZ3rFL9UTqeHKBKfPox_AGRFr7x7FSSvmjRHFu5WS0yT_xiDXUZV99ZPF_Va3_wZMGkwGJJbnaG7PnsYjOZ9lcpelqiy1vMZaIbeUIb1zYdVAFSfTZ-hJ_u6CeljixKAKmsdBRrJ_9Qjk1L8mInm74scsPq-k-5RELD5GtQ3OitLCS0QhjvCLg_fIY980yRsY9kv2_NvFpOOn-mK3wmQ4GjRa7C_bcaWXrbfEFuT6PDqABn_ncw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=n-e-oUsQDs9lvF4umuXQ2XIuNpl7MhqlSncaaNVA4duj2_OQo8MvnJW4T1Svu5cUoXA3lQrEghhsPlizFniVeTgR9SYxeNzaXCC5B8XWxXis8zf4u7yO0syWwDArnrlW9SPkWdXuAOyUvunYhRvGX19LkOFoMnseYRVcsDpwbc8IDhmIA-SjuWNVIAuQvD8yQ3ZR47tJEvrnSKCGQwalzE6tcRnz2F7wHTbqs8mp3EGQe1Q3BEskXDTSuZS1pXEFksnEeD6YzWlhOE-RM1U-4UdvpmOmomurPA4C7UuejVU7S3Dczv4FDTbjRl8Cs72cNX09wIOiiFJsGoEIsqXucQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=n-e-oUsQDs9lvF4umuXQ2XIuNpl7MhqlSncaaNVA4duj2_OQo8MvnJW4T1Svu5cUoXA3lQrEghhsPlizFniVeTgR9SYxeNzaXCC5B8XWxXis8zf4u7yO0syWwDArnrlW9SPkWdXuAOyUvunYhRvGX19LkOFoMnseYRVcsDpwbc8IDhmIA-SjuWNVIAuQvD8yQ3ZR47tJEvrnSKCGQwalzE6tcRnz2F7wHTbqs8mp3EGQe1Q3BEskXDTSuZS1pXEFksnEeD6YzWlhOE-RM1U-4UdvpmOmomurPA4C7UuejVU7S3Dczv4FDTbjRl8Cs72cNX09wIOiiFJsGoEIsqXucQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvzYNTYz-yQV5DhQXYevVez5eLNxSYPydvzVrmU7nHPean7QaH02BF17foN86EDj0XjJfIIJsFX-WiiumRHo8M28ECmC9EnkFvBUSo2AS7oVoQ-NNlxjkWKfwbWp1DGdJZ_N3HwoYAyIksJ1UYXtUBvajDUsb8gicpzguDhy1xFs1VhrOkPiOdtIkeZyPP31cA0a7Xz7H3tMVw1JLXVTyUQ3kOtAED_dvIc7yTF_IwOzGIvQzewad07WkgqcJuBH2Euf0texzY60OjKW-JuOsylxjJBF2Dp_ADDdS7gQyxFeNPWogsjQm-VHadQZupU2H85lFCvzLPyYC5W9-ADjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2a53E7lwHBhQZI5DKRMY_qgcFUZsZgOMJ5meOorz2wwyQgxmbnJLfkak2PFBetrStp1zSOpxfMHJb6rM4U3AKUf0aEEhLMSR0_TYKh37On3MUrhr5A7JxvVbYj0E_9CQj2WJ2mhZODNr9ThP7Wp9Uo28LmAzB5fDwmiwhjV-yzxodrLN11IFs38WEnPBTnlPY6C2FgK73HcQ8DU06-j222I2kKdpa7U5YSufBC28ZQDyKLmTK_eGWwFrxxjANb86v27gEgwbxeITSgzL7T5I724O8DcC3NxbgEdsdyoDxbP39BTxQ2FoWvtv0POfT-BwL8ZGwYQIsLwnyXqGf0dWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLkFV9p8y92QpmIUFBsYWysudLyemp1nEZruv5_BIWZT6rqyMQPPC-Ut7x5ZbBVHINDQo_tCajVLrkc-ulTdVrGggELCGR2eR_ka8NnixJgtDeOaI2HBGpAKNh0IT6dLj_vSzfGEAAK1GNRXYHoTHv80ppfD2T7WYEIPtE8m_zh_WlgAK3iZU2If4ulPqSGkbMUBVoQAbvMzAvPZU-0E3p9iReEjTDLN4MstSRJTBzf9rq2xr2i9VLlKs_dzHZj3tj4aKxqNzS3xphHwj5vYpZX69h6wuY16jxcCLZcYYDYmKhemCX1NN-4wgOR3xPnpLSLA4LnI4FXltwBB3Vk9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانردهم نهایی جام جهانی؛ خروس ها با درخشش کیلیان امباپه قاطعانه راهی مرحله بعدی شدند. گل‌های این دیدار دیدنی رو مشاهده کنید.
🇸🇪
سوئد
0️⃣
-
3️⃣
فرانسه
🇫🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPxZZQEkuRyUd98ytVm4SAOdBQpvWMbtuyOD2zbgoDEAcNHTIXP5q4RO8X2_YDNYjkBgekLluZDWoi2pADmY-VwYpibSHCYmdDckR16s1yPfAYHPKkyU2FN3OVz2T45mFwK6tVzgERPSCG30TX-cB_I-4Sm2NnSF0Jaj0dEGSb0fnImD4O1H5gIfTlpASTyIrrx496gZjiDdo4cHorfrjP0FiGbNMdwVqwoDS_LRsqP2g31RiWAFsv8ikIlzeSQIfLWUGy-FnwlZprs5fn1nF77K2uKzn9KHWjj_NPQPmMivOD0TRaY9s5Z8BNsBTgiz_wmQ5vp9omxULkisu5z_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=Y78TZTyHJzU2J31-GI4uuFl18vxqkEztM8rZhtKkJ2XNJkR8HJVj6S_zvjcExUnq9eAtwWOWCrmov-jIfmgKgu2MuTKtbd5ydg_zpfTSZU1Q4hunXAVWVy3xKrWUies7R8nbJaenraGrWH9P10KdWsFoi855Qpj7ylXhG4fmsNnXdweYyCxt1QtCcPw3QKzmLlYB77nbpzeLfFFbHMQ5mkb0LBhQXcQeQkjFnOQME011h5-s8F-oGeszVDshfmVeFfFcbDl7WG3JSJx-Po1i3o9LM8OLHUz6PeeT5wHFhq_nmqlKeWyoq_BqqR3q0eFpYzEAKjmS5hD2CA5Li9Iwmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=Y78TZTyHJzU2J31-GI4uuFl18vxqkEztM8rZhtKkJ2XNJkR8HJVj6S_zvjcExUnq9eAtwWOWCrmov-jIfmgKgu2MuTKtbd5ydg_zpfTSZU1Q4hunXAVWVy3xKrWUies7R8nbJaenraGrWH9P10KdWsFoi855Qpj7ylXhG4fmsNnXdweYyCxt1QtCcPw3QKzmLlYB77nbpzeLfFFbHMQ5mkb0LBhQXcQeQkjFnOQME011h5-s8F-oGeszVDshfmVeFfFcbDl7WG3JSJx-Po1i3o9LM8OLHUz6PeeT5wHFhq_nmqlKeWyoq_BqqR3q0eFpYzEAKjmS5hD2CA5Li9Iwmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWQAaPz6P9s59OB9-lgkCdHEmgjXQYM4wqRnkIIo20jAKjz3A-KK6jqSBNsMg2_U7QW_9U7sRYGZTDRO0ksboUXuQL00dGnfT6w1FH7hhopCqQv9kjRjAQkA-StKu-JXrJy-AFllp18LIhvFEx82JZ_O4PCtnbcV7g-0nZCHM3v7wLLcFCCD0zhV78U2LnEKROzPyjjxLneMKBGW2Iu38H7_Z8l0BuNTXVUnwXUidSIGVAwFoUlUYIuyJEwVVsYYEnT8x_X8PAISZEWf3eD60ZWU4zNDWVEBC63LJeoFXy3SkvWtwPkO1jEq7lAF2AP_3vC8YUxpmURfX6tUYbFQpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=ofkW2QYNn6Vrl7V8sEwBG7tsQxcK4VQ5kpNJKQLqNlkp0ot1fEaqGYY2_w3lpnPx60egsWIQf57wcNYnc20RFbQzVOWmGPMIRmqGRdIIiq1HNIChBAgkBdYYdBYlH6r8iMzw8Z5nQ-sYYoB1oMhyTS6B4leP1QkI1Y4dc7CbsUG0q0Gi8XdnBJ3XlZmXPxQ2YwEI1TQ1esoRzRatirMKZw_37dvsXvxPnFAZ6qGNb3CMUMlbkf-TGooozZ5pT0xig6H1LswLhyCneB9L6UMw_EYJTMtAcL-sgWu_ZCFgi_tKhr2ZO6ayQEJYcy8c3IJHCcRGyHp77gLikjpK2h33_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=ofkW2QYNn6Vrl7V8sEwBG7tsQxcK4VQ5kpNJKQLqNlkp0ot1fEaqGYY2_w3lpnPx60egsWIQf57wcNYnc20RFbQzVOWmGPMIRmqGRdIIiq1HNIChBAgkBdYYdBYlH6r8iMzw8Z5nQ-sYYoB1oMhyTS6B4leP1QkI1Y4dc7CbsUG0q0Gi8XdnBJ3XlZmXPxQ2YwEI1TQ1esoRzRatirMKZw_37dvsXvxPnFAZ6qGNb3CMUMlbkf-TGooozZ5pT0xig6H1LswLhyCneB9L6UMw_EYJTMtAcL-sgWu_ZCFgi_tKhr2ZO6ayQEJYcy8c3IJHCcRGyHp77gLikjpK2h33_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSaLYvX0EioyQmN5c_JIoJ5zN8Hqy6etNQIkDmZnYuOB1vDHJTRfaAzDk4yd3_h53UmvS4cPTHboKC6IBwQXh2KS_bUS5nQEZCyh74robDLNUziCfjZeh3Zw73QBxG4O-Yrqj6KJT-dLWigJbveO5YLTUKLT7P20XFxJTuC6m7qqADS_5HdsxKxNC7JE3NBw3-hxC0wBJdxMXQ4roUJWraWEviMHFL_oJHISkS9xV_LpsQY3CD1z3OAug_I5S3--u-46tzBZaeOx0MVwzl4bxSzPy0lIPBNnLS9x_P9fTvdAkk0u6XwpRNS3zwy8sRu53V8jvu1ZJarea00PCvhdFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsPlP0Vib-K5EzrRVOUFlwf_gSJ1Ah9RUmJxJcncoCtJtLafg5pDQ7JWnyWulNz5Ium71kX0cPwX5U0Ktf2CPO8dF2m-NVOCpv6mtLgYZByVCWD_b_-9CbtzxeL6ZcvFV8Fqifi68hh4GX36pgirmqvsCNlUADA0P56voPA30g6k8kzX07OCrFjdU1qG13UacJDcSTYSsiZgrHUyWYqFVLztgQ7S-yttXNY2p74iUbZ7Azdpsnci6suR07_kkC-Lc5Xm6j2t-c5mUrBYLarlZuubh5bD8yppZKZT-4t6_ep6hPPUYE3U6A-h3zcoMb3KHpki68ouqBwc6KwL3GJrog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO5Bb3CYUa5c3S1Mdb2LVyMQUbR1HjehW87h-tW-NwXT7uMq0hU6LDjKzZxTqwKb8VN3gP78V8xlXgQpcV4OWt9Noq7sp3KpckpTB3mbW4IjH3Jj-1avdINjZiut8-V3pBkMPJ-AFW5jp7-_bWogDUyyRXMMaltONxD2p5_PZA-0WQdt-Zu0ZiYVxuInUATATk2kaHNT2tIju6Ae00rxSZ1BZFbhElqq3U9hAZRcA9fQkIsIoje4jFvpT1RyzbcQg8kA-gME1VtT2Ma8M9Qhtj1dUVZ72hZPvQfyZJpsCZfRiZ0h7LQw1h2UsNorJ1ak891qDRhqdTxBD0Nr6qxU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEAn_KPQXN6_ET1dYV_WwSwIP7EFnoIRDZnqE5HMP_70KEHe8peRryTQscOvB0aS-Kxjsc7P74iOttW4wU7K6FIlSno3r2ArP2QGAbgPpbLogop9_sMmSk4dPkqKcV2aCveVWGF0qa0tLK7Zm_0GeNT18imjkabDJbKk74vWfGjOwSJcWt9HWDx2nmlYnAbMptFs3LUp5UF2KRpiH4zaPs3Em467yUs6oHDswx3sCzcQEE8UPYmgCp1lp4EIIQjhshAioWfUg1tmCQ_ojZ7eA0b0FAFlakrPuq6YHgpzaSiLsD5Vk4_MODkNnT3e7fFVQZ6KcG7e_tEJTMrpnX69Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6xzNnpXvu38dg6RXqomShUFD_z8QiHOmMPtRZjlFlrHszJKjquZVnIU0ApyxEfRAdTKXDEh5uovjv7fe21P_UoTr7U1Rs9MdTpBVnvuPbQI5V-y-2lgrLNvbjFXZrTNkpQyd2AGtyDhIu_jWwRob4aXGCDbLJK141ys5REeKHWgv-Aqn76uFR7HDxJZBUu-Nx7Wyi_Dn1Fhe7lcMR0Tg0vlgqme_NYFc_E6pXyc2mSOya7oOdzBbpSzJE1qi_HmuF15RotQ0vf8TAN9wF1RLk543o1Y_GYE5yg7mKhzoVEokwDSt2wOT7JELEYHVOkXKisUEctyIdmnO0R5LS8RiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T67_GfWKnINMGg1EdaKbtAeKE1SUalGgKb21H1FZ74xuiIjrOgN_JE9Qekyid-evWF8U1Z9XhDjymwexC3taUZn-p0OfE3-YP9JhkQzn8GZFNe0aKDLqpv-NEAnAuTJle0d717sZMHe4kQRbojDSPLOqHeTEwbPkKiYJR0sZ0slSCnEL_oFjCXL3aXaDIZ93HtSB_VL0WejkwHSbbp9PJIVCdTxVjuIl8OodF8Wi9a1hMfRRNq_x4BeuL7VWfS11--n8yeNh8ctQDcTjSmFNycNWQV2dT-aHDz-CIwk_ASOJsVbguI4aNxDsTDw63vvjcuLPzWCeiFqmK1R3WzlRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
