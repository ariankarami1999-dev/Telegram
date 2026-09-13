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
<img src="https://cdn4.telesco.pe/file/BLNcqQmCNugwWGuhz8fm6pYR0TGtIy63oKNzmI9-CKvyKBCaxHeNZQqxzMczLXRFTO2tTz4PbtSi9fAFql4bseQG5v-I1uEn6nzL_Rc42rGlGYbLozTWhUnSUDVMyzRAryZWWEDe1Ewr_CIoJ6n3sh5S3tFbLgnwwsLOFDfSZtUxk7Xw64-OMr1I8w8FIncv0eWDs6qboVEMFFSUl_MD1sZmA1bTGA70l95uIJcMowtjFyno5xm3AQLo2oMd6EoYZ2K9ITVwXWUeq69z02nFs7Va8H9bINfpcJBtuosxoytxMPCLDO-zNVA-4wEDwsiUz8KWbFXYoE-Hxy3feg-Efg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 16:28:12</div>
<hr>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf4511f99.mp4?token=CgSGOfBw3sbvkap17PW_u4BL9dHQCgk333IJW2jgtGcwpiXUJOBlAzi0-BhV0oL25DdgmBBAzNvkxm4vIGQU9wa4VEFycVxONjN96vLxBvqDe1BCbggAJhmEEKyplriEStiZdRLWuIVeKU-0k2cZp8QeWzShn-xYLEU6pC8H1GERanTL-4A3IIzlK2a88jki1N6oXso1DLOHRDlkJOjmgS6X1bLngN0WqYE_QobVpE4m6etE70gkNqlN9b4LSoX9r8MBPIFRchRr7g0xv0UVGRfwoyDU0tnCvINDqzmK72FArc4Y_Wu2lVWwppJwehIS380CdgEKZOdSUpy7uR8RCjS6MWxK-bstOllkmtWinWwFqVfuTSnjfSaNNw-pEPTVVyNOD6zJEpwXqC7oBytA9SveZrmSOCT7OVsiG-XoxNMjajwpzPDgMNymTc7Fmc9xoHQT-V7obQeZuvNMmlr1ZCy8ndSEeTyFMZyzu2CP48v9RvK5dGHAYv1oLjHfCFba58XSCSLDh9CuKlzeFsT9pET8m1sK0HQ6FTnM6OZ0uvo6qidrcn7lBwJekkOXil8MvAaYhFCXBHPGGVCX7rdIil1Yt_kJmYePdWoaUdLqK-2ThLBXfn_l3I4fTEBhd_i3wJLE-6lboTTGSvMk22Uk0GN7FFj_vsuax88_4czXyTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf4511f99.mp4?token=CgSGOfBw3sbvkap17PW_u4BL9dHQCgk333IJW2jgtGcwpiXUJOBlAzi0-BhV0oL25DdgmBBAzNvkxm4vIGQU9wa4VEFycVxONjN96vLxBvqDe1BCbggAJhmEEKyplriEStiZdRLWuIVeKU-0k2cZp8QeWzShn-xYLEU6pC8H1GERanTL-4A3IIzlK2a88jki1N6oXso1DLOHRDlkJOjmgS6X1bLngN0WqYE_QobVpE4m6etE70gkNqlN9b4LSoX9r8MBPIFRchRr7g0xv0UVGRfwoyDU0tnCvINDqzmK72FArc4Y_Wu2lVWwppJwehIS380CdgEKZOdSUpy7uR8RCjS6MWxK-bstOllkmtWinWwFqVfuTSnjfSaNNw-pEPTVVyNOD6zJEpwXqC7oBytA9SveZrmSOCT7OVsiG-XoxNMjajwpzPDgMNymTc7Fmc9xoHQT-V7obQeZuvNMmlr1ZCy8ndSEeTyFMZyzu2CP48v9RvK5dGHAYv1oLjHfCFba58XSCSLDh9CuKlzeFsT9pET8m1sK0HQ6FTnM6OZ0uvo6qidrcn7lBwJekkOXil8MvAaYhFCXBHPGGVCX7rdIil1Yt_kJmYePdWoaUdLqK-2ThLBXfn_l3I4fTEBhd_i3wJLE-6lboTTGSvMk22Uk0GN7FFj_vsuax88_4czXyTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از کشتی کانتینربر ایرانی که امروز در نزدیکی جزیرۀ هنگام قشم مورد حمله قرار گرفت با یک کشته و ۳ زخمی
@WarRoom</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/withyashar/23006" target="_blank">📅 15:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رویترز: احتمالاً عبدالرضا شهلایی، فرمانده ارشد نیروی قدس سپاه، عملیات حوثی‌ها برای تصرف شهر مخا در ساحل غربی یمن را هدایت کرده است:
منابع نظامی یمنی به رویترز گفته‌اند که بر اساس
شنود ارتباطات و اظهارات نیروهای حوثی اسیرشده
، شهلایی در هدایت عملیات تصرف مخا نقش داشته است. منابع دیپلماتیک نیز به رویترز گفته‌اند که
فرماندهان ارشد سپاه برای هدایت حملات حوثی‌ها علیه عربستان به یمن رفته‌اند
. عبدالرضا شهلایی از فرماندهان ارشد نیروی قدس است که سال‌ها در یمن فعالیت داشته و دولت آمریکا برای اطلاعات منجر به شناسایی شبکه و فعالیت‌های او
تا ۱۵ میلیون دلار جایزه
تعیین کرده است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/withyashar/23005" target="_blank">📅 15:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ازسالی : سلام یاشار جان من همسرم راننده ست الان سمت مرز ریمدان (مرز ایران و پاکستان)رفته.میگه اعلام کردن مرز بسته ست. اسمم  نباشه
@WarRoom</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/23004" target="_blank">📅 14:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فایننشال‌تایمز: ایران از روسیه پهپادهای پیشرفته و گران‌قیمت درخواست کرده است:
به گزارش فایننشال‌تایمز، تهران امسال از مسکو خواسته است
پهپادهای پیشرفته روسی را برای استفاده در جنگ با اسرائیل و آمریکا
در اختیار ایران قرار دهد. به نقل از
مقام‌های امنیتی غربی و یک فرد نزدیک به کرملین
منتشر شده است. درخواست ایران در حالی مطرح شده که همکاری پهپادی دو کشور سال‌هاست در جریان است؛
ایران پس از آغاز جنگ اوکراین، پهپادهای شاهد از جمله شاهد-۱۳۶ را در اختیار روسیه قرار داد
و مسکو بعدها با استفاده از فناوری ایرانی، تولید این پهپادها را در داخل روسیه توسعه داد. حالا با ادامه جنگ، تهران به دنبال دریافت نسل‌های پیشرفته‌تر پهپادهای روسی است
@WarRoom</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/23003" target="_blank">📅 14:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5e14331e2.mp4?token=na-gmsU3d1SO1C_oTfdzLw7vmTBIxG37sZmyRbL4Ktua5ZNU4PTlxxOhMmOwazFDbqlbaBlLSBzq03iJ-QDPIrnHVrndnLTbFRufDrOn-Gy-32Z44XrCN5xwGLE25tIO2u3WeBA691EhPgbIh9BkchccYwN3XiuTCLf4z4CIjUXEewXO3qky1BraE1jdl1906MQXi0QCErmirnvpIEf32n9sKK8TCCkeU3FbUX08dZFZSgJqbOSVaCbIFhi2nbJhJ0XXFZ9tVVXjv1xL1aCzCAg3GDPW4Qx91Ym_PLN-p3G1bJaBQnTFu-z1t3kUoIua5GTym3pTRLe1YIoTiZZs8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5e14331e2.mp4?token=na-gmsU3d1SO1C_oTfdzLw7vmTBIxG37sZmyRbL4Ktua5ZNU4PTlxxOhMmOwazFDbqlbaBlLSBzq03iJ-QDPIrnHVrndnLTbFRufDrOn-Gy-32Z44XrCN5xwGLE25tIO2u3WeBA691EhPgbIh9BkchccYwN3XiuTCLf4z4CIjUXEewXO3qky1BraE1jdl1906MQXi0QCErmirnvpIEf32n9sKK8TCCkeU3FbUX08dZFZSgJqbOSVaCbIFhi2nbJhJ0XXFZ9tVVXjv1xL1aCzCAg3GDPW4Qx91Ym_PLN-p3G1bJaBQnTFu-z1t3kUoIua5GTym3pTRLe1YIoTiZZs8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام یاشار جون. ممنون از تمام تلاشی که برای آگاهیه ما می کنی. من همیشه آهنگ پرنده که تو کانال گذاشتی رو برای پسرم پلی می کنم. اونم که خیلی تو موسیقی استعداد داره، یاد گرفته و اجراش می کنه. پسرم ۳/۵ سالشه. این فیلم رو مربیه مهد کودکش ازش گرفته
😂
😂
😂
گفتم برات بفرستم که بدونی از کوچک و بزرگ، همگی دوست داریم
❤️
❤️
❤️
اگر تو کانال گذاشتی، صورتشو محو کن لطفا
@WarRoom</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/23002" target="_blank">📅 13:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جرد کوشنر، فرستاده ویژه آمریکا: اگر اوکراین تا خط موردنظر پوتین عقب‌نشینی کند، توافق صلح می‌تواند نهایی شود:
کوشنر گفت
موضوع سرزمینی همچنان سخت‌ترین مسئله مذاکرات صلح روسیه و اوکراین است
و ولادیمیر پوتین خطی را که می‌خواهد به آن برسد مشخص کرده است؛ اگر اوکراین با عقب‌نشینی تا آن خط موافقت کند، بخش عمده توافق از قبل آماده خواهد بود، اما
کی‌یف در حال حاضر حاضر به پذیرش این شرط نیست.
کوشنر افزود وضعیت میدانی نیز در تعیین سرنوشت مناطق مورد مناقشه نقش دارد و وظیفه میانجی‌ها یافتن راه‌حلی است که ضمن حفظ اهداف اوکراین، امکان پایان دادن به جنگ را فراهم کند.
@WarRoom</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/23001" target="_blank">📅 13:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کمی پیش گزارش زنده فاکس نیوز از روی ناو جرج واشنگتن و پرواز جنگندهی F-15 و F-35 با دریافت کردن سیگنال تهدید از سوی ایران(پرتاب. موشک/پهپاد) به کشتیهای عبوری. همچنین در ویدیو میبینید که تماما پشت سر مجری موشکها و بمبها قرار دارد و این ناو بیش از اندازه تا دندان…</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/23000" target="_blank">📅 12:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxEVBLplBuc2umFY2JbbKkd-B7zyAt7Hjlzo_kpsHwFnJFYjPhn4gc1GVvnVDac3n3BYuct0fSATpwghfIKySn3Dfsr7UrLP2W9EmK-qhnnGdfgn9krmOXPmcnBcGLtyvVloqw3v-KwIewBZW0W91WqKinx0W6yVWRp41g-Ejr0_vtO5LzngyGovnQha8w5lGQLhnMTj-ZqxN3ylvfZDSoX1G6BYyEcPVU6AWmEikc1fD32sGVvJSey1EnTw62RbjstkR9t4iPGffinLXKpKt1L4D68eLjzs5WqVklPniEAWg2NRtxsQrXMcRRcI7QqfZo2DNjgskRpy3k3sAGdsQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست:
سودا (مرضیه) ابراهیمی شمس‌آبادی
، بلاگر ۳۳ ساله اهل بندرعباس، به اتهام «افساد فی‌الارض»، توهین به خامنه‌ای و فعالیت‌های ضدحکومتی به اعدام محکوم شده است. نیویورک‌پست همچنین به
ترانه رحیمی
، ۲۰ ساله، اشاره کرده که به اعدام محکوم شده و خواهر دوقلویش
رومینا رحیمی
به ۲۵ سال زندان محکوم شده است. این رسانه همچنین به نقل از منابع حقوق‌بشری از اعدام دست‌کم
۲۹ معترض بازداشت‌شده از ماه مارس
خبر داده است,صدایشان باشیم
@WarRoom</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/22999" target="_blank">📅 12:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الجزیره: هم‌زمانی بحران در تنگه هرمز و باب‌المندب، خلیج فارس را در وضعیت «بین دو فک گازانبر» قرار داده است؛
با ادامه اختلال در هرمز و پیشروی حوثی‌های مورد حمایت ایران در مسیر باب‌المندب، دو مسیر حیاتی انرژی و تجارت هم‌زمان تحت فشار قرار گرفته‌اند. این وضعیت فشار قابل‌توجهی بر کشورهای خلیج فارس، به‌ویژه عربستان، وارد کرده و
واشنگتن در مدیریت درگیری با تهران، بیش از پیش با این چالش روبه‌روست که منافع و امنیت کشورهای خلیج فارس را نیز در نظر بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/22998" target="_blank">📅 12:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فاکس‌نیوز: مقام ایرانی می‌گوید ایران تا پذیرش کامل شروطش از سوی آمریکا وارد مذاکره نمی‌شود.
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس ایران، در ایکس نوشت تا زمانی که آمریکا همه شروط ایران را نپذیرد، گفت‌وگو و مذاکره فایده‌ای ندارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/22997" target="_blank">📅 11:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خبرگزاری رژیم ایرنا: دقایقی پیش صدای دو انفجار در قشم از سمت دریا شنیده شد منابع محلی تاکنون در این باره اظهار نظری نکرده‌اند @WarRoom</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/22996" target="_blank">📅 11:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3mA9HdmWt6h_NhGcatEloFRbziB3cowr2XOyQKI1lUSqpnpdt167lC9RdOGBLaihxOCS3oEQoSd0BinKy4oyJmx_miQl_9nJiOxA0ZboR5lUx6I_tEyjTLmY4qCkupA7eUa-PuvIHV3FaMJpDApJrEjhQDAsfnZTzdc6fG_jn9cjPqdxh0zkGTCCPfnDVDMJ60ucvFZYGfjrigNSm3Eg2bU82Mh5O0FcxxeHT6t47C6pxNTuy7AQijdwimMeQMmu5wFr04aWReyHLNFBwD5_1JOfRFarrzRDaE4x03K9K_JQLQaJupjxBM_kH735vvfnRzJsOoRLJvmzhW6Va1cmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای در تنگه هرمز دریافت کرده است.
یک کشتی هنگام عبور از تنگه هرمز مورد اصابت پرتابه‌ای ناشناس قرار گرفته است. در حال حاضر، اطلاعاتی درباره وضعیت خدمه، میزان خسارات وارده و پیامدهای زیست‌محیطی این حادثه در دست نیست.
در پی حمله گزارش‌شده، آتش‌سوزی در این کشتی رخ داده است. مقامات محلی در محل حادثه حضور دارند و در حال کمک به تخلیه خدمه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/22995" target="_blank">📅 11:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afdd8f1fc2.mp4?token=oxtDrmvd1ESz2BRX8k9_wmeO8X5WwNMPhz104GzhPj_mjhIOUNMxeLMQ4fyxbGSkn1ZL7L2P8ahquS-vm0KtMARZhn8nU5EfqRXzSIwXrzjWVHUNI6oAzGz94LOyD4Y1jD9HldkBJyzHe484mZSBujA8aNM3k2BSiSdTTYTua0d2XZeryobTJAq4frPgvQvZkmeEmhb_wIhx67P1ScORP4kZr8eYZTgUXsw1UuCd0_xUTNdgfHaKLg6WwBmweYYpnYBX-N2WkL_lL9qGa9LiXAl8zyIFqKidWGJewbbJKXgDW2aiaYa8Cq6IFM0k7k9qr3RupAqO_SWorrAjydjKoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afdd8f1fc2.mp4?token=oxtDrmvd1ESz2BRX8k9_wmeO8X5WwNMPhz104GzhPj_mjhIOUNMxeLMQ4fyxbGSkn1ZL7L2P8ahquS-vm0KtMARZhn8nU5EfqRXzSIwXrzjWVHUNI6oAzGz94LOyD4Y1jD9HldkBJyzHe484mZSBujA8aNM3k2BSiSdTTYTua0d2XZeryobTJAq4frPgvQvZkmeEmhb_wIhx67P1ScORP4kZr8eYZTgUXsw1UuCd0_xUTNdgfHaKLg6WwBmweYYpnYBX-N2WkL_lL9qGa9LiXAl8zyIFqKidWGJewbbJKXgDW2aiaYa8Cq6IFM0k7k9qr3RupAqO_SWorrAjydjKoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمی پیش گزارش زنده فاکس نیوز از روی ناو جرج واشنگتن و پرواز جنگندهی F-15 و F-35 با دریافت کردن سیگنال تهدید از سوی ایران(پرتاب. موشک/پهپاد) به کشتیهای عبوری. همچنین در ویدیو میبینید که تماما پشت سر مجری موشکها و بمبها قرار دارد و این ناو بیش از اندازه تا دندان مسلح به منطقه عملیات آمده.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22994" target="_blank">📅 03:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ارسالی : من امروز پهبادم رو بردم رو کلانتری شهر رستاق تمام کلانتری تخلیه کردن ، الان رفتن تو بانک کشاورزی موندن
😂
😂
😂
اسممو نذار
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22993" target="_blank">📅 02:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کانال ۱۳ اسرائیل گزارش داده ارتش این کشور در پی تحولات باب‌المندب، احتمال
شلیک موشک و پهپاد از یمن به سمت اسرائیل
را جدی گرفته و در حال آماده‌سازی برای چنین سناریویی است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22992" target="_blank">📅 02:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad.Rf</strong></div>
<div class="tg-text">سلام یاشار من از اینستا چند روز پیش پیام دادم ندیدی بغل پادگان 02 ارتش رو سه روز پیش زدن من رفیقم سربازه اونجاس گفت با پهپاد پادگان بغلی رو زدن ولی کسی صداشو درنیورد حتی میگف بازرس اومد فرداش ببینه چه خبره دوباره پدافندا شروع کردن کار کردن بازرس فرار کرد</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22991" target="_blank">📅 01:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22990">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22990" target="_blank">📅 01:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromممدم✌🏽</strong></div>
<div class="tg-text">یاشار تقریباً ده دقیقه پیش موشک از تو شهر بندرکنگ بلند شد به قدری نزدیک بود کل خیابونا صداش پیچید</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22989" target="_blank">📅 01:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گزارش صدای انفجار بندرعباس
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22988" target="_blank">📅 01:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22987" target="_blank">📅 00:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سی ان ان: پیت هگست، وزیر دفاع آمریکا، برای حضور دو خدمه جنگنده F-15 سرنگون‌شده بر فراز ایران در برنامه«60 Minutes»تحت فشار قرارشان داده است.
به گفته چند منبع آگاه، هر دو نظامی درباره حضور در این مصاحبه نگرانی داشتند و هگست به‌صورت خصوصی با آنها دیدار کرد تا مشخص شود آیا داوطلبانه در برنامه شرکت می‌کنند یا باید با دستور به این کار وادار شوند. در نهایت، یکی از آنها با نام مستعار
«براوو»
با حضور در مصاحبه موافقت کرد، اما نفر دیگر با نام مستعار
«آلفا»
از شرکت در آن خودداری کرد. پنتاگون این گزارش را
«دروغ کامل»
خوانده و گفته تصمیم حضور در مصاحبه کاملاً بر عهده خود این دو نظامی بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22986" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22985">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزیر خزانه‌داری و دارایی ترکیه به شرکت‌ها و مؤسسات مالی این کشور درباره معاملاتی که ممکن است مشمول تحریم شوند هشدار داده است؛ موضعی که چند روز پس از تحریم یک بانک ترکیه و دو شرکت زیرمجموعه آن به دلیل ارتباط مالی با ایران اعلام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22985" target="_blank">📅 00:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22984" target="_blank">📅 23:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ارسالی : سلام داداش وقت بخیر
از بندرکنگ امشب با فاصله هر 30 دقیقه دارن یه پهپاد یا موشک میزنن به طرف خلیج فارس تا الان 4یا5 تا زدن
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22983" target="_blank">📅 23:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22982">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارسالی : مرز باشماق هم بسته شد من اربیلم و همسرم رفته ایران الان لب مرز مونده نمیزارن بیان گفتن مرز فعلا بسته س و مونده تا ببینم تکلیف چه میشه
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22982" target="_blank">📅 22:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرنگار الجزیره: نیروهای اسرائیلی وارد منزل همکارمان، علی السمودی، در جنین شدند، خواستار تحویل او شدند و به پسرش حمله کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22981" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک موشک بالستیک حوثی ها در منطقه "جازان" در جنوب غربی عربستان سعودی به یک مسجد اصابت کرد که منجر به زخمی شدن تعدادی از افراد و خسارات جدی شد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22980" target="_blank">📅 22:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22979" target="_blank">📅 22:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22978" target="_blank">📅 22:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حسین حاجی دلیگانی، نماینده مجلس: طرح سه‌فوریتی خروج ایران از NPT آماده شده است بهتر است هر چه زودتر آزمایش‌های لازم را برای سلاح هسته‌ای انجام دهیم @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22977" target="_blank">📅 22:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وای نت عبری : حملات جدید اسرائیل به جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22976" target="_blank">📅 22:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22975">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22975" target="_blank">📅 21:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تصویر ۳ پاسدار کشته شده در سراوان @WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22974" target="_blank">📅 21:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خبرگزاری رژیم ایرنا:
دقایقی پیش صدای دو انفجار در قشم از سمت دریا شنیده شد
منابع محلی تاکنون در این باره اظهار نظری نکرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22973" target="_blank">📅 21:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پرتاب موشک به سمت تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22972" target="_blank">📅 20:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آسوشیتدپرس: نفتکش آسیب‌دیده در خلیج عمان باعث گسترش لکه نفتی شده است.
بر اساس گزارش جدید، آلودگی نفتی ناشی از یک نفتکش که گفته می‌شود توسط نیروهای آمریکایی هدف قرار گرفته، در حال گسترش به مناطق حفاظت‌شده زیست‌محیطی در عمان و ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22971" target="_blank">📅 20:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLLHuJzUMJJJOvSeuGyBwBXD8-FPtgi_nj_ryGLR-V9mKeSVztj0r3H8tyyHD_XJV-6kdpd4LQ6nLgrqbzQuMkcqEm3GxuI9RNAxlxhGTET_29CQISRq-UyzjJOz-ay6erMDZ9HZtLe3xEiY6TzafoOeysVvEp-zWteK9nrusZzKpVqjOL6m3zLpnvyc2pLlcQYdG48rEV_5JTBlt3Cs4CYq38fE0HGsfQDEAV0lQBsZ4-PbeBQ8T-8K8tOIhrRvdRNVPFlpX6xMnjGEH7sURUoL55zibnUcnaqCQ_0S7gFhgFL28Kh9zjEcBEfzWudUR2aofW9COlPmK7ctOW5pVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ پشت سنگر : یاشار سلام محاصره رو شکستن افراد مسلح همه رو تارو مار کردن نظامیهای رژیم رو @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22970" target="_blank">📅 20:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22969">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دو مقام ارشد امنیتی عراق به رویترز:
ساعاتی پیش سکو های پرتاب پهپاد در چند نقطه از مرز ایران و عراق کشف شدند،
تا اطلاع ثانوی گذرگاه های مرزی با ایران بسته خواهند بود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22969" target="_blank">📅 19:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHDMiZjdm_7irYzvcHIDklDreGR1vN9Ol4fQ7xDHjFoMEtIZ1U_VeppD-n-eZ268SyKLA5OepBwOluaGa8vqLRsPVNkYOzjZIK8qr8ERma4hZRswnRuZtgLvxG1NNOhZLQBHF-eaJ6N9tNZGtGv0qB2XHXhTgL6XddcbMvPRXoNK5vqbIZ2MFdOYFKbDOl3MsO6J_xJRQvQyW59dhzjxXA7IhVHvjvfvLxlyRVB0dNTznRYPBykrfbdZUcEFjCyLlirC9wYHWUYYL1UbiTxbGJITwVuyi9vZEcs6Dxn1KFtOFIL4vjTLp2K521CGZGNxziWtCvw4IlgII8wE10ECGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک تانکر نفتی متعلق به چین با نام لیزا که در دریای مکران حضور داشت، تلاش کرد تا از تنگه هرمز توسط کریدور ایران وارد شود، اما سپس مسیر خود را تغییر داد و به عقب بازگشت. مشخصا آمریکا اجازه نداد  @WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22968" target="_blank">📅 18:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شبکه فاکس‌نیوز، هم‌زمان با پشتیبانی نیروهای آمریکایی از عملیات‌های ایالات متحده در جریان تنش با ایران، به‌صورت زنده از ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» که کاملا پر از موشک و مهمات شده است در دریای مکران و نزدیکی تنگه هرمز گزارش می‌دهد. @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22967" target="_blank">📅 18:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2884ed587b.mp4?token=VSA-puXj3SVk6Ukwla1ub76YXPUjbMiYfqvgZSR9-Ssg20Xq70JYVVnoJeALW-gpDZmWDVpCU1obSeJsLRdTY3z0sonz9xQ2l6zQZkx2oiQ97zmTNCmHDFOWNznT49PkXFIYGeXkoa65mVHg259nFCZTI5qAauH8Asu5SOKYfDMOngeBQez7C8aXBTgm74oE8h7CstLysJb5fNExxyKkdSl8cpaofKuohe6GogZqQd5_scynFy-4u1oqi80LcQXipuznbMgiEbybm2je1mUorfu2lEaBztMlWizjG31kaxeWCjoKc2BqFo97AaY97yaUXkVvpfwL5rbK8R8ffDaQk35at1dWRbVsqF6Y-2M0wviKMZoZBGuqz1unOEMZYMP8FnuBNOt5R8lQbd8fcPLimwrSUekJL1tt-WbKItLJdEmeTBHI_mAs1B78idV5G21d-UICKGsq3APgZVnDpQZYA_yFFrcQAhpYXZhb8b1UmEPyxw0tlQ5ySdHe2R9aGHFNKCFGCwQgByRJq06_djhEIwFKm78wtWpvOBoJyUwcG7iN_qky_JGLuRAwOgaZGg5VprfEv0yd_F_4I99B8ywkUpeWIahMHtoC-C2cw1g-GbP2kh95YHYDDRL_XMMUB-rZel04QF2LuNsy20_HXRJ6xzsZ7Pz0TT2g_gfkGF-RZPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2884ed587b.mp4?token=VSA-puXj3SVk6Ukwla1ub76YXPUjbMiYfqvgZSR9-Ssg20Xq70JYVVnoJeALW-gpDZmWDVpCU1obSeJsLRdTY3z0sonz9xQ2l6zQZkx2oiQ97zmTNCmHDFOWNznT49PkXFIYGeXkoa65mVHg259nFCZTI5qAauH8Asu5SOKYfDMOngeBQez7C8aXBTgm74oE8h7CstLysJb5fNExxyKkdSl8cpaofKuohe6GogZqQd5_scynFy-4u1oqi80LcQXipuznbMgiEbybm2je1mUorfu2lEaBztMlWizjG31kaxeWCjoKc2BqFo97AaY97yaUXkVvpfwL5rbK8R8ffDaQk35at1dWRbVsqF6Y-2M0wviKMZoZBGuqz1unOEMZYMP8FnuBNOt5R8lQbd8fcPLimwrSUekJL1tt-WbKItLJdEmeTBHI_mAs1B78idV5G21d-UICKGsq3APgZVnDpQZYA_yFFrcQAhpYXZhb8b1UmEPyxw0tlQ5ySdHe2R9aGHFNKCFGCwQgByRJq06_djhEIwFKm78wtWpvOBoJyUwcG7iN_qky_JGLuRAwOgaZGg5VprfEv0yd_F_4I99B8ywkUpeWIahMHtoC-C2cw1g-GbP2kh95YHYDDRL_XMMUB-rZel04QF2LuNsy20_HXRJ6xzsZ7Pz0TT2g_gfkGF-RZPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه فاکس‌نیوز، هم‌زمان با پشتیبانی نیروهای آمریکایی از عملیات‌های ایالات متحده در جریان تنش با ایران، به‌صورت زنده از ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» که کاملا پر از موشک و مهمات شده است در دریای مکران و نزدیکی تنگه هرمز گزارش می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22966" target="_blank">📅 18:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WyQIAal0bhBBKRf4VYJ3ynRsn1D98cLmb5OZ8NU72kkTbQPuPFxhHHe-6ZHAtXD1wsCVwT5y7WTs4u0TlUYpfdiXEo4Q2wn_dP0vAoQDY_XAPhJKXBk7YMqkWQEXk5hKUNHU5VqwSpD05nFftFFmZJ48hxp-nRSdfJf8j4ID_eFDd3KKCnJihO8ZfqW2_KXZjpp7anD3X5Ni-nn0_Y1JN0xQwRnPld0lCRQzTaSMxhdESGGsE1Eq57pK83pPrrOMCyXf33HR6wYr6UUm2icq-wKsI2njzBtD-WWKTbt7-M4BVesmFHNKChr-PR89HRpEMdRYDOnGBARx-HJhfZQZGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMHrEjbCZ6WmYIvDdY7zbi__Hcp1wYzSo5rJviDLG_YIj7YjoA56RaC34I1B28WwWj3tKWV1sNZ7J4cNSyRY_YrAUvmXz93oHrzHoMrQdB6Qfq3_WAXgC7WFJ5rOR-cTuRhRgiwlIb9cY0AZNTMPtwroIVgws4-zUZR8pOP4M8BW6Qmb4xO8Ly0tU8a1mNPUe9okYZGHd6U37pBonT9o3cHzTvNHxhS0PMHufxV-J1CGjshr9SJZDImRvC-QGA_vETz0tFgljRqtlOFfaSFVy_fD1kcPtWgAPPPAquKoXv7LunXeZL9XuSH2-A5SbCXLvvNe0_JFz5hj69n-zARHeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdcaeaJCxbAyzzCq5gPX_ZJ_PV2sKRUYcg80PK_jtXWRIWNAL4qCquwQi6xCS9yNDlFb6tF1Oc75kY7tfhyHmgafeIk3nRCvzfKjKUKdxnzEJwr2I7GdtNAcwRqFMwUrdm81E3H8Wz4sud-kdRQVIKPXp1S3RXzyHPgS3CKwfYk8m8P5X8R82OJ2_em9fH8jqQb1b7BAvi-B94MaB-K1ph-vkXg2K1jRv9LFQIGdlkRUoJNHCbALoiW4eNrKURc8kU76DBIKLp9WYiy9piKTgxrQhleqcz9QXKYw8BkbSvfFfLIHAgpZuOeoho4_5xtIj-vsMcsYZgRrSzks_iTbPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kld1vMUOvS0638kyaFx24hHz5nIpLnQDMGApOW2B-quOLoB4Mjfigkh3lOKpkYwHYSLTF8VN8NQmGHgSADAr28kC8O7RlgCqQLcPn41sp85Zji6ZXZPjUN9-hXxsxnTfJM7MYFmsqRyAyEGGmeSTYVjOndD29Y2bwOtJaNGy9S5T7w0f32SBc4bxdB-vTTc1CfNGVaYFCOljE0Ab4A9mkT2YTquPM2WVLI06cbMtozYYcL2Fk7GuOCn52Z31qTNpTBuYt7Hj-ZVtV7SYZ9vT0DfuVhIJW77H6pcjWpe2FFAMCyHFkj9u-ovq2ejXoN2ScW-fT6c7QQw8Ypza1Uukgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آمادگی برای حمله زمینی احتمالی به ایران
سنتکام : تفنگداران دریایی ایالات متحده بر روی عرشه پروازی ناو
«یو‌اس‌اس پورتلند» (LPD 27)
در حالی که این کشتی در دریای عرب در حال حرکت است، برای عملیات احتمالی تمرین می‌کنند
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22962" target="_blank">📅 18:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رویترز به نقل از یک مقام ارشد ایرانی: نشست روز دوشنبه ایران و کشورهای خلیج فارس در عمان به درخواست و ابتکار عمان برگزار می‌شود، اما انتظار نمی‌رود در این نشست توافقی برای بازگشایی تنگه هرمز امضا شود. به گفته این مقام، ایران همچنان خواهان توافقی است که به تهران اجازه دهد از کشتی‌های عبوری از تنگه هرمز عوارض دریافت کند؛ موضوعی که عمان با آن مخالف است. این نشست قرار است علاوه بر هرمز، درباره مسائل منطقه‌ای نیز گفت‌وگو کند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22961" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزارت خارجه بحرین اعلام کرد که این کشور در نشست وزارتی پیشنهادی درباره وضعیت تنگه هرمز شرکت نخواهد کرد و تا پیش از ازسرگیری روابط دیپلماتیک با ایران، در هیچ نشست جمعی که ایران در آن حضور داشته باشد، طرف نخواهد بود. بحرین همچنین تأکید کرد هرگونه توافق یا ترتیبی درباره کشتیرانی در تنگه هرمز باید بر اساس حقوق بین‌الملل باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22960" target="_blank">📅 17:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آسوشیتدپرس: یک شهروند ایرانی-آمریکایی از زندان اوین آزاد شد، اما همچنان اجازه خروج از ایران را ندارد.
کامران حکمتی، جواهرفروش ۶۲ ساله نیویورکی، پس از گذراندن حدود نیمی از حکم دو ساله خود آزاد شده، اما مقام‌های ایران همچنان ممنوعیت خروج او از کشور را برقرار کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22959" target="_blank">📅 17:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اتاق جنگ با یاشار:
اگر پرونده ایران در شورای امنیت به رأی‌گیری برسد، باید بین دو حالت فرق بگذاریم: اگر رأی‌گیری درباره
یک قطعنامه معمولی و الزام‌آور
باشد، روسیه یا چین می‌توانند با وتو جلوی تصویب آن را بگیرند. اما اگر رأی‌گیری از نوع
رویه‌ای
باشد، روسیه و چین حق وتو ندارند و نمی‌توانند جلوی ادامه روند را بگیرند. از طرف دیگر،
وتوی روسیه یا چین به معنی پیروزی ایران نیست
؛ اگر بیشتر کشورهای شورای امنیت علیه ایران رأی بدهند و فقط روسیه و چین مخالفت کنند، از نظر سیاسی نشان می‌دهد که اکثریت جامعه بین‌المللی با موضع ایران همراه نیستند و روسیه و چین در اقلیت قرار گرفته‌اند. حتی در برخی موارد روسیه و چین ترجیح داده‌اند
ممتنع
رأی بدهند و قطعنامه بدون وتو تصویب شود. بنابراین یکی از اهداف مهم آمریکا و کشورهای اروپایی می‌تواند این باشد که در صورت رأی‌گیری،
بیشترین تعداد کشورها را پشت موضع خود جمع کنند و روسیه و چین را در اقلیت و حامی یک رژیم تروریست نشان دهند
و آنها را
به اصطلاح در جمع خراب کنند
.؛ حتی اگر این دو کشور در نهایت یک قطعنامه ماهوی را وتو کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22958" target="_blank">📅 17:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SylGRenucC39x8xlWL9VvvhnzyjJAFBqauxH5IeURRFh4v4w__pDSZVoiw47XcXw06UJ-HUN095-U_FxR40l7Ca38dHvqCsWZFnaz7Rgrzezh99fOli4Mn1QaM2KPG3sKIC9a1lVP6-iMwFTsD-NuKvSKnJVv4ZgB2clfmwShehKZorsCw4THejd_RDu_mG4UZ-PVI6rEYNws2wOwbWFI7ule3f0RLVGpB6Fx663QrjcUxwyjl_ov25-s6C-k9HNh-Vq13hXkyhNMXOUWNUXbujSHTp9CVyJUQmqrAIOWtvltqIpUeZGsVVKG8A8kZjd5s1NgoMgJkNYKWGYgOWl0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست:
ایران پیش از حمله موشکی ۱۷ ژوئیه ۲۰۲۶ (۲۶ تیر ۱۴۰۵) به پایگاه هوایی موفق السّلتی در اردن، تصاویر ماهواره‌ای با وضوح بالا از این پایگاه در اختیار داشته است.
این تصاویر که توسط
نهادهای چینی در اختیار ایران قرار گرفته بود، هم پیش از حمله و هم پس از آن برای بررسی وضعیت و خسارات پایگاه استفاده شده است.
مقام‌های آمریکایی نام شرکت‌های چینی را اعلام نکرده و دولت چین را مستقیماً به دخالت متهم نکرده‌اند. در این حمله که منطقه محل اسکان نیروها را هدف قرار داد،
۳ نظامی آمریکایی کشته و ۴ نفر دیگر زخمی شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22957" target="_blank">📅 16:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: اگر ایران سلاح هسته‌ای داشت، ما تماس می‌گرفتیم و می‌گفتیم: "قربان، آیا می‌توانیم با هم ملاقات کنیم؟" ما با آنها بسیار متفاوت برخورد می‌کردیم. @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22956" target="_blank">📅 16:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حسین حاجی دلیگانی، نماینده مجلس: طرح سه‌فوریتی خروج ایران از NPT آماده شده است
بهتر است هر چه زودتر آزمایش‌های لازم را برای سلاح هسته‌ای انجام دهیم
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22955" target="_blank">📅 16:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22954">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d1bb0546.mp4?token=U8N74GcbDcB5_7QD5SXLGzm5oYIXzmVS7OIVuOaGU4Snt5cZoUznn2DRhevAuCv8oync1qlW8O14i-dXP7zXCJVA7Ser1eb1F4BjPkSlmL9PrlgGzI3wXsDBSqHjPBBBVguWmW0Mhuon5Ei8s_Xc51PgYAcVag0Z3W4H6F_Tv55VXgMdVoKDTsGV_zCqPoLC21WbKf7RtJbKALBNXwbAzAhs-X0MMBfqz32OxCS4PL_GHGGSg256fBT4HOduKPxxrYQm_Q1d2byrdtof1c06QItuU2jbHuZfqOT4idzkh0bLnuyTp0K9PWMS93jRLA2wZqwmY_uBnXIhsniRczF4Mw9ZrgvgN1DQlnWY86k1sIcISj5RV6LnGyZvGGoIFdiGOobg3c-Du2hztoVURaSk_KOTnDAg_Z8JTH8mmM4owxEpjgEiQmTP7BWV-0jbDJlIF7RDazf7GaimX24cnueaIaOI6n24fcvsEM5IogHPiI7T65CQvEQU-KlXEMBLEUJ6LLHfj25BqejTxtrbSRC4jt2LBCLkVft7iqSyJTMdvEG-Q4evtss9eM5VgW75AcWtHdCm9o3iYNd881eZ8LwAkhA3UUKPGfNrW2aeBRysXrlTN3pzvqJ_WeyN7tI20OwugMIMXhbO31CXDfzyBemjvQmTzoR2sfi6DFrsakBhv5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d1bb0546.mp4?token=U8N74GcbDcB5_7QD5SXLGzm5oYIXzmVS7OIVuOaGU4Snt5cZoUznn2DRhevAuCv8oync1qlW8O14i-dXP7zXCJVA7Ser1eb1F4BjPkSlmL9PrlgGzI3wXsDBSqHjPBBBVguWmW0Mhuon5Ei8s_Xc51PgYAcVag0Z3W4H6F_Tv55VXgMdVoKDTsGV_zCqPoLC21WbKf7RtJbKALBNXwbAzAhs-X0MMBfqz32OxCS4PL_GHGGSg256fBT4HOduKPxxrYQm_Q1d2byrdtof1c06QItuU2jbHuZfqOT4idzkh0bLnuyTp0K9PWMS93jRLA2wZqwmY_uBnXIhsniRczF4Mw9ZrgvgN1DQlnWY86k1sIcISj5RV6LnGyZvGGoIFdiGOobg3c-Du2hztoVURaSk_KOTnDAg_Z8JTH8mmM4owxEpjgEiQmTP7BWV-0jbDJlIF7RDazf7GaimX24cnueaIaOI6n24fcvsEM5IogHPiI7T65CQvEQU-KlXEMBLEUJ6LLHfj25BqejTxtrbSRC4jt2LBCLkVft7iqSyJTMdvEG-Q4evtss9eM5VgW75AcWtHdCm9o3iYNd881eZ8LwAkhA3UUKPGfNrW2aeBRysXrlTN3pzvqJ_WeyN7tI20OwugMIMXhbO31CXDfzyBemjvQmTzoR2sfi6DFrsakBhv5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«ما
تنگه هرمز را در اختیار گرفتیم
. همه مین‌ها را پاکسازی کردیم. من گفتم: «پس چرا آنها مین‌روب‌های ما را هدف قرار نمی‌دهند؟» گفتند: «قربان، این مین‌روب‌ها
زیر آب هستند
. آنها همیشه در زیر آب فعالیت می‌کنند.» گفتم: «چرا این کار را می‌کنید؟» گفتند: «به‌طور کلی، وقتی مین وجود دارد، بیرون از آن منطقه
خصومت و درگیری زیادی وجود دارد
.» به عبارت دیگر، اگر در یک آبراه مین وجود داشته باشد، یعنی افرادی هستند که به سمت شما تیراندازی می‌کنند. بنابراین اگر زیر آب باشید، آنها نمی‌دانند شما آنجا هستید.
در آنجا دیگر هیچ مینی وجود ندارد، هیچ چیز دیگری هم نیست.
و اگر ببینیم آنها در حال حرکت هستند، خودتان می‌بینید چه اتفاقی می‌افتد.»
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22954" target="_blank">📅 15:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a7fc7dd57.mp4?token=v8Iki7M_a8SFtLRZyTbdBgui0DVPCU04J8CVhYFFWy3rhAOoGPYHFjoFB0zy5mmH1lFj_r3sYkzkAhdCSfnJR_pvAENvGbN43b1gIGb7niKLlqD6LlIg2xSJOlnAWZ83PPfXHcOZEhVrvGPcbFVtptid0uSw_HTvjsv-NQWkdFzl4Zk-2QzDMO7SYVrOTDK8zcKnMbQ_jJ4Ory4kex2ovhpxCPNqljJSyCJQo0U85Z5MDpEMOXKWR1WaACRwgBel2vW92YYi2QD9qbtQWNFVa3vCYeL6_gE6BY0wL4HAx5_UBr-K2eykwinVBqll5xBeyLnKup4CyV6uDEYVuS4eow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a7fc7dd57.mp4?token=v8Iki7M_a8SFtLRZyTbdBgui0DVPCU04J8CVhYFFWy3rhAOoGPYHFjoFB0zy5mmH1lFj_r3sYkzkAhdCSfnJR_pvAENvGbN43b1gIGb7niKLlqD6LlIg2xSJOlnAWZ83PPfXHcOZEhVrvGPcbFVtptid0uSw_HTvjsv-NQWkdFzl4Zk-2QzDMO7SYVrOTDK8zcKnMbQ_jJ4Ory4kex2ovhpxCPNqljJSyCJQo0U85Z5MDpEMOXKWR1WaACRwgBel2vW92YYi2QD9qbtQWNFVa3vCYeL6_gE6BY0wL4HAx5_UBr-K2eykwinVBqll5xBeyLnKup4CyV6uDEYVuS4eow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما یک درگیری نظامی کوتاه داشتیم. آن‌ها می‌گویند: «آیا ممکن است از کلمه «جنگ» استفاده نکنید؟ چون وقتی از کلمه «جنگ» استفاده می‌کنید، موضوع کمی متفاوت می‌شود.»
به نظر من، این یک درگیری نظامی است. ما آن‌ها را به شدت تحت فشار قرار داده‌ایم.
در مورد ونزوئلا، ما آنجا را تحت کنترل خود درآوردیم. ما در آن جنگ پیروز شدیم
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22953" target="_blank">📅 15:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وای نت
: کشورهای خاورمیانه، سقوط جمهوری اسلامی را به نفع منطقه می‌دانند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22952" target="_blank">📅 15:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">صداوسیما:  پس از بسته شدن دو پایانه مرزی شلمچه و چذابه به شکل یک طرفه از سوی عراق؛ از ساعاتی پیش مرز چذابه برای فقط خروج اتباع عراقی که قصد بازگشت دارند؛باز شد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22951" target="_blank">📅 14:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آسوشیتدپرس: رئیس‌جمهور لبنان به نباطیه در جنوب لبنان رفت.
جوزف عون در سفری
کم‌سابقه
به جنوب لبنان، در حالی که نگرانی‌ها از حملات مجدد اسرائیل افزایش یافته، از افزایش حضور ارتش لبنان و تلاش دولت برای حفظ ثبات منطقه سخن گفت. این سفر اکنون پس از عملیات اسرائیل در ارتفاعات علی‌الطاهر و ادامه تنش با حزب‌الله انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22950" target="_blank">📅 14:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رویترز: کشورهای بریکس بر سر بیانیه مشترک به توافق رسیدند.
منابع می‌گویند اعضای بریکس در نشست دهلی‌نو بر سر بیانیه‌ای توافق کرده‌اند که
اقدام نظامی یک‌جانبه هر کشوری را محکوم می‌کند
، اما برای جلوگیری از اختلاف، نام هیچ کشوری در آن ذکر نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22949" target="_blank">📅 14:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f69baa1d9.mp4?token=bGWJ4nqrHcD_c65ky8HDPxncI48Z57J1kCCsDYS42M1GcMxg-pQcp9LMLf9brcl0vyN80DyYOM__FXm-GsyD0n86ymznShPj_w-SJodanZHN0kHzxHwBQlYN6jhlW8gz1h62xHXCVWnUhYz8OBT-m1V3bh77skH-DIJG1_KkDDbSHc2DgxpwSx4WrBiYUbQRnVA1ZMLrx5G1Vqk7iI8fn9vZf6lgEFjxCe0iC-yTMpjq7VaGaGbvUj6F_KuSXM3yrltXS_G7Nv42fpqdlUTyt24jh_sF-h4qHiFwmXN1UDJ7ayCpex-Munu4VYiC9xVMn6rA5Gpdz_Z8pQhwkS2sXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f69baa1d9.mp4?token=bGWJ4nqrHcD_c65ky8HDPxncI48Z57J1kCCsDYS42M1GcMxg-pQcp9LMLf9brcl0vyN80DyYOM__FXm-GsyD0n86ymznShPj_w-SJodanZHN0kHzxHwBQlYN6jhlW8gz1h62xHXCVWnUhYz8OBT-m1V3bh77skH-DIJG1_KkDDbSHc2DgxpwSx4WrBiYUbQRnVA1ZMLrx5G1Vqk7iI8fn9vZf6lgEFjxCe0iC-yTMpjq7VaGaGbvUj6F_KuSXM3yrltXS_G7Nv42fpqdlUTyt24jh_sF-h4qHiFwmXN1UDJ7ayCpex-Munu4VYiC9xVMn6rA5Gpdz_Z8pQhwkS2sXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تهران (ونک) ی غذاخوری افتتاح شده که عرزشی سوز ترین رستوان شده به اسم بی بی که تخصصش  کتلت درست کردنه، حالا ی عده عرزشی فشاری شدن و بهش گیر دادن، میگن تو عمدا اسم غذاخوریتو گذاشتی بی بی و فقط کتلت درست میکنی.
@WarRoom
😂
✌🏼</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22948" target="_blank">📅 14:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: فکر می‌کنم ایران موشک‌هایی دارد که می‌تواند شهرهای اروپایی را هدف قرار دهد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22947" target="_blank">📅 14:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22946">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دیدبان اتاق جنگ پشت سنگر : یاشار سلام محاصره رو شکستن افراد مسلح همه رو تارو مار کردن نظامیهای رژیم رو @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22946" target="_blank">📅 13:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/063b6ca407.mp4?token=WIqDncXCbkM5pX59dO1yiE5BefUxc-SEwx4x81t3eGE3rNAaLS0MqtedBISo_qAdUthHXPD6-HtbGpw9CvvnxlOFvjwrSUn3x_7vaBpqrvK9VwCd7xciLvdXD8lW8zvth_ULuVL-YtNAAlW5MQN-vJ79yyIgJ3S985kbodu5WZXNCpaA8Fh6HFrLztSXigx6SM5U6yj5zdxvHk4bTFB7DIZVdk0Wl-bummLSV9gw1RubPOGk2DCfliErHZl4yAgOSOxPP8r3xkSPDjlFFtG3kD38UtWdJNWnjtncmY8iYcnPqyaKKDBUjycfdvY6doergpx5BMHpCwfZTLTnLHBkVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/063b6ca407.mp4?token=WIqDncXCbkM5pX59dO1yiE5BefUxc-SEwx4x81t3eGE3rNAaLS0MqtedBISo_qAdUthHXPD6-HtbGpw9CvvnxlOFvjwrSUn3x_7vaBpqrvK9VwCd7xciLvdXD8lW8zvth_ULuVL-YtNAAlW5MQN-vJ79yyIgJ3S985kbodu5WZXNCpaA8Fh6HFrLztSXigx6SM5U6yj5zdxvHk4bTFB7DIZVdk0Wl-bummLSV9gw1RubPOGk2DCfliErHZl4yAgOSOxPP8r3xkSPDjlFFtG3kD38UtWdJNWnjtncmY8iYcnPqyaKKDBUjycfdvY6doergpx5BMHpCwfZTLTnLHBkVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران: ما با قدرت بسیار زیادی تنگه هرمز را کنترل می‌کنیم. هیچ‌کس انتظار نداشت چنین اتفاقی بیفتد.
ما به‌طور متوسط روزانه ۲۵ قایق را از بین می‌بریم
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22945" target="_blank">📅 13:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd5f25930.mp4?token=m4iQ5M-L_Xk2mG-apJh6oeg__7NSbZO4ceaHN0IrSPF2YmFWRdJ9VOfCJQngLmj86dwGlMGTkYe1JaNTeoCzwHbLob7FLzyxx1YlxwYSoYDVTPcvMosaMOUlSrzpmk8uvIeCZ-ud4yo0e-2Rhz6n8CE-NW29v_0pHuslkgHpo-z_ODJll0dq_F_IM3Kn7Z4-Av94jBZ4yenZdA70GvI8BDe0DtETR3Ew2Fh9gF-2Za1weOB9ROpLhPiVStY5Q7h7uEpXwtDnTVqrfttOn2EeLIdqg5evqm7lNAV-DC6Z8eiebEhj1ohKHI1uRm3G78n9jmz043aaNy8RHv27l8BsNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd5f25930.mp4?token=m4iQ5M-L_Xk2mG-apJh6oeg__7NSbZO4ceaHN0IrSPF2YmFWRdJ9VOfCJQngLmj86dwGlMGTkYe1JaNTeoCzwHbLob7FLzyxx1YlxwYSoYDVTPcvMosaMOUlSrzpmk8uvIeCZ-ud4yo0e-2Rhz6n8CE-NW29v_0pHuslkgHpo-z_ODJll0dq_F_IM3Kn7Z4-Av94jBZ4yenZdA70GvI8BDe0DtETR3Ew2Fh9gF-2Za1weOB9ROpLhPiVStY5Q7h7uEpXwtDnTVqrfttOn2EeLIdqg5evqm7lNAV-DC6Z8eiebEhj1ohKHI1uRm3G78n9jmz043aaNy8RHv27l8BsNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: جنگ در ایران چه زمانی پایان می‌یابد؟
ترامپ: فکر می‌کنم خیلی زود؛ احتمالاً درست پس از انتخابات میان‌دوره‌ای.
آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا انتخابات را پیچیده کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22944" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a5eefe77.mp4?token=BIidLas-zo5kscQzl5FhSbP_qPT4N07WWUU3VFUE9uYY_S90BBDbllzwI18lDfBqlTI5MHG3lBrjKSSu8xLba5vEm6FhH7PvyJD3GDgyt9kJ5rG8sFJVxCUt-A8ld7wBpbclKhM_s-uiXGFtASuoWniWwAu_RHRqyncBCJZxzr36HYJX_tBbTmQQf6mmGymNQccXHbnia81htvqC5IuDY5W2TeLVL1E2B6jDkd5GNhI4Z5hvfkjlkBERh3nPCxvMuK9Yaa2ivzBPOCLxbHeLyffHGGDsLUkkVTaM8I1t3shnoBYjTOZ8cn2iILBeZntVJyd0pePKXxFUBF8UlyCUwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a5eefe77.mp4?token=BIidLas-zo5kscQzl5FhSbP_qPT4N07WWUU3VFUE9uYY_S90BBDbllzwI18lDfBqlTI5MHG3lBrjKSSu8xLba5vEm6FhH7PvyJD3GDgyt9kJ5rG8sFJVxCUt-A8ld7wBpbclKhM_s-uiXGFtASuoWniWwAu_RHRqyncBCJZxzr36HYJX_tBbTmQQf6mmGymNQccXHbnia81htvqC5IuDY5W2TeLVL1E2B6jDkd5GNhI4Z5hvfkjlkBERh3nPCxvMuK9Yaa2ivzBPOCLxbHeLyffHGGDsLUkkVTaM8I1t3shnoBYjTOZ8cn2iILBeZntVJyd0pePKXxFUBF8UlyCUwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا
ایران
مسئول حمله به خط لوله نفتی شرق-غرب عربستان است؟
ترامپ: فکر می‌کنم آنها هستند، احتمالاً آنها هستند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22943" target="_blank">📅 13:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ در مورد حمله به خط لوله نفت سعودی: حوثی‌ها نمی‌خواهند با ما وارد جنگ شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22942" target="_blank">📅 13:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ: ما آتش را در غزه خاموش کردیم و روند صلح را در آنجا تسهیل خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22941" target="_blank">📅 13:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دونالد ترامپ در مورد حمله به خط لوله انتقال نفت در عربستان سعودی: به احتمال زیاد، ایران مسئول این حمله است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22940" target="_blank">📅 13:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">.:
سلام یاشار جان من ساعت ۱۲ فردوسی بودم
دلار ۲۴۲ معامله میشد
اقتصاد مملکت داره منفجر میشه
خدا به مردم رحم کنه با این گرونی ها</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22939" target="_blank">📅 13:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ : اوضاع در ایران برایمان بسیار خوب است
همه چیز  به آرامی حل خواهد شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22938" target="_blank">📅 13:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ae38d90fc.mp4?token=viUJEi5avgFgfOleWhYybjZ8BTIr_CcR5JZW6bl8yPsF6UCAcjYXWwY5anjIw74mwnHxkWHL_ymHhyiSG6Wm4iA9L0GvNgMqzYSS2_WjAxiiygY7r4hMTMpbYEmIos7IhmdLibFTYML4aYCHM--zJoaDejG1lmedQa-7bc6iGjpRvBF6MzynBKuy9DwS-RleYkSr0jAWbaoM47uMl82CrUxZznXQXSIvUFgPENx9NinPiKXP_4vw2jwKjW0pRSYYb49kdsbE--gb7Ad8qXQtgYK2ZNTnAdNgsS-vQKc6YhAQKIqHgoOHlgfEQwZb_GBWsUjj7Crl3nobShSe2bV91w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ae38d90fc.mp4?token=viUJEi5avgFgfOleWhYybjZ8BTIr_CcR5JZW6bl8yPsF6UCAcjYXWwY5anjIw74mwnHxkWHL_ymHhyiSG6Wm4iA9L0GvNgMqzYSS2_WjAxiiygY7r4hMTMpbYEmIos7IhmdLibFTYML4aYCHM--zJoaDejG1lmedQa-7bc6iGjpRvBF6MzynBKuy9DwS-RleYkSr0jAWbaoM47uMl82CrUxZznXQXSIvUFgPENx9NinPiKXP_4vw2jwKjW0pRSYYb49kdsbE--gb7Ad8qXQtgYK2ZNTnAdNgsS-vQKc6YhAQKIqHgoOHlgfEQwZb_GBWsUjj7Crl3nobShSe2bV91w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ پشت سنگر : یاشار سلام محاصره رو شکستن افراد مسلح همه رو تارو مار کردن نظامیهای رژیم رو
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22937" target="_blank">📅 13:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFD1dsaAP-FmNG2QbsEsM0NDNYNjOeXRttussK4llbfvaP3ZwbMHf1PLgiQWRoUVgUz6ku4xEzN0yBYNjSsPMfks6ycpqmHmR8a5bVMOFVbC1WSdiUuuJNp2j2dD5iQ7MM1mvEOIplkvoW8uphlzcWzxpWHMlyKs61GWz-a2V9S0hUpQ0MmdXk1y5g_-y7TTaA5hWyy030cb5DfrF-fW8ODeCe8Pke_v5us4lzR6SSbycsFp0i21QGfd-eWS-nOxeMyc81tjJfXx_IDaDS0I8xbo40iQa45zGE5CByqyyPgle6m_OcSthB_qYA3W9F17cMhFDGeNKCuiIko-jZy5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Toc17647zkm0VV4r8i_HF8vb-zMXPzga0UmVkDqe7DS3ClKuGaYzd2-jvyN2D55VGn2e4ajyFGV0HibNm0_ye2KzAhEoxPs2Q6Em4I18glaAcFifZ5ZfJUB4acR_RXQjl-9VGPJhrV73GbTuI2LmRx5QvTs-3uo45Tue1Yg-UBJf9knGw1wga1yInDkaxvl8W4iBExq2NJ6J5z6HW_uRxgHHvF8Ffu7W1x9H88d5GvRqH9x9UDCi6pkCLJhfqi_YTlk6N7P2dQM5Hl1jHcY1nSA9Q2KrrarnWNibFeBmnYPl2T-S8C-WlMxr_9uv0X_CNS7RpQm0Db7aKxw1mVZ_lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک تانکر نفتی متعلق به چین با نام لیزا که در دریای مکران حضور داشت، تلاش کرد تا از تنگه هرمز توسط کریدور ایران وارد شود، اما سپس مسیر خود را تغییر داد و به عقب بازگشت. مشخصا آمریکا اجازه نداد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22935" target="_blank">📅 12:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نرخ دلار ۲۳۵،۰۰۰ تومان
دلار کف بازار ۲۴۰،۰۰۰ هزار تومان
تتر ۲۳۴،۶۰۰ تومان
بیتکوین ۷۷،۳۰۹ $
انس جهانی طلا ۴،۳۴۷ $(آخرین قیمت)
نفت برنت  ۱۰۴،۶۱$(آخرین قیمت)
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22934" target="_blank">📅 12:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d069691bb.mp4?token=ofDpfYYkwsxVC3BNDVNZahXyH2769qTx_A7QKkL89nLyEyZIlg1M8KzxP8mv6SkWKtIG5yFsuOQKpHiJi3B1mSa5hoPIbcTQwiiFg4Pv7GC4EakOPpCbMu7gU9krKh14cDlFRH_3ImDqqrliwqIKowjrXL8tV2qjxWjlQmWkkvv0Q6jiA_dJQBTA3FOq98fbrRmIiAgkWjXYmha2-fti42iE4Ne522Vi8cdgoq4RlNwnUFLk5GHQSMuiqR32oe-g1Ac8M45VJiFP0_q5LXrFmWtrZl4HERX4CJ6Wwh1TelvRRjWEr0XpkbNjkJaMlAAyXDog9eAEb4PDpysXHfX6bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d069691bb.mp4?token=ofDpfYYkwsxVC3BNDVNZahXyH2769qTx_A7QKkL89nLyEyZIlg1M8KzxP8mv6SkWKtIG5yFsuOQKpHiJi3B1mSa5hoPIbcTQwiiFg4Pv7GC4EakOPpCbMu7gU9krKh14cDlFRH_3ImDqqrliwqIKowjrXL8tV2qjxWjlQmWkkvv0Q6jiA_dJQBTA3FOq98fbrRmIiAgkWjXYmha2-fti42iE4Ne522Vi8cdgoq4RlNwnUFLk5GHQSMuiqR32oe-g1Ac8M45VJiFP0_q5LXrFmWtrZl4HERX4CJ6Wwh1TelvRRjWEr0XpkbNjkJaMlAAyXDog9eAEb4PDpysXHfX6bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بتسالل اسموتریچ، وزیر دارایی اسرائیل:
«اگر جنگ در همان خطوطی به پایان برسد که از آنجا آغاز شده بود،
دشمن چه هزینه‌ای پرداخته است؟
چه چیزی مانع از آن خواهد شد که دوباره وارد جنگ شود؟
کشته‌شدگان برای آنها اهمیتی ندارند. می‌توانید بگویید: «ما
۵۰ هزار تروریست را در غزه کشتیم
»؛ این برای آنها اهمیتی ندارد. آنها مثل ما نیستند که
حرمت و ارزش جان انسان
برایشان اهمیت داشته باشد. از نظر من، اصل اساسی این است:
اگر علیه من جنگی را آغاز کنی، اگر پیروز شوی، دستاوردی به دست می‌آوری؛ اما اگر شکست بخوری، سرزمین از دست می‌دهی.
»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22933" target="_blank">📅 11:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الجزیره: حوثی‌ها مدعی کنترل کامل ساحل دریای سرخ یمن شدند.
گزارش جدید می‌گوید نیروهای حوثی پس از پیشروی سریع در امتداد ساحل و تصرف شهر المخا و جزیره میون، اکنون مدعی
کنترل کامل ساحل دریای سرخ یمن
هستند؛ اقدامی که موقعیت آنها در اطراف باب‌المندب را به شکل قابل‌توجهی تقویت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22932" target="_blank">📅 11:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اتاق جنگ با یاشار : مرزهای بسته شده تا این لحظه، ۱- مرز چذابه ۲- شلمچه ۳- سومار ۴-بازرگان(گزارش تایید نشده) همچنین فرودگاه بین‌المللی بصره تمام پروازهای خروجی به ایران و ورودی از ایران را تا اطلاع ثانوی تعلیق کرد. @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22931" target="_blank">📅 11:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مسعود پزشکیان در گفتگو با یک رسانه هندی خبر داد که روز دوشنبه توافق عمان و ایران درباره مسیر مشترک تنگه هرمز در حضور وزرای کشورهای عربی حاشیه خلیج‌فارس امضا و به سازمان دریانوردی بین‌المللی اعلام می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22930" target="_blank">📅 11:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خبرگزرای AFP گزارش داده مذاکرات بعدی میان
اسرائیل و لبنان در رم به ماه اکتبر موکول شده است
. این مذاکرات قرار بود درباره ترتیبات امنیتی و وضعیت نیروهای اسرائیلی در جنوب لبنان انجام شود.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22929" target="_blank">📅 11:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22928">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اتاق جنگ با یاشار : مرزهای بسته شده تا این لحظه، ۱- مرز چذابه
۲- شلمچه ۳- سومار ۴-بازرگان(گزارش تایید نشده)
همچنین
فرودگاه بین‌المللی بصره تمام پروازهای خروجی به ایران و ورودی از ایران را تا اطلاع ثانوی تعلیق کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22928" target="_blank">📅 10:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اخطار
⚠️
⚠️</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22927" target="_blank">📅 10:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5080718a1f.mp4?token=k67KQhVv0oheUpywgD9YleFhU8zodQ8KRkeIGWYTmxSDm60Z5sWoL4lyDyCJPmfKOmYhLLMQ3PnPRsArujY2YmUecncxzEiobl0PqOkgxvtzcipNfWzuDict_oyvyS9eRo77Sh2GDX9BjXMk7ekHgNBGbWNgVPQvK9Ablraa5xz05cQZLX1kiHQXIdplUlIB8tAiP0SWbBCdNzW6FFqIrUX9gEOLsuQCAID8Vbj_XgkNcdEvugHnPoeGM1D0gOg5QcIi9igU6lI4IcEMzhibLToJWy_QSTHqLmdAJpPX3Tz13c8D_VEdbeOgx-23fNTvI0GHYhuptbot45cRlFxwWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5080718a1f.mp4?token=k67KQhVv0oheUpywgD9YleFhU8zodQ8KRkeIGWYTmxSDm60Z5sWoL4lyDyCJPmfKOmYhLLMQ3PnPRsArujY2YmUecncxzEiobl0PqOkgxvtzcipNfWzuDict_oyvyS9eRo77Sh2GDX9BjXMk7ekHgNBGbWNgVPQvK9Ablraa5xz05cQZLX1kiHQXIdplUlIB8tAiP0SWbBCdNzW6FFqIrUX9gEOLsuQCAID8Vbj_XgkNcdEvugHnPoeGM1D0gOg5QcIi9igU6lI4IcEMzhibLToJWy_QSTHqLmdAJpPX3Tz13c8D_VEdbeOgx-23fNTvI0GHYhuptbot45cRlFxwWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون درگیری میان
نیروهای نظامی و امنیتی و افراد مسلح ناشناس
در منطقه بخشان سراوان، پس از حدود ۶-۷ ساعت همچنان ادامه دارد. صدای
انفجارهای شدید و تیراندازی سنگین
از محل شنیده می‌شود و نیروهای امنیتی حضور گسترده‌ای در منطقه دارند و مسیرهای منتهی به محل درگیری را کنترل می‌کنند. گزارش‌ها از
انتقال مجروحان و کشته‌شدگان نیروهای نظامی و امنیتی
و استقرار چندین دستگاه آمبولانس در اطراف محل حکایت دارد، اما هنوز آمار دقیق تلفات مشخص نیست. به دلیل ادامه درگیری و محدودیت دسترسی، وضعیت غیرنظامیان و میزان خسارات نیز مشخص نشده و تاکنون مقام‌های نظامی و امنیتی
توضیح رسمی درباره درگیری و تلفات احتمالی
ارائه نکرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22925" target="_blank">📅 10:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa0dc375e.mp4?token=u1aDrmnjhqXmT_Jb4V5OTt46aIF-aTkINx4V9usNODgGSuFVh1zHAJPqkI1R3Cy-ItkaENnQgSbCFuX9MOdm3GOSXVxb4t3TXvAKLCXP-VyRQXMC5TNeK51fSX_GkZpU50Sipv_T7eozaDprsTt8du_1caQSiWJumOvt6OEeP24Ydpo05Gx96n1AdkHyveitLwasCEoX9wtYbeKs2y-2bHHfTiFwE33GhXCobh4fZpOIviSsyvDIsHIiSW2UkeNp-jXbOkjikuND2n_kx88Z5sHB427HcRsPytFY9mISj-bshuNcGSAuMRZWjjuDPBSfZ884XfxdZ1mt55pFqHbi3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa0dc375e.mp4?token=u1aDrmnjhqXmT_Jb4V5OTt46aIF-aTkINx4V9usNODgGSuFVh1zHAJPqkI1R3Cy-ItkaENnQgSbCFuX9MOdm3GOSXVxb4t3TXvAKLCXP-VyRQXMC5TNeK51fSX_GkZpU50Sipv_T7eozaDprsTt8du_1caQSiWJumOvt6OEeP24Ydpo05Gx96n1AdkHyveitLwasCEoX9wtYbeKs2y-2bHHfTiFwE33GhXCobh4fZpOIviSsyvDIsHIiSW2UkeNp-jXbOkjikuND2n_kx88Z5sHB427HcRsPytFY9mISj-bshuNcGSAuMRZWjjuDPBSfZ884XfxdZ1mt55pFqHbi3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری‌هایی در شهر سراوان در استان
سیستان و بلوچستان ایران
میان نیروهای امنیتی ایران و اعضای جبهه مبارزان خلق (PFF)، که پیش‌تر با نام جیش‌العدل شناخته می‌شد، رخ داد.
این درگیری‌ها پس از آن آغاز شد که نیروهای ایرانی به یکی از
مخفیگاه‌های این گروه
یورش بردند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22921" target="_blank">📅 10:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22920">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فایننشال‌تایمز: آمریکا حفاظت هوایی از نفتکش‌ها در تنگه هرمز را محدود کرده است.
سنتکام با به دستگرفتن کنترل غالب اکنون به نفتکش‌ها اعلام کرده پوشش پدافند هوایی آمریکا در هرمز دیگر به‌صورت شبانه‌روزی ارائه نمی‌شود و کشتی‌ها باید در بازه‌های زمانی مشخص، از جمله حوالی ساعت ۹ صبح، عبور کنند. این تصمیم پس از افزایش حملات شبانه ایران و برای کاهش هزینه و فشار عملیاتی نیروهای آمریکایی گرفته شده است
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/22920" target="_blank">📅 10:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab9a6cb30.mp4?token=TR98p4ieDtaJJlgxD3jrT7xXay8pwnyKdDflLLoMBvdXmFWvfALIAE8a5TghWID2Ckj8ZOa_2B3rSeAUL64UltDdqHU4zrWwSuidHq0Ql9f5XKfSQXrc0yK0SN8_uuRMaQ6lJwCLIuP_F5Ze1BSruZR_cGvRQWUjXNzlUdYHAFU27nJG1Zen0ppXcKyAJYO09B0FbLhjyVnqdnWNG52dydIyrkSvjpaSgYLQYcjUcJvYg34hUGi8fD014c19sYZ5TJU8gRKfFtiDvMNFk-ry0p4iqtfhSGKfok1AwfrxSsotvUlE3kftpqMFGE2eMOtv5FW3ObYL-SJFyUzAqoQPvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab9a6cb30.mp4?token=TR98p4ieDtaJJlgxD3jrT7xXay8pwnyKdDflLLoMBvdXmFWvfALIAE8a5TghWID2Ckj8ZOa_2B3rSeAUL64UltDdqHU4zrWwSuidHq0Ql9f5XKfSQXrc0yK0SN8_uuRMaQ6lJwCLIuP_F5Ze1BSruZR_cGvRQWUjXNzlUdYHAFU27nJG1Zen0ppXcKyAJYO09B0FbLhjyVnqdnWNG52dydIyrkSvjpaSgYLQYcjUcJvYg34hUGi8fD014c19sYZ5TJU8gRKfFtiDvMNFk-ry0p4iqtfhSGKfok1AwfrxSsotvUlE3kftpqMFGE2eMOtv5FW3ObYL-SJFyUzAqoQPvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ ، درباره انتخابات میان‌دوره‌ای: «اگر از نظر آماری نگاه کنید، وقتی رئیس‌جمهور هستید، چه جمهوری‌خواه باشید و چه دموکرات، به دلایلی اتفاقات عجیبی در انتخابات میان‌دوره‌ای رخ می‌دهد.
فکر می‌کنم در انتخابات میان‌دوره‌ای پیروزی بزرگی به دست خواهیم آورد.»
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22919" target="_blank">📅 10:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d9f9d1ac1.mp4?token=QEiAKPn1fe2CeM6om6jA-si79uloPo3Yrdj3eJBPmMPlsqqtAhH0y4xLEqE1QuIXDPBd2wYS6e5grCAwv5Cp6z4HnssdTM4qn6VisvMJbPG3snCvl5v2FTjfhIMYNmyREy9PUf1FzOz81aSA3sbiLIlMrSe4FFunBa7lN-Ippg6nRgWA-a14CzMYl74tD6avN2mypMTaxRvfgRL9C9ooo1nF0DZgpZSE0stl31vMcU1afSs2FQAGGMyzuZbwo8GAxAJGNCWMiWAvRKjRNoknqX5SMEmEjPtvi-nooz5j3tqioUym9q8bjqEYG48WGPHVTXEEg0gy8MpOa7YVJwY-6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d9f9d1ac1.mp4?token=QEiAKPn1fe2CeM6om6jA-si79uloPo3Yrdj3eJBPmMPlsqqtAhH0y4xLEqE1QuIXDPBd2wYS6e5grCAwv5Cp6z4HnssdTM4qn6VisvMJbPG3snCvl5v2FTjfhIMYNmyREy9PUf1FzOz81aSA3sbiLIlMrSe4FFunBa7lN-Ippg6nRgWA-a14CzMYl74tD6avN2mypMTaxRvfgRL9C9ooo1nF0DZgpZSE0stl31vMcU1afSs2FQAGGMyzuZbwo8GAxAJGNCWMiWAvRKjRNoknqX5SMEmEjPtvi-nooz5j3tqioUym9q8bjqEYG48WGPHVTXEEg0gy8MpOa7YVJwY-6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : من عاشق سیاست هستم.
به دوستانم که در حوزه املاک یا ساخت‌وساز فعالیت می‌کنند می‌گویم؛ چون واقعاً در ساخت‌وساز و ساختن چیزها خیلی خوب بودم: «آیا در سیاست بهترم یا در ساخت‌وساز؟»
@WarRoom</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/22918" target="_blank">📅 10:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d38f899a.mp4?token=cXFJAiqZ_P7T2G3WESl2XHh31gaSzsmaterVH495Pc46NPCK-s9N-5_wDOK6P49azbhYfgXwFI6qoaRcPbHm0mkVBNb5l8PI1m8SffrbcpHN_oakk6RApyf0-5aQnVbPyhItL7Ci9Loz6ZrBHyXPXIT5QdvBpjn5CmfUKqDRHUVPYYFuff6PVSJlb-1qIUShhxOas-Hzgel4TSAQ0PrvGOTJQOGKIALZFT-PfQfflfUESxZoin_T71I5QXIS_Sg0wtMobWyAwQIz0zz5CWNGxlGEt3rJdWmqrjbPJ7cK6vmYCJVjId2M3aZuuYUnADLFmm6ukQd6Colvowe1AL7YjYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d38f899a.mp4?token=cXFJAiqZ_P7T2G3WESl2XHh31gaSzsmaterVH495Pc46NPCK-s9N-5_wDOK6P49azbhYfgXwFI6qoaRcPbHm0mkVBNb5l8PI1m8SffrbcpHN_oakk6RApyf0-5aQnVbPyhItL7Ci9Loz6ZrBHyXPXIT5QdvBpjn5CmfUKqDRHUVPYYFuff6PVSJlb-1qIUShhxOas-Hzgel4TSAQ0PrvGOTJQOGKIALZFT-PfQfflfUESxZoin_T71I5QXIS_Sg0wtMobWyAwQIz0zz5CWNGxlGEt3rJdWmqrjbPJ7cK6vmYCJVjId2M3aZuuYUnADLFmm6ukQd6Colvowe1AL7YjYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره
آنتروپیک (شرکت سازنده هوش مصنوعی Claude؛ ترامپ مدعی است از فناوری آن برای برخی فعالیت‌های مخالف و سوءاستفاده‌های احتمالی استفاده شده است)
: «بیایید درباره آنتروپیک صحبت کنیم. آنها کاری انجام دادند که بسیار بد بود و ما آنها را متوقف کردیم. خیلی سریع متوقفشان کردیم. ما گاردریل‌هایی داریم. بزرگ‌ترین گاردریل این است که افرادی را داشته باشیم که به همان اندازه باهوش باشند؛ چون هیچ‌کس این موضوع را درک نمی‌کند، مگر اینکه ضریب هوشی بسیار بالایی داشته باشد — نه جو بایدن.»
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/22917" target="_blank">📅 10:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf8a770bd6.mp4?token=VIu0mYOfArfdZhiG0HObMln0Djr00HiKuDYJv_2XjPTiwiS1mpeI3Q4F1Ej_Nlf0y3U6lYmsL-E_DiYOO-UdsgCsifb7JUDZw9V9vTRhwvVuk6Tl0VJFDxkUSsY0YY64mU1kau2W7TVmTe2IubsFzFWoHKaZ8S3P7c05UgwolRvkWrJZB-M5DGuAtLN-5Hq39FIIsZM7n2s0waFMWZGUVKZu6f9_ZwnF-vhckDK7D9DsMccdv8YUrCzvQJgasD12Q986ymCaL1hvmMjBfBPWj2DslRsBsp1UMEubAtEz8diJvEbPdlFeXFxN4e2fDLlDnYGn6AP7rsl9hINVmP44UrwR39IqHLWz0LdMUbVdsgW7zjqr0SBUmlpavCB9dOdGC975Ir7gwqIMRtsQitvDKBYDvQVdnPnpIovNuigs2nlKkIyUiS0DwEGV-QKdZyAoedxvcm2rRP-haPhQ576rFQVnicn2GnPRKXNUztYBpCQoNHOveRLBmIMhdtv6bJfCEM6vIxvPXc2JZMKmXXoLzdFFFzbZ3xGwqxzU4XNBvkjzl2TCYreEO1yVebgG-QSSMQJNzB0uyBxrzxsIT8EvOZWGrf180A4B6_pJ5coWDJUf66TdeeVY6ndEWAKWkdfX-59uzFIpucoG2yeQ1VtIMiA1Dxk6tJEefDQweFOs72w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf8a770bd6.mp4?token=VIu0mYOfArfdZhiG0HObMln0Djr00HiKuDYJv_2XjPTiwiS1mpeI3Q4F1Ej_Nlf0y3U6lYmsL-E_DiYOO-UdsgCsifb7JUDZw9V9vTRhwvVuk6Tl0VJFDxkUSsY0YY64mU1kau2W7TVmTe2IubsFzFWoHKaZ8S3P7c05UgwolRvkWrJZB-M5DGuAtLN-5Hq39FIIsZM7n2s0waFMWZGUVKZu6f9_ZwnF-vhckDK7D9DsMccdv8YUrCzvQJgasD12Q986ymCaL1hvmMjBfBPWj2DslRsBsp1UMEubAtEz8diJvEbPdlFeXFxN4e2fDLlDnYGn6AP7rsl9hINVmP44UrwR39IqHLWz0LdMUbVdsgW7zjqr0SBUmlpavCB9dOdGC975Ir7gwqIMRtsQitvDKBYDvQVdnPnpIovNuigs2nlKkIyUiS0DwEGV-QKdZyAoedxvcm2rRP-haPhQ576rFQVnicn2GnPRKXNUztYBpCQoNHOveRLBmIMhdtv6bJfCEM6vIxvPXc2JZMKmXXoLzdFFFzbZ3xGwqxzU4XNBvkjzl2TCYreEO1yVebgG-QSSMQJNzB0uyBxrzxsIT8EvOZWGrf180A4B6_pJ5coWDJUf66TdeeVY6ndEWAKWkdfX-59uzFIpucoG2yeQ1VtIMiA1Dxk6tJEefDQweFOs72w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :
«رئیس‌جمهور شی جین‌پینگ قرار است
دو هفته دیگر برای یک شام رسمی خوب
به اینجا بیاید. ما با هم کنار می‌آییم. می‌دانید، من و او
رابطه بسیار خوبی
با هم داریم. مردم می‌گویند: «اوه، او از ما جاسوسی می‌کند.» خب،
ما هم از او جاسوسی می‌کنیم.
می‌دانید، ما هم در این کار خیلی خوب هستیم. ما اکنون
روابط بسیار خوبی با چین
داریم. قبلاً روابط بسیار بدی با چین داشتیم، اما حالا با چین خوب پیش می‌رویم.»
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/22916" target="_blank">📅 09:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22915">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65695ba78c.mp4?token=LL13FmngkOjREXl0WxHkBnOTZF9B4G9Rpo-Ao1BOOI8eSA3Brm3ELah1OpXVbFFm00RiKEiEibGHDjaVOr7KETsWFGj96fKTHkwkvCE7kWp25X_vv76sqm9-SOTPbNA9yS5p7gm5BPxkCUijLLZ5TOjYHkgi0ohiGz5B5sK6nI0VGa_TyK-4DPvTjWH_mAHhsFmRK2PYfqDrY8aDgZcWQQuUX7uYWshTz0QJFbLQIrW6pOqTGhX_poIbiBHn9Z54dPoTgMbHTkr_vvBNvo_wjxBCjWhBsugxTse6s2tiN3UqypL-2wrD7JJlwBs-h2-H4WHSMfjRzY0fyiiy8CFMsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65695ba78c.mp4?token=LL13FmngkOjREXl0WxHkBnOTZF9B4G9Rpo-Ao1BOOI8eSA3Brm3ELah1OpXVbFFm00RiKEiEibGHDjaVOr7KETsWFGj96fKTHkwkvCE7kWp25X_vv76sqm9-SOTPbNA9yS5p7gm5BPxkCUijLLZ5TOjYHkgi0ohiGz5B5sK6nI0VGa_TyK-4DPvTjWH_mAHhsFmRK2PYfqDrY8aDgZcWQQuUX7uYWshTz0QJFbLQIrW6pOqTGhX_poIbiBHn9Z54dPoTgMbHTkr_vvBNvo_wjxBCjWhBsugxTse6s2tiN3UqypL-2wrD7JJlwBs-h2-H4WHSMfjRzY0fyiiy8CFMsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
جنگ ایران بعد از انتخابات میان‌دوره‌ای به پایان خواهد رسید.
سؤال:
اگر جمهوری‌خواهان شکست بخورند، چرا جنگ تمام خواهد شد؟
ترامپ:
خیلی‌ها فکر می‌کنند اگر ما شکست بخوریم، من فقط عصبانی‌تر می‌شوم و خودم کار را یکسره می‌کنم، می‌دانید؟
در هر صورت، آنها بازنده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22915" target="_blank">📅 09:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وال‌استریت ژورنال: مقام‌های آمریکایی می‌گویند
ایران پیش از حمله موشکی ۱۷ ژوئیه به پایگاه موفق‌السلطی اردن، که به کشته‌شدن سه نظامی آمریکایی منجر شد، به تصاویر ماهواره‌ای چینی با وضوح بالا از این پایگاه دسترسی داشته است.
این تصاویر پیش و پس از حمله در اختیار ایران قرار گرفته و به تهران برای شناسایی دقیق اهداف کمک کرده‌اند. مقام‌های آمریکایی نام شرکت‌های چینی را اعلام نکرده‌اند و
دولت چین را مستقیماً به مشارکت در این حمله متهم نکرده‌اند
؛ پکن نیز خواستار ارائه شواهد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22914" target="_blank">📅 09:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تعطیلی مرز مهران تکذیب شد
‌فرماندار مهران: مرز مهران باز است و فعالیت‌های مسافری و گمرکی در این مرز برقرار است و هیچ‌گونه تعطیلی یا توقفی در روند فعالیت مرز با کشور عراق وجود ندارد. طی شبانه‌روز گذشته ۱۷ هزار نفر از این مرز تردد داشته‌اند که نشان‌دهنده استمرار فعالیت بخش مسافری مرز مهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22913" target="_blank">📅 09:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">العربیه : نخست وزیر عراق پس از حمله شبه‌نظامیان هوادار ایران به عربستان سعودی، گذرگاه‌های مرزی شلمچه، شیب و مندلی را با ایران بستند. احتمال می‌رود تسلیحاتی که برای هدف قرار دادن عربستان به کار رفته‌اند، از طریق یکی از این گذرگاه‌ها از ایران به عراق منتقل شده باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22912" target="_blank">📅 03:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فاکس نیوز از عرشه ناو هواپیمابر:  «یو‌اس‌اس جرج واشینگتن» روز جمعه ۱۱ سپتامبر در جریان استقرارش برای نبرد با جمهوری اسلامی آماده می‌شود.
این ناو هواپیمابر که حدود ۵۰۰۰ ملوان را در خود جای داده و توسط ناوشکن‌ها اسکورت می‌شود، آخر هفته گذشته هدف حمله موشک‌های بالستیک ایران قرار گرفت؛ این در حالی است که در طول هفته جاری نیز چندین مورد تبادل آتش میان طرفین رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22911" target="_blank">📅 02:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رویترز: نفت در پایان هفته بالای ۱۰۰ دلار ماند.
برنت در پایان معاملات جمعه روی
۱۰۴٫۶۱ دلار
بسته شد و نفت آمریکا به
۱۰۰٫۰۵ دلار
رسید؛ نفت برای این هفته بیش از
۸ درصد
رشد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22910" target="_blank">📅 01:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22909">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به مناسبت بیست و پنجمین سالگرد حملات ۱۱ سپتامبر، سازمان اطلاعات مرکزی آمریکا (سیا) ۶۹ سند اطلاعاتی محرمانه را منتشر کرد؛ اسنادی که در سال‌های منتهی به این حمله تروریستی در اختیار بیل کلینتون و جورج دبلیو بوش، رؤسای جمهور وقت، قرار گرفته بود. در میان این اسناد، هشداری مورخ ۱۰ سپتامبر ۱۹۹۸ به چشم می‌خورد که بیان می‌داشت القاعده «ممکن است هواپیمایی مملو از مواد منفجره را به یکی از شهرهای آمریکا بکوبد.» این اسناد یافته‌های کمیسیون تحقیق سال ۲۰۰۴ را تأیید می‌کنند و نشان می‌دهند که نهادهای اطلاعاتی به‌طور مداوم درباره نیات القاعده هشدار داده بودند. با این حال، مقامات اطلاعاتی اذعان کردند که این هشدارها نتوانسته بود ابعاد کامل فاجعه برنامه‌ریزی‌شده را به‌درستی منعکس کند. جان رتکلیف، رئیس سیا، اظهار داشت: «بیست و پنج سال پیش، حملات ۱۱ سپتامبر ضربه‌ای به ملت ما وارد کرد، اما نتوانست ما را درهم بشکند.»
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22909" target="_blank">📅 01:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22908">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سخنگوی وزارت خارجه:
منشا حمله آمریکا به لامرد، خاک یکی از کشورهای جنوبی حاشیه خلیج فارس بوده است.
عربستان، ژاپن و اردن تبعات رای‌ مثبت خود به قطعنامهٔ ضدایرانی آژانس را خواهند دید و ما آن‌ها را پاسخگو خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22908" target="_blank">📅 00:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سنتکام : در اعمال محاصره ایالات متحده علیه ایران تا امروز ، نیروهای آمریکایی
مسیر ۹۹ کشتی تجاری را تغییر داده‌اند(۳ کشتی جدید فقط امروز)
تا از رعایت کامل مقررات اطمینان حاصل کنند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22907" target="_blank">📅 23:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مقام اسرائیلی در گفتگو با کانال ۱۲  : تسلط حوثی‌ها بر تنگه باب‌المندب به دلیل عرض بسیار کم مسیر کشتیرانی و امکان هدف قرار دادن مستقیم کشتی‌ها با موشک‌های ضدزره بدون نیاز به سامانه‌های پیچیده راداری، تهدیدی خطرناک‌تر از وضعیت کنونی در تنگه هرمز محسوب می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22906" target="_blank">📅 23:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ تلفنی ، درباره ایران: اگر نمی‌خواهید کاری را که من انجام می‌دهم انجام دهید،
آن‌ها به سلاح هسته‌ای دست پیدا خواهند کرد.
اگر من یک سال و نیم پیش با بمب‌افکن‌های بی-۲ آن‌ها را به‌شدت بمباران نکرده بودم،
آن‌ها همین حالا سلاح هسته‌ای داشتند و از آن استفاده می‌کردند.
اسرائیل از بین می‌رفت و خاورمیانه نابود می‌شد. شما این را از این واقعیت می‌بینید که ایران آن همه موشک شلیک کرد. مردم، از جمله عربستان سعودی، واقعاً شوکه شده بودند که ایران به‌جای آن موشک‌ها، ممکن بود از یک سلاح هسته‌ای استفاده کند
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22905" target="_blank">📅 23:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">لایو جنگ یمن در گوگل مپ
https://goo.gl/maps/LkwoDWLT38cUL1mVA?withYashar
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22904" target="_blank">📅 23:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_tyX79KHp5fJwHMdBrhPrF6lsJIx0q7Ja83k6QMz4_UCI2i9pe-Dwv5BhsmN72GA-90WioBtMlfYvv1DsUfJ-hbzURPs7aLiillPdKXtP-hzu5FHRtTjjQsIs7UtZPu7Ief0Ot-zQoPMWKcC4CISBp_WqHklDuGm8WjTl4WAoosQ_B0Wqu3HTYIUIIU7mtrpklZbMkfB8CFh6PiaarGbIafXrwGesHVmYIrtup7EuFGO3mzQgbEr5foC3l3Ukg0izlV-byO2EekF8u9TH5Yha-UVBuRdG3YgTw31WFeymYh8Lsi826dpx3I6qrGAJEStIlPx7darBh7iQDl0g3Awg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «سود سهام عدالت
۵۰۰۰ دلاری ترامپ
» که قرار است به همه بزرگسالان در آمریکا پرداخت شود، به‌دلیل اینکه کشور ما در حال جذب
تریلیون‌ها دلار توسعه اقتصادی، سرمایه‌گذاری و موفقیت واقعی
است، از سوی «دموکرات‌ها» مورد انتقاد قرار گرفته؛ آنها امیدوارند این طرح هیچ‌وقت اجرا نشود، اما
اجرا خواهد شد!
برای مثال، دموکرات‌ها می‌گفتند تصویب
«لایحه بزرگ و زیبای بزرگ»
که یکی از بزرگ‌ترین لوایح تاریخ کنگره بود و توسط رئیس‌جمهور امضا شد، غیرممکن است؛ اما تصویب شد. یا
پرداخت ۱۷۷۶ دلاری
که سال گذشته به نیروهای ارتش آمریکا اختصاص دادم؛ تقریباً همه می‌گفتند امکان انجام آن وجود ندارد، اما انجام شد، نیروهای نظامی میهن‌پرست ما پول را دریافت کردند و از آن استقبال کردند.
وقتی من چیزی می‌گویم، منظورم واقعاً همان چیزی است که می‌گویم! سود سهام ۵۰۰۰ دلاری اجرا خواهد شد، زیرا مردم کشور ما شایسته آن هستند.
به جمهوری‌خواهان رأی دهید، آمریکا را دوباره بزرگ کنیم!
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22903" target="_blank">📅 22:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">روزنامه معاریو: نتانیاهو پیشنهاد حمله نظامی مشترک با کشورهای عربی به انصارالله یمن را داده است
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22902" target="_blank">📅 22:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22901">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ: ما انتخاب دیگری نداریم،
باید سخت با ایران برای پیروزی بجنگیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22901" target="_blank">📅 21:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏رضا نجفی، نماینده جمهوری اسلامی در آژانس بین‌المللی انرژی اتمی، به شبکه سی‌جی‌تی‌ان گفت: آمریکا ممکن است از قطعنامه اخیر شورای حکام به‌عنوان زمینه‌ای برای تشدید درگیری یا اقدام نظامی جدید علیه جمهوری اسلامی استفاده کند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22900" target="_blank">📅 21:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏نیروهای مسلح دولت یمن اعلام کردند در جبهه شرقی و منطقه نظامی سوم، با استفاده از توپخانه و تک‌تیراندازان، نیروها، مواضع و انبارهای حوثی‌ها را هدف قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22899" target="_blank">📅 21:45 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
