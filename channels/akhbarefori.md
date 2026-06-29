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
<img src="https://cdn4.telesco.pe/file/HtnMrrJ1lQeqaBJfVORtEqAYD1FzMl5-eR46MYMvY2NoziFLXbZyteJ5aV3F6m7RWX99xkXjAlMzccdjhd3sOiNZmaSezJDjku012F-lBnqk216XSOWqECb-N8-6Fla_3b0ybkf1TksxBx_PzePtgo08ACORPe3bn-VRZ_99DqvuxbSRUUvrVM6bztzx-pev0a9VBcaSuIYYqbCIUHzrNeRpRfoHhnuxPwz4tuOhR11v1dMHOOSsvEtIfY61rcHxzjcLbMYhNH15tO0MaMjgoHDn74zhdts16ihTwN4W6G2TqZ4EpQ8MGocn-dKt1-hQjsVH65wLeCGQsnTbH6yUcQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.19M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 22:51:11</div>
<hr>

<div class="tg-post" id="msg-664714">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
سردار حسن‌زاده: امکان ورود ساک یا کوله‌پشتی یا وسایل حجیم به داخل مصلی برای مراسم وداع با رهبر شهید وجود ندارد #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/664714" target="_blank">📅 22:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664713">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
برنامه‌ریزی مجلس برای استیضاح وزیر نیرو
امید نصیبی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
قطعا مجلس برای استیضاح برخی وزرا برنامه دارد و یکی از آن‌ها وزیر نیرو است و توازن و عدالت در برنامه وزیر نیرو رعایت نمی‌شود.
🔹
عملکرد منفی وزارت نیرو در بحث سد پارسیان موجب بدبینی بعضی افراد نسبت به نظام و عصبانیت مردم شده است.
🔹
علت به تاخیر افتادن استیضاح وزیر نیرو این است که باتوجه به حضور او در کمیسیون‌ها مشکلات برخی نمایندگان حل شده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 11 · <a href="https://t.me/akhbarefori/664713" target="_blank">📅 22:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664712">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
پزشکیان: برخلاف برخی ادعاها، در مذاکرات هیچ امتیازی خارج از چارچوب منافع کشور واگذار نشده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/akhbarefori/664712" target="_blank">📅 22:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664711">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9UFeAmNtze_H6sEv2W6STch3QroMxowRQ1EIg5hiqkIL1XOuJOFRhL_x_3VASH8t-w0FXCDswmYin62A5NkyH9ZC7gcnSTE3pNfsHyXPisOGmPHDetTUw0DVB21JjqFxpnXuWQEC1JGR5msd74ps06iFtol3wVhf-H6bINYu6DV7HEZT2A8FwTUKkfvXoN0fr5xKWoS7-v0yWO_vVD-_GJNlDqZnrjDO5aJV5ffcHhptfN5_xC3GZvqAEQ8Xuj5WUa35iSt6oqQI49wI6ZxIKZtHJJXX589A3CkSAnWXZMPAreA1Q7ULPSJHFZn1sf6Bl2hZI9tkPB1i0A025u1tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح جایگاه وداع با رهبر شهید انقلاب منتشر شد
سردار حسن‌زاده:
🔹
طراحی جایگاه وداع با پیکرهای مطهر امام شهید و خانواده شهید ایشان بر مبنای چند محور صورت گرفته است.
🔹
فرایند برگزاری و اقامهٔ نماز نیز در این طراحی دیده  شده است. در واقع، این طرح، طرح وداع و طرح شهادت خانوادگی امام شهید و خانواده‌شان است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/664711" target="_blank">📅 22:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664710">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
بیانیهٔ مشترک عمان و فرانسه: ما بر تعهد خود به منشور ملل متحد، حقوق بین‌الملل و حقوق دریاها تأکید می‌کنیم و بر اهمیت بازگشایی تنگهٔ هرمز پای می‌فشاریم
🔹
بر اهمیت حمایت از کاهش تنش منطقه‌ای، تأمین امنیت راه‌های دریایی و مبارزه با اشاعهٔ سلاح‌های کشتار جمعی تأکید می‌ورزیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/664710" target="_blank">📅 22:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664709">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
پزشکیان: برخلاف برخی ادعاها، در مذاکرات هیچ امتیازی خارج از چارچوب منافع کشور واگذار نشده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/664709" target="_blank">📅 22:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664708">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
کاش پاتل، مدیر اف‌بی‌آی اعلام کرد که از زمان آغاز جام جهانی فوتبال، بیش از ۴۰۰ پهپاد غیرمجاز را نزدیک استادیوم‌ها و سایر اماکن ورزشی رهگیری کرده‌اند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/664708" target="_blank">📅 22:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664707">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
مشاور سابق امنیت ملی آمریکا: کشورهای منطقه دنبال توافق اختصاصی با ایران بر سر تنگهٔ هرمز هستند
🔹
جیک سالیوان در پاسخ به این پرسش که آیا کشورهای منطقه ممکن است دنبال ایجاد چارچوب امنیتی بدون مشارکت آمریکا باشند؛ فکر می‌کنم به‌سرعت درحال نزدیک‌شدن به این نقطه هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/664707" target="_blank">📅 22:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664706">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d91e5c60b.mp4?token=AAfKNzCZB1ggu-UkclPVKgwTxTYJHOaAqnW_UXPI8yjIDaBd2FxWQ8sU1vAcy_kTLCYbhlbgySGyUZgIvDscMaAkQlIrsH255ExbvQSJtRANswQ8IgnmwGXwO6OzACyE_NhqC3sUFH-smoe76_7TN-fpGzciYn0RHEOZuRX1sXOpvxi3WGd26CraG8gngpbQecoTfZ6AfXqlSvvmJm0oEpprCqN9J0tMCeaGhLhQAYTY6PNtYQ93RELVRovZP03a-1-ZUhkKFQXawxkJLYRbm3-BPfBQmJhDZdTA8ogPgRmYKMcm_fn5KKrLDWSKvzf4eh8kx2cqVmUmPdOxY5fqQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d91e5c60b.mp4?token=AAfKNzCZB1ggu-UkclPVKgwTxTYJHOaAqnW_UXPI8yjIDaBd2FxWQ8sU1vAcy_kTLCYbhlbgySGyUZgIvDscMaAkQlIrsH255ExbvQSJtRANswQ8IgnmwGXwO6OzACyE_NhqC3sUFH-smoe76_7TN-fpGzciYn0RHEOZuRX1sXOpvxi3WGd26CraG8gngpbQecoTfZ6AfXqlSvvmJm0oEpprCqN9J0tMCeaGhLhQAYTY6PNtYQ93RELVRovZP03a-1-ZUhkKFQXawxkJLYRbm3-BPfBQmJhDZdTA8ogPgRmYKMcm_fn5KKrLDWSKvzf4eh8kx2cqVmUmPdOxY5fqQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انار خرمایی
😳
🔹
میوه‌ای عجیب و جالب در بنگلادش که شبیه انار است که داخلش خرما است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/664706" target="_blank">📅 22:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664705">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70eb4993d7.mp4?token=LsjZ4aReEMFkG04sIQK23M5yQN7dojbXwhhx6zyG-BQcaIzg3yibhL6qZD-Z17j-nyvgcmKtk5D49RSOm81_6hLUur0pEd9InzHaUkc66SPSVA6ztn_-ULX-JwUz7vLsHctqlkXOidZ42UUwbnZrPnauCBBziVYo9rwWZt_2ZoH4DM9XXPC3dvABGkK7dpwzgWXKptzt5DDmidStOXQbjD6HvHx_fJeXREH59ctI9lOfv_Iokfpg1XXvfRjWisM_ac5reTXaoMPmSjqtdGL_3RByiSqykxRDsCN_-j-lN4Oehn7-znq84VqM0jL96RdM6E3jAw5SlSexnswh6ObYxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70eb4993d7.mp4?token=LsjZ4aReEMFkG04sIQK23M5yQN7dojbXwhhx6zyG-BQcaIzg3yibhL6qZD-Z17j-nyvgcmKtk5D49RSOm81_6hLUur0pEd9InzHaUkc66SPSVA6ztn_-ULX-JwUz7vLsHctqlkXOidZ42UUwbnZrPnauCBBziVYo9rwWZt_2ZoH4DM9XXPC3dvABGkK7dpwzgWXKptzt5DDmidStOXQbjD6HvHx_fJeXREH59ctI9lOfv_Iokfpg1XXvfRjWisM_ac5reTXaoMPmSjqtdGL_3RByiSqykxRDsCN_-j-lN4Oehn7-znq84VqM0jL96RdM6E3jAw5SlSexnswh6ObYxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیرخلاص برزیل به ژاپن در دقایق پایانی؛ گل دوم برزیل به ژاپن توسط مارتینلی ۶+
۹۰
🇯🇵
1️⃣
🏆
2️⃣
🇧🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/664705" target="_blank">📅 22:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664704">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
غریب آبادی: ایران به هیچ کشوری اجازه نخواهد دارد که در فرآیند مین‌زدایی در تنگه هرمز دخالتی کند و حتی عمان نیز اگر بخواهد این کار را انجام دهد، ما اعلام کردیم که کمکشان خواهیم کرد زیرا مسئولیت جمهوری اسلامی ایران است
🔹
مسیرهای عبور و مرور توسط ایران تعیین…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/664704" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664703">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تلخ اما واقعی، مستمری معلولان حتی به دو میلیون تومان هم نمی‌رسد!
علی جعفری‌آذر، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
با توجه به نیازهای معیشتی و سخت بودن استفاده معلولان از حمل‌ونقل عمومی، پیشنهاد شد، حواله خودرو به معلولین تعلق بگیرد و این امر نیاز به جدیت دولت دارد که تاکنون مغفول مانده‌ است.
🔹
همچنین اعلام شد کمک‌هزینه‌های ۱۰۰ و ۲۰۰ میلیون تومانی مسکن، با توجه به تورم و هزینه‌های زندگی، پاسخگوی نیاز معلولان نیست و برخی ادارات نیز به‌دلیل ناتوانی جسمی افراد در پیگیری امور، حقوق آنان را نادیده می‌گیرند.
🔹
با وجود افزایش مستمری در دو سال اخیر، دریافتی بسیاری از معلولان همچنان به ۲ میلیون تومان هم نمی‌رسد و پاسخگوی هزینه‌های زندگی نیست.
@TV_Fori</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/664703" target="_blank">📅 22:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664702">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
هیات منصفه دادگاه‌های سیاسی و مطبوعاتی، خبرگزاری آنا را مجرم ندانست
🔹
رضا توکلی خبر بیماری‌اش را تکذیب کرد
🔹
سردار حسن‌زاده: پیشنهاد میکنم اگر مردم مسیر طولانی را طی میکنند قبل از ورود به مصلی، در زائرشهرها استراحت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/664702" target="_blank">📅 22:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664701">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa35e724dd.mp4?token=kbajuiQ-6BFO7RZRwvIb6bd8dahwS_3F_yTQhHpufPrvzjaMVQkwMvg3Zn44-9Iw8vWYNfCZttWBKGjztI061e-uKtzCUQPnSRxmx-Y2GUaU092i9_E65gULGRiCtLk2riluHBBLG3Dr8eZFvSiPhNHLZzWIwQ8A05k8m30Lwo4XGVy3rutMV_wv4TxDolEERTfUvQ9XxNIPFcIE1HfYb2Mn9suHW6-DU-1w-oaN1hFI7fQ1JdbXyMJQLdRsMfRdzjJPzFK-rnjmWMzTTY8hjdw-NyIQnnxT7fYqAoPUKBQsZV26Oe2rLfo0VWk4TMk959L1swLyYFBNPHar6sbZSaop1towEOEtCkY9P4jIsGWfGFuIqO0L8J9DSj_b7-D8MZUUAahkGaxBHIp9V3adC-ZY0eze0ozPcmmYRzVKKkfAXihWen5Xbz77si9oYBztPUahIAZgDyj_6Fz9Qh_ginO-NF9tVN-JLhSLt-nInzUXxNXkdaede4O-fUVNwa0T3aubW8Qd18ECxQ8tFO37vBkeBgBMyR1UeFVQ3zSGqDGvDGwZy5jphb2SYbci85-pn2bQkCaBSXH1yElDNPBBPw5CfEkCGGyaJHH1pot14EJN2azLX0se3JZhvOVMjeeTqrzsppYrw-8dn-8F3rkzQMwI020pxWTtbKm6JG6QsX0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa35e724dd.mp4?token=kbajuiQ-6BFO7RZRwvIb6bd8dahwS_3F_yTQhHpufPrvzjaMVQkwMvg3Zn44-9Iw8vWYNfCZttWBKGjztI061e-uKtzCUQPnSRxmx-Y2GUaU092i9_E65gULGRiCtLk2riluHBBLG3Dr8eZFvSiPhNHLZzWIwQ8A05k8m30Lwo4XGVy3rutMV_wv4TxDolEERTfUvQ9XxNIPFcIE1HfYb2Mn9suHW6-DU-1w-oaN1hFI7fQ1JdbXyMJQLdRsMfRdzjJPzFK-rnjmWMzTTY8hjdw-NyIQnnxT7fYqAoPUKBQsZV26Oe2rLfo0VWk4TMk959L1swLyYFBNPHar6sbZSaop1towEOEtCkY9P4jIsGWfGFuIqO0L8J9DSj_b7-D8MZUUAahkGaxBHIp9V3adC-ZY0eze0ozPcmmYRzVKKkfAXihWen5Xbz77si9oYBztPUahIAZgDyj_6Fz9Qh_ginO-NF9tVN-JLhSLt-nInzUXxNXkdaede4O-fUVNwa0T3aubW8Qd18ECxQ8tFO37vBkeBgBMyR1UeFVQ3zSGqDGvDGwZy5jphb2SYbci85-pn2bQkCaBSXH1yElDNPBBPw5CfEkCGGyaJHH1pot14EJN2azLX0se3JZhvOVMjeeTqrzsppYrw-8dn-8F3rkzQMwI020pxWTtbKm6JG6QsX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای درخواست آیت‌الله سیستانی برای برگزاری تشییع پیکر رهبر شهید در عراق
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
استقبال گسترده‌ای از برگزاری این مراسم در عراق صورت گرفته و بیش از یک میلیون نفر برای حضور در آن ثبت‌نام کرده‌اند.
🔹
وی همچنین مدعی شد بر اساس شنیده‌هایش، پیشنهاد آغاز مراسم تشییع از عراق به درخواست آیت‌الله سیستانی مطرح شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/664701" target="_blank">📅 22:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664700">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
تردد کشتی‌ها از تنگه هرمز با وجود نگرانی‌های امنیتی ادامه دارد
‌
آناتولی:
🔹
داده‌های پلتفرم ردیابی دریایی «مارین‌ترافیک» نشان می‌دهد با وجود نگرانی‌های امنیتی ناشی از حملات متقابل میان ایران و آمریکا، تردد کشتی‌ها در تنگه هرمز همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/664700" target="_blank">📅 22:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664699">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
چادرملو برای اولین‌بار به آسیا رفت؛ چادرملو در ضیافت پنالتی‌ها سه‌جانبه را فتح ‌کرد و به لیگ سطح دو آسیا رسید
🔹
چادرملو(۷) ۰ ــ ۰ (۶)گل‌گهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/664699" target="_blank">📅 22:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664698">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozJt6_BjkYhYZCJuZ7mxKYEWDRiYu6ClhMJNP3uWYsuDK7vKCcJHoKfQpF2-FrxvAUFvFvFznfT2M3M33_3FR8R-3rkq-bKvFfBj8jklrLreEvPDED9G9j87akhRKooKKkgLFOmLS732fyqWQQTQyDRHndMlmHcH_oiomH8YKPy5Kgcf71m3eLzubu_kq72CBHSErOu9_eVNUaHz1AcG0JCq6Il3X39CY_2fco6MGVLTB6uWb0-migIm7p8IVuG_V93Z1SY1LgaaPxXVbC0ktU5NIYTZMDOeiokdoyA3l4ugc3VimKY2P5E5wYewETTj4-tMx-VRBydK2HKy3cFA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عدالت برتر است یا بخشش؟
🔹
امام علی(ع) در پاسخ به برتری عدالت یا جود فرمود: عدالت هر چیز را در جای خود می‌نهد و قانونی همگانی است که جامعه را منظم و شکوفا می‌کند؛ اما جود فراتر از استحقاق و محدود به موارد خاص است؛ بنابراین عدالت به‌سبب فراگیری و نظم‌بخشی،…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/664698" target="_blank">📅 22:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664697">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004d499b44.mp4?token=bP3dO2yWrjhIlrrn5oqqXy6llt3nVp5dKhKtsyYYXXWR27BkNxotSM9y5_CNHjKNvFQundVA7PjKTmG1dusoeBVFFgzw4-NmHfwIBnB3UT_gI7-VfSnZXzgaPyMAqBvSMuYtA3cv1OLu9-ucs03DJuwPtc29kj4bR7JgB3Qj20dtn48YRrsiaejRd7-S7smWv6p2iDz0wFtbEG6AZBuaTDe1hLt5a8-e8EVTUJzR56ckyog2dfb1A0-OT4_KvGt53kAS-5ptGNs5hM94XqyGYkc3ZGtzQe_X5pz08esX4dyKtFby-reYzSQPe0r7AoPjoCDnyv0E_nwulLX-_wRW0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004d499b44.mp4?token=bP3dO2yWrjhIlrrn5oqqXy6llt3nVp5dKhKtsyYYXXWR27BkNxotSM9y5_CNHjKNvFQundVA7PjKTmG1dusoeBVFFgzw4-NmHfwIBnB3UT_gI7-VfSnZXzgaPyMAqBvSMuYtA3cv1OLu9-ucs03DJuwPtc29kj4bR7JgB3Qj20dtn48YRrsiaejRd7-S7smWv6p2iDz0wFtbEG6AZBuaTDe1hLt5a8-e8EVTUJzR56ckyog2dfb1A0-OT4_KvGt53kAS-5ptGNs5hM94XqyGYkc3ZGtzQe_X5pz08esX4dyKtFby-reYzSQPe0r7AoPjoCDnyv0E_nwulLX-_wRW0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار حسن‌زاده: امکان ورود ساک یا کوله‌پشتی یا وسایل حجیم به داخل مصلی برای مراسم وداع با رهبر شهید وجود ندارد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/664697" target="_blank">📅 22:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664696">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
نظرسنجی که تن نتانیاهو را لرزاند؛ ۹۲ درصد اسرائیلی‌ها ایران را پیروز جنگ می‌دانند
🔹
نظرسنجی منتشرشده از سوی الجزیره نشان می‌دهد ۹۲ درصد از پاسخ‌دهندگان، ایران را پیروز جنگ اخیر می‌دانند. همچنین ۸۲.۹ درصد معتقدند این جنگ امنیت اسرائیل را تضعیف کرده و ۵۶.۴ درصد عملکرد نظامی اسرائیل را «شکست‌خورده» یا «ضعیف» ارزیابی کرده‌اند. ۷۲.۵ درصد نیز به اظهارات بنیامین نتانیاهو درباره جنگ اعتماد ندارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/664696" target="_blank">📅 22:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664695">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
کرملین: لوکاشنکو هیچ پیامی از سوی زلنسکی به پوتین منتقل نکرده است
سخنگوی دفتر ریاست جمهوری روسیه در بیانیه‌ای اعلام کرد:
🔹
لوکاشنکو رییس جمهور بلاروس هیچ پیامی از سوی زلنسکی به پوتین منتقل نکرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/664695" target="_blank">📅 21:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664694">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c4e4404a.mp4?token=k8JqfpD0Nj__KatFoRUCwmuMnKNuOFafyhgj_fapwOO-Pttd5oIH20ydVh3jneEzl2Ocfgc3PFAF1RgRNu5dLne3M5u_plBCm765kbIvJ9h97HndSqV2qTRBVHEaeCnbGi4xNKE9QHc5M0PiHkA6hqBNIf-rRVdv_WkRzDXM4U07FKIk-q6MjBCGfrEaAaMe9WsK8Bh4GGghlwDpLSDJcf6e2Nai5OfrJu7smJ1w_j1jiBBvSGZjeCsxdBMgBhNA3Zoj99KNU08kmRZrT1ttLbHRGelduCfrhNB4n4z0hlPsxsYswwMFzTLPxahh16b_wTXjpPvOmyYbv88mGrpd4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c4e4404a.mp4?token=k8JqfpD0Nj__KatFoRUCwmuMnKNuOFafyhgj_fapwOO-Pttd5oIH20ydVh3jneEzl2Ocfgc3PFAF1RgRNu5dLne3M5u_plBCm765kbIvJ9h97HndSqV2qTRBVHEaeCnbGi4xNKE9QHc5M0PiHkA6hqBNIf-rRVdv_WkRzDXM4U07FKIk-q6MjBCGfrEaAaMe9WsK8Bh4GGghlwDpLSDJcf6e2Nai5OfrJu7smJ1w_j1jiBBvSGZjeCsxdBMgBhNA3Zoj99KNU08kmRZrT1ttLbHRGelduCfrhNB4n4z0hlPsxsYswwMFzTLPxahh16b_wTXjpPvOmyYbv88mGrpd4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی: مین‌زدایی تنگه هرمز فقط توسط ایران انجام می‌شود  معاون وزیر خارجه:
🔹
ماکرون گفته در مین زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری می‌کند.
🔹
طبق یادداشت تفاهم اسلام آباد، مین زدایی صرفا توسط ایران انجام می‌شود و نه هیچ کشور دیگری، اصولا اجازه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/664694" target="_blank">📅 21:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664693">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ad4624ca.mp4?token=u0qq9hiWa2Tbstp4OHQ28VkDqpB0X8QR4B5YEggn8tWvlEJy_MRsNO90hfW8VapOO8rEqPddp2qfiHy-tRX6upCC5LnOvGNjEyhHngq4xSjVD5VsbFbg8OOLFAN3SL-4cG3KCUbUYuk6W3E8rviiJbI322ryWWo_rLsOL9kVayJgOA4O33meJXtVt1eGYT0bPIXLnRDd-8OGfjVXyfYZA63bFXWuhGQgRMS795muGi5pcU4Rjjv8fTwRE8yWXEq2fViHGOspJvbKRFvRiZyhU8zWS2DgQej3kd2ydSvl6sg_cMvpQrGHTX1eEokgiC8DCFkUT_8ImBJ93j4yf57fHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ad4624ca.mp4?token=u0qq9hiWa2Tbstp4OHQ28VkDqpB0X8QR4B5YEggn8tWvlEJy_MRsNO90hfW8VapOO8rEqPddp2qfiHy-tRX6upCC5LnOvGNjEyhHngq4xSjVD5VsbFbg8OOLFAN3SL-4cG3KCUbUYuk6W3E8rviiJbI322ryWWo_rLsOL9kVayJgOA4O33meJXtVt1eGYT0bPIXLnRDd-8OGfjVXyfYZA63bFXWuhGQgRMS795muGi5pcU4Rjjv8fTwRE8yWXEq2fViHGOspJvbKRFvRiZyhU8zWS2DgQej3kd2ydSvl6sg_cMvpQrGHTX1eEokgiC8DCFkUT_8ImBJ93j4yf57fHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل تساوی برزیل به ژاپن توسط کاسمیرو
🇯🇵
1️⃣
🏆
1️⃣
🇧🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/664693" target="_blank">📅 21:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664692">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: درآمد حدود ۴ میلیارد دلاری از نفت، برای ثبات در بازار ارز کافی نیست
جعفر قادری، عضو کمیسیون اقتصادی در
#گفتگو
با خبرفوری:
🔹
پول حاصل از فروش نفت کاملاً در اختیار دولت است و به حساب بانک مرکزی واریز می‌شود و هر جا که دولت بخواهد می‌تواند هزینه کند.
🔹
مبلغ فروش نفت که حدود ۵۰ میلیون بشکه با احتساب هر بشکه ۸۰ دلار است، درآمدی حدود ۴ میلیارد دلاری دارد و برای ایجاد ثبات کامل در بازار ارز کافی نیست.
🔹
تورم داخلی حدود هفتاد تا هشتاد درصد تأثیر مستقیم بر قیمت کالاها دارد و حتی اگر نرخ ارز کاهش یابد، تورم داخلی همچنان قیمت‌ها را بالا نگه می‌دارد. با فروش تدریجی نفت به تدریج قیمت‌ها ثبات پیدا خواهند کرد مگر اینکه مشکل خاصی پیش بیاید.
@TV_Fori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/664692" target="_blank">📅 21:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664691">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
غریب‌آبادی: مین‌زدایی تنگه هرمز فقط توسط ایران انجام می‌شود  معاون وزیر خارجه:
🔹
ماکرون گفته در مین زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری می‌کند.
🔹
طبق یادداشت تفاهم اسلام آباد، مین زدایی صرفا توسط ایران انجام می‌شود و نه هیچ کشور دیگری، اصولا اجازه…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/664691" target="_blank">📅 21:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664690">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
تروریست‌های آمریکایی صهیونی یک خانواده را در سراوان به گلوله بستند
🔹
یک خودروی شخصی حامل اعضای یک خانواده در حال تردد در شهرستان سراوان هدف تیراندازی افراد مسلح مزدور دشمن قرار گرفت.
🔹
این حمله توسط گروهک تروریستی وابسته به رژیم صهیونیستی و آمریکا انجام شده است.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/664690" target="_blank">📅 21:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664689">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpbjrwX0ci-wAnzaY-EGYFhV-soBuOBnNoeWuzuiAK2YCRWEcAukGTrcStRb6I5R2ulj4TQP47qx9lS7x5iNgVhAG0V6qJlkDJ-xJvvYgryx3LxVFWxWqbI2xDTqN6iCRVEupF3b0TjUvrTcSj9lifkewP6d7WGc1mXmGG3DCOYYg9TQBMt-_zH2a_Oz4VhzMf7Ct8oCtz3LeUlkHDyXU5u2Nbr8RnkXcpEqG9vq7bTKRSv_aMhxVWrhQbD2kSv3b2h79IubRboxndW_gRR4JQbI8ZAtquzxZMmaXKhG4Sr1ZiI6HHn8PI0Lc9cEFepBkk_-tqIG6uy0Lf3fifRUqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پخش زنده مسابقات جام جهانی ۲۰۲۶ در آیگپ
🔹
همزمان با برگزاری رقابت‌های جام جهانی، کاربران آیگپ می‌توانند از طریق بخش «خدمات» و گزینه «پخش زنده جام جهانی» مسابقات را به‌صورت زنده و تنها با تلفن همراه خود تماشا کنند.
جزئیات بیشتر را در سایت خبرفوری بخوانید:
https://www.khabarfoori.com/fa/tiny/news-3226605</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/664689" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664688">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
غریب‌آبادی: مین‌زدایی تنگه هرمز فقط توسط ایران انجام می‌شود  معاون وزیر خارجه:
🔹
ماکرون گفته در مین زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری می‌کند.
🔹
طبق یادداشت تفاهم اسلام آباد، مین زدایی صرفا توسط ایران انجام می‌شود و نه هیچ کشور دیگری، اصولا اجازه…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/664688" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664687">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دو منطق آمریکا و اسرائیل در جنگ با ایران؛ یکی دنبال امتیاز است و دیگری پایان!
🔹
اگر تاریخ جنگ‌ها را با نگاهی عمیق‌تر بررسی کنیم، متوجه می‌شویم که بسیاری از آن‌ها فقط نبرد نظامی نیستند؛ بلکه نبردی بر سر اقتصاد، منافع و قدرت‌اند.
🔹
بسیاری از تحلیلگران معتقدند بخش قابل‌توجهی از جنگ‌های مدرن را می‌توان با منطق اقتصادی توضیح داد. در این الگو، هدف اصلی نابودی طرف مقابل نیست، بلکه افزایش هزینه‌ها تا جایی است که او رفتار خود را تغییر دهد.
🔹
جنگ در اینجا ابزاری برای چانه‌زنی است و وقتی هزینه‌ها از منافع بیشتر شود، مذاکره دوباره به گزینه اصلی تبدیل می‌شود.
🔹
اما همه جنگ‌ها از این منطق پیروی نمی‌کنند. برخی درگیری‌ها ماهیتی ایدئولوژیک دارند، جایی که مسئله فقط کسب امتیاز نیست، بلکه تقابل بر سر هویت، نفوذ و نظم منطقه‌ای است. در چنین جنگ‌هایی، تحمل هزینه بسیار بالاتر است و پایان آن صرفاً با یک توافق سیاسی رقم نمی‌خورد.
🔹
بسیاری از ناظران معتقدند تقابل اخیر ایران، آمریکا و اسرائیل، ترکیبی از همین دو منطق بود. آمریکا عمدتاً با رویکرد فشار برای تغییر رفتار ایران در موضوعاتی مانند برنامه هسته‌ای و سیاست‌های منطقه‌ای وارد میدان شد؛ رویکردی که در آن محاسبه سود و هزینه نقش تعیین‌کننده دارد.
🔹
در مقابل، نگاه اسرائیل از دید برخی تحلیلگران، امنیتی‌تر و ایدئولوژیک‌تر بود، نگاهی که ایران را صرفاً یک رقیب سیاسی نمی‌بیند، بلکه آن را چالشی راهبردی برای آینده خود تلقی می‌کند.
🔹
در چنین شرایطی، صرف‌نظر از روایت‌های سیاسی، آنچه قابل توجه است این است که ایران توانست در برابر هم‌زمانی فشارهای نظامی، سیاسی و اقتصادی مقاومت کند و مانع از تحقق بسیاری از اهداف اعلام‌شده طرف مقابل شود.
🔹
به همین دلیل، از نگاه بخشی از تحلیلگران، نتیجه این تقابل را نمی‌توان صرفاً «شکست ایران» توصیف کرد، بلکه باید آن را نبردی دانست که موازنه قدرت و معادلات منطقه‌ای را وارد مرحله‌ای تازه کرد../خبرفوری
#سرمقاله
@TV_Fori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/664687" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664686">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
بانک مرکزی: انتخاب شرکت برای رفع اختلال ۴ بانک، بر عهده خود بانک‌هاست و ما نقشی نداشتیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/664686" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664685">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
کدام بخش‌ها در جنگ بیشترین ضرر را کردند؟
🔹
جزئیات تازه از رشد اقتصادی نشان می‌دهد بخش‌هایی که بیشترین آسیب را از جنگ و نااطمینانی‌های اقتصادی دیده‌اند، بیشترین افت را نیز تجربه کرده‌اند.
🔹
در زمستان ۱۴۰۴، حمل‌ونقل با ۹.۶ درصد، عمده‌فروشی، خرده‌فروشی، هتل و رستوران با ۵.۸ درصد و صنعت با ۴.۲ درصد کاهش روبه‌رو شدند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/664685" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664684">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم
🔹
اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیئت ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله  بند ۱۱ انجام می‌شود ندارد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/664684" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664683">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYffmTtGKALVdjI_S96596-Okgk3NpFJfMV_tFlC50xZvrDHv2iXZ5fp5Hk4REizxoFJyZC7OtAWaoc1uq4gXYM6mY6IpZxcBa8r4CKUkLcBqJLV-csSOauEZ_vfyYMKFxjKbVUHwENjWoBZjOBRiTcqQ7nNpGfnEsAnKsrczG1zZyZTvQPM7s4uE6JwDNdtVfKWKbe7x6b-s6TgQNKwp_fWZWV7-370W2MTxrKIwzhrNXhPWi8jcC_3wdPJRAxvj5w2gg3FVOwE76Il2KGLqzpKHBQITnsUHrXRLwp6w90Neyg9fkx0b3AEbrzHjKwP94CGE4d8jAqjqHypjJFAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی احترام به اعتقادات، از اسپانسر هم مهم‌تر می‌شود
🔹
جایزه بهترین بازیکن جام جهانی با حمایت برند آبجوی Michelob Ultra اهدا می‌شود؛ اما اگر برنده یک بازیکن مسلمان باشد، برای احترام به باورهای دینی او، نسخه‌ای از جام بدون لوگوی این برند الکلی به او تقدیم می‌شود.
🔹
حرکتی که نشان می‌دهد گاهی احترام به عقاید، فراتر از قراردادهای تبلیغاتی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/664683" target="_blank">📅 21:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664682">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0GvxGPpy1HH9ze8AcO-f9X-ATOLnkgN-9FT6Cz9Dn_PpNzCjOSXBqsR6B3eWnxTOhK8A2ceAR748zq1YzXdnMHn5wCkGuQVym7vDJPBtWJQiHRtaXm1ZznFV0JqZYPmySIH-xAtacAxMsyjJGT8FdPc7LnSnv1Sn4aw6JE0XdjQRH54pYDdzuF0mt0kPdWDSEHoES5FO5BTfZMzufAqJt_yh7PO2Y1kYIa7pC5MLv1gk9gBcn_896h998vc2saipV1t538wB1S8DZi_jDAmn8UHGqJyv-UG3_cA1CQngyRI868gRaLjdsGmxBp5hlOoGpozyLMDGGaSC9mJD6BTWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تماشاگران ویژه بازی برزیل با ژاپن
🔹
رونالدینیو، رونالدو، روبرتو کارلوس، ببتو و جیمی باتلر ستاره بسکتبال NBA
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/664682" target="_blank">📅 21:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664681">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27739e3f1c.mp4?token=WmDdmi-6aLek9gQp0I7C8-RvYVeuORRIYICIld_J3NQYhFoHX3l_KiemZDAfywmNGIxmcCTeQXS-goFx6TEgGrMqrN_OxPQrOB3n_wbvZn6c2S10UXU181PRKVTmYYNSWqG6gE4JhfSbhMCZGDj9r_5klpsP5FOl7wpQADHVgspcINT0ricYbBeycr7XPty9V8FvBNsjRT7-TaMyylN9QMDj1Mcczs0f1jpIlfsLIgtQNAW1JEIBswqOicrw8TexZlTQPNCwVnE6N0t7kx56iy5nXfnVijfflb4vJmMQ-rE0oo8yCnJxHLwGY-RERwkj5_xjmYa8N6odIEQIwwpL0YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27739e3f1c.mp4?token=WmDdmi-6aLek9gQp0I7C8-RvYVeuORRIYICIld_J3NQYhFoHX3l_KiemZDAfywmNGIxmcCTeQXS-goFx6TEgGrMqrN_OxPQrOB3n_wbvZn6c2S10UXU181PRKVTmYYNSWqG6gE4JhfSbhMCZGDj9r_5klpsP5FOl7wpQADHVgspcINT0ricYbBeycr7XPty9V8FvBNsjRT7-TaMyylN9QMDj1Mcczs0f1jpIlfsLIgtQNAW1JEIBswqOicrw8TexZlTQPNCwVnE6N0t7kx56iy5nXfnVijfflb4vJmMQ-rE0oo8yCnJxHLwGY-RERwkj5_xjmYa8N6odIEQIwwpL0YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تذکر پزشکیان به مصرف غیراستاندارد برق در سازمان استاندارد
🔹
در بازدید رئیس‌جمهور از سازمان ملی استاندارد چه گذشت؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/664681" target="_blank">📅 21:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664680">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/659dd30758.mp4?token=eQH1ypIHXbJgl_TTOmldIyNEwoenM-VphMlrTrDe7ajlga9bfNxjXoTj8aMx1ZXX0_OYcWCMezZxitMx2SJmw5WTQZkjZ11mHXxBfBuV1vWBZ5RjbSV6XHCj3ov9iQnd_-3VRDlq4Z02l1n3C5aqdO-pysl2GjRljdpGLdvlb0MgSi1oHTN__HBO-FWYqeg2bmz4Esj1KqP1oUo8msy47wGjl2GiyU7AUP6LZWgJWbp65bBsTWqVZkfPmaWiXKlC181MZ3OXEfofxjBoxbFkFGV6OPS9VslUf5J0nek6I1d6kC8-iZ3AjJt6suxeoDnr0YDk0AG-Mwgxx7Jnoftzd4T7Qk_dYES6FDl78FuLD0sOHNPieBgSU33su5wt423Fhf4aONGCJJtFLiqhIu9nKo3K2miWxXMpqRTbJz43Ui3cZgl-bxUvjfrzDxCD7xTQ92hhIY0cnwdAz1zA0r2IhMmQVVySbs_2AhXMNrib1RBck8Rk6n7OrivsCDvmyOaqH-W9hUG-gWbiCwL4OHm9xCdlckzgpCBWBrO_qlp9VBWxXVCNI6PFAV_cRosJ-Kkqmoj_q9Dv33cNoSJsceWvM0j8oO_6yEAgV5AXdTZ7GI-RNfbtfMz2hmEtEoTsvZnfkty6mfNwLv9cO7uxFOb1xUBXRak18Ka0-qiD7lrQHMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/659dd30758.mp4?token=eQH1ypIHXbJgl_TTOmldIyNEwoenM-VphMlrTrDe7ajlga9bfNxjXoTj8aMx1ZXX0_OYcWCMezZxitMx2SJmw5WTQZkjZ11mHXxBfBuV1vWBZ5RjbSV6XHCj3ov9iQnd_-3VRDlq4Z02l1n3C5aqdO-pysl2GjRljdpGLdvlb0MgSi1oHTN__HBO-FWYqeg2bmz4Esj1KqP1oUo8msy47wGjl2GiyU7AUP6LZWgJWbp65bBsTWqVZkfPmaWiXKlC181MZ3OXEfofxjBoxbFkFGV6OPS9VslUf5J0nek6I1d6kC8-iZ3AjJt6suxeoDnr0YDk0AG-Mwgxx7Jnoftzd4T7Qk_dYES6FDl78FuLD0sOHNPieBgSU33su5wt423Fhf4aONGCJJtFLiqhIu9nKo3K2miWxXMpqRTbJz43Ui3cZgl-bxUvjfrzDxCD7xTQ92hhIY0cnwdAz1zA0r2IhMmQVVySbs_2AhXMNrib1RBck8Rk6n7OrivsCDvmyOaqH-W9hUG-gWbiCwL4OHm9xCdlckzgpCBWBrO_qlp9VBWxXVCNI6PFAV_cRosJ-Kkqmoj_q9Dv33cNoSJsceWvM0j8oO_6yEAgV5AXdTZ7GI-RNfbtfMz2hmEtEoTsvZnfkty6mfNwLv9cO7uxFOb1xUBXRak18Ka0-qiD7lrQHMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماری که واقعیت تلخ تیم ملی را در جام‌جهانی فاش می‌کند
🔹
هرچند به ظاهر بدشانسی یکی از مهمترین عوامل صعود نکردن تیم ملی به دور بعدی جام‌جهانی بود اما برخی آمارهایی که در این ویدئو می‌بیند پرده از یک واقعیت تلخ برداشته است.
@TV_Fori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/664680" target="_blank">📅 21:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664678">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/978f228826.mp4?token=gtNo0D3ggxsz9zkqOkzHsjQzNllGX6xhmchNoj5aXcUrDTQtIClpkts2h1YaXjfF41qmrQ8Oju8MS6jtp4Hxph51JQj77T5qE9ZUxozXr2BIlhqGGDHO_6AViYLyQiMINNBYHmC8VGFvknP-UEz6qwzb2Gpcd8qbEcD2HVHOtdMuTsmIW98BTLPeERvjtwuYal39TDr-0cyTJgp9bDEsKP8g0DgKhvPiyc-O6y0Zkv6iGhKnfWGqvMk5WIwtXMkkuH7G1HG-OsODgvFAmdPsFq24POWFSfEqUXQShacliV7h_rD8xHJe5L0TXuhVrho0XRBz2z3l0u__EputemOqZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/978f228826.mp4?token=gtNo0D3ggxsz9zkqOkzHsjQzNllGX6xhmchNoj5aXcUrDTQtIClpkts2h1YaXjfF41qmrQ8Oju8MS6jtp4Hxph51JQj77T5qE9ZUxozXr2BIlhqGGDHO_6AViYLyQiMINNBYHmC8VGFvknP-UEz6qwzb2Gpcd8qbEcD2HVHOtdMuTsmIW98BTLPeERvjtwuYal39TDr-0cyTJgp9bDEsKP8g0DgKhvPiyc-O6y0Zkv6iGhKnfWGqvMk5WIwtXMkkuH7G1HG-OsODgvFAmdPsFq24POWFSfEqUXQShacliV7h_rD8xHJe5L0TXuhVrho0XRBz2z3l0u__EputemOqZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوت دیدنی؛ گل اول ژاپن توسط سانو در دقیقه ۲۹
🇯🇵
1️⃣
🏆
0️⃣
🇧🇷
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/664678" target="_blank">📅 21:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664677">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BI-XgAnt32ITg6s7yceNTaqgPIU6PBi67fc1EWUlslhDXAqbT7XapFOOHvMbqYYFxYKElcNmH2EHAYVWh51iiIx2bGBo1BEOKuZlaEoEpXdgNb_jm2-EKlVLfELtj-5VDUiPJ_6EW5v3coSNX0md_P-PqVCqhZE96JyKyLbphx76yrmFz_HQNKY3JcUUwWHggHSaDZS6OXxFLneq0xJwq1jS9ZcKmwFZjGwHPJnUEAELgTEgGEJ2HPsVI0O8bR1CYJPogx6WvfQ_BP9bG-pO1Y7_V8IEXPRZaF740ieU6Tw6FH9cM4BWxwIIfcWieNwByAekAY-Q-MUypaG8NS243g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی فیلم: مارتی سوپریم ۲۰۲۵| (Marty Supreme)
🔹
ژانر: کمدی سیاه، ورزشی
🔹
امتیاز (IMDb): ۷.۷
🔹
خلاصه: تیموتی شالامی در نقش جوانی جاه‌طلب ظاهر می‌شود که برای فتح دنیای پینگ‌پنگ حرفه‌ای، مرز میان نبوغ، وسواس، شهرت و جاه‌طلبی را درمی‌نوردد. «مارتی سوپریم»…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/664677" target="_blank">📅 21:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664676">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: هنوز وارد مرحلۀ مذاکره برای توافق نهایی نشده‌ایم
🔹
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آن‌هاست.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/664676" target="_blank">📅 20:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664675">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه:  اولویت کنونی ایران، حصول اطمینان نسبت به اجرای مفاد یادداشت تفاهم است
🔹
در رابطه با تعهد آمریکا طبق بند ۱۰، یعنی فروش نفت، مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم.
🔹
در رابطه با بند ۱۱، یعنی آزادشدن دارایی‌های…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/664675" target="_blank">📅 20:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664674">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه:  اولویت کنونی ایران، حصول اطمینان نسبت به اجرای مفاد یادداشت تفاهم است
🔹
در رابطه با تعهد آمریکا طبق بند ۱۰، یعنی فروش نفت، مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم.
🔹
در رابطه با بند ۱۱، یعنی آزادشدن دارایی‌های مسدودشده ایران، نیز فرآیند اجرایی‎‌شدن آن درحال پیگیری است.
🔹
در این چارچوب، همین هفته هیئتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/664674" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664673">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
معاون سیاسی نیروی دریایی سپاه طی سانحه رانندگی درگذشت
🔹
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان جان خود را از دست داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/664673" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664672">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ae4c4e4d.mp4?token=iMsGHXQdLAli6DUIQjoyMHvUVibO_Ppd5RHakcL7-6e6eAF17_k1rs0N7LcUUvElcYAFJ6G0LWS7ruGlRT0ia3RK_0vqUy6gC0zypRGs6y8B_II94jYBedwvIq2xLPsS_kPzV4-B_6IU4O3E0g2calr8eQGhJIcY4KREk_oaWqHX6aNVbThTwFlGkJKn2Yzs_jWjkSAFDWWsj2F5umpLaAoZyNaCYhBj-R4BbJqys7HOCmYV3lf1RrGhKycPKY3RfZ6Q52gqiISx1uDvqHl5HL95Is5694SwhGkTPews3XQT3SCm8BDTtjBCbcoZDnGJJBlIWpC5a_u3cxmMXLNfXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ae4c4e4d.mp4?token=iMsGHXQdLAli6DUIQjoyMHvUVibO_Ppd5RHakcL7-6e6eAF17_k1rs0N7LcUUvElcYAFJ6G0LWS7ruGlRT0ia3RK_0vqUy6gC0zypRGs6y8B_II94jYBedwvIq2xLPsS_kPzV4-B_6IU4O3E0g2calr8eQGhJIcY4KREk_oaWqHX6aNVbThTwFlGkJKn2Yzs_jWjkSAFDWWsj2F5umpLaAoZyNaCYhBj-R4BbJqys7HOCmYV3lf1RrGhKycPKY3RfZ6Q52gqiISx1uDvqHl5HL95Is5694SwhGkTPews3XQT3SCm8BDTtjBCbcoZDnGJJBlIWpC5a_u3cxmMXLNfXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار خرس از گربه که در شبکه‌های مجازی پر بازدید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/664672" target="_blank">📅 20:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664671">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
عضو رسانه‌ای تیم مذاکره‌کننده: تا الان هیچ مذاکرۀ هسته‌ای با آمریکا انجام نشده و تا عملی‌شدن شروط ایران هم مذاکره‌ای دربارۀ موضوعات هسته‌ای انجام نمی‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/664671" target="_blank">📅 20:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664670">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyt4SePEYe7MGg34q5Ph_NkMLBj_uYwG1gT3UNUma7coYIZ6FjDywt7TJIC02peTljUn2j-ECC9JUUOThmKyEmG--HJ74m7sPtMuaNQzFr_M7r2Aec1JKIgBRouPA54zA5Tfq8mpMm4XK0saRxTUOnhr92m_YTmKAccnRJSceo1mETrhWHyPAFXM8Rc--T63NUNsZzymSDKak1UgD6Y_u_S4W4sX8sWJHkdmkSBSCFod9ElKEyhel1bQ4HeFCZA-ikhoAW0AAQbiSKKkfhfW9mkwkpIse9qqUFA9sw7IlJBC9IHBXqzYaX0H3i6y7DeJBWtodP3gvIN3dfA0EqJ8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینوستوران از مرز ۱۰۰۰ میلیارد تومان تأمین مالی عبور کرد
🔹
اینوستوران به عنوان بازوی تامین مالی جمعی گروه مالی پاسارگاد، با عبور از مرز هزار میلیارد تومان تأمین مالی، به یکی از بازیگران اثرگذار حوزه تأمین مالی جمعی کشور تبدیل شده است.
🔹
اینوستوران تاکنون ۵۰ طرح را تأمین مالی کرده که ۳۴ درصد آن‌ها در حوزه‌های دارو، سلامت و امنیت غذایی بوده‌اند. همچنین ۵۴ درصد از مبلغ سرمایه‌گذاری‌ در طرح‌های این سکو به طرح‌های دانش‌بنیان اختصاص داشته است.
🔹
در طول مدت فعالیت اینوستوران تاکنون، ۶۸۱۴ نفر در طرح‌های این سکو سرمایه‌گذاری کرده‌اند که ۲۷۶۲ سرمایه‌گذار منحصربه‌فرد حقیقی و ۷۵ سرمایه‌گذار منحصربه‌فرد حقوقی در بین‌شان بوده است.
🔹
اینوستوران با رویکرد رشد جمعی در تلاش است با توسعه تأمین مالی جمعی، زمینه رشد کسب‌وکارها و شرکت‌های مولد و موثر کشور را فراهم کرده و در مسیر رشد و توسعه اقتصاد کشور نقش‌آفرینی کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/664670" target="_blank">📅 20:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664666">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
روایتی تکان‌دهنده از تجربه نزدیک به مرگ؛ از دیدن عذاب گناهکاران تا چشیدن طعم میوه‌های بهشتی
🔹
00:06:00 حسابرسی نیکی کردن و شیطنت‌های دوران کودکی
🔹
00:12:40 چشیدن طعم میوه بهشتی، مانع خوردن میوه دنیایی شده است
🔹
00:24:00 اطلاع از زمان فوت دوست در کما
🔹
00:29:00 سفارش به ادا کردن حق دیگران
🔹
00:35:00 دعای رفتگان در حق بازماندگان
🔹
00:49:20  بخشش اعمال در حق‌الله و برپایی عدالت در حق‌الناس
🔹
01:05:00 کسب معرفت از محضر اهل بیت در برزخ
🔹
قسمت بیست‌وپنجم (طعم میوه)، فصل چهارم
🔹
#تجربه‌گر
: عبدالکریم حاجی‌زاده
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/664666" target="_blank">📅 20:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664665">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyncNvNjnkBg2GoNvYB_CeVal4GNBv2kSOX0F0qzEAsdgXgcRnB71BP2w36dNTKfCDDyfyQa85OByTNB_F17IOuYZ5z5yBWw8CzrJBgnb-xBLOZYJwCMOjyO_VshDF3RMDMb_VlTGpWH6z0SvUdpwe5Yu_fcWUFIQKQZKmmAbWFlVruCs7JZuVZv1sPM3_leKeaICaBqwmc8MwyzWdU9t5ZovxC-ZgAvqnhlRToepUyT0mAMJ2Zfy9wIVOHd2f7pudObyIQjQgC1Chlef6JGRfvsd_FNjR5BSiDXSz15ET5M_CyGAQV7ZFULMgIMjBcnlZHtyLA1cRJJS-Uy1Dm0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: مین‌زدایی تنگه هرمز فقط توسط ایران انجام می‌شود
معاون وزیر خارجه:
🔹
ماکرون گفته در مین زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری می‌کند.
🔹
طبق یادداشت تفاهم اسلام آباد، مین زدایی صرفا توسط ایران انجام می‌شود و نه هیچ کشور دیگری، اصولا اجازه چنین کاری را هم نمی‌دهیم.
🔹
شرایط حساس و پیچیده است. توصیه اکید میکنیم فرانسه آن را با تحریکاتش پیچیده تر نکند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/664665" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664660">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtMtTS7sKvsYLWI-XtvY4uK5lVJQ-gRDqVupe5SMW7huAv9KFhxfTXzRZZrTfreycN8wdOaKAf-PTq8fUIevr4b5pm654i88OBm8ZvDQlYsuJBxgCqufh7eS6AtWv5JHNlTOxHjbJOiBM8JQ44qGyTPgCuUbn6fe-2EpSG5kuSxkXWkyBDLmOrOpaS6yJlWGpnnHX9GThhhwcVvF0AieIAkcMqAChcAHkpMxnLEcdo6ppuLexu9oAlcL4qBjDJ-JobzfToFgydpjrukAsyEX8lnyOpL4F_gGqYPOS2f5sXZg4DbImbfnXx9u1KM46tMKEnUqb2IX8jLwi2j3lpm9rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrXcdakADyIMp9knJoVccWs7ZSZgF_iWPi7lVNEP0XICp7uDtr4L_fI1wqRRT7Vah7cxgCbBM-gUPCsCgwPuHFfTgI3H9ogX94O6oPLMIGsabGqh2XXCM8gSyvhbQKPJJBHl40xwlWM6FoOdeqiwvcBW0WpsuNyhiAJn-MLgcXVpScRqSF6_mDsrn6H7MCZom25_e5WXPkUt7xXUf91EsrNmFeXrxYxjVImA_yjPmznGc4gIO19Gv1-usADOqYQWLL68yqDKIVhprGazuWl17a8ZVxRo1AV7oPp29_WQ8irrIe-VK_iVki8ShZZqmJaMxIDxXOwpuyvc58Xnj85STw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این کتاب فقط برای کودکان نیست؛ برای همه کسانی است که وقت کم می‌آورند
🔹
«مومو» فقط یک داستان کودکانه نیست؛ قصه دختری است که مقابل «دزدهای زمان» می‌ایستد؛ موجوداتی که آدم‌ها را آن‌قدر گرفتار عجله و کار می‌کنند که فرصت زندگی را از یاد می‌برند. رمانی خیال‌انگیز از میشائیل انده که بعد از نیم‌قرن، بیش از همیشه به زندگی امروز ما نزدیک‌تر به نظر می‌رسد.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/664660" target="_blank">📅 20:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664659">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jR6FeKwuOM_rleav2RHDuukLG4SVYP1OJkvFrkaMf47Nvix0HOJqvRsdqOiMfP22U4tmv47PBUMt_U5wWizaWUYxBcSd-csJ2XXgmUPzMO-naB2a5VmK_4artW_uvuNvjblrdTMGY0KgYoYiNcEEfmvr8IZmIpRpucmJMEugAAlTcInCFg2FHm_DkHD09QtHgBrV0OCUC-dz51OPD-mOACAM1-iXIOVt7dNSVio5ejOQyaMENFQri0FrPIzILhl2pRj2eRKPoMtHY65QlBMvV2M1cMWfw6Q3w5vNXrdmuswi53Fi8Zd14-vMOvFAf3woyi0Vqyv2JRHk5pphIfaaJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدیه سلطان عمان به رئیس جمهوری فرانسه
🔹
خنجر سنتی طلایی دست ساز عمانی، هدیه سلطان هیثم به میزبان فرانسوی بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/664659" target="_blank">📅 20:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664658">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3764ca1156.mp4?token=Zti8oNVDWik-LpSEHz9R6c-4vj6uzinkSwlADfwkDHhnjDx7GTuI3cmpI4yPD7sJltmsNXmPHvsh2ckzAYNjz0NrWoYKSyjlDoBuwoIOb_he2TyNcWvw_OvQsq49Q4DAvjgQLa3Yk0UGbG1eTEYxXm5anKlCFwwJlYz4VQWu0z8YUzYwxNkjw22gPlzEp7jpgESf6B5laG5l9UYXRnXu54tyC6Sp-gFhyTQjW5f6khcChNssUMPL1_hQhhKch-RvY0aA22OKuvxS2vDszZkJBz-yaWs5L8sPOjlx7wIG4vP2TCx8xGXXC7I_bAOUWEh7bY5rR_CCoUS30wuFGQZePw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3764ca1156.mp4?token=Zti8oNVDWik-LpSEHz9R6c-4vj6uzinkSwlADfwkDHhnjDx7GTuI3cmpI4yPD7sJltmsNXmPHvsh2ckzAYNjz0NrWoYKSyjlDoBuwoIOb_he2TyNcWvw_OvQsq49Q4DAvjgQLa3Yk0UGbG1eTEYxXm5anKlCFwwJlYz4VQWu0z8YUzYwxNkjw22gPlzEp7jpgESf6B5laG5l9UYXRnXu54tyC6Sp-gFhyTQjW5f6khcChNssUMPL1_hQhhKch-RvY0aA22OKuvxS2vDszZkJBz-yaWs5L8sPOjlx7wIG4vP2TCx8xGXXC7I_bAOUWEh7bY5rR_CCoUS30wuFGQZePw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم هولناک از دوربین‌های مداربسته لحظه وقوع ۲ زمین‌لرزه مهیب در لاگوایرای ونزوئلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/664658" target="_blank">📅 20:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664657">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8730ecbe0b.mp4?token=SCHN-7sgqnz1sj8g6UOFjNhdMj_-6RgteDzIO7gYmxXL6RqUu2mpyGaobfb22oPhGd4ESjDlyWurDmxWgkK7cFYaucrCwJrxCRi7-iECMNet9BuhNCq8a2uYJe4hIRNGDi53RAtD7ol3S61mKf5tAvohaGmrfgAcwVtXFZUm8IqxX6frhheKMUiLu2hhBISZht5DQ9U5XdzyyfNCWdFwNprSDVpf5MSEX8Wvm6cHZjn_xab0GF99MRJbkwPZsiNoaqhPHpM_4_RwJhy_CnSgbiDeovVzAMVnol2q2H4fKhJQ6IwgjZ83bVYHpgTKdl9PLDZVArKrkLratEcOgY3IFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8730ecbe0b.mp4?token=SCHN-7sgqnz1sj8g6UOFjNhdMj_-6RgteDzIO7gYmxXL6RqUu2mpyGaobfb22oPhGd4ESjDlyWurDmxWgkK7cFYaucrCwJrxCRi7-iECMNet9BuhNCq8a2uYJe4hIRNGDi53RAtD7ol3S61mKf5tAvohaGmrfgAcwVtXFZUm8IqxX6frhheKMUiLu2hhBISZht5DQ9U5XdzyyfNCWdFwNprSDVpf5MSEX8Wvm6cHZjn_xab0GF99MRJbkwPZsiNoaqhPHpM_4_RwJhy_CnSgbiDeovVzAMVnol2q2H4fKhJQ6IwgjZ83bVYHpgTKdl9PLDZVArKrkLratEcOgY3IFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول پولدار بشم بعد بچه میارم!...</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/664657" target="_blank">📅 19:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664655">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
سامانه‌های بانکی هفته آینده همزمان با مراسم تشییع و وداع با رهبر شهید ۲۴ ساعته فعال خواهند بود
بانک مرکزی:
🔹
شعب کشیک بانک‌های استان تهران روزهای شنبه و یکشنبه فعال هستند.
🔹
همه شعب بانک‌های کشور روز دوشنبه تعطیل هستند.
🔹
علاوه بر دستگاه‌های خودپرداز بانک‌ها دستگاه‌های خودپرداز سیار در مسیر تشییع مستقر می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/664655" target="_blank">📅 19:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664653">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3A5Q9mKF9SRtvQ_jC80wxFMTsE8Cw5ST8p3raU1-eNwDePlWdgWR6X2AIopahYaUbK13HFVLHP2EgUiZLWgSceKcMtmaDczzm5RoZply_M-bXWwZ3zXgtktr53HTcAvCqk05VoF8NSiCjd4hX2yzjT9wx2S1PdHb5e0mXz1CiUaCd_6ifGBC6Zt4ASXpGNZJQd8CXss22_FbfUllInJlPkpgsHE4UA0g6Ro6nkQK3OVwq0_fJTvHuPRSCZfZEYyjjsCvUL_9hsbiN4d20bta5YwMPagm88teOaCuThY49g-jyrSvJ3aFFr1V3nltUav73VOXPBbg0YO6bq6CAfHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏡
زمین را قسطی بخرید
بهترین فرصت خرید زمین
جهت مشاهده مزایده بصورت هفتگی به سایت املاک و اراضی آستان قدس رضوی مراجعه نمایید.
🌐
آدرس سایت:
https://amlak.razavi.ir/panel/auctions/#auctions
📞
شماره تماس:
051-91008003
#زمین
#مزایده</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/664653" target="_blank">📅 19:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664652">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: بی‌برنامگی وزارت نیرو در بحث قطعی برق مشهود است
احمد آریایی‌نژاد، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
در صورت باز شدن صحن مجلس احتمال استیضاح وزیر نیرو وجود دارد و نوسانات برق، شفاف نبودن این وزارت در برخی از موضوعات، علل استیضاح وزیر نیرو است.
🔹
بی‌برنامگی وزارت نیرو در بحث قطعی برق مشهود است و باید توسط رسانه‌ها این موضوع اعلام شود که وزارت نیرو بدون اطلاع قبلی برق را قطع می‌کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/664652" target="_blank">📅 19:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
سنتکام: هم‌اکنون بیش از ۵۰ هزار نظامی آمریکایی در خاورمیانه مستقر هستند و در حالت آماده‌باش کامل به سر می‌برند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/664651" target="_blank">📅 19:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABccn4AG8j-0SYnWmTyj13pBcN2BXPY3Q2glPmqIZNEGcdovRLVseTLXLy5I6TieGP4CPcXheyWfmuh99ZVYn3a3vXDJ7bV9mTVmqFjyQmZR_iAionqU1Q49DdmLseCX7GNKgjC1hkd6HKBX5xehrFdTXOj09RZzbcdkfQG7Gxgw7V-PpJ2BLwhiuo-YkKHorWQzJctnjZAD-vAFtAEWnAq8Fi8r93pwfZK0x9SkCFjoXGAR6z-KvTjYS5uhKdTBUlf6-I61eQTpPvHHCOg1DhtHjjk1GSzeRGRB-uWc9S5jaj9pg2DZIsz8AW_S9MoCWlrMWcRElBdHhE5pjDhXlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ از پیروزی تاریخی در پرونده اختیارات ریاست‌جمهوری
🔹
دونالد ترامپ با اشاره به رای دیوان عالی در پرونده «سلاتر»، مدعی پیروزی بزرگ شد؛ وی این حکم را «تاریخی و بی‌سابقه» توصیف کرد و گفت این رای بر اساس ماده دوم قانون اساسی، اختیار رئیس‌جمهور برای برکناری مقامات قوه مجریه و منصوبان آژانس‌های دولتی را تأیید می‌کند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/664650" target="_blank">📅 19:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664648">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wqox_q82jcX6lT6iUMeWmsJYvfm9wx4NosjAtfXs5GDw4ubI_dhKhIm7MM3OgXPYdnJhP5KsA7sJZ6Zv6RKDqVolPnGNhdgYtvo2DZLLJtYrHt94FylJL9V3yo215Seni0Uar641wCp41FEgewxuN9uLVfuveNVr71U8hNeGEEYMKGFN4AvimUqsPNsc4Xomyyumc7obqSitl557tKC9AyYXoXAn8hEh729FDgcC7bX5lWpPNOwMC72WyINAQFHtCmtY12Ib-e55-fw0ixTlgfrrHus2wdzoDufYQeRO7Cvtb6LR7MhwQCk6sCOrNCX07Gq03gPhnJZY3XPiDY0gFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زابل؛ گرم‌ترین شهر جهان در ۲۴ ساعت گذشته
🔹
طبق داده‌های سرویس هواشناسی Ogimet، شهر زابل با میانگین دمای ۴۸.۶ درجه، گرم‌ترین شهر جهان در شبانه‌روز گذشته بوده است.
🔹
همچنین شهرهای طبس، بافق، دهلران و بم در فهرست ۱۰ شهر گرم جهان قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/664648" target="_blank">📅 19:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664647">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
خاطره روحانی از ایستادگی رهبر شهید انقلاب
حسن روحانی:
🔹
در جلسه شورای انقلاب گفتند اگر بخواهند کشور را بگیرند، من خودم تفنگم را برمی‌دارم و می‌جنگم تا کشته شوم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/664647" target="_blank">📅 19:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664646">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IddEKVT2c67Iz5uE2Loix_60X17gPoUM-WDp-75efjR0hUNKXk5HPyUmTxGgOeweLSJnW1GBwZ5QrZC4Tp9PeG90OlUAmT14iIsARwHoWNSgZsqIIFewwIiAEBOEgKD5be-RoqaR7P-q62EsKPGoUW0JUHIRS1TVBeT81Oql7wKKwt7oKu4re0JQJfchTiGCBXffbvsWyAOkTRNaTkCJmK3tQRW5cRozC7xUqAH4S8dKxuysvDNs56OEnrUt4evyQEVhvo3RJqjX0_2kb4lQdZQNiRkyrcRtTIdZRyVljzphDUvHIC_2_vEYVGWgPE_fzvrzGIFpEiMTMXzHcmkj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/664646" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664645">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYga1fs6b9ktnz1B6u5Kf1V1aAO7PKpUAKjpV0Ms86EhEC-Gf_dbh9vs3RWYxpov-pWWPXI2gFEGTiEXc6yPJ-XeP-g48Qo71KGaNybGYQ-qntP-S2MuQpF0uh0iCFCcWic1s_YTCe5YBqORGUTSSAExIgCmvBqupfy7YQekrEqp0ASNcri_D-ZAerXHmjkWlwIo-o8885TGvJ5yeDnamdVkfyvMJ8cgYnzunSdWRh9cB3yW_jeGOYByfVwXPaH9Qivg7SpHU21cZ7jOJXh-7yeA-D84535zBpYDCHk2n2sOkdGl8NGWi3WPrMJx2OHwmhWty0-LClYu3sRJsBfgGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«برد کوپر» فرمانده سازمان تروریستی سنتکام که به لبنان سفر کرده، در دیدار با فرمانده ارتش این کشور درباره سازوکار اجرای ضمیمه امنیتی توافق میان دولت لبنان، آمریکا و رژیم صهیونیستی رایزنی کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/664645" target="_blank">📅 18:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664644">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqKY9cNyrzlZJx2YtuONvSHwrw9JvIlDK9H0PcLVQ-nEYqzvJtEGiKItr7DFFiNY4BT1dhxHr8_YUjnQ-0yqijGCaaL7mFiYrGlLoj7YodDpZC9xuMErWe_CQPE_bJLYnGSVosZM1qAUb1ejA46w338WM6iK6NRNG6HKTU9pXYtwJXBDVDMmz2jt4fbxka9dvmghx_XdhpFMIExHRfuWv-uS4C6DX7btTP1nCImeEq2Sa9lexkgVJUP_5zUX7umxfVCo-NjIEHH0K8g8mAopO6WU0cxsHzcGj-iJzR4I-INEU_EFVeXDMNdMcEXjXnMDcxQxQMgvsaTp1c23vso2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا برخی از حذف تیم ملی خوشحالند؟!‌ | حذف تیم ملی جامعه را دو پاره کرد | دو روایت از یک شکست
🔹
فوتبال دیگر فقط فوتبال نیست. دیگر نتیجه یک بازی نود دقیقه‌ای فوتبال با عملکرد فردی بازیکن و تاکتیک‌های احتمالی مربی سنجیده نمی‌شود، این ورزش سالهای سال است که تنیده شده به حوزه‌های دیگری.
احساس شما از نتایج بازی‌های ایران چیست؟ کامنت بگذارید
👇
khabarfoori.com/fa/tiny/news-3226626</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/664644" target="_blank">📅 18:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664634">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ocQkoUhPReXIjREIlj2raZpukBZ82iiPjxJSOgQ9p8ir1xFn__chnMbgW2t9Q9Z6IB0gc5rhDHz0h0yZn03synhAXl3XgdALl3bgOxmzWgQOtcZkjf2iE3xhWHlUZ5fcB_jObMiyLS7prZkHAXszphUTRSvZbvCqew4w359xLvq4dYWfNLKtd6YjH8ZmkPvOFtoptN_KOm-Ko8__hX1tCyXmGFZxfFxJDgYScgRQ654vJ_fFRKrtXTrtH4wqgMfsgC4FcsXnE_Vg901t_-TSZcqD9ANxAYAe-K4xFHYTW56PAlUV5snHzwrYlJIp8nimPlwEQZ8HWBlNwFV-PNsqAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LlhKOXAPr11VpS4M80pdoutheLHwUQ_QymUqx8gcPxQrncw2oGS88EZ--plqN9sspTi4EH9H11W0P7J1Ke7RkgKNr6w_ZW-TOG_Ozdl8Yq7i42saBEY6JjMpc3J1WStw2ZIAxCfEEdrAkre-kUU0HzQ25btb38zYXCuY7arA-poVwYuh2kubD8r2GREr9I_CeVGR7uODNMHJgDfj0btccpz-o15Ucof7pyog7Srp15I88GQU06dRcQ8XkIXWynlrtwPHC14lgXMyfvD2OrSK_8adslGyBJY9b_NosPEd9Bqo1qEaXu6tkd45GTOQobKrbtfh9HNRkl7pQDIMHquKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUBG8iAl9Ax7FRgTlkuyplcfGYqOF8gwC9OhrjKQzF_xIIXh9rqw3EG_Q3vffpjOBqGx2XDj-yNmZDLy-N7q03dswRtHJ_h4EKOeLcbY8YNAvPr0p0mT_Nm0vmOSAkZLhLmlPWd34sRbWCtFXvcr7dMKQJaCfZO5TmJJDkadttSWbxv-I5xkHPyus3h7SdL29nSjWTQhhgtXN2WmWrY3yn-7_X7P7skO0RaXaqwqfjU9F6JDNz7iRv9V1Z57zCTdJ0iAQ0n6Ddh1hoF_PRYvFSPUybJPEGkYpeuLJuI1vH2tjaJ30pT-u6ayI27N44EMlne04MbSo7vv1H0K0Ook8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtygKXUUY9RGWL_2YfWzy996X6c_2g6BrjskS3QD0lFEbCQI64XNhhBwmMgTMQlAFP2sxbjmyE5vHnDDpeS7eXIl6qmxs0RkRgppuRgua28F7Gex_6gZdBmCZ327p8bo4a8iVcGJMh_IWhaYr9Ha6n-5ruzJgTy6nOi0nQPUxcY1aXlTvvvRKiYyCO94dzpUXUT7YtbIgbnQMZsmMMYuSZ7-YgoBcWE0_VhfJb0TxvMwkjIgXjVgzquneEVWbbEE4HPATSd81uCHZBE8UzExTc88D8LobYBZ9KAaqbkh5Vy1fRww7ECKEZxbP7KFUDq95Xu8VyplfgFQEHiLMcHUiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLLHwFanN8CdZrfbUyXhSfqS2rSw6iDQ7aloLW51JDZLkZA0t6Npy1V5aMm2OIKXQ4nU92UAUsAKkuvZ2Qo92w5jPm96XvhNvx9Y_AT1H_5gFOYYQV9No-uwTyY55fj9eeI0nzoF9vBocvcvw49qWXyyh2ZuwzGWYRg2wn6MR3LAbbDJeGBG3oRLQu0XHVAh0-CKlWRkW4ZpaNH0xh-9D7n3gAy8x8Pnc-Xwq4AR3xkUSOezsz_Y2cmGAt-WpqmGB1uVEhM0vGo0GsIAXy-KPovmVAdZyekavpAbLGhvDkS7US7XS2ymxgk74XaaJO7NXKnoGEP46m_vAWYS5jsdAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRcC3S6-28X1dcmd2uRFjZs9L0jWW55qC7Ex0mPJzY2mXl1xK8MN9t9gowgNj6lvi8gdeMrd-gj_wqXvrh3YJPl1aQ7L9XiyIfvyy_IBG-asaQEulgtCqSqv20R-TzEpA9bIQnudtWxGFC4dPCumnhwdvMfVRasKFvmic9P_oGQm0xbzykTLYIvhSzw2gbY5RDNZfw-xG5VVkrx5iejWUs-eom8MuF7x2XgwBokf-CJRUsfIHocP-2-UDnJ6kRWixSCOEpXA54WdvEWz6ePCcQHcs8W9pRqNYoynDK82DXkPbX3T94yN8hWjarj8GYTdBYCO9w4GQ0XI3ockPEMt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DljyJWDzMHZsMkWYhstI2rfmWAAkMizbUKI8KLM8G04uP1oICm2y8PAWc-rKV9fX8sZDdcGCesHLl7XZJLfg6CRoFd1Ouw2jiDzOYT94eb6beY1u99eO88_mDnEjTt5SG4whHRhKGu9lQdPOlSmHbqV3hHiHk6OP_41oeurBFI50nkLDnMudGc0DdcxZI9kVZkE8mO_685Yn7INq9-hOQE1lBlDIJ7aMXYhbWgqAvlFGi8lTUvztSXLwGbAZh5wW4QSGxlqZ46ItHZSQoR8FeD1e_Rs6mBhMNgfzr65G1Dn_fYadg_UYLwL2ooraQnGgkRbQytghho44MhpKuB5UAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzdBEiJOPucEpa4EaRRR9KPC1KPdNv_X06AZtln_Za_Gtw4VgB0VFOSGE985gKUMoNnig3Caibj4mrmy-DMAcofRvuyPiVE_q5MV3hDhJWRojscZr4sdbvyxvo9zs-JDzyMC8hikkgKeJJHW24HmrUG3I5YYq7Y4lUDlc_L_F0OwG9Z8Lm_EdmcEkfVLCMRUJmQ9sH2mgod3tRScAQ0mXq4Ie4z7SUmdsj2mB4qXIyBXXOUzCO7JEbgMyfo4ZXex2zorvtGCy-yrVEq13b4OJ_kpk017tpdfy6DpNE9OhD3mPIxl36zGvzSModlcY_iF267F9KL7JnqTZuHEwF7-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bzi_rEg5DkpdURDJG94gaopR3wOiKh9ZqBbKsopEyzi2EsfvoR0aIcLg5dmNYVMkwDbakxJnHbQkS4gAX-SzQ7chCrGHmXw1ihxj6gejU6y0FrPfmdWwZ-JyHY6-ODTTY_w_sTSmdUlB-RfSnCNnWd8HRomWCuOWw1_tQOHoNlCfWwBbd-8gQexwnFe2llpTJlWo8D4zb6PJLOZEi0tttrawyEBjkmIF8JO9x_ngqG6BrTNXFjgBOQBW-b8t3DOnHShx9TmfLtdShu3QzszZXil_O2dU_4G391QzHjHY3kYHFfoNHhyEpFcIbDMD-bajKR38ecjaYNdZEZ1KKnIVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAfH7aAJE7jjoD6Q0wB1BxrXcnsmjsexgQWnbSI0w5YaGWgfbKZSM1kOLo8c5IJS6c_FN8RsRDNMWZ_O4c_NW0bEsBka1pikY0Tq2NtoOTK1aG36ZA3K1JNZnKKQFJ-YPbj87SZcE7sRNz0OaeRvp3lqCAmNKAqKo8EkoAIm9BYcZeWhlT5-ykhudh-gA5jszVWN5eWWTKNDKNH8i1Kow4PKHqvHfdyPU_5-m0iHi8sqYKe0TiXkqo6_C93eYpFJrDbJwLJvj12B8FXcZkMgBp1VkXEcVea0c7gB0Lc9lx66xePEzbkK4iPaqMHi23zc0cgObFzibW1yH_laOmBbXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بخشی از پیام‌های ارسالی مخاطبان خبرفوری در خصوص اختلال اخیر بانک‌های کشور
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/664634" target="_blank">📅 18:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664633">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سخنگوی اتحادیه نانوایان: یارانه آرد نانوایان قطع نشده و فعلا صحبتی درباره قطع آن نیست
امیر کرملو، سخنگوی اتحادیه نانوایان تهران در
#گفتگو
با خبرفوری:
🔹
یارانه آرد قطع نشده و سهمیه آرد در نانوایی‌ها توزیع می‌شود و در آخرین جلسه ما با نمایندگان مجلس و در گزارشی که دوستی، معاون اقتصادی وزیر کشور ‌داد، صحبتی از قطع یارانه نان نشده بود و وی قویاً تکذیب کرد و گفت الان تمام انرژی خود را برای مبارزه با قاچاق آرد محدود کردیم.
🔹
افزایش قیمت اقلام خوراکی و رشد هزینه‌ها، دلیل اصلی درخواست افزایش قیمت نان عنوان شده است. تعداد نانوایی‌ها، به‌ویژه در تهران، بیش از نیاز است و افزایش مجوزها می‌تواند با کاهش میزان پخت هر واحد، به افزایش قیمت نان منجر شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/664633" target="_blank">📅 18:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664628">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRmZHT36rxPdrmIPa5EnY2m7yiwxMTNdSQ4IRz5IO2vosUC88ZQmpavMMhyLs-cXBp8jjSJoQMEiKucVGNdXkDHjVBQ7H61uNXqRZ6t0ZMYG6DCq0Dm3tVWTlRzpNaql3CkFf5GNMZnS1JBNlyHN6uok-wGM6sCpWtc8MC4PU5fEWNnTxYzoA_1vXVLUgVGK3oFcjrNwFLYuZWrQAFEtT7Lh3q6LLHxt5x08_HuaM52LKyrw1bu3ECpeBaeLna28xVUqV15idNRCXdXKJpe9uozfX7lksJnLSFe_CG4sPHYMRvbAn_gl2_x_sdmH4NiqzwtxgmGyrVWDwM7fnJSgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe40c7f4c0.mp4?token=BLZ6YEi7FBcq3pl8KG_896pmbgm83L0sKInemvoebMZVsGScHolF_4b6yC9x15hW6Ve1YTmpYsrDQcCW6DpnXuT-Ngb9pvcdWZROGHFZFYPsJWzBSyuRKaeH-QsdKbgzoOgTHsjVVYfF2hXp2BrpUr1Vs7pIdAi5IEQC5yP4PZ3yE-J9k2OFAD888Fnx5U_HmYMDfQTfZw-f5ZyxLQ8sR5ePHsYN2VGSLQi5Lc4pTvZiUC6NCfBC2f5sH1A7Vxawlt5JdbWyyATmLIYmTFpqsaL7lmfgF-0gHiRzm13yDvM68BjtcKX7oHZ1OgzMOt4Gl7apOusalhKZl-tla6u3eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe40c7f4c0.mp4?token=BLZ6YEi7FBcq3pl8KG_896pmbgm83L0sKInemvoebMZVsGScHolF_4b6yC9x15hW6Ve1YTmpYsrDQcCW6DpnXuT-Ngb9pvcdWZROGHFZFYPsJWzBSyuRKaeH-QsdKbgzoOgTHsjVVYfF2hXp2BrpUr1Vs7pIdAi5IEQC5yP4PZ3yE-J9k2OFAD888Fnx5U_HmYMDfQTfZw-f5ZyxLQ8sR5ePHsYN2VGSLQi5Lc4pTvZiUC6NCfBC2f5sH1A7Vxawlt5JdbWyyATmLIYmTFpqsaL7lmfgF-0gHiRzm13yDvM68BjtcKX7oHZ1OgzMOt4Gl7apOusalhKZl-tla6u3eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت نماینده عراقی؛ کشف حجم بالای دلار در خانه
🔹
نیروهای ویژه ارتش عراق با یورش به منزل «علیا النصیف» نماینده پارلمان، او را بازداشت کردند. همچنین گزارش‌هایی از کشف مقادیر قابل توجه دلار در محل منتشر شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/664628" target="_blank">📅 18:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664627">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
دستور پزشکیان؛ برق صنایع به هیچ عنوان قطع نشود  آرش نجفی، رییس کمیسیون انرژی اتاق بازرگانی ایران در #گفتگو با خبرفوری:
🔹
مدیر عامل توانیر هفته گذشته گزارشی را به دبیرخانه شورای سه قوا ارائه کرد مبنی بر اینکه امسال در زمان‌های پیک ۱۲ هزار مگاوات کسری برق…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/664627" target="_blank">📅 18:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664626">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuJ7LoxCFre-7x9tKLLsURCB7kv6lJioi88ljwMlFB1jxYej5CTzocADsPU5bGnsJmL1FZ7mJOp0DMCErwuuHCVmsbw8Um9-v9euBZzf65Xd5C0jydMBt7OuETJuQHgubvS9wK8jdhz1iV9HAlxfXt4oZNSaZaBRn0oLquOs9CGjpOF8bGiBweo97lbrE4oHtncjGFn91hZmpHp1NG9GI302xBALWCL8qagkK8NXj_v1AMHTYyBNLdRp69xRoJyw5kW6qTkgRXAZRJDdnNxLr7qpod-4tWiQ7KudQ79MDhH5RpN4M4ETl-_oA-Sy1KRK2LNfqULAsjHD3dcCCwpoLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییرات ارزش طلای کاپ جام‌جهانی
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/664626" target="_blank">📅 18:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664614">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
مقام وزارت خارجه آمریکا: نشست تلفنی درباره گفت‌وگوهای ایران در کنگره
یک مقام وزارت خارجه آمریکا به الجزیره:
🔹
روبیو و ویتکوف امروز درباره آخرین تحولات مرتبط با مذاکرات با ایران، جلسه توجیهی تلفنی با اعضای کنگره برگزار می‌کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/664614" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664613">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljNQ1Tb2XljM4xPPOuwURbqd_ArLfMng9f7xwHHt19-IPwjybHC2Uhc7TK7npo0RIzR590eSwfc18lcMsW1evkndmp-xRtskAiP2f0v6ih26SzdTFOigJ6N_WBVf84yTBX2G_QkoY02OAcrfyzFnW4Bx8XDNBUfcTJXAIdYfiXBWIrbXX75nqSfuF1Ki09dN7BYCWjegsU-A1RMdc5qSY7ZSC8zmaw88JIjmaloFGP5BSyRnRMDZTomJ500746z32hOfGRW7lzcKfJ48qhqJzBx2hCNBUdlceNq5GYlx6eNWLVSvjqgbFTmRHHzVn_Yq7xAZqLDohOSGW8RfXb7S_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«کوسه جن»؛ هیولای جدید اقیانوس های تاریک / دانشمندان با دیدن این حیوان وحشت کردند
🔹
کوسه گابلین که گاهی «فسیل زنده» نامیده می شود، تنها گونه بازمانده از خانواده ای از کوسه – ماهی ها است و قدمت حیاتش به حدود ۱۲۵ میلیون سال قبل می رسد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3226644</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/664613" target="_blank">📅 18:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664612">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22dc59eb64.mp4?token=CRcgtPhlbRa6z5nl3GJSMlwEC1I2z4ihMkBsGLD_8ulI8QW2nYh4vQaGLPHFPuNgVzrJDWXTsjX7WafK3cWEmmiTMh0twbXru4vbQmieb9rNPRc6qx-rA5rnKSK7uwaniCSaO0dZs-EyLM4M2d66yw3TTVl4k7F1irsbYBnngbov_5MAC_erriCmiTdByiergOZIv_AZ4thg6vQYQdBevg1t4KleK58FE5LS-mpOgXZUH5e5MljCT0jlN0dqQ_canq60OVCuLfshpE0LInVDURS0CsyZMUZVonpIJx6dm5LZQy7AFKVmETY9h4FPgxvo-TCwf_BS9UiHPT2Vr4X-PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22dc59eb64.mp4?token=CRcgtPhlbRa6z5nl3GJSMlwEC1I2z4ihMkBsGLD_8ulI8QW2nYh4vQaGLPHFPuNgVzrJDWXTsjX7WafK3cWEmmiTMh0twbXru4vbQmieb9rNPRc6qx-rA5rnKSK7uwaniCSaO0dZs-EyLM4M2d66yw3TTVl4k7F1irsbYBnngbov_5MAC_erriCmiTdByiergOZIv_AZ4thg6vQYQdBevg1t4KleK58FE5LS-mpOgXZUH5e5MljCT0jlN0dqQ_canq60OVCuLfshpE0LInVDURS0CsyZMUZVonpIJx6dm5LZQy7AFKVmETY9h4FPgxvo-TCwf_BS9UiHPT2Vr4X-PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کتاب «میان‌وعده امروز» با طراحی آینه‌ای و تکنیک سه‌بعدی، تصاویری خلاقانه خلق می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/664612" target="_blank">📅 18:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664611">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nijHrC0frGRpy_xCFkRjg4cI6T3sMLDmMaPTsW3uHqTfX9vKEtQITy2KwhmvbGSif6mUGZ-_hsUfZp0cHjtiRQn2PfMleASmXmJxDBQsDSdK_hLOaYfjIVu0vyAaXf5bcul5qteM8Fc13zYQui9iiUJ1BIbCGM2kgSgnDcDzcjiQDDDZKsDX51Upaf0xDvnD2zisM9O0a-nCfRKfWgE0btV8uCq4tejGhyRyuA5GWXKS5iyJST6zqlkH0JmSZUX-q0TeieE2IoSmQ9nYpPGF8WXQu00ZZQg8aX46khXHQsPvrixic9FOoRJOoR2ZzPx6THq72WeFqHUe6CiUtbWPbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهشتی؛ اندیشه‌ای ماندگار
🔹
سید محمد حسینی بهشتی را بیشتر با نقش او در انقلاب اسلامی و بنیان‌گذاری ساختار نوین قوه قضائیه می‌شناسند؛ اما کمتر کسی می‌داند که او سال‌ها در آلمان به زبان آلمانی با دانشجویان و کشیشان مناظره می‌کرد و اندیشمند اسلامی روشن‌اندیش…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/664611" target="_blank">📅 18:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664610">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
قطر فعالیت‌های دریایی را موقتاً متوقف کرد
وزارت راه و ترابری قطر:
🔹
برای حفظ ایمنی عمومی، تمامی فعالیت‌های دریایی در این کشور تا اطلاع ثانوی متوقف شده و از مالکان شناورها خواسته شده موقتاً از تردد در دریا خودداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/664610" target="_blank">📅 17:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664607">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEhtq4TVscvsVm8W4H4xp5d_W9rE0Qt3Xb0XIqDjqh8kl_s9nThMTEQLiUAIjrkf520kQZBWSvTzzaI1dwjP0Tx-KQQ9lcPICypw_97o8RcpW6NiJUCYYTm0sfVYohG7Mx25j0q1f5ZLr69J5VbhF3mtx2W67PDwAvTxDNp8v7m36Dz3yAmTVpIBXqhGcTGAvPtRSzxFSZEBQOuQBKucX6CCWKHp3AseAlzlqeKSFYlRNNntHAO0Svh1gC0osxo74FKVJG9Q96LmEwJaPnItwLJYQklHSc2tItuv39vwvcPeUZX6_ZnAK6vdwTH6L7Gl0RwGqcQnyTX-oqwYlcmW0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واضح‌ترین تصویر تاریخ از کهکشان راه شیری ثبت شد
🔹
تلسکوپ فضایی «اقلیدس» متعلق به آژانس فضایی اروپا (ESA) با ثبت یک موزاییک کم‌سابقه، باکیفیت‌ترین و پرجزئیات‌ترین تصویر از راه شیری را منتشر کرد که در آن حدود ۶۰ میلیون ستاره قابل مشاهده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/664607" target="_blank">📅 17:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664606">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
تنها ۲۵ درصد آمریکایی‌ها جنگ با ایران را ارزشمند می‌دانند
🔹
نتایج تازه‌ترین نظرسنجی مشترک رویترز و ایپسوس نشان می‌دهد تنها یک‌چهارم آمریکایی‌ها معتقدند جنگ با ایران ارزش هزینه‌های آن را داشته است. این در حالی است که نگرانی‌ها درباره دوام آتش‌بس میان تهران و واشنگتن رو به افزایش است.
🔹
بر اساس این نظرسنجی، توافق موقت اعلام‌ شده از سوی ترامپ برای پایان دادن به درگیری‌ها، حتی در میان بخشی از حامیان او نیز با تردید و عدم اجماع مواجه شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/664606" target="_blank">📅 17:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664605">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
افشای تخلف ارزی ۱۵۷ میلیون یورویی در شرکت پگاه
🔹
بر اساس سندی که به دست خبرنگاران رسیده، گروه صنایع شیر ایران (پگاه) از سال ۱۳۹۸ تا ۱۴۰۳ بیش از ۱۵۷ میلیون یورو ارز حاصل از صادرات را به چرخه رسمی بازنگردانده است.
🔹
این شرکت زیرمجموعه صندوق بازنشستگی کشوری و وابسته به وزارت کار است و حدود ۳۵ درصد بازار لبنیات کشور را در اختیار دارد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/664605" target="_blank">📅 17:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664604">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM598rEquyI9ZsGT9VYoNhfPL-t621u2VrbXmRP-R1AN9MU877T5NRhojBhusC-fyEhDNdB7xOy0EJcW7XIcc1e9OX36-Qmat6K0jQSO-bFynzvBvdNWuWn5GiAxNVsfvjGpRINVMq6zPd1akh1Z4fpRhTUpjU14JbzNp_VtQrMQlXyOpnBuY0lCPKjETtetOxv0rv-ykfNa_RR-3zE9QNraDZyVYu8igc_3X4Rc322VW8LRnQpH-qe5hAjJaGe5jEhfvtuRntF79Mf3q3x-2_e2r3eWjIHs2Mw5gZjdf3ad028qRZnDuYlulxjB6K53LeBQzNeG1Rc7FpS16GY0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | اختلال در خدمات بانکی
🔹
اگر در ساعات یا روزهای اخیر به‌دلیل اختلال در خدمات بانکی با مشکل مواجه شده‌اید، تجربه خود را برای خبرفوری ارسال کنید.
🔹
اگر انتقال وجه انجام نشده، کارت بانکی‌تان دچار مشکل شده، از خودپردازها یا همراه‌بانک نتوانسته‌اید استفاده کنید یا هر اختلال دیگری را تجربه کرده‌اید، جزئیات را در کامنت‌ها یا دایرکت برای ما بنویسید.
🔹
نام بانک، نوع مشکل و اینکه آیا تاکنون برطرف شده یا خیر را هم ذکر کنید. روایت‌های شما را پیگیری و منتشر خواهیم کرد.
🔸
تجربه خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/664604" target="_blank">📅 17:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664603">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
جزئیاتی از نامه ترامپ به رهبر شهید درباره حمله نظامی به ایران
در کتاب جنجالی رژیم چنج که این هفته منتشر شد آمده است:
🔹
به گفته یکی از مقامات ارشد دولت آمریکا، ترامپ کاملاً در تصمیم خود برای دستیابی به یک توافق با ایران جدی بود و این، برخلاف آنچه بعدها برخی ادعا کردند، یک فریب یا تاکتیک ظاهری نبود. ترامپ واقعاً اطمینان داشت که می‌تواند به توافق برسد.
🔹
ترامپ پیش‌تر به اعضای تیمش گفته بود که می‌خواهد نامه‌ای مستقیماً برای آیت‌ الله سید علی خامنه‌ای ارسال کند. ویتکاف و والتز پیش‌نویس اولیه را تهیه کردند.
🔹
خواسته‌ های مطرح‌شده در نامه صریح بود: مذاکره مستقیم درباره برنامه هسته‌ای، همراه با تعیین ضرب‌ الاجلی برای رسیدن به توافق. بدون غنی‌ سازی. بدون حرکت به سمت ساخت سلاح هسته‌ای. بدون موشک‌ های دوربرد و دسترسی کامل بازرسان به تأسیسات
🔹
ترامپ امیدوار بود این مسئله به‌صورت مسالمت آمیز حل شود؛ اما همان‌ طور که در نامه به‌ روشنی آمده بود، در غیر این صورت اتفاقات بسیار بدی ممکن بود رخ دهد.
🔹
ترامپ سپس پیش‌نویس را برداشت و تغییرات و عبارت‌ های مورد علاقه خود را به آن افزود تا به گفته خودش نامه زیبا شود. او با افتخار درباره این نامه برای اعضای کابینه و کارکنانش صحبت می‌کرد و گاهی آن را برای برخی از مهمانان منتخب در دفتر بیضی با صدای بلند می‌خواند.
🔹
وقتی مطمئن شد که متن دقیقاً همان چیزی است که می‌خواهد، از ویتکاف خواست به ابوظبی پرواز کند و نامه را شخصاً به رئیس‌ امارات متحده عربی تحویل دهد تا او ترتیبی دهد که نامه به دست آیت‌ الله خامنه‌ای برسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/664603" target="_blank">📅 17:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664602">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0W-G2dnHy90UXLNF82lR8HdLqcvHGw3Icclj0UPVtIjlmdbZbw3HF171HzZrS4oyz-FyFp34l0wR8g2dw5_2ZQIgOhAgd3roZAUp4yQaTOgbIzERh478eh34JstXFanAxummgEuF_2zPl6cOiE43kJjeA1ZOfv0wgPZ5ZoxD1e9Bm6d7w-w6qIN_vTHr287OmHYelmx24iNpMQYWhlT8qrl-7__gOTBTGfrJHdXIYDurrbV2JdYri2v6fC3A9z0B9uJNw2Iny4lda_dfyGO2vB3hKcwxrtNgYHOtSim2denym7rzv-I03O_tW8K7TYDgy-uCRU_J2gglql1Nl3L5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای برخی تحلیلگران درباره پیش‌بینی رویدادها در جلد اکونومیست
🔹
برخی تحلیلگران مدعی‌اند تصاویر مندرج در جلد سالانه اکونومیست به ۱۲ ماه سال تقسیم می‌شود و به رویدادهایی مانند بازداشت مادورو در دسامبر، آغاز جنگ آمریکا و ایران در مارس و برگزاری جام جهانی در ژوئن اشاره دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/664602" target="_blank">📅 17:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664601">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk9Fy86jkCGN1w_RiKxBW8jyg34NekXS3lS9qiakEIGPf8d4FVAsDvIrJapyZy-BPoKrkJWuJK3t5BisS2mwdsO1ZN9uZAeNcqSqsCb1Kh9x1x3zm9FeW3I-n-k-Mapz6Q28E5cbRB4xmw1s0deJ084xA4Z-Ul26gM4wjYPtNWchETTkHPyuLJn2wmvcQ4gwaiFsyA6yny6QYr1cj_gSZcqwlI9f-fCWlLqz-3HIzsc_8dHkuHC4oLd0_Xsk5Eu9zdoD0_vMLNRF9Ved1WgDhmzt9TcuN1OKhPpbhbqIXIYZWQ8pnN5tQBxwYuCkzKO4e7GSNqQoiluGoqPkmWR9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک شهر برای جذب نیروی «بانکدار» آزمون استخدامی برگزار می‌کند
🔹
بانک شهر به‌منظور تأمین بخشی از نیروی انسانی مورد نیاز خود، از میان متقاضیان واجد شرایط، در رده شغلی «بانکدار» نیرو جذب می‌کند.
🔹
به گزارش روابط عمومی بانک شهر، بر این اساس، فرآیند جذب از طریق برگزاری آزمون کتبی و با همکاری مرکز سنجش دانشگاه آزاد اسلامی انجام خواهد شد و متقاضیان واجد شرایط، اعم از زن و مرد، می‌توانند در این آزمون شرکت کنند.
🔹
داوطلبانی که در آزمون کتبی حد نصاب لازم را کسب کنند، به مصاحبه‌های تخصصی و عمومی دعوت خواهند شد. در صورت موفقیت در مراحل ارزیابی، فرآیند به‌کارگیری آنان مطابق ضوابط، مقررات و آیین‌نامه‌های داخلی بانک شهر انجام می‌شود.
🔹
بر اساس شرایط اعلام‌شده، دارندگان مدرک کارشناسی با حداکثر ۲۸ سال سن و دارندگان مدرک کارشناسی ارشد با حداکثر ۳۰ سال سن (مدت خدمت سربازی آقایان به سقف سنی اضافه می شود) و همچنین داوطلبان صرفا دارای سابقه بانکی با حداکثر ۴۰ سال سن، مجاز به شرکت در این آزمون هستند.
🔹
متقاضیان برای اطلاع از شرایط ثبت‌نام و جزئیات آزمون می‌توانند از روز سه‌شنبه ۹ تیرماه به پایگاه اینترنتی مرکز سنجش دانشگاه آزاد اسلامی به نشانی:
https://azmoon.org
مراجعه کنند. همچنین این آزمون استخدامی در تاریخ 9 مردادماه برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/664601" target="_blank">📅 17:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664598">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d49d0083.mp4?token=cP2VE3JPvr4PKNC13kUK2iPqkhd8m3x46G3AlBueTsF2-o6Uj5lKOZ7KMkAm394yD4PZXOfAaEtdArB14zOD_EbjeB1kHEA6SSHBzEhbL2SMSoes4cmbNc8REyxlSliHx04quKfFw0nQH40kfjBUFxKh_DTKbLHQH0CIH-eTvv2S_k8UAW_NIim7YNRpGK11vjR3WohNSDfCb6_wFLklJ5Ucudsj1wfZxF6WzNNzq7w0M-wj90vUFQGPDzZzPsr3KMiH02HXgkdq1pcwq-H9QscR9QyW2LEPIT_ktLoR0HJB02yCx4yCN3Te0LPJwGkuc2GWQwpILhyrfXFJZY9AVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d49d0083.mp4?token=cP2VE3JPvr4PKNC13kUK2iPqkhd8m3x46G3AlBueTsF2-o6Uj5lKOZ7KMkAm394yD4PZXOfAaEtdArB14zOD_EbjeB1kHEA6SSHBzEhbL2SMSoes4cmbNc8REyxlSliHx04quKfFw0nQH40kfjBUFxKh_DTKbLHQH0CIH-eTvv2S_k8UAW_NIim7YNRpGK11vjR3WohNSDfCb6_wFLklJ5Ucudsj1wfZxF6WzNNzq7w0M-wj90vUFQGPDzZzPsr3KMiH02HXgkdq1pcwq-H9QscR9QyW2LEPIT_ktLoR0HJB02yCx4yCN3Te0LPJwGkuc2GWQwpILhyrfXFJZY9AVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از گردباد عجیب در طبس
#اخبار_خراسان_جنوبی
در فضای مجازی
👇
@akhbarkhorasanjonubi</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/664598" target="_blank">📅 17:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664597">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
اظهارنظر وزیر خارجه عمان درباره دریانوردی در تنگه هرمز
وزیر امور خارجه عمان:
🔹
سلطنت عمان از اعمال عوارض بر کشتی‌های مطابق با قوانین بین‌المللی، حمایت نمی‌کند؛ اما احتمالا درباره سازوکارهای مربوط به خدمات دریایی، مانند افزایش ایمنی ناوبری و مقابله با آلودگی بحثهایی صورت خواهد گرفت.
🔹
سلطنت عمان مشتاق است که دریانوردی در تنگه هرمز برای همه ایمن و آزاد باقی بماند و طبق یادداشت تفاهم، تضمین خالی بودن تنگه از هرگونه خطر مین، بر عهده ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/664597" target="_blank">📅 17:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664592">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F6Jzw04QA9zu4e9n23M90WYH5qIzD7MbFdZLxkzfcBHTK3I9PwDRv_R6z_VenEPpfOtxzUDOmStviMaiWIt6Htkj41SopojUCyKZCXw9sWcI5BZu8B7YZ_FzzXICdFGz0hY6tF3ewVmfr39Q62KMsWpxCo0y5NpyM6ArDJ2TeE3phivwPY568iJ5MvZ2zbyBxOV_d7DDFQCfNjZae4ge8Z2RF8KUMr8HxNtfxKHhuEUx2XmQhYJeQCicET_PQSrjCbz9gR-smss6tgjYj4JW0JvXMxKjprC_ctA-ew599fJ1KreQiVmI7DF9RI99RNzZTI7v3WK6Fqm5z31kqvhnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUATcCCW66lbop-eiPEWZ9Kln7Xp15JXqD-T2RPqoC2_k1eon3xISWIb8_5N5LMfITH-6l05jwl81G4VVbC4h7crP6oyItOAel4bnN9B_Iw8jTDeGv45Eya20GxMdiy2PnEa7crELHB0e9xFdQ2DvjvePvVelJB61urQxlBskWs5R4PQt_F-yswa9y5ApY4PkgYCB0aJN3RLxEZkk62km04hYnQoAe_08TjHzI_KLJ3NCkOIrhgbXWlxriympsamygasesBvOc7C6clZAv1Yd5XFddVuhJdd3rTI0NeznbP4zVeLqA-Ma6mfATVLwXUyiFdoka2Q9oCs_nVnUripdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAIF7vNStojVdFxaZjWIRAsjMstd1Xx-ZwtM3t-chdXzsRxopToXCGmcnYQN6Nx4C_Vaqq4quEvcqBWyRjTHrrIccLKRjDr7mx2mj8IgW8sokznCXZKRcilEzOP4aqy5moYy5aP4u62O0M-8lJczXlyF9jgFoVjuI6QsqC5sQ4VwRuB4eYrGHLP6Wk3tPYxhcU_t-pDNVRiFUNF8D51HnuH02sYZyYFl3IIGFv4ZXV35x_dkHIX_CJ92A5GM5KpaQ7yyKzA807e7fgUby4HTkhgGnkuV863FmPfAyolfbQtnISye4ukflByL3_WJB138oM13mZknWVXK98vFLM3Bgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ظهور «ماه توت‌فرنگی» سرخ در آسمان شامگاه امشب
🔹
ماه کامل ژوئن (ماه توت‌فرنگی) امشب با رنگ سرخ و صورتی در نزدیکی افق طلوع می‌کند؛ این پدیده کم‌ارتفاع که هر ۱۸ سال به اوج خود می‌رسد، حدود ۲۰ تا ۳۰ دقیقه در این رنگ باقی خواهد ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/664592" target="_blank">📅 16:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664591">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
برگزاری نخستین نشست کمیته مشترک عمان و ایران درباره تنگه هرمز
وزارت خارجه عمان:
🔹
کمیته مشترک عمانی ـ ایرانی نخستین نشست خود درباره تنگه هرمز را در مسقط برگزار کرد.
🔹
دو طرف دیدگاه‌ها درباره مدیریت آینده تنگه را بررسی و راه‌های تقویت هماهنگی در موضوعات مرتبط با تنگه هرمز را مطرح کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/664591" target="_blank">📅 16:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664590">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نقدعلی: در صورت بازگشایی مجلس؛ استیضاح وزیر نیرو در دستور کار است
محمدتقی نقدعلی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
قبل از دفاع مقدس، وزیر نیرو به دلیل مدیریت منابع آبی مورد نقد جدی بود و استیضاح او در دستور کار بود.
🔹
مجلس بدون دلیل امروز بسته شده است، لذا اگر مجلس باز شود، استیضاح برخی وزیران از جمله وزیر نیرو در دستور کار است.
@TV_Fori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/664590" target="_blank">📅 16:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664589">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDGf2XhjLyP-ib4fRbvnSnZSocIO59nOD6UDUkNxiyFO4H_SOEpBWPUFEaLA4WZkypOi6iaa0SwxhLo1UnOUi-Z8BTdj5HfbaAKsD_QCrG2bd901LasSwepRIvchAcu9xZTDs1TM0hmznKDu5PnEDqNQD-fYcI1AMU7xOx7plgaaBA96zWcL5oty8cn38bUh0mFixIJbq4jLK414w8Ovy29uQ_1UbsHVjsPAIeg12KQkx-Kmu4691WCNZkgG0nkmuqaR6MZQeAinzRQmBMUls76XDF5F64Ze3Si3PLDAbumiiCV5ncwg-zw-fPSK7yeZq_eE-yO-AETRzSqsiy0N9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فشار ترامپ بر سوریه برای مقابله با حزب‌الله | پیام محرمانه دمشق به لبنان | دلیل پنهان فشار آمریکا چیست؟
🔹
در حالی که دونالد ترامپ، رئیس‌جمهور آمریکا، خواستار ایفای نقش مستقیم سوریه برای مقابله با حزب‌الله لبنان شده است، مقام‌های دمشق تلاش می‌کنند به دولت…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/664589" target="_blank">📅 16:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664588">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9487e29f6.mp4?token=PYRVT3ad3kIGTjaqTPe62jcQ1Zt7WgeGY5kfr8m5oPEUOzu7H2V4MK4wxmAbTraMCJ-mwjXAZXzWBF3vW6tu_nkkYajS4vKJL9ZPa_ANA_d94mfjve2ncs471sFJJO2VCVNVtB8SRixI1uSpAbYPq2C6EScGpRy1hDdKrQjkiQn2kl1IuBWwEzCrh4dMqEoA1lJGJLLw0JTf1LaRpemhpW2iSS7SpxH4YYBj3NCP30_RLnKcbEUjoCJai3ZRcRxKs-FBdQfo8OWFYSoce515SpOVBAh5filGENlIyHrFX6mhYERujhYIShzjwFR9UrzGrQkjcDpzxRIQb464E-Rqrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9487e29f6.mp4?token=PYRVT3ad3kIGTjaqTPe62jcQ1Zt7WgeGY5kfr8m5oPEUOzu7H2V4MK4wxmAbTraMCJ-mwjXAZXzWBF3vW6tu_nkkYajS4vKJL9ZPa_ANA_d94mfjve2ncs471sFJJO2VCVNVtB8SRixI1uSpAbYPq2C6EScGpRy1hDdKrQjkiQn2kl1IuBWwEzCrh4dMqEoA1lJGJLLw0JTf1LaRpemhpW2iSS7SpxH4YYBj3NCP30_RLnKcbEUjoCJai3ZRcRxKs-FBdQfo8OWFYSoce515SpOVBAh5filGENlIyHrFX6mhYERujhYIShzjwFR9UrzGrQkjcDpzxRIQb464E-Rqrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این کلیپ میتونه نقشه‌ راه برای زندگیتون باشه، اول تو حرکت کن، بعد معجزه را ببین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/664588" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664587">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esA9x42CIjtq6i_lND07QIYokRFu6DpvmTqDSztOhKTSLL1-H7R2mkPwy6dKljVv_8t8jZaruMywnfrJkwGcfZRXKyJWrkV-nUs1Lm8O_KoCbSa_tnCzLUSHJgWW7PJEnAauqmxd3iQLSLhRreLoVbChL3HzlRzoTLc_s8VCh0IoKp2ngjTOrkTfGAmwtcZ1bCSQ6XOTiYi4i_bIxvt3ts1iYJg1J9J-drUw7PCgCMHJAToi1B5p90eeKcvNfeKHV8Y0A1IhI7nI9LJ1waSLchG2pM4HfmOrMUiyttTsuuJdTGuZsLMyoOLVXv-TykAydMsKW5w6md9vj9r8Cd2MlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار تکان‌دهنده مصرف پلاستیک؛ سهم تو چقدر است؟
🔹
هر نفر، هر سال، صدها پلاستیک؛ اما تغییر فقط با یک انتخاب آغاز می‌شود  شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک @Ertebat_baforii</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/664587" target="_blank">📅 16:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664586">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/He9DFHYy8NaIRiZxDkgOqLzQVPbkaYMOKCI09K8U_HYgPI-LfupHggZaTKrFfUkEfjQQyP1Dh17o5sbwZ_dSsWVy4UhjUZzWBTUq84z7s3HMwOYL2-ZUJJFNmRBJr5uAdUr6UvR-NY8gFRGPAotMmWnV6VwjeU0BuECh0MhIb2Y80x2c1SUwFG_p2HHyTdO6FzHktqo9wUkrcUFXiTAUFARTfWn1yEdJ4TOrBOOl9DypFsjq7XyHpjmtsojSTCK2kzdvodeHzePRmqLbF22KZrxuvZ-82bqZ9IpD6JfgFlyQwk-cpSR5jrLmR69zI2Vgwh3BaFhIYg31H9RUKfNSFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه تکنیک ساده برای تقویت هوش مالی #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/664586" target="_blank">📅 16:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664584">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سخنگوی کاخ سفید: استیو ویتکاف و جرد کوشنر برای برگزاری مذاکرات سطح‌بالا راهی دوحه خواهند شد
🔹
همزمان و در حاشیه این مذاکرات سطح‌بالا، گفت‌وگوهای فنی نیز برگزار خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/664584" target="_blank">📅 16:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664582">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
رویترز: توافق برای آزادسازی ۶ میلیارد دلار از دارایی‌های ایران نزدیک است
رویترز به نقل از منابع آگاه:
🔹
تیم‌های فنی ایران و آمریکا برای بررسی اجرای تفاهم‌نامه اسلام‌آباد به‌زودی در دوحه دیدار می‌کنند.
🔹
به گفته یک منبع ارشد ایرانی، این نشست با محور مدیریت تنگه هرمز و کاهش تنش‌ها برگزار می‌شود و دوحه و تهران در مراحل پایانی توافق بر سر جزئیات آزادسازی نخستین ۶ میلیارد دلار از دارایی‌های مسدودشده ایران هستند که در دو مرحله آزاد خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/664582" target="_blank">📅 15:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664581">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فروش آزاد داروهای غیرمجاز و اعتیاد‌آور در عطاری‌ها و سوپرمارکت‌ها!
محمود طاهری، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
متأسفانه حتی یک‌سوم نظارتی که روی داروخانه‌ها وجود دارد، روی عطاری‌ها نیست و برخی عطاری‌ها داروهای ترکیبی غیرمجاز تهیه می‌کنند و به دلیل عدم نظارت، مشتری‌های خاص خود را دارند.
🔹
نه تنها عطاری‌ها بلکه در بعضی سوپرمارکت‌ها نیز، اقلامی به عنوان شربت‌های تقویتی غیرمجاز دیده می‌شود که فروش آن‌ها در داروخانه مجاز نیست.
🔹
برخی از این داروهای غیرمجاز به کلیه‌ها آسیب می‌زنند و بعضی از آن‌ها وابستگی ایجاد می‌کنند و مصرف‌کننده راغب می‌شود دوباره از آن‌ها استفاده کند و تنها اطلاع‌رسانی کافی نیست. مشکل اصلی، ضعف نظارت و نبود برخورد قانونی مؤثر است.
@TV_Fori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/664581" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664580">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOW5biuwyOlFKFvpLVhWyPn4e0sxA2-rsvNuK9VOWfSYnipPgFp_Uxc2Y5dBPk-Nu4F_-j-pjB_yGim5x5U_v4hGWE2pPuBlHDWvHDQQ-QYMUPnh2asIloF_R59D80OiH267SpNTJR9VEYsyEP9o6b5tRkPK-yRrW_-HtmHp6h3BxEVcdZwoQVu5Ducmo9fzgbdlYauGkBCcEnCuigQ0GFMffJsknkcp-jusDMgQ8uLv7rgKCIlo8tcO8vWFZtP_WUfmEjZziHx10aBXbHACJ7vD-fNKRzzTBq1c5Yus4ej-cpmvivlTsbTfslV5DjSYmmUJMQwM4KpR7vjkcWHKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان اولین دیدار یک‌شانزدهم نهایی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/664580" target="_blank">📅 15:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664579">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fdf4ba5ee.mp4?token=kZq3yazbJxejXZbFTcyedwHskryFWZEXL4o85CAJzgV5_yh5WJB1AWY67LQLM8jtZQaEioaY0_GR4_4WbjY4GlGKLSDq9llUr_iA4IzNsHXMW6TU7ZtDeSE_8vZDj4IUYdVda2Wlh4MEF0gqlrhVZo5qPjIRq-4R_mamPoGkq92VvU5ar-Co806in8CGE9qXXLa6WBnF02PrVaY2Q-OYHqyyYzVv00hWBfO-jH9p9iL_vDK5pgT3cUZUvh7PIHAfFYVEWAumU9FfXfPxVGfdYI2eGt-5Jwc0djQTGgw0T9PCOhJmM_X1UEE1OluFe_DxDinGTmeUIg6lS6EsVdYhbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fdf4ba5ee.mp4?token=kZq3yazbJxejXZbFTcyedwHskryFWZEXL4o85CAJzgV5_yh5WJB1AWY67LQLM8jtZQaEioaY0_GR4_4WbjY4GlGKLSDq9llUr_iA4IzNsHXMW6TU7ZtDeSE_8vZDj4IUYdVda2Wlh4MEF0gqlrhVZo5qPjIRq-4R_mamPoGkq92VvU5ar-Co806in8CGE9qXXLa6WBnF02PrVaY2Q-OYHqyyYzVv00hWBfO-jH9p9iL_vDK5pgT3cUZUvh7PIHAfFYVEWAumU9FfXfPxVGfdYI2eGt-5Jwc0djQTGgw0T9PCOhJmM_X1UEE1OluFe_DxDinGTmeUIg6lS6EsVdYhbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار نیروی دریایی سپاه به شناورها در تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/664579" target="_blank">📅 15:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664576">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi0Pp9DmjeQ5OIpJHodZHodfR3x7z91Lv1kgGPrOPxQFRPdtsTR6AzkGQjS5Npr6lDP3_t-_EBoOmhVYX5tuv7eBUj5Zie303Bn1F3biO2RRB8HHkALCCo3sRot4H-ZCbcDHoIEhJ7-LiuJUQoCIjLYsnewNbrkfa7umkVuO3r2BudJmse0oM2ygJAkT9JDcXahUhmxJRMaIgeRBHr4-DNiloTOdwBaduPJNfIyR34g0Yvn0B9kmNhhRb23Uqnsf642tOdsBzlU0cbQcN_cTLp-BQqf7rRxfGcVL1Arid7DISM5ZUmnePZEsvCT6UCnZInOshX5xxLY_dssNvD9AMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جهش ۱۲۲ درصدی پرداخت تسهیلات ازدواج و فرزندآوری بانک کشاورزی در خردادماه
🔻
تسهیلات قرض‌الحسنهٔ ازدواج و فرزندآوری پرداخت‌شده توسط بانک کشاورزی، طی خردادماه سال جاری نسبت به پایان اردیبهشت، با جهش ۱۲۲ درصدی در مبلغ و رشد ۱۲۷ درصدی در تعداد همراه بود.
🔻
شعب این بانک در سراسر کشور با هدف تسهیل شرایط ازدواج، تحکیم بنیان خانواده و جوانی جمعیت، تا پایان خردادماه سال جاری در مجموع ۲۰ هزار و ۲۹۵ میلیارد ریال تسهیلات قرض‌الحسنهٔ ازدواج و فرزندآوری به ۸ هزار و ۱۲۳ نفر از متقاضیان واجد شرایط پرداخت کرده‌اند. این آمار در پایان اردیبهشت‌ماه سال جاری معادل پرداخت ۹ هزار و ۱۲۷ میلیارد ریال به ۳ هزار و ۵۷۹ نفر بود.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/664576" target="_blank">📅 15:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664575">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryxR3r9Ie6hV1iyorD9W07zTZktSQngWPOiojtpd2Ngbr_j_RIXTCqmiZEDZ3kjBJQUB-QCe75NFzCX0Jl7j-DrncIdMmGOFWO__j0gxQcUAbf-mtjpT2DEvkO7NH6RM4NzDty2ve7r128deBn-lTxw5KqprfvNSaEUQ4yNL922yzNGsKhonb3-O8ebByDDBCMS1b6a-HV5pSewhaXnqpkyRr-WT_1rHF5Ndm1AhbxTQnxnwZw6XnvCGR_M9pKZanAJR1iWZIDA7DNw8B6FCfHZx2Dmy0tYUQJmpfBIhJ3C3WfLddqb65OvEi8d8IWFXWaqkWEjPiVoODGR1vB_aFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشاگری کاربران از رنگ‌های احتمالی آیفون ۱۸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/664575" target="_blank">📅 15:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664574">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ناکامی وزارت نیرو در انتقال آب ارس به تبریز
علیرضا نوین، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
مشکل کمبود انرژی مربوط به امسال نیست و سابقه چندین ساله دارد و باید نیروگاه‌‌های اتمی هسته‌ای افزایش می‌یافت ولی متاسفانه نشد.
🔹
وزارت نیرو در انتقال آب ارس به تبریز ناکام مانده و علی‌رغم تعهدات و وعده‌ها می‌گویند باید اعتبار را برنامه و بودجه بدهد. اعتراض ما در بحث مازوت‌سوزی نیروگاه تبریز به جایی نرسید و هیچ اقدامی انجام نشد.
🔹
در روز رای اعتماد به وزیر فعلی نیرو باید تعهدات و برنامه‌های راهبردی را جدی‌تر می‌گرفتیم ولی این کار انجام نشد و علی‌رغم تلاش‌های وزیر نیرو هنوز نواقص همچنان باقی است.
@TV_Fori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/664574" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664570">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6tFUdS4KttaieK6MbFwNJoEPOzNzXUmOmIAshsAKeEOXWuTPfBND28qReZKg3ub6GNQo2N29AfKO6GDNN5_7VziicO96Eoct5tJ_ntTkE92MQW1CjIzkspoEBC_CCj-PsXgOWrASKKR2RbEkD958InFI-rONTIcVqFRFYht_SNrO8UKTc4IL4peXYsKMFzPMyUs2A7n-vQolRivq-VZICasoKffPUWAiZBjrPdxbWHAB-Bre5_D8rqKrD77SoHFiI7I1iIDjskGZuKPULOt1Zr2CwN85F5K2wYSkiRhMSzvX4SC_FnWunK6n5nS6I7HFqubNiQPHyc_550TQhNIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_xECjPmmUzaJJkDbGIEegQ8nQ9CL9WPoruluHt3n-IfdSRM1MrHqdUWinF1mf0Xq_F3cWDt3zvJzxEdxLgFyWZ21iIByip8aoTcNLDjdBrGmbSBRaKF02w0YPxYue58p6j7u2Z-pgg4gPOIsnkzKjuYkfH_b8GQC6Vdr7u1_ItqXR_8Mv_g1ypXmkDO5h_XqvGrb0bs4hSDftpRhyp4kwfv8fQHtbaIJw2eue41rlqeJo-6mN9pWHGLGwDZmRxNlPXIm0SFTQENIf9noOnJrVMAstDnMwVKK8jrn-fZ0aQxPMXZP_VRjs9UIbDte80ybdn2f7R_hZBX112984V-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsCeFnohopRP8X2uvVKB7TOUNzEVsKl1HnjtO_7muSKN76sOcjduK4lcwE76l5plTp3_hJlPmY2xxEcpQ0YaSEDOuDc0jYUuILWXxOcxIDBg3OafqPqzHdguuNzWbc-8YuLDrqvgfb8oZg6DKWEH8byI1xko8S8jAkbED34gu1FhPvcKi4bWKkW67SZyocUTAoSR-z4SK1Se6gGmIJW9G96Tssg4eH8--ZGPOM3PnbMpxA6LQDwJgd59Jx0A_etQJ0E03MjWDNKZFuHYyPzqGte_x1RxhZe1fgYm8MTI_oba1gTS7g_Dq-szE3wdkHQ06yCbHM7uuoeZ5Tnt0DbDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eudTthtShdUDFuYsrcMnk3VgHMXcfjzPIPIwJI1OYGSHaGIOTr07R3slPftrkEvpdOizeena5Tu3HY3lapK98yHtUKFYlcdm6u-DUF9ciJs32OA4CxgiuQMMohmQkckY8JHsWU19JELl-8C_7blxTEgKFoTduPWuXY6VArEHdxcHc-hd0tf4iO2gaRo_FPM1AfirBRfpd5-b8cQEYJcIbf5bp4fzD0x245bYIUx4aeINCp2vTkeH4HxyG6jztD0kNPG16oFwDimuhABu-ADatMDbuTwImbJtBx4Y8BjV9Muxll1P77SCx1elTAOkxRR9Ywobp1u5GkEChnZyrH74HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فرماندهی جنوبی آمریکا: تفنگداران دریایی این کشور برای پشتیبانی از عملیات امداد و نجات زلزله‌زدگان در ونزوئلا مستقر شده‌اند
🔹
جان انسان‌ها را نجات می‌دهند
البته بیشتر وقت ها می‌گیرند...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/664570" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664569">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GL6k9yw4lOG8zsch5AUfOw8prixEilaty-UCE_HpFBBlf-u2gKdlrhPhqD2ejkp1AljbnKCv8z3h5Cb0Jn191divXBfBXw6mEIHJiHC_zDaPNOHhQg_ub1EeqHhbWdXH1XPiDYDmfmUSQdXh3h8yys7ocrKlYLiDG3mCINGlKBMY88np9jhScaSlH3IEDxfBgDmLQdkeEziOLpCIKiIFogCMDSQD4UxbDxMO6mk-J6Ae5YcNpXTD2zs1o2Xe0z8uK9oIb1VRqVpnJeGYtGOC-4ApTFNeQ0QIFXhvf6fl5TF8YRMWpb7BmqOcYjKhXZ_oTcBbYfh63MHBl_599HKQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: دیدار ایران و آمریکا فردا در دوحه برگزار خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/664569" target="_blank">📅 15:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664568">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/333a29ab62.mp4?token=VJ_QZRjf1dWOEvqPoY0Od4HjrPID2zDdf3CSuxX4_DzMAK6wwX11kxQpNik2wb9ydL0KzddiulK0URax1yIMOsJHt4UOPM58hMR9fCFqf2xRvtlxETB1sEukeDiNOxh2RG7G3XOguT1mnd3d4NCoaWPaEOp45OhEiJJGkMwhG09mJl45Q9kbZlAIusxzia7VLtgQL6lOW4Uno9K32343ESf7VDfg1SwYJObAivkaOf5fOw0Tb9mIMeD0HgLhXdWXOY6EueMFl2ZoMlNAw3fo0GSAR1uRktcSm_94f1vvbdZgpaehe3Jqg5gfeeOvulqUNJ750APx3lSd4jp4rrdu5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/333a29ab62.mp4?token=VJ_QZRjf1dWOEvqPoY0Od4HjrPID2zDdf3CSuxX4_DzMAK6wwX11kxQpNik2wb9ydL0KzddiulK0URax1yIMOsJHt4UOPM58hMR9fCFqf2xRvtlxETB1sEukeDiNOxh2RG7G3XOguT1mnd3d4NCoaWPaEOp45OhEiJJGkMwhG09mJl45Q9kbZlAIusxzia7VLtgQL6lOW4Uno9K32343ESf7VDfg1SwYJObAivkaOf5fOw0Tb9mIMeD0HgLhXdWXOY6EueMFl2ZoMlNAw3fo0GSAR1uRktcSm_94f1vvbdZgpaehe3Jqg5gfeeOvulqUNJ750APx3lSd4jp4rrdu5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب بالن‌های حرارتی توسط جنگنده‌های اسرائیل در جنوب لبنان
🔹
جنگنده‌های اسرائیلی با پرواز در ارتفاع پایین بر فراز جنوب لبنان، بالن‌های حرارتی با هدف ایجاد آتش‌سوزی و تخریب پرتاب کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/664568" target="_blank">📅 15:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664567">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
مکرون باز دوباره با عینک دودی در رسانه‌ها ظاهر شد
🔹
برخی کاربران معتقدند که مکرون باز دوباره مورد خشونت خانگی قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/664567" target="_blank">📅 14:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664566">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6ZyIzHDMO2rD-dKVtwxLg2kjFNGFAeaTlfDiM0zET9za7RQVeHmUK2UB7wCWsneW68qZisH_7sqGD2aG5mf1UGIqer5uNuUhJaFOx2bQcyT53H_--iwFKIwALCe5OcFvQ8NYpaRBupJaspjFDbNUQIBTbMt1RYv1HwCvfefK2KuMSYJWAnF06A9MAEP3uEGnJxopRtsKlwhpZT5LdiubbKE0JQDcUjFwZZahD7cFavJThm46cqtUCiAlzOm-uK4Yb9LM9dvToAK59-gParNCyyoNtC2AljjCZZwwnzK7tmgccsQoA7LV4g1udcM-g-ygA_qGBCfOzyJY5S2O2SqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا نتانیاهو در اتاق جرد کوشنر می‌خوابید؟ | ماجرای اتاق خوابی که خبرساز شد
🔹
در سال‌های اخیر، بارها در شبکه‌های اجتماعی و یادداشت‌های سیاسی ادعا شده است که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در سفرهایش به آمریکا در خانه خانواده جرد کوشنر اقامت می‌کرد و حتی در اتاق خواب دوران کودکی او می‌خوابید.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3226332</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/664566" target="_blank">📅 14:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664564">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
فعالیت برخی شعب بانک‌ها در روزهای ۱۳ تا ۱۵ تیر
استاندار تهران:
🔹
تعدادی از شعب بانک‌ها در روزهای ۱۳، ۱۴ و ۱۵ تیر فعال خواهند بود و مراکز درمانی، انتظامی و خدمات ضروری نیز به فعالیت خود ادامه می‌دهند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/664564" target="_blank">📅 14:36 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
