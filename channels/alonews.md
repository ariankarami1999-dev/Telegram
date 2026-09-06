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
<img src="https://cdn4.telesco.pe/file/E6cKWQOx-yDAbk-v8gzhJlDanBJCqXifrCkbS27-ovHnwsD0DB_3GjzFkgbGGqAHTErkPoq6Ge-GpiReSDNavJJxu2HS5P64PMp-Y71jlRBWXawHpFzRtVnqYtiwNGEsoJ463ongW-X835ElEprmG2s7n7TT4XODT-ZHu5YONY4lrB_uBRNJOFNp1xzAf8WaBhDWHa3cbe2H1cd9W1JoQ_eRk1smpTsOZOi7SEPahnyFeu-i0gbYeuG09vLsiKQ6sCBiYakcuGEnZaYf8G-cpnbUFbhNpyhsreTwvzXbx1m51DshrhgmdJpJv4sGqMmBbZQufdwas8fEmmy7bHr0Gw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 934K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 19:31:23</div>
<hr>

<div class="tg-post" id="msg-145934">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
غلامعلی حداد عادل : آقا مجتبی خامنه ای خیلی ساده زیسته
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/alonews/145934" target="_blank">📅 19:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145933">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) اعلام کردند که یک پهپاد شناسایی تسلیح‌شده وینگ لوانگ II نیروی هوایی پادشاهی عربی سعودی را در حالی که مأموریت‌های «تعدی‌کارانه» را در شمال مقبانه در استان تعز انجام می‌داد، امروز صبح با یک «سلاح مناسب» سرنگون کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/145933" target="_blank">📅 19:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
حمله اسرائیل به یک خودرو در جنوب لبنان
🔴
اسرائیل در «النبطیه» یک خودرو را با پهپاد هدف قرار داد که به زخمی شدن چند نفر منجر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/145932" target="_blank">📅 19:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145931">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIOkjNmZW5kpShPp_BEJOWYIjXqROdE7GHYPY5FxvXPV-2Yq9ow_rilFsNl9Dwt0_Ss6Qt6UedRQ2efFPLbGmovh5z6UMIkglH4CWsxXu8N-cYXxpZkSNq0GvMwl1LlZ8KThCXxEEAzWsP2HWLrJuOR1PDtjPM9LxYLat9Nvzw4AcqE85qiN1IMuwAU2g4krxoFPmaNWCYBisN-01CgOClHlD7OzAmAjWwnzw4gftiCoGbYJXk3lM1hUli0YTKz4Hts534fxlREQuWHlHWb9KRcPHHpOiggdAHn6XvqNVgXGYsOimc2WCE10wdX3DMCOb5-BgAMnNs27wKWETG3kNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طعنه اقتصادی قالیباف به بسنت: چرخ‌ها را بالا ببرید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/145931" target="_blank">📅 19:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145930">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس اعلام کرده ماده ۹ طرح «اقدام راهبردی تأمین امنیت و پیشرفت تنگه هرمز» در این کمیسیون به تصویب رسیده است.
🔴
بر اساس این ماده، کشورها یا اشخاص حقیقی و حقوقی که علیه ایران تحریم یکجانبه اعمال کنند یا اقدام خصمانه‌ای انجام دهند، مشمول ممنوعیت عبور از تنگه هرمز خواهند شد.
🔴
طبق این مصوبه، عبور شناورها یا محموله‌های مرتبط با این افراد و کشورها از تنگه هرمز ممنوع خواهد بود و دو مرجع برای تشخیص مصادیق این موضوع تعیین شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/145930" target="_blank">📅 18:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145929">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
روحانی : باید با مردم مشورت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/145929" target="_blank">📅 18:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145928">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ویتکاف: از مذاکره با اوکراین راضی هستم
🔴
«استیو ویتکاف» فرستاده ویژه آمریکا: از مذاکرات جدی و مهم با اوکراین راضی و به ادامه آن خوش‌بین هستم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/145928" target="_blank">📅 18:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145927">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ_6japBhm6npy7VBVLLONOnN2iwF8YGRmwXUTuitMV-5Mhcsy_0nqJ7Qo0wmLABJv-nZlg7GkoaRSEtOPbYg5zrKS_HXUnYgTp03rPztENBve88gNmzpuaTSSnvYLC0Jr-vUKw6sW98xlDbxL_jY4kuRiO1b7_pJvw7ssQ9x2jv2osgoDAN6GmS6scFTe0SlzaWTG-Da9z3AfLlt2S8R4XeAs2ibcIeoc23hdZlkoTo1CXC8zMhnClRMO4Qx7Xz88KpWFD5xlXWAXZCYoohrU6B-3SrE_2SqiBhjWN3pHwWlz6YG-jJi2QLfrvPlmABhqGehBBeXwd0aLmjAPhcuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انگار ترامپ موهاشو رنگ کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/145927" target="_blank">📅 18:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=gEA0MMp_oFLlq1OiqPD1LS7ozQH3CgdZLywpsHZ2owxPYdJGq6a8oNU2ZSnNP9d5O7ZsBr-6t1iQCi4dKhs6byFaAMhe7FpXLxEsKY0b5MAbUWgjJgN5ITa5pWusieC0Bw1bGP2gPz4E_M7AX3FfJfGWWumWtbi8cNiGTnTJJlbmKt29XrGBo0SZ2tf4FjQotcKewVb1ZVlcmab_5M6fbptKb9jXMCHbr-BsJR5QdvyyVjsoWEQUP6LxOTbIyBhBxyZ3lBJeZDSh2mz8Do_APawq1bJ3zG1711xR_ddAD4DLhKYQ8_AqOYZeGyJatMRSHOwa4yEoZNvXtRAO1N9Idg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=gEA0MMp_oFLlq1OiqPD1LS7ozQH3CgdZLywpsHZ2owxPYdJGq6a8oNU2ZSnNP9d5O7ZsBr-6t1iQCi4dKhs6byFaAMhe7FpXLxEsKY0b5MAbUWgjJgN5ITa5pWusieC0Bw1bGP2gPz4E_M7AX3FfJfGWWumWtbi8cNiGTnTJJlbmKt29XrGBo0SZ2tf4FjQotcKewVb1ZVlcmab_5M6fbptKb9jXMCHbr-BsJR5QdvyyVjsoWEQUP6LxOTbIyBhBxyZ3lBJeZDSh2mz8Do_APawq1bJ3zG1711xR_ddAD4DLhKYQ8_AqOYZeGyJatMRSHOwa4yEoZNvXtRAO1N9Idg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک سرهنگ ارتش: یه قایق پر بمب با جلیقه انتحاری به من بدید تا خودمو بکوبم به ناو آمریکایی و شکست بخورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/145925" target="_blank">📅 18:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145924">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0406c9675d.mp4?token=QVwHfIBLxelPW7kd_IhL64zxQccfKM5SbgkYLr7upCrvCzeCfQzbGuYhWz9SNNjjzGHWzS6DTOvpJE3eZKhg_HJe9rVK5YiNo2dZDTrOQW0qQdQyDgfpGyoHyDX7ds5mx4_IFzKW7pl3LoUl0zmI1frXS5Mv0cKF1IgCHhd0U6VunEvmMBperWHf9RWTi4IUWwj-YdcIoxPQDit6vyeeJoO-XA4_QaqWIR8Y1F7aFnP7OWEs3Gayi571uLfSHlZc4oI_OclPmEybeKTX4jSVjK-5MeMmv0TreTNkaygtWqEmhgkva2yW2rUScfXsOtwARbv4fINl63rtjnm_2fZNuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0406c9675d.mp4?token=QVwHfIBLxelPW7kd_IhL64zxQccfKM5SbgkYLr7upCrvCzeCfQzbGuYhWz9SNNjjzGHWzS6DTOvpJE3eZKhg_HJe9rVK5YiNo2dZDTrOQW0qQdQyDgfpGyoHyDX7ds5mx4_IFzKW7pl3LoUl0zmI1frXS5Mv0cKF1IgCHhd0U6VunEvmMBperWHf9RWTi4IUWwj-YdcIoxPQDit6vyeeJoO-XA4_QaqWIR8Y1F7aFnP7OWEs3Gayi571uLfSHlZc4oI_OclPmEybeKTX4jSVjK-5MeMmv0TreTNkaygtWqEmhgkva2yW2rUScfXsOtwARbv4fINl63rtjnm_2fZNuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهران مدیری سال 1401: نمیخوام یک فریم از من پخش بشه
مهران مدیری سال 1405 یه سریال 15قسمتی به صداسیما داد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/145924" target="_blank">📅 18:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
ترامپ گفته ایران دیگه نفتی برای عرضه نداره… چین هم نهایتا ۳۰ میلیون بشکه دیگه از ایران میخره.. محاصره هم دلارو قفل کرده
🚫
اوضاعی داریم..  @ramezanii_fx</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/145923" target="_blank">📅 18:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nip7Q_mnasYrvJZ3MIH5ZuufcdKMBwYgUJfqJryTaInCBwctdSPuFoGhtgSGsTFNlif2csaD2_r5F1OQB-83y6fwapK2zB4v6gxaJQIf87Kqgc2R8xxRtyHOXRSaUQu8Z8kIyGB6RU0Xt60pUZ8kFCKuXagdvygRfha7Un22LsrxjTsY22LDFXJMNBxnXhOOmF7vlvx6Zw09hA_tZE2DNImmOhzadthjKUktRhVb3XV02YT58-DzKssSqU_oyWW4xHxx1-GoQBn8n91bJIqwAbCDA7op1b_FGGRmcnJaLC-O6H3QEIE7JQOCcP7Vf9RkYlhrQjGNVLyTdyjbp5CNEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هیئت قطری به سمت تهران حرکت می‌کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145922" target="_blank">📅 18:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145921">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
گزارش ایسنا: ۷۵ درصد کاربران ایرانی از فیلترشکن استفاده می‌کنند
🔴
نتایج یک گزارش از شکل‌گیری بازاری گسترده در پی محدودیت‌های اینترنتی حکایت دارد؛ بازاری که اندازه سالانه آن حدود ۱۰۵ هزار میلیارد تومان برآورد شده است.
🔴
براساس این گزارش، حدود ۷۵ درصد کاربران ایرانی از فیلترشکن استفاده می‌کنند و در دوره‌هایی مانند «اوج خاموشی»، قیمت برخی بسته‌های فیلترشکن تا ۲۳۴ برابر افزایش یافته است.
🔴
این گزارش افزایش هزینه دسترسی به اینترنت آزاد و رشد بازارهای غیررسمی پیرامون محدودیت‌های اینترنتی را از پیامدهای وضعیت موجود عنوان کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145921" target="_blank">📅 18:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145920">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr_xx6Eu8GpKxWnsjbVAKVtkmsam-qf_rSfaJ5CHDQENv5msFf5I8DB01FIjzCjbK2QMd-fwSlQSxNbUj75gITRoXRclqbUebWIGgboi7zcup4Ra-FAXujOjeUk9Mwr33PdEjmM9bplIYRsN9F0Ewjevjnr9VfktcDsXtLiAq1yq2Sb-7oWTZSpC4RBggi8V6Jjo99FO-EXzw1ma2X0QG2hucYuWqYUZ3v3u9TCNTACWGP0Dwvbt-0bUoimiUFGSLTDgZhnfxPJCY38L3OHLhjWl378fclRsmaW0AyP_A0X93CgyogmY9cbA4AIJ4i4LAk1rODki1VDDdg-WcY_4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت داماد آیت الله روحانی
: علی‌الاصول، روی اصول خود ایستاده است؛ مردی که ز عصر خود فراتر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/alonews/145920" target="_blank">📅 18:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145919">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
اویل پرایس: اختلالات شش‌ماهه در هرمز حدود ۳۳۰ میلیارد دلار به هزینه واردات انرژی جهان افزوده و حالا از عربستان و امارات تا عراق، کویت و قطر، خطوط لوله زمینی و بنادر خارج از هرمز به یکی از مهم‌ترین اولویت‌های امنیت انرژی و سرمایه‌گذاری منطقه تبدیل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/145919" target="_blank">📅 18:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145918">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
جزئیات عملیات مخفیانه مین‌روبی آمریکا در تنگه هرمز
🔴
آمریکا عمدتاً در طول شب، غواصان نیروی دریایی موسوم به Navy SEAL، قایق‌های رباتیک و تجهیزات تخصصی زیرآبی را وارد آب‌های خطرناک تنگه کرده است تا طی یک مأموریت چهارماهه، مین‌های دریایی را پاک‌سازی کند.
🔴
این عملیات دشوار برای خنثی‌سازی مواد منفجره، در زیر آب و در تاریکی انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/alonews/145918" target="_blank">📅 18:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145917">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
روزی که تلگرام رو به بهونه تاثیرگذاری تو گرون شدن دلار و سکه فیلتر کردن، سکه ۱میلیون ۸۴۰ هزار تومن و دلار ۵۸۰۰ تومن بود!
🔴
جالب اینه اون قاضی که حکم فیلتر رو داد بعدا به جرم فساد راهی زندان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/145917" target="_blank">📅 17:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145916">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
حمله توپخانه‌ای عربستان به یمن
🔴
منابع خبری از حملات توپخانه‌ای عربستان سعودی به شهرستان مرزی شدا در استان صعده یمن گزارش می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/145916" target="_blank">📅 17:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145915">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
عضو تیم رسانه‌ای قالیباف: بیش از ۵۰ روز است دیگر تفاهمی نداریم و نتوانستیم به حزب‌الله کمک کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/145915" target="_blank">📅 17:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145914">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=oL0iM6OeGeoGCSN6I8wvm23DhzevRhDURHhPkOeOc9f_ATa1dxedbCjIHWzkXhqfsvs2A1eDAYQluWquCSQPlw5_9X6FKY9Mo_lmqEecawiM_5Y34AzI4LsUfMth9GU1RS1Dl-LSSiYhWlMpKOWFqRdxzNjLeTo69citgGGMh9wHybDeOlP3y8UJEP-vZMXB5AbxD-n70y5JTl52gWjY9bMFMVGplkOI6qFZe2vM800dxJ3oRH3kVG3SIWUne2WwcoOZx7bqp3CNBGDT_jttWrLahWP-xuJSTC7sCutEGYbJSCBXlw7DlzItZQaoAZOVLMTjGOKxuqsth3Otmr3o0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=oL0iM6OeGeoGCSN6I8wvm23DhzevRhDURHhPkOeOc9f_ATa1dxedbCjIHWzkXhqfsvs2A1eDAYQluWquCSQPlw5_9X6FKY9Mo_lmqEecawiM_5Y34AzI4LsUfMth9GU1RS1Dl-LSSiYhWlMpKOWFqRdxzNjLeTo69citgGGMh9wHybDeOlP3y8UJEP-vZMXB5AbxD-n70y5JTl52gWjY9bMFMVGplkOI6qFZe2vM800dxJ3oRH3kVG3SIWUne2WwcoOZx7bqp3CNBGDT_jttWrLahWP-xuJSTC7sCutEGYbJSCBXlw7DlzItZQaoAZOVLMTjGOKxuqsth3Otmr3o0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمد سامتینگ: قاعده بازی عوض شده و دوران پاسخ متناسب به پایان رسیده است
رئیس مجلس شورای اسلامی روز یکشنبه ۱۵ شهریور، یک روز پس از حمله آمریکا به چند نفتکش ایرانی در خلیج فارس، گفت دوران «پاسخ‌های متناسب» به پایان رسیده است. او همزمان به وجود مشکلات اقتصادی در کشور اذعان کرد.
محمدباقر قالیباف در سخنانی در جلسه علنی مجلس تهدید کرد: «هرگونه تجاوز به منافع و امنیت ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر دریافت خواهد کرد.»
قالیباف که مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوهای بعد از آتش‌بس با آمریکا است، در بخش دیگری از نطق روز یکشنبه گفت: «نوسانات شدید قیمت ارز، تورم، بیکاری و مدیریت بازار، چالش‌های اساسی هستند که به معیشت مردم فشار جدی وارد کرده است.»
او افزود: «در کنار میدان نظامی، امروز اصلی‌ترین نبرد ما در میدان تولید و معیشت مردم است.»
این سخنان یک روز بعد از آن است که قیمت دلار در بازار آزاد ایران تا مرز ۲۲۸ هزار تومان بالا رفت و از سوی دیگر آمارهای رسمی نیز نشان‌گر افزایش شدید تورم در ماه‌های اخیر است.
علی مدنی‌زاده، وزیر اقتصاد ایران، نیز روز یکشنبه گفت واکنش تهران در برابر تشدید فشارهای اقتصادی آمریکا «مقاومت اقتصادی در کنار اصلاحات اقتصادی» است و این دیدگاه را که تحریم‌ها باعث تغییر مسیر ایران خواهند شد، رد کرد.
او با اشاره به اظهارات مقام‌های ارشد دولت دونالد ترامپ درباره اقدام آمریکا برای قطع رابطه ایران با اقتصاد جهانی گفت: «تصور اینکه بتوان با فشار بر اقتصاد ایران، تصمیمات یک ملت را تغییر داد، اشتباه است.»
وزیر اقتصاد ایران افزود: «مسئولیت اصلاح اقتصاد ایران بر عهده دولت و مردم ایران است، نه وزارت خزانه‌داری آمریکا.»
این در حالی است که همزمان وزیر خزانه‌داری آمریکا اعلام کرد ترکیب محاصره دریایی و تحریم‌های گسترده، صادرات نفت و دسترسی جمهوری اسلامی ایران به درآمدهای آن را به‌شدت محدود کرده است.
اسکات بسنت در گفت‌وگو با شبکه فاکس‌نیوز که روز یکشنبه منتشر شد، با اشاره به نقش چین به‌عنوان خریدار اصلی نفت ایران گفت محاصره دریایی مانع خروج محموله‌های تازه شده و برآورد کرد که «احتمالاً تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز نخریده است».
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/145914" target="_blank">📅 17:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145913">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRvLjwejvuYLLgir_3PGR_8gxwnAftBGfaDWFfEM9VC_d_qtPOk23kiDEr4RiDhNPIMFYkKPF-T3xxcTlVbhGf06w4FmKZjMSbx3aiHtSL8apED964r0yc-r9WDbLH7sSWrKhznfTcW5a00hoIuRUIj9konBXP037GTMlL40nwAmf12BWxMBOv7oj50n0NmRT26mo_kRZWH1ZAzr-KS9nxPww14rmdbVFLRSbBFTczfZmsdlb_s-b3WPULi_6upMptFLHfIh17bc4Q4suWfWqPK0ToQn163LrEkxWHLGzXvYBGBzPwN7Axabwan2IEz0dMH-b1pJE-wWnw94MPwtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
فیاض، استاد دانشگاه‌تهران: تو خیلی چیزا از آلمان و اتریش پیشرفته تریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/145913" target="_blank">📅 17:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145912">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
طلای ۱۸ عیار 23,504,800 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145912" target="_blank">📅 17:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145911">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏
👈
دبیر انجمن فرآورده های دامی:
به علت گرونی نرخ ارز، قیمت سوسیس و کالباس افزایش پیدا خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/145911" target="_blank">📅 17:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145910">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: سطح ترانزیت نفت از طریق تنگه هرمز به طور متوسط ​​روزانه 9 میلیون بشکه نفت است.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/145910" target="_blank">📅 16:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145909">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پژو ۲۰۷ اتومات ناقابل ۳ میلیارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145909" target="_blank">📅 16:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145908">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏
👈
سی‌ان‌ان گزارش داد:
نیرو های تحت حمایت عربستان در یمن پس از درگیری‌های شدید با نیرو های حوثی،
وارد حومه شمالی شهر حیس در جنوب بندر استراتژیک الحدیده شدند و آن را تصرف کردند.
🔴
نیرو های تحت حمایت عربستان و امارات در حال پیشروی به سمت بندر استراتژیک الحدیده در سواحل دریای سرخ می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145908" target="_blank">📅 16:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145907">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14170fc93.mp4?token=hH5ADymoIF2JedOKO5bJdJokeI80uwXUaHeaqMsoRawp8DzPBSZRGUoUjCmXS_BS-y0O4Mpq40dDKUMw1tzutInlFrl4KfTGmuGu0IBg0rBWYgrDg-reagQSntwLtp2aQzN_cCEg0rtP-KSOuO1WI_fwH6UXwT4nigA8_YtN0kh38-wyXUMP72xukDv46QsCRE_QdpnvqsgFN4pGb_hAW4hnENUTF2zjHthRMMiIrTsUZ6I2BwyJeYzqnNqH8zBIBkBhKRS-ZAHtgr06675mywqXvXJjt1ZfTGxquSq7XmaaUOfUKEaUZ9Gmm99ND_-hnM4jXZJTs9KYE89EtHTQSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14170fc93.mp4?token=hH5ADymoIF2JedOKO5bJdJokeI80uwXUaHeaqMsoRawp8DzPBSZRGUoUjCmXS_BS-y0O4Mpq40dDKUMw1tzutInlFrl4KfTGmuGu0IBg0rBWYgrDg-reagQSntwLtp2aQzN_cCEg0rtP-KSOuO1WI_fwH6UXwT4nigA8_YtN0kh38-wyXUMP72xukDv46QsCRE_QdpnvqsgFN4pGb_hAW4hnENUTF2zjHthRMMiIrTsUZ6I2BwyJeYzqnNqH8zBIBkBhKRS-ZAHtgr06675mywqXvXJjt1ZfTGxquSq7XmaaUOfUKEaUZ9Gmm99ND_-hnM4jXZJTs9KYE89EtHTQSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی دست هر پسربچه ای یه چاقو هست و هیچ برخوردی هم باهاش نمیشه واضحه که آخرش به اینجا میرسه...
کشته شدن پسربچه ۱۵ ساله توسط یه پسر دیگه با ضربه چاقو به شاهرگ
📵
هشدار محتوای حساس
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145907" target="_blank">📅 16:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145906">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eer0Rk0q7Pk18s1X4SrFlgOsyLhDlnPKSRGuNnNI0a9c1ZMlIeHPjKoWrTBCxQBXRHB2dQalPP_Bfxp7MZ6s2yu4BTFJjxEdAIWdPtMqs4ae0d26jUbY_9WSZvipu6kwdP7QMyxgDjBNYvdo5IYDysNXGPxSWsLcpPacEr6ldoguNKzwDkM8m9l16qHMTh98XWE-00frtXe_SLox7jKtp9Y3HWJ5AY0p-69FP7VAwc8J3A6zoQFoyDrah-ri0Lw2xPIIJB59YMQynB_hvKLPXSd6KI23PrRSwGmWXfG34ulUQZymox3QO49Ti78XgCb4dqmfj79S5WEHzxqweKvdIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منچ‌اوسینت: از صبح امروز دست‌کم ۳ نفتکش هنگام تردد در «مسیر عمانی» تنگه هرمز، پس از هشدار نیروی دریایی سپاه درباره بسته بودن این مسیر، تغییر مسیر داده و برگشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145906" target="_blank">📅 16:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145905">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">وضعیت جوریه که اگه بگی گرونی شده، به جرم تبلیغ علیه نظام میگیرنت
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/145905" target="_blank">📅 16:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145904">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d924e78a9.mp4?token=nU_I0cc5zrAe3meViHb3J3ZwMSwm_cqe05F7p5Fm9Jmwy_TBoiz6W6jhqTjGWozxNiXQHn-y2RFL8oAp0UDVYqmeggTbOhKypyNNzc9i7HtR1biReADszfOknUSFrQwRYBDFLn9SFhQddsJHdCe90y7HPKw4JN6LsbNi-fUqLHNnoSHEXuVmZuKochyYC7bFz6WvdMAU08MKtESf7zhCEgedGJQGxI-jK3EXhAihpT5u_edv-BhUjEJoMfnBrkiGxBedNBspPnRnSAY7u93HBDwPPji20HjayOkFPD6pQKAA_QwBA4o4kRYB28bnrfNzlR4eG3nRwFYiCboFNUAN3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d924e78a9.mp4?token=nU_I0cc5zrAe3meViHb3J3ZwMSwm_cqe05F7p5Fm9Jmwy_TBoiz6W6jhqTjGWozxNiXQHn-y2RFL8oAp0UDVYqmeggTbOhKypyNNzc9i7HtR1biReADszfOknUSFrQwRYBDFLn9SFhQddsJHdCe90y7HPKw4JN6LsbNi-fUqLHNnoSHEXuVmZuKochyYC7bFz6WvdMAU08MKtESf7zhCEgedGJQGxI-jK3EXhAihpT5u_edv-BhUjEJoMfnBrkiGxBedNBspPnRnSAY7u93HBDwPPji20HjayOkFPD6pQKAA_QwBA4o4kRYB28bnrfNzlR4eG3nRwFYiCboFNUAN3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گویا شخصی که تو یه ویدیو گفته بود دوتا سیب زمینی شده ۱۰۰هزار تومن، دستگیر شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/145904" target="_blank">📅 16:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145903">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEqSqaxwpZ0tRT2mHsu3Nns4MoqmtLWXM1fl7_7syDfzlZbt2DbhsQ9ZCwnuIszxzIDhMb9cG4sEkAEajx3PVHhsw36Zi0Iqya6L99g62JiI_A4yODrY7bTO9zeW7oRNWHtM2geCsNCrVtJxAjKZNmSg9ztD0fm7JDFd1_ikH71rpKLABsr1lIt3K8APfK9qXwx6U-BadcmI0Bwdb17Xb5GyM0vCQZQpqrbcLWIZkq9W1uekWjIBpHP-c3KOK4tk0gyEfXcDfCRsY0qKF28FSWRRJutmy07Vc9R9dh1tgx0fHjvVJZrpLEpoH4xAqKlCMKRUdvP1GR7a602be5W8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهریاری نماینده مجلس: اینکه ترامپ گفته بیایید از پول‌های بلوکه شده بهتون دارو و غذا بدیم غلط اضافه هست ما فقط نقد میخوایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145903" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145902">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رئیس ستاد ارتش اسرائیل: اوضاع از چندین جهت بی‌ثبات است و ما در ایام اعیاد یهودی در آماده‌باش کامل هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/145902" target="_blank">📅 15:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145901">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjMA1EyT7fcV58286LSwlbM3rfXPrpzFA3vaftalBBIKaZv6U_m9T_nEu4gpNa710EDUyEFoCfIJaPFK6--rKuWOR5r5oV5Yyr4IWrn3JNBcrh5BGSssSwqO-swNyULRAmgAkat8d4Gtkdje3J1EcGgeRdSg8twJTG7rr7SC2ytpHik9FNWbUCpNjO1O6yfKj8Bh0UZ5WmkMn8hS_ym-z-58KmHehugSYQWi7zjVvThie4PQNfQilTyy_7NRG7mxoGYVJS1aPbNEtc9uq8A3cn2yZ0N7tGGmpL_lB7VvVlPG5BIz6fSKXMCtzuNQjobft9OnfyCnSyMOITUFRQLgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت جوری شده که حتی عوستاد هم نمیتونه تحلیلش کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145901" target="_blank">📅 15:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145899">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
اردستانی، نماینده مجلس: جنگ طولانی شه ممکنه ترامپ بمب اتم بزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145899" target="_blank">📅 15:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145898">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سنتکام: ۹۲ کشتی تجاری را از مسیر ایران منحرف کرده‌ایم
🔴
ستاد فرماندهی مرکزی آمریکا اعلام کرده از زمان ازسرگیری محاصره دریایی ایران، ۹۲ کشتی تجاری را از مسیر خود منحرف کرده است.
🔴
سنتکام همچنین مدعی شده در همین بازه ۳ کشتی را از کار انداخته و ۲ کشتی دیگر را بازرسی کرده است.
🔴
این آمار نشان می‌دهد فشار دریایی آمریکا بر تردد تجاری مرتبط با ایران همچنان در سطح بالایی ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145898" target="_blank">📅 15:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145897">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/145897" target="_blank">📅 15:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145896">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvraHzLeRlO3dbV93Z1w5-3p2GKPpMq_SEAKAPYCc5BFRNjwpYFwXWfPHOVqYaYRPnlYP7kxZAUzHINDUBr16capGNvU381beacErPufSSZLflrolCMCvvJEfHQPo4z2Lyea_JP8Umak8ZMmdCwQDQsPZ3xKi-MEqxmvvRjkILljEo6AKGUrvSXy6QP6ufMlsgYZB8qEh9CYjjvH10JyDGzkYVj3wYu9_o9UnCzyJJLMyeJilmRudlbERxvUwqOy8DYQFFhbTctOUkxL62DbMRqp4S0rHBftPyOpPEljhyc7q2tlOCwQeFitE-gU0ksui4b8Nh9WjLhynAHQZDeXsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت جوری شده که حتی استاد هم نمیتونه تحلیلش کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/145896" target="_blank">📅 15:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145895">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004a973a40.mp4?token=E-UleUUL_5OtUXSGow6UEG5hBdtjVl1ZMK5iIhNTGCBMIVE5od_6K8aPXzWRYAMsfz52gZhW3jwR9ksgR7bVYoAjU7Q2OmOJZgLl_0WrQPPk7j3WTBCbV_TYReq-MyHR4xZFgaafm1ZCGWZsk7sdqO7MfZsVgZ3ZCzgh7nsxsd6GMyWxvRfOwAs8NS_0Yq62L-3e_fN2sklD67o1zmO6QmBPpZ40r8T42nVOj3q9AEd3ViB8W_WJYRsVCU8YQJsu81R7JS_KUNWzgsl6X0qifuOTIZP-Z8-uLOHhtZb8lKDCewe-IGGcsLJE82SQAUvQFE6VBK4E6abNRaOEb7OqlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004a973a40.mp4?token=E-UleUUL_5OtUXSGow6UEG5hBdtjVl1ZMK5iIhNTGCBMIVE5od_6K8aPXzWRYAMsfz52gZhW3jwR9ksgR7bVYoAjU7Q2OmOJZgLl_0WrQPPk7j3WTBCbV_TYReq-MyHR4xZFgaafm1ZCGWZsk7sdqO7MfZsVgZ3ZCzgh7nsxsd6GMyWxvRfOwAs8NS_0Yq62L-3e_fN2sklD67o1zmO6QmBPpZ40r8T42nVOj3q9AEd3ViB8W_WJYRsVCU8YQJsu81R7JS_KUNWzgsl6X0qifuOTIZP-Z8-uLOHhtZb8lKDCewe-IGGcsLJE82SQAUvQFE6VBK4E6abNRaOEb7OqlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طبق قانون، استیکر و گیف خنده داری که از رفیقت میسازی جرمه و میتونه ازتون شکایت کنه و تا 1 سال حبس و 5 تا 33 میلیون جریمه نقدی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145895" target="_blank">📅 15:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145894">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
قالیباف: حملات ما به پایگاه‌های آمریکا تنها یک آغاز بود، قوانین بازی تغییر کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145894" target="_blank">📅 15:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145893">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiW4WRYVnKS6wHnQYKwJJffJt4ekzL2EqIfOTmo4AkpQNmmrku3tzt10U_MEeWmYJ87c_fqLM4fu6jKUFKMOfqPNoiDEEuni866RyR0TAvQYHTwDRenMIPsYIMtKdnJ4w_O553c3QbSiqJ4wNAMhyEC2IufpLbuDbI9EEmUqekSUtqzl9X9WK2qPacfwN7v-tIZPbbBHrbR2_Spqq7y9oXlK-lpe4Bsi93RbBN8FTcz0iqzspPdIeBx-WdnlNqmwYufVdJKGCQM9l3quBtbvbP_iOqc_Fy8XKPx0B-r4lPQlAPxVolhJvj4PKMRDTIn_wllxCxI5yC9TW8PF2lTSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست: ایران در حال برنامه‌ریزی برای حمله‌ای جدید و گسترده به اسرائیل، مشابه حمله ۷ اکتبر، با هماهنگی گروه‌های نیابتی خودشه. بر اساس این گزارش، ارزیابی‌های اطلاعاتی اسرائیل مدعی شده جمهوری اسلامی قصد داره حمله‌ای چندجبهه‌ای رو با مشارکت حزب‌الله لبنان، حوثی‌های یمن و شبه‌نظامیان عراقی انجام بده. همچنین ادعا شده سپاه در حال برگزاری نشست‌های برنامه‌ریزی و تمرین‌های مشترک با این گروه‌هاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145893" target="_blank">📅 15:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145892">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797b887a7d.mp4?token=W2ioDeq6ActEeo4eZz7q9nFEg25eu_YmTPQ3j6aLxPN6tAAWgmFY1_TsFhPWUZLj9MaQQb1szfI4Cq6oqkZrygSyKwoMU7zVxGGVK7eoPZF5W8q7wbIAgFySeiFHaqmM02gQBVDKMJvZO_0ngtqHLt_qf8dONeoF_fc6fSQVQKT1NMk8HXSrWfZyyxcPezBSgjnuGmgQfMzRI_-tz3XRviSrOMpc65bDxiQqc7VeG-73_EbTI2BNXzslcV6BGJOUGrUQigYQYrp9Ph4J6cEKd8q62x1jxKCOQLvi-qgAG2g4hskt7xLIabcykyHVgl-j7UbxCjfpllz0r9h78PFAbJ9WzeBrq6OB-62Z_Wt2ncLTrqvVBY03ughMYAafghoLtSgHpDsPWeXCYlSMwrrRdXxUQq32reo9yLVcQ78ATVBD-bI9jdibcv4U3JsclxAs0drTRyJfHku7wfCtghJNedkkqfD5QEsRC5iD0yL6b_xF8oGfvJgXXXO1wOnz-nL7P7qwMSfz4K2b556g-TgCHzovg9ojo5X_sroChBz61veV5i2lP3aSjhWjV6VC6y7EAXLRHg39lcQ7zBwYclR0iBGr3A-L8L8KTnBu4IF0o33_i8ytL1Y1mwjrMNzualH6ZOaGO-bVYIA2OxY3pm91t3PGzLZex0xDNoCMYmnEm8Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797b887a7d.mp4?token=W2ioDeq6ActEeo4eZz7q9nFEg25eu_YmTPQ3j6aLxPN6tAAWgmFY1_TsFhPWUZLj9MaQQb1szfI4Cq6oqkZrygSyKwoMU7zVxGGVK7eoPZF5W8q7wbIAgFySeiFHaqmM02gQBVDKMJvZO_0ngtqHLt_qf8dONeoF_fc6fSQVQKT1NMk8HXSrWfZyyxcPezBSgjnuGmgQfMzRI_-tz3XRviSrOMpc65bDxiQqc7VeG-73_EbTI2BNXzslcV6BGJOUGrUQigYQYrp9Ph4J6cEKd8q62x1jxKCOQLvi-qgAG2g4hskt7xLIabcykyHVgl-j7UbxCjfpllz0r9h78PFAbJ9WzeBrq6OB-62Z_Wt2ncLTrqvVBY03ughMYAafghoLtSgHpDsPWeXCYlSMwrrRdXxUQq32reo9yLVcQ78ATVBD-bI9jdibcv4U3JsclxAs0drTRyJfHku7wfCtghJNedkkqfD5QEsRC5iD0yL6b_xF8oGfvJgXXXO1wOnz-nL7P7qwMSfz4K2b556g-TgCHzovg9ojo5X_sroChBz61veV5i2lP3aSjhWjV6VC6y7EAXLRHg39lcQ7zBwYclR0iBGr3A-L8L8KTnBu4IF0o33_i8ytL1Y1mwjrMNzualH6ZOaGO-bVYIA2OxY3pm91t3PGzLZex0xDNoCMYmnEm8Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موبایل‌قاپ حرفه‌ای در شهرری به دام افتاد؛ اعتراف به ۱۰ فقره سرقت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/145892" target="_blank">📅 15:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145891">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OapCQI3tUD-2JMjKSEo9HrVvSh27k_Y7qcvJ9MRlXxnP-iRMDpIYdOR32pCD9eBnaGSAg0svFLBgtFx7diewftYB0igg-IdhmwML4a5bHxVFnK_9tyIUg4NwZuOy2ISI23L3bA_kLZCECHEm6dKFnozdUICQuZwYlVtBrTO8kIm8liLdbZ0cvmiEt1e-iti6-vd7TTOd-VFKoMkHno9ZhCQmFRALPQsEAegmRPxuF1HRtUsZZbgis5fBJbys10KI9zCxltJy5Ptc6gZnmK447dtu5tZING1YmNSEWCt97XvmoomfXdT02mr2A4fAUV6zNy7jI42nuGCgx6ApHbAvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر اقتصاد امروز یکشنبه وارد مسکو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145891" target="_blank">📅 14:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145890">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
زلنسکی: «مذاکرات آغاز شده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145890" target="_blank">📅 14:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145889">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f92ebb79ed.mp4?token=cG5Rzq3edVFNrEoEfpFjr6ytsg6FkGLkfboJeASwCzAfsRjBo3ATi5e8blT1D5Duy1D8PSFB8MfafbO2rWz5sLParpKaDpvavfwm2-RuOSH4TYDivBubVdeq2jo1-m-MHLskL3A2djSscKlY4C3MmyAU-6dSR38fIQ5E1SOmPkwiPbFWZIVrvUzLrQBVdVeWAtCSDIO-X7qh54br0qti1VoNwXrmWGGqbxB2NIf28ONzzqcObkJbB4U13FVgd21ExmUwE_YSEtI0_3jyZ9p_B6uMhgXOFldgEpLw7E_mC0kFrPw7VoZFJjMenkQVRf4t9SFOECBNoRpKdFQx721zwGxik8gW2u6dk_zFEq0pVTLqlyz5eaPnu9t2xtVrEgVrGOZS-UhKgnyrnlezEl_VwLjkzIZdG3-bpPN_RyI6Ykd1T1_UDfqhoz7EJKg2_RrIR-uB3qcrJAKM385sKg1CXRGKJb9spJqoOWxLiT2Yf0TzMQevsbups2xjNqDSMJ-GK-QRJx64Pg9ayWzcrkOzLgWymiMzRrK4T8rCHZbzf32Ci4NN_tP-UIbA_SkezAsOSOk-CNGCadj5IZUoDXsYm7nEYcho6mkfzOdiddlzO658459uOwHJE5p9mI1tFOXiItnkTqs_fu94uYxZhgOjthpFzUWncCEecS3F9FPwozI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f92ebb79ed.mp4?token=cG5Rzq3edVFNrEoEfpFjr6ytsg6FkGLkfboJeASwCzAfsRjBo3ATi5e8blT1D5Duy1D8PSFB8MfafbO2rWz5sLParpKaDpvavfwm2-RuOSH4TYDivBubVdeq2jo1-m-MHLskL3A2djSscKlY4C3MmyAU-6dSR38fIQ5E1SOmPkwiPbFWZIVrvUzLrQBVdVeWAtCSDIO-X7qh54br0qti1VoNwXrmWGGqbxB2NIf28ONzzqcObkJbB4U13FVgd21ExmUwE_YSEtI0_3jyZ9p_B6uMhgXOFldgEpLw7E_mC0kFrPw7VoZFJjMenkQVRf4t9SFOECBNoRpKdFQx721zwGxik8gW2u6dk_zFEq0pVTLqlyz5eaPnu9t2xtVrEgVrGOZS-UhKgnyrnlezEl_VwLjkzIZdG3-bpPN_RyI6Ykd1T1_UDfqhoz7EJKg2_RrIR-uB3qcrJAKM385sKg1CXRGKJb9spJqoOWxLiT2Yf0TzMQevsbups2xjNqDSMJ-GK-QRJx64Pg9ayWzcrkOzLgWymiMzRrK4T8rCHZbzf32Ci4NN_tP-UIbA_SkezAsOSOk-CNGCadj5IZUoDXsYm7nEYcho6mkfzOdiddlzO658459uOwHJE5p9mI1tFOXiItnkTqs_fu94uYxZhgOjthpFzUWncCEecS3F9FPwozI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: من مدافع طرح نفوذ هستم اما نمی‌شود کشور را قفل کنیم و بگوییم همه از ما اجازه بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/145889" target="_blank">📅 14:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145888">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68141df3da.mp4?token=dJxBz2-tupj_IXGisT85iNtTSLg6wwFXd-ncsEp2q5UUrvJQwNbDX2pJ90wqOvKWwR8h0rGBcN9fpgXZHQvQxx0qPTpZzTzrA5DY4uL3tB66VBSSU1aOWlP5oAaqsPuJFiDgye3j4c5IxLxcWt2EkiLa2DUSCebYGt5ZE0ocLDvuDUXo0aP-b4rcPkojc7oFRyhv_nLZwBQwMDl0SKJj_sK5vPv6Buz8Bylk6LH3LcFs6m9hZKXi8kI9taf6biQ9oZs6_8JV9uoPX0Ci5wluRcfTtWtEJehASTbyjt33Yirnz6XdF6dGf0fQ9wEoC0qXpYFfJCEkvPa07DZy-wPtRbQY8-0dQ0s2cpMBYrNWq4eCGcA2ZvVAeayrMC8iKJU3BzKuU6hVTl1ktoQytOxT3qdfJZU1dGbTeLToIypOpdgWQRRPyaaJFAnQuR_S42R27OWPgrMd-Kk2WcRWneCGN8O4fBifr1SvQfWHggR38EnVXT_eDE17l1pmTovSVvNn1uWjlwdI3hpV4jjX2LbOkf0efzNaO-5yVH4MVbiZp53vsARHXnC-Js9L6XOZfmoHFKnjas_jLczZvAgEdBDL-wcbuC28TCtUqvxvtgtxL7SO0YNDI975MnanZrnLYPNH2L5NXMm-tjypX3eBg6gg_37epeYLztUD-xVb-5uoLfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68141df3da.mp4?token=dJxBz2-tupj_IXGisT85iNtTSLg6wwFXd-ncsEp2q5UUrvJQwNbDX2pJ90wqOvKWwR8h0rGBcN9fpgXZHQvQxx0qPTpZzTzrA5DY4uL3tB66VBSSU1aOWlP5oAaqsPuJFiDgye3j4c5IxLxcWt2EkiLa2DUSCebYGt5ZE0ocLDvuDUXo0aP-b4rcPkojc7oFRyhv_nLZwBQwMDl0SKJj_sK5vPv6Buz8Bylk6LH3LcFs6m9hZKXi8kI9taf6biQ9oZs6_8JV9uoPX0Ci5wluRcfTtWtEJehASTbyjt33Yirnz6XdF6dGf0fQ9wEoC0qXpYFfJCEkvPa07DZy-wPtRbQY8-0dQ0s2cpMBYrNWq4eCGcA2ZvVAeayrMC8iKJU3BzKuU6hVTl1ktoQytOxT3qdfJZU1dGbTeLToIypOpdgWQRRPyaaJFAnQuR_S42R27OWPgrMd-Kk2WcRWneCGN8O4fBifr1SvQfWHggR38EnVXT_eDE17l1pmTovSVvNn1uWjlwdI3hpV4jjX2LbOkf0efzNaO-5yVH4MVbiZp53vsARHXnC-Js9L6XOZfmoHFKnjas_jLczZvAgEdBDL-wcbuC28TCtUqvxvtgtxL7SO0YNDI975MnanZrnLYPNH2L5NXMm-tjypX3eBg6gg_37epeYLztUD-xVb-5uoLfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اخیراً تماس هایی از مبداء نامشخص با مردم بومی جنوب کشور حاصل میشود و درخواست میکنند که طی درگیری های آتی هیچگونه حمایتی از سپاه نداشته باشند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145888" target="_blank">📅 14:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ضرغامی: جنتی به دلیل کهولت سن امکان ملاقات و حرف زدن ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145887" target="_blank">📅 14:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dce26d7459.mp4?token=TQAEl2QoFtJBWX40ml9RtQANhIWykyZB5pfUgXoyG7YmcSeWJJem1QYeEsNeI9BypiD5Sjdv33W4EnHnvzq1xo7HgJpTr9PstKWXR83rHWpRmb5Wjalt3p3gNExTVbk5nErlmff_8CykBgnWNvMzwrBYbBb02K3wEIXftH3RKSbySI1GsLx_sGssugM95rYBJ6TV9TiZqquakl3jdeU2Fq8CMUPzi4nw7ZmgJ8Sgm03-JBye4zLBDX1HPsZhFTK-GMnMZcyuv8RbvTbyYUj77GQPON9nPk_LHsSaFWEgkp2IOJA_0G_P00AwdzDLbcimVrBiyze40BU-T1Ln7of6lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dce26d7459.mp4?token=TQAEl2QoFtJBWX40ml9RtQANhIWykyZB5pfUgXoyG7YmcSeWJJem1QYeEsNeI9BypiD5Sjdv33W4EnHnvzq1xo7HgJpTr9PstKWXR83rHWpRmb5Wjalt3p3gNExTVbk5nErlmff_8CykBgnWNvMzwrBYbBb02K3wEIXftH3RKSbySI1GsLx_sGssugM95rYBJ6TV9TiZqquakl3jdeU2Fq8CMUPzi4nw7ZmgJ8Sgm03-JBye4zLBDX1HPsZhFTK-GMnMZcyuv8RbvTbyYUj77GQPON9nPk_LHsSaFWEgkp2IOJA_0G_P00AwdzDLbcimVrBiyze40BU-T1Ln7of6lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: روسیه اجازه نداد هیئت آمریکایی با هواپیما وارد اوکراین شود
🔴
ولودیمیر زلنسکی گفت: «روسیه اجازه نداد هیئت آمریکایی با هواپیما وارد اوکراین شود، با وجود اینکه فرودگاه‌های ما برای ورود آن‌ها آماده بودند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145886" target="_blank">📅 14:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145885">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
فارس: دلار ریخت و به ۲۲۴ هزارتومن برگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145885" target="_blank">📅 14:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145884">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0192c9a24b.mp4?token=hFH64UWOHvr_a5scfctQjPKImnfHgjBg7_95bhRCtMrcHa9jOR-g-N_d_OzzdbeqSC93VlWwKRxlviwlsxDCqvPFk5mKDGHUM1EHMZU4myId44qTCDt9sEXEuSL17qgNWNziQq99lc6Qvd7WXT-nAQi2B4EGHiS42EJCfI7laMcrcY11ZLQyvDxQpubakcej7CZLtLflyxMJ9_m8FlNNeU37687aQADiA0iVthDqJr8GH9pm596_xvR7O7xn-VFyYfs5IjP_fmKN-26XYKZ7thfCSSlsnVO7BqQj_IffV9atiR4RCPN_2nCYCsGW85sNMextW15Ts_1Zw9PoRkA7Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0192c9a24b.mp4?token=hFH64UWOHvr_a5scfctQjPKImnfHgjBg7_95bhRCtMrcHa9jOR-g-N_d_OzzdbeqSC93VlWwKRxlviwlsxDCqvPFk5mKDGHUM1EHMZU4myId44qTCDt9sEXEuSL17qgNWNziQq99lc6Qvd7WXT-nAQi2B4EGHiS42EJCfI7laMcrcY11ZLQyvDxQpubakcej7CZLtLflyxMJ9_m8FlNNeU37687aQADiA0iVthDqJr8GH9pm596_xvR7O7xn-VFyYfs5IjP_fmKN-26XYKZ7thfCSSlsnVO7BqQj_IffV9atiR4RCPN_2nCYCsGW85sNMextW15Ts_1Zw9PoRkA7Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فریدریش مرتس، صدراعظم آلمان:
«برخی می‌گویند: پس بالاخره حمایت از اوکراین را متوقف کنید تا شاید در برابر تهدیدهایی مانند آنچه در فرودگاه لایپزیگ رخ داد، امنیت بیشتری داشته باشیم.
🔴
چه ساده‌لوحی‌ای! چه ساده‌لوحی‌ای!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145884" target="_blank">📅 14:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145883">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97d6b0d35c.mp4?token=l2Q-sMewJ12-OnRYYC9c6lxc4RzQRj8k9A-9iPnRUYHUsHB-v_f-0w70EEcWpkDOCGr-NF7PJGqEAcjmZvjpLQRQqWbDUfpKPS0YoIJrD3C8mLWVfrt4GLY9UDfW9R5V88kBLCndOCSFOHHEFmO_RmJCEVFSiKVDFnI3uyYw1go1TOIU_cl9OBAhy8w8ZeSa_4gR_zuAjQ_JVPJ5n48jORRDtuolD-hWB4BcXiXey6DZOn37JrFmvHlF_N3K2UGPQ89BItycdaJuw_gvJroPyY_tsdqF_wnsZOhfyZEW1K3ZH-Hao4jlCGHphk38sKggy5r2wddJaHpL9Vo2I6ODZACibED8tCibDrpr7lUoWXmekvYQ3QhiDsA3UAEyxboCKQbp5oEv4QS0f9LqjxXiNobr6zVSD2VGpBA1XG_QV-y9IW6mZKYKvo4yJtvV4KL08zmgeJAAFH_gsJ5YWKZaFQWUm6dGtIlSXfQnfqYyu1_K20T_lvE9O2oV-OuJWeJw90joHbmgkU_B32vGxbeXITxBy6FHE3DNFc-vab-M0qgutiMuokdGIpEsBgwA4wyrjaqVlTkUSLRDmlQlJvEAjzcWk5HD224CB8R6GRgKos9vuw29T-SHF2IWfyl5YG6xQv3TOS03a0OElQQkbtllZAc00iMs2DtbQuVLVKyAZBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97d6b0d35c.mp4?token=l2Q-sMewJ12-OnRYYC9c6lxc4RzQRj8k9A-9iPnRUYHUsHB-v_f-0w70EEcWpkDOCGr-NF7PJGqEAcjmZvjpLQRQqWbDUfpKPS0YoIJrD3C8mLWVfrt4GLY9UDfW9R5V88kBLCndOCSFOHHEFmO_RmJCEVFSiKVDFnI3uyYw1go1TOIU_cl9OBAhy8w8ZeSa_4gR_zuAjQ_JVPJ5n48jORRDtuolD-hWB4BcXiXey6DZOn37JrFmvHlF_N3K2UGPQ89BItycdaJuw_gvJroPyY_tsdqF_wnsZOhfyZEW1K3ZH-Hao4jlCGHphk38sKggy5r2wddJaHpL9Vo2I6ODZACibED8tCibDrpr7lUoWXmekvYQ3QhiDsA3UAEyxboCKQbp5oEv4QS0f9LqjxXiNobr6zVSD2VGpBA1XG_QV-y9IW6mZKYKvo4yJtvV4KL08zmgeJAAFH_gsJ5YWKZaFQWUm6dGtIlSXfQnfqYyu1_K20T_lvE9O2oV-OuJWeJw90joHbmgkU_B32vGxbeXITxBy6FHE3DNFc-vab-M0qgutiMuokdGIpEsBgwA4wyrjaqVlTkUSLRDmlQlJvEAjzcWk5HD224CB8R6GRgKos9vuw29T-SHF2IWfyl5YG6xQv3TOS03a0OElQQkbtllZAc00iMs2DtbQuVLVKyAZBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاسخ قالیباف به نقدعلی نماینده نزدیک به پایداری: شما نمی‌توانید برای من تصمیم بگیرید و من حتماً مثل شما سخن نمی‌گویم
🔴
ادبیات شما مناسب شرایطی که بر کشور حاکم است و همه حرف از وحدت و همدلی می‌زنیم نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145883" target="_blank">📅 14:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145882">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
فریدریش مرتس، صدراعظم آلمان:
«در فرودگاه لایپزیگ تا یک قدمی وقوع یک فاجعه پیش رفتیم.
🔴
واقعاً خوش‌شانس بودیم که آن روز این اتفاق رخ نداد. این پهپاد حامل مواد منفجره تنها به‌دلیل یک اتفاق کوچک، در آخرین مرحله نزدیک شدن به فرودگاه منفجر نشد.
🔴
اگر منفجر شده بود، آتش‌سوزی گسترده‌ای در فرودگاه لایپزیگ رخ می‌داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/145882" target="_blank">📅 14:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145880">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/alP_5h1WncLzGNOZ4Qgqi4eRYp2xPUXB-EXCKKXnzFEZKPhSgjFYq5h_uFppG8JhNynf1HORBH_fzX3o3qM2QW_Bda1g6APTeftXAk9ZpAVOSo3MKPWuT-oRFPH6RuUgUc_mXaP6d1kO1trpf44fGphl0hRCV-k9XEX-qUAw08MvzylQZxltgzWh7LBUuosiYlEc1X6YbacAKMEoS4uXKBsuHekxMGMo6ckNkY_X_aSNGtrPIuY9GxNX4B8bNGWmR23ta8WASjdejNjGxyXF-EvnN7YD4CIOkJ16Ks3HHS7JFrzcKEDXonr0KXSG34SfDWF1cRtpgbWwlIcWuxFdmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e_lGOLrlwjmANDECSX5adAecEz8rowWEkl69yVUx1rv1esLyNMq1jSj-RkgsZUCbpG2bfYgRs-GtjgtBNrXyrho-5ZqSvMrs5N2Ak-PKsTNevGaMzt4MbP7FmrqdinzmQkq3BwoOso79SQXBgHZQvVHFJlx_7_45thUQadzNwhqPSMZ4GdpkvKq-p_o5Jt_O2VlQWr8KiOt3yPXr9PjsGBvak7lpRtQQsw72c7vRrVj1RWPQTt5WM95LTL4j2w6y2nL_EYJNSohAmc2aNPOGvhgJ9kP0Xwz-Pnn7Rx4liDdfO20IRVW_2qOx17V0Lzl2mfsEzwxG70Nal2HlLPdqcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی  در شمال اردوگاه آوارگان الشاطی در غرب شهر غزه، حمله هوایی انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145880" target="_blank">📅 14:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145879">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8ed0a2e8.mp4?token=jWdFpdyq2lRX1Zvg2Eo8Oe48XPA02MkCzApTLOSfG94AkZP0AUciFdOHv9VQ2XQPnc6NYBG5X-OB79xLIKdaxCCR8vaIQFX8yuPlc90qJCzT4nPZZQQVeNhhaYtftrL9DMGJa77Uxyr-SD6aykutnXHHbjuP-ED-GGXiK1ByDt5tupJlUXfQFwbHOGjZhp7aIpg0OPDHEcFgsvAZ0n0qKfK9D_MHiJlSsAGnbIvotJozV1WKSTeB6bCV5878fBxq2bFrTmPtvMMy8ZB143cJES-qJicSXpvqh6oDrQX5JtQ8o0SYq1L6lQSaD4JcZdN_780P2HN_ZXLaeFngqI3Xkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8ed0a2e8.mp4?token=jWdFpdyq2lRX1Zvg2Eo8Oe48XPA02MkCzApTLOSfG94AkZP0AUciFdOHv9VQ2XQPnc6NYBG5X-OB79xLIKdaxCCR8vaIQFX8yuPlc90qJCzT4nPZZQQVeNhhaYtftrL9DMGJa77Uxyr-SD6aykutnXHHbjuP-ED-GGXiK1ByDt5tupJlUXfQFwbHOGjZhp7aIpg0OPDHEcFgsvAZ0n0qKfK9D_MHiJlSsAGnbIvotJozV1WKSTeB6bCV5878fBxq2bFrTmPtvMMy8ZB143cJES-qJicSXpvqh6oDrQX5JtQ8o0SYq1L6lQSaD4JcZdN_780P2HN_ZXLaeFngqI3Xkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر نیرو در پاسخ به اینکه چرا خاموشی‌ها ادامه دارد: یک خورده حوصله داشته باشید!
✅
@AloNew</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145879" target="_blank">📅 14:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145877">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUiG4HjhtWOSaONOuIzeltU8hb2LIqjv1HNhoCtioD2Ze5pFRXIHr7BBgCumHHTCLhWXGbjW4KtrrrOH4WOEPRc-f6BIWZ-Eg9Kx5-3tiIcbwPPCM4GwAVgL4JBz4vCV_2y15fMOrDWY5jDdEfheFUSc47W1N8rtjlQavtV8LxQbxw-_C2SP-sMJZH40Z9rfRAteT2773r8u-GI9zP49YWmYqhNGQHnJhD35jjm9Wk68M7zaWm3gKEWfVXwtF1_nlQt8FClVOrxbGKScmCJP1mQ6AhyS9Gm4lYMHdjUncRkaeSpJ_ybh-5hiMpPiWND_0hzNgKcvbp2vH-6WTDELQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qN_VwlSueMzdOorWlRDXMaJDhp0k0n13Xmf5epzeVYZ2qy8W1rrakwCLLJctq1Pg8r9UI-I6NIDel5Hyjb6EVe54oOO5ZPh5S2tyuakUmCBU3MOwD4_LUs8k8valyeMouv57xRKaeItBqpsZIXUIQI4z32-W6O_vjVuKsFvtpm-g4z6DxP10Aw0aK8YICdrfj7aCpYTUbLgxM4_VU90KweSX8e0RJuPWGVsOtHviFKeLVbdkO_pe7zV16eCPPQqLWPFhfwtgnHGno2CW9kZ_jsxWct7lOg6nuarN7xHoIUAWCrekil_EZZp02cBDAxOTl-s-QY1noRSfrYhctYbuMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
زلنسکی در کی‌یف با ویتکاف و کوشنر دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145877" target="_blank">📅 14:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145876">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
معاون اجرایی اندیشکده کوئینسی: شبکه «ایران اینترنشنال» در حال عادی‌سازی ایده حمله هسته‌ای به تهران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/145876" target="_blank">📅 13:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
هشدار تل آویو به اسرائیلی‌ها: فوراً اردن، مصر و قطر را ترک کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/145875" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
نیویورک‌تایمز به نقل از سنتکام : عبور کشتی‌ها از تنگه هرمز علی‌رغم حملات ایران ادامه دارد و شتاب آن رو به افزایش است.
🔴
ارتش آمریکا به عبور ۱۶۰۰ کشتی تجاری و ۸۰۰ میلیون بشکه نفت از تنگه هرمز کمک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145874" target="_blank">📅 13:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145873">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1b399eca.mp4?token=ldK3NcABxv4exjnZvaj3OeGhjlMIB4ISB3qX2z3YnjtdAXEQPOKEptW0yB3rcFjxZC8CPSo09ky6K2QNG_SmRgl0rV1EuD8TnYDS7lnil6ilb4F6HUFDNgus_eGgNcB4So5-CUMjZAfqAfJQ4_-lWRjab-wiE1ByJ_rUoRlYW9BU3xzwJNl-F5RelNcnhYbbRDb3Q021gC20koQQSE7ZsLzMqTLcNJalV02-En15bDDr2o8TV8t5JnIgfiNVIeSj8VkjvOaqpuVspSHwvHz04xqytJpwkxLbt0E0MqYnOnaiNrGEVaj7UH89idiKcCsnGy4sttVh0sqVjGaWL3TchA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1b399eca.mp4?token=ldK3NcABxv4exjnZvaj3OeGhjlMIB4ISB3qX2z3YnjtdAXEQPOKEptW0yB3rcFjxZC8CPSo09ky6K2QNG_SmRgl0rV1EuD8TnYDS7lnil6ilb4F6HUFDNgus_eGgNcB4So5-CUMjZAfqAfJQ4_-lWRjab-wiE1ByJ_rUoRlYW9BU3xzwJNl-F5RelNcnhYbbRDb3Q021gC20koQQSE7ZsLzMqTLcNJalV02-En15bDDr2o8TV8t5JnIgfiNVIeSj8VkjvOaqpuVspSHwvHz04xqytJpwkxLbt0E0MqYnOnaiNrGEVaj7UH89idiKcCsnGy4sttVh0sqVjGaWL3TchA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به علت افزایش قیمت موبایل، دزدی خیلی زیاد شده. زیر 5 ثانیه آیفون 13 یه دخترو دزدیدن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145873" target="_blank">📅 13:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145872">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3d01ae919.mp4?token=DnMCISJ9KzSVf_Miee3uYLJNjFw2tl4iSwO8p_IRRg1os7tM6Ws2Zuh3jkxNTAcmd3_HktSiDvlvu-ge2oOP1yT0jRB3hGI3s9MiUuB0DJfk5Qfu6l5DZVcu9yVOXldA5AONstTjI555NVW6md8MMkoqhj03H9VZjkrWaO0yYW0iX1SYRHWYeEQSJFHLaHDe7FZyHRvEzqKm08F4jYAfvjlOF-wuA4gukiDqnFzbFk8CpmlYBntDn9SgtU4y4nPINugoMzGTkqsKaZiVqyYdv6NYCRfDYkijffss7DaNRFKCnzj2tS68tuu1BTiTZqar3TDfjjuG3r8SYIgpg01gfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3d01ae919.mp4?token=DnMCISJ9KzSVf_Miee3uYLJNjFw2tl4iSwO8p_IRRg1os7tM6Ws2Zuh3jkxNTAcmd3_HktSiDvlvu-ge2oOP1yT0jRB3hGI3s9MiUuB0DJfk5Qfu6l5DZVcu9yVOXldA5AONstTjI555NVW6md8MMkoqhj03H9VZjkrWaO0yYW0iX1SYRHWYeEQSJFHLaHDe7FZyHRvEzqKm08F4jYAfvjlOF-wuA4gukiDqnFzbFk8CpmlYBntDn9SgtU4y4nPINugoMzGTkqsKaZiVqyYdv6NYCRfDYkijffss7DaNRFKCnzj2tS68tuu1BTiTZqar3TDfjjuG3r8SYIgpg01gfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زهران ممدانی، شهردار نیویورک، با امضای یک فرمان اجرایی، ۱۱ سپتامبر را به‌عنوان «روز رسمی یادبود و خدمت» در سراسر شهر اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145872" target="_blank">📅 13:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145871">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
معاون عمرانی استانداری سیستان‌ و بلوچستان:پروازهای فرودگاه کنارک از سرگرفته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145871" target="_blank">📅 13:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145870">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoZv01-YAPhTosSrA2M5WOYU4TCUu-EiwXzpIsNyrOZGdDROgitCXROm4PYoaKEpoo1KvG-r-SPDy-YHXHeBD2riK6XReX2BLa_gaWrCBADOHu3kQ0jIx_nrxy4zlOLZodkwhhaFCjFURq1ENrIVDbYi9FqODw01FXlpJ0Cw_UAA7A7nEd4hH5-uhNyPNpiadDg5xMi7p2o8IlESRSUK7mDKHkPhwgCjdSPiao-k2S1xYwWYE8TLPi0Z0T_FSTJ7BlobufTAix6hmZHb9hSPdQ8VHjaSaY8UAbFZacYaUrOY5VM639lv9mvZZviYbjCirI5WZERG3yjV84LsWAiA6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روغن موتور گران شد؛ افزایش ۳۰ تا ۴۰ درصدی قیمت‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145870" target="_blank">📅 13:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145869">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نیروی دریایی ایالات متحده اعلام کرد که ناو هواپیمابر یو اس اس لینکلن روز یکشنبه پس از یک سفر پنج روزه به بندر، تایلند را ترک کرد و توقف کوتاهی را در جریان یک مأموریت طولانی که شامل عملیات در خاورمیانه نیز می‌شد، به پایان رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145869" target="_blank">📅 13:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145868">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
قالیباف: همانطور که در عرصه نظامی و دیپلماتیک پیروز شدیم، در جنگ اقتصادی نیز آمریکا را شکست خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/145868" target="_blank">📅 13:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145867">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
این خانم ادعا می‌کند که در جزیره اپستین بوده
🔴
صحبت‌هایش در صداوسیما هم پخش شده است
🔴
وی ادعا کرده بود به کل جزیره تجاوز کرده اند و شرایط بدی موجود بوده است، البته خداروشکر طبق گفته خودش، ایشان مصون مانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145867" target="_blank">📅 12:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145866">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=dDXihYYJcmEuCd-cWATzTrF6513nMj3QLfPKg-ygPTPHOv3WzHS8JTL6jujEMPrMWr74yQms5uyqUt8jb43ZdGg6dtBCWjRRA69YXbnh8byiVHX1phNU8aZ-nZlS2FUbuaHddPxrmfP6FZPXob0hqVL_B1LuL154_I9YJZRa34hQr7NuPtI-_N4URgndaHdZIXsx5hg3VqhlDnTGmzRtRc-3gccZuNEL0-cPk_QLNFATxQB0fREVVKT6BWtxO1bu6S3_J220M5MeOzyZ-rt2GOv3ZuKxycrWNvtDYsECi0BepEVP58ZI0-2ITMok93Z21Y-e-GdE58kwXL0-OBxa5HyCDYpP6kg9LwGQNeo9JDi2zOlbopAXN2qWEifNKCbBw6lqdOzF6OxalRyOVt5ouSuB_JI0MDKyUxWoyVQXdrT3IOzCanNQwVmpntB98IFOvSbtqo63H1qBUGUogEyHc2Bi4cbcuhIUvm8TtnPJvF3YBTdkUcMA6B3zji_28hk6br70xzsyJ_eSprZe43EriirhjGdJE-vhJl9W8-lOnfy6UvaEFUwnqnz33ouHbj2C9BawjvZPSI1ypGPjldYel4sbJswk11k-mgOTeYZmM32jtdoYV9dpr9yD5KR4Sv-LIRfsSuZmZTaMSM6_vb9BSwwd_1HA8ZubOQt6OgA_dkE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=dDXihYYJcmEuCd-cWATzTrF6513nMj3QLfPKg-ygPTPHOv3WzHS8JTL6jujEMPrMWr74yQms5uyqUt8jb43ZdGg6dtBCWjRRA69YXbnh8byiVHX1phNU8aZ-nZlS2FUbuaHddPxrmfP6FZPXob0hqVL_B1LuL154_I9YJZRa34hQr7NuPtI-_N4URgndaHdZIXsx5hg3VqhlDnTGmzRtRc-3gccZuNEL0-cPk_QLNFATxQB0fREVVKT6BWtxO1bu6S3_J220M5MeOzyZ-rt2GOv3ZuKxycrWNvtDYsECi0BepEVP58ZI0-2ITMok93Z21Y-e-GdE58kwXL0-OBxa5HyCDYpP6kg9LwGQNeo9JDi2zOlbopAXN2qWEifNKCbBw6lqdOzF6OxalRyOVt5ouSuB_JI0MDKyUxWoyVQXdrT3IOzCanNQwVmpntB98IFOvSbtqo63H1qBUGUogEyHc2Bi4cbcuhIUvm8TtnPJvF3YBTdkUcMA6B3zji_28hk6br70xzsyJ_eSprZe43EriirhjGdJE-vhJl9W8-lOnfy6UvaEFUwnqnz33ouHbj2C9BawjvZPSI1ypGPjldYel4sbJswk11k-mgOTeYZmM32jtdoYV9dpr9yD5KR4Sv-LIRfsSuZmZTaMSM6_vb9BSwwd_1HA8ZubOQt6OgA_dkE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار محمودی بعد مصرف یک بَست: موشک رستاخیز ایران می‌تواند در لحظه اصابت ۸۰ کیلومتر مربع را نابود کند
(چیزی حدود کل شهر کرمانشاه)
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/145866" target="_blank">📅 12:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145865">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd83189492.mp4?token=szOI7nLGdUW64pjpkAEAqIW2SmwOnOMFhoDOfGeCtbFh1PFtE43d1dLWPez4ElcjfA8ATAGKoop3L1kPgAuVSox2yk1kwy35U-Vm33s11WdkTJNouyYtqxWgeSKmNXSz4ogw3zb5VNmAN-jgoxUxXjsVD55hJPvhyKdXcWmR-SXkwKAdmR7mNx96Ab7evAl3PnN9vJIBJaasCcu7kg9ZUjlGMg-z-QTAQIDQJkLohE0Vo4ZCjloo_EZN-CcMcP7Uk_x5g-g0u5DSVv2Al_kSDZgANVNHYibRNFroRHqlb3HJKf9e8O_inBwro67_z34zweWiALvaaF79yY0X2xmymA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd83189492.mp4?token=szOI7nLGdUW64pjpkAEAqIW2SmwOnOMFhoDOfGeCtbFh1PFtE43d1dLWPez4ElcjfA8ATAGKoop3L1kPgAuVSox2yk1kwy35U-Vm33s11WdkTJNouyYtqxWgeSKmNXSz4ogw3zb5VNmAN-jgoxUxXjsVD55hJPvhyKdXcWmR-SXkwKAdmR7mNx96Ab7evAl3PnN9vJIBJaasCcu7kg9ZUjlGMg-z-QTAQIDQJkLohE0Vo4ZCjloo_EZN-CcMcP7Uk_x5g-g0u5DSVv2Al_kSDZgANVNHYibRNFroRHqlb3HJKf9e8O_inBwro67_z34zweWiALvaaF79yY0X2xmymA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمید رسایی به پزشکیان: شما کارت دعوت بمباران عروسی سیریک را به آمریکا دادید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145865" target="_blank">📅 12:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145864">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
الجزیره: هدف قرار دادن ناو هواپیمابر و ناوشکن آمریکایی از سوی ایران، «تشدیدی بسیار مهم» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145864" target="_blank">📅 12:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145863">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
قالیباف: نوسانات شدید قیمت ارز، تورم، بیکاری و مدیریت بازار، چالش‌های اساسی هستند که به معیشتِ مردم فشار جدی وارد کرده و در سالی که توسط رهبر معظم انقلاب با عنوان «اقتصاد مقاومتی  در سایه‌ی  وحدت ملّی و امنیّت ملّی» نام گذاری شده،  باید با تکیه برتولید داخلی و استفاده ازظرفیتهای فناورانه‌ی نخبگان جوان، برای آن‌ها تدبیر  و راه‌حل کوتاه‌مدت و دائمی داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/145863" target="_blank">📅 12:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145862">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
قالیباف: آمریکایی‌ها حتماً فهمیده‌اند که دوران «پاسخ‌های متناسب» به پایان رسیده است/ هرگونه تجاوز به منافع و امنیت ایران، پاسخی «سریع‌تر،سنگین‌تر و دردناک‌تر» دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145862" target="_blank">📅 12:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145861">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630202ce50.mp4?token=NtiBiTqmKRDiZ3Do4SiqR3R7QMew9zjV6xl1zxoy26BpizDC5pTToXY-Ge-SyDNkg8yE1F7P9yQ_w2_8o5bLgNbZ56NLf3DZTOZLOL0g52QDc4jOqweLvcCnUPNxsm-oJyF_CH4tpGbjtcjJ-dSy1G6leimwDUbtdcZuD4ZvCoKbWlXGAPX8y6DEZgjXKXjWpu5pRI4Ihtn0VwC404n9rIEeRHfVenYis-8xuq_tnGiA5oncPj487Rgfxo9D89BhpWvhC8PbydGnHodpar9NShRTfMx2tMaxleCEwXvfX6dcL-iW9uFLs4ifAAOadd09kGBW3U0uiZyIEYPr6s9wBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630202ce50.mp4?token=NtiBiTqmKRDiZ3Do4SiqR3R7QMew9zjV6xl1zxoy26BpizDC5pTToXY-Ge-SyDNkg8yE1F7P9yQ_w2_8o5bLgNbZ56NLf3DZTOZLOL0g52QDc4jOqweLvcCnUPNxsm-oJyF_CH4tpGbjtcjJ-dSy1G6leimwDUbtdcZuD4ZvCoKbWlXGAPX8y6DEZgjXKXjWpu5pRI4Ihtn0VwC404n9rIEeRHfVenYis-8xuq_tnGiA5oncPj487Rgfxo9D89BhpWvhC8PbydGnHodpar9NShRTfMx2tMaxleCEwXvfX6dcL-iW9uFLs4ifAAOadd09kGBW3U0uiZyIEYPr6s9wBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی غیرقابل وصف یک آخوند از گرانی دلار و طلا در چهارراه ولیعصر تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145861" target="_blank">📅 12:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145860">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frs3vC2AbGkfh1IbRVPnrDWob499rn83YvLCrnkmuLEPvCWqe7F9xUN4c7colfs41MG_keQbpTOm17XLVFYUZxHg8j2G67nSx8gHnvdaJDr4MwEb9oHPJ8xXq86YIJztFM1bW4SC7JNyqfJB5iMpp4hkXJHHVHz9E_kyZeFFDZRU16W4Cg2CwCtE2l-LGpgpHxpZtlpAqBE3OH1Wzog4jDCPNy1OQ2fNACh3fyKUYT4a2I8rM_cti5VulaiJjZCSHupSxOgnwRjzly2YtRARMW0r4e54Jw0mMhhTv6Fl6DO-jQ-yidU4uXongyVA-4JaVKGdU_4tu2leuNYGRggnJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربی: نفتکش «ولوس امبر» (Velos Amber) یک ماه پیش موفق شد بدون مجوز سپاه پاسداران وارد تنگه هرمز شود؛ هرچند در جریان این عبور هدف یک پرتابه نیز قرار گرفت.
🔴
این نفتکش اکنون در تنگه هرمز گرفتار شده و اجازه خروج به آن داده نمی‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145860" target="_blank">📅 12:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145859">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
مشاور امنیتی نخست‌وزیر عراق در گفتگو با روداو اعلام کرد که ایالات متحده آمریکا تا پایان ماه سپتامبر، سامانه‌های دفاعی و نیروهای باقی‌مانده خود را از خاک عراق خارج می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145859" target="_blank">📅 11:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145858">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-bDYxq0yAhGuCU4ikiw7jvF5_b0Vd5Zzp-ICiNS75O8Oik9hsZgPDyps2G10VoD1JZ_N8c-K8X2WoMjutr9ykZ2232VMThNTjbT8fC49walQdhg36ZDGc38VQO11BnKsRqRDlO-eG6Z0Rsb3mgO7BI6rc7yx5nPOdNYfWqvUiNYC3z50o_qUpclYCfFO9ZTR3mNZ-Xys2Gv4oeQGMyBtoVMUOVI464GQMEBH3bXZIYvWcELRUtRGx2AR-HupeQulWkeWrP4FjE_yXTsq5eiiTjnTH0Uau4Kk8YiHXISi4-LGBFLBBkEWT2O-tv9eoINtsGoZC6dyiKEb95VrKmcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تجمع معلمان در اعتراض به وضعیت بد معیشتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/145858" target="_blank">📅 11:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145857">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر نیرو: تلاش می‌کنیم قطعی برق متوقف شود
🔴
با توجه به پایین‌ بودن میزان بارش‌ها از حد نرمال در برخی مناطق، مدیریت مصرف آب ضروری است.
🔴
شهر تهران تا حدودی با محدودیت منابع آب مواجه است.
🔴
امسال زمستان شرایط خاصی دارد.
🔴
در جریان جنگ آسیب‌هایی در حوزه سوخت، وارد شده که باید جبران شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145857" target="_blank">📅 11:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145856">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
مدیر سابق سیا: آمریکا شاید نیمی از موشک‌های رهگیر خود را در جنگ علیه ایران استفاده کرده و اکنون خواستار تغییر به سمت پهپادهای ارزان قیمت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145856" target="_blank">📅 11:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145855">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk05hlAtiV8e1uQ64Qh3g01cWOhidjOiv-l3dJIuye1nNLdTbgIKcQ-rmXt0atWk1J760Hr1PZmKukrot_l3T8maupjcJcAIOrkGMtMZI-Kr3cJdYO_D8PxnPKWKPMIsMNwn98V1Ub0G7VKqc1ofTI_vGLDme2ak31ifyhsTwy3-D2_xyFeGGOMJCoezgMWftFMWUVnT2CPNN2b4rj94RpXxZWLYxc_8yxMCm9BE7pFnZYMce08qWa8QLbi0rVmen5xT_RGxe3hD1hm0psJMhOk0g-fWVSb5YtoYQaVZuX3M5AJI6FFU9QpVFCL9SvaEk9Z4-oLZ67NpkKoPEYZjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وقتی وزیر با وزارت هماهنگ نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/145855" target="_blank">📅 11:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145854">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سخنگوی سپاه: هزینه محاصره اقتصادی برای آمریکا چندین برابر خسارتی است که به ایران وارد می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145854" target="_blank">📅 11:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145853">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
هم تنگه هرمز تقریبا باز شده هم حزب الله ترکیده، فقط مردم بدبخت ایران زیر سیاست‌های علی الاصولی شما در حال نابودی هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145853" target="_blank">📅 11:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145852">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل : تا زمان خلع سلاح حزب‌الله از منطقه امنیتی در لبنان خارج نخواهیم شد.
🔴
تسلط بر علی الطاهر به معنای تکمیل کنترل امنیتی بر جنوب لبنان است.
🔴
پیشروی نیروهای اسرائیلی به سمت «علی الطاهر» پس از دریافت اطلاعاتی مبنی‌بر وجود تونل‌های فرماندهی در این منطقه صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145852" target="_blank">📅 11:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145851">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8eeJnR8AXtOXzAGeGbag3G90V93vVyZlSLo8Rpr9SFsfC5O-MlAl5QcDYR_zGTZni2hWb6Bsrz-sWNyCnH0Rox3Imt_zJjBer2WVO7p8MwUVeabXpizaZKQQPL8rKf5qlCTfc5ZFikEuYBYgfzgj0O_vFKzXDtFGt5Alyga9li9n3KKIk61Iwn4qTh5yGIWGnitraTzyyCoRJZvYSlctm97VJGl2TL_4A_WKIz-QGFnHklh3XLKFsObqrCLAY32MQiFstSRlmKSXe-c1ZSnA6Rujsj-EvL8JfakPI1X8Lff4XPTboJWEDKYg1cr1IQy32Ll7MyIeZSx3JBG9urYjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاتس: تا خلع سلاح حزب‌الله از منطقه امنیتی لبنان خارج نمی‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145851" target="_blank">📅 11:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145850">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مصر و پاکستان بر اهمیت بازگشت ایران و آمریکا به اجرای توافق موقتی که در ماه ژوئن گذشته میان مقامات این دو کشور امضا شد، تأکید کردند.
🔴
وزارت خارجه مصر امروز یکشنبه اعلام کرد بدر عبدالعاطی، وزیر خارجه مصر، و محمد اسحاق دار، وزیر خارجه پاکستان، در تماس تلفنی روز گذشته خود بر اهمیت بازگشت به اجرای توافق موقت برای پایان دادن به جنگی که ماه‌هاست در منطقه ادامه دارد، تأکید کردند.
🔴
دو وزیر همچنین درباره تلاش‌های انجام‌شده برای مهار تنش‌ها و بازگرداندن آرامش گفت‌وگو کردند و بر اهمیت ازسرگیری اجرای «تفاهم‌نامه اسلام‌آباد» که در 18 ژوئن گذشته میان آمریکا و ایران امضا شده بود، تأکید کردند. آنها همچنین بر ضرورت دستیابی به توافقی جامع و پایدار تأکید کردند؛ توافقی که امنیت و ثبات منطقه‌ای را تقویت کرده و مانع گسترش دامنه درگیری در منطقه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145850" target="_blank">📅 11:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145849">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مدنی‌زاده، وزیر اقتصاد: ما اقتصاد ایران رو برای زندگی مردم اداره می‌کنیم، نه برای رضایت آمریکا
🔴
ملت ایران هزینه داده، اما هرگز تسلیم نمی‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/145849" target="_blank">📅 11:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145848">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزیر نفت عراق اعلام کرد که عراق ظرفیت صادرات نفت خود را به بیش از سه میلیون بشکه در روز افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145848" target="_blank">📅 11:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145847">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPExhoD7dkEpdPaw0nc1e6az51OIxmFe0AOgRbVqf-mfMnMqs_vMM5siLOPRiCg27q2ks_v4MzdwvhNODwAOFo8nGbKszNWL6ChaYAUW9sJksF4DhX8ndKZPanRMd012sDolV9AeADq2kn97zTZ-2ArDLhSI4tnB5YJ97WPkzTk5tdyUb6ZMIf5aQoKHiZS7c9nDqM1hRuoCB2A79z8nhIXcu4kCh856ZP7VEy6O5Ls82H3ZM4PrGpwY-TqleqnDLrBWf9Q0qNdJQFfVor8yWfTvJ7NDNl4Z2U5GQ1gkiftTrwzh0EteKjVn-s9x3X2Kdv-mHIpyq3OsDyqewojsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان : حادثه تلخ انفجار تانکر سوخت در محور سنندج- همدان و جان‌باختن شماری از هم‌وطنان عزیزمان موجب اندوه عمیق شد.
🔴
ضمن تسلیت به خانواده‌های داغدار و مردم کردستان، مسئولان مربوط باید رسیدگی فوری به مصدومان، حمایت از خانواده‌ها و بررسی دقیق علل حادثه را در اولویت قرار دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/145847" target="_blank">📅 11:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145846">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/500dcdb1b1.mp4?token=rvtkANNoKKRIXKeDCjeEGCOkNENV_X1mRJz9aeOKY_sAO-Yb8mH6dyqddsimto8nbw38mLNdWe0MjXUh9I-ZJidAVF3g74KCrIL3ap6MGMLGNVDxWA2_Kdx0vlatsnPInVz6B5REg-u9tclano4WzENg3fI7FhcAm_hC67_WZTm7-4nrrlXRvYQebaxb2CzoopqncWOotC7tsD4dsfp3ldMo07-5wTC00407d_jjMGeCkVulctogzzekm9CMXmNtApgGvF8Sre5NLyEKtcnhqHS6uGu8HquWR5Y-W9SmBKKA6ClZjYkJBslh_GAqDnaJV7oXt9MTm2qev9TzfVaHcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/500dcdb1b1.mp4?token=rvtkANNoKKRIXKeDCjeEGCOkNENV_X1mRJz9aeOKY_sAO-Yb8mH6dyqddsimto8nbw38mLNdWe0MjXUh9I-ZJidAVF3g74KCrIL3ap6MGMLGNVDxWA2_Kdx0vlatsnPInVz6B5REg-u9tclano4WzENg3fI7FhcAm_hC67_WZTm7-4nrrlXRvYQebaxb2CzoopqncWOotC7tsD4dsfp3ldMo07-5wTC00407d_jjMGeCkVulctogzzekm9CMXmNtApgGvF8Sre5NLyEKtcnhqHS6uGu8HquWR5Y-W9SmBKKA6ClZjYkJBslh_GAqDnaJV7oXt9MTm2qev9TzfVaHcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیر انجمن CNG تهران: مردم به فکر خودشان باشند، مسئولین در تأمین بنزین در شرایط بدی گیر کردن به نوعی بیچارگی...
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145846" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145845">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
شمار جان‌باختگان سیل نپال به ۱۳۴۴ نفر رسید؛ ۴۸۸۶ نفر نیز مفقود هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145845" target="_blank">📅 10:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145844">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZo5z6H8GSb908rNW9B1sBVxZe17lMYVzE1SNJbpWonXNDUSussUOhyR6KxtRqobC_rTApDXf_TF0oaGJ-FMs8dlHf87tYKsPTbTYAvwMOWfLJnWmb_OmeonxACar9i47LSqhE2OMl8HcW225gKRCg2XfRaqcB0Axtc_D6ChEud2a4rAaU5LcGE_PENeYAVWPijJDjOiJ_i2jrA_39z5eUhdfu6tqahsvhjUmuYT8AHkEYJEBclq6i8FUQxuxtDG9gzHNaJyGwM9PT9Oib6c6vdFDS2I9ucetHL7U8yBgi19EugLf6Ix6R3GIPfeTkM1L2gCX_i9Jtbc0fpNP-zKGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازداشت عوامل رژه موتوری مجاهدین خلق در کرج!
🔴
روز گذشته ویدئویی در فضای مجازی منتشر شد که در آن تعدادی از هواداران مجاهدین خلق در کرج اقدام به حرکت با موتورسیکلت و خودرو کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145844" target="_blank">📅 10:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145843">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
حمله توپخانه‌ای اسرائیل به سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145843" target="_blank">📅 10:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145842">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
بر اساس آمارهای تانکر ترکرز، صادرات نفت خاورمیانه در ماه اوت با کاهش ۳۹ درصدی مواجه شده است. این افت صادرات، منجر به ایجاد کسری روزانه ۷.۲ میلیون بشکه‌ای در بازار شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145842" target="_blank">📅 10:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145841">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
افزایش موارد کرونا در ۳ هفته اخیر
🔴
رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت: از حدود سه هفته قبل شاهد افزایش موارد کووید-۱۹ در کشور بوده‌ایم.
🔴
سرفه و تب از علائم شایع بیماری هستند و در برخی افراد ممکن است علائم گوارشی نیز مشاهده شود.
🔴
میزان موارد آنفلوانزا نیز در هفته گذشته مقداری افزایش داشته است.
🔴
کووید-۱۹ مانند برخی از عفونت‌های تنفسی از جمله سرماخوردگی و آنفلوانزا به یک بیماری بومی تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/145841" target="_blank">📅 10:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145840">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ارتش اسرائیل یک تمرین سراسری غیرمنتظره با نام "طلوع سپیده دم 2.0" را آغاز کرده است تا آمادگی خود را برای یک حمله بزرگ و چندجانبه مورد آزمایش قرار دهد. این بسیج ناگهانی پس از ارزیابی‌های اطلاعاتی اخیر انجام شده توسط اسرائیل مدعی است که نشان می‌دهد ایران در حال برنامه‌ریزی برای یک حمله هماهنگ و همزمان به سبک هفتم اکتبر علیه اسرائیل، به همراه متحدان منطقه‌ای خود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145840" target="_blank">📅 10:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145839">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOu1Y4uCxschoWmtsdnGdSHmkQS0w5pAuHoJtcAX1EXPeLEhoGpiQhxvvgpvwDEbBvunJuUtHov9-pIuGT6-tGW9F-261FjfcVz2zCSzaKQeLciLkNssKn3TI0OSRaeWtXVZds0TVyzLc44XEug1qTXqXd5R077cRNYqUgHJmrZOEuGpq1mlxbg4RIxbTX6rF6AXSzHXryUK7P_UCehhdBhljWwDVojiV9r5jJJ-LbQijLk1lt-OfIUqBzalF28QgeRiOczb2iCMg7GwbaRPWthwwKl1rUjhHQW-GZYdR4tJ38WK6xojRYBUbKygonZ7H_wsDFWVPgu97WC6AE8z3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان ملل سرانجام نقشه واقع‌بینانه جهان را که حاصل کار دانشمندان برجسته دنیا است به تصویب رساند.
🔴
بر اساس این گزارش، آمریکا با مخالفت دونالد ترامپ به این طرح رأی منفی داده و این نقشه را نپذیرفته است و ثبت نخواهد شد.
🔴
این تغییر به‌ویژه درباره نمایش واقعی‌تر وسعت آفریقا مورد توجه قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145839" target="_blank">📅 10:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145838">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxD59tmzR778RM3yk4pPK3Iw-9wnEcnXvqgg4H8BOOBPbX0j2RGG1Roq2Hwxoc2qFvf2RNtoj9dT4mDubIGNuO7KyYDVwaooVgtk37L-D1ojA9o2MSFhWOSMdjQIsKpIk_xt9e2A8mvPG-Rf-juIZtAvKfp8rQ0ZnYcJyCvD419pBuRhb48N976HyhZlnIrPex4oAbjqY1G26cWhewxUMiZpZTLCmhpglBoBoYWDZRrPDh4wnz4hBVPhauHJx_7qc4RC25cwsc8kw_ARBuTxQL5yAOh76nIR8qVEFe90wJRSynj6P2eTYlOAtjKEzGjsJkIIXREsBGVBMtsK5YVGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: ایران مجوز اقدام نظامی برای شکستن محاصره را دارد و حمله اخیر به ناوهای آمریکایی در همین راستاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145838" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145837">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73fa948c4f.mp4?token=ak94WfK1UFzstNHu0XI8SD_4c_ww5dlKiyFhRGEwGq65hsFpsvOWn5fh6LNSEf_JgLxy684iUSr0H3go-1Td1j3_V81gyA28Ii6NXgLfvM_mxwsNSQ-GtmSGMtJWIa2NqmMShIrCoueOtJXE3tQlThNcKsxpqjqYeqQ89SrvDg06u28oslZfMTmgZHGSYe-QvBXmojn2yu9esZMto_NnqTzkewLe1lccu39bbxPnYl-PFD4kkwjp6DBmiiXOmX_Qtbe66EdK1kuVPKavuS-itb9rMUxUswu7InFJ-UcGZP9yyIaY1I8SGUY6WxJH3DwAhf850QKwCA7NVtgAjRHY5UhVqj9SoRk6C1xQBUgjNjIWyD_HL1zkE6rmHXtaGXkOz2hG9egC9NvrCg9hjgyqHcHdDVbhXGlD0GohHcTlHHIi8igefSO0vYawixvgE5EZqfFdv5dFczk78TWhoQoxXHFB8mEszUk8p_-DuTSGgs8JnaU2FFBTKWwAh55qOlJgBCEibiNecekmGx34KuEbst6LI20o02MV5gvj6H4ks1ApDK0XQpSjsVsAOsuWTp6sxPSIpbhl41F34YAzydjLSNQAt5u1IqCbyEFZxlYwa1BwOSnjw7EV3FcEqRoCBZ6HoHfMmf2WvliLdIcjbXJUtNduhTaGvKoC98DwNDLOtmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73fa948c4f.mp4?token=ak94WfK1UFzstNHu0XI8SD_4c_ww5dlKiyFhRGEwGq65hsFpsvOWn5fh6LNSEf_JgLxy684iUSr0H3go-1Td1j3_V81gyA28Ii6NXgLfvM_mxwsNSQ-GtmSGMtJWIa2NqmMShIrCoueOtJXE3tQlThNcKsxpqjqYeqQ89SrvDg06u28oslZfMTmgZHGSYe-QvBXmojn2yu9esZMto_NnqTzkewLe1lccu39bbxPnYl-PFD4kkwjp6DBmiiXOmX_Qtbe66EdK1kuVPKavuS-itb9rMUxUswu7InFJ-UcGZP9yyIaY1I8SGUY6WxJH3DwAhf850QKwCA7NVtgAjRHY5UhVqj9SoRk6C1xQBUgjNjIWyD_HL1zkE6rmHXtaGXkOz2hG9egC9NvrCg9hjgyqHcHdDVbhXGlD0GohHcTlHHIi8igefSO0vYawixvgE5EZqfFdv5dFczk78TWhoQoxXHFB8mEszUk8p_-DuTSGgs8JnaU2FFBTKWwAh55qOlJgBCEibiNecekmGx34KuEbst6LI20o02MV5gvj6H4ks1ApDK0XQpSjsVsAOsuWTp6sxPSIpbhl41F34YAzydjLSNQAt5u1IqCbyEFZxlYwa1BwOSnjw7EV3FcEqRoCBZ6HoHfMmf2WvliLdIcjbXJUtNduhTaGvKoC98DwNDLOtmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت: ناو هواپیمابر «آبراهام لینکلن» در تایلند پاکسازی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145837" target="_blank">📅 09:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145836">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TA6OU3vMkwBDbHLjkB1o_K4ShI5oh49RdzyrQ-aJlAKX5vLl0uEMIb4v1YWdSGDmq5oqkOUeI2jvRFG2Lw7LV-1Ri0BipPtYxDKaudSflsg0cfrPLGVAcdDitKEWeDR5W1lFyCpZz6bslEbyG92YdntWaOZK-1Cfrn7HW135_ew47H-RFflnl6ox9qfkRGno0pOd1NYrDbgOz0LAe_sv2-g_gyAJtzoO7Yp-YpYuP2eiXCQw7-FAmTHQLVl0PgCNA-hh6QUCekMr5LZl34nRD338HO77bIZGIeUOa4Dlf5Hut-JMjXBIruDXP6_CKtiwNbGG3N6EiPiWyLkRpG73Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از حمله هوایی نیروی هوایی اسرائیل به ساختمان مورد تهدید در عرب‌سلیم، جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/145836" target="_blank">📅 09:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145835">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3d2e6a9ee1.mp4?token=N5-QpjUtQsLCGEcsuQLDtLk92Cm49MK6DPkSf3kyRV4MvcsgMuBSorlZ2wK_ehs_ID4BBFq729Yhy3QUViCAO0wJn0rV3UJEiGCWETCOdAKQ6A0DhwFqzpEyRM-U0ehOgOETMfN7IB9WEI-ZxW5qs9lz6hzfTPp6yIWD-RwYP8-vonNTb6uO_2WPXqP9UtcH_yNdJAUa-ntRzS_TX0SZoS6OEuLeQUoIUssTNYKqRFkjsupgUEGBZ43zYJY4C2oa1qDSLfi7lQHb973XLWoG0p0BfHVP-bgMc4SOpW2Xz5XqoVXPPL8Za-xQmetJsURffTs3V8zs0qe8tMiKh4jgdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3d2e6a9ee1.mp4?token=N5-QpjUtQsLCGEcsuQLDtLk92Cm49MK6DPkSf3kyRV4MvcsgMuBSorlZ2wK_ehs_ID4BBFq729Yhy3QUViCAO0wJn0rV3UJEiGCWETCOdAKQ6A0DhwFqzpEyRM-U0ehOgOETMfN7IB9WEI-ZxW5qs9lz6hzfTPp6yIWD-RwYP8-vonNTb6uO_2WPXqP9UtcH_yNdJAUa-ntRzS_TX0SZoS6OEuLeQUoIUssTNYKqRFkjsupgUEGBZ43zYJY4C2oa1qDSLfi7lQHb973XLWoG0p0BfHVP-bgMc4SOpW2Xz5XqoVXPPL8Za-xQmetJsURffTs3V8zs0qe8tMiKh4jgdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از پیامدهای حمله هوایی نیروی هوایی اسرائیل به عرب‌سلیم در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/145835" target="_blank">📅 09:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145833">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQPqpwGYB4upJp2OL9ML7s0ZCMwNxv5erCPyq7BiUwzrcoKVNTiYpUxPPwo5MsUI-FfCV4OhZhMdhg3fWCYq9MqRFiDGWZADJqhUntJMwIE6PNyD9bBFNjTnw0RH0OxQdmTJfSnTxuGurN0fYU8RsN_XS35O4KmQ09-bvn_P--Ntb6MII8I2VcEYs0TJJDtu-1CSP8827FnmRo4mhQE765OYISzYqNdgHDih2CXGzbF9fQsN1FnKweonUybOV4rWB-DkDqXTuUtYbhRHYFner6-NmW6dbXRW1fkDhet-6t7-8R5UoKRbi5p8iWwNTQKPpah6fzM0fAsbhPtdlmgB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGZ2JqsP3sZ5mezb0aEBDJq0LGtDDfVjdaWhU1w4X9_ylR7cLN2H2Y3ceWukhehmtGloaExARCRPvMiL_VekzEI5RoKCldusegwblWo84-RMAWpn4ZYeEhlQSfbkEtGOPeqj0gwuJUb3HzyLSg7B3DtYESt-GkHbSwaGh3FW_zKNVdrdrqvePdsT7VkTumaGFxXbaXTmPHJ3j7DOB_1Urir2RAKq7gP2KXlaE7m96UdjZsr2n-gzPM2TUtX2G3IJXI655tYfONwrTXtI1fjOAcJBLb3yifHFsceviPEFu0C10LVvr-JDWFS7r2LLZNnfpRB-gKBH3el11-ZClc9WZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
چندین حمله هوایی اسرائیل
دقایقی پیش مناطقی در
نبطیه الفوقا
در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/145833" target="_blank">📅 09:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145832">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KioaUlX7sbgH9oZYvRhjMy72j11eKY9hwQbtg4kyG9yaBVuDzZ2e-omIiWkH2xpDqPCYPJioTRG_4-ocdMzQDTlSwbAPnQKqHwdns3IOPUk1fKuPBaECyKonSEcTzOCghR_REiP_9KaGpUmBY0DzPF_r6GW06hqKIpfxIkI3m4mz4eNksLO2hhLfsOehF-HIVtfwp_CBmXXVPGgdLNfCqx4esI0ICk1THEfn-vb-DpaWZ2h4JjkpQF9lFxrBmZF2K5tVwHRJ6agW6iGIhWDwvIYqGxobN3kYo3OcQjjVaKDi9o-8WLGQJhrAHvnICgyt7cHh0gVXnngAxTIkGc27OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا:
🔴
«جدید SOUTHCOM »
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145832" target="_blank">📅 09:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145831">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7fRymhDFhYqCJNEGHoh-lfJt5dTAjWbXLXsXn_YkDrQGINnGLKMparbsM64SFHEARRL69se6tqOrwwoq_O61aCQRf5zLCqG2TatELoGzp3bQz4vZPgyOGssrYVQZBOqeC5ExRvc193iOWfeMYUhBio-pv12fsyyaTaXz2XzuMqCdnT_xaakuXWMuJW57a3g8Mku5C59g7XJzWp-m7g8mGiS-fNR-9NbVHj7QL8kclF4uA2WzlCU9sNSwlN4wY5qgN0ScXT4EjoQmlVIPH1XKN2BE-qk2QHdl_iXyv5otUsLDI6XsRuW6mepteKTPY73MYrd4UD2l3OmRFmJ6Erc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ در شبکه Truth Social:
«بسیار تأسف‌بار است آنچه در اسپانیا در حال رخ دادن است؛ کشوری که
هیچ کنترلی بر مرزهای خود ندارد. واو!
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145831" target="_blank">📅 09:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145830">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0166bc5c.mp4?token=knPuNzY_TNhEKhHHekLl0KoZbXTPNJRbJ9XP68egj_MvCg1gByMO1Vkd6YtMUq9G1OdV1H1yQwvrpYvkF_g1okoTwXo9aGWXWipbNZqYKpvhvntXoJaB-R_AytNJyARYGIGE9Yom-dyxzAI4xpSlAzeS72XVRu9e6JQ2MvMd0zVTppwAgFUrkkN7vjzIJoYLxn47NlE5tbtP8Ii_h5ZBhBNM_pIv19US6CreH6IRwfY4IRPGdSFe1tcEUIBdqIcimumQCx1JCrvUeodCWzzPRTy9OqiGB0PTeC-Pfe0KmBu2eN-dpW_8n8ZbZvp0OHw0HdFHlh4qYY8v1fp_VEk3fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0166bc5c.mp4?token=knPuNzY_TNhEKhHHekLl0KoZbXTPNJRbJ9XP68egj_MvCg1gByMO1Vkd6YtMUq9G1OdV1H1yQwvrpYvkF_g1okoTwXo9aGWXWipbNZqYKpvhvntXoJaB-R_AytNJyARYGIGE9Yom-dyxzAI4xpSlAzeS72XVRu9e6JQ2MvMd0zVTppwAgFUrkkN7vjzIJoYLxn47NlE5tbtP8Ii_h5ZBhBNM_pIv19US6CreH6IRwfY4IRPGdSFe1tcEUIBdqIcimumQCx1JCrvUeodCWzzPRTy9OqiGB0PTeC-Pfe0KmBu2eN-dpW_8n8ZbZvp0OHw0HdFHlh4qYY8v1fp_VEk3fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت: محاصره و تحریم‌ها قدرتمندترین فشار اقتصادی تاریخ علیه ایران است
🔴
احتمالاً تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز آن را خریداری نکرده، این مقدار به زودی تمام می‌شود و دیگر نفتی نیست که چین بخواهد بخرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/145830" target="_blank">📅 09:02 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
