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
<img src="https://cdn4.telesco.pe/file/I3XoE5Jrmthih7A1pJL6jF6f3e2EDdLoYHytAIj4Ap9HOBFd33c5dMailTNCtk2kb5IQG3I5432mK7b5vevF6bjwMPgccvMZtMcXcmLDalrIWt4ynGrxTp-G89PDrb8QyQnLBscgV320KsO3ixzPU7U9euULkiNoeJ2TUF-BFB0TJz5oHcD1et2mg0gpSN96EzZjt_Tze81Du7Rxe9gEKC_LFEoRUR-Y9LvprpiI-4XtrdWLzfBgC3TPMxIop2NMkLR1Vt3BSvSR3UigLiYH9wi4brpHJfV6x8AQmHHKunPERBjCnM5EiDoMSKDzOoNGh26ySH0R-BPokiarVRw-4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 15:32:00</div>
<hr>

<div class="tg-post" id="msg-140523">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
🤩
فرهیختگان: بزودی قرارداد اوستون اورونوف با پرسپولیس با دستمزد 2.2 میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/140523" target="_blank">📅 14:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140522">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUMz-Onh-CnYNf6Qmc6vLICKwtC13UyLvxhNyCkPV-8RKWNNwB7_DtIN9_2vVLE7WdV82VuZ7jHZMD7hVH8NWGYJ1CSC6zDyn2U3OvuxvJc_fqAUMGxU7VJREBO6OUsJ8GRHIqf6-EwZCMCFb30By3UNTg11pvs2A-6O4t1VNUcDTPTuvwqdAPComgcQO4OjdOHvZEAwgJyIErQWyT_ALEf19BLjFqW0c5f7SYYz0LgfhxSbi5TwPnMLHxSC_HUw7gONAu6H_neTLHO-VC_b6_3Gwsk7sOsHxquhxk3qf9yU716Bm_O7UA96uGnCI9b7sxgtEJtPiWPLlFaO_PG_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SorkhTimes/140522" target="_blank">📅 14:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140521">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/140521" target="_blank">📅 14:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140520">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SorkhTimes/140520" target="_blank">📅 13:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140519">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=IkJao9nsE5AETuvWqoOHKKqL5uohdfGkdEyxaMxUuSDbFx0ZWQpMRGpUgJ9EeHja3-ymTVZgw04M9yZ4f7oVt0iCLj9X-Mc5OAKDJmFHF11tLezdopG_aEyP29dzSsju0RXYkMhyUqtbg9ztX3lBvXCE6rt5IFz7Vif0aoPe6piekS7ivbaFQEZBfp6g76XxV1wwyiS_cgt5G_Lk0p4XEDF4oX2rZd39sa5wb6DqtNCNEMMc0UFE-A3cSX_8jLvXxoTrovhkvoNIDlFdDDDIxl-q9sLX_OP2Gmygm4Oq8SY4yM1uTr7UcprSDhMiuG7GpJu2fQInEatOykGKfdBjIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=IkJao9nsE5AETuvWqoOHKKqL5uohdfGkdEyxaMxUuSDbFx0ZWQpMRGpUgJ9EeHja3-ymTVZgw04M9yZ4f7oVt0iCLj9X-Mc5OAKDJmFHF11tLezdopG_aEyP29dzSsju0RXYkMhyUqtbg9ztX3lBvXCE6rt5IFz7Vif0aoPe6piekS7ivbaFQEZBfp6g76XxV1wwyiS_cgt5G_Lk0p4XEDF4oX2rZd39sa5wb6DqtNCNEMMc0UFE-A3cSX_8jLvXxoTrovhkvoNIDlFdDDDIxl-q9sLX_OP2Gmygm4Oq8SY4yM1uTr7UcprSDhMiuG7GpJu2fQInEatOykGKfdBjIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
بازیکن تیم‌ملی اسرائیل دیشب بخاطر این شادی بعد گل مقابل اتریش با کارت قرمز اخراج شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SorkhTimes/140519" target="_blank">📅 13:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140518">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk5AtxITBzRZKHoSK2Btuhqk8hx6SE1Q3My2aepaul58H38KhUytatgJvsTdza9a_Sgc8ey76W0b4Zseh0UM8z6_yEvCzI0flinfudFt3kmHlLbF6uK8mYxb2ihH0pzrrXmdyposY80V8Ce0jNS3rrV1T1gnxp7CAoSBmTS2bVLXVb6asyewKlHuR4RvVl7LcdW-lzx43xvbyZm7WHjV1t3eM11MwmqxMm-5CqrSefm7SmK1pZZQ6lvC1M9lJtWID4iUUrt0OyJJ_gISgFPhXhJhqb8PArSBWbYtGtj1XvHYP5e6zLctiwfzzu_FrsBbwLil3vyJbhWVysX0gnBYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
🚨
✅
⭕️
⭕️
⭕️
با تصویب شهرداری نوشهر؛ امتیاز لیگ دویی این تیم به پرسپولیس تهران واگذار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/140518" target="_blank">📅 13:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140517">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
جواد نکونام؛ مهدی ترابی به دیدار حساس‌فردا باپرسپولیس رسید اما مهدی هاشم نژاد بدلیل مصدومیت این دیدار رو از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/140517" target="_blank">📅 13:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140516">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQVco_iTzYhGquu7alOG02Lew4lV5_8FB9_zEL5M8A-eMOKn2LEhjMAPNv1SI9WKKmVI3KJ-DaD0g5n6OG3GVSNqTLbWfE0svDLKWr-KT6Iz7H_zsBwvl7ds19xv9CZMEEzz6mXgAs_-UBcaF6duPEo_qh9LPr4Y2JWizwrn_7L-VZU6ByHxc07VpFiX9vYXVw_e9zdBMo1XxSAAYddV20_spasTHBclDph9q0ssY7IassZrZom_ASD6mKjDoHJcklAJ0CPBbWj_T4f56yC3bEeX9zGt5l87UMmq9KDK4NGnHF185gOvH3GyDHzSiEvk1IV8U4Nr_6OyEyou3ky9Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گاریدو یکی از گزینه‌های تیم‌ملی برای
جانشینی امیر قلعه‌نوعی هستش
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/140516" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140515">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭕️
⭕️
#فوری | ترامپ:
🔻
مقامات آمریکایی به مدت سه ساعت با یک هیئت ایرانی دیدار کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/140515" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140514">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
✔️
✔️
محمدحسین صادقی، وینگر ۲۲ ساله پرسپولیس، در نیم‌فصل به‌صورت قرضی از این تیم جدا خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/140514" target="_blank">📅 11:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140513">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⚪️
⚪️
⚪️
مهدی تیکدری در غم از دست  دادن دایی خود عزادار شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/140513" target="_blank">📅 11:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140512">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/140512" target="_blank">📅 11:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140511">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDIIInCvG8WoAfkPKZJDD7ppffH3zEw1T9XK6L_hpfWF6fgL-SwGVKsWChiCUlhkhgjZEO1WNQMLf_rKmW_NITbI8PX2dXtgg3IqaRg-qS_5a7Q-flrHEGdZxmxGctH44Kg3wSg__K0w4-kRCDS1VQrNotItnbMQEv9Eib2F0uarnq2JuEETyjS2CSYMZueIMQJq2xRVPnqE5S-2UDuG0L3lwba6j3oXx1St1-XhOKcJ2qz8x8BGOI6uzgDgIZagORLQifbLqV12g71ek3-I-G8OlqkK__DP9JkE0c5b6HMOWzFyCUL1wOUoZL3L5rfCTiZsTZ9XYYBnKmcABqmECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
پرسپولیس قید جذب اندونگ رو زد
🔻
باشگاه پرسپولیس به خاطر ریسک بالای این انتقال و دور بودن اندونگ از شرایط بازی، تصمیم گرفت بی‌خیال جذب این هافبک گابنی بشه
🔻
طبق شنیده‌ها، تا این لحظه تراکتور تنها تیمیه که همچنان دنبال جذب اندونگه و نکونام هم روی این انتقال اصرار داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/140511" target="_blank">📅 10:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140510">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGCYwUCPHdioTEi1Fa8pWhv8NUfJ89NrgRUiRtE4f4ToKyYRl5708_cimCo-ICha0YHcSJxrx64X_UTznzYXxXh1Y8mKGsMV11NISKqXf92JpR6qWxp4bB1ddL2T5zU8E5Z0rl_K7Gt2us2zCMXZ5AEQtMrSj9NSC27MyiLnYC0lFGgfL4ItjiiTt1XJuNcYQ4B4EiyYDNt0Tc8axjWFEXu42fQiMSI5WWt06Nzq2tg73PVJYjOxFWvad4VLeCwyCeuNq6Q0Tsly1qpGSrTIa9Euel8zIsCi-A-y6S0RYD3Pwyln39bXJxkiglk9Q1beVuJkUXCilbVeBl_tExhFBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/140510" target="_blank">📅 10:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140509">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/140509" target="_blank">📅 10:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140508">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
حسین عبدی: از مردم ایران عذرخواهی می‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/140508" target="_blank">📅 10:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140506">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1kGexOzZvZW4oNy4T4Sxu6ERnHqo1L-aCV43y0-FzL5M0cTvBaTkwU7fZtYLDjO2RiZSa7D1-eqiBwk5jrjbQGsPiA2cgV-f0lQW7XJx1V0SvsE3KD8mR7lF30Y1BkmZPuDDsmaq9cjo-3a9H36gc5poIuMSqkKx8AGX_JBJcNfVMdjc94JQ0QUW_LhPBcAH2l8rCpqqOypBX9OJCJWZ2p_v0o_Nf1hdEC21NLcH68x24r8skhcMvEPGbSs2VlftMkghwl-af3LNzW6RIoTGChKgk-VZrN-h1IRNZ4Y98fGUho5PE93R111OtSTROEwzwwMVk7qwaqQrxwf9Jfx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ITALY -
❤️
BELGIUM
⏰
Tonight 22:15
🏟
Stadio Olimpico
🇪🇺
ایتالیا با بازگشت مانچینی و ترکیبی جوان‌تر، بازی را احتمالاً با مالکیت و فشار از کناره‌ها شروع می‌کند. بلژیک با حضور بازیکنانی مثل دی‌بروینه همچنان در انتقال سریع خطرناک است، اما غیبت تروسار، دوکو و کورتوا روی کیفیت ترکیب اثر دارد. آخرین تقابل رسمی دو تیم با برتری ۱–۰ ایتالیا تمام شد و تقابل قبل‌تر هم ۲–۲ بود؛ بنابراین بازی‌های اخیرشان نزدیک بوده است.
نقطه کلیدی بازی: عملکرد ایتالیا در پرس و کنترل دی‌بروینه مقابل ضدحملات بلژیک؛ احتمالاً جزئیات و توپ‌های دوم تعیین‌کننده خواهند بود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140506" target="_blank">📅 01:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140505">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭕️
⭕️
⭕️
فوتبالی: جام حذفی به‌دلیل فشردگی تقویم مسابقات و برنامه تیم ملی و امید برگزار نمی‌شود. سهمیه‌ آسیایی هم بر اساس جدول نهایی لیگ برتر تعیین خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140505" target="_blank">📅 23:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140504">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ9q7KScagYdCi_8r3SxI54W2wJ_UF6SAa7Xz0_cBE_h254im8bQAqbxHsnayTSjDSNRDHnYi6kLmFLkCG-L1IWV64P_HSPJX91Xzbjb2DXTibPCIGZe7bj0Myq-5TpcAAlziS7lcbcRX-eASWfWcynXN3M2Pu9c1_b6IkFt7WplpREVCpG9fhqQW9NdsCbRHDexkttyjOYKHhYOEsM-bd_sBioLbHc9phsE6gYfAwdxP6tjjohrIQzmXD69AobkrUV2gzqvDAy2mFqhY3UvA7WK-52I6U_xzTMAS_JzdZlwFoEKlZt95awfpMo2OXRUt1wpaXfSX5IGdK_hQyYXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎉
جشن تولد آقاکریم برا محمود خان و آقامهدی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140504" target="_blank">📅 23:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140503">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199c169158.mp4?token=bmulSWriF6wOav2BRSvCjr8_QiYpTfDZgVKTmTp8lzR47q6Y1K9HevJvHFMZmXMYzbEm31n9z5VbiQ1e978FgC5oEEcNbvzXKUdpQEOde9y9Z-PYchwxV8ICEl9UbAv_d78ojJnzaOuEvEmZhEV_yK2tA9XF0YcxrdaTtqffo8zKKA-MmpvMTJjKK5XlCwMW5fQBtCmUrpwLQAqXP21M2D9l2fAyA8_82hbsR6Xqs5lU5KGesaog_vmUEmc2mnZrEkoqvbs9HVZa5zKTDTalc7-v1OdEYwrrr2TxAJ3zYggaTMpXjIxS75fN5C1Nn92wA-DNl1YfdmxFZzeJDv5MAGXDP42kvmQ96-_xf-_9ymhJP_44nF1-DCV7iBd9p4nPWd0FGwdfoF10lEi7v5fI3nC6OoMw7OzYLM2han9timAIsVtuK345MOexzK7OGfzFtd3DqAdHAWMZ0envhIKcDl18-4jZmz3UrKrOqc3FsC7mYJEHs_wIpaopZl5ZCjuCA-U7QsqTuUlc8FF4woJjTUYSFzF7hOm_lBfXGOFrnNpVinocA8waK-GhoWksbhQVWBuEgTO2n_DRclQYSY9ZykgSgabbhUM9yGYV2ytyOvEvAKzgYfcDAU3LPQa0WEeOPBdwjBaCCc9PezIBM9Bvu0VBX7aqiLqBG0TqO6qNJzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199c169158.mp4?token=bmulSWriF6wOav2BRSvCjr8_QiYpTfDZgVKTmTp8lzR47q6Y1K9HevJvHFMZmXMYzbEm31n9z5VbiQ1e978FgC5oEEcNbvzXKUdpQEOde9y9Z-PYchwxV8ICEl9UbAv_d78ojJnzaOuEvEmZhEV_yK2tA9XF0YcxrdaTtqffo8zKKA-MmpvMTJjKK5XlCwMW5fQBtCmUrpwLQAqXP21M2D9l2fAyA8_82hbsR6Xqs5lU5KGesaog_vmUEmc2mnZrEkoqvbs9HVZa5zKTDTalc7-v1OdEYwrrr2TxAJ3zYggaTMpXjIxS75fN5C1Nn92wA-DNl1YfdmxFZzeJDv5MAGXDP42kvmQ96-_xf-_9ymhJP_44nF1-DCV7iBd9p4nPWd0FGwdfoF10lEi7v5fI3nC6OoMw7OzYLM2han9timAIsVtuK345MOexzK7OGfzFtd3DqAdHAWMZ0envhIKcDl18-4jZmz3UrKrOqc3FsC7mYJEHs_wIpaopZl5ZCjuCA-U7QsqTuUlc8FF4woJjTUYSFzF7hOm_lBfXGOFrnNpVinocA8waK-GhoWksbhQVWBuEgTO2n_DRclQYSY9ZykgSgabbhUM9yGYV2ytyOvEvAKzgYfcDAU3LPQa0WEeOPBdwjBaCCc9PezIBM9Bvu0VBX7aqiLqBG0TqO6qNJzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هر جا رفتیم اوت شدیم؛
🎙
درخشان: مشکل، ساختار فوتبال ماست
🟢
سال‌هاست فوتبال ما به قهقرا رفته است
🟢
آیا لژیونرها فوتبال ما را ارتقا داده‌اند؟
🟢
بی رو در بایستی ما فقر فرهنگی فوتبال داریم
🟢
ساختن 10 برابر نیرو، بیشتر از تخریب می‌خواهید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140503" target="_blank">📅 22:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140502">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab25e53c97.mp4?token=I8B-jT0HAK1mIT48jEqiGrGuxfnnfSM7jE3euG8JhWsv4Y4XP3Y3Si_LMiTuzwCDMyYDlhVMaSGNfSbd2iLtrKBVGQsMVANnu7zB-EbO56jsDoLye6n1Ww6dOkTA0uBxvQTirX4inNCiH5ONcm9CYhdGGVFN4guZ3Snxs3S1kagARX7ayjaWaYGEAbvUEJ5SbiO6fk223KeDtWvpZ_p_WMZkATS3cHCkGKfxxMEKlGtbw4Pz5UDFzpNKIngapkg3p4-uPbacsauIes6Lkzt8xYP2GTIGgEsk-dxXH4lwCUR3cTE4FM-9SUD-froDXa31wCuXgOuI7p-O2omaJg9_dx9pI9EQFiHiqtYBzda_8y0YHHHzK4U8_ETgaQUWzOl3GWO9KrdKcz3NsuIQFZG9pjx9W-5bYdrOiJbrWZ7qEe4BHUHyjK9TMlg7YHvGUXUJhC_6aluZJ5XJlh67vCbAGOyzEwnr0EIvLHIt6DvWsKsd1QiAV9r5bKTSkkldZyUMPwUzFKEWzVEupoq2Ffg-4Q99Kd95FWcQ4udTgxzUxBfGwe-aZStvsvaiCJtxQkB4spzln8kb4qCKcG2PsKZeqnfGjTenE8AHlBj9gXflXx2_07_F5VZC5QM1w7LOG3MhDgi5f1gwlFfmVVwYI49xpUVAUM5y5Q4_xbffrv27QPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab25e53c97.mp4?token=I8B-jT0HAK1mIT48jEqiGrGuxfnnfSM7jE3euG8JhWsv4Y4XP3Y3Si_LMiTuzwCDMyYDlhVMaSGNfSbd2iLtrKBVGQsMVANnu7zB-EbO56jsDoLye6n1Ww6dOkTA0uBxvQTirX4inNCiH5ONcm9CYhdGGVFN4guZ3Snxs3S1kagARX7ayjaWaYGEAbvUEJ5SbiO6fk223KeDtWvpZ_p_WMZkATS3cHCkGKfxxMEKlGtbw4Pz5UDFzpNKIngapkg3p4-uPbacsauIes6Lkzt8xYP2GTIGgEsk-dxXH4lwCUR3cTE4FM-9SUD-froDXa31wCuXgOuI7p-O2omaJg9_dx9pI9EQFiHiqtYBzda_8y0YHHHzK4U8_ETgaQUWzOl3GWO9KrdKcz3NsuIQFZG9pjx9W-5bYdrOiJbrWZ7qEe4BHUHyjK9TMlg7YHvGUXUJhC_6aluZJ5XJlh67vCbAGOyzEwnr0EIvLHIt6DvWsKsd1QiAV9r5bKTSkkldZyUMPwUzFKEWzVEupoq2Ffg-4Q99Kd95FWcQ4udTgxzUxBfGwe-aZStvsvaiCJtxQkB4spzln8kb4qCKcG2PsKZeqnfGjTenE8AHlBj9gXflXx2_07_F5VZC5QM1w7LOG3MhDgi5f1gwlFfmVVwYI49xpUVAUM5y5Q4_xbffrv27QPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
نتانیاهو تقریبا برای یک سالن خالی سخنرانی کرد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140502" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140501">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
حین سخنرانی پزشکیان، نماینده‌های: ایالات متحده آمریکا ، بریتانیا ، آلمان ، فرانسه ، اسرائیل ، سوریه ، لبنان ، عربستان ، مصر ، امارات ، الجزایر ، لهستان ، سوئد ، دانمارک ، کانادا ، ژاپن ، جمهوری آذربایجان , مالزی ، نیوزیلند ، استرالیا ، جمهوری خلق کنگو ،…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140501" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140500">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
✔️
✔️
✔️
✔️
تکرار تورنمنت سه‌جانبه؛ دو بازی دوستانه در برنامه پرسپولیس
❌
در جریان تعطیلات پیش روی مسابقات لیگ برتر، شاگردان مهدی تارتار تا پیش از ادامه مسابقات لیگ برتر، دو بازی دوستانه با چادرملو اردکان و گل گهر سیرجان برگزار می کنند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140500" target="_blank">📅 22:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140499">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
#فوروووووی
❌
با اعلام حدادی جام حذفی برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140499" target="_blank">📅 21:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140498">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=PrSViC37SFF8uzm61ov0rip6pexpnEvOIukpBE0naKS59UySq-m3aUxjXbonagpFFpE4Antv7A3YPyqkh1ryIi0nOJAMhBWUaTDOsPWPapRUkwXDqVJff3vVIHU5rWswETK0FIPjdxtrZMQ2iAwXbJoYQuj7riguQRTamvKBQGQAEb7ra4LWqxYARpSPW2Xj57uNKGFopzwwgMJUAkIJpf8D-8-GVF-e-eaxasmE-Q50dbMgNDIvF13DaT63tDH0T6xMQpWPAT1CTMH16uYox7AeZ25Ju-VsSXsT6znwOAOT9XkQLGGUrRNymWCiMrdieikuisVcCTOrZOlNuN8hkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=PrSViC37SFF8uzm61ov0rip6pexpnEvOIukpBE0naKS59UySq-m3aUxjXbonagpFFpE4Antv7A3YPyqkh1ryIi0nOJAMhBWUaTDOsPWPapRUkwXDqVJff3vVIHU5rWswETK0FIPjdxtrZMQ2iAwXbJoYQuj7riguQRTamvKBQGQAEb7ra4LWqxYARpSPW2Xj57uNKGFopzwwgMJUAkIJpf8D-8-GVF-e-eaxasmE-Q50dbMgNDIvF13DaT63tDH0T6xMQpWPAT1CTMH16uYox7AeZ25Ju-VsSXsT6znwOAOT9XkQLGGUrRNymWCiMrdieikuisVcCTOrZOlNuN8hkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجید جلالی: میلیون‌ها دلار خرج مربی خارجی شده اما برای ایرانی‌ها هزینه نکرده‌ایم به همین دلیل است که می‌گویم قلعه‌نویی از مورینیو بهتر است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140498" target="_blank">📅 20:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140497">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwcTh9g_o1eCxMyr7qEXj8K-v-zYYk8DKC--s9GYElS7yjaqodrQ_Zaap7OhqjHQSsqEh5pPEh7Uh53xh392ztUQgt2ZGv_QlW50qmfdG6jry4TU9phz22EXFZ25Xt4U9Q6G0qVu9aIgtHWisjWq-JBVRt5uRMk9Wvyc0HiucBkIHL_l-dBNN4Rg_y7CfbC1z7w5c38TbpcztsvfydPkF4k2X5QvbwYtGQPNrOMgfkMT1IAXPqqQE5IXe1bxCrEwIlp89NdaGefBu5hj5UicHbB2mri4lWbWkgX-MXfiSEb_-mW1U3iP6LK9EUyKSo57rLNkBuBdWAWT84rMj7yPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140497" target="_blank">📅 20:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140496">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=g1oucdqmONncpJzT_uvVeJ7dJWNSGEkfbgX43cAmezE4Bs__CSCEfUwGZpNv9WL-sfLJLaY9EFolFu6ZIGcTfMtRTQwulha1lBOFwTJ7dos3wtYoqE6xNdW4mhbMsllI6PwPNJ9lLCrq-7e31DbfNQQF3SLFTi3Yz6KALLpjoCXNczk3Ys1ws_tkSPO3Eh1okI4oNYtgreOCEpAf0ir-3qEWmNy3we0E7i_RN3cufc0gf2kW-JkR9o7SLOSvZS95QSdnUPjdFKc6q8sy_Epc8_9uqL-RLPzZ6z4nuuJxGp_EolL3kpWMBY4eQw2swRpdGZ8AfM5FMi-0av9HTxisxr8llvWxmpKWClUydNm5ar2oo30RUPuskAGoCcgXn8zCxq70B1y0zi82gng0rs0j2nnMP5FXk1rcP9FFNU82KolMELPx3PV0n1Sc0KiSoinlsDhpnc01UDYSg5_q9EK8SXBiwS6nBWzEMge6pvh2QJ6MaIBUebv0W2NHtqz5X3s0QKzZpH-hmjERap9ycBGZdGsiVK7em6j1HQcd3-Tj72etlqrYcVgy1PcrtSDCGC287TFsgTrYNT1p3w9rZhAI64_sFP_NRld2roOaEqQZ-NUkoqKpppsJ_W-lMi9llsxlaTkT-rae6ciF5QcQ9DFWKyR_5OxOFs06jzJY5ltX3F8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=g1oucdqmONncpJzT_uvVeJ7dJWNSGEkfbgX43cAmezE4Bs__CSCEfUwGZpNv9WL-sfLJLaY9EFolFu6ZIGcTfMtRTQwulha1lBOFwTJ7dos3wtYoqE6xNdW4mhbMsllI6PwPNJ9lLCrq-7e31DbfNQQF3SLFTi3Yz6KALLpjoCXNczk3Ys1ws_tkSPO3Eh1okI4oNYtgreOCEpAf0ir-3qEWmNy3we0E7i_RN3cufc0gf2kW-JkR9o7SLOSvZS95QSdnUPjdFKc6q8sy_Epc8_9uqL-RLPzZ6z4nuuJxGp_EolL3kpWMBY4eQw2swRpdGZ8AfM5FMi-0av9HTxisxr8llvWxmpKWClUydNm5ar2oo30RUPuskAGoCcgXn8zCxq70B1y0zi82gng0rs0j2nnMP5FXk1rcP9FFNU82KolMELPx3PV0n1Sc0KiSoinlsDhpnc01UDYSg5_q9EK8SXBiwS6nBWzEMge6pvh2QJ6MaIBUebv0W2NHtqz5X3s0QKzZpH-hmjERap9ycBGZdGsiVK7em6j1HQcd3-Tj72etlqrYcVgy1PcrtSDCGC287TFsgTrYNT1p3w9rZhAI64_sFP_NRld2roOaEqQZ-NUkoqKpppsJ_W-lMi9llsxlaTkT-rae6ciF5QcQ9DFWKyR_5OxOFs06jzJY5ltX3F8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140496" target="_blank">📅 20:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140495">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=VCydZREfKGx0RIT09T9slmCoJhuwJIYjlh5kFN9AyioMvixC5xyvL6PdqVDdQMQy4YMfULkKP_IX3fSvJkD9CvdfzXNaT8xcrxx8KPWqrBIpg9NVE1Qsp2DOhvf223Hnco9bHGPAAKmVVSpSL50loSO3Z0_WZcuFK-UX7eRx8GmNxFWHlKyTwZHSz9vYU33capkor9XsQT73D1VETQe7F2khj69COXISOWwXPsF9zExKKh3fQEeMzFtARgqaSYMmvfMODdSadTGYhinW9572KQWwg-YcpL0_U38TH8riufHVkbGCQ0_r8mlzXv5QKVajRTeGDO_E0mSVM4P2Y_boDy4hPVpB1_H934jS_k7fptZKSUxw9oXSyimrqc9MVihQsHt19V7zvF8cyF5IvHjrLCxgb3S_JNNpw7yCFK9f2mv4QbVH5mCcpmN0OPivzA6i2X8cuUZ7tAh40Dv-iAo3l9qvsgM8iGNowU-1Pd7mgDHq3Kc0QXMepHH1aNrmCQyC49-A_JpT-y5hwaSnOOB8TQe9FAN4HmxfIVC0MvTX6BXXoDEcZBtsOmrdWKbpbvlpgdu-Sgjvhl6e-yP-sUuDt0TzlxWzyUX3v6pOHqKYBRHyT5pRUDHNkh93gWAXjbTqlEnwKCmk6Bnh9pZi-Ko6eg3-pFvtTDJl_yRXNfyA7fs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=VCydZREfKGx0RIT09T9slmCoJhuwJIYjlh5kFN9AyioMvixC5xyvL6PdqVDdQMQy4YMfULkKP_IX3fSvJkD9CvdfzXNaT8xcrxx8KPWqrBIpg9NVE1Qsp2DOhvf223Hnco9bHGPAAKmVVSpSL50loSO3Z0_WZcuFK-UX7eRx8GmNxFWHlKyTwZHSz9vYU33capkor9XsQT73D1VETQe7F2khj69COXISOWwXPsF9zExKKh3fQEeMzFtARgqaSYMmvfMODdSadTGYhinW9572KQWwg-YcpL0_U38TH8riufHVkbGCQ0_r8mlzXv5QKVajRTeGDO_E0mSVM4P2Y_boDy4hPVpB1_H934jS_k7fptZKSUxw9oXSyimrqc9MVihQsHt19V7zvF8cyF5IvHjrLCxgb3S_JNNpw7yCFK9f2mv4QbVH5mCcpmN0OPivzA6i2X8cuUZ7tAh40Dv-iAo3l9qvsgM8iGNowU-1Pd7mgDHq3Kc0QXMepHH1aNrmCQyC49-A_JpT-y5hwaSnOOB8TQe9FAN4HmxfIVC0MvTX6BXXoDEcZBtsOmrdWKbpbvlpgdu-Sgjvhl6e-yP-sUuDt0TzlxWzyUX3v6pOHqKYBRHyT5pRUDHNkh93gWAXjbTqlEnwKCmk6Bnh9pZi-Ko6eg3-pFvtTDJl_yRXNfyA7fs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💛
🎙
حمله جواد خیابانی به امیر قلعه‌نویی: باید چیکار کنیم که کادرفنی تیم ملی تغییر کنه؟ نتیجه افتضاحی بود. آقای قلعه‌نویی نمیتونی تیم رو جمع کنی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140495" target="_blank">📅 20:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140494">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=tbG6y4lTKJfzrM0OrZzjae7t6IxW46FVsPD-M_yCxvjlY9cziRiCOhj-v5QrCkphIANcLEIbW33l5A2gOMlsNBMfcMCkspdfxoK-nv9hFo1DJTOg8ZK8LRU1ruNA7ktmvers6AeKxp-_QG1glPtBujDexpuKV7gLCbOONC99UjKosdtHiRSRmtWAaj5Xxsxna_sUguh4lb7GpoNLHHCA6u1ZkyCJZM4b9RPJQreDhCptKuQ_xnl1TrJWVHQ0vmIjJyukYczCTNc9CtHNLeLlbjZaR60udr4BnR_wRo-x8QMW65swFHKuFS5lgvWgaeK4IASUO8E42doNpUx11tERvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=tbG6y4lTKJfzrM0OrZzjae7t6IxW46FVsPD-M_yCxvjlY9cziRiCOhj-v5QrCkphIANcLEIbW33l5A2gOMlsNBMfcMCkspdfxoK-nv9hFo1DJTOg8ZK8LRU1ruNA7ktmvers6AeKxp-_QG1glPtBujDexpuKV7gLCbOONC99UjKosdtHiRSRmtWAaj5Xxsxna_sUguh4lb7GpoNLHHCA6u1ZkyCJZM4b9RPJQreDhCptKuQ_xnl1TrJWVHQ0vmIjJyukYczCTNc9CtHNLeLlbjZaR60udr4BnR_wRo-x8QMW65swFHKuFS5lgvWgaeK4IASUO8E42doNpUx11tERvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
💚
حمله شدید خیابانی به تیم ملی امید و کنایه به قلعه‌نویی: بازیکنان کره‌شمالی نه مدل مو داشتن نه قیافه آنچنانی می‌گرفتن ولی اومدن مارو درب و داغون کردن، بازیکنان ما چی یکیشون 20 میلیارد میگیره یکیشون 800 میلیارد میگیره اما دوهزار بازی نمیکنند و تحقیر میشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140494" target="_blank">📅 20:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140493">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXF2ZUFyhOQN93ZcWW1_FAuFpwQorto_cWUUJOiD2P412Jrtrzt8PBpuKUsXCqN5LpF08GEfyZVIiwCWLNLqzfw25h2Oc-reDsnOcgpA-GWlidlDSInsgf0EFnBrGo6ojRVIEAxKffPd9tOK39ZWmb7KobTaLUdTOP3EG78de9In2AqFOkLV7_3NUNCeTOBx9Rj1TX5CteNauTY2NKwt8XOd0Z6oKYaILAssVIWCBiBKgN3heCZxsoEKNWsrXYG7iMJ3d_bqfDvtB-utYINy91QX1-BjSrqOoz7xO_nmda7ThZP-KCTE6mrVj0161vl5QZbBcaGu6hvJ2L56lE5YNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Netherlands -
🇩🇪
Germany
⏰
Tonight 22:15
🏟
Johan Cruijff Arena
⚽️
آلمان و هلند در شروع لیگ ملت‌های ۲۰۲۶/۲۷؛ دیداری که از نظر آماری کاملاً نزدیک است. هلند در ۱۰ بازی اخیر میانگین ۲.۲ گل زده و ۱.۹ گل خورده داشته، در حالی‌که آلمان ۲.۴ گل زده و فقط ۱.۲ گل خورده است. در تقابل‌های اخیر هم آلمان دست بالاتر را داشته؛ ۳ برد و ۳ تساوی در ۷ رویارویی اخیر و آخرین بازی دو تیم با برتری ۱-۰ آلمان تمام شده است. از نظر روند گلزنی، هر دو تیم پتانسیل بالایی برای گل دارند؛ ضمن اینکه تغییر سرمربی در هر دو تیم، یعنی نخستین بازی رسمی یورگن کلوپ و ژاوی، می‌تواند بازی را از نظر تاکتیکی غیرقابل‌پیش‌بینی‌تر کند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140493" target="_blank">📅 20:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140492">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
✅
✅
سرگیف، اورونوف، آشورماتوف و ماشاریپوف از لیست ازبکستان خط خوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140492" target="_blank">📅 19:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140491">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
دو گل خوردیم .اونم آقایون شجاع و بیرانوند تقدیم کردن و دوتنه تیم ملی و نابود کردن   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140491" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140490">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⚡️
⚡️
⚡️
عالیشاه از دو سه سال قبل با خانومش هست، مثل کریس و جورجینا و حالا امشب عروسی میکنن، قرار نیست اتفاق خاصی بیفته، عروسی صرفا یه جشنه و قبلا با عقد رسمی شدن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140490" target="_blank">📅 19:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140489">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
این بازی ساعت 17/30 انجام میشه و بلاخره روی ماه اقای درگاهی رو میبینیم ...ببینیم چه جور بازیکنی هست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140489" target="_blank">📅 18:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140488">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
✅
✅
با اعلام باشگاه دوا یونایتد بانتن اندونزی، اوسمار ویرا هدایت این تیم را برعده گرفت
❌
این تیم فصل گذشته در لیگ اندونزی هفتم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140488" target="_blank">📅 16:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140487">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
❌
سعید الهویی : قائدی چون گفت بهترین مربی هایی که باهاشون کرده مجیدی و استراماچونی هستن دعوت نشده تیم ملی
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140487" target="_blank">📅 16:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140486">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
ترکیب ایران مقابل ازبکستان اعلام شد
⏺
علیرضا بیرانوند، سامان فلاح، علی نعمتی، صالح حردانی، احسان حاج‌صفی، سعید عزت‌اللهی، امید نورافکن، محمدمهدی محبی، آریا یوسفی، مهدی طارمی و دنیس درگاهی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140486" target="_blank">📅 16:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140485">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
✅
ورزش سه : زارع امروز جلو ازبکستان فیکسه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140485" target="_blank">📅 16:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140484">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
مهدی ترابی بازیکن32ساله باشگاه تراکتور که دچارپارگی رباط‌صلیبی شد هفته آینده پای مصدومش رو به تیغ جراحان خواهد سپرد و تا اوایل اردیبهشت ماه سال بعد دور از میادین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140484" target="_blank">📅 16:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140483">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
فدراسیون به باشگاه گفته که مدرکتون برای یاسر آسانی کمه و اون مدرک اصلی و قوی که ما میخایم رو ندارید شما ، حالا باشگاه از طریق یکی از ایجنت های ایرانی یاسر آسانی یه مدرک فوق العاده قوی رو کرده که فسخ رسمی این بازیکن با استقلال رو نشون میده و فدراسیون هم…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140483" target="_blank">📅 16:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140482">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140482" target="_blank">📅 16:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140481">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
❌
گفته میشه عربستان و چند کشور منطقه دنبال فشار به فیفا برای تعلیق فوتبال ایران هستن؛ اتفاقی که می‌تونه باعث حذف تیم ملی از جام ملت‌های آسیا بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140481" target="_blank">📅 13:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140480">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jyi2rwwfINdtKh9RmcsnT32j2W1Vl3QkhoVqft0qzUhP-sFy0x5J42EmTOV8kfM0v0IvaJdSEdRZWqDaFFMXtZ0PegDn_AOFn4Sp09kip6gu_Nv0yild3OWqdo2xS5LQL_31ICQaITAigxh-dKNVZGKuJ330rCvygZ26rlsKnV_pxk-I_n2vrP4ORs6GuZt080ZpXzY3XOYUx5npxWhBLff5jv0iap7o7OeHKhb0TOKTe_DeZ0EsM9mKiGfutkSc_STgPBLspQrgGKwh4mJl1krF8sofUD4BXauTPDrdzjUxUgf8wdOrMmuv1AnuqGqO_qfPjLinDh1doGNtOmOXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140480" target="_blank">📅 13:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140479">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwuuVQUSI76xhMgFzXbMYEu_gMwur0ZfSDlUQgv8jdACkknOZ4I6McfTmdIBweh51jISkUa8MSZpObhN6xnNIUGzR3ZRu_bccV3-95RYjWn740uL-kfygkvMSxMTdzUzFrVbucWPIHOK924o69jv3udAqBfa9B-uP2zNJtcJLRaZ0XtfpYDFnYYWCTDk4a4r2YFz0NUyuRgBAuK84UahrIpI6ARWIsLofx6r4I6SvdowQZBmuF45MJu-WS_--7P4F8DNEHGOk54tGa24oMuVG8fC83bxqeXFhsgPWR3_u38hpM9SmZYUauuMeKfCAMK8EupbswUQ3pmuyutYhBV77w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
از ریفوی ژاپن تا لیسبون؛ شبِ دوئل‌های حساس
ملی
🔥
⚽️
فوتبال امروز با دیدار ژاپن و اروگوئه شروع می‌شود و در ادامه، ایران وارد یکی از متعادل‌ترین بازی‌های روز مقابل ازبکستان خواهد شد.
هلند با آلمان و صربستان با یونان از دوئل‌هایی هستند که فاصله تیم‌ها در ضرایب هم کاملاً نزدیک است. در سوی دیگر، نروژ مقابل دانمارک و پرتغال مقابل ولز؛ جایی که پرتغال با ضریب ۱.۲۰ واضح‌ترین برتری این جدول را دارد. یک روز پر از بازی‌های نزدیک، ضریب‌های متنوع و چند تقابل که نتیجه‌شان می‌تواند جذاب باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای امشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140479" target="_blank">📅 12:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140478">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
✔️
بیرانوند برای فرار از سربازی، این‌بار به بهانه خالکوبی، دست به دامن کمیسیون اعصاب و روان شده تا شاید با برچسب اختلال روحی، کارت معافیت بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140478" target="_blank">📅 12:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140477">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
چمن شماره ۳ آزادی به مشکل خورد!
❌
❌
بعد از دو سال تمرین پرسپولیس در این زمین، چمن سفت و نامناسب شده و قراره به‌زودی زیر کشت بره. احتمالاً سرخ‌ها چند ماه آینده تمریناتشون رو در شهید کاظمی و زمین شماره ۲ آزادی برگزار می‌کنن.  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140477" target="_blank">📅 12:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140476">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
✅
ورزش سه : زارع امروز جلو ازبکستان فیکسه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140476" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140475">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgOh59vkVV4m6EteulApPZQf7WEeCrg7i5OSX0u6OsuKWeUcdzadmZuQQqOVnd7PFtY_aOgQHafGCtsY2Hl3yfFxZX86cplKRAm1yqnR5NW7QoE-Vei0-dScC88AzVor2ewEHgElFiiW7tDI3bWO2Pwn5QDauS7LonpMmiX123hMC51XtEK1JM_tKOY2bR-8fvQ37wNUzclGx_spHlxvkFV2GdSyv0IHGeweLTGS8aJ9RNZLyR_Dj5hSn_Owwv7ONcKFIFmZUAuNHD_FrBDSvqUdgLlYfB_PdYfq0D_n0MyVGYdUxVQdjzhJ3o9mfkXwXBGLId8Ncxe2ZnMGp8YMzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
| طرفداری:
🔴
⏳
🔄
تارتار اصرار به جذب رزاق‌پور دارد و ولکن این بازیکن نیست
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140475" target="_blank">📅 11:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140474">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
فووووووووری از قدوسی : کمیته انضباطی به باشگاه گفته مدارک شما برای محکوم کردن آسانی کمه و اون چیزی که ما نیاز داریم ندارید.. که یکدفعه باشگاه مدرک جدید و آس رو کرده و فدراسیون آچمز شده و هنگ کرده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140474" target="_blank">📅 10:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140473">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
بازگشا، سخنگوی باشگاه پرسپولیس:
✔️
از فدراسیون خواستیم رسیدگی به پرونده آسانی با حضور وکلای ما و آنلاین باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140473" target="_blank">📅 10:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140472">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
⚽
طرفداری: پرسپولیس در آستانه‌ی تیمداری در لیگ دو و شهر مشهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140472" target="_blank">📅 10:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140471">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140471" target="_blank">📅 09:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140470">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8wBRqS1I_tMxb_h26tmPktuMKdagcNrX_Tak1uIoTboKxehXofB5Ds7BnC7fD_rzluWHEZvqWwEsB3AQhMSREQH99YcrBOVrG7mUW5HdRickBl9FYchrU7h9uW6yTp0Rpr5IZ2UEv52jNaUroDlnADzYmw36l0FCrxWcyd1Y6YbPW13o9N93DsW4lFoIUA0Sf1a0fDF8y5I1sUrcHbgAbSGY_SCf3vpBNEs8y_XaTZ6n8TCtgDLQERYSABpCOwhCgbw0id6cNz_ea7ilBiUZfthCHZLkVWUVdwOxD-1v_-1cOod9MKdzzrATyOBngldbbpGIu_Z0_LCletRkC9dMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140470" target="_blank">📅 09:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140469">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBQ44vdWOBctaNl8TSMS5NzBmQ8Se2jMA21BJj6zUeXfSsNNJohVlsGciBSG3JjY7Ys27xQ9aXxfHGRY5ey8QNCPmZlDyk2RRKplsN4Jw9KBDsqo_BpGOUNnLjWRX-jgphZNC7w0lZsu3DwHZIP8aMWIYndTMDJ4zAWBXBOt7vPjDVZxPPWbIAFdFOTIj7TWjoIOop1elXDFmFax39CcGDyYqN36V5wS0KaxieWAOLqnLZltQYngbsZKTdCMsT86i-L56PO8j5aSNqPAgp7oO1-uAqCszETw8Fv5XyaWkQVYtZdUyx0corQzKcTZpLCF7oUKPGrt27tj5bMi9gTd1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ایران و ازبکستان؛ محک جدی در یک روز دوستانه!
[
ایران
🇮🇷
🆚
🇺🇿
ازبکستان
]
⚽️
ایران و ازبکستان فردا در یک دیدار  دوستانه به مصاف هم می‌روند؛ دیداری که بیشتر از نتیجه، برای محک ترکیب و هماهنگی بازیکنان اهمیت دارد. ایران معمولاً در بازی‌های مستقیم و انتقال سریع خطرناک‌تر است، در حالی که ازبکستان با مالکیت و بازی ترکیبی می‌تواند فشار ایجاد کند. با توجه به ماهیت دوستانه، احتمال چرخش ترکیب و افت‌وخیز ریتم بازی بالاست و آمار نیمه دوم می‌تواند متفاوت باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140469" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140468">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
🤩
فرهیختگان:
بزودی قرارداد اوستون اورونوف با پرسپولیس با دستمزد 2.2 میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140468" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140467">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqATBsfzJczBOkvByjYge57BXdo-yIawbUyErUfnd81d0vkXQz-EoXJ9MKkRv-sstk0sBVrmPBQg7pRT2jpz06GbVRveQ6oPYu4b67nIn19rkaMq9V-d_jynBll-SXYw2Q_eveQpqIdNZOHEdwmQ_KZJXQU-PR0_4uPofeJOgvqvtKXHaqlQ_CYZKIxUZ_8itJ_72EO7i2pIQdJGknUyXL5LCZxw439dXjUb5keOv6kZAppBdNQrmiPkv-eLAS8tETFCah4IdKjteRod2nZc48cwBR3FGZUmPTIk3Zba2nBeA354Nf6w_PfFHoRdByGnEDEusowIYT5OIah7N-rcrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
❤️
پرسپولیس در نامه‌ای خواستار برگزاری حضوری جلسات پرونده آسانی و ضبط کامل فرآیند رسیدگی شد
‌
📌
باشگاه پرسپولیس در دو مکاتبه رسمی خطاب به رئیس فدراسیون فوتبال و رئیس کمیته استیناف، خواستار برگزاری حضوری جلسات رسیدگی به پرونده شکایت این باشگاه از یاسر آسانی، حضور رسمی نماینده باشگاه و ضبط صوت و تصویر کامل جلسات شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140467" target="_blank">📅 01:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140466">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🤩
👤
🔴
فوتبالی: تارتار بعد از دعوت نشدن کنعانی نگران وضعیت روحی اوست و قصد دارد جلسه‌ای با کاپیتان تیمش در این باره برگزار کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140466" target="_blank">📅 01:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140465">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
⚽
طرفداری: پرسپولیس در آستانه‌ی تیمداری در لیگ دو و شهر مشهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140465" target="_blank">📅 23:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140464">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXFzlQ-j4T32HAHj1mJRWacKKfg9ORiMsQ4Xqo-JvAqvy016jb0-huKpE-8glIRoV0p-G5G94Qe8Vlna8tkvMU64mcuP5buZQVZhizk1fRZEp6cCw4Vh4VoDg79OTrwjDlAfPmoyyksb3ZevO0M_tZ9aC2Nv2M3MoE_RF9SbOilWONRaa-4FEfK44X7FHfNIIbMBK7eyOh3M_JH9be5DdZLrtCr8mGNRd74X0JLKuSwwSIEi-ZDAPJetntw1uUgfOjjjTqNRZYcK2UMd7nb_CKuTtrQbqbNBe5rBFd7VPc63IvxDtgCcJWzzP57syYoCNobpZe6EfW9pWyeV7zvpsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🇮🇷
سه درخواست رسمی پرسپولیس در پرونده یاسر آسانی
🚫
باشگاه پرسپولیس پس از ثبت لایحه تجدیدنظرخواهی در پرونده یاسر آسانی، طی نامه‌ای رسمی خطاب به مهدی تاج و ارکان قضایی فدراسیون فوتبال، سه درخواست را مطرح کرد.
🚫
این درخواست‌ها شامل برگزاری جلسه استماع با حضور نمایندگان و وکلای باشگاه، ضبط کامل ویدئویی جلسه رسیدگی و فراهم کردن امکان پخش آنلاین آن با هدف افزایش شفافیت و اطلاع‌رسانی عمومی است.
🚫
باشگاه پرسپولیس ابراز امیدواری کرده است این درخواست‌ها با توجه به اهمیت پرونده، مورد توجه مسئولان فدراسیون و ارکان قضایی قرار گیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140464" target="_blank">📅 23:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140463">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kDvFNl76mQ9nuOPeX4yjjt5BnqgkyuITxu-XqFLKsemLQmfe8f23cE3G0LCL9nzAy6CjtgMnN_7JpY83NfYCSOvmYuI6x_PYFPI_WpT-2XR8yHaibGxVCiVBqsCd3OSfYzFePrVEgbJlL-iN3iH1rC-7fSEd2rAyUVGlSXIBNVcntYzSeuuMzCBl3DthRNIVDQsnNxfr19OrQuo7Ip4-RZvW0iwuPvMDk7kmwhIlbEuawqUWLwftCBrRIh0OyCXyn3dqMqAOIhb2OFK4mtT7U-TyNUi16VlMmAydAtS7c3fpN8A_muJdRKCrnFSVaBzeQd3nQuehAprTagH85mbeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سعید آقایی: در پرسپولیس کم بازی کردم اما بیشترین لطف را از هواداران این تیم دیدم آنها را از صمیم قلب دوست دارم
❌
بعد از مصدومیتم در نساجی کلا فراموش شدم تنها دلخوشی‌ام در یک سال اخیر فقط هواداران پرسپولیس بودند که جویای حالم میشدن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140463" target="_blank">📅 22:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140461">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⭕️
⭕️
⭕️
🚨
🚨
🚨
در پرونده‌ی آسانی، پرسپولیس در استیناف پیروز میشه/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140461" target="_blank">📅 22:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140460">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULvg57SWRDkbrve1sprJZn6Aytqb6m2A6x06D4LDFh83h3OVZUjzvUuZIs6QKd5J-GTwzmavsSLJeRZ8jqMTKUM0BuBIQ6BMYtMjdE0_dC5h0tpVRA39lAKkzu5Zd8qeEtgokbnb7OiCBHyCM9X3zpdyD7m8W09GDiDWbTPdIBhaMAHG6O4_wChaPVUG5rH6W9isRmVTWy_ixeyaHTYWT1dMdjHrMfdEAR7opxHLrb3I2mBgQ1e7gmolbgUNY66utPTPjf9Wcy1nkUHFXMHxpw7PIJizmbpyTp7q0tRch_pofTzbYt8xZABhqCJlDwAZ1oxxLp1hQ6bHK-e6s15d4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
✔️
حسین عبدی: مقصر اصلی شکست من هستم، اما بچه ها با توان فردی خودشان فاصله داشتند از مردم ایران عذرخواهی می‌کنم
✔️
✔️
باید به کره شمالی تبریک گفت؛ آنها خیلی خوب بازی کردند. باعث تأسف است که در این گروه سخت نتوانستیم پیروز شویم و به مرحله بعد صعود کنیم.ما…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/140460" target="_blank">📅 22:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140459">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
ویدیوی‌کامل سخنرانی فوق العاده و طوفانی پزشکیان در سازمان‌ملل  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140459" target="_blank">📅 22:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140458">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
حسین عبدی: از مردم ایران عذرخواهی می‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140458" target="_blank">📅 22:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140457">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏅
🏅
پرسپولیس مدارک جدیدی رو به کمیته استیناف برای 3_0 شدن بازی دربی ارائه داده
⚪️
حتی اگه رای استیناف به سود آسانی باشه پرسپولیس تمام این مدارک رو به CAS میبره
✍️
همشهری  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/140457" target="_blank">📅 21:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140456">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDNWHt4JwjYb79q1dZ_rSVo1XGTg2Sy4pL6HPATFzmbpXiLtaqOexsQEgWep2YgE-QeNIGvsBb7acewTmsPIuErNjIMdyopiq11Qc-gKHnXGisyz9x7Ho3dNRdAHp7Wk4_DOMuN0Veetr4saU9oz2ftrH2RPV8kmNtF5WTUro2ZiJmwtBliG6Gn2Q6I-DqAjx1DbtZp-TXjXOhNdNPovU5wqugbBgfh_t8VJKklCjVc8KltnzjeSCtDvNEgupT6U5WmGDo1KNOvFTItzXTQCxbuV97edg8sa6rESn3A6f0ujucFmXw6v8OBYYJjsuuU3PRslfN4gXfwye6fXzpNYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ایتالیا مقابل فنلاند در یورو والی؛ جایی برای غافلگیری نیست!
🏐
ایتالیا در این مرحله با ۶ برد متوالی وارد یک‌چهارم نهایی شده و در مرحله قبل دانمارک را ۳-۰ شکست داده؛ فنلاند هم بعد از یک بازی سنگین ۳-۲ مقابل یونان صعود کرده است.
ایتالیا با سرویس، دفاع روی تور و تنوع حمله دست بالاتر را دارد و روند ۶ برد پیاپی هم نشان‌دهنده ثبات بالای تیم است. فنلاند در بازی با یونان توانست در لحظات حساس برگردد، اما فشار حملات ایتالیا آزمون سخت‌تری برای دریافت اول این تیم خواهد بود. با توجه به اختلاف کیفیت و فرم دو تیم، ایتالیا شانس بیشتری برای کنترل مسابقه و برد ۳-۰ یا ۳-۱ دارد.
🏐
اوج هیجان همراه با اسپورت‌نود، پنجشنبه ساعت ۲۲:۳۵ دوتیم ایتالیا
🇮🇹
-
🇫🇮
فنلاند به مصاف یکدیگر می‌روند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/140456" target="_blank">📅 20:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140455">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
#تسنیم؛ بیرانوندیه پرونده تو کمیسیون پزشکی ایجاد کرده و گفته من چون خالکوبی زدم مشکل اعصاب و روان دارم و باید معاف شم
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140455" target="_blank">📅 18:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140454">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neai_hTTB6vQyY3XzfuZOtZewAQUE__pgSEPuHvmD6VDNpeovHm5a6VPouyIp0mYR8y7ncvmlyXsB24ZLgZT9rwHrZM3VIjHRLpf88Q0n8pu1XLS4dMO0PPQyQZnf68RtbT9LkC6lx9X5JweseLVAZ5Ol3bvuXzdWn-81UsFRTRGvX1vZ5cUSgKz8lr9xT6QAE0uVRivra-xpjH_AXtr2BwU_jJpOnbs2T0pPsC08Tpcyi_XMSuVsc5369etiarIbV0p5qsZUOYwJQjHHNRXniVk6CybwL0uj5U7fuec4cYDdJcudJA6gyuIujlUy3maKajc48dfPWK0pbpuihLMHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
⚪️
رنگ پیراهن دو تیم ایران و ازبکستان برای دیدار دوستانه مشخص شد و ایران قرمز میپوشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140454" target="_blank">📅 18:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140453">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
ویدیوی‌کامل سخنرانی فوق العاده و طوفانی پزشکیان در سازمان‌ملل
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140453" target="_blank">📅 18:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140452">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwRhr1PVFPQT5cmgKe6dyqJVUFJMMnUZ_sXNQChg5JR7HY1qCW7nzf05HcziVDnQWAiWWnhjm8eAqwCl-bKT9_VFlGwTtt43mKxZqX9Pkz4vOH6t-1R6PM8EtSebjMcr8sIxmKymSF75Y-3LirhN1uJLdMJwvL3TVFry-qApYZRyrRFrdD2N6IT0UyjBF8ul3wyOutdFPEBGE4T9PHbF1mtyiRd2EPBzvs69OXQyu2IHN8BKfOxqad5kE5Uhql2rm2dNi-B03bpw1QfXZ7vqUdGShLrlVQN3082PWlmniSQlZkRZx1B3iITcmRGtCCLm4i1_kSx0jNwtXZ8M5ezPxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ارزش تیم امید ایران: 13 میلیون دلار
🇰🇵
ارزش تیم امید کره شمالی: 2
میلیون دلار
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/140452" target="_blank">📅 15:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140451">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7fB2_aqdC79SWrVKQTTA4F51Ga5w6olEikaOk-oxbBWJAeZX7-4K54rbzy_9fdgLNn1vEDK7hVMczJ-jrmWE8BcBpu_YE4h0kiEZIHmK1bMlQTeKM8WJGu-qH5_ixcM-KAxQk6P-XKWJ0GrnEUAgw-5wM3GlNChH08z_PFg0mLdcT_samm8p2RjNj3bEcg7kitCPa53GfBcj4RBPAlxrwY4ChuWljk8bDQFlOmaSnhhfD73q3sXNUCvd7fzREvmcrHuGtb0e29MEgehi5jG3078siMPwun5bXy4uNALSIHIhX1jTQcgHSPEnLeYqexp7krLtk7PoxM8yCRurRJtmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🏅
پرسپولیس مدارک جدیدی رو به کمیته استیناف برای 3_0 شدن بازی دربی ارائه داده
⚪️
حتی اگه رای استیناف به سود آسانی باشه پرسپولیس تمام این مدارک رو به CAS میبره
✍️
همشهری
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140451" target="_blank">📅 15:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140450">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIY2lDn15M_RjJ9Hy0HztGjUeEY9VngGA0J4qnN_cjHBgqPaluHWpDUF5hiBeKR4jTzOI6Mp1nBOlDNzWFPfOefdoQp7h2uF7lKt5C5zg-qWqXdVX46LH-vRQ_V3_718cErXu-12Vj95wZDC5how_I7EeoT7BY1SwPDhkHkR3EbvWI43UatfJGuTe0FlJZOai_dg1UjbZs4EZWvnaeBi3hpZIt9hS1zUPmmSEgnNACLTqXb3EMVciSVdV4CKPt1pBxto8z7Fom6i-C8xg4jgXAOx2wdnvbiJ_jY7TJ9XQZCvDEY1qcdHUILjc3kjKOcZYHcCUSU9k3C9wy6mguMzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام ملت‌های والیبال اروپا به اوج رسیده!
🇧🇪
Belgium -
🇸🇮
Slovenia
⏰
Tonight 17:30
🏐
بلژیک با فرم هجومی خوب و درخشش فره رگرز وارد بازی می‌شود؛ مقابل چک هم ۳ - ۱ پیروز شدند و ۱۵ امتیاز از دفاع روی تور گرفتند. اسلوونی اما بعد از برد قاطع ۳ - ۰ مقابل صربستان، اعتمادبه‌نفس بالایی دارد و موجیچ، پایِنک و کوزامرنیک می‌توانند فشار زیادی روی دفاع بلژیک ایجاد کنند. نبود تینه اورنات به‌دلیل مصدومیت، یک تغییر مهم برای اسلوونی است؛ بنابراین دریافت و عملکرد موجیچ اهمیت بیشتری پیدا می‌کند. بازی از آن مسابقه‌هایی است که احتمال کشیده‌شدن به ۴ یا ۵ ست در آن بالاست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدار هیجان‌انگیز امشب رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140450" target="_blank">📅 15:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140449">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
به نقل از رسانه ها دنیل گرا بزودی با گرفتن ۲۵۰ هزار دلار از پرسپولیس جدا خواهد شد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140449" target="_blank">📅 14:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140448">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
❌
فووووووووری
🚨
محمد حسین کنعانی به علت مصدومیت دو دیدار بعدی پرسپولیس برابر صنعت نفت و خیبر را از دست خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/140448" target="_blank">📅 12:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140447">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
🇮🇷
بهت و تعجب ملی‌پوشان امید بعد از حذف از بازی‌های آسیایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140447" target="_blank">📅 12:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140446">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c126edce8.mp4?token=L6VQR7KtW3nl_aD93JOh6VZ8QqFYrcdTPlqAx8SwtAM4SPYuD43pXTOa448E0oodl5pbYzVH1-Owi0hGcst-bIcdY0NWPJgslc4_j5DdXBSEy31E--K0S1zBrF7EzHCAE1-_UOy43r8Nkkjj_4FJCS2MtDV14pLGfY7CbFJEFGa6QN_aBpUeqAtgAMjoK95LkgHN9ixiX_gAB0W1zIBjNtos6LSuW9l6Tdxhn-dRvVx1lPy0br5tpByX19DQ5wNqu34hq-7CJlDK7Sk0-OzwnVCGI7-VFJbkEq7lAn-aGOxx4ASo0G6GRDJZMn0ELVAvDgx2SBlZSjgrQhjDuBFmyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c126edce8.mp4?token=L6VQR7KtW3nl_aD93JOh6VZ8QqFYrcdTPlqAx8SwtAM4SPYuD43pXTOa448E0oodl5pbYzVH1-Owi0hGcst-bIcdY0NWPJgslc4_j5DdXBSEy31E--K0S1zBrF7EzHCAE1-_UOy43r8Nkkjj_4FJCS2MtDV14pLGfY7CbFJEFGa6QN_aBpUeqAtgAMjoK95LkgHN9ixiX_gAB0W1zIBjNtos6LSuW9l6Tdxhn-dRvVx1lPy0br5tpByX19DQ5wNqu34hq-7CJlDK7Sk0-OzwnVCGI7-VFJbkEq7lAn-aGOxx4ASo0G6GRDJZMn0ELVAvDgx2SBlZSjgrQhjDuBFmyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
بهت و تعجب ملی‌پوشان امید بعد از حذف از بازی‌های آسیایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/140446" target="_blank">📅 11:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140445">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZ8lck3thH7d12aPPp7n-2XE3sISryCW-327cukIdqEvvyUbbZh4uyWhRZ4xAR1q0CYPoQhR4CBde0TH6NHX71hHJntAbST1qO6b7otIpAmySmpwc-uVV2hsKwwfLmR1nSNMdGed3DBSCrZDYBNmebjYdXVCwxON_DKodVC0RGBvRIk1hCNhF66Ue7KEACsO6OVcDVi6Tq0igWuWpZIWw244_AkvlRQ5z1sNWLMOtvCmr_ZatwQjvM7NpdL8jg9YcqqxIq9S029Hf7c-_q3zwt8gWRSYZo7hPSddqO49fSG-s5FKZfCfJZQgZg6bH1hFQruVF502n5iRAfstKdSPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تیم ملی امید‌ با این کادر با دانش به کره شمالی باخت و حذف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/140445" target="_blank">📅 11:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140444">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
آقای حسین عبدی ..بهترین تیم امید و ریدی توش و تیم و حذف کردی و از کره شمالی چهار گل خوردی ..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/140444" target="_blank">📅 11:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140443">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
گل چهارم و ببین ...از وسط زمین طرف تک به تک شد ...این چه تیم امیدیه ..آقای عبدی چه گوهی خوردی با این همه جووون با استعداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140443" target="_blank">📅 10:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140442">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29d58e82a.mp4?token=Rwc-rTEFHWOrrgPiNStUgREfSa3kzN4E7TqZulvsE4_zvwVSxE6uBeRsjeKNT2DEKcgxdv4CojPAKGKFPrhmuTJQvGE1yo75CD8IDsPEW2ufFmObb8iOnjuf1JhLbg1SktjjEEsebzsEtiSyGsmnhRSa8hJnPQTPDZuVVhjX5nNrc-J6V-05A7fCec6fUwIixjhxPjhDXa-RV_84RzMMvS7Tkpe5LmeoBgZBG1j7Li2OzOE52cBi3bWKNOK9f-EIsSRzQ9M8RuzXs4r9p9TQCzZVzjVDekgPE5FSIfF555DcwDkXkQPrhAUQsjljVak4USIhFjZ3xdGjEQnFwxWJQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29d58e82a.mp4?token=Rwc-rTEFHWOrrgPiNStUgREfSa3kzN4E7TqZulvsE4_zvwVSxE6uBeRsjeKNT2DEKcgxdv4CojPAKGKFPrhmuTJQvGE1yo75CD8IDsPEW2ufFmObb8iOnjuf1JhLbg1SktjjEEsebzsEtiSyGsmnhRSa8hJnPQTPDZuVVhjX5nNrc-J6V-05A7fCec6fUwIixjhxPjhDXa-RV_84RzMMvS7Tkpe5LmeoBgZBG1j7Li2OzOE52cBi3bWKNOK9f-EIsSRzQ9M8RuzXs4r9p9TQCzZVzjVDekgPE5FSIfF555DcwDkXkQPrhAUQsjljVak4USIhFjZ3xdGjEQnFwxWJQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل چهارم و ببین ...از وسط زمین طرف تک به تک شد ...این چه تیم امیدیه ..آقای عبدی چه گوهی خوردی با این همه جووون با استعداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140442" target="_blank">📅 10:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140441">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
آقای حسین عبدی ..بهترین تیم امید و ریدی توش و تیم و حذف کردی و از کره شمالی چهار گل خوردی ..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140441" target="_blank">📅 10:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140440">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
تیم ملی امید راهی ناگویا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140440" target="_blank">📅 10:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140439">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
چند روز پیش یکی از نزدیکان میلاد محمدی به ما گفت؛ این بازیکن بخاطر شرایط خانوادگی قصد بازگشت به ایران رو نداره///طاهرخانی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140439" target="_blank">📅 08:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140438">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWEqLeLBPejefCTVWr5T-fuwoRl0-lTaRvR18R0Y48kQepTDZ7--ZLk8WhEBdY9Ql3LZlfYe8KNR_G4QhoqyjohCdRsFFgVVg5W7hhEWQ3wJDeU6XvYQf_qkCXh1qeKTk7JeoYV8WizyJXigAdG8Aan5Y0oh9tpAmkB9ofEE4zrguSFch9OUJWkV2ycuZp-A-pUeE4JkpIUYKoyDQ1syo2DtuFBubcTReuVHjZFQICmfN_f8RTXP_z98_mWVppKaLGTqPyvLBEPj8-HxbxVzsu8FAxVJHaaTtUc-h1qP4O7yRz4eYlyEvuBgos8DMKgL7P96sSusZ90RMYbOASIflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🤩
خبرورزشی:
🔴
🔵
🇮🇷
پرسپولیس و استقلال در نیم‌فصل برای جذب محمد قربانی اقدام خواهند کرد
.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140438" target="_blank">📅 08:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140437">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
✔️
✔️
علی علیپور به دلیل مصدومیت زانو حدود سه هفته باید مراحل فیزیوتراپی و آماده‌سازی را پشت سر بگذارد و در لیست تیم ملی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140437" target="_blank">📅 08:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140436">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
ترکیب تیم امید ایران مقابل چین
✅
✅
محمد خلیفه، دانیال ایری، امین حزباوی، فرزین معامله‌گری، ابوالفضل کوهی، امیرمحمد رزاقی‌نیا، اسماعیل قلی‌زاده، عباس کهریزی، مبین دهقان، امیرحسین حسین‌زاده و پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140436" target="_blank">📅 08:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140435">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
🇮🇷
🇮🇷
صبح اولین روز پاییزتون بخیر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140435" target="_blank">📅 08:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140434">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJ59Q8-sh_h5F7wmZ7tlwCehmfubmNvkJmb8uW7KhhdEe45uf7wovDWiPy15cbhBuYuTWKyL4mh08Q-a8YNNYkYT85oxbwtu-sPYgOUIpiYnHvv69apqhRAdnSQMWAGyToIGRy7SFWKGUeiQ-K9g3DgNmwUUT1nqvHAIDYq64mu1nA0o-i1vMP6gOwvgeCu7XttxjjAdwjwPodAes2kE1wy6_Bek_wMQ8WkEYRcfGWUnSSKla4ufpmyb12mavcAIlwMTJPQ-lFZLhRTQFA3ai9G9v5W2RLPwWKaiynurHoJ9Dqxt6l1R4ZOCCOxR-DxjHzKv812greWUU6R8lvMlbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
IRAN -
🇰🇵
North Korea
⏰
Today 09:00
🏟
Wave Kariya Stadium
⚽️
تیم امید ایران در برابر تیم امید کره‌شمالی در بازی‌های آسیایی؛ جایی که جزئیات می‌تونه سرنوشت بازی رو عوض کنه. ایران با تکیه بر مالکیت و بازی ترکیبی، دنبال کنترل ریتم و ساخت موقعیت خواهد بود. کره‌شمالی هم با انتقال‌های سریع و بازی مستقیم می‌تونه دردسرساز بشه؛ انتظار بازی نزدیک و کم‌ اشتباه میره.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140434" target="_blank">📅 06:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140433">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
فوووری / میگن کنعانی مصدوم بوده و رفت شمال و از زانوش تو تعطیلات زیادی کار کشیده و پاشو بگا داده و چند هفته ای نیست ///فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/140433" target="_blank">📅 00:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140432">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/140432" target="_blank">📅 00:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140431">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd12c24d1.mp4?token=bCN6i7m12Cs5Ebdcugc663bXYx_SEuzY3Sq7XOBASgmErKewConYrqKRApcikmSLVxziTObluEzKURQ64-3RwgnWtpjnU9iLNeYkPYlcaheWTZ802Mm4bzR7lVoMoJJrwcKK_Gg7iC-k6GnUcGea0QeKMdB5lnE8BwbFwQqz-5bQfP-PYV50PuEl_zL2WJpqdtt-3rZkyRnnV5znQw43L9Ge3T5LJNK53QLjGrjWjfxZmndXtUvugXymHnUHehXvnbmdmi3saC2SqtuY_PYn8jlNLgFeQ_QTdtOxZN6Pt5MMwdWtdsEz5_MNPL4nukyBtQ9GXJJwpwTkhyYNaZKidw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd12c24d1.mp4?token=bCN6i7m12Cs5Ebdcugc663bXYx_SEuzY3Sq7XOBASgmErKewConYrqKRApcikmSLVxziTObluEzKURQ64-3RwgnWtpjnU9iLNeYkPYlcaheWTZ802Mm4bzR7lVoMoJJrwcKK_Gg7iC-k6GnUcGea0QeKMdB5lnE8BwbFwQqz-5bQfP-PYV50PuEl_zL2WJpqdtt-3rZkyRnnV5znQw43L9Ge3T5LJNK53QLjGrjWjfxZmndXtUvugXymHnUHehXvnbmdmi3saC2SqtuY_PYn8jlNLgFeQ_QTdtOxZN6Pt5MMwdWtdsEz5_MNPL4nukyBtQ9GXJJwpwTkhyYNaZKidw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
زهرا خواجوی: گذشته ام را نمی توانم انکار کنم ولی امروز پرسپولیسی هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/140431" target="_blank">📅 00:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140430">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
بازگشا، سخنگوی باشگاه پرسپولیس:
✔️
از فدراسیون خواستیم رسیدگی به پرونده آسانی با حضور وکلای ما و آنلاین باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/140430" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140429">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
❌
امیدواری پرسپولیس به محکومیت آسانی
❌
❌
از باشگاه پرسپولیس خبر می‌رسد مسئولان این باشگاه در مرحله استیناف مدارک جدیدی را نیز ارائه کرده‌اند و امیدوارند با بررسی این مستندات، رأی مرحله نخست تغییر کند.
❌
❌
پیگیری‌ها نشان می‌دهد مسئولان پرسپولیس موضوع این پرونده…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/140429" target="_blank">📅 23:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140428">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
تیوی بیفوما:
✅
• سرعتم روی گل به ملوان ۳۷ کیلومتر بود/ سال گذشته اتحاد تیمی نبود و شرایط خوبی نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/140428" target="_blank">📅 23:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140427">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
بیفوما:
🔻
از لقب میگ‌میگ خوشم می‌آید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/140427" target="_blank">📅 22:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140426">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
تیوی بیفوما: مدیرعامل در اردوی ترکیه از من پرسید چه چیزی باعث اذیت شدنت می‌شود؟/ تارتار به من گفت به تو اعتقاد دارم و شرایط نسبت به سال گذشته، تغییر خواهد کرد. هدفم قهرمانی با پرسپولیس است و نشان دادیم می‌توانیم قهرمان شویم. شرایط امسال خیلی بهتر است
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140426" target="_blank">📅 22:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140425">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
تیوی بیفوما : بهترین دوست من در پرسپولیس حسین کنعانی است / شاید انگلیسی خیلی خوب حرف نزنه ولی خیلی خوب با هم ارتباط میگیریم / یکی از دلایلی که کاپیتان شده به نظرم اینه که خیلی خوب با خارجی ها ارتباط میگیره و شرایطو براشون راحت تر میگیره و این خیلی برای…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140425" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140424">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⭕️
⭕️
#فوری | ترامپ:
🔻
مقامات آمریکایی به مدت سه ساعت با یک هیئت ایرانی دیدار کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140424" target="_blank">📅 22:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140423">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
❌
تیوی بیفوما: در خونه بودم که به من گفتن که تیمی بزرگ از آسیا تورو میخواد که تو لیگ نخبگانه و با النصر میخواد بازی کنه و به عشق کریستیانو رونالدو به ایران اومدم تا مقابلش بازی کنم اما یهویی دیدم استقلالی که من رفتم توش استقلال خوزستانه نه تهران
😂
😂
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140423" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140422">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
ترامپ: فکر می‌کنم درست بعد از انتخابات میان‌دوره‌ای با ایران به توافق خواهیم رسید
🔄
🔄
آنها منتظرند ببینند من در انتخابات میان‌دوره‌ای چگونه عمل می‌کنم. چیزی که آنها متوجه نمی‌شوند این است که من نامزد انتخابات نیستم. من قبلاً این کار را انجام داده‌ام و با…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140422" target="_blank">📅 21:57 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
