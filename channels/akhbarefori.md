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
<img src="https://cdn4.telesco.pe/file/DglKu2MKBPRGxrPo1lOlfAsttA1y2jDYXKZOTmWm1AyQMc6b-GU9AnS_IFJXz0jPoEJEA_xJp07d9YueqW_Fw-KuIKMeg3AGgd8xjSNAfR8imPqCYmQzVvrK9Ta2WrfcjWF-KdBDBQAllJbre9ibXT8iI7kjHSoCFdH79MNeygau35F3qWtddf3aJUfSVh-o1l4KsnRmtPEAkioBP9VMJEpCFUwG7yVQcKIvO5_w7eTykrVBlBRRZsvAJBstjg7RLOpyl4GBJE8M17Cr6tH4sXfPXo11USI_RVrZ8j9ZCl7FNoPH3VaQmbTaW401V272latSiU-OxC3tagkasKvMHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.12M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 22:35:44</div>
<hr>

<div class="tg-post" id="msg-682083">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZo4nAphHqDqAQjzfTGspIRkk1TGtagFObJElS1Mg6WOKMsVwdDl8ma829juFVZ6ifgQXki0eiDiiaitK33Mynphemt8spV6eS8WeGqrOstif4UOVNTYM99MnxWIseOWOc8YemJc914YfRl-KKeC4LtcJFXRJWIVQ8q1SbDUq5UxQ4_vsWtKd-gvOJOxC3ueWZLdhFBSCbE-4LMq8zSe3AcpDyPatj2U-vMgHQ8eR9KqM2uQ51VF_hhUzL0y5fy5-nie_uLhCLa59XBxfoXLhsFWAgXkpm_wV2AACbgDoY4kSSoAX0S0qE01c0K4hZi2GBFQmLib-_6mew8_8Z4j1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
خرید اعتباری آهن‌آلات با LC تا ۶ ماه
⚡️
مزایای خرید با LC از آهنگر:
* تأمین انواع آهن‌آلات موردنیاز پروژه
* امکان خرید اعتباری از طریق LC
* مناسب پروژه‌های ساختمانی، صنعتی و عمرانی
* تأمین از منابع معتبر بازار
* پشتیبانی از استعلام تا تأمین و تحویل بار
برای دریافت شرایط فروش LC، سقف اعتبار و استعلام قیمت وارد لینک زیر شوید و فرم را پر کنید.
🌐
ثبت درخواست</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/akhbarefori/682083" target="_blank">📅 22:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682082">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
بازار طلا حتی با جنگ هم سکه است
🔹
پیش از آغاز جنگ ایران، بازار طلا به‌طور متوسط ماهانه ۲.۸ درصد رشد کرده بود. در فاصله ۳۸ ماهه میان جنگ اوکراین و جنگ ایران نیز قیمت طلا تنها در ۱۰ ماه کاهش داشت.
🔹
این موضوع نشان می‌دهد که در این چند سال اقبال شدیدی به بازار طلا به وجود آمده است. این عطش البته ریشه‌ای عمیق‌تر دارد. سهم طلا از پرتفوی بازار جهانی که در سه‌ماهه چهارم ۲۰۰۰ حدود یک درصد بود، در سه‌ماهه نخست ۲۰۲۶ از ۶ درصد عبور کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/682082" target="_blank">📅 22:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682081">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
اصرار رئیس‌جمهور لبنان به مذاکرات بی‌حاصل با صهیونیست‌ها
🔹
«جوزف عون»، رئیس‌جمهور لبنان در دیدار با هیاتی از سازمان «تاسک فورس برای لبنان» به ریاست «ادوارد گابریل» تأکید کرد که بیروت علیرغم دشواری‌های کنونی به اجرای توافق چارچوب با رژیم صهیونیستی ادامه می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/akhbarefori/682081" target="_blank">📅 22:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682080">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1c0edcd3.mp4?token=Q6gLw6iHY80UGY29uLSWcw8CvigOPRNgh_LI_x2rEckQpYo7qXoY3xrd5XxECch0rjQYrh_sjVmr5o6sgB5JUqfmkWVfr3vaVSeUsa8eD7k8iLlmsE5vwoxGVkCidnjITzSgGN2ecgIOy-U5zCGvd1AOkMenP1eS_mYJlGpSW1-EhBaUiqsGjvb2kLcVRI2TLZIoEz14q7DrNNeneydlCR9Kom-s25zTDy9Su8Q4JdVUY8oSgbF9TzHw6BdRadUbT07mrLhZGxgadWdi7qk6W19Q92v95X9WSgAI5vFl3VYtBV4kwZfH8knM_ZLhL6MscH6DZIyC3bpV10rkYoh81Cct45AU222bNuIQc7sJacyXzL4a9cQWiL-FY44yItJWSpwr7iAjCL9-Rpg2Oj4oQqKsg_UZhFNab1m_LmKKJC8QY7qcQQYHTNFYxmzjBxsUhs47VBzjyFeDYES8Zmjrjxjl9v9AzUKHUR8_vrqEEq4WJ3zXOJhDICHT4ZVmoBiVWib0dFNizSqpAmriGQsispn-rBDyo2yYtVX-XnWz0Zm3XoA3mOTYEjxJK2YfL1rpWPNPR84gVyyUg14M19wYFs8_14upok3PuOEAeHqoTWUIdnQEd4pQYWiSnPIwv6-Y0xyDS63uAd5gA-neOCZyBW7AnTHNOilnZTtLNHSIgK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1c0edcd3.mp4?token=Q6gLw6iHY80UGY29uLSWcw8CvigOPRNgh_LI_x2rEckQpYo7qXoY3xrd5XxECch0rjQYrh_sjVmr5o6sgB5JUqfmkWVfr3vaVSeUsa8eD7k8iLlmsE5vwoxGVkCidnjITzSgGN2ecgIOy-U5zCGvd1AOkMenP1eS_mYJlGpSW1-EhBaUiqsGjvb2kLcVRI2TLZIoEz14q7DrNNeneydlCR9Kom-s25zTDy9Su8Q4JdVUY8oSgbF9TzHw6BdRadUbT07mrLhZGxgadWdi7qk6W19Q92v95X9WSgAI5vFl3VYtBV4kwZfH8knM_ZLhL6MscH6DZIyC3bpV10rkYoh81Cct45AU222bNuIQc7sJacyXzL4a9cQWiL-FY44yItJWSpwr7iAjCL9-Rpg2Oj4oQqKsg_UZhFNab1m_LmKKJC8QY7qcQQYHTNFYxmzjBxsUhs47VBzjyFeDYES8Zmjrjxjl9v9AzUKHUR8_vrqEEq4WJ3zXOJhDICHT4ZVmoBiVWib0dFNizSqpAmriGQsispn-rBDyo2yYtVX-XnWz0Zm3XoA3mOTYEjxJK2YfL1rpWPNPR84gVyyUg14M19wYFs8_14upok3PuOEAeHqoTWUIdnQEd4pQYWiSnPIwv6-Y0xyDS63uAd5gA-neOCZyBW7AnTHNOilnZTtLNHSIgK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سر اسرائیل در کدام آخور بند شده که در این جنگ نیست؟
🔹
اینکه اسرائیل در جنگ فعلی آمریکا با ایران حضور ندارد برای خیلی‌ها تعجب آور شده است. اما ماجرا پیچیده‌تر از این حرف‌هاست
🔹
در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/682080" target="_blank">📅 22:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682079">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n93ulAWEMrIberks_RzFtCTwxpCNDyGiaeiixlE7OrdSZLgxUecEVe608_l1wiOnPfMEJS2yeXWOSNSzUZMI7d-sEd36KvbTIsSQtTbtGbRDBFHR4bTFUuPRFMGmlVNbNiM-xy2-7MthN-cXCkrIGn0ekX38eu8CmDvWD5Eui5A3v739kWxSeR3NnzbcqY083lzvDPrbG-69v09RfY4PnwOD1E2of3IFxSxO7PLAYmSzseBXsmbCdoQnrYpk14sCBx8h3MNVENdbD5947TQUfMEhqytpjAlhZd4gP806DzuzfeBcSiba8wiA8z5x_i2YCErvyaUplL9ujMBix4UGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم در صدر عوامل گرانی مسکن
🔸
در این نظرسنجی بیش از ۳۸ هزار نفر شرکت کردند که سهم روبیکا ۵۵ درصد، بله ۲۷ درصد و تلگرام حدود ۱۸ درصد بوده است.
🔸
حدود ۲۹ درصد شرکت‌کنندگان، تورم و بیش از ۲۲ درصد، دلالی و سوداگری را مهم‌ترین عامل گرانی مسکن در ایران دانسته‌اند.
🔸
بررسی تحلیل‌های کارشناسان مسکن نیز نشان می‌دهد تورم، هزینه ساخت، قیمت زمین و سوداگری از مهم‌ترین عوامل گرانی مسکن در ایران‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/akhbarefori/682079" target="_blank">📅 22:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682078">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfhW9LpcZywzx0oXnmMhbffYnpjLsVNhRyuR8yCBApTa9Lfkpq2nlWdrFLQKZ79Ons1TszDdQIKiFelYXcu0ChQQ3x6zvt2lpSX9XzjDxiVzO4Vpto9SAYYsYyTcbdSVAaoxxiSpBOfRDmZirOfhjoe1M1bgktAuTQEzNzw5xD1uaOFY2n7TSVX9Yz_jLTGBllm-guwBeU2TmLzOLRQqYPBkg27RE1e2aQbBGTwEGoU2ZK08duilLFevRbKnoJjp6QSQ5ep_-Kv6DR14l74CgKp5QniXVt-UgDp6Ox1MHFHOxrL7ti3ewWlnbIvbhpdGhL6mlO_VBEEJ8dqs4dXX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از رهبر شهید انقلاب درحال قرائت قرآن کریم در کتابخانهٔ شخصی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/682078" target="_blank">📅 22:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682077">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
آتلانتیک: ترامپ، کره جنوبی را به خاطر جنگ ایران تنبیه می‌کند
آتلانتیک:
🔹
پس از جنگ ایران، ترامپ دستور کاهش رزمایش‌های مشترک آمریکا و کره جنوبی را صادر کرده است.
🔹
اقدامی که به گفته منتقدان، در واکنش به امتناع سئول از پیوستن به کارزار ایران انجام شده است. تحلیلگران این اقدام را نشانه‌ای از انتقال هزینه شکست‌های استراتژیک واشنگتن به متحدان می‌دانند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/akhbarefori/682077" target="_blank">📅 22:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682076">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMddgVAJbmycChOGPF26NyAc0TJ7l1XI12ZlX0P9yRGoehgs3zr3a5lkH6IBsmJ57EXWcG-5dkg0d0Qz9zUU9Qcy1A7USHuTjPmSITvxkIPiZlMTbt7PwEZ55Fm2xj57vXClHlXk9GjL-bvZwfgTAQzKBch10bqTsCiQxlMc8i5oqVHdTebRdgHW6ERd4Qk-ecWIaa9v3NEq9td72MSxc484s8ZF4wvF7FeU8h-orPR4x1d7b1KeldqI5oVMv0lnqbAo87KxkRRncIIeJQhk2GCzDHpCajQIhfBwHQ8wcNRIb06oNfDAcOxKu-LwNiDrabx4R4rKOrgI57xApxL9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار برای نخستین بار؛ تصاویری از رهبر انقلاب، امام سیدمجتبی خامنه‌ای، در عیادت از جانبازان انفجار پیجرهای لبنان
🔹
حضور در کنار کسانی که درد و رنج را با تمام وجود لمس کرده‌اند؛ دیداری سرشار از همدلی، آرامش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/682076" target="_blank">📅 22:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682075">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY_T-glZaWnycnrPyxyGoTeRCyB4cxyZMi_3DEb1Z-k_1NAIQKr0U8qbu5BeoKG3h3bdm9iW0qWgUWcTF7GMi2RI_VxFm0jFShM5aajHum57ZOuBv2ufhIgckL11WYH7gr7Qv0_51p9bQ3ej_r527C0CLiZBzvcyWFyoowsJzC1WTFlwe29o2Q26e8L_hP9_fS99P47K3e49RpuNl9v7fUd67fPKuL0gQj8bpU6IjEvZMhpVMleLY-_cVZx5ZF6HajVuMwC4verlXr09OTeOoMnEf2Vf58ZgWXrDX7GK1NeU5ul69-aP7FZLJOzGgWWmaHlzSRHg9RXsUag8JNL_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به عملیات پرچم دروغین در کردستان عراق؛ دوستان کرد ما، هوشیار باشند
🔹
هیچ چیزی حمله نابخردانه به دفتر نخست‌وزیر بارزانی را توجیه نمی‌کند. دوستان کرد ما باید در برابر ترفندهای پرچم دروغین که با هدف ایجاد اختلاف میان همسایگان طراحی می‌شوند، هوشیار باشند.
🔹
ما در برابر صدام و داعش از دوستان کرد خود حمایت کردیم و از امنیتی که آنها در مرز ما فراهم می‌کنند، سپاسگزاریم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/682075" target="_blank">📅 22:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682074">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22bf43f174.mp4?token=TZL4C3Nvyc7KPjjNxIukqbW1-fRlnsqY2yGtK5yX6Wfw6aeVW5E63BBiAwZd3hJJ5NjqpEo-GL0m3u4rAS0NvFG91hsbIv31QhQNjhmOxQDNqaFCjpKzZbxlCL4gL8YoCyR8BhvLvA_JyPky9HE13yy-zv1MAKLaaxCQIWnjLx6ocxIBp8taU3nRH4odz5EKHvlGCTT89YCiBIOfXbI4zR-W6UBtyiZlYyXjYedIa5Z4oZOvNP0JOUE5tuSdcmz35G0u15kZ-9YVz_vYV4dOULXnPccxFlPai0-xpFiu3zHtld9pYeSiHxZCEboY0f9IhflWB4wsKJ7w_U4BdX2J0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22bf43f174.mp4?token=TZL4C3Nvyc7KPjjNxIukqbW1-fRlnsqY2yGtK5yX6Wfw6aeVW5E63BBiAwZd3hJJ5NjqpEo-GL0m3u4rAS0NvFG91hsbIv31QhQNjhmOxQDNqaFCjpKzZbxlCL4gL8YoCyR8BhvLvA_JyPky9HE13yy-zv1MAKLaaxCQIWnjLx6ocxIBp8taU3nRH4odz5EKHvlGCTT89YCiBIOfXbI4zR-W6UBtyiZlYyXjYedIa5Z4oZOvNP0JOUE5tuSdcmz35G0u15kZ-9YVz_vYV4dOULXnPccxFlPai0-xpFiu3zHtld9pYeSiHxZCEboY0f9IhflWB4wsKJ7w_U4BdX2J0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار زیر میز ترامپ؛ سکانسی که پایانش همه را غافلگیر کرد
🔹
یک امضا، یک خودکار و یک انفجار مرگبار؛ همه‌چیز تمام شده به نظر می‌رسد. اما چند ثانیه بعد، مشخص می‌شود که ....
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/682074" target="_blank">📅 22:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682073">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmwNDM31rdfMjDsiK0-NKMowsoeI73-kaPOrPoH8mKiHOEoCNBNb7532o4AQib0H74cpZOeXDGdNke6m5j21WegvRVDZFSbOb1v-ltyrMc5fxQd3HgYuxRYrEeVjAkDCJJ5-oLrcxh58DGEi3VMudL7OGVb44X_tW4XufwzxIyByIFqFdwHzWmmI7gTWjhGZLRgZhU-uu8dqDCAAPB9nX2_fHpksW-GDPnBP-guS758M3MG0Ssp05LvpTW63AR0gZxN8oBBED3QGUYA2O8UoYehriX_dPDVnsByv0MEfKcjl3Dgy3eY4h6nd_YUa_Z-BsKNwQQ0VSnwUqHrQu5Vi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترس واقعی از خدا، آدم را سخت‌گیرتر نمی‌کند؛ مهربان‌تر و بخشنده‌تر می‌کند
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند کسی که از حساب و بازخواست الهی بیم دارد، در برابر لغزش دیگران زودتر راه عفو و گذشت را انتخاب می‌کند. بزرگیِ انسان فقط در قدرتش نیست؛ گاهی…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/682073" target="_blank">📅 22:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682072">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeVQB0_cDpVZ3NQLLfEgp9puENWnVa9D-SxYquE5UEab_Ih2T0MlxjjYwE8gsR7kDa7qivCSbvPRszYKmwEvIUIPqLEBLxiKgTRZiMuJjR7LCRlvbBGY5VPcNdMI9OQDO6NnMGCvkWyFT3pcuewKCvWMFUuQ9RS5f1zMFr95TyFH1Ik9YkLWsD4NdVnE4nk_su-DI5c4DQBlCV7Gwex93g1-bxpGUV6p3jvoPwEDKIPTGEanXBCBN4ouYm_JMMRG0IL44JJ-nZxTv36dfpzPZE5du1hPZu8jGqMxoQE8YzzcRp3Y1u4UIjL7VJYjYksywh5q2OCeNjKS98JjcVgcwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش‌بس هیچ
🔹
آتش‌بس ۶۰ روزه میان ایران و آمریکا در حالی به پایان خود نزدیک می‌شود که به دلیل بدعهدی‌ها و اقدامات آمریکا، از همان ابتدا نیز چندان شبیه یک آتش‌بس واقعی نبود. در طول این مدت، موارد مختلفی از نقض تعهدات و افزایش فشارها مطرح شد و همین مسئله، آتش‌بس را کاملا بی‌معنی کرد. اکنون برخی رسانه‌ها از احتمال تمدید شدن این آتش‌بس هیچ خبر می‌دهند، آتش‌بسی که در صورت تمدید احتمالا بازهم هیچ خواهد بود.
🔹
هشتصدوسی‌‌وششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/682072" target="_blank">📅 21:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682071">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0b0d45dd.mp4?token=Farpun-sCkgU8AF_Q-teqZyfvXPQIIO0rzXpfSEoZ1GNhRIMtY3tgGJcEF9icHF1w9ife8gTdufBNv92YMAGYxGv9hNcY2OoaXwC-yzvL6cnkAxo60b8lq_cK525G1JpqpDaQIXeFO_RpBlLBTyAJeht9wYKU8d9WbqERKeAuAxsdt1I_-cfhKkuzUvmTUK81VEPrTxVpMNKe5sayQt2OAnnuf2N5aX0wp_xkRO17e7KJQz5AlkbV6WIjBEM3m8KDqJqDv3BxwRsxPKYQQyBXcayWoieYWikDogorF-HaRL29FCzSxvZ41nHXp3aGxNFE6TeW395XqGqQbRKjZrekg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0b0d45dd.mp4?token=Farpun-sCkgU8AF_Q-teqZyfvXPQIIO0rzXpfSEoZ1GNhRIMtY3tgGJcEF9icHF1w9ife8gTdufBNv92YMAGYxGv9hNcY2OoaXwC-yzvL6cnkAxo60b8lq_cK525G1JpqpDaQIXeFO_RpBlLBTyAJeht9wYKU8d9WbqERKeAuAxsdt1I_-cfhKkuzUvmTUK81VEPrTxVpMNKe5sayQt2OAnnuf2N5aX0wp_xkRO17e7KJQz5AlkbV6WIjBEM3m8KDqJqDv3BxwRsxPKYQQyBXcayWoieYWikDogorF-HaRL29FCzSxvZ41nHXp3aGxNFE6TeW395XqGqQbRKjZrekg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ قمارباز درباره ایران: ایران در وضعیت بسیار وخیمی قرار دارد. کشورشان در هرج و مرج است
🔹
نیروی نظامی آن‌ها کاملاً شکست خورده است.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/682071" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682070">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d24fe61119.mp4?token=mGjVZItnmN5EMGrm65p_lo2mbgAWoHEeanTan4Aw4MPULJfyQ2bFOg9lYV53YUtflPnhUarJdSVk3e9eJYEiIxt0HelgcJbYxVp-awcqsPzZ084BBYkrs2uTtElQ9YTRcaqy5wOQ0y9L3IsqjTVbCt0ggTDmvpDVFO7QIRRiQyyJeqpIvkwSSIS9lSgTo1wF4PGcBmp-MpXUK2LgZuoKlkiHrha-9D2SBA3gtetb9o011D0L4cHuQS7UJ61cxJNN0oVmuRyjSnUkxvvAnqsDMKwniHt9x50WW_CD8CyCtUVGShZaoDPKIdBItpQmsh6fu9KBkdAMfQH6cwnxhCxAYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d24fe61119.mp4?token=mGjVZItnmN5EMGrm65p_lo2mbgAWoHEeanTan4Aw4MPULJfyQ2bFOg9lYV53YUtflPnhUarJdSVk3e9eJYEiIxt0HelgcJbYxVp-awcqsPzZ084BBYkrs2uTtElQ9YTRcaqy5wOQ0y9L3IsqjTVbCt0ggTDmvpDVFO7QIRRiQyyJeqpIvkwSSIS9lSgTo1wF4PGcBmp-MpXUK2LgZuoKlkiHrha-9D2SBA3gtetb9o011D0L4cHuQS7UJ61cxJNN0oVmuRyjSnUkxvvAnqsDMKwniHt9x50WW_CD8CyCtUVGShZaoDPKIdBItpQmsh6fu9KBkdAMfQH6cwnxhCxAYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دروغگو مدعی شد که ایالات متحده به دنبال تمدید توافق‌نامه همکاری با ایران نیست
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/682070" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682069">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b4c402d2c.mp4?token=b1I54xO78Zkwj7NnAbaOXh8HdAbYIsDRdSGRmiQfhPX4uonszweVffleQg8saCo_rAs1A7DZVZCvKjceGBMferlokbNd2yBuJWP5QqSKcmX-l7Zq505fuyuMwnKdpL-0YanBf8VaQl7yoOV9OYsMcQLrd6ZWpkNz2Tgk3hmOnbDPuWjZ598Z6TaTrd18wGSJ7sIBrUOg3wY1WrGoV3nXwhAgGs3wZOes4gaqaLdZJewCdII9XkkwIRuE_Nvz-hnUJ1NbiEBlQfIKOCcfJ0u3HwgKcK2a2mfE7hpcoOmHLTh8usfWHq1u3ykOyuIyarn3QjFY04098XtaE9itbiMd3qzQC3fCAyfMmWLltQeBmZf5mClfM-HSJVsIWbUHH5VPqyk5tVzV1TtoZqZeZELWmt30ph_vUXzcB2CG_xJFhoNZxwvAE3iBlE9bOIDuRwY2wBwwJNPj7-fIXucneBQfGuN2zQbEiuT_Rr0LvTAPfMflaWHMDjXgZSYkcjL8IOswtMrUrE6RIxSTO3gKPxeexoikgD-wnmmXgZGkYSlJ9GYAI0Vh9yuHEWuYlkPzP0NzM4s7FAK1sbmY3ZG8B3qpqew4JJiiR_KkNcP9p1sYXwzUGBNhijrLuKDOJIvNQ9l9UI81qQolcmBiecGH4mmxiUok3sR4HAt9amGnpN7ufg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b4c402d2c.mp4?token=b1I54xO78Zkwj7NnAbaOXh8HdAbYIsDRdSGRmiQfhPX4uonszweVffleQg8saCo_rAs1A7DZVZCvKjceGBMferlokbNd2yBuJWP5QqSKcmX-l7Zq505fuyuMwnKdpL-0YanBf8VaQl7yoOV9OYsMcQLrd6ZWpkNz2Tgk3hmOnbDPuWjZ598Z6TaTrd18wGSJ7sIBrUOg3wY1WrGoV3nXwhAgGs3wZOes4gaqaLdZJewCdII9XkkwIRuE_Nvz-hnUJ1NbiEBlQfIKOCcfJ0u3HwgKcK2a2mfE7hpcoOmHLTh8usfWHq1u3ykOyuIyarn3QjFY04098XtaE9itbiMd3qzQC3fCAyfMmWLltQeBmZf5mClfM-HSJVsIWbUHH5VPqyk5tVzV1TtoZqZeZELWmt30ph_vUXzcB2CG_xJFhoNZxwvAE3iBlE9bOIDuRwY2wBwwJNPj7-fIXucneBQfGuN2zQbEiuT_Rr0LvTAPfMflaWHMDjXgZSYkcjL8IOswtMrUrE6RIxSTO3gKPxeexoikgD-wnmmXgZGkYSlJ9GYAI0Vh9yuHEWuYlkPzP0NzM4s7FAK1sbmY3ZG8B3qpqew4JJiiR_KkNcP9p1sYXwzUGBNhijrLuKDOJIvNQ9l9UI81qQolcmBiecGH4mmxiUok3sR4HAt9amGnpN7ufg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ دیوانه درباره ایران: من ایده اعلام کردن تنگه هرمز به عنوان یک منطقه متعلق به ایالات متحده را دوست دارم
🔹
ما کنترل کامل بر این تنگه را در اختیار داریم.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/682069" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682068">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933209adaa.mp4?token=eyk9NGDuyWIo3mPMYFgDPS1C7k5npDoSBogkz5WUuPpOyj2LPonZL_R7MbwCSI5xjcgH55m-j9JsORwJIXApUv-8YexSisDCKLggiaEmOuj2Ua5z0YrE7zJGekVXqbQ2Zcp21t_GybOe0uqajk-t20ILeLOnFBhzizGIDYAQC8XMBFLGs9zO4HyMTpqVTNiljqbPpzxpf-NOZet3U6gbyrg8Hq5faPEo766B0JpzDfKqbNl8jfgP_pgjERMPj_j5ZPvLDq90sA1kPHdS06K2NJ3tMQaXpePAUFvluuJohLA1Ik7zhuGjRw47bzcvz5qgtAbXomM6rT9MYq8Km4BzsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933209adaa.mp4?token=eyk9NGDuyWIo3mPMYFgDPS1C7k5npDoSBogkz5WUuPpOyj2LPonZL_R7MbwCSI5xjcgH55m-j9JsORwJIXApUv-8YexSisDCKLggiaEmOuj2Ua5z0YrE7zJGekVXqbQ2Zcp21t_GybOe0uqajk-t20ILeLOnFBhzizGIDYAQC8XMBFLGs9zO4HyMTpqVTNiljqbPpzxpf-NOZet3U6gbyrg8Hq5faPEo766B0JpzDfKqbNl8jfgP_pgjERMPj_j5ZPvLDq90sA1kPHdS06K2NJ3tMQaXpePAUFvluuJohLA1Ik7zhuGjRw47bzcvz5qgtAbXomM6rT9MYq8Km4BzsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: افرادی که با این طرح ساخت سالن رقص مخالفت می‌کنند، به نظر من، بسیار غیروفادار به کشور ما هستند
🔹
بسیار، بسیار غیروفادار به کشور ما.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/682068" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682067">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dbd66f94a.mp4?token=bXcB9GAGhegz2nFMHAi6EwRxrEOMRvJZMC474-6sVdQ2ROhH9rsOWSi0zjQnC7eC69RKvgf3Oo9UZOjx0B0YfNB8rA83_mYwjpz_Lr809XfmH3gJcy0htwSOpV_gbSF9TPUn2IBR5IOIkgJS9WP8se9Qp7xo_3ZIgPhKMBtF7WXBulWfl1JG680E2WAT4ljNJTO3jVIVzDRz0ii5HlpYuZhBHawXluGPDrX0OE8Gx4NDfFSpMKUVZRJVy1i1sZa7dD0X_cHRmNQez-p7SctmPQktMf33ivgq07h-ujiVGpvvZg24yLaJMvwD_o7BiPnbSuv1t9YTjDK5u5DUlv-5WYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dbd66f94a.mp4?token=bXcB9GAGhegz2nFMHAi6EwRxrEOMRvJZMC474-6sVdQ2ROhH9rsOWSi0zjQnC7eC69RKvgf3Oo9UZOjx0B0YfNB8rA83_mYwjpz_Lr809XfmH3gJcy0htwSOpV_gbSF9TPUn2IBR5IOIkgJS9WP8se9Qp7xo_3ZIgPhKMBtF7WXBulWfl1JG680E2WAT4ljNJTO3jVIVzDRz0ii5HlpYuZhBHawXluGPDrX0OE8Gx4NDfFSpMKUVZRJVy1i1sZa7dD0X_cHRmNQez-p7SctmPQktMf33ivgq07h-ujiVGpvvZg24yLaJMvwD_o7BiPnbSuv1t9YTjDK5u5DUlv-5WYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دیوانه: ساکت، ساکت، ساکت. شما بسیار بی‌احترامی می‌کنید. ساکت باشید. شما با چه کسی هستید؟
🔹
گزارشگر: من از شبکه CNN هستم.
🔹
ترامپ: شما خبرهای دروغین منتشر می‌کنید. ساکت باشید، ساکت باشید، ساکت باشید. شما یک گزارشگر دروغگو هستید.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/682067" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682066">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76bf98717.mp4?token=DxuaJ4o6ancB3yiDFb_Kb3vuMFcz27zhN1FhjKVwH_7Hyqp2P684Hqdd_8Y-xV5_njFllS5RXDZmJbRrw9ddBhASLFeA5PpCH8adjfbNoip-bj3jdRIa3hMPEFgcGRWmlOpSZInZ-a1crnOm05OKXy9mSgYgqGxfAbUhcLenW7MIoFmaEfldjAInJDw1-Zs9xdCZwdSwfABwvDR4oveKc6Kdud0kt7C1Y0-79XBTiv9oxTPRATsMg9_LyHcIUK0ECwafurEExdoSDvGMgX_e4M6yILa1KTIkkkOg6SccLTNjCNOF2myuPzEE4C4QSeaBIlexYkqhgDCuHsyYTsEApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76bf98717.mp4?token=DxuaJ4o6ancB3yiDFb_Kb3vuMFcz27zhN1FhjKVwH_7Hyqp2P684Hqdd_8Y-xV5_njFllS5RXDZmJbRrw9ddBhASLFeA5PpCH8adjfbNoip-bj3jdRIa3hMPEFgcGRWmlOpSZInZ-a1crnOm05OKXy9mSgYgqGxfAbUhcLenW7MIoFmaEfldjAInJDw1-Zs9xdCZwdSwfABwvDR4oveKc6Kdud0kt7C1Y0-79XBTiv9oxTPRATsMg9_LyHcIUK0ECwafurEExdoSDvGMgX_e4M6yILa1KTIkkkOg6SccLTNjCNOF2myuPzEE4C4QSeaBIlexYkqhgDCuHsyYTsEApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
ترامپ جنایتکار درباره ایران: ما هر هفته میلیون ها بشکه نفت استخراج می کنیم
🔹
تنگه باز است، قیمت نفت در حال کاهش است و به کاهش خود ادامه خواهد داد مگر اینکه تصمیم بگیریم کاری افراطی تر از آنچه در حال حاضر انجام می دهیم انجام دهیم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/682066" target="_blank">📅 21:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682065">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ادعای ترامپ کودک‌کش: با رئیس جمهور کره جنوبی تماس گرفتم. من به او گفتم: «در مسئله ایران به ما کمک می‌کنی؟ اگر بخواهی، نیازی به کمک نداریم». او پاسخ داد: نه، متشکرم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/682065" target="_blank">📅 21:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682064">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: ایران نمی‌تواند به سلاح هسته‌ای دست یابد و هرگز صاحب آن نخواهد شد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/682064" target="_blank">📅 21:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682063">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e021862a.mp4?token=PwjVbWun9qYT_KUwFQbsQxq_GJrOqxLGo_fM8tQgQYSs_iX-AyAsDMWZ_np7QfcgLuIFg5VIU_ibXUG_k-RQh4pqk1T2OxnuCme40NqYADpuPyzUpGTKTrChhx6flNGLTVrG5ALPT9HMbRr1xT2JgoQCVp2GBmL28mRA9FdYZ4QfvnYFz38OIhEh5g3FDz5_yHNaxwu-OaJb3p2E4rL0o_6ExSLhpZPXvMq3wVIv9AWYw7E83KFq-BE4D2EgLzBeEGh0KeVuguQe-3UgMrn7GG3QuGzrIe-3DJgNZSTdKhv2v3-ynaJbLZrA-N5eN6Q1wueR43UMYHLKHuJLAK2JoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e021862a.mp4?token=PwjVbWun9qYT_KUwFQbsQxq_GJrOqxLGo_fM8tQgQYSs_iX-AyAsDMWZ_np7QfcgLuIFg5VIU_ibXUG_k-RQh4pqk1T2OxnuCme40NqYADpuPyzUpGTKTrChhx6flNGLTVrG5ALPT9HMbRr1xT2JgoQCVp2GBmL28mRA9FdYZ4QfvnYFz38OIhEh5g3FDz5_yHNaxwu-OaJb3p2E4rL0o_6ExSLhpZPXvMq3wVIv9AWYw7E83KFq-BE4D2EgLzBeEGh0KeVuguQe-3UgMrn7GG3QuGzrIe-3DJgNZSTdKhv2v3-ynaJbLZrA-N5eN6Q1wueR43UMYHLKHuJLAK2JoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در اطراف میدان شهرداری گرگان
🔹
چند باب از مغازه‌های اطراف میدان شهرداری گرگان از حوالی ساعت ۱۹ و ۱۵ دقیقه امروز دچار آتش‌سوزی شده است.  #اخبار_گلستان در فضای مجازی
👇
@AkhbareGolestan</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/682063" target="_blank">📅 21:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682062">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKMC</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEjJQ7iUqGXSjpXMxtczznsasfvr3EgBrGj3br6JrYhc-R1TKfZrCd341hC36srZcvWuRd2P_fJ9Nj6B7dLnFJgffHh1peh8GVsOpV6B31NdH8G74EwSOjTUReBsBtxAlzYSpXxRJFBLanJczwdALo4IxVgGYPQmsPwNvxqXaOuqaZLzb2oO5_Ypr0VcMUdA5NkW3yi9YuzKLdHYZbhsS4KLa_eNXboLRoP1G6m6fDAH3UtL2Busd_8q6fSw30xIGa56M8fGrW_O2Z_J69boW5c35-derjqib89jadXXf1EPvmiUV9YmqyH4na5eu-Be92I-tXkxCOuC8DwONFPM1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
شرایط فروش کی ام سی اس ایگل(KMC EAGLE )
▫️
قیمت: ۲،۴۸۲،۵۰۰،۰۰۰ تومان
▫️
پیش پرداخت: ۱،۵۰۰،۰۰۰،۰۰۰ تومان
مشاهده شرایط فروش</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/682062" target="_blank">📅 21:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682061">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای
ترامپ قمارباز: ایران نمی‌تواند به سلاح هسته‌ای دست یابد و هرگز صاحب آن نخواهد شد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/682061" target="_blank">📅 21:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682060">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
عضو سنا: ترامپ روی توالت طلایی می‌نشست و نمی‌داند سختی چیست
🔹
مارک کلی روز دوشنبه اظهارات ترامپ درباره ناو آبراهام لینکلن را «غیرقابل قبول» دانست.
🔹
او در مصاحبه با ام‌اس‌نَو گفت که رئیس‌جمهور آمریکا بخش قابل‌توجهی از دوران بزرگسالی خود را «روی توالت‌های طلایی» نشسته است و معنای سختی کشیدن را نمی‌داند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/682060" target="_blank">📅 21:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682059">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d187a30294.mp4?token=LPyiMFWUm424VYkDWr79sWFZWP6zHutht8UaA9U9TsWG2Ldm7qn9e-1Ys5-lX0BsUtQfWejLQ38HYGzJYUHKGdgoXDyHEqqnKTaIIdHXPyfRXJ40n2gwrHramZCHUmgzycc63alG_PWkCD4eXXVCChRiHnfl5Mmabb3x5oaVeCai0ftIp1R8aa8L8jmkba1QKQHUOvuu6_s8uFHeLK0Ps_RoggotA8HFSm6zLJrC40s5oteRcZ5evtLEG6PzJ5TPx2SFxEyZo7w0-l8WmoVwwStIqZN51FGpUwhEDc4dS429g6C4_vp72oeFAQeIfRf24h0NBXqbN6NYylVNOmkIQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d187a30294.mp4?token=LPyiMFWUm424VYkDWr79sWFZWP6zHutht8UaA9U9TsWG2Ldm7qn9e-1Ys5-lX0BsUtQfWejLQ38HYGzJYUHKGdgoXDyHEqqnKTaIIdHXPyfRXJ40n2gwrHramZCHUmgzycc63alG_PWkCD4eXXVCChRiHnfl5Mmabb3x5oaVeCai0ftIp1R8aa8L8jmkba1QKQHUOvuu6_s8uFHeLK0Ps_RoggotA8HFSm6zLJrC40s5oteRcZ5evtLEG6PzJ5TPx2SFxEyZo7w0-l8WmoVwwStIqZN51FGpUwhEDc4dS429g6C4_vp72oeFAQeIfRf24h0NBXqbN6NYylVNOmkIQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از تصادف عجیب در اتوبان بابایی تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/682059" target="_blank">📅 21:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682058">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
خبرنگار: شما گفته بودید اگر عمان در مسیر بازگشایی تنگه هرمز مانع‌تراشی کند، «حسابی آنجا را بمباران خواهید کرد». آیا می‌گویید دیگر صبرتان در قبال عمان، که یک شریک راهبردی است، به پایان رسیده است؟
ترامپ:
🔹
فکر نمی‌کنم آنها رفتار خیلی خوبی کرده باشند، اما ما به‌راحتی از پس آنها برمی‌آمدیم؛ درست همان‌طور که با مسائل دیگر برخورد می‌کنیم.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/682058" target="_blank">📅 21:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682057">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای وزیر انرژی آمریکا: با وجود کاهش تردد در تنگه هرمز، به انتقال نفت و گاز از این مسیر ادامه می‌دهیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/682057" target="_blank">📅 21:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682054">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
صادرات محموله‌های پسته خام با پوست به مقصد ترکیه تا زمان دریافت شرایط قرنطینه‌ای از این کشور، متوقف شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/682054" target="_blank">📅 21:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682053">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
پروژه تخریب در ایران اینترنشنال؛ چرا باشگاه خیبر هدف قرار گرفته است؟
در ادامه موج رسانه‌ای علیه چهره‌ها و مجموعه‌هایی که مواضع و فعالیت‌هایشان در حمایت از جمهوری اسلامی ایران و منافع کشور تعریف شده، این‌بار نام مسعود عبدی، مالک باشگاه خیبر خرم‌آباد و مدیر مجموعه آرین سازه، در گزارش‌های شبکه ایران اینترنشنال برجسته شده است؛ گزارشی که با بازنشر تصاویری مربوط به اعتراضات سال گذشته درباره پروژه «ستین»، تلاش دارد تصویری منفی از فعالیت‌های اقتصادی عبدی ارائه کند.
اما مرور سوابق فعالیت‌ها و بررسی روند اجرایی پروژه‌های این مجموعه، روایت متفاوتی را نشان می‌دهد؛ پروژه‌هایی که بخشی از آنها به بهره‌برداری رسیده و برخی دیگر همچنان در حال اجرا هستند.
آرین سازه طی سال‌های گذشته پروژه‌های متعددی را در تهران اجرا کرده که از جمله آنها می‌توان به پروژه «آبشار» اشاره کرد؛ مجموعه‌ای متشکل از دو برج مسکونی با ۲۷۴ واحد که هم‌اکنون ساکنان آن در این پروژه زندگی می‌کنند. پروژه تجاری ـ اداری «یاس ۳» نیز از دیگر پروژه‌های این مجموعه است.
در کنار پروژه‌های به بهره‌برداری رسیده، پروژه پدافند ارتش نیز از جمله طرح‌های در دست اجرای آرین سازه است که بر اساس برنامه‌ریزی‌های انجام‌شده، طی دو تا سه سال آینده آماده خواهد شد.
پروژه «ستین»؛ روایت حاشیه‌ها یا واقعیت حقوقی؟
پروژه «ستین» طی سال‌های گذشته با حواشی و اختلافاتی همراه بوده است. بر اساس توضیحات ارائه‌شده از سوی آرین سازه، زمین پروژه از سوی این شرکت خریداری شد و هنگام انعقاد قرارداد، واگذاری زمین همراه با مجوز عنوان شده بود؛ اما پس از گذشت حدود دو سال مشخص شد که امکان دریافت مجوز مطابق آنچه در ابتدا مطرح شده بود، وجود ندارد.
در ادامه، آرین سازه شخصاً فرآیند دریافت مجوزهای لازم را دنبال کرد و در نهایت موفق به اخذ مجوز شد. پس از دریافت مجوز نیز عملیات اجرایی پروژه با اجرای فونداسیون آغاز شد و پروژه وارد مرحله عملیاتی شد.
با این حال، شبکه صهیونیستی اینترنشنال در گزارش خود تصاویری از اعتراضات مربوط به این پروژه را بازنشر کرده که مربوط به سال گذشته است؛ تصاویری که اکنون و در شرایطی متفاوت، بار دیگر در یک گزارش رسانه‌ای مورد استفاده قرار گرفته‌اند.
از سوی دیگر، در جریان اختلافات شکل‌گرفته، شکایت‌هایی نیز علیه شرکت آرین سازه و مسعود عبدی مطرح شد که بنا بر مستندات ارائه‌شده از سوی این مجموعه، پس از ارائه مدارک و مستندات، با صدور آرای قضایی به نفع آرین سازه به پایان رسیده است.
عبدی؛ از فعالیت اقتصادی تا حضور آشکار در فضای ملی
اما آنچه این گزارش را از یک پرونده صرفاً اقتصادی فراتر می‌برد، سابقه حضور و فعالیت مسعود عبدی در حوزه ورزش و مواضع آشکار مجموعه تحت مدیریت او در قبال ایران است.
عبدی به عنوان مالک باشگاه خیبر خرم‌آباد، طی ماه‌های اخیر تلاش کرده فعالیت این باشگاه را صرفاً در چارچوب مسائل فوتبالی تعریف نکند و در مناسبت‌ها و برنامه‌های مختلف، بر هویت ایرانی و تعلق ملی باشگاه تأکید داشته باشد.
اوج این رویکرد را می‌توان در مراسم رونمایی از پیراهن فصل جدید خیبر مشاهده کرد؛ مراسمی متفاوت که طراحی و روایت پیراهن، به شکل مستقیم به ایران، شهدای جنگ و حوادث اخیر کشور پیوند خورده بود.
در این مراسم، باشگاه خیبر از روایتی استفاده کرد که هدف آن تأکید بر هویت ملی، ایستادگی و حمایت از ایران بود؛ اقدامی که در فضای رسانه‌ای داخلی بازتاب پیدا کرد و نشان داد مجموعه تحت مدیریت عبدی تلاش دارد مواضع خود را نسبت به مسائل ملی و کشور به شکل آشکار بیان کند.
همین جنس از اقدامات، در کنار حضور عبدی در حوزه اقتصادی و ورزشی، این پرسش را ایجاد می‌کند که آیا تمرکز رسانه‌ای اخیر بر او صرفاً به مسائل مربوط به یک پروژه ساختمانی بازمی‌گردد؟
وقتی یک پروژه اقتصادی بهانه‌ای برای حمله سیاسی می‌شود
﻿
در شرایطی که پروژه‌های آرین سازه همچنان در حال اجراست، مجوز پروژه «ستین» اخذ شده، عملیات فونداسیون آغاز شده و پرونده‌های قضایی مطرح‌شده نیز بنا بر مستندات ارائه‌شده از سوی شرکت، به نفع آرین سازه خاتمه یافته است، بازنشر تصاویر قدیمی اعتراضات از سوی یک رسانه خارج از کشور، محل تأمل است.
منتقدان این رویکرد معتقدند نمی‌توان ارتباط میان فعالیت‌های اقتصادی، ورزشی و مواضع ملی عبدی را در تحلیل این حملات رسانه‌ای نادیده گرفت؛ به‌خصوص زمانی که مجموعه تحت مدیریت او در یکی از مهم‌ترین برنامه‌های اخیر خود، یعنی رونمایی از پیراهن خیبر، روایتی صریح و ملی‌گرایانه با محوریت ایران ارائه کرده است.
به بیان دیگر، آنچه در این میان اهمیت دارد، تنها یک پروژه ساختمانی نیست؛ بلکه تصویری است که از یک چهره اقتصادی و ورزشی ساخته می‌شود که در سال‌های اخیر، حضورش در ورزش و فعالیت‌های باشگاهی با تأکید بر هویت ایرانی و حمایت از کشور همراه بوده است.
منبع: مشرق نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/682053" target="_blank">📅 21:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682045">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq0SRWXyd75o4uhCM-RszuI8IGnQ7aF6cg9g1hCU-rV7JqQWi6juGN1gjH67TD8hmQkU2nyR9DiRHZRIAxZur6U3RjeALwgHCPjm7yIft3HyO_JxYT9d1K7s_7FmGOCGpvO2Z99rCDjt_ui0XJMzarhWH45LF4uEv6mqBzCycY9s3dA877caFr6p55Y7a3_z1AjKk3GQR2WPlBEwSZDuOYK1pThWEJ7A45b_J0gk-ZesR3S3SwxYXYJjlVgo9TrwWkMFEeORfI3W3kshySEfXusrTwjdR-YguKX7Nq_5r4ur8ML2aBmAUICqgB4Agy_Didb9x368PX9cG0sU-Lmu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۹۰ دلار در هر بشکه رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/682045" target="_blank">📅 21:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682044">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعاهای جدید وزیر انرژی آمریکا: ایالات متحده در حال اتخاذ یک رویکرد بلندمدت در قبال ایران است، استراتژی ما اعمال محاصره اقتصادی فلج‌ کننده علیه ایران است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/682044" target="_blank">📅 21:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682043">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادعای سنتکام: از زمان از سرگیری محاصره دریایی ایران، ۶۴ کشتی تجاری را منحرف و ۳ کشتی را از کار انداخته‌ایم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/682043" target="_blank">📅 20:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682042">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
معاون وزارت خارجۀ ایران امروز در پکن با معاون وزیر خارجۀ چین دیدار کرد
🔹
۲ طرف در این دیدار دربارۀ مناسبات دوجانبه، موضوعات امنیت منطقه‌ای، وضعیت تنگه هرمز و همکاری در مجامع بین‌المللی به گفت‌وگو نشستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/682042" target="_blank">📅 20:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682041">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
فایننشال تایمز به نقل از یک مقام رژیم صهیونیستی: اختلافاتی میان اسرائیل و آمریکا درباره امکان خلع سلاح حماس وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/682041" target="_blank">📅 20:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682040">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای مقام پاکستانی درباره ادامه مذاکرات پیرامون بازگشایی تنگه هرمز
🔹
یک مقام دولتی پاکستان به «MS NOW» اعلام کرد که مذاکرات برای بازگشایی تنگه هرمز که حدود یک‌ پنجم نفت جهان از آن عبور می‌ کند و دستیابی به پایانی مسالمت‌ آمیز برای این جنگ (تنش آفرینی آمریکا علیه ایران و ناامن کردن منطقه)، همچنان ادامه دارد.
🔹
کاخ سفید در پاسخ به سوالی درباره احتمال تمدید آتش‌بس، «ام‌اس‌ناو» (MS NOW) را به اظهارات روز دوشنبه ترامپ در گفتگو با فاکس‌نیوز ارجاع داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/682040" target="_blank">📅 20:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682039">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875008b658.mp4?token=C-v0Lb1uX8c3GeStvIJrI3mbrdm58Ma_i0luR_28hmWKj4qFKJhePc9iLJ0RMENlIEwfnKb6B65OBKfWnMIsawlXTt7Tapkqv-3EJNuL97908T7cxCGC8QjJktACNTeGI4vqpxWl0HEqMB1XdnhD1nVypgFSa9ljA7aYsXpvhv1a9ctwneUbOkGWOK4NHtmERYpSg9vn6AH1DdT2m_fRyRuRwpy8-F9MG5G1kLx1ZeFSivo7eUF4ZXzRAUX8wIcFOGJqEyqEutpC0BfyGFeAm4eLD0pONo4YTxZKDUhoomFss-o25vn1uPyHbne68m5NYpN0zefLfTkLgFcs0lTZ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875008b658.mp4?token=C-v0Lb1uX8c3GeStvIJrI3mbrdm58Ma_i0luR_28hmWKj4qFKJhePc9iLJ0RMENlIEwfnKb6B65OBKfWnMIsawlXTt7Tapkqv-3EJNuL97908T7cxCGC8QjJktACNTeGI4vqpxWl0HEqMB1XdnhD1nVypgFSa9ljA7aYsXpvhv1a9ctwneUbOkGWOK4NHtmERYpSg9vn6AH1DdT2m_fRyRuRwpy8-F9MG5G1kLx1ZeFSivo7eUF4ZXzRAUX8wIcFOGJqEyqEutpC0BfyGFeAm4eLD0pONo4YTxZKDUhoomFss-o25vn1uPyHbne68m5NYpN0zefLfTkLgFcs0lTZ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استفاده‌های کاربردی خمیر دندان در پاکسازی وسایل منزل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/682039" target="_blank">📅 20:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682038">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFULv5KYg_DX6Uaznvs17RQ9g21Ri-WJIJ26a-lV2A3TnVwcja-UdGyO04PUGoaSXUgUI_1eP1_jisnPwfMueTbuRpaPE7fahVMrjMneY260zn19QtxMWyFvS5ViL6VrTM24Nqy_BqnI9dh7gzPE9AV-zsAHKlAh65xHTtg-V3PoPDNF_r7LTG_3UreerG65nFWJ08bppBn-y5n2PtuVV05ZUvWNkbOKMVU7YMn6Hi-J1DZHkPR4_oyAZ13jyHGf1T2x_ii0WYEaM4zkJuJy_lwOqDAKy5vid5FQFDxdF30WQYWoa52lgF-9BF6r3-2R7NfnhXB64ZHGVsy64qaY_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار مهیب در جنوب لبنان
🔹
خبرگزاری ملی لبنان از وقوع یک انفجار شدید در جنوب این کشور از سوی اشغالگران صهیونیستی خبر داد.
🔹
وحوش صهیونیستی اقدام به ایجاد یک انفجار بزرگ در شهرک زوطر الشرقی در جنوب لبنان کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/682038" target="_blank">📅 20:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682037">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
پزشکیان: صرفه جویی در یک بخش نباید منجر به افزایش مصرف در بخش دیگر شود
🔹
طرح‌های بهینه‌سازی مصرف باید مورد ارزیابی قرار گیرد، در مواردی هر میزان صرفه‌جویی ایجاد شده در یک بخش، به‌دلیل شکل‌گیری تقاضای جدید یا مصرف غیرضروری در بخش‌های دیگر، عملاً به افزایش مصرف نهایی منجر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/682037" target="_blank">📅 20:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682036">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617099824f.mp4?token=pEPnjiXrbNN9KetaMBBSK3WD3xnFl3zzYnh6dU3xUr4vEjPCHqVDy8ZWYKJ_3ZIKhN6eQSLuSS9rixfUU0H6ySEMwiW_xqFcY5YCQW-R5xRzV2bADqP4ZaKU2jjQwQZVTbZBKcj4zgnYeptVZc9gW4aVTZiO_oEaJRzpEr8Lq5msolKuoJuG58lZZIYsnwGeTa3x7pf7w5LJ3UotqvvqGCLoyJwhnO1BeHZRyRNKj9Zz11fyBKfe01ZAeOgQUP1tPLfLhjfmDijZ0W4obO6oRrrnEssGBIp0WttSh4QS7Q_5r3mnVXWVjDPDget66RqOjBLHPvPh3sF9Uwo5qbxarA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617099824f.mp4?token=pEPnjiXrbNN9KetaMBBSK3WD3xnFl3zzYnh6dU3xUr4vEjPCHqVDy8ZWYKJ_3ZIKhN6eQSLuSS9rixfUU0H6ySEMwiW_xqFcY5YCQW-R5xRzV2bADqP4ZaKU2jjQwQZVTbZBKcj4zgnYeptVZc9gW4aVTZiO_oEaJRzpEr8Lq5msolKuoJuG58lZZIYsnwGeTa3x7pf7w5LJ3UotqvvqGCLoyJwhnO1BeHZRyRNKj9Zz11fyBKfe01ZAeOgQUP1tPLfLhjfmDijZ0W4obO6oRrrnEssGBIp0WttSh4QS7Q_5r3mnVXWVjDPDget66RqOjBLHPvPh3sF9Uwo5qbxarA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط بالگرد در یونان
🔹
منابع خبری از وقوع سانحه هوایی مرگبار برای یک فروند بالگرد در جزیره «سیفنوس» یونان خبر دادند.
🔹
در این حادثه، هر ۳ سرنشین بالگرد جان خود را از دست دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/682036" target="_blank">📅 20:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682035">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
الجزیره انگلیسی: شناور حامل ۱۲ فعال طرفدار فلسطین از شهر بریستول در انگلیس به سمت غزه به حرکت درآمد تا به ناوگان آزادی برای شکستن محاصره دریایی اسرائیل بپیوندد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/682035" target="_blank">📅 20:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682034">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff4b43c150.mp4?token=OTGWj4_KFXo7z2CxxmaYPZsEvlpdpmdd-f1Tgk3_WG1PZ19KIS6SldGPppK2AjLr3iVfVtZ0-QjBHdx2d81pIR1YBPn2UoJE_YziiP2ZYpArpH4HMDcj0Pflb1Lkh9jsTkYvI0t9rj3eafpti780L3DhGi3p6aL968dvJdCBhQsZGPo0JvO6sfBQj7TEytUbSfqVOBntH2IP7ujgYhsPmVvAiQz0wHtaDx3MwFeukLLkByYsRxjBlwD4v_7CoC0c7W9ZoYPuBVtPRb23Xvm3wVn6Opm7FBIyfgYq0UWdM_JU_1XjVVa-bHBtlOuS6d8SONbitdmcj8V9Cv4UN33fEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff4b43c150.mp4?token=OTGWj4_KFXo7z2CxxmaYPZsEvlpdpmdd-f1Tgk3_WG1PZ19KIS6SldGPppK2AjLr3iVfVtZ0-QjBHdx2d81pIR1YBPn2UoJE_YziiP2ZYpArpH4HMDcj0Pflb1Lkh9jsTkYvI0t9rj3eafpti780L3DhGi3p6aL968dvJdCBhQsZGPo0JvO6sfBQj7TEytUbSfqVOBntH2IP7ujgYhsPmVvAiQz0wHtaDx3MwFeukLLkByYsRxjBlwD4v_7CoC0c7W9ZoYPuBVtPRb23Xvm3wVn6Opm7FBIyfgYq0UWdM_JU_1XjVVa-bHBtlOuS6d8SONbitdmcj8V9Cv4UN33fEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رصد پهپاد جاسوسی رژیم صهیونیستی  بر فراز شهر صور در جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/682034" target="_blank">📅 20:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682033">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
دیلی‌میل: ملانیا ترامپ نگران است ایران دونالد ترامپ را ترور کند و این مسئله موجب ترس او شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/682033" target="_blank">📅 20:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682032">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e2089c88.mp4?token=VfE40x4Bk3Kw543il_GX5qjaGm3TOxkoCzgPJoDDkQyRUJRsVcgEYOQPbcpVFNPCnT4OEtd89vrFdUgJaRraZfJwe_5UxEhJ58tC6Kt40kEDkA9M0TK7KcZlwVQCg5boko2t1V7NCLizMqi2zG8vCmxVXTHXvRJtuij4-QV0yzSTYqoWWyeoJZtm6vXIO51_gP087IK6X8cVQVCEvMfFRXeWRv0RlkvZBFkpCOk6fFyCVVZ3OAvWBKtSA1_IgxpgENjox1cebadJhQfYM_IXUWKNn0KIOOVzK8dJKXV6kWihkls28-EWhJRC8rGo-rKuWoQZ0mwOBIBSpxlMs9KtIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e2089c88.mp4?token=VfE40x4Bk3Kw543il_GX5qjaGm3TOxkoCzgPJoDDkQyRUJRsVcgEYOQPbcpVFNPCnT4OEtd89vrFdUgJaRraZfJwe_5UxEhJ58tC6Kt40kEDkA9M0TK7KcZlwVQCg5boko2t1V7NCLizMqi2zG8vCmxVXTHXvRJtuij4-QV0yzSTYqoWWyeoJZtm6vXIO51_gP087IK6X8cVQVCEvMfFRXeWRv0RlkvZBFkpCOk6fFyCVVZ3OAvWBKtSA1_IgxpgENjox1cebadJhQfYM_IXUWKNn0KIOOVzK8dJKXV6kWihkls28-EWhJRC8rGo-rKuWoQZ0mwOBIBSpxlMs9KtIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در اطراف میدان شهرداری گرگان
🔹
چند باب از مغازه‌های اطراف میدان شهرداری گرگان از حوالی ساعت ۱۹ و ۱۵ دقیقه امروز دچار آتش‌سوزی شده است.
#اخبار_گلستان
در فضای مجازی
👇
@AkhbareGolestan</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/682032" target="_blank">📅 20:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682031">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
گاردین: قیمت گاز طبیعی در آمریکا همزمان با بن‌بست مذاکرات ایران و آمریکا به بالاترین سطح ثبت‌شده رسید و رکورد زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/682031" target="_blank">📅 20:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682029">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8036ca0d71.mp4?token=YLckjA-Z8m7qNTXg2Ka6Zjia6k2iufiLdXs-xzxlmv3A0gpwG1iELe1fIKHY2CNVuj3363-GTqGQyznwGAWWRXwCV_0-F0eTD1x8urMM_m5BZ3gpdu-B_SnKbM4YZCWBzZPVviK9V2iMsEhKF-SGKJ_9KXkVa1GGqZnzf_YTVsVlTFVPf1cfTuqJGsCuNDKT3Pl_f3ytEhsT-03AoVi7J4d0nNQfa8Ou6j_cElDCN9UFGAOBHlI2weUSZff65bR_uLMTxlWpdSZN4XMw7SXcsM0ZSddJEFHg4lyjUGmEYYPc2RKUcvJvZes3qNpeJ_1hPw7KzdgIzZllclNMNDbx0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8036ca0d71.mp4?token=YLckjA-Z8m7qNTXg2Ka6Zjia6k2iufiLdXs-xzxlmv3A0gpwG1iELe1fIKHY2CNVuj3363-GTqGQyznwGAWWRXwCV_0-F0eTD1x8urMM_m5BZ3gpdu-B_SnKbM4YZCWBzZPVviK9V2iMsEhKF-SGKJ_9KXkVa1GGqZnzf_YTVsVlTFVPf1cfTuqJGsCuNDKT3Pl_f3ytEhsT-03AoVi7J4d0nNQfa8Ou6j_cElDCN9UFGAOBHlI2weUSZff65bR_uLMTxlWpdSZN4XMw7SXcsM0ZSddJEFHg4lyjUGmEYYPc2RKUcvJvZes3qNpeJ_1hPw7KzdgIzZllclNMNDbx0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سبزیجاتت رو تازه‌تر نگهدار و دورریز رو کمتر کن
🌿
🥕
#ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/682029" target="_blank">📅 20:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682028">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24e9f53437.mp4?token=rDbJ6FLStyQViNUBYIkUv7LTo2JFB3MX19QV5PLsYJWOWeU-B20dspc97GsE84WfUZz-eR5A_AdLGBNueV4gOvknRLbT71OBBYzPEhttQnSqQJM3BhZxoGivVcofxfPGrb6dDQ9h4yt-uRKEjiteW0Qcp4bksXOwC6MYbMq0R2__lzs2-2kZKs_j5IeRRyJO2r-jmIK_e_ug8BVGzzpRClyPn-1ZnqrlIr69CwNTMc8OnPo2MCNHRjtt80fKGl46PW-NPXwTOZxAr_UQa9SFCtIMIeH4sCLQdeKEReS9rUd78Cayhi6upr5xSRsi3edekG4P7uxjbkhgKydZ-4TXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24e9f53437.mp4?token=rDbJ6FLStyQViNUBYIkUv7LTo2JFB3MX19QV5PLsYJWOWeU-B20dspc97GsE84WfUZz-eR5A_AdLGBNueV4gOvknRLbT71OBBYzPEhttQnSqQJM3BhZxoGivVcofxfPGrb6dDQ9h4yt-uRKEjiteW0Qcp4bksXOwC6MYbMq0R2__lzs2-2kZKs_j5IeRRyJO2r-jmIK_e_ug8BVGzzpRClyPn-1ZnqrlIr69CwNTMc8OnPo2MCNHRjtt80fKGl46PW-NPXwTOZxAr_UQa9SFCtIMIeH4sCLQdeKEReS9rUd78Cayhi6upr5xSRsi3edekG4P7uxjbkhgKydZ-4TXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیشنهاد تلویحی مارک لوین برای استفاده از بمب اتم علیه ایران
مارک لوین، مجری مطرح آمریکایی:
🔹
حکومت ایران تسلیم نخواهد شد؛ هیچ‌وقت تسلیم نمی‌شود. ما پیش از این هم در جنگ‌هایی با دشمنانی روبه‌رو شده‌ایم که حاضر به تسلیم نبودند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/682028" target="_blank">📅 19:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682024">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/273b4ce7d9.mp4?token=qGmCLqslqusWFAdJpWdkKeQLpsje8nV2LrV0nWbYtrodC25YqNwEt5URY2fvngITsDOvky6T69JxdGmeK3BkSCvCiskI7aWm7tWc47q49KmBpUUHQUxQAd4qKXVGutPJYp6Vlo_0iq54DTDpE0P7tg_e8M5vNn8g87qns1kWHAXzfJnw7IF8lxNs7HbCtYkA4080Jj6TXznYUPZCjrLx8vhCt-GevmIzV0MdA96H9NClNy_hxDUYPeGyFP8JGJPzY_2sg3FE1vhuWve714wEfiez_aK4vbWfmO4O3bZm91l3aRSsf0HVPxu72rRRlmX8MrfBPMFqDq8IH27qIPuclA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/273b4ce7d9.mp4?token=qGmCLqslqusWFAdJpWdkKeQLpsje8nV2LrV0nWbYtrodC25YqNwEt5URY2fvngITsDOvky6T69JxdGmeK3BkSCvCiskI7aWm7tWc47q49KmBpUUHQUxQAd4qKXVGutPJYp6Vlo_0iq54DTDpE0P7tg_e8M5vNn8g87qns1kWHAXzfJnw7IF8lxNs7HbCtYkA4080Jj6TXznYUPZCjrLx8vhCt-GevmIzV0MdA96H9NClNy_hxDUYPeGyFP8JGJPzY_2sg3FE1vhuWve714wEfiez_aK4vbWfmO4O3bZm91l3aRSsf0HVPxu72rRRlmX8MrfBPMFqDq8IH27qIPuclA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لخته خون؛ بمبی خاموش در قلب
🔹
لخته‌ای که در حفره قلب تشکیل می‌شود، در صورت جدا شدن می‌تواند وارد جریان خون شده و به عروق مغز برسد و باعث سکته مغزی ایسکمیک شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/682024" target="_blank">📅 19:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682023">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLTE5NQ3V9U7_V9hwufC9MVjIJENQ8BxnhVQ420fe0rg34U9YTe3P9sg6wNNQ5cOcp8f34VAbNASuq0TIQOsmwn4_k503F-nlNRRhgJ_lUG3ImwsqT1YKGCUzDWQFay6uBQ1QfculkIGD8X6N8Ai3NUgVsG0hO1dHqTiOnHmxmTfa6euVgXQaTm-NPouOg178Dv80hD-26b4Xfj77BdgcKO2g6iTb-kUVKPBWeaYcdbpI3Woj4_OYJztB5lFj4kdVMEP1C2YyTdLaXJWxFiI8Lyu4uY9CVfY34CbnE9fyHXA3_BYXD70owALHmoSr6myJgyyBmy7yHu2cwoeCUpk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقیف نفتکش اماراتی در تنگۀ هرمز
🔹
داده‌های ناوبری دریایی نشان می‌دهد که یک نفتکش متعلق به یک شرکت اماراتی هنگام عبور از تنگه هرمز، متوقف شده است.
🔹
طبق ترتیبات ایران برای عبور امن از تنگۀ هرمز، مسیر ایرانی یکی از شروط است و پرداخت‌بهای خدمات و اجازۀ ایران از دیگر شروطی است که نفتکش‌ها باید رعایت کنند.
🔹
نفتکش امارات در نزدیکی قشم متوقف شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/682023" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682022">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ادعای رویترز: ایران تصمیم گرفته است سیاست خود را از حالت دفاعی به حالت کاملاً تهاجمی تغییر دهد
ادعای رویترز به نقل از یک مقام ارشد ایرانی:
🔹
فشار بر آمریکا یا تکیه بر میانجی‌ها برای رسیدن به یک توافق دائمی واقع‌بینانه نیست.
🔹
تهران ضرب‌الاجل چند هفته‌ای برای آمریکا تعیین کرده تا یادداشت تفاهم را به طور کامل اجرا کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/682022" target="_blank">📅 19:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682021">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1893f96cbe.mp4?token=KcyVXxwG-6NSnB4CL6TxUef1Bwm9e9-nRAkrfzfvxsORKJZhpELA6zDlcNY7-K6XTuRH-MQ98q1tc35c_ggt06OcrG68Rc0v_CvpJL89YSw7D2DD7XtMue2gBhk3YUhCl3ioiIvFl9SXYrPspGRM5DPuYl6Zj82Vq2b6WCHDqOb4zgCVP2x09uRHGtsru7qtuEvIZTA-14s8EhDscFOyVVeGzpkEhE3bAYyoUakHczpVUFW79USmOplLt0Mc7La5utToxj2DlCkJZMpAM268Hezx8ZkJYNPxTqzoaq-poA-Tn6yeLJOYDZoiNwBGl7IMMB-I5q7pu3L_Jl81fbvUGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1893f96cbe.mp4?token=KcyVXxwG-6NSnB4CL6TxUef1Bwm9e9-nRAkrfzfvxsORKJZhpELA6zDlcNY7-K6XTuRH-MQ98q1tc35c_ggt06OcrG68Rc0v_CvpJL89YSw7D2DD7XtMue2gBhk3YUhCl3ioiIvFl9SXYrPspGRM5DPuYl6Zj82Vq2b6WCHDqOb4zgCVP2x09uRHGtsru7qtuEvIZTA-14s8EhDscFOyVVeGzpkEhE3bAYyoUakHczpVUFW79USmOplLt0Mc7La5utToxj2DlCkJZMpAM268Hezx8ZkJYNPxTqzoaq-poA-Tn6yeLJOYDZoiNwBGl7IMMB-I5q7pu3L_Jl81fbvUGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دست‌نوشته‌های سربازان آمریکایی روی بال هواگرد ارتش آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/682021" target="_blank">📅 19:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682020">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99c0d9fee7.mp4?token=beDMz9UqaYnyQEWPZoW9FYMq2KI2W556A54GR1xrgG94pArQmyIr09DP1ennXTMk1lWzAsfnsDwg451BSdvrfip26znavhqxc-qcSNcEM4TNN718xPISYjuAJatRjmVij1wikneTOUJqK1ULwCTY8Jylj8ZaGGtxR_uXfd3pqPm4sabDasSUaPhkT4U1DvdwRd9rKdv0FFxRC7s2ynrg9RrSWyTtrn84uEU9SorThM8I8c4kZoZS6a5uBKHhpVsGzqF22wC2sH9Wdgx9cZJh0PT1Cj6jW0QOXSEARJI0i0JXL6mEuxS_AvJTXD3kxUHRgQ_lEmVWWGlRET2Lgxxc6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99c0d9fee7.mp4?token=beDMz9UqaYnyQEWPZoW9FYMq2KI2W556A54GR1xrgG94pArQmyIr09DP1ennXTMk1lWzAsfnsDwg451BSdvrfip26znavhqxc-qcSNcEM4TNN718xPISYjuAJatRjmVij1wikneTOUJqK1ULwCTY8Jylj8ZaGGtxR_uXfd3pqPm4sabDasSUaPhkT4U1DvdwRd9rKdv0FFxRC7s2ynrg9RrSWyTtrn84uEU9SorThM8I8c4kZoZS6a5uBKHhpVsGzqF22wC2sH9Wdgx9cZJh0PT1Cj6jW0QOXSEARJI0i0JXL6mEuxS_AvJTXD3kxUHRgQ_lEmVWWGlRET2Lgxxc6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکاف هذلولی؛ جایی که هندسه غیرممکن‌ها را ممکن می‌کند
🔹
در این پدیده، یک چتر یا میله صاف با زاویه و چرخش مناسب از شکافی با شکل هذلولی عبور می‌کند؛ نمونه‌ای شگفت‌انگیز از اینکه هندسه سه‌بعدی چگونه می‌تواند چیزی را که غیرممکن به نظر می‌رسد، ممکن کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/682020" target="_blank">📅 19:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682017">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IyNyDJDRYqnU4Pse3om7SPWF6HM8aXlPxN1qsN3v8qg-fP8M0B1KyZMXkzCPInKo17TLnuDuALQBKZn-MSV9qYMUX6LgEeIjZMcbjyo4gVntxo0rHPU6EXrdBkdTCIzXCcTsj66mW1NZsqTuHMREmdFtAON7z-eI6_SFDPb_8OsAlG-KsCUBCRR4h1Kf0_YDLOypXoAKLjm-BK_9OB-d_43kZULAyubDnd1azCb2CGV54YM2SabuUQtWzo9htwhub7DeoGVYbebVRBxUp7UOBmb4yB28PWzpiM3_e6TdGil_rqxJcAHvVMIxKOXiY9Zy6rYJH33b3FUrMiXCHN9u_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhV4bzAwebCnJ2R80kILAL9OUaGyM78NLoqqh4Zojv1AGYGpdI46HnWG2FvsA0EiqeLdWAJEsYlMAtz69pxsD67_HKgRdB5bpDc1aFzIN4W3IsBRhO_GPm8m_w__hveDGHHkIhOBbt66Gh8hkK-ILjqpY1zy7zC9CV6uEsZ6o9a8Vc0C78vrydpbSf-lcXTzIPEEjoCBD_fJL5hckj71c1MmtJRLjz9_bWd1MkMxsa21jN9hL8X2aGu68BPrmGzFgEX6Wh-6IMn-_E4HcSVinTGFHaf0sp3MWoD1mnXNSKzTkph5N78_lg_X3CgKeZMEzhu7hakul6WgfxHCh_7DAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آتش‌سوزی مهیبی در یک انبار بزرگ گاز طبیعی در گلنپول، آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/682017" target="_blank">📅 19:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682016">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b13ccc88d.mp4?token=a2Copt5VI2KNIpkGS8-eU1N-GLD0_LW3EEi0M4ayT0vF4v_IUuQDzborfOuNs2-qSbw2N5A6XbPpKLS1c9l5k-ZjTEDItoie8tXcImuGkxhJ3iipH41bEjCRYnm2y7ox4n32RY1fPRrc2JEm3nJOjFoj-G7ku8jrIOXteaFGElivPj-DGw6_NVQtg_8yET6lWF1ZdMK6FeV4NcVIhkzv274gQVCLz4bkoLSU8u2fEZzPG3I4fqnzZn1Z-OoV3sSXybqqs-3qopgimnmfRLymNXSg1FiTaEY_rHyl-yJJCoY5wV_7WsOS0y2dyLBBPsk1X8ihBKk4Vir6iog48N6ivJ8u9mt4-FcYhF0RCIaWkZpdl394a4FzVVpBRc2lsrBTAYKeB73DY6Cb_eixzNzZd5s-Frm8nV3UJlUVX4AypmCvjkbkrjDaYpXUa4gO9yJuN00FQubjdAo4skM8rF1_VzxPsI1tE6QxQosfImuR0swrhVi6hhtqrQ7b968bivC-HRf3mMoSedCF24Na8Tmt2fNdhbDpVsq197-rdxPdvmp_CUwct-dEBs_VBl8847VWumf220CYW9fhT3JUMLcVXryZhP12pb69vqKEnTQr3E6UNir3rTNCEnSUhIovly14Zf0BfCXss30JXbAsOqcriigF0awiJTfQ6QkYBdqTFYk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b13ccc88d.mp4?token=a2Copt5VI2KNIpkGS8-eU1N-GLD0_LW3EEi0M4ayT0vF4v_IUuQDzborfOuNs2-qSbw2N5A6XbPpKLS1c9l5k-ZjTEDItoie8tXcImuGkxhJ3iipH41bEjCRYnm2y7ox4n32RY1fPRrc2JEm3nJOjFoj-G7ku8jrIOXteaFGElivPj-DGw6_NVQtg_8yET6lWF1ZdMK6FeV4NcVIhkzv274gQVCLz4bkoLSU8u2fEZzPG3I4fqnzZn1Z-OoV3sSXybqqs-3qopgimnmfRLymNXSg1FiTaEY_rHyl-yJJCoY5wV_7WsOS0y2dyLBBPsk1X8ihBKk4Vir6iog48N6ivJ8u9mt4-FcYhF0RCIaWkZpdl394a4FzVVpBRc2lsrBTAYKeB73DY6Cb_eixzNzZd5s-Frm8nV3UJlUVX4AypmCvjkbkrjDaYpXUa4gO9yJuN00FQubjdAo4skM8rF1_VzxPsI1tE6QxQosfImuR0swrhVi6hhtqrQ7b968bivC-HRf3mMoSedCF24Na8Tmt2fNdhbDpVsq197-rdxPdvmp_CUwct-dEBs_VBl8847VWumf220CYW9fhT3JUMLcVXryZhP12pb69vqKEnTQr3E6UNir3rTNCEnSUhIovly14Zf0BfCXss30JXbAsOqcriigF0awiJTfQ6QkYBdqTFYk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف یکی از فرماندهان ارشد ارتش رژیم صهیونیستی: تهدیدات ترامپ علیه ایران برای ما هزینه‌های سنگین و وحشتناکی دارد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/682016" target="_blank">📅 19:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682015">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای رئیس اقلیم کردستان عراق: دفترم هدف حمله پهپادی ایران قرار گرفت
🔹
مسرور بارزانی، رئیس دولت اقلیم کردستان، مدعی شد دفتر شخصی او در حملات پهپادی ایران هدف قرار گرفته است. مقر رئیس سازمان امنیت اقلیم کردستان نیز هدف این حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/682015" target="_blank">📅 18:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682014">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
تلفن رئیس دفتر ترامپ هک شد؟
پولیتیکو:
🔹
فردی با جعل هویت «سوزی وایلز»، رئیس دفتر ترامپ، با اندی برنهام، نخست‌وزیر بریتانیا، پیام ردوبدل کرده است.
🔹
مقامات لندن هم  احتمال هک شدن تلفن رییس دفتر ترامپ را مطرح کردند، اتفاقی که قبلا تایید کرده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/682014" target="_blank">📅 18:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682013">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4b9b8fd26.mp4?token=f_00MMGL0_twgQxxW33x4BO0SNbqTNwYQEXlE9r6sm1UN4wfQaLyXdV2R1n5ZhTSY0SytBFNzdRLQAdM4_ajsCkRs4qhw22VY8k5_Kk21nKmtKiCgux33aCHgJ1SF1mn6qI2bQw-_ee0NezI53DgRYjS6gikAHGrsnUJzMswCxYn8bwY2fyOBRp841jy3j-KM0CJJXWh5ygMRUNuR9m4hKnH9uLBi7j0hGNkLwtBfQO9HsELwY6SW-Zll1CAwZlaT6O5ANeuMxeg8537M-vybX2wQjvg1hAy7CCRMa4sEuS4SaVwIfKHrt7sYp3C191fbaz6P730b3P_92gSDi8dmgoKx_pCBTzn2EvAlLYSysnfoSEg7ERkR2qgeYYTopgH2GdIW30aDr39NHwGCtLxuc9je5AUui3n7tia3XQ-sRFVio4437rDMYpoHueHq9MAVh85B6235Ug4RiQph7M9h4pDxWnmvo5dTlF5mnQVlrXLcwJrSCkkTGyi6XRmbSdL8R_XwxseRNzE0eH-Nmbmx1rfkvUbOzWeyDjjUMOHxovlqs59QGrPm8SggJjGza9sGs61vQz38hcTb2We8WEuPe0lmpFsB3E00UmqYAZ6sIF0L76-7sGaBDau-2p3of_aseFLJ9eCKGvBC24dwUj2YeTF5QdsumRrlUjovtUErfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4b9b8fd26.mp4?token=f_00MMGL0_twgQxxW33x4BO0SNbqTNwYQEXlE9r6sm1UN4wfQaLyXdV2R1n5ZhTSY0SytBFNzdRLQAdM4_ajsCkRs4qhw22VY8k5_Kk21nKmtKiCgux33aCHgJ1SF1mn6qI2bQw-_ee0NezI53DgRYjS6gikAHGrsnUJzMswCxYn8bwY2fyOBRp841jy3j-KM0CJJXWh5ygMRUNuR9m4hKnH9uLBi7j0hGNkLwtBfQO9HsELwY6SW-Zll1CAwZlaT6O5ANeuMxeg8537M-vybX2wQjvg1hAy7CCRMa4sEuS4SaVwIfKHrt7sYp3C191fbaz6P730b3P_92gSDi8dmgoKx_pCBTzn2EvAlLYSysnfoSEg7ERkR2qgeYYTopgH2GdIW30aDr39NHwGCtLxuc9je5AUui3n7tia3XQ-sRFVio4437rDMYpoHueHq9MAVh85B6235Ug4RiQph7M9h4pDxWnmvo5dTlF5mnQVlrXLcwJrSCkkTGyi6XRmbSdL8R_XwxseRNzE0eH-Nmbmx1rfkvUbOzWeyDjjUMOHxovlqs59QGrPm8SggJjGza9sGs61vQz38hcTb2We8WEuPe0lmpFsB3E00UmqYAZ6sIF0L76-7sGaBDau-2p3of_aseFLJ9eCKGvBC24dwUj2YeTF5QdsumRrlUjovtUErfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هنرِ کفاشی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/682013" target="_blank">📅 18:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682012">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یک عضو ارشد مقاومت عراق به دستور آمریکا بازداشت شد
.
🔹
سازمان حج و زیارت: سفر عمره از اواخر شهریور آغاز می‌شود.
🔹
الجزیره: عربستان برای دور زدن باب المندب به انتقال محموله‌های نفتی کشتی‌ به ‌کشتی روی آورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/682012" target="_blank">📅 18:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682011">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88583c85a3.mp4?token=Q90xLEniRRhLtealaFO7xwd1ZIpdms1gzvNd8NMj9B9wZEz3E0y3vxY9a_3xGnFYlolnKb5d4ovMnmJolY6Iwr2cPrfg6ENQR_evVAi6miAA4PVgw0jnGO4BStF6ImxJGkG7BzzMa854UWCahuellxPF2f7eiaKF4qEMjENPInYy1w0vVbgU8d_U7R-78t_BjBEHjjloldxOZhMWrYnpbqkU6J8pSmnxRFoc2xAEpVj2Ht464YBCYuynfCrr669GB-JdLj1Cdw_vYeR-q9qWGzqBhZbA6rw8A6d_bt0qd6ChzRGexBCgtSLt8IYV2u_o7O9Q09r8P97gQgTZnBFuM4fCbuf7iMHZPLrwIZK0lVr3mi7bnkSKq3rfxFdJr3Sz2LsX-LCUDBMaVAUlnjNciwDR3UST9d40-1nYjFOmal3-Czjvoz0lq3Q9__KCmwNmq-N_i3UrGTcXC8p6NvZZH2r4eH6sswU1JppDhhn2qCe2kKIdqJ0zF2spS_ZysLIKTDm6uilK_zztDX9AZs4WjbcJdIjSp6FW-rj11MdFyju8VFcu7AXu6bZJhGSMjcfM3_bpJEv_7QLdUK_2Uc2jmF4uMyVIVyBCy3HbBjAyLEMlTme5wCiZTrUPYE3sXIkS9EnUDvU2u0TvUGge-lWRITxH7DuLftUcgtaO7T2fgNY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88583c85a3.mp4?token=Q90xLEniRRhLtealaFO7xwd1ZIpdms1gzvNd8NMj9B9wZEz3E0y3vxY9a_3xGnFYlolnKb5d4ovMnmJolY6Iwr2cPrfg6ENQR_evVAi6miAA4PVgw0jnGO4BStF6ImxJGkG7BzzMa854UWCahuellxPF2f7eiaKF4qEMjENPInYy1w0vVbgU8d_U7R-78t_BjBEHjjloldxOZhMWrYnpbqkU6J8pSmnxRFoc2xAEpVj2Ht464YBCYuynfCrr669GB-JdLj1Cdw_vYeR-q9qWGzqBhZbA6rw8A6d_bt0qd6ChzRGexBCgtSLt8IYV2u_o7O9Q09r8P97gQgTZnBFuM4fCbuf7iMHZPLrwIZK0lVr3mi7bnkSKq3rfxFdJr3Sz2LsX-LCUDBMaVAUlnjNciwDR3UST9d40-1nYjFOmal3-Czjvoz0lq3Q9__KCmwNmq-N_i3UrGTcXC8p6NvZZH2r4eH6sswU1JppDhhn2qCe2kKIdqJ0zF2spS_ZysLIKTDm6uilK_zztDX9AZs4WjbcJdIjSp6FW-rj11MdFyju8VFcu7AXu6bZJhGSMjcfM3_bpJEv_7QLdUK_2Uc2jmF4uMyVIVyBCy3HbBjAyLEMlTme5wCiZTrUPYE3sXIkS9EnUDvU2u0TvUGge-lWRITxH7DuLftUcgtaO7T2fgNY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از لحظات اولیه وقوع انفجار در غرب کابل و انتقال مجروحان به بیمارستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/682011" target="_blank">📅 18:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682008">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d93c2708c.mp4?token=YA3Z5K_becNH3yCgB21g3YKgLX65wC44QXhOt7Yhc-l0pmpyBgh4gO_iWQmwEJrWk8DenG3_-oEUwvkODnqOsdqaH1higUxBGCJtRzaCSVQWrYKGViLABjBz5XmBoCX77MgEZcshplHsCL_qyj2vANOSxMV9G9N-kTXDo8xsrrL-9nN4m0xNJRwQ5l0ItBUs0S53_CWoDzeyai7eDgwA4cdS5dVtdbLwJztNfu9Rj6wShjIV4QrRoAJk_gmWXhBL7GDE4Rllh2f2gF0VYKqa3dj_sh7MNk_OdSDadD8YyftxwszCR9Qy-ACpSvlYjawT9oWFDjFlwMRlUOlGOrsD_2ILiPF3qsrfcSGZhedHuAsIwaMVCfaVfHZtB5vMx75Z2UjbGnmpFP55PvT340dobgPq5GGDrsq7bRoAn2Hr4VilqVoJVqVlbz0wS_Ps0gTAOtorHgX4x2y6T5_karLDpvb8b6u7QNu5r8AEhGV9dT49bh7DwVbe2sDCNP0cNsYQOx8p_V2r3ZmCrNrvPzBXQDMsFT9airre0z1P3Yzmyosu_p4dyVx2RhstnywC8nPRTdqVFFp5WPfrLabuTNjVD9n8Lkh4vOeMfaT2iLlq6Q1qnFng-SqARvj3b1BXWJmVP1ZvXZAt-Q5u4GNnrVe7uwlGGszMEknvPIKbPMRscOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d93c2708c.mp4?token=YA3Z5K_becNH3yCgB21g3YKgLX65wC44QXhOt7Yhc-l0pmpyBgh4gO_iWQmwEJrWk8DenG3_-oEUwvkODnqOsdqaH1higUxBGCJtRzaCSVQWrYKGViLABjBz5XmBoCX77MgEZcshplHsCL_qyj2vANOSxMV9G9N-kTXDo8xsrrL-9nN4m0xNJRwQ5l0ItBUs0S53_CWoDzeyai7eDgwA4cdS5dVtdbLwJztNfu9Rj6wShjIV4QrRoAJk_gmWXhBL7GDE4Rllh2f2gF0VYKqa3dj_sh7MNk_OdSDadD8YyftxwszCR9Qy-ACpSvlYjawT9oWFDjFlwMRlUOlGOrsD_2ILiPF3qsrfcSGZhedHuAsIwaMVCfaVfHZtB5vMx75Z2UjbGnmpFP55PvT340dobgPq5GGDrsq7bRoAn2Hr4VilqVoJVqVlbz0wS_Ps0gTAOtorHgX4x2y6T5_karLDpvb8b6u7QNu5r8AEhGV9dT49bh7DwVbe2sDCNP0cNsYQOx8p_V2r3ZmCrNrvPzBXQDMsFT9airre0z1P3Yzmyosu_p4dyVx2RhstnywC8nPRTdqVFFp5WPfrLabuTNjVD9n8Lkh4vOeMfaT2iLlq6Q1qnFng-SqARvj3b1BXWJmVP1ZvXZAt-Q5u4GNnrVe7uwlGGszMEknvPIKbPMRscOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک تکنیک ساده که همون ماه اول خرجاتو کم می‌کنه #چرخ_زندگی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/682008" target="_blank">📅 18:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682004">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aae993a9f.mp4?token=o9bZoNlJfvbcR40Uc8tHygDujs8S_m-IkRAnCsGLL2douIIfGU-Jx_oKgaVOamFWcx_DLvFoQdlnBVqkNm7neW24vWd46o3DvNZVHkegAKXIEC6dhNCqd9s6D8JEl8Sb4mDbNl3g-Nc7mUW-uk08aG1-f_JLMgbdqowieDZhzW5WAWNSDwPoaQeJCog42dr4YInwdhQRQ1RjLD-O0gP3opGlwobMCC2RCrGO3AqpDT4oky_IHjaa91Tipee2-7xLFXQSuzNESwmpLHl09k1yXj4_zHZ0NoDYpM4QliDxJ-cvaK3a-6nR07WglinAnQtzTsgHzsiM7GmFVp15bAR7IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aae993a9f.mp4?token=o9bZoNlJfvbcR40Uc8tHygDujs8S_m-IkRAnCsGLL2douIIfGU-Jx_oKgaVOamFWcx_DLvFoQdlnBVqkNm7neW24vWd46o3DvNZVHkegAKXIEC6dhNCqd9s6D8JEl8Sb4mDbNl3g-Nc7mUW-uk08aG1-f_JLMgbdqowieDZhzW5WAWNSDwPoaQeJCog42dr4YInwdhQRQ1RjLD-O0gP3opGlwobMCC2RCrGO3AqpDT4oky_IHjaa91Tipee2-7xLFXQSuzNESwmpLHl09k1yXj4_zHZ0NoDYpM4QliDxJ-cvaK3a-6nR07WglinAnQtzTsgHzsiM7GmFVp15bAR7IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری تازه از لحظه وحشتناک وقوع زلزله کلمبیا
🔹
تازه‌ترین آمار از آن حکایت دارد که شمار جان‌باختگان زمین‌لرزه ۷.۵ ریشتری در غرب کلمبیا به دست‌کم ۲۸۸ نفر رسیده و بیش از ۴ هزار نفر نیز در این حادثه مصدوم شده‌اند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/682004" target="_blank">📅 18:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682003">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqjfTOxGikAarDEVgvjobzj4oZFMCuEIVIPwzLXVUPQ4Zc0CXxYz-dxGFl-02BESnirPazl9YPivHUtHicxkAFupswiG1Su82Rn9NrxV2jSt5R5DMF0WUr-ux_qO6rJ_r3GoHjyYfhBuwUa7UckmtcpEIIDjMqk_s2NLZse7bu1GlQk2Bt9w-81RWqZsMxo7_b-VurEf9h9T7SZQwu30UzLIX43-DynvPGO-O4hxydDhr-WYhfGO5bxrSkpR-6llFUer3C8rEVN7-9YDIRZA2dR_lDyfT5i2UDkDJlIPVj7bLbkEVoN8DuOzAWg0DXVpVQ3R1VOCrdjPP_X6KNM8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قهرمانی که نامش با قدرت، جوانمردی و افتخار ورزش ایران درآمیخته است؛ جهان‌پهلوان تختی
🔹
غلامرضا تختی، از بزرگ‌ترین قهرمانان تاریخ ورزش ایران، تنها یک کشتی‌گیر پرافتخار نبود؛ او با منش پهلوانی، احترام به مردم و روحیه جوانمردانه‌اش به نمادی ماندگار در فرهنگ…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/682003" target="_blank">📅 18:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682001">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9DBlp22yQzFZReDOFfa83TxkjHIm2wUOMBYP69bmNL87w-SGsXVHlLWCOLFN8FKwl6Crwp2ixKeq3GkqBcYlUm58yaYyByMQ2e2WICz-_FfT_qKCZHj8V-ahSvJiZoXGo9sQXwXityApPbZd0Y607Pu-hMpd3XXVaI4YtQK45neKt-VAzBb03DKb_QFz6pmukj_2IKNPoRymLRpoJkFniH86axbqMMMCEd9-c5Hr0C08i8MIhAolOiWhry2o2w8Q_zrqtWNXdyIyJbTN_zS-6qb0obSCUViS3MiftybIiBnWkOzvA4_7GkgECmSZtYBeziowEWK82S7Mf0eKTpVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۹ سد برق‌آبی ایران پُرآب‌تر از پارسال
🔹
بررسی وضعیت ذخایر سدهای برق‌آبی کشور نشان می‌دهد ۹ سد مهم کارون۴، کارون۳، شهید عباسپور، مسجدسلیمان، گتوند، دز، مارون، سیمره و کرخه نسبت به مدت مشابه سال گذشته آب بیشتری در مخازن خود دارند.
🔹
سدهای برقابی سهم مهمی در تامین برق تابستان دارند، با این وجود در روزهای گذشته، قطعی برق شبانه و خارج از برنامه در بخش خانگی و همچنین قطع برق صنعت بیشتر از گذشته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/682001" target="_blank">📅 17:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681996">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/999d8e8665.mp4?token=uE5W7NhoH8JuOoANWVP7K_u4Ou4Nupf5KLcBn2qsTKIzHxsa-mcg4ElzGmIWXivxWSiafBbALhyFPfbdBjFb3a6xA0eTKu2dz3eOsPxN0DnTNQEE9bbmaCPXYR-qASxq_EJCBE8C0XF4lD1vmzxU2UH5nlgYvaG1FCqNXy5Gw_GUIuZQVIyfiZIzDe7Lv64TqtAofQAQlpJ_M8AzPGTEXe8Z83tRIHVgMRBY-5KC-ArUpIbJnsR1MxSHvC8fZ-yz9Yb48k0SrM-DG1tjsBRoJUfdc399vAAWuBi59BRAAri0_zW34_IO3nZrzLACtwOlZG2R8ecdWi0yHj5oeG7c5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/999d8e8665.mp4?token=uE5W7NhoH8JuOoANWVP7K_u4Ou4Nupf5KLcBn2qsTKIzHxsa-mcg4ElzGmIWXivxWSiafBbALhyFPfbdBjFb3a6xA0eTKu2dz3eOsPxN0DnTNQEE9bbmaCPXYR-qASxq_EJCBE8C0XF4lD1vmzxU2UH5nlgYvaG1FCqNXy5Gw_GUIuZQVIyfiZIzDe7Lv64TqtAofQAQlpJ_M8AzPGTEXe8Z83tRIHVgMRBY-5KC-ArUpIbJnsR1MxSHvC8fZ-yz9Yb48k0SrM-DG1tjsBRoJUfdc399vAAWuBi59BRAAri0_zW34_IO3nZrzLACtwOlZG2R8ecdWi0yHj5oeG7c5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وان‌یوآی ۹.۵ سامسونگ؛ انیمیشن‌های روان‌تر و قابلیت‌های جدید
🔹
اطلاعات فاش‌شده از One UI 9.5 نشان می‌دهد سامسونگ روی روان‌تر شدن انیمیشن‌ها، طراحی جدید حسگر اثر انگشت، تغییرات ظاهری دوربین و نوارهای جست‌وجوی جدید کار کرده است.
🔹
همچنین قابلیت میرور کردن اپلیکیشن‌های گوشی روی لپ‌تاپ ویندوزی نیز احتمالاً به این نسخه اضافه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/681996" target="_blank">📅 17:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681995">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Csi1xyF9mL8i2t_gMlqbzg-txGYjfJQb2FZ3I6t9i6IKfUsxJEi5AcqIr1vRlIqrAPKXsWoR9Etum_8PPrj1coO0x2qrUYNELtOmrRNDjhyoBzKkI4u8XLUPnKi41DxToC2f3f0nt5Snhhqq79sxvlgJtX0iAW8TOSmYvEo5AeBxzkpxouiKfi1Zc1-V7L9wlpEtvUJVRBN-rK6oXExekHT4q6bgwEmMi4Js-tlAPn1f6Yv2BnJnIg6E-TzbGy1Yxm2uaLlCx-_mY5YAN76I00eKgBO7un2kOhSHE_XvU7o2vHlAXwF73JYnX-OynWqn02ypKZm5_O-ySgc6C1ScXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار ۱۵۰ هزار اسرائیلی طی ۳ سال
🔸
بر اساس گزارش فایننشال تایمز، بیش از ۱۵۰ هزار اسرائیلی در ۳ سال گذشته اسرائیل را ترک کرده‌اند.
🔸
حدود ۱۰۰ هزار نفر در سال‌های ۲۰۲۳ و ۲۰۲۴ و حدود ۴۵ تا ۵۰ هزار نفر در سال ۲۰۲۵ مهاجرت کرده‌اند تا برای نخستین‌بار مهاجرت خالص اسرائیل منفی شود.
@amarfact</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/681995" target="_blank">📅 17:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681992">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfc3d46d0.mp4?token=q94Vab6jZNiBUJAxoDeL1kc6wyMB_mshI8CwaiB24Kii-Y17SEFWly1j5ALFN_YtCNkbKDhGkkoaGgecETOIwpyqRcBIDwvy2FMwE1F2zoPDKhR85guogVsDRfZggvsTDBgeoQQU6FNLBH1304POO4QbSwHStT83-ySMIj7w2_egeNGhpACqBuKfYl71lokuUixi-61-rPTq-D-utIMprZlBp5USUHkr5rlZbVNpQJ2JzujVRGBqnc8AixShECy7P5dc2kZGqlyjuUh8puBI38EH9-ZxjG194Jp8WwD0kWP7HuxBmiXz-5MxSo-pnZso8yhn0RQ1miNkCL0ur989_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfc3d46d0.mp4?token=q94Vab6jZNiBUJAxoDeL1kc6wyMB_mshI8CwaiB24Kii-Y17SEFWly1j5ALFN_YtCNkbKDhGkkoaGgecETOIwpyqRcBIDwvy2FMwE1F2zoPDKhR85guogVsDRfZggvsTDBgeoQQU6FNLBH1304POO4QbSwHStT83-ySMIj7w2_egeNGhpACqBuKfYl71lokuUixi-61-rPTq-D-utIMprZlBp5USUHkr5rlZbVNpQJ2JzujVRGBqnc8AixShECy7P5dc2kZGqlyjuUh8puBI38EH9-ZxjG194Jp8WwD0kWP7HuxBmiXz-5MxSo-pnZso8yhn0RQ1miNkCL0ur989_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهاجرت هزاران غاز برفی؛ نقاشی زنده در آسمان
🪿
🔹
هزاران غاز برفی در آرایشی هماهنگ مهاجرت می‌کنند و آسمان را شبیه یک بازی عظیم وصل کردن نقطه‌ها می‌سازند؛ صحنه‌ای شگفت‌انگیز از طبیعت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/681992" target="_blank">📅 17:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681988">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fac94c09.mp4?token=lIwnJa1Tc9y7jPZ0zWYJLrSEDMxrQWY7lD4SfR61sg3M0fiwQcjAYrT6uRg4kX29BXuA69IkPhKo6ZXUP3PZbKdklnmzBDUUR3arut2zczch78xCUBPL_dioo2J6AMqCzFpN7ma6fmoY_s9z4U_WMLQF29OQXJ625BuSHa_-tqb2dNoo6dIttlNR5vAvlLKCq1F2FXH75EeAlbjlo4xUsvl-4n1thLaBttB8ODYwpusBaRaWgxaqUCXKiGbmQXXq5mSv4M3JDPxp_Sdq9ZSWvq8qPpe7pTy1cpwT6gBcQFQVe8ezTRlyviW78kBwqnfqGFsMXsLEafV4KLKzrsDirQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fac94c09.mp4?token=lIwnJa1Tc9y7jPZ0zWYJLrSEDMxrQWY7lD4SfR61sg3M0fiwQcjAYrT6uRg4kX29BXuA69IkPhKo6ZXUP3PZbKdklnmzBDUUR3arut2zczch78xCUBPL_dioo2J6AMqCzFpN7ma6fmoY_s9z4U_WMLQF29OQXJ625BuSHa_-tqb2dNoo6dIttlNR5vAvlLKCq1F2FXH75EeAlbjlo4xUsvl-4n1thLaBttB8ODYwpusBaRaWgxaqUCXKiGbmQXXq5mSv4M3JDPxp_Sdq9ZSWvq8qPpe7pTy1cpwT6gBcQFQVe8ezTRlyviW78kBwqnfqGFsMXsLEafV4KLKzrsDirQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای سربازهای آمریکایی در آمده است
‌سرباز آمریکایی:
🔹
ما وارد جنگی شدیم که هیچ‌کس آنرا نمی‌خواست، جنگ با کشوری که تهدیدی برای ایالات متحده نداشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/681988" target="_blank">📅 17:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681987">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b10a7b718.mp4?token=YUcDmyMfATkk-wJvGhgmLlG1Vy0T24XMFmILvzLyrLca51ttMlSym8QdFUL-knFeaatfycKwIOgvQ4Mrv-BIH-Y1ygsKxwk0C18Bm7bej0qa59DMXtde7xeBn0_jksZ2h21DN5mDfnculvIN-yPifyfSkZymoaqGyv8-cXLX6EytGoW2OTHVaMRsZJKOHbr475E1Y3-Ui3qIvAUSVbWL2WZG9CKHzEvV4OVQc8RSR23KD31Q_aSiIwxoLrjp9YkilIDpSAvZ1Y-AjuJBG9Ia1bGCWILIot3-XAnQG2AozA0hJ8i7oEHN3mNZj3WblujJrnECXxmiPM0SFmkhw4CjGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b10a7b718.mp4?token=YUcDmyMfATkk-wJvGhgmLlG1Vy0T24XMFmILvzLyrLca51ttMlSym8QdFUL-knFeaatfycKwIOgvQ4Mrv-BIH-Y1ygsKxwk0C18Bm7bej0qa59DMXtde7xeBn0_jksZ2h21DN5mDfnculvIN-yPifyfSkZymoaqGyv8-cXLX6EytGoW2OTHVaMRsZJKOHbr475E1Y3-Ui3qIvAUSVbWL2WZG9CKHzEvV4OVQc8RSR23KD31Q_aSiIwxoLrjp9YkilIDpSAvZ1Y-AjuJBG9Ia1bGCWILIot3-XAnQG2AozA0hJ8i7oEHN3mNZj3WblujJrnECXxmiPM0SFmkhw4CjGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ترفند حتما به‌کارت میاد؛ برش دادن چسب‌های پهن بدون قیچی
✌️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/681987" target="_blank">📅 17:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681986">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
رویترز: تنگه هرمز قابل جایگزینی نیست
🔹
جایگزینی مسیر تنگه هرمز با خطوط لوله در کوتاه‌مدت بعید است؛ خط لوله پیشنهادی عراق از مسیر سوریه حداقل ۱۵ میلیارد دلار هزینه و حدود ۴ سال زمان نیاز دارد و سایر خطوط نیز با چالش‌های جدی مواجه‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/681986" target="_blank">📅 17:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681983">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee7e5ed0fa.mp4?token=fO3sZA6URjgocisFwAssox7CqFvglIJnoeT16ml6t-OUvwm7GJyqvAycSKBxqCQRPAjjO2XIs0cyDz87BPqGO3vCgga0HT31Aa5_RK1_4DH620rwn5PluXgmYU_EasOdO9KLG4meJErImF7hAWJ2t2UccwRmq5EOd7nuroqk8Rrp0gaVYlxMwOeYpQQJGrm6mVlhLak4t0KlHRDnujNZnknkCZaRqv9lvGvGbQvYy5Kjhfg6KgYqlu8AWakQlfH4bIfoIhywbZAXOlQcYgCHL7hx-dvDNVH3NNxG-E4mUDANrARGm1A4yRlMVe3kkBVuwaqRxKlS8RUyXxs5sBmU4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee7e5ed0fa.mp4?token=fO3sZA6URjgocisFwAssox7CqFvglIJnoeT16ml6t-OUvwm7GJyqvAycSKBxqCQRPAjjO2XIs0cyDz87BPqGO3vCgga0HT31Aa5_RK1_4DH620rwn5PluXgmYU_EasOdO9KLG4meJErImF7hAWJ2t2UccwRmq5EOd7nuroqk8Rrp0gaVYlxMwOeYpQQJGrm6mVlhLak4t0KlHRDnujNZnknkCZaRqv9lvGvGbQvYy5Kjhfg6KgYqlu8AWakQlfH4bIfoIhywbZAXOlQcYgCHL7hx-dvDNVH3NNxG-E4mUDANrARGm1A4yRlMVe3kkBVuwaqRxKlS8RUyXxs5sBmU4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پل ورسک، مازندران
🇮🇷
#ایران_زیبا
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/681983" target="_blank">📅 16:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681981">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال: ایران برای گسترش جنگ آماده می‌شود
🔹
ایران در دوره اخیر، ضمن افزایش تولید موشک و پهپاد، نیروهای سپاه را برای هماهنگی با گروه‌های همسو در یمن، عراق و لبنان اعزام کرده تا برای احتمال گسترش درگیری در منطقه آماده شوند.
🔹
این روزنامه همچنین از تقویت ساختار فرماندهی نظامی ایران و آمادگی تهران برای یک درگیری طولانی‌تر خبر داده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/681981" target="_blank">📅 16:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681978">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای ترامپ: ما مستقیما با مقامات سپاه در ایران صحبت می‌کنیم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/681978" target="_blank">📅 16:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681975">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d9bf50f4e.mp4?token=OFbwdI3gMrFiFz-Ioxbbb4DRlGN3wUs5nkoqeqnP49S26Z4Mje07LktQ2jKOkL0r6fcU6HoWMAS3tfNWAcCxLbrOCrEaxT-bHOWbcyKWt6XQwg7vgQ_cjbye7ogUwta3GDFQedVH0dRGc2ZVLJemA5ZgdnV7vWPjeX1AYb8zNYlEj-KG3h0pU3SNB0YayRr-MtigzYDD-ezJafvx3mnGrswGd-vVHG-G3nWrLcY56dYkZ3vxOD0v715RkflHQ4A1ulrDzLbnloSPxjUmu58m66cXUle0lcyjIr_cs4N7ZIGZyTFZsPhwfptGsc6tqvbrBLa4x0bBcOQFmeJ7ZjDzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d9bf50f4e.mp4?token=OFbwdI3gMrFiFz-Ioxbbb4DRlGN3wUs5nkoqeqnP49S26Z4Mje07LktQ2jKOkL0r6fcU6HoWMAS3tfNWAcCxLbrOCrEaxT-bHOWbcyKWt6XQwg7vgQ_cjbye7ogUwta3GDFQedVH0dRGc2ZVLJemA5ZgdnV7vWPjeX1AYb8zNYlEj-KG3h0pU3SNB0YayRr-MtigzYDD-ezJafvx3mnGrswGd-vVHG-G3nWrLcY56dYkZ3vxOD0v715RkflHQ4A1ulrDzLbnloSPxjUmu58m66cXUle0lcyjIr_cs4N7ZIGZyTFZsPhwfptGsc6tqvbrBLa4x0bBcOQFmeJ7ZjDzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفری فراتر از زمان؛ ایده‌ای جذاب سفر در تاریخ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/681975" target="_blank">📅 16:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681971">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0633a32c.mp4?token=YZ4pGqqqv3zW3MdMF-X1Zi_52wWaD2C6ySEveIvVicSIV9_tLq8pkev95NXggpoR1a3L3DdnDuHhNgKpMKxtBJUFhlcF5Ir9YwAYXPDFJ3Wm8c9hj3HRzt3ezN0PQrv-R0yjzXjXX93RaiWRJD5ptIZMAvPgYKBiCtPUrOqPATpOjIt6bm8l3_tbOvNN-T9YFQG3ifJz-jUp3kAqLldR_j35-XecKe0CFoveFdf7qWiXEAE76V46txOtM_llUo8GmWfn0TRMyjKxhW1ZZ8CWtsyrG5clIlcvfDRgcbYefPG-7r_G1xb5QeRUYgZrEndYGQuNDupidElNsJqKsGKiqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0633a32c.mp4?token=YZ4pGqqqv3zW3MdMF-X1Zi_52wWaD2C6ySEveIvVicSIV9_tLq8pkev95NXggpoR1a3L3DdnDuHhNgKpMKxtBJUFhlcF5Ir9YwAYXPDFJ3Wm8c9hj3HRzt3ezN0PQrv-R0yjzXjXX93RaiWRJD5ptIZMAvPgYKBiCtPUrOqPATpOjIt6bm8l3_tbOvNN-T9YFQG3ifJz-jUp3kAqLldR_j35-XecKe0CFoveFdf7qWiXEAE76V46txOtM_llUo8GmWfn0TRMyjKxhW1ZZ8CWtsyrG5clIlcvfDRgcbYefPG-7r_G1xb5QeRUYgZrEndYGQuNDupidElNsJqKsGKiqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این چند عادت، ناخواسته‌ شما رو پولدارتر می‌کنه #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/681971" target="_blank">📅 16:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681970">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpO-U-yL0h_pZT2Cql_o2Y8Oui23hCQbgmeaM67LWfo8VNTHxKciDc71By0JWmBx--YjmY7zKRitkbp_qnWkF91bY2Rvpolk9ZeRy1vj4V6cN4ed24IsQrw3WsSxtpIHgXivjWVzgeHNOdN_rfkp6PdbxpjlYoVwxQMXRnptjT7CWAOae9c-obPBvW95vEP9X4UuvfH3G175xguAoRnYqJml4y0T4xjxtDmXE3JOQPgM43bZ9IroscbUty8cF5L_By_TKQdpVfa2j2coFfw2QQDtlYfdYMgrL2rGHqpNKyke3BAVYvoo7XbqpdYVQVqT1fmv17fcKzLj4Uj98g218A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر جنگ رمضان بر افزایش جهانی قیمت گازوئیل
🔹
پس از آغاز جنگ رمضان و بسته شدن تنگه هرمز، نگرانی از اختلال در عرضه نفت باعث جهش قیمت گازوئیل در بسیاری از کشورهای جهان شد.
🔹
بیشترین افزایش قیمت در کشورهای واردکننده سوخت علی‌الخصوص کشورهای جنوب شرق آسیا دیده شد.
🔹
این جهش قیمت، هزینه حمل‌ونقل و در نتیجه هزینه تولید و توزیع کالاها را افزایش می‌دهد و می‌تواند به موج جدیدی از تورم در اقتصادهای وابسته به واردات سوخت منجر شود.
@amarfact</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/681970" target="_blank">📅 15:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681968">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f238b08db4.mp4?token=Gyo8hFSfz-RJNlA7hSSkWiuCjYJpMTJwUg9X1xNTy1T6QG3V2y1Po4VyHhp3Y0Eb1dVu2W3ZPUQllDqN_kGgSoXC5qspaNCq7cdoLwA9GkWWpaBtaBvA_JG-_AmlCoQmvMmbNIyII3GSXCsyDce1hxM9GwILHYI2loxy4wueW-RX18hwfXxz376hVP-G5a8ZBcOmlnvkp-8AIH4SjkCE0L8nd_wCCXwWn1Hf3XZjr-pRrx4PDY42YPS1jBBTyVxIDi-Q666xvJgFHKyLyzMYSQppJtvPFj4DoOQVANbhe4o3pgJUfwoQqQBN6OROQvvFET1aMYN7gh8SFCUYyTtf1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f238b08db4.mp4?token=Gyo8hFSfz-RJNlA7hSSkWiuCjYJpMTJwUg9X1xNTy1T6QG3V2y1Po4VyHhp3Y0Eb1dVu2W3ZPUQllDqN_kGgSoXC5qspaNCq7cdoLwA9GkWWpaBtaBvA_JG-_AmlCoQmvMmbNIyII3GSXCsyDce1hxM9GwILHYI2loxy4wueW-RX18hwfXxz376hVP-G5a8ZBcOmlnvkp-8AIH4SjkCE0L8nd_wCCXwWn1Hf3XZjr-pRrx4PDY42YPS1jBBTyVxIDi-Q666xvJgFHKyLyzMYSQppJtvPFj4DoOQVANbhe4o3pgJUfwoQqQBN6OROQvvFET1aMYN7gh8SFCUYyTtf1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این روش پوست ماهی‌ها رو راحت‌تر بکن
🐟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/681968" target="_blank">📅 15:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681967">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای یک نماینده: مدیریت عبور کشتی‌ها از تنگه هرمز به ایران واگذار شد
علی احمدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
در آخرین توافق با عمان قرار شد عبور و مرور کشتی‌ها از تنگه هرمز با مدیریت ایران انجام شود و عمان فقط نظاره‌گر باشد، همچنین قرار شده عبور کشتی‌ها از ضلع جنوبی تنگه انجام نشود و مسیر عبور را صرفاً ایران تعیین کند.
🔹
تصمیم‌گیری برای مبلغ دریافتی از کشتی‌ها به عنوان عوارض عبور از تنگه، درحال انجام است که مدیریت این طرح بر عهده ستاد کل نیروهای مسلح است و وزارتخانه‌هایی مانند وزارت خارجه نیز با ستاد کل همکاری خواهند کرد.
🔹
عمان نیز از این عوارض دریافتی، بهره می‌برد اما سهم ایران از عمان بیشتر خواهد بود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/681967" target="_blank">📅 15:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681964">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079fc18e6e.mp4?token=DJseTqY0Mf9kg2lhAcAITMrKOgUC4v-7q1kxzkXA4e5cDf9Hrzx_jKmyTbsrPW5FZPV9ns-Qj5svgRPDR8KtzlqLMqhw7Wc0MXkz96zVnshs1SyTcFjcSL5x703NDLjYd0Mu67cnL0AZXYF4MKOCs8ZuhJS6j9FRnUgqgZKLTnQCqj-szxCj9OY7ohUCR3XKrLHaJ1cxQ9RmyXMP2TrRPNbYbs83LgQBHRuv3OTpsQr9BDuYErtWywmwYWZX8UdMR_QUzfu5QO3qwjkjmv-9H5fvzcBNLAldjc7QX8XfITT4LzLqA6f4zowIIdOAW77pCayDj6DKoYQGhjBy8a6CjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079fc18e6e.mp4?token=DJseTqY0Mf9kg2lhAcAITMrKOgUC4v-7q1kxzkXA4e5cDf9Hrzx_jKmyTbsrPW5FZPV9ns-Qj5svgRPDR8KtzlqLMqhw7Wc0MXkz96zVnshs1SyTcFjcSL5x703NDLjYd0Mu67cnL0AZXYF4MKOCs8ZuhJS6j9FRnUgqgZKLTnQCqj-szxCj9OY7ohUCR3XKrLHaJ1cxQ9RmyXMP2TrRPNbYbs83LgQBHRuv3OTpsQr9BDuYErtWywmwYWZX8UdMR_QUzfu5QO3qwjkjmv-9H5fvzcBNLAldjc7QX8XfITT4LzLqA6f4zowIIdOAW77pCayDj6DKoYQGhjBy8a6CjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران حسی عمیق، شبیه افتخار، شبیه دلتنگی، شبیه دوست داشتنِ وطنی که هر گوشه‌اش، بخشی از جان ماست
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/681964" target="_blank">📅 15:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681961">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
جزئیات طرح اسقاط موتور سیکلت‌ها و خودروهای فرسوده  مدیر ستاد نوسازی ناوگان و اسقاط خودرو فرسوده
🔹
تسهیلات این طرح از ۴۰۰ میلیون تا ۱.۲ میلیارد تومان با نرخ سود ۴ درصد به متقاضیان پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/681961" target="_blank">📅 15:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681960">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa44eb4ce9.mp4?token=FHVWm7f4_N6Bp0aof2C7EQsmxY7B6sPIzYgk8cS0gc5qXtRZljw_ZQWomkaw0JAJbSM2_5Lszjw1X72_rcN5OJHOtJy-rDaGqlWXVAxlee9p9IsUDYC4Bx1d6IQy2byj500s3OvZDLwLMFLnlxxFjiH4WbtSmZqfQGkKUKSK2rszx69hAQadScGNzCIKVptfECXOIJ0mWuZFE70JtEphrQIT82zoOG0hJrN4GJHhrk5BRYgqed9RuigYk2DWYAlXjtvrW2F1MjHzWipz4m5_ltB5vqDnudp8Cvfs7fcZY6lUfRWbX1-keu3ZiaCWjyu9glXNsPwD8KKu3Dy8NWQ7WXlEXgFotpTa0pBmPRAqdFqNTgzyw_lOidppSpItvxmlAlIB3t4wkKWPV5OswVNdTQ8-6WY4fw6TZZI4fUa7eunsL-oNGmZwlWeEHLuI65e5jrDOk9e84BLXRmTvpjwG4N1f02msH9tNk1eJJtkgDU34GeEKkiowOvST6Zt8lfS4qeQE003HNRRKXoLD4J-H61rqd1t4zF6g_8swWnIn8ScjMbn99c7eOQ00EmIZ7g4skvrTbo3mNdkYqC6XPSMEuoipI3Ky9VO0J1h-daIdMABHFGJTHbQ9EB-mPBatZahecu9WuJObu-rI-AQFeiVCAn_y1ZOZ2nIwFkda2d0aoFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa44eb4ce9.mp4?token=FHVWm7f4_N6Bp0aof2C7EQsmxY7B6sPIzYgk8cS0gc5qXtRZljw_ZQWomkaw0JAJbSM2_5Lszjw1X72_rcN5OJHOtJy-rDaGqlWXVAxlee9p9IsUDYC4Bx1d6IQy2byj500s3OvZDLwLMFLnlxxFjiH4WbtSmZqfQGkKUKSK2rszx69hAQadScGNzCIKVptfECXOIJ0mWuZFE70JtEphrQIT82zoOG0hJrN4GJHhrk5BRYgqed9RuigYk2DWYAlXjtvrW2F1MjHzWipz4m5_ltB5vqDnudp8Cvfs7fcZY6lUfRWbX1-keu3ZiaCWjyu9glXNsPwD8KKu3Dy8NWQ7WXlEXgFotpTa0pBmPRAqdFqNTgzyw_lOidppSpItvxmlAlIB3t4wkKWPV5OswVNdTQ8-6WY4fw6TZZI4fUa7eunsL-oNGmZwlWeEHLuI65e5jrDOk9e84BLXRmTvpjwG4N1f02msH9tNk1eJJtkgDU34GeEKkiowOvST6Zt8lfS4qeQE003HNRRKXoLD4J-H61rqd1t4zF6g_8swWnIn8ScjMbn99c7eOQ00EmIZ7g4skvrTbo3mNdkYqC6XPSMEuoipI3Ky9VO0J1h-daIdMABHFGJTHbQ9EB-mPBatZahecu9WuJObu-rI-AQFeiVCAn_y1ZOZ2nIwFkda2d0aoFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاید عده‌ای به‌خاطر بازار فیلترشکن بر تداوم فیلترینگ اصرار دارند
نخعی، نماینده مجلس:
🔹
بسیاری از مشکلات فرهنگی حاصل مسائلی است که پلتفرم‌هایی مثل اینستاگرام ایجاد کرده‌اند./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/681960" target="_blank">📅 15:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681958">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuD7qrWYbRiS2vSAHyGYSI1KfNZQd5whnrKOHkEJCDg5RzpS20Q-fXcACMbB2FWoDYdNlXYyNwLqZqnzKbykVZK8XKAvhSoBpDwBgEx2f27_Nrx0P053brJAH7ufXfbsDMru2azKoxuNc2w2220H7Ly_3cDrp4e6TSiCZB_Bx1OMAzMfBn9hLTvE_OHFS9VYfM8giKX2NaU7XmVxdOK-75hwa0O0HIyzYUzEWhzcQNHkHdmws1NsI5fe4qB8BDVye8ET5txkvf2T0K41lC_znO40ac2Wms6pjCYazVW9xV0Djf2bfKMXPcElIZeJew-dqsuV8iPSnDPuslRzq2M_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
خرید اعتباری آهن‌آلات با LC تا ۶ ماه
⚡️
مزایای خرید با LC از آهنگر:
* تأمین انواع آهن‌آلات موردنیاز پروژه
* امکان خرید اعتباری از طریق LC
* مناسب پروژه‌های ساختمانی، صنعتی و عمرانی
* تأمین از منابع معتبر بازار
* پشتیبانی از استعلام تا تأمین و تحویل بار
برای دریافت شرایط فروش LC، سقف اعتبار و استعلام قیمت وارد لینک زیر شوید و فرم را پر کنید.
🌐
ثبت درخواست</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/681958" target="_blank">📅 15:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681957">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a0d5787d.mp4?token=Aprie9L-kaam4iHXFUa43vFfIfD7ZQaIejBtaI1y479AYqDw-FvGpO0B_WkGZ4SVMnPgHmxDpYzFrTIvX_Ju0FR2ILxvfV9Un27zbFbTE2jaXgbapt8wCmHrlIGKbSDfVnxOYZVZnYZzd6JtQJWw2JgQmTq2V-9UN-UBpZKI_CHsDYEuSHcGaN3EiWNCalzCZ4iGe6OjEVvvblqSElr2vuErAKR73_6D4He_TMGV7Uk6JWCZrKgZSnYECFYqyKP9KMtOT7YLLhPt_lNrx3on26JRo9-RIrhrKPyda5o84aCjQNIDu1AktJwFvzgl2Q_yZe8rlKZQUJoTUX7tIUBXvk3PSEtCYSC1r0lg6XF5OJUpGHqB4tcwbkneCUmJLDlqRpi_P97T8jJOfJ9xWtMnZVz8fGikzYvCIO9geJsmQP4tJ8oucAlqMk9o3evhEziJvtA0u53N7sZKjcxiQStmKHglNmoHgxzrfR2u-fhN8_cKTY-cwy4myYpqqOuwSIc24gR95YHiR5bwzP9f--R1ArqQ9iBDg01O6d2dOgj_paNj_JtX4DwHYyVlMMSvP8AkxSayVdxavkmEQatdPXLKGqaSVhboR_jNE6VTfUqsjjPhab3NPDiyeot84bsTfuLJL0ByMNVQ67_YZRbZtp7ujdgeWGfDFfFfUblFIqgBz4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a0d5787d.mp4?token=Aprie9L-kaam4iHXFUa43vFfIfD7ZQaIejBtaI1y479AYqDw-FvGpO0B_WkGZ4SVMnPgHmxDpYzFrTIvX_Ju0FR2ILxvfV9Un27zbFbTE2jaXgbapt8wCmHrlIGKbSDfVnxOYZVZnYZzd6JtQJWw2JgQmTq2V-9UN-UBpZKI_CHsDYEuSHcGaN3EiWNCalzCZ4iGe6OjEVvvblqSElr2vuErAKR73_6D4He_TMGV7Uk6JWCZrKgZSnYECFYqyKP9KMtOT7YLLhPt_lNrx3on26JRo9-RIrhrKPyda5o84aCjQNIDu1AktJwFvzgl2Q_yZe8rlKZQUJoTUX7tIUBXvk3PSEtCYSC1r0lg6XF5OJUpGHqB4tcwbkneCUmJLDlqRpi_P97T8jJOfJ9xWtMnZVz8fGikzYvCIO9geJsmQP4tJ8oucAlqMk9o3evhEziJvtA0u53N7sZKjcxiQStmKHglNmoHgxzrfR2u-fhN8_cKTY-cwy4myYpqqOuwSIc24gR95YHiR5bwzP9f--R1ArqQ9iBDg01O6d2dOgj_paNj_JtX4DwHYyVlMMSvP8AkxSayVdxavkmEQatdPXLKGqaSVhboR_jNE6VTfUqsjjPhab3NPDiyeot84bsTfuLJL0ByMNVQ67_YZRbZtp7ujdgeWGfDFfFfUblFIqgBz4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی می‌گوییم یک نفر ADHD دارد به چه معناست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/681957" target="_blank">📅 15:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681956">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP5C1dBHwfEyyDMx-7VTmxciwpheH1pmTNvUbfyN8MoR3dOvrmfWdKpHiJQj1p1xLXqCOlnx3eaCB2BJcko9gDVVYewGWquIdMWfnuhhdflxdvC9QSApOBnYnjERicZF1MVCdrAVpPb9EGpAjLrXbAPnFrktkatgb01ULHiVhHmaUftKo7AcXpGYKJ77rbjfJ-gupqy6pbof-bUV7GsKMhbk4M2lTnFYuH7osN9o2u4rnfQSyJ3j88iVMs7yYdweF9qm7mUGeJ-JOn1QsDCC3Vd20s5wSuc6YR0_Q9cvXdFZ4i4LZnGoxiL16iZl7V9GbJD1NXHb6Kt3rWjTd6RNgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش ۵۵ درصدی ارزبری بازار تلفن همراه
🔸
قیمت موبایل در سال ۱۴۰۵ بین ۳۰ تا ۸۰ درصد افزایش یافته و ادامه وضعیت فعلی، اشتغال مستقیم ۲۰ هزار نفر را تهدید می‌کند.
🔸
ارزبری بازار موبایل از ۴ میلیارد دلار در سال ۱۴۰۰ به ۱.۸ میلیارد دلار در سال ۱۴۰۳ کاهش یافته است.
@amarfact</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/681956" target="_blank">📅 14:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681955">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9189453b.mp4?token=IuCqHIYZXIt5dXslSVHhZfZoaKJ887kcZkLE2a-6utahSlfC0KI9gu1u8AZKHJi-zdA6lhrObE4jby0B_ULnHWamC6Re1fWV_JYZxzf3ZQyCx9Et1NYxQsLpRe9GDLkOa886YTKkKMrk4V7WgCOxVDCVkatcC1zvZ753GpsDz5ZuFUs3rENfg76655yQiPpV_J8Q2kvv4wZMPTGn87Hhkg1N8oUtRLTjXHXFbKNJ26kNF61eTBfZeRg_uan_x_M6fwicYR-zGbiPtyXthKBsmSX9BMkGOByuCNyz-tNKT2uDGOCGrGZZyf37xg5vBtyd8t6HdDAxpx7aZGBJnQOVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9189453b.mp4?token=IuCqHIYZXIt5dXslSVHhZfZoaKJ887kcZkLE2a-6utahSlfC0KI9gu1u8AZKHJi-zdA6lhrObE4jby0B_ULnHWamC6Re1fWV_JYZxzf3ZQyCx9Et1NYxQsLpRe9GDLkOa886YTKkKMrk4V7WgCOxVDCVkatcC1zvZ753GpsDz5ZuFUs3rENfg76655yQiPpV_J8Q2kvv4wZMPTGn87Hhkg1N8oUtRLTjXHXFbKNJ26kNF61eTBfZeRg_uan_x_M6fwicYR-zGbiPtyXthKBsmSX9BMkGOByuCNyz-tNKT2uDGOCGrGZZyf37xg5vBtyd8t6HdDAxpx7aZGBJnQOVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ما مستقیما با مقامات سپاه در ایران صحبت می‌کنیم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/681955" target="_blank">📅 14:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681951">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8966be94.mp4?token=XmNWRVPwoNocZnbd-LnY4ZeCQP4DvZwFf5T-LTqb1duXQjggptpkD0g3H5XOH_wA6sM2-j2XKW4oXZ3C1Ro43tO8AbMURdeWQHTlyADkAoJmBPrl1DsHi2ANWyUkZrwnnsyCdTKUp7m4yaZ8LQ3Kil5XzmBMNxknzNu-n9dyE3T4nyf1egAYHZIdD1IxgA8ODHDXmB36ZBJiuFthVohLvsjC0lHfBlgmvo9wWqAWHN1IrEGD7clQTLwzpQ6wC6lPNu5VeLwC_gAGVsDMZTENZuWJqFZTF-JtkgzIYwiP4EaMOTNGtNWdyxjgirLbQfADdDySHJNtm4pFv5Y-8NEJOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8966be94.mp4?token=XmNWRVPwoNocZnbd-LnY4ZeCQP4DvZwFf5T-LTqb1duXQjggptpkD0g3H5XOH_wA6sM2-j2XKW4oXZ3C1Ro43tO8AbMURdeWQHTlyADkAoJmBPrl1DsHi2ANWyUkZrwnnsyCdTKUp7m4yaZ8LQ3Kil5XzmBMNxknzNu-n9dyE3T4nyf1egAYHZIdD1IxgA8ODHDXmB36ZBJiuFthVohLvsjC0lHfBlgmvo9wWqAWHN1IrEGD7clQTLwzpQ6wC6lPNu5VeLwC_gAGVsDMZTENZuWJqFZTF-JtkgzIYwiP4EaMOTNGtNWdyxjgirLbQfADdDySHJNtm4pFv5Y-8NEJOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هفت بخیه ساده، یک پاپیون دوست‌داشتنی؛ هنر گلدوزی در چند دقیقه
🎀
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/681951" target="_blank">📅 14:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681950">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
چند خزانه، یک واقعیت: انحصار خزانه در بازار آنلاین طلا تمام نشده است
🔹
بانک مرکزی سرانجام امکان استفاده از چند خزانه برای سکوهای آنلاین طلا را پذیرفته و بانک‌های ملت و سامان مجوز خزانه‌داری گرفته‌اند؛ صادرات و کارآفرین هم در صف‌اند.
🔹
اما مسئله اصلی هنوز حل نشده: سکوها فعلاً امکان استفاده عملی از این خزانه‌های جدید را ندارند.
🔹
یعنی روی کاغذ انحصار بانک کارگشایی شکسته شده، اما در عمل پلتفرم‌ها همچنان با همان ساختار قبلی کار می‌کنند.
🔹
گرفتن مجوز خزانه یک مرحله است؛ اتصال به سامانه ناظر، ایجاد زیرساخت فنی و امنیتی و فراهم شدن امکان قرارداد و انتقال واقعی طلا، حلقه‌های بعدی این زنجیره‌اند./ پیوست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/681950" target="_blank">📅 14:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681949">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ترامپ: عمان را در صورت دخالت در مذاکرات ایران بمباران می‌شود
🔹
ترامپ در مصاحبه با فاکس نیوز در پاسخ به سوالی درباره نقش عمان در مذاکرات مربوط به ایران و تنگه هرمز گفت: «اگر عمان مانع شود، آنها را بمباران خواهیم کرد.»
🔹
ایران روز شنبه اعلام کرد که پس از هفته‌ها مذاکرات فنی، با عمان در مورد نقشه مسیر کشتیرانی تنگه هرمز به توافق رسیده است./ خبرفوری
#Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/681949" target="_blank">📅 14:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681947">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d621b4d8d1.mp4?token=jPspYxMjPzl67-gomILyO8njKTovF1zoh_X1bHanCZsSNJY1OEFWOWTuyDlovyPfCY92nLhsLF8W6WyTsgiRbvliS9l43nIBooPFYmyFB3DIn7KfYBgIHldz9etLWvzQ9o_cu9wT26Rj-bOUzXPSrhhASwJmyJYjhB9hCQAuIIgx9HUUD4vvKTACne8_l3-VhmN_4rrZpkaeaTXnugsG9MiG49qqaHUwG1q2Fd-19mGqJYPrWKcO_VF1zVAJTQ3J671Q_aZTKTP__7ONbakp6NNjb-ddsMpPrYy4m1_SEnCJkA6ufRjbd59XTHxc66rjdN6x0IYi7acJ02o_R6HFloWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d621b4d8d1.mp4?token=jPspYxMjPzl67-gomILyO8njKTovF1zoh_X1bHanCZsSNJY1OEFWOWTuyDlovyPfCY92nLhsLF8W6WyTsgiRbvliS9l43nIBooPFYmyFB3DIn7KfYBgIHldz9etLWvzQ9o_cu9wT26Rj-bOUzXPSrhhASwJmyJYjhB9hCQAuIIgx9HUUD4vvKTACne8_l3-VhmN_4rrZpkaeaTXnugsG9MiG49qqaHUwG1q2Fd-19mGqJYPrWKcO_VF1zVAJTQ3J671Q_aZTKTP__7ONbakp6NNjb-ddsMpPrYy4m1_SEnCJkA6ufRjbd59XTHxc66rjdN6x0IYi7acJ02o_R6HFloWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خشکسالی بی‌سابقه در هلند؛ راین به پایین‌ترین سطح تاریخی رسید
🔹
دبی رود راین در هلند به ۶۱۵ مترمکعب بر ثانیه رسیده؛ کمترین میزان ثبت‌شده در این کشور که منابع آب و حمل‌ونقل رودخانه‌ای را تحت تأثیر قرار داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/681947" target="_blank">📅 14:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681945">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uClQ72cj9dAx8rOzIVOXcGQ3SzxfgphTyx_vVNvCPc0ITaSiiGZM5WUEMyIoclFhvUCRB8Lf6pAEA5AUTJj6gINW5Thk6k-0xo_sFr1OusT4dsY4qL_FN3U7sM6lFYadlyEDAjmLt6gPhf2jOpX9taCdhAoykuyTD6vavKFdB0EmHyzB3ZitTlsbXKrM8b2EXSKkRH77iQtt_7uvhYN4UOJjPSTq-UwlIFuEJgSGBDoLPCcC7iDn1ZihPeLU6cPxk0-GUi9sv6Z7_Y6l_3XRaoss1kPbDBSC0mSSWYDaQ97q37lAC5wskesgvnM9GIy7mROozafO00PCWYFPWipDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش توییتری بازیگر مشهور نسبت به سکوت در برابر نسل‌کشی غزه
لیام کانینگهام، بازیگر مطرح سریال "گیم آف ترونز":
🔹
اگر از خودت می‌پرسی چرا دنیا برای متوقف کردن نسل‌کشی در غزه کاری نمی‌کند، اما خودت تا الان در این باره حرفی نزده‌ای، بدان که سکوت تو را به‌منزله تأیید تلقی می‌کنند. فرقی نمی‌کند دو فالوور داشته باشی یا دو میلیون؛ حرفت را بزن، لعنتی! سکوت یعنی همدستی.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/681945" target="_blank">📅 14:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681943">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7399b39d67.mp4?token=NP-YToJkVMValSmliS1lSceHck3jDHNyXO_trNXKTESSX7BCyOkhpOml4vRx0rBcP2UGySZ4e0yyBjjmZz6nAoX7no-tYOEiJ5AacEiLd2-2PiyuzQk3lRPMZw_Gj-uy6Jj-wXQFeOzfzqHGctPZWsS6AU9-a70KtgikwPF_9-Juxz0h6-ucENVXvAD_9iUbkcYgEgCvUtgrbzt7tp509psV1g4J-EIscBc3AssORja_0RWiwXgyx6Vx8202lMgX5D37UP8WrT7omeTAQU8t6G_4PyCSztc2OCogpd2yjljP_ckHjW_C1VnwpM41dShuiSGxYp2cYNBIBP2pFyfDXgYAc2oh231J2VEFtTqG3dItMIPfnU0LnC5KW-mlRf9wyvBNYuoQrOIExHSl81ul-xuKTTBhlOWfIfjKxCGt81_jUYlexrqrJkijWz4s6Bwi0kpQ27ZJax94WVePrp1xNmXOd_IWc2gNXO2wimEqT6AC_KECQ_m4GU74pCqNWQ3bRei9vkH7jg5vrUdF3K3v8L1FpNUnDn8aIEc1xl8KGHzSdluWon3n72Ri2W-sMPgeqTl0TKUwlwFjG-e6p3uEQe3zxhFv6EB-z_6U53yAatAt9XQbx8LYVKqqLrUQRcULcMkb_2YNR_4kgXX7p4IEznW9jttSQ33msLeml1WpzgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7399b39d67.mp4?token=NP-YToJkVMValSmliS1lSceHck3jDHNyXO_trNXKTESSX7BCyOkhpOml4vRx0rBcP2UGySZ4e0yyBjjmZz6nAoX7no-tYOEiJ5AacEiLd2-2PiyuzQk3lRPMZw_Gj-uy6Jj-wXQFeOzfzqHGctPZWsS6AU9-a70KtgikwPF_9-Juxz0h6-ucENVXvAD_9iUbkcYgEgCvUtgrbzt7tp509psV1g4J-EIscBc3AssORja_0RWiwXgyx6Vx8202lMgX5D37UP8WrT7omeTAQU8t6G_4PyCSztc2OCogpd2yjljP_ckHjW_C1VnwpM41dShuiSGxYp2cYNBIBP2pFyfDXgYAc2oh231J2VEFtTqG3dItMIPfnU0LnC5KW-mlRf9wyvBNYuoQrOIExHSl81ul-xuKTTBhlOWfIfjKxCGt81_jUYlexrqrJkijWz4s6Bwi0kpQ27ZJax94WVePrp1xNmXOd_IWc2gNXO2wimEqT6AC_KECQ_m4GU74pCqNWQ3bRei9vkH7jg5vrUdF3K3v8L1FpNUnDn8aIEc1xl8KGHzSdluWon3n72Ri2W-sMPgeqTl0TKUwlwFjG-e6p3uEQe3zxhFv6EB-z_6U53yAatAt9XQbx8LYVKqqLrUQRcULcMkb_2YNR_4kgXX7p4IEznW9jttSQ33msLeml1WpzgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوکیا N93؛ یکی از گوشی‌های پیشرفته زمان خود
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/681943" target="_blank">📅 13:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681940">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f17673114.mp4?token=qiefUymhhDeifHw9GVj-gC-iuDBwSUNUE0ao662NoymezxFoNPB7FMyql6xK35gSPzipK7ZKXeTqgMt9MJlB3pI7FG_T7Bhl96IsGhyn4iYKZ7HMtbKrxGETNIqsxPffAMoskv59kGsvkowDqbd9SOU836_gKvuxnkY9MEEUgDn9ivUxOmYG91iibmmw1N0wXRyPkvrJRx2keuALKlTH4_YL7TYZO0ajhOz-W-vpEDPFYsb6p529m0mmoWkVaYsh2J00v3wJ2mqSt9wV24ezwWvuhnI12yeOqbnfAlOfW0eqgM46deqjBKSrKOXa0iqjBE02-iU1kP6OK94APO1SzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f17673114.mp4?token=qiefUymhhDeifHw9GVj-gC-iuDBwSUNUE0ao662NoymezxFoNPB7FMyql6xK35gSPzipK7ZKXeTqgMt9MJlB3pI7FG_T7Bhl96IsGhyn4iYKZ7HMtbKrxGETNIqsxPffAMoskv59kGsvkowDqbd9SOU836_gKvuxnkY9MEEUgDn9ivUxOmYG91iibmmw1N0wXRyPkvrJRx2keuALKlTH4_YL7TYZO0ajhOz-W-vpEDPFYsb6p529m0mmoWkVaYsh2J00v3wJ2mqSt9wV24ezwWvuhnI12yeOqbnfAlOfW0eqgM46deqjBKSrKOXa0iqjBE02-iU1kP6OK94APO1SzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن اولین عبادت یک دختر ایرانی؛ ویدیویی که در فضای مجازی پربازدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/681940" target="_blank">📅 13:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681939">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF9o7FaWC_98v7zRVnGoyvnOmPLUAER1Bou6Tpfd50PPUNpbsOra4_9AfYvJH9sJMOGZz_XKW4YKmiCK6MeC94aBQ7Fn09Gf9UnzDX8JACMbgp3TKzpJH2sW0YAqStkCib8Rdi7xvytyFS-CVOznHKXl8lvOda7SeWW0H5xWqQjoF6TYKYW76ybgZ--nUgcpb3bIzXcBLxEjOH_OuhfMNQF1qhUhNN4ZTl-KA_lOqhQ_IR9vGdUEvDkN3bQsrXb-tes3LvyLHSzGEFVJNMXc9ifrNAWrwDzIkA2-q10VSyv54m5QAElGz7-bTMr77fVsWHrLw_wQejVPz0zok7tpww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکسی که یک ملوان آمریکایی از کشتی جورج واشنگتن به اشتراک گذاشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/681939" target="_blank">📅 13:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681937">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf402f74e.mp4?token=B016RPaOguSIKoULvcQwivYXo1EufZa8OVkGLNbqPVoX6tz9g-_v20H-VBHiq5vx97uCNIFlgLlkqvyDGEDq7f2RvMSaztdjGBofWjMNzrjXqZni6qVoJb4hkjpZ28rcbphMCqGRTUguFrhNrSRfPUcvV3B3eKp6Pum5kwG3iiipqx-U42sUJWIaZi1BH_iV5eYdDu43RbLX4FIB3Oaw52_uBb3yrwIswUPyI-WKje1no5xrgtiB0vjxuuKv_-vCS_R31meXxEW4PWs83xz55cMjSiOHQTdq7uty0BwOaZXJIafJ1ekEKxR-7wlQTH3FBZb3sDLyXFtqqYgYFXSvDYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf402f74e.mp4?token=B016RPaOguSIKoULvcQwivYXo1EufZa8OVkGLNbqPVoX6tz9g-_v20H-VBHiq5vx97uCNIFlgLlkqvyDGEDq7f2RvMSaztdjGBofWjMNzrjXqZni6qVoJb4hkjpZ28rcbphMCqGRTUguFrhNrSRfPUcvV3B3eKp6Pum5kwG3iiipqx-U42sUJWIaZi1BH_iV5eYdDu43RbLX4FIB3Oaw52_uBb3yrwIswUPyI-WKje1no5xrgtiB0vjxuuKv_-vCS_R31meXxEW4PWs83xz55cMjSiOHQTdq7uty0BwOaZXJIafJ1ekEKxR-7wlQTH3FBZb3sDLyXFtqqYgYFXSvDYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«چند روز مانده به کنکور؛ بخوانیم یا استراحت کنیم؟»
محبی، روانشناس:
🔹
راهِ درست در روزهای پایانی منتهی به کنکور، یک جمع‌بندیِ هوشمندانه است: حلِ یکی‌ دو آزمونِ جامع، مرورِ مطالبِ مسلط، و تمرکز بر مدیریتِ استرس، تمرکز، حافظه و تکنیکِ آزمون./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/681937" target="_blank">📅 13:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681936">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde605370a.mp4?token=HL7MK49qhmIR-1JpIVRam4jYWPSuFKATohiO6DKLf5uxPhegD03oACBnzbkUWswbZvc0u9lTAhA5opYG00x1rheU9oUofsGt-DB7QDRe4_wfgifsHBgXUcG8rvXLldXpMIhhWv-TXrqPMUDE93MRYo81DKehhxZxWw9d8v_9QMIGmdHMZvHsMej17ULFcsoAmeTVLe_3v-Miv8tkuRJ-JzOzR70au_ZDXkEYmepQuENuHqULl6EoqpPOuznbHdTtEYc9poSUxw2prTIvIkKnXAloROT8WBzF5dlCEA8DUzi_7ZFoxf8kAA9tD-7KThtjzlSU6uWinbkknA5HeAjzlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde605370a.mp4?token=HL7MK49qhmIR-1JpIVRam4jYWPSuFKATohiO6DKLf5uxPhegD03oACBnzbkUWswbZvc0u9lTAhA5opYG00x1rheU9oUofsGt-DB7QDRe4_wfgifsHBgXUcG8rvXLldXpMIhhWv-TXrqPMUDE93MRYo81DKehhxZxWw9d8v_9QMIGmdHMZvHsMej17ULFcsoAmeTVLe_3v-Miv8tkuRJ-JzOzR70au_ZDXkEYmepQuENuHqULl6EoqpPOuznbHdTtEYc9poSUxw2prTIvIkKnXAloROT8WBzF5dlCEA8DUzi_7ZFoxf8kAA9tD-7KThtjzlSU6uWinbkknA5HeAjzlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز ناتمام یک مسافر صهیونیست
🔹
یک شرکت هواپیمایی آمریکایی یک مسافر اسرائیلی را به دلیل اظهارات نامناسب درباره غزه از پرواز خود اخراج کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/681936" target="_blank">📅 13:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681935">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe61f8ddb.mp4?token=S5aFDMU8BLSJ1Wf1JWWOZcmCr6MBHVKpEDJssCOYF7EYOaD63bo_pJHQuOs8isW1GBC2ceK2fKns0CYTv2ZPkXJ13RXNZP_0UlFYVSd2am9JdkLUW7ppp5dOAAUjeAv3irTbtromOPif4f5-sbOsX-jpYyI30r_WJkjbx_r6SMmTuastqWJGHUz-uBz82ehLDbIseXWGls9fELQuTkk5keG8a58ensMkwCyDERMD3x-dIOKQGeqBSpC3Mpa-iisGmTFXPpM35x-pgxCfUAPMhyOn9_YgXTDos3hbFKzgSff_DEP9akTw1p8p_KxXoKi91iQ9L0FbqybRWA7xn46I6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe61f8ddb.mp4?token=S5aFDMU8BLSJ1Wf1JWWOZcmCr6MBHVKpEDJssCOYF7EYOaD63bo_pJHQuOs8isW1GBC2ceK2fKns0CYTv2ZPkXJ13RXNZP_0UlFYVSd2am9JdkLUW7ppp5dOAAUjeAv3irTbtromOPif4f5-sbOsX-jpYyI30r_WJkjbx_r6SMmTuastqWJGHUz-uBz82ehLDbIseXWGls9fELQuTkk5keG8a58ensMkwCyDERMD3x-dIOKQGeqBSpC3Mpa-iisGmTFXPpM35x-pgxCfUAPMhyOn9_YgXTDos3hbFKzgSff_DEP9akTw1p8p_KxXoKi91iQ9L0FbqybRWA7xn46I6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی پربازدید از تلاش یک خرگوش برای نجات دوستش
🐰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/681935" target="_blank">📅 13:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681933">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI9jx4yGPcsX_lUWKs0IyQiEtO22kv4g2mZvvH7910C7zbdb0ZpnCyVuut80cbHl27L7KpxgeI489W66hFZe95XfQKotLIQtCRuZFkTnppwmbiXh1t0_MZ7PpYeUcEqYjZafBjtZYyfjZNGrikKAVq82rmQDFwMTa2HueG0K8oq2Y_H4100Ug0A1HuwiEsGjO78h_o1YFmrh4X_-3fsci8_89ojLxDpPQuSWxMnWIGPGmjyJ3IGfmLkvbOzy55pdwGhihmqtDfUDARKF0LpBlYsR8LUQ2fd7khP82D7fXS_LDDOSxVD7Y8VE8gSMFktGS5Af4IOmpgAnoVOVYfELKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رئیس اقلیم کردستان عراق: دفترم هدف حمله پهپادی ایران قرار گرفت
🔹
مسرور بارزانی، رئیس دولت اقلیم کردستان، مدعی شد دفتر شخصی او در حملات پهپادی ایران هدف قرار گرفته است. مقر رئیس سازمان امنیت اقلیم کردستان نیز هدف این حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/681933" target="_blank">📅 13:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681931">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch8y43Nge8g36iVmrpOKCukFyLDAvnT2a3KaKZgJdeLjsx0StXQBobdTdD5iCHoOX0p5f8-64LhGf_m9hD1mbyLEllAV7i8S7_vg8g_S5P3_-ptJwnGYccKvpJysTanuxQk2LzGmg1dvBr5cC-0um_N8jKjebezPiRFs250mBV_24ecxxJorFnzCc72HDaVYMhlYGwTjgv7dU9mtDDyEIjfJl8vKiY-BAoIjaJ6x7fASEfqkhyL8rluev8P7rbWGh2-5tTPQ5S2Ew484zlPzh-BqFkhuI7exSlvPF37BE_xxZNaX3NtYo6pjmHSgLKnqf3z3iJheN7_slxAWFNJmZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۶ مرداد ۱۴۰۵؛ ساعت ۱۲:۵۰
🔹
دلار امروز بدون تغییر روی ۱۸۶ هزار تومان ماند و پایان آتش‌بس ۶۰ روزه ایران و آمریکا هم واکنشی در بازار ایجاد نکرد.
🔹
تحلیلگران این بی‌تفاوتی را نتیجه آن می‌دانند که در دوران آتش‌بس نیز درگیری‌ها کاملاً متوقف نشده بود و عملاً آتش‌بس واقعی برقرار نبود؛ به همین دلیل پایان آن هم نتوانست نگاه معامله‌گران را تغییر دهد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/681931" target="_blank">📅 12:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681930">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af73a7afe.mp4?token=LqEMezyrOvC3RhaFW2NUxRt9Qj5B73MhYEbMpr7wO1lBLt-r4cjv7HKhkC77CfDBf1I8V9hbEnHBICYGCS_oTvqKeE2XpRDUrgyl4oWd1dvTnB5yU2aptGf0YYAv1V2C2Mgs0UwfrwiitDt5kILP_GwCMwIc3FJAujk_tllmVyXENchZXbg86p3JkgJn6pjQgnKdxRNtfE5AEYZx1GWRw-GVskc4JPsCcS-52b9xcXX9XMIfWBqTDjGisjr4NX5JhwnhaXiLKQtHQJWZjks7QNh3zmRY4GyE89K8obDWMU2YFI6k8aVfa4pN663uMnHTiqjPhu1up64aipc4zRZsvAMjmhpGOopMpHl5_-TretbEKEWMSgVCtyY0n4twvB_HwBlK8UWSAaSy0joC60IqCGOz3kCruWCAcFuDmBZpbREuj4RiveKD8Bmp-pQCkFZQxz6G8sWehMr22OqWh-AmgKq3ovqs3aQQUHlSApplmUWK02MJQdhr_IMkIpbIcOCLIOYd71GAcIemTwxrhEXUbM0AHnhTOw5ukMOXPPEEe3zIg_3tY8PlgrEGpH_rjvemanH-V5DVaQrl0V6988yw23oi6jdfmqzquR4u9seoEkB6MPNQFbjns9yB9rAK6ZjYkxRObdxJ0T4OMon3pH7P3PMprIRQN9Gnjub4pNGc0KU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af73a7afe.mp4?token=LqEMezyrOvC3RhaFW2NUxRt9Qj5B73MhYEbMpr7wO1lBLt-r4cjv7HKhkC77CfDBf1I8V9hbEnHBICYGCS_oTvqKeE2XpRDUrgyl4oWd1dvTnB5yU2aptGf0YYAv1V2C2Mgs0UwfrwiitDt5kILP_GwCMwIc3FJAujk_tllmVyXENchZXbg86p3JkgJn6pjQgnKdxRNtfE5AEYZx1GWRw-GVskc4JPsCcS-52b9xcXX9XMIfWBqTDjGisjr4NX5JhwnhaXiLKQtHQJWZjks7QNh3zmRY4GyE89K8obDWMU2YFI6k8aVfa4pN663uMnHTiqjPhu1up64aipc4zRZsvAMjmhpGOopMpHl5_-TretbEKEWMSgVCtyY0n4twvB_HwBlK8UWSAaSy0joC60IqCGOz3kCruWCAcFuDmBZpbREuj4RiveKD8Bmp-pQCkFZQxz6G8sWehMr22OqWh-AmgKq3ovqs3aQQUHlSApplmUWK02MJQdhr_IMkIpbIcOCLIOYd71GAcIemTwxrhEXUbM0AHnhTOw5ukMOXPPEEe3zIg_3tY8PlgrEGpH_rjvemanH-V5DVaQrl0V6988yw23oi6jdfmqzquR4u9seoEkB6MPNQFbjns9yB9rAK6ZjYkxRObdxJ0T4OMon3pH7P3PMprIRQN9Gnjub4pNGc0KU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستور پخت کنسرو خانگی آمیش‌ها؛ روشی از سال ۱۹۳۴ برای روزهای سخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/681930" target="_blank">📅 12:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681928">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeNjQv60XlKuEcEGIFwShpSe2WdiwsK1aFyORnNMTNFAXxxiAqhBGX2zqD5juEDznXf-eNN8Lu7fvGVy0-ADv6RXEFb5Jfv803zs5ssCoiarfPNKET8rdRLE1xnx4X-ykwsshpWY1b9bI4Meij1mRHM2sbGbLqBfjU5Pu3POOXKLfJcYItv4NqatK_zgvwBa29On28aU88WtjE7ZideNekyTdLuXsZ5zClu1ZE4ipPz08ohhHkM8vp02_wfv8by4BvbUQQF3K-11WxWa9SNLzFzXfkBAPFhf8Zux4PXhsvaAtU1ZNYHpCsrcw1OK3rv5OKfLulTAb7oopImmRnwEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مراحل ثبت شکایت در خطاهای پزشکی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/681928" target="_blank">📅 12:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681927">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d313518a9.mp4?token=Yu3ig4MbO8YhrZ9rvdII6hm4If64LOhAPA_hLsaMOg8lJcXNhMISSJjXJzp56oaLN1_jW4Uhm5bZ_362BG_mkzCbEp2Zb_E3pN6A_T4io4J1rTVr1V3WQYorMrHZUhLYPKKg7JSGmXOfEEwbUIj2Aroe9cZeiEZXvEu_3v9vwmPT3GwWPQ9s5liXYPyXInuo-WyP8s-lXg_IUoSecCxWXqweSXqDriVHLkh6ssAwDZ49TRdkOPVDoZAfJM1RRe0w6fj5rShHT7N5vZesdRwq1vko-15omzxVd-w5Qp3ppP1ZMdtvQnB3GrVc3iOkgFSjZ9M3WEViVH3D_0ncMyVHlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d313518a9.mp4?token=Yu3ig4MbO8YhrZ9rvdII6hm4If64LOhAPA_hLsaMOg8lJcXNhMISSJjXJzp56oaLN1_jW4Uhm5bZ_362BG_mkzCbEp2Zb_E3pN6A_T4io4J1rTVr1V3WQYorMrHZUhLYPKKg7JSGmXOfEEwbUIj2Aroe9cZeiEZXvEu_3v9vwmPT3GwWPQ9s5liXYPyXInuo-WyP8s-lXg_IUoSecCxWXqweSXqDriVHLkh6ssAwDZ49TRdkOPVDoZAfJM1RRe0w6fj5rShHT7N5vZesdRwq1vko-15omzxVd-w5Qp3ppP1ZMdtvQnB3GrVc3iOkgFSjZ9M3WEViVH3D_0ncMyVHlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهین به ترامپ جنایتکار؛ مستقیم از فاکس‌نیوز
🔹
نماینده دموکرات ایالت ماساچوست و نظامی سابق تفنگداران دریایی آمریکا، در گفتگویی با فاکس‌نیوز حمله‌ای تند به ترامپ به دلیل عملکرد دولت او در جنگ با ایران داشت.
🔹
ترامپ فاکس را تماشا می‌کند، بنابراین اینجا مستقیماً به او می‌گویم: آقای ترامپ، تو تنها رئیس‌جمهور تاریخ آمریکا هستی که یک جنگ را خودت آغاز کردی و خودت هم باختی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/681927" target="_blank">📅 12:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681925">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6209fb52.mp4?token=MWA8YHy6LA2XQLroTjEzXaKOrXbzU0uausO0D2faLXhBl44IB34Loi6rlWilDamaniRjwuvRNIgXimdCuGWsTwOKKH8G-6ayGtpSTB8Rgw--fnIydSLrVlo6C9h30orB2IbETPg-JJkHDpK4rerH-5cz9Gbs29Clk6h8NeaGKg9Az_w4Sp1rzrHBnWscJavAZy2aZ_hPo1PPBTMXyJI7f6QIQV5Q0cWeT0TUMlKM8FjavsKh1QoBD2FSLG94AVamyY3u_OKl1XDPy8RN-GklY76pnQtd-ol0X6jkLVl5H_-RT-HwdEM9jlIL-imsri39OWILvV8ISA9TbT5Gne66PFS8aXc765SJ8rii6zG8QzgiNDE3mSvP4JM9Om0tApzwAtjQjIwSOpNmr9ME4_MKrekopE17z2z6U567coQj9rQ4jdx1dUCyYwse3oOhF2sLNL1XVHjYxaZ23JSQDKohkFsYU9Cj2QxvaxSQdJ6E_okW-PpAaGOI_9ZXicGbjR5mUedIhhaMfO96PVWQPvOuxGzuRQmru0PyJr007xMzdEbNVeRjfDZ9Dc4_v4Nnf-2LRVwZsljWsI2RVlYb4WAdAt-BOOR5rRWFiqQGR1_99C2h5S5lWhjB7uAAOQyw2eX3XBscbwq7i_bfDoCNWkV4dep-R0TD2TxgegU2QbYjPGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6209fb52.mp4?token=MWA8YHy6LA2XQLroTjEzXaKOrXbzU0uausO0D2faLXhBl44IB34Loi6rlWilDamaniRjwuvRNIgXimdCuGWsTwOKKH8G-6ayGtpSTB8Rgw--fnIydSLrVlo6C9h30orB2IbETPg-JJkHDpK4rerH-5cz9Gbs29Clk6h8NeaGKg9Az_w4Sp1rzrHBnWscJavAZy2aZ_hPo1PPBTMXyJI7f6QIQV5Q0cWeT0TUMlKM8FjavsKh1QoBD2FSLG94AVamyY3u_OKl1XDPy8RN-GklY76pnQtd-ol0X6jkLVl5H_-RT-HwdEM9jlIL-imsri39OWILvV8ISA9TbT5Gne66PFS8aXc765SJ8rii6zG8QzgiNDE3mSvP4JM9Om0tApzwAtjQjIwSOpNmr9ME4_MKrekopE17z2z6U567coQj9rQ4jdx1dUCyYwse3oOhF2sLNL1XVHjYxaZ23JSQDKohkFsYU9Cj2QxvaxSQdJ6E_okW-PpAaGOI_9ZXicGbjR5mUedIhhaMfO96PVWQPvOuxGzuRQmru0PyJr007xMzdEbNVeRjfDZ9Dc4_v4Nnf-2LRVwZsljWsI2RVlYb4WAdAt-BOOR5rRWFiqQGR1_99C2h5S5lWhjB7uAAOQyw2eX3XBscbwq7i_bfDoCNWkV4dep-R0TD2TxgegU2QbYjPGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکوردشکنی MSI؛ گران‌ترین کارت گرافیک RTX ۵۰۹۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/681925" target="_blank">📅 12:11 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
