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
<img src="https://cdn4.telesco.pe/file/vkr3Ud69VSP6xKDWzuSF8BHYM030NUsP3JES7G0OSEqP_Sp0JhE2YN1j_iApSkEgKn03aeoTRLowdy6S0bysCLXHJDHfeYaIHa4E86lATTKZm85cOh4vQO3uw2dfAkouGeMa8D2qJ5vrgAQN39zMjOl3eJq38YNfCje7HR4Gm6RFoiHXVPpklLJv4I9BNy7omAvIKCsOZfWRna_5NsUmCZTGqzPIu9s9PyjvJ6UyCZDwh0yb6f3z_b_qCJFdh6XbQ2SNaMYxR1So7pfAx5cF8qs8Kz-CDHSkV4cI1lJq8Ub4ZLlSW94B9ZPjUVr8JP-s9KJiecwa7f0nOXAyILtroQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 445K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 01:22:27</div>
<hr>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مدیرعامل توانیر: چند نقطه از شبکه برق هرمزگان هدف حملات هوایی قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/withyashar/22054" target="_blank">📅 01:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره گفت: حملات به سایت‌های داخل ایران هنوز ادامه دارد و ما پایان آنها را به محض تکمیل اعلام خواهیم کرد
@WarRoom</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/withyashar/22053" target="_blank">📅 01:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پدافند شرق تهران بی قراری میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/withyashar/22052" target="_blank">📅 01:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جزئیات حادثۀ بلوار وکیل‌آباد مشهد
رئیس پلیس راهور خراسان‌رضوی:
این حادثه زمانی رخ داد که یک دستگاه خودروی هیوندا جنسیس سدان در مسیر غرب به شرق بلوار وکیل‌آباد با سرعت نسبتاً بالا و غیرمطمئن در حال حرکت بود.
این خودرو با یک دستگاه خودروی چانگان که در مسیر موازی در حال تردد بود، برخورد کرد که در پی این تصادف، تعادل خودروی هیوندا از دست رفت و مسیر حرکت آن تغییر کرد.
پس از این برخورد، خودرو با بشکه‌ها و علائم ترافیکی برخورد کرده و سپس وارد محدودۀ حضور جمعیتی شد که در حاشیۀ خیابان حضور داشتند.
طبق بررسی‌های انجام‌شده، رانندۀ خودرو در زمان وقوع حادثه در شرایط عادی قرار نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/withyashar/22051" target="_blank">📅 01:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ارتش ایران در بیانیه‌ای اعلام کرد که در موج جدید حملات تلافی‌جویانه، پایگاه‌های آمریکا در بحرین را با پهپاد هدف قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/22050" target="_blank">📅 01:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ارتش اردن : سامانه‌های پدافند هوایی با ۱۳ فروند موشک بالستیک که وارد حریم هوایی کشور شدند مقابله کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/22049" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/22048" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تا موشک‌های سپاه برسه، از اون سمت بعدش آمریکا بخواد جواب بده داداشتون مثل جان اسنو  (نگهبان شب) بیداره ، یه لطفی کنین حالا همه که آنلاین هستین، چنل یوتیوب من رو سابسکرایب کنین که از هفته دیگه می‌خوام شروع کنم. اگه از تلگرام هم با من آشنا شدین که حتما برید اینستاگرام هم فالو کنین، چون اونجا هم یه مطالبی می‌ذارم مخصوص اینستاگرامه
📸
instagram.com/yashar
🐦
x.com/yasharrapfa
📺
youtube.com/yasharrapfa
⛑️
paypal.com/paypalme/yasharrapfa</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/22047" target="_blank">📅 00:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گزارشهای تأیید نشده حاکی از اینه که تو شیراز هم یک نفر با ماشین رفته تجمعات حکومتی، یه سری فاطی کاماندو رو زیر گرفته.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/22046" target="_blank">📅 00:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c3bf9130.mp4?token=A1R8g-SDKNsMWi7FplMJU_W7asDLuo1BiTMNGYFWmDCMMltilYrJ5nqdt2ohW43M5LG4QvkwdQlaUnPiMaxbS4gZCNCGjSANmqIf_0mZkXWCP5CGRuGDrODD7PxDq98YjmqZR7me2P4Z2tZs7MMe85iMO58X68Huq3MuRsknh7sUdezH0kmKTEb67DppuF-zVHtdJqFo1CplwvoOjytUA3SYiwexWyvP8ri37OP8UIQhmVpQXoH4XetdKhzgCj_IFVSaC_X0tXBZMIsdPlCZEqPMVnR5Yc6B6XiF-Vq-zJ4ExYGorQgRjG5HXzi4FB706mvtfHTo1xWLJ6A2dcuCiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c3bf9130.mp4?token=A1R8g-SDKNsMWi7FplMJU_W7asDLuo1BiTMNGYFWmDCMMltilYrJ5nqdt2ohW43M5LG4QvkwdQlaUnPiMaxbS4gZCNCGjSANmqIf_0mZkXWCP5CGRuGDrODD7PxDq98YjmqZR7me2P4Z2tZs7MMe85iMO58X68Huq3MuRsknh7sUdezH0kmKTEb67DppuF-zVHtdJqFo1CplwvoOjytUA3SYiwexWyvP8ri37OP8UIQhmVpQXoH4XetdKhzgCj_IFVSaC_X0tXBZMIsdPlCZEqPMVnR5Yc6B6XiF-Vq-zJ4ExYGorQgRjG5HXzi4FB706mvtfHTo1xWLJ6A2dcuCiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی قدس سه پا، ویدئویی را منتشر کرد که در آن، شلیک موشک‌ها به سمت پایگاه‌های آمریکایی در اردن را به تصویر کشیده است. این اقدام امشب انجام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/22045" target="_blank">📅 00:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb2a6fd69.mp4?token=KrmbYXuFU75HXXY-Ptz_qHesBv1_2XFScyoh5Lkli9DvvaXUoPA3YQQyTrBALyZ0v_pzCvi1I_3dY3wClUvw-CFLvJ0k8-4siSxhV6Io2EhORFejGf2r-Vfjm-4QkINKYuGdPwuweo1bwmPWSsgA0pqoIDypmhutxpRCxQzqvg6nQwhSIM7rAEkbjftTt6BqEBI14i_xFJm2BFKevzdXnAmzgV7f6griviGr2AHno01hGGHid_wipl9HoF4cvJlKCeQYuPQa8ERWCGvXv11Uy7rKm-L58ZQXPAWLaZYHFmFibOsftuMy6pW5i5ZInDohDP5zlAAN1dQubNWmfAqpaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb2a6fd69.mp4?token=KrmbYXuFU75HXXY-Ptz_qHesBv1_2XFScyoh5Lkli9DvvaXUoPA3YQQyTrBALyZ0v_pzCvi1I_3dY3wClUvw-CFLvJ0k8-4siSxhV6Io2EhORFejGf2r-Vfjm-4QkINKYuGdPwuweo1bwmPWSsgA0pqoIDypmhutxpRCxQzqvg6nQwhSIM7rAEkbjftTt6BqEBI14i_xFJm2BFKevzdXnAmzgV7f6griviGr2AHno01hGGHid_wipl9HoF4cvJlKCeQYuPQa8ERWCGvXv11Uy7rKm-L58ZQXPAWLaZYHFmFibOsftuMy6pW5i5ZInDohDP5zlAAN1dQubNWmfAqpaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ابتدایی حمله کوهستک ، سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/22044" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏گروه تروریستی سپاه پاسداران مدعی شد پادگان تفنگداران آمریکایی در اردن موسوم به «کمپ تبتین» را با موشک‌های بالستیک هدف قرار داده و ادعا کرد شمار زیادی از نیروهای آمریکایی در این حمله کشته شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22043" target="_blank">📅 00:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22042">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پرتاب موشک جدید از تبریز/ارومیه
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22042" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پرتاب موشک شاهین شهر
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22041" target="_blank">📅 00:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22040" target="_blank">📅 00:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A3nv1cXR2fghTdoqSvSwT3UPepLynyFdfHxEX0oJzNMgMqWuZ34PGUbwMMq-6jyo9VMVMIcD3DQnE6DkcBHg7B-6JDpMMOA1MiEXvp_OaaehsCErBirYWkQI4PpjvNsAHH_yQ7-g3JJBpSkzQFM8wMngxNgdy8j-sSEOiVcEl-mUvL67AaCcwceGZK82JCoJlArnwpEs2EM65JKYVgIOah4N6QqcJjBvwk7oUKFM2x9mxBKhotXu5UkjSY0ukH3L4qQ6oLU8BOrD8-GsSXC5F_hat54v-mlI0VRo0mkwrrQUtWkZ421McJhuoa84j2mBYJ0Fe865bT4gGnlUZJ993g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dpiqsya5lTBKU0UhfRe0zsyJG0ONs_popdid3m_g31-yaCkv7gtptxn0fkqjZEqW7eNcEAyeqomkZXydzD7qPp8JY1-TsxVjIhyCoxMYC6Q0PXkqJ_Krk1idwU3va6hY3xKkFP9LGbaMRdFPTup_RX0JJLhdE0a7xXFsreFWc5rIdpZ7Le_3vD7Pqiy4q6W4z9IEfzdutgikHvgQUMk8EBR8RsBZPvxqis-MpFcqV_sMCO3k0rNYUmKzgDCL6XhrhIF2R5kcJRYgYzRg5_DlGmQfAjfCvPOiafcpCZXZjHDAtmQKuw41Wn56-2qYeSNv6OgUPArDuiHb8m2HftxUPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دقایقی پیش تو مشهد، یه نفر گویا مستم کرده با ماشین به یه تجمع شبانه حمله کرده و چندین عرزشی رو زیر گرفته
😂
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22034" target="_blank">📅 00:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22033">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22033" target="_blank">📅 00:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22032">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دقایقی پیش تو مشهد، یه نفر گویا مستم کرده با ماشین به یه تجمع شبانه حمله کرده و چندین عرزشی رو زیر گرفته
😂
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22032" target="_blank">📅 00:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22031">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🤯</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22031" target="_blank">📅 00:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22029">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a99ae4fbb.mp4?token=hQhG88VaX1QEVeVwXGZe1VO2LirXq6aXYmBerGwdKGABXf8oWyKqOkKUmhlCXNpPDawYC4VDfiwzyXNsTmnoNKfYddwXVAzvcejxqZJfAimzuaYOO1K5viiL4pIoaj4TCO815tsukt_n3qPPuNWEbuhYCcr5irZMng72NsBRi1BqsfR3K5apGUNtT06Va9QP23QI1DSGyVWOuG2x0f5o2Lr3LWQFSZVf_ihHJUF12a3hVpPGXEuJYUaECg0a4i8CaM1yL5_cMF2tCSRoSHMwjuR9SOgx-MJvOSZXbfBnEZhNX7lnI2CTw3na4aGinf0-uzE34fD3GZEgqnFNpDHAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a99ae4fbb.mp4?token=hQhG88VaX1QEVeVwXGZe1VO2LirXq6aXYmBerGwdKGABXf8oWyKqOkKUmhlCXNpPDawYC4VDfiwzyXNsTmnoNKfYddwXVAzvcejxqZJfAimzuaYOO1K5viiL4pIoaj4TCO815tsukt_n3qPPuNWEbuhYCcr5irZMng72NsBRi1BqsfR3K5apGUNtT06Va9QP23QI1DSGyVWOuG2x0f5o2Lr3LWQFSZVf_ihHJUF12a3hVpPGXEuJYUaECg0a4i8CaM1yL5_cMF2tCSRoSHMwjuR9SOgx-MJvOSZXbfBnEZhNX7lnI2CTw3na4aGinf0-uzE34fD3GZEgqnFNpDHAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقایقی پیش تو مشهد، یه نفر گویا مستم کرده با ماشین به یه تجمع شبانه حمله کرده و چندین عرزشی رو زیر گرفته
😂
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22029" target="_blank">📅 23:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22028">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اگه الان بی بی بود ۱۵ رأس سپاهی هلاک کرده بود ۲۵ تا دیگشونم منتظر تایید بودیم که پودر شدن بخار شدن کتلت شدن یا زیر آوارن
😩</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22028" target="_blank">📅 23:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22027">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22027" target="_blank">📅 23:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22026">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐋𝐎𝐎𝐑𝐀𝕏</strong></div>
<div class="tg-text">داداش یاشار این زارتان زورتان گفتنت واقعا برکت داره</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22026" target="_blank">📅 23:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d64055f1c.mp4?token=MXQblqgjzcmprZm2nd8myF-NU9r04DQ9Z96gxQeBpWzHdeLMHdGCDMxkPIwyhopERPsnp9WiHIQIo0PIgJzQsNC8d5Rlcp-FMMjyMpPgZx93Q-u4Luw9Rmh4BWQQbDKUbopLHAMIV39AZFT0-FkkcULfT9N-GcIstomYon-TIOrDXHQz1faJFW4YSc_dqY8P6SXqmestijrQEaLSZ8JqehsI88SY7w01l5RvRFKXQrnPQatc_Ze6CJ5tUwNtQrO_iuS5rWn6eeMoUnqtJL25oW09-wUA7jtHQ_p-KThR9zGQmKkM48pcNcl9UNaTS8en8Aw6rrjnAXttcfau2gGhMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d64055f1c.mp4?token=MXQblqgjzcmprZm2nd8myF-NU9r04DQ9Z96gxQeBpWzHdeLMHdGCDMxkPIwyhopERPsnp9WiHIQIo0PIgJzQsNC8d5Rlcp-FMMjyMpPgZx93Q-u4Luw9Rmh4BWQQbDKUbopLHAMIV39AZFT0-FkkcULfT9N-GcIstomYon-TIOrDXHQz1faJFW4YSc_dqY8P6SXqmestijrQEaLSZ8JqehsI88SY7w01l5RvRFKXQrnPQatc_Ze6CJ5tUwNtQrO_iuS5rWn6eeMoUnqtJL25oW09-wUA7jtHQ_p-KThR9zGQmKkM48pcNcl9UNaTS8en8Aw6rrjnAXttcfau2gGhMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏حمله به دکل مخابراتی سیریک با پهپاد لوکاس آمریکای (نسخه کپی شاهد)
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22025" target="_blank">📅 23:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کاربر اتاق جنگ : وقتی از یزد میزنه یعنی جنگ ناموسی شده
@WarRoom
😂
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22024" target="_blank">📅 23:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22023">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پدافند پارچین فعال شده
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22023" target="_blank">📅 23:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22022">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رسانه های داخلی : پدافند شرق تهران فعال شده
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22022" target="_blank">📅 23:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22021">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22021" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22020">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzUxDLaydHU44ohZf9bm3XwpKcRBdZhzIGnSDuvjp8zmktvggHmnSKc4YKXtYKK4v0cKkc_Vlpd71L_GdVSGs2qti6Sf8H4QdhBTqC-HdSirsr1q18-4kdxxY-c6FFK92GZRUEbGhewoULGleGPw22oTORGmEgQx1VkI4VTv2Fk9hmJKuNyTBOQyxQU_Mu9G0SdIPPSIy_G72htttrGKX1oBNLy0VqxKG37zqv9NOWI3HahWkma68cifjQFOu-Vh_vWwrcTwBKUALgsFF_jHB72nQUxSPx_qdqPupbzLmSsxlzMwJhFmGg8act5DGAwP4AT_Gh2UlPOCzQ-CXarFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکل کوهستک ، سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22020" target="_blank">📅 23:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22019">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پدافند اردن درگیر شد</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22019" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22018">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">از همه شهر ها گزارش پرتاب موشک دارم سه پا زد سیم آخر</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22018" target="_blank">📅 23:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22017">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حدود ۲۰ موشک پرتاب شده</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22017" target="_blank">📅 23:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22016">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">از همه شهر ها گزارش پرتاب موشک دارم سه پا زد سیم آخر</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22016" target="_blank">📅 23:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22015">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هیچ خبری نیست. همین خبرها رو زدم. همچنان همین خبرها رو تکراری می‌زنند. یه اسکرول کنید بالا رو ببینید لطفاً.
😁</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22015" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22014" target="_blank">📅 23:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22013" target="_blank">📅 23:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بانک اهداف امریکا بسیار زیاد بوده امشب ! همچنان حملات ادامه داره…
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22011" target="_blank">📅 22:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">العربیه: حملات آمریکا تسلیحات و ادوات نظامی ایرانی در حال انتقال به تنگه هرمز را هدف قرار داد
آمریکا ارزیابی‌هایی در اختیار دارد که نشان می‌دهد ایران برای گسترش حملات علیه کشتیرانی طرح‌ریزی می‌کرد
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22010" target="_blank">📅 22:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7aDqojGoGAsxa4n3MBgJEAg7anY5Img-8CHx21R2PJhinLursu-B-zRrP-0Y9lxpp_8jINvhy7eg9Ggj0FYBVYP6yBcXpJuC6gMWv0vMgwa9rwErQqYrtZzC8wyVeCXCZjEHPrJM1K8kyZHtQsZybZi5pbQWWKVCZF0RhT8NeavBeEpKlby4CSjK-huPi-1iHRae4TkXQLePOI41dNdqBpskz5qx_VRMACSoqEy6BGlvG_XxdumIZMUx5sIF6j-2moFBIDnEbC2wne59oKlIIwy8IZZQBZuhctaAtDilgfSqbWv1VcyO4yUHa9u9DD_Lxfe8ym_Jfgr81XZM817tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای پزشکیان
گاز کش درحال بازگشت به کشور
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22009" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22008">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجار جدید چابهار  @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22008" target="_blank">📅 22:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دیدبان اتاق جنگ : سنگین ترین انفجار قشم تا کنون صورت گرفت الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22007" target="_blank">📅 22:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22006">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فرماندار سیریک : امریکا امشب یه خونه زده عروسی بوده
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22006" target="_blank">📅 22:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22005">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نیروهای آمریکایی کافی رو زدن برگشن پر و پیمون
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22005" target="_blank">📅 22:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بی بی نتانیاهو : مگسم سمت ما نیومده حوسلمون سر رفته
😁
@WarRoom
جوک</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22004" target="_blank">📅 22:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجار جدید چابهار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22003" target="_blank">📅 22:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">۳ انفجار جدید بندر عباس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22002" target="_blank">📅 22:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22001">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رسانه های رژیم
: نقاطی در بندرلنگه و جاسک در استان هرمزگان هدف حمله قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22001" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22000">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قشم رو دوباره زدن الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22000" target="_blank">📅 22:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21999">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سیریک کلی کشته داده نیرو های که اطراف دکل بودن ترکش هم پریده اطراف
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21999" target="_blank">📅 22:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21998">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">معاون امنیتی و انتظامی استاندار کرمان از اصابت یک پرتابه دشمن آمریکایی به محدوده خارج از باند فرودگاه جیرفت خبر داد.
@WarRoom
تو که راست میگی
🤡</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21998" target="_blank">📅 22:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21997">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فارس: منابع عراقی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21997" target="_blank">📅 22:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21996">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21996" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21995">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAZSOl-wgGzh0eZJxqH8RtF8dv87XWxVxrbmrAIOsox8TNi3ksSjYqt8lKWIWxRL85aW50K0PS3teVs8CicWzslwFJ2xDH4hbC-kSBDSt-FkjmxvdBcBAk3BwNA6ciNiFAo3ELx5TZyHWAWl0YWjjcmJMHFgpDfGCrUJYl7ZIXQY6YD77EUKyIKfC8d0tqkf369YncO0sFZO8wfQJ6q0NXkzezhyzOnnBdFSfg186EW_WqkOvIgcaOGDu6rwhWf9msi1JKUkNTmBeTc1e5Aj3bWMkX5UtWZxJjaplhi3YDFyMTWxmzyr6QhZGkQ8x2fzYPTk9LNcJtmyiTUHuZpEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک موشک با دکل ساختمان وزارت اطلاعات سیریک برخورد کرد؛ شاهدان می‌گویند دکل متلاشی شده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21995" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21994">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0159d75a.mp4?token=opY-tOg2enmoxbDy9hWXenVZkZovr_r8mk_V7mCqxJSNT1DUl50tO9XXKwliTHAHbwEvzzReY0pdmKkHrO_WqxEB6odVQCxTPlX_FOWT73FqBG3Sh0SHa-IjfeRNpaP9kd4D0fG70PCGSBCtxDAGuc7LCZ4-uIsv7gSvhgmPd4WVKUdgDr5ECsEGOIhpgK33rqP9KXjXxfM5l7JBWCRd1FIRGY0LngiFH8E1pntuFfv9NI_gRjnAhQZH5ITvdL7s8iy95F1Jv-izFqJj6VtfDI_049QSvoQVRswlYA99VqcUQo1B_p9Km22Y2-iC4jcJmu8txT5htAFGXhVFPnUn9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0159d75a.mp4?token=opY-tOg2enmoxbDy9hWXenVZkZovr_r8mk_V7mCqxJSNT1DUl50tO9XXKwliTHAHbwEvzzReY0pdmKkHrO_WqxEB6odVQCxTPlX_FOWT73FqBG3Sh0SHa-IjfeRNpaP9kd4D0fG70PCGSBCtxDAGuc7LCZ4-uIsv7gSvhgmPd4WVKUdgDr5ECsEGOIhpgK33rqP9KXjXxfM5l7JBWCRd1FIRGY0LngiFH8E1pntuFfv9NI_gRjnAhQZH5ITvdL7s8iy95F1Jv-izFqJj6VtfDI_049QSvoQVRswlYA99VqcUQo1B_p9Km22Y2-iC4jcJmu8txT5htAFGXhVFPnUn9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21994" target="_blank">📅 22:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21993">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش انفجار جدید در قشم/تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21993" target="_blank">📅 22:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21992">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رسانه های رژیم : پهپاد شاهد در وکردیم
💨
🤡
😂
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21992" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21991">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اتاق جنگ با یاشار : حملات آمریکا همچنان ادامه دارد , فرودگاه جیرفت رو زدند
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21991" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21990">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e93ddf06.mp4?token=iOiTML9TeXNwfnpug8L66-b52-UGCo0DsimFHm-4kR5XNeAi1Kp_R-IodVvclAMyMBGjI6a7DHXyn5048lx8wl-w8b1eTsk1rEmcummpXCQmBTs_Xix7YB2_NZcq_0GAh1xeTGYBCkCoGMy49ECFRQqAWSIXNv0QN6EEl3z2F3u0Deq6uKCReFym5K8IsZBsl0qu0xzT70LicUgEDMisQbPcjY2aS2yjL3M4JLwnqXChCkUeLV6RHH52VgGR3xRDM7HAmb0Y8yr9S-MjOqUOpEzK6cjZzD5fMBgx_zaOz65KCw9m-3Gihv5lg1xcJr1uN2e9K7geUICvQb19vABzbDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e93ddf06.mp4?token=iOiTML9TeXNwfnpug8L66-b52-UGCo0DsimFHm-4kR5XNeAi1Kp_R-IodVvclAMyMBGjI6a7DHXyn5048lx8wl-w8b1eTsk1rEmcummpXCQmBTs_Xix7YB2_NZcq_0GAh1xeTGYBCkCoGMy49ECFRQqAWSIXNv0QN6EEl3z2F3u0Deq6uKCReFym5K8IsZBsl0qu0xzT70LicUgEDMisQbPcjY2aS2yjL3M4JLwnqXChCkUeLV6RHH52VgGR3xRDM7HAmb0Y8yr9S-MjOqUOpEzK6cjZzD5fMBgx_zaOz65KCw9m-3Gihv5lg1xcJr1uN2e9K7geUICvQb19vABzbDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : گزارش ها حاکی است امریکا امشب مکان های حساس جدیدی رو زده که شاید تا پایان این رژیم هم اعلام نشه ولی کار اساسی انجام شده ! @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21990" target="_blank">📅 21:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21989">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش انفجار عسلویه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21989" target="_blank">📅 21:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21988">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ به فاکس نیوز: آن‌ها سعی کردند رادارهایشان را بازسازی کنند، زیرا چیزی نمی‌توانستند ببینند. ما منتظر ماندیم تا این بازسازی تکمیل شود و مجدداً به آن‌ها ضربه زدیم
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21988" target="_blank">📅 21:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21987">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ به فاکس نیوز : ناو هواپیمابر USS George Washington به طور کامل با مهمات پر شده است.
@WarRoom
💥
💥
💥
💥</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21987" target="_blank">📅 21:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21986">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بمباران سیریک هم اکنون
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21986" target="_blank">📅 21:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21985">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ به فاکس نیوز: اگر ایران به حملات ما پاسخ دهد، موجودیتش از بین خواهد رفت
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21985" target="_blank">📅 21:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21984">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21984" target="_blank">📅 21:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21983">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f800b25bb.mp4?token=EEg9m72POBXpPufeJd4vkMr4Ci5WtP358rZxUuvTBiucsjspTtX8gSMkz_EUNRLWuupkXOzLoZjizMDEUxcdPwYTX15tyeMuVPV8KaD4kHwPh_NAqHdIvjzHXC6uY9Ipx7lpa2d6u8KUo4jqL73cP9F1wOYBQaLuqQhreCgMQvI76rXdGPS7slv7JjnktMbxfBW1oowVIJ_V1KYm2FwLk0j_aVvQu79E_I32_CTgdhIfptbiYsc1uMUDSGYME-R4AENgWwGpkZZn4CicbZKDeJ2z_fpzanGx0J16XmIp_R23TiSR7I0U5GBZ92ihqEdC4yhkztxP9FNL8qCG4-nWmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f800b25bb.mp4?token=EEg9m72POBXpPufeJd4vkMr4Ci5WtP358rZxUuvTBiucsjspTtX8gSMkz_EUNRLWuupkXOzLoZjizMDEUxcdPwYTX15tyeMuVPV8KaD4kHwPh_NAqHdIvjzHXC6uY9Ipx7lpa2d6u8KUo4jqL73cP9F1wOYBQaLuqQhreCgMQvI76rXdGPS7slv7JjnktMbxfBW1oowVIJ_V1KYm2FwLk0j_aVvQu79E_I32_CTgdhIfptbiYsc1uMUDSGYME-R4AENgWwGpkZZn4CicbZKDeJ2z_fpzanGx0J16XmIp_R23TiSR7I0U5GBZ92ihqEdC4yhkztxP9FNL8qCG4-nWmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو از دیدبان اتاق جنگ از خمین
🚨
🚨
عراقی ها مردین بدزدین
😂
😂
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21983" target="_blank">📅 21:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21982">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پهپاد های آمریکایی حضور قاطع دارن
💥</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21982" target="_blank">📅 21:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21981">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">موشک خمین رو رو هوا رهگیری‌کردن زدن و سقوط کرد
😂
🚨
🚨
🚨
🚨
برگام
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21981" target="_blank">📅 21:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21980">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سه انفجار کوه گنو بندر عباس  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21980" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21979">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش پرتاب موشک از خمین
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21979" target="_blank">📅 21:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21978">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مقام آمریکایی: حملات آمریکا به ایران حدود دو ساعت است که ادامه دارد و بر زیرساخت‌های مورد استفاده برای هدف قرار دادن تنگه هرمز متمرکز است. واشنگتن انتظار واکنش ایران را دارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21978" target="_blank">📅 21:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21977">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پیج دوم شاهزاده (دفتر شاهزاده) از دسترس خارج شد @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21977" target="_blank">📅 21:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21976">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گزارش انفجار عسلویه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21976" target="_blank">📅 21:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21975">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اتاق جنگ با یاشار : گزارش ها حاکی است امریکا امشب مکان های حساس جدیدی رو زده که شاید تا پایان این رژیم هم اعلام نشه ولی کار اساسی انجام شده !
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21975" target="_blank">📅 21:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21974">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e6376e3d.mp4?token=V3ofrjJ1nwzWSfhEx8xwUF2Qt8Xjd9C7MrE47Ub0sQXc3iP2RN5iSurowH6M807Xqxf3vqlSDHEf2tqPNFlR8v38VAT2QXUhcLH1SkY7ZwsE_Bupf-w61BTL7_GpHcQMM8tmXmpZLhtieG5UJM4onoZWpZ4rOcvwbQIjHnG80RCafsIU0rZhlxZEdT647U-B99FpyC2Cr6o8jksIzYm54O7IM-inUZyYhbD7koVUwjpdRpfCyAr7Us4IrypjtVeRB5l21vg-VdhQXpvl7iSyGYfRn8XRWzKn0bTwvF2Qx-kNrQUtH6ooL4BUUZU7V5c2ag3nT2j0XOUkxQLF8SYB3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e6376e3d.mp4?token=V3ofrjJ1nwzWSfhEx8xwUF2Qt8Xjd9C7MrE47Ub0sQXc3iP2RN5iSurowH6M807Xqxf3vqlSDHEf2tqPNFlR8v38VAT2QXUhcLH1SkY7ZwsE_Bupf-w61BTL7_GpHcQMM8tmXmpZLhtieG5UJM4onoZWpZ4rOcvwbQIjHnG80RCafsIU0rZhlxZEdT647U-B99FpyC2Cr6o8jksIzYm54O7IM-inUZyYhbD7koVUwjpdRpfCyAr7Us4IrypjtVeRB5l21vg-VdhQXpvl7iSyGYfRn8XRWzKn0bTwvF2Qx-kNrQUtH6ooL4BUUZU7V5c2ag3nT2j0XOUkxQLF8SYB3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سه انفجار کوه گنو بندر عباس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21974" target="_blank">📅 21:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21973">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش مردمی انفجار در فرودگاه قشم
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21973" target="_blank">📅 21:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21972">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سپاه : مجازاتشان میکنیم
زاااارتتتتتتت
@WarRoom
😂</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21972" target="_blank">📅 21:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21971">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رسانه های رژیم گزارش‌ها حاکی است در حملات آمریکا، یک کارخانه تن ماهی در قشم، یک اسکله ماهیگیری و یک سکوی اداره بندر در سیریک هدف قرار گرفتند.
@WarRoom
😂
ارواح عمه جان</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21971" target="_blank">📅 21:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21970">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یه انفجار بزرگ دوباره در بندر عباس الان
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21970" target="_blank">📅 21:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21969">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">هم اکنون انفجار جدید در بندر
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21969" target="_blank">📅 21:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21968">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رسانه های رژیم : صدای انفجار در مشهد مربوط به ترکیدگی و آتش‌سوزی خط لوله گاز در جاده کنه بیست مشهد بوده؛ علت حادثه در دست بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21968" target="_blank">📅 21:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21967">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjbQp99o6m_9hlpg9iTI1tZfge4cldhDM_BZdzoYXYFhuM-JWCn7oiuYlAScm5kvAGoJdhLbXzG6t2O9nrafCIYLfifJzyf9IRsE4Z-f3HoTf_Rdfa9FT0ECPGEf9Rutevio3a7oxgc4PiDu4nLUR1s6J9JKvpzNbAogcbpH9Y4TpJby7qZeVX14WopVcrZNx7bx36nNQB0m0-wIrPIg0bc9vny1lZSv0mJskg_UHnwxSMaHv6iaaCFy_MigLajSFsUjPck6m_odtreilz9BZhiLGmdA9B5-aMfVqINbhBFVZjjkFqssqLRljJkeDpz_5pYQj7886CuOCSjMEtQsDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایالات متحده همین حالا در حال حمله به اهدافی در ایران، در نزدیکی تنگه هرمز است. این حملات گسترده و قدرتمند هستند و در واکنش به تلاش نافرجام ایرانی‌ها برای کار گذاشتن مین‌های دریایی در تنگه هرمز انجام می‌شوند؛ تنگه‌ای که در حال حاضر هیچ مینی در آن وجود ندارد، زیرا همه مین‌ها کاملاً جمع‌آوری یا منفجر شده‌اند! همچنین در واکنش به شلیک هشت موشک از سوی ایران به پایگاه نظامی ما در اردن که همه آنها با موفقیت رهگیری و سرنگون شدند. اگر کشور شکست‌خورده ایران در واکنش به این حمله کاملاً موجه دست به اقدام تلافی‌جویانه بزند، بار دیگر هدف حملاتی بسیار شدیدتر و در سطحی بالاتر قرار خواهد گرفت؛ اما این بزرگ‌ترین حمله از همه نخواهد بود. بزرگ‌ترین حمله همچنان در انتظار است و وقتی به پایان برسد، چیز بسیار اندکی از جمهوری اسلامی ایران باقی خواهد ماند!
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21967" target="_blank">📅 21:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21966">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLv50qGrb5sE5ad7ten94AqtnOtzFKQGPrTm-7Fnpuv2qsB0Ec40IyF7NvT9l0Py8tVNcdlZyCc4Xgh6TboTq9gmn8TrPvJO5lL0X0AWKw6aPoKsQqbRWQBDtlSmgXX5bYaZxEGo80IGYdzEH466zSgnu-urCR4R_KL1u-BsAXFn4QXfwGoWQHJfFZIEuYv-GmCzraofdbXGOQlhL9ViYxSo9CiQKn5qfT9MZ7HFAt02TjZh-sM-asWKn0NjOIfmoWESmeAzVxa1SM-sSWr-b3Sj9gi__-dWdOo-O1G_pWAM7R48a2KH-QRSY6e2Xczx13T8VC10URG2s_kIS-dwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود ناشی بعد از ۶ انفجار در محدوده/خود فرودگاه بندر عباس
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21966" target="_blank">📅 20:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21965">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دو انفجار پشت هم هم اکنون در بندر عباس
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21965" target="_blank">📅 20:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21964">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">باراک راوید اکسیوس : ترامپ و مشاورانش درحال بررسی طرح های حمله علیه ایران در تنگه هرمز بصورت بدون توقف هستند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21964" target="_blank">📅 20:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21963">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مقام آمریکایی به آکسیوس از ادامه‌دار بودن حملات آمریکا به ایران خبر داد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21963" target="_blank">📅 20:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21962">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تایید اصابت ۴ پرتابه در چابهار و کنارک
معاون امنیتی و انتظامی استاندار سیستان و بلوچستان از اصابت چهار پرتابه در شهرستان‌های چابهار و کنارک خبر داد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21962" target="_blank">📅 20:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21961">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سپاه : موشک در وکردیم
@WarRoom
😁</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21961" target="_blank">📅 20:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21960">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21960" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21959">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دایرکت هنگ کرده یه رخست بدید ۱۲۰۰ تا پیغام تو ۱۰ دقیقه لود نمیشه ! خواهش میکنم یه بیت رهبری برید
😂</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21959" target="_blank">📅 20:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21958">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjdr_WlJKhgALOXFf-iRAzjSHEVwLm6jVyAY6pKmTZwgSgf5i0MtOMSTDSqRRNjpfrb7Be37Pus0sLxM1fIlC7-K8mrvbySsg1FldQ-s5mcoQIo2uBYbphMgLoeT0XncryAgwXkkeeTj5RTcxDypQWRF7Kkidhtit87ZjZuE598pLxgDudih1A7Lxy5hYl-cJKsjiu7y1xb24_vJ-vyJuxrKYlGjRFNZMsoZcK-_2R5LKTfZXh9OOXzS-XnwQLaZ_wa2766fE_LhSw_UvheczQOgJGSj_wKhDxqF1nteiVs7vba7bcfenxW_lYkPQjUibAmKLX83sXgjDhW-GxgBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بنتلی با بدنه کامل فرج کربن
😁
یکی از ۶ تا ماشینام</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21958" target="_blank">📅 20:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21957">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21957" target="_blank">📅 20:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21956">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">موج جدید حملات شروع شده سوم یا چهارم میشه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21956" target="_blank">📅 20:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21955">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دکل سیریک رو برای بار۴۶۸۰۰۰ ام زدند
🕯️
🖤
💔
😂
🥹
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21955" target="_blank">📅 20:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21954">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش انفجار جدید بندر عباس
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21954" target="_blank">📅 20:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21953">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دایرک بیجا نفرستید ای مشرکین
😂
، فدای سر کل بچه های گروه که تو صدای انفجار قشم یا هر جای دیگرو نشنیدی می خواستی بشنوی لطفا درک و فهم داشته باشید با اونای‌که این گونه پیغام هارو میدن هستم ، اینا گزارش فوری مردمی هست من که اونجا نیستم !</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21953" target="_blank">📅 20:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21952">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">صدا و سیما : صدای انفجار در بندر جاسک و شهرستان میناب در استان هرمزگان شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21952" target="_blank">📅 20:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21951">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فاکس نیوز: نیروهای آمریکایی در حال حاضر در جنوب غربی ایران در حال حمله هستند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21951" target="_blank">📅 20:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21950">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مقام امریکایی : حملات آمریکا به ایران تاکنون با ترکیبی از جنگنده‌ها، پهپادها و موشک‌های کروز تاماهاوک انجام شده است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21950" target="_blank">📅 20:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21949">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارش انفجار در بندر کنگان
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21949" target="_blank">📅 20:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21948">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ناو لینکلن در میدان کلارک کرج دیده شد
@WarRoom
😁
😂
🚨
👀</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21948" target="_blank">📅 20:16 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
