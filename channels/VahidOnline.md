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
<img src="https://cdn1.telesco.pe/file/ew1M8w4zzRSxpWchzys-bogM6nRwEcOlEem-x61UIQEAKUmHKIM93Y8ii_TOSXPBK6XuyEDOrYaoTTi6oHSUsOwSoL20HkOv5POYwYUtLswKRf9Kvlm_L8Z0JeWIZ7QvtaSc12wvSyJZb-cBjzLqogi0jWYreehgEv8L3iIuvB4zv3xhBAopIW3LxNQWSj3SBdL1EDTDGNTOg8R4MWcwoy7kAbqFs1xihqhxzHCrLL3eqbwg5mwCcZJGQkxlHO8Y4EYj2Dr3_aq3PBL9AkqDgxRT2ipnmGi0pQN8FbgdDNU8MLQpsHnJd0nOjIDs8bznwHJdlQvR5-gW6A2B8qKgdQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.36M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 12:10:17</div>
<hr>

<div class="tg-post" id="msg-76408">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/na4-mC3FoEv45PChInOVfH7pMt-72IfWrxC4LMB8JPwJUAyu923qisr8q4KDyZvTYYGnTZQ_1o4hyqRZB6hPmwAUJHI_WMeX0TbLlowqMw7IBBxRpD3AEVytyia0IncXV5cOJM4Zw64WkmsUCq7hCIwcu3RfJ-fEj61_K6XxPTzhQHYVi8v_d1Hd2rMRzjP5j71VA2-CiIouH80fju7oikDNltg_lqVwPciIHwSd5eQGTo6tskhnf9scIRSIGZ4vlJq5IEt26DCrjAvOAop863gB8zsyKLXxlwSIFrGANWdKwkgjqfen5M9o-HPMKRsRw4Yo8F0TpB-MqIDKdgvGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VbecubBQaOkneM6eAtEr0C7LAamz4nQY3lMrF4iM9PdQDALplc-SJRdkQyZ_LECQnsM31eS6Tw6KD-06V7y4Y-QUgR3CuK-VnHOkzAJXR0PoLzaGs1iuzOcNrWXh21nlbKY0-hYCV8EQwJpfoBKxEFI30bFaIt-Oz1zS1tOWfhVz-vUzYzCzVX2_gcb0JMKtpXJVe8BrpA9D53GLIJnFMki-0NigsHGTjZW09YyAbRWs3UixfSLQINGoApMVnZIymfu_yND1fCjHVbztYlQF3lnY2R-vphFnwcjM4Am93yXuKOIUKt8QufDRLiF6AxgkUBiqyq510PE9Z2w1OUk7wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مسابقه نخست تیم ایران در جام جهانی ۲۰۲۶ مقابل تیم نیوزیلند با نتیجه ۲-۲ پایان یافت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/76408" target="_blank">📅 06:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76407">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6aa89bbb6.mp4?token=S1tylYFG-hgar4kw6OP38GiNqYg9zfjxUJ_domOKnwZP9n1yvzX5UN_KyfjG17iSpMCEruUoUpsDqA94gQpBiuiZWQEk_Sy-6-6B3kzEN085lcAiqhSZgTCN6mfwRWuX6L-o81i8S2IYqE_MNUyYwTay2mXsy9NzvXbo__NmEZUYtreBjPPj01Yuqg0Vuj1cVpO6bEGf2X4077HkNtf4GmvWCvobo9tZ_U37cPt6aTa7D-lXaMpRj2EoXhONmurioWNnwKm__ALsDdNIN3v_VnR0tFjspyJfjFYbQDMqq839mYO8W1dC4y1Q8VczfZ3NGWtqxFJ3wXD2jSWvQ8pqzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6aa89bbb6.mp4?token=S1tylYFG-hgar4kw6OP38GiNqYg9zfjxUJ_domOKnwZP9n1yvzX5UN_KyfjG17iSpMCEruUoUpsDqA94gQpBiuiZWQEk_Sy-6-6B3kzEN085lcAiqhSZgTCN6mfwRWuX6L-o81i8S2IYqE_MNUyYwTay2mXsy9NzvXbo__NmEZUYtreBjPPj01Yuqg0Vuj1cVpO6bEGf2X4077HkNtf4GmvWCvobo9tZ_U37cPt6aTa7D-lXaMpRj2EoXhONmurioWNnwKm__ALsDdNIN3v_VnR0tFjspyJfjFYbQDMqq839mYO8W1dC4y1Q8VczfZ3NGWtqxFJ3wXD2jSWvQ8pqzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس معاون رئیس‌جمهور آمریکا ویدیویی منتشر کرده:
رئیس جمهور از روز اول صریحاً گفته است: ایران هرگز سلاح هسته‌ای نخواهد داشت.
بار دیگر، تلاش‌های رئیس جمهور ترامپ برای برقراری صلح، علیرغم تلاش‌های بی‌شمار افرادی که از آمریکا و رئیس جمهور ترامپ متنفرند، برای مردم آمریکا نتیجه داده است.
JDVance
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76407" target="_blank">📅 03:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76406">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ef6Em01JhumiRMKDA_xTvEklKgVzWKDjkNzL3fP5hAR4gI-HOzm4Yl5uHeAxnlOfWEupDIOzhiEGen2Fp4IdHHN2Q0UOGJ8lfCCmuva2dEv6vpyppqF7jn3VXPFCm3M3eZaFt-mUb8TYjjk80wPbo1TKlotw7mdHQ_0jiZ34d3MYzlE6rBaGabrTR3GYu8C9C63K391AJw-ITkQa3LudD8xG_fk8KtLeYvgLrXDPFtslsS___0SASAG3drw3_FXA4IWU3eARGb69kPS_tOSKWKZWmBjttyCY6vJTJSnuuEqMLwH3TLJYBgmT32cTPhJKyUEeWsU2oHqHRjfDsVy7ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه و توضیح ماشین:
ایران موافقت کرده است که هرگز سلاح هسته‌ای نداشته باشد! همچنین، داستانی که می‌گوید آمریکا ۳۰۰ میلیون دلار به ایران پرداخت می‌کند، خبر جعلی است که دموکرات‌های احمق منتشر کرده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
(عبارت «Dumocrats» ترکیبی تحقیرآمیز از
Dumb
و
Democrats
است؛ یعنی چیزی مثل «دموکرات‌های احمق»)
realDonaldTrump
البته حرف از سیصد «میلیارد» دلار بود نه میلیون. ترامپ هم پرداخت از سوی آمریکا رو تکذیب کرده ولی
ونس هم نگفته بود که آمریکا قراره بپردازه
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76406" target="_blank">📅 02:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76405">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vx77_MFz5TGOdoRSZTvQWgtpNSWaYym_3CzBXdqs9YXUij3PMcskL6pc3IdnTi4YvQqe5Nw6xVpsu3tjrBfO7oAjW74dN3dKBY0LgXY_tZp95owoj3HNoOuF4hpqUsvkPYsxXp2JXOlA2mJDDGX2NUs3xGDvbg5MeKuiIuT7hO31rFpSdNS-BfcUoLHfXBbNWbLcXgsXd-yKOdHjd3PFBu0HPUKzBBH4D0O5kODtPW-cd4k353sF0HSRgDPWeTivTUI3WdL-g7ZIwkq9BZlT3XikT7aYKiWwjctwWz-E5JsJ0rGfwmzWGUzTv55NHLHEHG_K9rDiOwnwtbEXb5UnyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه منبع مطلع که با خبرنگار اکسیوس گفتگو کرده‌اند، می‌گویند: جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (سیا)، به دونالد ترامپ و دیگر مقام‌های ارشد دولت گفته است اطلاعاتی که چند نهاد اطلاعاتی آمریکا جمع‌آوری کرده‌اند، درباره آمادگی ایران برای ارایه امتیازهایی که واشینگتن در یک توافق نهایی هسته‌ای میان دو کشور خواستار آن است، تردید‌های جدی ایجاد کرده است.
براساس این گزارش، رتکلیف تنها فردی نیست که در تیم ترامپ دچار تردید است. مارکو روبیو، وزیر خارجه آمریکا، و پیت هگست، وزیر جنگ، نیز در نشست‌های داخلی نگرانی‌ها و پرسش‌هایی درباره این توافق مطرح کرده‌اند.
در مقابل، جی‌دی ونس، معاون رئیس‌جمهوری، و استیو ویتکاف و جرد کوشنر، نمایندگان آمریکا، از توافق حمایت کرده‌اند.
به گفته دو منبع، ترامپ و تیمش اطلاعاتی را بررسی کردند که چند نهاد اطلاعاتی آمریکا جمع‌آوری کرده بودند و نشان می‌داد شیوه‌ای که مقام‌های جمهوری اسلامی در گفت‌وگوهای داخلی خود درباره توافق صحبت می‌کنند، با آنچه به میانجی‌ها و آمریکا گفته‌اند، همخوانی ندارد.
به گفته دو منبع، رتکلیف و روبیو اعلام کردند که بر اساس همین اطلاعات، نسبت به این‌که حکومت ایران با اقدام‌های هسته‌ای مورد نظر آمریکا موافقت کند، تردید دارند.
یکی از منابع مطلع گفت: «اطلاعات موجود نشان می‌دهد نیت‌های ایران با تعهداتی که در چارچوب توافق پذیرفته، همخوانی ندارد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/76405" target="_blank">📅 02:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76403">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/luSoKwqbBJDLFfKOQU_CrHhmlyHkYZmnY4eDfaJSKm0qymV96G15juJh_LYfep7lmiOwPWr-NlS6p3rKakkC2V3IwxTOZTUneh_lFnwRSiwGmDt6PgxZn-ppB50k8ujLKlW40gppHymUgTUD3IeaPdSIFhxuimCp_vIaGsPtMgSNKsEY1bXIxBZYAy16tYJFH1mZRTBd8UyzeU1u-EE-CGSgP01UO0Nt_XZCxBdrobUlODEBgNI7elyFcyvdvdfgyBTHgK2xb3Jn16iGQEf28E_Ta8pAJ48h5U3gIJGjYlQ95WMHtpYYl6cQQ6h25wGAXRnD1pMAZdTbi4TKceCPrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cqx9F8MzgW_uIib0LQ2t9uYt-_5SRj4zOzh_Qvzk7qeYEgc1axODg-YbErig5JvsWvMbyMbxJoGu6hgkKDnvW0DtqfgK_PB1GeoAw9bXodIQRZVkpH8C0_vepx4rQ0g5SfJs_abrjulSt-s6VLNmwqN2TT0eos4ERZ2zpUjoUWewnYBIqJ3uhuzq9aQ_lhB-i_K3c1C5RTNshvsTyf4dz0DL11gLJGyCO2l-yrhuATfN-rbFrdi9Dn4WTfHBTMoepVa6T57_wiTPJGLMj-n-sc2Soxx5TJPoKFYIu7zDsOgV7WzKQsTekBYHoChAas0DzIr0IRB54CUf-ZzylzrE1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری ایالات متحده، روز دوشنبه در گفتگو با «سی‌ان‌ان» اعلام کرد که یادداشت تفاهم میان آمریکا و ایران سندی بسیار کلی و در حدود «یک صفحه و نیم» است.
ونس با اشاره به اینکه این متن تنها یک چارچوب کلان را تعیین می‌کند، تاکید کرد که جزئیات مربوط به موضوعات مختلف باید در طول مرحله مذاکرات فنی آینده مشخص و حل‌وفصل شوند.
به گفته او، این تفاهم‌نامه ساختاری را ایجاد می‌کند که بر اساس آن، ایرانی‌ها در صورت پایبندی به تعهدات خود، از مزایای این توافق بهره‌مند خواهند شد.
معاون رئیس‌جمهوری آمریکا در بخش دیگری از این مصاحبه گفت که در همان «بند اول» این سند، انتظار واشنگتن مبنی بر تعهد ایران به «صلح و ثبات منطقه‌ای» به صراحت مطرح شده است.
او تصریح کرد که بر اساس این بند، همان‌طور که ایالات متحده به صلح متعهد است، تهران نیز متعهد می‌شود که تامین مالی سازمان‌های تروریستی خشن و دامن زدن به بی‌ثباتی در منطقه را به طور کامل متوقف کند.
@
VahidOOnLine
جی‌دی ونس، معاون رئیس‌جمهوری ایالات متحده، در گفتگو با «سی‌ان‌ان» ضمن تکذیب گزارش‌های مربوط به آزادسازی زودهنگام اموال ایران گفت: «تا این لحظه حتی یک دلار از دارایی‌های مسدود شده ایران آزاد نشده و هیچ‌گونه کاهش تحریمی از سوی ایالات متحده یا شرکای ما در خلیج‌فارس صورت نگرفته است.»
ونس با اشاره به گزارش‌های نادرست در این زمینه افزود: «تندروها و برخی عناصر در داخل ساختار سیاسی ایران، برای متقاعد کردن افکار عمومی خود، دستاوردهای تهران از این توافق را بزرگ‌نمایی می‌کنند، بدون اینکه به تعهداتی که ایران برای کسب این امتیازات باید به آن‌ها تن بدهد، اشاره‌ای کنند.»
معاون رئیس‌جمهوری آمریکا با تاکید بر اینکه این توافق در صورت اجرا شامل یک بسته کاهش تحریمی بسیار بزرگ برای مردم ایران خواهد بود، تصریح کرد: «این تفاهم‌نامه نحوه تعامل ایران با جهان و منطقه را به طور اساسی تغییر می‌دهد، اما تهران تنها زمانی از این مزایا بهره‌مند خواهد شد که به تمامی تعهدات خود عمل کند.»
او در پایان به مخاطبان توصیه کرد که نسبت به بیانیه‌های تبلیغاتی و پروپاگاندای حکومت ایران بدبین باشند و تاکید کرد که بهره‌مندی از این فرصت بزرگ، کاملا به پایبندی عملی ایران به وعده‌هایش بستگی دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76403" target="_blank">📅 01:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76402">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Za3NNrJU9RP12LEBpz54KV4R-a0ibQiB6B1HHiR_HgyRUD9ptljlpLZhmmdFDtDBkJVK46BqHEe3ZDeP6M2H2o6Im_i_mw0EcsYBptL1j6JWnEgm2wZbg4b2NQ1fdWbe5St3kBzJmkck5ynE0nGLmVWuSugQK7jjS_bxt3ui8JN5LX_cXevsJI9X8hD81DRJ7WN61sJj-uxfHhlMbM2GFvtHDYoBptS-W449xuaaQ30BuEGG02IQzcXv3VIJyaM-3YObu-_KriEY4xEjN6klKrUXfeyUOSxB6TuoqtKPbJd9pZ8YcCK5DOcSMkkb0mF_BAhryj6eJQxrHKWfuu00-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر:  منابع محلی از شنیده شدن صدای انفجارهایی در مناطق جنوبی جزیره قشم و تنگه هرمز خبر می‌دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76402" target="_blank">📅 00:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76400">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OMVVGf5fymJHrOlPl7J6YerdAHEIMM56G0bkK4JexeDX6A19cs7quUNx6zHC7wHFHXhuq55z0gUWBbiD46pJAd46YyQnDFCMFPlQMaFWYHp0N4TlhVDUvAZCVBmuB6bIQZPPn0Rvfk3L59cinTB3pyWZcC6s4pFvXxWUGQBzPGWczvonx1KOcSQGHkDp0S4bmUkxGIP9N5joWcDyNikSJdsC4Zv-Y4JFvEhtjmnESQ1NhgLtJ-jqm-IeRxQ5ZHPyedy3BttV6quK_yAIgzVJMP0Ae-UWselEhBcmpjjuXP2Kn-ytuFAhG9GJnBNOJCe6p6CFIWEHJWGwn2DMhqw3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vyBa2oy0YauJIMiAR7-Rqb6zk1FytHw0LgJlERDm-vV38OM-GKVNsGlMfekku4q5UB7bW4isDLNdaBaFGSOB_9jq1buf_biCj8Tb8WErcsRSbI6tFDazrvpKu5USZEcCoxcanf73FM28R4NR2UWQt3Za0WHPUQJResderPvrH6sUGWo-VSHlyWtifb2lTg0sOQFmDjC3WCAj0uzmMr_c9-Ufc1xAOes6ONy0TUEwV3VLCdbkJRcgzl_rPzWB_10QM8Oz-2S8_JGBsbbbkEgPnOdcyLWCpxJWBOdSQ74Pam7LqOb9SN4FMc23KuzMNHkBVX0bMqgu09rCbDnq8GLllQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، نوشت: رفع محاصره دریایی عملیاتی شد و ۳ نفتکش و ۲ کشتی حامل کالای اساسی جمهوری اسلامی از محاصره دریایی عبور کردند.
پیش‌تر ‌‌ارتش آمریکا در یک یادداشت هشدار اعلام کرد که محاصره بنادر ایران تا زمان تکمیل یک توافق آتش‌بس با این کشور که برای ۱۹ ژوئن (۲۹ خرداد) برنامه‌ریزی شده است، همچنان برقرار است.
@
VahidOOnLine
بر اساس گزارش فارس، دیگر خبرگزاری وابسته به سپاه، یک نفتکش غول‌پیکر ایرانی (VLCC) به همراه یک کشتی حامل نهاده‌های دامی با گذر از منطقه محاصره در آب‌های آزاد به سمت بنادر ایران حرکت کرده‌اند؛ هم‌زمان یک نفتکش دیگر نیز با عبور از دریای عمان و خط محاصره، مسیر خود را به سمت مقصد صادراتی پیش گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76400" target="_blank">📅 00:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76399">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پیام‌های دریافتی نیم‌ساعت پیش:
صدای انفجار سیریک ولی با فاصله تقریبا دور
سلام وحید
۲۳:۵۷ دوشنبه ۲۵ خرداد قشم
خودم یه انفجار و موج رو حس کردم، اما بچه‌ها میگفتن دوتا بوده و قبلش هم حس شده، جایی که من هستم نزدیک تنگه است، شاید از روی دریا بوده
۰۰:۰۴ سه‌شنبه ۲۶ خرداد
مجدد دوبار احساس شد
سلام وحید خوبی
ساعت ۱۲ و ۵ دقیقه سمت سیریک صدای انفجار از سمت دریا اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/76399" target="_blank">📅 00:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76396">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HntGbkvcHHjD7eRDd-Z3JQprMS7KX7DgF5CKmevhAe9kZDicP3YUVcfmLTCiusQnV0MKnO1lrSeRS8lX3T8nnDcjc--vn2hDzG4Fb-B6Tyi2rXe5mDgZXIXuWYVd4RVSsXJqjSxrwWxFl23EwQdXBugbDrZgBQarfuLGSaYlG8CqLTE_aPu63z6viEKCmK6QZqUyC0ZRTL-EhBNYurJ2eEZKXPavqSrKJMqVQVVNrx_wxptsVo0QLbMrMm67YKQqmRaaaqxdtX5ualO0w7sAeoJgoYhzXUWINYiRBkxGOQENIOVF8G96a5EN693eJ-XzhAjoNbbC4Blp-FqwdROXfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/759110416d.mp4?token=hOFT54LFwXtZLI7TKt_zubDAkS2NqorkgzHwsQZJmIs7_KP6eJKamj-yCR7OdSB9DYAcS7pi9K9uaROfUIE4PnUIFaF9FPivpzQ8mJxL2ZEmRwqyONeAzICD850Za7xcr4qNOlGydT1IJvoWcxoESHEfNKYXP3MvhLhnXYE7cSo_KhYqO257PN2UDAQs9PLy-lZbMeeu9zDqfbZVAQwkjBsPIHC0GMuamQxdN2NuTNd7domYZZrWt0UGy6Uv6jqy1ySAWfiVEKpRUSOox44CvGQuAx2P2nbyI-2blQCUNxXTxXKzPMR1k9ziWFEEqQad6XJnc6JuWx2gR3cA-kZTfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/759110416d.mp4?token=hOFT54LFwXtZLI7TKt_zubDAkS2NqorkgzHwsQZJmIs7_KP6eJKamj-yCR7OdSB9DYAcS7pi9K9uaROfUIE4PnUIFaF9FPivpzQ8mJxL2ZEmRwqyONeAzICD850Za7xcr4qNOlGydT1IJvoWcxoESHEfNKYXP3MvhLhnXYE7cSo_KhYqO257PN2UDAQs9PLy-lZbMeeu9zDqfbZVAQwkjBsPIHC0GMuamQxdN2NuTNd7domYZZrWt0UGy6Uv6jqy1ySAWfiVEKpRUSOox44CvGQuAx2P2nbyI-2blQCUNxXTxXKzPMR1k9ziWFEEqQad6XJnc6JuWx2gR3cA-kZTfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه نیروی هوایی ادواردز آمریکا اعلام کرد یک بمب‌افکن بی-۵۲ روز دوشنبه ۲۵ خردادماه در ایالت کالیفرنیا سقوط کرده است.
بر اساس بیانیه منتشرشده از سوی این پایگاه، هواپیما «اندکی پس از برخاستن» از باند فرودگاه پایگاه ادواردز و در ساعت ۱۱:۲۰ صبح به وقت محلی دچار سانحه شد.
در این بیانیه آمده است: «تیم‌های امدادی بلافاصله به محل حادثه اعزام شدند و عملیات امداد و بررسی همچنان ادامه دارد.»
مقام‌های آمریکایی تاکنون جزئیاتی درباره علت سقوط، سرنوشت خدمه یا میزان خسارات احتمالی منتشر نکرده‌اند.
«بی-۵۲ استراتوفورترس» یکی از مهم‌ترین بمب‌افکن‌های دوربرد نیروی هوایی آمریکا است که از دهه ۱۹۵۰ در خدمت ارتش این کشور قرار دارد و توانایی حمل تسلیحات متعارف و هسته‌ای را دارد.
@
VahidOOnLine
آپدیت:
هر هشت سرنشین آن جان باختند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76396" target="_blank">📅 22:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76395">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10d585b107.mp4?token=ev3SdQ5_x6jv5gOiQV-SIWvIFapMbbbmSk-0_kmw2pUpaj4txfHIIwkWE37LJCHkwH0Zt25cEkNMPAkvrvBCOgog8cvnY2Cl0VHtorHjPbpIZDeVBg6Z6aJEIy_0pWFMO3MoDqR5u2iCLmQLeMIxL-5ILxIVujs2MUydViE-TDD1Ba6DxjtTC3VQuK13J02zKO4Dk0redFflRwv12pbLyqRCOtAUoEva0pSc5GN2SE8ad8XN0YckII5W5QJNmpbdxWtSpFyl5Hi7apm2F4YFO5eLmyxyA7ty7Nr06y9LCJUJpjUEY3AEBA8y7auF-DH6TXTEYP6FwcNEyghM9eKK2jjJC032Gf7Yo0BK2EKyT7vyAAUO6mL_oXXeZ38UkKrlI8TYmfu4ngKwocfu58E06Bl7LxmDPldpwNKGbea1ql9k8ggmFraQkyU3FgrBEC7IIes4N94cW7MA8_n0HVtiASWWOgZnh3WA47n5tnKSyp90jm4jNpX6pGvxr9PyqWZ3K2_i5J1ECil8sqMOLkgiuinFZZX_QfFLjV7npmFby4nYdV-BfvIreHliGbQFkM3TTABmzteVJxEiSwh34e9A5K47nIE6Ul0TTPe0H-t2HiPTkE_-NjuGxvTUZqUV15bq01_XIfRPqVINmGE6OAIljAe1NBTQWNXM_iNQK9Kufeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10d585b107.mp4?token=ev3SdQ5_x6jv5gOiQV-SIWvIFapMbbbmSk-0_kmw2pUpaj4txfHIIwkWE37LJCHkwH0Zt25cEkNMPAkvrvBCOgog8cvnY2Cl0VHtorHjPbpIZDeVBg6Z6aJEIy_0pWFMO3MoDqR5u2iCLmQLeMIxL-5ILxIVujs2MUydViE-TDD1Ba6DxjtTC3VQuK13J02zKO4Dk0redFflRwv12pbLyqRCOtAUoEva0pSc5GN2SE8ad8XN0YckII5W5QJNmpbdxWtSpFyl5Hi7apm2F4YFO5eLmyxyA7ty7Nr06y9LCJUJpjUEY3AEBA8y7auF-DH6TXTEYP6FwcNEyghM9eKK2jjJC032Gf7Yo0BK2EKyT7vyAAUO6mL_oXXeZ38UkKrlI8TYmfu4ngKwocfu58E06Bl7LxmDPldpwNKGbea1ql9k8ggmFraQkyU3FgrBEC7IIes4N94cW7MA8_n0HVtiASWWOgZnh3WA47n5tnKSyp90jm4jNpX6pGvxr9PyqWZ3K2_i5J1ECil8sqMOLkgiuinFZZX_QfFLjV7npmFby4nYdV-BfvIreHliGbQFkM3TTABmzteVJxEiSwh34e9A5K47nIE6Ul0TTPe0H-t2HiPTkE_-NjuGxvTUZqUV15bq01_XIfRPqVINmGE6OAIljAe1NBTQWNXM_iNQK9Kufeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"خون آقامون رو چند فروختید؟"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76395" target="_blank">📅 22:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76394">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4de6c46b4e.mp4?token=PYx32xybSPI8RuZOTJ-qiYrElfiMKa-6cL-kyqsmAF3RjvdWWSFhu4WGAfEUvVq2aN2rAhKD9zc0px5_QlXQjvD5lkH7YbcWgGs7dHi7QhVJebS6qbNoKT68Kre_00Zt_RxO4UnopaH_5JgAbe8_Pp_XatWbFO55yLddSVSbFI317uwrZOnZliQWKsykxPGQZt0qphgUL1TE2fH9fTHd_zkhAzsQmbFuh0noo2VfwMYsOTrGPYXQV0cueML6MsthGWPFVBCKQa5pAJtLwp2tKdWPPcZogvV2qnl5Al_onLs7ZxE8pmnQBdYegg6GI-inrYR_pxHWZnliQMIYmH3Dmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4de6c46b4e.mp4?token=PYx32xybSPI8RuZOTJ-qiYrElfiMKa-6cL-kyqsmAF3RjvdWWSFhu4WGAfEUvVq2aN2rAhKD9zc0px5_QlXQjvD5lkH7YbcWgGs7dHi7QhVJebS6qbNoKT68Kre_00Zt_RxO4UnopaH_5JgAbe8_Pp_XatWbFO55yLddSVSbFI317uwrZOnZliQWKsykxPGQZt0qphgUL1TE2fH9fTHd_zkhAzsQmbFuh0noo2VfwMYsOTrGPYXQV0cueML6MsthGWPFVBCKQa5pAJtLwp2tKdWPPcZogvV2qnl5Al_onLs7ZxE8pmnQBdYegg6GI-inrYR_pxHWZnliQMIYmH3Dmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی:
قرار است روز جمعه در کشور سوئیس که محل دقیق آن مشخص خواهد شد، یک دیداری بین هیئت‌های دوطرف انجام شود، که در آن روسای هیئت‌های دو طرف ابتدا این یادداشت تفاهم را امضا کنند و پس از آن اولین دور مذاکرات بعدی را داشته باشیم.
محمدباقر قالیباف، رئیس مجلس شورای اسلامی نیز در واکنش به امضای تفاهم‌نامه توقف مخاصمه خطاب به مردم این کشور گفته است: «با مقاومت تاریخی شما و رشادت نیروهای مسلح دربرابر آنان که قصد جان این ملت و نابودی و تسلیم این مملکت را کرده بودند، ایران گامی بلند به سوی پیروزی نهایی برداشت. می‌خواستند و نتوانستند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76394" target="_blank">📅 22:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76392">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c3fdaedd66.mp4?token=KCxhOMCUMbLnUYEDbiaa1-ZwuiarNiwPwOZRpq9SRjYwI7KFeicVCzLFX3p18lgszXdk31xDw8zRfXUxAo8uBNw5ckoCDbaWbU0z6asv1FLcnrCmTMj4Qr6nSfxOIqAFsnqafhsKn10QEwR33WmtnLNxn4K-W3YPIzb1C2fbNC55PW_bGKrNT24rkApXaCWJp4VulzrBGC1j2Q1QobMaepiMuED_RbbRJ4hXhWQbx5mltnlS6UO7Xh9ZCZrapYkSRRhKeN5tK6YsPJQjpkuOHYR67dblEbyXhFbtYRslJy6YZnVNiToAXuJP229qDcXo1ZMELlzIpteiomBOJ4y9-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c3fdaedd66.mp4?token=KCxhOMCUMbLnUYEDbiaa1-ZwuiarNiwPwOZRpq9SRjYwI7KFeicVCzLFX3p18lgszXdk31xDw8zRfXUxAo8uBNw5ckoCDbaWbU0z6asv1FLcnrCmTMj4Qr6nSfxOIqAFsnqafhsKn10QEwR33WmtnLNxn4K-W3YPIzb1C2fbNC55PW_bGKrNT24rkApXaCWJp4VulzrBGC1j2Q1QobMaepiMuED_RbbRJ4hXhWQbx5mltnlS6UO7Xh9ZCZrapYkSRRhKeN5tK6YsPJQjpkuOHYR67dblEbyXhFbtYRslJy6YZnVNiToAXuJP229qDcXo1ZMELlzIpteiomBOJ4y9-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، در گفتگو با شبکه سی‌بی‌اس اعلام کرد ایران در صورت پایبندی به تعهدات خود ممکن است به صندوقی برای بازسازی دسترسی پیدا کند که از سوی کشورهای حاشیه خلیج فارس تأمین مالی خواهد شد.
ونس با اشاره به مزایای احتمالی توافق برای تهران گفت ایران «ممکن است» حدود ۳۰۰ میلیارد دلار منابع مالی برای بازسازی از کشورهای خلیج فارس دریافت کند، اما تحقق این امر را منوط به اجرای کامل تعهدات جمهوری اسلامی دانست.
او افزود آمریکا با سرمایه‌گذاری کشورهای حاشیه خلیج فارس برای بازسازی ایران موافق است، اما این اتفاق تنها زمانی رخ خواهد داد که ایران به برنامه هسته‌ای خود پایان دهد، فعالیت‌های مربوط به مواد غنی‌شده را متوقف کند و با یک نظام بازرسی و نظارت گسترده موافقت کند.
معاون رئیس‌جمهور آمریکا همچنین تاکید کرد رسانه‌های نزدیک به حکومت ایران بر مزایای توافق تمرکز خواهند کرد، اما از امتیازاتی که تهران باید در مقابل واگذار کند کمتر سخن خواهند گفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/76392" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76390">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PqUe-DkQkZQZf1ZqB8v9Rc5cus2VO8-ptIlcKlsPA9jtol0PqEPLiGOYpGW5pJo8NODZmbQ7QqfGpW1XvKLnE6M7mYVjfOek0BDd4klHt3kA5EXoKegwTAGHIN_a6Orc3Svz7dqWnNxJ7UAW83JtDI9PVszmY5uGrSNuXhPHfnmwNjHrgdTevZl5CflR7pfi2JAEXmEDa04b4xcSKazs9Kkiu-qYFDW44p31b8-98Jg3NG5CSofTuaj9jnM15hkklgfE0iSdkAkaNF7VvKWnmtDlJ3uQESe1dRrlBKfVZVRd8BM3yxWkou3LUdLbZ_EA4aJ2RKM2IUUmOrBVtjV2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iZR_Yq3RtRZ2u6GlJjFhBv8Op1zBOnWk9ItayqiUBCTJoqS9chl6r9v-5AnJ3lJGGXh-dT6Y9FyjdZmpgYQKm5gciZ58f2OuepvF3h_zXFxZUDKcLoCeQG9-1Im5PtM_6T0GFdgemhLqMRNlmPhPOlGOxcvDJE34ywefCc4XIXmr0s1JiQvy51FsWlOorPGvIsFpvQdqGz66yC1PbFPvAAZKnuhssB-FPQrhOKjVlmVjXu3nxTGaGV1HRM4m1t_ukgcEqGZI6Qr1P9snZw_iTHdzmqB4392n7vB_p84u0Ud4fIQoMr8GZdkRt51Ey46PJmR2gtC6BZnI2QGUBX6S7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
ویدیوی قدیمی منتسب به تیراندازی به هواداران حکومت در تجمع شبانه
🔹
ویدیویی در شبکه‌های اجتماعی منتشر شده که ادعا می‌کند صحنه تیراندازی به مخالفان توافق با آمریکا در تجمعات شبانه هواداران حکومت ایران را نشان می‌دهد.
🔹
این ویدیو قدیمی است و ارتباطی به تجمعات شبانه هواداران حکومت در ایران ندارد.
🔹
ویدیو مربوط به دهم اسفند ۱۴۰۴ و برخورد پلیس عراق با هواداران جمهوری اسلامی است که سعی داشتند به سفارت آمریکا در بغداد نزدیک شوند.
🔹
گزارش‌هایی از تجمع مخالفان توافق جمهوری اسلامی با آمریکا منتشر شده اما خبر تیراندازی به آنها در هیچ منبع رسمی منتشر نشده است.
🔹
این ویدیو پیش‌تر نیز با ادعای نادرست دیگری به اعتراضات دی ۱۴۰۴ منتسب شده بود.
🔹
بنابراین فکت‌نامه به ادعای مطرح‌شده درباره این ویدیو نشان
«نادرست»
می‌دهد.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/76390" target="_blank">📅 22:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76389">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccb668e4af.mp4?token=W49Aa94tJ35QfnSM3J99qEJjIwwKMlFm6XfCxk6MIY5P7Sz0oAWOXgQTYsGKy1a8TVTqF179HsfE7lDPwrwgUz-dlUAt3NHOpMJRgMXjSJqv7j5HJeDBkMIxQQJ8Iid1ulv8Q6f8Q3hM_502r-XKUXJoCdGRVikGWpxdYw6VtcPLN-ztg-4hvEGtECoRdLHOUyrDc-fVWvhbo80dwvjF2xnMzXAJoAdv4gMpz6ks8HXgVZRDB5S5JZ27DNLuWABsL9pGAB9UhT6sh4CQVOh-clAq3EwGrKsE_pGQlUywP_X1wl5_1qzF08wt1CghMBw_iptuB5LPY7yNZV_cBVcgTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccb668e4af.mp4?token=W49Aa94tJ35QfnSM3J99qEJjIwwKMlFm6XfCxk6MIY5P7Sz0oAWOXgQTYsGKy1a8TVTqF179HsfE7lDPwrwgUz-dlUAt3NHOpMJRgMXjSJqv7j5HJeDBkMIxQQJ8Iid1ulv8Q6f8Q3hM_502r-XKUXJoCdGRVikGWpxdYw6VtcPLN-ztg-4hvEGtECoRdLHOUyrDc-fVWvhbo80dwvjF2xnMzXAJoAdv4gMpz6ks8HXgVZRDB5S5JZ27DNLuWABsL9pGAB9UhT6sh4CQVOh-clAq3EwGrKsE_pGQlUywP_X1wl5_1qzF08wt1CghMBw_iptuB5LPY7yNZV_cBVcgTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد نیروهای اسرائیلی در آنچه «مناطق امنیتی» در غزه، لبنان و سوریه خواند، تا زمانی که برای تأمین امنیت اسرائیل ضروری باشد، باقی خواهند ماند.
بنیامین نتانیاهو، نخست وزیر اسرائیل، روز دوشنبه در یک کنفرانس خبری تأکید کرد که به‌رغم امضای تفاهم‌نامه میان ایران و آمریکا، چالش کشور اسرائیل به پایان نرسیده و «ما باید گوش به‌زنگ بمانیم و در مواقع لزوم از خود دفاع کنیم».
به گفته دولت آمریکا، جمهوری اسلامی در قالب تفاهم‌نامه‌ای که روز یک‌شنبه امضا شد تعهد داده است که هرگز به دنبال سلاح هسته‌ای نرود.
نخست وزیر اسرائیل در ادامه سخنان خود تأکید کرد که «با یا بدون توافق، ایران هرگز به سلاح هسته‌ای دست نخواهد یافت».
نتانیاهو در نشست خبری خود همچنین گفت که حملات مشترک در کنار آمریکا به ایران خساراتی سنگین وارد کرده و به گفته او «بعضی معتقدند که خسارت اقتصادی به ایران یک تریلیون دلار بوده است».
او در ادامه گفت:
ما به مردم ایران قول دادیم که شرایطی را فراهم آوریم که رژیم آیت‌الله سرنگون شود، نمی‌دانم چه زمانی این اتفاق خواهد افتاد، ولی خواهد افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76389" target="_blank">📅 22:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76386">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d206f4a845.mp4?token=UGCOo4M8_LfZStPBHFnu4PLVK4BvmL_WkJAoaydrXLWn1BXsMgyiUVCfqMxH6AhH0p0qGMtT0AdBXW8W0VM3vQxygyz19euS-7l7RSt-gOBNzkTvSr7-ybSdR25vsC34T4x7R8itpOcRlpt6ztczkDHv1NPfRjFPohtQ083lKKQ-qip2QIurmvHDhmG6hLdl-n0rw1PBEelyG1BS4j6BPojIPVlLo34OSmBgBdKvrGquDPC_YWot9nUts6-oYL5ICADvjUwGWpFNaYxUc7s9GoZ9YojzsNheVhlq77QvKLviA_bTxzRkVp7S0uIeVYuIstSzKpoX84N0orFUH28GxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d206f4a845.mp4?token=UGCOo4M8_LfZStPBHFnu4PLVK4BvmL_WkJAoaydrXLWn1BXsMgyiUVCfqMxH6AhH0p0qGMtT0AdBXW8W0VM3vQxygyz19euS-7l7RSt-gOBNzkTvSr7-ybSdR25vsC34T4x7R8itpOcRlpt6ztczkDHv1NPfRjFPohtQ083lKKQ-qip2QIurmvHDhmG6hLdl-n0rw1PBEelyG1BS4j6BPojIPVlLo34OSmBgBdKvrGquDPC_YWot9nUts6-oYL5ICADvjUwGWpFNaYxUc7s9GoZ9YojzsNheVhlq77QvKLviA_bTxzRkVp7S0uIeVYuIstSzKpoX84N0orFUH28GxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'
#آتش‌سوزی
در  شهرک امید
#تهران
'
تصاویر دریافتی از شهروندان،‌ دوشنبه ۲۵ خرداد، حدود ساعت ۲۱
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/76386" target="_blank">📅 21:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76385">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e8cc0eeaf.mp4?token=F6akmQ5P1NaFn5Y8XctSjgoU5ObNG8iB0nIx8FQHZZiAM9_zMYMBrtdtxhAWaykouROJiKpI2UYa7orMUZdJp7cHf_vRe9wG7NX1A6H31sPSeOEx45Qvwbx6Jti11kiVK9aIBlhavS4yj88gUshhVYoE1i3GBduytLfsJYlgkUx11FvT6_oPjhmHdyZo2_p3Sk3uLvwkSPgTN12jV8Xw6ZAplw5vnKNMuQZaIuFDtRyCGVsucl6mdByLpPCqMpAnZTys8Tqsi2bRtrtLN8tf5SAyGnThG7DhGJFYYRAr4Pqx3ity6roiI6-9aL6zar1GYtEaE25Fr2bRp8aiz4VSpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e8cc0eeaf.mp4?token=F6akmQ5P1NaFn5Y8XctSjgoU5ObNG8iB0nIx8FQHZZiAM9_zMYMBrtdtxhAWaykouROJiKpI2UYa7orMUZdJp7cHf_vRe9wG7NX1A6H31sPSeOEx45Qvwbx6Jti11kiVK9aIBlhavS4yj88gUshhVYoE1i3GBduytLfsJYlgkUx11FvT6_oPjhmHdyZo2_p3Sk3uLvwkSPgTN12jV8Xw6ZAplw5vnKNMuQZaIuFDtRyCGVsucl6mdByLpPCqMpAnZTys8Tqsi2bRtrtLN8tf5SAyGnThG7DhGJFYYRAr4Pqx3ity6roiI6-9aL6zar1GYtEaE25Fr2bRp8aiz4VSpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی از
#آتش‌سوزی
چیزی به اسم "موکب"
منابع حکومتی به نقل از سخنگوی آتش‌نشانی تهران: آتش گرفتن گاز پیک‌نیک در یک موکب مستقر در میدان تجریش
#تهران
باعث سرایت آتش آن به چادر شده و دود بلندی در منطقه  ایجاد کرده است. بازار تجریش از این آتش آسیبی ندیده و آتش به سرعت خاموش
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76385" target="_blank">📅 20:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76384">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sfDFAFFPc1-HriSePaKoR9OX99iQ4NKh49NnlhMqak_okUKptFWBgWZvrEgw8N4dnKtr5dBMw_SXpkHY583J_4RjvzEMEaKQucYb5_F3Axik6gSW-OiMeUkO0ea4omgqDc8_agnFNsK3ZqZNlb9XMyEBG_UGDaVBVkd8RhoF01mi3vmuyT9j9_CwbckgAjelGzA8YjVWeZIARuqZWQj-fbjwhn7UdTj2MbkxBe_2mblMZbwd5x1yDSCyp_ITsdho3ATyfQmIoVl9Yy5m75aRucXg1Wh-v1HvuIh9GxxruPoEle-LZbpbA3AueWTdcVcTrZK7_c-4KcjHGOAQ-TCd_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی روز دوشنبه اعلام کرد تفاهم‌نامه میان آمریکا و جمهوری اسلامی به امضای دونالد ترامپ، رییس‌جمهوری آمریکا، جی‌دی ونس، معاون رییس‌جمهوری آمریکا، و محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، رسیده است.
او گفت در مرحله بعدی مذاکرات، آرایش فعلی نیروهای نظامی آمریکا حفظ خواهد شد، اما در صورت دستیابی به توافق نهایی، کاهش نیروهای نظامی در نظر گرفته شده است.
این مقام همچنین گفت مذاکرات فنی از اواخر این هفته آغاز می‌شود و جزییات توافق طی ۲۴ تا ۴۸ ساعت آینده منتشر خواهد شد.
او افزود آزادسازی دارایی‌های مسدودشده و کاهش تحریم‌ها به اجرای تعهدات وابسته است.
این مقام ارشد آمریکایی همچنین گفت: «از عملکرد عمانی‌ها در مذاکرات پیش از جنگ رضایت نداشتیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76384" target="_blank">📅 19:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76383">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e48597c90a.mp4?token=B65xVLk3GFivh9-_u1P27lbQ_tbKlamGIxU2tz59G3a9-SB33MteD99-Hmi3xlZT9-rPOJSypEgY0cxgJkR1hGIPXKBE8nl9iz6U-UhH4jh95Hj6dZGfn5KNA9iqPmbbMa3vTw5ULBZhee8w03ZKa9hpaqSd1MQLzERDfOe-5UnRWFTlG119Qi5ddDl3np5WiAmKLiNVIVk_tDcW6n9kLY5iu6qPqCNR5BXxvP3kTuE__RAuTMuVtxWwxTo8dA8Se1KUSvIMLsWth39nMWhYJ9bMMEIga7pR-iv6i1zJJEvwgUcnKxZ04Qdr1nKYG5u6MVW_UT-bmSpMUWl06QHqgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e48597c90a.mp4?token=B65xVLk3GFivh9-_u1P27lbQ_tbKlamGIxU2tz59G3a9-SB33MteD99-Hmi3xlZT9-rPOJSypEgY0cxgJkR1hGIPXKBE8nl9iz6U-UhH4jh95Hj6dZGfn5KNA9iqPmbbMa3vTw5ULBZhee8w03ZKa9hpaqSd1MQLzERDfOe-5UnRWFTlG119Qi5ddDl3np5WiAmKLiNVIVk_tDcW6n9kLY5iu6qPqCNR5BXxvP3kTuE__RAuTMuVtxWwxTo8dA8Se1KUSvIMLsWth39nMWhYJ9bMMEIga7pR-iv6i1zJJEvwgUcnKxZ04Qdr1nKYG5u6MVW_UT-bmSpMUWl06QHqgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس‌جمهوری ایالات متحده دوشنبه اعلام کرد که توافق با ایران امضا شده و متن توافق حاصل شده با ایران پس از مراسم امضای رسمی در جمعه منتشر خواهد شد.
دونالد ترامپ که در هنگام ورود به اویان در فرانسه، برای شرکت در نشست گروه هفت صحبت می‌کرد، همچنین گفت تنگه هرمز تا جمعه به‌طور کامل باز خواهد شد.
ترامپ در کنار امانوئل مکرون، رییس‌جمهور فرانسه، گفت مشخص نیست آیا در مراسم روز جمعه که قرار است در ژنو برگزار شود شرکت خواهد کرد یا نه، اما معاون رییس‌جمهور آمریکا، جی‌دی ونس، در آن حضور خواهد داشت.
او گفت: «توافق کاملا امضا شده است. و همان‌طور که می‌دانید تنگه اکنون تا حدی باز شده است. روز جمعه کاملا باز خواهد شد.»
ونس پیش‌تر گفته بود این توافق یکشنبه به‌صورت دیجیتالی امضا شده و هیچ‌گونه بودجه‌ای آزاد نشده است.
در پاسخ به این سؤال که متن یادداشت تفاهم چه زمانی منتشر خواهد شد، ترامپ گفت: «احتمالا خیلی زود. بعد از جمعه... فکر می‌کنم در آینده بسیار نزدیک.»
ترامپ همچنین گفت هرگونه کاهش تحریم‌ها علیه تهران «به رفتار ایران بستگی دارد. اگر آن‌ها کاری را که باید انجام دهند انجام دهند، این روند آغاز خواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/76383" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76382">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/06a4a159c2.mp4?token=pQmKid_ST5N3jspilQd2Oq9xfXWRa0xFK1XHVKy0q3rpHgHqzEQkR_jQfR_kdeO_LAqUo_G6YPuugEstBgBoY9GFrzgmDdh8tRN1wrB-HqRVWGHspQGk1_yXBIG76fyQ4i9O8MSqXM7LDOouqKxS4PTQsj4JmKGqELqBlREhmimNKls4mJ8LjalWpJBVlHf4l7AKjlkCeASHB8E9BcvWzlkIXPjOYmSVlv2CAv1cRqvKeDfD_s0JGPCh_y_nYxZ8GwapFZ3ELubBYKeDWhtQJyiD1dfKmFtGVhKkSO_ql5VbhjOOi34InlpCPxigwvf02BlAUF3KbRnaoQWQquIrNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/06a4a159c2.mp4?token=pQmKid_ST5N3jspilQd2Oq9xfXWRa0xFK1XHVKy0q3rpHgHqzEQkR_jQfR_kdeO_LAqUo_G6YPuugEstBgBoY9GFrzgmDdh8tRN1wrB-HqRVWGHspQGk1_yXBIG76fyQ4i9O8MSqXM7LDOouqKxS4PTQsj4JmKGqELqBlREhmimNKls4mJ8LjalWpJBVlHf4l7AKjlkCeASHB8E9BcvWzlkIXPjOYmSVlv2CAv1cRqvKeDfD_s0JGPCh_y_nYxZ8GwapFZ3ELubBYKeDWhtQJyiD1dfKmFtGVhKkSO_ql5VbhjOOi34InlpCPxigwvf02BlAUF3KbRnaoQWQquIrNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت فارسی وزارت خارجه آمریکا با انتشار ویدیوی بالا نوشت:
جی. دی. ونس، معاون رئیس‌جمهور ایالات متحده: توافق با ایران، «مبتنی بر عملکرد» است.
«باید به خاطر داشته باشیم که اقتصاد آنها اساساً نابود شده است. برنامه هسته‌ای آنها اساساً نابود شده است. اگر آنها [در چارچوب این توافق] اقدامات درست را انجام ندهند، از همان ابتدا هرگز پولی در اختیار نخواهند داشت که بتوانند برنامه هسته‌ای خود را بازسازی کنند.
USABehFarsi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/76382" target="_blank">📅 19:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76379">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SJGJDUZXm7HbukYM5nuwFnZ2JNsLw7N6FzMBkyTR6IYPOJ_nLfMshWKzAZmcbu3w4vIJ8LgLN0e3nZMa_q26vRhwFdmU7pr_kaScppQ_-1xTPnZ4gZ-PwbDGb4qYJiiNSRn36vjpwOGxsv_tnyoKiC1FQABAqb74YJVaWuuY8OyK7lU5Aj7tgb9NixNa6kzIb-FlEuDRF1dTezmeprx9rFUlOcs6H9qM3wVxNPU4PCbxmw0I3c1r1RH9c-_jLGnVchHOtuJt7WOO9jTMUNTVPw8Bj3gpy2sOfK22H6TI4zmZ2W7XCEIWPK54lB4Axgz2ZePdZzJsivmAsIJX8Miy6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SR-8rJhhbKrK492Jq84S0muMleWwGsM7HcFob6KdBC5l_MBoJzOykPNzjH3s72UkD9glbX-DlcvIDlttjUGe9VCdyfaIOUPmx4u5EK3VHv6qpO8ac1smistJxHi6ufsEhysR9gwoe_yZCzilQU4RCdKF4AUHjNOJUlSGRj9c1RHAE3Wt5MafhcjZ-M6Z93dNx8arGPo3Tp-HnpzDtyTKVfPngXAPL_ZGpTaOvVl0pJSqBF6kqvW3BStZ5LCsFn-ADvWJ9YGzVqyRA5mpJMzA8iN0iNn0ahx2p0BGrfKWVtlAcSO-QRVo551TfiJcyZ00-80cU3Qh6E0ZYXkVL3vM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eTSc7mqeIU7ejTa3FrP5SbOOE0XVyvg3yR0aBoG9SzIAydJ7SEdokWXBEVukUpaIKbKiUd8mTLKT5FkmV8U0vn0bcU5D7U74MICVi9UYztTxmKdPWexnfXe0o12RrWwdjY6Ss8DJMXMK8HZ0Y9cUCzZGVtRjtrFXDebEOgi3fogomwHyo2MIxcXN1NKg5XDJQC8sdI3jVD6LBrbPDDNbbF88g-peKmN-uD8JMAevzq9MyccGy3Oyfluhz9UbGlzz7EpqhVJF9ZOtVY6vCxNeQLC13heNOj5N7kg8OGoQuEzs0rOPNybYQNRFbArzUp_PjdyKRzF2WqCMn4eDiTenww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع حکومتی با انتشار تصاویر بالا نوشتند:
کلاهک ۵۰۰ کیلویی موشک تاماهاوک سقوط کرده در اطراف ورامین خنثی شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76379" target="_blank">📅 19:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76378">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6yUNKnhYGEk_Uhot7p1eP-Ms7ZulXexEQLFev77Z6dZmJoczVvZMDp3r94kyJHlFydS_gvft0m7aQyuOdW2CSBN0hSAlMxeIOgKLio_M44z3KHBUReTBZ5VhLoD8jFRAjYoqSDpiT0E2bog2FOfOilWMzqt0Ang-kR9IruJ4SNfQBj7v-tAyEKdvG-cewI1ldM25tpd9_gd8czNrQsBEHjEhqLDhGdVnHtQho61IN_PIP0aAnSMiPFeST-SJkdqwtAP74TgZkQVfSLxqvMD8rnljlfOY123bUJpIUsWXzxdj5x045P3mEhZ8rZeaQNXNSnsGWm21GtxlTHR6G2nmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس اطلاعات تهران، روز دوشنبه ۲۵ خرداد ۱۴۰۵ از بازداشت سه شهروند به اتهام انتشار مطالبی در شبکه‌های اجتماعی خبر داد.
خبرگزاری مهر به نقل از پلیس اطلاعات تهران بزرگ گزارش داد که این افراد در پی رصد فعالیت‌های فضای مجازی شناسایی و بازداشت شده‌اند. به گفته پلیس، بازداشت‌شدگان متهم هستند با انتشار مطالبی در شبکه‌های اجتماعی به مقدسات و آنچه «مدافعان وطن» خوانده شده، توهین کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/76378" target="_blank">📅 19:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76374">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fa0OMc3rRSIBOafYM7e_RnctrDhUgVbvLG7co0XDRV1DD9jw-1nNjS05NLlaF7aADCZrrsINkjLw5tdSqABuZMXfYxUAn5kjjVHpMCx2N10Yr2R7h-ZYMNMWbsjcgEvelQyK63BPckJVxuJ4gPJfuiVM9hK0EC57ARhhuz9Y0QJ9Jl0YgzyySa_BZblYmnVjJL2NsvCaaGR9bdyYE0VfneqLUOwVdYQ-XgYhP03W0jF7zsClGdGZtg_8uYgjwJW3rRMLogdXDs-sM9oha6cBZTDYunFyHKiPKenFON8zrkHHWZExW8sQZfa92R-JK_sTVIPMxo_rmZdsZViVrVB0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Az_JdX8FaZPchz9K2aRKm-FMjzEsoYjBiV7M3V6Hx78EdEo6cl_xSa8hmPZBVO57uQkRBVk4C1S3JBYdzPwT7ldUlb0YSUn3Y1nrzbUasT-YKKRKSGAZKskHOy7pOfmSpYhhcjGE4me0CgA3uS3jehWOWTZdVRf2MA5-l1MrgjsNYpNMXtDIDWvZ8veLk3oTdtwhRIFV_XXvbeFYoezprHueMipU3SjRRsJRXPZsb4MbSeN34YNWD0HyULgJF4k1P-YXFaawcmE1y-AdbNoe41JVEjD2WUkTwXbccImzZWeITqfrZ2Z5zRO1LGSHj85n4LO_BUJmwKpIaCYVNxD0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dzyd4YUB0GjfMobo3zJ_H8AHp7-s6FIvdJpTkcwmiZwaZW22MJWAIlVImwdE8mdYyfUVNmvpFPn3tdCCsuvveTnNpE6IpW4z8W8CDE0caL9GGVvkRSQEett1VgNkx_ytbeyLS-dkhBqtIhjsMt6hu-ktE2Akih0Qx9TninTpRZ-O2guKpf6o8vyQJJNkUj-y8t-jIwSL7R7vV6ovsQGhGqGejbzLy8HUfYLZxsu_PgyYLWnPalhhLs9eiIgcvuj3I6DIx5XNOk0sjtrJn8aL5x0qQ-ew1baN56huIddPrEaAsjsbI7AahH-VEWb_Tb6VmSEF_fxF1_3SszIHzmx3gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/65becd728e.mp4?token=Zj3-n3iRMZ_-gKvNuMJb5O_tUWn7zgLkZf1tYRKsSdeAiiypeJbxOwmnEaVhrE5za3k713Cz-pOyq5c6B961IHiZMtEx-TB2OiE4qd65GLm5ZpElUtxOjGmYNq4cNaHPiSf0X65vKUQEEOZPxa4Nqrp8lNWiHGXupB3R_glCoLfQOkooug_WjhILTIvqshgfJEwRfW_kqBGJxrIhpyw4Cb-i87XyHohj1QFS-Fbz_VqmXYMnBQidbi_mEu8e8BKTF8bOkztHssNs-MzOjAkwhPbkoumNtQhHeKoey2bCGV-dJr7wnMQ3Ncu7uwgtXu8ugzVRVlAbkdHtawTkKEL31A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/65becd728e.mp4?token=Zj3-n3iRMZ_-gKvNuMJb5O_tUWn7zgLkZf1tYRKsSdeAiiypeJbxOwmnEaVhrE5za3k713Cz-pOyq5c6B961IHiZMtEx-TB2OiE4qd65GLm5ZpElUtxOjGmYNq4cNaHPiSf0X65vKUQEEOZPxa4Nqrp8lNWiHGXupB3R_glCoLfQOkooug_WjhILTIvqshgfJEwRfW_kqBGJxrIhpyw4Cb-i87XyHohj1QFS-Fbz_VqmXYMnBQidbi_mEu8e8BKTF8bOkztHssNs-MzOjAkwhPbkoumNtQhHeKoey2bCGV-dJr7wnMQ3Ncu7uwgtXu8ugzVRVlAbkdHtawTkKEL31A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از دود یک آتش‌سوزی 'در میدان تجریش
#تهران
دوشنبه ۲۵ خرداد، الان'
Vahid
آپدیت در پست‌های پایین‌تر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/76374" target="_blank">📅 18:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76373">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOBQDT46DZ3jeQvgZq8LD-YVpVpjmu63XCF5yo5IMA1kjjR6UfNqMDRzdO-kimuZTO6P55BnFMHV_kKVtqjabsaSftWlCKJsTNRCzntnKwf9ftDJo1P18HMGEMbb4OJIvJkliQMr0-9z1afkDgIL1MMVD9mvlwyb1bSsJHL5nhkLv7vMFZony4LhcEKgI8lcHtx9tKOTgMZpgLhAJ8E5NCqyBmH0Mju1nlqRNPFQhpuXagpTcq2a83J1aOL72B0BK6riRkASEQxsyRL3NJ-v7vz7GlMC5dov4mrdgUyFBMu4nS4LYOrIoubcOwhfdJdli49dcA_bxDFRHjnKQa5uQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع امنیتی لبنان و رسانه‌های دولتی این کشور گزارش داد یک حمله پهپادی اسرائیل خودرویی را در جنوب لبنان هدف قرار داد و راننده آن کشته شد.
این نخستین حمله مرگبار گزارش‌شده اسرائیل در لبنان از زمان اعلام توافق میان آمریکا و جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/76373" target="_blank">📅 18:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76372">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afFCY8TFoP_8C6hZ5dmdhwgsOcVJEOPqiDJCG1NT4RzOpjq5Hbst-N6QihI6sHvSyL7J8LXqqhjodNPRZeLIGaH475p4GEGrPRP71BaPOv8-Dz5bTH0MbJdBaQWoyHe8rWWWKi7Llf6TgDO3f_9hcllq5Pq5yf6NGkydkVFPQIGKmywWEVXlcTwnhgeRjbcAS3t4HppfrtwgDt7vWYQ0DZZ4eFvXEw9V0pymWeNOBRMN_pTbKe9SbFv_V5FPoBzYXYq5oie6HE05LVAkzAfuInzZHmXGUOwUpULqmoZHFVXONU-DThpN-6Vme5_vZnpmpwDOER6q6l9981rrpUdT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز دوشنبه ۲۵ خردادماه اعلام کرد آمریکا و ایران پیش از مراسم رسمی امضای توافق، روز یکشنبه (به وقت آمریکا) آن را به‌صورت دیجیتال امضاء کرده‌اند.
ونس در گفتگو با شبکه ای‌بی‌سی گفت توافق روز یکشنبه «به‌صورت دیجیتال» امضاء شده و قرار است مراسم رسمی امضای آن روز جمعه در ژنو برگزار شود.
در همین حال، مسعود پزشکیان، رئیس جمهوری ایران نیز، روز یکشنبه در مراسمی دولتی با اعلام همین خبر گفته بود، توافق روز جمعه و حضوری امضاء می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/76372" target="_blank">📅 18:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76371">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oanGifGf0JXYtRKKo7OXCQDNuNt5Lb7sPT1xDuOwayrONG2CNagFZZLFJ6fXKFfSeynft4ddb5Gji1wnsIfQzBDyAbdEnTN4bryK3wlgudj1EMi0vdcoIqrCWksTjZ8asVtfqq4jLQzUeL93E-auvJIgd_VLnxeFQYSYlBgT6qBRe8ZYTNlVsyb87LNLz6lVGfg4lUs07DUOMIZ2BiMY1_Bic2JbOJ1ISbhE69o__GpyDZP-5CCqQIC4c2Gg0u0gQ1ceEDLLH2D8wxsh1bE4RH0fwFdPaZUlgx7TRXM6jpVetntt0KvztlpG0UOKAbRoJvd-iDlw9e6lO-P3GV2Gfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با وجود اعلام مقام‌های بانکی درباره رفع اختلال در خدمات بانک‌های ملی، تجارت، صادرات و توسعه صادرات، خبرگزاری فارس وابسته به سپاه اعلام کرد که بخشی از خدمات غیرحضوری و اینترنتی این بانک‌ها همچنان با اختلال مواجه است.
پیش‌تر این بانک‌ها در اطلاعیه‌های جداگانه اعلام کرده بودند که تمامی خدمات کارتی و سامانه‌های اینترنتی و موبایل‌بانک به حالت عادی بازگشته است.
فارس گزارش داد در حال حاضر خدمات مبتنی بر کارت در پایانه‌های فروشگاهی و دستگاه‌های خودپرداز این بانک‌ها فعال می باشد، اما بخشی از خدمات اینترنتی و غیرحضوری همچنان دچار اختلال است.
شورای هماهنگی بانک‌ها، وابسته به ساختار بانکی جمهوری اسلامی، روز شنبه ۲۴ خرداد حمله سایبری به سامانه‌های چهار بانک ملی، تجارت، صادرات و توسعه صادرات را تأیید کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/76371" target="_blank">📅 18:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76370">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdawQ7JOYmrzwUjySCB2GID-ICZMP9RUgC64RKANKZ_sxkGMt1mrflroeBcACTp_KxjfCi4C6r_1_m9k5ews6n8m70iURQIw-ozM1exQPKI9QQJFaxXcGoh1J9b35oUw-bLiKhvJfWWQbbkEIA6kUaS71e1icE1NQa2yNRZLYtHNDv5yJ7RVRcRIWAvqj31wh2FuSanDAmdaMi7Pp5EMSbcA6Xv6J0VNUNluBnREmIiKRN-k58BSKweSoyIXp8OTFQQCGFznNyD7sttE5QLGX1hue_wIjgEJ2uMwioI1UxnBglWc7A2FdQ5TozigHSp_RkOdqg-hJDsWFepdAuy--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه، به دنبال اعلام توافق ایران و آمریکا بر سر امضای تفاهم‌نامۀ پایان جنگ، قیمت ارزهای خارجی و سکه طلا در بازار آزاد ایران کاهش قابل توجهی یافت.
وب‌سایت‌های اعلام نرخ آزاد ارز و طلا، بعدازظهر روز دوشنبه قیمت هر دلار آمریکا را کمتر از ۱۶۲ هزار تومان اعلام کردند که نشان‌دهنده کاهشی در حدود ده هزار تومان از زمان اعلام توافق موقت است.
قیمت هر دلار آمریکا در روزهای گذشته بیش از ۱۷۱ هزار تومان گزارش می‌شد.
قیمت سایر ارزهای خارجی هم در بازار آزاد ایران کاهش مشابهی داشت.
همزمان قیمت هر سکه طلا در حدود ۱۶۷ میلیون تومان اعلام شد که نسبت به روز قبل کاهشی پنج میلیون تومانی را نشان می‌داد. این میزان کاهش در حالی رخ داد که قیمت طلا در بازارهای جهانی پس از اعلام توافق ایران و آمریکا افزایش یافته بود.
قیمت دلار و طلا در بازار ایران از زمان وقوع جنگ در ایران افزایش یافته و در روزهایی هر دلار آمریکا تا مرز ۱۹۰ هزار تومان هم معامله شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/76370" target="_blank">📅 18:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76369">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Evfx38TiQ31WCxvv8eBQJLBD2nQvD-E6QOdhBZHsUV-bGNBsejg-_y9r5Yah31D-fAqKnfbC5gS99mDbyZUgC5IDPEQfDqtcfGfLjShRLVbpuuwamtPi_5QOm0A9YKqoe0Nr9dPyWB7O2Ln_eV2UsljHT5w_8mqWaN8zATyGcbz_0y9TF2_6oWJXte51aEdoZyzradmPFL4L-UvzsrhXEI94rnrBCZOcXr3FDvUQNvSuIgWXNXpkr5f4x1MwTeYPdTrrGb_543D0ONwVF5g_ySrR4wXq8ths1lVHOY0bqwk5qJncOXb1bmp_mCupqRB7uA5qo5kK5-B-ONtZywLCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه ۲۵ خردادماه در پیامی در شبکه اجتماعی تروث سوشال اعلام کرد کشتی‌ها، از جمله نفتکش‌های حامل نفت، حرکت از تنگه هرمز را آغاز کرده‌اند.
ترامپ نوشت: «کشتی‌ها در حال حرکت هستند؛ بسیاری از آن‌ها با نفت بارگیری شده‌اند و از تنگه هرمز خارج می‌شوند. آن‌ها از مسیر جنوبی حرکت می‌کنند؛ مسیری که کاملا امن، مطمئن و پاک است.»
رئیس‌جمهور آمریکا همچنین افزود: «مسیرهای دیگری نیز برای تردد وجود دارد.»
پیام ترامپ در حالی منتشر می‌شود که صدا و سیمای جمهوری اسلامی ایران، روز دوشنبه در گزارشی تصویری اعلام کرده بود: «بیش از ۹۶ ساعت است که نیروی دریایی سپاه هیچ مجوز عبوری صادر نکرده است.»
پیشتر رویترز گزارش داده بود، نخستین نفتکش حامل گاز طبیعی مایع پس از اعلام پایان جنگ جمهوری اسلامی ایران و آمریکا، صبح دوشنبه از تنگه هرمز عبور کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/76369" target="_blank">📅 18:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76368">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoim7zSu013YFdCTLD-XydoAPn0_7ryt8ihhQ4ZXMeDisI_OS-MN4VCtYdpzKBQaU8FY9PgNx-RSZasEIGvROeTMnmp7FoTxZL27LaoEZS7Jnlk1k6TCWUaCloTHllo-roNFEWkCwYSgbcqrpuKHYMCoiY1NCZm5XzofjW6gOx74WekMbv8NPYmF_BotgbcnuQVOqU9bYrVibNydQYkUqbQlMpV89P-uCe-88-ltc7YJWT_S5t5CfFLKVCjYuI_cHFBkJM5r-4l6dupEnTfdaJ69WGsz_D_KAuwPqb4Y7f54uIAWGjtU_whxtuL1f2KOXqTc6EhR78ribWc76Vpl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا می‌گوید تفاهم‌نامه ایران و آمریکا روز جمعه در حضور عباس عراقچی و محمد‌باقر قالیباف در سوئیس امضا خواهد شد.
جی‌دی ونس گفت که «جزئیات زیادی از توافق هنوز حل‌و‌فصل نشده است» اما آمریکا انتظار دارد که تنگه هرمز «در درازمدت بدون عوارض باز باشد.»
سخنگوی وزارت خارجه جمهوری اسلامی اما گفته است که هنوز مشخص نیست که چه کسی از جانب ایران تفاهمنامه را امضا می‌کند.
اسماعیل بقایی همچنین تاکید کرد که ایران «به‌دنبال گرفتن عوارض نیست» اما «هزینه ارائه خدمات» را دریافت خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/76368" target="_blank">📅 18:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76367">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQdU1ddz_LxbkF7WzWIy6IfvwyubuIDgAQt5_jKOAzzuSuK6JOVe1w_OfdI9H7yL-MCI-wT-yTxRS1c81JDznPDowtkneDTGGWaHT8YpY7qOpkB_6zKkKlaNRkGvK2le31ixG4kWxzuZ2HliRzv0Pwd3P7RSQtTUg1VmqW38VLu1ufqt81hHu33kRNnMzhrOIm2RAHXlWkbwSASKbbcjJxllw1cLsZf0zr07Mt89BWHuKrkWDdYPEu-3dTj0B9fbAb8mukurpxsYJnrYgbEBAhf2lNBTgi9VepOwhZe1ziHi0-GNtv5wbuo0fCp5YEyljX5pYwjTGZAghi9K_YuBYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نوید عالم‌چهره» ۴۴ ساله، ساکن ملک‌شهر اصفهان و پدر دو دختر، روز جمعه ۱۹ دی‌ماه ۱۴۰۴ هدف شلیک گلوله جنگی قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله جنگی از پشت به پهلوی او اصابت کرده بود.
خانواده می‌گویند نوید عالم‌چهره هنگام مجروح شدن هنوز هوشیار بود و توسط اعضای خانواده به بیمارستان غرضی اصفهان منتقل شد.
به گفته آنان، کادر درمان پس از تحویل گرفتن او اعلام کردند که برای عمل جراحی به اتاق عمل منتقل خواهد شد.
نزدیکان نوید می‌گویند تا صبح مقابل بیمارستان منتظر ماندند، اما با باز شدن درهای بیمارستان و مراجعه برای پیگیری وضعیت او، دیگر اثری از نوید پیدا نکردند. به گفته نزدیکان، پس از دو روز جست‌وجو و مراجعه به مراکز مختلف، سرانجام پیکر او را در سردخانه باغ رضوان اصفهان پیدا کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/76367" target="_blank">📅 18:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76366">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p00VBNMhzRHCzCYDgTwjsQHNcx6zz341Lyz28MF1VTXX6d81-dbxxeMRPAzkA8o-XYm0F51NgTOt8vA0b440pyeDJZu-b2qKiaFlUnmqIhwB-2d3IsWem2TT81ibJ4TKQtbnKJgvORRC2UNVEUvibUgFwcUUK4C7iE0xCXUpJ_UvPTaavfBAmdYCfP2couaRVDtXgtmwrCCRY40f2vSSa0l2vUDc4rOx88SvXtBQJoJ0eJUXQzaxxbRvHTA_UPJoZ5NZqbDVK4IlgNKziKSKX7ssoTZifqixzubFvrtYDJw-cY_d2heirVPTBlPq8CqpgtoksQxM6U7lPCh98_kMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل اعلام کرد که از آغاز سال جاری میلادی تاکنون، دست‌کم ۴۰ نفر در ایران به اتهام‌های مرتبط با «امنیت ملی» اعدام شده‌اند که در میان آن‌ها ۱۸ معترض نیز دیده می‌شود.
ولکر تورک روز دوشنبه ۲۵ خرداد افزود: «مقامات دست به سرکوب شدید زده‌اند، هزاران نفر را بازداشت کرده و محدودیت‌های بیشتری بر فضای مدنی اعمال کرده‌اند».
او در بخش دیگری از اظهاراتش از اعلام توافق صلح میان ایالات متحده و ایران استقبال کرد و از همه طرف‌ها در منطقه خواست حداکثر خویشتنداری را رعایت کنند.
تورک گفت: «از اعلام این‌که ایالات متحده و ایران بر سر یک توافق صلح به تفاهم رسیده‌اند که شامل آتش‌بسی فوری و دائمی، بازگشایی تنگه هرمز و چارچوبی برای ادامه مذاکرات است، استقبال می‌کنم».
او افزود: «در این مقطع حساس، روشن است که همه طرف‌ها باید حداکثر خویشتنداری را به خرج دهند و برای اجرای سریع و با حسن نیت توافق حاصل‌شده تلاش کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76366" target="_blank">📅 18:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76362">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/beda093be0.mp4?token=Ray1-c18RnaJK2WKKFMD167RIg99LX86UAuX3GGG1SBOEn6DYU1_KukKUdS3Unv3HFPRCSkC_RI64wvTqiOWi7czGvzEW-oDNWKsh9fvUVnynnXpVjWYqeX3nQEoTeK_yeuFUpOxcexKR0iY8otVjo7pEd7OtB_Hv71yYvNj7_KR4Fcj8T6K1NUCUzRpFG74aw63dGZ3s2loTtCJX5wl4tJzLp6HXENY9WIEpZPh6r4DzP50vV3KTA5mvzrYNEgvtROJhwP9UFZy0j6t9G_X28D-QBqxoTn6wRBOCqaEeoHPos-gCw6cAmziitf1PBP2V5TtSZAuiNngCC5tXE7sig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/beda093be0.mp4?token=Ray1-c18RnaJK2WKKFMD167RIg99LX86UAuX3GGG1SBOEn6DYU1_KukKUdS3Unv3HFPRCSkC_RI64wvTqiOWi7czGvzEW-oDNWKsh9fvUVnynnXpVjWYqeX3nQEoTeK_yeuFUpOxcexKR0iY8otVjo7pEd7OtB_Hv71yYvNj7_KR4Fcj8T6K1NUCUzRpFG74aw63dGZ3s2loTtCJX5wl4tJzLp6HXENY9WIEpZPh6r4DzP50vV3KTA5mvzrYNEgvtROJhwP9UFZy0j6t9G_X28D-QBqxoTn6wRBOCqaEeoHPos-gCw6cAmziitf1PBP2V5TtSZAuiNngCC5tXE7sig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهروز رضوی، گوینده محبوب علی خامنه‌ای، درگذشت.
FattahiFarzad
بهروز رضوی، گوینده، صداپیشه، ترانه‌سرا و بازیگر، پس از دوره‌ای بیماری در ۷۸ سالگی درگذشت.
او فعالیت حرفه‌ای را از سال ۱۳۴۷ با گویندگی در رادیو آغاز کرد و طی بیش از پنج دهه فعالیت، به یکی از شناخته‌شده‌ترین صداهای رسانه‌ای ایران بدل شد. روایت مجموعه مستند «ایران» از جمله ماندگارترین آثار او به شمار می‌رود.
بهروز رضوی علاوه بر فعالیت در رادیو و تلویزیون، در سینما و دوبله نیز حضور داشت و در آثاری چون «گناه فرشته»، «سفر به چزابه» و «نجات‌یافتگان» ایفای نقش کرده بود.
او همچنین شاعر ترانه‌های «کویر دل» و «گمشده» با صدای مرجان بود.
این هنرمند متولد یزد از سال ۱۳۷۴ در کرج زندگی می‌کرد و برادر عاطفه رضوی، بازیگر و چهره‌پرداز، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76362" target="_blank">📅 18:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76361">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHfhlxpsU5YQ8Jwr-_SgtjPE8dz6QCs9PtBcxY9WbIkx66r3BueqBG3eZv5cob_uSzVic-2aShMrSoHkXbFy_KE7b7vJxEhHasNP9tf2QoL_9pp3n0H7CMfcqK48yPVH-hYDF0TgczrfT3W6dU_QUJXcTSTDq24SoU25Hw52wccjF-sWlDYRLL8pvmmvW-ipaFQ70bMU5rU7PZ8CESpUq4EyvG26CIJf16kgZ9Az7t8GcTSIURjuUc-CQud8R5mSIW5sKTBqU2LYqqY0LSAuCxbmCCmSNwzG6c7Gn0oNpwRjryNecVL49ZUSvkaFToplnbeUW1hHFiArODuMOldPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گفته دو مقام جمهوری اسلامی که نیویورک‌تایمز نام آنها را اعلام نکرده، تهران تا پس از عبور ساعت از نیمه‌شب به وقت محلی صبر کرد تا توافق را نهایی کند، زیرا نمی‌خواست این رویداد مهم با روز تولد دونالد ترامپ، رئیس‌جمهوری آمریکا، در روز یکشنبه هم‌زمان شود.
بر اساس این گزارش، اختلاف زمانی هفت‌ونیم ساعته میان تهران و واشینگتن باعث شد هر دو طرف بتوانند روایت مورد نظر خود را از زمان نهایی شدن توافق ارائه دهند. ترامپ گفته بود توافق در روز یکشنبه نهایی شده، در حالی که ایران اعلام کرده بود این روند در روزی بعد از آن تکمیل شده است. دونالد ترامپ ۱۴ ژوئن ۱۹۴۶ به دنیا آمده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/76361" target="_blank">📅 03:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76360">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مصاحبه ترامپ با نیویورک‌تایمز، ترجمه ماشین:
رئیس‌جمهور ترامپ بعدازظهر یکشنبه در مصاحبه‌ای گفت توافقی که با ایران به دست آورده، در نهایت تضمین خواهد کرد که تنگه هرمز  «برای همیشه بدون عوارض» باشد و استدلال کرد که با وجود مخالفت‌های بنیامین نتانیاهو، نخست‌وزیر اسرائیل، او اسرائیل را از نابودی هسته‌ای نجات داده است.
آقای ترامپ همچنین اصرار کرد که اگر ایران نتواند به توافق نهایی هسته‌ای با ایالات متحده برسد ــ روندی که دستیارانش می‌گویند انتظار دارند روز جمعه در سوئیس آغاز شود ــ او حملات نظامی به تهران را از سر خواهد گرفت یا در ازای دریافت ۲۰ درصد از درآمدهای منطقه، ایالات متحده را به «نگهبان خاورمیانه» تبدیل خواهد کرد.
در یک گفت‌وگوی تلفنی ۲۸ دقیقه‌ای که آقای ترامپ از محل اقامتش در کاخ سفید آغاز کرد، و در یک تماس کوتاه بعدی، رئیس‌جمهور ادعا کرد که تصمیمش برای حمله به ایران در اواخر فوریه و محاصره دریایی بعدی بنادر این کشور پس از آنکه تهران تنگه را بست، خاورمیانه را به سود آمریکا دگرگون کرده است.
او که در روز تولد ۸۰ سالگی‌اش صحبت می‌کرد و صدای جمع شدن خانواده‌اش برای شام جشن تولد در پس‌زمینه شنیده می‌شد، از دو رهبر اقتدارگرا ــ شی جین‌پینگ، رئیس‌جمهور چین، و ولادیمیر وی. پوتین، رئیس‌جمهور روسیه ــ به‌خاطر کمک به این توافق تمجید کرد و
آقای نتانیاهو را به‌دلیل انجام حملاتی که نزدیک بود توافق نهایی را از مسیر خارج کند، به‌شدت مورد حمله قرار داد.
آقای ترامپ درباره نخست‌وزیر اسرائیل گفت: «او آدم بسیار دشواری است، و صادقانه بگویم باید بابت این کار از ما بسیار سپاسگزار باشد. چون اگر ایران سلاح هسته‌ای داشت، اسرائیل دو ساعت هم دوام نمی‌آورد.»
با اینکه متن توافق هنوز منتشر نشده است، به نظر می‌رسید آقای ترامپ در حال توصیف امتیازهایی از سوی ایران است که این کشور هنوز نداده، یا به مذاکرات بعدی موکول شده است. برای مثال، تفاهم‌نامه فقط عوارض عبور از تنگه را به مدت ۶۰ روز تعلیق می‌کند و سپس وعده گفت‌وگوی منطقه‌ای درباره آینده را می‌دهد.
ایران پیش از جنگ هرگز عوارضی دریافت نمی‌کرد، بنابراین آقای ترامپ در اصل در حال جشن گرفتن بازگشت به وضعیت پیش از جنگ است.
آقای ترامپ بارها تفاهم‌نامه جدید خود را با توافق سال ۲۰۱۵ میان باراک اوباما، رئیس‌جمهور وقت، و رهبری ایران مقایسه کرد و گفت توافق او تضمین خواهد کرد که ایران «نتواند سلاح هسته‌ای تولید یا خریداری کند». ایران زمانی که در سال ۱۹۷۰ پیمان منع گسترش سلاح‌های هسته‌ای را تصویب کرد، با این موضوع موافقت کرده بود و در صفحه نخست توافق دوران اوباما نیز دوباره بر آن تأکید کرد.
در سه ماه گذشته مذاکرات، که به رهبری استیو ویتکاف، فرستاده ویژه رئیس‌جمهور، و جرد کوشنر، داماد او، انجام شد، ایرانی‌ها اصرار داشتند که هرگز از حق خود برای غنی‌سازی اورانیوم تحت آن پیمان دست نخواهند کشید.
آقای ترامپ گفت هنوز بر سر این موضوع مذاکره می‌کنند که آیا ایران غنی‌سازی خود را برای ۲۰ سال تعلیق خواهد کرد یا نه ــ ترامپ تلویحاً گفت شاید به تعلیق ۱۵ ساله رضایت دهد ــ اما گفت ایران برای همیشه به غنی‌سازی در سطوح پایین محدود خواهد شد؛ سطوحی که «هرگز نمی‌تواند از سوی ارتش استفاده شود».
توافق دولت اوباما نیز همین شرط را داشت، اما پس از آنکه آقای ترامپ در سال ۲۰۱۸ آن توافق را کنار گذاشت، ایران غنی‌سازی در سطوح بسیار بالاتر را آغاز کرد؛ از جمله اورانیوم نزدیک به سطح مورد نیاز برای بمب، با غنای ۶۰ درصد.
در جریان این گفت‌وگو، رئیس‌جمهور حال‌وهوایی شادمانه داشت و درباره رویداد آتی «یو‌اف‌سی» که قرار است در محوطه جنوبی کاخ سفید برگزار شود و احتمال اینکه باران آن را مختل کند، صحبت کرد. او گفت: «در زمان جنگ چنین چیزهایی پیش می‌آید.»
nytimes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76360" target="_blank">📅 03:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76359">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/129bb5a743.mp4?token=BuvcOXm4GqWPF7_98jgskPhYduTKQdMabHJKsh2k5-TOirayuw9sOKuVD2V5lehi4m91AFEBmMmSLi2dbOQV37BqMPHCa9u2rTR1vucu2TGo7avU3U6EYqxxuSUvWADdF83JbPKLXb3H3RgZgknqUehewEatFpwbQIkqbL7ZCtxNt6ga-RG0F1krT4OldkcqOuU39hPJjzHBoCyqonE-iJ70HvxTb92Eof9ZctBaYBwh93UxARNGmt6KYfrMq0_rkadPqQ5fva-QQkcyQd0jZZIAmjalKxqaWytDk90gMkT0V3NAqtKtbsuAwE1IamGtTCi166hFLzaGYYF8yrzcaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/129bb5a743.mp4?token=BuvcOXm4GqWPF7_98jgskPhYduTKQdMabHJKsh2k5-TOirayuw9sOKuVD2V5lehi4m91AFEBmMmSLi2dbOQV37BqMPHCa9u2rTR1vucu2TGo7avU3U6EYqxxuSUvWADdF83JbPKLXb3H3RgZgknqUehewEatFpwbQIkqbL7ZCtxNt6ga-RG0F1krT4OldkcqOuU39hPJjzHBoCyqonE-iJ70HvxTb92Eof9ZctBaYBwh93UxARNGmt6KYfrMq0_rkadPqQ5fva-QQkcyQd0jZZIAmjalKxqaWytDk90gMkT0V3NAqtKtbsuAwE1IamGtTCi166hFLzaGYYF8yrzcaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف پیش از چنج‌رژیم: مذاکره با قاتل سلیمانی شرافتمندانه نیست
همزمان با انتشار خبر توافق میان واشنگتن و تهران، ویدیویی از اظهارات محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در روز شنبه ۲۰ بهمن‌ماه ۱۴۰۳ بار دیگر در شبکه‌های اجتماعی بازنشر شده است.
قالیباف در ششمین همایش ویژه فرماندهان و کارکنان ستاد فرماندهی سپاه، در پاسخ به پرسشی درباره تفاوت کامالا هریس و دونالد ترامپ گفته بود: «حتما فرق دارد، ترامپ قاتل شهید سلیمانی است. مگر ما می‌توانیم بی‌تفاوت باشیم؟ پس حتما برای ما فرق می‌کند.»
او همچنین با اشاره به مواضع علی خامنه‌ای درباره مذاکره با آمریکا گفته بود: حضرت آقا می‌فرمایند شرافتمندانه نیست، خب شرافتمندانه نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76359" target="_blank">📅 02:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76357">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vozTAzUl8cs6KeJONHI93svw9zeVUH6g12N8m2MDsBs3RYmiitSjq3tjrr2TE3jJrVgFssc1FAN84rjF_6nQSj0gwEs_S8rAMn1zqKEBHhA8v55pSXfLMIgYIX7RDINY2sHirNBy5q9V7l8ocFKS40o0zfw7Tghujv_wtyFlNGWiUb-MoqKp1kYQeSXCQ0yU8AMHiMPczMIUWhq12dnYomv9tRL-EMTl6pURYe6lqDfM1_AfnvXK7NYh9Me5qq6OnysJ_dQo2rJHPdKVmKh9-0coysl2n-j8LPSMoMY9N-mRJosY1gTEOKLYmw03o8P7GzggAGZAvpUH5b_Eqh9-ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TYvmA788HXnB3WNJRnD1L0JVQE6N8YqfMej46YDYvlPsuEvoA0Fatxg2mUx5Zg5DOcl-99gZZnzZiS0frES3E982ADSVlOZ7aztrGtKXG3hUat2Qz4MGNT3DFBS9uZMOH3S6E4EK1cH95G0kunBac_BvJkA0GGo1ubuIgugUWFWeNUuLCu3u0s9RcqjVICTemYGOTmXLTOYr8y93mArOG9J_za4po3Vs3JyVu63bOC-sDlGvvA7aYmHVsFbr5_C3t7vmLw9Riy_0sqbLOYnoESvCttCFaC04p1f0xdWZVPHzsRLC2enPIWbi9H0DOJIbE4yPJZnPqpS0MaVl23i7bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کی‌یر استارمر، نخست‌وزیر بریتانیا، اعلام کرد که از توافق اعلام‌شده میان آمریکا و حکومت ایران «به گرمی استقبال می‌کند» و آن را «گامی بسیار مهم رو به جلو برای پایان دادن به جنگ، تضمین ثبات منطقه و بازگشایی تنگه هرمز» توصیف کرد.
استارمر در بیانیه‌ای که روز یکشنبه در شبکه‌های اجتماعی منتشر کرد، افزود: «ما آماده‌ایم از گفت‌وگوهای فنی که اکنون آغاز خواهد شد حمایت کنیم. اولویت ما این است که این توافق به صلحی پایدار و ماندگار تبدیل شود و برای تحقق این هدف با شرکای بین‌المللی همکاری خواهیم کرد.»
او گفت حمایت بریتانیا می‌تواند، در صورت نیاز، شامل «راه‌اندازی ماموریت دفاعی، مستقل و چندجانبه‌ای باشد که بریتانیا و فرانسه تاکنون نقش پیشرو در برنامه‌ریزی آن داشته‌اند؛ به‌ویژه برای ارائه کمک در زمینه پاکسازی مین‌ها» در تنگه هرمز.
نخست‌وزیر بریتانیا همچنین تاکید کرد: «موضع قاطع و دیرینه بریتانیا همچنان این است که ایران هرگز نباید به سلاح هسته‌ای دست یابد.»
@
VahidOOnLine
امانوئل مکرون، رئیس‌جمهوری فرانسه، بامداد دوشنبه ۲۵ خردادماه در پیامی در شبکه اجتماعی اکس از توافق حاصل‌شده میان واشنگتن وتهران استقبال کرد و خواستار اجرای سریع و کامل آن از سوی همه طرف‌های درگیر شد.
مکرون گفت این توافق باید زمینه بازگشایی فوری و بدون قید و شرط تنگه هرمز را فراهم کند. او افزود ماموریت بین‌المللی ایجادشده با همکاری بریتانیا آماده پشتیبانی از این روند است و ازسرگیری تردد دریایی بدون محدودیت و عوارض، برای ثبات منطقه‌ای و اقتصاد جهانی ضروری است.
رئیس‌جمهوری فرانسه همچنین گفت این توافق می‌تواند راه را برای مذاکراتی گسترده‌تر درباره برنامه هسته‌ای و موشکی ایران و مسائل امنیتی خاورمیانه هموار کند. او تاکید کرد فرانسه آماده است در کنار شرکای خود برای دستیابی به صلحی پایدار در منطقه نقش‌آفرینی کند.
مکرون در بخش دیگری از پیام خود بر حمایت فرانسه از تلاش‌های دولت لبنان برای بازگرداندن حاکمیت کامل این کشور تاکید کرد و گفت برقراری آتش‌بسی پایدار برای تحقق این هدف ضروری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76357" target="_blank">📅 02:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76356">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X6xHKov3g_efolBuHX57pAJQUtsSy0ae0YTgLTiGn84MMV7tqFrdRC9Aa4l_Aj9P6o5_oUpFj70IlN3jZq-CTlJJSAggttpPNbOL4YuOj0AwwtkzSkc6BPGiDO7Kn2jg-aRx38nAAxygbD49RlsL3KyFNTe6xG3yhgiEWtcSTP6m2sPR49bCGROa26uyEsYuAmge_nXDGmmwy1mUsrdc0kZQfcLsrD38KUEVED3v4oe3iXQbxmuNENJYvE5d-WCnpLk0m_UzlYgCBMO_y-S0K1zxyfQNYBl9TGeWMwED05n50NhYsI3s03AsUOJQ6lPhS1-n9HR_ZdRPVg2by7aiVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه معاریو به نقل از منابع اسرائیلی گزارش داد بنیامین نتانیاهو، نخست‌وزیر این کشور، در گفت‌وگو با دونالد ترامپ، رییس‌جمهوری آمریکا، به صراحت اعلام کرد که اسرائیل خود را به بند مربوط به لبنان در توافق میان آمریکا و حکومت ایران متعهد نمی‌داند.
بر اساس این گزارش، نتانیاهو گفت که ارتش اسرائیل از لبنان عقب‌نشینی نخواهد کرد، در مواضع فعلی خود باقی خواهد ماند و به اقدامات خود برای خنثی کردن تهدیدهای حزب‌الله، از جمله نابودی زیرساخت‌های تروریستی و پاسخ به هرگونه حمله علیه اسرائیل، ادامه خواهد داد.
به نوشته معاریو، برداشت منابع اسرائیلی آن است که «توافق احتمالی ایالات متحده با ایران، دست اسرائیل را در عرصه لبنان نخواهد بست. پیام اصلی این است: اسرائیل منافع امنیتی-راهبردی مستقلی در لبنان دارد و قصد دارد بر آن پافشاری کند.»
این روزنامه نوشت: «اکنون باید دید این شفاف‌سازی‌ها — فراتر از تماس تلفنی نتانیاهو و ترامپ — در بوته واقعیت چگونه عمل خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76356" target="_blank">📅 02:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76355">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بیانیه دبیرخانه شورای عالی امنیت ملی:
متن یادداشت تفاهم پایان جنگ پس از چند ماه مذاکره فشرده نهایی شده است
جنگ در تمامی جبهه‌ها از جمله لبنان از امشب به صورت فوری و دائمی پایان می‌یابد
متنی که در خبرگزارهای حکومتی منتشر شده:
بیانیه دبیرخانه شورای عالی امنیت ملی درباره توافق پایان جنگ
میان ایران و آمریکا
بسم الله الرحمن الرحیم
به اطلاع ملت شریف ایران می رساند:
▪️
جمهوری اسلامی ایران در پرتو راهبری رهبر شهید خویش، تفوق خود در برابر دشمن امریکایی صهیونی را تکمیل کرده و ذیل تدابیر رهبری عالی قدر نظام (حفظه الله تعالی)، حمایت های آحاد مردم و تلاش مجاهدانه رزمندگان اسلام، به دنبال یک دوره مذاکرات دشوار و فشرده چند ماهه، و بر اساس مصوبه شورایعالی امنیت ملی، متن یادداشت تفاهم در خصوص مذاکرات پایان جنگ (مذاکرات اسلام آباد) را میان ایران و امریکا در شامگاه 24 خرداد ماه، نهایی کرد.
▪️
بر اساس توافقات انجام شده، جنگ و عملیات نظامی در تمامی جبهه ها از جمله لبنان از امشب به صورت فوری و دائمی پایان یافته و به علاوه، محاصره دریایی علیه ایران بلافاصله و به طور کامل خاتمه می‌یابد.
▪️
امضای این یادداشت تفاهم در روز جمعه 29 خرداد به طور رسمی انجام خواهد شد.
▪️
مذاکرات برای توافق نهایی، به پس از اجرای تعهدات طرف مقابل وفق یادداشت تفاهم موکول خواهد شد. جمهوری اسلامی ایران از تلاش های جمهوری اسلامی پاکستان و دولت قطر قدردانی می کند.
والسلام علیکم و رحمت الله و برکاته
دبیرخانه شورای عالی امنیت ملی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76355" target="_blank">📅 02:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76354">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a76f7084c.mp4?token=MauoY9FwIx5D1iLgRWf_UMP_EDDu1LZRSaElCJnpmJyeY3RzXWt9YIKEw7pE5uB_dVWAx1mdjH3eQDNaHG8Dyg13H5mdiw-37RFco5XuAgmAmTxNjBJ7wKpITl5SllZgnNm24OhPGd5DYExflRU4wT2L61izqE3k67CmQ3s5DhBS3isSssCBZox4gMRv7g6J5b1mIF9cznQER5gCwqMf7BuomVWVfZc-6I4Gk2VPLy_5uOLDp7VW7ioZbkLVCkVIfrz2y3pZugFfduaiBElx5nQWL-uTOg_uwNj7QIZ3LVZFm3e_DscAZ6N1c-MKtshSlpUUc_C65oiMCdYxDXP9wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a76f7084c.mp4?token=MauoY9FwIx5D1iLgRWf_UMP_EDDu1LZRSaElCJnpmJyeY3RzXWt9YIKEw7pE5uB_dVWAx1mdjH3eQDNaHG8Dyg13H5mdiw-37RFco5XuAgmAmTxNjBJ7wKpITl5SllZgnNm24OhPGd5DYExflRU4wT2L61izqE3k67CmQ3s5DhBS3isSssCBZox4gMRv7g6J5b1mIF9cznQER5gCwqMf7BuomVWVfZc-6I4Gk2VPLy_5uOLDp7VW7ioZbkLVCkVIfrz2y3pZugFfduaiBElx5nQWL-uTOg_uwNj7QIZ3LVZFm3e_DscAZ6N1c-MKtshSlpUUc_C65oiMCdYxDXP9wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری فارس:
‌غریب‌آبادی، معاون وزیر خارجه: در مذاکرات ۶۰ روزه در مورد چند موضوع بحث خواهیم کرد:
🔸
۱. خاتمه تمام تحریم‌ها و قطعنامه‌های شورای امنیت
🔸
۲. موضوعات هسته‌ای
🔸
۳. تعیین سازوکار نهایی بازسازی ایران
🔸
۴. تعیین سازوکار اجرایی برای نظارت بر تعهدات طرفین
خبرگزاری مهر:
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا
جزییات این پیش‌نویس به شرح ذیل است:
۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان
۲- تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی ایران.
۳- رفع کامل محاصره دریایی ظرف ۳۰ روز
۴- تعهد آمریکا به خروج نیروهایش از پیرامون ایران
۵- بازگشایی تنگه هرمز ظرف ۳۰ روز با ترتیبات ایرانی
۶- تعلیق تحریم های فروش نفت، محصولات پتروشیمی و مشتقات و دسترسی کامل ایران به منابع مالی آن.
۷- لزوم ارائه طرح های بازسازی ایران حداقل به مبلغ ۳۰۰ میلیارد دلار توسط آمریکا و متحدانش
۸- ۶۰ روز مذاکره برای رسیدن به توافق نهایی مبتنی بر موضوعات هسته ای و لغو کامل تحریم های اولیه، ثانویه، آمریکا و قطعنامه های شورای امنیت سازمان ملل و شورای حکام آژانس بین المللی انرژی اتمی
۹- تکرار تعهد ایران در پیمان ان پی تی مبنی بر عدم تولید سلاح هسته ای
۱۰- در دوره مذاکرات آمریکا متعهد شده به نیروهای خود در منطقه اضافه نمی کند و تحریم جدیدی هم وضع نخواهد کرد.
۱۱- آزادسازی ۲۴ میلیارد دلار پول های بلوکه شده ایران در دوره ۶۰ روزه مذاکرات نهایی. نیمی از این مبلغ قبل از شروع مذاکرات باید در دسترس ایران قرار گیرد.
۱۲- تشکیل سازوکار نظارتی برای اجرایی کردن توافق.
۱۳- توافق نامه نهایی توسط قطعنامه شورای امنیت سازمان ملل به تایید می رسد.
۱۴- مذاکره نهایی قبل از آزادسازی نیمی از پول های بلوکه شده ایران، تعلیق تحریم های نفتی ایران و رفع محاصره دریایی آغاز نمی شود و توافق نهایی صرفا در موضوع سرنوشت مواد غنی شده و غنی سازی، رفع تحریم ها، برنامه بازسازی اقتصاد ایران انجام می شود و بحث درباره برنامه موشکی ایران و حمایت از گروه های مقاومت به صورت قطعی از دستور کار خارج شده است/مهر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76354" target="_blank">📅 02:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76353">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eRerCYSjFrOnSuSqlLLmE3oy0j8mufaSp9wlIfLbsisbaLWKVCZb6LFp2eo_N0CbX-ZvlnoCUc660inUNEqXGFcpEa400A1S8a6HsStKKn8nM4L4MQ1zmM4T0ocUZ6AHNi85uuZEqZqLsPkj7cTJAune9Ow_9bAsL3GOB7sUl143JmRcSPOB9-ug19GTulIBGsbSKBgrzchrHd9xbreLsU3SGnibRpsUOBndbg4Sy9gnh-v-xCRBjbYAoHs2bj-KzdjlCybDS4lEGD87nutIXqnq3Y53As2qQmUkOt3jAHV2ZaBzxZnw_Osm5eF-KxR1_h1GVcyexAUHN75RuLIz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: تنگه هرمز جمعه پس از امضا باز می‌شود
روسای جمهور پیش از من در رسیدن به صلح با ایران شکست خورده بودند
پست ترامپ، ترجمه ماشین:
این توافق بزرگ، صلح و امنیت را برای کل منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردند با ایران صلح کنند، اما همه پیش از من شکست خوردند. رهبران منطقه، برای نخستین بار، رئیس‌جمهوری را یافته‌اند که می‌تواند به آن‌ها کمک کند به صلح واقعی دست پیدا کنند.
با باز شدن تنگه پس از امضای توافق در روز جمعه، برای مقاصد مربوط به پاک‌سازی مین‌ها، نفت دوباره از هر دو سوی آن برای منطقه و جهان جریان خواهد یافت!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/76353" target="_blank">📅 02:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76352">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da696e6ada.mp4?token=kXnDzHGWAyz55k9a1FmlGG1TCLD0ZOV5lY7Vyoo-AoSO3J_DrvbSY9wbS9QSf23rh_8PxdxkQBbB-d4Euy_mox1bghodDMv5yBPO_ImDb_f9w33R-9m7nEs-hCS5lj70T2PvSdwbqGlIjJBRTQKQIrlQ-iVCqOGYgmmroy2A5mC_LMdird0TSzByA4IWCoss-x6xIvlKuv4FsW4z8ADTaW4vzZGh_J3SVwG5exvTz-yefSBHghYkPceA-InSTNU7RalYAQwR9KZ2HpAWxPhXSCT9dwIEiUYlSHKQhSu3Lgtkx4Bqai6ndrpnCIarPxfhUHOBRgJmXV6OTJGIu6TkMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da696e6ada.mp4?token=kXnDzHGWAyz55k9a1FmlGG1TCLD0ZOV5lY7Vyoo-AoSO3J_DrvbSY9wbS9QSf23rh_8PxdxkQBbB-d4Euy_mox1bghodDMv5yBPO_ImDb_f9w33R-9m7nEs-hCS5lj70T2PvSdwbqGlIjJBRTQKQIrlQ-iVCqOGYgmmroy2A5mC_LMdird0TSzByA4IWCoss-x6xIvlKuv4FsW4z8ADTaW4vzZGh_J3SVwG5exvTz-yefSBHghYkPceA-InSTNU7RalYAQwR9KZ2HpAWxPhXSCT9dwIEiUYlSHKQhSu3Lgtkx4Bqai6ndrpnCIarPxfhUHOBRgJmXV6OTJGIu6TkMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، به شبکه خبری فاکس گفت: «بر اساس توافق حاصل‌شده میان واشینگتن و تهران، ایران به طور دائمی از دستیابی به سلاح هسته‌ای منع خواهد شد.»
او افزود: «تنگه هرمز بلافاصله بازگشایی می‌شود و محاصره دریایی آمریکا پایان خواهد یافت.»
به گفته معاون رییس‌جمهوری آمریکا، با اجرای این توافق، زمینه برای سرمایه‌گذاری‌های گسترده در منطقه فراهم خواهد شد.
ونس در عین حال تاکید کرد اجرای این توافق به پایبندی جمهوری اسلامی به تعهداتش بستگی دارد.
@
VahidOOnLine
جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت قصد دارد در مراسم رسمی امضای یادداشت تفاهم میان آمریکا و جمهوری اسلامی حضور داشته باشد، اما احتمال دارد دونالد ترامپ نیز شخصا در این مراسم شرکت کند.
ونس در گفت‌وگویی کوتاه با شبکه فاکس نیوز گفت: «فکر می‌کنم هنوز در حال بررسی جزییات و هماهنگی‌ها درباره افرادی هستیم که در مراسم امضا حضور خواهند داشت. من قطعا قصد دارم در آنجا باشم، اما این احتمال وجود دارد که خود رییس‌جمهوری نیز در مراسم حضور پیدا کند.»
سرویس مخفی آمریکا معمولا حضور همزمان رییس‌جمهوری و معاون رییس‌جمهوری را، به‌ویژه در سفرهای خارجی، به دلایل امنیتی و ملاحظات جانشینی توصیه نمی‌کند.
این اظهارات ساعاتی پس از آن مطرح شد که شهباز شریف، نخست‌وزیر پاکستان، از برگزاری مراسم رسمی امضای توافق میان آمریکا و جمهوری اسلامی در روز جمعه در ژنو سوئیس خبر داد.
قرار است دونالد ترامپ پیش از آن برای شرکت در نشست سالانه گروه هفت به فرانسه سفر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76352" target="_blank">📅 01:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76351">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22e031404e.mp4?token=JYHoinJQE6iMbuuWGGC3ZyahQ9A4E2CHnlkt0CTWp29kwzbyNyE-9QYR37CtWdeBbnSwC-YUvMXfQ6TO4fXysF_FWGORMaijrJecqM_K3YIwQCBlRgkaqVMmyudaVOQPhHiUxbOG_W2c82t-jpeZkJNU7baH2alfXzeTOrFEdV3_fzUXKMDiKEsgK9h67Kgv3bYvAxQ1JiRWwRhMuhMRyRjMdzypYanUwx4gQh5l4uiZ3VHxpbWWP4YtRANlXMGFLkaBWvmys4yoEdrA_fsJqchefRscKahuZhP8uKAN7tLZAx-Nn82xjNJKDIbbCL6zhcriAH_pKmc6enXtrHWmYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22e031404e.mp4?token=JYHoinJQE6iMbuuWGGC3ZyahQ9A4E2CHnlkt0CTWp29kwzbyNyE-9QYR37CtWdeBbnSwC-YUvMXfQ6TO4fXysF_FWGORMaijrJecqM_K3YIwQCBlRgkaqVMmyudaVOQPhHiUxbOG_W2c82t-jpeZkJNU7baH2alfXzeTOrFEdV3_fzUXKMDiKEsgK9h67Kgv3bYvAxQ1JiRWwRhMuhMRyRjMdzypYanUwx4gQh5l4uiZ3VHxpbWWP4YtRANlXMGFLkaBWvmys4yoEdrA_fsJqchefRscKahuZhP8uKAN7tLZAx-Nn82xjNJKDIbbCL6zhcriAH_pKmc6enXtrHWmYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر توافق و توقف جنگ در شبکه خبر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76351" target="_blank">📅 01:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76350">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MLEfzljjUiQj1mrPFq_UxIE7Zrbep7-VarUlSfYEkiSBTYxQwvJs5FTqfk8hnhif3WQ7znFL1v6m-DX42FD5tX-qL4WLSdGMlKtV6bJOfmAV_EQPgVhEWHLrv_uTnl8uvMUZQlCqW5YroPnn1Y_gfjZzYMncV47E2I-4y_uw2D9Jyip2yM0XW36dylixPbqwa0Qwb1l_CVJmCC9T8hzO6re59tKW0vH1kuBQ5CULfaUEIQi0FooZL2s9vbyVoYNmZARYnEFBTefGlQ0KGjLWJ78clVnAEMeP91OvL0MAbteSUB8UAmSWsgOcbFTQk6U7vs-mychXa79LjFm0iFsclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: تبریک به همه، توافق نهایی شد
پست ترامپ ترجمه ماشین:
توافق با جمهوری اسلامی ایران اکنون کامل شده است. به همه تبریک می‌گویم!
بدین‌وسیله من به‌طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را صادر می‌کنم و هم‌زمان با این، مجوز برداشته شدن فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
کشتی‌های جهان، موتورهای خود را روشن کنید. بگذارید نفت جریان پیدا کند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76350" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76349">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GqvbVrfZjkqNG7hlQpgTwRFYvyAOF93ufLU1Ro_aR6sVgd518bQPXXRIvHJt9AF1lH2Bu_-F7EOzQinSYm0rypHtPFhnpR8p-WEROmDYCqkPGSY5apPOXiEdfYc68uc97NA2sje3n8xXq_ZT9DvDDoo-p-ibNQCooGeTZm2C3xjzc201KLpkAo8_YKy_ns-_tWglfdzPltmwwoLkckYmYCRtsNliHqkBw_FRjO-tR-GH3o0X5XEH6IA5yj8WW6Nsjdk4UY8MC0gPluKARfadCpbflKvpiv4zDqeX9IKbmLnRYpy4vIoxqJCIvsWuLWq6mcBuMrttWe5v5-2gjdgNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبر:
نخست‌وزیر پاکستان از دستیابی به توافق و پایان جنگ خبر داد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76349" target="_blank">📅 00:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76348">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QLc5wGGEj6CP3DTmV_5l26_LxSWTNUvTCCj5kPI5U-DM_xhtoH_V6649RXCfKoMMw39G-IRT19Fj58gMecffoawhQ119olGRkMsX7mhY3lD2FTIq9K1j1I7l7xIDeX3TOjFIBa3KiO1LrEkWZvoQOD8Sji5bvh8126waoz-lkiKGwXYU8zvmDvoTaLZ_aVv_E4et5ImXZcuubgoTe2776GfNqCLNNZUVDl4_u0YIF5gxOkbsFfXzYOuVXgZVgBzo6TkDxIYAoerWl9h7vSNRaq7iUQZGoyPzFf2_FDCj_PfbLegzd4P9s_hrO8sGBUmVoQ_vq7EDby1jAidP6Ah_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
نخست‌وزیر پاکستان: توافق حاصل شد
مراسم امضا جمعه در سوئیس امضا می‌شود
پست شهباز شریف، ترجمه ماشین:
در پی مذاکرات فشرده، خوشحالیم اعلام کنیم که توافق صلح میان ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شده است. هر دو طرف پایان فوری و دائمی عملیات نظامی در همه جبهه‌ها، از جمله در لبنان، را اعلام کرده‌اند.
مراسم رسمی امضای توافق روز جمعه، ۱۹ ژوئن، [۲۹ خرداد] در سوئیس برگزار خواهد شد.
مایلیم از ایالات متحده آمریکا و جمهوری اسلامی ایران به‌خاطر تعهدشان به یافتن راه‌حلی دیپلماتیک برای این مناقشه تشکر کنیم. همچنین مایلیم قدردانی صمیمانه خود را از برادرانمان در این تلاش میانجی‌گرانه، رهبری بزرگ دولت قطر، به‌خاطر حمایتشان در دستیابی به این توافق ابراز کنیم. به‌ویژه از رهبری دوراندیش پادشاهی عربستان سعودی و جمهوری ترکیه نیز به‌خاطر مشارکت‌های عظیمشان در این زمینه تشکر می‌کنم.
اکنون که توافق برقرار شده است، میانجی‌ها مجموعه‌ای از نشست‌ها را در این هفته تسهیل خواهند کرد. این گفت‌وگوهای پیش از اجرا، زمینه را برای مذاکرات فنی و مراسم رسمی امضا فراهم خواهد کرد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76348" target="_blank">📅 00:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76347">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cb9bbe1383.mp4?token=WLbpjFHmMcC-GFbZQQ3hPJ1H8dRNuSGUl5aD41lQLr7Cdso6xMDccNPdfd5TINwsM38QQ1KeERQ_MT432r_XUsrs1aL03RYz1kJJNoQ-ZDdlQIAl6ppgjQs9aqJN9JemkTe2N5vFJZtCFVDOPiZxgIVhOmb0OMl0aemJIoAzRQxnuyT3-kSN8VthttWNq54tPUdxz8bQfORJyMIBSd_BQNv49NyN-2x7Fo4aahZDCX83-YuUwdHbJPrQbOHPlpL66eI8CBfxMzp2dj1qX-JMBZcO8eZsfv63W0-ak9pkfDnIrUzNgsgQTqea2Jz4qVI_GUxTV4Ii5GRllg5lqHpBQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cb9bbe1383.mp4?token=WLbpjFHmMcC-GFbZQQ3hPJ1H8dRNuSGUl5aD41lQLr7Cdso6xMDccNPdfd5TINwsM38QQ1KeERQ_MT432r_XUsrs1aL03RYz1kJJNoQ-ZDdlQIAl6ppgjQs9aqJN9JemkTe2N5vFJZtCFVDOPiZxgIVhOmb0OMl0aemJIoAzRQxnuyT3-kSN8VthttWNq54tPUdxz8bQfORJyMIBSd_BQNv49NyN-2x7Fo4aahZDCX83-YuUwdHbJPrQbOHPlpL66eI8CBfxMzp2dj1qX-JMBZcO8eZsfv63W0-ak9pkfDnIrUzNgsgQTqea2Jz4qVI_GUxTV4Ii5GRllg5lqHpBQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی منتشرشده در شبکه‌های اجتماعی نشان می‌دهد جمعی از حامیان تندروی جمهوری اسلامی کفن‌پوش شده و در تجمعی مقابل استانداری زنجان شعار «اگر چیزی امضا شه، مسئول باید کشته شه» سر دادند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76347" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76346">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kR2gHkOOnqRmlflG-xGvlErPErhw1IQ8dokcXmOkvTnN-uCwvNgzHLlhyHgCmgZ1NKo17l8Brr8HPkhxYxByhhP5Td3jkzB93V3krJbmdqbNs4eoaakqlBu8fkrmPlYfi1Rch0DJnTnLitmfkHZJ6VVrONkswhPleUq3f73cUv5DzMN3xFMUaKjj-zqMRlK9XqZpAbDicyeE75pQQWUkkpR2PatWshrJVyvzc_POIKpm2s6V0XIzW-_yHUKmoPH_Qf02_FPjwZA3FigSJxUr8oLevOLsDFL0xTDNMKdhZFp5J_DFkFQ9bsE0dvEas94y8_n-jaiwcuYNKUm1Yfdhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در گفت‌وگو با
وال استریت ژورنال
گفت توافق با جمهوری اسلامی قریب‌الوقوع است، اما تهران هنوز موافقت خود با آن را تایید نکرده است.
ترامپ افزود قصد دارد به‌زودی بیانیه‌ای صادر کند که در آن اعلام خواهد شد آمریکا با جمهوری اسلامی به توافق رسیده است.
او گفت این توافق، در صورت نهایی شدن، یا توسط خود او یا از سوی جی‌دی ونس، معاون رییس‌جمهوری آمریکا، به‌صورت الکترونیکی امضا خواهد شد.
رییس‌جمهوری آمریکا روز یکشنبه این توافق را گامی بزرگ در مسیر پایان دادن به درگیری نزدیک به چهارماهه توصیف کرد.
ترامپ همچنین گفت این توافق شامل تعهد جمهوری اسلامی به دست نیافتن به سلاح هسته‌ای و بازگشایی فوری تنگه هرمز خواهد بود. او افزود عجله‌ای برای خارج کردن مواد هسته‌ای از ایران وجود ندارد و این موضوع می‌تواند در مرحله‌ای بعدی دنبال شود.
ترامپ گفت: «بعدا و زمانی که آماده باشیم وارد عمل شویم، مواد هسته‌ای را جمع‌آوری خواهیم کرد. به نظرم طی یک یا دو ماه آینده این کار انجام می‌شود و عجله‌ای وجود ندارد.»
@
VahidOOnLine
نقل خبرگزاری فارس:
ترامپ: به‌زودی بیانیه‌ای صادر خواهم کرد که تایید می‌کند آمریکا با توافق با ایران موافقت کرده است
🔹
این توافق به‌صورت الکترونیکی، یا توسط من یا توسط معاونم ونس امضا خواهد شد.
🔹
توافق شامل تعهد ایران به عدم دستیابی به سلاح هسته‌ای و بازگشایی فوری تنگه هرمز خواهد بود.
🔹
ایران هنوز موافقت خود با این توافق را تایید نکرده است.
🔹
هر زمان که آماده باشیم، مواد هسته‌ای را تحویل خواهیم گرفت و این اتفاق ظرف یک یا دو ماه آینده رخ خواهد داد.
🔹
من خواهان پایان یافتن حملات هستم و ایرانی‌ها هم می‌خواهند که جنگ تمام شود.
🔹
من هیچ‌وقت به دنبال تغییر رژیم ایران نبوده‌ام.
🔹
بازرسی‌های بسیار دقیق و شدیدی از ایرانی‌ها به عمل خواهد آمد.
🔹
در این توافق پولی به ایران داده نخواهد شد، اما احتمالاً تحریم‌ها لغو می‌شوند؛ باید ببینیم در عمل چگونه رفتار خواهند کرد.
🔹
محاصره دریایی اعمال‌شده علیه ایران موفقیت‌آمیز بوده و تاثیر آن از حملات نظامی هم بیشتر است.
🔹
نتانیاهو از این توافق حمایت می‌کند؛ این توافق برای او خوب است چون تحت هیچ شرایطی اجازه نمی‌دهد ایران به سلاح هسته‌ای دست پیدا کند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76346" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76345">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZcCE0zcZiIfa1wZQ4x0ExJ1qGL3tAE2S8UhWbjc0geg9-EvxHFhZHN-YZcxsrEfqGiErQEgU-Kq63ytKO9Yg1t00x7HkgOGNasjo9WfHPClPXMTtitaXLUrr3RRi5Ok8MzkV_n5tLGvAcUo8xJj31O-zJUBaIRNZDHm4wze2M-dRJed2yp-FamvYAaAMn5cGF_Ljp55y0E2w-XlpZ5H_AfR63X5Fn1pAvvDWaRV4PdaBM8H6C0W6LVb-2NVJKpd2VvW4DRzKjOCsPIAhtLxvrMg8RNlFUUuqsbtWeD92GO_K_Nz86tSRs25HYEJi5yv6lMUBU71t0BJW1CD-COdL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «کانال ۱۲» اسرائیل، بنیامین نتانیاهو و دونالد ترامپ لحظاتی پیش به صورت تلفنی گفتگو کردند و رئیس‌جمهوری آمریکا، نخست‌وزیر اسرائیل را در جریان «پیشرفت‌های کلیدی برای امضای توافق با ایران» قرار داد.
مقامی ارشد اعلام کرده که احتمال امضای این توافق «حتی طی همین امشب» (بامداد دوشنبه به وقت تهران) وجود دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76345" target="_blank">📅 00:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76344">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پست‌های ترامپ، ترجمه ماشین:
سناتور جک رید، یک «دموکرات» از رود آیلند، وقتی گفت توافقی که ما همین حالا انجام دادیم به خوبی فاجعه اوباما، معروف به برجام، نیست، دروغ گفت.
رید یا یک کلاهبردار تمام‌عیار است یا بی‌کفایت.
توافق اوباما مسیری به سوی سلاح هسته‌ای برای ایران بود، همراه با پول نقد و همه چیز؛ یکی از بدترین و احمقانه‌ترین توافق‌هایی که آمریکا تا به حال انجام داده است؛ به همین دلیل هم می‌گویم «دموکرات‌های احمق»!
توافق ما دیواری در برابر دستیابی ایران به سلاح هسته‌ای است؛ درست نقطه مقابل اوباما.
جک رید را استیضاح کنید!
(توضیح ماشین: در متن اصلی چند غلط املایی عمدی هست: Dumocrats به‌جای Democrats برای تحقیر دموکرات‌ها و Obuma به‌جای Obama.)
realDonaldTrum
ویکتوریا کوتس از بنیاد هریتیج واقعاً فوق‌العاده است! او موضوع را مثل تعداد کمی از دیگران می‌فهمد. متشکرم ویکتوریا.
ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز هم به‌زودی برای تجارت باز خواهد شد!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76344" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76343">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XBoJFEOhdjjIhA-vc3geTSeB1vo2S85umXiidi4MG15imBmPcXhovRgPZ4mjiRb74cgUgfED_6o0nZn22h8kZuz1P0fXf2KwMP_r1711JsEI1BinZseKClRGzn4RIBPdoutXsH0EvNTpkil9eJ-z0V5Z6DxpvCw3mKxNhZzk_R5x-8tlkStQeC1baz7u5-QgbVIXTsRov7jHatXldXCy7PTqWo83OqXlZYZptjLOc-7G6zhZ8PMAIQR0EJQRWSorl0e8evEzD26gJxx-OPdhDIwD5s6OY2X4Pcfox-gSaXK1-CRHttfU823GLRgeOCUvAQ7535TZK5TlGgPM9Yeg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، در واکنش به حمله اسرائیل به اهدافی در جنوب بیروت در
شبکه ایکس
نوشت: «مجاهدت‌های رزمندگان لبنان و دیپلماسی مقتدرانه جمهوری اسلامی حاکمیت و تمامیت ارضی لبنان را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی اسرائیل را بر هم خواهد زد، بچرخ تا بچرخیم.»
قالیباف تاکید کرد که هیچ‌یک از ارکان مقاومت را نمی‌توان «تک و تنها» قرار داد و حاکمیت و تمامیت ارضی لبنان حفظ خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76343" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76342">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lKKwDE8DTEZ7SEeq8LV30ETp4Avp4ee5z4ZvhAv6OyNaA-Wxte-2q-rmEqEavGuwDhxvsm15eD3_jtOP2x4FI7AOdMXN60ZifZpJzcu2HbpL8ZJ0ZqhFQLpM-Yg6VoqZNaKo3VqkmpXd0ay1UTULHGjgI1rnhLUIaOB7FuqOZC7H0350TOkx0jgC9k-eGgnseETeSPILXo0bciX2G8LFJyDdxJX14BiCMcLO-C1bF7T8uqIvTNu3weG1VWU3vhuKc8h9s_MbXE4RlwKCk93qymEATva2sjOpG5C1c8opk-dKgRCwDikCHuQJ6CrC1W0Fppn_S4dbOT9s2tRhMt0lsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم و صدا و سیما:
پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است.
این تصمیم در پی شرایط موجود اتخاذ شده است.
سازمان هواپیمایی تا این لحظه هیچ نوتامی منتشر نکرده است.
خبرگزاری مهر:
هیچ نوتام جدیدی درباره محدودیت پروازی صادر نشده است
🔺
مجید اخوان، سخنگوی سازمان هواپیمایی کشوری در گفتگو با خبرنگار مهر درباره برخی اخبار منتشرشده در فضای مجازی مبنی بر صدور نوتام جدید برای محدودیت پروازی در فضای هوایی کشور، اظهار کرد: هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
🔺
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76342" target="_blank">📅 22:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76341">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/201a6972d8.mp4?token=cTDDVvJ28g55sUVBVehQwWbtPUuFLil5xsaxNsbcShHFeund-47JNv_OPsnL3o7gydaf16Stbo53u-P92gGGIsRckptEDZy2PL9tBdnSajG5iam1Y2B5AyO-qiH4nARt4Dd7YauWJ48Aq1OaXRtbEyGGCcN49flubwbIvRK39sDosDcuUu2nt9249Q5GuwVggqKPE2NJdstXPQXvSFufGsgd9zaXr4Gdd9VVa_L3gly1v3O_JXl8QZt7xXRgq9r1HMG75J5w5_mYJgjPm-Ho7EuV1XikBmDqyamGBM0RI3PZmTlQgvfHNtS_4XNhI3oJA04Uaq4BTCu2c-hZWswrzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/201a6972d8.mp4?token=cTDDVvJ28g55sUVBVehQwWbtPUuFLil5xsaxNsbcShHFeund-47JNv_OPsnL3o7gydaf16Stbo53u-P92gGGIsRckptEDZy2PL9tBdnSajG5iam1Y2B5AyO-qiH4nARt4Dd7YauWJ48Aq1OaXRtbEyGGCcN49flubwbIvRK39sDosDcuUu2nt9249Q5GuwVggqKPE2NJdstXPQXvSFufGsgd9zaXr4Gdd9VVa_L3gly1v3O_JXl8QZt7xXRgq9r1HMG75J5w5_mYJgjPm-Ho7EuV1XikBmDqyamGBM0RI3PZmTlQgvfHNtS_4XNhI3oJA04Uaq4BTCu2c-hZWswrzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شماری از حامیان جمهوری اسلامی و مخالفان توافق با ایالات متحده، در تجمع خود با سر دادن شعار خواهان اعدام عباس عراقچی، وزیر خارجه حکومت ایران شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76341" target="_blank">📅 21:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76340">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LVdE9PWSLbMRhxLkPge3bRHwDQ-r0l7Xpc6jgNe0Bhu7c6prKuFbmHuylSNIPiEajiZCsIwS5QBQ7JefPKRMby7MffU8VLDjIWpOVu54uWqGIR9t0vXkUrqq4_czArga8NxamWopk8Vb_uOPx-nsh38aRRSiNptyVw5RwUAxaisSH14NUOvk5LWiOTUz7iXF30ZBFv6mNR_kn9NNIAqXM9nM9zMp7hQpezqsYs2zMy5BmdCtYWzA_eG6UhB8pH-Ob_knWiJH0JaLCBbvQi7ohJWTm-ziKyFS3h3DoEeDozBE6T15LuhglgJx1AHY8voun4_A35cb01BTbilaeXxZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"‏پاسخ رزمندگان اسلام در پیش است."
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی در جمهوری اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76340" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76339">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JtlZrQpOVWo6ktkTkPHnAknhWPxZxX8A-9uEV2Er8MAlKubyT3hiG8vrzY9rJvovpGtKWe_vjjZOgCicG_u-tDGoKal-SXyWa_oiOv_UoEw1cgqOR0GPKunT1jq-sobqWMUK9mbyauafmI7cr_l5jIty1Ssq55hFBgA8QOvixYJOHgj1uNBGUbw9pkNPkv7_mGCOjT0mKDchdoa2_sbC7--jZQK1BE1x6NCiITJU9vBhuhbVsylNv94uPTmF9b3HJYTcW8EAwQQTQ1YDXoYyhzxJlDH6lC2_1etGJVpKI7-ThBdolIQMQkOeLDWQW7ksS8AIUbcCU_YE5iQNs9ik8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب تصاویر #مجتبی خامنه‌ای و آدولف #هیتلر با هم عکس جعلی چهره رهبر جدید جمهوری اسلامی (دستکاری شده با هوش مصنوعی) رو با استناد و افتخار به سخنان جعلی و چرندیات هرگز گفته نشده آن جنایتکار دیگر منتشر می‌کنند. عکس دریافتی از بابلسر، سه‌شنبه ۴ فروردین Vahid
📡
…</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76339" target="_blank">📅 20:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76338">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPW0VaegnynrBS_9cCw0ZQTDL3QSC5xjvbGnEQ14sZEW_uxqKkzmEjNGLDVvxgDXX_Z_avZOJMW4bAx3touow_8wMKWzLuIp6XS5whjv6KqhnSPN__9X8rOWzQWqd_beeQPX3tjvOpOw45NxdO7bLqJSZUMls_13o6VtWM62vXawXlgcak22_IUbx95vxesS3NlK6EP-LkVzcG_rNk-qE2VvmDzNReZ2gqNuBrRBMqHOoFtcJIw3VWZ4CluSsMrjmCsCgpBw9N-miymw_1NTMijMygn8MzmvTNJBy2UgR8tyZyUMATbX13cL6YLud5rXVFf3DxStR2579IkOiYzZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، در پی انتقادات برخی حامیان حکومت از محتوای توافق احتمالی با آمریکا، روز یکشنبه گفت که روند مذاکرات بر اساس مصوبات شورای عالی امنیت ملی و دیدگاه‌های رهبر جمهوری اسلامی پیش می‌رود.
او در دیدار با مدیران رسانه‌های داخلی افزود: «تصمیمات راهبردی کشور باید در چارچوب سازوکارهای قانونی اتخاذ شود و همه جریان‌ها و گروه‌ها نیز خود را ملزم به تبعیت از این تصمیمات بدانند.»
در آستانهٔ امضای تفاهم‌نامهٔ ایران و آمریکا برای پایان جنگ، اعتراض‌ در میان حامیان تندروی حکومت به متنی که به‌عنوان تفاهم‌نامه در برخی رسانه‌ها منتشر شد بالا گرفته و تجمعاتی نیز توسط گروهی از طرفداران جمهوری اسلامی علیه این تفاهم و مذاکره‌کنندگان برگزار شده است.
در یکی از این تجمعات در تهران، تجمع‌کنندگان علیه عباس عراقچی، وزیر خارجه، و محمدباقر قالیباف، رئیس مجلس شورای اسلامی، شعارهایی سر دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76338" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76337">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c24456e9d.mp4?token=b4ny70IZ0EceKVSCZ83v65EL5Q6_G4vbfvOTmnETh_7V9H_3fpiDYmaD_EMbhNA7AenUxvRkNJMyr8PMXceCRW8xn2bmKLxcmL94TV-wTUsKYZZNf4O3CMpt5EzUidr7h9FupT_rXTlKvuo3rjzAr9WMR2D6-FRGQ4L2PNXJfu7YSyXwY5CTUGhJurE236zVpQqntXd2pEanVx-1zxzyGrug0R8ZitVzLqc8P0GkbX4pqrKUeL7QLglKBv1COOax5FWI2zcljSTwt3J7WNd_prJQgS34SACVKGcCQ3XKskuEKijRgWuAXuNP-c6vciDIb7L4gIJM5kRoQbex2lzecg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c24456e9d.mp4?token=b4ny70IZ0EceKVSCZ83v65EL5Q6_G4vbfvOTmnETh_7V9H_3fpiDYmaD_EMbhNA7AenUxvRkNJMyr8PMXceCRW8xn2bmKLxcmL94TV-wTUsKYZZNf4O3CMpt5EzUidr7h9FupT_rXTlKvuo3rjzAr9WMR2D6-FRGQ4L2PNXJfu7YSyXwY5CTUGhJurE236zVpQqntXd2pEanVx-1zxzyGrug0R8ZitVzLqc8P0GkbX4pqrKUeL7QLglKBv1COOax5FWI2zcljSTwt3J7WNd_prJQgS34SACVKGcCQ3XKskuEKijRgWuAXuNP-c6vciDIb7L4gIJM5kRoQbex2lzecg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: به نتانیاهو گفتم داری چه غلطی می‌کنی؟
ظرف دو سه ساعت آینده یک توافق بزرگ امضا خواهد شد
به ویدیوی بالا با هوش مصنوعی زیرنویس فارسی اضافه شده، متن دو دقیقه اولش:
«بله کوین، عصر بخیر. همین الان با رئیس‌جمهور ترامپ صحبت کردم. او به فاکس‌نیوز گفت که معتقد است یک توافق بزرگ با ایران ظرف دو تا سه ساعت آینده امضا خواهد شد.
از او درباره حملات امروز اسرائیل علیه حزب‌الله در پایتخت لبنان، بیروت، پرسیدم. او گفت با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، تلفنی صحبت کرده و از او پرسیده: “داری چه غلطی می‌کنی؟” ترامپ گفت به نخست‌وزیر گفته بود این حملات علیه حزب‌الله را انجام ندهد تا بر پیشبرد این توافق اثر نگذارد.
اکنون اسرائیلی‌ها، به گفته ارتش اسرائیل، خود را برای احتمال شلیک موشک‌های بالستیک ورودی از سوی ایران آماده می‌کنند. رئیس‌جمهور ترامپ به فاکس‌نیوز گفت از ایران خواهد خواست با شلیک موشک به سوی اسرائیل پاسخ ندهد، چون این توافق در آستانه امضا قرار دارد و انتظار می‌رود امشب امضا شود.
همه اینها در پس‌زمینه تازه‌ترین گفت‌وگوها برای رساندن این توافق نهایی به خط پایان رخ می‌دهد. رئیس‌جمهور درباره حملات میانه هفته گذشته هم صحبت کرد؛ زمانی که آمریکا بسیاری از مواضع ایران را زیر ضربه می‌برد و ایرانی‌ها را به میز مذاکره برمی‌گرداند.
شاید یادتان باشد، کوین، من با رئیس‌جمهور تلفنی صحبت می‌کردم، در حالی که او در اتاق وضعیت بود، و ایرانی‌ها با او تماس گرفتند و از او خواستند بمباران را متوقف کند. رئیس‌جمهور معتقد است همان لحظه توانست معادله را تغییر دهد و دوباره ایرانی‌ها را وادار کند این امتیازها را بدهند.
رئیس‌جمهور ترامپ گفت اگر آنها امشب توافق را امضا کنند، او فوراً دستور خواهد داد محاصره بنادر ایران برداشته شود و سپس وارد گفت‌وگوهای جزئی‌تر درباره برنامه هسته‌ای ایران خواهند شد.
اما دوباره، مهم‌ترین خبرهایی که اکنون می‌دانیم این است:
رئیس‌جمهور ترامپ به فاکس‌نیوز گفته معتقد است توافق با ایران ظرف دو تا سه ساعت آینده امضا خواهد شد. به گفته رئیس‌جمهور، این امضا به‌صورت الکترونیکی انجام می‌شود و حدود یک هفته بعد انتظار می‌رود مراسم امضای حضوری، احتمالاً در جایی در اروپا، برگزار شود.
باز هم تأکید می‌کنم: رئیس‌جمهور پس از حملات امروز اسرائیل به پایتخت لبنان، بیروت، واکنش نشان داد. اسرائیلی‌ها در پاسخ به آتش پهپادی این هفته از آن سوی مرز به سمت شمال اسرائیل، مواضع حزب‌الله را هدف قرار دادند. و رئیس‌جمهور می‌گوید از نخست‌وزیر اسرائیل پرسیده: “داری چه غلطی می‌کنی؟”»
TreyYingst
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76337" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76336">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XS7bCuf2FJe9gZFzDoeKNQQykbubgiF93zgmm5oIvuasvGe_wgWXd8Rjsw3FOqmxAzomQtZ1NoJpntK99Qr8MPRrIEjQBPUHcqO-sVoFSTmOYDUEuVbAagE9D6lWSmJcSbckJfLRB_iuBWLB4GwVMz5z_MdGQPlIktX01WsZGdd74K5Djo7_XLvFpU9RfaZ-WwX4eS62562mxyn01J1AbAWyrloZ2tvrqI1EKCaE4JiX2VtioMkdJPjPK4oSf-6JbcOsJlnu24h20zNcv73Gv0m4VPsfvvCEveW-XnWTLxyDvqmnzlnqu62oYLf3LzetkzrG1STgjy_pFPqt4EZ-zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی، فرمانده نیروی هوافضای سپاه پاسداران، در پیامی از حامیان جمهوری اسلامی خواست در مسیر تحقق آرمان‌های نظام، از مجتبی خامنه‌ای تبعیت کنند.
او نوشت: «ملت بصیر و غیور که در خونخواهی علی خامنه‌ای مبعوث شدید و در راه تحقق آرمان‌های بلند انقلاب اسلامی با مجتبی خامنه‌ای عهدی تازه بستید، هوشیار باشید که از شئون متعهد بودن، تبعیت کردن است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76336" target="_blank">📅 19:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76335">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RnRvQhN7HBvz-FIdsvNeaXqL2KLMqMG5IQDsBRmjmaG-r8wnVsuDTPqJBAESC8N_c7eDE9mfSyjYWkrwbBH6QOet5QVIxv4tXANzbEhJBcNkIWAlrup6icE_bf2nfEMqnX8wGTea3qYoz9hpuLlvFkR76rRgD5xlqeZK_pb6tCoItceDXhNzVygfiMBhF0EzZGkSb4zVZUcwVHFt0hNd584cVmHYt7BNiq-nPH5M1bcEGQ2pZbkdtTpUBLLC5-80CzR5ir-LmVA1YyrmiQJyhR7mkW6rD76c4TyKFWMKxp9a-Xm1t9kn9Y54z5sgLwTOEaKo3cmvfoBk7PrGeB42pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: بیایید خرابش نکنیم!‍
پست ترامپ، ترجمه ماشین:
حمله صبح امروز به بیروت نباید اتفاق می‌افتاد؛ به‌ویژه در روزی خاص که ما تا این اندازه به توافق صلح با ایران نزدیک هستیم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در پاسخ به آن انجام شد بسیار کوچک و بی‌اهمیت بود؛ هیچ‌کس آسیبی ندید، زخمی نشد یا کشته نشد، و نباید این روند مهم را مختل کند.
ما به توافقی بسیار نزدیک هستیم که صلح را به منطقه، از جمله لبنان، خواهد آورد و همه طرف‌ها باید عقب‌نشینی کنند. دیگر نباید هیچ حمله‌ای از سوی اسرائیل در هیچ نقطه‌ای از لبنان انجام شود، اما همچنین نباید هیچ حمله‌ای از سوی هیچ طرف دیگری، از جمله حزب‌الله، علیه اسرائیل صورت گیرد.
این می‌تواند آغاز یک صلح طولانی و زیبا باشد — بیایید خرابش نکنیم!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76335" target="_blank">📅 18:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76331">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QCYy05oPPvZa51hDrSuQHNa0SzoGlukrO4NSxpOs5awE5rjo4B69HGq-2RjcFh5hA2AT284CgOLZmxCRXscl8WZ0bjBfGAZ3d17RMSvMD6LXFlOG5GfNUW5xX5khgKn8OeIrIHEJiZSm1JhAS0kidYpFIGGW-wDsLUydX7TPjGZ77hfG31k4NnR1HcrSiOkOkqK04aGcqwzBtXHtQi91Us0D_XWiwhbRkQpvOP7bE6_0Yci41Plamxsi2BPOloxcng1RcOn-O4cLP4BUyLk230-jnMWO_VUHBuhHDmXCO2i2AYX0Qv5KQ-MdQ8HnThvU4sx3nwwW7dP59l2-RxO6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qfM4B8Z8ykTOHVoQE0YbOXckFcaOBRBINvSUbC6PwTTHZCuiTv7mzxY0CvkT2zkF6Q4o8wk8PhZOfmoPG5nEbGNkeM7lau-a4ok4SihWtzNubefc5mWRhJy0voVU_ujtJvOskBOcQx3mVZZ5BnQEXGiBdlK3Fj-3LwHiW2YqhbTQzhA80Eqzyi-kcH8KHpMBthFWWlGO4NYb6OBLtVkEjGCz3amwHSQvd8fnq8N3Ol1aqIDvb_6Th_3O-qwaXHvRaI4U1U4DFWWT-ddWY9HBGpymu3CyV-UgFC75cNnm-QCe2Y0kzJVPveQ60Vxydr9ns8FVXxs2Y0iM7WbLVwF3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZHPBertrOYP8wDDv685Kc4Ri7bQp8OnF7DydUZa-5L-dANzaKDmiXdLAdfqSFttmhOCC947-A9YI1-8jgzr6rs5Tn1uuez8gkK9W81rJehwKF4RxzEOH3oLXaDQVeEsqOQgqyuRPS3TWkVP1AFC4hr87BTvT6EOo12cfmuBc1ddvbXViEELZ43G9FaPQCCUh58ZAeg5tzvTAjvTScT5rSh2mEwBeJGCGIpOy3fYZeTWtytR9FVveFQgGX1l_FL2rQ4YxqxD_ZnZCUlHjqRsKdw4RfCMFhBIwnCNFd3j-igts81NsLKXDceCoWwx0_GhSCsoJQ41J2jQ1RGlhUoXpcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WaKE-Y-E5urlVOWS7kRX6e481aAEM1EsoikEzdW2toXcMvLYQoPOVhAoXRqk63ojH23k_HyYEfHJe0Xlaa9EcHOPeJ0YGHkYOPArsESxpt7bwR0C83_UVnYtemhO6fo5v_FmEK4oAO6OE3iuW90ebzOaHygOcMVzXz1V0tZq3y8WSr3B9AHNslGGY4-h1hQ2_79VZBCP6pIaR7fF2oc1MRyCYWA4addWi3lnhRpOicmsSGtKf91eby5sh2YKIRF-Dw-bEPwseI-kL7fgLT5tAOXhqwA7iTEADK43EeFUbua64zyuK-MHJJMgedqdtBiYHTh1Eld9TevpafJBRUtGSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدجعفر اسدی، معاون بازرسی قرارگاه مرکزی خاتم‌الانبیا، در واکنش به حمله اسرائیل به ضاحیه بیروت گفت: «بدون شک این جنایات بی‌پاسخ نخواهد ماند.»
او در گفت‌وگو با دفاع‌پرس، حمله ارتش اسرائیل به منطقه ضاحیه را محکوم کرد و نسبت به پیامدهای آن هشدار داد.
ارتش اسرائیل در بیانیه‌ای یکشنبه ۲۴ خرداد اعلام کرد در واکنش به شلیک پرتابه از سوی حزب‌الله به شمال اسرائیل، اهدافی از این گروه را در ضاحیه بیروت هدف قرار داده است.
@
VahidOOnLine
محمد مرندی، از اصحاب رسانه همراه با هیات مذاکره جمهوری اسلامی در پاکستان، درباره ادامه مذاکرات تهران و واشینگتن، در شبکه ایکس نوشت: «فعلا هیچ مذاکره دیگری در کار نخواهد بود.»
@
VahidOOnLine
نظام‌الدین موسوی، سخنگوی پیشین هیات رییسه مجلس جمهوری اسلامی، در پلتفرم ایکس نوشت حمله اسرائیل به ضاحیه بیروت در روزی که قرار بود تفاهم میان جمهوری اسلامی و آمریکا امضا شود، با هدف بر هم زدن تفاهم انجام نشد، بلکه تلاشی برای «تحقیر جمهوری اسلامی» صورت گرفت.
او خطاب به تیم مذاکره‌کننده جمهوری اسلامی نوشت: «حضرات مذاکره‌کننده، به تحقیر تن ندهید و در شرایط تحقیر، هیچ چیز را امضا نکنید.»
@
VahidOOnLine
ارتش اسرائیل اعلام کرد ایال زمیر، رییس ستاد ارتش، پس از حمله به بیروت در حال برگزاری ارزیابی‌های مستمر از وضعیت با همه فرماندهان مرتبط است.
ارتش اسرائیل افزود بر اساس این ارزیابی‌ها، خود را برای احتمال شلیک به خاک اسرائیل در ساعات آینده آماده می‌کند.
این نهاد تاکید کرد در بالاترین سطح آماده‌باش قرار دارد و برای سناریوهای مختلف دفاعی و تهاجمی آماده است.
ارتش اسرائیل تاکید کرد شلیک به خاک این کشور را تحمل نخواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76331" target="_blank">📅 18:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76329">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ulzu_EjWgbpgmAyMIoQbgcNQ1s5jZZQo6wE4HoRpqnngfVbZjyCC_00OuKy13U2J1YjQ_8v-K-0OwWQwMCxxC338Wo0j8XtEGwYkAXLsu185QLCPCmzeCEhvgyL5DpKJTKfyrcWx2BTUfQCBa7Zth1jW1bE4bfWx53kvGQ4YPCm8xlaCIgW-PgHWdF0TqpAjWh1UmK1qGol25NVOhjJPJYAuS9ua6VteN-r80d22VCEmN_vFbb-T8Q11JdWFaIi2xF7dOe_SgwRzN6MOS_eVibrrhFz5r0FYb3Ie-7iXow1Yh6bEvE_tCFOZpWNEODqrbK6qqz-eUCkTs8vGt7m3Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VLxo-r6ZRh28An_X4y-BS9iS8dSoHZ6WpP_McgjwSk9zNwEfQBzSs5qEOl_JT33l306vxbq19snZtfZDmj6v_RHYAb2y_pWZ_FKVzf-G97F5WdMXQ7om90yj70YtWy1FXLjMX_4VD_mUNXxzpQ6QYFM4eo3N43moLFJTADOvdwVXyxIZf1-MTzPK4JYdInklFI09DcARr1T8osTzgYy6rv1cVz4gdQIoJz6M8gzrss_WkPBERCky1YOhhKyKLy_n3MhUpHtnyYiJNfTo_ST8wIHuC86YV_ery41-peQFhbyxOnL2XNSiSm3WPzScnKlFu9_eYcdgZWvxgzgk8caJ7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوهای توافق با آمریکا، اعلام کرد پس از حمله اسراییل به حومه جنوبی بیروت، ادامه مسیر توافق با آمریکا «ممکن نیست».
قالیباف روز یکشنبه در پیامی در شبکه اجتماعی ایکس نوشت حمله اخیر به حومه جنوبی بیروت بار دیگر نشان داد که آمریکا یا اراده لازم برای اجرای تعهدات خود را ندارد یا از توان انجام آن برخوردار نیست.
او افزود تلاش برای کسب امتیاز از طریق چراغ سبز نشان دادن به اسراییل نتیجه‌ای نخواهد داشت و سیاست «پلیس خوب و پلیس بد» دیگر کارایی گذشته را ندارد.
او تاکید کرد: «اگر اراده و توان اجرای تعهدات خود را ندارید، سخن گفتن از ادامه مسیر ممکن نیست.»
@
VahidHeadline
حساب رسمی وزارت خارجه اسرائیل، روز یکشنبه ۲۴ خرداد ماه در واکنش به اظهارات محمدباقر قالیباف، رئیس مجلس شورای اسلامی در شبکه اجتماعی ایکس نوشت: جمهوری اسلامی «مثل همیشه دروغ می‌گوید.»
وزارت خارجه اسرائیل در این پیام با بیان آنکه اسرائیل شلیک به خاک خود را تحمل نخواهد کرد یادآور شد، حزب‌الله، صبح روز یکشنبه «بدون هیچ‌گونه تحریک قبلی» بار دیگر به اسرائیل حمله کرده است.
در این پیام آمده است حزب‌الله به طور مداوم غیرنظامیان اسرائیلی را هدف قرار می‌دهد و حتی پس از برقراری آتش‌بس نیز حملات خود علیه اسرائیل را متوقف نکرده است.
قالیباف در روزی که به گفته دونالد ترامپ قرار بود توافق پایان جنگ میان ایران و آمریکا امضا شود، در ایکس نوشت حمله اسرائیل «به ضاحیه بار دیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را. با چراغ سبز نشان دادن به رژیم نمی‌توانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب قدیمی شده است. اگر اراده و توان اجرای تعهدات خود را ندارید، سخن گفتن از ادامه مسیر ممکن نیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76329" target="_blank">📅 18:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76323">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ULWYAwBY569mAq_CE9sgzH26yLpKWyiISPTAukeyPYx5wC7TrMcZmlUtnD9iyNvJkp2OZDsdO35DJ12MCs7Sg9LYW0VcO82V7PxInDUdAEBiPohZLKBZ1H_e4uet7-FqqAmUufUiIOU663qBUrmT1nue0dHIoLDyYJ-Sf6m9VtiaCO8A15LUvoZJwIjZYczZtUrbXS2i0joN2utuPw0SoYq2jbo099sUbKdP6k276al97lvnYqV0pGmypEha7uQIq-IlwF_l_-pykanrWDKlHCHIWA2x4TJGvj0iUIhqCQlzSrec_Y0zg1d4rCL1LwQSN_6o6S3ZKzkLPWuv8JISqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sr6DUKHWLk64S6D0Vilh48u270TLh5SqskUEQzgxm9F2Kseimd-4kJ64CiIcIzaApy1u8xgASBuFvMMDAD4EBBwSGvzVjEek8T_sUnyz5LtjzdPaTqKiqGotYmpxTXLhO-T9zQZ7Kpn4Z5Vj07cd87JJRorO5CnYXI_fCidvAzujBY46yYJ8GK68cSdR6POqothesxmvrsAcizJq32efk7NCu-GD0m90GNRyzCOz2W7m5e1f_bsSVuppEt4p8s64edVAXLbdiB38BZsTDeZ1zOvrfYdjnvYpyUQPUmQKdCM3xRbr-ASDJLw0eyLTnrIS3O_agWD4cFvghC0t7ml3iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ro7-QAgER87NRkAuLn5JY1eRKFh3IM1JYwBqt8_naa38-ico3U4k-VsXCv779DMCyVxImDwwYFvveeEeVXe722urvjP_acBOV-tvDFvCequB6ZkFstV2UVPSrEIZFERYj2IeMgb-hrvscZPq1aNBqQCg8iawRan-6z_taSvo4dSfLiOeNIOmhGOl6sXc9UBN6dKhknst3HcSZ9rsj_uRd4iCTwfHvdT6itJxQpaSOwVuLI9PSqAkD_blp9Eozmh9hMzD9F3hGVrCUuDiQBpquMx4UxN5lHuyZgbK7BJF3QPbrLoa94NXjd-0XNKcHDpl-79tWqOxEbX05pwJLVH5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fwje2nyzBRVDYwI2cF07re6E3hQFYaGPZF6Sg7qrJoRd7GW_fn0WPqovo717k40hIS5jnZMPWzWLSEwNp_cIdRcqujTi-C1jppaO_M5RWBCwkC_gs5norfIfoi013xh4PwuEErB256VHDz2FHybCYeFTy1mV5-rZrIxJZd_90zR7F-CXesoJ6oK3-xE0Nes9xSZY5as3yN2eUCBPr0sKOS9qAPEQ4U2HPko9th8xv-xhDbJV7jEYB2svCjKdiGxN0qgTb87jCpEcAOD4TNKta9jdqoSQKG_xQMMnAFgq5BBS7zg8E5CCgIyZeDb6J9UEvYRJKMBsppe38ox4SPuaOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50b9dacbb2.mp4?token=fPIJPt0JHFFAPlSw_vTgz8dhgna_1cYgmfalbyE9Ry0sW7RTUKj2xQ4BcIk6w6WhN-EnLhJ15e54vVZpKlnW-AAh4TO2GbBZSnfXtUznIY_VlALHNowXwLc9nV6v3wPt549iXcwYTaibC1fanyCu9etdJ3URkMgc2v6vZXiUhkiZW4I1ecenBqqgqKTfqS-L21hlOSJnYM3_MtNhA4P5t-ihH3X9UXN251Ah2rFgcv-PplO4hNG2N8ONUcRV5ILGpllkZAMfFgQAkoV3uJHOBjl6jAaCWvBjQ4hVR8BSPd5ToWUEGXNU4mlM5tFaYWM0ImqgYhbhSBk1k12k1wce7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50b9dacbb2.mp4?token=fPIJPt0JHFFAPlSw_vTgz8dhgna_1cYgmfalbyE9Ry0sW7RTUKj2xQ4BcIk6w6WhN-EnLhJ15e54vVZpKlnW-AAh4TO2GbBZSnfXtUznIY_VlALHNowXwLc9nV6v3wPt549iXcwYTaibC1fanyCu9etdJ3URkMgc2v6vZXiUhkiZW4I1ecenBqqgqKTfqS-L21hlOSJnYM3_MtNhA4P5t-ihH3X9UXN251Ah2rFgcv-PplO4hNG2N8ONUcRV5ILGpllkZAMfFgQAkoV3uJHOBjl6jAaCWvBjQ4hVR8BSPd5ToWUEGXNU4mlM5tFaYWM0ImqgYhbhSBk1k12k1wce7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر نخست‌وزیری اسرائیل روز یک‌شنبه، ۲۴ خردادماه، اعلام کرد که ارتش این کشور سایتی متعلق به گروه حزب‌الله در حومه جنوبی بیروت، محله ضاحیه، را هدف قرار داده است.
در بیانیه ارتش اسرائیل در همین باره اشاره شده است که به «اهدافی تروریستی متعلق به حزب‌الله» در ضاحیه حمله شده است.
اسرائیل دلیل این حمله را شلیک از طرف حزب‌الله به خاک اسرائیل عنوان کرد.
ساعتی پیشتر ارتش اسرائیل اعلام کرده بود که سه پهپاد روز یک‌شنبه به طور جداگانه به شمال اسرائیل پرتاب شده‌اند. اسرائیل گروه حزب‌الله را مسئول پرتاب این پهپادها اعلام کرد.
ارتش اسرائیل روز یک‌شنبه همچنین به ساکنان چندین روستای دیگر در جنوب لبنان هشدار داد که محل زندگی خود را ترک کنند.
خبرگزاری فرانسه به نقل از سخنگوی عرب‌زبان ارتش اسرائیل نوشت که ساکنان ۲۹ روستا در این منطقه باید به نقطه‌ای دیگر نقل مکان کنند. اسرائیل قصد حمله هوایی به این روستاها را دارد.
طبق این گزارش، اسرائیل صبح یک‌شنبه ابتدا به ساکنان ۱۳ روستا و سپس ساکنان ۱۶ روستای دیگر در جنوب لبنان اخطار داده است.
@
VahidHeadline
شبکه العربیه گزارش داد علی الحاج، از فرماندهان حزب‌الله، در حمله هوایی یکشنبه ۲۴ خرداد اسرائیل به ضاحیه بیروت کشته شده است.
دفاع مدنی لبنان نیز اعلام کرد در این حمله سه نفر کشته شدند.
العربیه همچنین گزارش داد ارتش اسرائیل یکشنبه سه حمله هوایی به شهر سجد در جنوب لبنان انجام داده است.
ارتش اسرائیل پیش‌تر اعلام کرده بود در واکنش به شلیک سه پهپاد از سوی حزب‌الله به شمال اسرائیل و آنچه نقض آتش‌بس از سوی این گروه خواند، یکی از مقرهای حزب‌الله را در ضاحیه بیروت هدف قرار داده است.
@
VahidOOnLine
خبرنگار آکسیوس، به نقل از مقام‌های اسرائیلی و آمریکایی گزارش داد اسرائیل اندکی پیش از حمله، فرماندهی مرکزی ارتش آمریکا (سنتکام) را از این عملیات مطلع کرده بود.
جمهوری اسلامی پیش‌تر هشدار داده بود هرگونه حمله اسرائیل به بیروت می‌تواند با واکنش تهران همراه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/76323" target="_blank">📅 17:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76322">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExdTuDV99tQ9B5zhnjOG2xr38FcTNgHoVvVATpgMOyGRnK7pTTp8dbf-n8tYXg3fCQ-Kx8vtAkqtviZtjNjP8DpdN_hlSzguQGLdP_4hgZxvSMIjeZfmmEg8Pt83NTtqpHn47pYmpDj24n_zoumuFnkGflujdkivKL-KAbsulAkwK1FR1aCskZYprNtBmpktbNELRFFJRR30mM4p1nwkcvUOUXpicrOVpmTcRc8e36K1vaZzwIlJkCnsNeUxZpSOyLYTPphimNoCV5vMs5S6R22WGJahG0NV3K_Q_z_EUGT7hWWcdtij0sAioDg3llDz3Rw5LqK21xdmwW8ubV4XTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یائیر لاپید، نخست‌وزیر سابق و از رهبران مخالف دولت اسرائیل، در شبکه ایکس با انتقاد شدید از بنیامین نتانیاهو امضای تفاهمنامه بین ایران و آمریکا را «تکان‌دهنده‌ترین شکست‌ سیاست خارجی و امنیتی اسرائیل» توصیف کرد و مسئولیت کامل آن را متوجه نخست‌وزیر دانست.
آقای لاپید نوشت امیدوار است که «گزارش‌ها درباره توافق با ایران درست نباشد» و به ۱۳ مورد اشاره کرد و آنها را ناکامی و کوتاهی‌های آقای نتانیاهو دانست از جمله اینکه:
«او یک روایت بیش از حد خوش‌بینانه را به آمریکایی‌ها فروخت، بدون اینکه نقشه خطرات را کاملا برایشان تشریح کند و در میانه جنگ اعتماد آنها را از دست داد.»
او همچنین نوشت که آقای نتانیاهو «نتوانست آمریکایی‌ها را متقاعد کند که تاسیسات نفتی و انرژی ایران را بمباران کنند» و «مسئله موشک‌های بالستیک را در توافق یا حتی در مذاکرات بگنجانند.»
آقای لاپید همچنین نوشت که نخست‌وزیر اسرائیل «برنامه مربوط به کردها را پیش برد بدون آنکه واکنش قابل پیش‌بینی ترکیه و نفوذ رجب طیب اردوغان در واشنگتن را در نظر بگیرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76322" target="_blank">📅 17:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76320">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XYDj9SYFBHYzIOi8hSKgvVN_TdbfmwZH75IdkNy69v2DJA692jmflhjI86lRczcAcms57Xe4ewfcKe5inixaibnLzAxGgi1rsco6yAuP_h3JltJLIz-etFRCKeUksfx4Oyg5QoCMlXiDir0VJE3sqBlA5LsWIAAfBZwL817D4GAAHT6FS7AfHB6u8zNdQ4ur6Y77SsR975J9i0Em1g_i-zMk4L6eXNLIRoHdC8xatTc155F_32jZX1dsYnWgPwQ9wxPwoF7P8muUCIAfcvM0Nf7JueZZQldWtxpn7dMN1UydN_9KhDw_3NEqVwhNKgFYLCQKTIeMMe7dyHJ6FgSpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t2elNya2GdgY3A8G8RneCJo58plnlkWmXiwAmI0xkAb-in2RIm7clCaZcCiGvneUsYote-VV889PbiXlaGJw8hKyAN9ekViJz9BSAvToKWwqiXdR_oHBUUMtrC6z9oVrNLgTSKewIDSME00iktdXtx2afP8e-309GKp2FzDarpiQwaxCertLFui6-usknS9WpRueJXzQ7_8inlzRqdd5aDOW8SQtT2h_4sKwP0UKiFBfaKD9g00w-zovEsoNy_GmioHmXcrDIu3ZtLz0kEk1W-Z9UHBmbZyxQ-OJkzsamIYrhBsB6X2vdVMEk2i-d9gWnFcVkxvMdP5MyUlIJp8Ldg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در حالی که خبرها از داخل ایران اشاره به ادامه بررسی متن تفاهم‌نامه و نامشخص بودن زمان امضای آن دارد، خبرگزاری رویترز روز یک‌شنبه نوشت که دولت دونالد ترامپ در تفاهم‌نامه با آزاد کردن ۲۵ میلیارد دلار از دارایی‌های مسدود ایران موافقت کرده است.
رویترز خبر خود را به نقل از «مقامی ارشد» در جمهوری اسلامی نوشته، اما به نام او اشاره نکرده است.
به گفته منبع رویترز، دولت آمریکا همچنین موافقت کرده است که اورانیوم بسیار غنی‌شده ایران در داخل کشور رقیق شود.
این‌ها دو مورد از بحث‌انگیزترین موضوعات در مذاکرات جاری میان ایران و آمریکا بوده است: ترامپ بارها بر لزوم گرفتن یا انتقال یا از بین بردن اورانیوم ۶۰ درصد غنی‌شده ایران تأکید کرده و همزمان بارها گفته است که پولی به ایران نخواهد داد.
مسئله دادن پول به حکومت ایران به‌ویژه برای دونالد ترامپ حساسیت‌برانگیز بوده است،‌ چرا که او خود سال‌هاست به باراک اوباما تاخته که چرا در جریان رسیدن به توافق موسوم به برجام با انتقال پول به تهران موافقت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76320" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76319">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdJFJ0IfTo_9SwbX6qLdIvUikVr_jz47PBk_YEj_K9h_rdkldqdWO7Go2AzicJiPzjOiA91qQUiFWU9FawGApk8RU8hByTVOOnEQcz4FKMz3N8F44pIye3Q3lVRqkYpfSCybd7JrOSV7TF1yN3Skalh8EFK-169_W0Y9QfLFw9uAV4i5uelNCj6VjMKZxNWwTnpSbFMkzrYAZ9oplPtL362D1pqLkUK7IRkU4XMzbQm_e193bBAOVUCIi-N8tFtjpqIzBi5d7IF_d-m-Gyy1UcnhrEBdoO_RFblEvug4evPGohShFkzWOTQhwALWONLB1k5Z2JpdzO4DfOgK16oY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع دیپلماتیک گزارش داد مذاکره‌کنندگان قطری پس از رایزنی با آمریکا راهی تهران شده‌اند تا با مقام‌های جمهوری اسلامی درباره کاهش اختلاف‌های باقی‌مانده و نهایی کردن تفاهم احتمالی میان تهران و واشنگتن گفت‌وگو کنند.
رسانه‌های ایران نیز گزارش دادند این هیئت قطری به تهران سفر کرده است.
این سفر در ادامه رفت‌وآمدهای دیپلماتیک قطر انجام می‌شود. چهارشنبه گذشته نیز مذاکره‌کنندگان قطری پس از مشورت با طرف آمریکایی به تهران رفتند و درباره متن احتمالی تفاهم با مقام‌های جمهوری اسلامی رایزنی کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/76319" target="_blank">📅 17:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76318">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3bec2d43bc.mp4?token=L4dcrqS8TbMszOzokI7vpdNgdtyeJQ-UnI-9z0hTnhgqxoiTIDou9IqEFnFsfvk-TMUGPVMMWODS22JyyVnWA39rDF6-ZVfcFsPslfCbsmckZQpq0GAUkrbEHUlny8Kfu8LA7j5WXUscoQociYIwmZFsN_phLx8jcJBL2_2-pp1dabVcgvc_tKVAuH6fqqbBe8Z33u1mvE4hVVZwCEOrauN145iDTNa01I86I_Yr3w3tKAsIu288_g_Pui29nv2Y9m5UozBgyjyC41-Raa7snnEJV5kZ4wwI9YVd9LyjSH0-RIoDHN5HyIeBYT9qSyihlPXOtmL91vFOjJ1O8vZECw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3bec2d43bc.mp4?token=L4dcrqS8TbMszOzokI7vpdNgdtyeJQ-UnI-9z0hTnhgqxoiTIDou9IqEFnFsfvk-TMUGPVMMWODS22JyyVnWA39rDF6-ZVfcFsPslfCbsmckZQpq0GAUkrbEHUlny8Kfu8LA7j5WXUscoQociYIwmZFsN_phLx8jcJBL2_2-pp1dabVcgvc_tKVAuH6fqqbBe8Z33u1mvE4hVVZwCEOrauN145iDTNa01I86I_Yr3w3tKAsIu288_g_Pui29nv2Y9m5UozBgyjyC41-Raa7snnEJV5kZ4wwI9YVd9LyjSH0-RIoDHN5HyIeBYT9qSyihlPXOtmL91vFOjJ1O8vZECw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: مقاومت باعث جنگ شد
[اینطور برداشت شده که داره میگه نپذیرفتن شرایط طرف مقابل در مذاکرات منجر به جنگ شد]
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران شنبه ۲۳ خرداد در شبکه خبر و در پاسخ به پرسشی درباره علت دو جنگ اخیر گفت: «مذاکرات علت جنگ نبود، مقاومت تیم دیپلماسی در مذاکرات علت جنگ بود.»
این گفته‌ها که در تعارض با موضع رسمی نظام جمهوری اسلامی و شخص علی  خامنه‌ای، رهبر پیشین جمهوری اسلامی به شمار می‌رود، با واکنش تند رسانه‌ها و سیاستمداران جریان اصولگرا مواجه شد.
علی خامنه‌ای، رهبر جمهوری اسلامی ماه‌ها قبل و پس از «جنگ ۱۲ روزه» گفته بود دشمن هر جا احساس کند که ما ضعیفیم، حمله می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/76318" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76317">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIkbOaALRRNY2YQiB0lgU_QbBgqpZGR99xi-eiHrIYP6e7pb10bkTjh6-Sw0c24U6zJbnfcBYL0E7D_fQmAn3e8RBJqwmdb49rc2XMdFkn3W6eb2IjdN-IbE0afIaPTAdy8x6YDGSoQseZWRRPPLik-THq2o4Q7kB1g_i49Lfq7nTImUtTBMxd0ki2duFFaIlWdkn8FN_osnKHnGhNMhJj98EWhTBk4_1dEe1HLXVWiwVj0WKWu8RpGgd0jOfcgrRE658IBPm9I94ZDV_ejDZHGSPMQfDbShjF_Jgei02VOYB6r_63nIKcT9eHaFIjaJS6a7tSyGddmp5ZCXx7fyMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی در اطلاعیه‌ای مدعی شد یک فرد متهم به تلاش برای نفوذ به مراکز داده، یک هسته چهار نفره در جنوب شرق کشور و ۱۲۶ نفر از آنچه «لیدرهای میدانی شبکه خرابکاری خیابانی» خواند، بازداشت شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76317" target="_blank">📅 17:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76316">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izQlqB_USyffVb64tsB7iSABEVue3YHCEwXp7binRROiVDJ1tIL3Cl_XLuElyT0LK26PQeLfj8EaPQaQtzinOusuCh8CXg3IROVej7S8puGm7Nf-bqlWYZgegrU9URRf1O8N5uYlQhKnJcsN24pk0RuhOOwYX9hZlngbOT36ovVu7a0T5Dzw-iQAmmdvPAowwJ1nYeSMPQrpKudjcFoGfM8bs3zQpiz0QxJ6lsIoLOq0dXvxklY9B-e7Nwf_h33X4q1xzFTW9NPAUrNpeOiGyuy-FIsMMlI4E5VgdT205hFjhZJFSTDRB4IQYoOGAsIZ73SqMkGEarXn9B4KXPEQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود طراوت‌روی، نازنین سالاری و مسعود احمدیان، وکلای دادگستری، به حبس و به عنوان مجازات تکمیلی به دو سال ممنوعیت خروج از کشور همراه با ابطال گذرنامه نیز محکوم شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76316" target="_blank">📅 17:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76315">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nO9d8B4gZvA38iXA2QO1pgVKVqGnhzLtXQCPUnb2LVeQHSPcDMJB3RsCpt4Ld110gqs_kMJAvMDOCMjylxTls6Teppv2DEoxxuE_Wo2szyLqjbSj25jzyivHMzxILLo8RI9tSg-qBghvhsUFUdftIDva847yhTzYGXaCZDk7XXSXahunnsYdRctYcIkyyJIMjw0N935Ruy83RCr7mnoNt2Ec1-RrLasiiIOFpWtR_cMWgZdR262LVOKrv3_AB9nOkRPyK66-rmQcpH1nG89i1cHrnf9q2UyiWE7fcuyrrYQ33drPghxwnEsigh_2QuL_fV66_H07ZagVjfMw30R_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماموران اطلاعاتی و نظامی جمهوری اسلامی در استان گلستان با یورش به منزل خانواده جاویدنام ابوالفضل میرآییز، اقدام به تفتیش خانه، طرح اتهامات بی‌اساس و تهدید اعضای خانواده او کرده‌اند.
طبق این گزارش‌ها، ماموران ضمن بازرسی کامل منزل، بخشی از وسایل شخصی خانواده را نیز با خود برده‌اند و آنان را به برخوردهای امنیتی تهدید کرده‌اند.
ابوالفضل میرآییز، ورزشکار ۳۴ ساله گرگانی، در جریان اعتراضات دی‌ماه با شلیک مستقیم ماموران حکومتی در خیابان‌های گرگان جان خود را از دست داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76315" target="_blank">📅 17:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76314">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
وحید جان ساعت۰۳:۳۲ صداهایی میاد از تو دریا
ما چند کیلومتر از اسکله سپاه طاهرویی فاصله داریم
سلام وحید انفجار های پی در پی از یک ربع پیش تو دریای شهرستان سیریک
صدا انفجار شدید اینجا شرق سیریک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 474K · <a href="https://t.me/VahidOnline/76314" target="_blank">📅 03:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76308">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/icFjer5coqxxAPAfWFVaHCNCZHOmpE-bE5vx1Br7s3CP_9BXCbX_wKUrfI--YWqKm1HlvbWuL_aajS1s5sPS0mEegYZoczFaymKpmsQI-vjxEUbu2ki92F4MEztKwcu4gBPCh8WtTxkC-C7sYAPTFv1TJLJXzOrKGejfIMohnheLHPigNHJOzj2JvKmkMK0WaXSdEI-MPsnAfWCl1ViwzvLwWzEF68z4G1r-sY42KKCpgkcHpCaB5EyD7JNouL2TF8mMlWCA7nghu1wJAm6ZrbakwJXUtKQSl7pUb2MBQE1mtMBzGahn_rK4_SI2rRhP8cvbHrVhghE7qc7ro4TBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d60822ba5.mp4?token=X0stLfHsejBfH2jINlFauWNujWPCU55wZGM1ee3F24wrUZeGcZ_rpJ5ySsz8JpT3qmeXeUvSsYikte_vripOUw1SEFzrioFEJ-Tg2XMKkdxAQYIktYYsiS5IaFXDsmcKF9XS2gon2eFOlsVPqOuhNzJSeS_koU-8F3T5EYS4J4mIGmyOI-RUKC9GzoOTT_5DCGzMpkzvb1azS2eyAQQNY7QC4N_9JeQWYX7hKvrLva8AeIXXlhFlsVXQeb1_jOuacltAMRgpG4DeOOH4iuHmDVyn5z-fJzOSrjYNBknC0zmXVDKP44u_433c31I4TlMm7L_uYDPQdhtGQfNgQVw2_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d60822ba5.mp4?token=X0stLfHsejBfH2jINlFauWNujWPCU55wZGM1ee3F24wrUZeGcZ_rpJ5ySsz8JpT3qmeXeUvSsYikte_vripOUw1SEFzrioFEJ-Tg2XMKkdxAQYIktYYsiS5IaFXDsmcKF9XS2gon2eFOlsVPqOuhNzJSeS_koU-8F3T5EYS4J4mIGmyOI-RUKC9GzoOTT_5DCGzMpkzvb1azS2eyAQQNY7QC4N_9JeQWYX7hKvrLva8AeIXXlhFlsVXQeb1_jOuacltAMRgpG4DeOOH4iuHmDVyn5z-fJzOSrjYNBknC0zmXVDKP44u_433c31I4TlMm7L_uYDPQdhtGQfNgQVw2_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف، عراقچی، پس حون رهبرم چی؟!
برخی رسانه‌های داخل ایران تصاویری از تجمع برخی طرفداران حکومت در شامگاه شنبه را منتشر کرده‌اند که در مخالفت با امضای توافق احتمالی با آمریکا علیه برخی مقام‌های جمهوری اسلامی شعار می‌دهند.
در یکی از این تجمعات که در میدان ابن سینا در تهران برپا شده، تجمع‌کنندگان علیه وزیر خارجه و رئیس مجلس شورای اسلامی شعارهایی مانند «عراقچی حیا کن مملکت رو رها کن» و «قالیباف، عراقچی / پس خون رهبرم چی؟» سر داده‌اند.
برخی رسانه‌های نزدیک به اصلاح‌طلبان این افراد را «نزدیکان به جبهه پایداری» معرفی کرده‌اند.
خبرگزاری دانشجو نیز عکس‌هایی از یک تجمع در مشهد منتشر کرده که در آن‌ها پلاکاردهایی در مخالفت با توافق و همچنین انتقاد تند از مذاکره‌کنندگان دیده می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 529K · <a href="https://t.me/VahidOnline/76308" target="_blank">📅 23:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76307">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبرگزاری فارس، رسانه وابسته به سپاه پاسداران:
اصرار عجیب ترامپ بر امضای تفاهم با ایران در روز یکشنبه و آزمونی برای تیم مذاکره‌کننده
🔹
ساعاتی پیش، دونالد ترامپ، رئیس‌جمهور آمریکا، بار دیگر تأکید کرد که «یادداشت تفاهم» با ایران روز یکشنبه امضا خواهد شد. این در حالی است که مسئولان مذاکره‌کننده ایرانی صراحتاً اعلام کرده بودند که تفاهم هنوز نهایی نشده و یکشنبه قطعاً انجام نمی‌شود.
🔹
نکته قابل تأمل، همزمانی یکشنبه با چهاردهم ژوئن، روز تولد ترامپ است. برخی ناظران احتمال می‌دهند او با این اصرار در پی آن است که از این مناسبت بهره‌برداری نمادین کرده و آن را به یک رویداد تبلیغاتی برای خود تبدیل کند.
🔹
اما با توجه به مواضع شفاف مقامات ایرانی مبنی بر نهایی نبودن توافق، به نظر می‌رسد مسئولان مذاکره‌کننده کشورمان متوجه این لایه‌های پنهان هستند و اجازه چنین مانور رسانه‌ای و تشریفاتی‌ای را نخواهند داد. از این زاویه، سرنوشت امضای یکشنبه نه فقط یک آزمون فنی برای محتوای تفاهم، بلکه آزمونی برای صداقت و ایستادگی مسئولان ایرانی در برابر فشارهای نمایشی نیز خواهد بود.
@
VahidOOnLine
وب‌سایت خبری اکسیوس به نقل از منابع آگاه نوشت که دلیل امضای ویدیویی توافق آمریکا و جمهوری اسلامی، «ملاحظات اجرایی و لجستیکی» و عدم امکان سفر جی‌دی‌ونس به پاکستان است.
اکسیوس نوشت که یکی از دلایل اصلی امضای ویدیویی توافق آمریکا و جمهوری اسلامی این است که ونس در صورت سفر برای امضای توافق، نمی‌توانست قبل از عزیمت ترامپ برای شرکت در اجلاس گروه ۷ در فرانسه در صبح دوشنبه به آمریکا بازگردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 485K · <a href="https://t.me/VahidOnline/76307" target="_blank">📅 22:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76306">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TVa7nzNNtf0O5BV-vljxBAiCyVXvcnunU6ZyCSPBTX6KGUqsgJm5v-EnQBgdEcZod6U3yvp5m5migFGzwNLPlIKUqx-1Uq2CnAPS7-agXTpaGwp_0-fDqThhAA69GT1nJTqpRtxq_CaXcXdFAEh58Nj_cQ74rodNM9Zgh1Us9_kUZYTdaVJ32VJDATnqxKGVflk3mYmbCy6L5dKVpYXfc4j3YHsGzAYI3-e31bx1FQoTmdwAo-QtTgNI17GZFIFLkq6Dgb3f1RuowqtUbZotcOFq7yFH6rC3h7gmgOXuH-ivXNpqTVqzBjt0fMnnFgPt3gn1nQvwLWSjbXOt3Pdc4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: قرار است توافق فردا امضا و بلافاصله تنگه هرمز باز شود
پست ترامپ، ترجمه ماشین:
توافق باراک حسین اوباما با ایران، یعنی برجام، مسیری آسان، زیبا و هموار به سوی سلاح هسته‌ای بود؛ سلاحی که ایران شش سال پیش می‌توانست به آن دست یابد و مدت‌ها پیش از حالا از آن استفاده می‌کرد. توافق من با ایران درست نقطه مقابل آن است:
دیوارِ جلوگیری از دستیابی به سلاح هسته‌ای!
در واقع، آن‌ها دیگر سلاح هسته‌ای نمی‌خواهند و چنین سلاحی هم نخواهند داشت؛ نه از طریق خرید، نه توسعه، و نه هیچ شکل دیگری از تهیه و تدارک.
قرار است این توافق فردا امضا شود و بلافاصله پس از امضا، تنگه هرمز به روی همه باز خواهد بود.
رابطه ما با ایران بسیار متفاوت و بهتر از رابطه‌ای است که دولت‌های پیشین داشته‌اند. برخلاف صدها میلیارد دلار پرداختی اوباما به آن‌ها، از جمله ۱.۷ میلیارد دلار پول نقدِ سبز و سرد،
هیچ پولی رد و بدل نخواهد شد.
در زمان مناسب، وقتی همه چیز آرام باشد، ما وارد خواهیم شد و «غبار هسته‌ای» را که در اعماق کوه‌های قدرتمندِ گرانیتیِ فرورفته زیر آفتاب دفن شده است ــ به لطف بمب‌افکن‌های زیبای B-2 ما و خلبانان درخشانشان ــ به دست خواهیم آورد و آن را
رقیق‌سازی و نابود خواهیم کرد؛ چه در ایران و چه در ایالات متحده.
ما مشتاق همکاری با ایران و سراسر خاورمیانه در آینده‌ای طولانی هستیم. امیدوارم این روند همگی سریع، آسان و روان پیش برود.
اگر چنین نشود، ما گزینه نهایی را در اختیار داریم؛ گزینه‌ای که امیدوارم هرگز دوباره به کار گرفته نشود!
از توجه شما به این موضوع سپاسگزارم!!!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 459K · <a href="https://t.me/VahidOnline/76306" target="_blank">📅 20:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76305">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شبکه الجزیره به نقل از سخنگوی وزارت خارجه پاکستان گزارش داد که مراسم «امضای الکترونیکی» توافق میان آمریکا و جمهوری اسلامی یکشنبه ۲۴ خرداد برگزار خواهد کرد. به گفته او، پاکستان میزبان این مراسم خواهد بود و مراسم از طریق «ارتباط ویدیویی و آنلاین» برگزار می‌شود.
او جزئیات بیشتری درباره شرکت‌کنندگان یا مفاد این توافق ارائه نکرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76305" target="_blank">📅 19:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76303">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VuHJMaIukiRBvWs0jzlCjmR1tEJu7rJgQxKZQTeNMoFDMClCUNLgopKwEmivaTYv0n4zG3FakJdYpMdysHSYlCr1bIW6Bn56JEdVJR43EfFOZv2wRwpyvCxBk9kIDyWSQDb5mJBlUMPcsnWnkgQKp9fUzriwyoPAWzzBKEy6mDEi7dKilQz4e8h2qM-cvRiEYcq7oWAzZINStJ-HQhlksGIoZ3dflJD9H9CRkwa_GHoTkTOzuYrnL-KRLfOEZT-xteuV3gGvlCIIT0Nr5Gdrgx55rFpEIPAdfU3jvKnMggCykc9dJV8Zvvb8CzUMhCNS5JQ9ej6fDsUmpdTDhxToOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c6Fza0h-3il_a1w8fxSsKgNIeGVw8iNMt-FYGL365zQAa_I4wnPteij_4xFAtvyIEo19bOwPZ90TeQ3cJKT08p8xbhPb6noVTPxtLm9JyHtkqbFtyrNlm--0e_r7OHMD2jnXNhdlEbRE33mBAIrhbeOOzwumEOn3JJZdFgU4qXZ3NfUOZGD_KWxuPVX6DRRF0yJoajXjs5PxSBhhL3iOB0CFKQ_OPonNylgHDjFIlf_hNMQBM0VOIB2BMffDKiYCP-SsSsQtWfXJdVFCqETlSuLeUT9qFSjjzhWRw9VN54w1ZNi0YiMa7JlKjSuzXxRVFWnDt5zAR7SxjDkcerPKoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام ارشد دولت آمریکا به رویترز گفت که دونالد ترامپ، رییس‌جمهوری آمریکا، در نشست گروه هفت با رهبران امارات متحده عربی و قطر و برخی دیگر از رهبران خاورمیانه دیدار خواهد کرد.
به گفته این مقام، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در دیدارهای ترامپ با رهبران خاورمیانه هفت حضور نخواهد داشت.
نشست رهبران هفت اقتصاد پیشرفته جهان، موسوم به «گروه هفت» ۲۵ تا ۲۷ خرداد در شهر اویان فرانسه برگزار خواهد شد.
@
VahidOOnLine
اسماعیل بقائی، سخنگوی وزارت خارجه جمهوری اسلامی، در نشست خبری گفت احتمال نهایی شدن یادداشت تفاهم میان تهران و واشینگتن در «روزهای آتی» بالا است.
او در پاسخ به پرسشی درباره احتمال سفر هیات مذاکره‌کننده جمهوری اسلامی به ژنو یا اسلام‌آباد در دو روز آینده برای نهایی کردن یادداشت تفاهم، گفت: «درباره زمان دقیق امضا باید منتظر بمانیم.»
بقائی افزود: «برنامه‌ای برای سفر به ژنو یا جایی دیگر ظرف یکی دو روز آینده نداریم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/76303" target="_blank">📅 19:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76300">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B6Ni1oMiMXQffjPWyv6p5Iw95YuD91sN2qznFThZGH7BidsXExG1OdMebpuAjXskCfR2ou75dGHyNQae5dW4UznBEorX5QCTxbM3sTCcVb5p2CHvSAsQ_GpNzHUnQwGUWyccUCfy3lO7bTfUX2jntcAdsBq31CH26jsy8Uiala43VRdF5V3JHzA30frKzyD8BEHSkO8FjY1de7psGgQ5fTdJ1hYtQQlK7M2SwGbdxmevBFDNaaRC3Pz98B9okOru7MaXR-Fn2khHJcxWVB78g3LMnc4sJQdKq5mT-M48Q5I6QVOSJE3sqzaHZ9HCGltIN9T6fMktVv6EJKtyFXrZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sHcIdME8pxdZWXBVEsPIg-Ql95lYdQGvFtX7RS-ksDzWulaQFjjDy9YpnavODglYMjkFoxreBpLFhznhgO1kB8RbU9GTidEcTOnfOwrzTSigaTR8ul2Z4_jB8xpMqS6pV3UFncrphyKqbmgT7EBkLRuG6iy2WVrd-hf9OSODUb4AXY0N0fgla-yoUaprYdhTZ7mEjPt8KzU20YDuT2Nt_44DLiWlkZ6xYC1pjJ5ozcC9oCMk_SWBX1Y65tRuf4AHMZJjyhnz70CwCkVut7EZ4nxaXEpzHdEf4xe9UwVDmIkwxgjzBJAysSSJztZlncEHqupnNn7NdV6AR5ay2CF9ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نخست‌وزیر پاکستان: تفاهم‌نامه ایران و آمریکا احتمالا تا ۲۴ ساعت آینده نهایی می‌شود
نخست‌وزیر پاکستان می‌گوید ایران و آمریکا بیش از هر زمانی به توافق صلح نزدیک‌تر شده‌اند.
شهباز شریف دقایقی پیش در پستی در شبکه ایکس نوشت که انتظار می‌رود تفاهم‌نامه ایران و آمریکا ظرف ۲۴ ساعت آینده نهایی شود.
او گفت که پاکستان در حال فراهم کردن تدارکات لازم برای «امضای الکترونیکی» این سند است و پس از آن هم «گفت‌و‌گوهای فنی» آغاز خواهد شد.
@
VahidHeadline
دونالد ترامپ، رییس‌جمهوری آمریکا، شنبه ۲۳ خرداد، در شبکه اجتماعی تروت سوشال، پستی از شهباز شریف، نخست‌وزیر پاکستان، را بازنشر کرد که در آن به احتمال دستیابی تهران و واشینگتن به یک تفاهم طی ۲۴ ساعت آینده اشاره شده بود.
ترامپ این اظهارات را بدون توضیح اضافی در تروت سوشال بازنشر کرد.
@
VahidOOnLine
اسماعیل بقایی، سخنگوی وزارت امور خارجه، روز شنبه ۲۳ خرداد با تشریح آخرین وضعیت مذاکرات اعلام کرد: «یادداشت تفاهم اسلام‌آباد که در حال پیگیری است، به طور مشخص بر خاتمه جنگ تمرکز دارد و در این مرحله تصمیم بر این شده که هیچ بحثی در مورد موضوع هسته‌ای صورت نگیرد.»
بقایی درباره گمانه‌زنی‌های مربوط به زمان امضای این سند گفت: «درباره زمان دقیق امضای تفاهم‌نامه باید منتظر بمانیم؛ اگرچه این رویداد فردا نخواهد بود، اما احتمال اینکه ظرف روزهای آتی رقم بخورد کاملا منتفی نیست.»
بقایی ایالات متحده را به «تزلزل و بی‌ثباتی در اظهارنظرها» متهم کرد و گفت: «به دلیل تزلزل و عدم ثبات طرف مقابل در اظهارنظرها، باید در هرگونه موضع‌گیری درباره این روند محتاط باشیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76300" target="_blank">📅 18:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76299">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYqRYy7-8zIrkkuLicNhSJPG7MNllCINP2yLoRGEkUFBCVjsNrp5IPpYfCSoSVQP47OwKd93mDnOddLMNj-HOFVl1VWd3ZAG1eEus_CI0wBgKTxEaQSZxu8HfdfpNUx-rT8bBHtkgZWOqV8a0GubwvtPEq7lW0gT7Kl4i5tEu1k8GC38AGOGxEww4-eckoL2YpYzVAt85VqRJQV38e45Da73onLnxhDOaZYqHEhg9z5DLlZ8UfZci6vtQx2gwRwlolF0IplfjCBuqwWD5I1a_SSWmRYpVzv6r81O4lxLGJj2MbaaQkvPrC96fQlfd3Wyj-mMdD2kmrc5p056kEmPuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز پژوهش‌های مجلس در تازه‌ترین گزارش خود درباره وضعیت شبکه برق کشور هشدار داده است که با وجود افزایش نسبی ظرفیت تولید، ناترازی برق در تابستان ۱۴۰۵ همچنان ادامه خواهد داشت و احتمال بروز خاموشی، به‌ویژه در ساعات شب، وجود دارد.
بر اساس برآورد دفتر مطالعات انرژی، صنعت و معدن این مرکز، در سناریوی واقع‌بینانه میزان کسری برق در اوج مصرف تابستان به حدود ۱۳ هزار و ۶۰۰ مگاوات خواهد رسید. در این برآورد، توان تأمین هم‌زمان شبکه حدود ۶۸ هزار و ۴۰۰ مگاوات و میزان تقاضا بیش از ۸۱ هزار مگاوات پیش‌بینی شده است.
@
VahidHeadline
پیام دریافتی:
امروز روستاهای خشکبیجار  از ساعت ۱۶:۴۵ حدود ۱ ساعت و ۱۵ دقیقه برق قطع شد. بعد از قطع برق تماس گرفتم با ۱۲۱ که گفتن قطعی ۲ ساعته کنترل مصرف هست که امروز صبح از رشت شروع شده و عصر به شهرستانهاش رسیده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76299" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76298">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LFsFKHI3yUnDLl7Do5aCPcwG5fUbPIT_EgCoW8vFtyXaDk5pyY2lxHRuyFvn4dEDUCRPmH4QtIG8O9jyVOkalEDCgGO_2SiQBUNAGx-1byZlSaqzhiZytPF7VWm03V4i1NLBiCjR0k9KXGgozrWkRQpKS9VtjmNxrb3AJDtVmShcFoDgNwuiQLSpwEGqpzM5LE1HGUgkIfAnGUskSDH4PtmoxWYUt32M8CHRMcuyFhq1cWIpMt7w593Fd8XIiNEWt59IKOf7ll5SjLxOcE_Giq9Rkr5dIZJDWi2130qdHGK4ykO4AtU7RpcvU_ceLsum25iUOvgyS6mOmmcQob1xYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه تلویزیونی سی‌ان‌ان در گزارشی اختصاصی که روز شنبه، ۲۳ خردادماه، منتشر شد می‌گوید که حکومت ایران در هفته‌های اخیر بر تلاش خود برای سخت‌تر کردن راه‌های دسترسی به اورانیوم غنی‌شده مدفون در سایت‌های بمباران‌شده‌اش افزوده است.
این گزارش به نقل از پنج منبع «آشنا با اطلاعات و ارزیابی‌های دولت ایالات متحده» نوشته شده، اما به نام و منصب آنها اشاره نکرده است.
سی‌ان‌ان در گزارش خود نوشته است که جمهوری اسلامی در هفته‌های اخیر این تونل‌های زیرزمینی را منفجر کرده و در ورودی آنها مین کار گذاشته است تا دسترسی به آنها را هر چه بیشتر دشوار سازد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76298" target="_blank">📅 17:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76297">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2iDL1Fxl9eHV2Y8pd-fSEvUDUKpiLhIZC2cJYxd7fRB9nhWZ1tYutb_D77yRY2LEJT9jTb2uHQ6Om8fCnrvKLKDXkJfiJ8XiBfLHNq5Nl0bh0rq6N7sL-XErop8RS2_1efPxcZ1au0-Cc_yamD52HuJQZjRH6w3l7uqIiTKeFGRDr6mW1k1PbogRcpGaDlv0YDYu0CYjOYwuS0tmZ0p92igIHjCfA7OxNe9-BCAFMxm4GDR7-V4YyTzb3WXx6FOu3lGjV-1ZeEbZt5sNxDioBQ5QcblHA4q8ZbidkUJLvNOjVbNZtjN7Yn5rCuxJNU09M-Ldbfglbh-56AjixzQSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها و مقام‌های ایرانی روز شنبه خبر دادند که خدمات چند بانک ایرانی به شکل همزمان دچار مشکل شده و این اختلال تا بعدازظهر همچنان ادامه دارد.
خبرگزاری ایسنا اعلام کرد که «بانک‌های ملی، تجارت، صادرات و پاسارگاد» از جمله بانک‌هایی بودند که همراه‌بانک و دستگاه‌های خودپرداز آنها مختل شده است.
خبرگزاری فارس در این‌باره نوشت بانک «توسعه صادرات» نیز اختلال مشابهی دارد و افزود که «برخی منابع از احتمال وقوع حمله سایبری خبر داده‌اند، اما تاکنون هیچ مقام رسمی این موضوع را تأیید یا رد نکرده است».
ساعتی بعد علیرضا قیطاسی، دبیر شورای هماهنگی بانک‌های دولتی در گفت‌وگو با صداوسیما بدون اشاره به جزئیات درباره دلایل این اتفاق گفت: «رفع اختلال از خدمات بانک‌های ملی، صادرات، تجارت و توسعه صادرات در دست انجام است.»
حملات به شبکه بانکی ایران در سال‌های اخیر سابقه دارد و بارها اطلاعات مشتریان بانک‌های مختلف ایران هدف رخنهٔ سایبری قرار گرفته و در فضای مجازی و اینترنت خرید و فروش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76297" target="_blank">📅 17:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76296">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v28KotSUSBzENngRVdlCU1IXOwdgsU_AeFgM-1GZGEU8MrLnXb938BN0mW3jJ-LGEuLetyDZnOELhqLa2apMA115Ci55oEZc3uSM1JYtGwJP9HBKtZjTvNET2Nx51RHvTu7-WRqO4UnhWCNwcofWLadmPgUPU7XzlASV3CCNcZS1x0pYQ7OVTgSU8_7n9nO7ZXdF2mlJeVqkhUhadQx2R6iSimykFTUEbdOgkd5TL9EtYh-g8IoWX-VdgQ5GV2Tie3RXEAJylGNTNeyDPbUWPRSWcKvaLxOoO3hO8fxl9y_pjIhP_E_NVkiuJxH5yn56olBOR94Gf6VDb7GjJK7JoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش تازه «پروژه شفافیت فناوری» نشان می‌دهد یوتیوب میزبان ۸۴ کانال مرتبط با افراد و نهادهایی بوده که در فهرست تحریم‌های آمریکا قرار دارند؛ بخشی از آن‌ها همچنان از طریق نمایش تبلیغات در این پلتفرم درآمدزایی می‌کرده‌اند.
بر اساس این گزارش، ۵۶ کانال به اشخاص و اتباع تحریم‌شده در فهرست SDN و ۲۸ کانال دیگر به نهادهای دولتی و رسمی مرتبط بوده‌اند. در میان نمونه‌های شناسایی‌شده، نام‌هایی از نهادها و رسانه‌ها و همچنین برخی کسب‌وکارها و افراد قرار دارد.
پس از انتشار نتایج این گزارش، شرکت گوگل ۶۳ کانال را ظرف چند ساعت حذف کرده است. گوگل اعلام کرده که به قوانین تحریمی آمریکا پایبند است و اقدامات لازم برای اجرای مقررات را انجام می‌دهد.
در فهرست منتشر شده از کانال‌های شناسایی‌شده، نام‌هایی مانند نو‌بیتکس، و‌الکس، بیت‌پین، رمزینکس، گروه بهمن، ماهان ایر، فارس‌نیوز، پرس‌تی‌وی، ایرنا، بانک پاسارگاد، دانشگاه المصطفی و همچنین برخی چهره‌ها و کانال‌های سیاسی و رسانه‌ای دیده می‌شود. مانند علی‌اکبر ولایتی، امیرحسین ثابتی، بابک زنجانی و مسعود پزشکیان.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76296" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76295">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJgOj5z-7a3G0koYj1DDz4Cqx2kY7BrFPQFifp8Nmn6rD9z4wLpex-vANYkFM5uEDnw8nCuJftq-TQTwpnWQttInyr8NBH8V89_fV2vlPtX5u2OzKWG3PsM8mZDfXtdiNElChpPRGVwI1lP4q94yFj_90DOStiKWKlKbyYGLmL2AiBiOzpp9UIl2jfeI25oJ76dSPka79xQwBtg0FpBJTVpw6sAi2pyDvXS8DVNN2h0GuUenQJHZ4mmoIsacPa6JlnTJ9nR1oprQoNzHKpNR6fid5ud25gdiCWJ5-FPr64NDlihX_P_T3QZyiqzsNrFLe3IfwnSOIxN7GWlny686ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور کنترل صادرات با استناد به نگرانی‌‌های مرتبط با امنیت ملی، دسترسی «اتباع خارجی» را، چه در داخل و چه خارج از آمریکا، ممنوع کرده است.
شرکت آنتروپیک، سازنده دستیار هوش مصنوعی «کلود» (Claude)، جمعه ۲۲ خرداد اعلام کرد به دنبال دریافت یک دستور کنترل صادرات از دولت آمریکا، دسترسی به دو مدل پیشرفته خود، «فِیبل ۵» (Fable 5) و «مایتوس ۵» (Mythos 5)، را «برای همه کاربران» قطع کرده است.
این دستور با استناد به «اختیارات امنیت ملی» صادر شده و دسترسی هر «تبعه خارجی» را، چه داخل و چه خارج از خاک آمریکا و حتی کارکنان خارجی‌تبار خود آنتروپیک، ممنوع می‌کند.
آنتروپیک گفت این دستور را ساعت ۵:۲۱ بعدازظهر به وقت شرق آمریکا دریافت کرده است. از آنجا که شرکت نمی‌تواند به‌صورت لحظه‌ای کاربران خارجی را از دیگران جدا کند، ناچار شده هر دو مدل را برای تمام مشتریان غیرفعال کند.
دسترسی به سایر مدل‌های این شرکت، از جمله Opus، بدون تغییر باقی مانده است.
بنا بر گزارش اکسیوس و وال‌استریت ژورنال، نامه این دستور را هاوارد لاتنیک، وزیر بازرگانی آمریکا، خطاب به داریو آمودی، مدیرعامل آنتروپیک، فرستاده و با همکاری اداره صنعت و امنیت این وزارتخانه، تنظیم شده است.
متن نامه جزییات دقیق نگرانی امنیتی را مشخص نکرده، اما به گفته یک مقام دولتی، واشینگتن پس از آن که شرکتی دیگر مدعی شد توانسته سازوکارهای ایمنی مایتوس را دور بزند («جیلبریک» کند)، نگران خطرهای امنیت ملی شده است.
همان مقام افزود دولت پیش‌تر کوشیده بود آنتروپیک را به تعویق عرضه این مدل‌ها متقاعد کند و پس از ناکامی، نامه «کنترل صادرات» را صادر کرد.
آنتروپیک با این تصمیم مخالفت کرده، اما گفته است از آن تبعیت می‌کند.
به گفته این شرکت، روش افشاشده یک «جیلبریک محدود» است؛ در عمل یعنی درخواست از مدل برای خواندن یک کد و رفع ایرادهای آن؛ آسیب‌پذیری‌هایی جزیی و از پیش‌شناخته‌شده که مدل‌های عمومی دیگر، از جمله GPT-5.5 شرکت OpenAI، نیز قادر به یافتنشان هستند.
آنتروپیک تاکید کرد فِیبل ۵ با تدابیر حفاظتی‌ای به‌مراتب قوی‌تر از هر مدل پیشین عرضه شده و پیش از انتشار، هزاران ساعت با همکاری دولت آمریکا، موسسه ایمنی هوش مصنوعی بریتانیا و گروه‌های مستقل آزموده شده است.
این شرکت ممانعت از دسترسی برای یک مدل تجاری در دسترس صدها میلیون کاربر را به‌خاطر یک آسیب‌پذیری محدود «نامتناسب» خواند و هشدار داد اگر چنین معیاری به کل صنعت تعمیم یابد، عملا عرضه هر مدل پیشرفته‌ای متوقف خواهد شد.
این دستور، تنها سه روز پس از رونمایی فِیبل ۵ و مایتوس ۵ صادر شد. مدل‌هایی که آنتروپیک آن‌ها را قدرتمندترین سامانه‌های خود معرفی کرده بود. هر دو بر یک بنیان فنی ساخته شده‌اند، اما تنها فِیبل ۵ با محدودیت‌های سخت‌گیرانه، به‌ویژه در حوزه‌های امنیت سایبری و زیست‌شناسی، برای عموم منتشر شد؛ مایتوس ۵ بدون این محدودیت‌ها و تنها در اختیار شماری از شرکای مورد اعتماد، از جمله شرکت‌های امنیت سایبری و زیرساخت، قرار گرفت.
این دو ادامه «مایتوس پریویو» هستند. مدلی که بهار امسال با توانایی‌های پیشرفته سایبری توجه وال‌استریت و مقام‌های دولتی را جلب کرد و در چارچوب طرحی به نام «گلَس‌وینگ» میان گروهی محدود توزیع شد.
اما اهمیت این ماجرا فراتر از یک مدل و یک شرکت است: این نخستین بار است که واشینگتن از اهرم کنترل صادرات در مورد یک مدل تجاری پیشرفته استفاده می‌کند. این وضعیت نشان می‌دهد سرنوشت یک مدل را می‌توان نه با تصمیم سازنده، بلکه با دستور دولت رقم زد.
چارچوب «ملیت‌محور» این محدودیت نیز کاربران و شرکت‌های غیرآمریکایی را مستقیم هدف می‌گیرد.
آنتروپیک می‌گوید توقف عرضه‌های ناایمن توسط دولت را می‌پذیرد، اما در چارچوب فرایندی قانونی، شفاف و مبتنی بر واقعیت‌های فنی. اقدامی که به گفته این شرکت با چنین معیارهایی نخوانده است.
آنتروپیک این ماجرا را «سوءتفاهم» خوانده و گفته است طی ۲۴ ساعت آینده جزییات فنی بیشتری منتشر می‌کند و در تلاش برای بازگرداندن دسترسی است، هرچند زمان مشخصی برای آن اعلام نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/76295" target="_blank">📅 17:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76293">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HDugDasUBYRYyMZ4VtZx5-VKX9782BWaa06v1RzpN6956WNXi-NEy8LP9NPZLDsEko5Ha6vyL194rWM_vNPBevcb7TKUexcux8fuw3MmiXuVSgX7h8MJk38OyU29WzOIXzJ2a0rDX04TiE5iE4jaGMvMqUigSMUZM14n23eOD7dQLRyxoLFWnbGn76n-5CbDbqzkQYk5gvff9jObJgAwRJTg7nJzTwAzTPU0AoNg8icooI0rFjLEcBWflDzj_FST4HGStFtjiqdnVvusw1jPmmF635UUn6-EljArht52zFCJy51FfunF2RayjMdeL3fat3Y1-whKE0WMbggilVKF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a13lR_VKqfoctXdDnxv83av1TMYpdDoQvBsJeKkDtZqi1ZoA99pUCNQ0TO8vqq0dDzwt_kI4YNyXqUa-MvhbjAz9aEAOZnHGiR5t59xlc11-0PnvQ1XBd_BrNmUFU2vHVxEJoz6BL0YH1SzKRKLv1KPtMVh0d63x8q_l8zKSzCq1QxwLJkROBgxzuxAG4ZhA7ugTjcdbqetOezyE3JxBokasqR5aIC5X7JBS253KfoFIy_AUARWQw2SBrvkDFAbVX4oZk7ypIQsi389XmBtsBAh9vtUTpha_DVbN5RfpH78R8TpQQYlNuaZofEtN-S5wYUwCU88WEJpFN66pWUB7_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری رسمی لبنان روز شنبه ۲۳ خرداد خبر داد که ساعتی پس از صدور هشدار به مردم ساکن جنوب لبنان، ارتش اسرائیل به چند نقطه در این منطقه حمله هوایی کرده است.
ارتش اسرائیل روز شنبه صبح به ساکنان ۲۰ نقطه در جنوب لبنان از جمله شهر نبطیه هشدار داد که باید محل سکونت خود را ترک کرده و به شمال رود لیتانی بروند.
ارتش اسرائیل اعلام کرد این هشدار در پی نقض آتش‌بس از سوی حزب‌الله لبنان، صادر شده است
.
حال خبرگزاری ملی لبنان می‌گوید که هواپیماهای جنگنده اسرائیل چند نقطه از جمله دو روستای سجود و ریحان را در نزدیکی شهر نبطیه بمباران کرده‌اند.
اسرائیل در ماه گذشته میلادی تمام مناطق در جنوب رود لیتانی را «منطقه جنگی» اعلام کرد و از آن زمان این نقاط را بمباران کرده است.
اوایل ماه مارس یعنی تنها یکی دو هفته پس از حمله مشترک آمریکا و اسرائیل به خاک ایران،‌ گروه حزب‌الله در حمایت از جمهوری اسلامی به اسرائیل حمله کرد، حمله‌ای که بلافاصله پاسخ ارتش اسرائیل را به دنبال داشت.
درگیری این دو هنوز ادامه دارد و حتی پس از برقراری آتش‌بس حدود دو ماه پیش، هم ادامه یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/76293" target="_blank">📅 17:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76292">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBwZH_4Spn6Hy4oA0BfIFGbTS_ixAHkGpneJNeI55MBChlyh1qU1COhab95r4FQsRvsN8ByyP0mremnkp_Gz2aWsZxTb3b1ZwWPngSB7NnjHEvP8Nm9cKXrYUuHfgB6MvShIASDkRUUYfedDDTad1Ys50zt9ZToHHVHf9ddakUO9Juf2b0WlLs1P5LNo0djl7n5wj7JnKMxqiG6V9cxmaJywO4tf8JF0kD0PzTi41iaftMS7m13YIG9xRvHjdMqyzsa20HDZeKBSnidG0EMQEnuCe_6GeAsMwZqXifVrfFVvoouijtOXM_nDapyDw9urLcJz4wo-wJVrPYcBhCGKDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر حفظ و نشر آثار علی خامنه‌ای با انتشار اطلاعیه شماره ۳ ستاد بزرگداشت «عروج خونین» او، جزئیات مراسم وداع، تشییع و تدفین دومین رهبر جمهوری اسلامی را اعلام کرد؛ مراسمی که قرار است حدود ۱۲۹ روز پس از کشته شدن او در ۹ اسفند ۱۴۰۴ برگزار شود.
بر اساس این اطلاعیه، مراسم وداع با پیکر علی خامنه‌ای و اعضای خانواده‌اش روزهای ۱۳ و ۱۴ تیرماه در مصلای تهران برگزار خواهد شد. تشییع پیکر او روز ۱۵ تیر در تهران، ۱۶ تیر در قم و در نهایت ۱۸ تیرماه، همزمان با شب شهادت چهارمین پیشوای شیعیان، در مشهد برگزار می‌شود و پیکر او در حرم هشتمین پیشوای شیعیان به خاک سپرده خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76292" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76290">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWebwk758ziQjpmoc6hqukceO88WfrN7eFVchJ3h8Xbmy1SB0cziOro0DvY9NzOiFFnwUSBG7aQZAhjYiH1WeNqS12ZCdTIhXgkeo6wI74auJuOa3ndS8N1glXC3jL96hHdDgVzaD8J35VZv7vzCe_EyRyhGTHvrwcgRSdX0ktcCmTx1tYWKyAu7IpGb9NmOgyTwa5AC4gobqOaL496zMsaaGlkXMuKMlYE32wWHr0hxA9wsxsEPPQIIcbyJgeXmA7Kd48J-AmBG4qJW8vrjBj7SdR43kqsnvce4QcSB3X0wykVCBhjHcrdMA5BDpP6v0xzBNwBElomMq64Zae6EhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سید آرمان موسوی» ۲۹ ساله، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ در محله مسکن شهر کرمانشاه هدف شلیک مستقیم قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله جنگی به ناحیه قلب او اصابت کرده بود و در اثر شدت جراحات جان باخت. پیکر سید آرمان موسوی روز شنبه ۲۰ دی‌ماه در کرمانشاه به خاک سپرده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76290" target="_blank">📅 17:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76289">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLLe1HLAb6AGIcH_lJZNPwmAcjArKm2YgXLnzbyvdn4BidqMh6DSzu7b0d_1-InBi0F5KfQR9IwY3TZUuze8VXdkM1l93gIsjK7wo31WUKVKKRCIAoIFzo07HM6zYEWS32zzBuRIaCCqXNqJG7UspXEELIBIWloBivN4w-XtozwQxFJNFdtmwZI37suia_OMNqfzF679hbQLFQZx8dVG7fQQSJzkvbcP7A84rFFiW1EpdQZwqG4qoifeYIRTSWRJWbkX9xvcLy5Ifkeu5q9FxUn5aTTgkr-3r9CZKit8hXmREi_eN8Of9LgDGfoMUs7IiHzhBp08DGfpkKjZeGaImw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، در گفتگوی با «فاکس‌نیوز» اعلام کرد که با توجه به روند پیشرفت مذاکرات، انتظار می‌رود توافق صلح با ایران «احتمالا تا پایان همین هفته یا روز دوشنبه نهایی شود».
بسنت با اشاره به اینکه تصمیمات دونالد ترامپ برای جلوگیری از دستیابی تهران به سلاح هسته‌ای، هزینه‌ها و فشارهای کوتاه‌مدتی را به بازار سوخت و اقتصاد خانواده‌های آمریکایی وارد کرد، افزود: «ما درک می‌کنیم که در ماه‌های اخیر شرایط سختی سپری شد و افزایش بهای انرژی بخش زیادی از رشد دستمزدها را بلعید، اما ما در حال عبور از این وضعیت بحرانی هستیم.»
وزیر خزانه‌داری آمریکا با تاکید بر اینکه زیرساخت‌های اقتصادی کشور در حال حاضر بسیار قدرتمند عمل می‌کنند و بازار انرژی به خوبی تامین شده است، خاطرنشان کرد که با حل‌وفصل این مناقشه و مهار تورم، بهای جهانی نفت حدود ۲۵ تا ۳۰ درصد و قیمت بنزین در بازار داخلی بیش از ۱۰ درصد از اوج خود کاهش یافته و روند نزولی قیمت‌ها و کاهش هزینه‌های زندگی مردم با قدرت ادامه خواهد یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/76289" target="_blank">📅 06:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76288">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4Uw4-cZOk-TfR6xW2BYjYh0hYpUt9lTlO_P427Ve1SuH_LLzY50viWtmDd-gJ8Cko1G6_nFD2d7r2lZzYS6pbR9XBu5WwZcgOOkxVMkhZuFujqFL9PgImqHqKPNpW6TnV8cUHDME1R41Yz4ig5bDrk1sQmBCpkOC4wKzOmMnRBYb71GYp6oZQHFaiZTemx3CmKo8vI-azAhScecIqwWmRvK7puHGxfVrmHfCJ02_CTBV6mob4Ufe1okSuWgoWW0i52j_hR3fpxZfVkrCp55zns_b9Gc46sWKTqE-jxcizEKb8kQbH-UZ7y_0gXCRKgv5Zu3Iknpkb1W0aBhVlU9Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
فرماندهی مرکزی ارتش آمریکا (سنتکام) اعلام کرد که ایران چند پهپاد انتحاری را با هدف حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورده است.
سنتکام در شبکه ایکس نوشت که نیروهای آمریکایی در ساعات اخیر همه این پهپادها را سرنگون کرده‌اند و تردد کشتی‌ها در تنگه هرمز بدون اختلال ادامه دارد.
در این پیام آمده است: «ایران چند پهپاد انتحاری را در تلاش برای هدف قرار دادن کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورد. نیروهای آمریکایی در ساعات اخیر همه آنها را سرنگون کرده‌اند و جریان تردد در تنگه بدون مانع ادامه دارد. این گذرگاه مهم تجارت بین‌المللی همچنان برای عبور و مرور باز است.»
پیش‌تر نیز یک منبع آگاه به رویترز گفته بود نیروهای آمریکایی چند پهپاد ایرانی را که به سمت تنگه هرمز در حرکت بودند سرنگون کرده‌اند. این منبع گفته بود پهپادها تهدیدی برای کشتیرانی تجاری به شمار می‌رفتند.
این رویداد در حالی است که تهران و واشنگتن همزمان از پیشرفت در مذاکرات برای دستیابی به توافقی جهت پایان دادن به درگیری‌ها سخن می‌گویند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76288" target="_blank">📅 06:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76287">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kTDfZ33VEhF9FxvNad3A2e_MtuQYZYwx_2ZjmvVqIyByq24dXactgm1nv4TqO8579tPETP8IcKvI5EXnIn0bzdtGYXsFvgHTyjj3C19E41rLe7b5xyUJOEz5Bp66YCeAUSjNz32-eKfhzCtNSJRV8ciROV3nVqWCGODRkGNwGoOq5tYjUv6t-M78h13fRAMRdoYSjMLGLYCi1jWe41tYFbouWMphZOHbPYku_Q66Glx1zazuBUZFPVilc4PvzKB-QTpmHNz6JQW4o-GIDvMV04Al8X0l2UjNCGuD4dfnhSrg2YAmjoYUmAdC3lmDYXrjrcw-DFVvx2SdY2gPy8FGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه امارات متحده عربی گزارش‌های منتشرشده در برخی رسانه‌های بین‌المللی درباره انتقال یا آزادسازی منابع مالی برای ایران را قاطعانه تکذیب کرد.
این وزارتخانه در بیانیه‌ای در شبکه اجتماعی ایکس اعلام کرد که ادعاهای مطرح‌شده درباره انتقال مبالغ مالی از امارات به جمهوری اسلامی ایران، از جمله گزارش‌هایی درباره انتقال ۳ میلیارد دلار، «نادرست» است و هیچ مبنای واقعی ندارد.
پیشتر
رویترز به نقل از چهار منبع آگاه گزارش داد که امارات متحده عربی با آزادسازی میلیاردها دلار برای ایران موافقت کرده و بخشی از این منابع مالی نیز در اختیار تهران قرار گرفته است.
اما وزارت خارجه امارات تاکید کرد که هیچ‌گونه دارایی یا منابع مالی ایران از طریق این کشور آزاد یا منتقل نشده است.
@
VahidOnline
بیانیه امارات، ترجمه ماشین:
امارات متحده عربی گزارش‌هایی را که از سوی برخی رسانه‌های بین‌المللی منتشر شده و مدعی انتقال پول از امارات به جمهوری اسلامی ایران هستند، از جمله ادعاهایی درباره مبلغ ۳ میلیارد دلار، قاطعانه تکذیب کرده است.
وزارت امور خارجه در بیانیه‌ای تأکید کرد که این ادعاها کاملاً نادرست و بی‌اساس هستند و تصریح کرد که هیچ‌گونه دارایی مسدودشده ایران از طریق امارات آزاد، منتقل یا تسهیل نشده است.
این وزارتخانه همچنین از رسانه‌ها خواست دقت را رعایت کنند، به منابع رسمی اتکا کنند و از انتشار یا بازنشر اطلاعات تأییدنشده و ادعاهای بی‌اساس خودداری کنند.
mofauae
درباره این خبر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76287" target="_blank">📅 01:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76285">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mLXEyGEOiKyNapJihQZH-IqANE43Ow-xtm8d0YMeHEGOrkIWKqRnLWb1zpozub-Hyp9m4Vn_lQNogtMvDV7cFcv-QXPdSaGzN9s1K_30ID_hVIr1eAD_8BPKQ1W7phsXEpjXkJ4mkWCbdfB7QC62JRc8mzpU4D7wOL72BPJUJmVJ3oaZf-EBNdzfSUkG8yq76FfJMNVhLZw_KFQEBWGonS-DZjC5zkhm9QZc9hq8Pxix5e-8Iy9l1IImwNDLyC4uhF4Z3tW8iNepLDi5CTH2ZIULFxwVE3HKoKqJnJ844Vy_o7oLWbw0YX_-2g4YjPkLQFxakcuVYLSOQvf-0gsR_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OmWStZZLQ-Oz7n-AtjxuFL7BICkNX4146FwYLLbE0c36yb4NlqKn0rY4vkMv-1q_KvsY-UZanEiEO_dsrDmCpM2w47L6S9f_tn1j5TjeLT2KEAuilNbYO0VvxYEslo93TuH9_ISPKW3UqtbOnF1M3kxJTCKd9bWg7VJshGbq-VJg7A8NG0-SkePMggr2W9OkGYq1mbsnG-cHniP6X7OVuaslTjtgY6YZZaQ-ZCFCtzpno5zcGdh_3cPUSyfbfsU2SgOMiUbVPysHRCbYa6aCYa3pk1n2YCGDDGoA1Ap6I4-AjysnsbWirsHzkHAZmy7roKMMCXscwEX3jDqpz6dyog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مالک شریعتی نیاسر، دیگر عضو مجلس شورای اسلامی نوشته:
خب وقتی در باز بشه و ببینن که می‌فهمن مویوم...
malekshariati
این طور برداشت شده که داره میگه قالیباف پشت همه تصمیماتی است که به اسم مجتبی اعلام میشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76285" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76284">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wt95zEAE13HuoQ73tsDbEtMEKW_NuCXblsqkGhrabspsMybMFRc2ATi1d6FNRtC5TBcP2vdHHwXCrmPQBzpuZ14tvXZ7a0aHKYkvb5Z4Ri2hyx85BbP2cBK89RQU9GhXXpY9swh_OvdBcSTXg14uE3fcseAkSFvfmgvXL_k1GLI1XiG1QqMKrNiPraKXGPxg6RgQbneiu7kEBF1H2yp_1-ALs-xp2Qg_q0SDveYduDhapME04EI0ODrgkZ_fl9148YFl0V9dg4gWZtk3O9n7rDBkeBopzTYHFigmu4Fnb3xqM4D31RkQXb8cbf0ifDKPxEp38-ILC6X24JLIFp2wzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم:
استانداری هرمزگان: صدای انفجار در حوالی بندر سیریک ناشی از شلیک هشدار در تنگه هرمز است
خبرگزاری فارس:
شلیک هشدار به کشتی‌های متخلف در تنگۀ هرمز
دقایقی پیش مردم در قشم، جاسک و سیریک در استان هرمزگان شنیدن صدایی شبیه انفجار گزارش کردند؛ گزارشی از اصابت در این نقاط مخابره نشده است.
به گزارش خبرگزاری فارس از بندرعباس، منابع محلی از شنیده شدن صدای انفجار در سه نقطه از هرمزگان خبر می‌دهند.
دقایقی پیش اهالی مسن قشم، مناطقی از سیریک و همینطور جاسک از شنیده شدن صدای انفجارهایی خبر می‌دهند.
بررسی‌های خبرنگار فارس از منابع آگاه حاکی است صداهای شنیده شده مربوط به انجام شلیک هشدار به کشتی‌های متخلف در محدوده تنگه هرمز است.
منابع استانی نیز وقوع انفجار بر اثر اصابت در این ۳ نقطه را رد می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76284" target="_blank">📅 00:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76283">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t4JfIglG-FSEGITcxGIstgbqP9PzblP7rVYloyyMOUe2D0YIYrXBgqZ5lrh-cIcyz5dSDNqMtdBXgSF6ltz8DPKYpMrKKoXebbp9qwZYZQuy47dzjOrouJxBhlICUJv9s205ud1jDpeEYLwKpY1GmhR1EHt14VcAgFZjK61Xltu7dCRCLXcuvsFo3z0iURxdvb7kJskbBGPQNuv_WhVXSuO831LsnJDRqU2uv30CDjUuhtGpofqYkg4HNAr2F17C3i_uqQzBZM_U3LinajiP6WTI-S-7xsyxPzW6-n_3XkYrUvwxw4OagZoHPmTr9PsUwik1i_1PR0eRMP81FGbbVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، درباره تفاهم با آمریکا به صداوسیما گفت: «احتمالا در چند روز آینده تفاهم‌نامه میان ما و آمریکا امضا خواهد شد.»
او افزود: «امضای یادداشت تفاهم بعد از گذشتن از آخرین مراحل مذاکرات به صورت دیجیتالی و از راه دور انجام می‌شود که اعلام خواهد شد.»
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، شامگاه جمعه در یک برنامه زنده تلویزیونی اعلام کرد هنوز توافقی با آمریکا امضا نشده و مدعی شد که پرونده هسته‌ای ایران به مرحله دوم و نهایی این توافق موکول شده است.
او در گفت‌وگو با تلویزیون حکومتی ایران گفت توافق احتمالی با ایالات متحده شامل دو مرحله است و «موضوع هسته‌ای را به مرحله دوم انتقال دادیم».
این در حالی است که ساعتی قبل یک مقام ارشد آمریکایی به خبرنگاران گفت بر اساس توافق، قرار است اورانیوم غنی‌شده ایران در خاک این کشور نابود شود و سپس به خارج از ایران منتقل شود.
با این حال وزیر خارجه جمهوری اسلامی با اشاره به اینکه نتیجه مذاکرات یک «یادداشت ۱۴ ماده‌ای» است اعلام کرد مفاد آن بعد از نهایی شدن اعلام می‌شود.
وزیر خارجه ایران در گفت‌وگوی خود خبر داد که طبق تصمیم جمهوری اسلامی، «آینده تنگه هرمز و اداره آن مثل گذشته نخواهد بود‌» و ادعا کرد که ایران و عمان بیانیه مشترکی در مورد اداره این آبراه منتشر خواهند کرد.
او در ادامه اذعان کرد که طبق قوانین بین‌الملل گرفتن عوارض از کشتی‌ها در تنگه هرمز امکان‌پذیر نیست و افزود: «اما هزینه خدمات دریافت خواهد شد و این در مذاکرات تثبیت خواهد شد.»
عراقچی اعلام کرد طبق توافق، محاصره دریایی ایالات متحده علیه بنادر ایرانی به‌طور کامل رفع خواهد شد و دارایی‌های بلوکه‌شدهٔ ایران آزاد خواهد شد.
مقام‌های آمریکایی آزاد شدن این دارایی‌ها را به دفعات رد کرده‌اند. جی‌دی ونس، معاون رئیس‌جمهور آمریکا ساعاتی پیش تصریح کرد بعد از امضای توافق، هیچ‌گونه منابع مالی در اختیار ایران قرار نخواهد گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76283" target="_blank">📅 23:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76282">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UdFx6ojyi23QyrIEuuHToE_1bHNi2aJ-4vMr1Va_t9O_HEeliRw4DeQYua1Fkw48Mn7CVWdWbzecKvzXwU3DoYV9ijF4o7PgFIwalswsRwPeeS6L4ZectPZdgykWe1PhdZXrsBnXevtfCbtt7wXpH1I5rTpuXPEN-SjCqzyYs74slHYYazUdHj73Bovp3CmAoM12GZHvdlQP9LHTMXITNc5grb9nP5g2fxJ8zBQSaNT4L-zWq_7yYhNxPDnzo1yrpk3spMfeJjwNYAQYg-KVqcTpuOjtfuyG8M1rZLcRn_t-_YRCD0HCwtj0EG5H0hP3oMGMnism0wAz1CKBnn1ThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف، ترجمه ماشین:
تعهداتی که داده می‌شوند باید عملی شوند؛ نه اما و اگری، نه عذر و بهانه‌ای. برای توافق نهاییِ پیشِ رو، راه دیگری وجود ندارد.
هرچه بکاری، همان را درو می‌کنی.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76282" target="_blank">📅 22:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76281">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ug26XXcSn_DqOqavnE2gHnz-OOzCSAp-Bg_RvdysuL1NnCIGMnnZXmPvVMlX6IIsd2iszh01FAUiLTVived7W0ndgvyratAE9muN_cl1_uN-MENohiVbkTQxE5Q7nONsVSHp24Jvj9sXrepo8gIeLN7g9fxvwBQfAxWVP0M7EU9hNsRW-91BnEb_Akd0fpzJd9acM3QEikYhLDEYsZctCn_g6W3NUgb_NPKibrBuuyzGScyeMwWS2rcvSfWYJ2KaKlOgAhg2l6FRJxwIWPGHdnBXFZsacAGKDItOWtjlAO7eg_JFHXiZSZFLYNexDebk5NRx9W4zg2mRkiQ5B_rRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار منبع آگاه به رویترز اعلام کردند که امارات متحده عربی با آزادسازی میلیاردها دلار برای حکومت ایران موافقت کرده است.
رویترز نوشت که این اقدام نشان‌دهنده تغییر تاکتیکی ابوظبی پس از هفته‌ها حملات حکومت ایران به این کشور ثروتمند عربی خلیج فارس در جریان جنگ آمریکا و اسرائیل با جمهوری اسلامی است.
دو منبع منطقه‌ای به رویترز گفتند که امارات با آزادسازی مجموعا ۱۰ میلیارد دلار موافقت کرده است که
بیش از ۳ میلیارد دلار آن تاکنون پرداخت شده است.
دو منبع دیگر که از این توافق آگاهی دارند، مجموع مبالغ مورد نظر را ۲۰ میلیارد دلار اعلام کردند و افزودند که این اقدام در ازای توقف حملات حکومت ایران به امارات متحده عربی مورد توافق قرار گرفته است.
یکی از این منابع نیز گفت که نخستین بخش به ارزش ۳ میلیارد دلار تاکنون در اختیار حکومت ایران قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/76281" target="_blank">📅 22:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76280">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BWA1o0QGdTaCjPWa1RXNr-CJhYywSUNSRk0xYZvh4IIY375QKsuyioNYefMDQ-kaVk8dP7fgfCOp1X-Xl_dJWLv07_S_q5fBFqzGWyZS_4_0eeEnNGWVLCSI_VlWrz_kq0zD-h12-o_ZSBpGLSY0yMTrRaXpi-CQ3LSkF4EJFbX4j-Jks0WVYr47phCYGB7Rgv6C6P19cIcLOsg0qp1x6LGPqj8COxMeEECJrwR7ffzKXfsh3zKFS5k1o-sl29Uk9_JLlK491oQU9MkILUTy1KaIME48C8kteEpGkuG6kG7ZpN_F3fnOajvyE4TT74DdLdToh4QPBv6E_YvvsHXfuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس در انتقاد از
توییت عراقچی
نوشته:
عراقچی نه‌تنها مستقیماً ادعای ترامپ درباره «جعلی بودن» مفاد منتشرشده را رد نکرد، بلکه با درخواست از رسانه‌ها برای پرهیز از گمانه‌زنی، عملاً فضایی ایجاد کرد که می‌توان آن را تأیید غیرمستقیم نادرست بودن برخی اخبار تلقی کرد.
آیا موضع‌گیری او نوعی عقب‌نشینی یا هماهنگی با روایت ترامپ است؟ در شرایطی که ترامپ مدعی عذرخواهی خصوصی ایران شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76280" target="_blank">📅 21:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76279">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LXnP7P2819ypPhnRXReJL6M2stqBi0JMbNeKIqzYoePl_EvCiwYzmR3fX0zwlRdf8k6XfjytfcnisZGPC5xwDQLWktAm5FeR5rS5YlbaJw57qprtFnlxdslWyAY7zmcpzOE3JEA2_Z98ziXERtVgJTpyVxH8qDrnouJqnk9PNfY6Yjt-ckJ8FTbB51YQmqZOTYO85Ff4oByoVJcjinVUHFGI3jsS3ZwupFvWT8tRW_abIwGaNkFdKaUFZDI32Q9Bm0nRHsYqC5ZR3gpG1Iu4vQJu9p2C25Hnn2F5lh-IxCbSh3UUq-wQ3i-9OZzfNyAJ_SQ5BREVwu56eBjbUjv7-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی روز جمعه در گفت‌وگو با خبرنگاران با اشاره به این که واشنگتن انتظار دارد توافق با ایران در روزهای آینده امضا شود، گفت یکی از مفاد آن نابودی و خروج ذخایر اورانیوم غنی‌شده ایران است.
این مقام آمریکایی که به شرط ناشناس ماندن صحبت می‌کرد، اظهار داشت: «تیم مذاکره‌کننده ما را در موقعیت بسیار خوبی قرار داده است، اما باید ببینیم چه پیش می‌آید. هنوز کاملاً به خط پایان نرسیده‌ایم، ولی بسیار به آن نزدیک هستیم.»
او گفت که مفاد مورد توافق، اهداف اصلی دونالد ترامپ، رئیس‌جمهور آمریکا، را محقق می‌کند و «در پایان، وضعیت را در جایگاهی بسیار بسیار مطلوب قرار می‌دهد.»
این مقام افزود که مفاد آنچه «یادداشت تفاهم» نامیده می‌شود، شامل بازگشایی تنگه هرمز و لغو محاصره آمریکا علیه بنادر ایران است.
به گفته او، ذخایر اورانیوم با غنای بالای ایران نیز در محل نابود شده و سپس از ایران خارج خواهد شد.
این مقام افزود که مفاد توافق همچنین شامل یک رژیم بازرسی است تا اطمینان حاصل شود که اجرای آن در بلندمدت قابل راستی‌آزمایی و الزام‌آور خواهد بود.
@
VahidHeadline
پست‌های خبرنگار نیوزنیشن در کاخ سفید،
ترجمه ماشین:
🚨
اکنون یک مقام ارشد دولت ترامپ جزئیات بیشتری درباره توافق پیشنهادی با ایران ارائه می‌کند.
آن‌ها انتظار دارند این توافق طی «چند روز آینده» امضا شود.
صددرصد قطعی نیست، اما احتمالاً ۸۰ تا ۸۵ درصد احتمال دارد که طی چند روز آینده امضا شود.
این توافق «اهداف اصلی»‌ای را که رئیس‌جمهور برای این مأموریت تعیین کرده بود محقق می‌کند.
نخست، تنگه را بازگشایی می‌کند و محاصره را برمی‌دارد.
🔻
برچیدن برنامه هسته‌ای ایران.
دریافت مواد غنی‌شده توسط آمریکا: هم در محل نابود می‌شود و هم از کشور خارج می‌شود.
ایرانی‌ها دیگر خشونت در منطقه را تأمین مالی نخواهند کرد.
یک نظام بازرسی که اطمینان دهد این یک تعهد بلندمدت و قابل اجرای بلندمدت است.
🔻
پرسش درباره «حجم دارایی‌هایی که در صورت پایبندی ایران آزاد خواهد شد».
به گفته مقام ارشد دولت: وقتی ایرانی‌ها «به تعهدات خود عمل کنند، می‌توانند در ازای این عملکرد، امتیازاتی دریافت کنند.»
🔻
پرسش دوم: چه چیزی تغییر کرده؟ چه چیزی باعث شده این توافق نسبت به قبل ملموس‌تر باشد؟
-«ما به مرحله‌ای رسیده‌ایم که متن را به جایی رسانده‌ایم که از آن احساس خوبی داریم.»
-«ما متن یک یادداشت تفاهم را داریم که فکر می‌کنیم هر دو طرف نسبت به آن احساس خوبی دارند.»
-«ما احساس می‌کنیم کنترل ایرانی‌ها بر تنگه هرمز تضعیف شده است.»
🔻
مقام ارشد دولت: «چه تضمینی داریم که ایرانی‌ها به سهم خود از توافق پایبند بمانند؟ ما هیچ امتیازی نمی‌دهیم مگر اینکه آن‌ها به سهم خود از توافق پایبند بمانند.»
این مقام ارشد دولت درباره یادداشت تفاهم با ایران می‌گوید: «متن را به نقطه‌ای رسانده‌ایم که هر دو طرف آن را می‌پسندیم.»
به گفته مقام ارشد دولت، اگر آن‌ها بتوانند به آن پایبند بمانند، می‌توانند ظرف «چند روز آینده» به توافق برسند.
مذاکرات فنی ۶۰ روز طول خواهد کشید.
آیا رهبر عالی ایران این توافق را، به شکلی که شما شرح دادید، تأیید کرده است؟
مقام ارشد دولت می‌گوید: «افراد در طرف غیرنظامی و نظامی... شهادت داده‌اند/اطمینان داده‌اند که رهبر عالی از جایگاه فعلی آن‌ها در مذاکرات رضایت دارد.»
KellieMeyerNews
مقام ارشد دولت به من می‌گوید که در ۲۴ ساعت گذشته، همه از ونس گرفته تا ویتکاف و کوشنر و ترامپ، به‌همراه هگست، روبیو، وایلز و رتکلیف، در مذاکرات مربوط به ایران دخیل بوده‌اند.
KellieMeyerNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76279" target="_blank">📅 21:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76277">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hKtbe3TRzN4RzeV1iJVISZnHeyUPLjVJ0sCsyUFkjmU-ibF5OFo4dNChrwKxUE7k7enyq9KyNv8rUVc1RwLf3cTMW5mcX5zw6GNrqWTneCiZ19p99_qdNeSJjjh1s81j2AAK5v4JtJ2En03dQwNql0VfUQHoViDs1kqNWP4tl1veWM4mCTuKrqCDIqXd64Mgj9WGzC-4ZpsmD1gdOd1vnv2KRZCWWmMWhPnKG-YT0AKK4tsfDrzq3LUZn-w3uymRCjwA0n26l8hnuwGVtlFSqdZzHjI1FSqmaOx-lWIMx7p97twhNFu1CmfMoFuP7BmmrdgOeNV69VYAr8pIPLvJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/omTcFEKztiCg6lIcawBYVHaBF9lO3yYcxQGAGttAHV8W6Y2Dg_o1fcQ_45HB4UwqgkERlAP4pmc2E-oLO_s7AfFKa86gO2tktk7TBxnZmtAbbLPCjBkUtHbLentcyJ7pAmX3t7ARzSHZ9wzlQJJQfrFsb5MOk7bs3m6u_57RLP8cmPFJ7rsDBH_3W1fJLfSiRXQcN4MzaOc9qlTy8LKJy1-HmOp1uLN9U2rbmr5RjWSMYuoN6to-WnSYgg8xy1u9WbpdbNvnoPbUq4vl3CfjsBF3ccVZUACojYav13nJGW5iBmp-sgzB0TaEGyiHyL9Q2C4rhDOrCNZGWtTfjNNTOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یسرائیل کاتز، وزیر امور خارجه اسرائیل، روز جمعه ۲۲ خرداد، با انتشار پیامی در شبکه اجتماعی ایکس اعلام کرد که هرچند رئیس‌جمهوری آمریکا بر اساس منافع واشنگتن و هدف مشترک با تل‌آویو، یعنی جلوگیری از دستیابی ایران به سلاح هسته‌ای، به سمت یک توافق حرکت می‌کند، اما اسرائیل انتظارات فراتری دارد. کاتز تاکید کرد: «از رئیس‌جمهوری آمریکا انتظار داریم این اصل و شروط دیگر در حوزه موشکی و گروه‌های نیابتی را حفظ کند».
او با اشاره به اینکه ضربات سنگین مشترک، توانمندی‌های ایران را سال‌ها به عقب رانده است، افزود: «اسرائیل باید تضمین کند که در آینده نیز توانایی اقدام مستقل برای جلوگیری از هسته‌ای شدن ایران را دارد؛ به همین منظور، من و بنیامین نتانیاهو به ارتش دستور آمادگی لازم را داده‌ایم.»
وزیر خارجه اسرائیل همچنین به عنوان درس اصلی از وقایع ۷ اکتبر تصریح کرد که این کشور به هیچ وجه از مناطق امنیتی در لبنان، سوریه و غزه عقب‌نشینی نخواهد کرد و ارتش به دفاع از مرزها در برابر تهدیدات جهادی از بلندی‌های حرمون تا عمق غزه ادامه می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76277" target="_blank">📅 21:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76275">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WOOnBFja8RHjokGz0m5O9uske6XAZivs9YdkWCp1hKw2slNe-fXpiMeSSplNgE1sVbp6PhQKFoI72v1JG-smjajSgmrHa4mht8DbHk691ghkrUAKS1UmSzymEXcsiYszqLww7M-UrTinAUyh6j9HapQpPzFvx52LvapV3rDLwI-Py6XroFTvIY8v5el-g5WDmAq6p7V9C802D8aVgYVzKtEEmqvgm9y9rzun0pOkN1Dc51w1UhpMBQLGkDJGQcY3ibk4FhwBDBfhA5IzgOmgQMQ5NJfo1a2HMCNOLhwwI_wmstPwZNGNh-33-eVn_tsb2dEF7L96s2ynrPrapmAibA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DJmyLwkRTvoXz1EaPKsquTcZ43lrMxBTfs5ToQrdTUsNnQTo3Jv18qE-Qs3B6_79QYGtAyiu1WAEwW6Uqp7QF5Ywl227aQlbd8YJfDfnYwCF2qSnhv5py0jtL8wb42Qyw5HHPZl_3gMji4jUgMo8lvLaKyfoVTQwjuoGilKLfxG4vnXq4ICUh7KmIyu2w1dtKw3FeFQaVGJrM7edtqcz0KCAbpe1Ng2WSJFjlrqNJWIxgsy07ykoyqRPEbMCS6RQG5DTc1ITzPylt6Ns3GxqPNk-zvLE0ouXaCOuwxaFSkfOymIDRsBHk_6AzDZqiPriemjzNEnauZpSbFq3W4dt4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمود نبویان، عضو کمیسیون امنیت ملی مجلس شورای اسلامی، در ایکس نوشت: با مشاهده‌ی متن توافق باید اعلام کنم، نسبت به دو نسخه‌ی قبلی، خسارت بارتر و عقب‌نشینی‌های ایران نیز بیشتر شده است.
@
VahidOOnLine
نبویان سپس در توییت دیگری با اسکرین‌شات پست ترامپ درباره توییت عراقچی نوشت:
توافقی که با پخت و پز بانیان توافق ننگین برجام باشد، حتما
#خسارت_محض
است
nabaviantwt
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76275" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76274">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U6JwzBsvTHXIA7OPkm5WcG4abB3m6nS7js_vMN7soxbCE20lTr3j3khTuV0b2ctr400Oa9yuvmFoVapIQXF6BW3w0doaLING6R-WK5h0WBIgVJMdsck4fQoSOC2RWR69DZha68ZkULRPQsVXDwFZ9hyelfM5Udi29Qu72wmdikGRnoIVCNbxo7kt-zFTDB6moCPCTtHOZ1Pd-ItVsK4Bzk5NQhT5ISqHXk1IwFR95T8nwdDemriaEvQDslXEVpVosANBn26OjIOMFl2NhMew98UHRtX4NaCixCyKjKVhsFR_SS2069BRYu-pNaoNlzOurAMVNsMQG64HN0J5nAHB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.
سی‌ان‌ان به نقل از مقام ارشد دولت ترامپ افزود که جمهوری اسلامی با «برچیدن برنامه هسته‌ای، نابودی و خروج مواد هسته‌ای، آزاد نشدن دارایی‌ها تا زمان اجرای تعهدات، باز ماندن تنگه هرمز و توقف حمایت مالی از گروه‌های تروریستی» موافقت کرده است.
مقام ارشد دولت ترامپ گفت مقام‌های جمهوری اسلامی پیش‌تر گفته بودند بدون آزادسازی دارایی‌ها توافقی را امضا نخواهند کرد و بارها از گفت‌وگو درباره حمایت مالی از گروه‌های تروریستی خودداری کرده بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76274" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76273">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DWPwNMINQGgaiV5OXDH_TRbfd5d5iR-wnTpLLgRWV-4Z-yh-vHsTcnkd0oYAcqFgxn0DCfRP1Av0EVeqCvFNZ6N0K-B945h6aorhKkF7Fc4hmhTmEOSpbxQFp7UVlRslakY8mcAlYiMBTzNQiW3NoRdLl_RggxELb603bM_vyCK_Cm87Kuxg5BkREyhlPPHsWVXQCsK39Dm9XlEI_gMZr0TJ45Ux0sW1Swq4nl_RGuzmaAVZ9GTB7v9WzpRYI4QDt5_gbpekbBzYQanEaBlDrJoX55yNP_DuA2GbppNlKxpRIMhgMHP_jLDvFBhcAfKxE3aNp67lDpNuD-7PRqyNtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس گزارش داد دونالد ترامپ،
پیام عباس عراقچی در شبکه ایکس
را «بسیار مثبت» ارزیابی کرد و گفت معتقد است توافق با جمهوری اسلامی می‌تواند در آخر هفته یا روز دوشنبه امضا شود.
اکسیوس همچنین به نقل از ترامپ نوشت که جمهوری اسلامی به صورت خصوصی بابت انتشار «اطلاعات نادرست» عذرخواهی کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76273" target="_blank">📅 20:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76272">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ELk2T3y65TxOgsFENFIMFuLNfUr7syEYif0-f-ESRJsMx9I_Mcc4sFuAtI3_tKi8uhowyamIdk-AQ0G13r3qjYak-QwoHtbR4LVjGn12Msc0eDBYtvOIn75RZWuXbpmnwHwx31vcr6mRfHjph5dwVZ4FSSOV_t76OpoLi4yNWzQXICfRGTlaOjPWTV3Gum2yvom79RDAunuw5eg02OFWEfUUwe1DtmcZ75kl68YkiejxHWFfzNc6xoOUoQTOYqISjTDgepMKuIAEnNRN016ulp8ASvkuXLPfUmLk8tbD9R7zcaUig9nM1b7GrWGwvbqZkRTUl7YTqtO_WC3q01UpEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیرحسین ثابتی، عضو مجلس شورای اسلامی، نوشته:
طبق اطلاعات به دست آمده متن توافق احتمالی بدتر از برجام است/ چنین توافقی نه گشایش اقتصادی می‌آورد و نه جلوی جنگ را میگیرد
دوشنبه شب در تجمع مردم در میدان مجتهدی طرشت حاضر شدم و توضیح دادم که دشمن به دنبال نابودی ایران است، چه از طریق جنگ و چه از طریق مذاکره و کسانی که هنوز هدف دشمن را نفهمیده و فکر میکنند با توافق با امریکا میشود دشمن را سرجایش نشاند، بدیهیات اتفاقات اخیر را هم نفهمیده‌اند.
سپس گفتم طبق اطلاعاتی که تا این لحظه از متن توافق احتمالی به دست آورده‌ایم توافقی ضعیف‌تر از برجام در راه است که خطوط قرمز رهبری در آن رعایت نشده و نه باعث گشایش اقتصادی میشود و نه امنیت کشور را تامین میکند.
در پایان نیز تبیین کردم که اگر بخواهیم امنیت مان را حفظ کنیم باید بیشتر از همیشه آماده جنگ باشیم وگرنه با ژست مذاکره و گفتگو و تن دادن به توافق به هر قیمت امنیت کشور نیز در دراز مدت مخدوش خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76272" target="_blank">📅 20:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76271">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YFBs8RxBGidQj7MzyPPT7kwM9tFYYMTcc0JQca6vaSYlBj4EU_HEBQUqAdZh2-l6fVePpnjQUPEAl-dFWCXtvflo_TcLom042cK6iIorOwk9NUkhcXQ5wUcz_s75dZstC4ACWljd7FjSy46zGJ5p5_MxSyteT4emWr0UZ0JPuAxFLJJx_6XsFivuUKTJtDtMAYHh65WbTmOFUfd_agdnK-MGrgRiOek3uvuWtlHm-bsY6GEGwbU1n-CfaZ-C1igxaiJZme6bnnNVpg3KvzaqKKLwUA0k7hJIHfQQRCcHDlAfqkAbiiZzjnGBw2BmoaXX4nxrYaXSw1QMH3bIIfFOCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف، نخست‌وزیر پاکستان در پستی در ایکس نوشته است «در میانه تلاش‌های فشرده میانجی‌گرانه پاکستان، ما کاملاً از کارزار بی‌وقفه انتشار اطلاعات نادرست که از سوی طرف‌هایی که با هدف خراب کردن توافق صلح انجام می‌شود، آگاهیم. با کنار گذاشتن این حاشیه‌ها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق حاصل شده است و پاکستان اکنون به‌طور نزدیک با هر دو طرف برای نهایی‌سازی مراحل بعدی همکاری می‌کند.»
او نوشته است:«صلح هرگز تا این حد نزدیک نبوده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76271" target="_blank">📅 20:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76270">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fF7_OHwlcYFw17h_eraGXoA-DUNvYDZU5Yz7Uz2M_Fd_3Y-2m1RqB6AktsvvcKRWH7PdYPaXNYuaxKczEQ6u6Bkpi_Dj3NJ0uCL6PyqDb1tAXOkt1Heo2o8yEBJXYPcKrCcvWsvjzvg978eC4fQEPg3WcNtdKpYVWe2l0LTAGJPhpP6CWro2J_s1JQ6LYfoBe3clG8OJN_BlUy5Ac2sRMtO3TVyS3qQv_DQrIL8UICrNPJJMdL0aSbekVOjnvefuUP5CwOUH8cZ9Lxwt2-o6pJy_QO8RSt60cnWiM4i-9-TDcEzlvY7AUZ_9EoHCXlaH_QOPMlq2U6sVRjjipShjPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اسکرین‌شاتی از
این توییت عراقچی
رو پست کرد:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76270" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76269">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pEW02yNgmyM9w1g6uiVKJDgLeob8Ralnw5CRwMvKCcXA5Fmh5CnVin96_EY3G47VYHYt0uSbej-FOoOCI-0DHy9FSYfJKa3hYtZDBOJyLc9nCWu5JP3X7ySZejUnPI6toUI7m_NcNmFL0WDXdyxA8B8RgPGF4xFkaqhqrghlFAiXVuCw6rMFpjGx1jFvnoWO_cie1jxSctCu3Q-z0K7zghDRX1OM5qN2Dh2QjELxN3XEb6bmMrhWo9QEJAcMNTdBKSR6qXAGgWWT1QWP71sxOEBn7YAHkacDniOIgXMPWOBQLtCILzy71KHiQ9rJdk1Ihfyx1bw0aLdMk8FyGqd5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه واشینگتن‌پست در گزارشی خبر داد که قطر در جریان جنگ ایران مذاکراتی پنهانی با جمهوری اسلامی انجام داده تا تاسیسات گازی خود را از حملات تهران در امان نگه دارد.
قطر در واکنش، این گزارش را تکذیب و واشینگتن‌پست را به تلاش برای آسیب زدن به نقش میانجی‌گرانه دوحه متهم کرد.
واشینگتن‌پست در گزارش خود تاکید کرده که اقدامات پشت‌پرده قطر، تصویری از شیوه‌های پنهانی کشورهای خلیج فارس برای دور نگه داشتن خود از خسارات بزرگ‌ترین جنگ منطقه در ۲۰ سال گذشته به دست می‌دهد.
در این گزارش با اشاره به حمله موشکی جمهوری اسلامی به تاسیسات گازی راس لفان در قطر در اسفندماه سال گذشته، نوشته شده است این حمله بخش‌هایی از بزرگ‌ترین مجتمع تولید گاز طبیعی جهان را نابود کرد که نزدیک به یک پنجم گاز جهان را تامید می‌کند.
این حمله همچنین قراردادهای چندمیلیارد دلاری با چین و دیگر مشتریان را به خطر انداخت و چشم‌انداز پایان زودهنگام جنگ را با کشاندن قطر، یکی از میانجی‌های کلیدی میان آمریکا و جمهوری اسلامی، به درون درگیری تیره‌تر کرد.
به‌نوشته واشینگتن‌پست این حمله اما یک پیامد پنهان دیگر نیز داشت. به‌گفته مقام‌های امنیتی خاورمیانه و مقام‌های غربی مطلع از اطلاعات محرمانه، این حمله همچنین تلاش‌های مخفیانه قطر برای خارج نگه داشتن مجتمع گازی خود، موسوم به «راس لفان»، از فهرست اهداف جمهوری اسلامی را ناکام گذاشت.
یکی از مقام‌های ارشد امنیتی منطقه به این روزنامه گفت قطر چیزی در حد یک «توافق محرمانه» پیشنهاد کرد؛ توافقی که بر اساس آن دوحه متعهد می‌شد از نفوذ خود بر عرضه گاز برای تسریع پایان جنگ استفاده کند و در مقابل از جمهوری اسلامی تنها یک تعهد می‌خواست: «به ما حمله نخواهید کرد.»
یک مقام دیگر که به همان اطلاعات دسترسی داشته نیز به واشینگتن‌پست گفت پیام قطر به تهران این بود که: «شما بدون حمله به ما نیز به اهداف خود خواهید رسید.»
به گفته این مقام‌ها، قطر نتوانست تعهدی از جمهوری اسلامی دریافت کند. با این حال، روندی که پس از آن رخ داد نشان می‌داد که احتمال وجود یک تفاهم ضمنی دست‌کم به‌طور موقت همچنان برقرار بوده است.
قطر در سومین روز جنگ، زمانی که جمهوری اسلامی صدها موشک و پهپاد مسلح را به سوی اهدافی در سراسر خلیج فارس شلیک کرد، مجتمع راس لفان را تعطیل کرد. در آن زمان، قطر دلیل این اقدام را «حملات نظامی علیه تاسیسات عملیاتی» اعلام کرد.
تصاویر ماهواره‌ای که بعدا از سوی واشینگتن پست بررسی شد، هیچ نشانه آشکاری از خسارت در راس لفان نشان نمی‌داد.
اظهارات مقام‌های قطری نیز نگرانی‌ها را در بازارهای جهانی انرژی تشدید کرد؛ از جمله هشدار وزیر انرژی قطر که گفته بود این جنگ «اقتصادهای جهان را به زانو در خواهد آورد.»
قطر در پاسخ به پرسش‌های واشینگتن پست، هرگونه توافق محرمانه با جمهوری اسلامی را رد کرد و گفت تصمیم برای توقف تولید در راس لفان صرفا به‌دلیل تهدید حملات و نگرانی برای کارکنان و زیرساخت‌هایی اتخاذ شده بود که شریان حیاتی اقتصاد این کشور محسوب می‌شود.
...
iranintl
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76269" target="_blank">📅 19:05 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
