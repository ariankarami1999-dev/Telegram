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
<img src="https://cdn4.telesco.pe/file/QNOjOX7QBytQ6vWu5Rzw5o-_PndxbAStToeN7ermZG4r5YuZTcs2mJRwDkYz2m30htpwX4f4NoTU7uLSbh_-vUFBHc9WsHZ_zhZh8cHwTmECSPbzoE3FyVmUFklxmCo3MzeJX7MmXHYtT-aHCKBHZ3JB3OtrGHJhJDlrEa5ukKmRBaqOBMOqaa9YrUrvuEeHX4Fzzcdj9rJVTrGXVUi59g3eRRQ8-UDEQreZ8VZQe2Ib4xjDCYmzYjpcpsVK2r-cm7hZzQ9GpzIVZfT4XI4qwFz2Apk9dcNIEJZvYgyVw_0Nq3gmFBqmChceX7Z1onFN4SLmKTXF_TIXqUutcEl7JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 19:12:41</div>
<hr>

<div class="tg-post" id="msg-683373">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8as7cU8fgVa3qWBng3ODqDAlcPNRM6hIfk5ImUb5j5lb08rFXlU3lnZpJ5eTw3LMQC9W4HXJuNr9MNacTmaRNXPx-_WNpTDUR6uHXr5612qb2vq9G7pkWr2PmpjYcbm-fVJdj8d1vSrQcZEYNRB0e1XLZjy4v1zi2gc2YQ-zG02rRVDwJbLIAcBXaWzfCti78I-iIDdzBF-8M2saEw63TafYodXTnrVhLpxARw-GALu2XCowiuSOARTXAwIdlQ9qGlEL_SncTKl7r9Pts1TSFqmeggK-rEbl9Lu0UB6347ZIHE70cdV9YT7P1rLCDtdp0pP8-y6Nz8EgG7QTnb_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدهای دستوری برای استعلام امور اقتصادی خانوار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/683373" target="_blank">📅 19:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683372">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag4YVmZYZzXoDHMbzs3kpGcXosVRryINXZPpX904J-GrAeXVQHsJrDqjcP3nPCF_XO6TuOrrY_6cfx2aD225i8ssk2h4c7mGpvCz66X4MUKI_LPtRmCE7F_ovu5DoEwAq6YjEUuYzpEeADQUEv80pOWz_eI4IyRxrornDDsMn5EJKyXz6UEpChL55Qkjxw2fbNCb_5WF0QSwS94c1STOlZxMtkdiZcAJ4xuB5fM9mif4NbNrT2GxMWc7-Ypwr6dnKOHj1iWrUxMDgTCsTv5_zSkXsi4bPFXsfPO80aVAVMXIDrK8FXShcSi9UfGKwvsc6HPpAmb_Y80wDwqVuAVA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع غربی مدعی عبور ده‌ها نفتکش‌ و میلیون‌ها بشکه نفت از تنگه هرمز شدند  ادعای باراک راوید خبرنگار اکسیوس:
🔹
جمعه شب حدود ۴۰ نفتکش از طریق کانال عمیق جنوبی تنگه هرمز به آن وارد و از آن خارج شدند. سه مقام آمریکایی به من گفتند که جمعه شب حدود ۱۶ میلیون بشکه…</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/akhbarefori/683372" target="_blank">📅 19:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683371">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbHp2jTK3OcJ5ywi1XJ5tOIWnC9rYLIJPr9Vm4Ur4tQeZNojlgwcDivZr6PhWLVvQdiri-2G71sW4G_OcPF2YZJ4dM-lFYvVV_rfWdKe-tN2eQUiXIQ85H01bVqnRcjdjZkeecUYI8xqBRs0LlXWbtumemEP-_TndEHgeURAu36UC-NGaH0U25qniu_X57Afxhk-2n4gO12k7ycakZguK9K4h6nKO48lSKxr6PL3VS4pvcRcA9fAomx-IbFqVhZlN3nrxzEeYARdX0VP4f6IyKOau2VGXS_RcLFfJa6yOdoOmjKcTZ956KBwUEtZGUvF8GxZHKAUgn81dDo1u6HN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرپرست وزارت دفاع: میدان جای خوبی برای آزمون سامانه‌های جدید خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/683371" target="_blank">📅 18:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683370">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
نایب‌رئیس شورای سیاسی حزب‌الله: انصارالله آماده است در صورت محاصره حزب‌الله و لبنان، باب‌المندب را ببندد و «کلید» این تنگه را در اختیار مقاومت قرار دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/akhbarefori/683370" target="_blank">📅 18:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683369">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de26de11a.mp4?token=CTwtaf6tUayBxHJl5pjQx3gCE8zTMtvFX7CrDH1i395t4dPrVFzdQwyFpuLgoFefvH4DIMguATno8XPvNEsPQPZXHROhCI7cRfCGu0LdMI6ZGZpWHnvE7gn1wuvZBZDPfztFq8CgMYHebSESgS5JRx3yRKNuxcUs4lXAQeGLoGOV95oEAq0xu-lJqFqIhMJxbgmSe5Ne90W-59XNNGr-onxji4H4OqeC7kcjxtrNLPnkER8Du9CULH8LpyXIuHIWaK1MPVWkKPUkpfGMLWmIbf-p_qjhX1y629XhHwwQq44LLxYFuWpA72RHpe7fBsfUyoKel05oP1jrYYvCm1T7DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de26de11a.mp4?token=CTwtaf6tUayBxHJl5pjQx3gCE8zTMtvFX7CrDH1i395t4dPrVFzdQwyFpuLgoFefvH4DIMguATno8XPvNEsPQPZXHROhCI7cRfCGu0LdMI6ZGZpWHnvE7gn1wuvZBZDPfztFq8CgMYHebSESgS5JRx3yRKNuxcUs4lXAQeGLoGOV95oEAq0xu-lJqFqIhMJxbgmSe5Ne90W-59XNNGr-onxji4H4OqeC7kcjxtrNLPnkER8Du9CULH8LpyXIuHIWaK1MPVWkKPUkpfGMLWmIbf-p_qjhX1y629XhHwwQq44LLxYFuWpA72RHpe7fBsfUyoKel05oP1jrYYvCm1T7DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش باران تابستانی در بخش احمدیِ هرمزگان
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/akhbarefori/683369" target="_blank">📅 18:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683368">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
نخستین تصاویر از پشت صحنه تمرین «سیاوش»
🔹
همزمان با ادامه تمرین‌های کنسرت‌ نمایش «سیاوش»، نخستین تصاویر از پشت صحنه این پروژه منتشر شد؛ روایتی تازه از یکی از ماندگارترین داستان‌های شاهنامه.
🔹
«سیاوش» به کارگردانی حسین پارسایی، تهیه‌کنندگی سید محمود شبیری و جلیل کیا و بر اساس طرحی از متین ایزدی، با سرمایه بخش خصوصی در حال آماده‌سازی است.
🔹
زمان و مکان اجرا و سایت رسمی بلیت‌فروشی، به‌زودی اعلام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/683368" target="_blank">📅 18:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683367">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: عبورهای شبانه و «چراغ‌ خاموش» از تنگه هرمز با اسکورت
🔹
شرکت‌های نفتی عربستان، کویت، قطر و امارات، فرستنده‌های نفتکش‌ها را خاموش و نفت را از تنگه به دریای عمان منتقل می‌کنند؛ آنجا نفت خام خود را به نفتکش‌های مشتریان تحویل می‌دهند./ انتخاب…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/683367" target="_blank">📅 18:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683366">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7ADejpwpCjK6ys_UJjmUXtoWRYOoK5POdvN4-x4XZ0SJqzMWsLIyGPeVq1EnVm_CVQrJE7fleu5Jt1V6ISH5G_iDJWucE72I_fJJkMAMV7nlHsw4CdBCGoPFuQPuAsZ7YxqscTplv9sOghteRoI7y8mR6ujPKd-pFafUrYNwsXBz7vD8AF6X9sRsiub9kHEv5COo2xkq3erIcS0_4pct8pA6bQowYXf3OH0pkCxoTpIQqMC67rP9OLLBuS6eaMrFNV5vU5C3Zu_XHXZGB0JS10hycoSvWP4eaCgIyDHEGet7h1PnjI4qHcNA1MMrc10EaV2yIF3jiN_JxLfPfnANg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عملیات ناکام در قلب نیویورک؛ زنی که می‌خواست کنگره آمریکا را منفجر کند | جسیکا بویی کیست؟
🔹
مقام‌های فدرال ایالات متحده می‌گویند پیش از آنکه یک طرح حمله تروریستی به ساختمان کنگره ایالت نیویورک عملیاتی شود، عامل آن را بازداشت کرده‌اند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3239506</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/683366" target="_blank">📅 18:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683365">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15d39b2e72.mp4?token=VYBkvEnDh7UecO6ozAFhzEE0cxB8fdocmzW3E_-c5xBLMHjw8ZkHXhnjdMxscfL2yVkuALgOf41sIvThHWaOz37bL_Idq6lKhivJk-Y2MBfNGpYPGR-8i_yzkizeCtURGB2L_UuFP2Xodsj4TwVZUZ1ojSb9jG0ClGY2QVihGsR2FuKznrx3QdEi-aBXV8ddB7yPQvQ8KSQrCoTlpgTSgXvATRSz4AO6PW8bC1vvWSmA9vTagMhpXGyteI1Mnav30JsWS9d0-OIrh6S9-s47ieaJIroyS_BvKp3HCBCTh3LirMQ7kRt7Iu5QlWRO2n3mFWvLdCOQOurd72iZvO2YGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15d39b2e72.mp4?token=VYBkvEnDh7UecO6ozAFhzEE0cxB8fdocmzW3E_-c5xBLMHjw8ZkHXhnjdMxscfL2yVkuALgOf41sIvThHWaOz37bL_Idq6lKhivJk-Y2MBfNGpYPGR-8i_yzkizeCtURGB2L_UuFP2Xodsj4TwVZUZ1ojSb9jG0ClGY2QVihGsR2FuKznrx3QdEi-aBXV8ddB7yPQvQ8KSQrCoTlpgTSgXvATRSz4AO6PW8bC1vvWSmA9vTagMhpXGyteI1Mnav30JsWS9d0-OIrh6S9-s47ieaJIroyS_BvKp3HCBCTh3LirMQ7kRt7Iu5QlWRO2n3mFWvLdCOQOurd72iZvO2YGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ربات انسان‌نما از چین، رکورد اوسین بولت را شکست
🔹
این ربات، مسافت ۱۰۰ متر را در ۹/۳۲ ثانیه طی کرد و حداکثر سرعت آن ۱۴/۵ متر بر ثانیه است.
🔹
بهترین رکورد بولت از سال ۲۰۰۹ با ۹/۵۸ ثانیه ثبت شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/683365" target="_blank">📅 18:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683364">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: عبورهای شبانه و «چراغ‌ خاموش» از تنگه هرمز با اسکورت
🔹
شرکت‌های نفتی عربستان، کویت، قطر و امارات، فرستنده‌های نفتکش‌ها را خاموش و نفت را از تنگه به دریای عمان منتقل می‌کنند؛ آنجا نفت خام خود را به نفتکش‌های مشتریان تحویل می‌دهند./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/683364" target="_blank">📅 18:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683363">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس مرکز امور زنان و خانواده وزارت کشور: بعضی‌ها تصور می‌کنند زنان واجب نیست سرکار بروند ولی امروز اگر زنان در کنار مردان کار نکنند، نمی‌توانند هزینه زندگی را تامین کنند
پروین داد اندیش، مشاور وزیر و رییس مرکز امور زنان و خانواده وزارت کشور در
#گفتگو
با خبرفوری:
🔹
قانون حجاب خیلی در جامعه چالش برانگیز شد. به نظرم نقش دختران جوان در پیشرفت کشور نادیده گرفته شده است.
🔹
اوایل انقلاب همه وزارتخانه‌ها و کارخانه‌ها موظف شدند مهدکودک داشته باشند، اما دولت آقای احمدی‌نژاد مهدکودک‌ها را جمع کرد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/683363" target="_blank">📅 18:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683362">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
توضیحات مدیر روس‌اتم درباره وضعیت جدید نیروگاه بوشهر
مدیرعامل شرکت دولتی روس‌اتم:
🔹
بازگشت پرسنل به نیروگاه هسته‌ای بوشهر طبق برنامه پیش می‌رود و در حال حاضر ۴۲ نفر در آنجا داریم
🔹
روس‌اتم قصد دارد تعداد کارگران سایت ساخت نیروگاه هسته‌ای بوشهر در ایران را در روزهای آینده به ۱۰۰ نفر افزایش دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/683362" target="_blank">📅 18:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683358">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLUSK6Ol7MJOlc90JBR1w1PfxUKO8h2-OUEMVKyGbuca3Ip3KsCBYvsR2iSGtmNOVyrp9vG2DDZ08uUoxprWY7bMDdYDs_m-GFAIyAyMNIS1ooNl0lShQR-2eud_Fl-DRCKE7J6fDjghJ8i2XUYjaKA-0YZjP4FNFz5kCaEx5nNZIu7uAUC3l5ZOOjSyeGKl-osQSqR3GIymsD3nbLfQWOk04T_59_J3fwu0Tx9tSa-AqyFN950UpBeVTgzWGeOJ-BHQQh6F4MoGSSZWHdUTneuJG_iHy_ZRu1X2a6E314jce6mrzklQzx0IXqZWHSGZFzD6x3ERjbZr0e5lqD8LZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsVDxJLlUUoqr7J2OcQPLmGwkDd6Ogjt5vqSKQnWFPm1HIBqlSR3Q0oBDJcFrrnBsLZJv_c9FKPRctomIpl4WC74OJpPOPbHFUD_IpkQyMwTvHEWaPtaobhIl8W3vMpfL0Z57PX0NcvrVYSO8lcYXfIYneUM2BuwMLau3zcOMy6FjMEzCB50k0y4gxV1dym6odZgNh6Dql4zxjN-m30N17hRALnCx2VVpnO0lxFlSdMNLg1valaOjLwVWkqN8f3-O55hK0tkLWT3iSiSidshhsyZ4PFu82KLEi-Af_ZDU06xEfQyYaz2Ie-yS4GJrCj4IpJc1LNIHlTS2Ss_tI_AaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/im29p1kvohBs6SiNJ5uRjBO8u_doOAo4UWLtqU3yHUpIqCHXz5qog1aaSmrFE0UhH6lZmbsLgKcGg6OmbqZy83jcd2qW5tCojAHs9iXf7GW3VpmJtZZmihJQdxFYfgtCNzl3-KAYo18kF8sIuzee3lygTeDsJG3LdGvWk-DULIMVZHD94HGEyjhzBg6wfSk-RhocRdLoYArF5p6JCktSoFiu-eKmuh7lY4mdc8l7BuAA0f8xt7R9M_BQ_T57uAgJ-aC_CFD05SXr82wEb0qHr4mGtowYmifp1rFLCBrvn1_bxBC-kM-2lfvW6qlMQttppYs0VbwTxxc9ZKvepTIqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CkrJrA5_nIKIf5FeO_fuVQva1HKw1bBkzz-f8etrS3hl_zzbWY8kWASgZvHHZopm_aN4E0FKVXsqs3TB1Bd_ccNFaNcd7R2knJ-mPaSRE5SxiKJzKxFNx1aYVqlFgPnMmX8bYDLGYLEpJq9Vn3riJ5obINiunH2HYXWS_UXY0R_z1i9Jj-7TYZ7Pr5OAu4al3__v-PE0dZ9-uCKPtPl7twRwyG7CYKwBmigEOB6529m3WmmxSOcF1sbr9FkaMHXSs9IjM67y_oESZ0FGwWOwc2gMmiyW4iKCmdf-EdiXLACdO3lopD0CIhQpsXS99aOci1___ALYa0mhs7bjt542pQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۲۶ جمله کاربردی زبان انگلیسی که مطمئنا به کارتون میاد
#زبان_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/683358" target="_blank">📅 18:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683356">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPbh6lGCk0YKWLQ-0fd8IJGU1fN1cnhb2h9l0lnXlNk-ourudqA4izdP04eXNBarMac6V33voh3Zyv3OaUXRN2UizaIjieMIlt3S1WT5wYQzNaCsqp4UTPkrC3z3Ni-aySY6BG6xpf2GG8-98_5zuhwWCrSYbnePnvjV5QJ5hTW7zmAuZbsgYogS2fEJrjOQzjTdb7Gw_XI-HDE-BXRTfCMvxNjgk98eMmb5Fa-r1TCPhCG__zGgo0gNsl87ZXW-9VOKcHjKRGl8FxOZGtianxlkRWUC5C12WH9Y789tD__KjpoXjWMiKAmIKLLccKG-FC4lIjyZqZqp9zEmkp1w5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قرارداد بازسازی نیروگاه‌های فجر انرژی خلیج فارس با مشارکت مپنا به امضا رسید؛ تأکید بر تسریع بازسازی با رعایت الزامات فنی و نظارتی
🔹
سید محمد احمدزاده، مدیرعامل فجر انرژی، در آیین امضای قرارداد مشارکت مپنا گفت: هدف اصلی پروژه سرعت است و در گام نخست، بازسازی، نصب، راه‌اندازی و تحویل چهار واحد گازی با حداکثر استفاده از تجهیزات موجود در دستور کار قرار دارد.
🔹
وی افزود: در صورت توافق دو طرف، استفاده از تجهیزات نو یا احداث و جایگزینی واحدهای جدید نیز پیش‌بینی می‌شود تا بخشی از ظرفیت در شش ماه نخست سریع‌تر در اختیار مجموعه قرار گیرد. همچنین تجهیزات مازاد مانند ژنراتورها و سیستم‌های کنترل می‌تواند در سایر واحدها و سایت‌ها استفاده شود.
🔹
احمدزاده بر بررسی ظرفیت‌های موجود و زیرساخت‌هایی مانند خطوط گاز، شبکه برق و تأسیسات تأکید کرد و گفت اجرای پروژه باید با سرعت و سلامت فنی پیش برود.
🔹
وی نقش MC را نظارتی و حمایتی دانست و بر نظارت آن بر حسن اجرای کار و رعایت الزامات فنی تأکید کرد.
https://fepg.ir/fa/news/1135/
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/683356" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683355">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d10c8f321.mp4?token=ekDUhh4RKRFyosAGAfs4Gf5jPR1ia-2TOlKOAgPVwSyfQx9oSjoFFuPyUKQ1Mgb2cXfS3Fjf7_puuMv23LGLyNR6xSqk9hja5A1ESrV-NtesdJAoaN69Xg8CQ193LYZYulwZRic_xaDV1Csl8opkilwmG3_MjNaVRZw_8MW-VvOofby4E-ODceUaRJ3FLLrVwbCqWFH8PIrEEUVKCCEeWQwkhzXCM1QBjBdFVouGhBY4Iim571PAXl2wbvUtcxTR_ope9CIClhd3AB8-YMbjFxrMLCidQ8GoOqu_RnoXzENLykIPIhu-LQ43V4b9D88lHQKrqUTqahCNjBGZk67EJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d10c8f321.mp4?token=ekDUhh4RKRFyosAGAfs4Gf5jPR1ia-2TOlKOAgPVwSyfQx9oSjoFFuPyUKQ1Mgb2cXfS3Fjf7_puuMv23LGLyNR6xSqk9hja5A1ESrV-NtesdJAoaN69Xg8CQ193LYZYulwZRic_xaDV1Csl8opkilwmG3_MjNaVRZw_8MW-VvOofby4E-ODceUaRJ3FLLrVwbCqWFH8PIrEEUVKCCEeWQwkhzXCM1QBjBdFVouGhBY4Iim571PAXl2wbvUtcxTR_ope9CIClhd3AB8-YMbjFxrMLCidQ8GoOqu_RnoXzENLykIPIhu-LQ43V4b9D88lHQKrqUTqahCNjBGZk67EJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پژوهشگر مسائل آمریکا: تهدیدهای ترامپ علیه متحدانش، از کره‌جنوبی و امارات تا عمان، موجی از انتقادها را در داخل آمریکا به‌دنبال داشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/683355" target="_blank">📅 17:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683354">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نتایج پذیرش دکتری بدون آزمون دانشگاه آزاد اعلام شد
🔹
سرپرست وزارت دفاع: ایران هرگز تسلیم فشار نمی‌شود
🔹
ماکرون: اوکراین را به موشک‌های رهگیر تجهیز خواهیم کرد
🔹
حکومت جولانی حمله پهپادی رژیم صهیونیستی به حومه دمشق را تائید کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/683354" target="_blank">📅 17:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683353">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04a66453f.mp4?token=Um3vmq2xpwFTprgw-7gvu9Xt-W87W0kHgvzEDJkfYlFqCstzekRuWbubK5mOUvyZtTFt37thMpnVtndqYMfbcZFHHiRZM7FBvImfpylonIodXLdH9Le2QRAWhpw3m81YTYbSaJ4FYNk1J3TnIqzXda6FqiVZ66bc0jdhA2GDNJot_wWcjRzy6Rqah2Y11odxGF6iCfOKMjs_I6MnP7xe6tQqc1PcAM5CqjTUYd4p4thLyHyaPwM8AkmVYS_RyLoXEPj1_Egce-RcKaHCGTFTIeFsh4Kkb8q0-G7DiwDrNyGR6zyzNjPPZ1PQOBij9TVwhYw6ygRW_JpALZuj5Fik1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04a66453f.mp4?token=Um3vmq2xpwFTprgw-7gvu9Xt-W87W0kHgvzEDJkfYlFqCstzekRuWbubK5mOUvyZtTFt37thMpnVtndqYMfbcZFHHiRZM7FBvImfpylonIodXLdH9Le2QRAWhpw3m81YTYbSaJ4FYNk1J3TnIqzXda6FqiVZ66bc0jdhA2GDNJot_wWcjRzy6Rqah2Y11odxGF6iCfOKMjs_I6MnP7xe6tQqc1PcAM5CqjTUYd4p4thLyHyaPwM8AkmVYS_RyLoXEPj1_Egce-RcKaHCGTFTIeFsh4Kkb8q0-G7DiwDrNyGR6zyzNjPPZ1PQOBij9TVwhYw6ygRW_JpALZuj5Fik1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت ۸ نفر از عوامل نزاع و درگیری در سعادت‌آباد تهران
🔹
در پی انتشار ویدیویی در فضای مجازی مبنی بر وقوع یک نزاع و درگیری میان ۲ گروه در منطقه سعادت‌آباد تهران، دستور قضایی جهت رسیدگی به این موضوع صادر شد. افراد حاضر در این درگیری اغلب از اتباع خارجی بوده‌اند که با صدور دستورات قضایی، شناسایی شدند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/683353" target="_blank">📅 17:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683352">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
عجیب اما واقعی؛ سونامی تعرض جنسی در ارتش آمریکا؛ ۲۰۴۹۲ قربانی در یک سال
🔹
گزارش وزارت جنگ آمریکا نشان می‌دهد در یک سال منتهی به نظرسنجی سال مالی ۲۰۲۵، حدود ۲۰ هزار و ۴۹۲ نیروی نظامی فعال، شامل ۹ هزار و ۸۶۰ زن و ۱۰ هزار و ۳۲ مرد، مورد تعرض جنسی قرار گرفته‌اند.
🔹
در میان زنان نظامی، تفنگداران دریایی با ۶.۸ درصد، بالاترین میزان تعرض جنسی را داشته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/683352" target="_blank">📅 17:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683351">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKbcoSpa8QB3-dHB1AEnmHz336FBIVUDSbKCpgnwuTGNHoVQPyDsBblmKep6bzlEHFjIZ0goMJRkgiE_qKoWjrI95Z7uPQnN7SiLMUWZOPUhxPUz1b79A1Me1vxz9GGzOkYEn55FR_pTTXAyOX3hExA1rm1dJyxGWIkncZPEoN-6CglC9G_CoM7iXvYY1N9xcTK0qLDYU5tLSerqasHQe-pAitNMft7_y8w3fW3WkmNtQqsPp1sMwVDhfOZ536IzsCmRvGLKKtQKXLFXaUjHuYlfRBjHyBWcqtI0hzeWaVH4nlntS779YW2y8kHNoSUc4pZYV3m_mMkfPPqQeW2rMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت خودروی محمدرضا گلزار چقدر است؟ | رژه میلیاردی از میان صفِ گوشت
🔹
تصاویر منتشرشده از یک دستگاه رولزرویس کولینان با تیونینگ منصوری متعلق به محمدرضا گلزار، بار دیگر توجه کاربران شبکه‌های اجتماعی را به خودروهای فوق‌لوکس در ایران جلب کرده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3239571</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/683351" target="_blank">📅 17:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683350">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c60d36b56.mp4?token=OASRF0C1C3ChufIWsVFFPiEZM4PL5C2QsLw7inYd0MRyYOHPF-BGNLC2b_D32QpACuLr87IBT862KRyZn2eDUcDNXAaFOtu1h4OOGPhVuPGqgtAx-Q-bm5NVXN_uUtdesmhHYQp2_W3JoJK8kzJBaIpEQjukzuZLj2bPBUxaBHXNAT8PdKEBjjoY15vT1GL5WCZ7uuUJ94bE-Gg3qw1PPobaaVA091LKHPS3_tyGuZexVQLWHvgehMBzw0fHMtaCkOFZkMvq9mV97lV6dg3tDNhlKF32luk0eyYK1g9PR4uRic_K8v3szt-pYwLWhgI25CEJKXEXRLVLy04mBAk_hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c60d36b56.mp4?token=OASRF0C1C3ChufIWsVFFPiEZM4PL5C2QsLw7inYd0MRyYOHPF-BGNLC2b_D32QpACuLr87IBT862KRyZn2eDUcDNXAaFOtu1h4OOGPhVuPGqgtAx-Q-bm5NVXN_uUtdesmhHYQp2_W3JoJK8kzJBaIpEQjukzuZLj2bPBUxaBHXNAT8PdKEBjjoY15vT1GL5WCZ7uuUJ94bE-Gg3qw1PPobaaVA091LKHPS3_tyGuZexVQLWHvgehMBzw0fHMtaCkOFZkMvq9mV97lV6dg3tDNhlKF32luk0eyYK1g9PR4uRic_K8v3szt-pYwLWhgI25CEJKXEXRLVLy04mBAk_hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع یک انفجار در پالایشگاه دارمان کردستان عراق
🔹
جزئیات بیشتری از علت حادثه و میزان خسارات یا تلفات احتمالی منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/683350" target="_blank">📅 17:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683349">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tb9Epj8HgReRzV8gv3FGPAP467o43-BPXT3HkaFDLODIHnV8SKzHrTBOgiGWQSaG1BUxpXhRU6UtZ1JcmryIebCSIf1o9ITv--L9AgB4hDypk0AxgEUJZyd4Ar4lMgpS5vhMIYfjez4CxvogtXc24stP9hHU_LmVSs_ltpDySFPXvBTvPH8qP6YaCKylqpIk41oj4lD2pDflU0MNOWhkGZSvHs0_9I0J6FZe_1LYnt0mXUY_h2gFPxy4Qsm2zsTZbxVK_pFkMMu5vseHSElY4BtyllglwlM0wotK1hB9FC5jzc1QLiM4GT5yUqclZukrzZRNL_kWCzmQh0oZplO8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ست مردانه نیم زیپ و شلوار مدل EA7
👕
🔥
یک ست اسپرت و خوش‌استایل برای استفاده روزمره که با جنس پلی‌استر، سبک و راحت بوده و برای فعالیت‌های مختلف انتخاب مناسبیه.
✅
جنس: پلی‌استر
✅
مدل: نیم زیپ + شلوار
✅
سایز: فری‌سایز، مناسب L و XL
✅
قد لباس: ۷۲ | عرض سینه: ۵۰ | قد آستین: ۶۰ سانتی‌متر
✅
قد شلوار: ۱۰۰ | فاق: ۳۲ سانتی‌متر
👌
انتخابی راحت و شیک برای استایل اسپرت روزمره
🔴
قیمت 1,198,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/59419/180124/</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/683349" target="_blank">📅 17:27 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683348">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvq1Bwail79mW6_yFwZr7J7CjkjYAMWVrvkKRozr3Hqj7QqrIiiUqEOJejkNSJu6jy-RmyQ5LjQ2L7EzMlLOcjbhfnjiU2J5RlLMlAjvVZNUtGYI4dfcNSH2B-m0F-bdOLPsC6UInv0eiwc9CI26zOZi6rlnULSm-VEDX_H_n1lRJcY9RB9SFAaRpgS55g2NhohcmXcvS2chgrxFNTX386FuGVEvNOAjfdK7o7az73rfzTiJlUaspfhGqKaGBNzGkugnUhqheAcRPFZ5xH8B5BKwrNaT6pp_fdHU2PKjlBnubE_ZA6ppn5GD9iD-36glvDlFl_4gwKqkhVPAQjMdsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری کمتر دیده شده از رهبر معظم انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/683348" target="_blank">📅 17:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683347">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
آسیا تایمز: چین به فشارهای واشنگتن تن نداد؛ شکست پروژه انزوای ایران
رسانه آسیا تایمز با اشاره به تلاش دولت ترامپ برای همراه‌ کردن چین در اعمال فشارهای اقتصادی علیه ایران:
🔹
پکن با سیاست تحریم‌های یکجانبه واشنگتن همراه نشده است. این رویکرد، تلاش آمریکا برای ایجاد انزوای اقتصادی علیه تهران را با چالش جدی مواجه کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/683347" target="_blank">📅 17:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683346">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 در انتخاب پزشک، کدام عامل برای شما مهم‌تر است؟</h4>
<ul>
<li>✓ تخصص پزشک</li>
<li>✓ توصیه دوستان و خانواده</li>
<li>✓ نظرات کاربران در اینترنت</li>
<li>✓ هزینه ویزیت</li>
<li>✓ نزدیکی محل مطب</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/683346" target="_blank">📅 17:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683345">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت کشاورزی: برای برخی صنایع لبنی به‌ دلیل افزایش چندباره قیمت‌ها پرونده تشکیل شده است.
🔹
مدیرعامل شرکت توانیر: پیش‌بینی‌های هواشناسی مبنی بر استمرار شرایط پایداری دمایی تا نیمه شهریورماه است
🔹
منابع خبری از حملات هوایی و توپخانه‌ای رژیم صهیونیستی به جنوب لبنان خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/683345" target="_blank">📅 17:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683344">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای تل‌آویو درباره فرودگاه ابوالظهور سوریه؛ کاتس: ترکیه امنیت اسرائیل را تهدید می‌کرد
یسرائیل کاتس وزیر جنگ رژیم صهیونیستی:
🔹
اطلاعاتی به دست ما رسید مبنی بر اینکه ترکیه قصد دارد اقداماتی را در فرودگاه ابوالظهور انجام دهد که امنیت اسرائیل را تهدید می‌کند.
🔹
اردوغان پس از حمله ما به فرودگاه ابوالظهور در سوریه، مجبور به عقب‌نشینی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/683344" target="_blank">📅 16:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683343">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqRYmGl94sQiIFvsfo8XQVg1AeQX8mK-HQAlDrEW-FNPlJutTg2ZhQo5ekcpIug_PoAAU__N3ERqdOb0T-qvp1AZDLe0hV1DPudo6b1kKgrXcgwbl90CVOP9xrxanMHwsAckilqsFxAyyYLWPJD0tCVpodiMX2ep7LaFy1adW8pcLPC49ToPqfyvS9i9pMeCKyzc1EoCbslOnl8CsttzzxEUuopn41e1dkRgrU5NIEfxFRbnVySpEGIxs4NDAVo-gAo1aNbebJPadaiD7A0JG9iBUyFY6mhpw-w8kMoYQfglJf8k4_uEM7mF1ndOngN1zZmO1AEjczkUbdDCoRfsjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳ دسر خوشمزه با بیسکوییت پتی‌بور
🍰
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/683343" target="_blank">📅 16:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683342">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
دور جدید ثبت‌نام خودروهای وارداتی از فردا
سامانه جامع عرضه خودروهای وارداتی:
🔹
دور جدید ثبت‌نام برای خرید چهار خودرو از فردا (اول شهریور) آغاز خواهد شد. متقاضیان تا روز چهارشنبه (چهارم شهریور) فرصت دارند یکی از حساب‌های خود نزد شعب بانک‌های واجد شرایط اعلامی را به مبلغ ۵۰۰ میلیون تومان مسدود کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/683342" target="_blank">📅 16:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683341">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egFNYLxmM7reSijOFukqvNRNo_4V6znV0ar5EywgFrVQUXHRzeeXlXedCqNkutWjqTXOzInUuUS_sY0LOw2mZkT_pvsErlzNKw8w77nV2M3QquQnLwPv5zZDD_MB3dSMtf5pzQFm3Klp9w_ik4WglmiE5Hker_mx5ayUWjYDiRzYPGejHjuELjI1rrrz6yz7ghVrj8wyeiS8SYcgpz055z8jUgTu6v-IwFzvdOkvQ_VzO_MxlMc4EcW8wwMgagrje81y6rX-zI7FsSSDxEHD4uM8wK-hzjix0U8tr3agxp8G2gA_w1bw6HZPn0qF3b5EnvUhRnpRlZuc5yWoLqh5LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده کل سپاه پاسداران با ارسال تقدیرنامه‌ای به رئیس سازمان صداوسیما، با اشاره به اهمیت روایت صادقانه و هوشمندانه از واقعیت‌های میدان در کنار حماسه‌آفرینی‌های رزمندگان، از تلاش‌های مدیران و کارکنان رسانه ملی در پاسداری از حقیقت و تقویت جبهه انقلاب اسلامی قدردانی کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/683341" target="_blank">📅 16:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683340">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c8514529.mp4?token=qlh17eGXUMr1qDFfEWoE2TTHdRywAXZ6jy6g9hQCFrj_3E8S6EDJeHP0YZomWjaEnWi4z8nXRplZdBZbdC2lbPjGwq_kGZA8j90u-PI_ciD3YyK1QHKndcH-Robd-unFHUNjiFusSZ0d0jBJJaSlhUyGEFhf2EyFcgi-dckIP-nmm-Afe5O2fTGJ7ABLzRSvSLH_CmfZmfnCJOn6Pz3Kai27F82WZRAVgYs3t_gGzvZN2p8YTlb--YYpREZxnp9o4uZF3v49FZEPB_BN7EUKvUSTeycxsDKcIoWK-rqzWASpke4PD_Q539BteSOKw-SXurdcN9RMESGNfFQvGMHh7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c8514529.mp4?token=qlh17eGXUMr1qDFfEWoE2TTHdRywAXZ6jy6g9hQCFrj_3E8S6EDJeHP0YZomWjaEnWi4z8nXRplZdBZbdC2lbPjGwq_kGZA8j90u-PI_ciD3YyK1QHKndcH-Robd-unFHUNjiFusSZ0d0jBJJaSlhUyGEFhf2EyFcgi-dckIP-nmm-Afe5O2fTGJ7ABLzRSvSLH_CmfZmfnCJOn6Pz3Kai27F82WZRAVgYs3t_gGzvZN2p8YTlb--YYpREZxnp9o4uZF3v49FZEPB_BN7EUKvUSTeycxsDKcIoWK-rqzWASpke4PD_Q539BteSOKw-SXurdcN9RMESGNfFQvGMHh7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از مخازن سوخت ابوظبی؛ امارات برای حفاظت از مخازن سوخت در برابر پهپادهای ایرانی به حصارهای فلزی بزرگ متوسل شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/683340" target="_blank">📅 16:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683339">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deXwgvHxXbqg7-bplJlWL9IT2K-dOvLyj5LqdLLidmAKZvW-oxoHXZ-H9SkfmWPxNIGbh0_HPMR3lGV0I3VhGYBLULAYcqlBK0fNTb7Y-nta5nayUG5bo7oQc3fOa1wHYWsdbzH4zaRJ2AT1xFCTbn6HLjtH1gajWMBQPzR7SUBR38jiDGriARKKgDjJ4AegsZYmgf0rDjyjZznr6WMQg_sBAFP74m9FQElDeoCb8RfNz0cxstaSOnh6wokyINtycrJZAvcHuv9WPMgX1_JZNw7VU6zFqYi_GtpybAYccChdvcMhglGzHvGnkxXGzeIoJpItkmRWf8OOxezr6ZLjNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
مراسم تجدید بیعت با امام زمان (عج)
✨
🤍
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ «مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام: حجت‌الاسلام و المسلمین حیدری کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی : احمد بابایی
▫️
با حضور:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای : امیر مهدی باقری
📍
وعده ما: شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/683339" target="_blank">📅 16:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683338">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی وزارت دفاع: ارتقای موشک‌های بالستیک و کروز ادامه دارد.
🔹
یک بالگرد در ترکیه سقوط کرد.
🔹
۱۸ قبضه سلاح غیرمجاز در زاهدان کشف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/683338" target="_blank">📅 16:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683337">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMuNZZ06lUOGKP_m3FcDZGC4umZ9mOqWvNwUvhQB7PHrXWvpqQUaZAgpmjtf0EV8niv5HF6Cr-dmzZMFfGra5vgBzzE-SmT0yJtf7ySs0hNza0ZeimFTlSSKELlxaY43d3tu9r-ILXqoxiwciLM-Y3TG5elipOu-d7MVpm-VRTosRGn97RZNU42q_I6NjgxuTXAgj-lbjJSnqCA-u2apc9A8l3WHjn9CzLJOIJ0GKqS6gPLlGtpZJ8bxRb51kkBCNxvBKotxCok1xMp-xS2Eid4HmTgTb8K5LNbOomRiXgJDN_SyAcVTN72oZHQph0y69MzzigRURAgg-VMxWCgZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زین الدین زیدان رسما سرمربی تیم ملی فرانسه شد
🔹
با اعلام فدراسیون فوتبال فرانسه، زین‌الدین زیدان تا سال ۲٠۳٠ سرمربی تیم ملی این کشور شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/683337" target="_blank">📅 16:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683336">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس مرکز امور زنان و خانواده وزارت کشور: دختران جوان می‌گفتند شما کار و اشتغال ما را درست کنید، حجاب اصلا مسئله ما نیست
پروین داد اندیش، مشاور وزیر و رییس مرکز امور زنان و خانواده وزارت کشور در
#گفتگو
با خبرفوری:
🔹
در بحث حجاب ما با برخوردهای نادرستی که کردیم، زنان را به این مرحله رساندیم.
🔹
برنامه ریزی اشتغال ما مسائل و مطالبات زنان  را اصولی نگاه نکرده است و همیشه در حاشیه به اشتغال کلان پیوست زده است.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/683336" target="_blank">📅 16:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683334">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
راز خوشبختی من  خفته در قلب من است تو کجا می‌گردی  قلب من این وطن است
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/683334" target="_blank">📅 15:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683332">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
استفاده نیم درصدی از متانول در ترکیب بنزین  سخنگوی کمیسیون انرژی مجلس:
🔹
میزان متانول استفاده شده در ترکیب بنزین اکنون حدود نیم درصد است که این میزان مشکلی برای خودروها ایجاد نمی‌کند.
🔹
بر اساس استاندار جهانی تا ۳ درصد حجم بنزین می‌توان از متانول استفاده کرد./…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/683332" target="_blank">📅 15:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683330">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RzFqGXg7OjEn8VwI0ULkEn3ztwJxWu5M0_XznFHIy9g7LzQBfPJsnLdGeNnTQxZgS3gVMT9O9oU3iXK8Ty8Z7x4MqMY3XTe2oEDAvVTIdRl4Wigf8jzBqOJVh8LK2R92Ewwuru9dFq7vjehXvTHUXHj1JaOJeYeCrryZkzDtenNur3Ruix8Sd0b10TLqC-V_Jw3pI-QJhT63yDoIxjXSYsNjQRuShb3ad6PEL-XYHnTTUQXzNxFfw3HToq7sTqsPT0jh7NYGpnLaxiLz_yrSIftkrwax-yrnqm7rEwERf-XwBwlYXvJM6BnLMZ1oxwdsoIQOasRzbzLmW8i2UbehtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_mm5jcMGPtE7kQPZ_fvXNejOfPyIRP-JI0fI29YeHEmAJoHHqkzz_Kw9AfagMC99a56jPyM-ZoR5TMLCQsQXh214H9n_hWubMLtf37ZrzfonNdgBIA-GuoYpEC2gAfNlkejZjXG_zjLpNPHowFmQe9js-6S0aC-1iQKV94-bXPDdt4l-YjzgoDQBgOJScPYBZ_tfJHzOii4Co7TukQCzTi8LkIgixwjZz-zeO1ffbTrYwgvLZW2MYtcB3kYB2FLSiGSEGYO4KKT5aY9lEdUl5Px_sj3MMaPUkELGwddtxDTZAh_nYqoRMFPe_TSpf2g6j4fRMBNL8QikXhi6jKXPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاخص برابری جنسیتی ثبت‌نام در مقطع ابتدایی
🔹
بررسی آمارهای یونسکو نشان می‌دهد کشورهایی مانند ایران، آلمان، ژاپن و آمریکا با ثبت عدد ۱، به برابری کامل در نسبت ثبت‌نام دختران و پسران در مقطع ابتدایی دست یافته‌اند.
🔹
در این میان، کشورهایی مثل سوئد با عدد ۱.۰۷ و چین با ۱.۰۲  نسبت بیشتری از حضور دختران را ثبت کرده‌اند؛ این شاخص در کشورهایی مانند سورینام با عدد ۰.۲۵ و پاکستان با عدد ۰.۸۷، به نفع پسران است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/683330" target="_blank">📅 15:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683328">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dBDVGwYtuOvzjRF36rlwPijHnEvabB7SMfbIlkV1zQoWP28K6i4zRp0fgFouYnNrI5qnr1UKIcPFSrqRIspLRcTMZdjkyrDhUpRQAAtgsWUhpBglgsuSM35SG0of7xf98G_VOEFZ39BcSNDpmlsHuvJTGF-fXSrDCHzjtCjXXPAqJ2KYCfWJWhMIWTKzDJ_anqx1YK2hMMx0LmwyAY0rpw9B8Y7Z64H9aqP2hzkvCM09WwougGpEkQuBR6H6qepKxqn1P5oXtD3DJ-kP-In6SJzCDL9IGLy0zjmexrMMAcah65YlUhCATb3tD24EPPMHEn7eo3L9A5YrXlW20uGzkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYyLGfANBtyfNL2Wh4emcK_2ramNoWMXAXBxcB0p5tBc7EzMe30ui4i79vu_20pNtOKfFrUvRocjzc1BSwjEpyaLdf1dRylkKmkEm16vparu9Ml-VH-st12lr1YMNWz2jtK5yI9E8o3X2_-eHJkPl8P6UaPSbzbUqQ1V1GxrSGsGVqV5khsTqNUubCATSaHdnVePqEum0hOooNngBel2pN4fr14GtoopxIwB_w47hg_Hho2hI82HaCuXAsK1Lst3FNlvNUUNCk0Gjem1UlFV22XfnME9fGjygUgSrQmSx78zCCk5txg5Q4zeuOYbjTXE7Nzht7HFRlUUmc1bHVTEsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مهدی طارمی با عقد قراردادی رسمی به الوصل پیوست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/683328" target="_blank">📅 15:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683326">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJXpnKky_8wOO65OTPdRcP-UPJExvIGYVDMCusIzDExXJU4HrQ-RgLxIgBrmAvHcAzibI5unnmPiiPaYmZmv4SgCHBNXcE9_AL2Xdkfpqwb4Jq77Xe75diLXCkWxq_zLB_-twytj1jOsX5WjnMNur8Qffq8QrH7v0HqOYClm_4Ehrgn9sF9r7LyC1tp50Eo1SFIom_wxdR1PoSQAI3yYFzT8yrhU1dlCMQSbeF3G3g3ZsnqADwPFSPWLwX39XDAVc3iEc9r_6bebROOy3mS2NBYy61FLJYAqkXew9By2sngWxTjDojQunaXSAIB7o2kdMfmcL6BO6bToe-4O191zUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🏸
شروع روز با انرژی و حفظ سلامتی
ورزشی
|
#ورزش_صبحگاهی
| ساعت ۸
🍱
انواع دستورهای خوشمزه
آشپزی
|
#آشپزی
| ساعت ۱۰
🧠
سبک زندگی بهتر و ذهن آرام
روانشناسی
|
#سلامت_روان
| ساعت ۱۲
✂️
آموزش داشتن استایل خوب و مناسب
فوری استایل
|
#فوری_استایل
| ساعت ۱۴
🔍
کشف نکات جالب و پنهان در زندگی روزمره
|
#حواست_هست
| ساعت ۱۵
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
🔤
آموزش کوتاه و کاربردی زبان انگلیسی
|
#زبان_فوری
| ساعت ۱۸
💡
معرفی انواع ترفندهای کاربردی
|
#ترفند_فوری
| ساعت ۲۰
🧠
آموزش‌های کاربردی هوش مصنوعی
|
#هوش_فوری
| ساعت ۲۱
🔸
نهج‌البلاغه
|
#نهج‌_البلاغه_بخوانیم
| ساعت ۲۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/683326" target="_blank">📅 15:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683323">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhIWRbEN3AeFwLT0jLT9sdy5l0co7j3V4BJJzlVdkMAgoxIjDRl3fxM_6d0_4rln3SiRPNo6Hmv3H4p6gSIV1cZou7rH98uSxevwx5iOVZxIhdxmxnsc5tPIZkn4BCXnEJxSnc-9KtW_w8Fq4Qg13DMge88TTySAy1EZes8ln7UPZ-jRMdXYwen1ar4X7WqnL-JG15OMacbfYnJy12qLh9grbga8lHxNWu-WYiyOSM3SLrlIpnworqVtYjm9SoI2V8gDLBygGtR1SGt4mRIazxFr0zVsUHlAlJS_o4hcpm69rQTPuGZ_EBpHClSG1tZDTvy_Na5Av-DxM3mTPQrN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDqIY9JHHDVWC8RAIjEpslyROx4uXdetq7Czp-6_A5lTtlKJOfjuIn5wiS4Mm2b8yhVnusteKv_QEFfuusY_FHu0B28A0NsTS-WoHTsvUOYo983CtWtm9JqDQS8_3iiwRbceYOpagASf_4JuIedJpxDyJuY04sY74hz_hAxCKjUzQfUBccxyGd9wDsDLsfHo_ULMQvIL6NDckM5QBXMHOL-mayqu2Fgdi_gUkWs0t5W3Z9mpf0SEokUFysEHMP-DAxxGhtzSLmfDA839B_3zuqBJKG_evpFaebtx7-7R4BoVBBfhpRcpnZAR74rTQ0HXt0aN5i1yX6o5FOrEab87qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaO672Be93fZpBz52XJD__Y4ZV20UkYKliAGlFsPAR1yzqlDcKD9SmAzTZyMdd179ZimgEajX_xItB_Qcg8UTYow58roVvyjhfSdFYL-GkN0WQeltW_fu_BTyjQNmhw-mb6Hk1fx1HutM8cXhMYdPwKMhQdeEYGjHwwsJ0U3Dcj7xGWGcwsCrFZGQzuvE6FTSGVDtMK84l-7VSMU8lFMcs7-mdVllQyFw5nqM0XFBfr2eB0IQHiLgxmKD4zZenrehq3kaM2uBgughwi2Ik2FKAVl32onWlV1nHZCtuz6FJqghyfnRMfc1GUgo6e5ce9SkomkuCNZ4OPv8XigZsYc7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
علیرضا افتخاری تصادف کرد؛ بهبود اوضاع عمومی و ترخیص از بیمارستان
🔹
علیرضا افتخاری، خواننده موسیقی ایرانی، در مسیر اصفهان به تهران بر اثر برخورد با یک کامیون دچار تصادف شدید شد و پس از انتقال به بیمارستان، بدون آسیب جدی مرخص شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/683323" target="_blank">📅 15:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683322">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
سی‌ان‌ان: تنگه هرمز تقریبا بسته است، مگر با مجوز ایران
سی‌ان‌ان:
🔹
تنگه هرمز همچنان تا حد زیادی مسدود است و ایران به برخی کشورها از جمله عراق، چین، هند و پاکستان برای عبور کشتی‌هایشان مجوز داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/683322" target="_blank">📅 15:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683321">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f3c2e988.mp4?token=hMghut6f8sYq7Yf0FVtXmMdHW4Z7BTWBQi6TZs03fhj2vWhIO7-x8t90XdpGHaBNUD3WHwD_V7rAVPry5XLDk6rsvLmt7bfoSUymRNr9Pv12iNaDCNS4ldJxGIoniXNp4W6qL0P1Oo-WDY5yUg293wUXyvv5VyQFKU1eDbUL_Y8XF40Fs1ZRpL2Emlp3Zf0T8X5yU_H04GDTx57undD5_XinSSJE_KVQLG_QZvP6_pdh5yzfrzfTtid-zxkFAi67o0cDP-Sz3w1haeEcq_RPaIxRBlmcEb6eB8Yzxpijmm1J0wtGwCjfTKn0isDQu3qHsGj2Kr4ucTmJ4QV0CE3-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f3c2e988.mp4?token=hMghut6f8sYq7Yf0FVtXmMdHW4Z7BTWBQi6TZs03fhj2vWhIO7-x8t90XdpGHaBNUD3WHwD_V7rAVPry5XLDk6rsvLmt7bfoSUymRNr9Pv12iNaDCNS4ldJxGIoniXNp4W6qL0P1Oo-WDY5yUg293wUXyvv5VyQFKU1eDbUL_Y8XF40Fs1ZRpL2Emlp3Zf0T8X5yU_H04GDTx57undD5_XinSSJE_KVQLG_QZvP6_pdh5yzfrzfTtid-zxkFAi67o0cDP-Sz3w1haeEcq_RPaIxRBlmcEb6eB8Yzxpijmm1J0wtGwCjfTKn0isDQu3qHsGj2Kr4ucTmJ4QV0CE3-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینفوگرافی کاربردی از فرآیند تقطیر جزئی نفت خام و جداسازی فرآورده‌های نفتی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/683321" target="_blank">📅 15:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683320">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822a804c37.mp4?token=ds8Up_zHRyvQy8VheIES_how9iB3qyZCjzLW1wRsqD-mltPuxMn6Dyfcoa8E4dzdEicG8PGnybvRa_5XE-ePkD-AGq7ZVlzF-ugk2oQ68pxR4QzLhRkYdXSfWSVntqIBCA5M3ILQiypPSOIux0jwVqo4j9Zbyqus2fvypbYdH3Skz_iizJjOOtETjZSg98s8guGxZjxkovcPGaJjsdhi2gUjnhe_200yS9kMx4hXIGbfJCgBNVPlXY_qDGVTwoGVIeE7InOj7AJXzub0em-JYO-jLu-T53eseIvynvTp30Xx4koICR5oH_STstRElTMlibh-fJ0y8ZjH454-t04oZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822a804c37.mp4?token=ds8Up_zHRyvQy8VheIES_how9iB3qyZCjzLW1wRsqD-mltPuxMn6Dyfcoa8E4dzdEicG8PGnybvRa_5XE-ePkD-AGq7ZVlzF-ugk2oQ68pxR4QzLhRkYdXSfWSVntqIBCA5M3ILQiypPSOIux0jwVqo4j9Zbyqus2fvypbYdH3Skz_iizJjOOtETjZSg98s8guGxZjxkovcPGaJjsdhi2gUjnhe_200yS9kMx4hXIGbfJCgBNVPlXY_qDGVTwoGVIeE7InOj7AJXzub0em-JYO-jLu-T53eseIvynvTp30Xx4koICR5oH_STstRElTMlibh-fJ0y8ZjH454-t04oZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«همه دنیا فدای مردم جنوب»؛ پیام جدید بابک زنجانی در آستانه راه‌اندازی دات‌وان تریپ
🔹
بابک زنجانی با انتشار پستی در صفحه رسمی خود تحت عنوان «همه دنیا فدای مردم جنوب»، از آغاز به کار سرویس «دات‌وان تریپ» از اول شهریورماه در منطقه آزاد اروند خبر داد.
🔹
وی با ابراز علاقه به مردم جنوب، اعلام کرد که این مجموعه با هدف توسعه زیرساخت‌های حمل‌ونقل و گردشگری در آبادان و خرمشهر وارد فاز عملیاتی شده است.
🔹
این پروژه که پس از راه‌اندازی و اجرای موفق در استان البرز به بار نشسته، طبق برنامه‌ریزی قبلی برای ایجاد اشتغال و رونق اقتصادی کلید خورده است.
🔹
آیین رسمی افتتاح این ناوگان برقی یکم شهریور در اروند برگزار می‌شود و چابهار مقصد بعدی این توسعه در شهریورماه خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/683320" target="_blank">📅 15:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683318">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8262ba082a.mp4?token=BM7YxOHo6TDMIF5m8g9TzVhXjj-nZGZJ74b8TxbbGKyUn4xn0FDEGpiddGMf0oHquzl1jsFtrwl4krnHMdgO8s3xVyZAYbkd_o1T6gD-nkJHxb3PVQ-uAVj-Anke267iKrBlmaaFUPtKzHQm2_vD5cvKZ1ccqtt1lIgQdGqTdUSx8AW1jJmm6jMg4XI7udGKElslmCpPtg0PDTKOGHCB9pXZuXhh1yUQUGcccl8kAdkYlhCRTfxNj_UohMLC7KQI8pWUFbU5iIxODbw4qkUkhF4lEBQwY9hzlJzlV48O5vixSdrVNGK8LxwU8O0YrkWu8PouGPOY2RqP8coklKi-pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8262ba082a.mp4?token=BM7YxOHo6TDMIF5m8g9TzVhXjj-nZGZJ74b8TxbbGKyUn4xn0FDEGpiddGMf0oHquzl1jsFtrwl4krnHMdgO8s3xVyZAYbkd_o1T6gD-nkJHxb3PVQ-uAVj-Anke267iKrBlmaaFUPtKzHQm2_vD5cvKZ1ccqtt1lIgQdGqTdUSx8AW1jJmm6jMg4XI7udGKElslmCpPtg0PDTKOGHCB9pXZuXhh1yUQUGcccl8kAdkYlhCRTfxNj_UohMLC7KQI8pWUFbU5iIxODbw4qkUkhF4lEBQwY9hzlJzlV48O5vixSdrVNGK8LxwU8O0YrkWu8PouGPOY2RqP8coklKi-pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره ای از آثار حمله پهپادی یمن به تاسیسات آرامکو نجران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/683318" target="_blank">📅 15:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e958cc4e7b.mp4?token=bTRxXNbx6ojIB_OrL6hEXa5Bt2hOdIF4gO3bepgoRfugvBCejcNahJHGvurjsNS8mnmTV0-oUrjnH_wYUhju3wAcYAuPiUeoiutltTJPwQqxGPR5YorW8Byl0zUb1QFlnMk6hKcTvIDIYcYZln7OlPS2Kxov0f9OWI9ic1Zj62FC8P6WWH5tJtBuK0rLmzpJkAezcp7UeKWUX6imGK1-22vi9e8QV4jrwWdcyAkxh4VSDMgOqP7ZvPYU9Whm6eLQKiJM1SO3_ckhR0bRtAKZMuc-TfQAHpfAk_Zt6WBmNhfVQyZMxwzqeRnPFbN9wandtgoWjqnoXPMg4Mht631F9RKUGsjXMuQMaJ9tF1E8fQgX8csxkcZojxBpeC44jP8GIZ6q1XYApxTlho6Rj7zmtqHzPNnnXI4cIZlueTSqMFbrEiJwNiRCd74nNwhSvTfL177RxMGkm-aD_k6K1hE47vsCTwEgf45WZ4Tr0Re6oCwJdQfG4AnVw2oIEiDGJ3Gh_Ix_B8tydQ5ksiuXY2V6JUTbYFcpwdKz8OWU5GkETVyrycYzp_MjR236Wr6VAGUJGsIXOU74tSN7AE8qubAu1D7JpDjHNKaKLMCfQEgy0D0KNZOYq2npa9W3H_5PjZ3AYXofAN5pEfDEwsCvk1Sayl6tfeo8-umluLLYkYsxRIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e958cc4e7b.mp4?token=bTRxXNbx6ojIB_OrL6hEXa5Bt2hOdIF4gO3bepgoRfugvBCejcNahJHGvurjsNS8mnmTV0-oUrjnH_wYUhju3wAcYAuPiUeoiutltTJPwQqxGPR5YorW8Byl0zUb1QFlnMk6hKcTvIDIYcYZln7OlPS2Kxov0f9OWI9ic1Zj62FC8P6WWH5tJtBuK0rLmzpJkAezcp7UeKWUX6imGK1-22vi9e8QV4jrwWdcyAkxh4VSDMgOqP7ZvPYU9Whm6eLQKiJM1SO3_ckhR0bRtAKZMuc-TfQAHpfAk_Zt6WBmNhfVQyZMxwzqeRnPFbN9wandtgoWjqnoXPMg4Mht631F9RKUGsjXMuQMaJ9tF1E8fQgX8csxkcZojxBpeC44jP8GIZ6q1XYApxTlho6Rj7zmtqHzPNnnXI4cIZlueTSqMFbrEiJwNiRCd74nNwhSvTfL177RxMGkm-aD_k6K1hE47vsCTwEgf45WZ4Tr0Re6oCwJdQfG4AnVw2oIEiDGJ3Gh_Ix_B8tydQ5ksiuXY2V6JUTbYFcpwdKz8OWU5GkETVyrycYzp_MjR236Wr6VAGUJGsIXOU74tSN7AE8qubAu1D7JpDjHNKaKLMCfQEgy0D0KNZOYq2npa9W3H_5PjZ3AYXofAN5pEfDEwsCvk1Sayl6tfeo8-umluLLYkYsxRIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیلی گراهام، واعظ و بشارت‌دهنده مسیحی آمریکایی: دوزخ فقط آن دنیا نیست؛ جدایی از خدا، آغاز جهنم است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/683316" target="_blank">📅 14:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683314">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIiOINJjuDQ3rVLhTFlYdpFgHqdsieSNbC7vO3oit20FMrnaNpcsH6hNoJISZZl1-gMtQS4aSWUujJrivYanMiPYQJ3ql3LGT23oQQSLgpSEwUjROfIgOMtMv812PxwqbTLbZT1BM9mp_KXFxiz6RznDsG90bzTOeyyjy-wK1pip0Ej5YKfWV_F7Bs9bGJnHLDrZla05HhnmaP7ipGiYvdikpNUqs1C1M9UaR0LFRQMjRAR4vHub6HzbgMliTpkckiO18ubRmU0taB89u5rHAFkNXBOkAcZdPrhXIeo9ho2rpi5gKuA1F_ijpZsrDnW_DFIWKlxs4KFqyoFue2pfHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف ۴۱ جمجمۀ آهو از چاه آبی در شاهین‌شهر
فرمانده انتظامی شاهین‌شهر:
🔹
۲ شکارچی غیرمجاز که در یک سال گذشته بیش‌از ۵۰ آهو را در مناطق حفاظت‌شده شکار و ۴۱ جمجمه آهو را در چاه آبی مخفی کرده بودند، دستگیر شدند.
🔹
متهمان گوشت آهوها را به‌صورت غیرقانونی می‌فروختند و سر آهوان شاخ‌دار را نیز برای تاکسیدرمی در اختیار افراد سودجو قرار می‌دادند.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/683314" target="_blank">📅 14:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683313">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر علوم:انحلال دانشگاه پیام نور منتفی شد‌.
🔹
زمین‌لرزه‌ای به‌بزرگی ۳.۴ ریشتر در عمق ۱۰ کیلومتری زمین، ایذه خوزستان را لرزاند.
🔹
آلمان حدود ۱۰هزار پناهنده‌را در نیمه ابتدایی سال جاری اخراج کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/683313" target="_blank">📅 14:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683312">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522b06e6fe.mp4?token=mB4-Zj8LYVGnxjqCrZIKCsPtDPzXMyuFiLAgAO11tStVFT9XWqk7abzZDbDidxr-994wMnmMrrYef8DtrgzE9zarRydDHZcESdi8BL7qlN4ROvF_EIv6urJsWxNrT-xwUC8P5W6-7XHnU9LY8hAiR1--p0e92bNOugdNaS9GW4rjUF6V3Lt6EOYJxGB4ag5iO1wZ9S2NgUUP3sAvU6a3s1bOTOiWXzCGeXk0Y5cKWxKtDMRuTLvTrC8CpHRvhRTr2JPPRBK9u_EPKMTPxmAeiqb4idAufQdGJ_wkYhO0NbU85cces4DAMP_u0q2MG6VQqJz30wXF9jwVtRtPgeXF3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522b06e6fe.mp4?token=mB4-Zj8LYVGnxjqCrZIKCsPtDPzXMyuFiLAgAO11tStVFT9XWqk7abzZDbDidxr-994wMnmMrrYef8DtrgzE9zarRydDHZcESdi8BL7qlN4ROvF_EIv6urJsWxNrT-xwUC8P5W6-7XHnU9LY8hAiR1--p0e92bNOugdNaS9GW4rjUF6V3Lt6EOYJxGB4ag5iO1wZ9S2NgUUP3sAvU6a3s1bOTOiWXzCGeXk0Y5cKWxKtDMRuTLvTrC8CpHRvhRTr2JPPRBK9u_EPKMTPxmAeiqb4idAufQdGJ_wkYhO0NbU85cces4DAMP_u0q2MG6VQqJz30wXF9jwVtRtPgeXF3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این‌طور آتش‌سوزی شروع می‌شود؛ وسیله برقی متصل به پریز ناگهان شعله‌ور شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/683312" target="_blank">📅 14:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683311">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d662816f83.mp4?token=cj8YvCKYyMB1a7JP7F28G7_diKJTabCXI6uGTtTJA-9dfvEdOMEImYjdEDzwwAVxztggACgK8IyyV8CKyFj-L181A151pnDP7HZki55EsU4QRhbxWh2xtZvQuLlDSYLpd6L8z1yG-2InTNJNU8SH_ZkXHfaJ1Nb7KgXFZr6Zfe2amW7gnlmMs7WAEu_fp12ZMl9plSn9c12_A4MJHQ-2KpkBmSeX8iMXowoNkuwcv_f0Awpn-zzQRBOnC-vHdds8yHWvJIPM-yd_CbIU8UZ6W4YMh6mYPUXi_9p9wABcV05Da11h9fVQKv1ZzapQC-tIpRC4Y28iJeXHPR86-SscRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d662816f83.mp4?token=cj8YvCKYyMB1a7JP7F28G7_diKJTabCXI6uGTtTJA-9dfvEdOMEImYjdEDzwwAVxztggACgK8IyyV8CKyFj-L181A151pnDP7HZki55EsU4QRhbxWh2xtZvQuLlDSYLpd6L8z1yG-2InTNJNU8SH_ZkXHfaJ1Nb7KgXFZr6Zfe2amW7gnlmMs7WAEu_fp12ZMl9plSn9c12_A4MJHQ-2KpkBmSeX8iMXowoNkuwcv_f0Awpn-zzQRBOnC-vHdds8yHWvJIPM-yd_CbIU8UZ6W4YMh6mYPUXi_9p9wABcV05Da11h9fVQKv1ZzapQC-tIpRC4Y28iJeXHPR86-SscRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس ستادکل نیروهای مسلح در بازدید از یکی از تاسیساتِ زیرزمینی تولید موشک‌های بالستیک: دشمن باید بداند نمی‌تواند با ارادۀ یک ملت بجنگد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/683311" target="_blank">📅 14:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683310">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxAGgVmcA156ZnJfmZbz0JM6fQJHc07QYDZxPNVoaDMRPTJMRca934ep-dTfGHL2MDHh764eoQTAl6URy1vWSaTj4goBXbPQ_7mD8nlHlwcC7GnhJeKhusHk83d2iPVsMClVWPo7K_K9GBzStsEneVF9IMgsaHckrpcjM3Mxfu6Yji7nfa9cZnz0okANzbeXzHyweC70FBzS5qNbA2EUNsnpoZhmB5oKXYx6eQ-2a7cZ9g0TFgdvNgD-4u8ygkF8jcLRH8l6eZDQ_M_3DT-rOSOr8gPwcKDS8xdogk8k2ALtG7WGUsd3Y1GceLUzwWkDjbIndoZt4efycxzlm-4MNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصاحبه اختصاصی خبرفوری با پروفسور پل پیلار: ترامپ بی فکر است، ممکن است به ایران حمله کند!
استاد دانشگاه جرج تاون در
#گفتگو
با خبرفوری می‌گوید:
🔹
مشکل اساسی و بنیادینی که مانع از دستیابی به توافق می ‌شود، این است که دولت آمریکا و حکومت ایران هرکدام معتقدند می ‌توانند در فرسایشِ طرف مقابل پیروز شوند و بر این باورند که فشارهای اقتصادی ناشی از فقدان توافق، سرانجام طرف مقابل را وادار به دست کشیدن از تقابل و پذیرش شکست خواهد کرد.
مشروح گفتگو را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3239554</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/683310" target="_blank">📅 14:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683309">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سردار باقرزاده: قطر با حضور تیم کارشناسی ایران برای دیدار با خلبانان اسیر موافقت کرده است.
🔹
رئیس سازمان بسیج: آمریکا پس‌از شکست، به‌دنبال فشار و اختلاف‌افکنی است.
🔹
وزیر علوم: انحلال دانشگاه پیام نور منتفی شد‌.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/683309" target="_blank">📅 14:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683308">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258f3e48da.mp4?token=qs3lpjSgeIStdV7EmK7FW8wmgsxD5k-Wl5Ha-ZVfgW_8dsP5DjIVP9HueXupxZR-4dgi6Nv38g_YFDjWwULML_QWEsEBZUfKKjNwrjcmsukxxSUENwbJ3Agc0O0xm4KWDZtKImqfCtdDY-cg_8H-bonoFm14VhECj4sqCRYDdvrjpCTN3FzadYMzEXrNQSvW-xPXfTcXjTTqi4OzmUTxqIYI6wyH7ifpGdvpNPXI5-io-rhnsUQPoykPbsqWSn3D8iXAm71eCsIdbLcCTws_cZhzKkNpvM3EbAAvuESASfNKCHm42o8MBgbfUmz9IMoCsGh2zzw6jWn6w2IQzPjtYJWYctfr-XQPjBvj7vRnx5SrJJL9IVe9Gzx9cyOyrrme4KwZAjKi8BqyUEbklfyqFoHxjwuYoWM63eEowZsqAZFMyZYNsnnTC2zRBxYUCazirh_QW0vai5LKI9U2A8YFhcLwrMZWUdv4rrG1AWN2eudlgrn24acmswftTtN6K5iqcP6Kvi9ReL4X-w7vPehDEshbFvknMe-7aPZ2ZolYdApvq4r7PXOI2KPf1tIHBcMmn7xE7Fn6KD5XmySFW3OMxB3ITOkHLOnfxf84hHs7u4Na5lXAPiIyhGZz4KWevK9CCiCfUKE85SCahG5LD1daZniK4-EGvWuoDCYaeCngNAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258f3e48da.mp4?token=qs3lpjSgeIStdV7EmK7FW8wmgsxD5k-Wl5Ha-ZVfgW_8dsP5DjIVP9HueXupxZR-4dgi6Nv38g_YFDjWwULML_QWEsEBZUfKKjNwrjcmsukxxSUENwbJ3Agc0O0xm4KWDZtKImqfCtdDY-cg_8H-bonoFm14VhECj4sqCRYDdvrjpCTN3FzadYMzEXrNQSvW-xPXfTcXjTTqi4OzmUTxqIYI6wyH7ifpGdvpNPXI5-io-rhnsUQPoykPbsqWSn3D8iXAm71eCsIdbLcCTws_cZhzKkNpvM3EbAAvuESASfNKCHm42o8MBgbfUmz9IMoCsGh2zzw6jWn6w2IQzPjtYJWYctfr-XQPjBvj7vRnx5SrJJL9IVe9Gzx9cyOyrrme4KwZAjKi8BqyUEbklfyqFoHxjwuYoWM63eEowZsqAZFMyZYNsnnTC2zRBxYUCazirh_QW0vai5LKI9U2A8YFhcLwrMZWUdv4rrG1AWN2eudlgrn24acmswftTtN6K5iqcP6Kvi9ReL4X-w7vPehDEshbFvknMe-7aPZ2ZolYdApvq4r7PXOI2KPf1tIHBcMmn7xE7Fn6KD5XmySFW3OMxB3ITOkHLOnfxf84hHs7u4Na5lXAPiIyhGZz4KWevK9CCiCfUKE85SCahG5LD1daZniK4-EGvWuoDCYaeCngNAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ست‌های رنگی خاص مخصوص آقایونیه که می‌تونن شهر رو زیباتر کنن #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/683308" target="_blank">📅 14:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683307">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LL2iONv3lmzKtsjxJiTeUVd0OCFVPhGYaSQZoeVfBkk3SKvXmgjrAOs5vmpECDQeLz7f_HAES-TAMWY7ooiYp6eL39Mktcb9uabRJS_GQ93kYF6XmT0_gC2K4fFl4QAYfOgvSPS9Zzhb-SaZcaU7i0wLc58JF5zttElxkYbpSZ_QzmDHWvH9GU2e2YUlhPD3YLx1Gy2axHB86MdcuA8mO6HqCq8xwGA2uQo4cQ6tQUizEg9Mpt423rsFNvLE1Z9RHKBl8MzyROdWpNltSB8sBW_6zjmEqQy3Ww2eZaxcZJPcFJp3XFByeDZksNzi35jr6Jr2VrVVr_CmLr-BjG2TzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت قالیباف از بی‌اعتنایی کشورهای منطقه به اظهارات خصمانهٔ ترامپ: پیام‌های متعدد برای شکل‌دهی ترتیبات امنیتی و اقتصادی جدید دریافت کرده‌ایم
رئیس مجلس شورای اسلامی:
🔹
ما پیام‌های متعددی از کشورهای همسایه درباره شکل‌دهی به ترتیبات امنیتی و همکاری‌های اقتصادی جدید در منطقه دریافت کرده‌ایم.
🔹
ایالات متحده امنیت تک‌تک متحدانش را با قلدری و بی‌اعتنایی مطلق به منافع آن‌ها به‌خاطر منافع اسرائیل چنان به خطر انداخت که آن‌ها برای لحظه‌ای، تمام هستی خود را در خطر دیدند. یک نظم بومی و مستقل که واقعاً صلح و امنیت را در منطقه به ارمغان خواهد آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/683307" target="_blank">📅 14:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683305">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a425c60cf9.mp4?token=hpGlwEuxfGiQ0IhBsjeXIaotRg4O5kldZAKC2k971FWTwdcJJYu4bxCEEKWcv4TLH1jF4QXuRQIGficj6FdXwo_Jy5dZKzoiFkCiemVsghXRZx4PsZ2A256pmt7w79-1akBi0UfwG88Tzcca4p8Kw-smU5gsxJp-jI9-curXupPqaZc90_-7TrJ3yrpYC6hHUmB4YNG1b_qosEf9jxHMy7KYtznFWoQioSdsJ4_3DzJx8ctHmAxWSFLhSjn5ZKs1tuv2fMz0fyvoCZKur7P30gL0g4EByngH0UaeT0vzxVrB2mQJNnS92QmQkap4WY9LlWdfOPYq0ZozvZc0XeA8B4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a425c60cf9.mp4?token=hpGlwEuxfGiQ0IhBsjeXIaotRg4O5kldZAKC2k971FWTwdcJJYu4bxCEEKWcv4TLH1jF4QXuRQIGficj6FdXwo_Jy5dZKzoiFkCiemVsghXRZx4PsZ2A256pmt7w79-1akBi0UfwG88Tzcca4p8Kw-smU5gsxJp-jI9-curXupPqaZc90_-7TrJ3yrpYC6hHUmB4YNG1b_qosEf9jxHMy7KYtznFWoQioSdsJ4_3DzJx8ctHmAxWSFLhSjn5ZKs1tuv2fMz0fyvoCZKur7P30gL0g4EByngH0UaeT0vzxVrB2mQJNnS92QmQkap4WY9LlWdfOPYq0ZozvZc0XeA8B4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین موشک ماهواره‌بر تایوان قبل از رسیدن به فضا منفجر شد
🔹
اولین موشک پرتاب ماهواره داخلی تایوان در اولین پرواز آزمایشی خود با شکست مواجه شد و به جای حرکت به سمت دریا، به سمت خشکی و کوه‌ها منحرف شد، قبل از اینکه سیستم خود تخریبی فعال شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/683305" target="_blank">📅 13:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683304">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c6e0c64bd.mp4?token=T5y_WZy2tNiAg736eFkjnlPRQg3AHRmJWsZE3m7JgDQOLaVW04l7JRvBLMuLB-unzuqXGVHTtix97XdZdIrjSBjwxYslXn0Z23aD4KVfqlKJgOPahwOfIILVTPQpfpDLCgmXIKWpnKNms_PBotHvXkJkVef8ZybQgOcy0F5PaUlKh8WaE1eASoFGidlXy5J_Y243BcrtIcpOpx9L9d9R-8kLkHXi6HQQXOmIGEXE0wSo0D5h2L2GtxHLmF701mOVyCBib0St_x5VlTm0afA_mGsU_ANBsdIq8-5tUFJRVPiM6R5bGDWvcli6HLnc_6u2_lyosF381EiwkyLMOupqWhXtEOPC3U_BvgOnmaaQQuuZGCKfYfGVrf9XvwdREwFhyTPA93qALWKexIh-8bBmUO1O61VHcbOgKcZi85eYb3JdLnltQICCV6YT7lIHJ5IRWG1D9i2zki7_6n_HgIc-hDM4wpKlI3sCTxuQsKrnjipbMn4AJf29dFc__xg1u81dAJrBgs1nZOfHvbG1ygk6SjkbBOm1y82e0XpzP8-IDQC7YoGQtVZRgIz-RNn5f7iebwhVlZGGnut42Y4hLVXSPg4vX2BBR52nyO3yLpzOgb6IE6JujSHQEpAiuFiVdMSxLBLFoSyhZxPZPmBVViasCcGaL0V6eWVkKUiy_L0wqtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c6e0c64bd.mp4?token=T5y_WZy2tNiAg736eFkjnlPRQg3AHRmJWsZE3m7JgDQOLaVW04l7JRvBLMuLB-unzuqXGVHTtix97XdZdIrjSBjwxYslXn0Z23aD4KVfqlKJgOPahwOfIILVTPQpfpDLCgmXIKWpnKNms_PBotHvXkJkVef8ZybQgOcy0F5PaUlKh8WaE1eASoFGidlXy5J_Y243BcrtIcpOpx9L9d9R-8kLkHXi6HQQXOmIGEXE0wSo0D5h2L2GtxHLmF701mOVyCBib0St_x5VlTm0afA_mGsU_ANBsdIq8-5tUFJRVPiM6R5bGDWvcli6HLnc_6u2_lyosF381EiwkyLMOupqWhXtEOPC3U_BvgOnmaaQQuuZGCKfYfGVrf9XvwdREwFhyTPA93qALWKexIh-8bBmUO1O61VHcbOgKcZi85eYb3JdLnltQICCV6YT7lIHJ5IRWG1D9i2zki7_6n_HgIc-hDM4wpKlI3sCTxuQsKrnjipbMn4AJf29dFc__xg1u81dAJrBgs1nZOfHvbG1ygk6SjkbBOm1y82e0XpzP8-IDQC7YoGQtVZRgIz-RNn5f7iebwhVlZGGnut42Y4hLVXSPg4vX2BBR52nyO3yLpzOgb6IE6JujSHQEpAiuFiVdMSxLBLFoSyhZxPZPmBVViasCcGaL0V6eWVkKUiy_L0wqtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلیس تهران نوزاد ربوده‌شده را پیدا کرد
اظهارات عجیب متهم دزدی نوزاد دو ماهه در تهران:
🔹
علت اینکه بچه را به خانواده دیگری دادم، اختلاف پدر و مادرش بود
🔹
پدرش اعتیاد داشت، حالا می‌گوید ترک کرده‌ام و بچه‌ام را می‌خواهم
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/683304" target="_blank">📅 13:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683303">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg6vYRemfVeoXrrttijKP6O2WaA8prszl3-ms2xCION_DM9OksBa1r3NG_MBu9aLEAeR8XAYQR60N4Z40hwHJvaoZyxqu5Zq1qgZ7MNoBkwJcuaU_EdNc_ZFAriyqofYiZpxxVXBXIkcd4riMxjSfFh-a3Wj7V7f0JmFivPpgZLuOx2hYxqNEPNofA97VvNcvYz9eGtnMbSqZkWwg-xNau69BAjlIHbfzwU5qSuRQBAbraJYMHeHm7aiu0kgn-hMnbFuNn292DluyXTeJsgVJAw03SakRm2D7WZfgKVaBXgD4LwQub_OwAOCL1f3W6Go3OYk491L-Lql0foJGz0yOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کمتر از یک هفته، قیمت جهانی طلا بیشتر 15 درصد رشد دلاری داشته است.
یکی از امن ترین شیوه های خرید طلا، خرید صندوق های طلاست که برخلاف پلتفرم های طلا آنلاین که ریسک خالی فروشی دارند، صندوق های طلا زیر نظر سازمان بورس فعالیت میکنند و ریز تراکنش های آنها تحت بررسی و نظارت قرار دارد. آنها ملزم هستند تمام سکه و شمش خود را در انبارهای بانک و بورس کالا نگهداری کنند.
صندوق جام_طلا از گروه مالی فارابی با قدمت طولانی و عملکرد مثبت خود از صندوق های طلا مطرح کشور هست که از طریق لینک زیر میتوان معامله مطمئنی و امنی روی آن انجام داد:
https://ifrb.ir/tlt3</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/683303" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683302">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d0c904ac.mp4?token=hkG8LCRRFgc6O_VOJOPTa_X5pqiuCgGmxnd_5SpNVwhM3i54Nx-TYeQQbHVZ616cXKJcrC40YXV-knODEYx21eA0ipvOVB5FjPiB7q-tVyiUm4OQjD5hUGE8wcD_yYBWbMCqI07Ter0V_0zkJwZtQZ-zThGj7_aqR9_nao-487QQPPLkQqeiF5q0zbo8ZRAlz0IAhWptz3rAwEqXD84bIlM7k4k3ZwAt-FXrAC0H0ZthbdtHbrrPTF2usxz2q_gO5xRLCmLxiL7LsTvOxAMlaZmovN2ZGr91pT6CkDsBa9HjElvAcGQjWIohRYJVBM2Mrs8eXAitPuoEPSW6M4mM9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d0c904ac.mp4?token=hkG8LCRRFgc6O_VOJOPTa_X5pqiuCgGmxnd_5SpNVwhM3i54Nx-TYeQQbHVZ616cXKJcrC40YXV-knODEYx21eA0ipvOVB5FjPiB7q-tVyiUm4OQjD5hUGE8wcD_yYBWbMCqI07Ter0V_0zkJwZtQZ-zThGj7_aqR9_nao-487QQPPLkQqeiF5q0zbo8ZRAlz0IAhWptz3rAwEqXD84bIlM7k4k3ZwAt-FXrAC0H0ZthbdtHbrrPTF2usxz2q_gO5xRLCmLxiL7LsTvOxAMlaZmovN2ZGr91pT6CkDsBa9HjElvAcGQjWIohRYJVBM2Mrs8eXAitPuoEPSW6M4mM9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غاری که دری مخفی به اعماق زمین است!
🔹
لاگوآ میستریوسا استخری طبیعی است که هرچه پایین‌تر می‌روید، مرموزتر می‌شود؛ عمقی که تاکنون به‌طور کامل کاوش نشده و همین ناشناختگی، آن را به یکی از جذاب‌ترین مقاصد غواصی جهان تبدیل کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/683302" target="_blank">📅 13:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683299">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PejObsnjPXGyDjOC_ioOHBnJDK5ivwZY78rGMaAYfi17Si_etSSpOcaJPoOs7gdG7LOjzJmJ5JyEs9VO-cT35tM_eMZrOVutlZ1MdCacuF3K1ZJCxQVBNXo8wWD_X9pUozgjfncSe71LT11NJ9i0Uiwr3sFj9Xx61v1aznyH6abmfD-qV5wQW3zwz1eqFJ6tKfrWrmV58Na40MnQe42i9nEjlVEbAtbvRyvaMQVZEuZwRdnwXa5nU6vToQnKFWHQSPP3Qs1Jl2LAwy1kOi9nbDw0Jkmh6OyovnWaexAYtEOh3e9QYFu6FaYywRSsiy_hfNl4ChWeNZiNAc6kL5gQGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزانه به اندازه یک کلاس درس، کودکان غزه شهید می‌شوند!
🔸
اسرائیل به طور متوسط ​​روزانه ۲۸ کودک -به اندازه یک کلاس درس- در غزه را به شهادت می‌رساند.
🔸
از ۷ اکتبر ۲۰۲۳ تاکنون در جریان نسل‌کشی اسرائیل، دست‌کم ۲۰ هزار و ۱۷۹ کودک فلسطینی در غزه به شهادت رسیده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/683299" target="_blank">📅 13:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683298">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f04d9628.mp4?token=aKa_BF8ucvjf_s6UiCvvZtWKJBF8_-x5Byzc_K6JbMMiLeP_NnozC8l_L9zHurOoKQgIWTSaKPCsh6NM9-DYw2fjDX8iKgPxwPBwJkYwxr8tW-bqDybjr6zimRP1j7V7XYBFiJJyrMAaTIRXUxTU7i2l5w_55aHnnRdvghOTp_b6umOLLXf2QnchzX2mw0yrBMPn0l_h7_4HZkOdgzUfvFHk2TFSHc-usQHYsa4nwrt97NxZd7l2j4jXF7TiklUBxzOK111og15_bITDut8dTaoHfbATKxPVUmzJDGFZ3Cgd1wndJlRFs97aiO-_62eBYlPdvLriVIGNTf5UPlkglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f04d9628.mp4?token=aKa_BF8ucvjf_s6UiCvvZtWKJBF8_-x5Byzc_K6JbMMiLeP_NnozC8l_L9zHurOoKQgIWTSaKPCsh6NM9-DYw2fjDX8iKgPxwPBwJkYwxr8tW-bqDybjr6zimRP1j7V7XYBFiJJyrMAaTIRXUxTU7i2l5w_55aHnnRdvghOTp_b6umOLLXf2QnchzX2mw0yrBMPn0l_h7_4HZkOdgzUfvFHk2TFSHc-usQHYsa4nwrt97NxZd7l2j4jXF7TiklUBxzOK111og15_bITDut8dTaoHfbATKxPVUmzJDGFZ3Cgd1wndJlRFs97aiO-_62eBYlPdvLriVIGNTf5UPlkglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه اتفاقی در پس‌زمینه تعویض دنده رخ می‌دهد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/683298" target="_blank">📅 13:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683296">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF8nwSDplFXB71yYk5T0okUm0VWuJ4EiAzp_4D4_EciLOa6V96tIApRWIOI64rfnI9DqEcGcbPKmvTFUxOYLIKpyxQRbQg2FByG1KqGtwCVABghfT1QnrMoyqxc58uwylGsh2sVaP2UdqMfH3K5vEZ4UlU4HR0nILCrUFvQUfUsyrKuJGyoazY7l4Ja5ubYmM2pbjayXeUs3ALXxNdOAT5nipQX95kQIWWrcHLSipX87DSNk8PX5Meyk5Kz9lrw_TNbixY3v3RyYK6RsKmMbaUJMV3SyZUO6AX0jAeZSTuP3Kfuhl-W0QRMWh9Oz2drzig9lUYrpkmF3BLc2mgrKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۳۱ مرداد ۱۴۰۵؛ ساعت ۱۲:۳۰
🔹
دلار آزاد امروز به ۱۹۰ هزار تومان رسید و طلای ۱۸ عیار با جهش ۶۵۷ هزار تومانی، هر گرم ۲۰ میلیون و ۵۵۸ هزار تومان معامله شد.
🔹
این بالاترین قیمت طلای ۱۸ عیار در سال جاری است؛ رشدی که از صعود همزمان دلار و اونس جهانی طلا حمایت می‌گیرد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/683296" target="_blank">📅 12:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683294">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEJUSZmGD8gD5x-sj-G9CDi3S-nR5D8imqUIMV-Yq-dASLTqeZk0KtVMv_CyE9Tb6zkT7v16fWcrIZEiljh0gT3dRQ_c14zNqCxo2Cct_25kQHIwAkU-0okWyOKlezsTU58am66t9zK8TLMi_tpHOORiEqkxNSBjPkAfJom8qf-tcBeLVmSSDfeEBg2Ys7qOA6G-UZ7zgJIeU0dlGc3Frhwybs_ghv0KLfarQysHNu-6iRVAOwPdlBjSI2wJNEOJpt11gdwZXENemU7XWza12_KlPO6BYJgkFOU4WGxA75OL-ew8ktrClwAwKBv1IvIcsY2fB0l6Xs0VJ4fXmVRXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس بالای ۶ میلیون ماند
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۰۹ هزار واحدی به ۶ میلیون و ۶۲ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/683294" target="_blank">📅 12:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a225862f30.mp4?token=fGy6zVVmg7zImmdkXHeqZVW2RF_vyViGUQJWJ3POoU4z_HnEuCb5pQ8oZpb8ItYqvLRn8t8su3AaFsIwS8Uuepl_HGcflID0SpBKEvN3HdLpoYEUPGkS1dNsi3NS9RKwj9xbH5UvOoIZUtSGQrAk9GlFPO86yDI7qcuy1cw-aCCxKC5EGJDj9CQ7SlTu3TnCo53lediOhfj5Jok-6r-qx1EwV-zoTPmnhj5ksJR3H7mjfMBcR3R9weh8bxMmGyGj_ojuN7dlBgVL1PAISrHiXiQF42GEmbcIDNRN-QbOyi_Ej7vZZZX7jH8MN0-HIoZvpQr9i9RXWfYe1SDvNid_2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a225862f30.mp4?token=fGy6zVVmg7zImmdkXHeqZVW2RF_vyViGUQJWJ3POoU4z_HnEuCb5pQ8oZpb8ItYqvLRn8t8su3AaFsIwS8Uuepl_HGcflID0SpBKEvN3HdLpoYEUPGkS1dNsi3NS9RKwj9xbH5UvOoIZUtSGQrAk9GlFPO86yDI7qcuy1cw-aCCxKC5EGJDj9CQ7SlTu3TnCo53lediOhfj5Jok-6r-qx1EwV-zoTPmnhj5ksJR3H7mjfMBcR3R9weh8bxMmGyGj_ojuN7dlBgVL1PAISrHiXiQF42GEmbcIDNRN-QbOyi_Ej7vZZZX7jH8MN0-HIoZvpQr9i9RXWfYe1SDvNid_2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۹ ماده غذایی برای پاکسازی ریه‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/683292" target="_blank">📅 12:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
حکم نهایی نظام وظیفه؛ بیرانوند از مهرماه سرباز است  سردار زاهدی، معاون نظام وظیفه عمومی:
🔹
علیرضا بیرانوند از مهرماه ۱۴۰۵ سرباز خواهد شد و دیگر امکان بازی برای تراکتور را نخواهد داشت./فرارو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/683291" target="_blank">📅 12:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683289">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAz-F48E2WYkZd8bYoKBRGfnD5NyWFeX3fnLqDJ0U46nYUPtwqfsxD3RaN4se2Lyf-h_Sag56M5qr1LAIwXfo7cbQmdKfW9Mpj6q4didOdGVTOyfrum-7KMnILJ_CNxtIMTdF44vlucMcnq9WYfl6LJvvLD3kn9LzxHYO8XhNTOfIstIXH6xabvmd8Ytq2kDkThiBYGEmNjz2wtvTKPTckW6XYWnRDXz93ng9D2l8Jpnnoatgi_N6mchPs0vwjM0EZTyxHRz5qzrWOVIyd1ZhSFWFNXhI-MmxQFj-f3jMahJ6QTeOwmFBrDCHEzPA7Mr94K_3eMCveQPdZtu0Q8n8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
معماری و تزئینات منحصربه‌فرد مسجد نصیرالملک، شیراز
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/683289" target="_blank">📅 12:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683288">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی هیات رئیسه مجلس:
جلسات صحن مجلس در هفته جاری مجازی برگزار می‌شود./ایسنا
🔹
سایت و اپلیکیشن فوتبال ۳۶۰ رفع فیلتر شد.
🔹
فروش کتب درسی دانش‌آموزان خارج از سامانه‌ رسمی ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/683288" target="_blank">📅 12:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683287">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e615f58192.mp4?token=QJBtTsaOUtp03OXywEIyOgyuMseETZrsJRnjK32h4u-0vdif0lz6f3NuXfNzDg7lcx1txBdMKYI6fX-oZq-QJkGyuqppzRJHMk4MP-EHLlVAgcwkonaPhF01KEJaR_9Q2Hs9u4lm4SpoP-_ByoOrVevzgvsIiYjtxzLoLqw9FNK3JfIb9guiC3pdxn_hfbpN0ltK55ARU_Lj2V3zfGYURMIMZjnVRjibzMQFgn3XAHzV_hShY-Kn8ZZhGFnpXL4UPXvOoen1ZCme9MvcAVIjuPLXgRfTOB4hD9LkWzmaRtDYJ3OnFv7lgCIHwnN2VwpinChz3cD6LNi_zo9PHa1EMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e615f58192.mp4?token=QJBtTsaOUtp03OXywEIyOgyuMseETZrsJRnjK32h4u-0vdif0lz6f3NuXfNzDg7lcx1txBdMKYI6fX-oZq-QJkGyuqppzRJHMk4MP-EHLlVAgcwkonaPhF01KEJaR_9Q2Hs9u4lm4SpoP-_ByoOrVevzgvsIiYjtxzLoLqw9FNK3JfIb9guiC3pdxn_hfbpN0ltK55ARU_Lj2V3zfGYURMIMZjnVRjibzMQFgn3XAHzV_hShY-Kn8ZZhGFnpXL4UPXvOoen1ZCme9MvcAVIjuPLXgRfTOB4hD9LkWzmaRtDYJ3OnFv7lgCIHwnN2VwpinChz3cD6LNi_zo9PHa1EMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در یک دقیقه با خطرناک‌ترین بیماری روان‌پزشکی دنیا آشنا بشین #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/683287" target="_blank">📅 12:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683286">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
آخرین وضعیت پیگیری وضعیت سه خلبان سوخو  سخنگوی ارتش:
🔹
همان‌طور که قبلاً هم اعلام کردیم، ما به طور جدی خواهان روشن شدن وضعیت این خلبانان عزیزمان هستیم.
🔹
اقدامات حقوقی از طریق وزارت امور خارجه و ستاد ارتش با طرف‌های قطری و طرف‌های بین‌المللی انجام شده و این…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/683286" target="_blank">📅 11:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683285">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b2ac23bf5.mp4?token=fNdP8OMo9SMLU92nNfT_kgz5f3d_yqFP9_kvf4-MlVoRiNlOM6FCp9zBkdgL942Idkw2il3YWXWGMC23Y4i_dQKbPPxwdaLCOYSUnx4xZzUiToghy_4p0YwbIVVAANzhejYyjd64WIUdP-xQvZ1-zjkUw0tx53dEk6nqzaBQLAopzsDm929X_mER2fpmv2FvbOFB6FSadKgLxCYGnuTrfbGwKSKx_FpbQfNOQp0oUCsmv3TQ1c9LszQJPCwKj6WL1pg7KwdFL2FCVUTqRH5QAoBgqngAqiy4V3W_n7NeZdYUdx1MiH5HpDDMXl5h4cByhu-l0nNTBO6TAfQVIYXR1DmVgMFZuxUitUdUziGhXXakhzoJXaok4ubyHrQw8G7sikT062tH2aXyAjyWdCX4QWp6kWD0VtIUsx0yDUdENvknzmv5Eo9lHvQ1tW7A5nCQtOX18FOxYZTL2ECe5V8vGlfii6NzB76odLaCU7SsJ3jh6e-UaJZj-WsEQWoCoF_8yQ2LvdLfC-ZqLAITgbcKnTX_L0_M27rnxr4BE706ASXw2yGrC0i_IZ561kaMtKlEj4BIlLiTazC8pAxHEA7PMGNzfyjXT3iyd2qXEq9qoMGquwZnQusLZDx6RIBkIo2AuIya2-aV9X5eQNHDSu4hhtOnEEIC5XNiHYEwLIDllQY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b2ac23bf5.mp4?token=fNdP8OMo9SMLU92nNfT_kgz5f3d_yqFP9_kvf4-MlVoRiNlOM6FCp9zBkdgL942Idkw2il3YWXWGMC23Y4i_dQKbPPxwdaLCOYSUnx4xZzUiToghy_4p0YwbIVVAANzhejYyjd64WIUdP-xQvZ1-zjkUw0tx53dEk6nqzaBQLAopzsDm929X_mER2fpmv2FvbOFB6FSadKgLxCYGnuTrfbGwKSKx_FpbQfNOQp0oUCsmv3TQ1c9LszQJPCwKj6WL1pg7KwdFL2FCVUTqRH5QAoBgqngAqiy4V3W_n7NeZdYUdx1MiH5HpDDMXl5h4cByhu-l0nNTBO6TAfQVIYXR1DmVgMFZuxUitUdUziGhXXakhzoJXaok4ubyHrQw8G7sikT062tH2aXyAjyWdCX4QWp6kWD0VtIUsx0yDUdENvknzmv5Eo9lHvQ1tW7A5nCQtOX18FOxYZTL2ECe5V8vGlfii6NzB76odLaCU7SsJ3jh6e-UaJZj-WsEQWoCoF_8yQ2LvdLfC-ZqLAITgbcKnTX_L0_M27rnxr4BE706ASXw2yGrC0i_IZ561kaMtKlEj4BIlLiTazC8pAxHEA7PMGNzfyjXT3iyd2qXEq9qoMGquwZnQusLZDx6RIBkIo2AuIya2-aV9X5eQNHDSu4hhtOnEEIC5XNiHYEwLIDllQY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا داخل یک چاه آب رو دیده بودید؟ چیزی که انتظارش رو ندارید!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/683285" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683280">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqh-OwzJFWJdqFqIo2pOvVt0dNGMJupqvdHiaMcC7xdwgTTFJtuJ4ZJhQJq_hUHpqGIZVwVVqOAdezsnBOcRVuylQICn4rGJyVxD_xLqAMfDdxkfCqeLYmL0hs9YWZNR_YuQoWrvpzT3UD28f2pimhnEmRDewKWFddNWYQA9w3ROSQoXimFaQQyzB-Trp8_gYojHydsGU9rbIjVL6DOqS7wtB6-_HOhBKI-TaZf_vT7qyDyLyPdD_dtn1qizxbGGQB844i31YwF6FpduCbTamxtGpF_UOg5Y7QR009cVnA1mkNuy8xRCkmJYqXPpfU-vLiIagkKTDDpRouNc3KXO2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DVz0APPLpCPtLOrVB4sA-yCG5id7Y3sejmh6IjwawRJvjnTDVX_HfZdZzbM5oRSKRaQhmn83dJvQIIIa9MD4Hynngoqyfq3GDhKfJe-aFlcPPGsUYKkSwG_mz-f-8swphRs9Myu1zVI7bQ6yLh2WpFrj3NmDG9UKzIwtTFAC9C0JKCEuLp5S8v8CnUdvuyUW2mODla0ewDwVu86cmMjuXtw5qUqxxzxOF0R4n6H4WgPLoZi7o4ACuPOEMOemZX9xfp44zNJoSmtBvf9m7m-f-9_BIWJ2O0tHX731a9ly8epftC70TgG28wzuiFd1401AX8CWGpoyDTTYwWNNkbd5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fV9kCUzlwIE33yKG4IiDqHu8IIZi6PzJBMskCzjpZZdwPXZrrod5gSargj0ZOhPZYBW2IAOiCsV5lVp6y1DFw3Koodllho2mlrhLOhfcjaMwnaJ3yeH_cpkv3p2Js-XgXLxyKh8oj1q40EXNbQTSi5ZNSC1XgtAuStWEvlL3zm_ZOgD1kL21alMZEUdkNMNP69lGn0qg0BHNV7YwPd44vZX4rJxvBqmWJYt4taHdjL_uHVfOxuQubFtiDpCjAZH9QUXCZ4AlImSNLreUpu0OHYXxWYB0d1fjjYRVYAYHi7zpY1Kdxv2gEsdA4wvyacgur6qOlPXKhjigFRy6s5LDdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LenxLHah1FhcBqq9_0VZXUgabltDLXvdOIpnSCvmsoF4K3x8hx9INgjFvtz-oCrSZrUet3yC3FFag4Y4uftsPX-zjbuZ9OlDIf_lCNedsw8v1W6tH-MTlIPPzBAFhXCxTY9DgsHZEdhQIl7K9oK76152oKpSjsOu1PF2OlTeTy82kTfO8r5xvZxDnD7YqIJX8QaD7STr5PWpdWlzp6tfwYnnLD7NP6n7WY8Cd-CJLHyd6CPQEhYvzkJiJyA25e8HDcPpVObxMn3WKrxfhetakA3b_gZ_NSS0UqtDJWdFrXkJSTMAlPSPxm1VigEoGcuFPz4n8N9__YM74U33K4KyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofYHRdaEaI7oFH89w78EpVz9ImvfSzgkGLUHrP5xYKqdcCc2G7Gv_oSDpNq9coxypyz4YfyKSlWhALGUdX4hLNUPFPFBPkcqfhJjpPg-jiNpDggqmV4g5RcTeO9ydU3TwdiCZlOcNmjSsZrnECxzqkCOHrhveGwXIcJuhhR6sJDzGrKpcY-xcZEyDAtNb8gkHhqOBdjq2Mj1tXk0RJoUvbCxmJHg-doSXWbZxIOJgjO171BaaVHeq-aZxf2RY9QsaqzqBTL4XvenkwX4LoNOLtRd0nIU-rCcoLO4GqXKLEPRWyS9NT4jSvkq6SsLwQy7sGEcFppzd84bOfIr6mYtUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت اهدای خون در ایران و جهان
🔸
بررسی آمارهای سازمان انتقال خون و WHO نشان می‌دهد میزان اهدای خون در ایران از ۱.۷ میلیون واحد در سال ۱۳۸۵ به ۲.۳ میلیون واحد در سال ۱۴۰۳ رسیده است.
🔸
از نظر شاخص‌های کیفی، ۱۰۰ درصد اهدای خون در ایران به‌صورت کاملاً داوطلبانه انجام می‌شود، در حالی که تنها ۳۶ درصد از کشورهای جهان به این سطح رسیده‌اند.
🔸
شرایط اصلی اهدا شامل داشتن سن ۱۸ تا ۶۵ سال و حداقل وزن ۵۰ کیلوگرم است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/683280" target="_blank">📅 11:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683279">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2hgjDscBuGfstHKLgc1YX6bgfpO4w2BQmrG2eZAE8Q2YYHHePLOZTzZOghuQmqtZD76TbrpNO5JlO53rKt87SHs1o-obLP1_oQnre3Teo2UIvqwqTiJA9yV_kDntpqjuPoCgW7zPhRP2nryOYhiDnl5xELM2CrHq4pRDmPVln3BlqcKns0QKaKeufaIIfN2-jc36dpnOdhiuCCTaLOS5ajT-aQXSsRA9EV3S4Ln7ypLfDn_s92WVrHgR543RbDYdXbY2YeWzj8il73IKGY9nMhZrRM395nNdLCVfOMAA3RVGErhpwYUXiYyMnxcmD3_zVgrystF6o77rGoFVTINqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر‌ رویترز از کبودی انگشت ترامپ در‌فضای مجازی پربازدید شده. بحث مشکل جسمانی ترامپ ۸۰ ساله و بیماری احتمالی او در فضای مجازی به موضوعی داغ تبدیل شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/683279" target="_blank">📅 11:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683277">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Epc-uflNg31xa3jrc0kepriAuJoMMpkNmJyLjMt-KeRsf7M3ubv0t6p_ErrCyqEP-ZAKdcgR4fL9lJXB2Pdu0QzsjnKe_jXSt65pzFUzbY2BscBxNB6hg33jJJ3MiCOV86pTihpsc3H7v6IskdKcYO5G6ZyXpnI4hSRmZDsh-GCh0ncYSXX0sF7HE5p5T8zFAE332VnJL-UGGahieRO2Y5rH3uYNEHaqCPDwoaLpzIECVSweQDOXQL7L6xf8Q9mloEq7yN7BI-B6iKQtnomhPo105Qw8cehUgGwfyo-foITW3lHTO-Xrznap-HrewcfLSyJ4dbzG89yWK9X5KGXyoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز مدعی شد: آمریکا روز دوشنبه تحریم‌های اقتصادی جدیدی علیه ایران اعلام می‌کند که احتمالاً خریداران بزرگ نفت ایران، از جمله شرکت‌های چینی، را نیز هدف قرار خواهد داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/683277" target="_blank">📅 11:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683276">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6_IN0xSss5oLeNrOt_75ieCwV_LUXPy-eZu2F6Zz6emkDeJokszYvDWc3d05QLrzAgC-wP6EFMEUwE9OulRGBsTU6RbEP_TMowGU9mCTGfK6MaiGnFTrEZa2C2XaCarYHz4SYknQmsdzb-M--6NKqQiNpse16lO8Q3UR_px5Wfp5vAPAR1xxcizP3-jm8zvwDcp5SYUFmuAESEqPhMHTzH_9-EU7WZOcYF7C8arg6MVF_jSE1ondGDtLhyQasroEneQQna2_f3y-Yrv_VvYkHIpGUCKckHaS60TX7Hbu5ItOSgSAA8S7O_GYH724ZbY6DTyGCrV4RMsF04ZmLUfHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ ویتامین و مکمل پرطرفدار و کاربرد آنها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/683276" target="_blank">📅 11:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683275">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای آسوشیتدپرس: مقامات مهاجرت آمریکا با ایران در موضوع اخراج ایرانیان همکاری کردند
آسوشیتدپرس:
🔹
ایمیل‌های تازه منتشر شده نشان می‌دهد که مقامات مهاجرت آمریکا با ایران برای اخراج ایرانیان در سال ۲۰۲۵ همکاری کرده‌اند.
🔹
صدها ایمیل رد و بدل شده بین مقامات مهاجرت آمریکا که توسط شورای ملی ایرانیان آمریکا به دست آمده، جزئیاتی را از نحوه همکاری دو کشور برای ترتیب دادن بازگرداندن بیش از ۱۰۰ ایرانی به ایران در سه پرواز مهاجرتی جداگانه ارائه می‌دهد.
🔹
این ایمیل‌ها نشان می‌دهد که مقامات ایرانی تا حدودی بر اینکه کدام مهاجران ایرانی به کشورشان بازگردانده می‌شوند اطلاع داشته‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/683275" target="_blank">📅 11:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683274">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
توقیف ۱۱ شناور حامل سوخت قاچاق در میناب؛ ۶۹۰۰ لیتر بنزین کشف و ۹ نفر دستگیر شدند.
🔹
مدیرعامل تراکتور: بیرانوند به‌دلیل افتخارات ملی باید مشمول معافیت قهرمانان شود.
🔹
رئیس سازمان اداری و استخدامی: حقوق نیروهای شرکتی هم از ماه آینده بلافاصله پایان ماه پرداخت می‌شود.
🔹
در میان سدهای تهران، ماملو کمترین و طالقان بیشترین حجم آب را دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/683274" target="_blank">📅 11:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683273">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebe703340.mp4?token=fU8rvqH-nUFnpC94_orA6sW9DX5IbuUxoPhosOwdYSRXTLPojqcQa8djSjwLlE_qpC0uuGZVTxDqY_i2M6bh-p7nDH3OpDooAIqUaRD4g-wwLjZcpsAtwM36B48l4Xp2vf4FlNt-aP2MXh7TE95jDK8Dzt7piCygEk_Mdt7RnzJ0R_9Co5fft3JCJ0doDAC8enIkmjAP33PLsf54aJ2KOqZlROdzd27D6J0YvQjs00ysej96vtxRCOl8qrX9aMDW88sTsU6qNhlqcL8tOxwWy-Z9dI-oP9bW9Gy4dDZc7Mjwb7-aIcIu2HJpCmiaRclbl-HDG3U3Pbt10Mndvfqf5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebe703340.mp4?token=fU8rvqH-nUFnpC94_orA6sW9DX5IbuUxoPhosOwdYSRXTLPojqcQa8djSjwLlE_qpC0uuGZVTxDqY_i2M6bh-p7nDH3OpDooAIqUaRD4g-wwLjZcpsAtwM36B48l4Xp2vf4FlNt-aP2MXh7TE95jDK8Dzt7piCygEk_Mdt7RnzJ0R_9Co5fft3JCJ0doDAC8enIkmjAP33PLsf54aJ2KOqZlROdzd27D6J0YvQjs00ysej96vtxRCOl8qrX9aMDW88sTsU6qNhlqcL8tOxwWy-Z9dI-oP9bW9Gy4dDZc7Mjwb7-aIcIu2HJpCmiaRclbl-HDG3U3Pbt10Mndvfqf5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کفرگویی فرستاده ترامپ: خدا هم نتوانست خاورمیانه را اصلاح کند
🔹
در شرایطی که آمریکا به دنبال کاهش حضور نظامی در غرب آسیا است، «تام باراک»، فرستاده ترامپ در سوریه و عراق، تلاش کرد ناکامی در منطقه را با کفرگویی توجیه کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/683273" target="_blank">📅 11:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683272">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf6b0631de.mp4?token=UcibKOV9p0z9lMyClpPee8vXWrqUsJSnuwUgEnrURu4406MRPy_m68moN96eWMF4TZmn1UfTwiq9XrI3tYbhmQPykB0JUdaSUdBcZR16PkV5W5dK_SaiFma2kZ_U9NrPbW3FF60VuDTdGSPdGVMkNMocbQnhnOI3vjnaJqmm5Utbsvr4V25Fu5q9pU5D1KHluZ1fuZ_jOB_xBkHx_9kfw8a7p3FyvMKyASedlRiMPRpMxnldGhFw-Q5wWE3YC_li7KYMnotQHHKCtczA-E5CAJnyXm8AHVUaTrPbsnu4auiI32M0sW4geYTyNrTzCt-Z9tHX6LS_0Vgdg_7qiDijmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf6b0631de.mp4?token=UcibKOV9p0z9lMyClpPee8vXWrqUsJSnuwUgEnrURu4406MRPy_m68moN96eWMF4TZmn1UfTwiq9XrI3tYbhmQPykB0JUdaSUdBcZR16PkV5W5dK_SaiFma2kZ_U9NrPbW3FF60VuDTdGSPdGVMkNMocbQnhnOI3vjnaJqmm5Utbsvr4V25Fu5q9pU5D1KHluZ1fuZ_jOB_xBkHx_9kfw8a7p3FyvMKyASedlRiMPRpMxnldGhFw-Q5wWE3YC_li7KYMnotQHHKCtczA-E5CAJnyXm8AHVUaTrPbsnu4auiI32M0sW4geYTyNrTzCt-Z9tHX6LS_0Vgdg_7qiDijmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این هند نیست! چرا کرالا این‌قدر با بقیه هند فرق دارد؟
🔹
کرالا؛ ایالتی متفاوت در هند که نظم شهری، سواد بالاتر و همزیستی ادیانش توجه‌ها را جلب کرده؛ اما راز این تفاوت چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/683272" target="_blank">📅 11:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683271">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK2ScuoEaPej5MzncOfrb-_BEWUJZhEKfgSbHEdGYIuGOOv6JWQfjK98Tm4odVcC82J-EExzHG95vsqkdQZkP_T6JclvdB3L1GZQpLCADmQ-Wuq6IDKUDikrQYszlCmuXWj6uL-fNy_jozKESfISQMZv1w8l_gZyTZnw8K_SYNhyvAwzH_fKUzKidn8DSXpyAwpj5vXsDUl5xx9_GJZi8tptKX6RgcjJOj1CTarjj2Cr7te72pxND_LlomR-ISLVPau8jn6U6GnacMYpWxRSK7IWjJR4IKuFbk2k9izZxKx8JX3R4b-pVLkfvNw4UxgGfk2fvgvjOvUreIMCV-mzsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلا از مرز ۲۰ میلیون تومان عبور کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/683271" target="_blank">📅 11:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683270">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
قیمت گوشت در یک سال تا ۱۶۰ درصد افزایش یافت
🔹
هزینه تولید گوشت طی یک سال ۳.۵ برابر شده و قیمت لاشه گوسفندی ۱۱۰ درصد و گوشت گوساله ۱۶۰ درصد افزایش یافته است.
🔹
کاهش قدرت خرید مردم، مصرف سرانه گوشت را از ۷۰۰ تا ۸۰۰ گرم به ۴۵۰ تا ۵۰۰ گرم در ماه رسانده است.
🔹
واردات گوشت گاومیش از هند نیز در دستور کار قرار گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/683270" target="_blank">📅 11:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683269">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_qhaqurva3_pq0-Mc0FD8zTsplRb0zWhXpDAK7Bux3B69zI57SfpJrfNVSz6Ttr4hKWunQuBVSXH8VZPiBi6Zvn0ORqZjGDw6wu7TFQIroEfEl7Xxnl9VFRGQh5m0Pu7J_nu83ByNM1yoGLFDxWscDI0Sxcj-2fAWGn-6Rw4U8F_nz-2A1ReQ6-CCWafbobqB1PjujQwc4ARLT-Tbw7IxPGk4wDrVm228quxfyIEGAJdjgsRvp-RqSTPPEXFkLITYqw0vbPTRSffPnOolI5rBudNfkKneXoNDq2q9Fjmksk8R8ec8pS2Ngyfkn2WCgI2Gor8PUPnZeYamdTMMKN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار کنکور ۱۴۰۵؛ ۶۵ درصد داوطلبان زن بودند؛ در کنکور ۱۴۰۵ از هر ۱۰ داوطلب، ۶ نفر دختر بودند
🔹
تعداد زنان در کنکور طی سال‌های اخیر بیشتر از مردان بوده و سهم آن‌ها نیز افزایش یافته است.
🔹
سهم زنان از ۵۹ درصد در سال ۱۴۰۰ به ۶۵ درصد در کنکور ۱۴۰۵ رسیده؛ به‌طوری که امسال
۶۹۵ هزار و ۶۵۷ زن
در آزمون شرکت کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/683269" target="_blank">📅 11:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683265">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZwpSODpxb_hoOcgkA4fcyuVY9b_97Fay9eI5GJwO6H8WmWgxxqMBnSH-nfOluWiN9Qq8YfmyRu2KjYjILgWC_qS4PgThNjNsx6u59PQD3Bj0l3ku0oj12H_SWNbh7r5ol3Roq4Klgpp6a8UdqjurSYWIVGpswTU66F6L4QE8Wnc9Qr2nOoZHjKxujKKf59accnrgUxUfayBM41wXr6ZCmvd-GV0jc9p4oXvswVkF2MBsm-GYbkNhMN1CraxMNadykoFmGHHuWDZ0yuzlurV1iBN86QRSjgzsK9Er1R6Hb6TD0Sj2-U0g4kWQs3ZzKMRP1nbhqUgaC1avr4ks5oXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGaaKpH2_dUo7ZGU-LkHNa2256FSAjZDXAQzCFTkvMXhlkCK_yy2I3vMC8YApOog_hQmrb4I5PxVHgMbFE0wYiZCX8SP3GugM3Oy6Tjyv1nvpkwJEt_wnP-iJocwzKWSnNZz7d5iRnsu3mI5XQOT91LqHJj42wS6uNxYWsrU7ZgSir9cOGybbvyjS6I1E2PtVZvPcFTHsvBgxKIaY5YM82AjbJnX0CgzTzGuA3f54B0hYER_QCTjRgpgkIOFtZJesLtiOSMUnZM8gVHK9UEin6IqdtOWQwS22zvoFXs7kjn_xSI3ZOcom6KsHYXcEs6Q4cSbArKdsNP1-hF3iqK3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnGr9UCQV4VguuH0E5hV9FUIjvE81h5i97mVjm2FqaGJw6KJ0rZ3UDuIFNBYbss7g_E_fVnuecOek34XIRVQGNfwohEla0Si1gzBFsMLk5U1mcM4NEYvaGCyEWIYk5qvgXBErSRL5B9ja9P3dDVFiz8HRGRckT7PgQAJN_--v1C7Ej7a2F0zgiTViHO91N5E4Of69cz_qtPgsXni4VwJsq0bqOe8aYZ9v44im5yasJyA9pGrkfOh4jHhTHYdNToRQ07JCNkqVXtbItdygvL4GUOysQA7S6u2WK6Q3DT0DaI8jhS0fACbEEdy0e9r9al2OKjqUkpfKzEFtK3_mqKNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKeJPxVp6YSd9KG7ZhaxTH0fdt-qJmWdF1jZdUHwRZZ4dWEQc6zavT2CEI9288gI_IIHfzaOMRLfzghWo8SZe0TMnVD52SDOwZZ2jw6M3efguuepRkOlUEaYO7LwDZGWabX7JdvPhnMrnvy0GB_F_ymRnhKhz_9QKhmSMjLy5ouB0dPjDJ-dTuuXEv9vU-CBubVFWCixvPJPV4aIlWhxwwWR44aYHBmMF9DsG4UV3DZQyqH4nAwuFOfHAhjErf_Efs9y-DTioMr8FzmonmosBMjDQod2WwyhCfFNnRgqegzc8XKUUF55p0mtQR0axtT9CDvratCuu2xBj5dBnYrNLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۷ گوشی برتر برای عکاسی در سال ۲۰۲۶
🔹
از زوم عجیب سامسونگ تا عکاسی شب شیائومی و جادوی هوش مصنوعی پیکسل؛ این هفت گوشی جزو جدی‌ترین مدعیان دنیای عکاسی موبایل هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/683265" target="_blank">📅 11:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683264">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1568d8a38a.mp4?token=gyPrZycpMY4D_mbm24IAsnEDdBFS9GbK32zP5pufPFlU7PIuI6O8Mht0ESw0QXaw9GVtr0TCVifG3r70JObUMo8GY0dBrZZFzv1idSqFXTWyC_P1D6cd2fj2z6uP67FEJ1_8cbKNjs4n2GnD9kQaZSL_LxQC3ikCwE0e8jH6G22RV1JmB5_r4wcYk7ZF3bGU8m0AgQHAYBYFxNxE-8E3HZiO8Zl0DeA8oinJz8u2YXZmKGZsEVFok2kjzYPPY8HpHYPWMuSGJJbNZMOpJ--l3hYUAQ07lipnBX8-54HdSEocsf_0DkDqR1SxJyw0K3ShmA962N9_ng0KiuzeOprqjm3cmGogWePlLEg-AtEREpoezvYgcNOoHIMLbvEx5U2J5n5LcK4a7FKpsyD55PMBiUINKCqZ9jm6vfzn0OVYvFIZmRB6xL7WNGwWtmBWTxNCYr-QY0oDla_TMNXpO-hZ0MLr51wYfWf7nwrfveWICS7NBWnKanHNdon6h3Gj3x3XCO2XJxr18NN8OLE9norvyvh4cgswtpaDNSQVycz1FCW4Meomg02Ycglc7iJLC1vA44afPcm2E2eTZpOGXEj0CR0Q91xOBDHu9r-bzhRI0iIrJYW977RukCk4sDrij8HuzlSaVz8G659SMTyOwTC9CgJbY09Bb131KUmvUCDUYFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1568d8a38a.mp4?token=gyPrZycpMY4D_mbm24IAsnEDdBFS9GbK32zP5pufPFlU7PIuI6O8Mht0ESw0QXaw9GVtr0TCVifG3r70JObUMo8GY0dBrZZFzv1idSqFXTWyC_P1D6cd2fj2z6uP67FEJ1_8cbKNjs4n2GnD9kQaZSL_LxQC3ikCwE0e8jH6G22RV1JmB5_r4wcYk7ZF3bGU8m0AgQHAYBYFxNxE-8E3HZiO8Zl0DeA8oinJz8u2YXZmKGZsEVFok2kjzYPPY8HpHYPWMuSGJJbNZMOpJ--l3hYUAQ07lipnBX8-54HdSEocsf_0DkDqR1SxJyw0K3ShmA962N9_ng0KiuzeOprqjm3cmGogWePlLEg-AtEREpoezvYgcNOoHIMLbvEx5U2J5n5LcK4a7FKpsyD55PMBiUINKCqZ9jm6vfzn0OVYvFIZmRB6xL7WNGwWtmBWTxNCYr-QY0oDla_TMNXpO-hZ0MLr51wYfWf7nwrfveWICS7NBWnKanHNdon6h3Gj3x3XCO2XJxr18NN8OLE9norvyvh4cgswtpaDNSQVycz1FCW4Meomg02Ycglc7iJLC1vA44afPcm2E2eTZpOGXEj0CR0Q91xOBDHu9r-bzhRI0iIrJYW977RukCk4sDrij8HuzlSaVz8G659SMTyOwTC9CgJbY09Bb131KUmvUCDUYFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی به ماشین پارک‌شده‌ات زد و فرار کرد؛ چطور خسارتت رو بگیری؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/683264" target="_blank">📅 11:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683263">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R35rede97Fb0WFzEqEJETE9IZXjOauP1vGYb-jPegm0RfddRnRd4Yn9Uv51vWu8ie4utJ8C_ychzjjh616AghdJ8WSVM8AgwPXBCy_oy-U3XooFNXyKFJJ1qQ5n-O7R9SK2RbFQd00-W6Ew79TRFUIw3GcFnaUloSyELmqMYAmFrmdlZCwDlxwzH6Q79svZbOfsPDoG7IjQqyqJDIvJviJJzjCsgZ6Cank5ZOMYx46x8zApG6Ycnf4LmHD_AdpC-MOVAMeagngLkbP94RvNt5Amjux1YmUnhcacqo0MnqVdgryjnN08CqPqwF5wBxi6NHNOfYfXJ8NqZ-8evPyPhTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بزرگترین کهکشان جهان کشف شد
اخترفیزیکدان اسپانیایی:
🔹
بزرگترین کهکشان شناخته شده جهان ۱.۷ میلیون سال نوری وسعت دارد و آن‌قدر بزرگ است که ما نمی‌توانیم مقیاس آن را درک کنیم.
🔹
این کهکشان هنوز در حال رشد است.
🔹
برای مقایسه، قطر قرص ستاره‌ای کهکشان راه شیری تقریباً بیست برابر کوچکتر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/683263" target="_blank">📅 10:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683262">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIf9sQ-dFNkJYCTKgKyPqoKjQWuf8_OB2sHkP5J3L_8NIEx6YqpY_oI43rHPi4eFCy2OGY6DgKlrkeu_er_SqKN7MjJ81VJp1TE09l39VgrJqRzVfh7Zg32q6jLtzwkRhTZWJ7-NOMqRebBP4VA0igILtqv3Rg7B4QSTiJXAD7Y5-t-BCmEjG-_XzA5UsmIc0_pPQyntbtswd-HIMMlqwjgeiPYE0tWMz71NyV5c2E6dhPBDI4n22mpND58ovqtJI0DLnGtKOEHETFaNfuBKCc32TdNdcQOuchx9SrD_1yZTr_CUevuj2rLB9yhQEkByJef4o3S7kccf5K0ogKhiWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای فاکس‌نیوز: ایران از شریان روسیه و چین برای جنگ اقتصادی با ترامپ استفاده می‌کند
فاکس‌نیوز:
🔹
ایران در حالی که ترامپ جنگ اقتصادی «خردکننده» را تشدید می‌کند، از شریان مالی جدیدی استفاده می‌کند.
🔹
تهران در حال تعمیق روابط مالی و نظامی خود با پکن و مسکو، دنبال دور زدن تحریم‌ها و عبور از کمپین «فشار حداکثری» مجدد واشنگتن است.
🔹
ایران به بلوک‌ها و اتحادهای غیرغربی روی آورده تا بیشتر با روسیه و چین متحد شود و در عین حال خود را به عنوان «محور اصلی» شبکه‌ای قرار دهد که مستقیماً نفوذ آمریکا را به چالش می‌کشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/683262" target="_blank">📅 10:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683261">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/647ad94e5f.mp4?token=Z3li6igKXTL6yfK_a5xOwojLMiBwdptg1MGMgDjYJc6exiuC64L7SZfN8Dhv-QoZIfuONNzXdSHpR_NBcqGFfLk9Gtun6pklzvKeTYzd2c2v3Fgc3VIZBlyPLKJZ60a-BnNL0AiNUKDhR2xut_i-BE__HhbRs8oczdQbANx3TlQxDZnwjGGqp5kdNeRwRdrp-zxp9yctwHZ7IwEO2upVUJu1d-MPU7zCFZO-0WbwMcjR5B9Q-ot7_CvBu5EMpeZcfkraKa88QRjnbS4qUCjf28uoIv3bTjFpm6riQs9r1zjZwNu_JA91tqlhBY_LlhwBgjtYe5yvVFSx9JHDtRQAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/647ad94e5f.mp4?token=Z3li6igKXTL6yfK_a5xOwojLMiBwdptg1MGMgDjYJc6exiuC64L7SZfN8Dhv-QoZIfuONNzXdSHpR_NBcqGFfLk9Gtun6pklzvKeTYzd2c2v3Fgc3VIZBlyPLKJZ60a-BnNL0AiNUKDhR2xut_i-BE__HhbRs8oczdQbANx3TlQxDZnwjGGqp5kdNeRwRdrp-zxp9yctwHZ7IwEO2upVUJu1d-MPU7zCFZO-0WbwMcjR5B9Q-ot7_CvBu5EMpeZcfkraKa88QRjnbS4qUCjf28uoIv3bTjFpm6riQs9r1zjZwNu_JA91tqlhBY_LlhwBgjtYe5yvVFSx9JHDtRQAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بالاخره از ماکان نصیری، دانش آموز مفقود الاثر میناب یه چیزی پیدا شد
🔹
فقط یه برچسب روی جلد چسبش..
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/683261" target="_blank">📅 10:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683260">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ5rC8RhkJiBJbnKaDi-oomSoJ1NQLXmFoO7Ec0NdZmPZEd5YD_mdeeTTDY-BcHXJ0ZgND4tq00OIBVXYlhZSqoxzaBNyIHrcXg2AAAy5VX0Nk0G9XptIK6-HeFdbCtEwUt6gu-dC9uDfxwl7BQsC4gEw_BDSpRSCpmebqTzfrvXTw0u1mLBl55pUF7_9Hj6PowPGKxUVkwEHXVWodpUYaXtEUkW7jCrvULtanrMbEZAM2DMpnrxYU1ujCWD92kSXmrxGLfGN9-95-8Oy1V45jcuvPmMFHlMFFOOod4XaWYTcygouBZc0Fu9PA6DcIZKYXEPwN5TSZe7aaimQf1uOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
بیعتی دوباره با صاحبِ زمان ( عج)
💚
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ «مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام
: حجت‌الاسلام و المسلمین حیدری کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی
: احمد بابایی
▫️
با حضور
:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای
: امیر مهدی باقری
📍
وعده ما: شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/683260" target="_blank">📅 10:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683257">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f1Rp2AsrmZJVLXMmkqKz7QYoQ0J39hyxhpR62Z0IqfrhXNQlO6XyeJrZqzkKR_-u_YDP4S7L_w-iunlR2KvLLtkLRBJ8v7_KWDMCSp2R7mnFsBcWFKw3Jnu75Q_dhzqAPONZnKS_iWwcRHW5ths6aSoinwrErjG7AOTNmTDl6GXqNMWMZoa816ZA8qwyE7kMh6im_-nEKSUBsStp0X86YMWStto95C0j-1BKFjxcQivxPGsKfx7kch2jDEs-v16T_pfqeU1O7pmN6fmO-GMjdg3r03tjoFx94OVW7KE60nULsb2o_h1GC7ucD_0-HS3ZXCc8j1R_s1e07w4mJqXt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IzbAQU1HJA2JEbLnsUTfO7gAp3V2SMsLOhfemsAvnZStoB2_fC1TCOyL9Gv7SEgQjK67fKMYNGvTY3v8phEE887l_MhwZ2R40P_D85bJ9LvMduprhvL5Cv3LjenoBtF9F8m2uiiv619PJEYz57AwO2cxoN-DMGArzs1GZj04Q2zbILdgIs8rK00WShdsz5SeCwboBkFRWJrDBhhNZRySbzxemLG7NvAT8-KX0kpV9fE5O9oTIep6ohdh09_KngOUK_wtH7mouzLd5gLUD4KYqj3IXOeIb5OtBL7ntvtEnoj4t_IOJPRSnx0FdVCNvcYThdlR-VEz6AP-a_k9NMrvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZvJFlm_GdRsSByvd4N5Naeud004O63Mx3hHJohVG6Wbqpg1XytMVV_uTshH4GNwyGXLx2Dou14KR-0rVldD1l5JfHp1pivKjPEo58Mfe8yCFOKgxkLOKlbr6cUacYC14whws_Sp_4FN88kF05XwEJCnKCsLZJLy-WdoaY9mJiht9jvYdGFWiNDzP5BZHw6C-5iOxIN-L4zOz7KG7P81sGVMYrqMqxDDg17VMArdly8GNR-QWlMpFmxo6P0F6ehtyqi-eHr_Rkqw85MK2rB2cuMTgwGFOyNnX6BO5dxvu3O3KLWZ3_RnwJSdQWwX7PG27c9QLogtaHCOzjvtGyGbgpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مدل موهای مختلف کریستیانو رونالدو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/683257" target="_blank">📅 10:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683256">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
‌موتورسیکلت زیر ۲۵۰ میلیونی دیگر در بازار نیست/ گرایش مردم به بازار دست دوم!
رئیس اتحادیه فروشندگان و واردکنندگان دوچرخه و موتورسیکلت تهران:
🔹
از ابتدای سال با افزایش ۲۰ تا ۳۰ درصدی قیمت موتورسیکلت مواجه بودیم.
🔹
افزایش نرخ ارز و رشد هزینه‌های تولید و واردات موجب شده ارزان‌ترین موتورسیکلت‌های تجاری به حدود ۲۷۰ میلیون تومان برسند و دیگر موتورسیکلتی با قیمت کمتر از ۲۵۰ میلیون تومان در بازار وجود نداشته باشد و مردم به بازار دست دوم روی آورده‌اند./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/683256" target="_blank">📅 10:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683255">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
استفاده از متانول در بنزین تولیدی ستاره خلیج فارس تایید شد؛ احتمال افزایش خوردگی در برخی قطعات خودروها
🔹
مدیرعامل شرکت نفت ستاره خلیج فارس استفاده از متانول در ترکیب بنزین این پالایشگاه را تایید کرد.
🔹
انجمن خودروسازان ایران پیش از این در نامه‌ای هشدار…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/683255" target="_blank">📅 10:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683253">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974bcd2f48.mp4?token=Fj6zF6zblPpIylm_HeF3AZ6QOQz3BaKJ75nSGv84Zs_b2xgLCXBYjx1vUGMhlzW6yfjtgfR2azCjDQ-9sqm4zBbjXgK7roOkQB-_7kvvOo5WWFqwHV3TzKLesdVF4s8GnI7fm8tMvvMLf9mo2DHjW9_bIZ9ZZoU-lbIsz4NZy7g3EDeWIyBzzOgtGsKZO9PLGh6Ll4opfbzTFs0nOnto7JXNkjLFSJkqkXQu1xTVe8Z06q9E2B01lSI8Ey-EyTCOsQj3E3f01ajRZg8Rf-UljrTsTkg28roa0VrwWxCXt9bARTz4mWbiUJOfklM_IZeAAT32JjlKm1WSnDFZDKVd6oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974bcd2f48.mp4?token=Fj6zF6zblPpIylm_HeF3AZ6QOQz3BaKJ75nSGv84Zs_b2xgLCXBYjx1vUGMhlzW6yfjtgfR2azCjDQ-9sqm4zBbjXgK7roOkQB-_7kvvOo5WWFqwHV3TzKLesdVF4s8GnI7fm8tMvvMLf9mo2DHjW9_bIZ9ZZoU-lbIsz4NZy7g3EDeWIyBzzOgtGsKZO9PLGh6Ll4opfbzTFs0nOnto7JXNkjLFSJkqkXQu1xTVe8Z06q9E2B01lSI8Ey-EyTCOsQj3E3f01ajRZg8Rf-UljrTsTkg28roa0VrwWxCXt9bARTz4mWbiUJOfklM_IZeAAT32JjlKm1WSnDFZDKVd6oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نابینایی که اسکیت‌بورد سوار می‌شود!
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/683253" target="_blank">📅 10:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683252">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYDM7GgCIcv1UHF_sVQqPziVBJ4GokLXP_DM9V5XVm1loPmkGKYllc-VHBO8GuqBgWmrITzu8aX8Xl6qsT8N8ScbzG2tc1u349sZP-t_93_sO2agCIOY5skYdDvGR2XZ48NUaUedOLoo9hu_Lvap9XFYnQIAxoFM14f7cVzvYUxCLbt3pmczUvQqI34Vwx4SgMGU5ujomp-T_wEC0KfPEh0BSVZyiZCGk-E7B2ZJ5GPzvK0onJiwA7xsTud_7eGPIKtriYh19kwL7wsaK2yRX59PMbsaRQ6j2xzH5mYyCwHMPsCszXd_-MKj0EYn5J2j2dYEsP2nmKSjtdSFHJGFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره
02191551808
در ارتباط باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/683252" target="_blank">📅 10:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683251">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1995235159.mp4?token=I2zcl0DvL4wWlWDqg_oNAWcbPJKMsRIf_AvRN9_0VPsh6DEwkQ1LjB8G432BdZtzBW-X_guSX8HMrpq7kpoGRfPw9TQ210TYeK0rWel8rZE8LTALcIUvwrWUyAN7t0E7f76SA9PEdlJLsvYlSjSd_oqGyCdha58Jn9yoPef8fYk7eRlFBbr1SQtLdxN8o0iEsatXPeTk6lA_A-Cvrd8ZO82bk7uM8jiwA5h9JxKyt2R9I_L2ON8v2MdaPHSwk6O5u-pubT_ZagdwMy7Mkhgqa3hXDUmZPCcl8CY-OWDgBexCmVl5Aske9TIuVBOOrKFdFn1Rzow1On0uMuMMg8VjQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1995235159.mp4?token=I2zcl0DvL4wWlWDqg_oNAWcbPJKMsRIf_AvRN9_0VPsh6DEwkQ1LjB8G432BdZtzBW-X_guSX8HMrpq7kpoGRfPw9TQ210TYeK0rWel8rZE8LTALcIUvwrWUyAN7t0E7f76SA9PEdlJLsvYlSjSd_oqGyCdha58Jn9yoPef8fYk7eRlFBbr1SQtLdxN8o0iEsatXPeTk6lA_A-Cvrd8ZO82bk7uM8jiwA5h9JxKyt2R9I_L2ON8v2MdaPHSwk6O5u-pubT_ZagdwMy7Mkhgqa3hXDUmZPCcl8CY-OWDgBexCmVl5Aske9TIuVBOOrKFdFn1Rzow1On0uMuMMg8VjQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کنجکاو هستید بدانید ماشین لباسشویی چطور کار می‌کند
این ویدیو را ببینید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/683251" target="_blank">📅 10:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683247">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c213ad4251.mp4?token=KjxZuy-b8i6MKRZIFSAubSrS-NuoLoT2cQ8DpcTqhbYGlg3yWaJachz9XvlrXC_85YoZncjpEEJ4wqdQx1L5a9CRFqCqqNlGe0KPK-H1iIFyABgzXBFsxq-48pas0Z-RSj6WnFK3Mji1Q6XC8KFsZwlWbcSDJaRwT5F3PKLCZzmYCus_XIzV_8ihPmVsOUvGm18qw76jPR8yTCC50lmj_1_SOEkVpYIO2B_USxenDIozGW_EVA8WLZKGdgVD6HplyCwQvXAnDCayPB2j-Q_mDfCo7JD7pvqsltTU7keSzlGoLiW2zT7rXAIdRyFgyABDGTLxIQ6UKwWuR57jcgw-Y4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c213ad4251.mp4?token=KjxZuy-b8i6MKRZIFSAubSrS-NuoLoT2cQ8DpcTqhbYGlg3yWaJachz9XvlrXC_85YoZncjpEEJ4wqdQx1L5a9CRFqCqqNlGe0KPK-H1iIFyABgzXBFsxq-48pas0Z-RSj6WnFK3Mji1Q6XC8KFsZwlWbcSDJaRwT5F3PKLCZzmYCus_XIzV_8ihPmVsOUvGm18qw76jPR8yTCC50lmj_1_SOEkVpYIO2B_USxenDIozGW_EVA8WLZKGdgVD6HplyCwQvXAnDCayPB2j-Q_mDfCo7JD7pvqsltTU7keSzlGoLiW2zT7rXAIdRyFgyABDGTLxIQ6UKwWuR57jcgw-Y4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قبول کن خوشمزه‌ترین وعده صبحانه‌ست؛ پس بیا با یک سیب‌زمینی‌املت تکمیلش کنیم
🥰
🤌🏻
مواد لازم:
🔹
سیب زمینی نگینی
🔹
روغن
🔹
زردچوبه
🔹
رب رقیق شده با آب
🔹
نمک و فلفل
🔹
تخم مرغ #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/683247" target="_blank">📅 10:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683246">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9cbce3fcd.mp4?token=stn8ikTkdtGV3fYGC4xXf-mG0wt-57B-hvA7JzN02AGa2eu4wwAPS5b1rWAs4PGwjXgpYA2CkQebpStQMGu7eN4R2Mjj37K6zkphmrNeHtldcuOqB6EpWB3Qs8gf293BjnJjwXSHZcZww8mB9XeEhLjuZqfYUAnLjvA18-7ZL-65yk4_uBImDD42RHgJZ-dEohFZyA1sw6na2J4leZpJrjeVVnSGiM7ZE404-HYeJJNn_ikT_PzLp483kStorHSOX4HeBfHRgP5fGQD06Hj7bvN69OdGUec2p_l1yhSkM6ukL8Hu9c2jQ0mflq08bJzyrRs6bNbWHgMU6Cy7oebp1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9cbce3fcd.mp4?token=stn8ikTkdtGV3fYGC4xXf-mG0wt-57B-hvA7JzN02AGa2eu4wwAPS5b1rWAs4PGwjXgpYA2CkQebpStQMGu7eN4R2Mjj37K6zkphmrNeHtldcuOqB6EpWB3Qs8gf293BjnJjwXSHZcZww8mB9XeEhLjuZqfYUAnLjvA18-7ZL-65yk4_uBImDD42RHgJZ-dEohFZyA1sw6na2J4leZpJrjeVVnSGiM7ZE404-HYeJJNn_ikT_PzLp483kStorHSOX4HeBfHRgP5fGQD06Hj7bvN69OdGUec2p_l1yhSkM6ukL8Hu9c2jQ0mflq08bJzyrRs6bNbWHgMU6Cy7oebp1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت سلیمی از ماینرهای غیرمجاز؛ از کارخانه‌ها تا زیر میز کارمندان
علیرضا سلیمی عضو هیات رئیسه مجلس در گفت‌وگو با ایسنا:
🔹
براساس آمار وزارت نیرو‌، حدود ۵ هزار مگاوات برق در حوزه ماینرهای غیرمجاز مصرف می‌شود.
🔹
مواردی کشف شده که کارخانه‌ای به جای تولید، با استفاده از برق یارانه‌ای، ده‌ها و صدها ماینر غیرمجاز راه‌اندازی کرده است.
🔹
در مورد دیگری، فردی که در خارج از کشور زندگی می‌کند، یک واحد مسکونی را اجاره کرده و ماینر در آن قرار داده بود؛ مأموران پس از بررسی متوجه شدند حدود ۲۰۰ تا ۳۰۰ ماینر در این خانه روشن بوده است.
🔹
حتی در یکی از وزارتخانه‌ها، ماینری در محل کار یک کارمند و زیر میز او کشف شده که با این فرد برخورد جدی شده است. این کار نه‌تنها غیرقانونی و غیراخلاقی، بلکه غیرعرفی و حتی غیرشرعی است.
🔹
در این حوزه خلأ قانونی وجود دارد لذا طرحی برای برخورد با ماینرهای غیرمجاز تدوین شده  که در آن مجازات‌های جدی برای متخلفان پیش‌بینی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/683246" target="_blank">📅 10:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683244">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f74ef4bc95.mp4?token=BfXVEXbcYu3tI-HYibqKF-OGRFyqApnhPikTpYusBtXKPFPz7qv9s1tLnY2ZZGsOHL35B0vKvKzGFguNtzHj4JkuZ0fler-G8Y2lEg0ZPsfusxB3PWbwxRmMVzILIATpwHMZvXwYGHGTwHlyrd75n-GqWkEJlh6v1yezcric13F6wDIUgjp0sapPjT32E6NuEHl8cO8Lsx4JI9l0reUja-LaQqehg6MRMCqoR-0GaDcnnfudaRP1qXC55-34E6HwhBh3mv4JkXVdHmZCIA6QEJBLMWs5eRqIp4Q3WwPWcbDjK1c4EXmXCQOwQCae7MzBPW6aXzptNG28-Hu1ZWQCQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f74ef4bc95.mp4?token=BfXVEXbcYu3tI-HYibqKF-OGRFyqApnhPikTpYusBtXKPFPz7qv9s1tLnY2ZZGsOHL35B0vKvKzGFguNtzHj4JkuZ0fler-G8Y2lEg0ZPsfusxB3PWbwxRmMVzILIATpwHMZvXwYGHGTwHlyrd75n-GqWkEJlh6v1yezcric13F6wDIUgjp0sapPjT32E6NuEHl8cO8Lsx4JI9l0reUja-LaQqehg6MRMCqoR-0GaDcnnfudaRP1qXC55-34E6HwhBh3mv4JkXVdHmZCIA6QEJBLMWs5eRqIp4Q3WwPWcbDjK1c4EXmXCQOwQCae7MzBPW6aXzptNG28-Hu1ZWQCQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آشوب در جام‌حذفی آلمان
🔹
دیدار تیم‌های فالدهوف مانهایم و کایزرسلاوترن در مسابقات جام‌حذفی آلمان، به‌دلیل درگیری‌ شدید میان هواداران و پرتاب مواد آتش‌زا، به صحنۀ آشوب و ناامنی تبدیل شد.
🔹
در این دیدار ۳۵ مأمور پلیس زخمی شدند و ۱۴۰۰ نیروی امنیتی در محل حضور داشتند. چند هوادار هم بازداشت شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/683244" target="_blank">📅 10:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683243">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvmRL2Js5cswbbAt-WlOLfmTIvFz4SxqsNvMQBH_mdZLumuFBIhllye-KhVh3xcfEclIomAKRPGE8bNmPCauhPaz7emI4AgMNMuwsrxAYQQkx8KyifXQiq81LTD0iM2uXU5WVmG0gLTUiWFJmKtOgOQOsYtchmKXz5qs5R1oB3Efss65MryjyHavpf7miehXcgEHvMITUv1Hveil7YmjuM8FE8fqhVOTLG4EziU-xWXGeO1rFHD4jkpbOP65EuI1ATtNiKBxEtMYfCiB7FbXsdOasnJBaKMwxBGNCapM7mJ9-EpKihqWZfhDefqIDxd_hKHZct9UeDZyuhNIxq9QXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
إِنَّ مَعِيَ رَبّي
🔹
در ساعت ۹:۴۰ صبح شنبه، ساعت شهادت «آقای شهید ایران» و به یاد نقش انگشتری ایشان
رهبر شهید انقلاب:
🔹
جمهوری اسلامی با اتّکاء به قدرت الهی و با باور کردن قدرت حضور مردم، از هیچ قدرتی در دنیا هراس ندارد. اگر کسی به تقلید از روحیّه‌های ضعیف بنی‌اسرائیل میگوید که «اِنّا لَمُدرَکون» -حالا به ما میرسند و پدر ما را در می‌آورند- ما هم به تقلید از حضرت موسی عرض میکنیم که «کَلّا اِنَّ مَعِیَ رَبّی سَیَهدین». ۱۳۹۵/۰۹/۰۳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/683243" target="_blank">📅 09:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683241">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba2079f6a1.mp4?token=gofmoQOV5rKQor8vV78rM8sIX0qm7zFOW5vWyxTvdMKWq8UO1CCfKf57jm9FnkWpCifWEw9gcEP80MObW-pHDPMgi9IXlyG_PptpaQRQWbPXw5OUAbM2YhTJfoyhAmIfKE7vKWWu9A-uP7dAC0ujSoihIalnorR6YiDoq8jJbDHlaGDDngs7BKeLRSXMxWUU7fffVOWYpY0at4P9P-cZLwR0R8YvCmQuIE0M04ASEXWe31IY03Qcjabycay43Am1ro-gOc0hJ-5APpMT6jtbLFMhz5hLB09aZSuCX9MJPcHdJSkaLkX-4aSImiCd8QgTvbKODG2BLnnHlRK-nljlww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba2079f6a1.mp4?token=gofmoQOV5rKQor8vV78rM8sIX0qm7zFOW5vWyxTvdMKWq8UO1CCfKf57jm9FnkWpCifWEw9gcEP80MObW-pHDPMgi9IXlyG_PptpaQRQWbPXw5OUAbM2YhTJfoyhAmIfKE7vKWWu9A-uP7dAC0ujSoihIalnorR6YiDoq8jJbDHlaGDDngs7BKeLRSXMxWUU7fffVOWYpY0at4P9P-cZLwR0R8YvCmQuIE0M04ASEXWe31IY03Qcjabycay43Am1ro-gOc0hJ-5APpMT6jtbLFMhz5hLB09aZSuCX9MJPcHdJSkaLkX-4aSImiCd8QgTvbKODG2BLnnHlRK-nljlww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای بسیار زیبا و باشکوه برخاستنِ هواپیمای مسافری از روی باند فرودگاه SFO با پس‌زمینۀ خلیج و پل سن‌متئو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/683241" target="_blank">📅 09:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683239">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udnzr9JIAzKXYTKCjFI1jVOswGp1pdiFdvSk9KDv-yiwyGX1dKgKYJi4JTl3LS9CcSOF1LofhH9R8jaPTPMzBJlsuKlmrj5gx-zyMZKHM_CF9ZmFlLcvFBQlZvbnM7LdUSA_gx64oUXpr_jdawGNLI0UG9geKgELKXzJNBTA5fhmwSaxj3f1RFCXlEoW_77tx35q0MzDL5b_VOV10NONRFaCghNO6fP9QUzJ0dbQg1egDa0CfINJ2M1_dI_b7TTIN0cUlifHdsO1SPtxJYu1UwdHgvxGutSSXDWKEg0Ur1J8lRPkKTOLs18TQOI3j5uzGduvzne5xShxXrJ1Rq9-cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
آبشار نمکی پتاس تنها آبشار نمکی جهان در ایران واقع شده است
🔹
ارتفاع این آبشار ۲۵ متر و در شمال مجتمع معدنی پتاس در شهرستان خور و بیابانک استان اصفهان قرار گرفته است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/683239" target="_blank">📅 09:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683238">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55024570e7.mp4?token=BbWmAkkWut7a_keHSP8mB0W1_FCjRVxiJGNYRhmN3xd0G727puT60NLuO754yZABG2Zd73amYsYj62Z4U7oh-SSNVZG0NX7owlWuB1OszOHobO-Hr85xAoc1lENeKtnbjLb-q4L_0jRupCG03qVeaQmB8_nj7nugP0-XD1kuzHU4wd-aUTIe9ZEvpN0ukkXr9E-d_hCZ3V9DxWDC7U_KJVlq1CWNh1z-LGP2l_Y6Md5co66hOQE6UBKWdZZENMX1okmjN6oJS_aKFAHsHrtc0Z6N3H6ZcNdveyqcjzDZi-l70vGJGJV8fTZ3KK3vlfu01www7ELYYDBb76LYPHQH-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55024570e7.mp4?token=BbWmAkkWut7a_keHSP8mB0W1_FCjRVxiJGNYRhmN3xd0G727puT60NLuO754yZABG2Zd73amYsYj62Z4U7oh-SSNVZG0NX7owlWuB1OszOHobO-Hr85xAoc1lENeKtnbjLb-q4L_0jRupCG03qVeaQmB8_nj7nugP0-XD1kuzHU4wd-aUTIe9ZEvpN0ukkXr9E-d_hCZ3V9DxWDC7U_KJVlq1CWNh1z-LGP2l_Y6Md5co66hOQE6UBKWdZZENMX1okmjN6oJS_aKFAHsHrtc0Z6N3H6ZcNdveyqcjzDZi-l70vGJGJV8fTZ3KK3vlfu01www7ELYYDBb76LYPHQH-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ دل‌خراش دانش‌آموز هندی زیر ضربه دست معلم، خشم عمومی را در دهلی برانگیخت
🔹
این کودک پس از دریافت سیلی از سوی معلم خود در کلاس درس، دچار حادثه شده و در نهایت جان خود را از دست داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/683238" target="_blank">📅 09:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683237">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
معاون هماهنگ‌کننده نیروی هوایی ارتش: چهار خلبان پایگاه شهید دوران، مأموریت بمباران پایگاه العدید را انجام دادند، اما سرنوشت سه خلبان هنوز در ابهام است
🔹
تاکنون به جز تحویل پیکر مطهر شهید مجید کاظمی، خبر دقیق دیگری درباره سرنوشت سه خلبان حاضر در این عملیات…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/683237" target="_blank">📅 09:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683235">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معوقات بازنشستگان تأمین اجتماعی این هفته واریز می‌شود.
🔹
اراذل و اوباشی که به یک سالن ورزشی در نسیم‌شهر حمله کردند دستگیر شدند.
🔹
وزارت بهداشت لبنان: شهادت و زخمی‌شدن بیش از ۱۶ هزار لبنانی از اسفند پارسال تاکنون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/683235" target="_blank">📅 08:52 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
