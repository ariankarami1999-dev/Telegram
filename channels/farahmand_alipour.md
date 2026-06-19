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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 13:44:06</div>
<hr>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh99LCTwYnsTyTnlqFnvtZzwY5LKBUs8tTka5xttXWkjoDPPNXgaJhEjTmSEquQmmpNVgGRZ5uF5wOXBghdcCF2X3I4e6LHGs5NXb5-uyrYaTspnsLUPYultGCPBacinXcqtAlJXW8fGP8wM8eJ49mFmqRGwDvLDaK5yDW6IHYG0JVpryuCocGJuYXhnx6dOkTtCKnYt0hk8tEPuocITjMRIWRXil1Z2X6IEgb1LObvmaE9saJkOqIZq028DhaPUbbRuwPVMRXoMC5GXtPeZn5G7lET0e61ncN9LXVKCaN5NTYOsV1id_m9lox1Hp0sF4sOjfNc9LByGgh-Io986cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNaEnmYixfZUsj8qZho5tbGaEq6mrjKsxHkhcmvm6c_7z8cuIt9S-6wgRffdj-Mynsicg0kx3qS6ue1jExpkuOSw6X-waoMpUXWGNQ4aUsFdGnkxQoPnz2FI5kLJhvo2pTVbp5S9LSIzrkBH5NKKPiQXy4guMrN4yjxduYxp9i6uatijnb8i19-_5paAl5lKim_jw4NZxzMICNXeEb8YhSxXMjQ-n0YtDS7HLmVxIB9psZaMJkoWmk7SoHbtx1YyzxyeAUM7IohOPyDPtQJ7OcTdI9ru2wzeoPhv6Z9Wa5QuQ_kRdUWRS4_30Kd7Rj2O_YEZvAkcJRiVIcHuQAfwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJ2zZxfnkMNDITMtNtiJdMI0rBt_cuIKIMyAfQvAN5fPRtxVpM5kRcDSXjSyoGTbd_xm6-Xz9fsQVHPjWis7vdp8xQyrZ22GVXohviT3yleMjWwwZO8Uo5KxXUK4zoQ6vDLAc204UQg8ZnW4WGcWV76etpNCnX87pTgTjGJYnwX-lA1T7UjPHfvABBuTKUwyBtMIhuymK7FF6bNomJSSnKOJ3xPWyPxnlhogUnzMBc8yQ4kYjNVwyavJ8CDxFEaiYLNdvtxRzsYc3TBxb05TDC9uxQNHmV5h7zTpnntkPCZ2FQi8hYiyy9V4nFihvOAkv4-kUVnmS5b6nslk0VflGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=cyPP31PjYFFyn9KlZ6grgAk8lRkHVMo4rObCCdZFXuPuFYgZV9K7plHF6OCMG97th7U1eQ3HzimuvjueyhutaoKRkpR-i4RWsmCLtVdf210p6woeo1gHlWjKaxvTJmU-dPeGea8ar79zO07z54cXB-nt3ZMG0nTMKRbSXHPk0t43LAaL6sziHB9P9bO6dWcD4Ajia4Q7QzXhJfV87mUaL8sFAGLe8qLyNMemk-wI7x1Jt5_1cRydLwRjjo-QgAP2m_uoxl_Z0Mavv5n9meqZu9KvAgdFQIWoL1HKsiRrXbh7oIgARoSz-dH3UUpLW_IMsRVn_dK6TNcboNvlyQdc1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=cyPP31PjYFFyn9KlZ6grgAk8lRkHVMo4rObCCdZFXuPuFYgZV9K7plHF6OCMG97th7U1eQ3HzimuvjueyhutaoKRkpR-i4RWsmCLtVdf210p6woeo1gHlWjKaxvTJmU-dPeGea8ar79zO07z54cXB-nt3ZMG0nTMKRbSXHPk0t43LAaL6sziHB9P9bO6dWcD4Ajia4Q7QzXhJfV87mUaL8sFAGLe8qLyNMemk-wI7x1Jt5_1cRydLwRjjo-QgAP2m_uoxl_Z0Mavv5n9meqZu9KvAgdFQIWoL1HKsiRrXbh7oIgARoSz-dH3UUpLW_IMsRVn_dK6TNcboNvlyQdc1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NR8JAIJzL-MkFoIp9N3X5I0_fFWOsDA_KZ2LYCRXp9cXrXI7an33UOdVHEwsxxgKBH3B0nbnSvZX7uCZkW19xSnyJXlawqi1uBvHyr4FWXvDgaL960otiBzG0jr46ih1I3iADWVDK5XdGMlWaRXn1I9-M4xwpap9F4jbIfwCl82NSbtKfOLyI4VjjPzwA4yXT1P57x84QiQkqUIFgXB8gr_sG7wT3kQC6xgwe4hRiN3yCBC4tTcGh5yboiTRgxyFFEPUCt2aypiwkTyig1CqlAs8weh-PMHsfAheQ_-vqy93mqPinViKts0nZzijk3xGAcAthPX24Aqnp12KciyymQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aECkuhEdwBJ5-V8aB9IruK8z4kJjmNi0Rt90cJopx_Sbe3HSIgjsnxhsMl6_OO7yQb7jIlFp5O1-n96OYPluHTQpiCJFNXqNZM_F0MiqsR_fKAaFRoylxbYplmUnVRFdyx3RYj3RlmaXjLIT2xBhWAsxErCdED5dGjsbbnOS-xUTsIAz6BYj4qWL81clGrGx4AqKgfUZUTbwELYeLqRym3kZLbZnw9ivRqU7b-H_x3A4gyXcqT9ucFP5UG44i3by-49b-sIpfRTS0ihgD645LHkKjVsFu9WwIxa8FOd6CHQ7y1H8yjY-XTar3keaz5KWO1dzPOuIYnrvtbSbYP11yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpM-RZ5JdQKGve3K5rgAZ-UJxoBkPBBHGtjSa93Mj1mK7_IRaTREVtZ1wfdJu1BMdp9dkoWji_x8RGL1pXiwSmyBS6ijjMOy0y0OsfkqGyc-G0O72jQyu2uolzLzCIfzeWRIFQiuIp3WdE-auPm20OM7uRUSBLSl8Lunlj3807mgU7iMdwVcUgFVKy5Ua-hARJtaoibGLgzZbkXU5err3_WZs7OW9CWri3bPH9KYpjZ4dt6Is1fvp3gTigvo5_E4pOu07I10mhKel7NNo8We8RzLGz4ixXdaQGY6e8yL_kVThGBwrqGA1_keHDsmsXfuMLm2KD70yuQiPTcetPsWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=bioQav7JfjRE6SnxCODbpUoiens90aIeoHQefoi-jTOC6hZ8cQXGFADElz_qlLKJsf_ffFsk5D_Zix1SNJV2t9bBds2DwVtfsGY1XiS8XhNm0lsEjXMJw6ZTD8E7kGLMfnfIhV4slyyzszU8EZis7Ipou0C-yt4CurukKKk6fsLUAgMH18ultG3YMVYYlh5o-iL3OsAsOwYUHTSRanDJ-l6zaVR8kARTPDCTLaSCjLv3cLjoIJ9GD23bGpXAchhxFU4Gvpqbj6FaaqlWVTlxkczWubTl5atYdYoMVQLaeJYZIklyMk50EoPhnVhpymfmNMRhBlWPuuLX6djGO3vVjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=bioQav7JfjRE6SnxCODbpUoiens90aIeoHQefoi-jTOC6hZ8cQXGFADElz_qlLKJsf_ffFsk5D_Zix1SNJV2t9bBds2DwVtfsGY1XiS8XhNm0lsEjXMJw6ZTD8E7kGLMfnfIhV4slyyzszU8EZis7Ipou0C-yt4CurukKKk6fsLUAgMH18ultG3YMVYYlh5o-iL3OsAsOwYUHTSRanDJ-l6zaVR8kARTPDCTLaSCjLv3cLjoIJ9GD23bGpXAchhxFU4Gvpqbj6FaaqlWVTlxkczWubTl5atYdYoMVQLaeJYZIklyMk50EoPhnVhpymfmNMRhBlWPuuLX6djGO3vVjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyhagpcupVXjPk-nJKEJJ8eFP3HRp43PmbI7G265Q-OYFtT-KJAkqFZxy8bLm0kGY1zpdikpz3uUozvfH43cbsXwqJb4OcZ2ls3Xs__1fqMYcgaV5uQyLe0kuQAQy3b_KI9c7eZdrNx1w-jjpwwMUmgPh9wyCMB7xkDrQmQFQ7gJkt_HF4p9LJ03uPXAD1_-nlwdc_r-OJmoqMjlZMB9CH21NfJMdHq2RhQlfE3ITXxJzHX-PvPKLdjMaTWmW5Q_GlACaO9DqAtALNT4ue38sOX0HQYQVODwG0EdWd10BPHT48-eSuV0tLO65YayiUq6hv0TzFTBjbvPi-GZKCf1HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkwXhiYR91pSfodkrdV0ELnsF_yH4e7IjWKMsU-s4f6ftjuucISihMfFX3j-fK_jyumayOUihKYn8uO7zqiqf9ElP1pUGIj9gE7-IEsampqYqXxuewFlVEh0IpM2RhkMcelyk8CfOmHQGSloptPVxahZDV-J4jr0Sz0z_PjaPQV1PjP3RqRd5KRIl7bj4Z-Mk95WaXJ051L7M7rOWNxBpurPJ5CuAbBKPUm3Z9IV_440kXXig20PnF7amGpDmskMUDcQykdma5z2iMjsz6mYHXexyfTD6WZBMBwyrfZJgdUkAAbP1yUcquzIRS2PBOttqzkZnZaKUcplJpjG8RJcxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlfjZ2qS5jxiyZJCCxgt5bB0_ck_sqbgIrutNbja16zqHV9n3YzMvzRzd0-2UXKTQj2mRk_jSrRuuCBqvqye2VwbFLuUa1OqySqJsjFO8sg-d-NwpctguF53B09j5Sl4jadZAqL5pDlpu11Asjqw9C24y17waGVZ3701u9ZPqWThjrWStu8GYkKqP_RD1BUlisZ8j5l9CL6X_1c489ox8A5ggQ3v02JvWESg203iJt5rMKyeph4-vvCoScnGAbG43o9YNJDjHb6fqQBSbWMW6x4U4Uy6SNWfL_jWOFvTNWbWMCtg_QCqSjcd2vESk2NDWEDb5-LefSONCflHcmi-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTEk4MXhVeOCfJT25zVOSb3akt6E-A5ggvxcUVy3l8D82fxW4tyemyNSaRu2NSs9iWQwaoG8L8kfQbbXNvNgN0V9gDmUAcBc3_-ZP-LKJwW28xTuCXNpDuNCdb0_u1ji62kaUhdsKYHy7FAFgVxDIN4hxuf4XMzkMruvwtY2ti9Qq7ixR9SmwBuvdDevATAOkVpJ8RSpEKR86PhJtZX3SGPdmLlNbpWJubCBl-vySgBweZOg3Ec6GpbtPvuf_2gQ4JrKdhs5VJ8zAmR5HK-AnjGJzlDSRi13VXeZScRs6oX8Jh9iMlmYM_znIKjI0eOjEingt6puFKR3PG5z3HMr_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=A933KzKA3oVKQLGFCsuii7YARGO_aD8Pvicz3O0sf31tZ58z0BPvuErkYQIvZcv_LfkLr-7xaoaS-bD4N6ucK2iHnrTFtbCwquiDcEwabJX2D5V8nmEQeRRZnaESIMpM4AXZi5Sn1gv0uviSfNfNt_AiVfvRsNnkqXnIjczWOf52Dz-pLQMr_UheiKteAEkjAxaw7QY51On-lemS9O4VDjQsYJVQ3_Q7v0GYtd3hVfj80MY-sJ4TjlaLFAoHpW0zeWnPJcKDxg86Ha6xzfEB4wWGqTRwMPcmEE4nOPlXb70gKIihVB72hLKfoLTLU-XEXBekXGjUyTI-ot4AJ_czHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=A933KzKA3oVKQLGFCsuii7YARGO_aD8Pvicz3O0sf31tZ58z0BPvuErkYQIvZcv_LfkLr-7xaoaS-bD4N6ucK2iHnrTFtbCwquiDcEwabJX2D5V8nmEQeRRZnaESIMpM4AXZi5Sn1gv0uviSfNfNt_AiVfvRsNnkqXnIjczWOf52Dz-pLQMr_UheiKteAEkjAxaw7QY51On-lemS9O4VDjQsYJVQ3_Q7v0GYtd3hVfj80MY-sJ4TjlaLFAoHpW0zeWnPJcKDxg86Ha6xzfEB4wWGqTRwMPcmEE4nOPlXb70gKIihVB72hLKfoLTLU-XEXBekXGjUyTI-ot4AJ_czHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftkuEq7CymTglekHXCxXAVWAxvPSKjGj_IjBX_zIdII1uqvAn5WPdOc3HS_xHL6PkeNEZdZB7Z50KBedtATB8fQAdhkf9Qo4TOKox2I3VK1ry3Xl9yu8Gi8pgutvYfrwOzB-aEu2fouK4nDmxRb3sncQraBto-KHoZVgMBdDnIYnhTbAexvF_pf2KbYMZ5528hBmy2chbEBHDA6VpNVMnvCodH_Wi57QI1XsO3jX_BvpdUYky1JVdHVmNHYvhwdvHGpi1g7zvZ9XbfKpwgyNEslxiyKem_42K8_8rUQgjOe7hFlbDNGx7MDjst_fjjN7I5bnL1mu2SvFIGl7y1ec_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=uBG61RPg0jaghyIM_kaU8rh9i0SOiSYnjf2P45TCzCmo5-_26tkxwsBpUeEsqlRLCcwUuQvenvFqreAolgkmQuXqNgUMSW_SsjIPR4Ly5gieSeBu0if9X58lWJ6JA02SUL4l5pJhpnc0glYCTsez3lrHav_ojGTQaUWo9xq5XPj7Fo-jv-AnrynQ3N_jRxOKX_XXWD6j_joxe2relqlm_2v905bfX6z0zySmB1cLyagC5vpmYYabYVMbprN2KjYurWNGgTstkXj88nk6urQwXgzSAsqOKCVNec9nYweh7EvwHGPvlCxNzCs36NyHjmkzOFEIcDqsylPNauqxJ1BphA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=uBG61RPg0jaghyIM_kaU8rh9i0SOiSYnjf2P45TCzCmo5-_26tkxwsBpUeEsqlRLCcwUuQvenvFqreAolgkmQuXqNgUMSW_SsjIPR4Ly5gieSeBu0if9X58lWJ6JA02SUL4l5pJhpnc0glYCTsez3lrHav_ojGTQaUWo9xq5XPj7Fo-jv-AnrynQ3N_jRxOKX_XXWD6j_joxe2relqlm_2v905bfX6z0zySmB1cLyagC5vpmYYabYVMbprN2KjYurWNGgTstkXj88nk6urQwXgzSAsqOKCVNec9nYweh7EvwHGPvlCxNzCs36NyHjmkzOFEIcDqsylPNauqxJ1BphA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcgKkzauTVD-1WzYWEMTUZE_wF_J_x6fu4qyT58nayNDsun1YYJg1uHYs4VHUgSOux1LkCRr3soC8chz25pX1FJewYzW7Ze7lSBIfsn70S0oId6nZA0m10LdmltG3u-8e_0hHmttdyF6SIedwLBrL6kIgEyDkZ2n3gSWWfkxA5SbTQPqNNJO6gByhE-3lNMicwxbsNHXZ-im10gL4paLeE6xl_RSNfEhBoeojDn6SX_CF1hpH7KICk7BSsJ4Xq6ajo6BKYI8Pj4j42CttX9lWGjFsKQ16ZU1yQRlXFUGZO3qwqRtuwAaYsyE5Lb460pqymaOd59h9F-FzypJ46zm6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=TRsIxkb_m3vn4lL_iUvlV-RX01P9w0EtuWfW5UuF1A0snFWQhU60QtI77oBdKDTof0kEaEltkDVzCiJJfT0cuYvV5CusAahr-ZzcWo1SJ8wMQCiEAMf1LBlaT9XmobHqVsEH7-jSQRqBJY7nrOQe2shEX8tvF-j7jsO02HgWHduaFgQP00dhtaixOx4nH-ZciCaN6k9eFp1HAOFPKffGmsUaUL6QJDE_vwuPRReA1yuDiFDt4ShKRY3bOwFvqp3UsOKf0Z2q5ojsITOpKNO1Ny3ZW5CfbS1cliIoVDadEHDKpz2W5Vog2ZjHBhw3vLk0BWgwy2NzoyBhs3hF9ZBmag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=TRsIxkb_m3vn4lL_iUvlV-RX01P9w0EtuWfW5UuF1A0snFWQhU60QtI77oBdKDTof0kEaEltkDVzCiJJfT0cuYvV5CusAahr-ZzcWo1SJ8wMQCiEAMf1LBlaT9XmobHqVsEH7-jSQRqBJY7nrOQe2shEX8tvF-j7jsO02HgWHduaFgQP00dhtaixOx4nH-ZciCaN6k9eFp1HAOFPKffGmsUaUL6QJDE_vwuPRReA1yuDiFDt4ShKRY3bOwFvqp3UsOKf0Z2q5ojsITOpKNO1Ny3ZW5CfbS1cliIoVDadEHDKpz2W5Vog2ZjHBhw3vLk0BWgwy2NzoyBhs3hF9ZBmag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=YCMQrGzcqnBIcrHi52NdZFBdYI9zX4kls5uiD9DkpZ--iXt1RyNMaPJYHcW2dw-1P61quCq2TQtxfwbol0G7WLLUoCNTe39eyT188BkQE1toMsLzadTdzZjbjoU_GRYZKJ86wefonhrHE8HDQ1kS7i3X000BVsoNZjs-3seMFcVEXtMyG3_DJUGMIzEUS9kHS6a2Kn37l2bjVJ0ix00QTz-pgOFT1FLeSTXD5HdV7iPq3sliE4PulgtcdPkCfL1I_XY1hhGXbjDQqFSdJW0wpW0Ac_jMso6e9UqL3mL6VC9nK1eIn0WoZJDJ2KMbR7e1mqwPrco7fHnQzYXq_Zr9oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=YCMQrGzcqnBIcrHi52NdZFBdYI9zX4kls5uiD9DkpZ--iXt1RyNMaPJYHcW2dw-1P61quCq2TQtxfwbol0G7WLLUoCNTe39eyT188BkQE1toMsLzadTdzZjbjoU_GRYZKJ86wefonhrHE8HDQ1kS7i3X000BVsoNZjs-3seMFcVEXtMyG3_DJUGMIzEUS9kHS6a2Kn37l2bjVJ0ix00QTz-pgOFT1FLeSTXD5HdV7iPq3sliE4PulgtcdPkCfL1I_XY1hhGXbjDQqFSdJW0wpW0Ac_jMso6e9UqL3mL6VC9nK1eIn0WoZJDJ2KMbR7e1mqwPrco7fHnQzYXq_Zr9oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONUEnvd0OgVxooxgKyo9VZBgRGnZS7F6zx259ExK-IzlGdL-kMy0ZPZdFOFsFJbnk_eswW4MIkBHBagY0aeVPr6jxOHZ_A8D2VgjToceg6TFdB5zhSid1fm7_6oql--Hc3t-qp9-SIKq01mOXukV365g6JBuCUeKNYNYMCGovqtWObWJP_F5qks5E-xzHS1R3kFQrH55XSeuIOimFuQeZULLiirFpdBMZOc0UcnSnLKkmkz3yfMoFS_ArAIP4YpjyJ7vErTJpUuzpeNjr61pYw1hb6BUFZWMVOwhc32q0fjJMuvhI-uAbNStUm1wWlkJMg3UEpV3B8zsFF4AYErZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT0-65mf3YQ8dwcHlL3KOC2wl93rph6ZAB30wj7iq-mOGEJrgcbLTS7LcpEagGb3F8CT5Hae03K0PFXDIGH5PmaGq5jJByEppVz_r_57cMdVHclYaScADTHQPvDo-_9MYvMAbzM1DyOF4Irm5zRbqugeJqfKjcGQAEj6GFk3ZfhIBiwgtAVWdAf2fRDlEv9C3_HxsvEDESWQ2chmJtlJFRTeMVWvW_uA1hHHP8ydZ_CVC3G75DvEgtIqxK0n4RZCQnxjEJK3sRiXsYBDrtSs2aWjfSUZeQ5yGDef4j2svzSJZIQw54glOCqe1hMX51qMV-h0VY9zhdtvr5tO39r8mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUC6PTkYjRAdFl9hF1K6eYDPGfl7nnta7NiKb3YQyqbDzsdeFIvh7I4rfbLpHq39wM4IFBdtPBVejppwQyf9ldMfoigpOFeOBITI0XCU6T-kQr9eZxjz5DFhPC4qXDBq27SqdrBmZFgAplJTVzrbwGfmfo_6xHEixOjZcsgFbfRWYL14cSWEdo_yw5m93qK2VM2q9TxxYIwfmd7jMQfbwsv_emBMr0jcHFpktuGSVhVNYH5D3xRhbMqIjW6scpFQ1sySOIlhxQ26fnvn1l0UxIDOlbwVVboVkPvjQkGoSzAIuG_RXKIX9mNozL25ReXx50C877YBBYc_LU744IO7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4ST7lWdWzGOP3zO75ZHjgtzbY_OB-4iWozSxOIx597GXYc4KkTCpUomPEUVCx-yE5kHYbANcYCKAXUUPixbWw1U5WSGZ-W_jqyWyaQ6SxEJJrv6x64w1ROuoiI2gpksMgYvR1XBe7k7q-UjDdx8RmtfyEjH6EAfSmXFAK2-lzbj7dEvsnOQPCED4fp3wL_iJhVZ7sA1xhiOM8SKlK6EOupzttsAB9JJYL9IW9dM_MFQ741kXRr2cDXkevDysXvABj-iDNUI4ULe_v5bwzILQBGjD0DDwseY3n8Y3cTlsqtLTbq707DgF9qBQqZLOX7_8YZS7he6jtdoz5Nn2B8Kmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=ifOvSxwe5mcfJulOksfU_Clg32BbyxXMZd7zc7q_j8sCErlizc4akCH3ODPiwJMXcfc9rpRIw_7r8bWvQDzeG-q-AE8fU9D094yJfu4VvTV8LlOXIkFI_499GfDAjqXvi8cG9V4VUr4E2HAxFdYEJpqQua8vI-GJICYCZsutNVdKypkhP3haxObe-ek1kBg3AU9gWuCXbEQ-LHCXYmS_f3awsmgXUDMf9yNRIFvgQ6H0n2FFzpvirVsj-9L9R28lJ3qlpxQq8_Rm-UE0tvjU9030EqODex2WmgNcvzoRKCKTGY6M_DjnpiupSmM9aH-6fsaA3-G5rV1uueQXvzV7KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=ifOvSxwe5mcfJulOksfU_Clg32BbyxXMZd7zc7q_j8sCErlizc4akCH3ODPiwJMXcfc9rpRIw_7r8bWvQDzeG-q-AE8fU9D094yJfu4VvTV8LlOXIkFI_499GfDAjqXvi8cG9V4VUr4E2HAxFdYEJpqQua8vI-GJICYCZsutNVdKypkhP3haxObe-ek1kBg3AU9gWuCXbEQ-LHCXYmS_f3awsmgXUDMf9yNRIFvgQ6H0n2FFzpvirVsj-9L9R28lJ3qlpxQq8_Rm-UE0tvjU9030EqODex2WmgNcvzoRKCKTGY6M_DjnpiupSmM9aH-6fsaA3-G5rV1uueQXvzV7KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieCiimTGNpeFw3p3rH9Ih_pNcoiUHiYI3h_w2tDmB5Fk7m_Cnc861WPRzuB3udeUhkvyuAct2EIEUdb-CA4Ov9FmP9H_4stqr6ihPR-sQqSafikJDNyaJBfaH-IP816TBemnniDMziNmB7GIeB5YYIVLDQWMuYCbW2Olp2wf5wJZwUapR1SmMiWn8WWc2wY-BP4ngtRdr4x2BlSAtKRCoDoIR_30oi3oS6lQMI_VxWUuNyfeaL7WV7vc20hgmYGOBPQNC6LAagBAvvx3rvFWpbaWMB7ddxuvnzRZXXeDO7uYlR61QV9ElXlXvFuk4oMjmZjkWsInmUf6OKagKyz36ffU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieCiimTGNpeFw3p3rH9Ih_pNcoiUHiYI3h_w2tDmB5Fk7m_Cnc861WPRzuB3udeUhkvyuAct2EIEUdb-CA4Ov9FmP9H_4stqr6ihPR-sQqSafikJDNyaJBfaH-IP816TBemnniDMziNmB7GIeB5YYIVLDQWMuYCbW2Olp2wf5wJZwUapR1SmMiWn8WWc2wY-BP4ngtRdr4x2BlSAtKRCoDoIR_30oi3oS6lQMI_VxWUuNyfeaL7WV7vc20hgmYGOBPQNC6LAagBAvvx3rvFWpbaWMB7ddxuvnzRZXXeDO7uYlR61QV9ElXlXvFuk4oMjmZjkWsInmUf6OKagKyz36ffU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3kZz9OnM5xUCMt-BgTf6C2JqlLGCswlm7FXqC3lA45jXnheUtJn0svAKIm22Rpjn6tygLXxZIwRxkwrYsjxPoVAfRfGY4PbFSRj2DuzQBQlczNhbSTvqGQpzxrYJl6rxw7E1QVXRCqVgiytSQ6to9qDqww8x8u__1mQ21tUXFgGUbGgyUAXhw7BHCFKgk4_j8XIoz9HMqiwlcmwVX8eCFa4ceUuD9Pv455d_8cTToevHC7bwmpLH81rq4iXdCLEIVEbL6w1WOrUbaG23aFhhk-KOuyrT_20dKiiD9zv-ujH4Za_z6l5nG5OUe9_ognlQ2h9RspdQE0YwEk56UWOyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBb4ZEdKqGqkcYDfu7_1FhtcTZ2NS5sjPgIhenjA6_CprpjWuE5SzJF3n8luseId9vUxyGw7hMfKDL4IBkgbNSQpLkVUYafWeCA-zFzUDjf6fOEKBJ7V9pn8SUTDe7aaj3ja5gEFxFlDBdvhj9FO7wgEGfE9dNfkYeqfnegaZNOzMt6bav72Eb212as4lFLsuaL1kDrLqcNXNkcGAPhPwQ7OujkCo4Y6Ajj7GMBmVh7-FzIlar9aTdJB_PMNqgJU7Uq8K1bGh9TlkwnJ73g4hzC4YHsHRMOufv3Xorny6YSWi8XS4PcXHAASb4rhuRFguNroYvxBYnSlPiGjzLK68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cuSdtixofJ3hG87SNf3GGiqn32hcKDt40TXSkeUGZqQHNR3HuAL1qKSx5G62QmWkFVdoOLSXW9OK_bbgabygnFkTN_nPse9kanzu4VBezQ_ETES2nMyzYNQjV1YugvX3oEaF2XSEOaoLrFL1a31247h4eQX7c3qS-4boYr2BHUIOWEff1fX-mZpnxmgxpJImLDFRJZOEOBGk2WrtrMmtP2OIenVrPc4LMbrNiTLvg9c-1XioMmGBLoBFu2M32vjM1s5I14yOUutC0eH7zxTDEU4ERfMa1B1dUcz3grb5LfA3XjVElx__tjpGIz3EBQ9JrQQJIYClTtEW9ZPiUKT2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9-GUiJTCAy7Z25VsCfmOpVOUBr3fGahW-rEraoTon3OCWIdmjouNI4E1VcPBuo5AP-mU7e-YurL4JL2UXscb6ibUVYjzFCC2lE0Y9f5ZCgcn2rG55GeUM-jgMMx3vJFd3gwuSs-6Ku2WLLUkVZ8bHdQZ7DtAmcfwyx-o2FGmzbabN5MYnCpFlZ_ANeEGSKHcuCKzD8nqYSwMr1cEkYnSy7gY8NeJ7SZZ_tEg0UUMfwiETWaYj9B1z3TDkS2Mi24sPolFU3ZLFlQVtMEQXfhhDrYfv5jFM1ZowJ1ykoyikoXrc5rTDw_YgdG3wUx9rBy19tWOKwHqWtil7OUWtMAEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccorLR_-wr0uv4m5211UJpxT_az9h88fLqHNqNuxccycxdEEDpSV84g9dNlCxXIfN7ze6Jj4R9fp5Aqhji2dSslJpqao3c3QJdtbsLv_dISvoiYWJDmiKTJCUTljkMgiwmIiRsV6LHjc0CNFvI2IqscKxyb03Ag_6HwX4Ek9gw8wZ1MBVB9ngOpOrvW4VhpX2B-CguGwU1ujjRpbVa2LarE3QEl6_bd0m0-Q23QruBm4Xm7CuRa48xVpM8WdTxphF-5ZKC3VAssXnMwmlCFExBZcu9JKkL-2K08-CyowLxjQWRmE9BMr3_KcYmltIGTXJCuf-Lg9HJpwuXb3cU2toA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=MzbzBTJs7v9XS9KuKNpwehqHan2TaTCBt4tL7UWcDbXWALCLlCysWaZRJQkEkdtfpKyNaOXUr_6fAPm1NZxS-1uy3sljIsOZxK312LKrc9cBillOW5f4hyaEHK-Yyle5SCp3KlIbRzTYJ1f9YLs_v12NPlheu2ffRl-2kauNDerKeWmwgg6CRFosNSVuFlwtAh7qF_kZEEsjJrZxuSV1EqpcTJ5rkaoknA9MBQlIrtDJ5cPOczZGF7kw6kpVRRjI4lvp-5khM3O13tu788buiwYxnByLKb3URmLyDcwF0auNwGIo4WQrmsmAAvNyaE5g_4gt8bxptEK1gD8loUh4VUxhczWXVZIbhcYwSJSgE15b1OHtPpqOzvOFvER097W3bB3CqeZJ8F91NtaX9-QUhe2iOUX3yXSfGY3aTsBHtwo6Uf45QWKVB_buMpJ2UqEzbTc8fU9lAImwvVXGg59NMxfbeIwQVvcNLSbLnpt9FRB5E-q4-EDMwMMw2xT0nUETV2VBpdXV3FeGXmR26dynVnA3zDgYAyTVEnrS9_VnQ67tg_0J8IvaLU1BUKjcGUJSApbFV9qFjBmVg6oUE3zBqD6yHXR6S3i17d8zGx3MA6-qmVsHN1gojDzKiof7b8p9zTmjDlo1uxxyubSr2a20c0VFz-giYEWA5IXNz5LMBTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=MzbzBTJs7v9XS9KuKNpwehqHan2TaTCBt4tL7UWcDbXWALCLlCysWaZRJQkEkdtfpKyNaOXUr_6fAPm1NZxS-1uy3sljIsOZxK312LKrc9cBillOW5f4hyaEHK-Yyle5SCp3KlIbRzTYJ1f9YLs_v12NPlheu2ffRl-2kauNDerKeWmwgg6CRFosNSVuFlwtAh7qF_kZEEsjJrZxuSV1EqpcTJ5rkaoknA9MBQlIrtDJ5cPOczZGF7kw6kpVRRjI4lvp-5khM3O13tu788buiwYxnByLKb3URmLyDcwF0auNwGIo4WQrmsmAAvNyaE5g_4gt8bxptEK1gD8loUh4VUxhczWXVZIbhcYwSJSgE15b1OHtPpqOzvOFvER097W3bB3CqeZJ8F91NtaX9-QUhe2iOUX3yXSfGY3aTsBHtwo6Uf45QWKVB_buMpJ2UqEzbTc8fU9lAImwvVXGg59NMxfbeIwQVvcNLSbLnpt9FRB5E-q4-EDMwMMw2xT0nUETV2VBpdXV3FeGXmR26dynVnA3zDgYAyTVEnrS9_VnQ67tg_0J8IvaLU1BUKjcGUJSApbFV9qFjBmVg6oUE3zBqD6yHXR6S3i17d8zGx3MA6-qmVsHN1gojDzKiof7b8p9zTmjDlo1uxxyubSr2a20c0VFz-giYEWA5IXNz5LMBTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjE3p6AdygAKKCr5NzgJRhuszaZ_I2GPSyRraSDkYy1TrNzlZ54Q69YmcmrKaIzoTHM-xfV_pn2r0kIH1z6O6nFaJHCZD0Yw5xD_J5kmc19ZLcqGuuej5K80WhyseVilhlMW09cNPjHU8LVRdu-hPf3fN7cM9axlokfyMtvMX5OGK8rfl4m-mT2eCm-YYtmjTd3W0gtC0Mo9gH8esXc1q342hmIAgWMJhoRGPKkZz2yPYJuSptha31nBoP-sKD9d6og1I5LqDgxeka3T3F_uTkXqWzPldKqcaXZoaQgs3ysUhm-tgWs68X9iI3lq7pHyPEUO0pevOJx5B2quasmqyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=D9VAXbdaf1Gc8gdhXYW_5AF72Duxu5_tekj1OUDfLW5_V9FyilU6maVJH7dd3_fNwVKsFXZTvPMiKQ75tNkBHtGzONUPh85i9jMrFCqnzQcfi3yE-4REo5x5AHvkbE4aXFEsoIOVmiO8313Z2JrCmzU4Y3kGkizuYzgpoT0A7Npqlqu0Lwf7qUV0tdVnUx-XJjiGDpr5YTKZiJqa8JmREXMwMIkE11esP8YzzRIdL_loyhSbiuvGTwsipFWQsEgoTek_9k9gQGDikt6Qh2NCw7umerAlIuDKbRsVOwSvPclN22s7VwBqXLKyA3SsoJocEskt0bNkDpALct7OB37BDoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=D9VAXbdaf1Gc8gdhXYW_5AF72Duxu5_tekj1OUDfLW5_V9FyilU6maVJH7dd3_fNwVKsFXZTvPMiKQ75tNkBHtGzONUPh85i9jMrFCqnzQcfi3yE-4REo5x5AHvkbE4aXFEsoIOVmiO8313Z2JrCmzU4Y3kGkizuYzgpoT0A7Npqlqu0Lwf7qUV0tdVnUx-XJjiGDpr5YTKZiJqa8JmREXMwMIkE11esP8YzzRIdL_loyhSbiuvGTwsipFWQsEgoTek_9k9gQGDikt6Qh2NCw7umerAlIuDKbRsVOwSvPclN22s7VwBqXLKyA3SsoJocEskt0bNkDpALct7OB37BDoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=iLZ8P49zmRUdFars7IH_I-mmtPaYO6kARHtlN8qq8OpbhAWGVIRV_O6mdi29Oe7ytJJWFi_5UFpBSBR3niErY5zzy77Evj5R560HWP6d4DKRNNc7l23xaOtVYjX481xeXZ1rZmbBJRvSezvchHo2VBcrkQkQP9C1lUlhuRUaM0MyFJt2QiAVJRvJP_p_ML8SjNauE3tJoj70UIXiqQTDLDEn_w8FFiwy4qx7_0hnPQAVhFXoEIzXz0i84Vf2ktz4DG-0RQ1vmIpX6ljPlXkLtFt5R3A4R85E765NuQUsgwN_kb2roTfwAcpO8hKSQcjpkzRXfXqxZlJ2wm_mWwblK2kVkqFjtXBgmfBIGp8QFO291gmgqfA_JqBtm1r_YXGV3Hfe5XubxQNBGcSCmrLkwuOuPf6QMKHCtnB0rzbhxj-WgBiJSB72DgyyzZcYKxbbfhV32pF-UclCzoMfyY4cXysHt2fPpRiz61TsdGrBo-4Y7VlF0P3k8SUm6cc6YA2C-8Vydl7GEVsdHYEnF1gXyGE5CbgpThQcO8SvWok55L9yLTPx2zziYbmahNdIeJkiBmgrTVzYsTcdbRNnZ7UwTE2wYvCl6TUXup7dyotMUIt-RUJj5ydgFdb96fmMpubZ96jdM9Pmpa88N0biI8iOPA7IAKncJRZdeyHDbc7KovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=iLZ8P49zmRUdFars7IH_I-mmtPaYO6kARHtlN8qq8OpbhAWGVIRV_O6mdi29Oe7ytJJWFi_5UFpBSBR3niErY5zzy77Evj5R560HWP6d4DKRNNc7l23xaOtVYjX481xeXZ1rZmbBJRvSezvchHo2VBcrkQkQP9C1lUlhuRUaM0MyFJt2QiAVJRvJP_p_ML8SjNauE3tJoj70UIXiqQTDLDEn_w8FFiwy4qx7_0hnPQAVhFXoEIzXz0i84Vf2ktz4DG-0RQ1vmIpX6ljPlXkLtFt5R3A4R85E765NuQUsgwN_kb2roTfwAcpO8hKSQcjpkzRXfXqxZlJ2wm_mWwblK2kVkqFjtXBgmfBIGp8QFO291gmgqfA_JqBtm1r_YXGV3Hfe5XubxQNBGcSCmrLkwuOuPf6QMKHCtnB0rzbhxj-WgBiJSB72DgyyzZcYKxbbfhV32pF-UclCzoMfyY4cXysHt2fPpRiz61TsdGrBo-4Y7VlF0P3k8SUm6cc6YA2C-8Vydl7GEVsdHYEnF1gXyGE5CbgpThQcO8SvWok55L9yLTPx2zziYbmahNdIeJkiBmgrTVzYsTcdbRNnZ7UwTE2wYvCl6TUXup7dyotMUIt-RUJj5ydgFdb96fmMpubZ96jdM9Pmpa88N0biI8iOPA7IAKncJRZdeyHDbc7KovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=YxEe37NWGv7It5xJv96lbH8_jFBh5C52_UkkSkcRN9EaEDxOLXD9hBWWogwIl68lKu3HoyDwj9lJWCZxE_qOve1C5XKo5w-LnhRAwQwGMYmAS1CF5rtz7pYIcpiQTBKoAUEc9vwcNRIdGYaMMIkzfc79sur37a1TrGdC4il0hj0LIkFVdZ0l8scP0e76jHIugNx_HVc5NuxqzjZtt2X6wSHmqx0PpqWRXCYmKLiOS3O-4oGwozLMiOZDmgBYXpdSmpirt_S89zzyoBItZORZhzbONJbi_AW7HerA_a8SWpMhOwna4XNFmxHp0Qzt3PoJjWnTgA3ZDtok0lIaAgNTmIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=YxEe37NWGv7It5xJv96lbH8_jFBh5C52_UkkSkcRN9EaEDxOLXD9hBWWogwIl68lKu3HoyDwj9lJWCZxE_qOve1C5XKo5w-LnhRAwQwGMYmAS1CF5rtz7pYIcpiQTBKoAUEc9vwcNRIdGYaMMIkzfc79sur37a1TrGdC4il0hj0LIkFVdZ0l8scP0e76jHIugNx_HVc5NuxqzjZtt2X6wSHmqx0PpqWRXCYmKLiOS3O-4oGwozLMiOZDmgBYXpdSmpirt_S89zzyoBItZORZhzbONJbi_AW7HerA_a8SWpMhOwna4XNFmxHp0Qzt3PoJjWnTgA3ZDtok0lIaAgNTmIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F549fq8arIxJ0CDonPZmQQIskuhL8U5ubWSBJ0kqbYMdJhJby9_HSYmSsjEWzu4tW_3sDrHmRy6O6g1jeh9DShosOa780u_zz5-2b_6SHDN6-Yuy6bT-1lEVD5qUSotu-Zt-5l2ijFNSkqH8keJPunMdxBe4ftL3_Kh-XR_W46Lsy7RKfUioQnX4Y2M7N-K8w0GNf7s7eJSO37FY93IISCvIF48O9jmQquExBVWZQnAzD6T-08lw39C2dF0u6g47kQHWVQ366em24TnY0Ur5prKCg2KwpH6-OfIisKtoliGXOvtKuDh8wiKVCP01OMFUP_HMsy7vU24z5F2HoBIOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jylGN0CNU1W6UPl1KDU24LztQqpdJqSEcQva0F9Tg3Xv59fKqVZV3Jf_S4N0W8deWuQx0DcwAC7aytiopuuX33jftKAIKIK4Fnv62TPAj7l0SepwIONv3nuOTdnVk7Z3-IKOXrdHxatN5TpuMBf_-XMKrpZUihRoPgpnepmQTX5Ptg1SSMPIz8Tb75zz00J-OFgtfHXIPhngJgAvSIa4DX3PNjyBd7BpIZZlmPy6Mj4pYIRDKlVWN_eZrYHXhZIfemncDjBR_pwigBZg1hQkU6AzIBPEVbP1BMqkzF61ZuveZrfeWKYNFyUa0ko-v9Gm8HQAlFL0vJ_n41-_67yzeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6ZnQ1p0jmLZndMjPrdOEIfPENgBkanagvOSOP-gdJjs0srnBunPutM7dQLRSrQ9oo7ddBaeCBLxlbvh46FqzXc7uljzrr0wHpmbup7LXpfuc0XnFJgtmjUsbYCBcAiAqb9o3hKfm1VNRnEL7QzP3h-xy8b06Xa9NnVEKNZoZSIgoh5oPvh39QRZX7i7zoqbU49QpdoX-9HYg3aUMH6ij0LrVTJdoqcEqP84-bq3AYjiDJsnnfBxxuXDFrVJARIhzI5LScfhi0nFvFwDXNT77P2g5CZW2OY86bC9O70yBlb2pnwL2ZafoJdbqr7V-pvpgh-XyfO8JIu_p_XecElwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5SbOAi2yMy3RPDiwHQGxzEiZBItL6tcILgqrHkY41pMN-Q9r8XIEtErqexTndO-j78Y6vHOhsM8PK_0FNE-2qkwQqR0dJ32NKkm1YvE9lw-CJKe6e4UXLymQJQGBo0cwJGkIBTWQUagb4c_5tNkWaE_Chx_xhlY0ROvSjbS3obfBFdp4dD63XJIN00nqrGDRHHpHNASWbJcSBDpcjaCRG1spoGYnYTyPwuNhr9ONRWNI1Vx3zb-Qki4sqBHrFatrySxsKWcUs0sO2HrvS2IEzFZV179vktR9_h-0tFdse8JIJBNwRs49pkiFCKyBWC3PebkKsncJ0gKGdFoRkRMFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-hPqZhufXTh8spWE04280LBaMaCGdhfvkTPWPyq4Z4cNTT48GnnQO_tLM5FkhOUvSGt6rSVdKzlrYzxakp_5vwHwCesn0JZH1X70etCiLmHRmwlhB6d_3mFbhWaJMsw7spq2yxpUYtSeZFRIUOLrcMv-HSei2b5DkrqOnwSXmSnmvPpiZ6UvddKejNALErYHy9QQ4UhdLA76Znx80IVY52hiLeCCYseDuN8_mAKjDc-j3FBJXCF4l2kth5sde4KiGryR2qtUSbBp9rjlV7ZuLuGtHTVDzJjU8dJR0xhuWJOp0uJIKrhixZDohMUldH05kZto_oIHmPCR1Th5QH7zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=QiFqFMGOPxSvAf-O7aZBLfboIDzM2cou4x2fJcVcKJU278hkvpPmuk30PWDcd6YydjLp-hkWytTouOxIz3OsqjDg4Pld0C3EF1V2ELNLsl5KmfpLTkVfRWLPmKNPP1Gs0LSJcFOHKbW-I1H8U3Xe-qT1gvV82zmFofrR8jM5drGlghFGDB8nrbsQDQbMt2sZkqFD6sK0KVG6BLVP_VP4lfkgpCP1NSDGVG2nt9gev6s8QNq5RJL4W-VHrwtxpn7s_k8KjaGtkMY08rKB13P5d8UBEzBG4nV8amvpn9i3KWvIJZH5LD36VVrpFzEcPDFypTYfg3pIK_298Kkz5g-4cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=QiFqFMGOPxSvAf-O7aZBLfboIDzM2cou4x2fJcVcKJU278hkvpPmuk30PWDcd6YydjLp-hkWytTouOxIz3OsqjDg4Pld0C3EF1V2ELNLsl5KmfpLTkVfRWLPmKNPP1Gs0LSJcFOHKbW-I1H8U3Xe-qT1gvV82zmFofrR8jM5drGlghFGDB8nrbsQDQbMt2sZkqFD6sK0KVG6BLVP_VP4lfkgpCP1NSDGVG2nt9gev6s8QNq5RJL4W-VHrwtxpn7s_k8KjaGtkMY08rKB13P5d8UBEzBG4nV8amvpn9i3KWvIJZH5LD36VVrpFzEcPDFypTYfg3pIK_298Kkz5g-4cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_ahBc2i2oy1KumSYJNih44gFuP0-EKoRkx7kKrpKzFeIDjEBHr_mKcu60f4Z24Dc8dsscnOKrZH91WH_WqWFBhXHwm4wSmHckPO2WwrlE7aI-jsnohtgTmaPeCupEwR2qreT939qK4jJVateTPd10W-47od67l7y4OP2e0amATXvF2SHue8CZhOx5i26IHuTu5xtI_-iKKu5QUozDWeZtHy-6wRnOqcNXDrPZ1-ijMcY_YiiCCzpb_HqkIijYkc-EJ4aKbtX5xVPNpSaxlnbNUTidE-rWSvPB5BbhLMtkGeSjlD1LpqOx_mOzC_wq7ZIFgQ5rRyMe9_Iv8auBC3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z61v1reB8q6ZZ4vPZnx1c0cGCH8MFr_9mkdDFd0aqEiwz2_w6YTfnedTMR81JBmFHAokV43-Xbjtr-w1quPZnyG7sHX4WrO2WHNVycORzYUhk4_WHwQY7R958rhKvZWtIdzhahceF6jTd79o_S80M3jOqKW06Dm-WII608UBRZ8qQOV_JyyVXgGZTj7MR0AV5OUcVAlhFfZ0FA0FKfwe1HItxTnfGLE2aivtccHCs727NaR9OX7TICSYEW2xN28aKjg8XW-QUP7RhMfIxMAcxV6ifbkX01lUqHPx-8DZdhKTEuBeGNy0cAc8ZRlDRVgn1xzUXJNfC2nGEzwfgmraRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFGCJOHaYyg22qmbddXilXJOgkaFsjkt-nS1A0TNfnLXzklQspPTuVBQyQyUb9EakG2xhzKcN-MfnLuN_rmqcYyql29-PqxklvMEwuGg4hFNj_q6RhlH-H0Fs_2iX1MuWDxVIOt660WHVwKaq9anMudm-gbmMIj_uU5mKapcrkn8b_FwzpNM-BKncRHS7xztby8Wr8XmuC1cJVkeOwPm--9BccmXcGHX5WpYDwqkBOOt6r3eG_GdnhfrPDXsWIdnGLYWAqKMFL494xGZb4b-CiOzcS-1KAtnsVRFaPF6X4dm6eSD_fIfkVBTJ0bh_PiIWTn11LJHESKyfxfox39BQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMBoz4FBQsvHFfM3F_PDNexWE_9qyjG_53bao8_E4r-OhzoJol_JWfRMkX1n-P9DS0gqKBW9uKapRx2k0S1jV3bubDMLejiD43eTE6eqBoUslLA_qj887R-ZfTGscoZyB7V1ZFpvCqPdOgSUZqop9uWo66qFnoV92f-8snPeUIcbk8_oy3DgC-XmRl6Jq57JdL7o20UHGsd4sy6gwn62z-vdMRaFZlc-FzOaYb3Q7DV9IFuTnPC6EzjRkhOBYjUqSButiEeJa0T5UkG4I8cgi0_OLPTJe9s99L5eGrqve-xSv-8yDIYBpTckbPGLQm6AnihgbbKloTV-bcf8923ecQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJ3iOfsAoPPW1SWRW5IigOxiqWAl-fmElWpf3RxewZQf49qxeMEMWLBQkYEWlGiOPJ52uEewvmWct-wtX8eKT8IZBpjrJ_p6-IEx1dgpaMfwtqmx_dcuqhEBVEkJymnOulP59o74uEk8XhDJWQ5_idq4odLtjV-l_Aw4U3NPtd6fHC1bKUAiQGdZLIimvbO7EFeR6lHf9eDgCqMZQcB6myqqy9S7_wAtYtwWJCN3PrynigoR5ExdpRiVgbtsGuT-pm1W0cRm9tMusBNvT8842Dxq4jKB9fKPgfuK5wkY5YKRWhOp_GSwUia7ZWll0c05Qx_zpV7iNeRevDEjSZuX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyAN8iAvSBFrKthFk4JOgnpmL7Won22I0lXLsU__bx6BEC0arh-L0App4ufe78Y9AUVl_LErCaiwx13sHzkGmKB7tC853Tt0IO85KTF2e66XGydOihAM9JRBLhIZLE__VSxs9LRGBMp3aEp7MbIjQzHQn1a1hBZeKpHumKP8FEvTur6gAa0Ez2ocT1ZYzoITCmRsME3IUJ79WUO-zUtwRCHL3uhDbg3WNQhhOqIKVlWxxexjDC0ZosMN61uCN0dIMSSLC-yXbkuaaoTIMOzWWSA-VoTS6xjY4vGWm06WdqbYLWlmYKYwYhPOTW9JPIqNp5oBuag8J-HKGM8hl9XINw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcryaFNAoKSLUOVjd6Eh6ew14fC4gfAexnjMOu5pkqaPgnO0sHQ5oKjoxMh_tGnU-tXM0qJKds4zb7LPnR9v3mByzC0azcmPgYxnjy8xq-sKKm1rBi_gC0veYjXcFEZ2gocPjl_dDVwQHFvEtIiIIx0iJTEGffL9RkdlwEYVGtcLZYCo_83Xb67MbWFCdBm6IaxoIl1miR_86fb0xOTsZfzoJfDmW_yRtnmmWLME4iwddxYYAhu7aWHBYMXox2onTNgOLPwWMV-CzuJV0qeKunmCxjbib2F6k4rBA6akqlWHH0i3L_gIZfjx7eVNm3wAa3OC7XIAAmoioQrR-dnldQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxkPnYCCMXBGd8RxhKjhfhRBjvqau5wNn4EMaEYO0KQFF4wTzNpEVLd7I7M2n2SUF5qhVngoMqRccPfankcDUOZVJ-wFgkIFMMLLSvlHM17bYjNHCQIuCkWa5Hg5rdwrX-XT6Jo-4nCA-i0cVtQVrHrGU64JDvKVgjfL-CkaWlWF2Sf8fV9jwomUVbfq8WLKOx6jtgmkXn4P3mhfJ9K1vqlTGS7Mp5f_F9NE2SO89ysKja8Cz9uu9Sw1wlCMHzo9-Zb32bhNQhsh-Cag1cr9h6W4x1KwgwA7f8CYILZ9ftLCXjqsYzy4htJt8QmlSoaSLyCN7mip3xCgKxe_B-FyOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=JBWw_PHJoi4mxd2YDeTKCmfbHATm84cj12YUVGikc1_y2M-Gu8ob6bJLrQH160IOHuZuWuYHHKzEAaPGoDwxn2R-qh6y3_5iK1JMSHRa1ZAuYsSsxACBh6OADSiFCxehshc0TAImLH2bhqrp-PQJRi87NeG08nbbp9qPqvFqjdBles7NCwCKgIQ1y_MqwrfknSWs5eVlrNPGoOQhK2UOm97Miq1BFCsSPyZrvDgou_yYzrmgOhsvvnlCySS5E9FolfWqzdijeoFWvFp57BYgTxUyNVDCdpvRJkXkMiLJ02KAanGW710knD7xO0VBUdsTyJj-N1OZl0t_CbH5PdDQDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=JBWw_PHJoi4mxd2YDeTKCmfbHATm84cj12YUVGikc1_y2M-Gu8ob6bJLrQH160IOHuZuWuYHHKzEAaPGoDwxn2R-qh6y3_5iK1JMSHRa1ZAuYsSsxACBh6OADSiFCxehshc0TAImLH2bhqrp-PQJRi87NeG08nbbp9qPqvFqjdBles7NCwCKgIQ1y_MqwrfknSWs5eVlrNPGoOQhK2UOm97Miq1BFCsSPyZrvDgou_yYzrmgOhsvvnlCySS5E9FolfWqzdijeoFWvFp57BYgTxUyNVDCdpvRJkXkMiLJ02KAanGW710knD7xO0VBUdsTyJj-N1OZl0t_CbH5PdDQDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=i8mtbDdf0jClURKtdelxkSCo_JV4800kv4u8EUwIV-VpgSjH68BCw5eHrNWVVLGaczUmCHwIqZaAcq7ETW8rMZojP8nGwxaNzOoLjYtbilqOZVIttvxhU9x9cRbYts1i_s2Bb9G7vCzskxLFLAbDdLSr6B8pXER8DavcfgIXhyUOFv9JRUZlSaj0B4DWmwh65meDzQnH9oqOrJc17Sb9nobIlTd_g3qeIDhM6DluuCXj5QwYM7TMaGbFHJBPOAvZGRfKMkaEfM7yT4-S5t4gd-1qObV4WmpH1VMb52uYicEfPlmHD3VTmqkEADYQN91KKPDYO1jcIbEKwc5thihHkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=i8mtbDdf0jClURKtdelxkSCo_JV4800kv4u8EUwIV-VpgSjH68BCw5eHrNWVVLGaczUmCHwIqZaAcq7ETW8rMZojP8nGwxaNzOoLjYtbilqOZVIttvxhU9x9cRbYts1i_s2Bb9G7vCzskxLFLAbDdLSr6B8pXER8DavcfgIXhyUOFv9JRUZlSaj0B4DWmwh65meDzQnH9oqOrJc17Sb9nobIlTd_g3qeIDhM6DluuCXj5QwYM7TMaGbFHJBPOAvZGRfKMkaEfM7yT4-S5t4gd-1qObV4WmpH1VMb52uYicEfPlmHD3VTmqkEADYQN91KKPDYO1jcIbEKwc5thihHkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=lWplQ1DarSA_96ztddBSVKToYBR32vZsnnZTBFYVGOSFviAphMUKk0VOXFwH0sbMhjzPwju1eUQ064YlClK3TkYG3X04RYeDFjgwFjgSlrdcWJ0_NiXJAdACGij9wbv83uH8vEM5P8BNsz-8813JP7ZSsi4riW4MRFskL9RnhzSQSwG_AOKjzIOvqMdGClx2VYvASjkGFFqgexOHkPY7zTtzvjxg5wH928Smylk-Xk55uZjFtz8t-fflcdq6pnvbT934u-ggdUWnDqz9m0JMRhiHtnSLGg3SaUWkRWNCbnwuAuhoYZd5dQEsLvshnyznzfUsKXk0XL6B9QxBaicicg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=lWplQ1DarSA_96ztddBSVKToYBR32vZsnnZTBFYVGOSFviAphMUKk0VOXFwH0sbMhjzPwju1eUQ064YlClK3TkYG3X04RYeDFjgwFjgSlrdcWJ0_NiXJAdACGij9wbv83uH8vEM5P8BNsz-8813JP7ZSsi4riW4MRFskL9RnhzSQSwG_AOKjzIOvqMdGClx2VYvASjkGFFqgexOHkPY7zTtzvjxg5wH928Smylk-Xk55uZjFtz8t-fflcdq6pnvbT934u-ggdUWnDqz9m0JMRhiHtnSLGg3SaUWkRWNCbnwuAuhoYZd5dQEsLvshnyznzfUsKXk0XL6B9QxBaicicg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=mIxtdhqawFqOkbATHY3X-DINuB70VI3dabW7NSRNT6yEq-qNAW3UptHQkiSm9ccyTsPUCd75SgMw45-rFlLz8TMq90mZexIHyUajQ7HcNednARJ9R_E_Bu_QiLoasoSf8GiinUd9_niwznC9TWQHMAcG_gk-agDtwd_BtoVaKjL6NNYv4gE-JWX_2Q3e8noVjCJOjk72ZbHoZdoVx2Lo_pWYYSWdM5z9l_ysv0uoWpqp_GeBvoE3SfcqMhY--H-ru9cxrOc2D23JuONRV5BCYoCy32yaLDJqHdjqFo7W2g_AglR810wiofb6J-YgkyJfqHQbeCOlQjURIRqTkCRC0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=mIxtdhqawFqOkbATHY3X-DINuB70VI3dabW7NSRNT6yEq-qNAW3UptHQkiSm9ccyTsPUCd75SgMw45-rFlLz8TMq90mZexIHyUajQ7HcNednARJ9R_E_Bu_QiLoasoSf8GiinUd9_niwznC9TWQHMAcG_gk-agDtwd_BtoVaKjL6NNYv4gE-JWX_2Q3e8noVjCJOjk72ZbHoZdoVx2Lo_pWYYSWdM5z9l_ysv0uoWpqp_GeBvoE3SfcqMhY--H-ru9cxrOc2D23JuONRV5BCYoCy32yaLDJqHdjqFo7W2g_AglR810wiofb6J-YgkyJfqHQbeCOlQjURIRqTkCRC0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=grato4ZBrEIP7gWprN2SpD3DCXDfJcTT4FtE0fdevtH9G5W2tcGhkmPBwhbO8pdJGlIWMV7DyKPRUjzfo3DLHnjz0Nv67bSU62t9YlHPAZGLGShhibnt3wMJ3y_tc1S5J5Fz1FxMpoAN1uKLMDRVWE4Uz0m3d6AeHOGbhg_ZnbzcFzVl7RJnAiH7E-RdQFujOz-KO92t6XBLN3Xs82UBUHDQIXO1-PJJK5DuxwLSclQBKHWO0jF5NzSFrMNs0SmTd34vc1cp7bZTkHmCQ-iep5YY4CC0QOUdycrPoaw_fc3Z58OycgHMU_37CZa3iQ63L9VNWCUmh-umx3Daz0Bbkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=grato4ZBrEIP7gWprN2SpD3DCXDfJcTT4FtE0fdevtH9G5W2tcGhkmPBwhbO8pdJGlIWMV7DyKPRUjzfo3DLHnjz0Nv67bSU62t9YlHPAZGLGShhibnt3wMJ3y_tc1S5J5Fz1FxMpoAN1uKLMDRVWE4Uz0m3d6AeHOGbhg_ZnbzcFzVl7RJnAiH7E-RdQFujOz-KO92t6XBLN3Xs82UBUHDQIXO1-PJJK5DuxwLSclQBKHWO0jF5NzSFrMNs0SmTd34vc1cp7bZTkHmCQ-iep5YY4CC0QOUdycrPoaw_fc3Z58OycgHMU_37CZa3iQ63L9VNWCUmh-umx3Daz0Bbkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=j0-ONgM8LYAMFUS9qbww1oKbT-D5xyoEc8T5Z8pQmAl4K75AWNOK3MZ5eANSK6wAkT-_yrBIi_uzpLRDOBZnXtyvJPfJqvH1oAIgL4Cvd3-lefiR7UrX0_qRq2PiF7nUI_fi3wl_jGsxph-5mHNYyQ0mWpmm0P1N-gdjicC1F3ot9dN4n_C77dLhmgTs9FxiOVkvFE_3ugZzLxSUlImvJDDNSnCeat2QUBkjLilpqttJswXGYIWq-21b9BODABDj6CuoMWfudj_V1BV287KHFCrxlpPhlUIbq3WIcwSw6ecoFUg0BYKv3cxtFySRdGB0ml-Y2wN-TKyQdDuv3xQofw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=j0-ONgM8LYAMFUS9qbww1oKbT-D5xyoEc8T5Z8pQmAl4K75AWNOK3MZ5eANSK6wAkT-_yrBIi_uzpLRDOBZnXtyvJPfJqvH1oAIgL4Cvd3-lefiR7UrX0_qRq2PiF7nUI_fi3wl_jGsxph-5mHNYyQ0mWpmm0P1N-gdjicC1F3ot9dN4n_C77dLhmgTs9FxiOVkvFE_3ugZzLxSUlImvJDDNSnCeat2QUBkjLilpqttJswXGYIWq-21b9BODABDj6CuoMWfudj_V1BV287KHFCrxlpPhlUIbq3WIcwSw6ecoFUg0BYKv3cxtFySRdGB0ml-Y2wN-TKyQdDuv3xQofw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVR4inm2xViVJwFKQzMZNR1Km1T4HI4D_keJo44opL_eB3XoAR4qdaILPzjtE7xYgz8Xx8E2IbUAFbPTyBoICQFvbrdoDwaH68Bvp8YMqCsyMRxrLwG6uP_RYtDr4rfDuf0h01OHj8nLh49ZR7rDjkCfD05tHmQi9jkIB-SFNuiM9mmagd9j7HNCp1U-Ni7zq1rHZVXl9mFWHUUYEBLhAh5PxgGiBnGGwyhMDCPHmyC2yUOThq1xGQeAq-1rcl0IHA6RUDCAXc6hEWiUkUVQeI5_nMA53AlCFYhvj1Yv3bib9PpzGbP8PvpxzoHSWcUvJGZo35srR1pMsQQj4ESEDKuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVR4inm2xViVJwFKQzMZNR1Km1T4HI4D_keJo44opL_eB3XoAR4qdaILPzjtE7xYgz8Xx8E2IbUAFbPTyBoICQFvbrdoDwaH68Bvp8YMqCsyMRxrLwG6uP_RYtDr4rfDuf0h01OHj8nLh49ZR7rDjkCfD05tHmQi9jkIB-SFNuiM9mmagd9j7HNCp1U-Ni7zq1rHZVXl9mFWHUUYEBLhAh5PxgGiBnGGwyhMDCPHmyC2yUOThq1xGQeAq-1rcl0IHA6RUDCAXc6hEWiUkUVQeI5_nMA53AlCFYhvj1Yv3bib9PpzGbP8PvpxzoHSWcUvJGZo35srR1pMsQQj4ESEDKuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAm509D3wft8yFgiAGchJVqoXgoJrPSDd9t2q3mGwZyddOdZE8rBSKyRgN4aUBwopBkTh6GfsrOP85O34KgE9giblaFkIwnwHQAydcNKss82bg0Wy9CPaPgyv46zehwS8022bZopoVE98fy9RzsL3AHB0vMTbCrRNkqOj4imPlHkEbei8v-KaQ-ENsKxIqa2Ni-ybYKXJcQ-nZuXqgDFKSNikgdWmO2YReDhiWLg4EYTigcwdwSe8vyHGu5IhS30HZg_LcOrCsU6TSYlhSsmRDN9RcPbYJc3ULqveP6lK1l2dM8wsWJCRTQ-G9Gf8YORyEa0ZHOvPq4U6NS05Odg2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=Rl6eVT7reOjk8ZH_SJKyYzGp1wk0jKjxn8RT_rlBraZKRT7mD8IEfRKJH8yodkk0y_tnR3S803SuA3H7GBkgmOs7dIn_40dkdMbzFm3heZ6gz0nomb5CotIuETZ9wcq2eaUV4tCW4I8ic9RhEfjCNNsqRvSovKP5_anl9r3wauLoBJNRqey95MCBizNyAs_Ai8YktxryqyvJNTMczb0n5VM5OxiGO4yrHhctbgtKu66Rf6qBejfYtf55Z3p7EGgd7vGrmQK93nLBPRNhFekyz9xaZLrVsW9GiLf-Xt66Ohd2PRarHGD2g_jfEMgT4GeDmCdCShB8lrCT9Qq36Zfu8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=Rl6eVT7reOjk8ZH_SJKyYzGp1wk0jKjxn8RT_rlBraZKRT7mD8IEfRKJH8yodkk0y_tnR3S803SuA3H7GBkgmOs7dIn_40dkdMbzFm3heZ6gz0nomb5CotIuETZ9wcq2eaUV4tCW4I8ic9RhEfjCNNsqRvSovKP5_anl9r3wauLoBJNRqey95MCBizNyAs_Ai8YktxryqyvJNTMczb0n5VM5OxiGO4yrHhctbgtKu66Rf6qBejfYtf55Z3p7EGgd7vGrmQK93nLBPRNhFekyz9xaZLrVsW9GiLf-Xt66Ohd2PRarHGD2g_jfEMgT4GeDmCdCShB8lrCT9Qq36Zfu8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXxtCsHOV06klTDllaDoJDNJVd2xiGGVhUq9-rL0YCeZ5KSP2q_TD6mS4C1xC6HWin7L4mN-6RGJapGYE4GVv0LwHsk1M6vX9WABpU2xGdhNPkBwZlqZG8jyaGXll7d8aZQ6EOFZKgxwPVvEN2hlDixKCy9BakuSQMR7mbk6jIvalzKJbwo8XKLzxx1AovAjc-ghlAWr_qLhnBEbUI4G6PDwZf6ViX5VxZqxo8dWxrPkWfoo9SdoPThYXDKdfkSTyWqEQt8CxVvUCodvb8X69NSSGW6IYYQyfry-TT-s_gTD1kX7h3BPD7jqw1ig1H21OJIVuJtpRm5O9MKMVltaMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j45zJJLsonCXgKGcEPU-4a0q3gf93V2X0NEPzyq-e8FzdSLXWttSiK4dYiOEXSLXFXM8lEVnARFVF598t9GjaTXGag_6dCVesJUHvq09hWnZU9GEMNQGuX1Uqk3bpTKV2jF_T_wgCBzS5pQQO4bcgg55lEKkyj5BNfBxLc7KjDrkde8KpqVkfuQBW-1KI6maESMC2CLHm-5e1dsCiuLV4zHklFzxDyYW6mzLOBLUSwiO0WvJ7QMHdQXmvU828H4v4dUPOAqHu_H9pl-wgpKimyDagfrUTfG3XUkICva4u4XUR4lBU2M9UAlipPZUoWWCWiCfeH9PfqIrZ5co-XrTcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgqZPXjuN6s9tHiKuysfwMKkGfCEUE0AOfuhXX5xP3J0GNCVXi3Rh_HiWrBnKGaboDdbfraXlpSri0L8dtfuu1dACLythkZk_Rq1TofAvA3XBojLqDLkpLUTlwfRTi_17Gm9noyEBxphzdiGM0zKGkbua6D5nZAXl2U3nhbJaN9mjvLYu-CCVVIjNI8vo6-PTwMiR-H4Zt1UhnuxDECIDkkI_-QLOXoBOwpUwSwhqxeaOAtx55ht4O8HUmdYaMVfxovLMDbKkfWhG7KW42jEV_bpVER7R-9MZNCcaTr0ARB2dfWyL4EXEldTqMvxaostFQ6dYcktndCRKiOYz4cYbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=HcuNIK3PjDoE9MTkufXcXiTYyl3qkNzEk0oQcxGpEC5iEFT2G2aNDgwpjiAtNhoBDWXATpar4ikZW1DQEHHOpDsTqlmJi-m2e7Xsp-FXm-fkIMavsKWwsoS7IGPvS-svhZuL65KYhPOM0k4K1Zxq0ORLep-NIMCjCsMU33AE7cbZbwDu-Ce2xBuqAeU-CoXJ-G1_syUE05n6EBMID2qzXU1YZ4eanQeKPpjlBRD2LLACn0I7F4ejFfvCGCOqeX7ZnYiC26AsG5wUlgT3_anh9SrZ7Reevhh1apk_JKLqQmnFh0ph4-YVoRxpP5tlmS8Ll3UjLjY_D17z67FOjwHwxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=HcuNIK3PjDoE9MTkufXcXiTYyl3qkNzEk0oQcxGpEC5iEFT2G2aNDgwpjiAtNhoBDWXATpar4ikZW1DQEHHOpDsTqlmJi-m2e7Xsp-FXm-fkIMavsKWwsoS7IGPvS-svhZuL65KYhPOM0k4K1Zxq0ORLep-NIMCjCsMU33AE7cbZbwDu-Ce2xBuqAeU-CoXJ-G1_syUE05n6EBMID2qzXU1YZ4eanQeKPpjlBRD2LLACn0I7F4ejFfvCGCOqeX7ZnYiC26AsG5wUlgT3_anh9SrZ7Reevhh1apk_JKLqQmnFh0ph4-YVoRxpP5tlmS8Ll3UjLjY_D17z67FOjwHwxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVNVqAKLC9TfVCZeLGyaVkWLZWhB2NPSXn2MJO4kWF8fDZUSrEZ0Vb5HSubMVxNGWzQtvwFe6bSza9Th_R2DjMFrg6jA0688ppVENyD1eKvSMwk1n05xiUkNcOl99I0LHd5c1MrtvqORoJi9M-6bTZOO_TEugxelOrogxavgMqiFaX2xgfgoj9EjIZPBy5JH81RIMIjqgND0s5-xbnwRusc6mm8mfsjaKvkdYsGsWhjfTN6VpcVT6EjjSStAoZQJjQC9Zh5zc_09ffUMqNoCsWmEkjmfab-Imzc8SND1ck7R89Yz0mAcazxMLOH5CyHxB6NSWFVyzNORmRaEbUWUrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoAWqQ6ggw1DQFQFBkrLlgLLFt2UKD1jVzX96GOHHrshueka5XMrMxS8YMVZ2O-1x33DeBUob9v18t8X3E3kJlFGEHFfuRnoNeLpbvyfWMjCF0cKxxvOQPW_FVNpjYv_T11tfZvBzO0VtCv0Rip7xHdWrVjrIHwAx0gKpTqYU9qplcEjCfKJXQmJ9L2UiokQcj8d-MUNA-c-AJKOtwE6Dh3gYh9MwF-_DXtSWV-aiXAL4O-UoUy8x1Luzeom415mDOuGuK-aWL1kYfFJmZycSuTbM-rIGkHg6vCu6T1XlJC3PUfaqkuS3rj9jt5bmfFWs274he9y_HRMze8Po3CJqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA21Up-ZcCHaMANa59Hg1WGo82lTMNcwfHpz90oOyUkzdyT4OPmcIwQfGX1kTiK3Xb6lY4uf78tGDKhiAZCWe03AXk-u6X2oQfIMz0ZgH1jZNYRnliEC0taxraa1LQOZgLaXeTUdt4UK3GPmFHjqDuFT20tpVnsYy2sPSgm_nChTom-Ik_fKmoE6vf9NX-RGTFB3hgGOiP7v3egGebVDf7XLZyDkS1X1Q71oKkpbmDuATJYn5S58sgXL1XTg_QgBeyN-9vy_Nb58xrHKt3bRqJ5JPFqwNQOrtGiKwIyOM5sDP6hYnthp1GZK0BjLD2pdVru-8Sy6LmfIgXz3QiZLug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDEq_AbzGvigedyJvfJJS-UKvU_xHSIfOuisETsqeMVOhHT4nN3c5MZhDsF9aIQDV0BgWVm-QTk49EFaG7WF8b6ZfrT8YZHvUfLdVoaLm0c0wubtYeM4j0xR_-pLOtgmoClFPfwbRRSygX4uEfsScUvF9R28Wrn8Z7eRVR6su5E1P2wdGFNCI6W9YoDAPJpuhud51kGsWVW4y0ijqaedWbNx_i8000R5CdzyDjVZmix01Uexm_E2aMqZbeh9NQjZxPdVvfCzUP_H1Dg7_AmOhyZV78LhbLVr7wKKWcJMphi2B_sv8lUkLsTt922KryAsAcdSc67pDqyhjiVw9Vfa2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=k7k336wWQWO03wgZPinc4d-PotgcZJ5fJVRhqcIGAdyqTFtRiBQ4qXaCANzDOvaXKq_269AhyEYb8vujwmR7y0RwXc2xQMt-alDJC6mmSH3A3XL8FVB4fTZ7lc_nHV2wEdT92i_-l1sOTuiKKDcjeHK2_psjGQTjJ1zkTkwkARuFieDDbUyVrqU5oMf1VXgcBc9VOVrawl2wq077MgQ4zbJBU8w8qxe0II2ZqN7MB4-0Ro_e_rgI2V68RnTXSApNvQiAvWCXzQ2jrwHW5lBCMQ2Mz4la39jx_8q2kJVI4DrVHMia4OWM5dFqZ_DwtxgwCTvc3mTF2Ybu87wdm15hYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=k7k336wWQWO03wgZPinc4d-PotgcZJ5fJVRhqcIGAdyqTFtRiBQ4qXaCANzDOvaXKq_269AhyEYb8vujwmR7y0RwXc2xQMt-alDJC6mmSH3A3XL8FVB4fTZ7lc_nHV2wEdT92i_-l1sOTuiKKDcjeHK2_psjGQTjJ1zkTkwkARuFieDDbUyVrqU5oMf1VXgcBc9VOVrawl2wq077MgQ4zbJBU8w8qxe0II2ZqN7MB4-0Ro_e_rgI2V68RnTXSApNvQiAvWCXzQ2jrwHW5lBCMQ2Mz4la39jx_8q2kJVI4DrVHMia4OWM5dFqZ_DwtxgwCTvc3mTF2Ybu87wdm15hYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQkwB8gOvmMqyS1Ml3J_JHJbwUezvlBeuglCFzxHz1RE3BVsUyNeHIbraQZHd4ESjPFEl25ukVhANUvtsD8nz-tUEJ0BZKMvX8ZU9fY8CodY0oBNpVgaC_1ivat4FP6WI8ypAdQGnD0mOlWekXaKwtf1m8tp_uOxx0FEUVnr29sQZFDwdcfMbMXX9o8cc6TyVlBNErlDB2zTQ49I1cas5nSJYAvLcvsI2FH9lYN_jPnhpxdR-UMaJcOI9xaNy4HmtuiwQYLOOoT1hmu-aXvlKrzXQI5Do4xR__K7wnOMI5vq4cuht2NOSrH0ys1oarBDcZTUctuDS6M_fgMbXl_1YA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7q45KbpKdzNAzhy1b6qsSZ_4aycx-3lU-L-kjL6f2I55awyS2UCx1L-lVD-9gMOyu0T0tqvy_2sLiMB9gYBoCPyvojyWdSay7hOl-RMEuF90EOvTQJlFfdO5DPnwkkxMBmZSuCTHSwWcFCNlpu--u9mdlcbQsSJbDQ1QnjkrRRlNtv6HNb4OSKtd2gTS4VEkzaO_6c7jn1y_udL0k-vtnJjZDe-ibpmgXiKZhln_MHbZPPGoT977Ler95HXgULWkBl9-jWFN0LNbcuGJH2HG_aJOZrPHP8_Uhf1b01R8ouVrtg-V0TU7ZTMaHlcnaVUuWJVqjfUed7SGPh_dGO8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=RZUZUyuTZ2SIfxBO2r_V6TCUBdrG-7J2KoxF0nfCtCxMSwhsgSOspgLN3hG5QNNplBooQfLzmqZPY0JgPaNc_ddUJmc5jHGjwxQ1mHAtnURLLxxX9RbuDCcODmezTvahn-yD9PHEZDyi00N0a2QqMGJj05YNPkrEu10ZiVaREcmoYTb3fbGzsg6K-57KDwsdzeu-zm8-RN77vB8p8jgW--5C2q8T8Nbb8d0G4oTI2W9ZHhISGSFDjIrz-f0VBC-1S-Wfm-9Ybo13VrzC8i7TnrdIqzOq7Pzc1FJWOTqgEnK99jLyD0-ea0hYWSlNbcwP6c2lu713mk-MKpCj2SRX-Rtb_0bkxA5MukMC2ZpTizYiEBh1PzeplBZqob_0Am3o-32gzpkeg4CjUCeeJ28AeFBo6RBg5vduP9OnLX07LF4QrkTvUi6DHoi_x9dIc4F3YPtY8E77Y7GPXJb6T3A-87L-vbBr7SJr2CY5Nn9SbAAetB7cuKr5DoMdIfW86SRk9rUBMB0QUi0vLFY1sCY3wRVqMUS7eIiEcaYe_HFrctiAcFrrHZIxdPvmgzlUuO7Of2BP3nU-H0UGyuDAPSZ1K_puRU-Nxza41D1nlSNMyLVsh-t39JDsCqbI4sn2JeWXgshDe3JnEcb93SpTihpf47tu770BRaOspJlh3iVR2lc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=RZUZUyuTZ2SIfxBO2r_V6TCUBdrG-7J2KoxF0nfCtCxMSwhsgSOspgLN3hG5QNNplBooQfLzmqZPY0JgPaNc_ddUJmc5jHGjwxQ1mHAtnURLLxxX9RbuDCcODmezTvahn-yD9PHEZDyi00N0a2QqMGJj05YNPkrEu10ZiVaREcmoYTb3fbGzsg6K-57KDwsdzeu-zm8-RN77vB8p8jgW--5C2q8T8Nbb8d0G4oTI2W9ZHhISGSFDjIrz-f0VBC-1S-Wfm-9Ybo13VrzC8i7TnrdIqzOq7Pzc1FJWOTqgEnK99jLyD0-ea0hYWSlNbcwP6c2lu713mk-MKpCj2SRX-Rtb_0bkxA5MukMC2ZpTizYiEBh1PzeplBZqob_0Am3o-32gzpkeg4CjUCeeJ28AeFBo6RBg5vduP9OnLX07LF4QrkTvUi6DHoi_x9dIc4F3YPtY8E77Y7GPXJb6T3A-87L-vbBr7SJr2CY5Nn9SbAAetB7cuKr5DoMdIfW86SRk9rUBMB0QUi0vLFY1sCY3wRVqMUS7eIiEcaYe_HFrctiAcFrrHZIxdPvmgzlUuO7Of2BP3nU-H0UGyuDAPSZ1K_puRU-Nxza41D1nlSNMyLVsh-t39JDsCqbI4sn2JeWXgshDe3JnEcb93SpTihpf47tu770BRaOspJlh3iVR2lc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=V0Ib1YmDD56nxiZenMWDpYYoTnWMf3qUHMU-j6hX3QKtA5gU3VC6R-M6eEIVHiMjFI_X3-uuY5Z2Mbsih7lwTpAQuZdZnmfWVPBCUC76QbHIILTK8hwUKDrdiHUk_As7TvbhPsKJtbgo4KP8FVNICoaWIeviN8m9ECPoqbdC9JOZfQ7bgZFH0D9q41FBNjmdReJ-Odm8i5CcYvdZJ83OoAZJR8Wxmw6yVte2nsGie5QtCIEXjkcsYl9wY3_TPriDcm46bJMNTHzahh3u3lz0FASYHpszc5VgkKyFLY392k3o2wrYRJHMhqOTRRsyuknt3g7aHPqYlXmc8v-_oY_GvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=V0Ib1YmDD56nxiZenMWDpYYoTnWMf3qUHMU-j6hX3QKtA5gU3VC6R-M6eEIVHiMjFI_X3-uuY5Z2Mbsih7lwTpAQuZdZnmfWVPBCUC76QbHIILTK8hwUKDrdiHUk_As7TvbhPsKJtbgo4KP8FVNICoaWIeviN8m9ECPoqbdC9JOZfQ7bgZFH0D9q41FBNjmdReJ-Odm8i5CcYvdZJ83OoAZJR8Wxmw6yVte2nsGie5QtCIEXjkcsYl9wY3_TPriDcm46bJMNTHzahh3u3lz0FASYHpszc5VgkKyFLY392k3o2wrYRJHMhqOTRRsyuknt3g7aHPqYlXmc8v-_oY_GvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
