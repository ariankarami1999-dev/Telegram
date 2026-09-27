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
<img src="https://cdn4.telesco.pe/file/Wzhl-aKSZpAi4BFsU16T3sS3utwzg_OMZ6DIeStStyFK4sTG-DDpqVzE_t8Ztx5Zl40Ui3iHbRBWwX4W5I5yQ81TvcMW-Jmxny4XwB6lWCuDa3IrYt-V0t3cZX_4B3G2AK8eEi1XeR2xF4QD7_kBk2eAr-moeP5KDStIKiqRb933ZqZSIPNrLUX4JnG0D3BLCPCpj78FKOUsRWgK-GjJ3c8uJ6xmLDXKEl-Uk4mZPmih-kY8d5wcKZbkdw0ugP-H-_1k1gbKX55cjpa3zeP-u8Wu7lhRkqiMWjMwylf6T0pA3atrfnWQvLB_7NX5aG-n10UEZR2TPwiY7xMjRn3oqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 466K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 10:52:38</div>
<hr>

<div class="tg-post" id="msg-24307">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
تمام بانک‌های تجاری بزرگ در
امارات متحده عربی و ترکیه
انجام تراکنش‌های مالی با ایران را متوقف کرده‌اند. بسنت گفت فشارهای اقتصادی واشنگتن برای منزوی کردن ایران در حال نتیجه دادن است و آمریکا برای اجرای این سیاست با بیش از
۵۰ کشور
وارد رایزنی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/withyashar/24307" target="_blank">📅 10:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24306">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyjoNdHZK5N142iNk1Fxp3LSmT7lkkUDQu_FaLnm3uNGznvjpqFp38CoiJDUp5LvoUHAhfsyT-j7U7bHFRNzPjxvECW_ZpRRYufydw27uShNJkRwqHm26sH83g4J9oAPtHEKKHcDxEk8iT3_Um674GV3HcN9B-PQRisf7St1K_X8yBiDJkd6nYpMdR1bA-WTA7ZtDbua7zjSI0UzdvdijZlFaUqHiBDrZdRthDDbm24EGfzdaRbOmFadIhJmfbC2bUI8ji_n8NTW5CJge4HZZ1-qpPReKtBT8orItu8V8f0w74_GDEd7twEfjLl-mBf8xw2_E7TyKbjDQxlK7USWTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۳۰ دقیقه اخیر ۳ انفجار بسیار‌ سنگین خارگ
@WarRoom</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/withyashar/24306" target="_blank">📅 10:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24305">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تام کاتن، سناتور جمهوری خواه:
یک درگیری جدید با ایران در پیش است
@WarRoom</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/withyashar/24305" target="_blank">📅 10:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24304">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgZChXC8Ydja59fHWhw6WywmCEex9Il_oiwNAbVcVBNEDRAhnbfGJEI5eUCV9ZK0oDe7yvfFPpqZfy134RYq7D-KyWAm1Y8fCsSL6S_ndR3GK0jiQcHfhChah8eDi7_wsfequjVv3ldf4-gZq3hluV9-E18Q0AK8ms9h77ZP2O9SmfrnXdF73uHUbOn4yOG9SuCwuzv18hSwXP6YnckiFWIK0OC9o7aAtc2o3wA1i4L-po3aAOUyJso1kSrnbqyJFaY9SHEbFW6VlLOWb6JdSKhResl96k-7pbfCDX_3q3v6N2D_dwx5ZPUC7ssceuYNLWUv_NR-qx6Ww-kG_Lo1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس:
چین دو پاندا غول‌پیکر به نام‌های
«پینگ‌پینگ» (Ping Ping)
و
«فو شوانگ» (Fu Shuang)
را پس از دیدار شی جین‌پینگ و دونالد ترامپ به آمریکا فرستاده است. این دو پاندا بامداد یکشنبه ۲۷ سپتامبر از فرودگاه چنگدو با یک پرواز چارتر عازم
باغ‌وحش آتلانتا
شدند و قرار است حدود
۱۰ سال
در آمریکا بمانند. این اقدام بخشی از چیزی است که چین از آن به‌عنوان
«دیپلماسی پاندا»
استفاده می‌کند؛ یعنی اعزام یا امانت‌دادن پانداها به کشورهای دیگر به‌عنوان نمادی از روابط دوستانه و همکاری دیپلماتیک
@WarRoom</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/withyashar/24304" target="_blank">📅 10:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24303">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فاکس‌نیوز:
سخنگوی سپاه، سرتیپ حسین محبی، اعلام کرده ایران تا زمانی که
هفت شرط تهران
برآورده نشود، به عملیات علیه آمریکا ادامه خواهد داد. از جمله شروط ایران، رفع محاصره دریایی بنادر و آزادسازی بخشی از دارایی‌های مسدودشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/withyashar/24303" target="_blank">📅 09:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24302">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رویترز:
عباس عراقچی اعلام کرد ایران در مذاکرات جدید درباره
برنامه هسته‌ای خود امتیازی نخواهد داد
و حقوق تهران از جمله غنی‌سازی اورانیوم و نگهداری اورانیوم غنی‌شده، قابل مذاکره نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/withyashar/24302" target="_blank">📅 09:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24301">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اتاق جنگ با یاشار:
برای بررسی روایت انتقال مجتبی خامنه‌ای، ابتدا باید به سه بیمارستانی نگاه کنیم که
در ۲۸ فوریه و شب اول مارس واقعاً آسیب دیدند: گاندی، مطهری و خاتم‌الانبیا.
۱-
بیمارستان گاندی در شب اول مارس، در جریان حمله به ساختمان‌های صداوسیما در نزدیکی آن، به‌شدت آسیب دید و بخش‌هایی از بیمارستان تخلیه شد؛ تصاویر و بررسی‌های مستقل محل اصابت و خسارت را مستند کرده‌اند.
۲-
بیمارستان مطهری نیز در همان موج حملات آسیب دید؛ این بیمارستان در کنار مقر پلیس تهران قرار دارد و تصاویر قبل و بعد از حمله، خسارت قابل‌توجه در اطراف و داخل بیمارستان را نشان می‌دهد.
۳-
بیمارستان خاتم‌الانبیا نیز در گزارش‌های همان روز به‌عنوان یکی از مراکز درمانی آسیب‌دیده ثبت شده است؛ گزارش هلال‌احمر ایران از حمله به محدوده اطراف خاتم‌الانبیا و مطهری خبر داده و بررسی CNN نیز خسارت به خاتم را مستند کرده است. بنابراین اگر روایت انتقال او به چند بیمارستان درست باشد، هنوز این احتمال وجود دارد که یکی از مراکز درمانی مورد استفاده او
یک مرکز نظامی یا حفاظت‌شده وابسته به سپاه، در مجاورت این بیمارستان ها
بوده باشد؛ اما این ارتباط هنوز اثبات نشده است. همچنین بیمارستان سینا در گزارش‌های مربوط به مسیر درمان او مطرح شده، ولی طبق همان روایت،
پس از حمله اولیه
محل انتقال او بوده و نباید آن را با بیمارستان‌های آسیب‌دیده در حملات ۲۸ فوریه و شب اول مارس یکی دانست.
در نتیجه، سه بیمارستان آسیب‌دیده را می‌شناسیم، اما فعلاً هیچ مدرک مستقلی نداریم که یکی یا همه آن‌ها همان بیمارستانهایی باشد که مجتبی در آن بستری شده و سپس زیر آوار مانده.
@WarRoom</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/24301" target="_blank">📅 09:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24300">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">در جنگ ۴۰ روز قرارگاه سپاه در محدوده چهارراه آبسردار با اینکه کاملا در منطقه مسکونی بود با این دقت شخم زده شد
@WarRoom</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/24300" target="_blank">📅 09:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24299">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏افشاگری محسن حیدری آل کثیر عضو خبرگان رهبری در مصاحبه با تلویزیون قطری العربی تایید کرد که مجتبی خامنه‌ای همراه پدرش بود و زخمی شد و پس از زخمی شدن پی در پی به سه بیمارستان در تهران منتقل شد که هر سه هدف قرار گرفته شد و در بیمارستان سوم از زیر آورها او را…</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24299" target="_blank">📅 02:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24298">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اتاق جنگ با یاشار: پیامی که در برخی کانال‌ها درباره «تحریم جدید ایران توسط گوگل» منتشر شده، نادرست و گمراه‌کننده است. این پیام عمدتاً به ارور Too many accounts created مربوط می‌شود؛ یعنی وقتی در یک دستگاه یا از یک مسیر اتصال، تعداد زیادی حساب جیمیل ساخته شود،…</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24298" target="_blank">📅 01:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24297">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خبرنگار اسرائیل
ی
: حملات امشب سپاه پاسداران به کشتی‌ها در تنگه هرمز گسترده و کم‌سابقه بوده است.
گزارش‌های دریایی از افزایش حملات و کاهش شدید تردد کشتی‌های تجاری در تنگه هرمز خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24297" target="_blank">📅 01:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24296">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اتاق جنگ با یاشار:
پیامی که در برخی کانال‌ها درباره «تحریم جدید ایران توسط گوگل» منتشر شده،
نادرست و گمراه‌کننده است
. این پیام عمدتاً به ارور
Too many accounts created
مربوط می‌شود؛ یعنی وقتی در یک دستگاه یا از یک مسیر اتصال، تعداد زیادی حساب جیمیل ساخته شود، گوگل برای جلوگیری از ساخت انبوه حساب‌ها ممکن است از کاربر بخواهد
شماره تلفن خود را برای تأیید وارد کند
. این موضوع می‌تواند با
استفاده مکرر از VPN یا IPهای مشترک VPN
هم مرتبط باشد؛ به‌خصوص اگر از همان IP تعداد زیادی حساب ساخته یا وریفای شده باشد.
پیش‌شماره ایران (+98) نیز در حال حاضر برای وریفای حساب گوگل قابل استفاده است.
بنابراین این پیام به معنی تحریم یا مسدودشدن جدید دسترسی کاربران ایرانی به گوگل نیست؛ ضمن اینکه محدودیت‌های گوگل علیه ایران موضوع جدیدی نیست و سال‌هاست وجود دارد.
اقدام جداگانه امروز گوگل علیه حدود ۶۰ حساب مرتبط با صداوسیما
نیز به دلیل فعالیت‌هایی که گوگل آنها را مرتبط با
فیشینگ سیاسی و پنهان‌کردن هویت
عنوان کرده، انجام شده و ارتباطی با مسدودشدن عمومی کاربران ایرانی ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24296" target="_blank">📅 01:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24295">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پست جدید ترامپ در تروث : ترامپ : این رژیم به‌زودی خواهد فهمید که هیچ‌کس نباید قدرت و توان ایالات متحده را به چالش بکشد.  گوینده : او بار دیگر به جهان یادآوری کرد، همان‌طور که بارها و بارها گفته است، که آمریکایی بودن معنایی شکست‌ناپذیر دارد. اگر آمریکایی‌ها…</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24295" target="_blank">📅 00:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24294">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">پست جدید ترامپ در تروث : ترامپ :
این رژیم به‌زودی خواهد فهمید که هیچ‌کس نباید قدرت و توان ایالات متحده را به چالش بکشد.
گوینده : او بار دیگر به جهان یادآوری کرد، همان‌طور که بارها و بارها گفته است، که آمریکایی بودن معنایی شکست‌ناپذیر دارد. اگر آمریکایی‌ها را بکشید، اگر در هر نقطه‌ای از زمین آمریکایی‌ها را تهدید کنید،
ما بدون عذرخواهی و بدون تردید به سراغتان خواهیم آمد و شما را خواهیم کشت.
ما این جنگ را آغاز نکردیم، اما تحت ریاست‌جمهوری ترامپ،
آن را به پایان خواهیم رساند.
جنگ آنها علیه آمریکایی‌ها، به انتقام ما تبدیل شده است.
ترامپ :
ای مردم سربلند ایران، ساعت آزادی شما فرا رسیده است.
زیرا ما آماده‌ایم دولت شما را به دست بگیریم.
این حکومت متعلق به شما خواهد بود که آن را به دست بگیرید
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24294" target="_blank">📅 00:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24293">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرگزاری محلی هرمزگان:
هم اکنون فعالیت‌های نظامی در امتداد سواحل جنوبی هرمزگان، به همراه تعداد و شدت انفجارهای امشب،
در چندین ماه گذشته،
بی‌سابقه است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24293" target="_blank">📅 00:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24292">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اتاق جنگ با یاشار ، وضعیت قرمز : ۹ سوخترسان در خلیج فارس و یک دسته سوخترسان با مالکیت نامشخص به سمت منطقه ! (دسته دوم ممکنه برای جنگ یمن باشن) ولی موقعبت الان کاملا جنگیه ! @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24292" target="_blank">📅 00:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24291">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دیدبان اتاق جنگ : پدافند شهید رودکی قشم زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24291" target="_blank">📅 00:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24290">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بابک زنجانی:جلوی استارلینک رو میگیریم، تکنولوژی در برابر تکنولوژیتون داریم
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24290" target="_blank">📅 00:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24289">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inE6iC8bceSqVVYOZ0a4tp669Vd0ee9wz2WBHRGDKBEaVwFpY87QStHPkbpbYJh6GM7rdA_NyarHnMzUdi3T1eqfRH6lRaRpHcYpzWdnjxu0xCNP6In2FJCJ6yQH2vlYJDe-gcOfZBIod48XelgAeoRpQjW01wCQDUupmaIpIEJd7WT6FiAL5xk1vYdzJVSg8VKG8dYx_P9w7VGN1cvyo2yKOKq8N-WJ86RNo2rEelpALXU3-nKK5KQf32O3UFDEH1R8r0Rt2t_b5DWKM6htZSfWWlv-f0DjAeeVV8PMU4RAReCbvhhQqJfyAADXjjnVl03cmS7w42Fu7x4RHa6GVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست: دادستانی ایران پس از انتشار ویدیویی از اجرای نمایش «تهران پاریس تهران»، علیه گروه تئاتر پرونده کیفری تشکیل داد. ماجرا مربوط به صحنه‌ای است که در آن فاطمه مسعودی‌فر، بازیگر زن نمایش، سرش را به سینه مهرداد صدیقیان تکیه می‌دهد و او دستش را روی سر این بازیگر می‌گذارد. مقام‌های قضایی این رفتار را نقض «هنجارهای اجتماعی» دانسته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24289" target="_blank">📅 00:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24288">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سیریک زمین سنگین لرزید دیدبان اتاق جنگ میگه ممکنه زده باشن حتی
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24288" target="_blank">📅 00:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24287">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزیر خارجه کانادا : ایران تهدید اصلی است و نباید به سلاح هسته‌ای دست یابد. هرگونه حمله ایران به کشتیرانی در تنگه هرمز را محکوم می‌کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24287" target="_blank">📅 00:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24286">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سخنگوی نیروهای مسلح ایران:
موشک‌ها و پهپادهای ایرانی پیشرفته‌تر و قدرتمندتر شده‌اند. این بار، ما یک غافلگیری برای دشمن داریم و در برابر هرگونه تجاوز احتمالی، از فناوری‌های نظامی جدید استفاده خواهیم کرد.
هر کشتی‌ای که از تنگه هرمز خارج از مسیری که ایران تعیین می‌کند، عبور کند، امنیت نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24286" target="_blank">📅 00:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24285">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">۳ پرتاب از سیریک  @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24285" target="_blank">📅 00:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24284">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۳ پرتاب از سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24284" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24283">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">موج پیغام های  شما از گزارش عجیب ایران اینرنشنال توسط مجری افغان این شبکه مرضیه حسینی که مجاهدین خلق رو مردم ایران میدونه و پرچم جعلی اونها رو پرچم شیرو خورشید عنوان میکنه ! و پروموتشون میکنه ! @WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24283" target="_blank">📅 23:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24282">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24282" target="_blank">📅 23:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24281">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏افشاگری محسن حیدری آل کثیر عضو خبرگان رهبری در مصاحبه با تلویزیون قطری العربی تایید کرد که
مجتبی خامنه‌ای همراه پدرش بود و زخمی شد و پس از زخمی شدن پی در پی به سه بیمارستان در تهران منتقل شد که هر سه هدف قرار گرفته شد و در بیمارستان سوم از زیر آورها او را بیرون کشیدند.
‏محسن حیدری آل کثیر نماینده منتصب این دوره مجلس خبرگان از خوزستان است که در گذشته مسئول بخش عربی سپاه تروریستی پاسداران در خوزستان بوده است.
‏افشای این اطلاعات در حالی که پزشکیان در مصاحبه اخیرش در آمریکا مدعی سلامت کامل مجتبی خامنه‌ای شده بسیار قابل توجه است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24281" target="_blank">📅 23:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24280">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ
:امروز روز بزرگی برای کارگران صنعت خودروسازی آمریکا و خریداران خودرو است! من به تازگی استانداردهای جدید بهره‌وری سوخت را تصویب کرده‌ام که دستورالعمل احمقانه مربوط به خودروهای برقی که توسط جو بایدن و پیټ بوتجج مطرح شده بود، را لغو می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24280" target="_blank">📅 23:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24279">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24279" target="_blank">📅 23:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24278">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromK2</strong></div>
<div class="tg-text">اونهمه سوخت رسان تو یه خط نمیتونه چتر باز باشن
یا پوششی برای ب۲ ها
اف ۲۲ها</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24278" target="_blank">📅 23:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24277">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">صدای‌انفجار تنگه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24277" target="_blank">📅 22:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24276">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پزشکیان: اجازه نمی‌دهیم تنگه هرمز برای جابه‌جایی سلاح‌های آمریکا باز باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24276" target="_blank">📅 22:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24275">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">صدای‌انفجار تنگه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24275" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24274">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH0V-6L-B_w74KNrcV0zxmcB42SmDcG6CeN2vD--tJUzWSOIws8B5kxnfx3dsdmLe4QLlNlzegKB5n4cIUDgr1iIZq3O6w8xvd4jNvKuN5KbKHsJ3dXnCkzg4K2vCnv2FjaOPNOVVU_8dZJu50QMVAPVjiTVJETecU_xV6gf0gLmJnqRbS1e3uXgzDj0ewxG4mL130LzX3EGlhvCMU_mEHLlkt9EB5EMaseg-p-QNulyF1gnA0C5xpD3QCUxFKoB5OatmX2QDBUjsShpx6wsE4PgKKDph6hf_FL5D5kdLqqDIqKJg7bYdbXJloHP8_50SO2JPTO7rymuSd_7DN4smg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث
: ایران نمی‌تونه سلاح هسته‌ای داشته باشه
@WarRoom
یاشار : پست باحروف بزرگ در چت و نوشته اینترنتی به معنی با صدای بلند و پرخاشگرانه گفتن اون جمله است</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24274" target="_blank">📅 22:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24273">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiMhN1MhTTw2PjpA9MKbXXPQyh-jb6q8Ki7dVAIZQlDSfcxZr7PAQEv7qFsRPVGFVilaSyLu6UkGGIA0CvhLXyRV1amyVx2avyfH35BLw13SuWppYZiaSvnkVSIxEGLc9eY9smMlg2C7KRZKqiNeLdb_ZZv1sDZZdmvqcBGLqYTmiqLQ-IttMDxxnREmUsI58Jcn6eFmDHq3yw4UGjC5GoYwwa2A7jwh2KArQHFdMUfKaH3HD4RmW1JZ3--Jcas7dbTy7nd1-p486yGyMOeHXNCQiFH5qzBUWetEA8TMVEo5HX_z_UYJyC1XwAz4hXBPoynbng2-DkebVaPN1RUUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار ، وضعیت قرمز : ۹ سوخترسان در خلیج فارس و یک دسته سوخترسان با مالکیت نامشخص به سمت منطقه ! (دسته دوم ممکنه برای جنگ یمن باشن) ولی موقعبت الان کاملا جنگیه !
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24273" target="_blank">📅 22:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24272">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پزشکیان لشش رو آورد
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24272" target="_blank">📅 22:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24271">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">جنرال جک کین به فاکس نیوز:؛عملیات نظامی علیه ایران اجتناب ناپذیر است. با شکست مذاکرات جاری میان ایران و آمریکا، مسیری که در پیش داریم شامل ادامه محاصره دریایی و هوایی و عملیات های نظامی گسترده از سوی اسرائیل و آمریکا علیه ایران است @WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24271" target="_blank">📅 22:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24270">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها می‌خواهند تنگه هرمز را فوراً باز کنند. می‌دانید چرا؟ چون دارند از پا درمی‌آیند؛ می‌دانید چرا؟ چون هیچ پولی وارد کشورشان نمی‌شود. آن‌ها پولشان را از تنگه هرمز به دست می‌آورند، بنابراین خودشان خودشان را فریب دادند. آن‌ها گفتند: «بیایید…</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24270" target="_blank">📅 21:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24269">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جنرال جک کین به فاکس نیوز:؛عملیات نظامی علیه ایران اجتناب ناپذیر است.
با شکست مذاکرات جاری میان ایران و آمریکا، مسیری که در پیش داریم شامل ادامه محاصره دریایی و هوایی و عملیات های نظامی گسترده از سوی اسرائیل و آمریکا علیه ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24269" target="_blank">📅 21:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24268">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کانالi24  news: یک منبع امنیتی گفت که پس از رد پیشنهاد ایران از سوی رئیس‌جمهور ترامپ برای بازگشایی تنگه هرمز، ستاد مشترک ارتش آمریکا ارزیابی‌های خود درباره مسیر اقدام بعدی را از سر گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24268" target="_blank">📅 21:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24266">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guLRmXsBxOKZgRizk5o7sZ7BdqGutWKEzuzweEe6vm_C9lwUIIM3l5mgw-MVtJRJzVtpA06zg63dsG2gkdY9U6Q5v5x0kbRlm8g6HOECMo6bulE26HXppUDEpuMFWkZGEZTZiDHuLe-vXq15nKB0hoZTZaXz9zrVThsFilnea8aQyrmLmYCbvYQqvDwrE9VOLag8lph-2Udi06wLBYbeQ7gUIVkDnXFUkWsO6-10VnAM_ApcsMr-OMFkkME5IXXUdZUdF9qzt78yiqu3KMMF9n-2TTovXUERxY4eMC2UphzWeZwe-5Twkr2fzf2_tvbSwwV_CFFQuObbEP2CkD5AEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S994lg3wLFx6crPzvc-0CoreQ9ryqG71E9qFEihOfibRQWM0lc9shPtHShasaLqfCv78JKx5kprU1x1nT_dCGtBVIiaRe96eKJb1Gwg40GDx4EVFm_0p1jcw2pZbDkxhjLPKsXwjolX8oEmQZ2zl20bb5UMJeOJNYIY8yTHGNjQ50YeKyBoLRZLRkPNqTXk-iOC1TUQS7kBqU_RcHeABdPYNvzbX2iq3nz9BUoRQLTRRw1ezdhiFG2kspn-fH7H4uYl2ha3_czbMcy6y2ztpUoqKvzRPkg20ZB7y5OwDgJFLQaRwv6h4HtXL1BNhjuwPKLBmTtBvJ-WrKHnVh4XYRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مخزن سوخت یک جنگنده آمریکایی در ارتفاعات ایران پیدا شد: تصاویر منتشرشده از یک مخزن سوخت خارجی پیدا‌شده در ارتفاعات ایران، با توجه به صدا و جنس فلزی برای یک F-15E Strike Eagle است. چون F/A-18/EA-18G از فایبرگلاس استفاده می‌کنند ولی ساختار اصلی این مخزن از آلیاژهای…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24266" target="_blank">📅 21:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24265">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مایک پمپئو: رهبران ایران بی‌شرم‌ترین دروغگویان روی زمین هستند. ظاهراً آیت‌الله در سلامت کامل است و آن‌ها می‌گویند که به‌دنبال سلاح هسته‌ای نیستند. شگفت‌آور است که کسی تصور کند می‌توان در مذاکرات یا در هر موضوع دیگری به آن‌ها اعتماد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24265" target="_blank">📅 21:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24264">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">العربیه: ترامپ به تیم مذاکره‌کننده خود اعلام کرده است که تیم مذاکره‌کننده ایران تصمیم گیرنده نیستند و با آنها نمیتوان به توافقی رسید
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24264" target="_blank">📅 20:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24263">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اتاق جنگ با یاشار : شورای ملی ایرانیان آمریکا، معروف به نایاک (NIAC Action)، که از مهره‌های نفوذی جمهوری اسلامی در آمریکا محسوب می‌شود، از دونالد ترامپ در دادگاه فدرال شکایت کرده است. نایاک خواستار غیرقانونی اعلام شدن عملیات نظامی آمریکا علیه ایران به دلیل نبود مجوز کنگره شده است. در این پرونده نام نیما دیلمقانی، آلن بند(زنش ایرانیه عرزشیه) و پروین اسماعیلی‌زاده نیز به‌عنوان اعضای نایاک مطرح شده و جمال عبدی از چهره‌های اصلی سازمان در پیگیری پرونده است.
@WarRoom
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24263" target="_blank">📅 20:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24262">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wo-tSBUMY3uqZ8gwGCruz9FCzvDRNPBvE9YAWVKBZpWjkAqWpilGaMZEv6TWub7R1DvEcrm7lruzDj7xxtiq9Wq2MzI15Y4tTSSL5rrb4zZHgZ7ivOCvfmgYlPrfFppQa4diww3DuxhHqHKoXJlZkWmmsvdID_1KBCr3j7Rs70_b57R4kuEc1iA1JQWasNFtmRZsabJjbh9sXaZVd6gc5ZcpwvZgyo_w5Hmd2U5G94dLsHaHS5XoBBAZLt-lznGDx5CL0QeZi1yQkj7ZGiP02pFQO2AvBLVOuuN13HJPwBlCBPjyEIOVHwr7QosZED-sHVfWDfnq-87R8jeI7kAr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانمی که چند سال پیش به عنوان بزرگترین دزد و جیب‌بر خیابون انقلاب تهران شناخته میشد، آزاد شده و به تازگی در رزمایش جانفدا شرکت کرده
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24262" target="_blank">📅 20:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24261">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ژنرال جک کین: شی می‌خواهد ایران جنگ را طولانی کند و نفوذ آمریکا را تضعیف سازد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24261" target="_blank">📅 20:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24260">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سی‌بی‌اس به نقل از یک منبع: انتظار می‌رود دور جدید مذاکرات آمریکا و ایران هفته آینده برگزار شود.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24260" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24259">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گزارشهای بسیار از اختلال گسترده در سیستم بانکی و دستگاه های کارتخوان
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24259" target="_blank">📅 19:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24258">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ارتش اسرائیل: امروز صبح، انبار تجهیزات نظامی حزب‌الله را در منطقه سجده، در جنوب لبنان، مورد حمله قرار دادیم.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24258" target="_blank">📅 19:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24257">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وال‌استریت ژورنال: آمریکا برای تشدید تحریم‌ها علیه جمهوری اسلامی با بیش از ۵۰ کشور تماس گرفته است و به آن‌ها پیام داده: «در قبال ایران یا با ما هستید یا علیه ما.»
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24257" target="_blank">📅 18:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24256">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏اکسیوس: واشینگتن خواستار امتیاز هسته‌ای از تهران است
در حالی که ایران می‌خواهد هرگونه مذاکرات را بر موضوع تنگه هرمز و محاصره دریایی آمریکا متمرکز کند، دولت ترامپ خواستار آن است که ایرانی‌ها با امتیازدهی در موضوع هسته‌ای موافقت کنند.
مذاکره‌کنندگان آمریکایی در جریان مذاکرات روز سه‌شنبه به ایرانی‌ها اعلام کردند که ایران کنترل تنگه هرمز را در اختیار ندارد و بنابراین نمی‌تواند درباره آن مطالبه‌ای مطرح کند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24256" target="_blank">📅 18:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24255">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ef4ff4bd.mp4?token=u4b5Pq7heji-Duby4eBePsqAOIZ89N7bYH_8bazy5QB3jApQpBQeGwjuLPrH2I2Mfq-jnv4HZXWMI5j_CbmcUMddWWLzz-R3LCmkAcss55jqtqEyTQHp79iHGgMyvfBlxopYn2wOop9wX4_XKNjMbjcUThqXLyp4xGXPdZUGfpd9LnNyJ40X5TpyRfrje32tQZUEARS-rHizSLn8tw8tCCxLO210pPHY2QMTAw79v0m8Cb-iu4Zp1Ik7-Z4ZhwmK8tSrn1ThIpFm82EFqXzmJVcGALW4Xrga4Ayw1prrwy6fR4hxaU3FtLupm0tVDSf3pifX7UZ9xbDBuAQQPGU3_Vl6Su2-UQN3TjnAhYu7IMCt_2aNTVkDi6qBhwmeF_0MS7BlJvp-pJof878NUexctUx9ro4tdVLhF_CSBg8ulaDCnDngRRLHJeU3wvCLy08O2HKbX6_v-RCVRc1b-GE5w16PAZlmg_WsQ3BrsfI77M59dznPwNQ5lmlVdNQdOXmaIpTBkzDCQ8UaQJhUbdAJ-6Ww7NY9RSpbM3CVQFcDGSid7FuongS_muzxOC4iDjkcAwh7PzCqutGSWly6eTE16Y6S1eDcCOVjQqDfEOD8ivONgWz4QzVs86x475kK2-WrPLc94ww8tY29Sq9h10i5rPN5fE4Z7V7zU0RLDAUeAq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ef4ff4bd.mp4?token=u4b5Pq7heji-Duby4eBePsqAOIZ89N7bYH_8bazy5QB3jApQpBQeGwjuLPrH2I2Mfq-jnv4HZXWMI5j_CbmcUMddWWLzz-R3LCmkAcss55jqtqEyTQHp79iHGgMyvfBlxopYn2wOop9wX4_XKNjMbjcUThqXLyp4xGXPdZUGfpd9LnNyJ40X5TpyRfrje32tQZUEARS-rHizSLn8tw8tCCxLO210pPHY2QMTAw79v0m8Cb-iu4Zp1Ik7-Z4ZhwmK8tSrn1ThIpFm82EFqXzmJVcGALW4Xrga4Ayw1prrwy6fR4hxaU3FtLupm0tVDSf3pifX7UZ9xbDBuAQQPGU3_Vl6Su2-UQN3TjnAhYu7IMCt_2aNTVkDi6qBhwmeF_0MS7BlJvp-pJof878NUexctUx9ro4tdVLhF_CSBg8ulaDCnDngRRLHJeU3wvCLy08O2HKbX6_v-RCVRc1b-GE5w16PAZlmg_WsQ3BrsfI77M59dznPwNQ5lmlVdNQdOXmaIpTBkzDCQ8UaQJhUbdAJ-6Ww7NY9RSpbM3CVQFcDGSid7FuongS_muzxOC4iDjkcAwh7PzCqutGSWly6eTE16Y6S1eDcCOVjQqDfEOD8ivONgWz4QzVs86x475kK2-WrPLc94ww8tY29Sq9h10i5rPN5fE4Z7V7zU0RLDAUeAq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها می‌خواهند تنگه هرمز را فوراً باز کنند. می‌دانید چرا؟ چون دارند از پا درمی‌آیند؛ می‌دانید چرا؟ چون هیچ پولی وارد کشورشان نمی‌شود. آن‌ها پولشان را از تنگه هرمز به دست می‌آورند، بنابراین خودشان خودشان را فریب دادند.
آن‌ها گفتند: «بیایید تنگه را ببندیم و برای جهان مشکل ایجاد کنیم.» بعد من وارد شدم و بزرگ‌ترین محاصره تاریخ نظامی را برقرار کردیم؛ یک دیوار فولادین!
حدس بزنید چه اتفاقی افتاده؟ حالا دیگر هیچ پولی ندارند، چون خودشان خواستند تنگه را ببندند. من هم گفتم: «بسیار خب، ما هم آن را به روی خودتان می‌بندیم، اما بقیه می‌توانند از آن استفاده کنند.»
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24255" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24254">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67823a94b1.mp4?token=cAor5e5qJd0m9L7aU6NCyBSixHbQNnZsWmsOvmf7PqBCfFwsuWVIWcupa0wCnHt6ZFGL8yT-hVLp5BUvkGh7ULz0ewhc5wAqtyFyfF5oTJjtGFjxxYf8MANxiq1w54KsZs2Xke6FNv1xox6fhgGR8ThTtYS03EGLjrqz4jPWg-EWcxAz_yDATQP__kbfBKukqSUK_qsslLAGy4aPNWV6_puXfQ7_Bfv3M3i6syZUp363gmYM8JB0e_AbLBIS3qYv65CCjmKt-PFUOExhm8wisaoMVVLH8ogAEgIQ0n6ztpAEi_AJs4oA8I_DLpfFGQf6JyssZ5XsraG-hAhJVJt14rmHcur9dvvOFuDqXPPVYClySzbba_N3o7LF61c1k_B0OtEtKHmZ3k5bpUBUFa_9jdNSI9qAZPsEm0rgmNijcO3uoOindB8rlYyzZay-ILpmAC9eWvYUF_nsFYhlZGjzdXCTLA1b6xNc9TRJ2S48aUEzamex-xNZYILROaTPd2IUUbewWIrBWk90FnaFW4plV2tWCFW91gMXmr0dcGJA8hcd_xgwOZTKZrCaI8RRRdmmeH7NZ-pkZSq_kTXYLJ3noFhoNrvX-vNmFhpHxoiMkKjUxkxUinZyTbusa1BH6DfNlp8BL_lX-K1roV-g9C4E42DaP4OK53bLMaNR8iKuKM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67823a94b1.mp4?token=cAor5e5qJd0m9L7aU6NCyBSixHbQNnZsWmsOvmf7PqBCfFwsuWVIWcupa0wCnHt6ZFGL8yT-hVLp5BUvkGh7ULz0ewhc5wAqtyFyfF5oTJjtGFjxxYf8MANxiq1w54KsZs2Xke6FNv1xox6fhgGR8ThTtYS03EGLjrqz4jPWg-EWcxAz_yDATQP__kbfBKukqSUK_qsslLAGy4aPNWV6_puXfQ7_Bfv3M3i6syZUp363gmYM8JB0e_AbLBIS3qYv65CCjmKt-PFUOExhm8wisaoMVVLH8ogAEgIQ0n6ztpAEi_AJs4oA8I_DLpfFGQf6JyssZ5XsraG-hAhJVJt14rmHcur9dvvOFuDqXPPVYClySzbba_N3o7LF61c1k_B0OtEtKHmZ3k5bpUBUFa_9jdNSI9qAZPsEm0rgmNijcO3uoOindB8rlYyzZay-ILpmAC9eWvYUF_nsFYhlZGjzdXCTLA1b6xNc9TRJ2S48aUEzamex-xNZYILROaTPd2IUUbewWIrBWk90FnaFW4plV2tWCFW91gMXmr0dcGJA8hcd_xgwOZTKZrCaI8RRRdmmeH7NZ-pkZSq_kTXYLJ3noFhoNrvX-vNmFhpHxoiMkKjUxkxUinZyTbusa1BH6DfNlp8BL_lX-K1roV-g9C4E42DaP4OK53bLMaNR8iKuKM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: من توافق پیشنهادی آن‌ها را رد می‌کنم. آن‌ها می‌خواهند فوراً تنگه هرمز را باز کنند، چون به‌شدت در حال شکست خوردن هستند. می‌دانید، این را نه در رسانه‌های جعلی می‌خوانید و نه می‌بینید، اما ما با قدرت در حال پیروزی هستیم. کنترل کامل تنگه هرمز را در اختیار داریم. حجم عظیمی از نفت از تنگه هرمز خارج می‌شود و دیشب ۲۹ کشتی از آن عبور کردند. آن‌ها می‌خواهند به توافق برسند و به‌نظر من این خوب است؛ من هم اهل توافق هستم، اما چنین توافقی قابل قبول نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24254" target="_blank">📅 17:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24253">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639d93cd0b.mp4?token=XIIG4IhyWLJgxHAkxziJtbcYMDslXJYSBsUmmV7P0DlwPx-LSEoBz8d_zsE2aNJLxOBGBuSBjXgxYr_I9zfVpB8CTzfEENJsNsYBbgK9D0hJg6LXJ127sk0gwzJM6D0AX8GO5RuhMHx1RMZ3aZHwFPf-d96h7TieyPKKtPtNNzpxg8mKOOKR6LmCTA33E3H4dLan3YDiHGTuG-_yaXIf0xLGcy59_m7c177l-fP5otUevrOsIBXYk2tr7RCBztii_PBMHSuy-fG6OdWKPQXoRjGP4tUsgABW3w99cQq1BkTyB0mv0gzLYVAJ_M2m3Li-H80IrubtV53McTR-nSthAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639d93cd0b.mp4?token=XIIG4IhyWLJgxHAkxziJtbcYMDslXJYSBsUmmV7P0DlwPx-LSEoBz8d_zsE2aNJLxOBGBuSBjXgxYr_I9zfVpB8CTzfEENJsNsYBbgK9D0hJg6LXJ127sk0gwzJM6D0AX8GO5RuhMHx1RMZ3aZHwFPf-d96h7TieyPKKtPtNNzpxg8mKOOKR6LmCTA33E3H4dLan3YDiHGTuG-_yaXIf0xLGcy59_m7c177l-fP5otUevrOsIBXYk2tr7RCBztii_PBMHSuy-fG6OdWKPQXoRjGP4tUsgABW3w99cQq1BkTyB0mv0gzLYVAJ_M2m3Li-H80IrubtV53McTR-nSthAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها پیشنهادی ارائه کردند، اما من آن را رد کردم.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24253" target="_blank">📅 17:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24252">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ: ایران خودش را در یک بن‌بست قرار داده است با بستن تنگه هرمز، و ما بزرگترین محاصره‌ای را در تاریخ نظامی بر ضد آن اعمال کرده‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24252" target="_blank">📅 17:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24251">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: ایران متحمل خسارت می‌شود، زیرا به پول دسترسی ندارد و منبع درآمدش از تنگه هرمز تامین می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24251" target="_blank">📅 17:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24250">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: حجم عظیمی از نفت از طریق تنگه هرمز عبور می‌کند و شب گذشته 29 کشتی از آن عبور کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24250" target="_blank">📅 17:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24249">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ: ایران خواهان یک توافق است و من هم به توافق‌ها علاقه‌مندم، اما این پیشنهاد قابل قبول نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24249" target="_blank">📅 17:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24248">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ: ما به یک پیروزی بزرگ دست خواهیم یافت و کنترل کامل را بر تنگه هرمز به دست می‌گیریم.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24248" target="_blank">📅 17:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24247">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: من توافقی را که ایران از طریق آن خواسته است تجارت را فوراً از سر بگیرد، رد می‌کنم، زیرا این کشور متحمل خسارات زیادی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24247" target="_blank">📅 17:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24246">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی: تهران ادعای پاسخ نظامی به محدودیت‌های هوایی اخیر را رد کرد و از مذاکرات جدی با کشورهای ذی‌نفع برای رفع محدودیت‌ها خبر داد؛ در عین حال، هشدار داد در صورت لزوم، گزینه‌های متقابل غیرنظامی علیه برخی فرودگاه‌ها را اجرا خواهد کرد، هرچند امیدوار است موضوع به این مرحله نرسد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24246" target="_blank">📅 16:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24245">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KV04QAXATGNU7pQqA4M2J3wNCYuLpxMZbkkL6ENQrGb_Kc7IERBlC8umA8sRUqhSH-LwirMhyMcalN6IsH5jHGtXzgrb964gCpOYFqgD2O_LuYNBhMbYhwnTNjbKO3DVrX5WLLp7wAHBUqJdr9FkSnnamIafQDmWZBUKYuWIo0rozhDq28P9KW2bM0Wr1zJnMMSKCcmzzOx5TtL9SjYDkPlg8XLhjgxue_OzrgLuLzddGYh3zNwVAKi6G6csaOS-BVy3mmtQCJ457tzdMSU3kvN5WBKjEFQsJIZW5vG1ulV3MyxuxQB7LofufWKmuBiFuWO4XKCpIXCU3WH-aiSCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گارد ملی آمریکا اعلام کرده که در ۲۲ و ۲۳ سپتامبر، هواپیماهای C-130H3 هرکولس از گردان ۱۶۶ ترابری هوایی دلاور برای پشتیبانی از عملیات سنتکام در خاورمیانه اعزام شده‌اند و حدود ۱۰۰ نفر از نیروها نیز همراه آنها مستقر شده‌اند. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24245" target="_blank">📅 16:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24244">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عراق: خروج ائتلاف بین‌المللی (مبارزه با داعش) به رهبری آمریکا از این کشور در آستانه تکمیل است.
رئیس سلول رسانه‌ای امنیتی عراق اعلام کرد ائتلاف تمام پایگاه‌ها و مقرهای خود در مناطق فدرال عراق
(از جمله پایگاه عین‌الاسد)
را تخلیه و به مقامات عراقی تحویل داده و خروج نیروهای باقی‌مانده از
اقلیم کردستان و پایگاه اربیل
نیز در حال انجام است. مهلت نهایی پایان مأموریت ائتلاف در عراق
برابر با ۸ مهر ۱۴۰۵
تعیین شده است. این به معنای قطع همکاری آمریکا و عراق نیست و پس از آن، روابط امنیتی دو کشور در قالب
همکاری دوجانبه
ادامه خواهد داشت.
@WarRolm</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24244" target="_blank">📅 15:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24243">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تایمز آو اسرائیل:
ائتلاف سعودی اعلام کرد دو پهپاد حوثی‌ها را که به سمت ریاض شلیک شده بودند رهگیری کرده است؛ این حمله در پی افزایش حملات حوثی‌ها و همزمان با مذاکرات امنیتی عربستان، ترکیه و پاکستان رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24243" target="_blank">📅 15:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24242">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUbwPBqlmvff5H1udGSyUb_LOXZs7hHPcbov3r0nKulOcAlMxw2qrmwczKmhr4l8yDBtxXLFwn98djwI001QxAiZWeu666KZlE89ifw5l0KQZlF94fXKfKsTAZEnldUDq3xs2ZadVd5jRbB5oGfCfTptkLXvAs2oxuECetUudTtaKW5jE1yg2LGwAHioirW8SxzCSBjStzmaXe9irQk9-SFLo93jiTwNjb0bKCBPPEuRdiR2UkG5q8_d5fNe-GNFrOQzDy5UeXUOgQ8wUHbzLJDOQGu8G0cBtaLL2H6304hPPRPndGloUUhnFWFjlmcMWE530vHFCiLLhOkFyYUJfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس:
دونالد ترامپ در
واکنش
ی
تمسخرآمیز
به رژیم ایران تصویری از نقشه تنگه هرمز در شبکه اجتماعی خود منتشر کرده که روی آن نام
«تنگه ترامپ»
درج شده است؛ این اقدام پس از پیشنهاد ایران برای بازگشایی تنگه ظرف هفت روز انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24242" target="_blank">📅 15:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24241">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نیروی هوایی عربستان سعودی در حملاتی در شهرستان حیفان، جنوب استان تعز، پروژه تصفیه آب منطقه الأکبوش و شبکه ارتباطات این منطقه را هدف قرار داد.
این حملات در منطقه
الأکبوش ـ الأحکوم
انجام شده؛ منطقه‌ای که طی روزهای اخیر شاهد درگیری‌های شدید میان نیروهای یمنی و حوثی‌ها بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24241" target="_blank">📅 14:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24240">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پزشکیان در مصاحبه با سی‌بی‌اس: ما چند زندانی آمریکایی را آزاد کردیم، اما آمریکا به تعهد خود عمل نکرد.
پزشکیان گفت: «ما کاری را که آمریکا از ما خواسته بود انجام دادیم و چند نفر از زندانیانی را که درخواست کرده بودند آزاد کردیم. قرار بود پول‌های ما آزاد شود؛ این پول از کره جنوبی آمده بود و قطر قرار بود آن را به ما منتقل کند. ما به تعهد خود عمل کردیم، اما آمریکا به تعهدش عمل نکرد.» پزشکیان افزود: «آمریکا چیزی را که می‌خواهد می‌گیرد و بعد به تعهداتش عمل نمی‌کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24240" target="_blank">📅 14:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24239">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بلومبرگ: پایگاه نظامی دائمی آمریکا در لهستان، موسوم به «فورت ترامپ»، ممکن است تا ۴.۴ میلیارد دلار هزینه داشته باشد.
رئیس‌جمهور لهستان، کارول ناوروتسکی، گفته امیدوار است این پایگاه پیش از پایان دوره ریاست‌جمهوری ترامپ در سال ۲۰۲۹ تکمیل و افتتاح شود. مذاکرات درباره
مسائل مالی و اداری و انتخاب محل و زیرساخت پایگاه
همچنان ادامه دارد. بر اساس گزارش بلومبرگ، این پایگاه می‌تواند محل استقرار حدود
۵ هزار نیروی آمریکایی
باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24239" target="_blank">📅 14:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24238">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهور فرانسه، اعلام کرد که در سال ۲۰۲۷ به دلیل محدودیت‌های قانونیِ دوره تصدی، از سمت خود کناره‌گیری خواهد کرد، اما احتمال بازگشت دوباره به ریاست‌جمهوری در آینده را رد نکرد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24238" target="_blank">📅 14:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24237">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فرمول کلاهبرداران
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24237" target="_blank">📅 14:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24236">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یاشار جان درود اینترنشنال الان باید آنفالو بشه یا زوده؟</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24236" target="_blank">📅 14:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24235">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMojtaba Bahrami</strong></div>
<div class="tg-text">یاشار جان درود
اینترنشنال الان باید آنفالو بشه یا زوده؟</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24235" target="_blank">📅 14:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24234">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗦𝗔𝗝𝗔𝗗™</strong></div>
<div class="tg-text">حاجی پس ما برقمون قطو وصل میشه بخاطر این لاشیا بود
🤣</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24234" target="_blank">📅 13:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24233">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef185bab33.mp4?token=LUw9NngkQw5bcRnFw8PMwEKmDDS45fjdjt1wBcXoTS07Jy3fRyWUYnRNvCVl8jRS0fb2epaTJTo9ySZemCer696xWB9XwmgtP2s6NPpozWEAIiAYU5k3kqdiTY2kWpktIGG16FMsJUb2wkLx9cLrhKS39V97m2km6FEh3f39SNVEF0Xq-o0aILhg8pQIXUVRyQQnegg9czeuAD7gmuFUSqZWehAK1QmbfuZkffTrEveEVeDANZ_dgMu1e5RHmw7tFjS95b4tnDLybv96FSoTd10shcPoQtM0f2RE5DW9HArVnUGntoC5YwBX3ok8xNb4-B87pHGNWXSW-DKBi2ktog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef185bab33.mp4?token=LUw9NngkQw5bcRnFw8PMwEKmDDS45fjdjt1wBcXoTS07Jy3fRyWUYnRNvCVl8jRS0fb2epaTJTo9ySZemCer696xWB9XwmgtP2s6NPpozWEAIiAYU5k3kqdiTY2kWpktIGG16FMsJUb2wkLx9cLrhKS39V97m2km6FEh3f39SNVEF0Xq-o0aILhg8pQIXUVRyQQnegg9czeuAD7gmuFUSqZWehAK1QmbfuZkffTrEveEVeDANZ_dgMu1e5RHmw7tFjS95b4tnDLybv96FSoTd10shcPoQtM0f2RE5DW9HArVnUGntoC5YwBX3ok8xNb4-B87pHGNWXSW-DKBi2ktog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">IRAN: NO PLACE FOR AMATEURS
ایران جای آماتورها نیست
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24233" target="_blank">📅 13:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24232">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اگر بیماری قلبی دارید زیرزبانی دم دستتان باشد.
@WarRoom
😂</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24232" target="_blank">📅 13:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24231">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رؤسای جمهور آمریکا و چین توافق کردند که ایران باید به تعهد خود مبنی بر عدم توسعه سلاح‌های هسته‌ای پایبند باشد و نباید برای گذرگاه‌های آبی بین‌المللی عوارضی وضع کند.
همچنین واشینگتن و پکن بر سر کاهش تعرفه‌ها به ارزش 30 میلیارد دلار توافق کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24231" target="_blank">📅 13:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24230">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش شنیده شدن صدای انفجار در خارگ @WarRoom
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24230" target="_blank">📅 13:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24229">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پزشکیان: در حال حاضر قطر و پاکستان پیام‌های ما را به واشنگتن منتقل می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24229" target="_blank">📅 13:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24228">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گزارش شنیده شدن صدای انفجار در خارگ
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24228" target="_blank">📅 13:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24227">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94ee584150.mp4?token=Rwc_ZafFJa_mduUtR1ZTT9CMXGv2xZDJSgWHIfmENAUsSFMrwNWCKmViBRXfDLPQQl6WoJbG-18jBZCM_uk_88VpHYrPjIVEqaFeOb-MQffDHHrOS0YrOZVOzH3YMjKeVUmSyQq6hhMT3Mx2RqtmHDRF0hUicaFhSMqhioHxQ_8BG_PKdSCjHLbIr_3T1R4Y2WW5lNwZPuLVe5w1fe5bMe_O-8NIXv5t23ODHmhaoBFEWtMkzghq35EABnJrfMDwdvQ9rXNRzsbeo1WhAhwFkTUZlSdKaUGpT7lNVC1n5QdJZBpfi7fYxR7icuqkk0M2LeXFTyEBdWU0mJ8GPi1Fg6iZHee_BSS8o4sQIguOYdQHF699tOvtB9ouGq4T5I9AYOLLWh4cYkoe9vqBRAWH_R0qqVZavjpXwbfoJts9H3gX9RYuvMJa8bguFlieO0DHrEG5S9r-bB2pnuylObqGMe1zZS3f0J0n3695ljHeI6FkntOMgJ0yWdaZuEzWSwV_oo_nRtq4xbaJ1FGfSEuk789q2pEaOFOiccpmFYZYVAilgjQy1sU_xIIFDgszJ5oeVes9-rEkX8qKvjqK23KS1ZwUeuIphxd24oOaaR3LXS47DxY0b5r0dQ7TYU9UFuPXvhn6Ely45GTZA-pxKKomQlqkXgQCOymhBgXDXeU1omU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94ee584150.mp4?token=Rwc_ZafFJa_mduUtR1ZTT9CMXGv2xZDJSgWHIfmENAUsSFMrwNWCKmViBRXfDLPQQl6WoJbG-18jBZCM_uk_88VpHYrPjIVEqaFeOb-MQffDHHrOS0YrOZVOzH3YMjKeVUmSyQq6hhMT3Mx2RqtmHDRF0hUicaFhSMqhioHxQ_8BG_PKdSCjHLbIr_3T1R4Y2WW5lNwZPuLVe5w1fe5bMe_O-8NIXv5t23ODHmhaoBFEWtMkzghq35EABnJrfMDwdvQ9rXNRzsbeo1WhAhwFkTUZlSdKaUGpT7lNVC1n5QdJZBpfi7fYxR7icuqkk0M2LeXFTyEBdWU0mJ8GPi1Fg6iZHee_BSS8o4sQIguOYdQHF699tOvtB9ouGq4T5I9AYOLLWh4cYkoe9vqBRAWH_R0qqVZavjpXwbfoJts9H3gX9RYuvMJa8bguFlieO0DHrEG5S9r-bB2pnuylObqGMe1zZS3f0J0n3695ljHeI6FkntOMgJ0yWdaZuEzWSwV_oo_nRtq4xbaJ1FGfSEuk789q2pEaOFOiccpmFYZYVAilgjQy1sU_xIIFDgszJ5oeVes9-rEkX8qKvjqK23KS1ZwUeuIphxd24oOaaR3LXS47DxY0b5r0dQ7TYU9UFuPXvhn6Ely45GTZA-pxKKomQlqkXgQCOymhBgXDXeU1omU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مخزن سوخت یک جنگنده آمریکایی در ارتفاعات ایران پیدا شد: تصاویر منتشرشده از یک مخزن سوخت خارجی پیدا‌شده در ارتفاعات ایران، با توجه به صدا و جنس فلزی برای یک F-15E Strike Eagle است. چون F/A-18/EA-18G از
فایبرگلاس
استفاده می‌کنند ولی ساختار اصلی این مخزن از آلیاژهای آلومینیوم هوافضایی ساخته می‌شود و در بخش‌هایی از آن نیز فولاد، تیتانیوم و مواد پلیمری به‌کار می‌رود. این مخازن از نوع Drop Tank هستند و خلبان می‌تواند در شرایط عملیاتی، پس از مصرف سوخت یا برای کاهش وزن و مقاومت آیرودینامیکی، آنها را عمداً از هواپیما رها کند (Jettison)
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24227" target="_blank">📅 13:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24226">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1482c7d1a.mp4?token=nyz3i6VZoQ1RZh22LODqVCK2VBw9pSUCliDshkgT6I4o8ZTboQsJEY3_On2BQzl5Sr4hByiH--sZ9gOul2jvFJzySAR3_jZozvM7CB9QT4oTgahJMq4rLsCZ5WNwZh_FHnQQdC9KayPg3fXW0PlV99jrcxwOlvastqkkOv1zj3wtVSQbGycTU8Q6BKdxOeVpulDdEh0_58DjXJJDEfoadDmkmfavwNYXZvW_iAaPEBKMjhy3Hinu6WkOGB5wjrlXPUFIOtdyMInNFv7303go2HTYx1T8ZNq6dBinEWvaJXP9W-p0dHS2L92b5AnYhJ_59zZV_LQU3lIoscY2eza2pYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1482c7d1a.mp4?token=nyz3i6VZoQ1RZh22LODqVCK2VBw9pSUCliDshkgT6I4o8ZTboQsJEY3_On2BQzl5Sr4hByiH--sZ9gOul2jvFJzySAR3_jZozvM7CB9QT4oTgahJMq4rLsCZ5WNwZh_FHnQQdC9KayPg3fXW0PlV99jrcxwOlvastqkkOv1zj3wtVSQbGycTU8Q6BKdxOeVpulDdEh0_58DjXJJDEfoadDmkmfavwNYXZvW_iAaPEBKMjhy3Hinu6WkOGB5wjrlXPUFIOtdyMInNFv7303go2HTYx1T8ZNq6dBinEWvaJXP9W-p0dHS2L92b5AnYhJ_59zZV_LQU3lIoscY2eza2pYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش یک معتاد خمار از لانچر
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24226" target="_blank">📅 12:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24225">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOn6Hktpfk9Teyd-oZyOVezigTR2fAjhQfjGiJ4jqnWAT4g_NIXH1WVy-snQFuHj8bLa6SytWtW72hiA35G6a6epcgvgtWE0qMI5_H2469S_l8IK9i36O3SQrAF6uQGAaeonqwvmkztvUNkLC1OhJ3zCKvb2T7cKLKsBDVM9BTr6kj8fIBGhL902y7ni7MMgiilH99tw-E1wAm8-6AoI70GX4l4rAotfUsJ1BA4uV0T45wzxbNSjw4Y1tz371k09wGBGLBZBlFhLvj5NY6gjhRl61wwJK0PJFGD2l85SfCM4tZW9YroZg3Nct9W4sEsIKNk38QRf4OocvHjbcRx_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زرشکیان دو ساعت و نیم پیش نیویورک را ترک کرد و هم اکنون حدودأ در مرکز اقیانوس آتلانتیک شمالی است. بسیار جای مناسبی است تا کوسه‌ها او را بخورند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24225" target="_blank">📅 12:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24224">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a6f13b5b5.mp4?token=Zh7A1IzDhKZY0lW951IwW5fBk9zXROsgVfxRPuo94YuIAWfYaWuHFk5_0bnIUeBxxJ2QtO9zT58Wxr2zc34RR0lwj3sWL1W3RKn1yY4T9HjVR5mmua5314Il5H5GWte43jUHRJ7WASe7-N0r1uhN8uZ8flu530t9ZUv0r9qSZdA9eSpwS4XgZmSZnLaDj3rAzaQOMrdzMiUd05LmtUWTTOqLLCl_jcje6h5eSQPX-A4i0vYOyqdqZvd6YORTSTV5FTt4B7rP_5DzVurrioLmPIpD0tmv1kJdRokCWbjncmaI-8OlyKMn8I88Nb38OSHFez317hqQj4-ZqZVzAqVdSVolq1SexRh80lMuM2epGUosjxCyrv7Jtq-r8QaXmLOEgMOj5cSM1va1ihnQBNY5wm8XS63YK_r5uXfoS8lNotDmf0rke5UllFJrNXxFvwW7g4Hj-ThUoqnLNHW_EO0Z2qFbyJ6Zo5U1xxA8_48AMMHhRc8HNZuppWqCxEceX02pZpbwf6zgTC6-IYOVadaf77WfgmHqTeL2nbjdf1XEkyba5wn4oyKWdHB9SRBOXq175l3BLHo96mmwA7bVxN2oBWByPH6T-Y2u5Qt5y4rWKFO1tSjYpkUjwKtM90PkkmHyHcOVNrFB9r_Jr_N5aNTd46N2AZcOLrsNCbheZ26BSoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a6f13b5b5.mp4?token=Zh7A1IzDhKZY0lW951IwW5fBk9zXROsgVfxRPuo94YuIAWfYaWuHFk5_0bnIUeBxxJ2QtO9zT58Wxr2zc34RR0lwj3sWL1W3RKn1yY4T9HjVR5mmua5314Il5H5GWte43jUHRJ7WASe7-N0r1uhN8uZ8flu530t9ZUv0r9qSZdA9eSpwS4XgZmSZnLaDj3rAzaQOMrdzMiUd05LmtUWTTOqLLCl_jcje6h5eSQPX-A4i0vYOyqdqZvd6YORTSTV5FTt4B7rP_5DzVurrioLmPIpD0tmv1kJdRokCWbjncmaI-8OlyKMn8I88Nb38OSHFez317hqQj4-ZqZVzAqVdSVolq1SexRh80lMuM2epGUosjxCyrv7Jtq-r8QaXmLOEgMOj5cSM1va1ihnQBNY5wm8XS63YK_r5uXfoS8lNotDmf0rke5UllFJrNXxFvwW7g4Hj-ThUoqnLNHW_EO0Z2qFbyJ6Zo5U1xxA8_48AMMHhRc8HNZuppWqCxEceX02pZpbwf6zgTC6-IYOVadaf77WfgmHqTeL2nbjdf1XEkyba5wn4oyKWdHB9SRBOXq175l3BLHo96mmwA7bVxN2oBWByPH6T-Y2u5Qt5y4rWKFO1tSjYpkUjwKtM90PkkmHyHcOVNrFB9r_Jr_N5aNTd46N2AZcOLrsNCbheZ26BSoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان در مصاحبه با شبکهCBS: هر بار که تفاهم هم کردیم باز حمله کردند و کشتنمان،  آمریکا به تفاهم عمل نمی‌کند، مذاکره کردن چه مشکلی را حل می‌کند؟
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24224" target="_blank">📅 11:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24223">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اتاق جنگ با یاشار : به زودی قیمت سوراخ موش در‌ ایران سر به فلک خواهد کشید …
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24223" target="_blank">📅 11:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24222">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وال‌استریت‌ژورنال : ترامپ قصد ندارد محاصره دریایی بنادر ایران را لغو کند؛ واشنگتن امیدوار است فشار اقتصادی، تهران را به پذیرش شروط آمریکا(تسلیم) وادار کند. @WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24222" target="_blank">📅 11:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24221">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وال‌استریت‌ژورنال : ترامپ قصد ندارد محاصره دریایی بنادر ایران را لغو کند؛ واشنگتن امیدوار است فشار اقتصادی، تهران را به پذیرش شروط آمریکا(تسلیم) وادار کند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24221" target="_blank">📅 11:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24220">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کوین‌دسک ,
رشد برخی آلت‌کوین‌ها
: در گزارش بازار روز جمعه، کوانتوم (QNT) حدود
۳۸
درصد، اوندو (ONDO) حدود
۲۸
درصد و چین‌لینک (LINK) حدود
۱۱
درصد رشد روزانه ثبت کرده بودند. این ارقام قیمت لحظه‌ای امروز نیستند
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24220" target="_blank">📅 11:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24219">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">روزنامه گاردین: عباس عراقچی، وزیر امور خارجه ایران که پیش از پزشکیان به نیویورک رفته بود، قصد دارد تا یکشنبه ۵ مهر در این شهر بماند
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24219" target="_blank">📅 11:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24218">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏سیدمحمد مرندی، مشاور پیشین تیم مذاکرات هسته‌ای رژیم جمهوری اسلامی، مدعی شد مذاکرات غیرمستقیم با دولت ترامپ بدون پیشرفت بوده و منطقه به سوی تشدید تنش می‌رود. او همچنین کشورهای حاشیه خلیج فارس را به همراهی با آمریکا در جنگ علیه ایران متهم کرد و اقدامات ترامپ و اسکات بسنت را «توطئه علیه مردم ایران» خواند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24218" target="_blank">📅 11:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24217">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رویترز ، عربستان، ترکیه و پاکستان هماهنگی امنیتی را افزایش دادند: مقام‌های دفاعی سه کشور در ریاض درباره وضعیت امنیتی منطقه، تبادل اطلاعات، هماهنگی نظامی و یکپارچه‌سازی نیروها گفت‌وگو کردند. این نشست در چارچوب توافق دفاعی مشترک مکه برگزار شد.
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/24217" target="_blank">📅 11:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24216">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">«یک مقام ارشد اطلاعاتی اسرائیل، در توصیف میزان ویرانی رفح در سال ۲۰۲۶، گفته است: تقریباً هیچ ساختمانی در رفح باقی نمانده، مگر ساختمان‌هایی که تصمیم گرفته شده بود حفظ شوند.»
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24216" target="_blank">📅 11:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24215">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a2522c0a.mp4?token=qWXz4bZWitO9PSo-ZhGuE1MRrI-J7aXivsj7SnVfzh95DFee7-55UThDlHpDzyLfUnOFvhCkhIWEP7-Ft2HgT7XiY4HtHg5VJyHejC5-LuTNWUocjiACHkwMyZnS6WL3ZHUAnafjWEL0rKhSaN-HNpdwueCuVwxyfboq0N5m-5zNX5LdXjplYEAmyRXAq_3fWEaETcia7mwu-7x6felTo5Wft9PF4jv3uZDaqPpcuYoGUvwtf65lOT7G1YGOV7yrMpj_7MIfyntcOp6rR5RzWYVnzuAyhB4Prm3WaUSnZq34MU41XrVd8ic8pOEp63p-lTwAyPULP9PGqe-uvB96egK7jowF0lEOt8swxJAEI5jWtfNKRmZjjLKc1vMe6VAmG_iY7g0OnKOzG-6QcPYpbSdnfhHZj8ORWLeZj5toZhfm4Qi-wnhrghoCE4BQN7mAlHEPDcH0Q4wxzWsssqqBgXF1RtPrMr6x-cDMIvuZQ-zHdd2h-xhMjoCO91YMX32mq2x5FWKXSRoh-es6h6Q9oztgjyFk4H30KABmutQy20zZJMgrbm1JHpVD1OOVCc_HqnHqyWgokBByhor8PlR5DIIV2xPqEueLZ5vi-QU9Tu8p1fhCI1c0uu3YBjKPHpZ14CT6bbwcF6DAvauDhBIo1EH7tgxEk8bQy0l7aje04Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a2522c0a.mp4?token=qWXz4bZWitO9PSo-ZhGuE1MRrI-J7aXivsj7SnVfzh95DFee7-55UThDlHpDzyLfUnOFvhCkhIWEP7-Ft2HgT7XiY4HtHg5VJyHejC5-LuTNWUocjiACHkwMyZnS6WL3ZHUAnafjWEL0rKhSaN-HNpdwueCuVwxyfboq0N5m-5zNX5LdXjplYEAmyRXAq_3fWEaETcia7mwu-7x6felTo5Wft9PF4jv3uZDaqPpcuYoGUvwtf65lOT7G1YGOV7yrMpj_7MIfyntcOp6rR5RzWYVnzuAyhB4Prm3WaUSnZq34MU41XrVd8ic8pOEp63p-lTwAyPULP9PGqe-uvB96egK7jowF0lEOt8swxJAEI5jWtfNKRmZjjLKc1vMe6VAmG_iY7g0OnKOzG-6QcPYpbSdnfhHZj8ORWLeZj5toZhfm4Qi-wnhrghoCE4BQN7mAlHEPDcH0Q4wxzWsssqqBgXF1RtPrMr6x-cDMIvuZQ-zHdd2h-xhMjoCO91YMX32mq2x5FWKXSRoh-es6h6Q9oztgjyFk4H30KABmutQy20zZJMgrbm1JHpVD1OOVCc_HqnHqyWgokBByhor8PlR5DIIV2xPqEueLZ5vi-QU9Tu8p1fhCI1c0uu3YBjKPHpZ14CT6bbwcF6DAvauDhBIo1EH7tgxEk8bQy0l7aje04Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان در شبکه CBS: اسرائیل هر کسی رو که دلش بخواد با تواناییی که داره ترور می‌کنه، با پشتیبانی آمریکا. رهبر ما مگه تروریست بود که کشتنش. خیلی راحت میان ترور می‌کنن و بعد به دنیا می‌گویند ما با تروریست‌ها می‌جنگیم.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24215" target="_blank">📅 11:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24214">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c51e273e7.mp4?token=rZ0trltQemDRZcGBkMBHZ_ltZ6VSZhIREiMz6mvDTWt6lPCcRAayRPoPX0NlDUoWXEdP_eoVZn7xUo3Q3jREWFPP9ibWn8NR0hMljRmmJZ022SrmEy615ySNBR55DkSuKz5x_WyIu9njfB25vCyiHjy8yzWrm-KANUq4tTpp9EaI9Bnkb9En1lF92Dz2CYGb-9eMIT2H6WCK_HJuP_l_gWZi7hKt7BbB7HFkyQHPoy5GK0AZ8kzgPUFAKaBWwcvRklWN37cN91JlNjPMITOttXT6Ufba30dpFG8DZ1elkHcZfdMI-TmQXOB4stR-b0SbEVOhwBStaXe1bEL-1su8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c51e273e7.mp4?token=rZ0trltQemDRZcGBkMBHZ_ltZ6VSZhIREiMz6mvDTWt6lPCcRAayRPoPX0NlDUoWXEdP_eoVZn7xUo3Q3jREWFPP9ibWn8NR0hMljRmmJZ022SrmEy615ySNBR55DkSuKz5x_WyIu9njfB25vCyiHjy8yzWrm-KANUq4tTpp9EaI9Bnkb9En1lF92Dz2CYGb-9eMIT2H6WCK_HJuP_l_gWZi7hKt7BbB7HFkyQHPoy5GK0AZ8kzgPUFAKaBWwcvRklWN37cN91JlNjPMITOttXT6Ufba30dpFG8DZ1elkHcZfdMI-TmQXOB4stR-b0SbEVOhwBStaXe1bEL-1su8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضجه های حقیرانه پزشکیان در شبکه سی‌بی‌اس: آنها دنبال این هستند جامون رو پیدا کنند و هر وقت دلشون خواست بکشنمون ما گفتگو می‌کردیم که آنها ترورها را آغاز کرده‌اند. هیچ ضمانتی وجود ندارد که دوباره آمریکا و اسرائیل دست از ترورها بردارند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24214" target="_blank">📅 11:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24213">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873be0f119.mp4?token=KR7PAVaL5lwEFXmKV8ps96ybfWaf2RUgXRsVU4lpJGg9uF8Jl4wkxse9MKj5-egEebCUxM8iQHUD0BZBOl91wNoxXVka6IAoBxmhss36oOyjfRTaMDfo3lCEMVgohiteFT-hU-acUxEkCW-86Eqh0iAd0wN68hJ2BZhgu7Gv9H4_GAqZWsew-6MUtazjRfgmMjnd6z3TgjIHNG6109OOVRHLvg5DH2VkQw0N4Fd5UnQ-mhDANebWdZHvqzZSfuFsJMKccgQ3W6NtHDizEyG0WuQuhlWQr-GULAlb-GHy1_PUXOY6IXrAdQfI0iLWzEfhbbyyEH1T-Tb0GOXsfwRZjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873be0f119.mp4?token=KR7PAVaL5lwEFXmKV8ps96ybfWaf2RUgXRsVU4lpJGg9uF8Jl4wkxse9MKj5-egEebCUxM8iQHUD0BZBOl91wNoxXVka6IAoBxmhss36oOyjfRTaMDfo3lCEMVgohiteFT-hU-acUxEkCW-86Eqh0iAd0wN68hJ2BZhgu7Gv9H4_GAqZWsew-6MUtazjRfgmMjnd6z3TgjIHNG6109OOVRHLvg5DH2VkQw0N4Fd5UnQ-mhDANebWdZHvqzZSfuFsJMKccgQ3W6NtHDizEyG0WuQuhlWQr-GULAlb-GHy1_PUXOY6IXrAdQfI0iLWzEfhbbyyEH1T-Tb0GOXsfwRZjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سی‌بی‌اس: «اگر رئیس‌جمهور ترامپ این پیشنهاد را بپذیرد، آیا می‌توانید تضمین کنید که نیروهای نظامی ایران هم به آن پایبند خواهند بود؟»
مسعود پزشکیان: «طبیعتا هر تعهدی که بپذیریم، پایبند خواهیم بود.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24213" target="_blank">📅 11:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24212">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0590db4d.mp4?token=iJrGo4iYX0G5liyiBsgv2GE8E5e0hzSu3BoH95oIzXiZGzoDjgPZ4MkziHVM9Vx96jgQoCQopc-vP9Dmbl6ZW7_VKc9409AExzSRx_OtKbuxUrLW7swKSCCpael8nLgoV4dSyg8LOUnwIo08rXIYuxDchJ6Iq8cPg7a5OaxI34jivET_wrXfj-mol0UH4o_VlD1x2OnVPhNduus8Y0ZaXhaX-RRS23_SduIb1KQUGOXXRSDDcBL_gps3N_BVuY7HTjZ5JhmyXcfIsGN8JJbwqonlsLfqdSu6ookGrKwvMOCBhJnln5zguIi8UnQI98r-X07E0Lezfpv3q9qLOZAAoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0590db4d.mp4?token=iJrGo4iYX0G5liyiBsgv2GE8E5e0hzSu3BoH95oIzXiZGzoDjgPZ4MkziHVM9Vx96jgQoCQopc-vP9Dmbl6ZW7_VKc9409AExzSRx_OtKbuxUrLW7swKSCCpael8nLgoV4dSyg8LOUnwIo08rXIYuxDchJ6Iq8cPg7a5OaxI34jivET_wrXfj-mol0UH4o_VlD1x2OnVPhNduus8Y0ZaXhaX-RRS23_SduIb1KQUGOXXRSDDcBL_gps3N_BVuY7HTjZ5JhmyXcfIsGN8JJbwqonlsLfqdSu6ookGrKwvMOCBhJnln5zguIi8UnQI98r-X07E0Lezfpv3q9qLOZAAoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24212" target="_blank">📅 10:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24211">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a70d94d064.mp4?token=piZQ0NbOR1G9QwS5g4q8ZObBHz27o53A7Rl_BsGd1iXMCYXWIm-A-znf6YXmDwGqwzG1zXeHVX1SwdUecD4snb6zNN6zL9Iilay54iqExAeHiGeLGYdJ4_U03wkXI2CFrHVwprEMh6kpYjxH8KAixPbVrsLkX7aWDnssZLiCqlu3xMHjjAMtff6SpQG6EzAkDq6qW6w37DUDVGCg1xWu2rRplhI1WM-pcHXY7QN71uoYpIcj2ElPsOSoZNAX-M50MJ278VkYWJlX0l3UBPsZ9yUdTandCBFNY73sgcQuyXw_5Sn15VHCmAXHS44wGDyr3fpo4E9LqVtNVLyXdPRwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a70d94d064.mp4?token=piZQ0NbOR1G9QwS5g4q8ZObBHz27o53A7Rl_BsGd1iXMCYXWIm-A-znf6YXmDwGqwzG1zXeHVX1SwdUecD4snb6zNN6zL9Iilay54iqExAeHiGeLGYdJ4_U03wkXI2CFrHVwprEMh6kpYjxH8KAixPbVrsLkX7aWDnssZLiCqlu3xMHjjAMtff6SpQG6EzAkDq6qW6w37DUDVGCg1xWu2rRplhI1WM-pcHXY7QN71uoYpIcj2ElPsOSoZNAX-M50MJ278VkYWJlX0l3UBPsZ9yUdTandCBFNY73sgcQuyXw_5Sn15VHCmAXHS44wGDyr3fpo4E9LqVtNVLyXdPRwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید امیدبخش ترامپ در تروث شامل صحنه‌ای از منهدم کردن لانچر رژیم جمهوری اسلامی
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24211" target="_blank">📅 05:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24208">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرگزاری ABC : در شروع عملیات، اسرائیل اعلام کرد حدود ۲۰۰ جنگنده در بزرگ‌ترین مأموریت پروازی تاریخ نیروی هوایی اسرائیل شرکت کردند و حدود ۵۰۰ هدف را زدند.  آمریکا در نخستین ۲۴ ساعت بیش از ۱۰۰۰ هدف را در عملیات چندمحوره مورد حمله قرار داد. طبق آمار بعدی، تا…</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24208" target="_blank">📅 05:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24207">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرگزاری ABC : در شروع عملیات، اسرائیل اعلام کرد حدود
۲۰۰ جنگنده
در بزرگ‌ترین مأموریت پروازی تاریخ نیروی هوایی اسرائیل شرکت کردند و حدود
۵۰۰ هدف
را زدند.  آمریکا در نخستین ۲۴ ساعت بیش از
۱۰۰۰ هدف
را در عملیات چندمحوره مورد حمله قرار داد. طبق آمار بعدی، تا ۲۳ مارس بیش از
۱۰ هزار پرواز رزمی
و بیش از
۱۰ هزار هدف
در عملیات ثبت شده بود. گزارش سپتامبر Air & Space Forces Magazine می‌گوید Epic Fury در مجموع به
بیش از ۱۳ هزار هدف
حمله کرد و حدود
۱۰ هزار سورتی رزمی
در ۳۸ روز اوج عملیات انجام شد. همان منبع آن را
بزرگ‌ترین کارزار هوایی آمریکا در یک نسل
توصیف می‌کند. خود CENTCOM در ابتدای عملیات آن را
بزرگ‌ترین تمرکز منطقه‌ای قدرت آتش آمریکا در یک نسل
نامید.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24207" target="_blank">📅 04:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24206">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">۱۵ روز قبل از شروع جنگ ۴۰ روزه ۰۲/۱۳/۲۰۲۶</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24206" target="_blank">📅 04:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24205">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9961f001.mp4?token=i-h99RQEzIVY3quC-0lKMfPRM9A_2gJUPYLnqOd9dkHD8VkT1Bd5SWVmZ-r2vs021YkGYSJXM_6bka9vc0xTWKiwPKY4MN8LeL0ik4672uzJhYnR_aRmn7JjQdDNFFg25snkqwel9JxtFQtn7h36dbN0z8qTwxf4ch2Vpg2_Ul3gHq6O2T7rt_JAER-YCEp4nGsd5r3XrO1LNeCFGx-pzSkHWj6SWWmjEEDUlFid7lLSSEWVQAnMmZpLtWJqlqU4TRnMOIIOCtkhol3-rKmBSFoIa-0Z6pita49bMi8C_OfSMnIT-OeLjCBabpunleesvQCYMDnZfzFoUycH1XegKrTEFrFI4suVCEuKjL_gg5db_vuLGZARvNJml1jrBXFYBxV2Fwir8OFv0ubn-QouHIAnvxjaoXY63gjqN2Ara9q9lNMDyvPwKAMZWp5YBrV78n5EspYRgiI4y0MsG97jC_F_BqB03Q5qURj-JcyeRs_qvxoBNq0PJM0B_pYcZujGZPLUReoOwxslzUlFk3RYsH-1-fUtztPpAbSc5Kg_BTJbz9QgNuUnKaEZ8nVEdpUBtYir5MJgbo4-5XAoQcIXR1lpfdknRFYa_G4ZB2EmT_mVu7SXgqALD3y3QjVb8gjo2p4gNdtzmhQFnXVlwsF5i699d9TS7SWQX0MBkhiovTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9961f001.mp4?token=i-h99RQEzIVY3quC-0lKMfPRM9A_2gJUPYLnqOd9dkHD8VkT1Bd5SWVmZ-r2vs021YkGYSJXM_6bka9vc0xTWKiwPKY4MN8LeL0ik4672uzJhYnR_aRmn7JjQdDNFFg25snkqwel9JxtFQtn7h36dbN0z8qTwxf4ch2Vpg2_Ul3gHq6O2T7rt_JAER-YCEp4nGsd5r3XrO1LNeCFGx-pzSkHWj6SWWmjEEDUlFid7lLSSEWVQAnMmZpLtWJqlqU4TRnMOIIOCtkhol3-rKmBSFoIa-0Z6pita49bMi8C_OfSMnIT-OeLjCBabpunleesvQCYMDnZfzFoUycH1XegKrTEFrFI4suVCEuKjL_gg5db_vuLGZARvNJml1jrBXFYBxV2Fwir8OFv0ubn-QouHIAnvxjaoXY63gjqN2Ara9q9lNMDyvPwKAMZWp5YBrV78n5EspYRgiI4y0MsG97jC_F_BqB03Q5qURj-JcyeRs_qvxoBNq0PJM0B_pYcZujGZPLUReoOwxslzUlFk3RYsH-1-fUtztPpAbSc5Kg_BTJbz9QgNuUnKaEZ8nVEdpUBtYir5MJgbo4-5XAoQcIXR1lpfdknRFYa_G4ZB2EmT_mVu7SXgqALD3y3QjVb8gjo2p4gNdtzmhQFnXVlwsF5i699d9TS7SWQX0MBkhiovTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24205" target="_blank">📅 04:52 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
