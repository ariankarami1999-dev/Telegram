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
<img src="https://cdn4.telesco.pe/file/hz1dAJAz7YUKMn4vI8n8wN7bI4_Yn8SDCs5GkSkVTmPAybU9qVca62UqqtJOxMys8T4hAMqvcnAURn6BduFGp4A8J_BtUWJCYByslbIfZez0ErOErVGwMizN13ur4TQFdBtWRdRt_hFwALlKUrFZMeatzWOeGSxt1psgIZLMHai5861tOwfEvRQP7WSmciPjZXQQEG_oLQkRYnrtKIhmotdp62tZKGKMBzqIGcBkLRm4IMM044TJlmSV_aXyAEgaRMLLbfKBbP0gO83345hIdGmxTrNOn6Q8KVwyjBRFYJf-QV0cmkfd5XfgA-vcMApwGCMGYju-3NLkjUSJRZ4R9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.59M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 14:17:28</div>
<hr>

<div class="tg-post" id="msg-658714">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aw9xxg4rX7Ou_uQD_fbNtKV-qE8DDUoSBJniJPvh8zCfca823O0NDU82ryBF24U1tIc0tv5XvhiuNvaXZugQ0J1hsG-yfSFK7gGtYFGkFuoa8FBpiulkWhNEG-M81amsyoMvwHzrNjHHSURIwF5v9iKrea0n6JFkdfsIqmed600aXsVn9AU14GPTLITmXLcLmo31Ywqj_4xVRxj9StJtfAbuTYYPhBeUXwf-belH6AhpJSaIVzo6PuBxX5ibArqrsUODoQkFpsP5JpynOAjIynr0U1IUZm1eWs2mQWaU49cTfpXbNqeD12KKie6ulcuTsEC7FpDzvPYw7bwa15wj8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ گیگابایت اینترنت رایگان برای همه!
🎉
​همراه اول به مناسبت بازی‌های جام جهانی، به تمام کسانی که مسابقات رو پیش‌بینی کنن، ۵ گیگابایت اینترنت کاملاً رایگان هدیه میده!
​هیچ قرعه‌کشی در کار نیست؛ فقط کافیه همین الان وارد اپلیکیشن «همراه من» و بخش «زمین بازی» بشید، نتایج رو حدس بزنید تا بسته ۵ گیگی براتون فعال بشه. تا فرصت تموم نشده دست‌به‌کار بشید!
تازه فقط همین نیست،‌ کلی جایزه هیجان انگیز میلیاردی دیگه مثل PS5 و... در انتظارتونه.
📱
ورود به همراه من:
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/658714" target="_blank">📅 14:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658713">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2135019260.mp4?token=jpetWAQBJ3vXHp6rWdDRaZ3gNtob0cxGoL9aRfevZciEdAjvJe-ostsWhuNcTxbip6q5ISIAjXfaiXbwy-YKWjZpmb0UijkDYnKSZqEChhrykXjUM2vkujjpOxyDUcztRIemL6xQRyo7vT1DbcDliCyrrQgGm4cobkMEq2F0ZVLvLtr6nmww0pXarR_IDK806fONO8Izz-rCEGMMWyrUxlLVxw8_SuDLvdQXEtB1XSMa5f6LX6JH6n6PQiT1n133yaRhalIJ9l9M3HqNuMjU_Wo25ET09w_nZo6X9T_PDH8WqeNPXcDYoV-bXzTCvEnhK6nUc4GdXA5gt98WGvG_LJ6569Y5OQWNP9mi3edSluNxOq5ZOZQbxy4HkyT8e0B-nTAbOpiJzx_DazJdmXqLPF_kljqUVRBlDOFDfgEtVwCf0DR-HDXVHD-kn5SPWwL253hIAeWySNX0Ry38Kz5Y6ofabkEzjrdiD_aKZd32k6_dU0q4JgMegl8ZsVgKwJLqo6li3zRw9S1OI2wAcGMCio1PfJ8ks3bxoZA6jb885EcVEjBiv7UfWL7CIs_IuCicVU1HleiwvxaBvDF6TxrOw2yEdWy4zWMToe0pX7A0klo4dhCboKXQEI4rg5MgiQxXP9yOAeYw_edwJIp-Mjg1on9Lx1SEeaWHb07OY0MeVtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2135019260.mp4?token=jpetWAQBJ3vXHp6rWdDRaZ3gNtob0cxGoL9aRfevZciEdAjvJe-ostsWhuNcTxbip6q5ISIAjXfaiXbwy-YKWjZpmb0UijkDYnKSZqEChhrykXjUM2vkujjpOxyDUcztRIemL6xQRyo7vT1DbcDliCyrrQgGm4cobkMEq2F0ZVLvLtr6nmww0pXarR_IDK806fONO8Izz-rCEGMMWyrUxlLVxw8_SuDLvdQXEtB1XSMa5f6LX6JH6n6PQiT1n133yaRhalIJ9l9M3HqNuMjU_Wo25ET09w_nZo6X9T_PDH8WqeNPXcDYoV-bXzTCvEnhK6nUc4GdXA5gt98WGvG_LJ6569Y5OQWNP9mi3edSluNxOq5ZOZQbxy4HkyT8e0B-nTAbOpiJzx_DazJdmXqLPF_kljqUVRBlDOFDfgEtVwCf0DR-HDXVHD-kn5SPWwL253hIAeWySNX0Ry38Kz5Y6ofabkEzjrdiD_aKZd32k6_dU0q4JgMegl8ZsVgKwJLqo6li3zRw9S1OI2wAcGMCio1PfJ8ks3bxoZA6jb885EcVEjBiv7UfWL7CIs_IuCicVU1HleiwvxaBvDF6TxrOw2yEdWy4zWMToe0pX7A0klo4dhCboKXQEI4rg5MgiQxXP9yOAeYw_edwJIp-Mjg1on9Lx1SEeaWHb07OY0MeVtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت سیزدهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای رسول نجفیان که به دلیل بیماری ناگهانی در نوجوانی روح از بدن جدا شده و با رؤیت نردبان بالای پشت بام حمام عمومی توسط روح بعد از برگشت به جسم و تعریف کردن آن برای دیگران موجب به وجود آمدن ماجراهای شنیدنی می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: رسول نجفیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/658713" target="_blank">📅 14:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658712">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
تفاهم‌نامه پایان جنگ تقریباً نهایی شده؛ ایران تعهد هسته‌ای جدیدی نمی‌دهد و مذاکرات هسته‌ای ۶۰ روز بعد انجام می‌شود. هدف توافق نیز پایان کامل جنگ در منطقه، از جمله لبنان، است./ ایرنا
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/658712" target="_blank">📅 14:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658711">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
خبرگزاری دولت: متن نهایی تفاهم‌نامه تا زمان پذیرش قطعی آن توسط دو طرف منتشر نخواهد شد
🔹
تمامی خطوط قرمز تعیین شده از سوی رهبر انقلاب، آیت‌الله سید مجتبی خامنه‌ای، در چارچوب نظارت مستمر شورای عالی امنیت ملی در متن مورد توجه قرار گرفته‌است.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/658711" target="_blank">📅 13:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658710">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CocisK5Vf0vysxlIkim4-DeAt561cl42txZ8XRJUZApfpce6Q1dst9zZtyYTKFhgNM1MXyyG1lp8j1fO2u6rktNBiVtGgZjuEtpW96B4OHWnssTpLXcbmnU65kWlNhGpR_0SJT9_Y-Us92YpOMErEZ9HEDDQSGmwezg16_R3rbXPDdvMf-Lw5PRHUuIdvQJ_Ge90r6ouL6tFy0XjsqBVuzzW8PZ238A1aIGugtfLLIV57IJgXdbviij5gyx9KY8YrfXGJ6pWdvkiVl6Eijb0k66VzSrOGykKOckPR54uHeys4dQZ_WIJ3u1W7CnbwdAK_CM6isRYMs664kbarVQBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرجام دشمن، شکست و تنهایی است
سخنگوی وزارت امور خارجه، آیه ۱۱۱ از سوره آل عمران را در شبکه ایکس منتشر کرد:
لَنْ يَضُرُّوكُمْ إِلَّا أَذًى وَإِنْ يُقَاتِلُوكُمْ يُوَلُّوكُمُ الْأَدْبَارَ ثُمَّ لَا يُنْصَرُونَ
🔹
آنها [دشمنان] جز آزارهایی [اندک]، به شما زیانی نمی‌رسانند. و اگر با شما پیکار کنند، با عقب گردی از شما روی برمی‌تابند (و شکست می‌خورند)؛ سپس یاری نخواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/658710" target="_blank">📅 13:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658709">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: متن توافق پایان درگیری ایران و آمریکا تقریباً نهایی شده و منتظر تأیید نهایی نهادهای تصمیم‌گیر ایران است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/658709" target="_blank">📅 13:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658708">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
خبرگزاری دولت: به گفته سخنگوی وزارت امور خارجه جمهوری اسلامی ایران، کلیات و متن تفاهم‌نامه پایان جنگ میان ایران و آمریکا تقریباً نهایی شده‌است و در انتظار تصمیم نهایی نهادهای تصمیم‌گیری در ایران است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/658708" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658707">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
متن تفاهم هنوز در ایران نهایی نشده است   یک منبع آگاه:
🔹
متن تفاهم هنوز در مراجع ذی‌صلاح ایران به تأیید نهایی نرسیده است؛ فشارهای آمریکا برای تغییر متن ۱۴ ماده‌ای نتیجه نداده و این متن همچنان در حال بررسی در نهادهای مربوطه است./ تسنیم
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/658707" target="_blank">📅 13:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658706">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/658706" target="_blank">📅 13:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658705">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
فهرست چند عطر غیرمجاز و خطرناک منتشر شد
🔹
گروه ادوپرفیوم:
🔹
Dark Aoud
🔹
MAY WAY
🔹
ALLTEREI (Royal Essence Eau de Parfum)
🔹
گروه بادی‌اسپلش:
🔹
Mar Maris
🔹
The Body Shop
🔹
JANA
🔹
MATERIAL (Perfume Spray)
🔹
استفاده از این محصولات می‌تواند به‌دلیل تماس مستقیم با پوست و تنفس ذرات شیمیایی، عوارض جدی از جمله حساسیت‌های تنفسی و حتی اختلالات هورمونی ایجاد کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/658705" target="_blank">📅 13:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658704">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
متن تفاهم هنوز در ایران نهایی نشده است
یک منبع آگاه:
🔹
متن تفاهم هنوز در مراجع ذی‌صلاح ایران به تأیید نهایی نرسیده است؛ فشارهای آمریکا برای تغییر متن ۱۴ ماده‌ای نتیجه نداده و این متن همچنان در حال بررسی در نهادهای مربوطه است./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/658704" target="_blank">📅 13:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658702">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/740f69de06.mp4?token=Slo7a0brtm4xuA-rzah9ejnFc1GyibwawrZdv1qq7SKH-zq6NQRhFLLuvQ8qg5uCWl3WwE0ENo-bv0NoEFagsblHI2skRdHqgHxjcYTkiP4g_XCIqHL-4ezFz5ngRLUDMJ9ZWaKY0IbWJSo6uRh_hcjlL2hzTVKa3KYDlBtlGOqVeHzCcMawYu0wEc672DGgiBJ3AmY2A_8vxkR2HbButnWFlzQbdWbhpMCHgL1-97EPaq-YZSD7JSGu2u1KRKSRm1esHj_0uxDfpjh3u2GrfkFSti7zKzZnaaXB2_zDp_TNUrvChxRd3nynJ4tzHjktDSPjaSBYADnI9Urw6OgYGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/740f69de06.mp4?token=Slo7a0brtm4xuA-rzah9ejnFc1GyibwawrZdv1qq7SKH-zq6NQRhFLLuvQ8qg5uCWl3WwE0ENo-bv0NoEFagsblHI2skRdHqgHxjcYTkiP4g_XCIqHL-4ezFz5ngRLUDMJ9ZWaKY0IbWJSo6uRh_hcjlL2hzTVKa3KYDlBtlGOqVeHzCcMawYu0wEc672DGgiBJ3AmY2A_8vxkR2HbButnWFlzQbdWbhpMCHgL1-97EPaq-YZSD7JSGu2u1KRKSRm1esHj_0uxDfpjh3u2GrfkFSti7zKzZnaaXB2_zDp_TNUrvChxRd3nynJ4tzHjktDSPjaSBYADnI9Urw6OgYGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویداد تخصصی «نقطه تصمیم»
آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند.
جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود درباره بحران، بقا، رشد و آینده کسب‌وکارها سخن خواهند گفت.
یکشنبه ۲۴ خرداد ۱۴۰۵
ساعت ۱۶:۰۰
مشهد | هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774
#نقطه_تصمیم
#DecisionPoint</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/658702" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658696">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vSU_NKi66NHUB7Am8FFQnI7Mv1ttjklGc-eiWmDvsmlvxf691CU6yjrGK1ZFRWHun_aW9-qjboqFOB8HeX4kVF46N0Fl3NLpAQhFojKnCO66Rwj_yXYMun-1KgKUgvF_p14i5eBb8qYZOF5-ZFgz7wl2DZPbOlLKIJOgWHIoeJ7lRPTDOFP-w5ADTt0HMngwWrQlSuyyLg4LsCXT4ew5Ueff18U3fdPDMqcMmRD39mOYRN9MLyrAaMz51ZO6goh56H2vzw-tw-JpDcJPKM7icWX0oaYE7aB635dAwpIGZ8RlsE4Omc6I3zyWNWTAJDdjjNdLEGswMbzoX7-0kp7Rfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KdE5ir5_QKZOeprOnseeXtAA3E90-nMAZgtYSHlOZ8pNkHIMjlSc3y56c8llkidgFL-9K4xgz1Wj-dAJbcADOmYuodBedadA7vZgfQb5uvDo-vvXlVtAeGkg53j330ox9zsoIaZBTseBVV6PD7tV5lAvyTztqSUQoYUd7o6RPPbZHVGaixvWoCoJaHe5e6H1HpAZvdMUWjiIT6dklUcOqPBR_QHu4bfOhldJr2h6DzFi4ImKL1BgLquwKSdGps2BB-3qToQW1QBqDfVmYqjedo4V5RWaUn1brg_QTIi38jLARBltkbtgTa7hdquvz72Bwu7YfYGMEG7oCGm6jaQojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owP-euBfoSa7GvKC1owc73CqpKdB9GmE9A5ObD_jYXmzOtzqkbMThX7HVlefyEkgsqNmZnRms1c-57i8Df0r3kQM4EwA2qC0zHQxsDYxtF1n-EpMzss-0UpGCyOiwUhjh01tIzStLUmhnEyYbphsn8IosK4bu1KXBDDzDKXAiosXmG_lwyWFXxTIFjm6TQuGTtqHDe3x31EE3TGdzXBCSdprFfz1RFwFto_DSPwWvNm8F_LS0RGqjctcK2z6tHn9Z0E40y2OKpwYNCfy6bkuRjOqgAvfD6yjp0MsnwYHHryGXDldkp3KuGwrXcbFaamR5MVLCW8_oMHY2SnEguZ3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vtYLnGIpS7o8zFyoF6xhTsrIw_6IV3J3NO8nqyFXXZuN4wwDv-5INWHCgCwjjOJTx-RkfgRQ8tpxnYdRQ3KDqABJuJ51_hkQDcSPojqGxpdDncsxOiic6KW786UJ-GwgwP500AYLzsixrzFMlZUGjCd2bI0PdW_bP7fVDqGOl6bpK88xbZFX-EoNd47OED9xBJD6-fUINo75feqddCi26VjQsvctrg3XqTXj0JDQvc1j3BKHURLXROJxT8fZuLOJljWlBuGHvZRo60CBfTs4kbscMXWe62snNBxWpLfvfdPf_uO339creGekKUVGli2A8MeEzaN1XEjVcfvssAysPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G89Teo34tV9qN6J94yCa-DYvNvz85LJfgD9olMFKavezALN7yTyZoP_E870WFkFJsGwNOugMX6fTOgPlwL5tbyq635wit7AaBHAJQ29im6pcc90e1xKALgT123PFzzyDP51F2U2lCEOJ_7LsnYNhNDP9NMPOexWwXehDq4WJv9GjnnMmI-P6RBRN0QiYFB94YYA2qpYVNZ3Rye7yJUK5JWszXeUY7pgsFuhAXO_3PFh1gAySd-hL4YeRJ1pnQwnS6iKEXXMf01YQS6oW9JIOvIT_wkRzFA18iDx2-uYrit21tY2N53FLawcI8P1VZEGblXiABjfA7_FT7tZXxh8_NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3jWljDQ8nx7C2vmxqYEyRu44zPmTUuzN3k10z7XmrGrV4xKEL_DvROzskWgcgiWWVfM86giCxAROvexd3Wo-J5Tq54EOW60liO1Rr8RsJpYWPJsSN5aWsUx5ImNYHk4zKp0oaOKrC2S1P28FC5O7w7ty-uEtuAi7n_BgUNqSp6oWa6toskzr2pBn7LjiBQBfIvJdcEfGlb88N0Vq-DQT1FcUQYLYuTgsakImL89qYt3_5MikA5OyDGZIPdahfBIegiZwwBt-9Pe50XddQgyWj0cTvZONwzRoRm12Zg4RRWkVokClVXveOMRSwJdhqN7hPlzsHRh4q2BN78pelSpdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۶ مدل پاستای محبوب و پرطرفدار
🔹
درست کن و لذت ببر
😋
#آشپزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/658696" target="_blank">📅 13:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658695">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
جزئیات پیش‌نویس ۱۴ ماده‌ای تفاهم ایران و آمریکا منتشر شد  منبعی نزدیک به تیم مذاکره‌کننده ایرانی:
🔹
بر اساس این پیش‌نویس، توقف دائمی و فوری جنگ در همه جبهه‌ها از جمله لبنان، تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی و…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/658695" target="_blank">📅 13:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658693">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادعای العربیه درباره حضور تیم حقوقی پاکستانی در مراسم امضای توافق ایران و آمریکا
خبرنگار العربیه:
🔹
یک تیم حقوقی از پاکستان برای حضور در مراسم امضای توافق میان ایران و آمریکا در یک کشور اروپایی شرکت خواهد کرد. بر اساس این ادعا، ایران خواستار آن شده است که این توافق در یک کشور اروپایی امضا شود تا جنبه و اعتبار بین‌المللی پیدا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/658693" target="_blank">📅 12:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658692">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
از تیم‌های حاضر در جام جهانی ۲۰۲۶ این کشورها سابقه تنش قابل‌توجه با آمریکا داشته‌اند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/658692" target="_blank">📅 12:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658691">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2cd88d80.mp4?token=ksjiBiz44nHqA-ZkAWf_XeoPbBzdUfw4T0QG0I6w9HWkHsHBbKysZcIz4G1Y-HW1LxAwLTeBBx2W0WcVn9OrdaXpDz4TOIVfC-RKuKAenEWQoREIDyo8NKEJwjyuPmNDjLQFpjdA6oXpQzmTYqfEWaTJGGqs3lCsEbHeu9GbqGyAcy8bIcnRFCC_v48wM8FHl54rOQCaka-xwkUcAVpL3bkbG4TwxFYzkZ3xYMqYKIuM8v7uhqP628F71dZIXCRLrC_TmYl7uTVHczvMJzGypqpVjNVA3tfXpduCc35rPvOcGsoW2e8N78ZlUF9ZRhsBeXtnugvfJ9QHHKyj2AD9RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2cd88d80.mp4?token=ksjiBiz44nHqA-ZkAWf_XeoPbBzdUfw4T0QG0I6w9HWkHsHBbKysZcIz4G1Y-HW1LxAwLTeBBx2W0WcVn9OrdaXpDz4TOIVfC-RKuKAenEWQoREIDyo8NKEJwjyuPmNDjLQFpjdA6oXpQzmTYqfEWaTJGGqs3lCsEbHeu9GbqGyAcy8bIcnRFCC_v48wM8FHl54rOQCaka-xwkUcAVpL3bkbG4TwxFYzkZ3xYMqYKIuM8v7uhqP628F71dZIXCRLrC_TmYl7uTVHczvMJzGypqpVjNVA3tfXpduCc35rPvOcGsoW2e8N78ZlUF9ZRhsBeXtnugvfJ9QHHKyj2AD9RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف یک بسته مشکوک تمامی پروازها در هامبورگ را لغو کرد
رسانه‌های آلمانی:
🔹
یک «بسته مشکوک» در محوطه فرودگاه هامبورگ آلمان کشف شده است؛ در پی این رویداد تمامی پروازها در فرودگاه هامبورگ لغو شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/658691" target="_blank">📅 12:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658690">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ادعای ارتش آمریکا: ما سومین نفتکش را در خلیج عمان از کار انداختیم زیرا تحریم‌ های ایران را نقض کرده بود!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/658690" target="_blank">📅 12:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658689">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nD4aEojbcJVOnA2Ia3Gnv0pfiUmQA-PkqGIv0_6BW9DgEi2gp7G5sF17BtkKwxeDMD2FflzhNpmB2jQVvrr4zOVN5F97MZyHt7pLA6M4cDOfUKAfg4sGkhdXDYPITvlwXMD0Jtp0LWZGAfFIvLiuIIBtlKZ5mkzEVPuAb7YumitdDTwtR2dO75JPGmmrdrrp3A0GgXEv9dQXDcXUd_3tUqI-di3JLIa3pp8bN-JGwfSu4Tp1DmnFrWejwWXnoj9leK4eomOkdeC8P2_UYelOoKi9xqmSJZam71RNUnCZAj7Scvecl9yATR-lL0e6YARwB0N54SBoLct-JH3UewhgGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/658689" target="_blank">📅 12:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658688">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1EXf1KHUQx_CO8V0Q8_-rgkraj6nhOfxWu_HQBvk3_gXytHT_XsR2bNSl0Ty7pvtrHJg8Xbwr1IApKg86rVAYEdg2xc9TULvKuFxXtS9W4_AsbPWLNGbjcMruRmphnT8p-q_y-9vkpsaWBcYAIzjMfc--RIyvRm9_jh-2OMhVxGgnJYjeMOuw6CrhO0mIn2ehIIzlAy5EO_wZYjcyDA8b_pmQSFIhKP_nXcKrWcqwZQt4WPwTc4m_n4Qxgyf2f411QCAn7i2I38GSVvnp7Aqq1XKQ_dLYeXUs33J06D_Z_t2N6u-2QaasRWKEew8WPZ8a8ru6TVhXRyNsMdM_Uccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افکت‌های صوتی جدید اینستاگرام برای پیام‌های صوتی
🔹
اینستاگرام قابلیت افکت‌های صوتی مبتنی بر هوش مصنوعی را گسترش داده و اکنون ۱۵ فیلتر صوتی از جمله صدای خوشحالی گل فوتبال، دزد دریایی، پدربزرگ، مادربزرگ و پرنسس را برای پیام‌های صوتی دایرکت ارائه کرده است.
🔹
این به‌روزرسانی در چارچوب برنامه‌های متا برای جام جهانی ۲۰۲۶ انجام شده و شامل افکت «!Goal» با انیمیشن ویژه در چت و معرفی قابلیت‌هایی مانند «حالت فوتبال» در فیسبوک و نمایش هایلایت‌های زنده در مسنجر نیز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/658688" target="_blank">📅 12:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658687">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yxjbk3XohvBVs_IJASh8SzsjVeaHeRMtA0r5Dh0CRMCGFEM_ZjLJ8aX6b6YlMmIGoQyPbsWc4xgar6lE_4G0_e9m9BtoqYNJzfawU7GCTt3nkC3Xke6FQSt0IiI94A_Sl9yiEQnIW_XYwr2Pz7E_4jMCRjk45jgeHCLKSzodukahttQvdLVUTVXdlcfiBprNrr6Aj2XsxO3TDryba5H68CwXoHkNCcy_LlrGED4E2y9JKboC1t-SjvdC1mdi2FbT6CatdXYb_8cg-w_hhYkDQKgRB677siKdIm08K7HfHfcj7iLEXziTa1QVsfPHXcgD_GIeS-wKrhpjgrGIfZIVTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا ترامپ در کمتر از ۲۴ ساعت می‌گوید حمله سنگینی خواهم کرد و بعد خبر لغو حمله را می‌دهد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/658687" target="_blank">📅 12:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658686">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
چین یک شهروند آمریکایی را به ظن جاسوسی بازداشت کرد
🔹
وزارت خارجه چین جمعه تایید کرد که یک شهروند آمریکا را به ظن جاسوسی و به خطر انداختن امنیت ملی چین بازداشت کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/658686" target="_blank">📅 12:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658685">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پزشکیان: انسجام و همبستگی ملی مهم‌ترین سرمایهٔ کشور در شرایط کنونی است
🔹
در وقایع اخیر بیش از ۱۰۰ شب است که ملت ایران در صحنه در دفاع از کشور و انقلاب حضور دارند و نقشه های دشمنان را نقش بر آب کردند.
🔹
بسیاری از محاسبات و برنامه‌ریزی‌های دشمنان به‌واسطهٔ همین همراهی و ایستادگی مردم ناکام مانده است.
🔹
ملت ایران با وجود همهٔ فشارها و تهدیدها، از استقلال، عزت و تمامیت ارضی کشور دفاع خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/658685" target="_blank">📅 12:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658684">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ما ادعا نمی‌کردیم نیروی دریایی جهانی هستیم، اما اگر مرد هستید جلو بیایید
امیر دریادار حبیب‌الله سیاری:
🔹
خط و نشان معاون هماهنگ‌کننده ارتش برای دشمنانی که از دور ادعا می‌کنند اما جرات نزدیک شدن به منطقه را ندارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/658684" target="_blank">📅 12:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658683">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec08863fa.mp4?token=fEzV-wgRj-qemdSvQ5xxQrU8Zw2oQCmGos1ZnohQFPMts9FrVkaX4fWTtWpBtXgT6mPUYe5xax4Bkr45EW7YJZFlIC1bi5qlMgJXtRgT-5C5VH943SEliE4eEuW6M1tFRXgSXR7tTsM89W9oPCY3t1-FaRL3O4P79UaosTgB54QLAHOALia1HUiM9EBzP6408F2Ws92GAf8-Pffh0e8WOKiI2TPWGdX-6JGxjejFD3_8ycBXgNff6LJ4RZJ-LtnkfCKiZPY8Z2bnqsOH_GJd8zFmg4UTUtd3yRHf9j33IANc-UIAZqfi0_srUbK5_InI08GGDNAlN7n4aLswk_U06bBjL5Xv5tCS-CA5fUqXLBSm53FVhlXjPvNO6PyP5LVxHHi_B9Rg0dl4p1tnRwvXWkP-Vc9pecMF3InMO-0W_HQcrGGe_OmTzETbu13AtInbqHyt4bSGJoJz330JQmG8P69ssSMJo2l3S8eXZ1iKIzrvItbx1Wh8P9IiHjW56lD1SgjJ5biohJbtfQlWUPMW3MPz6HkwcA2P6KmNjt8DNPGVKt6E-KpmedI9AhKvKyggbfkPDa_b0aEdkVFgLqXzjvOKMDCM9MUEjBU_r0cmCODCpGpu_XUohvkWrklUNCk3mjhr02rn12DO7ICpp1NX1l_chHVZ8xnO8yM3wcryIWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec08863fa.mp4?token=fEzV-wgRj-qemdSvQ5xxQrU8Zw2oQCmGos1ZnohQFPMts9FrVkaX4fWTtWpBtXgT6mPUYe5xax4Bkr45EW7YJZFlIC1bi5qlMgJXtRgT-5C5VH943SEliE4eEuW6M1tFRXgSXR7tTsM89W9oPCY3t1-FaRL3O4P79UaosTgB54QLAHOALia1HUiM9EBzP6408F2Ws92GAf8-Pffh0e8WOKiI2TPWGdX-6JGxjejFD3_8ycBXgNff6LJ4RZJ-LtnkfCKiZPY8Z2bnqsOH_GJd8zFmg4UTUtd3yRHf9j33IANc-UIAZqfi0_srUbK5_InI08GGDNAlN7n4aLswk_U06bBjL5Xv5tCS-CA5fUqXLBSm53FVhlXjPvNO6PyP5LVxHHi_B9Rg0dl4p1tnRwvXWkP-Vc9pecMF3InMO-0W_HQcrGGe_OmTzETbu13AtInbqHyt4bSGJoJz330JQmG8P69ssSMJo2l3S8eXZ1iKIzrvItbx1Wh8P9IiHjW56lD1SgjJ5biohJbtfQlWUPMW3MPz6HkwcA2P6KmNjt8DNPGVKt6E-KpmedI9AhKvKyggbfkPDa_b0aEdkVFgLqXzjvOKMDCM9MUEjBU_r0cmCODCpGpu_XUohvkWrklUNCk3mjhr02rn12DO7ICpp1NX1l_chHVZ8xnO8yM3wcryIWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقایع خاص روز اول جام جهانی ۲۰۲۶/ از افتتاحیه تا کامبک کره!
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/658683" target="_blank">📅 12:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658682">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
همه حجاج تا ۲۳ خرداد به کشور بر‌می‌گردند  مجید اخوان، سخنگو و سرپرست روابط عمومی سازمان هواپیمایی کشوری در #گفتگو با خبرفوری:
🔹
وضعیت پروازها طبق روال گذشته در همان فرودگاه‌هایی که طی اطلاعیه‌های گذشته فعال بوده است، هم‌چنان ادامه دارد. فعال شدن فرودگاه‌های…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/658682" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658681">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5us-gXeMn1HUH9IwIzvN3_uK9Q8oV7qB6BC-X7bFlzaVKCnF3d6QlPpfjjp1NbuZve1xSN7rL8PuRQApDaj1s-6Sl_KixEAKf9_hSWSvMi3rHxijazDhD6KAwLR2QgxfnFPUVEY-NksacJqKu1nzwwHlSwUkhQY2poCMpZzFDh_ARa3dM2bMzTP3Wq6Bi0AxUi-A0xhhEnRhGFvGg_KnyjfKl8DsBI9-5pln6GVkepMe27ebAzY9eHU94kt940XPD8znlADsRHRb5fPUpRBnITnhMcojRgeuGbvdQaC4Zztxpi5bq1neP7UjaE4HixjoOvVP6SmkEjQfenWnZ2JoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصابت موشک ایرانی به رادار هشدار زودهنگام و راهبردی آمریکا در بحرین
🔹
تحلیل‌های منابع باز (OSINT) نشان می‌دهد در حملات موشکی اخیر ایران، رادار راهبردی AR-327 آمریکا مستقر در منطقه جبل‌الدخان بحرین هدف قرار گرفته است. این رادار سه‌بعدی دوربرد با برد تقریبی ۴۷۰ کیلومتر، مسئولیت رصد مسیرهای دریایی خلیج‌فارس و تنگه هرمز را بر عهده داشت.
🔹
تحلیلگران با تطبیق تصاویر ستون‌های دود با مختصات این سایت، احتمال اصابت مستقیم به این تأسیسات حساس را تقویت کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/658681" target="_blank">📅 12:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658680">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
شروع سوخت‌گیری با کارت بانکی از ماه آینده
معاون سازمان بهینه‌سازی:
🔹
از تیر امسال سوخت گیری با استفاده از کارت بانکی در چند جایگاه کشور آغاز خواهد شد و تا پایان سال به همه جایگاه‌ها خواهد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/658680" target="_blank">📅 12:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658679">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
سوزاندن پرچم اسرائیل در گوادالاخارا مکزیک شب گذشته هم زمان با افتتایه جام‌جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/658679" target="_blank">📅 12:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658678">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quU4qJYIuJ7imx5KCQpcdtfiRrHJJ6SaYIZT8tZggWw2gIJUpdJz-2oi_jlAMjxjyHtRpCrS5RL-5x7OYTLz1AwMlMGGppJDoiHaYK82d_CCK2YXmFd32u-YK3w1X3lQ7_KKi02Bi6rgtowF7ZJnukeBzKHrswUUz6yELsAagjb-3NCdI4hWCSv1s9nwL-l68XuKA-WZ-BTMv2-OA_RoCPqxOSzepzeC-1b35E5ng8NVvEeCfc7Q9dcyYR-FHxRW8r0HYiMYXw00G74up2OwIQPOmNEbpCODHl5p0n1NDNMGXqjpHJmIww5BwJMeeqT3hSRHZqyMGWIryRtj-5jNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">30,000,000 ریال هدیه استثنایی دیجی‌پی
ویژه خرید حضوری از "چرم مَنطِـ"
با کد: DEMPSD
UPTO 70%
➕
20% EXTRA
مشاهده کدها
👇
و آدرس شعب:
manteofficial.com/b
⌛️
فقط تا جمعه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/658678" target="_blank">📅 12:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658676">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
جزئیات پیش‌نویس ۱۴ ماده‌ای تفاهم ایران و آمریکا منتشر شد
منبعی نزدیک به تیم مذاکره‌کننده ایرانی:
🔹
بر اساس این پیش‌نویس، توقف دائمی و فوری جنگ در همه جبهه‌ها از جمله لبنان، تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی و خروج نیروهای آمریکایی از پیرامون ایران پیش‌بینی شده است.
🔹
همچنین رفع کامل محاصره دریایی و بازگشایی تنگه هرمز ظرف ۳۰ روز با ترتیبات ایرانی، تعلیق تحریم‌های فروش نفت و پتروشیمی و دسترسی کامل ایران به منابع مالی، آزادسازی ۲۴ میلیارد دلار دارایی بلوکه‌شده ایران در دوره ۶۰ روزه مذاکرات، ارائه طرح‌های بازسازی حداقل ۳۰۰ میلیارد دلاری، و آغاز مذاکرات ۶۰ روزه برای توافق نهایی درباره موضوعات هسته‌ای و لغو کامل تحریم‌ها از دیگر مفاد این پیش‌نویس است.
🔹
طبق این گزارش، آمریکا در دوره مذاکرات نیروی جدیدی به منطقه اضافه نمی‌کند و تحریم تازه‌ای وضع نخواهد کرد، سازوکار نظارتی برای اجرای توافق تشکیل می‌شود، توافق نهایی با قطعنامه شورای امنیت تأیید می‌شود و موضوع برنامه موشکی و حمایت از گروه‌های مقاومت به‌طور قطعی از دستور کار خارج شده است./ مهر
🔹
منابعی مدعی شدند که متن تفاهم هنوز در ایران نهایی نشده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/658676" target="_blank">📅 11:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658674">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f5624e1fa.mp4?token=FbBsRQ2orGG2_jfoHT8HpdeIRloIza-8et1u_B6ZmaxCHDSh88TMCU-Q1JdWzZtiHuI2mZupHKL079m3AHHX_kmJwsYBuh5gPnuEAkLM7MOqaPzdyQMH-23NOqtJ-Npm3yDZwv99WldkUI3qIQmCoW7KhPs9pTSonoS90mPPDEV4nLxrsABfbfyMNEMn1ogdv0BcmRZ7i-gbjGcsPq97-sWHFPPCCK4MHILo5Bqj7MrFKnOhoXk1e23vUr_Tuf4wgkwymn8DsKKWbGKTN500UWJqPk2riTvz69T5JPOl5cI0tDvDLqIxSLdqqI4quPtobJv3Ib5pZg5woes593ARy3-jxBfcOpaC5r9gtsDb4aRqhT4KtDmujHcgxlVHZn-HJQKkiSXwVOWq6KT77TpzLmkjyuRELv0_WlEq6CGUVTS-u3VN1QS15UBYBA8ZiOgp8cifdxuHpQOLOhNb_hfmg6tbQpzCb1oV-9WY-pCF_lVd5lWMwlStaFCLIeWF-_jVefUqzFT9uv-iszvOFuHik8KnXvRcrjSpVTHIKFI8b_mmFu7_z-osa1QfaM_9_y5IW1Q430FsBUyykglsjO0rAAbGnJKkWiJlQ1U5yNA0EX1A0wiIjQABpW4yMBYHWwtyiWRR6oNGYHtSbXpiUxzHj0nqFFs87rjEbXRWBnfYCUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f5624e1fa.mp4?token=FbBsRQ2orGG2_jfoHT8HpdeIRloIza-8et1u_B6ZmaxCHDSh88TMCU-Q1JdWzZtiHuI2mZupHKL079m3AHHX_kmJwsYBuh5gPnuEAkLM7MOqaPzdyQMH-23NOqtJ-Npm3yDZwv99WldkUI3qIQmCoW7KhPs9pTSonoS90mPPDEV4nLxrsABfbfyMNEMn1ogdv0BcmRZ7i-gbjGcsPq97-sWHFPPCCK4MHILo5Bqj7MrFKnOhoXk1e23vUr_Tuf4wgkwymn8DsKKWbGKTN500UWJqPk2riTvz69T5JPOl5cI0tDvDLqIxSLdqqI4quPtobJv3Ib5pZg5woes593ARy3-jxBfcOpaC5r9gtsDb4aRqhT4KtDmujHcgxlVHZn-HJQKkiSXwVOWq6KT77TpzLmkjyuRELv0_WlEq6CGUVTS-u3VN1QS15UBYBA8ZiOgp8cifdxuHpQOLOhNb_hfmg6tbQpzCb1oV-9WY-pCF_lVd5lWMwlStaFCLIeWF-_jVefUqzFT9uv-iszvOFuHik8KnXvRcrjSpVTHIKFI8b_mmFu7_z-osa1QfaM_9_y5IW1Q430FsBUyykglsjO0rAAbGnJKkWiJlQ1U5yNA0EX1A0wiIjQABpW4yMBYHWwtyiWRR6oNGYHtSbXpiUxzHj0nqFFs87rjEbXRWBnfYCUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به جامانده از مراسم افتتاحیه شب گذشته جام جهانی ۲۰۲۶
🔹
نورپردازی دیدنی در ورزشگاه آزتکا.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/658674" target="_blank">📅 11:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658673">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiPnSsYKzNa4mo8U9rfFwKHaZtVXryGZ1x976aJqZantNlSzEggz7szAQ0hi_7Ms92DMio-9eEW_o4jyeSj_0s_EwH865HAenwZSuXkw7ScBEeJC9s0j6iH9A3j7E9mmjgSlF9exKx9oqb3vYJve7rsvuGO7-JTejzX5D27rKUrUfMvLqLKB5BT69U5O99XcaRk1YUoUx7is8ORs1wvRWct7Oa0zymg3fdY61vnzz3fjeTaKMqOfQ-orCMh5jeezVDBBW2WOcFa5DgK7QrEDkabMEvVJp5HgZaGmVlhBnoKTBOBiAEK427Ex4Ezzok56DOosI9qWZt82XyodKM_S3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه آمریکا منع سفر به عراق صادر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/658673" target="_blank">📅 11:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658672">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای اکسیوس: یادداشت تفاهم ایران و آمریکا، آتش‌بس را به مدت ۶۰ روز تمدید می‌کند؛ آتش‌بسی که لبنان را نیز در بر می‌گیرد./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/658672" target="_blank">📅 11:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658671">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4294c74865.mp4?token=raHobX-KXoaQlqOP3DlGT741yZOM8Il0MoERi2spVQ-2SdtJUrXk4cOAgxbFw4txNVgjnhvCBPH8VOzy7_D9guAlZniwHDE0KMS9ernUVwBqNxvLfy2BpRVQrJAxG-7nWvO5pNPQ6WHxAMULU_AmxLW-WABxcYW4tIheM_eMgdcBQMvrXr9WQZ8YeEDBX9wN8NuQ2k_cq9iwdB_fu6-RA5_8njsgqni7HJiBH5ubFKK-yLRgfQ-xRNv5tJVen3-JbQwunImd9i6WtcbUL14IbasPVv2lqpAujVvyaGV08lxyzDWnYwkaL7A90DATAXsvvMoVSXWn0qOz0UTyxsWBug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4294c74865.mp4?token=raHobX-KXoaQlqOP3DlGT741yZOM8Il0MoERi2spVQ-2SdtJUrXk4cOAgxbFw4txNVgjnhvCBPH8VOzy7_D9guAlZniwHDE0KMS9ernUVwBqNxvLfy2BpRVQrJAxG-7nWvO5pNPQ6WHxAMULU_AmxLW-WABxcYW4tIheM_eMgdcBQMvrXr9WQZ8YeEDBX9wN8NuQ2k_cq9iwdB_fu6-RA5_8njsgqni7HJiBH5ubFKK-yLRgfQ-xRNv5tJVen3-JbQwunImd9i6WtcbUL14IbasPVv2lqpAujVvyaGV08lxyzDWnYwkaL7A90DATAXsvvMoVSXWn0qOz0UTyxsWBug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع آتش سوزی مهیب در یک انبار در کالیفرنیای آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/658671" target="_blank">📅 11:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658670">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b842e5b712.mp4?token=YxITURmMl8-0Pvk8Yv6z0MuNRJfDLcJXfANM8d2Xx6pgICUrZOqLEmJYc7DPfAoD5K0onQ7bowdTO-O8QLGWipJbLmtauM-q3fJ2RdNgIDziLCYGyGz5M_hurtVVGDCSQyaLcDQn4xE2omJcPsuHLzmXTJQKvm9IgAvDIZAP-GdBdec--2OcCjE1xEWHtalkB7INguRLoocXlu7EX0AOwSYfym6NWygA-fcl7S4gJMQ_KKlAexmLk_A69s-vaxHU3-rrBsMlSdffMLl6g32X7XNn4zaB_jJfDGCw79SH0FEL4z8Iit5PP9T8CJIPbAZEQK0mf1Us_iVLZfXWM2PznQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b842e5b712.mp4?token=YxITURmMl8-0Pvk8Yv6z0MuNRJfDLcJXfANM8d2Xx6pgICUrZOqLEmJYc7DPfAoD5K0onQ7bowdTO-O8QLGWipJbLmtauM-q3fJ2RdNgIDziLCYGyGz5M_hurtVVGDCSQyaLcDQn4xE2omJcPsuHLzmXTJQKvm9IgAvDIZAP-GdBdec--2OcCjE1xEWHtalkB7INguRLoocXlu7EX0AOwSYfym6NWygA-fcl7S4gJMQ_KKlAexmLk_A69s-vaxHU3-rrBsMlSdffMLl6g32X7XNn4zaB_jJfDGCw79SH0FEL4z8Iit5PP9T8CJIPbAZEQK0mf1Us_iVLZfXWM2PznQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رئیس فدراسیون ووشو از ماجرای حمله خواهران منصوریان/ از خواهران منصوریان شکایت کیفری کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/658670" target="_blank">📅 11:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658669">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rh9MwFaimL05PbwwVT4z3qxQue79UPxnxMyqsI4iWNI228MLXcyVLs0Xht8bU-VXU57FNBSuSHe6KLrdULWHil4EozwmND1qyax4sbcSfif3JuEQjjUh0-2SsPOur4wWWbMZ3aC0yTtX_TxfjvURSEuzKqrgm7qaQ-YP-jLWFGBQuSSqIED3QIlf3HDLaUfrBcyAisR-Wf5_N-7n6FKdAp3mBjnFc-UwHsbURhoz7x6Fb14MCErwnI5NDE61k7Z1fhsyQTWaMqYTMVXv49fiOW4RUlhEYtBKHUV5nQDdxTpOqado_8zKEWrzLuVNeiAHYpyQpeH5G1lMo0-ixDP5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: تمامیت و امنیت ملی ایران موضوع معامله تبلیغاتی نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/658669" target="_blank">📅 11:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658668">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
مخالفت یک کشور منطقه با کمک به اسرائیل برای حمله به ایران
کان نیوز:
🔹
یک کشور منطقه‌ای در جریان حملات این هفته به ایران، دسترسی اسرائیل به حریم هوایی خود را مسدود کرد./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/658668" target="_blank">📅 11:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658667">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ادعای پولتیکو درباره تماس مقام‌های قطر، امارات و پاکستان با ترامپ
پولتیکو به نقل از مقام‌های آمریکایی:
🔹
پس از تهدید دوباره ایران از سوی رئیس‌جمهور آمریکا در صبح پنج‌شنبه، امیر قطر، رئیس امارات و فرمانده ارتش پاکستان با ترامپ تماس گرفتند.
🔹
آن‌ها به او اطمینان دادند که یک توافق اولیه برای هموار کردن مسیر مذاکرات جزئی‌تر در دسترس است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/658667" target="_blank">📅 10:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658665">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsYBstmKPR5vVFLkydY5_NtHFa4nCJpks7LKqJRvO47CS8XxsF2JUbSDXiNncrJJjiiiykFs_7BNJJnx2xzezcPGsmaAZehbhgipxPyGtLWo--My09UF-E0UKUiE6yccwtl6-pWqorQFkqyar3k4dACT3JsPZZTxbx939IuXcclGQNCzH5imDsSLNwsj-jW2E7XGb36rUoOLJ_Vb_zdumnxu_VViv1cM_LBVl3sMBOOqoD1ujzNu7ar0gxXT0L_RsL_vxiwgm2qvZvDbyAU4mmRX5ufb73BY-XjQ_vwGNNTN-b-bAI4asRDhJJaiJjd90yyeVZrWk3JM1s7HoktE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فدراسیون والیبال پوستر دیدار مقابل آرژانتین در لیگ ملت‌ها را منتشر کرد
🔹
این مسابقه ساعت ۰۲:۳۰ بامداد شنبه برگزار می‌شود.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/658665" target="_blank">📅 10:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658664">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb5d49c6db.mp4?token=L0Zaiy2b8hqoskBZzlyTAlhsDDp6Y5PXyPNOtKeRxqC0aItjqEZqjYtjv0g6DSgBJ_effge4SmvbxbOswtUgPJbaklc3-exAkEvCisCUSloLoyEwiy5WX84b-pF80KrrVMRNi9aStO5nWqbiOviVJKGIRN-UlI6h3ZKoe343XUEwcFBn2gCxUoEAMsLPkoPt7qjK6ZJO1bfUBvBG26Nf3Yerz_xWgWblqIe_V3fuypfJydrTF4MXbJBhDA4tbv-P23ob7fpUCN4txHnnh8JB3eQatt55Imoow2yNJoqfI80oFKlCgBc8IK4EA1j5ZIvxgOyJw56Qit3A2lLcCjBL2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb5d49c6db.mp4?token=L0Zaiy2b8hqoskBZzlyTAlhsDDp6Y5PXyPNOtKeRxqC0aItjqEZqjYtjv0g6DSgBJ_effge4SmvbxbOswtUgPJbaklc3-exAkEvCisCUSloLoyEwiy5WX84b-pF80KrrVMRNi9aStO5nWqbiOviVJKGIRN-UlI6h3ZKoe343XUEwcFBn2gCxUoEAMsLPkoPt7qjK6ZJO1bfUBvBG26Nf3Yerz_xWgWblqIe_V3fuypfJydrTF4MXbJBhDA4tbv-P23ob7fpUCN4txHnnh8JB3eQatt55Imoow2yNJoqfI80oFKlCgBc8IK4EA1j5ZIvxgOyJw56Qit3A2lLcCjBL2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برافراشته شدن پرچم فلسطین در مکزیکوسیتی همزمان با افتتاحیه جام جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/658664" target="_blank">📅 10:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658663">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
یدیعوت آحارانوت به نقل از منابع: نتانیاهو گفت به ترامپ اطمینان داده که تمایل او برای توافق با ایران را درک می‌کند، اما اسرائیل نباید قربانی شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/658663" target="_blank">📅 10:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658662">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uj2uFO65wmYPPMe0Wgs3r-EGVnNcAsu7bjU6nIsuZKcpGmYjLNDUQ8fbyqQn-njF5lUhND0PiF6RUEjUl0Z9UgQTAQp98HgAeG9Sujc7YdndCjIAeR90C9Ea1fyWyAf-7HkjbIjZ15fjZpMm6RJrgV6mYcitlt_OVaged71ydFag-bUW4K35kT3i3ot-8ghxtCVjpncj-EVYJLrVrcVqOkDxqJ9ZlDwn_ne3uPAhOjKvVBjlsVE8f1MiA-6_rvWIHXoQcg57-EU9l3lhIndLXMIHgtwLFeNhY56mUsJfaELlf1teRnFCWAzf6QB9GWGwTmtf9FDjH2TNXyNoVl9Ojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدیمی ترین کتاب فارسی چاپ شده در لیدن، در سال ۱۶۳۹ که درباره دستور زبان فارسی است
🔹
لَیدن (به هلندی: Leiden) شهری دانشگاهی در استان هلند جنوبی و در نزدیکی لاهه در کشور هلند است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/658662" target="_blank">📅 10:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658661">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a69ae2d6b5.mp4?token=ENpPHX6RKRpAyeU0LNV9HFikzsx9rgiLGvW8PkOW5Tj7iXVbHxr4iczJ70mHYZEaBsGzUXm3jbO_7vDlaxFaR-9RFxaY5ykiiWXtVSrn5hd6UeiXPXFbFuzOhx6jbTZtKygqNIOxnS0YUv76WazTK6tWxJQnQpPP4DdQLoVzuKln5EkuDbKuTrtI3qwm9jo9eq84IOeS_h8mZWtPmIrwznDx0DfrBKDBcpLJb47E6v4bsEhEfOYFLlA2Hd45uIZRaZZjVsRl26WC8VaqtmjXzFNptgJ0gRfDkuaEEPYV5qt4IvKfU7dx6Jhj9A6ni63xq6BmmatBxZ-ZW66u6Ia8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a69ae2d6b5.mp4?token=ENpPHX6RKRpAyeU0LNV9HFikzsx9rgiLGvW8PkOW5Tj7iXVbHxr4iczJ70mHYZEaBsGzUXm3jbO_7vDlaxFaR-9RFxaY5ykiiWXtVSrn5hd6UeiXPXFbFuzOhx6jbTZtKygqNIOxnS0YUv76WazTK6tWxJQnQpPP4DdQLoVzuKln5EkuDbKuTrtI3qwm9jo9eq84IOeS_h8mZWtPmIrwznDx0DfrBKDBcpLJb47E6v4bsEhEfOYFLlA2Hd45uIZRaZZjVsRl26WC8VaqtmjXzFNptgJ0gRfDkuaEEPYV5qt4IvKfU7dx6Jhj9A6ni63xq6BmmatBxZ-ZW66u6Ia8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات ۳۹ مهاجر از یک تریلی آتش گرفته در تگزاس
🔹
۳۹ مهاجر از یک تریلی آتش گرفته در ایست و بازرسی گشت مرزی در نزدیکی تگزاس نجات یافتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/658661" target="_blank">📅 10:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658660">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
واشنگتن پست: جنگ ایران رشد اقتصادی جهان را به ضعیف‌ترین سطح خود از زمان کرونا خواهد رساند.
🔹
آکسیوس: نتانیاهو از جزئیات توافق بی‌خبر است.
🔹
مصر از آمریکا و ایران خواست فرصت دستیابی به توافق را مغتنم بشمارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/658660" target="_blank">📅 10:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658659">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5303981cd8.mp4?token=RvmBRiF3mbLgFRo5FnxaA9pa9qygsWWTufUcNI2B6f7SU-S1QgS_80DEaIIWwHGs4G7OJ4G7mOS-pssmGjSxM93aFDl9zKgik1EDnMTyADOCnta4wMU1OlV98LyeswLulT2uTXEZar-OEHYmP_8dUHFwQ1xMCiFkClW3xNpbqbxn9T74Mmscre3Z-UUfNzYgNg67DkJiZyKd2-o8So0yZHW7cpsFe1yCWT80sY7SM_JiicOgdrX4hnvEWkXabeW5Oyxc3yTND4jFsgsHLfV6h9vGDoPGRbqL216Lr3ECGCYgGdNra7YQId6x88-cKWU1Vj-jjw922KOPry-UcysgVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5303981cd8.mp4?token=RvmBRiF3mbLgFRo5FnxaA9pa9qygsWWTufUcNI2B6f7SU-S1QgS_80DEaIIWwHGs4G7OJ4G7mOS-pssmGjSxM93aFDl9zKgik1EDnMTyADOCnta4wMU1OlV98LyeswLulT2uTXEZar-OEHYmP_8dUHFwQ1xMCiFkClW3xNpbqbxn9T74Mmscre3Z-UUfNzYgNg67DkJiZyKd2-o8So0yZHW7cpsFe1yCWT80sY7SM_JiicOgdrX4hnvEWkXabeW5Oyxc3yTND4jFsgsHLfV6h9vGDoPGRbqL216Lr3ECGCYgGdNra7YQId6x88-cKWU1Vj-jjw922KOPry-UcysgVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین ماهواره ارتباطی نسل بعدی را به مدار فرستاد
🔹
چین با موفقیت ماهواره Tongxin Jishu Shiyan-25 را از سایت پرتاب فضایی Wenchang پرتاب کرد و نقطه عطف دیگری برای برنامه فضایی خود رقم زد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/658659" target="_blank">📅 10:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658658">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d8bf8457f.mp4?token=hCIgQX1e_pL3uRfzv8_L8hbhO2Q2TkCZ1D8xFYI8HNmtjfNcwq2eNGJnDfDHfOIpPf6k1RW7bfChyAbyKFun6KG86HZWdI6_H5E6V00L9zw2Yi49w_Z-Y504O4NAJ3nTdvUD5QzXoq-lsYuz0lmVWhb0cDid_OouFs_Sz1LEfM8QPEYFuz-t7p9bZJDqUkF7Fr3Go_nGWNQr1ACZeV3B_pK4LShUyrZcvziM3s66IucuNE0Rb58Jf5lN32z6Hgy5dLMsU0wvU8GX5fH2dcqayDvGS2iEYbqw2eN505YGnSTfOrG7BWnIEpEi87_IdJ2VsGDqsCuedbZIr2rqe-0iMh54g_W8EfA0pJD3vEtu1n-avGkTtGAEe2jWITfj77eGSmbfud34QALJ7aNDYdB2NLf2EuGw5k2cOP4RReK-jxg1zqjlx4SynppDcbNNJNiMNXxHPc6VtrSc0hUOGCw2PSAjl7lAb_PQ2KJQVbYFnwi5u7ZeDaMTWQvwj-PdpzuUlnH5f0Cnh1qfKm8Nf9IfCuJ7tJAw1zLXCGutR5K2pou5W71sD5bX3fd9zKUUvOsWuUrwyZFQ3Lt59PsA-F5PwZOSwBph5DvZ7b6z2GDgILwopqsBB9tvrlGyNGmIHSrprdNnD-3gGeIAMghgP_IbJNwKgbnk57gPiexSWkzjbtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d8bf8457f.mp4?token=hCIgQX1e_pL3uRfzv8_L8hbhO2Q2TkCZ1D8xFYI8HNmtjfNcwq2eNGJnDfDHfOIpPf6k1RW7bfChyAbyKFun6KG86HZWdI6_H5E6V00L9zw2Yi49w_Z-Y504O4NAJ3nTdvUD5QzXoq-lsYuz0lmVWhb0cDid_OouFs_Sz1LEfM8QPEYFuz-t7p9bZJDqUkF7Fr3Go_nGWNQr1ACZeV3B_pK4LShUyrZcvziM3s66IucuNE0Rb58Jf5lN32z6Hgy5dLMsU0wvU8GX5fH2dcqayDvGS2iEYbqw2eN505YGnSTfOrG7BWnIEpEi87_IdJ2VsGDqsCuedbZIr2rqe-0iMh54g_W8EfA0pJD3vEtu1n-avGkTtGAEe2jWITfj77eGSmbfud34QALJ7aNDYdB2NLf2EuGw5k2cOP4RReK-jxg1zqjlx4SynppDcbNNJNiMNXxHPc6VtrSc0hUOGCw2PSAjl7lAb_PQ2KJQVbYFnwi5u7ZeDaMTWQvwj-PdpzuUlnH5f0Cnh1qfKm8Nf9IfCuJ7tJAw1zLXCGutR5K2pou5W71sD5bX3fd9zKUUvOsWuUrwyZFQ3Lt59PsA-F5PwZOSwBph5DvZ7b6z2GDgILwopqsBB9tvrlGyNGmIHSrprdNnD-3gGeIAMghgP_IbJNwKgbnk57gPiexSWkzjbtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهمان‌نواز مثل مکزیکی‌ها؛ جشن جالب هواداران با هوادار کره‌ای در افتتاحیه
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/658658" target="_blank">📅 09:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658657">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4ZeENFXuLiUYrAbh6X4R603qrKvIklwFlYH6x4s5XSMk5Zsm2eX8RyYnjIrIBC4r2cAvnqyx3eGR0HWTo2rm-szCz49v0o3RhoovbfjLjWMLiTyygLd8UZrVRC2TEMfWxG-9CBiJsBNXHktN1EUy4pBHMSH-D6xixj3mVmwI2U3s3yDZYgKhWIE4co6caguY7HOkSZFb3mARm4cV3UROqyWIbSVOcVzVivOPr9WIbAJOKs7Vnu6XOqAf5FUu3f-8Iu8ywAtdF0h6-9xcAcVF12sdCSVt4brKGNTr7DaYayIY9kNaNquEO9-mLHlgaW-Hrg9U1s4OLXs4CaaWQZiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روز دوم جام جهانی؛ کانادا مقابل بوسنی، آمریکا برابر پاراگوئه
🔹
در ادامه مسابقات جام جهانی ۲۰۲۶، طی ۲۴ ساعت آینده دو دیدار حساس در گروه B برگزار می‌شود: کانادا به مصاف بوسنی و هرزگوین می‌رود و آمریکا میزبان پاراگوئه است.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/658657" target="_blank">📅 09:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658656">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
شروع سوخت‌گیری با کارت بانکی از تیر امسال
معاون سیاست‌گذاری سازمان بهینه‌سازی:
🔹
از تیر امسال سوختگیری با استفاده از کارت بانکی در چند جایگاه کشور آغاز خواهد شد و تا پایان سال به همه جایگاه‌ها خواهد رسید.| تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/658656" target="_blank">📅 09:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658655">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3Gs9ARzAHljWSzMurJP9R1HiTE8oS6oSP0PpqPh0w0UXmxIAwGNNPhzPO1KzZDUeMVp7ZDQlijolFgXlUXPmptR137_awOIpayYX_1b0EAj9TY-ffx1VqATv0mnBoSkY_lcbk4aA5eI-wAF6m_GrsYqYt6dsECmq3jX6ATiBzai5p9UWqep8eTMbEx74l7LWk0mRFePPbNVMnbIdLN4xkm2CMgEGz-TLdSLPN-zaKJA7bkWk1xqA4KblSzXGgvOLzqb7NUNk7E4JiIcEAUWJLZBOaQuwaflVJa9D2Y2dQAjdaheQMmBtY7WBOZLXhBGkGDBkN0X4wD_aWDwV-mAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میان وعده‌های مناسب بعد تمرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/658655" target="_blank">📅 09:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658654">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQkwI6NqKYq60M3e7CE-p2W2pNPwCogXdWwOuahhHPyy_pys-QKmQWc5H1VgpTpWbOMQ6_v8IlYPAUhVOdnc6Te86bWihNJxUIsgqgTfPh5DqLScsSXtKRh-YAF3JQ4wf8zUFULMiFon5vPfaKFiPqpe2hT8esoRgnKxaJvHMuh6GHvawAGRKQjQtvDXQm45ie2Sem0OPT9uCpMLnakh3CxI3_Ml0Me4XXEmNZkCUfM5CeXLgq_saTWTQgyHHR-RQExl5S3m68o7R_exoXR8ZKYypD_5loLiZZ9AR69uEaFz5KAsa2qaEHNU6RtkzNO5nPVs41kzynZg6Q2DgA2NHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خشن‌ترین افتتاحیه ادوار جام‌های جهانی
🔹
برای اولین بار در تاریخ ۳ بازیکن در اولین بازی تورنمنت اخراج شدند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/658654" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658653">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvu9nCf3Bxd3HXIc7j_FUW_io-ayNmz9I77_mHfF84P5Uhh4TWb0a8pI1KZJqTd7rriZynMBEaoQkZuGqbRb0bllQZYGZyP2S2psl2UkbZ9XvwjvVbEBZC58mQXexjVOGVLGIA2RfwwX2mIO6IeK_GBX1rAjcJsFY5lgyit93uC2bq0sH2cKKi1wm67TpQe3zZPdCdK5_ZedL_fTHkdavhspK2jRzjEIVOblT9RGfmeEpMLFe_OM_nCVsKmnJsyJkycCtjAq2Jo4DlKd0neYQ3ShoB5WWFKezvS-rSsQ_wiGhXs52cRYIHcX9O2u6nxDrYVchz01uZbYXFuA3VISZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعد از کارت بازی داور برزیلی در افتتاحیه جام جهانی، این تصویر عجیب هم ثبت شد!
🔹
البته جدا از خشونت جام ۲۳ تا الان، کیفیت لباس‌ها زیر سوال رفت و ضربه اقتصادی عجیبی هم به کمپانی «پوما» وارد خواهد شد!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/658653" target="_blank">📅 09:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658650">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9FN8GxMdv2FzMrlX2exm-_ml-xDFFC7nOgcFiTK4QzThevLHzT25pqiWVKn6Xj-4Nr-Nxe_ALjZUZS-ZZDnEtUC4KFmvzeRfrRM_p34M2qZKEmUr1r6EIk6bPIQFHpzuhN02sDAK2T1ljGNGhY_7R_Xm_wOxZAZndHKEZDsfBvU4anfWkCsG3DEHwl7seIDls34p1b5TRSVSJO98EAJIucpedzUgAjmgeY3mhZyZRT2JPhWwwdJiJt7vA-uvRznpQrpSUUCu2NnmpF16jeLnlACaTIZuXJLocexhThdwfKTlFeCC9oRngDxj1t3uYZx_wb131cq4hfK5K1M-zNEzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین اتفاق تلخ جام جهانی ۲٠۲۶| مرگ یک هوادار در جریان دیدار افتتاحیه
🔹
یک هوادار آلمانی پنجشنبه در نزدیکی ورزشگاه مکزیکو سیتی در جریان دیدار افتتاحیه مکزیک و آفریقای جنوبی در جام جهانی ۲۰۲۶ جان خود را از دست داد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/658650" target="_blank">📅 09:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658649">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c602ebbfd.mp4?token=R83vak5CI8IjZauRvQL1BC1ifUO22nIoVpJM99oDBjqrJDO_Qo30ZYWDMVvUTY3CiDj14CYkeIzpfX3HbTx7VHis2gEfCgOcR2dvZeMLqYu9HBfWNHf32Nr-iXeRxdMsfNg_cYahjhoJln2Qrwc_A23bweLiQlzlPwpY2A90N2IgAkqbceU7bKvCsUBVqYn2o5EgOEw4-5l5A_lLEIXcwPmkvzc9zfBisj7_6zaPRqIk_LELO_MTrfBPK-5Vi9Emoq4QLEylYzp1dvaDotfZSDh6WEM58xCcO8StMhrDP0ApzkqS7OQckr0K1IxWBLYn8suDR5tsIEesfy4aXVQf7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c602ebbfd.mp4?token=R83vak5CI8IjZauRvQL1BC1ifUO22nIoVpJM99oDBjqrJDO_Qo30ZYWDMVvUTY3CiDj14CYkeIzpfX3HbTx7VHis2gEfCgOcR2dvZeMLqYu9HBfWNHf32Nr-iXeRxdMsfNg_cYahjhoJln2Qrwc_A23bweLiQlzlPwpY2A90N2IgAkqbceU7bKvCsUBVqYn2o5EgOEw4-5l5A_lLEIXcwPmkvzc9zfBisj7_6zaPRqIk_LELO_MTrfBPK-5Vi9Emoq4QLEylYzp1dvaDotfZSDh6WEM58xCcO8StMhrDP0ApzkqS7OQckr0K1IxWBLYn8suDR5tsIEesfy4aXVQf7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمام دفعاتی که ترامپ ادعا کرد به توافق با ایران نزدیک شدیم!
🔹
۳۹ ادعا در یک نگاه
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/658649" target="_blank">📅 09:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658648">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca12a42c85.mp4?token=nItcZ1X1gI3AfObKCx7m6zB0xJeTXkGqWBUJii3oO8J5IdxU4Dd0QccgmN59KikSfJ8YPW3JSzNm8zIxgKa5pCXwba7lMlGzwylfFetx91-Hh7e-RO1eayPbfYckvcMZqzwYbGdRY8EwPmokUnY1CM0ksJ-r76SEm7TavalhBfu5Xyi8VxckTYa5R2JKdkEtEhHyCyg7iJE_emiTtOQtYRRYRuEZ-IAcLaE4fZfdH2H7ieBWXogn9IdvkvO5qKofLCSsn_JszHVlRZZmyuKljVQR2vTccsXFJdC4kPiQlwhR3tbMz6eccg65rZPRP3oJpT2fwNK13VHff_LQbeP6lH5dVJdwiy3igGumoCsOMvplegI5KEeqnJW-AZRF0_e7likoxyQE9dLiadW6fGO6VTNy3t1n5yjtflRvsEslTdVUb_hwOFWyrW2X2ogvwANgKijJfTe9IdlwKPlHUKw0mQz5E0BzHpxkRw_YDymPnpVC3IgonTenBzLQKhhfhBIw3RgfAdG10VU1lGLFbwBBIUPszTF9hibL1nEhISKja2x2Ec7wv1RHT__NhsEI3M4EHpeZ_u1qrnHR1DK_q8MUCM0clWUvuX2m9JBf83IJGsLVV6t9ID3PdC8mMuVgzPSs3OtYjfjIFGL4M0-tA3zLsvuWgsasyuLDTNlYh_Rqj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca12a42c85.mp4?token=nItcZ1X1gI3AfObKCx7m6zB0xJeTXkGqWBUJii3oO8J5IdxU4Dd0QccgmN59KikSfJ8YPW3JSzNm8zIxgKa5pCXwba7lMlGzwylfFetx91-Hh7e-RO1eayPbfYckvcMZqzwYbGdRY8EwPmokUnY1CM0ksJ-r76SEm7TavalhBfu5Xyi8VxckTYa5R2JKdkEtEhHyCyg7iJE_emiTtOQtYRRYRuEZ-IAcLaE4fZfdH2H7ieBWXogn9IdvkvO5qKofLCSsn_JszHVlRZZmyuKljVQR2vTccsXFJdC4kPiQlwhR3tbMz6eccg65rZPRP3oJpT2fwNK13VHff_LQbeP6lH5dVJdwiy3igGumoCsOMvplegI5KEeqnJW-AZRF0_e7likoxyQE9dLiadW6fGO6VTNy3t1n5yjtflRvsEslTdVUb_hwOFWyrW2X2ogvwANgKijJfTe9IdlwKPlHUKw0mQz5E0BzHpxkRw_YDymPnpVC3IgonTenBzLQKhhfhBIw3RgfAdG10VU1lGLFbwBBIUPszTF9hibL1nEhISKja2x2Ec7wv1RHT__NhsEI3M4EHpeZ_u1qrnHR1DK_q8MUCM0clWUvuX2m9JBf83IJGsLVV6t9ID3PdC8mMuVgzPSs3OtYjfjIFGL4M0-tA3zLsvuWgsasyuLDTNlYh_Rqj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احضار سرباز آمریکایی به خاطر حمایت از مردم فلسطین
🔹
سرباز آمریکایی می‌گوید من قسم نخورده‌ام که برای اسرائیل بجنگم من را به خاطر چند پست حمایتی از مردم فلسطین احضار کرده‌اند و می‌گویند مشکلی برای امنیت آمریکا هستی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/658648" target="_blank">📅 08:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1e-R6w3CxjmK78s3ptZrMj1eyx6BPube6YvJvshB20DsQEcNURnooL2cO_cJYW5-BkFe3uQvyEShNg4YL4L75UiztVr_bqVmrrt1WciPXb3KKUlK4YLJ0f3srEvi6FWTTBa1ktmruS2n59v3-W6pYCsJQFpohkwyJU-_yriDdI2g6ev-to2YzVCs4s0aEXJ4BgyawwAOh-Cr6MXwmrKV2BcdIMFwXRrEVTS8C3KvqNzCuuQyNrNCM2f7zrwu_HgeHeuOd9PMoYLCCAJEo3Ivj7ZcWdo0jzln11JuWbSJFgMesBdm_7-1NBZ1hEAPeFEsg8ysVckFSa4Tk4r9ijw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbZhVwNaHtHhZs7TAgbWc2-8s1Ea5Fng7jJXjj3MJ9iTc4FbAhsXFptM5jLtjtIKH0Ykf5ehJmxPxbf6otuRmYLKje_uFSQICoUj_UqrXg_1jh_EwaeXs2DImDjsZbpyGsCNOX1ceOelUg3sqtEmjCAOqndOQKpJ70rcZfxsUdXd5qUFVaIDxb3m5VCioe2ftWQTMEdYRNkW61Arwht6BHtarPpQKgbKh8bTJCUdByqq29iLrtS5ufdrRla-kvbWr_6k6i5nX_HaAxjQleA5aVfKMeEzJDqNx0a-asU4zuLbjTiOYCM_iQgAW7m2o2etEEw7Ek8txP6aqYbPydFHoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
فوتوشات‌های بازیکنان تیم ملی فوتبال ایران برای جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/658645" target="_blank">📅 08:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658643">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
مقام آمریکایی مدعی سرنگونی دو پهپاد ایرانی در تنگه هرمز شد
شبکه فاکس نیوز:
🔹
در پی تلاش ایران برای هدف قرار دادن کشتی‌های عبوری از تنگه هرمز، نیروهای آمریکایی دو پهپاد ایرانی را سرنگون کردند./ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/658643" target="_blank">📅 08:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658641">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n00hVtOt5JRgFaceV1lYuZ029mmw9Rb3UqF3jSc9oLZrEw69r8nnneHjUaeUKs3k37gab-X6UDR3ruBX0mX7O7VlOTdspBR2Zjr_9bLwdG9cl50PQsjegeVjay3IRXDs-_R1oxHKBKtkY6CzXH2dcNbtYmQs7cwzyGIOGeO3xxaAekjhcCCwNXTcWDYHFyXdoVEd3TjYETivjYiaFrYqgviurpow7PL-v4I2i4E-fZDJuC-TBtX1gtq2nCOV65FvvgTXod-rtlO6d3BMB1PLVZhrT5oPhJt_Koynkah1WJPgxtu_QgluAhm3j5ZRmn70Q6MDDOz8u3isIrLVHyVeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه نوجوان هندی با افشا کردن تقلب در تصحیح برگه‌ها، دولت را به دردسر انداختند
🔹
سه نوجوان هندی با شناسایی حفره‌های امنیتی و تقلب در سیستم تصحیح آنلاین اوراق، موجی از اعتراضات را برانگیختند.
🔹
این افشاگری منجر به بازبینی صدها هزار برگه امتحانی و برکناری مقامات ارشد سازمان مربوطه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/658641" target="_blank">📅 08:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658640">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DECVw4wf6TMHJ_OyIMPrVBReEVv2tClA2Zqn0-v71HnpucrtJNpeOQMjyfiTQGcNSzL21PWaGUSlYxknkF9Gmg0v8OkAHd9jxoyJcTBWnhWmEp32kSPyGdNVJmtqfDORY1RGyCMZlQkmqujCdDOpEOjLZl8z_jOvVa8CEarWSwESbjIP7P1VyqFqhq_OaA74h76TD-2pJTWv_St9a7iF-kWAs3ksIsE1M9LAdnIr22blqca5pzBolHYiKAEh_qjv4LJdxnnKkqyJtGZ9NChgeXSO7IlswO3ksMW2mzMlH0Ur5dTMF7KqNHFod47uyVrdmlSJOwVw3OTG77gakkMP_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وَلَا تَحْسَبَنَّ اللَّهَ غَافِلًا عَمَّا يَعْمَلُ الظَّالِمُونَ...
And never think that Allah is unaware of what the wrongdoers do. He only delays them for a Day when eyes will stare [in horror].
گمان مبر خدا از آنچه ستمکاران انجام می‌دهند غافل است؛ فقط آنان را تا روزی که چشم‌ها از شدت وحشت خیره می‌شود مهلت داده است.
#WillPayThePrice
#تقاص_خواهید_داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/658640" target="_blank">📅 08:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658637">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای اکسیوس: یادداشت تفاهم ایران و
آمریکا
،
آتش‌بس را به مدت ۶۰ روز تمدید می‌کند؛ آتش‌بسی که لبنان را نیز در بر می‌گیرد
./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/658637" target="_blank">📅 08:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658636">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLmAQpifX1hDHR9J5cB79ffQkrkPqlxzBOnjLoLNh0SzPtEVsNAWvWHI71zQqruWw2zpwfcfuqBQt6w6MvFxDkb1FcqbWL7dQ1cRgfgOiskHkV-zPDUyAYO57sfGAc9ejKzYmsg6w0HyLQcEv-MDvEyQj8NRbUTAgyaQqIN7lj08O41frKLwtcNtqnHJB0BmHZVlwYkmNjIqeJy1VXH2ArEEL5caLrp3ACYvEzfSKiGoFaI_lVJWxvtFe46LSApvtqvp3vN9wrFNrS-9skw4J4fAjR7yXCTTjfIcodQOxrj7IdtE1jgiJVbQtvkhuxyk-BTgYlKsBsbq7Q9bzS5IKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پوستر AFC برای تیم‌های آسیایی حاضر در جام جهانی ۲۰۲۶ با تصویری از مهدی طارمی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/658636" target="_blank">📅 08:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658634">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGfyWY3JgxYpQazijwsuh8TL9MN715WAcybOCvR1Q25UETB_wt9KGK80rrNN-Ys7OHx4idw8WiQPvR9vRS0JJ0T9KmOM4Ef7X66b0UzBNP6Nv1gvriuUoi0ZL4hypwbl-pZU0Q-PXB4_WyHcXRA7W0O02R_eqrZvrABqkHAZ1hv6BgF7oHDPmwxzc1HiAL6RE55Y4K2fXm1O-URq6SycRE3p03i1RcDb3xnY_E3ojvGFhRtuUIXtotokec2IHEYTM2rjXAVUo-1GoBrwxIzhPXeSSmMUjrIeOX03aGuHtSB_a1vqP3zhhGOFaXeb_6iaZqwlBjkr1uXVzw4uOjakrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایلان ماسک پس از عرضه اولیه سهام اسپیس ایکس، به اولین تریلیونر جهان تبدیل شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/658634" target="_blank">📅 08:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658633">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9wu-6u-Z9LIBCoukcf_mKru04wNphhjvn_K4nfTwgu6rj3rYI5Pvr8hQhPyjg3GFwswTxZkLZwqEDeMu4O7LAf2Ta08s7LfHQtpa4eErS-D90FyFE6BxgZAyvgiD1MWLMrPqCJQzr5cZvFSov1BistY961qdL2ih-VWKpShkNXrNDbTo5InioMNZURkPncQQsoadO9Bm78nrkfMD2uwPX6g0DtHglAaS3rDvWmTqhyRy2EBtqpOYSR8_nZZ3l7rPT3GXfAyYBAPwe7dP6aZ5qNEr4mUo32A0j7ZMRbjlDdbbkdn6uHJ8msbrltG6XtXYOj63AN1z6T0ttCCiDPKjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه خبرنگار اکونومیست به اخبار ضد و نقیض ترامپ
گرگ کارلستروم، خبرنگار و تحلیلگر مشهور اکونومیست:
🔹
"اعتبار آمریکا تا آنجا تنزل یافته است که رئیس‌جمهور می‌تواند از دستیابی به یک توافق دیپلماتیک خبر دهد، اما واکنش تقریباً همگانی این باشد که:
"صبر کنیم ببینیم {خبرگزاری} «تسنیم» آن را تأیید می‌کند یا نه"
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/658633" target="_blank">📅 08:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658632">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDejc32DtRKHavLU_xDBwIriWPmTuVjBrVBP0luH8d-ppHrUjJnhUBj1vElMVmQetBaMwPc18ZLTP0XIayEcdXgYuaW-IZLiHpasMl1-8P5cQqV1t_mphCHeziZ1w9eKEn_Tl7OiethWn7AYckeVRibFWx7T6MoV_ZnrK8uwajs-PZRN73k597zVpKH0uaiG5udQCqN2k1k8XByLJC7utDRVqcZZPdhlR9gZroKuG4UMwrKwYGXq8eYsPKJ3_pjvtdCXjD725PSt60rI_XjFrXpo-qOPOMISfHHHy7_Ju_u1F3DCHDmB4YdWTnuJSv3zmpmj0Y3xqkrL7RH6iWShWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رده بندی گروه A در پایان روز اول جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/658632" target="_blank">📅 08:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658631">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
اذعان نیویورک تایمز به احتمال جنایت جنگی جدید آمریکا در ایران  روزنامه نیویورک تایمز:
🔹
براساس تصاویر ماهواره‌ای، حمله آمریکا به یک تأسیسات آبی در ایران انجام شده، اما مشخص نیست هدف‌گیری عمدی بوده یا نه.
🔹
اگر زیرساخت غیرنظامی عمداً هدف قرار گرفته باشد، ممکن…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/658631" target="_blank">📅 08:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658630">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHrEet9Av6UvKL4fAzY7jSbjzniKty97qIJsZLlIUhNMdaC4xGNq1a-lQ0LE2h72S4P7RycYDF-29amNd6nHsMPTtlsLLvnCy-8RCN1yK4ZTSr4Yg69XD-v5UpMBVaJxeBNPlH91sZfRdCxRv0EV0avrXktLyU0utAWWJUMQpTINlxkKuQiSaELYGAXgStU1jnOWkdDrVD_llUxxGFJbf4EUC1N9BANJgfoW2Qn5ezQ5J24YhKd1i_yAEBW2Xv0-IMHArLYCIoKzFrPYmv1UBfr-pYSlVnKiAHmc6KeqPna8wHGAMaQ4fcHQ2I3d2El02rLHRk8lR3Q9lZor0L6xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: امروز به جنگ با ایران پایان دادیم
رئیس‌جمهور آمریکا:
🔹
ما امروز به جنگ با ایران پایان دادیم و آن‌ها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند؛ این همان چیزی بود که ما بر آن اصرار داشتیم.
🔹
کل هدف ما همین بود؛ این موضوع ۹۵ درصد از هدف ما را تشکیل می‌داد و آن‌ها این کار را به محکم‌ترین شکل ممکن انجام داده‌اند.»
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/658630" target="_blank">📅 08:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658629">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1V3_M4vOuIHSgqi7PnLiN3DTlov1Ld1m2chnV-kLwvQWo2Wtg2YWZlOxikQuMGXKPE5uylt7lU6fr1-ZG6jjvlAmEeQFZwzv3cu7G9_paOyD7u4ZUmBEb2a-TJv7HlyrZ0SC4IxfftsZdTJW6X0rAkTeIW5Ni_9Q_54gQu1nJ2ASVE7hEFqMz4mZby51C-W1ubFAVyUtLcr93d16l1hlYnnPGY0GsPRC0wYlHn7pZaYtJO94WhtEbyu3hDMFQe6E8HttZMeRJCAlOFQtbfAVNhn0A1xzriwZIWyJuDSZkhcgtipY8_5AIPR68fx6E9ygcmTyhvch3ZLeIfdaKXHDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین برد آسیایی در جام‌جهانی
🔹
کرۀجنوبی ۲ - ۱ جمهوری چک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/658629" target="_blank">📅 07:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658628">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
پلیس مالزی خواستار ممنوعیت کامل سیگارهای الکترونیکی
🔹
پلیس مالزی درپی شناسایی ماده مخدر مصنوعی جدیدی به نام «پیو پیو» در مایعات سیگارهای الکترونیکی، خواستار ممنوعیت کامل فروش و استفاده از ویپ در این کشور شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/658628" target="_blank">📅 07:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658626">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcJAM3URhoJocPcGCrcFdpS-93_mA-emJxE5TBjk29dGscn2OawhwpKPiTfxl8cKlAQwbRuJRvzuqHdoJl0o6hLMTNt8CMgJKuz_5kquJ09uEof32iJgTNYnJrMs8fIV4NfSrq8wgpFWi9aHz4PqZuiDn52Ewp14NJix0C2Q_WCXyY9fR2NfhLTCnzJ4oKTq8KsjHDHsvcyvQiJOYdOFRxa0Oy8VXMbqFESs-pL9fpTourpOARhP9Kl5qSf9eAmU1nvAawVzSbQoIaPRRBj_c7Se88U-znTlfm3xTjifCG_cL7PFnBAUjYZOUFOB0CgR6UM-h60t3PQmVDV1x6DfaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voGDwvnomRydzbo_SSOOAFU-gYQV825Gddqv1olaNBOzieW4d8-DC0CkN4SW8da3UOpVueK2y313yYT6rpb8xQaBjBDSxV4M1neX3mdqD3FG8B3zgDxk_89Lb4xkweVDQ_NCoeEqOPdaqDerP7cQ4afrRPIHN5XbkQ693T63hR9XrDy7VJlGqqZem0IDPslV3Zrz-1gxnP1OeghwemcynvYKn_2D5QZNMqQX0wMovpF4MFpN4Jp07qCa83MnZ-FLr7TB7xybXuk34ECfV03rmcqHsaaE1ML-HJn7rnvNbtjaqkRR9jaOasjEyNQZie8fqC-AjnmM_olbwo_CWfffhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حنظله: در پاسخ به حمله علیه زیرساخت‌های آبی ایران، تأسیساتی آب ایالت کالیفرنیا را هک کردیم
گروه هکری حنظله:
🔹
در واکنش به «حملات آمریکا به غیرنظامیان و زیرساخت‌های آبی ایران»، تأسیسات آب ایالت کالیفرنیا را هک کرده است.
🔹
باوجود دسترسی به سامانه‌های مرتبط، از ایجاد اختلال در آب‌رسانی شهرهای آمریکا خودداری کرده و این اقدام تنها «هشداری» به واشنگتن بوده است.
🔹
هرگونه اقدام علیه ایران با پاسخ متقابل در حوزه زیرساخت‌های حیاتی مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/658626" target="_blank">📅 07:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658625">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luMEng6W8cGVhszROAsEQ6SQOM_zamRGKnevPJEzaEi3LTRldUo0r7fpZN5FI6Rm6VjASlVo4b_YI8gxaxKXiTtc4rq1I9HD4MnbGkUXRS49TSomi6nx2eKaYqy7kFwrYEMeumc3IAgiVDHIsYEs4XXaZ7iYI4PGScsubApOXnADCeM_y3OVl_Harc0TwVgjoOgDfSM6sentaTAAJ3nH-tfcHHEGvuuxCHID508dWy-rBQEaKeDIHC8xr2sCePDRyooZ2_MK3ybVfOtjvTusI7kfTxDJZBy9YYcdMvymtbY-3JeZbaJKRMUxkyHdmNMjLDHnmOrg6WgEisCcO0g0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۲ خرداد ماه
۲۶ ذی‌الحجه ۱۴۴۷
۱۲ ژوئن ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/658625" target="_blank">📅 07:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658623">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔹
فرصت محدود
🔹
دوستان تنها کانالی که وقتی دلار ۹۰ هزار تومن بود با قطعیت گفت دلار ۱۵۰ هزار تومن رو میبینه…
تنها کانالی که وقتی طلا حوالی ۸ میلیون بود از طلا ۱۵ میلیونی صحبت میکرد…
تنها کانالی که ماه‌ها قبل از اتفاقات اخیر درباره رسیدن درگیری‌ها به ایران هشدار داده بود…
✅
بیش از ۱۰۰۰ تحلیل منتشر کرده
✅
حتی یک تحلیل پیدا نمیکنید که به واقعیت تبدیل نشده باشه
✅
حتی یک تحلیل حذف نشده
✅
حتی یک تحلیل ویرایش نشده
✅
حتی یک تحلیل پیدا نمیکنید که با تحلیل‌های قبلی در تناقض باشه
اگه میخوای چند ماه جلوتر از بقیه باشی همین الان بزن روی لینک زیر و عضو شو                               .
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/658623" target="_blank">📅 01:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658620">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
فارس: ایران اجازه عبور نفتکش متخلف از تنگه هرمز را نداد
🔹
دقایقی قبل نیروهای ایران اجازه عبور یک نفتکش متخلف که بدون هماهنگی وارد محدوده تنگه شده بود را ندادند.
🔹
گزارش‌های مردمی نیز از شنیده شدن صدای سه انفجار در فاصله حدود دو کیلومتری ساحل از سیریک حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/658620" target="_blank">📅 01:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658619">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
شنیده شدن دو صدای انفجار در شهر بندرعباس
🔹
دقایقی پیش، صدای دو انفجار در شهر بندرعباس توسط مردم و منابع محلی گزارش شده است.
🔹
منشا صدا هنوز مشخص نیست اما پیگیری برای کسب اطلاع دقیق ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/658619" target="_blank">📅 01:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658617">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88480d9614.mp4?token=gYCiJUh-ndBSCIQHho1uZqGilSrRIX5nb7UxnrAIGDnA4uiV7QFRIZygphTWOMHXcjZkot1BQJHDrHHFlagHJYdUflVuHk61AlMIAsZSVlNz5qW1P4srDNVqsl_gieSxIJPhOTHApmECEkqNsdI88DJEDxAF4nlevmONrXzyPwM2to_M-P24yEtSVpBz9rgbP0_gWx3wWv7ejwXDYFA76uRwXp7IocQviYhOE7QOQM8VE2uGLwaP16K6urtaiNXtZvxRzUU0vYlERsfSCG0_dFDlkHto-ako_ASImJJQlxGp2bJydag32U7B8I1ZkS1rdals03o2_WGu0Nhe7H4hmSAsmMmBXzvahIHh_obElxGB7-f0fZDw2TmaiNMnSAoAZz2LSz4Ghk4pyvvDNN6_4w0Q_MtIcPDORDtXG61NrmBDXiMyrrvGPQhzIlmjkzWf4fMEgGfRtG3t8EPrhnEhRCvyycyjtx03UPpwJDnJj7ujtCcH7ke7NUpJavgHASYK7anXTX4z7hO0CU2ce0b4cFthH63zY_Dux1pFiUNl8BZg1NGR1u-QYEbqouFld_GZ3NzugkIvBSN-VmbRbpvLxHmcxE178h-OZfXkt1Q9RwyOU1P-6YCkYWHaz4ZZ-9rIPAM1r80uUruRIPD9Z5el-7A5qNL5b-q9c4mYGNKvLjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88480d9614.mp4?token=gYCiJUh-ndBSCIQHho1uZqGilSrRIX5nb7UxnrAIGDnA4uiV7QFRIZygphTWOMHXcjZkot1BQJHDrHHFlagHJYdUflVuHk61AlMIAsZSVlNz5qW1P4srDNVqsl_gieSxIJPhOTHApmECEkqNsdI88DJEDxAF4nlevmONrXzyPwM2to_M-P24yEtSVpBz9rgbP0_gWx3wWv7ejwXDYFA76uRwXp7IocQviYhOE7QOQM8VE2uGLwaP16K6urtaiNXtZvxRzUU0vYlERsfSCG0_dFDlkHto-ako_ASImJJQlxGp2bJydag32U7B8I1ZkS1rdals03o2_WGu0Nhe7H4hmSAsmMmBXzvahIHh_obElxGB7-f0fZDw2TmaiNMnSAoAZz2LSz4Ghk4pyvvDNN6_4w0Q_MtIcPDORDtXG61NrmBDXiMyrrvGPQhzIlmjkzWf4fMEgGfRtG3t8EPrhnEhRCvyycyjtx03UPpwJDnJj7ujtCcH7ke7NUpJavgHASYK7anXTX4z7hO0CU2ce0b4cFthH63zY_Dux1pFiUNl8BZg1NGR1u-QYEbqouFld_GZ3NzugkIvBSN-VmbRbpvLxHmcxE178h-OZfXkt1Q9RwyOU1P-6YCkYWHaz4ZZ-9rIPAM1r80uUruRIPD9Z5el-7A5qNL5b-q9c4mYGNKvLjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیزر فصل جدید «حسینیه معلی» ویژه ماه محرم ۱۴۰۵ منتشر شد.
حاج سید مجید بنی‌فاطمه، حاج مهدی رسولی، حاج سیدرضا نریمانی، حجت‌الاسلام سیدحسین آقامیری و کربلایی امیر برومند در میز ذاکران این فصل حضور دارند.
🔹
نجم‌الدین شریعتی نیز همچون فصول گذشته اجرای برنامه را برعهده دارد.
📺
«حسینیه معلی» از دوشنبه ۲۵ خرداد از شبکه سه سیما روی آنتن می‌رود.</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/658617" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658615">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در نزدیکی ساحل سیریک؛ جزئیات همچنان مبهم
🔹
منابع محلی در استان هرمزگان از شنیده شدن صدای انفجاری در دریا، حدود دو کیلومتری ساحل سیریک، خبر می‌دهند. هنوز علت و منبع این صدا تأیید نشده است.
🔹
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/658615" target="_blank">📅 01:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658613">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای دفتر نتانیاهو: ترامپ با نخست وزیر در مورد یادداشت تفاهمی که با ایران در حال آماده سازی برای شروع مذاکرات است، صحبت کرد
🔹
اسرائیل طرف این یادداشت تفاهم نیست، اما نخست وزیر از تعهد رئیس جمهور ترامپ به اسرائیل قدردانی کرد.
🔹
ترامپ متعهد به حذف مواد غنی‌شده، برچیدن زیرساخت‌های غنی‌سازی، محدود کردن تولید موشک و پایان دادن به حمایت ایران از نیروهای نیابتی خود است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/658613" target="_blank">📅 00:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658612">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در نزدیکی ساحل سیریک؛ جزئیات همچنان مبهم
🔹
منابع محلی در استان هرمزگان از شنیده شدن صدای انفجاری در دریا، حدود دو کیلومتری ساحل سیریک، خبر می‌دهند. هنوز علت و منبع این صدا تأیید نشده است.
🔹
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی در دست نیست، اما با توجه به دستورالعمل‌های مربوط به بسته بودن تنگه هرمز، این وضعیت احتمالی می‌تواند در همین راستا باشد.
🔹
با این حال، این فرضیه تاکنون به طور رسمی تأیید نشده است/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/658612" target="_blank">📅 00:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658611">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ترامپ ادعای خارج کردن نفت از تنگه هرمز را تکرار کرد
دونالد ترامپ، بار دیگر مدعی شد که کشورش کشتی‌های زیاد و «صدها میلیون بشکه نفت» را از تنگه هرمز خارج کرده است.
🔹
ترامپ روز گذشته هم مدعی شده بود که ارتش آمریکا در عملیاتی مخفیانه دو میلیون بشکه نفت را از تنگه هرمز خارج کرده است؛ ادعایی که به گفته کارشناسان با آمارها و داده‌های منتشرشده در تناقض قرار دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/658611" target="_blank">📅 00:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658610">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvgK2Uz_KcD3I2X6QWo7xMdzRjKnjy6ked9CC8kooooSTwSNobejnF4AL8HQRI1KgDO6y9R9mgQjaHB7iXDKPcBef0IR4_nUo57H6iO79zHgT3DWU_iS71P_fe14ECOcgTVxnQI_k4MZF-AD6-VLBbl7USpw8QI_ye5is5l-E_k5cFAgLTUt_vOa556cs6fUJN-O03o_NQmzSY6UKnj52YLqfmJrsfWBGjvKFzUpU_7-DYtXHeTRHps0UDuqRNjB3Rdr6QsFQ64qDD8mitNjKx6bpaJw9Ao6ZqcsAwc9JoYWvFdIp-BNUBdNwTP7sEAX59Tc0RlMDh-SL1WPkHaTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد تماشاچیان حاضر در بازی افتتاحیه جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/658610" target="_blank">📅 00:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658609">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ابتدا باید مراجع ذی‌ربط نظام دربارهٔ جزءبه‌جزء هرگونه تفاهمی به جمع‌بندی برسند‌
🔹
به‌محض اینکه به جمع‌بندی نهایی برسیم رسماً اعلام می‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/658609" target="_blank">📅 00:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658608">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: اعلام تاریخ برای امضای تفاهم، گمانه‌زنی رسانه‌ای است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/658608" target="_blank">📅 00:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658607">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: به‌دلیل اقدامات غیرقانونی آمریکا در تعرض به ایران، روند دیپلماتیک هم تحت تأثیر قرار گرفته است
🔹
میانجی‌ها فعال هستند و ما خیلی شفاف به آن‌ها [مواضع‌مان] اعلام کرده‌ایم‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/658607" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658606">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: اگر قرار بود ایران تحت فشار و تهدید از مواضع اصولی خود کوتاه بیاید، یک‌سال قبل این کار را انجام می‌داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/658606" target="_blank">📅 00:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658605">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUuAOX1sQZ5-rAw5v27VMDIP9SAP5in9TLiX-ojwn8TdGEqjMJnBUiILLyN9PlrR0-YzkElsG1J3j3jUq3EP3SimDBoxurma8zlMIon-pTts70MuokEMlU9FzumXc2SDH7eXeJDBc3z_JE3CKTm-Td-vgASaJKXb5KBCH6dIJTM1mWyf7nJYtnogXEbfSJkQVMik9BkZaowGallE82zxw9WBvi7geJZzGc4KmO6Hoc2tTJPD8LLo7txTHrMnW5GeluEXq9yL5au0aJadnzHi_w8vGEEI9VbSR7duSOWwYGX3gOT5ACGxDIXFh7sEgF8PLTQFliI6EkbqO14cK3OKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز عادی نخواهید داشت. هر روزتان را تبدیل به کابوس میکنیم
לא יהו לכם יום רגיל. אנחנו נהפוך כל יום שלכם לסיוט.
#WillPayThePrice
#تقاص_خواهید_داد</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/658605" target="_blank">📅 00:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658604">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
بقایی: وضعیت مذاکرات از نظر ما این بود که بخش عمده متن تقریباً نهایی شده بود اما آمریکایی‌ها زیاده‌خواهی می‌کردند و درخواست‌های جدیدی مطرح می‌کردند
🔹
آن‌ها در حال القا هستند که جمهوری اسلامی تحت فشار به توافق رضایت داده است، در حالی که ما به هیچ عنوان از…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/658604" target="_blank">📅 00:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658603">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c497468ed.mp4?token=Fzyi_i-20fm4s0ZrLTaSI50dOtgZ7-QatMV6qFNOviWcStG2zOwTkgBDnjQ1RmrrMwEL8LcXzBpcHNoloIvcCNudpk5s83gr64_VUwoj3VYirMscGRClchyZbAXwym7JsQFDMFioTGc2X5zU0Zm41CVTL291ok8GIX9iqIhca050yMUl1F5UFmpazXwDFIaiVxBxaZdrXL1VZz4DbRwv1jvC1ehx2PhK9vursmi_DwPyyyd338g-J2cCpuHvkGBYRz8amCBm6LpSJe4N1q59d8Y90fWjvLCWGZ8Dsq355NEGECr4E9DUDBVRjrPerdjXIRaLzzil-scUKhGWxcKyqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c497468ed.mp4?token=Fzyi_i-20fm4s0ZrLTaSI50dOtgZ7-QatMV6qFNOviWcStG2zOwTkgBDnjQ1RmrrMwEL8LcXzBpcHNoloIvcCNudpk5s83gr64_VUwoj3VYirMscGRClchyZbAXwym7JsQFDMFioTGc2X5zU0Zm41CVTL291ok8GIX9iqIhca050yMUl1F5UFmpazXwDFIaiVxBxaZdrXL1VZz4DbRwv1jvC1ehx2PhK9vursmi_DwPyyyd338g-J2cCpuHvkGBYRz8amCBm6LpSJe4N1q59d8Y90fWjvLCWGZ8Dsq355NEGECr4E9DUDBVRjrPerdjXIRaLzzil-scUKhGWxcKyqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم مکزیک روی ارسال دیدنی
خیمنز دقیقه ۶۷
🔹
مکزیک ۲ - ۰ آفریقای جنوبی
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/658603" target="_blank">📅 00:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658602">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b73ad01da8.mp4?token=jh-BXK11EySnUctJigVZypCoSWc1J9c_-IeEcbbLM7dm7D-eM3CWLn_qq0PyGgGPRKifcdduvTRFh6kYAR32oQ94sEcgW7fK2hIT2HX094bACiNH48ZU_asjukCeFVzxQ7Kp76suTFZlUV1L0gqf8TrzI6qp6Dtovj9OgKpQoaZLS2KHReVrUskmksoYTHeqogJx3HjwFTE6YkDm8fLRPptr6XgYZKxe5rFUc-GUWzxkyWQsx-phZx45R0gAFvXZmFk7Tvo_FIT9fFg6m52VYyrpuQj398wkyfsWQ_qyQQWG_3lZZ3Yj6qITjkCdv98iYHb-ZmYn-u8AQsz7xiAJMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b73ad01da8.mp4?token=jh-BXK11EySnUctJigVZypCoSWc1J9c_-IeEcbbLM7dm7D-eM3CWLn_qq0PyGgGPRKifcdduvTRFh6kYAR32oQ94sEcgW7fK2hIT2HX094bACiNH48ZU_asjukCeFVzxQ7Kp76suTFZlUV1L0gqf8TrzI6qp6Dtovj9OgKpQoaZLS2KHReVrUskmksoYTHeqogJx3HjwFTE6YkDm8fLRPptr6XgYZKxe5rFUc-GUWzxkyWQsx-phZx45R0gAFvXZmFk7Tvo_FIT9fFg6m52VYyrpuQj398wkyfsWQ_qyQQWG_3lZZ3Yj6qITjkCdv98iYHb-ZmYn-u8AQsz7xiAJMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش فوری کاربران فضای مجازی به توییت ترامپ
🔹
دونالد ترامپ در توییتی ایران و آمریکا را مقابل هم قرار داد.
🔹
کاربران فضای مجازی هم این توییت را بی‌پاسخ نگذاشتند و با الهام گرفتن از کارتن معروف فوتبالیست‌ها و به بهانه شروع جام جهانی ۲۰۲۶ به رییس جمهور مغضوب آمریکا اینطور واکنش نشان دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/658602" target="_blank">📅 00:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658601">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قطر و پاکستان به‌عنوان میانجی‌ها فعال هستند
🔹
وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمده متن نهایی شده بود اما آمریکایی ها مواضع خود را تغییر می دادند.
🔹
ایران ثابت کرده است که در آنچه را به عنوان خط قرمز معین کرده است مماشاتی…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/658601" target="_blank">📅 00:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658600">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsTLDiCawPNC9tNot15od0nKr9b1KGsLPaNhMAwEnvptnA5sdsdvB9s3WKa-nOTWRbGFdUZHcbw7SwaOMN3UGG83hay73R5Q_87cFTIQlYS5jM6jIlwtqsYFAfzv3G9jxQPUmFSVFW93pwp9A_DPFvZyjU2ZTYZ3aF7-TlVFke_0ya_G1UuZTkI_QsAQYVwW4ratVAcO1WoPQQaY-sSR3fX6PSfoMP-M1rS77rWzF5d4OsEOdrwVIdYA2-k19tzUH5hrE4MVMcLdQlZxqF1Y8Fg1FUvnlEuQUsLR65Te_uGZzpNjdTLwSgX678FjaDosTUtJ6dAYZuBld-XOMhwp-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/658600" target="_blank">📅 00:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658599">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قطر و پاکستان به‌عنوان میانجی‌ها فعال هستند
🔹
وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمده متن نهایی شده بود اما آمریکایی ها مواضع خود را تغییر می دادند.
🔹
ایران ثابت کرده است که در آنچه را به عنوان خط قرمز معین کرده است مماشاتی ندارد. مواردی که درباره توافق مطرح می‌شود گمانه‌زنی است و موضوعی نهایی نشده است/ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/658599" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658598">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e6aafc5a.mp4?token=M5RPnTZFhNVMWrHrBCxtlgTnw4Lz9vB_RUVJi-ab7pc2-yya829tLGvMI5yeJpWiN6YEBBGv70CHlYPwXFDMY_HuKPraKxqIaaGMg7nhoFF8L-8YntKxRAewRbmInfXKNhxZBEOVSJxGLMb40KQW16qmjyQt3SASji7hKYm2e8MsFKrxyR7sGG2Z5ArCvs0vrZWfEyDgLRLTSkFNqEhQ0iWPvZ1OI78xj9GqeoDtdVmEtdL8H-te8JuB19j78S2xdazOQW3Psl151HPWCJJN1qOEt0EjhC1M7lBCLmJpAnHPFbewDKp6EPmT0LrRszGT7Abu6bF1ZBmZf6g4gpkeiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e6aafc5a.mp4?token=M5RPnTZFhNVMWrHrBCxtlgTnw4Lz9vB_RUVJi-ab7pc2-yya829tLGvMI5yeJpWiN6YEBBGv70CHlYPwXFDMY_HuKPraKxqIaaGMg7nhoFF8L-8YntKxRAewRbmInfXKNhxZBEOVSJxGLMb40KQW16qmjyQt3SASji7hKYm2e8MsFKrxyR7sGG2Z5ArCvs0vrZWfEyDgLRLTSkFNqEhQ0iWPvZ1OI78xj9GqeoDtdVmEtdL8H-te8JuB19j78S2xdazOQW3Psl151HPWCJJN1qOEt0EjhC1M7lBCLmJpAnHPFbewDKp6EPmT0LrRszGT7Abu6bF1ZBmZf6g4gpkeiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: مهلت شما برای رسیدن از این مرحله به یک توافق نهایی چیست؟
🔹
ترامپ: نمی‌خواهم مهلتی بگویم چون بعد می‌گویید من مهلت را رعایت نکردم. خیلی مهم نخواهد بود چون قرار است امضا شود.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/658598" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658597">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
عقب نشینی ترامپ و وعده امضای توافق با ایران پس از تهدیدهای تند
👇
khabarfoori.com/fa/tiny/news-3222314
🔹
مروری بر حملات آمریکا به ایران در شبانه روز گذشته؛ از جنوب تا تهران
👇
khabarfoori.com/fa/tiny/news-3222174
🔹
حمله سپاه به ۱۸ هدف مهم متعلق به ارتش آمریکا طی ۲ موج عملیاتی
👇
khabarfoori.com/fa/tiny/news-3222176
🔹
شلیک مستقیم طالبان به یک خانم تنها بخاطر شرکت در تجمعات اعتراضی حجاب و تحصیل/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3222289
🔹
آقای تاج بابت دیپورت شدن از کانادا هم دستاورد‌سازی می‌کند
👇
khabarfoori.com/fa/tiny/news-3222313
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/658597" target="_blank">📅 23:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658596">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ادعای ترامپ: تعداد زیادی کشتی و صدها میلیون بشکه نفت را از تنگه هرمز خارج کردیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/658596" target="_blank">📅 23:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658594">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ادعای نورالدین الدغیر خبرنگار الجزیره در تهران: دیگر همه چیز قطعی و تمام شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/658594" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658593">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای ترامپ: تعداد زیادی کشتی و صدها میلیون بشکه نفت را از تنگه هرمز خارج کردیم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/658593" target="_blank">📅 23:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658592">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
توهم جدید ترامپ: به ایرانی‌ها می‌ گوییم... ما از نظر نظامی در جنگ پیروز شدیم
!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/658592" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658591">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fdc227ec7.mp4?token=ZbgBjEZO6DK0USlePwpNFx1X8Y0XRuNbaPeEeJ4HAgbpygCrm20lRkklL7O-3NcQ6QRWqweBpl7FnIkN6OF2Lgz-A-A2ObRBDdM8J8RVNJg1NL9FIGhhB2nYacyXSBDAxO62gZCLg9LYDWJk48uyTsIZfsw7rPjQeQdakVtBcCs32c3mXsuJuIVzlr6AEUTNe72Tc3SKIpjpDIrFYXBW45Lwm1pMNE3Sg6wrMjRYRVH0ZcDo_xLNcxCvFZ4kaofUD-G4AqK2tfPmh9IpZ9GqoNLDeAazQqYBAL9drZihmHhY8c2OLBD537j3QzSuKxOQigJQ09cNRY5KWDQ-OKyKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fdc227ec7.mp4?token=ZbgBjEZO6DK0USlePwpNFx1X8Y0XRuNbaPeEeJ4HAgbpygCrm20lRkklL7O-3NcQ6QRWqweBpl7FnIkN6OF2Lgz-A-A2ObRBDdM8J8RVNJg1NL9FIGhhB2nYacyXSBDAxO62gZCLg9LYDWJk48uyTsIZfsw7rPjQeQdakVtBcCs32c3mXsuJuIVzlr6AEUTNe72Tc3SKIpjpDIrFYXBW45Lwm1pMNE3Sg6wrMjRYRVH0ZcDo_xLNcxCvFZ4kaofUD-G4AqK2tfPmh9IpZ9GqoNLDeAazQqYBAL9drZihmHhY8c2OLBD537j3QzSuKxOQigJQ09cNRY5KWDQ-OKyKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: آیا رهبر معظم ایران این توافق را تأیید کرده است؟
🔹
ترامپ: تا جایی که می‌دانم پاسخ بله است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/658591" target="_blank">📅 23:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658590">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f17a9b2ac.mp4?token=qB0sgBzs73JBv85yHX-2XmcaOrdu2WWk9FzktyxzZbj6RaZcNw4rexiiO51FXBhrUnJj6ZTL1J3EXS9-GeLrl8YclzfT1XRXvoARqAIcaD-KRDKHpP7x0JVOrfpwIBMKGfNTuwuoIi4ONky_iRKJQEcjdkA7GCQGHzUKD_1RyYeF3VnQ6RqpHiwFrijo28y5FF2NcjRCT9-rhRrHl3tuiMh_IWkwxXMPK5ep-ugW7C1uFnww04t9mH0IPAi7j-8drCXPD-P02Nlq8czOFMiGwY6XIC2HvLPoOptOxxWKqdt_CTSrwZxITsls8yMb78NAVW9skc7lz4cTgHyBQ0FtkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f17a9b2ac.mp4?token=qB0sgBzs73JBv85yHX-2XmcaOrdu2WWk9FzktyxzZbj6RaZcNw4rexiiO51FXBhrUnJj6ZTL1J3EXS9-GeLrl8YclzfT1XRXvoARqAIcaD-KRDKHpP7x0JVOrfpwIBMKGfNTuwuoIi4ONky_iRKJQEcjdkA7GCQGHzUKD_1RyYeF3VnQ6RqpHiwFrijo28y5FF2NcjRCT9-rhRrHl3tuiMh_IWkwxXMPK5ep-ugW7C1uFnww04t9mH0IPAi7j-8drCXPD-P02Nlq8czOFMiGwY6XIC2HvLPoOptOxxWKqdt_CTSrwZxITsls8yMb78NAVW9skc7lz4cTgHyBQ0FtkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: وقتی این توافق امضا شود، آیا آمریکا بلافاصله محاصره را برمی‌دارد؟
🔹
ترامپ: بله، این بخشی از توافق است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/658590" target="_blank">📅 23:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658589">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bff61170c7.mp4?token=XqFMR6VaSEbRNv4RG6Xx5CnL2bbpfELMWeK_NR64LYjGnyvzdvK3l16rkMDEFAfPQawjGV1DxEiflwPoWBxAeFMB_OMAxTAHjd3hMShY91UeIO_2aTusjCj_0aLev9oQl2HcLx543RfEM6EKJ08nN_6QZ4waZKCv-TlORMgX-HO7mgWATiUyYUSgmK1b6RfNbbFTyZHA4RfgXly27Bp5YrYziIi0zPZ6wxgg_dzW0lrqhuZq0n5LmHkRX25BHEYVWNAmb90-gFYpRQsIr-MOEaU4VT3bWmKeZQlCWvN8SSzcqF0HJSYHbYXOaoXatJzBZ5M_he7YkWtmWOjBQsqcQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bff61170c7.mp4?token=XqFMR6VaSEbRNv4RG6Xx5CnL2bbpfELMWeK_NR64LYjGnyvzdvK3l16rkMDEFAfPQawjGV1DxEiflwPoWBxAeFMB_OMAxTAHjd3hMShY91UeIO_2aTusjCj_0aLev9oQl2HcLx543RfEM6EKJ08nN_6QZ4waZKCv-TlORMgX-HO7mgWATiUyYUSgmK1b6RfNbbFTyZHA4RfgXly27Bp5YrYziIi0zPZ6wxgg_dzW0lrqhuZq0n5LmHkRX25BHEYVWNAmb90-gFYpRQsIr-MOEaU4VT3bWmKeZQlCWvN8SSzcqF0HJSYHbYXOaoXatJzBZ5M_he7YkWtmWOjBQsqcQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رودی فولر، پویول، داوید سیلوا، ماتراتزی و کولینا از دیگر چهره‌های حاضر در جایگاه ویژه استادیوم آزتکا هستند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/658589" target="_blank">📅 23:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658588">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b10fe89a2.mp4?token=O2KaUdyr38ofub3raoehcBkL8HxinuNm6FEThzXDw8oB1-a0uzpr4HZZn2Fj_AJeBpWteBqw70UkNgRgLVgMJ6dD27Nw6UlK80OuLHYWwuM1i9aX8zCMBMqRxy50BGCxdhygTErNaHX_ez5ZcKR1YcxY9ULSKYVYGcZRlsCJlHePt7CCXIW4mPEghHlYgLlP_luW1_mBRVEINL0u-rQqK7UQk58TW73YI43afnbKdKaqo9x2wtf_G-nJ2NbgPWuTW3581exPqaZx9pivJ48atRrAh0004R5Rhsz49fdyEAGZztoC3Hp9twSmmjkgD3GexDTr0V-Uk5rv-gnnQjGmCQK98Cghbn4jHWpz9idWIhC4cIObzoLqVJdQgo7pLOskOhpqe137IA9weFjY8JQlmF6Fuv2xBmCyH4v7tUeamv_UFFTl7EAVDyfhUDFDZRqfIhMN_MaJ7OUzlXqJdWAVaFwarwCHZS-gO4Y2eVtcZsK7OBSyEYze65fAcScKGDQMonBQFNBtzYDI853GU7oA9KUiVuNdku3WENEWNN6wsdOgoCvG0Kx-bnvbkVx7l1FBR2ciEnYTeJZ11QUjLveRBOZoScw0uriGVfVbMttzx37T8KFsHBVndi2SrCJ2DK9YRY5qc1rRwPMuKYE2oG3eLo5NqB8ump_BLEjad7duMsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b10fe89a2.mp4?token=O2KaUdyr38ofub3raoehcBkL8HxinuNm6FEThzXDw8oB1-a0uzpr4HZZn2Fj_AJeBpWteBqw70UkNgRgLVgMJ6dD27Nw6UlK80OuLHYWwuM1i9aX8zCMBMqRxy50BGCxdhygTErNaHX_ez5ZcKR1YcxY9ULSKYVYGcZRlsCJlHePt7CCXIW4mPEghHlYgLlP_luW1_mBRVEINL0u-rQqK7UQk58TW73YI43afnbKdKaqo9x2wtf_G-nJ2NbgPWuTW3581exPqaZx9pivJ48atRrAh0004R5Rhsz49fdyEAGZztoC3Hp9twSmmjkgD3GexDTr0V-Uk5rv-gnnQjGmCQK98Cghbn4jHWpz9idWIhC4cIObzoLqVJdQgo7pLOskOhpqe137IA9weFjY8JQlmF6Fuv2xBmCyH4v7tUeamv_UFFTl7EAVDyfhUDFDZRqfIhMN_MaJ7OUzlXqJdWAVaFwarwCHZS-gO4Y2eVtcZsK7OBSyEYze65fAcScKGDQMonBQFNBtzYDI853GU7oA9KUiVuNdku3WENEWNN6wsdOgoCvG0Kx-bnvbkVx7l1FBR2ciEnYTeJZ11QUjLveRBOZoScw0uriGVfVbMttzx37T8KFsHBVndi2SrCJ2DK9YRY5qc1rRwPMuKYE2oG3eLo5NqB8ump_BLEjad7duMsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقایان مسئول نترسید!! / با صلابت در ادبیات سیاسی کلید واژه انتقام و خونخواهی استفاده کنید
🔹
بیانیه بدید که این جنگ ادامه پیدا خواهد کرد تا وجود تمام فرماندهانی که دستور ترور رهبری را دادند از دنیا پاکسازی بشه
🔹
ما امام از دست ندادیم که دلار بگیریم!
آمریکا با لگد ما باید از خاورمیانه بیرون برود تا آرمان رهبر شهید محقق شود.
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/658588" target="_blank">📅 23:36 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
