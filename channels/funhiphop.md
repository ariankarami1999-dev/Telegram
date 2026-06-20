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
<img src="https://cdn4.telesco.pe/file/uuBqIuCxj1taWsOKRqAlOXySBDTZSHa5asfVSOb1MZvYJmFIIF6TMIcQ3VhTCT7K820JdqFDX357GBPj-LFoMJVUzJWADmpelEiQiQsXYqzc_gMDghfD2W5hLrHWJeW7LRLm1mFyASELXafxfL_QazeWxyZTqGUo6FXlFJNd4edd2AVJBS8F9gLzhIYfhyrzLaK1R8v9GtNmaXKK6axZsk21uzr9JSg2yXjijhApTgdJOMpeUscxw_oMI41N9YsYJ8GE1ePQ89x1VUqusD-IiDiv9aOW25AfF4iAyYTnq0oxWMUo1ILyk9XulKzObgXnjerJmYzDSjBf2P60QnrYmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 169K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 15:53:56</div>
<hr>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دولت عراق مجوز استفاده از استارلینک و صادر کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/funhiphop/78278" target="_blank">📅 15:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rhe04G0qF0TAV3GymFjeMjTkKkSOgTDhY_THmQWPPh-x_DL3KrX5Lyvv5_hTIIJXOV0wikAAcFBF3rLu-IJwiWi_8l2HHCsX3WVgNUNbJYNHejtZHPEcrwU9bxiz4aQgr9CfH-iWK0v62LuEOzMnghxTEnUdVVb2HVJmj7Cf4D6aCczGqVQ7_JPVfgxA-jNzZxRN660YaIadnp2c4E3lEIUTi0rGD0wUREQtGR9QqNTlmfvczpEBsRGg6WLj_GE1j3JkDAJE79BLQXh76yymU_umRuNPRmvSrg9km0lSIVO7Kr1F7KneIE1zVGbEuCWS8_LjuwL5fsT_iVuCwFBFnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدینیو و طرفدار گمنامش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/funhiphop/78277" target="_blank">📅 14:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78276">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv9niYtcIAT0CelmNIgBEtmUoVp3zMSGCJfyqa0GITBLe7vxnJw3VUCLKpOnKP4rAMazQptCVrB2NrTniD5hECfZYsNKawPEMeN8AuGOntdy-wK81D5_UqJicOgm87qWtkeDYzrTO235SAfDSN34mze_ehMJwgoymkEr2WoYX-wXRJ2WNzqJZ5WHSukVQc-s7YX5gez0TmHaQOi6nFi-miaBM7nMY3rwWdAUW98yHPwCXynsDMAa-uI37OH8WFBl_BMZiBWxVqgDxO9lb4rzybbxdIIza-eurt1Iy7ytYYuMuHfEmm1Fu-TspEmiDUPfkM4buVSOS2b2pv8k7RZKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باهوشا جواب بدید
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/funhiphop/78276" target="_blank">📅 14:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تو جنوب لبنان داره نسل کشی و زمین سوخته سازی انجام میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/funhiphop/78275" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIVOT-iQ9vo3vqbAO0Gw2DHHnS6FzcmmdbMLJdOtbJrObZHMmTMXxa3SYk7iL3opw3EjUHVf-JhRh7aebY9wz5FbQAOfntGv3zOmalKoJAcl1Y6tlmTizte0KnRx9s-RQN_5ohPC3NyFhj-WOC13yuo6_mSQ4WAW9j3pOis598suLSUktxq_FZBh278H0df6XrsRQ04zoPK8HZ-5bQ8FsAZ2vvPaC9GscUegFFA4QCZmyWsHTYpUen9AE62N7UuwEgzlIBq-4CDaOevaFQrdvNGNj-13BJKYnAy6-2mfsEj2UeV9U71ZBYtLnFJEyg4x9LnZb3JpO_skkvTJ3YuXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخواید اعتراض هم بکنید لااقل یه متنی بنویسید که با عقل جور در بیاد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/funhiphop/78274" target="_blank">📅 12:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78273">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4X4rVzSepZ2dBxExb05esSqrKW333rk0dwBMOdQKv5rUw3fR-BgiXQNWxliwiSG_JD67hCZYDxwI7J1Gfj1xnjurT4ZDODs5Td_3iuvawCfGz0WUIrwrBKUnxE_9OHekuMdlZ_CpKyIVIjE2__a3HpbdDTaUN24fO6ZfEsrAM0NHv5Y7n6H0-NGKIR4vDnClr0aBccWqpStaNDFwIRYkD9UpU6p1v92kj4ZmJldPt7Q6qRsf8Z-pE1VUjbuAi8r0pPI93XrNlysiHKTMyH3fVHfoJX9gbMAEdNT-YQjt5uuYZlS8sycGfjQl4RARuhayG39VV7AmTteuGDleuXVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تیک‌تاکی ها هم کم کم دارن آدم میشن
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/funhiphop/78273" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78272">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/funhiphop/78272" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78271">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWr8lWHltcBk-Sdi_0ZKqoM9jyOSY6C7zQLmmQV3fYCPe80p4q7ChKQylFY_u1UWctjFsEx3KyFni4RY2xELslYIK-5HUJUFzvv6fEgailUynemUbSvCy1Q7jmKwK-eSkLprRpgQ7PZomrPQngHgWSU5ggf9kfcYUhg0Y0m4RTqHPKKuciJlsKZUSB0XhjzxAPMMpBH4P5FKsYbbymVszkQGYZ3QsN85EdK5NBii0hZKZIY5t0uvNUKlAVpzrI96FUlyszrk8cTnStkomcBaKEuuHywSEFkH-WfLqsCfQoPPfrOkJKE6jR7qFoQ71qCfCFyL9BvqNjp8twnV5MoYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
R30
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/funhiphop/78271" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78269">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نمیدونم چرا بازیکنا برزیل نزدیک ۳۰ که میشن با هر بدنی تبدیل به شیشه میشن، من دوسال پیش اون بدن رافینیا رو میدیدم میگفتم این اصلا مصدوم نمیشه، حالا ماهی یبار مصدومه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/funhiphop/78269" target="_blank">📅 11:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الان وضعیت جوری شده فنای مسی دارن از پرتغال تعریف میکنن فنای رونالدو از آرژانتین
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78268" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78267" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گل دوم برای آمریکا
پوچتینو تیم خوبی ساخته
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78266" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ دوباره مصاحبه کسشر کرده که به خاطر اعصاب ممبر های عزیز ترجیح میدم پوشش ندم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78265" target="_blank">📅 23:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کشور جنایتکار آمریکا گل اول رو زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78264" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بازی استرالیا و رقیبش هم داره شروع میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78263" target="_blank">📅 22:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78262">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw0wUlfXKOk7jMHp3peWLhZP1Qh1JJ4LrUfiPmNymeEEwvh8Oc4nmV3ggGiMrWxCpqINKErWhuFLbocRyePSbwpNMlOea8iWdDONWwp2H4N2xSAkudHNvnRXZAkpc4bycRIgXbYCYcuhw5SLUsaVp-C5aWkEldDDtYTXZSTrtR0mdY9iRcaRAa736q0kUgKZ9LHzRGb_Yug5rAzFnxpvzKiHacj-d7XcN6NsXsVILnC1_0loX0rqV87xpy87FzUwaQIFLls-Cpmp9-49JBE9g-YEQdOTjMBciwDyq1tgZXW7Dklp1oRxwekLJRECf82WSlpM85mVkNwDvYFpJbntnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین رونالدوی موجود در جام جهانی 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78262" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oidmaOkvlye9kLxiXFnPOIPekaEaDj8pOAbiUZdJoPocVJdd40rLzSJ4FaNvSpDwQ5yJfv0Zys2exD_U0LgIzNcx4McfCulnV1auVIkBNaki8XuH8K8eJp9BPMkoOae1_EDz3O7vW8onLyyN0ZykMEwqAxNVJ6YCZeJGO-FHGbZNSx3Ntbs0fodtM4ceUsI71kfMJ6UChoKiabWJ3uFWsfOvFdbuBdSGeS46Ktp3lnmpExqodw_4oyyYJaURA0xIe8qe2vS5Tk1pZNtRQCcfz5ifva5hiHhcC92nC-qVgxKaq0wTeLEsddb9tQaAf5qNUM7_QLfEULTJ5cBgCIOcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید کون میداد تا بهش 10 بدید؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78261" target="_blank">📅 20:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فنای رونالدو به پیج کل بازیکنا تیم ملی پرتغال حمله کردن دارن فحش میدن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78260" target="_blank">📅 20:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Offc9nsst3g5qbCEokUWAW0ETT0YgruT3k2eYp8oxpSik3p2k_rpxz4hAEOXD_3ooysol2GEX-m181QxWx0aKGv3Xdd26N8ZrU7tZ5la-iNt-WUj-awZ4tXTJzi056OI3GBlHtDMDLhhBbRtqKw5J0gWlRt7j0JdTBpXkHsh1JWgQTnI52ymFJAWDacf0RU8eshNDH0h__0k_plrQNDKDBSr-5N6_vhY6FowMXEi5y8Z--NrwZf8pikl8T7vPjMYioOQCF751c2NXFPTWHP8I7PqNhsoiPT_hLSxb0lbqM_VqLG-8-Y7qnD6YcYnJIrSFXyWt2N6KvgMoI7cCG9vuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید شایع به نام بلاتکلیفی منتشر شد.
Download
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78259" target="_blank">📅 19:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شایع ترک داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78258" target="_blank">📅 19:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTQARp8KE_y7dbdJkNq01OQqMly6NYsXgyI7WG4OBhJYODqn18n7P3Kn_neLskwJmKz0DcU5X0Xn7Ly3R3sOuVjVpTbwZ5QFc9aSUXMRqgT77EYPnZa8d-_CBYyNpqwNatmvkmsCBer11DnErKPw-yDkifXbSVXOxt-umVauICW-MFH-2ZyyhVae6uEVfWOxcs0QNkS4NK5kaFJgcOUcg9K4Kw2YOKczwaYyOyenHC4YhBCuDKzKXfqL-whF9xaka3Nvoyp4lT-DpWP9i-pw7oolCz_6HVjaAM1meo1n9WKASkChHmm4HsUuKlHqXEViFiTpq7uyYf9xSNzJngYJdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنیف عمران‌زاده: یه شب تو باغ با برادر خانمم مست کردیم تصمیم گرفتم از فوتبال خداحافظی کنم، به خانومم گفتم یه پیام تو پیجم منتشر کنه که من خداحافظی کردم از فوتبال، فردا صبح بیدار شدم از تصمیمی که گرفتم پشیمون شدم ولی رفتم تو گوشی یهو دیدم همه واسم پیام گذاشتن داداش تو ادامه مسیر زندگیت موفق باشی، منم دیگه مجبور شدم از فوتبال خداحافظی کنم با اینکه دلم نمیخواست این کار رو کنم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78256" target="_blank">📅 18:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9eBzYif42E4kp34bwXPpcKL_EeeKj0miAi0pYSg2EpaQP-okfzQJBSXqz0c9TNuALjvIRYJue1tqstBvYsjPunfbODKuITNIlePhSlLZ6cdYmiEWeCzfLyb9BoTO_cRpsfhnHzxOUuH7QI2wSKGs5fLydRrSnLux2DZyQJXnf4KEOJE9mOzSSnXrKyZnxE7wltnE88Z8G4gkqZu0opZM69A76hkM0Dc8nVFGk498V3csIbsAx2NIyo5epee5d0aNdl5jV6Hy2C6wOOMGeez6Hnti6sYrbLYe2aPnLwiKZ9q50HvOS4cNETkEzkA3PVPtMNjFiQOWRs0-pultdYU5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78255" target="_blank">📅 17:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78254">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEvmdyiM4HnLTDocqM6GZ6uS5YuxNOheI9WZc-kaup17L0ojdDdnhym675JoRI2phLTbfBc31EU_F3DvSD0C7bqHUJpb1ZPYsHLx-NgSUehIIxOzHPGGSU0L5lpu2wS4qEtIndNcs7YXdikgmExk9bU0XqY5QJXECo6kLmMMwfMkSM2hjBH9eFZDXHYBBNA3mvgzE3wQtqksUWixhMe9ZdzLLV3DSNNs032XKT6hBmBdJ2BdAVkMrElHcyDv3sKdtvFbc97pLXTcl_camxgrH_i7TCmzYOhKMXT4fosGRp87W1sm6Pz5OQyK4_3_jxGV4iBIBSFEYs_DkFhhWEi_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78254" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78253">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">جام جهانی ۲۰۲۶ با بری بت شیرینه
🔥</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78253" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78252">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎁
🌳
جام جهانی با سوپرایزهای بری بت
🌳
🎁
⭐️
تورنمنت 1،000،000،000 تومانی
⭐️
✨
شارژ اضافه
0️⃣
1️⃣
🔣
برای واریز کریپتویی
💰
🏆
5️⃣
🔣
کش بک روزانه ورزشی
🏆
📱
همین حالا در بری بت ثبت نام کنید تا بهترین‌ها را تجربه کنید
✅
G29
🅰
🔴
ورود به سایت
👇
🔴
https://gfyweuuchsa.shop/fa/affiliates/?btag=914641_l303106
☑️
کانال رسمی ما در تلگرام
👇
☑️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78252" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78251">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN9_EHQwj_W31y3637mEmNGt_yWlUdchkc-bVt-m_CoA67TVRJssNJi2vN3I6QUbZVFW5q3puShIZektqbIkQ7SH4ILOcgmgGIpC_diiEFhMhOuJkgiGf4sBn-_oSjB9eKcAp-SXITr46z1S-KCitIkK1RcDeml23i981JMqyfvwCz5DpflkjR0ajd9rjd4eUdMw6Z-slZQlBELyPURy3TaVIsps19d1N8U_Oq15venO_Pu3LuSzSZS3FKNV1hCRYX9z4whN-SH0VPRijZDmN8_UfJhEl9N-DXKBdrnAk7F3PW6miXByXrvQmIfd8gE9mW12p_i3ZaJe-qIz5AzV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژوتا یالا از قبر بیا بیرون پاس بده دیگه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78251" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnO3i1rXeM1pbj9aocaTYwqe47gBYrE79kheNhSW4nUcuBoVa3SgHWBeSIkkrEqdlVORRjeQULWH1JOYXf52VLYEt-3pW7gVAowt3HgwKPtv_dwnIc3XxD_Uwp1k9GiXZbqJXkqmBCEiAJSjEjVBTLMZnVa1D0ypLKoZ0KTHkTAdbQlDvFfveGgWDquWytsfZF72V9f_VyAex4Fx1IiBjW4WE6THTautqMbSaP8XnG9OhPhHHVEszGrRaUs7U24vo0z8qj_bFJ6y89gOAvWabXgRLlMw-eRDNkNBfOBp6qM7Ukt_IYuFDCw1DZIEPK3pIN5h9utlKN0OWeoj0oMh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78250" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfvfNjp3TTV64OB_EjswTRdHy3mNsR2iOOTSn2sYWD5DqKP8SBj2zztAwQDA643DfSBt1WaBVrvG23XEQzdcHnl-rwxqUZ3cQPqVptemweYpKcg_hWf5nBS0KHWKW_5VS5Uv-UAweD9wWUGBKwPTYyVDVvQrGCLFNtK1CK4X4NvwqdeGiobpCqHxXc_BmcMBUbM9h2FZOcFCdk2G7njs6CMwCnzYJ7rTzOf2m6CdMLPomhwYVtlqbDjj0TJAsGVwjJTtAWHIAUDaavloErBF1iMbWMgfsTHceNPHwJuDiscCTh199wK-buoEx-SqmBB3IcjclE-lEcB2K5Hsic25og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در واکنش به لغو دیدار فردا و کنسل شدن مذاکرات:
«ما از روی استیصال به دنبال دیدار نبودیم؛ این ایران بود که چنین درخواستی داشت. آن‌ها تمام شده‌اند!
ما همان مهلت ۶۰ روزه را تا آخر اجرا می‌کنیم.
هیچ پولی هم دریافت نمی‌کنند؛ حتی یک سنت!»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78248" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vk4F_uLc5i_hVteIa2C17aHzvD2XlAO1x0Rvoe-Cs6cddjoM3pvfCCHFpBe4Q1AcPcrlByaYmgpxsZUOIz43JDcWb1s5PxegnbJYWLdMh7fMSZhbKUsG9hDm6bUOe4JVlOG28Le1ejb_6LU8HcSPVkHkciLCLkpN9v84V9MVwOFzYUMdMFJ8l5FpxEdxKxpFaUheEbuw2Ho068kmMVAXhEilqyUfIRhnFOXzvpkDA1Tk9Utj_9TgT6i8eIvdrp4oE9lFIPmjZ_V7ctWU61Z7AdWk3Z7lUF-52N3M6KMuwfSYFQfVbNkRZzutLErRIFsqvtE89t42D9FdXDb7ie3PwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید بهزاد لیتو به نام "Late night drive" منتشر شد
SoundCloud
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78247" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نتانیاهو: دستور داده ام، جنگ در لبنان با تمام قدرت ادامه یابد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78246" target="_blank">📅 15:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ میاد خایه مالی میکنه و میگه اسرائیل باید حملاتش به لبنان رو متوقف کنه وگرنه باهاشون برخورد میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78245" target="_blank">📅 14:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سپاه باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78244" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78243">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">معاون راهبردی پزشکیان: تجمعات شبانه باید جمع شود. آنها سلامت روانی جامعه را بر هم می‌زنند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78243" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مادر اشکان لئو رو گاییدن الان تو کماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78242" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-rO7yo7XqRaC3MDP9xkZSc8uUqTIKrNJnAPQVNNuEhcRS6jdN3zLvWwaxpbi2glp1STqhyfKUwDCUY67qb1hm676l_mgfDfhb1UqPPZxB8l5T36nGRu8_QUuppAOXTge_R1zZVB65zCJhSs7l_ItWm-YJ39u3P9tADBRF8RR75iW8Wi_UPs5SvT8BBKI7p8CeNM_P-yE8_Uf1bzPRuEaXQ7CZ_E9H1xk2IgeX1e-5rM9zsQTSG-p5WQIEmQFhjghUnM_FDkwXmhNzVVOm2_gYEQM7Uce9NtVxs_TGhbpuHDALLp7g1b3Z-HrKkKsZPfQ0pgyfNZDqwbIJgqgaF0yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم ترین دغدغه این روزام اینه که بدونم این یارو پایین تنه چی میپوشه میاد جلو دوربین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78241" target="_blank">📅 12:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جنوب لبنان چرا منهدم نمیشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78240" target="_blank">📅 11:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aafpymu7aH80vK-d5fs_l8FShvT7NcoSJO5fiDdGZv2_0ORygrbCnImOrO1kpAXuABL7UlOmW1GuVD9ybyCO4oJ0h3_GnHDFXyWXitsPFEpA2QuMeYiWm9wxzZySsNh26Bx05oAW4w82QYpZrcgo-kH1zJgoRlkAwgkXUvb-AmO4M8GA844w207TbZUmJLCq9VvGtzXboCKWsGPmQVb_0o6o9ZN3h_EWgm35Qg10ih4Hpecik3mNcRNayuzWMoOr1Gz2mS14uUODBOqfNFihpwGp119mrGTz9kBRB_BX-fxMA_WTXnrhBFVDc_-EUEq4dnt0TqizSJQod1KNjH-H_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبلنا که ترک پوریو میذاشتم آرشیو تو کمتر از ۲۴ ساعت بالای ۲۰۰۰ تا فوروارد میشد، امارش تقریبا یک سوم شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78239" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDqhtsZBF4415tKZM_aWkmeCjFPf8BqicEvbMYbZtveiMYUGEz64W9I5GzEsWAai_hVfI1XGSUqCH1-0E_wq3j5J05fmTVZ7AQMRcPI5-dqt9pn6qh3pAAFOUn_oDrR4R0jJ0YmiqV_h9LDbelgQM9I70KmHPYg_2H5YUMsfBw_615ewA-452s84MRU6QfjF_LKwHu2S8Ccb_3KpAykhr1HTb6TzjxE4s04wO4Ad1gFsnccyloK2YmrnlftJ89SUnQWtb3os8swu7NKVGF6PhIaGFJxExYu6Ip4ebLwKTfYLD_K950bAzr1CRhCxqommimnHrgf80-T29SrtXjM3UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای مادرجنده
💔
آقای مادرجنده چقد فید شدی آقای مادرجنده
💔
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78238" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78237" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78237" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2x87FCRuDjwVnRa7xuoCKynmcV4YPhX0a_AHA10jl5-avjeO8cv2ZfhP6ezCv_KcYt_RXV3kQmN_7CgS3Bwp4e8ontd1VbnwxDaEl969W3986juq8kHe3K-dZ7A4lw4qNCVb_touEZXXwpyEWBvKsseT5cLLw1TiZCSbEdK_rELJBqpqj4PIWDt6UYLbkd4nKHAE-3CGlToW2gyq8AK49TrGopmYzQh9Rid5ULWbPBepbZYH9qqUcj73FJcxmvW-eBF87mQVYoo06DqURyzvfgiATxKIQIj1PKJDRYQX3sv7QI5P6lzXnsx5VSA_tI_5Jm0L3Kr02yWxNo_3hBvAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r29
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78236" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سوییس کنسل شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78235" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ولی سکانس به درک واصل شدن حرمله >>>>
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78234" target="_blank">📅 02:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستان کسی از ساعت دقیق پخش مختارنامه خبر داره؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78233" target="_blank">📅 02:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78230" target="_blank">📅 00:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اون سازمان دریانوردی که اسمش یادم نیس: تنگه هرمز گشاد شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78229" target="_blank">📅 23:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تروخدا وضعیتو المیادین: هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78228" target="_blank">📅 23:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تروخدا وضعیتو
المیادین:
هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78227" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78226">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شجاع خلیلزاده به عنوان مادرکسه ترین موجود هفته اول جام جهانی انتخاب شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78226" target="_blank">📅 23:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2OckjRBjiZDsxQhNFgCRdhHn6gICFhB9KZM_2HdmTyIx8yrOypiDEAMbsHpEFqE0ZqZRU-GLGPdViXtRChfFvRp6C6nSVZSuqqe0UT6rJWAccKSzvo4ld0uzoksszu8rWY1kyeFwEewen4FJU8Jw5C67a_5OT8Lm6W9WGcJDsXUlWzTgcsflbdYTDFm03Hql406R4DUVNxo9UN3g2QqB8R-nDCoSXO37YZBdpdz1kL5n4-t1KlqunKbGah3jpxxZAdm-_CBv-cGHZulxkezr0knTugaOWYqOMaPHzFxIYAAoH0frJpM3Ph9UVIEWNRvYWNPvgrz-_OdtH7F_cWHAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام چه داره پیشرفت میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78225" target="_blank">📅 23:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78224" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78223">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWeera news | ویرا نیوز</strong></div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78223" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJLnG3I55TC6XWPZ8hwo3ipdyl6WttrSc5-f_uow2f0y7aY-84CJrcP88O-u5iLNUJgmcoTkbR-nZLIQtod2cy6Ywamec9nEUQZ840Urox3woP8_gDT7FHMExHU9z2xN0qIJI6Z3Y7oFVeIyCDk6l97AVVTcQkogrfQmuEVeuNh4bO3gQoTmnubfFgRHa2kO10O_7YjRbcrJQQgOg85XORQ3MGSGOSmUAqC9mjhE2xyEtqu6VH86h_FWiHosXt-I_bNED4tUCc2GuxIQi9_hBhrIc23p9I4-4XZxa_Ej4D70UlUNps3JuhtQ5umwOqwdgOcQ-1zkOu8CAOkLgBaMaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون ۱۰ نسل قبل یارو نسل کشی کردن یعنی این دختره خوشگل نیست؟ خار منطق
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78222" target="_blank">📅 22:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78221">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خب حل شد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78221" target="_blank">📅 21:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78220">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شما جنبه افغانستان ندارید، بزار یچی دیگه بزارم</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78220" target="_blank">📅 21:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پوری کیرم دهنت کاش خایمال نبودی</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78219" target="_blank">📅 21:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تنها کسی که میتونه برینه وسط مذاکرات تندرو های داخلی ایرانن، تحلیلای مرادویسی من‌باب نتانیاهو همه کاره اس رو جدی نگیرید، نتانیاهو خیلی وقته قدرتش تو لابی کردن در آمریکا از دست داده و توهم اینکه آمریکا سگِ اسرائیله هم از تفکرات رائفی پور طوره
ونس امشب یه حرف حقی زد، نتانیاهو بدون ترامپ و آمریکا(عملا یعنی بدون جمهوری خواه ها) هیچه.
تا فردا صبحم لبنانو بزنن هیچ آتش بسی نقض نمیشه، ولی تندرو ها تنها کسایی هستن که میتونن کیر کنن تو توافق بین ایران و آمریکا
اینکه مجتبی خامنه ای امشب همه چیو ریخت رو پزشکیان اگه نتونن جو رو کنترل کنن میتونه استارت یه درگیری داخلی بین موافقان و مخالفان مذاکره باشه
تنکس فور یور اتنشن تو دیس متر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78218" target="_blank">📅 21:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78217" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a862002bab.mp4?token=DRtWhtW9fKROwlCtwaw4ziGxAutfF-Hz7bbfrQmSOIBkl1VaNtCt8esVloim2aFOmkD_OQojy_QMByZau0F-ZUU5vpSR7mJK8nt5PGoaBiSdyGDBXffIBx0m7MaIzS5w4kEjclWevBDcqPN50Dy8x60p3oK3DZaglCRbw1MqrH4NNQ63wvw-o6Mqka9elEQmCmb5HAMN-8v_6Nnzn1ZKvDIW8gpiQVFZPNXb9L7Fg1j1N5_ivRqJCOnQbmIVGqvG1qt0F9RGTJflc4gMLQMA3CnYQggOZQD06xGOto6pUyVT3yATLNqF8p4ARjKBDIE0Zes0-mr4zQvWonGhq7xSJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a862002bab.mp4?token=DRtWhtW9fKROwlCtwaw4ziGxAutfF-Hz7bbfrQmSOIBkl1VaNtCt8esVloim2aFOmkD_OQojy_QMByZau0F-ZUU5vpSR7mJK8nt5PGoaBiSdyGDBXffIBx0m7MaIzS5w4kEjclWevBDcqPN50Dy8x60p3oK3DZaglCRbw1MqrH4NNQ63wvw-o6Mqka9elEQmCmb5HAMN-8v_6Nnzn1ZKvDIW8gpiQVFZPNXb9L7Fg1j1N5_ivRqJCOnQbmIVGqvG1qt0F9RGTJflc4gMLQMA3CnYQggOZQD06xGOto6pUyVT3yATLNqF8p4ARjKBDIE0Zes0-mr4zQvWonGhq7xSJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظریه داروین درمورد تکامل انسان
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78216" target="_blank">📅 20:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">محاصره دریایی تموم شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78215" target="_blank">📅 20:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78214" target="_blank">📅 20:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78213">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSEnqXlsnOKi5CnuyxqKP9xIKwBhNTOx0WqAUl0EP9-7ZcOq79kJD3M0iYipuqo3ctZOVNEkcjIW_b7MqnFvqtNiO6BGpedCNukPzol2zq1xi_dKpbavEf_gvv5bQM5AWbMjQpO-DdAMlNClqRXe83AR56NmDYcsVw3mJVvSqmOAjXte59trAXvxjCV_EF7leY6-Ht5CdPFZ51ng7qvvO9VP4sItADFETTAcdmfZWRffEwQgt72VMowF5H6oqj4MxXnDRV1Um4Y07tpmQepNFnqw-rFFckcfOxMJV3s_n-D8tDE9hWIA-5qWL6dav-x7YUscIBlHNbl0e-zcJtCH-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتو جدید ممد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78213" target="_blank">📅 19:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78212">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEnhUSv_zh2rDfe0Np4Yl_VN0DNKNv4nUZWZHFeUCkOtxHujzct4YH22nd-VcO9-LT9431khz4Yaebo_xKrZPfK3ChqI0qHDSq7e6sFTLiv7yS2-bWcHmGsZTRB8ny8qFrNp-AMxxG6pVCukK8rvVVEyVBzUymKtSkLfZBsni_IQwaUirgGgmjyIIX68_akDVHJv-qw4Zjs-tXUkFA70l20aJAsD4ORBMXoOcoaGUzCRzkNMJRTMHNEf9iLr_uiOK_DYps9ImZLUzoA6eMtT0yRlebrsxSaXqC4dVc9FH6n4IvrY0DtjODj5bkT-IpSYkLRcGg27HI98v95vaUbkBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری عماد قویدل برای پوری
@FunHipHop
| Behi</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78212" target="_blank">📅 19:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGzY3gNXrKTkWG_5QBin_jzFTZj6vFUDIlfwYUupMUKJPDBbegxTLyMm0ayUAHixq3nWRxwOJVnjbULJ63WTjrYOnbr1XgxHmP2yUgWI7CFt3MGXDWOjaMPbfLbFfPfS_vSzFo2lsNnSl0-1qot_NNc6oJgLpxeDGyDNU3XirB4tVUhix3oaqgbMQ6FmTblfQSlYx-gYkXXfN4LP8Lb7fmA0PeIAFEmgQcEARku1E6NC_P0ECJVb13bqojUvOf1ch1waV-l3qQFrPaCoNh7aV5KSYS7QBi9_yFvlGF6hAVOIZ3L0T7C4Eo4njFpEl7_jFuyKYEl3SgjBxVehJKu0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4 کامیون ایموجی خنده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78211" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78210" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78209">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oK12QOVpVv8DMXzbLOzSV_wyr2iQyp4ecQ1_88nc2Sz6DWQVWp9qE42qV1DzOD4gpDOjBaD0_6LSwegRc8Pvm7SsNxDa4gaT1vBRN7cqlYiaEwFmG9W-9IvUpQv_RTiXamtTwDNqK8uDtgTVKlDPRkSVp3SBiwOXOGZwLUo0bvXbQgDv3-4M5EzsxJZEg-ikfOzy6dkXDlY47IMY0vxCHddPB1jsja_EoqkEK786thAkZvUPAT78aH2WuUE8rw6XDtKR_8kxxW8gAHBOf_kiXMkyoqQNXSMkCB9trLmpBKydTKn6cK0eh5YBzt-bh7oxxOluYsYLCCpH2x6pRtq0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78209" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZWiHcz0p47It9ELHtXg5Vc2MonkR2AKN973PCwTDoOu_UxjC11HdW-lSa5mOoQIf-MDquyiABEXYzXMDeHDZSjdIi89woSOKfLRufF01yL4LyUWFkXsRwSNK1ISqjGZZSfu01jLjE0TtUsBBsCPElfgKDN1cL_AA9jRFTCpZOqscFEXsBuW8iMMRyqw83kWOTylf6n8OidVG-z_vHCPPLIpiNHrSq9afEGRdXOKGMhPbth2yA9-cccKyA2FzeRJinFjeSoRxJosqPmm6zQQjHFtXNUSLY27qHZmg8w1HR1RhFL-zciY37wt4N_x3s-HTSOgaCty4SJeMd35jjKDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند ساله ترجیح دادم پول سیگار
بشه غذا واسه حیوونای تو خیابون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78208" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78207" target="_blank">📅 18:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQY-l4i0ZsQsnS3fKNS3LoUS3DNQ83H2m_dmQoHOzy8JspT1j0waeT7LCK2oTSOaweFZzLr6WI0xV0rL4ZSp8pLh7sIvCdSNmVyYsdeYszDkIS7G8aDbbxpD_mGAMVRBXBFYGRXLyFT34v7XPlRB1crlj06CDbUze1drjCo239ZS15UkC1Azd4-tl3Sma3kJE8KWeayqWh1L90JSOMUNTvTI5hf1A7MTDkh-N6N4JVxeA8YXL1Gi68kiIzAHihC75DsVZ-s3Mn1SfnwTIk7Gqy1FsamdVwQ98P5wvJfIMMrEIXmQV7e5b5dR55SuQqRzRr6AaamRVbu0fFy2yc940A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب جام‌جهانی
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78206" target="_blank">📅 18:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78205">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLk</strong></div>
<div class="tg-text">بچه بودم دوست داشتم مثل رونالدو بازی کنم،
الان رونالدو مثل من بازی می‌کنه</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78205" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78204">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF9nMn58So5KyVjc8iW4AqbyI12OkFCD_WMujD3j67XntTlClwTIvokgYFCbQs23EY8MIc47X0Gxh_kq6X5cVpHW2F17Ocq3R_Fdir803F2anQ-zRyBvV938RpCXa84EdI4zElBSyix2_V2Ajea4jf1CbjIdjetAAQvdJDZ83Qs_8_JxzK2jL7d527KGhCCwKYp8AeqQ1bdTOdBAV6yporJBML6ZOrs0juOyZxzEEI0SjZiDjxAGpmzXuJbuj3qvErYoybUv6Qg3nC2alm2DOMCOcex4UP4_3HKmjjX-gnzPIOmd5Tt3cetOGc5aAOb6Yt6AT_sZrShYirHeSuMxuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای تاپ دنیا توی اولین بازیشون درخشیدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78204" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78201" target="_blank">📅 17:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpfrJpgYJY_H3NxwHiDgY9axRyQroZsgT80NYEbKBbUdogRnKBrJvmfHD4C0pXY7GkUi65LJjs-SKD-YJ1sLuG4Va-00QOcRb33pQ1CDe-rks4xz8Uu_9wUCKVCZG_6NecRoNHnnhvFgqtHPX2dXgLQ_IoxdBKfrbLxrcJu82mHy4BGce25ym1xFpDFu3w5QpcuixYw2NVCKpbxkHKqZtzW2KMm8uXqWAYQqGlXk0RL0-82SgegQ6cctLZzag2lDNoFslDT4vyg1npasPyvGui9JU4nU4T_ZnHn8fDIgVgx5q3KT5y5T3sHDUQ5QDHFyhlBvKnZ72MGkAhRXm7BX6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم سرپا ریلیز شد   YouTube  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78200" target="_blank">📅 17:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEjG7bTHJkqW4QBjAAzMmKkWTQhC24kBvIhi-H4DDibxst-URV38CZLqUv-eiVhntM_pvCxqgeyCV4vMfVr52lWPsKKK9pFmAN7u1gLEe1tsvWuqZLx9nsD-s3LhnrjBsFm4zLwJZVbfqsVF4naexRq2r0tpIevishb-7iUVR6b2AkWi2pifqqT-CUsMayjU3JriF76lC80_qm6kZB6l_8PuWmSLqkdwKUTrRDYUJUXA4ec7-COc9i0LmNgmTLjZeygqBm1y0auRoH0ljflHotPTuwXb66VGE92mIFd-0hO_NYMZ5EoiXNy8J5wepHdza4xf00s53EJqLmKwD4nQKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم
سرپا
ریلیز شد
YouTube
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78199" target="_blank">📅 17:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78198">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وقتی مردم ایران صدای بمب‌ها را نمی‌شنوند، ناراحت می‌شوند؛ آن‌ها می‌خواهند همچنان صدای بمب‌ها را بشنوند. چون آن‌ها می‌خواهند آزاد شوند.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78198" target="_blank">📅 17:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ: فقط مردمان دیوانه میگویند کشورم را بمباران کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78197" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CC0OeLEFZKl2Ibf4yxsjV-XK293MxdZd2hPr8SnzeElXUWYV08CJb6tN4usnP5cT4D4cts9V6u5PuElSUmGPTPcMawuPa7gPvWhwIfsWIsjmE3BsE_KPKGFP9aCMfKYL6Bsm2zsdLS0pfoKzdEEkVNmEdMPWGdXYwunh6cj7O4RW8IYiVTkIm1192WujHpGufuA02OnPh3A2Nb8PfAwNh19CcvcON-q_BIcuR3eQG77pAx8rKuRfT2Nopqm6mDY70ZV5ggHcrNQ-2DJwSTQUYcpMipIqGmnqj1MeU3jAcnZXjYD4utPDxOghM8v1XBkkMwXqu6GZBhUDicPI6yvlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78196" target="_blank">📅 16:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpdVMRLEo1Lm06cmRUOKqWX9CMHZ0n7HKXGifoe50GxTTqpNe3YZV3PO_dFKXDXCRMnrwYe7N7qQiog5sdRxQECuPvFgs-uCtAiSqs3aK1CGhDTGDs35bq3UVltNnc-YqyHarMBpcN7_ZsQ4TFKNxw9-2WWtMTB3pZ260zgDstSi0nuaYxvzS-08_O_3IqaTiKI65yVTvcWeP-1mD2qnRg5CLXEfIkCgJfOh75tR-f7I8fr9vbAsTqt7N5h3RMiEpTsS43tYzZ_S4FOPQFXYV-eP2lifFZZ_tCmVigaykFITv9VaNQmVTFCK1wBo9mLjuEAKfc9OYUCIUPf0MHNFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سنت خجالت بکش کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78195" target="_blank">📅 16:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78194">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پوری میخوام برم بیرون، سریع تر ترکو ریلیز کن یکم بخندم برم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78194" target="_blank">📅 15:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromuıǝssoɥ pɐɯɯɐɥoW</strong></div>
<div class="tg-text">مهدی واقعا افغانیه؟ آگه آره که کیرم دهن صاحب کانال که یه سگ افغان و ادمین کرده</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78193" target="_blank">📅 15:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06ef661660.mp4?token=LWF4zYFj5Zv2pxgUbymM-mLXT_-IDmxefft2Z14iH75XnaMXwEKBoKQ2GTDwWfgseL8XOuim9eqdqO2nRmjdLQy6aKbzx5jA_4zkRRF61tUbVr5vYtxyhl-0MHzPyEAqfr3zGoB5oYnmBZ5OT6YkRfGohZ3MfvvL1FiqZNRuW78eEyhUJrTu5y-xv8aL-y0D40bdf5VNc3AWNDw_BbO5U_IEgEMmeT7qreeDPhC1VaSl2kGQhNDlIrJbUyUFAm-MmVjZI1QD9j7xbURKNUqkBUddHEIY4a3Wd66VPYTi61vFx09FA41Cyay-TwaJj69O9Wv74Rzg-4uMckXa4elMdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06ef661660.mp4?token=LWF4zYFj5Zv2pxgUbymM-mLXT_-IDmxefft2Z14iH75XnaMXwEKBoKQ2GTDwWfgseL8XOuim9eqdqO2nRmjdLQy6aKbzx5jA_4zkRRF61tUbVr5vYtxyhl-0MHzPyEAqfr3zGoB5oYnmBZ5OT6YkRfGohZ3MfvvL1FiqZNRuW78eEyhUJrTu5y-xv8aL-y0D40bdf5VNc3AWNDw_BbO5U_IEgEMmeT7qreeDPhC1VaSl2kGQhNDlIrJbUyUFAm-MmVjZI1QD9j7xbURKNUqkBUddHEIY4a3Wd66VPYTi61vFx09FA41Cyay-TwaJj69O9Wv74Rzg-4uMckXa4elMdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریچ یک کانادا و حومه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78192" target="_blank">📅 15:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">راستی محرمه، پرچم عوض شد</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78191" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انقد همه پرچم گذاشتن جلو اسمشون منم تصمیم گرفتم بزارم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78190" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fX1nRiBY3s0eEfcCTZRmRMKHp3cy8_m3v5t_8ZFY2t49nMIqfNyk_po0S3tOPOg2jHQgYfJqycJW0FCNb1UR7GTdN8Blh6h7rSOH65ap8iVU0sZPYIXRZPu1o3BeLTkKSUAiwoBXlLkxcv9Fv8_YepRVbuNvIsGsB0uxbYVyvvFlPhDZJOZ4V8jOE6Mgbd6noTAQ3GQQsm3KRYe-SwZKY3vGi2BL4qy3mUPKao3y55uROesBaoNt4aKNZt0wSJzY7YaLM1N1tGMxOVUkN_n5yI4UtNfgur6X6i_Db2-tAJcn6YplOdJ1EV2fWQkd4tMLR2H-WENoiMxEovtT532XhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت اوردم براتون که توش میتونید خودتونو درحالت امضای توافق با آمریکا قرار بدید
پرامپتش:
A tight close-up mirror selfie, black and white, grainy backstage aesthetic.
Subject 1 (Foreground): A young man with messy, sweaty wavy hair. He is wearing a tight superhero suit with a web texture. His face has realistic battle-damage makeup (cuts, dirt, bruises) and he looks exhausted but calm.
Subject 2 (Right): A girl leaning her chin heavily on the man's shoulder, snuggling in very close. She is holding a small retro silver camera directly to her eye, covering half her face, smiling.
The lighting is harsh and direct (flash photography style), creating strong shadows. The background is cluttered with a hanging white t-shirt and messy towels. High noise, raw, candid snapshot.
‌
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78189" target="_blank">📅 14:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78186">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78186" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78185">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78185" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78184">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uthCF6rHRVR3ocnGZtb9BdJXUGrE7P5UfogMShRRdei5KVB_2au_CDVaijgdszXC5ezjtjYURDNVmsLiNPXh2JYNSsJE0C2OwGkFZdwnJTh4hA9z8_96Ridiu5LkRMXANSAGk4zNnBTwb1XZbM7sEl70o3Y2dzwQt3SF4EJC8UnriDTNvE2a6iz1pBvrtKmLPLHYD7YqK1Mj_GoNWVc5zrd6Tol6Oy4zRsM9w8uMce0CDGcjeksceS1wtcptrY9SQMY-nc2Rq2bwLOCYQUx7tEmBKfApvZS1Aiwb_ankMKNppXJR8rBlvfeOamN3IzNTdEEm3zrGnICzuvoazKJmvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78184" target="_blank">📅 13:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خب دیگه توافق هم امضا شد و مانعی برای سخنرانی مقام معظم رهبری در ملا عام وجود ندارد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78182" target="_blank">📅 13:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78181" target="_blank">📅 12:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be-hkxUdop2_7SQ03FB94Ay_eCRj-_XP2DeAHYjj3dFPDtO2Kd3gT-VlMSPIm46v4WuRn6bkXU9MdqNHLjW67SOgrrfi-zE7jvS6XZT6OH7yzLfYNxu3bFh2Y8qSP2Gsmxt2fm8BFYuaDymlBlAMF_diPAJ21AZC31j1WTiDxWAjoSd3NJPfvpZqYSgOoWs3jUgOUS141KT40ZKw79TqhxOqHvkrrYUOtONXBTNkhnKwSQZs3qYjJrxPitusOr4Hu8GkzhO087_gKHtsVhAesQwS9A5FWauOwAP2CHuMU8pS0XidigZcXrL38d2qMCmJUTJ2oXhQHXz1OwIM5Zu1vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78180" target="_blank">📅 12:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عرفان چطوری میتونی انقد کصشر باشی داداش</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78179" target="_blank">📅 12:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78178">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آرتا:‌ کصه بشینه نمیره عین جمهوری اسلامی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78178" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78177">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78177" target="_blank">📅 12:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78176">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78176" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78174">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhdm9TCbT1Ra5XiM_HNg1UbX9z9HTlqcTNwHLfB3QgDId6LovLbRvSFSYjJ7blcQ4qKc7nHv9xLeJAo36GwKBal5itPkt9Oh8W3rtAd4KkeipMeaGEYtJ1jS5c7X62kisY79rKnMhaM_rKoFqwf2oMbBB4UuGvXMqnLEwwu3aS90Oy4B978yNoMy3CHXIaRMm_XJVJY3lXUjJWTYV1xLz1GigWKT3tO7WaB84a-yZpKYzQkzsn41xhp4ezjaYDJv15zinSehsnwLqkjREw2UPy9j4Sz2O4jaNz6S7vinYXN489zeMngI7_GPJKy7g-1QzTEkv33EJTEJJMlCdtVYZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.
Download
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78174" target="_blank">📅 12:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78173">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آرتا، ویناک، عرفان پایدار، کوروش و کچی فیت دادن</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78173" target="_blank">📅 12:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78172">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBgzWYZ-pNYXI8canqVoPfPkom1SGli8fD5MTqAuvcDESURsn2gu0tP4CPe-m-Qn5I7D2D2CtbCSPc1qRtxzx8iad2LYvWHH3_G_s7IQI4uTJUDr99mirYhFMKw8XNDIXEltKf8W1Tdf41lsex58Ra097zDOYG-TssZ0--JGPS6xblqlIBl7yTFI5gZZRpI7cJ-6aivq3DrDLObwJFweU584gKy_9GUVOPARmdNE65cwSnxxIP3Yn_PYSKSvkCBJSyEPAjJUAn-e8pxuhvrhSS-1bastcgbPZWVsnGQOAAt_2Xl4eL999qOlRNTQKFshgswp6AEPktm_hUuUBFpx4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرانی بدون خایه نمیمونه، بالاخره یه جفت خایه پیدا میکنه برا مالیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78172" target="_blank">📅 12:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78171">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آیت الله سید دونالد الدین ترامپ(دالگخیز): عادلانه نیست تمام کشورها موشک داشته باشند اما ایران نداشته باشد
آنها باید بتوانند دفاع کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78171" target="_blank">📅 12:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78170">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رائفی پور: اگر میخواستین توافق کنید قبل از ۹ اسفند میکردین حداقل رهبرمون زنده بمونه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78170" target="_blank">📅 11:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78169">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رائفی پور: اگر میخواستین توافق کنید قبل از ۹ اسفند میکردین حداقل رهبرمون زنده بمونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78169" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78168">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شاهین نجفی نوستراداموس   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78168" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
