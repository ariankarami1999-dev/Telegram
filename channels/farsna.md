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
<img src="https://cdn4.telesco.pe/file/sbMugxMv0AwGatps2FPIF2LxmgrCEMWFWu1asRiidQtIB7gf6kv9qSiNAPsTk87-yETCcWc68Bnz9pT9MkkhRKJNgm3NJkmufRxxOrsTkmV_FbC46_jH0tKu7NxgBUuEhw-m0wu0IKmhP68TO8wm0aF7Iox-cLG-9XuTHdU45sFKbYPG_c6uw768tXwU7vmlUfSli1L70J0oG5vfQnt1I0UW0cC7YWd8ql31FMAHjbjOUqZBqqLIvnPsUbCOmbS75mJ5IYs7Qz14pBbnELvOxQ_JtDO1-yUp3vVsn81br1-ZWlD17vVn5vJ4PzG_usc6qa3PPbI4M9CNa3cniLD29Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 07:01:12</div>
<hr>

<div class="tg-post" id="msg-438049">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LV5q4PpVm7bfddIRXOx424tBXYrst6aNuteldah04g_CcWdHU9hjqTgXn0nx6RjnolQZbM8uIGw3AvN1xNcEe8AHOp0MZPGmIpYRXNh_6QXqSc1xQgc0OYOI9ZVHd-E8Sv0EF8oEybKyNnkAnWACqMbF57MJRht_IAdfp0eZOvDDPf8qxf1Oi09rg-lz8v4eFlLbuxmbswX-bxeI7ztiAhe-Rhxu54Qwi_eMfJOTU_KrkxqSiEC-u4rLCVQgRoNqUQywZzzPLPrqhAO50gE0b-OruOftgWKbKDmi-Dge3IwXgT-nfRby99mzUquqhrjSk9vAh_RpNU0VLA879Qau7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEDsjnQPLrxfjV89mxPeIFIS4Drj6Aqkxp4pY4QJPaWHraePIcARAkBy7mt93Oy8plejsLrbkHJwMij0ftU8DoilTjksIMoOwhEH8m1Zr4guL0RCjEPEJzrv-RVpH-pPiTcy3dIjkNl9iLoyAS1GR-tw4vEaTuPcB4JwMou48rJcw5f0SoTTJOhUAl1E_l77e3LEnYUYJqP0GuNw1TTTV8W4K-JDtgdhlJbGsj8Em96n-_OjzopBQJ-ez48kEOpAunGCC33rEv_BqWck0ayoVGTpDZm8tzslx_an7FYLnP4kU5kmFtvumzpcd_ZXl3opgUseDhUYlGn5JswI2KEx6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZB2R5RHFH7kUciV5F3kI6OgY9kZ6Uqq47NLLygIkztEnb3fr5zrOx4qtXGvkQESrgMC03yF5t-fsfiPUCoUsmrVF_Ub3miVtZnH0plufjdyTu8b0gExLeNBKbgJpnlD58YlzbhbO5AIX6lhTLR0dBHKN9bEK20ou2Y-hm5Wy-PymJG4gGSNaPOwOhKXRJo4QdxLfG2dRHWYoAVQ53iS62ilxp1uXtOEL5Hz2X7UGU0d-O0G5MOwfPcsP_TJJ0sXpuNVm-QR-Ay6SeLz8DwpP330SxV6WNpoORIhJ8NMrezD2wBUAXanbeeaPgMyAuEUH9AXFce4XdNXmCpHRb0HDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwoJjUDS3qookwyWSS3ggEDpdD_VoChUirAgQjfCq9dZWnsHloucFIB1bRD01Z0PCKWN9FlRx9nFal-zHT-cikslbul45YFVdRuU7xnChuMJ7GJBO90FcV6AyvXvdZMBUyUwxA48D8i_9jWVOOzZf0nhtx_BPRqTUNz6JDPFValyKo2inrQLLAEPWXujWzEsgPGfvAMm90ky_q2C0085h7vfuByBXtlBCm07oASuEOs3F9KJ09EDKWs7fAWgxAP3CpXnvthmvBCJWXRfYuDS1yJ5F0ELjDyq31plDHpO-pSvlHdXt-obSsJm-tgiT_zUoc-SDDG5oOycfKFEB8cGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYgoBEsCtCJko5RZuNeXqKGL8zHvfIxInaOST5WkfHAsIxAfuSjI0baIV28-TRB54H5Sqhhdw4N6WOBSCnZFLJ9d_XERLslMI2_zeZB6cGCRIoAzV4M8S8NpO8MCDpk5PMR6r-OLKl9fi-P57oo9F7WTPYA71OsQzceffnlfVv2TK2XCxZUXv0WPlqI9xYb2ZHkAWBGQGM7I4B2-jt18xdxSSu5GY0H133IGFdHwp5SAJuD6mTR-3Tj1BKSXECi4mduF8kIS5JZWaBlJMdtHiHsC8zkcH4m0K-5k5FnJxSJajMOLfJou68wICcYlwEKz6MaM1nMSpEZGNCALPzwLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUv_72Sf6YSisJDTaeVqefqo4KhGn3Z0m1rJ1DkR4TQxpuyH3OhDHZCcl3imd6qdevxUdnxFGE1pMHrgPgrhqs8_uJXObGhUBuEgoD-dLy671jqGnWC_xN5KzBkufhm_Ti_ySFZbacUNKSAXRe2MoPTN0Q-MV0Hnr-dYydFeF_w1DT1jujax4ntIRJhbbgHQdVYVDStnA2uS8B0k54zzeITyIftFKk-9o919ing8eRnD5NA1RFzImnLxXzHIm-CfWPfsyTwYN-s8Kv0CC_XM0XxQ7c7Fvx4GWRXYkluJGS_zZyTKw5AHUEAXrz9tYFUPbdfJcayGdHKlFa06i3pfrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شکوفه‌های سرخ کویر، در باغ‌های شاهدیۀ یزد
🔹
این روزها گل‌انارهای از راه رسیده بهاری، باغ‌های شاهدیۀ یزد را به رنگ سرخ درآورده‌اند؛ جلوه‌ای چشم‌نواز که در کنار زیبایی طبیعت، نوید فصل برداشت انارهای ترش‌وشیرین کویر ایران را می‌دهد.
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/438049" target="_blank">📅 06:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438048">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mqv6xY99yQ4Cw1Kl1DB4QeGzOsqK_hORNpvqQN6iiEdc9-lTCRm5X88_UHY5cqvoSprZzX89FwiNmotkGDtOyDIZiYdVv_0xUldpK1o-eVWbWJPW3DvkDEaX4pcnBL4AfNJemSK4Ih-LXvXcX151EaYo4rYds-f9Sh2gLbwFuD70wD0wJcCBolROXrhGwXDYMI6cgcr9dsyuQMYtMBF3HopTM5Z1jsxYmmyTOjqhW5qc7NfjrQ44JW-AG76Gdpx0Lc20QHL3jNkymF1dqaMvIm7-B_EOsvq7YIqFhZOBh8CLcvl4Fh9RpLOI5L-sYffsc0HIOh3er8e9xlB74z-9iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات روزانه ۶ پرواز به اسرائیل برقرار می‌کند
🔹
شرکت‌های هواپیمایی امارات در حالی عملیات خود را در اسرائیل گسترش می‌دهند که دیگر شرکت‌های خارجی به‌دلیل ناامنی از این کشور فرار کرده‌اند.
🔹
روزنامۀ عبری «کالکالیست» نوشت، یک شرکت هواپیمایی امارات از افزایش تعداد پروازهای خود به اسرائیل، به ۴۲ پرواز در هفته خبر داده، که این تعداد معادل ۶ پرواز در روز می‌شود.
🔸
به عقیدۀ کارشناسان عربی،‌ اقدامات امارات فراتر از ملاحظات سودآوری رفته و نوعی حمایت از اسرائیل محسوب می‌شود
.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/farsna/438048" target="_blank">📅 06:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438047">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تنگۀ هرمز مادۀ اولیه کود آمریکا را ۵ برابر گران کرد
🔹
فایننشال تایمز نوشت، شرکت‌های بزرگ کود جهان، مانند «موزاییک» آمریکا، تولید فسفات خود را در برزیل و آمریکا کاهش داده‌اند.
🔹
دلیل اصلی این تصمیم، اختلال در تأمین گوگرد به‌دلیل بحران تنگۀ هرمز است؛ همان گوگردی که برای تولید کودهای حیاتی ذرت، سویا، برنج و روغن نخل ضرورت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/farsna/438047" target="_blank">📅 05:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438046">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دریافت شهریه هنگام ثبت‌نام مدارس، ممنوع
🔹
وزیر آموزش‌وپرورش: تمامی مدارس کشور موظف‌اند هنگام ثبت‌نام از دریافت هرگونه شهریه خودداری کنند. ثبت‌نام دانش‌آموزان نیز صرفاً بر اساس محدودۀ جغرافیایی انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/438046" target="_blank">📅 04:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438045">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cf096c343.mp4?token=dGuPAVvmqQxcn5W7B17UPChRa1Q4vJGPHdWaUtsla5XlUdP7BzAOZ9d-K2oDc82fUw7gpnW7SkAi9CbmoS3Jbl_aeD9NiAKOboZmLs358o28dM9GVqBSHYQUGR12UoqDaPbcgzC2aaLMTxH1i2K47VQxUCDa2z98zhayB9jcXnKLtgFD1KXempUPOskWWQWjlX_6lczNEa62Hve8vn-LA4L-aT4AIK1wnFJB1IcuY4mcdWINaB55DEN-0HH38d3ZX_mNBfjfPg8sWxfFbv7SjvncsQF_qG2SBCdvywAqWdqzAXDQk039hsFBjZxP84uCE4y92QraFkyX0ri8ylwKkQiqVCH3i2Y0XaSiVuwmw67FWErYeLrPYHdVVDBsVFce5RM1A5GSl-XqQ6bmLjhDMRv3gE2_AxGuSDuhLpOvLTMrTre1K5uJUBTj6JSprGHthyMiJ3t5ztrGIh8c0IeLRDJ0SEuk7d2SS05KbAhY50vioaXjLwsqn2m_bbMrU9vDOzLriKzo9BNbM6BDabeKPmnUxE7gKxKk3AGVlIfJPtXkFLUVrJb1tYQFYad54CaRjAqqIZW83u7BdXz8PzM-KOjtR8ad-_5r2qhHjVu5cOGbNnLdo_esT1Aado1R632O62x-B-sMMldtOb2fMZNvLBwLRz7BJ6HKglBHv5naIMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cf096c343.mp4?token=dGuPAVvmqQxcn5W7B17UPChRa1Q4vJGPHdWaUtsla5XlUdP7BzAOZ9d-K2oDc82fUw7gpnW7SkAi9CbmoS3Jbl_aeD9NiAKOboZmLs358o28dM9GVqBSHYQUGR12UoqDaPbcgzC2aaLMTxH1i2K47VQxUCDa2z98zhayB9jcXnKLtgFD1KXempUPOskWWQWjlX_6lczNEa62Hve8vn-LA4L-aT4AIK1wnFJB1IcuY4mcdWINaB55DEN-0HH38d3ZX_mNBfjfPg8sWxfFbv7SjvncsQF_qG2SBCdvywAqWdqzAXDQk039hsFBjZxP84uCE4y92QraFkyX0ri8ylwKkQiqVCH3i2Y0XaSiVuwmw67FWErYeLrPYHdVVDBsVFce5RM1A5GSl-XqQ6bmLjhDMRv3gE2_AxGuSDuhLpOvLTMrTre1K5uJUBTj6JSprGHthyMiJ3t5ztrGIh8c0IeLRDJ0SEuk7d2SS05KbAhY50vioaXjLwsqn2m_bbMrU9vDOzLriKzo9BNbM6BDabeKPmnUxE7gKxKk3AGVlIfJPtXkFLUVrJb1tYQFYad54CaRjAqqIZW83u7BdXz8PzM-KOjtR8ad-_5r2qhHjVu5cOGbNnLdo_esT1Aado1R632O62x-B-sMMldtOb2fMZNvLBwLRz7BJ6HKglBHv5naIMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت خلق شعر «خدای خامنه‌ای زنده است ای مردم» از زبان محمد رسولی، شاعر اثر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/438045" target="_blank">📅 04:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438044">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شهرداری تهران: ۹۷ درصد از واحدهای آسیب‌دیده در جنگ تعمیر شدند
🔹
محمدخانی، سخنگوی شهرداری تهران: با همکاری مردم، گروه‌های جهادی و شهرداری تاکنون ۹۷ درصد از واحد‌هایی که نیاز به تعمیرات جزئی داشتند، تعمیر شده‌اند.
🔹
حداکثر تا ابتدای هفته آینده، تمامی این واحدها به طور کامل تعمیر می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/438044" target="_blank">📅 03:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438043">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e85815.mp4?token=lWDRaClnqFaohR5Ve_XGTbWl2rdeELxE9Z0B-mteV02Oi_aPM4nQVcWR8EWb_qZxrUN_dENr_SEiX-cspdCMETRw-y5lyGPoSlKjMlx3uJd49YJ2N-DBiEdIdf6yWFnej0ZrDZJIHZ7jEJOPCnJiyQRwQUHo5HnjGbBPUlWSgU8cpcxfFFeZabXl-1q8wZY68XL1Cuujc_yls_83Xsjo-72s110FuzLZjbjFtKvsiPn4sHr2O5oXPtguFrD-UmuVUufOJn05KINbk-_r6Opuocd94zZEyC_vXnN7wW-5uM3XAYsVwaPMYW3DDKsvZMFtHgk7GVk7-cW1qfBZjNonVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e85815.mp4?token=lWDRaClnqFaohR5Ve_XGTbWl2rdeELxE9Z0B-mteV02Oi_aPM4nQVcWR8EWb_qZxrUN_dENr_SEiX-cspdCMETRw-y5lyGPoSlKjMlx3uJd49YJ2N-DBiEdIdf6yWFnej0ZrDZJIHZ7jEJOPCnJiyQRwQUHo5HnjGbBPUlWSgU8cpcxfFFeZabXl-1q8wZY68XL1Cuujc_yls_83Xsjo-72s110FuzLZjbjFtKvsiPn4sHr2O5oXPtguFrD-UmuVUufOJn05KINbk-_r6Opuocd94zZEyC_vXnN7wW-5uM3XAYsVwaPMYW3DDKsvZMFtHgk7GVk7-cW1qfBZjNonVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری فوتبال برتر: طارمی برای دریافت ویزای آمریکا مشکلی ندارد
@Sportfars</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/438043" target="_blank">📅 03:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438042">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq9Oxg2M1aQR3-92gpKPHM0f5kJjjm_nyZQFMCxoFToVIKlnBdlBgzldYqDYac4iNjVVmhapZLszfqMOfvaLlOJIWf1cXyoQaJ_e4wlRj1dENjfZS6JQLTXB-SzEtEUEM-E0M7B1da8lngrdmsS-lbpFfoVq51w-l0wnum10fudyhF6rvDk6UKsIsXHNnu9juiwgbv-TTIbZZockXpvOXdLT4gFkjfCzlz6j-nePLeCgujsYdcI_NCptH-rFhqAKEu0_2tLu82BGFak-vgzeas6hOUi_eoKtlsaRLB7BydVnauV7_7f7Z8kOEY6dDc5-WlU0VDsaHkVUmfTr63V-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور وزیر برای برکناری پیمانکاران کم‌کار طرح‌های حمایتی مسکن
🔹
با دستور فرزانه صادق، وزیر راه و شهرسازی، مدیران کل استان‌ها مأمور شدند پس از بررسی و ارائۀ تحلیل از نحوۀ عملکرد پیمانکاران طرح‌های حمایتی مسکن، پیمانکاران کم‌کار را برکنار و سازندگان متعهد و توانمندتر را جایگزین کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/438042" target="_blank">📅 03:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438041">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2iDW04NegoVjAgpt1ZWwSmC3aTcWLYwSfxH6hjve1oH7O5OiHcSGyhFnXUCedM781P1ACDMNkqmOQNk0dfjGbspS_u0m6oMQJuL5omntMB-4dDCPulGdi7rBxYOK4PdfEbc0OfX9UvIRLK3GjVGdCBgYUiewsB33pXM2Hvp9MlBN-G0etaGoqmYuhMxGI38Xo6xV3QIiQaHJ_PEmLzXIuWCzYYg38WU-NhwtQLUHhimaIHZ2IPuT5cbyIkjwgxDsIa8GT7lGfDYcVdfM-_I6ylkrekW2tNaCoO5rAjWmSHnO3gh7QUmlm6gVwJF1oMwi6zySqD9xQSx5FaVvQLV8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذعان سنتکام به نقض آتش‌بس با ایران
🔹
سخنگوی فرماندهی مرکزی ارتش آمریکا بامداد سه‌شنبه به نقض آتش‌بس با ایران از طریق حمله به اهدافی در جنوب کشور اعتراف کرد.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/438041" target="_blank">📅 02:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438039">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce7282d4a1.mp4?token=dtEpPQ4sfUpA-bXOa8dxXuUmB8b35wDD6-JAtPwQayVtGadz61fJkIl6nWgdR_ec0ZP39XfsDK5j62F3L2h70raMG09Hdw7kY16EcrktMoRbeqQaJczIHjFE14QAI9NXGyYk3moOt14gaCPBGz4M_NsFb8hZP_QCBwU11Z6W8BIiS8eC_38rAgWZ_XtokHD6lvz-ENmXB58sjqkzot7XSBEDYsF4kTm9gWR0KWJGf689sE-j4cjCCllimTD4HiquqkZAara2u1VCOMiHYUUvskMXb1lIAMGdes03t5_2HzMZsu2ucVyY02lpWBb9UBDfK2H7ntjmrnFnRr10tCzzGW22_Xk_nH3sU5T1Hf5hyxW7oGzljg-GwbQbB-Ttl6MtMaAXIIG-NrymibvkHFh6N1gDu9REoZ6RAx-2AOo5uhR6soP9AhtQ5hi7JuaIDj8fj7lvcpbWjnY7Qqdwk-MwZ-DSaQDco2ZjXmLwen43qcNwA-2F-9aasvJBrre2MvcFx1wguJKt7F-5D2OtI5lUf6k35HBX2RpXN48WZfMGG2M7cE6gXxxhRotpP5gT4jcE5_UyApofrsgt0HJmp4qbbGv0ger4fP1Q3TrwjY_Yd7wnTQLUZjkEOlQ9yrbX3OnFhvixuyVbZqhMNchESJ09IUD0T2sUlJbjksg9KZdNcpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce7282d4a1.mp4?token=dtEpPQ4sfUpA-bXOa8dxXuUmB8b35wDD6-JAtPwQayVtGadz61fJkIl6nWgdR_ec0ZP39XfsDK5j62F3L2h70raMG09Hdw7kY16EcrktMoRbeqQaJczIHjFE14QAI9NXGyYk3moOt14gaCPBGz4M_NsFb8hZP_QCBwU11Z6W8BIiS8eC_38rAgWZ_XtokHD6lvz-ENmXB58sjqkzot7XSBEDYsF4kTm9gWR0KWJGf689sE-j4cjCCllimTD4HiquqkZAara2u1VCOMiHYUUvskMXb1lIAMGdes03t5_2HzMZsu2ucVyY02lpWBb9UBDfK2H7ntjmrnFnRr10tCzzGW22_Xk_nH3sU5T1Hf5hyxW7oGzljg-GwbQbB-Ttl6MtMaAXIIG-NrymibvkHFh6N1gDu9REoZ6RAx-2AOo5uhR6soP9AhtQ5hi7JuaIDj8fj7lvcpbWjnY7Qqdwk-MwZ-DSaQDco2ZjXmLwen43qcNwA-2F-9aasvJBrre2MvcFx1wguJKt7F-5D2OtI5lUf6k35HBX2RpXN48WZfMGG2M7cE6gXxxhRotpP5gT4jcE5_UyApofrsgt0HJmp4qbbGv0ger4fP1Q3TrwjY_Yd7wnTQLUZjkEOlQ9yrbX3OnFhvixuyVbZqhMNchESJ09IUD0T2sUlJbjksg9KZdNcpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صداوسیما از بندرعباس
🔹
وضعیت بندرعباس عادی، و استانداری در حال بررسی‌های تکمیلی است.
@Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/438039" target="_blank">📅 02:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438038">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎥
پیش‌مرگان کرد مسلمان باز هم به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/438038" target="_blank">📅 02:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438037">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc745442e.mp4?token=Na2Gxs-1ZzrQObL-Z3E-33sWi3fNNAQqbJ4w99SBsCtFA1yKIW0z9cxmysslkJHrkm-eauJGhYfzWQ2F0LTmbrxr7CMaJ-AI1G3IEbwGBFAWACCJUy25PWibFXr5phzZOZW4-zOf6xMqeohM92znL5U1iLDc6Ja0WCXfL21oSc5oXnYJlOKmWLsYl98Oq-zepC2SS4bW8cvrqjvXSoILN8_J2TVxk4GHx7DHstt7doVCWR946uGBnoYZuWyhHgHkW7Dontn3Iu02zt7NTz1GCBdXk21HLV0K5OeuJsDNu9wsS4m6exm8NK6s0qSGiFNEYd9l-AIojB09Lmiin7HllFMr-z83ane-QvxxTkm7ayFtYyB2q0Zfeb-H-BxeutbfD5LY3Fb3gzKMIB0Y_UwQvpDub6N7gmOmoZ5qkDiiWTjW9VB7HDFPfrzvTvh33luah0oHPOJkOcsnSj4EVh0vM9dLnabkXZK6pD2TL_MALx_C_Y2RtUOw8OwLM_jjzx5cAM8qkDtHvimi-ZgfMebbvXkzMSTARSb4cW-RDYrPdA45w-2VL2coX3C8k39_e-CpE-EO-WvKOtznRJL4p_yL4HvkUW5gO__-_wldxgFE5VzwGGucUPZG0cS1oL6evnNPB02NmmINxM2Mo2VEd52WP7RQDyRBGKXqR42YBqY0OS0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc745442e.mp4?token=Na2Gxs-1ZzrQObL-Z3E-33sWi3fNNAQqbJ4w99SBsCtFA1yKIW0z9cxmysslkJHrkm-eauJGhYfzWQ2F0LTmbrxr7CMaJ-AI1G3IEbwGBFAWACCJUy25PWibFXr5phzZOZW4-zOf6xMqeohM92znL5U1iLDc6Ja0WCXfL21oSc5oXnYJlOKmWLsYl98Oq-zepC2SS4bW8cvrqjvXSoILN8_J2TVxk4GHx7DHstt7doVCWR946uGBnoYZuWyhHgHkW7Dontn3Iu02zt7NTz1GCBdXk21HLV0K5OeuJsDNu9wsS4m6exm8NK6s0qSGiFNEYd9l-AIojB09Lmiin7HllFMr-z83ane-QvxxTkm7ayFtYyB2q0Zfeb-H-BxeutbfD5LY3Fb3gzKMIB0Y_UwQvpDub6N7gmOmoZ5qkDiiWTjW9VB7HDFPfrzvTvh33luah0oHPOJkOcsnSj4EVh0vM9dLnabkXZK6pD2TL_MALx_C_Y2RtUOw8OwLM_jjzx5cAM8qkDtHvimi-ZgfMebbvXkzMSTARSb4cW-RDYrPdA45w-2VL2coX3C8k39_e-CpE-EO-WvKOtznRJL4p_yL4HvkUW5gO__-_wldxgFE5VzwGGucUPZG0cS1oL6evnNPB02NmmINxM2Mo2VEd52WP7RQDyRBGKXqR42YBqY0OS0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهار دعا را اینطور غنیمت بشمارید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/438037" target="_blank">📅 02:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438036">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gp_VxKanSyDL4LySN0_Kf8BIjCgeYjhgTyBAJcZd0wOyBWkCOE8cE3Pdpmr5P0s9EJF1FY20_N5mTmDI3rHAqSiVD2d3ieyTsbWYyS77nnA66TfgfULm4hz-wA5dMU2q2f4MeVxd2Ii6tqSD_MLSLWUqzoQuoO9-RVZOQeVcRmv8M9Zp7_5GWbHC6DveULRu6SV1q8tTffBUKwm5kApLMwScDkvYI8j5_D1hKpTEzZ8QVmkhOm7WUAG21HBfUhRFbjZAnC7NGXTclmBT_62Twrn5_mMq-KuJZSFV87imeGDX4MZVFwMhPfnLzU5pOCqgnfu1vHFsEb9jTPUBZs3Iyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۷۵ هزار مادر روستایی دارای سه‌فرزند رایگان بیمه شدند
🔹
مدیرعامل صندوق بیمۀ کشاورزان، روستاییان و عشایر: تاکنون ۳۷۵ هزار بانوی روستایی دارای سه فرزند و بیشتر، بدون پرداخت حق بیمه و با حمایت کامل دولت تحت پوشش بیمه قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/438036" target="_blank">📅 01:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438035">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad4c72e30.mp4?token=MMFLmoJbVsW64TY0BkR56l9t0HrZHw6a8paDRnVAlA0zTmfaaEby6LE-C5ACw4wR5-jEClvI5Y28rAEhceENF2OToO0b2Ad1-p2RcoTmHcAyoI5JntyXb8c5ini6yaRB7y1pm1RH6XzS2xN2vaKWfou6JT3MW8jkfMrnHab-5XiyyUEqihV4jmS7HFah1MN7kS63JhlH9x-h7qFewyrT9IP3GG1eCg4ke0iVF9C5tvbKu2vG9dRvfqldF2h56opdH99rVXi47juSut06j3EWNnlG8N6Z91_P1RyNP4YmxZfeQ0eLJOyt29_9y5zDaAJojcOlKOZ3zDAWX4aqaIXHWElSBciB_35KIV_6xsHDNGgnBOlLIR1CKhqLhIq9zFe__pNEXmVkhYhnTafGvQn7Qv-5jcXcOkx7S8zwEjjQmFzz-_h2MpCXky02AIoY8hmxilGn7irOFVE2hOZCyYZO6UPqhYG8n3tbVL99Grq1r49oyrx11v56p0tmn4HUbjx75vo_TxRU9VuN45QCjx9YLfDgR1Eu37c3im1GVYDL_q8ok6j5pjee5JI1dbKSk3HowCQ_17KUus_6yY50ZnbwErxLfVf3rDcRwUwzzb8iDc6QJG8ghobYkHxKvtWw0udCQsjW4FJVxiMXJKodjbRgdHOxyrAgE2RQTN0o7CeopSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad4c72e30.mp4?token=MMFLmoJbVsW64TY0BkR56l9t0HrZHw6a8paDRnVAlA0zTmfaaEby6LE-C5ACw4wR5-jEClvI5Y28rAEhceENF2OToO0b2Ad1-p2RcoTmHcAyoI5JntyXb8c5ini6yaRB7y1pm1RH6XzS2xN2vaKWfou6JT3MW8jkfMrnHab-5XiyyUEqihV4jmS7HFah1MN7kS63JhlH9x-h7qFewyrT9IP3GG1eCg4ke0iVF9C5tvbKu2vG9dRvfqldF2h56opdH99rVXi47juSut06j3EWNnlG8N6Z91_P1RyNP4YmxZfeQ0eLJOyt29_9y5zDaAJojcOlKOZ3zDAWX4aqaIXHWElSBciB_35KIV_6xsHDNGgnBOlLIR1CKhqLhIq9zFe__pNEXmVkhYhnTafGvQn7Qv-5jcXcOkx7S8zwEjjQmFzz-_h2MpCXky02AIoY8hmxilGn7irOFVE2hOZCyYZO6UPqhYG8n3tbVL99Grq1r49oyrx11v56p0tmn4HUbjx75vo_TxRU9VuN45QCjx9YLfDgR1Eu37c3im1GVYDL_q8ok6j5pjee5JI1dbKSk3HowCQ_17KUus_6yY50ZnbwErxLfVf3rDcRwUwzzb8iDc6QJG8ghobYkHxKvtWw0udCQsjW4FJVxiMXJKodjbRgdHOxyrAgE2RQTN0o7CeopSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرهٔ تصویربردار بیت رهبری از سفر رهبر شهید انقلاب به مشهد با پرواز عمومی
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/438035" target="_blank">📅 01:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438034">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حملات رژیم‌صهیونیستی به جنوب لبنان
🔹
منابع محلی از حملات هوایی و توپخانه‌ای متعدد ارتش رژیم‌صهیونیستی به مناطق مختلفی در جنوب لبنان خبر دادند.
🔸
همزمان حزب‌الله اعلام کرد که در دو حملۀ جداگانه، تجمع خودروهای اشغالگر و سربازان را در سایت المطله هدف قرار داده است.
🔸
هم‌چنین مقاومت اسلامی لبنان در بیانیۀ دیگری، از حملۀ پهپادی به یک تأسیسات توپخانه‌ای متعلق به ارتش اسرائیل، در شهر عدیسه در جنوب لبنان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438034" target="_blank">📅 01:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438033">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ9SgXoC21kNNG4mZY51thdSCeqsIiU6_HPQ3RyjexnqtXI8AEMxT9w2hXUNWCfMTWewJnQgvAc-xYl8vnW0OWYGz-B4cPkBwrqjoWClOFv8y6MYSD6Rf9aM0XEY2es1Q0m8wp3KZHqyEan7qGcZbOmfZHZaynH1rJtEfTCwFlRe9uHHJ5_RijjgcGGuZi8-dogNF_Z969JfcvdBISppelI72PRLxJt1VE6y6e-jxrYb--1weY-uxBGk0Bj-VN8rIu6STY-gIXw2KrmZtUE5G6k86g160TkGi4LxonyXxDjAXgxT4T2J8vzpozpokoqThIV8IOMQJ7PdXiajOooS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان و موش‌های آهن‌خوار
🔹
بازرگانی پیش از سفر، صد من آهن به دوستش امانت سپرد. پس از بازگشت، دوستِ خیانت‌کار ادعا کرد که موش‌ها همه آهن‌ها را خورده‌اند!
🔹
بازرگان بحثی نکرد، اما پسر کوچک آن مرد را دزدید و پنهان کرد.
🔹
روز بعد، مردِ مال‌دوست سراسیمه آمد و گفت پسرش گم شده است. بازرگان گفت: «خودم دیدم که یک شاهین کوچک پسرت را ربود و به آسمان برد!»
🔹
مرد خشمگین شد و فریاد زد: «دروغ مگو! چطور شاهینی به آن کوچکی می‌تواند فرزندی به این وزنی را ببرد؟»
🔹
بازرگان پاسخ داد: «در شهری که موش‌هایش بتوانند صد من آهن را بخورند، شاهینش هم می‌تواند فرزندی را برباید!»
🔹
مرد به اشتباه خود پی برد، آهن را پس داد و فرزندش را گرفت.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/438033" target="_blank">📅 01:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438032">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KH03b8PcuuDUKcE_ktwToKdfYnq-ndoZksTDzlgAE0EulqnZ-B6y-Rj9AuVu3w1vHMdKqcD5taB8pkCjngduGMBnUafrWz2c--bAImGzReiwlkASU2MUJPyDyphMPgHrdytppKblBmFoc6lUVYscbNTdxgey-jxE6N3Ay-5dA5yRtbVVmv6Sj_DNoDEJvdgOdJZ86Uk8k88wGrgPjLJ60vDPVdOnhfiOwcYvgLsiA8DDr8eCuHf9hyrJ90njnBfrQZjl2hWGMcrqGjZ4f4YXAFLVwuFv9BRsEv_8bYkl9Z17KpFMJ7STVKwl2JGI5b22TqOkNJoeE3JGeS2NkTzJug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بار دیگر زیاده‌خواهی آمریکا دربارهٔ اورانیوم غنی‌شده را تکرار کرد
🔹
رئیس‌جمهور آمریکا: ایران یا باید اورانیوم غنی‌شدهٔ خود را تحویل دهد یا آن را با حضور ناظران، نابود کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438032" target="_blank">📅 01:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438031">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c05b1e3c4.mp4?token=B10Wnbd-Al0X8M7vgpGca527QBHACkdkA1M2qRUNABB2A0YSwbi8KpzRX-WREuFlJlDc6hJ28WM0LUErFDCSL_0c4dla2g2AU3xbH4_Eof_GSBqDTzgjziL1fVRgljp39quHgT1jsb6vReiKiHA_0FwsHRy7VkXv4Ti7T_85J9_erHdCCdCxO-_ZGvbsNjkOmopa9Kp04uBvgN6Fy0flhk5XqUykDhWU6E2Zqu8dx8YjSN0zIwgwxEAvLOcyZutHY63Ui62JORjzq3Z-jKB-FktB_aw0DJTgbTDN3vNyglCM0fUMjqMiluUkMeIGamxafy9ZBjWiHWkf6PAbADz5gYP27kdt5lkcZh5h53ppC5gioPEmWVo4SccuM93w9ZrN5j0af0h-zuOuA5S1zzfOE0P1i1cOhLxJS08pRj4ZtrojIbhLIljdCge3l-5tgivRzlNueucllp4sYqWpnSrLKUCSzKe2ytnWjI3_puLLoKJ1u7CBCE87DA09yni9x-i-w_lMC4E56Nnom7BRp4qWZxCzEukJqwIqWp7kCiJkadl09yN7mFpfLsFaWIjvVmfQw7K6aSVivSXDt-LCTmV-kj2csjlZ2-699m14M9Cn7gZMpXssewOoDfhqcShmmISIphkq3AiG0C2ENyyNs-ahULM7Is3dY8SIizjm3e_a8Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c05b1e3c4.mp4?token=B10Wnbd-Al0X8M7vgpGca527QBHACkdkA1M2qRUNABB2A0YSwbi8KpzRX-WREuFlJlDc6hJ28WM0LUErFDCSL_0c4dla2g2AU3xbH4_Eof_GSBqDTzgjziL1fVRgljp39quHgT1jsb6vReiKiHA_0FwsHRy7VkXv4Ti7T_85J9_erHdCCdCxO-_ZGvbsNjkOmopa9Kp04uBvgN6Fy0flhk5XqUykDhWU6E2Zqu8dx8YjSN0zIwgwxEAvLOcyZutHY63Ui62JORjzq3Z-jKB-FktB_aw0DJTgbTDN3vNyglCM0fUMjqMiluUkMeIGamxafy9ZBjWiHWkf6PAbADz5gYP27kdt5lkcZh5h53ppC5gioPEmWVo4SccuM93w9ZrN5j0af0h-zuOuA5S1zzfOE0P1i1cOhLxJS08pRj4ZtrojIbhLIljdCge3l-5tgivRzlNueucllp4sYqWpnSrLKUCSzKe2ytnWjI3_puLLoKJ1u7CBCE87DA09yni9x-i-w_lMC4E56Nnom7BRp4qWZxCzEukJqwIqWp7kCiJkadl09yN7mFpfLsFaWIjvVmfQw7K6aSVivSXDt-LCTmV-kj2csjlZ2-699m14M9Cn7gZMpXssewOoDfhqcShmmISIphkq3AiG0C2ENyyNs-ahULM7Is3dY8SIizjm3e_a8Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌خوانی مردم تهران در میدان انقلاب
🔸
حالا که با نائبت، عهدِ دوباره بستیم
🔸
ای پسر فاطمه، منتظر تو هستیم
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/438031" target="_blank">📅 01:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438025">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6wlI94JB6xGJunVA2WE7eWuDvWN02PkiW0s3JGTHJ4tC-6A654TPDPHHH4BwqGiahmAlHXaLsMLPP_5nisFlRXG6vMfBYQm62zC_3BW_wo3PS7YGSilPXHZRNo4q5hXB0TyO3J9488D9aYFlLIgO_48He23NCwQ5pctoFgBL3q35X8891qcmjdA1P_75ZhWOWXXc_2A3NTbS3qt4-0Gn2mnmmsqJFs8UQGN1iQJX97AgSQ6IVbfR2Lj7YPxj1XdTQyPNYGP0Tw9Hb6XPACXQ8UwxYt3s-ODrC-3-nGSKf7jwbb1vI8kQz3JMxZvizPjyKvIzXoJPb3JNFvEboBIsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkBDT0kJIs90y4jQ1I5nI4mMKp9-4caHbCeIgz0ZOAj80mWuaQo3m6oj0J-qTwA8IgbmkxZ8DL-u9co1iBXtaH-fM8j60zQ8tI4YQ-lCIRlhuI3A4cacQdlugk6EDYFY74pe-xP1GRR1cuyjmBbfeIR_P0ksHsoYBFMhxGTxu29O4w-RtyMQxL1EJm43xYf2ccVKtDXZpPG9ssoJ8se806m_KnCJ-I67gkT65R2-z64rRVKJZ8o-A70oS2WwdX3oF1iJpiXo4oRLv3wCnnUWdIEpuC4zck0If1nXkavd4DgNpA-7Ddl2lLeWjaHVqcrbqxJhr8lniS79Vx6YWCxGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWl4ql5mG6YqhxY_JVtzh2ApeLtdXij6sEDQlkvNZaIVn5N_x-7OiU85qMG2Wb09HN9CiIQ7M39IlQPA7TZRANdMx2p4cGH1d9U7pngcFZ-3AeOOVG9K3HXFI0QHryUsh6pXNA99V60t53OHufVzYuYGusPALl0mb01hCPdtcaglXvrXb_nwBpGH1EUempAxndEWoW_Qu8tiCB4xFEngNeEWBGRn7ntgg2mSGtm7dgW-5qfaKjP6zDRp9VdSbA79AT-_t3Vh23X-TSVY6ONQhBmSj7PguyLReI9SEXhKvQs_5vKahP6VTz3CSdiDJ1kntYYVICw3yUp8Q9DscAkpBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c4sBIHz9oyizjV8ngHJyRjiB33MVbMMRearybf-A1bE736CcQuZFmIpY7FllmoSzVvDGFA2eZ4XO-TUd8DeJqPxsULYcwaGBcK0IkCeHw7v-RpLN5gCJq-4k3ju47LvduoskNRk70uwRDrYrSHlsZXJgcwLHMj9iJ02EKRzvDgIszs2cUdMz9_maeDtWv2lzwYeyMbds9Ek09Ny7maDSRquAKaOnt9PUkm90btYq1rey0hV9HdI-WPjCFSrZrtdXj1bjqIW1s9FSSUksp2ezWbxZbunkY5ILhO2KFCo1ZsBcgavq1aIHe86o4HQuGWa_JZo6rvNuh3ymlCd9T598Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DktompG3F5PFDgRTyIWqQjQTL0AIeatg59VCJTjIQsLcebksTsviClrWyELV_saPWgR4RjP9metTTLioM33qlHg74QxYHGzu730bACZa0B4cYctAOaaZUYz_s_nbbKJqNPhcCGXrtlMBaSeK8aCV9u2wuZpz6YYuD5QISNdWl0Ue-C-vjoCiVvIJljMoO2eVbcgELY1N8OriLiGZZD3SL5X53hOJZvpdhjRjAxdb1fnDk_8w_IwSc0_K_Xl7F6tAxNobtWESoABLouPjerXBWekFlV3b97umDLupIBhvFHtIR4_PuH36JVMccRs44zElDEbpIU-e15CejWlxs7ez1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TI6WiYpNTG6H6Gr7gtqRtOr7MIj6GURYaQNfGAjznLDAnGQcfw91XIW4dxY59y1UxpvymoLcwO0LN-Cb3Unz4dCTZnbExwfpri2M9qjqv-AHNH0_eNQbRClCWKtc2nAt9M7Et-iX9z2MwVeuSokZOOteCZLslBIHyLpnNf8AQXS2bCTgCFtCrynQy5Ccp0VCg5XPplKhrRrR8PbqspirPQNU0D9nxjvEUoIhn27213FG8osnM0PSe1BKrB_rv9xXtVQV6Jb87BM4Ahp2n-UAt4v_t1mv0acXObySyOiqL-0HCBSYETNnGUGUMzuqS3raYgovV7q80e2j02ebJ_LjeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۵ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/438025" target="_blank">📅 01:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438015">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxVSKLYivwtOtjFqkSz59Asz15o2Siv_V9Je8huFnooBoQ87clW3nBaCUA4zQTA3S8cOGVcQksKfM86kN8dmwldDZGOTdHN-hs270PxRibSK6YcdeyZ0BpIemPjwUIwXiKZSqMB3BvLBAiR7FBR_q57_oKz4HRRw9VexrgMuB_mKg8A543qcn9-rZx-X3m0RLm6gXDAhY-6CaHHtmk73G30TOzrKVwgUoAgAlLBJe_z-V9HfS1QCD6lA6xeeKdcLamDAH5YonqsW5A_jfHn4Tn7sfxJrYGF499G60Sf46q552iPWldoDTaaPO_UlVEh2ct-T8eQ9GI_eXUZsHjjW9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffKsjkfT-Yf5p1PzodmI6BJUeePJZm1lCwdm-bZK8pMV0kb9TeE1JUipMolFvml_2HnWQOohq9j1RoeobEspMYT5npLVVylKJxumYBXyZ3RPTRdUquqH-smtiBLQWb9uWRD80rmJq2fIV6xqzG03zargTMlsuICed4opvQ8b4Wih3S3-rKDIibdrdspg1yeQ65JrkvdEfAOwZMsQvCrS9ul3E2XfnAfrsx6WZuXHIgkielLWjFaHqY5Ubgt3_DoCnNZrIC07922kcAHXyYJg_PtpMMuOECtmdtkI8eiNhLwp5pmQTPZJI1_q7nFDMJUec5S_NJaf8_Cua3qm9XOTNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0qIRYoj6LrqKgPF8GNCdQb8pJ-SXCR3t2LiY7szfdJsNqdSiZqRztlr2d0G1qmHbmoc1vg4q_uRnhocXvoOBW16gx-MEpTBOgEMloYg2RTyIHaQa7lPOlOYCEKxJHKskkZwlswNCnKcrcB8TqUnM9mJslWimLQb-pBFoFFceZOpUnnSBQxzGJ1orltVDyDd3H0CI5SEiaujB9YomcbDExjKEB0AV60gzXjI1GmoMw0O5EwOjNFoinV6awATKBToFN_CZyx5bwqukDzXVvUEQ-5hLq-exVFiHFhI3BT27UNwp95gb-lEIaoEntWXvJe0D0qRgfVSnYH22ovdxa-FuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mUO2_9DjJf88OecCxOjILmbcWb2eDXeUoM7fmS_xGA5nfCL-a98cjIQdsRaWZj2eO6YZQhaujjsnHasYGqlIMxWRHwzqnSKLL04e17YCP0EozWKwHYBdjiIlB0y0y7YM01Ha7GdgGbfxijz39gULgGGUIN1ogQbM9_Nikh9P-IBpuOK-5YYQ1xydF3nq4E6uO5jDwagicE76cAN-fCT__y10wCY2qI_aZRPOJToigifFHk0qkXZkHAsyXumNxQi0LDjCnKa9_Lzz0pG2i1kedzg8hiHTc-gCEHCcviJiYKZUMWxRop3XaRBmFdtp5B58NWn7RpkFjtWEbp14RGUlPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEhmv1SVTfojT20Wo5Jf3E2o4ZRqM5eQ3HNbdyVWYChhwirBr1_dQh7_SMRp0y0NYa44GBpOSgcQUCt_Ws8pQ0uVzJWX4ZqdFBGBg2_oZkWj0xvcwnIYdkvYRhMA3QIK6t20I5J1GN5MA6MsiJFaN5u9WYzvsIKZCAPvfxOv3vqGP0EzF7jafGaAzLFvZIrhTaA1IMM7FZRbFsYaKDdvBrpurkckQoA-4Bqg6lwyGrlLcXCTwaIcV3rrPt9rVbTOzNC2dequHBNZGDUyC-8frBCPeSZ3lcHDP0koWjToLBeJA8w83zUVN86cdeiTbvzlQbBEFMRBpwPEnpKCpgLB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_fL4SjZzuB6Noft-mllF9oPAKCz3WIrNAiqTYueFlh8XUYBp0wFm0DFwDN542QLwKF5HSPXCME_CcN5UtgFw5DvoblHFtAAWt-X1yu0mnZMmNAVJ9mq_KXhHCZ7qA9QwEIUhOc5QBuSjcVyY6KUOov8wgXFq50KsalS9iLjywZZMgFlAG8odD8Sl2OvG_NKxGDda2zZFJRxuBZrrm0maJKoy2qxlplHODBWg9KL6gRxcEF_7F-0HGdSXCVbz4O_zSHu37dncefgMxiTXfnKu2AfEispkbQSlCTQbZnQ4YiXnhEXoMEu9ME9WBfpDElZjTkGEnyHqY4vJQC7UZhMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kiF7XBVT6nkXtomCAl24PRXGc-sSgCrZX53aKQcO1JCWUFlg1QrCpUFB12g3JtathLnqOXkU6h2KgP6B2nNnW5gZrtUgKGtXeYUaQpmAAbnMzx634fn72tfTA2QosKQidqr8lTXAYcfVDj-93KIIwf49WzyNGukg3Pbct_pplrlY9gnTIpm0_dNr2Zzp0yloY4W8FhMs1vHAAhXfv9DHzMifC4Us2Taj4zRW4rUeOaTt9cmv3nuIwJi6ef1Io2phxFAeNd6Sj69sw_sFjKR34jENWGJCAH_QIpdBjaaafbwDIDi3gkerdRJs5dlQucw83oh_V-sSrlGwC-zXYRfjcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M643M7IL8YzFcKFQLNLzxQHzRzNVj79Y17cWhnJk-WLlWWzkHSFuIaL5Hr60Kv4aVWIE6ntEAJLWDpHUwJ33LAI_o759The5mn2kE4Mx_hgo9bMDrFFk9tUGuh2Azaap_fuYVhStMTjFQ3W9oRZF3-5znJ7IeBKQ-EcNKRt6YRG_FdNA1tTlwDsWl7GtU2vD32oeM80KSHzYS_WpwcOz2hH__WqQttq269cxV-G0059lPJKxwAUF_0aUE55elGFFx8_Tii6MTXCl4f2DJwJJqbgjRCXYimjuMPBnuYcQ49PyYmAOXiWSinNB6NJFZLQR_U-ft09IRRaPp8C-vOOOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rH2H56Ko3zp6LPu9tLEaJnUQvPO8haNszWFysj-BYUL-pVTkbozhZRugdgGlo8N8I72NeQXgdu_dTY52UVIkIKnHhgcuOt29qelgBUFmJQxqxkM8aqMJp0FPLfMipQ2WJdA7cxVZ4FFJR5x69-3w1uaclL6M4k0251U2kzsf83e2SHtTJqPYq6XfoTSb7KA_MFnazcql1ZTdayAEC1fVs2KFbNoUNA2wR0xzPH4eHWvx7yhOafH6VqZAgIKSGaDRRUY4F2YlWCfCrdZcvl6PGHe0ns2kZ5kZkj9wlcJb1sXCRbIES97WevXo2nBX8cF7HGJqxSKuYSv268Ko7hHBzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2vX3FbRz8XBhn1VhNy1Ar5fY5foQJdPUNvI61T93JLbgSRkD28XMYEY8voRiUegT2D_sroTfTkCh-ZgP7TDbK-IEb7okIml0l0kn6mp99ESXsM4CzqBobybaXXYZMVGTzJt1NPCMFHM2uENZJew2rybvBywGmDBBAGJ0C_vv2wj08DgIO7wLHavmfEpqkf3JJm5EWdfxg9g3PddBNQWeA9U5mfCc1zah4MYtWWIqhYR3gfK_PFC9V0YJY0o_ysFr8y-WH5fs1WX5JP02s8k8mDj0YNnYR2Mhss1aILlmMbp3TDHTLKhuif2mMh9EkRqA2-H_TPH6Gy-tye_BbLJpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438015" target="_blank">📅 01:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438014">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f525GQo0BaemrbQ0GTGRG9P2avnOMTIT0LIpsADrfI_EFNvb1veJ-wBQGdra1b7IOuu70Rg8HnGjBp3_tb_BD1mBHepbu_Ia6FkZmmkbVewyXc3pVECBieu-RNSam6klwpX4C1jAN2qV12kvQmUtGU8RYr1bhSySMxPUOxAPTj0lt1Srinj1A8HNiMH2y0bl4mezP--3kYjyVQ6maTRFslWf9-EJCsQTdCXo3cLpO0gCeop2tTESaaXmv0AlfWTZFwEZqjgd5MxFveoYTD5cxMAJ3QVkC0TxZ6OJqDp6LKy2jZUeBOXRgPDspkSKjzNof3eVX1Tk-QTERVUMl4tuBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چراغ سبز ترامپ به اسرائیل برای ادامهٔ توحش در لبنان
🔹
در حالی‌که نقض آتش‌بس توسط اسرائيل به یک روال مکرر و هر روزه تبدیل شده پایگاه آکسیوس گزارش داده دونالد ترامپ به اسرائیل برای تشدید حملات در لبنان چراغ‌سبز نشان داده است.
🔹
یک مقام آمریکایی به آکسیوس گفت:…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438014" target="_blank">📅 01:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438013">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqYN_gwMN1tPVh3j1XvPPTW5Zfh5UWqS1osNYZkq-zlLjC90Db0qtzj2DJTbiVXlB4CTXb8CkhpvHvvQVUekhKbaLbkxQSLktMgWHGwLNAdfSDfaUhv_qX1UuslfnSYzsg7DlbE1OWit0Yr3CIPd9GG67ETKAr6cMey480UcFgmpWbxdzfeAZnoKDXlmND-xPDgoZzxn2ZarCKPKlzUs_mRq5-2D6KTrC9Yn7bPvvevY57QgtjHe7RC15CmPxitteSfsaPryp2Uf4vTBvCaC13nc9hfxiqLGJIJlIso24SEvYPswi9jDZfDdjklai8qNwK-aK5T78ZOiitpJQGSWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاریخ احتمالی آغاز امتحانات نهایی مشخص شد؛ ۲۱ تیر
🔹
رئیس مرکز ارزشیابی آموزش‌و‌پرورش: امتحانات دانش‌آموزان پایه‌های یازدهم و دوازدهم از ۲۱ تیر به‌صورت حضوری برگزار می‌شود.
🔹
برگزاری آزمون‌ها منوط به دریافت مجوز از شورای تأمین استان‌هاست.
🔹
درصورتی‌که شرایط کشور به حالت عادی بازنگردد، تصمیمات جایگزین از جمله برگزاری امتحانات داخلی نیز بررسی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/438013" target="_blank">📅 00:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438011">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5255500874.mp4?token=UeM3g8tj5kYeW9v0nReO68mRq4nW_iGTga-EGqHpeJBQVEcOr11eevl24vL8XAvIhikr8pjxeBo1Otu7RzIbOxEzrLqvwbkpVKhPVjbp4OK1oLeliVffiwdINHceJQK5c52E7iTrQe8RlsLj2Tm2WCoVVrqBJXNL8XN4lFSWY6Sv44v-RNZXoPhNYBWZ4-4TocPKQvd9LiI1WWt5t-7s3-riD_AUrghzfgh0S0qMHt4XrPqviux0Xi_BbHdK_n5T3ulItgbVOqMQQr04FhhQb-x_LcwFQLc1_Lfrafvwwcq4V4FW5s1PfEyPDSlIPNdBWR84lrcSKkpXZ5xKDRNisw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5255500874.mp4?token=UeM3g8tj5kYeW9v0nReO68mRq4nW_iGTga-EGqHpeJBQVEcOr11eevl24vL8XAvIhikr8pjxeBo1Otu7RzIbOxEzrLqvwbkpVKhPVjbp4OK1oLeliVffiwdINHceJQK5c52E7iTrQe8RlsLj2Tm2WCoVVrqBJXNL8XN4lFSWY6Sv44v-RNZXoPhNYBWZ4-4TocPKQvd9LiI1WWt5t-7s3-riD_AUrghzfgh0S0qMHt4XrPqviux0Xi_BbHdK_n5T3ulItgbVOqMQQr04FhhQb-x_LcwFQLc1_Lfrafvwwcq4V4FW5s1PfEyPDSlIPNdBWR84lrcSKkpXZ5xKDRNisw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقر گروه‌های ضدایرانی در شمال عراق بازهم هدف گرفته شد
🔹
رسانه‌های عراقی اعلام کردند مقرهای گروهک‌های کُرد ضدایرانی در اربیل عراق هدف حملات پهپادی و موشکی قرار گرفته است.
🔹
به گفتۀ این رسانه‌ها، اردوگاه دارشکران در اربیل هدف حمله بوده، که طی این حملات دو تروریست کشته و هشت نفر دیگر زخمی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/438011" target="_blank">📅 00:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438010">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e3bcfd35.mp4?token=pVMI4IuVjBfVii01P013Om_92VDXigni6Htnyx8dpVxQEFxFoIaoBRsT4ZTVs3hyPqZGUga3P-rP4eFnA-IGaI4yAhw4DrgGnvO_aWMyhmy8jJmQoPsKwRIgO45H2mqNo9XvQhSSyuQx1f2gw4YYsLPbViRrSDSx8wPEcQ7hStl4mUSjJQU34cQ1M8CZJKXreTEaZtUxZ9BUz1WIPSZsPG3KSSWUOjCxrHICAB-4tkJfnSleSzEX7vwNSNU2ewbhQvrDvGElt5LYjJ5utNE8ZfD3tWn5PvU896xUxqg4S0i5LTGbzKJjAmmySrLlvbIq3NWPJo4boyacW9k0RLN1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e3bcfd35.mp4?token=pVMI4IuVjBfVii01P013Om_92VDXigni6Htnyx8dpVxQEFxFoIaoBRsT4ZTVs3hyPqZGUga3P-rP4eFnA-IGaI4yAhw4DrgGnvO_aWMyhmy8jJmQoPsKwRIgO45H2mqNo9XvQhSSyuQx1f2gw4YYsLPbViRrSDSx8wPEcQ7hStl4mUSjJQU34cQ1M8CZJKXreTEaZtUxZ9BUz1WIPSZsPG3KSSWUOjCxrHICAB-4tkJfnSleSzEX7vwNSNU2ewbhQvrDvGElt5LYjJ5utNE8ZfD3tWn5PvU896xUxqg4S0i5LTGbzKJjAmmySrLlvbIq3NWPJo4boyacW9k0RLN1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رهبر شهید انقلاب: آقا گفتند مهریهٔ دخترم همان ۱۴ سکه است که برای دیگران سفارش میکنم  @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/438010" target="_blank">📅 00:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438009">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
دقایقی پیش مردم در بندرعباس صدای چند انفجار شنیدند
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست.
🔹
همزمان در خلیج فارس حوالی سیریک و جاسک نیز صداهای مشابه شنیده شده است.
🔸
سحرگاه امروز یک فروند پهپاد متخاصم در محدوده خلیج فارس توسط نیروهای مسلح ایران منهدم شد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/438009" target="_blank">📅 23:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438008">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‌
🔴
یک منبع در وزارت ارتباطات: مصوبهٔ بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴، دقایقی پیش از سوی رئیس‌جمهور به وزارت ارتباطات ابلاغ شد.  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/438008" target="_blank">📅 23:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438007">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad9a3ece8.mp4?token=MzTbejLcRo90fpHP8RXNtsxOe0I2oO2HbmNDRs6QM4zTbkHCF7O9BWWV66dtgXv56egq5pHXu2TFpXLi4RSqBLGZT0Omdq3lf6ZJnYC01_drCnU2E6BLwwcVYWLWX5OsD33xCmlvfk4W8lu72xeFQ49YJkmDQNVGVFGqxkgO09Je4HWj848H3n38BvVZPN_qJKeqxtszl7g__vVL6vpRyjwt0JDn7sOXoVK2g6UR0z9yOrqxgrgw37Wb7PCqogcLI_4gmgQA-oG_-cu-j6fIIqXcg5cEPwmIgnDmi747OwnQg1F8lETKyf5OuSCjaYOVsXP0Vy7hRnq2m785plWB1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad9a3ece8.mp4?token=MzTbejLcRo90fpHP8RXNtsxOe0I2oO2HbmNDRs6QM4zTbkHCF7O9BWWV66dtgXv56egq5pHXu2TFpXLi4RSqBLGZT0Omdq3lf6ZJnYC01_drCnU2E6BLwwcVYWLWX5OsD33xCmlvfk4W8lu72xeFQ49YJkmDQNVGVFGqxkgO09Je4HWj848H3n38BvVZPN_qJKeqxtszl7g__vVL6vpRyjwt0JDn7sOXoVK2g6UR0z9yOrqxgrgw37Wb7PCqogcLI_4gmgQA-oG_-cu-j6fIIqXcg5cEPwmIgnDmi747OwnQg1F8lETKyf5OuSCjaYOVsXP0Vy7hRnq2m785plWB1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رهبر شهید انقلاب: تمام وسایل زندگی شخصی آقا به اندازه یک بار وانت بیشتر نمی‌شد.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/438007" target="_blank">📅 23:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438006">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea7803896f.mp4?token=VNfkNZw1QhKJm6dOwxbh0eB7ygPaAbJHlrtDrTjiY6IjfyDYDbwnxVMo6MTx4dcgcjfEqfcfpi070_9QT9diuJPfWM72LLxkXBNiYT7q8ozPy4iQ2bt315hJ4AYEgBczyTD1sClrPSKQAc1PLttJt8jpTgsCcmRXGpg1WddF_YysDXoP84YhIaY5xps6Qg-j2wbWJ-DtO7ueHuw1ZTceUStOFDaZc7xHfIoudzfCb40ebk1plYD4gnvOsC1u29_xiBGbU7sgOObZ88Q3H15hrjrw40Chvbunq8LBul_ATj-6ZxffaF0fZ0msaqUyLOn-VCy3mcGrOH2muaPf6kSS2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea7803896f.mp4?token=VNfkNZw1QhKJm6dOwxbh0eB7ygPaAbJHlrtDrTjiY6IjfyDYDbwnxVMo6MTx4dcgcjfEqfcfpi070_9QT9diuJPfWM72LLxkXBNiYT7q8ozPy4iQ2bt315hJ4AYEgBczyTD1sClrPSKQAc1PLttJt8jpTgsCcmRXGpg1WddF_YysDXoP84YhIaY5xps6Qg-j2wbWJ-DtO7ueHuw1ZTceUStOFDaZc7xHfIoudzfCb40ebk1plYD4gnvOsC1u29_xiBGbU7sgOObZ88Q3H15hrjrw40Chvbunq8LBul_ATj-6ZxffaF0fZ0msaqUyLOn-VCy3mcGrOH2muaPf6kSS2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رهبر شهید انقلاب: تمام وسایل زندگی شخصی آقا به اندازه یک بار وانت بیشتر نمی‌شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438006" target="_blank">📅 23:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438005">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacf521b07.mp4?token=uDvQQz_NdMriTl-qfFBLqttJCWEGaWQZd_JwCj6vBC4ohmJeb8AH67Py16RW_QmY1c1NprAJnu2EDbo7VhgDv8OpjH-geKu0fPoWtIBMnAkQLyI7sJImh3Z1E46DDsjdfBS3v9LGcPUJ6hA5tAe1Oeqx0zK2vSvZ3Lp-hubJUtMNHdwnxipdOXDsINKkdSAb5vFZVrC-OddCQjfSuZRJkkspYTm6nJA_xOrPyWS4DTaCH2a3eqJnqw0MmuCD_R04SRq4OMyLUyMVTZkNA5rIqcYKWvBxqjqs_PYczRe_ozg6Y5FyfuUDqXsZtbIytdRp0TkhGE_QDyNmJgm-UaebuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacf521b07.mp4?token=uDvQQz_NdMriTl-qfFBLqttJCWEGaWQZd_JwCj6vBC4ohmJeb8AH67Py16RW_QmY1c1NprAJnu2EDbo7VhgDv8OpjH-geKu0fPoWtIBMnAkQLyI7sJImh3Z1E46DDsjdfBS3v9LGcPUJ6hA5tAe1Oeqx0zK2vSvZ3Lp-hubJUtMNHdwnxipdOXDsINKkdSAb5vFZVrC-OddCQjfSuZRJkkspYTm6nJA_xOrPyWS4DTaCH2a3eqJnqw0MmuCD_R04SRq4OMyLUyMVTZkNA5rIqcYKWvBxqjqs_PYczRe_ozg6Y5FyfuUDqXsZtbIytdRp0TkhGE_QDyNmJgm-UaebuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره‌ای از اولین دیدار پوتین با رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/438005" target="_blank">📅 23:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438004">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38969e4884.mp4?token=C0LJkGuOlo6YTZAnr0T3gt6bXnYkG0GyuAbjzB0ob6wG0ZgwVAJrrO4PowJCPmbOEkJs_3nUQGXfve9cDirkw1BtJOxEIHNm0HfNf2aZ9V2m7uHN1EyazqqVg71CMv0XUWV3VcE4V3eH07bXY-ENAV3-erEBO6IYqFb_S4qiQlvZoC-duyA98dA92Wduviys2TVuvHlKg4eeExhOfg-glFUuD6i5wyi5Mr1u0Ixh_WEBh13dem177tNxhUwhfzV5dAwGLdsJMHaBWgqLkKNmVNQ9y3rb0nzU9BH6NV3AXy4TJlK7oAiNEpmeKkVcPMaNsBHdRYpqtRmHTqKyVxv1bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38969e4884.mp4?token=C0LJkGuOlo6YTZAnr0T3gt6bXnYkG0GyuAbjzB0ob6wG0ZgwVAJrrO4PowJCPmbOEkJs_3nUQGXfve9cDirkw1BtJOxEIHNm0HfNf2aZ9V2m7uHN1EyazqqVg71CMv0XUWV3VcE4V3eH07bXY-ENAV3-erEBO6IYqFb_S4qiQlvZoC-duyA98dA92Wduviys2TVuvHlKg4eeExhOfg-glFUuD6i5wyi5Mr1u0Ixh_WEBh13dem177tNxhUwhfzV5dAwGLdsJMHaBWgqLkKNmVNQ9y3rb0nzU9BH6NV3AXy4TJlK7oAiNEpmeKkVcPMaNsBHdRYpqtRmHTqKyVxv1bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره‌ای از اولین دیدار پوتین با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/438004" target="_blank">📅 23:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438003">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d49477a9.mp4?token=Y24rLrYfBrRnvkDu0bLzk5xGcChpE1S2p0k-ne_3v-oF9-ys39OHmPmD3MmLujm9U0guOxLus_-8-0aTviQxHIk2_Vwvth95GP13r1cTHNXBtJIfFRmmAny69P1qX5LhhPDRQQkN5KHfELy4NjVnACXE0tUMl2ch9IW5TCpfW6jcM0py7ws4EW_M7SBqfJpzbv4RrDq6E5_57unUzuLDOs17_IxPjJkAeWqrOD09vB_eMrREoC-nLWzj_ShEFTiQ3ojmPRyMGI4NR1LyxoNCwqjoSoFtoop79rzEYNxU5JbzXReQv157ZvBfuHDFMkbQA3oOP5UAEIbNTpSw5CGQNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d49477a9.mp4?token=Y24rLrYfBrRnvkDu0bLzk5xGcChpE1S2p0k-ne_3v-oF9-ys39OHmPmD3MmLujm9U0guOxLus_-8-0aTviQxHIk2_Vwvth95GP13r1cTHNXBtJIfFRmmAny69P1qX5LhhPDRQQkN5KHfELy4NjVnACXE0tUMl2ch9IW5TCpfW6jcM0py7ws4EW_M7SBqfJpzbv4RrDq6E5_57unUzuLDOs17_IxPjJkAeWqrOD09vB_eMrREoC-nLWzj_ShEFTiQ3ojmPRyMGI4NR1LyxoNCwqjoSoFtoop79rzEYNxU5JbzXReQv157ZvBfuHDFMkbQA3oOP5UAEIbNTpSw5CGQNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فرزند شهید تنگسیری از آخرین تماس تلفنی با پدرش
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/438003" target="_blank">📅 23:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438002">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1a1f2780.mp4?token=oubueU7UL2LP6kf-4HJWM_jaNLINWSk2Wh6ZgpRVStpxRkeR0cMT341DW_4z8rzmGrYw1DsfeJqyoi6TId93zOTMS61hpcwdjuwLZSkRS7bG88CM_FPd_jxsfOtUU3apF57VFE7dM9xk93bgKCvjrwjqiZsNAbvs3KQMF0ypx9nhpwX7GVuIByY_bH1yPcT2y0vNRz2ih1IlJtQmfuOEH8SUB5rr7PFDhvWDc4An3CNA_rwLfyVk373fQL4xEyDk8FnKKew4__DbxHFFee2AGvoZmdS3Bg2dmjGdMHDq8EzY8uZGuS9mvmHMZtsI53i7qRNZ3YcuMU9dQhNKpyt9yHFtX3FGpmGUsHAlyAD4KKXUOmUlpvxQCGkX6nS5pM5mrrnGRBHOqeBN_i9UBvhXSTkSW0rnALibBPvF6tmHVRBvtztY4i0JhcaBLutnQviXY2RPL18fbuWcU_B8kWLz-AoBeBzJ9LQZupTWaWk2jtfHkQCFyffms0iSIEKxdQTNs7o1osYlhIVN1snJA9UHr_C6V1Fs2jHSajrC2K_vvGhGG07ibjGno5OwPs2HWh444pdqEL2-YGj0qDA6XDnGcFD6GS7wtBD94WRzWY0RcPzJOSyHnK1rUeU4YxKtxMho1vihApQR2xzhasXJadm3MGo1wbYdluvDy2jRCDlgfm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1a1f2780.mp4?token=oubueU7UL2LP6kf-4HJWM_jaNLINWSk2Wh6ZgpRVStpxRkeR0cMT341DW_4z8rzmGrYw1DsfeJqyoi6TId93zOTMS61hpcwdjuwLZSkRS7bG88CM_FPd_jxsfOtUU3apF57VFE7dM9xk93bgKCvjrwjqiZsNAbvs3KQMF0ypx9nhpwX7GVuIByY_bH1yPcT2y0vNRz2ih1IlJtQmfuOEH8SUB5rr7PFDhvWDc4An3CNA_rwLfyVk373fQL4xEyDk8FnKKew4__DbxHFFee2AGvoZmdS3Bg2dmjGdMHDq8EzY8uZGuS9mvmHMZtsI53i7qRNZ3YcuMU9dQhNKpyt9yHFtX3FGpmGUsHAlyAD4KKXUOmUlpvxQCGkX6nS5pM5mrrnGRBHOqeBN_i9UBvhXSTkSW0rnALibBPvF6tmHVRBvtztY4i0JhcaBLutnQviXY2RPL18fbuWcU_B8kWLz-AoBeBzJ9LQZupTWaWk2jtfHkQCFyffms0iSIEKxdQTNs7o1osYlhIVN1snJA9UHr_C6V1Fs2jHSajrC2K_vvGhGG07ibjGno5OwPs2HWh444pdqEL2-YGj0qDA6XDnGcFD6GS7wtBD94WRzWY0RcPzJOSyHnK1rUeU4YxKtxMho1vihApQR2xzhasXJadm3MGo1wbYdluvDy2jRCDlgfm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین یاحیدر بروجردی‌ها در ۸۶ شب حماسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/438002" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438001">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e7101796.mp4?token=NPgNFfJjxnMV4UNaY_KgNV3bagHYQUyZ3nlGzsuyozYg7CjV0gZgWQRhf0JUg07tcfCXIimbgJT3qZEy6RLlxRxzqOg8ZpjbZ72YiXUF6Bn7SFYCQEDd-c8hzYO-bOEWfGpwCCpf3V5V5hqEJygGMKi4fekLfaKfXJzzNd9vlVtwhGTlzZi0lpxsGh-NRSu5FKcYAgR-ax1XHk2hrTLIXncU8hg12m8W9_cZsE6mqU2gnG3HiMLT5dl9bDbhcef8nLMOcS-njXWSoQo2IopHI2foluEWHUHF7xfZd6tFkTRV2REkQNnAS0MVb_XMU2a4kXdJkZg4eHSg8wrBCMho5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e7101796.mp4?token=NPgNFfJjxnMV4UNaY_KgNV3bagHYQUyZ3nlGzsuyozYg7CjV0gZgWQRhf0JUg07tcfCXIimbgJT3qZEy6RLlxRxzqOg8ZpjbZ72YiXUF6Bn7SFYCQEDd-c8hzYO-bOEWfGpwCCpf3V5V5hqEJygGMKi4fekLfaKfXJzzNd9vlVtwhGTlzZi0lpxsGh-NRSu5FKcYAgR-ax1XHk2hrTLIXncU8hg12m8W9_cZsE6mqU2gnG3HiMLT5dl9bDbhcef8nLMOcS-njXWSoQo2IopHI2foluEWHUHF7xfZd6tFkTRV2REkQNnAS0MVb_XMU2a4kXdJkZg4eHSg8wrBCMho5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما مسلح به الله‌اکبریم
🔹
سیل خروشان جمعیت خرم‌‌آبادی‌ها در موج ۸۶.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/438001" target="_blank">📅 23:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438000">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
رئیس کمیسیون امنیت ملی مجلس: تا آمریکایی‌ها ۵ اقدام اعتمادساز را انجام ندهد، چیزی به‌نام تفاهم و مذاکره با آمریکا معنی ندارد
این اقدامات عبارت‌اند از:
🔸
۱. خاتمهٔ جنگ در تمام جبهه‌ها به‌ویژه لبنان
🔸
۲. برداشته‌شدن محاصره و دزدی دریایی آمریکا
🔸
۳. تردد کشتی‌های غیرنظامی از تنگهٔ هرمز با ترتیبات ایرانی
🔸
۴. تعلیق ۳۰ یا ۶۰ روزهٔ تحریم‌های نفتی
🔸
۵. آزادسازی پول‌های بلوکه‌شدهٔ ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/438000" target="_blank">📅 23:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437999">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gShM_xwVZpuTM5Ogmtl0lnBrvOaybzsECDwGu2gO1PluUd_-QX1np92moWsXfPc_uJF1FNEmohHEr9ty3FE4xA3dvQOl73KYXF9oLC2TLlKzsW8lDuLvurfUqYKwQOVn_CTOUafQelvWrlUPEuKhlJuy-_m_EoOLn7VLkWszgbdjA_r19Q31aAHAMOfyJnfJ0I_eglcICwBEIxKRUQxprGvYvHGeyxcyn8amEj4bpCbwFm3wTjBwbrzlTyMXn1XKLTFG3e22EVLO6sMQ4L4cStwAJohy6SYG86UNuzDOirwaTQ_Tgo1xnzPvepcjINQW8SXoXqVbow9D_K7h1qOKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌نوایی اعراب خلیج‌فارس با اسرائیل علیه حزب‌الله
🔹
دبیر شورای همکاری خلیج‌فارس امروز در سخنانی از اظهارات دبیرکل حزب‌الله علیه حکام بحرین اظهار عصبانیت کرد.
🔹
شیخ نعیم قاسم روز گذشته در سخنانی به‌شدت از بدرفتاری و اعمال فشار دولت بحرین علیه شیعیان انتقاد کرده بود.
🔹
شورای همکاری خلیج‌فارس شیخ نعیم قاسم را متهم به دخالت در امور بحرین کرده و گفته شیعیانی که در بحرین سرکوب شده‌اند برای ایران جاسوسی می‌کردند.
🔸
دولت بحرین به‌تازگی موج جدیدی از اعمال فشار علیه شیعیان بحرینی را با اخراج و سرکوب آنان آغاز کرده و تاکنون بیش از ۲۸۰ نفر بازداشت شده و مورد شکنجه قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/437999" target="_blank">📅 23:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437998">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8fa5ae42e.mp4?token=CpdSlY43FIRM2B3CumdpxfzwUrziqNKbrFEWpq3YnHOz_6UFPYupeSAVxesTofS9_kx_jGvRw31Vj-OFYL3oInSWSlhEiO_xHOv3k3KfFNlXhjmB0xdN9kPpHZ9mxY8iM9fCc0bv90q-91GnjFERgYnvPyI83bMYR8WVAqMA97AUrsZM6K-NaJZP67QI3thHrBG70ejvgr2p074A4DINIAvnBO73XFq9-FpjSeVguJW8mMUx3ciLan9GbRHjsrwn-SV2XdlD6oOEuyge6ajNNTodZ6f9H6f5dwoMxVz8oInGMnMkcRzJfFNkTHDHNtvqIRM9dfbPADvC4QjZNcW5Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8fa5ae42e.mp4?token=CpdSlY43FIRM2B3CumdpxfzwUrziqNKbrFEWpq3YnHOz_6UFPYupeSAVxesTofS9_kx_jGvRw31Vj-OFYL3oInSWSlhEiO_xHOv3k3KfFNlXhjmB0xdN9kPpHZ9mxY8iM9fCc0bv90q-91GnjFERgYnvPyI83bMYR8WVAqMA97AUrsZM6K-NaJZP67QI3thHrBG70ejvgr2p074A4DINIAvnBO73XFq9-FpjSeVguJW8mMUx3ciLan9GbRHjsrwn-SV2XdlD6oOEuyge6ajNNTodZ6f9H6f5dwoMxVz8oInGMnMkcRzJfFNkTHDHNtvqIRM9dfbPADvC4QjZNcW5Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
​۱۰ سال بعد، از این شب‌های خیابان چه به یاد می‌آوری؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/437998" target="_blank">📅 22:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437997">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎥
از دل دهلران تا قلب ایران؛ «حکم آنچه تو فرمایی»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/437997" target="_blank">📅 22:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437996">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/406bbcee05.mp4?token=nuVDHafAewA3Y2-rY10ETDWhQpLgzNlybbX0FmDl66qsvnnREexq33ZOY27o-3Sk163czhD8vBziOJ_QqKxSS9bGrXbjGyIQpHZpOYnnszptpI9vCFrOkm8vPMaMXB2blnzdFufH8M9NxjWrHniemNbu4qeBMX9bWdi8XcnO0MmUZlj2L9t3g9DlbwZ1zK_ixEcogSVym4c6Ik4o0X90ESu9QxW1AoDxI4Y-5PjUUPSXELUHq-eWEFIUmO8_Ea2RcOEEwQEr6Pdenc2sxUkL9pXyirLWg-Ole_tmzNJtDM2ziC0K8QqFu75Sue4TrhfkdLzmlWoIIDhE0JpoZZmtKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/406bbcee05.mp4?token=nuVDHafAewA3Y2-rY10ETDWhQpLgzNlybbX0FmDl66qsvnnREexq33ZOY27o-3Sk163czhD8vBziOJ_QqKxSS9bGrXbjGyIQpHZpOYnnszptpI9vCFrOkm8vPMaMXB2blnzdFufH8M9NxjWrHniemNbu4qeBMX9bWdi8XcnO0MmUZlj2L9t3g9DlbwZ1zK_ixEcogSVym4c6Ik4o0X90ESu9QxW1AoDxI4Y-5PjUUPSXELUHq-eWEFIUmO8_Ea2RcOEEwQEr6Pdenc2sxUkL9pXyirLWg-Ole_tmzNJtDM2ziC0K8QqFu75Sue4TrhfkdLzmlWoIIDhE0JpoZZmtKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سطر ۸۶ از دفتر مقاومت مردم بجنورد
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/437996" target="_blank">📅 22:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437993">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صدور حکم اعدام برای سرپل عملیاتی موساد
🔹
با حکم دادگاه، غلامرضا خانی شکراب، سرپل عملیاتی سرویس اطلاعاتی موساد در خارج از کشور، که هدایت یک شبکه خرابکاری در داخل را برعهده داشت، به اعدام محکوم شد.
🔹
این جاسوس موساد با اقامت در یکی از کشورهای منطقه، اقدام به شبکه‌سازی در داخل ایران کرده بود. او در مدت کوتاهی، ماموریت‌های مختلف اطلاعاتی و عملیاتی را با هدف ایجاد ناامنی، رعب و وحشت، ترورهای هدفمند، اخلال در نظم و خدمات‌رسانی عمومی و همچنین انجام اقدامات تبلیغی به نفع دشمن، در چند استان کشور اجرا کرد.
🔹
پس از رصد این اقدامات، پرونده در دستورکار سازمان اطلاعات سپاه قرار گرفت. با اشراف تخصصی نیروهای امنیتی، این جاسوس و تمام اعضای شبکه تحت هدایت او شناسایی شدند.
🔹
از آنجا که «غلامرضا خانی شکراب» متهم اصلی به‌عنوان سرپل عملیاتی در خارج از کشور حضور داشت، طی یک عملیات پیچیده و با استفاده از ترفند فریب اطلاعاتی، غافلگیر و به داخل کشور منتقل شد؛ هم‌زمان، سایر اعضای این شبکه نیز در یک اقدام هماهنگ در چند استان دستگیر شدند.
🔹
در نهایت، پس از طی مراحل قانونی، برگزاری جلسات علنی دادگاه و دریافت دفاعیات متهم، براساس مدارک، مستندات و اعترافات صریح، رای دادگاه صادر و نامبرده به اشد مجازات (اعدام) محکوم شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/437993" target="_blank">📅 21:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437992">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74b46e53d2.mp4?token=hOHzCUiuBh_bKbJMNIephxgZyIhSefSVJnBKXq8hpViBz97WUuSPz0T4cFj86kXNHPJ-65PjDQ47sBhlig_xc-X7_NjM4Z8OcxaTtABDwwzAuF-HXStXBGiVya24JOUcpPKqMnMGpMcPAS80BQmQ3EbVpmPkWHbn7NgiMyGVCyRP4I2k9wu_zgUWeNpMhkTq6Y9yWCyGk9pWIcZi0KcsWmYWXHjvSt5WRWHrvMvYou0De5qZQylca836mNSZ4lfNog8N_6O2QU91eMd7ZS5i9j0JvX9aI5wEJ6Azill0M-uzb6XHX4YrPQrFT9GLKecQQqdlhNXyK3oLbi9crXyvYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74b46e53d2.mp4?token=hOHzCUiuBh_bKbJMNIephxgZyIhSefSVJnBKXq8hpViBz97WUuSPz0T4cFj86kXNHPJ-65PjDQ47sBhlig_xc-X7_NjM4Z8OcxaTtABDwwzAuF-HXStXBGiVya24JOUcpPKqMnMGpMcPAS80BQmQ3EbVpmPkWHbn7NgiMyGVCyRP4I2k9wu_zgUWeNpMhkTq6Y9yWCyGk9pWIcZi0KcsWmYWXHjvSt5WRWHrvMvYou0De5qZQylca836mNSZ4lfNog8N_6O2QU91eMd7ZS5i9j0JvX9aI5wEJ6Azill0M-uzb6XHX4YrPQrFT9GLKecQQqdlhNXyK3oLbi9crXyvYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقدیر رهبر انقلاب اسلامی از میدان‌داری مردم سیستان‌وبلوچستان
🔹
هیئتی ویژه از سوی حضرت آیت‌الله سیدمجتبی خامنه‌ای، رهبر معظم انقلاب، به عنوان نخستین مقصد استانی برای قدردانی از ایستادگی و حضور حماسی مردم سیستان‌و بلوچستان در دوران «جنگ تحمیلی سوم» به این استان…</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/437992" target="_blank">📅 21:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437991">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a49a8d2b1.mp4?token=tcze9yoiEc3T5bHqFUJn84wh80MK2Iwt5I3R89PfsrQCKxqIHnyNM1mjfHDrrgEORI1VBDtd-20elIONR5KmclPBqTX9Lh09uO0y-05W0dx3G4wNrumTcvas04PD-aU_PtkWyHP7lG1pdO-rVy6ruhHCM6k5_Yf8JrhF28GuMGiRIvyYasqtaceswFUIRK93p0YXLUvZF3valzvrtLBadTyhhTfJm9eIOiKei0ue5Y4xGpybgSgtNkPzJcEFqLkzgg9BwIGMu9A2Jo-DkPQdhdkUwtMiXLcCQHhtOaqXNpLzNcmVx57tEPNcJSAqI6hkQh9YZcVeayLPdsZaUoOBjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a49a8d2b1.mp4?token=tcze9yoiEc3T5bHqFUJn84wh80MK2Iwt5I3R89PfsrQCKxqIHnyNM1mjfHDrrgEORI1VBDtd-20elIONR5KmclPBqTX9Lh09uO0y-05W0dx3G4wNrumTcvas04PD-aU_PtkWyHP7lG1pdO-rVy6ruhHCM6k5_Yf8JrhF28GuMGiRIvyYasqtaceswFUIRK93p0YXLUvZF3valzvrtLBadTyhhTfJm9eIOiKei0ue5Y4xGpybgSgtNkPzJcEFqLkzgg9BwIGMu9A2Jo-DkPQdhdkUwtMiXLcCQHhtOaqXNpLzNcmVx57tEPNcJSAqI6hkQh9YZcVeayLPdsZaUoOBjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: از اینکه حرفی بزنم که خلاف جهت رهبری باشد اجتناب می‌کنم؛ چراکه این مصیبت بزرگی است.  @Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/437991" target="_blank">📅 21:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437990">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d19eee5e.mp4?token=Aid9aQpfdvT2Y_44jVSCcu6oprQila1_cSw1z0k7unQiSMdNNg1RWtLpZAveUBGzLTA4cRdbXeEL477vs6HcYHbHq2DGOo-iWVLPVP2FVGMypd7d6LVQPuvhdchJ99gG_1MVVM3vmPuPU6KE1W16KsZtp7b7uDvJV_fMNgqPfE3wUgj417fKM5J9KnBHGJ3KPX3lrIpNzSTiwQ8qsfje7jF5n8SbaPr7stMyiES5DQr6i7sX0Qmk3eEJypKOFQr_RxcnKfaMqrimaSQCQsrVpbWI4gXo6q4hDumRxiNhGkUTEnEG8q7XM_qoYabPP44I56Z5x-mwwltZhya5dUGQ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d19eee5e.mp4?token=Aid9aQpfdvT2Y_44jVSCcu6oprQila1_cSw1z0k7unQiSMdNNg1RWtLpZAveUBGzLTA4cRdbXeEL477vs6HcYHbHq2DGOo-iWVLPVP2FVGMypd7d6LVQPuvhdchJ99gG_1MVVM3vmPuPU6KE1W16KsZtp7b7uDvJV_fMNgqPfE3wUgj417fKM5J9KnBHGJ3KPX3lrIpNzSTiwQ8qsfje7jF5n8SbaPr7stMyiES5DQr6i7sX0Qmk3eEJypKOFQr_RxcnKfaMqrimaSQCQsrVpbWI4gXo6q4hDumRxiNhGkUTEnEG8q7XM_qoYabPP44I56Z5x-mwwltZhya5dUGQ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اگر ارز را در زمینه کالاهای اساسی اصلاح نمی‌کردیم، مطمئن باشید که الان با قحطی مواجه می‌شدیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/437990" target="_blank">📅 21:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437989">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a16baf27.mp4?token=auYD-tfp8WPjHDv7ua57HNk47RhmdG-8jYc2XA9b8J17hOJtwlzD6PPHif7aobWL1dcCcDs4XdZNe4u82YgofJsq3WQuBcbSmwrBjjA4cNYb4xangrbDTghiOKD0m-PMoH0Ju--Scn8B9AWVEZ4xtsPnVpYgS61LInpPj9xOwqkevpoVtcIUY8a2e6FMcPrZj7mGoVECMZ7MVDS7eMh_6Z6bkwdCJt9V12oALv5IBz05I6VNNJHOktMlxoVEWdRNz9ihtic-ul8m9bZSuobDEKUW26-yFIm-RwqhnOq1EzZj-CMv87MVsK5vePr4wi_SDi7yA6E3UG4RGdthJm7trw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a16baf27.mp4?token=auYD-tfp8WPjHDv7ua57HNk47RhmdG-8jYc2XA9b8J17hOJtwlzD6PPHif7aobWL1dcCcDs4XdZNe4u82YgofJsq3WQuBcbSmwrBjjA4cNYb4xangrbDTghiOKD0m-PMoH0Ju--Scn8B9AWVEZ4xtsPnVpYgS61LInpPj9xOwqkevpoVtcIUY8a2e6FMcPrZj7mGoVECMZ7MVDS7eMh_6Z6bkwdCJt9V12oALv5IBz05I6VNNJHOktMlxoVEWdRNz9ihtic-ul8m9bZSuobDEKUW26-yFIm-RwqhnOq1EzZj-CMv87MVsK5vePr4wi_SDi7yA6E3UG4RGdthJm7trw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اگر ارز را در زمینه کالاهای اساسی اصلاح نمی‌کردیم، مطمئن باشید که الان با قحطی مواجه می‌شدیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/437989" target="_blank">📅 21:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437988">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">چراغ سبز ترامپ به اسرائیل برای ادامهٔ توحش در لبنان
🔹
در حالی‌که نقض آتش‌بس توسط اسرائيل به یک روال مکرر و هر روزه تبدیل شده پایگاه آکسیوس گزارش داده دونالد ترامپ به اسرائیل برای تشدید حملات در لبنان چراغ‌سبز نشان داده است.
🔹
یک مقام آمریکایی به آکسیوس گفت: «انتظار اسرائیل هرگز این نبوده که منفعلانه حملات به غیرنظامیان را تحمل کند. ما دولت بایدن نیستیم.»
🔹
ادعای این مقام آمریکایی در حالی مطرح شده که بیشترین کمک‌های آمریکا به رژیم صهیونیستی برای نسل‌کشی در غزه و حملات در لبنان در دوران ریاست‌جمهوری جو بایدن انجام شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/437988" target="_blank">📅 21:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437987">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نماز عید سعید قربان روز چهارشنبه ۶ خرداد به امامت آیت‌الله سید احمد خاتمی در دانشگاه تهران اقامه خواهد شد.
🔹
در‌های دانشگاه از ساعت ۶ صبح باز و نماز رأس ساعت ۸ اقامه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/437987" target="_blank">📅 21:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437986">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951378c241.mp4?token=BqFsO29JhN2572cBHq87y3FwozO7ypXRy2CbUgDwbULuznqgPLaxyRwvawLoHrDnxJoFPv6qYKb6ijU99XsV4cotP3vW2BxkS5y87RQa7DYpw10LcEkxAZEbdxPMffVPS-4Z34UnADmRZ8DEh9xn6Gd12alFJcW5bAYa0dlQk4gN6wHvMJkDn5nkafiC0pYVJMW0WkO6P0xTRaR04f5wrNhALbIFlXT7NLRaCNZIrfhAG1Sc50yRHiY3MoHyyctfa-f8JmRFBXGWJYs0Fkf_Ky3NaDLU7cVywGoLQtjSoFHrsx5m6KT0ImFp3svK7ChOQKW-7D9Y9rQ-Ndz_sOkKPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951378c241.mp4?token=BqFsO29JhN2572cBHq87y3FwozO7ypXRy2CbUgDwbULuznqgPLaxyRwvawLoHrDnxJoFPv6qYKb6ijU99XsV4cotP3vW2BxkS5y87RQa7DYpw10LcEkxAZEbdxPMffVPS-4Z34UnADmRZ8DEh9xn6Gd12alFJcW5bAYa0dlQk4gN6wHvMJkDn5nkafiC0pYVJMW0WkO6P0xTRaR04f5wrNhALbIFlXT7NLRaCNZIrfhAG1Sc50yRHiY3MoHyyctfa-f8JmRFBXGWJYs0Fkf_Ky3NaDLU7cVywGoLQtjSoFHrsx5m6KT0ImFp3svK7ChOQKW-7D9Y9rQ-Ndz_sOkKPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهادری جهرمی از نقاشی در میدان می‌گوید
@Farsnart
_
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/437986" target="_blank">📅 21:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437985">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7589a255ce.mp4?token=fspCLKF0bGLVv1DOt8omB_Ew1So8V7-jfdBMAvXirKZftfUKpkMmw_5mBXzPpR-irhLla_wDtFGaLgmpTljQDSuCl6DKROHQSI5AHAqYwfgfiB84BJITEL54Y0WcR_qKf_QfexpkW3TTfo4C39uzBrbxZHoxOtDFFlNlo0iR93H_wOw0a56YT-jaAQ0WN5GfbU10svY32Qrl5oyRX380fv83fVWYzjFUqf9WcV-OsIV783rY7cb8s-tu-M05mS6lMlw1suy5yp3PWHfiSOZd6VTODZQwAJvpav4YA0Q9wa2QqQGX7x228d5hvR7N232XaZ16upQFfTsycVB1uQJkeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7589a255ce.mp4?token=fspCLKF0bGLVv1DOt8omB_Ew1So8V7-jfdBMAvXirKZftfUKpkMmw_5mBXzPpR-irhLla_wDtFGaLgmpTljQDSuCl6DKROHQSI5AHAqYwfgfiB84BJITEL54Y0WcR_qKf_QfexpkW3TTfo4C39uzBrbxZHoxOtDFFlNlo0iR93H_wOw0a56YT-jaAQ0WN5GfbU10svY32Qrl5oyRX380fv83fVWYzjFUqf9WcV-OsIV783rY7cb8s-tu-M05mS6lMlw1suy5yp3PWHfiSOZd6VTODZQwAJvpav4YA0Q9wa2QqQGX7x228d5hvR7N232XaZ16upQFfTsycVB1uQJkeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشورِ مردم آباده استان فارس در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/437985" target="_blank">📅 21:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437984">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ستاد جدید دولت اختیار قانونی تصمیم‌گیری دربارۀ اینترنت را دارد؟
🔹
اعلام مصوبۀ «ستاد ویژه ساماندهی فضای مجازی» درباره بازگشت اینترنت بین‌الملل به وضعیت پیش از دی‌ماه، بار دیگر بحث حدود اختیارات نهادهای تصمیم‌گیر در حوزه فضای مجازی را به مرکز توجه آورده است.…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/437984" target="_blank">📅 20:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437977">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pSdDH-mzNeryc8T9PPqjgT6GM5Sqk9oYpZiOLW9HUH3I3699lNsEBgdwhkfJhYZSPGZB5-gtZcaA2nvwo-q4bXQ_htRj8eNfQgz1_jSBowW0SHBe2BTGnjWcZPS5bucnOyOQbxWKNvMBQSpjZM5kCJw1AUwr2fv9o_CmTFiiJAYtAzU39vc7M4TAyeVNG3LD_KhLYGN6u25DU634dlv50ApQuGLEr1Gs7VLi98K827zd71wORRezqUcbhz_9CK1XCR5raqJk3Up5O9TlBDsZFNjosFcOsG6jXhuWbbXo0wt6ZP5M2J-VAdgG84DYoRiWqOaGbx3gxgGcceVn00IL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wB-H9Cg3hCnwpSg9hZissQ6PeZT4GTHOoB1BLLupm0nAHPSwCJYJn1nt2iUC5mtMQYYWx963JIUwhBhZsbnR6xdCGbAV2Bol0zH9iJYWM5_t3yTTDyjM2_LUgJAHcn1Ji9FDize8gb61BIBS6-M7hLPhXUF--4OvIl7HNG5n8ilztd0qAi2feJhBhoUx9XBLvzGxHXd2f9aWJ-O0D8wLR92dD9iHEigbjLNxRW6S6KYkl9LqeYFWzZWVtnSnd1IGWQgp-IKYH7ayH6DfDTX6-1s15Ugl4DKsDZpR_Bbs0r6r6syqAijbrMpkpc9lLNT-6fi6kOWtqcnT_tfjbL0wog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBkMjR1_b7Mu_tbfP-1BpzErHVoYALje0wg2Xj1VqWXXD-UI3VP9guSgtMVtuTUDaUhep1DoD_XIO_wg8Lh3it-A---S4DWnhE59N6LZeUmOLP0c63oc5sT5eSw4QJiVt9ZJM-9ecDIlNgxacERxB7G4sdqy5N9faHmFDLybdn7tHvEEEu3GGWBPhWYf1blNmfxEB6z4xSPLgaZx2c1uJmkP54Pcm2B3VSskXEl2lZ6CMyVo7tTLDe9B3_Y7cF7_ISDPZ1uOTs5qfFdj_6dQp953UGDZQgnimaYc8VOeEy-TOXPdl-Ox1N7G3D9dKdlKKQv8RtjimKSvCNALOw80rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4-5cS19UDoV3072FO6tA0yBbjIt936zxr26h8o8nRurWjI_AWqOVxnkrXNS8Ag0SzzOKfhZfy7U-X5g0q_e1nZR9rkMB7Ww-Fq-O_A5b0TCcT7Q2T_c2Q0PWyTQNJ4rGTCQrggyZVcservcJFiJwN5otEK7bxwrgOPrdffPDgM6zaeEQhf5h7fA7LarK3QMyTmL7M_GqUBsstx_zhQ62z3ElSpvYmHPSlPHLYjCo9WqTRU_YT1ljwMOek3wdYUQ8YwKRxVANLC89yDdEnJlcMc5PcsY4TB4OnvP-8laDKHP_FANOqJ_D1wvBAv_b8b9xbW4BVTo81rdpaWeja3MTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQEYCwZQOJKD6ZxmKPgkf1oONgvAUX6SWEN8AFh2dGtO4dka4-EX6VRJmh2CAO0OfCMYwHyit83u_YH3Y4w_wpIRqHN4NgZnI0DqfQNdHLvLxKShGgM-z8X5DMk-TJ_iiCdzjrPjhhleaaCmcHQiZThQHH82RBzPujPJivr5s1jQ-R42B8gAibTyDZLQcvlpOFjR3_RFKJd7EiyA2X5FE8HCUtnkoaZHd_7snPyP24t1utznnq99HvM5ydrWLAtgm8D6Af6DjnTO3mdhdeFmBVJf2qelPhsFE2h4FbR9OOEmqR7fCy9U6f2BhZETGfoAz8qNGXvaFhq0hHhruQXDSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M7QzKdwxnEHC0oJ-yQ_S41l3S0Hx95ALzJVvsdXGXKlvig3_vzjx_24ZPXVAQkh3s9P-gKzHoqMHCNO9ftc_N8hTAv4owFo3psECtTG6daUFnPAVe1k2zfnPgygtyy2ZE4IG4SndPkRVc-oNh5iBAKaHr1uHdpFqv4RODXevBfmo3c6bM48gn2zHIC-h9DVsxdNtGIShPP7e4Q9KgR7cC1w_HJP_yEtPksmx8b-3O3txDd0zaM-n7xZSOtoiCuGBFkHYNwbU9H2oGZ4FVMFWxWAWDCcfBd_pGRcT8f6po9e5r2DjGht874C_-raE8pOACIOWLCcBL_7F1B34BJq8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZjA-15QjwM3LOe50pEFedDvzjjdyA79Ui05RQP832oKYP6tiCaQi50NiuvyxpQMOoveo5VPGIvRi5p0r9DbCxDoheAtU0UBfjbgEA16g2MFzYcLF_YP4mM3freZGCZuln5wHNcISlK8lELUMVAdZHXfFZ71g2Ia6U0LWTHpBDmwXKuq0et41vvF1vpSu29ARrbTcvSOFZwbBLxejpFW5CLGupTsJpz2NH1o2Z71JeU3Qhbm--duCkYRrpH56HuaVFGmcsnbigwPLH63c-fd6dOXsEf5Blc5cJkcGzZb3ONGz9Jt0A7W0opyDkhzTRolM2HsLGhCbK2FSf215SNMhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم اربعین سرلشکر پاسدار شهید مجید خادمی در شهرک محلاتی
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/437977" target="_blank">📅 20:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437976">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4364a9738.mp4?token=DSAa5I898LYi58hWV7JJCwkGuMpWjCA2hC8_Co6tS__CtgMMzbQNU0vPsQQ7-USH7U1PLcoXUqYITowFpyTlMfEEarJxg1gC3BnDdCWafax6s9vA1ByFJ7A3-FzmmN9fKZGShn98GhOt5da2lX2pLjq1Zj3c5QOJAKk47DtI-4WZXPayIx4n9zNUyUzDmVGBgTrVqz-FOgAeSlTcNNCTspDOYGn-QbGu3024xVHfw45rWFLEX-5It7LqqAjUl1S80puChVJCjbKKRunB84ZlhBQ0ZOlo8qaDN6nhlSvYlgA29EEmsqPsPK7a65Bgw-7t2ZDhjJX-qEpsBkFiYioA1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4364a9738.mp4?token=DSAa5I898LYi58hWV7JJCwkGuMpWjCA2hC8_Co6tS__CtgMMzbQNU0vPsQQ7-USH7U1PLcoXUqYITowFpyTlMfEEarJxg1gC3BnDdCWafax6s9vA1ByFJ7A3-FzmmN9fKZGShn98GhOt5da2lX2pLjq1Zj3c5QOJAKk47DtI-4WZXPayIx4n9zNUyUzDmVGBgTrVqz-FOgAeSlTcNNCTspDOYGn-QbGu3024xVHfw45rWFLEX-5It7LqqAjUl1S80puChVJCjbKKRunB84ZlhBQ0ZOlo8qaDN6nhlSvYlgA29EEmsqPsPK7a65Bgw-7t2ZDhjJX-qEpsBkFiYioA1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش سربازان کوچک ایران در مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/437976" target="_blank">📅 20:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437975">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvH5-sdZKQCbN7OCYSI7lla31XmEPiY8QFhm0qvYXU1LzUejz7JKqlFgicRuNoyO1Lm5pWj_PsL9Nvx_u2sW50p9iUchkJItSLlMfd7jdUl9xxqli7IHjtZlzJNCcVpDJUtPseNerAKgi5FUYJgqHxQi55fX0U1NXMNWlGFMAGh3RMAYlJKZPnz0nZsyMjo_txi5LbZmEL1SDJ-sdIh84pV6Cc9cLB84b7ZWwKLOGmHJ8r2DVfEoYyhq7V23lMdHBqc1Ll20eDBHAMNtKlabwJXA00_QxnO2cq1DHxjlVgi43P3bsd4DPKAYqRBHkcoI6W2h8SCMpzSMHvhzobq28Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: توجه ویژه به خانوادۀ شهدای جنگ باید در اولویت باشد.
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/437975" target="_blank">📅 20:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437974">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">زمان مشخصی برای تشییع پیکر رهبر شهید تعیین نشده
🔹
رئیس شورای هماهنگی تبلیغات اسلامی تهران: هنوز زمان مشخصی برای تشییع سیدالشهدای انقلاب اسلامی تعیین نشده و مردم به شایعات توجه نکنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/437974" target="_blank">📅 20:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437972">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قسمت آخر سریال ۷ میلیارد دلار پول بلوکه شدۀ ایران
🔹
همزمان با اخبار آزادسازی پول‌های بلوکه شده ایران در قطر، بی‌اعتمادی ایران به آمریکا سبب شده تا دوحه مسئولیت تحویل پول را این‌بار خود بر عهده بگیرد.
🔸
ماجرا به سال‌های اجرای برجام باز می‌گردد، زمانی‌که فروش نفت ایران به کره‌جنوبی ادامه داشت اما هم‌زمان با روی کار آمدن ترامپ و خروج یک طرفه آمریکا از برجام، ۷ میلیارد دلار از دارایی ایران در کره‌جنوبی مسدود شد.
🔹
اصل مسئله پرچالش پول‌های بلوکه شده کره‌جنوبی و قطر به ساختاری با نام حساب امانی باز می‌گردد، سازوکاری که دست وزارت خزانه‌داری آمریکا برای تحریم ایران را باز کرده و امکان نقل و انتقال پول بدون اجازه واشنگتن را منتفی می‌کند.
🔹
کارشناس اقتصادی علی زارع معتقد است که ایران باید به عنوان پیش‌شرط نه پول قطر بلکه مبلغ پول‌های بلوکه شده در سایر کشورهای جهان را نیز مطالبه کند؛ اما یک کارشناس اقتصادی دیگر، محمد اصغری می‌گوید آنچه اهمیت بیشتری دارد، سازوکار دسترسی ایران به این پول است، بارها دیده‌ایم که گفته‌اند پول را آزاد کردند اما ایران به پولی نرسیده است.
🔹
کارشناسان می‌گویند، ساخت مصارف دقیق هزینه‌کرد برای پول‌های بلوکه شده و پیگیری کانال‌های مالی امن مسئله اولیه برنامه‌ای است که ایران باید روی میز بگذارد و آزادسازی پول‌های بلوکه شده را مطالبه کند.
🔗
شرح کامل این گزارش را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/437972" target="_blank">📅 20:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437971">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ed3iFlVFen_QHJrPl5gMQxhV2dfXSPN8aTolZowYqXW354J1XW8C76Ejxys4As4ZEIwY-YB-k1kaiZV6HhW6pkLKYHh-c6jMeyqCGVm3SIgLiZyHohi6DWhQ_dOxOkJPBKfsEMxOE1Zc15Srwn4oam4j0B5EqgIqUQrNJd0fl-eBOUvFFY5ukdznOMKyPMFF8Hh-j15UkjWgjDBzQ5zVUsoXJ3aBysfHFeIdDH7Ivpq8FyPLDUYWNxKWLKSLpywT7zarIJEvGuxECDg91gakL2xSdOWCBeR_6mvqcsC64VvXzmF51M4TDwbzUaM5FKZiqL-_EEEd34lOuJO4WABMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورکر: هر توافق ممکن با ایران برای ترامپ تحقیرآمیز است
🔹
رسانه آمریکایی نیویورکر نوشته: هر توافقی که دونالد ترامپ برای پایان جنگ با ایران به دست آورد، به دلیل شرایطی که خودش ایجاد کرده، تحقیرآمیز خواهد بود.
🔹
جنگ ایران یک «شکست استراتژیک» برای آمریکا بوده و حکومت ایران اکنون در موقعیتی قدرتمندتر از قبل قرار دارد.
🔹
ایران در چارچوب توافق پیشنهادی، هم پول نقد دریافت می‌کند و هم از تحریم‌ها معاف خواهد شد.
🔹
به‌نظر می‌رسد جنگی که با هدف سرنگونی حکومت ایران آغاز شد، در عمل به تقویت این حکومت منجر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/437971" target="_blank">📅 20:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437970">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7Xi6Sbsp5n4lmxDwRMgtahSLVgIfgNqt768aRS3xhGesDQd6_NA_bnI-tXj2UumfeIrnmlGZRaK7aouuCv9wPn77f7zTgl87Md79pincgDpYuzhlCR95zioL3ifRrfZ5PTltIlxMOGNH8w-TO4g2my9lLnHumSLinBe-T_G0d7Sv-1lroWVhZjoqNLBA6SQIh-ymCk_X6fQAxy1AEXTCejc_VRtVlWUCpVRFVQcWHYk7z6leBaEyNqkvLcz4p0AIFtCENZLasrweYRWuFNB4-m3mIrqo-_tp-oncDLZoAMUQJooFQ_H_0Vh9e2zqu0BsI-sFtWeSu3AE_lfp5329A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام شبکۀ سرقت سوخت از خط لولۀ اصلی انتقال سوخت در هرمزگان
🔹
رئیس کل دادگستری هرمزگان: ۳ نفر از سارقان فرآورده‌های نفتی را در حین برداشت غیرقانونی سوخت دستگیر شدند؛ در بازرسی محل وقوع جرم، یک لوله متصل به خط اصلی انتقال سوخت کشف و دستور مسدود سازی آن صادر شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/437970" target="_blank">📅 20:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437968">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02341b84fe.mp4?token=QyjOdGpelz0V6SskJ4bWqi-4zSpTBybltWFEc5RUoTQDyURiGseuUkvUxhWtjBIZMRDUHjem6FEt2smnYswHcpPRjV03n1US2Txc47w2qlxT1LFuYdiIVzl1EAlJHBhf_NKP0Vzzo2CkJwIhVKyGdpTrHSOxPyvmiJT4dYunQ0pNxng29kSx4QWODeKQEns4VH1gnTuNbd37d80CYL9VejDF4wmzZjC0dQRWGHmM1dPwl4gBELSK-fd9PMgqYab4UqK3WfnfNEwDmXXQUeJJtYgi9GcemS0EBjdDSzYIDDZr5wMaLADhDYFj9TINJvpII07_GL6ME20vPvj5Av14tmawSe7UBWLJeC_N-T-o-_h3oJEj1eWFGiGbfJg2eut5aqzsPKKDkgB4hKbXD-ZxAPJCHBYmG6PKb_g7IbgznGaleyTklsveLBjiAQ4rEDRKrxDWtFzNCAmhXKpJnBZJc5jo7AJent4AZbgQGaUO0bpHx4uskF0gu-rVF-Hl3GtaX8G5cJ4OZg5VVm291B8d5VcAFFVMhRs27qCbzwIty1OSw1VWpQRC2bQJvgRhGkpyktQgCMxOb8A2Tcu6yDoB2XSk3Jsmw4xzUSOwDNoWHOM2JSH-JENJKUBY_4pP0W13THucVj3Io6sUizYBU8YGdA7j2LKfYyuM-vzy-OIHbX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02341b84fe.mp4?token=QyjOdGpelz0V6SskJ4bWqi-4zSpTBybltWFEc5RUoTQDyURiGseuUkvUxhWtjBIZMRDUHjem6FEt2smnYswHcpPRjV03n1US2Txc47w2qlxT1LFuYdiIVzl1EAlJHBhf_NKP0Vzzo2CkJwIhVKyGdpTrHSOxPyvmiJT4dYunQ0pNxng29kSx4QWODeKQEns4VH1gnTuNbd37d80CYL9VejDF4wmzZjC0dQRWGHmM1dPwl4gBELSK-fd9PMgqYab4UqK3WfnfNEwDmXXQUeJJtYgi9GcemS0EBjdDSzYIDDZr5wMaLADhDYFj9TINJvpII07_GL6ME20vPvj5Av14tmawSe7UBWLJeC_N-T-o-_h3oJEj1eWFGiGbfJg2eut5aqzsPKKDkgB4hKbXD-ZxAPJCHBYmG6PKb_g7IbgznGaleyTklsveLBjiAQ4rEDRKrxDWtFzNCAmhXKpJnBZJc5jo7AJent4AZbgQGaUO0bpHx4uskF0gu-rVF-Hl3GtaX8G5cJ4OZg5VVm291B8d5VcAFFVMhRs27qCbzwIty1OSw1VWpQRC2bQJvgRhGkpyktQgCMxOb8A2Tcu6yDoB2XSk3Jsmw4xzUSOwDNoWHOM2JSH-JENJKUBY_4pP0W13THucVj3Io6sUizYBU8YGdA7j2LKfYyuM-vzy-OIHbX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقیف ۲ همت چوب احتکارشده در مازندران
🔹
سازمان اطلاعات سپاه مازندران: یک محموله بزرگ چوب احتکارشده به ارزش ۲ هزار میلیارد تومان در سوادکوه توقیف شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/437968" target="_blank">📅 19:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437967">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180a3e98bc.mp4?token=EPtlOBFAd4z8qMwKyxgR0tl4LqLYnOpr5mWeoruQWGWIk2kMrqyI2brzCDXJ-_w4fV4kwu0p6M8SXGdFLyXLrNUe0j__kYrjnzUi3ZP6O06PNmXqjx4DkqakXwSmzNldXRsCQtKu9VDPYzx8ONuB-1BuLXIWtk2Ds0qzJV-2AbU-GhcS0KuvSonf3hzaWX7B4JIGQP8VaD7i3Rw3i6EoVnEsuyMGjg5951WpBnl7o1F_G-52_TIGXSJMIAiIAKj5MR2MC1oCaRzFTgfIPPLsbRruTW5QcxmFQq3ISIJ_OJgiQVA6bbS2PUYFUcP0EbXDnBbWffb-H-1iK5MSeKLrzWbFfW_31e4knLt2Xy6yFX0LDBvgTGw0zYotuxtX_rNZGVrxPFze0EZfI8ABKZ5wM2oxsh2ypea7Ol8u3CjWzNvwpqpvhzIH_OLWXoFRqV_WcmHJVgLVPgIu72RG7-T02Ed2OW-xFT3I8wnuI1gMG_gy2YSLB5zS-xJsECMZGLcDg5Li3suPMnvXszSPYCPJfYmMkjmJv1Tc28xyizpfEJcQcI7vXvegSdBRYVcyv8clVaIYe8WESnQ4GGWVEzps6xlQP90BHNg0jUAbZh3sRDcItjtCMVbIynZnTbhEUyEk-iDqkVN8cPTzrx7T_J6iwRrXOBsmL7PbHtzCwGKNfuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180a3e98bc.mp4?token=EPtlOBFAd4z8qMwKyxgR0tl4LqLYnOpr5mWeoruQWGWIk2kMrqyI2brzCDXJ-_w4fV4kwu0p6M8SXGdFLyXLrNUe0j__kYrjnzUi3ZP6O06PNmXqjx4DkqakXwSmzNldXRsCQtKu9VDPYzx8ONuB-1BuLXIWtk2Ds0qzJV-2AbU-GhcS0KuvSonf3hzaWX7B4JIGQP8VaD7i3Rw3i6EoVnEsuyMGjg5951WpBnl7o1F_G-52_TIGXSJMIAiIAKj5MR2MC1oCaRzFTgfIPPLsbRruTW5QcxmFQq3ISIJ_OJgiQVA6bbS2PUYFUcP0EbXDnBbWffb-H-1iK5MSeKLrzWbFfW_31e4knLt2Xy6yFX0LDBvgTGw0zYotuxtX_rNZGVrxPFze0EZfI8ABKZ5wM2oxsh2ypea7Ol8u3CjWzNvwpqpvhzIH_OLWXoFRqV_WcmHJVgLVPgIu72RG7-T02Ed2OW-xFT3I8wnuI1gMG_gy2YSLB5zS-xJsECMZGLcDg5Li3suPMnvXszSPYCPJfYmMkjmJv1Tc28xyizpfEJcQcI7vXvegSdBRYVcyv8clVaIYe8WESnQ4GGWVEzps6xlQP90BHNg0jUAbZh3sRDcItjtCMVbIynZnTbhEUyEk-iDqkVN8cPTzrx7T_J6iwRrXOBsmL7PbHtzCwGKNfuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کدام گروه عراقی در ایام جنگ تحمیلی سوم به مواضع آمریکا حمله کرد؟
@farspolitics
-
link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/437967" target="_blank">📅 19:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437966">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">سه نمایندهٔ ایران در آسیا مشخص شدند
🔹
استقلال، تراکتور و سپاهان ۳ نماینده فوتبال ایران در آسیا خواهند بود. این تصمیم را هیئت‌رئیسه فدراسیون با توجه به جدول کنونی لیگ برتر اتخاذ کرده.
🔹
اگر سپاهان موفق به اخذ مجوز حرفه‌ای نشود در آن‌صورت تیم‌های رتبه‌های بعدی جدول به آسیا معرفی خواهند شد.
@Sportfars</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/437966" target="_blank">📅 19:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437959">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKCYSU5v6O2PGRqkGv3YK3T0NehJEmsoQpwZC8AlxDnUa-5FiUNL99eoqt2Pym94Md1LrwqHnwOUxRw2g9sJVh7rcvQdL-3CVTpadQ_VwSIiS-0vLdNz0y1RWBU3-of_s6Hg7JDXSsiLF-h8ET7Ya-ONnosF60eHy53FtoAMr4Hz3n8aLlHuwf_bCF8xAwy07vSbCCYliO3PV-b8wEXiYsUo_tkF0KXZU1Dy4TIRIOApEToJItpPvJi92-PI6VVOWLnOz-ouwz6Hn4IGTs2EWZdDmpzeiCmmAxJhr2gTv-IwwcmfTf0URdilan8PzWRioYeQ6p60idF9af9gVx0r8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6TEDXNy8Pp07Ax6GKMwm04qsFsTu4HAIfVDtr9jWRaEEb-Tgs95X8p-ub4N9PgzURj23tFKT9wSBHXZauHd0K87x4OSHwgaChWRkuoypsUpTpkmYrWdcv30I580MUpvbVM8UpaExTHy9X_FMnIkaPORyWRDq_olbXYHV6lhHXKPXiiGZGJfy9oqvq_BUXpvGjhjwr0q5hZcHxHnNP8wtQHzgiJMcVKRVymdMC_VzycnOvXt1ayJrSTpbFdO6G_s8k9_rfn-Gwe-JjZR1KvEHKY4zqyWacyFQPGkkj6Hj0ogmzKbzkMPYBhidrQTlS3p4ET4jTXCFwIjenVeTwOPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XlLYq2QHb2P43c4s5OoBQeIwUJOGcla-8HUk4SjYqUja_EBwmcbqP7yu96aAo8BPCoq77iGJdEXfkG3B5iYbg_Ccv3ob75JsDyqxLrJB_ARxwr7hKEI8QcnoVnB6cnTWfevctnP43FrEWFvU4z-Ovg42ZaLyRYjO74XRPcvswQqCDbfG84LolmgkkgWAkp1A1ArbUrgXFmbUlJbhsgnVNxpkI-lOtNhAtkVDLrDfjV3KyMZiMs7fXcse8KV1M8G3H8BIUEaAYHUq-i7EtyCJq5KlflLQM56HD4ze74qlbaGXvgezkGVC0P6CXYVIjzVoJo1F1MSzh7_dVqxvY2mVSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5Z2f7yEwf-QzujWokRZmiTPx7DwhqupVvdBjW93PgWIlYfrKxMb-hTGBhJJXBp-Pc9oM9FMk1j3_SV7xe7WDeIO6AQxdOj1NgED6MSu65L8w3eU94YRaFsJ2vtANZlSxlHebiNSxfymHYqFufHfbROFWLKtOu5grMiHik33zzsIkARfQQMbFEX6AeaTve2LHTfnlyXAM4mbKl7fydliudgn3kKBCKz4Gt8fo-QFG6PVGf1zkcMjnM2qQFBFdqKlaJMCo-yBC-57oO1U6xWpRyq5n1R69rO6bRQtanaEMlM9dY76SREofPp7kW0WY6zghvJASvzw5zmBHQCoaGNTJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q81SB-S-fHz5eyvymg3dIzB_hlBLE-l-Ozb2I9aL1FEZATJAhEI13ZVji1ox0hhvBVhFCkEbWANg-zjhJi7w2BpijyauBi_IfIod7i-AI1btNe6raW7dGoGV8jR9Y38O70-7-BJwbUE7II3qPU5C7qtr1Rq4Jw84P4oUz23jNmKga3v11jAnTsnYEDX941dcQciYVe0lqFsOnX-LVf9zA8kFBQXavXdBQ4Sl8aTumqiJ8dn38L6U-a2SRywRZFjmjazPuL-XBChfYj3R_h8eVQjAUYGeIOnFvtmQS3RYaMXJj_ZNf7wvAM8oUCwxg-8L3jI5_Zz6VgFvK4jB1SwTBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c1IihmZFF4xczvSK5FJQL0bwwAMr98qsrelgDXmZrl3w09IscCK0J_PjnTb325WvJxn21o3lemedFT8LogkoRuqlDLTfytMJykYukWEqz0QjuMXemejNXal5Fpgz7WKagx3-d6mpZxTfrAFlPjNScP2qNGYgHxHbohUFBsDpnG2Au42RFJzJDZ3JALjmGc-BfWpPb7q9oI_OlUp9GgUBDYVBxrPHCEs2o5Kf_75EjYLvSgvBg_JA-Cetp1dR0mTA_SLPOfU0IR1hrD3yc5cGTxvAx0BsMTWbzKJcYly1xuHk_ioRFCbh8I9LY8cgvbxfU0Nt1iJffFERR1CTXVXl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvkF2IpPa5XNmpdKPQUAgMYfyuztgSIsQdbFBuo2RWfz3VVJc7YUzdzMjagjKacXuqHOjkMTRPzT-vfKsdwqirS8TD4CcdeY4IWNf5g7n140eBPn1CpKhi9BnR7ao-vJwQFQhvxOnkq9DzsUD1Am_9li7gn4nuse-mWHq1Cusfn-q4qg8Ral4eUOZTh0lJKQVAig9Sqxlm-mHckuW_kdDu7ilRzzxp-5Q4JuK5XLY3PinEJ11QZRb1-s7WgHzplYnlKPUDfITaOowUGb0kSzLu_LxQO3wJa9X60D7rae0rzIIxW2dO3loeqlYSZRyaMw2VqJuz47Ayt9DS5S1U4c_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گذر زائران عرفه از مرزشلمچه
عکس:
فریدحمودی
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/437959" target="_blank">📅 19:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437958">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWOkkEdvK8ALXcfflKaXHJ6dxLXc5gacZCtIYeuNVSJrU55KQHTJj3ZdGaTDv6xhEAERHBkdyRlUJM6UiT3054bGAPDYBQ2rT8-SNW0xEuCVVQ62W2U4WfY2oNpUYrspyI4ek_A1a84ezHj4HGQerag7zyt0OF3KSpYDjwYWPYsXORCfrQokvTJzSR-cB5FRZtRImgbdCWgaCPKofV_6-BQcOotNHkjDwhPcR5VSg2eVHaRVoVlv8LHpVdPrr5cHyAYs9SHMyMFuA22ezZQLS38jW4VWHm11VRM9XDQn_k3qGYRXvj52TINd5UEC4fvpIcpYwCXJiga7gu53XVFHoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: عقب‌نشینی در‌ کار نخواهد بود
🔹
این را میدان نظامی، میدان دیپلماسی و مردم مبعوث شده حاضر در خیابان با مقاومت جانانه خود نشان دادند و دشمن را زمین گیر کردند.
🔹
حالا بیش از هر زمان دیگر کشور نیاز به وحدت و انسجام دارد تا آمریکایی‌ها و صهیونیست‌ها در این زمینه هم مأیوس شوند.
🔹
میدان وحدت و انسجام هم یک میدان دیگر در مبارزه است. تلاش همگانی برای جلوگیری از هر سخن و اقدام وحدت‌شکن، ایرانِ عزیز را به پیروزی نهایی خواهد رساند؛ ان‌شاءالله.
@Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/437958" target="_blank">📅 19:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437957">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccnCwxetMJ-3-pvvmQnu94hQjfvZWh2EVkIXpirmlInnDxKW_y0wIuqFabMni0eY1xyqzgnwxPP5jm0JE7TqoWD-GNJIpGEIBx6Awdz9i4MqEAQ-1PnaeumrPD2tkjClbLVZ4BzolxFLPyRUldtGzztfaykgEPnhGfK0Eyu1DmzZuCPTXiyXU0eaiEUs5Cy-wsGdrFm2RcIwNQbXTQdQdWQXFR8Nl-uA7hVDYhltXju5Gt90_iCf_jGpHSZcWg0278IXLMPVd5Oru0fkEq25f8BNdGr45al0UqeEuqFJeGQlSQvXA3-fQtLtSfPPKhxDlCPWT3X4qIEVwaXLR_9R5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ۶ کشور باید به پیمان ابراهیم بپیوندند
🔹
در رایزنی با رهبران عربستان، امارات، قطر، پاکستان، ترکیه، مصر، اردن و بحرین، صراحتاً تأکید کردم که همزمان با توافق ایران، الحاق تمام این ۸ کشور به «پیمان ابراهیم» باید الزامی شود. البته امارات و بحرین از قبل در…</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/437957" target="_blank">📅 18:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437956">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c1487f04.mp4?token=K7GMxDS_jtdo6JlYFLtNndeYy0CyTG3eiNpEPno0nwTyZco4gHtMt0Rkp9xYzMI7Bo4_vkOkNiNRuKu-O4CMknd4rF0qCO9Gz6VqSh6oKVp3gwwULikiEKkm6aQbG_7DsJv0afhqeB7uiRM7t2-QFdG5-Xe6aoueSF86ISIDSnRZVF4RtL1M_cp_N54PYb_EXoJbX7J556_xJNSprv3J0yDQBnMkwVcGCKF6dydFipdgp0CJXezsRB0bLqnsHBJiqUoQJpYc0PHt7R7IRPu4JIRI6ODyGGOZzJAgpo51xfHexCNWT9df8IB-XbRKdPmxeq357Ewr_0cwTFVKdcasPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c1487f04.mp4?token=K7GMxDS_jtdo6JlYFLtNndeYy0CyTG3eiNpEPno0nwTyZco4gHtMt0Rkp9xYzMI7Bo4_vkOkNiNRuKu-O4CMknd4rF0qCO9Gz6VqSh6oKVp3gwwULikiEKkm6aQbG_7DsJv0afhqeB7uiRM7t2-QFdG5-Xe6aoueSF86ISIDSnRZVF4RtL1M_cp_N54PYb_EXoJbX7J556_xJNSprv3J0yDQBnMkwVcGCKF6dydFipdgp0CJXezsRB0bLqnsHBJiqUoQJpYc0PHt7R7IRPu4JIRI6ODyGGOZzJAgpo51xfHexCNWT9df8IB-XbRKdPmxeq357Ewr_0cwTFVKdcasPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار نظامی صهیونیست توسط پهپاد حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/437956" target="_blank">📅 18:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437955">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1200615a.mp4?token=rgF0i_Q0oNGunpS616iDbUR0o91R8j1aVw0x9J7dFS2Fgs7IRnYSne8ZD-3LwiZ3UN_Wu_LKE6nqBMNJq5Ib1FOVwRCNShJnrcr-vC4UFDiE89hZPzKz4D025lIl11PLiKPpvmH7hR6Db7XfRsWL7pSZcymfYBy2XA2MOYZk1GP6rytk8mGBneJosfr7DfspleidcFLQ0Op3dcmL7gCCywfu0sTUSlSBdSPSirhocS80o6M5LkFV-oBTtkXUb7Wm52B1MIUxqc16V4eusD9ShWDzmlSJBygSd0Xz7Y-gueqMVswMhLCAAXlm4ERMWxMQPaTioy20TgUnNuzbqX29Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1200615a.mp4?token=rgF0i_Q0oNGunpS616iDbUR0o91R8j1aVw0x9J7dFS2Fgs7IRnYSne8ZD-3LwiZ3UN_Wu_LKE6nqBMNJq5Ib1FOVwRCNShJnrcr-vC4UFDiE89hZPzKz4D025lIl11PLiKPpvmH7hR6Db7XfRsWL7pSZcymfYBy2XA2MOYZk1GP6rytk8mGBneJosfr7DfspleidcFLQ0Op3dcmL7gCCywfu0sTUSlSBdSPSirhocS80o6M5LkFV-oBTtkXUb7Wm52B1MIUxqc16V4eusD9ShWDzmlSJBygSd0Xz7Y-gueqMVswMhLCAAXlm4ERMWxMQPaTioy20TgUnNuzbqX29Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودزنی به سبک منوتو
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/437955" target="_blank">📅 18:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437953">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKdtW2fyEoZBiCLoA5mrVFJu-jw3kSJhBhmDHNquXXAKQ_ctU24Eq5dktX5Ezh5YWuiJpmVjPOWMjFjW-xBq8SrGamNj5iLvGcg0adzrC96o-bczZEgei-em7HIw5VEpwl0Ti2YBTcKY0kFEEzsiTc9fGsaAmd1t3c7DL9oVs1ITs7-YnN5HjppYkKUIOiIC8wUnfRgsSwzyYX_Bp6ze9TrzAjEiPSEccHjz9CAtTC3Nvy-znZZ9o29H3OFGoAFWzrc2BfxtLN4cGvbwRHVsRqQGeZA9VIwCQRmVBYi9Rn8Td9JmHq54nuFDWpjIyLppgDJ8ABwwwZQLFkTHDQrsAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تبریک اژه‌ای بابت انتخاب مجدد قالیباف به ریاست مجلس: دکتر قالیباف حقاً و انصافاً در جنگ‌های ۱۲ روزه و رمضان در عرصه‌های میدان و دیپلماسی جهاد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/437953" target="_blank">📅 18:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437946">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIA1RQA45q8NOj8xVQp0O47kuF5VkBIAqqLxs4WPTYwxJZcXXYFMijQ0Ye2bz54mo_Nx7XGH0E7FgaRTt-UCWTCDmvz-GvTVcfbh87iTMX3_zLADJZuVln9Z3fXbAjPHlh52R0c9U49L_c36AnLljy1FXUo4h4-ioLIUu4WxzK-grmuK6dv7zNgqYgSMN-cpsFP_xuv85xCm_O5ABj9q4GQir5fIqacb6yal9-Roc-elR0G2vsnVEiwBrsK9heojXbjQxQBqlXk-6nwC7UA38_RzfxXsvAOiRqnGedNERv5kkZ2QajFn1kr6QTGnXKHmhXssj-k1jYtklqV-mMIcJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kVDahFNvlwHLrugV399RVUWWDYrEsty82BkTA71Ev9clzfnYVFSRPtDvQN_GjOOnC4RkRv1pwDd2thmVfHks7DI0RHsqyE6uRJyTmxUjvWbfEWNDGqyng1n2v3suIDJN62sDOF5JdLsgmiJJSNXEKPP8ULCpMtxtOkEJlQug0dSwG2EM8Vf-45CeYaCD2SDrK3Ky9CTSuxJ44ELz0_djyy08qKa8K95GvZ7P8yv1Vmy1_xk7cZtOWi8jXXQqdcm_7YYQ3O36j5xMXX3drVN1WcevWCcNvLqwkYVrgVGvnFETW7D7fYziBODSA4ylztTVoGXd3aRnHaLvwp_UOfO10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7GHsLaOZHSI59C1uXcj2in2AcKJPgUhfUSs9Ntdc8v8__5DQdc5a2iIGZ72fNaW2pB2wyJGx5pcBlV0EEybijr0Mgaah__o8h8qW43ydzy6HlbKwX79O4IBSq_-4hoULoV3T2J-_29Z1sB3FTlEQTXbp40Qwe48Hw19COSg2RkzeqaLXowh7S5NK4rbFd3FAsVVeSNuDMG3pd71vwsriuR6XKknvG1eMEP-5PY2YLRFufFpc_AQWCxJ6udvjhv0Qt57oILp5BAoPuFMV2Z4fhUIxi-tVyhLtEnOqBVewTMLXOqJjPV5NCjve6y05IDKNO6y1LMcZp0uT5qU-Kz6IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A7cABHRpABuLAgJzwJI_QyqWe-YnBTdw_hVmntegLw-ouZ8AjM7mRcKjVvR-cbBqmW0kLmMFWBGPKZCmjjL3jKGfvTfXAOBZXWkCnR0IVMdUquGCmg_vvWB5YPTD9pic18htfMIKBoCg-BtnpzXQVVW59dOnrptVd6z0Fz2JRMme46HKZfvbEZAwFFzkn8qH4EWlULcZYhBK7SQ5vJdulGm1wl3VMKuQrWLw-bHfHA47iQpWux1XnX3FbI3mYdxNNPSGe7_-UmfiYWi5W-ieyCYFGJ4FGm3f5vB45j63hVTCIzkVTkk6JeQdouzl61lIyOg2o9VvPQ0T6pFlOeoWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ez_OzutT6TGe6fX-7lj6v2sFCzBmhG_o9g2qaDCLOrPe0EG6XIi2Z9vO6ox4FQXFO-FZV2YX2DiZspMoStOP_NumGgKcYytEylO6NHcpcYCP_zWO3468ZqoQK0YoP2y9yXMUegEUeUPWlK1mtPwDoLtIvh9hwVUsdpxlBX9rmJS-AxmEC6m0JgME0Wi7Dpk4KC6PyJWCe2PMJrVmAX0ftcc_5YpZsIiS-c-AOkoCDnl8FXRSNCSIqk0pJT3fcMzuJ8X-NVRdkjctCpbjE2LFjXAPa7qMPBR5Nup9wQ0VDOtyyXAteUeRF_K84GRkawsn1dS49qyPVlOCJ7QFfsiQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FK1jAXZrIYPvCdXmc0jN4btMT0JGc8OLNMpwzQXob-4i0odMYqSpEJuRNtQE35Us_3CzPHWodxMGar-PRdHO7zN_BTbE6ebR45VT8Zw2KvctqmDDdJPWTvy873eoJHz-om-zfLLGHO-QfPU3rENA2P7RuUtH6i-vudL76MDzoAJjQCNLAzsZenCPPVUDt3pxI4xrZ8oAV_BGMKhFk2_9unDAVV2I-P00FLR0Abq14Xy6DlLLsmbAPHTM2L1s-rKRVKelBn2ZTz2sZougHg8b6xeOYZ__Q7EkaXPnUioRHSv9cF6YO7W6gCpoga4Jr1cyXHLZnlFJ2twWLMTBfABOYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBVPWJ3XWvBeqCME3X2PNGy3tZwFFG_bNI74ETZ9s1vaT_2D3jkOD9U7P5ymWWSByVanXEi7O7ejcydFa59p7frTCDKrSvSDD3Dmo8N2EIZoPRiXK4GFVAtreBXwAthWfL_Ns4GnfKkFbavAeTifXJwv_Cg-X0YnNWnkQFLF2xbkD7p6egflXWLh0x5sWWvMimrkz99OfIWe595XW4xabLjWSUs-3a90_29WeAyBBCaEgtiGpa-HPNNdyBjWKsyKEquNsbdh-hTd7xBDPRLtrqK-TI5SmkmOfL-n13L_ZD9vxfOZxwqlPcxlnIjvmdyCc56eitJKMSog786fuWrAQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آموزش سلاح در میدان انقلاب زنجان
عکس:
عرفان تقی‌بیگ‌لو
@Farsna</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/437946" target="_blank">📅 18:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437945">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyrAIYI_mW_5Gm9_rgllb-uzwVkobm1WOv8DK4jKDhVXHOzwu9KOf_KMKOJyWgD94Jew3tOmjsSdVgOuw-o7VloDuqyU0fH_etEnfX_WFVPHVcCI9bfcrZnJlV2MT94EK2St5PxTwxdfsTRfUL2_fkK9xbBmManTwj9uqMBiOX79JoeZr0VXo8v7BXFgP2HkKevR56z4Pfoo2JfUqTiLuLyJEeNVPQcT9tZ80maJ6GwtaQGHYtTYPRh33WK-gFirw2CcZkGB02pr7yqejvbEjOkhQHICiaDiP8lJhaulu420Q3nC8PnnVRg-vj2cWBBuUVstLJR0ZgIVfCPcyrMVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل: اختلاف نتانیاهو با ترامپ عملیات فریب است
🔹
طبق گفته یک تحلیلگر ارشد امنیتی اسرائیل، گزارش‌های درز کرده درباره تماس‌های تلفنی پرتنش میان ترامپ و نتانیاهو بر سر ایران واقعی نبودند، بلکه بخشی از یک راهبرد حساب‌شده برای گمراه‌کردن تهران بودند.
🔹
بر اساس گزارش کانال ۱۴ اسرائیل، این جنجال با گزارشی از پایگاه خبری آکسیوس آغاز شد که مدعی بود یک تماس تلفنی به‌ ویژه دشوار میان ترامپ و نتانیاهو درباره یک پیشنهاد جدید آمریکایی که از طریق پاکستان برای ایران ارسال شده، صورت گرفته است.
🔹
کوبی مایکل، پژوهشگر ارشد در مؤسسه مطالعات امنیت داخلی (INSS) و مؤسسه میسگاو، توضیح می‌دهد که این یک فریب تاکتیکی درخشان بوده است: «نه رئیس‌جمهور ترامپ و نه نخست‌وزیر نتانیاهو هیچ علاقه‌ای به یک بحران واقعی ندارند. با درز داستان درباره یک بحران جدی ادعایی میان آن‌ها، ایرانی‌ها ممکن است از زمان‌بندی حمله نظامی بعدی کاملاً غافلگیر شوند.»
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/437945" target="_blank">📅 18:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437936">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gloRDUOILAehJkrrIna39LbfXikViK72AGlvaT49rbsXkFh02v7u5HXtu0W72Z-0oEhJkgAGF9BynTP1nWY-IKJi6xPe50QitAUl-SeBiCbCy0RMSbbed9XQXh1b8R--JxVCWnqNAHNc9g9uxIkmQR6A36PYL6QX7p2bYdTXVejUBeqKG7H_Fj16vd9C3o2y8aGf2zlxPcTD7krCqW-J8GZ8V4zPilUawUBVAOtEG3W_ALuMcKRQf2OXKkUCHwA51mUfIwmPNHZnDS21cAEg65NzpIkkrObO44LvGFrY-AJKeFfSowREmvFP3JA4J1Lm1HCQlC1bc-DX653hKttZog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جلسهٔ ستاد ویژهٔ ساماندهی فضای مجازی به ریاست معاون اول رئیس‌جمهور، موضوعات مهمی در خصوص برقراری اینترنت بین‌الملل مصوب شد که پس از تایید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات ابلاغ می‌شود
🔸
یک منبع به خبرنگاه سیاسی فارس گفت: در این جلسه برقراری…</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/437936" target="_blank">📅 18:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437935">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sumhSwu5JZlIIHZiFDQvAFm8ZaYDHVI6LuH2f1ih529Sstvn2gq3Mzz1JLzR1LBb6_yXDLfDWFcyDzFeuZj-ry6a3KVTgW39mzI00swQkDatB9zbT-BCIXbLSQuUZuTLmogSjaXnR26a0NwqyErjR6jLPxtozXK9b_zu4UuHhGTpn0XeP26stFCgEnz9KG4befKvxzDiMF4TujsXHI4UG0b460IiB2xpX6E5_24ynOlPjl43ZjJpgyaaGi8bHHbZ31B2f1EYNDx71xyTBXaTgc47En3-n0rmLyFwXdLkhG9MUWfc-kB6_aSmGdoDUu2jBCyc54viyW_DE5l7u8KT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت‌های جدید لبنیات اعلام شد
دبیر انجمن صنایع لبنی از افزایش قیمت ۴ قلم پرمصرف لبنی خبر داد:
🔸
شیر نایلونی: ۸۴ هزار تومان
🔸
شیر بطری: ۹۸ هزار تومان
🔸
پنیر یواف ۴۰۰ گرمی: ۲۰۳ هزار تومان
🔸
ماست دبه‌ای ۲ کیلویی: ۲۲۸ هزار و ۷۰۰ تومان
🔹
هفتهٔ گذشته نیز قیمت شیر خام با افزایش ۲۹ درصدی به کیلویی ۶۰.۵۰۰ تومان رسید.
🔹
گفته‌شده انجمن صنایع لبنی و سازمان حمایت برای افزایش قیمت‌ها به‌صورت لفظی توافق کرده‌اند و هنوز ابلاغ رسمی صورت نگرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/437935" target="_blank">📅 18:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437934">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-46.pdf</div>
  <div class="tg-doc-extra">2.7 MB</div>
</div>
<a href="https://t.me/farsna/437934" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔸
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/437934" target="_blank">📅 18:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437933">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سردار حسن‌زاده: امروز از روز نخست جنگ قدرتمندتریم
🔹
فرماندهٔ سپاه محمد رسول‌الله(ص) تهران بزرگ:  هرچه دشمنان جمهوری اسلامی، به‌ویژه آمریکا، شکست بیشتری متحمل می‌شوند، هیاهو و فضاسازی رسانه‌ای آن‌ها نیز بیشتر می‌شود.
🔹
خصلت استکبار این است که هر زمان در میدان دچار شکست می‌شود، با اظهارات گزاف و جنگ روانی تلاش می‌کند واقعیت‌ها را وارونه جلوه دهد.
🔹
خود آمریکایی‌ها نیز به‌خوبی می‌دانند که ایران امروز از روز نخست جنگ قدرتمندتر است و اگر بر مسیر تهدید و فشار اصرار کنند، بار دیگر طعم شکست و ضربات سنگین، مهلک و پشیمان‌کننده را خواهند چشید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/437933" target="_blank">📅 17:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437932">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3fd2d26d4.mp4?token=TiFD4he56eL2CwqUHDyTatvTUnEk9kX1efXdv1-ngKbTbCK20CchUApxmvK8YFG_JbQVnyOCtccvgmTQ1pzbpZq-9CaaFSJOt-9D05sJip2i64J6r8F9wf64eaxxfPAUiQgmHR-Z8t0pjwaLeGicZHycfNneSq1nmFIUZ9H_B2rIX5M7oUEBimH7Y55CCwoOnaxkumR7fLLowftQnhLhKDE2Da5D8F9hY3GmW_kL2viq6zco9MF8gOz_KXAw71kDWSGrQqUVpY7b8mjbEoq27fz9_0epFdARp3sF58MR-VJhK7_JqXxhLipcFUjPApwTV0K7Z0F92_NXj-KMjKTGgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3fd2d26d4.mp4?token=TiFD4he56eL2CwqUHDyTatvTUnEk9kX1efXdv1-ngKbTbCK20CchUApxmvK8YFG_JbQVnyOCtccvgmTQ1pzbpZq-9CaaFSJOt-9D05sJip2i64J6r8F9wf64eaxxfPAUiQgmHR-Z8t0pjwaLeGicZHycfNneSq1nmFIUZ9H_B2rIX5M7oUEBimH7Y55CCwoOnaxkumR7fLLowftQnhLhKDE2Da5D8F9hY3GmW_kL2viq6zco9MF8gOz_KXAw71kDWSGrQqUVpY7b8mjbEoq27fz9_0epFdARp3sF58MR-VJhK7_JqXxhLipcFUjPApwTV0K7Z0F92_NXj-KMjKTGgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«مسلمیه» چگونه دروازۀ ورود به عزای سیدالشهدا شد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/437932" target="_blank">📅 17:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437925">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oo2YlML50Q5ukUtczjrREvqBJV9-klyOGUXu9NUOyVT5-MuKiseyhRBjKyQbizNknbK7w9wCiHCY_W3mbAr_ZQitfiYK4MPpQnXiQlWfI26OJ_PzMvV2yUcQr9jl2rbar_G_0rAZZOAKav4jbI29-47JHTBxrlRCgvPGR5fN-FVr5xvS9trHLmjHJLmRpNEFpKslLJTmWITZgZe3WayyMkWy-UdberK6IQ3prhgRzAkYjyfS14Drogk-nfX9nWlQdYITMLsnAFBvskTUntUjetZFW0mDp7W7FkFz7MvqP4jkyK04AyixFRd3N8gG54N_K_tYD8dLGJkeUrIKa6-kIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHxjUxNj_OMy6QBLjsOirtiyDrb_9EDA8PS4m_WqN8Jove6gAAA8T11hKAN2Qw_BQF8hfTLopRB1I1ZQcMHB-2pYXzCQ7qkK651J11dCoE_gT_qZsCLZ5n9vsUU4IduowKo8Ga2k7FBUzfIf8bNZvHCaO41vxxpFdNmg1_LYaybx22IM-ZywZhOOwsCrdFOMQTR5yFt8tqkLMEm5YOvwbV7uBtREzhyoKdVnAc845OTHXBx6BMYCpGM6SEnRwQq9a9UiGWNOTCn7Tz4x8NsJV3x_5UsP0V_snL_REAvtomnRzXdtZVU1zW3qtLo65Vg-0_uWKw_TH7wHAu76pG4Daw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehdOsc1zy7Obkt4b8OsSBpsYV9wpuqvx9FRT9eEAIGjShy0xt2Du7Hes9LLS2VUVzgRiAGHpevuQh6V9hU7tAiOe0gYnV5Isg3Q4yalDf_E6lVm0vvQDvJ8g87DWg9sHw3yQopJ8mGxZpzYhWiMbTPgUkGn2Blhja8PGBnz-qayFHvlJGPfCaIs1KLtEHu29yTWZ1OouZCFAY-v1qQtpOvGagxknK2Gif8EtWduCRYRP32iu91oumgZTfQrWQJN0X3iRXW3zILw011w5riuXoYYYnRaB2CUweVFb9RZZDau_VQeg0IQBE78ZYpnkI4U-K7dqkAOJup6BU1bh3ogq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oryAGoI51iLbbZWC-8kjnn0vXgBDZ7MtDvgfLViMZuqejtjtZFDER9njQEV-GIrP4TFNOAPSjaj8oKRliQZmgtF6v_GoKb6Ts6TohYWnx_piwurEHiEANvRMYXmaDFqacZaNetdXaD_L1yVitwdrMqQYgKkKQNAMlJFH45NyDST-OPNnw0DfEz-gfbieySckFWxz3Di6rJKR0ywAtqt-hjm6Si5OnStSFSmN4kEi6Mcta7gkPfwmmmGONDeDsugSgUvSG0Mu4vufhPbsqz7BPcRVYhQcTNKUqogjDABpxNjCCCZLeanTHsPDVvYVBBAkIoVrOGIWE-4CXRhzdUCq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vg9UIn_drPuobpW4PjynWDXVG78_I1digJ4k8WsyHaz7gzUtxV1VBIDU_spH9uCeHqfw4NBhz6ns6Diz7yisNEgzue6SPi4U0aOI-GQXkhYsBVtwTafRyDbVWofM8xvBOKIt42I_L1p2eRfqFyVVbNEKVLP0Dp9FalEaJV_15XRCHk2YVbVwC_VNL1mVi2fElo2eavcklx5FNWc_1none20XsuIFTGx0mVNizVeWRlwbmeRaXy9lT1hOAGQfFshaIbkgcLoywPb8tCU7D1bMAkHYd73V8h86-H79O_3fnEm8zhCVUSutXo3_xWwz4g-K9PGAngXsLk-ifb9NA3je7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aG-ZzH2tX29Q-lEbSs9OJJqd1V5a4JB0forH76fdDblK3z2PzSV5uhWRztURjb3LTuReGEi868P05N9sm8jPcyJh-4cQPQxe0zhhF7mRRu8ooEd4JKK9HDfmFuP8cIHKZFGrf1cHQfMNrlqnnGEwiGPPzIS4EJ8HF_3ydK2O6W-tPR_J8y-nYbPzeJWfzGEEgg2yaDsNRSqkGflLkupd1NUuEBDilW7RFxjLJC4W9qsX5B0FtmqAg744MLlI_KeDodftKJmmhZ2AWbg3HuuyFutT3mBW4qNlnFIci0yLvZZ6pPCkGr-s3bSDDbnuYvS959TQb3yOXBcgiYiVv-EzHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TrMiIqyWnq7FIt9BYrkXtVd4TKvZkfWb7vNQH1--uGsPKtBEOCplBgRrCpFZ2_W9ycZq0u4OOkaW59OZuvIIV-GqOhgjs41ICDhGj3D_yc0NkpQSNWk_IWoyuAai3euaycpIRD35W4086PDmeU80EV-fOOrqs9Npgfw75tZa77C-6QBkhiDMbR0Qe15vwqhQou2O7-LwMKp8yo6i9edyMWHUHfZDq1pEfFTdtR0dqm4Korirx0E1CPp8d0Q9OOYsT9BDx3cvHhONNhGbn_s7OHWbFU-vZn5pSwFF4VkO6Z9SXedMEOe1l9-Ji4zaFoy8tg-W0k-HyRWaQSqGQV5Q9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دریاچۀ شورابیل، قلب تپندۀ اردبیل
عکاس:
حسین حسین‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/437925" target="_blank">📅 17:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437924">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تجمعات و تانک‌های رژیم صهیونی هدف حملات حزب‌الله شد
🔹
حزب‌الله: یک توپخانه و تجمع نظامیان صهیونیست در شهر العدیسه و ۲ تانک مرکاوا در شهر دبل را هدف قرار دادیم.
🔹
همچنین تجمعی از خودروها و سربازان ارتش دشمن اسرائیلی در شهر القوزح با حملهٔ موشکی هدف قرار گرفته شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/437924" target="_blank">📅 17:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437923">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22b517759.mp4?token=Mw0ksSCqvrHCw5WdRuD-sTvAu8suPyXLrhPDTq24Hl4ipw_X4F606vmgzKoOWxpHAhw4k0vwsfVqK328C-rIZI1hsnIceJm0qWeQdDNzP9n8rEATRQPxzA3yr_rwBR8pa9nw5RR-i4CXXc3tY2bqseEDCjMIZWpHmZbNjgkJOZGF6gg7x50KXAGmO9JoD0F2HdaibtZySlN03yS2N4joEZCNWjkaW866Xzhvv7ge4QAW3x7QIaDykW_2_MLM3IVliibxr77eaDkLfI370AsD_Y2Rqkqtt8ptvn99MB2usxfLWwqcl6cgGIDVlPyMDsvcrvRapHRBv9w8mcYx66S7MJHL2vIdDC3Av7Khky2E3qZfJVP5LRWaTkb0RH_BpqZDsR2-cq4W5-uLMXZQgRxZcX5JS1Nps8a3EXyi7qc8aNAhBJZLHwo88Ts65DPuC_9R01PBcXxQRkFqio-dutVVRNZ92da1dAeByT-_LQRSn64_mad-cYA-LbH6D6JdrMme69mvhe77nxVA1xB_MqQr8EKPOPJeVhXb0ooLdrnuxPdaL-Y7GfrxbUZ_gX94JFOLla9-aaHc8np46LjCGTu4v1puQrBlPItss1VQ1UBrABEEpdNF12uAJqGHMzST9BP8qc1pIypGaKC0KeOD89kfMybx0rChyyD5eg9Dz_p_80g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22b517759.mp4?token=Mw0ksSCqvrHCw5WdRuD-sTvAu8suPyXLrhPDTq24Hl4ipw_X4F606vmgzKoOWxpHAhw4k0vwsfVqK328C-rIZI1hsnIceJm0qWeQdDNzP9n8rEATRQPxzA3yr_rwBR8pa9nw5RR-i4CXXc3tY2bqseEDCjMIZWpHmZbNjgkJOZGF6gg7x50KXAGmO9JoD0F2HdaibtZySlN03yS2N4joEZCNWjkaW866Xzhvv7ge4QAW3x7QIaDykW_2_MLM3IVliibxr77eaDkLfI370AsD_Y2Rqkqtt8ptvn99MB2usxfLWwqcl6cgGIDVlPyMDsvcrvRapHRBv9w8mcYx66S7MJHL2vIdDC3Av7Khky2E3qZfJVP5LRWaTkb0RH_BpqZDsR2-cq4W5-uLMXZQgRxZcX5JS1Nps8a3EXyi7qc8aNAhBJZLHwo88Ts65DPuC_9R01PBcXxQRkFqio-dutVVRNZ92da1dAeByT-_LQRSn64_mad-cYA-LbH6D6JdrMme69mvhe77nxVA1xB_MqQr8EKPOPJeVhXb0ooLdrnuxPdaL-Y7GfrxbUZ_gX94JFOLla9-aaHc8np46LjCGTu4v1puQrBlPItss1VQ1UBrABEEpdNF12uAJqGHMzST9BP8qc1pIypGaKC0KeOD89kfMybx0rChyyD5eg9Dz_p_80g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرهٔ علیرضا پناهیان از هدیه‌ای که باعث ناراحتی رهبر شهید شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/437923" target="_blank">📅 17:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437922">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrqHSj3uNSvGljCMouKjIT9Mx7LSa_RM8JHV7760gx4QequWZzwsUyZ_iAUULibo61WmN4v6bKn7qKH5zRwCPkYn0hxkSHdI8KDA7cxCGl1VCzT_54F2fbdcmnrOEEAI7iW2R_rzeL3pEF91_HktybUICBg1A4A7yLGju8WwWDOikrny3jepTZlM4GU61LS2sTOBQFSLgu1xlH-_VJE47lVyKS6P30YVWD9LTrpTORvnCyx9FbW_xgu8lNaKehmovM0_W0MflOOc2SMa7Rm0yU8TU2X7iKLu77nCZnYxQv0GX_ycywMOH3zSwaQfyIVBh_Zq2KHh469TnGvmBe7-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
قیمت مرغ درحال کاهش است
🔹
براساس گزارش میدانی خبرنگار فارس، امروز قیمت مرغ در مناطق مختلف تهران از کیلویی ۳۹۰ هزار تا ۴۴۰ هزار تومان فروخته می‌شود.
🔹
پیش از این، قیمت مرغ در بازار به دلیل کاهش جوجه ریزی به ۴۸۰ هزار تومان رسیده بود.
🔹
یک مرغ‌فروش منطقهٔ بریانک تهران به خبرنگار فارس گفت: قیمت‌ها در چند روز گذشته هر روز حدود ۱۰ هزار تومان پایین آمده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/437922" target="_blank">📅 17:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437921">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAS2syj_Pz_dSkGcvu8TNp6HJmsJLB1irgC_OniCOGbVWndDvnU-N1bdtPmsGHnKCQqO3Z73cG-l2_STfbpI73A1mpwC3VWUeIkU0Xmn9hJEn6aiasmqV5_hz5aWHMIyQvo5DbfgQXbGyMQh6bJLq4-e3lB41KwTLUIkKLkWQdSJ0ZTqtlHKorP0WmPsZnY0k6AVefYwhsKeVgrwJMTBGTYbhhkKd1-BdOHPW8FoBKJnkO0BmqgmjOeSDMpB_aEjFHnVN1jThKnjQWWsE0nLQp1USlg_zbA7xTTakWyEKrXfbH2TMQJOUdao613E0pRQtsCKBkKmylIAnRlMiGcHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: یا با ایران یک توافق عالی می‌کنیم یا توافق نمی‌کنیم
🔹
من به همهٔ احمق‌هایی که هنوز چیزی دربارهٔ توافق بالقوه‌ام با ایران نمی‌دانند و از آن انتقاد می‌کنند، می‌خندم.
🔹
این توافق دقیقاً نقطهٔ مقابل توافق فاجعه‌بار برجام است که توسط دولت شکست‌خوردهٔ اوباما…</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/437921" target="_blank">📅 16:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437914">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nR6YIYWSpCt9b4gVMX5SEZr4TUOoNV3_f4feJprWWDfiAv775kUgXg-fh4SPx1epn2N-0QeIu6L2Qr3wYmT1NjldP8172V5DoICAbX_lZKdI-NEpBdmynHqUI5mqwgHyUsHmXBeY7fn32Wgoh-4KATXEhnxzWIp2BMwg4uK5jOmzow5xcDHjveueJYtVpkZ74IJZ4lbrt6432Cud-rHtv9aM_gqYkDAsef_vBBDS-XikbwSfF2mH91nvnP2u73W6Fz8V1324njFNghpB2bjiz9cWX6kagm1qk2nWOBLecY4aqGo64TA2wSHqP6E0FMID7m1WSrOjLVRVR8o7gTbkRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqKDrUgztdwxEVwJaYfKXRIsyQ-PUmHhl-W-Mt06yfLdaRisLX6JYHI4NipuWPxCr04-yvyKLhfXhdzvzt8shC_YWnyYtAPdArOVtuTLb5Yeftlx-OC3a-eSBNXVofNv8I-1GTSTE1N5tUPjEHbv9nUajrjTMFGt28oK2s5cc2xj8zqzbLCLZw6UwaNUNlon8t_Y_jIxtRu5YpFiToEI9WPtmLFYFQAYmxd6O-VwhbG3Dx1GyXqGztG8aLUQDqgjHAt1gwKIUnDFnUMikEV3vDgFmxMzcJCmZFrqm8P1oDWCxkiGnbN6sALbs1hGAfqWXJ6BPwwffdHkWvFvwnXZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rK-KzlTEsVlbtxjpBMz144xfR50K0Rg7ikF_olpSLrz1T385c551Ml0oHINaqCPS_apOGBdBEtVRl-ZTcfd268lOgWZV8j3hyn2gE2hAFU_h-t6o0mHWPgHWPGoO83JhlTgbAcVT8Z6TRGhWo2GQ972ScdJz5rkHbc6PnNBhCumpISdFZSzDnTDhr2UPaw-6Ts__2ySzusdKkEjTZ5u0dXL9kJJVaGGeDPjYzW5KrK9CoeVqTrItjo_7f4Hzuk9OnWX5YSCZA-1QY64TRvN05z2iC8C9yS1NTCO7rc4ZuD6DCAcIf-IFQxLf3pDdduHjhtrs9umSFX2QCxRI0jEfFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jc1IAUWUzo-flc6SgaU1lWZ872KJhBvEWPCQINJtsjJRF8-VebLgyVzku0hJ5RfXJQ7VM0U68r2RrzQSwhwc3XsWzT4urbez09cFydZMDdIg3_nrbeJzozKDVlop086BgQ3NcBspXI3I1DCpEnXMJi9mjjXDkTVn9JINGPY8lRfWPRdUm2k5PnN3j_P1uK2iXmMzpdC_-OYBOBOksij9vzI-_hO8Wu1ktw55syVuUg6h3mwzBYbaZDgipIi-a0b9EFoM8KcgRH1qiYLMr35NfSuF2qcWv7z4504VkrWit317TGc4avzDeoF0RRLXjpDsVecBkxWP7L7VXwJj3Vxd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlbH0offhMuf4UclsoXZeLbOy7MIm2p9acLCmYmpaxTasO6lVMg_1hK1pyy0-Lze2hW4je1n3w0xgB6itqEunnQ4PiEN1W77vD7XwJPvxWCWCGd7fmazcKQdgmoM81bz_UI4TkP0Bj33C3Gu0PoNQHIpmX0DI6yQ4R56TVN9lmAx7cs-q2x69I_82VEjrA3N2CMG0Rn51whCaHnaU6xVAcsBAAL_GNox5nv7GApVDksxEVFIFc8i8bCTOne8QuosOMee4qZXgJ_5HWKf-653zxMphfkROyenswDVbPt7hGS7UC5rZBw_lHr8OIyF-0OuzmZyg8CqQad0bnz6Ez_a-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVl_qRJw2M14sZrhuoOPW5aNVbi1B7mazB1CqMGE46Y2u22kBlJPDmNzLalr5UgL_5XFofbP-r9oB8MDmdHKZb-pnGwFMTpr-rEF9DNDbvHPcVWWBuqNyxPqwMBqYOKoxsqyB6VcIxEGDtAj9mkBUmN5l2GuYbQU_ZypUbgNMO5TBbChE4jhb9jJB2MiTH1LuryHwU1FcHyVnAVa0-0KenC3z9EEdzBlZSbwwkpNSSUyls01r8uaZBzEg-yn5yJXSEU4jOH-jgNMVcPZ6Ybsmqzjv2QsxNWmALTLBhs-iNvAHoTW-kBAqZi_UKg4jk_EqKSiyEQ_-7dzQppDuMqUuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ با آغاز انتخابات هیئت‌رئیسۀ مجلس، قالیباف در محل رای‌گیری حاضر شد و اولین نماینده‌ای بود که رای داد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/437914" target="_blank">📅 16:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437913">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4egP_wNOawQ67BSos_ieiwncFZ2TgIkLN9DScq-_Jg-1BuFmdsg6xsTVCFhLLCEhIQ0SFVk8XDRRywI_FAGAtCL-JwaFO1IqUX3zTxw_VVS_ukDZzAlPCnka28IMpR--U9WEMX4okbkY76K83CyRAPSA6anjQSQil6iMArEvwdy81VsLkxYSn5OTis8C0PYAUVrkhoUkRdD5a8dZtpCaSv7kifZNzIWCvLP79YOB7LNi1opUYioYrE6NdV9ngp4jqj-MUG_XfwzrXa4xSBYEGwFBeyYINbnFq6qXLbXE6XPBEL_GsxHEr6u-0AkFzUbyup25U751OgZl3bNZzL3aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تابستان داغ در جایگاه‌های سوخت آمریکا
🔹
گزبادی، تارنمای آنلاین قیمت سوخت در آمریکا پیش‌بینی کرده امسال آمریکایی‌ها گران‌ترین قیمت تابستانه بنزین در سال‌های اخیر را تجربه خواهند کرد.
🔹
رئیس این تارنما می‌گوید به‌خاطر بسته‌ماندن تنگه هرمز، میانگین قیمت بنزین…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/437913" target="_blank">📅 16:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437912">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پهپاد متخاصم با «آرش‌های کمانگیر» شکار شد
🔹
در ساعات گذشته، فضای خلیج فارس شاهد نمایش اقتدار دفاعی جمهوری اسلامی ایران بود؛ جایی که رزمندگان ایرانی با رونمایی از آرش‌های کمانگیر با سامانه‌های جدید، یک پهپاد متخاصم را بر فراز آب‌های استراتژیک خلیج فارس با موفقیت سرنگون کردند.
🔹
این عملیات که با به‌کارگیری سامانه‌ای با قابلیت‌های پنهان انجام شد، پیامی روشن و قاطع از سوی ایران به شمار می‌رود. مقامات مربوطه تصریح کرده‌اند که «این نشانه از طرف ماست تا دیگر هیچ پهپاد رادارگریزی نتواند بر آسمان خلیج فارس نفوذ کند.»
🔹
این اقدام، تأکید دوباره‌ای بر حاکمیت و امنیت کامل ایران بر حریم هوایی خلیج فارس و آمادگی نیروهای دفاعی برای مقابله با هرگونه تجاوز است؛جزئیات فنی و عملیاتی این سامانه جدید تاکنون محرمانه باقی مانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/437912" target="_blank">📅 16:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437911">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a8f1d68e.mp4?token=sr-eQkrcgGe7fMpoqXLnANnNP0llFe-I3yNkn4aTnz6ern3JXDxsJxTuFyWFNDRbzm7CwZu_GpoR6ujNFWvHFuBUtWs05sNIMkA-E8TiygFdf5M9RSDJdGU1egDOvKlUXnmosIUKwOz0kMRKWtQSGYLLX0OZ6W1-LmKsTxF4rH9do7FnC1DUFuo__W92Ex8FPHCHmm0kF46AI3-J3nYQAVOHS0dOVh-EMUTi1YfQUMQ09S2eDbYCDYZc34JXG-5k0wZkLuhGrdU9oNh0xAh3VyFbZTpV5Zt8QJWIoZxfsBxKnllahJlH7NSJGGEX9wPenwIuwYcEqN1ukaV-GDsaaQd7hvhkf4NZdc5hTDZ46BoOYGhOHZCo43ThxvAY9oJfQoy96CS6ESbePT_uwxtEh8iy_eqChAIW3Jdhv8zd7iypxNx3ZAyq7sPj8MAdqRotijCSqjIPBj4POgO_JDWw_DLEkF3_RE8cOgj9i3CiJnT-3vcxGfIzDVXe3qAOtaI3CGUkQ9QjsIFldZwjPRAygQy2iHA7-xmJfPcMUc1ciOrai6O6_tEBrIyaHsE9fDNcLnXRe7Gcrd6AJMVKmbdgeyYBQUaU4Oh8Bnrn7zLUVMIBtQtOHsBdhMy0JdT-RxvNWw8-UyN-PPgCuTrgyFltJ-3kHha4cXnQaATK5GqImb8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a8f1d68e.mp4?token=sr-eQkrcgGe7fMpoqXLnANnNP0llFe-I3yNkn4aTnz6ern3JXDxsJxTuFyWFNDRbzm7CwZu_GpoR6ujNFWvHFuBUtWs05sNIMkA-E8TiygFdf5M9RSDJdGU1egDOvKlUXnmosIUKwOz0kMRKWtQSGYLLX0OZ6W1-LmKsTxF4rH9do7FnC1DUFuo__W92Ex8FPHCHmm0kF46AI3-J3nYQAVOHS0dOVh-EMUTi1YfQUMQ09S2eDbYCDYZc34JXG-5k0wZkLuhGrdU9oNh0xAh3VyFbZTpV5Zt8QJWIoZxfsBxKnllahJlH7NSJGGEX9wPenwIuwYcEqN1ukaV-GDsaaQd7hvhkf4NZdc5hTDZ46BoOYGhOHZCo43ThxvAY9oJfQoy96CS6ESbePT_uwxtEh8iy_eqChAIW3Jdhv8zd7iypxNx3ZAyq7sPj8MAdqRotijCSqjIPBj4POgO_JDWw_DLEkF3_RE8cOgj9i3CiJnT-3vcxGfIzDVXe3qAOtaI3CGUkQ9QjsIFldZwjPRAygQy2iHA7-xmJfPcMUc1ciOrai6O6_tEBrIyaHsE9fDNcLnXRe7Gcrd6AJMVKmbdgeyYBQUaU4Oh8Bnrn7zLUVMIBtQtOHsBdhMy0JdT-RxvNWw8-UyN-PPgCuTrgyFltJ-3kHha4cXnQaATK5GqImb8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باقری، دبیرکل حزب عهد ایران: قطعا نمی‌شود به آمریکا اعتماد کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/437911" target="_blank">📅 16:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437910">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p81TYYaCSaiaah1fAjBhnj3XcFeYUuoiCIAdplweNrCgeDORZ7ONTcm3-Ohd4eemHk7aJFflqcN9khp_eFk4EAFwTA3y3lLWSmUsQp1MtmFtXQkNzCDkDn-dgA6F4sx_qiOHZyWE4vRjA1q9uweZ6mHHTwJ787BHI_CwRlmX-v50adXz-ZtSXAcMSG1I4kapcvyU8ZJnwoa_qtTCdrUBvRU3B0j_QxA7ca2laJlAf88NBbkJ6_pG2BRHaKozmYI7I3bWZVE4B-6G_aSHfh5EGG9Mv4u-zR2RknmeDOAFxVSBx4S-sY5IcmJzV09Egq05EPTetwYnUV-42GOQtGKqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی‌برداری مصر از پهپاد ایرانی شاهد-۱۳۶
🔹
ارتش مصر از پهپاد انتحاری «جبار ۱۵۰» رونمایی کرده؛ پهپادی که به‌گفته منابع نظامی، به‌شدت از طراحی شاهد-۱۳۶ الهام گرفته است.
🔹
مصر تنها کشور کپی‌بردار نیست. تا اواخر ۲۰۲۵ دست‌کم ۶ کشور نسخه‌های مشابه ساخته‌اند یا درحال…</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/437910" target="_blank">📅 16:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437909">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVRbVH7xiUQHY1FiddmHA821ukyzyWtDF9IR4OrAuN5kHEHtXSDHRObkGK09OSpgJ1RA6DzKsiMKWN11hSJYKB35UYDX-JcBXBjmiufG0upMurk-xcikZ9g-teEqHTmdQ9BPIvZi2b32HGdLsrTyr-ayWPAePaxVg9jpfVnwfl3C0QnFK_SBs8ja1EscohYUPMSuTXooovVqosY20CydNHSLKC5ggB-UQCk-7f4-sOOxrJizBJf4Tkxvc3kZq6nVjzzlQyWvlu2ocZ08fxa_1nYcZVHqVaVflHeYv_K4D4D9HWa0tP8B05A2oBStB5D8Uvbs69cGH_VW6eugi3__Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسب اجازۀ مجلس از رهبر انقلاب برای رأی‌گیری وبیناری
🔹
سلیمی، عضو هیئت‌رئیسۀ مجلس: با توجه به شرایط جدید، از رهبری اجازه خواستیم تا جلسات مجلس را وبیناری با امکان رأی‌گیری برگزار کنیم؛ زیرا در قوانین فعلی محدودیت‌هایی برای تشکیل جلسات وجود دارد.
🔹
به محض دریافت پاسخ درخواست، هیئت‌رئیسه تصمیمات لازم را برای آغاز جدی فعالیت‌های عادی مجلس خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/437909" target="_blank">📅 16:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437908">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfbde40c65.mp4?token=mBcES5its2mWtBvJiqvlB-DrWeWNVedfxNrCIoAIEBOGimf2L6YD7e6kvj_PBPVpGC8xKCp9IvfdRKQUWr7z4J_rKwpPt-Bhb-N6bblkvz7XymwlS0O5Mz5sBzCf8ZM8nYagrjgyvu-EbdxQYhMs-FLhRfReolsGKj8_WKwmE5wQLl-AONa9YolLaoZ4F_VdTxOvEI3Xp7sC_qd7kGZwcqqfhyoeZEcxi04wYobod022AKFHbznd8r94UsZYUdfPYk0LZ3TFmC2hw5ws3XpmJgzDz_e1m-9Sf2QwOa3bSFwQtxfKSk1ElqZ69wNoNQaw5wGJuOJ30WKtJx9J0eTCu7ZttCph4GeXD2RCd0R4eCHZM-YhoxgqZP0lOTYekFcQk9rdmHjqw4WXwpcaFnqxlLM7Jzx1ip81mjXcpXpcZTfkbej18j7mMcVuOxyyX1lSkXcU0lJow3IrBbCvXJduvLDe1efKODSrQq8GUQx5LrNes4c1sxtIYA7KZSQWcWri9k2aLaFuSxmhayOWtLp9LC-PF-jv-dXA2luz6G2BtJpxacSuPPatyH5WF6hwlqy4z00iG56_HS-KtMYt81vmnv2QTA9_4KCbjlWlRheovWZl-QjND6WCfyVEAWP_sXfxf4rAviMiuHmTpIeQz0pMwcNgsLmdLIwq_-F-n0Sg_P0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfbde40c65.mp4?token=mBcES5its2mWtBvJiqvlB-DrWeWNVedfxNrCIoAIEBOGimf2L6YD7e6kvj_PBPVpGC8xKCp9IvfdRKQUWr7z4J_rKwpPt-Bhb-N6bblkvz7XymwlS0O5Mz5sBzCf8ZM8nYagrjgyvu-EbdxQYhMs-FLhRfReolsGKj8_WKwmE5wQLl-AONa9YolLaoZ4F_VdTxOvEI3Xp7sC_qd7kGZwcqqfhyoeZEcxi04wYobod022AKFHbznd8r94UsZYUdfPYk0LZ3TFmC2hw5ws3XpmJgzDz_e1m-9Sf2QwOa3bSFwQtxfKSk1ElqZ69wNoNQaw5wGJuOJ30WKtJx9J0eTCu7ZttCph4GeXD2RCd0R4eCHZM-YhoxgqZP0lOTYekFcQk9rdmHjqw4WXwpcaFnqxlLM7Jzx1ip81mjXcpXpcZTfkbej18j7mMcVuOxyyX1lSkXcU0lJow3IrBbCvXJduvLDe1efKODSrQq8GUQx5LrNes4c1sxtIYA7KZSQWcWri9k2aLaFuSxmhayOWtLp9LC-PF-jv-dXA2luz6G2BtJpxacSuPPatyH5WF6hwlqy4z00iG56_HS-KtMYt81vmnv2QTA9_4KCbjlWlRheovWZl-QjND6WCfyVEAWP_sXfxf4rAviMiuHmTpIeQz0pMwcNgsLmdLIwq_-F-n0Sg_P0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگو با رانندۀ نیسان معروف جنگ رمضان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/437908" target="_blank">📅 15:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437907">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f6c61094.mp4?token=pZ2duBBDHXTRa5_hZLG0OlOwAMyS61Awzu_fhbH4gBTnXvd0xPOGgYfGvX2ZGXrn3JpDOKfDhT4uOMhD0VCnodyCnBNK6FavNWrbJhJdDmKqQkoydv-teolRXcf2cpjIbg0elP-m178apFZo74bG091G3Cs-xHPi0WhyC0mSJpNniPVRbMsVEvW7_GHaGgmAj-9FzOCCXLlMQ_i0M6je-ezflkbQ3iHRQ2UVwsy6JyHEwpvD57YP9mne8IRSbCCdjjDz3dGpQuT1bBTaj1q0TwG4xihJAdNlka4fFCrODRGzekLjC0XXb1rNzR_S4y442uNTqdzlPryZpcGIbjx0Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f6c61094.mp4?token=pZ2duBBDHXTRa5_hZLG0OlOwAMyS61Awzu_fhbH4gBTnXvd0xPOGgYfGvX2ZGXrn3JpDOKfDhT4uOMhD0VCnodyCnBNK6FavNWrbJhJdDmKqQkoydv-teolRXcf2cpjIbg0elP-m178apFZo74bG091G3Cs-xHPi0WhyC0mSJpNniPVRbMsVEvW7_GHaGgmAj-9FzOCCXLlMQ_i0M6je-ezflkbQ3iHRQ2UVwsy6JyHEwpvD57YP9mne8IRSbCCdjjDz3dGpQuT1bBTaj1q0TwG4xihJAdNlka4fFCrODRGzekLjC0XXb1rNzR_S4y442uNTqdzlPryZpcGIbjx0Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شمس‌الواعظین: طبق اطلاعات من در مورد آزادی اموال بلوکه‌شدۀ ایران اختلاف وجود دارد
🔹
عضو شورای اطلاع‌رسانی دولت: اختلاف در مورد رقم و زمان آزادی اموال بلوکه‌شده است. اگر این اختلاف حل شود یا امشب یا فردا شب شاهد یک تحول امیدوارکننده خواهیم بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/437907" target="_blank">📅 15:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437905">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌ رویترز: قالیباف و عراقچی در دوحه هستند
🔹
خبرگزاری رویترز به‌نقل از یک مقام رسمی ناشناس مدعی شده که محمدباقر قالیباف و عباس عراقچی برای دیدار با نخست‌وزیر قطر دربارۀ توافق احتمالی ایران و آمریکا به دوحه سفر کرده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/437905" target="_blank">📅 15:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437903">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رئیس بانک مرکزی به قطر رفت
🔹
عبدالناصر همتی پیرامون بررسی آزادسازی اموال بلوکه‌شده و در راستای کمیسیون اقتصادی مذاکرات به قطر سفر کرد.
🔸
هیئت قطری هفتۀ گذشته دربارۀ میانجی‌گری مذاکرات ایران و آمریکا به ایران سفر کرده بود. @Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/437903" target="_blank">📅 15:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437902">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwSf4CBBo0G3GPrBkvFUu2OIKBzv7mFFfdpzaw4T2X40lKj0GESK9kwPaV8-8Y1AtDHDfsJVNjt3X9bfKXCI5ZbDvXwm6xEO-ZwvuAimV7Kp9NeirHDXjPo4d_FPBXoa7si4k9xEJzGOLqipcKi0qNh8TytRAOlLOn8dMcywcrgG8oipd7WqxR6WxbtX29BR6ODNxCbvfumbDRTzMHoobGB_O-ekMvvmVbGhBRwBaV5QlM88KRnVyvlF95XwU7AukGc2mxumlVtq7eh5Ttya9MAcyBbV_6kDnD5HA7smKkQD-1wrxU7ERjbaaB2CI3XjPGQxFFWEUkw1iqOxMSJV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنظله: هویت افرادی که به ناوگان صمود حمله کردند را فاش می‌کنیم
🔹
گروه هکری حنظله: فردا هویت افرادی که به ناوگان جهانی صمود حمله کرده و علیه آن اقداماتی را انجام داده‌اند، افشا خواهد شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/437902" target="_blank">📅 15:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437901">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JW0tRyDJDDTFS7q5aeAHlBvXi1cspd8MirtOG8-XH3isO-6ljD_gEM2cfs9AR5h_pM08We0YeQW3JbyCX5xwz86SxljQ2oJds7okb9hfP-FNy8KYds39oFNkLRhyZzujITsP8qw8MofHteF_X1WE026fSaDqFKMZ0mok-FjHQBdll1kskpZIQ1CKerKLsZ1lRsiMJvGWSZfXT2XDxb_2N3NKRRV22jZWqqngbXHd547cS__DxV2u8QJvJXD2cYMzsKRUwf-hyFSQuwOgGF-6iei0uHiJ_87gEch11z6QBmpkM66AoJPoU0sxS3Bkk4Hca2AX-KSKH1HB7QSMerx9Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واردات انبه ممنوع شد
🔹
سازمان توسعۀ تجارت ایران ثبت سفارش واردات انبه را تا اطلاع ثانوی ممنوع کرد.
🔹
استان‌های هرمزگان، سیستان‌وبلوچستان از مناطق مهم کشت انبه در کشور به شمار می‌روند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/437901" target="_blank">📅 15:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437900">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgnru3JVRnOosWN_pFl3BIrWptX6pVkIHDfZ2zU_p-9E6uoXoyaikdfj6Yl1z6T0j9J1au9a_kn63uR2-TRrNOgL1iDwxZX1tH-rZblsFiEaj7aZNAc-e-wdK4BjfRXtLUAB1sjznpUnJHABwsV8spZBkIVjbV4OyvzXKn9v2c84EObjrp4uANcEwnCvomL-1Od9LGWwClYy5QyvDOdWkwrDgQZX9auIlD4aQiz_m38IfKwu-2pXqFQQvHBZXfnd33RJlq4822sbP-GE7jkAs35EMpdp5Wy14_0yjyyyGOOgWKr4VM61pSSO9UjPvBJEv-axoVpbGTrdlZcewrZ_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جلسهٔ ستاد ویژهٔ ساماندهی فضای مجازی به ریاست معاون اول رئیس‌جمهور، موضوعات مهمی در خصوص برقراری اینترنت بین‌الملل مصوب شد که پس از تایید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات ابلاغ می‌شود
🔸
یک منبع به خبرنگاه سیاسی فارس گفت: در این جلسه برقراری…</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/437900" target="_blank">📅 15:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437899">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d53ff24aa.mp4?token=agxPmjC6VmGlPVh_CBDkvN0QUXyP47QKhVcxeTwTV8Ur5NXaRIg-qr7WyNdcVfXrPc_plndMIwBsZUqhNlCTdEtjWAZRUiKy4jCJeY-qfY9i-LLGpNziRb2nW20FZVfxB5lARuGFGm8-ox6l20QOzK6u8XJWLHb8OiS7cZ8IkRhMb4VfJGw3grX6kVRovgbWm23HlRmHqY864wRboXCOvEgyS1LCzipVfcFGzNiM8hQv1Yu7ZKUHXJ9UziDm8t04LiaR6cHX-rXVugHJBEPwA9rETm5A77WH9Oyahyt1SGhI_aLHGDEqzvedjED-ECQMJkqP6keAujzYRqIJt1zWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d53ff24aa.mp4?token=agxPmjC6VmGlPVh_CBDkvN0QUXyP47QKhVcxeTwTV8Ur5NXaRIg-qr7WyNdcVfXrPc_plndMIwBsZUqhNlCTdEtjWAZRUiKy4jCJeY-qfY9i-LLGpNziRb2nW20FZVfxB5lARuGFGm8-ox6l20QOzK6u8XJWLHb8OiS7cZ8IkRhMb4VfJGw3grX6kVRovgbWm23HlRmHqY864wRboXCOvEgyS1LCzipVfcFGzNiM8hQv1Yu7ZKUHXJ9UziDm8t04LiaR6cHX-rXVugHJBEPwA9rETm5A77WH9Oyahyt1SGhI_aLHGDEqzvedjED-ECQMJkqP6keAujzYRqIJt1zWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ عبور ۳۳ کشتی در شبانه‌روز گذشته با مجوز سپاه
🔹
نیروی دریایی سپاه: در شبانه‌روز گذشته ۳۳ کشتی اعم از نفتکش، کانتینربر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند. @Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/437899" target="_blank">📅 14:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437898">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e120ca66a3.mp4?token=U8I5tzDVX29AnCbiwVtBZEj6rmru55Qhzakpy8wXup5BvApkKHgiFLEk7NuJMwhPfbLlXoi1VzwRm9i_ucp7ZXuMQTFrt-pZiE9zZwGKEIieONZUYU724EdpAX5BLG3RKIji4YgnPY28g8tAkFB0uALmc7-Mdtz5aPy024Vjzqbl3wh5s0rZd404SL-mtZD6Gp9d2o667z0WVM9e3J9P39bQ9nxB-XZ2a2_2XhQ8jNaVyisL8JE-YAQm27sz1zcLcQKLiwnst9XNQRHe27uyEBIJiUr3KhxvvDq8RobsiWl4K7VvcUs-IaTYyi8FisOq0SVPF-mmAVtlwe9pI-x-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e120ca66a3.mp4?token=U8I5tzDVX29AnCbiwVtBZEj6rmru55Qhzakpy8wXup5BvApkKHgiFLEk7NuJMwhPfbLlXoi1VzwRm9i_ucp7ZXuMQTFrt-pZiE9zZwGKEIieONZUYU724EdpAX5BLG3RKIji4YgnPY28g8tAkFB0uALmc7-Mdtz5aPy024Vjzqbl3wh5s0rZd404SL-mtZD6Gp9d2o667z0WVM9e3J9P39bQ9nxB-XZ2a2_2XhQ8jNaVyisL8JE-YAQm27sz1zcLcQKLiwnst9XNQRHe27uyEBIJiUr3KhxvvDq8RobsiWl4K7VvcUs-IaTYyi8FisOq0SVPF-mmAVtlwe9pI-x-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس بانک مرکزی به قطر رفت
🔹
عبدالناصر همتی پیرامون بررسی آزادسازی اموال بلوکه‌شده و در راستای کمیسیون اقتصادی مذاکرات به قطر سفر کرد.
🔸
هیئت قطری هفتۀ گذشته دربارۀ میانجی‌گری مذاکرات ایران و آمریکا به ایران سفر کرده بود. @Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/437898" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437897">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyP7HqvNAHJ_o42mOf0TFYK2ANCttrgtYg1YtmmlkhAUp_EAiVOlBPrS4zq1EG2ZIDTc8h2h55Y0aiaGT5usK98hnwvEtPYHeAPpInm2s_9zxgpxTizCZuEPFxNlWU0cDFvlImIx8XS4PpxaLLyFO3tkzF6JsD2MEkXG5E_xKhjArqympLwT-rTyk1Ku-ZBIdW0RVPGuQYOca6xkAKVFatcafc1JQHWTI84CB3QnD0YAAMqGIWE_ZZL_dbyWKfnps9hshcElxdp3HMrp7w6cQMmoZPTHh_lx-nVeUQ3KBKCBIJGiSI-ptz40JvaGUr74roMIfOzSd0cT2hUS6kwimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: یا با ایران یک توافق عالی می‌کنیم یا توافق نمی‌کنیم
🔹
من به همهٔ احمق‌هایی که هنوز چیزی دربارهٔ توافق بالقوه‌ام با ایران نمی‌دانند و از آن انتقاد می‌کنند، می‌خندم.
🔹
این توافق دقیقاً نقطهٔ مقابل توافق فاجعه‌بار برجام است که توسط دولت شکست‌خوردهٔ اوباما انجام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/437897" target="_blank">📅 14:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437896">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRP-NRzeCXNFQRDcTdwnNaaIoVv2S7VRcLMZI2L5fGNZ5i-ZsQyaw2jCPoyvFDAbg7H9R371GLNPBiChcB08SzWVqzj__ZNRP9cfClsCsdEB5ikIMp9vSx2fZVY2d8EaieflxJHpYFPWiR4YNZVFNEqE493RPNbrJq0gv2kAfkdUybjsthKLlE8PE16mbbVwera1X5TGFVbz1nKqAtWaKPdjBs3A6WChBU_E9NkGr05VKwE49lqjWPWUD3AkG8WeGK4lDAGvakC0Zf9EQzqqrjB-pfdQB7ZB84b332dLoeFWruAjdSzgp04k7jRP5BO8yig4X5DSAoLkxsw3LmJExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی به قطر رفت
🔹
عبدالناصر همتی پیرامون بررسی آزادسازی اموال بلوکه‌شده و در راستای کمیسیون اقتصادی مذاکرات به قطر سفر کرد.
🔸
هیئت قطری هفتۀ گذشته دربارۀ میانجی‌گری مذاکرات ایران و آمریکا به ایران سفر کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/437896" target="_blank">📅 14:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437895">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868d082d3a.mp4?token=AZnukhuWA_5E2EVsnBm29V8LG3XPGOskl7o-RCJfsDxGISC8SA-sKoSzY5EGKUGUDpPFuSB1XmsV3ijIi-mt91CCCy3yDsb0UiNQQpYV3uCpbrG__Ae1UjX6XOuDvBbVOwgA0I3Y7jYW5kxkkayFhVI9KNiG6ePKnuHuuYRCPQolVnrhNcIulBu6HHn_enFQNKg0viO7ezhHVmIqPRTRa_oxe1KhTGhs21V-wNcZoLbbT3BgH94l9ixkAa42_dj4Jg6SjQWBZDrZXM9XpbeLsuKywtDD0a6HqqgMcryKM1pDfWhzmMQC2QSxF3L8Nt0SFpSRVZq_SEWGIqumq9eFSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868d082d3a.mp4?token=AZnukhuWA_5E2EVsnBm29V8LG3XPGOskl7o-RCJfsDxGISC8SA-sKoSzY5EGKUGUDpPFuSB1XmsV3ijIi-mt91CCCy3yDsb0UiNQQpYV3uCpbrG__Ae1UjX6XOuDvBbVOwgA0I3Y7jYW5kxkkayFhVI9KNiG6ePKnuHuuYRCPQolVnrhNcIulBu6HHn_enFQNKg0viO7ezhHVmIqPRTRa_oxe1KhTGhs21V-wNcZoLbbT3BgH94l9ixkAa42_dj4Jg6SjQWBZDrZXM9XpbeLsuKywtDD0a6HqqgMcryKM1pDfWhzmMQC2QSxF3L8Nt0SFpSRVZq_SEWGIqumq9eFSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ دبیران هیئت‌رئیسۀ مجلس مشخص شدند
🔹
محمد رشیدی: ۱۶۹ رای
🔹
روح‌الله متفکرآزاد: ۱۳۸ رای
🔹
فرشاد ابراهیم‌پور:  ۱۱۳ رأی
🔹
مجتبی بخشی‌پور: با ۱۱۰ رای
🔹
احمد نادری: ۱۰۹ رای
🔹
سمیه رفیعی: ۱۰۵ رای @Farsna - Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/437895" target="_blank">📅 14:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437888">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oa0hbMoPqcxf4GwReI3Ov9rkq8jCQbABppEhUGnjH3TtvbH-o4-CzPtMhmlG2-ENIEaCzSFuAPI0i5vEPJZAgjFUa1tiELOvdAqEKnm_g6gGF4x5RQZgt2O11q8u2k3qVHoMI14G93fAghbnBsfD9wRgksk-_ept5IMazAB2z4JWkrKTIHGj1jb6qj2xX6NiSVxHvY0HM2v57CFvdWdwP27iE6uQBcj7iYHAjnamoLEYa6WISC_6ksdkCgHgc3EwOj-s0OL6Qc05wVmP6BWgmctS302OXlskjdBXUHDwfHN2gNOal1mZr9V6HUaBCcvYIVu8OR1kcmhP5dsgq8Yi7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkWAKa0VdArZS0neHaNCtwHtuaro6OcDd2ErP7KVzomqLP-TvF_d8xScRWg5Cjmoq6xqUZV1i2p32LCYKI5D8nRSV1lBgxFZ6c9a-0O7Sh04FnqYxLRTqWGEFFqh4Ejarp1ndeSlMzL_UtzkHf9RsFt99lVJuITViCXyIIVCyQ48u4A4gOV28UlQfKlnPkVW7Or-gTAXTSn9qKotmR0jdHgL-vyFeD5w567CO2v0_Cgc7cqqOjLh4y-Ny839v-uBGoOYAJUdaMtNuYxeTqOcaORbvd9r-IYPI0KpkxCKfJw3afQ1NCf0NQw2_7YsxDl1dpM6GSrqYRqREgQh1N4JNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTdMYsNJ4vIozsPbj2Ul8ICEWfl7DMyhECxpDFWIHTejeZHvSGkhEYV4eh9gRcRlgec0SznuUx6tbbHXHUVdjlRsKpeM4nqiNUathRmSJRp-nwtRBJuKsKbYpFl1orq4vADnbTOzXbKvx26jKb2lbm6hWukXWsDZiNFr30Gq5Tj-tQsKeIryiLl-RyzFrBfRCVryFoG5Ora8IMWjX_aQQgi-05JEJJsWJiT5-WpuTaGtWuF8kd7ZBQZYZ3Q0p9fc-Kcgz4NgNM3-Caha7sIq2fWBtu3KKCdg-dncQhpu6Yf2H7xg1-vbiehMsBQpmu7D0nEFPMewOaP0nGn6OJ7AiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwUaTDd0MKKRRmegIISd9ihEXMKdKS_xAnwi4B2wIIu9B1i30rKhTH25Av8S3VfyDUwbNXm0I6id0FaguwtF1YYE2PyDVFuSFXzQoDhL7fo6TA_0x2LLohoMJZVuikyaJkQHXuUn5cuVPh-LcfSraKzwaJa8RY_uiplgZl9KHkyZ7_DWcVn3SBkvGd2aeLERzVAG4vcF_47MQpur-P2EUXNFRzfcFfs3Kk5pc_wbaBCski16OBdIYMBIvJT0KUu8vxIARbYlg0kpsVTFglyIt_NhqKk7unpZztF34tYLbXuXITxhqf8sO5KMYpKBg5chj4YbgwMSAZpsEdQ8kZkfww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcuE8pUr6GzModzwC3EUQG7kKt-IYwMg63OhQn3EByZoege10yrOsVpnyNJVkpVx9C4NLFXKFVayh1aB5xx97q2U_SX7wTPrVUhD-uQhxQbn1BljbKhMbV31myX-VgAtRXFWs2aZO5wzrnMmPBMlHcz5CU9otlrSIGuP80eyHHXaeAQIwSm7neMJOgVCb2t_VTfgL8PTPLp1fZUVmGts2aWlAfMHso0lV7k-bac3nG1kiXM1v-26mRE8CkbT8g9ojbh_7Wz_NsRJ5XX3UjQzAEV7yo0vFXO_yCWS0WY4ZKeph0dvX4f-ACIg0x46a5Yi6U9u9bQthR1uIwknOeubUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L33N3jPm19Pgmg3arDZX5MAoCCGSXzt5yHscMiT5UvjAfsUJQ3mHSvTjCX0yaw0v8R_2C8ndyW4tFGn3iJLTxU_S1Kto_kY02VcoUdnKP18wgSokeYV48w6tQuxDZeax8a-6iNmI8vxgSpHrTMU1YJ1dn2Bl1iII4eMg9nLdJkeYOy8d2gKPSTR1fZDsvgh8J1Z9oV6SioYMuAWg0RE-D8CjINOYUBWvzJKsSvYkn7RdOheE51UB1eekD039bMhdhn2Q9UhEhAYcdyr_6ARChjj436YsZd5RwZelb99hSJ5EEPCdOpgv1ud_v3rijnhj40dA-cfNggk86jBshepDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wy21MCWN5_-TAKLUVo43dC8qzyY2CcNzKurGFeno12iPUGvCkFtLL0jizyqQdvQgOD4mtCPITdEnJeORD1L4Qm0y9WDz4bPL366UYHpIZKdMTpKTOGHtQU6bUfKYI1R64OQ3X-KadslF7-MXeqbZsP-VexZJenzuq1OjZGZGC4CmrDASGPw_dKRptpCXKJIk5dljOlw73ChZ2bK-TzGe_i0Vwe9wBAv_AYII5_wkcRPiAXczmT5N08zliUAY_7r3NquRjjCNFuEnlQ7BN4sTTIVc4Wh7KSAidDJZMHH94228M9DT_BiW8az8vjHsyy-HJGiwKF_ACXX841o5TJhWOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: حتی سنگ‌های میناب هم از وقاحت مسئولان آمریکایی کهیر می‌زند!
🔹
مسئولان آمریکایی بعداز حدود ۷۳ سال اقدام علیه مردم و علیه توسعهٔ ایران دم از دل‌سوزی برای مردم ایران می‌زنند.
🔹
همین آمریکایی‌ها در جنگ تحمیلی سوم به‌جز مردم بی‌گناه ایران،…</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/437888" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437887">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c52eca46.mp4?token=duaCVTl63OwPR2JGKo6qonH4FbLgSXfPemPCY3ogN15o-LtFuiIAnvmidfUtQwhY8dQRTqDsQkCyvQP1x8p-n7n7VdF4y-6enaD-gF1H4Hcm36b1EF5WbeUVNkj3cHgud7Lxu-NAOETQG8FnQusa1uh4GNBmt2JX9DF3PVO39p9rhjYlK5QLnkfPn7zn0PdB-Nb_5nkmxKM95F9qQ-HsPHdFnIAuJe8MZTIK1PURsli4mny8UrAR3DS19cHk9fH2jB5pjccNvPQWAsw09szUxQuSrmN13Vb9NWzyhwRzXuLxpJ8Wb9kFXhtvoj1d4Sgr-gINz2XAuRA25hZPXuyNAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c52eca46.mp4?token=duaCVTl63OwPR2JGKo6qonH4FbLgSXfPemPCY3ogN15o-LtFuiIAnvmidfUtQwhY8dQRTqDsQkCyvQP1x8p-n7n7VdF4y-6enaD-gF1H4Hcm36b1EF5WbeUVNkj3cHgud7Lxu-NAOETQG8FnQusa1uh4GNBmt2JX9DF3PVO39p9rhjYlK5QLnkfPn7zn0PdB-Nb_5nkmxKM95F9qQ-HsPHdFnIAuJe8MZTIK1PURsli4mny8UrAR3DS19cHk9fH2jB5pjccNvPQWAsw09szUxQuSrmN13Vb9NWzyhwRzXuLxpJ8Wb9kFXhtvoj1d4Sgr-gINz2XAuRA25hZPXuyNAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت محسن منصوری از نصیحت شهید رئیسی به الهام علی‌اف  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/437887" target="_blank">📅 14:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437886">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPMcn4-_692zEEDclwJjLj8o1CquVHvRWnFiTZPrCp4rZGshBH5cMujlGQxr5c_8QOF679JZfjX24P9wihuJLS2vDyrnbhVHqeLOkRDK14Or2awEAtQIkIvF9d8oVcJLCDIosx9BADUwGSSFRC0Z5mZjhUXwiWxvwc2hYOyxDQ0rBdGw5fIsMUnwCQ-URXGRpGn-X51C7voX8qYqF7wrcZfNfA-Ecq48rNDUn1vMH5IgNBSGAQSOIkMMn1sRnp7_1YAgNCvqGTGWVXp_1m208wr4aRnrvyF_fX0B9WWIQ_84pI0apK-0o9G8GY4e6tMapK68BJC7I0KSFw2UGZx4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم جهش بورس در چهارمین روز بازگشایی
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۸۳ هزار واحدی به ۳ میلیون و ۹۹۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/437886" target="_blank">📅 14:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437885">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dce6905834.mp4?token=I3DvqH2jF2PPd_SSRVy9-gZ-z0hv1UWX6gS3coN9iwUDDGtymQTRRCAuViB4gqzc9HpOoiLZLGULq4WjEe3xaNifeL1iChckcgv8QXMIm8W4yI8PLFNfA_EWHffaT8n70iT7eTeuUNcaEzlXvc9V8uS6HiJ__oGKgrnqPQ4huqbokgUfIvI2WJrJHu8EWWbdggt5zP6ssj6-WU_sZzm0rB2p_mhuGAE58Kf-AYtv8QlDTOEdNqvckoZd5WYclQcsBzW-WAYbdmt7Q9F3VxHqJtnWzHeOVYraD6u3sE_GOhNwgHOFXmrZQsiDaT35Ug9aMbxT5CxyHdYap_fvl2I0Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dce6905834.mp4?token=I3DvqH2jF2PPd_SSRVy9-gZ-z0hv1UWX6gS3coN9iwUDDGtymQTRRCAuViB4gqzc9HpOoiLZLGULq4WjEe3xaNifeL1iChckcgv8QXMIm8W4yI8PLFNfA_EWHffaT8n70iT7eTeuUNcaEzlXvc9V8uS6HiJ__oGKgrnqPQ4huqbokgUfIvI2WJrJHu8EWWbdggt5zP6ssj6-WU_sZzm0rB2p_mhuGAE58Kf-AYtv8QlDTOEdNqvckoZd5WYclQcsBzW-WAYbdmt7Q9F3VxHqJtnWzHeOVYraD6u3sE_GOhNwgHOFXmrZQsiDaT35Ug9aMbxT5CxyHdYap_fvl2I0Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تانکر سوخت مخفی‌شدهٔ ارتش صهیونیستی هم از پهپاد حزب‌الله در امان نماند
@Farsna</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/437885" target="_blank">📅 14:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437884">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONlLY93_zdQwrXnhQOpnRXpp-SDrrySNu2zzMQAOpHTWv9Qvi6fTXKeWFNz0KUU0NT4yoajqdVRTBsQzJzak11mELI4R8kbvEE9wxLaLClukkmHZFoNvkAVvTx9bzQLYVIW0wxWptPnWIgPdkTBUsdURz9WtGRZ4S8BZklmkdVtdRhHWxS_cL5_RoxZigGTf-4OwC1Bl6kk5pszPdyVUTZnk7FFfwQiB6chsGN48fnHJXQQvlEEYlaxKTyIeDecyqPoh-Hqd5qmr0QyUrvZE7f0Wy_qVVT3sMGI43SmdlrqWELnBMmWz_Y_CqEOAcjAScK2UB_swblII2SBA87vaMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رحیمی بر سکوی نایب‌قهرمانی آسیا ایستاد
🔹
در ادامهٔ رقابت‌های پاراتکواندوی قهرمانی آسیا در مغولستان، زهرا رحیمی، ملی‌پوش کشورمان در وزن ۵۷- کیلوگرم موفق به کسب مدال نقره شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/437884" target="_blank">📅 13:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437883">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No-qW6KyRpkZqldPzbfVwvIsAASE8Rq0e0A3aMFiWwNHQNHKFBHYKrpueGUsGDN9WyBEYJeDa0_Yx3WXR0eUi9pQO-cU3Re4WIR2D6vdOtveZUoJ0RiFsPTTVpx2Ba7gRbuy01D71kTq_1VR0fxAZ7OhX88TAdxb9i7ZqKDKVqjw7NBjutDzoF9yuuQGwHDc7223x6t3U04SzSzkczMpk0g3pC5Mq0-gAnsN5gOSzAtFwwFtTNHCyijClF2WzofpvHy-yNw-qAI0jfPgFFWtgekb_V5bIXF_qT9kTPu-nfAMa6_YoSUwAd2Xm5VMBcJkfU9kBF_O6F5pjvDqViDQMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رحیمی بر سکوی نایب‌قهرمانی آسیا ایستاد
🔹
در ادامهٔ رقابت‌های پاراتکواندوی قهرمانی آسیا در مغولستان، زهرا رحیمی، ملی‌پوش کشورمان در وزن ۵۷- کیلوگرم موفق به کسب مدال نقره شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/437883" target="_blank">📅 13:51 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
