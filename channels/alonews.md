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
<img src="https://cdn4.telesco.pe/file/pKtdacKK7PZ0slH5lMiqmIbeyVn4NOa1XOpUKqbiM6N-NTfiTvt4JXTGsZ2_W5bo6Px9OWeQTZA3ytsMV5DBcaSEUxc0tq5ALx1FA9_hhVdzY66kzcL-5-23Hp_yM8Jt-dQLouXJgm5xT_HyOX477GARsFncTCk-MDnHJHwJhxTJ4rJJmIHF8fvc4LUDiVx2rn8DxlAzlHnkA7aH5cptnXbXDjyOMVdSd_MxdvzIzSJN7BjE8KD8RIFjlWGQl5Rvrb8u4xBUo3cPIwedPDwfqG0eidYAlZ2fa_hFjczCw3g4viTobkL43lR2Y2LHt3ZaexFo7MTn8HOxTdxtzgGkOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 978K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 23:48:21</div>
<hr>

<div class="tg-post" id="msg-143803">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
گیدئون ساعر، وزیر امور خارجه اسرائیل، اعلام کرد که نمایندگان هلند فوراً از مرکز هماهنگی بین‌المللی غزه در کریات گات که تحت حمایت آمریکا قرار دارد، اخراج خواهند شد.
🔴
ساعر گفت این تصمیم با تأیید بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و در واکنش به آنچه او مجموعه‌ای از «اقدامات ضداسرائیلی» از سوی دولت هلند توصیف کرد، اتخاذ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/143803" target="_blank">📅 23:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143802">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4311254a.mp4?token=Y9XdyiROd9UD4Y_rJF14phf7440qvaHA7VFzHWM33e1YDt96jldNwVstPKd0oHYGx0ONVOl7lBrq-0UCeTI54o8X9Thhd7fUdv1JugCZ1DH1FhMAJcYxywYKpklZI1btN2eR-JNdvQFMFCwo14XLmV4yflXAOT7oP87jxYl_T0MtAW5wwDcEDN1xsp4VMSjXNnVMY-40G9ORShhFMgozy3vg9kd6eCbTuOfSGn4ac_wHCTR_5eKbmAacXQm56uYtD3oqKwGsaScWsywN4ltM8XTfDN_qYGLbvTMW2fIfUbghRU9CwocDFo4R1P_PCPbGBumUJ2lR50_tdoUqdW-GZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4311254a.mp4?token=Y9XdyiROd9UD4Y_rJF14phf7440qvaHA7VFzHWM33e1YDt96jldNwVstPKd0oHYGx0ONVOl7lBrq-0UCeTI54o8X9Thhd7fUdv1JugCZ1DH1FhMAJcYxywYKpklZI1btN2eR-JNdvQFMFCwo14XLmV4yflXAOT7oP87jxYl_T0MtAW5wwDcEDN1xsp4VMSjXNnVMY-40G9ORShhFMgozy3vg9kd6eCbTuOfSGn4ac_wHCTR_5eKbmAacXQm56uYtD3oqKwGsaScWsywN4ltM8XTfDN_qYGLbvTMW2fIfUbghRU9CwocDFo4R1P_PCPbGBumUJ2lR50_tdoUqdW-GZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غریب آبادی: بر خلاف ادعای مقامات آمریکایی تنگه هرمز بدون ترتیبات ایرانی باز نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/143802" target="_blank">📅 23:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143801">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7553b9202e.mp4?token=kalufmxSPhSXra19GifOA7fMNANfSqvxtZb0W8yzd7ji4q6Qyl4qEvVmn6IZOXW8XYXGLpRg_UXA301pzhCg-e-Wi2-pCcXZqO02Ghq_5aInP2Dxy5rZyL8a9NImNAgCGVJRG1SeeQJ-YEvQ2elcN5KmYtqbeM1bcQRwmK1rXa-hydQrTTiJ2YlSxSxJmx9wKU5foOPnrGCv7-blc0N99EIl-nZa32aHHGBh1Qz8iUr7vXmJqQ8dwt0w2gFk-cJ4_6I-TAv646F8oEibwkZoHnIjecwkZ5FFnYQrfNJvClPwgAlkmfysxO_PaDPP7dtYIGlXIrOp9r2Dkms2XIIIVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7553b9202e.mp4?token=kalufmxSPhSXra19GifOA7fMNANfSqvxtZb0W8yzd7ji4q6Qyl4qEvVmn6IZOXW8XYXGLpRg_UXA301pzhCg-e-Wi2-pCcXZqO02Ghq_5aInP2Dxy5rZyL8a9NImNAgCGVJRG1SeeQJ-YEvQ2elcN5KmYtqbeM1bcQRwmK1rXa-hydQrTTiJ2YlSxSxJmx9wKU5foOPnrGCv7-blc0N99EIl-nZa32aHHGBh1Qz8iUr7vXmJqQ8dwt0w2gFk-cJ4_6I-TAv646F8oEibwkZoHnIjecwkZ5FFnYQrfNJvClPwgAlkmfysxO_PaDPP7dtYIGlXIrOp9r2Dkms2XIIIVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غریب آبادی: در مذاکرات با عمان ستادکل نیروهای مسلح نقش اصلی را ایفاء می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/143801" target="_blank">📅 23:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143800">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
‌غریب‌آبادی: پیش از هر اقدامی برای بازگشایی تنگهٔ هرمز، آمریکا باید تمامی تعهدات نقض‌شده خود را به‌طور کامل اجرا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/143800" target="_blank">📅 23:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143799">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‌
👈
غریب آبادی: انتظار داشتیم تا با کمک دوستان عمانی مسیر جنوب در تنگه هرمز را ببندیم اما فشارهای آمریکا مانع شد و ما مجبور به درگیری نظامی شدیم
🔴
در تفاهم با عمان مسیر ورود به تنگه کاملا در اختیار ماست و بخشی از مسیر خروج هم در آب‌های ایران قرار دارد؛ همچنین فاصلۀ ۲ مسیر زیاد نیست.
🔴
در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد
🔴
البته درحال حاضر هم نیروهای مسلح ما اجازۀ عبور از مسیر جنوبی را نمی‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/143799" target="_blank">📅 23:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143797">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
غریب آبادی: تفاهم ایران و عمان معنای بازگشایی فوری تنگه از فردا نیست و این دو موضوع جداگانه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/143797" target="_blank">📅 23:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143796">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
غریب آبادی: طبق تفاهم‌نامه هیچ شناور نظامی اجازه عبور نخواهد داشت و تنها شناورهای تجاری امکان عبور از تنگه هرمز را خواهند داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/143796" target="_blank">📅 23:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143795">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
بحران بنزین شروع شد
‼️
‼️
خودتونو آماده کنید برای طوفان!
تحلیل ترسناک این پسره رو حتما ببینید
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/143795" target="_blank">📅 23:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143794">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYDkY4Ej_3LnxwAhl0cjI4dYzo05rD6Ehi5eB7KTR1Y2KGiRgJArmVN9v6OsqL98yTNdAGVZQ_ANuRpHE6i3h7p7thr3y2RNVgKO7w6jzj5b0Ca815CA-sp_CUU7W891Jehfrs-ThZm4M98H-Mm2DXOJCbXwaj6mXO0JaLrTRUWs00YV1rCgbBpnszKVpWrurN5uhx1G0l37VGgoKempaQwoF2g05CIV9GTZKiUcNhnjC0NRpm3jSbINl8tMfwWJ_fC7ek2-AmGQSmTMdlc8m5NXLFuwgsZxyXgcj2SpoHIcCyTQPKlDEmugtpxckvwYJ5GmqtFhzRGhah5lhhRabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر تراکرس: حدود ۲۵ میلیون بشکه نفت خام در خلیج عمان منتقل شده است و ۱۵ عملیات انتقال از کشتی به کشتی مشاهده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/143794" target="_blank">📅 23:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143793">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزیر نیرو: ایشالا با تدابیری که چیدیم تابستون بعدی برق کمتر قطع میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/143793" target="_blank">📅 23:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143792">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbRys_RCD18U64HIW_i-Wbj9zw9OI-g9JNTss0gyrpKcUbdRznPVQwgiDMBZVUygR8O4j26mayfVPRzYpv06kmp3u8kwmpY6T9TUeJJgQO6AHP969jhG6wq8I1ZZmKboefPamnsKCHeM6zGBDazngjDNecrJLrxG3pKsY22L5xdqHvoEep64mDtBXeZqrqgVBBbsES-vm0LimZzB0nVwRDqh1hGsrscfxiz7RRLpc5-4EeQKlUUP72X8lLXj8t4EB-o61131POVY5dpUK1WktwmBEOfYu6PZ3N0yH0Y1xDm40lshBn63NmX4JD95PlLgSuCnKMCNccERwZo_vMnX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیام عراقچی پس از دیدار با واسطه‌های پاکستانی و عمانی
‏
🔴
تعهد ایران به صلح و ثبات، همراه با دیپلماسی استوار و مستمر با همسایگانمان دنبال می‌شود.  در گفت‌وگو‌ با میهمانان پاکستانی و عمانی، بر راه‌حل‌های منطقه‌ای تأکید شد.
‏
🔴
چارچوب پیشنهادی برای ایجاد یک کریدور جدید، مین‌روبی مشترک و مدیریت آتی تنگه هرمز، نمونه‌ای روشن از این رویکرد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/143792" target="_blank">📅 22:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143791">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rl6xYDHMWkSTveZUdmXGvlhbrCSNeY8JXfx0eKQJKIZRoMBCirxqUan7VHiqDsFxpWVPwDWdfCN74ELlLAeAmcjl1I4NeR0oieb2Nrf9J-ZwSbgq09xegfNWi-h2qjtrel8D1vEcTji_nteDiN_mJL01wRX7VAS8Sz9ApfX5NIELqK4YoXShgwjOStlVZZBRYHzb9Si8UWAkZBOVyYtxE4Nd9yuaV_yoayv81yilWkZ50U7YstaOykPVCPeEJF2T2hODmzt1baVtCldqWu9i9keHXa4_TQhQc3yLgNvXXtxVcUCPJwG4cN72pVaGp0jbf4qNDoZwy3dMFw-prjxf-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ دستور داده است که پرچم‌های ایالات متحده از ساعت ۱۸:۰۰ امشب به مدت یک هفته به نیمه کشیده شوند تا به افتخار دولی پارتون
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/143791" target="_blank">📅 22:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143790">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
اتریش حجاب رو برای کل دختران زیر ۱۴ سال در مدرسه ممنوع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/143790" target="_blank">📅 22:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143789">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn8cB4r1eqR2aDZtnWHCFWrkHjz2gAbxAP71_2j4UkrKmnx0MuSUafz8qqzTELUGb6xjBt-VHpslC-evKOwjN_gGvk7PaZQx3qF9E3MlsdIskQMHR7zksAkr3pbhYzfJbPWYtpvx4LWmYc33F2lXxsfN7EEriUxb3rE0l1t5egq43qYEulxAQOFFNK8YSwuPFs3kTfx9Ega6ShKz1GAtxteIHBUFEWMbWGmz0T0MlBD2-pLxXoT--Nk0g9mfjspNxFXlpZJXKjnoKo_aa4V-M_YF9lnyAv_cVEE67k27uClGjDd16x5eretmjXAOe3N_DDlAdMmD1e1pf7VInm1u6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف به بسنت پاسخ داد: نمایش مضحکت، «روز پیروزی» نبود؛ «روز دلقک» بود!
🔴
اسکات بسنت که پیش‌تر ادعا کرده بود تحریم‌های جدید علیه ایران مانند «عملیات نورماندی (D-Day)» کوبنده و سرنوشت‌ساز خواهد بود، در نشست خبری دیروز وقتی با سؤال خبرنگاری درباره توخالی‌بودن این ادعا مواجه شد، دستپاچه پاسخ داد: مگر من می‌خواهم اقتصاد جهان را منفجر کنم؟!
🔴
محمدباقر قالیباف در واکنش به این عقب‌نشینی آشکار و تناقض‌گویی در شبکه ایکس نوشت:
این برنامه اصلاً شبیه عملیات نورماندی نبود؛ یک استندآپ مضحک در کلاب شبانه بود که در آن حتی دیالوگ‌های طنز خودت را هم فراموش کردی!
#روز_
🤡
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/143789" target="_blank">📅 22:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143788">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رویترز به نقل از منابع هندی: رئیس‌جمهور چین ممکن است پس از سال‌ها برای نخستین‌بار به هند سفر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/143788" target="_blank">📅 22:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143787">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3cc1597a2.mp4?token=OMm76hL7Bhykmi5uzgcoohGLWl6ekqnsYEciTYsG42j8I7wBmteCz3bdwm02WiSxDaI3m6TOSJAzV3HNhuDHm9afFHwll-Mbx9pwLU0A4xlBL0t6Odxv8TFrktAB-zMyWwCcBsswrewVK-ciomZiRNOK7EVnIUVx_DMSTkui5LojqaJ3Pl-uHDPJpmWFh89ndobNHA3PehNPuKlxiMebFdp6uE1UC3q-ifs7ERs7EfoflvaniIWwpXevs32Ldvr53ZxI0DOIYvuUBO-VadG_z9MEtHkQp5NQQTaXVcjGElg60u38b2mcFdi-eEmlHvNZFve7BQlVme1rNDajUg5ynA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3cc1597a2.mp4?token=OMm76hL7Bhykmi5uzgcoohGLWl6ekqnsYEciTYsG42j8I7wBmteCz3bdwm02WiSxDaI3m6TOSJAzV3HNhuDHm9afFHwll-Mbx9pwLU0A4xlBL0t6Odxv8TFrktAB-zMyWwCcBsswrewVK-ciomZiRNOK7EVnIUVx_DMSTkui5LojqaJ3Pl-uHDPJpmWFh89ndobNHA3PehNPuKlxiMebFdp6uE1UC3q-ifs7ERs7EfoflvaniIWwpXevs32Ldvr53ZxI0DOIYvuUBO-VadG_z9MEtHkQp5NQQTaXVcjGElg60u38b2mcFdi-eEmlHvNZFve7BQlVme1rNDajUg5ynA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر نیرو: ما آن‌قدر نیروگاه داریم که حتی اگر دشمن تمام توان خود را به کار بگیرد، نمی‌تواند همهٔ نیروگاه‌های ما را هدف قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/143787" target="_blank">📅 22:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143786">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k2JwhNPgd8k6YRGvOjUhOALNhEaFbXacmFlxoNt1FbTI7Z5DVYZk8xIRQqH1hlNWPkI241Rbr1pORGHZ9kTmNt1FRCyCyof39Le1r4qdEbeBAx979BjBCBkzUa_jz4YdR228yf6UczB4__Ia3Ig1gNs7X9yzdAK5IO6pHXTpxQAbHwwi1edKjQUDlOOx5oY8ZKwuudMmHZ9NSgTNrk2BNbZcYmy4g1dHY84eAVqM7NI55KGwN8-mecOhA8vlQ387okYHWtPVkBPC4ObrnOPJCt3Tvacty0m4lXEFvV-k3PoQuFREE62NSnqfjypXO_AtUFC2dbn4Rig21G_qdhXWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دود بر فراز دره سالوکی پس از حمله هوایی اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/143786" target="_blank">📅 22:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143785">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
فایننشال تایمز: کشاورزان غلات آمریکا با تشدید هزینه‌ها بر اثر جنگ ایران، با بدترین بحران چند دهه اخیر روبه‌رو هستند
🔴
افزایش شدید قیمت گازوئیل و کود تولیدکنندگان غلات را تا مرز فروپاشی اقتصادی پیش برده
🔴
پیش‌بینی می‌شود کشاورزان طی دو سال آینده هیچ درآمدی نداشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/143785" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
پاکستان از آمریکا درخواست وام کرد
🔴
پاکستان رسماً از وزارت خزانه‌داری آمریکا درخواست تسهیلات تثبیت ارزی به ارزش ۱۰ میلیارد دلار کرده که بزرگترین درخواست در تاریخ این کشور به شمار می‌آید.
🔴
این درخواست پس از نقش پاکستان در میانجیگری در مناقشه آمریکا و ایران، که روابط با دولت ترامپ را تقویت کرده است، مطرح می‌شود.
🔴
پاکستان در حال حاضر تقریباً ۱۲.۳ میلیارد دلار بدهی دوجانبه کوتاه‌مدت دارد که نیاز به بازپرداخت مداوم به عربستان، چین و کویت دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/143784" target="_blank">📅 22:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4YidmS7Do-FXO6K_CTTpYt_kA_kbz4SGr_M0qFKLFY9fFf5nghlRouiWGK1HSQ59oYuyDoSTlwcr9HlV_b7CqlAbUhc09xPge6TQ54iK5weKy_K54_QiL5SJn81OXO5TKsqhJDxlw7HN6n5K3_A1P9ZxBIvPf7QnGD5xjduST2Q9Vs2xl1I4bHL2ScF-EOFvr5Tdy2pUr8f9HMV4us8URPs2UqF2In_VfHVjuGOdfH05XKBdUMg9MJzgqReTV5j_RMA3idhxG-cPkdvI00DJhFZ4W5On_0cBaH8iVlat-sbdmTTJc6jhcxRruyLsZHslO58Hw-wYUZlJHnIaElpoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک انفجار در شهرک سربین در جنوب لبنان مشاهده شد، که در نتیجه فعالیت‌های تخریبی اسرائیل رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/143783" target="_blank">📅 22:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFwziEdOmPlAc2LhQXLzlYR-I1KyiaUCfHMy0xr7_MWPvPOVgIKynRASAd5PoHtjGaeOKIR34y_4p-nXSHCYkD9U5aciVS3kZudalQ2jbjEkDtWNi3_hh7kyxKbWTamAdgadVHRDLIJKDDoDf9Qn3jsrbYQbsr1CksdS6XNOpzrkR05VjO-IURIPpQ5FVXWox3nzxPk5KR28D8-eN7PiQdYjRAg8HELySPBbnd5f7yKyuZu_5qJpgXfBUs-0INxUUgvTO4m_XkrB6A8sBZkFFs32hhtU13HUNSL6KpSsBSOinSqAvddVj2KZsBFqgf8hbzcj9crN6x7IbYE1RykLzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو حمله هوایی اسرائیلی به شهر المنصوریه در جنوب لبنان هدف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/143782" target="_blank">📅 22:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143781">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
روزنامه القدس العربی گزارش داد انحلال شبه نظامیان کُرد سوریه (قسد) اعلام و مظلوم عبدی فرمانده این گروه به عنوان مشاور جولانی تعیین می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/143781" target="_blank">📅 22:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
گفتگوی تلفنی عراقچی و عاصم منیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/143780" target="_blank">📅 21:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پوتین طی فرمانی اعلام کرده شرکت‌های خصوصی که نتوانند از خود در برابر پهپادها دفاع کنند مصادره خواهند شد.. منظور کلی این فرمان فراهم کردن پدافند غیرعامل،مثلاً مانند حصارکشی مخازن سوخت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/143779" target="_blank">📅 21:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41454d8267.mp4?token=M09jLeL-iAFqp-kt0BI8WjUpK9BNWpFEfeT9dcYZWnm2cBUM-4pQXrHsU5A1POftPb-GgN7gnWCAuHCbsyTNdkSoa34a4d_IHHK7Z5gVjCxeVRjZpy2P38bw8QFe1AsBvuSYwty3V5U3WLFq3s8ds-dBsH68q2SA2AlkHupb_28MeBTl-2LNcS_aAjx1HDcOe-c27x44V1HojRSk994-iMZUj64wCMn2Jhn9DZONBhNnYTOM372kMNuQ8FVoUiMJ8K5IqoNNkyA2FJGo0QrZs1C9o6Bx7q2xhtMhAp2uqEEhjJw8gEIhEA66fk3R9J3BfjZfQoHm9KeRpkvqL9MVSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41454d8267.mp4?token=M09jLeL-iAFqp-kt0BI8WjUpK9BNWpFEfeT9dcYZWnm2cBUM-4pQXrHsU5A1POftPb-GgN7gnWCAuHCbsyTNdkSoa34a4d_IHHK7Z5gVjCxeVRjZpy2P38bw8QFe1AsBvuSYwty3V5U3WLFq3s8ds-dBsH68q2SA2AlkHupb_28MeBTl-2LNcS_aAjx1HDcOe-c27x44V1HojRSk994-iMZUj64wCMn2Jhn9DZONBhNnYTOM372kMNuQ8FVoUiMJ8K5IqoNNkyA2FJGo0QrZs1C9o6Bx7q2xhtMhAp2uqEEhjJw8gEIhEA66fk3R9J3BfjZfQoHm9KeRpkvqL9MVSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون وزیر نفت: با راه‌اندازی ۲ پالایشگاه جدید تا پایان سال، تولید روزانه بنزین کشور ۱۲ میلیون لیتر افزایش می‌یابد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143778" target="_blank">📅 21:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای خارجه ایران و قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/143777" target="_blank">📅 21:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
هیلاری کلینتون، وزیر خارجه پیشین آمریکا و بانوی اول سابق این کشور، می‌گوید هند و چین باید به دونالد ترامپ کمک کنند تا از جنگ با ایران خارج شود؛ زیرا به گفته او، این دو کشور خریداران اصلی نفت و گاز ایران هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/143776" target="_blank">📅 21:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOgV7l5w5Y2fmp2oJ1C1LD5g10fvxSo8bOVwqXSKBW4vstAjNk4FiOe_JeZjbEoHVtZZEnHYRFhZfBUq9gJurgpU7XStuP_0NxPIzpXOipEi87qOedoBClDw9cQbVHXkToEcra4qmGEp5_SxVMOjP2PgMTCjTXJhiwhBmUu2RDOFAbdn7DsYSZd9d-9a67ksIjD0tFh7wr1Xw2kgFYRmsji62Rpo1E4cmA3qfnfTTZAAlDgFkt9vVKeMO0M9qchDwQwJ2vETR7X-KkYhF-5mNLXAA7kPh9ViQqR2Deu_ziw3-0tYA69tPkxHgoMUXp3PQs--AkB9GXFD0QZ0GRT0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی این خانوم در ۲۳ دی ۱۳۹۸ گفت هرکی ناراحته جمع کنه از ایران بره؛ دلار ۱۳ هزار تومن و هر گرم طلا ۴۸۰ هزار تومن بود. جنگ هم نشده بود.
اون خوبیتو میخواست ولی تو گوش ندادی.
خودشم رفته آمریکا
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143775" target="_blank">📅 21:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n--52f_sqBGA3mRaIK1yTE0WOo4al-U0vJDRH8Hy2v3LXNu1BQt0LcJwhoRWaXHsoHKKYoz0zRcUEcJSbw_B9Y3uQhVgq86yFtsJsdSWRcwf4tfmLMbtCwtOPxzDAOmFbpNPJ8sYBnNOS4jSqQcJnfeLKPrMILYsRyFSnpRQ7xqWUc--npkrpm4F-LhUzcWMYGrAysDrnvW-6EQ8iB3DuMKa_Ruk3GcCwoek-U2nisKA-NOMvjwE1ink58BJsFiwJ4XLmcVlYHJPEvXPN29VFOl2jDMXcS2_ga2x774jroxwaYDz9-R9AKfaftNA9rBCXPmhLR4uFET7HQWg8s214w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش وال استریت ژورنال؛ جان رتکلیف،رئیس سازمان اطلاعات مرکزی پس از آنکه ایالات متحده اطلاعاتی مبنی بر آمادگی مسکو برای بسیج نیروها و برنامه‌هایی برای آزمایش عزم و اراده میدانی ناتو جمع‌آوری کرد،وارد مسکو شد.
🔴
به گفته یک مقام امریکایی، رتکلیف ممکن است با پوتین ملاقات کند تا هشداری مانند«ما می‌دانیم شما چه خواهید کرد، و بهتر است این کار را نکنید» را به او ابلاغ کند. همچنین گفت و گو‌هایی در مورد کمک اطلاعاتی و پهپادی به ایران، آتش‌بس در ایران و مشارکت دادن کرملین در مذاکرات آتش‌بس باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143774" target="_blank">📅 21:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143773">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
العربیه: کابینه عربستان به ریاست ملک سلمان بر اهمیت باز نگه داشتن و ایمن بودن تنگه هرمز و باب‌المندب تأکید کرد
🔴
این کشور از راه‌حل‌های دیپلماتیک پایدار و آزادی کشتیرانی حمایت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143773" target="_blank">📅 21:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143772">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143772" target="_blank">📅 21:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143771">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات رسمی گزارش داد: زیردریایی‌های بدون سرنشین آمریکا تنگه هرمز را اسکن کرده و بیش از ۱۰۰ شیء مشکوک به مین را شناسایی کردند.
🔴
ارتش آمریکا با شرکت‌های خصوصی برای خنثی‌سازی یا انفجار مین قرارداد بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/143771" target="_blank">📅 21:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143770">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYx7yy0cmMSl3JXv5VcD8qx7kPIAU24nabfJHkih5Syqjnv8_gbpZZ60xdVNbjMENK3fUOcdtls7yAHy1ZcNNvlTv5PGvTJ-P5cwxDRYAgyaJWvDgSZ_DCbjITpZ7VQ3Dwuh6ikLNKsh7MdPHYuYjJPUd0LbSfSTErj7HFrQTHR4f67n-FpMBLLvriUcYkd0R__fwxMYBDIy5a9HJpXh9RPq5fEH5ivoBynWPnZzucD4hfzjgUSr-Ru3O-DGNuHJlBCTQ7A5dLrCllCQNk0KJUA2rIOznTeMGZDqARZzCKwpbhWrzCS8pqMDBpMN8xNqKtnoULZA4_8lEf_ngxSvCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روابط عمومی فرودگاه مشهد: پرواز تهران به مشهد هواپیمایی سپهران هنگام فرود از باند خارج شد اما مسافران و خدمه در سلامت کامل هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143770" target="_blank">📅 21:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143768">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
کانال ۱۲ عبری: مارکو روبیو، وزیر خارجه آمریکا پیام‌هایی به اسرائیل منتقل کرد با این مفاد ‌که انتظار نمی‌رود ایالات متحده حملات جدیدی علیه ایران انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143768" target="_blank">📅 21:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143767">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رویترز: حمایت آمریکایی‌ها از جنگ علیه ایران به پایین‌ترین سطح رسید؛ تنها ۳۱ درصد موافق اقدام نظامی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143767" target="_blank">📅 20:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143766">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i3CUmq1kY_KW2mS0CLWDaAwRflgwz2opzar4CWcScIsr2XzZxFDqqoeWqGT0gwRBr-aynkacKtf7dDW1XCSSdLg7NxFsVild0Ymut3ssOWAzeIIEEyEqH3-Yg9NV2o48L_IlDxzA0y1hfDiljf3DNJ1nNCv7NE5RWb5AU8oTwuyL2oAr7UrcW1qpJFIAxaX9PTzaYJWuq7NxGwt_2SrTJwYUmJjsJ9hW-tOACiYS6fE_C_QisWFu9H0-G3AB3Lg8xCaunNQ4ECgjivow1fNo8_Qe39Tx_b5aMXo0QpyCzeuMJFiBWWZuTYsEZUSi8lMx5a9p8g23bR6vmaiKPnSSEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز حداقل دو تخریب گسترده توسط ارتش اسرائیل (IDF) علیه منطقه المانصوری در جنوب لبنان صورت گرفته است.
🔴
همچنین چندین رگبار از ضربات توپخانه‌ای نیز به این شهر هدف گرفته شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143766" target="_blank">📅 20:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143765">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geu-FbajKa8Yneie7tTt3AW6Fv4VPAERS-LEjMmodNa6Xpy8QiIm6iEPpfKCDzxMNjB-6LJXTSUKsY_I7UDA-Sol9IwTAo6gWvDrggtbtySkc5wIFjBThg8EGe7ZV04NFmLubGYNlzaui0BF3wWw8JK36HXhasOf81ZXdqDzrLgyV-ckrxAsH2_g2VtPI7aoEHxwxKr0jwu53V8O2OqUEE_6iK0WKj9pbzQ_JGTKujS2EQHOr2QTYWyXlO7Uz6kHLXHVX7C7eWoFevf019tCE8AebPCPzlNPsQB0qGcapG1eJYMByI2o9TST424dz1X7AVEACPi5R21skj30lp-zeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوه دهم رئیس جمهور ترکیه با نام «گوزیده» متولد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143765" target="_blank">📅 20:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143764">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab64273b10.mp4?token=UnCSbY41FDP1U16-jZfGt7QyZ7DaJeMV7BSvjvsOTcSC9z68P6v1IH3mOKnlzzUtZdO6C5EarY9mkrxTOHP5J4k5L7OoOuwZtcWpdmTBTkDL8h2kIi8QZ6-T5p_27vy9d6vMnKlgO251vNSZ3XPGDrLcqTjwvJGWoQXEHdpZvO-FpErKz3qh-DdRSWasOnXhzEOVRwQIJWRw6k7d7ol0baetX06i0TL8WrgmzBApcW-pPA3UvwLYAxTiRcqdlzvi1o74Wh98e7RArTa6PHiqeN2zTMcWKdpKZgCOkW1HPThBXN26R9Wwwl8Ph0uGv-ye8EG-Jvu_r8zRKSTWXveWow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab64273b10.mp4?token=UnCSbY41FDP1U16-jZfGt7QyZ7DaJeMV7BSvjvsOTcSC9z68P6v1IH3mOKnlzzUtZdO6C5EarY9mkrxTOHP5J4k5L7OoOuwZtcWpdmTBTkDL8h2kIi8QZ6-T5p_27vy9d6vMnKlgO251vNSZ3XPGDrLcqTjwvJGWoQXEHdpZvO-FpErKz3qh-DdRSWasOnXhzEOVRwQIJWRw6k7d7ol0baetX06i0TL8WrgmzBApcW-pPA3UvwLYAxTiRcqdlzvi1o74Wh98e7RArTa6PHiqeN2zTMcWKdpKZgCOkW1HPThBXN26R9Wwwl8Ph0uGv-ye8EG-Jvu_r8zRKSTWXveWow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان خطاب به اسرائیل: جمهوری ترکیه کشوری نوپا نیست که تحت حمایت دیگران تأسیس شده باشد، کشوری نازپرورده از سوی کانون‌های قدرت جهانی هم نیست و حافظه تاریخی خود را هم از دست نداده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143764" target="_blank">📅 20:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143763">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=sVrmkQ0Ssz7Q3xUxsE7fy3BA_LkovnESBaGXq486UW7sWAd9rOYLxjv6tMmGP9B6_FFyc8n0ayEtJlxMfHD4Iu4ZlXYVdofhmFSfjPcS1FCDYrUzwqXof8hNLS5n8hDvAFUWpzwK_wKoGfNXGDi6mosVU-W1DiQYTiuozeC73TJ5NPNOCxSzuoGD-yZYfkOT9g0LbAKFzswqHR5cVfHnta8jRw81TJqVkgLMKZdi84L1QOPgwH6xYKMI-U6M6SJX_eH8FPy88UJhCdUrYdwhflPZIIeVF4f0bGIUHFpimUJlh0X654-Xhv2IEvILzq1ebekSMrrzkag83r8-TOREHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=sVrmkQ0Ssz7Q3xUxsE7fy3BA_LkovnESBaGXq486UW7sWAd9rOYLxjv6tMmGP9B6_FFyc8n0ayEtJlxMfHD4Iu4ZlXYVdofhmFSfjPcS1FCDYrUzwqXof8hNLS5n8hDvAFUWpzwK_wKoGfNXGDi6mosVU-W1DiQYTiuozeC73TJ5NPNOCxSzuoGD-yZYfkOT9g0LbAKFzswqHR5cVfHnta8jRw81TJqVkgLMKZdi84L1QOPgwH6xYKMI-U6M6SJX_eH8FPy88UJhCdUrYdwhflPZIIeVF4f0bGIUHFpimUJlh0X654-Xhv2IEvILzq1ebekSMrrzkag83r8-TOREHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب ترین سارق خودرو تو ایران:
این آقا بلاگر معروف اینستاگرامی بوده و عاشق ماشینای مدل بالا بود تو برنامه دیوار ماشینارو پیدا میکرد و به صاحبشون میگفت برم یه تستی از ماشینتون بگیرم بعدشم ماشینو میدزدید می‌رفت باهاش دور دور میکرد بعد از چند روز زنگ میزد به مالک ماشین میگفت ماشینت پیشم امانت بود و صحیح و سالم ماشینو تحویل میداد به صاحبش
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143763" target="_blank">📅 20:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143762">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fz6DdScRQkElGbGi3UOYs0W_0tcWN0dItsqbOZ87OGTNrcv9eznnMlRLV7NN24FAShz-7p5Udz43jabl5Qt8CWkCRGiuFlM1ytNnnAWcOSfchJ7lsLy4stPM89-ZsDBXLhbYEOzydO9ldpfow1bluK4HWfzZxwJrPSR6zJK0ksMugFMNXK7DN9FSN97ER3dI2VdEzQdZB1HsMKKluaocpGMikeCtBDb7B-_cKrgZxAY_pXQ-6MCJLv4GIfM8mA2hdR8v23neIeg3onyCOCEYwzEjECHU2DuCjS5znlZowmLKhBfSRNiGNWvvB7_aAUcbeTHFpJa3osLFQjhdVVbOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور خارجه عمان، بدر البوسعیدی
:
امیدوارم به‌زودی یک گذرگاه موقت برای تنگه هرمز و چیدمان‌های عملیاتی برای بازگرداندن ناوبری ایمن اعلام کنیم.
🔴
مدیریت آینده تنگه و راه‌حل دائمی در زمان مقرر، مطابق با بند ۵ یادداشت تفاهم اسلام‌آباد، دنبال خواهد شد.
🔴
مذاکرات با شرکای منطقه‌ای در حمایت از صلح و همکاری، ثبات و آزادی ناوبری انجام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143762" target="_blank">📅 20:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143761">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aEHeO0CZE7Yr0rjUeflOAqGhC70TZrbJSS95PcDZbAldjm0dk1zbYy7cWkeF30U6aYYSz2-r8QejreFXC6Qwvv41Lv4yzyQOIZIx1WgQ_gNni25EA_Q9LZARoIOb_w2q03_YPtsZ9_dv7V5jS5orY2_JRb6_NoFp_defnjL9VvyFoQi6dP1qknxquWQgytjSNvgPanQKw0OgdeMftpVEXkSTuW2-2oM7UVrIirs3BajHTZda96ibDAMAiogjPDMT-gEZDt3M4lym_p76yHzDwCJgmn-LiYw6Ml0d7qg-9jfC_KbUvbYaSMqhVh0GCp5a2aTmFqM7KNqTSzG0myCYpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیما سی-17اِی گلوب‌مستر III متعلق به جان راتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (CIA)، از فرودگاه بین‌المللی ونوکوفو در مسکو، روسیه، حرکت کرد و در حال حاضر در حال فرود در سمت ریگا، لتونی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143761" target="_blank">📅 20:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mW1EG1u1jFap5LoLpm8h1qneYbovnJTHU13L-aI6OFIUxDxW_DQLL0qWf1KOCD4M4_MHrn0A3Vh3Xjzb_bWADmZbStkkLCzHbdCy5eLpYwS2JgQMmFplS5OBsdPYvgofsi_3pXIGpmOcLY3eIZowZHXcp84Idl1C0Xwhs91lfeYl76jgJuYoZGlbnxqdL4xZ6Dwz9PgBo1J-CslImzIuL2SCI_AXk_mCcJK7wo8L2vpwEEgohgsgH_6AH_rpH8X5CmFDsIy1R6LpzkLphE9jVB_yTzBnwA4jnoeAMwo973as_kAKzLj-zxF11zJ1ZQYJS9tzn5wzy7QTE1QITtb5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E9-kwa2QRnGYfdsFWgocSA0IJSmO0viEJKiLSamnigZ-gVHLEVLsoH_P8DTpPASslBG5ZcWLkz3gin5ug38rZSNUcw8RMS1rKH5dH3nr4GcjQqoXD3iKxy_WO_3mOJaAE_Z9nmwEt3XDCW1mqMhEJMxxmyI6Lu2H-ZJuG1iy3zPECXYSM3XBX06wEwXtt0Uzo1F7x_qlrLp6R_XKZqIooO9k_2xh2IaWzz1-M0PparKPykkZL6Qs6FrtwtD031-8v90zqZ01V5AODKw0TqvuT-w-hHO6Fq2L9bxYyav_gX47OhuAavG9BDvWMGswgP6HO9HrzP6c67rUAfirgsSb9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U5GvQDcO6DKjS-6LhgRhznZboRjBnrijsnMtYWzDkrUzV1063cMMN0BnL7yyxnt72DQE83LjEhysJo-uzlpKJoJc0OiO-9kwhPKGSuVsrpwUXTFmAzVGsz1nXsSQSLwGFn6KcQTJYx9WtoCRlVGBt3JVL7DJ33tAMtUqwCnzK4tE4L3U2hyDqI5oFT0vu88TbgJRqp-DDwXIEhfzjti5p4SC1d-kOXsJxMuEgJ13OiWd54NwTMi9S_kU2GgZ5WQWrDfTHPfUGVwUzvYzZHNZ0jEhEhrHvPTOesz-kG67Wje9SloYVV7ZilvKZ-tgT4mgksZe_M8HHdOrLe4eJGQyPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پست اسکانت بسنت، وزیر خزانه‌داری آمریکا: رهبران ایران دارند به چیزی اعتراف می‌کنند که حالا جهان می‌تواند ببیند: فشارها مؤثر واقع شده‌اند.
🔴
مسعود پزشکیان، رئیس‌جمهور ایران، با اذعان به کمبودهای اقتصادی کشور گفت: «جنگ بالاخره باید در مقطعی به پایان برسد.»
🔴
محمدباقر قالیباف، رئیس مجلس ایران، حتی صریح‌تر گفت: «هرچقدر هم قدرت نظامی داشته باشیم، اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید داخلی نداشته باشیم، دوام نخواهیم آورد.»
🔴
در دوران ریاست‌جمهوری ترامپ، وزارت خزانه‌داری به قطع هر شریان اقتصادی که این رژیم را سرپا نگه می‌دارد ادامه خواهد داد، تا زمانی که تهران تنها بماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/143758" target="_blank">📅 20:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143757">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kb190pdnqN8CGzc8Qynrvb92vAkSHtR_G2HT6_TfHG4L_jbMWRB7wOGXHTSLjjBCE1JB7Pv1_hvAwLsuUgRla25zM1G1iSgWUOaY31o_xjHcx-sVpk3pJHBmTJQQxBsL_8j8JtczE7vb1YrgyE6hsfWDVUwVapJ6CUn87OvcvYtvZexnq2N3aU07rIppXBBoMoYX1U_tj733RtIpOxNYfQ8dkjwYPo8xNdEUSO_xf2tHQJCf5dr4Def1TqKDLZiKqJXswQHuLVI_dcrGSlzZjOHbnuTc20YMVZObMLZp2ZzL9iJIbku4hVBe8lPy1A_zqraWJ5crrTTK1f0E1SsMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهاجرانی، سخنگوی دولت: تاکنون هیچ تصمیمی برای افزایش قیمت بنزین گرفته نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143757" target="_blank">📅 20:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143756">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
اکسیوس: روز عملیات اقتصادی وعده داده شده ترامپ علیه ایران با شوک و هیبتی که وعده داده شده بود همراه نبود و در عمل به یک اولتیماتوم تمدیدشده دیگر تبدیل شد
🔴
آزمون واقعی، چین خواهد بود؛ کشوری که حدود ۹۰ درصد نفت صادراتی ایران را خریداری می‌کند
🔴
موفقیت عملیات «طرد اقتصادی» با این سنجیده خواهد شد که آیا ترامپ حاضر است این تحریم‌ها را علیه کشورهایی که بیشترین اهمیت را دارند، واقعاً به اجرا بگذارد یا نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143756" target="_blank">📅 20:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143755">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilA6Xp4NzzlFjDSWi5lmTdzy5rdTAQApO8HB5w5YCAQPtRFCmat9JVSYH2CXLHgCf42tnTQkP33mq-RD-03tKbQ7-cpDoMslQ0GVMaFICjyT5LmjN_vY4abUdJCAQsc8P10Lq-3yNrfO1nWC5JrDwCl9tBpzR0mP1dBIlf6e0UNbID2i18a1I6sZsDTs1f52obWt7CbufS25YcM1b4hvEf7Sh4wXTQPxHkM1yhyaQuh9hkiHfjUhw2YgdQ8lkOpKM_Oo8UfZpIboWzDmMELZaG1qJycrsQ4pNc1P5Kt-rAyg_UOPMdIOxXz0nIyLASIVWi1ozw9d9x3VNmlMkxzwoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بازنشر کرد: «آمریکا در آستانه به دست آوردن ثروتی عظیم از خاورمیانه و منطقه خلیج فارس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143755" target="_blank">📅 19:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143751">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQu_NRpltrVfNGojy5i9ZO8gdUmGPlGnnsrE3oLG6hAv0kki-xYQ3lZaUmRXB2view2bNU8uOPerjCe7NXDUCujbD4vGc_alspDNUwVA63hfAida8uDKEr5PWGWisy723m77X3OMgatIRWLun_jb49JArtPB-rqZ0pMfqRHXyL-HJSntxFuMrY-sw3CXxYoa-qsgXMaEa5QK5gaFll60nwB1ovMd75mEabgqSiUUuLN3L7C1S88Z7GFT0adViZdgYRWNtAJN6TzUTp6Wd3E1eMNz1x67loa6qgYNZ2BfVTO6BehVj3LKq7gzbJfEoCgf7JNOlwCAajTnFGr2iQfMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hHoahQ0ItICYyRmg254eaiV5RoJJKhfsjH0r76PEliiLdaNI10AfhhUnhYXBm81zZMuxUAJNmUb6lS8Ab53C65Mwqy8u03n36_ax3hshQzy33OHdWlysjgPTzuBPJGCBatfgNcnQEw8O_YtrULjxgMxKzHRT0X0JFR4Y6clzNbluOE--Vs6w9YGsfxWHCkmzicYn9ih2QRiEv6SluDLBIll_a4BfZ_b3FCmkxm2TCfBDjllD4ERxj6yChWL_QmrWpIeg9J5kSnWytewjzN5gPVB_Ihkg51c0ij9ptIE1oIOkmJ8MJd4W2CW0Ed9-5lLu0Nua_dew1-1DLcCEz9El2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltHcq6zTR8FA-FmtelMpLVZM2PYU6ibIMqZDwISgq_RoRdkgfQpN_MO8Ve090JN_aqPtc-Da-Y3ZrXMONk_4WLsL09kaMURdFxZGKybB7rlSHUFsom7zo9-If8VMDerVEIT1MNEuPHqaFsdiu_pIFZus8mJyqqRAX7qn2aQJaau4fzoAowBn-SyTEH5eLCS0KAmSrTuAjR4oKg3vwqD593RAc1Nd3OhUNQwKjzowIvGIrDxzkN_68GpsQNxsQYWONjV3WpqPCFBMpVCKpDqYvu7RZRt6GjOeeEKY5i2ljCRScLAbPPs-IO5EeimRmE6evzdakrVAX0HuAsnD8trMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVMcOsYD60cCwLHgEm67R07HxbRkiFAk3w1CwHEeBL5S7qWAa7gm3Mushq7LuUp6_lvAe2eVh5gxGvucZlXKOWQGG2n_ogsU8PIGosFQ2IRSSc3UZs0URyzbjwERD0efFGQCD72zXVLkWugoMSLIqaoGchE-QLku5qkLlvWGLu6oQy7tvcxkGUEF4EqEZlGj4Xor70JrDW7HXvYH-t-E0joBFS2C6ROV5TbaLsrfYoMxeu0e7C7XwXMbBj4hYcRKqZcs8k_elMqoF9VXo6dL-GrOFPgxbMhnGb0vlefLED1BKQq0oKXTuZWgqVeNIzri-r97HW_NaQt3zFeZR1iOxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار رئیس شورای عالی قضایی عراق با قالیباف
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143751" target="_blank">📅 19:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143750">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزیر امور خارجه اسرائیل: به دلیل اقدامات ضد اسرائیلی دولت هلند، نمایندگان این کشور را از مرکز پشتیبانی بین‌المللی غزه اخراج می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143750" target="_blank">📅 19:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143749">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
دونالد ترامپ لحظاتی پیش مدعی شد: آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/143749" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143748">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏
👈
یک مقام کاخ سفید: در حال حاضر هیچ مذاکره یا گفت‌وگویی با ایران در حال انجام یا برنامه‌ریزی نیست
🔴
‏یک مقام کاخ سفید در گفت‌وگو با الجزیره مدعی شد: در حال حاضر هیچ مذاکره یا گفتگویی با ایران در حال انجام یا برنامه‌ریزی نیست
🔴
‏محاصره دریایی به طور قاطع و مؤثر اجرا می‌شود، تنگه هرمز باز است و مین‌ها جمع‌آوری شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143748" target="_blank">📅 19:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143747">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/209cb6a4c3.mp4?token=lgcXbmXTYIH6JXNlvzRjr77slNNQp79CAi1Q94ivyzgkMwA3spILdOGWYafXXUO_yVanLa7iU4Vct2saGyAAEcuOUm7kjnvqR8tfRpWmHXGKH2pm0sdjdV--zJj9lSm8rn5aY-Rmk-LqvBWmykvBKbUVBODhCCuwzU-vTgxeCcdsn6JLmM37DBX63P9-t185G9VquZA9kibU-ZIlZJteKeTyD1GCSc8CTRTlCeTEWE2YoMJcpIG1RRbZamdZgSfF-l0i4N3e6zAf9sosyq_-6CCRnialyVEdnCpP8lVWiH90ud2kJgDAq37GOwwC6c26ybpz31Fr6v6LFa5s_b6lyF7lQRz42cRsdUtpDAnr65m_4JPD4leFcfEk0lPwu2pIAAK_fZpOKIWRlXJgQBia4-sHCGkNGX3cydw4cTsxoRTp0xF_HZbWVYID_Dh5gmW-89TeQ1IY62C9F-PJQFiX5v8kFyQ-aFbA80oEF7FB_OjZMWtoo4rguHNSqGBf9kOvTdn5_zUNNdftrTdTKaXQQ7edSMM459CVbEK3AiSfPjfBfK8omkDfot92pDJBsJr2m2qecJqqJSEYLNfeQWNgDC-Fym1U18GnTHCzF6sKfLuiN6Pa_GTAkNGVbZqUBDxOF1Y3mzjQKWQxHkLE66-1cvHxaZJPG1CBg0MH6vW4ozQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/209cb6a4c3.mp4?token=lgcXbmXTYIH6JXNlvzRjr77slNNQp79CAi1Q94ivyzgkMwA3spILdOGWYafXXUO_yVanLa7iU4Vct2saGyAAEcuOUm7kjnvqR8tfRpWmHXGKH2pm0sdjdV--zJj9lSm8rn5aY-Rmk-LqvBWmykvBKbUVBODhCCuwzU-vTgxeCcdsn6JLmM37DBX63P9-t185G9VquZA9kibU-ZIlZJteKeTyD1GCSc8CTRTlCeTEWE2YoMJcpIG1RRbZamdZgSfF-l0i4N3e6zAf9sosyq_-6CCRnialyVEdnCpP8lVWiH90ud2kJgDAq37GOwwC6c26ybpz31Fr6v6LFa5s_b6lyF7lQRz42cRsdUtpDAnr65m_4JPD4leFcfEk0lPwu2pIAAK_fZpOKIWRlXJgQBia4-sHCGkNGX3cydw4cTsxoRTp0xF_HZbWVYID_Dh5gmW-89TeQ1IY62C9F-PJQFiX5v8kFyQ-aFbA80oEF7FB_OjZMWtoo4rguHNSqGBf9kOvTdn5_zUNNdftrTdTKaXQQ7edSMM459CVbEK3AiSfPjfBfK8omkDfot92pDJBsJr2m2qecJqqJSEYLNfeQWNgDC-Fym1U18GnTHCzF6sKfLuiN6Pa_GTAkNGVbZqUBDxOF1Y3mzjQKWQxHkLE66-1cvHxaZJPG1CBg0MH6vW4ozQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرانک-والتر شتاین‌مایر، رئیس‌جمهور آلمان، درباره مهاجران: حتی اگر برای مدت طولانی نمی‌خواستیم آن را بپذیریم، آلمان از مدت‌ها پیش جامعه‌ای شکل‌گرفته توسط مهاجرت بوده است.
🔴
به‌طور قطع از زمان توافق‌های استخدامی دهه ۱۹۵۰ و ۱۹۶۰ با کشورهای جنوب اروپا و ترکیه، این‌گونه بوده است.
🔴
اقتصاد قوی ما که در دوره‌های طولانی رشد کرد، مردمی را از سراسر جهان جذب نمود.
🔴
و حقیقت این است: ما به بسیاری از آن‌ها نیاز داشتیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143747" target="_blank">📅 19:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143746">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1be7038459.mp4?token=JN0cc6XAJ2KTnFT12C0ZTO6arMaE5NslB_E1XgFtIGAV_aMWCu1RtYhVkOq7tq5E4CQCJtnmBtKk23woa2Fg70l0cAE3hQr0-TYVt-aceFHVrZOSHRfElOC31lnABRrNlW3pnw03LScDtHTMMJfiZnSnvsddzQ7fpf-DO97xI_OHjwADIsSmhCclZO6F0quCcKYd02e7ZxxIutEgdrJk-L6XFSB-Nipk01Fk6Mozkf-F17J_yl9mpn47H7uAP_xvpxhgI_Hl03R7me6KQGaWINcSfb-O6lIsUW4Lc0B9iCMxAu25_yuFj0oQgK3PtjaMAGclHMibTXo_5TbTsPViMjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1be7038459.mp4?token=JN0cc6XAJ2KTnFT12C0ZTO6arMaE5NslB_E1XgFtIGAV_aMWCu1RtYhVkOq7tq5E4CQCJtnmBtKk23woa2Fg70l0cAE3hQr0-TYVt-aceFHVrZOSHRfElOC31lnABRrNlW3pnw03LScDtHTMMJfiZnSnvsddzQ7fpf-DO97xI_OHjwADIsSmhCclZO6F0quCcKYd02e7ZxxIutEgdrJk-L6XFSB-Nipk01Fk6Mozkf-F17J_yl9mpn47H7uAP_xvpxhgI_Hl03R7me6KQGaWINcSfb-O6lIsUW4Lc0B9iCMxAu25_yuFj0oQgK3PtjaMAGclHMibTXo_5TbTsPViMjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور آلمان، فرانک-والتر شتاین‌مایر: ما به عنوان یک کشور به مهاجرت نیاز داریم. اگر بخواهیم عملکرد داشته باشیم، به آن نیاز داریم.
🔴
این موضوع به بیمارستان‌ها، خانه‌های سالمندان و مراکز مراقبتی مربوط می‌شود. تاکنون، این موضوع به بخش‌های بسیار بزرگ از اقتصاد خصوصی نیز گسترش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143746" target="_blank">📅 19:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143745">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
بیانیه مشترک مطبوعاتی ایران و عمان:
رایزنی‌های وزرای خارجه ایران و عمان بر اهمیتی که هر دو کشور برای از سرگیری دریانوردی ایمن از طریق تنگه هرمز، با حفظ حاکمیت و حقوق حاکمیتی خود، قائل هستند، متمرکز بود
🔴
دو وزیر با توجه به وضعیت کنونی در تنگه که ناشی از جنگ اخیر و پیامدهای فاجعه‌بار آن است، چارچوبی مرحله‌بندی‌شده را مورد بحث قرار دادند که می‌تواند مبنایی عملی و قابل اجرا برای پیشبرد امور فراهم کند.
🔴
چارچوب پیشنهادی شامل ایجاد یک کریدور دریانوردی موقت مشترک از طریق تنگه هرمز و توافقی برای اجرای یک پروژه مشترک به منظور پاکسازی تنگه از مین‌ است. مذاکرات فنی میان دو طرف با هدف توافق بر سر یک کریدور دریانوردی دائمی و اداره آینده تنگه، و همچنین سازوکاری برای تبادل اطلاعات، مدیریت ترافیک و ارائه خدمات دریانوردی و امنیتی مربوطه ادامه خواهد یافت.
🔴
وزیر خارجه ایران و عمان بر اهمیت برگزاری گفت‌وگوهای مشترک با کشورهای منطقه هم مرز با آب‌های خلیج فارس تأکید کردند. آن‌ها همچنین بر لزوم رعایت حقوق بین‌الملل قابل اعمال و احترام به حقوق حاکمیتی کشورهای ساحلی تأکید ورزیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143745" target="_blank">📅 19:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143744">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwQ6jWHKGi0K-JT9ZhJavaFicYdZmGvQqGP2pkZwaHyKXO_YCO3ZMxa_kvGjWkwRoVHgmry6kvAZycYYeSQdEeEORUci2KTDF1hr9akjJrPjoWfKta32X8IZsU9HoBDV4hZABHoACGhBm8WQU-fvXIuyYk-k1gGlBgOQi5uFdXpK0BmSq1QCCqR8g03oWoaxNjCfTMQbAhWA6Ih7avZPtToxaNNrFneGTWxEypf-n1rqdISt1kVn-n3CR0cuPiQ0pA13vucewv5NLwhif8M06cCzvkbk1AJiIf1xsLUu0p79JnHHb4HZp_Wg-jorRNxKLolG5QJRm_8KEtKbnjNSEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده ولی فقیه تو‌ سپاه:
آقا مجتبی خامنه‌ای رو
خدا
انتخاب کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/143744" target="_blank">📅 19:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143743">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
الجزیره انگلیسی: تاریخ نشان داده است که تلاش علیه ایران دقیقا نتیجه‌ عکس خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143743" target="_blank">📅 19:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143742">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d1f210ee.mp4?token=aj2EUhaFWc_N1RZw_duAs7uVJoCn1bkYRo6ClHyI5WIgRFWZwjF0Uf07YKEc0oYYo9-hZp_GHpgJCOAyErMTrbLt6-RrmCVlLB23qjWPkKIhO01HG1Ttmr13ByXZXMnQBuwUQ-dQentC2YrWMg0KJCiwyTEYL8DbFIpJcweTslN97JZ61JWIx9w2TOUZ-EtOuL2lGntnR3HiLjO6NI5jhXCYwyYSRV_bv0BJ2V1fEYeDYlnNmWkQpQA41f6v6-_GDrR51c7jcsuen7PotWzuE_n9DOiE9kRNxc6LyRoov61iBDTyMkoPNDvWYdyn7FUdYe0_pfRpGgvD_CEDv6Bz72Nau71ktzEeBF3V-gSfSDv1gN4atZdQsVt3-bPdtaWQd72MRxBm7DKcKgeLS4hal-HQF1KYE8a0N3me-i0AB8c7LTbXv1RnH6iQLgT_JX14RM3q3FYctRW8eWFy3Inv9dFD6dpjMIUXAYBXEbKVC4NrI5-Df23TibutUC5eRPcO2LQtnfJ9_EVnCsqzw1civ2ixgGAoUXv0Td5hBcekmjcX8nBjC5CMM-KMpQ3Bm-50vrJCYoJzFA9vEKaSpGvNZBiRJp2B0LpMTA2Qef4RY62yJKzRSTayzNnAm6CzPH1BhU_YsxkWJndjrtie6axqDARvifXj_0jFT0DdtIaEOag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d1f210ee.mp4?token=aj2EUhaFWc_N1RZw_duAs7uVJoCn1bkYRo6ClHyI5WIgRFWZwjF0Uf07YKEc0oYYo9-hZp_GHpgJCOAyErMTrbLt6-RrmCVlLB23qjWPkKIhO01HG1Ttmr13ByXZXMnQBuwUQ-dQentC2YrWMg0KJCiwyTEYL8DbFIpJcweTslN97JZ61JWIx9w2TOUZ-EtOuL2lGntnR3HiLjO6NI5jhXCYwyYSRV_bv0BJ2V1fEYeDYlnNmWkQpQA41f6v6-_GDrR51c7jcsuen7PotWzuE_n9DOiE9kRNxc6LyRoov61iBDTyMkoPNDvWYdyn7FUdYe0_pfRpGgvD_CEDv6Bz72Nau71ktzEeBF3V-gSfSDv1gN4atZdQsVt3-bPdtaWQd72MRxBm7DKcKgeLS4hal-HQF1KYE8a0N3me-i0AB8c7LTbXv1RnH6iQLgT_JX14RM3q3FYctRW8eWFy3Inv9dFD6dpjMIUXAYBXEbKVC4NrI5-Df23TibutUC5eRPcO2LQtnfJ9_EVnCsqzw1civ2ixgGAoUXv0Td5hBcekmjcX8nBjC5CMM-KMpQ3Bm-50vrJCYoJzFA9vEKaSpGvNZBiRJp2B0LpMTA2Qef4RY62yJKzRSTayzNnAm6CzPH1BhU_YsxkWJndjrtie6axqDARvifXj_0jFT0DdtIaEOag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیر سازمان ملل متحد گوترش:
به شورای امنیت نگاه کنید. سه عضو اروپایی در شورای امنیت وجود دارد.
🔴
خواهید یا نخواهید، روسیه یک کشور اروپایی است و اروپا [سه] از پنج عضو را در اختیار دارد. منظورم این است که اروپا سه‌پنجم جهان نیست.
🔴
هیچ عضو دائمی آفریقایی وجود ندارد. هیچ عضو دائمی آمریکای لاتین وجود ندارد. یک عضو دائمی آسیایی وجود دارد.
🔴
اما از سوی دیگر، واضح است که واقعیت‌های میدانی، در نهایت، باید حاکم شوند.
🔴
بنابراین اجتناب‌ناپذیر خواهد بود که شورای امنیت مجبور به تطبیق شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143742" target="_blank">📅 19:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143741">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6f741c16.mp4?token=IGIm8Ey5bj44YNsmN7NKE15JN5Lf8VPzMD_Jt8wEj3XnPwI4oebEy9Lccd4V6huTP8Wz6wwaEDC9AdDrjc7e9IVVkIEKCYRWlxHVGMaeSBFpWi-ophqiLUNU4oLGMzPe3BuW3WeYfEglMSpeME_k2OQWLD3CHry-Hx9bZ5-0toC8ePjgnigFDWBmLNKt644QN3HJ9KF-8JNYnh8RuTMgv3C0KWftHndxtoizkVj2XO-8dm5RS9iuTqiK_aOO3D1cUellmI85PsBC1mj_I49-g7ELSqJTWC6PpzkkumE8Bphv6aVbtv_xDlGQxCUpKc-r9ly2jl5M2BoQxZuGjKfbJ0aWzSt6ZN03mIjuLADVJNkZHYyJ4Yikive7Mu2EdXuACOcBRTxkpI7IENfdwW9yCMW4jB1RVlZ-RO9NzJz92-GJaTimf9-B-Rucbx3mKpvUkoV55C64vdPGoFPac4kTbSytJuFsfNwryDujuBSmg0ISO1tjUqwkvz5VN0rThtz9SmTCyg2t1njnVdkbVSPqI9YFa0nZgOV9G_GnmyMp9T1jc1uSDbLGx9nh1m-JtcCumtUwsRonrfEfqGCk8xR_rS_fARR5xcO60K-MK5c-gESQDf1Ck7aDmCLF_x-yC7sEhzCfWMSIW8kCRGc7KxBJgOYO4d7GDi0boT4jSZJVpF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6f741c16.mp4?token=IGIm8Ey5bj44YNsmN7NKE15JN5Lf8VPzMD_Jt8wEj3XnPwI4oebEy9Lccd4V6huTP8Wz6wwaEDC9AdDrjc7e9IVVkIEKCYRWlxHVGMaeSBFpWi-ophqiLUNU4oLGMzPe3BuW3WeYfEglMSpeME_k2OQWLD3CHry-Hx9bZ5-0toC8ePjgnigFDWBmLNKt644QN3HJ9KF-8JNYnh8RuTMgv3C0KWftHndxtoizkVj2XO-8dm5RS9iuTqiK_aOO3D1cUellmI85PsBC1mj_I49-g7ELSqJTWC6PpzkkumE8Bphv6aVbtv_xDlGQxCUpKc-r9ly2jl5M2BoQxZuGjKfbJ0aWzSt6ZN03mIjuLADVJNkZHYyJ4Yikive7Mu2EdXuACOcBRTxkpI7IENfdwW9yCMW4jB1RVlZ-RO9NzJz92-GJaTimf9-B-Rucbx3mKpvUkoV55C64vdPGoFPac4kTbSytJuFsfNwryDujuBSmg0ISO1tjUqwkvz5VN0rThtz9SmTCyg2t1njnVdkbVSPqI9YFa0nZgOV9G_GnmyMp9T1jc1uSDbLGx9nh1m-JtcCumtUwsRonrfEfqGCk8xR_rS_fARR5xcO60K-MK5c-gESQDf1Ck7aDmCLF_x-yC7sEhzCfWMSIW8kCRGc7KxBJgOYO4d7GDi0boT4jSZJVpF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیر سازمان ملل، گوترش، درباره غزه و اسرائیل: من کاملاً با ایده تعصب مخالفت می‌کنم. برعکس، فکر می‌کنم ما در سمت درست تاریخ قرار داشته‌ایم.
🔴
ما از آنچه برای رسیدن صلح به خاورمیانه و امکان زندگی مشترک دو ملت ضروری است، دفاع کرده‌ایم؛ زیرا، منظورم این است که دو ملت با چند میلیون نفر در هر یک وجود دارند و هیچ راهی برای نابودی یکی توسط دیگری وجود ندارد.
🔴
بنابراین، احتمالاً بهتر است همه تلاش‌های ممکن برای آشتی انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143741" target="_blank">📅 18:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143740">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
دبیرکل سازمان ملل متحد، گوترش:
بسیاری از کسانی که فکر می‌کنند قدرتمند هستند و می‌توانند به اهداف خاصی دست یابند، در نهایت قادر به انجام این کار نیستند — و شکست می‌خورند.
🔴
امروز، وزن آن‌ها بسیار کوچک‌تر از قدرتی است که فکر می‌کنند دارند.
🔴
منبع: فایننشال‌تایمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143740" target="_blank">📅 18:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143739">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
اختلال شدید در سرویس جی‌پی‌اس در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143739" target="_blank">📅 18:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143738">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
فایننشال‌تایمز: دولت ترامپ از کی‌یف خواستند که در روزهای دوشنبه تا چهارشنبه، با موشک‌های دوربرد و پهپادها به مسکو، سنت‌پترزبورگ یا شمال روسیه حمله نکنند؛ این درخواست با بازدید برنامه‌ریزی‌شده جان راتکلیف، مدیر سازمان اطلاعات مرکزی آمریکا (سی‌آی‌ای)، از مسکو هم‌زمان بود.
🔴
اوکراین با این درخواست موافقت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143738" target="_blank">📅 18:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143737">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
خبرنگار دیلی تایم پاکستان: ساعاتی پس از بازگشت از ایران، محسن نقوی، وزیر کشور پاکستان و یکی از اعضای مهم تیم میانجی‌گری پاکستان میان آمریکا و ایران، با کاردار آمریکا در پاکستان دیدار کرد و در این دیدار، وضعیت منطقه مورد بحث و بررسی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143737" target="_blank">📅 18:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143736">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
طوفان تورم تو راهه
‼️
خبر مهمی که منتشر شد
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143736" target="_blank">📅 18:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143735">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJbf2a-IwlzkREVVbRpr9bLRiwGWwCdIPaG827rk2TU7LboFV97HD4BVSOMA6Dn0DM01DGfzLoMIm6qc7dJq_iRt-bqf0ys0LYLsMgWiqUm00FoiF7assXlYiUtsbL5VF8qGDRvRV1u4-kHmMqvzaqzZ06sZtVQLdxTn35aWI_ZC0FjA755gDjGJbbWbplpKcLerCZU0oWWVVpd0eMmjLqnt0Pu2UPU5ZeiItHT_2JItV9XiJeilQLTNpt7KDNyqCNEV5P0Z3T3RoPrXFEMIcvpZyU6BQ5P52S5MUAzWOrKYWWkqk6HEA9zvUN-stOoTzkcchY9zdZpTLCSmthll0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزیدنت ترامپ در تروث سوشال با انتشار تصویری از دریاچه اُنتاریو (مشترک بین دو کشور) واقع در مرز کانادا و ایالات متحده رو آن را دریاچه آمریکا نامید
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143735" target="_blank">📅 18:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143734">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh5jx3BJDwBRoPrTR10xMCToUA55ASHpz4A_4201FNhP4epy7Ij8E6mYVXHXJNL5O680G0E1Z-aRRWDDNEGpw-c4IbLHJHp-sID1hgwhKFYyKjhnqH9Xe_Fo2hgFeRFIPfLv-oeA4v6XAkq0UitSy26SGCvQt4J-fRKVVydUVdKTX23Cg8u3Evl-U8tsl-nDDfzOezZMCfssyAiMvCHhF_iyGjHmoKie653zdkItaM1AZCZ4MMdLgAZzo3AcBQi9lirIYMj6sv-20NH20aG4RCGp91nQpGM6GdvO_h1yxtM2Ds-TnqcnAbmFTeOEUzfTXcDzOmYsEDKCuPCnd-JIeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: در طول ۱۰ سال گذشته، ایالات متحده به طور متوسط سالانه ۶۰ میلیارد دلار به خاطر کانادا ضرر دیده است.
🔴
دیگر نه!
🔴
پرزیدنت دی‌جی‌تی
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143734" target="_blank">📅 18:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143733">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8n2546VxAW1fzt_IMxbDPNovvZh1tig_lVjb9_5QPFa0Exeio_3jZigENj_KyKvsYSdXi15mYH8Y-QCUxOm0lbMSGq2L3vC0hOmC5KXzyRaIA117QSE37i00Unbyr2eX8s-dJQBG8TzeUlu34mi7R-svV2BiEWgJaHlZCBtDevE_SAUevJa10UBsLq8ccXMuOnq5STMTDMtf2IUROyijGOOBuHQ7D1CLPxjh1vvWkaoI_O7-6X7xkNdPesoH7hCgy2udi3GVL3x0G0x3WpDEOEcWemG8ZOflJCDE74GsxgUYr8SYDVMxxnNC8C1U5yaNceSqNicwoospWF31mbO8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ چند ساعت پیش: جمهوری اسلامیِ رو به زوال ایران، حقوق بخش‌های بزرگی از نیروهای نظامی خود را نمی‌پردازد و هم‌زمان، معترضان را ــ حتی زمانی که در حال اعتراض نیستند ــ در ابعادی بی‌سابقه می‌کشد.
🔴
این یک بحران انسانی در ابعادی عظیم است و باید همین حالا متوقف شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/143733" target="_blank">📅 18:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143732">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
عارف: ما برنامه اقتصاد جنگی را ترسیم کرده ایم، اما برای جلوگیری از تنش در اذهان جامعه رسما آن را اعلام نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143732" target="_blank">📅 18:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143731">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFwUuLToZfus20Nq7CAKw0VG1aeV4qox18rev_FVQHf1YZd7V-IsM4z5qEuOIkEinnRObNk5R65vGMDIAh-QvN_Wqv8ALqPW552Ue_YWmj26npsmSuIepOuMvDB4rKLp12DOxIlaD7He-K8rV1F2qVNgcvqMOsCRQKLGkNiGVmW_WUyKehrFxyMgiNQ95sXOu1OEUxxQ42HQPoZZXcK_CGUYf-p7ddzDse6jRAJ08h-1vo1K-6lGuHG9c2yXiQEKrKEqvWBhoTzqd96k0j_iRlMnCj466hW5f9JXRQv5EMQ41vRSHvA9liLZ8zzLDjbo8Vc-BdgVwj7Zn3iRufzC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: به تازگی توسط نیروی دریایی ایالات متحده به من اطلاع داده شده است که همه مین ها از داخل آب های بین المللی تنگه هرمز برداشته و/یا منفجر شده اند.
🔴
به ایران اطلاع داده شده است که هر کشتی یا قایق مین جدید فورا و به طور سیستماتیک منهدم خواهد شد.
🔴
از طریق نیروی فضایی، ما در حال تماشای هر اینچ مربع از تنگه هستیم، همانطور که با کوه پیککس و سه سایت هسته‌ای دیگر که قبلاً ویران شده‌اند، مشاهده می‌کنیم.
🔴
یک خط مشی تحمل صفر در مورد قرار دادن مین با قدرت و اثر کامل وجود دارد.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/143731" target="_blank">📅 18:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143730">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری/ترامپ: نیروی دریایی آمریکا به من اطلاع داد که تمام مین‌های کار گذاشته شده در آب‌های بین‌المللی تنگه هرمز خنثی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/143730" target="_blank">📅 18:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143729">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
دلار و طلا ریخت
‼️
بیا اینجا ببین کی باید بفروشی و بخری
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143729" target="_blank">📅 18:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143728">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
خبرنگار دیلی تایم پاکستان: ساعاتی پس از بازگشت از ایران، محسن نقوی، وزیر کشور پاکستان و یکی از اعضای مهم تیم میانجی‌گری پاکستان میان آمریکا و ایران، با کاردار آمریکا در پاکستان دیدار کرد و در این دیدار، وضعیت منطقه مورد بحث و بررسی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143728" target="_blank">📅 18:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143727">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
از سهمیه ۱۵۰۰تومنی بنزین‌ها، ۲۰لیتر کم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143727" target="_blank">📅 18:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143726">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رئیس سازمان سیا، اطلاعات مرکزی آمریکا در سفری ناگهانی و غیر منتظره وارد مسکو شد، طبق گزارش های تایید نشده این سفر مرتبط با جنگ اقتصادی علیه ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/143726" target="_blank">📅 17:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143725">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
پزشکیان: امضای تفاهم‌نامه نه از روی وادادگی، بلکه از روی منطق و آگاهی بود/ عده‌ای کنار گود نشسته‌اند و مطالب نادرستی را مطرح می‌کنند
🔴
رئیس جمهور: امضای تفاهم‌نامه از روی ترس و وادادگی نبود، بلکه بر اساس منطق و آگاهی شکل گرفت.
🔴
دشمنان متوجه شده‌اند که از راه نظامی نمی‌توانند ملت ایران را تسیلم کنند یا شکست دهند، از همین رو بر روی ایجاد مسائل اجتماعی و نارضایتی‌های اقتصادی هدف‌گذاری کردند
🔴
با مشارکت تمام آحاد جامعه، منطقه و کشورمان را آباد خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143725" target="_blank">📅 17:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143724">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGUwoB3a7hpFaSOt3AiQztByNGc9RNDx8FDlGwyfukMJfcSamwErTjSfU3biFIp3vPp7pj0YpE-8nbbmq9fkuyHDg0JMGsws73PC1SnPJx9sa1lDMTbDjHE7KEXvjfiG25DHILPxlq5L6UPWmHX3nwekFWNx5RoAiwQFr5oIDRCK5J5si9L19gX53YVmNCWoz3_twRhJfSA01b2MWOFQ1xwSTxrmtMUhmbDPGLyruOhLSjtL5gdyGmxWIMUNHBijzhKlXN3NXhCyVwR6CtABgu25K8VEpayUXbu6mXjg-YyYFVVsdZhrbfaCuhHRSWxRpW5I-1EgolAUD_EjxqHNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرانسه و
عربستان سعودی
به توافق رسیدند تا یک پارک سرگرمی با تم مانگا به ارزش ۶ میلیارد یورو در نزدیکی پاریس، الهام‌گرفته از مجموعه انیمه و مانگای ژاپنی "دراگون بال زد"، توسعه دهند
🔴
این ایده پس از آن شکل گرفت که امانوئل مکرون، رئیس‌جمهور فرانسه، و محمد بن سلمان، ولیعهد عربستان سعودی، در جریان بازدید ماکرون از عربستان سعودی در سال ۲۰۲۵، علاقه مشترک خود را به "
دراگون بال زد
" کشف کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143724" target="_blank">📅 17:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143723">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
نایب‌رئیس مجلس اعلام کرد: سهمیه ۶۰ لیتری بنزین با نرخ ۱۵۰۰ تومان حفظ می‌شود، سهمیه ۳۰۰۰ تومانی از ۷۰ به ۵۰ لیتر و سهمیه ۵۰۰۰ تومانی از ۳۰ به ۱۵ لیتر کاهش خواهد یافت؛ نرخ چهارم بنزین هنوز نهایی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143723" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143722">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b43ed20b.mp4?token=Zt5g4yf05G7JzFDSDyYbTA3NOdZWJnQ6_1L-1nGbCIJyhoKzpX3jYCVB6EmGW_fdiq-1OPPa2ZZT_wM7waonIK5HY8x8dMGHozFppb4G9sW6NNMkFn2jri9uThzF6qv8-2d9tg9ZMmKKHRvXh3zGR3w_xp3bgB_C9J4M5M0ex-5FhjCFMfpSBh5Vua2jY_9IvGv7o5MA0Y7TqO0Nc1qmV5XmV9K5TLEsMzUbmVEHGcgTgrMRM4DfqVJMPx3T0i_93xA-A944Agu098eL1QEsN2BWSLk9-QAtOrJsIZO6DAx8PncQGTE5lTqVBfxhjnt-TEle-W-h3_WLWNyDgVR7vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b43ed20b.mp4?token=Zt5g4yf05G7JzFDSDyYbTA3NOdZWJnQ6_1L-1nGbCIJyhoKzpX3jYCVB6EmGW_fdiq-1OPPa2ZZT_wM7waonIK5HY8x8dMGHozFppb4G9sW6NNMkFn2jri9uThzF6qv8-2d9tg9ZMmKKHRvXh3zGR3w_xp3bgB_C9J4M5M0ex-5FhjCFMfpSBh5Vua2jY_9IvGv7o5MA0Y7TqO0Nc1qmV5XmV9K5TLEsMzUbmVEHGcgTgrMRM4DfqVJMPx3T0i_93xA-A944Agu098eL1QEsN2BWSLk9-QAtOrJsIZO6DAx8PncQGTE5lTqVBfxhjnt-TEle-W-h3_WLWNyDgVR7vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش پزشکیان به افتتاح پروژه نیروگاه خورشیدی: یه کف محمدی صلوات
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143722" target="_blank">📅 17:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143721">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
عقل عرزشی:
+باید با همه بجنگیم
_خب محاصره شدیم و گرونی اومده
+تقصیر پزشکیانه
_خب دلار تقصیر کیه؟
+معلومه!همتی
_دولت بره توافق کنه؟
+غلط کرده! رهبرمون هرچی بگه همونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/143721" target="_blank">📅 17:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143720">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECIuhqrNKYOgQVoVtZsRsH8Dk4GoMSSrUO7PmL1sNRnHK0004T3Tv7nvWcMx2TCk4zble6z1j99eN0cEa5o7IYq3kWwvbXzZynIDU_ojhdWHsVYrRVQVG6nCKIrbv0HmqTp2ja4pNT7jOkNZ3qXOjypY_1ExEwHbhwXy1VBFBWS-y736jKKCQTG7QKY1uG8wGvhsO-EkxGlDzGuLEj72oJfM3QDQyLHbE8EalpYxhvClGOyuMxW93vkci7agHTWx158qwUEtja8Dj2b09VOvOJ9enuxMJIGRbuhzUs_POGJ0ZlJQvvdeSVxDM9KkcxlreWKFkH0jvEm_9kPkEXtjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: کره‌جنوبی حاضر نشد در خلع سلاح هسته‌ای ایران به ما بپیوندد
🔴
با توجه به رابطه بسیار خوبی که با کیم جونگ‌اون، رهبر کره شمالی دارم، از این واقعیت که ایالات متحده مدت‌ها پیش با مشارکت در رزمایش‌های نظامی مشترک با کره جنوبی موافقت کرده بود، راضی نبودم.
🔴
این رزمایش‌ها نه‌تنها پرهزینه هستند و بخش زیادی از هزینه‌های آن‌ها را طبق معمول ایالات متحده آمریکا پرداخت می‌کند، بلکه پیامی کاملاً نامناسب و خصمانه به کشوری می‌فرستند که تا زمانی که دونالد جی. ترامپ رئیس‌جمهور بوده، تهدیدی ایجاد نکرده و محترمانه رفتار کرده است.
🔴
بنابراین، با توجه به اینکه برای لغو رزمایش‌ها خیلی دیر شده بود، به پیت هگست، وزیر جنگ، دستور دادم رزمایش‌های نظامی مشترک را به میزان قابل‌توجهی کاهش دهد.
🔴
در موضوعی که شاید چندان مرتبط نباشد، اخیراً از رئیس‌جمهور کره جنوبی پرسیدم آیا مایل است در خلع سلاح هسته‌ای جمهوری اسلامی ایران به ما بپیوندد؟ آن‌ها گفتند: «نه، ممنون!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143720" target="_blank">📅 17:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143719">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyjNALdk-wwwaQ_TpDvQtwQZbSNGtf_5_YYwZL5FyjO0p8PS0UJWsDQ0M8Y6mWQBzX5_xoL7HFTOREiXseYasAQ_RIsur9Q4455UOYiUdoSFBATMnqOOdckAuM132FPkIh6E7FIKMhR1PlF4AiEfwPcLguLTyikvGnwtSrWu8XYlioBzui4_K-Ze-W0ANOqnoYdQ6xWpIhLq6EXSI7a_RgFcLNw3h__TAKM51PPakVMP1fv84DG3jn8QFNosiJ8dAR6v9KwZqyzLSvvRt1I_VPH0La0LcNiLrzxgSpe4hHVMrsLxNxPSGjznC9clAvcvSDPj5VnHtet7m2bzmyxQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی: با نون زحمت کشی به اینجا رسیدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/143719" target="_blank">📅 17:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143718">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ویدئوی جنجالی صداوسیما؛ نقشه ترور بارون ترامپ!
🔴
صداوسیما در اقدامی بی‌سابقه، اطلاعات محرمانه و مکان‌های دقیق تردد پسر ترامپ و نقاطی که در تیررس است را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143718" target="_blank">📅 16:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143717">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKYAre6tG5WbJOn1zxNv0z4vMH3xiBeX-Y5nmYaHVn_fvt75Y-GpG90hKt5IlLnReMDhrKctGmQe8Qx_pmkGAdw7fvtk7bIPwv0SXbVhr_bBuDdLt_cLwP4YLSv9J5hZM6mF3b1cajinLqe0xpinXZ3qehZSZBbvg6JXttRjTQxiwyt1lhsHHjrA4-P0-u1-L-qc1XDBLkPLs4unZWxqEq5pKwVxEakZ-CvsD613C7wDG06G9NWP6SPLAKpDavszaCsJHPe-RZELEbamuFcKdzBkuqTtw6HUAQz9WbZJkQ9T-D4Vm9Nwej0C4RuznhJqJWAK8lm74zbqOTHGehKo0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان ادامه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/143717" target="_blank">📅 16:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143716">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uxv6uyHeg0LOr_XihUJdlFXDXsDdt4PpvWAVRYI3sywJYUjM7ra_lKBPgxpGgPOUAhCSWgoSx1FDHt1wIWSIvEMBQ8xD9tOiZOfHEMjHER4ZA1gcAuATLs_ezriEw2IOeP5gf-NO-z68UyT6sbcrxBFF7g8hScLnGao3C_xXDitNle5RGaaUOBzlBXQ8TAG2WK1VbybqAbVUY-ml1aAyVaVRMWxYmEz2cgYxzGwKMFU1g7VjiZX3lU5GcROHUHN5n2JGZPN5t_qjgr2m4-GKWhAHGbIMYsU664F8wm98QlueizDFcQwOLDSJW4PylexPtpM5dDxITWFzcG0d7H-l9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
اردستانی، نماینده مجلس:
درسته مردم از فساد و دزدی ها و بدختی دارن پاره میشن ولی با این حال بازم پشت نظام و ما هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143716" target="_blank">📅 16:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143715">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lRlC8VQ3e8YXQD6nCniI0NT1w-Nvov7w2aNAQRnKuQ-6qlMbfRWP0FY7ZJuuqIeuUuv2pCmmeeuoeIiQdhoibmZWXKnapsHTaRvSh2iIoYLiMYexPsM5SiL5WPST7_NOq_VA31DfI2WGP9wzdPU6WPJBKnm0IiHvhiVQeP4qEoSeX72COt2eHcLEZqBFIRaIRH-JyVY81Qwu7U0xck8nYvSMwcpG56Mv15EQEo-aYeKAwZvdi9aBOopGOfTVz1RmF648suj6VnuoSsdnAeXXMn9d7SQIUhG5lqykdNOq7rMyw85nsHRogVc_jayLv5LF8dBiNSGrEJSt2On4iFiVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متأسفانه یه دختر ۱۶ ساله در کردستان، به علت فقر و گرونی، خودکشی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/143715" target="_blank">📅 16:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143714">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_lYaBndHvHTCvIBeggdiy-LBw7Cf0on9zC-a_YF1zH2qjW3cebwtAsR5L2WUnqfpbKjYpCBYAP7UlapqgqO_SGiigkJ4sKMCgNzB32DrT06bAYaVLo7e2DfWJ0rwuGMHp6cIbTiEXcmNLN4GqKu56iac_CllDr9YE1lVqfexEelZK9-tIR6KKfqToxkgX3CM73MBPC31E93x6k0X8Fa_k7c0OlIULJd7KVt5DEbXYLRJZM6OczWNxd072zdmmYOFCv06hza33HozRogmCk6Zm5_cwqlNu8R84RhD427S6HWHI0t27yEvc9HhNMGDztN04c4-zeuLN3QDe18PgUgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیفون 17 پرومکس 2 ترابایت:
1,000,000,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/143714" target="_blank">📅 16:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143713">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
طبق گزارش‌ها برخی سنگ‌ قبرها در بهشت زهرای تهران توسط سارقین دزدیده شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143713" target="_blank">📅 16:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143712">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزیر صمت اعلام کرد بیش از ۶۰ درصد ظرفیت پتروشیمی‌هایی که در جنگ اخیر آسیب دیده بودند، دوباره وارد چرخه تولید شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143712" target="_blank">📅 15:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143711">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGOt1tqFIcrudAmONfos2msz5fIGLOpzD1O9ATFmYfc0Ty-rj8KpeRmyjaef5hoOkQut0ZIpUhSP-vpGovnYiXi9KAKAUzH4sVT5xayO5N0PCk2Y72qpTXWdy-fwLjzEHqocJhBeWF2-IXDCoVITXSSndV_L_SvbJqvCCqWrSJ1ovfsZoOnKByIqL-EovuBnWruPtS-UsupZoXKgvmtrpqzC0ifFiYA-nAbfvcsitmPTFzBwu0k_Rdb8xsH-vA2dEPJcXIBz4VUdy3Ui8ObWW4bEAgH11F9T7jG6d33Tt8wSDTao5BeRur1-mZMp84b-Irh-ufCnjfVupH1n-lxJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس و دیسبک طرفداران پهلوی و جمهوری اسلامی
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/143711" target="_blank">📅 15:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143710">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdaoJoa5qkwTdifyOmTU2GALONjA5ZffQGyCjIDJcB4su9aFC31ENQcNG0rQeIleU9oP4hYALBqIjnOLWI3btDB46z8ghPZRurc5Uik7OM845KMvnT7vmyr7O2_7ok1SeJ9yZthmrHVT5h_iDIKtGO9HfMZ_P1rOqXkxzFhYWiSWjB6RGdUs6SaM3cDsk_Cj-GoX-LbBqmZ244sY-H_MPETSZpbHXhwS-H6yC6v3meu8Nqa8qNX1SQPOBIbUoFUmu7XslSff-7GU16NnEw6a31QjKcJGeEE05fNHL2Wsf8wzzvTQY26qkRY6XEC-7oh1PKRSqEK2ipLmKX-355fbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قیمت نفت برنت ۸۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/143710" target="_blank">📅 15:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
برخی کارشناسان اقتصادی معتقدن که؛
به دلیل‌ کمبود کالا در کشور ممکنه دولت قیمت ها رو خیلی بالا ببره تا دیگه همه نتونن فلان کالا رو تهیه کنن و اینطوری دیگه کمبودشم تو کشور حس نشه.
🔴
کالا وجود داشته باشه ولی به خاطر قیمتش نشه تهیه‌ش کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143709" target="_blank">📅 15:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
خبر مهم درباره ابر تورم
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143708" target="_blank">📅 15:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjOv1kcRkrohL9LcPA9I4eokcbcIV2dv2Zl9r2zLxGVYoZVWj0MrOuGFuB-GCNMW801ep4Wkj1M_zR5qa2w6xqJ5_HsqzpcJNW_oYqtfB3mz2xccq2-fsRfrQJjJiOv_rT9orpSPI6Wr7XRM9nT6yNRTIgFvX9_Mx3BIVNh4Zm7gSHHmOnW6JnCQMdmHZjEFoHNLkZV7YqCrBp6xU0Qut9UVH4NR_iZhjz4jya4AYhj21R4P_cSXlbuMO3_djZgYzWVPJrvELwExA7492khvkAwSAv4i3mmsHo4NarR4Tf-G_m05EaXyCatqJAoufQXxG98tchKDQqZScvzwPQwa_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بوسعیدی هم یک پیام از آمریکا به ایران آورده و الان داره با عراقچی حرف میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/143707" target="_blank">📅 15:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uijEFOx_G43gisFAOTGfKO2c9Mm2pA0ssIsRePEmm8mbpJwdLuTkmcw-AsOonPMsWxSsonHEJ4GOsWdslKxrLk6W_YXuY_A8t58pMq2w648KLasKVZ9vjT15Lyr1_gatGkSOqePlf7HHbZUn5DdcnkOCwCduaNjvOSaCNOpVMho_Yb-VTRFNv3NMAiLofmskGd5jlO2IndemYgO8nYtRxpAS1b2njtW3-edUAo1Bxq7UegArMeeIUH6DTTUAt3eVcJza3QktUafodK8kG5scOR8kfXJG_ZCDOGr0G-XdM2Jv0i6N85vH_GFkMGwE72NtC8n8aJlm82VL5fajITCQAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاسمیان، موسس
شلتر
:
باید سواحل آمریکا رو اشغال کنیم و همزمان واشنگتن رو موشک باران کنیم
🔴
باید با همکاری کارتل‌ها، تجهیرات نظامی رو به مرز آمریکا و مکزیک ببریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/143706" target="_blank">📅 15:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143704">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-GL7xRC2efZYiUz5udcGQtOBTiHeH_Ryhr_0NySH1HGOZZrGnCJOh7DcTdOBHw0XyDi0GqPpFiDy1N4l8mLwi-MDdOmkgeUe2mb6-hlha10TJfhDEhul-V9QFU8dXZPkQkPwLL8nT3s9a5CLJuoCJF_aV1Lcea90ip9hyu4t1wHCrK-YSKwKMmHDx7YDTUNzPHKJvPLDMEZ1Q49rm-A81rclGflzCZ4eXJ0l2mLkISJ9gSd-mjt6UrzP3PU4QkvO3guSUbPk9h0XW5FYrx8UpSz0AuS-Z9BfFk8WxhKzJReLtFaaIwY7E99TGcdxjnhjNQ7C_hNRfbuRzojIfVe7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: جمهوری اسلامی ایران در حال سقوط حتی حقوق بخش بزرگی از نیروهای نظامی خودش رو هم نمیده، ولی همزمان داره معترضان رو میکشه
حتی آدم‌هایی رو که اصلاً در حال اعتراض نیستن، اونم در سطحی که قبلاً دیده نشده
🔴
چیزی که الان در ایرانه، یه بحران انسانی در ابعاد بسیار بزرگه و باید همین الان متوقف بشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/143704" target="_blank">📅 15:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143701">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0AlOzCVuWoPXBphtio1Yl4lDMM0x4Tgq4qXilyi3GsKGmUgpHc_vYHZAk-q0olu2l71KhaaZ_eAUZATFq65AWmkTh1gXqsxGMjPeesbck61YJWcRo8hGnCyAO2eTHbYO-zFm9RtGQ2HOBmGQtwLaDi7XY_qGiFZQCrHN21Lb2Pm7m2pGT58jKeBw6z-lVMkQQ3U_NNacouiplIjSvLVx2sH5TEGVxbtp0jejo1_1cHQqwyBl9v5QhyCfgVTKEH-jGXXU8OfJWuqMAIEXSMGphIFa4lsUz8pYzRQxiOokdYC62SHyPf00Sym5ituJkAmEX-F41j0wh7w-zcUF5dTOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرپرست وزارت دفاع: هر فشاری که معیشت و امنيت مردم را هدف بگیرد، بخشی از جنگ است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/143701" target="_blank">📅 14:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143700">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
قطر: ایران با بستن هرمز آزادی دریانوردی را نقض کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/143700" target="_blank">📅 14:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143699">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e42e42d81.mp4?token=uh-VFDGEGzEsqP_lkYkUr3dI-PiJgM_9EzjrzDZ2iG4b-_NWkNqJ67e3OzpVcTtNH6Lzh3wl_RrRESvSh1CBwz7Yrao4InShTYTe1lLXSM0x0UWSgmYbC0sW1Sk8-pQEjDj3Zt7nfmJ1_UtPihXbZHBOpFLDJ-8_oWD5R5mpi-45WBZBDN3oRkwxgpCJH56LNogMaslHurQCggJpro-nj2h4UEMyfhMXQRwIzD_FjpQlgDOQZuEk04Q-xi_uFSnkInCeqh6sieQ5hlf4Ub5GC9YwQwsB3S18jvr_pyQ2pb7-UJ8kd-Bsb4HaUl7Uhuq_aJbsi6WxuGQq-KMPCkMlvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e42e42d81.mp4?token=uh-VFDGEGzEsqP_lkYkUr3dI-PiJgM_9EzjrzDZ2iG4b-_NWkNqJ67e3OzpVcTtNH6Lzh3wl_RrRESvSh1CBwz7Yrao4InShTYTe1lLXSM0x0UWSgmYbC0sW1Sk8-pQEjDj3Zt7nfmJ1_UtPihXbZHBOpFLDJ-8_oWD5R5mpi-45WBZBDN3oRkwxgpCJH56LNogMaslHurQCggJpro-nj2h4UEMyfhMXQRwIzD_FjpQlgDOQZuEk04Q-xi_uFSnkInCeqh6sieQ5hlf4Ub5GC9YwQwsB3S18jvr_pyQ2pb7-UJ8kd-Bsb4HaUl7Uhuq_aJbsi6WxuGQq-KMPCkMlvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پزشک با گریه: مردم وقتی مراجعه میکنن میگن توروخدا دارو کم بنویس پول نداریم، بعضیا پول ویزیت هم‌ حتی ندارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/143699" target="_blank">📅 14:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143698">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=mud3opm0QQdcQl6zwv6SKUfpZJgEHoOx3eKzm1Kl55oJP3WRURfmP5yEDoks1wdT4XBUVkKHRcVDzQF_6FItI1zXAN44Xuhijd0CYTsAtvE0Ld5fEjdRDBvX5-iKMTnIjF2X48mO5foUlgYPgU8IXXLd8L7b1_HGOqXuc2lNk8j-pfE0KYcqvtMJuFzlCGLHoEjm5aGYKAF4yYsVspN-j0Le4Qj2q3dTFTlPaFUHa5eB9dfmowj-Wqg_eeUPh_Ta9Ao85CXEj54LECaIbri7olkFyBEjNz4tpSYScThzo8cg_rYzwc-pm8vXaCAe9tSBjGcKb3IGIk-BFzS-Nv6p3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=mud3opm0QQdcQl6zwv6SKUfpZJgEHoOx3eKzm1Kl55oJP3WRURfmP5yEDoks1wdT4XBUVkKHRcVDzQF_6FItI1zXAN44Xuhijd0CYTsAtvE0Ld5fEjdRDBvX5-iKMTnIjF2X48mO5foUlgYPgU8IXXLd8L7b1_HGOqXuc2lNk8j-pfE0KYcqvtMJuFzlCGLHoEjm5aGYKAF4yYsVspN-j0Le4Qj2q3dTFTlPaFUHa5eB9dfmowj-Wqg_eeUPh_Ta9Ao85CXEj54LECaIbri7olkFyBEjNz4tpSYScThzo8cg_rYzwc-pm8vXaCAe9tSBjGcKb3IGIk-BFzS-Nv6p3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند مریض: اگه شما آزادی پوشش داری، ما هم آزادی تجاوز به شما رو داریم
#پفیوز
#لاشی
#دیوث
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/143698" target="_blank">📅 14:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143697">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439a914edd.mp4?token=VqeHRgMbfm4mMHlcTGJUJnVurWsnJUWFCKgkEZZvwcAoY9WmezTXpaxOB59GUSrZCJP3m7A-qEIJLytEEsopj0IJp87wWsPA4HHJ9alA8zW8L6SAfuGAQ1CsZnhdXJc2Qt4nn_9Wj8f8GdJZ0OZ7MjyfKTNZgOc1oR4v93uIKWVVopIFm43vyLtGs9eRGUoY7hW6Owv_ha5RkQcRwNrVh-Yb8-e-ajufe2hxR69iVU4MJXhJFsTb51ZLZqxFgMNkRTPzsRJfAvFOi_9VC8p1nqsif_M590orI77sgupJBk5FsJ3D6MCgL4S9hL5ZkNX3C6GK62h9EMKcsLgn_nda2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439a914edd.mp4?token=VqeHRgMbfm4mMHlcTGJUJnVurWsnJUWFCKgkEZZvwcAoY9WmezTXpaxOB59GUSrZCJP3m7A-qEIJLytEEsopj0IJp87wWsPA4HHJ9alA8zW8L6SAfuGAQ1CsZnhdXJc2Qt4nn_9Wj8f8GdJZ0OZ7MjyfKTNZgOc1oR4v93uIKWVVopIFm43vyLtGs9eRGUoY7hW6Owv_ha5RkQcRwNrVh-Yb8-e-ajufe2hxR69iVU4MJXhJFsTb51ZLZqxFgMNkRTPzsRJfAvFOi_9VC8p1nqsif_M590orI77sgupJBk5FsJ3D6MCgL4S9hL5ZkNX3C6GK62h9EMKcsLgn_nda2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجموعه‌ای از انفجارهای اسرائیلی شهر "المنصوری" در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/143697" target="_blank">📅 14:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143696">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
فرهنگستان زبان و ادبیات پارسی  اعلام کرد: معادل فارسی واژه بیگانه «لانچر»،«پرتابگر» می باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/143696" target="_blank">📅 14:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143695">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
الحدث: عاصم منیر به مقامات ایران اطمینان داد که پاکستان در تلاش جدید، به دنبال پایان دائمی جنگ است
🔴
محسن رضایی به عاصم منیر گفته که تهران پس از رایزنی‌های داخلی به زودی پاسخ خود را ارائه خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/143695" target="_blank">📅 14:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143694">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1525fa44a.mp4?token=JpuZTClsT0uLaJ0vwXxhf2Zieyzw7QtgjuVgDE65oMDOIiaLZ1viPMsH3luDXah78yXhEVOR-BO_QCGvlTKCqwv4Kd6Gday12ENEHytbVcp5iyXZiHHL-sz2JXriiCnpxY52otR7xuy9kQKo3csaJdnbeOpZyau3276ZnLaJ8i9LOeW8ezkF5j-aqsVXGsL2ckUY9vipCg-z96Hw7Llgdv-i0rNlVBsPBDv-OSJrLvS0D6imiTDiAJMaQvJTOo04JJqGmX-EwfLfyYgmkt9l7ePe8MA4nHkADo7LbYfk7HufTuHep9ybGZuQilPrywDvN4cEge6o6Mu3pgx0NlEjRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1525fa44a.mp4?token=JpuZTClsT0uLaJ0vwXxhf2Zieyzw7QtgjuVgDE65oMDOIiaLZ1viPMsH3luDXah78yXhEVOR-BO_QCGvlTKCqwv4Kd6Gday12ENEHytbVcp5iyXZiHHL-sz2JXriiCnpxY52otR7xuy9kQKo3csaJdnbeOpZyau3276ZnLaJ8i9LOeW8ezkF5j-aqsVXGsL2ckUY9vipCg-z96Hw7Llgdv-i0rNlVBsPBDv-OSJrLvS0D6imiTDiAJMaQvJTOo04JJqGmX-EwfLfyYgmkt9l7ePe8MA4nHkADo7LbYfk7HufTuHep9ybGZuQilPrywDvN4cEge6o6Mu3pgx0NlEjRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دیده‌نشده از اصابت موشک‌های سنگرشکن به ساختمان شیشه‌ای در ۴۰ روزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/143694" target="_blank">📅 13:54 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
