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
<img src="https://cdn4.telesco.pe/file/RcNWJov13IRwYWKvNLtkRKXmHoK2PuJsOyDHUXwV5gJejWWv8cEh3hw-UE5p36v6HCnSH7Ozv7imNkbGJWIfvnMa-3Q2gmZI4eKURg42ZCzKTTKBaYa67edaOxHbZpI9IrrIYLDEsvd-kQ9Fa-f0CrpVtC-X2kxBYR10anlhBftsW3H1UweAdv8XumWhg3-1KaytA4llOoz2L3P_MG4bPMBR0g0fn_un0hoAjRa14T_xIziJ0EDvFzOLgdoifsGvRhG-4JyN88-YlFYXslv20CI5mcB2cHSxHqFUIEJpra9977P7wvazA0n82IKR0ePuLlNByLFR_nNsIrGSyNH4aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 411K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 15:41:04</div>
<hr>

<div class="tg-post" id="msg-18856">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آکسیوس: آماده‌باش هوایی آمریکا برای تشدید جنگ با ایران آغاز شده است
آمریکا تعداد سوخت‌رسان‌های خود را به سطح مشابه آغاز جنگ خواهد رساند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/withyashar/18856" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18855">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj_8nQ1X9Zgjw2IYHDdJwD3tXaPglg-ETafPlRqphp7wH4gX7IIMvKqbcYNNbyVQ7Ib8khwsI91uX3zMaAQkmrNDZN6OjqHAzdX131i_IKpVsA03Vri3JYrL9OrBabrc6gmRHx4hcteYBFfrDNu199GFrCSEKSTWU9iSVusjX1UGWYU01jv11JVTp2sAY7BHT6zSgxiNL7pgl35BA_-qPsj0cNqWqPBQrRRsbiZwYdi1oYYqZ7DvOYz7NhROPysWd1FCJ4zGiVqK4wgbVbBXVsnaWOxG-E18Ce_5bAcUBQu8jvshS9RzR3e2-ubdzJ7enlvpYkk61Ubeo21sw8C95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :جمهوری‌خواهان باید ایران را به لایحه تحریم‌های روسیه اضافه کنند. این کاری بود که لیندسی می‌خواست انجام دهد و قرار بود اتفاق بیفتد. مهم!!!
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/withyashar/18855" target="_blank">📅 15:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18854">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/770115730a.mp4?token=lBMui_ajFdPNGjrRZt4WNFt7rsLfNQH_gBpgZf6wKPeHD4hSREoXKcD6DS48p5oeF-2iXKgMNAAiXb2eJRoFZehODj3xbwfoTbA5_xk1v8fa0N3Qb7xiHAaYJs-0pEt6a4FYg0coQOOZlE17cVY1AYKJDIqgIuKzOVem_IFnaMjS1CdL7QVUA3nIsZ8ZETtCtbupKK1VKaoW6aDv2-tve3D4ZyyYSWGR8uz7Wws7yKQXBXw8hyZTgT9DHbAsJKeyVO9vUUbLAPA6OjPOURz0RSimtwP7932YLrLFLkU0HGij89hsEYYEBpkvH8_giv300V0V0LKarEOSZNdkY1zJrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/770115730a.mp4?token=lBMui_ajFdPNGjrRZt4WNFt7rsLfNQH_gBpgZf6wKPeHD4hSREoXKcD6DS48p5oeF-2iXKgMNAAiXb2eJRoFZehODj3xbwfoTbA5_xk1v8fa0N3Qb7xiHAaYJs-0pEt6a4FYg0coQOOZlE17cVY1AYKJDIqgIuKzOVem_IFnaMjS1CdL7QVUA3nIsZ8ZETtCtbupKK1VKaoW6aDv2-tve3D4ZyyYSWGR8uz7Wws7yKQXBXw8hyZTgT9DHbAsJKeyVO9vUUbLAPA6OjPOURz0RSimtwP7932YLrLFLkU0HGij89hsEYYEBpkvH8_giv300V0V0LKarEOSZNdkY1zJrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی
در
انبار گرانول مراغه
…
@WarRoom</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/withyashar/18854" target="_blank">📅 15:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18853">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USjGU0PQVAxZyXuNWAsKG0_7drT21x19hMFyPg5QJAPqwvUL6-0-PZ9BilCzHw1LrNjjdXpURNfTpb_p-bnyLytRTfz5rCMcXdqpjIAL3D0SIqnnZe0qnQ9mxJpjBbxsgTNIs7wYxH2_-6F_ajVv2LQZd81tZiJvFX3fOkR4qwiIa_Ay97FXWKIfv2kioGzmZ6_fC0QHDA5fsRWV2Szf8neRFGbmwnl0DO6yuVi-IljJ3TQSHjFxx_cHFJazbBKk9aNyWHxh6bIUGk267a9yYPzhhfdHUlklNBrvFM7-v5gNnoFIAOusQu3CPbI6sgFOOcQS1XxjvIL7YSDkrET_tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهروند ایرانی/آمریکایی ممنوع خروج شده که ترامپ اداعی آزادی و رژیم تکذیب کرد با نام دنا کراری بعد از 566 روز به آمریکا رسید
کراری، ۵۳ ساله ساکن کالیفرنیا، برای دیدار با خانواده به شیراز سفر کرده بود که گذرنامه‌اش توسط مقامات جمهوری اسلامی ضبط و از امکان خروج از کشور محروم شد. به گفته وکیلش، او هرگز رسماً زندانی نشد، اما تحت بازجویی‌های شدید و مکرر توسط سازمان‌های امنیتی قرار گرفت و در چند ماه گذشته تحت شرایط بسیار محدودکننده‌ای قرار گرفت.مقامات امنیتی کراری را به «همکاری با یک کشور متخاصم» و «جاسوسی» متهم کرده‌بودند
وی به عنوان کارمند در شرکت امنیت سایبری پالو آلتو نتورکز کار می‌کرد. او در کنار حرفه فنی خود، بنیانگذار یک سازمان خیریه حمایت از کودکان محروم بنام فرزندان مهر را نیز مدیریت می‌کرد
@WarRoom</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/18853" target="_blank">📅 15:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18852">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYDLsaCecx3G6eh70xzeUR5NKUY-foj8hdKsvY8hgzW985bpkUQAzmV5nFkMXsJyUGgxO2B7NivcJL5i5VDmUo_iC88FRyDMk7jsv9UxMttSvS7VGWIumLIfEuAsICJPr1yHMtFd9BErMiAGsUwh92fhZzUCuk70gceVHPwRBZxviWihd5igtcpKcTKMDmBBousMWrX9ShKmk9ABP8-C8nXNBbM6MJ-G2yUU24yEeWO53HtvLJrtpLamdWLRCnB8DOSxE9sl9fW5QB32phCY4L3Z1QOYQ88Z-ckOI3ieCgsIk7yLPovNuRv5Eb74AG5OulvApLEX7Z-ErfBZOVUO9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه هسته‌ای شهر دارخوین با نام های(کارون یا استقلال) در استان خوزستان، در ساحل رود کارون و حدود ۷۰ کیلومتری جنوب اهواز، در زمینی حدود
۵۰ هکتار
در حال ساخت است. این نیروگاه یک راکتور آب سبک تحت فشار (PWR) با ظرفیت حدود
۳۰۰ مگاوات
دارد که طراحی آن توسط متخصصان ایرانی انجام شده و ساخت آن توسط
شرکت
انرژی اتمی ایران
با مشارکت
گروه مپنا
و شرکت‌های داخلی دنبال می‌شود. عملیات اجرایی آن از
آذر ۱۴۰۱
آغاز شده، هزینه پروژه حدود
۲ میلیارد دلار
برآورد می‌شود و طبق برنامه قرار بود طی
۸ سال
حدود
سال ۲۰۳۰
تکمیل شود. این سایت زمان شاه نیز قرار بود میزبان دو راکتور ساخت شرکت فرانسوی
Framatome
باشد، اما آن طرح متوقف شد
@WarRoom</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/18852" target="_blank">📅 14:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18851">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سازمان انرژی اتمی ایران: ما حمله آمریکا به تاسیسات هسته‌ای دارخوین در خوزستان را که هنوز در حال ساخت است، محکوم می‌کنیم. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/18851" target="_blank">📅 14:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18850">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سازمان انرژی اتمی ایران: ما حمله آمریکا به تاسیسات هسته‌ای دارخوین در خوزستان را که هنوز در حال ساخت است، محکوم می‌کنیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/18850" target="_blank">📅 14:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18849">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مجری : دست فرمون شما ما رو رسوند به جنگ  خلاصه گفتگو با سید عباس عراقچی  @WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18849" target="_blank">📅 13:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18848">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نیروی دریایی سپاه: ساعاتی پیش، چهار فروند کشتی متخلف، با حمایت آمریکا، با ایجاد اختلال در سیستم‌های ناوبری و بی‌توجهی به هشدارهای مرکز کنترل تنگه هرمز متعلق به نیروی دریایی سپاه، قصد ایجاد اختلال در تردد و خروج از تنگه هرمز از طریق یک مسیر ناامن را داشتند. دو فروند از این کشتی‌ها دچار حادثه شده و متوقف شدند، در حالی که دو فروند دیگر از ادامه مسیر منصرف شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18848" target="_blank">📅 13:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18847">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اختلال در اینستاگرام / واتس آپ ، به گیرنده های خود دست نزنید مشکل از مرکز است
@WarRoom
⚠️
⚠️</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18847" target="_blank">📅 12:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18846">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گزارش‌ تایید نشده ، 4 کشتی در بندر شهید رجایی، هدف حمله قرار گرفتن @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18846" target="_blank">📅 12:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18845">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارش انفجار در اربیل عراق ، مقر کردها
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18845" target="_blank">📅 11:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18844">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش‌ تایید نشده ، 4 کشتی در بندر شهید رجایی، هدف حمله قرار گرفتن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18844" target="_blank">📅 11:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18843">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آلارم حمله موشکی در ‌بحرین فعال شد
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18843" target="_blank">📅 11:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18842">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ادعای اسرائیل هیوم:مجتبی خامنه‌ای از ایران متواری شده  @WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18842" target="_blank">📅 11:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18841">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ادعای اسرائیل هیوم:مجتبی خامنه‌ای از ایران متواری شده
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18841" target="_blank">📅 11:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18840">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نیویورک‌تایمز:دولت ترامپ نگران است که افراط در استفاده از تحریم‌ها علیه روسیه، کشورهای بیشتری را به روی گرداندن از دلار آمریکا ترغیب کند؛ در نتیجه اقدام به کاهش برخی از تحریم‌ها علیه مسکو کرده
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18840" target="_blank">📅 11:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18839">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0163277b0.mp4?token=oHaTdD6c6Z2hF1mAh89NfRaSisn81PfTmHJf14o2Xr9y7Xt9YgEqUhaI2enO6URA8PUH8V4K9zTEszGBZT7As6r20cc_sDDWGNVtB_7RW_U4-N42Z0kXG76f3aVtKTb2mKPuuaa7krfg9m3gMYOZh1a16dxh0v5hB3-G7nPTNe-Y0njee3JwTWzOvyD0ntci0XjJQ-Cfn0jkzZDEPtkf5dMC60GbJalMYGzmrV0FK2oCl3XKIqKjCOuTB7MeFStDOT7cojaYhCDTmhbPdqH0y4_xzFGqwtAnIMDSErEdlUETQKK0zHrXGKkBi_5EDtagAiQ8reMjhJJ0L2FKKTtbdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0163277b0.mp4?token=oHaTdD6c6Z2hF1mAh89NfRaSisn81PfTmHJf14o2Xr9y7Xt9YgEqUhaI2enO6URA8PUH8V4K9zTEszGBZT7As6r20cc_sDDWGNVtB_7RW_U4-N42Z0kXG76f3aVtKTb2mKPuuaa7krfg9m3gMYOZh1a16dxh0v5hB3-G7nPTNe-Y0njee3JwTWzOvyD0ntci0XjJQ-Cfn0jkzZDEPtkf5dMC60GbJalMYGzmrV0FK2oCl3XKIqKjCOuTB7MeFStDOT7cojaYhCDTmhbPdqH0y4_xzFGqwtAnIMDSErEdlUETQKK0zHrXGKkBi_5EDtagAiQ8reMjhJJ0L2FKKTtbdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رسانه‌ی فرانسوی با انتشار این ویدیو نوشت:
‏زنان ایرانی در نزدیکی بندرعباس در جنوب ایران گرد هم آمده‌اند تا خبر حملات هوایی جدید علیه رژیم اسلامی را جشن بگیرند.
‏آن‌ها پیام زیر را خطاب به آمریکا فریاد می‌زنند:
‏«ادامه بده. کارِت عالیه»
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18839" target="_blank">📅 11:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18838">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e681b632df.mp4?token=f3ylE0cqo6MgyV9UkXFb65eqGP4a-72SCjdtCcyQpm9p-d7BYbTl9naiDfGbVn9flLAfC7NIwSFhw-tiE5g3YXNHUZ64dnlVvqNot7XaQEUwqye6yCN4DyF6MjAc6rZVeGSWALJ9xdNoTYqLTE49DasKiDYB61TjNMAgAeLmk2q1BjkI88BOzuYLrdjsBbpkMVvjNHCQQPUfDV1y04_CZwsW80DS1-Kc29RQCEbLXf3Qe78y5KxJcFT6_1qRHd_AGSHAXXKIw6WkAjX3zLgx3j8c8bkpbO6DoKlQI93pl-oMD-wp6IcGjoptsePIdM-9elLCbLJS6KVPvLj3BO903RmSujjOWV4t-FwWamP1iok8HIgSYmdISkcodYgRw5xodGGczQZK36rycCjLAVbYALvmjOrfqMa2KZf-ewWf8oSHewBaP-aFnYJrsSUBmw0176bwlrXk94Tb0CbEx2LViPDpMcRr4Q_OtvZYD6O8Vw6_r4n6Csx8XGZDqf80lI6GH8hpyyXPWQEmxextbC0LXLjd3R6HB5A-OZ7-p97M-nW7c8ySgl85GZkJGWnLLQcu7sxFJUCVzr0R74F-5JNqcugzSa7t20oiPrxa39n58kLtJHziasAwCYS86leu03Nur5wh2OUqgAQOl62w9pYhatGngt4IbvuIGpEd2EJ2CpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e681b632df.mp4?token=f3ylE0cqo6MgyV9UkXFb65eqGP4a-72SCjdtCcyQpm9p-d7BYbTl9naiDfGbVn9flLAfC7NIwSFhw-tiE5g3YXNHUZ64dnlVvqNot7XaQEUwqye6yCN4DyF6MjAc6rZVeGSWALJ9xdNoTYqLTE49DasKiDYB61TjNMAgAeLmk2q1BjkI88BOzuYLrdjsBbpkMVvjNHCQQPUfDV1y04_CZwsW80DS1-Kc29RQCEbLXf3Qe78y5KxJcFT6_1qRHd_AGSHAXXKIw6WkAjX3zLgx3j8c8bkpbO6DoKlQI93pl-oMD-wp6IcGjoptsePIdM-9elLCbLJS6KVPvLj3BO903RmSujjOWV4t-FwWamP1iok8HIgSYmdISkcodYgRw5xodGGczQZK36rycCjLAVbYALvmjOrfqMa2KZf-ewWf8oSHewBaP-aFnYJrsSUBmw0176bwlrXk94Tb0CbEx2LViPDpMcRr4Q_OtvZYD6O8Vw6_r4n6Csx8XGZDqf80lI6GH8hpyyXPWQEmxextbC0LXLjd3R6HB5A-OZ7-p97M-nW7c8ySgl85GZkJGWnLLQcu7sxFJUCVzr0R74F-5JNqcugzSa7t20oiPrxa39n58kLtJHziasAwCYS86leu03Nur5wh2OUqgAQOl62w9pYhatGngt4IbvuIGpEd2EJ2CpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : دست فرمون شما ما رو رسوند به جنگ
خلاصه گفتگو با سید عباس عراقچی
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18838" target="_blank">📅 11:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18837">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فرماندار چابهار گفت: صدای انفجار شنیده‌شده امروز، ۲۸ تیرماه، در حوالی این شهر مربوط به عملیات امحا و انهدام کنترل‌شده مهمات عمل‌نکرده بوده و هیچ خطری شهروندان را تهدید نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18837" target="_blank">📅 10:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18836">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏ارتش جمهوری اسلامی با صدور بیانیه‌ای، مدعی حملات تازه به دو پایگاه نیروهای آمریکایی در کویت شد.
‏در این بیانیه آمده که ارتش جمهوری اسلامی در پی «حمله به پل‌ها، زیرساخت‌ها و مناطق غیر نظامی»، انبار مهمات ارتش آمریکا در اردوگاه العدیری و رادار پاتریوت و رادار هوایی این ارتش در پایگاه علی‌السالم کویت را، آماج حملات پهپاد‌های خود قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18836" target="_blank">📅 10:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18835">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نیویورک پست از قول دونالد ترامپ: کشته شدن دو سرباز آمریکایی مایه تاسف است، اما ماموریت نظامی همچنان ضروری است
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18835" target="_blank">📅 10:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18834">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: اگر تهران متوقف نشود، منطقه ممکن است وارد یک درگیری گسترده‌تر شود
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18834" target="_blank">📅 09:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18833">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وال استریت ژورنال: بر اساس اظهارات افراد مطلع، در حمله ۱۷ ژوئیه ایران به پایگاه هوایی موفق السلطی، علاوه بر موارد دیگر، هواپیماها و پهپادها نیز آسیب دیدند
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18833" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18832">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-Iz1-x8dAYFGCCDlBWYnpTWx2LZjRdev5uYXLB7cL5BfRq16gB613FOwkuI9cXHhAygWCx0NMApt6Hx4cJO9RguN71gyFkjFjBY8hDmNSzpgN-6ocvmrqb1ZfHtqayUV7vVAWEluR4xbY_pt3-BDrv3BEfMWHo3prMGDE_3OyALwLouQdJ2jDtVPLcXfcOyF44A2JHWmwr50CMAPlEhmC1Yzz-KsMsQg-RtJtIfQmm_ROEtkhgb5zPOpHJQNJoUiDrLMAlECwOPr4dm2UWgfsLsjpn0XqOtX8IJ-OqlsNwwBWPJn-qVtoyHujJIfpIjuHDUdBYBNDCabMCpxBvCHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزله در دزفول و اهواز @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18832" target="_blank">📅 08:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18831">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">معاون امنیتی ‌استانداری خوزستان:
جنگنده‌های‌ آمریکا ساعت ۰۵:۵۵ دقیقه نقاطی در اطراف شادگان را مورد اصابت موشک قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18831" target="_blank">📅 08:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18830">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سایت موشکی خمین ,کوه انگشت لیس , بین خمین و گلپایگان @WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18830" target="_blank">📅 08:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18829">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">زلزله در دزفول و اهواز
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18829" target="_blank">📅 08:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18828">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95514648b.mp4?token=NC-z4i61X0GebNF9dogSrqobPAgtcaKE_i1-ZJL0hCGCBz_lVnpuG1YGauFzX3cfHYp4wlCAFRa-gVJ_M_yzs-AWySkdVhaMhOzPWKPHRGgGgTOi6xP278r6g0tP1hBZSg3Q2cfx4_5M_ZchYf5AsqUBHdgxeNPn27NP4-wzMBEg517gLE4RMerXZIa_IT0JaNDrBvGPZ2FTzmNNW5zdfLV8tiM1W9_1kwJrLK2KCP2Gj6RqBQoFonDWEkKgwJ0IbCkujre3L06kym82lfaFRwKV_KFAdXESKkY16zAPI1jyL9zFWGCx6_Yh3s_RzoN5DXfW1bupE5J92Epke5HcFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95514648b.mp4?token=NC-z4i61X0GebNF9dogSrqobPAgtcaKE_i1-ZJL0hCGCBz_lVnpuG1YGauFzX3cfHYp4wlCAFRa-gVJ_M_yzs-AWySkdVhaMhOzPWKPHRGgGgTOi6xP278r6g0tP1hBZSg3Q2cfx4_5M_ZchYf5AsqUBHdgxeNPn27NP4-wzMBEg517gLE4RMerXZIa_IT0JaNDrBvGPZ2FTzmNNW5zdfLV8tiM1W9_1kwJrLK2KCP2Gj6RqBQoFonDWEkKgwJ0IbCkujre3L06kym82lfaFRwKV_KFAdXESKkY16zAPI1jyL9zFWGCx6_Yh3s_RzoN5DXfW1bupE5J92Epke5HcFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام :شب هشتم تمام شد
ما
دور تازه حملات علیه ایران
در
۱۸ ژوئیه، ساعت ۱۱:۳۰ شب به وقت شرق آمریکا (ET) (۰۷:۰۰ صبح ۱۹ ژوئیه به وقت تهران)
و
به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)
به پایان رساندیم.
به گفته سنتکام، در
هشتمین شب متوالی
حملات آمریکا، نیروهای این فرماندهی
تأسیسات دیده‌بانی ساحلی و پدافند هوایی، توانمندی‌های دریایی، و انبارهای موشک و پهپاد ایران
را با موفقیت هدف قرار دادند تا توانمندی‌های نظامی ایران بیش از پیش تضعیف شود. همچنین نیروهای آمریکایی،
عناصر سپاه پاسداران
را که به گفته آمریکا در
۱۷ ژوئیه (۲۶ تیر)
در حملات علیه نیروهای آمریکایی در اردن مشارکت داشتند، هدف قرار دادند
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18828" target="_blank">📅 08:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18827">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09cf3dc329.mp4?token=vtZT_MwuvFHUYoPuCpJ-tEXR532Dhizl4Sv_A3-lnoVqdniRJPKyge-RWTTyfTj1kV_u1VlkGb-WrKMG6gRQpf4L-GoBiNHE3VDPD3tZQ-zzr4aNTcm17TdWIYA7USJLj5IZ1gPROogdcIgf-EeEOlG4Y_f4hMgvBk04PUJ_OER3Yd38UMwrk4Hq2U6tNIrqYVUrBq4bxrx_pJLyfu6ad4JjKBumVZ2DU61THsGlWdt4c9rd4abyOLXPTLdwX4cF_6HxCeGfzaLWfjz1pl5dY_iaYqs6txNkbgLm9w3zVjw11AQsRr1BNZSOEE7sB-vTuEX3wqwnbF8d8tBRamgoYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09cf3dc329.mp4?token=vtZT_MwuvFHUYoPuCpJ-tEXR532Dhizl4Sv_A3-lnoVqdniRJPKyge-RWTTyfTj1kV_u1VlkGb-WrKMG6gRQpf4L-GoBiNHE3VDPD3tZQ-zzr4aNTcm17TdWIYA7USJLj5IZ1gPROogdcIgf-EeEOlG4Y_f4hMgvBk04PUJ_OER3Yd38UMwrk4Hq2U6tNIrqYVUrBq4bxrx_pJLyfu6ad4JjKBumVZ2DU61THsGlWdt4c9rd4abyOLXPTLdwX4cF_6HxCeGfzaLWfjz1pl5dY_iaYqs6txNkbgLm9w3zVjw11AQsRr1BNZSOEE7sB-vTuEX3wqwnbF8d8tBRamgoYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش انفجار  در قشم
@WarRoo
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/18827" target="_blank">📅 05:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18826">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سکوت عجیبیه</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/18826" target="_blank">📅 03:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18825">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سنتکام: امروز ساعت 6 عصر به وقت شرق آمریکا، نیروهای ایالات متحده به دستور فرمانده کل قوا، حملات هوایی جدیدی رو علیه ایران آغاز کردن. هدف این حملات، تضعیف بیشتر توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز و مجازات سریع نیروهای سپاه پاسداران انقلاب…</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/18825" target="_blank">📅 03:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18824">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جزیره لارک سایت سپاه رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/18824" target="_blank">📅 03:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18823">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجار‌سایت موشکی حاجی اباد، هرمزگان  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/18823" target="_blank">📅 02:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18822">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDwNeSXT5yTnPgMzjk8RcLbUWCa5hYl_7lcmQsiEMurPNJwCQUYYbCYc2I4Y6hiV04f0Fs8EwG_jCPhTdGoNI3ztYpl2DUaS6glQ8e-4bmR4ho6X7j5SHXw_MFNbalUN4okx23FOgICY22GENTa8sLq8xk8FovVVBGuNizNNx6lCJ74mxwulKmOkXHmHgGOmkHV1ENQh1CE5AEEXyHihmzxnlnf2W8zzRiTNFgyj1GToJJWe9zzrwkcoCE19_s04OAB_fhcV_w7qzhEwlCbNtQGVkFgTtgrg5JvacHvBJZWucWKqE1JIYtGxKsmxt81iKPxxZUYY6KocVz8zW5z4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار جان الان امدم بالا پشت بوم جنوب تهران ستون دود بلند شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/withyashar/18822" target="_blank">📅 02:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18821">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اتاق جنگ با یاشار : بعد از مدتها نمیتونم ببینیم چیزی
🤒
همه رفتن زیر پتو رررپتپتوووو  @WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/18821" target="_blank">📅 02:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18820">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یک صدایی شبیه به انفجار در کوه دراک شیراز که شهر موشکی هست شنیده شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/18820" target="_blank">📅 02:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18819">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجار‌سایت موشکی حاجی اباد، هرمزگان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/18819" target="_blank">📅 02:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18818">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش انفجار خرم آباد لرستان
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/18818" target="_blank">📅 02:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18817">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/18817" target="_blank">📅 02:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18816">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هیچ گزارشی از‌ بندر عباس نیست !
🚨
🚨</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/18816" target="_blank">📅 02:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18815">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش انفجار در بوشهر
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/18815" target="_blank">📅 02:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18814">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش‌ انفجار در اراک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/18814" target="_blank">📅 02:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18812">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer"><a href="https://t.me/withyashar/18812" target="_blank">📅 02:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18811">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/18811" target="_blank">📅 02:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18810">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/18810" target="_blank">📅 02:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18809">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/18809" target="_blank">📅 02:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18808">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گزارش حمله با موشک های کروز تاماهاک (که خامنه ای‌رو کشت ) توسط ناو های آمریکایی‌به ایران
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/18808" target="_blank">📅 02:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18806">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مسیر جاسک (بیاهی) از طرف دریا  ۳۰ جنگنده اومد
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/18806" target="_blank">📅 02:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18805">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حقیقت یاب اناق جنگ : همانجور که اعلام نکردم سیریک خبری نیست فقط نیم ساعت پیش صدا جنگنده اومد اما انفجاری چیزی رخ نداد فیک نیوزه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/18805" target="_blank">📅 02:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18804">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">۲ انفجار بندر لنگه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18804" target="_blank">📅 02:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18803">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">جنگنده های آمریکایی بر‌فراز ‌کیش
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18803" target="_blank">📅 02:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18802">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش انفجار‌اهواز
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/18802" target="_blank">📅 02:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18801">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/18801" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18799">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کانال ۱۴ : کنسولگری آمریکا در اربیل کردستان عراق در حال حاضر مورد حمله شبه‌نظامیان تحت حمایت ایران قرار گرفته است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18799" target="_blank">📅 02:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18798">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcMXFXtMNeaOtfJ4P8f6m5UqwSD9icbcJdNkpQN3UuIkxkycThUtSKNwZiDp_0zVby-cB1nruVZkt3gsAN7CdqJLu_3A6owUvJrUXBstCJuRFi10dusJyhh2a9aiCCP0k2SSLPyIfe-wWWGZz-qXVLt1Dd4cDtTfpdBgo3usVf669yjX9tL7iTlXUey0mNEhWusm-d-CMgu2GvuVMIg63idGN17k36Ios9wi4MIEjqu8B0QF41_TPkq4yjYiniUM79emEs5eQhHVRJUAdvae0_qQi3_7gnGid6FHuBrd1v8D1NKZNN6AVFMr-TQ0uYSOV1wnbVwhH3kuEpilUDBo2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا اربیل عراق کنسولگری‌ آمریکا رو زدن
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/18798" target="_blank">📅 02:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18797">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18797" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18796">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18796" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18795">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سنتکام: امروز ساعت 6 عصر به وقت شرق آمریکا، نیروهای ایالات متحده به دستور فرمانده کل قوا، حملات هوایی جدیدی رو علیه ایران آغاز کردن.
هدف این حملات، تضعیف بیشتر توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز و مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی است که شب گذشته حملاتی رو علیه نیروهای نظامی آمریکایی در اردن انجام دادن.
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/18795" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18794">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سنتکام آغاز حملات را اعلام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/18794" target="_blank">📅 01:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18793">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سنتکام آغاز حملات را اعلام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/18793" target="_blank">📅 01:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18792">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وال استریت ژورنال: جنگنده های F35 ارتش آمریکا از بریتانیا به سمت خاورمیانه اعزام شدند
@WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/18792" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18791">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/withyashar/18791" target="_blank">📅 00:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18790">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزارت امور خارجه ایالات متحده آمریکا یک "هشدار جهانی" صادر کرد و هشدار داد که گروه‌هایی که از ایران حمایت می‌کنند، ممکن است به سایر منافع آمریکا در خارج از کشور یا مکان‌هایی که با ایالات متحده و/یا آمریکایی‌ها در سراسر جهان مرتبط هستند، حمله کنند
@WarRoom</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/withyashar/18790" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18789">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وال‌استریت ژورنال: آمریکا به نقش احتمالی چین یا روسیه در هدف‌گیری‌های ایران مشکوک است
وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد که پس از اصابت حملات ایران به چند هدف حساس با دقتی غیرمعمول، احتمال ارائه اطلاعات هدف‌گیری از سوی چین یا روسیه به تهران در حال بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/withyashar/18789" target="_blank">📅 23:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18788">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یک حادثه دریایی دیگر، سومین مورد در امروز، دقایقی پیش در نزدیکی سواحل عمان رخ داد.
@warroom</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/withyashar/18788" target="_blank">📅 23:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18787">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">طبق گزارشات غیر رسمی دقایقی پیش آمریکا پل سورمیچو که ایرانشهر رو به چابهار متصل میکنه هدف قرار داد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/withyashar/18787" target="_blank">📅 23:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18786">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">میگم تا حمله شروع نشده، یه لطفی کنین خستگی منم در بره. چیزی نمونده بشم 1.7M یه هول بدین تو گروه چتا بذارین، به دوستاتونم که ندارن بگین اینستاگراممو فالو کنن. نوتیفیکیشنهای پیجم روشن کنین، استوریا رو هم حتما ببینین.
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/withyashar/18786" target="_blank">📅 23:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18785">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مقام آمریکایی به NPR : ترامپ دستور داده تا طی ساعات آینده ارتش آمریکا درهای جهنم رو به روی ایران باز کنن.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/withyashar/18785" target="_blank">📅 23:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18784">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وال استریت ژورنال : مقامات آمریکایی می‌گویند ایران در حال شلیک موشک‌هایی است که با سرعت بسیار بالایی حرکت می‌کنند و می‌توانند هنگام نزدیک شدن به زمین مانور دهند
@WarRoom</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/withyashar/18784" target="_blank">📅 23:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18783">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : ویدئوی منتسب به پست دونالد ترامپ در اینستاگرام مبنی بر حمله زمینی فیک است و ترامپ از دیروز در اینستاگرام هیچ پست جدیدی قرار نداده.
@WarRoom</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/withyashar/18783" target="_blank">📅 23:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18782">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkSnK-pbx_l_asCe6wMLpQVGicL7FaCLSNde5a-L8vEZVlONEEu-3e05ccnhN6cjFPHeeijTJbSNtxGOA7vIKryqMR5XEuKjiyRPNmaGUB48e7QPt0zJ6jg9ih5AJpgXmCL29A0KbAjcSqmOOsRojfhtYTwd9E3umUn2FPmi9XZ57bXcipni98--NkNv5_qqZUkE0TiTlQqAC_JJ41ogDrZlitXD_WMmtZTvfnkavz3mvkg9p0BILzwgT5psjs5BynkwY2lf52VOnDYbfawzEqw4ksgZAiPSITZCwzlODapc5-JZE8HegoRi129GxtYJZkMExHXB1RQYwMotACp8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : بعد از مدتها نمیتونم ببینیم چیزی
🤒
همه رفتن زیر پتو رررپتپتوووو
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/18782" target="_blank">📅 22:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18781">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هواپیمای های آمریکایی در منطقه فرستنده های خودشونو خاموش کردن
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/18781" target="_blank">📅 22:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18780">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شبکه CBC: امشب احتمالاً شاهد فعالیت‌های بیشتر در ایران خواهیم بود، و کشته شدن سربازان در اردن ممکن است چهره اوضاع را تغییر دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/18780" target="_blank">📅 22:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18779">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش انفجار بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/18779" target="_blank">📅 22:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18778">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کانال 14 عبری: نشانه‌هایی حاکی از احتمال قریب‌الوقوع از سرگیری جنگ با ایران، از جمله در خاک اسرائیل، وجود دارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/18778" target="_blank">📅 22:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18777">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آکسیوس:ایران از خط قرمز ایالات متحده عبور کرده است. این احتمالاً باعث می‌شود رئیس جمهور ترامپ علیه رژیم ایران تشدید شود. کمربندهایتان را ببندید.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/18777" target="_blank">📅 22:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18776">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش انفجار بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/18776" target="_blank">📅 22:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18775">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرگزرای CBS به نقل از مقام نظامی: حملات امشب دقایقی دیگر آغاز میشود و گستردگی بیشتری دارد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/18775" target="_blank">📅 22:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18774">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کارشناس صداوسیما: اگر آمریکا اومد جزایر ما رو گرفت، اینم جزو سیاست‌های جنگه، نباید بشینیم گریه کنیم چون دنیا به آخر نرسیده. باید بریم تلاش کنیم تا آزادش کنیم. زمان جنگ با عراق تمام سران کشور زنده بودن ولی خرمشهر سقوط کرد و ۱۸ ماه طول کشید تا آزاد بشه.
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/18774" target="_blank">📅 22:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18773">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پیت هکست وزیر جنگ ایالات متحده
خداوند به قهرمانان سرعت و توان دهد.
فداکاری آنان تنها عزم و اراده ما را راسخ‌تر می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/18773" target="_blank">📅 22:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18772">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بندر عباس ( حکم به نام خدا داره) صدا انفجار گزارش شده
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18772" target="_blank">📅 22:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18771">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فککک کنممم شروع شد
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18771" target="_blank">📅 22:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18770">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18770" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18769">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجار در سیریک و جاسک تکذیب شد
استانداری هرمزگان:
دقایقی پیش خبری مبنی بر حمله جنگنده‌های آمریکایی به مناطقی در حاشیه شهر سیریک و جاسک منتشر شد که این خبر صحت ندارد و تا این لحظه هیچ گونه انفجار و حمله جنگنده های آمریکایی گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18769" target="_blank">📅 22:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18768">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa5c312e2f.mp4?token=uyJyU2un-UVf3eI90x4qpruWEZjdtXrvgAvo23S1fZMTAPQuefgUSoa5ruDKAx7z8LHUqH1XtUEivP1SOjngVySvM_fiJwMRsZq9cCss1QqMdh61L4TsQoWTIFU8L6ArjFP3UB6I4VXYlLtI0HK98gT9qWA_fl3cO3FFjiiilTeTlaP-7LGNCzcZzTNKm2LumKL8Ooq52McAMmIT6RNl4nL6hyEsUnf6194Iyx70yGbr2em9qX3_pAocXUhscL4tAdJtoyJ6dB-_uE5mvThI7nz1ChxuqsUrvsG1vF74P1YOPwBDwaBji5O0joEoycWBcgEhsGg39P8Sn6255g1yxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa5c312e2f.mp4?token=uyJyU2un-UVf3eI90x4qpruWEZjdtXrvgAvo23S1fZMTAPQuefgUSoa5ruDKAx7z8LHUqH1XtUEivP1SOjngVySvM_fiJwMRsZq9cCss1QqMdh61L4TsQoWTIFU8L6ArjFP3UB6I4VXYlLtI0HK98gT9qWA_fl3cO3FFjiiilTeTlaP-7LGNCzcZzTNKm2LumKL8Ooq52McAMmIT6RNl4nL6hyEsUnf6194Iyx70yGbr2em9qX3_pAocXUhscL4tAdJtoyJ6dB-_uE5mvThI7nz1ChxuqsUrvsG1vF74P1YOPwBDwaBji5O0joEoycWBcgEhsGg39P8Sn6255g1yxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
ما از آرژانتین به طرق مختلف حمایت می کنیم، از جمله فردا.
کتمان نمی کنم که به آرژانتین علاقه دارم. من فکر می کنم بیشتر شهروندان اسرائیلی به آرژانتین علاقه دارند.
موفق باشید! واموس آرژانتین!
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18768" target="_blank">📅 21:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18767">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ادعای i24news فرانسه: نهادهای دفاعی اسرائیل در حال آماده‌سازی برای وقوع یک جنگ بسیار جدی در کل منطقه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18767" target="_blank">📅 21:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18766">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هم اکنون ۳ سوخت رسان از اسرائیل بلند شد، احتمال میرود دو تا سه عدد دیگر نیز  بلند شوند. اون یدونه که سلکت کردم داره برمیگرده حساب نکرم @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18766" target="_blank">📅 21:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18765">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saYc8M4FEVDET35692wilzENgdURW_XewXQWswhzdE8tpgeJDE-FSHViWjPTjFMoBaNIPCOFH1UaWm8j7cCguR1CmgDRDIZ87UXbINXi6XZFruE_v5P8aFLRmM4RQHZl88FcWNmBjTbf_stdGIAP51EsUAB_J0Z8vGR6W3tL9veldaONoOTnFI-_YLmQP_VsQLlr-ZAxysteMDk6Z49jKkMh0cByU3wKZvrFMWPh1i9y4vUNyCqKq0p-O8mNN6sn1bpHZg8iJbB_JrFL0QtmoDYJS3T0P4VBNRjgL8Qvo9KdCWP4K8SLVSKZLk8zCeub-X7UGm93SRE9UFN9IDqkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۳ سوخت رسان از اسرائیل بلند شد، احتمال میرود دو تا سه عدد دیگر نیز  بلند شوند. اون یدونه که سلکت کردم داره برمیگرده حساب نکرم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18765" target="_blank">📅 21:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18764">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">درود بر خانواده تلگرام ما
😍
🙌🏾</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18764" target="_blank">📅 21:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18763">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18763" target="_blank">📅 21:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18762">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صدای انفجار سیریک سمت اسکله که دکل معروف هم آنجاست
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18762" target="_blank">📅 21:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18761">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صدای انفجار سیریک سمت اسکله که دکل معروف هم آنجاست
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18761" target="_blank">📅 21:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18760">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فاکس نیوز:موشک های ایران مستقیم به نیروهای امریکا در کویت برخورد کرده و حتی جسد پیدا نشده است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18760" target="_blank">📅 21:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18759">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ادعای رویترز‌ : خبر کشته های امریکا به کاخ سفید رسیده است و ترامپ بسیار عصبانی است
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/18759" target="_blank">📅 21:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18758">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سنتکام : در
۱۷ ژوئیه (۲۶ تیر)
،
دو نیروی نظامی آمریکا
در اردن، در جریان دفاع نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان در برابر
حملات موشک‌های بالستیک و پهپادهای ایران کشته
شدند
. همچنین
یک نیروی نظامی آمریکایی
همچنان
مفقودالاثر
است.
سنتکام اعلام کرد
چهار نظامی آمریکایی
برای دریافت خدمات درمانی به بیمارستان‌هایی در اردن منتقل شدند، اما پس از درمان مرخص شده‌اند. همچنین سایر نیروهایی که دچار جراحات جزئی شده بودند، به مأموریت خود بازگشته‌اند.
سنتکام افزود که
به احترام خانواده‌های جان‌باختگان
، تا
۲۴ ساعت پس از اطلاع‌رسانی رسمی به نزدیکان آن‌ها
، اطلاعات بیشتری از جمله هویت نیروهای کشته‌شده منتشر نخواهد شد.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18758" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18757">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ادعای کانال ۱۳ اسرائیل:
در اسرائیل می‌گویند آمریکا برای گسترش عملیات نظامی در ایران آماده می‌شود: هفته‌ای سرنوشت‌ساز در پیش است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18757" target="_blank">📅 20:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18756">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شبکه i24 گزارش می‌دهد که شبکه‌های تلویزیونی اسرائیل از سوی دفتر نخست‌وزیری مطلع شده‌اند که ممکن است پخش برنامه‌های اضطراری به‌زودی و در هر لحظه آغاز شود.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18756" target="_blank">📅 20:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18755">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18755" target="_blank">📅 20:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18754">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9571048b32.mp4?token=fmBUYo2i_mIuiXq6zcaOri7KADnJIZ_ZMpjz990luuoGNCCFGN7Qu806SjCwA5troTx-6r-Ysz0cHqgzz7sztN5jMBAvAIjwzrODrNoNCD07OZFa94YdDhe_6F9T7rbLKdDkmLt5O1Ttr_D50rrgkb5Bkx_jcsJzs7EJXhuLXipAAbf1RGwg2JlNQl9tqklqH9qWnHtSWn5qstduvulHXmz0laRdiMplkapUFgJp79MNqGGta3dbNR7Y9xCpCeKBDQDgCDFKPJlqPo3iDBhJKX0_QSDUikI6ydtydIwastS8RmnGrEHMrkaTBnhXBgTN8DZLJN3IBagxUp_GLljABRyYi-nRn61U_ww3FQ7-hSCnJ-CEwABh6FFvOi-u8GCgaEVwhbjgOwOd1Q6A4OBZFp5OEIRXcyBteTwH8Az3rAtw1fVhblEX3AGI0xVfQiI6jWeB9deNneg71bfLZ2xy3Y0yNcBzBNgeT7w6FsrpjW3MQCUlw4toZoDvrnwuMwM6zUq6su9acq-2bvMbj1ZDGr2bhEVQvYVt8RKg5Pyg6BsKbr4G8AUe9FEh8jmbelJ87fcCyZhhHzMHbWwQlwSxyOL6bJnfOLhmaNy44YFctxAKfAzRhDiN7gzsep9Ou-x3eq7JcUn4oAON2zYr7YCmhqtFKaqf7eU7ST5RzRyBHPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9571048b32.mp4?token=fmBUYo2i_mIuiXq6zcaOri7KADnJIZ_ZMpjz990luuoGNCCFGN7Qu806SjCwA5troTx-6r-Ysz0cHqgzz7sztN5jMBAvAIjwzrODrNoNCD07OZFa94YdDhe_6F9T7rbLKdDkmLt5O1Ttr_D50rrgkb5Bkx_jcsJzs7EJXhuLXipAAbf1RGwg2JlNQl9tqklqH9qWnHtSWn5qstduvulHXmz0laRdiMplkapUFgJp79MNqGGta3dbNR7Y9xCpCeKBDQDgCDFKPJlqPo3iDBhJKX0_QSDUikI6ydtydIwastS8RmnGrEHMrkaTBnhXBgTN8DZLJN3IBagxUp_GLljABRyYi-nRn61U_ww3FQ7-hSCnJ-CEwABh6FFvOi-u8GCgaEVwhbjgOwOd1Q6A4OBZFp5OEIRXcyBteTwH8Az3rAtw1fVhblEX3AGI0xVfQiI6jWeB9deNneg71bfLZ2xy3Y0yNcBzBNgeT7w6FsrpjW3MQCUlw4toZoDvrnwuMwM6zUq6su9acq-2bvMbj1ZDGr2bhEVQvYVt8RKg5Pyg6BsKbr4G8AUe9FEh8jmbelJ87fcCyZhhHzMHbWwQlwSxyOL6bJnfOLhmaNy44YFctxAKfAzRhDiN7gzsep9Ou-x3eq7JcUn4oAON2zYr7YCmhqtFKaqf7eU7ST5RzRyBHPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنتاگون تأیید کرد که در درگیری‌های هفته جاری، سیزده پرسنل نظامی آمریکایی مجروح شده‌اند؛ این شامل ده سرباز و سه ملوان است که با سه پرواز تخلیه پزشکی از منطقه خارج شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18754" target="_blank">📅 20:28 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
