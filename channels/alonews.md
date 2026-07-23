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
<img src="https://cdn4.telesco.pe/file/Hy-43fF5_pucDh4i9ICWmaPkamxKDXaXLw93TRIUgNvvnJGOa12lfVMVRB9YnbNgvvtgVkKJJnc0ps-5s5590XN2PH1ZKKwAPG0MjUgncrs4MQpI28n8kkienMK66CGqKCJgiLPZXRXwBPSJDCwoVA_eOc4kO7Uw4foU8Pc7e-GVWEpSSOTv_SOhM_31KoxC7jpNuL90JENOCYlaaGZVTbcGZGrMurl44m1coZj-sFPJb5D62WaWBc54fp7GxUWhjsUvOwt71Rkv1VW8g1nbSv9pMdX5pgj-TY8HYMXCV4uHBc854Dxv1_-zAqyX75m317e1FSEgF4hE_tjk-cXhqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 933K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 11:27:00</div>
<hr>

<div class="tg-post" id="msg-136897">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزیر نیرو:  نیروگاه زمین‌گرمایی مشگین‌شهر اردبیل به ظرفیت پنج مگاوات و با حجم سرمایه‌گذاری ۱۰ میلیون یورو به شبکه برق کشور متصل و وارد چرخه تولید انرژی الکتریکی شد.
🔴
این طرح به عنوان یک پایلوت بر روی مخزنی از انرژی زمین‌گرمایی با ظرفیت تولید حدود ۲۵۰ مگاوات درحال تکمیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/alonews/136897" target="_blank">📅 11:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136896">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTvnISWmcf70spY100EtoGyvOjdk7FfS2OuF2lLktA8ep8kMtfF3bSyM3hZXPdLgGJRwFiJgdKSQMbC3-Cux3Yxcc6jKzBOdUNJp6HSnyi03sM0vFInE6GCI4id_z5XcS4PLertw-ShDk7UYnLx6mrK6icZrOIciosurwSqwOqx8RFoOS7l7Si8Tg2mIBkONqZtqq-t_uWVpTiVBvNXynzEDkQO8vfMlr_i9qYUrm2hSJVLXlNf6DADnckmX8ZyAxwV-ggM-RFilqx1XR1RrcXEMhpQ8Dr2ce_GLFigOY0PxiL2ujSvd09NZGBTp-Vo2kUlWmQGXW-R3G0q2vFNMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۷.۶۳ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/alonews/136896" target="_blank">📅 11:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136895">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
صدای انفجار از قطر و اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/136895" target="_blank">📅 11:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136894">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd04aa4c7.mp4?token=rEWZvy-ZgDNCeBuWpOxQx6hDO948fm9SDUiwpCxlzOVUFsSstUMwZG0XOW-0j_fevVtIQIKILeY9e4xQfCILeT_vyljd4TBT8iobulH5Ro669Jtl91KXW1dYqQylagXSXWzmkEBwIBYpr5ijADfAmZ2j2PgPM2JoanL_RnzwN_AgVsrVYmSxTmzvEdqjyIVnPGWfyHh4fn7IIxP_GjSBmEzC7UMuAhFJX3rJdtdkJtsKqqtZ8SN_oUohDQQcUV4dElP9p0Li9og61AvODDc5VVKw0ArpKkH6j0oplV4NV8bf8NV3FXpFyfa0YY5ihXScSSNz9sCtmxRbd0ZfISGmkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd04aa4c7.mp4?token=rEWZvy-ZgDNCeBuWpOxQx6hDO948fm9SDUiwpCxlzOVUFsSstUMwZG0XOW-0j_fevVtIQIKILeY9e4xQfCILeT_vyljd4TBT8iobulH5Ro669Jtl91KXW1dYqQylagXSXWzmkEBwIBYpr5ijADfAmZ2j2PgPM2JoanL_RnzwN_AgVsrVYmSxTmzvEdqjyIVnPGWfyHh4fn7IIxP_GjSBmEzC7UMuAhFJX3rJdtdkJtsKqqtZ8SN_oUohDQQcUV4dElP9p0Li9og61AvODDc5VVKw0ArpKkH6j0oplV4NV8bf8NV3FXpFyfa0YY5ihXScSSNz9sCtmxRbd0ZfISGmkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری های نیروهای حوثی و نیروهای یمنی تحت حمایت عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/136894" target="_blank">📅 11:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136893">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
اتحادیه اروپا با صدور یک معافیت یک‌ساله و قابل تمدید، انتقال گاز طبیعی مایع (LNG) روسیه به کشورهای ثالث را مجاز اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/136893" target="_blank">📅 11:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136892">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ1FdY-TNAEb1UnGDDXmFKDeMJwbF7C-gclGDiC50GkdJVEZKqnWeYNPGp_yYQSvLy4kpJKCzFz__adc-SrV3TAxyp5aTTUDELp2sF08tuL_bLI8orppgQzxM2RubXHmM3UIR7g1vFmZ4-4PMhfvtnz4cnCo2l6hMci5zInf9f8iEfsHc31TWEdIVGpT2jS0dquViG2fyV5_fOhZGGX-Rw_aDxXC5281iyffa1cFP--doZcJMlnByzS3WTqufsf88Zt7iz3D9vPWQ4AsfWHR_Tr5PEZnPpqZbY0kNutC-sDdTM-vnGQ40BaOWcGqkgl6yqrwl6z0k5qoXTDLri1qhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر عراق عازم تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/136892" target="_blank">📅 11:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136891">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7bWGTAp73_v0T_vAswypfaDVYo1upVjK28lnroE0oWhw-_RLKvJcU4uNLKLpW5HBdHj9dbwSX2BD7749nrwtf2GeKZ0UibkzA7HDcVXRbr3FcUMQ4tjjTqVuaY05_gzk101JIJz0o_4eVF9FQCDKPNP8IOAFtJHV53i5rYIv7C_u6y4XDTrfS_2xk3JFbFRstjabM2CgqQkEkzpcRcGmyXOwG5fInI1spwzfCoUGzf5dKr2oIkOSx8t5jecZekyG4vJuMaklOr5rojspq3BWXgbWIzxIG_uqEsv_yTjP4n8AdOwL24psvsF3mYpad040B52j_SRdKD0zOFqfB9bIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
دو شلیک موشک از آسمان خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/136891" target="_blank">📅 11:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136890">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان:
تهدید هر کشتی که پرچم پاکستان را حمل کند، تهدیدی برای امنیت ملی ماست و حق پاسخگویی (واکنش) را برای خود محفوظ می‌داریم.
🔴
ما بر ضرورت کاهش تنش و پایبندی به مفاد تفاهم‌نامهٔ اسلام‌آباد تأکید می‌کنیم.
🔴
پاکستان از تلاش‌ها برای کشاندن عربستان سعودی به درگیری در خاورمیانه ابراز نگرانی می‌کند.
🔴
ما بر حمایت خود از امنیت، حاکمیت و تمامیت ارضی عربستان سعودی تأکید می‌ورزیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/136890" target="_blank">📅 10:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136889">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
شمار قربانیان زلزله‌های ویرانگر در ونزوئلا به ۵۳۹۸ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/136889" target="_blank">📅 10:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136888">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
امیرحسین ثابتی:
نباید تنگه رو از دست بدیم، نباید تنگه رو بدیم بره. شما می‌گید تنگه رو باز کنیم، مفت بدیم بره.
🔴
شهریاری، عضو کمیسیون امنیت ملی مجلس وسط پخش زنده :
بدید برررره، تنگه مال ننت بوده که بدید بره؟
مال عمه‌تونه؟ مال کیه؟ ارث باباته؟
🔴
امیرحسین ثابتی :
آقای شهریاری ادب داشته باش چرا وارد بحث ناموسی میشی تو پخش زنده...
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/136888" target="_blank">📅 10:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136887">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLGi39UoKBlHGLmc9Q5rXC96Sx7BAi1QEFqj9FhI4WsCnfdYYENUs2hg8hh4FlILK31hK4UKIP9dGtgJgJcsyV-3vwKhJ5Br-xrO8yWPUE7tLd55BJKRvZx5iNWYTIL5YDY1_5O9nmSIvQ6V4KA2w3tqCImQNgW2QjornMwlvXSW1lJC1fy_LOjBuo47hig59dey1Voob_WYKDwdwWmzh6vU5TIk344lS-V4StLnoUme-p6xRXNKfgFCcVKqvWPem_DvFv5u-GuOxwbXDgq_PyvX4KjV4_Pki-yQk6dcndVAOLQvOK_4fibrB8zcLqz_gF4-mLbVvIE8lbkCACQtbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش از حمله موشکی سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/136887" target="_blank">📅 10:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136886">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApAIbvCFCXkNp8ZSwCT62Z8AwYHShRuAl-_8PWdEh-xAkgS1zdBkl7s0Ur_bAqkN-u0TvYgmM4e8Z_hf0hiFz0YDZGacOjF0WDrgAbUJbeIB0KgXFQpFpjgCI-UbpG9FhyhsSEFg3rTbyj45ejWSF1u4GXa-_rjAdxo4VfCKSm5HcnDfQ2avMpT1YYsCJ68R8Miv1X0esxqiEbwWJJgP4v59Fx6_j7UFKK3ErqdmXOaBYghzUlUFQcgXPTVXAEVei56J_aMvoXYjYHQoJuenuMDRkGP_7o8Ny5_vbBh3g-MgZdvGGQqwv5Ud1-AHE4oOzwyu0RVba5fwIxRU3e0wXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متأسفانه امروز صبح خواهران دوقلو
رومینا رحیمی و  ترانه رحیمی از معترضان دی ماه اعدام شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136886" target="_blank">📅 10:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136885">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رسانه رسمی عربستان تأیید کرد که یک نفتکش این کشور در دریای سرخ هدف حمله قرار گرفته و دچار آتش سوزی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/136885" target="_blank">📅 10:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136884">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af710f15dc.mp4?token=chamZj4AlwwTZzejuEUfjMSVBhFwlkVMePND8c51K_wdTjdADXQBeD4ahBhsqaztAa2Ghuy_d1C2P7xkR9F79_2vvkkJMXD2sMSJL7JgoBCm3g7x5NT-zwHJ1mEWJM3Fr34rjtzTwmrwXbpeB-CPXS0RAmhIZPcbTC-iIC04XUhhA2Dgg4BpONhHBP-e2Rna-x2Eb7E26CMT1qZ4ISOY_nroH1T0CWbMXUOCP4ZkqpM4QdPctGZKDEO1gRwh3UImpeuVyxvy8rdCo9JPnLHUynoNhmRbUn4Zd7P380YdqxvXr05wp7EpyH-TCvrF3h7jxmgXOUECGldt6clmy-1SIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af710f15dc.mp4?token=chamZj4AlwwTZzejuEUfjMSVBhFwlkVMePND8c51K_wdTjdADXQBeD4ahBhsqaztAa2Ghuy_d1C2P7xkR9F79_2vvkkJMXD2sMSJL7JgoBCm3g7x5NT-zwHJ1mEWJM3Fr34rjtzTwmrwXbpeB-CPXS0RAmhIZPcbTC-iIC04XUhhA2Dgg4BpONhHBP-e2Rna-x2Eb7E26CMT1qZ4ISOY_nroH1T0CWbMXUOCP4ZkqpM4QdPctGZKDEO1gRwh3UImpeuVyxvy8rdCo9JPnLHUynoNhmRbUn4Zd7P380YdqxvXr05wp7EpyH-TCvrF3h7jxmgXOUECGldt6clmy-1SIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز هوای شمال غرب و جنوب شرق کشور با رگبار رعد و برق همراه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/136884" target="_blank">📅 10:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136883">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
براساس حکم قاضی آمریکایی محاکمه نیکلاس مادورو، رئیس‌جمهور ونزوئلا، و همسرش سیلیا فلورس از اول ژوئن ۲۰۲۷ آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136883" target="_blank">📅 10:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136882">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8a27cdc2.mp4?token=FwBtXcxpwqFWbjEwQbxe_fxLg-TCMpIj-ea6_R8oYzhHOYjNytBZWbmtCA4RotaRuUC8kfOlITtK1L49awUfGvCLrcu0lJMTiNpEComwJDvDwo1p2CNhPZhP6zfiiA1hllp_ERLHWizOt_ftJYpD8a9vg8qnd9ogJbYL9ht_UQh80d7a4XmWpDDu8TEUA1xFoPiIt22Vp2gRdSJZy_yEDNA22cThK6MsDM6tNugBFsRscyFNiZwyipNU8tabYZ8umMfT5fkbUrmZUFy8R2ZBm-qkjv_ZUFrmUx-X7TyNegj0HB0JdzzeFGjKm49PljN9wVGvYeNmt5FGY2kBG0QEoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8a27cdc2.mp4?token=FwBtXcxpwqFWbjEwQbxe_fxLg-TCMpIj-ea6_R8oYzhHOYjNytBZWbmtCA4RotaRuUC8kfOlITtK1L49awUfGvCLrcu0lJMTiNpEComwJDvDwo1p2CNhPZhP6zfiiA1hllp_ERLHWizOt_ftJYpD8a9vg8qnd9ogJbYL9ht_UQh80d7a4XmWpDDu8TEUA1xFoPiIt22Vp2gRdSJZy_yEDNA22cThK6MsDM6tNugBFsRscyFNiZwyipNU8tabYZ8umMfT5fkbUrmZUFy8R2ZBm-qkjv_ZUFrmUx-X7TyNegj0HB0JdzzeFGjKm49PljN9wVGvYeNmt5FGY2kBG0QEoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک‌ مرد که پشت سر ترامپ بود، در یک گردهمایی در جورجیا خود را به جای رئیس جمهور آمریکا جا زد و توجه همه را به خود جلب کرد
🔴
او به طور کامل حرکات، سر و صورت رئیس جمهور فعلی کاخ سفید را تقلید کرد و عبارات او را تکرار کرد.
🔴
این ویدئو به سرعت در رسانه‌های اجتماعی و رسانه‌ها پخش شد. برخی این تقلید مسخره‌آمیز را سرگرم‌کننده دانستند، برخی دیگر آن را تمسخر دانستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/136882" target="_blank">📅 10:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136881">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e26a43d45.mp4?token=jTs39uwX0w9bNeBEXW-li5kS_vz_WXFDXAXbE8khx3UlBM9e2YUah9fXYa-JSbXn1fzKtlidjJioY7DsHMZgh2ds1BvV_pfZfpli8FM7yVmQWu0p626xJlgtoT08IFsOd7msOSdV-y_Rv7VQUa3KY4WBOoVs90CriibjTtLPq4yfWXeYqp5jwb5J_BapYWXnXimb8TBSlQFJ2Tzur-UNOgL9Mli7p3xiJ2Sk9oLPu2kSr0xlIWWfRv3GfnZBoEGrUxVRBx5t83jCSwIuM7N0e6P46Qis6LcDfCzF2ByUH9vNAYWaptSFpvj0sUuhTFAjzFwycUZKmBz3HLL26rEHhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e26a43d45.mp4?token=jTs39uwX0w9bNeBEXW-li5kS_vz_WXFDXAXbE8khx3UlBM9e2YUah9fXYa-JSbXn1fzKtlidjJioY7DsHMZgh2ds1BvV_pfZfpli8FM7yVmQWu0p626xJlgtoT08IFsOd7msOSdV-y_Rv7VQUa3KY4WBOoVs90CriibjTtLPq4yfWXeYqp5jwb5J_BapYWXnXimb8TBSlQFJ2Tzur-UNOgL9Mli7p3xiJ2Sk9oLPu2kSr0xlIWWfRv3GfnZBoEGrUxVRBx5t83jCSwIuM7N0e6P46Qis6LcDfCzF2ByUH9vNAYWaptSFpvj0sUuhTFAjzFwycUZKmBz3HLL26rEHhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی همچنان در پایگاه علی‌السالم در کویت ادامه دارد، پس از حمله ایران. می‌توان دود ناشی از این آتش‌سوزی را از فاصله دور مشاهده کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/136881" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136880">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRqTu7c-gI-CL3VVOsGCpEpCskKM7aL53ieBTJ3JTvQSL3Dr8PJZEaUNZt0yWLEweJGkRuxRbjBneQ2hnPrqDdJVsM4aWkOahltpi1ExujGc_7Fl1VqmVesrG7aZ-FGiCLqGx9PyTPp0N2kn8mwFLJni8mO8hvJTOFj78z2phZ4DWCdP6S0_2Di78RsZzb-jkjvJ3jGmOepI3xdfqy44gg7l9CFUiSDobnPRR5I1wEy5iopZW7NZWj3Z492GW5jSRa9Cv2V4t-gQjObNW74IswQZqmgpaEa-9s-bHcpGwZTowkO4yCPlX-ea0MM1TfCXg6m6oBGzxjcTveSP8-dvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری رسول خادم برای عادل فردوسی‌پور
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136880" target="_blank">📅 09:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136879">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
شبکه آی۲۴نیوز: نتانیاهو همچنان منتظر تأیید کاخ سفید برای دیدار با ترامپ است؛ سفر او به واشنگتن در صورت تشدید تنش با ایران ممکن است لغو شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136879" target="_blank">📅 09:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136878">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f280731e5e.mp4?token=d643dVFz72NTPOgmTkAYP2osZXm9TIRcHF2RsHoZ-FuMQFSE5iuE3OioKnf9Tc4nvPdPHugu1J5wXIyFIcvALFCdQx2dkYyEoIq_QXezWyO5Vz9b5jjKjIM535XbW506pLbtACcVcZSvxovsS05UN2DMVWcFxjEW6MsO5lkGPHY7HXvXm_b5jnz_qn8KTmwHK1ghmBl0xSGVjyF2WSRh5yxl4Ek-rt271XtbdeZBjYqIRq32P9_QEOO679Rkj0rwhi5mhPyr-s1H92NeWUZmO3qg6kqLTWSyWP9LLZdK_KaPrJwF2PE7V57o3_y5EMvYyyqsywh_i7nsLl1E8zMbSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f280731e5e.mp4?token=d643dVFz72NTPOgmTkAYP2osZXm9TIRcHF2RsHoZ-FuMQFSE5iuE3OioKnf9Tc4nvPdPHugu1J5wXIyFIcvALFCdQx2dkYyEoIq_QXezWyO5Vz9b5jjKjIM535XbW506pLbtACcVcZSvxovsS05UN2DMVWcFxjEW6MsO5lkGPHY7HXvXm_b5jnz_qn8KTmwHK1ghmBl0xSGVjyF2WSRh5yxl4Ek-rt271XtbdeZBjYqIRq32P9_QEOO679Rkj0rwhi5mhPyr-s1H92NeWUZmO3qg6kqLTWSyWP9LLZdK_KaPrJwF2PE7V57o3_y5EMvYyyqsywh_i7nsLl1E8zMbSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اخراج خبرنگاران از اتاق دیدار روبیو و لاوروف وقتی سوالات حساسی می‌پرسند
🔴
خبرنگاری از مارکو روبیو می‌پرسد که آیا از وزیر امور خارجه لاوروف در مورد کمک روسیه به ایران برای هدف قرار دادن نیروهای آمریکایی سوال خواهد کرد یا خیر.
🔴
خبرنگار دیگری از لاوروف می‌پرسد که روسیه چه زمانی حمله به اوکراین را متوقف خواهد کرد. سپس یکی از کارکنان، خبرنگاران را از اتاق خارج می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136878" target="_blank">📅 09:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136877">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d28883e8.mp4?token=pMebASnqNdCVr6DBXrG6n9syeMzcv5n6htH4uobWTqvcxkIGpkOeTQg5C5HkJcojm6WAaYrA5S279Lb33iM7KBJOarwUiDH4wsfhOUNjJV3JaJN4kXuYw-HwJS9TWOdqOPelgP1nyDeFlr0CmeuPBb1H3J90mjQxFjjGd9QoW4PcUTYFJ7guuDnT1zPPLad4-N0TJHzSO97_5Y4Qe0aJuiZRU3EXLB3HJ0RV0g72kC6MiIe_klmHEs3lHSIJXXsbimBNcuzgOUW9slJW-QQL4pmmi6V-S7pZpRVgjh8mC9SMr93ZkT7TZV-NggqNOnexQ8vBqZpXsGwocETgFbLq9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d28883e8.mp4?token=pMebASnqNdCVr6DBXrG6n9syeMzcv5n6htH4uobWTqvcxkIGpkOeTQg5C5HkJcojm6WAaYrA5S279Lb33iM7KBJOarwUiDH4wsfhOUNjJV3JaJN4kXuYw-HwJS9TWOdqOPelgP1nyDeFlr0CmeuPBb1H3J90mjQxFjjGd9QoW4PcUTYFJ7guuDnT1zPPLad4-N0TJHzSO97_5Y4Qe0aJuiZRU3EXLB3HJ0RV0g72kC6MiIe_klmHEs3lHSIJXXsbimBNcuzgOUW9slJW-QQL4pmmi6V-S7pZpRVgjh8mC9SMr93ZkT7TZV-NggqNOnexQ8vBqZpXsGwocETgFbLq9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلمچه دیشب
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136877" target="_blank">📅 09:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136876">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
عربستان سعودی در پیامی به یمن اعلام کرده است که انهدام یک کشتی را بدون پاسخ نخواهد گذاشت. این هشدار در شرایطی مطرح می‌شود که تنش‌ها در دریای سرخ و آب‌های منطقه همچنان رو به افزایش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136876" target="_blank">📅 09:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136875">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=tOJgtUf8vNsQEEkfHdllaPEEOR1iP68Jbl4N6Q2rvjbwwcoIHlmb-k2OXiRYUT8bQ-uag5NVVwo2QPZ1Ai96VK_LZMSFmAKmaRHLpQk7JyUwsveQT3zT16Zp4vS1GXTnJrx3bTOmGOt3escySpQFnmO1sSaNJ3s8pRrrbvsdN9bkcInYzRRSPJWizUTi-EzXMBSgttpBj1gE4ykmIeER8RC08QmNzxSfU7oekru8mYJtFG9UKReP12bJRLnB5DcVnhsGJsUxQOY8Sx3LBpAiLp-2mLIT_eMmdDxlL17sSHdRr1TtQRDv4dpAmM4mX9vF4tX3wd-ud_NdL6oX9Wniaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=tOJgtUf8vNsQEEkfHdllaPEEOR1iP68Jbl4N6Q2rvjbwwcoIHlmb-k2OXiRYUT8bQ-uag5NVVwo2QPZ1Ai96VK_LZMSFmAKmaRHLpQk7JyUwsveQT3zT16Zp4vS1GXTnJrx3bTOmGOt3escySpQFnmO1sSaNJ3s8pRrrbvsdN9bkcInYzRRSPJWizUTi-EzXMBSgttpBj1gE4ykmIeER8RC08QmNzxSfU7oekru8mYJtFG9UKReP12bJRLnB5DcVnhsGJsUxQOY8Sx3LBpAiLp-2mLIT_eMmdDxlL17sSHdRr1TtQRDv4dpAmM4mX9vF4tX3wd-ud_NdL6oX9Wniaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهریاری نماینده بجنورد به ثابتی: تنگه هرمز مال ننت بوده؟ مال عمه‌ات بوده؟ ارث باباته؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136875" target="_blank">📅 09:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136874">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
به گزارش وال استریت ژورنال:
اعزام گسترده تجهیزات و نیرو: آمریکا در حال ارسال نیروهای ویژه، کادر درمانی، تسلیحات و هواپیماهای سوخت‌رسان به خاورمیانه است تا گزینه‌های نظامی بیشتری علیه ایران در اختیار ترامپ بگذارد.
🔴
آماده‌باش نیروهای ویژه: پروازهای باری از پایگاه‌های عملیات ویژه انجام شده و این نیروها آماده اجرای مأموریت‌های مختلف از جمله رزمی، جست‌وجو و نجات هستند.
🔴
آماده‌سازی بمب‌افکن‌ها و جنگنده‌ها: بمب‌افکن‌های دوربرد B-1 مستقر در بریتانیا برای عملیات‌های بزرگ آماده می‌شوند و جنگنده‌های F-16 و F-35 نیز به منطقه اعزام شده‌اند.
🔴
میزبانان احتمالی: کشورهای اردن و اسرائیل به عنوان پایگاه‌های احتمالی استقرار این جنگنده‌ها و تجهیزات جدید در نظر گرفته شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136874" target="_blank">📅 09:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136873">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
معاون استاندار خوزستان: در حمله آمریکا به گذرگاه مرزی شلمچه در استان خوزستان، ۲ نفر کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136873" target="_blank">📅 09:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136872">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68bda1db65.mp4?token=KOgxqxoNjtHN0cEiWt8CqqqTPNa30J0UHtfkW4w3HBtT68j26qcsRhmHiMckCFyeJAN5gEtWyljQc4PkuwQUWUWz3IoBMsL7b1XNQ3oAmAC4-KhfbD8UGu8w2arZog2PlJtVTR4i1p72aNDTcq7OtPQeF3D85dtQEPfJGaMfqv97f67Vh3vUlX5OVDj1KpfTHJ95B7z0yConXEnF6s_q9Mf9lzD8Ztzn3iVUDtoOvZNitQxI3Go52rr9WjXFBJAHADHYQPB6lhIrx8v8wQVNC-pn8rUjX0Qmu1lEAyL0rBAw3KaDLQMXCmSUF0T_HtM-7oEIzB0Va4-C3TLVAQEJ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68bda1db65.mp4?token=KOgxqxoNjtHN0cEiWt8CqqqTPNa30J0UHtfkW4w3HBtT68j26qcsRhmHiMckCFyeJAN5gEtWyljQc4PkuwQUWUWz3IoBMsL7b1XNQ3oAmAC4-KhfbD8UGu8w2arZog2PlJtVTR4i1p72aNDTcq7OtPQeF3D85dtQEPfJGaMfqv97f67Vh3vUlX5OVDj1KpfTHJ95B7z0yConXEnF6s_q9Mf9lzD8Ztzn3iVUDtoOvZNitQxI3Go52rr9WjXFBJAHADHYQPB6lhIrx8v8wQVNC-pn8rUjX0Qmu1lEAyL0rBAw3KaDLQMXCmSUF0T_HtM-7oEIzB0Va4-C3TLVAQEJ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما: چابهار و کنارک شب آرامی را پشت گذاشتند و زندگی همچنان در جریان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136872" target="_blank">📅 09:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136871">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlJH59TgYqYYh6t8cDLQlns6rLdvba51YKZyyNtmMxRz5_atGoI2jM5D4aJcYgstfiXr0iiPpD0drdd0DPpPWAmZz-e0LgAJOyW30ukL87qs2sRuenJRCnxxqV7tlmgUPTZShG5k-DNVVMaOyNy35QoMQqCrS1MYzYGeJW-HWFLdZaeCU65e6X6iqyhs4YK12VkDX-EPX4R9fbnl6FTtJ3gBemaL6c1Oic-dwVgbWMHmVVCe7VYLHN2ph_1xAECBt-dv_HptQfOmMzO_UXTdGf8hpKjf-YAVKGW3_t4F30z1jIQzsheZMw7lrujbVpafk3Mop34KN4IUUWntF-BJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخابره کد اضطراری توسط «آواکس» آمریکایی در آسمان عربستان
🔴
یک فروند هواپیمای آواکس E-3 سنتری (سیستم هشدار و کنترل هوابرد) نیروی هوایی آمریکا پس از ساعت‌ها فعالیت بر فراز شرق عربستان و در نزدیکی قطر و بحرین، بامداد امروز کد اضطراری ۷۷۰۰ را مخابره کرد و مسیر خود را به سمت پایگاه شاهزاده سلطان در عربستان سعودی تغییر داد.
🔴
مخابره کد اضطراری ۷۷۰۰ به معنای وجود یک وضعیت اضطراری و فوری است که نیاز به فرود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136871" target="_blank">📅 09:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136870">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e40882f729.mp4?token=RHM4mhrmn6BHkQJWgwyeDJXg_zidmuqbebWMOIl0-V5ruuezY75sKpIbE1q3cAIPYHnAdcoG3fecIHltgLE3Sed0eJUXiDbsBHHtUwRadEKKhoMrV5PBltdWJtsgP1LKhxp2smWlznvugB8zxVZFOE5SKAIKkdPurbqIIBXbwFEZbqZl9PPhqWKz8GozYJkY84KiiWElDX4cgwMOqE46tBLRorZzLOFFXFBKtr4i3ohrE_t45iLDLYYqPNLPt7VralM_Bsq1kdedsDh0wuiAxKwSTiebPPD15nL2c12_mFbR2QJxHHNuqd19Zr21UADxf3TjWpHIf7Vx5YLQukw2fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e40882f729.mp4?token=RHM4mhrmn6BHkQJWgwyeDJXg_zidmuqbebWMOIl0-V5ruuezY75sKpIbE1q3cAIPYHnAdcoG3fecIHltgLE3Sed0eJUXiDbsBHHtUwRadEKKhoMrV5PBltdWJtsgP1LKhxp2smWlznvugB8zxVZFOE5SKAIKkdPurbqIIBXbwFEZbqZl9PPhqWKz8GozYJkY84KiiWElDX4cgwMOqE46tBLRorZzLOFFXFBKtr4i3ohrE_t45iLDLYYqPNLPt7VralM_Bsq1kdedsDh0wuiAxKwSTiebPPD15nL2c12_mFbR2QJxHHNuqd19Zr21UADxf3TjWpHIf7Vx5YLQukw2fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا، و سرگئی لاوروف، وزیر خارجه روسیه، در حاشیه نشست وزیران خارجه اتحادیه کشورهای جنوب شرق آسیا (آسه‌آن) در شهر پاسای در مانیل فیلیپین با یکدیگر دیدار کردند.
🔴
روبیو پیش از این دیدار، با اعلام آنکه واشنگتن به دنبال ایفای نقشی سازنده برای پایان دادن به جنگ است،‌ اعلام کرده بود قرار است درباره جنگ اوکراین با همتای روس خود گفتگو کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/136870" target="_blank">📅 09:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136869">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سپاه: یک انبار بزرگ تجهیزات نظامی، یک سامانه پدآفندی پاتریوت و یک آشیانه پهپادهای MQ۹ آمریکا در پایگاه هوایی علی السالم را با حمله پهپادی منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/136869" target="_blank">📅 09:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136868">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLko3UsTn65qHeJ0QeR63qFvROfmc_FVbybEibGvKGPcELgtfV1ZskSjIxa3jHslBUr4IIx6yXZmp8j0yIJoj2mqmRcxGxg-fvWOE2eRgwaxDtkQAsVdldcZEZuLbKipIJE4Mp3-fGtWCF8FsnJeKmSvKCZKXvJAchgfXLCmh1vA_j-WG1bFrWWu7HMEc6pTzuP1iKdZi5UIiegMc5AuZOMruA--YQ7SemznmipHtngFZNMMu-LjE0XjD0IbO-RzaSrCrw4GavC_NgwWBPLi2gQafwLp-aZ1mkWGzZ3W0cqKWCvH1Q-kzFUn6qrMfBEEYjHHIxcs0l7MZH2YCYu9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مسئول آمریکایی:در این ماه، ۱۲ سرباز به شدت مجروح شدند. این جراحات ناشی از حملات موشکی و پهپادی ایران در اردن و کشورهای دیگر بود. به طوری که این سربازان به دلیل شدت جراحات، با هواپیما به یک بیمارستان نظامی آمریکایی در آلمان منتقل شدند تا تحت درمان قرار گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136868" target="_blank">📅 08:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136867">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
خبرگزاری فرانسه: بعد از اعلام محاصرۀ عربستان سعودی توسط یمن، ۹ کشتی مسیر عبوری خود از تنگۀ باب‌المندب را تغییر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136867" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136866">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
شهر هایی که دیشب مورد حملات ارتش ایالات متحده آمریکا قرار گرفته‌اند
🔴
بندرعباس
🔴
بندر جاسک
🔴
سیریک
🔴
بوشهر
🔴
اهواز
🔴
شلمچه
🔴
رامشیر
🔴
بندر ماهشهر
🔴
اندیمشک
🔴
کرمانشاه
🔴
اسلام آباد غرب
🔴
ابهر
🔴
شدت گرفتن حملات به غرب کشور در دومین شب پیاپی
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/136866" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136865">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwsyDesPDz6uTvq3AB-Z09xV8dtUTCBijM35dfWJcfzPd-_Wk8NxeKs3fv_sctA9z35MpUMS23ERhWaKHA0A6Mk1XEr5D3kgfm3sh-2z_ohdf89q93Cxxlo6qCzSesZkhme85tEFtbu1GWOnArEI1yGBrFdolWOqqVqKOQzdzGDk8K-YvN7hcxYLfjkECs_hUxcga716erIT2H7zOyrZzI4X92dlAcFEnGuAZ0HLaWvhDn33intfKAYRVvlCKqdo78ofUKN0Fl5p7jbQqvFqz8Fnbvot2-yMbpxmlfWWjGgxGu_H6KMvIFNPLloHm1rsY9ZMT-01CxPlDiPeotnzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۹۶ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136865" target="_blank">📅 08:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136864">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سپاه به مردم کویت: آمریکا تمامیت ارضی شما را هتک کرده، نه ما
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136864" target="_blank">📅 08:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136863">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MjHj_Vsm-B2wkv-ZGYz7FPi-aNkOnPwvyx4GSJAv_aQjQu_-LFyQUVukRLmOMnUXPga6-s3BgSbZHXfU-GyJ-f-75vAsi0tbxZ2RYSIy5yn6n9oXU7TZvnmQlPWbvC1JDr2u5IuuIlNv-jMP3QmX57y9h6z8pI7G-Oufsar7QuKBQvfq6SPYCS1dq747e-vrcO-HLSWqYMgufsM3hzGn39e0S55eh2nahHP3QuoadIf4-KYoOYH-SsCuuOhSzEaRcpUhurmjCPgHHcBRKix2v4go9tPd9uec7ttrnWqR13WgwbIv2wMvfoBgAqvSQyFdomwfmPBeNPqiWaZr5rjn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس، با استناد به مقامات آمریکایی، گزارش داد که یک فروند از بمب‌افکن‌های استراتژیک B-1B Lancer نیروی هوایی ایالات متحده، شب گذشته به ایران حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/136863" target="_blank">📅 08:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136862">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
منصور حقیقت پور، فرمانده پیشین سپاه:
اگر آمریکا خارک را بگیرد روزی ۱۰۰۰ موشک رویشان می‌ریزیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/136862" target="_blank">📅 08:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136861">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfBqYg_Zmv6KB8XG515XP3Yb5MvVH7Iyy768h91cU2MsL2nN8a5zSnoo8HQqzQQjppJEg1RFeA9Nxlwtf7RodskSrbtEkPnH3DlMkzmD0ZsznsYjlTjmVzXRxDaHAApk6Aus1ZnAPbs1N1l50yr3RiwsEAol0_TfL6A5FoDx-C-BQmIdcJAChiSiLw1a2O07n5RpvNumTbSe6d_PFhNXOpXtrJlquXi3wLUZpMvEKRYlQe4AInxXvpbtCGW4G7nSyJGeMallMgifwl8C-pa6XZgYCHk_OpHm_s1P_jhVfsQPBgmQXXkgpbPDpyHYl7WZgbs-2JoZEg3a6gjbMHeLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از کتاب «قدرت مذاکره» دکتر عراقچی، کتاب «دیپلماسی ایرانی» نوشته دکتر ظریف رونمایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/136861" target="_blank">📅 07:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136860">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سپاه:
حملات دشمن رو با قدرت بیشتر پاسخ میدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/136860" target="_blank">📅 06:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136859">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/959a8c1fa6.mp4?token=rj5DM17DSLm11EDTUfm0wJv5bQSSRwCLrUYlXMNDBP5gNWMjZgv4wv3dlJ3972lwcdZ6SJHt5LsS-TL4IX5nPjzAwK9eKJUXX3Hr5KyrNGN1WyU3qdqsWiXctrXVBy65HI8PCNnB_YXOuS95XOHd71drGzJj6b33D26ysIbycZtHofIoQbE5OgXls2SO7_72GaOKC2lKafLkbFPAxh3QW8Cf11cuIQM2TWPh0FzgDq6lGTIGjahXBGKf3tn7jH6djoBwblC85NknEF13Vh6WGzEpbFigEWX9-0_SvREi6Y506Fk3s1uyPfzV04oS_gF9hHecvBrUtGPNSWs8jNe-Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/959a8c1fa6.mp4?token=rj5DM17DSLm11EDTUfm0wJv5bQSSRwCLrUYlXMNDBP5gNWMjZgv4wv3dlJ3972lwcdZ6SJHt5LsS-TL4IX5nPjzAwK9eKJUXX3Hr5KyrNGN1WyU3qdqsWiXctrXVBy65HI8PCNnB_YXOuS95XOHd71drGzJj6b33D26ysIbycZtHofIoQbE5OgXls2SO7_72GaOKC2lKafLkbFPAxh3QW8Cf11cuIQM2TWPh0FzgDq6lGTIGjahXBGKf3tn7jH6djoBwblC85NknEF13Vh6WGzEpbFigEWX9-0_SvREi6Y506Fk3s1uyPfzV04oS_gF9hHecvBrUtGPNSWs8jNe-Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سود ۶۷ برابری دولت ایران از واردات BMW
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/136859" target="_blank">📅 06:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136858">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHrORIESa6rG53foPM3v5FOSrx642mKGPXKRdR6JUHOYRejAlam9EDCa5X5UWlJDpFS5DgNLdeAx_jwr4El9z4dOEbDkuggvEli8MOkXnzTuDrb4sjNFlCOTWtZuOkUv6m5hTGcBr4BO49PBBkVvQt_7_jvYxG68Ag0lIfn7tMVQNToe_adaYmwm4jUwFHTJ2kekSgVlGBXWqUHKnXgPxnJ4PyrUz7aD43bfWhHq_tqrmdrEotrWkA6MvFBh98SWHbrrUFqWYIYy_KLbrj6oB4HAb1fdFS7TRyQy_aPIoDNcvkEkfeIdOxoXd5TYES9OYu3EoQNuR5a_OXNcgCE6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/136858" target="_blank">📅 02:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136857">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
مارکو روبیو: توافقنامه با ایران به دلیل نقض تعهدات، دیگر معتبر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/alonews/136857" target="_blank">📅 02:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136856">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مارکو روبیو: توافقنامه با ایران به دلیل نقض تعهدات، دیگر معتبر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/alonews/136856" target="_blank">📅 02:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136855">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
حملات امشب خیلی ضعیف و کم بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/136855" target="_blank">📅 02:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136854">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
بوشهر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/136854" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136853">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9377b3601.mp4?token=W9vNFz4EESAldLkOAR5l24XC30PrQuJizxsiZQ4RCDdVjfm_TrRpBlSfTaj58tjJ6ricv_6i858pM7YL6I0lck66RtLHtDw24N0cCkTQRKfN745gh1hGrbT65iBhPDi1uo8gQq3XJKHMH1AberaLvyQrcI2P7HPAbrDkQcWn8B1Xtf04Y7ndgSpfYL3IsIaADluIH7iOCKE1U6qSEJ5Z7t1I3MFf2cwDUdbFfTPABVY86cVettUZWAiHg4QPCQ1waJjOCyUkHmcr8g68hlZhCS4UdLcBDHvK5XfOMFINhmyF67g1xn_uBKYJqnYZBiV1EzK5z2xPaePLZ5NvuP-83A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9377b3601.mp4?token=W9vNFz4EESAldLkOAR5l24XC30PrQuJizxsiZQ4RCDdVjfm_TrRpBlSfTaj58tjJ6ricv_6i858pM7YL6I0lck66RtLHtDw24N0cCkTQRKfN745gh1hGrbT65iBhPDi1uo8gQq3XJKHMH1AberaLvyQrcI2P7HPAbrDkQcWn8B1Xtf04Y7ndgSpfYL3IsIaADluIH7iOCKE1U6qSEJ5Z7t1I3MFf2cwDUdbFfTPABVY86cVettUZWAiHg4QPCQ1waJjOCyUkHmcr8g68hlZhCS4UdLcBDHvK5XfOMFINhmyF67g1xn_uBKYJqnYZBiV1EzK5z2xPaePLZ5NvuP-83A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجلس نمایندگان ایالات متحده لایحه سیاست دفاعی به ارزش ۱.۱۵ تریلیون دلار را با ۲۱۶ رای موافق در برابر ۲۱۲ رای مخالف تصویب کرد که شامل ۶۰ میلیارد دلار هزینه نظامی اضافی است و انتظار می‌رود بخش عمده‌ای از آن هزینه‌های مربوط به جنگ علیه ایران را پوشش دهد.
🔴
این اقدام که تنها شش دموکرات به آن رای موافق دادند و هفت جمهوری‌خواه به آن رای مخالف دادند، اکنون به سنا ارجاع می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/136853" target="_blank">📅 01:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136852">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فووووووووووووووووری/مجلس نمایندگان آمریکا بودجه 95 میلیارد دلاری تامین هزینه جنگ با ایران رو تصویب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/136852" target="_blank">📅 01:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136851">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k15w0dFNymx4oSsw6NAdeqxiPMYxpFte4YarXPj8Pi4jtd-tjloEfiM6ZAltgzH3syl6WETUZ2iN81FG8cunKUpQ7NxTvIRO_utsXSe9EH1ZXuAOBLyshJffrhuw2CmAkuCm5tkBX2-4AsaBa2pgiwx_rYMWVIOZ-yCKLt2QNVOx8WMRjaltgBRVlR7sVq31IenmBid_dCXf2IpAKsaNElmLbPtyO2aKG5jY8lN8A0YX7ruCR99Yf72Lg_TIuqeqgqbS2RjJvyKMrSf0FXfl7Cohh3SN7aVyDvdJ-QaxinWkuS7OF6hMQBEcYJqqg6B-CH2o-nzcr9e_EPXpFgfA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: امروز ساعت ۵:۳۰ بعد از ظهر به وقت شرقی، نیروهای ایالات متحده طبق دستور فرمانده کل قوا، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند. این مأموریت ادامه خواهد یافت تا توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاری در حال عبور از آب‌های منطقه‌ای را بیشتر تضعیف کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/136851" target="_blank">📅 01:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136850">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
العربیه: ارتش پاکستان هشدار داده است که در صورت هرگونه اقدام حوثی‌ها علیه کشتی‌های پاکستانی، پاسخ لازم را با استفاده از همه گزینه‌ها، از جمله نیروی نظامی، خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/alonews/136850" target="_blank">📅 01:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136849">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=cVEj8zblmoma7_wLpMvk5ZvOV3jRtOwILIUIxgofaUCdFyd2J7PLcx7BNnysNM0G8tE3bRTUrw_HnBFiBTmNFV7h1Epgh-5TYuiVeENI_Qovd8MI_yNg_yTeqQbSnO8fQvyn79tw8HVWVh5lT0OqZk8AenwRVkf73E1xuN9zwjRETmrFtbi6ms-dr55uwSPlPtEJlQvJQxPEice7ukG_SyMx9PmhQEq3QQ0IKVWRKS8lKIQUtp8GyjtVg7HxLwJHbVL6w-pVJajyGXe7iuVDrJYS7D0c3SxabmATljazRIsMeWDaAB-6ynyU9bpmvCoj_ivrgSdBJrfJ8DFVXAns5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=cVEj8zblmoma7_wLpMvk5ZvOV3jRtOwILIUIxgofaUCdFyd2J7PLcx7BNnysNM0G8tE3bRTUrw_HnBFiBTmNFV7h1Epgh-5TYuiVeENI_Qovd8MI_yNg_yTeqQbSnO8fQvyn79tw8HVWVh5lT0OqZk8AenwRVkf73E1xuN9zwjRETmrFtbi6ms-dr55uwSPlPtEJlQvJQxPEice7ukG_SyMx9PmhQEq3QQ0IKVWRKS8lKIQUtp8GyjtVg7HxLwJHbVL6w-pVJajyGXe7iuVDrJYS7D0c3SxabmATljazRIsMeWDaAB-6ynyU9bpmvCoj_ivrgSdBJrfJ8DFVXAns5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت کانالای ایتا وقتی آژیر کویت فعال میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/alonews/136849" target="_blank">📅 01:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136848">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
صدای انفجار در آسمان کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/alonews/136848" target="_blank">📅 01:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136847">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
الان به کویت حمله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/alonews/136847" target="_blank">📅 01:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136846">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
فرماندار بوشهر: یک نقطه در مرکز استان مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/alonews/136846" target="_blank">📅 01:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136845">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
یمن: ۲ نفت‌کش عربستان که سعی در شکستن محاصره داشتند را با موشک و پهپاد هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/alonews/136845" target="_blank">📅 01:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136844">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سیریک رو بازم زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/alonews/136844" target="_blank">📅 01:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136843">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری/ماهشهر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/alonews/136843" target="_blank">📅 01:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136842">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پاکستان به حوثی‌ها هشدار داده است که هرگونه حمله به کشتی حامل پرچم پاکستان یا منافع دریایی پاکستان، «تهدیدی علیه امنیت ملی ما تلقی خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/alonews/136842" target="_blank">📅 01:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136841">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
️12 فروند جت جنگنده یوروفایتر تایفون ارتش سلطنتی بریتانیا جهت حفاظت از حریم هوایی متحد خود، اردن وارد این کشور شدند .
✅
@AkhbareFouri</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/alonews/136841" target="_blank">📅 00:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136840">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlsRgfp7nb7rvnH1KrCyebXk6tHx82cihbF5oPLIL4jjFj_AgXNvW_rt50V4ssSPlj1U4jpgUodsnIFN_BUvcRW_CvyAUW_BfV8PltfUflIswFa52aOm5YSh1R5C4XagXjD9HAiXHimsqRKD2yTDDAfJgIyKTsj-YBeTo9c49R2SajgG56UzINpZDOhLJNzF1Lyp-2AxiLtcI9BSKYOIHXvlHw95yR2c6KPXt5jea8teJiMy8hdgbLAzs6bvMpXSh5VgeuYlfm6QiS_PwQyOdC25OPoWd5IcJZaDt7We_f8xwVXIrYjF4aVWWNiSjT_62q4p19Ufg-uJD4oa98THfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان بین‌المللی امنیت کشتی‌ها (UKMTO) گزارش داد که یک نفت‌کش در فاصله ۷۰ مایل دریایی جنوب غربی الشقیق، عربستان سعودی، توسط یک پرتابه هدف قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/alonews/136840" target="_blank">📅 00:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136838">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
اینترنت ضعیف شده؟
👍
👎</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/alonews/136838" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136837">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
بوشهر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/136837" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136836">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccF_57Syk982El95oFK696QoytwM178zIajuwqkbDLL9NutZRuPQ0eXRO3eNGMkBqNWzK__Xn32K-dzGeyrKyGG-jQiWCxKjuZGKy7j-8YADcFX49nNuAF8-sB-vzoo63IZRJxeqkVULZZ8GTGZR7EjDI5q4UW-8Ff78lXeKM2Y3KcKF_cgQc8UhWpvQhODwE0190uoCBMqwSqWJDwPoNxbG7lTWllzcj7uNJ4U3hqB63sBx60LaUh2cqX1_y6iGSc7jwPiukuZLX54dzv04JPjjJ1lU5YNh9CQNQyU2ZtyI9AkzPzMj_SX0rAEGJm6sTAuXafcI0U5GxYXqe386aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان ایران همانند خودش در انزوای کامل
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/alonews/136836" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136835">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
هدف قرار گرفتن یک کشتی در نزدیکی عربستان سعودی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/alonews/136835" target="_blank">📅 00:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136834">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پایگاه موشکی چمران رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/136834" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136833">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
یه سوله انبار آسفالت تو اطراف رامشیر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/136833" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136832">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پایگاه دریایی سیریک رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/136832" target="_blank">📅 00:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136831">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
لشکر ۷ زرهی ولیعصر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/136831" target="_blank">📅 00:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136830">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وال استریت ژورنال:
‏به صورت اضطراری نیروهای ویژه، جنگنده‌ها و بمب‌افکن‌های ارتش ایالات متحده در حال اعزام گسترده به خاورمیانه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/alonews/136830" target="_blank">📅 00:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136829">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚠️
فقط زیر ۱۸سال ممنوع
⚠️
◀️
مشاهده فوری تصاویر</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/136829" target="_blank">📅 00:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136828">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
صداسیما: صدای انفجارهای بسیار بزرگی در اهواز شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/alonews/136828" target="_blank">📅 00:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136826">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ : اون‌ها هنوز برای توافق آماده نیستن، ولی خیلی زود آماده می‌شن
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/alonews/136826" target="_blank">📅 00:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136825">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ca1873d4.mp4?token=pwLq7l-R7Z0xsFBk-uRHQKpI57gNEHqmvhtWkgZebzOrFaKDJkopa104C5YGjEKuED1582-c13unh5QzPNmrB7qkjbkIGzaaGAo3MVSmVChzONZYCwXKGm9bXh570jYJo9ulGrL8vAHhPtIOON4fHVDmrRaRtqe7o7t5-eCfFZJhH6gjpnSQxBTSxYm0qLJwVsMnNPkCU0pzjqE4QKG24uMvg8plievwO22L-JknndCWwFPNvQ7dJFF82XGMqSv1nx1gO3SvShn4vaxMAMqBt18-fWqqoVM0qr0NY2hRsejlWlodbEJhI35bnx4i5LDjc5lYYs6Z2786dn2DqqfTqoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ca1873d4.mp4?token=pwLq7l-R7Z0xsFBk-uRHQKpI57gNEHqmvhtWkgZebzOrFaKDJkopa104C5YGjEKuED1582-c13unh5QzPNmrB7qkjbkIGzaaGAo3MVSmVChzONZYCwXKGm9bXh570jYJo9ulGrL8vAHhPtIOON4fHVDmrRaRtqe7o7t5-eCfFZJhH6gjpnSQxBTSxYm0qLJwVsMnNPkCU0pzjqE4QKG24uMvg8plievwO22L-JknndCWwFPNvQ7dJFF82XGMqSv1nx1gO3SvShn4vaxMAMqBt18-fWqqoVM0qr0NY2hRsejlWlodbEJhI35bnx4i5LDjc5lYYs6Z2786dn2DqqfTqoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری مشاور قالیباف و الله کرم(نماینده طالبان) در پخش زنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/alonews/136825" target="_blank">📅 00:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136824">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
حملات امشب آمریکا شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/136824" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136823">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
گزارش انفجار در ماهشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/136823" target="_blank">📅 00:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136822">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/136822" target="_blank">📅 00:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136821">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommydiplom.ir</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrVC2VJiwKozx2Zlac-g9b6zoAFGH4sQUG3ycVPaTXXzptQuS9IjbBtON4RCfSPzahi35c-g2IagrDraBlcXwyOtn1D8674K96P0EfSv5f4Uf5oYwCrIQOzOhqsiKWq6xjaeOEPMUIHN7SuVsI6nf3jzoME9OFOzYhuhOuFRubFJu6n0JEK512GvKlaU9j7V_EMx9JN4HSGlYXtXABq_i7ZVTghZTQHktX_xzrAy1QmLuqaDmZVBaKAayXA8gD5fWIYK79NFKdAoOhl9Z-4xymtyQrK5WyhE2NEHlUkNlbJnNEigLk7dsZg8Unt3Rmu_KftoT2CShtrmSAt4bpqHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/136821" target="_blank">📅 00:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136820">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بلومبرگ: مقام‌های ارشد سعودی و امارات با انتشار پیام‌های هماهنگ در شبکه‌های اجتماعی، بر روابط دیرینه دو کشور تأکید کردند
🔴
این اقدام پس از تشدید دوباره جنگ [علیه] ایران، نشانه‌ای از هم‌سویی علنی دو کشور تلقی می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/136820" target="_blank">📅 00:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136819">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/136819" target="_blank">📅 00:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136818">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
رویترز: حداقل دو مرکز سازمان سیا در ماه مارس توسط ایران مورد حمله قرار گرفتند
🔴
از جمله پایگاه سازمان سیا واقع در سفارت آمریکا در ریاض و یک مرکز دیگر در شرق عراق
🔴
یک ارزیابی داخلی سازمان‌های اطلاعاتی غربی به این نتیجه رسید که احتمالاً روسیه در این حملات نقش داشته است. دو مقام غربی که در جریان این اطلاعات قرار داشتند، گفتند که حمله به سفارت آمریکا در ریاض با استفاده از دو پهپاد شاهد که فناوری روسی در آنها به کار رفته بود، انجام شد.
🔴
برخی از مقامات معتقدند که روسیه همچنین به ایران کمک کرده تا دقت پهپادهای شاهد-136 خود را با ارائه سیستم ناوبری ماهواره‌ای کومتا-ام بهبود بخشد. کارشناسان می‌گویند که این سیستم به طور قابل توجهی دقیق‌تر و دشوارتر از سیستم داخلی ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/136818" target="_blank">📅 00:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136817">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
یمن: در صورت آغاز جنگ علیه غزه، فوراً وارد عمل می‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/136817" target="_blank">📅 00:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136816">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
در پی دستور رئیس‌جمهور برق صنایع با هدف جلوگیری از توقف تولید، حفظ اشتغال و پیشگیری از بیکاری در مرداد و شهریور قطع نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/136816" target="_blank">📅 00:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136815">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S26_HkK3kBSX2PUSibtvkt5sI3iw6HZGmAL_hIGBTWDvpQfuCBBI7V3qJdxZo65svBiFXrfCOLQGayPmUJUqnTcLEzAfrcHnjTgEOdq-xJVAL5pvYQX5hzf58Uhl_wn70n11x65UTJENqZqwEmUl_g88zFvb4A4Xdq3c_p0ntUzmXpxXywU05vlY8zjGhKltotWI-1tIj82C_EXuYGQZ1Vz1hkc1ospwcRdf4DhWQ5wiov3sQsIOUZLvbuTQBuiTea8RwT7hQerReYWEJ_BCffdn9ZJeHnpY1eOM5_HaGipi0MXQlkwsmRRcfkbi73Jhxw54hQxYiHvmenjrXMNXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: منابعی در ایران می‌گویند که پرونده کوه کلنگ (کوه تبر) طبق روایت اسرائیلی و موساد در مورد این تأسیسات هسته‌ای، با هدف تأثیرگذاری بر تصمیم‌گیرندگان سیاسی در واشنگتن، مدیریت می‌شود.
🔴
برخی منابع می‌افزایند که در صورت هرگونه حمله، اسرائیل از هرگونه پاسخ ایران در امان نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/136815" target="_blank">📅 23:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136814">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مقام کاخ سفید: امکان دستیابی به توافق با ایران وجود دارد
🔴
استیون میلر، معاون رئیس دفتر کاخ سفید در امور سیاست‌گذاری در گفت‌وگو با شبکه فاکس نیوز ادعا کرد که ترامپ برای تحقق هدف واشنگتن مبنی بر پایان دادن به «تهدید هسته‌ای ایران»، تمام گزینه‌های لازم را بررسی و در صورت نیاز دنبال خواهد کرد.
🔴
معاون رئیس دفتر در امور سیاست‌گذاری کاخ سفید مدعی شد که جمهوری اسلامی ایران در طول ۴۷ سال گذشته «با مصونیت کامل» دست به «اقدامات خشونت‌آمیز و کشتن آمریکایی‌ها» و حمایت از گروههای مقاومت در منطقه و جهان کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/136814" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136813">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
بلومبرگ: مقام‌های ارشد سعودی و امارات با انتشار پیام‌های هماهنگ در شبکه‌های اجتماعی، بر روابط دیرینه دو کشور تأکید کردند
🔴
این اقدام پس از تشدید دوباره جنگ [علیه] ایران، نشانه‌ای از هم‌سویی علنی دو کشور تلقی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/136813" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136812">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کانال۱۲ عبری: پاکستان و قطر به طور فعال در تلاش هستند تا آمریکا و ایران را مجدداً به میز مذاکره بازگردانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/136812" target="_blank">📅 23:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136811">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded6599216.mp4?token=pndmuzNfkvMYFnzninK7dCUtFeWQSjGkevvZJ5Tqkfd8T23uTEaMgHWtvPtxCQTveIjwjoSAjfj2EZAccKZKN0i8hetxni1xwj4DsMYQxIz8sxOSj5U1l9KK2-du31jpHC3yFPmAXc79fOjdX9wgHRnYdOYsXsX2OmnghxHgEgtLBLEPC3C5O69DcNABaAaV_HB_oDQ2xXPZHvdimXe4PdoKaYeXcPfWr4XDeaDEVa2xuCasMA4hEOAWY4DaQJ2wDcZIKErnWI3HMotDUpUEPLYMyH9LgUNmXS0GMSd8aqeRQBNrefEmdKtkVB8fS-bKCgExdSEHWdjfW8JgtquIrCtnhNsfK3I6o3DOuHtlNc6KGDZN1z_cQe4XybW6Zza0FH3pisufDNVb_qQzGogcNBsvt3OznHj7T-acX5PmRIK2-8IaxsmrGUcyMseTEJlGzGjZtVE9YYlb6IOTRKxLtOvX7oEMs61atqs_TrmL64KZ4h4W78-YrFMUqoXVmKAJhuSWaum6q1LM2IjFt6kmNf0fhS9gcQc8YaVOqSAzCLUY_pp4nIxq7LTXlpxGUelvI1SRqATEVrkj4cEXH7V4I66CTwIoqYUcQLwl1YeuC6a1zFl5Id1xXg7pgao0mtCn6EapmdhVMHBV69b1eN4cztUgqI5LDZdfITHlFxKlBhs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded6599216.mp4?token=pndmuzNfkvMYFnzninK7dCUtFeWQSjGkevvZJ5Tqkfd8T23uTEaMgHWtvPtxCQTveIjwjoSAjfj2EZAccKZKN0i8hetxni1xwj4DsMYQxIz8sxOSj5U1l9KK2-du31jpHC3yFPmAXc79fOjdX9wgHRnYdOYsXsX2OmnghxHgEgtLBLEPC3C5O69DcNABaAaV_HB_oDQ2xXPZHvdimXe4PdoKaYeXcPfWr4XDeaDEVa2xuCasMA4hEOAWY4DaQJ2wDcZIKErnWI3HMotDUpUEPLYMyH9LgUNmXS0GMSd8aqeRQBNrefEmdKtkVB8fS-bKCgExdSEHWdjfW8JgtquIrCtnhNsfK3I6o3DOuHtlNc6KGDZN1z_cQe4XybW6Zza0FH3pisufDNVb_qQzGogcNBsvt3OznHj7T-acX5PmRIK2-8IaxsmrGUcyMseTEJlGzGjZtVE9YYlb6IOTRKxLtOvX7oEMs61atqs_TrmL64KZ4h4W78-YrFMUqoXVmKAJhuSWaum6q1LM2IjFt6kmNf0fhS9gcQc8YaVOqSAzCLUY_pp4nIxq7LTXlpxGUelvI1SRqATEVrkj4cEXH7V4I66CTwIoqYUcQLwl1YeuC6a1zFl5Id1xXg7pgao0mtCn6EapmdhVMHBV69b1eN4cztUgqI5LDZdfITHlFxKlBhs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کمونیست‌ها می‌خواهند مجسمهٔ راشمور را تخریب کنند. آن‌ها قبلاً هم تلاش کرده بودند تا این مجسمه را تخریب کنند.
🔴
آن‌ها می‌خواهند آن را منفجر کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/136811" target="_blank">📅 23:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136810">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ :  آنها از کلمه‌ای استفاده کردند – اولین باری که آن را شنیدم – که توسط دموکرات‌ها ساخته شده بود: «دسترسی‌پذیری».
🔴
این کشور در حال پیشرفت و تحرک است.
🔴
سرمایه‌داری آمریکایی همیشه به درستی اجرا نمی‌شود، اما وقتی به درستی اجرا شود، هیچ چیز مانند آن نیست.
🔴
گروه‌های چپ‌گرا و رادیکال در تلاش هستند تا آینده فرزندان ما را با فاجعه‌ای به نام کمونیسم نابود کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/136810" target="_blank">📅 23:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136809">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c650eb82b9.mp4?token=iHM0dKxzithJGEDNbd4ISp84KaXW19v4VK58XMzPz62irEETuXvyYuytMsJtcQ8KY-MG6TVQqrScWSApxSW9BT1yLyhoNU8MnzXMBW10xsJ8toWaNAEhI1UYTJRxBdx0BUnnC57NOL5e4LAtb1tMC3HgxV16TRzL5ke3JmUCd9jBgHnlnAKgbH5LnfHqHUIT-ICTAmEUnAP2I7eTFB6K7715COIN8_zR7W6GOW3ZOlFVdYZzVF4O6nU4vZDUOGdpotn-6w8MxzHH8KA8hRQvGo6U42PDN9JWSzycYl490FQJekmX3U333oUNGNJAUswIWvSsU-vNk2W3P2iidRerBzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c650eb82b9.mp4?token=iHM0dKxzithJGEDNbd4ISp84KaXW19v4VK58XMzPz62irEETuXvyYuytMsJtcQ8KY-MG6TVQqrScWSApxSW9BT1yLyhoNU8MnzXMBW10xsJ8toWaNAEhI1UYTJRxBdx0BUnnC57NOL5e4LAtb1tMC3HgxV16TRzL5ke3JmUCd9jBgHnlnAKgbH5LnfHqHUIT-ICTAmEUnAP2I7eTFB6K7715COIN8_zR7W6GOW3ZOlFVdYZzVF4O6nU4vZDUOGdpotn-6w8MxzHH8KA8hRQvGo6U42PDN9JWSzycYl490FQJekmX3U333oUNGNJAUswIWvSsU-vNk2W3P2iidRerBzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران و تنگه هرمز گفت:
ما به تنگه‌ها نیازی نداریم. ما به هیچ‌چیز از این نوع نیاز نداریم.
🔴
اما این کار را انجام می‌دهیم، چون مجبوریم انجامش دهیم؛ چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/136809" target="_blank">📅 23:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136808">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c74afdfe5.mp4?token=ZRYJkWYOfbqN2EfGqb_p4nQl_Bf5F4ZubJnidF2fxHQ1UNxCiIqQ8DCSmhNoRlnbZdfjp6RQHO8nAsdzwnZaK6Y9PIykjf2efQEJHRpm0yqU3zbxPgdDuEM8gHveF2hRsTSz4qvrHV2JK9wKIp-CSBrUhQbmkezaT_rxhByvRvPraT0KXgYtQeeDMoTe9d38iNfGVk9_RatQXKzItG2qWm8rowvZ3DvZgpH0Kt6iR1gBXpFLzA22ml9ZuFmQny2Xixr8Ws234eWpiLYFEm5a51PvfRiUSDTqqiC7jZJ1rcQqUu0ihzzx8RVwAhXfi2_tM85fCTEArcC9MPUsptY2Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c74afdfe5.mp4?token=ZRYJkWYOfbqN2EfGqb_p4nQl_Bf5F4ZubJnidF2fxHQ1UNxCiIqQ8DCSmhNoRlnbZdfjp6RQHO8nAsdzwnZaK6Y9PIykjf2efQEJHRpm0yqU3zbxPgdDuEM8gHveF2hRsTSz4qvrHV2JK9wKIp-CSBrUhQbmkezaT_rxhByvRvPraT0KXgYtQeeDMoTe9d38iNfGVk9_RatQXKzItG2qWm8rowvZ3DvZgpH0Kt6iR1gBXpFLzA22ml9ZuFmQny2Xixr8Ws234eWpiLYFEm5a51PvfRiUSDTqqiC7jZJ1rcQqUu0ihzzx8RVwAhXfi2_tM85fCTEArcC9MPUsptY2Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور: ما یک مرکز نظامی فوق‌العاده در کاخ سفید در حال ساخت هستیم.
🔴
این یک سالن رقص است، اما همچنین یک مرکز نظامی بزرگ نیز هست. یک پایگاه پهپاد در بالا و چیزهای فوق‌العاده‌ای در زیر آن
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/136808" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136807">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W69vEk39WpbOifVutD3Vupglm_uvWBrVKxeWbiB6DEZhp3eKpY9aBY5TE8_R7LT4JJWxRrtRcqI0nxpXF0K0JrZK5tIeFWCWzVq0nwk_cmJTH_sgbWX83FJqCXTpvbw3iOfUqa0bobrjRJwzn8rGgryX2C3N110jgUaNXJFjhx4bzWVcOz8bH_KqU9k3VcCFF8oAlX3sbYTz15o5ahOngHEswddaRfB02hqVzTHDpBuADTHGypjlW5WcIN4k_W0b_1nGaZLq06ol3-ouCjLInsRncgnndQ7vkqM0McMf4YDQayXi_EBKv2JcfwDy5lw9XpgJhptF1KVU4qHkpqX9pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ایران تنگه هرمز را کنترل نمی‌کند. این مسیر آبی بین‌المللی علیرغم تهدیدها و حملات سپاه پاسداران باز است. کشتی‌های تجاری همچنان با پشتیبانی نظامی ایالات متحده از تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای آمریکایی به عبور بیش از ۹۰۰ کشتی از تنگه کمک کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/136807" target="_blank">📅 23:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136806">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سفرای پاکستان، عربستان و چین در. ایران در محل سفارت اسلام‌آباد در تهران دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/136806" target="_blank">📅 23:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136805">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd1d57aa35.mp4?token=KL0wzmj8jwTlL_UMw59NuhGkdrMlBFDmVx0Mf1EIbliX8S67EYrBVaqRVwVulsfOZWsBRb5E4CWEknVq6MugL64_zcj2bqMOtNUVr3FHSGPjKwFIaGHLK-PxKI_obtcO6EX8BjvX5tb1cF_V3OrBd2A8DO-CCqBtrieHddSoj84O8oF4D4cZ7mGIYsiG0TMupzRCBVuWHVMgJHxOCGvqbkGPRRm5owQURquC7IpfXAjqmuEmlnt_X0tBjUweJhh1QQZkl4uC1ZodiskQTv4vyIXuny9-jOO5393gmVWdk8K6F1LyR6lW4K2fxreQnchKJBLw9Ac_eaT6Hxrh3M8mh4EVlVCbZeF7WFFstIsUtUew70LEuEDdgdHTcLQMRYx301NkyuhAIuMAV6TDvzxrULzYbE_HU9t9sn4W_26iwTQmHpMtuefg9fKCDnFw4HM7IUmWFjyALl6TloALaTXO-Ch9qida8Qnq5rDLulhyyLIwtiQfgeEIgrRKHWjwoJJNNIp-802RjLz9u5Qv0GGslWF9rNJWUiw4PzhdXE6oOsRUrdMalIW9y6KbTdwU6fbjA59B-O7YT6bweKyK-EXh8OtMGXtTK_Z_x0Z9dRlD9h01g-dchTVK143YyEYG7ONj6OcKVi9H1gwLSb99-SA_NSb87w6ADCKQuoLiHjoaDec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd1d57aa35.mp4?token=KL0wzmj8jwTlL_UMw59NuhGkdrMlBFDmVx0Mf1EIbliX8S67EYrBVaqRVwVulsfOZWsBRb5E4CWEknVq6MugL64_zcj2bqMOtNUVr3FHSGPjKwFIaGHLK-PxKI_obtcO6EX8BjvX5tb1cF_V3OrBd2A8DO-CCqBtrieHddSoj84O8oF4D4cZ7mGIYsiG0TMupzRCBVuWHVMgJHxOCGvqbkGPRRm5owQURquC7IpfXAjqmuEmlnt_X0tBjUweJhh1QQZkl4uC1ZodiskQTv4vyIXuny9-jOO5393gmVWdk8K6F1LyR6lW4K2fxreQnchKJBLw9Ac_eaT6Hxrh3M8mh4EVlVCbZeF7WFFstIsUtUew70LEuEDdgdHTcLQMRYx301NkyuhAIuMAV6TDvzxrULzYbE_HU9t9sn4W_26iwTQmHpMtuefg9fKCDnFw4HM7IUmWFjyALl6TloALaTXO-Ch9qida8Qnq5rDLulhyyLIwtiQfgeEIgrRKHWjwoJJNNIp-802RjLz9u5Qv0GGslWF9rNJWUiw4PzhdXE6oOsRUrdMalIW9y6KbTdwU6fbjA59B-O7YT6bweKyK-EXh8OtMGXtTK_Z_x0Z9dRlD9h01g-dchTVK143YyEYG7ONj6OcKVi9H1gwLSb99-SA_NSb87w6ADCKQuoLiHjoaDec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره ایران:
من این را یک درگیری کوچک می‌دانم. ما یک درگیری کوچک با جمهوری اسلامی ایران داریم.
🔴
آنها به شدت تحت فشار قرار گرفته‌اند و می‌خواهند به توافقی برسند، اما من می‌گویم که آنها هنوز برای توافق آماده نیستند.
🔴
آنها هنوز برای توافق آماده نیستند. آنها به زودی آماده خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/136805" target="_blank">📅 23:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136803">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a974815af.mp4?token=qZV8l1bqHjwR-VULE9WBt-HxuuehiwFKnEW_GVGbXMqcI2CeufIacDl_SAdn1TqwA_ggTqNIk3QEgqDz2S4-laydCRESuvtZiIu7TPaF2bozngjpfFcxCEWvlmvP7540IgK1rvfqDdg1wB15I2KKdhhq5Db-Lk843LpHBN_u4aYv_UP2xl-SujrcBkrm56d62RpDPb6YJEGECh4Giu1SORT1ulWPdjFpQbA_J7LxHlat2RtvP2mwu3Z_iW1HOKh0F0FaViVLzRwVopYGkfFj0Ln8WM1wOOY0-z1NZGx1NZVYGrVAhKBQmSc_A3uyJmlr-JZ3vzjMJWT2VUSBSooCAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a974815af.mp4?token=qZV8l1bqHjwR-VULE9WBt-HxuuehiwFKnEW_GVGbXMqcI2CeufIacDl_SAdn1TqwA_ggTqNIk3QEgqDz2S4-laydCRESuvtZiIu7TPaF2bozngjpfFcxCEWvlmvP7540IgK1rvfqDdg1wB15I2KKdhhq5Db-Lk843LpHBN_u4aYv_UP2xl-SujrcBkrm56d62RpDPb6YJEGECh4Giu1SORT1ulWPdjFpQbA_J7LxHlat2RtvP2mwu3Z_iW1HOKh0F0FaViVLzRwVopYGkfFj0Ln8WM1wOOY0-z1NZGx1NZVYGrVAhKBQmSc_A3uyJmlr-JZ3vzjMJWT2VUSBSooCAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در سخنرانی خود در جورجیا گفت: همه‌جا موضوع تراجنسیتی‌ها مطرح شده بود.
🔴
مردانی که در مسابقات ورزشی زنان شرکت می‌کردند، همه‌جا را به‌هم ریخته بودند.
🔴
تمام دنیا به ما می‌خندید.
ما در سراسر جهان به یک مایه تمسخر تبدیل شده بودیم، اما دیگر این‌طور نیست؛ دیگر به ما نمی‌خندند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/136803" target="_blank">📅 23:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136801">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/714c9598a5.mp4?token=A2DA-I2r9kJdhV7XXhsRONDDc56ymgcYOGZyqiP2mTr7nTIDa9GR1Yhb6qAuNJKNEghA5I0N9jhlTj_MZ6XmneevAnqk4gNyvVqbftWkNuSngDDUJaYreb2OtBWXgcp67QfdHMMGzzrORQ6rPbD7ZWkE6tTrQYSNQ__EavONFLJ9ei1fPqQw--PjahUjZGW3wcOlzc2Fb8AFFBT4FK0pvvPQEGn7gVGSennVifbzEDUaHfRX4x7SPkwA2Iy824Wf3X0AA5nDXB-sKARTYPrGtrCaPDbamdPsqs_6iJZtd0hGo3KUIf6KJmIz03uOUD4OokVB_QYnPa2TRWWsymBVNAWi57Mv57LnnHE273O7T6zyjOc0hpmr3PtjornuNMoEDmvexsikewJ5am41De_VTasCboR52iszkBcK2Jh9c83ua4gYXj4gad6iRJ_VU3B8kkYftmGOkvmFBnsYNf4Kl4RSbj9f0kW-ptsDsC3hFQJkm1QTqeT7zAVH1YTOwp7flzwnFNZ7NuQqT6K2yqQ21r0Dv3Icq07JN3O6uo2hi7aYZfwNSuycGHKZ28sMLH_uZP3svkrimJ_snqNTPh1TOPLDMferk8THjw8LERlQ_33jq0GP0uzrAe7xtA6zyoHPHtH3SYew0LkBTZdC5KuNK3f6ZpvZf6Ry5BC_vq2iH-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/714c9598a5.mp4?token=A2DA-I2r9kJdhV7XXhsRONDDc56ymgcYOGZyqiP2mTr7nTIDa9GR1Yhb6qAuNJKNEghA5I0N9jhlTj_MZ6XmneevAnqk4gNyvVqbftWkNuSngDDUJaYreb2OtBWXgcp67QfdHMMGzzrORQ6rPbD7ZWkE6tTrQYSNQ__EavONFLJ9ei1fPqQw--PjahUjZGW3wcOlzc2Fb8AFFBT4FK0pvvPQEGn7gVGSennVifbzEDUaHfRX4x7SPkwA2Iy824Wf3X0AA5nDXB-sKARTYPrGtrCaPDbamdPsqs_6iJZtd0hGo3KUIf6KJmIz03uOUD4OokVB_QYnPa2TRWWsymBVNAWi57Mv57LnnHE273O7T6zyjOc0hpmr3PtjornuNMoEDmvexsikewJ5am41De_VTasCboR52iszkBcK2Jh9c83ua4gYXj4gad6iRJ_VU3B8kkYftmGOkvmFBnsYNf4Kl4RSbj9f0kW-ptsDsC3hFQJkm1QTqeT7zAVH1YTOwp7flzwnFNZ7NuQqT6K2yqQ21r0Dv3Icq07JN3O6uo2hi7aYZfwNSuycGHKZ28sMLH_uZP3svkrimJ_snqNTPh1TOPLDMferk8THjw8LERlQ_33jq0GP0uzrAe7xtA6zyoHPHtH3SYew0LkBTZdC5KuNK3f6ZpvZf6Ry5BC_vq2iH-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در ایالت جورجیا با شوخی گفت:
من اینجا هستم تا نامزدی خودم را اعلام کنم...
🔴
شوخی کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/136801" target="_blank">📅 23:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136800">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630fb8e1e5.mp4?token=M7Yf9C3K5Gp3lk7W7stXF6sSv8K4xORBFrBDRA2_tWoumA8qwIH6bJzPsGmgjY_LiaENn-HJsmJrNSqXPr0ERrNCqNOzxtPVF0jSJYrtaVVvje_4IOHtuFlZbVxMtSzNQlXea4hEOWWN_QmOEYhY7r2lDeRT57804VT374BfeC0bHXa2kwgkdEMIJjx7bulFBw9d4H7ah4LJdtjVU1EPtoDnSLoiChjcaXATWDDBRwehH73cLtl1ihWp8-SmCKyNDuRPp-iBtWHmtEWJs-kv6rfC42QZxvPCZO2RlJd9z-vEI_zIwkRCT4s2jkT7EeVC-fkLzo1gbDJj7rpACtS0KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630fb8e1e5.mp4?token=M7Yf9C3K5Gp3lk7W7stXF6sSv8K4xORBFrBDRA2_tWoumA8qwIH6bJzPsGmgjY_LiaENn-HJsmJrNSqXPr0ERrNCqNOzxtPVF0jSJYrtaVVvje_4IOHtuFlZbVxMtSzNQlXea4hEOWWN_QmOEYhY7r2lDeRT57804VT374BfeC0bHXa2kwgkdEMIJjx7bulFBw9d4H7ah4LJdtjVU1EPtoDnSLoiChjcaXATWDDBRwehH73cLtl1ihWp8-SmCKyNDuRPp-iBtWHmtEWJs-kv6rfC42QZxvPCZO2RlJd9z-vEI_zIwkRCT4s2jkT7EeVC-fkLzo1gbDJj7rpACtS0KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درمورد قاچاق مواد مخدر:
به نظر من، افرادی که تلاش می‌کنند مواد مخدر را از طریق دریا وارد کنند، شجاع‌ترین افراد تاریخ هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/136800" target="_blank">📅 23:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136799">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ:
ما به تنگه هرمز نیاز نداریم و اگر هم اکنون آنجا هستیم چون مجبوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/136799" target="_blank">📅 23:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136798">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EDY6CnBb8oHVenEVeZWbDRTjpiXgN7lWMRF2Ky-wNgzf5NqG5BMmPmbsQ3mseGc1W6btAd4AG75Ti1NBnVOsNMSli7s8RpR23ofxPzu9m5qel8f2QjIXFJfObYjV3h5LmPdT_SiLuj04Kmpvn674LIcnWnxS766fc01NdVxs82ABdNkbr_cD9bW5SRAZ62I3E7uUzVHf3_wT0vHgxzCvLeAPQIwKERmjTQkD9xGtCcjlJjkFYq8WjXM8L_2SghvwFndQPDsozPfJZ5vBZAQjNv8kDVM013jYvFJPRClwwHHzgu-olMyuyj7oMkGQ49gamZ8QA2-pxUTgVd6NOQ2NiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفعه قبلی روباه پیر(بریتانیا) ۱۵ ساعت قبل جنگ این هشدارو داد:
🔴
۲۷ فوریه ساعت ۱۸ هشدار
🔴
۲۸ فوریه ساعت ۹ جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/136798" target="_blank">📅 23:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136797">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klmNx1xOH40HqnmYF-tSFFjntO1_Ps7ugND4RwYMuaVZ2zibH29PIrlL3VmIWYWU4EbkZkxm71DPtMv44EjqfdQp3U0cG7EnD0niborpNDicx05c7fXA_V4Hyej7D_X2Ky318uPD3qKnLe0sBLs6QdqPLuzcgL22u9c3VX2zE61lyBdrX2luP_wgfeNbgi6rSgiKEb5_FYYfAAuFozZrtM-P04FqYT2_3egBK5pcQWZoFcKwMdtSc9D0yw3DEeFuRAV_DLlBKOKNq3CjLPDrpRO3gLX_7ZFcHa-mTFDWJZeUs5u6jjs2pP3OQIFBgP2fol_oL5Y54oKhkeHbc9x-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیر نویس عجیب صداوسیما:
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/136797" target="_blank">📅 23:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136796">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">💢
فوووووری/برای اولین بار در 2ماه گذشته 4 هواپیمای آواکس درحال پرواز بر فراز خاورمیانه هستند
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/alonews/136796" target="_blank">📅 23:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136795">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
صدای انفجار در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/136795" target="_blank">📅 23:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136794">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
روزنامه قدس وابسته به سپاه :
وقتشه که این گیم نت ها و این مراکز رو جمع کنید و همشون رو بکنید پایگاه آموزشی برای جانفدایان کشور تا در صورت حمله ی زمینی دشمن آماده باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/136794" target="_blank">📅 22:56 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
