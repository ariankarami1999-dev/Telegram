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
<img src="https://cdn4.telesco.pe/file/qugs9vHqmldfcp9S95cqbvorrRk4umsmAm_OzXz444eBmQ-LWpEM2J54kyPZnniTfb84CN5mbw1Vd9QuZNcUV-IkwIpvQlatKJXAmrTEL_L6h4tyqRQZvinchGJNk9ZQ0h3AprpyKPACcJeOKdQhC5RDlJPSfggPkAEy4MBSUDMgFheCzAr_z9d6x5L4E91YjRu1D8VqfwmL9pIHGHc2I7QyK4nXCvQEvll8qpGQfmVr_8jHsrEgrLWKkp4UbZFSewyeO-tbVbTdDbc0PmyWBeUf4LIKDOpbSSE-4iXNGsSQTKgoZx1cMfr1S7bSQfeeDiCp2HKe287XC6X_g-TelQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 921K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 17:45:14</div>
<hr>

<div class="tg-post" id="msg-147074">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سفارت ایالات متحده در امارات متحده عربی آمریکایی‌ها را به اعمال «احتیاط بیشتر» در اطراف اماکن یهودی و مرتبط با اسرائیل، از جمله اماکن عبادت، هشدار داد.
امارات متحده عربی همچنان در سطح ۳ «بازنگری در سفر» به دلیل تروریسم و تعارض مسلح قرار دارد.
این یک تهدید خاص و جدید نیست، بلکه یادآوری‌ای در میان ریسک‌های افزایش‌یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/alonews/147074" target="_blank">📅 17:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147073">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
بحرین اعلام کرد
تا زمانی که روابط دیپلماتیک با
تهران
برقرار نشود، از شرکت در هرگونه نشست با این کشور خودداری می‌کند و پیشنهاد عمان برای برگزاری نشست وزرای خلیج فارس و تهران در مورد تنگه هرمز را رد کرده است.
بحرین چهار شرط تعیین کرد: توقف حملات، پرداخت خسارت‌ها، احترام به حاکمیت و حل اختلافات از طریق قانون.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/147073" target="_blank">📅 17:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147072">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-hethfFMwjswzMUWF5IjC2vnU28D6RNp77Elyq0N57LCWrnFWJDjBCEkOdy5pWzFuQGX920rNAx9E3yipTRfUMj5NHFpG3JMhzhtW7SVSIRkVv5jtUqVS7uqdKUHYtCQ6KaSy1jZXe9VzIn4pp7hUlOjfOYfGyyh82jCakRPVTBgIn6yjAZEgrZ0Y9v4f5sLm7_LjPIce47-PUx0RJ3T8YGKY1XbNpsbOmBW_7NPz35aZv863qM_m5kQhz4C2WNj8LOBOCjFcUsawDP9hAq32fAL2WG2HXePqqDcTfQExeUS7q3Vf0rnWoX8rYXgOuTWRf8teWbbhobQvViZ6KI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای خرید آیفون ۱۸ پرو در هر کشور باید چند روز کار کرد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/147072" target="_blank">📅 17:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147071">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
رئیس‌جمهور چین، شی جین‌پینگ، پیشنهاد ایفای نقش در مذاکرات صلح میان آمریکا و ایران را مطرح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/147071" target="_blank">📅 17:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147070">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea0cc24d7.mp4?token=TN0-wECzswp1BsNBfntli7cZQ4v3OYh9b-_wGVwN5FMDOGwfHMJfKqpDXN0qFsEh8lCE-i64lzRsUpUVRFPOlBxEjop1hXX_K6WskFs9S2fmQxjr4_PTmGdzu4E19UB_wS2dH1fsh21wFSPb8j4S8luxAdv74JQ7wnMb4P7WuGLbgzqHD-pOb6aGMKCtQzEg_Rx1D_lVEflr0JLkouGo5LzM_yM929810hSlnIFqmC5Lm4YGEDyYqGaqJagd6NUCIfowOXeDqY1d3CmNLeYC6m5qG-U_dbLwCHqg6wZmDciZD2nWBmjKOJ3JJSEuAtFDAULzxzH94hCUZYL1tA1PDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea0cc24d7.mp4?token=TN0-wECzswp1BsNBfntli7cZQ4v3OYh9b-_wGVwN5FMDOGwfHMJfKqpDXN0qFsEh8lCE-i64lzRsUpUVRFPOlBxEjop1hXX_K6WskFs9S2fmQxjr4_PTmGdzu4E19UB_wS2dH1fsh21wFSPb8j4S8luxAdv74JQ7wnMb4P7WuGLbgzqHD-pOb6aGMKCtQzEg_Rx1D_lVEflr0JLkouGo5LzM_yM929810hSlnIFqmC5Lm4YGEDyYqGaqJagd6NUCIfowOXeDqY1d3CmNLeYC6m5qG-U_dbLwCHqg6wZmDciZD2nWBmjKOJ3JJSEuAtFDAULzxzH94hCUZYL1tA1PDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روته، دبیرکل ناتو: روسیه متحمل تلفات بسیار سنگینی شده است که اکنون تخمین زده می‌شود بیش از ۴۰ هزار نفر در هر ماه یا به قتل برسند یا به شدت مجروح شوند.
🔴
لحظه‌ای در این مورد فکر کنید. بیش از ۴۰ هزار نفر. در هر ماه
🔴
با وجود این تلفات سنگین، پوتین هیچ تمایلی برای پایان دادن به جنگ نشان نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/147070" target="_blank">📅 17:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147069">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwcfwBvG01lWq918J8Nh6Un8B0LL0EpAM43rJSMq1nrQwqmBNGZT-_FCBX0SRZoqppNDYBO8ookmfXt7YDojSsYS5eUZ2DE7xH-b_LV-3dsSJZ1mmQmVtoXqZ1U0rWYST9WpZ3Gv6MKq8MAjDM01PJ671ltioVXQSbKWR0AzZ-A0nkj3veUmHwoxgZXANBSocipYd0ASPHK4uoDuaHNk_YiXyk-SBzxHOw_mUmmFXEl4B23YczbCJgQqRdnjYzDcpHNwrWpEN1Vtiz5_iXj1eD82epyuQhhTDOg3d09syBZTfwdk6r0XsfynPpXCYjYFrjGOcx_x8ONqbJ7TsfEQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: ایالات متحده با یک چالش جدید مواجه است: اگر حوثی‌ها تنگه باب المندب را مسدود کنند، ضربه دیگری به اقتصاد جهانی وارد خواهد شد و 7 درصد دیگر از عرضه نفت جهانی و حدود 12 درصد از تجارت جهانی را محدود خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/147069" target="_blank">📅 17:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147068">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری / بحرین اعلام کرد که در نشست ایران درباره تنگه هرمز شرکت نخواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/147068" target="_blank">📅 16:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147067">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
دولت عراق: نخست‌وزیر با درخواست ایران برای انجام تحقیقات مشترک درباره کشف سکوهای پرتاب پهپاد در مناطق مرزی موافقت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/147067" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147066">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c66927e311.mp4?token=UG2Lf6H7u4gadW4ZVh1cy-0FYG2MTUOFK9HHxOid3PvxGLWhB3ND62rd184qM9m1xx-fH7JS3s12nhB5u34VJ8DsHHof_Tkil1fB5v9VX6ZcbKhJXur23Fe_5sVqi1FaLT1cxGIvYwlEeQ7BDDXWOj7AuLrSEHE-tdLmIfAqIlulGLi1Qgef2ezSLu2jF3Pkv2HMZrl2lH-vF9PDoCiiAm87N8_vZveVOggdMXe8v-CsWpKthJiQsASJmlvYeog-QgALYtg-BNVRYh5OtCYBAvsDXoy2thr3YX775Mj6BL9ilPEc3D9Fpr2cGL0Viud9xWTZmPSn5clyseTxIyM2SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c66927e311.mp4?token=UG2Lf6H7u4gadW4ZVh1cy-0FYG2MTUOFK9HHxOid3PvxGLWhB3ND62rd184qM9m1xx-fH7JS3s12nhB5u34VJ8DsHHof_Tkil1fB5v9VX6ZcbKhJXur23Fe_5sVqi1FaLT1cxGIvYwlEeQ7BDDXWOj7AuLrSEHE-tdLmIfAqIlulGLi1Qgef2ezSLu2jF3Pkv2HMZrl2lH-vF9PDoCiiAm87N8_vZveVOggdMXe8v-CsWpKthJiQsASJmlvYeog-QgALYtg-BNVRYh5OtCYBAvsDXoy2thr3YX775Mj6BL9ilPEc3D9Fpr2cGL0Viud9xWTZmPSn5clyseTxIyM2SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خودروهای زرهی متعلق به امارات تحت کنترل نیروهای حوثی یمنی قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/147066" target="_blank">📅 16:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147065">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsTaPeYCGYPCTT6iNkGbUkxw7BHeHT72c0UeuKq4fBvMfYFh6AMFEQqil6H85dX9uk3wm_pnGfnYUriHS3ETH1r4t-EKCdPd8jRJPSQF9JgI3X8KkW7-EZdJykk5RplL9B3Uq3gNeANOoQT8WUY94e5KCAMGONiRnozrpLGI1RZJUa7uc1-fk92Q6GWGiG528SjtubkQsCoY5ohflRyer0JHA80yeyToPizqQakKvrvPhRW712RK0TNKvsZ9VVN1HYNWxIbZVoY6tFeZqlCKImWXgAkDxbpxKqMl7jKLVgOLohaLiFLWUdUorlABaydBFV7PW34cscT555KwwLkqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارسال مقالات علمی هم تحریم شد
🔴
معاون تحقیقات و فناوری وزیر بهداشت، با انتشار تصویری از صفحه محدودیت دسترسی شرکت Salesforce به دلیل قوانین تحریم‌های آمریکا، از ممانعت کاربران ایرانی از ارسال مقاله به یک مجله علمی خبر داد
🔴
در تصویر منتشرشده، نوشته شده که این شرکت برای رعایت قوانین و مقررات کنترل صادرات و تحریم‌های اقتصادی آمریکا، دسترسی کاربران از ایران و چند منطقه و کشور دیگر را به برخی خدمات خود پشتیبانی نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/147065" target="_blank">📅 16:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147064">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: ناتو و اروپا در قبال ایران «بسیار ناامیدکننده» بوده‌اند!
🔴
ناتو نمی‌خواست در تنگه [هرمز] به ما کمک کند، با اینکه ما هیچ نفتی از این تنگه دریافت نمی‌کنیم
🔴
ما همه مین‌ها را از بین بردیم؛ دیگر هیچ مینی آنجا وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/147064" target="_blank">📅 16:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147063">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d0c57f91.mp4?token=Wq_cz9UwAzF27urSAqbu11BT7iZ4zfq5dVjU40_cTZRToP2n37yylwPV7DEcZPmwvXpQZ268CBd8usbwWd0VpX5A038GVv0_Vpv0HMTd_YtR9gBuJxGeR9YIokIxkHePj1TO-zc8sA_Ac9ArLr0itE3tnrWPJ3ighO3pOHUtm-YD8-TTG472tU1sEWto3wfAFIc25AFmdPGFcZl68T9zn27_OMV1r_GH0UWWPD3Osc9mgnAj75GpBRecoDIX9dFA3huRo7YFslqV_urrJ6byfggWQabEbP6Bq5I_17NyAKiGunfeL4irCVz2agXJi42wpSc3mI6g1ijYwgSiNsuH2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d0c57f91.mp4?token=Wq_cz9UwAzF27urSAqbu11BT7iZ4zfq5dVjU40_cTZRToP2n37yylwPV7DEcZPmwvXpQZ268CBd8usbwWd0VpX5A038GVv0_Vpv0HMTd_YtR9gBuJxGeR9YIokIxkHePj1TO-zc8sA_Ac9ArLr0itE3tnrWPJ3ighO3pOHUtm-YD8-TTG472tU1sEWto3wfAFIc25AFmdPGFcZl68T9zn27_OMV1r_GH0UWWPD3Osc9mgnAj75GpBRecoDIX9dFA3huRo7YFslqV_urrJ6byfggWQabEbP6Bq5I_17NyAKiGunfeL4irCVz2agXJi42wpSc3mI6g1ijYwgSiNsuH2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: تاسیسات هسته‌ای صلح‌آمیز باید از حمله و تهدید مصون بمانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/147063" target="_blank">📅 16:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147062">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
آرش اعلایی، خبرنگار اسبق اینترنشنال: عربستان تا ۱هفته دیگه شورتش پرچم میشه و آمریکا هم کلا منطقه رو بیخیال شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/147062" target="_blank">📅 16:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147061">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کاخ کرملین: هنوز مشخص نیست که آیا پوتین در اجلاس سران گروه ۲۰ در میامی شرکت خواهد کرد یا خیر.
🔴
اگر زلنسکی واقعاً تمایل به ملاقات با پوتین دارد، می‌تواند به مسکو بیاید
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/147061" target="_blank">📅 16:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147060">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
دلار بزودی 300هزار میشه
⁉️
🔴
تحلیل ترسناک نوستراداموس ایرانی
👇
https://t.me/+WZbLEaPPJQUwZDU0
https://t.me/+WZbLEaPPJQUwZDU0</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/147060" target="_blank">📅 16:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147059">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
حاجی دلیگانی، نماینده مجلس: طرح سه‌فوریتی خروج ایران از NPT آماده شده است
🔴
بهتر است هر چه زودتر آزمایش‌های لازم را برای سلاح هسته‌ای انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/147059" target="_blank">📅 16:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147058">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8i-yTixrY4CUB2hf4ZJGD6DohJ5nITV23s1g1_kpoGCNuNmVP4qE5YwLM2c6uVbDHu3nwn6e8inDLkAd9gRafuqLjdhe-HfMYufAYfKDeWgfyk6CJBh_MAB7y0ts4MSqeAJfGQ0yOmrf1nE6k6eHly2N3nhKCQlzLDrWEYqAYAZSES-DtL5DNJjqy3CrhF3SxGfRl1zBXTvI63jV7JAnyOxBrMPNWq744zi0hzeBoY1kBQdcJhddO0SAd1gqpedGCMBQvMqK9V68rsk959IwXbxOWiiQuymXzPCy1G0J6eUTqG2-x45qZSIPiTMVnn-c1Y6RdMQ64orly_yEQHhhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دلقک بازی امت معکوس در شب نشینی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/147058" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147057">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c3694001e.mp4?token=vAmVIcrFnJeLgRq9U_1S1ej9ojs4F44KlRsIyphBg8dZ8KzemIY008YXQENZESOBOMm8fld7TAEfeXfWoS6KsW7qHuoaKbsvqDbKUbuYy5zz7newPkQwaLP6IuZ-yAgl5PAbvoR36c708uZeEgRLQE6Kg4yt-V03xbIbSL2fZS2wZFf2Uey3g2WcmbkdO7GiUQqclonkOFl2_TweLFmaDpd6d1z5Zh7qwDEJo65hDHWSgxOdSkvcCKtJM3KLWU8pk30eTg5qBJ7g3Kal5al_zVVV0yV65ix4AcxGw_g6gZH-_1rKf4wB9anm525eNMwOntIfKgrHKAwX--DyM3n0OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c3694001e.mp4?token=vAmVIcrFnJeLgRq9U_1S1ej9ojs4F44KlRsIyphBg8dZ8KzemIY008YXQENZESOBOMm8fld7TAEfeXfWoS6KsW7qHuoaKbsvqDbKUbuYy5zz7newPkQwaLP6IuZ-yAgl5PAbvoR36c708uZeEgRLQE6Kg4yt-V03xbIbSL2fZS2wZFf2Uey3g2WcmbkdO7GiUQqclonkOFl2_TweLFmaDpd6d1z5Zh7qwDEJo65hDHWSgxOdSkvcCKtJM3KLWU8pk30eTg5qBJ7g3Kal5al_zVVV0yV65ix4AcxGw_g6gZH-_1rKf4wB9anm525eNMwOntIfKgrHKAwX--DyM3n0OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کانادا
:
به احتمال زیاد، به زودی شاهد توافقی با کانادا خواهید بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/147057" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147055">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHDrrQ2xXQ444wtBfL5WcEW0OLIvt09RepgmbOVeaiEuxk4nKUOmnPHClWBJ7vvX6xcO9xxq8R6qxX_Lq8MbSjUbxQcoT_T5e_krhAEjFTgaU6xfKl40-BO8afj7jnCaf9UJ2NH35dOedQfNshmKSnz_LPK428RH5u0-bBuoqRv_mFh8g2S_Bkg9bcPTziOnEtPnNE8HWMAotC3JLkXIlEWVxTPtvc13AhLh8unMjQm3IX8ZZAEKsbDe_N1n810U1IXtMZQlvraNTKlHZcxC0EfYREkLn8OibabgaGqa-pWxMckL47JCnWI8PoXJBVLEeCZa2IhQ5fGD9G9-2IqEig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8deb1520.mp4?token=smXOk4vojlev-i9bCo_n8Upp9T1shn-UhnHv3ngLt2wxXiLjBA_IQRJQtgGpbeVJhjxhz2ERRjCWnB73rjn8Hyur2fYPhwhv4QdJD488J9m8GeYPOlsbmy3lJdFBWJFlJnyg0VRUQwgMTQjGLSuAtFrVyixoSk91TJgXuLemr5MFJ6nQKRwGpTpBPrRUL_ewe0AmLM3tSpLN3LkMFwbU7eVvo7M6jIUQHJxu2AN31uwZqGICg2JXXxaMrYm0yhuc4ka_fOMXg7M2a_Jhz3flR-StHBRTl33fNBJ4E4J9SuPj5Lg6foKCtshDll7xZSOH-DjUHjRS3zvnAPBV_rNm3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8deb1520.mp4?token=smXOk4vojlev-i9bCo_n8Upp9T1shn-UhnHv3ngLt2wxXiLjBA_IQRJQtgGpbeVJhjxhz2ERRjCWnB73rjn8Hyur2fYPhwhv4QdJD488J9m8GeYPOlsbmy3lJdFBWJFlJnyg0VRUQwgMTQjGLSuAtFrVyixoSk91TJgXuLemr5MFJ6nQKRwGpTpBPrRUL_ewe0AmLM3tSpLN3LkMFwbU7eVvo7M6jIUQHJxu2AN31uwZqGICg2JXXxaMrYm0yhuc4ka_fOMXg7M2a_Jhz3flR-StHBRTl33fNBJ4E4J9SuPj5Lg6foKCtshDll7xZSOH-DjUHjRS3zvnAPBV_rNm3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو تهران (ونک) یه غذاخوری افتتاح شده به اسم کتلت بی بی که فقط تخصصش  کتلت درست کردنه
🔴
حالا قراره به دلایل نامعلوم پلمپ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/147055" target="_blank">📅 15:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147054">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">💵
ماهانه بالای صد میلیون تومان تو خونه خودتون با ارز دیجیتال پول دربیارید !
💰
🟢
‌‌‌‌‌‌‌دیگه مجبور نیستید برای دیگران کار کنید!
🟢
‌‌‌‌فقط با یه گوشی!
🟢
‌‌‌‌‌‌‌بدون نیاز به تجربه!
✅
‌‌‌‌‌ آموزش ۱٠٠٪ رایگـــــــــــــــــــــــــان
جا نمونین ازش لینکش
👇
👇
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/147054" target="_blank">📅 15:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147053">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40b6de5cd2.mp4?token=eEJyAyiJOZ-df-0TxCJVuQdJbNFEm_MnHBhKZ4jipfwGDP8xNzuVygBczSsLtNqi7Oo1rw9eDjamjK9H0ZVXJMajPaKA4hHkHeAwfpPzmHfH2JvmaZdqI7M1P4ZFqOJYMOCiAcm0_e8cyjBAK7LlVBAOtzkzlLT7Q7U2At4QYcGOH9NNqrkZgbE8X40aOkUCEtJU0xFDrPSO2q5TDuVtISBF0KNRljo4L7VqcePuGERjioFcmkkKvvpqGOBh3Yjh1vtGVfwHKsbTl6KmgG0M7fMoWMySn_mja8twZZh3SQva6pNBA9Vw3hB1S6gpb2qD51IuW_hHGJaEqDfSoobG2Ah8VdvGtK34RrcUvsNI4cqRz_d_a2FHHiA4Cg9ew88tQWaFR4irfyXkFm4Rzh8jfetZfP3EeZ_uAYYSC0NAjP3QiZfwjkK-THrFt6jRL7oT24GAWu7LUp92f_wf57cgw8xiJDsPAx3FD-Ky1xs213BhbJO9jR5WJw_Pqvb36a6WCgYpvLl8dw6_VxiJQ6KTdy18ckZsjWfUhWAoo3RQBTWEi0xnw9Z9mOe5QsAKWDyWuSyE9KxLo7UvsITt1nYez4GGMZnJBS25-EYI0TXHl7NsxwDNQybQz0SuT9g5XvtZha5bZKBloHc0ppYgibOxuuyzSTrXjEDInTcuuUl8-7M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40b6de5cd2.mp4?token=eEJyAyiJOZ-df-0TxCJVuQdJbNFEm_MnHBhKZ4jipfwGDP8xNzuVygBczSsLtNqi7Oo1rw9eDjamjK9H0ZVXJMajPaKA4hHkHeAwfpPzmHfH2JvmaZdqI7M1P4ZFqOJYMOCiAcm0_e8cyjBAK7LlVBAOtzkzlLT7Q7U2At4QYcGOH9NNqrkZgbE8X40aOkUCEtJU0xFDrPSO2q5TDuVtISBF0KNRljo4L7VqcePuGERjioFcmkkKvvpqGOBh3Yjh1vtGVfwHKsbTl6KmgG0M7fMoWMySn_mja8twZZh3SQva6pNBA9Vw3hB1S6gpb2qD51IuW_hHGJaEqDfSoobG2Ah8VdvGtK34RrcUvsNI4cqRz_d_a2FHHiA4Cg9ew88tQWaFR4irfyXkFm4Rzh8jfetZfP3EeZ_uAYYSC0NAjP3QiZfwjkK-THrFt6jRL7oT24GAWu7LUp92f_wf57cgw8xiJDsPAx3FD-Ky1xs213BhbJO9jR5WJw_Pqvb36a6WCgYpvLl8dw6_VxiJQ6KTdy18ckZsjWfUhWAoo3RQBTWEi0xnw9Z9mOe5QsAKWDyWuSyE9KxLo7UvsITt1nYez4GGMZnJBS25-EYI0TXHl7NsxwDNQybQz0SuT9g5XvtZha5bZKBloHc0ppYgibOxuuyzSTrXjEDInTcuuUl8-7M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جزایر فالکلند:
من نمی‌دانم که آیا بریتانیایی‌ها مایل به سفر به آنجا هستند یا خیر. این مکان بسیار دور است؛ صحبت از هفته‌ها سفر با کشتی است.
🔴
من مطمئنم که در این بحران احتمالی فراخوانده خواهم شد
🔴
احتمالاً من می‌توانم این موضوع را حل کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147053" target="_blank">📅 15:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147052">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f83c0d55.mp4?token=cS7mnCMQ2MqNL4xa9VSbyfXzo1Jt1v19fYXeM0g3u9VuVBJk_IwyYfEkrSgErpveIfmnrGGx5YuVpYssyGqDpBmySihdiPhVRik5X9ohc8faOEtxYSViBuKrVz1xtXziMNETJ49jKCn1_Cq8y3reaw156TfJtKt9d37EWyRPObYknTd2DGOS1-5qwmSCSTmfY7jSDlIXqjdczz2cwE4LvOgqo32dw2Q4TgU8XUspXvF2Iu-xls9Mvf06GKbTY0YEEg-Ne73zlXslLeCQBz9EW8mN45JeXXtmoAclfB8DlEBeYqNlkkQ6zgOpXGSMVBSlg55zKf2h3JYhTEwQ7tOVWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f83c0d55.mp4?token=cS7mnCMQ2MqNL4xa9VSbyfXzo1Jt1v19fYXeM0g3u9VuVBJk_IwyYfEkrSgErpveIfmnrGGx5YuVpYssyGqDpBmySihdiPhVRik5X9ohc8faOEtxYSViBuKrVz1xtXziMNETJ49jKCn1_Cq8y3reaw156TfJtKt9d37EWyRPObYknTd2DGOS1-5qwmSCSTmfY7jSDlIXqjdczz2cwE4LvOgqo32dw2Q4TgU8XUspXvF2Iu-xls9Mvf06GKbTY0YEEg-Ne73zlXslLeCQBz9EW8mN45JeXXtmoAclfB8DlEBeYqNlkkQ6zgOpXGSMVBSlg55zKf2h3JYhTEwQ7tOVWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره شی جین‌پینگ و چین:
مردم می‌گویند او از ما جاسوسی می‌کند، اما ما هم از او جاسوسی می‌کنیم. ما هم در این کار خوب هستیم. با یکدیگر کنار می‌آییم.
​
🔴
اینکه روابط خوبی با هم داریم، اتفاق خوبی است. اکنون روابط ما با چین خوب پیش می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/147052" target="_blank">📅 15:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147051">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ea108cac.mp4?token=a407JuPRk_E1hTUHubxO50xhj_fhiZo8bhIxpOIagCm661q4jgvLrZqFnLaEazixyZ9z1mQqYgOi95sKdXQYH7rJXVuWQ_D9ZGlTbhNEWqqZE1rM8wWA300JrfB3lFl7YzeVFReik0OOjsoRhQNGbsnrVfee28Yf9SYkQxKuk4n1XRp6dlWB7D7HFLUHD-GtLKh7oSrcLtqFCag5ZzHsF_L-D-uhRFPNVf0I2UoK1ZQHmIJxOwHoUQx9SrNu_p7-n9U0GVQ3WHD7rG7Fiy5UVmFozSbm_21xBEzu9NiIS_0LCDMeRDWGOga_OeoW2I2ieBjogWw-CIFHMwhcv4n5XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ea108cac.mp4?token=a407JuPRk_E1hTUHubxO50xhj_fhiZo8bhIxpOIagCm661q4jgvLrZqFnLaEazixyZ9z1mQqYgOi95sKdXQYH7rJXVuWQ_D9ZGlTbhNEWqqZE1rM8wWA300JrfB3lFl7YzeVFReik0OOjsoRhQNGbsnrVfee28Yf9SYkQxKuk4n1XRp6dlWB7D7HFLUHD-GtLKh7oSrcLtqFCag5ZzHsF_L-D-uhRFPNVf0I2UoK1ZQHmIJxOwHoUQx9SrNu_p7-n9U0GVQ3WHD7rG7Fiy5UVmFozSbm_21xBEzu9NiIS_0LCDMeRDWGOga_OeoW2I2ieBjogWw-CIFHMwhcv4n5XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط هواپیما در حیاط یک خانه در روسیه
🔴
در پی سقوط یک هواپیمای کوچک در حیاط یک خانه شخصی در روسیه دو نفر جان باختند
🔴
با آغاز تحقیقات کیفری، بازرسان احتمال خطای خلبان و نقص فنی را بررسی می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/147051" target="_blank">📅 15:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147050">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a405ba0f.mp4?token=Yx0lYsgwf4K5CQeJLbSZUqY-KcQP8JNla3RfX3NC3ZubVKizebKSPwITbWhzd5NNJD_jgUJ4tmacnjIqsawmiDQ_4qUQ4jB1gK8AGVVKQNS9HXroNnehCYt21HDh4AgeWIMEWXbLJI9Pno99uAz3PDYV3ayODujtoILSuMYlDuhNOkUfT_EfMPzJomPmTeG8ZlAnDvKiDXm3gxILYjpsmaLNUETl3-HeLQq86RKNMD1_RytUEDbBGnTLecHtWq3oWNNc_EfkhHMPy56Zkfs1PNluxRQQZWPFK65ttYlrSIShZlxnzj_gGFXA8IurD8sqPLNF-Gpg986Dx1Wd_Wtx8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a405ba0f.mp4?token=Yx0lYsgwf4K5CQeJLbSZUqY-KcQP8JNla3RfX3NC3ZubVKizebKSPwITbWhzd5NNJD_jgUJ4tmacnjIqsawmiDQ_4qUQ4jB1gK8AGVVKQNS9HXroNnehCYt21HDh4AgeWIMEWXbLJI9Pno99uAz3PDYV3ayODujtoILSuMYlDuhNOkUfT_EfMPzJomPmTeG8ZlAnDvKiDXm3gxILYjpsmaLNUETl3-HeLQq86RKNMD1_RytUEDbBGnTLecHtWq3oWNNc_EfkhHMPy56Zkfs1PNluxRQQZWPFK65ttYlrSIShZlxnzj_gGFXA8IurD8sqPLNF-Gpg986Dx1Wd_Wtx8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما: مرزهای بسته‌شده توسط عراق در چه وضعیتی هستند
🔴
ساعتی پیش مرز چذابه برای اتباع عراقی بازگشایی شده، اما هنوز خبری از بازگشایی پایانهٔ عراق به‌سمت ایران اعلام نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147050" target="_blank">📅 15:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147049">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba6f72c328.mp4?token=FnUNGHOcmtGyzl1JAXVIFPYG7KEG866hbCCjcwUd21-uFWjp3aGDd3It_pc4q3Ixfswjl190MENIcCDjd4tNBYv8c7RuIok0lf1Qdrl6KL-iAXAkG65D0_l23ueY9W4GhGjiyAg-krfdic0QdXfnH8OlqwFjNPIr_IQdlPoOwSvLl2VxqMqFHot1sjUHA7Hmd064ir8mxGly1m2SHlX2mz_ALBySH9YEMk9_oe8OBlFGHbQj0QZY8fNnx4-sbZTrm8YPbufMolS8qcsX9J_mP2g6fsaRQjyzoEKXyG_nwbBTpIn38E9_GZyGdfSioMUjeRG82VumzNkAcXG457zxeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba6f72c328.mp4?token=FnUNGHOcmtGyzl1JAXVIFPYG7KEG866hbCCjcwUd21-uFWjp3aGDd3It_pc4q3Ixfswjl190MENIcCDjd4tNBYv8c7RuIok0lf1Qdrl6KL-iAXAkG65D0_l23ueY9W4GhGjiyAg-krfdic0QdXfnH8OlqwFjNPIr_IQdlPoOwSvLl2VxqMqFHot1sjUHA7Hmd064ir8mxGly1m2SHlX2mz_ALBySH9YEMk9_oe8OBlFGHbQj0QZY8fNnx4-sbZTrm8YPbufMolS8qcsX9J_mP2g6fsaRQjyzoEKXyG_nwbBTpIn38E9_GZyGdfSioMUjeRG82VumzNkAcXG457zxeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ناتو: اصلاً چرا داریم به آن‌ها کمک می‌کنیم؟
🔴
بعداً در این‌باره بیشتر خواهید شنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/147049" target="_blank">📅 15:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147048">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/731f902b63.mp4?token=bkSl6viNfxvnR_REZp9mZaKdEU5OedtFq1vIITvfVHEcG7HAAc6sZ5yfoceS39kVxHa9_L3u1OXq7mhJxWkAODLkAjKT-L3YLnrq8aEuS_uukNB79yC1Twc0y0KeCrKKPhM2Fy4YAQ03eUKtAqBR_ZAJ5xOF_L8YoWyJg7eSvapprjrXQe_oRpZNFJTAtBtQvELr6jLT9SYe0Za6Koku_ZxGfXT_EF9hf9V_1Zmmod7AJNOmMvMdBGPJJuO-gP_oe14yshx0RtL8C4_XOaRWIcbd42nzBNvg1njbCmxmCFfzLQWPLU2RLDfQC8xFeagf9hf8kFRMsqUMPx2RlAYFVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/731f902b63.mp4?token=bkSl6viNfxvnR_REZp9mZaKdEU5OedtFq1vIITvfVHEcG7HAAc6sZ5yfoceS39kVxHa9_L3u1OXq7mhJxWkAODLkAjKT-L3YLnrq8aEuS_uukNB79yC1Twc0y0KeCrKKPhM2Fy4YAQ03eUKtAqBR_ZAJ5xOF_L8YoWyJg7eSvapprjrXQe_oRpZNFJTAtBtQvELr6jLT9SYe0Za6Koku_ZxGfXT_EF9hf9V_1Zmmod7AJNOmMvMdBGPJJuO-gP_oe14yshx0RtL8C4_XOaRWIcbd42nzBNvg1njbCmxmCFfzLQWPLU2RLDfQC8xFeagf9hf8kFRMsqUMPx2RlAYFVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما یک درگیری نظامی کوتاه داشتیم. آن‌ها می‌گویند: «آیا ممکن است از کلمه «جنگ» استفاده نکنید؟ چون وقتی از کلمه «جنگ» استفاده می‌کنید، موضوع کمی متفاوت می‌شود.»
🔴
به نظر من، این یک درگیری نظامی است. ما آن‌ها را به شدت تحت فشار قرار داده‌ایم.
🔴
در مورد ونزوئلا، ما آنجا را تحت کنترل خود درآوردیم. ما در آن جنگ پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/147048" target="_blank">📅 15:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147047">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
بیانیه مشترک گروه بریکس: بار دیگر بر تعهد خود به حل‌وفصل مسالمت‌آمیز مناقشات بین‌المللی از طریق گفت‌وگو، رایزنی و دیپلماسی تأکید می‌کنیم.
🔴
خواستار اتخاذ رویکردی چندجانبه هستیم که دیدگاه‌ها و مواضع ملی متنوع درباره مسائل مهم و حیاتی جهانی را محترم بشمارد.
🔴
بر ضرورت همکاری برای حفظ جریان روان تجارت جهانی، زنجیره‌های تأمین و جریان انرژی تأکید می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/147047" target="_blank">📅 15:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147046">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbb1aee77d.mp4?token=C4oDfPBb6kFhpIcUXG4Q7sOko5o6BNCOTviuKeQbJSlNmExgiH7WS6P_71066xnvUs5g9e4dJu_g9aVY7skdZGidc_En797jYDDuwlk0qJMxld40Ek-p_TtuSpXRwsMsqQHB_khz4KrGdfQbYHaWFdhg8wFOiywvTx_lru5ujz9XIC0Oc0eIQShg-ls0MTv4ZTs98q9S1AKS0UTnwP2d8Ph8HLzNSRQC_XGJ4kxTmMzm4pH32zrUICO9wvD7H26-6NyRldbub7KO_u46Olu9JwZj2FTzqHCI39VTYofUopRSlA1UEYtTUzMY1kNxS_P_BfajWZmt3cOujzda-sowXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbb1aee77d.mp4?token=C4oDfPBb6kFhpIcUXG4Q7sOko5o6BNCOTviuKeQbJSlNmExgiH7WS6P_71066xnvUs5g9e4dJu_g9aVY7skdZGidc_En797jYDDuwlk0qJMxld40Ek-p_TtuSpXRwsMsqQHB_khz4KrGdfQbYHaWFdhg8wFOiywvTx_lru5ujz9XIC0Oc0eIQShg-ls0MTv4ZTs98q9S1AKS0UTnwP2d8Ph8HLzNSRQC_XGJ4kxTmMzm4pH32zrUICO9wvD7H26-6NyRldbub7KO_u46Olu9JwZj2FTzqHCI39VTYofUopRSlA1UEYtTUzMY1kNxS_P_BfajWZmt3cOujzda-sowXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ونزوئلا، ما آنجا را تصرف کردیم. ما در این جنگ پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/147046" target="_blank">📅 14:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147045">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3c10d8e3.mp4?token=B3PJCConpaA2Qk1liBkZ-1pusvvk29ui5J4OpL7jnkglczTus8jtaUxHepr6Fawf7NnhODW2TnVy0PvbOR7jWWL9fnhAFo5_KtpLvh1UWOiIcT80ggSuiB6pJxKwvWX73AHb9jbDSY1k984damVraK6QTlKKVHmoIL9rwjfp49ICXTfRK9i47h-AgLyWBEnPs6HZAXmYpyu12WtoSqbWPE_0CZuG2Yg7hNLLAMJeHa24vNX0MUi_2YkiOPNp-dlplC7zmNu-edg3Z_9EwW86MCktrpsLWL9mkQoDzyXIDgUUZmWtz_DnRJMo03tclbNih1qtZpabFtMWrl4fT538-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3c10d8e3.mp4?token=B3PJCConpaA2Qk1liBkZ-1pusvvk29ui5J4OpL7jnkglczTus8jtaUxHepr6Fawf7NnhODW2TnVy0PvbOR7jWWL9fnhAFo5_KtpLvh1UWOiIcT80ggSuiB6pJxKwvWX73AHb9jbDSY1k984damVraK6QTlKKVHmoIL9rwjfp49ICXTfRK9i47h-AgLyWBEnPs6HZAXmYpyu12WtoSqbWPE_0CZuG2Yg7hNLLAMJeHa24vNX0MUi_2YkiOPNp-dlplC7zmNu-edg3Z_9EwW86MCktrpsLWL9mkQoDzyXIDgUUZmWtz_DnRJMo03tclbNih1qtZpabFtMWrl4fT538-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: از من پرسیدند: «نظر شما درباره اتحاد ایرلند و ایرلند شمالی چیست؟»
🔴
به نظر من، من پاسخ خوبی دادم
🔴
این یکی از آن سوالاتی است که در آن، مهم نیست چه بگویید، هیچ پاسخ درستی وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/147045" target="_blank">📅 14:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147044">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
صداوسیما: پس از بسته شدن دو پایانه مرزی شلمچه و چذابه به شکل یک طرفه از سوی عراق؛ از ساعاتی پیش مرز چذابه برای اتباع عراقی که قصد بازگشت دارند؛بازگشایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/147044" target="_blank">📅 14:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147043">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e22cc60c.mp4?token=n4-JT0wDMUysuIRJZBQxMyQX5hv3pbM6CqW4U22xY_IxTt5lEuy2uSSGRw7rUgSoKEZqrM9rTtKoWpPYHGLahYxmBR3B-uX3ez_ykj66sIjhvdnswm_OXUffVd3BWLfDeqGzc2VNqZ3RpT19IL3nYRW9RUFAyU0vaVzYVISTqWESSLTQvZbWLPCm1vMBp4pjdGVrwhWsCt3O8Sx1Ic7_B88tluqzaPEptQOJxWQUi6mC6T0IYq3iTDDcxvSt5d6kiB16zbc6G6OZLkm4kk8ZcGdIxlQ3BHVv_xWRitYLku9PhzyIFNSzRJpRXHfcmTe7vIXhRfou7lE3Y4Hhuu2HdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e22cc60c.mp4?token=n4-JT0wDMUysuIRJZBQxMyQX5hv3pbM6CqW4U22xY_IxTt5lEuy2uSSGRw7rUgSoKEZqrM9rTtKoWpPYHGLahYxmBR3B-uX3ez_ykj66sIjhvdnswm_OXUffVd3BWLfDeqGzc2VNqZ3RpT19IL3nYRW9RUFAyU0vaVzYVISTqWESSLTQvZbWLPCm1vMBp4pjdGVrwhWsCt3O8Sx1Ic7_B88tluqzaPEptQOJxWQUi6mC6T0IYq3iTDDcxvSt5d6kiB16zbc6G6OZLkm4kk8ZcGdIxlQ3BHVv_xWRitYLku9PhzyIFNSzRJpRXHfcmTe7vIXhRfou7lE3Y4Hhuu2HdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: خبرنگاران به قصد ضربه زدن به من سوال می‌پرسند
🔴
دونالد ترامپ: هر سوالی که می‌پرسند، قصدشان ضربه زدن است؛ آن‌ها همیشه به دنبال ضربه زدن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/147043" target="_blank">📅 14:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147042">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وای نت عبری : کشورهای خاورمیانه، سقوط جمهوری اسلامی را به نفع منطقه می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/147042" target="_blank">📅 14:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147041">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
معاون امنیتی و انتظامی استانداری خوزستان اعلام کرد: نخست‌وزیر عراق دستور داد به مسافران معطل‌مانده در دو سوی مرزهای چذابه و شلمچه، اجازه ورود داده شود.
🔴
آقای حیاتی گفت: مسافران ۲ ساعت فرصت دارند از این دو مرز عبور کنند و پس از حوالی ساعت ۱۴:۳۰، مرز دوباره بسته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/147041" target="_blank">📅 14:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147040">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9dvQUAuse_HRO5wxLXZAsbw7AKMecyHfOUlcl-juA33oTqyQMlm9VvCc8ajTHqqXhZCX0W9lzH9cqiDen9vcQTUchDSJEF8jaLF7dDgyXkmcw-Qb6zqb9dJFUHHOKZjHReNndwa6Rn51jwKqg3Hjv59RlF11wXkxjTwzGltIcd8mG8meukqv2gQJsvBQnvX3UQeYBgkVLyt4lmIRRb1P20nazsJE1_Wu2ibYfspLlZhF85RVGkSHY5VZ9FUCy9OPNcju4glfa48a4Z8Eh-IEDVVvz4b3WqZJmChKmzSPIPusmpeEhS3rtDfiQs2rFyHMtKR5sSKdJkxpr1uSebnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور در جریان حضور در اجلاس سران بریکس با محمد بن زاید آل نهیان، رئیس‌ امارات دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147040" target="_blank">📅 14:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147039">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
پزشکیان: برای ارتقای کارآمدی و سرعت بخشیدن به اجرای تصمیمات بریکس، تدابیری همچون مقاومت در برابر تحریم‌های یک‌جانبه، تبدیل رقابت‌ها به همکاری و استقرار دبیرخانه دائمی ضروری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147039" target="_blank">📅 14:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147038">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB1Y7b4Oc5G9wz9N1kYvlC3EUV-ZFvfGvQ3maww4otTe34V6mh1XI81EaV_99DLicaLOAxsxHhGfB4VY_XnXL4G6zKux3kBvThHSlrae21QJmti3rg60-UAFPFT8snm9XOszzMpw8pi0ZIs2In6Lh3yMVPIYaCUGmMqm3d0JRBSJtbLh7sSvUy1ynhifMsedwptyrh6qHXVrG3mgn6096jRDIOMGdleNy1iPIZsx6Te87ylIsXEM6WzwExmIOaKuGEixo4hpugrSJt-sCKNjomnog-VGf1jHc5X9P9wf2McARaaQ2x8Pe3CKc5uuq0nsPq0QDxUogzz4eJT2tch4cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این سوپر النینویی که الان شاهديم و البته هنوز به اوج خود نرسیده تا بحال رخ نداده بود و البته شاید تا صدها سال دیگه هم به این حد نرسه، شاید باورتون نشه تو ۷۵ سال گذشته فقط سه بار سوپر النينو رخ داده که هر سه تاشونم در برابر این سوپر النينو عددی نیستن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/147038" target="_blank">📅 14:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147037">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=dJ9vV9qlhj2Eb1SzEtGzarX1G1ENTgW59H2FXIRpdkwh5htioMigsRLlViKj6UVh-t50erHRJnFyAInvAZIEG6ZYB_h_8oxExA4jmcRm3kUklT_ZMdAC8IQSewa2R4LxQ69BYryIE7pV1ZeKxP3H3nOfiMJJ_41npecHYlbqtK4T2K4-ikuggP5zLzqzH2ptJQ0s830hIRIJ5lvQIqzIWIYNZcFs1qQ6AZeCv1bbyuhmxsMtE6fIL04qQkKwrgBZYi3iiMWjeWsJzIzoSSuj8P8rs6Q8d-3NEcbUASUdHKGFAo6nSecXUcFq5u_A_eC_UmXWszb8iVZwAL4zhYvnYJ3qb0xYepbCVnRp0PF7vd_siVsHLoLpv30xMm0zNYygbbF1erT4SgAUYASRWq0q1a_F7fD5nvCfBR-ZKynjDqRYi7zcVkRtYTrB3m36-waAdIAY2iuagVPHyQy3-yrhwBmo1LZPGpZKugc65vihNB4pQee4PH0gBvE0aUKyFhOhJfYI-gMmCsJiutNOnFLDIrfj8jS-WXlfN03X1EoRrYhuw3RYKExkfUCOPIIzks8-DQnqmsk76QMv3GB9r1mX0rECStba0f8z7w0SXSmfeKaKecsCVFr6i8v9Q3Vnrrdjp2dUB9WpCyTrGBBJm819ZbEpCCbUzGjbH4yGdjHzSAI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=dJ9vV9qlhj2Eb1SzEtGzarX1G1ENTgW59H2FXIRpdkwh5htioMigsRLlViKj6UVh-t50erHRJnFyAInvAZIEG6ZYB_h_8oxExA4jmcRm3kUklT_ZMdAC8IQSewa2R4LxQ69BYryIE7pV1ZeKxP3H3nOfiMJJ_41npecHYlbqtK4T2K4-ikuggP5zLzqzH2ptJQ0s830hIRIJ5lvQIqzIWIYNZcFs1qQ6AZeCv1bbyuhmxsMtE6fIL04qQkKwrgBZYi3iiMWjeWsJzIzoSSuj8P8rs6Q8d-3NEcbUASUdHKGFAo6nSecXUcFq5u_A_eC_UmXWszb8iVZwAL4zhYvnYJ3qb0xYepbCVnRp0PF7vd_siVsHLoLpv30xMm0zNYygbbF1erT4SgAUYASRWq0q1a_F7fD5nvCfBR-ZKynjDqRYi7zcVkRtYTrB3m36-waAdIAY2iuagVPHyQy3-yrhwBmo1LZPGpZKugc65vihNB4pQee4PH0gBvE0aUKyFhOhJfYI-gMmCsJiutNOnFLDIrfj8jS-WXlfN03X1EoRrYhuw3RYKExkfUCOPIIzks8-DQnqmsk76QMv3GB9r1mX0rECStba0f8z7w0SXSmfeKaKecsCVFr6i8v9Q3Vnrrdjp2dUB9WpCyTrGBBJm819ZbEpCCbUzGjbH4yGdjHzSAI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما کنترل بسیار قوی‌ای بر تنگه هرمز داریم. هیچ‌کس فکر نمی‌کرد که این اتفاق بیفتد.
🔴
به طور متوسط، ما روزانه حدود 25 شناور را توقیف می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147037" target="_blank">📅 14:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147036">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
گزارشگر: اگر بخواهید به مردم ایرلند که امروز در حال اعتراض هستند، چه بگویید؟ آن‌ها معترض هستند زیرا نمی‌خواهند شما به ایرلند بیایید.
🔴
ترامپ: من نمی‌دانستم که اعتراضی وجود دارد. من هیچ اعتراضی ندیده‌ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/147036" target="_blank">📅 14:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147035">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
چین ریاست سال ۲۰۲۷ بریکس را بر عهده می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147035" target="_blank">📅 14:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147034">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ : حوثی‌ها «نمی‌خواهند با ما بجنگند» و افزود که آنها با آمریکا تماس گرفته و خواستار آن شده‌اند که واشنگتن در این درگیری مداخله نکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/147034" target="_blank">📅 14:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147033">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ: فکر می‌کنم ایران موشک‌هایی دارد که می‌تواند شهرهای اروپایی را هدف قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/147033" target="_blank">📅 14:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147032">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رئیس‌جمهور چین: جنگ در خاورمیانه در خدمت منافع مشترک کشورهای عضو بریکس نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/147032" target="_blank">📅 13:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147031">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=MrYkCbjMYpREMFWhgGlDo2SaZVmDBRiTDUYOkXUK1qIUS_NTja9Pry0HtJYSNQCj3Z-Ks9ZkYEAKeMnrVkSLkW2m8CObtiMTt8E2eer4uP3zGDFDmbZPLagszi92HS5coX4r9edfs9y4DOHYzxhNrrp8CNWTaRk8-sL7eHL51ZDTbBWy8IMs20NmapydBJ7g9qXl-ChvnHJCM5WJk4jRfBMDXX-IRCyF8xnFzkM0PAPt7LMaytNMz8jOdj_apSrSc_hj9ywOLOwyfZ-bS8I6mtHopE_SgqNT7ufz-lPqGbcvmgPjqyX2y7U6SfB_WEJx8rSX1Qv9ekT3C-uXhApJ8kR1ZHb41mskkpCudpdJptsBZMvF1UqbKr5Zu_ouJv18rsdRe7ri_EPpNJbQZOjfYA8QxSr1QMHD9wuPY7LtKdv-OKkKkT-tZH_4L2M-ZOpiP-jZhkUuZKd1wY1g9dAejCDuULjUv2jjHCmx_xdan3qDSIQg_72I58o48Y249ROpzDeRQvGpnUEUgA234_r9dQ1cD1g-JfVBHM4R3ilkGkILB76O1D1lnNlh2aiyab5TGyilgckHX49Lq1jFAPXgqiPd-9HnAndJUlWlnLPWtIg-G_tlj7oVBDTdV7SOGFCS8fhJ4C34j6SHyFkpJ8MaHOnwMMwuNw7aWHf9bNl2fMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=MrYkCbjMYpREMFWhgGlDo2SaZVmDBRiTDUYOkXUK1qIUS_NTja9Pry0HtJYSNQCj3Z-Ks9ZkYEAKeMnrVkSLkW2m8CObtiMTt8E2eer4uP3zGDFDmbZPLagszi92HS5coX4r9edfs9y4DOHYzxhNrrp8CNWTaRk8-sL7eHL51ZDTbBWy8IMs20NmapydBJ7g9qXl-ChvnHJCM5WJk4jRfBMDXX-IRCyF8xnFzkM0PAPt7LMaytNMz8jOdj_apSrSc_hj9ywOLOwyfZ-bS8I6mtHopE_SgqNT7ufz-lPqGbcvmgPjqyX2y7U6SfB_WEJx8rSX1Qv9ekT3C-uXhApJ8kR1ZHb41mskkpCudpdJptsBZMvF1UqbKr5Zu_ouJv18rsdRe7ri_EPpNJbQZOjfYA8QxSr1QMHD9wuPY7LtKdv-OKkKkT-tZH_4L2M-ZOpiP-jZhkUuZKd1wY1g9dAejCDuULjUv2jjHCmx_xdan3qDSIQg_72I58o48Y249ROpzDeRQvGpnUEUgA234_r9dQ1cD1g-JfVBHM4R3ilkGkILB76O1D1lnNlh2aiyab5TGyilgckHX49Lq1jFAPXgqiPd-9HnAndJUlWlnLPWtIg-G_tlj7oVBDTdV7SOGFCS8fhJ4C34j6SHyFkpJ8MaHOnwMMwuNw7aWHf9bNl2fMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران: ما با قدرت بسیار زیادی تنگه هرمز را کنترل می‌کنیم. هیچ‌کس انتظار نداشت چنین اتفاقی بیفتد.
🔴
ما به‌طور متوسط روزانه ۲۵ قایق را از بین می‌بریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/147031" target="_blank">📅 13:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147030">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb11451447.mp4?token=govLm3oZJnSySDvoVSL85I2hesZEPl-3L3rdinHkR1Vs0uRFJaHhbB-RrZIr4dWBJuy8u8998VvCcHEh0pBItP4ZWw659xdnN1ZcVSEaWHGiRcXq59hTBn4t9rEqPRaiNZ54tRSmy3xCTEPMScm4WdJyPjamgN6_Zz7O7QyEhuK-mrEP24K0i5sTBj9zKdejKZ0gMzdxqMZKTT7qmJJiDr2da0Yf_D8Rlbwhjg29Gos9cd4hJbBir6bYhytubchhmSbKSmJOaRM7Z50zugSQI1GxVGZYFY4ebZanrWdCNhhap05tT_p2HtJ364PEQrwS-VG1zvJ6INPVCk9PvZrLkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb11451447.mp4?token=govLm3oZJnSySDvoVSL85I2hesZEPl-3L3rdinHkR1Vs0uRFJaHhbB-RrZIr4dWBJuy8u8998VvCcHEh0pBItP4ZWw659xdnN1ZcVSEaWHGiRcXq59hTBn4t9rEqPRaiNZ54tRSmy3xCTEPMScm4WdJyPjamgN6_Zz7O7QyEhuK-mrEP24K0i5sTBj9zKdejKZ0gMzdxqMZKTT7qmJJiDr2da0Yf_D8Rlbwhjg29Gos9cd4hJbBir6bYhytubchhmSbKSmJOaRM7Z50zugSQI1GxVGZYFY4ebZanrWdCNhhap05tT_p2HtJ364PEQrwS-VG1zvJ6INPVCk9PvZrLkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره غزه: اگر به غزه نگاه کنید، در حال حاضر روابط خوب زیادی در غزه در حال شکل‌گیری است.
🔴
این واقعاً شگفت‌انگیز بوده است. فکر می‌کنم ما کار بسیار خوبی انجام داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147030" target="_blank">📅 13:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147029">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=J1UoLUxqeQTRTeMRNplhzlIyxCgY7x9ScjpLLVVBXUQn4wG6a9PqFrSH62dAS8r39BUGQ0oVTHwjFOqtpameaehuRbPwcZ_IVJWFBEUgg_O5KXq9vW632XSdJzg8hvgkjdPFP0qdeqZ9cuoYT38bJ5p2qFmC7t7KNHS2RoF0NtQxZkwOtwzhQWt-ctPF19e8dB9Tb5-UmlHg9vTUNNH4rUSTBdw7kGfg0TLIif2jFJQD0AC4gj-34rGcv1bu9KfJaLC0WubTBAw0BcwFngLlDxAFOj8lNlCiFbgXwwg3KKscVnDuC2x44wtqJ_bnOAfMj1IN-BJOMIsqEbYTUFnoQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=J1UoLUxqeQTRTeMRNplhzlIyxCgY7x9ScjpLLVVBXUQn4wG6a9PqFrSH62dAS8r39BUGQ0oVTHwjFOqtpameaehuRbPwcZ_IVJWFBEUgg_O5KXq9vW632XSdJzg8hvgkjdPFP0qdeqZ9cuoYT38bJ5p2qFmC7t7KNHS2RoF0NtQxZkwOtwzhQWt-ctPF19e8dB9Tb5-UmlHg9vTUNNH4rUSTBdw7kGfg0TLIif2jFJQD0AC4gj-34rGcv1bu9KfJaLC0WubTBAw0BcwFngLlDxAFOj8lNlCiFbgXwwg3KKscVnDuC2x44wtqJ_bnOAfMj1IN-BJOMIsqEbYTUFnoQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زهران ممدانی شهردار نیویورک: قربانی اصلی حمله ۱۱ سپتامبر عمه‌ من بود که بعد از اون اتفاق نمی‌تونست با امنیت از مترو استفاده کنه چون حجاب داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147029" target="_blank">📅 13:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147028">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ: «کانادا بسیار مشتاق است که به توافق برسد؛ درست مانند ایران که بسیار مشتاق است به توافق برسد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147028" target="_blank">📅 13:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147027">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=NxXSIXK4whiqsXVAO412PkCriS1_P0Felx8ZUcq3_cQK70py7VDgztxMI3zpc94iCczy464dbOseRkUMgjTgOaNUBzGgUgDNOStlwFd27q6_ild-tCM29-DrjIYdBcAXUWarM68JLclz3MeQ3qhVHTEWgUzcRXx33OHmIXBFhQhtXBw8ektMpgEA-Mz35YxNO5QPYr0v_I-WUZb7UqdMw4_vXLN_kZPTArXXyWbWT7MvZYsgXYZ3uGWhka2CNUgrPXRxgImLnUhJBN4MCqpLxNzTfl8d0-cVVF5FoU3_QFEGX62lQPrz5z0QeuGJ2Ocwz3zh_BbX0q07_33k7p6_0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=NxXSIXK4whiqsXVAO412PkCriS1_P0Felx8ZUcq3_cQK70py7VDgztxMI3zpc94iCczy464dbOseRkUMgjTgOaNUBzGgUgDNOStlwFd27q6_ild-tCM29-DrjIYdBcAXUWarM68JLclz3MeQ3qhVHTEWgUzcRXx33OHmIXBFhQhtXBw8ektMpgEA-Mz35YxNO5QPYr0v_I-WUZb7UqdMw4_vXLN_kZPTArXXyWbWT7MvZYsgXYZ3uGWhka2CNUgrPXRxgImLnUhJBN4MCqpLxNzTfl8d0-cVVF5FoU3_QFEGX62lQPrz5z0QeuGJ2Ocwz3zh_BbX0q07_33k7p6_0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا ایران مسئول حمله به خط لوله نفتی شرق-غرب عربستان است؟
🔴
ترامپ: فکر می‌کنم آنها هستند، احتمالاً آنها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/147027" target="_blank">📅 13:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147026">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/996f54b8aa.mp4?token=I_jZWxGqmAez-hBVUMz0RkQGzWNFngGzQtN6nUizHs9BXja6ZaydxwAcc8OkAR61MH-Eh04NoRUv0pzNnkZQJCYj_mQIYsmvL01T7XrTCPwuLUgO55IiTd9Vm6AaenWWAgQPqjjGrwjGU1axR1MQD-3CyDKEuowQaGich8ZB1w1PKLKcJWtU_JZ9bH1_Ijw4csMTx2W1AnHxLfE4OLippUwXW6gatvlUQuGfME5BpoOaUQmm5AAu2zbS9j3IFAWWF67qMOfzPJ8BmTExOdnvGK0v-kRhOZGpHYSieTwpR5TNGp69l5oqe7ezTe1lxAHNy98VMchg01OfLJ1lUIw_4mtZ0mCnXupTolhQvkPlW7q_yGLDsmnaipF03vC-TSuS5btyWIwsayq3hilgcrex-GrCOBlG5LVVenK3csMEywmZQqbnT6N-JlxbVJyOqqJ_1Alm1UuOJqPbKGZbv-4khFrLl-1jPxtQo5YgItYhAmpkkh-l-gqztmYVBVidg2Ftl2WQcBP41YVxN-9xhS4c5zbJ7-RRZs-I-wSjAcE1WH096vbqccD7hGFqi16HxpvlmoV-180XVUIFfp4FPb2GsNlLCQMOxU4qjWABoKCYNi03eK4a-w1UBxfrGfkTKvAL8avI29z-dJzpzqqwodeeuIPOvgB_lQHymaS-exkRtz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/996f54b8aa.mp4?token=I_jZWxGqmAez-hBVUMz0RkQGzWNFngGzQtN6nUizHs9BXja6ZaydxwAcc8OkAR61MH-Eh04NoRUv0pzNnkZQJCYj_mQIYsmvL01T7XrTCPwuLUgO55IiTd9Vm6AaenWWAgQPqjjGrwjGU1axR1MQD-3CyDKEuowQaGich8ZB1w1PKLKcJWtU_JZ9bH1_Ijw4csMTx2W1AnHxLfE4OLippUwXW6gatvlUQuGfME5BpoOaUQmm5AAu2zbS9j3IFAWWF67qMOfzPJ8BmTExOdnvGK0v-kRhOZGpHYSieTwpR5TNGp69l5oqe7ezTe1lxAHNy98VMchg01OfLJ1lUIw_4mtZ0mCnXupTolhQvkPlW7q_yGLDsmnaipF03vC-TSuS5btyWIwsayq3hilgcrex-GrCOBlG5LVVenK3csMEywmZQqbnT6N-JlxbVJyOqqJ_1Alm1UuOJqPbKGZbv-4khFrLl-1jPxtQo5YgItYhAmpkkh-l-gqztmYVBVidg2Ftl2WQcBP41YVxN-9xhS4c5zbJ7-RRZs-I-wSjAcE1WH096vbqccD7hGFqi16HxpvlmoV-180XVUIFfp4FPb2GsNlLCQMOxU4qjWABoKCYNi03eK4a-w1UBxfrGfkTKvAL8avI29z-dJzpzqqwodeeuIPOvgB_lQHymaS-exkRtz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «ایرلندی‌ها اکنون برای سوخت گرمایشی منازل ۴۰ درصد بیشتر از قبل از جنگ پرداخت می‌کنند. پیام شما چیست؟»
🔴
ترامپ: «وقتی دریای شمال را باز کنند، قیمت‌های شما به‌شدت کاهش خواهد یافت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/147026" target="_blank">📅 13:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147025">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
هر یک دلار به 237,500 تومان رسید...
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147025" target="_blank">📅 13:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147023">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fooHXrLVPWkUoWD-cTkmz-_QO83u7f57rET5YSLbgi3nU3oR733LtXbkNm0MEubIE-Bd-LziOnDCD-hgwrBle8WeYTdNG_DOBu5qqxVXF_Res2ztSzjWNqJ60HLvIuHQEw8fuqa5kPO5Aa7G2C2JuFsjxodmSU76_YwsTg6LCVmy91sLHIPzzHH-xNg04z2J-G3BIWapwuIeTP-40w9_5IQ-YRcCKwqKOZ0J9LSoVQsijmqOw64uBCIfp_W_ka6uUOl0VmTFflz8lUXTqYfzMzkytuxcHOAquDiaN10r0SwdJR3z6Wfv7HNt1dWycf7fLvFq4rGNqZctVLscW86z6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HO2cqhml6YprWFxKTG_cyWC5iNp_10hp6NVwiWeYqCHrv8TchqEIKHArDqVRRe0pS_UBvdBz9PXkRIV2XhyA-4AnpIIU2-2wkqzLAq1d3fQ4FqIDpjl2dCYlRSzKfhU6MDxLChkQpt_fzzd1fe6z8WE7SYzW7tqhHJB55YqinBN6DtBF_VCqu7j2npvARd_umONsBNZs3TfCkCxDAoPeRDuwcM1OfBM99iuGNXi4K1EppoNT2vpoRwpQ80L6fltaNav7XAGzhYTEKdZWsyadOCsQSvpy2c5gq445AvWIqDy77MWtuWfDwZ_ssdY9zmkt_Iivm3HKRmA_Ymy967vwjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک تانکر نفتی متعلق به چین که در تنگه هرمز حضور داشت، تلاش کرد تا از این تنگه از سمت ایران عبور کند، اما سپس مسیر خود را تغییر داد و به عقب بازگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147023" target="_blank">📅 13:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147022">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
عراق دومین مرز را هم بست
🔴
مقام‌های عراقی گذرگاه چذابه در استان خوزستان را تا اطلاع ثانوی بستند. پیش از این نیز گذرگاه شلمچه از سوی عراق مسدود شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147022" target="_blank">📅 13:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147021">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزارت امور خارجه کویت حمله پهپادی به خط لوله شرق-غرب عربستان در مناطق ریاض و مدینه را به‌شدت محکوم کرد و گفت پهپادها از خاک عراق به پرواز درآمده‌اند.
🔴
کویت اعلام کرد این حمله موجب تلفات جانی و خسارات مادی شده و آن را نقض جدی حاکمیت عربستان، قوانین بین‌المللی و امنیت تأمین انرژی منطقه دانست.
🔴
این وزارتخانه از عراق خواست مانع استفاده از خاک خود برای انجام حملات بیشتر شود و بر همبستگی کامل کویت با عربستان تأکید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147021" target="_blank">📅 13:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147020">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
معاریو: سربازان ذخیره ارتش اسرائیل خواستار گسترش عملیات در داخل سوریه شده‌اند و برخی از آن‌ها ایده اشغال دمشق را مطرح کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147020" target="_blank">📅 13:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147019">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
خبرنگار: آیا از وضعیت عربستان سعودی و تحولات مربوط به تردد در تنگه نگران هستید؟
🔴
ترامپ: همه‌چیز به‌خوبی پیش خواهد رفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147019" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147018">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1D6eNDK0qw4FLVGxYRgIqBuR8uLowfx6_xXaMAUyQvU8yArkP4Afp5oMrWKPvbJ4xwKgLngyvYMGyBideRsjBpvR_TYcg2mXVy-vGPCjpOhPd6ET1ib-HTJ3oa6RZlVoYuC5GXIEzRm8GRAJK1Sx4lfzhDzThBSkkSdM2ob4zBEgiWXZp__DR6nwXz0EppIXBQJCC4ndGQ43jv_5kVQhzkKsz0qacuvH5kQ2K5qW91XXqE8r1D-RoXrbucJo6ymXLkGTntXPxzykgmuplihBAmmWpPoJSx6DQFKvMAsz3z5f3QD1MQeprP65-sAZDkwBbSMStPQV2C0sJ4e1O3tBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکرترکرز: صادرات نفت خام عربستان در چند هفته اخیر روند صعودی داشته و محموله‌های صادراتی از مسیر تنگه هرمز و تحت حفاظت سنتکام ارسال می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147018" target="_blank">📅 12:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147017">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS-helNfaDgDuXeDNgeJq9FVjIUZoujdFem_NUVBnzVJ1DgmJqOeWynFYdMcruEu8jGWSq0Bew4DqMEoiyhjHS2X6fDR3tSpJU4rr2e7oRus8AmqraIoU0KFk3z7fQQ-wEl45XfrSG3IFb8qgwFC5pxB7NIJwvVsOL1435Si_mUTWO35VFsfJiv4ELGV7KkflOYYM3bZedIvhPGPTlkEaMK_0eKYP671ix1d4jlJ2nFDAuD_5KuF3RZGxJW8QH74N1YxJE-zePLvUqb2zOrdcOKXvKDU_3tTtc5UVtjZy_Z5gwSQrmP3lVooY5MOC2RGVZ3kYFTQqMyteAl1bnunqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرود پیاپی هواپیماهای ترابری نظامی آمریکا در استان اربیل در شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147017" target="_blank">📅 12:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147016">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6d2568d3.mp4?token=ciy1iioW4NTYtFsdBi3Ip_ihhEsocE6e4UgLyreCvEd6gNnzbSThox_gMVECXR7D1KHEbHzCNs8KHQ5Evt4T-iA_VNk0ge3cfMFbHdyGkyMIYMYrgo_ozCD_Y2OQl3Vm7SCaE2SuzNqMTk6J7Fnm62QqHR3W2y-2XAHMq24Z42VZx9nG_Y1BHnojjtob8FWM0-a5RPiN-rbeMIeYNammRMjGmpc9QH4RFal0SHw86Vs3tBlwYjI_vsKP0oXaxuMXxbd99csyTnTRNC0tE3TR8xJjGVqgDGl_PP6mz3CSB_Bm8L2b6P_Ffw0d9reQLCjEhbtQ79k8sqB1wBd9TKwOa4Zcf755m8FIlUTY2hYFsLDwDBukTeEvjGAS6B5qGad7aQj6tuauWsF33LdZ47rF3mDe0o5-3rTMbv6cH8xDoPkx8VsXc2v7deJE6iaePC6_i5s3yFkacqfvcv9keTmznJm6KZizw91x67MArPoz-UlJjZnZ4oQeXyRyS90LHst9tirjiylUW1GRppaTC4Ty1XkVeUmJB_KTTcF1jds1VJlz2-4v5qMtNHxdHNKe0YXkBUOZFq-Zhl6-kN4RWtMPkoTjfzZS1GpGj7nAiAOIdv8WJSPm6daKh7455QjxtdBe6Ivb2lMA1veowtEvXLZXNpT2BHWgIwsrpyICTeYNk_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6d2568d3.mp4?token=ciy1iioW4NTYtFsdBi3Ip_ihhEsocE6e4UgLyreCvEd6gNnzbSThox_gMVECXR7D1KHEbHzCNs8KHQ5Evt4T-iA_VNk0ge3cfMFbHdyGkyMIYMYrgo_ozCD_Y2OQl3Vm7SCaE2SuzNqMTk6J7Fnm62QqHR3W2y-2XAHMq24Z42VZx9nG_Y1BHnojjtob8FWM0-a5RPiN-rbeMIeYNammRMjGmpc9QH4RFal0SHw86Vs3tBlwYjI_vsKP0oXaxuMXxbd99csyTnTRNC0tE3TR8xJjGVqgDGl_PP6mz3CSB_Bm8L2b6P_Ffw0d9reQLCjEhbtQ79k8sqB1wBd9TKwOa4Zcf755m8FIlUTY2hYFsLDwDBukTeEvjGAS6B5qGad7aQj6tuauWsF33LdZ47rF3mDe0o5-3rTMbv6cH8xDoPkx8VsXc2v7deJE6iaePC6_i5s3yFkacqfvcv9keTmznJm6KZizw91x67MArPoz-UlJjZnZ4oQeXyRyS90LHst9tirjiylUW1GRppaTC4Ty1XkVeUmJB_KTTcF1jds1VJlz2-4v5qMtNHxdHNKe0YXkBUOZFq-Zhl6-kN4RWtMPkoTjfzZS1GpGj7nAiAOIdv8WJSPm6daKh7455QjxtdBe6Ivb2lMA1veowtEvXLZXNpT2BHWgIwsrpyICTeYNk_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کثیف ترین ویدیو وایرال شده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147016" target="_blank">📅 12:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147014">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b37381aaf.mp4?token=rvrJVftRhCWE91kQS1gU2khN1UDj68-HciDhhp05LMUo5XTAGZMXN17Au0ykZtHSmtb0-BCtjxIOvlU0unSLqctdyADo3Befh3wFUWyuyh0S43lUlfBgAhJtpQnuIlAScsg4whcRX7gjuugBLmIDHsip9p92dtvznFLIu_3ZbXq2MHC_QgPPG14Bu7PwAZT5znCYGiO46LdX1g7qZWZQiaMiCiwjZkhmvvJC9rNH3nG6CQpZwO9lEb6CLdWzYgp-D3fFC1i8TDc1aUWb4xnBBIboPxiXJdXZ_9gpCDsLagA5k8PU_pknZaPQM0tyukeWsA2yf7JUxytV_Z5HmS8vWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b37381aaf.mp4?token=rvrJVftRhCWE91kQS1gU2khN1UDj68-HciDhhp05LMUo5XTAGZMXN17Au0ykZtHSmtb0-BCtjxIOvlU0unSLqctdyADo3Befh3wFUWyuyh0S43lUlfBgAhJtpQnuIlAScsg4whcRX7gjuugBLmIDHsip9p92dtvznFLIu_3ZbXq2MHC_QgPPG14Bu7PwAZT5znCYGiO46LdX1g7qZWZQiaMiCiwjZkhmvvJC9rNH3nG6CQpZwO9lEb6CLdWzYgp-D3fFC1i8TDc1aUWb4xnBBIboPxiXJdXZ_9gpCDsLagA5k8PU_pknZaPQM0tyukeWsA2yf7JUxytV_Z5HmS8vWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی عجیب
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/147014" target="_blank">📅 12:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147013">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری / سه تن از نیروهای نظامی شورای انتقالی جنوب یمن در شهر الضالع هدف تیراندازی قرار گرفته و کشته شدند.
🔴
گزارش‌ها حاکی است این حمله توسط نیروهایی انجام شده که از المخا در جنوب‌غرب یمن عقب‌نشینی کرده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147013" target="_blank">📅 12:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147012">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXx_lWHVXbXiVaFfP-Xq7G9yazuim2y1xXEdVYmN5yAqLQ6w_BRzLPCMEkpqDC6XvPLSsZNJ9swLdnijwH3f1qX7UhU_VwkqS8INXLXAbw9AeBlGuDwsvIhQHvcITAh0HysHYxmnD9ozLy4JN8Ss6fZGKeFPL3nRuSB-PR27E2Km-lIsXFMAccN7StcunaejlQAQczSZjASWW3fo-flCsDGt0Gymc_PObXCqCMR7Xe0Ux-0g9nipSQrQZ8oydffzqONKiZLXhyV43DV9TXNRuS0gKkn-CFE_IGtewOPTYPg5OkxGHs-M5luoSpQheQISY_SXVXHOQ9WZgp_Jb3e3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
درگیری‌ها میان نیروهای انصارالله و تیپ‌های غول‌پیکر وابسته به شورای رهبری ریاستی (PLC) در منطقه المضاربه در مسیر عدن، در استان لحج در جنوب یمن، همچنان ادامه دارد.
🔴
همچنین درگیری‌ها در هر سه جبهه استان تعز ادامه دارد و هر دو طرف تلاش می‌کنند پیشروی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147012" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147011">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه در گفت‌وگوبا المیادین:  نشست برنامه‌ریزی‌شده برای روز دوشنبه در سلطنت عمان، گامی اساسی برای تضمین ثبات و امنیت در منطقه خلیج فارس خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147011" target="_blank">📅 12:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147010">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
اکسیوس: دور بعدی مذاکرات اسرائیل و لبنان که قرار بود هفته جاری برگزار شود، به اکتبر موکول شد
🔴
علت، تدارکات برای مجمع عمومی سازمان ملل عنوان شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147010" target="_blank">📅 11:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147009">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
صداوسیما: لبنان به سازش تن داد و نابود شد؛ حوثی ها مقاومت را انتخاب کردند و درحال پیروزی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147009" target="_blank">📅 11:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147008">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
توضیحات دولت عراق درباره علت بستن برخی از گذرگاه‌های مرزی
🔴
نهاد اطلاع رسانی امنیتی عراق: نهادهای امنیتی ذی‌صلاح تمهیدات اداری و امنیتی را در تعدادی از گذرگاه های آغاز کرده‌اند که این امر مستلزم بسته شدن آن‌هاست.
🔴
بر اساس این گزارش، مجموعه‌ای از اقدامات قانونی لازم انجام شده و کار اطلاعاتی، تحقیقات و بررسی‌ها برای تعیین شرایط نقض‌ها و تخلفات رخ داده در این گذرگاه‌ها و تدوین راه‌حل‌ها و بررسی‌های مناسب، تشدید شده است.
🔴
بر اساس اعلام این نهاد امنیتی عراق، دو گذرگاه مرزی زرباطیه و المنذریه به روی تردد مسافران باز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147008" target="_blank">📅 11:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147007">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
فایننشال تایمز: آمریکا از نفتکش‌هایی که از تنگه هرمز عبور می‌کنند خواسته در ساعات مشخصی از روز حرکت کنند تا امکان تأمین حفاظت نظامی از آن‌ها فراهم شود
🔴
این بازه‌های زمانی عبور به دو زمان مشخص در روز کاهش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147007" target="_blank">📅 11:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147006">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRHCpE2Pf0MPML6GlELsBX_paxiMzB2kQhpyIFGcfUNb53lbfL1B6g0W16azdItae5hWCJO_HG0o3e5j0ZzOC_gOpDf9beP2E8Lf8ncQvnEPtx0yinh493CeMGNyYJYMG4mhjhbEtWYpoTZyos0fG58liR0TZl342CbWcPx6B5vvVHM55Cf2WqRkVnZdbM609cyz7V0XBMsv7HQ6iwNZu-7U6q_4UFhIjCwjS5Tc0wGLhh6RVjA-Fc2oCLFQr-h5YqOdim7U-5gxyFHze-FOfX08sy75U1f-vWnVNj9pDhvXNVXQqks6qbSLeMZJWj54Sd32hQiG1KJ02_m8hefDew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان با رئیس‌جمهور هند دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147006" target="_blank">📅 11:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147005">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/547525abfa.mp4?token=BLTSvnAWk8uZ6mlhVUI1ONYj3OW2mJDuUkDpWyhR2kKmtg8er-UZI1Nu3wAvokrbRdDSH2DEZEaWXNsykKcalwYYpFIXIlewxEPZjlBse-8mzZ9YnssGY3h2KsD41KIQTn3q01C07k7cW8-kfRaQjeu3bvusAkkcZ2oBgajYZdq3lxaMUhQL0a4_X7T6FcHatKnxZYfTq6fkA-Pn_Bjh0S8dTGRcA_EIr3vnjuid_pMLbo6c9yZh60f44UfJgoS2qLzqp4_0snC209xA8vOXGzCxK-dU6HJTA6PrQKACDe6A-Y3ogGmy8PrB6FYjch3CcE8G3KLgn71R-OsqE2XQHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/547525abfa.mp4?token=BLTSvnAWk8uZ6mlhVUI1ONYj3OW2mJDuUkDpWyhR2kKmtg8er-UZI1Nu3wAvokrbRdDSH2DEZEaWXNsykKcalwYYpFIXIlewxEPZjlBse-8mzZ9YnssGY3h2KsD41KIQTn3q01C07k7cW8-kfRaQjeu3bvusAkkcZ2oBgajYZdq3lxaMUhQL0a4_X7T6FcHatKnxZYfTq6fkA-Pn_Bjh0S8dTGRcA_EIr3vnjuid_pMLbo6c9yZh60f44UfJgoS2qLzqp4_0snC209xA8vOXGzCxK-dU6HJTA6PrQKACDe6A-Y3ogGmy8PrB6FYjch3CcE8G3KLgn71R-OsqE2XQHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ با استقبال مقامات ایرلندی وارد دوبلین شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147005" target="_blank">📅 11:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147004">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69323d53ed.mp4?token=XaUNA5oEvw8AKG_NGF1FQ4Q8bslDys_Yifkp9i--hDK7HFaR1IQ8WTgee3SB-PWIh4NCZF4EZP8__mymASn0Irz6V9STbOUl_2YmNoC-xZkmEIfiV7FlApmBLqAblFRFJc3DHuQJeQeZ1VzSnqamXuT80LLrPB8yfmMbjt4oprWvcT3wKTTXKfY1q2GMfgYAdh2z4EBx5xiVf9NATarSfI2BzxE0d186Bh3emfDOwzVXyk3udq2WAVtzYI8uvbK_pNQaXKqCYXfY7pUuAN4jx5aTTct6ji_g6oirDivMKz98tcOmlhWPiZEEWTNVs_Y5mWMSqbpR4NgxOPgQ67d_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69323d53ed.mp4?token=XaUNA5oEvw8AKG_NGF1FQ4Q8bslDys_Yifkp9i--hDK7HFaR1IQ8WTgee3SB-PWIh4NCZF4EZP8__mymASn0Irz6V9STbOUl_2YmNoC-xZkmEIfiV7FlApmBLqAblFRFJc3DHuQJeQeZ1VzSnqamXuT80LLrPB8yfmMbjt4oprWvcT3wKTTXKfY1q2GMfgYAdh2z4EBx5xiVf9NATarSfI2BzxE0d186Bh3emfDOwzVXyk3udq2WAVtzYI8uvbK_pNQaXKqCYXfY7pUuAN4jx5aTTct6ji_g6oirDivMKz98tcOmlhWPiZEEWTNVs_Y5mWMSqbpR4NgxOPgQ67d_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر نیرو: ممکن است بارش‌های سهمگین داشته باشیم/ همه آماده باشند؛ نباید غافلگیر شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147004" target="_blank">📅 11:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147003">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
معاون استاندار خوزستان: بر اساس اعلام مقامات کشور عراق، از بامداد امروز مرزهای شلمچه و چذابه تا اطلاع ثانوی بسته شده‌اند و هیچ‌گونه تردد کالا و مسافر از این مرزها انجام نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147003" target="_blank">📅 11:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147002">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58db88bf67.mp4?token=tiZhwsdaY12AwFHt8G3HSAz9EOa82N3G3xyCDOSziEJsKZR4GPsd14jQByAlumK2jbsEO-gSNfPCGEYydrrQwfCFPlVpLhc33OnCNFq7gMyPJVi0WjReFge0RKuIqcvW1Tg0k5H8pHf8rABscMaoL-jXd_3yTXAII3qDnrhgOgCGulfkchyofCrIj2FB5o7tMSrlM5tuy-IbNrrszghGIMVlIccA4fqjXkdNvJBC1umPj66pmAxeml5gGrnI0rYLWAuc8yKNjN4ruVWa9t5FuxchcT1iLMJLTqcxol9hrUKKNh8RcM_uCpaRT_KR9CD0uLs3wAkyU21JOW3XXF5czQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58db88bf67.mp4?token=tiZhwsdaY12AwFHt8G3HSAz9EOa82N3G3xyCDOSziEJsKZR4GPsd14jQByAlumK2jbsEO-gSNfPCGEYydrrQwfCFPlVpLhc33OnCNFq7gMyPJVi0WjReFge0RKuIqcvW1Tg0k5H8pHf8rABscMaoL-jXd_3yTXAII3qDnrhgOgCGulfkchyofCrIj2FB5o7tMSrlM5tuy-IbNrrszghGIMVlIccA4fqjXkdNvJBC1umPj66pmAxeml5gGrnI0rYLWAuc8yKNjN4ruVWa9t5FuxchcT1iLMJLTqcxol9hrUKKNh8RcM_uCpaRT_KR9CD0uLs3wAkyU21JOW3XXF5czQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکت عجیب مجری؛ قلقلک مهمان روی آنتن زنده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147002" target="_blank">📅 11:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147001">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
فایننشال تایمز: آمریکا از نفتکش‌هایی که از تنگه هرمز عبور می‌کنند خواسته در ساعات مشخصی از روز حرکت کنند تا امکان تأمین حفاظت نظامی از آن‌ها فراهم شود
🔴
این بازه‌های زمانی عبور به دو زمان مشخص در روز کاهش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147001" target="_blank">📅 10:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147000">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09617cd40e.mp4?token=KZQgfLjI79MsSDhRjglObG4tU4itJgNQPTSuNNrYfm5RCoA9p1YEaFBpedkuxCWsOexe2_XNLIy-iVjun2_eqvvk5lwiWCQq6GW0s9S4FepT97mwuwd_D53Uemgf3hVS5gQzBfsICIWblTeM5xEYtOlG8tw3om4y4V4FQFW_cnmSeERjmm3GxxOTyX1iy2dQgBJ0U5RSH5PJZzmnMQHEXscd578p73jgqV5edQ548hblyMCbuWmn4LZXjkv6tS34Y4l-60_XaZnol-eT7RBDqrekGWRkgBBiN3ofI95IRf9uOpriavCVGHEU7vW5mDfU6kl9ajGHT-SIh24JZTTkGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09617cd40e.mp4?token=KZQgfLjI79MsSDhRjglObG4tU4itJgNQPTSuNNrYfm5RCoA9p1YEaFBpedkuxCWsOexe2_XNLIy-iVjun2_eqvvk5lwiWCQq6GW0s9S4FepT97mwuwd_D53Uemgf3hVS5gQzBfsICIWblTeM5xEYtOlG8tw3om4y4V4FQFW_cnmSeERjmm3GxxOTyX1iy2dQgBJ0U5RSH5PJZzmnMQHEXscd578p73jgqV5edQ548hblyMCbuWmn4LZXjkv6tS34Y4l-60_XaZnol-eT7RBDqrekGWRkgBBiN3ofI95IRf9uOpriavCVGHEU7vW5mDfU6kl9ajGHT-SIh24JZTTkGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید ترامپ در ایکس : با این رئیس جمهور در سر کار بازی نکنید، زیرا نتیجه خوبی نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147000" target="_blank">📅 10:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146999">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPgvyEnH4OYaj1pJiUTvE3O0B1t45niI3Mbcrz6S59AfhPlQ7PovJCzlOe0p1lctgFlv47Bjj2LmkeRwVY4fbEaQAopfhYtAx7EYG4BEqjRabNoPgdKBJYUGxNCkg3oZ5F9gRCx-1ZAUejiIAkelh2Et3BemBAnmUghF2430Np8pZ3v9ND3hTI_ht67-_nGOE75dJHr6XYkeYNQ4Ba6To7OpOs5ZQ_qOg3wfmOzTrEfI8Y-K-cVWiwvyQtTCqhwviSnOOtGdNdc-U4b5OT51FAeISnQ8NT66eITrvJCOW3Q9j7kxedzHi0_3xdlUZGi4cEcT5GWy4McPqbepWR7uJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی: بدون پذیرش شروط ایران مذاکره‌ای در کار نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146999" target="_blank">📅 10:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146994">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad0ba6154.mp4?token=QUPzqibb-guEJLMf2PY42UnJKbaiUKRjDAnx8jKz_NnW4pHvPH9eIJzO00Qg6R2jVznD_iacWkJAx2N-rqzApGL3K4QdaNlMzNz0p-f5t58PFd7M61iF1Qpyh15hZ7wckIBJ8OEEx2CMELmSB1m9kCvjgWIHyhcdP0cECepsWwKo2shMpFZ1HiOIaePq_xRE7yVPiZ_o0s5TQmNFSpD68IfPvuxFEAsxKJvFx6Ywb8ACUXDvGFSNi7HXdrdMubpW1xqceRagDVcBNStl3n0Sjiw5rblPQ9bBW819ezgdVaCfKWNWa7Qe3Hjk9BLU3eohSEx6wu5SWr9kUFpmkHPVmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad0ba6154.mp4?token=QUPzqibb-guEJLMf2PY42UnJKbaiUKRjDAnx8jKz_NnW4pHvPH9eIJzO00Qg6R2jVznD_iacWkJAx2N-rqzApGL3K4QdaNlMzNz0p-f5t58PFd7M61iF1Qpyh15hZ7wckIBJ8OEEx2CMELmSB1m9kCvjgWIHyhcdP0cECepsWwKo2shMpFZ1HiOIaePq_xRE7yVPiZ_o0s5TQmNFSpD68IfPvuxFEAsxKJvFx6Ywb8ACUXDvGFSNi7HXdrdMubpW1xqceRagDVcBNStl3n0Sjiw5rblPQ9bBW819ezgdVaCfKWNWa7Qe3Hjk9BLU3eohSEx6wu5SWr9kUFpmkHPVmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری‌هایی در شهر سراوان در استان
سیستان و بلوچستان ایران
میان نیروهای امنیتی ایران و اعضای جبهه مبارزان خلق (PFF)، که پیش‌تر با نام جیش‌العدل شناخته می‌شد، رخ داد.
🔴
این درگیری‌ها پس از آن آغاز شد که نیروهای ایرانی به یکی از
مخفیگاه‌های این گروه
یورش بردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146994" target="_blank">📅 10:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146993">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رویترز به نقل از دو منبع امنیتی بغداد: عراق پس از حمله پهپادی به خط لوله نفت عربستان سعودی، در اقدامی احتیاطی گذرگاه مرزی شلمچه با ایران رو بست
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/146993" target="_blank">📅 10:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146992">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18db6ddd86.mp4?token=LP3btO9D63IekplSft0K-hejNXCIqod_PvkabXmQCWkI_Q4Okp2v1LB8n0fGWZfK1n0TlEnOSDTCAI_UROAzw1ACnlA_sjl-KsIzZYQiE94SaTFVkbPCk5hQSI5FMlTdp-pk2hQzS-hTdAznmgMWINUerAdBVtfKQqAG1JERWDfCjdSzYUzD88kxMR8z4guU06rwlieBVETF7AJ6x7Xm5Dy1HYZkJ7a_rNhodE3d2PgnKiLgVZNhJPDj_RPW7U11mw055L9oEE-lY8Kbcs0k1ZoWeqtc-wW7fsXL3sFONS3DKJYSSqxOqvpNKk2b_zNqGJquZ6JkuWNCmSol7JiBjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18db6ddd86.mp4?token=LP3btO9D63IekplSft0K-hejNXCIqod_PvkabXmQCWkI_Q4Okp2v1LB8n0fGWZfK1n0TlEnOSDTCAI_UROAzw1ACnlA_sjl-KsIzZYQiE94SaTFVkbPCk5hQSI5FMlTdp-pk2hQzS-hTdAznmgMWINUerAdBVtfKQqAG1JERWDfCjdSzYUzD88kxMR8z4guU06rwlieBVETF7AJ6x7Xm5Dy1HYZkJ7a_rNhodE3d2PgnKiLgVZNhJPDj_RPW7U11mw055L9oEE-lY8Kbcs0k1ZoWeqtc-wW7fsXL3sFONS3DKJYSSqxOqvpNKk2b_zNqGJquZ6JkuWNCmSol7JiBjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، در تیک‌تاک:
«تازه از دالاس برگشتم؛ جایی که یک کنوانسیون فوق‌العاده داشتیم. دو شب بزرگ و دو سخنرانی مهم داشتیم. باورنکردنی بود.
🔴
جمهوری‌خواهان عملکرد بسیار خوبی دارند. اما همه می‌پرسند: «چطور این کار را انجام می‌دهی؟» چون الان هنوز اوایل کار است و من در دفتر بیضی کاخ سفید هستم.
🔴
می‌دانید چطور این کار را انجام می‌دهید؟ باید کاری را که انجام می‌دهید دوست داشته باشید. اگر عاشق کاری باشید که انجام می‌دهید، دیگر شبیه کار کردن نیست.
🔴
و من عاشق دوباره بزرگ کردن آمریکا هستم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146992" target="_blank">📅 10:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146991">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d5dd1149.mp4?token=gN_HjZqpWtVtXqMMJH4qLem3O4jCqZm9w6jqWw159z4rXD9PcBkcerW8pwB0BQb8Sj7PHEpaTuddyfE56ZvnnHQRgQnjB0rUmPVtlu23rUYT2-jBzPXqE3Dg8b0pTIOWqgVFPm_TUPSNdKfOi8gTtmMovY-u1tCAHjX89QSlI0bvBb42KwB5Y00So_ZkuWA1Bb8x0HOFQYSPhoypIH07jioOmX4myurPbVO9_HM0OYFw9WQjzBAlnQobfzOTYMzOXmQyiOaZa1Smz39prDZT0ZdDyZYc7GxIdLIJvz4i4bA2-DuW-F0cfwEKKt2CeE6QSFWVKXvTJtPauGPcWvCSIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d5dd1149.mp4?token=gN_HjZqpWtVtXqMMJH4qLem3O4jCqZm9w6jqWw159z4rXD9PcBkcerW8pwB0BQb8Sj7PHEpaTuddyfE56ZvnnHQRgQnjB0rUmPVtlu23rUYT2-jBzPXqE3Dg8b0pTIOWqgVFPm_TUPSNdKfOi8gTtmMovY-u1tCAHjX89QSlI0bvBb42KwB5Y00So_ZkuWA1Bb8x0HOFQYSPhoypIH07jioOmX4myurPbVO9_HM0OYFw9WQjzBAlnQobfzOTYMzOXmQyiOaZa1Smz39prDZT0ZdDyZYc7GxIdLIJvz4i4bA2-DuW-F0cfwEKKt2CeE6QSFWVKXvTJtPauGPcWvCSIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، واشنگتن دی‌سی را به مقصد ایرلند ترک کرد تا سفری دو روزه به این کشور داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146991" target="_blank">📅 09:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146990">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d237dcf54.mp4?token=c9xV9f7HCpFPHWo_mljK-cZ2CAao2fdc13V_92YrVuQaR5nYgwdhuHJp0KabAmiYMjsFhurjUl-GFJYx_p_8vLu8TEkHYZf8gtlkeKfqc5OfmGAyowM1Fd2M86cVgURU2UKkcp5qJVd97HSHGejhqyXeY2zXvQENQOamcL9mh5ebBr_138kTeo0pTMgEkfegdcvVS8OgjljMZ-tZUVNJ--vXQObBYp4Z9-Iyq76jtH5E6SBionfm1JgPqvX7XqtDAOQTXJNU1qE0hXFSL1x6HyUNBq_uopTH_KzaagIiRSTyOGZzyKcIdqAEOJAK_4QeWPxSoZCEhe-XByna4zUD-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d237dcf54.mp4?token=c9xV9f7HCpFPHWo_mljK-cZ2CAao2fdc13V_92YrVuQaR5nYgwdhuHJp0KabAmiYMjsFhurjUl-GFJYx_p_8vLu8TEkHYZf8gtlkeKfqc5OfmGAyowM1Fd2M86cVgURU2UKkcp5qJVd97HSHGejhqyXeY2zXvQENQOamcL9mh5ebBr_138kTeo0pTMgEkfegdcvVS8OgjljMZ-tZUVNJ--vXQObBYp4Z9-Iyq76jtH5E6SBionfm1JgPqvX7XqtDAOQTXJNU1qE0hXFSL1x6HyUNBq_uopTH_KzaagIiRSTyOGZzyKcIdqAEOJAK_4QeWPxSoZCEhe-XByna4zUD-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره انتخابات میان‌دوره‌ای: «اگر از نظر آماری نگاه کنید، وقتی رئیس‌جمهور هستید، چه جمهوری‌خواه باشید و چه دموکرات، به دلایلی اتفاقات عجیبی در انتخابات میان‌دوره‌ای رخ می‌دهد.
🔴
فکر می‌کنم در انتخابات میان‌دوره‌ای پیروزی بزرگی به دست خواهیم آورد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146990" target="_blank">📅 09:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146989">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130d71260b.mp4?token=jdqNco7ZkvKftiuSSHpLeOGuQckVNIGes8WY3CaI2b100RfKILAMGp_xthYfsP_amcQsXTimmxl8WwwBMJLFf-sboeP_dmbU5zH-hMc4tvsbKpp9W43oXraECSTxedHVZu_SV1f-cCUdXaGL7eiBL79EHaAOOiSDS2g9qUHOo1WoS7AalDtV2U9lk2AypgSbfFYRkzo10rVsLVBSYM38lnrQOejotU2mstnQVuwrPJ2r1Z2Vd_GEEBTAABqhSO1uUj4eV3GAHd6rSs07kwzwcSnAXA9WBkfbZXL3cjhSx3TVOrvhzj6-7T9c6r2W2T1BRmlBpQNFrF3KsUJRLK7uqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130d71260b.mp4?token=jdqNco7ZkvKftiuSSHpLeOGuQckVNIGes8WY3CaI2b100RfKILAMGp_xthYfsP_amcQsXTimmxl8WwwBMJLFf-sboeP_dmbU5zH-hMc4tvsbKpp9W43oXraECSTxedHVZu_SV1f-cCUdXaGL7eiBL79EHaAOOiSDS2g9qUHOo1WoS7AalDtV2U9lk2AypgSbfFYRkzo10rVsLVBSYM38lnrQOejotU2mstnQVuwrPJ2r1Z2Vd_GEEBTAABqhSO1uUj4eV3GAHd6rSs07kwzwcSnAXA9WBkfbZXL3cjhSx3TVOrvhzj6-7T9c6r2W2T1BRmlBpQNFrF3KsUJRLK7uqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، درباره سفرش به ایرلند: «ما دیدارهای زیادی با رهبران اروپایی و دیگر مقامات خواهیم داشت، بنابراین زمان بسیار جالبی خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146989" target="_blank">📅 09:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146988">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4e4a261f.mp4?token=eFTJSZaeTepFTCYkJpp2pP9MYt-cJurgQKP9G0IxYo4LZx9lDWGzY_zCwZYoR28i06UZrXhQtvBkdIgi-x16ORKKxVGHLX_3lgQh__YyS-myDz14r7HaZ4ikH3opBBCGHTuB6i8Z8aQVR03E3jyHSmzffK_ALB4EaR1FYVIkFWrGs6Zdi5T0PYLJGm3gQ3Wyyz4Mnw-GKLIBZuopV88PQ93Yu_dAJA3iQKk3Micl_jofp8hVEjLl3LbJuBDN3OtMsJiO1QRQKEsi_NroPpbdc4KB9BttSPcN9fRkUqVPG4yTU39VyB-PsKi96qjjgOkzCTlfO1ro2TaTcLjaFHcxYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4e4a261f.mp4?token=eFTJSZaeTepFTCYkJpp2pP9MYt-cJurgQKP9G0IxYo4LZx9lDWGzY_zCwZYoR28i06UZrXhQtvBkdIgi-x16ORKKxVGHLX_3lgQh__YyS-myDz14r7HaZ4ikH3opBBCGHTuB6i8Z8aQVR03E3jyHSmzffK_ALB4EaR1FYVIkFWrGs6Zdi5T0PYLJGm3gQ3Wyyz4Mnw-GKLIBZuopV88PQ93Yu_dAJA3iQKk3Micl_jofp8hVEjLl3LbJuBDN3OtMsJiO1QRQKEsi_NroPpbdc4KB9BttSPcN9fRkUqVPG4yTU39VyB-PsKi96qjjgOkzCTlfO1ro2TaTcLjaFHcxYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من عاشق سیاست هستم.
🔴
به دوستانم که در حوزه املاک یا ساخت‌وساز فعالیت می‌کنند می‌گویم؛ چون واقعاً در ساخت‌وساز و ساختن چیزها خیلی خوب بودم: «آیا در سیاست بهترم یا در ساخت‌وساز؟»»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146988" target="_blank">📅 09:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146987">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2200cb9823.mp4?token=azb1dl6_COntx2Nl0n1X7TCMmo36zZKv4dUzVwGC1pivt4s1PIE71g6DTwTVsyEIp-wvjo4U0ADSEXZArSYNbj-3dH2f7k2xvWbdLk0MhRyeh1eYQFbx-lO1WIFStAdjeiVSbJCh84BItvmlCCWPqawcFBi_pMGouexD945ULLp8mmIxqbHTjNRWGUeqOjNlYMEmGGT35mTKZGJAqU0QGWk0-WyhDseIer03B4Ik2WtObv5i9NtzuQrNRt5yb2bCw8-fBTwx1NR0inGsSbV5UOopHWnRNZ_zmMuIuNQalOUe5zQezNf6uP4chwoFa8PRXIVzHJL5LMdW2fCXGchoiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2200cb9823.mp4?token=azb1dl6_COntx2Nl0n1X7TCMmo36zZKv4dUzVwGC1pivt4s1PIE71g6DTwTVsyEIp-wvjo4U0ADSEXZArSYNbj-3dH2f7k2xvWbdLk0MhRyeh1eYQFbx-lO1WIFStAdjeiVSbJCh84BItvmlCCWPqawcFBi_pMGouexD945ULLp8mmIxqbHTjNRWGUeqOjNlYMEmGGT35mTKZGJAqU0QGWk0-WyhDseIer03B4Ik2WtObv5i9NtzuQrNRt5yb2bCw8-fBTwx1NR0inGsSbV5UOopHWnRNZ_zmMuIuNQalOUe5zQezNf6uP4chwoFa8PRXIVzHJL5LMdW2fCXGchoiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره هوش مصنوعی: «ما گاردریل‌ها و چارچوب‌های حفاظتی می‌خواهیم؛ می‌دانید، این موضوع خط بسیار باریکی دارد. چین گاردریل ندارد. گاردریل آنها رئیس‌جمهور شی جین‌پینگ است
🔴
آنها تقریباً در هیچ زمینه‌ای هیچ محدودیتی ندارند. در چین می‌توانید هر کاری انجام دهید
🔴
ما در زمینه هوش مصنوعی در حال پیروز شدن مقابل چین هستیم
🔴
و می‌دانید، یک عبارت معروف وجود دارد: هرکس هوش مصنوعی را برنده شود، پیروز است. اهمیت آن در همین حد است. از اینترنت هم بزرگ‌تر است. حتی ممکن است بزرگ‌ترین تحول تاریخ باشد و در بیشتر موارد، برای خیر و منفعت است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146987" target="_blank">📅 09:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146986">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff392cb863.mp4?token=RW2hnaj2osONs0x2-YEun1-OUa1_AgJJXzFiePyudEPe564YHeDOImuU6oto1KEMCC-NEJyk_n8lO_K4N6URsyTsGlfhU31Chpimft4q3a9L96NJgPTRdDEfDEp6Ri0ijSuFubIF8O6uRwUJIjmI7Jj_41J99EV645AUWsJMUThRAgeFIX_yoIQGB_l3ZYAvxp-X4aRHGEKfmPGKxEPXiUv2n4Rq9hLmnrf1fZPQ9e8NJtDsZFiLkTC_Tz3j9OzuCO7n_KKWGZgL9mVCOoU12neIcbSx-9ZtlNpV2HgaI6gOisxsdMBbMhSpZtkZ6_n1x9h0WCWzOYqR_m3CP4phgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff392cb863.mp4?token=RW2hnaj2osONs0x2-YEun1-OUa1_AgJJXzFiePyudEPe564YHeDOImuU6oto1KEMCC-NEJyk_n8lO_K4N6URsyTsGlfhU31Chpimft4q3a9L96NJgPTRdDEfDEp6Ri0ijSuFubIF8O6uRwUJIjmI7Jj_41J99EV645AUWsJMUThRAgeFIX_yoIQGB_l3ZYAvxp-X4aRHGEKfmPGKxEPXiUv2n4Rq9hLmnrf1fZPQ9e8NJtDsZFiLkTC_Tz3j9OzuCO7n_KKWGZgL9mVCOoU12neIcbSx-9ZtlNpV2HgaI6gOisxsdMBbMhSpZtkZ6_n1x9h0WCWzOYqR_m3CP4phgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره آنتروپیک: «بیایید درباره آنتروپیک صحبت کنیم.
🔴
آنها کاری انجام دادند که بسیار بد بود و ما آنها را متوقف کردیم. خیلی سریع متوقفشان کردیم.
🔴
ما گاردریل‌هایی داریم. بزرگ‌ترین گاردریل این است که افرادی را داشته باشیم که به همان اندازه باهوش باشند؛ چون هیچ‌کس این موضوع را درک نمی‌کند، مگر اینکه ضریب هوشی بسیار بالایی داشته باشد — نه جو بایدن.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146986" target="_blank">📅 09:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146985">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf0c3dd2b.mp4?token=mhmm4Ax5GWYUyTYeCu9raqs0RFkmPUjNOnraR0Vb9UUJ0luu3EZoL2XMxoNoSh67vXYVejzwxVWKMf1bv4kCWlLIK_Y6JZqhUEboajb60aXUJa_-WDn7360AyVXZCixGGC8ouxrozQbmO0joo2NtdGv7KqJfe1vX-d1rSuYGm3PzWBRCIrdfSksG3kKcbfEuxjzkfejJikmthZOTmAgH_68p1lYS9p72ltQWB7PUkijeJ4-c-2AuZFH5G53m0a_Yl0ayn0FtslzhJowl2pixdaa6lSp_WVvRjty-iT11ismdr8dgpj1g_vIutoPPNJ52xguaLEN2_DEXl1UK0rak9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf0c3dd2b.mp4?token=mhmm4Ax5GWYUyTYeCu9raqs0RFkmPUjNOnraR0Vb9UUJ0luu3EZoL2XMxoNoSh67vXYVejzwxVWKMf1bv4kCWlLIK_Y6JZqhUEboajb60aXUJa_-WDn7360AyVXZCixGGC8ouxrozQbmO0joo2NtdGv7KqJfe1vX-d1rSuYGm3PzWBRCIrdfSksG3kKcbfEuxjzkfejJikmthZOTmAgH_68p1lYS9p72ltQWB7PUkijeJ4-c-2AuZFH5G53m0a_Yl0ayn0FtslzhJowl2pixdaa6lSp_WVvRjty-iT11ismdr8dgpj1g_vIutoPPNJ52xguaLEN2_DEXl1UK0rak9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «راستی،
جنگ ایران پس از انتخابات میان‌دوره‌ای
پایان خواهد یافت.»
🔴
اینگراهام
از
فاکس
:
«اگر جمهوری‌خواهان پیروز شوند. اگر جمهوری‌خواهان شکست بخورند، چرا جنگ ایران باید پایان یابد؟»
🔴
ترامپ
:
«خیلی‌ها فکر می‌کنند اگر شکست بخوریم، من عصبانی‌تر می‌شوم و کار را یکسره می‌کنم؛ می‌دانید؟ می‌دانید، این هم یک راه دیگر برای انجام این کار است. در هر صورت، آنها شکست می‌خورند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146985" target="_blank">📅 09:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146984">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/689440a6bc.mp4?token=DBEQaE7D17gdI0EP3_G5e37eW_-r3Ejti9XSzivoIQR85Gpstm0nptBoQOynM4KqW1PMOWpTpZjIuAOQQYnlRY4sFCuMczQMAfq1jTI_hXjFFhWfd630LSmG-oLvwcovnmcJt6_dd4u8CGW-u0fr9J_kYYu55cWmeMmq4I27jf4xjFX5IGrx5L7DyKsGLlDmyqRiF4oBisXEibbXmg2Nxd07WqbXjL8pFIYgqxYe-FAlppajYG4h5iRU2g5sAtVkdw3d_lbo_DesVYNsXG-VrDpbr5BvMgUDCJx1H4WX-qiHSlSI7BSHUvcUtP-ai0Ne-y-NJT9Ad3XODVLoeTAKtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/689440a6bc.mp4?token=DBEQaE7D17gdI0EP3_G5e37eW_-r3Ejti9XSzivoIQR85Gpstm0nptBoQOynM4KqW1PMOWpTpZjIuAOQQYnlRY4sFCuMczQMAfq1jTI_hXjFFhWfd630LSmG-oLvwcovnmcJt6_dd4u8CGW-u0fr9J_kYYu55cWmeMmq4I27jf4xjFX5IGrx5L7DyKsGLlDmyqRiF4oBisXEibbXmg2Nxd07WqbXjL8pFIYgqxYe-FAlppajYG4h5iRU2g5sAtVkdw3d_lbo_DesVYNsXG-VrDpbr5BvMgUDCJx1H4WX-qiHSlSI7BSHUvcUtP-ai0Ne-y-NJT9Ad3XODVLoeTAKtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اینگراهام از شبکه فاکس: «فکر می‌کنید وقتی تاریخ‌نگاران درباره این دوره بنویسند، چه خواهند گفت؟»
🔴
ترامپ
:
«وقتی کتاب‌ها نوشته شوند، فکر می‌کنم خواهند گفت که
من این کشور را نجات دادم.
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146984" target="_blank">📅 09:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146983">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1096f3ff.mp4?token=NyywWUhrtqWWrnaD54a1pXXpDqaVXkD64jANQvGzR-uR1z5UIAqFHMgYdpk53Itz0GmJgw4UJ-d7M00lFHFfn04bRBfzt9-hSMftDunDtADVtSTNAMeDTnWegDKgJaDxqbhi4JzcCR_br6yGTplJxIZqM-5PPWBTdgxohknZ0pSMxn-B8i685ICvQhqqXBD9d2ql4BRSr6-SWfjR-2BL2bKWt5UBdqAt4cltXo_KMreSmQZSqRpZ9FPlyY_3iidnez5l3WiLLXyktOZB2ZMmjeQauDxT_6BWphmvxUyE41RlCk4DuculxgHOUXRXqhrAdanyOOX0_G1B7x4_LN-zKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1096f3ff.mp4?token=NyywWUhrtqWWrnaD54a1pXXpDqaVXkD64jANQvGzR-uR1z5UIAqFHMgYdpk53Itz0GmJgw4UJ-d7M00lFHFfn04bRBfzt9-hSMftDunDtADVtSTNAMeDTnWegDKgJaDxqbhi4JzcCR_br6yGTplJxIZqM-5PPWBTdgxohknZ0pSMxn-B8i685ICvQhqqXBD9d2ql4BRSr6-SWfjR-2BL2bKWt5UBdqAt4cltXo_KMreSmQZSqRpZ9FPlyY_3iidnez5l3WiLLXyktOZB2ZMmjeQauDxT_6BWphmvxUyE41RlCk4DuculxgHOUXRXqhrAdanyOOX0_G1B7x4_LN-zKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره آنتروپیک
:
«آنها مجبور شدند مهار شوند و حالا ناگهان، همان‌طور که می‌گویند، کاسه‌کوزه‌ای از خوبی و درستکاری شده‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146983" target="_blank">📅 09:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146982">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f1804432.mp4?token=uSV_jNolX_oK9zJgcsDPqVVaaOUfMtNC9QA8sDIgPxfY_xGNawaf1SoECE8QKxHAhEHO9NifBmBwRCkkXAXWfsaXyWEb4Pmo52nsFomVRDjTLAYk3m15hbNOymY9fJZj8PrIMTw4leJXyB7iGxXh5ZHRAXpNvYwr0igPMysqizcWmkM61-HXQryP4igy45nFJ8L_rAS9LrplYgEfP-CFoj9jpKNpMpzyche-2Emo1SvenWgzvqEkD7Zy1-GrcdhXxVFdfFZLzlCRlmnPtl15WhkVLN3845E_a0qoHUjzMt2PWESd28qZh2a-ktkiie731lYAujLSmnG8QAX5HB71_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f1804432.mp4?token=uSV_jNolX_oK9zJgcsDPqVVaaOUfMtNC9QA8sDIgPxfY_xGNawaf1SoECE8QKxHAhEHO9NifBmBwRCkkXAXWfsaXyWEb4Pmo52nsFomVRDjTLAYk3m15hbNOymY9fJZj8PrIMTw4leJXyB7iGxXh5ZHRAXpNvYwr0igPMysqizcWmkM61-HXQryP4igy45nFJ8L_rAS9LrplYgEfP-CFoj9jpKNpMpzyche-2Emo1SvenWgzvqEkD7Zy1-GrcdhXxVFdfFZLzlCRlmnPtl15WhkVLN3845E_a0qoHUjzMt2PWESd28qZh2a-ktkiie731lYAujLSmnG8QAX5HB71_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره چین: «اگر چین بخواهد اینجا بیاید و کارخانه‌ای برای
تولید خودرو
راه‌اندازی کند، من با آن مشکلی ندارم.
🔴
نکته مهم این است که آنها کارگران آمریکایی را استخدام کنند و از نیروی کار ما استفاده کنند.
🔴
چیزی که نمی‌خواهم این است که آنها در مکزیک خودرو تولید کنند، آن را ارزان بسازند و بعد، می‌دانید، از طریق مرز به آمریکا ارسال کنند.
این دیگر اتفاق نخواهد افتاد.
🔴
درست مثل اینکه خلیج مکزیک دیگر خلیج مکزیک نیست؛ حالا خلیج آمریکا است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146982" target="_blank">📅 09:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146981">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd817edf8.mp4?token=iMwp4DeyigAjcP__3qgpd38f1ElgZZeXpYdnUtLnSB01WIEIAZZp7DJZTUFQr3mnh-49M0mnOBdAHPUX5RoZMgZwqUpmgdFziHh-q7z-foa9ygUO2yGosU-5Lz7woBAy6MZuCOlDMz2KO3r_xF5FAbeLka703vUCMVpipBEM4uJxI_pPdrf0fWs6wBZn98v9ySjnSapNQ0oyVS4xdsgMaXyN1EWcoxa45hSvCAp9LBlcl4t-_Kv1m33-GItJL6GlEv0uvgPg7PXJ9_hlaE9P2yCoF32SaRtUeaDXPRZ3ITNL9OkGYIZBmFFSFEJwFSWPaFYvSWdJLn1ruhB8wYWjMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd817edf8.mp4?token=iMwp4DeyigAjcP__3qgpd38f1ElgZZeXpYdnUtLnSB01WIEIAZZp7DJZTUFQr3mnh-49M0mnOBdAHPUX5RoZMgZwqUpmgdFziHh-q7z-foa9ygUO2yGosU-5Lz7woBAy6MZuCOlDMz2KO3r_xF5FAbeLka703vUCMVpipBEM4uJxI_pPdrf0fWs6wBZn98v9ySjnSapNQ0oyVS4xdsgMaXyN1EWcoxa45hSvCAp9LBlcl4t-_Kv1m33-GItJL6GlEv0uvgPg7PXJ9_hlaE9P2yCoF32SaRtUeaDXPRZ3ITNL9OkGYIZBmFFSFEJwFSWPaFYvSWdJLn1ruhB8wYWjMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا:
«رئیس‌جمهور شی جین‌پینگ قرار است
دو هفته دیگر
برای یک شام رسمی خوب به اینجا بیاید.
🔴
ما با هم کنار می‌آییم. می‌دانید، من و او رابطه بسیار خوبی با هم داریم.
🔴
مردم می‌گویند: «اوه، او از ما جاسوسی می‌کند.» خب،
ما هم از او جاسوسی می‌کنیم.
می‌دانید، ما هم در این کار خیلی خوب هستیم.
🔴
ما اکنون روابط بسیار خوبی با چین
داریم.
قبلاً روابط بسیار بدی با چین داشتیم، اما حالا با چین خوب پیش می‌رویم.»
✅
@AloNewd</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146981" target="_blank">📅 09:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146980">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd52e61643.mp4?token=g2GYlT_Wpiq7vhWD-4JTrYmzb_7FER6Twq4yX0pysRfjUnIxnLtL1C3R3vky0WsVA-ZGA369ZUAINTXTKmzLl0TYvavxkwJ5YxRmIRRWa9GPJsQbKkVT7pXV5ljcITdOT5zO-XGh4VUvWZDggBjjWG9OxhvzbntWMJfmWV-7JCCNv1Nn9fb4RPCKEOZMZv_QPR_I3Jr5ZaCOtdYVPc9AH9C-Ghjuwh89gFgvK8j9nHyt9ChIDuiMl8ryU4jLggG1TrEJSggtx5d2mLaEXbJQh_gXfJE2iB0XV9fCZl1e3HuGUGq9WfwjKlsLUpicx5pEEU6T8wC_goS_5ZaeQzWMwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd52e61643.mp4?token=g2GYlT_Wpiq7vhWD-4JTrYmzb_7FER6Twq4yX0pysRfjUnIxnLtL1C3R3vky0WsVA-ZGA369ZUAINTXTKmzLl0TYvavxkwJ5YxRmIRRWa9GPJsQbKkVT7pXV5ljcITdOT5zO-XGh4VUvWZDggBjjWG9OxhvzbntWMJfmWV-7JCCNv1Nn9fb4RPCKEOZMZv_QPR_I3Jr5ZaCOtdYVPc9AH9C-Ghjuwh89gFgvK8j9nHyt9ChIDuiMl8ryU4jLggG1TrEJSggtx5d2mLaEXbJQh_gXfJE2iB0XV9fCZl1e3HuGUGq9WfwjKlsLUpicx5pEEU6T8wC_goS_5ZaeQzWMwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:به هر حال، جنگ با ایران بعد از انتخابات میان‌دوره‌ای به پایان خواهد رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/146980" target="_blank">📅 09:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146979">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
مسعود پزشکیان در گفتگو با یک رسانه هندی خبر داد که روز دوشنبه توافق عمان و ایران درباره مسیر مشترک تنگه هرمز در حضور وزرای کشورهای عربی حاشیه خلیج‌فارس امضا و به سازمان دریانوردی بین‌المللی اعلام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146979" target="_blank">📅 09:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146978">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات آمریکایی: چین پیش از حمله ایران به پایگاه موفق‌السلطی اردن که منجر به کشته شدن ۳ نظامی آمریکایی شد، تصاویر ماهواره‌ای با وضوح بالا را در اختیار تهران قرار داده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146978" target="_blank">📅 09:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146977">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c24f8e1f79.mp4?token=J8vt4pHjHwfgcQ8Z3hoL-WiYYk_-uDqmhW9lfGyvsHKgMEYAIieHuE78OaYSgrxXJ2loCIhBJP34S8tp2uSanbAV2y1MW0oNvL68tcqGdvcY58TSouMkIAlm36T94uzL2iX118Bis6dds1OiIBmynMB5t9EfShLhzXYn4WFRHX_kowq30Hzhi32jY7gF6ECe1FZpP6q72eKTwg_OdeRKSQ9B7u2fT2SkGCe_X7HR4dtc8D3EEzyW2y7qm93dAMYPpgxtyaLbbNS0D5YCY2GQVpwH4obuSKjjROdJMhExm0-Gh7mkWe7sdnUTMThXB3DOkpCRFRzRrGVJbI1P-PGyuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c24f8e1f79.mp4?token=J8vt4pHjHwfgcQ8Z3hoL-WiYYk_-uDqmhW9lfGyvsHKgMEYAIieHuE78OaYSgrxXJ2loCIhBJP34S8tp2uSanbAV2y1MW0oNvL68tcqGdvcY58TSouMkIAlm36T94uzL2iX118Bis6dds1OiIBmynMB5t9EfShLhzXYn4WFRHX_kowq30Hzhi32jY7gF6ECe1FZpP6q72eKTwg_OdeRKSQ9B7u2fT2SkGCe_X7HR4dtc8D3EEzyW2y7qm93dAMYPpgxtyaLbbNS0D5YCY2GQVpwH4obuSKjjROdJMhExm0-Gh7mkWe7sdnUTMThXB3DOkpCRFRzRrGVJbI1P-PGyuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات پهپادی روسیه به نیروها و تجهیزات اوکراینی
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146977" target="_blank">📅 09:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146976">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
بدر عبدالعاطی، وزیر خارجه مصر، بر تلاش برای آرام‌سازی اوضاع در باب‌المندب و تضمین آزادی دریانوردی تأکید کرد.
🔴
وی ادامه داد اختلال در ناوبری منطقه باب‌المندب، منجر به خسارت ۱۱ میلیارد دلاری به کانال سوئز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/146976" target="_blank">📅 08:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146975">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
پزشکیان: تنگه هرمز به شرط اینکه آمریکا دست از محاصره و حمله بردارد، باز خواهد شد
🔴
روز دوشنبه در مسقط در حضور کشورهایی که از خاک آن‌ها به ما حمله شد، توافق عمان و ایران بر سر «مسیر مشترک در تنگه هرمز»، امضا می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/146975" target="_blank">📅 08:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146974">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac66aef0a.mp4?token=PV3c7p1TKPatKMYRVvbSI8Xw9yR5hYHQ4HPNcrRZ0qv-O1Rnk3u9KCsj_X94kZn-cXZSf5O5CalR6rK7I-p82Gbn4-uWedHOEKB03K2oJSwLjFZTqmFoCXXTrxrNx5eILEVAkJKrOclriuglMYxlPHzlUKRqSfm7CylWLj-V0cJ1QDDxeYilcRcembILSX9r5DD54j63s5IPE60bfNmTtxsRysGfUDDLb-wMqMBgYfnjXQnMpM58WvcTbBIWoBfWsxk5StsmIgmEf6NAUupLuDWG-JJbKCDce0t6cwcDRgFLAq-WoE7NbSJtUDW4NyzRO4mlzrrfgSQXZKGjTnLZBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac66aef0a.mp4?token=PV3c7p1TKPatKMYRVvbSI8Xw9yR5hYHQ4HPNcrRZ0qv-O1Rnk3u9KCsj_X94kZn-cXZSf5O5CalR6rK7I-p82Gbn4-uWedHOEKB03K2oJSwLjFZTqmFoCXXTrxrNx5eILEVAkJKrOclriuglMYxlPHzlUKRqSfm7CylWLj-V0cJ1QDDxeYilcRcembILSX9r5DD54j63s5IPE60bfNmTtxsRysGfUDDLb-wMqMBgYfnjXQnMpM58WvcTbBIWoBfWsxk5StsmIgmEf6NAUupLuDWG-JJbKCDce0t6cwcDRgFLAq-WoE7NbSJtUDW4NyzRO4mlzrrfgSQXZKGjTnLZBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: خیلی‌ها فکر می‌کنند اگر در انتخابات ببازیم من عصبانی‌تر می‌شوم و کار را یکسره می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/146974" target="_blank">📅 08:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146972">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nkMQWlG-c8W44UQlohDihOTaZ7FylC8yYXNaXrB1z-fjc7jwWXx87AOSB5lHnsl5D4YD0G0v9P7iEHlOV8kO7HioCWXxkXCFnXsyiczUe_b80iZvyeX1XR43QVT8Pp9yaAlx7AI54MUxU1nU8jVYbylCHA6DobC-oeoYMsjVb4E7TqTqM2LHYytUggpRoHZpRlnJRqNZVkN1vJVZaEA9BJKWRVDI3hDoAwTpKRWYj5aonkD1sbvbA6M52Rs8WGC7cxQd7t8AnUk_S5HuJxrJq8o7c7q6M2E2MWh9PUxDXYLzU8syFg86BQLvla4Nqfm5rYgcw35n9b_fFuKCA2ddhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q51B6lFpbXSW59Y1ghU3ZjBgehXU6tK1yhOb0F9qAt_P1oXNyuWdLTmxWFPYQGXUZLsK-1ps9fCAeL167KGkbWedczMBmVjDAibAFOWr4tZsKetBxTm3WeECCSoWj7565QYAQ_iPTmWh7KI80RFK_imabI2qbjgsfr9iHlzFz1MFDS10VG3S3wkjRZxhPfG9dNjvS9o1tTxuvO2cDdS8LthQ6RPQ6hxZsgBRhPFNs1beJ5BfsHBwvJuwNJkFPZvsWCg0T2znN5BgpBpCKugRQomOyZ4swoLLFCtHVqcSuo06INYQMlpESV0tBGXrobOxiOKMLgd5ly90DmMfTV-eKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از یک مقام آمریکایی:
🔴
حمله ایران که در ماه ژوئیه منجر به کشته شدن 3 سرباز آمریکایی شد، ایران از تصاویر ماهواره‌ای چینی با وضوح بالا استفاده کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/146972" target="_blank">📅 05:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146971">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b31d12ff0.mp4?token=I0XaUOqrXVCI31Zzr3vuP9U4u8Vqqmy__RE4t0XMcDeQzoOmjNaSQSaOo2medCpHRHyOk4QEzOBM3yqT6vvY-JytrnGaDLDftU6QVk9p1p-tRp1Y-9kXZAzbJf53h3LgGFnrO3LawptdBIC9tM9d1UX_lEt_dKSbbMwNUos1RXUWOzHngz6HuUqRzVjhjU32T-RL_TStZuJae3znp_ivArO3A-1H5moqOtUZfCmSlgRoULKHJdA2kPbzVqjf7k4AXw4rXQFG20Y9ipTv12US4A3ZxhsSpM6ObWSMGNGMdYB3PKf7cE4A-vPl-qWuyVIyALfXzKfGS051Dh_6o1Ht0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b31d12ff0.mp4?token=I0XaUOqrXVCI31Zzr3vuP9U4u8Vqqmy__RE4t0XMcDeQzoOmjNaSQSaOo2medCpHRHyOk4QEzOBM3yqT6vvY-JytrnGaDLDftU6QVk9p1p-tRp1Y-9kXZAzbJf53h3LgGFnrO3LawptdBIC9tM9d1UX_lEt_dKSbbMwNUos1RXUWOzHngz6HuUqRzVjhjU32T-RL_TStZuJae3znp_ivArO3A-1H5moqOtUZfCmSlgRoULKHJdA2kPbzVqjf7k4AXw4rXQFG20Y9ipTv12US4A3ZxhsSpM6ObWSMGNGMdYB3PKf7cE4A-vPl-qWuyVIyALfXzKfGS051Dh_6o1Ht0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراق مرز با ایران رو بسته و هیچ ترددی رو اجازه نمیده انجام بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/146971" target="_blank">📅 03:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146970">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
مرز شلمچه به دستور نخست وزیر عراق رسماً به روی ایران بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/146970" target="_blank">📅 03:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146969">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
مرز شلمچه به دستور نخست وزیر عراق رسماً به روی ایران بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/146969" target="_blank">📅 03:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146968">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
برآورد شده در دو دهه برای تاسیسات تپه علی طاهر بالای 2 میلیارد دلار هزینه شده است که خب مشخصه از کجا تامین شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/146968" target="_blank">📅 01:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146967">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f254d9cb95.mp4?token=EUiigC9yL4Ff6QK6_4K-LtzMhHcPYjQGYWixKiv3OEfzEwyw5fbXKkC5ouctwI70j6auCitPPD9cdVQ4VJOl22FKBrKHJq0Gx61EOMg5Tr2O2OgEi7zMFXnznsd6hSx0e3ctzrzvmdeDPDR7amDqC6eUsc1ab7GPoGZiVtJhUwppzAkT0TL_Fz01hE-EyYqGEVXJ_eVCF2MVXrYqeTFvN4W1iva8p1lbqU42_ev-QcZHbQGb73xpJveDZD7ETwttxs1iEUsFo3RI0Ftfuvuj5MOjZ7zFaP0hXZNFMN0xX1ziNKLLkZbSCdKHGDACH1vHEhlDpeYtwtjdgnANgG1nAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f254d9cb95.mp4?token=EUiigC9yL4Ff6QK6_4K-LtzMhHcPYjQGYWixKiv3OEfzEwyw5fbXKkC5ouctwI70j6auCitPPD9cdVQ4VJOl22FKBrKHJq0Gx61EOMg5Tr2O2OgEi7zMFXnznsd6hSx0e3ctzrzvmdeDPDR7amDqC6eUsc1ab7GPoGZiVtJhUwppzAkT0TL_Fz01hE-EyYqGEVXJ_eVCF2MVXrYqeTFvN4W1iva8p1lbqU42_ev-QcZHbQGb73xpJveDZD7ETwttxs1iEUsFo3RI0Ftfuvuj5MOjZ7zFaP0hXZNFMN0xX1ziNKLLkZbSCdKHGDACH1vHEhlDpeYtwtjdgnANgG1nAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری‌ها در مأرب، در استان تعز، همچنان ادامه دارد
و گزارش‌ها حاکی از آن است که
نیروهای شورای رهبری ریاستی (PLC) از شهر عقب‌نشینی کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/alonews/146967" target="_blank">📅 01:11 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
