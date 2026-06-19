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
<img src="https://cdn4.telesco.pe/file/PuuXlDQuHGrAPWm3n3CeAy87C8QoK2ptUqdl95nZMZjLE2aQZbL56BKT6agc4_EunMgZZrr5XrSsfVnTn74xtisBqfy28kguvMRW9euvtwCgaE4LolbKTjHEV8uG1qvZtNxOtW1uU8fsVUctFGXbdrBH_MPXl9RQBY9ph0NEZPdz5pGn2jfiDQ1A3ndhwZiAgW44o-UPebWZUJbVzFNHu4Ash9SOPsKBzutyhy0Cv3cRn66nrMOnaT-YtSvMAp_co02blsTmDSlaRGLjcUbfo3XhwmIljG1eXPWUGeRktxQKP2GtSGdTN3I0Ot3n8VrvFcdHhNyPyD7Co2HHfItqDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 17:23:16</div>
<hr>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=nEXfeO5cBsfBxA9VrRX7j3hOAB4DrvPlMuaZjzViBSZs22oymuUh5uTB8xAGRrohHcED8XXQNsKVR2vdtWSPIEOPuEKmQf_umbWklh1Jvr_B-j-X7rUUEkiw9tSfM03niac01QgebpiMAwvB6zzdRAV-xCYgnK4E15hcXpDvYINcOn-jGF2RAY2mvbD1m1oYZwNO9RqI4hAnzGmL635dms_YY4I_uEcLv6hrDIgmEU0D0usg-yMKADG2-WWUFNjQlgOQ-epDKbRZcGYIbR9kfje23SiJ9yWfnDEM_8nwOTV6dCf2J2vZ-H9fLs5cistZ30uCVtvdFSqxGtyDvLGQtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=nEXfeO5cBsfBxA9VrRX7j3hOAB4DrvPlMuaZjzViBSZs22oymuUh5uTB8xAGRrohHcED8XXQNsKVR2vdtWSPIEOPuEKmQf_umbWklh1Jvr_B-j-X7rUUEkiw9tSfM03niac01QgebpiMAwvB6zzdRAV-xCYgnK4E15hcXpDvYINcOn-jGF2RAY2mvbD1m1oYZwNO9RqI4hAnzGmL635dms_YY4I_uEcLv6hrDIgmEU0D0usg-yMKADG2-WWUFNjQlgOQ-epDKbRZcGYIbR9kfje23SiJ9yWfnDEM_8nwOTV6dCf2J2vZ-H9fLs5cistZ30uCVtvdFSqxGtyDvLGQtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh99LCTwYnsTyTnlqFnvtZzwY5LKBUs8tTka5xttXWkjoDPPNXgaJhEjTmSEquQmmpNVgGRZ5uF5wOXBghdcCF2X3I4e6LHGs5NXb5-uyrYaTspnsLUPYultGCPBacinXcqtAlJXW8fGP8wM8eJ49mFmqRGwDvLDaK5yDW6IHYG0JVpryuCocGJuYXhnx6dOkTtCKnYt0hk8tEPuocITjMRIWRXil1Z2X6IEgb1LObvmaE9saJkOqIZq028DhaPUbbRuwPVMRXoMC5GXtPeZn5G7lET0e61ncN9LXVKCaN5NTYOsV1id_m9lox1Hp0sF4sOjfNc9LByGgh-Io986cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=Wf9QFXaHilqVDnnMxQbOj6S-7GXKi9rdmSUuJJlj_OWFIHB_eZ2JA_XfHHN4VxvcLGF-yHEPH4rohXrX0ZEv5cDeLFRuHiHN8idwratDGp9IWotd4heKAurEBd8I3zECSig_Ka6mjw_Ye8Y_f3CnQROUGkbDrCiSOC3zR2A3ehJwAlkBxVSwYe5mpa86mvSCCvQSaQii2-n-0NnImjgUuayc5NrITlLfNsuvjFHLZXkyxhkPR_vp24xQ5EMEvpiXH5sWM9aqZfw6YjNm81U46InhCsh5YCApCIcwDlgWbwJGjE8X29j0trjygpeafvmUTjmdQ6NmiYWmP25V1lcn-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=Wf9QFXaHilqVDnnMxQbOj6S-7GXKi9rdmSUuJJlj_OWFIHB_eZ2JA_XfHHN4VxvcLGF-yHEPH4rohXrX0ZEv5cDeLFRuHiHN8idwratDGp9IWotd4heKAurEBd8I3zECSig_Ka6mjw_Ye8Y_f3CnQROUGkbDrCiSOC3zR2A3ehJwAlkBxVSwYe5mpa86mvSCCvQSaQii2-n-0NnImjgUuayc5NrITlLfNsuvjFHLZXkyxhkPR_vp24xQ5EMEvpiXH5sWM9aqZfw6YjNm81U46InhCsh5YCApCIcwDlgWbwJGjE8X29j0trjygpeafvmUTjmdQ6NmiYWmP25V1lcn-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNaEnmYixfZUsj8qZho5tbGaEq6mrjKsxHkhcmvm6c_7z8cuIt9S-6wgRffdj-Mynsicg0kx3qS6ue1jExpkuOSw6X-waoMpUXWGNQ4aUsFdGnkxQoPnz2FI5kLJhvo2pTVbp5S9LSIzrkBH5NKKPiQXy4guMrN4yjxduYxp9i6uatijnb8i19-_5paAl5lKim_jw4NZxzMICNXeEb8YhSxXMjQ-n0YtDS7HLmVxIB9psZaMJkoWmk7SoHbtx1YyzxyeAUM7IohOPyDPtQJ7OcTdI9ru2wzeoPhv6Z9Wa5QuQ_kRdUWRS4_30Kd7Rj2O_YEZvAkcJRiVIcHuQAfwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJ2zZxfnkMNDITMtNtiJdMI0rBt_cuIKIMyAfQvAN5fPRtxVpM5kRcDSXjSyoGTbd_xm6-Xz9fsQVHPjWis7vdp8xQyrZ22GVXohviT3yleMjWwwZO8Uo5KxXUK4zoQ6vDLAc204UQg8ZnW4WGcWV76etpNCnX87pTgTjGJYnwX-lA1T7UjPHfvABBuTKUwyBtMIhuymK7FF6bNomJSSnKOJ3xPWyPxnlhogUnzMBc8yQ4kYjNVwyavJ8CDxFEaiYLNdvtxRzsYc3TBxb05TDC9uxQNHmV5h7zTpnntkPCZ2FQi8hYiyy9V4nFihvOAkv4-kUVnmS5b6nslk0VflGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=YecdkQ-aA1LUuXjlL-RfEOMgu0x-OME0zaVYyGBe9qmwtEJBt9nkqpOqJOgPOyOimB97Ip-si9_-uUeJgkEZvsKSN6esNQnx93J-kmSFT9dVqEjsjaUOxglW4-GrGjb5zgOG-pJioVXiX_1hZlhuH8CYegQh_Qx3QqyTzxaFGkZjAQrurbHBPUtPoKOnkv2EHSakyJlqm2WGFuGO894vxcZYFIIXqapAgxGAStIbnGbEVlagKULVBnKbmJX2AZk9rj8RBJclZ9IMLG_EvTey4o3-eLn0_0c0J09JzRAURuNTlTXNYS2l4cJllzty2ibC3NxQd7FvPQSekn2JkwFkOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=YecdkQ-aA1LUuXjlL-RfEOMgu0x-OME0zaVYyGBe9qmwtEJBt9nkqpOqJOgPOyOimB97Ip-si9_-uUeJgkEZvsKSN6esNQnx93J-kmSFT9dVqEjsjaUOxglW4-GrGjb5zgOG-pJioVXiX_1hZlhuH8CYegQh_Qx3QqyTzxaFGkZjAQrurbHBPUtPoKOnkv2EHSakyJlqm2WGFuGO894vxcZYFIIXqapAgxGAStIbnGbEVlagKULVBnKbmJX2AZk9rj8RBJclZ9IMLG_EvTey4o3-eLn0_0c0J09JzRAURuNTlTXNYS2l4cJllzty2ibC3NxQd7FvPQSekn2JkwFkOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=cyPP31PjYFFyn9KlZ6grgAk8lRkHVMo4rObCCdZFXuPuFYgZV9K7plHF6OCMG97th7U1eQ3HzimuvjueyhutaoKRkpR-i4RWsmCLtVdf210p6woeo1gHlWjKaxvTJmU-dPeGea8ar79zO07z54cXB-nt3ZMG0nTMKRbSXHPk0t43LAaL6sziHB9P9bO6dWcD4Ajia4Q7QzXhJfV87mUaL8sFAGLe8qLyNMemk-wI7x1Jt5_1cRydLwRjjo-QgAP2m_uoxl_Z0Mavv5n9meqZu9KvAgdFQIWoL1HKsiRrXbh7oIgARoSz-dH3UUpLW_IMsRVn_dK6TNcboNvlyQdc1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=cyPP31PjYFFyn9KlZ6grgAk8lRkHVMo4rObCCdZFXuPuFYgZV9K7plHF6OCMG97th7U1eQ3HzimuvjueyhutaoKRkpR-i4RWsmCLtVdf210p6woeo1gHlWjKaxvTJmU-dPeGea8ar79zO07z54cXB-nt3ZMG0nTMKRbSXHPk0t43LAaL6sziHB9P9bO6dWcD4Ajia4Q7QzXhJfV87mUaL8sFAGLe8qLyNMemk-wI7x1Jt5_1cRydLwRjjo-QgAP2m_uoxl_Z0Mavv5n9meqZu9KvAgdFQIWoL1HKsiRrXbh7oIgARoSz-dH3UUpLW_IMsRVn_dK6TNcboNvlyQdc1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NR8JAIJzL-MkFoIp9N3X5I0_fFWOsDA_KZ2LYCRXp9cXrXI7an33UOdVHEwsxxgKBH3B0nbnSvZX7uCZkW19xSnyJXlawqi1uBvHyr4FWXvDgaL960otiBzG0jr46ih1I3iADWVDK5XdGMlWaRXn1I9-M4xwpap9F4jbIfwCl82NSbtKfOLyI4VjjPzwA4yXT1P57x84QiQkqUIFgXB8gr_sG7wT3kQC6xgwe4hRiN3yCBC4tTcGh5yboiTRgxyFFEPUCt2aypiwkTyig1CqlAs8weh-PMHsfAheQ_-vqy93mqPinViKts0nZzijk3xGAcAthPX24Aqnp12KciyymQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aECkuhEdwBJ5-V8aB9IruK8z4kJjmNi0Rt90cJopx_Sbe3HSIgjsnxhsMl6_OO7yQb7jIlFp5O1-n96OYPluHTQpiCJFNXqNZM_F0MiqsR_fKAaFRoylxbYplmUnVRFdyx3RYj3RlmaXjLIT2xBhWAsxErCdED5dGjsbbnOS-xUTsIAz6BYj4qWL81clGrGx4AqKgfUZUTbwELYeLqRym3kZLbZnw9ivRqU7b-H_x3A4gyXcqT9ucFP5UG44i3by-49b-sIpfRTS0ihgD645LHkKjVsFu9WwIxa8FOd6CHQ7y1H8yjY-XTar3keaz5KWO1dzPOuIYnrvtbSbYP11yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpM-RZ5JdQKGve3K5rgAZ-UJxoBkPBBHGtjSa93Mj1mK7_IRaTREVtZ1wfdJu1BMdp9dkoWji_x8RGL1pXiwSmyBS6ijjMOy0y0OsfkqGyc-G0O72jQyu2uolzLzCIfzeWRIFQiuIp3WdE-auPm20OM7uRUSBLSl8Lunlj3807mgU7iMdwVcUgFVKy5Ua-hARJtaoibGLgzZbkXU5err3_WZs7OW9CWri3bPH9KYpjZ4dt6Is1fvp3gTigvo5_E4pOu07I10mhKel7NNo8We8RzLGz4ixXdaQGY6e8yL_kVThGBwrqGA1_keHDsmsXfuMLm2KD70yuQiPTcetPsWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=bioQav7JfjRE6SnxCODbpUoiens90aIeoHQefoi-jTOC6hZ8cQXGFADElz_qlLKJsf_ffFsk5D_Zix1SNJV2t9bBds2DwVtfsGY1XiS8XhNm0lsEjXMJw6ZTD8E7kGLMfnfIhV4slyyzszU8EZis7Ipou0C-yt4CurukKKk6fsLUAgMH18ultG3YMVYYlh5o-iL3OsAsOwYUHTSRanDJ-l6zaVR8kARTPDCTLaSCjLv3cLjoIJ9GD23bGpXAchhxFU4Gvpqbj6FaaqlWVTlxkczWubTl5atYdYoMVQLaeJYZIklyMk50EoPhnVhpymfmNMRhBlWPuuLX6djGO3vVjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=bioQav7JfjRE6SnxCODbpUoiens90aIeoHQefoi-jTOC6hZ8cQXGFADElz_qlLKJsf_ffFsk5D_Zix1SNJV2t9bBds2DwVtfsGY1XiS8XhNm0lsEjXMJw6ZTD8E7kGLMfnfIhV4slyyzszU8EZis7Ipou0C-yt4CurukKKk6fsLUAgMH18ultG3YMVYYlh5o-iL3OsAsOwYUHTSRanDJ-l6zaVR8kARTPDCTLaSCjLv3cLjoIJ9GD23bGpXAchhxFU4Gvpqbj6FaaqlWVTlxkczWubTl5atYdYoMVQLaeJYZIklyMk50EoPhnVhpymfmNMRhBlWPuuLX6djGO3vVjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWNzIUYyJaeFrGg0xGaFhSlPkAkulWn7j2e4kZ6Nqass_6Y3KtMuTwbo3N9lCcT3omvn1ecNIfhYtrW9U9a5EYLkwL3_qiTnKSU-7CJJkGH-ZhqzuIqxtO3Ph0V-pcdH2Pq3FXNg4g37nwpKY2x9YXDW9IuuhFoiY6kC5zJmjvtaN_mx1LRop-zwgngb359SYeNUhL43v9k9vSATpOql6uoMZTbA-1GuNKgX1n2lgNTUBi75q36VFjGfoJBf4K1WDNkmg-jrpu_YpBnvhExY5X0yQNDR9pUkPDK-Nds6ap1Z1xwS89eObjVWfGSYi9AI0w0Ra-UzAPASrY7_eSx_0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو
به
ترامپ
اعلام
کرده
است
که
اسرائیل
بند
مربوط
به
پایان
فوری
و
دائمی
جنگ
در
لبنان
را
در
این
توافق
رد
می‌کند
و
به
رئیس‌جمهور
گفته
است
که
اسرائیل
خود
را
متعهد
به
آن
نمی‌داند
.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkwXhiYR91pSfodkrdV0ELnsF_yH4e7IjWKMsU-s4f6ftjuucISihMfFX3j-fK_jyumayOUihKYn8uO7zqiqf9ElP1pUGIj9gE7-IEsampqYqXxuewFlVEh0IpM2RhkMcelyk8CfOmHQGSloptPVxahZDV-J4jr0Sz0z_PjaPQV1PjP3RqRd5KRIl7bj4Z-Mk95WaXJ051L7M7rOWNxBpurPJ5CuAbBKPUm3Z9IV_440kXXig20PnF7amGpDmskMUDcQykdma5z2iMjsz6mYHXexyfTD6WZBMBwyrfZJgdUkAAbP1yUcquzIRS2PBOttqzkZnZaKUcplJpjG8RJcxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جمهوری اسلامی تا اینجا با آمریکا به توافق رسید، اما هرگز با مردم ایران همراهی نکرد
و به توافق نرسید.
از قضا با اسرائیل هم به توافق نرسیده.
مشکل آمریکا با جمهوری اسلامی
برنامه‌ای هسته‌ای اش بود.
مشکل اسرائیل با جمهوری اسلامی،
اما هسته‌ای، موشکی و نیابتی‌اش بود .
مشکل مردم ایران با جمهوری اسلامی
اما ذات خبیث و خونریز،
غارتگر و سرکوبگرش بود.
اینها هیچ کدوم حل نشده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhCBW7su0zyE7DgjTyocLqKxQNLz_FHdGl1BabR5cmXEDJz1lZyYLzcWKH8rfzfI3qY5NswsUyQvXYCpKnJASKZyS_m5NhDS3UrjP-oaEmByoF6_3o06TIiQCH3PonjIKY-pDY217yK-5ue0Pq8aHu2iIZpKIWZZp29u7Hpc9-_WS5LYYXMCnC4-gBKCWxzC45KPgVe0rHMZUpYzkKQqFGEM_b5DhHx7PMIpSRowBbk_vBzecNu_92QCN_svpWZ4ETZ_T2yuBTw5hS6LWCfxeTcp1kW5SIwKPsbZGf_0eXHKwHACwCAbTwIzc4b7jhPQDNXoALmT8O9W5v9LPAdtMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbNnV6d7HqKbUFKRGijtPkFfcSuDowOhMfvuPVCPo5N0oqhk4NVnL58WTR85oFOMToP-QctDWF7VY7Ujo7vp8x5pfXRG-q4MCFnhcaXZsWK8y7Lwc4tn6rtSbCjWtTOA-Qiih5Ho6NrNknI8gIMfRwCor2wGYIiLnNT6-ErtbjXqj4YW4QOE5KZKritcYMjQxvHtd_LIlYxXxtr6iV0gFtP-2ExO0ArV5qLXAumV5U0vDekk-DiIaEDSlONEmhgor4UE42b0bkoOHvir4MC8oxtgp9H9NGndSL2qlhOoZZnv0xa5w9NPjaMp5IiXKKVvBNnQVfMc_GsyQhEShkh1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=ZZzZwwCcDPtJufjOB5lhXrPv_9LI97TjSPXkqNd-lN8kSkH9eG37JGrk1rrcXQx0EF-etLBuCkBPZjiImWAtKG1fWvyAG6cIZIqGmQjkur_TMR5fZh9equRkeL1XOQQsi5Deg7N-nkqPN2D3DBKoFGjYWIL8QK2YQwu_W7WCagz0hNmyUt4-kw_TImZDA5ITzQjsa7opZeh2o8FWZaFgLO_UKEXYndc8OLIQ9mQmr87ZiIWnYYDgQc3KMNCqW4ewMeM2HzTexuD6dEMPXtkkAiPpNWyXBBFDEakupFwo38WlSzLsQHPi1w1Up_eeefXVun8unzfZP5t9TDset-7K6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=ZZzZwwCcDPtJufjOB5lhXrPv_9LI97TjSPXkqNd-lN8kSkH9eG37JGrk1rrcXQx0EF-etLBuCkBPZjiImWAtKG1fWvyAG6cIZIqGmQjkur_TMR5fZh9equRkeL1XOQQsi5Deg7N-nkqPN2D3DBKoFGjYWIL8QK2YQwu_W7WCagz0hNmyUt4-kw_TImZDA5ITzQjsa7opZeh2o8FWZaFgLO_UKEXYndc8OLIQ9mQmr87ZiIWnYYDgQc3KMNCqW4ewMeM2HzTexuD6dEMPXtkkAiPpNWyXBBFDEakupFwo38WlSzLsQHPi1w1Up_eeefXVun8unzfZP5t9TDset-7K6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgtCVriizB_mtVQmN2vw8AVDjEmboV1Jg_xZL_fiTx1R9Tk0fisO_0-rmc1EQJ9EnoTXHyeosg2LHK42zSti56js1qAn46x_KMjG7DYllkpaRoqoHDTCpOvbLYPIk-ezIbJeXW1H7NNpfCGHyM2OJi-jwSd6jEOK_m6EygtdPXw7gM7oS8GlVTpXFqlAAOBp_TKNtTJfi7Twk8k2E3cGR6JSnHkEjHK2Dtt-hoyjFFEfhEQ05SMWWVTOuRgcvSEBsVQKI5U8pW8lzI9XlEPX1_rY9Lef6gqdG-H5X8X9yMDYKP_r7can8sJtchQ181qDBrIyim46egYGFYd4FPUwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منهم صد بار نوشتم!
جنگ رو برای خونخواهی خامنه‌ای راه انداختن!
بیش از ۷۰۰ کودک لبنانی رو به کشتن دادن!
جنگی که نه به خاطر لبنان بود
نه برای منافع لبنان بود،
نه با سلاح لبنانی‌ها بود،
نه با تصمیم و اراده لبنانی‌ها بود.
یک گروه مزدور تروریست
از جمهوری اسلامی پول میگیرن
که هر چند وقت یکبار جنگی با اسرائیل راه بندازن!
فقط برای زنده ماندن شعله‌های
خشم و جنگ و کینه!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=pwVUx1LrMblKqrRodZ7rjW-2jd74qGrk0R28kns4lxU2znZA97s_U0FJ3w8l5Re5zBd3dKjkLI-bSewvxXIxt0jXRuW9e_clqYe33GnBRWmvTbs3ezFNyGlIHNbSoZ2UQOid2Pk0aAnAhcnm5m7QGAbFkW4Yt5PvxHiK-E3-CbHar0L13X_qfTeaGOOQIBhhlwfBbdOuHWguXVFHy_5UWmqM_7NLHNAymEcCv5ZLo4ktgtGJPFR-39CpIv6nEZRhSBdu45R3SU46NCTVnTPbplfyRTk1AQBWwFOQkxYUMN4VARRdU46CxyuAs_hVWG3RFhpRKbT2loC1jsDws9T7LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=pwVUx1LrMblKqrRodZ7rjW-2jd74qGrk0R28kns4lxU2znZA97s_U0FJ3w8l5Re5zBd3dKjkLI-bSewvxXIxt0jXRuW9e_clqYe33GnBRWmvTbs3ezFNyGlIHNbSoZ2UQOid2Pk0aAnAhcnm5m7QGAbFkW4Yt5PvxHiK-E3-CbHar0L13X_qfTeaGOOQIBhhlwfBbdOuHWguXVFHy_5UWmqM_7NLHNAymEcCv5ZLo4ktgtGJPFR-39CpIv6nEZRhSBdu45R3SU46NCTVnTPbplfyRTk1AQBWwFOQkxYUMN4VARRdU46CxyuAs_hVWG3RFhpRKbT2loC1jsDws9T7LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=B7qQxSkPuVsmcsAnyGL15yqZM1G0KaK5lux_WVJMduDST7sLg2WmRLbFoUj9P67HaUCdrt0VAThbiCryUOP7PMGJcEBD5lAY0dHQS1Wun8CmME3HZa_Beiaik8_xR1cZwjgMugH592TP_A2MqiGJ9o91go4-OFdrI7FjEsIwrwcyhaRQBZixf7cJJ_RQNdG0nhAxkCpO0gpwyF24K8ZSKswtpY3_2G_7xstPSAAPb1_k4azRgJS_JK2FcCUfSiWEhMkBSo6SxqOAxXuI3tn6M-tkXnzWDG0HwV8bO-DE7NoKwdo9mHhDfHeYMwtPJWL5gK2Cbse-o7_hWJTSQhoYmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=B7qQxSkPuVsmcsAnyGL15yqZM1G0KaK5lux_WVJMduDST7sLg2WmRLbFoUj9P67HaUCdrt0VAThbiCryUOP7PMGJcEBD5lAY0dHQS1Wun8CmME3HZa_Beiaik8_xR1cZwjgMugH592TP_A2MqiGJ9o91go4-OFdrI7FjEsIwrwcyhaRQBZixf7cJJ_RQNdG0nhAxkCpO0gpwyF24K8ZSKswtpY3_2G_7xstPSAAPb1_k4azRgJS_JK2FcCUfSiWEhMkBSo6SxqOAxXuI3tn6M-tkXnzWDG0HwV8bO-DE7NoKwdo9mHhDfHeYMwtPJWL5gK2Cbse-o7_hWJTSQhoYmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfI70m7Ap6j80EwT-PuV4cLp8_ljRkoQ7gV_vAbyxPeH3HSecHfR_csAe0A66FEBKVL3uGZo7k2ywJi6jp9KoRV58boc2r99J8ZQBP5zB2MCR4H8yIPNOpBHDYLI-h6hMrfBk8jwq5DELu34AbmrZ3kjR__p6eLFnynQNJojmZuTnfG3FSWa0X16vdV0TqfyHg-qTeWUbQoRGRWIojXnwABT3zbVXl8gC_9cS01RLkupW7p2INxEby8G9T9rD3YD3WFuZm7B8logAjrJdIeiFMSXOEPjoS74bwDwZ-EWlGL2af0J9wahetwMVw0-P1owCiPi5I0kAzUOHvJUAL7_kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=LXfWB9IjKLsFN85eB7i3WHP2ViIP7KutQuKetPjQexu2L9gJCCpF_Rfu1uk6g0RSoZmrsM-MRSlQrLtQdx9aEmlSAxBZBIX9cTxobUfXJvbuCQ30qX7PYhBeFI1jpkrtmPgOewqjHJcc-jjmIJxNLu_i3vFp1-UrPeNr9VWqfIVGo6K1uePiSaWUckvo8gP3HkTdCQ_gs7yDxF8GqtBbAXXt1bHP4uaxIDtpIJFYXw5i_IBkt_TrcJMiPVcVma35_-qPNIrIri9XDvkptjJJKtQqNLONqntXyrnffrMgJXQS1enJPaAMASoiybSpM6Sm368qulkW6bY_HGX-HBeC8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=LXfWB9IjKLsFN85eB7i3WHP2ViIP7KutQuKetPjQexu2L9gJCCpF_Rfu1uk6g0RSoZmrsM-MRSlQrLtQdx9aEmlSAxBZBIX9cTxobUfXJvbuCQ30qX7PYhBeFI1jpkrtmPgOewqjHJcc-jjmIJxNLu_i3vFp1-UrPeNr9VWqfIVGo6K1uePiSaWUckvo8gP3HkTdCQ_gs7yDxF8GqtBbAXXt1bHP4uaxIDtpIJFYXw5i_IBkt_TrcJMiPVcVma35_-qPNIrIri9XDvkptjJJKtQqNLONqntXyrnffrMgJXQS1enJPaAMASoiybSpM6Sm368qulkW6bY_HGX-HBeC8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=mlYfFcRzlZ7X_q1ht165OWrZZmNMtWdl-bvFyiXyly5VveGwDiEDbm7x6VAg89o-XEc8ja6c3t0IH9tazqPGVnmSRbq7NMnFBkuBj2vGdUv-Qysdnnas7OF5f1LZ9trO2eshRW4zPOD3Dv4Gf9KVLbvhv3tu8PBPg1tACPpaA072H6cPER7IgRuBmX8r2KiLqD8-YtDvSYuXm2BXb4yaVp3t1ndhqhQWUXWhA9z2xpVd_WyIPHq9H2CjAztEG93S0XMZ_AlOUMlX-3c0vOn8y74wqMHaS88eoam22MT9D0fbn2iL_KGpViInKzAglelXRXXaQzuI3ZY5TOC2fHH1Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=mlYfFcRzlZ7X_q1ht165OWrZZmNMtWdl-bvFyiXyly5VveGwDiEDbm7x6VAg89o-XEc8ja6c3t0IH9tazqPGVnmSRbq7NMnFBkuBj2vGdUv-Qysdnnas7OF5f1LZ9trO2eshRW4zPOD3Dv4Gf9KVLbvhv3tu8PBPg1tACPpaA072H6cPER7IgRuBmX8r2KiLqD8-YtDvSYuXm2BXb4yaVp3t1ndhqhQWUXWhA9z2xpVd_WyIPHq9H2CjAztEG93S0XMZ_AlOUMlX-3c0vOn8y74wqMHaS88eoam22MT9D0fbn2iL_KGpViInKzAglelXRXXaQzuI3ZY5TOC2fHH1Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUz6yNt7qo413s45GTk5PlFUtQPCKrXpP3tc0bNUJXoxf0YC2NzsxSD5U9wpbC1pQQ7MYTLS1dmnpAuC6tA9L6AvMq6BeCywI8crG1oEOUsR5Tpmu3-vw8FtVgzVJrtvlVEWXus5kY2L0xGSmGGQrVVcayKWkuirGjwSsaroTNmlbfxiyJIeYow6uCqaAw4DeBeuxFk-XwC81zJPzR07pOHYQ6hpwI-FTydXZNlAN4kCiFJcc1TcFGaHLeqtJqJ8cz2fJJaDUxtRVYMdCY-w7r5lcCQfG6QNwshPxTRERPirPyBIkE-sPCgdAHHfp1x9_zx0vniUqDE1J7y09VLW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukOCaX-u405H8L3EbG73AUpepnjy8qBDMInq-2Zjqip3g9TJFJ-lfx7oRiNyDd23QROr37ng3d74NJlMCJ5hsLE2N9gyD2-g6u-5Cw34S2Wg40M8kZCUfbpgyExV4tGCo-Lhur1-PrBKC-1SZcsm0tV_ilOvfoVknuOLqNTKIwTNGa5SQ6qHSuTXaSqzhZ3TzitMBstRWIxcvbVHnJDDGAhjnf8u1bF0fnLvc68hI-gJxxa2PvObolp8ZwAd0m_8qDUtbK7aVrDke3_dVlqmgaxp4TeWSBi7fyx9ENWUIfIj5yJ-xlZbYNk_-oiuHcufSefBU1RLBQxRAIvlWvusVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای حزب‌الله ۱۵ سال در خاک سوریه و در جنگ داخلی سوریه مشارکت داشتند
تا اینکه یک روز همه شون فرار کردن!
مجبور شدن فرار کنن!
نیروهای جمهوری اسلامی با کمک هواپیماهای باری ارتش روسیه به ایران گریختند، نیروهای حزب‌اله
هم زمینی به لبنان برگشتند، گریختند.
و بعد به سرعت نیروهای احمد شرع
سراسر سوریه رو گرفتند.
بین نیروهای شرع و حزب‌الله ۱۵ سال
جنگ و خاطرات خونین وجود داره.
احمد شرع اما در این ۲-۳ سالی که قدرت گرفته سکوت کرده، اما اگه نیاز بشه، می‌تونه تا ۱۰۰ هزار نیرو روانه لبنان و مناطق تحت کنترل حزب‌الله کنه.
انگیزه بالایی هم دارند!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBAD3jrRBTJt1ImnlL8Yca9n_Y2aiMPooerailicUngU9ZLoZ7F0A1pI08IwX_Y4tD7lJVDRtx8AB6pIq7kRwzbhV5ULXkgspN4RiqmabEti9ZTuOnov09mYFKVrhp9ROz35ToQmwLuTl78GXy3wkkfqLx2kdvvzU1fuYcodLtDaC52n5w6nbPdbtWdjUWN9wMuq06u_ty_qw7JIGeGQ_AMOgSsXx5TvlAUKLC5soUuQx90WFr8Jj3hwbM12DAh0pmGh50D6Kch9KYX2jOknCRVSWEcGONnBtcb2hy6xtSXlximm1OjWvhR12qhGFM1nzzo5BTOOME7HfAekCuxVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMwu9av0PlH7U7bQ7MYLuRtLuaCIWnvrQ6JVMLSKznHlfaUCjD0pX03hvIWG4h8NBfU8UCIK29mIexqp6gGNomNSt_40dMSPocwBZlwgFJp9eVYHQ_7qBLcug0OJNu6mQI6vSBx_pdWuh6luzpcuYRKMEKY9Hg5fs3LfhA-lsyiRPrNOSzXsJ_WBoZUdga_r1XY7O7Ayod2MF93xindeGwXCpWdO7ja1fad5_SfUjgjcBdiRJkZuXZI0j-oWqe99UKAEsNNzloIkEYktpLj6Z_fTB8HRYONBxCdGzwXJYa2luW8RcnF5zov8NcyPuguj3mDxYmmyJqQA_Rqg8d4GJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=mi1cnJm8Sq6MYbfZisS_DFIVeDFkGWMTlP10dSnnP-OX_E8NyofYbwBKQHwG5-VjzF0CYXcDC6yR9EPTcjkaoD8CDISxAJB0mx-DCS2MvpWr4JT6tsCMAvbVbqeMjh5Yjty2ilLgPWqofD55TEwNvdPl-r-caM9e5WOkWdBGVB8uFhGh4wWGNUzcpVA1hiHpSgcL1dkkmVTUlJnt04CitUh5TdC3q0x73CafF52sKYHaKY5u2Z0qt5X-o1mVBpcNsm4aL-UqttJ2VZq3KCoDYm0u1ld-rdm8ta17A7JgPSFeST_7vb_bG0Ps-0tqdbP3S_1nWFpD8LIfXsJSvmQpdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=mi1cnJm8Sq6MYbfZisS_DFIVeDFkGWMTlP10dSnnP-OX_E8NyofYbwBKQHwG5-VjzF0CYXcDC6yR9EPTcjkaoD8CDISxAJB0mx-DCS2MvpWr4JT6tsCMAvbVbqeMjh5Yjty2ilLgPWqofD55TEwNvdPl-r-caM9e5WOkWdBGVB8uFhGh4wWGNUzcpVA1hiHpSgcL1dkkmVTUlJnt04CitUh5TdC3q0x73CafF52sKYHaKY5u2Z0qt5X-o1mVBpcNsm4aL-UqttJ2VZq3KCoDYm0u1ld-rdm8ta17A7JgPSFeST_7vb_bG0Ps-0tqdbP3S_1nWFpD8LIfXsJSvmQpdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieAaGv-ZNOM0PiEsmRX9QxoeHzEgoL8tYWSWFGishiBjZP5slBagPShgFgkp_rVSXsi4E9b2PTSa6llfyX4xkqsLGWFgAiDmGPKOwh4gzkP4Zv6tIwd3chFdxk9jt9yIb84PYX_KiANkSOxGEHyCgQ0v_zJ1he02KfAXvcnJBC5k-3XRfIrjGzcecDwioZrdk35UzZdQrkqfI5aUykMnozm9g0HjWekEWUXo4i8KRSYsZjc_6WfaWs4ZQCfgvqd6qbOtukhE5qbRlR2luIvOZ3CRvsRSGrmS3Xy8KPKR1AAbSEke_avV4tx6XGpoYDkE-6G1c2dlorBmEutt6zutubMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieAaGv-ZNOM0PiEsmRX9QxoeHzEgoL8tYWSWFGishiBjZP5slBagPShgFgkp_rVSXsi4E9b2PTSa6llfyX4xkqsLGWFgAiDmGPKOwh4gzkP4Zv6tIwd3chFdxk9jt9yIb84PYX_KiANkSOxGEHyCgQ0v_zJ1he02KfAXvcnJBC5k-3XRfIrjGzcecDwioZrdk35UzZdQrkqfI5aUykMnozm9g0HjWekEWUXo4i8KRSYsZjc_6WfaWs4ZQCfgvqd6qbOtukhE5qbRlR2luIvOZ3CRvsRSGrmS3Xy8KPKR1AAbSEke_avV4tx6XGpoYDkE-6G1c2dlorBmEutt6zutubMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLXJzqC0I-gh1lFEmvcxijsTveyijiybhvS6jkwS_YT98Z4BOH0Grr7IojCpKev3NQy9IUg703xzlUAi_4yzWNkpMSp9zwTErB15uut57el5C4vG78pT4RPpiObGAfe_ylOI0Nhv5boVynIJRzbN4tpOzQi-IyO9hX62NVdQ3dNbo0OaaOoj_ov3o6XrjMEETnP0WQEkvnqHuCc3aRvMs2zqeMHDpsY9OWZMPk3CcSj9Ix2FYy_9kxkKpyNpQLrVU_CKvhFB9alC5ReEHDxGd53-Dg3Kpsyhxv6e5SxcKP-FX4n3bzcpJb5galR2Pl9z-Ld2XFwbWDwcUmfTH3q9Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOJOMfi994dTYeWEX5rNyvH4GSbTBKtuZ2BWgNJpp7_PYmrNWlXDomuOJf6l5lHzVjpLdJaF9xyeEGEBwyOpQnVijykFLCy_2TsMJ-YgHCeRyOOo2cWElJJsL4rVZ8Fq8nJjGEugzTY1hGoRrZOicGVW1HBslbO7eDU5Ryk8xaTHp46J0sxDQCd1pm4qcFkPIH0Xqv978jZxEun9h6RWaOmL2zFh-TyGfZTeflckHXprJAi0YNImhG64wsBd41TADCaAmTcccBeZjoYGDZ2XLlgl90W-xOkBFFciaPq1jlxoU1gwH_mWym-Lj0cLI2qHeuzSx4oo90J1NkjDsy1-rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBQyvCGGr01JUdCq5tWKDR78BXQJO9Yetlw4oOqY3YWs8mv37QXjkbA4pxo3KZ0Rz2xfMVizNpln8x-6xH1IOQC4e5n0SKxvws5-0lKUbBNgEhGUZeCXXMBWHtz8oFED88rrynesqVdJRCHGD0FisYPQ6ALKJ_-7mxXHo6DL9PKnAc7FLOU2Q9e7rxoH5prcBVhrgaWgdSzS5bjIg3plY3Q6S1cLnf5F3cZq0aYrn9cuBBRpkTPspMdVCtUgOqIthJuT1ohmbqr3ZdCneqvN-bJHfcFTisaDdSV_XZ4SD2q3s6aDCI7zZztUnuIsRFDN5TrV8YEEwxVqo-1aldjhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOXkhN6pv-SGvI7MN07wdvXFII1bYWPgIQujW-Nby7TVpZhvc0Zso2_MQuF7pSTjCyBJm_q-hNZD0C6npqPzLX8ukEUyoEXdrh-FdjEiqygEttC4JOx3H4PI9_jaB1_8kCSTv9HHAFBl-fDm0u3NnI1TyNvZOjRYK8Sl5ObO8mNNObnQ0_M9yk_BvEGQVA4lnMatA6bFsINb2h-Lu1_WCy6zeqf-Y1grO8KVq5r0MNM7x-SJJSfDzwn3lvPU2VaniAvzGnJYPRDq8L8CC1YfQzqrgtpDRha-WwLlp8YwDdG_BTXtpQ8lA5MoMP3jpadiBFymholiIzRTAKd3DxUN9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrCoiwfGXt5CTgKX8_wfpL6AcGtFv8SjSesqd1N0VHLk826atImNXkNwCD1tW-GGCKc63phiqX0Bn-WIHHlK82cc_sWAzfgKVYHBkLCQPtrRBUXEnzjq-6jrnibjY4Qu97o2wB42Cv26xngoXPqotta4bHTCFn2xpyvMfFb4zk0r1Ezmgbso53ir0FGXRtMQZSdrDr0kjhfI5z5Nql253ojhK4XDhPKQxl_CFgNM01FaG6V4StTdf39G84otX59y6zL-CIHggYhHRYxm1Waip750HIJQR0V869KwMqifYzqo6nG_-pJZKjbRGkZosj8L6iQT6ORatvUkyydGV6o9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=FJpWVrDO2C_iE8ZJ8QfQfrJ06XLRhetMXr1kywJ3cONkmMC0eEKyDVrG-d-AvB5huSW6wH8OtkdiyF6htL-qCk5O6nG4Fx9s5UuXZd9yYm0eqcS4_m65MObug2oY94NGgzqxmWiojC5Mb4-v5tDupaHXsYBnb9piGnBVrc1On0C9JwsDJpELInegUPfflUByt7G3kDvjNSRvk-wyilobibnu5STRCzZHVvSXuqrl1ig9sUcLfDIcIW3oAZ5Ltcw1O01R_V7aXaeBYJoQ3iMIqxHXghMF-YD77SpQUX7-JnYVmTBnk9U9JJ4GC0-FtOGyoYyj4QfGBF4aEMtZ8OZUYaAogh4eBfnaLOe6J5_M4rrw13_vpBC0uy2_o_A5Rmjbviq1w334PLXT-2h-HK-h3iHOdfzw5h1oFoBkVrFyGxa-OwMmfTYRfntHKNzzrArcsXXAjy1_NsH0SHD_cTQA5ThOFw0-uBci_OqZZGK7w7_cG11y__4c-OOLSsM-L-NXEl_iNBJAoseRiIrNLNSvvqGHb4BG3Ua9eOjSXfh--gzbYgCHa7rEoIdAvQRO0vYKsycuriaqYN6xl3oCnNEg9POhbhH4ULqWzSPsW352sKEb98h0oyuBfsaVsOQi7Nigw0hAk_zw1fLsW7PqmdoySLSDd_hS8JcATcXZsl7TkSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=FJpWVrDO2C_iE8ZJ8QfQfrJ06XLRhetMXr1kywJ3cONkmMC0eEKyDVrG-d-AvB5huSW6wH8OtkdiyF6htL-qCk5O6nG4Fx9s5UuXZd9yYm0eqcS4_m65MObug2oY94NGgzqxmWiojC5Mb4-v5tDupaHXsYBnb9piGnBVrc1On0C9JwsDJpELInegUPfflUByt7G3kDvjNSRvk-wyilobibnu5STRCzZHVvSXuqrl1ig9sUcLfDIcIW3oAZ5Ltcw1O01R_V7aXaeBYJoQ3iMIqxHXghMF-YD77SpQUX7-JnYVmTBnk9U9JJ4GC0-FtOGyoYyj4QfGBF4aEMtZ8OZUYaAogh4eBfnaLOe6J5_M4rrw13_vpBC0uy2_o_A5Rmjbviq1w334PLXT-2h-HK-h3iHOdfzw5h1oFoBkVrFyGxa-OwMmfTYRfntHKNzzrArcsXXAjy1_NsH0SHD_cTQA5ThOFw0-uBci_OqZZGK7w7_cG11y__4c-OOLSsM-L-NXEl_iNBJAoseRiIrNLNSvvqGHb4BG3Ua9eOjSXfh--gzbYgCHa7rEoIdAvQRO0vYKsycuriaqYN6xl3oCnNEg9POhbhH4ULqWzSPsW352sKEb98h0oyuBfsaVsOQi7Nigw0hAk_zw1fLsW7PqmdoySLSDd_hS8JcATcXZsl7TkSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyRVARQuCKMG1fGgyJAcsROzfe1kroTpdoZbKafc4UJqlRFWZO4sUO9Brh3_62rqWtFvvzGlGxFktdW5mOUJsA9R04nMLOV4kuxWoY13GRqZcHkppLSjZ9PbzXeOCNjsd8Ht9km--5maQiFt4FdVpa38JtAUPEAii6TvBuQLenXUeGbWy71kJTQ3SdzEd9CpZVOsqW0DD8EeVAM84ePJPR1MYRdDzt6mLeJPUSImFUgjIlDO25DrTEX58xseehKgGvHUf2FZb6QV4jwejuvbC60iDrbTJQrADh0l1VTTQR2KMllv-VxO0HfUqrUzencanOePKhn43mybwzh4n8FMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=swyhfw2pAc4ttGDI5ZGsBLyIYHghcXz4GNQO76K_SWmSw20ppXsX06IKt7_OBTTmwMgIcBF0eMzFx5esROSFgfLY8FRDkLJVa90pbUWpCTTu4ZDweTzxUlDJ2BkbRLbWg-rq7K_k6IiZDwO8MUY1f2uoC7vdDb--84vgbTkRi_CUUqhGiwFi1GTEhTT-IHbHMknxHhK_lrdgp5XNHQjNskqhYRP2BX_SY0wpDPrll7RdFWlopSnZsZvidutxoo9oFkNyKQqPwzH3Zt3YR8F2n2y5ExQ7KFiN_IKdBtJD1U3gLdGXSvOcZEATML8hXph4KOBayO5qqnfDxbYO0CIiU4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=swyhfw2pAc4ttGDI5ZGsBLyIYHghcXz4GNQO76K_SWmSw20ppXsX06IKt7_OBTTmwMgIcBF0eMzFx5esROSFgfLY8FRDkLJVa90pbUWpCTTu4ZDweTzxUlDJ2BkbRLbWg-rq7K_k6IiZDwO8MUY1f2uoC7vdDb--84vgbTkRi_CUUqhGiwFi1GTEhTT-IHbHMknxHhK_lrdgp5XNHQjNskqhYRP2BX_SY0wpDPrll7RdFWlopSnZsZvidutxoo9oFkNyKQqPwzH3Zt3YR8F2n2y5ExQ7KFiN_IKdBtJD1U3gLdGXSvOcZEATML8hXph4KOBayO5qqnfDxbYO0CIiU4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=g7UUTZhQWh-qlK2XTcVzjVfcFJVA-KUGfZnnSaYSgdzj9Nmr8qAqS4Qq7mAUVn-_lvfU6o0qYsw6LR-7Vw0G42D54VY4Cl-NWUpd-dgbUgX_I4hf6OS7WGTkph6rYWS7L1aMkl9Io28hzr4RFSjvOQzcZTNCJnWDwsAhatEH1yelSaswwAQHoPKXX-sHAYPlBvcxd6qpsUh37S4hdauRFG8s9g-v1LgVCDUa23C7JT7uLIwZ-UJaUsONLNwVol5Jp355lggJEmeREB-ki6BM5LNtL8xQpRMtkM7M_yg7CF6tshvtZ0a4D8JpBspQrzOvNHUzgZGkT0U339jDJY0Wi1Q1oJb9FmwmkPAIpMdFxPPWNnZWa0sBYSdJOR5jIIJlxmo1eKQaHa21o7qO_eounuGCt-qSob_HIwuSWaGteqgrWArywE8mVUH6CDKW-8b_edBXlYOsFXMKO3MdY-BI2EeiA_ljII3hTUDZjfocQyvPS7swGmquOUi7kQ1PmljWKigmHBsyTw91NF2SoE1N_r0uVZu-NyZ0v86VLlOgGYOOXEIoXvDv63bZXEVPkZi-5C3YEm0rNzj6cz1SKUou04qp869pa0_zyzKFe2ez0PC6usC_Fx5AZA4HBncP7wvl51t47uOEYDfAbtMd2o23vIhV--kB2S5IjvchiD5i_jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=g7UUTZhQWh-qlK2XTcVzjVfcFJVA-KUGfZnnSaYSgdzj9Nmr8qAqS4Qq7mAUVn-_lvfU6o0qYsw6LR-7Vw0G42D54VY4Cl-NWUpd-dgbUgX_I4hf6OS7WGTkph6rYWS7L1aMkl9Io28hzr4RFSjvOQzcZTNCJnWDwsAhatEH1yelSaswwAQHoPKXX-sHAYPlBvcxd6qpsUh37S4hdauRFG8s9g-v1LgVCDUa23C7JT7uLIwZ-UJaUsONLNwVol5Jp355lggJEmeREB-ki6BM5LNtL8xQpRMtkM7M_yg7CF6tshvtZ0a4D8JpBspQrzOvNHUzgZGkT0U339jDJY0Wi1Q1oJb9FmwmkPAIpMdFxPPWNnZWa0sBYSdJOR5jIIJlxmo1eKQaHa21o7qO_eounuGCt-qSob_HIwuSWaGteqgrWArywE8mVUH6CDKW-8b_edBXlYOsFXMKO3MdY-BI2EeiA_ljII3hTUDZjfocQyvPS7swGmquOUi7kQ1PmljWKigmHBsyTw91NF2SoE1N_r0uVZu-NyZ0v86VLlOgGYOOXEIoXvDv63bZXEVPkZi-5C3YEm0rNzj6cz1SKUou04qp869pa0_zyzKFe2ez0PC6usC_Fx5AZA4HBncP7wvl51t47uOEYDfAbtMd2o23vIhV--kB2S5IjvchiD5i_jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=UHfqFFghhFf6GHuAC78cvxTDSwA2Js9dsnI3fjXYRO1mxPnLxfJj7JxDK6YXRHfOZZiIXXCifBxyG602HcxK9UNGfOKQxwUe_E_J3NduQ7K7mYfjmIB9eI6jJ9yEKmxmmG0WIwsklnW798Nam2TeaeselfsKsW-E1Bpet0Trm2Jsns56FggIrt_hWAB_WyI_Sl3fhaxsVzgB7-PfekztVHJ3GATuiWCKZ5CQKXs2nePcY0guVkQbJoLBNFvUoVqDpfXX1OfoBu67TkP6C9MApwtfA3leQzLGsF580uq8ASXTPxGqMriJVc9hv2WcM-nURnF16aXh6eJ8OTuLy6IC9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=UHfqFFghhFf6GHuAC78cvxTDSwA2Js9dsnI3fjXYRO1mxPnLxfJj7JxDK6YXRHfOZZiIXXCifBxyG602HcxK9UNGfOKQxwUe_E_J3NduQ7K7mYfjmIB9eI6jJ9yEKmxmmG0WIwsklnW798Nam2TeaeselfsKsW-E1Bpet0Trm2Jsns56FggIrt_hWAB_WyI_Sl3fhaxsVzgB7-PfekztVHJ3GATuiWCKZ5CQKXs2nePcY0guVkQbJoLBNFvUoVqDpfXX1OfoBu67TkP6C9MApwtfA3leQzLGsF580uq8ASXTPxGqMriJVc9hv2WcM-nURnF16aXh6eJ8OTuLy6IC9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FgSrXV0jQnT6CrjwA8Qi_PT15-QFSotv3TZ2HLPMqNCh6CZP4W6bEWg9xJ0ZC2Xlua7uMir502w1C2PzrqaFhM8WjKegoDJDlw4lm02-HjOlRRmVvLDRuWFG7v1AtO_3BTbmtt22oF-Nz7jUcSDvxWeqGrJMmt6BYxBnK8cZQ9dUS5Ir7CwYGwtwMyeVvtHCqzCAxExEFnQx7L96QAATWEy-6WxskdrZyeak1x0it9XsSLFXJrZf-48TsfI77iErdS5XYbF3JofLTdgJGQf4tESvye6QCvzddOgYg0RUWlP41M6ZLIuy8sDKXdmrzi7Br27gHa8FFozwA9lNYIYKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdxAO6-c1sApzkpC2NJVnfKSlv-kK8hHqPTsDRIy_-2TaUGVa88lul7QiXsURoxoRoHINScDbIAtYmN9HH-eflbq7pKFBFqAXVwgErKpwMPyfcU_WH_tbVuZb7QyOBdj-PBbJc_5c32oo034HcyXH1DpBCrlktlWOFAY2g-agexivJet7bTMRq9QG32v_bEa9zFMZ6WxjeOxamkKaeCtvWsSKaKaTBsARFzKFtBwnPIqYWyQCHr22umqkky36An7TNrF2pq2IcT_n3IUtwnPrYsu3IVt0vTuWj2JO0Cw7x5S5O4IrO8MSNThosRSD2DtL2tjoVDvcSIdD3ZRLwMPCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyCG20ZFHGAJxZcY7fe7SNuPwhUf3GEbUl2BBzidafsLQuOm2Hmkf96igQ83-IE5Eu_3fD-HiZpRduiohr9PGcp1Vp8PpZj8uLdupZwwb7HnUoLF-O5BCoGDrmHbt7EPNHw6NE-avGRvY5u6NeeaOiXSJEVloVGC0pzjDGHT_jWYwrqopNtkwbDcDkcWic6hIoqUFaw0Dj_BKUUCQ4Cg-HbYfXYc4Ckb4weyq7d6Dv6shLpdNHLv5deDE2Fpp3dMTOoJSR7AOAtqkiLI9UgKXinu78sajmqBJnfPUudxcFGHQeeSEk7mwdp3HtjBI7pGVpARjK8bDULj5U9jj6NQAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnBXxmbjWwg0XYKTyICXiUwviRrVtGJaBsBIGX9nGpNekbCPV1ZbhCaNYINtXgqXGkD5AS5KenPOtfroR93ka3VYbrn2VqUbXRIqNxqU37wPY8IssgCf8euIKv_ti0D9pB-FcF9UiZigeWW-irAx69Z9bviehxMGYGvF4Exw3vMznAzOItonohk3EIIYQVCUKj3mu9D0095RgL2rvRjzREXtgL-jJn3xGgXMY1vu6DJDiI97g7lrj53EYnDZlyHub5i1wWSaMtK4IiN_jcOfeFffrlMVlKZGCKkYuUccE8RxhZqGVl0-gn6jwXD90gXAaF5S77PFy_mX0yhbg27EVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gmr2wm6OvoKAy_a-5v8n_WViDicP9A5fMivFutmM4fTZdFv9lraAj5oBWYeT9k8FUE4aTh9_5awFxXpEJI-RxCPg4t2qqQBupUWmRQ518iHMX6ajdohs2QpwVN6X6vRTjQCEcEcejjBoAaXLbQJ4IcWiW6ZwyVaBZBsnotUDbGRpOwxfoFaw4G9rfafQ-TwoyF4jFj34ShPO1pW6HjPFVbAy-_3dIkiT8dN0FLjrkqYXe13hy2FacWsP55N3joH6XNSw-vskwe4wNSDY7HCbCvJr6Jvjkkn1WBynJu1GMwnCaMNEXOz5YusgoCQ0T_mUy-a3kBLGcJfg0LwE2NmRfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=XH4EC5trSA-yPwgKGlBrs44pk8sS1CDmxiSiFi2AdSu34jRvRHghv8EXPesAYpxh9jlRQS4vvvWgE9NS52ZOuCNWgFPN6vsbNX-DyPv3DpRdeIC9tVcl2aGR015mY06XohQWvKZoEs0Ihf9LtfdUwACTKRW1beWJ9pbQiKDYevU3Vtspo0YR755dvFqkYCPLBX53DUlk-eqNzm7jzRztk5XH0FRu64TzZR5QNMd2Gyl72hO1DA4VLWAfzPY-21mx3ZopHFX4U6ss2sXkris8kt0mHj5fMAA8_m6mZMZHWxRv7XH-1zqWNpCdG4CZi5F9yKkz7TA1rDNPLEgRCr6qjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=XH4EC5trSA-yPwgKGlBrs44pk8sS1CDmxiSiFi2AdSu34jRvRHghv8EXPesAYpxh9jlRQS4vvvWgE9NS52ZOuCNWgFPN6vsbNX-DyPv3DpRdeIC9tVcl2aGR015mY06XohQWvKZoEs0Ihf9LtfdUwACTKRW1beWJ9pbQiKDYevU3Vtspo0YR755dvFqkYCPLBX53DUlk-eqNzm7jzRztk5XH0FRu64TzZR5QNMd2Gyl72hO1DA4VLWAfzPY-21mx3ZopHFX4U6ss2sXkris8kt0mHj5fMAA8_m6mZMZHWxRv7XH-1zqWNpCdG4CZi5F9yKkz7TA1rDNPLEgRCr6qjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsakrH7XW38GbE31L0R5khWaRYMokymPkMBHzNyv6eMdJnzQm5bJBYq8k8Sm-Re0lI4ZpMAmfhFIjzDvRGQL_jMUTIQTOSZcCXhREs6RcWJvtBBgE3SVYT85OepMOP215R-Ivv9IHI0hBajGWJiIOVWp7z8WwuTdzMeh4fvS-yGvHlX7CaIZG2r3a_GmOrDXxHGk8Wxl_FIPyM3LaNDNtS7eTsgBRlkUYwd6RfVoUwF2r0kKbaB7MK5DcKQGl_m7VMYjYuhm4jNNYqxbSSnikq6kW2kHg_5qLRqYIvQfSn-1lOl8Y3FbOyr5IkWKHp9jUMJZuQOJGOG-aC9AskHg6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t70dHqm4FwMJQihbQyPVpAcKO5ZUeAzNZi8BDm9fVxVLJqOfH_Pc2q3HuzpbbzFhh7sNWs7Ij_x5xMWbhbaX7jFcoSIuIxIx5uE1kuZjmbO3jcEngEGmxvRyjvwX6Fu04oXbN3gqtQEQR_vwrLxtOqEsNrc-z9U17r-fUeS9yXGxY3Jge8V_mHWFUv_TpyaUVaaNdLVuj03GTqjDcNPV4DQ-r1fpjHVgSrfgeIHfOg7vzzhvRxM0zQeS9xxz0GbNr3YXpCsEteWhuPRmGJKm1PdJ78mZ2EcR0VltnymTWHM4-DksEYAj_hWZs4SiyTU8BNuUZabNqHVI7Z_ofrzi5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIRu41waZpoP9_shifHGPb70M4KQZ4V7TXqKDUPmrPJkB2P4X2HZ3IXySDS0kaykGPpT6H3OGvhWgx3Se4hSEkrI8W13HX6-AB2QFZm6Y7xaa4YtoF1QvLtP4OtqEhbeECM9kGXXcNSvDaN-eiE0arGi6EJKWzKn0-jPtfQ7V-TJaRa6l-oXyOfExcwOAQ8R1WDh3QPxko7PkBjS_eEBisycSPcim0sx2P2AnQQUP_foSEsDPag3NDag7bFNmK4bj9RNdNzZVYpa29XaQRZZLU4SMTC5jqnUbTGlFc25cPpVkSqR-qLqLQHfsQ8bbwzxrHdc27Skl_-R3iN0E7wpVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOUfc7akeSuIp4AAPuqfT3mtJAEJfrtbtEbwGbplCe-amtq0PNan2_L_QBEbK0oACoEFot6GjximLpRD8iHa9805zgBIqtzYkAT_ZVeB2DyA3n0LNlO2LysysS20Giizi3BYtwl--yYkY35ROLDz-7eRLqqBuTpbqSvSON5yRy2rc8CgFMw3Y19YqCDwGSbUiag_oO2kaZ1qqGOsf-_RKVuQPQTvnVLLwp3KKm8b3hwlRZ5Db-_LW52VZ3Zv0-a28_yL9344yyn9YrqdHNS9ZvoLdxLnt_gB3yZaIwgYANYxVYyqgz2NWmgnKBxXRnw77jn13-Dkx4vUszdKbDhoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tS61GAsxSDnHVh5FBn0OZbU0IjdbTRXOMzl8gqDInWw7xsKz_yh2J7_1-1yBF0AbM5YHo_0JrEB1RIWsm8d3XkYkKQb9_VgelHdN9gu2-bbb8J5Dx8MQx1uu2PjQeldiczdu1SKZUsaT7MpZ9Qby1nszQX2Y3nWl7PLf29dB6dgdp84FwTG_kmDctuzNuhXDE-4Y7q4lvsFTAdPNuGsW7xiNHzQumBZxPFLMIkWmYbLY74Wh-q7z4w4x1gbg7yCsPh0jkgLFgoOo99_fRk4JfkT3E2ZQqx11msViIOwDy0ufr2Ep8X_flNPee4XNOW4Chm9IPU73q-3d0rZGiOQHcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU6mQQrVXOhp5rqrXMOcQrazq9hi5Zl8EDKjJsmyeg0G2A64Nekizn2oZzLX-iE-c_lN_ZWw2d2-ouO9XhcRmMdgEiu9eR0KloaYBiJTX5ZusvsNlgqopBSA3rZCiQqEtvrEYXcDck1EUMX-3xRNWI6D_BpjLZu_VHRshAJwrJ4_KI93__K32zJ_EIca-sYNFN8z3JT0L2OYxoarNc9fro566NgEeCoSVcDrFEZdStLkXXmwGk_kR8CCBx6ifnXl_Ild3z9od3sFlkTuMdR2kingWcpLEMNGW63FY0hwKWcyeyh1ShOBieXviOcVQBtc1gIpte2PGFIQYCL6rYhoGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McxvY2vpsjuD2RS1KhW3RhwQKTCu3aY6V3OrEGiuutkvS4qULK3Zpwghd9ZBFdqpscKbW4PvLnddcD9R0LyRUvaRbyq_DSLcODzibA4smqoEZcCNpzisgwZlkHmQEjB68WEOHjIkoosmBWlJ0ljxfhQUaJMyF2vLmOV8vwYEIQt3bL0WdxXumTml8xoLtHRoJ8LmCeDl__0eosEv65qN8LlSktnsVC0JKD9zyughsXxsFOClaWotPMhMyobult8WrtAeIy7rruNJZPSuRYHVvqk0lqnQEZWlk_sWyVSbyF9ljlMBobvFW3ISkA74nUaf8fzAymClA6N1YlbYscIO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل خبر از حذف
«علی موسی دقوق» از فرماندهان ارشد گروه تروریستی حزب الله لبنان داد.
علی موسی دقوق ، بعد از سقوط صدام حسین، توسط جمهوری اسلامی ماموریت یافت تا به عراق برود و به ایجاد گروه‌های شبه نظامی شیعه عراقی دست بزند.
او از ایجاد کنندگان گروه شبه نظامی شیعی «عصائب اهل حق» در عراق بود و در کشتن ۵ سرباز آمریکایی در کربلا دست داشت.
اسرائیل امروز با حذف او،  پیامی چند جانبه و جداگانه برای حزب الله لبنان،
جمهوری اسلامی و البته آمریکا فرستاد!
فرمانده‌ای را حذف کرد که نقشی کلیدی برای جمهوری اسلامی و حزب الله داشت و آمریکا نیز از حذف او، نمی‌تواند خوشحال نباشد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzn7v4w_7efgSycck8PJCoJ9oCoW3p8sbdFJRQ4EOcDbBpVS7l822beQk-dWk_cxthFR1I9G4Z00-hH4WP4HT6P95JLGQAr-iN_DzVLuAP8awGFuRyqQGz6sq7OlQZfzyNnVBlldmjOC-L9wbFjFGn8bKSutLYcmvAdfLAVV0X64eAJ7G6iiFIeOg6IfB1JY6vwjTwJYXe5GT16lliboZIC4KjsTx0r6cnhURhSKyRNO2TnMp66FbfYt-tC9jlIudoN4Xdn7Pc_mbO1JqPrZvdqC6wkvtusx6jA9D0K_N208vdMTfNFwNWFb1-zgrt6itrczsulUKcb9zUpt232m0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=XprfCJWqJHC9BL_4OTiQiXv2oyq0mUsBCMUHQfj0jfyH7WJGbq1icyreJ0tdv8yxGWBle6im7qnSuF3OQ24p_ZhYFl9-iWrJAqmeWDPyM8t1jSTqfY4PWiToebOW97AucmgmsNwnuVRD1S3rYMOnOdSbmPzVo05MiHDSge5qnA-TsWbPcTETPdhgDV-_00BV2A3hnZ2QMOK9pDnzUpftpp15-OfAFZZ4aLC3hIsMbZSDE87GF3uGzXAOkD6l52YC3EMcdj46HRFaGIUk9sUZG7E772ay0w8S709BbsKQKRFjjfSTcIdHj5KJ9ndXSmevU4baPJZZWO-YV5CJQDgw6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=XprfCJWqJHC9BL_4OTiQiXv2oyq0mUsBCMUHQfj0jfyH7WJGbq1icyreJ0tdv8yxGWBle6im7qnSuF3OQ24p_ZhYFl9-iWrJAqmeWDPyM8t1jSTqfY4PWiToebOW97AucmgmsNwnuVRD1S3rYMOnOdSbmPzVo05MiHDSge5qnA-TsWbPcTETPdhgDV-_00BV2A3hnZ2QMOK9pDnzUpftpp15-OfAFZZ4aLC3hIsMbZSDE87GF3uGzXAOkD6l52YC3EMcdj46HRFaGIUk9sUZG7E772ay0w8S709BbsKQKRFjjfSTcIdHj5KJ9ndXSmevU4baPJZZWO-YV5CJQDgw6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=TmhbMoF5ECxH2awGGN_BZOIMOuvVufOQKUjmF2gnuGGq8Wu3sdCMxcynPb4AeOmTk6mRn9sMN68NJq6ITpp1gMOWn-XtCsWNuorM-Cif33zpRpsEduSNCaGNhXynpb9dnPE25H1E3UV01t0pV4UCPdAzc8J-rLGx9TvKYLQTuQCDvppoOtbTOUc1xIBDrJiNxiwXlD-2KRYMfIp9XD82QqhizN3ZyuyuXEB8pCpI4kJ0AUz6dcu9Fm95eRm6hK8pxnzzsQv1I4dXlSIrOulh9QyI9pPaNERIEIN8uihCdUNsDkDlMVTEi24Ua9OlXkQQgPiscbA7u1KK4nEUgF75Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=TmhbMoF5ECxH2awGGN_BZOIMOuvVufOQKUjmF2gnuGGq8Wu3sdCMxcynPb4AeOmTk6mRn9sMN68NJq6ITpp1gMOWn-XtCsWNuorM-Cif33zpRpsEduSNCaGNhXynpb9dnPE25H1E3UV01t0pV4UCPdAzc8J-rLGx9TvKYLQTuQCDvppoOtbTOUc1xIBDrJiNxiwXlD-2KRYMfIp9XD82QqhizN3ZyuyuXEB8pCpI4kJ0AUz6dcu9Fm95eRm6hK8pxnzzsQv1I4dXlSIrOulh9QyI9pPaNERIEIN8uihCdUNsDkDlMVTEi24Ua9OlXkQQgPiscbA7u1KK4nEUgF75Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=GgZacr5AZpWD35lYlgFs61kMrtIHvFD5eFUnOTxgg7dV76OaikbEG13APGDHTfSsYr660dAJCdnDGUv-_beUMthx8NU6TGLpr7_rXSdbhTgv-vUDWSJhSj7OyQLVvNH6uJsEQ_bSDbp5FpKY9HNkJ3PPqKEjtuS-8z0ccHFTMZa1kIebAtCtCB0SjUoF7vXR_RazUDjEB7VCP4k2uR0U_GqUZfHzhiZreAUVvlyPYMNMDRqvP7z0g4RN0KiIw9-v40ippCPkpm7zKcd4FyTy5i4c_ByqAfZ8xmyfZD9Eiqneu14JLHCvOPWIw7VZDgMV7JcQcDY5m0VrimzyvvlfBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=GgZacr5AZpWD35lYlgFs61kMrtIHvFD5eFUnOTxgg7dV76OaikbEG13APGDHTfSsYr660dAJCdnDGUv-_beUMthx8NU6TGLpr7_rXSdbhTgv-vUDWSJhSj7OyQLVvNH6uJsEQ_bSDbp5FpKY9HNkJ3PPqKEjtuS-8z0ccHFTMZa1kIebAtCtCB0SjUoF7vXR_RazUDjEB7VCP4k2uR0U_GqUZfHzhiZreAUVvlyPYMNMDRqvP7z0g4RN0KiIw9-v40ippCPkpm7zKcd4FyTy5i4c_ByqAfZ8xmyfZD9Eiqneu14JLHCvOPWIw7VZDgMV7JcQcDY5m0VrimzyvvlfBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=rxdYIFQOdwqRrUWjB5UkfSsB0jWxegyjE_WJv8E2pvwpNyt6CDuIjSmZltORd3v4CdRap_PMFAYqhhEGLYx7thUbPpRyJcFppuLXOCnkiOPPFkz0tKsMhMSfbtDY1SEO2cE3diLaxejzzu_xcaCiluT2epxSTB7jw38mQlW0H0kbuKQS6pqgQy5EPNUmPVq1M9D9pRKbqgmMrRpDKPJhN63shX75gkMcCporFpF-HDdSVZzHgBDOAC1K4k51weN09wIlk5Qe0TMvyxLMN07qRTbWXmdIKE4kdDtABz_OuUa9mh2NFutOuaI5UdUxETcai5G64DE5u_XhyBiPOQ_Auw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=rxdYIFQOdwqRrUWjB5UkfSsB0jWxegyjE_WJv8E2pvwpNyt6CDuIjSmZltORd3v4CdRap_PMFAYqhhEGLYx7thUbPpRyJcFppuLXOCnkiOPPFkz0tKsMhMSfbtDY1SEO2cE3diLaxejzzu_xcaCiluT2epxSTB7jw38mQlW0H0kbuKQS6pqgQy5EPNUmPVq1M9D9pRKbqgmMrRpDKPJhN63shX75gkMcCporFpF-HDdSVZzHgBDOAC1K4k51weN09wIlk5Qe0TMvyxLMN07qRTbWXmdIKE4kdDtABz_OuUa9mh2NFutOuaI5UdUxETcai5G64DE5u_XhyBiPOQ_Auw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=A-HmTZpqdrg5hCoBf55KewS2GVu1RQdcymjMdUrhPpJCZJQRwoJ34qLc9lJSu9iP-ZCloTByEFkP40nN8V6_8kPiWymi38xncASGhcZkQaHS4UZQPY-H55Rqd4Svr_xnnHwiVGe3xHHmJYj_Im38otx0MIaXTg9dFaKwdwUwnPzRIo7ylvu00EawwEdoHhtGEO6nSny5BgvRRbKzA41YLL5MMipd3AHczHpFDhc7XeqS4IyGdIGyxTkU4akcMgXpnu-MA1nmB-Ca86HvV-SqwrEgfWpDbOUPDArlevpKtwj6QJ1KEjBo8gUlWGpy9kYu7dSsUodIlNdQ1MPHf1ilfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=A-HmTZpqdrg5hCoBf55KewS2GVu1RQdcymjMdUrhPpJCZJQRwoJ34qLc9lJSu9iP-ZCloTByEFkP40nN8V6_8kPiWymi38xncASGhcZkQaHS4UZQPY-H55Rqd4Svr_xnnHwiVGe3xHHmJYj_Im38otx0MIaXTg9dFaKwdwUwnPzRIo7ylvu00EawwEdoHhtGEO6nSny5BgvRRbKzA41YLL5MMipd3AHczHpFDhc7XeqS4IyGdIGyxTkU4akcMgXpnu-MA1nmB-Ca86HvV-SqwrEgfWpDbOUPDArlevpKtwj6QJ1KEjBo8gUlWGpy9kYu7dSsUodIlNdQ1MPHf1ilfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=m54h0ZGPU524GIYb7JqmxYyRFMpw5b7SBzbXzCrMxxdPN0AJjwsgi92DCAIIp_nHJob90mrIw_wPTVDsYThCfyg8yEkl6dUhuuq1fEc0d_i6U0SxFT0Z_DfkjYPPhqHGW5SohfRW4c1o8MR8o0P2Q-JSF1fKqJCofZbqO_BLtJvaByZlLmU2ri4pvoXbBnL_r8GD0bY8OXB2CRVWVx_XUjODw_uzx0p_mrqN2rcWdSfW_1amSg_pmiGAnDafXNxr2j50o-3LDfoDF5oStJRgTUnd2GZfMRMhopP6C-oWSj8pPi2hDoAmoG19iHWujIJFAOWOfYSZNvEcoyuc1lUVZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=m54h0ZGPU524GIYb7JqmxYyRFMpw5b7SBzbXzCrMxxdPN0AJjwsgi92DCAIIp_nHJob90mrIw_wPTVDsYThCfyg8yEkl6dUhuuq1fEc0d_i6U0SxFT0Z_DfkjYPPhqHGW5SohfRW4c1o8MR8o0P2Q-JSF1fKqJCofZbqO_BLtJvaByZlLmU2ri4pvoXbBnL_r8GD0bY8OXB2CRVWVx_XUjODw_uzx0p_mrqN2rcWdSfW_1amSg_pmiGAnDafXNxr2j50o-3LDfoDF5oStJRgTUnd2GZfMRMhopP6C-oWSj8pPi2hDoAmoG19iHWujIJFAOWOfYSZNvEcoyuc1lUVZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO90I7NHnnbibG0KwlEm18B-T57vtwUEId0xkAaqe5-rtzw2_6qEHyzNiJyQWtVbLuCNvYdnteHUUTkjLXEEbhgEV0IwBtuP7MirKpw79MAO4uq1ic-bEgbe4f6PhsNTy2YeIP9wgH6m_Mkofth5_DiilQ5NPQs7Bb7adCGB3NicuK6iQuoy2rMknayOdlZbWoon_ZFZht_P-EiM0qSaLfaqMgLzbt45cQXkx6bJz43GCWDglUutKEnfbQr9NWjbnUpFOoMWOg0Ti-_05g5JIbkynKGfTUhIvbCsagoxm42E-b2_ll39LFzQEcsN7zb_J2We449v4uJRycT6DWLRM9WdY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO90I7NHnnbibG0KwlEm18B-T57vtwUEId0xkAaqe5-rtzw2_6qEHyzNiJyQWtVbLuCNvYdnteHUUTkjLXEEbhgEV0IwBtuP7MirKpw79MAO4uq1ic-bEgbe4f6PhsNTy2YeIP9wgH6m_Mkofth5_DiilQ5NPQs7Bb7adCGB3NicuK6iQuoy2rMknayOdlZbWoon_ZFZht_P-EiM0qSaLfaqMgLzbt45cQXkx6bJz43GCWDglUutKEnfbQr9NWjbnUpFOoMWOg0Ti-_05g5JIbkynKGfTUhIvbCsagoxm42E-b2_ll39LFzQEcsN7zb_J2We449v4uJRycT6DWLRM9WdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdlcHdb1SwJNuSC0enmsL9zg0WGRcz_kZ1pyruchv98tpt7hL7RWVVp3QZw1zrBatpzK5ONsWZQPdL5mOpcOgPYrGF5gV8Fb5YtVlTH8KhF29PFDOkTzFPN5d4-aWrxjWf0jLcZLFUsihwsdFPLLD4dO5FgOaN5yEaIsboEVXCN_h4rmZjvwocWJaYOKUXnsrwkc9UpRDq55QEukh3X3GRohvbT-xOjn7KIRkINCTSJYsYkFc69y3_ehoujRq7_34rDTFqPSEVF0x6GFwhqO_Wob8VIXQmF9O3SH1lbyyxXBO_AYJZLNKVOdIJfLSPcADC1kC6WDghPXwA5WVJ11OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=oOVerKWACEFUpBtWSv0sc4h72lH4eWkx-GtIJtVGVFKCeO_owJ5bLW_HL2Hbaf9M2zImXhdPEliEprhZhjQ4JhqNjc_INAY-16lcQoha_lp7SYDEAEn7O87zd64BUfdELw_lHIzAQLiKEpHw2pi0gt0jReIhz7zD51FwYd2RJaYl2q4-Hn_dYpRqrVjA9_T4mzrGaQIMHr3OJdKSHDDrY3XGk2WqNqB4O_uW1IJ5ecYoHSOLZGkNJGbIwD6QzY1a10JpnAeZ9jhVEa08vq_Fjm5FLaEl0MTSLibPIJtsPIjnEY5cPyd92eHAmFAx5rcUw0gWkPn9ZRbaRA-kynxnbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=oOVerKWACEFUpBtWSv0sc4h72lH4eWkx-GtIJtVGVFKCeO_owJ5bLW_HL2Hbaf9M2zImXhdPEliEprhZhjQ4JhqNjc_INAY-16lcQoha_lp7SYDEAEn7O87zd64BUfdELw_lHIzAQLiKEpHw2pi0gt0jReIhz7zD51FwYd2RJaYl2q4-Hn_dYpRqrVjA9_T4mzrGaQIMHr3OJdKSHDDrY3XGk2WqNqB4O_uW1IJ5ecYoHSOLZGkNJGbIwD6QzY1a10JpnAeZ9jhVEa08vq_Fjm5FLaEl0MTSLibPIJtsPIjnEY5cPyd92eHAmFAx5rcUw0gWkPn9ZRbaRA-kynxnbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkajQl94asBtqkal_eaVushspchv59SA1W7UGf16ezJ4YySd6WtRCj-su5WmeyXUntoejSdS8TmGe6oNIq9RzrEaJ3ciSryGJfH1s-AzXGofaZlYYgxrOzHxaFcyCH0Op0DMIJoPiycC8DpPwUOftUGHICMD_cZ52zNhqnfE-BHz8LDiZXDS51O2p9Bqexa9o6W_maPKR8F-PxEwRYg7Er2q5i19-ylJtk6Kn_vH-Wxo3aM3P2As5Zd6L_F9s2GJOLMeyfAtmuCG1do1PzM9EimitwhbXWbnofDIIxlLnVgbMtaQpEv05Pfm7ERGe6MIPB1bG4l6nokJXeNyy9omzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUIj2qD8Ig2A-H_hXqNO8gUKAJmv0CqTK9PGoU024r9EvVyuvsT-8IMpXi6ZbvqCtp5DHHS3En_fRmT1Fdei_QQgpFUaGdXwfI5lV0BRBbHybYyRSm0aw84IZvQD9VkbjWA6E5qtbK3yR0ZGzX__wKS-ZAe02thFw74rT5TF1Ocx5wheDHmS_fJDWCz8lBkZs4W6gRyPdsaSX9365l_RAaJGd16h0TjxKTe7pttV0Gq_9nCc7RYNSdY6EL9DDCSS12gS9c3R34T_-MK8MH04KXJECvJ5RQQ4urVcSVQ2PKWkb9nPpf81ro2_ZieKkqjwWhxw_4iShlI14iuBbkyepg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzIFqsD7Kn9G6PZpP34WuzqGkS10Pv3p4njSTsLdkvBIm22mrdGfag0x1b3zKPsK2Kf9teLKaFQ_j5FXRBL_USTyiEe8-anzlRkXDuzgqSiAZdVG2fsIFvXI1kxFtT7OCSTn2HAkVCEWbhF2nbpYt8DZqhMljeaqM76SSbbvYp06-WpggxwC3YSaKIj7OcoSS8GPiNWJaQSeXW6rx1jU5PjW8pVBXM2zndqrL4VGXrM-HWwKFV6XsdBkQLWgHXYbCJhzkCuRmPmbcyQbSqRlMhysN_RjgQ8T5VOvG0B9EnBU12ZZtE53_A7BQW3mIhzgjl5ATr3njBBfk1puCMhdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=TEAZIGDgRbkxydNomsHlZSxZLrrgVhX3vr-CGp2tZwCIhXs58XBJL9pIA9WDgLDlbV-k_i7zlRpXXy1RkxYs9tf2OtbVudaZ5tcGNFKhFcoK_I4ypIeUCOicnv0jxCIJRbWaA1UOXweAFk3gSzAr_M0qw_--s0habkPbQL_5-eGSxAjUebDKZCRVx5927VXMdu5mDE1eGMd3VfibHOcn1buUA7bc_8s2B1mkfa2LXrCvoVs3RVQHJRQkWSf7EpLuvo4b3LkRNMuJ4Qc49d4a67tJdd3DRvxBshwmP3GJk71QceHxpBvxy4hdw2xyEsebi9Js6Jpar_JSwheXBAuQ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=TEAZIGDgRbkxydNomsHlZSxZLrrgVhX3vr-CGp2tZwCIhXs58XBJL9pIA9WDgLDlbV-k_i7zlRpXXy1RkxYs9tf2OtbVudaZ5tcGNFKhFcoK_I4ypIeUCOicnv0jxCIJRbWaA1UOXweAFk3gSzAr_M0qw_--s0habkPbQL_5-eGSxAjUebDKZCRVx5927VXMdu5mDE1eGMd3VfibHOcn1buUA7bc_8s2B1mkfa2LXrCvoVs3RVQHJRQkWSf7EpLuvo4b3LkRNMuJ4Qc49d4a67tJdd3DRvxBshwmP3GJk71QceHxpBvxy4hdw2xyEsebi9Js6Jpar_JSwheXBAuQ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOJGfoRsSVDS2vjMemE6GbxpuMvRPVbszHgHfjROx8CUOW3-pVZPPh2hJANr9R_XXZnha8XF1O-r9IfdignDEnyi0ELBI02lJHBiM7v4yXxovvQpkCxw0f5al6gNfgYvNRYPN_aBHSjJv-ZWAcCx9xQKlDfMu2pI0quy_9EIVezgBqFJduqJmvDHF5udi3GSgxuFZMsADgiwPdE_gh_iNrk07E_UbM7191a9y2ZZQ06iKAmZogVlMJAhq_aEjEieTLQZuWuNqGnTZX_th1Hbg_OHxunvNGJrYn32lhum7Hcxljgx_0ljZLf8KfbqzCj-Z4Uk1ZWB3okRDqfsQxxJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPoSsdSPCR_3HKPPgXMNVYfREQL647cd-17DpkPYE6dCZV2-KvLQDDEPqK23xFwclCXRuohHd-ErqvdRYbpwn1zhFi9tqpuWI159gxJAnFuFdi7UqRdcuNccRqyLbbakJvvVsajDCfp61tDYrV6kea3-6_2XJOFeK1HRz4QoW3su9Kp-jQWGAi1xQW3TFw8jGdhK_T2zGrEoh1AKY7qyVPlzLJ-X8Ec6H2UVZoaHx3xoLb90_3OvkvelHf68sDgJ63eaTatV4_yXeBOn7RLL5PWN8-45EdfyMZWERDb3ymhqJSGgHYjq3KCoYv_yHIjUqOHhS3w6arOpgbw6yMwb_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeZFDGsBxkNVXc4pm6VIWN21uEA7LWZ9JGhKLE2ILYr20LCGJbSaMC4E6odgLUIZ-05tHVG1jK40U8dAX8lP3IzUWTQ_-WVs7XBXAS6NdAxz93H62zPNn4yLXmQId1d5zhzu9BTwdwT0GGcBc07KeJQm7UjxdmV2xMO51siIOhznIN9OMUz-Txm2sHelF_XLtRaLhBwjqSW2z9Ttww3_QIR86R8frXWlbjAWPCUCZoXG4l3mqi6cdlRgvDednu42PS7z0Um3X73t-gCPePbxkQRiXNoWWo2yUIDJXsCadJQVNo4O5fjXVMQgMhXazQRjs-H_uyynfdRBtVNs261emw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmKrQv46HscHSAIVgcMbSAOrdKQ3SjNMRrBkHEWkMjABXtED_uiEQxOapp3Abu7P_jvHWSQv4Ui_sW27l4cXHnIOVwH6J2DgTpKyyBV4EAZYBVhlDTD-PVw8yqg-MZY88WuBcYiDJgbvIcd3fwQ2ALiOfFXnO5JrpsPsgOseZM_vwuak6kycm_svt0nsDW9TrpIS-bCeXruJYRYbrsk33mB118d8p7QUadvFherRqFClwt9MtGVl4Wfc6KkD1K1Fa-7aekidiIMF0TD7rBSbwMHXnurRanariVgq445OQYmqf5O91AWlfdJg5AwYJTSQYHirzNxivFe7t869sD4RJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=HO--E-akgHI8uroyyJ19tFCp07j1qnaHNIFc6cg7kt9YPnHdzDDNa1vAM5wS4lsNfYgrKr5tzlCFXaXqHFxxM-HQDKMumArfE1KP4qV54HSGkHUNcLXBmxdpz1j--UuSNnoT1rjrTbQnk2CivanX_DdDoipBfsG_KkXD2124nWXmVgR9t7MMlNK8-Lq_GJKNjFm-5WP0_7AxnVy-NYrx0ROf5-ouLArpnP8b7Ne5fIgm9uLjtFVjehVR3YMGW7NlpkLaTtExkJ0YwWeC5GCXRlEgwOIFJDrx99FYBgtgdon-xC0Mdi1WVFjkL5U4mEIlr9-DkaAnxgcjtTZ3kZpdBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=HO--E-akgHI8uroyyJ19tFCp07j1qnaHNIFc6cg7kt9YPnHdzDDNa1vAM5wS4lsNfYgrKr5tzlCFXaXqHFxxM-HQDKMumArfE1KP4qV54HSGkHUNcLXBmxdpz1j--UuSNnoT1rjrTbQnk2CivanX_DdDoipBfsG_KkXD2124nWXmVgR9t7MMlNK8-Lq_GJKNjFm-5WP0_7AxnVy-NYrx0ROf5-ouLArpnP8b7Ne5fIgm9uLjtFVjehVR3YMGW7NlpkLaTtExkJ0YwWeC5GCXRlEgwOIFJDrx99FYBgtgdon-xC0Mdi1WVFjkL5U4mEIlr9-DkaAnxgcjtTZ3kZpdBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز میگن دشمن جمهورى اسلامى
ايران اينترنشناله!
همين چند سال پيش تلگرام دشمن بود!
حتى «روح اللّٰه زم» رو به خاطر داشتن
«يك كانال تلگرامى» ١عدام كردند!
توی صدا و سیمای نکبت‌شون هم گفتند :«شاهرگ رسانه‌های بیگانه»! یک کانال تلگرامی!
قبل‌ترش وبلاگ! ستار بهشتی رو به خاطر نوشتن در یک وبلاگ کشتن!
قبلترش مشكل «روزنامه‌ها» بود!
چندین روزنامه نگار رو كشتن ، دهها روزنامه و نشريه رو بستن!
قبلترش مشكل راديو بود!! دهه ۶۰! امت حزب اللّٰه بیاد گزارش بده كى توى خونه اش راديوهاى وابسته به دشمن رو گوش ميده!
تاريخ جمهورى اسلامى همين نكبته!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggbVkrZHxWbIAbN6R_OC0JGP2kP81l7nbwEGzXzMJujED0oD3H6kcy_18q-VB7of3JDp4W3OawEAGA6hW1g7RZZqycdXDrHXo-OKBO2SBjmKn4XALsCtNlFtAtEEnX5CEMPXi4fDnnaLbNZymbat44Vh3hrNPxRHEVqrdFKHBHhLhOmcAnm8ai1DFqMKmX8NYiMjVeohVcZDP9WEYsumlO2pxvIHjjcRwSmXsw-ffx-1sa6B4CW5C4oxe0Ftnvef9aUF55nd4wwMEJ9xVbvTWxnOyzn-Va_2dFA1GPvUY9rbpZudG1qWaYEc4wzZsQgqdXGwq1NlQ6aJ7KGT8vmdwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن ترامپ میخواد ۱۰ میلیارد ،
۲۰ میلیارد از سرمایه های بلوکه شده ایران
رو «آزاد» کنه،
و این رو همچون یک پیروزی دارند به حامیانشون القا میکنن،
جمهوری اسلامی بعضا سالانه
۱۰ میلیارد ، ۱۲ میلیارد دلار تخفیف
نفتی به چین میده! از سرمایه‌‌های مردم ایران!
اون بلوکه‌ شده‌ها توسط آمریکا یک روز،
دیروز و زود نقد میشن،
این چوب جراحی که شما به ایران زدید
هرگز برنمیگرده!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu5YYTAX2qy7u_0rZqmnMsaijghZQj2RBo3oBpcxobNSpOlhDOitCWvc2skkLeMUM_cMdhgRTugglvcPkO5sbuw_e10-9g5nCHBccF62PE4xq3AH0t40l9rBS7sibAt8XCcdnO1Y8_JsbqJ7Wg8JNdpLkXUUgU4fGCvtYa7OirUTUcV_IoEy5WNt3QjfvQDP6u3F6FhnMT_o6z7x7UCFpkiZ_c0DtvUD4r1MzfSpPoqhXGDdWTb7wB9NBJEN1DWjVLuYnrDqsHbecnI1dgqaalysWBDiUzECrDW5mW8v-AKIqMisZQBCz6RLqouepY1Dp_HsI3Ce1WybN3Upo5PafA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=q61TB36LOM7Dm_K7Yr1Ba7tCuWLDCPMoZVcPW1qvLxxysMr8PPoDQIBvCqvI5Fj7FJBbVQEhv59o46RjM8U1IWFQpZs9cCIO2mpgIIKdPFOp7wH0vSHHYXoumtw4dO0T74XP44zYqIbjq0EyhYx6ceWhA4X5Iyod0DMD-eHtbkxbrr9By2pD5ZwOZJU2z0Y_Fhx0-9wEDRDbpsUmQIMKDJG0FxvO_6_KeYC0U29tstDIeuWQ01cYv5KCNc1uOw7hywQFfQPJoOm4KrFkWb7ThjRaUGCHA_mWkU416FCiiw3js47ZAbHyguHurfJ-OxFxeCN8Sq5oga4GXSmpg222DK83Y3pYpxIVk_iMHMsb_Cy67v7I4Xmx2MQvs93aUOdRT6ai9lWGcaSAflV7eBvdTueg1RFdzmzVg-Plu6EY4TDdZvzS9dlp91n-kPk9dL9nYFXMKbwI8TXMqjSdfC2tgz507xV51Gg9hcTqVtFAXRP6-BNF-pWWHij2OakOIXGlVV3sYwVguwGvBVXkG3gLjMtS6pVaXHspYBM_brfQmhvbb9XjyjptkGKdgNDsBjWT5KmaSYuKaVEEbBaOZTGt35OV0xOiGe_c0-kGHWeEPfG2psYK8RdsMcUQf3Hc-4a-Olq-XNd48X4FZT6i2UXReRdK18VWs4j2-gePsT0-Au4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=q61TB36LOM7Dm_K7Yr1Ba7tCuWLDCPMoZVcPW1qvLxxysMr8PPoDQIBvCqvI5Fj7FJBbVQEhv59o46RjM8U1IWFQpZs9cCIO2mpgIIKdPFOp7wH0vSHHYXoumtw4dO0T74XP44zYqIbjq0EyhYx6ceWhA4X5Iyod0DMD-eHtbkxbrr9By2pD5ZwOZJU2z0Y_Fhx0-9wEDRDbpsUmQIMKDJG0FxvO_6_KeYC0U29tstDIeuWQ01cYv5KCNc1uOw7hywQFfQPJoOm4KrFkWb7ThjRaUGCHA_mWkU416FCiiw3js47ZAbHyguHurfJ-OxFxeCN8Sq5oga4GXSmpg222DK83Y3pYpxIVk_iMHMsb_Cy67v7I4Xmx2MQvs93aUOdRT6ai9lWGcaSAflV7eBvdTueg1RFdzmzVg-Plu6EY4TDdZvzS9dlp91n-kPk9dL9nYFXMKbwI8TXMqjSdfC2tgz507xV51Gg9hcTqVtFAXRP6-BNF-pWWHij2OakOIXGlVV3sYwVguwGvBVXkG3gLjMtS6pVaXHspYBM_brfQmhvbb9XjyjptkGKdgNDsBjWT5KmaSYuKaVEEbBaOZTGt35OV0xOiGe_c0-kGHWeEPfG2psYK8RdsMcUQf3Hc-4a-Olq-XNd48X4FZT6i2UXReRdK18VWs4j2-gePsT0-Au4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
