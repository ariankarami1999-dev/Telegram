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
<img src="https://cdn4.telesco.pe/file/KJruVFYI-1redxzGQGWCpkvBkJDqsztibEMbusvAURYLQ2AZKZBHzpSAlk8jW34cU5xiq1GDUqk6uY7QeyyZ9LTRAhtQLDmln8ld_a91o2LL_hB3EohE4STV7nirjOGgJo-8hg5mNAFnCC3Mo7-zAGgft89LurzQn6U2IBG1YzBoJBeZKlzEcp-P6BzorpeCCVVZda0R9BXbz5lzT-WgDMu4UDzT_hu-FgQwDiB6m2wJxJRZv4Dq4F2rnFOzGhjK7Hq2WPMESuv260xBhsrnlIZN08O_zlsc88r2s1NCgSuUz37h7ni_b0jY2xd48IpxHgH4GtrjrM8T4Jy46WqQjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 142K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 01:33:15</div>
<hr>

<div class="tg-post" id="msg-74924">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رئال بازی خودشو برد و یک قدم دیگه به قهرمانی لالیگا نزدیک تر شد
🔥
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/funhiphop/74924" target="_blank">📅 01:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74923">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tarCeFYCl37fhvGFjqnHvCKQdd31l4766HZZolqZep-JnqXTmj4dgsjwDl3q5NRvCxOF7efhBujXB_y8fWOpcuXi00i12ghr7vulboBl-EeQ5AOItDlDPOY9Na_T-i8syhpZMWR2prOIPp8n0kUv8e7E5SwUxkC3ZSYwZSwYPk8D_x1g1c_kKwWg8Kbz9GmuYTzqdkUWfpdw0K8-8QHPDZLwFUiY3gyjnBwv_Mch9fqKl_Fd9orLmFJrA9TkmJfoNE5f1E_59SiYTXrtU1rJ81G3qvILBuvPyv6bSrR1vTobB8_kvHhEKCm8-1sJCjN9qJZvhlq5qx68Kyb3aNJw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار بورس اوراق بهادار تهران در ۷۵ امین روز بسته بودنش رکورد تاریخی‌ای را شکست و با ۲۰ درصد رشد، قله‌ی جدیدی را در تاریخ کشورمان ثبت کرد.
❤️
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/funhiphop/74923" target="_blank">📅 00:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74922">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فاکس‌نیوز:
ترامپ و همراهانش از ترس اینکه مبادا چینیا لپتاپ و گوشی‌هاشونو هک کنن یا نرم‌افزار جاسوسی روشون نصب کنن، همگی از گوشی و لپتاپ‌های جایگزین برای سفر به چین استفاده کردن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/funhiphop/74922" target="_blank">📅 00:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74921">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سی‌بی‌اس:
رئیس سازمان CIA امروز تو هاوانای کوبا حضور داشته و با اعضای دولت این کشور مذاکره کرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/funhiphop/74921" target="_blank">📅 00:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74920">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کان نیوز:
اسرائیل معتقد است که رئیس‌جمهور ترامپ پس از بازگشت از چین در پایان هفته درباره آینده جنگ ایران تصمیم خواهد گرفت.
مقامات اسرائیلی می‌گویند گزینه‌های اصلی مورد بحث، از سرگیری درگیری‌ها یا از سرگیری عملیات نظامی در تنگه هرمز تحت «پروژه آزادی» است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/funhiphop/74920" target="_blank">📅 23:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74918">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">به به  سازمان عملیات تجارت دریایی انگلیس:  گزارشی از وقوع یک حادثه در فاصله ۳۸ مایل دریایی در شمال‌شرق فجیره در امارات دریافت کردیم.  قایق های تندرو سپاه پاسداران یک کشتی را که خارج از تنگه هرمز لنگر انداخته بود را تهدید به هدف قرار دادن و سپس توقیف کردند…</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/funhiphop/74918" target="_blank">📅 23:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74917">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">میگم مگه مجلس تعطیل شده؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/funhiphop/74917" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74916">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ: کوبا بعدیه.  اوه، لطفاً وانمود کنید که من این را نگفتم، لطفاً.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/funhiphop/74916" target="_blank">📅 23:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74915">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عزیزی، رئیس کمیسیون امنیت ملی: پیش بینی کردیم که هرکس که ترامپ رو به هلاکت برسونه، 50 میلیون یورو پاداش دریافت کنه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/funhiphop/74915" target="_blank">📅 23:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74914">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوستان این رفیقمون که چند روزه تبلیغشو میزاریم تا حالا هیچ شاکی ای نداشته، اگه نیاز به کانفیگ دارید بهش پیام بدید ازش تهیه کنید با قیمت خوب
ایدیش برای خرید
@r_downey_jr
ایدی چنلش
@suii_vpn</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/funhiphop/74914" target="_blank">📅 22:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74911">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کان نیوز به نقل از دو منبع اسرائیلی و آمریکایی:
تو هفته اخیر جلسه مهمی بین ارتش اسرائیل و سنتکام برگزار شده و همه منتظر تصمیم ترامپ بعد از پایان سفرش به چین هستن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/funhiphop/74911" target="_blank">📅 22:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74910">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ی زمان اینجا پست جهاد خامنه ای علیه کشور های بیگانه ۶۰۰ تا ری‌اکشن قلب می‌گرفت
یادش بخیر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/funhiphop/74910" target="_blank">📅 22:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74909">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb2vQd4livPirjvdKGbd6YcP3WD00tbw9jGbFK_QwzEnXe3BVkDqGqekqCH69Tf2Jbi9L7UX40C2MdQBHBetOQAuv-F9mOdEECamKI0cZDBVaGgcjg-mfuiYslD8UeDKRctCKVsM-OECrOcGaM7D-oxB_1zOsV3FdGz5hfpxVMyX4F9UQaw-roZ2EnxGIUsmXp4KPssAA_fCd58FVCvD38iBdmFAsOrHVTABybg2YpoX3v2Ow9vRO5F3_63T3a9IsQe332OOgFLMfs_DUsM09QaFFqhWm2eCLhMImKVL1pNdq07tCFXE9doIQiYahOnzwpZFqNeCwIjOkxN7Ll1htg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه نمیدونن یکی از ادمیناش برای پسرعموش ساک زده</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/funhiphop/74909" target="_blank">📅 22:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74906">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftuZ58Za00UfXPUC-L5s_3zvQJKHrb2uDkv8c2pxoq02c6q41mpVpsr77vSd74ISQLDrHI2j4tGHfnDI0Lwy4HEH6vCpZV9H1n0QE2209pb4pOZ85uIibrQwWDvX0DboxgVJO4ONDEigQWsRD_YQ7T9Mh9QEoQl56VHQBBKbBnvLTyVw9in7Ygvl2N_ea1zygXMBu7hezEqw-aptsmcrzIp6IOzBa3CDDetToqC7sPzOIuxWUpmsm050FDDlkzLoVkiIJhPyO_y3lHWKo0F9INm25JwhT_zmxOlLIGTV7UZc4vdPhCkczdt7cMK2wKSzENDgh9oyPuH-qMw_dWcfdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر پسرای توییتر میخوان شات از فان هیپ هاپ بزارن بگن رسانه ی خایه مال
بعد سرچ میزنن میبینن عه؟ ما به نام خلق فعالیت میکنیم
بعد یکم میرن پایین تر میبینن عه؟ علی از پایگاه داره پست میزنه
بعد میان پایین‌تر تر میبینن عه؟ ما کصخلیم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/funhiphop/74906" target="_blank">📅 22:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74905">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9609b2009.mp4?token=bu6wajFcx2s9FwCUBtoUTdjBEh7oO5A2XFPaCIP6WYWal7FxF9EGN6JpIgcGdWmYYLg8rsNHPh6iJmVfS1T4Esbn7AFPaEEDEhuqZ4ki43bvCPSAkG2-vkgKewGrrdbbAoZtcUM_CHKO59LMigHLMy24thIZ8ctcB3baBBAtE-upOx0ES6ZnHyZYcq_HSpGBis7JKp1ATJ3y9JIk6xfo8ixKLkLNJHeiKrz6mWqRJYPP149OoKRCIR56ZvLhGJTm7oxmgjD25x3yZaCR87BsEHr50huFt4it4vkMDSG2vTbRGxmHIQknRTYUY9iUeREZdPRESXcjT7b2-NjA5nkwpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9609b2009.mp4?token=bu6wajFcx2s9FwCUBtoUTdjBEh7oO5A2XFPaCIP6WYWal7FxF9EGN6JpIgcGdWmYYLg8rsNHPh6iJmVfS1T4Esbn7AFPaEEDEhuqZ4ki43bvCPSAkG2-vkgKewGrrdbbAoZtcUM_CHKO59LMigHLMy24thIZ8ctcB3baBBAtE-upOx0ES6ZnHyZYcq_HSpGBis7JKp1ATJ3y9JIk6xfo8ixKLkLNJHeiKrz6mWqRJYPP149OoKRCIR56ZvLhGJTm7oxmgjD25x3yZaCR87BsEHr50huFt4it4vkMDSG2vTbRGxmHIQknRTYUY9iUeREZdPRESXcjT7b2-NjA5nkwpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسان صدا و سیما :
در جنگ ۴۰ روزه زیر ۲۰ درصد از شلیک‌های ما به سمت رژیم‌صهیونیستی بوده است
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/funhiphop/74905" target="_blank">📅 22:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74901">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآقا یاسر</strong></div>
<div class="tg-text">رضا پهلوی یه برنامه معرفی کرد بود ریختم روزانه 500 مگ اینترنت می‌خورد با اینکه نمی‌رفتم توش</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/funhiphop/74901" target="_blank">📅 22:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74900">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوستان کون خودتونو پاره نکنید
بنظرتون کسی که ۳ ماهه روی تلگرامو ندیده براش مهمه  اپی که نصب میکنه به کجا وصله؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/funhiphop/74900" target="_blank">📅 22:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74899">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdXiYeuv_09uU764gD0q5Yug_ZKw9pX2LyjPe5PynEE1HUEVjpvI6dh42sQqJTWkWCTLzoI8d19B2uwygyiXrsofbNycdiB9mE9HSAFi6bLJMG-7SaibNow52y5U3OZVuoqc_R3rbxDmK8VXY-2oTnOpqYD4rkJfsEkm1zSVW_xN9nKskO7Oa0gOjq9POpkOwKQ3jbcUJlv1tI3I_vKK9AiVqYJvWUrsRJGF-QRwah1oZD7aU6KL2zKVjx_T6ag5hoDKKstcqYeaRxy0tpqutXTtr3fS0NqFYZ8_rzDypkidRXo5Kx89eHO0lYmp5MyhWIv0Fa-F9v-zOs4tNA_mJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خایه هام چسبید
مکس تو استرنجر تینگز‌ هستن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/funhiphop/74899" target="_blank">📅 22:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74898">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبرنگار:  همزمان با حضور شما در اینجا و حضور دونالد ترامپ در چین، مسئولان آمریکایی و اسرائیلی تهدیداتی علیه ایران مطرح کردند و گفتند که به محض بازگشت رئیس‌جمهور ایالات متحده، حملاتی انجام خواهد شد. پاسخ ایران چیست؟ دکتر عباس عراقچی:  ما به این تهدیدات عادت…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/funhiphop/74898" target="_blank">📅 21:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74897">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانال ۱۲ عبری به نقل از منابع:  اسرائیل سطح هشدار را به اوج می‌رساند تا برای احتمال از سرگیری جنگ با ایران پس از بازگشت ترامپ از چین آماده شود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/funhiphop/74897" target="_blank">📅 21:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74896">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">باراک حسین اوباما:
ما بدون شلیک یک گلوله برنامه هسته ای ایران را متوقف و 97 درصد اورانیوم آنها رو خارج کردیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/funhiphop/74896" target="_blank">📅 21:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74895">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کارشناس کانال ۱۴ اسرائیل:
رژیم ایران به شدت به پول نیاز داره و در حال انجام تماس‌های مخفی و مستقیم با دولت ترامپه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/funhiphop/74895" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74894">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کانال ۱۲ عبری به نقل از منابع:
اسرائیل سطح هشدار را به اوج می‌رساند تا برای احتمال از سرگیری جنگ با ایران پس از بازگشت ترامپ از چین آماده شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/funhiphop/74894" target="_blank">📅 20:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74893">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اما حقیقت ماجرا چه بود؟  نه صدا و سیما دروغ گفت و نه خبرگزاری ها اشتباه کردند بلکه این خودرو دقیقاً داخل هواپیمای ترابری هرکولس C-130 آمریکایی وجود داشت. یک دستگاه خودروی پارس پلاک ملی داخل هواپیمای ترابری آمریکایی بود تا نیروهای ویژه آمریکا در پوشش مبدل به…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/funhiphop/74893" target="_blank">📅 19:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74892">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDLulrqh7CoMfWIShNfkqPXOCGFSP5qLrF972m9iIMTku4Pa_C5wCfw1Mp9bKdUSJmmKrWjpTe8HGQoNm0BW4vHPIGqxmRfv_hfjTyr3shDle9Tz8UBg3h1YuGjTihyTfOx5_Ir_xi3iUw6k84vRGbaaxd8OvgoBPakgV3nzhU0EExrjYiSJ7wslGSy537qKlGPdkmIjJ-DIWxGF2mTtICKGC7skSYfoSncRvGsGnfqhqhkiZbjZePBSheRFdOWbih28g3VH5iL4Vo8S-JtaeX300jMvtKBZQaa_MhYNxKs1VbObahcxalSCTMFHqM8aDAPYfvghdCp0vOv-W-Wu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال های حکومتی عکس یه پارس که جمجمه توشه رو دارن پخش می‌کنن به اسم هواپیما آمریکایی  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/74892" target="_blank">📅 19:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74889">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اینایی که واسشون پیامک میره اینترنت پرو شما تایید شده بعد بدوبدو میرن پرداختشو انجام میدن در جریان باشید بعد پرداخت برای احرازهویت عکس ممه تون رو هم میخان  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/funhiphop/74889" target="_blank">📅 19:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74888">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اینایی که واسشون پیامک میره اینترنت پرو شما تایید شده بعد بدوبدو میرن پرداختشو انجام میدن
در جریان باشید بعد پرداخت برای احرازهویت عکس ممه تون رو هم میخان
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/funhiphop/74888" target="_blank">📅 19:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74887">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فرمانده سنتکام در کنگره:
مذاکرات حساسی با ایران در جریان است.
وظیفه ما این است که آماده باشیم، و ما آماده‌ایم.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/funhiphop/74887" target="_blank">📅 18:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74885">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-text">اگه سردار سلیمانی زنده بود تا الان یه دوتا گروهک مقاومت تو اسپانیا و فرانسه ساخته بود
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/funhiphop/74885" target="_blank">📅 17:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74884">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وزیر دفاع اسرائیل لامین یامال تصمیم گرفت علیه اسرائیل تحریک‌آفرینی کند و در حالی که سربازان ما با سازمان تروریستی حماس می‌جنگند، به نفرت‌پراکنی دامن بزند؛ سازمانی که در ۷ اکتبر زنان، کودکان و سالمندان یهودی را قتل‌عام، تجاوز، زنده‌زنده سوزاند و به قتل رساند.…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/funhiphop/74884" target="_blank">📅 17:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74882">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cx6s87IZMtSaFJE6KJFpuAfLAwaLqWiuZT6syy_Mk31d8qyE9gW9GmPbWw0xSNRZxkRghLqzGSNGGtyc_VL2299AqCLWLfGxFul-7xvTlj3IjuH6OHZJcJyF5xa3ST7VJppQrW14gwRfpZOhc6t8GLyIOVjaJDzAqLmYl3qhaHDZoitRi3zfRKr1P6OKIEMZskb3H28fe4-mgypSXtThpApDM0oSoBvebcsFp-dtzTolJSW2qyMMMhu3gYJ1TKsuYwZ942R2VfhLM1rASavDg97cLKIi8ZdzdFGeqsfFPhLDuKEkWO4BHSZ62lAiE2gRGoILudq40K6JtIbkUJlqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIkU91NHSDMUDfCv4egrnPn3KG2E3cpYSQsh1tbHzxplsXnhGeQ-ku-P5h41yPMLgczWmXfaXDD6gi-PpQvq7osHwlJy6FRo4x5Q5CDLZLG_f-js-DneQllFEn3iPpCWf2XrmnNgQwNxZosYFmgpyBgQ8i07kCo4eqeOgqoK_5147GzPlAe6OvuqSDxz9AAqkSt12sIAStil3dch3GnAXg1ywRRThLgiShgbjJeYC6hfCKlgcbb2f7-mLKuaQ5IE3KRsSm8o8zH5ll5LmXZ-jNrdq7XMcvFX1QFTCyyvp6BsDQJEQ67Os6E3VkXe3AyjUZxRg6V3Q5gSElaDBPAViw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزیر دفاع اسرائیل
لامین یامال
تصمیم گرفت علیه اسرائیل تحریک‌آفرینی کند و در حالی که سربازان ما با سازمان تروریستی حماس می‌جنگند، به نفرت‌پراکنی دامن بزند؛ سازمانی که در ۷ اکتبر زنان، کودکان و سالمندان یهودی را قتل‌عام، تجاوز، زنده‌زنده سوزاند و به قتل رساند.
هر کسی که از چنین پیامی حمایت می‌کند، باید از خودش بپرسد: آیا این رفتار انسانی است؟ آیا این اخلاقی است؟
من به‌عنوان وزیر دفاع اسرائیل، در برابر تحریک علیه اسرائیل و مردم یهود سکوت نخواهم کرد.
از باشگاه بزرگی مثل بارسلونا انتظار دارم که از این اظهارات فاصله بگیرد و به‌صورت شفاف اعلام کند که جایی برای تحریک، حمایت از تروریسم یا نفرت‌پراکنی وجود ندارد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/funhiphop/74882" target="_blank">📅 17:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74881">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRiOJmP1QDr0kNlrSjT1o-f6cT71zkYxRghf_M7qGbJrI2od-OqRfyYbwxsScEdGwdvI_HsH0j1OT6adSiclmZACwnksW0WJRk5Masfy7gZDgGuZz28ZyYwfRtGTeEoOvYrCeUagJk7npd-lGfkxRd_LHR_8FQlABn1OYbhiWRge2zjbA0qFam5Dz3Mfx6AC5FUk0SnafkygikM2mh3yeMRp6E97GmSBxlV5686IvVlOlcMT2AxOyw5qjOJVI9raXAXHMrZuVZIRBpT9EDPaNo1zgkwh31WA-dl6fQuJwZsgcAePm4Ysq0dvm7FPdvkfYq_L8w5O-b9gZuFNzBancg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/funhiphop/74881" target="_blank">📅 17:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74880">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اگه دنبال کانفیگ با سرعت و قیمت مناسب میگردید از این بات استفاده کنید داره گیگی ۱۵۰ تومن با سرعت خدا میفروشه:  @vipamomamadconfig_bot</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/funhiphop/74880" target="_blank">📅 17:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74879">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اگه دنبال کانفیگ با سرعت و قیمت مناسب میگردید از این بات استفاده کنید داره گیگی ۱۵۰ تومن با سرعت خدا میفروشه:
@vipamomamadconfig_bot</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/funhiphop/74879" target="_blank">📅 17:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74876">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5Jwnh4GcY3b8qlPZFhDNmRKly6XX0Jr5qnGbHNKez1o3TKlt2e_zfuHb5pQMSTtxkIy1QqBu8YBhrgmltdwn3lk-qyVJYL0qJH-_5VPr15w3EOmX5JbjuX6wClPqEyfimq8Vdk4dseidfusZogWGYBg8xhAqjQ3gHFKLkw_-9HUto1YlGeNiSNn-Opav-Nbsr29j9w95fGFuQCld4JhP8IdXYuWn9GwFRNLLGMkrJf5HRKk4wjVjnjhNhvdsNyT39-bmB29ESAJNEuQexjG4cN-j7YHVO8hl-0wCqSroD6YYyFBErPc55AcIpmHjsoasTcQ0L0u59zToCMCpEIKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه آمریکا را قیچی کردیم؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/74876" target="_blank">📅 17:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74875">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به عنوان یک بارسایی امیدوارم که مورینیو سرمربی رئال نشه چون در این صورت رئال دوباره قدرتمند میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/funhiphop/74875" target="_blank">📅 17:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74874">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سنتکام
تا امروز، نیروهای سنتکام ۷۰ کشتی تجاری را تغییر مسیر داده و ۴ شناور را برای اطمینان از اجرای الزامات تعیین‌شده از کار انداخته‌اند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/funhiphop/74874" target="_blank">📅 16:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74873">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si3WNtj62IC1coI6jZzXY7KUdtWiF0Ofo41USymk70vY0StB6yKTNUtnvZ3lDTrTKZj93O2oAFaEoTid2SFG2hO8e_meMe1nx6YLuvdtdC_w0I7I3PJFJIknX8Kbcr6EGqNue9nHZnvPiFh3o5JJ-_MW__ZrnHHX5HybjwD5p3R50QNqdnCJcVCf5-JCgphFrhkHFR7Di1ZZJctzVuHJ1IcZ8_iIH7bgUxCOnUQymN4yV7JSkazo8vVP0q84TaK0671Kh_8H2PZ0e-Zn6t_aZkTUeagzyKD01j-L9cd1DKrVW3MT3yj6z5aQB8x8U2sNcmvgi5OYZb_eQ4eUAH7t1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرهیختگان
خطاب به کارولین لویت : بچه کش مادر شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/funhiphop/74873" target="_blank">📅 16:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74872">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزیر دفاع اسرائیل
ماموریت ما هنوز به پایان نرسیده است.
برای این احتمال آماده‌ایم که شاید دوباره مجبور به اقدام شویم؛ حتی ممکن است این اتفاق خیلی زود رخ دهد.
اگر اهداف موردنظر تأمین نشوند، دوباره اقدام خواهیم کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/funhiphop/74872" target="_blank">📅 16:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74871">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مارکو روبیو
طرف چینی اعلام کرده که با نظامی‌سازی تنگه هرمز یا راه‌اندازی سیستم دریافت عوارض در این مسیر موافق نیست و موضع ما نیز همین است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/funhiphop/74871" target="_blank">📅 16:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74870">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اگه نگران امنیتتون هستید بیایید برید از بات رایگانمون کانفیگ رایگان بگیرید که دیگه بدافزار نصب نکنید  @SonicVPNRBot</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/funhiphop/74870" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74869">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اگه نگران امنیتتون هستید بیایید برید از بات رایگانمون کانفیگ رایگان بگیرید که دیگه بدافزار نصب نکنید
@SonicVPNRBot</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/funhiphop/74869" target="_blank">📅 16:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74865">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یادم باشه یه بدافزار درست کنم اسمشو بزارم شیرو خورشید
نصبش توسط همه تضمینیه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/funhiphop/74865" target="_blank">📅 15:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74864">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اپ شیر و خورشید یک دقیقه باگ خورد شمشیرش شد ذوالفقار
خداروشکر امنه باز
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/funhiphop/74864" target="_blank">📅 15:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74847">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اکسیوس
تیم Donald Trump در حال بررسی گزینه‌های تازه برای افزایش فشار و تنش نظامی علیه ایران است.
به گفته مقام‌های آمریکایی، احتمال دارد پس از سفر ترامپ به چین، تصمیمات جدیدی علیه تهران اتخاذ شود.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/funhiphop/74847" target="_blank">📅 15:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74846">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رویترز
ترامپ از شی جین‌پینگ، رئیس‌جمهور چین، دعوت کرده تا ۲۴ سپتامبر به کاخ سفید سفر کنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/funhiphop/74846" target="_blank">📅 14:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74845">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ
مذاکرات پکن بسیار مثبت و سازنده بود.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/funhiphop/74845" target="_blank">📅 14:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74844">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آکسیوس
ترامپ بین افزایش فشار روی ایران و جلوگیری از رشد قیمت نفت و تورم در آستانه انتخابات گیر افتاده.
در حالی که مذاکرات هسته‌ای متوقف شده، تیم ترامپ گزینه‌هایی مثل فشار نظامی و تشدید اقدامات علیه ایران رو بررسی می‌کنه، اما ارزیابی‌ها میگن ایران توان تحمل فشار اقتصادی برای ماه‌ها رو داره.
یکی از مشاوران ترامپ هم گفته ایران روی نزدیک بودن انتخابات آمریکا حساب باز کرده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/funhiphop/74844" target="_blank">📅 13:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74843">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پاسخ عراقچی به ادعاهای امارات در اجلاس بریکس:
ائتلاف با اسرائیل هم از شما محافظت نکرد.
من در سخنرانی‌ خود نام امارات متحده عربی را ذکر نکردم، به خاطر حفظ وحدت و ترجیح دادم به آن اشاره نکنم. اما در واقع باید بگویم که امارات مستقیماً در اقدام تجاوزکارانه علیه کشور من دخیل بود. زمانی که این تجاوز آغاز شد، آنها حتی از محکوم کردن آن خودداری کردند.
آنها اجازه دادند از سرزمین‌شان برای شلیک توپخانه و تجهیزات علیه ما استفاده شود.
همین دیروز فاش شد که نتانیاهو در زمان جنگ به امارات و ابوظبی سفر کرده بود. همچنین آشکار شد که آنها در این حملات مشارکت داشته‌اند و شاید حتی مستقیماً علیه ما اقدام کرده باشند. بنابراین امارات شریک فعال این تجاوز است و هیچ تردیدی در این باره وجود ندارد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/funhiphop/74843" target="_blank">📅 13:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74842">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چین که چیزی نیست جرعتشو داری برو کره شمالی  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/funhiphop/74842" target="_blank">📅 13:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74841">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">چین که چیزی نیست جرعتشو داری برو کره شمالی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/funhiphop/74841" target="_blank">📅 13:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74840">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پشمام معین میخواد برای همکاری چین و آمریکا آهنگ بخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/funhiphop/74840" target="_blank">📅 13:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74839">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کاخ سفید اعلام کرد دیدار و گفت‌وگوی ترامپ و شی جین‌پینگ «
مثبت و سازنده
» بوده و دو طرف
مذاکرات خوبی
با یکدیگر داشتند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/funhiphop/74839" target="_blank">📅 12:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74838">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آمریکا به چند غول تکنولوژی چین مثل
علی‌بابا،
تنسنت،
بایت‌دنس
و
لنوو
مجوز خرید چیپ‌های پیشرفته
H200
انویدیا
رو داده؛ اقدامی که نشون میده
واشنگتن فعلاً نمی‌خواد جنگ تکنولوژی با چین بیش از حد شدید بشه.
این خبر برای
انویدیا
و کل بازار
AI
مثبته، چون هم
فروش انویدیا افزایش پیدا می‌کنه و هم شرکت‌های چینی می‌تونن مدل‌های هوش مصنوعی قوی‌تری توسعه بدن
.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/funhiphop/74838" target="_blank">📅 12:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74836">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کاخ سفید اعلام کرد در دیدار ترامپ و شی جین‌پینگ، دو طرف بر
حفظ امنیت و باز ماندن تنگه هرمز
تأکید کردند و همچنین برای
گسترش همکاری‌های اقتصادی
به توافق رسیدند
.
طبق این گزارش،
چین قرار است سرمایه‌گذاری‌های بیشتری در صنایع آمریکا انجام دهد
و در مقابل،
دسترسی شرکت‌های آمریکایی به بازار چین نیز گسترده‌تر شود
؛ موضوعی که می‌تواند روی معادلات اقتصادی و تجاری جهان تأثیر مهمی داشته باشد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/funhiphop/74836" target="_blank">📅 12:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74835">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یک مقام کاخ سفید اعلام کرد
آمریکا و چین
در موضعی مشترک تأکید کردند که
ایران نباید تحت هیچ شرایطی به سلاح هسته‌ای دست پیدا کند.
این اظهارات در حالی مطرح شده که
تنش‌های سیاسی و مذاکرات
مرتبط با برنامه هسته‌ای ایران همچنان زیر ذره‌بین قدرت‌های جهانی قرار داره.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/funhiphop/74835" target="_blank">📅 12:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74833">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3a3103e12.mp4?token=rseO7r5y6HBUf8jYbSfG_a5fzJ9VtxnZ5iN9XLmu_btXbrBIZ3WWiIK1eERDCJoo4aQBzm5mU1mQgZMBYwAX9ywD2KHaN4jpIhwWM2xH1v_XBtiO7hpxVlaatt8ZS_-C_hnva4Yf0EnXN7fJKyzQU3SeCozWH703bsQYZtWC0fbtoeCQyqjs1JKb86v0suypgbp1Te5GaG3D75PG9DSjKazq80ArC20ehbiBT5kC5nKPEwV3bWflwUo4wFUy3lv0B_oJc8V1Y1fZVVj3YztpHH5s-u8SfhTByrRT62plCDaVnp8Obyfdg617_zt3fqD20OWsdHW7-96EDgj556uaUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3a3103e12.mp4?token=rseO7r5y6HBUf8jYbSfG_a5fzJ9VtxnZ5iN9XLmu_btXbrBIZ3WWiIK1eERDCJoo4aQBzm5mU1mQgZMBYwAX9ywD2KHaN4jpIhwWM2xH1v_XBtiO7hpxVlaatt8ZS_-C_hnva4Yf0EnXN7fJKyzQU3SeCozWH703bsQYZtWC0fbtoeCQyqjs1JKb86v0suypgbp1Te5GaG3D75PG9DSjKazq80ArC20ehbiBT5kC5nKPEwV3bWflwUo4wFUy3lv0B_oJc8V1Y1fZVVj3YztpHH5s-u8SfhTByrRT62plCDaVnp8Obyfdg617_zt3fqD20OWsdHW7-96EDgj556uaUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با نحوه دست دادن همیشگی خودش خواست شی رئیس جمهور چین رو به سمت خودش بکشه ولی شی خیلی محکم سرجاش واستاده بود و ترامپ موفق نشد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/74833" target="_blank">📅 12:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74829">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هاردن چه مادری از دیترویت گاییده</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/funhiphop/74829" target="_blank">📅 12:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74828">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryFgPN6JFs0bg_ANd6x9lDES89GzzdkW7A5MIZsQV0CwOZJYhLwVL-kxT9dpgri_Gq7G9QyweBuRFRVSJTOwepyR0dsOMOaYdS_F6ivgrjctkvxif31iJ6PnewowxnrFzcZSZd29VT9tvbGMjxdBfU3OGszfibY_SwLpPx6FdeKzJp5Jzam1PTJwXjAF_CaRUnb3S8W0aDx4G5DJQUpPpr4oNbD8KzcUNNWJ7QqX1B-KO6HR4hjh0RZuY0F-Tyg_m1fPw51sZhN2WmNXJd-CgYxeesHkYmR1cIMjqxrJFbX2qqyEeJIxf2AGuh5koP0fXQAaoRUj8mzWHKhGwWawfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس
📵
قطعی گسترده اینترنت در ایران وارد
هفتادوششمین
روز خود شده.
این محدودیت‌ها حالا به شکل یک اینترنت
طبقاتی
اجرا می‌شود.
مدلی که در آن فقط گروهی خاص به اینترنت آزاد دسترسی دارند و بخش بزرگی از مردم عملاً از جریان آزاد اطلاعات
محروم
شده‌اند.
ساختاری که خود مقامات سال‌ها
مدعی مخالفت
با آن بودند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/funhiphop/74828" target="_blank">📅 11:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74827">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به به  سازمان عملیات تجارت دریایی انگلیس:  گزارشی از وقوع یک حادثه در فاصله ۳۸ مایل دریایی در شمال‌شرق فجیره در امارات دریافت کردیم.  قایق های تندرو سپاه پاسداران یک کشتی را که خارج از تنگه هرمز لنگر انداخته بود را تهدید به هدف قرار دادن و سپس توقیف کردند…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/funhiphop/74827" target="_blank">📅 10:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74825">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1MwEXgLXMtSBtuHxWxbwHDtNyFU0ae3D3_qrNRoWflGsDPn49l3FwKQoplr3uBQSBHCnZrGh3RpCXhF2WRMA0tw9SkxxQKJcHV30AEXn_bs4YuTc2_F8Qi-MleavqD-PRVgjDzRH-w3sKlcnlX3tzXcRloRCGY8uTc11C-w-odsxjeb89mFZs_3bwTqef1Jjsvo0FRGyX3TgtigL6u0pciqZG20TAycpJvEHP0YSPpy95KDOfxNEmPFUdPySGYJXPDVPWqfGe9jOkJAhThVpXXwzgxkGqU8O5_4sJqwGSCG6MquEfxWgZPtgIwYLO35juRyd1i8cZeMTb8FOkYM7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به
سازمان عملیات تجارت دریایی انگلیس:
گزارشی از وقوع یک حادثه در فاصله ۳۸ مایل دریایی در شمال‌شرق فجیره در امارات دریافت کردیم.
قایق های تندرو سپاه پاسداران یک کشتی را که خارج از تنگه هرمز لنگر انداخته بود را تهدید به هدف قرار دادن و سپس توقیف کردند و اکنون در حال بردن آن به سوی بنادر ایران هستند.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/funhiphop/74825" target="_blank">📅 10:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74824">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDX6CsKmr2xuWTXBzQXJxxztiTTlq4UI5NumETUPh8qTtTK3WIBANWevw2mwOf_QUdUbjnGioSvXpuRdQP-5M__n5my_Vlyy_DGh1sKy5jWrgJEyiOqcddct_Kn5oXXiwHTcJzXHaWAuH03ze0mwqrAZM9GcppH0Ec9dSdVBrOSeaF2ovkBbhMml4uPNtfIO1MN90qG9gNoWrl39mAK80zLM28g_7gyYiMflKWsb0uiqqQeW4F980jYGKCQ0B1n-fAybTSUqQfJEF9jaw3Pe-V1MEIPlp14qjJ6IF9sLZngzS39oTLlMS5WUnq9hFwYSEIL61F5Oid2EPiIW0xT76A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی پسره قراره 6سال منتظر بمونه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/funhiphop/74824" target="_blank">📅 10:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74822">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حمید رسایی:
تنها دلیلی که برای تعطیلی مجلس به ذهنمون میرسه اینه که نمیخوان مجلس با نطق ها و تذکراتش تو روند مذاکرات خللی ایجاد کنه.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/funhiphop/74822" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74821">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سخنرانی دکتر عراقچی در کنفرانس بریکس: من به نمایندگی از جوانانی صحبت می‌کنم که نمی‌گذارند گرد و غبار جنگ آینده روشنشان را پاک کند، به نمایش از مردمی که تحت بمباران وحشتناک، تصمیم گرفتند استوار بایستند؛ به نمایندگی از مادران میناب که زیر غم از دست دادن فرزندانشان…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/funhiphop/74821" target="_blank">📅 10:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74820">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سخنرانی دکتر عراقچی در کنفرانس بریکس:
من به نمایندگی از جوانانی صحبت می‌کنم که نمی‌گذارند گرد و غبار جنگ آینده روشنشان را پاک کند، به نمایش از مردمی که تحت بمباران وحشتناک، تصمیم گرفتند استوار بایستند؛ به نمایندگی از مادران میناب که زیر غم از دست دادن فرزندانشان خم نشدند.
ایران از کشورهای عضو بریکس و همه اعضای مسئول جامعه بین‌المللی می‌خواهد که به صراحت نقض قوانین بین‌المللی توسط ایالات متحده و اسرائیل را محکوم کنند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/funhiphop/74820" target="_blank">📅 10:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74819">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ و شی جینگ پینگ چه در نوشابه ای دارن برا هم باز میکنن</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/funhiphop/74819" target="_blank">📅 10:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74817">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlNnJjp-3D9LlzrLnG32hVRM0i6sVgC3lgJWzDzjozApeqZJeguS84E3ipMNvF6W6sEO8rTd7LoI9CkuMt_hyZ8llFGYCAnDRNGMoL1RKucLbC3IuLER2DrMJxrSCQyHWzINUbrczGKfQ-M589BU0ie5fbj5OzXNPI3idmK7usKbe_ZadWLDLS63G6GtIakxTw3UEDXwvp0oscPonoJVcoSuM9QqKkKc29hkxQbWQaw-PcHWvLTQmrxnzry4uPsOGxSjctTC3eWm4jxnsxEbIv2sSPO3_eUYSBumJgmBrBX-fYt86DLr_kSGRppu3LzKVyEwkqTp41SoleQUZX0qeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه معین قراره واس تیم ملی بخاطر حضور تو جامجهانی اهنگ بخونه.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/funhiphop/74817" target="_blank">📅 03:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74816">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مارکو روبیو:
امیدوارم چین نقش فعال‌تری در متقاعد کردن ایران برای خودداری از رفتارهایش در منطقه ایفا کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/funhiphop/74816" target="_blank">📅 01:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74815">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxtIf5OSllMftLL8Q9G5QSfYfnib3xb12ic9xERLIUnNPiCI5OkbGfn8PbnjJxUIYaV0vU3y9ZJkemV8g39txEjVsGwNwP7NfYB-5XtxUV_Sx9TgirwrjwFOZZG4NJQhrp6cLYkg5p6OT2y2kKAuCskGOpLNPoGaKXrK3o9N9MLNUWIgyaHcM5tmEMMcwDIcc9_LHiE8klH5AVGkpKHSxecVWt6Zqqg-_U1Z09giehsmyt_a-Y_BF0xwsUI7V9I9FHsozf1tje3Lru725DYiQPw3I2bVFnKviOsdTLkAMQetf8Y-ecRMFfLpAT3TZS-j9JF_w9_VcugQkYZzQfzzyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز عصر دفتر نتانیاهو گفت طی جنگ ۴۰ روزه، نتانیاهو شخصا سفر مخفیانه‌ای به امارات داشته تا با رئیس امارات دیدار کنه و چند تا مقام نظامی هم تو این مدت رفتن اونجا که درمورد جنگ هماهنگی ایجاد کنن.
الان امارات کلا همه چیو تکذیب کرده گفته ما هیچ‌کس رو اینورا ندیدیم و اینا همه‌ش دروغه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/funhiphop/74815" target="_blank">📅 00:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74814">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مثل اینکه معین قراره واس تیم ملی بخاطر حضور تو جامجهانی اهنگ بخونه.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/funhiphop/74814" target="_blank">📅 00:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74813">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مثل اینکه معین قراره واس تیم ملی بخاطر حضور تو جامجهانی اهنگ بخونه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/74813" target="_blank">📅 00:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74812">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه بات زدیم که کاملا رایگان با رفرال گیری میتونید کانفیگ بگیرید ازش، چون جدیده کسی استارتش نداره و راحت با پخش کردنش بین دوست و آشنا و گپا میتونید چندین کانفیگ رایگان بگیرید   @SonicVPNRBot</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/74812" target="_blank">📅 00:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74811">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه بات زدیم که کاملا رایگان با رفرال گیری میتونید کانفیگ بگیرید ازش، چون جدیده کسی استارتش نداره و راحت با پخش کردنش بین دوست و آشنا و گپا میتونید چندین کانفیگ رایگان بگیرید
@SonicVPNRBot</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/funhiphop/74811" target="_blank">📅 00:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74810">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جی‌دی ونس:
فکر می‌کنم مذاکرات با ایران درحال پیشرفته.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/74810" target="_blank">📅 00:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74809">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a5eb89bfd.mp4?token=D2YhnDx6-yFRHZvwhDxwk4QfNKHkGvDCxnH9CoCZcOfrXGcm9054mdxcTJpsx_h94PsSkNi_m6cpbR3FuAhzipYKvLqfDaiY-AgXg16qqnG20za_iMgNzMDEQJ7WYsjyfzC2EmHsOzPsUcunVgQS_HUbDp7PnyiA48lbm277vas26bLbYB0H-4BQJZDZX923tqcTGB4ilIbYoZy6btBkQae9EKF_5M9EvlC4ZAk-qfCqiWr7sGC1CgRHgdyIApRJt7lp6hgQ4T5wXmqsxpij4vBAj28uM9hlS3jrEScdQWm1qecJfJstHJ5r8MtKrrrC9ke7tH4xpOZ0DGxQo4MYLnCO5_adCPYMh6AGAVcZ4WCkWXh2Jq_CgcyAyfNsjFtijbBuZEPFg_Yrw_LDA3WAbmGc4smLZszy1sOhvpn0vqVOl0XaXEjXH81vG3pPizzIGacgcIgS4WD1bNvkll5oBYyIpIMnf0G42axyE_Wk374NdLcAvPEjTF6BwI97P6sx7JwU-zmPb_2n2c7erXHys449iWz7Znimj-okgsCHo2HhHe6HCQgyXCeTaK8Bt_SvPHTz0-GUgoiEH1VhNSE15W_St99lUFrrviH3uf9k72383wtnz9DgdebS1U_CDemYlDiUOA1RQwCo9soN8DEA5bdFt-CNtPpIKEUPVYtaKzU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a5eb89bfd.mp4?token=D2YhnDx6-yFRHZvwhDxwk4QfNKHkGvDCxnH9CoCZcOfrXGcm9054mdxcTJpsx_h94PsSkNi_m6cpbR3FuAhzipYKvLqfDaiY-AgXg16qqnG20za_iMgNzMDEQJ7WYsjyfzC2EmHsOzPsUcunVgQS_HUbDp7PnyiA48lbm277vas26bLbYB0H-4BQJZDZX923tqcTGB4ilIbYoZy6btBkQae9EKF_5M9EvlC4ZAk-qfCqiWr7sGC1CgRHgdyIApRJt7lp6hgQ4T5wXmqsxpij4vBAj28uM9hlS3jrEScdQWm1qecJfJstHJ5r8MtKrrrC9ke7tH4xpOZ0DGxQo4MYLnCO5_adCPYMh6AGAVcZ4WCkWXh2Jq_CgcyAyfNsjFtijbBuZEPFg_Yrw_LDA3WAbmGc4smLZszy1sOhvpn0vqVOl0XaXEjXH81vG3pPizzIGacgcIgS4WD1bNvkll5oBYyIpIMnf0G42axyE_Wk374NdLcAvPEjTF6BwI97P6sx7JwU-zmPb_2n2c7erXHys449iWz7Znimj-okgsCHo2HhHe6HCQgyXCeTaK8Bt_SvPHTz0-GUgoiEH1VhNSE15W_St99lUFrrviH3uf9k72383wtnz9DgdebS1U_CDemYlDiUOA1RQwCo9soN8DEA5bdFt-CNtPpIKEUPVYtaKzU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدرقه تیم ملی برای رفتن به آمریکا و حضور در جام‌جهانی ۲۰۲۶ با شعار مرگ بر آمریکا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/funhiphop/74809" target="_blank">📅 23:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74808">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خبر تکراری و حوصله سر بر
صدای انفجار در اربیل عراق
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/funhiphop/74808" target="_blank">📅 23:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74807">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رپر ایرانی از عجیب ترین موجودات تاریخه، یکیش میگه چرا از خون بچه های میناب نمیگی در صورتی که چندین هزار نفر کشته شدن و جیکش در نیومد و تخم نکرد حتی چهارتا پست بزنه واسشون، اون یکی میگه چرا از خون ریخته شده چندین هزار نفر نمیگی در صورتی که خون ۱۷۰نفر از کشته شده های میناب براش ناچیز تر از اون چند هزار نفره، جفت طرف جون کلی آدم از این مملکت شده براشون سپر بلای عقاید تخمیشون، اون یکی ادعای وطن پرستی داره ولی تخم نداره به کسی که وطنشو بیش از ۴ دهه مورد عنایت قرار داده چیزی بگه، یکی دیگه اونور میگه وطن پرسته پرچم فلسطین نمیگیره دستش ولی خایه های اسرائیل تا ناموس تو دهنشه.
اینور یارو تخم نداره به کسی که اینترنتشو قطع کرده چیزی بگه میپره به کسایی که خواهان جنگ بودن در صورتی که بود و نبود اونا فرقی نداشت و اولو آخر جنگ رخ میداد، اونور طرف میره کنسرت میزاره که کمبود درامد از استریمشو جبران کنه
خدایا کیرم تو این کشوری که مارو توش اسپان کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/funhiphop/74807" target="_blank">📅 23:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74806">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شجاع خلیل زاده:
قهرمانی در جام جهانی سخت ولی شدنیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/funhiphop/74806" target="_blank">📅 22:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74803">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwCdLCSl60dUyeCI2maq2kHXmRWaD1maQt-1LhxzsQT8STFKQ3GyIqk63DFa6Ia78HvOrh4wMkX9_4WrLJZJL2TI8cAV0CXok3MRSzrz-pdXKJiS-8cqPC-uTDKGR67d86BzOvupofP8CYD-UK03L5tsJ-aHDGzIaBHuE8_f0klSZ7Vfbj-O4yfARxHwyWf6BYh8CC0MxfF2DxniXrL_sL-covh0B-MlLc7rTofGZfGUz1AiuP8xO746kMxDaml_PcDvKY6y51XZdnEEMCuRnGwtuceHIASG_Gn8Vc3qLS5EQFOARcR6e8QmqKk2o_trOtL1HJAJ5vVcPEgncGUE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tv9nL3uMaupydxySAAuOBUBnezPsYljG5y8rsozRBzm2AQYeBwkke_Xw2LiQsC9QYgr_I52on14sq_uBs5QP4Y_3iX2ZfaWClkGXX2ODwYifwWcdD4I3Usujhg-3u_-OMajgGNRflMp9Yk7172kDjMJPYtoD-1T6ITrrAYsAW5N45YTGqqGvsV0SDWwzkOy4q3x_aqdWxnV9hNXh2Jzragy090JxS5XCXcA-197gYZ9mjiRBQGWi5h3xx8-o3_EhDkKf_-pB-fy73mlaKe7IMONhLnIWaiSbt-2GaS_EeivOluHjkhYyb9oG9HMwQjL2BCg2OdRrG9_cDr_ECrgR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3Lbavwl91r2q-_aOFY6-qjp6wgTLhNCmmcSw2fvGn-BLOp7ObPNogjDxdIXIhSMV2DNDAal2btojsNTT1W4QMOXU7EDSwLlxMo8IDg6nvtglmQWknJ2N6t2di0v0ePsPjMLuebORvPntSh67A848JLZi82B-MSv0gUv-oeSKErkPwXZSeouElLezuq_B2_hNpURetdJ0uIivPx8ocRdC20keKH6yw5iTLj01C0hhtuAvXlD2DWUX_tTBm4HSyj9tEktpnCLnmdy4kp8pvic0WX3CgUs7amJU_znMR3MrhU3RS7RjqASeU19ZgvBEvwYUnC0SoHRRqV3xF_gkhZPiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم من میدونم هم شما میدونید که قراره بزنن و امیدوارم از این وضعیت فعلی خلاص شیم
طبق اسناد از ابتدای ماه مه تاکنون، 50 هواپیمای ترابری آمریکایی وارد پایگاه‌های این کشور در خاورمیانه، به‌ویژه پایگاه موفق السلطی در اردن، شده‌اند.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/funhiphop/74803" target="_blank">📅 22:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74802">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سوپراپلیکیشن ایتا:
امکان ارسال فایل تا حجم ۲۰ مگابایت مجدداً برای همه کاربران فراهم شده است.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/funhiphop/74802" target="_blank">📅 22:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74801">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNwIneRxmcNGbeWY86nfAh8o3Ln7zqmsY7pRX2SJeBJA1T965XpurteOSlt_Sye6z6sE1yVcXS_fD7QV_2eTpWd_3TkLJ4mcnjH5RxNLon_OMC1iRdnaZbjIZUaOoxMAOJt7mkDTXM3TvZQs4Cen_7cNk-17P6xuxlp00tXIYtvDn5Nbpxgn0HibEk0FsQhsYznKj6rQL_O2lQzq2hx3XbcDiFi9HnJXDWiuTPh2cqoF2xnMBllLzJQ4GqR3UYfcX_P5fDqf4FacMHBnDMYfdTDWQfgT2ytfjMu7cjOFCb3KAaWwsOM7JIcgDrNIcBCLXJuxnSORaZcraIBKMLYu5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئالیا درگیر نیمار شدن وینی بودن، امباپه نیمار شد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/funhiphop/74801" target="_blank">📅 22:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74800">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!   دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 149 هزار تومان!
😈
( فقط 400 گیگابایت موجوده! )
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/funhiphop/74800" target="_blank">📅 22:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74799">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTORNADO Ping</strong></div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!
دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 149 هزار تومان!
😈
(
فقط 400 گیگابایت موجوده!
)
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin
| خرید
🤩
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/funhiphop/74799" target="_blank">📅 22:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74796">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نتانیاهو تو جنگ 40 روزه دوبار مخفیانه به امارات سفر کرده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/funhiphop/74796" target="_blank">📅 21:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74795">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حاج صفی کیرم دهنت بمیر دیگه کصکش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/74795" target="_blank">📅 21:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74794">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این جام جهانی خیلی جالبه
طرفدار های حکومت بازیو لایو تو تجمعات شبانه میبینن
از اونطرف ایرانی های مقیم آمریکا هم با پرچم شیر و خورشید میرن استادیوم
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/funhiphop/74794" target="_blank">📅 21:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74793">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امیدوارم تو جام جهانی کسی برای بازی های تیم جمهوری اسلامی فاز وطن پرستی نگیره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/funhiphop/74793" target="_blank">📅 21:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74792">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">داداش من خودم رضا پهلوی‌ام
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/funhiphop/74792" target="_blank">📅 21:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74791">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رویترز:
عربستان و کویت درجریان جنگ ۴۰ روزه به هدف‌های شبه‌نظامی‌های طرفدار ایران تو عراق (حشدالشعبی) حمله کردن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/74791" target="_blank">📅 21:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74790">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سنای آمریکا بار دیگر طرح محدودسازی اختیارات جنگی دونالد ترامپ در برابر جمهوری اسلامی ایران را
رد کرد
.
تصمیمی که نشان می‌دهد این لایحه نتوانست
حمایت کافی
را به دست آورد و عملاً به پایان مسیر سیاسی خود رسید.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/funhiphop/74790" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74789">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEz2YpAHdosm92zVHtMx2LccMVqZj9Ma5AX37xy3KM68j6l1mO0CGdj2XLK4j6EGFIulKaotIz1TEFSi6ZLcWdLuMHBfu4N0TBwjoL7lnehHQOo5DbQOAvMu3dECCaoPZnmd8VNr79_L5hR2qEL5GhW-GuybqUtRt62aGq3QIh1wHxn9CwDUR-ksl0NWvb8Qyczcn1f3ba--r33x2rZyr5bMo8QdYJ1mMYkTbYZNFUBcy3oauzRFF8wMSvjx9CQkR4YIAXpkEK1braUavAZBeN0GmmXEE2BUnBintnbRjSlRqQjXPwa7H-Hk3NBdDwNIjEgYYQXYJjmeIW7q4Z5oWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه شب بخیر
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/74789" target="_blank">📅 20:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74788">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqYA5jhn7slKb2w7IU-mu71s-5XZ74jJDZcoioaJLXiuSopze2mmcHVc-sgoXEms-AEauFiF7hiUbw-UG3uFNaSoW2NaaGycgystXWjiA9jE665Ff8BqPsWbSvIxeVaMaExMI5w_mQRUcCUF47-0vXmdl9vj5xopfsMCH_BvjIwGKJA7HOSjLxSVWfDw5XQwgyljItjV0dY9uDjRFnb_zc5dYjScEUN1RYWnIFPoILndPp7CK5OZyP3FOjwxWwC5ZA3Ln2xa7nSzY5WCQkVNYHaxZFgWhZdhdyQ8QGLEtu4tDSQbnBxqARiDTE1bvaADcFbkxVpRqe_yy3qoCvzEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره خبری که منتظرش بودم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/funhiphop/74788" target="_blank">📅 19:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74787">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فون برند
🔝
فقط با برند میتونی آفرای ویژه ببینی
🛠
🔵
سرویس های V2ray    1G
➡️
230,000   2G
➡️
460,000   3G
➡️
990,000   5G
➡️
1,150,000 10G
➡️
2,300,000 15G
➡️
3,450,000
🟠
سرویس های open و L2tp     5G
➡️
1,533,000 10G
➡️
2,830,000   با برند، یه کیفیت برند رو تجربه…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/funhiphop/74787" target="_blank">📅 19:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74786">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v10DpKOEKVHyRqARKGeDaEOAvGn4qYzibLmoVQWzmF7X4JwrhuyJM7u0Jw_Znq1I8u-Z7d2JExda2_Qw7KSiNrsWd8SCLVGIT1zuxcHHkXv-1BN7nhSZ6F1b4TwQ8MSp5YfDmBHTmLTuOotFtPUcSsurCOHLSjezCsC1rH2SSo_WD-uf9oeoGh9zF8qPijOHJxmmDzT71sF05BjIoBpZEGcZq0Dov-CIcOGpbXruocanp0dnXX5iHKkIgwKDrbV9NdJOHYrkNwx7SAexqb0nuuS5QGRpgfIn2_CQSeXBLP46xvyr7vMTRPuf0Omd6Olbz7fDaFPk4bryMR2wwJDvIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فون برند
🔝
فقط با برند میتونی آفرای ویژه ببینی
🛠
🔵
سرویس های V2ray
1G
➡️
230,000
2G
➡️
460,000
3G
➡️
990,000
5G
➡️
1,150,000
10G
➡️
2,300,000
15G
➡️
3,450,000
🟠
سرویس های open و L2tp
5G
➡️
1,533,000
10G
➡️
2,830,000
با برند، یه کیفیت برند رو تجربه کن
🦅
@phonebrand13
✅
@phonebrand_support
✅</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/funhiphop/74786" target="_blank">📅 19:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74785">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پدر احسان افراشته (جوانی که امروز به اتهام جاسوسی برای اسرائیل اعدام شد) با شنیدن خبر اعدام فرزندش سکته قلبی کرد و در گذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/funhiphop/74785" target="_blank">📅 18:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74784">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">روزنامه های فرانسوی مدعی شدن گلشیفته فراهانی و امانوئل مکرون رل زدن برا همین کله زن مکرون ازش کیری بوده  این اولین باری نیست که این شایعه پخش شده  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/funhiphop/74784" target="_blank">📅 18:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74783">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">روزنامه های فرانسوی مدعی شدن گلشیفته فراهانی و امانوئل مکرون رل زدن برا همین کله زن مکرون ازش کیری بوده
این اولین باری نیست که این شایعه پخش شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/funhiphop/74783" target="_blank">📅 18:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74782">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530c2c0a1f.mp4?token=LZFXavjijVICAfvT8HuIr8ALFHUSHa4nLQt5h4lvAdNTtaavu22XHed546sStokT4N51nJl7fIMU6mi5QY85uz7QsNaaa8HEyTv5ZJTnKQoohaySOt0jcMf8SzmU1Wm7Z3UxZfPqsl7f6XkYF3iVzUcSyoOLV6O94KU7kgS8B-fPx0AKPCkGhD6lSkURWN6A4xuv1zQ__-1cmUx7VLP_vZpUBMNaiZ0ak9wHErlltlOH1OXsvWXGdlEUhbby7Zn9N7P9fJL2hqHzv0I6pxaPpkfx_rI6xJUwp8i4MemCfSAXmLxYie1O3fPnhgilFPSzFZJZKliN3afkSFoIgb74xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530c2c0a1f.mp4?token=LZFXavjijVICAfvT8HuIr8ALFHUSHa4nLQt5h4lvAdNTtaavu22XHed546sStokT4N51nJl7fIMU6mi5QY85uz7QsNaaa8HEyTv5ZJTnKQoohaySOt0jcMf8SzmU1Wm7Z3UxZfPqsl7f6XkYF3iVzUcSyoOLV6O94KU7kgS8B-fPx0AKPCkGhD6lSkURWN6A4xuv1zQ__-1cmUx7VLP_vZpUBMNaiZ0ak9wHErlltlOH1OXsvWXGdlEUhbby7Zn9N7P9fJL2hqHzv0I6pxaPpkfx_rI6xJUwp8i4MemCfSAXmLxYie1O3fPnhgilFPSzFZJZKliN3afkSFoIgb74xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز خیلی عجیب و خیلی سنگین دارن به جنوب لبنان اتک میزنن
جنوب لبنان تبدیل به یک مکان آخرالزمانی شده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/funhiphop/74782" target="_blank">📅 16:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74781">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b397b8f97.mp4?token=S1nJaFmkPikH-FSubPZVFPSx7toorUHk0bqbH8xFX53HJ0Lt-QB00LUIddH9XE-9vaOKababIog4PE2PEm-kcIpdVOv5pqIo2CNabyqgjRWevecbJbwOUqlnMxyvKBbhVrI0hHh6GJKS3r43E1B0i0g1z_kHmVd67-r1CYWVknGq10zT9nVhW-U0XW6MVo-escQDidbl1BAsnYPSCbgY6XHOXrc0fAX9fTEjvW6ygecNQq4uOhcZo5hoj5ANPijqDgdS15xjjpk4SjPprDRobdXQgoFczDo4-KM9CV8xoTDyPohjtb_0IbWvHCyI0ChyC1zRVYEwZUy0NulaL7SgzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b397b8f97.mp4?token=S1nJaFmkPikH-FSubPZVFPSx7toorUHk0bqbH8xFX53HJ0Lt-QB00LUIddH9XE-9vaOKababIog4PE2PEm-kcIpdVOv5pqIo2CNabyqgjRWevecbJbwOUqlnMxyvKBbhVrI0hHh6GJKS3r43E1B0i0g1z_kHmVd67-r1CYWVknGq10zT9nVhW-U0XW6MVo-escQDidbl1BAsnYPSCbgY6XHOXrc0fAX9fTEjvW6ygecNQq4uOhcZo5hoj5ANPijqDgdS15xjjpk4SjPprDRobdXQgoFczDo4-KM9CV8xoTDyPohjtb_0IbWvHCyI0ChyC1zRVYEwZUy0NulaL7SgzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون همیشگی
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/funhiphop/74781" target="_blank">📅 16:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74780">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/al6w5X1Vjmc2RtKS9qJvWUGTxEvpNkCpRFMbZVGB8-z0WzrEml_OBxRodm0DfWlGbiF2XD3QlyS3BzrB2vUoqNPQXz14d3-zqyD79wvbbaY9o2x9cOFy4a2DlzkP0bNckftKAz3DW8VzLcrTrnn9O65jjoZDUcqONErb72OMN6gXLx8ABex-xpSSa9gpjx6bkyFOH2rNUbgqTF3JCgLZvpjmNjIeIwOQ-nk0BErIcDVjCtlWyuSMx1uUpT1d-8ZzejRP1mAKoqRE_Sst9SUglMyUWnn94GA5ySW89dyhWFVtt2ZblTRpZqVX7eIclUsHseHW2CVwrw5ceam5VJ63lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید مجید نقطه زن هواپیما رو با موشک بزن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/funhiphop/74780" target="_blank">📅 15:49 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
