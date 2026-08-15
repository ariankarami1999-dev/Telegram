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
<img src="https://cdn1.telesco.pe/file/owzh1-RYE3910EXidIUh2-9TTE0vRgjOh1ttAmVnHUtVAkvvvtVC815l6SLY1K--dRW8nczfGmTjH25V2akMMAArruA3la0KhwyjlS3PoKlTwLNV4fV3A-myITQM-4PD5zLz46QK5AGs-1Bbn5t3YjnpySlBmpYSgpU3D1yXOyrBpmwOdQSbOTWIkvdt3njvVKE0O_CXze0HGFgsGr3FiDdUrGZzsZ4XGn2FAPM75LxdZ_nHXknZUMKH4iOzavXUE0AZOxgC0AhEVJzvaBjEE2WQ8cs38c7srhj24jIHl1faQRC8L4Za9i4GWp8Holp_2P2ZaRd7CpTamyYjeqKLAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 09:52:06</div>
<hr>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=ks9o1XfAzQ71Kx0ycj7hI4jTnpLw0_1EXFwzC7BkRHGJPx94zTfctRmJgyWG1zKec4n5Z-DnhtbGxmGgTqQD7jR7BjYjeOCjvNYN3TdC-2A50HEi4HkZ44PRr8zvmz8rc0POKd_9_EKntD7f_R11X4aKU7n41kvdJK-aEIDDN5pTbg9x9GxC5d087LKibAY47VwcQ1U20Aa1DGthJeo5VxKT_GJFCy9XNDPibJKuSHWerDc_nzrqRDrkCJDkdhn2Ope2UnsA8jl7aDYLmBkgRdyLMQF1tMQMag0Unk3UNok0VsE5LSZ2oSk9htLdUVxhjXtG-GJ6QQAhANYrYKUjgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=ks9o1XfAzQ71Kx0ycj7hI4jTnpLw0_1EXFwzC7BkRHGJPx94zTfctRmJgyWG1zKec4n5Z-DnhtbGxmGgTqQD7jR7BjYjeOCjvNYN3TdC-2A50HEi4HkZ44PRr8zvmz8rc0POKd_9_EKntD7f_R11X4aKU7n41kvdJK-aEIDDN5pTbg9x9GxC5d087LKibAY47VwcQ1U20Aa1DGthJeo5VxKT_GJFCy9XNDPibJKuSHWerDc_nzrqRDrkCJDkdhn2Ope2UnsA8jl7aDYLmBkgRdyLMQF1tMQMag0Unk3UNok0VsE5LSZ2oSk9htLdUVxhjXtG-GJ6QQAhANYrYKUjgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eHPHfCkxHzv9U7wnaiUJyNrPbexjwPIF40x9NC08JRsjQK1W7uDwzM3eliM39gRuxaNH3tsZsMx6o5rurIBMDuAsUtun7HnN_Jg3VUDYFF3r0_Htnf9zfq_18cN_-EY11w1mJ5lBY2MRk-Wq00Z9luv1vD0l0isQRAbmDR4TEYroHhQ2oI5uVkNqCMCa7E3BFV4mqNu9OguR8_gBclb14aBOxuVUNGTsFn5w0blaB-9OGbwppG3fIQdX9BYxHn3XYI6ntXFOOIeQlVJS6ISv8doiihJEOqXuozXBA4IbZK3zR4ClHOOMnE8C-UHQUkr6BPs8Ku6SPErU07zWV_Rk0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NwSG1UHoIctaWmASnMql1fUqVDub6WeDoaaU3l6StPk1OawxaewPWd0k1RmjrghLnDbyRlz9jp84ZEIjz-0wcaMN8yPSktJVGO1-KtYCnzUFb32p6FtpCiihXV2yhzzfeea6b6jFN7XWx5SFTg0to4msVfWiHJYSxYu6xyDczmEtTEYP0DkdomF8SnjzM2jqd5dSxlm3q3lQo8I84hE-s89GSIBnEb2Osi0Mh0Tm10drBQHtfmbaNujC47vlkxnEU66CsWpl9HJYG7Tm-ClbCmC9kT-ZTvFkDIPidfcgM9O9P7s-foR9ccrrZ-wEd7IVf3h6Ox-ygWXXlQRbeMlogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vP12sJno5Lt7iyjINSy94Q1quUeLHc39sMwMV2UVskcPXmKUo7yC-vehwhNw0Tluo2y3bDffsvA8jBXgn4Bkfx8bWKi_JkT4gFtjsMlhpyhRFKEBwfEgDwcflKJ9Ec8SuYuvdBNYUptzhCMYYA8CZWgwNxYx3KBMEoZIlZokuIhvsAcZ6nKH9o_CddmoB8RusRMW7YtIR1fBZLVJhJ3DTocBQh3KHntObvOyFTHrY78XiV6rKbOvPeSsrnpCW4cLc2uJmFJSHH6-MFz43nl6PMoDgquDnEcRcRcWfiuLumQIEJNkkLYV8jaenRXD9f-DpONYGM7xFtD_qZ8OSA2G5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oW8tSkr6FfI1yGlcU-RvRQry4nr3DI1m3ysFDBPwfUXy5OgUZQEB6Ne6--86D16GJdVzn8Gf8IM6cImnB1oEYotbEXv8RoX86MPJmIQVrx7TY20TtPYFfXpFfY8eU-A1tyrPU12WVyiJqSlgm32W0u2JpHiS5H_1sj1wB-xqtVzfEVcLlEEMqImZb588aMuijrJ49OZiO9bJZHhA1Bm0hWEC0teAB-dJfJTu29qSxAetE9JkO12jOs8rbHL2mtselDiwmW9ZLHEfryc1NknPqgIAhJDxcnurdT5BHsA22gboF8t-NWkWAEsizqaA13FY1aNwCJth6MCpHf_EGWs93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iDIwiJ4zHxToIeSV-m50-LfRNJfBOTgT2CJ5U00oMemE4HzUyYVrVHFMBjnAF0ZfNei3sTLRkU1iX3GYVQHbUI34Y-h6HEGM0TdBJUjvj2a0xalzR9P2wCRXDo6tBgoXmv5tCOolCWxZoaAuetyQXeTZNBTdoudGjJGa47SQxHqPP9NVLVUdyr2KlhOMv_j33t7asVuVOPugJHTKwmm66QhIpTCKAB-CIMrcDnPVx38lxCSlgPxAZMvOivSmcNt-4TK4sl_URN6MRMISkAQM6ZJ-hsc3umsvFPoFKePefih-3xraiCKS8z-eaHDVADU5nlvJl8ZDExwegytSVJi8Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dXsZUzuQCCjEPoP2G5WVXB1EzajeGa4miNqQiFpBZ7VWbnk6ES_-biOMc4vy3B2dlhV-OFI5v5k2A5MLmyK6oC9xwwdcAFgwX3kQEXaoeN4mXqPjeafZGyfzhxlza5jE_jA_pMCeGozxznrzzX9Yz60AsA2TCFCV4pLjw47BCl4nLRGfFcXm3sOXJAKQUALTrVAFWTA2s-LQK9gIg_SD3ehdHoFMQoAnndPGP3orRWrK1jGVlZLm6K2rkLaA98BeXoHn_tWCyCwDyg_hDM48RYYUriwRY9vS_2oiCC-oHfwge8pwPrsy8ofEpOGUwmGEAYNOg1jn2dYxuuAz1f1xZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nEkdtzdhe7r0QXBNPOVX7G95ZEPjsuMqW8aP6lm1tc_kA2MiPcrk64BWyuZcHAvI-Ks1b_aOjFP8d-qpMUBGO6s0j969TfGhWmUo0XH4Pz5sRwXeUsKCRIl5HCiLTGoFGZBkwQ8riRT88KRClChkszD_yoh0SSo0f67Se0b0owvsz_ZA3ljMmOSXLCfu9bnKhcgpk2hHH9e5e28VLihlo293yqDHp5R55pR98TOTEp9T4nec5czVTHZfYfFT2-c4ay6OdFjm3MvjLNYHvp6aH72dGPGCLXBHCcGHdPpwiCLz6G6ER78d25A5vXrwpVNoxseZwSjZyOZbu4sU2sn7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AcPh9-ilZcawwr0gtLjNpFlN7pMmmg3Min5eEAzPO8-enrt_Z3ThjkuZAw15UXlfMtHwIbBNTAzv4dxKcMKAOLtOGsFC7C60ji9zJlHNJzLUVMJtqKd3LsGKt5Cvn3uUR2AAsyG6HqylHQ5WmfCV8lXVARaV49sxvuVvdbONHX9Ia1OxEIPGBYPvVEAw4vxLowFuq7GoLRN-EDy9hDVW9-pnhkUivjTaLYW9jKbOvw35kp0jK7TpU33vdZBaMPFW9PvEqDDxVy67Ahdf8GKVhw9kH4O8SBYJErwsJCLBOwy_ob0bgKw3qkzJ9y2ND1rFrDth3a9yzTwI2b2xIsCyxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eSGoR4MxEFIpaZvvWbLnI0vEeTdNRIoCw-XirGaHEQPO5JuXnO0PWc9i6ZwHtKZLqgwJ0CEo9goDiDIDgfEfenD6rpZ-ha4cLDZEZQmya6H4rmrYYnQfRfpCzvqJlLzX5r1lXQ5j7EkgyqyFO128EikwXf7fHLgqQo4hkpaCSQHdxMyDpGpHJa2vapWaMhrhkTJ2CmkgHM-SMM3LR7BFnmv9woYlzfMel3-sT5G_PWCXy1MqV4jxOFbtSGHLfjnInUfh42gb_zq-NZh3Y9LikQEQKicD7rb1KAQ2dO5wtGobtjZ9PSoYWnku4H4SkdmGo_zdz1YVEGJHWCE7BvT9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AL-CxF8QFwbCwHWCMkjqIVnBdCVlPOVq_faBE9ZOReQpUATcrCCb0121dpgggRh01r5ggnAmA2O6tE7fD0qT-e4ZGwKLMSDgGUA4R7d4UUGrCO-q-p0evTd339vnAY-GZ5BCLCT6arLGS2DDroN5m2L3wZgNC2ga3NVqntugwRrsX-0WZaYbh_H-2kAcAgQFbP6mciajXhmYel8IM7f2GraGSaJtJKRU0zSktLxv3tUs-BHlS-Z48blyq1jruimydSK1FHagCKfPvLEWbEYgoNby8bH8r0ED31JuOXnPXyZ3lbJL2bbgCykF3SgkFBAbqEvnsoyJtEUJ8VmhJlWNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RySNjka6hDn7vGpcw5YPeIypglrcGGwv1Bb9mVYk7pzQ2x765SVmlzUsOVat92ww475c6NOy1DOphqmf0Ez73Rm4u8mEVVyTL9sFPvGPD9DJbSW0zLGNRuHXY6CHJmHWKdTRfXNjB9QZd1Mw85o7hY6TiT0XxTMviliHwrjDyZzRtADtGISffr0YLynafgL3ljQ7L1ISo1wbNRAc8BqaUNrzl1y4ngL80miQsgpWhALJ5cJwO-8w-gaMfM6sHJOpePRP9nJP61cRu6joQDg2ca2TkwWawyxnOI8pcgqO56zQg6_6cDgZDi9ylehcgSFQJhYw926QfzCVb7KFpZdbUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DuyJS0DEwDpz43KZtRZed-4veyJTqIo61ggvkNd7jyPO9C0T9F7HXdDPyr6DadUr8IJOkZPw3jRhGmhNCAmmCJhTKXT2pgE-skuysE8dPSjTzG2gf-e0v2Z45Ohk26izGbbqN2jOLCBIG_40VnsqWq7wAZjiR2yBGb-k2lyycWA7Q0GNKLRc_19eUrSlAbtXGHQiL1vvQJynoned4H9o0xloYWUpFiDyi4O_0bUzf_UzyE47uN_c4pOSmZg-n0jtCMagrcbP7zU0rlYjU8hpC52OU409sW1-3XHEXy1zDOq-2V8FK-YEdfTZv8vkD4mw0IgNn6soV_VAInbx2xRthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WEQBFrqdnH4AIQQwwRNlNtLiPq6_cL7Ssx_rzc9j_YNhWj4J_nybgLoxgo2kBwjwo6I7NMRD_lWekn1ZJUgdWoQqIT_J-Lvw26XqQRsyCOib5uPbE8jB7rFpkUOHG1i7SblA7qD_dSjaXDg71tYmr37EK5tDzqrlkc5-ZMI5quDsBKg-gyREJVnqH0xrUjm3ukqq_M_u0GWoo3gVmqA70Kbyi2dK3__eImfWMdSVyXSIijFSTO0Zd6ajuiEcCEZ-VaX_2lyL_I-4J6b8k9-4oNbvZ39vxiyBYbm32577M7ltNqmat0mKofAUiTr2Clg23_LUmFD0d9zNwsxl-a0LoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KRl-VyxG9S-mmAYQEvfHj61WJ7xt1Ci4Lfz6JCsReZ-TpJ8aaciLijOCMsKZDK0lOgBWYghRtdKWWR8k3-6JjTrVfqtX1WAPr7ey3aVqzZ-l6Efb8pN6yNvyFh8Yw6d02RDgPGRMaWMmUZmH9ryGcViuXW0unHt6dKsZQJVx-v4Eme0Qfm3sqhI2fx3bq-N2r4Nfc4pq7uoSXq9QjniaOgpGh2TIwTdCCF6kqThs3wWczhit8ZyMLzJbAi9ehTL65e45u_w-So7pVFB4XBiNI0pXwoSG4ZwgipziLeFGUr-sQlDsPEhjHwbIDJAbcCHJb7ky_R8I9i70paSxLVfBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C89YIU3Sy0SybBZ2o1hVpBFwUJyhZsON5Y2Vkm1lwl33B_kVn6a9SRHP_PTh6FzzA8GLBZyz6ObO-UyTCYNH-kSXmiH8C4YAizqKq0rmVOT0QgfRD1-gvgSaKAlPoRU7qwKlJshRnFV-elnyQnYfPkTRX8csA83mWfG4vooauuc57cfkUUXxbpFM1O1Ob6ObdJiYVKwtJe5MNOR3J3RybIlkOnNlaZcLIeybzhT9SzweFhKYFumHIGwv6BooXLqD1RX4W27hkNAZFHaBQqXpuEc7FGyEPmV8HVfAeaHVe9UqepQ3LU9M6JcHemee9P-AxeHyyKWYbDD_Y51SlLG7OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ii7Q-otoSn9uQw-Par4IADI_9MvXLzXgVfQ-DO_JBMOxQm18L3bwf3tMg1RGrTU4yRfVKVjtNsQGGXziJaKIiDx44JRpLWJ12qmDkGJTMULEayWqCB4Njh-8H7DlHtOgTT2GKX1e5GKDgxeHJscsLr4M907CT-17Jt9vxrk3ya77X0Au8NP_CGpTXyVE6UP_5E3Q-vA8Hz5VDdulI2YsaHXX9TH7TMaNV5idn6DxKLdhNqnZYuqGai-ThGiLPWsLvLoOkPJPBE5Atp3RUUOn0f02EkImCqi_K3UMGZ4zG9jl5Trs_DmUHgAYLQ7TIjjmNtnoqZPZAGyiUQYmTnSDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ELKz7k1cAAHPIsg1JakoYBAqSsFgNqzONkXoYwwgenPnPqibKYowCK6yuhP2MK0rQ_dn2aYgmk4Z3D6S1VSOKGQAw5Ou0rAYFv1sUp2U-qbwv8VjztAOP2ov0sQDoPMQx7br5imP5SqH2mqCCttiXYph87wXgexUDVd35bj6KnYuio6-D1vFmcg262LQb98RrLkm94knVbOdnNAmEAL5jYvvvNK9IUaRsal3ENjoWtQoO5QKSqt0e9LCr7G_s7EulrPp24rPBvOh1DiZmyQzX5YfkGJc3bNFIUyPRp-gcPOz_Sr_n_8sXZalXzdfjGXfFf1TUHNXFdJKkrrWnmSE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bN3FP7p2zNx8Cq_ARgnjzA-MBSBpqGoby3Aor7kE2FRtW4-98sojbiGeeW1mpCrnzr4TIWp4JHAuBkLkheCVlILAnTasIAePwOBAKFWMCwT9uIpBC7pPevEd6ND98per8Aunawsz-NNa706iksvw7Z4BdBRFr3FWdK7iSKS7tJa7ogMGdP9LgrPUgADIOpJ55vELMsbAWLADuuqD3qXdOTQ-H189arbpZ-BJYVxuKzWrtyosG4Nfvb-okLClOOVoux2J2ct_ea1L-Uc_ZuIba67I1OML6MibuoOHrkfCk8Z2w3jdk4bPcKBVi0Ns-DQ2xsuw8TODXXAwKVC_mxhmyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n-QkfbZuodkusdhukhUO37y0k155toAfW58THPsrUfBpPT7BDmOUgamOsR5vgTNZtvlj5bpEQ8i66ccl2FDH5XtqzHZsmlj9XXEau0Dfvkku4lJbe1F2cNe8M36EjJMvvMvqF0vmr3tMMeVi8lEk40kEPggBmWdvhCCPdmbt5izaEm3aGYsKPInxUgadMaPX0GrFWXpfG4BoRn81DaKTvqQJMFHkgL1QQ0kib6YJqXH0wDjUWoEYOhCNL4vwh_FWRsrjIx1Rl8KmGy1pcVXhwjgQB11PdoaAu8qdLDLajfH27xDvRKBaFVe6twf9KxAJbokMvGJf7GSJhxIIBIa5KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TDJ__9tUuotgSHj6K0-lMTahbZkiziCvmWNzKhMD1inzUR9kfztvlrDlrOkVGJHF5N5QtPL6pegSIbunk38JHnaecyUnnML8j4WwfmK7EmJdVPxsSHgjwj3EWT4NPDfWABJWrYrLuYhxSmws9_Wws6K2Hy2WwhXBuJ8EuCIuOXnZkduJ8L0fOk356Sm9zGyl_BHsFKReTXJX0OIduo2gAjz1k_Zu499_fCVpEc9-CpT4k-qocVz8OG4plMsVir64AfsqstvNH1s1DgXFO792cUz08FFOBZkrQOkoub60H-0dKSb39DdaUlpPEV6o0xiF_hnqVnAPMhtbskRqH2IQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oXXxksf68B4gR_M_OQupdvvhRnbATDrg6Pl3vKBdGbqeKoKlFp3WX3zRR7ylgd65Sm_0mNBSWBCqFAayS9VyjhJY1N8F1jQGfRgId-QJjjQ7ji69daegCjpiXB6bU3OAO4qQDsiILdYtd-QQ6VcOY-AcfgHPD4VWA2uRjQUG9gPF8iBKp1cyVoz5TFmQUPfwz7ySXaO0JZ8jRByt2xkFpHgG__wmxnE_ua9FfFzys0HWWaRDp1FdY_KL1iJ0OabUL2M469qXO3IaeOT9NRkpsOSEoxipBZkxnWeDV3aNEPoOwd8CT4zGwNSTWVbPiHkHMK1QLUtVtYnouFtoEFrj-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pQ0X27OcYuuGbBN5ZdLdDGIX_VN6QbysB0S_POsfsJevx1xWqphaXs_zMJIWskybF1FaXcOzGZJ6vbuPe9r5qvJX1BaglFqFBKi1TQgRSFnqVwCzdun687S1ShunkZpE2GbJVL6Hnu7kHyXyPoYAOGVW7DwsW0hlt6w6rOFnnfIck-g6cMqvM10TAoCZX515H7w3brMC9vLs_XXxo0S7iiKJMvnMCntWMk-2jpAN1JhWhgLoesLI7PTIV_V3nMSjEj6BPZqnHQ90DoVse5C_asHiIFSSo7giplSQ5XiaDdWgsrgIwSjuKfPK2tNFlBR3LSu5_VRE_m7lDrXRT6SXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/msL5PvmHc3oSEn7PF0FqpSmYPUBXvpMd0uSmaFmdL7CRfkBpHyg309TPtXaamqUqcVEkS2uqGaB-8imvhBqsnxJN29dxaxTg6TPVGN8hmVsE1sf8uY7p33Xxk6QW2ccGmiwlRWSHg3hDaY9hgiDH1oa5D--LWW70FydjYFQw3dUm5wzznWz6sEYLbUepOxxNenkwb2oLl2yLnqYfO6CgdIm-m1S1WvxYX7Lzc2E6ZpIffKdX7loFbbUI9FDCHUSTeJb-UGO7IX2AIINtNrOFzvL3rb8-X-0_IOfL3PJ3kpHaDqMMNvsIUOp8Z08jMjZJkdWqOaebIrfT7qZQHdt4ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JUzwV3qlCKVsl-75fszQZSSFnBqueGjavT4osbUgB77twe23rVsvWtO_uUc9DAxZj2mK1sA75aMjcW2-9-MdI4a_I1rAzYpeTGNZyDfdhc1eo7crczTg8_7Q_mYWDKaVWUHi9mYfGeYJ0LypDvqwVa0v69F2emrVqDBP20jmWazkZQ2D75Z_EKRp8d6cEh9yccBxJPwHrGIRlTrypdzxDXYOewMGrx9qSAFTyTsrCe3vRDwygufy6bFX-07vD7tdXkMqAwqvfnlJ-RXblYk0DPcOzmFpIV2cAU18b1lzHLpVjudc6G2NqQVSAY3d5TAgG4gHZhYvdzA5z49yOn2O3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GpLXRD1FoCxoXXU5BGjNC7WkJ9NGiyVx2Va3gFiY35RWz_pJcL9QTXuyhHL9LL_G7UO4wakBzUZZsHxN_LCWAuIWP4XBMKvkP6tF60rYOoR_qUSpz9JLEOb3LdyJBk-eIj77z2k4eIrT-m6uTqTqBqqvKyPtZUdb1NBX9-JvkXUMalx4v652MgdJnUXXuUjbRKQ321ELhxsiu9QqbqMY7nV0Xy1Dppp3lnTrKhM-UotePTErh0yy0BbciWETS_OCrbvXkLWYi2xRjUWhONuku82yiFBYp4K_rldtRFoXI9VLi-yocXNK3skGR1E4DhQUDvC1yox_6cTWwL3nc-oeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U_0i2umBXAwfxfkV5MJBImKYCwrQtjnia7a2r36aNU6RY6c1Of1PG3frVKQjpN6zCDfhDiVsFOVipBAGT2DZA1FEltTUCNPPacOyD2mwiS5O8FKK3CyfqmnZFXnsC4Xk3_YSwaW-5tMP_QPBuOKo85-MkFSknAnQF0eYZriLEfurZzN_hEYExSeqlHn1DDa4Ft2OylWSZjtYYzJ6dxxbOfekEC44LoFYUHVUqqAzvwKpFZ0dpS9ARdb1U45JIZBn_Y9dRQTlV3G9T4dZq9Xe2fESTu3EUmRPokz5qxIdCrkF8TfF4fQf67fSJ8qy-nMrVWaGM2Vys_W9o87qEXQvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pKiRmsbyWLntNcCnOO_lP4LI7hSTm1dUpGx-xU8c-Lt2kqDgyj0rDHpOhGueAUmLbDRhDv2UFkUmFVv4yPbNFEucskdXJDS11X4_fWACaWIO3Xtu0gpZM_kYDYr8PdbThmif1WvcqWti9_EL6YgBM9C7Lg57YiYjobjza_HaAinkpwD-8OTW9Ez37IXOxneLmNKorEDSIlcJ-NrAI3dbSiN4K_R1go2V4xiSbH_OJBjbNBLwxs_eFkqfBY9r0eaciAAOQJSBLl2i_VOmf7hSOVcNrODcGB5Kh6Ztr4_ylkczX-87cFo_1Hw9ROGL9gxmFplEDjOLK01428YpMNmrqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c6WhxkzRJRForYHcucOXN5BKzObVLEJvpvpuzvYzgidK_behzePlFEsfN95NUgmdwUqsOyxnLoK8-fwx2nD6c2YaSch1Mh7rsdihRnPZXOMClfq9pEXCH5YKyN8eMDNNaXNMsSBbpSFUlwK8fv7I3qISuzyLf1aohtj_2ALSfl4TsWM9TPg6AmtQfoUF0WQE9gnNyrMXIiiMbRMta9pxA_ZAKGbSCa4_Ix-LCrTCTnST6XHNLkSCCs8Q1BgsmSLEBB4Pj9qfvTJDmDNijkh-yAJLNo2EDB_1ZcG4_qLz1G9I1Q5ZQXPnpvHoZqf7BzCzPxwHYGUryqgrDeE6UtbrWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BfFeChzWup26kjGChfgHDJTooYz0wKRgnhmncKUcFHA4T9JqcUBNTige3AjjDWm7ZUIUU-t2FVoApDzKqyBub_YnbV5wd2GqH47G_fTmyp2qraOgO49HmuxVUScU41a9W8eENZlYIq7X-NcitvQOtUhVgCEmrAtie-ARVDLPhGzXSJLWYSiTvJBLR4ToFBJntYMp5eMEKGdaTU0qWPWfbwsTfuaD9-Hic2nhTv0CWn2fRjOW6ZoTgLaZ_XQILq0qGcrRrUuzqFkhd8xcqEjQtD2u9MIKMDOUAmhTktYeyYYEzxD8sburtmraAnvS3kZBt9-jOUEN9UlHoktXt_Zt6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bYggnOiFw_VWGKn9eC4sZz42--6zo32omxTD6IXTG7pxBhSbmEzBiUoopMjidDNVgCQINNeGs_c-m4QA-dCCKZOQG8Itx4bGKr2S5d9PCSnns34ZyDN5V6GS3HW8KUNqD19HIqJj7tz6-DfWRmwUApc4xf5Hvys0BcRzJOhytrszWkBOL4yNOkXvTEvU9jZ5PEmPV6vL7Oi72haUMbWJCZKeJeWzYfUTBJVqGsxSdWn8A-pPUiGgLXB-tTNKimqL9ceOup36rr655p_xuk0D4p8o3P-IWfHOXM0iG_syA3pvCEti_dH2NDq1IEqn555_vA8ZjXpJCaaB3HPNyTfYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/drCtJSxAvOERhXZzYJ9I9aJ6vODHHEoceSMus2BvSguoVyVS-t618iiN3551nYRY2egAwO0IfyCmfMX_e2AjOyzWhFURRdItB6f_DRwNI9QKySyHb-ou7D86_1RXY_BpHcQ8-9h_wEbXrgPgXHxRsmOcJDewz_rhNnSDTHyaE1ToXCq1ncHzMNu3tNgLbBu1un2He69ZhmZgbhJUIF_8T28jLBnHMjZeJFZrZ0UA-RVqxDszvHgk0mkP8KAKk_SYxAxt2I1abSxpqsyhuUXfSVG2zARGqiu3v4rwVON6giMa5jaNFpIMNvWgIgFnCXLV614zPXVOg-uwDi8UnT0SIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FEijT4iK-x7x1RGpkjTAUdrslrWKoAI7VgrgtXsY1-zpL_IsXEhsa9DhQWmr4lt0mWO7RlgiQkVr5TaMp7OUE53L9TMRGNiHW-B58k16FOahEO9HRI6AUGoTGqI8GMmddI5qDwRvDCKW8zmb9wsyQLs_9PBIL9CK_weNzOEt5y0sQQPIFdcDdoa3FVGT5csNlcH6jlLMbX6ztPRyjvbDQwgVOO7M_2jlCOxSJQnNjPSQKcHlEVCtehcldhsfnmOdoLWhehhtacc4d4V7bL8SZJmcvtwA7QZUngSQdRhhRMh825NrRvA0rT5v8ckMsh4cjLiaZ50ThX7J2-HXJCXOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CiM7_6pKhSr463wZKMiefW8dlPToEmNj_HD3vkH5OPMncDB2mG9hi-0uQvm6BCCrNXM_tLE4BS1cy1dt6JzwGYLVD3fYWKV_M1JxRDR27q62ghZ1XO7vN1zrSApQLI9wjD7_JG4I40m2rTwyQZ7v-OfGd84IfcWb0Jyjj74o3VLiyUXKuJN0-sCLLRwWXJQKq9ddFnx8sp90Rt_i-WZb8eETB-k7Z6yaqVgtVVe00BJ_eA7KA-Yqc5FWwp42NxlBfHqkf5OVq3GicRoy2nrJd688ogg2NRWbIFZbEuH48znhDS6LWWWVpI0NyuEjCyD97IH_tQVmd09SNLvWzi_EyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m337HmVEDcP1JuXl6Lp1y4TpZgrNaP2ak82465xXekIoitxScKsDW4CqbzX8w230YHnbwt78SP2ccfJ4jHJhXybZdnKszEjRvizlqaxvzv1lmvdj_LrhX_RIVb_-I8p3OND-PDpG4U4pti3WAo9-7D7b1BIs_ISlOmSsOFOlAkxwLk3HDmd4BDDfojuvsrCla2WToqJcw-zO3lzn8CtdmmPOA-ZaEIYam1vfKDjZvU6_5A3zpMEoDg4oQK6waMVN18G8l0-YdAS-USe7o6zg3SuN3Ktlj_oSDRTveTw5PH_mbATm0NlG3oys2rFbNpiD5mNtdVmNChaKIidi3Lhvqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V8Bzw2SqZuuWdffL6ziy1BSDTeUVho7wrJY2vLYUjUsYYJZhlUeGzuOCm2-SuQOl_aLTcNG9hYjZnaKNoZWbjx4-4kSJndJfNbGfyzZq4VWdSn464UjkFnBrzTQJnTPx1Ig9KAGSIDEgzjjl6dHQQyIgIts2jTKhL5dP3aQyQglZYup-g8djv9feIOaJfmXQvUBSUhgUMRbHysHD-CBwcyApJIcGKJ-wZ8xq2DIfjPQczYyM5PQf3-1P7eOsuloH7KcMccSQUQLrDbYudRVEJMtCpWUbNvq6w544u10UNaHi9o7CI7i1e90qYqfjZZyCwxRS-lOWPiVZjhKKuADBpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DFEPzXZ9rEx5W2CEQfsF9QD8Om6v2ev_OCNxKaQm-JWiYj5zGZ8fWNbGL787zW_J2UeaEQ-k7CNSvtcFrUKpD1rTRTMH_gupo-Af-ETv2OX5Vfxw7SvT4dDLk89PEv58__GH5U8hGr3hkOwOowRa3MhUy6wBx4fL93W1qFoeczw2jhWyrZ9_lp9viBeoLlo1GVI6EP63SJ2d0HEjfkMzUKNmFKW1Bka0yFTmjU9RicGnAMB8eVG7_iGxP2zq3x9AOv-9dPio2WfRRQZdUFXgMbigH62uY8-8RtI7bUldJkVa-A2znwwW63d8nwktkp2oDLEmr1ZLJD-2-lbwV2Qh2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xv1Z7Mt69Ok4lfTOR8Vseg9-tsnyzxY4c3Ke5KbHmxx_KZpOGg1vgkvrL7MLToHVGc4QjgiObOeWqNd9cMa3KtDCwl73M_IYTfgCkT9mFWxTYixhu5_Q1_vnHejn11vP_wftJF50MApU7qKVPCGrw_pEJhCXTzbbTK1EFFNIsp_785xf7ir5Q9CJfpV55ZqpWEXycZJhu1jU001MASMl2JeiDC3HHq_oEW0pAiJ_GwPRjVtSuvMIjGW__wZ-3akmxAmcYZBYZ6dLTRAggKJes91JuMk4W_ztn57Z3Xnn33ZdWJFtIKElVVS3SeQY8_zrd5jdtATYbY8c6lgHAgC0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aKSja6k-ImI4bIYPhw-mVmxXn84LpdhkDRj9jHAAjXQY7MOpwLddXpLVxHoboEZPmBkNPFExFS81cTVofWegjKOLnXOi7NWHzIS-olzLAvekXBQB8panlsm4ZesElc1Dk9-iQcuklESL1qqpyzBDw5_f6y1Pkphx-aU4VrCLB7ujRG_RR8vl4XhqhRForQbldR2nxIzf8_bx-HgPOA6u3q4CQLhSQi1dcRkVkc9r35xFcKEnpQEA38Ks5JvgBHjm3gLavK3n4CXG6c9NaC1x2E6AKxVGDvEARw4Xy_cLmiy_V-HpwuilIU7pHCiv3tyD4kVG1mT_Vl9zvRlIkoazcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UMoCt9NaH8NVlpLzTVkZbsHOl9hFCO-FaKBQkFSVE0mfRXSpUQfJjCNF1c80oh_zOTaEpvFXVRDOqYyIOodY_37fO9vcXaRLmAdRKNYEwoq6cL5f_wuYb8r-k_AjWEE1MTAQXUaXgD0Nd9PFNYA8ogwZ9_h7vBe6dUArCZMFqsbxVC53mP6n8IjzRii3QM09iXQVODFZh6ncnPpsym_B5oMsuDzxnL1Jb-ICXVUEdnH7vsNPbd_mjrf91n8ENCKyVVd9G2TErajv-P4um4V0rb9Rhn0RvVAZRJwRFgB5ec6H-qU6ef20rxIL6udJmSj-0hrYCxmxS1aUW2tTLdFWFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YXDiEm7WM44Q9-Wyg0TcNY_dH48g0L1vhypzCbC0H16bvyF1MsgseEr7BuArGKAEgcYOZuEPlsoOmwg1ijq6DcjYjxNu1x-JXRYpmEWdtd3_zm-NHA9W_zprQrBq3OLZg5q7pQJ60AP4HZLEp4xL3tiikpdix83eyPVvNDYo662kMtwIEmSBGZ7sZZGFlx1FsxcCRVhC5obTM0UVQG7m-YzKSaBH_ONOXk00W_l2ZTEF7qJkYNTkGXY6QepyjDQJmpY5fHXl2w4DvgXFQM-OR6EzZhDwcghKjLgQpAXz5j7gbjkHQTg68ufOjLTxkxPg6P_QJjZ6tgDKH7UTkaJgLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sAkXiEd5Pc-UAQDuEu2Cqhiy_279rUoz4GxkHl-Vv8gBbviRTsLwcC0JRVOk5WmUsUVjMimxNP9QiKdCDd8Ayx-ZswgOfwZO2tKQS98HME2fxrka-zlaJrmIq8oNAmpRahZNwUuGsm5VWqZhI8vgUPw9LThZCkxNw1AMfcNxM7iOTeJKpaBJrO7dPElsdcZZc-rlvNp1vK0_zYUl3XjxTvrkCrRb7lKn5Unk_LSTla5GZrVLzIx3WS78f-dir2oakZ6LTFkpzKdAOp7iHojwzWlH8PQYg7RxSJ1aS6QM5f6O3KTf9Jlsn7QwwzPcUiffFw985iN9_5bwfDUVPH7-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FPqONmY631YqPhwotNw8dVMcX4u44__n2gWh6oWaVT9SfZhJ3VCzEqoo3r4czXsC8Zbcs1wN6dpCOJCWEyuLjpJSlQBHcsGeRM-_VAUP__tnMoemgdyXz2FHvNMPETKxXsJ6-NHvExjxYDtlg5etTv4uAm9JXDQBEnUpAbPfQpjDPK566izhRMtybbJbY47niP5kxLp4OOwTi8w0MCAXuS8CTIbB2IIXnScl9VLa-BSfB1hWtx4WB_0uZrWW5aGxkHy1eeGPe--N8MMrWThVc2PorJ53brQEyjxnTYe7Ye8DolZ-PWEUkwsh__xvxsylSaxNdulCaD1WyWe4ht6Mbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ELWaOIElIJYxuCPNJNG00SKirx3oxD4JrQg-Smz70FA4hTR3Tlr9pbYW00tVtlmvF70FxX7ps_OtB0X5-NSLc6ucuzzoONIg-Evksp_tXVPDF08dtuC1sUZeQn1pJ4MH5uyxKQKvNi5ZeUV3uDskFlRwoXd86YK7bxo4-Mc3-lDBjJ62D3WF9lpxl5xDq-P8dsHAcaxGGIPbOWjUjKsjclXB3d2yq2qNmECUl89YtZzNb5YBgo1FnoIjX1z6VKzSY8jvZVW_70f4G1GdDg-iGzqfRD8P_6tmVn-04ONfyR3g3J2Yiob3i2xgEGxoyNdXImScuVun8puBwZ7MXLiDhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DG7iFizuwr1uN29fnnjWliFu3BQd8y0h0tjzAnUEUKp5vle5dKH1U0Zlv0khpOIvnOKWX6gMe6eT7aRuRD4ASPRlRG0RA0P1EyhB3Z_mNddNz9E-SsS0xBnjGXKpPPfcehlIPht3tTzmHIucFdXVN8DwVNXjQsHXwo6XCiqkWQcGgXZOr4e4dul0cZym8fexmLyOR0jckrc1-8cWVgKabvQ38BgVxRdex05-D01ryDNNh6Oi0pt8E1mIc9jaymHTWvKG7RM7KSF-OdYZUr_cc1-ZPCUjmVgkUBYVYQ-bO2q-6h4-4K7rHX0iPZUS6A_Jd3Ji10ycOkbswtUaJzFeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WhXFMHfHKP3Nns1x0aD5xYXsyughzdsiDq02g_gTpc4WX9N0g81X0dS9h9G3ijyS5IzE3pqcNDHfFhnowl-ZnHRYmc7UigXo3LEf3GgTCIHnlyzjXgU4uloADuNsIWmfGHVYSm5DV8cy7Dj55sG1Jp7jZzsyBqU1RPnULG-rGO63BBae7WrLwxL60uWWBIqDM7sqffxlmN0YZbcs2oiSoJTIDx0BuOXdiYjleJjNwRB7BbsQN1BCQKS0beTPe66G6c4ObT0anscAn4c-jHV8U4QILsdqoup3iFi4XWdPjv-fbc8aX8S__pxPy7uDD-f3SWPoiOaf-7Ct-OETIYXeAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I-9OH4DPcqljBIL2yG-if-SdErYP0G7Dvsvci-QOgjN6mJ9tye22nfFowd0pmpz_ZXAPiyaOa4R5RSY64tywKZmMjt9zrtxovNMeeQvi5-mRdBMr0fGeQ5hqcMebtpb7fwFH90IIZ7w9wIkp9LmRLxYDO_uR7ryC4EDVhY6JCoTUMCLtlG_jjqVLwSeEzMwi4QNlXVWY53eDy_fhS6QKk_5EdIdOgAXlHUSPXlDWMI-nkpdKCo06htOrs4sxdeQxk5zNJgQtDeFhw6MzEzs7Xe5Bh1kOanSS4qXP0W4p7K11YO31HAnuhjK5goQWW-JqWHwzxRHahldY5Sar-4Ybsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c-RgZt5A1IJhuHWIfcDFlLzKJWz_6rA8mTYTA9N47mxqNvyYv-36LWyeLnoKZcwkdY_oVjqJqG71SnRcy5JFW2rWga8r7gWDz9LS7TgT5mUoQ6gyKMJwt9a2ZlUITQ0bp6F_a9le1WPIc8n-csz9wrOeE9wMNbkyc6M7fQaQOV3HsLTltjwI5HEP-S9s1DN1offhZErEfOA7GU-YfdUHSaNY0ft7hUJ_hFR6dn9e6b_TvPTgZyZvXhyDZTSw71igLwO3HFPax4T-KIbwBmd9M6aMk0dFjf2YxgxKJilWg1z1wXjLOIQLZm5PLUkKKz3abAw8wNEEsNQ1utmdv2y_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uWGmPrXDU49TYmdYfLkvyaof8HqjRAr3yLL1Sbm8iWOeoNDFTgs3chi78Wur71SuEXnKZ7FYuVTaPXtkefiKCwoFuYGNFOBdytUSnEK8Ene6LTiKUfs5g5CXyi1fx8-VieWWMo_PQyXBaqFLi6FkL5oX0IR84mfCdhME0kKoo6uOrvSAiGvzbZTWbwLM7PK33rsX9N7rFyhn4QHXTR2eq1dBtSt0rj3rysg6Dzv6cTnmoYUBRiBFJaWtdcyheVJ_ZriHV4xFDGhVzorXoseOtpFlod4bQtxwDdOVtFtELl9omcpMf2E9nXvFJgUxwpA6IYBCa9fwf6Ni_0tXHGWcJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VVvAQGABuDWmlO07IOF8u6fu1Xhke85udNTGafjc3svrktaY3VIdMq96S7WoXKX2sSpRmYivbfXu_OyfR6aTNJic7FTthBLGywyd79VFDQtKqhgIEWoI5c0g6DTqehSLx3NiRc06lpeU6_UrO0OLJgmbkAu2bZVtzvJoaz0j4WLIiKWYlp_NWQskK39gqDEAFSt2OGVwwmmdVjHBfOUneNZ4H2KqmCk6BYRrtHfjGtl0QIwyPsQcpYK2d6Om7IfRs2xjPv9t0Dp5bmFs-HWmKs8LM1zUScpJM4bZNJJLhjSTrVk4zHAAGBU8PoQzuDEcUerGnJMrN8mIuSZQ-go5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cVePFWU3J-LCNThfH3pj4yf8m4CDcFbj976ex7qvVxV_AFFRFIerC-DZ733j-wLq3kfZ6aa_s86lUZcFbF1nrCR7pNsxVSQJGAeat2GRHsdDhTfTID2WT3l17ZQPAKgd9AJvw9RejXwl0uQZnCv4c96kgmYBlV_ZTPfj7cQb89zyBJVaFlWWE-2j9rJt9Jt614BJK0cYiCMPSw9oC4ktjpbSynf7CUbr7PXTI4LrQsnqjrSBwV01wiVTY3jYbtRAXWpvW3TA8KSTSiYkfXio9qFMFIwV_JGhFlqKrzo7c7D7ewEInHQTHUHAHpj655UfdpsQej3ema4URbhsJqf_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nNO1kuxh8qIqCNIi0hGGzbsgISJcc4v1FsHpdGsbTKGPAUiFffKXczqMbKNWHzq4_t8pyY8mONvIpNFcKyHH7FToO-ZuTZeRCnZMS1bg5In_25rdS-rJKhCxWG0-9rWfRM9aouSw2rc_SG3iFDx0mL6bvthi4CTP1L2cBBaN1sOiePOhVwqlj534wo3lZwG7tSuvuE6BIXLHg90zY7OU7lxY1jw4mXd6JaFAvdA1kGsiog2xmC6qf918S3HI3n_eLYuJ5kyglqIeL7FgLK4t2HuG0ElVKNDd0ACscc649Z1jPGVipf8zPJ2i0MTjz_Iy7IjgionKMgEhrzLKb4w_ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LrvaACJ4SP2H2QcPSDpuwTlWOcKUSFV_uxt04xB-qig0_4rXLvc2f5WeUsED7NEeDoH530e9MPsf7ytU7ATR40MH4EZpHo6u11nP4OxOX7E2X5hVbbFAn-2ssdTd6CSxlA3qjiDbijXnicQDAO1rb91pDnc36-iHELicibuD5Y_Tdgt5BrqvM1g4FQ-Q6r8AxPeoIpSzFjnVhQVaMB4-1q-T2_l1X-MZiY7TVng-wln4YLAvLSyoPgSqiL8GAK1DC8NvSDiJKABHp22S1qh_-l3BKP2q0ZdGT7zVyQOTdDlnwyx7ia_d5nFpuYwldjy011jL63hjpXx6U734xibawA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yz01UuQ79VMVLv57K6Nc1u0SWDVuIJSgVDPY7TwBzAqwP868Rc-IB2IEktiPstMSzPc8pvdJcTkx0hne6ZD6E4k3ggk47MIqes0-Ar3uCe77PCDyulL9Sq1Yz9Dk9qPfgkIZJlsM9_ISkJFxNTVINg5e3xvTb8RiAoGVfYCo9nSa26U3Iy5yzaekjHLYCspseUVI77mmyTIMeGOec43Rz97hTaYqwv1S6EGWL3YM8frQgQLDmOA0IxnuD_pC0rUZYcCALtAjD0RHMOSgKl9fmgyZXdmZiGCVZey4o-YSn-P5nVFUL92n9MJC77qkLIb9RUZSMrXzzR6Wkzjd3JLYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ewVq_xrchtS0hPq4-EuEZ_bfdu0vn9mFyu9nbdgH7RP7lNt4xh97KZqElw0exfifVorCBU5cFj9Jiyl6LWOO5c0gAgKKfFwo1LPTpYX8_db3Y6-3E0RiGiLvcBhRwezmfd8wRyR185Ab6hahdfgTKH6PdkZ_zEzhXXJrR2Jqs4goSeMdZ-syG19Bcg2OTq1FpbMvN69jyxz5Ev6WXNFhqzM3ebd4DzABptM_SSrpTxQEwSV_YzOt61p-nwYX9GI5t13eWfJcL3EicvYyOqO8-KToPB5zvGzp9E6fQRsEflvx4pu78EekoNHXOwhQytztR2VEKPMJrEuXdrD7Jbl11w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mx4fqqnU4EEqHA2YED1Lp4SLXbdl6S4HoQm_bt40iq1fw6zm7jykX-OSMpJyQzENFOTuZhO7eLU0aBksweL40cTxg3gZJiDgvb-8sMKZvYBqm8wo5qXKWwrgZYVvizbfwx8qsz55uel2Kj3c1u8mqM_MEWOTozwHmsNmuKRSg-SHTdZ7pQrEm8571IwIthqP-28mu8QAQK0a07tYmXJ2tdhEC0B0hMEwkKQBaWikd7MhHp2kfyGXsa-2LmjeF3CFafvJZbl4KMBdVnGb5ldmLQ2m-gGy5jMN00w_kGPSeSDfN-G6pYnvqVntKcFH2OM48OOg6ISEWT0YumykFBNTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uYX2coi4d6d9JcfVzLovc4_6Tpc7x8IqfofGrejZ_HrMitiVl6UveihsDWElOChDyy6WDDvG0BEEYrgYc5tx241v9FyKhLqmh1_Ju6zI7LskdkC-RInuIt3AEFSGEJJm0YYbnqIQJoR0XkyrNAQvGd-Mynp3lEMnqea6QeR3BIbsxx50pl7u_YPNELFJW2JStjBT39w1cVD47CAnvWXTHMbIIp7o7UbH3r9Z42WaLFmVmq_Qq0qlWrNyaZqXgqxbCc1NLZYrZT_ZDAF7DfdYcvkh919F56Zg4MiECe-a541Y2zG_7zFtdAcuvMZJ_63fqlkIIxZF4oQXGMpekAXmjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PbTeMwFSkPzw2rH5DGbUCLoY5V8-CoYI1F9AITd6GPVU_UgfUoFnPPkkUsqd4RPZdkiqbT8ADKtqKXoJfe9VGGPSdmb9dQVni6slqHqlBdbSYmBESwVgd_71jalNjfCA4jiv4DSyHTiFBKs16myVVOPcUPk4Yua8Yksnq47-zzsCQjRqrup51KfToSaugGyMkWOkcvhZE6zYr0cN8vmAH-ZQLcKQHcyxwBQyMmR64uKj9_LOIovEtbp7FofPOKWht3CznyxZ8QDll-I6PDBYG4A2ZOI7YfjKDmi99TaxdXa5KwR-uG_SVrYT0_bXdqgUJxMHxFN4ypinN5qm3D_xoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DRzd6mWkU7pnCHlYnqxBo0rq2fRffH5_VXTPb1lgyObjPlAgbAXx1uqYyKVwQfVYy6F77ABt4tieHCLmzFaja94SDQjNP2MSZ1BA8WuHY1lwCeE8kKxHFVDOMvnD1mKnm9TS_OuHIxO7ZcEv2Q15tPIis7uKLVmwr-ugjLwerW8OhVqundtaH7XQubu7yo12oZ1DgaD6PJ_fmDXLf_1_3FnN9r_C3ujnGm9zaltuXRT5lMDXCkIgcSzeeDnIP8Wz9ymBKwR2ISfbAxRoFT7JJIWAG9bPwSuHF0dl1P5X0-mfO7dl6B7ju5gpDuSSVBhDUj8HFFFQQs0T4bug27FyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SOTF9DMB-QhLIrv06XQL0tyVImWmImeziV-ikuK8LW-Yrz1Yz3cINZ8x7_jdwYHKOOdBZMqZQiMjqiuuUJZLx4N4fBF7d195257DLUSbNFB5K1sUXXsKt2x-pieJVAKuze7BALKxOAJlyTsSc3G7V5KLQN6CEKSggy-7qIIzjo6-L6mrM6_Q3WL61mKQSgIgbFR8Kxh9sqR0Q9PX6K_WeEV1uYB73lFNa_eu-v_T_Po5EtLeXm-ZOns1HBBLDty43IsvK84s3u1ASkBVlwNIVUiAPXHwNl6ZXxrHxv-H_fS5_XktOILR_F0-cVVhEWY-VYvnJ-uNI4Gx_4HdGtGZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر سیمرغ یک ابزار متن‌باز و رایگانه که برای پیدا کردن آیپی‌های تمیز کلودفلر در اندروید و ویندوز ساخته شده. این برنامه میتونه آیپی تکی، رنج‌های CIDR، رنج‌های دستی و لیست‌های آماده ISP رو اسکن کنه و بهترین‌هارو بر اساس سرعت و تأخیر بصورت رتبه‌بندی‌شده برگردونه.
👉
https://github.com/rezakhosh78/SIMORGH-Scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HBN_B606WHr_IBEG1CC80iB_BcaBJjvcN64nUN1R07BV6HrcEVad9Iwt18yirAVFVCz6Kjommx5T9XeQtl3FRnIuuzp4bVedYHCpv8L1j20PBsY3cELrtXdrjX9p3kzbfNopNnav1pYZ0XMph3NMPLIg5ZLXw-HcG3bnaAZ7iisoz-gul9tIHwn4ZpyhQNw90Q54QUR5ANIq-e2lmjdXWOGKlVkGrEWOnnqFnt3x7PXUXBG-tAT70HSbXL_5gtYxY2pza8jGUk0k3FmCQXq3zlMfqGIQ7IXZRs0dPNroZE59Xjv4AVxYG-g1_jOaJWBwEKdiEoILrZIxk7mOwLdpJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر Asha یک اپ متن‌باز و رایگان برای اندرویده، که با تمرکز روی پیدا کردن آیپی‌های تمیز و پایدار کلودفلر ساخته شده و کمک می‌کنه سریعترین و مناسب‌ترین آیپی‌هارو متناسب با شرایط شبکه پیدا کنین.
حالت‌های مختلف اسکن، بررسی لیست دلخواه آیپی، شناسایی دیتاسنترهای قابل دسترس کلودفلر، امکان تست سرعت واقعی از طریق پروکسی و استخراج هوشمند آیپی از وبسایت‌های پشت کلودفلر، از جمله امکانات این اسکنر هستن.
👉
github.com/ashanews9776-eng/asha_scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نسخه ۱۷ از اپ
#MahsaNG
منتشر شد و توی این نسخه هسته سایفون بصورت ویژه برای شرایط اینترنت ایران بهینه شده. همینطور امکان ساخت، وارد کردن، خروجی گرفتن و اشتراک‌گذاری کانفیگ‌های
psiphon://
هم اضافه شده و یک اسکنر IP جدید برای CDN Fronting طراحی شده تا پیدا کردن آی‌پی‌های مناسب راحت‌تر انجام بشه.
امکانات جدیدی هم به خود برنامه اضافه شده؛ مثل دریافت کانفیگ‌های ایکس‌ری از طریق نوتیفیکیشن گوگل، قابلیت زنجیره کردن دو کانفیگ و حذف کانفیگ‌هایی که موقع تست پینگ توی ساب فعلی پاسخی دریافت نمی‌کنن. رابط کاربری بطور کامل بازطراحی شده و جابجایی بین ساب‌ها با کشیدن صفحه به چپ و راست انجام میشه، مدیریت ساب‌های بزرگ بهتر شده، شماره کانفیگ در حال تست نمایش داده میشه و از این به بعد خود اپ می‌تونه اعلان‌ها، اخبار و بروزرسانی‌های پروژه رو مستقیم به کاربر نمایش بده.
توی این نسخه مشکلات مربوط به اتصال مجدد و کرش سایفون، ایرادهای ویجت، باگ‌های CDN Fronting، کرش نسخه ARMv7، بازیابی نشدن رمز عبور HTTP، وارد کردن لینک ساب در بعضی شرایط و چندین مشکل دیگه هم برطرف شده، تا تجربه استفاده از این فیلترشکن پایدارتر و روان‌تر باشه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مخابرات قیمت اینترنت ثابت را سوسکی بیش از ۵۰ درصد افزایش داده و آن را به بدترین شیوه در محدود کردن کاربران و تغییر ویژگی بسته‌ها انجام داده است. مثلا اینترنت ۱۶ مگابیت قیمتش ثابت مانده اما در سرویس سه ماهه، بیش از ۱۰۰ گیگ از ترافیک آن کاسته شده (۳۶۰ گیگ به ۲۵۵ گیگ).
حالا شما اگر بخواهید تقریبا ترافیک همین بسته را که تا ابتدای سال عرضه می شد بگیرید بایستی ۱۰۰ گیگ ترافیک بخرید که قیمت آن بیش از ۲۰۰ هزار تومان است و در واقع همان کلاس ۱۶ مگ سه ماهه با ۳۶۰ گیگ از ۳۰۰ هزار به ۵۰۰ هزار تومان تغییر کرده است. انتخابها هم محدودتره و برای ۱۶ مگ یا همان ۲۵۵ گیگ را باید بگیرید (و بعدا ترافیک جدا بخرید) یا انتخاب دیگر ۸۸۲ گیگ است که قیمتش بیش از ۳ برابر است!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o8PG-n3StyKaiX3RuR4cjAQOuktTLxhi28F_2IDc4WiyD2Mv7HMOCqAuG28zrG_HtK5XCSpbcaaUGl6AFzUMHzEbxG9M2DwfZQ9Ofo-CoguMWuEqNgFF6ziS6LCLhft2374Voq8-cM_q0KL00d7UNYYHQUl9TjgE9dDoQ7_pdtPtCEjmmSoSq6Jhep6Uuo-j4j0HP9BgqLZlDPsguh3kgCD-IfWDFnM2qm-Hlp4wA6pHWfn9xqXrThGhmmF6D9Rzt53x1QcRBDbf2k-l8WNcLQhMBn2Jxb-qhcsQKxxSkcsLNlHFKP1fKyHXDaFq_mgf7cxY1fWWm5SCRa-StWm-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2467">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارش تحقیقاتی
HalcyonAi
نشون میده شرکت
ابرناک
(مالک جدید دامین ویکی‌تجربه) مستقر در تهران تحت پوشش یک شرکت آمریکایی به اسم Cloudzy مشغول ارائه زیرساخت فنی به هکرهای حکومتی کره شمالی، چین، روسیه، ایران و چند کشور دیگه‌ست. زیرساخت این شرکت برای ۹۰ روز زیر ذره‌بین کارشناس‌ها میره و مشخص می‌شه نه تنها گروه‌های هکری حکومتی، بلکه گروه‌های باج‌افزاری از جمله شرکت تحریم‌شده اسرائیلی Candiru جزو مشتری‌های این شرکتن و بین ۴۰ تا ۶۰ زیرساخت‌هاش به فعالیت‌های مخرب و مجرمانه سایبری اختصاص داره.
آدرس خارج از ایران این شرکت (که قبلا اسمش Router Hosting بوده) به دو کشور قبرس و آمریکا منتهی میشه. نشانی آمریکا به یک مرکز خرید در ایالت وایومینگ می‌رسه که آدرسش با بیش از دو هزار شرکت دیگه مشترکه. ثبت‌کننده کلادزی در آمریکا شرکتیه به اسم Cloud Peak Law که تخصصش ثبت شرکت ناشناسه.
گزارش تاکید کرده بعیده مدیران کلادزی یا همون ابرناک ندونن که بیش از نیمی از زیرساخت شبکه‌شون داره برای کارهای مجرمانه استفاده میشه. این شرکت در واقع به عنوان command-and-control provider به هکرها فعالیت میکنه و برای استفاده ازش فقط داشتن آدرس ایمیل و رمزارز کافیه. ابرناک در ایران در سال ۹۹ با نام «آلان فن آوری ابری» ثبت شده. دانش بنیانه، بسیار هم فعاله و در حال حاضر ۳۴ فرصت شغلی باز در سایت جابینجا داره. مدیر این شرکت محمد حنان نوذری به رویترز گفته فقط ۲ درصد از زیرساخت‌هاشون در اشغال فعالیت‌های مخربه. همینطور گفته نباید چاقو فروش رو مسئول خلاف مشتری دونست.
دور از انتظار نیست اگر اسم این شرکت و عوامل اصلیش رو توی فهرست تحریم‌های آینده ببینیم. ابرناک حساب‌های توییتر، اینستاگرام و لینکدین خودش رو غیرفعال کرده. نکته آخر اینکه غلامعباس نوذری که در شرکت ابرناک شریک محمد حنان (احتمالا پدرش) هست، دیپلمات ایران در نیوزلند بوده. حنان هم در پروفایل لینکدینش به تحصیلات در نیوزلند و در پروفایل کوچ‌سرفینگ به ۱۵ سال زندگی در این کشور اشاره کرده.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/ircfspace/2467" target="_blank">📅 08:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2466">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DxPHNuc6NXWHvUoGut-PEq_3DMVPr6Qc7UaXJ_4UPRkq1yCjBFDIz1RWlk22u42aMBouxU-DekbBBakDhEQ7GzpwbTQpM4HWIlshfeLz28aIM0aALHd2z_J3RoNIWHGjFVKqwdCM2CCs6HuMbnJQvoXVs1Hfuy--mizHLo8tFeyLRfaRiFryPk50iCjSb0fRqQxfpyXJMB7y7Fpy3fXmytEOueLE0ryW-NsWC1LwqeSJSHcsPvIV4FqU0oVGvvDiFdd6MRYi8iGT21Tj3Op2e7jc-TlcMIkuJa0zmQBh4FuJTwKwpcU29z9rvIDJJF5uxgZXYgWUdrazCajvJQamew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران از رتبه‌بندی جهانی اسپیدتست حذف شده. شاید فکر کنید چون دیگه حتی ته جدوله، رتبه بدترین اینترنت هم توصیف مناسبی نیست، یا دیگه زیر ۰ و منفی جوابگو نیست.
نه، چون چیزی که داره ارائه میشه اسمش اینترنت نیست!
👉
speedtest.net/global-index
©
Mehrdadlinux
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2466" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2465">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Og6qeNP7BP5jNE0S3WxpnviFPX0xv_ygzqneKNSIPlb2zDXcL0QYwjGgkrVKOAyIEEotiGIjnMpuDW_vBEfom8Qp7mXW1C-qCFco2lxT_Sl6DPrLH_wk25HsXYaXAuvdxDod-N05kx1sz9RkLlbLJuWcdGStPiYT89CZlZxkD3-QMNljMklvVz0V1qBJT2TNfTLvBP9zlohpTyJbGGFZlA2G8kEuhkXkTGrCbgEv4aoRkIePMCuKDIfNwyaoyUUwtmqIIohRxcKLKqwmdpXrADwyDIHsMNeK4Us_Opqv6eRVQlnv8kUjB8KZAHXBG37c91w7SAXskCD9c0-gtEaUzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این چندروز احتمالا در مورد اکانت ویکی‌تجربه و سرنوشت نامشخصی که برای مالک ناشناسش رقم خورده چیزهایی شنیده باشین. متاسفانه دامینشون رو در ایام جنگ و قطع سراسری اینترنت نتونستن تمدید کنن. بعدش این دامین توسط ابرناک ثبت شده و با یک پیام مسخره و کینه‌توزانه، صفحات سایت تغییر پیدا کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2465" target="_blank">📅 08:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2464">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B1jMieRNKIqIY5JRctIf5BpQ_scNGGkYvZd4c1J-guRxMSdaGhbjF4b89SktrUdX7Bu6kiIc1soWG63di1_phLyquIkIdHfU2b7Mot59yRF77KHkowMcL2Iy3webogC8LWNN4eYFdS-_FzJqJ8JBsmbhfPuJFujAkZNf-qPBOE9jbNLwsdAaYFo5udVsmVV7tF0VSipSMLH5rJbb_oBPKqNBHPRUViCCLpafrJXr1eaOn29Drpj4CKVSa_FCxD72yvUHMjLmUsheFUXI2iCURmMXFdzRrUgS2Ty0UsqXenQYi0s-xBGaCaXb_Haqnn_rzKXegG16RuEHWhGoikqjCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از
#لینوکس
استفاده می‌کنین، فیلترشکن دیفیکس در جدیدترین بروزرسانی خودش پشتیبانی از این سیستم‌عامل رو اضافه کرده.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/ircfspace/2464" target="_blank">📅 12:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2463">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XyjzxUxNEJ2Jqk6Szn5zDVaC0P33BchvKM7MlxueHY4DpGcqSsRLBe3cR0D7NzT3Tx5HWwFBQE4l663iUi6kaEF9eF3drPUqELXBxS_AKVblVCgWwj4La1UXkx_cEC69BMbw9BxoWdsVmN2rC0b4sXaG744hbm4jPufJMrL11g4zSLAbAKy8J8EDuT8kfifVT3RwLmnRzSkhzT164WZT2GasbJWFYsYSPs_BhZdnDC7KTSOpL6wqo4EfyeWrfwidx_Er5nDs-_W0LLN8Z_bDG6M7DamZhnipSEluCjZoQzKBsYLH5TXeNQDPsZVtZKfHwgAj7akdgSH64wD_ZhpVEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ RedCloud VPN یک کلاینت متن‌باز و رایگان برای ویندوز و اندروید هست، که با استفاده از هسته Xray توسعه داده شده و امکان اتصال از طریق کانفیگ‌های VLESS، VMess، Trojan و Shadowsocks رو فراهم می‌کنه.
این برنامه تمام ترافیک دستگاه رو از طریق تانل‌های رمزنگاری‌شده هدایت می‌کنه، از قابلیت اسکن و سنجش همزمان IPهای کلودفلر هنگام اتصال بهره می‌بره و همچنین با استفاده از قابلیت Sniffing، ترافیک HTTP، TLS و QUIC رو شناسایی می‌کنه تا عملکرد اتصال بهبود پیدا کنه.
👉
github.com/Devtahas/RedCloud-windows/releases
👉
github.com/Devtahas/RedCloud-Android/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2463" target="_blank">📅 07:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2462">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بانک ملی از اختلال مجدد در خدمات کارتی خودش واسه ساعت ۲۲ تا ۲۴ روز جمعه خبر داده بود، که گزارش کاربران نشون میده این اختلال در روز شنبه هم همچنان وجود داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2462" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2461">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده. اول باید چک کنی آب وصله، بعد کارتو بکنی؛ وگرنه ممکنه گیر کنی.
©
shokhmatic
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/ircfspace/2461" target="_blank">📅 18:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2460">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">در حالی که با اعلام شرکت خدمات انفورماتیک اختلال خدمات کارت محور بانک‌های کشور برطرف شده‌اند، بررسی‌های کاربران نشان می‌دهد که همچنان بخشی از اختلال‌ها در خدمات‌دهی بانک‌ها برجاست. اغلب اختلال‌های موجود در بستر نرم‌افزارها و همراه‌ بانک‌ها برجاست و این موضوع کاربران را در برطرف کردن نیازها روزمره دچار مشکل کرده است. /ایسنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/ircfspace/2460" target="_blank">📅 18:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2459">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IApNEY3eicqae59KumJIp43EyxFcvczs1sq_GBV_2t8mBC689b1E5x9dBLyejyEeTrWn492_cJ95I4SHwD_HCqPpOT5mhqJJbOP24pXBynVDUZzGfsTq8aUT4PdieQkD8Pbr8CQglKlda-10HQpM-lsmSjGxIndoLgFawZDKQrc4-Ge91WMBEGfwNSG2cl0k61e4gPwiy39mnPX_fmne_6gEQqjB7Lz5i0jN_cxOy6254y5KBo35Ua03YQ8WzT-bQHWULpW7BaQsfXZCrKFEiVg2DTOn3kCc3isWXXdOUBDd-y4LYCStSjiSM7c4JBtDHPsyseq_7UYgyA8GnBoK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسیون اقتصادی مجلس طی نشستی با ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات، از عملکرد این وزارتخانه در دوران جنگ تقدیر کرد. /دیجیاتو
بابت تقدیر یه کاسه دادن دست وزیر قطع‌ارتباطات؛ اما بابت ۸۸ روز
ریدن
به اینترنت باید یه لگن بهش تقدیم میشد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/ircfspace/2459" target="_blank">📅 20:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2458">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/ircfspace/2458" target="_blank">📅 16:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2456">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اختلال خدمات بانک ملی بعد از چندروز نه‌تنها برطرف نشده، بلکه این اختلال فقط محدود به همین بانک نمیشه و خیلی‌هارو گرفتار کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/ircfspace/2456" target="_blank">📅 13:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2455">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جنگ شد، اینترنت رو بستن، تنگه رو بستن، آتش‌بس شد، توافق کردن، تنگه رو باز کردن، اینترنت رو بصورت تدریجی برگردوندن، گشایش شد، مسابقات جام جهانی سر رسید یا هر نمایش و کوفت دیگه‌ای؛ ۸۸ روز قطع سراسری اینترنت، سرکوب، اعدام، زندان، شکنجه و کشتار ده‌ها هزار نفر معترض دی‌ماه رو به فراموشی نمی‌سپریم.
خون‌هایی که روی این خاک ریخته شد و نسلی که هزینه آزادی رو با جون خودش پرداخت، از حافظه ما حذف نمیشن. بین ما و شما دریایی از خون فاصله هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/ircfspace/2455" target="_blank">📅 09:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2454">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OKpdXzPGbjUznIk_dACLT9Z82thfMdSPdxAYOSz0l6gnnLQrbBs4KC3tRkmtEnGqFklUI6eWoUOM8dPEZYOo3MSoEW_DZfwQGjtVBKpkjmrw41krOqJJiNouWbyB7P1NInsFUl2y0pIqTfXB1tJWzJYnTu99MOiWAi6cQpq2lGLNnWc_Z1R_oojKbk6GtJdkZAetfaQxM_SMt1beV8ymgQgGDQWDxXeHVKnvmvZ7Yw13RSyL2nT0sy-HZPKBIoWlCcjhkz6vR4VFV7Nyr0Q8RwVzNaSwtrdsRk_QchfvgpEbPK29PC_gjuiRuYjhhlY2twelPYsTOM30sb2hY0Pk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل V2X یک ابزار مدیریت اشتراک سبک و متن‌باز برای VLESS روی WebSocket + TLS هست، که به شما اجازه میده با دیپلوی پروژه روی سرویس‌هایی مثل Render، Railway یا DockFly، برای خودتون و خانوادتون اشتراک اختصاصی با قابلیت بروزرسانی خودکار ایجاد کنین.
این پنل امکاناتی مثل مدیریت کاربران و کانفیگ‌ها، تعیین حجم و تاریخ انقضا، نمایش آمار مصرف، مدیریت IPها، اسکنر داخلی و ارسال گزارش و هشدار به تلگرام رو در اختیار شما قرار میده.
👉
github.com/SulgX/SulgX-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/ircfspace/2454" target="_blank">📅 09:16 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
