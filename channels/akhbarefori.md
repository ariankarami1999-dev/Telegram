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
<img src="https://cdn4.telesco.pe/file/WOpU48kJUupeyagb48xAeWQUlPMAhfJoWdL2Ax123CicIAlY9Jk70_rtsiusbwOxum5AdnXA3lpy09V40k9F1SP2qTdHwJtCLhW2nsjuDRttj2C3gj7IFGYvllsWVc5Xr0ptpN-EkiEip1OLSn-fsHlqYDNjj3AGFQ_VdKejzdZTBIUoZxzAxV9AvVv2ept5xYHreR7zGC2Ob9DoADmMdO0Dt0DhDFDC6E4vLJAlGDISBqFbMRmJQrLuqjNqiuC-2MM54EVR8Vmzn75npO18DY3_XrGJey8SWVgmlROuXh8ojLwIzQHPN6KybhecD9Jt7M_1x22ZLrvElEGpOrHdOg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.33M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 03:59:58</div>
<hr>

<div class="tg-post" id="msg-695979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuVNhzCDIjtrBfBJZ2FBxyYIKJXy7L1QpePX5ZJYkSINOEA69tXFlvr-gnuD1AQqVwmuhkNvOGufkErZCgRWppeAZ9WO10J9iJ2mCftlvpY3UifsLijBi43oDVNXDPWrKwtgZV7kuSfH3B_lcJaCKRlcsvd3TtNEPcFNWh0jBUXGWLbndFKeIcjtENAa3OJ36MLPUC0rxKiyt936nVOgTvTFBeYEFNGre7EoImO6ujhjZNGGlMQYW-9f7ZqqsWH1rcgJfN8CMrovuWQjsIy3p7c0noYSX9xvzRKsW-krRJncSIDmScK-WrN3mmvP6FAa5HZv6pUY0NU9X_uB8aXiMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تک رقمی‌های کنکور ۱۴۰۵
موسسه عارف
🫡
💡
فقط درصدت مهم نیست
💡
جایگاهت مهمه !
🎯
هم مسیر رتبه‌های برتر
🎯
از همین امروز شروع کن
💪
موسسه کنکور عارف
🫡
| موسسه رتبه ساز | کل کشور
کنکوری داری؟
پس این لینک رو براش بفرست:
📱
https://t.me/+xVKhaZN3zi41OWZk</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/695979" target="_blank">📅 00:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGK79e_BaDxYuYhzpDnD4WiydSxq9iJafQDtB9mKhbcUWi7vD3_iSCRyY7LBc5AtjMAvJe4tdzJrvxWzm5kY1v3a1R0Ko-tHSm_MVKqSFx36t386Hb5iYI3rXUtPniCdqK6m7vGxeSIT0HIugfWgtX5ghd8h8WECpo6Sg90WU7ErtiQgnyAN1CGyF_TF1VLY82_aSDuRxbfG6dc2sfVbd-oqemRXo8e5dIejtzwEYGRIQ5d4gbmXvJarXUELlelIifKCsX-ckZcXqZfdnMlD3aAfO0lhB4uBDA0flMlWAZua8KzD0NyreaR_QDRjR5UNByXZfKEkUMkr6wI7YJ4mCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«الان بخر، بعداً پرداخت کن!»
📱
🔋
دنبال یه گوشی دوم مطمئن، خوش‌دست و جون‌سخت هستی
🔹
گوشی نوکیا ۱۰۶ (مدل ۲۰۲۳) – Nokia 106
▫️
طراحی جمع‌وجور، سبک و مقاوم در برابر ضربه
▫️
باتری بادوام با نگهداری شارژ طولانی‌مدت
▫️
آنتن‌دهی قوی حتی در نقاط کم‌پوشش
💳
شرایط خرید ویژه و آسان:
•
قیمت نقدی:
۲,۹۸۰,۰۰۰ تومان (
پرداخت درب منزل
)
•
خرید اقساطی:
۴ قسط ۸۰۰ هزار تومانی
📥
برای ثبت سفارش و کسب اطلاعات بیشتر کلیک کنید.
https://memarket24.ir/product/fast/63669/180124/
خرید قسطی
👇
https://memarket24.ir/product/brief/63669/180124/</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/695978" target="_blank">📅 00:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695977">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aB308u1x1zskteLC7Jsk0dfAARl99G88mu0I1fFge2oLLO8zjqf6K-tboqrixqSOBu5GhizQ8wdtBWOdV-nVLVSD1pHH9mDv0E0a2dUMtvGxO_hHz7V05mWYesOAOrk2RiVbuSiBkL5KGT2QCKLlCYu6kIPDQSq6XvEp87acKfg5mPlTb0uzxIUbZQJKlnDfQb4DYTg3fcNLGhqVopjlxY8K5SnXbdohUBzCx1ZBfM_fgPPsNs4tn-ZBhphk8VbCOZ8bQImC6MXS-3MVz7OQNBhCm7gl4ADi96JMi_RS18r_3Co9XnWo0aiaLOnEKE65YqhQAortS_mChIJuQ3qFQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅️
سلام رفقا، برای شناخت میزان آشنایی جامعه ایرانی از سوپرمارکت‌ها نیاز به تعدادی پاسخنامه داریم
پر کردن این پرسشنامه کمتر از ۲ دقیقه از وقت شما رو میگیره و هیچ اطلاعات شخصی از شما گرفته نمی‌شه؛ در پایان هم به قید قرعه به تعدادی از نفرات
جوایزی اهدا میشه
🙏
لینک پرسشنامه
لینک پرسشنامه
ممنون از کمک بزرگی که به ما می‌کنید
🌸</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/695977" target="_blank">📅 00:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695976">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650f6da1ad.mp4?token=lLSDUkpr_AgobrkEQWUJZ3MZva8VSt2OlcwndIWItZJBtl0CyyU3jvOVW699vQZAZezNiq9loUIgLjKXUlRYIvELGckVema34JMEZjIQZtk8vgMu0BDqjF5thYwX9DV0nsh1ZdWTRsDa6YErTNbBre2HUYpACSvEyVJRiJfBJD6fIdQqMwYOQuUKRj3Ew7Qx7P2soo1QV68AaMbwKHTMEvoWd1uhuWri3bpbYHkWWrZaWs6uRap-BvRZAMxgAZeJyikTlZb4-pcNK7zvoxPUh2jlLQZEnyKko8uNJXU2WfO7TnWY8HFv4w_5ImYuLQcvdXtF0ON_WcBhIxz5uIZ6Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650f6da1ad.mp4?token=lLSDUkpr_AgobrkEQWUJZ3MZva8VSt2OlcwndIWItZJBtl0CyyU3jvOVW699vQZAZezNiq9loUIgLjKXUlRYIvELGckVema34JMEZjIQZtk8vgMu0BDqjF5thYwX9DV0nsh1ZdWTRsDa6YErTNbBre2HUYpACSvEyVJRiJfBJD6fIdQqMwYOQuUKRj3Ew7Qx7P2soo1QV68AaMbwKHTMEvoWd1uhuWri3bpbYHkWWrZaWs6uRap-BvRZAMxgAZeJyikTlZb4-pcNK7zvoxPUh2jlLQZEnyKko8uNJXU2WfO7TnWY8HFv4w_5ImYuLQcvdXtF0ON_WcBhIxz5uIZ6Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال شده از روتین غذایی یک خروس در فضای مجازی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/695976" target="_blank">📅 00:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695975">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada5338a9d.mp4?token=hw6wHFRY5o6SWO4067rXf9H445pILWhWvM3B3BicTVoKbogyz--ag0TX59obXDS0_KWz3ZBNAKIldNturfHfL6N9kBr8WXAS6HJOeYFil4ipzy2xkqLeAzsHxnKwk7R3_p7KeVRVuQuWZP3FW5lMloFS0dovuz-INMBY8pC_rDFN--WfNrb666KBfHFz96UE1qja0Na11BtNBd4YJbUkAdD7HgYW_JMgKJsaD-Ru5mPQtN9f9B0UwDQDPKQJvOwcTJUvKEcgv94MKYJqfipkLGLh0eaZH_Ux_Yy5t09vlRXE3YRt-vJHnAXEY29jCP_f4vC1eqfZc4sQjuRX9b8w2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada5338a9d.mp4?token=hw6wHFRY5o6SWO4067rXf9H445pILWhWvM3B3BicTVoKbogyz--ag0TX59obXDS0_KWz3ZBNAKIldNturfHfL6N9kBr8WXAS6HJOeYFil4ipzy2xkqLeAzsHxnKwk7R3_p7KeVRVuQuWZP3FW5lMloFS0dovuz-INMBY8pC_rDFN--WfNrb666KBfHFz96UE1qja0Na11BtNBd4YJbUkAdD7HgYW_JMgKJsaD-Ru5mPQtN9f9B0UwDQDPKQJvOwcTJUvKEcgv94MKYJqfipkLGLh0eaZH_Ux_Yy5t09vlRXE3YRt-vJHnAXEY29jCP_f4vC1eqfZc4sQjuRX9b8w2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنگین‌کمانی که از دل گدازه‌های آتشفشانی بیرون آمده است
🔹
ابسیدین یا شیشه آتشفشانی زمانی شکل می‌گیرد که گدازه با سرعت زیادی سرد شود. در بعضی نمونه‌ها، آرایش لایه‌ها و بلورهای بسیار ریز درون سنگ باعث ایجاد درخشش‌ها و رنگ‌های رنگین‌کمانی می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/695975" target="_blank">📅 00:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695974">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
خبرنگار العربیه: وزارت خارجه آمریکا فروش بیش از ۲ میلیارد دلار تسلیحات به خاورمیانه را تأیید کرد
🔹
امارات متحده عربی: ۱۰ هزار بخش هدایت‌کننده سامانه مهمات دقیق‌الاصابت پیشرفته APKWS-II به ارزش ۱.۰۴ میلیارد دلار
🔹
کویت: خدمات تعمیر و بازگرداندن موشک‌های سامانه پاتریوت به ارزش ۴۰۰ میلیون دلار
🔹
مصر: سامانه‌های موشکی جاولین به ارزش ۸۳۲ میلیون دلار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/695974" target="_blank">📅 00:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695973">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
یک منبع آگاه آمریکایی: پهپادها احتمالاً از قبل در داخل خاک بریتانیا مستقر بوده‌اند
🔹
ایالات متحده نگران بود که ایران بتواند با الگوبرداری از عملیات اسپایدر وب اوکراین (عملیات تار عنکبوت)، حمله‌ای پهپادی به پایگاه نیروی هوایی سلطنتی فیرفورد انجام دهد.
🔹
بنا…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/695973" target="_blank">📅 00:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695970">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: ادعای درخواست پناهندگی عراقچی دروغ است
🔹
روبیو به عراقچی نگفت آمریکا را ترک کن. ما در زمینه وظایف نمایندگی، آزاد هستیم
🔹
برای نمایندگان تهران هیچ مشکلی وجود ندارد و پرونده ای نیز تشکیل نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/695970" target="_blank">📅 00:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695969">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQgRjdLSJm-450UoIQk3qA13hdQb8YagXyMk0mZCfD4xSnVSqlWuKzqeKwP0C-9Yl-eMqDNdv90GA1oZnr3FamxPSA9Nld80JA20ZdXG69Ssp_b6qk68SiecJuuqx8OO9c7mh9qYP1sX-knEP4O5JkJqj1DXHLl0wCSvwI68OYtqy8XeglMllPeWGQfhxYoh7t--4Ma5IqJfVOSBsjk01vCG-1TH2hIC-iOYrW-kY0N-1QYngOBqIF0nkF4BgfAzEZWPAl_nmEZQB0GN4tc3Ye5SzcGPPnqwcrP6HJimtOETryGEYamdd2CjcUxMT6h4whErdsvtwx9scT8Lv6Io4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باید دوباره دنیا را وارد قرنطینه کنیم تا تقاضا برای نفت را نابود کنیم
🔹
اقتصاددان و استراتژیست حوزه اقتصاد کلان و ژئوپلیتیک: این تنها گزینه‌ای است که برای پایین آوردن قیمت نفت باقی مانده
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/695969" target="_blank">📅 00:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695968">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdsEhAqgcQJbkUlMIzB_lRq41B6g2-L5TJy-jp97e_DURfi1ySQaX2xF-pD30E9PeChNccrMSaNKp68gwOlPhTkpbd8BU-45jizT5CiNgunMM2cUpWIrQN5IDVYU3OO6pHdxjNGZi5SKK1iNXOoIdo95cgTii2Cyv7Zhu20HjXg4Ygg69XAOs67oTNOlnAoMGVNQeomP5zs08meLCDb3MkSs3zrcxuCQ8AJSjrQ61h6Vs_hWLf-6Y0Fh9k_SdBkqSmE_IJQMu5dz2d8qcZ7HUtN31Hzb7GwLY8t9kFGB_qxBNGRRrskkhmQzvV3qyWXPLj4NHQJP3NM-ogVjwI-T2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/695968" target="_blank">📅 00:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695967">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
یک منبع آگاه آمریکایی: پهپادها احتمالاً از قبل در داخل خاک بریتانیا مستقر بوده‌اند
🔹
ایالات متحده نگران بود که ایران بتواند با الگوبرداری از عملیات اسپایدر وب اوکراین (عملیات تار عنکبوت)، حمله‌ای پهپادی به پایگاه نیروی هوایی سلطنتی فیرفورد انجام دهد.
🔹
بنا به گزارش‌ها، این نگرانی باعث خروج ناگهانی بمب‌افکن‌های B-1 شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/695967" target="_blank">📅 23:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695966">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7faea8050b.mp4?token=pcPx7vua104QLhmUFkQzczt5PoScO16oXmuh4ZM9CkX8384WmGn5lHbNURY0d2gz1h93DQROCYCF19OX4_7kFt8qURLqy92pPHcJ4DkYDYWO5F2Uo2OmOkG456zDdBprJY3i-JTX3E2bhh-yLNWww2zhJSP2WdOnrT0zgupynhot3Rk2kPCen5nV8CuNYtNMSR1Qb0RCZWWm80ML5rnst95ZyxBj6WJKTxCElwjMtJzhqY568SIwmLrtGbxHHy0yRs4JEIsn4NC97FkED3-0zmvlrBMwfOy0cjtlCsYwm0R5NV0gaf5Njb2rcjciGvVZ-67ieHzAzYg7lcm_emwVD3jmDsxhBE0V4uBAoSx1VSy72-SDEByKgsX5XrAPfzAhx9elslyQma8zmPCWIqIFQzwlNWe2AEAunsipLQFuVm_opyTs6JVxwzTGVEgrjN9C6GxxMiglHXPjmeryc3U3urWqhMDQQECQDSRG4QwDaiSRPCJiaesOYSdqO4p2czFi1A6_h0udhFJhZsuw03ngkvHXgqyJYBIvy_pJFZu48zumgYBLZMNPHcYWxCOzMGG_sXxxRUBfKpXq3bu7FZCxKgb8W-rKR6C7yFgsV53jCDvC81mpu31QSFlLXZW9MwOxoam1-FLh0qicrnJb7dxkJRVc_sue3qC-MwhrYhHgI1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7faea8050b.mp4?token=pcPx7vua104QLhmUFkQzczt5PoScO16oXmuh4ZM9CkX8384WmGn5lHbNURY0d2gz1h93DQROCYCF19OX4_7kFt8qURLqy92pPHcJ4DkYDYWO5F2Uo2OmOkG456zDdBprJY3i-JTX3E2bhh-yLNWww2zhJSP2WdOnrT0zgupynhot3Rk2kPCen5nV8CuNYtNMSR1Qb0RCZWWm80ML5rnst95ZyxBj6WJKTxCElwjMtJzhqY568SIwmLrtGbxHHy0yRs4JEIsn4NC97FkED3-0zmvlrBMwfOy0cjtlCsYwm0R5NV0gaf5Njb2rcjciGvVZ-67ieHzAzYg7lcm_emwVD3jmDsxhBE0V4uBAoSx1VSy72-SDEByKgsX5XrAPfzAhx9elslyQma8zmPCWIqIFQzwlNWe2AEAunsipLQFuVm_opyTs6JVxwzTGVEgrjN9C6GxxMiglHXPjmeryc3U3urWqhMDQQECQDSRG4QwDaiSRPCJiaesOYSdqO4p2czFi1A6_h0udhFJhZsuw03ngkvHXgqyJYBIvy_pJFZu48zumgYBLZMNPHcYWxCOzMGG_sXxxRUBfKpXq3bu7FZCxKgb8W-rKR6C7yFgsV53jCDvC81mpu31QSFlLXZW9MwOxoam1-FLh0qicrnJb7dxkJRVc_sue3qC-MwhrYhHgI1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: دولت ایالات متحده در مورد خطر شیوع طاعون از روسیه چه اقدامی انجام خواهد داد؟
ترامپ:
🔹
ما این موضوع را به دقت بررسی می‌کنیم. میکروب‌ها و عوامل بیماری‌زا قوی‌تر شده‌اند. ما به آن‌ها کمک خواهیم کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/695966" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695965">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
اگر فرصت دنبال کردن همه خبرهای امروز را نداشته‌اید، پربازدیدترین‌ها اینجا در دسترس شماست
🔹
🔹
نشانه مهم از تغییر آرایش نظامی آمریکا | از ۲۳۲ تانکر سوخت‌رسان تا ۱۶۵ فروند جنگنده | چرا احتمال جنگ کاهش یافت؟
👇
khabarfoori.com/fa/tiny/news-3250072
🔹
ترمز قیمت‌ها کشیده نشد؛ بازار طلا با فشار دلار صعودی شد
👇
khabarfoori.com/fa/tiny/news-3250124
🔹
حملات سنگین به یمن | پای آمریکا و پاکستان به جنگ باز شد | یمن تهدیدش را عملی می‌کند؟ | نشست محرمانه تیم امنیتی ترامپ درباره ایران و یمن
👇
khabarfoori.com/fa/tiny/news-3250188
🔹
آزار جنسی بازیکن مشهور فوتبال توسط مجری بی‌بی‌سی! |+ عکس
👇
khabarfoori.com/fa/tiny/news-3249918
🔹
طاعون از آزمایشگاه روسیه خارج شد؟ | آمریکا به حالت آماده‌باش درآمد | واقعا چه اتفاقی افتاده است؟
👇
khabarfoori.com/fa/tiny/news-3250121
🔹
خبرهای جنجالی را در وبسایت خبرفوری کلیک‌کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/695965" target="_blank">📅 23:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695964">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
نیروهای مسلح یمن: سه عملیات منحصر به فرد علیه دشمن را با تعداد زیادی موشک بالستیک، بالدار و پهپاد انجام دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/695964" target="_blank">📅 23:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695963">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
آزادی بیان به سبک آمریکا؛ دولت ترامپ حضور خبرنگار خبرگزاری پولتیکو در هواپیمای ریاست‌جمهوری را ممنوع کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/695963" target="_blank">📅 23:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695962">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b31a9d3c.mp4?token=UpGrVXmXC0sA8KZEbzvV4sb22AsFWwwc1NuOssTjLgQsm5XDFZduDH0Oz6_JHL2w8jeudmvbmMoPF2yNdmSA3L4Q2O39oqgnQqa-uZbmbt1gTz-yz0gy4LsSAqonu73LVGXWLuKiofdAzB0CDurwuMZdTA0V_4YEAGsCOJ0ZvY-n8TyBh4KnfLbnhqEdq_dtbGAeOVP9S-lfPtfYAYemvyKjuMiWZElu5ESG6HpX_yMobvKWUGmZqjNcdOdm3deRCEI9QeumDOsC-2NWCJaPb7AIitzMR0FWwrKm-y9iHH-5WzCrv0KrMLGRnHBPHoypd_0SREU1-M82AIujmml_xUcIX_0mU85-x589RzLvLylWMZ5h0IiS_vtGIr78q5P9ZxtsV-Impozt6NZcOsWckrFOogGlSbwlK233OFhJJfjPZusl5lP3ICBSrHjjS7qsHY5-V2FgIDV0CPzica68EhmG1HgmxYOHc6kt5vuFM-v0nQaqwWRtJ2hh8OH-Lte8AwISoZnn3oDO7Kbd3QaVGvKzF01Iqb5DQQFqrCUfiFt3340Ca-y13BWh4Nlpuwx4fZDnHgkijy_BOAaOX4yYoML90IwWaasCoKLLTBISbwQwdeXKviQzRpiLnn-hYnIQ-Rs38bi_uRtkNIIfvtixa-TRrmzWESj46T_xOP5mjNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b31a9d3c.mp4?token=UpGrVXmXC0sA8KZEbzvV4sb22AsFWwwc1NuOssTjLgQsm5XDFZduDH0Oz6_JHL2w8jeudmvbmMoPF2yNdmSA3L4Q2O39oqgnQqa-uZbmbt1gTz-yz0gy4LsSAqonu73LVGXWLuKiofdAzB0CDurwuMZdTA0V_4YEAGsCOJ0ZvY-n8TyBh4KnfLbnhqEdq_dtbGAeOVP9S-lfPtfYAYemvyKjuMiWZElu5ESG6HpX_yMobvKWUGmZqjNcdOdm3deRCEI9QeumDOsC-2NWCJaPb7AIitzMR0FWwrKm-y9iHH-5WzCrv0KrMLGRnHBPHoypd_0SREU1-M82AIujmml_xUcIX_0mU85-x589RzLvLylWMZ5h0IiS_vtGIr78q5P9ZxtsV-Impozt6NZcOsWckrFOogGlSbwlK233OFhJJfjPZusl5lP3ICBSrHjjS7qsHY5-V2FgIDV0CPzica68EhmG1HgmxYOHc6kt5vuFM-v0nQaqwWRtJ2hh8OH-Lte8AwISoZnn3oDO7Kbd3QaVGvKzF01Iqb5DQQFqrCUfiFt3340Ca-y13BWh4Nlpuwx4fZDnHgkijy_BOAaOX4yYoML90IwWaasCoKLLTBISbwQwdeXKviQzRpiLnn-hYnIQ-Rs38bi_uRtkNIIfvtixa-TRrmzWESj46T_xOP5mjNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سبزی خوردن فقط دورچین نیست؛ یک بخش مهم از سفره سالم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/695962" target="_blank">📅 23:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695961">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
نیروهای مسلح یمن: سه عملیات منحصر به فرد علیه دشمن را با تعداد زیادی موشک بالستیک، بالدار و پهپاد انجام دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/695961" target="_blank">📅 23:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695960">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
منابع خبری از توقف موقت کلیه پروازها در فرودگاه «شانلی‌اورفا» در جنوب ترکیه پس از هشدار وقوع بمب‌گذاری در یک فروند هواپیما خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/695960" target="_blank">📅 23:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695959">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4V9A3dTDM-dZAH31koANb4cGvsr_edtZC5QlgmNugmKomESR98s68gvpRhTzAb5nCPr8UGfP-ftyvv_BcRTLY0OwsQSUhA0PAIMfm_0iB4oFIUf9tlSoNMXGItSOMJnb06oywTarfyjpkPSuTRggHHabxNCQa_TVlHxsPktSQ2iOjdKG_vQPQBzBz7Egqpj1OztOLWgSbHRobwmE9mN_PPNWhjNPhAa26Y0Wb7dScYTTV2UurxiBoTt7MSPgmi41Ogiv4QFWGLhcEH7q-EHo1QX6VTttb6mUJx8sksQSU13-2RXKtuDkrl65puDE3XZEMsOurWJDTGNLv-PXbOkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از صاعقه در گیلانغرب/ امشب
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/695959" target="_blank">📅 23:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695958">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ug2usIj7XR70PLMZR3C-6j6w64bdleUm55pvgkVS6mCObkkiG2j7ciBv8-QZE_-5rPa9_3y3a6k7sqHnJMWCWB3iYHBzUHFkBCW0SF0ziq6SJ0iMGJa3qFtSczE7-p-tMWhdr4W98uKyrulBxe9yOOwCN_4luzECGY0oHp17bdOwUBP8QHJT8eWs4S1AHzRNgOKDZ1wXVP024HYUEY90LUCg62lfEj0ZpoLVsdCrKbp7N4kNb5yaJzyxMSJu2y3nJs1JmMQlTqadn3N4mOEe75n460KptzBKbL-WS8zy2qK37818l3NkKnGJjgLqIss-rCTF0iPE2C1Pzo2C6-JkJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرور وحشتناک‌ترین اپیدمی تاریخ با ۷۰ میلیون مرگ / یک خبر نگران‌گننده: طاعون مجددا عالم‌گیر شده؟
🔹
مورخان تخمین می‌زنند که جمعیت اروپا پیش از طاعون حدود ۷۵ میلیون نفر بود. تا پایان سال ۱۳۵۱ میلادی این جمعیت به ۵۰ میلیون سقوط کرد. در برخی مناطق، مرگ و میر به دوسوم جمعیت رسید.
گزارش تاریخی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3250225</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/695958" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695957">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
شلنگ باغچه‌ سوراخ شده؟
قبل از خرید شلنگ جدید، این ترفند ساده برای تعمیرش رو ببین!
🔧
🌱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/695957" target="_blank">📅 23:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695956">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون انرژی: استعفای وزیر نفت به دلیل مسائل پتروشیمی خلیج فارس و تراستی‌ها نبود
فرهاد شهرکی، عضو کمیسیون انرژی مجلس در
#گفتگو
با خبرفوری:
🔹
استعفای وزیر نفت به اصرار خودشان و به دلیل مشکلات شخصی که داشتند، بود که بعد از دو الی سه ماه پذیرفته شد.
🔹
مسئله تراستی‌ها و پتروشیمی خلیج فارس در مجلس و کمیسیون انرژی مطرح نشده است.
🔹
هر مسئولی اگر در زمان مسئولیتش اتفاقی بیفتد، حتی اگر استعفا هم بدهد، فردا روزی باید پاسخگو باشد و اگر تخلفی باشد، به تخلفش رسیدگی می‌شود، اما این مسائل برای وزیر نفت مطرح نبوده و استعفا به اصرار خودشان بود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/695956" target="_blank">📅 23:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695955">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOAcbWmNwbCo-WPbv-qcQCZ-zqzygKZz0vPP28_qYKCJ1qxgmz3hy9yPLtzyfpisEkMlMHRXqx6bDtW-cjWk5dgh9156ZM-7xsY2gelktFvNWJVOO9GTRpcE6aYR4hQlv2mmDO3lvg2Cje1E7aJCC6lHGfJDC2OD-I1xReaN7_FgNV9wjXvAue_Nv7nyaXhs3TFzMGb0xfwXo3x5mrgmjA6DCJrr9yx9FNgJKGMTbRQPUI87seTa3Y8jzv18TQCymd39bWAx7q91XwAwfFAofYTlagdc2cYJzpK1aYKGvXIYQ2ShJa6Jku52tjgzeaizaJQAOvWJ0wXBoG4eKC-ykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش مصنوعی ایلان ماسک هم در پاسخ به یک اکانت توییتری اسرائیلی، از کار افتادن استارلینک توسط ایران را تایید کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/695955" target="_blank">📅 23:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695954">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای ترامپ: من معتقدم ایران مسئول حادثه هواپیمای فلای‌دبی است
🔹
ترامپ: عقب‌نشینی بمب‌افکن‌های آمریکایی از بریتانیا، در پی یک تهدید صورت گرفت و ما می‌دانیم چه کسی پشت این تهدید قرار دارد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/695954" target="_blank">📅 23:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695953">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtyWRzmS32DQ8a96lRhUy8F1OfeJbyHELAY02ZGs-AFwYTXFp9LcZLpdFEjzy3dKEUMD9JMKsk751k2ydVem2k8e--NKJQhQeEyzB_lY_VnUorDVNU0Cw2AUbM_2IJXLyQQTuqiATGfFeItZUMvTSgUQHjdtSgf8etZ0fis6cI2k14YYVxKNKXTBgRhAlr4rnqMIt6efyxy0h5r0sJyWMvrVal_4g34_eeAlCoQcYnNw5xR7TakYMgc8iVwTzBMKkDepKL5lB6ikgK8ofpOmrqyN3mS32aFlvrqaq3vuq2XMFOuQSgds6c4m2SMm0neImaG9x9i-eqJ6WaRQQ6OGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسوشیتدپرس تصویر دیگری از حمله پهپادی ایران به پایگاه محل استقرار نیروهای ارتش تروریستی آمریکا در کویت را منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/695953" target="_blank">📅 23:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695952">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای واهی ترامپ جنایتکار: همیشه آماده گفت‌وگوهای مستقیم هستم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/695952" target="_blank">📅 23:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695951">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/668e7e80f8.mp4?token=nRL_HxUbTDohrT5N83ETkAL0dd-VOKJSEDvOU3zqlP3pjSVIllG1PVGwknJoPrnon1Yi4lkWJBJw7oQ35cpiTRX3LSXmrOY9PHU1xZnJ8YuB5rcAMbNWRoPxjzwp557IdNN6bAqK4pRPU0bbcztJ26TVVq-JVH-6qtXR3yKRbhAuSLOmUmwAkz9D1wpWcHTFwD7Cp9fv_jHDJ8L5Xs0jcfOq6tGgsdLcwuS4JFnRR7vLjKLOUVWrm7q0C8akTjJt-C65x6F1-TmlqjQgBRVh9mfHeoNHFkDCT2eN7Fswac1OUESigEtj05Aya3AHp3QhNWJoxM_t-hIQojGpa7jrq41wWrhG_95cqg4t-FiHb2HNVxIe5SBTPonzz_ZOhh4ixqmyyi1B_T6NGd6IfFApKYN9_1m_5s5jd9BY3cBsjysedEhFq8SI1SJ7DqlHjYH6S9Rv9qqD9NoJhFh9SwOHxRdBwp4ZG6OeH2ueraWNytcrmD5NDLfhBpw8ScIdWJGWHPrw6E03ppqJxFqMbIzGe2iGwM_aTUFRi3vmDMbPyGs8-Jw6iiGkdB7OD_NrdJSJcRfVubLDnC8Xmm5g4q56seRj04VmTPqZKnU687AmV_LoINvKEuyDyt9NUAjkjhD4yEdj3wfZXd3jvWUbMUBHSGySPLhZUFhAv-xkRnDNtso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/668e7e80f8.mp4?token=nRL_HxUbTDohrT5N83ETkAL0dd-VOKJSEDvOU3zqlP3pjSVIllG1PVGwknJoPrnon1Yi4lkWJBJw7oQ35cpiTRX3LSXmrOY9PHU1xZnJ8YuB5rcAMbNWRoPxjzwp557IdNN6bAqK4pRPU0bbcztJ26TVVq-JVH-6qtXR3yKRbhAuSLOmUmwAkz9D1wpWcHTFwD7Cp9fv_jHDJ8L5Xs0jcfOq6tGgsdLcwuS4JFnRR7vLjKLOUVWrm7q0C8akTjJt-C65x6F1-TmlqjQgBRVh9mfHeoNHFkDCT2eN7Fswac1OUESigEtj05Aya3AHp3QhNWJoxM_t-hIQojGpa7jrq41wWrhG_95cqg4t-FiHb2HNVxIe5SBTPonzz_ZOhh4ixqmyyi1B_T6NGd6IfFApKYN9_1m_5s5jd9BY3cBsjysedEhFq8SI1SJ7DqlHjYH6S9Rv9qqD9NoJhFh9SwOHxRdBwp4ZG6OeH2ueraWNytcrmD5NDLfhBpw8ScIdWJGWHPrw6E03ppqJxFqMbIzGe2iGwM_aTUFRi3vmDMbPyGs8-Jw6iiGkdB7OD_NrdJSJcRfVubLDnC8Xmm5g4q56seRj04VmTPqZKnU687AmV_LoINvKEuyDyt9NUAjkjhD4yEdj3wfZXd3jvWUbMUBHSGySPLhZUFhAv-xkRnDNtso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی یکی از گوش‌های ایرپاد صدا نمی‌ده، چطور درستش کنیم؟
🔹
راهکار ساده‌اش رو در این ویدئو ببینید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/695951" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695950">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 7- میدان هفتم، صبر</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/695950" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صدمیدان خواجه عبدالله انصاری
🔹
میدان هفتم، صبر
🔹
آن زمان که قصد الهی خود را مشخص شده یافتید و به درک آن رسیدید، می‌بایست در مسیر تعالی استوار و مقاوم باقی بمانید
🔹
صبر توانایی تبدیل آزار به لذت به کمک نور و حکمت‌ الهی می‌باشد
🔹
هرگاه در هنگام دشواری صبر را پیشه کرديد تغییرات مثبت بسیاری در زندگی خود مشاهده خواهید کرد
صبر سه قسم می‌باشد:
🔹
صبر بر بلا (به دوست‌داری توان): یکتایی دل_علم باریک_نور فراست
🔹
صبر بر معصيت (به ترس توان): الهام دلها_قبول دعا_نور عصمت
🔹
صبر بر طاعت (به امید توان): بازداشت بلاها_روزی نابیوسیده_گراییدن با نیکان
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/695950" target="_blank">📅 23:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695949">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
اظهارات مضحک و تکراری ترامپ: مقدار زیادی نفت از تنگه هرمز عبور می کند!/ شرایط در تنگه هرمز نرمال است! #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/695949" target="_blank">📅 22:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695948">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
اظهارات مضحک و تکراری ترامپ: مقدار زیادی نفت از تنگه هرمز عبور می کند!/ شرایط در تنگه هرمز نرمال است!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/695948" target="_blank">📅 22:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695947">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a7fba16c.mp4?token=SIurKgnIxQScsx5mp2mh9WIvPpA6UNnfP0gyR4pS_jzyJbfZ81cCBzpI04wxjGoIMzzkRooNI0BiEJyV81gj58gOqyvRW0M_NyO05V1QvN57wwHQKFNjjiteBz5CWoamMBBl57HGml50xngUSSa_gz120O6XeLOwLl9xOFgqu2pvjiawk6QUlR8nI65NeN9DAEXEjo7PwybyBaAG0Lqx1QclsdnARBzWnUNHen1JZ-jwypBwnM7OVyLCRKF3UGmJUbPNsXTOOp83jXcXj0a5X2p5xv1rC5SUiPdnT0_hNkHjoMIKtltrSAuGiCRK5Xw0zsoxuhduunEAJPTxxA58LHXaPId_GzkS641rD3Qqc0DnxrLZ4DrO7Hf2qzUCwcnrQ5w4FjeIJzZOhRZe44FDMc7tDBa5Nz9lNieeOQRFi0RtKg-H_CzRWE3mMy8YjRbumRT-XD86bJo36bXe3HgaWxkaGE9C17Pq061cv5EDph1_3idJOYRV2fNnZ-AYHNcQIm3dEwSuKhHmkm3SCketbEqn0nTbKDd5V0sIwjwgYiVqOIoo3gJIQcEXcGnu5hLZZtAuFmIT5vY18A2vYY4GuJm-uOdDh8H-bva1DqobUEKYEtS3xhdi2KhkydtYFm3lcGPOpK-EkcToqD_QqSRxiWAid6mGnXeM6hHCqesujgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a7fba16c.mp4?token=SIurKgnIxQScsx5mp2mh9WIvPpA6UNnfP0gyR4pS_jzyJbfZ81cCBzpI04wxjGoIMzzkRooNI0BiEJyV81gj58gOqyvRW0M_NyO05V1QvN57wwHQKFNjjiteBz5CWoamMBBl57HGml50xngUSSa_gz120O6XeLOwLl9xOFgqu2pvjiawk6QUlR8nI65NeN9DAEXEjo7PwybyBaAG0Lqx1QclsdnARBzWnUNHen1JZ-jwypBwnM7OVyLCRKF3UGmJUbPNsXTOOp83jXcXj0a5X2p5xv1rC5SUiPdnT0_hNkHjoMIKtltrSAuGiCRK5Xw0zsoxuhduunEAJPTxxA58LHXaPId_GzkS641rD3Qqc0DnxrLZ4DrO7Hf2qzUCwcnrQ5w4FjeIJzZOhRZe44FDMc7tDBa5Nz9lNieeOQRFi0RtKg-H_CzRWE3mMy8YjRbumRT-XD86bJo36bXe3HgaWxkaGE9C17Pq061cv5EDph1_3idJOYRV2fNnZ-AYHNcQIm3dEwSuKhHmkm3SCketbEqn0nTbKDd5V0sIwjwgYiVqOIoo3gJIQcEXcGnu5hLZZtAuFmIT5vY18A2vYY4GuJm-uOdDh8H-bva1DqobUEKYEtS3xhdi2KhkydtYFm3lcGPOpK-EkcToqD_QqSRxiWAid6mGnXeM6hHCqesujgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی پول‌های کوچک مردم کنار هم قرار می‌گیرن، می‌تونن کارهای بزرگی رو رقم بزنن
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/695947" target="_blank">📅 22:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695946">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
عربستان اعلام کرد که ائتلاف مکه توافق کرده تا در واکنش به حملات حوثی‌ها به خاک عربستان اقدامات بازدارنده جمعی را به اجرا درآورد
🔹
این تصمیم پس از برگزاری نشست اضطراری «کمیته راهبردی سیاسی و دفاعی» این ائتلاف در ریاض اتخاذ شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/695946" target="_blank">📅 22:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695940">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe3z60IRrmTZkZvwBvxXwfgp3wX2mkHehlCOW3cHTOvoCkRNgCJ7K9pDuH_lVuLCqCZHN1nGUACJEvU1P8n2DdVGctciJTbrpW0pzjkg2DhKoQWN8Y6jQhcPRZ7_bQapWXPF77jQR4JQ4ExKpk5FOZE0WcSugTN4utF8bY4kTVmrGa60qTXwx_agtcsKKZKD6vDK4cNtSKJWVMG2SxYRfK80qEjXi-L8NLc6_h0Mn-UnlDxAjH1bslWo2UH2ES3SvftJ9-WOSCkMMlY6Z4OuQditPHmCXWe_yiGfC6_RttkmlbCShIRh-rm-D6DhInGdCKgdO0o2Z51yWlkAzF5DNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPJyEIsGausOMmRCNsj62Jc2yAtEk-NFPK4tgs_IadlWw7i5izyZ56ws40Pim1Pv7TVM6cV7p0jIH8FFhDcV7z4JlOfFD_7-MVPo9WFCoXOdfne2EibYHz17EhyE1nsQHUvyIAVOuOASdiNAhD5gyb3zQk-mqN-tmgzuRiaB2T-AySJ657yiL6Vbx3yHVHlESDaGX9UmH4zmV4QbCJ0AWgZzPrgXahwGVuysLDDg8wB3YO5WWArJ40XRyBoXx1prqujEAkKQUUGXPu6pHqCONFTzrca7S5hntZ_2Yk4R2flHhuFKJpIaeC_MQyKsDxpQhtwDhFMaYWjOOuIBqoemdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWrDwQ8Wsfg-b35co3fml7Yubkw8wbKCexsZW7S5XIxluzNh5Zy_x_7ClOI2ZGuN-th-dYXAWmt-RHi-2Wr7m3nRRc7o65C3dg9vlUSn-Rmc5_r1vvMiSxAt8OenIAWpu6uSNf6VJJDeD9NMHMr1DxM8YiKVG2f0yLXerxGjeEHRNhzB-RG1kByK6cAcoWRu322jOXt4er3ioUIPpbho7NG3lPZgdIbMAUP20HVE5G58wUhD_0u1EOJFRonROffRDaCothPPMNHzp07sEZVrBco47efmzeXbR7Y8iLLq-JOE7zXhWSkOfA6rB910NJK3z9hN6qt0YvZPDADovPTgiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWOcKoIkDUTC-1NRwmG23QfzF_Sdh2uZTJb-HXCt1_gkhOrT0yoIoVbNlshQ5IhsgU8FVXNwPS6mNTz4FUzEpiMTrHyZQPxqJrQy6X8L71wr90nEa3KVpEhpxtUYt63WzwkS50uIUg0JAEg151gzlPzvJqDkYTEFaZ4ppGe6bPFGqeuDG8NmWfHcXFaf9WLB-YCP6uLSOxNRCKpB5q447lw1aGC6N1vu5NQHqYhs7gFsJND4Q1UbgFg58t75SfxKwL2Z4caercq9g_WQKyzGvE2p5En4n15tLhKWV83Ufx1zDJBkYW917al22Mkms7E3Xv-tYVrgvZVCi3gntGte6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRihr1H33WTagxG90Z68a8O1Zk4qXK_zVolJlRwwbmBd25ZLHTmQB07MY-j9OB7Lpl5FGS95c031XmvmsW5VH2iz7TrwR52DIwT6Eetuaw0JgCgKBkhOvgFt_Gwc-1Zs_5WJJB-abFw4mo0kkDiR5jBGmx_qosDX6buV8zMYVkmPJG0BwVqrcprhOLVsi7daw4Fcc7Y3K7YY0_qCCBLZZUmorsCpRz22R8p1IaSJBeVkx1uTKgv4YF0jSE3mkkXE6q0gDonYB20D4CsKZjXGsY3NE4zRhHJM9o27iQTPEwFR93UiqJEYXryQXEOOZd_YdHEDHS-D7fY2OyS9rAvOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auka1K_J0FSn8gnDVpBg--03TxNFBBEOvvqUmcJkP8p4_OEw8zarReERnKQgpKkYmzT6bUvpcUMaHBlFehFb7BQvF9-3qywhvylR2_JW3hPlMCs-tg4BMIMD-fIJF4ZkjWad8Yo7ZRk1pG2mn0Zcwi5kL4f_oyLDWefAw4E7KukJmXzmn3nGZ0OnFVFySQlSlVipORTwFBf_povhZGHksfVtrOrrWyo4cJ-i3bHF3QJZBNblZwLSUsGhQAOvjSJu67-YCu3o8qgdEjIbfI6orC9jNdyjl5hcAqmkV2nsJO3cX39siBbCA134vYYMC5VCXRUmAGUL2gPF-iEKYFP6Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چیزهایی که هر روز می‌بینیم، اما اسمشان را نمی‌دانستیم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/695940" target="_blank">📅 22:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695939">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd281cff39.mp4?token=UQiTIWGychDXI1BEuVS7kwmSdnp0hkh90-utfDLufQ9fjjZB4Myca3iuPK5fR677PJjqHwWzwQlPgi9EUXZtKsQ_ACoGq4RVwb490fGapgGMM02L-Lh-AbyTXK8Y-UiLo-75lZ4xKwVqADh9lZuACDhPC6vDKbSgp3w98EQmsWsLlOHZMVieZtFU-Qgkb1mK_-3AemHIaNjOAYI3fOdIK2VcEYgWIF-lkCS57t73G8YcPYodTSQlfuvWeBYbFFCUZeZIRwklgulmzQrBjh1lIMJi8N-3ledte6RD6Q_ryCZoWfqu0OJGP7pY6b8FlIclFpTwMx93inLI28KXDbxVjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd281cff39.mp4?token=UQiTIWGychDXI1BEuVS7kwmSdnp0hkh90-utfDLufQ9fjjZB4Myca3iuPK5fR677PJjqHwWzwQlPgi9EUXZtKsQ_ACoGq4RVwb490fGapgGMM02L-Lh-AbyTXK8Y-UiLo-75lZ4xKwVqADh9lZuACDhPC6vDKbSgp3w98EQmsWsLlOHZMVieZtFU-Qgkb1mK_-3AemHIaNjOAYI3fOdIK2VcEYgWIF-lkCS57t73G8YcPYodTSQlfuvWeBYbFFCUZeZIRwklgulmzQrBjh1lIMJi8N-3ledte6RD6Q_ryCZoWfqu0OJGP7pY6b8FlIclFpTwMx93inLI28KXDbxVjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عاقبت یک نفتکش در تنگه هرمز پس‌ از تخلف
🔹
تصاویر جدیدی از برخورد با یک نفتکش متخلف در تنگه هرمز منتشر شده؛ این نفتکش به‌ دلیل نقض مقررات و هشدارهای دریایی، متوقف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/695939" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695938">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMPKi31KGzITB7wUf1t9lcxfxx13KebRj07M-A18XsBV-yAOQ_V3uH0hqEfLJlYxZ39gkBjnFVyGJRiaC0B4Px5LHsO0u1sawLwbZ-crYCvWH2-d46lNlvseDHXNuPLBY19FR0TDvvETF0Qdq75mtzaE5JjRSvBBucwqtQokKlMCvH6Y9TZSv7oaoTip0vMBmgJHbZwuqZzCygkXymZLa90jUdukLRZZsDtNlXYVIEpMdtLCpeG2yNXoWGUP2g17kUkSSEBktvEPPOZcSkRN6Ki8KmZ3cacCyJqIOboCS9ziiSTjr9lPTUSilO5G_bQEVThF-ygl6EPgI_HnF4jIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ نشانه مهم از تغییر آرایش نظامی آمریکا | از ۲۳۲ تانکر سوخت‌رسان تا ۱۶۵ فروند جنگنده | چرا احتمال جنگ کاهش یافت؟
🔹
در شرایطی که احتمال ازسرگیری حملات آمریکا علیه ایران همچنان یکی از پرسش‌های اصلی در محافل سیاسی و نظامی است، برخی نشانه‌های میدانی از کاهش تدریجی آرایش تهاجمی نیروهای آمریکایی در منطقه حکایت دارد؛ روندی که البته به معنای منتفی شدن حمله در آینده نیست.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3250072</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/695938" target="_blank">📅 22:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695937">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnBN1c-p1VtnpeAJkwESWb3vUDnAPsMg_bXP-UJz75UR-DCktYijbKkLcpTbKjiIDEEKLSFg8KUI0g1b7xczwdsJRhEbShA5a88bSZuZGL7Vic2HYcD0tlNkdXJp5rYHucw9WoutE13ZUe1Goeg1Ht-_Bgy_udvS93tBg1ZuD66QWRoNDnEFm-pVodCyJfA2wDloMI337F0qcjjte6tZ0y3y4NxMUgkIEtR_kQnGsC6kMzn2k7Dj_SD7mBv0n_FlsIeRKdTng_w1DyrB0xcqcpvAAoA7rIQ9c6ac4VYIOp8MaWioqCasIJTyZM-B7QjGlR3imLboYXwbf3q6pQj7XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیستی از ۱۰۰ قرص پرمصرف همراه با کارایی هر کدام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/695937" target="_blank">📅 22:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695936">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تامین مالی از بازار سرمایه، راهکار مدرن بقا و رشد شرکت‌ها</div>
  <div class="tg-doc-extra">گروه فیروزه</div>
</div>
<a href="https://t.me/akhbarefori/695936" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔵
تامین مالی از بازار سرمایه، راهکار مدرن بقا و رشد شرکت‌ها
گاهی اوقات سفارش هست، بازار هست، خط تولید هم آماده است؛ اما اگر پولِ خرید مواد اولیه و هزینه‌های جاری سرِ وقت نرسد، چرخ تولید کند می‌شود. برای بسیاری از شرکت‌های تولیدی، گره اصلی دقیقاً همین‌جاست: تأمین مالی.
در این فایل صوتی با پرستو ابوالقاسمی، مدیرعامل شرکت مشاور سرمایه‌گذاری دانش فیروزه درباره تامین مالی بنگاه‌ها، شرکت‌ها، سازمان‌ها و واحدهای تولیدی از بازار سرمایه گفت‌وگو کردیم.
🔙
مشاوره تخصصی و رایگان سرمایه‌گذاری
🔜
+982179672000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/695936" target="_blank">📅 22:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695935">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
یک کارواش در آمریکا با کارکنانش تم هالووین زدن و اینطوری مشتری‌ها رو میترسونه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/695935" target="_blank">📅 22:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695934">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ادعای
اسرائیل هیوم: اسرائیل در حال تدارک گزینه‌هایی برای حمله‌ای دیگر به ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/695934" target="_blank">📅 22:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695933">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMTHhMtvjhx6JFhmhd_QIEUvOkFz18hnOXT0Tlcn5kHxYIegnAv4w8pmc_usqLOCu8pDLW-vzlE1VS5TNbk6jkwhY-7Gv5V1HHEeJYwMpldEDw6p7ZK73wxvPLFuuUOfMz05Xzbk8WAzqO-c3j6kz7ObuOqyD1B5_Av60KpOM1HKzMPTqK1KyjARl9wx_oVMVqJPemh1AVmxUDxodvfvjYp2AiNe8FM_mmRdYrsWWPWBnmlCjwL4wRSvwj50KxDXpz9fELCF-LQODM98bhamId1qETygk8h9vruFqXUZIhBjVM0wXPSE-hCXIKNnz2pkq95UfIBrkT7saHW_9wUMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشت عفونت ناشناخته از آزمایشگاه طاعون روسیه/ ۲۰۰ نفر قرنطینه شدند
🔹
یک کارمند ۲۸ ساله آزمایشگاه ضدطاعون روسیه پس از شکستن تصادفی لوله آزمایش حاوی نمونه زیستی، به ذات‌الریه ناشناخته مبتلا شده و جان باخته است. حدود ۲۰۰ نفر قرنطینه شده‌اند و احتمال طاعون ریوی…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/695933" target="_blank">📅 22:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695932">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dbcd65b81.mp4?token=PzLdiORBqdsqCpdEkFIcOLAHEbnBHvZbUzAaQDvhN0BprZrrKjsFWMTkmwpdec01NB58TTsQw5Un-E8H6ry5haY3a-UxdcV8X7i17hB3jzOhZQTPsKi7byrDQkA869-SPD9yBAZmUEGarnaSmS4fzeK2PfBI7PgYiXlaN8UkY_dSMniJp3Fck5f3RoeghFEG0aUJdlpPj3YXqbw0my_m6xb5Ugu9CN0iHOE8XqmBSkq2x-VA3CRydsbXGjVfquSE50n308dy9LYK2f1DHk0qNWOfnFSqj_P14sAaAbSWMH7Stlb0qvo-ggtMgpbY7l6a3IBaa48qvHM1oMCUrzcYuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dbcd65b81.mp4?token=PzLdiORBqdsqCpdEkFIcOLAHEbnBHvZbUzAaQDvhN0BprZrrKjsFWMTkmwpdec01NB58TTsQw5Un-E8H6ry5haY3a-UxdcV8X7i17hB3jzOhZQTPsKi7byrDQkA869-SPD9yBAZmUEGarnaSmS4fzeK2PfBI7PgYiXlaN8UkY_dSMniJp3Fck5f3RoeghFEG0aUJdlpPj3YXqbw0my_m6xb5Ugu9CN0iHOE8XqmBSkq2x-VA3CRydsbXGjVfquSE50n308dy9LYK2f1DHk0qNWOfnFSqj_P14sAaAbSWMH7Stlb0qvo-ggtMgpbY7l6a3IBaa48qvHM1oMCUrzcYuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله تروریستی به خودروی شهروندان در پل جکیگور راسک
🔹
بر اساس اطلاعات اولیه، این حمله توسط عناصر گروهک تروریستی جیش‌الظلم انجام شده و شهروندان عادی هدف این اقدام تروریستی قرار گرفته‌اند.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/695932" target="_blank">📅 22:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695931">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1QAQB3qb8biszRevLW8535CWG6IC7hHNM1QUa-DTMPkNsndiQ1I1ev3-r7uE7jCu3jlHTcd3SUD0VWDWcle-gXzj0P1IliUosiqqHhuM15OCm9zvNTptrvd5XRQwsS9YSkN-y6JqsIoFjL4juwPTKqN2WOqB5yfC-VmLbsju8x3bTGYb0QjwthiG1r3G2GfmHxzZmaLbQjFfuFo7sZiRX35USKe0XRAgLeXu9QB5LEgCIH8XDpOvW-wpVy0SE9T8mBB00XtVL8ey49A-1VXVpvP6y8AW7G__2cIGaKT6255z0gyPpah8-QXhJcDCtQlYQiJqiNFrmRR5GgfoIda0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
علوم پزشکی وارستگان (اولین و تنها مرکز آموزش عالی علوم پزشکی غیر انتفاعی کشور) فقط از طریق کنکور سراسری در رشته‌های زیر دانشجو می‌پذیرد:
🔬
علوم آزمایشگاهی (کد مهر:37358)
🔬
علوم آزمایشگاهی (کد بهمن:37359)
🥗
علوم تغذیه (کد مهر:37360)
🥗
علوم تغذیه  (کد بهمن:37361)
💻
فناوری اطلاعات سلامت (کد مهر:37364)
💻
فناوری اطلاعات سلامت  (کد بهمن:37365)
🏥
مدیریت خدمات بهداشتی و درمانی (کد مهر:37368)
🍏
علوم و صنایع غذایی (گرایش کنترل کیفی و بهداشتی) (کد مهر:37362)
🍏
علوم و صنایع غذایی (گرایش کنترل کیفی و بهداشتی)  (کد بهمن:37363)
👩‍⚕️
پرستاری (کد مهر:37356)
🚑
فوریت‌های پزشکی پیش‌بیمارستانی (کد بهمن:37367)
📞
05131771
🌐
www.varastegan.ac.ir</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/695931" target="_blank">📅 22:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695930">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91ec4c629.mp4?token=kSOJvTNmL9eK_L7rW5vxdfT79sGcul0dEzD9Ln9i3n96Dl5O4EsbZj61aqnsRmD7PETHzzQ7DYT0F7bAyXRkkmk6pY7WjFpSIL86BcfBLaCci1aB9hAZ2N3_ehxy9wDZ36a1tCXRdxpCa2YGmcLvSdrLacgkIInuHkzT7pvwKCEsbqUJKDuzpolK5_L_beO9i9e9W4gZn4LGStR_tq4-86wkHAV07kE4J5-LYgeWqo77AoIh1NdS0yacM4JuxEI3iR7EmXnX7OZYdd4pLYq8YDbjqhDigs5kuCTircg9YWXrYLGW7PjbU6MANHgAsLQbAYtqvsEqrrZp7mtsiNdIGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91ec4c629.mp4?token=kSOJvTNmL9eK_L7rW5vxdfT79sGcul0dEzD9Ln9i3n96Dl5O4EsbZj61aqnsRmD7PETHzzQ7DYT0F7bAyXRkkmk6pY7WjFpSIL86BcfBLaCci1aB9hAZ2N3_ehxy9wDZ36a1tCXRdxpCa2YGmcLvSdrLacgkIInuHkzT7pvwKCEsbqUJKDuzpolK5_L_beO9i9e9W4gZn4LGStR_tq4-86wkHAV07kE4J5-LYgeWqo77AoIh1NdS0yacM4JuxEI3iR7EmXnX7OZYdd4pLYq8YDbjqhDigs5kuCTircg9YWXrYLGW7PjbU6MANHgAsLQbAYtqvsEqrrZp7mtsiNdIGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرود افغانستانی خوندن پیمان طالبی مجری برنامه سرآشپز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/695930" target="_blank">📅 22:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695929">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
امروز سیزدهم مهرماه، سالروز برگزاری نماز جمعه تاریخی نصر در مهرماه سال ۱۴۰۳ به امامت رهبر شهید است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/695929" target="_blank">📅 22:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695928">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
افشای طرح محرمانه عربستان برای حمله پهپادی به کعبه
🔹
منابع منطقه‌ای از طرح تیم امنیتی سلطنتی عربستان برای پرتاب پهپادهای «لوکاس» ساخت آمریکا به سمت مکه و هدف قرار دادن کعبه و مناطق مسکونی اطراف مسجدالحرام خبر دادند. در این طرح هدف قرار دادن چند هتل نزدیک مسجدالحرام، از جمله هتل انجم مکه و پولمن زمزم، و همچنین مناطقی در اطراف مسجدالحرام پیش‌بینی شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/695928" target="_blank">📅 22:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695927">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a0c44aaa4.mp4?token=QhbjLBjr1BHHzS3uOIoB3mUSwlAYZ66PfT2vISJXBX3OKnVeg9QF3QwPsY46qVw9MCg5RXwa7KtHw6KX9Zwakf5aw4yGmnJ5ubGfuPf51DnAodWd2CWOtfayeDc6IUdXi7_24JTAnGjG7EztHGi8I7pOydBuiGN7Kleu87DR3a9N0QX-cy2v1QYaXA_YWpwG3jVgK7qh9qTBKWJ45aPoPrWGrvILW9cTNfod29douekpzPscn2XSG86PWXQtIeFCdA-RHPsVYVaz4KUThrWxiKxkdx3-8SfcKQFoEG7sSl1n0LKg2PCxOX-8dLVVG6mhxMy4JK1gN1Yj8xx5_dGjQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a0c44aaa4.mp4?token=QhbjLBjr1BHHzS3uOIoB3mUSwlAYZ66PfT2vISJXBX3OKnVeg9QF3QwPsY46qVw9MCg5RXwa7KtHw6KX9Zwakf5aw4yGmnJ5ubGfuPf51DnAodWd2CWOtfayeDc6IUdXi7_24JTAnGjG7EztHGi8I7pOydBuiGN7Kleu87DR3a9N0QX-cy2v1QYaXA_YWpwG3jVgK7qh9qTBKWJ45aPoPrWGrvILW9cTNfod29douekpzPscn2XSG86PWXQtIeFCdA-RHPsVYVaz4KUThrWxiKxkdx3-8SfcKQFoEG7sSl1n0LKg2PCxOX-8dLVVG6mhxMy4JK1gN1Yj8xx5_dGjQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفع دردهای مختلف از زبون خودشون
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/695927" target="_blank">📅 22:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695926">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a037aa0fa.mp4?token=eQOKRnHprxpeMuyhj5xm5E8RreRbOQHgRqKCMuPKmX4ZCXHYGTN4VerXzpKIzHcaQjNaeTGFII2AfHm0bhGVBcpLJatQ9ivkCdqaJoTouOyOu-IFcyz_rangHLBnfyEHimJ2NRoYFCvwW_PjTt3aNgeEzvmjBu-ZSjn_Vt6XwCKAXDxOJZ0-RqqXbeWv9YN7dnscm_n4fGaPDvPsvis2rETSfTdxchQiaJiVRkj6XFndP1qh9gjCg9gKPQzQYjj2xBibWcai41WLJHzos5Rh-YevdTdFzzUXp79oiyBCgfhcABVw5P4x4YPrxBKm5LTE5sd1gZAzdSQ5uSHdbSyr-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a037aa0fa.mp4?token=eQOKRnHprxpeMuyhj5xm5E8RreRbOQHgRqKCMuPKmX4ZCXHYGTN4VerXzpKIzHcaQjNaeTGFII2AfHm0bhGVBcpLJatQ9ivkCdqaJoTouOyOu-IFcyz_rangHLBnfyEHimJ2NRoYFCvwW_PjTt3aNgeEzvmjBu-ZSjn_Vt6XwCKAXDxOJZ0-RqqXbeWv9YN7dnscm_n4fGaPDvPsvis2rETSfTdxchQiaJiVRkj6XFndP1qh9gjCg9gKPQzQYjj2xBibWcai41WLJHzos5Rh-YevdTdFzzUXp79oiyBCgfhcABVw5P4x4YPrxBKm5LTE5sd1gZAzdSQ5uSHdbSyr-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین ویدئو از شهر طاعون‌زده‌ شلخوف در سیبری که مردانی را در سطح شهر با لباس‌های مخصوص محافظ سفید نشان می‌دهد
🔹
هم‌زمان گزارش‌هایی هم درباره قرنطینه شدن بیمارستان شهر و کمبود آنتی‌بیوتیک در داروخانه‌ها منتشر شده!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/695926" target="_blank">📅 21:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695925">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX0HZOctQuTi186tnvhSYM6hIR33HrY0vGGfQwF6DVgykyHuoGwiO_3tBm0jBWxdnvwMNo5MhgIEPZHOL4XXL_wT0x4dRf9X-S-FwOTOxRZdsUh_ED3kN8s_xEdGfeKK5vtX5Dv7iJAhuni8xTAiuDr9XQtAIt4KLvUjmi5BVVw49SXcHLNSebOrM-mJrwurG3IkxARiUDbeRiBmOcLblnsHRqSQtMwAXwi9v-SnCAf5ci50Zete3XXLrh0BTk-U0qePP_Fc_GZU86K061ju5xxb7XT_3KUOka8cu2GKad2Aw3mjJ53__znKe2slhcURXFCVw9xFsGVKOz6M86976Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریشه‌های شوک ارزی در شرایط جنگ و محاصره
🔹
پویا جبل‌عاملی ریشه اصلی شوک ارزی را کاهش شدید تجارت خارجی و درآمدهای ارزی در شرایط محاصره و جنگ می‌داند؛ وضعیتی که به گفته او، صادرات کشور را به حدود یک‌پنجم گذشته رسانده و بازار ارز را با عدم تعادل روبه‌رو کرده است.
🔹
او تأکید می‌کند نااطمینانی درباره درآمدهای آینده دولت نیز از مسیر انتظارات، فشار تورمی ایجاد می‌کند. به گفته جبل‌عاملی، تا زمانی که یک چشم‌انداز اطمینان‌بخش در محیط بین‌الملل ایجاد نشود، ابزارهای اقتصادی به‌تنهایی نمی‌توانند بازار ارز را آرام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/695925" target="_blank">📅 21:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695924">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
عربستان اعلام کرد که ائتلاف مکه توافق کرده تا در واکنش به حملات حوثی‌ها به خاک عربستان اقدامات بازدارنده جمعی را به اجرا درآورد
🔹
این تصمیم پس از برگزاری نشست اضطراری «کمیته راهبردی سیاسی و دفاعی» این ائتلاف در ریاض اتخاذ شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/695924" target="_blank">📅 21:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695923">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MR3AcaK2VXT-j21_pujrVXehOv4DRCPCH1GEUVaQS3RdSLogySTit3PVjIymTqjhQLMjgGBILd9E1Kz3eBekBVXcqbkAxyTeO1Uhc3iulSwET1-Uz4rptin5um5DhSIe8POE5kaHlAk0wGgb-ne6-9La3gVexzutiCKWvfGfytnSUsd-YGAjg1Yk2yVQ1ql5_CiiT5DGAU9sM-GJId-oEsUwjM71vB4K-dHlqvYgtgZeWR1eI8w5cRgfu2YjL0X8-MqlZ0Y5ZwYSj-aWjE1CaBfIzgRA9qC44lyCtpIahJV3vXBmm7c9892HK6ou3fv0dAVWhryoue0mylFp7hRQPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صورت‌حساب سنگین ۲۳ ساله آمریکا در عراق
🔹
از هزینه‌های تریلیون‌دلاری تا آوارگی، ویرانی زیرساخت‌ها و پیامدهای امنیتی، مروری بر میراث حضور آمریکا در عراق.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/695923" target="_blank">📅 21:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695922">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
آمریکا با فروش تسلیحات یک میلیارد دلاری به امارات موافقت کرد
🔹
این قرارداد شامل فروش سامانه‌های تسلیحاتی دقیق و تجهیزات وابسته به امارات است که توان عملیاتی این کشور را افزایش می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/695922" target="_blank">📅 21:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695921">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS_Z2uqJD3Hobew9w9hNoS5NicTIM3nNnShS7iF-I60ZMkknk7xbGiERBnrKQjMlPVu7vTQNABxqFBWP-Sq_4MftiHTQMpqUn0QsTr6trmQM0yx9LRnNlUwZkF6uppOl6jGqV03y8EnggCAVgmlOeZQ-DA2yyUyLxSp4WZmSkHgn3sHCXsjl9FJN9-EKyUILpuyETimKyLXWfzzW9UzxZJa4T0buyk7QAhzKo-PFxpLA1MjaindXXJRMbg4lI8lmXZfwXRxa8CYhzmwnX34yCLs8tc4omrVSyuze4Pcc7FvYCvyu02NToa8hfT5_kxppJCCC69HI_Z7bOng0zS9zng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دعای خاص استاد شفیعی کدکنی برای ایران: ان‌شاءالله ایران سربلند و مستقل باشد؛ صددرصد به ایران امید دارم
🔹
استاد شفیعی سرش را جلو می‌آورد تا صدایم را بشنود. «شما برای بچه‌های ادبیات با کلاس‌هایتان همیشه پناه بودید. آینده ادبیات ایران را با نسل جدید و این‌همه تغییر چطور می‌بینید؟» می‌خندد و جواب می‌دهد: «والا غیر از خدا هیچ‌کس نمی‌تواند پیش‌بینی کند ما دعا می‌کنیم که ان‌شاءالله ایران سربلند و  مستقل باشه.»
🔹
یکی از همراهان می‌آید کنارش و می‌گوید: «یعنی امید دارید به آینده‌ این...» شفیعی‌کدکنی سرش پایین است و اجازه نمی‌دهد جمله تمام شود و می‌گوید: «بله. صددرصد»./ فرهیختگان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/695921" target="_blank">📅 21:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695920">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
حمله تروریستی به خودروی شهروندان در پل جکیگور راسک
🔹
بر اساس اطلاعات اولیه، این حمله توسط عناصر گروهک تروریستی جیش‌الظلم انجام شده و شهروندان عادی هدف این اقدام تروریستی قرار گرفته‌اند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/695920" target="_blank">📅 21:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695919">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiWaP9hTEYE66h9EOT2XAm0MuRwGouZ4YdHdqu0sePFvtiKgue2uBAAdKMHQA7uf-0AMLli-oQDjl98XPQ5TKZY5srRH96nITHWyseR71FLteci3o5afTwczzOPuTwwGNbFf1vOYevpd_snSPVWo7IR5sUuiVRTgKHYfPDKAfGZw8DpebyXzd0VW9BUiRTnC4LQGyEeHTM0xKFRsuMzPRPFkxiQ_Sz9kEcvZlOShhxbSUrPozneNoxiT-orgZ7U_QrRPtEp87k7oMB5hT_pfsWbRbOHKnp8n9ddcLBiceJVilIY28lWJo0WMfJEpwNUKQMfC_RwXddbbvX9N4pp9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تجربه فرهنگی با اعتبار دیجی‌پی؛ کنسرت همایون شجریان در شیراز
🔹
کنسرت همایون شجریان به‌زودی در شیراز برگزار می‌شود و فروش بلیت این رویداد از طریق
فیدیبوآرت
انجام خواهد شد. دیجی‌پی نیز به‌عنوان حامی مالی این کنسرت، در کنار فیدیبو و دیجی‌کالا حضور دارد.
🔹
در این همکاری، کاربران می‌توانند با استفاده از
اعتبار و کیف پول دیجی‌پی
هزینه بلیت را پرداخت کنند و در صورت استفاده از کیف پول، بدون نیاز به ورود اطلاعات کارت بانکی در لحظه خرید، فرآیند پرداخت را سریع‌تر انجام دهند.
🔹
حمیدرضا سعادتی، معاون سوپراپلیکیشن و مارکتینگ دیجی‌پی، این همکاری را بخشی از توسعه کاربرد خدمات مالی دیجیتال در حوزه فرهنگ و سرگرمی دانست و امیر بهدانی، مدیرعامل فیدیبو، نیز از آن به‌عنوان بخشی از مسیر توسعه فعالیت‌های فیدیبوآرت در حوزه موسیقی، تئاتر و سینما یاد کرد.
🔹
این همکاری با هدف ساده‌تر شدن دسترسی مخاطبان به تجربه‌های فرهنگی و ایجاد زمینه برای همکاری‌های بیشتر فیدیبو و دیجی‌پی در حوزه هنر شکل گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/695919" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695917">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47e78e0ce2.mp4?token=ds_Tv2p26b3pR8lSpJwjcDvH1JjO0udE4koO5wbpJOPlYvnE93Sdjqzr9WsNHaAvaqZSHuOThui6Y3OI6e0D0o2xPeL63xE7tOf2MYEPU-ED0tjNK4Snl_1WrIND3eGEbDYmoHFqXOjZoVL2pwey9OfYnSk1UqyML2p7cxYbpVK4izjPBXPH9JwgcfHdyFhCdIx7VqmhmkV3DGHcqpJMU-IIM90hhp9zDCJ12OB8KLe9uI4dC1LH0f1jJNfG0vNnhcOwv7C1SFVtW9SmNTXIYW8QHAgr8l4ZeYuEbbXBssYp7bcnWoAef9IPPpnq-Qm2WBYmKO0M0HLa0qZWGiVWJIVCSxKdH1qXZItNkXF6jFf6vFOVLpRyMBdADpi5e5-SOxMLVob6Ms3fgIzURMhZBfp_ceWsjhRqI4W5nt_mTdM57KQWSfKbAE-IzAxCadVSKeawjmm-kyJg1yew-o7FwNe2tLpx7V-BwzdS-ANKhtq3ZyLBB-EpY4-2sK-4utHFuZvaR3O70unS95fVh9uuHxDdrdUunE-adFHgaROHrt8u84AR6s_nJwAJr8MORoiGPRRl56yoETHje3DjDxUJuJ2EPAamMVbS4xnaoLfuCqAoui1rOeM7wwF-nSxT_qhJL0Nh1edmYfRrMSPr5n_0PLeVAkoDymcSGnZHkVizrV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47e78e0ce2.mp4?token=ds_Tv2p26b3pR8lSpJwjcDvH1JjO0udE4koO5wbpJOPlYvnE93Sdjqzr9WsNHaAvaqZSHuOThui6Y3OI6e0D0o2xPeL63xE7tOf2MYEPU-ED0tjNK4Snl_1WrIND3eGEbDYmoHFqXOjZoVL2pwey9OfYnSk1UqyML2p7cxYbpVK4izjPBXPH9JwgcfHdyFhCdIx7VqmhmkV3DGHcqpJMU-IIM90hhp9zDCJ12OB8KLe9uI4dC1LH0f1jJNfG0vNnhcOwv7C1SFVtW9SmNTXIYW8QHAgr8l4ZeYuEbbXBssYp7bcnWoAef9IPPpnq-Qm2WBYmKO0M0HLa0qZWGiVWJIVCSxKdH1qXZItNkXF6jFf6vFOVLpRyMBdADpi5e5-SOxMLVob6Ms3fgIzURMhZBfp_ceWsjhRqI4W5nt_mTdM57KQWSfKbAE-IzAxCadVSKeawjmm-kyJg1yew-o7FwNe2tLpx7V-BwzdS-ANKhtq3ZyLBB-EpY4-2sK-4utHFuZvaR3O70unS95fVh9uuHxDdrdUunE-adFHgaROHrt8u84AR6s_nJwAJr8MORoiGPRRl56yoETHje3DjDxUJuJ2EPAamMVbS4xnaoLfuCqAoui1rOeM7wwF-nSxT_qhJL0Nh1edmYfRrMSPr5n_0PLeVAkoDymcSGnZHkVizrV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطارهای معلق ووهان چین؛ واگن‌هایی که از زیر ریل آویزان‌اند و کف شیشه‌ای‌شان منظره شهر را زیر پای مسافران نشان می‌دهد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/695917" target="_blank">📅 21:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695915">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ اسرائیل: کمک‌ خلبان فلای‌ دبی قصد داشت آن را به فرودگاه بن‌‌گوریون بکوبد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/695915" target="_blank">📅 21:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695914">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
یکی از فرماندهان پدافند هوایی خاتم‌الانبیا: ادواتی از دشمن به غنیمت گرفته‌ایم که در آینده نزدیک، به لطف الهی علیه خودشان استفاده خواهیم کرد
/ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/695914" target="_blank">📅 21:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695913">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمدرضا حسین زاده؛ یادداشت ها، صحبت ها و سخنرانی ها</strong></div>
<div class="tg-text">#یادداشت
📊
داده ها؛ سرمایه های جدید صنعت بانکداری
🔸
در گذشته، سرمایه اصلی بانک‌ها را شعب، ساختمان‌ها و منابع مالی تشکیل می‌داد؛ اما در عصر تحول دیجیتال، داده به یکی از ارزشمندترین دارایی‌های بانک‌ها تبدیل شده است.
🔸
هر تراکنش، جست‌وجو و تعامل مشتری، اطلاعاتی تولید می‌کند که می‌تواند تصویری دقیق‌تر از نیازها، رفتارها و ترجیحات او در اختیار بانک قرار دهد. تحلیل هوشمند این داده‌ها به بانک کمک می‌کند نه‌تنها بفهمد مشتری چه می‌خواهد، بلکه بداند چه زمانی و با چه خدمتی می‌تواند ارزش بیشتری برای او خلق کند.
🔸
با این حال، داده به‌تنهایی ارزش‌آفرین نیست. ارزش واقعی زمانی شکل می‌گیرد که داده به بینش، بینش به تصمیم و تصمیم به اقدام مؤثر تبدیل شود. از این منظر، رقابت در بانکداری مدرن دیگر صرفاً بر سر جذب مشتری نیست؛ بلکه بر سر شناخت عمیق‌تر مشتری و ارائه تجربه و ارزش متناسب با نیاز اوست.
🔸
در کنار همه اینها، یک اصل اساسی وجود دارد: اعتماد مشتری. داده‌های بانکی بخشی از حساس‌ترین اطلاعات زندگی مالی افراد است و استفاده از آن باید همراه با امنیت، حفظ حریم خصوصی، شفافیت و مسئولیت‌پذیری باشد. بانکی که بتواند داده را هوشمندانه، امن و مسئولانه به کار گیرد، نه‌تنها خدمات شخصی‌سازی‌شده‌تری به مشتریان خود ارائه می کند، بلکه می‌تواند از داده ها یک مزیت رقابتی پایدار بسازد.
داده ها، سرمایه های جدید صنعت بانکداری هستند، اما اعتماد، ابزار مهم حفظ این سرمایه است که نباید به هیچ عنوان آن را از دست داد.
@Mohammadrezahoseinzadehh</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/695913" target="_blank">📅 21:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695912">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9eb85747.mp4?token=JUIxMvOyqNRrjiOg3fsUm1xuTYH5-ZYOJ9JCS98p6z2rsrYEC9cf1qvXJ_XVqNzHE7dB3uQ6S5ZnKqM2EFPTGU9Y6pzU4F-XrNtIDqmx7qZdlkNQivScNh8wnlVjiC-B8EiHFZYjClWxrBwKPjOBGmHQ4Qk5n9Qf6FtlPQ33-Kay3jP1DJle1mfhwjUOmE0-Xjf5hw0loOyRqjfMcSNLxP4G-gw8N8DOLAGqVWY1I4konK0_yykJ8pNNWD1J5lrqG4EuZDrGWDhkPES-P6j8oJMi2wQLh9VjfnsDR3MpeNdC964WlKvzqzEAlByIb98Jw6PjB90RPKf32MdN0v9YcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9eb85747.mp4?token=JUIxMvOyqNRrjiOg3fsUm1xuTYH5-ZYOJ9JCS98p6z2rsrYEC9cf1qvXJ_XVqNzHE7dB3uQ6S5ZnKqM2EFPTGU9Y6pzU4F-XrNtIDqmx7qZdlkNQivScNh8wnlVjiC-B8EiHFZYjClWxrBwKPjOBGmHQ4Qk5n9Qf6FtlPQ33-Kay3jP1DJle1mfhwjUOmE0-Xjf5hw0loOyRqjfMcSNLxP4G-gw8N8DOLAGqVWY1I4konK0_yykJ8pNNWD1J5lrqG4EuZDrGWDhkPES-P6j8oJMi2wQLh9VjfnsDR3MpeNdC964WlKvzqzEAlByIb98Jw6PjB90RPKf32MdN0v9YcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های یک دکتر: حالا که هوا سرد شده به‌خاطر یک سرماخوردگی بلافاصله آنتی بیوتیک نخورید؛ بدنتون به آنتی بیوتیک مقاوم میشه
🔹
یک پسر ۳۲ ساله و یک دختر ۱۹ ساله به خاطر یک عفونت ساده فوت کردن. چون از بچگی به خاطر سرماخوردگی آنتی بیوتیک میخوردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/695912" target="_blank">📅 21:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695911">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
اداره ارشاد خراسان رضوی، با لغو کنسرت علیرضا قربانی در مشهد، اعلام کرد: با توجه به «برخی ملاحظات» کنسرت به وقت مناسب دیگری موکول شد
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/695911" target="_blank">📅 21:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695910">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9xHr1nMFZzCF8dBVkKNITfI1Kccz9Dg8GyBjxVGDkj5-kcknp7Cd_zU4qW3Q_Ywv6FEIAqi0lyqFImMf7NM-ngghHvWMFaZ2aMO1hUFg-h4QRQ1J6Yd5VV6J7pmwjZaA8v8cqXmGrcYKf8wHQyejLnpXg6C1mtznzZIyux8gQRjQn_dFZIPRKBbeN3uiGJ-gVsepvAS8aQJi5owR6GEYCpYB7Y187KTzwC5ElHRW6YqmJLXaJq2NHe-9aIEMz1Un0F-Z0P_Rszr9WVBJbZM9pFUNLF1eMukn3ltbaBomwqQWIzN7a-VuqYYXczDdMCyhzGltpsucvqB2dM4_zz8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای هر کاری، سراغ کدوم هوش مصنوعی بریم؟
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/695910" target="_blank">📅 21:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695909">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efda9da751.mp4?token=td8jXMe0fnD6lxo4uPAwutkffOobiVcWtA0fD6T12E7c4cv5wdQd4GbkENaOYoTOATKE04K0TWsGHstN39uF3H3aanrWXqcNtzDdX59ml9Ldd5BgL4oH-IX-3V3Bw9jE7aBvy0qy4bKMJUHfdqsqPpeq0rkMQQY5zoexYrdVlAd_Q1qvcEM9GlKvC_hmBypM2gpn_BeJk4VO1zysXCRSrF4rBQNgVrmvFVIJm9vGpDQS8xWlMJkJfcL3qDI8hmuG8nHpj4CFAxYKEb8XABD8m6grPj7XtSQlxYK_MxzZoyVfm0x876WqrsRFYlOjW_007_DpeAjjWEvP_ny6CsYKoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efda9da751.mp4?token=td8jXMe0fnD6lxo4uPAwutkffOobiVcWtA0fD6T12E7c4cv5wdQd4GbkENaOYoTOATKE04K0TWsGHstN39uF3H3aanrWXqcNtzDdX59ml9Ldd5BgL4oH-IX-3V3Bw9jE7aBvy0qy4bKMJUHfdqsqPpeq0rkMQQY5zoexYrdVlAd_Q1qvcEM9GlKvC_hmBypM2gpn_BeJk4VO1zysXCRSrF4rBQNgVrmvFVIJm9vGpDQS8xWlMJkJfcL3qDI8hmuG8nHpj4CFAxYKEb8XABD8m6grPj7XtSQlxYK_MxzZoyVfm0x876WqrsRFYlOjW_007_DpeAjjWEvP_ny6CsYKoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این اشتباهات پولت رو قفل می‌کنه!
🔹
یک اشتباه توی سرمایه‌گذاری هست که ممکنه باعث بشه پولت رو، روی یک دارایی نگه داری که دیگه ارزش نگه‌داشتن نداره،
اما نکته ترسناک اینجاست که ممکنه اصلاً متوجه این اشتباه نشی، چون این بار مشکل بازار نیست، بلکه احساس خودته!
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/695909" target="_blank">📅 21:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695908">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
سفارت آمریکا در عربستان هشدار امنیتی برای آمریکایی‌ها صادر کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/695908" target="_blank">📅 21:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695907">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtMs3_qIy5BYpPrk5deIk4NvPetiJLhcPjTZ6esFVcRvCy9BwLBNswD_Xt5LbPycIrthDfaQDjGyzXoRv-F_2gLCyahOib71M84evqQhQ4TGawXazljnv7qNn5cBwCkcrYc_PgOBB8p3otB-5ayqe4NOlvfI6KQVKfSKlPvAybDfyXu47PsaaxXcgjlgssK-xi9k3hFpWfrR-PZsSsne9JZ2hH1Fp7v6BF5aByCfSh8r0wdEBtbqm-VjPSSPjWDlnarDvmHx0bCusEKEjex_FC2OpeTLTfcg0okAZRWS0fjmeWnsuk6hpMEBAjDAHiA8ZYHE_jQOfs4Gaw_NfYwybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جشنواره هدایای رویایی اسنوا
🎉
با خرید و نصب محصولات منتخب
🎉
—— بدون قرعه‌کشی هدیه دریافت کنید ——
با خرید از اسنوا، علاوه بر دریافت هدیه از تخفیف حین خرید هم استفاده کنید
💰
⏳
فرصت، فقط تا 15 مهر
❗️
🔥
برای اطلاعات بیشتر وارد لینک زیر بشید
:
👇
👇
👇
https://lnk.snowa.ir/snowa-telegram
.</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/695907" target="_blank">📅 21:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695906">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک گردشگری | TOURISM BANK</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyzpjQAezmA0-vr0HN3XkuPXm56rF5IkawCe83D5f2ovb2Pfr_vsMwSdkZEuZlM4_aE5uS2FMeFtn63XLyg1mAcxUC65QOSPxJwBCUe-jOliUUA7OzrQR2u9Tt_DbnPKDwZbhDfy1A6QTCVDdIBry_BM8hb3ardSyOsy4rpEmmBAUc2nhoJ1sl8OIJU-bhHSCqqE0a45QGO15mHk6lN8aInduV-ugXpEfyiZQN8I3GPgpuUXYCKVimCr59MlD6v9tCVORVlOIiRduZ7CttC4YLQ12nRcQm_AA0YXM5rYdLCF1wLVgxzIqIAthJsJJzenkXsa_qNz8546leMXrQtxcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
تمدید شد!
قرعه‌کشی حساب‌های قرض‌الحسنه پس‌انداز بانک گردشگری تا۱۵مهرماه تمدید شد
دارندگان حساب قرض الحسنه پس انداز با حفظ یا افزایش موجودی می‌توانند در قرعه‌کشی شرکت کنند.
🚀
هر ۱۰۰ هزار تومان در هر روز = یک امتیاز
🎁
جوایز: ۲۰۰ جایزه ۲۵۰ میلیون تومانی، ۳۰۰ جایزه ۱۰۰ میلیون تومانی، ۴۰۰ جایزه ۵۰ میلیون تومانی، ۵۰۰ جایزه ۱۰ میلیون تومانی و بیش ۱۰ هزار جایزه نقدی دیگر.
📅
دوره محاسبه امتیازات: ۱ آبان ۱۴۰۴ تا ۱۵مهر ۱۴۰۵
🎯
قرعه‌کشی: ۲۶ مهر ۱۴۰۵
💳
حداقل موجودی برای شرکت در قرعه کشی= ۲۰۰ هزار تومان
افتتاح حساب و افزایش موجودی:
🔸
مراجعه به شعب سراسر کشور
🔹
آنلاین از طریق اپلیکیشن توبانک:
tobank.ir
کسب اطلاعات بیشتر:
📞
۰۲۱۲۳۹۵۰
__
🔴
بانک گردشگری؛ فراتر از مرزها...
@iran_tourismbank</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/695906" target="_blank">📅 21:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695901">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSfMj4vMdIT3dlfHhTFWceXPQhtPNkjuQXzNt7hlMbl9jkzY8Yw7uVP1ztypHyPJTfS6ahjzJd10Y7YXgCO0_whZ_KK1TFm_Msr_2RCTBw6mIkcQ_BA0QBT2Fap9if2tySJgrCSqtKGnRnihpeFl4vXzzVqL3vAWseJMprCo8VslAx7jFJ98-E-wY-frhDCwx6AG7CtZxwnmvaHnwjjZNHtEpVqpJzZxENikiR4CD7R0nlurSO1wnvc42ykCF_Qdg3mERKFeHzz7PXrBZ_VxbsWSNTo-r1KceWuk9dwaGxgxfqaVnF2Gy8jNUUJRv20JmbFYUzDinvFYKn_S7MQzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRvb5kSS6z67vdOxwwgF_1dRQlhd417owVis4ILMMpu7CMS7nGA2gbqQY6l8Ia_VrVX0612YpN1fPxtxlTwTdC6cEKO1V7jY-3DCG_Hda6bZtIlWvVQ1UF2F3Iba_Zf6WOQHW3YboAlQh_-qxpd2L-3CpI4IH__7jIlCsD_WsU0jkJJnpc5ydg5YG2zQt3x1mARgzHAxj504eWL1am53AYGreb5hPMGFYE3FVffT7YntYUpFAj5OEOgGlmvgp1Pa205gbFuaEnEnAOCuvwGQc6RLdPPEgercG4tSyWHC3miJ8hSPAQT-iSF_dR9CiO2wIENP3su_4PWB0NeolBr5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIF8p6BK4f2U7CpUTR8wxUOUOcZfaJBX83zGxJJXOhEzqaJT152NJgHs-DiPJ0l197g9SDRqvnAcikaFyYUloAuuL8PCf9UNvBNrfQkPh_0JwyiLy0fHu2tPSfPFWK4cdpEE6DbeCXbMDX_V1M1i2kw2mLB_LZ4KdZz5B8og1hV84uRrCS_GRsjs4O9F2vKU_T3y3X5zb0KQ6LAM009s86f1YaoxOgEmhJe0wTSEwZdkhcMn3BBO4jJ97E3JS-oRZVZL4hnTOgpHa9SjCe4a8XTA840nMjPzyEKRB6YBFZxR9gYBwacNbqN51gHwvY2Wu08IlE15QdLVKHk1xqAwvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NgC3NW7TqU-dgZ3eKrekhZ6MUc_qb8aUurqU4LLjjw4dFksdfz3nF8xdtqQeDuLz369CvVxnUpTCf1Hoxf4r1Vv371bkPiDfWtPZ1bZ1tVBMZM2N8cJkgjnML8eLXynFeM2DGtmUWclRXL2aRUTuYnWCkMwdrxNRDgz7jYXr54XcG4qOvoPPM3JCyOEymUt2rR0oMHRSeNtB-EpDwMDBUiRXX1IlKJ1rXD0yUeRztpFT1aUyLiBkI_msOSeDduwyM_NJxAjcci1HD0E_ZZDkkFlqHilehd92JaB5qIbQoGargiciK6HUJuXaMeXluZDhtwlbE_8rvu2InFsAA2fjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eB9U03riCS9I9JH9NPqamhUYg_GR6d8Uvh6u14TgT7vxmlPEoDpxF1HB-AqAlV0QQLFA2Hfk-vMfXUnQeV-UlTdHO7HrQIJAYoH7l6gHLv_Y0-21jOl-lotH-MqBvoKRHODOowMhXCCPUMQy26dMQaWAiOJreCyBNiv2Ca8_WQBGXlaH4b0Y1erc20d8kj295oXzvhWc5fC8bLxocxY3d5bgj5exhsG63SR_CnSNxcEuvNgMMnmNDaZ1C3lmMeWHLOF4oOazAPVum0sMGQQ3m-WrI1-_7f9bjdQDWka9568U_3vzUmnI5KL_b86NOWnuznulhNDFwas8LjABw1cM6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جزیره بان‌وول در کره جنوبی؛ جزیره‌ای که در آن همه چیز بنفش است: ماشین‌ها، خانه‌ها و گل‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/695901" target="_blank">📅 20:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695899">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGdITTRXQVW_qjCJ5U6VBClibYc03BM1pqtAVMbgVx38g45OPMnermXITzorv_4tgWXBrzc_JYHmc2k98H0YNVClR5QDEmNz1kI4fpjjNXXx56xqbtTOqDy8LM7o9ZCNujUJQXfWH_Fj_alJ-yt4L2O28E0q4foGhB5BRwJZrESZsvJnUTeYvmEKAhGpgPkPXr2qDpamh5rEnJxVMgdJd78ppu_4fjx_ogqD45hE_JFlNNRsMesLdcuVrOUpLj5QTDblP0OO1Oon-mvxXRhPwZKPNRpO8gTVLoUJflgRlRznUgfaDJqmWjgOfmfqriz5NLQx2K2xm_lhUl6OIXCiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وعده‌های نافرجام رفع فیلترینگ
🔹
در این اینفوگرافی، مروری بر وعده‌ها و اظهارنظرهای مسئولان درباره رفع فیلترینگ داشتیم و سوال اینجاست،
بالاخره چه زمانی رفع فیلتر صورت می‌گیرد؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/695899" target="_blank">📅 20:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695897">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VC_doKI7lbAue1gfUhUlRTRBxNCTqOl-lkw6NHAm92Yaj-68yUFEnnnJqgmrFYz1I-G8WIXP6XVLl6oL0G8HFBxQpkkgrm35MiV8l4zO_5MdTVFZp-TTo0HX1jyX87SHivS__b7p5M-2KXdtZcExqPa4EXUJ-oykPmtSh-dc7DogGmt0xofR5fSsA63SPps6PiXe6_29LWjSe8Ox_B-ke2KGk6JseYLGvDJtlpk2X7pfSLOI_m6glnar_iOZ0sfQfM88QQCyRPs6u4_szMz8zVNX6U_QSv0HvMqpYCIK0XQbDZZuihw_kNVtenHlgSuuSyQqrwtU_Me45DC4ysHzRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JB5EIToT8dIjIlh0Bk6k3rXZdpRBJyUpq4QFCGucpQT-LRW6MIhcrTHlUy2UXZuLJ9SZ0ex2tPSdgCQu041J2-cDR3xn-2OW-VnOQSBXS0z8Ax7bAZpXNH4uSrD2sUGgBZp7T7YD08QjDeC9K4I-MFbQFp9ACf9Cfq4AK5Af_sImXZ_DQ5k3QoDQNR90dhRGAP1M1FzS3GflfSF_B_YilvHcDcT7E0TaD9y-uiqlOZMtUYLAGj_FAhtLe3Sq82nlpvSl9Dbyc8hmZw8ZsU4O1-zV3Hw3ZFg9uv_08J_PnW9xPQzmOmXqNnW2dzkjD_buCXP6l6Z6jq2djfmPG1Mk7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منابع خبری از اصابت مستقیم یک فروند موشک به فرودگاه ریاض خبر دادند
🔹
در پی این حمله سنگین، دست‌کم ۱۰ هواپیمای مسافربری از فرود فرودگاه ریاض منصرف شده و مجبور به تغییر مسیر اضطراری شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/695897" target="_blank">📅 20:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695896">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
پزشکیان: آمریکایی‌ها تاکنون ۳ بار پس از گفتگو به ما حمله کرده‌اند و این نشان می‌دهد که آن‌ها به دنبال گفتگو نیستند، بلکه هدفشان ساقط کردن نظام جمهوری اسلامی ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/695896" target="_blank">📅 20:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695895">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">طلا و تترم رو نگه دارم یا بفروشم؟
از موج صعودی اخیر جاموندم؛ کی طلا و تتر بخرم؟
همین الان کدوم بازارها هنوز نقطه ورود جذاب دارن؟
نرم افزار مشاور سرمایه گذاری اکوتراست
👇
برای دریافت نرم‌افزار کلیک کنید
برای دریافت نرم‌افزار کلیک کنید
برای دریافت نرم‌افزار کلیک کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/695895" target="_blank">📅 20:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695894">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okVdHwMNDQNFsb0EZ5J7WKE8wmyLvSlVnly5W3V3B1wEPt-eEvtqrmYKrfE_CByRKgUb7CGpzULxI7RosXQNSiEL-p1qNmZCJI1CHqeJuvqJo892s2l5zyev753BEzZYL7-PGUoGHEL5O4zwEWN9Kq4L_WDZKlctopOGWITQh63UomRAi1QccUSD2SDSORmb445PA0jZnqK8u8d60YbZnAZAovcAgKqrTLvtUzMgDkWFsAhZBUfHoAxzPJaezKsc9dOoOdKmeV6zLm2nkQJDpIsap0FiourEo_Ypd_tImG6XTS2k60CukBX-dwro88wDzNAOT7_Lw79-ril2lhkQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تتر بعد از موج شهریور، فقط ۱۴ روز استراحت کرد و دوباره وارد موج صعودی شد
🔹
ویس زیر رو بادقت گوش کنید
👇
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/695894" target="_blank">📅 20:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695893">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
پزشکیان: مشکل ما با آمریکا این است که هر بار به میز مذاکره می‌آییم، بلافاصله جنگ به ما تحمیل می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/695893" target="_blank">📅 20:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695892">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
پزشکیان: با دشمنی که هر روز ترور و تحریم می‌کند؛ مذاکره معنا ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/695892" target="_blank">📅 20:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695890">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6708cb5096.mp4?token=Qe1IacYnrxrV8zuSZTgJPDHcjoOD9B7gaVnZvBoiTL-9S5H8zdRw1PQZX1Fkted16xVvXXymuwhjbL-C9PkcNsdpQP815X_GFy1X5WCmbwojO7mtoazlpXXeBrJa9k2kvMRS56YPKCMrHfr_LNWEaAHPOZ6rDWEu9fi5EuBQGxwVMiQi3NqJnp_pCR6YRqJGGb7H8ZOH5tNehYIKc-CojupsWCK2DvzJaHM23nyHQWY5fRBjk6pHcYc8oFJic_PMddiVd5hvWAriYX5k939XkU10ztmaALGpr_u5dB1ZnJcWY-fu_wkaAuvv00nnC7nqfyIpXrLp6VKnb4Hu5Y8pgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6708cb5096.mp4?token=Qe1IacYnrxrV8zuSZTgJPDHcjoOD9B7gaVnZvBoiTL-9S5H8zdRw1PQZX1Fkted16xVvXXymuwhjbL-C9PkcNsdpQP815X_GFy1X5WCmbwojO7mtoazlpXXeBrJa9k2kvMRS56YPKCMrHfr_LNWEaAHPOZ6rDWEu9fi5EuBQGxwVMiQi3NqJnp_pCR6YRqJGGb7H8ZOH5tNehYIKc-CojupsWCK2DvzJaHM23nyHQWY5fRBjk6pHcYc8oFJic_PMddiVd5hvWAriYX5k939XkU10ztmaALGpr_u5dB1ZnJcWY-fu_wkaAuvv00nnC7nqfyIpXrLp6VKnb4Hu5Y8pgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جدید از یحیی سنوار، رئیس فقید دفتر سیاسی حماس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/695890" target="_blank">📅 20:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695889">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
پزشکیان: با دشمنی که هر روز ترور و تحریم می‌کند؛ مذاکره معنا ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/695889" target="_blank">📅 20:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695883">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hY1EuGG3OBBpGZwktQ6y0obVqF-tMVLQg3ecJylvz1UZFqJKKMW7k1JQ_Kunax5RN_RM5tZlibKkwQrgW9zZW63c4LZcs_g6aohziUD4Ih6-7tY98mJiyQzMNeA-d_2OO0l6GokFjuwpudclL49YRj4HIcRPsC5ammzuulzDhJv1gjjWvvaTtM46BO71c3Bd9hx1L62P3Pj3PYzdbokRjWYK9hw94mrbFmx-xcv1HN6-BzA00_1YwSeoz-Z9lbD_RCXIMgC_LXSqqY3zBWWKwea0_hlUX6LjOxjHpbsTeAGgocuHsVl-K0iqrLsK3a-w9wTGZufMAbjyec-osH9jNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gopQNKXAaz7tTXVtsAv4__61V_NXWXtuljUAHmTmP_Wwu9n-7iSw8cLXi0g97vwLBST7HWZQGSy7BsYufwH-1OOtkJT0AVhYjUaraKbxCB4eEpJXM5JDpgm2fUr6gWKNne6mDbNvbjmJt3Bdp-83cWpEiUhc1SPTUMEXGcAxHXFJKIZOjKoshgLIwALpEZHJ0G6qr7idghx6eYKpzABcz6Led40SPMx00Qhv0dW_SXdmTaSxOMf4Fj_Zm_4ZP7h8WaQXrDDpaMtlfh87wfKJZZ-5NhooQWdb00IFT5oKVGwOygJqyvW9yDcbhXEN1EQhCo-bBdaAG8J051Xln23zvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3Ri9cTK31Ia2qhxaA0Ld4bpbXdSsnchunXif6S3iNelVc_N4nTbJxwK52HDlDqPjxZlRpStdpdE2nc-m2WUiFrH05NjqSLhVNtOu2dKyfyjNaA0PjtVHkB4Yc9xQwdBnYU6dF-2Zk8mcio6v5u3qd73uGP2aghljOISrb2xhw2RXrWuG2BfLadfe9El-LpeAMatBatdRMIjiQ05UjJuzjd-UQiLCydMRyxQGyO1yns3avb9B89Q9SM5ZlD-0KeqYIKIWLTo-aXwIRnXTpzyipMxk4GXRBA7UfoGWpC0XkItr0VxZPALgz67xuaRmr_Gx0eGMAhH3CkP6Wdjin__fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kwmaJZod0M2io8Xu1Giz2ikVS3NpilprwHGe5QXHPxHEfuGJPOAZGt_CgEn_jPgITteKnSAIObr7eeDpPheZI6ihwb3EpsSA5Jfvi48ZBnCtJjdQKzTT8DodfWo3uhpKbqogGeCy0qc7bzRQp-6UMpnj45_XID7oXbCmFJzgff8FgWnmzX2tO0w0CZJc5adOH17qPLw6J2abNN1wwPTnvwdjJyZRgVghe72Z86VBeqc4tQp8schkyvXyiKdMQgRpLjsy-2DYGwlgkMFRIxuOqNvMlqjRWKIUQgv3A527gH-rCJfWCEaWPiq9i0ukJxlAx_wKTtGCD29z9bvQ4TiZ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFLL5WWovwh0cAKU_1cd-KA6w2Pr5ArPCIRax1t2DvC12Y2VYuys802HMO1fSJPobp_uvO4PEoxAHuGUpoZqKw2ukFljTd8D3GfXH9fOlvVTtri4Msk3TbrgX7hJX3OMK3FE58oPZA8yr2OafnCFYtPOl22_iMHRt_pdSSC4aBo3X5OBajKLogGpQeUdCt6cgoIqRUOs38EZev3Nk6wlxgLkzeJsiuqd_WNpxlH313drW1JWxRC-MKRhuQtULL4qyf31XUqL0fGs3IvLE20NOroI1t1zI4r6SVn16TfVonYl49kzrS4OJ_1j3WJVwedfLMvPx0GtKSoWLF6EY-Llpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ورزش نکردن فقط فرم بدنت رو تغییر نمی‌ده؛ بدن از درون هم تاوانش رو می‌ده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/695883" target="_blank">📅 20:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695882">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
بررسی دمای مسافران در روسیه برای شناسایی بیماران احتمالی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/695882" target="_blank">📅 20:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695881">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmKYvi27hGu1X2icHcD1r10uZ2XZjWS6_GTTvyPhC9QDvqDdDCkAJ68hNp2ri7bMXA1GMLHNg7cTBTY-zKBrzQwwPjFYerz3JFX_6OlVl18yO20ycqqfgmzRgKqu2AJhwrkxzkfu4yQzYadj-O_aZIWB_DRlqSNTrIRY5QykA_YoJp5wIUmzwEl-sLFQaa3c3zKxP6Thzi06pbMSnAIb94uqW9sRwnwZ1zFD2SZBncdxY865s1Ojnpb4-Mdane_GQvYBj8phuiImhsaVJFxIzdCON3GFccONBhe3ZPzRM_jqVQhoxAPWC7OSV5TPvwqAUOg1QJptlWl67nlOws_wiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کابینه تکانی
🔹
کابینه دولت چهاردهم در آستانه یک تغییر جدی قرار گرفته است؛ تغییراتی که پس از استعفای وزیر نفت، شهادت وزرای دفاع و اطلاعات و مطرح‌شدن استیضاح برخی وزرا، ضرورت بازنگری در ترکیب کابینه را بیش از گذشته نمایان کرده است. حالا پزشکیان با فرصتی برای اصلاح تیم دولت روبه‌روست؛ فرصتی که می‌تواند با کنار گذاشتن وزرای ناکارآمد و انتخاب مدیرانی توانمندتر، به جای آنکه تغییرات را به مطالبه و فشار مجلس واگذار کند، خودش آغازگر یک خانه‌تکانی جدی در کابینه باشد.
🔹
هشتصدوهفتادوهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/695881" target="_blank">📅 20:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695880">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
احراز هویت تصویری کاربران حقیقی ایرانی الزامی شد
مرکز ثبت دامنه‌های اینترنتی ‎.ir و دات ایران:
🔹
احراز هویت تصویری سطح ۲ برای کاربران حقیقی ایرانی الزامی شده و ارائه خدمات تنها به کاربرانی که این مرحله را تکمیل کنند، انجام می‌شود.
🔹
تکمیل‌ نکردن این فرایند، موجب محدودیت در دریافت خدمات خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/695880" target="_blank">📅 20:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695879">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StlaJMHWaCOJBbInB8Vm2jnjomXIASGGbHPbA8DWagFuJwVfnyeen-K8peRg8nrNBCkAB4uoeGoIo47bVMl3P1H_VE8BhSVcqPqFQK0HgcS3arvFkPumYuh8DveqV1usvCZgSKhjee-s1kqy1Jljyox5gtwgG4IEDusYy4a7Sk_AHBQjSAntZysEobo92qjubNl_X3GuChcvKK3UazNpUbYynuKImN2VfDhiGX_GkbgH2W8xb1389S5thS04lczTQQKIda3P9DuVKFj-bcG6jctghx3HStu6clSTzy6vmOWj9J_QZFpvUWLem_iFYCj9t2kPaM1MHHKMdTsOfzckgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهانه تراشی تازه ترامپ برای توجیه قیمت بالای سوخت
ترامپ:
🔹
دیگر تنگه هرمز قیمت بنزین را بالا نمی‌برد. حملات اوکراین به پالایشگاه‌های روسیه باعت افزایش قیمت بنزین شده‌است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/695879" target="_blank">📅 20:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695878">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">22-2 Ane Manaee (1404-02-09)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/695878" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌ودوم؛ بخش دوم
🔹
در ادعا تابع، در عمل منافق! نحوه مواجهه برخی با مذاکرات برجام و توصیه‌های رهبری [00:00]
🔹
وقاحت سیاسی برخی افراد در پذیرش عدالت و قضاوت، و استانداردهای دوگانه آنان در مواجهه با نتایج انتخابات‌ [12:44]
🔹
معیار "بستگی دارد" در برخورد با مسایل سیاسی، اجتماعی و دینی، ‌نشانه بیماری قلب، تردید یا ترس از عدالت الهی است. [19:39]
🔹
وقتی ملاک منفعت است، نه حقیقت! نقد و بررسی استانداردهای دوگانه در عرصه‌های مختلف سیاست داخلی و خارجی [23:49]
🔹
برخورد دوگانه دنیا در مواجهه با تروریسم، دموکراسی و حقوق بشر در مقایسه با رأفت حکیمانه اسلامی رهبری [32:53]
🔹
تدبر در قرآن، نه‌تنها تشخیص‌دهنده بیماری دل بلکه درمانگر حقیقی بیماردلان است[37:30]
🔹
تدبر، سفریست پله‌پله، از ابهام به وضوح، از تردید به تسلیم و تفکیک میان اهل هدایت و اهل ارتداد [45:11]
🔹
فهمِ مکانیسم "تزیین سوء عمل" و "تکفیر سیئات"، آغاز هدایت، ولایت الهی، و باز شدن قفل دل‌هاست  [48:23]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/695878" target="_blank">📅 20:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695877">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaab9ac46.mp4?token=IsZ5tzvVIaAVSNblrGVdWfVDsp8OlP0yi30NnTelUTTG7SLl0dPtvTKSclpFj3YC_bhTfgwi0UZxlhkrmjiAtlJZwS-XWjekc0jxsgDtiWEnc5Nz01vXQytV1oBdtScmZuwoBLc81n2j0uBGauRXyF_W2gYb3g-MUmEef8Ps-rUZqZ0fRK4o5FuMMwNy5IiaCiWzXxkzRnz2L35P4HR_y_fVTiArWP8tht_zxlZXcnD9sl5DdBb3XCIkfBmXfP-cQbKwAoMy4fTTJCLYzqmnVCH9z3WIWsuLjS_kyrWXhAC2yrL9dEWhaW7a1HMUUN4AxWV-dQ9ucogQ_Zoa0q-ryUb1DBc42erXfqYGlgiKCVV1907XuqtfMQqsbxULwlFeViCl41rZR_y-DrA_ExSmmIb1chTfgC3o8Q_JHvmfp5SUd2JdV9OuVXgjcv-volk9i9c2ZahY7tYROeU-E9toTrHBP4dX4U3buS1aR_uaO1vHBmCAZj1MAW1l73UJ5sJq1iZi-p2rt8-SVhXU9czy26uyN21k-ZNKUn3XswSRGMuMymFX4AVcLXmevsI_hQH9-kgTrB9rOnsgPtw6eFhgAVpKu5GE-6hJjzfcZCl4N7YbCqla_9c_TFVVig0YmeeRoBAnvqbijOp_mDTpTXpNfUOCg1jGSzSvDH9MEyEExMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaab9ac46.mp4?token=IsZ5tzvVIaAVSNblrGVdWfVDsp8OlP0yi30NnTelUTTG7SLl0dPtvTKSclpFj3YC_bhTfgwi0UZxlhkrmjiAtlJZwS-XWjekc0jxsgDtiWEnc5Nz01vXQytV1oBdtScmZuwoBLc81n2j0uBGauRXyF_W2gYb3g-MUmEef8Ps-rUZqZ0fRK4o5FuMMwNy5IiaCiWzXxkzRnz2L35P4HR_y_fVTiArWP8tht_zxlZXcnD9sl5DdBb3XCIkfBmXfP-cQbKwAoMy4fTTJCLYzqmnVCH9z3WIWsuLjS_kyrWXhAC2yrL9dEWhaW7a1HMUUN4AxWV-dQ9ucogQ_Zoa0q-ryUb1DBc42erXfqYGlgiKCVV1907XuqtfMQqsbxULwlFeViCl41rZR_y-DrA_ExSmmIb1chTfgC3o8Q_JHvmfp5SUd2JdV9OuVXgjcv-volk9i9c2ZahY7tYROeU-E9toTrHBP4dX4U3buS1aR_uaO1vHBmCAZj1MAW1l73UJ5sJq1iZi-p2rt8-SVhXU9czy26uyN21k-ZNKUn3XswSRGMuMymFX4AVcLXmevsI_hQH9-kgTrB9rOnsgPtw6eFhgAVpKu5GE-6hJjzfcZCl4N7YbCqla_9c_TFVVig0YmeeRoBAnvqbijOp_mDTpTXpNfUOCg1jGSzSvDH9MEyEExMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنج ترفند کاربردی رانندگی که مطمئنم به کارت میاد #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/695877" target="_blank">📅 20:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695876">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_z391mofX5CgoJ5sUL6s1-YQbugIxvc1O3tdkxBPnYKJMEu07Cd6uP0cHRxQvv7RwGNaUqfws_9IsdgitkQTb6IWJYBrlAZYvFiyPovLcg4sFdGUBVZIS5jzqDwHAS6K8Q2xD7ZJlVeG7X7koTTrnbGoFgPnE3XHjHgO8YRw7JHMQOsiniV-iD7ok04OkQhtf3X9wof4k4CX1z-RIciURkBA6SF2VuKasy1IeKNdF-fJeR7bjwVg1rw-k77DBxWgZrCaTirhWb7Nj7039BTyaSnKNkB4mG0TUg3l_K8OqYPerNMF8HK1CUU4VDdRu5e0w3mTen2jiqbLpLETj8bHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از یک نئوبانک تا یک اکوسیستم مالی
بانکداری دیجیتال دیگر فقط به افتتاح حساب و دریافت کارت محدود نیست. کاربران امروز یک تجربه مالی ساده، یکپارچه و متنوع می‌خواهند.
بلو از آغازگران این تجربه تازه در ایران بوده؛ مسیری که حالا سایر رقبای نئوبانکی هم در حال حرکت به سمت آن هستند.
به نظر می‌رسد رقابت آینده دیگر بر سر «خدمات آنلاین» نیست؛ بلکه بر سر ساختن یک
تجربه مالی کامل و یکپارچه
است.
مطالعه خبر:
https://www.khabarfoori.com/fa/tiny/news-3250214
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/695876" target="_blank">📅 20:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695875">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4_628VDq3Pay9wNuzUiU1agQ0hSHEp1MU5msY-HIyPhkoqo2YJLT9G-REtp3eSsJy5Xug1RZf60vvm_4xJ-ygRyZtpj5D9U8m8Y4Y7k9MdNqbfPfXypvr7L-a710Ec-Uqcu9fcxBG-p5dS5opXnBOO0s7ulIBoj746cTJPLFK0gzbbIizZ3z3VuegfATJ966zkoOTrKLJDkJJ9p9MqMGbZ4ZNAeJCmWDpeP0OB8dlBiCO89VPlYuLWeRHXJ-BbrtvJaQsq6SM9W-02p_D7n63v9E_ZPHQHJGzSyQhhnmLvG02sVmPTxUrICvTxY3HM1nataPRniHpMpRKIBQiwp1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«کاپشن امسالتو ۴ قسطه بخر!»
❄️
🏔
با شروع فصل سرما، یه کاپشن گرم، سبک و شیک حرف اول رو تو استایل زمستونی می‌زنه!
🧥
کاپشن مردانه مشکی مدل Hamto
▫️
طراحی مدرن، بادگیر و فوق‌العاده گرم
▫️
تن‌خور عالی و دوخت تمیز
▫️
رنگ مشکی مات همه‌پسند و مناسب استفاده روزمره و سفر
💳
شرایط خرید آسان و مطمئن:
•
خرید نقدی:
۲,۳۸۰,۰۰۰ تومان (
با قابلیت پرداخت درب منزل
)
•
خرید اقساطی:
۴ قسط ۶۶۰ هزار تومانی (بدون معطلی و بدون ضامن)
🚚
ارسال فوری به سراسر کشور
📥
جهت ثبت سفارش و کسب اطلاعات اقدام کنید.
https://memarket24.ir/product/fast/64834/180124/
خرید قسطی
👇
https://memarket24.ir/product/brief/64834/180124/</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/695875" target="_blank">📅 20:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695874">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
اسرائیل هیوم: ایالات متحده به اسرائیل مجوز حمله به گروه‌های شبه‌نظامی مورد حمایت ایران در عراق را صادر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/695874" target="_blank">📅 19:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695873">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
روایت کارشناس مسائل نظامی از ورود امارات در کنار موساد، برای کمک به گروهک‌های تروریستی در جنوب‌شرق کشور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/695873" target="_blank">📅 19:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695872">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای
مقام آمریکایی: در حال تشدید محاصره ایران هستیم
یک مقام آمریکایی در گفتگو با الجزیره:
🔹
نیروهای ما از اواسط ماه ژوئیه، در چارچوب محاصره بنادر ایران، مسیر ۱۳۰ کشتی را تغییر داده‌اند.
🔹
ما در حال تشدید محاصره ایران هستیم که از نظر اقتصادی دچار مشکل شده است و سنگینی فشار ما را که ادامه خواهد داشت، احساس می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/695872" target="_blank">📅 19:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695871">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900a6d1b76.mp4?token=t3IetlMjaLJTp31wnz46W8oUswDv94gQLZutPLI6UzyKxlXjMZajEzbV0aaN1uKyXwI0jsSTOUvGh2a5yYGGzJL2Y7cQZnELTxN0jkzaEFhM5yeUUe5L8md5u2PivNc1_eCU1K-tfmcC3GBZcl9yuXrUqOvWrgD8vv6YX1w48rW3qhOrDec34rGUeAA3SbFspAJCL0HG-h-pyiENOuILyODlyN4EiEfqRVBe2zVelrGL5ebmTnqFBBYcKuePEdUFv_UWSxsA5hNrei18JQXxm_G1ttg2qm_R8juBZ4qwp6LJwPCkVawxovSK1X74JFrfHzS83m1YY8ZlXp-DFKGTzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900a6d1b76.mp4?token=t3IetlMjaLJTp31wnz46W8oUswDv94gQLZutPLI6UzyKxlXjMZajEzbV0aaN1uKyXwI0jsSTOUvGh2a5yYGGzJL2Y7cQZnELTxN0jkzaEFhM5yeUUe5L8md5u2PivNc1_eCU1K-tfmcC3GBZcl9yuXrUqOvWrgD8vv6YX1w48rW3qhOrDec34rGUeAA3SbFspAJCL0HG-h-pyiENOuILyODlyN4EiEfqRVBe2zVelrGL5ebmTnqFBBYcKuePEdUFv_UWSxsA5hNrei18JQXxm_G1ttg2qm_R8juBZ4qwp6LJwPCkVawxovSK1X74JFrfHzS83m1YY8ZlXp-DFKGTzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نشت عفونت ناشناخته از آزمایشگاه طاعون روسیه/ ۲۰۰ نفر قرنطینه شدند
🔹
یک کارمند ۲۸ ساله آزمایشگاه ضدطاعون روسیه پس از شکستن تصادفی لوله آزمایش حاوی نمونه زیستی، به ذات‌الریه ناشناخته مبتلا شده و جان باخته است. حدود ۲۰۰ نفر قرنطینه شده‌اند و احتمال طاعون ریوی…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/695871" target="_blank">📅 19:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695870">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
یکی دیگر از افشاگران پرونده اپستین جان باخت؛ او نخستین مورد نیست
🔹
سایمون آندریس (Simon Andriesz) از مراودات تجاری میان هاوارد لاتنیک و جفری اپستین پرده برداشته بود. او نخستین فرد مرتبط با پرونده‌های اپستین نیست که از زمان علنی شدن این ماجرا جان خود را از دست می‌دهد و خبر مرگش با ادعای خودکشی منتشر می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/695870" target="_blank">📅 19:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695869">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYBaFnUcry70dUw3LfNk_8wu7euiZbHOVCPXBNQzV40cu43DkSNLGdyp-Av1nYnCULsYAyWDNl0GtUTiKZ6zZVjFVwhJOEGYPCM4ZSSzZaFccLkUj74B470MIKOMpz3yva6PgDb7FmM6CvDpY8uZkRLOjCGsOaSS5zT7pJmprWiaE9iH70pMO5IQVf2DAkq_ZckMCIPD1s5m67tlh0F1RpcysLmpEneHx8qQ_PNBdFfiwxVvPP-sxuh5-iElkrei2gFdT2tAc7VYtUfbKM8tZmx_uxvBejR411QP18YjYo1p3yAmv470HN6gKwNekJVVZiTGIO8PmuleRev2pi6ZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر سوئدی: اطلاعیه تحریم‌های آمریکا نشان می‌دهد که ایران همچنان برای عبور از تنگه‌هرمز حق حفاظت (پول جهت حفاظت از کشتی‌ها) دریافت می‌کند؛ موضوعی که به نوبه خود می‌تواند نشان دهد یکی از دلایل افزایش جریان صادرات نفت از خلیج فارس این است که بخشی از انتقال‌ها و جابه‌جایی‌های نفتی با شرایط موردنظر ایران انجام می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/695869" target="_blank">📅 19:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695867">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آموزش و پرورش مجازی شدن مدارس از ۱۵ آبان را تکذیب کرد
مصطفی آذرکیش، معاون آموزش متوسطه وزارت آموزش و پرورش در
#گفتگو
با خبرفوری:
🔹
درحال‌حاضر هیچ بحثی درباره تعطیلی یا مجازی‌شدن مدارس از تاریخ مشخصی مانند ۱۵ آبان مطرح نیست و برنامه‌های آموزش و پرورش بر آموزش حضوری در تمام طول سال تحصیلی متمرکز است.
🔹
در صورت ایجاد شرایطی که نیاز به تعطیلی یا تغییر شیوه آموزش داشته باشد، موضوع به‌صورت رسمی اطلاع‌رسانی خواهد شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/695867" target="_blank">📅 19:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695865">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a06532b0.mp4?token=XROFzRmVSuIeOgEWKQE4k0MkXfKG12zUYPBKbokkZtGzQtF7URjW2MWDih6f641tn6mvIbnlhm7KTltkgcOyULqfLWcZ6SFAY6eex-vNjMmxVuN1B118wrIabr-K9tazEAkdES47QPqZhaHlWbB8oTP2lEr5rLYg9tu5LMRZegG0eiJDO_KxDGl1uV0RGCUlBqtwdM830ggiT5CVB73-7mVrkzNsKZu3mrvZlvjRPSBI5WGeCF3Kriv6E7S7rM5zmoaxZ_9MPyJO-MZQlRWMzb5axM_toxXnLcGqPU_Qo1JMoW0BZJ4JMS674-qHd8tHCroPJn53O-wzli9HK3okhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a06532b0.mp4?token=XROFzRmVSuIeOgEWKQE4k0MkXfKG12zUYPBKbokkZtGzQtF7URjW2MWDih6f641tn6mvIbnlhm7KTltkgcOyULqfLWcZ6SFAY6eex-vNjMmxVuN1B118wrIabr-K9tazEAkdES47QPqZhaHlWbB8oTP2lEr5rLYg9tu5LMRZegG0eiJDO_KxDGl1uV0RGCUlBqtwdM830ggiT5CVB73-7mVrkzNsKZu3mrvZlvjRPSBI5WGeCF3Kriv6E7S7rM5zmoaxZ_9MPyJO-MZQlRWMzb5axM_toxXnLcGqPU_Qo1JMoW0BZJ4JMS674-qHd8tHCroPJn53O-wzli9HK3okhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سه ترفند کاربردی برای کاربران گوشی‌های شیائومی
🤳🏻
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/695865" target="_blank">📅 19:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695864">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
اعلام قیمت خودرو در بازار متوقف شد
🔹
پلتفرم‌های خودرویی در اطلاعیه مشترک اعلام کردند با توجه به شرایط هیجانی و نوسانات فعلی بازار، موقتاً امکان به‌روزرسانی قیمت خودروها وجود ندارد. به‌محض ایجاد ثبات در بازار و روند کاهشی قیمت‌ها یا رسیدن به یک تعادل نسبی، قیمت‌ها مجدداً به‌روزرسانی خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/695864" target="_blank">📅 19:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695863">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwjpQf7qVKGt12Hb5Hv2ipAQcWHmqiu1gzddrgkE92VRNZxq7vNbSC0TbvIZ0nkEKaM2khRk8vY6glFV0DWq2s96pMu5FSX3PMxlhnc12k2K31txyBiTFX7WJbjeP6LCyEl9s8oLc5QCLYXNjV3W4IEic9dUQ12dBbz6eF6GfDJHB4zxyy2PqJ7dCM64HQozeG3K7kZoDywGnRv0gTKp6Asa4TfMLtwhHCSnlrI5-fFoA1nHCwNhC_XJLy9KNofyOg6IPNSsK_KO0tgWO7VZqZijB7TdsC32W_k7sdVn-RBrvoLuGFFJboDjqQy1cWQC2iy3jK5yTcUEs3JDEfN1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجری: آیا این یک دیدگاه یهودی است که بخواهیم کل غزه را نابود کنیم و کرانه باختری را به اسرائیل ضمیمه کنیم؟
موشه فیگلین، سیاستمدار راست‌گرای افراطی اسرائیلی و رهبر پیشین حزب زیهوت:
🔹
صددرصد. تمام عرب‌های ساکن غزه، حتی نوزادان، دشمن محسوب می‌شوند و دشمن فقط حماس نیست.
🔹
هر کودک، هر نوزاد در غزه دشمن است؛ دشمن حماس نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/695863" target="_blank">📅 19:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695862">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCs_YhvjrAYwPY6tiH8g_d59SBZLRnj2f7sCero6p9VPzeIQ2EIdijBUVtK7t2MAMvK12CAoXklodmwj-HyWU1Jmfnca8N2LW8JOH2bOomgRInt-9DW-ehWLhFhElMuwddM2IpMbuEYIc_Lquc8lMa127awp9WiXQr5lzvwgIFn3N0b9ZE1UHtdM-Ln7EMwDvasoq8A74QPRDyTxz1vBzR7Ft09g1Uaq71n0Kw1R_Qg-BECujC2LETKW62Pxpw6x9PD0ouNUi4LrNIhVFWvbr2mdKDcUZQPhtoybpwgjuUQG82VlJEi5CBndsLiwcB9kK_VdZTqa8eAnkBEgpdxQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبر خوب برای حقوق‌بگیران: اضافه‌ برداشتِ مالیاتی، عودت داده می‌شود
🔹
رئیس کل سازمان امور مالیاتی نحوه استرداد اضافه برداشت مالیات بر حقوق را به ادارات کل امور مالیاتی ابلاغ کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/695862" target="_blank">📅 19:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695861">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28eb7e86ae.mp4?token=Jdy-FQrR5IW4c0I_aF_fCO4vMmVyEzqUcqFjVKXFVyxGsuDcS4Wesn1__-l5JCeEBbH_V1CQ5VYe78rWrI9wyxhVzIaRsOnnzHa3cw54ktfnSkkIBuK9WXjZxTxMhzl2MI89v0MOZ3R59yfXkw-nwofppojJ6iHuEj5EXYTClSfLlO7Dg_0MMiQVYxYbHtRDY5ktGC30ACtJIgXIwF61kaFe18WQx523Fts2H5QtmvbJHVbnincMoBdsaY_ILvt-YbmWB135TQuGSaHj4jbpUjh-pnc9I53QEYs9Lg4U_4xqpd6EV9yjxiiaCFqRPUsfUuOgP9WH0opstExbYX7mLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28eb7e86ae.mp4?token=Jdy-FQrR5IW4c0I_aF_fCO4vMmVyEzqUcqFjVKXFVyxGsuDcS4Wesn1__-l5JCeEBbH_V1CQ5VYe78rWrI9wyxhVzIaRsOnnzHa3cw54ktfnSkkIBuK9WXjZxTxMhzl2MI89v0MOZ3R59yfXkw-nwofppojJ6iHuEj5EXYTClSfLlO7Dg_0MMiQVYxYbHtRDY5ktGC30ACtJIgXIwF61kaFe18WQx523Fts2H5QtmvbJHVbnincMoBdsaY_ILvt-YbmWB135TQuGSaHj4jbpUjh-pnc9I53QEYs9Lg4U_4xqpd6EV9yjxiiaCFqRPUsfUuOgP9WH0opstExbYX7mLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ونس: ما با اطمینان نسبی معتقدیم که ایران در تلاش است تا همان کاری را انجام دهد که دولت ایران در طول ۴۹ سال گذشته انجام داده است، یعنی اقدام به اعمال تروریستی علیه ایالات متحده و همچنین علیه بسیاری از افراد دیگر. ما بسیار محتاطانه عمل می‌کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/695861" target="_blank">📅 19:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695860">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aa41670cd.mp4?token=B5X73SarV1whl5ETtIK0ODG4Kheodcw750KqyEf4aKBYYV63UxBvfvIuRnIlyqPms70S2vB7P4icXDt-n78wHVkxAD615IJJDxlXHoqe1spbpzYuLKTdLoCGCiit54M6Nfd3V4cVzdevMx3pBQp1vqKKT7QayJW_x5LIIByBqAx7brVu3iDOCOeckVQ1n6bRQb5ZW9-XMJU8bzTVMAxrZUmGbfEYZ0fQNBoWLtronj1_LNhbBKYePN4AFIsGPbt0GiVLNS6H8nMJCO01JYCqiXcCYQmoVuXXeZhMsN-u4vKfXsuQFUg3RGneiR-oRZv6oNo16cK-EoCr3MxNhomRbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aa41670cd.mp4?token=B5X73SarV1whl5ETtIK0ODG4Kheodcw750KqyEf4aKBYYV63UxBvfvIuRnIlyqPms70S2vB7P4icXDt-n78wHVkxAD615IJJDxlXHoqe1spbpzYuLKTdLoCGCiit54M6Nfd3V4cVzdevMx3pBQp1vqKKT7QayJW_x5LIIByBqAx7brVu3iDOCOeckVQ1n6bRQb5ZW9-XMJU8bzTVMAxrZUmGbfEYZ0fQNBoWLtronj1_LNhbBKYePN4AFIsGPbt0GiVLNS6H8nMJCO01JYCqiXcCYQmoVuXXeZhMsN-u4vKfXsuQFUg3RGneiR-oRZv6oNo16cK-EoCr3MxNhomRbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین از نمونه‌هایی از «سلاح گوشه‌زن» برای استفاده نیروهای پلیس و یگان‌های ویژه رونمایی کرد. این سامانه امکان درگیری مسلحانه از پشت گوشه دیوار را فراهم می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/695860" target="_blank">📅 19:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695859">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ناو هواپیمابر جورج بوش پس از ۶ ماه حضور در خاورمیانه در تایلند پهلو گرفت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/695859" target="_blank">📅 19:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695857">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c2d0ed10.mp4?token=MQeC0xds2f0FU4FyO7D6mV95MSRMDhx1elz-NboVIC3IfVonTpYwiFgck64fNtoi9bBz4TrvnDc7gVHrgYtyNOJjIRL_8Se7XPApbKCurgIj6jLfw7UADYn6jzvU2e1tpHLlGpUUPr2CO8ewmtJGAnoqh_hTgqBFLgBhNcvh3IaMlcQ9SEeT7Fdzb2Y9LStZoz19806BZEYJEj-Lchdni4ZD7rXq1VXH5jLNgit51gge3xki0Cu5UiclzqPP1ra3liYTPEqlN09ah-0WWKqsmQp941HjQWxQ0XMUQbUsp6Io-6vpf6io-PnH_xO0AR16m3_342PWRFzmtfqOzedARG3vONwHdSb87V0IbsukVaEmGhiowK61yo4luaGY2Q7U06DDmnIboEKPodzMu3B7r7wBj9vuWGJLCeKcA0lsxpJKGt_3Eyq47MMikzha6FV_ulJZbRIuKSUnlURg8pQsNCNrjMXuWawolWa5Clo80fqsk6RmEMlnWWeYCOSsKJSYzop-dJGuedHQS_JKz5_SMGONAZbvUXc4Yow1Nf5M0iCZneDeOQtf9kMnTQ1qY9-yXbGwht_LVqaN9b90stgE5_9z4MKDVqlMrMBbuMS6PAVSwV5KyQLZMK0G3nz48kDWtJfqk4jRP_MasKINTeh2hU3DJc3yB4_PnRCSxwQdq9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c2d0ed10.mp4?token=MQeC0xds2f0FU4FyO7D6mV95MSRMDhx1elz-NboVIC3IfVonTpYwiFgck64fNtoi9bBz4TrvnDc7gVHrgYtyNOJjIRL_8Se7XPApbKCurgIj6jLfw7UADYn6jzvU2e1tpHLlGpUUPr2CO8ewmtJGAnoqh_hTgqBFLgBhNcvh3IaMlcQ9SEeT7Fdzb2Y9LStZoz19806BZEYJEj-Lchdni4ZD7rXq1VXH5jLNgit51gge3xki0Cu5UiclzqPP1ra3liYTPEqlN09ah-0WWKqsmQp941HjQWxQ0XMUQbUsp6Io-6vpf6io-PnH_xO0AR16m3_342PWRFzmtfqOzedARG3vONwHdSb87V0IbsukVaEmGhiowK61yo4luaGY2Q7U06DDmnIboEKPodzMu3B7r7wBj9vuWGJLCeKcA0lsxpJKGt_3Eyq47MMikzha6FV_ulJZbRIuKSUnlURg8pQsNCNrjMXuWawolWa5Clo80fqsk6RmEMlnWWeYCOSsKJSYzop-dJGuedHQS_JKz5_SMGONAZbvUXc4Yow1Nf5M0iCZneDeOQtf9kMnTQ1qY9-yXbGwht_LVqaN9b90stgE5_9z4MKDVqlMrMBbuMS6PAVSwV5KyQLZMK0G3nz48kDWtJfqk4jRP_MasKINTeh2hU3DJc3yB4_PnRCSxwQdq9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت انتخابات اسرائیل؛ نتانیاهو دوباره با ایران می‌جنگد؟
🔹
خیلی‌ها می‌گن تنش بعدی ایران و اسرائیل، فقط به تصمیم تهران و تل‌آویو بستگی نداره و یک عامل مهم دیگه هم وسطه و اون، انتخابات اسرائیله. حتی بعضی‌ها یک ادعای جنجالی‌تر دارن و می‌گن نتانیاهو برای اینکه دوباره رأی بیاره، به یک حمله دیگه به ایران نیاز داره، اما واقعاً همین‌طوره؟
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/695857" target="_blank">📅 18:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695856">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0b30fdb18.mp4?token=NeZGfoe8q9Bpj4m0PT-p1DXAhDPvgA30Z4TYnrQcANiObD0dUZdF-h8uRlB0Uxl9F8JlRn-StHPuhVkC2y-vdzdAt3Ff1VMSI-Ooe797Jr_nyXcHTNwQtjgvpbkZ6J216_8Qc5Rt33vNZBgdc6GQSBfLH39LuOr2Twyoc_urs8MF2QRHZ61z8cWdJtuEODmltxfyhPYwO4UlZnPhMmIkltjSdmr1_Y0s3A9crHI5lWVQ95py-pWwmG9PwRcbwWTO_Tmecunt0UKtXgQJS4OupfMx6gH-_Ah0EqVCS73gd-dvIrkmXRnqUFz5uJ2tmpxvGgx5VPl99sMwqxnctS8kOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0b30fdb18.mp4?token=NeZGfoe8q9Bpj4m0PT-p1DXAhDPvgA30Z4TYnrQcANiObD0dUZdF-h8uRlB0Uxl9F8JlRn-StHPuhVkC2y-vdzdAt3Ff1VMSI-Ooe797Jr_nyXcHTNwQtjgvpbkZ6J216_8Qc5Rt33vNZBgdc6GQSBfLH39LuOr2Twyoc_urs8MF2QRHZ61z8cWdJtuEODmltxfyhPYwO4UlZnPhMmIkltjSdmr1_Y0s3A9crHI5lWVQ95py-pWwmG9PwRcbwWTO_Tmecunt0UKtXgQJS4OupfMx6gH-_Ah0EqVCS73gd-dvIrkmXRnqUFz5uJ2tmpxvGgx5VPl99sMwqxnctS8kOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظر توریست چینی در مورد جشنواره فیلم‌های کودکان و نوجوانان اصفهان در خیابان چهارباغ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/695856" target="_blank">📅 18:58 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
