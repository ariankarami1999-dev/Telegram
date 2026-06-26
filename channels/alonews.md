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
<img src="https://cdn4.telesco.pe/file/NaYTvHoa1w6nI-dbIMTPVjIzvNm5vDMpCuDMz_WRBW68T39iSlpjl2a3ayDPAHH5ORIKwvxBitZFEDa75kZkItA6fNfZmN0PFptp5s0FC36l-nlwbUf8TaWbUuazLq3k2zLeqrqQlEY4aBAV4hlq8qYwA_GTB27vcisPR4nzPTJtVPiKuZq80Mzv3q-8gLj4gCVRr6yI1UDRDRBnIs5ODs5RdKm44GKAtUgYepsCbhi1yQh_e1q6iY3MEyHlEL9oblcYApEWamZH19YQVYqP6cdtxKirnYQLNwlc63dSa_dgMjDu8lKot96VoI0tjae610L-HybiZiz_yfmpS7ZLRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 937K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 02:11:51</div>
<hr>

<div class="tg-post" id="msg-130436">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXWDduVrkewAnqEyMNHIys__kH7t9dSFsA6UEeYbbigP7Io_J5ieN755hUC_Vj8woYakICbGjP79aYBYeCFouru-TC6drbn7lFCc5YMy_6ZSImrtbRmZT4NohzWYG0WFmnq8iTqtkv5F7VJyuwlIWZ7nnlbJEC_EXqxrdwvaNOYhRJzOU2qEHAfxBJG19KIwwChD48hgJ-S5T3ojgb8qWPINszIz-Y0svo7VbW-z3fXWkN1AE4dZWoCbIfbRCG-CWsdyro41_mqXaNh-CD4tayyhh6f4nuv-LB26rB2i5c23-TMx2eVCIEqgu09oaJDIBwesZSryBHPQj057HIv4eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی از ترس خوارج مجبوری خودتو قایم کنی.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 16 · <a href="https://t.me/alonews/130436" target="_blank">📅 02:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130435">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ ۚ
🔴
به دنبال نقض آتش‌بس رژیم صهیونیستی در جنوب لبنان، ساعاتی پیش رژیم پیمان‌شکن آمریکا نیز مانند همیشه دست به نقض تعهدات خود زد و به بهانه‌های مختلف از تردد یک کشتی متخلف از مسیر غیرمجاز در تنگه هرمز به حمله هوایی به سواحل جمهوری اسلامی ایران اقدام کرد.
🔴
نیروی دریایی سپاه پاسداران انقلاب اسلامی در پاسخ به این تجاوز نقاط استقرار ارتش ترورستی آمریکا در منطقه را مورد اصابت قرار داد.
🔴
بر اساس بند ۵ تفاهم نامه اسلام آباد ترتیبات کنترل عبور و مرور در تنگه هرمز با جمهوری اسلامی ایران است؛ لکن آمریکا با تحریک جهات مختلف در صدد تخلف از این تعهد بود که پاسخ لازم داده شد و من بعد چنین خواهد بود. در صورت تکرار تجاوز، پاسخ ما گسترده‌تر از این خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/130435" target="_blank">📅 02:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130434">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ونس: خشونت با خشونت پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/130434" target="_blank">📅 01:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130433">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
فارس: سپاه فعلا نگفته به آمریکا پاسخ میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/130433" target="_blank">📅 01:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130430">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U70QlL27dYWCpw6jbzc-pamJ0AarFrNMlxd7SJfVpnmokM0NqHxp2I4XFvSh_f1aak7WU0NdqUiIIJcjcNXrFZkKZ0qXIkeZk2aJUIL8iE3POObphhFE4lCMgvFO-gt4C4CaKhxwwl2p3N_NCkoX3XrCGAqginTGugDw7L8op_ovsKKo576ig0UG32r2AeBrZ1P1eIdnAavdUfdG2QKmqEBXx8TzL8E5Eyx4izm9lgJyylCPi91LRXQH70eVwp1tVWbguui9y_Q9kepPzIaVDUueaZsrBCfHtFpOwkgCqFkSXdBAjO8dExGstLQgT91YdH1NshCUQmPxf0gae16q4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1bf794007.mp4?token=OKpzUATexcUpx8jDZ8n4ijOKOc8kpNZmNPHvJXwb7OTAgKpxULKB4J4M3hOI45gp72cURnOppeGJJpFfWKnqHH01L-U4hLlHxBBNoNA6VNC1bLiASd4H569EHXn-m6UvV81VFLMlZzesD0JA9gzi1pnspHjrO4SIQfBXxljQV3NiIyhy_TF0z5OFhJRQDr5QRVF64xW9uAriUqfqiE4FDwyn1LVWpNEoqdCB5b6I8LoL8UK-E5dnO7ToWgELm8FmEIp-mWK2ZppB7cGehQoQVTz8oEDjOxqjHiNr-DlO4f_1i0aWS3N5CymOptQ-UIo1jtOUWZuc0O9sRUfmaJmjig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1bf794007.mp4?token=OKpzUATexcUpx8jDZ8n4ijOKOc8kpNZmNPHvJXwb7OTAgKpxULKB4J4M3hOI45gp72cURnOppeGJJpFfWKnqHH01L-U4hLlHxBBNoNA6VNC1bLiASd4H569EHXn-m6UvV81VFLMlZzesD0JA9gzi1pnspHjrO4SIQfBXxljQV3NiIyhy_TF0z5OFhJRQDr5QRVF64xW9uAriUqfqiE4FDwyn1LVWpNEoqdCB5b6I8LoL8UK-E5dnO7ToWgELm8FmEIp-mWK2ZppB7cGehQoQVTz8oEDjOxqjHiNr-DlO4f_1i0aWS3N5CymOptQ-UIo1jtOUWZuc0O9sRUfmaJmjig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرکوب اغتشاشات در لبنان شروع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/130430" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130429">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
برخی منابع عربی در خبری فوری از آماده‌باش در پایگاه‌های آمریکا در بحرین، کویت، قطر و عربستان خبر داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/130429" target="_blank">📅 01:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130428">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
رئیس جمهور لبنان:
اغتشاشگر را باید سرجایش نشاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/130428" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130427">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0-rPIps_OY1Oy4iaP2EIAHtuhvF-psQMMT7Ft1wtENAa7UxfFMJUvvqNBt7gVfNgsvolh8ksn6KKQzzwu8jUpNgu4owCttUt4Th8ScNllZZZ20AkQbgHA-oO05CKdpNyfoQXploMWlEJ8--5luq08E3E9n-iFWJkQQ6kpDLi0lkiNSvR-IXrOIClfZvQ_q_PyOAQpHWslIEd8eJIAjRIwmxxD8iBz-IQsw8Uf3j1-xjL4tUhtFpbkNEay5p6tQ1e_PKG-WsvURf9DTMJQGpER-mD74QLhvit_SE6BKpUWRK2kA2k4AWOKY8jHpj9o_ehAGTvCnRv63lmKash7vu5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای ارتش لبنان برای سرکوب اغتشاشات وارد عمل شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130427" target="_blank">📅 00:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130425">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c12144a38.mp4?token=fm8siUt83P-Yx_2Ck78Cf96kTxLPkasPC-7i52FYAwFSncXfdDfllhjKvbeO7ZVlN26EYvpvX2gcQcc8LevKwFHSkw9eki6fO0rYWWSwLypBkfinn5cFFQorUfQpFmMSycely6QaMHqJROjn8PgQcH5JLt53iTR7j_KVRVXop9YYd08rI0HY_rUFaoLdXQAQ0WR8W-L8F63x-Ti-TO04IL7gv0p-hdoghaW8GlCm92E8hguJrtIh240JYv4Zld3DyKKXtJ_ZYYpds5fC0kEWsEbFi3zbPACqn9x9B3dEQsYFeqpYwf9ZaGDzSiVA5lPtzXyAdPvS6m843E1OlSDI4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c12144a38.mp4?token=fm8siUt83P-Yx_2Ck78Cf96kTxLPkasPC-7i52FYAwFSncXfdDfllhjKvbeO7ZVlN26EYvpvX2gcQcc8LevKwFHSkw9eki6fO0rYWWSwLypBkfinn5cFFQorUfQpFmMSycely6QaMHqJROjn8PgQcH5JLt53iTR7j_KVRVXop9YYd08rI0HY_rUFaoLdXQAQ0WR8W-L8F63x-Ti-TO04IL7gv0p-hdoghaW8GlCm92E8hguJrtIh240JYv4Zld3DyKKXtJ_ZYYpds5fC0kEWsEbFi3zbPACqn9x9B3dEQsYFeqpYwf9ZaGDzSiVA5lPtzXyAdPvS6m843E1OlSDI4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از اغتشاشات در لبنان
🔴
اغتشاشگران اموال عمومی را آتش زدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130425" target="_blank">📅 00:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130424">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ارتش لبنان به سمت اغتشاشگران در جاده فرودگاه بیروت گاز اشک‌آور پرتاب می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130424" target="_blank">📅 00:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130423">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
خبرنگار فاکس‌نیوز به‌نقل از مقامات ارشد دفاعی بیان می‌کند حملات هوایی آمریکا همچنان در جریان است که باتوجه به حجم تحرکات هوایی در جنوب کشور ادامه‌دار بودن آن قابل انتظار است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/130423" target="_blank">📅 00:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130422">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سپاه پاسداران: ما مقابله با حمله‌ای که توسط نیروهای آمریکایی به جزیره سیریک انجام شد را اعلام می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/130422" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130420">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e331902452.mp4?token=gQK70XgD8rDtIEOsRxzladEgTTrg_soNIgh10kqn5k1haKqzoSzeIEACiZXg6I8UJDz3sDG9Jkr2nB_Dg-QhMO0AmSyJfngYopisfZRP5ofoeFow-gyAcnyL3yQVMd1DIViz5Vpn54Rm0Zb27ArRS_ZrC_tsOMV3GmZFQ6XtqjeCQYhqVXzJwcwVLuC9BDq_jjk66ORdNpUK1s4U_un5IDnAvXgAjyThKLEW9vwgxc-L2nPFYeLQB41SnkIecphhIEHmKJqjsEF8fBCmcRidmXUWPgjjfWWIG8VA-pJv-3hiCa_nzkZ28z-wxUDGat2MzDTIVSVZ9A0pf6frFXzTlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e331902452.mp4?token=gQK70XgD8rDtIEOsRxzladEgTTrg_soNIgh10kqn5k1haKqzoSzeIEACiZXg6I8UJDz3sDG9Jkr2nB_Dg-QhMO0AmSyJfngYopisfZRP5ofoeFow-gyAcnyL3yQVMd1DIViz5Vpn54Rm0Zb27ArRS_ZrC_tsOMV3GmZFQ6XtqjeCQYhqVXzJwcwVLuC9BDq_jjk66ORdNpUK1s4U_un5IDnAvXgAjyThKLEW9vwgxc-L2nPFYeLQB41SnkIecphhIEHmKJqjsEF8fBCmcRidmXUWPgjjfWWIG8VA-pJv-3hiCa_nzkZ28z-wxUDGat2MzDTIVSVZ9A0pf6frFXzTlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اغتشاش و کودتا هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/130420" target="_blank">📅 00:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130419">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
گزارشات از جابجایی لانچرها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/130419" target="_blank">📅 00:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130418">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
تسنیم:
نقض آتش‌بس و تفاهمنامه توسط آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/130418" target="_blank">📅 00:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130417">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
خبرفوری/ حمله به تهران
⁉️
برخی منابع خبر دادند در صورت گسترش حملات، به تهران نیز حملاتی میشود
⭕️
@Akhbr_Fourii</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/130417" target="_blank">📅 00:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130415">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
فاکس نیوز به نقل از منابع آگاه: حملات آمریکا به اهداف ایرانی ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/130415" target="_blank">📅 00:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130413">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_Au69aRJuFPHkU0pyCzcVI1_kZ8tNcVZsyYXUjilxAPH2R8UtAo_WpZSvYWGvL-B7fA6xjiVly9xFZlVnWgHIZt9Dh59ZTFreJgkXVC4KEp0Uuc-Hw9XiVBXjS-hT2HN1uc5Fxpchv6ki9zDN1ktBmFhiUen3Bb9065W3oYQHhw4BHN5LyxM-vMI_s0K2OvJfKy9jih2UYjrbBXUFrCAUpSS_arn5e-L8S_wKp3ePIqei3ejEPiHq45XRdc8potmP1ZMwcM7ZRaTGUCdgXPWMnytiCktvZCKC6x5UNe7A84hem20t3P6SkV_zMtPZBYSy4Q3wW-kMM8YI6dX1A29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا: ایالات متحده در پاسخ به حمله‌ای که یک کشتی تجاری را هدف قرار داده بود، ضرباتی علیه ایران انجام داد.
🔴
هواپیماهای ما حملاتی را انجام دادند که سایت‌های ذخیره‌سازی موشک و پهپادهای ایرانی و مواضع راداری ساحلی را هدف قرار داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/130413" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130412">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
گویا یک دکل مخابراتی در سیریک مورد حمله قرار گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/130412" target="_blank">📅 00:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130411">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فووووووووری/بریزید اینجا
⬇️
https://t.me/+1RDlZFB3XPtlNzg0
https://t.me/+1RDlZFB3XPtlNzg0</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/130411" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130410">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی: ارتش آمریکا در منطقه تنگه هرمز حملاتی انجام داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/130410" target="_blank">📅 00:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130409">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQw0-iluI-Qd6Tef-Ai1IT2xPeaAHVJkgpAbUJtfVb4Ln3THO_hiOUFQftISHx__ZY2uAqrBy7p7Q-k1Y7WqOXW8emZRfiihNEuowS6zVfRIw_2mZ2SvbuWExF1Equ5ypU3Kqfse8wym5kLsBmKftQ06-3dA2SyFveHWK0R6D9HnHtyPD7vkcD47OeIp-1NXpsNxwsEsN2rxcYiobLxs2dhLUcmYDrodDJW_QHeWwdLIdr6g4PPfgUBe-t8VxIOf_B1hh_0Pk9Su8e0eCjRdMRbaeQvnFKDbn7g_jZECy_rLnBgeV3tZ37yZlnTmrY5aXLg71QApO9NyT8U7VkqJOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندین هواپیمای نیروی هوایی ایالات متحده بر فراز امارات متحده عربی و ورودی تنگه هرمز در حال پرواز هستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/130409" target="_blank">📅 23:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130408">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
برخی منابع ادعا کردند صدای انفجارها، صرفا نوتیف دریافت سویا و ذرت بوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/130408" target="_blank">📅 23:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130407">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری/ترامپ: خواهیم فهمید چه میشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/130407" target="_blank">📅 23:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130406">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوووری/طبق برخی گزارشات، سپاه قصد دارد اهدافی در منطقه را در پاسخ به حمله آمریکا مورد هدف قرار دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/130406" target="_blank">📅 23:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130404">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری/سنتکام: اهدافی را در ایران زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/130404" target="_blank">📅 23:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130402">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوووووووری/ارتش آمریکا در پاسخ به نقض آتش بس از سوی ایران، اهدافی را در جنوب ایران هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/130402" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130401">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سه صدای انفجار در سیریک، هرمزگان شنیده شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/130401" target="_blank">📅 23:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130400">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tx3Q5ocuzgepeHIoJ3gYeAtS-H7yHYtejLMPrhFnh_jzH8jRfjaEQog8lMkNk27I9sk6H2ii5CN9g1ppvcppXDuBnUK9GvVxU10SFXf3NcuRhdLwOMpr3eYTY65WcDXt7DS3RM2gd31shKZpfi07vzlFuLOSKhXCmvBaQz1MIz3hE6TYSCj7-apoJSmfiM4Y06-KViygLQNsOQYUKl-mS_11AiYQcy3gCwK545JV-Isl7s58rMhbIobdjRmsHtJLp5OFalwDMNp0S6ilzCEVCatM-5Z3Cb7d_zkcLUwRIP789oesMWWm8Ak8XfEdN4xi030WlshZJAyIpabiO648BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده…</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/130400" target="_blank">📅 23:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130399">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2nVkN7xid50G6Ec6m9uxIWFDW6wnu_rIr4P0XEDe746vSDeT_Vnb3vLt8Rut-RqYbCsiRnQX0ksSWRzduFb7ZnzjQRQNNjGv7WXICUvbnbti87_fLzhT_2JLEbeog9WW7gqbtc6kDbRc1NgWa-mSo5jr98nXN_n-hiCvqYQ22ZCFHvblBmwX2nTeKxRGyZ_MPA9Opk573ECjtUQZMcJrb5GAs12U4YyvCIHaxsfUfir24Dj27N8IDaaxt_BvT31TGhRTmXRZBeM1qEEJ6UEuXkY_gwP9wJBCvmjNidhDavuZ-OVdFdc2rYMwKHol1Kc6d0mOp__4oZSymcbLfIqYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موکب تنگه هرمز تو ضاحیه بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/130399" target="_blank">📅 23:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130398">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: ما مجبور بودیم به ایران حمله کنیم، چون اونا دو هفته با داشتن سلاح هسته‌ای فاصله داشتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/130398" target="_blank">📅 23:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130397">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی: اگر دشمن خطایی مرتکب شود، جنگ بعدی دیگر مانند جنگ 40 روزه نخواهد بود، مطمئن باشید ما توانایی‌ های جدیدی را به میدان خواهیم آورد و آقای ترامپ بداند که اینبار تلفات انسانی گسترده‌ ای در پی خواهد داشت
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/130397" target="_blank">📅 23:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130396">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی: اگر دشمن خطایی مرتکب شود، جنگ بعدی دیگر مانند جنگ 40 روزه نخواهد بود، مطمئن باشید ما توانایی‌ های جدیدی را به میدان خواهیم آورد و آقای ترامپ بداند که اینبار تلفات انسانی گسترده‌ ای در پی خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/130396" target="_blank">📅 22:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130395">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
الحدث به نقل از منابع سیاسی لبنانی:
سخنان نتانیاهو با آنچه در پیش‌نویس چارچوب توافق پیشنهادی آمده، در تعارض است
🔴
«چارچوب توافق» با اسرائیل به‌صراحت از «استقرار مجدد مرحله‌ای» (عقب‌نشینی یا بازآرایی تدریجی نیروها) سخن می‌گوید
🔴
بر اساس این توافق، ایجاد مناطق آزمایشی با تصمیم یک‌جانبه اسرائیل امکان‌پذیر نیست
🔴
این توافق هیچ‌گونه به رسمیت شناختنی برای «منطقه امنیتی دائمی اسرائیل» در خاک لبنان در بر ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/130395" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130394">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: ما مجبور بودیم به ایران حمله کنیم، چون آنها دو هفته با داشتن سلاح هسته‌ای فاصله داشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/130394" target="_blank">📅 22:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130393">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
حزب‌الله: چارچوب توافقی که در واشنگتن به امضا رسیده، از دیدگاه مقاومت مردود است و هیچگونه الزام یا تعهدی برای مقاومت ایجاد نمیکند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/130393" target="_blank">📅 22:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130392">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124d0585ad.mp4?token=JDalwuAMrEmCslPVofRg0IN6SEuU0XOtBeGEuovMAKipozKNneDqO_agv2PfnyJ1qsZaA7mXerZGn2DV3gn76R0UkJyLt_9nJd1txPGaVYwLTUJhT6HJEzaO5p1QXDzEOrmdHh44eYV39FHsNsH_xQiJEyDlW62R1XXfYOd71fJieoNiLV4ejwfnUVmLq_yL9-8Nml7DAdDEKy9T_7VIJEzgnKo1VpHVGsVtxLBbn7OJMr6U7I8eBtr-xAol9ShczdMdp5IBGai2Var8hTdfn91WhoqHj9lHx9iWFS-gfvt2FElv48A28Zj_zkEqp8ESxLQm0TgoHF419ejo9Jel6oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124d0585ad.mp4?token=JDalwuAMrEmCslPVofRg0IN6SEuU0XOtBeGEuovMAKipozKNneDqO_agv2PfnyJ1qsZaA7mXerZGn2DV3gn76R0UkJyLt_9nJd1txPGaVYwLTUJhT6HJEzaO5p1QXDzEOrmdHh44eYV39FHsNsH_xQiJEyDlW62R1XXfYOd71fJieoNiLV4ejwfnUVmLq_yL9-8Nml7DAdDEKy9T_7VIJEzgnKo1VpHVGsVtxLBbn7OJMr6U7I8eBtr-xAol9ShczdMdp5IBGai2Var8hTdfn91WhoqHj9lHx9iWFS-gfvt2FElv48A28Zj_zkEqp8ESxLQm0TgoHF419ejo9Jel6oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ توافق اوباما با تهران را «JCPOC» می خواند.
🔴
پ.ن:
Joint Comprehensive Plan of Action
است که در فارسی به آن «برنامه جامع اقدام مشترک» یا همان توافق هسته‌ای ایران (برجام) می‌گویند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/130392" target="_blank">📅 22:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130391">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ: کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که تابه‌حال در خاورمیانه رخ داده است.
🔴
من فکر می‌کنم خمینی (منظورش خامنه‌ای‌ست) و دیگران در ایران از اینکه من سلیمانی را کشته بودم خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
🔴
او یک ژنرال درخشان بود. او مردی بسیار بیمار از نظر روانی بود.
🔴
کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که در خاورمیانه رخ داد. مردم گفته‌اند که بزرگترین اتفاقی است که در ۱۰۰ سال گذشته رخ داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/130391" target="_blank">📅 22:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130390">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9bda5bb20.mp4?token=c3TPtRcy9eEj5Ra8IbyKKEvUxOoyDLZUC6Ixi7-cQC9OC68wMLJWTMHtAOkpJuM8KQekBaHoHiDVDj5HfVredhvjO8939bt627gqCY1b1dBfZxopJKeAiyfDzoKmukYlFfW5GWKZHiCsYY5fp4zrTgpyWDsBHxNeUDxnLKCSZ4s55mU7f4pla1BOxAVV2CDik3XuvaPAaHjeVDdIQ5BhwUGMDma4lmV35jj6WJqaLsrnmsAi-eYAvlktdDPfDarLs-dckgEzUK2HZSNPxifwjYU6PREiok1kaTl8OkGWq1uoy8VwWkMflWPd1Db8_gPtcKReAPkhxW2eSgmyIC-CH20Q3K0okWcz_NfDzzsg2jPoSkLLKfsgM6UuLeYPL3uSUFC2dXOrYRgpBfjmbO3dNPRLCMvnkYFis4ce61qgNRZV-TjuPNJP4UhC-CR6426bkxm--nE90IavKJEaMSfeNeSEoruabN-iRJmq0iEOHAElQdGgiqS67wKpl5VjQgd8SOSDWpmwHZYH1QeEhDipKMftvsJlzN92o-4G-cAdvzBlja0h60cGZXSWRR7jy7chr1gdo7DvvebwGWtW-eNX7eDpyI3pcigkPUUceAtSMAGn8HABEOhiYiPAZcpgI5SLqT_ZSXQe1g4KdWHFtUbqiNC3hzLtfJN6yvo0g7dD4dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9bda5bb20.mp4?token=c3TPtRcy9eEj5Ra8IbyKKEvUxOoyDLZUC6Ixi7-cQC9OC68wMLJWTMHtAOkpJuM8KQekBaHoHiDVDj5HfVredhvjO8939bt627gqCY1b1dBfZxopJKeAiyfDzoKmukYlFfW5GWKZHiCsYY5fp4zrTgpyWDsBHxNeUDxnLKCSZ4s55mU7f4pla1BOxAVV2CDik3XuvaPAaHjeVDdIQ5BhwUGMDma4lmV35jj6WJqaLsrnmsAi-eYAvlktdDPfDarLs-dckgEzUK2HZSNPxifwjYU6PREiok1kaTl8OkGWq1uoy8VwWkMflWPd1Db8_gPtcKReAPkhxW2eSgmyIC-CH20Q3K0okWcz_NfDzzsg2jPoSkLLKfsgM6UuLeYPL3uSUFC2dXOrYRgpBfjmbO3dNPRLCMvnkYFis4ce61qgNRZV-TjuPNJP4UhC-CR6426bkxm--nE90IavKJEaMSfeNeSEoruabN-iRJmq0iEOHAElQdGgiqS67wKpl5VjQgd8SOSDWpmwHZYH1QeEhDipKMftvsJlzN92o-4G-cAdvzBlja0h60cGZXSWRR7jy7chr1gdo7DvvebwGWtW-eNX7eDpyI3pcigkPUUceAtSMAGn8HABEOhiYiPAZcpgI5SLqT_ZSXQe1g4KdWHFtUbqiNC3hzLtfJN6yvo0g7dD4dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
اخبار فیک/جعلی گفتند که ایران امروز بسیار قوی‌تر از ۴ ماه پیش است.
🔴
آن‌ها تشنه‌ی انجام یک توافق هستند.
آن‌ها به ما بسیار زیادی می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/130390" target="_blank">📅 22:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130389">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e369539a42.mp4?token=kDq-G5CdcqC-YWMU1Wkx9bXodAsKnkw71R-I-jYPRuhH3l4-bBHoS07TpK2jV2wk_2jB_EEV41UlqaVBQRzDaBrUvlafT99LYtqobSZbdPgLb5L05cCoEOHnPys2T9DpiUBfAwNi5pZfhcx2FZ6KxcsqjRRAOBQdVwyQG_FwFICIehqwYjAukdvqw60RSxDcpFuokWw4lkkM-jGa8Ty3aMNQpUsb4rYnJn6mjjNmfDn9K4RVWr8GLIFVybOBYjJ179ocBTxncYqjtqcx4tk-QmwH-7HwQz_SplgVjL7Hwilbcv2uzEYmFksK__N5GXt_YoA9CGlTS0EomBC0ROi-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e369539a42.mp4?token=kDq-G5CdcqC-YWMU1Wkx9bXodAsKnkw71R-I-jYPRuhH3l4-bBHoS07TpK2jV2wk_2jB_EEV41UlqaVBQRzDaBrUvlafT99LYtqobSZbdPgLb5L05cCoEOHnPys2T9DpiUBfAwNi5pZfhcx2FZ6KxcsqjRRAOBQdVwyQG_FwFICIehqwYjAukdvqw60RSxDcpFuokWw4lkkM-jGa8Ty3aMNQpUsb4rYnJn6mjjNmfDn9K4RVWr8GLIFVybOBYjJ179ocBTxncYqjtqcx4tk-QmwH-7HwQz_SplgVjL7Hwilbcv2uzEYmFksK__N5GXt_YoA9CGlTS0EomBC0ROi-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره رهبری در جمهوری اسلامی ایران:
دیگر کسی نمی‌خواهد رهبر ایران باشد. گفتند: «چه کسی دوست دارد رئیس‌ باشد؟» و همه گفتند: «نه، ممنون.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/130389" target="_blank">📅 22:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130388">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ درباره شهردار نیویورک:
شهردار ممدانی که به نظر آدم خوبی می‌آید، گفت که قصد دارد مطمئن شود مردم افزایش اجاره‌بها را تجربه نمی‌کنند، حتی اگر هزینه انرژی افزایش یافته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/130388" target="_blank">📅 21:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130387">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a205f15b6.mp4?token=Y7j5zWxVceNlI_0aJHmsK1gK6OL2KiY0DHH3nPrrOS-YZexJIlwBMyXiYJoKqj16br2dYqKNLueBcO5y0GIxJa1zsvcCuruRaxxZqgTM92dmf9j0fR09TvADf9JcJIJ3vmm1dZCa7lUHJoj90BIo6PQMke2xx_8RLK1vrI8Msy5isA_cINmimi_suGXRM0VYhetJaXxNvnyEeHsg8hLop6dF8qkSyPc-ak_EpXBaBRJsRjcdJFvky4K3LkKKbb0AGYJDB_p1F_bEyYOYfJ_LhQ6o3Rof54WD6ye1woSfMuM0tvwBnBAl4zFRUMwoOtuSnQPx45SJFzKkpdHQ3yRS-LggHxWj6eCharL-RLc6Beu1ZuQcbqlvHTttP11K0FB8P9FpGcgRudsWCxCDPgZboioJ6g4kI5SkwOGc2ywy6lBWSkz2o8XuqSS7A_gMm7UIiAlbiOt_I6dbSX8MeXjjrAie2zT1W2aWNiobaLv1ZGq234oCi_jHcso-AxXW_sIgmzyRKuQQpyx6mMgdJUOeb-yUNd7C_qgJJ4XNq73GX4A1PkoFyg3fOpaFIm45arkESe14MKNBcNZDbxAMebIuHL3rFzYsUDjMsrRLfWQfNWCx0c81txPBz9_FyjW_hGHk1GqulQJpYbNzH0zL9hENa25N8dthW0DQdoWuOOTbNRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a205f15b6.mp4?token=Y7j5zWxVceNlI_0aJHmsK1gK6OL2KiY0DHH3nPrrOS-YZexJIlwBMyXiYJoKqj16br2dYqKNLueBcO5y0GIxJa1zsvcCuruRaxxZqgTM92dmf9j0fR09TvADf9JcJIJ3vmm1dZCa7lUHJoj90BIo6PQMke2xx_8RLK1vrI8Msy5isA_cINmimi_suGXRM0VYhetJaXxNvnyEeHsg8hLop6dF8qkSyPc-ak_EpXBaBRJsRjcdJFvky4K3LkKKbb0AGYJDB_p1F_bEyYOYfJ_LhQ6o3Rof54WD6ye1woSfMuM0tvwBnBAl4zFRUMwoOtuSnQPx45SJFzKkpdHQ3yRS-LggHxWj6eCharL-RLc6Beu1ZuQcbqlvHTttP11K0FB8P9FpGcgRudsWCxCDPgZboioJ6g4kI5SkwOGc2ywy6lBWSkz2o8XuqSS7A_gMm7UIiAlbiOt_I6dbSX8MeXjjrAie2zT1W2aWNiobaLv1ZGq234oCi_jHcso-AxXW_sIgmzyRKuQQpyx6mMgdJUOeb-yUNd7C_qgJJ4XNq73GX4A1PkoFyg3fOpaFIm45arkESe14MKNBcNZDbxAMebIuHL3rFzYsUDjMsrRLfWQfNWCx0c81txPBz9_FyjW_hGHk1GqulQJpYbNzH0zL9hENa25N8dthW0DQdoWuOOTbNRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ با اشاره به پیام کمی پیش خود در تروث‌سوشال در طعنه به کمونیست ها:
راستش را بگویم — فکر می‌کنم من بزرگترین کمونیست در تاریخ می‌شدم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/130387" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130386">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ: تمام کمونیست‌ها بی‌خدا هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130386" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130385">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa291828e.mp4?token=hmqZMB6HWT1VX6860kOmeIKPaOetsOjJdQmBvMWIdf3YgEP9ALb708F669EfKXOhdd1VsXJ9RBQXiffTRd_J2waXCkTHJ_mW6vmrm1MlrLofVrtolxIeKXuvdoQc5q-TyljXRFCqCgTTseeO82uRO-lBDsosc-fqu9tXSHlleJc909QsMpievjPhQ9hoxuD_wQDGY2gH2dfZnkSYu2NyZhzDkLzKuCgZ51UlukZHr-n7AQGOs07OGXFHgORU7zEukUoRySiwQtRgmnLnAOETbh5lFIMwJFDwsA9w-AfrPesmMSzDIOlZ21eghVYfNDhC6fnI3xePBYMDh-OvWBE9FrLX0m_rdSP2Vs45DrLS2dtnkG-pC6IQODl10Daq-qKMtliiRg3em2Q3GbOCmgEI5_F-9Rod2imcIJ_jR9njj_rhyiG13irC90Lg8sCGgxbHXeqMkibq9EqgcPbVWxPPXXocJFvj-xuzstozORzciIVVNl7QvABdxP6nfY_1vc2gQNhHlwSE05RBJR_lzDdqdSNC7e5x4IIAb9NJm4chQwa72g4ps5cXGm6Unf4UcI29UHaQlifaTj73mmws_oWrs46LW8uAKJaSfaHggurlbvqL73Y4aLeQGfL9tlOirfQf46Etiay0KXPSdvAqLK20NbLLukkdde06FtphhzPI0qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa291828e.mp4?token=hmqZMB6HWT1VX6860kOmeIKPaOetsOjJdQmBvMWIdf3YgEP9ALb708F669EfKXOhdd1VsXJ9RBQXiffTRd_J2waXCkTHJ_mW6vmrm1MlrLofVrtolxIeKXuvdoQc5q-TyljXRFCqCgTTseeO82uRO-lBDsosc-fqu9tXSHlleJc909QsMpievjPhQ9hoxuD_wQDGY2gH2dfZnkSYu2NyZhzDkLzKuCgZ51UlukZHr-n7AQGOs07OGXFHgORU7zEukUoRySiwQtRgmnLnAOETbh5lFIMwJFDwsA9w-AfrPesmMSzDIOlZ21eghVYfNDhC6fnI3xePBYMDh-OvWBE9FrLX0m_rdSP2Vs45DrLS2dtnkG-pC6IQODl10Daq-qKMtliiRg3em2Q3GbOCmgEI5_F-9Rod2imcIJ_jR9njj_rhyiG13irC90Lg8sCGgxbHXeqMkibq9EqgcPbVWxPPXXocJFvj-xuzstozORzciIVVNl7QvABdxP6nfY_1vc2gQNhHlwSE05RBJR_lzDdqdSNC7e5x4IIAb9NJm4chQwa72g4ps5cXGm6Unf4UcI29UHaQlifaTj73mmws_oWrs46LW8uAKJaSfaHggurlbvqL73Y4aLeQGfL9tlOirfQf46Etiay0KXPSdvAqLK20NbLLukkdde06FtphhzPI0qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کلمبیا: من ال تیگره را تأیید کردم. او را دوست داشتم. می‌دانید چرا؟ چون او مرا دوست دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130385" target="_blank">📅 21:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130383">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ: بنیان‌گذاران ما چهار بار در اعلامیه استقلال به خالق اشاره کردند. چهار بار. من حتی یک بار هم ذکر نشدم. من بسیار ناراحت هستم. حتی یک بار.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130383" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130382">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ: دین در کشور ما بازگشته است، بزرگتر و قوی‌تر از آنچه در سال‌های بسیار زیادی بوده است.
🔴
برای اینکه یک ملت بزرگ باشید، باید دین و خدا داشته باشید. اگر آن را نداشته باشید، به نظر نمی‌رسد که کار از آب دربیاید، آیا نه؟
🔴
زیر نظر دموکرات‌ها، کاتولیک‌ها توسط اف‌بی‌آی هدف قرار گرفتند.
🔴
مادر بزرگ‌های حامی حیات به زندان افتادند برای دعا کردن.
🔴
اعضای نیروهای مسلح ما به خاطر باورهای مذهبی‌شان از نیروهای مسلح اخراج شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/130382" target="_blank">📅 21:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130381">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e316bf1446.mp4?token=Iw80NbdszIxa9G_WcBuGSU9BkWVzL_p28FuAQkuA5zpbogJS4EEvOvwViqG_NZoTUWfNtgdaYuz-WPH1HY5Z3jOQjPPPVXvpsJj0yP4m_gvVa64MsNXEPkDcMsk8VGF9WuyyjAXA_t8Spp8pCK5dWY10NkrSST10KTe1KMKEuTm7yUqa0bYFqNrci29VuXHcC83VNG7YcpbuMw3TZk5aOZoftjyZSbB2YvSvjsiIveTslCk11JtQ1nZWEmD-0ejSizYUTvQ4fdiq_QA0TJSY3ZfAX_rSn9jiFTp9ptG-pFOfgh_hnZi2mBFpmPJv_Z44ldVf_gCRQW0Wth0xr7wLow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e316bf1446.mp4?token=Iw80NbdszIxa9G_WcBuGSU9BkWVzL_p28FuAQkuA5zpbogJS4EEvOvwViqG_NZoTUWfNtgdaYuz-WPH1HY5Z3jOQjPPPVXvpsJj0yP4m_gvVa64MsNXEPkDcMsk8VGF9WuyyjAXA_t8Spp8pCK5dWY10NkrSST10KTe1KMKEuTm7yUqa0bYFqNrci29VuXHcC83VNG7YcpbuMw3TZk5aOZoftjyZSbB2YvSvjsiIveTslCk11JtQ1nZWEmD-0ejSizYUTvQ4fdiq_QA0TJSY3ZfAX_rSn9jiFTp9ptG-pFOfgh_hnZi2mBFpmPJv_Z44ldVf_gCRQW0Wth0xr7wLow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسایی وقتی قالیباف رو تو مجلس میبینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130381" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130380">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa0bb5024.mp4?token=pMDpMmRwW04PWyJHYFIN1NovsvT395swG0c5WQQY1Wov8MMFbsitamkIaTGJEQflEFA_a1LeEwS42KgLnQdq8rcNlnxzvFC8Hv5LdEleI3x-NIPXaFnNhjd8RMyYoYQXELb1_l52l7Ts5jVY3i7hwN7vL4herTBt1hrm1KqTJbE5ZBa_CSJWP-Vpj3u9UYswvak13Rwtg7NWSK0v3lSkCZ27JWEoktiV5WBSSu5tQRzUhhAjZefjwP_BNThZF19RFnBYb6zHrslwwn6pL6vd1zfiiig2B9pOqO0089LcOQQAAKNVQ1dopOAARXMpd7jrrn6bBleY1V3c8_vItMLTtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa0bb5024.mp4?token=pMDpMmRwW04PWyJHYFIN1NovsvT395swG0c5WQQY1Wov8MMFbsitamkIaTGJEQflEFA_a1LeEwS42KgLnQdq8rcNlnxzvFC8Hv5LdEleI3x-NIPXaFnNhjd8RMyYoYQXELb1_l52l7Ts5jVY3i7hwN7vL4herTBt1hrm1KqTJbE5ZBa_CSJWP-Vpj3u9UYswvak13Rwtg7NWSK0v3lSkCZ27JWEoktiV5WBSSu5tQRzUhhAjZefjwP_BNThZF19RFnBYb6zHrslwwn6pL6vd1zfiiig2B9pOqO0089LcOQQAAKNVQ1dopOAARXMpd7jrrn6bBleY1V3c8_vItMLTtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداقل ۹۲۰ نفر کشته و ۳۳۶۰ نفر در نتیجه زمین‌لرزه‌های سه‌شنبه در ونزوئلا زخمی شده‌اند، طبق گفته خورخه رودریگز، رئیس مجلس ملی ونزوئلا
🔴
او افزود که حداقل ۱۷۲ نفر همچنان زیر آوار گیر افتاده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/130380" target="_blank">📅 21:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130379">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09db5bdb36.mp4?token=kohSJifwrdoEIEsSLfsO-9u6UqEst-ogU-sn2hYukYYB9zlv9vYK20zKoaUf5bjbIj99C3z1XwsEg0V4pjQHMRmYVZDvJiNq32qhh82BVZaspCZ-7ZSfoFkny64nEr1dMSRKpFJ0TlLywP5DLPRMQCXj4hqcLFliYyGQPoZ3PWIotyM0bP2TZF8JITVXPrvG6dbL1K9Bllf0GAeaBwlr_N1PbXSE87_QvHpPzMDsRgjgfiLqZECWsW2wp5ezH-Ew9cecDv3-6Ei633CQqMaZeeyzldX1-1qAT0LqjGGASV88JVaqAQkucwqop1VaBtgoXXCMdtLDwkv82HHHfkNprDYFVxqrmpJVLN7y5wmHyoMYcxX3ua0vb--2Or1AQeHUhc66HJPkWx_PEunQ9yH2y3X9r1szQuppZ_NRgWaMoJH54XkJBr4GBqWFGSAT-3933s28KUofeTpVpXCjQuPeC3DsvIu_sxNmCa7iX5So7RYZrxLzoIBboDogFN9TcbaIq52OjTf9yHCKw7CPK5rWfGT4bjGQxpOxHx870bM3N1LrZkt3lnrsz5mpkiQGme5j34ZRmqTyEtmd9VjFCBmPja2DlZe3s06p_7Ah6rOkFnbSnb7Beex8aUdd2y8Rm8t5VomMT_1h0xEDy3z0-ubLrnDwWr8H-A0UwNvoZZ__uow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09db5bdb36.mp4?token=kohSJifwrdoEIEsSLfsO-9u6UqEst-ogU-sn2hYukYYB9zlv9vYK20zKoaUf5bjbIj99C3z1XwsEg0V4pjQHMRmYVZDvJiNq32qhh82BVZaspCZ-7ZSfoFkny64nEr1dMSRKpFJ0TlLywP5DLPRMQCXj4hqcLFliYyGQPoZ3PWIotyM0bP2TZF8JITVXPrvG6dbL1K9Bllf0GAeaBwlr_N1PbXSE87_QvHpPzMDsRgjgfiLqZECWsW2wp5ezH-Ew9cecDv3-6Ei633CQqMaZeeyzldX1-1qAT0LqjGGASV88JVaqAQkucwqop1VaBtgoXXCMdtLDwkv82HHHfkNprDYFVxqrmpJVLN7y5wmHyoMYcxX3ua0vb--2Or1AQeHUhc66HJPkWx_PEunQ9yH2y3X9r1szQuppZ_NRgWaMoJH54XkJBr4GBqWFGSAT-3933s28KUofeTpVpXCjQuPeC3DsvIu_sxNmCa7iX5So7RYZrxLzoIBboDogFN9TcbaIq52OjTf9yHCKw7CPK5rWfGT4bjGQxpOxHx870bM3N1LrZkt3lnrsz5mpkiQGme5j34ZRmqTyEtmd9VjFCBmPja2DlZe3s06p_7Ah6rOkFnbSnb7Beex8aUdd2y8Rm8t5VomMT_1h0xEDy3z0-ubLrnDwWr8H-A0UwNvoZZ__uow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل: شهروندان اسرائیل، پیش از آغاز شبات، می‌خواهم دستاورد بزرگی برای دولت اسرائیل اعلام کنم. می‌دانید که مذاکراتی در واشنگتن بین نمایندگان اسرائیل، لبنان و ایالات متحده در حال انجام است. مذاکرات طولانی که امروز به ثمر نشسته‌اند.
🔴
مهم‌ترین نکته این است که اول و بیش از همه، اسرائیل در منطقه امنیتی جنوب لبنان باقی می‌ماند. این یک دستاورد بزرگ است و ما آن را تا زمانی که حزب‌الله تسلیحات خود را کنار نگذارد و تا زمانی که تهدیدی برای دولت اسرائیل وجود دارد، حفظ خواهیم کرد.
🔴
این همچنین ضربه بزرگی به ایران است. ایران سعی دارد ما را با زور از جنوب لبنان عقب بکشد. و در واقع، اسرائیل، لبنان و ایالات متحده به آن‌ها می‌گویند - این کار شما نیست. شما هیچ نقشی در لبنان ندارید. نه شما، نه حزب‌الله، نه هیچ سازمان تروریستی.
🔴
نکته دیگر این است که البته، ما به ارتش لبنان اجازه می‌دهیم تا برای به دست گرفتن کنترل اراضی سازماندهی را آغاز کند. ما در حال انجام دو منطقه پایلوت هستیم. هر دو توسط ارتش اسرائیل توصیه شده‌اند. و یکی واقعاً خارج از منطقه امنیتی، جنوب رود لیتانی است، و دومی شمال لیتانی، بخشی کوچک از آن در منطقه امنیتی گسترده‌ای است که ما در دو هفته گذشته تأمین کردیم و ارتش اسرائیل به آن نیاز ندارد - این را بسیار به وضوح می‌گوید.
🔴
ما دائماً منطقه امنیتی اصلی را خارج از برد موشک‌های ضدتانک حفظ می‌کنیم. ما اجازه نمی‌دهیم حزب‌الله یا جمعیت وارد آنجا شوند. این حفظ شده است. و مهم‌ترین نکته این است که اسرائیل می‌گوید: امنیت ما اولویت دارد.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130379" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130378">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
اسرائیل و لبنان رسماً یک توافق‌نامه چارچوب میانجی‌گری شده توسط ایالات متحده را در واشنگتن امضا کردند.
🔴
این دو کشور مذاکرات رسمی را در سطح رسمی آغاز خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130378" target="_blank">📅 21:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130377">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1b3AXQj9igHMPuQhrXwccUDgfNe_JJ96L9A-ahGsrxMlHcwSEgrO64jJWR_8L7VZGbBogkNJVwuz7pes6kwLBPM1dWgtXAQZnZKKn0e6URH6JE9PG_Sn96h0pGlR_yecBlfgidelVkVJRG_dMKnMyY3y_CtLTXlv8vZmDhCIQtm5KP7r7VL4P1yZrOucwp3BMl_nkGEjV4O5I1ZiG_-1kgRpIymmUW_nkspvMaTmWzVaP1Ct6If75G91hoa5sbFQIcA1ebISue10pg69OSWjrQzpgoOlbOP8DmdulW3OCn_qOzW1k4Db6NKgxMWastn8uUKW9E6jl9YqQ78IynACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: کمونیسم بسیار آسان است برای فروش. من بزرگترین کمونیست در تاریخ خواهم بود. من اجاره رایگان، خانه‌های رایگان، غذای رایگان، همه چیز رایگان می‌دهم. متأسفانه، پس از دو یا سه سال، کشوری که این اتفاق در آن رخ می‌دهد شکست می‌خورد. همیشه اینطور می‌شود، و سپس شروع به زندگی در فقر و فلاکت خواهید کرد.
🔴
غذایی نخواهد بود، مسکنی نخواهد بود، ارتشی نخواهد بود، هیچ چیز نخواهد باشد. شما از هر نظر یک کشور جهان سوم خواهید بود و همه رنج خواهند برد یا خواهند مرد. متأسفانه باید بگویم، اما ترور کسانی که با آن‌ها مخالفند، یک عنصر بسیار مهم در ایدئولوژی آن‌هاست. آن‌ها حیوان هستند! در بسیاری از موارد، باهوش نیستند اما، در برخی موارد، آن‌ها هستند.
🔴
برای آن‌ها آسان است که پیروان جذب کنند زیرا وعده‌هایی می‌دهند که می‌دانند نمی‌توانند به آن‌ها عمل کنند، و دموکرات‌ها در برابر آن‌ها نمی‌جنگند. آن‌ها به آن‌ها اجازه می‌دهند راه خود را بروند. آن‌ها می‌ترسند که انتخابات خود را از دست بدهند، آن‌ها از درگیری می‌ترسند. آن‌ها به اندازه کافی باهوش یا سخت‌گیر نیستند که با این طاعون بجنگند.
🔴
اگر آن‌ها را همان‌طور که با جمهوری‌خواهان یا من می‌جنگند، بجنگند، پیروز می‌شدند، اما آن‌ها شجاعت انجام این کار را ندارند. این‌ها دموکرات‌های اجتماعی نیستند، این‌ها کمونیست‌های سخت‌پوش و بی‌خدا هستند. این جدی‌ترین تهدید برای کشور ما از زمان تأسیس آن ۲۵۰ سال پیش است. آیا این مسخره نیست که ما در حال جشن گرفتن یک تولد بسیار مهم هستیم، و به جای صحبت درباره مسیح، آزادی و پیروزی‌های انواع مختلف، درباره تهدید دیگری برای بنیان‌های آمریکا صحبت می‌کنیم؟
🔴
این کمونیست‌های بی‌رحم به تمام ادیان حمله خواهند کرد اما، به ویژه، مسیحیت - آن‌ها همیشه این کار را می‌کنند. تمام کشورهای کمونیستی به خشونت به ادیان حمله می‌کنند. همان‌طور که می‌دانید، ما اخیراً به نیجریه ضربه زدیم و عمدتاً کشتار جمعیت بزرگ مسیحی آن‌ها را پایان دادیم. آن‌ها می‌دانند که اگر بیشتر پیش بروند، حمله بسیار بزرگ‌تر خواهد بود و، در آن، آن‌ها نمی‌خواهند درگیر شوند.
🔴
من مسیحیان را در سراسر جهان نجات می‌دهم، حتی اگر ما در آن کشورهای مختلف نباشیم، با ضربه زدن به این تروریست‌ها به شدت و با خشونت. آن‌ها کلیساهای شما را می‌بندند، مردم شما را می‌کشند. این همان چیزی است که درباره آن صحبت می‌کنند. این بزرگترین تهدید برای کشور ما از زمان تأسیس آن ۲۵۰ سال پیش است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/130377" target="_blank">📅 21:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130376">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
روبیو وزیر خارجهٔ آمریکا: لبنان و اسرائیل به توافق چارچوبی دست یافتند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/130376" target="_blank">📅 21:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130375">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سفیر لبنان در واشنگتن: چارچوب همکاری که امروز امضا کردیم، گام نخست برای بازپس‌گیری حاکمیت لبنان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/130375" target="_blank">📅 21:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130374">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f979ed21d.mp4?token=qy2yZ7yaq_ut8K83TOrfFD_A_VACrswfqbA8v0G8gbMBDKVgmOxmLOa_8-_Ed66KX3RMRnJ2F3P4Iw9mxgEMd5hEhZlpkMMGTY5W_rLFP3pvuTOG3wJXD0yeRMb9_huyPtHZI9oJ9e_ynA3uQYn4zE-ZGrR9yFBnjZq127Pb2JU4SCzz6zH_FfvNMeiHzJ7WAvP9IilOxvpUJ0tbJtEG6UHCzZEjEz1zJw2HVJ6D9o-Dwd_B2-vtXI5w1zTiuIOut_xheJUryFZVTHGwJX70J5T-fxBprBh7FygTws0XRvjTnR2pTfaWYerLSBvCB1tDlr8GKuBf8pkEgxuiUnu7iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f979ed21d.mp4?token=qy2yZ7yaq_ut8K83TOrfFD_A_VACrswfqbA8v0G8gbMBDKVgmOxmLOa_8-_Ed66KX3RMRnJ2F3P4Iw9mxgEMd5hEhZlpkMMGTY5W_rLFP3pvuTOG3wJXD0yeRMb9_huyPtHZI9oJ9e_ynA3uQYn4zE-ZGrR9yFBnjZq127Pb2JU4SCzz6zH_FfvNMeiHzJ7WAvP9IilOxvpUJ0tbJtEG6UHCzZEjEz1zJw2HVJ6D9o-Dwd_B2-vtXI5w1zTiuIOut_xheJUryFZVTHGwJX70J5T-fxBprBh7FygTws0XRvjTnR2pTfaWYerLSBvCB1tDlr8GKuBf8pkEgxuiUnu7iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان ایالات متحده مایک جانسون در مورد انتخابات میانی:
🔴
اگر در انتخابات میانی شکست بخوریم، خدا نکرده، این دموکرات‌ها، همه شما، نگرانی بزرگ نیستند
🔴
آن‌ها هر کمیته‌ای از کنگره را به یک نهاد تحقیقاتی تبدیل می‌کنند و به دنبال خانواده رئیس‌جمهور، کابینه، اهداکنندگان و دوستان او خواهند رفت. نیمی از شما در این اتاق هدف قرار خواهید گرفت.
🔴
من برنامه حفاظتی را اداره می‌کنم. ما مراقب شما خواهیم بود. ما در انتخابات میانی پیروز خواهیم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130374" target="_blank">📅 21:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130373">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
روبیو وزیر خارجهٔ آمریکا: لبنان و اسرائیل به توافق چارچوبی دست یافتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130373" target="_blank">📅 21:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130372">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
روزنامه تلگراف در گزارشی می‌گوید برخی منابع اطلاعاتی و کارشناسان امنیتی اسرائیلی احتمال می‌دهند حمله سایبری اخیر به چهار بانک بزرگ ایران، کار اسرائیل و گروه هکری «گنجشک درنده» باشد؛ حمله‌ای که باعث اختلال در خدمات مرتبط با کارت‌های بانکی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130372" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130371">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rInppMM3PLWjiJhzBq-c_Wugs-2cqnD5xQT7dDCL9Zwjl-OdJNoVeIgBWvHIG5vNyK7ND_fPrYuYALxGKuXZHGfxCUVdoNNcclwBx_52JClBRr0Fsf9vzIP6vtECmNflZaF1FBZogkGmFJlH0D9LTyrWVmjrsUN-DtSgsBdnvGPddPxeUcZXHi_7FF6HYOxdkadqO5c8k4VhF00tD6qrdxwAG8cMjh9yIwM6j0vTfK8FBcEwzY6afYLPM-yOmekfVNVLelBiO2fZEAwS7ztrPzhwcK169tEbzCoIKAw8848Tu3s7oABeTsZg763NHYdjOOrKB-D_FeSwKkNddFckVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار محبی ، سخنگوی سپاه : تنگه هرمز سرزمین ایران است و هیچ ارتباطی با آمریکا ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130371" target="_blank">📅 20:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130370">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzK_AUJBME14WO4KIyWbLfQBiBb4mmFPuLGFcIcNvu31WUyjLMkodkqHTgRGvlyQvvMQTT1phlI3zCRG64vn3O2kRaVItSGWN5OEyuY0rQdFVBvxRXc2V2boGk4I42vPAq8xKClAPds1kJX3k-OHfAY2oGWrjDid8EtXe7ZVY_KpK4hZp98m5ZJRMRR0fbbH1Q6xtHQxIDOtfRzZMIcVX7es0t3yQBoRZa4kTvmP1j0CFEgOVc6ZiWCMPx-ccyb4JfLYPZVbV0EV8ipBZeNurDSQ4UET6339l8KScDvk4kBYUOwEExsYypndqY52zvpfiAw4vGnhQjsU85BTPF0HQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از دست‌نوشته‌ای در یکی از تجمعات شبانه با حضور سنجاب انیمیشن عصر یخبندان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130370" target="_blank">📅 20:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130369">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ارتش اسرائیل مدعی تسلط بر تپه علی الطاهر در جنوب لبنان شد و گفت که نظامیان اسرائیلی کنترل این نقطه را به دست گرفته‌اند.
🔴
این ادعا هنوز از سوی حزب‌الله تأیید نشده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/130369" target="_blank">📅 20:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130368">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نیروهای مسلح لبنان در دو منطقه «آزمایشی» که توسط نیروهای اسرائیلی تخلیه شده‌اند، طبق چارچوبی که در واشنگتن به توافق رسیده، مستقر خواهند شد و نیروهای اسرائیلی تا زمانی که حزب‌الله خلع سلاح نشود، در «منطقه امنیتی» گسترده‌تر باقی خواهند ماند، طبق گزارش کان نیوز.
🔴
طرفین همچنین به تفاهماتی در خصوص مقابله با شبکه تونل‌های حزب‌الله و افزایش توان نظامی آن، و همچنین آغاز مذاکرات آینده درباره مرز زمینی بین اسرائیل و لبنان دست یافتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130368" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130367">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خبرنگار i24news: توافق لبنان اسرائیل حدود ساعت ۲۰:۰۰ به وقت اسرائیل در حضور وزیر امور خارجه آمریکا روبیو امضا می شود
🔴
یک منبع رسمی لبنانی به الجزیره گفت: جدول زمانی برای عقب‌نشینی از این دو منطقه مقدمه‌ای برای عقب‌نشینی کامل اسرائیل در آینده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130367" target="_blank">📅 20:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130366">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ : نمایش هوایی چهارم ژوئیه، بر فراز واشنگتن دی.سی.، پایتخت بزرگ ما، بزرگ‌ترین نمایش در تاریخ ایالات متحده آمریکا خواهد بود.
🔴
صدها هواپیما، از انواع، اندازه‌ها و سرعت‌های مختلف، به نمایش گذاشته خواهند شد. من تقریباً ساعت ۹ شب سخنرانی خواهم کرد، پیش از آتش‌بازی که مانند نمایش هوایی، تقریباً ده برابر بزرگ‌تر از هر آتش‌بازی در تاریخ کشور ما خواهد بود.
🔴
پس اگر به هواپیماها، آتش‌بازی و رئیس‌جمهور ترامپ علاقه‌مندید، حتماً آنجا باشید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130366" target="_blank">📅 20:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130365">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت بهداشت لبنان: از ۲ مارس تاکنون، بر اثر حملات اسرائیل، ۴,۲۴۳ کشته و ۱۲,۱۸۶ مجروح ثبت شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130365" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130364">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCkomMEcP-1iQiUcInpB7CCshgfOlAFimylpAZuAffO4nujFADbOXAOpc724Pmr7mGLY2Gga9i-qHu6nE2pqL0i5YmKLmR4nG-ZhWCd_ogr3ldvhrNsAyiMlBubEFciJyE7GURmoWFB-UsRQKHspOPmrxAqbS2cLa6ObW2ufontnxqA_IcmDhIkD_SSGDD6p203Euhm1xgvBVj3GdG614hE2v9fBtu4pzEJhBzaXLfeIIevm9rAhgI-4fS5nLmSfCaMv2E3q44J-6sLkd-FHT3j6NO947YDT28eP2AiWahPrOcNwU8UZnu8XSs8BdHQT8yP_rzgDvq8e8IyKl4DNWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / خبرنگار آکسیوس از امضای توافق بین اسرائیل و لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130364" target="_blank">📅 20:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130363">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI6Qczlei1OZIS97M72B920Cw6YE7MN8PmAkVW_xE5EINY8LpW0I44rGF44DyxLAadBzbyhSKFzkYRSop049u9dntMqp3vKYrh_kFOyThsW217RtPm204ZyzBiOJpPmOXzhHyUoOtvoSkzqa_TGwH4w7o-t3HcibOfqfZTMPD-OUtfD8p3_2dgCIP85kSg6ZYm1e9ZrnEQhu4yvAgRwkSBe3E_w-68FHDGRbZuYZWcO378bZ5bqshpAkBC15VzOwzbo_GFshRGPtB6kFabWooMl5UhNdjxFtCpFUT8qWKjWQRwnZH45Q2vcAjc1y6wDEUd77a4AgdD0LGppDeJymVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی، کشورهای حاشیه خلیج فارس را تهدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130363" target="_blank">📅 20:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130362">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1winPD-PosD-PftPg54CHMoJl8X_iX3MoQmn15C3tBWRuNvKG0XiFZ9IeZeC6sslL_dPRBKY5m1DKqf4QsogLpAtq53nvJ67rS6lIsgLUGBx7GSozQQ0uXZTG3Bt9L3FFJmDhRu3fJCo0gERMuYU-Su05LFPmA7Co34ZudKPTSNvxzbidDnpP_GT6AUO6KWTGGXBRTbN1Mc-GRUoYbfzhFuEPJu73fA7m6yUaJg3MYoZPWiDHpNnvwHcNY79RV2fsUpoaHvxGXA-2smxFx3G0yBB1nKturhIgmGctTsyzgP2cJSvRy71Syag9MZskBdNa261ZTHnUEcpASyujwucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: کشورهای اروپایی متعدد در حال بحث درباره اجرای فوری مالیات خدمات دیجیتال بر شرکت‌های آمریکایی بوده‌اند. برخی از این کشورها به انجام این کار نزدیک هستند.
🔴
لطفاً اجازه دهید این بیانیه به نمایندگی از هر کشوری که چنین مالیاتی را اعمال می‌کند، نشان دهد که بلافاصله با تعرفه ۱۰۰٪ بر هر و تمام کالاهایی که به ایالات متحده آمریکا ارسال می‌شوند، مواجه خواهند شد.
🔴
این تعرفه بر توافق‌نامه‌های تجاری انجام شده با کشور، چه اجرا شده باشند، چه امضا شده باشند و چه نه، ارجحیت خواهد داشت.
🔴
علاوه بر این، اگر آنها پیش بروند، تعرفه ۱۰۰٪ بلافاصله اعمال خواهد شد. از توجه شما به این موضوع سپاسگزارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130362" target="_blank">📅 20:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130361">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d110c5d9.mp4?token=mtB3Gbyj8-nRsPrLcq-F3O80eMwRSXI2bkhPAcNQYV_BDsOQ6YCMCQWCAPxuhQzQ7Cu-K9QQVg2aYUthpDAvKW_geQjRliA20sh8Mv6t2L3jTkLK_5UEgfncSDe3Mtkzm6dNajlxqL7FLYM2UfOIRAXOHRO6ZnroWn-rKRX2orMKbIj3ZGklFM1366xw-fPIOcnwbq3iAIN8xr8EqeIQcwItRF1h5nn1H4hbLG-zjAXNFHCxNWTqWGJT0aAmancScmL-29L-T1yW7sGZE4_y-fmaT0hscprRqznTDBC_yyaGr0lJp4oIySQ3QpD3sfmafaRYDu0DvCvtzzyOR4xQdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d110c5d9.mp4?token=mtB3Gbyj8-nRsPrLcq-F3O80eMwRSXI2bkhPAcNQYV_BDsOQ6YCMCQWCAPxuhQzQ7Cu-K9QQVg2aYUthpDAvKW_geQjRliA20sh8Mv6t2L3jTkLK_5UEgfncSDe3Mtkzm6dNajlxqL7FLYM2UfOIRAXOHRO6ZnroWn-rKRX2orMKbIj3ZGklFM1366xw-fPIOcnwbq3iAIN8xr8EqeIQcwItRF1h5nn1H4hbLG-zjAXNFHCxNWTqWGJT0aAmancScmL-29L-T1yW7sGZE4_y-fmaT0hscprRqznTDBC_yyaGr0lJp4oIySQ3QpD3sfmafaRYDu0DvCvtzzyOR4xQdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طبق گزارش ها هنوز 50 هزار نفر در پی زلزله های دیروز ونزوئلا مفقود هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130361" target="_blank">📅 20:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130360">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91151c5fc0.mp4?token=DtSDiSAONHLfZLjxxcXvVIgjZD02L9jNvuFTMbMqTYDOGtsH_nI21SwvOhlL6T1I1MQCcSUpgIHVpQg6ULQI3TAzXWE6IxgiraqPkpVB1pHdlo9HUTqxLNbd6cswhH-c4_2I9zJaaXNgL7WF7cWVMi18iREoBWdjOUu36HnwAHUkuplYvtbi-FVAekqxwP4iUuBPeqOId46LFJgiE8GsPBTfTmYejmKAJE9gHG3bS4v7QoN3AIXuySDx1H6hmtJSIveYjE5zGjUBFYK6EasofP56LArCzVBnFYB6U_oh-NwmPZI6bavCEtwtWb5Z24imstm6-EkjoDwxOn7b0ZMNoxFSU8NGl2KCczAgM1GrcxE6SFO_DpRibmYxRHCakxAKZehLRgxu6C_pln8DqNV6a7l2brDP12vZZzizBUMuyopAHQ3bK0TxE4N_iuN_auSltOzctWP9ra5aGup05IsZI2ManSvCV2zoZnFI5n0gUI7hsEn_nQg_MiRmf0n7wTMTrd4_nlJAbUCWLIVPYpSP8PRQAFuDEeVHgkeX1TQCYDHRQ7ztQfjyGXFHc62Sa9VtsvBD1TskCsxLC8rP5Stx8xFGUf6pWm4HiIc8iFrAObAaH1-iFNkAMFjvurlvUo4oPwYaJ9M3YpnK0VYHu54Kbk22URPVoV_9-eETRx_l96U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91151c5fc0.mp4?token=DtSDiSAONHLfZLjxxcXvVIgjZD02L9jNvuFTMbMqTYDOGtsH_nI21SwvOhlL6T1I1MQCcSUpgIHVpQg6ULQI3TAzXWE6IxgiraqPkpVB1pHdlo9HUTqxLNbd6cswhH-c4_2I9zJaaXNgL7WF7cWVMi18iREoBWdjOUu36HnwAHUkuplYvtbi-FVAekqxwP4iUuBPeqOId46LFJgiE8GsPBTfTmYejmKAJE9gHG3bS4v7QoN3AIXuySDx1H6hmtJSIveYjE5zGjUBFYK6EasofP56LArCzVBnFYB6U_oh-NwmPZI6bavCEtwtWb5Z24imstm6-EkjoDwxOn7b0ZMNoxFSU8NGl2KCczAgM1GrcxE6SFO_DpRibmYxRHCakxAKZehLRgxu6C_pln8DqNV6a7l2brDP12vZZzizBUMuyopAHQ3bK0TxE4N_iuN_auSltOzctWP9ra5aGup05IsZI2ManSvCV2zoZnFI5n0gUI7hsEn_nQg_MiRmf0n7wTMTrd4_nlJAbUCWLIVPYpSP8PRQAFuDEeVHgkeX1TQCYDHRQ7ztQfjyGXFHc62Sa9VtsvBD1TskCsxLC8rP5Stx8xFGUf6pWm4HiIc8iFrAObAaH1-iFNkAMFjvurlvUo4oPwYaJ9M3YpnK0VYHu54Kbk22URPVoV_9-eETRx_l96U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تام هومان وزیر مرز های ایالات متحده آمریکا: من به اندازه‌ای که به پدر خودم احترام می‌گذارم، به رئیس‌جمهور ترامپ احترام می‌گذارم... من می‌دانم که در درون او چه چیزی وجود دارد.
🔴
اگر می‌خواهید رئیس‌جمهوری بی‌نقص داشته باشید، بهتر است منتظر ظهور دوم مسیح بمانید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130360" target="_blank">📅 19:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130359">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
تام هومان، رئیس مرزهای ترامپ
:
من نمی‌خواهم حتی یک کلمه دیگر درباره دروغین بودن رفتارهای غیرانسانی رئیس‌جمهور ترامپ بشنوم. او هر روز جان‌ها را نجات می‌دهد.
🔴
وقتی رئیس‌جمهور ترامپ مهاجرت غیرقانونی را ۹۷ درصد کاهش داده است، چند زن تجاوز نشده‌اند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130359" target="_blank">📅 19:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130358">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ارتش اسرائیل: نیروهای ما در حال تحمیل یک واقعیت امنیتی جدید هستند که به حضور حزب الله در این منطقه استراتژیک پایان خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130358" target="_blank">📅 19:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130357">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ارتش اسرائیل مدعی تسلط بر تپه علی الطاهر در جنوب لبنان شد و گفت که نظامیان اسرائیلی کنترل این نقطه را به دست گرفته‌اند.
🔴
این ادعا هنوز از سوی حزب‌الله تأیید نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130357" target="_blank">📅 19:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130356">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyJJiQ9f9em8E6tspjH38Ow3Ftwp9g-_3sMfK7w8JwVyu5s0FNEySP4SsVFgw-JmMSajMcu7hDmVdLLbYz0X8RCIiAj_4H03evN6edfVQ9iAZoFGM2jIZ-F6P5F1-LH_1BJuu3IvxQ7HhELfGLJ-vRFRUwPbLPoecEGzREkabxBxkjKMtMGJIk2AzuJEjL_8tPiLxIl7WNsMhvAbDCVdew6odewe2lwOy8-6WZIHMQbBrdyiQHXLG54iQ_YLGyAvUgySJFZRZ9YvQ2YLSpw2w4SjhlTKkhUlrVjNBiv7-NjJ2zAmXsxVyFQv6ZJhmEJgMAuVxr0npOGdDTwByU8txg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ:  ایران حداقل چهار پهپاد تهاجمی را در یک جهت به سمت کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
🔴
یکی از پهپادها به عرشه یک کشتی باری برخورد کرد و ایالات متحده سه پهپاد دیگر را سرنگون کرد.
🔴
این نقض واضح آتش بس است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130356" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130355">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
فلاحتی، امام جمعه رشت: شعار مرگ بر آمریکا همیشه باقی است.
🔴
ما با مردم امریکا مشکلی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/130355" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130354">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
پرس تی‌وی: یک خط ارتباطی ایران و آمریکا در تنگه هرمز ایجاد شده است تا از حوادث نظامی جلوگیری شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130354" target="_blank">📅 19:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130353">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
منابع داخلی: حملات امروز اسراییل به لبنان نقص اتش بس محسوب میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130353" target="_blank">📅 19:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130352">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTLC_zxPKmF2Uu66eHorBYs7q5pXdc6JKSqn2M3-f4-XinesDYGnLkJsRFsSWWVF-n3oHjwTFHTVMOzvi_Z6PF823f8xKwEMka8tQH-8y9xhe_sSzlPZ5gqG7cR3J5Uzk66YgEULQBCmmJz3GN94pEWwaYJgVAeIXSIWddmGcBokSfU3GnCkf3gQSyaq7gX80Vfr2vhrNKfzYb6ZS4WyoDH1eXSj8z_GQ-Ma9NbwWmmOfMxsZ6JwB00We3kro2NheUzMwFmxvhkO5wCETOOKiJh2yxgcurLw9VuIp2w7-bSG8IOELYNHVsuOkqh53Ms5KHU1G074vwCmnhwylQYaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: همین الان اعلام شد و من لزوماً از صحبت درباره آن خوشحال نیستم، زیرا اصلاً خوشایند نیست، اما دولت ترامپ بالاترین میانگین نرخ بازداشت روزانه توسط اداره مهاجرت و کنترل مرزی (ICE و CBP) را دارد، از جمله کل بازداشت‌ها و دستورات نهایی اخراج، که به مراتب بیشتر از هر رئیس‌جمهور دیگری است!
🔴
دستورات نهایی معلق به دلیل دادگاه‌ها به شدت به تأخیر افتاده‌اند، اما این نیز یک رکورد است. دونالد ترامپ با وجود اینکه اعداد خود را دستکاری می‌کنند و افرادی را که هرگز حتی تلاش نکرده‌اند وارد کشور شوند نیز در آمار لحاظ می‌کنند، بالاترین مجموع اخراج در ۱۲ ماه را به مراتب نسبت به هر رئیس‌جمهور دیگری دارد.
🔴
همچنین، میانگین روزانه دستگیری و بازگرداندن به کشور، به مراتب بالاترین میزان تحت ریاست جمهوری ترامپ است. هیچ رئیس‌جمهور دیگری به این ارقام نزدیک نمی‌شود.
🔴
بنابراین، وقتی این لایه‌های خبری، کارشناسان، دمکرات‌های احمق و کمونیست‌ها سعی می‌کنند استدلال کنند که ارقام باراک اوباما با ارقام دونالد ترامپ قابل مقایسه است، خوب است افرادی مانند «شانون بریم» که به «شیر و نان» (Milk Toast) معروف است و دیگران، کمی مقاومت کنند — فقط کمی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130352" target="_blank">📅 19:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130351">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
منابع العربیه: دور آتی مذاکرات میان آمریکا و ایران به‌طور فنی در سطح کارشناسان و با حضور میانجی‌گران طی روزهای 28 و 29 ژوئن در بورگن‌اشتاگ سوئیس برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130351" target="_blank">📅 18:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130350">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وال استریت ژورنال: پنتاگون در حال بررسی انتقال نیروها به پایگاه‌های دورتر از برد موشک‌ها و پهپادهای ایران است
🔴
ارتش آمریکا در حال بررسی بازسازی پایگاه آسیب‌دیده در بحرین، کاهش حضور در کویت و عربستان و انتقال نیروها به پایگاه‌ های دورتر از برد موشک‌ها و پهپادهای ایران است
🔴
به گفته مقامات آمریکایی، احتمال دارد برخی از ساختمان‌ها بازسازی نشوند.
🔴
مراکز فرماندهی و کنترل ممکن است به زیرزمین منتقل شوند و سایر قابلیت‌های نظامی‌احتمالاً به طور گسترده‌تر در سراسر منطقه پراکنده خواهند شد.
🔴
اسرائیل یکی از مکان‌های مورد نظر برای ایجاد یک پایگاه جدید است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/130350" target="_blank">📅 18:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130349">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی: از کشتی‌ها می‌خواهیم که با پیمودن مسیرهای غیرمجاز برای عبور از تنگه هرمز، خطر نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130349" target="_blank">📅 18:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130348">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
عمان به متحدان اروپایی هشدار داد که ممکن است نیاز باشد هزینه‌های کشتی برای عبور از تنگه هرمز را پرداخت کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130348" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130347">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
روس اتم: متخصصان در هفته‌های آینده به نیروگاه هسته‌ای بوشهر بازخواهند گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130347" target="_blank">📅 18:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130346">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=JMjREAO0_vWokp1_DWyPRhtJAjWI_tQgttjRGmdr--pQLn4U_h7-zilgSkHJeLMq2KPYLrS_jqAaTDBSp18qw0eMfesimBVqdRS0lz-SVKB3NNuF7QQDLq9Ozyo5RmM8L9aG2tMOMBVkq_qGx05Wqcu4RN6DNvWSr47edbrb56-FhV55bQ_3Blr7mxrlnelzWNNKZQ1PFw7dV-cD2XGKcxSAoh6aZKc2tvvq1XyPxDXX7YlUabP-UzmD8WDD0p972coXEjGJinf1DSHaZ1pyToWYCexEsm5C94adPsn3dkUIZD_edT4ozJ5vE-xVsx9aZ5b9BnCEwWRMkez6gvTWHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=JMjREAO0_vWokp1_DWyPRhtJAjWI_tQgttjRGmdr--pQLn4U_h7-zilgSkHJeLMq2KPYLrS_jqAaTDBSp18qw0eMfesimBVqdRS0lz-SVKB3NNuF7QQDLq9Ozyo5RmM8L9aG2tMOMBVkq_qGx05Wqcu4RN6DNvWSr47edbrb56-FhV55bQ_3Blr7mxrlnelzWNNKZQ1PFw7dV-cD2XGKcxSAoh6aZKc2tvvq1XyPxDXX7YlUabP-UzmD8WDD0p972coXEjGJinf1DSHaZ1pyToWYCexEsm5C94adPsn3dkUIZD_edT4ozJ5vE-xVsx9aZ5b9BnCEwWRMkez6gvTWHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌کمانی و برگزاری مراسم حمایت از جامعه LGBTQ در ورزشگاه سیاتل
:
ما اینجا برای فوتبال هستیم، نه مسائل دیگر. تمرکز ما بر روی مسابقه و کسب موفقیت است. درباره موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
@AloSport</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130346" target="_blank">📅 18:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130345">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
بانک ملی ایران در اطلاعیه ای از اخلال مجدد در خدمات کارتی این بانک خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130345" target="_blank">📅 18:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130344">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6viX3-gbU0R0PWiCl3tfdvpEborkXMTBmrBUXCRDr7g4SfyLjKmXBrrsiwKtxp3scKqB8c3wf6GckSYblbukC98PBEi__dD95OW3yzuf3kjiqFAyrpA1tJiz-fD3-eeb5iMFMc-gtklYbXe0GK7vppFsN_ym_k58VQZFTk9N8sWXHDvFwqLlOLuAO31dONnIlfZIa36Hcvbu0QIYNLhBw18dhO2aWwjSYoQTnUoc6yWyvyTOWMLrdHkKACGVmowtEmUT30nmDYmoyE4azQrfj_XWoNqWuaMcOBSvRa5k437JANRKwu1U2gzfP2VaOFsuYV_ByzYeK8oC4SE-3BEjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان به همه مشاغل علاقه داره به‌جز ریاست‌جمهوری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130344" target="_blank">📅 17:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130343">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
۲۲ خدمه ایرانی نفتکش توقیف شده توسط آمریکا، در کراچی تحویل سرکنسولگری ایران شدند
🔴
۲۲ خدمه ایرانی یک نفتکش که توسط ایالات متحده در آب‌های بین‌المللی به طور غیرقانونی توقیف شده بود، با پیگیری های سفارت جمهوری اسلامی ایران و اقدامات تسهیل گرانه دولت پاکستان، امروز به نماینده سرکنسولگری جمهوری اسلامی ایران در بندر کراچی تحویل شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130343" target="_blank">📅 17:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130342">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نعیم قاسم، دبیر کل حزب‌الله:
«ما در کنار ایران خواهیم ایستاد و می‌خواهیم متحد باشیم زیرا مشخص شده است که قدرت شما، همراه با قدرت رزمندگان مقاومت در میدان، به ایجاد تعادل مناسب برای شکست اسرائیل و اخراج آن از سرزمین ما کمک می‌کند».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/130342" target="_blank">📅 17:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130341">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">دعوا سر نذری تو همدان
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130341" target="_blank">📅 17:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130340">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران، اسماعیل بقایی:
همسایگان جنوبی باید پاسخگو باشند: چرا خودشان برخلاف اصل همسایگی خوب و قواعد بنیادین حقوق بین‌الملل، به تجاوز علیه همسایه مسلمان خود دست زده‌اند و اجازه داده‌اند از خاکشان علیه ایران استفاده شود یا موشک‌هایی از آنجا پرتاب شود؟
و چرا چشم بر مسابقه مخرب تسلیحاتی و خرید و انباشت صدها میلیارد دلار انواع سلاح‌های پیشرفته که هیچ توجیه دفاعی ندارد، می‌بندند؟
و چرا تجاوزات مکرر رژیم صهیونیستی به کشورهای منطقه و اشغال سرزمین‌های فلسطینی، لبنانی و سوری را نادیده می‌گیرند؟
چرا در برابر زرادخانه هسته‌ای اسرائیل که خارج از نظارت‌های بین‌المللی است سکوت می‌کنند، در حالی که توان دفاعی متعارف کشوری که بارها تهدید و حمله از سوی کشورهای همسایه را تجربه کرده، به عنوان «تهدید» معرفی می‌شود؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130340" target="_blank">📅 17:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130339">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8be098ed9.mp4?token=uLRZ1UmSdJLSCnyA0JKQpblHiTROFDW46ExU2LpzhBh1-vwN4uxEhdncwVa5fAmP7NBuh-XlLsw3Jd5z_C40zjM_9LnhTZhHSCK8upAEa5AztKcWuz0C8kPlMigTbvUzLWiI2YgSVVUmHoG286TDP9u2s1xboMnEbKL6Dgsjv-slLqTRkcAsW1k_LyazZOY2I5hQeTQpmIFngvIghIEV15zOHvZ-sv7yroVprc6wqG8wZnM4KP-ZYwhYzfrtqY7fEKdybh-BnLUg9az-mfUgusuEvCADXFLIzOrJSbZVyLItQUdIgzRhWJAvb8NMkhc98fWUpdpIuWRca_rF6eUqFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8be098ed9.mp4?token=uLRZ1UmSdJLSCnyA0JKQpblHiTROFDW46ExU2LpzhBh1-vwN4uxEhdncwVa5fAmP7NBuh-XlLsw3Jd5z_C40zjM_9LnhTZhHSCK8upAEa5AztKcWuz0C8kPlMigTbvUzLWiI2YgSVVUmHoG286TDP9u2s1xboMnEbKL6Dgsjv-slLqTRkcAsW1k_LyazZOY2I5hQeTQpmIFngvIghIEV15zOHvZ-sv7yroVprc6wqG8wZnM4KP-ZYwhYzfrtqY7fEKdybh-BnLUg9az-mfUgusuEvCADXFLIzOrJSbZVyLItQUdIgzRhWJAvb8NMkhc98fWUpdpIuWRca_rF6eUqFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوروش احمدی: اگر توافق نشود، ترامپ به سمت محاصره می‌رود، نه جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130339" target="_blank">📅 17:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130338">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
هشدارهای حمله موشکی در امارات متحده عربی فعال شده‌اند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/130338" target="_blank">📅 17:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130337">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
هشدارهای حمله موشکی در امارات متحده عربی فعال شده‌اند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/130337" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130336">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPt8FcpQi6NZ7MIOQM0Yb6L_5Kb5UR_mz6J6tIcI6WiMIR8zfZrZb3PA2LUMd5St5PCLyZzSFL4bLcn8cCeB-WoeqxJyquSZtFAcT9ic1VMZG_6GTqPXkLPeZC4fAFEzVxvpiPkNsa5sE2g60bwjeMdUxYUjiw0_J2Ht04y1MggAstXhZIVUmFQPIQ0glKkmwsgXfjnrsTdfbJlERKh1E3-VBgE9j0r1cybCghIZ3Juse5XgS075YWMNjYYnRJ0mNHsfaNHDVWUoXyKB4qEFaaByNgfQFPrisISBkGrWFiQA9F2ubOgoLyGKsNCp5iQmZ7Bo1c0-mKyS6f4O7eLIaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدارهای حمله موشکی در امارات متحده عربی فعال شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130336" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130335">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
العربیه: دور بعدی مذاکرات آمریکا و ایران در ۲۸ و ۲۹ ژوئن در بورگنشتوک برگزار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130335" target="_blank">📅 16:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130334">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a208c87a.mp4?token=j02lhr7jSc3X-dMa2N0pmY95ZqrlsE337RICGx-0GFy_lf_6zZhJp2BmlsLdU3fTr1ksRfGwlGXSvAWjqnQE4DvbzgaXLkJWnneWkAYSnGQCuOHZp_xRuCIG-xuyro0j3qWUrZykKAcF1JPA7D7YeN6-o3vWBK-tZ3UwAaSWxfMlrcJ54o9_aS3hBmlIGR8L-HG2Hsz22K3wtodsWevqmRzqwRZoQAzWpv7ZDXyRwVb7_XsYu9Ty_FW4ngIJXyDwVPigagZAV6yg72zPWFsprBxul_JEJYV5SuEzn1RXlEIIKytY6bkIcHgqtPu_aYUKhJj7RLBX-wBgiUnmCVBiNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a208c87a.mp4?token=j02lhr7jSc3X-dMa2N0pmY95ZqrlsE337RICGx-0GFy_lf_6zZhJp2BmlsLdU3fTr1ksRfGwlGXSvAWjqnQE4DvbzgaXLkJWnneWkAYSnGQCuOHZp_xRuCIG-xuyro0j3qWUrZykKAcF1JPA7D7YeN6-o3vWBK-tZ3UwAaSWxfMlrcJ54o9_aS3hBmlIGR8L-HG2Hsz22K3wtodsWevqmRzqwRZoQAzWpv7ZDXyRwVb7_XsYu9Ty_FW4ngIJXyDwVPigagZAV6yg72zPWFsprBxul_JEJYV5SuEzn1RXlEIIKytY6bkIcHgqtPu_aYUKhJj7RLBX-wBgiUnmCVBiNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این سکانس مختار دقیقا برا این روزهای جلسات دورن نظام ایران ساخته شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/130334" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130333">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554e768468.mp4?token=WKBlNIh8non7bTwVdCKCvZb6PwLQOJQL6CGTiXvv0jEMp4pMipj7RrM-tfOTPAdkV3qoNFqWbKj5fHGdnS9j9YPInMZYH7NwkI2u-cbxeimqyMIWiYJng8QVDRRguc1IOnMCMk2FoG6jvqIqH33Z2FaGZJNSfgAzlK-7ktSbLk9GifOGTQ4wsCsh1oTdSiw3r6G3S3kqWsRIM-zX1cZ0NUYU3D6kuBQPH1DFuXoVwbci5_7rnLKXXOamUNvm1lCkaaVHdE_zGzCoFvaiTKj5gZL2PIvRltObK8n23wia_IHt7NY86OTaqgZu4dsey-aoy0_Urf7-kQ4hPg0LC89ehQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554e768468.mp4?token=WKBlNIh8non7bTwVdCKCvZb6PwLQOJQL6CGTiXvv0jEMp4pMipj7RrM-tfOTPAdkV3qoNFqWbKj5fHGdnS9j9YPInMZYH7NwkI2u-cbxeimqyMIWiYJng8QVDRRguc1IOnMCMk2FoG6jvqIqH33Z2FaGZJNSfgAzlK-7ktSbLk9GifOGTQ4wsCsh1oTdSiw3r6G3S3kqWsRIM-zX1cZ0NUYU3D6kuBQPH1DFuXoVwbci5_7rnLKXXOamUNvm1lCkaaVHdE_zGzCoFvaiTKj5gZL2PIvRltObK8n23wia_IHt7NY86OTaqgZu4dsey-aoy0_Urf7-kQ4hPg0LC89ehQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اقلیت کم عقل در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130333" target="_blank">📅 16:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130332">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4cwjgEbknPYGFEeZ8lcdfqFqxDrXyxSz7EUseLbvNdy4iZTuWvq7Tt4qE9Xnm8YqXBMVt_xMuE7T2vGWgR_itTZqZpos3VmhmiG0EOb3O_QpuUPOP-TM_Q0GYQrHFym6MLXj8liEHMSHtr-mFjf3sDzdjJW-4amCr0pdrEKDW0ZnOuOLjhUL1Qg5I7ZIHxmUTXnDFqVFmAlvTopIBSQevTpteqdClH_CMeEUJ6650LUcvbnxTh4VgFOCOmO9TgEPOiayFe-9jRQWR9MPMoXshxO2OdIHQo1Hvi2ANaDn73t41gEdL9Zyeho8mi4vXRa1WwrbIdVbneiK0qR7DpU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش وزیر دفاع اسراییل به سخنان سردار قاآنی: اگر ایران به اسرائیل حمله کند، بزرگ‌ترین اشتباهی خواهد بود که تاکنون مرتکب شده است.
🔴
نه هرمز و نه شلیک به غیرنظامیان در اینجا به او کمک نخواهد کرد. هیچ چیزی ما را متوقف نخواهد کرد.
🔴
نیروهای ما آماده‌اند تا کار را تمام کنند.
🔴
وی در انتهای توییت، پزشکیان، قالیباف و عراقچی را تگ کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/130332" target="_blank">📅 16:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130329">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OvMPV6le7MpxWrQX3j6a66x7S1w2B50drWkh6bi0MUJiF3Ps3mpOMyJBEXSwuM0z-p5zdsMXAuIkqd7kWamXRbhyV86vk8-Ga6NDP7BwET0WDUX-ApozXcCMbSn-Y7yxb0lIRytlKRFaOjXmq97Vl4rcpNJCM5TqZwIhadSNz3cC699ic0LSeXZWNJaIjBohbFw9_9rK8icbtbft7VoOK0YQO_5LJ9lIHbN3kbYr7Z0qgepWWn8iaINNsPMT5CaRFkfWEVyRzgOfObCeBecHYYgSL0g9FrlC6feIEgbNxFRoICMmzrNM11PWMpqqRw8RMDYwLcZ-KbBiPTDgnGXbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWrsuXrCTMkv3C45ooBXW_lLUbUQNL18w27LZw28tUxruPa5iku44Hd24BqIvK7maR__oC-TXdTvGK0Gs9t6BRNFvM-jEA43yah33dXZYFOEIVGK1L4dOyfImzKgWjiac12KGDncWCNiTx-UpZrQAfHbMmo4VQyo3akwJHYh6mfhssB2sQOwNXfVPUXFE6tGIdZvSM7nj_i2qGmGfiopdZdbj_Vz90kGR6yW5U4GHI25z5ViuPoFI1NHIdf8IdFBIO0GVDbRsvrFAyigSYxTSXIW7FfS6fXaR-LYmkWaSVfK7rPbeRdHgmGuWqy8TsnzVgYF6t17m_gcRD8A9RxCMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=FonFw81km6GMQbSMCZj7sPaju8bXodfhzwNV3cIjQbpXGYkSnMjzqwRaUpM9euxXXTGpRa3z6H3MuedKbgwrdZJ9I-Dyb_yst4fOoXs7MwM3TdcaJLks5GmE4qgQIELOCtPnqljwYiWRJHYUG5kNXhdvXh7arX7HNb7XnK5gcveXQQCtACO75F1iAut0ocpg0MDf2a1KOe35G38FFAjyUm7RWj62EWJgqin5ThsSq0i037cSy0eOUy-iKTMK6ebYo9HxdvulFeurOnb_1QW0vSo0ieT3wrdv2yWeTU9iqhEY4yVEJMdH3FvV0FREMSijDYq2vZg9RHsCwYkFkkpy7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=FonFw81km6GMQbSMCZj7sPaju8bXodfhzwNV3cIjQbpXGYkSnMjzqwRaUpM9euxXXTGpRa3z6H3MuedKbgwrdZJ9I-Dyb_yst4fOoXs7MwM3TdcaJLks5GmE4qgQIELOCtPnqljwYiWRJHYUG5kNXhdvXh7arX7HNb7XnK5gcveXQQCtACO75F1iAut0ocpg0MDf2a1KOe35G38FFAjyUm7RWj62EWJgqin5ThsSq0i037cSy0eOUy-iKTMK6ebYo9HxdvulFeurOnb_1QW0vSo0ieT3wrdv2yWeTU9iqhEY4yVEJMdH3FvV0FREMSijDYq2vZg9RHsCwYkFkkpy7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
🔴
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
🔴
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
🔴
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
🔴
شمار تلفات هنوز مشخص نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/130329" target="_blank">📅 16:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130327">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSOGSs1NJdRR_SbZ1Lju9x4lFXBQe9kGiN9o5mPq6YgDvsQYD1kWgf0JNDXB50mvIAIX1LulzkI0xmGvLG85_yx6FVp5Kq_EppLYnUek7mQFo8Edv0xVBSeEhfTnDdIN5h6JZefJnSs7FkFIznJ0mkFYQ8jr5TfERUSN0pa1Xr27mERRuPT_jLpmCM6i5SaxcUfG57Zdk8Q_SR1ZF_24qr4nyjrmfuXWk1Fwgl6nflA-VdkUYMY7ufUdL7zxOfS2AmE-NLbTJgFApKvlvtf1DsFgmzAlYdC9tf6YWF_D5hP2jCCdHpkuzSJ9DgD5Q7VVYuSs6Iv7XX8Zst5MukJM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازی ایران و مصر که به عنوان مسابقه «افتخار همجنسگرایان» نامگذاری شده؛ فیفا اجازه داده فردا همه با نماد و پرچم رنگین کمان
🏳️‍🌈
بیان ورزشگاه و معلوم نیست صداوسیما چطور میخواد بازی رو پخش کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/130327" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130326">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3a84c436.mp4?token=MngbsYZekmF9KaeVbVhanHFBCXoBZ3ArzN_PyXSvFgvellBz5sR8xFyHrWSRq9c-3Ubo2pg-XbM2XUuuxYdQSRCUW_SQD3-2rIDY2AA0RCo4H7--OxLrtL-dtRteU0_CFF1tSdGx03Di5UHVzhRHPLGjG0y3bTze7hRnfqO-3N8AEOgCB-3UgLdOE40ms6_VOvx2SeIV5yHPiYCvKEUFq5595B_h4lXe2PLMHRgbXahaHj5lbvNAfHq1GDXFvtcjNyFM7OvfVhby1eDylFvLLvfPza9UDgYar9iMx_DIyBaMH9fTcH7XbSFIY90zyxeEfe1jaB0Xhck4aODh1oLqmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3a84c436.mp4?token=MngbsYZekmF9KaeVbVhanHFBCXoBZ3ArzN_PyXSvFgvellBz5sR8xFyHrWSRq9c-3Ubo2pg-XbM2XUuuxYdQSRCUW_SQD3-2rIDY2AA0RCo4H7--OxLrtL-dtRteU0_CFF1tSdGx03Di5UHVzhRHPLGjG0y3bTze7hRnfqO-3N8AEOgCB-3UgLdOE40ms6_VOvx2SeIV5yHPiYCvKEUFq5595B_h4lXe2PLMHRgbXahaHj5lbvNAfHq1GDXFvtcjNyFM7OvfVhby1eDylFvLLvfPza9UDgYar9iMx_DIyBaMH9fTcH7XbSFIY90zyxeEfe1jaB0Xhck4aODh1oLqmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده تا از مزایای عدم توافق و مقاومت و بدبختی بگه
🔴
نون این جریان تو بدبختی مردمه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/130326" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130325">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
مهار آتش‌سوزی در پتروشیمی کارون
🔴
روابط عمومی پتروشیمی کارون از مهار آتش‌سوزی امروز در این شرکت خبر داد و گفت: این آتش سوزی تلفات جانی نداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/130325" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
