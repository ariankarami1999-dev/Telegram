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
<img src="https://cdn4.telesco.pe/file/ODlY8868Vc1bENeazxxYpXjdBdUGsMLwuS0XrzyVImHYtcj4yEkilP5ymy3ES7TdD9EHKzXC5N90Nx558M445Iu5uylHm4eI6QEFbyQWGnbtZhenF36IvwGZSKy08as9_sBKxlfCQjbdKY0zpb-EOQRnHFGPUAlJywFMwRZifCmewZ1IZYcmvWV6NYBiGTNoGCl07zgIZkY8UV72bEQY_0Za1STc8PX8n9Y4uL-_YuqfM-gk_q7yp-w8HGzWLyQrOkNXQ_ZVBSkwWFeFNij3xk6uC8xornvXh3zBlmNDL0Ite2CEfIqAlvj54hCtSveClKznu7LCOgb8drJVereXkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 940K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 03:37:39</div>
<hr>

<div class="tg-post" id="msg-124356">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q5y6Z7ELi14sm4nNL8-Iz1DFPNZ5mhkXM-mAp9mRDk9G13R3lTRlG9N9wp644wvZyRus2MUXtoL6FeeUA3uPu8l5zOf3pqvEPlhwXjT7j66r3IvVCkUBofDrylHrNWrRe7jnuf5-ktiGncHxqgD4-ErN8gq6hMnqBat0XZLWlMwa4nzw6SJKXm5rDXokghzbmgDCpFgSrFk4bu_cuho4lh7f_3HQ4PkAY3eW57k1qQUchmFfBU-QIXA42LH66VNDCdTzo3VNvJF4rFxOHjcBT8kQsXSjfJ_RMbjCYZVhkGh66o-jrNDLZRehYulPqnab50bnULdL8YOkvrZvHlWM_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 8T!
🚀
😍
فقط گیگی 8 تومن
😍
✅
باخرید
90 گیگ
100 گیگ تحویل بگیرید
😍
✅
❌
فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/124356" target="_blank">📅 01:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124355">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9vb3iRObxbB4XNVPcNmGvySYMj_jswccNOxKE39SXT2woycx3NFGAhjKOixBC6Z33GoOzn5Js6f_pvqiTi1SyFe0HT610pGndXP4n6DulvmTa_4n1IDq8dXzHmtMQ5_rXdAZKvC-Ag3zqVambVbuS0Oj0ta8FBxlDdqF7_1xQTB16a7RIP1De3LP88xhnuGbMw6_rgRcBLdsFrbBqz-mjrJ_Y567wTxd2yfPc2qv6I2FXF9fdcz6ajJ739OP_mhGHcrxqy6VIEc1AImMXJZaCuCVX86S_8OZXQQAXA37nbIK4CeYvE4cIMH8n_-UJt0xWUH0exLNncnl9YigUyrFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها از حملات اسرائیل به لبنان ناراحت بودند و من سریع مشکل را حل کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/124355" target="_blank">📅 01:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124354">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbwtjQpYNjt8slyaFeG-tptz0ZN8Lc17ko8mYZla6lMuT72xb7uGu2mqe5UKXx9LV1imPVlDATIx9BbRpBrpS6q8dw5m6Yn3x9lTzm3GCwxaQjnpxgPsxzk3NIt2RHotT6OTeL1pz8IyRKTCMSHO-1zxCbqWgPSblFqwePs-2WO6iTuSH1TW2wSgOz4FUi9_HFQ3LJx8ci7oXSB8nAL4KYuVkItndwPI8s_mtgyDa-AQhbSMaRPjmVnVO0qyj_UNqSYtItqr1N4bAVzRET50IaFKgQAMjLToSDy4SbiiekHpn8dkspitf5jUk2qMu2P3NEcRtZQ1H2mPXK2XrtvxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: ترامپ تنها به دنبال توافق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/124354" target="_blank">📅 01:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124353">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
کارشناس صدا و سیما: خون یک لبنانی اندازه خون یک ایرانی با ارزشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/124353" target="_blank">📅 01:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124352">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAv2xhcgUuk2UkIqltuTmCfXR3xp_ing9uQnB9SRtVrKUXAFgyPBux7CXKSZY_1d4ILNlJljju1e8UMhX8jdV7OlI5X4espgHxhdsgpVpNCKUjkoNuE4HVY7niXBTJi2Og_VNL8steTgnvN7U2118eIPYESFKxKFeH5ch4urN3N4xZJR_E-o8LvCpLQEpSpK_h061lGVT9nB0kB4Rq9FIjv51XdJKRpgoyeqq5wZxbrLa7AU2N9eOZNfk94jRucibnFsx8MF13kGZNcpq1J4bOhnB3ooPHR6E6gKovNwfLJQQZX9pxVL0WH6qwUHI0EjKpJ__ewV--SUWZ6LOZhFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ آمریکا: آماده‌ایم به جنگ برگردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/124352" target="_blank">📅 01:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124351">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQQTgYRbZhsi16_7tXEaU-TXVUwIVVwUi_sA9qLf_vYcx_p0nl-TnPt3HndI6CLib0ZiqQVATcRAzqxb4qJ6WvUp3N86r0K7aIvb-E3XPHVMH11584pabOQvGQkeH4O0uGBHqu2bNUW25t_YMS9uwhcoiBcSDxZ4WlRhwRoAepFaCK0oL12rSOL9DYd9Ll9wO7eDo1WINRVagSLU1koFQb8fxMKgGpp5b6bhy2gQPiQktVLc9H3CUPMQlQtZdtcenFL8_KTrc4dg2dVU_cStlPBmFJjFI07xcXIuAsg0lXQtg01imGun2ijyFRza-VLoZxQl3WIhTB-aPKj5Wt-veA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
4 سوخت رسان آمریکایی در نزدیکی مرزهای ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/124351" target="_blank">📅 01:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124350">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28a044344.mp4?token=Z_YhC7H8IR5O_Jw50-2arGjhjyE7IPEsPJ0HXoqkK_5IzZo1zVgAe1mIP9-PrSU9UULI7gPYtDJs2HJyyCpPZlqQ9t2Abi_lvx0Spe3M3Y_MIkvn7MX_FIUlzpGYZCWLaNTfaVtRPtA2yKU05JH1Sw_S-AwpeCmWvnOOItrF-aD8thFJ5GinOlliGMzNXz5lncD1Ck2nhgw45z4o6oJ31BuuR-pRzHcR9TS7c3EkifgmpbDxg_IdI50IX63hvgyl4HgdFhdMdnkLFkfnEUop_XyphDoIpgcP6-8URFAtQlaroZBm1IjpBZgqeho5wRP-h9g0Z72WUQrrcZs1FRE2EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28a044344.mp4?token=Z_YhC7H8IR5O_Jw50-2arGjhjyE7IPEsPJ0HXoqkK_5IzZo1zVgAe1mIP9-PrSU9UULI7gPYtDJs2HJyyCpPZlqQ9t2Abi_lvx0Spe3M3Y_MIkvn7MX_FIUlzpGYZCWLaNTfaVtRPtA2yKU05JH1Sw_S-AwpeCmWvnOOItrF-aD8thFJ5GinOlliGMzNXz5lncD1Ck2nhgw45z4o6oJ31BuuR-pRzHcR9TS7c3EkifgmpbDxg_IdI50IX63hvgyl4HgdFhdMdnkLFkfnEUop_XyphDoIpgcP6-8URFAtQlaroZBm1IjpBZgqeho5wRP-h9g0Z72WUQrrcZs1FRE2EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش تاج به ناامن بودن شهر تیخوانا: کاری به مواد فروش‌های مکزیک نداریم و نمی‌خواهیم هم اصلاحشان کنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/124350" target="_blank">📅 01:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124349">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm2uYev05GfDDzxioUFqf7jr6a5mYgwT5qVviEDbX_K06N-LpRe4x5JFS2zGNJNlt5GPlsfAYXOK92mz3NxjG9Aj_8TwvpjbqT_vAcD1_FMBwBJb92gVg3RFsynZ9XbpFWgVBPUGt5k6v_XZBESSNasqODe1HR9RyXH4hO5-VQXScGiw9FAPY3c6xuMsqEw73SNTobny6zwuX9ZBzW4j3p2ipPXyff35NogE-qgMQYUCuJx_DDoAp5s3zBOFdWVJeCUd2jWrWDHimFW8zaEXonR7PYjfqgfPeIoCHAeo_-OjaH97IDLByUQOLBsid0vLfyhtsxrP-GWb5Gk1RDZeNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوستان این تبلیغاتی که پائین کانال نمایش داده میشه توسط تلگرامه و دست ما نیست و  کلاهبرداری هست و فریب نخورید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/124349" target="_blank">📅 01:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124348">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj40knS7bLdHJbecOoPjS2I-nxEN7DmmPBwFalxikkllGnGQUyKh6q56WFJwmcEploNkM7nVX9jiFB30xjOcnwYOH04qtnPJI9_rGKy6GjmxOMP1nwt0sdar6EROPC2TM7d8kjH-O1I7VafYTogPIjkvf1M_wJ987x4BKQPXZvFwaDfhCFhbvN3omr5MZg1YDV8C0cpmy9W4Dyz8ZfZXFlQQTjcJTHqiH7T61vvpmsiDNExc2YiPtqjmx_dyu6sptD68ybQd88S1-nydFIivIG2GOy2T9j4NMVxop2VwTJgyLcFFOovltvQVWJcaFB7ZMOCp2Ma8U812LBPJ4iGmhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: فعلا جنگ نمیکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/124348" target="_blank">📅 01:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124347">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYMXL-ekURemRlnwo2b-v7NCWYO-U7zFu9Q_uvHjLqscALqxwQbiG4q8_HaixE9h_LFKyYi0OIiUnNnx8oCWzVFFgaeGVUNAFrgHZqBMc5ZgS_oyx5Pj3fxndQOL0HgUk-1qNlXuAdz6c0d0V5S8BOxtYjq-_XZhq1228f5vBerm7ENnIWsIjKbNKovyYGlM4zJorMsi1AYhu9WVGAE1LxNjHRtdi61UNFuvE8_UhhQ56A9-55IWpGnkzaI6sY1dLCiqXr6nf5EtSqcPa25uP2CRPmsTcyH52OQGM5ViSFvgJe0aUCDRFZacg_o-QMwO_AfOcl6-BBsmTjcSPoz1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور ترامپ:
امروز با بی بی نتانیاهو صحبت کردم و از او خواستم که به حمله بزرگی به بیروت لبنان نپردازد. اون سربازاش رو برگردوند ممنون بیبی
🔴
من همچنین با نمایندگان رهبران حزب الله صحبت کردم ، و آنها موافقت کردند که تیراندازی به اسرائیل و سربازانش را متوقف کنند. به همین ترتیب ، اسرائیل موافقت کرد که به آنها شلیک نکند.
🔴
بذار ببینیم چقدر طول میکشه-امیدوارم برای ابدیت باشه!‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/124347" target="_blank">📅 01:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124346">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c51d90e9c.mp4?token=GDJDXKOKW5uUu5CkqE2ycjhuJbJcZNpy6NDzXcr1XsbdGLmSlcp-5gvvnaRSO2YccWFOcUVHRM0W1hjPnF1spPkE1gZ9npiBCivrThbQKUE6E5gZUhIrnQh_DIOsxJCxWtrLxoEBpok_yJIl_NR4Kjl-cIKywfPBeSNqibpXvDh3qhkCh-Uk6PFM3VOMxTkY3w8tF2gxvExsdl1zvrXXJK9aflzSdELNKQZ65bOWjNQgRBk-w4_l4VicD97xuTxBWYialJMImgn4M9UEVvhiHiDCSaIR8KSANJuQex1P955Cr1HyZNkf9aA2fPJ8nugsxCICMwzXJCaUtFixgDrUdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c51d90e9c.mp4?token=GDJDXKOKW5uUu5CkqE2ycjhuJbJcZNpy6NDzXcr1XsbdGLmSlcp-5gvvnaRSO2YccWFOcUVHRM0W1hjPnF1spPkE1gZ9npiBCivrThbQKUE6E5gZUhIrnQh_DIOsxJCxWtrLxoEBpok_yJIl_NR4Kjl-cIKywfPBeSNqibpXvDh3qhkCh-Uk6PFM3VOMxTkY3w8tF2gxvExsdl1zvrXXJK9aflzSdELNKQZ65bOWjNQgRBk-w4_l4VicD97xuTxBWYialJMImgn4M9UEVvhiHiDCSaIR8KSANJuQex1P955Cr1HyZNkf9aA2fPJ8nugsxCICMwzXJCaUtFixgDrUdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم وایرال شده از بلاگر روسی در کافه‌ای زیر زمینی در تهران با حضور جواد یساری
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/124346" target="_blank">📅 01:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124344">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1MUm4b4jxnDsrKXkIwZXa-KfuPhVxg6okIscRdQvz7mTqRUgprWdctTAlDHAisqGmKxKShHLU4nOO0cojnaGDGK8VBRT_RDPoYH5YmJVKgDqdc_ehdU9qhKxrK7JiztAYPpEBeHF_Mk2KCh8AV_dZR06bCaD4ETzzxA12dlvrrbeos5iR7N75VuHnRbZmVJS_pnLV_khuFyjmXJV0iSSt_s1amFKd33gju3JZlyUWvDaMuub8TDtHkRL-8xxd3u7VuMBzW52kQfvptrm_3utaRm8Jfj8D0l1ER0fTQhcYX2ZsqxX30kOneXMb2yKFQxrWtDjiJb35BMXYAHyiyrIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qf8bcBLKsKCAqRvg6PD_eVJksaggsaqpoPD4UsmhXJNTycoaXDSR8bFuvw8BQ8BDcC4wMMGEj6jsSFUPNHxjVJmjlULDBLJeYmeMZdB2WbHPo2Wgh0UFpBj6TspIOyFCjrB2szIp_mpl4U1_mUgyzJI6RmWYlmceUQBkmNtoHO-c1saUui6ixo0Edk1AyVyzniC31ygAJiltnlHcGX1Xpe3QYXEuGXkyaaJegSEJHl_hoGdfhi58rf1e7PGNhc8wc7dxh1jlIco4RML_SHUiKcxHo1b7W_jZEjOnQcxoKnrBdS2SBJ3o-16jFlWBXd-fyrFymcXPXo5wG55prShzWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💔
جاویدنام حامد بیابانی، ۲۴ ساله، اصالتاً کُردِ کرمانشاه و ساکن پرند بود.
🔴
شب ۱۸ دی، در تهرانپارس، وقتی دوست صمیمی‌اش جاویدنام علیرضا صحت‌بخش هدف گلوله قرار گرفت، حامد خودش را به خطر انداخت و به سمت او رفت تا کمکش کند و او را از محل تیراندازی عقب بکشد؛ اما در همان لحظه خودش هم هدف گلوله جنگی قرار گرفت. گلوله به گلوی حامد خورد و جانش را گرفت.
🔴
خانواده‌اش تصمیم گرفتند پیکر او را به سنقر، از توابع کرمانشاه، ببرند؛ شهری که ریشه و اصالت مادری‌شان به آنجا بازمی‌گشت.
🔴
حامد از آن آدم‌هایی بود که عاشق زندگی‌اند؛ اجتماعی، شوخ‌طبع، پرانرژی و سرشار از شور. هر جا می‌رفت، فضا را زنده می‌کرد، جمع را به هیجان می‌آورد و لبخند روی لب‌ها می‌نشاند.
🔴
حامد بیابانی و علیرضا صحت‌بخش دو رفیق صمیمی بودند؛ هر دو ۲۴ ساله، هر دو ساکن پرند، و هر دو در تهرانپارس با گلوله جنگی کشته شدند؛ علیرضا با گلوله‌ای به قلب و حامد وقتی برای کمک به او رفت، با گلوله‌ای به گلو.
🤔
عرزشی حرام زاده، اینها تروریست بودن که به قتل رسوندینشون؟ ادعای عدل علی هم دارید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/124344" target="_blank">📅 01:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124343">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
باقر:
ایران نه تنها روند گفتگو را متوقف خواهد کرد بلکه اگر اسرائیل حملات در لبنان را متوقف نکند،
مستقیماً به اسرائیل حمله خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/124343" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124342">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ: مردم ایران مرا دوست دارند زیرا رژیم را عوض کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/124342" target="_blank">📅 01:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124341">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ: «کار ساده‌ای نیست. شما درباره یک کشور واقعاً بزرگ صحبت می‌کنید، آنها یک کشور بسیار بزرگ هستند که می‌خواهد توافق کند. خصومت فوق‌العاده‌ای وجود دارد، واقعاً.»
🔴
او ادامه داد: «بنابراین این کار برای آنها آسان نیست. در واقع از منظر ما هم آسان نیست. اما ما داریم آنچه را که نیاز داریم به دست می‌آوریم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/124341" target="_blank">📅 01:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124340">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ در گفت‌وگو با ای‌بی‌سی:
من هنوز این توافق را تأیید نکرده‌ام و هنوز چند نکته دیگر باقی مانده است که باید تضمین شود.
🔴
من هنوز با این توافق موافقت نکرده‌ام و هنوز باید چند امتیاز دیگر بگیرم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/124340" target="_blank">📅 01:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124339">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ: شاید این هفته با ایران به توافق برسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/124339" target="_blank">📅 01:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124338">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ:
امروز یک مشکل کوچک پیش آمد، ایرانی‌ها از حملات اسرائیل به لبنان ناراحت بودند.
🔴
بنابراین من با حزب‌الله صحبت کردم و گفتم تیراندازی نکنید، و با بی‌بی (نتانیاهو) صحبت کردم و گفتم تیراندازی نکنید، و هر دو تیراندازی به سمت یکدیگر را متوقف کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/124338" target="_blank">📅 01:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124337">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ: صلح با ایران شاید حتی بهتر از پیروزی نظامی باشد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124337" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124336">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
فرانسه: ورود نظامی اسرائیل به داخل لبنان یک اشتباه استراتژیک است
🔴
«ژروم بونافو»، نماینده فرانسه در جلسه شورای امنیت درباره لبنان گفت:
🔴
ما خواستار برگزاری این نشست اضطراری در پاسخ به تشدید تنش‌های بزرگ اسرائیل در لبنان شدیم.
🔴
هیچ چیز نمی‌تواند ادامه عملیات نظامی اسرائیل در لبنان را توجیه کند.
🔴
نفوذ رو به افزایش اسرائیل به داخل خاک لبنان، یک اشتباه استراتژیک بزرگ محسوب می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/alonews/124336" target="_blank">📅 00:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124335">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZqJ2qeuU1n6rjeUYJ1UmpQqm2YPYGGfZ07RXR22T94XGPt55CgZ4d9KO_iE4XC6r5IMcz30hiBa8ZrGzmHxa6ZlIW7jrjaJEujo9cXNbWjPDndLjbWqiQ1W9m5fSW0GvLFXH-LWRFsWGqFkN-Xq82_u215Z6-TaA7o2Cshtt4xCOjG69k-C2g4HQgoMrtR7O0JKId4sSiU9isEIZvt9FU8ErUt8ULejEv_Qj7sAC77gij87xNQigG-r6JoWy5eON0bk8QK2eY3CnCGzUtJ1KmDX8l28n1CiAIkGUKlMytHM6I0AwVXI0jopVu6MN1XdSKVWM55BGdwLpZUGM2cAmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید کاخ سفید
:
«به ترامپ اعتماد کنید.
فقط بنشینید و آرام باشید، در نهایت همه‌چیز خوب پیش خواهد رفت — همیشه همین‌طور بوده است!»
— رئیس‌جمهور دونالد جی. ترامپ
🇺🇸
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/alonews/124335" target="_blank">📅 00:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124334">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1207bac6cf.mp4?token=NfP6hkiZFlFPy2Nlr1QAIh6cdvc2oPlnHkDMxPx3xBxNfT4_F8aOAjkyeLTqUarHil7hsy04N_IrXMTmab8ZfdzLYwttCmTWaWhHLfDUg0g_fA9c6CzLrikcJNl0agDp39ppfr1TXTzBdeEeKhGbSm5mD5XkH-6Uw_mPOP8yn4UAcIuajLXRvOGnpUQySTVfIbzPt2EYqWswZK6r30txtxuPjgG4qsRrkjvrzLCdCbLDJtfVXeX06VG-E-prk12cICoq-ztiBHUsepn4oOu8XZZ1CpQPCrElfRg2gWUDMa9rSbMIw-GLY-GLP7P14lrveM9CdZSAd8MUxBtdvw4y8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1207bac6cf.mp4?token=NfP6hkiZFlFPy2Nlr1QAIh6cdvc2oPlnHkDMxPx3xBxNfT4_F8aOAjkyeLTqUarHil7hsy04N_IrXMTmab8ZfdzLYwttCmTWaWhHLfDUg0g_fA9c6CzLrikcJNl0agDp39ppfr1TXTzBdeEeKhGbSm5mD5XkH-6Uw_mPOP8yn4UAcIuajLXRvOGnpUQySTVfIbzPt2EYqWswZK6r30txtxuPjgG4qsRrkjvrzLCdCbLDJtfVXeX06VG-E-prk12cICoq-ztiBHUsepn4oOu8XZZ1CpQPCrElfRg2gWUDMa9rSbMIw-GLY-GLP7P14lrveM9CdZSAd8MUxBtdvw4y8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تاج: ۱۰۰ هزار دلار به مالی برای بازی دوستانه پول دادیم؛ هزینه پرواز و هتل‌شان را هم پرداخت کردیم.
@AloSport</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/alonews/124334" target="_blank">📅 00:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124333">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca354355b.mp4?token=ginlYqx7Sot0XbKzhN5bEJdhudkneOMRQJ5wz99ZxlVFNdlG6nJYLPKS6iD6fEPgKCHIHGAO70E0lTz1hHcJpH4n_V8qe1SWsYIeEk5oF9_Lov7-VOqv-_b981ENv7iIBirNB2n23LVqosUI4NRTQ0o7k04GxD_HDf52zvKJ4NVoO6pMbRpBveEq9EbhD0ysysqbMWXPMlV66Po9Mu7tCcEbzANIuXJycgGGr_H8f23H3a64DnWgQFHQVw9PMvpGb_JhlhcALQ5J3mF4gi8OPmRVHGMYOgILGuGK4ubUh5o0IIclHd-e3v0OVzLYwbJE9BoyYN94iTUHGiOkxDri6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca354355b.mp4?token=ginlYqx7Sot0XbKzhN5bEJdhudkneOMRQJ5wz99ZxlVFNdlG6nJYLPKS6iD6fEPgKCHIHGAO70E0lTz1hHcJpH4n_V8qe1SWsYIeEk5oF9_Lov7-VOqv-_b981ENv7iIBirNB2n23LVqosUI4NRTQ0o7k04GxD_HDf52zvKJ4NVoO6pMbRpBveEq9EbhD0ysysqbMWXPMlV66Po9Mu7tCcEbzANIuXJycgGGr_H8f23H3a64DnWgQFHQVw9PMvpGb_JhlhcALQ5J3mF4gi8OPmRVHGMYOgILGuGK4ubUh5o0IIclHd-e3v0OVzLYwbJE9BoyYN94iTUHGiOkxDri6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اگه واستون سواله که موج انفجارِ نزدیک چه شکلیه؛
🔴
این ویدئو از حمله به تهران رو تا آخر ببینید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/alonews/124333" target="_blank">📅 00:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124331">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_5WclMqKjIONSmj-Fe9yWqxA9puwIvvRl4VqjrOF7KqLx2uoprGFk5SU7fpZxCxXNEGbP7PE20g6AX0v0T2Tf67fkboiab4S81Y048xp5XzO5JGwwUBH1dQ98IgaAGm7ctAwi0kj9TaD_N9bhqnQne8gTFUWDTmQ-bCmcNb30tNHs3QOwKJCnymMBXytG09kxD5-RZAV_eSg3aqDs027Ytf8KfennK9SCxY4kTEJFtT2AAl4G_0LImv5RARYSwStT8DKOeTK_cZI-6E5WESUeEktuxU3yV3rfUWsYC0ENP3RPan-BvcBaaZUlQk8A0sETCt6v1xcFVHObuH5poN8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDlL8MQlgdvgsQ_IaILLm6Pr3oOmRqAr8GxgAgteAX-ALnrp02fR5T6TUlG4l-arbg8QVFe1OIU3FjPhOC5UYokOEOWgAjo3nRHFz1T9bQbHdT9hkS7fqZrFNxfVnpgyPe74NSReEEE48_hm9OWcyUlxR9a2gpuGfI5RqmeG4XJEjWfo5DGGroyfxB2RWUsXGw-HBUKkJ7uWdta2r9h3afyfwkClBM0BqEV8lDF2PpPnVcxWLelI5lciHt92nbi2Mz-knCC-CA2xSetALCCvrO-VmY8URXDV6Bk_FN3oFtzhjijhB8tAheGFBACMq9Oy_t6RglwDQHCJW5AH3HY4Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💔
جاوید نام سید داوود امامی 39 ساله، دارای دو فرزند، از شهر میبد.
🔴
هیچ کجا اسمی از این جوان که در 39 سالگی پیر و جاویدنام شد نیومده.
🔴
رنج زندگی رو تو چهرش میبینید؟ هم وطن ماست
🤔
عرزشی حرام زاده، این تروریست بود که با اسلحه به قتل رسوندینش؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/alonews/124331" target="_blank">📅 00:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124330">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfb6BS8JcIrUoI-OldO_vvTcXEyHbt368MW8saDEpGarcXQIx16ejOZKRExEkqxlWWrP7bixZNPtuvZTQGhdeKBWXhtBnz791kmUgxXl9C_Eym5qKw1v_lLF7E2Ngq67dvSVzy7rgaM2BQuSbf0aDTlgP-FWdxxsb1B6r2UWx9REbeWzh_LuJ0Q1FkRK2e-BIKzwPIwee9CrG5xVj4iMy4pJkNr4jzwTn_j5AfFDdOOQGj0qn6cLbYdVdnU8hJp29HkkcSu_gxKS4gkM-1WCXZG6ZCBw_yDK6Dbv2DEP9RgaUHCRg2SCe5huaNTniO4EUsgjbhvLFSgc8lLLGqaxNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: جنگ نمیشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/alonews/124330" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124328">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEM4PgScoMLOdGoeNetWPu4Lv--3-0-FkmhFg3XsVWNy5tsRMee0TsFXmlHUK_xoZXXa2XKJnSJ0PUEqKJmU7rX3flxfdZjmrtuRrWkfhDSUKouYE7vld0m1Cm6uNyKcLttb3YfdKkqca9SYvURH3vm-2QuuJhAI1HQqfBcREPMluXC2pApfX2kXYx5xIKABWeTuwg9ZRGLghOU7AcqKLhA9FQA2zPD6ld7u_YwwT0UjDJhfhjUmUkmk72-tzA8ww5iTmcuRkp3FkqqqtwQ4OtWOJqPZ5CSjVsL2P8J8CTOEJhTMwhWDr17aHzx2gQ-e_oN0VIAsSF5ISeMbWgtJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JH1lHvI1mZ4wFs_9QQ41sei_rCQhsGIZJ0vcuSg9PRMmaGCnqYODuxYU2GJIwuklkCesLfZ26Fw2gg_RolCIuOWVyB3jAMpUh6ga0Q5mEs44WzKXlnt-Td0tYqaZu0d6c5NufotYc8tv6OGKouibgZ8W4EqlpPo1P8MJJW_32Ol4zP7OWxWT5-ePg5Pz7RNNTwIhfZtjw0CiuUQ1JNw6KkMTG7bsyjqZymnyxG9xJgemqLUEPkqT8waI_JkeBM_lYGW1HuBq5DAj7l1_U03UXlu7oeN1R0RDF-Jgkg2iSSqwmevHeQmsY3H4m-yr67Te_yAReFPa5Q4heTeKsV1hJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
سپاه قم اومد یه بمب عمل نکرده از جنگ رو خنثی کنه و ۲سپاهی بر اثر انفجار کشته شدن و بمب خنثی شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/124328" target="_blank">📅 00:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124327">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHI_UAmCrFyJtqUelTUjhVrIGYARDsfxfV78raaZZNpn-1TpVQM0oRTa8EUVbTnlavRWkO3kKQy97fwG-SeM_HxelMXyor4-xNRJo_p388JUdkIGMy4liDR7KzLCTDhXDKfXw17qFQzHF5AVdC8tuQSsWZJxFoit11_S9GxT95YWSWShlHSOC1JOW2gmJoS8WPl0dlDzfhVBoCddwt5KyKeKLY5gCH6HbKKwdq98iju8fOqZ1Xjf25dsRG4mEc-deI5UEmCcQTq6vLK108MWVamYeH0JF5XJyva6Bvew2Mq1oI8FL33MDUd44jHpXB04UcD9TbBAq8BszNWT7Yxenw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حزب‌الله چندین راکت به شمال اسرائیل شلیک کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/124327" target="_blank">📅 00:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124326">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/124326" target="_blank">📅 00:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124325">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/124325" target="_blank">📅 00:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124324">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نماینده حزب‌الله در پارلمان لبنان اعلام کرد که پیشنهاد آمریکا مبنی بر توقف عملیات مقاومت در مقابل عدم حمله اسرائیل به ضاحیه جنوبی بیروت غیرقابل قبول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/124324" target="_blank">📅 23:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124323">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
سپاه قم اومد یه بمب عمل نکرده از جنگ رو خنثی کنه و ۲سپاهی بر اثر انفجار کشته شدن و بمب خنثی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/124323" target="_blank">📅 23:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124322">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری/رئیس کمیسیون امنیت ملی مجلس: اگر جنگ در لبنان به صورت کامل متوقف نشود، روزهای تاریکی در انتظار آمریکا و اسرائیل خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/124322" target="_blank">📅 23:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124320">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQOcxzsCTeJ_g1WMpKyMLd6V98_oO8vd3NH3W3u0sH_IQKD5WMGWRLoHfakfidd9rMuO4KI6ib2qqtNlMUrolvBm5oYpfYavtr6FwDpUGOswxRMISt1g2SBl6_ScLPRGCOhaSs7dEUnBU9RDbfUCn41sK8xCkWrGulSDwFkOZDn_wN7U0hyNOLNwgjZCewy22N_DAugZvGAA-iK-NyqtS41zQNVVRBEx5gzATmUgrhH8DyTaMEkC-kYeAepD3GCdY8WRLs7XuLVTRbWIaSRrvCHtURPYReopYDW0TGkM_H2sNYGXfXjBNBpOAHWijyrFjJZnZa08vTvGSkxreyjWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WIFS8_4F6yzOFpLGBz9oSPPdm9kPH52-oaIBkg7IUEAFNGgHA46drzpanC2PjyC5puHHZLyGuxVzU-RkXSLQWg2H_ROmiO9KQKq36B22RcipHt8sSIToXUOoA96_GJ-auj1QdtR87raeSkpLiUhq9LbZdUdNlqbTs4fc7NAlVDY0CnKE_XjQfBDsGhdV1w3Y_dj1OT8Ssp7NQ5Fjg1p0XBUP_Mem4G6PyrHfFJCbQvHTvst_ummy_2bex8gzrESj918m2VbB8WB_AC_Sapv7FXXd5_HZc17luMRHDOLdwmPux10Dz8Zzonf4cHslU_i_ib7mDCOIdgoGdL-_xhaY1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی به حملات هوایی در جنوب لبنان ادامه می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/124320" target="_blank">📅 23:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124319">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/124319" target="_blank">📅 23:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124318">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17ae224db9.mp4?token=td5l8wCntAsYS1EPgeswOPUNA5sV3vmWt25QGFnogTONoFWO2ADBhpQkg00TxXoWAClZy_XSe3UNxOUhz6klCsiPJupD1WnF0cGtBvobV0pL4T1xLkPBngWvzUBK73RgapLZTSgO-8gicxuDu_0u9CwngdMgm_hZotcPgle_OliXV-XzpahpDCJS_CcUhD3UTYTU2lar2PLawDXZ5Nkz6up2r791dtoxJPAhPrhuolss4iHbt16KDQjYXqJgCIofEht98_-6X0s4BlbULUl15rggpN0QprE_ynqGE07fndf4qCPVpPj26J3MeP58-BLFl20LKQbgpm8a0Lk29Xmocg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17ae224db9.mp4?token=td5l8wCntAsYS1EPgeswOPUNA5sV3vmWt25QGFnogTONoFWO2ADBhpQkg00TxXoWAClZy_XSe3UNxOUhz6klCsiPJupD1WnF0cGtBvobV0pL4T1xLkPBngWvzUBK73RgapLZTSgO-8gicxuDu_0u9CwngdMgm_hZotcPgle_OliXV-XzpahpDCJS_CcUhD3UTYTU2lar2PLawDXZ5Nkz6up2r791dtoxJPAhPrhuolss4iHbt16KDQjYXqJgCIofEht98_-6X0s4BlbULUl15rggpN0QprE_ynqGE07fndf4qCPVpPj26J3MeP58-BLFl20LKQbgpm8a0Lk29Xmocg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روابط عمومی سپاه: در پی حمله ارتش امریکا به کشتی ایرانی  " لیان استار"  در محدوده دریای عمان،  نیروی دریایی سپاه طی یک عملیات مقابله به مثل، کشتی  "msc. sariska" با مالکیت دشمن امریکایی / اسرائیلی را  با موشک کروز مورد هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/124318" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124317">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxDjjUuhavWZaRKHpsCeRk_eAWSmgiB6-CdCS-h3unceQ-tY59VZz9VeIyHiWypcy6WuxCeJouNoswKrgYqiV0aBU70QIZ4nIBDJZ-mTTZ4WWX3QE0btz5UUdAIAuHCcPxF3sAI7eTAwF4A253V5qWuLs45hCocz6lYiVUFx2VDghbiy3kNXu18uCGPdofR2E1LFGDpHrSZVYHJ_YmmiAckE63med4maARpvm3shIa77FN1HjyUn2JCcZHMuAf9lCGpDBpdt8iY1_RVHPidOrGXdR_R1kWDwMSgq6OPUNy__3PpyKct9SeN_1F9SoP7a5S6jrO6oLt-JtYnvFifaAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۴ سوخت رسان آمریکایی در نزدیکی مرزهای ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/124317" target="_blank">📅 23:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124316">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvUnQSJOIPZfQDeZ53P4tI_0SyzZKsJkqAaynhMh9x3BtOFG0VCRcV_ApaEs6KjbULAAMH6b9tAlDRwWspvxCCuZf7pS9_6TWNsv2y9_U0Zj8Y9CUXimQ373Wc-AziYS36Ce__XrRzkSNfl-qdDUbmHiLAr1m2TfRnJZiilvJ80wengqY7nnniaVQmouzJ4nxKgTFqgmCoon0hMogt4x4NKNYB9I8Bf6WIzJ5m0PTno7iBy7Vn5EWZ0pm6rqX9kmAV5SVNCyAI6IP7Dm8k0Tc8oXWQKZfPrtX6gO8X40Hyy7K9Si1PwL52grxv0YlTEKgZEi27z83cKw_aqWF27ZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی و کیفیت بالا
❤️
تا ۱۲ ظهر فردا تخفیف جشنواره هم گذاشتن
❤️
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/124316" target="_blank">📅 23:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124315">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
هم اکنون موج جدید حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/124315" target="_blank">📅 23:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124313">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
یک منبع مسئول در فرودگاه بین‌المللی رفیق حریری بیروت اعلام کرد که پروازها در این فرودگاه جریان دارد و این فرودگاه تعطیل نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/124313" target="_blank">📅 23:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124312">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نخستین پرواز شرکت روسی آئروفلوت از مسکو به مقصد دوبی در امارات متحده عربی امروز دوشنبه پس از سه ماه وقفه انجام شد.
🔴
‌ این شرکت هواپیمایی اعلام کرده است که روزانه یک پرواز از مبدأ مسکو به مقصد دوبی از امروز یکم ژوئن ۲۰۲۶ میلادی (۱۱ خرداد ۱۴۰۵) انجام خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/124312" target="_blank">📅 23:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124311">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
آکسیوس: تصمیم ترامپ برای مهار نتانیاهو سیگنال واضحی بود مبنی بر اینکه او نمی‌خواهد متحد کلیدی‌اش مانع توافق با ایران شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/124311" target="_blank">📅 23:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124310">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری / بنیامین نتانیاهو : من امروز عصر با رئیس جمهور ترامپ صحبت کردم و به او گفتم که اگر حزب الله حملات خود را به شهرها و شهروندان ما متوقف نکند، اسرائیل به اهدافی در بیروت حمله خواهد کرد.
🔴
موضع ما در این مورد بدون تغییر باقی می ماند.
🔴
در عین حال، ارتش اسرائیل طبق برنامه در جنوب لبنان به عملیات خود ادامه خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/124310" target="_blank">📅 23:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124309">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سردار قاآنی: شرارت جدید صهیونیست‌ها باب‌المندب را مثل تنگهٔ هرمز خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/124309" target="_blank">📅 23:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124308">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIBw1jd2g0WKEJLbdNB9_N8oHZlI6hIMOpq7NDWvTJ3u5pVgKWbYwEIoIJAxLtRmmozgwIB-FE84Vpua2B8vv-Hp0SFSTPf7P7pNEWMsKl7y21QLeq3EzC9KGzNZUixqyXWPjuYOYxfHCsMvcluJtl7ixI1smVuUT5Lx6R91xRurPkfyG6-DwZFSJae0AdfwWf6dAkpRSwwnuGKElNy_elJq7EaJegovpLOWgXQyzsSZDlfmvHGve4_R3RePgzEZE9lpdV-yxwiDA2RVyzU520egCH6MXVcbvt6D2S4YfbF1Xo4GZjdPq1qmtFQEJXoeiI5TqhLsCSqWApaz3uqysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز آمار: تورم نقطه به نقطه اردیبهشت ماه در مناطق روستایی به ۱۰۱.۸ درصد رسید
🔴
تورم خوراکی‌ها در مناطق شهری ۱۲۹ و در مناطق روستایی به ۱۳۵ درصد رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/124308" target="_blank">📅 22:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124307">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی: ترامپ تهدیدهای نتانیاهو مبنی بر بمباران بیروت را عبور از خط قرمزهای قابل قبول دانست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/124307" target="_blank">📅 22:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124306">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام اسرائیلی: حملات برنامه‌ریزی‌شده به بیروت انجام نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/124306" target="_blank">📅 22:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124305">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سفارت لبنان در واشنگتن: دولت لبنان در دور کردن لبنان از تشدید تنش‌های بیشتر موفق عمل کرد
🔴
ترامپ به سفیر ما اعلام کرد که نتانیاهو با آتش‌بس موافقت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/124305" target="_blank">📅 22:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124304">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
دونالد ترامپ رئیس جمهوری آمریکا برغم عدم مشارکت ناتو در حمله به ایران، بار دیگر از اعضای این پیمان خواست درباره تهران به او کمک کنند.
🔴
ترامپ روز دوشنبه به وقت محلی در گفت و گو با شبکه سی ان بی سی نیوز افزود: متحدان ایالات متحده در ناتو «باید وارد عمل شوند و به ما کمک کنند» زیرا آنها بیش از ایالات متحده به نفتی که از تنگه هرمز عبور می‌کند، متکی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/124304" target="_blank">📅 22:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124303">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
کاتز وزیر دفاع: ترامپ معادله‌ای را که ما تعیین کرده‌ایم پذیرفته است - اینکه شلیک به جوامع ما به معنای بمب‌گذاری در بیروت است. معنای سخنان او همین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/124303" target="_blank">📅 22:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124302">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ارتش اسرائیل: یک افسر با درجه سروانی از تیپ گیواتی در جریان درگیری‌ها در جنوب لبنان کشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/124302" target="_blank">📅 22:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124301">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
شبکه الشرق‌ سعودی: حزب‌الله پیشنهاد ایالات متحده را پذیرفته و آماده است که از هدف قرار دادن اسرائیل خودداری کند، البته در ازای دریافت تعهد متقابل مبنی بر هدف قرار نگرفتن حومه جنوبی بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/124301" target="_blank">📅 22:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124300">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری /  وزیر جنگ اسرائیل: در لبنان آتش‌بس نداریم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/124300" target="_blank">📅 22:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124299">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیر خارجه قطر با عراقچی درباره تلاش‌های میانجیگرانه پاکستان بین واشنگتن و تهران رایزنی کرد
🔴
وزیر خارجه قطر بر حمایت قطر از تلاش‌ها برای دستیابی به توافقی جامع به منظور پایان دادن به بحران در منطقه تأکید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/124299" target="_blank">📅 22:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124298">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری
/
وزیر جنگ اسرائیل: در لبنان آتش‌بس نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/124298" target="_blank">📅 22:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124297">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بریتیش ایرویز تمام پروازهای خود به اسراییل را تا اواسط پاییز (۲۴ اکتبر) به دلیل تنش‌های امنیتی لغو کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/124297" target="_blank">📅 22:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124296">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
لیبرمن وزیر دفاع و خارجه اسبق اسرائیل خطاب به نتانیاهو: این نخست‌وزیر نیست، این یک عروسک است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/124296" target="_blank">📅 22:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124295">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
یائیر لاپید رهبر اپوزیسیون نتانیاهو:
یک کشور تحت الحمایه تمام عیار شده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/124295" target="_blank">📅 22:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124294">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
نفتالی بنت نخست‌وزیر سابق اسرائیل:
دولت کنترل حاکمیت اسرائیل را از دست داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/124294" target="_blank">📅 22:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124293">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بازگشت نفت برنت به ۹۴.۵ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/124293" target="_blank">📅 22:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124292">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
حملات اسرائیل به منطقه صور ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/124292" target="_blank">📅 22:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124291">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بن‌گویر وزیر اسرائیلی: وقت آن رسیده که به رئیس‌جمهور آمریکا بگوییم نه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/124291" target="_blank">📅 22:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124290">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHwfXREb3pLZkelkUoIbpcLy8vmbUQ8oDReo1FTcszT7V43DGHYIZfJY9px6sW-36x8dvEZsAEDW2UBYpVA0YB5QB-pufBBjcthwVISa2j2FOr_PDkIh0zZWXgGlu54bZtTmKSa_KvfCBg5oZmbF-iFjvU6zyEqZgipOqlefcwA1maMp8UVlUMnakbvEcnJszdE8W4KKGQwwFdJXA7b_cp22sLAFPQIhhvrgwUjMZSKGWCcJnWupm7KzTggJyUiqy4Q5F3pdzolA0XINyqPKY-AB8rjdtFioAelpJ-ny_Nb59WiVWPbUYKLlRKRD8qU15JQedn2kjiKDvxTnVlCa8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/124290" target="_blank">📅 21:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124289">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
عراقچی در گفت‌وگو با وزیر خارجه پاکستان نگرانی ایران از نقض آتش‌بس توسط اسرائیل در لبنان و حمله احتمالی به بیروت را ابراز کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/124289" target="_blank">📅 21:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124288">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رئیس مجلس لبنان: حزب‌الله به آتش‌بس جامع پایبند خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/124288" target="_blank">📅 21:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124287">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / گزارش ها از حملات جدید اسرائیل به منطقه نبطیه الفوقا در لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/124287" target="_blank">📅 21:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124286">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رئیس دفتر پزشکیان وارد قم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/124286" target="_blank">📅 21:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124285">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ: هیچ نیرویی به بیروت فرستاده نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/124285" target="_blank">📅 21:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124284">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سنتکام می‌گوید نیروهای آمریکایی از آغاز محاصره بنادر ایران در ۱۳ آوریل، ۱۲۱ کشتی تجاری را منحرف کرده و ۵ کشتی را از کار انداخته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/124284" target="_blank">📅 21:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124283">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
العالم: حمله بزرگ اسرائیل به بیروت با مداخله امریکا به تعویق افتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/124283" target="_blank">📅 21:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124282">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
موریا اسراف خبرنگار کانال ۱۳ اسرائیل:
در دفتر نخست‌وزیری اسرائیل سکوت حاکم است.
🔴
این واقعیت که یک رئیس‌جمهور آمریکا، هرچقدر هم که طرفدار اسرائیل باشد، اداره کشور را به دست دارد، باید برای همه ما مایه نگرانی باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/124282" target="_blank">📅 21:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124281">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c3f227d6.mp4?token=isBkl4_5CArYpiq2V4njPtxrcWvotvSzClzPJC1GZnzabzvmLkQSsREYhMt_cmJChn1lfi-MGpPRDCMzC9dslvhna6tkJ10qmcfUcCciE67_62ZocWpMnrtflYoEkaMz2xe4etepzv7S-ZGEQIXZaKV6YkXFoO8Scye2oD77dMEnt-ti90hfvqIQrpKdvLFY-BvsPRrDnw7sfw29taihk3WBdlA4XJXRXdvr24PQYNcxE-TrdItmUF39hiVKQow35j4Grn7c01FQ3ru3SafO9XtxjZZ_zzMx10bRG2CQqYu6XD0zqBpGpaTYv5Z6-2fhysWE8f4oTQAt5vR8qIfVgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c3f227d6.mp4?token=isBkl4_5CArYpiq2V4njPtxrcWvotvSzClzPJC1GZnzabzvmLkQSsREYhMt_cmJChn1lfi-MGpPRDCMzC9dslvhna6tkJ10qmcfUcCciE67_62ZocWpMnrtflYoEkaMz2xe4etepzv7S-ZGEQIXZaKV6YkXFoO8Scye2oD77dMEnt-ti90hfvqIQrpKdvLFY-BvsPRrDnw7sfw29taihk3WBdlA4XJXRXdvr24PQYNcxE-TrdItmUF39hiVKQow35j4Grn7c01FQ3ru3SafO9XtxjZZ_zzMx10bRG2CQqYu6XD0zqBpGpaTYv5Z6-2fhysWE8f4oTQAt5vR8qIfVgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام معین بصیری ۲۱ ساله
🔴
18 دی در تهران غرب شهرک اندیشه توسط حرام زاده های عرزشی کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/124281" target="_blank">📅 21:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124280">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رسانه‌ اسرائیلی : اسرائیل بعد از حرف‌های ترامپ گیج شده و از هیچ آتش‌بسی خبر نداره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/124280" target="_blank">📅 21:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124279">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aoj7Uy_d7jRCj22dR3_E0ZE26CfmA7kpdxBIMGkTvCfxDExr2N6VZKtsaWlVeXcKswPt07PjgH0fsTMuNA6vezEBYPY0rLjwWS1EdX2BDJD28kJNc2HM93LhU6Z4K_ELnK4fs1RmVPZ0AhHl3XRkU5UukWhctKt9Ts0Nhvnj9XK4OIUtm3lIGLyjNBlf8617C2sD1OEff1qoTPHsgAR019pzzJAjRWxYCA5LAK1TtcIvw8FS_565Sj2iFr_CWu03qLITYiCm6Q3DEfDm9f5yQU9hizgjzy_jq28Uf90Qa0KYB4lysRFCWVgzRfSZRu7mcfnAbejbJpCrW377W5t4jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: مذاکرات با سرعت بالایی با جمهوری اسلامی ایران ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/124279" target="_blank">📅 21:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124278">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI5-BZvH0v6DUarVVt-XtQ27aYdgQAXDswlObO8vilREKckWA-cz34TrXIYzCSuArmWBTEa_0b2qSip05J488nH4oZFQ8PUxNOojaByEJj8iMLQVtv6xgBRCkaszRmO2qtTZsdXO3axo8XR7-DhZ186LGCyo41h9bC8929bq_PhkUYS9odnKmBWdybI0ZzCRVuOR9URIoKdH74Fc5Qjt8JDOHPKZhEcLHiofHcabhB63Sxr3vmEvZlxhE3rDKYnAScWoeoM4_x4xm_22hZVgCGl7RC9HCXgKwGpuaW1STUpr9Bncr3qg0veVGmWopciCVryySgHVwGlizFPr3RofQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ آتش‌بس ترامپ حدودا ۵ دقیقه دوام داشت زیرا به دلیل شلیک راکت از حزب‌الله، هشدارها در منطقه جلیل به صدا درآمدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/124278" target="_blank">📅 21:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124277">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رویترز: اسرائیل منتظر تایید نهایی ترامپ برای هرگونه عملیات در حومه جنوبی بیروت بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/124277" target="_blank">📅 21:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124276">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رسمی/ترامپ رید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/124276" target="_blank">📅 21:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124275">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QsduDTKqgKzrNmH9_L3WZtO_pWas0eR6zfs3B6-bTG-aIbqkIn2-pJ8RXQy-yO--w6bh_BPyRirAnsQ7upqsU_Ct1DVfTNJNUS5McHJ2fe2dnEduj9TMyelhsO7Xh6DZL1Do_wF34tgtbdnrRlZKfHVNgv4yc8OVOve5f81cn8jr5utE-i9rw5XvRsBUG5fdIJy7wXARRyaDSewX3g65sHleSjbQuA_MH_-vkAFKAezXipppI3kvAeseM7O60E3UmjtCoU8DbXVg9mKV_5oSnN-gfZTGqxo6LbBJ3LSw7Zas2uS7mNmJoNxga_F5NDa69Z3KRNJ6uu_ng5xhJuYqLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: من یک تماس بسیار سازنده با نخست‌وزیر بی‌بی نتانیاهو، از اسرائیل، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد، و هر نیرویی که در راه بود، قبلاً بازگردانده شده. همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت کردن که تمام تیراندازی‌ها متوقف بشه؛ اسرائیل به آنها حمله نخواهد کرد و آنها هم به اسرائیل حمله نخواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/124275" target="_blank">📅 21:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124274">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری/ ترامپ آتش‌بس لبنان را رسما اعلام کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/124274" target="_blank">📅 21:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124273">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp3HcSRKko7QGHfuA8y_JBy31ZrdZLdc8UlGBpLRAMRDoQlwXlvkui2-SWaJN2G5ZbdAIMvwNM7EXG76CSK7xB8SB6357zKPmH0_mYTk3SrWF5-f1gk_DYUj-HR7JKnGwe6VO5FDWycao1sBioVGY8pCivQ3nTaiMSzt-pkdk0_pZzDsJRa9puT1Mb5_3VuIl86hRgQr0qfiygiyZ37-SVUCjfHAcNngGhRKQR8m611KzlsAS-rWh74oJngC4flcbTFRIZ_ffOpoCFMMdwMTtdYNJ979deGhnm5oRycB6Ss-q_yNy6HmDwvMDGcLtTYk2coB3GzaMqw6pkBP7V1Qgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی و کیفیت بالا
❤️
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/124273" target="_blank">📅 21:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124272">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
کانال ۱۲ عبری: تماس سرنوشت‌ساز بین نتانیاهو و ترامپ در میانه‌ی ابهام درباره اجرای حمله اسرائیل به بیروت.
🔴
نگرانی در اسرائیل از عقب‌نشینی از تهدید حمله به حومه جنوبی بیروت پس از فشارها و تحولات منطقه‌ای.
🔴
واشنگتن تهدیدات ایران را تهدیدی مستقیم علیه منافع آمریکا می‌داند.
🔴
ایران در صورت گسترش حملات علیه لبنان، تهدید به ازسرگیری تشدید نظامی می‌کند.
🔴
نتایج تماس نتانیاهو–ترامپ ممکن است در ساعات آینده مشخص کند که آیا اسرائیل حمله را اجرا خواهد کرد، آن را به تعویق می‌اندازد یا لغو می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/124272" target="_blank">📅 21:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124271">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
به نقل از دو منبع اسرائیل: در انتظار تأیید نهایی ترامپ برای هر عملیاتی در حومه‌های جنوبی بیروت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/124271" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124270">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
رویترز به نقل از منابع اسرائیلی: اسرائیل برای هرگونه عملیات در حومه جنوبی بیروت منتظر تأیید نهایی ترامپ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/124270" target="_blank">📅 20:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124269">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزارت خارجه آمریکا به تلویزیون العربی:
واشنگتن پیشنهاد داده است که حزب‌الله حملات خود را در مقابل خودداری اسرائیل از تشدید تنش نظامی در بیروت متوقف کند
🔴
پیشنهاد ما با هدف فراهم کردن شرایط برای کاهش تدریجی تنش و توقف خصومت‌ها است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/124269" target="_blank">📅 20:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124268">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: همه منتظر نتایج گفتگوی دراماتیک بین ترامپ و نتانیاهو هستند تا بفهمند اوضاع به کدام سمت خواهد رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/124268" target="_blank">📅 20:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124267">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ به CNBC : قیمت نفت به‌زودی مثل سنگ سقوط می‌کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/124267" target="_blank">📅 20:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124266">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ به سی‌ان‌بی‌سی: برایم مهم نیست که مذاکرات با ایران تمام شده باشد و نگران قیمت نفت هم نیستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/124266" target="_blank">📅 20:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124265">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ به سی‌ان‌بی‌سی: از نتانیاهو خواهم پرسید که در لبنان چه می‌گذرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/124265" target="_blank">📅 20:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124264">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
پاکستان: ایران خواستار ادامه میانجی‌گری اسلام‌آباد است
🔴
وزارت خارجه پاکستان خبر داد که ایران خواستار ادامه میانجی‌گری پاکستان برای تنش‌زدایی در وضعیت کنونی و حمایت از آتش‌بس شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/124264" target="_blank">📅 20:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124263">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری / رسانه اسرائیلی i24news: اسرائیل حمله در ضاحیه را متوقف کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/124263" target="_blank">📅 20:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124262">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2touFQHOlpYSdhUOpe57-dN1BthvRS9DYgCPciI_D_Y4QWaV6wY2KO61M5kSFs8uPPFLfhb3ut6RCYQwWZOtBDqBksw2WJdluhu0q9qmhb0y2sgjxetJmEwl3BPLZyLGfVpAlt5wta5MEe7cJiSGd3_kiabUtJT0NKQXBlZLcA-p1kaO34B9dVbzQq8FZnPIu-SzCOVlK4HFz7ajfyt4rweqd8_AyPPKsx-AgB1QfT7eC86Z4NZpWniMbVPHQX8lDhxNHBaIrjVcNz9qebcMF4yPYsatSOL7y1EBy6D8uhlmPNJvcYQB3StUj6na0LH2lNCZOMNwc5PtttMWichhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پخش تلویزیونی اسرائیل: نتانیاهو در تلاش است آمریکایی‌ها را متقاعد کند که به حومه جنوبی بیروت حمله کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/124262" target="_blank">📅 20:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124260">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری / رسانه اسرائیلی i24news: اسرائیل حمله در ضاحیه را متوقف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/124260" target="_blank">📅 20:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124259">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سازمان ملل : جدی خیلی نگرانیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/124259" target="_blank">📅 20:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124258">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjEn68fSM1Rl9B-918hEO54LnX_lh0hAQUmgvInt8mxIdo3DvcKRuJdQ1esXmYjRucSw9tPUZVqksaSrj8xU89aK-o3CnKSB6zHfffe7KRGdFaUuswkj-s3j0f-Ol94m0E4WYADNFwLFbJjInJtKnwTjgbaeSupUeyPG2CHjgVA4sZUFANC4SPwGjsM78WpxAK_2JLM83myzs-jV3iSdWyfVNkLAgEUhMFwZhUcp_W6JZeUtFAfWGgEll9LQFF-hFFgZTSMcpXA-waBOf8B1kYPNAlvXmkdGAdxS4GQMcXj90VS0Q0IITy1FrlKNY54szP4dAoUZWcEoGIeXe7WV0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه روسیه :  بیشتر نقض آتش‌بس‌ها از سمت
اسرائیله
و هشدار میدیم حملاتش به
حزب‌الله
تنش‌ها رو به مرحله خطرناکی میبره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/124258" target="_blank">📅 20:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124257">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / گفتگوی تلفنی ترامپ و نتانیاهو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/124257" target="_blank">📅 20:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124256">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
مشاور احمدی نژاد:  نگران نباشید ، حال احمدی‌نژاد خوبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/124256" target="_blank">📅 20:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124255">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: وزیر خارجه پاکستان در تماسی با همتای ایرانی خود، وضعیت جاری منطقه را مورد بحث و تبادل نظر قرار داد.
🔴
عراقچی نگرانی خود را درباره تحولات اخیر، نقض آتش‌بس در لبنان از سوی رژیم اسرائیل و حمله احتمالی به بیروت ابراز کرد.
🔴
وزیر امور خارجه پاکستان به عراقچی تأکید کرد که تضمین تداوم آتش‌بس برای جلوگیری از فروپاشی تفاهم‌های موجود ضروری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/124255" target="_blank">📅 20:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124254">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ارتش اسرائیل :  فرمانده یه واحد تو سامانه موشکی حزب‌الله رو از بین بردیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/124254" target="_blank">📅 19:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124253">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szVJ5X4_eL4rG3o8vKpUk67qlE8BgZ7jSOglBB6REciUkYWfXfyUI3jK4w3CTJdzWl6wG-_A4YjlD9ca4zSZGxqkKp1kh-i31kohhNNUwuhL9TlUd0pCHu4qSpAakFdFwJX25ocwqPsfEQeNy7dKEktFLyJgP6AIKR2DC15-Y3dCBd0KyaFhqKvhurVVtkfvx_BTVLEXre-xe3PoK24kRBX7mp5VSSRyKHFh0gkCCvikqYcNGbcjVmKfqbIrMl_O2bn1MuiZTwWhltUGv9pIPamy1SQssLZVhvBv7SBZCVeFuufFw3QLigYIoBkSnfw0d5mYjzf3tNfwiEc7C8kBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی: تحریم‌های ما علیه ایران به محکمی فولاد است و به همین شکل باقی خواهد ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/124253" target="_blank">📅 19:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124252">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ : اگر گزارش‌ها مبنی بر تعلیق مذاکرات ایران با آمریکا درست باشد، «اشکالی ندارد»
🔴
ترامپ گفت: «این به آن معنا نیست که ما برویم و شروع به انداختن بمب کنیم. ما فقط سکوت می‌کنیم. محاصره را حفظ می‌کنیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/124252" target="_blank">📅 19:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124251">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
دونالد ترامپ به ان‌بی‌سی نیوز درباره مذاکرات با ایران گفت: ما بیش از حد صحبت کرده‌ایم، سکوت کردن خوب خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/124251" target="_blank">📅 19:49 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
