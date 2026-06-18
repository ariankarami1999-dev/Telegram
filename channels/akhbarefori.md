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
<img src="https://cdn4.telesco.pe/file/O1Pr5_Mi2_gIV_f_6QVQGagTiV3XtIV7Sn-7hMkatfTMScX28YRRw5Z0Z1VXqFSfBWQPtr0LaUSB1kK_xPkpI4DjCCLTD9MKQm9jVQkOxDKvhydOu29PHAIEznjUZqMLF9Iqotyv7rnMHLTt-_8t-no7IrpjBE12MAHCQqRQnUvNaNSaGRsBCvbqt65-9YQXozgqEheTVyk6i7i3f3m8-zatXoRGU9AROMd5AyDv8CyA0-5tE2tGmfAbl8X_jPU2CHpbQ5-V-NSZJ3H1lR46VqG9xYK0hyKM_OhZVOku9fLhr8nqSrsY4RZks0nCVpWlkK23fDieNa6UoNHDQh-PHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.48M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 01:58:36</div>
<hr>

<div class="tg-post" id="msg-660979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه مهرمبین</strong></div>
<div class="tg-text">🔶
فراخوان کمک فوری برای یک بیمار مبتلا به سرطان مغز و استخوان
🔸
یک مرد جوان اهل یک روستای دور افتاده ، مبتلا به سرطان که تاکنون هزینه های زیادی جهت درمان انجام داده است، جهت ادامه درمان نیاز فوری به کمک دارد.
🔹
در این مرحله از درمان نیازمند مبلغ 250 میلیون تومان است که هرچه زودتر باید پرداخت گردد.
❤️
هر کمک شما، امیدی تازه است.لطفا این پیام را برای دوستانتان ارسال نمایید
شماره کارت خیریه مهر مبین:
6063737004808968
شماره شبای مهرمبین:
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در کانال خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/akhbarefori/660979" target="_blank">📅 01:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7ca1e367.mp4?token=AQz-MkBTv28y-UOP_jaDZ9utBf5kyU06Kj-dXw0YUvDZ2D5FWzENVhIpEV6vSikVUQ45FLz2sH8_i0xsdIAlfG2-z5I34YvZlJ4ZuGq4DS9GaKREvD4taTy9NzDu0cNwWa_-PKZyCkxVlxhD_IoWI6D-PjPW-c64E-CIAy1V4qxngBc4VlnLPldgX0lpm2YeMHKNf9yCJfPE9Nz526qg1lrR5RVGCfW4ykGljnOwL38z2sI81lwROgmqQMXh-z_SxMfsm3DnK4hrExa7AtPbflEnpRE2lUmbr0TJV0xAMB835OiMrmX6RcH9QDMUgKoR2A9jNPN4e8sU_tL1VknXrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7ca1e367.mp4?token=AQz-MkBTv28y-UOP_jaDZ9utBf5kyU06Kj-dXw0YUvDZ2D5FWzENVhIpEV6vSikVUQ45FLz2sH8_i0xsdIAlfG2-z5I34YvZlJ4ZuGq4DS9GaKREvD4taTy9NzDu0cNwWa_-PKZyCkxVlxhD_IoWI6D-PjPW-c64E-CIAy1V4qxngBc4VlnLPldgX0lpm2YeMHKNf9yCJfPE9Nz526qg1lrR5RVGCfW4ykGljnOwL38z2sI81lwROgmqQMXh-z_SxMfsm3DnK4hrExa7AtPbflEnpRE2lUmbr0TJV0xAMB835OiMrmX6RcH9QDMUgKoR2A9jNPN4e8sU_tL1VknXrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور فرانسه: در مورد لبنان، نتانیاهو باید مسئولیت‌پذیری و عقلانیت پیشه کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/660978" target="_blank">📅 00:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660977">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
عقب‌نشینی تل‌آویو در پی هشدارهای ونس
🔹
در پی هشدارهای «جی دی ونس» معاون رئیس جمهوری آمریکا به مقامات اسرائیلی درباره توافق با ایران، سفیر اسرائیل در سازمان ملل ادعا کرد که تل آویو به «دونالد ترامپ» رئیس جمهوری ایالات متحده اعتماد دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660977" target="_blank">📅 00:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660976">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55984694b0.mp4?token=CtFTAHpLnXm9VEFLpEVU0GcjJ0sjA0SdLaY4jcUN0XL6JnxXChdyT8MGZ_fCcBM1f2A_NE-uBMDZ5kbY7WOyy3uqnA1Wvk7OTrNcwW0h578zQjbHYBuNgH-44uLrZQv6jl6BiCGZZSF9oPZU5699pmcoGtwOQJ2DbUgCwQU4wylezDs1_iVXppcxq1ostMa9pcZgyvi_1Q0XblHKqL4TORUAlr4RTLNjpfk7pVB_wz2OeA1XfkjfffNylzLCP6n2p1KAyBwmILINS2fmzFw9_tg5fqfBgTUi7nEaZZaiU25mhBFAKEdYRXyZtDS_t0HT-w3O4P8FkYcZTII1sMJdGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55984694b0.mp4?token=CtFTAHpLnXm9VEFLpEVU0GcjJ0sjA0SdLaY4jcUN0XL6JnxXChdyT8MGZ_fCcBM1f2A_NE-uBMDZ5kbY7WOyy3uqnA1Wvk7OTrNcwW0h578zQjbHYBuNgH-44uLrZQv6jl6BiCGZZSF9oPZU5699pmcoGtwOQJ2DbUgCwQU4wylezDs1_iVXppcxq1ostMa9pcZgyvi_1Q0XblHKqL4TORUAlr4RTLNjpfk7pVB_wz2OeA1XfkjfffNylzLCP6n2p1KAyBwmILINS2fmzFw9_tg5fqfBgTUi7nEaZZaiU25mhBFAKEdYRXyZtDS_t0HT-w3O4P8FkYcZTII1sMJdGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیراندازی در میدان تایمز نیویورک
🔹
طبق گزارش‌های پلیس نیویورک و مشاهدات شاهدان عینی، صدای تیراندازی باعث ایجاد وحشت و متفرق شدن جمعیت در محل شده است. مظنون دستگیر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/660976" target="_blank">📅 00:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660975">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
نورالدین الدغیر خبرنگار الجزیره در تهران: «اطلاعاتی حاکی از آن است که دیدار ایران و آمریکا در سوئیس برای فردا جمعه دیگر برگزار نمی‌شود، اما مذاکرات طبق تفاهمنامه ادامه خواهد یافت، هرچند ممکن است به سطح کارشناسی محدود شود و احتمال دارد بازگشت به پلتفرم قدیمی در مذاکرات صورت گیرد.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/660975" target="_blank">📅 00:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660974">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سی‌ان‌ان، به نقل از سخنگوی کاخ سفید: هیچ توافقی فراتر از یادداشت تفاهم وجود ندارد، اما بحث‌ها در مورد مراحل بعدی در حال انجام است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/660974" target="_blank">📅 00:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660973">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✉️
متن کامل رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
✏️
بسم‌ الله‌ الرّحمن ‌الرّحیم
🔸
ملّت پرشور و باوفای ایران
💬
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/660973" target="_blank">📅 00:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660972">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d947988c.mp4?token=JvxrO5-hfF48F9UwUwt1M_WMIWTBuYbOBYV82np3jVULnBoDIA1UXvua2-UuxpWHZLd9Mq3tAuFtmDBmiZMOQXxznAcwr7kPxOke0ki3JtK7hVS6ZqGGSMSuiunVdJgbLPs3_IYEnggGC7yiWC0SyiJ7GuiB5WumNnbFtgggFZYObxg9VquYDk6etuUyXEubm9hRuJNMMpHvybzz27p0G-pruZr4uPNJcDNIFMVDxD3YMs_EXU-n_TLkZ2c318AoXaEC3wmuhueeyhsq9J2JzpLD5EyEW_xth2X6apg5iYE5C-FXKL3TtAvLIVe3-5shC9Jc2tMdY_jNeEvrNG1B1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d947988c.mp4?token=JvxrO5-hfF48F9UwUwt1M_WMIWTBuYbOBYV82np3jVULnBoDIA1UXvua2-UuxpWHZLd9Mq3tAuFtmDBmiZMOQXxznAcwr7kPxOke0ki3JtK7hVS6ZqGGSMSuiunVdJgbLPs3_IYEnggGC7yiWC0SyiJ7GuiB5WumNnbFtgggFZYObxg9VquYDk6etuUyXEubm9hRuJNMMpHvybzz27p0G-pruZr4uPNJcDNIFMVDxD3YMs_EXU-n_TLkZ2c318AoXaEC3wmuhueeyhsq9J2JzpLD5EyEW_xth2X6apg5iYE5C-FXKL3TtAvLIVe3-5shC9Jc2tMdY_jNeEvrNG1B1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فشار کره‌جنوبی بر فیفا پس از حاشیه نژادپرستانه
🔹
پس از انتشار ویدئویی از برخورد نژادپرستانه با یک یوتیوبر کره‌ای حین تهیه محتوا، هواداران و فدراسیون فوتبال کره‌جنوبی از فیفا خواسته‌اند این موضوع را بررسی کرده و با هواداران متخلف مکزیک برخورد کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/660972" target="_blank">📅 00:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660971">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqwiWzJEQbuLd1RNez_NFi0pMZ73XASh9mF32SP1FAoZPHItgOtXVePp57cUpGRrLmNLKsfmJc5BIPGxLFnFrm1qlZU6cbnlYg4mASzgmDs_w9-CLjOKO23EePq08vRz-KjHsIp3YVY46hhavWtpEZPcHWSQcb0yFErt8ixe8etmOxGb7saxS1oXTfgUxtZFuwgGvV69fNTlV4swSoC7gOZNkWCeCfhKa8cv4GlprCYXxF5mf4wLXnS9wlhBhRGD2wwFex17IIuSeXqh26nGGTitu_TpGoUwa648Aog2NTzNLi-a2rHAFuj-CN5x2fzHyJTsRbT3ed_9fmdTT5ublg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
برای اولین بار در تاریخ، تیم داوری یک مسابقه از جام جهانی با حضور سه زن
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/660971" target="_blank">📅 00:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660970">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
آغاز واریز حقوق خرداد بازنشستگان کشوری
معاون صندوق بازنشستگی کشوری:
🔹
حقوق خردادماه بازنشستگان کشوری آغاز شده و تمامی واریزی‌ها تا ظهر فردا واریز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/660970" target="_blank">📅 00:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660968">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiU4lLEgHnJYgOfOIarz-a9aNtSOL6H3Mk92kgDqOrNt6ZE1xYS_mhsMe4pV13gX-PFEsnoQNarLhIuvlu8k5d7I81ZiEVCP8neFioZCVT2KWYBev1qqWt6fQU1JfznXB4ZGHEHkIZQ2fX2yp8oVs1Oe5x8L9Aq6xXJ0lqTYWpD5XQrzHdiFpKkHLZVUmexP7MaWPTkbssqCqRRKIXelEyVoCTJiGLG9NsVPiXs66ze2_FZEpxGqwrQu9eLfdYg8goh4pK4eqF62NVaG2S8Dvpc1GnA20WWUXLXFPZknKolSSao0BLIY9-mt2othurxJq7f6YYqmeMZcOvjfQEFE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/akhbarefori/660968" target="_blank">📅 00:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660967">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
سرطان در ایران ۲ برابر میانگین جهانی رشد دارد
دبیر کمیته ملی کنترل و پیشگیری سرطان وزارت بهداشت درمان و آموزش پزشکی:
🔹
ابتلا به سرطان در ایران تا سال ۱۴۴۰، دو برابر میانگین جهانی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/660967" target="_blank">📅 23:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660966">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ویتکاف: بازرسان آژانس راهی ایران می‌شوند
آسوشییتدپرس:
🔹
ویتکاف اعلام کرده که ایران از آژانس بین‌المللی انرژی اتمی دعوت خواهد کرد تا از تأسیسات هسته‌ای این کشور بازرسی کند و روند شناسایی و کشف محل نگهداری مواد غنی‌شده ایران را آغاز کند./ نسیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/660966" target="_blank">📅 23:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660964">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
مکرون: درباره توافق پرسش‌های زیادی وجود دارد و معتقدم که جنگ پایان نیافته است. نتانیاهو باید در ارتباط با لبنان «مسؤولیت‌پذیری» نشان دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/660964" target="_blank">📅 23:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660963">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrZa4HLPq8xBTc6ab1WsBNgEBdLPp_9zFIQhH74TzS4_1zpd5jZNwuxFzWlVXko98MYpm4bLwKjUoJbGZXzFN-DG_BjSCuY0a2-BPEQ1j1XKUQujZWeTUhlRPxaqjlDc9WS1xNo7qwmwKqbvf2A3nz9RAcNY2jkxLwi_d49ZeZZMQwmEN70nuFyWzfBNKmAKpas6pK1dQEKbntXfaI0Bv1eiuOJcrQICW1bR1nd8zwUpH64v49GzUAH1-qgbHaH-N0PhNbtUfxmTxCDBRWx-X3m-l4CmU1W5AjOY2d4-ZwYuqkiTnXUOm-GB-N8e2rbayFpOs-yGCgu3SrVEhlXugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترافیک دریایی در تنگه هرمز پس از امضای توافق صلح میان ایران و آمریکا افزایش محسوسی پیدا کرده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/660963" target="_blank">📅 23:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660959">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نوحه</div>
  <div class="tg-doc-extra">میثم مطیعی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/660959" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پک هیئت قرار  ویژه شب چهارم محرم
🖤
#محرم
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/660959" target="_blank">📅 23:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660958">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLtanKFisfcjCj_9u2WeKKkueyDhqFTvjs-yQpKRVbs4jQ4FUVf9cxronn66Nw1yCopvDaOIM2Fh72_zJsudXT0U7dkv5OkQijXSQkJLjlPUhdDmAni6rudW7p4lZrdCthhDMDgZz-Pl_F1uK0gO84GB-aufB8JDAycj6_S1PD1kUUG9qyXL9HxBavh8Qtsv0VDdBTHVQqN3MxvlnojiDUwgDWXNIrnYL7tbZdvy7R87W5ZvYf2QZ0XYf-deWMCIEcOF1lpN63tl4q8Y08PN1WfNNVkgMCXT2pEMEPsAhofkqXYoP1UId-V_ITX4VbICWVtlzwQDHF4iRhJyZol1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصیبت‌های کوچک؛ آزمونی برای شکر و صبر
🔹
امام (ع) هشدار می‌دهد: اگر انسان مصیبت‌های کوچک را بزرگ کند و ناشکری نماید، گرفتار بلاهای بزرگ‌تر می‌شود. زندگی خالی از سختی نیست؛ این حوادث گاه آزمون، کفاره گناه یا بیدارباش‌اند. صبر و شکر در برابر مشکلات کوچک می‌تواند…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/660958" target="_blank">📅 23:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660957">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-pvCh7H1TopgjApBrc5wAXfvNFioe21qAD1gqqvZXu4YacV-2Jpfhfu_8nAcgel_uYsnMKEyC4CE8ppuRuJZR9eWah7vu_DQV9DrkwlD-FKj5D4-A9Lfr0u21-jRJvaNhq58-dkzTHCKZ145huFwa_gLowRv7MLYwKAefdLPbELYNM0T2-AEeYQQdwdGfKP4HIYuMGFXYPy9nmFFUZJb1jhgZ_eaPjGGl6L6iaAUKHHMPULTG7gF2pY4FdLk2V-6KgZEb3OBtzZFvl4xWnAxeLq2EGoBgdZwzu1UAdsv6gB9AsWDwLec4Kh_YXLQV_SQO-sAA8S8UXzwvE1D3UNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون فوتبال ایران برای بازی بعدی در جام جهانی ٢٠٢۶ مقابل بلژیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/660957" target="_blank">📅 23:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660956">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkT-R5PDsMEyvRC8wEjVmfN6zx2odBEg0DijJzAEqWeLUd3foqgIuH0AO7w1T5c7k8zHQlPobAlIk5g13YJeUEyDTELf7q3vyMbpzX5F95tVCuz9Cd1ULSnEbXTpggZjafg7WpPJE5-lAIr0TGZB5u9fLUNWBqdZHYY-l8Aj5B7tvI98uPuzF8FHpkWP12JJcLJZJx6jCtVJ2IpiueA5MG4nuw5MelIB0tQFVFsFDd4XVNpPP9txm4RwNTOjamKTmNsGgaKiqIwH9fnanGSn2PFnCDCmFCtwS3iruSPfiKvG7ibd46_pFmB64Fhz996rg-9GwmRB1RwYRScNNC_rOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیرخوارگان حسینی
🔹
مخاطبین عزیز خبرفوری؛ پویش بزرگ شیرخوارگان حسینی جلوه‌ ارادت کودکان شما به آستان حسینی است.
🔸
برای شرکت در این پویش کافی‌ست  عکس‌های فرزندان دلبندتان  را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/660956" target="_blank">📅 23:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660955">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
نقطه عطف روابط ایران و آمریکا در روز سرنوشت ساز
👇
khabarfoori.com/fa/tiny/news-3223984
🔹
پیام رهبر انقلاب درباره تفاهم‌نامه ایران و آمریکا/ بنده نظر دیگری داشتم؛
👇
khabarfoori.com/fa/tiny/news-3224046
🔹
افشای جلسات فوق‌محرمانه ترامپ | خشم ترامپ از افشای مذاکرات جنگ ایران
👇
khabarfoori.com/fa/tiny/news-3223914
🔹
ادعای عجیب سازمان اطلاعات آلمان درباره ایران
👇
khabarfoori.com/fa/tiny/news-3224032
🔹
پسری که همه چیز دارد | رضا پهلوی؛ شاهزاده لاکچری و روایتی از یک گسل طبقاتی
👇
khabarfoori.com/fa/tiny/news-3223831
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/660955" target="_blank">📅 23:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660954">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1E3WSYcPfjuEbYUuIRTgmVO5VRDqo9CzHdGM64qzWP2nwOh6bgNfVCTjD8o7vAE0kykIE_97_aBhxiVezcr3ESqLLQ183HuFkTdPVlNQVMerjZBJhUacir3oZ1KIsGH_At-R9ODhAKVs51sxtP2-zqWXW4Pf0MmedfrWviuTl-eo_FU3PjKqd5Mst6ia9quAmonXmHY0xqnr2ppY1yzNCjnvb3zi6pg-x7Umkve-YKK018hY2jNx0NLIrT5Faks0JlurVlgbiKYv-ELVhK8hfy_GYX8CukasywzpqB5avHN8U7ZFZHRnUnAV5Nllob00h5WJKZpWNziUddYR9rCtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیت‌کوین به زیر ۶۳,۰۰۰ دلار سقوط کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/660954" target="_blank">📅 23:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660953">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
المیادین یه نقل از یک منبع آگاه:
هیئت مذاکره کننده ایرانی سفر خود به سوئیس را به دلیل تداوم حملات اسرائیل به جنوب لبنان متوقف می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/660953" target="_blank">📅 23:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660952">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
نبیه بری، رئیس پارلمان لبنان: تأکید می‌کنم که موضع لبنان و
پایبندی حزب‌الله به آتش‌بس، تا زمانی که «اسرائیل» به‌طور کامل و همه‌جانبه به آن پایبند باشد، ادامه خواهد داشت
./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/660952" target="_blank">📅 23:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660951">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✉️
متن کامل رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
✏️
بسم‌ الله‌ الرّحمن ‌الرّحیم
🔸
ملّت پرشور و باوفای ایران
💬
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/660951" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660950">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a555eaaf9e.mp4?token=YBa5yOjcPFsJoM7uM3sDKT4VgjVCwM7i8dSksn4rXKPft5PnfetM8_mzXvOgIptScpLurUDgeFL9lPoCng835bOUrH_0o9S3390TgYQX_tE2YY_zk_l-rCldUH0ysfIcRn2j2Ie4DbyD8Rvuze50IVz8_LTPBtvb8JVLUI8DAEVCrTYDQEVSqbhUcB17uL1rqS18nhiDX-fvx7pV4Jx01aO-EPD1hFwhK8RSWfbRwdgmqDkKGuRVRuSIgnZAaatZVtZ_-AGBKwY2zkkeeU-Kn8uSdNCk9odMtrMPJkwrSWmTKGQXfQhpgC5inf6-wVLYJ2ySgCxfLrnshppYCSSO3bcAVRaJ2IgiFoWIiXxQQTiV7f-juIWau5VrxGbfGN-GC6Lw2wSqbtv1Pnjbn14-0QNS7kG1YKkHifQ4J0SHf4SO3cR3zJDhOXaG6YO4J3UGu7Nux5Qaac8Z_Eg6qiqWTTUK4mhmd_4tYEgKjgREHPxRmotcgv9MNH9txObm00Y36_LHhafoiiU_an-ogbKmQdLUKw61ok92gbuluVpzYG5Z3N5oYG_-AL2Ozs7ce4CydRNyC6OoODubQGtRmvGTaZ5Te7DjD01zaCA7xgIHUm76bMzAiW3KDrioXEw5oxUOKX-snSyvmKeDvTClo3RDdiaSSYd7x92xyJynYYo1hLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a555eaaf9e.mp4?token=YBa5yOjcPFsJoM7uM3sDKT4VgjVCwM7i8dSksn4rXKPft5PnfetM8_mzXvOgIptScpLurUDgeFL9lPoCng835bOUrH_0o9S3390TgYQX_tE2YY_zk_l-rCldUH0ysfIcRn2j2Ie4DbyD8Rvuze50IVz8_LTPBtvb8JVLUI8DAEVCrTYDQEVSqbhUcB17uL1rqS18nhiDX-fvx7pV4Jx01aO-EPD1hFwhK8RSWfbRwdgmqDkKGuRVRuSIgnZAaatZVtZ_-AGBKwY2zkkeeU-Kn8uSdNCk9odMtrMPJkwrSWmTKGQXfQhpgC5inf6-wVLYJ2ySgCxfLrnshppYCSSO3bcAVRaJ2IgiFoWIiXxQQTiV7f-juIWau5VrxGbfGN-GC6Lw2wSqbtv1Pnjbn14-0QNS7kG1YKkHifQ4J0SHf4SO3cR3zJDhOXaG6YO4J3UGu7Nux5Qaac8Z_Eg6qiqWTTUK4mhmd_4tYEgKjgREHPxRmotcgv9MNH9txObm00Y36_LHhafoiiU_an-ogbKmQdLUKw61ok92gbuluVpzYG5Z3N5oYG_-AL2Ozs7ce4CydRNyC6OoODubQGtRmvGTaZ5Te7DjD01zaCA7xgIHUm76bMzAiW3KDrioXEw5oxUOKX-snSyvmKeDvTClo3RDdiaSSYd7x92xyJynYYo1hLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظم عجیب و با شکوه افغانستانی‌ها در شب چهارم حسینیه معلی شبکه سه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/660950" target="_blank">📅 22:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660949">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
عبور رایگان کشتی‌های تجاری از تنگه هرمز به مدت ۶۰ روز  شورای عالی امنیت ملی:
🔹
طبق یادداشت تفاهم اسلام‌آباد، کشتی‌های تجاری متقاضی عبور از تنگه هرمز باید درخواست خود را به مدیریت آبراه خلیج فارس ارسال کنند و به مدت ۶۰ روز هیچ هزینه‌ای از آن‌ها دریافت نخواهد…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/660949" target="_blank">📅 22:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660948">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77b8275dc.mp4?token=g6LglDqqm3Qqh6bboBnExpWNG-WO4s-FPhXt8xDs4RHKNMhiu7snvHVjrDpcJ1YrKOTiBftqi9DgCz0TRAfarv8p7EKAVZ--h6FC4myWLwBRo-xYaXed7PYgId3EDDFgpPerWrrQMr8ymuhaCK0hNYhEPGCx3IFcbwrRgMLgEq83a2EAXWz1Cc691jjmiLWFebXn2Bdaoy6BhtuffOK_tkFWh9fFLSMh9vfBWJB-XyaSVNHGiH5HSLe1Lm-2L_x4m9K6sT4EMiC_xXwrFKx7EqES3TaCrQZ5jagQEnVE2UNMfEaZP7zAYGPRA8vrEq6Kmkj3Cd_BnBQ0dN8rRIKP6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77b8275dc.mp4?token=g6LglDqqm3Qqh6bboBnExpWNG-WO4s-FPhXt8xDs4RHKNMhiu7snvHVjrDpcJ1YrKOTiBftqi9DgCz0TRAfarv8p7EKAVZ--h6FC4myWLwBRo-xYaXed7PYgId3EDDFgpPerWrrQMr8ymuhaCK0hNYhEPGCx3IFcbwrRgMLgEq83a2EAXWz1Cc691jjmiLWFebXn2Bdaoy6BhtuffOK_tkFWh9fFLSMh9vfBWJB-XyaSVNHGiH5HSLe1Lm-2L_x4m9K6sT4EMiC_xXwrFKx7EqES3TaCrQZ5jagQEnVE2UNMfEaZP7zAYGPRA8vrEq6Kmkj3Cd_BnBQ0dN8rRIKP6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شریعتمداری: با مصادره اموال آمریکایی‌ها و متحدانش از طریق تنگه هرمز باید از آمریکا غرامت بگیریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/660948" target="_blank">📅 22:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660946">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S987nQZYpUk2UGjXQx8_nqUGqyCOZLiveodwMysFkLQFluWnG3IZca-U3P0_TU1BLQHCIiejESWZzS5FrkskYJw8p9krfpyWI24qGZS-BDcCYUnHTndWs_OBKswe-0tpHQzH_sC6gy8zJ0mNtz_8BgSjLlAQgmyun9NwrAwIguqBSPvwcYNAZ-OXqX7IlHRULLe8_rDdh5mgOYvMachDkNa02Ctme-R9oCcqyuU95qDJdkr06x0XOpsgDAlpOne29HEcqGBWigBPfi_UvtS7G8SanBF5FrqoWd2aLmRutPJ5t1XreXDpWiHJZ97427Gd4e6XVwHWWkaMUxmrJ6N11A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رامین رضاییان بالاتر از اولیسه در صدر خلاق‌ترین بازیکنان دور اول جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/660946" target="_blank">📅 22:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660940">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImpBFIpRPXpceBkv_RlEEt70OpOjpNr90qmAGq49wuexjv_qXCPxvGpGpmCs6HB4YnkfDLwfU2jD6-1zB-C9FQ8BbL2NYYXrn3ZSzVzY1ISeEa0dVuGEOrkoE9S3nJ7P_ztD77VPF7wZAw-kwDTphMo1pFpwg38rQqSsWsOaFkOXJrgDWuJdEl83okJ9t-kAh_w0SDhF5Mi9Y2oyB4iW5rUwAsrGO29nwrXPp2-GNUX2Xmx9pWWvqGLnofJEi2S7LxoOnrBQxII2P78D94wRgEI05V3E7-ZMg_Ms8-jVcsQkcBXBA205QUxFE_6ONjilVyX-svuVy_mLhTtT-bHEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/925a0b51a7.mp4?token=YQIn3DVSDqetukUgLqJytoxhMgS3tqPUKDI67bfMvFqPtVeiTG1Lm-6F1W_0E-enz7caNWaAPWC0-NG3j7mJ1PlvZQb0TWMRH0vKUmCFl3iydn-hysADxcMmhEIyef-VMuZh9WasuxFDhGpbwmkzOMAEQIz5J9LYa3t0Yyo0I8HwoZV0q_aM5x-ERTKLZySYqJhIsZqAwytyxEcxTiZS7peEiREHTeJdSDJNQzZD_s6J7aAkhe4s9-Vziz0bECzkXwxKj-PCeBOKkbq90RPJOq9OnoPUzG0NqJlFRK5CpryjVTg8QyzPSsbtvzGJUlFgI0BtdMfHm_VfpT3WYZ4XlHgmzIoy6CUQM-Rwz6gyyWj3pe9CGpWMSUlEy9qkzAPNW6019rtVXqoUUUUwDTe_vpEUrg4eNGgwRnLN3WQZpwWCwky0nWpPC3hl6iCP9t-cG2eGnJunR8wd2Py-0xaNJgl5SzAP_OpcM20PfaOEb4YwTB8Um_h4x7QqTgy1MQrKG_Q3_zF9cAQ6GGtgZdM7XDcBca3Fewh-_kKvjv2eYLLpAemWBhlDKqw8rsDFZjxhNVrNOnYn3SHzMp4or15GUmJSO2x5dVxZZSGI-E2ZGPMPbpdDQTecilYw3o1qEcyeKbg0rH-I3HzKiVFdScMVm9GMbVU9CRR9INS0V3NDeQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/925a0b51a7.mp4?token=YQIn3DVSDqetukUgLqJytoxhMgS3tqPUKDI67bfMvFqPtVeiTG1Lm-6F1W_0E-enz7caNWaAPWC0-NG3j7mJ1PlvZQb0TWMRH0vKUmCFl3iydn-hysADxcMmhEIyef-VMuZh9WasuxFDhGpbwmkzOMAEQIz5J9LYa3t0Yyo0I8HwoZV0q_aM5x-ERTKLZySYqJhIsZqAwytyxEcxTiZS7peEiREHTeJdSDJNQzZD_s6J7aAkhe4s9-Vziz0bECzkXwxKj-PCeBOKkbq90RPJOq9OnoPUzG0NqJlFRK5CpryjVTg8QyzPSsbtvzGJUlFgI0BtdMfHm_VfpT3WYZ4XlHgmzIoy6CUQM-Rwz6gyyWj3pe9CGpWMSUlEy9qkzAPNW6019rtVXqoUUUUwDTe_vpEUrg4eNGgwRnLN3WQZpwWCwky0nWpPC3hl6iCP9t-cG2eGnJunR8wd2Py-0xaNJgl5SzAP_OpcM20PfaOEb4YwTB8Um_h4x7QqTgy1MQrKG_Q3_zF9cAQ6GGtgZdM7XDcBca3Fewh-_kKvjv2eYLLpAemWBhlDKqw8rsDFZjxhNVrNOnYn3SHzMp4or15GUmJSO2x5dVxZZSGI-E2ZGPMPbpdDQTecilYw3o1qEcyeKbg0rH-I3HzKiVFdScMVm9GMbVU9CRR9INS0V3NDeQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
ویژه شب چهارم محرم طفلان حضرت زینب (س)
🥀
رو سفیدم میکنند و فخر مادر میشوند
نوجوان هایم سپر های برادر میشوند
این پسر ها پیشکش های من و عبدالله اند
صحبت جنگ و جدل باشد قلندر میشوند
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/660940" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660939">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
عبور رایگان کشتی‌های تجاری از تنگه هرمز به مدت ۶۰ روز
شورای عالی امنیت ملی:
🔹
طبق یادداشت تفاهم اسلام‌آباد، کشتی‌های تجاری متقاضی عبور از تنگه هرمز باید درخواست خود را به مدیریت آبراه خلیج فارس ارسال کنند و به مدت ۶۰ روز هیچ هزینه‌ای از آن‌ها دریافت نخواهد شد و این هزینه‌ها توسط دولت ایران تأمین می‌شود.
🔹
همچنین کشتی‌ها باید در مسیر و زمان اعلامی عبور کنند تا تردد ایمن انجام شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/660939" target="_blank">📅 22:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660938">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0dsOglaQEDjHLkwAJ9Cn4uTgkSoLHgyzzsGPRlLdtDyd7fIxz615E0JHcIaaR-FFqmlO0UTDsastEM5E67A2TT3QfV9aTaq0I3pystJfOyRFQ1gyBwgDqUDWkNs9lmhUHWcTlL78HXj1gK-DlmkkfJCAli03J8XN6RqeyG61HzLnko1a3AUXhbEA05_NNzZTV3Vv9s4eoXmfDS8c4g3W0kWphlBPTAxYkVQ-u60TKb5dwB8eMxNdYigoJOfXWTc-K78JVKmS7nc684TZjQ5EBgl5kQtwn19vuYyMN9jUhnljJHmha3sJ8oJ5hHh3IuCqEbjeXqWOcp1715gCL3wCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علی قلهکی: رهبری با این متن موافق نبودند، شروط ان محقق نمیشود.امریکا بعد جام جهانی از برنامه اصلی رونمایی میکند؛ اگر اسرائیل پیشدستی نکند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/660938" target="_blank">📅 22:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660937">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
وندی شرمن: دونالد ترامپ جنگ خود را با تقاضای تسلیم بی‌قیدوشرط ایران آغاز کرد؛ اما در نهایت چه چیزی عایدش شد؟ به نظر من، خود او کسی است که عملاً در برابر ایران تسلیم بی‌قیدوشرط شد...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/660937" target="_blank">📅 22:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660928">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RqT8LgvDMhCF6aCHIjRkgqMNpA7swUxkBLEzU-oq8-uTIuOtWX9lfp96CpjR673PdtBre75BiA3vU59DVgUfJZTloa9Q93YMOQ8YTGMB1GsenxQy24rDxSZNLOoO7bAAC_iQE4Eq0gC9E8Q9otyaXRGknnK1_sv0b4kmCgnMvDDyjAwvfLSwokKBfANhQ2JC9dzO5NsToi6P0PWi9zjUvxK0RTWKzzWggRmRISBota_e_3Xtrxk0zO5G6mz4xChFo7FMh-FBUS-PedFuP6QZv4bmqjpN2__st0LQBNNlfpK92g9U7ZNE-7nsoFfdybib1uZ4CHVzE2WPaCbipD738w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSXe61gcQ_4t_8T9-sRTnEaLvJj2vBdPTyvvAXs9_Nsc1HZuRk3Wu6zSrUfFGvsqKtcAMsJs4ptv7XJGJctRvo7rbHKqvK887o9PkYNMSzuLjqYaTyI8wdMtYZHQ6WTXZltY3wAX-lYiRJioxzyLoYU0uvQr-vheJ22XYzXJ6_4KbRhuQ9FigzmcZVooDKDitUjZ213rlcIwkDnzCzBwIIFg6lzXZiy0A6bKMGxlQVBpMzmh-Foqj79ZLICjvh-e2dh5ahg37_b-qLHYGry-iSd-OIJY7aKdbT1mnbx_fQOS8savi58tdShs73pJNCMSm4ov6olr2ZXjTqzEalRQaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gql4L2FKk0XYN5Hz7eTzwhGVp9RybDkzpa4z3nyXsxW8vUvascP2pCbyydzaL5AqJ6e_wKSjUID-8dwaezsms57eAagu5UgD6yEdKwgwt09BW9LuOuhucp0Kk5Y8tXRou02bpib3EdT6pKvRKLFFz-lMhDUY9m3XTjy9dkVbRWOC5iOXFWluSS3GF4okqtVzgiRlfLCNFdTnJNzp26Yj4MrIHXj5zzPyrg3l4v9iEAQVATz9CPHOP_dxLXVMu_vyA4VMQ2NLWiqVUwfAPVbdpl6SwOFZA4oIPDs3q_YEDcF6ZcCuhYBFSABpkRgjusmSlwXDKKO7jrrjPkixNTBXsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjsePK_eM66Q3sOPvxlrvN-1s5_7G7TPlxYh3PCJdBtbWSLwKGryOYgedeEq8THVVtY1kcKAYpKqISuKjQmau_KkYpHFPVEHGae9xmimPBFsXxQjovuK7OwN8LAzvBuEF4b30tdv9u8XhedK6tzCYib6636AQqZR5wwXjImXIU5rZMyJH0gNvdcQqYr1kzK99f9sivbf-N-YGn9qg-hTB1LXkqM7v0nzyz_5ZEdvo10TUIrPBMEDGaVyfm2Dx040y9L7G72eQHOyy1SQlkuwXoXvsafR6F2JnJ-1ETinLf5TN2Ic1tWx01wdVvyGjuB2VO4-ILr-_PF6oNTQZMLcdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QMQl37-IXskzeE67OAnjm-zrX1RiFdxrAlKHjkkhj5-TLpudrzVx-xbjSmOifU4gj15hYa3K-d_8x-lPFO8fbHHnC5bfKgeP_koldTU1qONwk_KLt39KUt-vhDHp-LaPn7ExB-LsCl779pWJA2iKcliHltOm35uL6kbdSEwyIhPVXyZxcVNMh7IeS-7-q8RaCboPOIUvB_TmUmM1PFBjQOa6oHo4Yd5jGlSTTNjDw1TDfvFcjG3kDYuA5m02VjM89xh2Jb0pDtZ2tooEXDx24-D70kS8bnpePFCAFAOseUp4TqVV6v5SGXVbIYpnc6RIN_WezW5tmzE1ypO0gJNLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvfgivMXSj8yXYPa2dEJBkCZQmu7Z5yFe9clLD_GJVhvCKtnkTZQCE_c0dWXPJisnSWYm73xKJLalKAOrk1H8JpgEXkWTlbZebFf4waRvC6A1OgAB_0eQaGYJh09sBjRjpKKUIUFMZtdp4oBbFdZlH6R76s0UDfmAlgZVTLE3qzn1DxsxnSup19j-Bt48jiF8Y5lbmCUYiyWymdfN-jyir6CnzgumBOYe3ma2e2xaAHRdgoxCCWTZ0aWfkhIk5kImg9RsRW_ZGEyZGWrCoJjZsE9cpyCODB-bhgAgJHpkZ2ZAhfEI3ZEl1I7hjXUCUmMbotKNPXs-mOYqADd5bTi9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ea5fjXiJ3bgVO4oU4tqBk1MdGNtgYW-LoWRAImW32rMArMSta7OdB1KEsScLKsr7GddQ1chxCaD7xyH3c5wpRbG_12J63j841yBf6B1iWW5Qi89Rac2sV3MqhBxnwJNLw-ZjW1v3cN1Fp7LPbF3F-ZXbRNcIVzky8fCK-8ibRcn7cAyERdgc0WuKsjNIb-CGNNG19OQvlIOzxL8YL5is0ldxc_OBGYqQe1Uv2K6Jx1z4z9ABQcXSg8uqM3TTF3GqFpPLPdccknn0jsJs303rLwYgR2jsE5onxldsEvM-8B4eGjZcOsk0Y9-7WpgaJ6ONuZc5RIcQaypjLumRxefocA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJaUPF5NQ_pM4h8UM31jyIdcRtJMs0X8r3M2biLNsAZComYVd7zkxKVSQN0fvpUCEKHGJAQXBf9npCDrgcrHH_CBmd_KKnVlSlt0E8rsY-1pt4wyulOwPlGcmFlLnHnT5fKGQjKWcjIhjGsmbIQaOOf1rS9uJ05DG_nE22motFa8j8WvExt3Cs9d37qPjtD0vZcFhO4BxGorRwG9nIyk6reCauGO6EaLQPblrgFfU1ZmTe6NgL6dqNfmt3UPHVzOWxjPyAvE7EyU_nmaiY7Mfb8rOw75DDwsRHmwY9WYIgki9vU5bjpPNyXP0-USHD05WFROUFTusRiBjw6s3c60mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eo7YwewcV5Ynte8p7H9ug8xDaRyYorIvBvmhg-3MoI_G75qQpwHFHuZhQvmf_NQIr5Lkc63vMB90i_2cwtInWBGuxJywibd73sf1v1LzjjXgouQ2wRBp25sH5t6s6GSe-IvOXVb8mD4rYObXpG2hY0ABeC-7dd8Gl_QBARQMxfyqSdeM5YJPkERWpBKjxIJuFG5IwS8SlyNF9M9glZWHJ3JEx3QxzYWeREZ3G2cV0Fapnc8IIPWG_i4pJiXGk1KMBmCSzAr4j5ZAk7VgsMT96MC7z23Jum_bw5ISv-NkLWzvzJjxpwqCMfxo-pyUNQQrAEut6KnrbN75KEDfqy6aXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حال و هوای حرم حضرت ابوالفضل(ع) در شب چهارم ماه محرم الحرام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/660928" target="_blank">📅 22:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660927">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mT6CYvmOK2VStGI9Uswn5AWMMf7UxrpSzcNYPwFzX8-eXaviqQ-TUVK2sgG5byKotOBJEjYutpJ4fiKjqLO9YePFSK_VVhL2qAIUhtU-mI4qsroz3BruCjt-5VJuA8I1nMZ-11er7PJpCzYBX80-Hiw5USG2ek0edwmqBylBc-pzRKDS_flMoIbpYZTsk5iUuzUWrMNs5F7WNZn1-cJGSyYdlKnftOFajY7sT1zETN1W-HhKSxuwkpqWfVkwqExyBvALnWdMhi3PN1Vqczyaj4sXZT7nbfA53URA3hF8ZeZsOWowvd-jdh91-p04NGwmm-Ky62nEyaH2fsXFYgcUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فقط 3 روز تا پایان
هدیه 30,000,000 ریالی دیجی‌پی
ویژه خرید حضوری
مشاهده کدها
👇
و آدرس شعب
manteofficial.com/b
همراه با
🔥
تا %70 تخفیف
➕
%20 "بیـشتر"</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/660927" target="_blank">📅 22:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660926">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYtq7-7TFjbLdoRcApF1EiPsOStv6NSdrUlDcIS_WuEgJnoBKGnBCQusLbUMXL1qFUkDBbQNIcDDIcb5m5wRPEUtX2EBoLsxDrBeIeNCTID54YxvyLj5Q87WWuVAbNLEbc8SsTvzzpv-kfVeSNZ-BnUzTmQkflCZ1t-3ql12DNO57TXh3PH-U4Ldo-EwQzXNGrbUP92Qj8txJV0zg_d9xh0HBiEOzv8r0EBxk6mt9D3IusxHSzv70kAFEekzxn7PHBW4FEbUUiFRMqRxEz3Od-eZJhTa5rinNHLQuOcHXR1isLA-MamyCcodTxB3_TRJc_UE10GjZVfMoSO4c5wWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش جالب کارتونیست یمنی به تفاوت اوباما و ترامپ در مذاکره با ایران
🔹
کمال شرف
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/660926" target="_blank">📅 21:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660925">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F06lolYSaSyTm00X0gmnEzl2zNuAwcjpGcxvSijhWYbuyBSXhd-l2Ur1jShrNNAzGOoOlQfhb48yrqVzCZlzLJt9DGPKIi1Y_F6GjNoQe1n0pxaYelwzPKqxURUZsUfmQQaOSc3NW7UWVVPaMiN4wluKdqrEyUs2rozz8DPy1_tx31WBx_8MPHRcP9_Nk6NmOjXrHXX86MWowUcLsjkLGw_Q_S-jZc1D0wVRZmM1HHJU1b2gWL5gRrLDelQKZrhiT8Br7gaVY5rToY8N5M0pzqF-rtYSAAQBZOqhuBZ7JxM8MCZ9aoRbreafTb6vCHDxOm1QR6acWB0FprUPNivu4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
۳ قرار تا کربلا
✨
بعضی خریدها فقط یک خرید نیستند...
گاهی یک قدم‌اند در مسیر عشق، زیارت و خیر.
از امروز با هر ۳ میلیون تومان خرید از فروشگاه «قرار»،
یک شانس برای شرکت در قرعه‌کشی ۳ کمک‌هزینه سفر اربعین دریافت می‌کنید.
🕊
🎁
هر ۳ میلیون تومان خرید = ۱ شانس قرعه‌کشی
🤝
و نکته‌ای که «قرار» را متفاوت می‌کند:
بیش از نیمی از سود هر خرید، صرف امور خیر و نیکوکارانه می‌شود.
✈️
جایزه این کمپین:
۳ کمک‌هزینه سفر اربعین برای ۳ برنده خوش‌شانس
📅
زمان قرعه‌کشی:
شنبه ۶ تیر ۱۴۰۵
شاید این «قرار»،
آغاز مسیر شما تا کربلا باشد...
🌐
ghararshop.com
📲
@ghararshop
📦
ثبت سفارش:
📲
@gharar_order</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/660925" target="_blank">📅 21:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660924">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
اتحادیه اروپا از احتمال لغو تحریم‌های هسته‌ای ایران خبر داد
مسئول سیاست خارجی اتحادیه اروپا:
🔹
ما تحریم‌های مختلفی علیه ایران داریم؛ اگر توافق هسته‌ای وجود داشته باشد، فکر می‌کنم کشورهای عضو اتحادیه اروپا در مورد این لغو تحریم‌ها بحث خواهند کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/660924" target="_blank">📅 21:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660923">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwsiM5jVBMYO-dpZs1F2VxtgJpU_fdZzDmclOasjd4kowgFfkDeQ4Q2fBfCq4PJrZVnTBs_m2Xvq0Su8vgF4hUwPl107V9AX6OFhAkNIyL2XwtD8_omea0yTc_HxPfFhL-OjuokbZH9TaAvAFZHBDjSY---w2LQioMDVSewNWDJcaaIAoJ05RN9qRf5e2tYAIwoZqf0ujIHTOCvwnpeSeEjqkuhpF2zHn5KLnSrzRN4s0gp3HTv5ci-YsyRbpCCUSeIHK7LrqeIJSrfc5oEdPArwGMWwtmUkpBwCzwsRBpScio9V2iQ-djeFSBczeZ0XKrrwZci2rROapmhCB5bLjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✉️
متن کامل رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
✏️
بسم‌ الله‌ الرّحمن ‌الرّحیم
🔸
ملّت پرشور و باوفای ایران
💬
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/660923" target="_blank">📅 21:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660922">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYlCWrD8fnFCkOJ6d6niOnSsesJjhsvjvKEvBWRJP-WS7X1qyWi4VPst4DkPi5-c8KkllP1GIlJTEmbYGg_IQ2Xig7YKP1IrNgHtNlQHufdZxm1graiBBecNDnCw2dQu5NuhazaeHB7NnJsW8y3ojqIwRUJcMf1jLqMyoa3MWjvHYGnj_94nNSMAs5uMnehYVFOaJqrMS4R43CzKLsDj6wc2rntXz1HmIzolDoFr7jgqa3uCOcW67EjzoJ0okDaeTQdqGgVihab-k2_4ecA_HDXBX363r6NzHwFohRE9hnEr70Grlhh2OawfOKFxfaUXrO7qdRTbvHuq1CUIzuUVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ قمارباز: انتظار داریم آتش‌بس کامل در همه جبهه‌ها از جمله لبنان، حزب‌الله و اسرائیل برقرار شود
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/660922" target="_blank">📅 21:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660920">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ارسال تفاهم‌نامه توقف خصومت‌ها با ایران به کنگره آمریکا
پولیتیکو:
🔹
کاخ سفید یادداشت تفاهم مربوط به توقف خصومت‌ها با ایران را به کنگره ارسال کرده است؛ این سند ۱۴ ماده‌ای چارچوب توافقی برای پایان موقت کارزار نظامی چهارماهه میان دو کشور است که ترامپ آن را در فرانسه امضا کرده است.
🔹
انتشار مفاد آن با انتقاد برخی سناتورهای جمهوری‌خواه و نمایندگان کنگره همراه شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/660920" target="_blank">📅 21:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660919">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ادعای فایننشال‌تایمز: طبق توافق آمریکا و ایران، ایران به تدریج به ۶ میلیارد دلار از دارایی‌های مسدود شده خود در قطر دسترسی پیدا خواهد کرد
🔹
این پول فقط می‌تواند برای خرید کالاهای بشردوستانه و سایر کالاهای آمریکایی غیرتحریمی استفاده شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/660919" target="_blank">📅 21:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660918">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✉️
متن کامل رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
✏️
بسم‌ الله‌ الرّحمن ‌الرّحیم
🔸
ملّت پرشور و باوفای ایران
💬
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/660918" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660917">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/660917" target="_blank">📅 21:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660915">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jL0COiMZyQzaOLe6bH-f4XSe0NdjCLTnFVXLc2B6f9AWdDu8n9MZVtBQdd0nKctbG3yAY66CRFBKl6RfoKFrFXoiO0rxT6mWwci06Xv4OzEc8KP99sSqmmT05B6U1PZ75KMHJQzm4dmYTdMVmTh0X03U9t2TGXZb-ztdTbc_2qceBhl40k918-JupB7fqcyn5g_z4IsGbpQ8IRCIioLVnIOtBFuLkeOnfL3JSfeeXA-6W_7eO24w8ycXSrG-GMp9-xQ_HZlqVUxVsQbsN38NK6aWiyF4eM7Ju3dSdCMUpODor9leu2rLW5zWuXs4YpnUilqsOJAFJyvZcSEYMGV0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✉️
متن کامل رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
✏️
بسم‌ الله‌ الرّحمن ‌الرّحیم
🔸
ملّت پرشور و باوفای ایران
💬
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این مرحله، مسئولین امر، از سر دلسوزی و با حُسن نظر، تلاش‌های زیادی را به‌عمل آوردند و البته این رئیس‌جمهور آمریکا بود که از روی استیصال، از انواع اهرم‌ها برای این امر استفاده می‌کرد.
💬
بنده علی‌الاصول، نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت حقوق ملّت ایران و جبهه مقاومت به بنده دادند و تصریح به قبول مسئولیت آن نمودند، اجازه‌ی آن را صادر نمودم‌. ایشان همچنین تصریح کرده‌اند که اگر طرف آمریکایی بخواهد زیاده‌خواهی کند زیر بار آن نخواهند رفت. از این لحظه، ما یعنی شما ملت سرافراز و این خادم ناچیز، منتظر تحقّق شروط گفته‌شده خواهیم بود. امّا بدیهی است مذاکرات حضوری که در آینده برقرار خواهد شد، به معنی پذیرش نظر دشمن نخواهد بود. امیدواریم که دعای خیر سرورمان عجّل‌الله‌تعالی‌فرجه‌الشّریف انواع نصرت‌ها و فتوحات، برای ملّت باشرف ایران به ارمغان آورد.
🔻
والسّلام علیکم و رحمة الله و برکاته
✍
سید مجتبی حسینی خامنه‌ای
🗓
۲۸/خرداد/۱۴۰۵
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/660915" target="_blank">📅 21:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660914">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ر
هبر انقلاب: ملت پرشور و باوفای ایران
همانگونه که مطلع شدید، تفاهم‌نامه‌ای بین روسای جمهور ایران و امریکا امضا شد. در مسیر رسیدن به این مرحله، مسئولین از سر دلسوزی و حسن نظر، تلاشهای زیادی کردند و البته این رئیس‌جمهور امریکا بود که از روی استیصال، از انواع اهرم‌ها برای این امر استفاده می‌کرد
.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/660914" target="_blank">📅 21:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660912">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfpPHDUEGyQH2Ao_1z7fUuPNVJX4eSzGBRH_rjBhfBF8m7vFelIw1OSTfgCVNBBlNMAWBCxe1qMNgB_iIo6grsxe_ERFMdR7QzoaHq6W0R5GW_vFcRLRDEUN_xIl-GQqgi7hFaRzPZUYp0SncHDnZFEMAxH6ekBOzavstQjeIFLvqpEnQp-0dB8AuFRHIS0HEYgJMvei6dIZTFVuQCjG4Wl5cbz1O9sHK4PUVIIgWx7rlvsKK9yj6Pnq6GrTHcQagozn5VozQUOoOkDwaQjC3Rcdm_k70wftQJn45cwoW0KZ0fZExYTX09warXh9Bx0bf39tEIGxJguBQV1cQt4OQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مِثْلِي لا يُبَايِعُ مِثْلَهُ
رهبر شهید انقلاب:
🔹
اولین و بزرگترین درس محرّم این است که نشان داد که کسى در حدّ عظمتِ شخصیّتِ حسین‌‌بن‌‌على، فرزندانش را، زنان و دختران و ناموس الهى و حرم پیغمبر را، همه را برداشت آورد به قربانگاه.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/660912" target="_blank">📅 20:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660911">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f6989de6.mp4?token=vC_9Ybb4kq8VEgiDq8MO2c-hjMznB2v5dnnxUYoCfIYjMr0naW-eRJ-yFFqk5_DyDR8jY-Zd9umOJeoynBS-QJAHNLMQVkD9VcSDBOwamEuutRpUZIuA7D0RtW8-tqoG5xOlrmLUfqznBMVQCh9pQ6tinP5opCMeebPalWmYSlyFvhXf6bxVmLDvGjHbURDcmphH7ytl-jqqEjt931RQ9_fgHhKXzt6QTRbr9iBwjTPFu6D-NRv0K0Kc0qSae2c2unoBadD6b5i2ns8By-KioASgXG1Bfm1N18mQUQDjq4acJonagXfw3CfDwGCsPcUmDxmKVktlKGU4xXhlbwNF4W0Zk48k8ksSjJSXJe4YnLvtk7NfA9gUPNBsaxTXhkW0E-cpPiRuaJLiadFEmjvo8enCvSP-ODCxMeziO53s_3jn8Iw8nT0zB0R51W_55HRtfvLHz1dpTY-2w_EdTBjMAUfg-xeniHm9HaaTmWAqeo6Djjt-IRxeWG4puUR0z9f3Z5SPbQ5TkawfIHNh5uIDI5shP9RBvIpjGR0-8expx5kS_-Ett3YR0dUlCRsTcRT06kspOCjqlh6goL1yat3Lz60MuRMBGGYZ686yPcnU02AK9Vw-Zu5-QFKhHCTWVVeLvx0n44dL6CA_9OQ061pFNkx2hGWOwPyrXnKenPekF54" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f6989de6.mp4?token=vC_9Ybb4kq8VEgiDq8MO2c-hjMznB2v5dnnxUYoCfIYjMr0naW-eRJ-yFFqk5_DyDR8jY-Zd9umOJeoynBS-QJAHNLMQVkD9VcSDBOwamEuutRpUZIuA7D0RtW8-tqoG5xOlrmLUfqznBMVQCh9pQ6tinP5opCMeebPalWmYSlyFvhXf6bxVmLDvGjHbURDcmphH7ytl-jqqEjt931RQ9_fgHhKXzt6QTRbr9iBwjTPFu6D-NRv0K0Kc0qSae2c2unoBadD6b5i2ns8By-KioASgXG1Bfm1N18mQUQDjq4acJonagXfw3CfDwGCsPcUmDxmKVktlKGU4xXhlbwNF4W0Zk48k8ksSjJSXJe4YnLvtk7NfA9gUPNBsaxTXhkW0E-cpPiRuaJLiadFEmjvo8enCvSP-ODCxMeziO53s_3jn8Iw8nT0zB0R51W_55HRtfvLHz1dpTY-2w_EdTBjMAUfg-xeniHm9HaaTmWAqeo6Djjt-IRxeWG4puUR0z9f3Z5SPbQ5TkawfIHNh5uIDI5shP9RBvIpjGR0-8expx5kS_-Ett3YR0dUlCRsTcRT06kspOCjqlh6goL1yat3Lz60MuRMBGGYZ686yPcnU02AK9Vw-Zu5-QFKhHCTWVVeLvx0n44dL6CA_9OQ061pFNkx2hGWOwPyrXnKenPekF54" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیگانگان واقعی‌اند؟ پاسخ مبهم ونس درباره یوفوها
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/660911" target="_blank">📅 20:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660910">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله به ایران آماده شوند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/660910" target="_blank">📅 20:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660909">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
از کمای عمیق تا ارتباط با ارواح؛ تصادف هولناکی که مسیر زندگی دختر را تغییر داد
🔹
00:09:20 قطع امید کردن جامعه پزشکی از زنده ماندنم
🔹
00:26:30 عدم رعایت حجاب قبل از تجربه
🔹
00:34:00 رؤیت حضرت زینب در کما و پیام ایشان برای مادرم
🔹
00:40:00 مرد زیبارو با میوه‌های بهشتی
🔹
00:44:35 ارتباط عجیب و باور نکردنی با ارواح بعد از کما
🔹
00:49:00 روح دختر ژولیده و پریشان که درخواست کمک داشت
🔹
00:57:30 مادرم با توسل به امام حسین (ع)، از خداوند خواست که دیگر ارواح را نبینم
🔹
01:02:30 تبدیل خودخواهی به مهربانی بعد از تجربه
🔹
قسمت هفدهم (خودسوزی)، فصل چهارم
🔹
#تجربه‌گر
: راحله خمسه
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/660909" target="_blank">📅 20:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660908">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9OrR2XUS-unbwVOwpsPkZdpoy7jw6B2Cn_56rJrzpzGr0A1K5e8nzuQaQR6eNhNN3WvgH1nowBX_OWs0GU-djtGdqEiX71n7l3DlAQ-41ibeTS9C1DIeox3aNN4qau7HN7LDCwjpmK2hj8w6jB7wPI9qaKQKQqiL-iZLRy7VKqaBgH_UO7efaHwGHjO2T-kR8EkqmN3mHDMw3bJbtx2bsPPxGy9gnH5ZDR6O2IN9Hx-4ViolfGriZetVMeS9Fb6uOWF9C2d-e_RJh0NZfXVuZmDrSeuIZL77cxQDGim32Gvr8c4i1V_a80gtptlEXxtV5giZZsM_Ec27pM-DJoRaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنت‌کام از لغو محاصره دریایی ایران خبر داد
فرماندهی مرکزی آمریکا:
🔹
نیروهای آمریکایی طبق دستور رئیس‌جمهور، محاصره دریایی ترددهای ورودی و خروجی از بنادر و مناطق ساحلی ایران را لغو کرده‌اند و دیگر مانع تردد کشتی‌ها در خلیج فارس و دریای عمان نمی‌شوند.
🔹
در این بیانیه همچنین آمده ناوهای جنگی آمریکا در منطقه باقی می‌مانند تا اجرای توافق را نظارت کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/660908" target="_blank">📅 20:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660907">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO8ivenEgp01DtxSXcNVBvmapZW1dHtFdWYUZAb0ptjHVnYiBH-VvxYTnGUAZ2F-QgYgbOCP-1xnpr-iIhK2p74TEmJvwfjuL75LrOmc8-Ur-Ye1bDkOm0wx_J7LhJFmd2Hwlt3EoTnS51fWb__df11LQ7sUjMuoJw7a-U6e5W2B7-dZ05xnMpRf7Goiimf1nubsN26ZJJDTmMwk2M2Jj80xYQfv2t5829p6QMbdx3BnNnKOKSrdnEB1Q1JHo5uX9jt6YNJ3FARquazIesFVKXMD_6c5ysWn3XJhW1uF6LqCBbbGak76OfxaKaceOZqbNEvRzZKaSdAUa5BMUNTpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شمارش معکوس برای حکم نهایی
🔹
بررسی‌های فضای بانکی کشور نشان می‌دهد که عملکرد آقای قربان اسکندری در دوره سرپرستی بانک صادرات ایران مورد توجه نهادهای بالادستی قرار گرفته است. کارشناسان، مدیریت ماه‌های اخیر بانک صادرات را یکی از عوامل تقویت جایگاه ایشان برای تصدی مسئولیت دائمی این بانک ارزیابی می‌کنند.
🔹
بر همین اساس، پیش‌بینی می‌شود معرفی آقای قربان اسکندری به‌عنوان مدیرعامل بانک صادرات ایران قطعی شده و در صورت نهایی‌شدن تصمیم مراجع ذی‌صلاح، حکم مدیرعاملی ایشان در آینده نزدیک صادر و ابلاغ شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/660907" target="_blank">📅 20:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660906">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY9D1jS1jGuygrmW5zWEkkkVE--sF3dtWJ1GzzPoeVaeYN3BvhDbzb2qlmbelJjk_9ax3vj-pBoguuV40IATSP4wFpsqY6xvhZfvfSBo701sBroXzOW3MNwye5a5MdrIz7--_LLcjb-T3v1u1sa3q2UiBgbMXodLwd6UAyYWoK4aLF7Yos8QbDOdnMFFd9ImNzllYgrIaRDPqYrsFcJeM7RmjxBue9LKf0WIFiV0oZWZhviqu0YzxIiWCvVFV8YMuRKCDW_HkAvbgy_l9T2HL0j5dYvIWwJiHh6XysOVX_V7FLZJofPNbhEJ_o2nnVUgbL38uHJOosrz2lTNY7u73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ قمارباز: هیچ پرداخت ۳۰۰ میلیارد دلاری از سوی آمریکا به ایران وجود ندارد و این خبر دروغ است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/660906" target="_blank">📅 20:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660904">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNhF4cnrilNEfnlgcat9jM36T0dvtakaLkfdd4a0qxHC7Ia_E_-em68RtvcgmgepDQenISOPonlrdzy4iHsgOGHU8i8pC8zUIaI836ocyeiXabC5DUjhoqIm_nWEt8f8PuhWibq_GZXACXa9n9qGeUSjbnLpPYd-lP7OfVzqX_QQJlExEec49FxDWK9pLtu_HxH70NAYGZ5IpLUosy1uBPfxSo34He7ewKtd5Ffua9-q0Q3hCfKmmMODR-EM6ujaZCxROxsEwyYR_1WmuhluN3LCfZea7KF5CGNQvyqzzEJqX_FYBzhV_NTILtGCLCTXAZSkZQyoYxLOCkCb2KPFVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبیعت زیبای ترکمن صحرا، گلستان
🇮🇷
#ایران_زیبا
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/660904" target="_blank">📅 20:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660903">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2tJHrKiBBm6qsQURfHSYcM8L5hT-rAMogovOIsvMIp5fkfIFvZAgZanh3ymDqJeAKF7NqnbhE8zqkuCrUI93DQmRDwOujlFgx8BCw2QTw_YsynymdmyexUDMJ0uJNC4cz-otpl2S_uNjE2EnhzydcfTC1jl8p5RtO-633UtYUc1rz4hgpA-z8N5XOBUB2S_4lwIOVTqmqfz9AReU-Q9TMe_G3CN874koPwbroWYD_FYq2I_DNHf12oXkJFliXJAaEjnD5dmntql6cgdMkY3u2b-Du6tMt1mYoQQGgjCf0xw1FPx3uGivQErPE2yC6lbzCb6E4XlSffzDeIAARVOUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/660903" target="_blank">📅 20:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660902">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYmaug7pPYXfB3SyEEvG7wc1LmXWDHULNxwBqigw-voJKc7tbqpJPgnojb4qTWYg4HaGqFp41n6H6GLaGjVCGE1A0pTBL3MdNPcwEQpoYcbpPFUUXN0JWB8bjtfdWUafEr_UFI84uudYNlbIbbar4UNQODUDfAa1NWiGiG9SG9gG8LNqJj_q4EwR5tCarlMVrcsJnhDxJdQlTEd0tCpMUTyhrNr2-PF3EI6oWiS56fB8p4ga-Vit0OT-ctkJURjcvYshWkpbjo-oB1WiQXKNylDIACCnktdOWjyhrNWxSi0QeqSpAzUjUYyZw7y3qUNMvAM5Drqcmg-FHz-tIVBjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه جدیدی از دارایی‌های بلوکه شده ایران در دنیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/660902" target="_blank">📅 20:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660901">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
نرخ دیه سال ۱۴۰۵ اعلام شد
🔹
بر اساس این بخشنامه که در اجرای ماده ۵۴۹ قانون مجازات اسلامی مصوب سال ۱۳۹۲ و پس از انجام بررسی‌های لازم صادر شده است، مبلغ دیه کامل از ابتدای سال ۱۴۰۵ در ماه‌های غیرحرام، ۲۱ میلیارد ریال تعیین شده است.
🔹
این بخشنامه از سوی رئیس قوه قضائیه به مراجع قضایی سراسر کشور ابلاغ شده و از ابتدای سال ۱۴۰۵ ملاک محاسبه دیه خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/660901" target="_blank">📅 20:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660900">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
تا ساعتی دیگر، پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای، رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رؤسای جمهوری ایران و امریکا منتشر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/660900" target="_blank">📅 19:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660898">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd31f766ad.mp4?token=pY5gCaBzMLEZ71Y2LAgfS5VuqX7s2MqaxLZWcZ5p2f1Q-lCWLKkyj8uJI311AUF1_Z5nQytG9EICTc4FWqmgRc9JDH-3T_ZbQsnnlMlJxQNvYmUvUCMn7R8tJ9GVXqXZmWU1dFDhAJKoPcGp8AsFcjYATiRxFIK3l7BmMu6mFXeef8Aezmx_AeuTFvqiimgRyT3IP20GCZeu38zsf3X5yejKWM6vp3LnqM4bjFh_6p2CHJ_5Iatc1FGfl2PtFJXEEuy9XCrqZ-IarkmyapfVDkum5RLj-0T2aEboTVQU2mPXKWrj1G2ezrZ4ydrRUz4hjxAc-DK1f46GA8S6UpR4dp59Tu1BTuVU2slyqgUqVsF6FwI-MLHOwXJubu2f2SeDG6APcoN-uVBxL_RLLBTId0hh26S2xn7aKf4o9TESz5efhO3Ru9ORSBYsnaqmBelZD7XHUBULb2bFzuPp6YWjSG7qdDTVZyYy3A7AwSES9pZwHj3KXwSHXaRTtmJDsY8tK4E84Tdq6lq9jzflrC7N0uKKYl4wr5NxHklf6WyvY3xbME9Eqa7ixSEwr6bRlV5EPYAxN677lubix5DlkiV8ypvdvDabycCRKyRPobAMkcWsqURch7WHP1Ae5OjMGrWfdgkCNenipDWW7_WdYySJ8oz2auUIHrIjZWOEqfjsnfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd31f766ad.mp4?token=pY5gCaBzMLEZ71Y2LAgfS5VuqX7s2MqaxLZWcZ5p2f1Q-lCWLKkyj8uJI311AUF1_Z5nQytG9EICTc4FWqmgRc9JDH-3T_ZbQsnnlMlJxQNvYmUvUCMn7R8tJ9GVXqXZmWU1dFDhAJKoPcGp8AsFcjYATiRxFIK3l7BmMu6mFXeef8Aezmx_AeuTFvqiimgRyT3IP20GCZeu38zsf3X5yejKWM6vp3LnqM4bjFh_6p2CHJ_5Iatc1FGfl2PtFJXEEuy9XCrqZ-IarkmyapfVDkum5RLj-0T2aEboTVQU2mPXKWrj1G2ezrZ4ydrRUz4hjxAc-DK1f46GA8S6UpR4dp59Tu1BTuVU2slyqgUqVsF6FwI-MLHOwXJubu2f2SeDG6APcoN-uVBxL_RLLBTId0hh26S2xn7aKf4o9TESz5efhO3Ru9ORSBYsnaqmBelZD7XHUBULb2bFzuPp6YWjSG7qdDTVZyYy3A7AwSES9pZwHj3KXwSHXaRTtmJDsY8tK4E84Tdq6lq9jzflrC7N0uKKYl4wr5NxHklf6WyvY3xbME9Eqa7ixSEwr6bRlV5EPYAxN677lubix5DlkiV8ypvdvDabycCRKyRPobAMkcWsqURch7WHP1Ae5OjMGrWfdgkCNenipDWW7_WdYySJ8oz2auUIHrIjZWOEqfjsnfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونس: دو سوم سلاح‌های دفاعی اسرائیل ساخت آمریکا است
معاون رئیس‌جمهور آمریکا:
🔹
طی سه ماه گذشته دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند در آمریکا ساخته شده و هزینه آن از مالیات مردم آمریکا پرداخت شده است.
🔹
مشکل اسرائیل دونالد ترامپ نیست و کسانی که چنین تصوری دارند باید واقعیت موقعیت کشورشان را درک کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/660898" target="_blank">📅 19:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660897">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
جی‌دی ونس از استقرار تیم مذاکره‌کننده آمریکایی در سوئیس خبر داد
جی‌دی ونس معاون رئیس تروریست آمریکا:
🔹
واشنگتن یک تیم میدانی در سوئیس مستقر می‌کند تا مسئولیت هدایت مستقیم گفتگوهای فنی و هسته‌ای با ایران را بر عهده بگیرند.
🔹
او همچنین احتمال سفر خود به این کشور برای شرکت در مذاکرات را مطرح کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/660897" target="_blank">📅 19:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660895">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
خبرنگار: چه کسی آن صندوق ۳۰۰ میلیارد دلاری برای ایران را تأمین مالی می‌کند؟
🔹
جی‌دی ونس: تمایل زیادی در جهان عرب، و همچنین خارج از جهان عرب، وجود دارد که در صورت رفتار درست ایران، واقعاً درگیر سرمایه‌گذاری در ایران شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/660895" target="_blank">📅 19:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660892">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmxULJR45iP1qbMGo4g0_OtRhQuQgKlfjqeLyMDOdN5x1jlXZp8GiuQQUovxcd-krXG_rLe2Kw1HDORKdgQga6RsSzWYFOqrXiQzcaS9hh7x_VVyr-fFG4z1sFVZRpRsv4EG80fs7aKZEWOqqx7DwECVSegytpKRTGtj4H55PNiPKS6JwU1f6EkvMvm0kHuKaqTTTG3Md4YsTfznhRAkpocA0tQQa_vVjdK0ozfqCH651ztoswAL9SXywIi1l7wyasopbT9psiLl_Ubm6vwjUbgv5OAqtw7cpkpow4rHsnYMgE1kn-htLKg_V-HfSCgg4442jiJMBFuafxslrC3eDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKtZMaDOhGWbGjK-NnPmdA1sKcvfRaal0wF2mUplhw2cwhfI5Zyy6FzwesohMywoX4Aro4SFubUhKLH9rHGsxzOBLPna-JXcRpna5SWfQT6cNQPYLsSxL_GbIzSATAVVZk0-TmyvtAUmRuokKJ6byYeOWZKmE43_lpKPhIBpJaJhU1EYRzQ23rjPN0nbJ6HlTm1NpmcJwQab50UpFfSUOqpgbIZ9-Q65FmZd6hnLCfZulKVhBTHaSAMkii0SJtFgOL1y7OA1_w3jGUoHoL-ysE4miP6neoKnqdsU8hDEqf0VLG8qUmjOoU39ylDFoQ_ZtWObqib1CuUw8hsJkK0nrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر قرار باشد فقط یک کتاب درباره تربیت فرزند بخوانید، «نیک‌سرشت» را از دست ندهید
🔹
این کتاب به شما می‌آموزد به‌جای مقابله با احساسات کودک، آن‌ها را درک و مدیریت کنید. حقیقت این است که ما بزرگ‌ترها هم در طوفان‌های احساسی، بیش از هر چیز به همدلی، درک شدن و همراهی نیاز داریم. «نیک‌سرشت» راهنمایی کاربردی برای تربیت بهتر فرزندان و ساختن رابطه‌هایی عمیق‌تر و سالم‌تر است.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/660892" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660891">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
جی دی ونس در مورد برنامه هسته‌ای ایران: توافق هسته‌ای اوباما اجازه غنی‌سازی را داد - توافق ما این کار را نخواهد کرد
🔹
توافق اوباما اجازه انباشت مواد غنی‌شده در سطح تسلیحاتی را داد؛ توافق ما در واقع منجر به نابودی آن ذخایر مواد غنی‌شده می‌شود.
🔹
توافق اوباما…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/660891" target="_blank">📅 19:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660890">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCgWjgo5bZHtvH7y6KuVRYD7r5IYBYTlH3Q9Lms0OqaZEkvsVyr33cXRoJvl8E1_SO6XxWBzpVMACTewby8GBXUWS4ZgrjcgLl8UTbEOm3yqp-JyK0mrcrIm7IdWnIdM5CyfZJ8O_OKAWv_BDHGKy2RqhMgsc9Iflm51OyhTPP-pwMNjEX2wv31_0AFxmsr8Nf8AeVgAONDHUuyGIH8RhTL-75_6QqOx7JCn6IJtiz_ANBYKUDTA0z_gps4Cz-3FayCgb0bAzYYIdruJGplqtlSdFoMXOKfVZC25IoDYrtNGvFUgBqe_atdBsIM1rv1BhQR2wnTdJZVdknDWladzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای سقف انتقال وجه بانک‌ها
🔹
سقف خرید با کارت برای اشخاص حقیقی مبلغ ۴۰۰ میلیون تومان تعیین شده است.
🔹
سقف انتقال پول از طریق سامانه‌های پایا و ساتنا، هر کدام ۲۰۰ میلیون تومان است.
🔹
برداشت نقدی از دستگاه‌های خودپرداز همچنان روی رقم ۵۰۰ هزار تومان باقی مانده است.
@amarfact</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/660890" target="_blank">📅 19:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660889">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
جی دی ونس در مورد اسرائیل: به نظر می‌رسد که ما درست در آستانهٔ یک پیشرفت بزرگ در توافق بودیم، و بعد ناگهان یک انفجار بزرگ در یک منطقهٔ غیرنظامی در بیروت رخ می‌دهد، و تعداد زیادی از مردم که هیچ ارتباطی با حزب‌الله ندارند جان خود را از دست می‌دهند. این قابل…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/660889" target="_blank">📅 19:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660888">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ونس: مطمئن هستیم که می‌توانیم بدون کنگره تحریم‌ها را به طور موقت لغو کنیم  معاون رئیس دولت تروریستی آمریکا:
🔹
دولت آمریکا اختیار دارد تحریم‌های اعمال‌شده علیه ایران را به‌صورت موقت و بدون نیاز به کسب مجوز از کنگره معلق کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/660888" target="_blank">📅 19:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660887">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3093423e56.mp4?token=GITA8Mv8vZa5PKk2L3qAMbYvX_phsS66YJj8qiTS8DPwa21gdRdE8ny2dinhN4vXa_udJum7loCjGoqUbIk98BjLOpIXUsw2Py69yiHlt3jzhHFR0eG3LuSjjHdCs-ehOlZrDFNA_52HZFrB5DxLhXO2kduLdMb9lE8KCMZ2BDPcSB-83LE-7JmcbXGT2CpOBqtWWnQ4iqDr8kiOK_UaC1QMjpIu3dteaFQIhUGg4VhTlD-00RJuvopuwenAl9lfsPfwRQfmffx1NCDmG-YYzAe3Xatb4u8FW4asJ9M2f1WR9i5pk1MOzi5WwrkNs4HQaZWLLgNoh0afwLPolhrRfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3093423e56.mp4?token=GITA8Mv8vZa5PKk2L3qAMbYvX_phsS66YJj8qiTS8DPwa21gdRdE8ny2dinhN4vXa_udJum7loCjGoqUbIk98BjLOpIXUsw2Py69yiHlt3jzhHFR0eG3LuSjjHdCs-ehOlZrDFNA_52HZFrB5DxLhXO2kduLdMb9lE8KCMZ2BDPcSB-83LE-7JmcbXGT2CpOBqtWWnQ4iqDr8kiOK_UaC1QMjpIu3dteaFQIhUGg4VhTlD-00RJuvopuwenAl9lfsPfwRQfmffx1NCDmG-YYzAe3Xatb4u8FW4asJ9M2f1WR9i5pk1MOzi5WwrkNs4HQaZWLLgNoh0afwLPolhrRfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونس درباره برداشتن تحریم‌ها: ما صادقانه این موضوع را یک امتیاز بزرگ به ایرانی‌ها تلقی نکردیم، ایران هم آن را یک امتیاز به خودش نمی‌دید، چون چیزی که مانع فروش نفت آن‌ها می‌شد، تحریم‌ها نبود
🔹
آن‌ها بدون هیچ تخفیفی مقدار زیادی نفت می‌فروختند، چون تحریم‌ها…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/660887" target="_blank">📅 19:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660886">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
معاون ترامپ: نباید از تنگه‌ها برای فشار بر اقتصاد جهان استفاده شود  معاون ترامپ:
🔹
ما هرگز نمی‌خواهیم که چنین اتفاقی دوباره تکرار شود، درست است؟ موضوع اصلاً بحثِ عوارض گرفتن نیست.
🔹
موضوع این است که اطمینان حاصل کنیم تنگه‌ها دیگر هرگز به عنوان یک «نقطه فشار»…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/660886" target="_blank">📅 19:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660885">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">جی دی ونس: تمام چیزی که رئیس‌جمهور دیروز گفت این بود که، بدیهی است، کشورها حق دفاع از خود را واگذار نمی‌کنند
🔹
اسرائیل اگر حزب‌الله به سوی آن راکت یا پهپاد شلیک کند، حق دفاع از خود را از دست نمی‌دهد.
🔹
ایرانی‌ها نیز حق دفاع از خود در کشورشان را از دست نمی‌دهند؛…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/660885" target="_blank">📅 19:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660884">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac0ba5a10.mp4?token=XGS_wEm0_2vcXECSrRTmRLHQLFyTYbXwQg_IabcSy0ZU5TxttZAQiGxerCiWfsfS5dgRstdnPhjD9pgEiKNkylHQmiCh_hfaMUu6pXtxSDAT9ARasmxEXyUb9Z352X2wA7rJkx-o_mXpePwknyqpv4r7LxR0rVY1Wkl1DwzMjzGw437sNjtzhcuxZDKjUjxhMCxDCvtkhySp-YoatKILkeoR_SB5jpnCL5pWRQJYKML6fUAjOLjar8L1QQwAJG2g7eh88a9D8kkFFLhsYdh6RjKpqqkN8H6kbWOOONTgyY8saKlufuy9Uup5jC4fTnjuaX-P1yXf3iXeVcF_3OlEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac0ba5a10.mp4?token=XGS_wEm0_2vcXECSrRTmRLHQLFyTYbXwQg_IabcSy0ZU5TxttZAQiGxerCiWfsfS5dgRstdnPhjD9pgEiKNkylHQmiCh_hfaMUu6pXtxSDAT9ARasmxEXyUb9Z352X2wA7rJkx-o_mXpePwknyqpv4r7LxR0rVY1Wkl1DwzMjzGw437sNjtzhcuxZDKjUjxhMCxDCvtkhySp-YoatKILkeoR_SB5jpnCL5pWRQJYKML6fUAjOLjar8L1QQwAJG2g7eh88a9D8kkFFLhsYdh6RjKpqqkN8H6kbWOOONTgyY8saKlufuy9Uup5jC4fTnjuaX-P1yXf3iXeVcF_3OlEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون ترامپ: تحریم‌ها علیه ایران را لغو نخواهیم کرد
🔹
آنچه تاکنون اتفاق افتاده، صرف‌نظر از اقدامات ایرانی‌ها، یک پیروزی برای مردم آمریکا و رئیس‌جمهور ترامپ است.
🔹
ایران دیشب به هیچ کشتی شلیک نکرد، و تا زمانی که رفتار مورد نظر را از ایرانی‌ها نبینیم تحریم‌ها…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/660884" target="_blank">📅 19:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660883">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/236c140d81.mp4?token=iYGCcJCGw6Z1ApBM-UjtBBa9UHDZKFBh24tr2iLfzLbCLErgc8MQpcOk44msTPbKeTU379ySbnoffyboX1-4NUAO5W2TR774rQON3Oo23v8uAr9PapK-LzE5BhHzQGpEu_Kbdc9sxMT5Wovu0lYO_2iAHZkY7RCilJF7pcJAiafxA8JYqGaJ2m5Dj9JBDiQfB0R6AsvbSGgFOyN3Mp4aJRv41CTu8HeYDokHA3P6T0jXX4hOjC4Zhb3l6JLdAxsPsKJcU38hiSYFy3d6k1e9OYcaOYnEmLbf8TsSB4CZVR79qWl_0YjNJZ2vQFYI3QHnn-BrhQIsE7FCnTfgjP25Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/236c140d81.mp4?token=iYGCcJCGw6Z1ApBM-UjtBBa9UHDZKFBh24tr2iLfzLbCLErgc8MQpcOk44msTPbKeTU379ySbnoffyboX1-4NUAO5W2TR774rQON3Oo23v8uAr9PapK-LzE5BhHzQGpEu_Kbdc9sxMT5Wovu0lYO_2iAHZkY7RCilJF7pcJAiafxA8JYqGaJ2m5Dj9JBDiQfB0R6AsvbSGgFOyN3Mp4aJRv41CTu8HeYDokHA3P6T0jXX4hOjC4Zhb3l6JLdAxsPsKJcU38hiSYFy3d6k1e9OYcaOYnEmLbf8TsSB4CZVR79qWl_0YjNJZ2vQFYI3QHnn-BrhQIsE7FCnTfgjP25Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رویترز تأیید کرد که محاصره دریایی ایالات متحده بعد از ۱۰۰ روز لغو شده و کشتی‌ها بدون دردسر از تنگه هرمز عبور کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/660883" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660882">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای معاون ترامپ: شب گذشته ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرده است  ونس، معاون ترامپ:
🔹
شب گذشته ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرده که این میزان، بالاترین رقم ثبت‌شده از زمان آغاز جنگ علیه ایران بوده است.
🔹
نیروهای ما در خاورمیانه به بیش…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/660882" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660881">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای معاون ترامپ: شب گذشته ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرده است
ونس، معاون ترامپ:
🔹
شب گذشته ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرده که این میزان، بالاترین رقم ثبت‌شده از زمان آغاز جنگ علیه ایران بوده است.
🔹
نیروهای ما در خاورمیانه به بیش از ۱۲ کشتی اجازه دادند تا از محاصره دریایی عبور کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/660881" target="_blank">📅 19:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660880">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOheIVUOMskyJXtj5gMyoRp4rwZsog6VcHmTHkvXFHaSHcNIKedxET-xYQkp5TdYGXIkh9tdIrjEfHQAX6Xi6fCGA9r8XRYu6vhW6zYPRsGYlu-k7g3J7mnU_CsaLPUtTfQHwqEhdYofvUwfjY3ebavuwoudwEyJz3R9NkoKR63JTu0tFojH8czZN9DqQu9eH0v2XR9GiVKJSEsoUpyf5K_4SqhBs1pNjko6KHPHLaqZFJgjLQYUNPekxPG-n5pZPXkneFHMsSf5NBRbgqXOa93a0GqlrapETWotAcISR6tjhtymnJc_zd4z7ULBkG16mjfjtBM8NOYZdR7vA8qABg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/660880" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660879">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1lvrJxixUjnE-zw53nzQa3RUOpXZPxOZ4WURIMMHdK2A8Df63l5Ok9Kt7H5v0uOE6zDa13gWOsZhk71C3YHrf1xmTbupBXcg6f_838N8jYobn_GZuWzTwXsmmXrAhx7DdlsvZTlLhDulJGiLQ0v1iSg7x-r581isw15rXjV1dYqQGkr1NuhrfTiDZcJNX0Hb0EYJVp6SnEPCsmYOy7JMx0Z_bbFQ82lMAcCmcwOfcPehbj5p2hd_QswfLc3TK-y_Artxs-2YXxLAJv8oyvvzFeLI3yh-iXd9JsCdjF1YDqoVzVfBGiiEhrS6ZJicMjAWqBAzOswaZxnz1UsqC7ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش ترامپ به انتقادات گسترده در آمریکا به توافق او با ایران
🔹
این احمق‌هایی که فکر می‌کنند من به اندازه کافی در برابر ایران سخت‌گیر نبوده‌ام، در حالی که بازار سهام به تازگی به یک رکورد تاریخی دست یافته و قیمت نفت در حال «سقوط» است، یا حسود هستند، یا آدم‌های بدی هستند و یا نادان. دوباره آمریکا را با عظمت کنیم!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/660879" target="_blank">📅 18:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660878">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvQS_aBbzE_qmoJDlHfMH0jeSS3rrd4gmBFs_XyRHPqHINANLwTqmDKTRu4s1ZhIHWt8DwgD8KwpyKwI0d6yxWgTEx1yfIn0YWKyqMvU87ZoE_nLVuChheq17MpELn_WaFuK27xx0W0fgSHv7gYg3VdFLTryzEWEOgIpxhzcPF8wdylgfRsDtvkCCsONLRtyvaHy5FBZzmNBrzwU0U0f6pS6VYS67slE2KIvfHzcJ5-6Wjgi5jww7ggOAB9E4rtxcHWAxcP9E_0h66PX9ZzluHOHmMdsyZSHszuN5qClSWcB4PnA7_kWLtt17hjvM8Xph7UGSRROns3Q3J_bfp0x0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنی که مرگ فرزندش، سرنوشت میلیون‌ها کودک ایرانی را تغییر داد
🔹
وقتی بیشتر مردم حتی نامش را نشنیده‌اند، میلیون‌ها کودک ایرانی با میراث او بزرگ شده‌اند. توران میرهادی کسی که «غم بزرگ را به کاری بزرگ تبدیل کرد». او با وقف کردن عمرش در آموزش و فرهنگ کودکان…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/660878" target="_blank">📅 18:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660877">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
۵ میلیون بشکه نفت ایران به آب‌های آزاد رسید
شرکت تحلیل انرژی کپلر:
🔹
ما حداقل ۳ نفتکش با پرچم ایران را رصد کرده‌ایم که مجموعاً ۵ میلیون بشکه نفت خام را از محدوده محاصره دریایی آمریکا در خلیج عمان و دریای عرب عبور داده‌اند.
🔹
همچنین یک نفتکش دیگر با حدود ۲ میلیون بشکه نفت در حال نزدیک شدن به این محدوده است. نفتکش‌های دیگری با پرچم ایران نیز احتمالاً از روز یکشنبه (روز امضای توافق) از خط محاصره عبور کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/660877" target="_blank">📅 18:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660876">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0kMZHefvqcC3V7jhK5CNAg9zLVy8bnR5mw6ew62TktPYJKjWVtx8h7XtokmMmQGtUXvNnycp8kQd12doU3O0ivVeMdjshdZxS46dLbw5-Pdd253T8kGFHUSZlrPhLSrNvvAfZtiy8tCVbr0M1sTUvliUOnpHgBMoaCH7HugN5R63OvAY0An6e_WBAafpJXsHfTymJnnxnNlLhFjRAGER2dk6NnrM_kcbvVhkwyuU9fG7xehgpa42cFnBKTN_k_FJf56SVXGaMnuik0RfGG1vxb9oTob6pqpDYlXNuZNhCbId_Wmk1A-7cFJnC3dD4uzyey-PBT0ChudF1aHRiwQcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلندترین و کوتاه‌ترین بازیکن در جام جهانی
🔹
دروازه‌بان اتریش بلندترین، با قد ۲.۰۵ متر
🔹
مهاجم پاناما کوتاه‌ترین، با قد ۱.۶۰ متر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/660876" target="_blank">📅 18:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660875">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faae639bb0.mp4?token=v0tR2rnmgOmkgElXe_LR7HJKcT6SGu_40IhZIjGRwJtwJbMKfy6-AyQZWMHCIgBkeeTt4o6WpqK-JPpblFaMihPvfZx-qXr4IF9j-WHKY6zHjtLFp7F6stLflvgUIIdLTRhA1wQjsOQWGiqmsw1GswlsGedtjfKC1AYOY7QDhrd6k0dc8bGJRaHzicWVKhbefeRg6WF2LoC5Mr74DncswkAEsG3QATiIamgk5NqyfPa1I3QZAUMt-44OACi8oEprNdsdgof6DM1rtVSDaA2fvhHPS4vefz4WLn7LQxeJV6mIWLsM0TpkWS86JOk39zsugOTrU0SHoYqAr2YYzCWGNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faae639bb0.mp4?token=v0tR2rnmgOmkgElXe_LR7HJKcT6SGu_40IhZIjGRwJtwJbMKfy6-AyQZWMHCIgBkeeTt4o6WpqK-JPpblFaMihPvfZx-qXr4IF9j-WHKY6zHjtLFp7F6stLflvgUIIdLTRhA1wQjsOQWGiqmsw1GswlsGedtjfKC1AYOY7QDhrd6k0dc8bGJRaHzicWVKhbefeRg6WF2LoC5Mr74DncswkAEsG3QATiIamgk5NqyfPa1I3QZAUMt-44OACi8oEprNdsdgof6DM1rtVSDaA2fvhHPS4vefz4WLn7LQxeJV6mIWLsM0TpkWS86JOk39zsugOTrU0SHoYqAr2YYzCWGNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگ روز عاشورای امام حسین علیه‌السلام یک بخش از جهاد ایشان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/660875" target="_blank">📅 18:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660874">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
حملات اسرائیل به جنوب لبنان با استفاده از بمب‌های ممنوعه فسفری
🔹
ارتش رژیم صهیونیستی با استفاده از تسلیحات توپخانه‌ای و ممنوعه فسفری، مناطق مسکونی جنوب لبنان را هدف حملات خود قرار داد. این حملات شدید، ارتفاعات علی‌الطاهر در جنوب لبنان را هدف قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/660874" target="_blank">📅 18:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660873">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پاسخ به چندتا سوال ساده میتونه تو این روزای بحرانی سرمایه‌ خیلی‌ها رو نجات بده
ما در حال بررسی دغدغه‌های مردم درباره امنیت سرمایه توی شرایط بحرانی هستیم. تجربه و نگاه شما می‌تونه کمک کنه این مسئله بهتر فهمیده بشه و راه‌حل دقیق‌تری براش درست کنیم.
اگه چند دقیقه زمان دارید، خیلی خوشحال میشیم، این پرسشنامه رو پر کنید.
تکمیل پرسشنامه
ممنون که توی ساختن یه مسیر امن‌تر برای سرمایه همه هم‌وطنامون همراه ما میشید.
❤️</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/660873" target="_blank">📅 18:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660872">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9c038fcf.mp4?token=YA2VB4pk-h737JbeBpriJdUwjUAL1p6R9vtSXlcuvPxvCV7rtB_SB1H3xgiJu9Q9b9siaylwiSebZ19rwogoKqIaZvgSErCgbamfPnvSL6PoB7lrKn-WIPbhdqXFXxRRyWbNi7Q9U_W9cdJXdChFs54Wjtnj8fr0Vj5VMit_Zxtp9lG0wRCHAvgQK5JJnxnHrZhd_dxpuNY0DfeLmb6Bf9aqQSMY2zb5ictl55Vi45XmOV5QxO98sRBgYwak2AjFAdfbfGDNhNyEGKAhnQlnR0d9VT9RVZseSBUSJY1As4QFoxsVjkyh7c0UyZP0RYwHPRtO6XoIwi5d_Qk_-bCc4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9c038fcf.mp4?token=YA2VB4pk-h737JbeBpriJdUwjUAL1p6R9vtSXlcuvPxvCV7rtB_SB1H3xgiJu9Q9b9siaylwiSebZ19rwogoKqIaZvgSErCgbamfPnvSL6PoB7lrKn-WIPbhdqXFXxRRyWbNi7Q9U_W9cdJXdChFs54Wjtnj8fr0Vj5VMit_Zxtp9lG0wRCHAvgQK5JJnxnHrZhd_dxpuNY0DfeLmb6Bf9aqQSMY2zb5ictl55Vi45XmOV5QxO98sRBgYwak2AjFAdfbfGDNhNyEGKAhnQlnR0d9VT9RVZseSBUSJY1As4QFoxsVjkyh7c0UyZP0RYwHPRtO6XoIwi5d_Qk_-bCc4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقشه شوم براندازی در ایران از زبان نفتالی بنت؛ یک برنامه جامع و دقیق برای سرنگونی دارم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/660872" target="_blank">📅 18:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660870">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BICbWujUkxROrplDtCbfgeSUCdENnZAJDCmTdgRIJBGvztfLSjLLYhZAOdKFm0bzcQeg6NB-9lSYHL-BZlZnQ9XdS9SAtLoEE3kz1LS-oVrMPT14weY-L2CtA_N4zprQ1A8psTTLR2vWI4lAB-0z0EjM016IbslxJ8vE9VHLyOTnqIDqkF7b_JlnlA5eiWAYd_KGB3ihwzmovem0iJ9KeekD7TcgtArehPY0GDPQaFdCATrQhpvnTwCFHMVzKb0phI7JTv1DeRyHb-2dmrZp9KWuhW14jAbmdEmEqk0LwnuewZVqq7MS844k_Mj0TLhQINz6gqOdSlohUirytrr70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMOQQxkyDjHvQdusG9moiEmwwpj7f2qTsCcaMANr1iGHjZgHkisAupiLOhJA33zMTPXifiB7vft9AebS8Y4jXZqrplZMna_5A9_U01JjAzEkwgUp6Ma01MBmnrXAYh8b2RTEVMDx8hpot08pyttuxJv8xSvOTymFVv3hnFH9chkaDbRuAf-E1Vs2DtplA17vJxtvPZkBAfiSB2viTimxyneotnERMb6V7Atf9Kp5YfJJ6drtg-rdNLnPHL7GERzC8QjreBTbxPGDl3lCVfAWEHWWthPDgZKNRfJRMjcb2ieLWCh61jevSx2D4ce2ixS16JjRvU2zH8TV6lptnQohnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
متن کامل تفاهم‌نامه ایران و آمریکا به زبان فارسی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/660870" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660869">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
علی‌هاشم(خبرنگار الجزیره): مسعود پزشکیان شاید تنها رئیس‌جمهور ایران باشد که چندین حیات سیاسی مختلف را در یک دوره تجربه کرده است
🔹
او پس از جان باختن رئیس‌جمهور قبلی در سقوط هلیکوپتر به قدرت رسید. پس از مراسم تحلیف او، ترور اسماعیل هنیه، رهبر حماس، که مهمان آن مراسم بود، رقم خورد.
🔹
سپس ایران مستقیماً به اسرائیل حمله کرد. پس از آن، رهبر حزب‌الله توسط اسرائیل ترور شد. بشار اسد سقوط کرد. جنگ به مرزهای ایران رسید.
🔹
چند ماه بعد، اعتراضات شعله‌ور شد. سپس جنگ دیگری رخ داد که در میان آتش آن، رهبری کشور تغییر کرد؛ رهبر جدید در شرایطی انتخاب شد که کشور همچنان در وضعیت جنگی قرار داشت.
🔹
و اکنون، همان رئیس‌جمهوری که در میان تشییع جنازه‌ها و موشک‌ها وارد پاستور شده بود، در حال امضای یک توافق صلح با رئیس‌جمهور ایالات متحده است.
🔹
در دوران پزشکیان، ایران هرگز از حرکت و گذار از یک مرحله به مرحله‌ای دیگر باز نایستاده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/660869" target="_blank">📅 18:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660868">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
مدیریت تنگه هرمز قبل از درگیری به خوبی کار می‌کرد. هیچ مشکلی وجود نداشت
شاهزاده فیصل بن فرحان آل سعود، وزیر امور خارجه عربستان سعودی:
🔹
کشتی‌ها آزادانه در حال تردد بودند. هیچ مشکل ایمنی وجود نداشت. هیچ مشکل زیست‌محیطی وجود نداشت.
🔹
پس چرا اکنون، در نتیجه یک درگیری، باید ترتیبات جدیدی را که قرار است به آن تحمیل شود، بپذیریم؟ این، به نظر من، منطقی نیست.
🔹
بنابراین فکر می‌کنم باید به روشی که قبلاً بود برگردیم، و آن روش به خوبی کار می‌کرد، و این باید پایان آن باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/660868" target="_blank">📅 18:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660867">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/US14nWIJ1mRsDFGblkdVRpgi0B7ivA1MskBQmFvmsAvlLbpqfyaDPF9RyJFu8nDV2KQzjbRH8JNNoEQN6Zspuo4N3q-pShlg1wG78eUu72ItBYCJ6-5RcZHHX311g2wOXrgqGoseaUuWBEe4aIbVNCTCXD7ylZBfioAz8EUjlUVvM-6kF10_WnBYpC2-Vkb7yItMp-uymQZhB43U---aN5kGMb4z91S7qNaxPfLmhmAMk6tF9dMd2zIi4ApxKE1mj3AM4-yNKpcfIsl5kGYLnGsJ4DGqRLNGhlM0EE5W9QNt372QBnEIblxPMOflbZKkIcSD19ao8v_QMrMBb_s9PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبق نسخه ایران
🔹
پس از هفته‌ها تنش و رویارویی، دونالد ترامپ و مسعود پزشکیان سرانجام تفاهم‌نامه‌ای ۱۴ بندی را امضا کردند؛ سندی که به باور شماری از تحلیلگران و رسانه‌های غربی، مفاد آن از دست برتر ایران در روند مذاکرات حکایت دارد. ناظران سیاسی معتقدند فشارهای ناشی از جنگ و ایستادگی تهران، معادلات واشنگتن را تحت تأثیر قرار داد و دولت آمریکا را به پذیرش چارچوبی نزدیک‌تر به خواسته‌های ایران سوق داد. برخی رسانه‌ها حتی از این توافق با عنوان «امضا زیر نسخه ایران» یاد کرده و تأکید دارند که متن نهایی بیش از آنکه بازتاب‌دهنده مطالبات واشنگتن باشد، در چارچوب شروط و اولویت‌های تهران تنظیم شده است؛ موضوعی که از نگاه آنان، ایران را در موقعیت برتر این توافق قرار داده است.
🔹
هفتصدوهفتادوهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/660867" target="_blank">📅 18:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660866">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYibZU1eYUyNOAzgRDdo_F4ZwulXcOsaaIsZaZxqMjJrek7c_UCwYt6d7kufIR1nzMJC4p-N00BeKYTFOsPV6ZYSjCeNhzP46cdlixAqi5-dwSQZt-vWjNZ8lHGkfDFyGc31qFGLK8ZNXz2ZgPaY-JgcVdyrEzjpwL3uWct1yJeyLB_G0b2O5lVAAi3r8RAuRjBEtzhGyqjxp8AtamhOukB_3iCEjygQycuONo5vmumQwBRgQ7Nq5aEWc9vqL69mGlIT6t2gtDCgJyjgcLUf4KNbl2YedZp54U7adT1UMhS-UWixCM5uklbzcdRS-h4i9JE7zUQ04YS03EwysJaIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار نخستین‌بار؛ تصویری از دیدار سردار سرلشکر شهید حاجی‌زاده با فرمانده شهید کل قوا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/660866" target="_blank">📅 18:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660865">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkZEnYpCEgDFsVMsRA6V8vA3eLu0ox-ifo9CjoXxfCurot05ltSrt_0o4dyCoWmwvG57G-Tf6SXvkz1R5t1btz7W2llTYIQC7QrbFtM8udbXcaQgTHW5Qxt5CKbI3upXrvB6b1TY3y-BNoUwYOQ-iLN1d20y4O5BllDRH46zcnaES8XlgOgwm5grj0Ghwld0uU20CNkyaOftpcSbnPtU23kv_NThQkbdvHobYxeIWJPrX4S3DRc-2_zNzCvYAjGPLZKCAK0ri5WEYxONHiLU_rfTDP_R9MKWMeBKnQGmgxjKspxlKk6SEpqRI_67vkLHwILuHQ2-hDj2asHZld7GMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کهکشان راه شیری بر فراز قله دماوند
#اخبار_تهران
در فضای مجازی
👇
@AkhbarTehran</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/660865" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660864">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7d1aae69.mp4?token=PbA-8A04Qw25hClqk4cifWUcvbCNBQiCXtfYFbFN0c9jXQo7YLixYZOryLCPUgg2QTz919QU4V-2_thXLDux2xK7n8ev33lJIw8zkFb143KRW_xfDD2X8zo1Zrn9DNts4nLHN0RLNSagfaKLU_lfXFssa1-YKEXqvZ2fB0Kze_1yOU4T77_ZaBcwyMetqZ4FkEC6ZmTMi1amCAH2VomGY1aKivGKlywypXkke5st38DNOwdFght6Ml6qLJ4a_PQ0UWgqb_kyYlJOw-NX5m8H9y2TZTgL5AuPmSNgTBO4rCpSTU1cYFk7Ts9H5Uw_sFl649_HmUpiURrfOJREPh8CkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7d1aae69.mp4?token=PbA-8A04Qw25hClqk4cifWUcvbCNBQiCXtfYFbFN0c9jXQo7YLixYZOryLCPUgg2QTz919QU4V-2_thXLDux2xK7n8ev33lJIw8zkFb143KRW_xfDD2X8zo1Zrn9DNts4nLHN0RLNSagfaKLU_lfXFssa1-YKEXqvZ2fB0Kze_1yOU4T77_ZaBcwyMetqZ4FkEC6ZmTMi1amCAH2VomGY1aKivGKlywypXkke5st38DNOwdFght6Ml6qLJ4a_PQ0UWgqb_kyYlJOw-NX5m8H9y2TZTgL5AuPmSNgTBO4rCpSTU1cYFk7Ts9H5Uw_sFl649_HmUpiURrfOJREPh8CkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا با اسرائیل دارای سلاح هسته‌ای برخورد نمی‌کنید؟
🔹
گروسی: چون عضو ان پی تی نیست! خواهش میکنم عضو شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/660864" target="_blank">📅 18:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660862">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaQvckhHtWWKwD-i71BcQRBehNKZoeiYX-7mEcfk5kYgN1CRhwy9K7vvAusolXISOuDj6Ji7LZ5KzN-iG9MEcTV1q-KhKUw2b_mVqPTp6jIh8S7DvyC-Sqoeei_AYXbnBNgsilhirvlaIi4rgSwc91xhIP6_mA8JoPvoAzwsc3NJWDhi89IkiaX_0m4m73lE9Yx0Ax5IXe-Ct2EnSEi7F0arfeUHd66kwmhrwiyRwg4FY8jONHQttc9HMGkAirelYOQYaObVqEifg1xoWGLMYG1NXxMhUg1kGF86S7pmyV_VVgpLexmbIQoe0tdXMHY5kaQBef9KpjmREU7TeUcfjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو: ما نباید از لبنان عقب‌نشینی کنیم
نخست وزیر رژیم صهیونیستی:
🔹
ما نباید از لبنان عقب‌نشینی کنیم. ما چالش‌های بیشتری پیش رو داریم که نیازمند پایبندی به منافع امنیتی و حفظ روابط با دوستان آمریکایی ما است
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/660862" target="_blank">📅 18:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660854">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96275c4a5.mp4?token=iUkdSBwsMaDYtUhTPXtCi9NtDVPEFo3MfJnvlIu2wKhgJQSh6p2mxBZA5Q_NhnAXrGn4aN_DKCA4UFy5F3hZc5xDDCQc_zH-SuUsbI9Drl-vrPHJgriiOJsuNBGyUnk_WPxDbdeOEOlydFCUwJCpkKcIRXipf8dC2hxYYQn1YQX02F6j3xlIYzzk7OJRTSV4PvzCCnsUgpwLny19Qq2fjsbAaW6dxAbJDqDVUCNDkUuPyRMNRfpB-D8eZn-Ru0jtXUFYlS6-_JI_14Jz52cC5Ah_vfXV6578vr6UEfIqEyAm4miUiT4yk0Y353IvdEw_nJsgCs779J6OU0j9ZCxJTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96275c4a5.mp4?token=iUkdSBwsMaDYtUhTPXtCi9NtDVPEFo3MfJnvlIu2wKhgJQSh6p2mxBZA5Q_NhnAXrGn4aN_DKCA4UFy5F3hZc5xDDCQc_zH-SuUsbI9Drl-vrPHJgriiOJsuNBGyUnk_WPxDbdeOEOlydFCUwJCpkKcIRXipf8dC2hxYYQn1YQX02F6j3xlIYzzk7OJRTSV4PvzCCnsUgpwLny19Qq2fjsbAaW6dxAbJDqDVUCNDkUuPyRMNRfpB-D8eZn-Ru0jtXUFYlS6-_JI_14Jz52cC5Ah_vfXV6578vr6UEfIqEyAm4miUiT4yk0Y353IvdEw_nJsgCs779J6OU0j9ZCxJTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در اول آوریل: ما اکنون کاملاً از خاورمیانه مستقل هستیم. ما به نفت آنها نیاز نداریم
🔹
ترامپ در هفدهم ژوئن: اگر با تفاهم‌نامه موافقت نمی‌کردم، ذخایر ما در حدود ۴ هفته تمام می‌شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/660854" target="_blank">📅 17:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660852">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای منابع پاکستانی: ایران به پاکستان اطلاع داده دیگر نیازی به برگزاری جلسه حضوری در سوئیس نیست/ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/660852" target="_blank">📅 17:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660851">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
لغو سفر شهباز شریف به سوئیس  الجزیره:
🔹
سفر برنامه‌ریزی‌شده شهباز شریف، نخست‌وزیر این کشور به سوئیس، بدون اعلام دلیل رسمی لغو شده است.
🔹
این سفر که قرار بود در دستور کار نخست‌وزیر پاکستان قرار گیرد، به طور ناگهانی و بدون ارائه جزئیاتی از سوی دفتر شهباز شریف…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/660851" target="_blank">📅 17:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660850">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGlbQkKB_rJX_rrXphSM5ksZy6uuB7l28GPIKhcVuekXnuXDVj8ed4Opz2BzxGlrr4PgaNuiTNP-mPkc89CDuON13MObOrEFOej04nSEXsIBOZV7t0XVbZStbq9RG8kM8mxgyClsMvqkLTeufN7sbNk7wTQ-xnwRXYwqkjKrxaQ5UydR5b8f2VxPMp0uN3tc6s8y50JH_CEL6SAAEMBO37VKIJI89WWZcJt6icLQyLSKT4OhJxfOWNiJ_WuNYE058YPCMaSQ-JDy8EcNyOeg4Oxtt72ksjRNvi_vOGNU1_XcsIyeaikK1Qi_l75lfVe0wDwIZHgCrMcCy56aZS_I8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ: قابل شما را نداشت!
🔹
نفت در جریان است، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد (جهان امن خواهد بود!)، بازارهای سهام در حال رونق هستند، مشاغل رکورد زده‌اند و قیمت‌ها در حال کاهش هستند (توانایی خرید!). کشور ما قوی، امن و محترم‌تر از همیشه است. قابل شما را نداشت!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/660850" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660849">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBwYaSdl_RJXZArpuwh9LPjhx9XS2o7qtAC00eZWRzIsi6g8looofQbMz-HgUvbyG6AiI28X0Axb8hlMsoGdZlZPIEJ2m2m8dolsnBchY3m9QrfEzmrQxjS_UqLa41hz5K5c2D-pvRyE7wb5MjG1Vc6lbooNC2_OVR41l-INB3aEbNmn3Cwmdrba3y-oCUAyFSR9oFXsYgDLam2n6OYN6x_nglNxbv10T6LP0SK5nz0-TBnqTrKBvbkyQC8alT61xcMxtF5kQVy4z5mpaIk66lyvx_hXF_SlTWhktBEqTRYBDrij19DBryBsjKW04GFYyIZL6fJJBYSJjlAjyMlWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران خودرو قیمت افزایش داده‌اش را کمی اصلاح کرد!
🔹
این کاهش در شرایطی رقم خورد که این شرکت در یک سال گذشته چندین بار قیمت خودروهایش را افزایش داده.
🔹
در این اصلاحیه تارا توربو حدود ۲۰ میلیون، دنا پلاس ۶ دنده حدود ۱۳ میلیون و پژو ۲۰۷ هیدرولیک حدود ۷۵ میلیون تومان کاهش یافته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/660849" target="_blank">📅 17:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660848">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
رفع محدودیت تردد کشتی‌های تجاری در بنادر جنوبی ایران/تردد ۵ فروند کشتی حامل کالای اساسی
دبیر انجمن کشتیرانی:
🔹
تردد کشتی‌های تجاری به بنادر ایران از دوشنبه هفته جاری به حالت عادی بازگشته است. تنگه هرمز همچنان تحت نظارت نیروهای مسلح جمهوری اسلامی ایران قرار دارد و شناورها باید با هماهنگی مراجع ذی‌ربط تردد کنند.
🔹
تا کنون سه فروند کشتی حامل کالاهای اساسی و غلات وارد و دو فروند خروجی نفت خام داشتیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/660848" target="_blank">📅 17:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660846">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVf4tQb4x-r4tK52nfDK3ACiULgpQ3AVIaQyXcZbqze-Klzm-01yHcAxUanan15kMZ3Fw-9ZF9w2CYyFp-UyDYlXeoMgq7ax1yrzOVtCs26UtJO1o8TorQICGLFj_zJOymSfVW9ZdkKJH1WlFos3lr6ga8MkhJ_csN1OUZc7dq57-XpscBCvhwi_-mCtVnsIGJhOl5QrK7K1lROFrFmyamU1UuIIOovS0cY3ZjKR216ZKlESyC2k1y_uziiGgqV4Ra5OVmRB5V7fhn5lCKdw-6jt1qwAFkBbebQJ0IBC8WilSZCsCpQHthXCHxXt8sVS1U5FZvsqv-ez57mVP66iMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاخ ورسای فرانسه
🔹
دیشب ترامپ سند حقارت شکست نظامی اش با ایران را اینجا امضا کرد و تمام دنیا نیز دارند همین نکته را در مورد امریکا و ترامپ میگویند
🔹
در کاخ ورسای، جلسه پایان جنگ جهانی اول انجام شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/660846" target="_blank">📅 17:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660845">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
لغو سفر شهباز شریف به سوئیس
الجزیره:
🔹
سفر برنامه‌ریزی‌شده شهباز شریف، نخست‌وزیر این کشور به سوئیس، بدون اعلام دلیل رسمی لغو شده است.
🔹
این سفر که قرار بود در دستور کار نخست‌وزیر پاکستان قرار گیرد، به طور ناگهانی و بدون ارائه جزئیاتی از سوی دفتر شهباز شریف لغو شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/660845" target="_blank">📅 17:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660844">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idBSHgmbs3aqa9fIwPlKEEqZYGSqww5VXF4lBJGpwvxfIy9ayqOt0EcYzeXuyvKkzCJVSAjaxmLKiy5fGadbOgDIqcXb2yDOLxt37hHyPCx50XVJ0bt6oT4r05kLeLBzc5CShs4MWi6Z-SbL6Qaf3H0p4UfClYVsG1VfnOlBIIyOjqtyeq992XJn3QDDHL0nvipHKKbn-Fw6DEbA1wghw97YOPJHrBk22_AwMy5Rp-LQcpaB5M2SOEz_Qb3__gTv0yGNq5waOMJHEiDDB_4tm5nMNCNoUBIs5739ltAZKeXYGfLhURL8yhjjuXO5NcmoH70Cwly8FUTNv3FeRasWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعا یک فعال رسانه‌ای درباره رودرویی وزیر نفت و رئیس در ماجرای هلدینگ خلیج فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/660844" target="_blank">📅 17:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660843">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eeffe02ee.mp4?token=MmKJSEIBuZLepvVL_31G8SPbnHNkOkKPLzicp8DxJUw5pwx_UwpJ4qT1-xRbwrrRVDgpZ1OkizVeEHJtpYBjdxz9GTcxC_W6WkCtwvP0Y2u9os5Hr1ZL9pZrUQfyvkDCb1bNeACMROhZ0r5hyY5FcwwkhAF5GAcwoxsExbgCSg33MbXZylZqo7SxRimpMwOCNrIewF-UAghyhr6QxxOXu-1SXG_Ew8H-KayrxtdVM9vActQ4QGkaKujNHluAV9ihW94zFkWuISkFEcVTuvbIgJK1a_e0fY0xn_q4mkI4MEEPvus6KF-7KHxZSjFVXo1ylSnEKq34C5rzk5wuA7p3jx6gr0gyFx-kcSDLb51Wa5Ru3hCIin6rXdAndSDJq05PHFItSVLZV2OAFZs9h61RNSvIyJV_0fAU44ay0l3oWUs4wD4vIFOgizBSVdY9Fu-NavuXETu-MLSiA7b030Yo1l6T8_iCy4nwEw2jC_2Hurf3MWserUn9nTNl8j1ZY9uMALCjiNHTNK3i9LUlT0WxjaFojglJjvJoN1_9_u13iN-6lax3gAOivrDMhHNqUFLl12ohpu5gIKr045u7-HSkzQHITbZYfA73Zjcec4yriDOpZ5EXc-df42SbK4shsfyrc6zvRIkZxyvq6_Ve-xJaZ_lQlPJG7Tel15efLv6-PHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eeffe02ee.mp4?token=MmKJSEIBuZLepvVL_31G8SPbnHNkOkKPLzicp8DxJUw5pwx_UwpJ4qT1-xRbwrrRVDgpZ1OkizVeEHJtpYBjdxz9GTcxC_W6WkCtwvP0Y2u9os5Hr1ZL9pZrUQfyvkDCb1bNeACMROhZ0r5hyY5FcwwkhAF5GAcwoxsExbgCSg33MbXZylZqo7SxRimpMwOCNrIewF-UAghyhr6QxxOXu-1SXG_Ew8H-KayrxtdVM9vActQ4QGkaKujNHluAV9ihW94zFkWuISkFEcVTuvbIgJK1a_e0fY0xn_q4mkI4MEEPvus6KF-7KHxZSjFVXo1ylSnEKq34C5rzk5wuA7p3jx6gr0gyFx-kcSDLb51Wa5Ru3hCIin6rXdAndSDJq05PHFItSVLZV2OAFZs9h61RNSvIyJV_0fAU44ay0l3oWUs4wD4vIFOgizBSVdY9Fu-NavuXETu-MLSiA7b030Yo1l6T8_iCy4nwEw2jC_2Hurf3MWserUn9nTNl8j1ZY9uMALCjiNHTNK3i9LUlT0WxjaFojglJjvJoN1_9_u13iN-6lax3gAOivrDMhHNqUFLl12ohpu5gIKr045u7-HSkzQHITbZYfA73Zjcec4yriDOpZ5EXc-df42SbK4shsfyrc6zvRIkZxyvq6_Ve-xJaZ_lQlPJG7Tel15efLv6-PHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد جالب مجید بنی فاطمه و مهدی رسولی با مداحی نوجوانی که در حسینیه معلی شروع به فالش خواندن کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/660843" target="_blank">📅 17:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660842">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk22sBu3P8QfQoUYG8pYfB-lLMYxHNUugPgsr92cekX4hdBduiybE9iRzkjebJVhZjLMcJacnxr58z5DTS1NuZA5x1kzEiPNxs9dp2honFKBMb04dwI-pTDDSvSygYE9Y9MG8stu0ys6bEf_yh1DVuJOanEMlvuP6Mx5c1gW1ICrcmi1arqSvKmCx-9ltTrNfoEvFN3v7678P5g9v8CTFcN2jc89YLLqETgaF7IHwjTXSslbJ-3Lzztb9Q0YRxUCJO5WOG1XmdQAaUt26KjFyzzb59ZD_TG1lUoU4aS9fk9M9qpYLt5VERKtY8_krQn84E9XR9ZiPUUJ0Et4TxpsZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جان بولتون: توافق آمریکا به معنای واگذاری کنترل تنگه هرمز به ایران است؛ اکنون تهران می‌تواند جریان انرژی را مانند کلید برق قطع و وصل کند....
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/660842" target="_blank">📅 17:13 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
