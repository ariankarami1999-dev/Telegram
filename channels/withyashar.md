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
<img src="https://cdn4.telesco.pe/file/erPFeiKnaUHeVh78QEMtvClmwAGMlMjR6_btiJa9a620W0r-YENCT0PTZXz3I8ctnR7SEoSaJ5vc0h6iIvMrV1-HBR7MIzD_mzbiDYtXAt9D37PQbxLVy-qAF7vUSnHczkSNlQbCTiP00Qt5N2PjMlqeX8LLfZyO1jQK4hdPQLepUSozO0s7DavheWpVwN4Mnnl-LRFhepAduFBtPfMN3olTUNMcBwz3rQS7396beKFizuOfiomyjuM-8ReA89RKfo5zasaUKflUdKv3eYch3aSiNZsR_morkkHMIKiJS6OolwXLB-hHMpo6KU4ewkChp9rQUViMEG5ukVxdyEHluw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 440K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 02:49:00</div>
<hr>

<div class="tg-post" id="msg-21665">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نیروی دریایی سپاه انقلاب اسلامی: رویکرد ما در مورد تنگه هرمز تا زمانی که اقدامات آمریکا متوقف شود و این کشور به تعهدات خود عمل کند، ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/withyashar/21665" target="_blank">📅 02:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21664">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxFx7keykmaBbvQYJvWSKZANWB46xOajSZ0-oiEWDiCeMj3RUiQN8F6zmidh4ag1p5-N0Dtu7vqBaLUDpFs-CsSVDpl7qDF1TAX0tQppuU-QeV4PFcr4fj4Wxvzswa8sqpojI43SEb3dsS7ECNFwEJoo4-hJ3898Q02D7cUxCh3aRJmghSiZ00wTrdYvZMPegk6nm4CxG2c4K3trNfZSXu4wdQnZv3LrxNZ1F1Q49sh1Z64e_mL8MhtHLNhyQaly-r0THy2Ptx7NyW0EA62xuqGibobJvzNAm7Q3bc6Sgsauz9HTKWNbZS6riC4SS3nemjGoib5YdMoOHtXobOdwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای جدید نشان می‌دهند که یک عملیات لایروبی مخفی برای ایجاد یک مسیر دریایی جدید در سمت عمان از تنگه هرمز در حال انجام است.
این مسیر دریایی حدوداً 1600 فوت عرض و عمق طبیعی آن تقریباً 93 فوت است، که نیازمند لایروبی محدود برای عبور تانکرهای نفتی بزرگ است.
آمریکایی‌ها می‌گویند که کشتی‌هایی که از این مسیر عبور می‌کنند، به دلیل جزیره مسندم و انحنای زمین، خارج از دید ایران باقی می‌مانند!
@WarRoom</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/21664" target="_blank">📅 00:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21663">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اتاق جنگ با یاشار :  امشب مارگاریتا زدم
😁
ببینیم چی‌میشه … بیداریم
⚔️</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/21663" target="_blank">📅 23:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21662">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18d571649.mp4?token=kJD7qHyo0ow57hCSt5h_51tDLIfsqJwJcbkg63s0b_z8p6SS1EMy8Zse35rfz6QyD0am_ycO4PRZyd1t-UH6AQ1pZ2EE_WevWa82q7WqWyf8Tec9kX9gkBsh6lhZKUTWM2MJEd29OjwNeWO1rLCaNztQaJvHVSUAmaWxv-Fc457ZLvd-TCe5WaBNaMHtrohmth13qcpOBKrrsO505TobIsBm6VNM93ScdAi5QIN1aK6LNZyEcG6rOrzQNts3AN8S_CQBR9gHBpgR8nqwVMsB8WHfpDoXlp8ve0itn4UH0g1Bx5_MGNY9ZpPN-sjyhX02xMWZJIDTwbKlH3ubaGQbXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18d571649.mp4?token=kJD7qHyo0ow57hCSt5h_51tDLIfsqJwJcbkg63s0b_z8p6SS1EMy8Zse35rfz6QyD0am_ycO4PRZyd1t-UH6AQ1pZ2EE_WevWa82q7WqWyf8Tec9kX9gkBsh6lhZKUTWM2MJEd29OjwNeWO1rLCaNztQaJvHVSUAmaWxv-Fc457ZLvd-TCe5WaBNaMHtrohmth13qcpOBKrrsO505TobIsBm6VNM93ScdAi5QIN1aK6LNZyEcG6rOrzQNts3AN8S_CQBR9gHBpgR8nqwVMsB8WHfpDoXlp8ve0itn4UH0g1Bx5_MGNY9ZpPN-sjyhX02xMWZJIDTwbKlH3ubaGQbXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: اونایی که میگن تحریم تاثیر نداره عقلندارن
@WarRoom</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/21662" target="_blank">📅 23:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21661">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufDWwX0PlY0OYJjgfoIAbjaItdFKBuSCcw73wT0vOOPLB2pFrssWdr2HI87CH-AqwL0knDsGoPwdHlu03X3PWTz3ViIoP3ZXC4yVA_O02i2cGCxmIUeR4PpcuAcndLebmRUghgdWOl1-xvpNROgdB9JqlOq6KZNertW-7OdsN2LBym8PRsIV1Z3hguplWXZ41kpezBRPN8HO7ENsMGhiY447JQqszLnnavVoZsQyytZbhc4OmguCq6fY49Fw1Z--JuGR9_tkQuyOJFO8PTOr5ERT15J75Mm76SD5F2hQzlQNLWegWsA1d0ojGHZIVYSK8p7ZMi4WD6JwcJZdoCgz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : مخفیگاه دقیق: سه تا موشک/پهپاد ساعت نزدیکای ۲۲ از نزدیک مدرسه پرتاب شد یه تونل دارن فقط چند صد متر با خونه ها و مدرسه فاصله داره یه جاده اسفالت فرعی هست رد میشه  صد یا دویست متر بیشتر با محل پرتاب اینا فاصله نداره..سیریک-بمانی @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/21661" target="_blank">📅 23:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21660">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دیدبان اتاق جنگ : مخفیگاه دقیق:
سه تا موشک/پهپاد ساعت نزدیکای ۲۲ از نزدیک مدرسه پرتاب شد یه تونل دارن فقط چند صد متر با خونه ها و مدرسه فاصله داره یه جاده اسفالت فرعی هست رد میشه  صد یا دویست متر بیشتر با محل پرتاب اینا فاصله نداره..سیریک-بمانی
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/21660" target="_blank">📅 22:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21659">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مسعود پزشکیان هم اکنون اعلام کرد نرخ سوم بنزین، از ۵ هزار تومان به ۱۰ هزار تومان افزایش پیدا می‌کند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/21659" target="_blank">📅 22:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21658">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دیدبان اتاق جنگ : سه تا پهباد بودن یکی افتاد نزدیک ساحل
@WarRoom</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/21658" target="_blank">📅 22:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21657">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljOJodWABGdLH28-XYUuEe5OpFtNKFEwZ1XW2Nzjy88JIbc8DKoLDKvNtuNjlUS1vLJVu4GDHYRQz-T9XXaOS0ZwLtW4rA3zCprw_JlSztJ-fjuZZcGoEAhx4jSGo07pWysgmeett0kBzwBMrM_cVZc0Bj4EAjHWRSgZyQoM6IG9luRf7DeBJ0_Tu7VXQZrOAnADDxG1KIcB4Ra-fxvcPvGsNntysCpWlVg2G53YAGJYUGObQWA_mgz471tbesug6FJzzqueowP1EFTq4h_6bTYLwh0Ax5gcmr9NhZUuVH67JbAEYy_izWyANZG_PM9RgfgFF6AIw73_1mdYvkZEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در تنگه هرمز در آتش میسوزد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/21657" target="_blank">📅 22:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21656">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش ۳ پرتاب از سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/21656" target="_blank">📅 22:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21655">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گزارش ۳ پرتاب از سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/21655" target="_blank">📅 22:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21654">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مستند و مصاحبه جنجالی کامل تلویزیون إسرائيل با یک نیروی ایرانی ویژه در موساد با نام مستعار آرش در داخل ایران ( در این مستند صحنه ها بازسازی شده اند ) که در طول جنگ۱۲ روزه نقش مهمی را در انهدام سایت های پدافندی جمهوری‌اسلامی ایفا کرده بود. با زیر نویس فارسی…</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/21654" target="_blank">📅 21:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21653">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کرملین
: پوتین ۱۰ شهریور با پزشکیان دیدار می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/21653" target="_blank">📅 21:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21652">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">موشتبی ای آی : گاهی اوقات، بیان صادقانه نقاط ضعف ما، کمک بزرگی به دشمن است.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/21652" target="_blank">📅 21:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21651">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52453c0c98.mp4?token=szlAAtOmSUSx57XZvLAh1HE65RsjlRb6odCObxKsCz63-HdxdMMm_0Fa0pPahnX3tGnmhe_IV9XLdl7he1TwA-LXS5LmyrPfMUgjfitQ0wLDQ0uiajykUCSLMEJbSs2TXMZelLAhplGlQ4lbwMzTWvcAqxxw4kwQqxcPsZkwmJuyb0V6MP44bP2B2Ygelh7Ih5Vbxg0UQdAQNBcHoobA4x_-JNNJI623cc0D0r9doSuddlq-PR0rQ-GFATLE3bSzbtLb4bMgAGgko-kpSafdNoY9gcJ7jORT6VTe9ppWNbHQkvP0E9KKNNn8xEQ4srtQSXiNrwQqJuxs8yv7ZS4ziA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52453c0c98.mp4?token=szlAAtOmSUSx57XZvLAh1HE65RsjlRb6odCObxKsCz63-HdxdMMm_0Fa0pPahnX3tGnmhe_IV9XLdl7he1TwA-LXS5LmyrPfMUgjfitQ0wLDQ0uiajykUCSLMEJbSs2TXMZelLAhplGlQ4lbwMzTWvcAqxxw4kwQqxcPsZkwmJuyb0V6MP44bP2B2Ygelh7Ih5Vbxg0UQdAQNBcHoobA4x_-JNNJI623cc0D0r9doSuddlq-PR0rQ-GFATLE3bSzbtLb4bMgAGgko-kpSafdNoY9gcJ7jORT6VTe9ppWNbHQkvP0E9KKNNn8xEQ4srtQSXiNrwQqJuxs8yv7ZS4ziA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
:
می‌بینید که چقدر خوب می‌جنگیم. ما بسیار خوب می‌جنگیم. به ونزوئلا نگاه کنید. فقط ۴۸ دقیقه!
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/21651" target="_blank">📅 20:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21650">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f934b07069.mp4?token=OVyihWniYv7rAzb47L4Fi3CK7ypwpih8BCZ9hOPwV_agnrmEF-LVn0BbNUs-98I1QFbI_-6rvPlMDxh52bzqMnfRSssUrP65bb2AiyVnO9unjER0ZM0V8WeSD7wQm2j98OPAfZFEkevECr9FRMUFqFwDMX4XVvARqi2_c0BWs3OiSBvjfkjgnmVtdlCDPGV6gdU6SeouYR8P5bIPbvgwihuL-TCZKV7xs4bEYSR5a4O_VXpuabtK_INz28eQgB7xfTmbVeMokNCsOUcaK5L07HIKTBOtr-Zwnrk2PrTxPRF_B3oSv-WUoYpOVL47FThDz_NrWrgrOJ-oIRrjL-dWTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f934b07069.mp4?token=OVyihWniYv7rAzb47L4Fi3CK7ypwpih8BCZ9hOPwV_agnrmEF-LVn0BbNUs-98I1QFbI_-6rvPlMDxh52bzqMnfRSssUrP65bb2AiyVnO9unjER0ZM0V8WeSD7wQm2j98OPAfZFEkevECr9FRMUFqFwDMX4XVvARqi2_c0BWs3OiSBvjfkjgnmVtdlCDPGV6gdU6SeouYR8P5bIPbvgwihuL-TCZKV7xs4bEYSR5a4O_VXpuabtK_INz28eQgB7xfTmbVeMokNCsOUcaK5L07HIKTBOtr-Zwnrk2PrTxPRF_B3oSv-WUoYpOVL47FThDz_NrWrgrOJ-oIRrjL-dWTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«رویای آمریکایی دوباره بازگشته است؛ فکر می‌کنم این بار قوی‌تر از هر زمان دیگری بازگشته است. در حال حاضر شرایط برای ما بسیار خوب پیش می‌رود.»
@WarRoom</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/21650" target="_blank">📅 20:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21649">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2130ad167.mp4?token=SZxwYseufnyymFAKe5qaMSsuU9yYyHlL5UcCPMOus75xIc0P78Lqxc4Vq5kbhB0qe5tztWnADlwjNxeTO-MDYoCIUhwvZKyr_BhIdODjcYOqV-DodATw0DA6DaOjTJGznq3XMRrhQNG3CJV_1jsAJazz5OQOjEls4j1yEkGCPCUVf_49PBdaa5yq8DuftqBOPIQuLqRG4ugn1ZA60kAesi3Iz23pxQ5REnXyi49kP2GFK2x_QjQpNbblWmsUV22NiAb1o8BXHTwKb_0Up8v8vt7us7DEmtIZQjDsuosRkTLEJF16qLlQ36ALgF_dYO_DoFhPV1XVq8rd8xIgofJ1hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2130ad167.mp4?token=SZxwYseufnyymFAKe5qaMSsuU9yYyHlL5UcCPMOus75xIc0P78Lqxc4Vq5kbhB0qe5tztWnADlwjNxeTO-MDYoCIUhwvZKyr_BhIdODjcYOqV-DodATw0DA6DaOjTJGznq3XMRrhQNG3CJV_1jsAJazz5OQOjEls4j1yEkGCPCUVf_49PBdaa5yq8DuftqBOPIQuLqRG4ugn1ZA60kAesi3Iz23pxQ5REnXyi49kP2GFK2x_QjQpNbblWmsUV22NiAb1o8BXHTwKb_0Up8v8vt7us7DEmtIZQjDsuosRkTLEJF16qLlQ36ALgF_dYO_DoFhPV1XVq8rd8xIgofJ1hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی های
ترامپ:
«راستش من دوست ندارم با آن افرادی که پشت سرم هستند(ناسا) صحبت کنم؛ چون بیش از حد خوب به نظر می‌رسند!»
@WarRoom</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/21649" target="_blank">📅 20:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21648">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: وزارت خزانه‌داری وعده داده بود تمام شریان‌های اقتصادی باقی‌مانده برای تهران را قطع کند و به تهدید رژیم ایران پایان دهد. او تأکید کرد حامیان ایران نمی‌توانند همچنان به دلار آمریکا و نظام مالی جهانی دسترسی داشته باشند. بسنت…</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/21648" target="_blank">📅 20:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21647">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وال‌استریت ژورنال: پروژه عظیم «نئوم» عربستان متوقف شد
وال‌استریت ژورنال گزارش داده است که پروژه چندصد میلیارد دلاری «نئوم» عربستان، به‌دلیل هزینه‌های بسیار سنگین، مشکلات تأمین مالی و بازنگری ریاض در اولویت‌های سرمایه‌گذاری، عملاً به حالت توقف رسیده است.
بر اساس این گزارش، بخش‌های مختلف این طرح جاه‌طلبانه نیز در ماه‌های اخیر با کاهش مقیاس، تأخیر یا لغو روبه‌رو شده‌اند؛ اتفاقی که ضربه‌ای جدی به یکی از نمادهای اصلی «چشم‌انداز ۲۰۳۰» محمد بن سلمان محسوب می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/21647" target="_blank">📅 18:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21646">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZJssD5CItytO9fDKvmjc1PRkWEFlhfioEhw-5u0Yds4s88DgeARIk3d8NwUv_BmfJj1o7SfhIxE6w5bhRoLpMNnVEQrVNtCL2q-cFNb5rCplatERXaeEniuzDZ9eMvMfyf-RdSbd_0WjMcut23ZrZM9lQQKlrKroKVDwv1bpcVhhkDxM_NvqtKnIwMpehb37eha7yCRzuENfhRzIiH_jIk1jRInELjNiIk7ShAHf-nYV-iLKkcH4J09JcfO5qEHoX7DArgWwmVVLs1IpnF0mA4Zmc5gqAsnA6BCD7E9YwZBObsPrmQF-hlGrSOxMSvCdMj2kUM0G3_-jt0A1o_cAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری وعده داده بود تمام شریان‌های اقتصادی باقی‌مانده برای تهران را قطع کند و به تهدید رژیم ایران پایان دهد. او تأکید کرد حامیان ایران نمی‌توانند همچنان به دلار آمریکا و نظام مالی جهانی دسترسی داشته باشند. بسنت گفت
بانک مصر امارات
این هشدار را نادیده گرفته و آمریکا امروز نخستین گام را برای پاسخگو کردن این بانک به‌دلیل آنچه «حمایت مستمر و فاحش» از رژیم ایران خوانده، برداشته است.
وزارت خزانه‌داری آمریکا:
در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast)، شبکه اجرای قوانین جرایم مالی آمریکا (FinCEN) پیشنهاد کرده است
دسترسی بانک مصر امارات به خدمات بانکداری کارگزاری مؤسسات مالی آمریکا لغو شود
؛ اقدامی که عملاً دسترسی این بانک به بخشی از نظام مالی آمریکا را هدف قرار می‌دهد. همچنین
دفتر کنترل دارایی‌های خارجی آمریکا (OFAC)، رضا محمد تأییدی، مدیر بانک ملی دبی، و یک شرکت پوششی مستقر در هنگ‌کنگ
را تحریم کرده و مدعی شده این شرکت در پول‌شویی وجوه برای یک صرافی تحریم‌شده ایرانی نقش داشته است. خزانه‌داری آمریکا این اقدامات را بخشی از تلاش برای
قطع آخرین شریان‌های مالی مورد استفاده حکومت ایران
عنوان کرده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/21646" target="_blank">📅 18:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21645">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارش ویژه فاکس نیوز : ترامپ ‌به فاکس نیوز می‌گوید ایران با افزایش فشار اقتصادی، صف‌های طولانی بنزین و تورم فزاینده‌ای که کشور را تحت تأثیر قرار داده، «برای توافق التماس می‌کند».
وزیر امور خارجه ایران می‌گوید دیپلماسی هنوز امکان‌پذیر است، اما استدلال می‌کند که فشار ایالات متحده مؤثر نخواهد بود و از واشنگتن می‌خواهد که اعتماد را بازسازی کند و به حقوق ایران احترام بگذارد.
در همین حال، مقامات نظامی ایالات متحده می‌گویند که خطوط کشتیرانی بین‌المللی پس از عملیات مین‌روبی در تنگه هرمز باز هستند، زیرا رهبر عالی ایران همچنان از دید عموم پنهان است.
@WarRoom</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/21645" target="_blank">📅 17:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21643">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Egabob8QKt6MLEmIL44jwakZerrA-ciPEQADtOMwGCiXJ3DqLgyVRl_hLxmn1VmTxq3Kn76_VOY9RqCQuUeXs2uQEdOL5FOqvvlpq-60puyzKCd2qo3ixtocCYKtf38D9k2gnZ6YOZ75_pel1e_3qY-Npj1fhweW5PuMBDOqvvjmEC5VRF4HIamL97iFlB31rYII9XH2_ho9ZD-VSr7EY2UT9VRyLn9auWzlT1q8btYUfJLF8iHbwJFMoguEwFgE1Ce1hXbYaDE18uYbMGtMGhpDwe6Xg0jPqHV0kNEc1IadBqpnvYyBEuHf2QJNe6YrlssDEH78tJsxH50UgR5DrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دید بان اتاق جنگ : هم اکنون ستون دود از سمت شرکت کاله آمل پیشتر کارخانه کاله آمل در ۱۵ دی ۱۴۰۴ (۵ ژانویه ۲۰۲۶) دچار آتش‌سوزی گسترده شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/21643" target="_blank">📅 17:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21642">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دبیرکل سازمان بین‌المللی دریانوردی:
حدود ۶ هزار دریانورد در ۴۰۰ کشتی همچنان در تنگه هرمز گرفتار هستند
@WarRoom</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/21642" target="_blank">📅 16:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21641">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhTF8G3jWzCoQfun_ISV43DSMfIyNutvKjjXR7kUqbiszJ8QLJEZYqO2RrSPRMC0xiugk4dhS3ze8RXCom35v0DZeVMPDuLH2MdXJ3ATIrBUmMwonQCwNesGt1VEVuzJj1taCqofKvw2leaxZ370srqYJCNFQuIa-jCQeZLsf0WGiBx6VjaPCreuz1hUgctBH3A_2f96Z7C1jYa7rVqu27fSXoB8MpPovMQ70TN1mHNWwZscHDXlPHDEzK0h8B-WeoyVMWhwTdGKc9g6D1bAltZQVx8xDI8di9MV0Fm7UeXzAbdFtGNKY4KkPmZ4VkrTI2z9Ed1ajnY02X-ddK52Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دیگه از اون آدم مهربون خبری نیست.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/21641" target="_blank">📅 16:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21640">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مستند و مصاحبه جنجالی کامل تلویزیون إسرائيل با یک نیروی ایرانی ویژه در موساد با نام مستعار آرش در داخل ایران ( در این مستند صحنه ها بازسازی شده اند ) که در طول جنگ۱۲ روزه نقش مهمی را در انهدام سایت های پدافندی جمهوری‌اسلامی ایفا کرده بود.
با زیر نویس فارسی
@WarRoom</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/21640" target="_blank">📅 15:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21639">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yxf6FU5PjGXMIhgSKxd5jdFirK6v7N4xo67zZxuhKGSl-AtUN1YHxdPtDDWblPDwm9JF-IIGWgOxAo_LLoCbPoXXAVzvuxox00AISXl4EOuKR6kOieWqqRaJWq28t1UTJC3aNVNIGrkARSgXF1mCSxz-R7Xamg2KOn6RxYQz4ea8_3Vs7xQavRSIBGo5bAhpdprnmNyVcKSHZij1mHHhupYApmqC0bVLBMJ4uBBr0KVvttU3eJfPnzoULiThbH602bs4J9dNetIvG0hZ0-flsQ5Ls64_P9tsDDiHzX9D_G_8fy4eFJmhRyCkbEYcVgG2CZv5SguDnzmAw636Yuib5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دید بان اتاق جنگ : من با یه صدای لرزیدن شیشه اتاقم بیدار شدم دوباره خوابیدم  ، بعد نیم ساعت رفتم دم پنجره یهو چشمم به این افتاد @WarRoom</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/21639" target="_blank">📅 15:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21638">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50b72f483d.mp4?token=gvoOJwQpn9HtsjNjgt70lvNqtzYB-xEWkebE0zhWAAA0H9uQmcN0lYdJmkmo9xzeAyQ6eov7GenK92r1ZLoWMe0AqFxtIcxmpt9AAIemvLiw_RGg8FhCDesyL9wFEkWeuMmA351uwMKyGKSNCg04wcBQV4K9f5flgW8cd7z6LxoakMMiB4PE69wN6zfxj59YyHQOYmIS5f6YU5zWPEBlh3dsU5FwGE6HnZXClnYjnQZT0j5k5KQc9BTz9KqIuF8OvrFdBMZ0IzQ-yYNEDeY-6TkvW2UvUl5bkrpif5PJgd7s0P7HgBQCu2IyDDKb7Vucqv-dS_XPgnmyJc0tuV8d4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50b72f483d.mp4?token=gvoOJwQpn9HtsjNjgt70lvNqtzYB-xEWkebE0zhWAAA0H9uQmcN0lYdJmkmo9xzeAyQ6eov7GenK92r1ZLoWMe0AqFxtIcxmpt9AAIemvLiw_RGg8FhCDesyL9wFEkWeuMmA351uwMKyGKSNCg04wcBQV4K9f5flgW8cd7z6LxoakMMiB4PE69wN6zfxj59YyHQOYmIS5f6YU5zWPEBlh3dsU5FwGE6HnZXClnYjnQZT0j5k5KQc9BTz9KqIuF8OvrFdBMZ0IzQ-yYNEDeY-6TkvW2UvUl5bkrpif5PJgd7s0P7HgBQCu2IyDDKb7Vucqv-dS_XPgnmyJc0tuV8d4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : اگر ایران سلاح‌های هسته‌ای در اختیار داشته باشد، این پایان اسرائیل و پایان مردم یهود خواهد بود. و مهم نیست که چراغ قرمز باشد، چراغ سبز باشد یا چراغ آبی؛ من به رنگ چراغ اهمیتی نمی‌دهم. این برای من مهم نیست. ما باید این کار را انجام دهیم، زیرا در غیر این صورت نابود خواهیم شد. ما دیگر اینجا نخواهیم بود
@WarRoom</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/21638" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21637">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175422b47.mp4?token=Torc6LTpQm0t7_PfX0-jMs_f9pRpRv_QFIRm2R4IymWZaHjzQTIug_uX20XqA1DAhq5Ea_RLanWPEaKYqjjSHy5Wqr4jIdyz1NHX9HqOyLUKiZduygG67EKS74e5iunI_XezP97pMzMp1M02WsquOEbYhEHodOqKaM0tmb1U9LpD2Ge_0h5JrW0ZsO2wdEBT8jqAVfyIAtBS7pKZtI7I5FSplL9Ks-gqsdr-fqpr7v2FHspXeVAf8q6iPkPXjaOViGTgQl04bmaDSaBP9y_qYZfkoP713IkeZjHQMWkfHvAn8aRSVNPMAkWIqp8_HpK7XTtF3bcoWgsfl3q8P2dODw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175422b47.mp4?token=Torc6LTpQm0t7_PfX0-jMs_f9pRpRv_QFIRm2R4IymWZaHjzQTIug_uX20XqA1DAhq5Ea_RLanWPEaKYqjjSHy5Wqr4jIdyz1NHX9HqOyLUKiZduygG67EKS74e5iunI_XezP97pMzMp1M02WsquOEbYhEHodOqKaM0tmb1U9LpD2Ge_0h5JrW0ZsO2wdEBT8jqAVfyIAtBS7pKZtI7I5FSplL9Ks-gqsdr-fqpr7v2FHspXeVAf8q6iPkPXjaOViGTgQl04bmaDSaBP9y_qYZfkoP713IkeZjHQMWkfHvAn8aRSVNPMAkWIqp8_HpK7XTtF3bcoWgsfl3q8P2dODw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویری که ادعا می‌شود برای بندر کنگ و لنگه امروز صبح هست.
@WarRoom</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/21637" target="_blank">📅 15:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21636">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2bad7297.mp4?token=KAF2_qcC14MgYyidt2l_2fqB-MNIMtSAW3hbHywSb7-k6frgjEy6VDftm2gQr8p4EZNvAi30fnQCW8oYCs-trbKM4Ze4gxAQ_rObDZrqfA2f9Xc0VKcpR3LQ_19LEbfWs7Pju4UpnVKGRSHmfUZisuq5HTGIAevQeW7Tyuh2ctdoktX0b4QcgFI27ER58FmPnPTwyD0kurGvcuTWPAqfkYt0PEOVWpfZBbPSyHJcOB0tYQgiAErRuMlBc2SZyV8l0tNmGxKQi5P-9ylMISe32fYSSfJkOl3_ZerbDu0anSFqk7QL4V-PgtNpFu5XTVJz4jQfBRKsfpDqJcwFLVR4xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2bad7297.mp4?token=KAF2_qcC14MgYyidt2l_2fqB-MNIMtSAW3hbHywSb7-k6frgjEy6VDftm2gQr8p4EZNvAi30fnQCW8oYCs-trbKM4Ze4gxAQ_rObDZrqfA2f9Xc0VKcpR3LQ_19LEbfWs7Pju4UpnVKGRSHmfUZisuq5HTGIAevQeW7Tyuh2ctdoktX0b4QcgFI27ER58FmPnPTwyD0kurGvcuTWPAqfkYt0PEOVWpfZBbPSyHJcOB0tYQgiAErRuMlBc2SZyV8l0tNmGxKQi5P-9ylMISe32fYSSfJkOl3_ZerbDu0anSFqk7QL4V-PgtNpFu5XTVJz4jQfBRKsfpDqJcwFLVR4xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دید بان اتاق جنگ : من با یه صدای لرزیدن شیشه اتاقم بیدار شدم دوباره خوابیدم  ، بعد نیم ساعت رفتم دم پنجره یهو چشمم به این افتاد
@WarRoom</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/21636" target="_blank">📅 14:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21635">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آکسیوس گزارش داد روزانه حدود
۲۰ تا ۳۰ نفتکش
از مسیر تحت حفاظت آمریکا در تنگه هرمز عبور می‌کنند و حدود
۹ تا ۱۰ میلیون بشکه نفت
جابه‌جا می‌شود؛ نزدیک به نیمی از صادرات پیش از جنگ. امارات، بحرین و کویت به این مسیر پیوسته‌اند و عربستان و قطر نیز ممکن است به آن ملحق شوند. آمریکا قصد دارد با
افزایش عرض کانال اصلی کشتیرانی تا اواسط سپتامبر
، امکان عبور حداقل
۵۰ کشتی در هر شب
را فراهم کند و در نهایت
۶۰ تا ۷۰ درصد صادرات نفت پیش از جنگ
را احیا کند. آکسیوس همچنین گزارش داد حدود ۲ درصد کشتی‌های عبوری ماه گذشته مورد اصابت قرار گرفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/21635" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21634">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ed644e27.mp4?token=fbMf6C16gphaUy_QxLCKqzLqZhGSEEbrwM_epXMQ_ANnuEjYL9jakDjnh45mNMN0-76PeVFlBefFmQC-UzIT-FnvFWUvImqGm8lNV17H1hsSfmQb25ot-5HHSsTe3YPA_FUK5mWPUadOxO--pUJHS0YUw-ZeN2buOWoDbozroa4KbbSOTyguO3xaJxjQkAho9t273pjgpnitDD3yodRVTOvfnknXMRWGcDuV-NTQoHph9jOn2KIJP4zwGRHvIqww34vgaoa0Ukjcu4lt2nciumxVPqP9Qb-gK_EqdTY0vK5DG23Q-oMIbzkUOkVLcx0vvr7pMXQizbsbrDmpRXhk0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ed644e27.mp4?token=fbMf6C16gphaUy_QxLCKqzLqZhGSEEbrwM_epXMQ_ANnuEjYL9jakDjnh45mNMN0-76PeVFlBefFmQC-UzIT-FnvFWUvImqGm8lNV17H1hsSfmQb25ot-5HHSsTe3YPA_FUK5mWPUadOxO--pUJHS0YUw-ZeN2buOWoDbozroa4KbbSOTyguO3xaJxjQkAho9t273pjgpnitDD3yodRVTOvfnknXMRWGcDuV-NTQoHph9jOn2KIJP4zwGRHvIqww34vgaoa0Ukjcu4lt2nciumxVPqP9Qb-gK_EqdTY0vK5DG23Q-oMIbzkUOkVLcx0vvr7pMXQizbsbrDmpRXhk0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف پمپ بنزین پشت زندان رجایی کرج , ساعت ۲ ظهر امروز جمعه
@WarRoom</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/21634" target="_blank">📅 14:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21633">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیویورک پست: پسر ترامپ، زندگی منزوی را سپری می‌کند، در حالی که با تهدیدات از سوی ایران و تلاش‌های برای ترور پدرش روبرو است. او به شدت تحت تأثیر ترور چارلی کرک، فعال محافظه‌کار نزدیک به او، قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/21633" target="_blank">📅 14:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21632">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پروفسور جان مرشایمر، استاد علوم سیاسی دانشگاه شیکاگو : وقتی فشار اقتصادی یک کشور را تا مرز فروپاشی می‌برد، معمولاً آن کشور تسلیم نمی‌شود، بلکه برای بقا واکنش نشان می‌دهد و دست به حمله می‌زند. مرشایمر با اشاره به حمله ژاپن به پرل هاربر در سال ۱۹۴۱ گفت فشار اقتصادی شدید آمریکا علیه ژاپن و قطع دسترسی این کشور به نفت، در نهایت به واکنش نظامی ژاپن منجر شد.
او درباره ایران نیز گفت اگر تهران احساس کند بقایش در خطر است، به آمریکا و متحدانش پاسخ می دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/21632" target="_blank">📅 13:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21631">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آکسیوس گزارش داد آمریکا در نبرد بر سر تنگه هرمز به‌تدریج دست بالا را پیدا کرده است. بر اساس این گزارش، نیروهای آمریکایی با هدایت و حفاظت از کشتی‌های تجاری، عبور نفتکش‌ها از مسیر جنوبی تنگه را دوباره برقرار کرده‌اند و مقام‌های آمریکایی می‌گویند کنترل عملی این مسیر اکنون در اختیار آنهاست. اگرچه حجم تردد و صادرات نفت هنوز به سطح پیش از جنگ نرسیده، اما نفوذ ایران بر رفت‌وآمد دریایی در هرمز نسبت به ماه‌های گذشته کاهش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/21631" target="_blank">📅 13:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21630">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزارت امور خارجه رژیم :
تمام کشورها موظف هستند از اعمال تحریم‌های یک‌جانبه توسط ایالات متحده خودداری کنند، و تحریم‌های اقتصادی ایالات متحده علیه ایران غیرقانونی و فاقد هرگونه مبنا هستند.
@WarRoom
یاشار : بابا شما که قوی هستین چرا ترسیدین ، تحریم هم که برکته
🥴</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/21630" target="_blank">📅 13:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21629">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ در مصاحبه با شبکه 12 اسرائیل: این موضوع «تنگه» هنوز باز است.
واکنش ایران بسیار ملایم بوده است. آنها نمی‌خواهند ما دوباره به آنها حمله کنیم، این تمام ماجراست. بقیه چیزها مهم نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/21629" target="_blank">📅 13:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21628">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بلومبرگ : قطر در ادامه اختلالات ناشی از بحران تنگه هرمز، وضعیت «قوه قاهره»(حفاظت حقوقی و قراردادی در شرایط اضطراری) برای تحویل گاز طبیعی مایع (LNG) به مشتریان آسیایی و اروپایی را تمدید کرده است. این تصمیم به‌دلیل ادامه محدودیت‌ها و ناامنی در تردد کشتی‌ها از تنگه هرمز اتخاذ شده و بازگشت صادرات گاز قطر به سطح عادی را به تأخیر می‌اندازد. قطر پیش از جنگ یکی از بزرگ‌ترین صادرکنندگان LNG جهان بود و اختلال در صادرات آن، فشار بیشتری بر بازار جهانی گاز، به‌ویژه در آستانه فصل زمستان، وارد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/21628" target="_blank">📅 12:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21627">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش‌ها از سوریه: نیروهای ارتش اسرائیل (IDF) با آتش سنگین به منطقه تپه بت‌ال‌ورده، نزدیک به شهر بیت‌جان در مناطق روستایی غربی دمشق، شلیک کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/21627" target="_blank">📅 12:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21626">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نرخ دلار ۲۰۱،۵۰۰ تومان
دلار کف بازار  ۲۰۰-۲۰۵ هزار تومان
تتر ۲۰۰،۰۰۰ تومان
بیتکوین ۷۹،۷۸۰ $
انس جهانی طلا ۴،۶۰۹ $
نفت برنت  ۸۸،۰۸$
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/21626" target="_blank">📅 12:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21625">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فری استایل یاس به همراه من (یاشار رپفا)
۲۰ سال پیش و زمانه همچنان بی رحم است…
@WarRoom
@RapFA
✅</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/21625" target="_blank">📅 11:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21624">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ql-3sMXqQHv24b5z5KLZbXg5BDBZhX10mXY3v6kgTZm1zlgWP1N1nh2Q31qETn8fJhZjGKQvXlyNbnQMb2WRlRbGyPr1krC7r_3VynZFnkVMWgkSzOvYpASkFaq5xc3cvBwzQSMpJmPwNOcdgC38xfhW4sawEN51FODs4VCV0ncdhZZYaQV0x8GPCPm2VW2KiyQzU1TeUjUwtvgz_OCcO_ItrzVbBVZRT3LvSNePhnPli0D0RpaDQnUN-x5nMrZGTg1CMTZ-E2VNgNXtI_uidVUxOko69_Ur7j2gcPcQU25Ob3_olnBo4dMT0nvPKD6XpPbxOdDsf45secJ5UNjUvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی از دیدبان اتاق جنگ : کاری با دست خط ندارم سطح سواد عرزشی جماعت که برای ۹۰ میلیون نسخه میپیچن (اسرائیل)
@WarRoom</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/21624" target="_blank">📅 11:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21623">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آغاز واریز سود سهام عدالت:
سبد ۴۵۲ هزار تومانی: ۴۴۳ هزار تومان(۲.۲۰$)
سبد ۵۳۲ هزار تومانی: ۵۲۱ هزار تومان(۲.۵۹$)
سبد یک میلیون تومانی: ۹۸۱ هزار تومان(۴.۸۷$)
@WarRoom</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/21623" target="_blank">📅 11:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21622">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRZJkZ2dlHJO9KLaWlgqIrohC7OaBZPHjsWBplZwMhJjKuaE52WMC0U69vcVyyCveI12horjTcbjZlbx3SdKdUTTnmJQLlOD1LrbC2l81tb-4OnPEMyhrFFb2ZSU7BgbqONIZROkYVYOm2hPG-me3YVIueiwGFxQK6P5Otf3TpFx-5xgxru8m_voZ-DaotLUdJpnXy0DWl2LxWa9g_QgQc8ZrJHQg2PXOLGyBupJeSIJ4iWizsIkDlHi7fDL8UkUa4kEocPrxNHP-3X37us4dTixHko2V92gvV_5RLO-rBV680f5s6O00DLcyJZPadDjHr_JPvmQQWRPegWgXRZlMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث دوباره:  تنگه هرمز در حال حاضر قلمرو جدید آمریکاست
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/21622" target="_blank">📅 11:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21621">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEDkUDvMfDFSTRCtQpznItlnpRTmM1ACNw3ZFqAeiiQYseYf1erj_FIO6ygcyp4-E1kRPllUjzXSE40me1qLP1cWjy-AzRj_xePrF5k--hPp7ftzjikOhLw763-8uimTDSOnY1gcLRXlamw3BvW7uIZ6Ya-MFb278JIawb7pvfDSPfo8CBzdt7p_D71bGwvk-UChrUJWmmQk6u_2tLS6o0xoGj1EfnrekGT1QzOb-bXVNjf48L0cNfrFy-oBmEOIjlDADMDk5TgiC0Eppb-Z1DtujIPgZ4Ssk5GbMW5L40TSrNOSkffePViomWmBjMpHJZXspvNP9NFnQ13IJnfQWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هارالد پنجم، پادشاه نروژ و مسن‌ترین پادشاهِ در حال سلطنت اروپا، در ۸۹سالگی در بیمارستان دانشگاهی اسلو درگذشت. کاخ سلطنتی اعلام کرد او صبح امروز جمعه ۲۸ اوت، ساعت ۶:۳۵ به وقت محلی، درگذشت. هارالد از ۱۹۹۱ پادشاه نروژ بود و بیش از ۳۵ سال بر این کشور سلطنت کرد. او به‌دلیل کم‌خونی همولیتیک تحت درمان بود و پس از ابتلا به یک عفونت باکتریایی در خون، وضعیتش به‌شدت وخیم شد. پسرش، ولیعهد هاکون ۵۳ ساله، اکنون پادشاه جدید نروژ شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/21621" target="_blank">📅 10:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21620">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی آمریکا (سنتکام)، مدعی شد نیروهای آمریکایی از زمان آغاز محاصره بنادر ایران، عبور حدود
۱٬۵۰۰ کشتی تجاری
و انتقال
۷۵۰ میلیون بشکه نفت خام
از تنگه هرمز را تسهیل کرده‌اند، در حالی که به گفته او، ایران اجازه صادرات حتی یک بشکه نفت خام را نداشته است.
کوپر همچنین مدعی شد هیچ کشتی ایرانی بدون اجازه سنتکام وارد یا از بنادر ایران خارج نشده و تنها در موارد بشردوستانه اجازه تردد داده شده است. به گفته او، تاکنون حدود
۷۵ کشتی تغییر مسیر داده شده
و
۳ کشتی
از زمان آغاز محاصره بنادر ایران از کار انداخته شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/21620" target="_blank">📅 10:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21619">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
«محاصره و عملیات “
طرد اقتصادی
” اقتصاد ایران در حال فروپاشی l را درهم خواهد شکست. آمریکا طی ۱۴ روز گذشته با مدیریت خود
۱۳۰ میلیون بشکه نفت
را هدایت و منتقل کرده است.
ایران: صفر.
@WarRoom</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/21619" target="_blank">📅 10:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21618">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmntVcj_lG5rHjoRtX_PX6KMv9VFbME4ldAqyl5Rf7kjeZ5XHpYvyDZ8tTs0MmIWtmQ_7VpDaoy15iKi6fh0Q6lei0Sv_8vxcTk9c9JBNCJx4otwZCZpgDpHbOfX_7l2Q8LF1k185l0Zp3t43aZpIZVDZ9OHEaA1h4FitmSxD9Th4g4XbB_SHuU7_C3mscr3vKA2Z5FxYmCD4u4wGtB-UZbkHMvjyONZipQdFu7kHkYHQm7NXdUnYxtV1B_1uWhoCm2OUE7mSoQ6vXS39_GF6sTOf1jzN4fvtGLh0wYeOtzhfwvRPzQ3m8eTDtJszPCVdKRtOPT0pDzuQRPiLPgUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ با انتقاد شدید از گزارش جاناتان هانت، خبرنگار فاکس‌نیوز، آن را «بسیار نادرست» خواند و گفت: «من نمی‌خواهم با ایران دیدار کنم؛ آنها هستند که می‌خواهند و برای توافق التماس می‌کنند.» به نظر می‌رسد این یک سوءتفاهم باشد چون هانت در گزارش خود گفته بود مذاکرات مستقیم میان آمریکا و ایران فعلاً در جریان نیست و دولت ترامپ به‌جای مذاکره، در حال تشدید فشار اقتصادی و تحریم‌هاست؛ هم‌زمان کشورهای عربی، از جمله قطر، برای گرفتن امتیاز از تهران تلاش می‌کنند. ترامپ در ادامه از برت بایر، مجری فاکس‌نیوز، خواست «زیردستان بی‌کفایت خود را سر و سامان دهد». بایر نیز در واکنش گفت هانت «خبرنگاری عالی» است و تأکید کرد فاکس‌نیوز اصلاً نگفته ترامپ خواهان دیدار با ایران است، بلکه برعکس، در گزارش به صراحت گفته شده بود ترامپ نمی‌خواهد دیداری انجام شود و مذاکراتی در جریان نیس
@WarRoom</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/21618" target="_blank">📅 10:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21617">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سازمان عملیات دریایی بریتانیا بامداد پنجشنبه گفت که یک نفتکش در آب‌های نزدیک منطقه «الخصاب» در شمال عمان، مورد اصابت یک پرتابه نامشخص قرار گرفته که باعث آتش‌سوزی در آن شد. @WarRoom</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/21617" target="_blank">📅 09:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21616">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5CDzx8DdspE1VkdaRuhc0WZFtx9wxKViKErXcTIEBBF5-mK-t1mjvpJ9gZ1oleP1fUQ8azskMKkePENftiowoGKUq8-OzH0hg1GbV_jk_KBORt4lAiy-zKL8_vdqRYwXDseSYWyPLTQBs6lnhWDLRi-BWxWbk31cf3kZ2MerYtOIFAh6HNnlI8oFyGT-WxbN8anRymWA4XAntv3VSWmx0Z9gTxQxRM-7OZyar4EqLu9iZx8FdJMFjQv6LdmTMktLGo-bIzQVQN6ruVsKlTSkCdT5ig0_aYV_PBf-h6gHmjNS_2a6M40eaQ9MSdFw8o4gH9AFgCnzTyZh8ar8EnbIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایران کشوری رو به فروپاشی است
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21616" target="_blank">📅 09:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21615">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucDNroIdLVfisY8TA8wgNLuU-YAjwUgtnb8wjPcq3pW-TwvzxgWKsWp7Q3C6JxjuuTsKHFYC0tJJiZVnl4h93mAmjmuxqU7Jdh7TKs-_DGRYOpydxQwWBTHne_7Lozrm_fUbGBIhsIwbsMlU25dcEOnE1ZP3nDvYi5p5dRWeXil2Q3c8DcL7E14uxIEnXnky_M970L0xnTADOplMbp-HrgAAN4vAroauJ7MsrM3SnuKiiyLJOVaH85J7LMl2-ZCSpIGgDHhh6AXVlEUJjrSJAR20DsbbrSCL08dkIl7uZ2DvWrZXZTvt1HSsJTIn31NYkw7mXQTDQ8x7KmC0fnLrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ سوخترسان آمریکایی و ۲ پهپاد در خلیج فارس در حال مأموریت هستند ، بعد از مدتها این حجم مشاهده میشه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21615" target="_blank">📅 00:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21614">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d6860a3c4.mp4?token=k5zM9zRhCEu1jh2rx7KpR6W1UXoP6t3a6bdILjwEW1P5cyOhrh-Itus7-_mdXL6tAqqV0zrjB2lHQtsRgIObmftOuIL-GK64Zu_RLMn5EnDh6-AxNG8gCjTW2QLqBcevTHwY-EGkRhVOG8FGuBoZ0lSwlF_Taaov_wlJvFHfapckLEFQVqgFUOuPp33EttHIAcdXx6aDoEK7JU0lXJ6wryZjvoTaakXz-UqfMxPM8J-Y82v7vcDJk1B3id5FS0UYe1bOmbRuU69EOJF2e9ENsBbVimY7GzNAJ9tZ_z9TRJSP6YTQQzyR_7mSrWkGcuGPDAf4DzBji_7wbr9GJG6kTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d6860a3c4.mp4?token=k5zM9zRhCEu1jh2rx7KpR6W1UXoP6t3a6bdILjwEW1P5cyOhrh-Itus7-_mdXL6tAqqV0zrjB2lHQtsRgIObmftOuIL-GK64Zu_RLMn5EnDh6-AxNG8gCjTW2QLqBcevTHwY-EGkRhVOG8FGuBoZ0lSwlF_Taaov_wlJvFHfapckLEFQVqgFUOuPp33EttHIAcdXx6aDoEK7JU0lXJ6wryZjvoTaakXz-UqfMxPM8J-Y82v7vcDJk1B3id5FS0UYe1bOmbRuU69EOJF2e9ENsBbVimY7GzNAJ9tZ_z9TRJSP6YTQQzyR_7mSrWkGcuGPDAf4DzBji_7wbr9GJG6kTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : هر کسی میخواد برقش قطع نشه میتونه از بورس برق با قیمت آزاد خریداری کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21614" target="_blank">📅 23:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21613">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">محسن کج بند رضایی، دبیر شورای امنیت ملی، ادعای وجود توطئه ایران برای ترور پسر دونالد ترامپ را «دروغی بزرگ» دانست و گفت این ادعا ساخته بنیامین نتانیاهو برای فریب و ترساندن رئیس‌جمهور آمریکا است. او مدعی شد نتانیاهو با انتشار گزارش‌های جعلی درباره «توطئه ترور ترامپ» او را ترسانده و بر تصمیم‌گیری‌هایش اثر گذاشته است. رضایی افزود: «اگر تصمیمی بگیریم، هیچ‌چیز مانع اجرای آن نخواهد شد؛ اما این گزارش‌ها صرفاً یاوه‌گویی‌های نتانیاهو هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21613" target="_blank">📅 23:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21612">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دیوید بارنیا، رئیس پیشین سازمان اطلاعات خارجی اسرائیل «موساد»، می‌گوید جمهوری اسلامی در نهایت در اثر ترکیبی از فشارهای اقتصادی، عملیات علیه حکومت، و اعتراضات مردم ایران سقوط خواهد کرد، و تحریم‌ها به تنهایی برای رسیدن به این هدف کافی نیستند.
@WarRoom
🚨
🚨
🚨
حتما چنل رو دنبال کرده
🤣
🙌🏾</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21612" target="_blank">📅 22:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21610">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش پرتاب موشک زد کشتی از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21610" target="_blank">📅 21:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21609">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وال‌استریت ژورنال گزارش داده است که دونالد ترامپ با بازگشت به چارچوب اولیه توافق ژوئن با ایران مخالفت کرده و ترجیح می‌دهد با تشدید فشار اقتصادی و تحریم‌ها، تهران را به دادن امتیاز وادار کند. در مقابل، ایران تأکید دارد که بازگشایی تنگه هرمز باید بر اساس همان چارچوب ژوئن انجام شود؛ چارچوبی که شامل کاهش تحریم‌ها و محدود شدن فشارهای آمریکا بود. پاکستان، عمان و قطر نیز برای میانجیگری و نزدیک کردن دو طرف تلاش کرده‌اند، اما مذاکرات تاکنون پیشرفت چندانی نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21609" target="_blank">📅 21:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21608">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ به شوخی می‌گوید:
ما یک خلیج(مکزیک که شد آمریکا) داریم. ما یک دریاچه(انتاریو که شد آمریکا) داریم. حالا چیزی که نیاز داریم یک اقیانوس است.
بنابراین شاید مجبور شویم نام اقیانوس اطلس یا اقیانوس آرام را تغییر دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21608" target="_blank">📅 21:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21607">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرنگار: با کدام رهبران در مورد قطع روابط با ایران صحبت کرده‌اید؟
ترامپ: چیز زیادی برای صحبت وجود ندارد. ما نمی‌خواهیم با آنها صحبت کنیم. تنگه هرمز باز است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21607" target="_blank">📅 21:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21606">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ: ایران در وضعیت بسیار دشواری قرار دارد و نمی‌تواند حقوق سربازان خود را پرداخت کند.
اقداماتی که ما در مورد ایران انجام می‌دهیم، به این معنا نیست که ما از گزینه نظامی چشم‌پوشی کرده‌ایم.
ما نمی‌خواهیم با ایران صحبت کنیم و قصد نداریم جلسه‌ای با آن برگزار کنیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21606" target="_blank">📅 21:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21605">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شرکت روکِتسان ترکیه موشک کروز «چاکیر» را با موفقیت از یک پرتابگر زمینی آزمایش کرد
. این آزمایش نشان داد چاکیر علاوه بر پهپاد و دیگر سکوها، قابلیت شلیک از خودروهای زمینی را نیز دارد و می‌تواند اهداف زمینی و دریایی را با جستجوگر تصویربرداری مادون‌قرمز هدف قرار دهد. برد این موشک بیش از ۱۵۰ کیلومتر اعلام شده است.
جنرال یاشار گولر، وزیر دفاع ملی ترکیه،
نیز درباره تسلیحات جدید روکِتسان گفته است: «ما این سلاح‌ها را عمدتاً برای بازدارندگی می‌خواهیم، اما اگر استفاده از آنها لازم باشد، ترکیه بدون تردید از آنها استفاده خواهد کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21605" target="_blank">📅 21:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21604">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: هیچ نگرانی‌ای از حمله روسیه به ناتو ندارم
دونالد ترامپ در گفت‌وگو با آکسیوس گفت که «اصلاً نگران» حمله احتمالی روسیه به کشورهای عضو ناتو نیست و تأکید کرد: «هیچ مشکلی وجود ندارد.» او همچنین گزارش‌ها درباره سفر محرمانه جان رتکلیف، رئیس سیا، به مسکو برای هشدار به روسیه درباره حمله به اعضای ناتو را رد کرد و گفت این سفر «یک کار معمول» بوده و «هیچ پیامی در کار نبوده و هیچ چیز غیرعادی‌ای» رخ نداده است. با این حال، گزارش‌هایی از جمله گزارش وال‌استریت ژورنال و CBS مدعی‌اند که رتکلیف در مسکو به روسیه درباره حمله به ناتو هشدار داده است؛ موضوعی که تاکنون از سوی مقام‌های آمریکایی یا روسی به‌طور رسمی تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/21604" target="_blank">📅 20:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21603">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رئیس سابق موساد اسرائیل:
اجتناب از یک جنگ دیگر با ایران غیرممکن است
@WarRoom</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/21603" target="_blank">📅 20:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21602">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏ انفجار در اربیل عراق , منابع عراقی از حملات پهپادی به گروه های کورد در منطقه سوران در اربیل خبر دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/21602" target="_blank">📅 20:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21601">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjUtJG-ynRZWNH8XCmmLwCjNuedyWZ820VwcosvebBY7Ic7QerQAafKsEBcu2IcG1VFzTNHEZevmjXkdw8g3LK4ZTwFDBNOxi9XjzSkCKOp-nY6UBTEkfuhBGHEmevdxzqj8AgkFCMCvnzTSk6V8nT63STqUjyJTrwEbB7UgfKKJK42GqNJqtu5MbqTL7og_ihi-fmuJ586h0GRc9mi5IYMjA6gc-hJd9uRTpIygRPZG2KNO1GJiwiycmA-OUykkPjNIf1rzKU-gpC61Bxt6ZbxJLByZxbsidqQC_-YMCu7dnsOCrhAe6GbeGYRvvwlXlISQ0b3J7FNxvxf17jiIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امبر اولر، ۴۱ ساله و دختر شایسته میشیگان، امشب در مسابقه میس آمریکا ۲۰۲۶ در میامی روی صحنه می‌رود. اما تنها پنج سال پیش حدود ۱۳۶ کیلوگرم وزن داشت و پزشکش به او هشدار داده بود که در مسیر یک «مرگ زودهنگام» قرار دارد. پس از این هشدار و تجربه‌ای تحقیرآمیز در یک پارک ترامپولین، تصمیم گرفت زندگی‌اش را تغییر دهد. او طی بیش از سه سال با رژیم غذایی و ورزش حدود ۱۷۰ پوند، معادل ۷۷ کیلوگرم، وزن کم کرد و در سال ۲۰۲۴ وارد دنیای مسابقات زیبایی شد. اولر که مادر سه فرزند است، امسال به‌عنوان میس میشیگان آمریکا انتخاب شد و اکنون در میان ۵۱ شرکت‌کننده میس آمریکا ۲۰۲۶ قرار دارد؛ و در ۴۱ سالگی مسن‌ترین شرکت‌کننده این دوره است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21601" target="_blank">📅 19:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21600">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مقام آمریکایی به فاکس نیوز:
توافق ایران و عمان برای ما اهمیتی ندارد؛ فشار اقتصادی را ادامه خواهیم داد و مذاکره‌ای با ایران نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/21600" target="_blank">📅 19:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21599">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزیر انرژی آمریکا: به ایرانی‌ها گفتیم می‌توانند با همکاری با ما، فقط برای تولید برق انرژی هسته‌ای داشته باشند
@WarRoom</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/21599" target="_blank">📅 18:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21598">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ارتش اسرائیل: دیروز، یک فرمانده از شاخه نظامی حماس را در حمله به منطقه خان یونس به هلاکت رساندیم.
همکنون نیز ارتش اسرائیل در حال حملات هوایی به جنوب لبنان می باشد
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21598" target="_blank">📅 18:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21597">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKTLo2X4W3WFbp_zU3OjmqLSKZ4cxNSDG-8cbn-09GNVpRCVS7l8j_AhdQy3eeirQD5T8YqJXRyiSUyVuEmjxcWeSZDqAB3pLvjqKSPNB7e2O0H7BDwWezn59LAdB7NVj2KtBLUF3JEUFUfth7FpRolQPRqmwVjHy6vy1AVGGzWOo8F1-yXME96865uSoWHWq_JXWujJRcmu4jPoo8b2n45-zmhaDjg1LEYRs4gNYL6Ro2sNhZ7sfrVY_3EGxl2fRVQw3UYG3ABP6eNnDYK0JI9N_Y96B73Do2O7jh_auTfKGZwsNoYYLrU7-biknwVjAXcqRM-O4rFS16fjR6dscA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیماهای جنگ الکترونیک E/A 18G نیروی دریایی ایالات متحده در حالی که ایالات متحده همچنان به اعمال محاصره علیه ایران ادامه می‌دهد، بر فراز آسمان خاورمیانه گشت‌زنی می‌کنند. تا ۲۷ آگوست، نیروهای سنتکام ۷۵ کشتی تجاری را تغییر مسیر داده، ۳ کشتی را از کار انداخته و ۲ کشتی را توقیف کرده‌اند تا از رعایت مقررات اطمینان حاصل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21597" target="_blank">📅 18:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21596">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21fec76a7.mp4?token=Ooa7A3bc518t25PBHDQFGG_qDbepllQpi2TQbmtjs6AXhMZSxrj7FN3bH0SRbZ4LBqgy8b24JgPsGSdKg2cFCopbEZmCM5NO-jWtl8nyoK9NAResXR2ihOrPRHHEp-rN6nOJHSEPs1u8DMeYS_98SYx5ZzQuY-ODmNedZcN4S-exFA6VbbqOPdIjYZI54Sgp7AUbpFgKAZSo1gE8OwB5Feq_4NGQ-pZVM93IvXJyq5ulL8Qoy1mqh35e3LPIedYLvDQ1CMd6bhln9pO1OoYSnED_RvC2VRFM2PTkqxG-l7FnrNNtJD8z5Aa_5y1Ygr_i1jntGKdHxmAdclteUaPd2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21fec76a7.mp4?token=Ooa7A3bc518t25PBHDQFGG_qDbepllQpi2TQbmtjs6AXhMZSxrj7FN3bH0SRbZ4LBqgy8b24JgPsGSdKg2cFCopbEZmCM5NO-jWtl8nyoK9NAResXR2ihOrPRHHEp-rN6nOJHSEPs1u8DMeYS_98SYx5ZzQuY-ODmNedZcN4S-exFA6VbbqOPdIjYZI54Sgp7AUbpFgKAZSo1gE8OwB5Feq_4NGQ-pZVM93IvXJyq5ulL8Qoy1mqh35e3LPIedYLvDQ1CMd6bhln9pO1OoYSnED_RvC2VRFM2PTkqxG-l7FnrNNtJD8z5Aa_5y1Ygr_i1jntGKdHxmAdclteUaPd2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن نامجو در ویدئویی از پیش ضبط شده مدعی شد که هنگام پخش این ویدیو او در ایران یا در پرواز ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21596" target="_blank">📅 17:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21595">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏یسرائیل کاتس، وزیر دفاع اسرائیل، در جریان ارزیابی امنیتی با ارتش اعلام کرد: «مهلتی که تعیین کرده بودیم به پایان رسیده است. از این پس هرگونه پرتاب بالن یا بادبادک از غزه به سوی شهرک‌های جنوب اسرائیل با پاسخ سخت روبه‌رو خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/21595" target="_blank">📅 17:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21594">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">معاون وزیر نفت ایران: حدود ۴۰ درصد از ظرفیت آسیب‌دیده میدان گازی پارس جنوبی به تولید بازگشته است
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21594" target="_blank">📅 16:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21593">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">@WarRoom
losing my religion</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21593" target="_blank">📅 16:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21592">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وال استریت ژورنال به نقل از منابع آگاه گزارش داد که هدف از سفر جان راتکلیف، رئیس سازمان سیا، به مسکو در روز سه‌شنبه، هشدار دادن به روسیه  بود که از حمله به ناتو و کمک به ایران خودداری کند. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21592" target="_blank">📅 15:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21591">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b30ac12425.mp4?token=b52OsEjTWkLa8Q6t51Laka9GEgCg4NesN7DCr5UMdNii6FSqkPgFO3EEi6TcCQUcMwEE6wxIr_RNHuAwaPqCnbW3B4PgAt5RTsSM0-CyUtzyaVmDsOMLBjbHPdgnij_g9rgWrYaYBf3bbPSl7WsrN9GheMFQN9hLbjbJs0WOTt9oSh7m86jSKhPndadHba6iw8DQpGHgb4zqBb8z0qUFQ4mbb9i2Me1w3GG0e-9dK6Iq8qmxtDfPqnDcbudPWHvNlnEz0-L5DFrdBHKBe9j9PhjCNyd_ypmGt9kCtIPlfq8frI0MP2n1YqaWh5vrp-vLjC7keJfqwTFojQf_phGR-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b30ac12425.mp4?token=b52OsEjTWkLa8Q6t51Laka9GEgCg4NesN7DCr5UMdNii6FSqkPgFO3EEi6TcCQUcMwEE6wxIr_RNHuAwaPqCnbW3B4PgAt5RTsSM0-CyUtzyaVmDsOMLBjbHPdgnij_g9rgWrYaYBf3bbPSl7WsrN9GheMFQN9hLbjbJs0WOTt9oSh7m86jSKhPndadHba6iw8DQpGHgb4zqBb8z0qUFQ4mbb9i2Me1w3GG0e-9dK6Iq8qmxtDfPqnDcbudPWHvNlnEz0-L5DFrdBHKBe9j9PhjCNyd_ypmGt9kCtIPlfq8frI0MP2n1YqaWh5vrp-vLjC7keJfqwTFojQf_phGR-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21591" target="_blank">📅 15:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21590">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شیخ محمد بن عبدالرحمن آل ثانی، نخست وزیر و وزیر امور خارجه قطر، امروز در تهران با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، دیدار و گفتگو کرد
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21590" target="_blank">📅 15:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21589">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آتلانتیک : کاخ سفید به‌جای تشدید عملیات نظامی، به سمت تحریم‌ها و فشار اقتصادی بیشتر علیه ایران رفته تا هم فشار بر تهران حفظ شود و هم جنگ به موضوع اصلی انتخابات میان‌دوره‌ای تبدیل نشود.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21589" target="_blank">📅 14:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21588">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">روزنامه نیویورک‌تایمز گزارش داده است که عربستان سعودی در پی هفته‌ها حمله حوثی‌ها به اهداف سعودی، خود را برای احتمال آغاز دور تازه‌ای از جنگ در یمن آماده می‌کند. بر اساس این گزارش، حملات متقابل میان حوثی‌ها و نیروهای مورد حمایت عربستان شدت گرفته و خطر تبدیل‌شدن تنش‌ها به یک درگیری تمام‌عیار افزایش یافته است. ریاض در حال تقویت مواضع دفاعی و نیروهای یمنی متحد خود است و در صورت ادامه حملات، احتمال اقدام نظامی گسترده‌تر علیه حوثی‌ها وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21588" target="_blank">📅 14:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21587">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZp5mDfmNoa39RYkS6kTu4-RX0isaBD-UPEnAuT8EaZCZtC0HTqbLS8KsZ7Rj1nHC_sf97gIHlpQMt89TPS6b4HBcG_JYwT2ibHjjc_dp08UJe_8-C5G9r-oSoLQpe3Lqdorb-W2Z4NJKPz88L2LAeDrjpi7vOh-LWj6wIQhsw2gJyTwkZ4E7i7xsr7cWlxbZUS5XuTkgU7myzaVv9sm1J8xofZfPAUtvmONnhMRZSmVe9Iu5FvBEaFkdE8zxk54YEHi1TqzzBh02Krfw9a5VgTZ3cgKbXMTSxGpca9PgriSF8t4JUj4EUpNLm6YOXOWJCyOxLrfRLsScCE5m_XE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون گزارش آتشسوزی بزرگ در پادگان سنندج
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21587" target="_blank">📅 12:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21586">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">Bitcoin = 80,080$
🚀
@WarRoom</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/21586" target="_blank">📅 12:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21585">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرنگار: آیا می‌توان گفت که در حال حاضر حملات نظامی علیه ایران متوقف شده‌اند؟  پیت هگست: نه. اگر لازم باشد از حملات نظامی استفاده کنیم، این کار را انجام خواهیم داد. اگر ایران آن‌قدر احمق باشد که زیاده‌روی کند یا با ارتش آمریکا درگیر شود، ما هر کاری را که لازم…</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21585" target="_blank">📅 12:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21584">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به گزارش MS NOW، یک ملوان ۱۹ ساله نیروی دریایی آمریکا از خدمه ناو هواپیمابر «آبراهام لینکلن» در ۳ اوت ۲۰۲۶ به دریا پرید؛ همسر ۱۹ ساله‌اش هم این اقدام را تلاشی برای خودکشی عنوان کرده است.
او پس از حدود یک ساعت در آب نجات یافت و حدود پنج روز در مرکز پزشکی نیروی دریایی سن‌دیگو تحت مراقبت بود. همسرش می‌گوید او پس از تولد دخترشان در فوریه، چند بار درخواست
مرخصی پدری
کرده بود که رد شد و پیش از حادثه نیز درباره وضعیت روحی خود با فرماندهی و کادر پزشکی ناو صحبت کرده بود. به گفته او، پس از حادثه مراقبت‌های سلامت روان محدودی دریافت کرد و پیش از نخستین جلسه درمانی، دستور بازگشت به خدمت گرفت. اکنون این ملوان با
اقدامات انضباطی نیروی دریایی
روبه‌روست و طبق اسناد اتهامی، به
تمارض (Malingering)
و
غیبت بدون اجازه
متهم شده است. نام او به دلیل حفظ حریم خصوصی منتشر نشده است. این زوج یک
پسر سه‌ساله و یک دختر نوزاد
دارند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21584" target="_blank">📅 12:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21583">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه ویس های دیروزم رو گوش کرده باشین ، خودتون صحبت های همه را میشنوید بعد تصمیم میگیرید به هر حال ،ما در راه شخص شخصه، فقط شخص خود شاهزاده ادامه میدیم و با اطراف کاری ‌نداریم و این بحث اینجا به پایان میرسد و تحقیق و تصمیم بیشتر با شما است
🙌🏾
اتحاد باید حفظ شود و رمز اصلی است همچنین انتقاد هم اگر محترمانه و درست بیان شود نیز باید شنیده و پاسخ داده شود
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/21583" target="_blank">📅 12:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21582">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ایرج مصداقی مشاور شاهزاده رضا پهلوی: علی کریمی یک آدم ابله بی شعوره که سوابق ننگینی داره و توی فوتبالم هر تیمی رفت اون تیم رو بهم ریخت. هیچ سابقه مبارزاتی هم نداره. حالا اومده ما رو تهدید میکنه. آخه مردک تو عددی هستی شاهزاده رو تهدید میکنی؟! چه غلطی میکنی…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21582" target="_blank">📅 12:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21581">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ایرج مصداقی مشاور شاهزاده رضا پهلوی:
علی کریمی یک آدم ابله بی شعوره که سوابق ننگینی داره و توی فوتبالم هر تیمی رفت اون تیم رو بهم ریخت. هیچ سابقه مبارزاتی هم نداره.
حالا اومده ما رو تهدید میکنه. آخه مردک تو عددی هستی شاهزاده رو تهدید میکنی؟! چه غلطی میکنی مثلا؟! داریوش که میبینی که بلایی سرش اومده تو انگشت کوچیکه اونم نیستی.
بهش گفتن جهان پهلوان باورش شده. اخه مردک کسی که دوتا لگد به توپ زده پهلوونه؟! همین مونده بود تو برای ما شاخ بشی. فکر میکنه چون فوتبالش خوب بوده سیاستم میفهمه. ما اصلا تو رو حساب نمیکنیم ابله.
اینا رو ارزش دادنی فکر میکنن خیلی بالا هستن آقای کریمی با تو یا بی تو فرقی نمیکنه زیاد حرف بزنی صداتو میبرن
@WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/21581" target="_blank">📅 11:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21580">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اتاق جنگ با یاشار : به نظر من علی کریمی باشرف است و جنگی ، ‌ابتدا باید با چهره خودش برگردد و این موضوع روشن شود ، افراد سمی دورش را عوض کند ، بعد بهترین فرد برای بخش جمع کردن کمک مالی برای مردم و کسانی که اعتصاب انجام میدهند باشد و این روند را مدیریت کند و از پتانسیل بالایش استفاده درست بشود باید در پست درست قرار بگیرد و بازی کند همچنین نیاز به همکاری بیشتر شاهزاده با ایشان هم هست و نباید ترد شود ، ولی باز میگم باید با چهره خودش برگردد اول
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/21580" target="_blank">📅 11:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21579">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">علی کریمی : ‏از اين لحظه به بعد؛ از هيچ شخص يا حزب سياسى حمايت نميكنم. در حد توانم به مبارزه‌ام عليه رژيم اشغالگر شيعه ادامه خواهم داد. این تصمیم من به منزله سنگ اندازی در راه مبارزه دیگر افراد با رژیم اشغالگر آخوندی نیست.به اميد آزادى ايران و مردم نازنينش
@WarRoom</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/21579" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21578">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یاسمین پهلوی : آدم‌هایی هستند که برای یک روز جنگیده‌اند، آنها خوبند. آدم‌هایی هستند که برای یک سال جنگیده‌اند، آنها بهترند. آدم‌هایی هستند که برای چندین سال جنگیده‌اند، آنها خیلی خوبند و آدم‌هایی هستند که تمام زندگیشان جنگیده‌اند، آنها اصیل‌ترین هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21578" target="_blank">📅 11:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21577">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تحلیل الجزیره : توافق زمانی شکل می‌گیرد که ایران و آمریکا به اصل «امتیاز در برابر امتیاز» برسند؛ یعنی هر دو طرف چیزی بدهند و در مقابل، چیزی مشخص به دست آورند.
در غیر این صورت با پافشاری مانند تکرار شکست‌ها و بن‌بست‌های مذاکرات قبلی ، احتمال جنگ وجود دارد
@WarRoom</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/21577" target="_blank">📅 11:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21576">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مدیرعامل شرکت ملی نفت : چندین پیمانکار در حال انجام عملیات بازسازی و نوسازی مخازن خارک هستند. بازسازی اسکله‌ها و مخازن و همچنین پروژه‌هایی که از قبل تعریف شده‌اند، بدون وقفه در حال انجام است و هیچ‌کدام از کارهای جاری متوقف نشده است. در حال حاضر برخی پروژه‌ها حدود ۲۰ و برخی حدود ۳۰ درصد پیشرفت دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/21576" target="_blank">📅 11:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21575">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFM0T6daqxDzjfU58npoPnG_f6ZPV9dC9PfqhgFBrRQNODMQk5Ki3oEY4d4OdpR800vFELwfvpgf5_qJwHZ-RyTZpFmKzgjk9ui5yG4HHcoPI5PADLP9sRUPFA3YO5BmlAIpG0kspdo5-GnSRtRRoPetprraJPpFrUFuNbu6KuybfmJFhJzTxn_AilB14OU6ClaNZ8R1eFITzmUTxQfriYCqMCs9ptkMts0Eh-_6Br6x5gCUhbys6OUVzhA0RtE2NS3SXrNSnStcMrypi1RWSMYMLMK_TMfHWm-UyfzXqN7-rkuC1IsgxsH6bAg6dB3FzKF9iryl77fTtmhMZ_5mBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : همین الان قلعه حسن خان بغل ساختمان مربوط به دانشگاه که در جنگ قبلی مورد هدف قرار گرفته بود
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/21575" target="_blank">📅 11:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21574">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سخنگوی کاخ سفید در واکنش به سفر وزیر خارجه قطر به ایران اعلام کرد که هیچ مذاکره‌ای با تهران در حال انجام یا برنامه‌ریزی‌شده نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/21574" target="_blank">📅 10:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21573">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a3060c7b.mp4?token=jNRRb33mK1yb_V5e6LmN2ft5Kyl6moWem-kPHM_y95mxcL5785QO6jxL89_6uUX6gc3dA-M1tfpsvJe9xkQUPQae4EbN3XvbyWwL3S235Pc-vbGIO8YAODcl3BEjBI6cW8E0LVKCFvvutFXAFgN0l_xrqbkOFjHNZGSqnUnggFK86zk2Ccoqu34FDPf5f7ewGXjNkVMxZq1v2DpqD_tVOhbD6eKPG4FNtfG4WvmGI-krgBgvC9X-bI2-p0jZU__lYdeFt7AvcESi4eXFVylCJ-kaIX_WEt_RK5Gwd-DUr08PpYWD4W2uofDYkwc8L9I6B4r_3YglZ6zzxn87QPwlFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a3060c7b.mp4?token=jNRRb33mK1yb_V5e6LmN2ft5Kyl6moWem-kPHM_y95mxcL5785QO6jxL89_6uUX6gc3dA-M1tfpsvJe9xkQUPQae4EbN3XvbyWwL3S235Pc-vbGIO8YAODcl3BEjBI6cW8E0LVKCFvvutFXAFgN0l_xrqbkOFjHNZGSqnUnggFK86zk2Ccoqu34FDPf5f7ewGXjNkVMxZq1v2DpqD_tVOhbD6eKPG4FNtfG4WvmGI-krgBgvC9X-bI2-p0jZU__lYdeFt7AvcESi4eXFVylCJ-kaIX_WEt_RK5Gwd-DUr08PpYWD4W2uofDYkwc8L9I6B4r_3YglZ6zzxn87QPwlFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بحران گازوئیل؛ صف‌های کیلومتری و سرگردانی رانندگان کامیون
‏گزارش‌ها از تشدید کمبود گازوئیل در جایگاه‌های سوخت و اختلال جدی در ناوگان ترابری جاده‌ای حکایت دارد؛ رانندگان کامیون در شماری از استان‌ها ناچارند برای دریافت سهمیه پایه سوخت ساعت‌ها و حتی روزها در صف‌های طولانی بمانند. کاهش سهمیه‌ها از سوی وزارت نفت رژیم جمهوری اسلامی، معیشت رانندگان و روند حمل و توزیع کالاهای اساسی را تحت فشار قرار داده و نگرانی‌ها درباره گسترش اختلال در حمل‌ونقل جاده‌ای را افزایش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/21573" target="_blank">📅 10:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21572">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مؤسسه نیروی دریایی آمریکا USNI : گزارش داده است که ناو هواپیمابر تئودور روزولت CVN71 و ناوگروه رزمی آن در هفته‌های آینده از سن‌دیگو حرکت کرده و برای استقراری بیش از هفت‌ماهه در خاورمیانه آماده می‌شوند. فرمانده ناو نیز خدمه را برای مأموریتی حدود هشت‌ماهه آماده کرده است. این ناوگروه قرار است به حوزه فرماندهی مرکزی آمریکا اعزام شده و جایگزین ناو «جورج واشنگتن» شود؛ اقدامی که در ادامه حضور طولانی‌مدت ناوهای هواپیمابر آمریکا در منطقه و هم‌زمان با ادامه درگیری با ایران انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21572" target="_blank">📅 09:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21571">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLbUmYJ5VwGn13sEAMbtm9vXLRs-zk_8SREfDykSuIfDQ6SHm8WHb_e-6aUbyCJnEKpFrJYTCrUdzK_Xd79OiYyyfwrIELY-RVnNzsvczKHKjtoV11HrH7w_uar-RcolRfAw8T_jtYdX3SrKIsEAlj3ZtEniMVbndCerRjfBkjywRCB81CHapdbPuqhsE4hHxlhp74QMTzHlLl7wXUowlA020NWXO4D06QIfHCDkwIDURnxAOqedocisvXpbsLEsvSWWDstCKwgzfLi_8FSOIgpu21_doO0DieFldZI0E9bvUiS8xhb479FLNbWcgWs78-wrhnEM6g2319EDpwMl2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات دریایی بریتانیا بامداد پنجشنبه گفت که یک نفتکش در آب‌های نزدیک منطقه «الخصاب» در شمال عمان، مورد اصابت یک پرتابه نامشخص قرار گرفته که باعث آتش‌سوزی در آن شد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21571" target="_blank">📅 09:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21570">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وال استریت ژورنال به نقل از منابع آگاه گزارش داد که هدف از سفر جان راتکلیف، رئیس سازمان سیا، به مسکو در روز سه‌شنبه، هشدار دادن به روسیه  بود که از حمله به ناتو و کمک به ایران خودداری کند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21570" target="_blank">📅 03:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21569">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_Bu34JQbv89YlYJUMrBMsbNQS5bBZixdyhb8_fNSXXONsDFPYYUgcLyWFKHTK4tuCycZG8lF-tSNosfOFbka_eY5QJS0qi1L_MYAiFvMN92I9p3WnQMRbqIg05Uv9Fv4arOKFzddW-shU4RIM2IJr3JYsOgHccGrq_HBBEPuRskuKX998tPWGbXscszTwIj7tZDZ04MtW7wt17YpkhWQtFhzhYPfA8y6q9HMkMSqPj1HlqeplBYgelyXzIe8mOexmWRQWQJHP_yqOFzk-8iKj3Zh6KLibdcPizPbhgvDDoHK8EeA5qzyiFYiMrgUO2aMnAK9ax4LNDxlHagm_TKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیونه خونست! صفحه اول روزنامه نوبنیاد امروز
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21569" target="_blank">📅 03:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21568">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در منطق دیکتاتور مردم دو دسته‌اند: آنهایی که باید گول بخورند و آنهایی که باید گلوله بخورند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21568" target="_blank">📅 01:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21567">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بلومبرگ: وزارت دادگستری آمریکا در حال احیای «دادگاه غنائم جنگی» است تا بتواند نفتکش‌های ایران را به‌عنوان غنیمت ارتش مصادره کند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21567" target="_blank">📅 00:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21566">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تنگه دعواااا شد
🚨
🚨
🚨
🚨
پرتاب چند موشک از سیریک و صدای انفجار از تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21566" target="_blank">📅 00:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21564">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21922cc89d.mp4?token=n3RDsZJhcjc8Np2vl93K2dYGkQskcBnLlsARCCV0xW4Dw94ifRvJjwy4MKNIx9SYPNNLj0Wf1u3PW6NXCZ0iOzcNb-N6GUsoa-cp3hngFDojKFlZBotY1dxsGNpidDavF6h1zQfVlzbzNvpA_QUt3KhtOVtY2XSd6kZQVU0nggCEIcb_Tns87sfe06hSRsO4emYA06rnL5NjcmiC6Q-s6K9C_TUa8Wnx54nCS4HIt8bdrwoQ_KjJJiR-pkot3bwLB1LHsl_ARHeNvlPNx4Qi-N4XnYSnuokRtQYOdJp3Nvl1SA7YyVPVaVVYkoIR_ZzS8cHG_l_QJnMLf36rXP1I05DgEC81M7h7liBfoOjA8SezVOGfN77VMIpnY7j-50Q4WSa9mQDvw7FVJZGGQVyyuHtDa7e9z__nhpsWYyXNpG_3vBIi5CpB5Xo3uZZTauV2bK3pxJOLZ0Bp0M-I0UUQfID11SBs8UZOrtaGEfnLCfpsYZp4zb8csmtHyAhQPPtTSWmoiK0-HPPQB_QY1Repsy9zjnVpPZ1pPuOtfWev_plMFne40pRmIBmj6rPHNJBIZwBeqtQ2THR4VRCNeWKsruNQKrY9QD8EJewTHA-kqfL_cGxG45doq658Uwx09PdgWHD1xXG3ldWQV30bx3VlQeW6VB8TMNS99uAH8aPREnE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21922cc89d.mp4?token=n3RDsZJhcjc8Np2vl93K2dYGkQskcBnLlsARCCV0xW4Dw94ifRvJjwy4MKNIx9SYPNNLj0Wf1u3PW6NXCZ0iOzcNb-N6GUsoa-cp3hngFDojKFlZBotY1dxsGNpidDavF6h1zQfVlzbzNvpA_QUt3KhtOVtY2XSd6kZQVU0nggCEIcb_Tns87sfe06hSRsO4emYA06rnL5NjcmiC6Q-s6K9C_TUa8Wnx54nCS4HIt8bdrwoQ_KjJJiR-pkot3bwLB1LHsl_ARHeNvlPNx4Qi-N4XnYSnuokRtQYOdJp3Nvl1SA7YyVPVaVVYkoIR_ZzS8cHG_l_QJnMLf36rXP1I05DgEC81M7h7liBfoOjA8SezVOGfN77VMIpnY7j-50Q4WSa9mQDvw7FVJZGGQVyyuHtDa7e9z__nhpsWYyXNpG_3vBIi5CpB5Xo3uZZTauV2bK3pxJOLZ0Bp0M-I0UUQfID11SBs8UZOrtaGEfnLCfpsYZp4zb8csmtHyAhQPPtTSWmoiK0-HPPQB_QY1Repsy9zjnVpPZ1pPuOtfWev_plMFne40pRmIBmj6rPHNJBIZwBeqtQ2THR4VRCNeWKsruNQKrY9QD8EJewTHA-kqfL_cGxG45doq658Uwx09PdgWHD1xXG3ldWQV30bx3VlQeW6VB8TMNS99uAH8aPREnE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏وزیر انرژی ایالات متحده، رایت: در صورت شکست بازرسی‌ها و مذاکرات آژانس بین‌المللی انرژی اتمی، زیرساخت‌های هسته‌ای و صنعتی در ایران به صورت نظامی نابود خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21564" target="_blank">📅 00:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21563">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23dd6e08b2.mp4?token=RvnDMsJh60e4g-Qkcwikpc9ZRy_G_W4eA_yg-mFPg3VvUPk0EV7HpeStRLfpvAn0XiISd8vFWlQhSwZ0JHOjREU1JiuR2PRMOmPBpVEF-fIn-eAauY9GU5pSnoMLGjKdVapiYB2fLIVxS8ugVgrnCkpdD1S3HGHKlPjSjaFyBJvPaE1yXcmsBS3ABtCTkF9viDVy6F1eyCM8sKpPgK-rCKLMbvZ5yUuIHvag6k0VafJtXM9S0xPY33MuwFSsx3PuEGZZP7p1chcylSHItQgtfKyVdACtGV4L3TNWd4yHK173PAJkNwZlH7bZmhW34set2UchlBWcP16ly8SpWYuWwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23dd6e08b2.mp4?token=RvnDMsJh60e4g-Qkcwikpc9ZRy_G_W4eA_yg-mFPg3VvUPk0EV7HpeStRLfpvAn0XiISd8vFWlQhSwZ0JHOjREU1JiuR2PRMOmPBpVEF-fIn-eAauY9GU5pSnoMLGjKdVapiYB2fLIVxS8ugVgrnCkpdD1S3HGHKlPjSjaFyBJvPaE1yXcmsBS3ABtCTkF9viDVy6F1eyCM8sKpPgK-rCKLMbvZ5yUuIHvag6k0VafJtXM9S0xPY33MuwFSsx3PuEGZZP7p1chcylSHItQgtfKyVdACtGV4L3TNWd4yHK173PAJkNwZlH7bZmhW34set2UchlBWcP16ly8SpWYuWwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : سگ‌های نظامی در کنار نیروهای آمریکایی در سراسر خاورمیانه خدمت می‌کنند و ماموریت‌های حیاتی متنوعی را انجام می‌دهند. این جنگجویان چهارپا، هم‌تیمی‌های قابل اعتمادی در کمک به محافظت از نیروهای نظامی آمریکایی در برابر تهدیدات هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21563" target="_blank">📅 00:00 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
