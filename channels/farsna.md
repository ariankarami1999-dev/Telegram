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
<img src="https://cdn4.telesco.pe/file/tL4PrONFlb9XBXACl9nhLr6KAzjkq6VCdCCkcH7jOlK7icl5eRQa78Z9nIl2G9gvgWy5_xUqDwZErEjdZsklDz0_FvQZVJ6yHhbUIdlj91nkMx22XFoJQVKLlDsJc2uRBvOB2VGvvUALYVgOmYu1BKJmkToFem09mWDk_5qaGLN5VxC-bJ9OB6-CdpZMCdI9tPgDgnxtVLLESlmr3_NiTjrnOFlWforThTjZzd_24Xdj7P3riy7xuKfuNfO7t7daAEPcFPzUrruWKnyIgq1ZfQ66h7koA5N_RXI4V1KZeMNdXB_6HOHPrYy5kcRSsrJEEZJECysWtp43X5O8Dn_XiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 14:07:21</div>
<hr>

<div class="tg-post" id="msg-460669">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d0321e63b.mp4?token=GJd6bUbIC77QMw64oT_ZqoOzubqRqOnA13fIXdNFhLxDn0zyqHiD0D3iJozCUcS0w88kTiWTNqWLqDKTwN9RI2LB8sq1j02NWpSo1VQlaTE3KYnR3vmxEHh7zixwzwX3R0UFzYOwXZ3OIvAye9PTL6LLr5zNqsdH-96UVmhwk4WBIftKIz91Ns0MIwlrmqGV2Uk6ESjo8cagUSFfNjg4r3Ie09GorojGBVypHvUlj3KZGM8jPkGZ_gtGyZAS4s7HO6dv95OYCPLmjgt13ZwK4jtCS1Tm7crw834KK4BxMchRvbO6d2jn30AoBt26dBdH-1ZRWyiNV4rrgYKLdJgWvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d0321e63b.mp4?token=GJd6bUbIC77QMw64oT_ZqoOzubqRqOnA13fIXdNFhLxDn0zyqHiD0D3iJozCUcS0w88kTiWTNqWLqDKTwN9RI2LB8sq1j02NWpSo1VQlaTE3KYnR3vmxEHh7zixwzwX3R0UFzYOwXZ3OIvAye9PTL6LLr5zNqsdH-96UVmhwk4WBIftKIz91Ns0MIwlrmqGV2Uk6ESjo8cagUSFfNjg4r3Ie09GorojGBVypHvUlj3KZGM8jPkGZ_gtGyZAS4s7HO6dv95OYCPLmjgt13ZwK4jtCS1Tm7crw834KK4BxMchRvbO6d2jn30AoBt26dBdH-1ZRWyiNV4rrgYKLdJgWvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از حضور خادمان حرم رضوی در جنوب ایران
🔹
کاروان خادمان امام رضا(ع) با سفر به هرمزگان، در روزهایی که جنوبِ قهرمان ایران آماج حملات استکبار بود، به دیدار خانواده‌های شهدا و جانبازان جنگ تحمیلیِ آمریکایی-صهیونیستی رفت.
🔹
خدام رضوی همچنین با حضور در میان مدافعان «ایران امام رضا(ع)» و شرکت در اجتماعات شبانه مردمی، پیام‌آور دلگرمی، امید و معنویت حرم مطهر رضوی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 312 · <a href="https://t.me/farsna/460669" target="_blank">📅 14:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460668">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8YaWB-8Yb5W1T7_a7LxxmVy_rxZ6vTbVdYoCnGOWXXAa6W4QEs0e5ynGXlgs6l1PkRWLgdhc4OvY2xDdQEhru3_mfqFmrcIVXnTgQqiefKxz8PDwWrHY0JrQSx_b9lKIVAvUV2DKHCADp-4bhDE-CoRXIXlLccp0tEy-sL30EZMhhm7zVMO7Q3vsJvukjjr71XRvJdBJBC2GaybpuiJz3LafbliVyzblzwIOKRAwzcFGQRHeIaNdvCwEtyfQK8_xEVs6Azg1fFnebZGmRb9FHzMUZ1nNdsontQs0Mf0UUGiux7BpO6lR7a6yU2nhdw60y5egaMXCVd6bxNW-jAKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل تاپیکو عنوان کرد: آغوش باز تاپیکو برای دانش‌آموختگاه شریف
مدیرعامل شرکت سرمایه‌گذاری نفت، گاز و پتروشیمی تأمین (تاپیکو) در مراسم جشن فارغ‌التحصیلی دانش‌آموختگان دانشگاه صنعتی شریف، با تبریک به دانش‌آموختگان، پشت سر گذاشتن دوران سخت و پرفشار تحصیل و دستیابی به موفقیت علمی را حاصل تلاش و پشتکار آنان و همراهی خانواده‌ها، استادان و مدیران دانشگاه دانست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 622 · <a href="https://t.me/farsna/460668" target="_blank">📅 14:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460667">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخانه ریز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHyUDgrWOu1KCUf9K_OHKnzi_Y3vkalmHd6AT6SRNEpf3tl3XsbR8E8HvSDUJYA2ErJ_JqtLNqRuZm5RqOHFK7n2O0jtP3VrOFsI9Hvhz36XwTpvIbXF59G-vtVuthv8MKWI552LVAtL9mG5HsLsSVBtI3wbVaGQfplkaQo1Che3nu_xB6GY_FYPp82CszmM8ely0PhZQhT5_MIIVMyyiY6gjneFcSDDG4M1lA5is4Smyk_EfwaK1mr9t_JHsb4GqOjgfaq519QMmlw4Lr_72zAsMVjR8NqmR-P2nsYkPx90UxNld_XsHnRxMjpEnbr32rTNlh_ZZN6xhCbq2Wwnew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرحله دوم فروش «خانه‌ریز» در شهریورماه؛ چهارشنبه ۱۸ شهریور
در ادامه برنامه‌های فروش «خانه‌ریز»، دومین مرحله عرضه واحدهای پروژه «فجر» در منطقه پنج تهران، روز چهارشنبه ۱۸ شهریورماه از ساعت ۸ صبح آغاز می‌شود.
نخستین پروژه
#خانه_‌ریز
با عنوان «خانه‌ریز فجر» در منطقه پنج تهران و در بلوار آیت‌الله کاشانی در حال ساخت است. این پروژه شامل ۵۴ واحد مسکونی با زیربنای کل ۱۰ هزار و ۲۹۰ مترمربع بوده و در حال حاضر در مرحله گودبرداری قرار دارد.
علاقه‌مندان برای کسب اطلاعات بیشتر و مشاهده جزئیات فروش می‌توانند به سکوی آنلاین «خانه‌ریز» مراجعه کنند:
https://khanehriz.shahrzadcity.ir
@KHANEHRIZ_IR</div>
<div class="tg-footer">👁️ 647 · <a href="https://t.me/farsna/460667" target="_blank">📅 14:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460666">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 649 · <a href="https://t.me/farsna/460666" target="_blank">📅 14:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460665">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ8jQkO-jk_oTk3-14pdYSflco-vBzguTWUBzD87nBgp40Pn2T6sFNAAnwx3aVE_NXccQ4KOJAeFFprDPDrGSbg0gZlke-s4aBlYTGUa-JhLJuKCTTZcZPC_oLlfY4QfZKZs4aHaI5Euh6tpM75wj5_cmW3fYglbPaj4yWV_PaiBBLi43ngbaWQTAPI9-IDC3g3ilsjq0_F9DZrJLECGqw2Hes7Jau_UCts6oq7tnaEV85ykB6jOYakJtf65t1itw8f41MLdjn1NghqnVvL-w-bZNsJE0iB38DU0WgsyTLHqxA5cUIDzKM3PNd07cZlEkkc1bo8zbLOH3R3TtOyfIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر حیدری: تغییر معادلات جنگ از سوی ایران خارج تصور دشمن بود
🔹
جانشین ستادکل نیروهای مسلح: دشمن پیش از آغاز درگیری‌ها، بر مجموعه‌ای از سناریوها و محاسبات خود، حساب ویژه‌ای باز کرده بود.
🔹
آن‌ها تلاش داشتند با بهره‌گیری از جنگ ترکیبی و همچنین استفاده از عوامل وابسته به خود در داخل کشور، ایران را با آشوب، ناامنی و بی‌ثباتی مواجه کنند.
🔹
ایران با بهره‌گیری از ظرفیت‌های راهبردی خود، توانست تأثیر قابل‌توجهی بر معادلات اقتصادی جهان داشته باشد.
🔹
دشمن تصور نمی‌کرد ایران بتواند معادلات جنگ را تغییر داده و عرصهٔ نبرد را به سطحی منطقه‌ای گسترش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/farsna/460665" target="_blank">📅 13:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460663">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDnuFtaEVFEAbxgdSaUQLo8A-3B3ylKVFOX2feWiRLYn-EXShMxdC3a6bXMR76GhzFnk4hFIWhlqjODk6HsZQbvdOR1x0rNuMyHj77CI4DqqfSgYDNAQtAC6mgnKfi6Ukn5gDUYiNauwSosN7TId2tOlnja6Ce08BVLdDIZeVCYGiQZJ0xsYQDU5WC7FkoyVSP5Bd8R54N-_JD1bFCNLnc164PKTbe27-1GIs8Nwjr7bUtgFSpj9ESgHkzrwW5O9OEmDvZeWDdnpDONUxvucirAuMr2qJbkJ6DVrB6FZ4f6nrdjV0NC9na3GFT2_hhZmH6jkAy_aWn0HuEdHf_DVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAHJNYUGw6JA-QyrUBiO2sLUE5gqmTmSbPqhwv9ToPQdvu0DwOUnnbpXDg8Hl9op8LtrzawL-mqBwFMEtMbp4fiyK7nXi2XV71cbPocTI2rVvvhk10jOAnxu96VVimE4Pi0jG5xc6-A5_exPj4mQebPey5BXQKN-G5F-eRLRfYNI1X8qdN6AhCfDqmHDKZQ45fH9syTbf34peEHCmeeMZ7N-qA45GBSS1Sfb5qt94z4sYl5GkTOkpnkIvpLk2RFk1IEwKAZR-keTiBASc83Dcde-MagfyoN6A3-RiPB3EJxr0U8VeLYIUI7netTfh1va38BWbP7YH6QtLG2mfW-vvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خشم کاربران از رویکرد تحریمی آمریکا؛ جهان از دلار عبور می‌کند
🔹
وزیر خزانه‌داری آمریکا با تکرار سیاست تهدید و تحریم علیه ایران، از اعمال تحریم‌های جدید علیه بانک‌های مرتبط با تهران خبر داد؛ اظهاراتی که با واکنش گسترده کاربران خارجی مواجه شد.
🔹
بسیاری از کاربران با انتقاد از رویکرد تحریمی آمریکا، استفاده گسترده واشنگتن از تحریم‌های اقتصادی علیه ایران و دیگر کشورها را نشانه‌ای از سوءاستفاده آمریکا از جایگاه خود در نظام مالی بین‌المللی دانستند.
🔹
بخشی از این واکنش‌ها بر این نکته متمرکز بود که تحریم‌ها زمانی مؤثر هستند که کشورهای هدف و شرکای تجاری آنها همچنان به نظام مالی و دلار آمریکا وابسته باشند؛ اما با گسترش سازوکارهای مالی خارج از کنترل واشنگتن، قدرت تحریم‌های یک‌جانبه آمریکا نیز می‌تواند کاهش یابد.
🔹
کاربران همچنین به نقش بریکس و تلاش کشورهای عضو و شرکای آن برای افزایش تجارت با ارزهای ملی، ایجاد سازوکارهای پرداخت مستقل و کاهش وابستگی به دلار اشاره کردند.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/farsna/460663" target="_blank">📅 13:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460662">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHdQrmZoSTclg9T8txl5tumOpJIiDk0hrjREmwpB9xxBRuSc4sMovbh3cdCbZfW38AbH5DPOPltQ-AxLA8XbKzsb4bvVyot1EY4L2TT4BXatDIZB1_yorULmtogpK0Htt2a8M-BVa3NUkswBMERYJorybxYZVc3Zhv8dKUHqrFDgudnDdSJLZI3SUyRYJ7MWDKi71cMazEFRhQ-hlwRWMhbCMI2e34GdARtYfg1cVSgKKHCGaVnz5XpLb8ayv4tEhnrR8LnDE4ojxPSy2_Dz0YuidlRfjFA-nRa7tU8TSuSoa-Pso5x9r20DppLukUYAWg5CCA6ChhGmhS1mWmLmFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۴.۴ ریشتر در عمق ۸ کیلومتری، بوئین‌سفلی کردستان را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/460662" target="_blank">📅 13:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460661">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌‌‌‌‌‌‌‌‌‌‌ دفتر نمایندگی وزارت خارجه در هرمزگان: ۱۰ صیاد مفقودشدهٔ بندرلنگه‌ای امروز به میهن بازمی‌گردند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/460661" target="_blank">📅 13:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460660">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF2oTCJEtPXEkmg4cc08UjPwMUnIX9QavANNL7GZM74i-aAwXNgjXO5P7Eiv_wS40sNe0s86FBpB6N0v_w1A2stKFsIYVKPiEO_9rRcIFte5AgecBQ7J_aC-wC4Kh9M8Ke3hF2PPRdr4EDRTaGlJds88VM-6C_DvrNRpi8sJF2UQ5UsqiUgiqfF1AyW14im0tEkFPvqTK4sVXOHYS_PN9a7RcgTuk1wi0-jYp3lu3wUswuL6KJ4ZrWU4qZlPF9bHhE5cxcJxUgTyp84VWgyd8sk2TsXqugz9zZl3b4koV3gUssMhHjv74eWHyfX7I0-XIMsWKuwv-fPuI_chjvPD7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تجمع دانشجویان شهید بهشتی در محکومیتِ پرچم‌سوزان
🔹
دانشجویان دانشگاه شهید بهشتی امروز در تجمعی در صحن دانشگاه، با محکوم‌کردن هتک حرمت پرچم ایران، حمایت خود را از آرمان‌های انقلاب اعلام کردند.
🔹
اما در آن سوی این تجمع، برخی دانشجونمایان با حضور در بلندی‌های…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/460660" target="_blank">📅 13:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460659">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-URwlJsPoQiWWimaZY4s3M4K19LiJvDqEJVliPQyWT1Zu6eILq2SjRNO0MASRYMKADHxYcrtKQB6mLe0XkszK_pe9sBPhqn0m2uPdxI5GldYrUDFtQNd_CW5OPZV4ABGPvjiGp2VSq1hqwH01iFDkY7hjx4_5oprhBHjpfb0B3EdpQBgbHTFtClRZ8aT8lOoTxVyxl9KiHYacCro8X-rxDV3qBRRy5mO7Hqa9MzDrHV5qsQMiy4z9ahPxanNpmKmffFhVglMdAQZQZEqcylipg8r81jTBE9RwN3zHQ11EXBz4ExJZdxo7uW0tLwzqaM1Bwi0HoLdXoAUDjC_7DDsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنگونی پهپاد ارتش عربستان در آسمان یمن
🔹
نیروهای مسلح یمن از رهگیری و سرنگونی یک پهپاد شناسایی-تهاجمی مدل «CH-4» ارتش عربستان بر فراز استان الجوف خبر دادند. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/460659" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460658">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kc_Tbmi9We8H5IfkcUQ4YXMzZ0eOAVzu10YIWhVULSqA-oniuNT6GMg045Rb_Bp4buBPRHl_JemeEenFheRxekx7DzuyYH1bX_PNMX5lDnyEcqWsakyjs4RQ6ouBo3RPKsHA8-OqAL31rm3LYDI15heYwnSj2NV8HTnE04x-P6-D2zaZR8HITLLGbXDf8daa3A2A-5fGxh6_Cr1WpnknzMisuC3T0DVqmgPZiy2lCjgNYYdrnApnpzabMKfpDO1KtlhfaNsvjCXQC8fU0DXzZu3LAz9aaCJ2XSa0sXUKchIJumHeX9dkmCLl2Y54cgBcHWL1zExmHIBFNZdGV22ouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عروس رفته گل بچینه...
🔸
کمپین خیابانی غم‌انگیز، به‌یاد شهدای عروسی سیریک
@Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/460658" target="_blank">📅 12:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460657">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OktBpXzTaBo6sIBAAAgsaDkbm-yOczFy6vUjIkfB1yYJm8Hoy1VUy_afYH38HPLKQ6QOcOucLqqDmG8wZye3Ve9vMY7gEd5Lhn0fxOyRzvSdmh6c8kZpXQ8VNtjfN7U1qvpYnq-5t_eqAw1pWjdU1Th2ORHvKxrGEEzBlO-scifaCBalhy9GQv0NOs_aDd8_G68jmTsda5P2OL1_egpnLoMLpEbVh2oUCdvnQMf-DSxBk2k0SHUD0NYHSe84OeuUsF4_1t7Vt2DQx71pnGgoo_ECHvTlNjqCTeWGDbazG6cNegVHSX6WIsPRnWbwFvr4cSNKmJnK7C3KeVfNEJtJMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس امروز فقط ۲ نماد منفی داشت!
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۸۴ هزار واحدی به ۶ میلیون و ۹۰۸ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/460657" target="_blank">📅 12:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460656">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbEadwQEoJ9WHm2D80M6ZqXig2UcbQBVxmyqMHbwqwpNKmwgKSfl_PNUjSFageVoD-U6ztTUQF-YmF8xi8AyEgF13ye7hv0f9PVWex3QSAxSEiKsF3I4wsruXcdV_Afbm5YrO-rOeHB1YhXmonXgK4BZETY1bLgxk126cqJZAjf-PLt2NgIf9sQBhfdOkoQRprlgFHISBl5s4b4rcIGaiXE3NACR3WH4rtUuq_bu1c2xyrZKDKQBJ5id4S4deLcdUizLU0p3rXeu1fzlNSYVgXUYPhJsyE4Bgjj-NH1ehKiUJughyqECX-n17fv8TZhQQEnG725uE2zi9irAo7HXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: ایران براساس اقدام واقعی طرف مقابل تصمیم خواهد گرفت
🔹
رئیس سازمان بسیج: بدعهدی‌های دشمن برای ملت ایران ناشناخته نیست؛ مردم ایران بارها وعده‌های دشمن را شنیده و نتیجهٔ آن را دیده‌اند.
🔹
از همین رو، جمهوری اسلامی ایران نه براساس وعده، بلکه براساس اقدام واقعی طرف مقابل تصمیم خواهد گرفت.
🔹
پیام ایران روشن است؛ هر تعهدی باید اجرا شود و هر توافقی باید در عمل به تأمین حقوق ملت منجر شود.
🔹
دشمن نمی‌تواند هم‌زمان تعهدات خود را نادیده بگیرد، تهدید کند و انتظار داشته باشد ایران از حقوق خود دست بکشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/460656" target="_blank">📅 12:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460655">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0RCvaLUYazhxqO1vXhecKOag8c5Qh9GEo6EAofHZAxKRJT2v_gNFo0J8fM60qcdFxOhmL9RH29qTrDfe5pe971HJMjzyhrtvee_YXNv6i-DzQBbfoOZy0WxdH8wJDUKGauallAUSaaz1Fyo4dPIcCJoIZI-QTdnJm3cb08wkdlSYTlIejLas6wGrfpt8wCTvp4uWnJx4qnl9ch-xKLi9McVOCqwBc0a5Vw9BxDLAg2bq75ytinYIMMT31Dve_x3Yp1xFgABsrOgoibF84AStaVAC-GuCWZD04j1KjVFYVMUxhg0Wcgv6wH_hHDb8qVleXDdGC6vLMIEsHgpW57BRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
از داده خام تا فرصت کسب‌وکار با «قالی»
«قالی» همراه اول، یکی از محصولات معرفی‌شده در نمایشگاه اینوتکس، با هدف ساده‌تر کردن تحلیل داده و استخراج فرصت‌های پنهان از میان حجم گسترده اطلاعات طراحی شده است.
این سامانه می‌تواند جریان‌های مختلف داده؛ از اخبار و قیمت‌ها تا داده‌های مکانی و زمانی را دریافت کند و به کاربران کمک کند با ساخت فرضیه و مقایسه الگوها، ارتباط‌های پنهان میان رویدادها را کشف کنند.
محمدعلی تولایی، مدیرعامل هوش مصنوعی قالی، می‌گوید این سامانه می‌تواند شباهت‌های زمانی میان اتفاقات را شناسایی کند؛ برای مثال مشخص کند افزایش قیمت یک کالا، با چه فاصله‌ای می‌تواند با تغییر قیمت کالای دیگری ارتباط داشته باشد.
نام «قالی» نیز از همین ساختار گرفته شده است؛ داده‌ها مانند تار و پود کنار هم قرار می‌گیرند تا در نهایت یک «نقشه» از بینش‌های قابل استفاده برای کسب‌وکارها شکل بگیرد.
هدف این محصول، توانمندسازی کسب‌وکارها و متخصصان داده برای تبدیل اطلاعات خام به تحلیل و فرصت اقتصادی است.</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/460655" target="_blank">📅 12:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460654">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb7ae037ce.mp4?token=YZmn32LIFd11zouGvwtxvO6pCVXHB1E9LEK5Wu_jY8OH_HyQZMshGgPAloE8fcPHF2cIrSvBgP35V2wyUThSHrQtU2ejCoJ7tR8kOdel91oi7qgmpkNC7xdzLqBYk8Bzp4-veFZTRlRk1aWdWApdu5-Q2YfQU4kp1Q6gcGrFrCUfpmjxAlzrL0iTqyyOLhWBzShqfulwWGpFRsEIlcFdPMLNVHSfixPnWv2lTQ9J2bcd1lpQBE7QMXHOCGzMALwzKuyqEZg3rZaE-FzgBu492FBdpnusJR3ydSgdkCKpTjxkJRdrIfOPLGFId7E9RrYNNCptnKFDU5iKUG4iSdVH5LzJMQOW2pn7mvaD6ggfxE-VE9crH_KUVmfOvkaHWePXUijwBQ7R6oOTVOo-1lF4RYkdLq9qK_60F3-InoudPplNw1gRlOaNPZ_niYJQg4kDswJ3IthjJF74UAovNfiLLu4WfZl1sxKN0RfeD_YlXTWiBfRiySqNRUYceyRUEVQli1N9iGuxxtgXJrtwsm2zjD9fjN7Po1JBfZUCnVd-8vsVo1p2HrzeGAT5VXGqnZrzfxeKcRz6niWW4_ZH7sGRvYAbbcard8-gm9gTy1nf7VHR7yLERN9J6V1X59X32mlaairzSV2d3s0kfud1nnAx9gY1PLIUgDiI8XzEJyycaLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb7ae037ce.mp4?token=YZmn32LIFd11zouGvwtxvO6pCVXHB1E9LEK5Wu_jY8OH_HyQZMshGgPAloE8fcPHF2cIrSvBgP35V2wyUThSHrQtU2ejCoJ7tR8kOdel91oi7qgmpkNC7xdzLqBYk8Bzp4-veFZTRlRk1aWdWApdu5-Q2YfQU4kp1Q6gcGrFrCUfpmjxAlzrL0iTqyyOLhWBzShqfulwWGpFRsEIlcFdPMLNVHSfixPnWv2lTQ9J2bcd1lpQBE7QMXHOCGzMALwzKuyqEZg3rZaE-FzgBu492FBdpnusJR3ydSgdkCKpTjxkJRdrIfOPLGFId7E9RrYNNCptnKFDU5iKUG4iSdVH5LzJMQOW2pn7mvaD6ggfxE-VE9crH_KUVmfOvkaHWePXUijwBQ7R6oOTVOo-1lF4RYkdLq9qK_60F3-InoudPplNw1gRlOaNPZ_niYJQg4kDswJ3IthjJF74UAovNfiLLu4WfZl1sxKN0RfeD_YlXTWiBfRiySqNRUYceyRUEVQli1N9iGuxxtgXJrtwsm2zjD9fjN7Po1JBfZUCnVd-8vsVo1p2HrzeGAT5VXGqnZrzfxeKcRz6niWW4_ZH7sGRvYAbbcard8-gm9gTy1nf7VHR7yLERN9J6V1X59X32mlaairzSV2d3s0kfud1nnAx9gY1PLIUgDiI8XzEJyycaLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔖
روش‌های متنوع انتقال وجه
✔️
پُـل
✔️
پـایـا
✔️
ساتنا
✔️
کارت‌به‌کارت
🔝
برای اطلاع از روش‌های انتقال وجه، این ویدیو را ببینید.
👍
#اعتماد_می‌ماند
#باجه
#خدمات_غیرحضوری
📥
دانلود
#بام
،
سامانه بانکداری دیجیتال بانک ملی:
📲
https://baambank.ir
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/460654" target="_blank">📅 12:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460653">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/460653" target="_blank">📅 12:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460652">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8943cc4e99.mp4?token=R8bj6ZX4WdqZC6RFSpWS53_f49uS5J626brhwJGQ2Apys_jwierixFEyDi7BPUnw3eK9F4Q9Y9bF-3BKOXzwNFCaK5ov0Z9adPWztEkCdBIgxFoF70wgmfMurRwgH-cabOhb8Ms266CdVSLYWdZ0fpAxBOVcM6Vk2wcJmZQLaAZLQP44pDo1dRx3w_0tY6QPjV1kD3SIr9sQ06T6vHhk-iSsIxeVnaGTbbz05UgwdkyPO3fZJk43ySkQZwTSAPcyeQ6yi7El_Xqw5ePXL0Sah8hsrhs3bXE2t78oZLUsz8CxTuSAHXL5ySh0KcITysuTV-wdcH8bf8Ft9FGLu2VpZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8943cc4e99.mp4?token=R8bj6ZX4WdqZC6RFSpWS53_f49uS5J626brhwJGQ2Apys_jwierixFEyDi7BPUnw3eK9F4Q9Y9bF-3BKOXzwNFCaK5ov0Z9adPWztEkCdBIgxFoF70wgmfMurRwgH-cabOhb8Ms266CdVSLYWdZ0fpAxBOVcM6Vk2wcJmZQLaAZLQP44pDo1dRx3w_0tY6QPjV1kD3SIr9sQ06T6vHhk-iSsIxeVnaGTbbz05UgwdkyPO3fZJk43ySkQZwTSAPcyeQ6yi7El_Xqw5ePXL0Sah8hsrhs3bXE2t78oZLUsz8CxTuSAHXL5ySh0KcITysuTV-wdcH8bf8Ft9FGLu2VpZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: هنر مقامات آمریکایی این است که صادقانه دروغ می‌گویند!
🔹
سابقهٔ حملات آمریکا به غیرنظامیان را مرور کنید تا متوجه بشوید آمریکا از الگوی اسرائیلی پیروی می‌کند.
🔹
الگوی مقامات آمریکایی این است که ابتدا حاشا می‌کنند، بعد برخی می‌گویند «توسط…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/460652" target="_blank">📅 12:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460651">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8326718891.mp4?token=hDOwtV0lFAeCd0_iq2z25r9zEBU34VdcQr_AYvYjRg2Z4C2GAfvXOogejA81f0-hdw-sWegKl-N5bLJ-ryQKR3IHMrQ0sJBGu9ONGx8ZczgPEtXo0FNuzaWOVrmdvSic-T45s3ekzTQrwGXawbTMNOXWAfCxfqfNNYTZG4_W1FRr1ppskjvcwRsRb7gDueCG77A5Lz7jkpFgICASFQCrZ1Se6BVjQwGXNUmQ6aW12JSDGyvzWtlwiDUtvkTGlxF2nO6Wa9aI3jb0WBHLcXRTV4OSjfz6SJbgDbXlIIC9JimJTsS8fZdmx38nT1y21jm3wJVh9f3zLoEjPktTFjlQBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8326718891.mp4?token=hDOwtV0lFAeCd0_iq2z25r9zEBU34VdcQr_AYvYjRg2Z4C2GAfvXOogejA81f0-hdw-sWegKl-N5bLJ-ryQKR3IHMrQ0sJBGu9ONGx8ZczgPEtXo0FNuzaWOVrmdvSic-T45s3ekzTQrwGXawbTMNOXWAfCxfqfNNYTZG4_W1FRr1ppskjvcwRsRb7gDueCG77A5Lz7jkpFgICASFQCrZ1Se6BVjQwGXNUmQ6aW12JSDGyvzWtlwiDUtvkTGlxF2nO6Wa9aI3jb0WBHLcXRTV4OSjfz6SJbgDbXlIIC9JimJTsS8fZdmx38nT1y21jm3wJVh9f3zLoEjPktTFjlQBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: هیئت فنی ستادکل نیروهای مسلح در روزهای گذشته به قطر رفتند تا وضعیت خلبان‌های شجاع ایرانی را پیگیری کنند
🔹
قطعاً ما از پیگیری این موضوع صرف‌نظر نخواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/460651" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460650">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bceae9093c.mp4?token=WIhTk8EzxiGdH55q1pV2kSlbqJl7Kw0yIzTYOBsUQhFQMTpMfbtgJVA16e4XWiXTa_Hk9UM_xzVsOHm6tr8DjGErXo7nG3rG-VIywbDiwd_JgXdC5ubKkWlAE1owvI4Jw0I6Z5eOt0vXoIRHdso-J1Jub7IY8yYQtOlunYVC9K2rev9cyd35Pujt06VteKx00JRJqC_s3W1TPnpxfvVBHG12Y7WXIBhz5rvPaVcCOFc4fATaSkDQhKmBH19KSNTIE228s8gOonkQ7gFUiFORV6KLetdBRsnXXWZwKuPBPy-_GizlPVocMZ1OMUu5b27SmF1ao0k1amTg95uvKghRag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bceae9093c.mp4?token=WIhTk8EzxiGdH55q1pV2kSlbqJl7Kw0yIzTYOBsUQhFQMTpMfbtgJVA16e4XWiXTa_Hk9UM_xzVsOHm6tr8DjGErXo7nG3rG-VIywbDiwd_JgXdC5ubKkWlAE1owvI4Jw0I6Z5eOt0vXoIRHdso-J1Jub7IY8yYQtOlunYVC9K2rev9cyd35Pujt06VteKx00JRJqC_s3W1TPnpxfvVBHG12Y7WXIBhz5rvPaVcCOFc4fATaSkDQhKmBH19KSNTIE228s8gOonkQ7gFUiFORV6KLetdBRsnXXWZwKuPBPy-_GizlPVocMZ1OMUu5b27SmF1ao0k1amTg95uvKghRag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: به‌شرط اینکه آمریکا به تعهداتش در صدور روادید عمل کند، قرار است در نشست سالانهٔ سازمان ملل در نیویورک شرکت کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/460650" target="_blank">📅 11:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460649">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6bb9013c.mp4?token=KujqIQ_uHBAzEf4cpUfqRLpQzfStle8Qd4tEuxg6yfz2F0CCv8KHvpJ6Ymfs4ft-SB6IYSc__l1yEW0-fTRunQDx-jiMVnc1gtLHu568sEStpuYavv69WioqXO-mLe82jBGBFMRNNBtkaKPqS3kcrbdimNz0MYnWX8g6egESagbgUicMNCN0B-68nhu8UeiaajZWIa_1RjSbwiwU5YALMkwl5WiN58G0_Aq0YjYplv_XxH4AVGH-dnMzByG_pxSu1REsRKU3yXtLuhhw8bv2o_Achm2fUoG04MVKoWctBUSXqaFaEIKmPTVUPZr03fxlQq2mEbioeIYazVhqPHKA6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6bb9013c.mp4?token=KujqIQ_uHBAzEf4cpUfqRLpQzfStle8Qd4tEuxg6yfz2F0CCv8KHvpJ6Ymfs4ft-SB6IYSc__l1yEW0-fTRunQDx-jiMVnc1gtLHu568sEStpuYavv69WioqXO-mLe82jBGBFMRNNBtkaKPqS3kcrbdimNz0MYnWX8g6egESagbgUicMNCN0B-68nhu8UeiaajZWIa_1RjSbwiwU5YALMkwl5WiN58G0_Aq0YjYplv_XxH4AVGH-dnMzByG_pxSu1REsRKU3yXtLuhhw8bv2o_Achm2fUoG04MVKoWctBUSXqaFaEIKmPTVUPZr03fxlQq2mEbioeIYazVhqPHKA6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: هیئت قطری دیروز در تهران حضور داشت و برای کمک به کاهش تنش‌ها دیدارهای خوبی با آقای عراقچی داشتند.  @Farsna</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/460649" target="_blank">📅 11:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460648">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvUu5f7BMpZu_5qi3vy8ctV0wJwTnIhyQpzotJcEPo2LLfLcE8JgPrniHhAPg4YZjrOuPLL7DwV_W2uz7l8LjNkKHGylbMH3Vcm7MBXoTqZkddVZyeqinmKmwVO3N2gGdyMBOgpxg0rOYYxy8jAeq0dcm7u7ES_dMJdc3_rPVP6e3VXGGBkhxxLIdMAOoWwzPCrDpMDFOKlle0BNP286R93r0esfOMfF-m2yeLlQ-5DfcrAPHzqxd4zfz-LFhKgLezibe5QNmAl3EUf4fpq5hCeSX-Jb_fD5cZNwcskcSB42jt7nepooqcJgWDU2jK4AhFL-us9exoCYeAMZU-oBnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: اگر به دارایی‌های ما حمله کنید، مورد حمله قرار خواهید گرفت
🔹
رئیس مجلس در پاسخ به تهدیدات اخیر وزیر جنگ آمریکا: ساده و قابل‌ فهم است: زنجیرهٔ تولید نفت و گاز در این منطقه گسترده و پراکنده، در دسترس و آسیب‌پذیر است.
🔹
شرکت‌های نفتی و گازی آمریکایی که در این آب‌ها و تأسیسات فعالیت می‌کنند نیز همینقدر آسیب‌پذیر هستند.
🔹
اگر به دارایی‌های ما حمله کنید، مورد حمله قرار خواهید گرفت. ما این توانایی را قبلاً ثابت کرده‌ایم. از پایگاه‌های نظامی‌تان که غیرعملیاتی شده‌اند، بپرسید.
🔸
وزیر جنگ آمریکا در لفاظی‌های اخیر خود گفته بود که «اگر ایران به کشتی‌های آمریکایی حمله کند، نفتکش‌های آن‌ها را غرق می‌کنیم.»
@Farsna</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/460648" target="_blank">📅 11:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460647">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5bb5afd21.mp4?token=haMZA9_xNDViMhcP6piDrPq6JW41JhbmOjyakA9pA2vZ_F0UFHZK8MdC-mbAC5CNvgpIf-oSfVqsPKfH8ZGRxYZEr3-daN11Y2SkYZOeSRKDkgIhmz6qTviN0LyRWGkIu5YI5PxKu2vetDsouWWhBWK28Ri4z6PpcoTpNnl6LaskBBEuGWS5hdHBR8duTWYxPoRaALhKI-6lIEYuS-DaSiwuqn3BpYQ9yJp3JF-H-PUrowYdDrd0D2d-4pMAkhIgzaHPQlDI_9svALiQsxSxuBu29GDsVMLfqITuIRN6bG9zLkSZsIGkGrduFX-JoOZTryd0VVy2_LumZ61VlDj_cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5bb5afd21.mp4?token=haMZA9_xNDViMhcP6piDrPq6JW41JhbmOjyakA9pA2vZ_F0UFHZK8MdC-mbAC5CNvgpIf-oSfVqsPKfH8ZGRxYZEr3-daN11Y2SkYZOeSRKDkgIhmz6qTviN0LyRWGkIu5YI5PxKu2vetDsouWWhBWK28Ri4z6PpcoTpNnl6LaskBBEuGWS5hdHBR8duTWYxPoRaALhKI-6lIEYuS-DaSiwuqn3BpYQ9yJp3JF-H-PUrowYdDrd0D2d-4pMAkhIgzaHPQlDI_9svALiQsxSxuBu29GDsVMLfqITuIRN6bG9zLkSZsIGkGrduFX-JoOZTryd0VVy2_LumZ61VlDj_cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: تفاهم ایران و عمان برای تعیین مسیر موقت تنگهٔ هرمز در روزهای آینده نهایی خواهد شد؛ امیدوارم طرف‌های بدسگال در این روند مداخله نکنند.  @Farsna</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/460647" target="_blank">📅 11:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460646">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57d27e7d9.mp4?token=YhfdU36nzeC0G2E_IUILGmNkhSfE6PPb3pii5kzmgo_gBfuSZClgqunMXt4y2VVkM_80CY1zsu3XJrlZc7c6cDuwKhDPShTsRoYHnkJ0PlZWYivGkNZ5EZ2SG6Gsa-TRkfCCpXqWXJJyTH-_hpIsVxkEhEjM8tCexirOiOecmTKnYi7VGHOdfDtUrbBNdZ0s_qtgjVXQ41YXye1OOO64kNxXScmZaBYSbMQKDNPU5kjTvHD3AP_TiJtQ4mYMP8x-GxDH2e6lLOsUbUwj3Rszr0npejQADZhlk2d8I3guOEBJahyWXWX_pY1IEYbMyfLoqIuh3CRq4wEXa3kXckx67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57d27e7d9.mp4?token=YhfdU36nzeC0G2E_IUILGmNkhSfE6PPb3pii5kzmgo_gBfuSZClgqunMXt4y2VVkM_80CY1zsu3XJrlZc7c6cDuwKhDPShTsRoYHnkJ0PlZWYivGkNZ5EZ2SG6Gsa-TRkfCCpXqWXJJyTH-_hpIsVxkEhEjM8tCexirOiOecmTKnYi7VGHOdfDtUrbBNdZ0s_qtgjVXQ41YXye1OOO64kNxXScmZaBYSbMQKDNPU5kjTvHD3AP_TiJtQ4mYMP8x-GxDH2e6lLOsUbUwj3Rszr0npejQADZhlk2d8I3guOEBJahyWXWX_pY1IEYbMyfLoqIuh3CRq4wEXa3kXckx67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ناامن‌شدن تنگهٔ هرمز نتیجهٔ اقدامات آمریکاست
🔹
این که دشمن، ایران را «مشکل امنیت» در تنگهٔ هرمز معرفی می‌کنند، یک دروغ آشکار است. @Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/460646" target="_blank">📅 11:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460645">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/065364d19b.mp4?token=UOJZsMOj3SX0SIg5xX9fCuQzD0nXwn0-c0_OoO0zFP7zP54YqOh5_hW1Mzo7EHvo7AEbdDNO1Dl8pQAanhNRvvEV197iJWtf1wM3xDNYR-YEcaWgzTFVYRd2OMHlIVTeDKm6-UPV47QaWSmNla6Sh9MzbToWIKaHm7_LWVFOOv_LV0d3pQEOOtzCzlg6pcVhxW1fxERt9tUp6si5DbXSBWJOwtqwqW3S76-J3oNZG3O-OlRHLITJ3bNlYkWnqHum85KietJpiNMK_-UfE8h9JlEJyv1OGUqigUcJv3wwu2CwyLIii46DactazrdISNcByNNdnWWC4hn-ZDETx_DCdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/065364d19b.mp4?token=UOJZsMOj3SX0SIg5xX9fCuQzD0nXwn0-c0_OoO0zFP7zP54YqOh5_hW1Mzo7EHvo7AEbdDNO1Dl8pQAanhNRvvEV197iJWtf1wM3xDNYR-YEcaWgzTFVYRd2OMHlIVTeDKm6-UPV47QaWSmNla6Sh9MzbToWIKaHm7_LWVFOOv_LV0d3pQEOOtzCzlg6pcVhxW1fxERt9tUp6si5DbXSBWJOwtqwqW3S76-J3oNZG3O-OlRHLITJ3bNlYkWnqHum85KietJpiNMK_-UfE8h9JlEJyv1OGUqigUcJv3wwu2CwyLIii46DactazrdISNcByNNdnWWC4hn-ZDETx_DCdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: اینکه آمریکا برای فشارآوردن به ایران متوسل به کشتار کودکان در جشن عروسی بشود، هیچ ارزشی ندارد
🔹
ایران در موضع دفاع قرار دارد و ضربات دفاعی ایران به پایگاه‌ها و ناو آمریکا در چهارچوب دفاع مشروع است. @Farsna</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/460645" target="_blank">📅 11:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460644">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd3ae401b.mp4?token=nled_i7AlZ7NEbndVTxTXFYcgRmSPdQF2yP6ZwkPzYXvQoYbR1bK6mX5nDW-3LTaNIXLFOQOFgO679_P_Pm29w1WnIwpXJIJ0x4jgV3Ds6K3RwRES4L9vhVFHC9vl4RPUR01G13h8CTQK-1Bd9tcG6_nSyf4Fbvb4hCFXIHD7Xe7J8fjSChM_W_8ppty3UociPA5fEPcHL1Lb9e59xF7qxxCk3FWtiUXlYTdchGVt55kBZnDKOHhTNF0NWU5__m6Z71Yx2S04PKiJoYP5ePNi3ox9KQ-3B99Y74f1ja_BHJWk9LTBsFhUiS6M6jTspSOtUcVV2wQaVksXfjgFPICZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd3ae401b.mp4?token=nled_i7AlZ7NEbndVTxTXFYcgRmSPdQF2yP6ZwkPzYXvQoYbR1bK6mX5nDW-3LTaNIXLFOQOFgO679_P_Pm29w1WnIwpXJIJ0x4jgV3Ds6K3RwRES4L9vhVFHC9vl4RPUR01G13h8CTQK-1Bd9tcG6_nSyf4Fbvb4hCFXIHD7Xe7J8fjSChM_W_8ppty3UociPA5fEPcHL1Lb9e59xF7qxxCk3FWtiUXlYTdchGVt55kBZnDKOHhTNF0NWU5__m6Z71Yx2S04PKiJoYP5ePNi3ox9KQ-3B99Y74f1ja_BHJWk9LTBsFhUiS6M6jTspSOtUcVV2wQaVksXfjgFPICZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: حملهٔ آمریکا به کشتی‌های تجاری، ایران را مجاز می‌کند تا اقدامات دفاعی انجام بدهد.  @Farsna</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/460644" target="_blank">📅 11:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460643">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1799a27c3d.mp4?token=qNzT0nzC5hubiDvNC-8dVwHeYizXHEOgJv4S4lqBeErdl08mRhQC-zVHrrX-stTW6sneLYHsMvILQ5Tvfk5BVqyuM5OnBUn7KXGH2ThY-8LOARB_xcSj-1_vpsHGTK5W7aKlkjusdXxb3sWeF3DeRJWfUkkNkSbbHsV0_D0OEUVtwDs3jDvd5BEUQMxdlV1FyaE0nt1A1Se-6tcvUDdEZ5piIKYNG_Nkfmxmaq597NpHjzbAc1gCG7O81CeKWT4w1HZX3Rnn2lLCSx2yNrop244GccqsrgJotqeXk4sJ14oJhfd8yJexxoD-RSjWtoRHBNI2gQixWN9M-dpp6TVJdqgFyeA87Gtjj_FGjGUc9C_KDdsSWPjlMLR3MWg_fqcLd8hQlm7Qq4It0CJBrtqW5q18Qsw8K7_U3gB47zwSPVeuwt8RgdY00dybN0i91pVVDR5QAaWUTVZ5dk5OtIZmczN33VPl4QbFx0JHn3CFHzFHcevJn3fZwOfZDDFbtyc7M71cjZ8FiV2A1OiMSe_TgGp7LqyJFFnVtbYHDdFsu6itiSmO78HMHouw57ymgdCdmubNiviftiJ5XN91gWTTWV8wyf7TbyixEf-8kxHCaEarldjj84iMt6Jw22OZfeFXha1rVWYoDBzaW4D9JecY4SjkwimlhGvtZdNlp5zjX10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1799a27c3d.mp4?token=qNzT0nzC5hubiDvNC-8dVwHeYizXHEOgJv4S4lqBeErdl08mRhQC-zVHrrX-stTW6sneLYHsMvILQ5Tvfk5BVqyuM5OnBUn7KXGH2ThY-8LOARB_xcSj-1_vpsHGTK5W7aKlkjusdXxb3sWeF3DeRJWfUkkNkSbbHsV0_D0OEUVtwDs3jDvd5BEUQMxdlV1FyaE0nt1A1Se-6tcvUDdEZ5piIKYNG_Nkfmxmaq597NpHjzbAc1gCG7O81CeKWT4w1HZX3Rnn2lLCSx2yNrop244GccqsrgJotqeXk4sJ14oJhfd8yJexxoD-RSjWtoRHBNI2gQixWN9M-dpp6TVJdqgFyeA87Gtjj_FGjGUc9C_KDdsSWPjlMLR3MWg_fqcLd8hQlm7Qq4It0CJBrtqW5q18Qsw8K7_U3gB47zwSPVeuwt8RgdY00dybN0i91pVVDR5QAaWUTVZ5dk5OtIZmczN33VPl4QbFx0JHn3CFHzFHcevJn3fZwOfZDDFbtyc7M71cjZ8FiV2A1OiMSe_TgGp7LqyJFFnVtbYHDdFsu6itiSmO78HMHouw57ymgdCdmubNiviftiJ5XN91gWTTWV8wyf7TbyixEf-8kxHCaEarldjj84iMt6Jw22OZfeFXha1rVWYoDBzaW4D9JecY4SjkwimlhGvtZdNlp5zjX10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام ۳ هستهٔ عملیاتی گروهک تروریستی در جنوب شرق
🔹
وزارت اطلاعات: ۳ هستهٔ عملیاتی گروهک تروریستی-تکفیری هنگام ورود به کشور در سیستان‌وبلوچستان با دستگیری ۹ تروریست و به هلاکت رسیدن ۳ تن از آنان منهدم شدند.
🔹
از تروریست‌های دستگیرشده مقادیر قابل‌توجهی سلاح و مهمات جنگی کشف شد. ‌
🔹
همچنین یک انبار از سلاح‌های جنگی سبک و نیمه‌سنگین که به‌صورت مخفیانه و غیرمجاز وارد کشور شده بود، کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/460643" target="_blank">📅 11:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460642">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/659545a10e.mp4?token=ABXw7HQgShaLTVZilA6qzosxXxtHp_XhEoD4zBuCAQHQpa2S3wdbP4DyHtbI5pCtqTsRNq31cx0_A3nswDKRtoamGQ9Wjn_ZAJP7R8YofPl7FYm-W8w6xLb-JGJnbWRfIuV8pu52qKgt2CLompWPQONMVfk9B_cymOzrMh0vOu8CMRnHNZInAuKVhcYuOhONOKfF7_Pt2DHAlSr0qE0fVCCNkeIzr6kg9abi4Lqq03y15Un0MbLBWBI24zb0rWz1lGCKHk2ZzEVcaSMWakeecLqpXO8zvyOggbHCMwb122zgKV1AK-965QogARzQp-tOOlnLydBmS72jw-FVdoT0eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/659545a10e.mp4?token=ABXw7HQgShaLTVZilA6qzosxXxtHp_XhEoD4zBuCAQHQpa2S3wdbP4DyHtbI5pCtqTsRNq31cx0_A3nswDKRtoamGQ9Wjn_ZAJP7R8YofPl7FYm-W8w6xLb-JGJnbWRfIuV8pu52qKgt2CLompWPQONMVfk9B_cymOzrMh0vOu8CMRnHNZInAuKVhcYuOhONOKfF7_Pt2DHAlSr0qE0fVCCNkeIzr6kg9abi4Lqq03y15Un0MbLBWBI24zb0rWz1lGCKHk2ZzEVcaSMWakeecLqpXO8zvyOggbHCMwb122zgKV1AK-965QogARzQp-tOOlnLydBmS72jw-FVdoT0eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما با کره‌جنوبی روابط خوبی داشته‌ایم اما هر مشارکتی در اقدامات تجاوزکارانهٔ آمریکا برابر با هم‌دستی در تجاوز خواهد بود.  @Farsna</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/460642" target="_blank">📅 11:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460641">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9483b7adf4.mp4?token=pNnTkkYm7n3vkRU4jzDrI4jMpE0nBvLf7T1ACENxwx1HUhWG35328QhsaQOM8wNfnIazpnWnRF--6rbdJgYI9l1nVUj8Zzfpj8peSuvCfjeN8JAABM7B2TVJbdmPinCdjCUrgTEQrsHD6F4Xc1JqeT18g5Tmak6SkyfdwIkxEzfejCbaeMeDO_n-fYKjOsp7fIX1D9nBVShZwpDCSGSE7g3fncDYc2Abvr8nSJQhJF8HfALeQsAkfN4Yi7Gq1Y6LQBc4tW-opdd7g2ABmfNdF9BZKc5rQ2BzPo3NCDBDzO2RKBgaZwbDu1nI6Z6KiL150xGfztEHtFcftNl60KX2HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9483b7adf4.mp4?token=pNnTkkYm7n3vkRU4jzDrI4jMpE0nBvLf7T1ACENxwx1HUhWG35328QhsaQOM8wNfnIazpnWnRF--6rbdJgYI9l1nVUj8Zzfpj8peSuvCfjeN8JAABM7B2TVJbdmPinCdjCUrgTEQrsHD6F4Xc1JqeT18g5Tmak6SkyfdwIkxEzfejCbaeMeDO_n-fYKjOsp7fIX1D9nBVShZwpDCSGSE7g3fncDYc2Abvr8nSJQhJF8HfALeQsAkfN4Yi7Gq1Y6LQBc4tW-opdd7g2ABmfNdF9BZKc5rQ2BzPo3NCDBDzO2RKBgaZwbDu1nI6Z6KiL150xGfztEHtFcftNl60KX2HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: رفتار آژانس و گروسی یادآور داستان حکیم عضدالدین ایجی و خان مغول است
🔹
هرجا که در حوزه‌های دیگر کم می‌آورند، سراغ آژانس و شخص مدیرکل می‌روند و بالعکس، مدیرکل خودش را عرضه می‌کند برای سوءاستفادهٔ طرف‌های اروپایی و آمریکا علیه ایران برای…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/farsna/460641" target="_blank">📅 11:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460640">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd7da7504.mp4?token=f1mk9u3HBZoupQQXXPEgfkIBtszZNATANYXrPUe3h2XxOBHttOGXs8adPhzJFnMvAtABLCWBdFQ245tiGg5YWQhCS8o26DEOxSFo9F5Yfl_oAgaF4GUtkCD5iVBy10hmxnzL_ODSu2dqliqUIH_BZnMfNuEULuHDfHV9Eh1aWQ9kkkXh_GjFtbtLsTtmETXj1xcTaCIoxP7Q3D6lLnB1LEax1uFevqMSH0w0U7-b70aDJa0ODwQPx0PtD6iwtmQvC6uh_uGTd3pMV-oUNwUq9fnKDnmiJvV5TAH6it4r4tYHRbjX9TxMTJXvNIDvOrShff2zKbOL8MPb7fgSjHMlMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd7da7504.mp4?token=f1mk9u3HBZoupQQXXPEgfkIBtszZNATANYXrPUe3h2XxOBHttOGXs8adPhzJFnMvAtABLCWBdFQ245tiGg5YWQhCS8o26DEOxSFo9F5Yfl_oAgaF4GUtkCD5iVBy10hmxnzL_ODSu2dqliqUIH_BZnMfNuEULuHDfHV9Eh1aWQ9kkkXh_GjFtbtLsTtmETXj1xcTaCIoxP7Q3D6lLnB1LEax1uFevqMSH0w0U7-b70aDJa0ODwQPx0PtD6iwtmQvC6uh_uGTd3pMV-oUNwUq9fnKDnmiJvV5TAH6it4r4tYHRbjX9TxMTJXvNIDvOrShff2zKbOL8MPb7fgSjHMlMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۳۱۳ هزار نفری جان‌فدایان ایران در تهران
🔹
رزمایش بزرگ مردمی «جان‌فدایان ایران» با حضور ۳۱۳ هزار نفر از نیروهای مردمی، بسیج، سپاه و انتظامی ۲۷ شهریور در تهران برگزار خواهد شد.
🔹
علاقه‌مندان برای ثبت‌نام و حضور در این رزمایش می‌توانند به مساجد و پایگاه‌های مقاومت مراجعه کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/460640" target="_blank">📅 11:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460639">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GF7Hi5-d7tgVn0KU_AwTWEB7XfYMo5ZtrJuJZsGmEOy_nQBnC7ovxjPH4QK2-VJgFr6cQWBiq1T37P1rUJIKxUIpahwlskRbJj7zBUKriOhyZsNLkKBInsLgL2qlmPfDvzwYst-M_6VqB9u7K7SV8b6A4qUt5tojyoViESkxT-QQcb8dFXhWKGsXKWJkXWuQBhHVEl1Qco6zKV627OVcZeb5Cgv3V7pIE785e8tbx8xMUOHlr_jsDxfdth97sUHrjrKtOvLoLc5ycQ-r7MC0uQl_IURX1bfhmQrrv4v6mypuAaIC0FfZvaKZKBEKGIrXTnAQtjiK2SoBF8VxBf4Nxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
۳ نفتکش با هشدار سپاه تغییر مسیر دادند
🔹
گزارش‌ها حاکی از آن است که دست‌کم ۳ نفتکش و شناور حامل انرژی ازجمله نفتکش LNG قطری که از مسیر جنوبی تنگهٔ هرمز درحال عبور بودند، پس‌از دریافت هشدار سپاه مسیر خود را تغییر داده و بازگشتند. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/460639" target="_blank">📅 11:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460638">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حملهٔ ضدصهیونیستی با سلاح سرد در کرانهٔ باختری
🔹
کانال ۱۲ رژیم صهیونیستی: یک فرد با چاقو به یک شهرک‌نشین حمله کرد و با خودرو از محل دور شد. شهرک‌نشین مجروح در وضعیت وخیم قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/460638" target="_blank">📅 11:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460637">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd41bb479.mp4?token=C0ZZ4Wa_TisqP3URtXE9RX_KuQ6Qczj4a5C-ehFl8nwdE-AyjUBDWnyg9B4UOEbGOXNAue8hw49tAT_OkFRsgV_vasNIvIldHTHD4-2cY7XErSEupLurvy_Q3X1EgzzxpHf3o6qZJ2OB0BM-yNPR5YVbSyWpsvMlTbw69ngOjOLmAprxt2FWhTUg_2ojs6FUXHkgS7fbaNUSzbIvG5cH8aWKi4t-Al_T1RQAnb7pMyAr05vqZJZ8oErraAkDskKYAN_l1oW3jXUzY5MDJBmLPQENEtumVRPULYd5-0zlfxhiOzDGGYUSHnxnDWz9llE1Xcy_FpGFNtIKZdl8JEW67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd41bb479.mp4?token=C0ZZ4Wa_TisqP3URtXE9RX_KuQ6Qczj4a5C-ehFl8nwdE-AyjUBDWnyg9B4UOEbGOXNAue8hw49tAT_OkFRsgV_vasNIvIldHTHD4-2cY7XErSEupLurvy_Q3X1EgzzxpHf3o6qZJ2OB0BM-yNPR5YVbSyWpsvMlTbw69ngOjOLmAprxt2FWhTUg_2ojs6FUXHkgS7fbaNUSzbIvG5cH8aWKi4t-Al_T1RQAnb7pMyAr05vqZJZ8oErraAkDskKYAN_l1oW3jXUzY5MDJBmLPQENEtumVRPULYd5-0zlfxhiOzDGGYUSHnxnDWz9llE1Xcy_FpGFNtIKZdl8JEW67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: همهٔ دنیا دیدند که آمریکا و رژیم صهیونیستی جنگ را به ایران تحمیل کردند و باید به‌خاطر تک‌تک جنایاتشان پاسخگو باشند.  @Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/460637" target="_blank">📅 11:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460636">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4vs3AgHDXXrjLLmKnOuhiNH0HxaidtlCaIZOLz2jBI6-3O0rcj0zfvdrA1aGeO3v4GFvVTP3yMQK1YzGMLp9JF0TYLOMhNHxgHIwYlaSl-4_mUKKcjcFA0prkv4DPE5uaMwN_vVoAfomZ_ae2glFRNOfLKDg8nGh5gzDuFr-MOOfsCu8rVpKA6OBqiOzp9f8M4N4Y03UkHSesqsUzkOoA_ccSy8Js-JIfl70e46kkRJMjIf6XtwGd9hPeYgMmGCOxOmKZxoPCcecgFsYzZn2fynlQrADv46UK1r67fNlsbvGgt3oce22nxUMy-368p9GyrrqadnDKyIDkzAIvs71Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنزین بحران جدید اسرائیل شد
🔹
قیمت هر لیتر بنزین در سرزمین‌های اشغالی با افزایش ۰.۱۶ شکل به ۸.۲۵ شکل رسید و قیمت هر گالن نیز به ۱۰.۴۱ دلار افزایش یافت.
🔹
درپی این افزایش، دولت اسرائیل برای کنترل قیمت‌ها مالیات سوخت را به‌مدت ۲ ماه، ۰.۵ شکل در هر لیتر کاهش داد تا قیمت بنزین به ۷.۷۵ شکل برسد؛ اقدامی که ماهانه ۱۵۵ میلیون شکل از درآمدهای دولت کم می‌کند.
🔹
این تصمیم درحالی گرفته شده که حدود ۲ میلیون شهرک‌نشین زیر خط فقر و ۸۸۰ هزار کودک با ناامنی غذایی مواجه هستند.
🔹
هم‌زمان بانک مرکزی اسرائیل برای سومین‌بار متوالی نرخ بهره را ۰.۲۵ درصد کاهش داده و وزیر دارایی این رژیم خواستار کاهش بیشتر نرخ بهره شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/460636" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460635">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84f85f87e0.mp4?token=tqfirmLGcd-Idpj-VmhoBTTMHW5EtUKiaHKwoLkAOg6QNR5HoBPVvA-qZlJ8rvyq8i0iCb9zNSlScTb7-vNroGbCuT516hvoIqgYrNsjYW1udNO_fai-dyZyGXq3WBE5-YOq3fxu-9aYToyw1HDebOqcadnL-U3mO669_JYb0abXBk68HBYsvTLWgr_Xv8TgrwUB9eXmmcveA3NsrZyVS2n6pskdo5Xeb2O7G9fh6nXzhtyuvVNAEd65F9WcyNTF87eJrs5cCvMRn1Z3PmGaVYKctzvJV-ZXSgj9R8_mKF3q9UznVqsd500hny4Ap0sPa94e_v9LN38SDW8XH8gyEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84f85f87e0.mp4?token=tqfirmLGcd-Idpj-VmhoBTTMHW5EtUKiaHKwoLkAOg6QNR5HoBPVvA-qZlJ8rvyq8i0iCb9zNSlScTb7-vNroGbCuT516hvoIqgYrNsjYW1udNO_fai-dyZyGXq3WBE5-YOq3fxu-9aYToyw1HDebOqcadnL-U3mO669_JYb0abXBk68HBYsvTLWgr_Xv8TgrwUB9eXmmcveA3NsrZyVS2n6pskdo5Xeb2O7G9fh6nXzhtyuvVNAEd65F9WcyNTF87eJrs5cCvMRn1Z3PmGaVYKctzvJV-ZXSgj9R8_mKF3q9UznVqsd500hny4Ap0sPa94e_v9LN38SDW8XH8gyEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: همهٔ دنیا دیدند که آمریکا و رژیم صهیونیستی جنگ را به ایران تحمیل کردند و باید به‌خاطر تک‌تک جنایاتشان پاسخگو باشند.
@Farsna</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/460635" target="_blank">📅 11:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460634">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce5d9f285.mp4?token=UolC8enCZ63X663aufBSI2dHTZixv3f2AvYGKqXJtnOnM9g_tjo0ED2b5Luncka76eu5OYFM2KPcGsXXkwxGWU2y9RlLJ8MDrtYReb2lFCDQxI7UL_O-sTgDQTt1fFWsGdKseXTfEQw_gB48pwAFnaPrJ0vYuCKmAZbGiAf-_fxD91N9LehfBkDoXe_9yZAp7GNrl2IJJ20gA3CvkO9c_hOZZHvEMhxsLjRtamPnUM2FTjDfIKhMbEVlpVUQYmTIEfV-8I_NhKuGF6jkmxe7BaWonc_zV-O5IAWZQEmJfaLdBaQJ6_2ZXe6njs0psRHpcqQLPvp8AU_fL-WES9Ja9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce5d9f285.mp4?token=UolC8enCZ63X663aufBSI2dHTZixv3f2AvYGKqXJtnOnM9g_tjo0ED2b5Luncka76eu5OYFM2KPcGsXXkwxGWU2y9RlLJ8MDrtYReb2lFCDQxI7UL_O-sTgDQTt1fFWsGdKseXTfEQw_gB48pwAFnaPrJ0vYuCKmAZbGiAf-_fxD91N9LehfBkDoXe_9yZAp7GNrl2IJJ20gA3CvkO9c_hOZZHvEMhxsLjRtamPnUM2FTjDfIKhMbEVlpVUQYmTIEfV-8I_NhKuGF6jkmxe7BaWonc_zV-O5IAWZQEmJfaLdBaQJ6_2ZXe6njs0psRHpcqQLPvp8AU_fL-WES9Ja9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان لیگ: طبق مصوبۀ هیئت‌رئیسۀ فدراسیون، لیگ نیمه‌کاره قهرمان ندارد
🔹
باشگاه استقلال درخواست اهدای جام کرده، اما هیئت‌رئیسه در این زمینه تصمیم می‌گیرد و من و تاج تصمیم‌گیرنده نیستیم.  @Farsna</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/460634" target="_blank">📅 11:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460633">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌ ۱۰ صیاد مفقودشدهٔ بندرلنگه‌ای پیدا شدند
🔹
دفتر نمایندگی وزارت خارجه در هرمزگان: ۱۰ صیاد مفقودشدهٔ بندرلنگه‌ای در امارات هستند و به‌زودی به کشور باز می‌گردند.
🔹
هنوز از ۳ صیاد دیگر مفقودشده اطلاعی در دست نیست؛ اما همچنان پیگیر وضعیت آن‌ها در کشور‌های همسایه…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/460633" target="_blank">📅 10:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460632">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiHVy6wKPhkuBLSLUZtAewSBR_Ia7M6ZZ6c_M0OO-awWr7L6Q2_2k9cwSd42Qlf7pXWkn5f7Fhj9kaff-yyF5sF_CzaESSUhzw4VDeVXbCkqEENJ_wJxs3RLPHT0ttsb9f8UAlHUp8iACzq5lrt8hGN4NGaGelu2ifDrthz-d5t5dWcLSlO8nRbsd9J3mPzs9boC8SCZHLimyJYSn1GFVfLNFWdaDQfh2TbYkvrvmstglchM_6m4QBbz2MN3Ha_aXg6JVaP5kBw_IfucVEvF0HEIYHsJzIDWzeaDtxCcvHZYoGolw5zy0iil7BX9XQw2OrChW7vjfaGlIO-iuIPpPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اصلاح قیمت بنزین از ساعت ۲۴ امشب
🔹
مدیرعامل پخش فرآورده‌های نفتی: در نرخ‌های اول و دوم بنزین هیچ تغییری نداریم.
🔹
تنها نرخ سوم بنزین که کارت جایگاه است از ۵ هزار به ۱۰ هزار تومان تغییر می‌کند.
🔹
سهمیه‌های اول و دوم ۸۵ درصد نیاز خودروهای شخصی و موتورسیکلت‌ها…</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/460632" target="_blank">📅 10:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460631">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c20f18907.mp4?token=W30IQa_lE3ALgmwyCtVx_kBAyn8MGbsAB1V6C633fMwLCeucCmNPBd8wvBVmZ9iAvVBAhfA_yoNkACvHuxyHP0l9aYppsLdvSapHjsdWmAYEMC2bxfYup4VS3paFZyjAK13bSw767dRdfcaZgsmD3BYg5yEmUXUA4ARpKcjk-6qJqI7oWGa1UF65r0a-UrvTnPySt3jEK8JBbzF9GucRPRiwvaS97u0ug5qDBoSAri7PAO3G8J5YB9p1-9iWg4sX5HOmZYnCaD2qm0PNLPhmGiQ61RUBTYqh5yuke7n8LgS55yk-gbRFzw8CLFKdsKmrwmT1cLa_QWnKDS8iJ1A9Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c20f18907.mp4?token=W30IQa_lE3ALgmwyCtVx_kBAyn8MGbsAB1V6C633fMwLCeucCmNPBd8wvBVmZ9iAvVBAhfA_yoNkACvHuxyHP0l9aYppsLdvSapHjsdWmAYEMC2bxfYup4VS3paFZyjAK13bSw767dRdfcaZgsmD3BYg5yEmUXUA4ARpKcjk-6qJqI7oWGa1UF65r0a-UrvTnPySt3jEK8JBbzF9GucRPRiwvaS97u0ug5qDBoSAri7PAO3G8J5YB9p1-9iWg4sX5HOmZYnCaD2qm0PNLPhmGiQ61RUBTYqh5yuke7n8LgS55yk-gbRFzw8CLFKdsKmrwmT1cLa_QWnKDS8iJ1A9Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان لیگ
:
طبق مصوبۀ هیئت‌رئیسۀ فدراسیون، لیگ نیمه‌کاره قهرمان ندارد
🔹
باشگاه استقلال درخواست اهدای جام کرده، اما هیئت‌رئیسه در این زمینه تصمیم می‌گیرد و من و تاج تصمیم‌گیرنده نیستیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/460631" target="_blank">📅 10:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460630">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎥
نقدی بر یک شبه پارتی با ناظرانی راضی!
🔹
جشنواره و نمایشگاه تخصصی مد، لباس و فشن موسوم به «همای» درحالی در تبریز برگزار شد که فارغ از ابهامات مربوط به چرائی صدور مجوز و همچنین، ضرورت بررسی اهداف موسسۀ برگزارکنندۀ این رویداد، نفس حضور برخی مدیران دولت در آئین…</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/460630" target="_blank">📅 10:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460629">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BU9GL_JNJp1hzz3roQLRXdeJOK1CcJ2oq7NWml7gtKjq5qxRp5c6K-eDNv8PeDrec7SRumDNvTjOokr_u2l7fxbFii1PQWwk1a6MFFtxT9Mqni_Ld4RFgBiiwb9I_33mE3jtt7J4y1rRI5aDmafdhzemj-kDD7H9b8iPQKrOpifrfQWLz3R0cqwKdaY4nLd8quprADLuc-JmmjFgTQ2_P4BiLwQSzFpRQlyqmx9-dHYYra-5f9wfk4AmDp7fHDPvABiK3u0m4bqlZe-Uen5D0GCupxz9mKACi4hLmZ9IWJ2gyfpdfvvoRqnexKpBbIEvze1e-sq-Iyf3eXlnmgD7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنگونی پهپاد ارتش عربستان در آسمان یمن
🔹
نیروهای مسلح یمن از رهگیری و سرنگونی یک پهپاد شناسایی-تهاجمی مدل «CH-4» ارتش عربستان بر فراز استان الجوف خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/460629" target="_blank">📅 10:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460628">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRZaiWgUp5MJrGgyZBX11jTT4IzSs4jF-dAioPHOzIjJv-0c-kGSifo620vQJGARv6WLAxX0qjmYztWd2L8Ax0AVgugPB4TMJQf9z5d8RZE9jOgEs3QZWvQwRPnkD88icA7m286FexptDzQrdrdlRykkRhho7PtA9y-_ZUZurQl4xXgiV1DpXzrSCzNss0S9FOCIyNneD585ml8m0aFinpUAHWhbSNZaqFUoR652denTdS1FQtU0WEB6TyzSvudwHwmXptqEDSg86NhWdBsnmFwLPaaMCFparRNv-DO2SgL5qKHUaJ-fBd5FmKKxgNKpD11FKSU_T8QxFfSEDPv7Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شستا با ۱۶۰۰ محصول به حل مسئله‌ مردم می‌پردازد
به گفته مدیرعامل شستا، این شرکت با عرضه ۱۶۰۰ محصول و حل مسائل مختلف مردم می‌پردازد.
محمدرضا سعیدی، مدیرعامل شرکت سرمایه‌گذاری تأمین اجتماعی (شستا)، در آیین دانش‌آموختگی دانشگاه صنعتی شریف که با حضور جمعی از اساتید این دانشگاه و مدیران ارشد صنعتی کشور برگزار شد، ضمن تبریک به فارغ‌التحصیلان، بر ضرورت ارتقای مهارت‌های مختلف در کنار دانش تخصصی و دعوت این دانش‌آموختگان به همکاری با مجموعه شستا تأکید کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/460628" target="_blank">📅 10:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460627">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAvjaSFmkXvW34wvKcxoBVcMsP6EQeUbOOCdnxaS5bBMQzJk3nyBR70WZ60GZrW8lo6D3Hb2Zehc3TscnMUxTZrBKzNRXT9wzGiY3dezxaJUjCo94Q3ptFYyhMXYFRk2k2N9frDuhyNtXB9PFYbWMe-PPqQnJAOOGJ4rMKnvSOm4V7wEUsFjz9tyZuKU31zzs-DGncEJlJFzZJW7_WNlzaYAWmAUk6Ji5k3jj7_7FXu-V0L9VnvPS30iCe4mVSt1yilnRtDsPA0Mgm21Xq-flS-F4sEqhxNoukYHLI11djrB57VmzuyDrmoLWpx-8qSdl8kFWf4LqJmjgrXXshuHnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❇️
سالن مبله برای ختم
❇️
❇️
همایش های آموزشی
❇️
🔹
۷۰۰ صندلی
🔸
پارکینگ وسیع
🔹
تهیه بسته پذیرایی
🔸
هماهنگی واعظ و مداح
🔹
گل مصنوعی به نفع خیریه
🔸
سرو ناهار و شام در سالن
🔹
فیلمبرداری مراسم و صوت با کیفیت
🔸
دسترسی آسان به بزرگراه
شهید همت، شهید حکیم، شهید فهمیده(کرج)
📲
۰۹۱۰۲۲۷۷۱۹۹
☎️
۰۲۱۴۴۰۰۴۰۴۰
📣
امکان رزرو شبستان مسجد
📌
آدرس مسجد
🔻
فلکه دوم صادقیه،بزرگراه شهید اشرفی اصفهانی ره ، جنب بوستان صبا
🔸
مسجدجامع‌امام‌سجاد(علیه السلام)</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/460627" target="_blank">📅 10:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460626">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/460626" target="_blank">📅 10:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460625">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6a74dd10.mp4?token=dRHCTu46qeZ3zdJqiUjAVFar1LXOzVVppWnMDAE2N97n93Flc9Z4xrOoQNApnvet_9cGoNnVgmcniVVLIpDFN9iIngQiN2FTsBE_hq2TesNQOYpM2dhZ0QHiuURsOhah1GDYOSoYY6786MPVyYb4TabBvd0-xm0RomyabDe8s02qjy-cOwJsp-EClh3iBh7qL4JQ7R0NWm1YEBeVyC1hzutVgTTrIQsAZIKFIrPczSfWKirUaglamJEeVWAyakZzBihoRdj9-83JOOdolvaRg5QIoznvnHtJmU2lAHFZViIbYZlwP3Ci1sZ2dqjHJu4_3_rMjfGRamUI81uxHFelbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6a74dd10.mp4?token=dRHCTu46qeZ3zdJqiUjAVFar1LXOzVVppWnMDAE2N97n93Flc9Z4xrOoQNApnvet_9cGoNnVgmcniVVLIpDFN9iIngQiN2FTsBE_hq2TesNQOYpM2dhZ0QHiuURsOhah1GDYOSoYY6786MPVyYb4TabBvd0-xm0RomyabDe8s02qjy-cOwJsp-EClh3iBh7qL4JQ7R0NWm1YEBeVyC1hzutVgTTrIQsAZIKFIrPczSfWKirUaglamJEeVWAyakZzBihoRdj9-83JOOdolvaRg5QIoznvnHtJmU2lAHFZViIbYZlwP3Ci1sZ2dqjHJu4_3_rMjfGRamUI81uxHFelbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عملیات پهپادی یمن در عمق خاک عربستان  سخنگوی ​نیروهای مسلح یمن: در پاسخ به نقض حریم هوایی استان صعده توسط پهپادهای سعودی، ۲ عملیات پهپادی موفق انجام دادیم:
🔸
۱. حمله یک مرکز حساس در فرودگاه نجران
🔸
۲. حمله به تأسیسات آرامکو در نجران @Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/460625" target="_blank">📅 09:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460624">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a73fOptfF5rOI5CVhPEdbUaupIYHUI4JDOi23peD0DDDMC5z5IHTXWfcJGZcNjfZhH3ft9l02sVCSzBVqQy2obc7wHRMcqWRi3z16JfbUbYGKCRx21LgdZvaiLTzAw--mgIQKE8BGYJaRktzvEfPPAPLJF0YwWbLAB7akZ1eiV-pcPcFXubLOfo3nz3hv_FH7DqXWYGj0EMO6bYNGjdlZ1iw0vdYgv-zn09yyjZOkNYm7YMSqORJBhfFTSsFCJ_CLOyRyu2_8C_Mon5qH4GkFcBV2kWfYdYWbgdKkHAkR3WlmfkYEM6uDtgxkpZojDEDq9jG-5yf-MzPut5KJMaGUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/460624" target="_blank">📅 09:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460623">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌ شهادت نوزاد ۲ ماهه در حملۀ اسرائیل به جنوب لبنان
🔹
المیادین: در حملۀ رژیم صهیونیستی به کفر رومان، یک نوزاد جان باخت و ۱۰ شهروند دیگر از جمله کودکان مجروح شدند.  @Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/460623" target="_blank">📅 09:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460622">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/120452d242.mp4?token=S5sP12_udOKSDFq9kRw40fZQozOO_sNofVtM_Ly1KgX_1oenaWT3X8qgdVVQncfFeV-uKsFZCVTW5RUYYnTz5lY-me2BMPuqMdhQdC73aqXZ1VuehKpf3JDOShd8RiR3aOCLlmlOpW3luRVmRg1Hv3FQ42CvKDe-ICiGCZjbMt70YB5wTydqn90D44F9uFjUbVqXKmfmMpmR3vAiBjx1VEF0CHwY8TtMQO5s1oa--x7mpTGahW7xbU5Iou7LwLEX_Mr3ANa3FbHt8ofJGXlGJQ2LRURfILubbtimHyjz9klSqcsamqBcmxz0NR52YEAbaaJ8NGrt_YYNNFHa1TlnGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/120452d242.mp4?token=S5sP12_udOKSDFq9kRw40fZQozOO_sNofVtM_Ly1KgX_1oenaWT3X8qgdVVQncfFeV-uKsFZCVTW5RUYYnTz5lY-me2BMPuqMdhQdC73aqXZ1VuehKpf3JDOShd8RiR3aOCLlmlOpW3luRVmRg1Hv3FQ42CvKDe-ICiGCZjbMt70YB5wTydqn90D44F9uFjUbVqXKmfmMpmR3vAiBjx1VEF0CHwY8TtMQO5s1oa--x7mpTGahW7xbU5Iou7LwLEX_Mr3ANa3FbHt8ofJGXlGJQ2LRURfILubbtimHyjz9klSqcsamqBcmxz0NR52YEAbaaJ8NGrt_YYNNFHa1TlnGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصلاح قیمت بنزین از ساعت ۲۴ امشب
🔹
مدیرعامل پخش فرآورده‌های نفتی: در نرخ‌های اول و دوم بنزین هیچ تغییری نداریم.
🔹
تنها نرخ سوم بنزین که کارت جایگاه است از ۵ هزار به ۱۰ هزار تومان تغییر می‌کند.
🔹
سهمیه‌های اول و دوم ۸۵ درصد نیاز خودروهای شخصی و موتورسیکلت‌ها…</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/460622" target="_blank">📅 09:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460621">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0JgMOPmg7xueuizZqRKtHi9S7-Uh_9qcy7Yt9fnAiW5TosqDj9M6F8Jl85cKcFW4_ka09DgdbFT4CPiu-JpF6hetqteFHyYGuwlGX5hqPa0zyu7wboVto4EfZBDY7iecYpideMng8Y9RyTyfDQ95cYPXfgxCToB5t920MRu-Pt73cOpi7xlf4iiuyjK1Bh5LXotkfGvO64-mMW4f05JTvFA4gE2pgFYtpuIJ-pPra1cd0O1_fh8VkZlfIq5CyhSmx55J2vp8S-wPCVESzEvmigr0mwntu1GwqYSjbcFrzsGDIUhpPfzLXL0Am90SJo8ST_ArwGR0TibUh6U5O9jzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۵ ریشتر در عمق ۷ کیلومتری زمین، دانسفهان قزوین را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/460621" target="_blank">📅 09:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460620">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efe97b2643.mp4?token=GNvK_A3r0xeDm3egMd7oVHOkPUTVPtT4MMtAlxH8BSc9rWTvi4MqNTNBKw29c1zPzkjYddzfeELpn0_-YBPIdkPfhEIRak9CLlbR3IF-c_xHri9rO_IEXuW__X2lhUiRitI817NteKpEbqNYkMPVl1D0itCc9ElmB9IJ0ML6YyEcWh7m5TyL5Ps97cSut0abWEz7CPSuwrFO7yVQRCqFItJpFKYnR2wo6rXslDVR8mUw7o_SLoc5s5tZVWXoSVQdaQhw8ufNCQ-D_4LIR3CWllGEU9ygDBul0cLED2-Ko1EMBBuPnoH0cJwfEq4EBVGiRPu5MHaarSXtzqWXL2H5hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efe97b2643.mp4?token=GNvK_A3r0xeDm3egMd7oVHOkPUTVPtT4MMtAlxH8BSc9rWTvi4MqNTNBKw29c1zPzkjYddzfeELpn0_-YBPIdkPfhEIRak9CLlbR3IF-c_xHri9rO_IEXuW__X2lhUiRitI817NteKpEbqNYkMPVl1D0itCc9ElmB9IJ0ML6YyEcWh7m5TyL5Ps97cSut0abWEz7CPSuwrFO7yVQRCqFItJpFKYnR2wo6rXslDVR8mUw7o_SLoc5s5tZVWXoSVQdaQhw8ufNCQ-D_4LIR3CWllGEU9ygDBul0cLED2-Ko1EMBBuPnoH0cJwfEq4EBVGiRPu5MHaarSXtzqWXL2H5hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری یک متکدی در بجنورد که خود را به معلولیت می‌زد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/460620" target="_blank">📅 09:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460619">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb62d7caa3.mp4?token=eF6LleWWv-Pj-Xi7fVQMQlasxacbl4nHQgGVMO0HgvX-aR4LZphm1Uz7mNWdOOCOX5MqYkf5ybNMQ1XsnOgmPAloFvTrb80MQkUdB0l04DvnKUwggVI0DzUmPtmmLKltv8db22Ogz1cblvDpOv43HSWROferV9BMu-Qv4tWFltM-MN6lvew-Z5Vecp74kjW0hO3pK9bUA3E6E9Fqkf1rVov2cKWz_eDvmbBFT1cnvM6rG7poUhT4bRI6pUQZSdOwCuWLydFd7fx3RJVzy487_9m7ov4Sl_MeEUPKWKH2-f1Ezn9S4M6VRZV7nGHL_4aavEKSDucaeqOSpxFhe3JzEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb62d7caa3.mp4?token=eF6LleWWv-Pj-Xi7fVQMQlasxacbl4nHQgGVMO0HgvX-aR4LZphm1Uz7mNWdOOCOX5MqYkf5ybNMQ1XsnOgmPAloFvTrb80MQkUdB0l04DvnKUwggVI0DzUmPtmmLKltv8db22Ogz1cblvDpOv43HSWROferV9BMu-Qv4tWFltM-MN6lvew-Z5Vecp74kjW0hO3pK9bUA3E6E9Fqkf1rVov2cKWz_eDvmbBFT1cnvM6rG7poUhT4bRI6pUQZSdOwCuWLydFd7fx3RJVzy487_9m7ov4Sl_MeEUPKWKH2-f1Ezn9S4M6VRZV7nGHL_4aavEKSDucaeqOSpxFhe3JzEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: مردم ضرورت برخی تصمیمات را درک می‌کنند
🔹
امروز پس‌از اعلام قیمت جدید نرخ سوم بنزین، صف جایگاه‌ها خلوت بود.
🔹
این نشانۀ فهیم‌بودن ملت ایران است. @Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/460619" target="_blank">📅 09:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460618">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سپاه اصفهان: عملیات انهدام کنترل‌شدۀ مهمات امروز در جنوب اصفهان انجام می‌شود
🔹
احتمال شنیده‌شدن صدا در محدودۀ صفه، بهارستان و اطراف آن از ساعت ۹ تا ۱۴ وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/460618" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460617">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6398035fdf.mp4?token=Hd3mDWXzmvsa6pUo2ArBxjTCxlnosyzg1ZzLqm9eBbMywSh-5ifGleUF07E1CSNq5LtSi_nGUWxD6XtmKCKNuXBDoYUvQ9F9W3m4MsQGuoJhyOelqby4sWItOLf_lcTi8O2WU_lvp0ppoFU1RZmvRrXHnookO_SxDO_tlh0MW3oSHIpoayIEVVUlmGLR8bpvRNi4aMh3u6CN3f8HhhtLACw1bxSIwiD9ovJYNJaNno021TJC_8u8_t2tdUGbEr161eWXwn-QFGp0EG0WCR2Qyrvbkr-KmTQuIk1IQwdyMsbMMif2aKG2UUuQgMcyfEyBQTcHjvTAlGDjE4HJvxNqbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6398035fdf.mp4?token=Hd3mDWXzmvsa6pUo2ArBxjTCxlnosyzg1ZzLqm9eBbMywSh-5ifGleUF07E1CSNq5LtSi_nGUWxD6XtmKCKNuXBDoYUvQ9F9W3m4MsQGuoJhyOelqby4sWItOLf_lcTi8O2WU_lvp0ppoFU1RZmvRrXHnookO_SxDO_tlh0MW3oSHIpoayIEVVUlmGLR8bpvRNi4aMh3u6CN3f8HhhtLACw1bxSIwiD9ovJYNJaNno021TJC_8u8_t2tdUGbEr161eWXwn-QFGp0EG0WCR2Qyrvbkr-KmTQuIk1IQwdyMsbMMif2aKG2UUuQgMcyfEyBQTcHjvTAlGDjE4HJvxNqbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عربی از حملۀ پهپادی به مقر تجزیه‌طلبان تروریست در سلیمانیۀ عراق، و برخاستن دود از این محل خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460617" target="_blank">📅 08:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460616">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZE9HufZnjg9oWscPVzziONa5w1xxY_PIhX0ymVkCMPRzM-Opt1Dm6SizI4mfEMqR0yW24FEu5_80SfRfurean21MmoZpQMe7dJTB0chJ95TiO1jb4kJZR4KEGKwXr6gcmgCa8X1Cutfye6ElOFYMe3NxHkvRW0uteYEs3IdQhEF6Al8gA20ci-SlwBBJUPkLzQwk5a6xyt_hVkqirructKpoGVyZ3imnk-pWALjqXHktXGNHuiJy8CZ9oFBkvfWt59lSLobGscql9mv2Q37EeOClmxJI0evTe0U_4dAGPRHr3f4kqn8_loWb06T_ybIjfo3xj0PBcPIV-012oDMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس علیه استقلال تا دادگاه عالی ورزش CAS می‌رود
🔹
پس از هفتمین دربی پایتخت که با تساوی استقلال و پرسپولیس به پایان رسید، باشگاه پرسپولیس به دلیل آنچه حضور غیرقانونی یاسر آسانی در ترکیب استقلال می‌داند، از این بازیکن شکایت کرده است.
🔹
مسئولان باشگاه پرسپولیس معتقدند مدارکی در اختیار دارند که نشان می‌دهد آسانی به‌صورت غیرقانونی در استقلال حضور دارد و به همین دلیل پیگیری‌های خود را از طریق مراجع قانونی و فدراسیون فوتبال آغاز کرده‌اند.
🔹
شنیده شده مسئولان باشگاه پرسپولیس قصد دارند در صورتی که از فدراسیون فوتبال به نتیجه نرسند، پروندۀ این موضوع را به دادگاه عالی ورزش CAS ببرند تا شکایت خود را از طریق محاکم بین‌المللی پیگیری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460616" target="_blank">📅 08:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460615">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk0qfkt8vrYwpTx0Lvs3WraOCd-pH_Vj75l81yVKX4ZJ7VQ-au1qffgf2o6REBON8BGf18a76mS-Qnjdif1uWIqmVX7SDmlb8wS1b73oy5y97odQaUiDBHsBZFbxAutwLk-qpAXhKfBVnG8kqjYjJl5TU0wkQQoSvEXc7eauq_-lA-lAFVYQHt5cbFqFFU-rbq6Uqj2-HLZ7Ln6xBRWGGZV_Y-d5Vh3iBoiy8TtHeGjF9rMfYn857FThREtqa139LGN58yK50OV-GLT9NfBOUlRGtfq3tc_TGM-uWVxxbruyER2uquJirqI7BBF-D4nIomu8pvoZYYHiUllDqfKSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی‌ها از هرمز گریختند
🔹
داده‌های جدید شرکت رهگیری کشتی‌ها «کپلر» نشان می‌دهد که میانگین تردد روزانه کشتی‌های باری در این آبراه استراتژیک به ۱۰ فروند در روز رسیده که رکوردی بی‌سابقه در ۳ تا ۴ ماه گذشته تاکنون محسوب می‌شود.
🔹
کاهش چشمگیر تردد در تنگۀ هرمز درحالی به‌قوت خود باقی است که وزیر انرژی آمریکا دیروز ادعا کرد به‌طور متوسط روزانه ۹ میلیون بشکه نفت از تنگۀ هرمز عبور می‌کند.
🔹
اما براساس داده‌های امروز کپلر در روز شنبه تنها ۲ فروند کشتی از این مسیر عبور کردند که ناچیزترین تعداد در روزهای اخیر است.
🔹
روز یکشنبه نیز ۶ فروند کشتی تردد داشتند که اکثریت آنها از مسیر آبی تحت کنترل ایران گذر کردند.
🔸
یک مدیر کپلر گفته به نظر می‌رسد وزیر انرژی آمریکا عدد ۹ میلیون را از هوا بیرون کشیده است. واقعیت این است که ایران کنترل تنگه را در دست دارد و تنها نفتکش‌هایی از تنگۀ هرمز عبور می‌کنند که از مسیر آبی تحت کنترل ایران حرکت می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/460615" target="_blank">📅 07:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460614">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هوای پایتخت همچنان در وضعیت «قابل قبول»
🔹
شاخص کیفیت هوای امروز پایتخت با قرار گرفتن روی عدد ۹۴، در وضعیت قابل‌قبول است.
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/460614" target="_blank">📅 07:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460613">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‌ روایت برادر همسر رهبر انقلاب از مأنوس بودن ایشان به قرآن
🔹
در یک سفر با هم بودیم، من می‌دیدم جایی که هیچ کاری ندارد، قرآنش را باز می‌کند، دو صفحه می‌خواند و نشان را جابه‌جا می‌کند و دوباره می‌بندد. قرآن مخصوصی دارد که اصلاً از خودش جدا نمی‌شود.
🔹
ایشان…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460613" target="_blank">📅 07:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460612">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">امروز، آخرین مهلت ثبت‌نام آزمون کارشناسی به پزشکی
🔹
داوطلبان آزمون پذیرش دانشجوی پزشکی از مقطع کارشناسی سال ۱۴۰۵، تا پایان امروز فرصت دارند نسبت به ثبت‌نام اینترنتی و ارسال مدارک مورد نیاز اقدام کنند.
🔹
دانش‌آموختگان همۀ رشته‌های کارشناسی مجاز به ثبت‌نام هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460612" target="_blank">📅 07:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460611">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تردد در نقاط حادثه‌خیز و فعالیت‌های دریایی مازندران ممنوع شد
🔹
مدیرکل مدیریت بحران مازندران از احتمال وقوع سیلاب، طغیان رودخانه‌ها و رانش زمین در پی فعالیت سامانۀ بارشی در سطح استان خبر داد و گفت: گردشگران و فعالان دریایی از تردد در مناطق پرخطر و فعالیت‌های تفریحی خودداری کنند.
🔹
همچنین هرگونه تردد و فعالیت غیرضروری دریایی از عصر دوشنبه ۱۶ تا صبح چهارشنبه ۱۸ شهریورماه ممنوع اعلام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460611" target="_blank">📅 06:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460610">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سه روز بلیت نیم‌بهای سینما از ۲۰ شهریور
🔹
به‌مناسبت روز ملی سینما، بلیت سینماها از جمعه ۲۰ شهریورماه به مدت سه روز به‌صورت نیم‌بها عرضه می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460610" target="_blank">📅 05:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460609">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxbezPPb2CDnZZm9tmozC6432-ufEs-TngaS3UzIQuTIWgsuXcDg3WnpxHsWkOp5ApOMeyXpjJt5kJ1DIbvqqDKcHnrtWNtyrGldpBQsqImESgyQlTNDGK-0zI3ZvgyghENXGFaTf7por4HSOqFmr0GSWnuVtXjXq3Vppoq6gV57zfuaRSvK_IwnF6fUw0dUt1ii7shnKxdCs2Nus48o2NJ5QrE2J1dDcl8yfKot3EmDIUWPoRjoJ_3ehyoIVHQYdPvrgxRnarNKj7zwPl_ffxI8kSheKnmgEv-qVT0w6T2OybklHq1tdbGAP1R8wcxw1J5jnBTxpt8QqZv1zN17TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دردسر جدید ایلان ماسک برای حذف فرمان و پدال!
🔹
ورود تاکسی‌های بدون فرمان و پدال تسلا به خیابان‌های تگزاس، با واکنش تند پلیس راهور و سازمان ایمنی جاده‌های آمریکا روبه‌رو شد.
🔹
علت این واکنش پلیس آن است که تسلا بدون گرفتن مجوزهای رسمی، فرمان و پدال را به‌طور کلی از خودرو حذف کرده و قوانین ایمنی فعلی را که بر اساس رانندۀ انسانی نوشته شده، زیر پا گذاشته است.
🔹
این جنجال قانونی در حالی آیندۀ تاکسی‌های خودران را در هاله‌ای از ابهام قرار داده که حذف امکان کنترل دستی، ترس و عدم اعتماد شدیدی میان رانندگان و سرنشینان ایجاد کرده است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460609" target="_blank">📅 05:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460608">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">عرضۀ واکسن آنفلوانزا اوایل مهر
🔹
سازمان غذا و دارو: با وجود تأخیر تولیدکنندگان خارجی، افزایش قیمت و مشکلات نقل‌وانتقال مالی و حمل‌ونقل، واکسن آنفلوانزا از اواخر شهریور و اوایل مهر در دسترس قرار خواهد گرفت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460608" target="_blank">📅 05:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460607">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌ المیادین: تیم‌های امدادی تاکنون ۱۰ مجروح را از ساختمان مورد حمله در نبطیه در جنوب لبنان پیدا کردند. جست‌وجو برای یافتن افراد دیگر ادامه دارد. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460607" target="_blank">📅 04:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460606">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نجات بیش از ۳۰۰ نفر در آتش‌سوزی یک هتل‌آپارتمان در مشهد
🔹
سخنگوی سازمان آتش‌نشانی مشهد: حادثۀ آتش‌سوزی گسترده در طبقات منفی یک هتل‌آپارتمان واقع در خیابان آخوند خراسانی مشهد به وقوع پیوست.
🔹
بیش از ۳۰۰ نفر در محل حادثه گرفتار شده بودند که با حضور نیرو‌های آتش‌نشانی و انجام عملیات امدادونجات، از محل خارج و نجات یافتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460606" target="_blank">📅 04:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460605">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8ec87ac3.mp4?token=CD8qNngYzRhwxo_ODE9O6dngXOWhMErhdU878LwOqRmezA5KVmXLjN1KuxN5IWJSktRql3Jv2878Viuh11hqUF1OdNWGv2YPiCF5k_Sga8nh8QvS9D_xpJ4IuSwyjXqhZvOUczS5LrUEw2qbx07uJkxV6IGt3rvW7Jwe1ml_aXK-Ty5WVnnnHKogXE46bmObBLYJWnpNaISIaFZnhhtNAfq9WyrXgwzVQsVyagZOOO5mGBrdJp_Lm_3swFSY0Q-RiuQ-h4XXfoTsKAr4LgOq7lzg3W6IccSZDo5WyWl9jmdf_YHwDkDVsbgdC-JB9DbH8UCFNxD6AP1QTgLKgc3MLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8ec87ac3.mp4?token=CD8qNngYzRhwxo_ODE9O6dngXOWhMErhdU878LwOqRmezA5KVmXLjN1KuxN5IWJSktRql3Jv2878Viuh11hqUF1OdNWGv2YPiCF5k_Sga8nh8QvS9D_xpJ4IuSwyjXqhZvOUczS5LrUEw2qbx07uJkxV6IGt3rvW7Jwe1ml_aXK-Ty5WVnnnHKogXE46bmObBLYJWnpNaISIaFZnhhtNAfq9WyrXgwzVQsVyagZOOO5mGBrdJp_Lm_3swFSY0Q-RiuQ-h4XXfoTsKAr4LgOq7lzg3W6IccSZDo5WyWl9jmdf_YHwDkDVsbgdC-JB9DbH8UCFNxD6AP1QTgLKgc3MLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): در زیادکردن دوستانت تلاش نکن
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460605" target="_blank">📅 04:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460604">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌ خاطرۀ برادر همسر رهبر انقلاب، از تولد اولین فرزند ایشان
🔹
فریدالدین حداد عادل: برای به دنیا آمدن اولین فرزندشان در بیمارستان رسالت، چون ملبس نیامده بود، کاپشنی که مادرم برایمان آورده بود را پوشیده بود. جفتمان شبیه به هم شده بودیم.
🔹
ایشان وقتی در بیمارستان…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460604" target="_blank">📅 03:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460603">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌ المیادین: ساختمانی که دقایقی پیش از سوی رژیم اشغالگر اسرائیل تهدید به حمله شده بود، مورد هدف واقع شد.   @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460603" target="_blank">📅 03:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460602">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌ اعلام حملۀ هوایی اسرائیل به جنوب لبنان؛ صدور دستور تخلیه برای ساختمانی در نبطیه
🔹
ارتش رژیم صهیونیستی برای چندین ساختمان در منطقۀ دیرالزهرانی در جنوب لبنان، هشدار تخلیۀ فوری صادر کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460602" target="_blank">📅 03:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460601">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ادامۀ جنایات اسرائیل در غزه و لبنان
🔹
منابع محلی از تداوم حملات وحشیانۀ رژیم صهیونیستی به مناطق مختلفی در جنوب لبنان، و همچنین نوار غزه خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460601" target="_blank">📅 03:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460600">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnNB9p4CVFxhVy2IDeFRmaQAEqSEz5N6gR5LgquNI4gzg0LUjqn4zNsB_WECHzuwtFgmUu8p1A8JRu5Bj3FhOwb0oPnwQFCQ0viVzeDRj2DiOgAWE4j7_QAgwRMWrKabpwh4c-Tjp1uVtHlfJbMF1WkKUFteAFu1yg7f_yUWDzLB27lMULPNDd1P4-xar8rKas6RMB3GcG_cBv93jZvsUJ_jN5PXjhLgpwlGVUFDbs6_c9GbW3VUmMxgYTVm8bXdByMlQTux9FPtN7MBMdH1xADDTqL7DLSZFXXGm8Waibz5CE0ofaYVVQO3RRm-0f8ZrGK5Zmn2s0QRtTZdonynXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنجیرۀ «پاسخ هسته‌ای کرۀشمالی» مجهزتر شد
🔹
رهبر کرۀ‌شمالی در مراسم آب‌اندازی و ورود رسمی ناوشکن جدید این کشور گفت که این ناوشکن بخشی از سامانۀ پاسخ هسته‌ای پیونگ‌یانگ خواهد بود و می‌تواند حملات تلافی‌جویانه «ویرانگر» انجام دهد و استقرار این ناو در آب‌های شرقی شبه‌جزیرۀ کره، پیام روشنی برای دشمنان پیونگ‌یانگ دارد.
🔹
رهبر کرۀشمالی همچنین اعلام کرد که طی هشت ماه آینده مرحلۀ دیگری از تقویت توان دریایی خود را به نمایش خواهد گذاشت.
🔹
کیم همچنین از ادامۀ ساخت پایگاه‌های دریایی در سواحل شرقی کره شمالی خبر داد و گفت این کشور قصد دارد یگان‌های جدید دریایی ایجاد کرده و انواع مختلفی از ناوهای جنگی را تولید کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460600" target="_blank">📅 03:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460599">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39055cd071.mp4?token=fteVMwln9fB1baOpbt_orgpWFCMHvgpR6k-082L8Hl3RXzICDvE9aiOuAPcVSUyT-TwB4NM9X2TQnw-MjUFjQDB_8ApC_vNAhcuj4dH1_v1QdtirNnSWfyPgxngufoBt-_SC0yeIKZr2wWUQ4uVRKRP_blFiwuO-VCcyRUCMiYkKnEEHh3mlvtds0czR7C4oZsMCVVX3_LFhcy7Zgb5OB88aJ83BPadySPkYv5qrju034M30qXZZ9AxkNatF-n1sp3hyEl9jRpWVopofoMyp3bZ6uiHWh1fDH-HizOdaIB6ABBUvJgspDDwKG_EOuEWvOhoKf4vaXolTTUp2Aerx-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39055cd071.mp4?token=fteVMwln9fB1baOpbt_orgpWFCMHvgpR6k-082L8Hl3RXzICDvE9aiOuAPcVSUyT-TwB4NM9X2TQnw-MjUFjQDB_8ApC_vNAhcuj4dH1_v1QdtirNnSWfyPgxngufoBt-_SC0yeIKZr2wWUQ4uVRKRP_blFiwuO-VCcyRUCMiYkKnEEHh3mlvtds0czR7C4oZsMCVVX3_LFhcy7Zgb5OB88aJ83BPadySPkYv5qrju034M30qXZZ9AxkNatF-n1sp3hyEl9jRpWVopofoMyp3bZ6uiHWh1fDH-HizOdaIB6ABBUvJgspDDwKG_EOuEWvOhoKf4vaXolTTUp2Aerx-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع پیکر شهید مدافع امنیت در تنکابن
◾️
شهید امیرحسین سلیم‌زاده در حملۀ دشمن خبیث آمریکایی به خوزستان به شهادت رسیده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460599" target="_blank">📅 02:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460598">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">روایت فریدالدین حداد عادل از زندگی و شخصیت رهبر انقلاب
🔹
برادر همسر رهبر انقلاب: زندگی آقا مجتبی بسیار طلبگی و ساده است. در قم که بودند، خانۀ ساده و وسایل محدودی داشتند. کف خانه هم تنها با موکت مفروش بود. وقتی هم که برگشتند به تهران، رفتند و در یک خانۀ ۷۰،…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460598" target="_blank">📅 02:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460597">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ادامۀ جنایات اسرائیل در غزه و لبنان
🔹
منابع محلی از تداوم حملات وحشیانۀ رژیم صهیونیستی به مناطق مختلفی در جنوب لبنان، و همچنین نوار غزه خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/460597" target="_blank">📅 02:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460592">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVfk1eWYYiRwyYoCZ-uLtRKFum3r37QV6Y40qBClt-6W5DXUzlMmd2w9QwH8Jq069BAoXhIUHJsCg-oMCwRQ3D18ZhTuAAMlO_QMIs3_e1ZhB0NwMmDAe97oAfaXM1Rur2zBh39TIBWQsdcjjTZWZf3kS-kVXw38qZszggRj9a2YttrMoYWcuQtmSJtQTwwUgF7iDnSXmYa7Ib1O-AQBAsvuzlvy3E3KOsIwemjlPTvDyjRrHE-q5Ne4RMGeHDcNoEI6jpJLzx8ThNitHa0WOWyLjYTYVW0tYMLaM1BH2YFt8RrhzpfroAmhsNGRxk7kfC1xQu5gE-QjMeiUHqV5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vH9OYvtLnixX4Kj-PgypmXFufnzvgb9qsuQ5IXGVskkORJG_I0c8FX5hKidsGMALFe9SMCNZSCiAI47gHT7gCWL06PzB-Ot_Mp4nSdsreNY0ZIKB-0oIpxAhrUeICsJgdOfhNb10RqFCTxhhgq7FB8gTldw7KG36sfaIiJXYltZM3ETqFWH5U7BCDf3pUr5P2IVUhnXXQWbRXVlmKAkLw_yVQtdF0XbwNtugMKswTJiRaLY3hdg5pplXJVgZHUqf6XriBib2l789TJyeOkpSHcyKYkxhkBl3pa2szp67osFsnzJOGN1_n_UEUiKqslQgEQ8HaCvTGG66NevDOyvC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fOg02nyykBdYZp9zZOAeJEI_8d-BJsWRRX0WejROhojjOJ7yseXvBiOjmGomWf14Gjxs90OcSE4ulvbrJghsSdDROC7YhLKF4bIDNN60UVSWLcakzc9crXeYFQB-l0Lyc1Kekl-dO5bHTV2hwg9MkgiIUGOTvA1Z3myTNtvEC73D4a91JdUxLuZppRO9u7Iw4BrySehHSv64iG15wxqaGDF3hWBTjhpstGcv7Y__5pXKUukqe-auz9pxuyU3BIaJTeQ9SJos_XhF3uysQ4Mn3wt-RR8B9FgafSvmDoORiGQyLjJWjtPRXfogCIGnkWf7ZFsvpKBeDJoCuXMShO3G1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqsqeSxaQ67FskSiOgmLFbE-oXcGYxR5OvVnEwouLUQDhmE3BiLrh6Zgtpy6M-X8qcnyC4ueuBDOnu12V2iZZbzOtKMtcX6mfo68QJmIUzbklmwXbJ0OylE-fPLU4HXumZh0Q9ospcw28FQWSXh1yWsLhhQ-_B42y_3qAsgdjxXGgS6bqy1lOcY9ssHtrLlqvZSg9R7khN49cVZk06ob3fOByjJtObCGNrT-HBd8JOPhN1C4OeC3O7g5gh2VH1B57BP_B192W65WhzD54wa6ekfQ1pNosHgujKDme8zXiWFRCd9LNaID0FcGKO7aqCDB6DFPHrOJNils-iecswiU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2lhY0St5I-BTRLGqrVjgyinBOOdwBGqcRb8bC0fJZdsvR33LaKT5yGfJSvw9REYZS2Po2Sw7ULoIx0AId1sAB9scsnAB5crU1-fjbfLnlvlJ8k0KO2C5lHJqCRUKcPwxXkOfXV2HIq5QwKJNF_Th8ZKG4987xjv7cxwwGxB6N2Lxqa2Lb38Rn8xCfquohFbfbMIkEpZ7rHRYILeWUE2pHTumtCVecwiGJZ8uqCvQqls_0BC9wDAmC2l_oSm3444H8PJYFGk-2OStsG9HwkQYUwUhMpFsnSPvog0FKeKRTcKgCbe2YyanblaXSALanjR5d6gjQ1kqfwjLFgDEHkJ-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
قطعات موشک به‌جا مانده از جنایت آمریکا در عروسی سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460592" target="_blank">📅 02:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460591">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">روایت فریدالدین حداد عادل از زندگی و شخصیت رهبر انقلاب
🔹
برادر همسر رهبر انقلاب: زندگی آقا مجتبی بسیار طلبگی و ساده است. در قم که بودند، خانۀ ساده و وسایل محدودی داشتند. کف خانه هم تنها با موکت مفروش بود. وقتی هم که برگشتند به تهران، رفتند و در یک خانۀ ۷۰، ۸۰ متری ساکن شدند.
🔹
خواهرم در مدرسه کار می‌کرد و خردخرد فرش ماشینی و مبل راحتی تهیه کرد. مبل سبزرنگی بود. با شوخی به خواهرم می‌گفتم آخر این چه رنگی است گرفته‌ای؟! و این‌طور سر به سرش می‌گذاشتم.
🔹
یک بار خواهر بزرگ‌ترم گفت: فرید! دربارۀ این مبل حرف نزن! زهرا بعد از مدت‌ها پول جمع کرده مبل خریده و تو مدام به رنگش گیر می‌دهی، او هم اذیت می‌شود. قبول کردم.
🔹
حالا بعد از بمباران، این مبل بزرگ‌ترین چیزی است که از آن خانه باقی مانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460591" target="_blank">📅 01:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460590">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌ المیادین: در اثر تجاوزات رژیم صهیونیستی به نوار غزه، از بامداد امروز ۴ شهید از جمله دو کودک به شهادت رسیده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460590" target="_blank">📅 01:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460589">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=AIzk9VmLravLyafOXpwuQCvmeyFDjoMdL5k3hW5FOwBopc4gDJULI73nIe1KfImKK1WLCmi20GDAWRe4Ofv0Xu7is68I66ySt38cEANvlQBYLijs1Pph-QqmegqLvSgb42ILZtHWeW-NCiGhycDM2WAexg0_qBntmWBX6KypZE_pygLlXljUo-Xx68pc58m3w5VAtlUusue7BQWL6R2Djoly2N3awrJvj6326BXnOkcKEAjvX6SNXCxvD7a0sq406fbkjSzTekJxuA7yk9Gdenxr7Em0Onm4XmkxjfRogAedUW4iXTLZJFLQJI9ZHLQ9HDsGbEwISoeazMqdoSD0pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=AIzk9VmLravLyafOXpwuQCvmeyFDjoMdL5k3hW5FOwBopc4gDJULI73nIe1KfImKK1WLCmi20GDAWRe4Ofv0Xu7is68I66ySt38cEANvlQBYLijs1Pph-QqmegqLvSgb42ILZtHWeW-NCiGhycDM2WAexg0_qBntmWBX6KypZE_pygLlXljUo-Xx68pc58m3w5VAtlUusue7BQWL6R2Djoly2N3awrJvj6326BXnOkcKEAjvX6SNXCxvD7a0sq406fbkjSzTekJxuA7yk9Gdenxr7Em0Onm4XmkxjfRogAedUW4iXTLZJFLQJI9ZHLQ9HDsGbEwISoeazMqdoSD0pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهران رجبی: حضور در تجمعات شبانه وظیفۀ ملی، دینی، دنیایی و اخروی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460589" target="_blank">📅 01:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460588">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Do9w_K_5pu3Uzy7TOlM52mOxoXFlEfxs_s8xyxA5mvVmiewMnswT1Y8HKk-2DyTtlO_q_uJEL4WJkMdXrb5TyljCr9HRB3-KKCN60d1EqC7C_-JCXdx54LdckFeNn9rzs0JnxaSFNd4YjpcDmwejKRBpV8UxsSNi0h0kNtn826Xm4bCzDFUROD8o8eKIAkxYQaTdMj6nacQs27CiVOk_U9ManaP_plz-evPHTB57Phv25JnJVzWkVHJmsbG_eeXBM7dAlwTNK9nM79vk_WMY7dcvRvvDsg1pxl2xUihUmOd3iJMhFZwXeYJR_pV5mI-1quvI4cG-REPDZAMaXbnCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سانحهٔ هوایی در آمریکا؛ ستون عظیم دود در آسمان میامی
🔹
پلیس و واحدهای آتش‌نشانی میامی پس از سقوط یک هواپیمای ۷۶۷ پرایم ایر در فرودگاه بین‌المللی میامی به منطقه اعزام شده‌اند.
🔹
گزارش‌ها حاکی از آن است که این هواپیمای باری امروز بعدازظهر به وقت محلی از باند…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/460588" target="_blank">📅 01:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460587">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyKuI-dtBRa8IZ_mmOg7D5xNO1tJ6ZDkBb9ajrTRd3LmPtLjdP7LS6YhT1tb3K5pOxv8lpI_g9zV100NhKnFz9E6CL4uODSq3435uvTw8A37N2lYfu1VOfS8dTL4q96uxb-fO3UpKU86jKl1s9YaeLudf090XzfxyyLxJYTu5I90XiW9nyumKzL_B-uv--h96AbYBAeJ0PwefIx_T-tChDZggMUoAundiJ0u4PQaQUWUX0OAO21pAa56s8OfNEIzo4hQ-b96HeYlMS0H29TrBONAuq1aYje-sQk2RP-08b24lfeg09nyEmDVrY_FOEm25RFQJ3XKq4onUrE2n-Ep7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: اقدامات تجاوزکارانۀ آمریکا عامل ناامنی در تنگۀ هرمز و اختلال در کشتیرانی تجاری بین‌المللی است
🔹
سخنگوی وزارت خارجه: تنگۀ هرمز تا پیش از ۲۸ فوریه که آمریکا و رژیم صهیونیستی به ایران حمله‌ور شدند کاملا باز بود. واشنگتن جنگی غیرقانونی و وحشیانه بر منطقۀ ما تحمیل کرد و جریان عادی کشتیرانی را مختل نمود. نفت‌کش‌ها متوقف مانده‌اند، تجارت مختل شده و بهای انرژی سیری صعودی پیدا کرده است.
🔹
اکنون واشنگتن تقلا می‌کند ایران را عامل این اخلال و ناامنی که آمریکا خود مسببش بوده است معرفی کند و کل دنیا را مجبور به پرداخت هزینه‌های گزاف اقدامات غیرقانونی‌اش نماید.
🔹
براساس روایت واشنگتن، جنگی که آمریکا آغاز کرده باید به نحوی وارونه به‌عنوان هزینۀ رفتار ایران برای جهان قاب‌بندی شود.
🔹
آمریکا جنگ را آغاز کرده، اما انتظار دارد تمام جهان هزینۀ آن را بپردازد و همزمان ایران را مسبب آشوبی جلوه می‌دهد که خود عامل آن است.
🔹
این وارونه‌نمایی، به‌غایت بی‌معنا و بی‌اساس است!
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460587" target="_blank">📅 01:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460586">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ9cDXa5Lo6RxsNpW7312u4gjH1AdU56nepEpQLH8ha-JMaw1a-dOMellqKd3xWWtG3-9RKjTeEKATxM5WAIuNTU_2gmrsjEBtP14qEsIkMTIeVq7OYsEadR3Y5O502PTKzMNM_jf1sznJ-B_syx16iRbnphBvu0DZ643wBbwSzs0wqOT2r5e1HnM6QPMqKzkNLQ_Riw-N2m0mu-rYdRoNHY_Mzu1dnX95nKo7JaeOz9FYQ_HqHrd61-8oCwwixeSAobcr7HYvE6FcVXQc0So8xTta06G8T0DW582In1zaanPj5YVJ8qVFbUGaBeY7MCmVKt82x4E-VmgAN3yVhBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«پینوکیو» فرماندۀ جنگ اقتصادی علیه ایران
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا فرماندۀ جنگ اقتصادی علیه ایران است. او در هفته‌های اخیر عملیات روانی را کلید زده و گفته‌هایی نظیر «افزایش صف بنزین در ایران» «رسیدن دلار در ایران به ۳۰۰ هزار تومان» و «تمام شدن نفت روی آب ایران» مطرح کرده است.
🔹
با این‌حال افکار عمومی در آمریکا و رسانه‌های رسمی او را یک دروغ‌گو می‌خوانند و معتقدند او دست پینوکیو را از پشت بسته است!
🔹
معرفی خود به عنوان کشاورز، ادعای سقوط قیمت نفت به ۴۰ دلار، و ادعای عبور ۱۳۰ میلیون بشکه نفت از تنگۀ هرمز، تنها نمونه‌هایی از دروغ‌ها و ادعاهای اسکات بسنت است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/460586" target="_blank">📅 01:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460580">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/di4ixeGzX4-SDdNtjXBAdY3kBBxtJv5XPIYsNyMxQ7_BQ0aO8KvKAK3D2bkQPfSha57-mQ9iFM6OFXXjmBLPbAGYANw6-isftbAaJ-DL4leKyZiXA_KIW-fI09KaSnK1olE2SiDN-fEoBszo3LVRxcoBJaTmDr-akhvVgZ999iH3316mq9Rk5POvLdFRounCNn4wZwlHG5MxYOSpjHtZOVpjLe-zSmXI8kIcamk6F2L3rZzFkOxRa-AoKbHx26jcU_-x0ASMCw5FZW2ZPCnTsbjqXZq53Q1IaEHQXjGuhYIpiWFALwSA4bp-Yy4faXMNuEQ1HicMvywex8TfDCg1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROFQIpRPPeruoUwLV9zgjbWtmx6TdiearridvIxy486kInjMY8quM-1ZTey_xL9yWME7diMOfJhaBww43YZdf9KyJRmMmwQxe1nHsh0-AWbjJW_3NwhHbtGevmEWi6ScsGqX1giZEOerqb_fpG6lJ3e6inPeSqe_g6f2mlyCZNuwTpXt252zfOURnt3l_4pjdCwHeJEQ44AwxHnOc6HhqDnYBcuamNyVS2K9N5fpHaOSDnNvNae0FlVIBkmHuGsRS0_VnGIqA9f8kXHrCn9KnSwMcqEFlSet2BzNotqd42coTtaCDBiE9A3LDi65UuWmEVcNgyzZkkABnr9DUKz4Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9UKf9yhbOYUGdKOd5NIOYUpIMIaLJtk9RbAP8x4gEwtVGmjK6H6bgsWGZ9jQLY7zMZWlMOAnsYCBq-mp1-O68WzZwcIZUSO-ApzPcN7WZrq4ACXk4N99tmvb4xbh3UC6l1QDSwpf5EPLrH4UnieVv1eX0-oiANimPcvryvARDNhCqDRBst4yncgI00X3YuamTHfNwJU6AUllCgTiohhBfFPlFKAOs4SjEjrD-2TQ4xkf5ZyuGl1voPXxZ0ARDuGkAEEUROPCOI0QXrZSyWeGyRYymf6sCRDsrLAlAJoyP6muOYjXSDdw0ph_cBmYe5j45sVgHqR26aOOeDTBAvEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjzcLxA9TqEKoexB4HaO_-8P7cMyDan_lNPM2R6LVCGP_PzIlP3WL5cxl_ZyEQKUzxRzbakEJe-XzOBmM-BBVxqc4Uy_p-5ZtHZsyNNyF3UmOBQcPXZHV3dt231K44IePeUX7isP0FvoGWJ-ig4weBbcgC6QZl9oh8MKFiyqE0tI3PeAWVoxM49U8MKwbaTeFjt4Az4NHR98vDY8JFzZZ7kiA6V5IWLmuIqkngbR_LZUf8iR2Q-hU8HQ4ASuNJNSZ5tsdL1KIOj1NK7vc495umo7Kp-KHeXY2YNdzEgbXILAdiI_vYI0IRnuCMB7Z18OIQz5HqxmsgtDLtB4V26M6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWWhSo6GhoNNbTxqFphkqdkKYt6p1qwM1dfeKoLkPSl9ydfc9QnKZDasjWJJNVEMOxxZQGs5yG5ZcBINwsDfWsmnevYpeT0KzHNYDK4f_mbRwQdteccUiolhVvhl0KVhDRUjl0gw4-PLkEr315yeQ0sWvvEUF7Fg0JKfopW7jnt82AEuNKGa5jRGP7B8Z_V5NZT1vDAA-dVjWrNHNe4iIrxH15s_C3Mzndp73wheNfga8WmWQBGXCne7p5h18eWb_DuUDoMdmG9Obh667eWovOoIq6NEpBG1sr__5seT2niv0mROzs-1KL8B5L6F9v1NgVbG0BTOiAtupmKpTmcNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTf0cxIPje-5GfUSWfQo239jfnb0AP74QA8ZCvxC9z0Uk9cQR6Mf53FIqclpUE4uYGiLffIcD0OE0ImJH3H3jVQFEvFouqJVxbG-GJ9dPIDByBge_QN3MEqNxwP86il3WndBMZnPVWs94ta1I6hGzHn7ZaiOCVtt7un9aXdunpS27n3z-yqDMdAL8qFluvfFqvisZtUGhoccZh35CtuiJRWrzv87vC_W993cM70Onx2_Xg2cmnMsUWhO4fW050EYCzvslpMLwE6IFhK42y8FPQUpwhHgF1-y7JzHffTCkkaXPRAJ5_dLQOc6NC1dQu9d6cQUNV5rqLTQ2aj7a-oybQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱۶ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/460580" target="_blank">📅 01:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460570">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WibLpB6MSifJh97u4qRWfDThb44K6l0a3PZF78ikL9GnxtbvsbxEvLKBT-Uvm5Co2gbGFAcWIf802p77ifQuAZqmE61s6anpstfQUZnciAgajk1sAy63pL6kOIMDqQBozY2n6Rk5h0eY-EsXMn-yO5Z9x9PPJS8JXIecsWwuJvb8HPydXxgW3891RPOv0AHPEFtG6ZVsae-yRxPK3XUQYmcNwEDpKMtHpPEOV_Wd39AJS2TC4CPxamjp-colhpwcsboAqtjbVAxOr1Ehhc-YFUYGc2OpiCZBykBiceByKDlQYKaU0IGdsuykxNEkhSqGF4u0Ree5i8rDemVELBalTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSzdFv-mWJf3kVQQ6sxh8u6kvrGK3DY3yKSKLb0rn3m3w2StUPhBQqajKJ0HJX-tMeLZw80_1a-sGziaY7UaR0vBk7pfI6L2cbg76ZBWLkwI5MLbzJ-BjbNwFYnswpu9S3psL74a3s1zNJcWqEvQ2Q66lWxdDCXwDCGfUIzYUJOhqkGxTSjJcWis9eB7aFMyn3EbV6XtITw88YN2GnCBTpkUjYYKeMaNd7aFfsF8JHfirk9hnJHtBUENRIzy9590HRicN_LV_nGf3NR5_MN1M8dMF5bEwBTX8I-boW79KFst1RoAp8Peo5h44DVseFNe2I2WGCX9hh3eL_mbWxfPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B142DOhiZbvEUWFpOwOHKFaAcNIdrFEbVCndrhYrThTkFRmaUfydSVLyvEifEdWL5iCNn75HTDpVJ7SHX5-FztcQIEGT56nX_pLnA9bdUfuVWQ0iE58hyfgNj9fugbdHbxtUPcrFRMulHzozg3OvJM4LHl7aCiw7_wJvya-QqqnGAMkJQOh906nKmzJC0isfNzb7xjSwNueeEABsm1fK11Eq1LO7c-NNA-ftzMv4V-Ftsc0B9YFcm1YS3cuSmaRa-kKCURMaH74dpQBsEk9dzgDWtns3GBYFhFCYFaV43ZHJVXiEtFcCQdLl-cy2T2o9fhL-eZ8ArXh8lfWaSYU74A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkOAbb1eL09f_iFIawtMonCzfDiadUsitad5NZQknAyKnFMx7FjTngYgyuzpTLyzlDbnsnYzNTvEJyyE616i0moeNIxeZdXuumZUVMGclnBDLYbPKKb5D6Eythh8ZTnt_vGy246djsikWpRUOvImdb2YCCxd_aA08HUqgLExPd9cw8eNT-YpWEihp5D0hcVbmIlfpUK98J70-TIqEj8mtxOhALi_8jOFVRbzuK_aEZ-NRdd_7YxuEQ9lzt2dzMUMrAdLqlZniYLV48khhA4zAMjMKjG-l_unHrGTDtufJyJ0Buo3HAEHMuyf20Zpa2mCNCaAlLuE7xGwtFrYV-K4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWrpS35gqRBPFpZ87xLOoUC5XZmuukEGOCt_eY63FBZ_VEEk5hh6DtYGs_p_NziC0DeLlPC5AzLjnlBXKww8uzSWlVU0kfbWLGNXQFp2AfmGAzhFMPndR-x9-BaKEtr7fwbEDundF2Hin5N3qyvopjVpqgdYdQ5Sw_oB97muH5l2hk-uH-L9_1goGUm44z4zGhbCS60lAGdvTDxvFWydxGv8-IdggeYuRNwSV07o-J87IY1hhGl7hVEdiZqYOqF4PDWCboabgUkzjhkF-bTM_VKijbIsbl8jQZLvy2Tctpqg_QZpU0jhLGyE8p2c9xHY8NBoIhfX5X_XHGCdciAT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbLPQ6SVjLGHwiQJwfjl3XSJVKP2yhHyI-dBN6WYGaXvB4fN8sKLebDrIvuEjqMIfhEBYvrnevstm_p9iAbKzblyBZetsRcD5crgL_G3cRZtKybbmHs4RnRsdsKP4ZkdZLpfMzWLt8DziMP_iKaj-kby_VCXORW6auTvMQV5RG99gpyXfRa9ahUyX-YNN6VU7Ht0BfmmbnurDGH_RVdJXyAUvJK2Trs_Gv6YDt26UhBt0U0s81qsz4HeJHh71NokshnI6ln3-k-TJlahUHCstO8O3oOFQLckCpx0Pf_SSBMtwGnhwHGH1Ma3yG1HEQU4YJXcjwwz8S6ySu2_kMyx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSvM3DlrIhvUAa2rtjsvndwJzFO6WvI9W-uCu7s-J5ROC2FX40FrsbN5z-raTc91W83DeJze6RXQSLpEpWqNZNT-MnKcdoMo7Ieeu8TeyAR7t2sDEC24m7nQO7FGkQjtPyQ85ojGDflLkOuX0dv9oTM4h75PaHHHjUBa3CHH16Uwq51TY6MAq3gQJrWuhfFKQop-yPDScsnIJ5BsqrGPtB6V_royMB4OHr6Fz_-GBni2hotw2zthLUyxn9DqdTvKFrJssmXiDWTZFei6wUPMiINJq0ZaqazN6ljkEJdWj3g3tDso5WQvfUGoG53aPDQ0PAAZod5uJ_CzbkuErqSl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIBcvI-D0PwygkD1Hy10RVAoKqDqUikcEfb72tqckM_lf0zRGDCI5RlEHo3_5DQxNe6Kb8QGqYX4YSQOijlaiXa6tKyGl3ON--7rLv8CQMHn-aSGn6fHTjjzfj3ikeFe0U8eB656ut_PI8_EG5Z8kyTbf-yb0JqrpPqUxtpuNXMvx8EvPZpJfU6GIJe5Sxu01FfmaD2dkWdC0B2XTiA5Phb3sXt6oRLmx8plYnsqxiwJsfwR0FaeL2YkHZV1kr6Tq7BcLdVoKIXnRJ215Y0__0bz0_NN2klknhABZopD0whTXn9CoQgTA4CZG-AokXQ3gXtkzVz9zfesaP8FTOTooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0vo_et-2KUfAzlDZWCYzHAziW28PVQKFLFSvy0x9onpFgI4aRtUlG3clEr7tGMx_ltn6D18MpFYNy-Az9ugrTQbpSJ69mg87XPx3oVeJujrNQCeBrMhnXKQOOvgKs2NkpBJ1olSIL6ZM9SMC3nQCfww6gwoJFWvKWl2UJJwvh6XthDdgKr9Pqpf9OcgWFmxI5A7H441dbkx7SnJCiqM15HScZb3Kutc5HtpoZWXxgxEX1lbccO5D5M90I_Wf_DeEuDfcNKpUZmuRIJAeIO052UeRGNGdexIr4WkdFjbzJ3upDJ1LLwWpVBcRfOkqWvZykfIKkGEuoF0IiVodQoUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akPSPeJWgQ6yxVbDw1efjI-T_jwTa1l__GMivF62W3YRjSkpHnB2BMQHGxzxXvBkEoor7e9ZJrkq7wHnQch99SFBCNRa0LiKdlqKWSIn3sksCFu4etvhrz0YmpDvJHxAmeRIfHx74WKRNPrfIa7niDXFydNiqCCnrPyFSyqTnRtOC02bX7AdimXbHSbkN9JvD97pMfXD3B6n1WZhJNhYVof7KdcRvvvMmYN8z8j-Jn189qBOVYkvM1ovdr1Qg0fxC7J6ESNzz2VFxsZ__AMpGUccSLwIoeZGS4Cn8-E7qUkGVJBtbJgCfUnp0yrn2OD3EcIE0ysn8tBmkN-MxtvEnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460570" target="_blank">📅 00:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460569">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">زلزلۀ سیاسی در آلمان؛ پیروزی چشمگیر راست‌های افراطی در انتخابات ایالتی
🔹
برای اولین‌بار از زمان جنگ جهانی دوم و سقوط نازی‌ها، یک حزب راست‌گرای افراطی در انتخابات آلمان به یک پیروزی مهم دست یافت.
🔹
برآوردهای جدید حاکی از آن است، حزب راست افراطی آلترناتیو برای آلمان (AFD) با کسب ۴۴ درصد آرا همچنان با فاصلۀ زیاد در صدر قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460569" target="_blank">📅 00:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460568">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">در پی حملۀ هوایی اسرائیل به محلۀ الرمال واقع در غرب شهر غزه، تاکنون یک نفر شهید و چندین تن دیگر مجروح شدند.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460568" target="_blank">📅 00:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460567">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a393542d86.mp4?token=dG4r0SuNIJO_QMX1MHJZd6b3dZ3IAFFnJvA_gjnx7OgekvjdQk9Sz8TxRsn-erArLhDuQ5J2X5ITKk1ZLw_Byd9FvR4edBgTaRrpQ_Hj5RILrX6tHSkAlNnRjnztWkcffgIM1yGZ6eD0HqzxHeKkNp2jquumFHTmbjxXOl-8xUbvQEOArGy8VjBoSgIG8cRWB2H5-2iAxEGlnpTOWzHdhGQOMRTzkmPsuoft2dfXYg-4c72mHGkacO1xWb0XSny4KWbOAOZfItMMis9xNrAKpvlNIJX-iVzvIDWNHEpx1E4Z3SIFSolEBCmfQQsKfReiTc1-d3Gdq2vu4lUOZ9FD8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a393542d86.mp4?token=dG4r0SuNIJO_QMX1MHJZd6b3dZ3IAFFnJvA_gjnx7OgekvjdQk9Sz8TxRsn-erArLhDuQ5J2X5ITKk1ZLw_Byd9FvR4edBgTaRrpQ_Hj5RILrX6tHSkAlNnRjnztWkcffgIM1yGZ6eD0HqzxHeKkNp2jquumFHTmbjxXOl-8xUbvQEOArGy8VjBoSgIG8cRWB2H5-2iAxEGlnpTOWzHdhGQOMRTzkmPsuoft2dfXYg-4c72mHGkacO1xWb0XSny4KWbOAOZfItMMis9xNrAKpvlNIJX-iVzvIDWNHEpx1E4Z3SIFSolEBCmfQQsKfReiTc1-d3Gdq2vu4lUOZ9FD8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرایان در ۱۹۰مین شب، روایتگر تداوم حضور مردم شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460567" target="_blank">📅 00:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460566">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">در پی حملۀ هوایی اسرائیل به محلۀ الرمال واقع در غرب شهر غزه، تاکنون یک نفر شهید و چندین تن دیگر مجروح شدند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/460566" target="_blank">📅 00:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460565">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80db7c1466.mp4?token=jpEuxJdntwjHP7Cbxn26k-PVjJYL-Y10lwaa0eB6d1jaY2o2oN6TCg7tgyIt3L6pFpm5zbJaEY6zWLYnDvxkNcKDJZJ1rE6GCuNvh9oGTLJaNdL_AgN1THsp4Krjn4oOAGSWvj5KiLKxy6KBYugKAiL5NdUAUtgX-dI1UhzGITanchExBFxBNYolE7zxaoMLZEWGiiCz3UpU4F58iIGfjORQL8BeJbaxBWS3vCRAVCJzp9gTJUpI_ROxiqMDA1hM1OmbJxzsEjSO7XsFdlDJYdIQSsjZPf9BTZ83LInqC4tn_yPtSN6fFjReQQFyiVlfQD3Z5JYujgy_4BUjWOYKHGI3xBTRTYi5BL33S_bj6oDZ7ln3ZL0VXEhLSGc9Jmo_DdlOw4UO8AR1fC60jV5KvNftbsYZy82--XKN9x0sfH9DJkyK6kwByDhVmZxtDm1nSJM1S9-kshabTLgqVhgq8CyMkk-gyrnUKVXY8DEfeDZ_0ctlwRPXBDQvOocAeMRv-ouC8t3QBnJHwaqyhWAAfKxXQZzf19Bq2VgI4iByifA5rfIdRbc3VLOOwtxqGPvhylY_64q8VXuyKSj60KNejrFYC1bnSDPvYaTFVPWhprIHfTfKWMgplo1h4z_zjiqeNNsRWu4tDkdcKFnjdQ-_DhpdqIJL-txWaZKO7hUjPaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80db7c1466.mp4?token=jpEuxJdntwjHP7Cbxn26k-PVjJYL-Y10lwaa0eB6d1jaY2o2oN6TCg7tgyIt3L6pFpm5zbJaEY6zWLYnDvxkNcKDJZJ1rE6GCuNvh9oGTLJaNdL_AgN1THsp4Krjn4oOAGSWvj5KiLKxy6KBYugKAiL5NdUAUtgX-dI1UhzGITanchExBFxBNYolE7zxaoMLZEWGiiCz3UpU4F58iIGfjORQL8BeJbaxBWS3vCRAVCJzp9gTJUpI_ROxiqMDA1hM1OmbJxzsEjSO7XsFdlDJYdIQSsjZPf9BTZ83LInqC4tn_yPtSN6fFjReQQFyiVlfQD3Z5JYujgy_4BUjWOYKHGI3xBTRTYi5BL33S_bj6oDZ7ln3ZL0VXEhLSGc9Jmo_DdlOw4UO8AR1fC60jV5KvNftbsYZy82--XKN9x0sfH9DJkyK6kwByDhVmZxtDm1nSJM1S9-kshabTLgqVhgq8CyMkk-gyrnUKVXY8DEfeDZ_0ctlwRPXBDQvOocAeMRv-ouC8t3QBnJHwaqyhWAAfKxXQZzf19Bq2VgI4iByifA5rfIdRbc3VLOOwtxqGPvhylY_64q8VXuyKSj60KNejrFYC1bnSDPvYaTFVPWhprIHfTfKWMgplo1h4z_zjiqeNNsRWu4tDkdcKFnjdQ-_DhpdqIJL-txWaZKO7hUjPaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شهید سلامی از دستیابی به تکنولوژی انهدام ناوهای هواپیمابر
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460565" target="_blank">📅 00:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460564">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9012d9a6.mp4?token=YUYCuBZvmCFntdUx0dSKYO0i_Vj8lL5VBllohJO8nS1rTTj57c-4pezTb5zF4LZZCu4XcZmiPJZv4Jys8oQQU0FxuO00aFRtr_KHNRGe5olYVYsjF6rxU9DTEx07K5xfEOL22naLL6319TrUtxXNlkrPTRjXQ9l8OS3_JH0FZwazqI2yDyfouxBz-Mt_pbZbdeG6aF07Z4nb6H8Vbx0F8vyc2qN9DymycuHhacyWEM5O2GPAPkE9kgSd8bkk4oiknpDVPi5GiMSbYrELQPcwfTBxY0oWo4RAy7-aVo8Dm6j36XJ-yIJ-QR_W7NHMATeQedcvEdV2f0dJ4f4UZLsjlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9012d9a6.mp4?token=YUYCuBZvmCFntdUx0dSKYO0i_Vj8lL5VBllohJO8nS1rTTj57c-4pezTb5zF4LZZCu4XcZmiPJZv4Jys8oQQU0FxuO00aFRtr_KHNRGe5olYVYsjF6rxU9DTEx07K5xfEOL22naLL6319TrUtxXNlkrPTRjXQ9l8OS3_JH0FZwazqI2yDyfouxBz-Mt_pbZbdeG6aF07Z4nb6H8Vbx0F8vyc2qN9DymycuHhacyWEM5O2GPAPkE9kgSd8bkk4oiknpDVPi5GiMSbYrELQPcwfTBxY0oWo4RAy7-aVo8Dm6j36XJ-yIJ-QR_W7NHMATeQedcvEdV2f0dJ4f4UZLsjlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا و یک رسوایی دیگر؛ تسلیحات کمپانی ریتون در حمله به عروسی سیریک  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460564" target="_blank">📅 00:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460563">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تیراندازی در آمریکا، این‌بار پس‌ از مسابقات دانشگاهی
🔹
در پی تیراندازی جمعی در ایالت کالیفرنیای آمریکا روز یکشنبه دست‌کم ۳ زن هدف گلوله قرار گرفته‌اند.
🔹
پلیس محلی اعلام کرد که در تیراندازی صبح زود در ساکرامنتو پس از یک بازی فوتبال آمریکاییِ دانشگاهی، چهار نفر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/460563" target="_blank">📅 00:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460562">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193a0b1649.mp4?token=o2okKgC6khaIyRHhrEGvsfpbuh-q3RBxJWjd8HVkl7IQA44S9z6xxaa6RweazehPI0B3y8HbJ4Ze91idHaKe7aIXwE1PbgX8T7dV09CBa30TIFnIZ-1m3Si4ilnk9XukEuhbgLSB1uKOLQ4ZDQpN0y6Urqh-_YHnePJwhR-IyuG_Jr2Tj_qFc8U3425FrnSP9bCF56VD-CZZIzfk7UQFDEi6sfcNU6OovUZ9ze-jzsTLyDG_Sf2YU4LERzHcfCP7CEfZepLrlOMiUg6icV8JSUhB4WweHrKNL-QbdvQLVGsQ5xDVuG4s9b0bfWBEh-FD1dUe4W3WIAJ-frdJ-A8v-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193a0b1649.mp4?token=o2okKgC6khaIyRHhrEGvsfpbuh-q3RBxJWjd8HVkl7IQA44S9z6xxaa6RweazehPI0B3y8HbJ4Ze91idHaKe7aIXwE1PbgX8T7dV09CBa30TIFnIZ-1m3Si4ilnk9XukEuhbgLSB1uKOLQ4ZDQpN0y6Urqh-_YHnePJwhR-IyuG_Jr2Tj_qFc8U3425FrnSP9bCF56VD-CZZIzfk7UQFDEi6sfcNU6OovUZ9ze-jzsTLyDG_Sf2YU4LERzHcfCP7CEfZepLrlOMiUg6icV8JSUhB4WweHrKNL-QbdvQLVGsQ5xDVuG4s9b0bfWBEh-FD1dUe4W3WIAJ-frdJ-A8v-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین مدل اپن‌ای‌آی یک بدن انسان ۳بعدی ساخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460562" target="_blank">📅 23:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460561">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f79baf2e1a.mp4?token=jgXNqx2hE7jlAZZuk0uFrg6yly4PbZs6ye2LDe0xBt-if2KG59RX6H5FX90wvZlU-26WRp4vUBBR8VgQQ8xGZala7Ok5feGgsulVorCOqdX7p9i3USaTnMv72zHHuBo5ulcyhJHyFhsHhm96LhEVn37WPibwv0MohJ3PY6ZgYt8oHiDKct3cm1gXqSJR00RUyV2J1JL0pAErCLFKVvOzfoMbz0-dHDQ7-AjfaPwuudZIPFifxaQyDeIXCqGwOJ9CLf36fxTo4Q7tjchwYkyUxfE2vApA0_S2w6A0mc5Jz7HrSdqX8y4IvmJEylPO1FtZY65EWRyr_HjGrBPAj_MvEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f79baf2e1a.mp4?token=jgXNqx2hE7jlAZZuk0uFrg6yly4PbZs6ye2LDe0xBt-if2KG59RX6H5FX90wvZlU-26WRp4vUBBR8VgQQ8xGZala7Ok5feGgsulVorCOqdX7p9i3USaTnMv72zHHuBo5ulcyhJHyFhsHhm96LhEVn37WPibwv0MohJ3PY6ZgYt8oHiDKct3cm1gXqSJR00RUyV2J1JL0pAErCLFKVvOzfoMbz0-dHDQ7-AjfaPwuudZIPFifxaQyDeIXCqGwOJ9CLf36fxTo4Q7tjchwYkyUxfE2vApA0_S2w6A0mc5Jz7HrSdqX8y4IvmJEylPO1FtZY65EWRyr_HjGrBPAj_MvEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم گردانی مهران رجبی در تجمعات شهر قم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460561" target="_blank">📅 23:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460560">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1a55c75f.mp4?token=teLAKo8vrLmWsz4QMLOU2OHbEKDqoI0qiXgLjDrso9ITZ5dEUpZnQ5ovcOzpBuaKXY7EI1Qmug8CUC28v1OupOUUZ7Lc4m5t8fxeIEVz3UHjkQPL1gpqCKQCauMFFjMjWWV6_NMgNavO9-se2jX3slcjIL2kALR__XizIwQC-PgGinuDAAV7NCwxIiUj3iJEiOpFxU3MiIP_kUbGLaLHWYTo-X0-vUr-eySKUyeY_Ip6dOZeQcn4I68ug6msOGc0M9R3HGOCX2-fpX153MG2ooDcUNDwdNJk7EJiHAVrkh5ijmXpV3LCk4u_0SUuvrhb9x0s3QBcndnKLdRbnYzhvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1a55c75f.mp4?token=teLAKo8vrLmWsz4QMLOU2OHbEKDqoI0qiXgLjDrso9ITZ5dEUpZnQ5ovcOzpBuaKXY7EI1Qmug8CUC28v1OupOUUZ7Lc4m5t8fxeIEVz3UHjkQPL1gpqCKQCauMFFjMjWWV6_NMgNavO9-se2jX3slcjIL2kALR__XizIwQC-PgGinuDAAV7NCwxIiUj3iJEiOpFxU3MiIP_kUbGLaLHWYTo-X0-vUr-eySKUyeY_Ip6dOZeQcn4I68ug6msOGc0M9R3HGOCX2-fpX153MG2ooDcUNDwdNJk7EJiHAVrkh5ijmXpV3LCk4u_0SUuvrhb9x0s3QBcndnKLdRbnYzhvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام خلج در برنامۀ سمت خدا: تفکر فرعونی، قدرت و تجهیزات را عامل پیروزی می‌داند
🔹
همان تفکری که امروز در آمریکا و رژیم صهیونیستی دیده می‌شود.
🔹
قرآن پیروزی را از آنِ اهل ایمان و تقوا می‌داند، نه صاحبان قدرت و ثروت.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460560" target="_blank">📅 23:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460559">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5362dd7c43.mp4?token=bAZHEtSFgKKCDDtQOo0PzFYlzLzew--xuImLDA38uyV4cR0nZh-eZYQrHnjfFCW3kmANRs1H9D1wXExdx8JV79eX66LNEimXSoe3kUkes0Vm_ZcdjoT8ZrvmHtGCWd7n2ltMZkV_OX1bgGhgk2pfPrM-WdWbQEXdwaC9c4MxAKUDCrf6-RoL4KdQ7v6tioth44QSp0IKSukdXu1fULT9GA7o6jubkyfqw-GnSgTUeJRPz1aYGT4dQPLzqXOQ5Bxk-IO13ivq0tOhn-6q9dxjWcA3CHQgEKI_mFlpweohWrRZSkiJ88PWQqE0UMwvByv8v3vhxpImZ077ljKfQP6dAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5362dd7c43.mp4?token=bAZHEtSFgKKCDDtQOo0PzFYlzLzew--xuImLDA38uyV4cR0nZh-eZYQrHnjfFCW3kmANRs1H9D1wXExdx8JV79eX66LNEimXSoe3kUkes0Vm_ZcdjoT8ZrvmHtGCWd7n2ltMZkV_OX1bgGhgk2pfPrM-WdWbQEXdwaC9c4MxAKUDCrf6-RoL4KdQ7v6tioth44QSp0IKSukdXu1fULT9GA7o6jubkyfqw-GnSgTUeJRPz1aYGT4dQPLzqXOQ5Bxk-IO13ivq0tOhn-6q9dxjWcA3CHQgEKI_mFlpweohWrRZSkiJ88PWQqE0UMwvByv8v3vhxpImZ077ljKfQP6dAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا این فناوری را از ترس ایران خاموش کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460559" target="_blank">📅 23:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460558">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
لحظۀ انهدام جلسۀ فرماندهی مزدوران وابسته به سعودی توسط موشک بالستیک یمنی  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460558" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460557">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb6cdf6f4.mp4?token=gsx7_TSW79RK5ZsEWhMqZwk-4z2pGX2hL23TfQa0bmH-7p9fawAVWvjsPJTNhHFTJ_fFZgumvEcv5afi6eCEx-wnkdiZ3GeGEiVmQjzFC2wn5RD7toE-HPGQ60QAgssRfuCKk67sowoJa3_iMFvlF-Btzl3dRJcemROh-aBgs1hgSBbwc4icoOvsC2FlszoeSl-VgP6Ro6lLm_Od0DK_1x6mU7HiId9N2gVngI2TectBdpPp49hU9hJfpgIsqrUM7LTGLNgfiX-nv3bbTKl2Ly_xAqSF_PIt36YLBtegP6F8DzlCgnxP5-Fqi2A9rNMVXJ2f3jirKOyZDN7A2NR6mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb6cdf6f4.mp4?token=gsx7_TSW79RK5ZsEWhMqZwk-4z2pGX2hL23TfQa0bmH-7p9fawAVWvjsPJTNhHFTJ_fFZgumvEcv5afi6eCEx-wnkdiZ3GeGEiVmQjzFC2wn5RD7toE-HPGQ60QAgssRfuCKk67sowoJa3_iMFvlF-Btzl3dRJcemROh-aBgs1hgSBbwc4icoOvsC2FlszoeSl-VgP6Ro6lLm_Od0DK_1x6mU7HiId9N2gVngI2TectBdpPp49hU9hJfpgIsqrUM7LTGLNgfiX-nv3bbTKl2Ly_xAqSF_PIt36YLBtegP6F8DzlCgnxP5-Fqi2A9rNMVXJ2f3jirKOyZDN7A2NR6mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: در بنزین ما متانول نیست
🔹
در دنیا استفاده از متاننول در بنزین گسترده است و تا ۳ درصد هم استاندارد است اما ما استفاده نمی‌کنیم.
🔹
تنها در یکی از پالایشگاه‌ها به‌صورت آزمایشی از ۰.۵ درصد متانول استفاده شده بود. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460557" target="_blank">📅 23:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460556">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/he1-b2UmHLkXOLK0MqE1hGIVRoCJNq-tApMywGbcw62-0AYFA3eE0F-TenLbIO_MEH_h_WHRqzXhQF6ennRqKfbK1OWSfTuiAFhzKgFF2R5By0OItTbGdgtKikB6D-Zy9h4nqrbcauejt-bV9qgrwVAifzz-GVkRT3pp-Du-kuRFrSUYluOuM1ZT9myUF6PbNEsksKIr3ZzM6LDLkaS5KkHVT75Jzit9wGBad2nf-Dw7bXPc0BffFn799I1Hsf2DnRP-N8dB1HLreddplpBLozPpqU7Oo17BaQsEgEduC1gvubbQtqVhugUpgJbRzbw90Rih3l-cG1lvXAB_tsqZeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ شهید طی درگیری با اشرار در کورین زاهدان
🔹
یک منبع آگاه در زاهدان: در جریان درگیری امروز با اشرار مسلح در کورین از توابع زاهدان ۲ بسیجی به نام‌های کیوان رامرودی و ابوالفضل عودی به شهادت رسیدند.
📝
اخبار تکمیلی متعاقبا اعلام میگردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460556" target="_blank">📅 23:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460554">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/686281167c.mp4?token=ANfpr_kvuIr1TYDLOKFUn3TlfWGCdN9T5Y4PsmS2X7694trV_NMKBN0_MjUEj1A-J_kFI2qY48UqR6Gx_Tj2-MJKULpkH2Pn-1xoCHsVb9dBOOl0HMXYdfDXnHLugurZyINfmeElbBN5Nyu3OBQoVLxofLeZKA2ai__u5LOfmlcMr8bKoSbhOcWNndtS50jqL4ZghGrft8X70c8R_XuRbWEcqCo-ry4Z2YjEtukyrCy5jmM2uvfL9VZ1F74Ndt9EEE7xOONm42smv0ZDO3lUy_on8kSq45w15lYrYD0xW-rh9F-O6kpN1VJUIxU2Rzpf5f2hYglp53OoG2dylHiM9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/686281167c.mp4?token=ANfpr_kvuIr1TYDLOKFUn3TlfWGCdN9T5Y4PsmS2X7694trV_NMKBN0_MjUEj1A-J_kFI2qY48UqR6Gx_Tj2-MJKULpkH2Pn-1xoCHsVb9dBOOl0HMXYdfDXnHLugurZyINfmeElbBN5Nyu3OBQoVLxofLeZKA2ai__u5LOfmlcMr8bKoSbhOcWNndtS50jqL4ZghGrft8X70c8R_XuRbWEcqCo-ry4Z2YjEtukyrCy5jmM2uvfL9VZ1F74Ndt9EEE7xOONm42smv0ZDO3lUy_on8kSq45w15lYrYD0xW-rh9F-O6kpN1VJUIxU2Rzpf5f2hYglp53OoG2dylHiM9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: کارت آزاد جایگاه شناسه‌دار می‌شود
🔹
در این طرح که در آینده اجرا خواهد شد هر نفر که با کارت جایگاه بنزین بزند با کارت بانکی احراز هویت می‌شود.
🔹
این طرح به‌صورت آزمایشی در چند جایگاه تهران درحال اجراست و احتمالا تا اواخر مهر در تمام کشور اجرا…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460554" target="_blank">📅 23:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460553">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02b05b065.mp4?token=PAib0dHBZ2j_yjx_X9hAt-SIt59BPLi2rKa3l1ulFtelkPk7MYTcRiifGy3Iqt6XV_k3mvrfN-JKEYX_8JpyIBxqsdvgh8pCsE_YZZNes37g9NNEqATSHHuHqrA5Tt2ca3RZyulU5lnGXN0SbcuFgbaojbYZyBY5eZGNuLiD8tcVGALUMrqTLT66Swh84hnc46v1O6kae5UUM-8j6KJkS1mphqI94CZTXU6FWve4hwdHbic64Qx3HpDVVk0IC2R0VvftduGc0U3aj7_3hVtCo-17j-7sZ6e5XSOf1Hzp8bhG5QqfkYolZwShkD4yhwZqGDXExDkSorYRudLCYDkyDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02b05b065.mp4?token=PAib0dHBZ2j_yjx_X9hAt-SIt59BPLi2rKa3l1ulFtelkPk7MYTcRiifGy3Iqt6XV_k3mvrfN-JKEYX_8JpyIBxqsdvgh8pCsE_YZZNes37g9NNEqATSHHuHqrA5Tt2ca3RZyulU5lnGXN0SbcuFgbaojbYZyBY5eZGNuLiD8tcVGALUMrqTLT66Swh84hnc46v1O6kae5UUM-8j6KJkS1mphqI94CZTXU6FWve4hwdHbic64Qx3HpDVVk0IC2R0VvftduGc0U3aj7_3hVtCo-17j-7sZ6e5XSOf1Hzp8bhG5QqfkYolZwShkD4yhwZqGDXExDkSorYRudLCYDkyDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سانحهٔ هوایی در آمریکا؛ ستون عظیم دود در آسمان میامی
🔹
پلیس و واحدهای آتش‌نشانی میامی پس از سقوط یک هواپیمای ۷۶۷ پرایم ایر در فرودگاه بین‌المللی میامی به منطقه اعزام شده‌اند.
🔹
گزارش‌ها حاکی از آن است که این هواپیمای باری امروز بعدازظهر به وقت محلی از باند فرودگاه بین‌المللی میامی (MIA) خارج شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460553" target="_blank">📅 23:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460552">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed1c55e0c.mp4?token=bG_Nbc8LjkYCg3oR0flLCDJONTacA6BRZI0KSN8CCXXccsMBULTMMeSGnm-PK1oxdF63JyoujFJ6YnJwIfhpjHSKE0w6npnmOabSo1hePOoWQ4oBrH_6G57PK_DZIoEznZlRUobfrlNpa7U6Vmf5G2DjtZ9kvHQmgdwEVfU9A6uAXB_1iRq4MzL00IU1sXGLUY1AQ9clzbvaEVe9XNTySWU85k7E0i2-sMnSRJS3F3RLasKeR20InN8OlmDu3SKR0aPNFCw-NcPcKghUkUZFjAQ0r0ERmSNzW7tnuxRMesDSeWCZWHIOULwDbOciLsXJHaqfTSbUFw1ED46W_TF53A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed1c55e0c.mp4?token=bG_Nbc8LjkYCg3oR0flLCDJONTacA6BRZI0KSN8CCXXccsMBULTMMeSGnm-PK1oxdF63JyoujFJ6YnJwIfhpjHSKE0w6npnmOabSo1hePOoWQ4oBrH_6G57PK_DZIoEznZlRUobfrlNpa7U6Vmf5G2DjtZ9kvHQmgdwEVfU9A6uAXB_1iRq4MzL00IU1sXGLUY1AQ9clzbvaEVe9XNTySWU85k7E0i2-sMnSRJS3F3RLasKeR20InN8OlmDu3SKR0aPNFCw-NcPcKghUkUZFjAQ0r0ERmSNzW7tnuxRMesDSeWCZWHIOULwDbOciLsXJHaqfTSbUFw1ED46W_TF53A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: با جمع‌آوری کارت‌های جایگاه در کرمان مصرف سوخت‌های جایگزین مثل سی‌ان‌جی ۳۰ درصد افزایش پیدا کرد  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460552" target="_blank">📅 23:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460551">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af729e4ee.mp4?token=dCOz_PCmOBiXPXwcUvgH5cTtJWVOAT5hbVhPQelMJs53vm5f9IwZ0TtiSHeDlVhkXapuIHEydQIXIIvOjIORrxkYhxuC1MVKunJRd2i7Bg_Z1gInEFjwQkhWAYJt3b_NDaGwie8_xQVX2V4Buz9p4Q1v-JDABgXg8gCWyIg-s6-rRLFENakSz1LNv3FlKRIiLy5q_uFaOARuMVLVwlMjjMGRwwUYBBx5XkfKzsURDpiLKtN-O5tGDn0FQdcEQK7J6B_m7KKpYyadwFWWr9guNSyw9i9_8kNh7QgGtbB4TQlYw1zbq_A1OVfqL0ECexdVlcJ5PwgrIHHdURuC0veDCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af729e4ee.mp4?token=dCOz_PCmOBiXPXwcUvgH5cTtJWVOAT5hbVhPQelMJs53vm5f9IwZ0TtiSHeDlVhkXapuIHEydQIXIIvOjIORrxkYhxuC1MVKunJRd2i7Bg_Z1gInEFjwQkhWAYJt3b_NDaGwie8_xQVX2V4Buz9p4Q1v-JDABgXg8gCWyIg-s6-rRLFENakSz1LNv3FlKRIiLy5q_uFaOARuMVLVwlMjjMGRwwUYBBx5XkfKzsURDpiLKtN-O5tGDn0FQdcEQK7J6B_m7KKpYyadwFWWr9guNSyw9i9_8kNh7QgGtbB4TQlYw1zbq_A1OVfqL0ECexdVlcJ5PwgrIHHdURuC0veDCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: قرار است یک روز در هفته مدیران دولتی ملزم به استفاده‌نکردن از خودرو بشوند  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460551" target="_blank">📅 23:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460550">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/407cfd0892.mp4?token=uWQ8e0k9pUGM1AntTlT1W_j7t7N09nLzYUU_UHwEWGF9_vi1wQNTGGTwf9Th7jbvFc9Ovn0jQe5ewvLrBOZHU9loqade88j123V3tkXmwGpaGXARnrp79tf8277eHHLHv-rdbSGM6n3Bs9WuXrI8Yp4eg2CvFYn_-MJxl6zWTt4TTlVG-CxuHiVzZATsB0Cm2HMJn4Ltmzm45ql2Ov4-Y1kA-HBDmyJ4-kWpOpCWhjO1MQjsV4oqagHV_nbfUWTXzxBdlIbb5wo6U2TZ9FjxCttCFq285ehFGqiDAslRBv3accC32JN9xb4NQFV0i61BYZzxId52bVN42bitvtcbCVnR-hbvKdyRjbfWPrc9OSu3JebJAh89kFL3PZ0oCVTIxTVq-8yMaLrsQla0xdPixSm7huIQyECXMEes9X2HxFr0-Q0YGWCJOVQRVgJLQcJN9Jk-0ugyICBITbc7r4bPvCqUsrjipc0Z9TsX1XjuNe7AdzR-ko-bILsoPzVBjoFuuLV-soISOqwfT5froEUF7i635qLKcCqJjIHJu-r7Ya0SpjPHSJ7thSP4X8irdCHkCsKiYZDggM3N-hLmRJv_OfOMVmv-qO2xDOHAnCQPzFN_wgyZwRIPlig7Vf3jK2QNzLN48duxVmYy0eVUlWz0uMQ8GCuGwoQKGoNmd4ptWec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/407cfd0892.mp4?token=uWQ8e0k9pUGM1AntTlT1W_j7t7N09nLzYUU_UHwEWGF9_vi1wQNTGGTwf9Th7jbvFc9Ovn0jQe5ewvLrBOZHU9loqade88j123V3tkXmwGpaGXARnrp79tf8277eHHLHv-rdbSGM6n3Bs9WuXrI8Yp4eg2CvFYn_-MJxl6zWTt4TTlVG-CxuHiVzZATsB0Cm2HMJn4Ltmzm45ql2Ov4-Y1kA-HBDmyJ4-kWpOpCWhjO1MQjsV4oqagHV_nbfUWTXzxBdlIbb5wo6U2TZ9FjxCttCFq285ehFGqiDAslRBv3accC32JN9xb4NQFV0i61BYZzxId52bVN42bitvtcbCVnR-hbvKdyRjbfWPrc9OSu3JebJAh89kFL3PZ0oCVTIxTVq-8yMaLrsQla0xdPixSm7huIQyECXMEes9X2HxFr0-Q0YGWCJOVQRVgJLQcJN9Jk-0ugyICBITbc7r4bPvCqUsrjipc0Z9TsX1XjuNe7AdzR-ko-bILsoPzVBjoFuuLV-soISOqwfT5froEUF7i635qLKcCqJjIHJu-r7Ya0SpjPHSJ7thSP4X8irdCHkCsKiYZDggM3N-hLmRJv_OfOMVmv-qO2xDOHAnCQPzFN_wgyZwRIPlig7Vf3jK2QNzLN48duxVmYy0eVUlWz0uMQ8GCuGwoQKGoNmd4ptWec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: تاکسی‌های اینترنتی از تبعات افزایش نرخ بنزین مصون می‌مانند
🔸
قرار است با دوگانه‌سوز کردن ناوگان و اختصاص سهمیه مازاد مبتنی بر پیمایش، از افزایش هزینه و کرایهٔ تاکسی‌های اینترنتی جلوگیری شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460550" target="_blank">📅 23:10 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
