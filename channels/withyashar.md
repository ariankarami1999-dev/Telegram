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
<img src="https://cdn4.telesco.pe/file/nf9YSxSbNLBdPe-iswn91_VEdqkZ5EbOZg59p21ymn3w63JluuuUNIui75zALQ9XWa0ljKCom9LMlL6xnmJKeOxOb7sHCmrPGF3kMTO0wd02wKi8qodDNjBf6o8_ANgtHlOrngk7rIW06KdL6Pr_D1ocSJVB4cBzGqVKFtXS-XdiU9zraGgGYs5m-mIaGYYhs-MiieZ-AXL3HUqdqNLHMECdJjE8sbb3bAzDFQ-ERTVBo1h3uPAZQMP2dByaccwy2Jdya9h207-oRiCIzJ2OMnrzONsTFvBPHiKLDBUlJPBbAwjvG3M-hSW1vdzVWJxYx-IQVFJPTX2ZEf-j9dGCzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 332K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 03:29:46</div>
<hr>

<div class="tg-post" id="msg-16246">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=m0nrO3qxzHL_jMUGjvOvZMIFAOp_0ndmq5zD4OvhNULxXMICNZjxJzqJNcCM0v3lJWXw1ZwwmtxPM0IsIqRxAb7y-JOsY0_4eOQYMwOGuC2NKecMPBzwlE8Y6aTI5XVHet_e2XMOYgdWUnFz-V2KEJGxOw0vD4RbaL9tP-t4EnFRlhsUucU8DcbEzTnIzZaK3KSnIBDCszFXtLto9qnc_95OW4znHQecXO1INrH4ZEx1JLuzwC6qDAN2qKD5NIPU1flYrd2Y5ZKc0YvFgmWweyfmETy0rbm3pvFbJ2D2pwMT6YQ_g6_ED8XyLf5RR9ndxJSDSycmE9YbtMqCnA80kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=m0nrO3qxzHL_jMUGjvOvZMIFAOp_0ndmq5zD4OvhNULxXMICNZjxJzqJNcCM0v3lJWXw1ZwwmtxPM0IsIqRxAb7y-JOsY0_4eOQYMwOGuC2NKecMPBzwlE8Y6aTI5XVHet_e2XMOYgdWUnFz-V2KEJGxOw0vD4RbaL9tP-t4EnFRlhsUucU8DcbEzTnIzZaK3KSnIBDCszFXtLto9qnc_95OW4znHQecXO1INrH4ZEx1JLuzwC6qDAN2qKD5NIPU1flYrd2Y5ZKc0YvFgmWweyfmETy0rbm3pvFbJ2D2pwMT6YQ_g6_ED8XyLf5RR9ndxJSDSycmE9YbtMqCnA80kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها) , سپاه پاسداران که بیضه های این ارتش هم نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/withyashar/16246" target="_blank">📅 02:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16245">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رویترز : مقام‌های فرانسوی تجمع بزرگ شورای ملی مقاومت ایران (مستقر در پاریس) را پس از آن ممنوع کردند که نهادهای امنیتی نسبت به افزایش تهدید از سوی فعالان سلطنت‌طلب رقیب هشدار دادند.
پلیس پاریس این تجمع را که قرار بود در ۲۰ ژوئن برگزار شود، تنها چند ساعت پیش از آغاز لغو کرد و دلیل آن را فضای به‌شدت متشنج داخلی و بین‌المللی و خطر بروز خشونت اعلام کرد.
تجمع‌های پیشین شورای ملی مقاومت ایران، که توسط بازوی سیاسی سازمان مجاهدین خلق ایران سازماندهی می‌شود و شرکت‌کنندگانی از سراسر اروپا و جهان را جذب می‌کند، معمولاً بدون حادثه برگزار شده است.
@withyashar</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/withyashar/16245" target="_blank">📅 02:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16244">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUE7J5vGNMoNgUuQZJdPFopx4cNTfSBXLt335BtwLhjrjw9ui9ZBeItsxKiFNRmZy6f70yzvx6WLFbfa4gAdFa_RZoqAoracPq-aVGDipqKM-xZo0Yl5nSMsUBiByq8Az7dvspBq9tHtTjc-ehkREK9SgfmxbITd-Y7FY4__GlSIZlSZPcCgehX8PPNSsVpkLlq_KA9OCPd4-oGRcCMckdYlsmoAdGOGt_RdgIrP0naV_OpVkAs59X-hOqou-5GIyMQspnN0LtLyc-9OSEHMS14F1Ww0MZG1vJFwk1PBdBsX5WVkS4kSuCcFVRXZ9erFHpSy1sQ59AcThDBXJWqJXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است.
از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد تهران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/withyashar/16244" target="_blank">📅 01:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16243">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نتانیاهو:
حزب‌الله چیزی شبیه به «پنتاگون» را در زیر زمین احداث کرده است
@withyashar</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/withyashar/16243" target="_blank">📅 01:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16242">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shoNSEWJI5dwcaK9uxhdv3B0Jv9CRjlw_yXuqI1TvZg4SgXZIIO7RU92OSEka5WY4IDWD_wK3adem6YRLenZh2EW6Q0zvG8-R51fOD63u5ntKH7ehHGEosDtgM9MZQAHnwq7lFPApOfhcJg8vr9ODlkrkii7IioqmfXSUpBlN5UCF-lEgz_0DY8FFSLy1BVRymqZDhyxuBD_5OTBBu40OLmTyGmBw0qE0yhH-hnWdO7SUXTxtt-zJiA0jDTmsEHShYLOyz8R2ADXy2C21ZA4PectFy_naa-8e8q2ynqzXp82XPM73xI_SkEokjFX4U6dWWiC0HE8N6PXQEECx9DLxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبی خاکی باکسر داره میاد ! ۴ ناو ۱ آرایش رو به جلو و آماده به سمت خاورمیانه  یو اس اس باکسر، یو اس اس پورتلند، یو اس اس جان ال. کنلی و یو اس ان اس پیلیلائو در آرایش جنگی در اقیانوس هند حرکت می‌کنند و تحرک و پایداری آبی-خاکی را در دریا…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/withyashar/16242" target="_blank">📅 01:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16241">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رسانه رسمی قالیباف بعد از اینکه صداوسیما مصاحبه‌ رو قطع کرد، اعلام کرد بخشیهایی که پخش نشد درباره این موضوعات بوده؛
پاسخ به ادعای بازرسی آژانس از سایت‌های ایران.
جزئیات پیگیری آزاد شدن پول‌های بلوکه‌شده ایران.
توضیح درباره اعتبار 300 میلیارد دلاری برای بازسازی که تو متن تفاهم اومده.
پاسخ به ادعاها و حرف‌های ترامپ.
توضیح درباره پیام راهبردی رهبر جمهوری اسلامی تو 28 خرداد.
@withyashar</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/withyashar/16241" target="_blank">📅 01:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16239">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0q-hZcTcWkr8ykfj78naAn6KI6ZRqw3rPNArtWgw-iRboZSK9E_4PWGoEQn_AsSBv-PmWDOYFGB2vJ1_dMOSfSfSCmA-iPI7E6fZalS-KdPoeKO89_E77oN61qMye9r3cwmkOzOCU5mzLJo8RSiui82Yl3gd3lVmqscHXK7Cgy1JJE_02mZsn7kLBbY67xK5ZmVzTAWQEtoyujY4_1xKeCBezMmJpfKbmApwGy95xL1ZHHC2jvNXiUaD15BL3XphHGASrOm8qQ9Cwt3y_qY6PAhkS1HdegvljFG_hHQY5C4cbqVCQ6i_BobSlGIKzp4pLgjBirS20i1ez7HJqah2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9663206797.mp4?token=VDYr500ziZN-VECMbsg_2mvzbLzTyJuxYRcB5UYgy5fCnwXA6t4AC38bY1bbRqbuZohXUD0Dm4RDLhv40giYyuvCbh3uzTVeLQF-qdox6Qw1nTitbogb23Um6hrPMdc31R2uPlmVViR9zoni3VjrEBRzEbfxpuIwB1i4JiaxlNaULsuohMNtcvrUOBrhWn2kpjr1r9_xCYtf5z7R5mdxKUEGCA9ShZ94bG5kY04Er3_rsW22SLcQ3YZaZtPacSk0Fd4DqtQzSm71BJvSAVHyW77tFS_eVsIHuZUNAOVEOk2LEZ1V6wBxpXkcZB6LMsHW1-I1TinsM-PLP_xwEfiMqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9663206797.mp4?token=VDYr500ziZN-VECMbsg_2mvzbLzTyJuxYRcB5UYgy5fCnwXA6t4AC38bY1bbRqbuZohXUD0Dm4RDLhv40giYyuvCbh3uzTVeLQF-qdox6Qw1nTitbogb23Um6hrPMdc31R2uPlmVViR9zoni3VjrEBRzEbfxpuIwB1i4JiaxlNaULsuohMNtcvrUOBrhWn2kpjr1r9_xCYtf5z7R5mdxKUEGCA9ShZ94bG5kY04Er3_rsW22SLcQ3YZaZtPacSk0Fd4DqtQzSm71BJvSAVHyW77tFS_eVsIHuZUNAOVEOk2LEZ1V6wBxpXkcZB6LMsHW1-I1TinsM-PLP_xwEfiMqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای افغان به مناطقی در بلوچستان پاکستان حمله کردند و درگیری‌های مرزی آغاز شد.
@withyashar</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/withyashar/16239" target="_blank">📅 01:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16238">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unJKlWMunXBfv7fwbZaKFofgrpjOGxMR93KY50yHW8VeSeACtRTWGw2kCd2sjto4d6Bl27fpJ55c78sZGbUkXT33FI1HiGaGZAeaHFWyS9ho7T_8wB5G2vgAQyUJYb8FgKTwLuGXcWGfQQQ4Esi5GaiH6XGbpiYu0cDnybPJve3B0V1xgfToke6vjlv1jVwXYYZvDCmRQquYdvIrJStKqUIPFIq_MbrVPUjrl-pLW0TORlx42gxYIz4s44z9qigxWmqTOkm9qMxiJOuYl5-_BOAP1dpSlETvZuJTQhHdN0PxHJRx2SF2QngsG2HXLvYHkw2LBKepAzznTVPqrCZJAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاروان‌های کامیونی پر از تابوت جدید از تروریست‌های حزب‌الله که توسط اسرائیل نابود شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/withyashar/16238" target="_blank">📅 00:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16237">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وال استریت ژورنال: سپاه پاسداران این پیام را به واسطه‌های قطری منتقل کرد که اگر تضمینی مبنی بر کنترل انحصاری تنگه هرمز توسط ایران دریافت نکنند و اگر ایالات متحده و کشورهای غربی از برنامه‌های خود برای دریانوردی از مسیر جنوبی در این تنگه در نزدیکی سواحل عمان دست نکشند، دوباره تنگه هرمز را خواهند بست.
@withyashar</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/16237" target="_blank">📅 00:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16236">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaGZy5au2zooT0tRirK4ROQyyMkRhcGk_XcAsgBVOKVeD8AyxHyGD-l56uovYXtq7wOAeZ9QVAyPhU66HV7pKDYP3qh_zD1r1kSw-m8ScVBbIrTzY3_co14EM-xhyyuIhbfwxrdZBKLy96BAXbLO-N8AvXyNW88QL6AalZvmIfvahUpfAQmmR1TYScTEao9aFkz6_-mcmFTcFRuviwpNsYU1MXgaxp_iE-cqcGvExNfREQR0yZuGc5WAkTOVtEJ_ulYYGQJei716ndKtRDDqNDL9paIh_RfcZu0CujYHhdSYqhU-D84Pb6PI-zBRuxlzXS24OVE4RSRg-UiztNOVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین لرزه ای به بزرگی ۶.۲ ریشتر خلیج کالیفرنیا در سواحل مکزیک را لرزاند.
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/16236" target="_blank">📅 00:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16235">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جی‌دی ونس: ایرانی ها یه تاکتیک عجیب برای مذاکره دارن. توی رسانه ها میگن مذاکره نمیکنیم ولی وقتی به ما زنگ میزنن برای مذاکره خواهش میکنن. خب این یعنی چی؟!
ترامپ مایل است بمب‌ها را رها کند، اما فقط اگر هدفی را پیش ببرد.
@withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/16235" target="_blank">📅 00:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16234">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اتاق جنگ با یاشار : چک افسری ! این ویدیو نکات ریز مهمی داره حتما دقت کنید! https://www.instagram.com/reel/DaOSvJUxDdL/?igsh=aGRkbWQyN2ozeTNs  کلیک کنید و کار های اداریشو انجام بدید</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/16234" target="_blank">📅 00:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16233">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کاور پست ، چقدر اینو خوشم اومد
😁
💥
@withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/16233" target="_blank">📅 00:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16232">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اینترنشنال: مجتبی خامنه‌ای میخواد اژه‌ای رو بعد از پایان دوره پنج ساله از ریاست قوه‌قضاییه کنار بذاره.
@withyashar
( البته تجربه ثابت کرده هر چیزی که ترامپ و اینترنشنال بگن، جمهوری اسلامی لج میکنه و بدتر انجام نمیده.)</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/16232" target="_blank">📅 23:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16231">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kofg781dy87e2f2PyH1b1qUP_NgNA0R-Fn1L0KAPsT9Fq_lEVGj3gyTxHJEF_frv0PtaKPSDcNIiCllq7NCGUeNCRMxiaVStgrYpvt_eS-tnFNnANVCMl66-uYibjtgb8USLUHjMCYHtG9RfyQHj4nhH42ti4XNm5bmNKqdDRmbUOMaLpF3-cnJ4vttWEa3QaI3L86LBmbEZwDzr7-hh1gtL47ketWFvHe4yOe6x0bzZHYOoOxCSHFUXYYVLncPiUZWD6pmOialYgPC8bSiBS34UASbGCbs3_Hec_sqBc1SNT4y3oi6-Rpe4jhKtizCbDvzmjutMZjGDiMprgCorGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور پست ، چقدر اینو خوشم اومد
😁
💥
@withyashar</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/16231" target="_blank">📅 23:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16230">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ec7f9b40f.mp4?token=Oi9mTfr3g4Qj6tEeGRoAS2U19s6DRo6IBSIGEbbq-VDMVWjN0UGm0udgprU2P12CDWgxf72fXaSTypE77_8ytEm4X6CNY-y55lWL_CHVQw4paqTbP3gRQu0Ri7cnsPpAXrly5N5ZEvQt7MkoFyQYhDggHpVAC_QRBkeOp3adrs-QYyajnkP8BRXo-YRzRa-9yzUG-U98a2l7N7CLRPA5GqQ2Cwi0gkJoeukAPpxxA-anAHz5NOPSsEEuvUn2vlBr98d7nj5NIVelZR3NQrl0jadX99VmEtD5ShX4CsCcJuFWdxlYC8rH6Z4iXaPSworwd3X6FRr_69wKXMPLHf__lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ec7f9b40f.mp4?token=Oi9mTfr3g4Qj6tEeGRoAS2U19s6DRo6IBSIGEbbq-VDMVWjN0UGm0udgprU2P12CDWgxf72fXaSTypE77_8ytEm4X6CNY-y55lWL_CHVQw4paqTbP3gRQu0Ri7cnsPpAXrly5N5ZEvQt7MkoFyQYhDggHpVAC_QRBkeOp3adrs-QYyajnkP8BRXo-YRzRa-9yzUG-U98a2l7N7CLRPA5GqQ2Cwi0gkJoeukAPpxxA-anAHz5NOPSsEEuvUn2vlBr98d7nj5NIVelZR3NQrl0jadX99VmEtD5ShX4CsCcJuFWdxlYC8rH6Z4iXaPSworwd3X6FRr_69wKXMPLHf__lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : اگه لازم باشه، برای بار سوم به ایران حمله میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/16230" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16229">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/16229" target="_blank">📅 23:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16228">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سی‌ان‌ان: آمریکا و کشورهای خلیج فارس نهادها و مقامات مالی حزب‌الله رو تحریم کردن.
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/16228" target="_blank">📅 22:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16227">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmwATtYKBhcgab1QGdeZhDqkwDPgwR_rSTaHeMvezex_fOkxcBazpp8SUVZGn0Q57khydObZ6f9lkjUIpan9UnR6zGzSXBKyJtZNty1hfUquwFJSMtB52V3tLtIh6LPg22UVMVRzUFo7C8zQuaL9ZaFjz-jjMmgrkqJ_UiWUy5XXUsQCQjg6y-s4Vs8IOknv2-irwWiKWENtVqRoWoK8ujB1ocImChU8h6rpVRdnC_aeLbilCvdDc0LUNFG2avRiKvu5EWoQjSOnb9aW590VB2b_t_8RhB-2tUH555ELabk_dns4AcvLXWhdBqgcPkTUDvl9Mk_ximsIIpbsTFnmtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تابوت های آماده شده برای خامنه ای و خانواده اش
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/16227" target="_blank">📅 22:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16226">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔸
فرمانده سپاه تهران : خودروی حمل اجزای خامنه ای به شکل ضریح حرم امام رضا طراحی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/16226" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16225">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ در تروث : مایلم به رئیس جمهور شی و کشور بزرگ چین به خاطر پیروزی بزرگشان در قانون شهروندی از طریق تولد تبریک بگویم!
@withyashar
یاشار: ترامپ در آغاز دوره جدیدش فرمان اجرایی‌ای امضا کرد که می‌خواست اعطای خودکار شهروندی به بعضی نوزادان متولد آمریکا را محدود کند(پدر خودش با همین قانون آمریکایی شد چون پدر بزرگش آلمانی بود)، اما دادگاه‌های فدرال دوباره آن را متوقف کردند الانم  عصبی شده داره به چین تبریک میگه
😂</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/16225" target="_blank">📅 21:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16224">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نتانیاهو در خط مقدم جنوب لبنان:
«حزب الله زمانی قوی‌ترین ستون محور منطقه‌ای ایران بود، با تقریباً ۱۵۰ هزار راکت و موشک که به سمت اسرائیل نشانه رفته بود. امروز، تنها حدود ۸ درصد باقی مانده است. اگر تهدیدی برای امنیت یا سربازان خود شناسایی کردید، فوراً اقدام کنید. منتظر نمانید.»
پیام ما به ایران و حزب الله ساده است: شما اینجا جایی ندارید. آینده لبنان باید توسط لبنان و اسرائیل تعیین شود، نه توسط تهران یا نیروهای نیابتی آن. هدف ما امنیت و رفاه پایدار برای هر دو طرف مرز است.
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/16224" target="_blank">📅 21:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16223">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزیر خزانه داری آمریکا : فقط چین نفت ایران را خرید
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/16223" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16222">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رژیم چنج ؟! محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی استعفا داد @withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/16222" target="_blank">📅 20:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16221">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رژیم چنج ؟! محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی استعفا داد
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/16221" target="_blank">📅 19:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16220">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=cQMo6olaitLPhVIgnnLkN4fQ5XRGGFJiMOfch4De2yrXhCBiFMaakSggWHvFCvnfVCLH7bx2WMtlNMOoojbh1yoV-awlFjWq85GRrfaoQAcnAX_SkMj9YlJ0fSU2pj1dx_nNozbjeZA6xpOWYRwhqaQ_b-Sr4cINFgyZ0MtaaQmZfnnpEzK_8arvTJq9vFjBD5UzEb5fdyG7LiK33GECPp4lbYsVnnXEjxj8F7ePxBe0g3rxgUF_bJqiKLQdeNpDdXx5jAhrabtfD240flcurG_6RItp7ROItl8-qbBQunVBNEUufktPZ3xOkmk7De6HBG1lOgFH-AIXeenrP9ptFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=cQMo6olaitLPhVIgnnLkN4fQ5XRGGFJiMOfch4De2yrXhCBiFMaakSggWHvFCvnfVCLH7bx2WMtlNMOoojbh1yoV-awlFjWq85GRrfaoQAcnAX_SkMj9YlJ0fSU2pj1dx_nNozbjeZA6xpOWYRwhqaQ_b-Sr4cINFgyZ0MtaaQmZfnnpEzK_8arvTJq9vFjBD5UzEb5fdyG7LiK33GECPp4lbYsVnnXEjxj8F7ePxBe0g3rxgUF_bJqiKLQdeNpDdXx5jAhrabtfD240flcurG_6RItp7ROItl8-qbBQunVBNEUufktPZ3xOkmk7De6HBG1lOgFH-AIXeenrP9ptFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خالد مشعل از رهبران حماس مرگ مجتبی خامنه ای را لو داد
@withyashar</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/16220" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16217">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خالد مشعل از رهبران حماس: مجتبی خامنه ای کشته شده
@withyashar
🚨</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/16217" target="_blank">📅 19:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16216">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نتانیاهو: اسرائیل و لبنان دو کشور دارای حاکمیت هستند و حزب‌الله باید از بین برود.
هدف از مناطق امنیتی در جنوب لبنان دور ساختن خطر از شمال اسرائیل است. ظرف هفته‌های اخیر 9000 عضو مسلح حزب‌الله حذف شدند.
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/16216" target="_blank">📅 19:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16215">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeKLx4LVvXAGPq1pZnxIxxcSfxSLpdcsdaLh6tM0GYML8Z7JcZKKJk_o--IKtdK5hd6HvPhU4xzB9bFhVZg7raGvmMSCH9G7G2tcqwzspt2ZjQnQHXfxb30mLZ05iOfhA1dnLQO70794qg50TEU9WwOxeON3Jk-VGBua6NYjYFVNqXgKJt_szo5HKi0HYK4rV4mQ1xLCeHxhplfqCst7lMx3DINqACQQbvYZRnUeEUk-1fdlajmLCG-m-8sQxSeq1jZSUmUfjDfD-LFYOn3AtU6b2bHO3_T2GCYW4KejGj2SiIktqmCyT_c0QBwzcu5uX8EAsDth6M9QFZOtv1oW2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: اولین آیفون تاشوی اپل هم معرفی می‌شود
iPhone ULTRA
اپل احتمالاً در ۸ سپتامبر ۲۰۲۶ از آیفون ۱۸ پرو، آیفون ۱۸ پرو مکس و نخستین آیفون تاشوی خود رونمایی خواهد کرد. به گفته مارک گورمن از بلومبرگ، این تاریخ محتمل‌ترین زمان برگزاری رویداد معرفی محصولات جدید اپل است و در صورت تغییر، مراسم ممکن است یک روز بعد برگزار شود.
آیفون تاشوی اپل، که به‌طور غیررسمی
«آیفون اولترا» نامیده می‌شود، گران‌ترین گوشی تاریخ این شرکت باشد.
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16215" target="_blank">📅 18:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16214">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWhVgwDvWwbAvAwOaPRZgKqdWuH1ocBNIQT4vkiKoFrtFxI63a_cqv5xbRC6rUa3mmGQvVRbVI-Sag_9-ZHZieDYBGly5AGmhUm8D0wZPTQAQV9F7CSvq1Y8BsjWHt0VkHXtE1y1x-qMAOUjFEALeY3VTODfDy3gHDDfU9_5uVIkjEAAib_S-9tD4UvPD0LJmuJpm4CTlWYOqmBGzWbK9oMsHlWRdOkN5zml3aZsHOe3Ggp09z1QxZkFMwU_ltgT5PVSjDO4txONgarpc7kNR3EmltMJbGzo9ppUvwH0iAM8mdUC_qHg6p9zEnckwaFooedeIbxEU2LIbzHt8bSyKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
"پیروزی بزرگ: دیوان عالی ایالات متحده همین حالا علیه حضور مردان در ورزش زنان رای داد و این رای، آن وضعیت مضحک را کلاً منتفی میکند."
@withyashar
یاشار : منظورش مردان تغییر جنسیت داده هست</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/16214" target="_blank">📅 18:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16213">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y69YhraUlCUVhY89XwXhh0PPvnd6AunIF1sTxcR4-F02sodc5gvvg1_9cNqRiCabbCG3D1iIdILdbxv5ecvkedZrhOx3J9GW_JTeesWFrfRZKu4LTFg4LPFE_fhIpu9sM-6m8ewfRPqg5Gz78yKXMAKf6uhjMGhi-m4CGVu3_BICD60Wrd7FTtd8-JKkJj9UMIvdj3sgYOnsLPhwzH7CPbd81cYc-DzoeSivHzJbbZxvfegK5zWjv0qzzn8rO4KkbsaKA2JV4E-fvEFLWulJr670Ry2x0QZOo5AOZ_uWXBODernBUe4VOAVqyPeYk9uI7M8G1g6T8R9jhiFg-G9nRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/16213" target="_blank">📅 18:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16212">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رسانه‌های عبری : «پلیس و سرویس امنیت عمومی اسرائیل (شین بت) یک شهروند آمریکایی را به ظن جاسوسی برای ایران دستگیر کردند.»
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/16212" target="_blank">📅 18:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16211">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
📩
درخواست همکاری  اگر علاقه‌مند به همکاری هستید برای کمک مسیج های قبلی پرید ، لطفاً اطلاعات زیر را از طریق تلگرام برای دوباره به این شکل ارسال کنید:  نام یا لقب نوع فعالیت / حوزه کاری: سابقه کاری: آدرس لینکدین: (خیلی خوبه باشه) آدرس اینستاگرام: (اختیاری) آیدی…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/16211" target="_blank">📅 17:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16210">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وای نت عبری : یک هواپیمای مسافربری شرکت هواپیمایی الکترا ایرویز که با نام تجاری لات به سمت اسرائیل در حرکت بود، پس از آنکه دو جت جنگنده نیروی هوایی به سمت آن شلیک کردند، در هوا چرخید. طبق گزارش‌ها، خلبان دکمه‌ای را فشار داده که هشدار ربودن هواپیما را می‌داد. این هواپیما از ورشو پرواز کرد و در آسمان ترکیه نسبت به ربودن هواپیما هشدار داد. پس از آن، بر فراز قبرس پرواز کرد و پس از عدم دریافت اجازه فرود در قبرس، برگشت و مسیر خود را تغییر داد. مقامات ارشد صنعت هوانوردی این حادثه را بسیار غیرمعمول و خطرناک می‌دانند و تحقیقات فوری در این زمینه آغاز خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/16210" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16209">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آتاانتیک : اسناد منتشرشده نشان می‌دهد با وجود هشدار قبلی ترامپ درباره عدم استفاده از سیگنال پس از یک افشای جنجالی، مقام‌های ارشد دولت او همچنان از این پیام‌رسان برای هماهنگی‌های حساس استفاده کرده‌اند. طبق اسناد FOIA، دست‌کم ۱۳ گروه گفت‌وگوی سیگنال در نیمه اول ۲۰۲۵ فعال بوده که یکی از آن‌ها با عنوان «Iran/Ukraine Planning» به بحث درباره ایران و اوکراین اختصاص داشته است.
این گروه‌ها با حضور مقام‌های سطح بالا مانند مارکو روبیو (وزیر خارجه)، پیت هگزث (وزیر دفاع) و دن کین (رئیس ستاد مشترک) اداره می‌شدند و برخی چت‌ها دارای حذف خودکار پیام‌ها (۸ ساعت تا یک هفته) بودند؛ موضوعی که نگرانی‌هایی درباره نقض قانون نگهداری اسناد فدرال ایجاد کرده است.
در حالی که کاخ سفید استفاده محدود از سیگنال روی گوشی‌های دولتی را تأیید کرده، این اپ برای تبادل اطلاعات طبقه‌بندی‌شده مجاز نیست. با این حال، وجود چنین گروه‌هایی به‌ویژه درباره ایران نشان می‌دهد این پرونده همچنان در بالاترین سطوح تصمیم‌گیری آمریکا به‌طور فعال در حال بررسی و هماهنگی بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/16209" target="_blank">📅 17:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16208">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1345ea8bef.mp4?token=oQLFuYN_8V-yKEDE7e0uGfqlAINFzWGG8DZaiDpAHx4mQB1wm_AlAZYHcDi2jrDgmVBd1BD4S3JH0yzN70X4UvFeSBAGZSAPHNfOuiAST1V9BjzY03lw1XaeIXEtW1FwfJXPfwlNB12_KJ01biIcDrTL-Gc0HtrC6cQHoEs_Y6ejy5w_6vscGirGepJAYSmdadVX8da3nv-oqiWix3czuStfDXyx1NdeG2zBQr67clD9rQT16FdSRdSt58UmiiEszpgQaFaQ587k81_7tTlCk0pxMLiFSvxeKXq3XJegoQpbU40MO_gNI__SmQXkNjPx3XSJjguWg4JCOZHNUixyTkDVKn-1xC6g4T7sifscyVRZcU4EQtzqxNXEHa0RQkImVffr8Fg-Cku_t_CUz4DmUE3OVHaMe40gFaUDpIkq0EES4V-aJhX_MrJYMwZoYSnQLlPXmkLwYnVLA9M9nr3GWUNGCFgXkIXKqrwcUWATl4nPRDBTPuOsST1uwLlWj7byRiV5SkTgTb34bb0FTduwDLRfZmsCLD2yoQdExEgHbEA_mMQpLkXn-bJ3XmQ84pl0lpCtdunFHWIMOfmZCn-jizuhcXrY8xoATTmUVT7YTTCahQKrBxORJXFNKAIWX4VKpfu5WjwVYbVhOPb6PoJw8m3vVgBj8cpLlCUcWXF0Y_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1345ea8bef.mp4?token=oQLFuYN_8V-yKEDE7e0uGfqlAINFzWGG8DZaiDpAHx4mQB1wm_AlAZYHcDi2jrDgmVBd1BD4S3JH0yzN70X4UvFeSBAGZSAPHNfOuiAST1V9BjzY03lw1XaeIXEtW1FwfJXPfwlNB12_KJ01biIcDrTL-Gc0HtrC6cQHoEs_Y6ejy5w_6vscGirGepJAYSmdadVX8da3nv-oqiWix3czuStfDXyx1NdeG2zBQr67clD9rQT16FdSRdSt58UmiiEszpgQaFaQ587k81_7tTlCk0pxMLiFSvxeKXq3XJegoQpbU40MO_gNI__SmQXkNjPx3XSJjguWg4JCOZHNUixyTkDVKn-1xC6g4T7sifscyVRZcU4EQtzqxNXEHa0RQkImVffr8Fg-Cku_t_CUz4DmUE3OVHaMe40gFaUDpIkq0EES4V-aJhX_MrJYMwZoYSnQLlPXmkLwYnVLA9M9nr3GWUNGCFgXkIXKqrwcUWATl4nPRDBTPuOsST1uwLlWj7byRiV5SkTgTb34bb0FTduwDLRfZmsCLD2yoQdExEgHbEA_mMQpLkXn-bJ3XmQ84pl0lpCtdunFHWIMOfmZCn-jizuhcXrY8xoATTmUVT7YTTCahQKrBxORJXFNKAIWX4VKpfu5WjwVYbVhOPb6PoJw8m3vVgBj8cpLlCUcWXF0Y_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت دفاع اسرائیل و شرکت رافائل در بیانیه‌ای اعلام کردند با توجه به تجربیات دو جنگ اخیر با ایران، سامانه‌های پدافندی گنبد آهنین و پرتوی آهنین را برای مقابله بهتر با پهپاد‌ها،راکت‌ها و موشک‌های کروز ارتقا داده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/16208" target="_blank">📅 17:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16207">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">روزنامه لبنانی المدن گزارش داد:
توافق‌نامه امضاشده میان اسرائیل و لبنان در پایان هفته گذشته به
قطع روابط دیپلماتیک ایران و دولت لبنان منجر شد‌ و عباس عراقچی در پی امضای این توافق‌نامه، سفرش به بیروت را لغو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/16207" target="_blank">📅 16:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16206">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اتاق جنگ با یاشار : بعد از خبر تشکیل نشدن جلسه جمهوری اسلامی و آمریکا تتر شد ۱۷۲،۵۰۰+ و بیتکوین به زیر ۶۰،۰۰۰$ و همکنون ۵۸،۵۰۰- اومد و نفت برنت +۷۴$ شد
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/16206" target="_blank">📅 16:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16205">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الحدث: منابع می‌گویند ایران تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/16205" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16204">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ستاد مراسم دفن خامنه‌ای: مردم برای نزدیک شدن به جنازه علی خامنه‌ای اصرار نکنن.
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/16204" target="_blank">📅 15:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16203">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سخنگوی وزارت امور خارجه:  فردا در دوحه با قطری‌ها «دارایی‌های مسدود شده» مذاکره خواهیم کرد. @withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/16203" target="_blank">📅 15:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16202">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXI_QhZsaH59P3WOHEGo3QaoNYPpa3J_pQW-wU4hahwZrtLN1MfoI1rkk_e4fxQ8fg89tTN5kIiGPl0Jh6cb48T3MbpqKCBvtn7CrLE7uco67yt8yjIiNkcLEiTs-nJbhIqNhbsDwMDPreOSUzIVFeBNHNfJG9TEYGKQMX7jValI8c83ToXw7ATw0njpLmQFBtT2OQ_HxTK0gOHF8pTdnzIuU0VWbyNH2YUui1EcNqU9fm-LOYN_iB-bqCzayDfNiqUpFx0RRspmBYGhUoEV5JpC9HK2_u3hNggHeISZEuaOC5GMLmsmgUrUpDOX4nwBAMS9j0xAmB9lXN8stoKfJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانا کوآکو بونسام، جادوگر مشهور غنایی :
کیپ‌ورد آرژانتین رو حذف میکنه
،
من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/16202" target="_blank">📅 15:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16201">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سخنگوی وزارت خارجه:  آمریکا صراحتاً دربارهٔ پایان جنگ در لبنان تعهد داده و باید به تعهدش عمل کند. @withyashar
😂</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/16201" target="_blank">📅 15:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16200">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سخنگوی وزارت خارجه:
آمریکا صراحتاً دربارهٔ پایان جنگ در لبنان تعهد داده و باید به تعهدش عمل کند.
@withyashar
😂</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/16200" target="_blank">📅 15:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16199">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVDH3QIfgANGAdrY0HqlMrddHmKygCiw9Fhh8_546Fh-mVJdxr0fvAjluZyS8rTqTvOvHmFh_6KWTAvT2g3tuY2g4raOD0d06GHFzQzemjGL-P67yrE5NYcZellHMXb634Ome8ITqoXOMuCvS9AiTTxM47ZiC7Ft2r3ZXYNBDySWTBVDd5PbOWwp9Pz-gQgdIpzeI-134xtA5cMrpDIpRW3_1cpOt5QxPBygqdeaxAP8Om-IDF5m1dQrLbthqqocdx3kjYJu-noaBnVOPHVv-yn9-q2DnAX5iCkB_gQNjQqpYlXC7gAACMFmBZYGTZWvk8qm4_IK_GVuatm4i1Sugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر وایرال شده از تعزیه محرم
قیافه بعل یه جوریه که داره میگه خب عاشورا من چه کاره‌ بودم
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16199" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16198">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دبیر ستاد تشییع جنازه خامنه‌ای :
مجتبی بخاطر تهدیدات دشمن نمیتونه تو نماز میت پدرش شرکت بکنه و باید مخفی بمونه
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16198" target="_blank">📅 14:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16197">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فاکس نیوز : ویتکاف و کوشنر به سمت قطر حرکت کردند  @withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/16197" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16196">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر : هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/16196" target="_blank">📅 14:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16195">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUESteEhmQMgN5pEOs9_u_J588EAid7c4c7MY8UMxYSrVXVuWpxzbsfw6gBp1GiAPbMZJAy8RJrVvz_wlA51P59yj8WQ7-ULREECop-l7f-gkrTNwd1YJ6zS_ApJJ5WsXG7AaPpEl7x5gch5zobfr0fRUA0kFDPXQh1JQ6rMjTSLfq-Z6X4Ak8GQ4rFQ4K7CZ8eRsnvKD3RKklrM_z3bBezIpnCx45JdA2v_QiJqE_VeS9L66r8M_q308JbNVV0jvVisNnHVKW3KQ6RPjOX2XzXbqAJDB7CnRegwT_pIqm4MbeVMYJF3mvNFd2JumWNHHSymXYeV-e8fW__Z-jwDFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی هوایی آمریکا موشک ضدکشتی LRASM را با بمب‌افکن پنهانکار B-2 عملیاتی کرده و در رزمایش Valiant Shield 2026 با آن یک شناور آبی‌خاکی بازنشسته را غرق کرده است.
در حالی که B-1B از قبل این موشک را حمل می‌کرد، تلاش برای افزودن آن به B-52 و P-8 ادامه دارد، اما B-2 فعلاً تنها پلتفرم برد بلند پنهانکار برای شلیک آن محسوب می‌شود.
ترکیب برد بلند LRASM با پنهانکاری و سنسورهای B-2، توان حمله دقیق و دورایستا را افزایش داده و تهدیدی جدی‌تر برای ناوگان‌های دریایی، به‌ویژه در اقیانوس آرام، ایجاد می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/16195" target="_blank">📅 12:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16194">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزیر امنیت داخلی آمریکا:
پس از حذف ایران از جام جهانی رقصیدم
روزنامه نیویورک تایمز گزارش داد، مارک‌وین مولین، وزیر امنیت داخلی ایالات متحده اعلام کرد که پس از حذف تیم ملی ایران از مرحله گروهی جام جهانی ۲۰۲۶، «رقص شادی» کرده و حتی «چند آهنگ» خوانده است.
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16194" target="_blank">📅 12:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16193">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یک منبع آگاه غربی:
ممکن است اسرائیل ابتدا در هفته های آینده وارد جنگ با جمهوری اسلامی شود سپس ایالات متحده آمریکا به اسرائیل ملحق خواهد شد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16193" target="_blank">📅 11:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16192">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وال‌استریت ژورنال گزارش داد که مارکو روبیو، وزیر امور خارجه ایالات متحده، توانسته است دونالد ترامپ را متقاعد کند که اسرائیل باید حضور خود در لبنان را حفظ کرده و علیه ایران اقدام نظامی انجام دهد.
در همین حال، جی‌دی ونس، معاون رئیس‌جمهور، ناچار به عقب‌نشینی از موضع خود شد و در نهایت اعلام کرد که از توافقی که با محوریت اسرائیل شکل گرفته حمایت می‌کند، نه از ابتکار عمل ایالات متحده.
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16192" target="_blank">📅 11:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16191">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9kg3GUZyfBZEeG3u0Svc8SXuwuxVAbgMhbhY_l1nvNwts8gc1dft343A04-MQA2zCFz46s8098jUaORamJhX7ZEBBDxpGbRCqi783Ex9nBBR9isRly4uMyhYEXumN-nbcpoUQORc0r7JrwUrcW9Zd4hNojS4Xqxytg1bs9WpdWhN_8-fMcdLfwIn9hn-JG19MUlFa0mMGehgG3iJyUboYDwozO1WO91OoDiFEuRusp98uIZxLWcUGJZyPfn2xjujzlCqc0vGtDLLswPl9zA-JKT4bFY4I0hJcW__dXQUwQlwK9l9k6kkbu9X78Rliy9WnKySW9ZiutLzDGSclRXjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین تصویر ثبت شده از محمد اکبرزاده قبل از تصادف و مرگش
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16191" target="_blank">📅 11:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16190">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAfDRgbLtqpA4Fm5FFvyeMzHSHb5nUfWaDwXU-wk39z-pDiiai2YRhox4Rt4nIhdn2YnEBcfQsx_KIIICUprsVTTkcMoAOEVHcUyGptFd6h5LF3Fs5Jw21M2b-GlJwMCrKWUI2BqHkfb30M-dRB913s7njauBaNEFmwSvk_Hb67foaAFdZWrG3DR64w9BxETIyzf8DRGhlaDhgrF7qDyZBVbS2KnSobtJCkAHmTAk6yYhBRGPjvy11iCGeL-CeQvtew2nAZ3Gh7s_E-hDEWZm1J-XQBQ-c4GEPSK65dF4gKXYkQ8IqWlnql4TVvVEZzakAf5MmbVVxpbzWz3xlQf0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان انفجار مهیب و برخواستن دود از سمت فرودگاه شیراز
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/16190" target="_blank">📅 11:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16189">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اسرائیل در حال آماده شدن برای شروع مجدد جنگ تمام‌عیار علیه ایران
بر اساس اطلاعات موجود، اسرائیل در حال آماده‌سازی یک کمپین مستقل برای آغاز دوباره جنگ تمام‌عیار علیه ایران است. این تحرکات نشان می‌دهد تل‌آویو مسیر جداگانه‌ای از آمریکا در پیش گرفته و انتظار می‌رود در آینده بسیار نزدیک وارد فاز عملیاتی جدیدی شود.
در همین حال، فعالیت موساد در داخل ایران به‌طور محسوسی افزایش یافته و شتاب ناگهانی این تحرکات، از تسریع آماده‌سازی‌ها هم‌زمان با عملیات مستقل اسرائیل حکایت دارد. هم‌زمان، انتظار می‌رود در روزهای آینده موارد بیشتری از انفجارهای مرموز، آتش‌سوزی‌های صنعتی و حوادث مشکوک در داخل ایران رخ دهد؛ رخدادهایی که با الگوهای تاریخی خرابکاری و عملیات پنهانی موساد هم‌خوانی دارد.
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16189" target="_blank">📅 11:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16188">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبی خاکی باکسر داره میاد !
۴ ناو ۱ آرایش رو به جلو و آماده به سمت خاورمیانه
یو اس اس باکسر، یو اس اس پورتلند، یو اس اس جان ال. کنلی و یو اس ان اس پیلیلائو در آرایش جنگی در اقیانوس هند حرکت می‌کنند و تحرک و پایداری آبی-خاکی را در دریا نزدیکی سریلانکا به نمایش می‌گذارند
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/16188" target="_blank">📅 10:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16186">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5553987fa9.mp4?token=oGNQcbquVCwefwkhoT0kZQA7pL_BGwxqsstebuxRTFvb2ka-UKVz4qsI28R0DZ_J0EpluDlzHJ55WqhxG9GArbrf21KvFOObqQytJaXdljvctXT08CiMEoQlbd2Im7wX0MvGhIVh9Ofe8-gw7Cw_B4HsnCTH2AQ0TPJTlJ31MisAhPJu6Q8TNnigfor9ynBt8vsoxDvAk5tqDua5WWRN0BQ-2z_ErrvHO2UXJL-tTJjx5YIssvSnerC7M9m252LQZUQeUBsZuoQN7NY7qjHgk6X_NiyAkcqYrwzoVG0-kHMpAfFa02FoGWLn9ZQWZi3Z08eJctTbIQIUKaHq3mptTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5553987fa9.mp4?token=oGNQcbquVCwefwkhoT0kZQA7pL_BGwxqsstebuxRTFvb2ka-UKVz4qsI28R0DZ_J0EpluDlzHJ55WqhxG9GArbrf21KvFOObqQytJaXdljvctXT08CiMEoQlbd2Im7wX0MvGhIVh9Ofe8-gw7Cw_B4HsnCTH2AQ0TPJTlJ31MisAhPJu6Q8TNnigfor9ynBt8vsoxDvAk5tqDua5WWRN0BQ-2z_ErrvHO2UXJL-tTJjx5YIssvSnerC7M9m252LQZUQeUBsZuoQN7NY7qjHgk6X_NiyAkcqYrwzoVG0-kHMpAfFa02FoGWLn9ZQWZi3Z08eJctTbIQIUKaHq3mptTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قنبریان سخنران صداوسیما: اگر ترامپ را قصاص نکنیم رهبر فعلی باید بدون شک تا ابد در مخفیگاه باشد
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/16186" target="_blank">📅 10:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16185">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldzFbwmI2hb-w3wopI8eHFTQ-va7G3Btxu1TiYatsKByIfPZ86myv9HNPHfkhquDs8U7YcFSERXV5GncX4_8NkihpY5lzTgWP5uvlO7351bxPc23scLkjsOn3ryofAVCMM9-AwYX2d2zn5ExboLTdZOWAVCAqkJdhGwOxjg8QoKeKwJfjJMS7RieFWMT1FygkYanTiVPPeur8vp_L3MOL-8CjY8XbQCRUGu62jqoeol7f26whQ3OE-RRVc5JGXfaqn9T4DUavLTUjvtPHSQd_SVbbtcpBaLUl3CNG_X2gp2tmY2oBZYFhGc6dmUT6bTeHDUlBvs7dzXvd3e-bo-AjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو نیروی سپاه پاوه ترور شدند
روابط عمومی سپاه استان کرمانشاه:
طی اقدامی، افرادی با تیراندازی درب منزل در شامگاه دوشنبه هشتم تیرماه، «برهان کریسانی» و «خالد خالدی‌نیا» دو تن از نیروهای بومی ما را هدف قرار دادند
در‌این عملیات خالد خالدی نیا بهمراه خواهر و خواهر زاده‌اش کشته شد﻿
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/16185" target="_blank">📅 10:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16184">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسناد محرمانه هک شده مادربرد و تراشه جدید آیفون ۱۸ پرو مکس فاش شدند.
بیش از ۶۳۰ گیگابایت اطلاعات از جزئیات کلیدی آیفون ۱۸ پرو و آیفون ۱۸ پرو مکس اپل به سرقت و فاش شد.
رویترز : فایل‌های حساس شامل فهرست قطعات و تأمین‌کنندگان، و حتی عکس‌هایی از مدل‌های در دست‌توسعه آیفون 18 پرو از طریق نشت داده در شرکت هندی Tata Electronics توسط هکر ها روی دارک‌وب منتشر شد.
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/16184" target="_blank">📅 10:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16183">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حزب‌الله:
قمار سر توافق ننگین بی‌نتیجه است
حسن عزالدین، عضو ارشد فراکسیون وفاداری به مقاومت در پارلمان لبنان:
صهیونیست‌ها مکان‌هایی را در به اصطلاح
مناطق آزمایشی
گنجانده‌اند که اصلاً جای پایی در آنجا ندارند مانند شهرک فرون.
دولت لبنان اساساً خودش را فروخته
و به دنبال فروش قدرت لبنان است.
پرونده لبنان همچنان در اولویت ایران قرار دارد
و جمهوری اسلامی ایران این پرونده را به هیچ طرف دیگری واگذار نخواهد کرد. معادله‌ای که تهران ایجاد کرده همچنان پابرجاست و ادامه می‌یابد.
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/16183" target="_blank">📅 09:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16182">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شروع حذف‌های هدفمند؟
دریادار دوم محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه، متولد ۱۳۵۰ بود و در زمان سانحه رانندگی و درگذشت(دیروز)،حدود  ۵۵ سال داشت. او تازه سه هفته پیش، در روز دوشنبه ۱۸ خرداد ۱۴۰۵ معادل ۷ ژوئن ۲۰۲۶، در فهرست تحریم‌های اتحادیه اروپا قرار گرفته بود!
وی در ماه‌های اخیر در سخن‌رانی‌ها و مواضع مرتبط با امنیت خلیج فارس و نظارت بر حضور نیروهای خارجی فعال بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16182" target="_blank">📅 09:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16181">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دیوان عالی آمریکا امروز سه پرونده سرنوشت‌ساز برای دولت ترامپ را تعیین تکلیف می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/16181" target="_blank">📅 09:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16180">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2b4B7gIkUm8Zhbrsoh8DVVLUXXyuMK0KoQR_ULX-AeHHNYD_fW6d0OomqAAU-2dAtFn_tLo0T_cNfknWvldtUM6dybUlz-WFLimqbz7PtWb_t1kn8_SdILg2JMN0UdQMMPyPKoaQRyOiU3PVPzvAIh2qpVyjIbiwyCDt2OSIbEq-utH1TdDH0WWIScGHVIi-yd_Ecj1gWQL-Ft1F5yZuZWDaVeXOXn6oj9N5W_zsSAF9wce8_YagZUH4DCCrYKY5e9w8kv8OATsh-lfeMFhXSYJRcwwMB6DoYlJko3iHIfhD0qN9c6FfZV5GgvIoWgqaP2-IVmvjS1vOPA4-oet9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید روزنامه همشهری :  انتقام قطعی است
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/16180" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16179">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">روبیو: احتمال شکست مذاکرات با ایران وجود دارد
شبکه «ام‌اس ناو» به نقل از منابع مطلع: روبیو در جلسه توجیهی با اعضای کنگره آمریکا، گفت که دولت ترامپ هیچ توهمی ندارد که مذاکرات با ایران آسان خواهد بود.
روبیو به کنگره گفت که احتمال شکست مذاکرات وجود دارد، اما دولت می‌خواهد به مسیر دیپلماتیک فرصتی بدهد.
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/16179" target="_blank">📅 09:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16178">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ به شرکت‌های نفتی: «قیمت‌ها را کاهش دهید - وگرنه مشکلات بزرگی پیش خواهد آمد!»
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/16178" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16177">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFyGJPob7muFi3P70LVVzwHftaFBkCY2XmkXCcY-l6akOhg3Naio9sgX_QfaTB5yVImW075srS7J66z-I1A682RoxTwlzkZBPvoB-pphzrI7Dp7L_G3Y1F1sRvvADjKc8cwa4yTFtbIGRpH7nkrZYuky5F51Ttr4sGRcVTkJ9vy1fYA2zrW--aOPYZOei-tb1qsDt7heSwQR3gncKsCbcglI4H1-iK5KZbgB3RlBJ97pj1wekCb7T3PFuDPlGnYDk9qPajEeHfoVIA_0MglOyqwanpEZ_mgxqLLRSHzxgDZZd43jvgyaRXXfT3Jjv4tVQrztARKIPmH8SwTcImAEDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار هدفمند در موناکو فرانسه
۳ اکراینی نفر زخمی شدند که حال دو نفر از آنها وخیم است.
پلیس در جستجوی مظنون فراری پس از انفجار «هدفمند» در موناکو است که شامل یک وسیله انفجاری جاسازی شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16177" target="_blank">📅 08:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16176">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حمله مسلحانه به ایست بازرسی پاوه در کرمانشاه باعث کشته شدن 3 سپاهی شده که یکی از این افراد نقش مهمی در قتل عام مردم در سال 401 داشت که به هلاکت رسید
@withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/16176" target="_blank">📅 08:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16175">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهو : اگر از غزه خارج میشدیم، خامنه‌ای، نصرالله و اسد الان در قدرت بودن.
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/16175" target="_blank">📅 00:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16174">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egUFcKB7DNKUVcYbUXCzLmEqoqAwKqhmnnFpN9wvtCwYMr9-SynWiX8hqzdUheLrtqXDq9F8gzjXvZTlJQHiKlIqPyVC7UjrLblc1-wyL7XkgLzzkWYbozcbc2dAKKASoG7Fk1HzAfppithmgPaK5JNDMDenGVBHiP_7db9QVCjd31mu7SqFitca6B230I24gVjGU6cHUaKUxTBhEn1WDQRJyKa4_czsO9wa_10RGknp-UCQB6VjMECKAGSIweKZGgPtzYgwu9kJSjWsU2oDmEr5FYUmGWXRFG6R9vJmIS7fbXw0aO_N0QmZ6uzEu4jIL53cyzWOptpAO8FqHrjrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات سنگین اسرائیل به مواضع حماس در خان یونس
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16174" target="_blank">📅 00:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16173">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAWpKRPBaIXcsm236djpajjtWx2d6tUnF9hK9s55cSIAn1C-KCaQZVaIXKk-V5ozPc2KfmnLFWmy--_VN_Q3WjBQhOTLnZF-on1PwEhfFycYfKN4F8hBjCcLgB6S62tKDPwQp3yXrfqUbywi23lPqJaGHXtBTmfvQxcyeYjbGCg0HJFwsUNTTrsvPAXaJ6FyCoPVFFJEUOLzq6GCAYH8390TUagzxNapAnyfjKf3duNgfXwOS8XZLGkBEl9XW9E8b3orypIRl008krpF1qlcBsQ3v58T2UcUhEAoE7HJMw1WPl_cPLJazWDh-emczIkGsCudYOPJ2X4UuC7-7PQVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید باور نکنید ولی؛
امیر قلعه نویی قبل از شروع جام جهانی از فدراسیون فوتبال
۱ میلیون دلار
پاداش طلب کرده بود و فدراسیون پرداخت کرده
۱میلیون دلار هم بازیکنا و سایر اعضا دریافت کردن
اول یک میلیون دلار (۱۷۰ میلیارد تومن) رو گرفت بعد نشست رو نیمکت.
نتیجه: حذف در مرحله گروهی در آسان ترین گروه.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16173" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16172">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وزیر دفاع اسرائیل:آغاز جنگ مجدد با ایران ممکن است در عرض 2 روز آینده رخ دهد و ارتش اسرائیل آماده عملیات و هدف قرار دادن اهداف در ایران در صورت شلیک موشک‌های بالستیک در پاسخ به نقض‌ها در لبنان هستند،اسرائیل در حالت هشدار قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16172" target="_blank">📅 23:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16171">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">موافقت عمان با اخذ هزینه خدمات دریایی
وزیرخارجه عمان تفاوت میان عوارض عبور و خدمات دریایی، زیست‌محیطی و مالی را توضیح داد که می‌توانند به‌طور داوطلبانه با کشورها و شرکت‌های ذی‌نفع مورد بحث قرار گیرند.
او افزود که برخی خدمات ممکن است شامل افزایش ایمنی ناوبری، حفاظت از آب‌ها در برابر آلودگی و ارتقای آمادگی برای مقابله با حوادث یا شرایط اضطراری باشد.
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/16171" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16170">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a48fb273.mp4?token=nlZ3cY9jSk8yplqLuBadw6W1NLwOPdigO-WJGaXZ96xbskP6wXdvLuqppxCa0TQlhiqMSJy-XzJq762DlAaTAwByLZldFsil5xLlQKDSOeQvHbSmuwwq3_2F8oCiwN71i-5tVQsMQU5QCSPM2FvplwpKWXYP5PUIny4Kt5YZh6aWH3tq_FlEdeR7LKjz3JCdSstuV8G2nITDV-k7bPv6WbgN480XIz7Ofuafna-L2ZPVp3a7k4M6lfYBjikRcTq7R4bxfnz5sldPuNLqQ9psi9QvhQhB5zTBtNCwZv4gvUMfuURGiEFLtw5Z37W_gWrY7hBNsGUalEyNpo34xY240w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a48fb273.mp4?token=nlZ3cY9jSk8yplqLuBadw6W1NLwOPdigO-WJGaXZ96xbskP6wXdvLuqppxCa0TQlhiqMSJy-XzJq762DlAaTAwByLZldFsil5xLlQKDSOeQvHbSmuwwq3_2F8oCiwN71i-5tVQsMQU5QCSPM2FvplwpKWXYP5PUIny4Kt5YZh6aWH3tq_FlEdeR7LKjz3JCdSstuV8G2nITDV-k7bPv6WbgN480XIz7Ofuafna-L2ZPVp3a7k4M6lfYBjikRcTq7R4bxfnz5sldPuNLqQ9psi9QvhQhB5zTBtNCwZv4gvUMfuURGiEFLtw5Z37W_gWrY7hBNsGUalEyNpo34xY240w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در‌ مورد کمونیست:
آنها مردم را به خاطر تعمیر ماشینشان دستگیر می‌کردند.
این حتی باورکردنی نیست
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16170" target="_blank">📅 23:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16169">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6615611a73.mp4?token=ihR8F0hucNEGCqplrHS5TxMh4c6tpS9E9J4mX-6m9Asbh_x4y9rTLw-92WWdpmWSJ-VpDFFZolGyHVsDwbZBvx1_HzRfuZOhvxW9Xc0DbnRnkksp-M330wCTDCqWIZADwMeA07mJsUDN0Dk6r2pNnDJBXy7G5I4Y5IgtK0HdJGB-JfEa_KwljQmw2nbCV0A-ADb9pLI4RSFDZhOe3Yai7gFjxDbiqsOIpW4EYrPcxZsyBvi5cpRGXnOlxmKKJ4TGB7yX4OzxMWtfJIJ-O5-zgb8FMfyhcjYzUJwMKfbhJo8B4gUcqFnrNfJ-Kb3CPuIBRbQ0fdriRkcnBjuziRG2Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6615611a73.mp4?token=ihR8F0hucNEGCqplrHS5TxMh4c6tpS9E9J4mX-6m9Asbh_x4y9rTLw-92WWdpmWSJ-VpDFFZolGyHVsDwbZBvx1_HzRfuZOhvxW9Xc0DbnRnkksp-M330wCTDCqWIZADwMeA07mJsUDN0Dk6r2pNnDJBXy7G5I4Y5IgtK0HdJGB-JfEa_KwljQmw2nbCV0A-ADb9pLI4RSFDZhOe3Yai7gFjxDbiqsOIpW4EYrPcxZsyBvi5cpRGXnOlxmKKJ4TGB7yX4OzxMWtfJIJ-O5-zgb8FMfyhcjYzUJwMKfbhJo8B4gUcqFnrNfJ-Kb3CPuIBRbQ0fdriRkcnBjuziRG2Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ما از نظر نظامی در حال پیروزی هستیم. به نظر من، تقریباً از نظر نظامی پیروز شده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/16169" target="_blank">📅 23:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16168">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82e78ece16.mp4?token=b5FMgB0KL8Pel3kKiiuBuUtWWXd52ozSVEfkksG4OaZS18BUsqmVjyiASjTm09jXW2vuXdVtgxS6KmYdEsP758P931HqSDdZhp821MtAu3kt_tqqaTss7IHBeC0ZxJIfOBWACR0qkA376MDOahck3RHpDtudAJ2HyBfN0yNcFcpxjz8BbGZHRyIInlxCWv4KKcoW0Jl_qhyvOoJDqH-EzemQ4mS5deaCwzAkkr5rThI0f0UEqFfulYYVntA6bAaShKU84zsHiVgOyg7gtgYs2bfjxeXMXDbDrB66pmo5TiLtlBecFQzcz2uQU0F63LP97rdWYFiQHVtbZj8xA1a3IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82e78ece16.mp4?token=b5FMgB0KL8Pel3kKiiuBuUtWWXd52ozSVEfkksG4OaZS18BUsqmVjyiASjTm09jXW2vuXdVtgxS6KmYdEsP758P931HqSDdZhp821MtAu3kt_tqqaTss7IHBeC0ZxJIfOBWACR0qkA376MDOahck3RHpDtudAJ2HyBfN0yNcFcpxjz8BbGZHRyIInlxCWv4KKcoW0Jl_qhyvOoJDqH-EzemQ4mS5deaCwzAkkr5rThI0f0UEqFfulYYVntA6bAaShKU84zsHiVgOyg7gtgYs2bfjxeXMXDbDrB66pmo5TiLtlBecFQzcz2uQU0F63LP97rdWYFiQHVtbZj8xA1a3IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: نشست دوحه شاید مهم باشد، شاید هم نه؛ خواهیم دید
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/16168" target="_blank">📅 23:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16167">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کانال ۱۲ اسرائیل : وزیر دفاع اسرائیل، کاتز، دستورالعملی از ارتش اسرائیل بر آماده‌سازی «عملیات آبی و سفید» برای یک کمپین احتمالی علیه جمهوری اسلامی اعلام کرد و تأیید کرد که اسرائیل تا زمانی که «خلع سلاح سازمان‌های تروریستی» انجام نشود، مناطق امنیتی در غزه، لبنان و سوریه را ترک نخواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/16167" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16166">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برخواستن جنگنده از مهرآباد
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16166" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16165">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a561d8b149.mp4?token=cYVi0f2D72OvLVf5oPvyu34vG6VxN6Futj36_YrA3I7uJlprNXHBbWyrF-Vk2R_zkwoj1DBTNsTDznncH3CMd_mK0zAIOXr7ZyNtsHAP1mxhGj5WW_l5aDuIvSo-HJLvQQYCNK-HsXk5CJCzoB3SGjfE89iYhYtzGA78XZIyHh3c9WCxDRBpQH56RfqWb5HW0NeQmWi9YlqWRoqgLEomJZmb2zXvzViEAWJaVnoinyZ28F6q-RPKx242yEcKiQCi4J41VGHRve-hlZ9AXN8tX-dqCceq8mNTCCNQ88gt66wRgLV0EDTkajgHX9UE1oYrgmcj_Ffu-TrQFhfAFB5CDbZGotyvcp8b5EZhyFJeAJE204UHnjw5RtB03iH6qcpUbgX2eSdCGQLX17W1YsJLwa1LbZZIZcyHkPxJ4pzHRIqukC_UtOGjopjmYoU-PpMqk3qsi6MYGnUduZBefotMoP8R8Nrorn82fJS-O-9YGUgHp44V_JCNbtQ5KvkGqDgj1lAo_8U987HWuarpoK9-Ybv6WFU5nRl4gTW2dsMnFeUgDKkxL-SYwAh3ThNyh3oatAt7LAFBRJv-3vrePv5059OQCJ_nWvPrFuWDH23WQVm_zzjFsoLuLdjttod1m8XOKgHKzb01tbjpKWxFoLT_pq_bhXdkV-g5MPvecUQhKHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a561d8b149.mp4?token=cYVi0f2D72OvLVf5oPvyu34vG6VxN6Futj36_YrA3I7uJlprNXHBbWyrF-Vk2R_zkwoj1DBTNsTDznncH3CMd_mK0zAIOXr7ZyNtsHAP1mxhGj5WW_l5aDuIvSo-HJLvQQYCNK-HsXk5CJCzoB3SGjfE89iYhYtzGA78XZIyHh3c9WCxDRBpQH56RfqWb5HW0NeQmWi9YlqWRoqgLEomJZmb2zXvzViEAWJaVnoinyZ28F6q-RPKx242yEcKiQCi4J41VGHRve-hlZ9AXN8tX-dqCceq8mNTCCNQ88gt66wRgLV0EDTkajgHX9UE1oYrgmcj_Ffu-TrQFhfAFB5CDbZGotyvcp8b5EZhyFJeAJE204UHnjw5RtB03iH6qcpUbgX2eSdCGQLX17W1YsJLwa1LbZZIZcyHkPxJ4pzHRIqukC_UtOGjopjmYoU-PpMqk3qsi6MYGnUduZBefotMoP8R8Nrorn82fJS-O-9YGUgHp44V_JCNbtQ5KvkGqDgj1lAo_8U987HWuarpoK9-Ybv6WFU5nRl4gTW2dsMnFeUgDKkxL-SYwAh3ThNyh3oatAt7LAFBRJv-3vrePv5059OQCJ_nWvPrFuWDH23WQVm_zzjFsoLuLdjttod1m8XOKgHKzb01tbjpKWxFoLT_pq_bhXdkV-g5MPvecUQhKHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیم
ا
: جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@withyashar</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/16165" target="_blank">📅 22:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16164">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، گزارش داد
محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه پاسداران، در یک «سانحه رانندگی بر اثر واژگونی خودرو» در یکی از محورهای استان کرمان کشته شد.
فارس نوشت پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و اکبرزاده به مرکز درمانی منتقل شد، اما به دلیل شدت جراحات جان باخت.
این رسانه وابسته به سپاه افزود بررسی علت و جزئیات این سانحه از سوی مراجع ذی‌ربط آغاز شده است.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16164" target="_blank">📅 21:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16163">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCP__k0IbshMKsVaU1VTvRcMf_1ccBO91r1MxUzR0gIXxeD-G0yPABQ5wvIOATQnPp6xkZ9PxkSd69sgGh_aM7yp1k_uoLFRq7aBHru9mIqNU5i4qQzG520t68K_3YdHn3nZSg7RMuZj1RWRm3J8Mqeazi_Z_dH7UVVz8_tpOJdj-rClFa_lWQAURuvpssBju7WubJHCcUdYG09ldI3MWbHujLjSzDsNMjcK80D5DTUuusmmxW1mdzieV_Gj7TKwUhIOb2HhfWtYc7x5g4kqqbJ4EwmuWi064lyqDLAdLKOORtvJlsm__ocL3TgiCaVhGYQVvSTvY_2Ad3dVlKz9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون پیام هشدار سفر از طرف سفارت/کنسولگری چین
🚨
🚨
🚨
🚨
«وزارت امور خارجه چین و سفارت چین در ایران به هم‌وطنان چینی توصیه می‌کنند که در
حال حاضر از سفر به اصفهان ، قم ، مرکزی ، بوشهر و مناطق دیگر خودداری کنند
. لطفاً وضعیت امنیتی محلی را با دقت دنبال کنید، از مناطق با تنش و درگیری بالا دوری کنید، سطح هوشیاری را افزایش دهید و تدابیر امنیتی را تقویت کنید.
رعایت قوانین محلی، خودداری از حمل مشروبات الکلی، گوشت خوک و سایر اقلام ممنوعه در هنگام ورود، و پرهیز از عکس‌برداری در مکان‌هایی غیر از نقاط مجاز ضروری است. اگر امکان استفاده از کارت بانکی، کارت اعتباری یا چک مسافرتی ندارید، از پیش برای آن برنامه‌ریزی کنید. برای اطلاعات بیشتر، اپلیکیشن “China Consular Affairs” را دانلود کنید.
شماره اضطراری در ایران: 110
شماره امداد: 115
خط اضطراری جهانی وزارت امور خارجه چین برای حفاظت کنسولی و خدمات: +86-10-12308 / 65612308
شماره کنسولگری سفارت ایران: +98-9122176035
شماره کنسولگری سفارت ابوظبی: +98-9914240393
اداره فرهنگ و گردشگری چین در بخش گردشگری نیز توصیه می‌کند: “سه رعایت، سه نه” یعنی امنیت را آموزش بدهید، ادب را رعایت کنید، به بهداشت توجه کنید؛ سر و صدا نکنید، بی‌نظمی ایجاد نکنید، و قوانین را نقض نکنید.»
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16163" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16162">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/16162" target="_blank">📅 20:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16161">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">معاون وزیر امور خارجه:
ایران به تنهایی عملیات پاکسازی مین‌ها از تنگه هرمز را طبق یادداشت تفاهم بر عهده خواهد داشت.
هیچ کشوری در پاکسازی مین‌های تنگه هرمز با ما مشارکت نخواهد کرد و از نظر اصولی اجازه این کار را نخواهیم داد.
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/16161" target="_blank">📅 20:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16160">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یک مقام آمریکایی: ما به ایران به‌روشنی توضیح دادیم که تنها در صورت تحقق پیشرفت در پرونده هسته‌ای، دارایی‌های مسدودشده این کشور آزاد خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/16160" target="_blank">📅 20:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16159">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه با فرمول پس زدن خاک از اجزای خامنه‌ای وضعیت رو نگاه کنیم ، با توجه به اتفاقاتی که داره می‌افته، این فرضیه درمیاد که یه درگیری دوباره پیش میاد تا این تشییع انجام نشه ! و اینا مثل فوتبال در دقیقه ۹۵ ضایع بشن ! و هی زجر بکشن…
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/16159" target="_blank">📅 20:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16158">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سفارت ایران در قطر : قصد مذاکره با آمریکا را نداریم.
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/16158" target="_blank">📅 19:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16157">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68787096d3.mp4?token=RzjD8lD1W0DAG2179L7WDCmm5VlfZQZ8vrN-1DTAAGfkcHXMSKOdDipT9HfJEJ_1IXVZhKc17j6VkSGeRIh6Rcft5k5UpXp84wzCcB94sNAa_DGSBRq74kCsNi5IHDqpT-YbhBMkoSP5_iP_n0vWYdOwKZ6pwrB4G2upkC2J1iiqftpeeLoQqGdP8md5knCt0v84wL_PVe5nQ8Wjgb75hJajs5p4Ouricmqh3K1GiGOgoD1uXXcDwLogIL737u4kBYZ8yI5Sd5vaVbT7RMLdTGMBvlbYitzPbDusYFkbcNa7NNaLWaIy17ST5zucg1_fA3ccAshsmjFGJFim_lXMfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68787096d3.mp4?token=RzjD8lD1W0DAG2179L7WDCmm5VlfZQZ8vrN-1DTAAGfkcHXMSKOdDipT9HfJEJ_1IXVZhKc17j6VkSGeRIh6Rcft5k5UpXp84wzCcB94sNAa_DGSBRq74kCsNi5IHDqpT-YbhBMkoSP5_iP_n0vWYdOwKZ6pwrB4G2upkC2J1iiqftpeeLoQqGdP8md5knCt0v84wL_PVe5nQ8Wjgb75hJajs5p4Ouricmqh3K1GiGOgoD1uXXcDwLogIL737u4kBYZ8yI5Sd5vaVbT7RMLdTGMBvlbYitzPbDusYFkbcNa7NNaLWaIy17ST5zucg1_fA3ccAshsmjFGJFim_lXMfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : در جریان سفری مداوم به خاورمیانه، دریاسالار برد کوپر، فرمانده سنتکام، با رهبران ارشد غیرنظامی و نظامی در اسرائیل و لبنان گفتگو کرد. کوپر و کارکنانش در لبنان با رئیس جمهور جوزف عون و فرمانده نیروهای مسلح لبنان، ژنرال رودولف هیکل، دیدار کردند. این رهبران در مورد مسیر پیش رو برای اجرای یک توافق‌نامه تاریخی که روز جمعه در واشنگتن دی سی امضا شد، گفتگو کردند.
سنتکام : بیش از ۵۰ هزار نفر از نیروهای نظامی آمریکایی در حال حاضر در سراسر منطقه در حال فعالیت هستند و هوشیار و آماده باقی مانده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/16157" target="_blank">📅 19:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16155">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزیر جنگ اسرائیل: ما در حال آماده شدن برای نبرد جدیدی با ایران هستیم که هر لحظه ممکن است رخ دهد و ما از لبنان عقب‌نشینی نخواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16155" target="_blank">📅 18:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16154">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔸
قطر فعالیت‌های دریایی خود را تا اطلاع ثانوی متوقف کرد
وزارت راه و ترابری قطر با صدور اطلاعیه‌ای اعلام کرد به‌منظور حفظ ایمنی عمومی، تمامی فعالیت‌های دریایی در این کشور به‌طور موقت متوقف می‌شود.
این وزارتخانه از تمامی مالکان و استفاده‌کنندگان وسایل دریایی خواست موقتاً از حرکت در دریا خودداری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16154" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16153">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک مقام آمریکایی به سی‌ان‌ان:
آمریکا و ایران پس از چند روز درگیری و تبادل آتش در نزدیکی تنگه هرمز، فعلا از تشدید تنش خودداری خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/16153" target="_blank">📅 18:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16152">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دولت عراق تا پایان شهریور به مقاومت عراق مهلت داده است تا سلاح خود را تحویل دهد
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/16152" target="_blank">📅 17:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16151">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بیانیه دولت لبنان پس از دیدار عون با فرمانده سنتکام
ریاست جمهوری لبنان:
رئیس‌جمهور عون با فرمانده فرماندهی مرکزی ایالات متحده درباره آماده‌سازی برای آغاز اجرای توافق چارچوب با اسرائیل گفتگو کرد.
رئیس‌جمهور عون بر مصمم بودن برای اعمال حاکمیت دولت از طریق نیروهای مسلح خود تا مرزهای بین‌المللی جنوبی تأکید کرد.
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/16151" target="_blank">📅 17:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16150">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فرمانده سنتکام، دریادار براد کوپر، برای دیدار با فرمانده ارتش لبنان، رودولف هیکل، به بیروت رسید
هدف اعلام‌شده، نظارت بر آغاز اجرای فاز آزمایشی است
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16150" target="_blank">📅 17:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16149">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21080c94a8.mp4?token=B37OZixJDv-FzjhyQW5OPoETlJt4oUZZe6GRwz7Rjhrlf0bc1dfQiUjX9krxGR8w0fzOgOUmB9H-Wom7oFRdDgqNHSHiF0RGNY61NxyLikdKveES35-EBYD1ngn9nSQfeP1wfDesKc5HE8eBcbiranJ8K7N2KRYwG2XSVfOBrrYsC3f-3mqAE6zrIZkF0SruP0-ZpMeAfcVQd1c9hMjnJhz1cPy3RqdkLWA3lQENaKv6tR8EcLYZHRHrKaRG63cGbsgwHjQOFvAMcHs-ScJwCsHF9hgSkGvLixJwRQBB3OvwgpvpnOQZkpwIQ72S-I55WaOXgP9FuHeKjFAOywrnPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21080c94a8.mp4?token=B37OZixJDv-FzjhyQW5OPoETlJt4oUZZe6GRwz7Rjhrlf0bc1dfQiUjX9krxGR8w0fzOgOUmB9H-Wom7oFRdDgqNHSHiF0RGNY61NxyLikdKveES35-EBYD1ngn9nSQfeP1wfDesKc5HE8eBcbiranJ8K7N2KRYwG2XSVfOBrrYsC3f-3mqAE6zrIZkF0SruP0-ZpMeAfcVQd1c9hMjnJhz1cPy3RqdkLWA3lQENaKv6tR8EcLYZHRHrKaRG63cGbsgwHjQOFvAMcHs-ScJwCsHF9hgSkGvLixJwRQBB3OvwgpvpnOQZkpwIQ72S-I55WaOXgP9FuHeKjFAOywrnPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاخ سفید؛ پاسخ خشونت با خشونت داده خواهد شد،
سخنگوی کاخ سفید اعلام کرد که آمریکا به هرگونه حمله، به‌ویژه حملات اخیر به کشتی‌های تجاری، پاسخ نظامی داده و این روند ادامه خواهد داشت. او تأکید کرد رئیس‌جمهور هم‌زمان به دنبال پیشبرد روند صلح است و از ایران خواست «توافق خوبی» با آمریکا امضا کند، در غیر این صورت واشنگتن آماده استفاده از قدرت نظامی خود است.
وی با اشاره به عملیات‌های «چکش نیمه‌شب» و «خشم حماسی» گفت در هر سناریویی آمریکا برنده خواهد بود: در صورت پیشرفت صلح، توافق‌ها ادامه یافته و کاهش قیمت انرژی تداوم می‌یابد؛ اما اگر ایران نقش «مخرب» داشته باشد، به گفته او با انزوای بیشتر در منطقه مواجه خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16149" target="_blank">📅 16:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16148">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فاکس نیوز : ویتکاف و کوشنر به سمت قطر حرکت کردند
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/16148" target="_blank">📅 15:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16147">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhA-P_WPinfx_0InuNdB0JZpkvjLpRdxSueHoYUJaf637MxonD9p_tf2lUuvzpkWTl4w5Px6pocqZn2Oso97Rtnd6IYxiYAWIJ4DogtY3jX_ayZPyJDE26xlbY_VJwRRLg9hMi1spCnT5YWrd2vLTM51IimOuBXUYcoEwUlleLbWHQtAnofcEYUa4ghxqAPpsGYFjU0uEVIpi14V3xj9NeHG00jzgGwgS3O74flSgg8NN-sv98KZQRXYlpv4Qdz89rqyMcfDt_rCBKybC8_WrRetfvZMwSzZwT2Dj7z7fTOomHKtORIJRDYSUZnlHlARuPAH-OjPp8I7gukUB9zLug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : نفت خام ۶۹ دلار، و در حال کاهش است. این کمتر از مقداری است که پیش از آغاز غیراتمی‌سازی ایران بود
قیمت بنزین به سرعت پایین می‌آید! هرگونه تخلف در سطح خرده‌فروشی را گزارش دهید!!
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/16147" target="_blank">📅 15:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16146">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqTdAA5Z83NLS-aj3UHCvEG31_JrMYntRkj1EDXcb9ONCqEiDcZwvj17-MPh6qszsELxJCRBtTMVSyQlLjepIrFo7FVGFH6XdYQEb8AueM9di8DR7OzcEBO2Y8oQgOx7lDNIuqL-sT_99iKcyzjgFQCsKBP2l_rveTJlD6dRJ7ior6dE-u475ddup5POcdxY52nFVA6zgxwKItE8upJrns59nnxdiKF56GHHko4a0CDoP9LVEvDIDzMfNDLHEog835qjinkjpDDeGUMTyl31bgL-FiapgjlnG2yIDap6Jkaop8APmB5p8sMxumAJ47SJuiLGr7erPmH1zfB4ji4bEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران درخواست ملاقات کرده است. این ملاقات فردا در دوحه برگزار می‌شود! رئیس‌جمهور DJT
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/16146" target="_blank">📅 15:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16144">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYS4LrvyC4h1RpP9Ha6gj2fNzmCcWn1uwcjMRPprj5RCcuzEAKNbvaFdes74Sxs5goh40dSoFflnuC1PY6uWiLNZdhxR215d4ZZSs8fFle-cjlS22XqHVKVVYLVKOnaWiC1-beWXBc17q9wC5LbhxasCopNA_C8IPIvqAfPBdzXjj764-zDedMNigb6Y1BKfeaiswb73XUHySVK4-8NxYqB0BoHUUYFUVz0omsxD9cSMhKAcfc1Od1hiKff-B-qaManrsqxqKYYZ2hqV010sezWoLpjH5wSCOOfaMC_XUwuyDUA4wm62cLgT61SVLelS4G_KHsG9fYxHJxtLtDvO2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZ_J6zeWlyyBXmsUVS9QC6WHfNnyrIJrWd-JLcGoC4qv5mP3zpqulotvR54lZSLytKAxIWdLmrZSh466IXcE7_l1D2TTv_f3dOU8jkXR_mjWhbodqQ6Kg1epDIn4oSjETn0YdHRRFOeLZYRqIfZ71RgYpj4YnUwtqKyx5jfyi5t4Byth0y90HfnsaDj8eT0Sb71iUh4xZJgULKGDxvZMoid_dwah4-eIU4h4gAhJBuEO6TWDfwqJxBDYcw7D1XSYHJOSevdIN9oD8crhPaHHV6jg5aQCkY0l-Zo4la86hF1QEeg6Z4xTo7IzvvOff6OQY02byOVxBf15tMph2BVLVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نفتکش شرق لیما، المحبوبه (شماره IMO 9340415) با پرچم عربستان سعودی است که از چین حرکت می‌کند با سرپیچی از دستورات سپاه پاسداران عبور فقط از جنوب جزیره لارک از کریدوری تحت حمایت آمریکا و در میان اسکورت سنگین هوایی نیروی هوایی ایالات متحده، از تنگه هرمز عبور کرد.
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16144" target="_blank">📅 14:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16143">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رویترز: ایران شرکت در مذاکرات فنی را لغو کرد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16143" target="_blank">📅 14:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16142">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5Ct12SPdUA6SHX63YS4H4zlk8-EpefBJlU8-W1K-rcUafBBGljTM4_RgkZau6TisUUuHMr23v3ijdikBF8vSId9shDs7czHloZZQWkK0nU9vBhJdpOwfdPiKey5uym-OtSVjT4OP83zJkOxGVPH9OAeQK-MMklDzDEAYi10MSsoPrqcc0Egix8dfTcYgPtm-vWDTSYDTM3_vzdn7Iz4qzXRYnPzbUct-WElCawTNQBiTNOkzPyP30ZF7WaL3lL1JScGIKav42AMMCtFwMWWNHwXSTe-vpcvFWUL_mp8qdX4XZtZ4XZeS6gzEMcBVlkbZzjPDhf6TmnR8500zACcZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل اسرائیل، ایال زمیر در‌جلسه به مناسبت ۱۰۰۰ روزه شده مبارزه : الان جنگ به یه مرحله حساس رسیده
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/16142" target="_blank">📅 14:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16141">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmP-uag5odS7LSGB6dgREcAk28bXt6klgXt6iWbHaIlwhuq4K1WgHNacp4Oye1muEY6wIQIwvtbliA1t1XWqymZpX5TXEUUMzrEw0aYz-kR0LdbMQUVXDVzg9m2ItW4mDoGp_Athcsrd2Ttgs-wYK-IobZyZG0EyVoShxK3ziwj2ox67MoUAbsdI9yZIualHq2f3B04DdkJ-5-Tnzwp60iTGfL6S_6ERZJyz5qklv6o7FWpTx3bkL7xuL-k2qudiUWOtvY5N8-chemrFKXHgslh3vRltY1iG4XD__4P8mFgEaNfH1TJ8PzEIDXdViGyB_4ONmPk7mLRjC7914VDpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : بالاترین آمار نظرسنجی‌ها تا کنون. حتی بالاتر از روز انتخابات، ۵ نوامبر. این علیرغم این واقعیت است که ایران سلاح هسته‌ای نخواهد داشت!
@withyashar
یاشار : نردبون ایران
😂</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/16141" target="_blank">📅 14:26 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
