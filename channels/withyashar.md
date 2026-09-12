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
<img src="https://cdn4.telesco.pe/file/O72a9-HH3H6esaWGx2BmphN1DtYpem78EhNeQvD8STwVQM8jm5P_OgdODy7Ag3W7V8EZzPV9uqpAg9rlG7lxLoighKSQUK5CKIT_uJBjYdY-RoUIlTns8RFOSDdBhgdoP3Q0on2axtdN-qCTFI-buWQvvUuSLZcf4sMEvLDRNyr1ojYLIOvdkNDBwLU20doKFjKGzWkJoW-fcdSR9oxmfdwxUxfo3X2tcQ_SOAVQuOmmJ9OsL_u-5eS15zvaJ80PYwJmXjdi8uQ17Xx3OTYWfkY22pgsmq9KiF7WChAnM3qqaKq9RuJmVji9AMrF8YDLQ78tBbko_aPBwtNYdQ4GQw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 01:20:48</div>
<hr>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارش صدای انفجار بندرعباس
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/withyashar/22988" target="_blank">📅 01:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/withyashar/22987" target="_blank">📅 00:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سی ان ان: پیت هگست، وزیر دفاع آمریکا، برای حضور دو خدمه جنگنده F-15 سرنگون‌شده بر فراز ایران در برنامه«60 Minutes»تحت فشار قرارشان داده است.
به گفته چند منبع آگاه، هر دو نظامی درباره حضور در این مصاحبه نگرانی داشتند و هگست به‌صورت خصوصی با آنها دیدار کرد تا مشخص شود آیا داوطلبانه در برنامه شرکت می‌کنند یا باید با دستور به این کار وادار شوند. در نهایت، یکی از آنها با نام مستعار
«براوو»
با حضور در مصاحبه موافقت کرد، اما نفر دیگر با نام مستعار
«آلفا»
از شرکت در آن خودداری کرد. پنتاگون این گزارش را
«دروغ کامل»
خوانده و گفته تصمیم حضور در مصاحبه کاملاً بر عهده خود این دو نظامی بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/withyashar/22986" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22985">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزیر خزانه‌داری و دارایی ترکیه به شرکت‌ها و مؤسسات مالی این کشور درباره معاملاتی که ممکن است مشمول تحریم شوند هشدار داده است؛ موضعی که چند روز پس از تحریم یک بانک ترکیه و دو شرکت زیرمجموعه آن به دلیل ارتباط مالی با ایران اعلام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/withyashar/22985" target="_blank">📅 00:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/22984" target="_blank">📅 23:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ارسالی : سلام داداش وقت بخیر
از بندرکنگ امشب با فاصله هر 30 دقیقه دارن یه پهپاد یا موشک میزنن به طرف خلیج فارس تا الان 4یا5 تا زدن
@WarRoom</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/22983" target="_blank">📅 23:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22982">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ارسالی : مرز باشماق هم بسته شد من اربیلم و همسرم رفته ایران الان لب مرز مونده نمیزارن بیان گفتن مرز فعلا بسته س و مونده تا ببینم تکلیف چه میشه
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22982" target="_blank">📅 22:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خبرنگار الجزیره: نیروهای اسرائیلی وارد منزل همکارمان، علی السمودی، در جنین شدند، خواستار تحویل او شدند و به پسرش حمله کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/22981" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یک موشک بالستیک حوثی ها در منطقه "جازان" در جنوب غربی عربستان سعودی به یک مسجد اصابت کرد که منجر به زخمی شدن تعدادی از افراد و خسارات جدی شد.
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/22980" target="_blank">📅 22:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22979" target="_blank">📅 22:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22978" target="_blank">📅 22:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حسین حاجی دلیگانی، نماینده مجلس: طرح سه‌فوریتی خروج ایران از NPT آماده شده است بهتر است هر چه زودتر آزمایش‌های لازم را برای سلاح هسته‌ای انجام دهیم @WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22977" target="_blank">📅 22:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وای نت عبری : حملات جدید اسرائیل به جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22976" target="_blank">📅 22:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22975">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22975" target="_blank">📅 21:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تصویر ۳ پاسدار کشته شده در سراوان @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22974" target="_blank">📅 21:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرگزاری رژیم ایرنا:
دقایقی پیش صدای دو انفجار در قشم از سمت دریا شنیده شد
منابع محلی تاکنون در این باره اظهار نظری نکرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22973" target="_blank">📅 21:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پرتاب موشک به سمت تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22972" target="_blank">📅 20:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آسوشیتدپرس: نفتکش آسیب‌دیده در خلیج عمان باعث گسترش لکه نفتی شده است.
بر اساس گزارش جدید، آلودگی نفتی ناشی از یک نفتکش که گفته می‌شود توسط نیروهای آمریکایی هدف قرار گرفته، در حال گسترش به مناطق حفاظت‌شده زیست‌محیطی در عمان و ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22971" target="_blank">📅 20:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLLHuJzUMJJJOvSeuGyBwBXD8-FPtgi_nj_ryGLR-V9mKeSVztj0r3H8tyyHD_XJV-6kdpd4LQ6nLgrqbzQuMkcqEm3GxuI9RNAxlxhGTET_29CQISRq-UyzjJOz-ay6erMDZ9HZtLe3xEiY6TzafoOeysVvEp-zWteK9nrusZzKpVqjOL6m3zLpnvyc2pLlcQYdG48rEV_5JTBlt3Cs4CYq38fE0HGsfQDEAV0lQBsZ4-PbeBQ8T-8K8tOIhrRvdRNVPFlpX6xMnjGEH7sURUoL55zibnUcnaqCQ_0S7gFhgFL28Kh9zjEcBEfzWudUR2aofW9COlPmK7ctOW5pVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ پشت سنگر : یاشار سلام محاصره رو شکستن افراد مسلح همه رو تارو مار کردن نظامیهای رژیم رو @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22970" target="_blank">📅 20:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22969">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دو مقام ارشد امنیتی عراق به رویترز:
ساعاتی پیش سکو های پرتاب پهپاد در چند نقطه از مرز ایران و عراق کشف شدند،
تا اطلاع ثانوی گذرگاه های مرزی با ایران بسته خواهند بود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22969" target="_blank">📅 19:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHDMiZjdm_7irYzvcHIDklDreGR1vN9Ol4fQ7xDHjFoMEtIZ1U_VeppD-n-eZ268SyKLA5OepBwOluaGa8vqLRsPVNkYOzjZIK8qr8ERma4hZRswnRuZtgLvxG1NNOhZLQBHF-eaJ6N9tNZGtGv0qB2XHXhTgL6XddcbMvPRXoNK5vqbIZ2MFdOYFKbDOl3MsO6J_xJRQvQyW59dhzjxXA7IhVHvjvfvLxlyRVB0dNTznRYPBykrfbdZUcEFjCyLlirC9wYHWUYYL1UbiTxbGJITwVuyi9vZEcs6Dxn1KFtOFIL4vjTLp2K521CGZGNxziWtCvw4IlgII8wE10ECGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک تانکر نفتی متعلق به چین با نام لیزا که در دریای مکران حضور داشت، تلاش کرد تا از تنگه هرمز توسط کریدور ایران وارد شود، اما سپس مسیر خود را تغییر داد و به عقب بازگشت. مشخصا آمریکا اجازه نداد  @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22968" target="_blank">📅 18:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شبکه فاکس‌نیوز، هم‌زمان با پشتیبانی نیروهای آمریکایی از عملیات‌های ایالات متحده در جریان تنش با ایران، به‌صورت زنده از ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» که کاملا پر از موشک و مهمات شده است در دریای مکران و نزدیکی تنگه هرمز گزارش می‌دهد. @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22967" target="_blank">📅 18:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2884ed587b.mp4?token=VSA-puXj3SVk6Ukwla1ub76YXPUjbMiYfqvgZSR9-Ssg20Xq70JYVVnoJeALW-gpDZmWDVpCU1obSeJsLRdTY3z0sonz9xQ2l6zQZkx2oiQ97zmTNCmHDFOWNznT49PkXFIYGeXkoa65mVHg259nFCZTI5qAauH8Asu5SOKYfDMOngeBQez7C8aXBTgm74oE8h7CstLysJb5fNExxyKkdSl8cpaofKuohe6GogZqQd5_scynFy-4u1oqi80LcQXipuznbMgiEbybm2je1mUorfu2lEaBztMlWizjG31kaxeWCjoKc2BqFo97AaY97yaUXkVvpfwL5rbK8R8ffDaQk35at1dWRbVsqF6Y-2M0wviKMZoZBGuqz1unOEMZYMP8FnuBNOt5R8lQbd8fcPLimwrSUekJL1tt-WbKItLJdEmeTBHI_mAs1B78idV5G21d-UICKGsq3APgZVnDpQZYA_yFFrcQAhpYXZhb8b1UmEPyxw0tlQ5ySdHe2R9aGHFNKCFGCwQgByRJq06_djhEIwFKm78wtWpvOBoJyUwcG7iN_qky_JGLuRAwOgaZGg5VprfEv0yd_F_4I99B8ywkUpeWIahMHtoC-C2cw1g-GbP2kh95YHYDDRL_XMMUB-rZel04QF2LuNsy20_HXRJ6xzsZ7Pz0TT2g_gfkGF-RZPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2884ed587b.mp4?token=VSA-puXj3SVk6Ukwla1ub76YXPUjbMiYfqvgZSR9-Ssg20Xq70JYVVnoJeALW-gpDZmWDVpCU1obSeJsLRdTY3z0sonz9xQ2l6zQZkx2oiQ97zmTNCmHDFOWNznT49PkXFIYGeXkoa65mVHg259nFCZTI5qAauH8Asu5SOKYfDMOngeBQez7C8aXBTgm74oE8h7CstLysJb5fNExxyKkdSl8cpaofKuohe6GogZqQd5_scynFy-4u1oqi80LcQXipuznbMgiEbybm2je1mUorfu2lEaBztMlWizjG31kaxeWCjoKc2BqFo97AaY97yaUXkVvpfwL5rbK8R8ffDaQk35at1dWRbVsqF6Y-2M0wviKMZoZBGuqz1unOEMZYMP8FnuBNOt5R8lQbd8fcPLimwrSUekJL1tt-WbKItLJdEmeTBHI_mAs1B78idV5G21d-UICKGsq3APgZVnDpQZYA_yFFrcQAhpYXZhb8b1UmEPyxw0tlQ5ySdHe2R9aGHFNKCFGCwQgByRJq06_djhEIwFKm78wtWpvOBoJyUwcG7iN_qky_JGLuRAwOgaZGg5VprfEv0yd_F_4I99B8ywkUpeWIahMHtoC-C2cw1g-GbP2kh95YHYDDRL_XMMUB-rZel04QF2LuNsy20_HXRJ6xzsZ7Pz0TT2g_gfkGF-RZPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه فاکس‌نیوز، هم‌زمان با پشتیبانی نیروهای آمریکایی از عملیات‌های ایالات متحده در جریان تنش با ایران، به‌صورت زنده از ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» که کاملا پر از موشک و مهمات شده است در دریای مکران و نزدیکی تنگه هرمز گزارش می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22966" target="_blank">📅 18:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22962" target="_blank">📅 18:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رویترز به نقل از یک مقام ارشد ایرانی: نشست روز دوشنبه ایران و کشورهای خلیج فارس در عمان به درخواست و ابتکار عمان برگزار می‌شود، اما انتظار نمی‌رود در این نشست توافقی برای بازگشایی تنگه هرمز امضا شود. به گفته این مقام، ایران همچنان خواهان توافقی است که به تهران اجازه دهد از کشتی‌های عبوری از تنگه هرمز عوارض دریافت کند؛ موضوعی که عمان با آن مخالف است. این نشست قرار است علاوه بر هرمز، درباره مسائل منطقه‌ای نیز گفت‌وگو کند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22961" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وزارت خارجه بحرین اعلام کرد که این کشور در نشست وزارتی پیشنهادی درباره وضعیت تنگه هرمز شرکت نخواهد کرد و تا پیش از ازسرگیری روابط دیپلماتیک با ایران، در هیچ نشست جمعی که ایران در آن حضور داشته باشد، طرف نخواهد بود. بحرین همچنین تأکید کرد هرگونه توافق یا ترتیبی درباره کشتیرانی در تنگه هرمز باید بر اساس حقوق بین‌الملل باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22960" target="_blank">📅 17:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آسوشیتدپرس: یک شهروند ایرانی-آمریکایی از زندان اوین آزاد شد، اما همچنان اجازه خروج از ایران را ندارد.
کامران حکمتی، جواهرفروش ۶۲ ساله نیویورکی، پس از گذراندن حدود نیمی از حکم دو ساله خود آزاد شده، اما مقام‌های ایران همچنان ممنوعیت خروج او از کشور را برقرار کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22959" target="_blank">📅 17:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22958" target="_blank">📅 17:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akbKMNKppZn5n2uaAICAUkX1is1ngKRdCtFlIkK-qs7sU5AHu8-KsEckDwPyLZ4cBN81AZKGJC3pKJSfagoMzaFURB2V9kevChH2fWbgnC-tIGsjrCSMkdgQbyN3UAtegBO_39RCiTQAjlHSG-K3MLVwnDous-906BftqX64JCvuZJ78beosSYW6IkZSdvo4dhP-XE2U-BIWVfs-dxN-f-02htHs50cZLttXvJmTIVkaKrhPCC86o0la1GboCLai85u4INxNaAdPzNz6RtQaXql4yl5tqmnM2PQOlnlbf7zX_UozC3ioVzEkiVezJY8nyGmSmsv8vyenQIRfKCcfzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست:
ایران پیش از حمله موشکی ۱۷ ژوئیه ۲۰۲۶ (۲۶ تیر ۱۴۰۵) به پایگاه هوایی موفق السّلتی در اردن، تصاویر ماهواره‌ای با وضوح بالا از این پایگاه در اختیار داشته است.
این تصاویر که توسط
نهادهای چینی در اختیار ایران قرار گرفته بود، هم پیش از حمله و هم پس از آن برای بررسی وضعیت و خسارات پایگاه استفاده شده است.
مقام‌های آمریکایی نام شرکت‌های چینی را اعلام نکرده و دولت چین را مستقیماً به دخالت متهم نکرده‌اند. در این حمله که منطقه محل اسکان نیروها را هدف قرار داد،
۳ نظامی آمریکایی کشته و ۴ نفر دیگر زخمی شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22957" target="_blank">📅 16:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ: اگر ایران سلاح هسته‌ای داشت، ما تماس می‌گرفتیم و می‌گفتیم: "قربان، آیا می‌توانیم با هم ملاقات کنیم؟" ما با آنها بسیار متفاوت برخورد می‌کردیم. @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22956" target="_blank">📅 16:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حسین حاجی دلیگانی، نماینده مجلس: طرح سه‌فوریتی خروج ایران از NPT آماده شده است
بهتر است هر چه زودتر آزمایش‌های لازم را برای سلاح هسته‌ای انجام دهیم
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22955" target="_blank">📅 16:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22954">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d1bb0546.mp4?token=dffYhC8S1pu_C4V-fcyQzy58OwrRllOa2ECdR4lYMXzpB4ILrsSfr1regEnnhgPSC-GqrGXajL8eTQUAiqcS9AZinZVt7enkIgr4uAnDorx4HIAvcne4TOeCtOwjawNkYahzAgJ33-eA0vjnyJMVC9glF3OUqHYEK9dtrRpvuMLzMQ9HEn5eOgas_nKaPG84fy0xC6GyZuJQ0ULWxnL6c6515DKvuxgaqTh0zcnvqj5Cfdg905B4XM0l89ondGe5Ue-9R7yDVTQMoW3w4ivvvEkdUooYPmWijruG56SHno62zJ9BPfpdQICUcxEmNzu2H2FTOZIzsB-MVD9OVIJfUlkx4i6Aji_0-1ZCjEWYvqxh-uQudBHy_0gxcI1Y3fRlvF3EaczOYd8_iV5DG2aKYANrydOeZdLGdeoOmwZZBDGwzCctxdD6P1gB9cCl2luh0Exl5E0ryDq0saePg85fnysTqcb18TR8qCZeIZ2iKRAJJLNfKDKelLLJ1s968SD9LuLSZHmF_AXNUTbpKw9j_aVJ8Zdtj46g-qjWKArjGF7Lqxfry95chDgtcFra8gFZPh64FX8W4xWrqFENvEBBzKXUIdbU7tHDjmKBvXXlQ-v4hqWt4Hk4BjY_me75QcJljT7z-5yLFYhfNaXE3cDaKkxmyI2Rev_b5hegDGUhHFY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d1bb0546.mp4?token=dffYhC8S1pu_C4V-fcyQzy58OwrRllOa2ECdR4lYMXzpB4ILrsSfr1regEnnhgPSC-GqrGXajL8eTQUAiqcS9AZinZVt7enkIgr4uAnDorx4HIAvcne4TOeCtOwjawNkYahzAgJ33-eA0vjnyJMVC9glF3OUqHYEK9dtrRpvuMLzMQ9HEn5eOgas_nKaPG84fy0xC6GyZuJQ0ULWxnL6c6515DKvuxgaqTh0zcnvqj5Cfdg905B4XM0l89ondGe5Ue-9R7yDVTQMoW3w4ivvvEkdUooYPmWijruG56SHno62zJ9BPfpdQICUcxEmNzu2H2FTOZIzsB-MVD9OVIJfUlkx4i6Aji_0-1ZCjEWYvqxh-uQudBHy_0gxcI1Y3fRlvF3EaczOYd8_iV5DG2aKYANrydOeZdLGdeoOmwZZBDGwzCctxdD6P1gB9cCl2luh0Exl5E0ryDq0saePg85fnysTqcb18TR8qCZeIZ2iKRAJJLNfKDKelLLJ1s968SD9LuLSZHmF_AXNUTbpKw9j_aVJ8Zdtj46g-qjWKArjGF7Lqxfry95chDgtcFra8gFZPh64FX8W4xWrqFENvEBBzKXUIdbU7tHDjmKBvXXlQ-v4hqWt4Hk4BjY_me75QcJljT7z-5yLFYhfNaXE3cDaKkxmyI2Rev_b5hegDGUhHFY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22954" target="_blank">📅 15:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a7fc7dd57.mp4?token=CUkF73WLiZ41_neWNSWZGkh73OvIgaKLuOTMn_0vKVY_rO60E4CwaiXpeXbh6Usw67mQYnYjUSVwtLar7F5rM_xgntXc-a5fdXKbp5cdJhqgZV9Oqk-grtR634vZnNj5FrKG9-AZWxg6q1yx7BLASJKuUZjNswtph7vxtONatwLXw1YGyQ5_Z6uKSqsfNTKwqEYmHgF7gxuK8oV9f8X8M-G2z52Td5rntoRNh-9VqCGemrD3dWLfZUz2RZWoteowfFUwOW_K2nxQZ3EhJMOeEu_HT3slBitS2-zhZPprO6STCK51iK7Zvl1HeGRmsoiPiPmJTdMxhAAnvltvFLYSWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a7fc7dd57.mp4?token=CUkF73WLiZ41_neWNSWZGkh73OvIgaKLuOTMn_0vKVY_rO60E4CwaiXpeXbh6Usw67mQYnYjUSVwtLar7F5rM_xgntXc-a5fdXKbp5cdJhqgZV9Oqk-grtR634vZnNj5FrKG9-AZWxg6q1yx7BLASJKuUZjNswtph7vxtONatwLXw1YGyQ5_Z6uKSqsfNTKwqEYmHgF7gxuK8oV9f8X8M-G2z52Td5rntoRNh-9VqCGemrD3dWLfZUz2RZWoteowfFUwOW_K2nxQZ3EhJMOeEu_HT3slBitS2-zhZPprO6STCK51iK7Zvl1HeGRmsoiPiPmJTdMxhAAnvltvFLYSWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما یک درگیری نظامی کوتاه داشتیم. آن‌ها می‌گویند: «آیا ممکن است از کلمه «جنگ» استفاده نکنید؟ چون وقتی از کلمه «جنگ» استفاده می‌کنید، موضوع کمی متفاوت می‌شود.»
به نظر من، این یک درگیری نظامی است. ما آن‌ها را به شدت تحت فشار قرار داده‌ایم.
در مورد ونزوئلا، ما آنجا را تحت کنترل خود درآوردیم. ما در آن جنگ پیروز شدیم
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22953" target="_blank">📅 15:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وای نت
: کشورهای خاورمیانه، سقوط جمهوری اسلامی را به نفع منطقه می‌دانند
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22952" target="_blank">📅 15:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صداوسیما:  پس از بسته شدن دو پایانه مرزی شلمچه و چذابه به شکل یک طرفه از سوی عراق؛ از ساعاتی پیش مرز چذابه برای فقط خروج اتباع عراقی که قصد بازگشت دارند؛باز شد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22951" target="_blank">📅 14:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آسوشیتدپرس: رئیس‌جمهور لبنان به نباطیه در جنوب لبنان رفت.
جوزف عون در سفری
کم‌سابقه
به جنوب لبنان، در حالی که نگرانی‌ها از حملات مجدد اسرائیل افزایش یافته، از افزایش حضور ارتش لبنان و تلاش دولت برای حفظ ثبات منطقه سخن گفت. این سفر اکنون پس از عملیات اسرائیل در ارتفاعات علی‌الطاهر و ادامه تنش با حزب‌الله انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22950" target="_blank">📅 14:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رویترز: کشورهای بریکس بر سر بیانیه مشترک به توافق رسیدند.
منابع می‌گویند اعضای بریکس در نشست دهلی‌نو بر سر بیانیه‌ای توافق کرده‌اند که
اقدام نظامی یک‌جانبه هر کشوری را محکوم می‌کند
، اما برای جلوگیری از اختلاف، نام هیچ کشوری در آن ذکر نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22949" target="_blank">📅 14:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f69baa1d9.mp4?token=gC72AcUwyqEjcV-iT_2pBLSAppWHWCYDE8s31s5mfVHq2UdR1LKhcmIJiQ8ud6BvAN7UaNTi31txuOli0ZfYYVryb1WzO0lVo5HhAQsquC_Cw6UrBewAsl5NJIiQwY7syPpvkG3sT5zBpoKwLIuYCYG06L1BfC1dvhFcOPUi4PfxgI13EQZBZMrytiTwN9XrnCnoVPRqGD9H7VY-UwFU7fOpiP4eWgMwoft7wi7WW7j0paYoID8nACwVWGzOIpV3hsVwXZ_AKUZeg77CkUdhubNTZR5p_a9wGUM02GfX4v3eT_uuXFgk-JnLLbsveJrj4MkVTysvmF9_xzKQ1ZhDVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f69baa1d9.mp4?token=gC72AcUwyqEjcV-iT_2pBLSAppWHWCYDE8s31s5mfVHq2UdR1LKhcmIJiQ8ud6BvAN7UaNTi31txuOli0ZfYYVryb1WzO0lVo5HhAQsquC_Cw6UrBewAsl5NJIiQwY7syPpvkG3sT5zBpoKwLIuYCYG06L1BfC1dvhFcOPUi4PfxgI13EQZBZMrytiTwN9XrnCnoVPRqGD9H7VY-UwFU7fOpiP4eWgMwoft7wi7WW7j0paYoID8nACwVWGzOIpV3hsVwXZ_AKUZeg77CkUdhubNTZR5p_a9wGUM02GfX4v3eT_uuXFgk-JnLLbsveJrj4MkVTysvmF9_xzKQ1ZhDVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تهران (ونک) ی غذاخوری افتتاح شده که عرزشی سوز ترین رستوان شده به اسم بی بی که تخصصش  کتلت درست کردنه، حالا ی عده عرزشی فشاری شدن و بهش گیر دادن، میگن تو عمدا اسم غذاخوریتو گذاشتی بی بی و فقط کتلت درست میکنی.
@WarRoom
😂
✌🏼</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22948" target="_blank">📅 14:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: فکر می‌کنم ایران موشک‌هایی دارد که می‌تواند شهرهای اروپایی را هدف قرار دهد
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22947" target="_blank">📅 14:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22946">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دیدبان اتاق جنگ پشت سنگر : یاشار سلام محاصره رو شکستن افراد مسلح همه رو تارو مار کردن نظامیهای رژیم رو @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22946" target="_blank">📅 13:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/063b6ca407.mp4?token=a7WOGdGKBgTNKGeXPYNdE6TKleM7NjDLQaFoFvZMdBhdI5_NtvCYp_Z18i5EsvgzRTuOsxf2UCBWvG5ERG-a8PtaCA6w2X5YBi_Ss4NS2PVdwrO-uVpp73U76QkjOLhHZMgo1PcW-jT-ffQa_pCReBce-fQi3euKUQ-r5qVL0QOGsv7CUCdrRMppoGIDKbpcRbyUFq2Zfao002oYLA2FE5-nxUilFATTzkaN4vy-zzTmPgRmh9GqKaOjP43HxChSrsdEtn73z7pS0uK_axo8BKvO7kZlYi8LJ94cBjNCu6UxTRoZl_o69rQgmdhurc7ZSTgFdvIqSHxCxFCcEkHgqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/063b6ca407.mp4?token=a7WOGdGKBgTNKGeXPYNdE6TKleM7NjDLQaFoFvZMdBhdI5_NtvCYp_Z18i5EsvgzRTuOsxf2UCBWvG5ERG-a8PtaCA6w2X5YBi_Ss4NS2PVdwrO-uVpp73U76QkjOLhHZMgo1PcW-jT-ffQa_pCReBce-fQi3euKUQ-r5qVL0QOGsv7CUCdrRMppoGIDKbpcRbyUFq2Zfao002oYLA2FE5-nxUilFATTzkaN4vy-zzTmPgRmh9GqKaOjP43HxChSrsdEtn73z7pS0uK_axo8BKvO7kZlYi8LJ94cBjNCu6UxTRoZl_o69rQgmdhurc7ZSTgFdvIqSHxCxFCcEkHgqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران: ما با قدرت بسیار زیادی تنگه هرمز را کنترل می‌کنیم. هیچ‌کس انتظار نداشت چنین اتفاقی بیفتد.
ما به‌طور متوسط روزانه ۲۵ قایق را از بین می‌بریم
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22945" target="_blank">📅 13:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd5f25930.mp4?token=uiZo3UPDU5vfnqwM2RelRZcRYGxnxm6Sc-jST9oCSlKDaQH_9eTGeLNPzKA7oHaNWVEwNCke0r3Si6tGqcuSZg7SJuAX8plyVPgoW2eagczJ6qU_8Kp2_Mz3-BHQx_-jpJgBmRxi5jV3401EqCGJQLM8SXRZqxj3EaRuUt5-4_VZoRVsds10VCmcr9eYMLy_JTgEhf848MC35wHrOxHjCgWSQB__ZcfwVE1tV-tbTOSQk9kLwOiEiiVNpEPtn6XnSESH-Wa2t1b1Gclyjmj9IBkfjvIeyoCQpnJOr6CWm_5XfEisS6c4tC4PSq2e94XDRLEXHnZIAMLSTm0Bd2iwtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd5f25930.mp4?token=uiZo3UPDU5vfnqwM2RelRZcRYGxnxm6Sc-jST9oCSlKDaQH_9eTGeLNPzKA7oHaNWVEwNCke0r3Si6tGqcuSZg7SJuAX8plyVPgoW2eagczJ6qU_8Kp2_Mz3-BHQx_-jpJgBmRxi5jV3401EqCGJQLM8SXRZqxj3EaRuUt5-4_VZoRVsds10VCmcr9eYMLy_JTgEhf848MC35wHrOxHjCgWSQB__ZcfwVE1tV-tbTOSQk9kLwOiEiiVNpEPtn6XnSESH-Wa2t1b1Gclyjmj9IBkfjvIeyoCQpnJOr6CWm_5XfEisS6c4tC4PSq2e94XDRLEXHnZIAMLSTm0Bd2iwtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: جنگ در ایران چه زمانی پایان می‌یابد؟
ترامپ: فکر می‌کنم خیلی زود؛ احتمالاً درست پس از انتخابات میان‌دوره‌ای.
آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا انتخابات را پیچیده کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22944" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a5eefe77.mp4?token=NJcGTV8zCc4JRC5Ma-7WAzCXypceVv-m9fUiWvnFUtzL3RTLY4aScq2WsMo1lYqjMvRmEg8mQpqzgwl-rrvs05ZvxLt-swaekw6kdfgCNOoNUzgEEKjO78z6efrz5BgvhLc4Up9DS8SEafJC6vuAVUTS6n8XXoCjHhHkNR9TgtXuNcuC20UhImkosYROxzuuRdd5q755HEyoRH7FmHaG-Ze3ZXU-W4yoMN4grlIO2a5hb6Bjf-mvwk0GJDBmcgmilaiKnDkwsSvfw6GtFMWFT0cBQ4nIax-xw2YXNPtiFN-tsDOQUizMHQa02tARaL7b-OXUFduVfp-4GqFU1-E4VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a5eefe77.mp4?token=NJcGTV8zCc4JRC5Ma-7WAzCXypceVv-m9fUiWvnFUtzL3RTLY4aScq2WsMo1lYqjMvRmEg8mQpqzgwl-rrvs05ZvxLt-swaekw6kdfgCNOoNUzgEEKjO78z6efrz5BgvhLc4Up9DS8SEafJC6vuAVUTS6n8XXoCjHhHkNR9TgtXuNcuC20UhImkosYROxzuuRdd5q755HEyoRH7FmHaG-Ze3ZXU-W4yoMN4grlIO2a5hb6Bjf-mvwk0GJDBmcgmilaiKnDkwsSvfw6GtFMWFT0cBQ4nIax-xw2YXNPtiFN-tsDOQUizMHQa02tARaL7b-OXUFduVfp-4GqFU1-E4VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا
ایران
مسئول حمله به خط لوله نفتی شرق-غرب عربستان است؟
ترامپ: فکر می‌کنم آنها هستند، احتمالاً آنها هستند
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22943" target="_blank">📅 13:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ در مورد حمله به خط لوله نفت سعودی: حوثی‌ها نمی‌خواهند با ما وارد جنگ شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22942" target="_blank">📅 13:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: ما آتش را در غزه خاموش کردیم و روند صلح را در آنجا تسهیل خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22941" target="_blank">📅 13:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دونالد ترامپ در مورد حمله به خط لوله انتقال نفت در عربستان سعودی: به احتمال زیاد، ایران مسئول این حمله است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22940" target="_blank">📅 13:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">.:
سلام یاشار جان من ساعت ۱۲ فردوسی بودم
دلار ۲۴۲ معامله میشد
اقتصاد مملکت داره منفجر میشه
خدا به مردم رحم کنه با این گرونی ها</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22939" target="_blank">📅 13:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ : اوضاع در ایران برایمان بسیار خوب است
همه چیز  به آرامی حل خواهد شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22938" target="_blank">📅 13:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ae38d90fc.mp4?token=C6AGv7XFvPuae2Njcp6L6CHf83utrfcI9wDxkatmORr99_6IplI7br9Px-RSGBduRTKCfDaVEIsfg43zeJjy66tBhDm7Ro0N1fRgsvT_wdtgKWOALmp7WNReIfuEhrOJDg4oUv0JZEDXBqbqWqarZAsv312Qefb35mhzNnYnm0Zo6nBIJt72vYEOm72agjIA11HkFjzBhqF4R13GaNyyEjgL7v95OIWvYevdvqOJtGhpCYTs3EgfQ5hiLnVypDyKalXsyagbncQceTO-GzB8PzZ8WTxVRqc9wNumOwlJVaHEmauGyns1eXs2rxrkKIls2wh3EvgXjA53FF3vILLPSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ae38d90fc.mp4?token=C6AGv7XFvPuae2Njcp6L6CHf83utrfcI9wDxkatmORr99_6IplI7br9Px-RSGBduRTKCfDaVEIsfg43zeJjy66tBhDm7Ro0N1fRgsvT_wdtgKWOALmp7WNReIfuEhrOJDg4oUv0JZEDXBqbqWqarZAsv312Qefb35mhzNnYnm0Zo6nBIJt72vYEOm72agjIA11HkFjzBhqF4R13GaNyyEjgL7v95OIWvYevdvqOJtGhpCYTs3EgfQ5hiLnVypDyKalXsyagbncQceTO-GzB8PzZ8WTxVRqc9wNumOwlJVaHEmauGyns1eXs2rxrkKIls2wh3EvgXjA53FF3vILLPSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ پشت سنگر : یاشار سلام محاصره رو شکستن افراد مسلح همه رو تارو مار کردن نظامیهای رژیم رو
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22937" target="_blank">📅 13:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/suwtSCIdDm4MxzSfemTRq4ymFgUOU3xG_lhIBXzKJ-s4Z62X72SkrrAT0CBD6nx5oo8nSBPP2hy_DtKHKcE00HVhTBThwivB0HRF1nJMeYrioe5wnO--P4kdTp1eAXM2o--qQQ3Otl9Sx2hQ_tMhj7XHX373syj2OOjIPEOw19u8y1T--6K1NxRhPX-iHXldF__9BEk0MRvMmVCzrqrWGsaInWigEF1daz4jD-5ppOfieDZWv3PpcFuJuBBif1MJFJoHjbBaQsEdFBzn8eYgQOYN28IamonpLQgwfZMNDBQEZ62FB7B0aCgsK2yDw7ncikjtuCC3Wd_d7jFpSYDplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fnokP9FF9s6EWCumH7kdNbYIsjAsSXI8xYpMJyrZYrpiXuQYK7A7j2I4wIufpgGt8_YWHrQd_MZM1UyIx3jwOPgqZolRCR6wpDjKqxK3_ffn54mCit6_iSbGJG3q-dolFkdQVIOzWz617LmYUVoNPXLgmUpO97Kfm9BiAIY08SODMkdUoFJM48vv9vV8o4vazbNexmZOtrt7XJ3QPgYtTzWmECdeohfXV6iNHnaqc4kKKbiCH6QyJHhyqwIwCclWR_YgRlosXhgHrZMCPy_a0BlAm8Dp6gJGaFg4sju0fI721ybboQ-j8bKEATl8tLCdyobHxrY8nMyRWEr7tc64mQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک تانکر نفتی متعلق به چین با نام لیزا که در دریای مکران حضور داشت، تلاش کرد تا از تنگه هرمز توسط کریدور ایران وارد شود، اما سپس مسیر خود را تغییر داد و به عقب بازگشت. مشخصا آمریکا اجازه نداد
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22935" target="_blank">📅 12:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نرخ دلار ۲۳۵،۰۰۰ تومان
دلار کف بازار ۲۴۰،۰۰۰ هزار تومان
تتر ۲۳۴،۶۰۰ تومان
بیتکوین ۷۷،۳۰۹ $
انس جهانی طلا ۴،۳۴۷ $(آخرین قیمت)
نفت برنت  ۱۰۴،۶۱$(آخرین قیمت)
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22934" target="_blank">📅 12:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d069691bb.mp4?token=TGktAHJddIJhkYbK0ZCuz624UjnbyDBz0m13AcIfHwf09pikaiJPN41uGiE9iZ4o4xc_NY8GzaOFuw5Ne_6-PFjVxmaI1qm7j5ismTh1Eri4AFsPXIHfMY3GZ9DaOd1PtwVzLH-XI_6VoXnaQMmZujryUGMeEwM8aCNemkKAVdY8jxb2v-x1izseZ6QkVhEK3gAKQWwHg-UOnZ9Ep5zXFr2NyTCqblqFsaBC81IUwMqf1hioHGllJF85ETBJEAZ_idWm7AR49168VkgLpXrlPBwNM45lNbJxrNLNKf7aa5SOspft6aRgaM8E1IJ30teTNVOmugPiXYyblUvuuvU52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d069691bb.mp4?token=TGktAHJddIJhkYbK0ZCuz624UjnbyDBz0m13AcIfHwf09pikaiJPN41uGiE9iZ4o4xc_NY8GzaOFuw5Ne_6-PFjVxmaI1qm7j5ismTh1Eri4AFsPXIHfMY3GZ9DaOd1PtwVzLH-XI_6VoXnaQMmZujryUGMeEwM8aCNemkKAVdY8jxb2v-x1izseZ6QkVhEK3gAKQWwHg-UOnZ9Ep5zXFr2NyTCqblqFsaBC81IUwMqf1hioHGllJF85ETBJEAZ_idWm7AR49168VkgLpXrlPBwNM45lNbJxrNLNKf7aa5SOspft6aRgaM8E1IJ30teTNVOmugPiXYyblUvuuvU52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22933" target="_blank">📅 11:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الجزیره: حوثی‌ها مدعی کنترل کامل ساحل دریای سرخ یمن شدند.
گزارش جدید می‌گوید نیروهای حوثی پس از پیشروی سریع در امتداد ساحل و تصرف شهر المخا و جزیره میون، اکنون مدعی
کنترل کامل ساحل دریای سرخ یمن
هستند؛ اقدامی که موقعیت آنها در اطراف باب‌المندب را به شکل قابل‌توجهی تقویت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22932" target="_blank">📅 11:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اتاق جنگ با یاشار : مرزهای بسته شده تا این لحظه، ۱- مرز چذابه ۲- شلمچه ۳- سومار ۴-بازرگان(گزارش تایید نشده) همچنین فرودگاه بین‌المللی بصره تمام پروازهای خروجی به ایران و ورودی از ایران را تا اطلاع ثانوی تعلیق کرد. @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22931" target="_blank">📅 11:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مسعود پزشکیان در گفتگو با یک رسانه هندی خبر داد که روز دوشنبه توافق عمان و ایران درباره مسیر مشترک تنگه هرمز در حضور وزرای کشورهای عربی حاشیه خلیج‌فارس امضا و به سازمان دریانوردی بین‌المللی اعلام می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22930" target="_blank">📅 11:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزرای AFP گزارش داده مذاکرات بعدی میان
اسرائیل و لبنان در رم به ماه اکتبر موکول شده است
. این مذاکرات قرار بود درباره ترتیبات امنیتی و وضعیت نیروهای اسرائیلی در جنوب لبنان انجام شود.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22929" target="_blank">📅 11:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22928">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اتاق جنگ با یاشار : مرزهای بسته شده تا این لحظه، ۱- مرز چذابه
۲- شلمچه ۳- سومار ۴-بازرگان(گزارش تایید نشده)
همچنین
فرودگاه بین‌المللی بصره تمام پروازهای خروجی به ایران و ورودی از ایران را تا اطلاع ثانوی تعلیق کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22928" target="_blank">📅 10:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اخطار
⚠️
⚠️</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22927" target="_blank">📅 10:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5080718a1f.mp4?token=qiMqlxS800AF6fqNFFKaUl2jhxa9au63OWCvT9kuQbWc9GdNhDcdfdey2fhLxG8t69NQXJQMhE02KdYTz0WRuO-VuX_2JJSGvnDEtDRPceil8lyBc1OH0jDbm7Mw6AgaZ_WSD7_rHuPGqtP30QL1WrY93iHSWISrAlc4LFUFdzLppungmnroxDbckVRbRpQ3fzS8CG3dDZqoLVzqsLwr9XFIRPKcGcS1bczBHThxjX_-mbMAv98MOiFNSIXUAkh5mmeHCd7mI1XcoTYYRS6V6yrnGnDUvr46TSRlEQzzidxCF6dYAXAKHJBOBCYPVQOquj23-9d6yIm7C7b-V4xT_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5080718a1f.mp4?token=qiMqlxS800AF6fqNFFKaUl2jhxa9au63OWCvT9kuQbWc9GdNhDcdfdey2fhLxG8t69NQXJQMhE02KdYTz0WRuO-VuX_2JJSGvnDEtDRPceil8lyBc1OH0jDbm7Mw6AgaZ_WSD7_rHuPGqtP30QL1WrY93iHSWISrAlc4LFUFdzLppungmnroxDbckVRbRpQ3fzS8CG3dDZqoLVzqsLwr9XFIRPKcGcS1bczBHThxjX_-mbMAv98MOiFNSIXUAkh5mmeHCd7mI1XcoTYYRS6V6yrnGnDUvr46TSRlEQzzidxCF6dYAXAKHJBOBCYPVQOquj23-9d6yIm7C7b-V4xT_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22925" target="_blank">📅 10:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa0dc375e.mp4?token=RcfDGy-YIl2lN7PUDSexWAh07RlHJzoHLCrbmvcv0_iuNVNIyXzc2YCImHfBsED0_3vuH14hFxH6QsoUn0UpKXpNgtI9gRBeaZxhS-H3lSbRgHBElOwa2SdBaqmnBgnIDPpmkapeBK8W9kJzLaUKKlfUIFG-7yKfKr8_DMGtAlTUoTM7-6EIV2OCdNPpstat0EAtpBPAfCc_5WWy13TFLJpatEPnsZtBRxQxSyHzRlGNBdJHqj-DiEFuJMw5rCq1pwDBpb-KfsTVk9jwVX0h9_3FnTyBk8ZO7IiRm9HyzbWdE7CQuM3HeemdfW_Df2WhMLSTCDeii0hOagqGpmS9Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa0dc375e.mp4?token=RcfDGy-YIl2lN7PUDSexWAh07RlHJzoHLCrbmvcv0_iuNVNIyXzc2YCImHfBsED0_3vuH14hFxH6QsoUn0UpKXpNgtI9gRBeaZxhS-H3lSbRgHBElOwa2SdBaqmnBgnIDPpmkapeBK8W9kJzLaUKKlfUIFG-7yKfKr8_DMGtAlTUoTM7-6EIV2OCdNPpstat0EAtpBPAfCc_5WWy13TFLJpatEPnsZtBRxQxSyHzRlGNBdJHqj-DiEFuJMw5rCq1pwDBpb-KfsTVk9jwVX0h9_3FnTyBk8ZO7IiRm9HyzbWdE7CQuM3HeemdfW_Df2WhMLSTCDeii0hOagqGpmS9Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری‌هایی در شهر سراوان در استان
سیستان و بلوچستان ایران
میان نیروهای امنیتی ایران و اعضای جبهه مبارزان خلق (PFF)، که پیش‌تر با نام جیش‌العدل شناخته می‌شد، رخ داد.
این درگیری‌ها پس از آن آغاز شد که نیروهای ایرانی به یکی از
مخفیگاه‌های این گروه
یورش بردند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/22921" target="_blank">📅 10:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22920">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فایننشال‌تایمز: آمریکا حفاظت هوایی از نفتکش‌ها در تنگه هرمز را محدود کرده است.
سنتکام با به دستگرفتن کنترل غالب اکنون به نفتکش‌ها اعلام کرده پوشش پدافند هوایی آمریکا در هرمز دیگر به‌صورت شبانه‌روزی ارائه نمی‌شود و کشتی‌ها باید در بازه‌های زمانی مشخص، از جمله حوالی ساعت ۹ صبح، عبور کنند. این تصمیم پس از افزایش حملات شبانه ایران و برای کاهش هزینه و فشار عملیاتی نیروهای آمریکایی گرفته شده است
@WarRoom</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/22920" target="_blank">📅 10:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab9a6cb30.mp4?token=Vr4qDAXXgJmBMJceuDkGwwMsEP14w5uKSdEYObH2xBeXHSO93CI557DyS_44MPB0dDCIWL8eQU-Xr9svKHQ-OO2QbB3nUXGeiyfCmhYFI8dXGfOR5I2SSxe5xDY-HrWvcdrcy_zZ2enIrJSVEIzsWCyIwgG2rZgj_Dht7YIgYOq5zWHMT0jekD7LKS3uuP5ALv8s27nFmNR9UrL3yZtqnzwdwsY7-gJ_rUAlZtoz3-eFCDBM8gZww2U_fMhc1MjJ0dqYrmm5Z99V1sV2qWhzYb7cP7Uy32luBQh3_VDTwQgeFQKKmSZS6qlU3WhddRi6XEanyiD4uLaY59RdfGN82Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab9a6cb30.mp4?token=Vr4qDAXXgJmBMJceuDkGwwMsEP14w5uKSdEYObH2xBeXHSO93CI557DyS_44MPB0dDCIWL8eQU-Xr9svKHQ-OO2QbB3nUXGeiyfCmhYFI8dXGfOR5I2SSxe5xDY-HrWvcdrcy_zZ2enIrJSVEIzsWCyIwgG2rZgj_Dht7YIgYOq5zWHMT0jekD7LKS3uuP5ALv8s27nFmNR9UrL3yZtqnzwdwsY7-gJ_rUAlZtoz3-eFCDBM8gZww2U_fMhc1MjJ0dqYrmm5Z99V1sV2qWhzYb7cP7Uy32luBQh3_VDTwQgeFQKKmSZS6qlU3WhddRi6XEanyiD4uLaY59RdfGN82Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ ، درباره انتخابات میان‌دوره‌ای: «اگر از نظر آماری نگاه کنید، وقتی رئیس‌جمهور هستید، چه جمهوری‌خواه باشید و چه دموکرات، به دلایلی اتفاقات عجیبی در انتخابات میان‌دوره‌ای رخ می‌دهد.
فکر می‌کنم در انتخابات میان‌دوره‌ای پیروزی بزرگی به دست خواهیم آورد.»
@WarRoom</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/22919" target="_blank">📅 10:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d9f9d1ac1.mp4?token=XroIog-u8TeI7YZrWTb7U3eh1ZQi1TqfGgUhmQCUnp8qOcEepi5b7TZnS4-z2bNv8uUgTycc_nIGiskVrBNLI0LV9KwSn3rIXDrCgySQKPqdInc4nh4CKDZUnEX7XldFTYVvbuShmwNfViqiES3CUMZKekNn7Q59hfzOg37HyS4pTx_pA-NzmUcdG1VC_-112s12Q90xxAqSl6FOyBLq-PStUbX-nroEUWyIZmcIhVEdSo-i_zJlTD2Qwu_VeGPBM-Z0oYNSOiTCdH-3crvmK_shJCXSkAXsMT-M6h5i_SEbXPcxkVezu_U05OFdduSdBnzj3L6QNbjwGks9ZzNb8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d9f9d1ac1.mp4?token=XroIog-u8TeI7YZrWTb7U3eh1ZQi1TqfGgUhmQCUnp8qOcEepi5b7TZnS4-z2bNv8uUgTycc_nIGiskVrBNLI0LV9KwSn3rIXDrCgySQKPqdInc4nh4CKDZUnEX7XldFTYVvbuShmwNfViqiES3CUMZKekNn7Q59hfzOg37HyS4pTx_pA-NzmUcdG1VC_-112s12Q90xxAqSl6FOyBLq-PStUbX-nroEUWyIZmcIhVEdSo-i_zJlTD2Qwu_VeGPBM-Z0oYNSOiTCdH-3crvmK_shJCXSkAXsMT-M6h5i_SEbXPcxkVezu_U05OFdduSdBnzj3L6QNbjwGks9ZzNb8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : من عاشق سیاست هستم.
به دوستانم که در حوزه املاک یا ساخت‌وساز فعالیت می‌کنند می‌گویم؛ چون واقعاً در ساخت‌وساز و ساختن چیزها خیلی خوب بودم: «آیا در سیاست بهترم یا در ساخت‌وساز؟»
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/22918" target="_blank">📅 10:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d38f899a.mp4?token=oofc7YBWCLC8hc4bny8NE2O-40irQR-_FmAwlpkiBAutylb9ZlBAVhRVUlFC0a3PLV2wyp-lash4FXa8mAG7gbSSpoW4J0MtOxG50VyWovKY3TKJEF4286Gk1CMkH0q6x8nmkmlF68WUylLUtm7qqTalshdkZEbKF8vp9nL0WwrJW1-JNseqw6_hCbojReJwW3OPEt5qM0mDlnkI2Sb_x1gmL5hYmePBiG9Rc5irURs7vC1gUb5jFNbf0NUhwW0DRJyGKfqr-e5k9yRZo6sUHLNXdNgv-lk4oeyHmC-HvO66cXVbuSUzYWlIYqJVhG0LlnwlDWmpzLPsryu2VclMwIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d38f899a.mp4?token=oofc7YBWCLC8hc4bny8NE2O-40irQR-_FmAwlpkiBAutylb9ZlBAVhRVUlFC0a3PLV2wyp-lash4FXa8mAG7gbSSpoW4J0MtOxG50VyWovKY3TKJEF4286Gk1CMkH0q6x8nmkmlF68WUylLUtm7qqTalshdkZEbKF8vp9nL0WwrJW1-JNseqw6_hCbojReJwW3OPEt5qM0mDlnkI2Sb_x1gmL5hYmePBiG9Rc5irURs7vC1gUb5jFNbf0NUhwW0DRJyGKfqr-e5k9yRZo6sUHLNXdNgv-lk4oeyHmC-HvO66cXVbuSUzYWlIYqJVhG0LlnwlDWmpzLPsryu2VclMwIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره
آنتروپیک (شرکت سازنده هوش مصنوعی Claude؛ ترامپ مدعی است از فناوری آن برای برخی فعالیت‌های مخالف و سوءاستفاده‌های احتمالی استفاده شده است)
: «بیایید درباره آنتروپیک صحبت کنیم. آنها کاری انجام دادند که بسیار بد بود و ما آنها را متوقف کردیم. خیلی سریع متوقفشان کردیم. ما گاردریل‌هایی داریم. بزرگ‌ترین گاردریل این است که افرادی را داشته باشیم که به همان اندازه باهوش باشند؛ چون هیچ‌کس این موضوع را درک نمی‌کند، مگر اینکه ضریب هوشی بسیار بالایی داشته باشد — نه جو بایدن.»
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/22917" target="_blank">📅 10:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf8a770bd6.mp4?token=ZbZL-PPRSI350-wkVpDBPQMEH3ef4BdtD0mmShnA1QucC5vPasBahJUBdX4lTBQ2xqcWiKhUJROOBxyq0l6peeEGkd4O75WDIHX7eGQlS-Mb5xZwYT6pM_0RFVOLf7ZceLsr1WlAsOQzJ_iKY5tV8oxxq7nNJXj2jrRGacF1GiC1QZe1AwZ39c4gGwX0kLKl7HBxpHpTB0DAY7KZT-96Qs6CW2ECMf8gc2_2ZT4ChX2camWMux1tGYQmFDF84Dlbi_Y20QETOMwIRImPevBaLYGnjUPvwXn1mOXFcjGWDn4i03Zm7JSLqLNTDTzdZqMjN7t6cNRJBqIxDB-PnZSaVGhFYars-70P84SUQuFoQZxfiJJTb3KZLvGmYO5gNXIh2JiNMO3KB7lbQigKAmiyt7lKQJtKTwQIfiam0fOObOePjhAOiGToOT02tBd3IkZNykD4OFDZmbVFJhg2uSD-0siW6PqXjPBjQJ4sKye722urFvtUAijqlgLQkKBqOGmMnbW1xYsI2l_2NjTK03dXwX9lhtXs6Bc2nlmRvxX_0_Gc7IMbiNuC5F9RRcpq0-A-jsJk7ChK4fUNDl0ZrkBx_ZloEUFeM3J9BxFy2KeNTJye8tvlIkYxAMLc5VCZHVX-nNVxy5GAaf-f-5K-UirbNvQExlHiiCtN4yGaSTZaT9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf8a770bd6.mp4?token=ZbZL-PPRSI350-wkVpDBPQMEH3ef4BdtD0mmShnA1QucC5vPasBahJUBdX4lTBQ2xqcWiKhUJROOBxyq0l6peeEGkd4O75WDIHX7eGQlS-Mb5xZwYT6pM_0RFVOLf7ZceLsr1WlAsOQzJ_iKY5tV8oxxq7nNJXj2jrRGacF1GiC1QZe1AwZ39c4gGwX0kLKl7HBxpHpTB0DAY7KZT-96Qs6CW2ECMf8gc2_2ZT4ChX2camWMux1tGYQmFDF84Dlbi_Y20QETOMwIRImPevBaLYGnjUPvwXn1mOXFcjGWDn4i03Zm7JSLqLNTDTzdZqMjN7t6cNRJBqIxDB-PnZSaVGhFYars-70P84SUQuFoQZxfiJJTb3KZLvGmYO5gNXIh2JiNMO3KB7lbQigKAmiyt7lKQJtKTwQIfiam0fOObOePjhAOiGToOT02tBd3IkZNykD4OFDZmbVFJhg2uSD-0siW6PqXjPBjQJ4sKye722urFvtUAijqlgLQkKBqOGmMnbW1xYsI2l_2NjTK03dXwX9lhtXs6Bc2nlmRvxX_0_Gc7IMbiNuC5F9RRcpq0-A-jsJk7ChK4fUNDl0ZrkBx_ZloEUFeM3J9BxFy2KeNTJye8tvlIkYxAMLc5VCZHVX-nNVxy5GAaf-f-5K-UirbNvQExlHiiCtN4yGaSTZaT9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/22916" target="_blank">📅 09:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22915">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65695ba78c.mp4?token=dWWv4-pseekZ2oS0mXJmJqtAcfQv9Zw1D8-ZxlSPpDVv5OstVdBt5UtigbkscPlGmPAEWnGAah8ueGI8nBUPf71DWdPFBObzj2UGWNroUoG2iZ2ehbvJ9M1jIu1xnDd9otYMAuLwtmygmCJukO47Li9RzLUpJZ1agfNP7AVgOtzVAvwIF-AA3oA3KsFqIJsC8oO7M2UydALvKuhmRzWJ6ZMMdg6j4O8dpYjH1z85yH5HPRxpoyxkyWtOzPdJw-QM0EWfXchC8ICV_VPMCCLYJeDQIw8ai-032-t523849T20F-zfPv5VR2MQiS5B1aCYz8phHyJXpMVfm83EFb4MYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65695ba78c.mp4?token=dWWv4-pseekZ2oS0mXJmJqtAcfQv9Zw1D8-ZxlSPpDVv5OstVdBt5UtigbkscPlGmPAEWnGAah8ueGI8nBUPf71DWdPFBObzj2UGWNroUoG2iZ2ehbvJ9M1jIu1xnDd9otYMAuLwtmygmCJukO47Li9RzLUpJZ1agfNP7AVgOtzVAvwIF-AA3oA3KsFqIJsC8oO7M2UydALvKuhmRzWJ6ZMMdg6j4O8dpYjH1z85yH5HPRxpoyxkyWtOzPdJw-QM0EWfXchC8ICV_VPMCCLYJeDQIw8ai-032-t523849T20F-zfPv5VR2MQiS5B1aCYz8phHyJXpMVfm83EFb4MYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
جنگ ایران بعد از انتخابات میان‌دوره‌ای به پایان خواهد رسید.
سؤال:
اگر جمهوری‌خواهان شکست بخورند، چرا جنگ تمام خواهد شد؟
ترامپ:
خیلی‌ها فکر می‌کنند اگر ما شکست بخوریم، من فقط عصبانی‌تر می‌شوم و خودم کار را یکسره می‌کنم، می‌دانید؟
در هر صورت، آنها بازنده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22915" target="_blank">📅 09:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وال‌استریت ژورنال: مقام‌های آمریکایی می‌گویند
ایران پیش از حمله موشکی ۱۷ ژوئیه به پایگاه موفق‌السلطی اردن، که به کشته‌شدن سه نظامی آمریکایی منجر شد، به تصاویر ماهواره‌ای چینی با وضوح بالا از این پایگاه دسترسی داشته است.
این تصاویر پیش و پس از حمله در اختیار ایران قرار گرفته و به تهران برای شناسایی دقیق اهداف کمک کرده‌اند. مقام‌های آمریکایی نام شرکت‌های چینی را اعلام نکرده‌اند و
دولت چین را مستقیماً به مشارکت در این حمله متهم نکرده‌اند
؛ پکن نیز خواستار ارائه شواهد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22914" target="_blank">📅 09:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تعطیلی مرز مهران تکذیب شد
‌فرماندار مهران: مرز مهران باز است و فعالیت‌های مسافری و گمرکی در این مرز برقرار است و هیچ‌گونه تعطیلی یا توقفی در روند فعالیت مرز با کشور عراق وجود ندارد. طی شبانه‌روز گذشته ۱۷ هزار نفر از این مرز تردد داشته‌اند که نشان‌دهنده استمرار فعالیت بخش مسافری مرز مهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22913" target="_blank">📅 09:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">العربیه : نخست وزیر عراق پس از حمله شبه‌نظامیان هوادار ایران به عربستان سعودی، گذرگاه‌های مرزی شلمچه، شیب و مندلی را با ایران بستند. احتمال می‌رود تسلیحاتی که برای هدف قرار دادن عربستان به کار رفته‌اند، از طریق یکی از این گذرگاه‌ها از ایران به عراق منتقل شده باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22912" target="_blank">📅 03:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فاکس نیوز از عرشه ناو هواپیمابر:  «یو‌اس‌اس جرج واشینگتن» روز جمعه ۱۱ سپتامبر در جریان استقرارش برای نبرد با جمهوری اسلامی آماده می‌شود.
این ناو هواپیمابر که حدود ۵۰۰۰ ملوان را در خود جای داده و توسط ناوشکن‌ها اسکورت می‌شود، آخر هفته گذشته هدف حمله موشک‌های بالستیک ایران قرار گرفت؛ این در حالی است که در طول هفته جاری نیز چندین مورد تبادل آتش میان طرفین رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22911" target="_blank">📅 02:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رویترز: نفت در پایان هفته بالای ۱۰۰ دلار ماند.
برنت در پایان معاملات جمعه روی
۱۰۴٫۶۱ دلار
بسته شد و نفت آمریکا به
۱۰۰٫۰۵ دلار
رسید؛ نفت برای این هفته بیش از
۸ درصد
رشد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22910" target="_blank">📅 01:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22909">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">به مناسبت بیست و پنجمین سالگرد حملات ۱۱ سپتامبر، سازمان اطلاعات مرکزی آمریکا (سیا) ۶۹ سند اطلاعاتی محرمانه را منتشر کرد؛ اسنادی که در سال‌های منتهی به این حمله تروریستی در اختیار بیل کلینتون و جورج دبلیو بوش، رؤسای جمهور وقت، قرار گرفته بود. در میان این اسناد، هشداری مورخ ۱۰ سپتامبر ۱۹۹۸ به چشم می‌خورد که بیان می‌داشت القاعده «ممکن است هواپیمایی مملو از مواد منفجره را به یکی از شهرهای آمریکا بکوبد.» این اسناد یافته‌های کمیسیون تحقیق سال ۲۰۰۴ را تأیید می‌کنند و نشان می‌دهند که نهادهای اطلاعاتی به‌طور مداوم درباره نیات القاعده هشدار داده بودند. با این حال، مقامات اطلاعاتی اذعان کردند که این هشدارها نتوانسته بود ابعاد کامل فاجعه برنامه‌ریزی‌شده را به‌درستی منعکس کند. جان رتکلیف، رئیس سیا، اظهار داشت: «بیست و پنج سال پیش، حملات ۱۱ سپتامبر ضربه‌ای به ملت ما وارد کرد، اما نتوانست ما را درهم بشکند.»
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22909" target="_blank">📅 01:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22908">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سخنگوی وزارت خارجه:
منشا حمله آمریکا به لامرد، خاک یکی از کشورهای جنوبی حاشیه خلیج فارس بوده است.
عربستان، ژاپن و اردن تبعات رای‌ مثبت خود به قطعنامهٔ ضدایرانی آژانس را خواهند دید و ما آن‌ها را پاسخگو خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22908" target="_blank">📅 00:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سنتکام : در اعمال محاصره ایالات متحده علیه ایران تا امروز ، نیروهای آمریکایی
مسیر ۹۹ کشتی تجاری را تغییر داده‌اند(۳ کشتی جدید فقط امروز)
تا از رعایت کامل مقررات اطمینان حاصل کنند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22907" target="_blank">📅 23:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مقام اسرائیلی در گفتگو با کانال ۱۲  : تسلط حوثی‌ها بر تنگه باب‌المندب به دلیل عرض بسیار کم مسیر کشتیرانی و امکان هدف قرار دادن مستقیم کشتی‌ها با موشک‌های ضدزره بدون نیاز به سامانه‌های پیچیده راداری، تهدیدی خطرناک‌تر از وضعیت کنونی در تنگه هرمز محسوب می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22906" target="_blank">📅 23:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ تلفنی ، درباره ایران: اگر نمی‌خواهید کاری را که من انجام می‌دهم انجام دهید،
آن‌ها به سلاح هسته‌ای دست پیدا خواهند کرد.
اگر من یک سال و نیم پیش با بمب‌افکن‌های بی-۲ آن‌ها را به‌شدت بمباران نکرده بودم،
آن‌ها همین حالا سلاح هسته‌ای داشتند و از آن استفاده می‌کردند.
اسرائیل از بین می‌رفت و خاورمیانه نابود می‌شد. شما این را از این واقعیت می‌بینید که ایران آن همه موشک شلیک کرد. مردم، از جمله عربستان سعودی، واقعاً شوکه شده بودند که ایران به‌جای آن موشک‌ها، ممکن بود از یک سلاح هسته‌ای استفاده کند
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22905" target="_blank">📅 23:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">لایو جنگ یمن در گوگل مپ
https://goo.gl/maps/LkwoDWLT38cUL1mVA?withYashar
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22904" target="_blank">📅 23:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdiMSRHT33eXlh16r9TLv2FmR3UdkJhK2u9-ZhMOI7Ebva1ZkJ-jmDOo6_U3k2ItmZnzzf9yG1frlICfa90mpNgogMe_ZhkR-0zc1NDqvtBwGIj4gTwnm5-qDBAQgwAyvLYY7yB1zvLfhejCcHxv2WDi1ZIUl6eWEnDFJ-mD7p6ayEoHxRdZt8rL1bkVRqa20lmwPSAaZFMgKKnBHVjmRYJP003gaqKLkHFEPmZuM8grVCAkXp3qbotTEDQiMx_vXgTdb69HRlm79FiO0NBGz_856EeONfqI-KFnvDM9CY2BYIyUObVDHx1KZ6_hI85ZjsCFJshY1N_kBB4PFmYwKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22903" target="_blank">📅 22:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">روزنامه معاریو: نتانیاهو پیشنهاد حمله نظامی مشترک با کشورهای عربی به انصارالله یمن را داده است
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22902" target="_blank">📅 22:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22901">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ: ما انتخاب دیگری نداریم،
باید سخت با ایران برای پیروزی بجنگیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22901" target="_blank">📅 21:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏رضا نجفی، نماینده جمهوری اسلامی در آژانس بین‌المللی انرژی اتمی، به شبکه سی‌جی‌تی‌ان گفت: آمریکا ممکن است از قطعنامه اخیر شورای حکام به‌عنوان زمینه‌ای برای تشدید درگیری یا اقدام نظامی جدید علیه جمهوری اسلامی استفاده کند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22900" target="_blank">📅 21:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏نیروهای مسلح دولت یمن اعلام کردند در جبهه شرقی و منطقه نظامی سوم، با استفاده از توپخانه و تک‌تیراندازان، نیروها، مواضع و انبارهای حوثی‌ها را هدف قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22899" target="_blank">📅 21:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏تانکرترکرز گزارش داد برای نخستین بار در دو ماه گذشته، مجموع صادرات نفت خام عراق، کویت، عربستان سعودی، قطر، امارات متحده عربی و عمان از خط محاصره آمریکا به‌طور میانگین از ۱۰ میلیون بشکه در روز عبور کرده است.
‏بر اساس این گزارش، صادرات نفت خام ایران همچنان صفر است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22898" target="_blank">📅 21:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏ارسالی : ساواکیهای اخموی جذاب اگه توهماتتون  با ای آی تموم شد یه فکری بحال انداختن رژیم بفرمایید
‏مملکت به معلم و نانوا و تراشکار و مشاغل دیگه هم نیاز داره!!!!!
‏یادتون نره ساواک یه
**
مثل پدر مهران غفوریان هم داشت
‏یادتون نره هسته وزارت اطلاعات رژیم رو همون ساواکیهای خائن به شاه پی ریزی کردن
یاشار جان فروارد نشه
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22897" target="_blank">📅 21:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22896">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22896" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وال‌استریت ژورنال: یک گروه مرتبط با ایران از مدل هوش مصنوعی آمریکایی «کلود» برای ردیابی و هدف‌گیری ناوهای جنگی آمریکا استفاده کرد. بر اساس گزارش شرکت آنتروپیک، این گروه با کمک کلود اطلاعات مربوط به ترانسپوندر کشتی‌ها و هواپیماها، تصاویر نظامی و تصاویر ماهواره‌ای تجاری را جمع‌آوری و تحلیل کرده و برای شناسایی موقعیت و نقاط آسیب‌پذیر ناوهای آمریکایی در خاورمیانه به کار گرفته است. آنتروپیک اعلام کرد این عملیات را شناسایی و متوقف کرده و حساب‌های مرتبط را مسدود کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22895" target="_blank">📅 21:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سخنگوی نیروهای دولت یمن: نیروی هوایی، عملیات بمباران منطقه "صندوق مرگ" را که پیش از این اعلام شده بود، آغاز کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22894" target="_blank">📅 20:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارش پرتاب از سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22893" target="_blank">📅 20:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سی‌ان‌ان گزارش داده که در پی مشاهده دود و آثار انفجار در نزدیکی خط لوله راهبردی شرق–غرب عربستان در جنوب‌شرقی مدینه، احتمال می‌رود این خط لوله هدف حمله قرار گرفته باشد. این خط لوله نفت خام را از مناطق نفت‌خیز شرق عربستان به بندر ینبع در ساحل دریای سرخ منتقل می‌کند و با توجه به اختلال در تردد نفتکش‌ها از تنگه هرمز، اهمیت آن برای صادرات نفت عربستان افزایش یافته است. منابعی در گزارش‌ها احتمال نقش
حوثی‌های یمن
در این حمله را مطرح کرده‌اند، اما عربستان تاکنون وقوع حمله به خط لوله را به‌طور رسمی تأیید نکرده است. تصاویر ماهواره‌ای نیز وجود دود در نزدیکی مسیر خط لوله را نشان می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22891" target="_blank">📅 20:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22890">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">احساس همدردی مردم ایران بعد از شنیدن خبر حمله تروریستی به برج های تجارت جهانی نیویورک در ۱۱ سپتامبر … که امروز سالروزش است ، خودم هیچوقت اون روز رو یادم نمیره @WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22890" target="_blank">📅 20:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">روزنامه عبری معاریو: حزب‌الله تلاش دارد از نبرد علی‌الطاهر، روایتی از قهرمانی شبیه نبرد کربلا بسازد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22889" target="_blank">📅 20:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22888">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حتما تا آخر گوش کنید موتورم روشن شد</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22888" target="_blank">📅 19:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22887" target="_blank">📅 19:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSemoyami SMYM</strong></div>
<div class="tg-text">ولی یاشار اگه بهت بگن با یه بمب اتم تو یه شهر کار این نظام تمومه تو حاضری این اتفاق بیفته</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22886" target="_blank">📅 19:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22885">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ستاد کل نیروهای مسلح اوکراین⁠ گزارش داده نیروهای اوکراینی بندر تجاری مخاچ‌قلعه در داغستان را هدف قرار دادند؛ در این حمله در محدوده بندر آتش‌سوزی ثبت شد و میزان خسارت در حال بررسی اعلام شد. این بندر تنها بندر عمیق‌آب و بدون یخ روسیه در دریای خزر و
یکی از مراکز مهم کریدور لجستیکی روسیه و ایران است که بنا بر اعلام اوکراین، در آن مسیر قطعات و پهپادهای شاهد از ایران به روسیه و مهمات، مواد منفجره و قطعات پهپاد در مسیر معکوس جابه‌جا می‌شوند.
همزمان، اوکراین اعلام کرد در حمله به نووروسیسک، سه شناور روسی شامل ناوچه
آدمیرال اسن، کشتی آبی‌خاکی پیوتر مورگونوف و مین‌روب ژلزنیَکوف
آسیب دیده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22885" target="_blank">📅 19:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فرانس‌پرس: حوثی‌ها با کمک هوش مصنوعی برای ساخت موشک‌های هدایت‌شونده تلاش کرده‌اند.
شرکت آنتروپیک اعلام کرده یک گروه مستقر در شمال یمن از هوش مصنوعی «کلود» برای طراحی سامانه هدایت، ناوبری و کنترل یک راکت هدایت‌شونده، یک موشک بالستیک چندمرحله‌ای با برد هدف بیش از
۲ هزار کیلومتر
و یک موشک با طرح سرجنگی گلاید هایپرسونیک استفاده کرده است. این شرکت می‌گوید شواهدی از عملیاتی‌شدن این تسلیحات ندارد، اما یک راکت هدایت‌شونده آزمایش شده است. با توجه به محل فعالیت و ارتباط این گروه با حوثی‌ها، احتمال می‌رود این افراد وابسته به حوثی‌ها بوده باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22884" target="_blank">📅 19:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f58f12cf8.mp4?token=CMSa-YlOc1f7Va8_aDt3NVOcJBV98mubLj2fzGNu1qgrBlfTBb8ol19eKQOnuZlyGtFY9_EjecQZPY2SP0VgkOs3-_E_2xZ6gn-iEJvYD3RbxBRI92oMfG9QtLOBpnvFPXCofmVVkAiBsU8pgNJtmKraimexKH-5VL-zcZ8eVlEUhXFHDRVFtNTn_Fk4A0Vw1V5tGtxn62kb9CSI8cugQLoS4Zv_NGrYjImwvq8dFvv5twpAMz750isQEIpB-Zmh0yLpdDEgUahwkxiqjc6fZDrx4Zpv-BOlALFbAZBtKTDTQ0qKs-Ma9puqUCCXcBZYhl7jFsMKvvdKquHLf8zDbYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f58f12cf8.mp4?token=CMSa-YlOc1f7Va8_aDt3NVOcJBV98mubLj2fzGNu1qgrBlfTBb8ol19eKQOnuZlyGtFY9_EjecQZPY2SP0VgkOs3-_E_2xZ6gn-iEJvYD3RbxBRI92oMfG9QtLOBpnvFPXCofmVVkAiBsU8pgNJtmKraimexKH-5VL-zcZ8eVlEUhXFHDRVFtNTn_Fk4A0Vw1V5tGtxn62kb9CSI8cugQLoS4Zv_NGrYjImwvq8dFvv5twpAMz750isQEIpB-Zmh0yLpdDEgUahwkxiqjc6fZDrx4Zpv-BOlALFbAZBtKTDTQ0qKs-Ma9puqUCCXcBZYhl7jFsMKvvdKquHLf8zDbYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما به نیروهای نظامی‌ای که همین الان مشغول خدمت هستن و تلاش می‌کنن مطمئن بشن بزرگ‌ترین حامی تروریسم در جهان، یعنی جمهوری اسلامی ایران، هرگز و تحت هیچ شرایطی به سلاح هسته‌ای دست پیدا نکنه، ادای احترام می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22883" target="_blank">📅 18:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e269d57611.mp4?token=fdIP40ebb96atlvZr_vNK4ADclUFcNuXn7y1cNYAKQMEgyzhSIO6mCKTIyzM3zHc9UmIGC3JzCSRdH6e0LpyfGjmhp0POCSvBFSczcd3vY_mrKi8Xxk_CebvfGjQK7XLVqUGS0PgQKwpVyeVoNVWQy5j5ecpc4xHiHOsIAEHa87SsCkzsY2eybB7EJc5PwVrfeyj3dP37bYD1tPxobk8f-a0jOC3Di_gqsHUafKaIBtwD-2kyJuGucynPHCvz-peABYy9QX615PvXari81PjOgwshZxq_88kIdktyZOETL9cb47NriFtAuGN0zsksmOn4AN5KjnhsDPPjMZUl8_k-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e269d57611.mp4?token=fdIP40ebb96atlvZr_vNK4ADclUFcNuXn7y1cNYAKQMEgyzhSIO6mCKTIyzM3zHc9UmIGC3JzCSRdH6e0LpyfGjmhp0POCSvBFSczcd3vY_mrKi8Xxk_CebvfGjQK7XLVqUGS0PgQKwpVyeVoNVWQy5j5ecpc4xHiHOsIAEHa87SsCkzsY2eybB7EJc5PwVrfeyj3dP37bYD1tPxobk8f-a0jOC3Di_gqsHUafKaIBtwD-2kyJuGucynPHCvz-peABYy9QX615PvXari81PjOgwshZxq_88kIdktyZOETL9cb47NriFtAuGN0zsksmOn4AN5KjnhsDPPjMZUl8_k-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر هگست وزیر جنگ:
تنگه را ما کنترل می‌کنیم و این نبرد را نیز تمام خواهیم کرد!
تاریخ به پایان نرسیده بود؛ هیچ‌وقت هم به پایان نمی‌رسه. مبارزه با شر ادامه داشت و الان هم ادامه داره.
و این مبارزه تا روز قیامت ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22882" target="_blank">📅 18:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cc98c2628.mp4?token=BVq19ZwNwCiSPZPak3rVFymXWPjGrCwRq8Q5KGZ4aXIRHoDhjKeQWyPV01eGuLR-N7uLdhpn4yPXfvHqN01CEu3ifBPWZWnzUCxe77VvKQDlmJTU4_8GFQl6_xq7ujF-2KQkIJJwS5C-fhJOLFcRr3zSlRdmJsmIeBoGD1a_AcNZWOVc_pNWpVZ7fpGM9BNjHifYblwc09XH0C_JYuXe5VgpgRSy047lM7kcq2TOCmMRn6PCfUuEOM2vTFhr4yBYa1GUE9K_oVQVf9DU9xqJfNNquHP3ApAY9DBWq5W_Y9f7BpoP2SHPludAmZpFK5Rg2aBP9_jpx4NB9rvx-Yp1yDtGKzNbj9UWtwMYkRMeGpoBAD2UgPlCSrh59oN6O28-bFKNFbc_9EP0X7gGuMbYMX-EyP-kWo-EEcRAJL-yiZf6q7XiL5avEnYHWilsJrsxTDiFs_Q_NygznafYTSvvcn7OJTOkZJHC4AWBr2-DBdbJnnSQKjjXgCQmPn8zEKO-9BFvDjBtQbrJjGzfQGdvT5uua6y-hifVxQ1UBlC_Y2VrDHAOEVFPfRUJFsLiLqqEiruuHtOaAAn9nPJ3CAjrkmg97fdqGZ5GfQZomzKnroTSLjXlgsQXkIhNdP5q-u8hLlhso084tPFth3KJA_7aF6iXs8A5sO2OeuI5n_y2ssI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cc98c2628.mp4?token=BVq19ZwNwCiSPZPak3rVFymXWPjGrCwRq8Q5KGZ4aXIRHoDhjKeQWyPV01eGuLR-N7uLdhpn4yPXfvHqN01CEu3ifBPWZWnzUCxe77VvKQDlmJTU4_8GFQl6_xq7ujF-2KQkIJJwS5C-fhJOLFcRr3zSlRdmJsmIeBoGD1a_AcNZWOVc_pNWpVZ7fpGM9BNjHifYblwc09XH0C_JYuXe5VgpgRSy047lM7kcq2TOCmMRn6PCfUuEOM2vTFhr4yBYa1GUE9K_oVQVf9DU9xqJfNNquHP3ApAY9DBWq5W_Y9f7BpoP2SHPludAmZpFK5Rg2aBP9_jpx4NB9rvx-Yp1yDtGKzNbj9UWtwMYkRMeGpoBAD2UgPlCSrh59oN6O28-bFKNFbc_9EP0X7gGuMbYMX-EyP-kWo-EEcRAJL-yiZf6q7XiL5avEnYHWilsJrsxTDiFs_Q_NygznafYTSvvcn7OJTOkZJHC4AWBr2-DBdbJnnSQKjjXgCQmPn8zEKO-9BFvDjBtQbrJjGzfQGdvT5uua6y-hifVxQ1UBlC_Y2VrDHAOEVFPfRUJFsLiLqqEiruuHtOaAAn9nPJ3CAjrkmg97fdqGZ5GfQZomzKnroTSLjXlgsQXkIhNdP5q-u8hLlhso084tPFth3KJA_7aF6iXs8A5sO2OeuI5n_y2ssI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احساس همدردی مردم ایران بعد از شنیدن خبر حمله تروریستی به برج های تجارت جهانی نیویورک در ۱۱ سپتامبر … که امروز سالروزش است ، خودم هیچوقت اون روز رو یادم نمیره
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22881" target="_blank">📅 18:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22880">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f47e9c912.mp4?token=snbm_n1VQr1V6WelUqg7Rn_YNuGxt5bMEHFqwIRmTjeS4xuGmkcRxUh3vjKyHl8QQQ_jMctVIu3cUdTciYgC_1GvlSCSG3BfGzHGSNQI7WAJ1ziTF7Qm99Ppn0n0CA2NeqkOZ18Z9vNwI8TQmxJ6YPKcnjRUR1jvvkBowRCI8M9SKDcE5o-1nsyJ-29ttIaJlenjnKS4rhcCvUXB-NHcqLKfR83_mY4eC-_vwuJtxJgbKoUG9qDMif14Pnb5gPlGAJSmVXoj28vxgx-gsYFGEIplBzQzCggn21WlPmFPQrGvu9AzSxrxtVWSPLvNrugDeDKyxTOLakZRWAW8RuH0kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f47e9c912.mp4?token=snbm_n1VQr1V6WelUqg7Rn_YNuGxt5bMEHFqwIRmTjeS4xuGmkcRxUh3vjKyHl8QQQ_jMctVIu3cUdTciYgC_1GvlSCSG3BfGzHGSNQI7WAJ1ziTF7Qm99Ppn0n0CA2NeqkOZ18Z9vNwI8TQmxJ6YPKcnjRUR1jvvkBowRCI8M9SKDcE5o-1nsyJ-29ttIaJlenjnKS4rhcCvUXB-NHcqLKfR83_mY4eC-_vwuJtxJgbKoUG9qDMif14Pnb5gPlGAJSmVXoj28vxgx-gsYFGEIplBzQzCggn21WlPmFPQrGvu9AzSxrxtVWSPLvNrugDeDKyxTOLakZRWAW8RuH0kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، حملات 11 سپتامبر را با جنگ خود علیه ایران مرتبط دانست: ما هرگز این واقعه را فراموش نخواهیم کرد. به همین دلیل است که امروز می‌جنگیم.
ما هیچ انتخابی نداریم. تنها نتیجه ممکن، پیروزی است
ایران بزرگترین حامی دولتی تروریسم در جهان است و هرگز به سلاح هسته‌ای نخواهد رسید
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22880" target="_blank">📅 18:08 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
