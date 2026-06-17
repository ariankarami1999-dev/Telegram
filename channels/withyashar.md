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
<img src="https://cdn4.telesco.pe/file/bEiDHH-8iQI9KCUJeW3glFQxnGg2Wfgu71d4xPcJa19CSCtgAQwVcrSfciJL7bbmq2e2dezjtafjh9qrnjmPXLhVhQk2P4cXVOf_h8uJ8bnzlzQ3vg5PyF2xv-xc_OE4vf_bdwOVOlv2LbdPI4flKC6oG2xdYULSeZu-vf2WFMTF1kZNKYC1Sk-Yifhbj4TBlfuVxHjeQ5SMAxlXOSXSkcoUSJQvvFYmPttnbtDvOZP2wxKvrHb_Fbf8RjQBTfX6HeScnHt6jem9zgrnQHAqq4tbztiMtoOint3srtpjF-k-z-4sGH4Ux-IKcP2lIU6ahTQzNsqMmux3oQfDS38d7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 03:51:59</div>
<hr>

<div class="tg-post" id="msg-15116">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
اگه میخوای بدونی قیمت دلار طلا خودرو .... درسال جدید چقدر میشه این چنل تمام پیشبینی ها همراه تاریخ وقوع رو گفته
🕯
@link
🕯
🕯
@link
🕯
🕯
@link
🕯</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/withyashar/15116" target="_blank">📅 02:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15115">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPGdg_iy1_aMouWTfZS_N-iyI-NDeAZEmKn244eaa5taB7IOtvs8zUcA-gULiG78sWpcVRAAi7rW8t2Dl4Fdbirkld1oYxaUwIWkj9-QNgZJwpbIjKbhIqpbr6PVvLTzlZKQOR7j7IbtXBtwu0i7kycrpwVfOnVmGRRN2EQq4ahO6yqgJ_rGS8urGF2SjF9Hr48H1MwpWbVjTSFq6BbfNpmzHPI0UJdIWgMgDvH5hWYgIyVFRUGr6nhsWRrq5DXGPhXECo4R0RQB9_CXUYdoOAFFR7AnL_17o4r7IqCVcj1lTn5jRuZQCux7hFjRHA8Gk9SVgxDFHPukZtUzRrr3GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین  الان ، چه خبره خلیج فارس
@withyashar</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/withyashar/15115" target="_blank">📅 02:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15114">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/withyashar/15114" target="_blank">📅 02:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15113">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95de30e10e.mp4?token=iG0ZynP2rd2iQ4cFJOO9SPXvtMfAoLsvhCo3gixvwwLmXHGwvLZqch_p1hck1QhgIbZmXf9BOUnxPQDghEjCWnBARCI2-wnhzV_0-xOjFwR_KqXK6nSVJaIBeCc9VhR7LmpKRx5bST94UsD_sJRoToVfuwZfH-jRNlMhgIkb0uGcmJtY9Oqk2U4M7iKni6Gn1dr0ufFKB9d5UbtmzVf1WR8I7xaoelnU1hGZHQdhWa9-3JHLhnX445DHHcvvoh3fd58kZTaiPVGsjVVk4TCbHH0HgOEHdVvvhx3HN7sTJ6S1N6PORZ22KPKbdopGvFxzZacKwPk2cxAY5odODFv6jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95de30e10e.mp4?token=iG0ZynP2rd2iQ4cFJOO9SPXvtMfAoLsvhCo3gixvwwLmXHGwvLZqch_p1hck1QhgIbZmXf9BOUnxPQDghEjCWnBARCI2-wnhzV_0-xOjFwR_KqXK6nSVJaIBeCc9VhR7LmpKRx5bST94UsD_sJRoToVfuwZfH-jRNlMhgIkb0uGcmJtY9Oqk2U4M7iKni6Gn1dr0ufFKB9d5UbtmzVf1WR8I7xaoelnU1hGZHQdhWa9-3JHLhnX445DHHcvvoh3fd58kZTaiPVGsjVVk4TCbHH0HgOEHdVvvhx3HN7sTJ6S1N6PORZ22KPKbdopGvFxzZacKwPk2cxAY5odODFv6jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس : اگه دونالد ترامپ حتی به عنوان رهبر معظم انقلاب در ایران هم انتخاب می‌شد، دموکرات‌ها باز هم می‌گفتن آمریکا شکست خورده
@withyashar</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/15113" target="_blank">📅 00:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15112">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23735193e5.mp4?token=NMEe0CQFmZ9Z9QUJr-9i-mGlUzkFbikQgPRBDnuuxsBwXXUZwTKpIJeD8nRY1VVyVLZ4wfZcqxsZZNqurQM8jdcwwzFAt0e_bNMsuFZAVu5HI5y5ugngYyitXsA3zfbKN4PZXQ18C6A6969Fli8CcopUtx6IVsSm5tpqutCDGKBQfuzvCZh2ZfP4QoJYuUhsvItshGnH5gp4x8T1sMBDjLr4OW8ZcrKuz8-2COCskPbhIuporjIovClbpYett6U6D7EPjcKpkL1ThACuSAD9umcjLRN005-OoGe5BagjebZm86esav0EugmGkkiSW5CKfc_ryydP-gJSSvh3YhOCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23735193e5.mp4?token=NMEe0CQFmZ9Z9QUJr-9i-mGlUzkFbikQgPRBDnuuxsBwXXUZwTKpIJeD8nRY1VVyVLZ4wfZcqxsZZNqurQM8jdcwwzFAt0e_bNMsuFZAVu5HI5y5ugngYyitXsA3zfbKN4PZXQ18C6A6969Fli8CcopUtx6IVsSm5tpqutCDGKBQfuzvCZh2ZfP4QoJYuUhsvItshGnH5gp4x8T1sMBDjLr4OW8ZcrKuz8-2COCskPbhIuporjIovClbpYett6U6D7EPjcKpkL1ThACuSAD9umcjLRN005-OoGe5BagjebZm86esav0EugmGkkiSW5CKfc_ryydP-gJSSvh3YhOCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور جی دی ونس:
پرزیدنت ترامپ هرگز نگفت که هدفش نصب رضا پهلوی برای تبدیل شدن به رهبر جدید ایران است.
آنچه گفته این است که اگر مردم ایران بخواهند قیام کنند ، عالی است. این کار اوناست این بین آنها و دولتشان است.
چیزی که ما می خواهیم توقف برنامه هسته ای آنهاست.‌‌
@withyashar</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/withyashar/15112" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15111">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f65655673.mp4?token=R3AMR68Vz61uriYUxxjf0eYJA4ZBv6MPQg38jncG9b3urgRji5qwOtEYTnZ0D8lPeO-pk18DJyd1o-l77Jh0Ffx2clX-cNf7xZ5UjnjocI_xsjqfeO7BgUVykA6jLuUKRxcPl_1vmHuG7yfbVdQDt8UzNFZuVnUGUNIMT7DgKU7k-tunQNGnh7vSEBPV4Udkq6CkeHFQQB3PNESs-7nzt_WidcT1BViIriT86TTLhTLcFLD1MJx2xee33USrOhqAJ3X8BUDCcPznasAYouFRyFV0Gsinp7OZVwAt12PRtPBobZyIGuXAKaJvVSkENv9RUX-zdhI6t8KAAwAp1mlSpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f65655673.mp4?token=R3AMR68Vz61uriYUxxjf0eYJA4ZBv6MPQg38jncG9b3urgRji5qwOtEYTnZ0D8lPeO-pk18DJyd1o-l77Jh0Ffx2clX-cNf7xZ5UjnjocI_xsjqfeO7BgUVykA6jLuUKRxcPl_1vmHuG7yfbVdQDt8UzNFZuVnUGUNIMT7DgKU7k-tunQNGnh7vSEBPV4Udkq6CkeHFQQB3PNESs-7nzt_WidcT1BViIriT86TTLhTLcFLD1MJx2xee33USrOhqAJ3X8BUDCcPznasAYouFRyFV0Gsinp7OZVwAt12PRtPBobZyIGuXAKaJvVSkENv9RUX-zdhI6t8KAAwAp1mlSpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور در به در دنبال  دکتر خوش چشم هستم که او را به صنعت فوتبال وارد کنم
@withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/15111" target="_blank">📅 00:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15110">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">همکنون
انفجار های مهیب در جنوب لبنان،
گزارش های محلی از شلیک گسترده تانک های اسرائیلی و درگیری شدید با نیرو های حزب الله در تلاش برای پیشروی در جنوب لبنان.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/15110" target="_blank">📅 00:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15109">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اورشلیم پست: ماهواره‌های اسرائیلی در طول حدود ۴۰ روز اجرای عملیات «غرش شیران» بیش از ۵۰ هزار بار از ایران تصویربرداری کردند
میانگین هر روز بیش از هزار تصویربرداری
@withyashar</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/15109" target="_blank">📅 00:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15108">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جی‌دی ونس: برخی خواهان اعزام صدها هزار نیروی آمریکایی به ایران هستند
ترامپ جورج بوش نیست؛ در باتلاق ایران گرفتار نمی‌شویم
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/15108" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15107">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">واکنش آمیت سیگال خبرنگار کانال 12 اسرائیل به توافق ترامپ:
ممکنه دشمنی با آمریکا خطرناک باشه، اما دوستی با آمریکا مرگباره!
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/15107" target="_blank">📅 00:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15105">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کانال ۱۳ اسرائیل: ترامپ مانع اجرای یک عملیات نظامی‌برنامه‌ریزی‌شده اسرائیل در غزه شد
این طرح در بالاترین سطوح سیاسی و امنیتی اسرائیل بررسی شده بود، اما پس از ارائه جزئیات به آمریکا، واشنگتن با آن مخالفت کرده و خواستار عدم اجرای آن در شرایط فعلی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/15105" target="_blank">📅 23:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15103">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">با این جماعت چه کنم
😞</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/15103" target="_blank">📅 23:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15102">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArtin</strong></div>
<div class="tg-text">اسکل عقده ای یه پیام رو جواب نمیدی
عقده ای هستی زیاددد</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/15102" target="_blank">📅 23:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15101">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شاهزاده رضا پهلوی به نیوزنیشن: مردم ایران اکنون میگویند چرا بمباران متوقف شد؟ ایالات متحده باید بمباران ایران را ادامه میداد
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/15101" target="_blank">📅 23:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15100">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش حملات پهپادی سپاه پاسداران به اربیل عراق
🚨
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/15100" target="_blank">📅 22:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15099">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">به گزارش ان‌بی‌سی نیوز، کارشناسان ارشد صنعت نفت هشدار می‌دهند که علیرغم فضای مثبت ناشی از توافق میان ایالات متحده و ایران برای پایان دادن به جنگ چندماهه در خاورمیانه، بازگشت بازارهای نفت به حالت عادی و از سرگیری تردد در تنگه هرمز فرآیندی زمان‌بر است و احتمالاً چندین هفته به طول خواهد انجامید.
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/15099" target="_blank">📅 22:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15098">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmEXNIJvooHtD0y-GaGhXNDzfCYLZDGvODJERuZEvFOTgulSwf8TePhVs91aY6Ps9OC6i4nQLTrABDL4oemCvRpSwHGC9BPduaL-osyQrnk7RyLmhB0NngcTtuDMORE0ipC4oJ2Y9-mQ1_giEIWO1RSa9jP7BmUzgQTMgW8NePwrKR_N5UhM58OpHLPykMAw64k7vevPUVYOBb7xQB7khGEf8jOOqc9vns3Nxkr7AzggK-07ZuI8RR37rJyZuLMJfZioN4mEmwpVw03Cz5TkNQey2ix3gTr4aGdpQxpI8adUZ9M7-grJIYIQfswmff-Z_9NzcPJuH3zmBoRMviVieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پایگاه موشکی دیگر در شامل شش ورودی زیرزمینی، در حال ساخت است. یکی از دلایل احداث ورودی‌های بیشتر، قرارگیری این پایگاه در ناحیه‌ای استراتژیک از ایران می‌باشد
بخشی از فرایند ساخت پایگاه مذکور، پس از جنگ 12 روزه صورت گرفته است، هم‌چنین برخی از سازه‌های روزمینی این پایگاه در دو جنگ اخیر هدف قرار گرفته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15098" target="_blank">📅 22:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15097">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b21de6065.mp4?token=BZn3HaouK0BB18gApH-DFDU3O0WG6eAIVtKWrYgAg5TB7YtgWP15WfM3CBjVtetHiDjttb56doWDnO2DWlGDvHw7SCRxMK9X2BzuX1VdaeegsezFUQ06O2INk3qDxAPfGwlc4ylsgFDS6YJ8Ln4HxOh7ofwyKmA1HS1qlyY-BqEfW7ucINY1GAAqMP8NuVxDrAex9aD6nNJ8kKVodivGafspL8QQ88Wq0w7waRtt3f1juOz4C9irnHRrPdrH-YX5pRO8ZEoh79nnMhrgDs7RJ7jEqtGY8KbTxnqM-8xO5sm88UneMi_WtmK8i7p30nNjBsR72px_tJG_IgnOCsAHHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b21de6065.mp4?token=BZn3HaouK0BB18gApH-DFDU3O0WG6eAIVtKWrYgAg5TB7YtgWP15WfM3CBjVtetHiDjttb56doWDnO2DWlGDvHw7SCRxMK9X2BzuX1VdaeegsezFUQ06O2INk3qDxAPfGwlc4ylsgFDS6YJ8Ln4HxOh7ofwyKmA1HS1qlyY-BqEfW7ucINY1GAAqMP8NuVxDrAex9aD6nNJ8kKVodivGafspL8QQ88Wq0w7waRtt3f1juOz4C9irnHRrPdrH-YX5pRO8ZEoh79nnMhrgDs7RJ7jEqtGY8KbTxnqM-8xO5sm88UneMi_WtmK8i7p30nNjBsR72px_tJG_IgnOCsAHHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدئو احمدی‌نژاد بعد از توافق
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15097" target="_blank">📅 22:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15096">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68844ebd5c.mp4?token=RCNOHxm8tWfqi0wvsl_CR7HzCGUilIrp2vgOXgQj81fwm9O0vQMTrSH8gjMiU1ysjWHU5xLuNmGBUCngH8wcT2SoCPonO0JpiQ4rr77fzQnsB38BeikJc7mw5XS3VK_jru3LpnVlN9UndlKygvrKTzFGVNqZH28Vir6jZ6xAWi-KtmRbpBR46ZUTikT-VxYtiuaN36IU9VxityJC_ixSVp3tCJLaxgg6GT3qgI41gbg3-LQAdI1YzlxGLOxiEQA0qUuNDGzvdFdSRscM7y2ukp9kbzzdTXMM9zDNdFs00zAfsRUfXz0MsW6plyO16ySYrONRP6w-QjNv7xvJitsI1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68844ebd5c.mp4?token=RCNOHxm8tWfqi0wvsl_CR7HzCGUilIrp2vgOXgQj81fwm9O0vQMTrSH8gjMiU1ysjWHU5xLuNmGBUCngH8wcT2SoCPonO0JpiQ4rr77fzQnsB38BeikJc7mw5XS3VK_jru3LpnVlN9UndlKygvrKTzFGVNqZH28Vir6jZ6xAWi-KtmRbpBR46ZUTikT-VxYtiuaN36IU9VxityJC_ixSVp3tCJLaxgg6GT3qgI41gbg3-LQAdI1YzlxGLOxiEQA0qUuNDGzvdFdSRscM7y2ukp9kbzzdTXMM9zDNdFs00zAfsRUfXz0MsW6plyO16ySYrONRP6w-QjNv7xvJitsI1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد اینهمه شب تو خیابون رفتن، آخرش بهت میگن اقلیتی تندرو
🤣
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/15096" target="_blank">📅 22:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15095">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا:
اسرائیل تو دو روز گذشته پس از اعلام پایان جنگ توسط رئیس ترامپ، 84 بار آتش بس تو جنوب لبنان رو نقض کرده و همچنان به جنایات و کشتار مردم لبنان ادامه میده.
هشدار میدیدم اگر اسرائیل به شرارت‌هاش ادامه بده، باید منتظر پاسخ سخت نیروهای مسلح جمهوری اسلامی ایران باشه.
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/15095" target="_blank">📅 22:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15094">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی: در صورت بدعهدی آمریکا، پاسخ  ایران، نظامی و کوبنده خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/15094" target="_blank">📅 22:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15093">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/15093" target="_blank">📅 22:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15092">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">12 بند توافق ایران و امریکا به گفته باراک راوید خبرنگار ‌آکسیوس :
-ایران، ایالات متحده و متحدانشان خصومت‌ها را متوقف خواهند کرد، از جمله در لبنان. ایران تعهد خود را به عدم توسعه یا دستیابی به سلاح‌های هسته‌ای مجدداً تأکید می‌کند.
-ایالات متحده و ایران متعهد می‌شوند مسئله دفع ذخایر اورانیوم غنی‌شده ایران را حل کنند.
-ایالات متحده و ایران درباره غنی‌سازی اورانیوم و نیازهای انرژی هسته‌ای غیرنظامی ایران گفتگو خواهند کرد.
-ایران وضعیت موجود برنامه هسته‌ای خود را در طول مدت مذاکرات حفظ خواهد کرد.
-ایالات متحده محاصره دریایی را برمی‌دارد، از تحمیل تحریم‌های جدید خودداری می‌کند و در طول مذاکرات حضور نظامی خود در منطقه را افزایش نخواهد داد.
-ایران ترتیبات لازم را برای تضمین عبور ایمن کشتی‌های تجاری از تنگه هرمز، بدون هزینه، به مدت ۶۰ روز فراهم خواهد کرد.
-ایالات متحده متعهد می‌شود دارایی‌های منجمد شده ایران را پس از اجرای تفاهم‌نامه در دسترس قرار دهد.
-اگر توافق نهایی حاصل شود، ایالات متحده نیروهای خود را ظرف ۳۰ روز خارج کرده و تمام تحریم‌ها علیه ایران را لغو خواهد کرد.
-هر توافق نهایی شامل برنامه‌ای برای ایجاد صندوق ۳۰۰ میلیارد دلاری برای بازسازی ایران خواهد بود. ایالات متحده به ایران معافیت‌های موقتی تحریمی برای اجازه فروش نفت در دوره مذاکرات اعطا خواهد کرد.
-مذاکرات بین ایران و عمان با مشارکت کشورهای خلیج فارس برگزار خواهد شد تا ترتیبات مربوط به حمل و نقل و خدمات دریایی تعیین شود.
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/15092" target="_blank">📅 21:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15091">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نفتالی بنت(نامزد نخست وزیری اسرائیل) در پخش زنده خطاب به جمهوری اسلامی: باور دارم به زودی یه دولت جدید در اسرائیل میاد و امیدوارم من رهبری اون دولت رو به دست بگیرم. از همینجا به رژیم ایران میگم؛ من قراره بدترین کابوس شما باشم، تاوقتی مردم ایران رو از دست شما…</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15091" target="_blank">📅 21:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15090">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شبکه خبر: تمام کسایی که توی بیت رهبری بودن کشته شدن جز مجتبی خامنه‌ای @withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15090" target="_blank">📅 21:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15089">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شبکه خبر: تمام کسایی که توی بیت رهبری بودن کشته شدن جز مجتبی خامنه‌ای
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/15089" target="_blank">📅 21:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15088">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b67afa5b.mp4?token=su7upL5wLJclSBYTCzwELO42POUVUwWBmeCrWMrHRk15vIrShxKoMiR7mcPHRZkrRcF0FXqChuZWqeYhgvqc7cyxHJAW4y5N0QouhW-0NNtTmTJzoJQMVjddo90UgXRrOW4dj-FCM0Utx3ZXNKz11BTswss6kpMXArB_jejQQb7OpBN8yx43DWxgKYcvjUtNqaRYGpFIRM5lVyQhlsy5DoYbbkaZMqYQEnevi3NAK5kkfDzFF-17YrhbS8V6bD-g8T19jDqvgMXCs1S9TXH6NpEOVTrykYY3a11JilVY-KNgf7wNskCwn2Kt1COH-S6wMaXQk7hIF8qSd_qglpjE-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b67afa5b.mp4?token=su7upL5wLJclSBYTCzwELO42POUVUwWBmeCrWMrHRk15vIrShxKoMiR7mcPHRZkrRcF0FXqChuZWqeYhgvqc7cyxHJAW4y5N0QouhW-0NNtTmTJzoJQMVjddo90UgXRrOW4dj-FCM0Utx3ZXNKz11BTswss6kpMXArB_jejQQb7OpBN8yx43DWxgKYcvjUtNqaRYGpFIRM5lVyQhlsy5DoYbbkaZMqYQEnevi3NAK5kkfDzFF-17YrhbS8V6bD-g8T19jDqvgMXCs1S9TXH6NpEOVTrykYY3a11JilVY-KNgf7wNskCwn2Kt1COH-S6wMaXQk7hIF8qSd_qglpjE-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت(نامزد نخست وزیری اسرائیل) در پخش زنده خطاب به جمهوری اسلامی:
باور دارم به زودی یه دولت جدید در اسرائیل میاد و امیدوارم من رهبری اون دولت رو به دست بگیرم.
از همینجا به رژیم ایران میگم؛ من قراره بدترین کابوس شما باشم، تاوقتی مردم ایران رو از دست شما آزاد نکنم دست بردار نیستم.
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/15088" target="_blank">📅 21:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15087">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/15087" target="_blank">📅 21:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15086">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شبکه ۱۳ اسرائیل: امروز یه نشست اضطراری تو دفتر بنیامین نتانیاهو برگزار میشه تا بررسی کنن چطور میشه بین جبهه ایران و لبنان تفکیک ایجاد کرد و با این شاهکار ترامپ کنار اومد.
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/15086" target="_blank">📅 21:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15085">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/15085" target="_blank">📅 21:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15084">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">@withyashar
استادیوم</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/15084" target="_blank">📅 21:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15083">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMona</strong></div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/15083" target="_blank">📅 21:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15082">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">@withyashar
بی‌بی و ترامپ
mma رو  گفتم wwf</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/15082" target="_blank">📅 20:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15081">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=fxCFdm7CjfaMEDv-3S0qI2IN-nU6YxQ5Ik54MT-DhOUVrQhYHuAkZDNQAMDAjD7afd3m-d6OflO6viY61cZikkP-RY0AuZPo8DxqVsFLHI405p8yJ9ktzZd3rDqU9ZPymvWUs51vqCntJyDG-Ij0RbszHFBbh20-vHF6wmsQPxYlL4kyyECf5lG2-LFqCWqBxnqAPq9LKi5ExictsNKhszJ080dNV2bRi5PKlNr-PZPRm1x-__uR6_yvfvlkYMXx6-tTS6PWc1HsYjbzkSE7Cm6ZeXFuvx3WO8Lij5KfltR5Z4jF-1hFfGBIshA17yFoXwAjQEt32u3-_Gwqz32hxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=fxCFdm7CjfaMEDv-3S0qI2IN-nU6YxQ5Ik54MT-DhOUVrQhYHuAkZDNQAMDAjD7afd3m-d6OflO6viY61cZikkP-RY0AuZPo8DxqVsFLHI405p8yJ9ktzZd3rDqU9ZPymvWUs51vqCntJyDG-Ij0RbszHFBbh20-vHF6wmsQPxYlL4kyyECf5lG2-LFqCWqBxnqAPq9LKi5ExictsNKhszJ080dNV2bRi5PKlNr-PZPRm1x-__uR6_yvfvlkYMXx6-tTS6PWc1HsYjbzkSE7Cm6ZeXFuvx3WO8Lij5KfltR5Z4jF-1hFfGBIshA17yFoXwAjQEt32u3-_Gwqz32hxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/15081" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15080">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from자</strong></div>
<div class="tg-text">یاشار اخبار خیلی دارن میگن که شکاف به شدت زیاد شده بین بی بی و ترامپ
به نظرت زرگریه یا واقعا ترامپ پشت اسرائیل رو خالی کرده ؟</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/15080" target="_blank">📅 20:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15079">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شبکه ۱۲ اسرائیلی به نقل از یک منبع امنیتی:
کاهش محسوس در عملیات‌های ارتش اسرائیل در لبنان
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/15079" target="_blank">📅 20:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15078">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دلار ۱۵۲،۹۰۰
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15078" target="_blank">📅 20:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15077">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/15077" target="_blank">📅 19:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15076">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJAj7Y-uZPzdiOS2O4l8fKf-gT5EVwvpwE8oq9ZPoMYtNWD8XYBiDDfye8bUo3wv0lDaO75Fhbnc7LBY0W9ud6wMopSMRetLtHJekit9p2O3XAGD2c3KSmC-X3-w4cURZ_7jvzW9ndpPHKhS4ofBeqFi5BL8yYAzRrNu5CDKurlmvbpZFZdO2hx-gwgwon5vYHtJ2i9WA9eQZVlkQNNnfMVRFA416CB5seD9liC6jVvq11syN6HQQkrqYmlboPv03UvF3lwqbFpmG6ci9InaCvnfH3B2RZQivsm4QslJm39vDY6eZVumMHtb5TaHsS6CRjWpuhel2ecF7PGMls710A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقتصاددان سابق ترامپ می‌گوید توافق ایران به معنای رونق اقتصادی بزرگ برای ایالات متحده است
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/15076" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15075">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUiN9yWZWeFatUDccTrH8Hby2HEE9aunJJcNlrDBFEzrnaI9fjjVrb4nVY7n2k_htvXWSfRfOCqbAHh3ABttgxvM52X21iY75wSbFvffnG2FG4I0XHSja6gAhduoA4ferQmii19spu_47VPtr3VU80ZWGkA4sJrwS2KSUSbfuD7uqLnKwHpFIaLmSfk4yjcxddGNHL4wy8EIzQ6gwzQDkdQpzE2DrLSVg0S1BAMsBceBEeV9ouWj-CY8AV8b0qMr9cuNv9NtymECy7FWZ7OITWcfLtlKKw4IY2syae3uontrbhpg1C8Kq7OtYEZRzzS3kdQC2fUF7I-ws_EElomX5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته ایلان ماسک ۱۶۵ میلیارد دلار سود کرد و ثروتش به ۱.۳ تریلیون دلار رسید
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/15075" target="_blank">📅 19:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15074">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نفتالی بنت، نخست وزیر سابق اسرائیل:
توافق فعلی بین جمهوری اسلامی و آمریکا فقط یک توافق موقته.
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/15074" target="_blank">📅 19:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15073">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ادعای وال استریت ژورنال: واشنگتن به تهران اجازه خواهد داد تا بلافاصله فروش نفت و سوخت را طبق توافق پایان جنگ آغاز کند
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/15073" target="_blank">📅 19:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15072">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دلار ۱۵۳،۵۰۰
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15072" target="_blank">📅 19:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15071">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf74c8a754.mp4?token=U5XLBKhwsXxVyTVqNLBYHz_l-nhSZ76qmNUhJMihyboEjl3N0ZxqDgwTH3HBLoc1tr2-zdxwSMW-Xjb062-5ThKyLpP9-n-36gKVFS0ouQ6R2GrdrOTUNNBZEHbe_7E8m9YZSPotBtCQckmwGhHEHzOS5OrOPqJyjtanqfuC4p7BPdClLCRhoqE0590RliG1LsZlCwu1wvBzIA7GQYNf0gEhBHWUYJdzDkqD3rmfA0AdogiNOCuq8Yd4NtU1-o6Vfdi3sTKPjCDeqYkbuXPdnRrrQz0W9lWfzWbuE3Rf0Eqy5zw6B_1vP8Byvk3c3Uyqg0DoQ-1kOcaFoSeQ-Uz0NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf74c8a754.mp4?token=U5XLBKhwsXxVyTVqNLBYHz_l-nhSZ76qmNUhJMihyboEjl3N0ZxqDgwTH3HBLoc1tr2-zdxwSMW-Xjb062-5ThKyLpP9-n-36gKVFS0ouQ6R2GrdrOTUNNBZEHbe_7E8m9YZSPotBtCQckmwGhHEHzOS5OrOPqJyjtanqfuC4p7BPdClLCRhoqE0590RliG1LsZlCwu1wvBzIA7GQYNf0gEhBHWUYJdzDkqD3rmfA0AdogiNOCuq8Yd4NtU1-o6Vfdi3sTKPjCDeqYkbuXPdnRrrQz0W9lWfzWbuE3Rf0Eqy5zw6B_1vP8Byvk3c3Uyqg0DoQ-1kOcaFoSeQ-Uz0NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس فدرال آمریکا (FBI) در جشن تولد ترامپ، پهپادی که قصد ترور وی را در کاخ سفید داشت شناسایی و خنثی کرد!!
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15071" target="_blank">📅 19:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15070">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری وابسته به سپاه:
اسرائیل آتش‌بس در لبنان را نقض کرد.
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/15070" target="_blank">📅 19:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15069">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618d127639.mp4?token=uMLc9WCsQeuYwx2cMY3E6z6rkZnA6Dn8WbDH_jRQS5kiPdPA6iDnJNBoJDwFiy-FQODss1N6B_DcPsohmTmUQKm1cGnJCJL3tXqJM9CgWIIWTDsxxrsfHECcTKAVaG1BMQDsEi1LWi4hShprdFIMRHRj6lidZNhEI22u_BBjHbSvFkXgzVycZRDoFdRIvcfp3CYhCGMVCmTiFCZdxPUDtmU1NHLbjrYOMXLEkcCnvmQIp7RXq5XiGa_AQqZzwH3s1LDPuO4QDSUZs4jJdu_WAhLBcALVTYQW7173b0Y531u3Esk9ksJfF8nxjQ546r0GOky_TNT-x8cEj1JoRwFo-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618d127639.mp4?token=uMLc9WCsQeuYwx2cMY3E6z6rkZnA6Dn8WbDH_jRQS5kiPdPA6iDnJNBoJDwFiy-FQODss1N6B_DcPsohmTmUQKm1cGnJCJL3tXqJM9CgWIIWTDsxxrsfHECcTKAVaG1BMQDsEi1LWi4hShprdFIMRHRj6lidZNhEI22u_BBjHbSvFkXgzVycZRDoFdRIvcfp3CYhCGMVCmTiFCZdxPUDtmU1NHLbjrYOMXLEkcCnvmQIp7RXq5XiGa_AQqZzwH3s1LDPuO4QDSUZs4jJdu_WAhLBcALVTYQW7173b0Y531u3Esk9ksJfF8nxjQ546r0GOky_TNT-x8cEj1JoRwFo-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند عرزشی هم صداش در اومد
@withyashar
اینو پیدا کنین استخدام کنم اتاق جنگ سبک منو داره میره
🤣</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/15069" target="_blank">📅 18:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15068">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWwbNHii6jCndfFJLeD0ghn7SuayGxyac9SbWvsdgJ3x9qDoSOj7WivkizN1ZM4kW8Kt5uMkuu1lc2FdWDj7M-FcytQrTmMsjfJxE_ut5phcxb-p5SB4hIjKIRNC7QC-SQzSSyKOyWYOjuLNN0I8ScDYPdmc4PtzUEk94Xc6RTzO0CdIu5C96nkZ2xD1_UMUz7LUdTOroQFHCK_h6spZM4wBXgSOurFksQFLlH0MQPLGSaGksbZ0Qh_JwsBW0VbO6Tq8UlD688RgVnxKkO2KbkqOF85sovLdZwJV488S0xG37xLb7GuFH20QrNhQe553bC3eCGaW7ioL0WH07g7QKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دراپ سایت: ایران برای تحلیل رفتار ترامپ، دوتا روانشناس به تیم مذاکره کننده اضافه کرده
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/15068" target="_blank">📅 18:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15067">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/15067" target="_blank">📅 18:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15066">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">صداوسیما : همین که اول بازی پرچم ایران توی خاک آمریکا به اهتزاز در اومد یعنی ما بردیم. دیگه نتیجه بازیا خیلی مهم نیست
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/15066" target="_blank">📅 18:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15065">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4feef4c4.mp4?token=tuLMCmhwdPuxgu1tS_sOhRpFZLVWlogoOnMXPIAVaZA5K1Lxtld2Xs53JmwKaPffUeHGYBfOxNx6qMrhm0vhqvxLdx5KQeIAX38Zgg9SGiqyM2wC47N7id3Z1opZ3BUfNDs_Z29Dw9s_7x0m3gFEyiUBztmZsqLb3spT8N91roE8Ce9RhasiYS4w4p1gRANhZsF7JJzLVUKugCydkDMvnxr6EjkfVHyZ-EZv3lod9S9T-9LTk74hq0gHH8OF6otrun4bUWxVE6gxIH3j5tqHVrYj_LwXy5AWNYGS5Eladytc80fOJQATYfUMeUoXa0f8z_rtEZ7WOCSoRIw6C01RBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4feef4c4.mp4?token=tuLMCmhwdPuxgu1tS_sOhRpFZLVWlogoOnMXPIAVaZA5K1Lxtld2Xs53JmwKaPffUeHGYBfOxNx6qMrhm0vhqvxLdx5KQeIAX38Zgg9SGiqyM2wC47N7id3Z1opZ3BUfNDs_Z29Dw9s_7x0m3gFEyiUBztmZsqLb3spT8N91roE8Ce9RhasiYS4w4p1gRANhZsF7JJzLVUKugCydkDMvnxr6EjkfVHyZ-EZv3lod9S9T-9LTk74hq0gHH8OF6otrun4bUWxVE6gxIH3j5tqHVrYj_LwXy5AWNYGS5Eladytc80fOJQATYfUMeUoXa0f8z_rtEZ7WOCSoRIw6C01RBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس:
اگر مردم ایران خواهان رفاه بیشتر هستند، رهبرانشان باید پیشقدم شوند و رفتار خود را تغییر دهند.
اگر این کار را بکنند، عالی است. اگر نکنند، ایالات متحده قبلاً چیزهای زیادی به دست آورده است.
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/15065" target="_blank">📅 18:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15064">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ونس به فاکس نیوز:
ما پیروز شدیم، چه ایران روش خود را تغییر دهد و چه تصمیم بگیرد به توافق پایبند نباشد
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/15064" target="_blank">📅 18:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15063">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کانال 12 اسرائیل: اسرائیل درخواست دیدن یادداشت تفاهم بین آمریکا و ایران رو داشت اما این درخواست رد شد.
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/15063" target="_blank">📅 17:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15062">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ: ممکنه یه کنفرانس خبری برگزار کنم و متن یادداشت تفاهم آمریکا و ایران رو با صدای بلند و کلمه به کلمه بخونم تا رسانه‌ها اونو به درستی پوشش بدن.
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/15062" target="_blank">📅 17:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15061">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ: اگه لیندسی گراهام بیاد و به این توافق با ایران شک کنه و حرفی بزنه، واقعاً براش دردسر درست می‌شه و حسابی به مشکل می‌خوره.
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/15061" target="_blank">📅 16:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15060">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آکسیوس: جان رتکلیف، مدیر سیا، به دونالد ترامپ و مقام‌های ارشد آمریکا گفته ارزیابی‌های اطلاعاتی نشان می‌ده ایران احتمالا تمایل واقعی به اجرای تعهدات هسته‌ای خودش نداره.
گفته می‌شه تفاوت میان حرف‌های داخلی مقام‌های ایرانی و آنچه به مذاکره‌کنندگان آمریکایی گفتن، باعث این نگرانی شده.
مارکو روبیو، وزیر خارجه آمریکا، و پیت هگست، وزیر دفاع آمریکا، هم نگرانی مشابهی دارن.
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/15060" target="_blank">📅 15:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15059">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، سه‌شنبه 26 خرداد از اجرای حکم اعدام جواد زمانی و ابوالفضل ساعدی، دو زندانی سیاسی بازداشت‌شده در اعتراضات دی‌ماه در استان سمنان خبر داد. میزان اتهام آن‌ها را «افساد فی‌الارض از طریق کشیدن سلاح گرم و سرد در شهرستان…</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/15059" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15058">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6041510c69.mp4?token=HFSoKV0fgKoEZXD_fULvsoP8BEzUL7sa6Pfck165F47VJ9OSUJUKH2bLOjjmwLZEh_h7VGeVD7_xeJiDqrlrg85XL1Df-KwlR2dL56VS9CojO8VtT9JXYIBKN7QybMAOPE1VehLyBLN9UM1hsILNpyLlMVc_f1lYscjiltACUd9W_wTkxuWvVuW07DlkQBRCoQimElKsp5iP4Ap5OGRfgmwLpEsRzzjRKX4df6WDmbd3b59Cl1Ty9fvirWGc9J5wV45TdZi-EkAjkAzH2Fx8Y5D-A5TWtCzAgYCDR4LgoFiGCK65G06h1lQVFpYRv5HIF526Pr0Fd3mDmvBvb9xfiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6041510c69.mp4?token=HFSoKV0fgKoEZXD_fULvsoP8BEzUL7sa6Pfck165F47VJ9OSUJUKH2bLOjjmwLZEh_h7VGeVD7_xeJiDqrlrg85XL1Df-KwlR2dL56VS9CojO8VtT9JXYIBKN7QybMAOPE1VehLyBLN9UM1hsILNpyLlMVc_f1lYscjiltACUd9W_wTkxuWvVuW07DlkQBRCoQimElKsp5iP4Ap5OGRfgmwLpEsRzzjRKX4df6WDmbd3b59Cl1Ty9fvirWGc9J5wV45TdZi-EkAjkAzH2Fx8Y5D-A5TWtCzAgYCDR4LgoFiGCK65G06h1lQVFpYRv5HIF526Pr0Fd3mDmvBvb9xfiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با پراید رفته دم لانچر در حال شلیک
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/15058" target="_blank">📅 15:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15057">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرگزاری دولتی ایسنا:
محاصره دریایی آمریکا در حال لغو شدن است
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/15057" target="_blank">📅 15:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15056">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/563a3a2554.mp4?token=KkISdeacNOH1mBF5OtgETjBmTEXny_lsZWjZ1bjg8ZFofffS-hTtazjruQ9qEJr496rE4UsCwx8siTpmPhorbjS-Io-ra8Wh4SOQO0X6BVs4lL4V8k5__NHhFGS7WWQ0s2sDnZKBTXCgElAkUBYpqMmyjxhhjaC43j3ag2FaUTaywqUWLme3H7gzQiUB5Tl6yzx3bTA8R6U1nreQWJw-UAgwQvauirZcHWJW_2EkPeN2HbjWNY8WDcP9VihXpEgE90snKtx0jqlE-z3abYAo3XlndrQpv54NuSjGhTKurB_hCv8P2HQ3ZWC-tifv_KCks_nnkOs_FL1MYHNwbhjtAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/563a3a2554.mp4?token=KkISdeacNOH1mBF5OtgETjBmTEXny_lsZWjZ1bjg8ZFofffS-hTtazjruQ9qEJr496rE4UsCwx8siTpmPhorbjS-Io-ra8Wh4SOQO0X6BVs4lL4V8k5__NHhFGS7WWQ0s2sDnZKBTXCgElAkUBYpqMmyjxhhjaC43j3ag2FaUTaywqUWLme3H7gzQiUB5Tl6yzx3bTA8R6U1nreQWJw-UAgwQvauirZcHWJW_2EkPeN2HbjWNY8WDcP9VihXpEgE90snKtx0jqlE-z3abYAo3XlndrQpv54NuSjGhTKurB_hCv8P2HQ3ZWC-tifv_KCks_nnkOs_FL1MYHNwbhjtAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران حتی یک بار به ترکیه حمله کرد، من هرگز این را درک نکردم، هیچ‌کس آن را درک نخواهد کرد
این مشکل است، آن‌ها کاملاً غیرمنطقی هستند و اکنون آن افراد رفته‌اند، فکر می‌کنم ایران اکنون رهبری منطقی دارد!
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/15056" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15055">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش روزنامه New York Post می‌گوید که پلیس فدرال آمریکا (FBI) پنج نفر را به اتهام طراحی یک حمله به رویداد «UFC Freedom 250» در روز تولد ترامپ که در محوطه چمن جنوبی کاخ سفید برگزار شد، بازداشت کرده است. گفته می‌شود این طرح شامل استفاده از پهپادهای انفجاری، تک‌تیراندازها و همچنین تلاش برای نفوذ و شکستن دروازه‌های محل بوده است.
بر اساس این گزارش، FBI در تاریخ ۱۰ ژوئن از وجود این توطئه مطلع شده و سپس طی یک عملیات چندایالتی اقدام به بازداشت افراد کرده است. مقام‌ها می‌گویند در جریان تحقیقات، چت‌های رمزگذاری‌شده در اپلیکیشن Signal کشف شده که بیش از ۲۰ کاربر در آن‌ها حضور داشته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/15055" target="_blank">📅 15:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15054">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf2f513ca.mp4?token=bcEosgxdXGbYbVtyRd9nS4ok8-H34Gw3xK2PaaPr23Pd1JAVaqGuhreGeE2Z8DuvYJLQrJvvMQfSTwsUe8noZ-rX1qP2RsOPzgaxlvyJTZo7HD4hFBa_lE8VYQW_6BRj56qZzSue1cnEnR7yCfBdEtQK0tGulQB9H1sMnPuGQSmzYXtPl_tKAsNdtFmRkyUYRrhuJxS6l0qF5u1TL4sYxeIalhnhfBuCURFRjiQiG1UymjQPCOWwv7Dw76vXzpK_hepRa0C-UNSBrUh6bxLXx3T7QO1grv1pfE33Uouvk68Mrv0OT2y6-zNjZ8Zwi1QpIagCKmvSPJ1pKmGU3BtlFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf2f513ca.mp4?token=bcEosgxdXGbYbVtyRd9nS4ok8-H34Gw3xK2PaaPr23Pd1JAVaqGuhreGeE2Z8DuvYJLQrJvvMQfSTwsUe8noZ-rX1qP2RsOPzgaxlvyJTZo7HD4hFBa_lE8VYQW_6BRj56qZzSue1cnEnR7yCfBdEtQK0tGulQB9H1sMnPuGQSmzYXtPl_tKAsNdtFmRkyUYRrhuJxS6l0qF5u1TL4sYxeIalhnhfBuCURFRjiQiG1UymjQPCOWwv7Dw76vXzpK_hepRa0C-UNSBrUh6bxLXx3T7QO1grv1pfE33Uouvk68Mrv0OT2y6-zNjZ8Zwi1QpIagCKmvSPJ1pKmGU3BtlFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدراعظم آلمان در جی۷ پیراهن «ترامپ ۴۷» را به رئیس‌جمهور آمریکا اهدا کرد
@withyashar
خانواده دونالد ترامپ ریشه آلمانی دارند. پدربزرگ او، فریدریش ترامپ، در شهر کالشتات آلمان به دنیا آمد. او در سال ۱۸۸۵ و در شانزده سالگی از آلمان به ایالات متحده آمریکا مهاجرت کرد. پدر ترامپ، فرد ترامپ، در آمریکا متولد شده بود و شهروند آمریکا محسوب می‌شد، اما از طرف پدری کاملاً تبار آلمانی داشت. از سوی مادر نیز ترامپ ریشه اسکاتلندی دارد. مادرش، مری آن مک‌لئود ترامپ، در جزیره لوئیس در اسکاتلند به دنیا آمد و بعدها به آمریکا مهاجرت کرد</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/15054" target="_blank">📅 15:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15053">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ با انتقاد از نتانیاهو  :
لازم نیست هر بار که دنبال کسی می‌گردی، یک ساختمون آپارتمانی  خراب کنی.
تو اون خونه ها ادم های زیادی زندگی میکنن و همه عضو حزب الله نیستن
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/15053" target="_blank">📅 14:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15052">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7693c44486.mp4?token=MJIvv23lSiTH-IjeSK8hIEo-ii9m9N5Fp_12EccbR8Wp2t9ULeoMHc1mjydVrVbIBDWHDyZKpywpL2YDzI2W1wAxJ64x377icPu0safqWMh7kvHXIcDDPB6NOU3G44ovtF2bno1WYBRxQ57bwqVhrk_WSxZKUtlMO1rnfp6kqh6_r05830A_9G0FJ_zTYVji0O-y9U5-ysU55HCUnPdckWHu9Fm9Y9EBerzPUvY0GOU6YufI2HR4KUYsQ0O3jN_SyVZVQA4J12-whBnLTw0clIutKaFKSC9CbJ2oayBEZuA8tGVGKPY3s9xgqoXRcUumMOoSdhQ0J1I462PGDn0kRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7693c44486.mp4?token=MJIvv23lSiTH-IjeSK8hIEo-ii9m9N5Fp_12EccbR8Wp2t9ULeoMHc1mjydVrVbIBDWHDyZKpywpL2YDzI2W1wAxJ64x377icPu0safqWMh7kvHXIcDDPB6NOU3G44ovtF2bno1WYBRxQ57bwqVhrk_WSxZKUtlMO1rnfp6kqh6_r05830A_9G0FJ_zTYVji0O-y9U5-ysU55HCUnPdckWHu9Fm9Y9EBerzPUvY0GOU6YufI2HR4KUYsQ0O3jN_SyVZVQA4J12-whBnLTw0clIutKaFKSC9CbJ2oayBEZuA8tGVGKPY3s9xgqoXRcUumMOoSdhQ0J1I462PGDn0kRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : اگر رژیم ایران به کشتن مردم خودش ادامه دهد، آیا شما همچنان این معامله را پیش خواهید برد؟
ترامپ: ما با آنها در این باره صحبت کردیم. بیشتر این اتفاقات در دوران رژیم اول و دوم رخ داده است، بسیار بیشتر از الان.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/15052" target="_blank">📅 14:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15051">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خبرگزاری msn
: ترامپ و کنگره به هگسث و روبیو اعلام کرده‌اند اگر با توافق با ایران مخالفت کنند ، از سمت خود برکنار خواهند ‌شد
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/15051" target="_blank">📅 14:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15050">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ: جنگ لبنان مسئله فرعی است و توافق هسته‌ای با ایران می‌تواند پابرجا بماند.
به اسرائیل گفتم که از حمله آنها به بیروت خوشم نیامد
من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد
من از نتانیاهو ناامید نیستم. ما رابطه بسیار خوبی داریم
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/15050" target="_blank">📅 13:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15049">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ: من به تغییر رژیم اعتقاد ندارم. سال‌هاست که تغییر رژیم‌ها را دیده‌ام و هیچ‌وقت نتیجه نمی‌دهند!
فکر می‌کنم توافق با ایران عادلانه است
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/15049" target="_blank">📅 13:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15048">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ:
می‌خواهیم اورانیوم غنی‌شده را از ایران بگیریم
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/15048" target="_blank">📅 13:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15047">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ: ما می‌خواستیم برای دریافت اورانیوم غنی‌شده به ایران برویم، اما این اتفاق نیفتاد.
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/15047" target="_blank">📅 13:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15046">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ: تلاش‌هایی برای تغییر رژیم در ایران صورت گرفت، اما موفق نشدند.
چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، اطمینان از این بود که ایران سلاح هسته‌ای نداشته باشد.
اگر ایران به دنبال دستیابی به سلاح هسته‌ای باشد، جهنمی به پا خواهد شد.
ما از نحوه مدیریت امور توسط قطر در طول بحران اخیر، احساس خوشحالی و احترام می‌کنیم.
توافق با ایران به مرحله دوم منتقل می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/15046" target="_blank">📅 13:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15045">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5d35b80d.mp4?token=MHBwKjYn9SN8wGU_1IcEUEAuiZoC79RPygiADeL2YkTJEXlCVigz-U9SJDDUKNlIjl-iWkKV5awP9lG-leEhYiK8KpbTq_Pzcp7YQdZNAxSeMQjeLPVP4Rsy3B8O3uCGSVi42xY1J5P434G0EO1F02aKorsNQEfPTpmHfGpLivuruiSl3KmG72WOvyY_eB1z6rq2dNArwvU-pMXma6JSipmf4F0j2HeTlQohcEBIhV-qAAvw3P2BHg5ZcClf7iATwQtOkXjBU2TlXNFo6Lxgu2TORd9wj1ukseqF22M-BppKbjBVBNMBICybL0QGKXQHHofzaCWMcLIsod6FCn0P-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5d35b80d.mp4?token=MHBwKjYn9SN8wGU_1IcEUEAuiZoC79RPygiADeL2YkTJEXlCVigz-U9SJDDUKNlIjl-iWkKV5awP9lG-leEhYiK8KpbTq_Pzcp7YQdZNAxSeMQjeLPVP4Rsy3B8O3uCGSVi42xY1J5P434G0EO1F02aKorsNQEfPTpmHfGpLivuruiSl3KmG72WOvyY_eB1z6rq2dNArwvU-pMXma6JSipmf4F0j2HeTlQohcEBIhV-qAAvw3P2BHg5ZcClf7iATwQtOkXjBU2TlXNFo6Lxgu2TORd9wj1ukseqF22M-BppKbjBVBNMBICybL0QGKXQHHofzaCWMcLIsod6FCn0P-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ما هیچ پولی در ایران سرمایه‌گذاری نمی‌کنیم، راستی. دیروز شایعه‌ای پخش شد. مضحک بود.
ما حق داریم روزی وارد شویم و اگر من بخواهم کاری انجام دهم یا کسی بخواهد کاری انجام دهد، اما ما هیچ پولی سرمایه‌گذاری نمی‌کنیم.
ما هیچ تعهدی برای سرمایه‌گذاری پول در ایران نداریم.
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/15045" target="_blank">📅 13:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15044">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: ما هیچ پولی در ایران سرمایه‌گذاری نخواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/15044" target="_blank">📅 13:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15043">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، سه‌شنبه 26 خرداد از اجرای حکم اعدام جواد زمانی و ابوالفضل ساعدی، دو زندانی سیاسی بازداشت‌شده در اعتراضات دی‌ماه در استان سمنان خبر داد. میزان اتهام آن‌ها را «افساد فی‌الارض از طریق کشیدن سلاح گرم و سرد در شهرستان شاهرود» اعلام کرد
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/15043" target="_blank">📅 13:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15042">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ویس میلیارد دلاری ۲
💰
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/15042" target="_blank">📅 13:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15041">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ویس میلیارد دلاری
💰
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/15041" target="_blank">📅 12:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15040">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/15040" target="_blank">📅 12:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15039">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/15039" target="_blank">📅 12:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15038">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScKxJtOemPRWFwZJh_VERnyqaFTAo8uS6DCfnJUuD7oIZsR1ovnCOsClAsrIEcoj-eCs89ppUiPxrWkVSQmllxRMXUl1iAV_NsiOpzOk93FTHIJ2g0HdTtjJ0OlCl4iNPvapVzGEhNrR368dPLz2pJhg2_FMtBgcpAs8WkIbPG3pwQlAl1E1ZE6ppe5P88_mWQllX_97qY3win5YkmWj_m8-3xq5ac_ZtWM3ygjnHWESJ1wNWaL9NXokFs3QSIsjAkcE12Co1vw9qDXmAoyPW-brIsEO57cIFUCk_hd5fplbLHg7Lt-kWK4Yhb8StOKc6lDuAWEc3r4BoUSrrQexbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی پیش اهواز چیزی نیست کباب‌میزنند
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/15038" target="_blank">📅 12:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15037">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/15037" target="_blank">📅 12:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15036">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ارسالی</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15036" target="_blank">📅 12:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15035">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/15035" target="_blank">📅 12:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15034">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">چپقچی: در سوییس پس از اینکه مسئله امضا ( تفاهمنامه پاکستان) انجام شد، مذاکرات شروع خواهد.
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/15034" target="_blank">📅 12:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15033">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTrebfZtWGwrGV0mUYOPD-wb-Cus4lSFa-4esL-KxeQwAwnB6TJbX6JIv6KEHea_EY6GNaZM7yDLZpmngxY3zkjTH6rKKgeiJ0IpNYTXBtSUkJjVzECSUVAonfNwKA1GU-M1vfgufaXWD8eRmzTSHrVsvRSHLx2-TyqCKERdS8Dl7NLOCXEBebHWrA7FOqoFL4S3WwT3aaOjbM6tEfkcdC9xNuwFQ6mZnilnyIrGt5Ob0C5BFnn6lEGQPh3nxqLReK0Rr9MHlrazyo5LKQwoRkWH3eeVwkbsdyTTqOQ5Maa9h1UJQ9MiDUprJroAaacYYidwuzmKLuIPD-KYFaXjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای روزنامه همشهری از متن و مفاد توافق
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/15033" target="_blank">📅 12:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15032">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">عراقچی: هرگونه حمله نظامی اسرائیل به لبنان ، نقض یادداشت تفاهم محسوب می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/15032" target="_blank">📅 12:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15031">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کیهان: معنای سکوت رهبری درباره هسته‌ای این است که دیگر مذاکره‌ای در کار نیست
@withyashar
روزنامه کیهان وابسته به اصولگرایان تندرو نزدیک به بیت رهبری است و مدیر مسئول آن مستقیماً توسط علی خامنه‌ای انتخاب شده .</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/15031" target="_blank">📅 11:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15030">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3bf6e0591.mp4?token=PElfhFm3I_Ukh0bpwrgyTPNOwPG3TxHgRRmfVduMF4UGixDGhUCWszJvmoxQALDaVXPlv_IkB4RNNWlBmUXuiZcbCAd2BFiiSjowekA2VAUVQnXk4_lswiMC-3pPAzAq9b-Q5SiajJ7JAu7z8HNClWDAPfPDitKPIAadvqObbNKl0t4pcS69ueJwbZyBF2sKNA_lzFgbnAKbDdAHurMK9v8Iy3tpzilQbWhJmTYBiQ3-Zt6FqatKJD3c9YcRLwC9HrBbZuLBoox7_WRMWedOXFmcpbitcbQwUhXKH2vttm6bAkqkoPjW6wqEjVBm3Rmqzv2rnZXjL-bs1WEl_hSpcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3bf6e0591.mp4?token=PElfhFm3I_Ukh0bpwrgyTPNOwPG3TxHgRRmfVduMF4UGixDGhUCWszJvmoxQALDaVXPlv_IkB4RNNWlBmUXuiZcbCAd2BFiiSjowekA2VAUVQnXk4_lswiMC-3pPAzAq9b-Q5SiajJ7JAu7z8HNClWDAPfPDitKPIAadvqObbNKl0t4pcS69ueJwbZyBF2sKNA_lzFgbnAKbDdAHurMK9v8Iy3tpzilQbWhJmTYBiQ3-Zt6FqatKJD3c9YcRLwC9HrBbZuLBoox7_WRMWedOXFmcpbitcbQwUhXKH2vttm6bAkqkoPjW6wqEjVBm3Rmqzv2rnZXjL-bs1WEl_hSpcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبی بعد از  زدن گل دوم، با نشان دادن اسلحه و شلیک نمادین به تماشاگران نشون داد این تیم مزدوران حکومتیه نه مردم ایران
این نفهمی او واکنشمنفی‌ در‌
رسانه های جهان داشته
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/15030" target="_blank">📅 11:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15029">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دونالد ترامپ در گفتگو با CBS در واکنش به سفر کاروان تیم فوتبال ایران به آمریکا گفت:
"افتخار میزبانی کاروان تیم فوتبال ایران را داریم. آنها تیمی بزرگ هستند.
به قلعه نوعی گفتم اگر اینجا جایی نداری شب بمانی به منزل ما بیا. شاید قبول کرد. شاید هم نکرد. باید ببینیم چه می‌شود"
@withyashar
.
😂
شوخیه</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/15029" target="_blank">📅 10:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15028">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ویزای مهدی ترابی باطل شد
در حالی که برای بازیکنان تیم ملی برای سفر به آمریکا روادید «چند بار ورود» صادر شده است اما ویزای مهدی ترابی تنها برای یک بار ورود اعتبار داشت و پس از سفر تیم ملی به لس آنجلس جهت دیدار برابر نیوزیلند و پایان این بازی، اکنون ویزای این بازیکن منقضی شده است.
فدراسیون فوتبال ایران برای اخذ مجدد ویزای ترابی اقدام کرده تا این بازیکن بتواند در دیدارهای آتی تیم ملی را همراهی کند.
@withyashar</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/15028" target="_blank">📅 10:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15027">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یک بمب‌افکن B-52 استراتوفورتراس نیروی هوایی ایالات متحده بلافاصله پس از برخاستن در پایگاه نیروی هوایی ادواردز سقوط کرد.    جزئیات تلفات هنوز گزارش نشده است. @withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/15027" target="_blank">📅 10:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15026">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ونس: ترامپ ممکن است که پیش از روز جمعه، جزئیات توافق با ایران را فاش کند
جی‌دی ونس، معاون رئیس‌جمهور آمریکا اظهار داشت که رئیس‌جمهور دونالد ترامپ ممکن است تصمیم بگیرد پیش از روز جمعه جزئیات توافق با ایران را منتشر کند
@withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/15026" target="_blank">📅 09:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15025">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">امکان پلاک‌گذاری خودروهای بالای ۲۵۰۰ سی‌سی در مناطق آزاد فراهم شد
معاونت حقوقی ریاست‌جمهوری در نامه‌ای به دبیر شورای عالی مناطق آزاد از امکان شماره‌گذاری ملی خودروهای وارداتی بالای ۲۵۰۰ سی‌سی موجود از قبل در این مناطق خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/15025" target="_blank">📅 09:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15024">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjJjvr-rGD2R3f0s7zYUJPAQHcSu7P2oGmKognIW73PuHt9O6mEd3UOl-96Bt2E3Hp3Y2mlSj4JOmpDhHRa0Jn1dcwg1kh-Mnxs0gUKegqptBg7GI-5JJzYjcoCn_1ZIkJRZWfXm8f9vqLE53KKEzXbWIe64jXItmhxBWrvYzx4e-OQzBwayi2JxIyMId83fowC1lxkbOYkWoGkCrtAP-6Mt7DWAab7H1yaROtvBx9ncxulYRw-tnRPJyKaxw5YSiofJY5cgezU4z6PHXJ7OOOMn8zoWIM00MxVD70szCV_as5W1GMCTIl03_0w9XsUK3f5SBSHevlyxCOMinrxeUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندین بار در جریان بازی مسابقه امروز تیم نیوزلند و تیم ملی در صدا و سیما پرچم شیر و خورشید به نمایش درآمد.
کارگردان فیفا تا حد ممکن در حال سانسور صدا و تصویر (شامل هو کردن و پرچم شیر و خورشید) بود. از طرفی تعدادی از پرچم‌ها هم با نزدیک شدن به پایان بازی توسط نیروهای امنیتی جمع‌‌آوری شدند.
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/15024" target="_blank">📅 09:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15023">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a672a698ff.mp4?token=OGDhXLlkh1bHfP2FgY4elIFRvtMj7H1StFjc23ehUOChndStNJcBcWNpz4ll-xN1jwtYHQ_S1NLuT1cTBgndHDJBPwDd1bTJN0x3eov8s8x1zcP-yM0c7jF5yaTsB-bgzU_a4WENn9HGHfRwHexzfYKGFxSQ2acw9d8atPr7-EP_6pFwFoUeudM2hdm44DZx0aGPQm7_i33xIVwLThI-V7E6_yNGFdfEYqDnfGjQsMPfP16IGCQzgjUe80r7pen57nVYQZ_WSDjH8t1_4xht78Rqlo9XWXmImWpZLYkPUW55vHDZlbaRbNoSrLckNqEUUImhpJAAO6BBg_xkHWDWYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a672a698ff.mp4?token=OGDhXLlkh1bHfP2FgY4elIFRvtMj7H1StFjc23ehUOChndStNJcBcWNpz4ll-xN1jwtYHQ_S1NLuT1cTBgndHDJBPwDd1bTJN0x3eov8s8x1zcP-yM0c7jF5yaTsB-bgzU_a4WENn9HGHfRwHexzfYKGFxSQ2acw9d8atPr7-EP_6pFwFoUeudM2hdm44DZx0aGPQm7_i33xIVwLThI-V7E6_yNGFdfEYqDnfGjQsMPfP16IGCQzgjUe80r7pen57nVYQZ_WSDjH8t1_4xht78Rqlo9XWXmImWpZLYkPUW55vHDZlbaRbNoSrLckNqEUUImhpJAAO6BBg_xkHWDWYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">7’—Iran 0-1 New Zealand
32’—Iran 1-1 New Zealand
54’—Iran 1-2 New Zealand
64’—Iran 2-2 New Zealand
گلهای بازی و تساوی ۲-۲
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/15023" target="_blank">📅 09:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15022">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ecb9fedcf.mp4?token=SW1aNsi4DTYXP2gqOOO-BRpknPu9eG8mZeqDJIl_7a6KvsWtEhoCux36ZljK8LmuhVp5l11nUzP551w5I2jWK4hep1D9osc4KDP0uNBjvuWQes1pzb8Pm0oe-V6R90-PWpKjSmAoyuMb95_KEqWcid5r61zlvQHSEU0L40WIQnGMjKm-1jvGXi_UBek-fCTQOaWTzj3bxVMDc-ol7dWwIHLj3roAj7B3iPgyBt06AmJbrznMSGORqDXz2SJfngNJRZHFgRBklUemztlCCVKxqIQPBT4aBR7R4xTivNxxzPZRzgEe3w6-h8ZaapT1P-P8Iz-u5j2SHUJex42_8Hq3oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ecb9fedcf.mp4?token=SW1aNsi4DTYXP2gqOOO-BRpknPu9eG8mZeqDJIl_7a6KvsWtEhoCux36ZljK8LmuhVp5l11nUzP551w5I2jWK4hep1D9osc4KDP0uNBjvuWQes1pzb8Pm0oe-V6R90-PWpKjSmAoyuMb95_KEqWcid5r61zlvQHSEU0L40WIQnGMjKm-1jvGXi_UBek-fCTQOaWTzj3bxVMDc-ol7dWwIHLj3roAj7B3iPgyBt06AmJbrznMSGORqDXz2SJfngNJRZHFgRBklUemztlCCVKxqIQPBT4aBR7R4xTivNxxzPZRzgEe3w6-h8ZaapT1P-P8Iz-u5j2SHUJex42_8Hq3oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج مکزیکی بازی ایران نیوزلند
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/15022" target="_blank">📅 09:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15020">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9VMIBbj4w-bYsgdJP5w8zOTWHVYfiSgF9KS07sWrEhmrTojFxv6p5c_gAZECSDC4Kx72K_Tby662QCVhloOsxyFwoqQkwQAMIXXkF-QDCTizHfnNvZIYp7XU6EOgBktPXzJuSjpR5wpMYAZyQN-g44E-jMw5EB7duA6AjlW2izQVsVIrNkFs1UcZxHTN6IKtFlYVN0j6jKC8ma0VvIJHqV0m9RQqht3TJr6DM1Q2fKHfXJQvIbP_5B2UZaPPlQ1pY5GGN8HP201gZYfx7Uw3QoE1-UzZq2tM91USAfZnmc9UhhqC7Pzs-4ttL4e4qc3m27KkaW392uvWfsictVerw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :ایران موافقت کرده است که هرگز سلاح هسته‌ای نداشته باشد! همچنین داستان اینکه آمریکا به ایران ۳۰۰ میلیون دلار می‌پردازد، خبری جعلی است که توسط دموکرات‌ها منتشر می‌شود!!! رئیس‌جمهور دونالد ج. ترامپ
@withyashar
فقط این ۳۰۰ میلیارد بود که میلیون نوشته</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/15020" target="_blank">📅 09:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15019">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769eece9da.mp4?token=qE4emNkVfKkqwyU5W03gDDvfrHEpCMtgbPmvHcalL8HPyvv95OOwRcRe7qD6YzN4-yJNg2ZmDNO2qlJIQUvi8xCJCjZ3NKccA4fqku2Dn7B175LDLtlq7pkVlVznI6Y4ACP0WZUp6IQsFEeDdZvY4Sp1iVgCFWVRCnInrAjUpzhDOLjHmovxSMnryWIPsbFNznuKUVgOUrEV_JCCgGnUkiskwtu2L7FTtpVL-n7kZWtL3mYUUYHUSomvtrIGsejvgAFRGXE3mnyuRMDBo_X2Djlrb38JLaRBEN_QhE5s4A2Hzs5A5-8hE1rib1VMrgC5_tNrLCbmr94U_kKRBmqM2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769eece9da.mp4?token=qE4emNkVfKkqwyU5W03gDDvfrHEpCMtgbPmvHcalL8HPyvv95OOwRcRe7qD6YzN4-yJNg2ZmDNO2qlJIQUvi8xCJCjZ3NKccA4fqku2Dn7B175LDLtlq7pkVlVznI6Y4ACP0WZUp6IQsFEeDdZvY4Sp1iVgCFWVRCnInrAjUpzhDOLjHmovxSMnryWIPsbFNznuKUVgOUrEV_JCCgGnUkiskwtu2L7FTtpVL-n7kZWtL3mYUUYHUSomvtrIGsejvgAFRGXE3mnyuRMDBo_X2Djlrb38JLaRBEN_QhE5s4A2Hzs5A5-8hE1rib1VMrgC5_tNrLCbmr94U_kKRBmqM2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس : هیچ دلار تخفیف تحریمی یا پول بلوکه‌شده‌ای، نه از آمریکا و نه از هیچ‌کدوم از متحدای ما تو خلیج، آزاد نشده
این امتیاز فقط وقتی بهشون داده میشه که به تعهداتشون تو توافق عمل کنن
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/15019" target="_blank">📅 01:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15018">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پرس تی وی: ۳ نفتکش و ۲ کشتی با کالای ایران از محاصره دریایی عبور کرد
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/15018" target="_blank">📅 00:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15017">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">@withyashar
تحلیل وضعیت</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/15017" target="_blank">📅 00:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15016">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwlMhBI-tkLKsXDf_hzrnzCalrNaLss1fIk9hAQXkQ47wmDQaitP-mws8gMw-S56GrOIxHyrTJwuIHiqxWy_9ZFrLQEwwvhbjxam4n5J3_98NP6Ls-vdT3ghLy7Kg4NydDr7Qq6XVrwHGxx31jzQeqw1FWDUlUoCTuk2uHz7sh9YH9McOeg-bxpk9NPb6VcUM7GX4r5zlA8jxuW9uza3FhD4yuevjso1amCN6D1J_vWC-6HYb1YtpSwu4uSX3uTak87Dr79vl_erDgwF1ox9KpjU8e5yAOf2xplPB0o3rlUJYAAlGVqPDEnIMI4x2PrnPtJS0dre26Ngg3EYC872lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قشم  سمت سوزا همین الان خیابون اصلی
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/15016" target="_blank">📅 00:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15015">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صدای توافق از قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/15015" target="_blank">📅 00:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15014">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3QHiQ5gSlpey3O72gFdtattvzQ8aA4OhZrNV9v0BRGgMaZj4Tau9umcCZSF9EqMXq9FXWMv8OtE25KoSMZD8D24R3_PZNQARwa1_btOpRwPLSe-vYBIgQN54DqPXvFRvDYr8jVQOjMf62Aow9sR0zkIoAY5tRMWvBUujwppNCXmoNaYouHc2pN7mS6RIRG6c6jwk-iIBFNKCZiS2WObjiCLsF4_t_Bhd9J_xQTzoBrJJg50rTIjYx89-yMpN4kf4SW_3yK7QTUP0DoEBMY2cjTlGl9C82EKULMdEiIzodGMkJoQgiipJi616jZvn63tody9h7TKjblY1wFmKeuM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
توافق یا عملیات فریب برای حمله وحشتناک امریکا و اسرائیل!
⭕️
مشاهده تحلیل
🇮🇱
🇺🇸
🇮🇷
👇
https://t.me/+hLt81qXCGTQzOWQ0
https://t.me/+hLt81qXCGTQzOWQ0</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/15014" target="_blank">📅 00:01 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
