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
<img src="https://cdn4.telesco.pe/file/f_qNT3E3MIMIrLfMkDfQau8nTg45wvoAADe5ExpfLPCAs0QKHSu82xi_FemrUJIg35TR07mwYNB7DFgOlplcNB_UP0xOK2TBUqb0EukKp7mXIX_cxU_O71eFwY095VJXJb3vccU0hQkifq-x_yBRio3cn3sb_vG6aVsne93nBTVsmP3u50_PTDw-IGvbY-EruJvgoVt89b6_fxvMO2trSNGR8EHd-ImynaqxoxlTBdRntjn3LRFV0ZRUgmtz4GLBq03u1w7Yg7OcbPvDaHVHZTqJXouPFe740HsZsttZ0CrFs0ZcAwV2NYpyFTQFyrXSyxaZPJqQI3rnmoGaPn0m2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 981K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 02:31:12</div>
<hr>

<div class="tg-post" id="msg-127765">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNqCB-Ayma5ZePXfL-merplQBGeq8jdT4XVV5mmaEm5G6IyMBB2uhEQ7Vom4HEIBdVOqQH_JlRQA7SWGHWLO5_2-DE6wK2GywxfZfnj2moBLK05iEDW3ZgNtSIF5nZUtL-WdguADzyIXS5MWyfNlE0aZzmDLCcXg5j04mkIb5XuBz2JEORzYqBU6oPSBSNnE5edW9DcbLi0QRRuBfdllQoBPtybh7dLhPOy4RHKpqW9rPWd1eZCS-g-XermTUSOQzqkxiChpDRU95uWd05Pv4VksxoKVMG-jZUSiPW7nl73wlTq5qNJ9LIF0vcueEdgMQn3oat5_KKFFkT2mmCFjDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wk_STw7e5Qjns_JJb0AnGNHwbOe7xlF7Tr8EJoZVskLIRwPUImhWN-7_x_lYENsp9ONvWXW1XlyXKKmZy9ydRKdo1833bJ0BgzAnyHDbW-kQ_sNqAus2Mpi6scnVnkQPkImIf2yM-0buaHx7gck_bA17H-xlN1yn8wpjWgJiBezx6kvMhI_djRCY3LloghZXkBJ1XcpEWITirW69XzuXnbM9D53W4inCD9nWHyrXDrRyKRH-FuAWUfnWbSxvWtM6FVZCXnPHC4GpxP6DhP1_LuR9Hr2Xrq7lebxWA7OjSU1_-puCX1RiHW1XwtfIAm9w7WVnO-S-q2isU0QI2AYqng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
امشب تولد‌ ۸۰ سالگی پرزیدنت ترامپه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/127765" target="_blank">📅 01:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127764">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1ee53f0561.mp4?token=N8mqst9JiX9jW-VLrTj4BfwmJFQ7G6N3vAJ7R1UWJMC2GwhFH_C9bJjqTGBjdSY5zqns5U-R8f341YieLzKHwsO1afgjITTpbcFyTgNTCrmWCS-WDMhi4BaC-N_A-6IG-ZTsiEclNlYmltzGpDsz33KhzRxnD8XbQH4Z77uIDF2szuiCGlvjudKl8J17TyxggGPt24TZk7yg4HmhtUBj-fEtUbolbavOMztuo-zhXjHOeMle_v8_IZh0YIcHRN8WvrYQ3FgJaJ0KrzFhOoV2jC14uYP7Log8ZI-2zYA8ayjAWWqTzk6VlcWFSOh41b_RhAfdZABlyZqfSLBvJgrnQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1ee53f0561.mp4?token=N8mqst9JiX9jW-VLrTj4BfwmJFQ7G6N3vAJ7R1UWJMC2GwhFH_C9bJjqTGBjdSY5zqns5U-R8f341YieLzKHwsO1afgjITTpbcFyTgNTCrmWCS-WDMhi4BaC-N_A-6IG-ZTsiEclNlYmltzGpDsz33KhzRxnD8XbQH4Z77uIDF2szuiCGlvjudKl8J17TyxggGPt24TZk7yg4HmhtUBj-fEtUbolbavOMztuo-zhXjHOeMle_v8_IZh0YIcHRN8WvrYQ3FgJaJ0KrzFhOoV2jC14uYP7Log8ZI-2zYA8ayjAWWqTzk6VlcWFSOh41b_RhAfdZABlyZqfSLBvJgrnQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما: خدا شاهده همه اماما اهل مذاکره بودن و با دشمن‌شون گفتگو میکردن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/127764" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127763">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWpN1jWdnhdmz-KPXvzsbTpmv5Auibe6DMG201pbDydgek4Om539X2g53FrxP88lCgQm7JWPmfD9SUpk7HhDsRw942luriEoXBlQGHUxt3-UVLL4CT3hjHdq9xZX59P8msxX9GrATu2_rKjovkgeYE3bZo4fqlE_w46QKzvqi4Iy2l_RPN1YhYvUNskkCMmCB-hcrq-vVM6gO37bEAe1OwPsHwBlHkgnm0FM45dnS55YfmtxLCa8d9j9LdVdI1qvksnE0eXDkrlxKgTTS6qgDz-k0-urOuQDyS3sxM20b08PQ_Gom7WuTfXbtSqLN4bt2UHRdWtDhypiK-PexeZaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رائفی پور: میتونیم رمز ارز به نام علی خامنه‌ای بسازیم تا همه بخرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/127763" target="_blank">📅 01:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127762">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
آبروریزی تندروها در همدان
🔴
صابرین: ساعتی پیش در همدان و در مراسم شهید شادمانی درگیری رخ داد؛ عده‌ای خاص با برخوردی تند و ناشایست (مخالف مذاکره) مانع از سخنرانی بقایی و حاجی بابایی شدند و حتی به فرزند شهید تنگسیری نیز اهانت کردند!
🔴
دختر شهید شادمانی سمت آقای بقایی رفت تا از دلجویی کند اما این افراد در مراسم شهید شادمانی به دختر شهید اهانت کردند و علیه او شعار بی شرف دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/127762" target="_blank">📅 01:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127761">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiv5GNsPFY5X2htjIqd3suAbqA6-DTVjoGzViKBy5BhKAryVGyu1cq3FHnv1JKyMdBK221jzxSP_EM_sabkBaoKdzxTMAFpNcLkQc7JBFV5eWFTa3lzIOV_ZUbiKMr58WIxgwlZ61X1T5bUCddC3yJxAbIRN-Ap5aPn8w-HG5jhv8oNHCefBi9lqa1OVFnX5TRBsA2Km-OWlSgO38GwauGxm4EsbyFQh4Vt1jUdUPd16QEoTrR8kwfv4dm4-JsuqhHHBJtpw-cBdauVl75SuEHM8VVhgp3YdcrLrC0lI_qOZonxCQ1onb53lnYrquzcvnwLODXtR2g555IemJuuysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش‌ها حدود ۱۰ فروند ترابری c17 از کشورهای منطقه بارگیری کردند و عازم اروپا شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/127761" target="_blank">📅 01:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127760">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adca31cc4f.mp4?token=d7IOuGbyktLAqaPtrFyJLjCR013skRZpYew57YsBe7N6XXrPpuPd-k3bHxLqz9Bjwnw71rgkBn3uLTNZRebyfQei089w2DhCoQfepH9IEwnmVxjPNIIbdbERs9Y60FWQWe5bQfJgvhB4fu6MHzXwDVNFhGI3fDLTjJFLsDoyFNYSKl3B5hxcNK1Ike9T6JMJ7qFsNkY0Z8WYy5LCCmpJ5BaxJoOeG-FTXPuhCTSb40ZB1fYYCtBE7_gvLcEn2U7wQqSWl6-CBd2iq77ptBjgkyUIYPPIK1AEHQ0dlEcBV4uKGxcCZTTWQP2Bntpq2R9ypQXEwiehhQxkn6U5MGsO-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adca31cc4f.mp4?token=d7IOuGbyktLAqaPtrFyJLjCR013skRZpYew57YsBe7N6XXrPpuPd-k3bHxLqz9Bjwnw71rgkBn3uLTNZRebyfQei089w2DhCoQfepH9IEwnmVxjPNIIbdbERs9Y60FWQWe5bQfJgvhB4fu6MHzXwDVNFhGI3fDLTjJFLsDoyFNYSKl3B5hxcNK1Ike9T6JMJ7qFsNkY0Z8WYy5LCCmpJ5BaxJoOeG-FTXPuhCTSb40ZB1fYYCtBE7_gvLcEn2U7wQqSWl6-CBd2iq77ptBjgkyUIYPPIK1AEHQ0dlEcBV4uKGxcCZTTWQP2Bntpq2R9ypQXEwiehhQxkn6U5MGsO-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت‌های یکی از لیدرهای شلوغی‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/127760" target="_blank">📅 01:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127759">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h1RnV0xb_yd0Gl9xfQNk_v1QITQTFVVF-BrqB2ACUGMh8hrkW8AHfx07T1skLiZRHW_nS1jzfgMZrpdOOUJMwUQ-RPxUjrxbZfWfoJPg04omYNmsJf-GjtAo15QOpFihD262rVuhyDXx4Qb0cAy6ioSUahTPiYbNuCkY1NGrckfyO070_T4R02KSbaJpZzej91AXOsp8JhurrMPrHHtMluFsaA8S-mq6tF3VOCJ5kvqUTYk8glClRTcgCmKbIoF8pV8GEencbeMR80ae_APL-d2OYS7eOOrO62p3JW0j8GVIdpHTmy33mrjSJy1j8kqS_qGEvsyk9xT_Uh8vJ3NtaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فقط عباس میتونه جوری توافق کنه که:
جمهوری اسلامی ناراضی باشه
مخالف جمهوری اسلامی ناراضی باشه
اسرائیلی‌ها ناراضی باشن
آمریکایی‌ها ناراضی باشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/127759" target="_blank">📅 01:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127758">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
خروج تعدادی از هواپیماهای سوخت‌رسان آمریکایی از فرودگاه بن‌گوریون!
🔴
تصاویر ثبت‌شده در روز شنبه نشان می‌دهد که شماری از هواپیماهای سوخت‌رسان آمریکایی پس از ماه‌ها حضور، فرودگاه بین‌المللی بن‌گوریون را ترک کرده‌اند.
🔴
تنها تعداد اندکی از هواپیماهای سوخت‌رسان آمریکایی در محوطه فرودگاه باقی مانده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/127758" target="_blank">📅 00:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127757">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz5UfQ_X5OIFh_F8HEgGCaSXXSNE_j38NIGoc427ZdU4g9McX3GNzc2vRi6t44GyBUtz2TomvvZBTm9xHN35UWlwdXGAlTsFiXre2FMVlLx3H5zfS44HQT90ewFnmJaFw7cMDHhEEdN1_RJu5SQ2DYNUXTUXQmoQBE0N34_WnsMBYc7V9dW-B_OU9pYlm0aZz74L76TAgaECs9yF4Lqjr7-pjyhLlghKGsaAZ2GG1_II7UPWygC45nn77xfM0J6g99FR0KheQhsZzJcThprsLpgK91LOJcpU26JwaIbTsd5oZDBvgth_Acz6GRfzKBmtH9M_PrVgIycCw64U4KUnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین طاهری مداح در میدان انقلاب: تندروهایی که امروز شلوغ‌کاری کردن هم ردیف طرفدارای پهلوی هستن که شلوغ کردن، باید مطیع رهبر بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/127757" target="_blank">📅 00:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127756">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=MztnWDCwSiWYBiA1FNl0IngH3jDHSS_API8kuoSnHXaBihEzJ6KaSWH04_q1EDPJ0xiOAF3URmSTm50Kb1sUYpuzm9ciKvFLVJq9pNTIhgqTPdIxA2bOr7vPyfJhRr7uXu-bfJ7tOHkzb6Wm-8JT2hIhHqZZn9-ci_MYKU2cmLAYe1wzkF-_E-OLLWQGplavuKKlcJpoNQa1UAKvKV8VAvfdktqTYFDK-5yX6rQXC6Y9_toYWDK3gGAYmZMrFLkznRdGFUfSuDHcv_HsK8DGPpa7BLWjK89C54iUIypKBa3CR2lO1RxW1vasN9uslLYIPksbtBr0jAq2oUtRqHmsoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=MztnWDCwSiWYBiA1FNl0IngH3jDHSS_API8kuoSnHXaBihEzJ6KaSWH04_q1EDPJ0xiOAF3URmSTm50Kb1sUYpuzm9ciKvFLVJq9pNTIhgqTPdIxA2bOr7vPyfJhRr7uXu-bfJ7tOHkzb6Wm-8JT2hIhHqZZn9-ci_MYKU2cmLAYe1wzkF-_E-OLLWQGplavuKKlcJpoNQa1UAKvKV8VAvfdktqTYFDK-5yX6rQXC6Y9_toYWDK3gGAYmZMrFLkznRdGFUfSuDHcv_HsK8DGPpa7BLWjK89C54iUIypKBa3CR2lO1RxW1vasN9uslLYIPksbtBr0jAq2oUtRqHmsoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار در تجمعات امروز: اگر چیزی امضا شه، مسئول باید کشته شه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/127756" target="_blank">📅 00:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127755">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Olonb5p5FTwg5Jh8sTWqF_SdS039boGqfCcxKbGGfydrOJ5-9C7QEYHdIfsoWq8oHBGuY4LHqg_bdjHb7ueiClltNm9aXO1oI6UqRy1AF3Z0HTgr8zRwEyuSTrsPeN9RG9SUzdYFRDl_5DguZgmnuUhwyfbIkhTJpUe1CGkIS9ruMzfqDCYyBVghr0d5lAHu8YxxXallMmUAaYNC3Gne47IiNCbPQeth_GuU_ikmgLQxK476A9XE4JkM1HwTgD7CSSC89KthPAVkGq7JZ5b2zsEp3Y_XU0Jp2No4QFtlyXL-HI5zob696RN2Ij_dMrxhY3OQT6UkNYFh0zv-q4ESzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح از روبیکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/127755" target="_blank">📅 00:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127754">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt_xwQDbesDzyUIDPyhuooPTQoDwZ4NmxjwmeHmSUJE-LGtG4YZlepgD_3wiypWOSr20833LEkMA-C2pBJxmEa8TSrSxc3CcsAFcOeS_ZDAomMLgOHEedbb2VUbs7M8WmHulJom0qXKaR7aidDRcd5D0nx4nrxXmamUZK2_R-FMP_C1DUn2Vapp6lj4Bf6rcFeungr8E6T3CDWTRsHtMRrUdNaVmx2WwnTkQhBnBKfxy9N2fHT5IdlzeXZUHxevxWRNvhg3GxnfZBuBgwcAjEZl8L3HeWiRVlLia_19psEQ_C8YbCcW-aEipo6vTIG_wxonJJU9smSSJulnCyYFOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست یک کانال مطرح عبری در تلگرام در واکنش به تجمعات پرحاشیه امشب:
خشم بی‌سابقه‌ای در این ساعات خیابان‌های پایتخت ایران را فرا گرفته است. هزاران معترض حامی رژیم به درگیری‌های مستقیم با نیروهای امنیتی برخاسته‌اند
🔴
وضعیت بحرانی – فریادهای مستقیم علیه رده‌های بالای حکومت:
معترضان در تهران سد ترس را می‌شکنند و خشم خود را مستقیماً به مقامات ارشد رژیم معطوف می‌کنند. فریادهای شدید توهین‌آمیز اکنون در خیابان‌ها علیه وزیر امور خارجه عباس عراقچی و رئیس پارلمان محمدباقر قالیباف شنیده می‌شود.
🔴
توافق با آمریکا در خیابان های ایران به عنوان «توافق تسلیم» شرم‌آور و خیانت کامل تلقی می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/127754" target="_blank">📅 00:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127753">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
واشنگتن پست:
قطر به ایران پیشنهاد یک معامله مخفی علیه اسرائیل و آمریکا را داد که بر اساس آن ایران به قطر حمله نخواهد کرد و در عوض قطر تولید گاز را متوقف خواهد کرد تا قیمت انرژی را افزایش دهد و غرب را برای پایان دادن به جنگ تحت فشار قرار دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/127753" target="_blank">📅 00:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127752">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d50508a6c.mp4?token=dswS1tVGta5DiLNl5QyxOCAHU46JH79IqXOnju0Xl3_iRto0f9tt6QFiZ6geQ7lGO3Yo_rtJ_G-TnotuzOYNYv4nV6YA8uHtYQH2rZWDRgYn7EX0vyfRjzwebsiUEd1wmDNuQ7A1coR0x495__81sPGNrC8lIfOw-Aqw9dJjGwdDPyNAZfcGD04yeTf09sHm8FlW-J66kzHVc3nNxrd4HQXLPM2UQ9Txe9MxScDP5RbSkt_yKz5QvAwkvW8bUiD1WGWHablsb5WtT6tuwvzTDVOxbzhAEv_PTZ0t_R3rpsFfXILaG4ilEVBafDSfcIA9ayZz_8xSwEB7J4135i2cwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d50508a6c.mp4?token=dswS1tVGta5DiLNl5QyxOCAHU46JH79IqXOnju0Xl3_iRto0f9tt6QFiZ6geQ7lGO3Yo_rtJ_G-TnotuzOYNYv4nV6YA8uHtYQH2rZWDRgYn7EX0vyfRjzwebsiUEd1wmDNuQ7A1coR0x495__81sPGNrC8lIfOw-Aqw9dJjGwdDPyNAZfcGD04yeTf09sHm8FlW-J66kzHVc3nNxrd4HQXLPM2UQ9Txe9MxScDP5RbSkt_yKz5QvAwkvW8bUiD1WGWHablsb5WtT6tuwvzTDVOxbzhAEv_PTZ0t_R3rpsFfXILaG4ilEVBafDSfcIA9ayZz_8xSwEB7J4135i2cwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نبویان، عضو کمیسیون امنیت ملی مجلس که متن نهایی رو دیده :
با امضای این توافق، رسما مستعمره آمریکا می‌شیم!
هر بار که ترامپ بند جدید اضافه کرد، آقایان عقب‌نشینی کردن و گفتن چشم.
تنگه‌ی هرمز بلافاصله و بدون محدودیت و عوارض، باز میشه؛ حتی واسه اسرائیل.
مواد هسته‌ای باید رقیق بشه.
کوچک‌ترین غنی سازی بخوایم انجام بدیم، قبلش باید از آمریکا اجازه بگیریم! حتی واسه ساختن دارو و برق و...
آزادسازی پول‌های مسدود شده؟ معلوم نیست.
منفعت ایران از صندوق 300 میلیارد دلاری؟ معلوم نیست.
رفع تحریم ها ؟ معلوم نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/127752" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127751">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
گویا تندروها فردا هم فراخوان دادن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/127751" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127750">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی به وای نت:
🔴
این یک توافق بد است. هیچ‌کس از آن راضی نیست. آنها می‌فهمند که این برای ما خوب نیست و به منافع اسرائیل آسیب می‌زند.
🔴
چیزی که نگران‌کننده است این است که اسرائیل نمی‌تواند تأثیر بگذارد و صدایش شنیده نمی‌شود.
🔴
این عمدتاً یک «توافق جام جهانی-جشن‌های ۲۵۰ سالگی تولد ۸۰ سالگی ترامپ» است.
🔴
هدف این است که برای همه رویدادهای بزرگ فعلی در آمریکا کمی آرامش بخرد. واقعاً چیزی نیست که دوام بیاورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/127750" target="_blank">📅 00:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127749">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
انتخاب: تو مشهد کلا ۱۰۰نفر تندرو تجمع کردن اما هیاهو راه انداختن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/127749" target="_blank">📅 00:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127748">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzEsmktzPhrhW9COwK8T2W_aaKLUgeBOvjzLyy9ZrpXTZM_xS0rF0BSxB2nVSBGxjiBUIs5S9Fm3AkQ9HQAzVgR1Vgp34Rjv__N1W-iFA_Pt8oJfNtnt6Dp48fRCQxtDftby1Vj2MOYCkaEfPO9OF_Ttbij7K-TUT8RgO_nk_2DyYnClVsYvWlwzIYTjNVFC9oQerfN0IaPvV6LliCVTxSOwQGOJUvGq56pWgtXO7T0JARP1qWe8ZF1BzXiu4DCGNOsh_9A5vDZyWfW1iq4h_cVWLdMnJXnvEF44RkWW-4JzVygPL7BuAw31pgPqlxHXeR0MgyibEZ_vbrC6gtVh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری فارس گرای ادامه شلوغی‌ها داد
🔴
۸۰ درصد شرکت‌کنندگان توافق را به ضرر کشور می‌دانند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/127748" target="_blank">📅 00:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127746">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVujUNxuCJBLsaO5F0ymjgY5_lBg-RTh8iwN42yY4g6O3_M6BxiI_7JfmZAghR33v_Gh5fNyUmFVP9ekDx16gtknMx1VsQEWkhIwua5IYNOUN88uOFM24OaLfNQjcC0JEqiXn0ewfqLYt4YmM1hK2SNLpf4VLluMoljlZk3uExdlxeXfS0jv2YzJPxKMEQ2E0nV-KnKnIRDc8kVg6j0Fc-o6XvGCY_BGsLgzLgq-ug3jLYiJ0JgIN76wXIlNurM1KSTBaExZbyj4Rux7uNRID8Fc9zzBrtcS2UmdFngNAscdk0iYkvQ1HuHRNWmnxk5RMrlsaSG9IplsjZK-kkQBtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WiF0NT9QiaNEhiqyGVcuhUt6WbTfWqEROMdvvleCadlWmo-y5-yV0QbMJtMOv7ZC-MBjpAiCW7LHlKY9U5HZJhhdyLWELkdmn7tx0evZyyt3Vcfu1VIFr0sx5cJZhC6EpLtJ7UPuqjxkA55cBGOSzWLOtKMGiOiEjSPVFbqd-3yfRtYKqA--mIRnv-qQoN_YU3mhAqyXwj8o_02hexaHLayXB82PQ2Msnz4RJsw8fJ0cFrDm8RsuwHNlSddZNFVveU-fUlL8xLXAajIwqSM_CkmQnn92lEOYQ6-0drkrNByODLyB8QKt3PXbuJrrZrfngVSy7K8lYIVcu8hBL_NtkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
درگیری به روزنامه‌ها کشیده شد
🔴
دیس و دیسبک دو روزنامه نوبنیاد و سازندگی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/127746" target="_blank">📅 00:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127745">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f489787669.mp4?token=Ag2SeiIjOZhDpqHXt6rdzCENrJgjuHQid_DBQRKcKGdNkYGBpRWCXbAH4nKI-_ZZ-xOfzOSaNseP7lSbnVCrTopedRpRhM9M1hABQyDHuFGPbdzWU2gMTYL6sUTdD37aIQ_0t2zw_Le2CqEvNGLMZ6aluhx-H1Y21wOjafbHYrFZE9ddQY2uL_vrXZrG6nimnC8VilKTNkk53j0mzfpIzCokXJmnRQhnqXFy1UYFKkfI1s0gT6dU_E71zmELPu5hhqXiK_Ojolrdjqkb2hR6YK8AeLUBQBWBS8ta1fZa7rXXY2TvZRyAZhHCP1e-35VaCk3ETdANH_BPl0B3Dhddhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f489787669.mp4?token=Ag2SeiIjOZhDpqHXt6rdzCENrJgjuHQid_DBQRKcKGdNkYGBpRWCXbAH4nKI-_ZZ-xOfzOSaNseP7lSbnVCrTopedRpRhM9M1hABQyDHuFGPbdzWU2gMTYL6sUTdD37aIQ_0t2zw_Le2CqEvNGLMZ6aluhx-H1Y21wOjafbHYrFZE9ddQY2uL_vrXZrG6nimnC8VilKTNkk53j0mzfpIzCokXJmnRQhnqXFy1UYFKkfI1s0gT6dU_E71zmELPu5hhqXiK_Ojolrdjqkb2hR6YK8AeLUBQBWBS8ta1fZa7rXXY2TvZRyAZhHCP1e-35VaCk3ETdANH_BPl0B3Dhddhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار مرگ بر قالیشاه در تجمع پایداری‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/127745" target="_blank">📅 00:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127744">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEJofdPjyWLf7f1q3ovBukaASmkSdTKw35wHseI23UiSIAP36LfpV7AlO2EYqyETZBRzxStrhCYTfihj5RFbHnuQCLFf0ov4EJW3IMJw-FdtIwzhclrhD2aOQ9oGnFEoBWRw59TwaCyDQKCwgD4j66q4aYIFf444EmFW_ZCL0Z7niWDVAUFtoNzmT7MJBGeomDDJfm2KzQbk6MZbbJG6GYrp4TG6ObuLvaT5B92y-e8kqpvCkFzwpsBiVrvvbdUpPowzqYmvt2_4KR7IYWJXQ3R6TxpGRRQr6LWyA5i3IYD74DVZ52jJnRHDnFWNfE7QpBgPCg1xh0Qrw94QQ-mEPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیافه یه پایدارچی رندوم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/127744" target="_blank">📅 00:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127743">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🤴
رضاشاه روحت شاد
🔴
فقط تو میدونستی این جماعت چه احمقین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/127743" target="_blank">📅 00:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127742">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrxvYrsEyyCIxtXPYw-hLlBMZ6AOaD3A6Cp7DCRsZlmvNz0aVGT6tXXFWMwriW4e39LW9kcnhvldLKZjYplQI4yv4FoAOSE00ObbCvxyTFqtXY3leteF3kcen2zlF9ciMfOeG_1p-VB2GgkkJ8XzXQ1aFWKY2zLrx85piDhC0iNZ_IvOghXgVcXzMOS61cPnQAGzWRst_mjeewZewqTKrZUaah7orq-pYhHdyDlgwm49wadeejiPknYpC3X6_Vh7Zaf-jhlS-21yuPWVJy86b2bhqJmp7UxJSxzvRdtZTCUXbwVDQwtXm0sN8UtJ_-YIMFhGLcqPQjOX42HEpaF7bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت کامنتا
😂
🔴
من خودم بسیجیم ولی الان بحث بحث انتقام رهبر شهیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/127742" target="_blank">📅 00:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127741">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJe1D66iYL9QYCTVhovtuRG2kh2WCJd4DE5BCL9RskZ4Q9f1VK3E1Y0svmGFckvY1i_ORsi44m99zX8mzcocIqJhPIl38xFQE_a7TM9VrYxkJOhWkJsUWE2HLn_KbXJGih_h4LoQmBRAPt9chWU9LaoOTTce5FwDOO6YthBJnrelf3EM6u2Q46llbVhzXPn_udBF6OiMneBs9E-uHH7i6ciLOb8WaraqdEEcFSEfx4RcrX-ITPVFnEh_sOgGan2Ealxf4NqYpV_kPo7hkPiQZQhvBD7ZgmU_P8Rq3jFn3HithlEkz-DW3ZwZBwqjMYQQisGULx95rHf7RtzJXtwGwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: آمریکا پیروز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/127741" target="_blank">📅 00:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127740">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نکات ایمنی برای تندروها:
۱ـ چفیه نذارین، ماسک بزنین به صورتتون.
۲ـ عطر مشهد و گلاب نزنین تا شناسایی نشین.
۳ـ اپلیکیشن بله، ایتا و روبیکا رو برای ساعاتی حذف کنین.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/127740" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127739">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
خطاب به تندروها:
🔴
هر کی ناراحته از ایران میتونه جمع کنه بره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/127739" target="_blank">📅 00:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127738">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6743285f93.mp4?token=tiUUGZseKKNL7pdTlOANinSsZTtpxM51e0MO7XQcil16tE6l3tee1WhiICMael4_HMkNcmrjtvHC8gHN4PCvWfpa0HL0QgubgB-3fYUgB7edtbg4kqk5ZAdsEVvbV-wkZ63fvhrIi2WpOXPkEneYfHXWs_zPrIiU5AsLOVJVNg0ZHDW1o4Yq3_CGujbKhGrxxtEQlwI9OtFGv57t_MrIw4jGcL7WJqQZ8nRJlvnfJKc6zwS9FqciR3NrBYdEb1IGKyTLh1P1CU-mJtTMXEQ5HmeIn1aCOr1-WA46ReSO6t_iDD-XuhledykpseVI4cDux4-MPgRYvuKfPr3btUgncQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6743285f93.mp4?token=tiUUGZseKKNL7pdTlOANinSsZTtpxM51e0MO7XQcil16tE6l3tee1WhiICMael4_HMkNcmrjtvHC8gHN4PCvWfpa0HL0QgubgB-3fYUgB7edtbg4kqk5ZAdsEVvbV-wkZ63fvhrIi2WpOXPkEneYfHXWs_zPrIiU5AsLOVJVNg0ZHDW1o4Yq3_CGujbKhGrxxtEQlwI9OtFGv57t_MrIw4jGcL7WJqQZ8nRJlvnfJKc6zwS9FqciR3NrBYdEb1IGKyTLh1P1CU-mJtTMXEQ5HmeIn1aCOr1-WA46ReSO6t_iDD-XuhledykpseVI4cDux4-MPgRYvuKfPr3btUgncQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از مخالفان توافق:
بر پدر و مادرتون لعنت غرب گراهای بدبخت. عراقچی خاک بر سرت. مردم دارن سکته میکنن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/127738" target="_blank">📅 00:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127737">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiAc1Tapm681SBC8hXHXlG-tFP99QePetj99q84kak8h_f0clEkzdKFj_xZcXVF1gSZGi-d92IpdAnHlQ5AFFz6cO3IhuZehEg1MIOdCg599RHWrO-bRplupX1_U0VNxxZo_68ggDLlqBX3RVM29NOKDn24Ga2N-e3AhuwPZznP7pmlYGmd0Lndd7KXq4KpfZIHc-sA53KeumeivSELiApMTK014u-XgvWl8LNjoDIHdah82qxbXkSVrpoKN269ZpyJ4nzH5X9jrmcm0uB3krFUuW3kgO2NI-Gg1KktkITMN-kocjJOvQS-3ntYXobEqfOTUQ8f9g5ROHJHVlvUZIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ملت درحال تماشای درگیری تندروها و امنیتی‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/127737" target="_blank">📅 00:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127736">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">فرزند جمهوری اسلامی و جان فدای انقلاب
عبدالله محمدی ۸۰ ساله ۸۰ ساله ۸۰ ساله ۲۴ خرداد قم عزیز
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/127736" target="_blank">📅 23:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127735">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
شعار مرگ بر قالیشاه در میدان انقلاب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/127735" target="_blank">📅 23:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127734">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qsZT9NxDCiFFkFjyyypgsPgMMhgl6_YyNnr2cHFheXK74ZARO5Cvix1scrTLFa1O7pPs7XI-yi-T1CKewNNC8aUY1vNKv0mN1JveMNtgSymZB8VOP_-8B4IPp4oaXaZUFzGqrtqWF8qtvwJ8ly3FkVQxeqw0t3AQRz1uNhoee92IZ3_BIYMCHtpDrgTQWtGwq8ZB_ySitZiWUIXBM8SZI6KGpnrmvwRq3n6iEi1gnOlJT4vgjVsxRls8a8J4_cjHUsEd5vV6HfeJmT7YR__UpEMNqIY41E-S-i68wWtUiLm1kKLSnNvub3tQBdE8dn4uqBwr0Q-OtvAVUx7aacEYZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنر عجیب دیده شده در شلوغی‌های امشب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/127734" target="_blank">📅 23:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127733">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
گزارش‌ها از درگیری اغتشاشگران در قم با نیروهای جان برکف امنیتی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/127733" target="_blank">📅 23:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127732">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
کم مونده تندروها شعار:
لاحکم الا لله خوارج رو بدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/127732" target="_blank">📅 23:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127731">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
طبق گزارشات تعداد زیادی از مردم در گردان‌های امام علی ثبت نام کردند تا با اغتشاشات امشب مقابله کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/127731" target="_blank">📅 23:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127730">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdUkz53rVPEXexrwLH83QTdTpJQ3JXW0W0LlC26T8raLwDS2nl5MFC_pte0UpWgBYoCvCwnsJ9wpezli3AYDK8Ml9udWme_IzhVyQOpvFu_fJ37NlQWgI7vkye0QDm_PbqzXuKeNj1HxXJ_Iqjmu3eJEv-zhPwhUK7d1gwmbvuDqeKy9qA1x-AnsqOLBVqtyzOxzvhDzIE5nrY35wPgzw1DstxISOrlWLlI3rwli-oSTc_qZ-PGK_l4mDs7XR1GPwjKGBRPzYD1p1YSvZCrfYVSLpRGnFlG834iS8w6ltwsD9gqcePp5mDf01PkYdqGIdSOcFp06LBe7Zd54kKzA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: تصویری از دو لیدر شلوغی‌های امشب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/127730" target="_blank">📅 23:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127729">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تندروها
❌
بولشویک‌ها
✔️</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127729" target="_blank">📅 23:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127728">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
گزارش‌ها از اغتشاش تندروها در قم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/127728" target="_blank">📅 23:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127727">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
گزارش‌ها از اغتشاش تندروها در قم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/127727" target="_blank">📅 23:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127726">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
حجت‌الاسلام نبویان: با این توافق جمهوری اسلامی مستعمره امریکای کبیر خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/127726" target="_blank">📅 23:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127725">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
شعار تندروها در میدان انقلاب: نه اینوری نه اونوری جانم فدای رهبری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/127725" target="_blank">📅 23:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127724">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
شعار تندروها در میدان ابن سینا تهران: قالیشاه حیا کن ریاستو رها کن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/127724" target="_blank">📅 23:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127723">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سازمان ملل درمورد سرکوب اغتشاشات امشب تندروها ابراز نگرانی کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/127723" target="_blank">📅 23:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127722">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur7xPRpcRCkVURScksGeDTzKpFx_xqB8-T6XGUtyxDoZA0R5CnNCoHnlPGICBW5lwovR66jY0CJtsd7KZUHjvS5q0cCekVkt_5tkRs7LUlf_RGYk8ejX2UkD3KkqTNGXj71Q235dvLom8Xy8nIb8VXLIq_8WTNNhP2HGXBOyRBAOJgdbX8Bv_7GD9mlS_5HKNqKTDkPWcCilFoXI5VZcT3m-Qf82j4XtNxBokDsK-dS6F3md9M8_C5IEOkxc-BEmwFIBWn3CrN-Bo5vCtNMHuDUXetpNlqDQnLgif_vYj_Ci34UP1adFDU7ibJT_5Phq4fCgU9aEqbojSxFcUnHxXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این پست صرفا برای بازی با روح و روان تندروها است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/127722" target="_blank">📅 23:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/108f731480.mp4?token=dyudW1yIHmejFO8EjHFoT1q4czI6ktFl5CJQbRFpA0lnAh9D7DdR-LvDOXu-ekaLZU5P9RRiB36HRvirtuqDwyO1k1sb751mwc5uT6wMplhN5m2PhjY6Mnh8R7W0azN5c5Ej9O8aXCf6S5QotFhZel2Tybp7tIYvJ7FM0GYfY0KFe2fu4g8ToPsklcopcjCxs6yKET0pggEloW0yVdoKJ_Gi3TJTD8Yt5nqsYXGWMq_QEFfav8JiW4ps2StDb1p88Vaed58Hj5ChkwRfLcJiUA1Rqd8hg4R1-A2qlZlXTYV2tdASMWb80BFPG2aDasCc8v4yAZM_ejFe9B5SaFZcKB30uTanZmXhkqLak3smNiETEvmN7IaFtN0UK1UTROqpWpHf35nF8C8aN0OH5ytYAb_vAHDtYZOZtxQ8t5HPQ3jUdxWE1ltZTfN1bRyHbDHGBppoADiGUIjQVCAjOzCK48N9F5Na92rqyd_A8E55nD8TjPzp3C986rt369S0qCjLAP4prYItdQ6zABryK3B7yPqxXXWLEfYZBmUM2e28te6v9kQRYC4dqddfzkChblH-5Pr_0yFp6tf8NCYo0Sz3L1QOaRB3MxwlDXP9b4W5pS19F1wckX6BtJGA9r1u2LY5AgnAem_BW0Ipql94uWa3qtNHFHiERvaW8HANYXiPCi8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/108f731480.mp4?token=dyudW1yIHmejFO8EjHFoT1q4czI6ktFl5CJQbRFpA0lnAh9D7DdR-LvDOXu-ekaLZU5P9RRiB36HRvirtuqDwyO1k1sb751mwc5uT6wMplhN5m2PhjY6Mnh8R7W0azN5c5Ej9O8aXCf6S5QotFhZel2Tybp7tIYvJ7FM0GYfY0KFe2fu4g8ToPsklcopcjCxs6yKET0pggEloW0yVdoKJ_Gi3TJTD8Yt5nqsYXGWMq_QEFfav8JiW4ps2StDb1p88Vaed58Hj5ChkwRfLcJiUA1Rqd8hg4R1-A2qlZlXTYV2tdASMWb80BFPG2aDasCc8v4yAZM_ejFe9B5SaFZcKB30uTanZmXhkqLak3smNiETEvmN7IaFtN0UK1UTROqpWpHf35nF8C8aN0OH5ytYAb_vAHDtYZOZtxQ8t5HPQ3jUdxWE1ltZTfN1bRyHbDHGBppoADiGUIjQVCAjOzCK48N9F5Na92rqyd_A8E55nD8TjPzp3C986rt369S0qCjLAP4prYItdQ6zABryK3B7yPqxXXWLEfYZBmUM2e28te6v9kQRYC4dqddfzkChblH-5Pr_0yFp6tf8NCYo0Sz3L1QOaRB3MxwlDXP9b4W5pS19F1wckX6BtJGA9r1u2LY5AgnAem_BW0Ipql94uWa3qtNHFHiERvaW8HANYXiPCi8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا سیما: خیلی راحت می‌توانیم با بستن تنگه‌هرمز بازار انرژی را به تلاطم بکشیم/ مذاکره‌کنندگان هیچ‌ نگرانی در بحث انرژی نداشته باشند، ابزار و امتیاز دست ما است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/127721" target="_blank">📅 23:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127720">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
گزارش‌ها از اختلال در روبیکا و ایتا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/127720" target="_blank">📅 23:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127719">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ: کمک در راه است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/127719" target="_blank">📅 23:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127718">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ: کمک در راه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/127718" target="_blank">📅 23:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127717">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
گزارش‌ها از کتک خوردن اغتشاشگران در مشهد به دست نیروهای امنیتی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/127717" target="_blank">📅 23:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127716">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m38EreZnVINRvMLCAVP33hBF_t2DdcF1V7JvLJZPAvGfW_3dCQnAfuYeAhy2N79EyQUoi8dfYOlV0dEeHedpxdN1pxZ-0mACMCyX5273aUjLVnm5B-7osaU_lhpes19Y5CR9rRw91HI7LuljErBbNeYqHhjEaj0C_iqmOgUBSHXG8VzLq078m0FK-6eOrPHnGRiLT0rQZsUjqu0qT4kULugdGT3dec6CB4rHnKzjP1_Rg2MUlb7EFq0ABYK9i-DKIIPFjnQklrKE6tLhbp1fug0G-tTJCSqV-SaUV0Zbryp0RX2KNY0b8JtuL17-LZF68j2AbhzPCnP-nqCYtQCh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده در تجمع مخالفان توافق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/127716" target="_blank">📅 23:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P82aG4pEuX257qnD9fEE0CnzXi3Sn6Da1kT2RzDgAlNzYRPlj5iYdCNKSzL_36gnylk52muYlXENkyq2FSeM_V56Ph6f-luAVcK8qyZyQreWt0Pcdz9Llcv9B9zQCCymU65Sw0l-XYbaepXkZzTbes7BSdFQ04wd2ss4jNFwH4OMHPbTtmlF18834YQuxveLlO8yoZ94rVED3SPJP3WIePlFLBYVCzbtBHVTPcEVGxVt4EwRiLK2C-y19jq4n5k-tcuARfakmhTRmSYpT4bIHBrNNH4-F9i79Q6w70yxhUHBhrVSP7ofRpQ99LdfEDmgTEySiDRGKfIq_KSVNvmLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت رشیدی کوچی نماینده مجلس: تندروها به زباله دان تاریخ خواهند پیوست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/127715" target="_blank">📅 23:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127714">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
شبکه CNN به نقل از منابع اطلاعاتی: ایران ورودی‌های محل نگهداری از ذخایر اورانیوم خود را مین‌گذاری کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/127714" target="_blank">📅 23:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127713">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: مقامات ارشد اسرائیلی و کارشناسانی که سال‌ها در حوزه ایران فعالیت می‌کنند، امروز هشدار دادند که توافق فعلی بین آمریکا و ایران، عمیق‌ترین منافع امنیتی اسرائیل را به خطر می‌اندازد
🔴
مقامات ارشد اسرائیلی می‌گویند «ایرانی‌ها بی‌دلیل با این توافق موافقت نکرده‌اند، طرف آمریکایی شرایط اصلی آن‌ها را پذیرفته است.»
🔴
به گفته آنان، این توافق بلافاصله منجر به رفع محاصره دریایی و نجات ایران خواهد
🔴
اطرافیان نتانیاهو می‌گویند: «نگرانی بزرگ این است که ترامپ در بحث توافق با ایران، با ما همان کاری را بکند که اوباما کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/127713" target="_blank">📅 23:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127712">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQvYB6JZzaT-9VKNgYheHtMkNNd20w5fey4iVjMbpbl_tueBR85YVh7jReUkUK5_PQqKkLvNlZxzS-MUHAwXzISHMky57mLWzMAz1EnGoy3cXn3ZHXVeGscZ4rSzK_lsWIx5e75GRBuhaQicY5Xv0ta0qkShGDoDfphypZtX1hj4erZcy4x34-g4Zs4f-S2prZQu-DNgdfEAHg0Blq2CFx-kAGmQOqZXklc3zC1LURe2vQCLNoBzKNpGT_BAXHTz6z-UuPxQkHrmOHUgyhA7FfSZZg0y0Yi-fjMNa4T1yaOPXcNgWq6pgJjzrhb1njeKDe5WIgtPdK1EeBSi84k6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانالای ایتا:
قالیباف و پزشکیان، رهبری رو زندانی کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/127712" target="_blank">📅 23:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127711">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmIyt4HiF0JdzJbAAWMXZoGw3VmvDDdG4tizPiBivBrPIpuNSlH0Sm1w_mIzvnO7J_bw6l5HYOGFcUJOiKqzi28XbWIZLfg0sF9-KWPnA747E6beyLJTqk5F8MvJP5YbFJOzvPnQLX6DWgixjPFkK36QFzZnyIlZ1VA7UEo5RB0QsTEg27-y5_KnQA8bey-7_rw-UIFeFXfeH66EUs7qmCfiVgvZf5DAV_s_VLKiPDYDJaZnbm3_lIt0Vb72hplM4m7oaGScwozd_P2JsG7r4CLqcYY_dwz3iTlxcZUMLfz12zXke9W4bcb2aaJo9H_OCdfF-0QPjphqfL50j0jUpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دارایی اسرائیل، بزالل سموتریچ:
تنها راه: به ازای هر شلیک به سمت قلمرو ما، ده ساختمان در ضاحیه فرو خواهد ریخت. امشب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127711" target="_blank">📅 23:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127710">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed66484609.mp4?token=SUXfLFeYLmpKGLRxQHc0Dfug_FgUlOlkVrwZWpe_JyGutgmgSsMjJFVTgS388HxFcNVRfI9jrI8WZDBFlsVDMSwkaEFGYCd4hQiq2dJ-Flfilhw1NRdbofWltFxQICpRw9k60w1qkLLLQg6fuoAraVHZCEFrmDz45g4N2mTsd9RE1xzYBzslmtPrJ_WRy9DbSyKxjVsTjTloSAxFNBNuaKLUncBzslprm_DNcOlz2k9aMUSlapchwo5RVTpt5zaFWIrZ2psjEzmsB9d4i4vRL2CJWLoT_cF1fIs5PNAPEj5RdYhUPDX7pLC0Z-7uNBtoHdObtKP1yR1SYaZvBsCq_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed66484609.mp4?token=SUXfLFeYLmpKGLRxQHc0Dfug_FgUlOlkVrwZWpe_JyGutgmgSsMjJFVTgS388HxFcNVRfI9jrI8WZDBFlsVDMSwkaEFGYCd4hQiq2dJ-Flfilhw1NRdbofWltFxQICpRw9k60w1qkLLLQg6fuoAraVHZCEFrmDz45g4N2mTsd9RE1xzYBzslmtPrJ_WRy9DbSyKxjVsTjTloSAxFNBNuaKLUncBzslprm_DNcOlz2k9aMUSlapchwo5RVTpt5zaFWIrZ2psjEzmsB9d4i4vRL2CJWLoT_cF1fIs5PNAPEj5RdYhUPDX7pLC0Z-7uNBtoHdObtKP1yR1SYaZvBsCq_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اغتشاش مقابل ساختمان وزارت خارجه در تهران
: عراقچی حیا کن آمریکا را رها کن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/127710" target="_blank">📅 23:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127709">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmbCXba94zFXP1iIFJUep3ArvIEjXOEl_p-ps4fvR2LMtLa9p0uMLyGAEGcPTW2XHS2h9SEEd1MbjrovE_WnT9cNlpNAxERguBTHDPIlJ0JWOVv80onzzES05kV1YVjakmSY97Fy90Ob6dfoBwQ3lrcBTWnBuy1tGwgegqtmrZE_F4Vt5U11pO29EYqHLW5cTY3rqhdKh8H9YByYiMC8hIaJHNKwduZK-TGyaWgjZkBpxeaLQms8y5pkOPMfmvL_Q457RSPRN5vwUAaM23k5dD9pdPRnCqQqHbdCrxksD4iIIT95Tdkehcg6KF1etOf0jTFXzS_HrPSagauJDFajsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: فقط ترامپ!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/127709" target="_blank">📅 23:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127708">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ثابتی در اجتماع مخالفان توافق : پس از اظهارات شب گذشته عراقچی ، استیضاح عراقچی در سامانه مجلس ثبت خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127708" target="_blank">📅 22:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127707">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
کیان عبداللهی سردبیر تسنیم در شبکه خبر: مسئولیت متن و اجرا با تیم مذاکره‌کننده و دولت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/127707" target="_blank">📅 22:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127706">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
گروه‌های تندرو و افراطی اعلام کردن اگه مسئولین توافق کنن، انقد میان تو خیابون تا جمهوری اسلامی سرنگون بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/127706" target="_blank">📅 22:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127705">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
هم اکنون در تجمعات تندروها شعار عراقچی، قالیباف استعفا، استعفا!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/127705" target="_blank">📅 22:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127704">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a737b065cf.mp4?token=ueaQE3S5yGNaNONtPYVSnYTYoAnZxKt5NndNBjzT8DmCGbXIu2GY1o2Fu4zHY5Fkcgjb-NsgWOvY8_BtwoUMp-C8QmVzGNDlih8o8_taJXxW4RfClL7gMh15Sz90BT7CvQbqGnyeCCdq3sa94Js68nGo-uF7fEGJWwfqm1SOIhTlRuF26phVaqbobL-UF8Jzvw4JAfsfANiaoJelyUzgKu47l_ue_UiN5Em7EVfYQU-LZ-qO2tC-SCZb_uEcBZcEdZEnUMKerdfiluBR6FemlIHxVota2P2SWKiTPP63Fn9ZY5Knn6D9hhWDpkRNGnnKOVplPkCBrOi0vy9Awvqsaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a737b065cf.mp4?token=ueaQE3S5yGNaNONtPYVSnYTYoAnZxKt5NndNBjzT8DmCGbXIu2GY1o2Fu4zHY5Fkcgjb-NsgWOvY8_BtwoUMp-C8QmVzGNDlih8o8_taJXxW4RfClL7gMh15Sz90BT7CvQbqGnyeCCdq3sa94Js68nGo-uF7fEGJWwfqm1SOIhTlRuF26phVaqbobL-UF8Jzvw4JAfsfANiaoJelyUzgKu47l_ue_UiN5Em7EVfYQU-LZ-qO2tC-SCZb_uEcBZcEdZEnUMKerdfiluBR6FemlIHxVota2P2SWKiTPP63Fn9ZY5Knn6D9hhWDpkRNGnnKOVplPkCBrOi0vy9Awvqsaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون در تجمعات تندروها شعار عراقچی، قالیباف استعفا، استعفا!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/127704" target="_blank">📅 22:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127703">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBOw3f1d6b4EsWAnJRuu9kY6AH8ckqpBIi-a6LAeFz7p1S72pOWwXlMN73mE7tJdttwGr6YseqPUUYZr1fAKp4ikplPyV7B_jGqZ7kzyTtRqbb9UEgAbQi-dypm3A0GkSRXQGyJ7qExvXvruJbgYXkFzUoZlS_gHXpfNYpQrOrezq8L3vmKiblQF77IJy2FLqZeh_85_JriFuNcXk07NM6OySsT28SAd9lQoq4eE-NhusRQ960IZu6CRJ6-kA83Hdlb-iOJCbAaIkTUekSEZ9_WnnuIawJmDx7lET5gLuorq3vDugETMyxrKn-8_9Uvdvt4BnzO4Sv24AhNGfy5-NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قمار بازه؟ بچه بازه؟
کصکشه
؟
این ده شب رو میخواد امام حسینی باشه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/127703" target="_blank">📅 22:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127702">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
شبکه اسراییلی کان به نقل از منابع آگاه: ارتش برای توقف عملیات زمینی در لبنان به عنوان بخشی از توافقی که در حال شکل‌گیری میان واشنگتن و تهران است آماده می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/127702" target="_blank">📅 22:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127701">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
یه عمر می‌گفتیم چپ نفهمید ، ولی اینطور نیست.
🤔
چپ مستقیما از جمهوری اسلامی پول میگیره که اوپوزیسیون رو تخریب کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/127701" target="_blank">📅 22:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127700">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVNgoHcbY_NLCnDp9BoJZdYdlH2DT7VDEUStSDIXyyJ3nJsyobgUR5BMJCsNFSfCLuGlmfgzrVKyu0SlfQZDWnSvQbzpvJSd4F9mMctQoQlDPZ7FpwiQWuhKcrtKtqUwA_Oe9egvLqGTM16n0bwGhUn2XAfoQdt5NFSCBEFToJ_y_xbrBt5lwuGN9iW_QeyP4EZjaWL9459IcBNBa2NO27oqUyhlxMMOCZyCV9PUsdWrB4Xj4IJaFkyWQXVtKOKKUk5XK4cVpGVgSkjpDDWg_9p8f1B_-iG0VTH-j6BPoMxxdbucxG7WlxFKpH7X_Kr13pyEwP9RvUEKPrGgOEhRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیلی به شهر كفر جوز در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/127700" target="_blank">📅 22:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127699">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688218f580.mp4?token=FlMmgzf6MP6bjJmpJxiemA5oy3JwDskeC_XPIKPhB8thoiem5cOwf1P1v-RG1_oGvfB3BZBbKuFPVSw-tdGc3jK4odXFtUfKagTnRpnX0k07ugzBx4HoKUw78tC6nXjvB0f2ikRit4WgLIc6iqvdVdNR0miPLsRL1gk2Yg5HBInRusJ1gBPTw1Fx_BkB0S_dZppK-xeQOoB6oRYYBHExiHTan1uB23otnZYpgQZkMJYmpsEyukKVbHjlMYv7UqKwkMwCRcPquQheKMFNo0rBhMoYe80XtrR7UwBojS8fQpeo4Sizy23ur6bZKTO-QOgqOeqyvG9bC0sLkN-URTRkUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688218f580.mp4?token=FlMmgzf6MP6bjJmpJxiemA5oy3JwDskeC_XPIKPhB8thoiem5cOwf1P1v-RG1_oGvfB3BZBbKuFPVSw-tdGc3jK4odXFtUfKagTnRpnX0k07ugzBx4HoKUw78tC6nXjvB0f2ikRit4WgLIc6iqvdVdNR0miPLsRL1gk2Yg5HBInRusJ1gBPTw1Fx_BkB0S_dZppK-xeQOoB6oRYYBHExiHTan1uB23otnZYpgQZkMJYmpsEyukKVbHjlMYv7UqKwkMwCRcPquQheKMFNo0rBhMoYe80XtrR7UwBojS8fQpeo4Sizy23ur6bZKTO-QOgqOeqyvG9bC0sLkN-URTRkUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریستی نوام، نماینده ویژه ایالات متحده برای سپر آمریکا، می‌گوید که فکر می‌کند سپر آمریکا «قوی‌تر از ناتو» خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/127699" target="_blank">📅 22:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127698">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f489787669.mp4?token=DEs0jWg1U1znAS2vqI4HFEpr8vH2s5o4jPRg-EECnbd9caQxD3SS5YrYjOnQFyxiiC9dAmTlzB-Ke-Q-u6ui1MU6yavsgpFiAaXGBOll7AGg729j7bSP6QlzZZPE0q53dcllMJuxQBxxlkzpRZGlTbKTdkEKSPquX7WAoMXuV3a0VXGJ5QaRZiUKpUynMFHyPNouQuO8dlNA99HnnRDlgUd39-0z8I_5LjY_quIGaqg0WHqc6A0MvpqIF3zKuODKIcvQmhnI9X4A51Cw6M9ALtIr3Q5pluwaI0PNURbLNABBBUz3XJYfUrvgjphE8U2lxgvwL060cniSalcZxlbEmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f489787669.mp4?token=DEs0jWg1U1znAS2vqI4HFEpr8vH2s5o4jPRg-EECnbd9caQxD3SS5YrYjOnQFyxiiC9dAmTlzB-Ke-Q-u6ui1MU6yavsgpFiAaXGBOll7AGg729j7bSP6QlzZZPE0q53dcllMJuxQBxxlkzpRZGlTbKTdkEKSPquX7WAoMXuV3a0VXGJ5QaRZiUKpUynMFHyPNouQuO8dlNA99HnnRDlgUd39-0z8I_5LjY_quIGaqg0WHqc6A0MvpqIF3zKuODKIcvQmhnI9X4A51Cw6M9ALtIr3Q5pluwaI0PNURbLNABBBUz3XJYfUrvgjphE8U2lxgvwL060cniSalcZxlbEmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار مرگ بر قالیشاه در اغتشاشات میدان ابن سینا در تجمع پایداری‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/127698" target="_blank">📅 22:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127697">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
الجزیره به نقل از سازمان پخش اسرائیل: ارتش برای احتمال صدور دستور توقف پیشروی زمینی در جنوب لبنان از سوی فرماندهی سیاسی آماده می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/127697" target="_blank">📅 21:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127696">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مقام ارشد اسرائیلی به کانال ۱۲ اسرائیل: این یه توافق مزخرفه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/127696" target="_blank">📅 21:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127695">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نشست اضطراری کابینه امنیتی اسرائیل در پی آخرین تحولات ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127695" target="_blank">📅 21:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127694">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nte8qXIAIcF1KqV23mgiMi_2E6zaP3ZT4gcFCmL5vzB5iz0g5SJJMRbMak9g5atBIDJXcL6mBQvKRUc3ssFI3BGl4Ie_LHE3GTMAc-sJQh7m79WhG4e-4ipk9afT4AcKPN-CU7QHUfLvf3L0eOz6OqIxBE0tvOrJKdORIc3DC0oToiZoVOQgkw9OIk1BlfoCIigi_Y5DUP3yY45M0kAo_tRIyg1FG6Z5eVDkbm0iscEpSa7wuZNk6P5MhGOcwwJbeygv31G97HqrgVu-A1ZVMp_QYg2xs7DvUw_zKhCqeKF_zk7PreOL0q9JMpYJ-vWboZVuFL8YhJlmAeXH8mzfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ یه عکس از خودش و رهبرِ کره شمالی، کیم جونگ اون، پست کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/127694" target="_blank">📅 21:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127693">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سران کانادا و ایرلند: آتش بس در لبنان باید در توافق ایران و آمریکا لحاظ شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127693" target="_blank">📅 21:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127692">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
اسرائیل هیوم: اسرائیل ملزم به امضای توافق با ایران نخواهد بود و قادر به دفاع از خود است، اما رفتار آن باید با ایالات متحده هماهنگ شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/127692" target="_blank">📅 21:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127691">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
خبرگزاری فارس: ترامپ در تلاش است تا یادداشتی بین آمریکا و ایران روز یکشنبه امضا شود، هرچند مقامات ایرانی می‌گویند که توافق نهایی نشده و امضایی در کار نیست.
🔴
برخی معتقدند او می‌خواهد این اعلامیه با تولدش همزمان شود و آن را به یک پیروزی نمادین سیاسی تبدیل کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/127691" target="_blank">📅 21:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127690">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVbkzCI4W3r-laR9y4OudelrZkvHzPHmpL7GT-OuGLnOo3TlWDr5QcYMVkb7rgfLal5xc5pgrN9gcElhmqnUay6u-QCIvqDGYlGes-_3WBRb9JOiPbZJ1q8IGq3NbRK0TGw_Q1G97jrCJoeI_Zlz14zMSGEusMjpHqoC7yiKDkDmmvodY78YlvuKfJbqf0bswivrDMdkLtI5QwD5_atgUGDRqGYgokTnALzgevD6DzaijJd-5weJjpatpGanZyZfb4j3UN3tuMgeKpXFnVwPN0wXWnTTaukoYFsb32sMeMsIt2OyHgrTOp6X1zT5vFGUYNKacQbRfpyY22_YSF-WVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده اعلام کرد که کشتی‌های جنگی نیروی دریایی و دارایی‌های هوایی ایالات متحده همچنان در حمایت از محاصره علیه ایران گشت‌زنی می‌کنند و عملیات‌های مداوم را از سوی ناوچه یواس‌اس دلبرت دی. بلک (DDG‑119) در دریای عرب برجسته می‌سازند.
🔴
بر اساس گفته‌های فرماندهی مرکزی، تا تاریخ ۱۳ ژوئن، نیروهای ایالات متحده ۱۴۱ کشتی تجاری را به مسیرهای دیگر هدایت کرده و ۹ کشتی را غیرفعال کرده‌اند تا به رعایت محاصره اجبار شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127690" target="_blank">📅 21:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127689">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
کانال ۱۳ اسراییل: در اسرائیل اعتراف می‌کنند که میزان تأثیرگذاری بنیامین نتانیاهو بر توافقی که در حال حاضر میان ایران و ایالات متحده در حال شکل‌گیری است، بسیار محدود بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127689" target="_blank">📅 21:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127688">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/El66-b_89Y85MyEs5TeNcnbtTQ--F4Fk-GpIIQwMqKNHEOkPaEcS6tjmABIunL_L7dQ9JLgVQ36s_TR2iV9EfhqkMU3hn4_cFEL_0BlsW2mQ4-uE4K5HNzjkkLBNzwpYBiYZeP6CmKgdCmDFI05FgIc_F8Ryt2OHvshNSrd-8MRAuv9rPrgZj4Qm7uDx_b91skw1IR6_g62Lehq9uJxrFKxPd3jQBkkatYqrBJ1KVmxWGC8w9m2AfOJRv20GdlhmY4J0jd2QPAMgk92Wc9WwxrSwRHfVL3g4xSXSEnnkpioIZyFoSsN9So60ugLBlLnTY-KvwS-QywsDtZKZr38BLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: انتظار می‌رود ایالات متحده و ایران، با میانجیگری پاکستان و قطر، روز یکشنبه یک نشست مجازی برگزار کنند تا به صورت الکترونیکی تفاهم‌نامه‌ای را امضا کنند که آتش‌بس را به مدت ۶۰ روز تمدید می‌کند، تنگه هرمز را بازگشایی می‌کند و مذاکرات در مورد برنامه هسته‌ای ایران را آغاز می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/127688" target="_blank">📅 21:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127687">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
فرهنگستان ادب و زبان فارسی: از این به بعد به جای هدفون بگید گوشینه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127687" target="_blank">📅 21:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127685">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KHyUiWQ1SjXI6qggOFjFI7SQG2z77xawrgvcsdyqBXTQ7XWN0-Ou07fXyC2aR4QHaRkEWoBOoiFnTpCEPHJtgFwS1FmO59wFrR8T2febV-UoszKDYnAZzYscPSDbNdFrru0Br0ZBOTI2BK4rN4B3nkunVgVdIdqLYrIuqPLoB0yLIQNyusdX2RTpotcH3rH8btleG1tPxp8wyzDCKBa3YWSEJkfcHfkkKOmfmrFcsPyMrTEC6iF1qczAzSMywCha5lhBnJ72gRAVBBuAVlnbPbgaKrrHtzjlf5f0iImnUedIQBbJ068TxTbWx-3bOM5SWTb998GYag6M_GKWXrr4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cfKlAlC3XPXlyC9mh6jChiHFMKIYPwq8pHkyWhkPien5V3hlU4qBaBR49y_rXZQzalYg8lAsWxTMesqj0cFGYNwJUDcHqCCgORgFUOkNFoEV09vxHW2rBlKlQv9SMk9DAsAlk7LwWKUIoZdxLFMTHxujrzAqNdf7uP_yWNtRIWDOZTEpKA6rNLg8182vFSfkIFpgJr8s7IT27sWgO_PVpcWpozcePeiY3owulMD65JYLybn46N5fXDauYiKWqmSv1D8Gq6FCA7G6sj1Rxn12rGcRI2lk5V8k9T0PP5Y-vnawFW3fXpBrKjK8DLF9RVEOoPSy-xU-IDX2paipi1uVHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملهِ هوایی اسرائیل به شهرک
الزراریه
، جنوب لُبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127685" target="_blank">📅 21:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127684">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
صداوسیما : یه نفتکش غول‌پیکر از محاصره دریایی آمریکا، رد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127684" target="_blank">📅 21:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127683">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
فارس: با توجه به اینکه فردا تولد ترامپ است مسئولان ایران اجازه نخواهند داد توافق فردا امضا شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127683" target="_blank">📅 20:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127682">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ستاد فرماندهی مرکزی ایالات متحده: از زمان آغاز محاصره بنادر ایران، ۱۴۱ کشتی تجاری را منحرف و ۹ کشتی را از کار انداخته‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127682" target="_blank">📅 20:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127681">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
یک مقام ارشد آمریکایی: ایالات متحده همزمان با بازگشایی تنگه هرمز، محاصره دریایی خود علیه ایران را پایان خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127681" target="_blank">📅 20:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127680">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
دولت بریتانیا : کیر، به ترامپ گفته که لندن آماده‌ست از اجرای هر توافق صلحی با ایران حمایت کنه و کمکش کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127680" target="_blank">📅 20:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127677">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jR2NEUFn2iq8xZNjKxdiR11ND-cunsFAifBfji3eeKEqJsCs3Buu_wGVQeGGrDF0kjTfUFza3NjFL3fZEo-h3Kp5MFj1EsI6QpRMB7kHTkVU7mqhxYHA28OckNDO5dPbTpEzZ17wbmzMH--vRlVQ_Gx5YEpsV8wvXhXO7Q8NI6ssvpSPKQKeNzImT0SwqAh-XkWsKLslFOSSpLkxoj7weugw1yAQwtOqt1njffDct5okMYb56W2C3-Dvaz6llJV6tXNMeVH6F7aH7zH9z5joga9lXfehYHLyYJcNWI6rSyHaBlDw6JuKcA0-T9cm87d8XIX0W8xUDXRuFQeE1XPInw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
مردم میگن حاضریم آب و برق نباشه و نابود بشه اما مقاومت کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127677" target="_blank">📅 20:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127676">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ:  این توافق قرار است فردا امضا شود و بلافاصله پس از امضای آن، تنگه هرمز برای همه باز خواهد شد. روابط ما با ایران بسیار متفاوت و بهتر از دولت‌های قبلی است.
🔴
مشتاقانه منتظر همکاری با ایران و کل خاورمیانه در درازمدت هستیم.
🔴
در زمان مناسب، پس از آرام…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127676" target="_blank">📅 20:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127675">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDtdQx6eJiZJdBsFt-7K9SA3XAOLogUOSoqUUJ-RLnX4Ry86IsK7DYrnmBaBn4GGaG2srBelxFVn7WUm1-aA8_DJudPNwNzCHxlQmU25B_6v_yov3Vo-4zxYGG2pIttqzh0cKmwSCVW8UEIYCDn-_gD4agZ0AaSC6ucGqkGbFBeZ2m3Y_dDAedfRTptwUwVFrQ3MNnGDqyxt2DaVPdKDyR99J5_jyKltH3Zrp6h4fWGpufidzEzLMev7EcqHSJEf_iyNcYmY9LwWqojPHA8AS4YK1HatzSpACAuis53kBKr4-BJhgddTS-ErNwXMPlD8uCJ6iZoklK98xOF5-AdRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رنج منفی سنگین تتر پس اعلام ترامپ مبنی بر امضا توافق با ایران در روز یکشنبه
🔴
دلار فردایی نیز وارد کانال ۱۶۰ هزار تومان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127675" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127674">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ترامپ:  این توافق قرار است فردا امضا شود و بلافاصله پس از امضای آن، تنگه هرمز برای همه باز خواهد شد. روابط ما با ایران بسیار متفاوت و بهتر از دولت‌های قبلی است.
🔴
مشتاقانه منتظر همکاری با ایران و کل خاورمیانه در درازمدت هستیم.
🔴
در زمان مناسب، پس از آرام شدن اوضاع، برای جمع‌آوری غبار هسته‌ای وارد عمل خواهیم شد
🔴
ما امیدواریم که این روند سریع، آسان و روان پیش برود، و اگر این اتفاق نیفتد، ما جایگزین بی‌نقصی داریم.
🔴
توافق من با ایران دیواری است که مانع از دستیابی این کشور به هرگونه سلاح هسته‌ای می‌شود.
🔴
ایران دیگر سلاح هسته‌ای نمی‌خواهد و آن را چه از طریق خرید، چه توسعه یا هر طریق دیگری به دست نخواهد آورد.
🔴
هیچ پولی رد و بدل نخواهد شد، برخلاف صدها میلیاردی که اوباما به ایران پرداخت کرد.
🔴
ما تشعشعات هسته‌ای را چه در ایران و چه در ایالات متحده کاهش داده و از بین خواهیم برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127674" target="_blank">📅 20:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127673">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a7c7f1291.mp4?token=mcgjCd02Jq-oxSs71GM7R9FEB3Dj0CF5SmL-_KKfNbOQwNe8c_Xx2cWmBoL44a6n5QPEDCfyrx7Uu64GUaDlAbfSWwba5apGn2DggkL_2bXr8hUFC_g6qft2u7m5_aoa4duRu0vvfwUvG5WwxbxuQ5fPFTyxkd5rX1N6C79mK20OpxglhMv79D76jWup7JPT7GaVWCmn4OMmw5aR0ufqJW8lnZ5oH5nawKglOyzbnXeO2dAYfnYsZxIj9Z_tjhZh2HdUhoNjKCbgam5gPLxdB_r2XKpEwDIJYVXA5YaxowtlgiBhJdfC0F-aPY-6J7Ng-iadpX0Uy1oLipmNmGfw4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a7c7f1291.mp4?token=mcgjCd02Jq-oxSs71GM7R9FEB3Dj0CF5SmL-_KKfNbOQwNe8c_Xx2cWmBoL44a6n5QPEDCfyrx7Uu64GUaDlAbfSWwba5apGn2DggkL_2bXr8hUFC_g6qft2u7m5_aoa4duRu0vvfwUvG5WwxbxuQ5fPFTyxkd5rX1N6C79mK20OpxglhMv79D76jWup7JPT7GaVWCmn4OMmw5aR0ufqJW8lnZ5oH5nawKglOyzbnXeO2dAYfnYsZxIj9Z_tjhZh2HdUhoNjKCbgam5gPLxdB_r2XKpEwDIJYVXA5YaxowtlgiBhJdfC0F-aPY-6J7Ng-iadpX0Uy1oLipmNmGfw4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اغتشاش و شعار عجیب تندروها
🔴
مرگ بر عراقچی بی شرف نفوذی
🔴
مرگ بر قالیباف سازشگر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/127673" target="_blank">📅 20:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127672">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ: «توافق باراک حسین اوباما با ایران، یعنی برجام، جاده‌ای آسان و زیبا و هموار به سوی سلاح هسته‌ای بود که ایران شش سال پیش به آن می‌رسید و تا الان دیگر مدتها از آن استفاده می‌کرد.
🔴
اما توافق من با ایران دقیقاً برعکس است: یک دیوار محکم در برابر سلاح هسته‌ای!
🔴
در حقیقت، ایران دیگر سلاح هسته‌ای نمی‌خواهد و هرگز نخواهد داشت، چه از طریق خرید، چه تولید، و چه هر شکل دیگر تأمین.
🔴
امضای این توافق برای فردا برنامه‌ریزی شده
و بلافاصله پس از امضای آن، تنگه هرمز به روی همه باز است.
🔴
رابطه ما با ایران بسیار متفاوت و بهتر از دولت‌های قبلی است.
🔴
مشتاقانه منتظر همکاری با ایران و کل خاورمیانه در آینده‌ هستیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127672" target="_blank">📅 20:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127670">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری /  ترامپ: قرار است توافق با ایران فردا، یکشنبه، امضا شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127670" target="_blank">📅 20:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127669">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
تانکر ترکرز: یک نفتکش VLCC دیگر که تحت تحریم‌ها قرار دارد، با غیرفعال کردن سیگنال ردیابی AIS خود، از خط محاصره نیروی دریایی ایالات متحده عبور کرده است.
🔴
این کشتی با سابقه پنج سال تحریم‌های OFAC ایالات متحده، با تجارت نفت ایران و ونزوئلا مرتبط است و می‌تواند تقریباً دو میلیون بشکه نفت حمل کند.
🔴
این کشتی همچنین می‌تواند به عنوان ذخیره‌ساز شناور نفت مورد استفاده قرار گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127669" target="_blank">📅 20:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127668">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
یک خودرو در شهر کوثاریت السید، جنوب لبنان، هدف پهپاد اسرائیلی قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127668" target="_blank">📅 20:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127667">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEvtMvOAaZDcPLjP7Z8Cb_GjN6ie7L0AoeTmkG8WZHe4X7tNpJBXaTBNsXuiTbK9mb3mfwUAhR0Z5vqEdOQEqdU5Q0pGzKxEqV3nTfqx33kZ_aVi0jL-qu-kxX0MZeZd6dqNVRtvQsn6DsR49jMzGHaO7at_A7lXAq7NAAj_eriq24nXbkcx9xNgIn62t0aWuR5qDLQ9SndH-UD5bHg4xd4Gz-RLqPUkwZdu_hfcYwzCW8xrt10GgGsBYuopsVyQScnAxKARTt2xMybYrIhkS8fipnQRRHNAYi6bv9TdcXhSCrW_GNhoeRkXrXIv0spG1dFVcSdR_14dvyKPsBj3-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران از لحاظ آی کیو ۴ ام جهانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127667" target="_blank">📅 20:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127666">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
خواهر امیرحسین مقصودلو:
تتلو به علت انتشار آهنگ از زندان، ممنوع تماس شد و تا اطلاع ثانوی نمیتواند با کسی از بیرون زندان تماس برقرار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/127666" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127665">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
رئیس‌جمهور سوریه، الشرع درباره لُبنان
:
هنوز بعضیا دارن شایعه می‌سازن که سوریه داره تو لبنان دخالت می‌کنه
🔴
به نظر من این حرف‌ها کاملاً اشتباهه
🔴
ما همیشه از پایان جنگ، تقویت نهادهای دولتی، همکاری اقتصادی و آروم شدن اوضاع لُبنان تا حد ممکن حمایت می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127665" target="_blank">📅 20:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127664">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRkuKx3DedengGjiQD3gGKLdAb8jiwMwAZL4kTtQmwNfH2wk-6LyraGlj2EaKWVWqnlG4dk4j7DDYgugSfUZxOwTzugWiZ9ZttP2EnCFp_DRWfVxh1YB07X1LKUXJe8KizdmaLxmb5Cc1nAnTZUKl4qsy3nTUpBrbRGBjY3OZ0SEcwUxywz9db7Sugxxh0noh03XAfiPlEQsAGxhju5IR_iZRJZiFV6WB7PBmD3akFQRNydP_nhl95Ak8xUVfZ41sASmeiitmkdtB_HoTAbCqizsohWvghpdbVmp3VF3kugcR9FThlRENtStoWbJv6k_dmSpip4syFEZnU2lJBJCWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
70 حمله هوایی اسرائیل به نقاط مختلف نیمه جنوبی لبنان تا شرق این کشور در ساعات گذشته
🔴
بنا بر گزارش ها ارتش اسرائیل (IDF) اخیرا 10 فرمانده میدانی حزب‌الله را کشته و از آغاز جنگ اخیر بعد کشته شدن علی خامنه‌ای تاکنون بیش از 2100 عضو پیاده نظام حزب‌الله را نیز از بین برده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127664" target="_blank">📅 19:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127663">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
بانک‌های ملی، تجارت، صادرات و توسعه صادرات از جمله بانک‌هایی بودند که امروز به طور هم‌زمان در خدمات‌رسانی به مشتریان خود از طریق همراه بانک و بعضا ATMها دچار مشکل شدند.  ساعاتی بعد اطلاع داده شد وجوه پذیرندگان چهار بانک امشب به حساب‌های پشتیبان واریز می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127663" target="_blank">📅 19:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127662">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
بقائی، سخنگوی وزارت امور خارجه:
ایران در تنگه هرمز هزینه خدمات دریافت خواهد کرد
🔴
حضور پایگاه‌ها و نیروهای نظامی خارجی در منطقه باید به پایان برسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127662" target="_blank">📅 19:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127660">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ادعای شبکه الجزیره به نقل از سخنگوی وزارت خارجه پاکستان گزارش داد که مراسم «امضای الکترونیکی» توافق میان آمریکا و جمهوری اسلامی یکشنبه ۲۳ خرداد برگزار خواهد کرد. به گفته او، پاکستان میزبان این مراسم خواهد بود و مراسم از طریق «ارتباط ویدیویی و آنلاین» برگزار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127660" target="_blank">📅 19:22 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
