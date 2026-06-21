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
<img src="https://cdn4.telesco.pe/file/O1ufRcbpQuYmcEa_PWk8cWFAOxOdfa-dHNLw0QOpTEz4L00tD9Sy-ssiK_KdfWVQ5PzVQH8AUO8nM-umZ5h1Qdgrukb9a2Tb5gJnGMtZftCqRhnDQ4g8b1MeUJwI7OGuHnk4bM7dRPgcjZCxIQjo1PIQFuLj9fJxs7cYRFGzR_3iMW3Ng3oea7bPVYI24lzsKEeEJSNoUj5JZ3Lb4oHDMtJIr2ijSNp85Puu_nqL2lBQ3kUbSwHGK44UBDMH8SLiiku1oBFkXmnPNNiZq8zLeYZjF117xWQMiTmZ87YLTpG4FYjGj7ZjK3VpCfAsl0jTWtXt_-WJYeSJt2UlshduJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 313K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 14:21:26</div>
<hr>

<div class="tg-post" id="msg-23980">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUWVD0MIVFt0ZoLkLUEsS0K55xTg7TGBqCr4xF2LgoNAJx6prMfC0gKTXRvduJu7G4yGMk6CblZXWwbJflDX8K773ng_e3UFudivckK0J50D5VxpMSyU-YffGuXTsJYTIeqPZEvYsq_fhMi_iYJSl0NEk1wZ0yntbWWZmjizszbRwgQqfySTiyjwpzQotLmYbd9WrCKBo3Hs8O-nvh333msV9CZ49hmBnbz07OHkqw6gBU5eAZ8-3CJmDaNbw4U18T-qX5zgPmcPcoev0vonelMNNduWfGMEu_VqNm_mZzuLgmf2qpgya_pjdHwq7pZpXbRsktXYzfU68Z-uSJyqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ تاجرنیا امروز صبح در تماس با سهراب بختیاری زاده سرمربی جدید استقلال گفته درصورت موافقت او سریعا با گابریل پین قرارداد امضا خواهد کرد. بختیاری‌زاده علاقمند به مربیان ترکیه‌ای است و احتمال داره دستیار دومش هم اهل این کشور باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/persiana_Soccer/23980" target="_blank">📅 14:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23979">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nESqrOxQS1v58VqVpcF9gZIDGu5jGzHSjisDBvXHFGnQV8IjSpGzEEMuTIa6xbG3ghR_M5Ol1peNq4YzJX6W9qwdnqP9rGUT9ayxc9JhCtFQDbtXwo5eylvo3WCmJsW7_M54f_CD0J2bWzZBC8XPLWbcPQrn_Dsjc0B3ry56UOL2vSdZyvWr9zqBLejvtW4NLQoIo6ecR08oEKG_vVs1o3SS8ho8njttlAGsxbnfLVLkASYRXEimOTNTzm9y-Vnwk46p3I9qOX8uxBgd0RKgWd04KQuaplxLEN7FaDSMdLoPogWNOOGVG7AO3GNEcyNYiiWOrJCKJyfr94122A-4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ باتوجه‌به‌تعدادسوالات زیادی که درباره آخرین وضعیت نیمکت‌پرسپولیس پرسیدین لازمه در این باره به یه جمع بندی برسیم؛ امروز پرسپولیس با اسکوچیچ مذاکرات نهایی روانجام‌میده اگه به توافق کامل‌برسند بر سرجزئیات قرارداد امضا میشه اگه به توافق نرسند اوسمار…</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/persiana_Soccer/23979" target="_blank">📅 14:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23978">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9df1a6812.mp4?token=hubq86CscdPLOig7FcAjDTsiStumoBdY2TCxrUiD5HSnXnenoxGfsyuNGsksnJuqkyExeGISSSoPwXrEVGhdFqyjALY0r_jIJ_OpfMgBraWQTtIrMnhP6g2FSGGwzGd-LyWxdYL1GiuaYqT_zLVTjfyMxenRHMPHqM-1eFoxv10Tl_uOUIy8S_YRxM2uzLvI3pCZCQaH3tGDDXBIKzW7x4g71AnjJxbwcQ2G8SbCK78iy7eQQb11ibm7gKCg3gpYWWXJkdpMt5XsNNZofONv_SkLcjXNNTwK0OlC3gKBjfMVu0tv6M5wHzGNIvFqxNRAnkpNleDXTXM8cMrBvtmb8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9df1a6812.mp4?token=hubq86CscdPLOig7FcAjDTsiStumoBdY2TCxrUiD5HSnXnenoxGfsyuNGsksnJuqkyExeGISSSoPwXrEVGhdFqyjALY0r_jIJ_OpfMgBraWQTtIrMnhP6g2FSGGwzGd-LyWxdYL1GiuaYqT_zLVTjfyMxenRHMPHqM-1eFoxv10Tl_uOUIy8S_YRxM2uzLvI3pCZCQaH3tGDDXBIKzW7x4g71AnjJxbwcQ2G8SbCK78iy7eQQb11ibm7gKCg3gpYWWXJkdpMt5XsNNZofONv_SkLcjXNNTwK0OlC3gKBjfMVu0tv6M5wHzGNIvFqxNRAnkpNleDXTXM8cMrBvtmb8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
هاجیمه موریاسو سرمربی تیم ملی ژاپن با دیدن هری کین کاپیتان تیم ملی انگلیس فورا تبدیل به یکی از هواداراش میشه و باهاش سلفی میگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/23978" target="_blank">📅 13:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23977">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv7peAJ0HMOrWAZjVfKn9m_7EasSoZf3YbttEWgZhLSSNQRyf1R6gQ-e1QnsTQ5JRanvp0O2w4RFgC_CUdlF7ixe2OZuZWOROreBPfGkjlncCHAHNh-hae4st1Gfsa8wY-m7z_8UYL4dFQPqfqRASu71jPle1JChiLoUqDjXIPvVWYhUv8KH2ZiGDzuvHqr6QqJMQdNDfETdPBFwHmzXgkP8-9JGjASU26WWPTae9vogo-zMvBgNty4n1OiSlQDcirHbXn0GYGEzOzkbb_m1AvKxIfSVWfi0Fv2k-CJOWAYeuwS2MX4CjFZis2qqQVCDvZch3loexSIHNXyk3qEWEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه‌رسمی‌تیم‌ملی‌بلژیک: آقای قلعه نویی عزیز دعانویست‌رو از تیم بکش‌بیرون‌. ما اصلا با شما بازی نمیکنیم سه امتیاز بازی‌برای‌شما. تک تک بازیکنانمون رو به دلیل مصدومیت داریم از دست میدیم.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/23977" target="_blank">📅 13:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23976">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGr2AO-3puRbQ-APZ6wZ4wT29u6WZQ_E88a-c4oVkTswasnV920zWKZsrM_9us6XJLv0YZ_z6uK5vZowQRjjbgnKnEAnc2TqxT-nHf3FY1SkQk58dSm4WcTi9MIi0dnmV87BVusNV6peoWGJiVXzYBsOFxzFg42h9qfUt55kU5hplIOmLCILETmvjPlwn8ODB5s_PhVK_KZ3NeEZeRx3LNaxWO9mrEZLUCPLULf-fG9lrO3wKzMu3D0R9IeMwHo1NMMM5RYqq-KbvxWTkcRThdKgFesYN65aRXS3uzkcCTg5rHiPUtt3DKRFgER7woYZiDCME4kTXVWbt-8jzZ9RKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ مگه‌میشه؟! رسانه‌معتبر اسپورت بلژیک گفته لئاندرو ترسارد ازناحیه‌کتف‌احساس دردمیکنه و ممکنه دربازی‌امشب‌مقابل ایران فیکس به میدان نره. پزشکان بلژیک در تلاشن او رو به این بازی برسونند. تروسارد جانشین جرمی دوکو مصدوم شده بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/23976" target="_blank">📅 13:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23975">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tizu5hK7fOUkzjLexAFvcH7vrkcDXhFm3Y-H7uC7wX1DtIZ98wgcNmbwd9khxEPWGqMBaIm4McqCbOpy0ThuG-mvy_q8MgpZ1I8YQ_RSlXiHy_2uYSv6usSoVrLh5QxPVnKJOXb9QLYaK9p-KMIhrBHqAfc_Mp37HXmgeaRa5E-5XowI8gAkFrUdT5YUqelIVr7CCoV72H_ju2Ec-cw9D7AkBxVkSn88Akk6loKi1OikTbK-ywpG0auEzAe7MfQ57JZByoll8MVvuHNXEXKrEfmJC5pieiEONe2TNG0y5x4kE5ZgGUgBQiz-tnqUAg-yePR1w8CcJzcDkNWg-meHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌پرشیاناازباشگاه پرسپولیس؛ امروز ساعت 14:00 جلسه نهایی مدیر عامل باشگاه پرسپولیس بادراگان‌اسکوچیچ و نماینده‌اش در ترکیه برگزار خواهد شد. باتوجه به مذاکرات مثبت روزهای اخیر انتظار میرود امروز قرارداد رسمی بین طرفین امضا شود و اسکوچیچ بزودی راهی…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/23975" target="_blank">📅 13:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23974">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewTvkyYmzCR4IC7XnczFBIfLiuUbO4DM5zPHfHLyvgRWM9aUpdVaDdxiHcDEaBJbrbnXyh49iZuWYxIJqYGJAog15a-6eaX1ky1Akr-SdPPbjdlMhWYK0Hc9ojG42Xnhyr_uD4cOCzBbapMUfXmKhp_FPuMqmD8ugZwfNjbYFQLVH5ZyhhG8ftb4s68VOj3Md0KuXN-NOv-VCw8TqD_rfY-TPQua4MYIL8zm08vic2l5BicwPfONhcZXiyPZUXEQserBoiOjFZPoamDGFCk41Y_mSjixDRSAsIWobFVE4QvtXt8R-cNryFr1vBWnw24o9J3TopAf0dzTRZ5qMFvdqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانا؛ با اعلام فدراسیون فوتبال رقابت‌های‌فصل‌اینده‌لیگ‌برتر 18 تیمی خواهد بود. هیچ تیمی سقوط نخواهد کرد و دو تیم از لیگ ازادگان نیز به رقابت های لیگ برتر خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23974" target="_blank">📅 13:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23973">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415bb37d05.mp4?token=hFo1IwE13kN1tGzLyBe5srGKWiY0756LOBiM3tyUFnbsCJkPCvL3k769H8oAYnSistg7SQlHgSuwOFh2wDMdk-s_d15YszSCIJQ2DBbEtMAUa4kdQWacGMIWt50FbljgSMtVsryTXsmIZDW8v8sS_IpLjOcX468WfX_SXsXWAJ7aSk43YX4o9coRI_6svTf9w5qfGyrg5ijOZyj0s5iNOXeeZHnKDjG94uSG34uomOtpb0lAkkCQ8kJexq4pF3sP6WdeXThJv910hMJEPzvFkpG3GJjIfOCT4GfAwfQln15phnneD0rCllrs0urXrv2_NoEBoL6ccKUvISsZww9QJ12BQf1a_iLBXPgb5ezRw3lN2JjFvjvZ974oinihD5uIbSSYnl2z4NQE5r_f5RrRwQJaomZlc6nhEpsJmqGWk14EiZubbM2vkysCbQ4p7m-XETAhyBtni7WzzPSleQuHgVOmDnT5YgTubEeX3h1yX2lUS46b48Z4vZs_CTaY_OiMFv8Tno7XzkKryQGnGTC0Rzr5YYghQV6kyEV8UC1C-HY586xMrnT5MHWYpJVWMHcGjiDxMZ6jBVor1heXrKH6QO5BnjVxoaN9ucpk5tzLL1dKkjc9MkQaRc7EdadFXeN5all7u4yqozmGx_rCra9H88qNbsVfIm7PeRTEf_7Tn7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415bb37d05.mp4?token=hFo1IwE13kN1tGzLyBe5srGKWiY0756LOBiM3tyUFnbsCJkPCvL3k769H8oAYnSistg7SQlHgSuwOFh2wDMdk-s_d15YszSCIJQ2DBbEtMAUa4kdQWacGMIWt50FbljgSMtVsryTXsmIZDW8v8sS_IpLjOcX468WfX_SXsXWAJ7aSk43YX4o9coRI_6svTf9w5qfGyrg5ijOZyj0s5iNOXeeZHnKDjG94uSG34uomOtpb0lAkkCQ8kJexq4pF3sP6WdeXThJv910hMJEPzvFkpG3GJjIfOCT4GfAwfQln15phnneD0rCllrs0urXrv2_NoEBoL6ccKUvISsZww9QJ12BQf1a_iLBXPgb5ezRw3lN2JjFvjvZ974oinihD5uIbSSYnl2z4NQE5r_f5RrRwQJaomZlc6nhEpsJmqGWk14EiZubbM2vkysCbQ4p7m-XETAhyBtni7WzzPSleQuHgVOmDnT5YgTubEeX3h1yX2lUS46b48Z4vZs_CTaY_OiMFv8Tno7XzkKryQGnGTC0Rzr5YYghQV6kyEV8UC1C-HY586xMrnT5MHWYpJVWMHcGjiDxMZ6jBVor1heXrKH6QO5BnjVxoaN9ucpk5tzLL1dKkjc9MkQaRc7EdadFXeN5all7u4yqozmGx_rCra9H88qNbsVfIm7PeRTEf_7Tn7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ماجرای جالب آشنا شدن اوسمار ویرا سرمربی فعلی سرخ‌ها باسنگربان برزیل‌ و لیورپول؛
پسربچه هفت‌ساله‌وتپلی‌که حالا یکی از بهترین‌های دنیا شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/23973" target="_blank">📅 12:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23972">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7jyC_pD0_5UxMdzhboveOHCTQ6bHz88cZZKTykacK3pSvJAdOF83TW9VXs2c0HZ8sChI4myWc-bCjE0Ucc_psgz9_AOZpN4zLBm5ttvxb0lPvb1dDQlJhtarNXS9iqxrkM3IS3bXXyTHGNIUhVCU7ympYMljOvGp7ZJQqNmrdswWRjaPn07FdtYdRycC8oQsrH8ad-NIFwaxZ-wsHBGvjmYwpJJh89APqyoBX1gml7NCNjR90giXvprt7JbSPjvDXb_3R1vCffXWFC8_YTICWC8yPP05EGYEJhXss-gYS-IApzCl187N33wiQSVyW55h-hIfQiB-qCqicIcIMu8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکوردداران‌کمترین‌درصد مالکیت توپ در یک بازی جام جهانی؛
پاراگوئه با مالکیت ۲۱ درصدی در بازی با ترکیه، در رده هفتم کمترین میزان مالکیت توپ در یک بازی جام جهانی قرار گرفت.
‼️
ایران با ۳ بازی، تنها تیمیه که بیش از یک بار در جدول کمترین میزان مالکیت توپ قرار گرفته است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/23972" target="_blank">📅 12:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23971">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUGtzVryx4iouyPcZ3EJB3Ao9Pa9sHuHmqgoPEwJgQUl_lpFLPIC-YavFjqsc5Aj80Nw1YXQqQPVEMfd7GMsR7BWC92co16JJvZCsqVh-drR00zhBSwnnCPz7kRP4r0RIZVNjufz981PvulDgHyGwtFBaIQ396M_RUy7-DtNYa-bn90-25AVS2ubiEoC9XQTKOhQfUPsxM_g8AQqLSYMu-Zf5v5hVkkzyF8Z1hQunAGJTkvirMn_fAPGSxMDYWb33zP4vjfy0cGvcHzg_dU7xW65kAJOT5wdpc67lP_RAwSMbjS3mKkBHNCUNyJGH6qdc-NlLjK3-RvoKveX0ZmMdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
فوق‌ستاره‌های‌فوتبال‌جهان بابیشترین تعداد فالور در اینستاگرام؛ کریس رونالدو با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/23971" target="_blank">📅 12:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23970">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeT4YsER5bO8QSmv34H6xcMRREY-mHpCg_o6xAE51jt5YdQNGHuVkwXt2F9GkWciN0dm4_zNQOcSIhHCMVzpZeCfXggJPwid7v8AVd_7dYlzQWBH3moIn_rfayn35f7G92TJ5bYO9wCjFlL6jHyTSSEXl-KeKMG0MUzM7bUobE3fDArzmitU9qiXbp5JPzk5MRmEFVOIOGHhb6HE9ev5-zHeXUBSLhHjLe1gP61Ew1zY7aJ6FvjRvvYsXOwB5spn9JOfcufvySBivc0dwR-tqtdX2xTxO2Gshrtonc9dKRccIyOw32nPUgPI3jLaUKfV0642vB5joFwrXBLAzRHBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/23970" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23969">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d78439566.mp4?token=QZXQ8MT1vGI67Vu-oURG8budwg70bNTKotnevE-ww0TcKYuNJf77YI3ZYFWB2Tvi1b-gyYljUVlvr3D659Gg7orlf-RHGDbOy-M1IJf1P9u2W8Lmk8V1IBS6-qMcZ_KCGtnvqEIS9P3p5QFzAZsCAzdrh6T0G3-KgmTefT4t1KjNEFABlVXbLj6Huq8tvnobLlrWtMQK7mLcED6dp3HHC5QGdEs_RV8_jteDQsqFCq7TcTh8udDNinGt3vaBvFRCBVzogpQrr11l9JgoRramAX8NNJYe-pDY1vgcF_F8Fc68F9c8AIozw5reW8yuDn7SoD_ddQDwqi3ggfYh5biZnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d78439566.mp4?token=QZXQ8MT1vGI67Vu-oURG8budwg70bNTKotnevE-ww0TcKYuNJf77YI3ZYFWB2Tvi1b-gyYljUVlvr3D659Gg7orlf-RHGDbOy-M1IJf1P9u2W8Lmk8V1IBS6-qMcZ_KCGtnvqEIS9P3p5QFzAZsCAzdrh6T0G3-KgmTefT4t1KjNEFABlVXbLj6Huq8tvnobLlrWtMQK7mLcED6dp3HHC5QGdEs_RV8_jteDQsqFCq7TcTh8udDNinGt3vaBvFRCBVzogpQrr11l9JgoRramAX8NNJYe-pDY1vgcF_F8Fc68F9c8AIozw5reW8yuDn7SoD_ddQDwqi3ggfYh5biZnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇪
بااعلام‌‌رسانه‌های‌بلژیکی‌؛روملو لوکاکو دیگر ستاره خط حمله تیم ملی بلژیک به دلیل مصدومیت جزئی در بازی‌ امشب‌مقابل تیم ایران فیکس نخواهد بود و احتمالا این مسابقه رو از دست خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/23969" target="_blank">📅 11:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23968">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
رکوردجهان توسط یک مرد اهل جزیره کوچک کم جمعیت‌در دریای‌کارائیب‌شکسته شد
؛ الوی روم دروازه بان 37 ساله کوراسائو در بازی دیشب مقابل اکوادور موفق‌به‌ثبت 15 سیو شد و رکورد بیشترین سیو در 90 دقیقه‌یک بازی جام جهانی رو شکست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/23968" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23967">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c204841a.mp4?token=PE23OgfBoAsgaZMbAUGt0LGc0srK1fGxiyta8s5BNC0UGzjdw3VtRrGWosYKkNeqiQPGAjI-6k30CUyr9LhQqK_pm1vUjFIZ6yL3IUAoRlxFJGVV5CpdNLJxYqwcl8YDCwFz3JeI-wIQk0ogOfLMaJlXYNqxuZPmk0mD2m8xZUMJ9CwQSFm-2JshZT36RqMf_cvQWxmnrpfAYRno6m8-IEaQD8qhl_8F-wElCmZIqhVqlk5p9AX3hYc4ahKNJhY_orU-z2GtyPxSN6im49-E7i4mfEzYxLjwGANi9z4DISwo2_LBpaUFVXlvJVEHD0cmLQNhDRqh4rt0SG-HuUALeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c204841a.mp4?token=PE23OgfBoAsgaZMbAUGt0LGc0srK1fGxiyta8s5BNC0UGzjdw3VtRrGWosYKkNeqiQPGAjI-6k30CUyr9LhQqK_pm1vUjFIZ6yL3IUAoRlxFJGVV5CpdNLJxYqwcl8YDCwFz3JeI-wIQk0ogOfLMaJlXYNqxuZPmk0mD2m8xZUMJ9CwQSFm-2JshZT36RqMf_cvQWxmnrpfAYRno6m8-IEaQD8qhl_8F-wElCmZIqhVqlk5p9AX3hYc4ahKNJhY_orU-z2GtyPxSN6im49-E7i4mfEzYxLjwGANi9z4DISwo2_LBpaUFVXlvJVEHD0cmLQNhDRqh4rt0SG-HuUALeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فیروزکریمی‌کارشناس‌ویژه برنامه جام جهانی:
خانم‌های ایرانی می‌توانند داور بشوند. حامی بانوان هستم‌. داوری بانوان از رانندگیشون خیلی بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/23967" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23966">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgnJO2_AOvK9TEPExFdt1jhyHZQWDkAign3Nci_G1lCNX4hCQmY_HQiyQNqMkx13sOCv-aT3zSXHNmGAcoP8ui8kH9ZHHXgylaRQmisP5o3iPdCT874Fj7SoLmD2wwwNj6fRFKK6T2JvgCAzn-KHPCFbR02t8HK6SirqRjdfZVuP8CFm5f4Jd0ADt3tDA6uKbJLhCJzc_D2qQzUSHFB_l9fHF_hjiJPRH95Wbo8UhFkdsGxlL6a7oU6T2nHNF6njmodC78P7pmbtRp27Pp-0pUW0IZECARkUwuMGsST5ctn6a7_ziWTeAl_duk1m0s_QnzF2jPyPUCfGR6ja6aOwTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیشنهادویژه‌فقط برای بازی ایران
🇮🇷
- بلژیک
🎁
🤩
🤩
فری اسپین رایگان کازینو در انتظار شماست!
فقط کافیست حداقل
🤩
🤩
🤩
هزار تومان روی مسابقه ایران و بلژیک شرط‌بندی کنید و
🤩
🤩
🔠
🔠
🔠
🔠
🔠
🔠
🔠
رایگان‌دریافت کنید.
⚽️
بازی ایران
🇮🇷
vs بلژیک
🇧🇪
💰
حداقل‌مبلغ.شرط:
0️⃣
0️⃣
0️⃣
0️⃣
0️⃣
5️⃣
تومان
🎰
جایزه:
0️⃣
5️⃣
فری اسپین کازینو
⏳
فرصت محدود!
همین حالا وارد شوید و شانس خود را امتحان کنید.
هوشمندانه بازی کن، برنده شو
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا er31
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/23966" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23965">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVgwp7TUVX7UQlTf-qOUzbcuJfgpkbDDfHc6s3-Wsw1npmhk0O8tD4D96HsQR6lJ2ePoISq1QyNKWiL4rfYHtna7xK6uZ6RTA6L3Tk9gNrnlsK_KlJVfExvLxScQYLVvFSuMdqwwXES0Jz6bhraAT-mxUZ8uZxcZUsTX2lcsxS3fS-e3uERHqITRi9ULjCabi0KBUKpbLUNwxKvYO4oVvEIIJs6ElWROCs_qf1qEYvC2qyzm8FZfvfh01Brn2LrooaXf6jkXmxsUlLd2YJUJ3uZAWsrE26GuFno7jJsKaOB-N3mgA5EicRwTUA1JWHPBzspGdiMuyjlepJbMzZ7t2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
طبق ادعای رسانه‌های بلژیکی؛ گویا روملو لوکاکو ستاره تیم ملی بلژیک نیز دیدار امشب مقابل ایران رو به دلیل مصدومیت جزئی از دست داده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23965" target="_blank">📅 11:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23964">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBpSNP-eB65-tiHV9BXqeb-2RKtIuQwr0oYIjrfoZoU2W8TcsVNPinq6aGxkTzfjTAiJMq3Lh6S_2YzgQxvJWC_o1RLBhK3m2TlLUBt7oVUm9KOY-U0bigJ3H8hx46jzXrKn6ZPYj4AF1k8pSane6rotxtYyo-_Y2g3xsPQ_XhVWxmTBPfrJckrGTXh8xb_ELjpaoAZmzvWZpPtgPPh3c5TSdWxsaaMio0-kmGH8PN79SCX8j8unY5YCyxvcN9z-a3vQXWxUHycEHJXmbs_WE65abhVhVPKPyXZWjCviOI0n1caINlePHKLFpcAvPpISc32X8NJ6w9RD5BmsikbHOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/23964" target="_blank">📅 11:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23963">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH2evKFOr7ZBP3hw4hiPFK2qLj-1IfqUOYj_PXATFhVi7Sru8CpQ1d5uO5vPGsVgDSJqN9Onha3f9DWOTHanjFJTR222wwPVq16mY82Frt6qRDgDCuvC00mZBKREcIiOuAZDRIudDnjyfPKZf1h1cFobXBnZpa81adbfxLEMj7nswHbiRb4KYikGskQ8G1U0-x-6stU0E3iu0YA_MOm91QWU-RJ0wYlNBMrOFD0Jd9U58F4ihnWN_4ikkNkC0YDquCPABAwNYirPo1q_Kqvtj0O-YFU3DmDF4voAFcpySZ9PRxkJo5m93OZdhx1Zzb87yfeWq3Xjt7ci28rhLH15gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛باشگاه استقلال امروز با وکیل‌ایتالیایی‌خود تماس گرفته که این وکیل به باشگاه اعلام‌کرده‌است که نهایتا تا پایان هفته اینده فیفا پنجره نقل و انتقالاتی آبی‌ها رو باز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/23963" target="_blank">📅 10:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23962">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caZWsBnquqJn_FUz7etX4ekibKsWeDSGxUIbE6i8IBzIYobUUfLLLBIxBKC8h3x6k65CImhafh5aJhxV86ttu2z1N70hZP48UTC0AC60SGYeN-a9-u9bg8vVlDlfEXufYrT5IWJvt1YHZIVPoHtRUm_QPdNB5YnlmkkCBS5aO39W7CCxXWJD2m6JR2hmLnKfizycMiGZfexWw1Wixwa1n64fzfwvN_7YNS2wOtX6ztOaWF44q-9xzqSvkAquzT8B370OnyxnjWi-F4S22y-mX63Lb_NMlESDNbZqNLsuFW_Cz8fve9zXMQ_nPxwAq0mE9wn6G_y9-Ug7N5ofb_rZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پرچم‌باشگاه استقلال تهران درحاشیه بازی امشب دو تیم آلمان
🆚
ساحل عاج در جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/23962" target="_blank">📅 10:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23961">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8CEwgFv1ZFp0ZvJ2ahEFuSfLeJLX-OSBC8GpFZUevp1dCs_lSYT62YFbG0RgQDx5Dyy-kP1l1H2r-c6ztKKHG0FsSoZklv0lvpSytK2OwLwV-WskA1A7bcFXzCAS33GTvPMnsmJhVjPQdXraiTVkZL1blPyiTsYVKn--_m1UnXpT6RX1yqLm7-HYwD9Nfj6C0YvTAtdb8WcdAA1oURROjXy-D6xqvF6uBSgKrq5WDp_Grjlnu5dqG3Rq9rOM5Q5Z4Myclc-h8tGK_DVPCHrLK7Bgwh-y8Ae86YnPuIFBujpGN5sihiwwuQ9gbI2g0IKExcDK-TVDRCzh_uJwmoV5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آمار پیروزی تیم‌های‌ملی‌آسیایی درادوار مختلف رقابت های جام جهانی؛ کره جنوبی فعلا در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/23961" target="_blank">📅 10:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23959">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550fbf8a8f.mp4?token=lHXTQUm_1KN7jPMrm9-Jh0HhC7jBrce8hc5aB4B8YOHbnUok6QQniohiCkvIj73mZ-7lBQxKEDF2lv0JtU1aqwbNM9DPJfCAehf0Fl-lATQ0JTGfFB3FIRgfi-8BcBEMnNhvN-zZXl53JBl9jTph8mBfbK8aDu---nPA4LTzIpNqVVsDdjMB3xXEXqAOS9CJ-vKi-V6bpIfP3QeZJQ9dGYQCACUb_T60tXBGHfYh0FMV9wXY-REYwA4UOTgY_LZ9o8PbMaVhlzHeU0TJxldhF-nuC730bli-U9xRmglFT69XiAhdrg47LlRQo9F8I_ecSyZngigXGdfWiU9zRYq5Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550fbf8a8f.mp4?token=lHXTQUm_1KN7jPMrm9-Jh0HhC7jBrce8hc5aB4B8YOHbnUok6QQniohiCkvIj73mZ-7lBQxKEDF2lv0JtU1aqwbNM9DPJfCAehf0Fl-lATQ0JTGfFB3FIRgfi-8BcBEMnNhvN-zZXl53JBl9jTph8mBfbK8aDu---nPA4LTzIpNqVVsDdjMB3xXEXqAOS9CJ-vKi-V6bpIfP3QeZJQ9dGYQCACUb_T60tXBGHfYh0FMV9wXY-REYwA4UOTgY_LZ9o8PbMaVhlzHeU0TJxldhF-nuC730bli-U9xRmglFT69XiAhdrg47LlRQo9F8I_ecSyZngigXGdfWiU9zRYq5Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سرهنگ علیفر:
از اونجااصلا نمیشه گل‌زد؛ واکنش صادقانه آیاسه یوئدا بازیکن ژاپن به علیفر
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/23959" target="_blank">📅 10:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23957">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSoNIK1tD9Mk3Xf4EuYPcXDALo4J2q_p0BpoplJ2uR9uJHu5QoTHl-A6DFeLupW638wAMxbkndKeyoBMQXKeGVar1y4fZgO3V-evo-azMyNbgV0JjECHGDafA0beGQtI7JLe9SAQwTzvWdP_Y3JyzIX2h4rxnw47QbV7wuRlpMRaHgFGeGVMCblB7uqn836cFWW6pHSTUvigiB72Hrs6DefL6UpHObJEHJbGSUMNpk_24S2c3iHBDqsBT_nFTR9Zu_RsCDstUGXBloibs56hyKDnyr2gKMwSaXF3ryCx1SSC_lAG7O7c7JyN46rKGc2hgTWcHvwHxjO_-Q4ulavyiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2roYN7wN957X6ZfdcfQ7cMl6tLRHsnHvU-15DybnLY2RkeEc0AVR1wjyOiCrBxV_uS4N82TLJoNQl6am96HIeW7n851KmuIRj-iutsGi96wNUrVjF699f5rSY9H7vAcWZT4PO57svSme1HrpH8wqxtP5qPeE0ztJMpFbLxe_Pk_1uD-8oHfW0NQxw8b8N3CI1SBt60MhMn2xnDQ6irIFm1qFopF9vCYWZ9xxNqa8QT9lOHUZ0H0amat6bs4gg-4H9_SgPHM-yDB1tVzYFcxWIfWXsm5LKM7TrOHF9xmvCpa0kOFgP68QCaisp3Qugth-Vkf-c3SECc4MK8zDpYIwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23957" target="_blank">📅 09:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23956">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1ZDqF6BZUFmtP0N0-IfpndXIpzFCOMveKf1K-UuJALqyWW6ovcJKvsIOEEY00m2-L9omwcp0XZ52-yObxm2FZ23Hy6Km4hS7O3ta35FO7fbIF4c5hG1j2_6rsT1DpZv5ifOwTBQvfpXiC-JVezi26TabXF1zLUzkvP5qbVC9xG2iM8iEHyZePAQ-f4L_sJT8tYyWqNmhye7DaCnkSemOB_6tKiZST_TBmMy0VGXoDzG-9A4xwNLThw2zRNbHJdp2EyppeqMsn2WYaWXWSE2o412OCAqzlVzho_IyhAXwmjV7Pmkb1HlEBr3N_qVQtMIWOSYCGzm6mM2VCubqZAFhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
رودی گارسیا سرمربی‌تیم‌بلژیک:
مهدی طارمی، سامان قدوس و رامین رضاییان بهترین بازیکنان تیم ایرانند. رضاییان اگه 25 سالش میبود الان در یکی از بهترین‌های تیم‌های اروپایی میتونست بازی کنه‌‌. چند تااز بازی‌های او رو دیدم فوق العاده بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23956" target="_blank">📅 09:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23955">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOljrrBvmZTpmkwhG3iczplb_cuXFmIvr18YS4dTCHD_9kh7yCAVmOwU8GzWxQQtaVwzJM0OAoC7FEUHVMP5ZQfsKwNMW-i8DyLqQvfY2p7tUZBrISP9lRnFtEZ86qJbEFDleB2G005pbZVF9XlrgHyhDF0zjbHfkqg71w5bHYxsFvnAP6aC4r69hwegyfATWjWB4lma0M577VN6DPxuzi18yZcf9b2Pi4F1V90Sy3b4oa_8UvXA27iKJNl5MX5dRBFkD0R6a0N_udMtjLkxbtIE9ChcRJhmBLMdmuy_aN3RaMiFN9UBRFcxJqwTz2EYV5FvpUKMmGjGE4L9q_vtfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23955" target="_blank">📅 02:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23954">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkNigWgx5bUzDNT58cOpJcFBHlDV_8c2gLTFYw6V3D6QcZff6inbLPyagNAIzwo1ZDAjo2QthxHNvLMKBgfeQVE3MxUN7X-H556XRbnQ3yAZB0VHKbAAa16qAAMOD8UIMCMhqdDI5kA4ZkCNyVcHwrs21VOHEGgGpSkmZ7wVer05lToWloo3T7rQRCkHCUyZnH2dbMeScWkfTd5w338kUlLyBjgstjCYh0rrSvQS0wfJVTm4XG1QYo6tx-wFEVr7eG1qDdC7011q2WsCNP4QUhHPYMzPq7dUi0fNgxNqoh6qznW6ov2K8FIUmhqN1pH7Zf8WjvbD55GPj3OlT8GUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23954" target="_blank">📅 02:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23953">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcsVHwqXOGw6_nmq-KVVJsO_-aOrK44jW-x5LpRh1L9zUUWw6ZRMuQNd_kekWcaiyyFGwy0t__KrpHu-kxsyM7Uvky1yrUmB9hIDVWchKNaqLogtY3bpQPoz3flHNOsvWvdsXu3YcduFAr_bsvODHqO0XXkOdftG6BNaF0Zt1yOOeT26jJRi-tXmowLxd8J2zAzbb6pNHiEEWPjoPK49jIJUG6aT1FU9bnCPUK-87fXDmGezU-bUQ5Qp5TSB0IzlRwdfSqhgpvgcngreMxgAjCmP7tlX18xZWihi2pZWyR8Irx0uoskSSRitEA5pxrAJiOHpduv-YqiYA2Cebr448Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23953" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23952">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PG7RJhAuKckc4tkIV3Lal-gH9m4cxVl4P7lNvrSRJicgGI2rbt05uTldgGNO04aC4GBjhTZy4FI8S_Hh0eKEDYVhHlSC_q5IFv2mqD_gRTA0wF1bTCwD4EiAR9HP_4ry-UIadNNkcI1vRe1WUyjMUoVWqAHIj_cqXQk75OGpnNsIQKkSuInGrVNLrGs70U0BqqJ1axl34VCm9mKOIM5eYJybpl3vRUzDfNBIhhedR28meoTtHNUxFlPb-YLPD1eGc42np9am3s0ZkcKEYTKYibIy-D4ABp4WujBywatmbBIU45aehKmt66RRP3URzo_ke6gYbg7mdEy7dja2TG0iwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌برزیل و هلند مقابل رقبا تا راهیابی مانشافت به دور حذفی جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23952" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23951">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=Va9hu9Zxn8Z9g6bi5qfasXg5qpNqqo7r_DP45GNvnpQkER9pkVHnRjFWzLu9yX3VxKFBahDK3NYGLN6N6oYyIqfv9vMua7UFzmEseljkyXG75jSjZ1IL3JzB_K8WLZXmMLPqZmC-BzL5-jauf3ULzkCBe4Lbho7N7gwp4KISALl_SB1F4gjGL9Uu0uZ7JOFfkWbLnon_AqoLXOhz-ZZ6A4mMPoRaqUFUzxA4-XwZQcyAHQo0IYvs9V5umkr38wG67ioRM8INLRIP3UTeujOCbPK2et13QUOgPAGfPwaGB7tb3DeG5zx4q6dUsiH_Dz32VR9AXDa-CEcsbBVqfSbI1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=Va9hu9Zxn8Z9g6bi5qfasXg5qpNqqo7r_DP45GNvnpQkER9pkVHnRjFWzLu9yX3VxKFBahDK3NYGLN6N6oYyIqfv9vMua7UFzmEseljkyXG75jSjZ1IL3JzB_K8WLZXmMLPqZmC-BzL5-jauf3ULzkCBe4Lbho7N7gwp4KISALl_SB1F4gjGL9Uu0uZ7JOFfkWbLnon_AqoLXOhz-ZZ6A4mMPoRaqUFUzxA4-XwZQcyAHQo0IYvs9V5umkr38wG67ioRM8INLRIP3UTeujOCbPK2et13QUOgPAGfPwaGB7tb3DeG5zx4q6dUsiH_Dz32VR9AXDa-CEcsbBVqfSbI1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23951" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23950">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exU-xW9J9CH_WkhPd51on3UT7vgt9y6cZsfOOqNhR9SniZhnnh05jcjvWqixJitCZCUDC2D6M8lIxtZBrnzHVyHqE30mTJsuw1fKKAv5gbkUaAmu97kSOBm57j4HLngvqrldrjT2q3VA4lJ59u4IbbeOcxAjmeRZL9vBMQ2frqFwAXbl1ld2s1ISVumKH7J3KYFgQQPEow9sDr3h3NiHO55sqCuJh5SFKnhmfTaW-iWcBa-5K5iK2I6oGOsC0gBStMy4YP35xpi3x5xrVMzQh9tD2uOG18BO8fmMMxleR1kQTA51RzJeJeDSbWzjzgqZnYhzgFXy9E4msR9MzDtXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌ گل‌گهر به مدیران استقلال اعلام کرده با دریافت20میلیاردتومان‌رضایت‌نامه پوریا شهر آبادی مهاجم جوان این تیم رو آبی‌ها صادر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23950" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23949">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdXsMlCidCU6Rqd5XIhKNRKszhn1iJM_kGlraxJesZ7P8hjMUgvfbxudIEYiWzwDaU-1FiXh6mwN7mPifMTnv3sAiJcnQBS2wJ7l8cdIbBvsIbg4aOYENyCKL-2CzWF3vmM3oBaj9z5_ZsxJRwCum2PPD1rFHV0pJS3uu2bjDUQlVB4fEVfvKeag0HevL8bElTmjhefJXUqHDA4bFgbCh6Ui9HY0CgE7D8T2po_6Xdy0uTJ6Ht1vACRC88CEe9IYrTNwnF-vCYpvtTKXeTbcv80sHEpW7PpGr-vPHrM7PASoMBis_AqdibxmlXCyA_bXkFhhvYOssJA0ImVF_TeRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
آیسان اسلامی به تلگرام پیوست.
⭐
اگر توم از طرفدارا ایسان اسلامی هستی بیا توی کانال تلگرامش فعالیتش شرو کرده کنارش باش
🙂
ادرس عضویت کانالش
👇
e30
👇
https://t.me/+QMjHLL65ocsxYzRk
https://t.me/+QMjHLL65ocsxYzRk</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23949" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23948">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40b51e8a93.mp4?token=hzMuZFRpTc4wUTfgBJgzCd7dr1pcI_60XljzfLbNbP_JQJUi1wtE3fkl229gZUssWeUrXpekgS5-xUADwYc42B8VH1823IT-h43zmo6-FdVqV-8RRhNAp9rgWsZmQbbj9pNAqmFzNa1566EBOX6jg_sQuSa7HaNtbrQRUujTHaGyZxN8XgbbuLsNSYU07nm01wbjmipmca_-uWxUVvKGHc18LWvcqbtsrCKDwc9icIXaeE6te-haxvZ0WeQEv5OK7KDMPhdqQf6UXwCzFu6jvJAUq0DR58ywolKATzxoqF5Yj-bYcBbgKA8LI7f1UV9cUjksLk-zr7yP0vb0OsKNrhMtrKVhFjCnfYMQj1NalOywkVi7KMaOHpH_xS8zbwcFas5vLRvu_dHJ72CqFoOTvH-L7N_3_Tg-kQXrmkS0qQOF84ppSjuo7ShFXQd1dXZY_H6izeOHMV-qfsK-jN_mHkDVlgWRfmWzQUnddr0QDJw7tKePi0rD3xvpfN4e3FOQklh-Q7-2BQhhXeBaGA4hDU7G-K5ZI5-EugBZr3S9lEsKV2jCU8Z4OMRrhxYAzyar7PwurBf-nAgdpKYTvY-hAGcZpj9cXk3Ic2-R_7sirujkadti-9oooaLxEL5woJBbjHByLqNdP0RapbqzEo4aNaBavx8y17iZsnktD3nh0vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40b51e8a93.mp4?token=hzMuZFRpTc4wUTfgBJgzCd7dr1pcI_60XljzfLbNbP_JQJUi1wtE3fkl229gZUssWeUrXpekgS5-xUADwYc42B8VH1823IT-h43zmo6-FdVqV-8RRhNAp9rgWsZmQbbj9pNAqmFzNa1566EBOX6jg_sQuSa7HaNtbrQRUujTHaGyZxN8XgbbuLsNSYU07nm01wbjmipmca_-uWxUVvKGHc18LWvcqbtsrCKDwc9icIXaeE6te-haxvZ0WeQEv5OK7KDMPhdqQf6UXwCzFu6jvJAUq0DR58ywolKATzxoqF5Yj-bYcBbgKA8LI7f1UV9cUjksLk-zr7yP0vb0OsKNrhMtrKVhFjCnfYMQj1NalOywkVi7KMaOHpH_xS8zbwcFas5vLRvu_dHJ72CqFoOTvH-L7N_3_Tg-kQXrmkS0qQOF84ppSjuo7ShFXQd1dXZY_H6izeOHMV-qfsK-jN_mHkDVlgWRfmWzQUnddr0QDJw7tKePi0rD3xvpfN4e3FOQklh-Q7-2BQhhXeBaGA4hDU7G-K5ZI5-EugBZr3S9lEsKV2jCU8Z4OMRrhxYAzyar7PwurBf-nAgdpKYTvY-hAGcZpj9cXk3Ic2-R_7sirujkadti-9oooaLxEL5woJBbjHByLqNdP0RapbqzEo4aNaBavx8y17iZsnktD3nh0vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23948" target="_blank">📅 01:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23947">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU5bepStVCZ53iWeF3UvUtIRv99nAHO5wf8eJIsUvdzHpwxITnZNmO4opGnMKefstM_AJ8DMAGXkJTb634mEHOb8OaYrXxejo13DPv7QmrcJUbn_XZ_H0pQFspRgSR4E_wXe1EG-arOubNdRG-L0EfnbTyiSqSbou-mYirMJu7NoonEmAMhGqvGgHpSJEd3JHn4L4_WLPXye4YUNf0VPUpCC-g3WrnD35gYD9NHyZStVTUQoD9ECQpX8kHg0FEPR5IYdbFpq5h_HGZjdgufBOJ1KYnzzYqu118GNWnhgE1utFhQBqCrLNE-ekw_4HJVJ75yd507SDa7lndja3lnm8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
گل امشب تیم آلمان به ساحل عاج: ندیم امیری بازیکن اصالتا افغان پاس‌گل داد. دنیز اونداف بازیکن اصالتا کُردگل‌زد. اونداف در دقیقه 60 به زمین اومد و8دیقه بعدش گل مساوی رو به ساحل‌عاجی‌ ها زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23947" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23946">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsqHgy_rrd8HXxpvQQDKjR_pGzacO4rggG_9C-_RkZJecamHgqRMyp4dGW5BMAO4NCfw6scrBNO90ErKvc3-TJOx0ZBl7P-W3OR1VINGTS7p8GpGQCbtOU03o1C3ZtJ_v9oexg60tXbkefryRcR4l3TudUy_ght_xsFHt5_GOmJ4GLb-ln9xqFXpC99ASwTCcMUVzPmTdoCwxLqzlwGAhzLHTp-XSfvuqT3kOkTo-NjfTR1lS2VNlEOQ4oxOP3ZAJDDLGZoq4dG1ThKKdBi19uLK7vpa_LVdRdjG80RbTltY360O9RZVChqAIsNlPQp49jg9deICEDjQX0drnJ-elg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23946" target="_blank">📅 01:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23945">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TexTjT393f7QGSjqX9xClr805tP4Gld-RNrVI7CBahwTP3Un1Wdkh3Vz_M8hehSZBmoVhDBG7jLjYtZE-Fo1mMhoP7ILGb8fQBroEX7ctSYRTHs2-QlM6aSscxOyIbLqOC4azCmCL7v2x8tdCU9s8AN6gxv_AYCvk_bg2vaJZanJIsiVhgnp0auW8KIljYSpnised6wgMez8wc3rH00m5zwHlWJFJv6-Im4Lq5vC2G00HKUNH6_gkRDJ-cJwtNzW6IGLktR8jzuLdPAHHKJfGiXexJTNNebjygrQmFs3qDSOz4419M5fZ9VjLLyKkZSYCJ3Ox8JV-vv2sl9cUm8lDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
امیرقلعه‌نویی سرمربی‌تیم ایران به این شکل نشون داده که ساعت رولکسش رو پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23945" target="_blank">📅 01:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23944">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb124e2149.mp4?token=CCDKm9HaaiXXCtrsjCl7cPkmR41yXSuyOQYmj3_xbyjqHdNAXPmJWnS7R-rHkNMhsrYuSOQeZQ1BTAOC9osrc0Lfo2PipmbCZq428hyggLqNqCXR_9fPDeaJgVPI8qatmlX25SIzNi8P9wdBd-36ylxgHazNada5puOx3Qg1kOo6kmZ7FuLj0Ig5LWNOqRAkKoWMJrHA98nW79wNwM7c5ICu43j0U3C-t6ITCvOStlg1lvwD-BGrschFLT-Ka9W-DJP92c96uizMVLxB0DRNFpq_iGTUzclG90NwQXRudS-_6AR4KTouy_FrTduFTIFxAnuQYGmGVjzwGbym5Heepw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb124e2149.mp4?token=CCDKm9HaaiXXCtrsjCl7cPkmR41yXSuyOQYmj3_xbyjqHdNAXPmJWnS7R-rHkNMhsrYuSOQeZQ1BTAOC9osrc0Lfo2PipmbCZq428hyggLqNqCXR_9fPDeaJgVPI8qatmlX25SIzNi8P9wdBd-36ylxgHazNada5puOx3Qg1kOo6kmZ7FuLj0Ig5LWNOqRAkKoWMJrHA98nW79wNwM7c5ICu43j0U3C-t6ITCvOStlg1lvwD-BGrschFLT-Ka9W-DJP92c96uizMVLxB0DRNFpq_iGTUzclG90NwQXRudS-_6AR4KTouy_FrTduFTIFxAnuQYGmGVjzwGbym5Heepw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزهای اخیر شایعه شده بود ساعت ژنرال فوتبال ایران دزیده شده که عکسای رسیدن تیم به لس‌آنجلس نشون میده‌که‌خداروشکر این خبر کذبه.ساعت‌امیرخان
🟰
خط قرمز مردم ایران
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23944" target="_blank">📅 01:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23943">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE56T4cDhI_0ZDQMRw59vMF8y8fp-eIeNemfDPT324lJ0VBPq0YNF-Fjm_rD0jZpj3Q5lVR4NYaphUrhNgnnNwxG6SyYkSGMHp4dBh4o8zRqIhHpPdRbsUR2kY4lqd25P6eyLbYdxTfwVSqv9a9efha6PmTaVu5zuLmiL0njz3Hm1q4hgibYkL8-sr1_KQ4NTQavx1HBnJOdeyuAdtSsi3N1nCh-ZjDPYBzMLLIpVohTOWeaf5P6v4Nx8V2MzIAFiHq66WECoSHNknfYu3GfKb80zugagaO29Xv4sgy4DtmmTYQgcw-zr5rOTQ_d73NnywsFiAcEG6auDVrJQRKKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23943" target="_blank">📅 00:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23942">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnu3rdG57mFzPLkX6K2fBc3rWaIA_5DqhT9s3SnfxtZakAW3C-nFMjQgl-i7gkFtoi7apWTYFjHtMabzRCWDQ9qUTjwoT9B70t2JN_WF4c573DIIaOl0p0PSLhlt9JQT0OCGlST6XcFPBB63h-jRykHtPnW42PdPTCc4Vk7sJGpLovD07EMZrsT5OBUBGUPNDEVg_Es4r8HqS9fa6_xwPdUtfSO0WOcqf1rUzD4gY4YXRUqOS-9JD88YogSizScYbQsSadpSDaZRfpHNVhXyrEX0ln6cRSRrkgCBFy748-ElYbh1348fSTf1vZqLGLBFBoau7Po-hObfMYFi3UCHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مهدی‌ گودرزی ستاره‌ جوان تیم خیبر امروز از طریق نماینده اش آمادگی خود را برای پیوستن به تیم پرسپولیس در نیم فصل اعلام کرده و درصورت‌توافق دوباشگاه‌این‌انتقال انجام خواهد شد. احتمال اینکه فخریان راهی خیبر شود نیز زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23942" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23941">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=r-5vsb1WGgxONBeoyuI3pILcJWh_C9tU0MomCal4fBYF3OdeT1m3raBHTD44igzh45fyHyF-4cPfSzZavHffGNvfNOiAe839gSGT6MeAt5WdZrDeWu7nIWaUrO3YtwpRJaclb1z0MvBb5-07Jqw-rG43xkBw5mWn691P7S8LVUKJsRwJE9ndVSDUGS_nQ9l3m_rX1BPx6DNOSH6JC1hjJ6L5GgDFDpEu4jyOYMe7zr2oQl8KmL4DN_3j-AFRqSgO4J3mxEKoPYIxf7n16-6deGPYIDr8P_61g5NPu7ETPUYotT4b6zxHrMSUni_tPpDRpkCsF0RGrE55vNPlU96u1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=r-5vsb1WGgxONBeoyuI3pILcJWh_C9tU0MomCal4fBYF3OdeT1m3raBHTD44igzh45fyHyF-4cPfSzZavHffGNvfNOiAe839gSGT6MeAt5WdZrDeWu7nIWaUrO3YtwpRJaclb1z0MvBb5-07Jqw-rG43xkBw5mWn691P7S8LVUKJsRwJE9ndVSDUGS_nQ9l3m_rX1BPx6DNOSH6JC1hjJ6L5GgDFDpEu4jyOYMe7zr2oQl8KmL4DN_3j-AFRqSgO4J3mxEKoPYIxf7n16-6deGPYIDr8P_61g5NPu7ETPUYotT4b6zxHrMSUni_tPpDRpkCsF0RGrE55vNPlU96u1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از دست‌کارای‌ جواد خیابانی فشار افتاده میگه حضرت عباسی این کارها چیه میکنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23941" target="_blank">📅 23:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23940">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJOMxK165KRnNbQAfK6dHKitJBz5X52qosnCd0GFmq72RqLy6dXD3IXo-_dQplUcG_w8_1gXow-mXp-1A8FhXzjMPd7qufcM6XiAqUskyf6X8dGH4P6y8p5-5iBjJvLmMe5jg9mRMd5cOoQqNqInVDhlqLBzPQsO0-fm3BOq0mDknu_HBSH_zP-2Qt0RJoFwUE3eHN6AXtUDt-Xds3k0JoPhtaaoIQF-a1sFfbwbnlRXkle41hCNg6rKu97lOQISTeQu947hkXF36C3SbYXXmy3BI8g6_OLdZ-EVMkosy1X6g5kw242xgAEphmtvFuifxxStIMa8vJrCR1u5GdkTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی‌که در جام جهانی ۲۰۲۶ امتیاز کامل ۱۰.۰ را کسب کرده‌اند: لیونل مسی مقابل الجزایر؛ جاناتان دیوید مقابل قطر؛ کودی جاکپو مقابل سوئد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23940" target="_blank">📅 23:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23939">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJzjvK0Ur_u0KvqV_VFH_vBKAmUghHBtZ5MrKj70pLd_pqe4iHqnPgixe72stRpey4It7tCrohsSFt90TEksMq40jJefAMKnq_z9Mq3xQxCrP6qxG6TiIIjdCe5o7CQqOdEalcULARw0MJmgk1f_tgNtW7ZeyzpsMQF3YgZmnzI3ndjNdPejib7DefqK_jgIkmJeVDbbYrOlcYVLT849VrSEZKCxzk_HbqyZ5eYeraiV8WmICYq0Fe9F7zuEH8nP7jeCSeJ0SWavMKwODtsCos8crq7001NfoiUoQTNt_ZvRwre6xwpuqulSV5pOijpmHttrJOnt58zhO5sVm60rMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23939" target="_blank">📅 23:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23938">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_ObyA2-aEaFBX5KMEIWtjojLVSREMTRvj-vnXNcmwfaO4_z-b3ivkDRh9Vl_w4RtMFQyBLpLtjosQPbUo_RgPowTarxhBI5tKO4rQsvwMD_HfCCohBcqJ9n1YzhmBxh-wiIXeei8raMC9Z9E59kdumFeUKyiBT4nxQkkxCF_XgkYPe4UdQjDYqfsSjoaMeJo_qZF_JXoqJ2cLYCAtNhlhuBUOa9HXxG3hQ2Y_XzrHIJgow5TXSZ9ClCC17hVYr1aKSFzsytmOlnx5H2lVWYWwaoV718ItKAM_KXg3EAvR-RTq-6ePjQs5yWO5Zjyyw8Qi4a5zf72QijnZm5gH2T3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23938" target="_blank">📅 23:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23937">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qhh02YrScFqmUEXqLBmQOGYcIVo9KkSdNgmsydTUv1JtABxoAoz-Tt4Ca5WXfvI7b_2kxu3knI0TFm3Vhif8XbrpqzB1EAboBGqY3bT65znk6o9PBd-xzleWhJOJNy3658QBhotcbNfvw4SeuC48YH8O-pF5s9ADAaCLDK9qABCTuKMPozHhZarYYOBYvu6bewR4DSwRFL4kSWjo1c2wVmLGQ4vOOZ7p1zmDaI4hn5-82TuqZwhqyRCS1C8NDdu0XL79rQBT3iNYIj03azkG4R5Va4zEf2ZSIi6vp0vbqjHnAgDFTKJttT94rrtnpvDGnQnSPpecaCfHMrdN5Z9nng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پیمان حدادی مدیرعامل باشگاه پرسپولیس برای انجام مذاکرات نهایی و عقد قرارداد با دراگان اسکوچیچ  راهی ترکیه شده. به احتمال 99 درصد اسکوچیچ سرمربی فصل پیش‌رو سرخ‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23937" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23936">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e541eb115f.mp4?token=kNl8VyPU7FVjGngmcW-wtA40dSCAiVhLdUg9uzJyN6W7KPeDMqwyK4zX7rrep1ITz1gYFcuf22bkZLFcp2Y94-ZHwAfyRs35O2_bEQjadUNjRaSUWyMdni9_fCbfVK7-GkLkQJHvvDaR318rDyJYE_gRoFwUSdO-oMMWB7BDWrmcYUN7OhZpRDMhleHt49KLX3fN_8ghx0_q3YWseViDyorN6DTydx2pUwJWF2KIlcsleOYwoV80K5ivJrHvEtVoNdUsYrKNjN1SasFVfpt7a3GFgQnDSO0aJXGzjoZtuApsWkybCpLxHCs8rvH__ZTmvA2b8Nchoopr06m40jqd65LfOGvTs2p7QwMfTdrt3UYE0q4bK3ALtIa5BZT_nvBZF7v8wrs6CFv4gv1cDZqPeRP7XJedwKgLJdMjGDMaq6MXxi6z_bbw1QJ-V9nVy_DuLgIK3rTdJbRkRvi8GK79EGFwbSXmRPV7beYeB6BrpeVvBxW6NZS8PfS_cNoGnTz4Qswb7PPYpFhFHVhusFl2rvW_A6DVb22hNKnmIxINb2YIjdL_En38kOD_pegNqTvImobkeuN4kPn2rOUy31kba8RlGI8fuA-q2GK55aMl4wq7YNg5JJDZhQsdX-1qIGPl266-_hEbho1E4DC9sIfXwZQpdwOpYqX02ha-Ev9YVis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e541eb115f.mp4?token=kNl8VyPU7FVjGngmcW-wtA40dSCAiVhLdUg9uzJyN6W7KPeDMqwyK4zX7rrep1ITz1gYFcuf22bkZLFcp2Y94-ZHwAfyRs35O2_bEQjadUNjRaSUWyMdni9_fCbfVK7-GkLkQJHvvDaR318rDyJYE_gRoFwUSdO-oMMWB7BDWrmcYUN7OhZpRDMhleHt49KLX3fN_8ghx0_q3YWseViDyorN6DTydx2pUwJWF2KIlcsleOYwoV80K5ivJrHvEtVoNdUsYrKNjN1SasFVfpt7a3GFgQnDSO0aJXGzjoZtuApsWkybCpLxHCs8rvH__ZTmvA2b8Nchoopr06m40jqd65LfOGvTs2p7QwMfTdrt3UYE0q4bK3ALtIa5BZT_nvBZF7v8wrs6CFv4gv1cDZqPeRP7XJedwKgLJdMjGDMaq6MXxi6z_bbw1QJ-V9nVy_DuLgIK3rTdJbRkRvi8GK79EGFwbSXmRPV7beYeB6BrpeVvBxW6NZS8PfS_cNoGnTz4Qswb7PPYpFhFHVhusFl2rvW_A6DVb22hNKnmIxINb2YIjdL_En38kOD_pegNqTvImobkeuN4kPn2rOUy31kba8RlGI8fuA-q2GK55aMl4wq7YNg5JJDZhQsdX-1qIGPl266-_hEbho1E4DC9sIfXwZQpdwOpYqX02ha-Ev9YVis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های فیروز کریمی سرمربی سابق پاس و آبی‌ها درباره‌ اون‌ویدیو معروفی‌که ازش بیرون اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23936" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23935">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXir4Tdg84lYWO-8hVC528Q3DoVrOTNo3_tIHFgHLDCP0UkOBft6VklnuqzflM5BrTjvjNGImd9E1S5sQL7vz1aLYbxh3_ouo2NtXG2X1UZOKkH4hHhmSVMhO9HgAGkHcqfx_ik2J-uQzrcBcrddN5QSdxGBmSGdP2eDkTTcKvovDYyfRjC9Pj_viNEFO3fc7PiCRvZXsmOFM1Ym4-WicJDSr7WFKpgNF93ZTp2vMjEQzexMpZl8KIZK788elAs76vMPMrZP_8ipONI_N5OBlJJq7MW_W4801pzfHhS51n_-X44oGO0Tx00Eh9SAO4mSdkBG9Sx02M_wiBsP0lnAvw.jpg" alt="photo" loading="lazy"/></div>
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
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23935" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23934">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23934" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23933">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJAftfsek8qyM61wD4YEVG_0traQYCQ46Qo_1A3qZfV7Q6W1vNoxtjUmeMt60Cz5G1zouR5RE5vh1NDv4Y5oi5ht8aPGY4mIaQpAh-QWpS_LIY79qYztvm1xAOfi0_hvYuDqhvAsZcrbljbXLQRknfUdWKItaBehmUQIwsjjyvSrASBIlCFC0dWDseEnX5KTtP0FMkUT1iQIEKM6OxbncQXOZNuLB9CNjS1PZtkZ2Q-i56YcGt3D22TGPVshLErauHA68kURCHGyiyMVq1Ur9U98veCWK92XUEgfyaRa7TdA1dsIp1MCLzucvxGpjUCz4AG3I1iCH2ytcRJnt3tDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23933" target="_blank">📅 22:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23931">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E2-Ci10QdH7FXc9mOly8_vg-s5tZgeFUftm-Zv_dsPzIjmjPczAvhtDG-xCehh4XRydNS9R_v9K1XYyuwHuA1EJy9HJ5WfixkEgIeHzFbvSfWjYvjrOWZrpqAOB4x9JHKsXnj81d5v25EXsAiYrOWT4JeYi7NsXUszMhL7_zm7pqY8Fu7wf1t5XdA1uFvj0nhnxY7kDq_sBLL4Y_thsoTLH2noAQKIXOuTPsDwz4G18fFy_Qc56b5UwlwqpRNWFSyXXCdA13bfX8yV21q3X6tDz9cGTAkk7o9Kh-yg10wXX9cMrSeJ8ePQ1KKec79OXNIIYoyAdWBTGQYDh4omL55A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DaD9BPwglYKHkp6Uh7MCFuljvNNM-mA1rLE5Uf5SYGNqSSRpSI2LJiV_nFinhSJSWVW0s6xiznOOi331HuWhdTifcfS6BX9V2QTTYYN20YH58xh9zXHdeSuMBhPr7zJborh40VXNnllSNbhummWWyaOo64CQnUIA5c32uQTP9PSX17nn0UePtkP3XCFyQuQtgrzZ-A1j0JpDpvJm8AyATEpMGUFvdDRRwi6EI31C4XuNSDSQ8aV4-mo3zv-XAKcAUBEXg8x68nM5lBiICAWS-WgW4mWyajdlKvW6Aa7vGSv6Ye6BAxGhVwJcM54a5-rM6YROw15QrtZe3D3GJNDhMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026
؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23931" target="_blank">📅 22:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23930">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Em2J3F9kDheM1q45J3Gr734qz0tI66N_Q_CSswk6fMNY7waZQp2CI3-aM16nfHlUGHU5DOPrSue6Q1uqBG3WneiEjtdcBtDmTf3CX-AejX8BxhQFVMvl9bptOFaX1_X-zr_oGy7BxSe7ENY78mo0Zpmoxfb7RhxJswNxSgC3aYWqgGX0afpdFPZbanHyYMe24_bzi2W1RGWULD8O0MXWSn73SLJr3tFQLAnnKlV3GNFULHxW854x8m0Qmab5JjBUANz_UP8jbMfB_8qjwWLx1F9yN8EcUp2hSIpeI-ku1MNvxSgNJQyu1bh9BYhcQQA7pTccVJc2vqCsNvOW1yU3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23930" target="_blank">📅 22:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23929">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3537466720.mp4?token=MJgTh4G94WTy4WZbS1rf_9gfaoozlqjBnHT9VT_x3KAWUZeFC7GfZU-1ghFjCkQoNAus8X9tE3UvYS8MjMudRBaOr3NDSdXYhHPysFy1httR9aJykJL8a4QOFHyy44q93PjUEKULHpe0y2rxvFov0tDWIW8PPTNDQz8mYyHip3joRJZ6YeoM3Iiau92Ky25alhSlum0bzN3c2fFaGGwXSGnX_VW-QyypRmqYEXEKcNeBpCyI7JUJtNzNSskaSKCQ-LtENj0I36UmcMI2y3ijIULMr-BBVuknbbNMLp0S_znrV5Vhx9cvT69GeO8YzpXuxmuU1BEx9Xavg8jQ2NeXGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3537466720.mp4?token=MJgTh4G94WTy4WZbS1rf_9gfaoozlqjBnHT9VT_x3KAWUZeFC7GfZU-1ghFjCkQoNAus8X9tE3UvYS8MjMudRBaOr3NDSdXYhHPysFy1httR9aJykJL8a4QOFHyy44q93PjUEKULHpe0y2rxvFov0tDWIW8PPTNDQz8mYyHip3joRJZ6YeoM3Iiau92Ky25alhSlum0bzN3c2fFaGGwXSGnX_VW-QyypRmqYEXEKcNeBpCyI7JUJtNzNSskaSKCQ-LtENj0I36UmcMI2y3ijIULMr-BBVuknbbNMLp0S_znrV5Vhx9cvT69GeO8YzpXuxmuU1BEx9Xavg8jQ2NeXGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سعید دقیقی امشب‌ مهمون‌برنامه عادل بود بنده خدا داشت‌راجب‌برادراش‌میگفت‌عادل برگشته میگه خودتم سفید مفیدی؛ عالی بود ببینید
😂
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23929" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23928">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=KlLnSxhFuI0nXmmUCnlF2jdGcBmG99UthOkaGQ6GcK6SZA7vcEOMmHas0lUxDNMp1-C9xUa3d5196oBZthJQ26JOsKAiD3V0WVHL5j0Sw3gqAjpq0VGwK69EIXhi1MqHirPEvyXDs74fHT7aLCz9qUmEWGXGPDgqjrdwyQIP343Sa14YQfuZBLMGyDmLeZhbBRfe9ZiPQWOLxjo9Zz1eMXs9jrEGVFec-IAodUONJYlzyhJyuD22V_9wLMsbh-ZJXWrS_4O6nZPlbOI8UALhhyh1ZcO2Z93MPq4xELCu-WRdI7PMa9Vy2xhjP7WVtjbh-N2H9ekK3DJTSWLPDrLf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=KlLnSxhFuI0nXmmUCnlF2jdGcBmG99UthOkaGQ6GcK6SZA7vcEOMmHas0lUxDNMp1-C9xUa3d5196oBZthJQ26JOsKAiD3V0WVHL5j0Sw3gqAjpq0VGwK69EIXhi1MqHirPEvyXDs74fHT7aLCz9qUmEWGXGPDgqjrdwyQIP343Sa14YQfuZBLMGyDmLeZhbBRfe9ZiPQWOLxjo9Zz1eMXs9jrEGVFec-IAodUONJYlzyhJyuD22V_9wLMsbh-ZJXWrS_4O6nZPlbOI8UALhhyh1ZcO2Z93MPq4xELCu-WRdI7PMa9Vy2xhjP7WVtjbh-N2H9ekK3DJTSWLPDrLf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
این بخش از گفتگو دیشب عادل و اوسمار ویرا تامل برانگیزه؛ زندگی‌سخت و تلخ اوسمار در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23928" target="_blank">📅 21:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23927">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇳🇴
هوادارای‌نروژ وتشویق‌وایکینگی‌شون‌کف آمریکا؛ چه عشق و حالی‌میکنن، چه تابستونی رو میگذرونن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23927" target="_blank">📅 21:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23926">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTbNlf93GsEdhe1E05T-xOvqBiTZhP2zMkPgqWAlt62--uSKsQlawnzkgnavWgQNh_n99qqr-GMzKIfiF4bOVQvLIYpIf2Mr0IPiqQ4GyzXtGKd4_uote1FkqtM2Ls9ZOgc3nFwONAn02qam8bj1FL9fQx0WI3b2ZhjEGn_3FMPEcxidHd9QbD1RJ08PlCG4mLgPAVKXSzjrrlg6TT-GjRw8CXXf74KVNRrsjE6S6SDzrxWS9DOEG14hA5mJ9hV-mHoN4k8OrhnRSYwWbJk4Pe9O4ojqSf-sSID7xMA-bZlt33At6Rgbs51tBaA7HuGqQTP_cOBEqu5ZapUyE5ejhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛دقایقی‌قبل با یکی ازمسئولان‌باشگاه‌پرسپولیس ارتباط گرفتیم که ایشان اعلام‌ کرد بزودی قرارداد اوسمار ویرا با باشگاه فسخ خواهد شد و او فصل بعد درپرسپولیس نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23926" target="_blank">📅 21:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23925">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwavZm3Xtqk8Rn37bM7I5G-6Zi5fESNHB8k1dDUYKoh0PRU2btbserOeojxLff59mG95pPV-N00jPUeGZW9zX10Gqmlp791w-7wSjD3t6Vpc80ojHfDpJX2VdRGc9bOPchrQ3APybJlrQ59uRKuzsg1b_sS5Blh3vn2up797M11pBpn0FdRucYhYwkCxXszHG67ZGNylkZS65CAEPDW-sqL0CMzYFVSQot31KxZCVWyBuJIae_2X6vtkt8FJ2KjTcbI5ui48IvxoeqeKuz1utxYRyn11yIxp1THKEU2YjnCW9c4EkVo_prlPUFvg5qJSgF60zJ9R0f5dxLETyjRITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇹🇷
تیم‌ملی فوتبال ترکیه با ترکیب 300 میلیون یورویی و لژیونرای مطرح بادوباخت بدون گل مقابل استرالیا و پاراگوئه از جام جهانی 2026 حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23925" target="_blank">📅 21:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23924">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
محمدجواد حسین‌نژاد ستاره سابق سپاهان: من خیلی میتونستم به‌تیم‌ملی کمک کنم و خیلی ناراحتم که در جام جهانی حضور ندارم.از لیگ ایران پیشنهاد دارم و احتمالا برای فصل پیش رو برگردم ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23924" target="_blank">📅 20:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23923">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1Qq5b2cAIlS3Fm3xsoUxrK-FLlJnr17ns5J7csDipGP3boV3Pfy8vSqoG29E2jKy8gY0xHTV3GAH2C06Pw7F5k8ZE_0KrkzUB-guQBoQHI52isrQf8XmAaUaZhKeNs-fMkENFE-4cyKvUaodAOJm8ba_cwJi_esfBjDZk2VzxK2QjkmzgS02ghXNVIJmzNHJUyrO6voM9nJ58Ip5FJKcw3Hcd459r06jhzTy1JQ2chfeLvrp7cA_28d6c-zdZzPwUjuR2psy5UXsuDYZ8EnJ7ouldD8rRpj0fFvxfFuTB73HtIzleCuPFTU7wuy1lBRdILd3hApuFSpvJsN5D6Dxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23923" target="_blank">📅 20:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23922">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=s-TQVTGw9ahmBE78YqT67zp2-UltMFDjyctpEpWb1HnTgUxgYNYkd9PETO3XzZBwFRl0sMXt7WE6PJbr-FkOCuTM4ARvOF8royifFLh0Grl3CU7Wx_CBzg-K7AoETL5yto67Bxhog6MFHQ-UqPklfYFRBHr3GMZ35D_CGXwWv77MBrHZ12oiv0hWepZX42d885CneLs6ZTyfwdMEwCQcdejiBv6X9XeAmQKGGBhUMXhsMCFmlFcQzkCoP-GYVNGjkPto3cZpf8LgII24WH60HVieO_hUAUg8cukqA8B8LzhrlmTFKXC3bS0ZPRQ7vfmHXn24OASxOdI4xcVJi7LHBIUiAZFiU7zvjPspaIdFVwlRKW68uPPnOMisSAQ0r1P5K6mZTmfh7mkMcM-aP9-S0XgAp8iSXaJS_icD03Q9oXyxITFco6gQ3DSIGp3mxwUNdm7tF_Y_y-aHLpX-IM1GajVKg9Y3QznYsasDvEIzQE9hJK_OSw4gYkRp12yYekA0ZloP6sgWpgM_9bKQZlaZpCWDBpr93NV21_r7PxE9pS5iFhdRiUwrMV0Ht-pLareubOQISHliZdfzy4x_K5LEkjGtY9MQ88_p8D7629risXbHM4j6EqesQC-rxq0TjDWtgvnwN-ZpWU71dJHrLZZDxnWprKuSR1-okyLi9OhXLVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=s-TQVTGw9ahmBE78YqT67zp2-UltMFDjyctpEpWb1HnTgUxgYNYkd9PETO3XzZBwFRl0sMXt7WE6PJbr-FkOCuTM4ARvOF8royifFLh0Grl3CU7Wx_CBzg-K7AoETL5yto67Bxhog6MFHQ-UqPklfYFRBHr3GMZ35D_CGXwWv77MBrHZ12oiv0hWepZX42d885CneLs6ZTyfwdMEwCQcdejiBv6X9XeAmQKGGBhUMXhsMCFmlFcQzkCoP-GYVNGjkPto3cZpf8LgII24WH60HVieO_hUAUg8cukqA8B8LzhrlmTFKXC3bS0ZPRQ7vfmHXn24OASxOdI4xcVJi7LHBIUiAZFiU7zvjPspaIdFVwlRKW68uPPnOMisSAQ0r1P5K6mZTmfh7mkMcM-aP9-S0XgAp8iSXaJS_icD03Q9oXyxITFco6gQ3DSIGp3mxwUNdm7tF_Y_y-aHLpX-IM1GajVKg9Y3QznYsasDvEIzQE9hJK_OSw4gYkRp12yYekA0ZloP6sgWpgM_9bKQZlaZpCWDBpr93NV21_r7PxE9pS5iFhdRiUwrMV0Ht-pLareubOQISHliZdfzy4x_K5LEkjGtY9MQ88_p8D7629risXbHM4j6EqesQC-rxq0TjDWtgvnwN-ZpWU71dJHrLZZDxnWprKuSR1-okyLi9OhXLVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
‏یسری‌از آمریکایی‌هاازهمچین‌جایی‌شاهد گل دوم تیمشون مقابل استرالیا درهفته‌دوم‌جام جهانی بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23922" target="_blank">📅 19:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23921">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDZna6Qz9O_0N3Jzv_kKnArvZ1dw6lhEKZCq6JT0qmJp6HXNAEX-XZ3V7qPrSg007R01gJJ6464i53T9WHV9vqUGA_0KAiSc_ft95rsTydyxeikBey7_BnaQfcy5HUwrJ5Qg_9o3N75eiR6JG7cq95QzqCIwgDHieCp-p7hfkWR5wIhLFbMqk9hfsBFmVG4Xdfou7pPg6hGH6TIqfNh8Q-dRbtUBeo0oMo4lcXLDm8xiPDxT2PGEpoRVh-IscXRM4zZQy-LFnys2TlUnFdwOShvPIfhr3JoQM5rHqh5Xw49WmYar5OzGQcovvqEmoM-HoxsfhOTTrduk6aY0tiv2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟢
طبق شنیده‌های رسانه پرشیانا؛
سید مهدی رحمتی در روزهای اخیر مذاکراتی با مدیران باشگاه پیکان و ذوب آهن داشته و احتمال اینکه با یکی از این‌دو باشگاه قرارداد امضا کنه بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23921" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23919">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmVfX7qzyhMBwS6S6zbP4rh1UWMALyjf9L3zQbdd3ZkG7btjk1_ApA9lMqPMldz3ZuRPU8GndOaNwvM1kZqHG7kPq4rSL-GMBTLzbmavXiL1FKXpm3RhcLeI4o8vwx2ldTTCZ_GsUUMpcqSSr_1Oo0_nER5xpExlRx2OZjmnyvqWUSSncoiVv2ZUK1J0aVAQfXAIgKDhWc_vmmomFG6d2skRYaN8UbsEq5-c9OzAk6X4vqMHY_k2o2N34sRRqAzo9rUsxbZdvpYnOZuKJ7duAxYcD8TdjHjo4A1--mWaW4IR-ZU-JTUbIscnRFcdMF8PY-1w-RK4WCoZCoDk-9e-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaChM3oE0oC3-vD-ZHV-yBGZMrOlDbXpm8aGhq64Ikfkk5PMRksxeiQHVdgURdvIPTWio4_bfYlBGtrR9OlxzdpA_LqajUtCHL2UJUWV8gLa2OUxRtf6mrNBNezbZyOXUHsGAIuoq6nT7TI7zRaFjI5hK1zX7WbY6PEQy6PlX35r70taL8bL-i3DtuVUrtsxKoDRRgKDlCxPoOmweZzmLjp11ibNn9crOM69sGfkDEmDEJhLWEIYd2iEfNN51-BWkMouys7hHRhOjH0CKtPXmLjbSLBdH8VI9ha8AV87RU9Ozg-fLySGz8LPHR9dWotWDHCuJDVIYm_dxbkxpT8T0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23919" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23918">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413165ef88.mp4?token=IILgRH-O_VAalXvxpyzqeMG6vVHf2_wrcHaCTi2jpx4g7PFjwyZdDFqnmpDs10U_KRfhdvk2Z4lWbb9WzMs-_bESg7WMJ-soM5FiYyzFWYedFmXZk7kO07Z4PPPk-WF3y8dRoDSlmCN3yXJLccz9Y6EJcewZXI92UH51AUl8EJsjAlfqV-hDCwNRYXDeMcOUifvTTlk7Z7HHtriJfxPv8XdicOOmwkZ6EARyyVf5l4gC-oPVzmdddRGB9sliVGOfzwWvDTh6mOav3-WrDBnyeIlADNu2hzA4NJqD412PNsEnwnhllYqBb71LyXzDwnt2JveO6FJcfP07M-omHSytzB3IDm61SiG0dx5-WDeBavrADv8RYACvLE8IddQEhktW_7YbaoqdL0BT9Uurr1H6GzibTxlpOXTYxy0mwAgAyO69pFFO_-70vTrBLKl_sTnoQFcZUp0xQlaF3awZZuFlORLRvW6bor43ainLL2MdBYIJhuxOyBZZjusZdUIrQjAWfH-l0_8CmnrhpvAI4JbhHfVA40y8EKv3Je7nsCPeP52Egm4Wey0PqWlyl1dQ2zrJAhHO73kcbV8yiNC2fpCbj-RIXDt7GeYTYBA9Eidc6BTm6RfrPEtsMhQTHZhoSvlPvuDtYxCijIuER_2rxqrhzEsssyMJ_bTiveM-ygK6xK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413165ef88.mp4?token=IILgRH-O_VAalXvxpyzqeMG6vVHf2_wrcHaCTi2jpx4g7PFjwyZdDFqnmpDs10U_KRfhdvk2Z4lWbb9WzMs-_bESg7WMJ-soM5FiYyzFWYedFmXZk7kO07Z4PPPk-WF3y8dRoDSlmCN3yXJLccz9Y6EJcewZXI92UH51AUl8EJsjAlfqV-hDCwNRYXDeMcOUifvTTlk7Z7HHtriJfxPv8XdicOOmwkZ6EARyyVf5l4gC-oPVzmdddRGB9sliVGOfzwWvDTh6mOav3-WrDBnyeIlADNu2hzA4NJqD412PNsEnwnhllYqBb71LyXzDwnt2JveO6FJcfP07M-omHSytzB3IDm61SiG0dx5-WDeBavrADv8RYACvLE8IddQEhktW_7YbaoqdL0BT9Uurr1H6GzibTxlpOXTYxy0mwAgAyO69pFFO_-70vTrBLKl_sTnoQFcZUp0xQlaF3awZZuFlORLRvW6bor43ainLL2MdBYIJhuxOyBZZjusZdUIrQjAWfH-l0_8CmnrhpvAI4JbhHfVA40y8EKv3Je7nsCPeP52Egm4Wey0PqWlyl1dQ2zrJAhHO73kcbV8yiNC2fpCbj-RIXDt7GeYTYBA9Eidc6BTm6RfrPEtsMhQTHZhoSvlPvuDtYxCijIuER_2rxqrhzEsssyMJ_bTiveM-ygK6xK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی کنیم از این صحبت‌های علی دایی عزیز اسطوره مردم ایران درباره رونالدو اسطوره جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23918" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23916">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmWqOBZFroneIVmhEdif7Kteu5VsNNa7v4JXFtOtMREokRAf0u8ACqUFjlkWmmlTMRdqr7eiRNlWXRi1k7qypW0d5cIffZUkotHI5hITGgBxr3WERomYXS4Fdi5vKcD3w-4ulXmN-gUcqI-y--BwWzo3iwxSlcOAxf31d2ZW6V7NceRkNXawMPW4fTn67xY7j-O15bLjBw_KZndYe0-7S8PM2wIPTdndM0fbW4CZT6sctvi2v2BKFDUDdJx3ompXfdEjvUCirI9ZDJUnVgtJGpSzZToTEKXOyaVGiN9oXh5uo4ZGa08fPDmT7kAZV2PijOZlzPl6cjcsHxwN656vtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک: تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23916" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23915">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVK23VkdbDXlt3GmeZ2w3dFn_f2Vb8-DKyW7_j0udA7b_LSVjEBeYmBGAcHMVAB45yCJ3cpct7IcCq3GGBtqTog6EYGECkdCDQljR8UVKzLo5TljqcHWkmi1nCi_Om9NFdi4cpeT0oE16apBHjoHnw80kKo5VfM5PUtxbmht1WxUqnmY9gvx1oLs8x3BoYzArqVohcxiGaUxmKqQhfuRbkWhxte421RgktyYMG6e4NH093OjmhKlAyino2ewGVIhOqvSWvnbkoLtdX-nIRufcjv5TQ96HM2G0XHbMLayTMftamfDdGghZYLoeXIwEkKb3gG1zWfE5ESwBRHe1r62Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیش‌بینی اپتا از نتیجه بازی ایران و بلژیک
‼️
سایت‌اپتابراساس۱۰۰۰۰شبیه‌سازی‌نتیجه‌بازی ایران - بلژیک را پیش‌بینی‌کرده که درآن شانس برد شاگردان قلعه نویی ۱۵.۱ درصد است.  در این پیش‌بینی شانس برد بلژیک ۶۶ درصد و تساوی ۱۸.۹ درصد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23915" target="_blank">📅 18:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23913">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=vD3UNeaKlR-LCu_hU7mQ9XjEOGdEPjwKFxxIk3CowbTUd2PpR6yrFnCfjOXRnG9MstJeOj3dRHvPd3szo3SVfwVpGzYMosWF-nRGDGPv3rYiFQQu2LBMa3r3i_6rrdfClEzpr3W7kR2yBTAMah74PUPZ31yt-25fRkft_YZgdBXu9H04Us1zypG4wihZpcUyRrtZdvClPca4jVTesJLdi0RUOugFykUUXVbSYKfnTIg4urmPTDdW8FhPKcyniCbQ4USZAu-5hW73HZUu41kXzNNwCuKKCh7bKKR5vO748-DV3-u3xmtSN_cDXHNP_pkZJfUjzuJMWGPV1OeYJF6_-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=vD3UNeaKlR-LCu_hU7mQ9XjEOGdEPjwKFxxIk3CowbTUd2PpR6yrFnCfjOXRnG9MstJeOj3dRHvPd3szo3SVfwVpGzYMosWF-nRGDGPv3rYiFQQu2LBMa3r3i_6rrdfClEzpr3W7kR2yBTAMah74PUPZ31yt-25fRkft_YZgdBXu9H04Us1zypG4wihZpcUyRrtZdvClPca4jVTesJLdi0RUOugFykUUXVbSYKfnTIg4urmPTDdW8FhPKcyniCbQ4USZAu-5hW73HZUu41kXzNNwCuKKCh7bKKR5vO748-DV3-u3xmtSN_cDXHNP_pkZJfUjzuJMWGPV1OeYJF6_-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخراج‌المیرون‌ بخاطرتوهین به ترک‌ها:
آلمیرون بازیکن پاراگوئه به‌دلیل توهین‌قومی به بازیکن ترکیه اخراج شد! تو قانون‌ جدید اگر دست‌جلوی‌دهان بیاد و مشکل پیش‌بیاد بازیکن اخراج خواهد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23913" target="_blank">📅 16:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23912">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=h6rUsVne7bNjP1Dx-thX61eIkLe6ZNgTnWEeEesw3EFqxpvjr_T8l86pvNgysvQ-7sj0xgaiZr2eCDwZ1hW72O-6cx3cwutbziXQ1jfmoEItT4FkXvltWHaJrLs-OOeu6NeU7MmRbT1qrp_LeF-_g39dKNeZw1qeiCuhOWsf-dHTo3uVmTsonD4EaLtAbHCC6t2QDubcsZ0b0DWAWPv5EQ5zzKVMAyPH7rBPzEPHzCN9Jx6LAv3L_iHIRBLcW0CjqVRiWco8hdKKuk7KtzuGj_MaNjVRevDaFJ8qdosxcOnT98W5xVhHdVybg05H6Zz_xfHYTe5UOsIbFVdLmvS_Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=h6rUsVne7bNjP1Dx-thX61eIkLe6ZNgTnWEeEesw3EFqxpvjr_T8l86pvNgysvQ-7sj0xgaiZr2eCDwZ1hW72O-6cx3cwutbziXQ1jfmoEItT4FkXvltWHaJrLs-OOeu6NeU7MmRbT1qrp_LeF-_g39dKNeZw1qeiCuhOWsf-dHTo3uVmTsonD4EaLtAbHCC6t2QDubcsZ0b0DWAWPv5EQ5zzKVMAyPH7rBPzEPHzCN9Jx6LAv3L_iHIRBLcW0CjqVRiWco8hdKKuk7KtzuGj_MaNjVRevDaFJ8qdosxcOnT98W5xVhHdVybg05H6Zz_xfHYTe5UOsIbFVdLmvS_Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گرفتگی یهویی عضلات پای عادل در ویژه برنامه پریشب جام جهانی؛ سه تایی غش کردند از خنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23912" target="_blank">📅 16:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23911">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PS_rVug5Znid3YaMz4EKjVGwDbNM9I-WG2R7f-2fVfQO58RAPIH5UQ-wN2wkbRIe5ubyUo1-XKUBmiarv0EJuW9LjRfwtzq1Y3H6dRKQVFC-QNsk2k1WIadmL8Rn7XDtdo-bRVSUmfw3Zw-l80MHBBQ0w-QSVf0TdtNvIeDGUI-wCoykdOoAyPFnTny2TvZ_OIUJcHF2gx6VonJ0t4zXcFunSQLl4Gib2YG0-2WPPV0ZYBQ3VrgBkYsZUOgH26QIx9tLNbWB2HdssglJh9_W0ibIrCwYSElecAS2YP_HPYHDMl2154EwiJP7CJgqKQTDjlvmuF4bSD4IcdxjYidSkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23911" target="_blank">📅 15:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23910">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLxa4iEGD08MZPvyIW98AKsA7bAO9NScgtjuTb6WK4XWV6I42vrCzw9hpmb8b35Upy8OWCoCfUv23fLj2oRboLtq6NdgRWi1YB5AxWrEU2mGTcgYp6WVtKlLLaqXKUnXOtVjKdBQ2EfG3TqT1ryMt1JtMV48IyUJtiIQhvyuMLsBFz6lWHUe_AHwtI3OmnYIIo4XVJyQGoNDD41a0ocz0kKQ38qpJDJe60leLKjHuOEJREXVjAOdDVTmiZgnRijO1bMmLYI5_SvVV45rwo1g05KIw5BxVuX6vswsetcrlTlzpWQv_rHtrKEFQK5CeF8U1vkGv2-zELPzD93qW_stIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23910" target="_blank">📅 15:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23908">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=IEyKUwXYMG6y-RjTBZZGIDerbLTxhZ-sbXvXJDLok914dsZ_UKw3H0_yd2E6ovXfhvPtwZJGwSDy0dE3VoSZvM-zhtr2B9TV1W0BYjFRYlNQ0sOa-BIvObwVjLdbPAP_MCB5Lc5pU-mK1fIvSm5pxkgAejbBtcy_SWmXeASiTU50xy-cuBn_tdwK1us_iBFMzj5KR3YQIbFbdgRl2SL8nstzPerDaus5zcU_zu9CLUF3JpqoMAPwlCzar91Q2iiVDaxblne8h-RIebh88-SUZFVyjX_z67R5hEtrghaULzutWU1Ea1n5fZshYmZNm_H-aUbE-kO8AoCg3U678pWDqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=IEyKUwXYMG6y-RjTBZZGIDerbLTxhZ-sbXvXJDLok914dsZ_UKw3H0_yd2E6ovXfhvPtwZJGwSDy0dE3VoSZvM-zhtr2B9TV1W0BYjFRYlNQ0sOa-BIvObwVjLdbPAP_MCB5Lc5pU-mK1fIvSm5pxkgAejbBtcy_SWmXeASiTU50xy-cuBn_tdwK1us_iBFMzj5KR3YQIbFbdgRl2SL8nstzPerDaus5zcU_zu9CLUF3JpqoMAPwlCzar91Q2iiVDaxblne8h-RIebh88-SUZFVyjX_z67R5hEtrghaULzutWU1Ea1n5fZshYmZNm_H-aUbE-kO8AoCg3U678pWDqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ لحظه ماچ کردن خبرنگار کره‌ای توسط یه‌خبرنگارمکزیکی؛ حالا خبرنگاره اگه ایرانی میبود تا از خانومه لب نمیگرفت ول نمیکرد! این خجالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23908" target="_blank">📅 15:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23907">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvgF6hUfyyhVMRjxNDeBjvHaMhoOgrRgwW-7Cb0ouHnUN2MHbShBWPAeMt-sg1ze1qTrsTZ1zCnrjLa_CxDmfKxTf7FihKtvlPskasYn-yPFRXXYlTDXUReM9kZ5tvyUJf2nk6ILU9a9kYqeoRK-BkjfwkFEqhCm5f9_xYNUTqEooN-BjAmJ6iwYZuqi-bBUiweGFcU9njbqTx_Zv5TaTPS009KZ6Fe_lA-St2hUY7ZlXryWK8j2-p81SNSLS1LGncvjBufcxso8NOw4GgWNt3lXnfLVd0FVuZAPW6Apg7n7HisCX0Ushz_pAIXNZoaI7KH9m_7q16KZ5_K2GpFW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23907" target="_blank">📅 15:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23906">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYQJ4jmf5o6xATPzD-cz0evp_kobmENWg6Pgpe1wcX8CGI-2ngjDweeRsiXHhhwI5aCUwYxJ1KAZLLt_BMSaMiKlssQM6ymmzbohjrHkP2g4stWHzxvsCwWICqHprD6QaXrBJf8uypbdAE_4QLO2UfuPHFMKm2VcrdkQA9Jf2p7LxNQJLMVlH5hIcsd0Xe0ZPg-WeABxOPKBQvwV4rYsTgKI9Ig0xr6lulW3E2TF385eLIYq8nBTW_HYrwDs1edTU5fJ3QM1pcOYLHTpIi03XScytFKwV7sQvpGZCD5XM4p80dIgKNpL6A0MFKsF4VgRzh8v_2XNbYijkb2JReSYNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23906" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23905">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rABMwarWe_lm02VwdZtTd7qJJias3qHurq4FJgBLmDvkCDBew5XqX1WNCwVnbsEjqE3LxWvHAJ4AcaXiHLtfG_UE6YgSzwGpUbWXJVsveFJL231Ol--855ZUOQSjOtduf1uD6kBKkxO59nHyiKTMGSaAKOYjJvJbq-F7hO1QCHqA2VBCcaC69g-yIP0GoAxU3DC9PrFZ12Gyk6wpEmIAinhqKL3x-KcvkuotHliCOgW9T0Q2Au8dcUXqCFhVsBqCR5IAS_1cWYYN7CInW48wLfavaynmzDIVaRG8voKu766wFvLzGkhirVDveTS2IRHmNVDOsNcawqQes_HHWd4jJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاسمیرو ستاره‌خط‌هافبک تیم‌ملی برزیل و سابق رئال‌مادرید و منچستریونایتد برای‌عقد قرار دادی دو ساله با باشگاه اینترمیامی به توافق نهایی رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23905" target="_blank">📅 15:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23904">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQNrvLD0dzw-CwlmhNQkj24Yqn9pzRnO4fogsFfZoH49_iIA-5RTQrIZqb1hRXIIkuOfaFuiOGeZj2NEoeym4Y-4dLO6EOtr8eoGQsJ-JZitv4uz2TIrmYSUwFa_6Hrp5E8DFrBugqLhd0ScLA3fye-IB1ndtwm_9GfGjWPjQMGfm4hRJs9gCo3UKjiI0TjcjKtqxl_W5x7LgZctpYwgtka0rK7rm5jFv3qNTm2meyG9a5uolDy8n9BO7JIl09W96At0mNojWItSWraX9b3xMS6M0o92pOGrN-qxubJ526aR9s1eowghiDg52MPqO7pvD6Ll5CjP3aDw-6L3HVR7Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویژه برنامه پیمان یوسفی برای جام جهانی بدلیل این که علی فتح الله زاده به میثاقی مجری سبکه سه تیکه انداخت متوقف شد و به او اعلام شده که دیگر حق ادامه تولید این برنامه رو نداره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23904" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23903">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=SLhrm0KqNw8B9XU5Dc-FBZhezgiPyRltMSaF9uN0yb71kf1G5c10S1xbW5IDwF1ClATALWTAlAwbhw4uT2LxnYhxcGOuMYIxFT2UyslFbqheWnjVWfo-pwI7ZKBjiS8Tdv4ti-79KEQQBk-kZtEt2W_vdMBbWoJUtAioQjC8V117oolRxrIotZgh6omre0HqsxBcu0RMY_DQikQxK0A6ulm9t8saDje-HHy59R7ErxUZQSp-TkXfHmvKN4N6Wl_Y9X1aszQhPmFGnBrQBhHdpMToz88vgIN4EIZinIoYbPg0gF34f-4UhcklCtWWMT7Kox_81FqE27fz3WkgjdOKbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=SLhrm0KqNw8B9XU5Dc-FBZhezgiPyRltMSaF9uN0yb71kf1G5c10S1xbW5IDwF1ClATALWTAlAwbhw4uT2LxnYhxcGOuMYIxFT2UyslFbqheWnjVWfo-pwI7ZKBjiS8Tdv4ti-79KEQQBk-kZtEt2W_vdMBbWoJUtAioQjC8V117oolRxrIotZgh6omre0HqsxBcu0RMY_DQikQxK0A6ulm9t8saDje-HHy59R7ErxUZQSp-TkXfHmvKN4N6Wl_Y9X1aszQhPmFGnBrQBhHdpMToz88vgIN4EIZinIoYbPg0gF34f-4UhcklCtWWMT7Kox_81FqE27fz3WkgjdOKbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی پور:
یه زمانی من و محرم خیلی بدمون ازهم میومد ولی الان من خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23903" target="_blank">📅 14:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23902">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNcaWYHnmc3JHbP7G7OR04-0UPPaG_v9L8SVRV0Wv9caTZJ0kmkiyVOpmDmT6TqrDfUVCp7jAjJ8lgwzmad3oX6oU0Ah_Tj1MJvQKY7_HMjkyp4trYx1RyQrEAgP0ci3XZ84D8JGEynfeRT-DpwFk4bSbZVZbn5yLO7OaPlLcWcTLYUHlkAIwgOth4ZMD8XbBysvTZ-5MHVqMxse_OfFkH2UdqG9nCVjgqU0NUC5PpirVR43epBCLwuBHKTrC2u1maIMqEtv3suxmI2jlZ2VXcG8jmhrM8CH6h5SMeGtulVUlj-fUVIGv9NEQWfe7gYOXoW3GMgNi4JBfwsyVUoddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23902" target="_blank">📅 14:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23901">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj3SWMbnIVEXFDjY3mYZf-z6QnPx7_09oLsOs9ZOSlQcYPYmv-95HP96vz0msmjM0TkYktV_lLVTyXsO0Tm2qMOuLTZO2R9iqc8AtxBxNQSs6SLsnmJwWpfy-sOJ7JAQWlpUJ4lIIB_pN-LJmQawmjjbelNHQaufC2xamnZzvoLTQaznhNeZWXSWmOC1tS4NPZHex_xduCPr388Dufsde4wZpoQIiCHJYX3C3MunAYGIjVq__9k3EOjG9tfOQOY9cMMONvM_GzNnDMJWichYrwnwagDBn3wOge6sM1Ds77qcEQjs73b_fjOEW5rC2iBevDDirjjRldFUHsjcLMu_Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
عملکردشاهکار ارلینگ‌هالند در لیگ‌ها و تورنمنت‌ هایی که تا امروز بازی کرده: 279 بازی و 260 گل!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23901" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23900">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCoSM2-LrVqfcUtBNj6CD8oyMymnqQzkaBS4e3HAVbAasbM4Ifvxb8B63RaD5JQTBRAnwWIuqtkGip5Kj7LVEFDVFhALzW-kQMqyqbpDR71XmA8fKmTYhpHVQ3-TmCuzXC5dhNr2bRWm9ttGtghFLfEyAFyd7zYupjGR-ib4TJAviSVsvakoLeHsH8V_mUB9atsE5QcqEwoYWWoAn51MjiEiuYEiSNXDkInVhkq2TQv5LPVnvkDfilVMBa4CB1RzQsCT5WGac4ucQjMNBH93RXKNuybJPDZLfAvmDKNqkPOjOaWJYhoX0wulLpJIaBIyQgZd3gdjmUrms_W2tpNPgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال؛ سهمیه خارجی باشگاه‌ های لیگ برتر درفصل جدید چهار عدد خواهد بود که یکیشون حتما باید آسیایی باشه. به این شکل 3+1.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23900" target="_blank">📅 13:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23899">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBZUGNRr9-kqKOOPuWWrL2mD4SFrh-D8VWPjicR3e62-YUrSY1eZJ0e1ckwM03CyVyTbrlKRtl1w83aqbhiN8x9PzGPhZ6Xv9PRRpDzUV2YPyL-XmC-y2TUYyVUoEYQwBr_bbOtcd4Qr4QRZsQzvRsGwz-_U8OK2RF4ZEnfZlE2Oc8xvwMXRkVqrAefZnZM4Ns-TTNmdfOW3XFpDdXb-SGVDR1OPzj6PWNc6ChhiayVKaTSzIbJLf5Jukr_bTYUiv6a_hwxOdy5tkInQEi1lDeCpzFmwbVqzch5w5M_JCB1Bm5wN1Bc2fSuWY-PQEa9XG5lXSoeNzb77vpV7f8BiSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23899" target="_blank">📅 13:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23898">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=LemLhAVmmnbPqgpieQ6ZLTrhFE6jCzG65Wtt2JICtreS4-FC9Cxdq-A3K3a4kiSt8laPbrpeUDfsj6J6lxZzZayAhDMZPTZIf79rzQRnrawFB3F3aAdsXmH7W0t8egFWIDLVAsvBFMI-Lvrjnk01sn3-0oiblqpZnG_kxldKK4170lgrzTKwp0KG0tQ0S_2LQ3c0uKNJ5F9b4uwUz_lEjivKJMCbqbizYKB5siK7a9_hG9ByY-4Tg5ClrywIkYQBtn4R-qaXhabGd6Bmwe6oCB_h3_xC2PlR22IlMH1EMbGMtFfKtMNZQ5jOqgsGgFrBt0N-ze-E7Iy1SzRrbL2SGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=LemLhAVmmnbPqgpieQ6ZLTrhFE6jCzG65Wtt2JICtreS4-FC9Cxdq-A3K3a4kiSt8laPbrpeUDfsj6J6lxZzZayAhDMZPTZIf79rzQRnrawFB3F3aAdsXmH7W0t8egFWIDLVAsvBFMI-Lvrjnk01sn3-0oiblqpZnG_kxldKK4170lgrzTKwp0KG0tQ0S_2LQ3c0uKNJ5F9b4uwUz_lEjivKJMCbqbizYKB5siK7a9_hG9ByY-4Tg5ClrywIkYQBtn4R-qaXhabGd6Bmwe6oCB_h3_xC2PlR22IlMH1EMbGMtFfKtMNZQ5jOqgsGgFrBt0N-ze-E7Iy1SzRrbL2SGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23898" target="_blank">📅 13:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23897">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=IZ_s9zXqen7gnEj7taSSyYQRvn8pcgMmTW5H4zTSVfw-oGePLTOnfjjKYyPdTs469QhCECyHaOfqQTwAsuzFY7CI6i2atMIohaFKw3W7NG9CNDzblN_4uXFN1GuOKk3aOaeSp2LhBe4suaHjIhu3qsb40En7zrhwpl7_UJgsw4xamizs_oRs6Ru1vAGIwiZwa1LrVsjAg0TwmOIabFDS57gwmC3Ot1pcqkGfOYFyCB6rZstviPCgjj7XyuMxP2V6jGh7ASwenPfS9MFwzhAtLA384jiDvdCpjAnAenfdW7Pw-REfHSy6RpZLbcDqhy07be-89gN9bjSg_cJvZ8UNEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=IZ_s9zXqen7gnEj7taSSyYQRvn8pcgMmTW5H4zTSVfw-oGePLTOnfjjKYyPdTs469QhCECyHaOfqQTwAsuzFY7CI6i2atMIohaFKw3W7NG9CNDzblN_4uXFN1GuOKk3aOaeSp2LhBe4suaHjIhu3qsb40En7zrhwpl7_UJgsw4xamizs_oRs6Ru1vAGIwiZwa1LrVsjAg0TwmOIabFDS57gwmC3Ot1pcqkGfOYFyCB6rZstviPCgjj7XyuMxP2V6jGh7ASwenPfS9MFwzhAtLA384jiDvdCpjAnAenfdW7Pw-REfHSy6RpZLbcDqhy07be-89gN9bjSg_cJvZ8UNEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی مهمون ویژه برنامه جام جهانی یه لحظه از دست جواد خیابانی عصبی شد پا شد زد تو سر خودش و نشست گفت من استعفا میدم.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23897" target="_blank">📅 13:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23896">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcjBB3s3skru9JaCJo31ms5OSccEHlBCqmm5ZL-XuaAh1jXkZmhBOOLKuw_9hatHk_nCYREmf6u6u0yzWk9rzi5vBaEYqh3orS5D6lDfZFuQsJhuLnz70rgmlKjx861FBkRPY4bwo_xwop72-X5cbD9mzHTPfW8yTY_4ObFcUr0teg_AuqRMCBl607J6lonDwCQzJ1LdNI6S9sCOe8eCL0nv54uiSVja3gm5_yllkGlXIyeDGYw045P1gYJTHz3ur5kWE7TwErYvq5937cHBiMra0Zp41DHFajqAPmv-cdhoPBJwLzrOAROgcxdYTnytPAV4Mqf_hu-egC0pcArYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23896" target="_blank">📅 12:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23895">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d19JjbTU2t4DvNPcKJyDc6Z7cVprscjXE5jhJh8XRey1JY1OD5r2fYD3s13E8iKyAkCXt-HivAFbfNE_EciWpa1pb7LxUb17m2F2V2H9Ic1BH7qbHb29CRTllblFdlC6YMyBSaXJlMQ92EmnDUp4sEc_VbEuPpmQlDpULmoqfMqv19UwUMjRxo3hkwAyEgoHZaJ784dn_wGkhmqV1sGa_H2NL7L_WYgTP1AoKgUnbKXt37CT0pmEabEIgXYZb38y4E_8zOakXP_ae_p-MeU_7Rc4aUZL-Lc7TkX4hiDjp1t9saG6KYyp3AomboMFMcmM1Ict4IDAxjaRycvG26CptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23895" target="_blank">📅 12:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23894">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=AwtHXHnIbp5ffZZ5G3bxMPrrH9Uyefn14VkE6nvXvx3g3yKCunIo9coBITnusnQKXWZvWzW9O5pTVf0vzQugQLvk2dcBf6nRKbA9ivVGiDDoIhHcZrj8vCjDSIcl3XkVVZMw3HuH8NiWpM3zh9B3AY2Wt8Nq32ow0FBCeIqp_vcOQt5HZ8a6B46CGQmuFWQ_55_uW6p9L8a_6aolHho-bcb9RJfwntQtDsaVQLCVj9Bf3A4Jbn6Fl4jcGOH0QbkEkZOd08BxWc8wMJl3jr1PDSd341L58vMeAu3swti8JknZVASPzMssT-VmQdbwUxkqGhj_nGk392hi7Xe7AlGdV4VXuwTf6RPQWCDYfVOfw4JTod7cLMofepG-6nRrE9X0MZlrk8zWj-ZAbZv-_NdtsO9XbIDZTR66tOPQEBNGrBUnRt9H1YJi2l4yGn_6PMhdFp65QBIUXn2hU6WEwX4RzfZkKNjrRCw4WHyMg64XAW9nbcZRssCYhg7hTkYC4ahCJS0-JWsTdi9tr2JpoUQVRhn_7GsCQP1bA3at8Ggi1l-8gDbMAbEDlHJjZHUWSN-KHtmfjz434SM6-U5pD3fSpxa3WqOSpDfG4aTmjcpJnNkO6s-7lCHCYllxw5ZC9PFXkShAi1sYfJw9yP0WUM7ENj-hxOKunQh_XiAxMeba6lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=AwtHXHnIbp5ffZZ5G3bxMPrrH9Uyefn14VkE6nvXvx3g3yKCunIo9coBITnusnQKXWZvWzW9O5pTVf0vzQugQLvk2dcBf6nRKbA9ivVGiDDoIhHcZrj8vCjDSIcl3XkVVZMw3HuH8NiWpM3zh9B3AY2Wt8Nq32ow0FBCeIqp_vcOQt5HZ8a6B46CGQmuFWQ_55_uW6p9L8a_6aolHho-bcb9RJfwntQtDsaVQLCVj9Bf3A4Jbn6Fl4jcGOH0QbkEkZOd08BxWc8wMJl3jr1PDSd341L58vMeAu3swti8JknZVASPzMssT-VmQdbwUxkqGhj_nGk392hi7Xe7AlGdV4VXuwTf6RPQWCDYfVOfw4JTod7cLMofepG-6nRrE9X0MZlrk8zWj-ZAbZv-_NdtsO9XbIDZTR66tOPQEBNGrBUnRt9H1YJi2l4yGn_6PMhdFp65QBIUXn2hU6WEwX4RzfZkKNjrRCw4WHyMg64XAW9nbcZRssCYhg7hTkYC4ahCJS0-JWsTdi9tr2JpoUQVRhn_7GsCQP1bA3at8Ggi1l-8gDbMAbEDlHJjZHUWSN-KHtmfjz434SM6-U5pD3fSpxa3WqOSpDfG4aTmjcpJnNkO6s-7lCHCYllxw5ZC9PFXkShAi1sYfJw9yP0WUM7ENj-hxOKunQh_XiAxMeba6lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
گلچینی از صحبت‌های جواد خیابانی در گفتگو با امیر حسین قیاسی؛ مجری برنامه هنگ کرد قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23894" target="_blank">📅 12:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23893">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZcqfiyCY5dUKz7DqFs7Qd_86YUlDkxKBEmnLN42e0pUKPgAZypNV_b15yUJzWxxFs3s95gR8pZvu_25NvWH9ck7NQ9cMG0uVxuD4LVDP1cmIZopyo1t7zie_FxtIQSaUfdUIx1tUJGgIRm-aQdujy9WPVfoNVTkxIw9hDw7Ie1_vf2LrHYDZ4UucdHFu7IPLkEJ57Xa23g9xV584MbW7L7tfuplJ_BAVBtcmpgvFbCd_77qRCXWGYdFU5UTk4ygPkjp9IrXB2JisxgD7MateYUMM2jdM32zXp1YP0cKAPU4MlBJHry43OoyrZe-er9jCLLtF0ZoNPqD1j8lLInfOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23893" target="_blank">📅 12:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23892">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuEsuusrW8ZNZWFD6JfMQyHareJtvbPGohNcMUZqE5-LpAJYcceUBBGyYmTjmHHAJkgsBBkcif3NQrwlsTbJriPfX8l24Ix9aihNCQoLJGiyEXpBiYNor62N-l4wwIH8zgdYGzyyXD9dKfhvweYYxZlWu7zMlciRNOVr1_5pitjGgUoy1RpLKWmJCKoEmL9Rdj-L9uVhlozGnyfY0F2EGALDFS_bjHB8u4ObKiqbitQyj9MJ_zLosj02PMSfKm583dEzmXJ4SUheydLghVhT0t5wDMxesl443rkTjf6yupP95KZJdzU3zEdrdeaDgLul3cQdRSftzH0JwEpvvSTUnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی پرشیانا؛ دراگان اسکوچیچ ظرف 72 ساااعت آینده به تهران خواهد آمد تا مذاکرات نهایی رو حضوری با مدیران باشگاه پرسپولیس داشته باشد. هیچ چیزی قطعی نشده. اوسمار 50 درصدشانس داره. اسکوم 50 درصد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23892" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23891">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=NVu8nF32FxRRH8uKnoFinwdOljuyYxlibZWlZGI8GV7Emc2FpywEXRWngSU5v5rX__Q5b2gU9KAs4D5uVAoUt51242FXBqC2ZSgHfpghi552Jsd1inTYxzC6T3PHOkyjWVwNZorNilB4ZBk1xQtaLa5S1UBdoY8LzExaIK1lRDUAanhfmPs9T43wBRCg2kBdAGsr2xxW3DT4br0O5hImeR5YD_1H8wKzcooX8olXfmuw-dgp-zL6eJiefVX4EryK2eaLohn8dTiM-3UYXdHvw5UiNcjHW-Q9xioWzIOb8HCZiO2ES9heXcbCEb-tNSeHyk5AKIbgGyDwSoIUddCzoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=NVu8nF32FxRRH8uKnoFinwdOljuyYxlibZWlZGI8GV7Emc2FpywEXRWngSU5v5rX__Q5b2gU9KAs4D5uVAoUt51242FXBqC2ZSgHfpghi552Jsd1inTYxzC6T3PHOkyjWVwNZorNilB4ZBk1xQtaLa5S1UBdoY8LzExaIK1lRDUAanhfmPs9T43wBRCg2kBdAGsr2xxW3DT4br0O5hImeR5YD_1H8wKzcooX8olXfmuw-dgp-zL6eJiefVX4EryK2eaLohn8dTiM-3UYXdHvw5UiNcjHW-Q9xioWzIOb8HCZiO2ES9heXcbCEb-tNSeHyk5AKIbgGyDwSoIUddCzoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
واکنش‌طرفداران تیم‌ملی فرانسه وقتی بعد چک کردن وار فکر کردن علیرضا فغانی براشون تو بازی مقابل تیم ملی سنگال پنالتی گرفته ولی...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23891" target="_blank">📅 11:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23890">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjIYdc2cLNUuJNS_8848EXUAtErAu8xKoQOREviCmEDQHzBwhWCL1YwcZfz6zBodrcSSWE7-BeAiCgEF9tgTaq_ajoZKU-EwJoARtfBhJL2wR4tx-MpOV77669q4GAFi2J6JFW0PNm5UWEi_zJQsfvtYQTiP8EiGTdx9rKjQuGc3pO8Q0P106cE_ggnjCSGuF09RDPrp4NXnwWzqGLz9WjbJYjngCXjayWwHjLGDBitPv0QALY2R3-TZjIn46eL4cVi1DpbiZkedSf5b9XFj6xHvRo3NA7-Jb-IW5rJEpmUgPYCvvGpoFj17OpWfUBpR_9JBziMYd2M0t2h22A7lVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌فابریزیورومانو؛نیمارجونیور ستاره برزیل که به دلیل مصدومیت دیدار با مراکش رو از دست داده بود حالا در حال ریکاوریه اما ‌کادر فنی نخواسته روش ریسک کنه و او رو برای دیدار مقابل تیم ملی هائیتی خط زده که به آمادگی کامل برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23890" target="_blank">📅 11:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23889">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=fACVYrh3pEKAFNU8DLsJZKpRqYRSxftAP56eZ-H1JrUUDOZa4yvhWtqdjnHbs-saIqs444RB7bHnuoqAv446Sj_r1bY-gVkKZIpflv4djPTTc1jct06HerLWk7skSllOxk_wIC4DLRc_26IbSHldOsBP2caS1wS65dVg6r7bP74EBTMV094u-Og-Yj7ZddC3RxGm0BIAZmgOuHD7gqbg6cLStwC4rTtIoDCTxcut4FmL9DNnfWwct2P38g2hv9Xfbpc5r9Nnt7A12yQrJFrR-iTW8LgDJ0LM4UDgN0ybda6_JB5CGtJ1s4wNxPwalwdbLmWkORidhcMTQ9ga59ITFgNQpwVwHEkM6KVmaDzNjCaHkk04ZOoE7ZUyef-CEynNhIJwYfY-wwconRqASXKeUhaKFUBlVLfu-IVmxUyLFWHc511Q1K18raL-oVIfM_dA1-X7U_mtMyyOr1F9_SePmx-dQDA_HoxgVoJ9C8zmu80itfKmBcls12UkRM0y3uCo0zp9fN5OIo8n68h7MPVu3PeO3IR2nqD9i9uEeg6luo5cc-wOn7d-6SiHoI4Od8GeXHIohXmlOyoSRC0XU1dCfNkiEXyvxFxVswx4PiHqMe7yjA5MVjCdv7XKBzg1rAQuQiI4Tx5y61pIXk61G871_f7i6R681gwDNJPd8sXzNtE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=fACVYrh3pEKAFNU8DLsJZKpRqYRSxftAP56eZ-H1JrUUDOZa4yvhWtqdjnHbs-saIqs444RB7bHnuoqAv446Sj_r1bY-gVkKZIpflv4djPTTc1jct06HerLWk7skSllOxk_wIC4DLRc_26IbSHldOsBP2caS1wS65dVg6r7bP74EBTMV094u-Og-Yj7ZddC3RxGm0BIAZmgOuHD7gqbg6cLStwC4rTtIoDCTxcut4FmL9DNnfWwct2P38g2hv9Xfbpc5r9Nnt7A12yQrJFrR-iTW8LgDJ0LM4UDgN0ybda6_JB5CGtJ1s4wNxPwalwdbLmWkORidhcMTQ9ga59ITFgNQpwVwHEkM6KVmaDzNjCaHkk04ZOoE7ZUyef-CEynNhIJwYfY-wwconRqASXKeUhaKFUBlVLfu-IVmxUyLFWHc511Q1K18raL-oVIfM_dA1-X7U_mtMyyOr1F9_SePmx-dQDA_HoxgVoJ9C8zmu80itfKmBcls12UkRM0y3uCo0zp9fN5OIo8n68h7MPVu3PeO3IR2nqD9i9uEeg6luo5cc-wOn7d-6SiHoI4Od8GeXHIohXmlOyoSRC0XU1dCfNkiEXyvxFxVswx4PiHqMe7yjA5MVjCdv7XKBzg1rAQuQiI4Tx5y61pIXk61G871_f7i6R681gwDNJPd8sXzNtE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تماس‌تلفنی امیرحسین‌قیاسی با «سردار آزمون» وسط برنامه بفرماییدجام: من ایـرانی الاصل هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23889" target="_blank">📅 11:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23888">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y16PaUkQxGNJj7xT9gg5rSBt_cK0sD-3g0YA7NsktELPqBa5201FLyQoPkBEW23gZP7ZD1Mq_pOAPGUeFuMzzxn554m27mVrPPm-RUwwzLS56QlFjHvkqRArCDLyRuCSwaz2iDaVOSQJPd7vMP-lVv86BkCwp8nI4I5ErfDlaodeFCd5I0ZtuxnHitk9SJ9JO7RxQZvJw5Zo_7-UJwSjvhyPBBsIdUy-OjIO8QKEg5UPtZ2uHtxgeoDXXFc3TOp0nhqq0fH1sK_470JyxkZRtRq_n9BBYlImupAdTz9cT0B_oqT4cZT1Fgnr8UiA23pXIRFy6BCFKqLO2JFQ5VkkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک:
تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23888" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23887">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55029334cb.mp4?token=qJ8jSRxQdO-fCX0k_SVvVm2Dy-LgtUylS46XeM_ws1F8Q5FpAECAi0aCniLGwsVAbhN6EAy_fH-0ozYootZNuYji2O7vi7LSI0NwnXajA0gtwHr5kcJ80U0i7EviNkxWxHlXHY3xzttOI6zX8DGDa5nE3Y60EIuzHGLITewFIXGrC06_xbr8fCgcwBypKG_rlenjMJ9YpVLjOeT6V2Bp8pVIb0q4nioGJMmXtyTcA5vYNsPeN7aUBoPgUdsvoDiCKVWZ8fL_JYHNMLwL8u4nDUl1TmbXm-JcBxAmrFKZY3KWMTr3XjN4ac1XLfWmRdZIZ5DTNDXEsl4yUoXNO9H-Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55029334cb.mp4?token=qJ8jSRxQdO-fCX0k_SVvVm2Dy-LgtUylS46XeM_ws1F8Q5FpAECAi0aCniLGwsVAbhN6EAy_fH-0ozYootZNuYji2O7vi7LSI0NwnXajA0gtwHr5kcJ80U0i7EviNkxWxHlXHY3xzttOI6zX8DGDa5nE3Y60EIuzHGLITewFIXGrC06_xbr8fCgcwBypKG_rlenjMJ9YpVLjOeT6V2Bp8pVIb0q4nioGJMmXtyTcA5vYNsPeN7aUBoPgUdsvoDiCKVWZ8fL_JYHNMLwL8u4nDUl1TmbXm-JcBxAmrFKZY3KWMTr3XjN4ac1XLfWmRdZIZ5DTNDXEsl4yUoXNO9H-Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#فکت
؛گل‌اول‌تیم‌قهرمان‌درجام‌جهانی در 3 دوره اخیر این رقابت از روی نقطه پنالتی به ثمر رسیده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23887" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23885">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9SUGBfTcCBaXTwy5m94h-ULVYQIy-dYpY2OPMFTaHSVhcNzf5eXpx37SD3VMgt_Vec3mnGrJmgzeRKFD9wh3Uh0-qbfZA9t7s1nSOgtXesf_Byonnj3DHBCUjw9lWVmA3tDnNQSP4KLEZSkLJyCPdJ-Cl_P92-1GVkqHguXZPc4fTA0HmVXG3m5d3PSjHhrRi-Z1UX7CxsMnihOJX1jcAWNKNCHzjR8gJHR6P0byaEXwbX5lfYkdlXGCN17XPqnzEKusze31AhmUYgKKWLoFldF3dia9iSVQJMgoLe4IxhUrKAeP_FwdJjUFQKJlyQHzKOsDSfVaWf-NdDdOl0jcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23885" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23884">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=s0dukf5GEHW8QxvSU896OcNZJgApTOYOzpkMTR1HHbCGkt_qrIQN83XhSzHf8TZ8kr-9m5__vQbhf-nRQCkvrQ1rApld3Uu3RWOYqNCFvGy2r2zgcYutx4kKfuqJH191DOd3dLWBnqtbHRX065KuhzxprwcHtw3cPSa571GqHtgiPtmDuu40QA8ruKFjmnB4GN6sDxFi39QZCZclQyAZRAstSY7NxZg1gkr8T3tCVCu1d6mySWf5GTzR9L537dM0fsg5v3TFDSDBoh1Y8yCSCry2G-d_tn6QzVwVYJVuwNcA8U7PsC7c9wT3QW5Rzpk5gwqtRksc77gVzf2zjTnIOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=s0dukf5GEHW8QxvSU896OcNZJgApTOYOzpkMTR1HHbCGkt_qrIQN83XhSzHf8TZ8kr-9m5__vQbhf-nRQCkvrQ1rApld3Uu3RWOYqNCFvGy2r2zgcYutx4kKfuqJH191DOd3dLWBnqtbHRX065KuhzxprwcHtw3cPSa571GqHtgiPtmDuu40QA8ruKFjmnB4GN6sDxFi39QZCZclQyAZRAstSY7NxZg1gkr8T3tCVCu1d6mySWf5GTzR9L537dM0fsg5v3TFDSDBoh1Y8yCSCry2G-d_tn6QzVwVYJVuwNcA8U7PsC7c9wT3QW5Rzpk5gwqtRksc77gVzf2zjTnIOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
بعضی حرفاوجملات هستن که ارزش داره روزی چند بار بشنوی؛ جمله‌ای که این داداشمون تو برنامه دیشب ابوطالب گفت واقعا باید با آب طلا نوشتش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23884" target="_blank">📅 09:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23883">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNvxc5hDpaMZKmGYDRnuniP3v54TNK6O7DZmjrEDbQaiiuQZaOum1CjUhw3HjGTe9KGcSsSn1JN9YgX81ZD9lUEPq57_kZwzNk5xfH9vcyAwNjaBp2G6sKrBroEwfk5kKGS53fTunvSYvs_4i23UM4FZCBi-MKSdX3Doby4XZXtZldBmL3IH3NGYi9MMoPAYoZ80AOBDUhcxhs3MYv7H0lt-2KQWWURBvUs57C3s06j7h6wSiCpswlJsIv60RVUGAqFD76hANbkfIbZUiNOHLU0YjJOuM-I9sXYGVgxRqjDYvkOsIuNexNN1okTIMgAOa24qV3QquuWZfEgFXQ8wNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یادی‌کنیم‌از واکنش‌کریس‌رونالدو وقتی مسی بعد از کوپا آمریکا 2016 از فوتبال‌ملی خدا حافظی کرد: دیدن مسی درحال‌گریه کردن واقعاً ناراحتم میکنه و امیدوارم به‌تیم‌ملی برگرده چون‌اونا بهش نیاز دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23883" target="_blank">📅 09:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23882">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mo26Lj_q0obTyc-mQiObSCLC9aPM-zsvOAMh2mdjq8cgthboHVFdC9mnKNDt1s8PlSDapQUlLc-tahW1c0VO3E75LCTFhBDw4oU6yai9AEE2lcKdcS9785s8RUvPVMqiw73GrHh-GNVKZlinSSu9fKWzA-yDhBJ7fnCytvlhyp_-gO44QEmto8OMnIGhlXTNWcQE9GNVB0qjL5xe_cKp7m5gGMaiBd0U8rX3ruUCbPNlXOIhsDMqjDw1lCPxeUqX5Jf66_5RT0jSPRkuZQk1ULur2AcfgY_Ho2JAoesbO4Av4mHAAagR8CnBSrQO0pU3VPqVmY74J_9WeoNsLoo27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23882" target="_blank">📅 09:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23880">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMu43X4Dk9k4C46pfo3E9JGp9xiE-D-E9bFkR7lwz7SWk1TQfpD2Z5UsKfelol0Xxdsx4NRm9-1J6kGhWzK2y8Peb4v_f9hOJz1206sOMplt6q-Xe7w_qwFIMF9u8wscH3mJM6aMKLbiWghKkwX4fxdBJxVt4HS2szCpAlCMxquoY04wMqMRLMJ-vDYgPVKT_BdPxrPqKgfIW9Yi-hzOptcA86eSmxUG4gmb3Ek5F9vjDjsoVyHTCTVG9ndwVhxF3N6T5-1ipbhunlQM7zw5IL-dFj0fy0EAICFfs2aVeon3s72PhLSN0EAY9u-zfEU7QYHlSQybskd03kMVr8YxPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دوم ایران در ادوار مختلف جام جهانی؛ پبروزی دو بد صفر شاگردان کی روش مقابل ولز بهترین نتیجه در هفته های دوم جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23880" target="_blank">📅 08:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23879">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23879" target="_blank">📅 08:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23878">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4xmiX89IJ5JafIIQfytnRFBR3OXZkv5HAwIRIrYysxc-vWI65q2TwGUcSjfknj0S1DFtRVA9J2rjadQ3ypXr9hIDBL6HydS3wSxPWCJCXj4uR4ZbZvHdNCnE9u4U-rHsehxI0nvW-5JuSEzzKa0VGYaDmpc7mWp4LeduGCZJVZoKcUA_fH4nQCcl1zwqXyocAfGhxcmG7wa1gRti0Enk3jJS0K8qYUkZ9mp_R6-rfHW7sw-hAH-zI4aQ5-A1Eo8btiHjFU2ATnwmPkuNToi4I0_JBaQ4iwWTELb7BFD5o7tUK9qVbFkhy4v-8rP0qDxTRJNgbY1SKi_fkWz0FL-PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/23878" target="_blank">📅 07:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23875">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DV68110CltlEL5tK93Pl2TCThRH3RxRj6fEZjtEFxrBzIrxdBKB3zAqKSjhk5wUu1wI2lr50-hQtsExzymOFKy9FibUdhM3HjA689ay76T4OCRxV4ftBT2MYR-NPYI2Oq_46sJUjGDhPG6gB6EvMDvP2Kg147a67ihv1vsmx5Gks4KkPjHzQOfWF7KlxlTbiIUPmN1SiAcPaw2Vig0YnrS_p5wWerZEIPeR2t9Ji3RZG_K-8q6iQnh3obZIbUnp7UaU0PXnJ4UrUOoNvs9NAuvYpWzHMK2RVRcriwPSiqRSRcCmwHrXnsYXNrbgwz36xUdZHWTlVDyUfVP3ydM7o5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت خانه در محله‌های مختلف تهران در سال ۱۳۴۶ چقدر بوده است؟
جالب اینجاست که در متن آگهی ذکر شده مردم قدرت خرید مسکن ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/23875" target="_blank">📅 01:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23874">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCrc_QIc5J1D-ijbVeRuovxAaiReh6aPLcq4SHBZX83ghZCLMvLkEvKrIA64uOyKXPI3lgTFVeb9oa4I7kcYxNB6YLOe-TEM-KLZBZinytPoWUjRdRJPILqI9ufPtf-nD-1OPNAt4H6FjLsS69TMPhubxYRMcb3F0rRIBjN-JeSdBevty76I-sbUt2j6O2BBRfAf7tu3V5o6LJTHtlxM5WKJBkkU0lQVisWDX1BX99iw4zHJlcHWi-EfpLyuxiLxiSav9EiFZOWwt5lwRmxOSDWXKnpr9lSA95DqPqAgqkLC3eW6yJWrwSJlhngaLYfhbNoYNpbwLCcm4Ghajo2Mkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/23874" target="_blank">📅 01:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23873">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">▶️
قسمت‌‌‌ نهم‌ ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/23873" target="_blank">📅 01:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23872">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNCCBSXC9D442ne1rzg94WHGe5Is-I9d8n-MYbDQeVaDFVuA2JxhZEUZr1-SNFIYVcsdmKVewO-TjCaRuUDccBGMlf0AiHgBVZpxJlsWRYK3_rrdq_9Z2bdvGCrnUSiH2xKaXiMxJwxGB5FWkdARa8ZogfQf5vow8SafjKFJgf5puUqHs04pq5GBcj7UeNIdCswvGkbEXm5870-FxXiM3Au2Irzc17rsrexlzbvBTYE0AjoUfzs3LxubZPrkBgdpXm4UZLaDfZE-igqaX4BkYZZb8yagOgqlwoY67E2v7Uk94c4D78wcQTiR3ZlhY30BZPULqTCfnAPDVG_48-kLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با درخواست نیکو پاز برای‌ حضور در کومو به مدت یک فصل دیگر و بازگشت به رئال درتابستان‌سال‌بعد موافقت کرده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/23872" target="_blank">📅 01:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23871">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jau1hQwoJ4lVkj0qdurde0SabN8iE46Wqbd87GTzeCEui5GD1tepZY-KC_tz-FveiEjXSXhpQTeUmHzP4URaxSILdZE3LcD4Or1KtKmwFALgXigN0eEaLFQo5fzCf_MWBXpUhBmi8P7FVsz9R-Qa6esku0YZO3nkGyvrGf9Q_G-wAutRA4uZKivLBp-9XrGwtAOoAhpBIH8r1VGT26MZ54G6XLizUMGxBtLSwyF7AE5Eh215QpWIJQb85m5wHH69ft_uxMT0ehIA6H3EJizf3lB88osegBWnr60fIkOTmgTsm97P6tdziuPAz6jilT38t0D7lO9aObeHFzpVz-1_eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23871" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23870">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jde1qzXzriRDzd7jO_hbNVX5SOCAH_qHjM72Dx4zMQcNYHDMPVv5BhhwV31-Ih5MjVDlgLuUCAGItMhuSynhnzjHPT8O7rmapiU7fdVoVIeCw3O8fnOiwfv-rhnAjhEJDMW9TWu6ADmJe6tIoP4zST6gXZggmm9Kt_Iwwt0cbv520hoLP813yLHfan0jKbv5Rwyckne34v0iOdvVEiNzv7441xKecIgDFv7UsEv9Tkgjj9GJulmJAz60qCtHc4vmZhZ3nIfS2JiBGU8H0_OZ4_8aQ23bJrcUK-AtjRXkoFFcdGwZEFp8iy4xELR6wCn8sttxPr6VN3-SIHx0u9_OZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
از باخت سنگین قطری‌ها برابر کانادا تا صعود مکزیک و آمریکا به دور حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23870" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
