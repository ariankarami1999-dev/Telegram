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
<img src="https://cdn4.telesco.pe/file/aidFB_ZS6yhMg2eyIZOMaGzXfHZO9HDUozMt6CPPXl729x1SCpyn2IKRUGBuABDSjFvKD0fMa3zqttRcCHRMcoaXi3aElRdSBtQMaG8zuICmIivHQWTWshOEDk56VeTmJC-MqMYn9Y_JvvvYuO-b1t0n_i6RroUbWj9DhTgw8ExP65PPJv7TAZuYR2Es00_NzSbtf_YMp5c1Ozf7oE3_LW5GfHHc5l-fFule9MCWYi3Foey7Lh6eA_tcS-c9TIH-bajCTVliubtRDH7Sy9pSUajIdCM49ttV1DUXX6jR9ST7eoO7JsII5XvQKEsLTXtW6LKxAAKvqy_EnIlz_sbV0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 15:50:14</div>
<hr>

<div class="tg-post" id="msg-457530">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d03d1ff8e.mp4?token=IapewhYObD5Cz-TNzj7rNkS3LCzBcaezEbF5_8nwEtZ_Oy6JWWq2QuYpzSUi3ScX55JUBml9YvszNU5HPRUZCD1-wDQWxtn8dvt_u_wnC9n1Gfwv8dnsoj28meaQJhK3eNkv9s2FWaX53V7iWdKM2BKrYPJQ6oQo85frpmJVw2IKC8cLy53eCqtM0YMzU70w4JCKbuPXURh91chPCrOMrOQaqUgVrueZxAoiwzHng-P5VExMUQac_yD_uRb-GpcP2W8HysrgZSn-U6te-hUJQ74nivScQIgJuZQDNCQnA2dRTtDsUxO6yJMadeoV04Y4hJoP-3vhrUHocmrNJHj7CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d03d1ff8e.mp4?token=IapewhYObD5Cz-TNzj7rNkS3LCzBcaezEbF5_8nwEtZ_Oy6JWWq2QuYpzSUi3ScX55JUBml9YvszNU5HPRUZCD1-wDQWxtn8dvt_u_wnC9n1Gfwv8dnsoj28meaQJhK3eNkv9s2FWaX53V7iWdKM2BKrYPJQ6oQo85frpmJVw2IKC8cLy53eCqtM0YMzU70w4JCKbuPXURh91chPCrOMrOQaqUgVrueZxAoiwzHng-P5VExMUQac_yD_uRb-GpcP2W8HysrgZSn-U6te-hUJQ74nivScQIgJuZQDNCQnA2dRTtDsUxO6yJMadeoV04Y4hJoP-3vhrUHocmrNJHj7CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراض فعال نیوزیلندی به حمایت این کشور از رژیم صهیونیستی
🔹
یک فعال حامی فلسطین پنجشنبه در جریان نشست عمومی نخست‌وزیر نیوزیلند، در شهر کرایست‌چرچ، به حمایت این کشور از رژیم صهیونیستی اعتراض کرد.
🔹
این معترض خطاب به لاکسون گفت: «شما از نسل‌کشی در غزه حمایت می‌کنید. باید اسرائیل را تحریم می‌کردید، اما در عوض از آن حمایت کردید. آن‌ها ۲۰ هزار کودک را کشتند و شما به اسرائیل پول دادید. آنها کودکان غزه را گرسنگی دادند و شما به اسرائیل پول دادید. شما باعث بی‌آبرویی نیوزیلند شده‌اید».
🔹
او در ادامه گفت: «اگر این اتفاق در دهه ۱۹۴۰ رخ داده بود، شما از نازی‌ها حمایت می‌کردید. شما مایه ننگ هستید. شما جنایتکار هستید، شما از اسرائیل حمایت می‌کنید.»
🔹
به‌گزارش روزنامه «نیوزیلند هرالد» نیروهای امنیتی سپس این معترض را از محل جلسه اخراج کردند. این جلسه که در راستای فعالیت‌های انتخاباتی لاکسون پیش از انتخابات ماه نوامبر برگزار شده بود، با اعتراض‌های مکرر چندین فعال دیگر با محورهای مختلف از جمله جنگ غزه هم مواجه شد.
@Farsna</div>
<div class="tg-footer">👁️ 684 · <a href="https://t.me/farsna/457530" target="_blank">📅 15:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457529">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDn0W9BVRARXObh_hf1dxhJgrVh4eLK--og5SrkRAyfg3w6JZHRjO1N6UWtgMYyA_2NXlg2JHpiGCRrgnepUAgS-a5tup4whJSKeRG0sQXZFHX9Z8xgxtQgMfhQrxQ6ZeqQBSidcBkbSCO7jd5McB0YoQNl5Fzfy2D_-YzwWAvXkNkQy9T2105hSZcd39hIzLcAj3yiSdYN0h88RjZNjGL156EL-CUM10xBnOzztSn1kJUgBvYlKfVfYr4e5bSQLzfG-l_WRuhUbLuyenbAoHTdK7BPOPmLhFnqmAIElBk-H9FYg6jFm1-2uqNUL8YGtkm2l4sCK9X_zYpc22UBHow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
مهدی طارمی با عقد قراردادی به الوصل امارات پیوست.
@Sportfars</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/farsna/457529" target="_blank">📅 15:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457528">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3f4182b4.mp4?token=vxV7bbvwZgajEYVbnLyZsCbtNJkjSeN-xjnDkH_fi4C9fadYumqXX_OU-Q1Wnqmd7L5hBYiQJdkLi5f8f5RMrV6kydbnA1qQV1skZYsU2VCbG_YLQx_Y06pHWobKeu182xwkEAtl9ehfQK43eXrojsI4BSZ1r2IwxCNW4K1PPtUmoZrHGTztk0QA6omZj0EsmANC30261tvMJBJLV-3G_Sb9slqRczKObkL6NPCX346Q76PwPZrOoF68DWlWxxXFKGzCZnEcLJ1_jVumHQiy-mGQrS2DgA7nNcFCt2Y7zYuTVCmyqNt9iHuTy036AtNdSpLvutGhsx0kJA9XEXte8rB2rsNw_4yRs3CO6i1vyXXawF4juQlCz10ZhXzZMA2Ear_azS2gyFYVcVZZrkfI4zyGcNmq06A6B9JL7n2-pKZuMsDnLehad0x97Zi9hzmWvjDOY76NXxNvkIHDwqanomRlcy4Di4JL2fzZ0D6kDvncWG2Lq8tQlhIyHFSSGLn3qQQEhaeTeM4kOLN98at00AckdvtBjRoliPQ-ed-eA8CIVtcQr8_5NK_DN52YtUBn9NbuxM3-zFoB__lpLErjDN_aFgM4o8Wl45UX0vfAaPYEyCS0e77fqk8On8wp_9w9gitqlBEfC5ZlWK3Rv0gwmDb8zwmf-tpimZdJsr2VDXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3f4182b4.mp4?token=vxV7bbvwZgajEYVbnLyZsCbtNJkjSeN-xjnDkH_fi4C9fadYumqXX_OU-Q1Wnqmd7L5hBYiQJdkLi5f8f5RMrV6kydbnA1qQV1skZYsU2VCbG_YLQx_Y06pHWobKeu182xwkEAtl9ehfQK43eXrojsI4BSZ1r2IwxCNW4K1PPtUmoZrHGTztk0QA6omZj0EsmANC30261tvMJBJLV-3G_Sb9slqRczKObkL6NPCX346Q76PwPZrOoF68DWlWxxXFKGzCZnEcLJ1_jVumHQiy-mGQrS2DgA7nNcFCt2Y7zYuTVCmyqNt9iHuTy036AtNdSpLvutGhsx0kJA9XEXte8rB2rsNw_4yRs3CO6i1vyXXawF4juQlCz10ZhXzZMA2Ear_azS2gyFYVcVZZrkfI4zyGcNmq06A6B9JL7n2-pKZuMsDnLehad0x97Zi9hzmWvjDOY76NXxNvkIHDwqanomRlcy4Di4JL2fzZ0D6kDvncWG2Lq8tQlhIyHFSSGLn3qQQEhaeTeM4kOLN98at00AckdvtBjRoliPQ-ed-eA8CIVtcQr8_5NK_DN52YtUBn9NbuxM3-zFoB__lpLErjDN_aFgM4o8Wl45UX0vfAaPYEyCS0e77fqk8On8wp_9w9gitqlBEfC5ZlWK3Rv0gwmDb8zwmf-tpimZdJsr2VDXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر ربایندگان نوزاد تهرانی
🔹
این ۲ زن متهمان پروندهٔ ربایش نوزاد ۲ ماههٔ تهرانی هستند که یکی از آن‌ها نوزاد را دزدیده و دیگری او را تحویل گرفته و نگهداری کرده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/farsna/457528" target="_blank">📅 15:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457527">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slL58QenS-oh5JePEi4_OwDrYh1L8XAGGW2xt8CaLbuxQidmGeA_b8yp9pD-gKT7sQ9K-Jr7RjAnViURmCxA3dp7w5ciJBay_l1MsaWNu0BlnlqXyBk29ff9LmpQNer6qwGM73OvYoGKGn9fCmMASrWi1n9RWzWtnp9swPLUsAi4TIxejRRysATmNnsUI6Difn633xPqpz7ZjTqEmXVxhOh_yFox63KBveN5ba1J3RybHP42VjHf3Y77ptdKA8_IptbS8xOHJpxkd2cWCmc0vHtUIBHykPWpq8faMdmjRjJAsY-kRwPt6dC1nhtCt-y3AZHY5TMKCV2B2kTqCvJFqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: در شرایط جنگی هم سامانه‌های جدید وارد میدان شدند
🔹
امروز صنعت دفاعی در ایران با وجود مشکلات و تحریم‌ها توانسته، دستان بلند نیرو‌های مسلح را قوی و با اقتدار کند و با وجود ادعای دشمن مبنی‌بر نابودی آن در خلال جنگ‌های اخیر، با تدبیر و دوراندیشی‌های لازم، خطوط تولید تجهیزات و تسلیحات مورد نیاز نیرو‌های مسلح را فعال نگه داشته و فراتر از آن موفق شده سامانه‌های جدید آفندی و پدافندی را در شرایط جنگی وارد میدان رزم کند و این روند همچنان با قدرت ادامه دارد.
🔹
ایران هیچ‌گاه تسلیم فشار نخواهد شد و نتیجۀ این مقاومت تاکنون منجر به شکست بن‌بست راهبردی و سردرگمی برای دولت ترامپ شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/farsna/457527" target="_blank">📅 15:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457526">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j602MIeAFljZ8e1ifYB89tCutVfJ5HxQdK_bI-h57O-OxLrtbqtvA5ZSSOHUsG2w6KU9Aju3KtZZ1cWrOpf2pbrERdm_Fx_Hz5wTpHUifvJ8OMuZVIywOqwVVUENiXXyfZtvVcS_ndwvasDudE1Rebm5Cr2Oj0Jmy8af-URGtDTc6oJGsA7ufS-CFk1es08sVvwJ5uvD72A4Tk7ipDJI8u6K1RrAPYRbmnoWISDEJBQOjDAKaM6s9iorVhLEP7Rt2OstOcBLqpp_JDpycyai6iSnaIyrKWNSFo-rxmZ6BJd4kxVKshbwUXbVDpx_xdjHkeO4Fdj6TVNBjbkbB2iikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بادهای تند در راه ۱۲ استان کشور
🔹
سازمان مدیریت بحران با صدور هشدار سطح زرد، از احتمال وقوع بادهای تند، گردوخاک، کاهش دید و خسارت به سازه‌های موقت در ۱۲ استان از فردا تا چهارشنبه خبر داد.
🔹
خراسان‌رضوی، خراسان‌شمالی، خراسان‌جنوبی، سیستان‌وبلوچستان، کرمان، یزد، فارس، اصفهان، مرکزی، قم، کرمانشاه و ایلام درگیر این شرایط خواهند بود.
🔹
همچنین احتمال شکستن شاخهٔ درختان، اختلال در تردد جاده‌ای و خسارت به محصولات کشاورزی پیش‌بینی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/farsna/457526" target="_blank">📅 15:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457525">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76845d14b.mp4?token=R7ESfRxG78TqPKCmS9MbZ82NLfvldPlCNlCfFdT-MrUOUFObskMznWPB3vosGOCCRp9AyPNjLI3sR5Ynrl9_T83lBPo4CWdJDgD8qArrFDXG-ff0VWJj6NY-BsA75YXzHyZQuAfvWPnrz-bZhcnsC0HSc2NpZAYV1L4lk-gtvhh2R3Jv6npl9R6kus0bC1VubL8F2HaK5xup3CgpPrIuEhLo9CPL8ouWz0M004wkdMMCSnXKnIBHom2ApYxAbJklKmA0EKbTZNGybnWibkENjdMApsVIKhyigg8MY12seRLvmHd-EzAavQYJbFBhEUEjEpsdeyKx7HevHHv2WKf2Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76845d14b.mp4?token=R7ESfRxG78TqPKCmS9MbZ82NLfvldPlCNlCfFdT-MrUOUFObskMznWPB3vosGOCCRp9AyPNjLI3sR5Ynrl9_T83lBPo4CWdJDgD8qArrFDXG-ff0VWJj6NY-BsA75YXzHyZQuAfvWPnrz-bZhcnsC0HSc2NpZAYV1L4lk-gtvhh2R3Jv6npl9R6kus0bC1VubL8F2HaK5xup3CgpPrIuEhLo9CPL8ouWz0M004wkdMMCSnXKnIBHom2ApYxAbJklKmA0EKbTZNGybnWibkENjdMApsVIKhyigg8MY12seRLvmHd-EzAavQYJbFBhEUEjEpsdeyKx7HevHHv2WKf2Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تغییر مهمی که در پدافند ایران رخ داد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/457525" target="_blank">📅 14:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457524">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hijZiR2uRGPjrSQ5-JgkBJpGWVV7NK5qydKZgeXINvvFqOPUN_GGtRTy6OOjoe_obEEEMj7LS4QwrS7iET6_hGRQTsW0fEYCRWwr1Jq6VCxMLpin0vztPtsGdWshMz4gTc51O0miwNzg7w7yKfDayctfSXlyBAe3Q6g9_mRHOLGtoETADxcFvy3x2sqQZehxo5Wwu7e58hzC4-DXzZp78CRwQhNek-Pm65Mj2eUdLup-3oWu09rkdubDpeb6fuzqCx5pJSb-qtK4rGvV2ggIxenFaiIcpJ_0R3wygkxAVv_aeQqMS8FdhGx3HwNdAvk9xS10VHVQzuUdqYkCBlKPnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود بی‌سروصدای سریال‌های اینستاگرامی به شبکه نمایش خانگی
🔹
میکرودراما یا «سریال‌های کوتاه عمودی» بی‌سروصدا وارد بازار نمایش خانگی ایران شده‌اند؛ قالبی که برای تماشای سریع با تلفن همراه طراحی شده و حالا با فعالیت سکوهایی مانند «سریو» در حال تثبیت جایگاه خود است.
🔹
شبکهٔ نمایش خانگی «سریو» با معرفی خود به‌عنوان «اولین پلتفرم سریال کوتاه عمودی» یا همان میکرودراما در ایران فعالیتش را آغاز کرده است.
🔹
پلتفرمی که تولیداتش با محوریت استفاده در تلفن همراه طراحی شده و قرار است تجربه‌ای متفاوت از تماشای سریال را برای کاربران رقم بزند.
🔹
در معرفی این پلتفرم آمده که «میکرودرامای ایرانی و آرشیو جهانی» برای سرگرمی کاربران، از خانه تا صندلی مترو و اتوبوس، در اختیار آن‌ها قرار می‌گیرد.
🔹
با این حال، «سریو» در سامانهٔ مجوزهای ساترا ثبت نشده است. این پلتفرم اقدام به بارگذاری تولیداتی کرده، اما در زمان بررسی، امکان ورود و تماشای آثار آن برای نگارنده فراهم نشد.
🔗
ادامهٔ خبر را
اینجا
بخوانید
@Farsnart</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/457524" target="_blank">📅 14:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457523">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf-YQB6X-ThHb-MZPd2CuAg7tjhEH4QsfkO2MP28W1pmtGkWHyDohLgE-p9gWySYK4O4SmCG8UIxgbXE5SZo9nQkYmfx-bnrg_Ca4_tbBCflHwWQWzzSXpfpFsILfmD3gb8qlXQrV1pXA_Kym9wM-aS9FGIzXidEbtYLE-0Q66PMDFuUeZVhNr-2Sjkk4uSW3mlJzluum1CFylua0Y1A4oaaEssKVNfC0e51MAfdWJAh7_QPUVTlOYAVA0Z2NKOteP6-zqjIkeYntHvBWY2l6pltFirz4v0XXv2ZIrNjKo_3coMpqqKxr3TcXwiZnCHU1caKbiyJ6Gu-PcZPtricGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۴۱ جمجمۀ آهو از چاه آبی در شاهین‌شهر
🔹
فرمانده انتظامی شاهین‌شهر: ۲ شکارچی غیرمجاز که در یک سال گذشته بیش‌از ۵۰ آهو را در مناطق حفاظت‌شده شکار و ۴۱ جمجمه آهو را در چاه آبی مخفی کرده بودند، دستگیر شدند.
🔹
متهمان گوشت آهوها را به‌صورت غیرقانونی می‌فروختند و سر آهوان شاخ‌دار را نیز برای تاکسیدرمی در اختیار افراد سودجو قرار می‌دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/457523" target="_blank">📅 14:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457522">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d662816f83.mp4?token=sUxJbomaEIVzHwLtv1yKW1NzcXnl7kk2FpF0NaFmqJa_xaloY8HzMq2xF5isd5F1rfCep_GvAxGI_W761IQwFTLFQU2_r7-GTenCC6cG3DJRqCPvqVYW70lygYDV9UI7v0ZVM7i0zJJ6ULTPBxXgRq04SsCoicfw0cjRcl5cDKa1YWfsBweY5eVf-UPCghESSbzyhv2hMqof_ARJ3Y0Ef8sg7fwzkz1h3itQcBbwTglHYOTSGt1RipfIp-lIzk-t1ttNIaltY02NS20U5ZZsWYS0PHIXI3y45TAqAsccywbCcrXrz96GLXJ-HlPWe_x3_WifvaQRkup_D-ax07Agd4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d662816f83.mp4?token=sUxJbomaEIVzHwLtv1yKW1NzcXnl7kk2FpF0NaFmqJa_xaloY8HzMq2xF5isd5F1rfCep_GvAxGI_W761IQwFTLFQU2_r7-GTenCC6cG3DJRqCPvqVYW70lygYDV9UI7v0ZVM7i0zJJ6ULTPBxXgRq04SsCoicfw0cjRcl5cDKa1YWfsBweY5eVf-UPCghESSbzyhv2hMqof_ARJ3Y0Ef8sg7fwzkz1h3itQcBbwTglHYOTSGt1RipfIp-lIzk-t1ttNIaltY02NS20U5ZZsWYS0PHIXI3y45TAqAsccywbCcrXrz96GLXJ-HlPWe_x3_WifvaQRkup_D-ax07Agd4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازدید رئیس ستادکل نیروهای مسلح از یکی از تاسیساتِ زیرزمینی تولید موشک‌های بالستیک
🔹
سرلشکر عبداللهی در این بازدید در جریان آخرین وضع تولید تسلیحات بومی کشور  قرار گرفت.
🔹
رئیس ستادکل نیروهای مسلح: دشمن باید بداند نمی‌تواند با ارادۀ یک ملت بجنگد.
@Farsna</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/457522" target="_blank">📅 14:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457521">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KATuv-GeZuUWryf7Y6Z1NaLecsPIJWpSuh5oVbougszzNGhIbpd27Y1ztWoQNQta3S_Ny6Ygw8ELiw2w7ujU78G85SM5QY6dGv-n3HCx9sfTW6iIplAWj3zEFmxAzUmUx1DK5RoWP11ixyim9Bex8N5Dph6s9bHobKRdcJtF-LuQu37JP6TO8N-Dypl1CshZVj6Y_koHjlpHlafnCbzimWX3RoVX7dq4IoXYUazOI3BxplzFEugkDFU2ORIrKJxSitkTNpj3ishh9NvZ2G9WplDcye-FSowkhX86tT-KioJrbPOan_7ZFQSeFbfnexQC4mow2meVmTciLDC6mxHIoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
روایت قالیباف از بی‌اعتنایی کشورهای منطقه به اظهارات خصمانهٔ ترامپ
🔹
رئیس‌مجلس در واکنش به تهدیدات ترامپ رئیس‌جمهور آمریکا علیه کشورهایی که به همکاری‌های تجاری و اقتصادی با ایران ادامه دهند، نوشت:
🔹
ما پیام‌های متعددی از کشورهای همسایه درباره شکل‌دهی به ترتیبات امنیتی و همکاری‌های اقتصادی جدید در منطقه دریافت کرده‌ایم.
🔹
ایالات متحده امنیت تک‌تک متحدانش را با قلدری و بی‌اعتنایی مطلق به منافع آن‌ها به‌خاطر منافع اسرائیل چنان به خطر انداخت که آن‌ها برای لحظه‌ای، تمام هستی خود را در خطر دیدند.
🔹
یک نظم بومی و مستقل که واقعاً صلح و امنیت را در منطقه به ارمغان خواهد آورد.
@Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/457521" target="_blank">📅 13:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457520">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9t0SIv3u7kiQ49Lxxyy4sU4s81oykCaMV2Bt9ic3_lJdhN95CRT0-G0tIh_WDPXw5wKZa20mlXR9i7JUEBkbEkkeDtrKQedf1etOOvag8jg1NAecNVxREX8MfngSwCd1oAHevlH2XAyKG6hSwMjQ1D9AJQf-MMbXCxk77zAFozDnD9ZsIp02Qe5nw4W1vDN4TBKtganCVM9g088d2lA5TB_pDfQ2GFRB_TCMggQLYscBom1_EhczIF0g8eCwnV4saSwzgXc030wrVjHExtkF1R7wu82SBJbbdEve3k03e1_mTHpdXXD0BKhYbhC4U_WZzEgV3Ue6ZgepOTAO-uhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۴ ریشتر در عمق ۱۰ کیلومتری زمین، ایذهٔ خوزستان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/457520" target="_blank">📅 13:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457519">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv1bp96jLrHgm8wfOnRnxOe7Ho1xi0jci-00wT-E1bixsRRubiKqN8F7OaRkh4xadhbx1fPgNSIE3rsccfCwoAXI617J1rfte8vXVe12LD4MFRGxGd8XTlBaTGpSh_Lpmad68pJ2dQTPdjutxh1HvS4GdRsxhHNdbI9-uxh9W_v9khbCnrU5vN6lekkfS2URRqI9hi10c6Btsv5qpD3NxN3youKCsZnT2ebOIGWVyCZRcjFoR67fk6lL-OBSPsOHG6Es5x0L27UBzhufBdBz1y8jguTiL8_799HSFOfdl1EFIjSVq0r6kTGywc_rdBywgRjnmz_JUYlAJjnlC17hPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بسیج: نقشهٔ جهانی قدرت درحال تغییر است
🔹
اروپایی‌ها متوجه شده‌اند که از سوی آمریکا تحقیر شده‌اند و در سند امنیت ملی ترامپ نیز به‌وضوح دیده می‌شود که جایگاه اروپا تا چه اندازه تضعیف شده است.
🔹
امروز نقشهٔ جهانی قدرت درحال تغییر است و این‌گونه نیست…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/457519" target="_blank">📅 13:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457518">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c47d6c6a.mp4?token=kH_U6TsEBgaJDpB9RRdZ4EFIEK0QPxLoWGQi7HTJXYtE-uNOVmHibipDAB3knTCIaRhtleXj09g5k-wHLTzgQco_OxfrqPKotrvkoO_abKuLHZlN2Q4J3gphw1XZYMKZrwm53jsWqvWSngIXJi2oyLgTZ1lJS0ZBINu5r9SxjFqezzd6IfsizsQHcUWX_5Up5gMEqMlU6VtzrnZQkgzD9VUu-ZJGbRaUGCAmk0Eyc1XPX4zATGjpqs4G1nchlmjoYW-tMvwag0GpAXq3Xx1UUPUpNflhICPXWr9zhqsqmcoahPvGPmMrw9x99gqcxFXtOBLdC7V3t5zW895WNbqefg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c47d6c6a.mp4?token=kH_U6TsEBgaJDpB9RRdZ4EFIEK0QPxLoWGQi7HTJXYtE-uNOVmHibipDAB3knTCIaRhtleXj09g5k-wHLTzgQco_OxfrqPKotrvkoO_abKuLHZlN2Q4J3gphw1XZYMKZrwm53jsWqvWSngIXJi2oyLgTZ1lJS0ZBINu5r9SxjFqezzd6IfsizsQHcUWX_5Up5gMEqMlU6VtzrnZQkgzD9VUu-ZJGbRaUGCAmk0Eyc1XPX4zATGjpqs4G1nchlmjoYW-tMvwag0GpAXq3Xx1UUPUpNflhICPXWr9zhqsqmcoahPvGPmMrw9x99gqcxFXtOBLdC7V3t5zW895WNbqefg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با کلاه انتخابات ۲۰۲۸: باز هم برای ریاست‌جمهوری نامزد می‌شوم!
🔹
رئیس‌جمهور آمریکا بار دیگر از تمایلش برای یک دورهٔ دیگری ریاست‌جمهوری برخلاف قانون اساسی آمریکا سخن گفت.
🔹
ترامپ در شام همراه با خبرنگاران با لحنی طنزآمیز گفت: برای اینکه نشان بدهم چقدر…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/457518" target="_blank">📅 13:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457517">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMnGs--HGQvbePR8szh5_s8cAj1JI58L6tN3uUpRi02T3CH-WkvPFUUCcILqzpiX4WRMaOIxrd_R8JscRMCJKwuHRhbrnGeU7gMEZ_YKmAXGgsF-kD09XWpfmvB2OJ8wWYC1hUAiTx0Tbku9m4csNgULzeIUrCtHKoAT1oI1oU5xF1HgQ4atn79aLiogtBpmHMm7AEpM_bjbDvcNcupTrm8BOU1mqIpgWTwJUR7efWmyIbvjVRdgQItuSE5X_IIzLdFMbAaHmQZr0h86sei3NVjGsKmIHuPv2Kf6zaujZPEernK-Rm7zypgyKKSlV5LOYe5UrMfF_8TEOKs4oXPzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: لفاظی‌های ترامپ از سر استیصال است
🔹
رئیس سازمان بسیج: اگر این حرکت را با قدرت دنبال کنیم، باید بدانیم که روند دشمن نیز نزولی است.
🔹
رئیس‌جمهور آمریکا به لفاظی روی آورده است که این لفاظی‌ها براساس ابتکار عمل نیست؛ بلکه از سر استیصال است.
🔹
دشمن ابتکار…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/457517" target="_blank">📅 13:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457516">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5WAPXp9gCGSrzVr7DwMRL97zgD9Sh-EZSedb0TZwY-f25RZpbq5iDb6c6VTABJn9w9XLaUm4D_TosWlDtCpFyGLhrwrK5Iv13sFNywtaL7yhjjrfrNEf0jP-haR6jFouEdWCPoyk3L-d9WLRbpfwlqN62NFkcz3njukGqpib2IWiaRW6zvGdHJvn4jYYazCd7SnYyP22yQ8KLacx9AEoQIP5B_kCRhP14VdSOJMZIuZiT-Woh82bOQ6pqzjPshb5K7dvOhUYZ15F0Z4n2LmSNIykqRBan7URlQiDI_0MQqnkAkwh0Lm92e-OBjYxzudcrveQbgVkKFyN-zm13efWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: لفاظی‌های ترامپ از سر استیصال است
🔹
رئیس سازمان بسیج: اگر این حرکت را با قدرت دنبال کنیم، باید بدانیم که روند دشمن نیز نزولی است.
🔹
رئیس‌جمهور آمریکا به لفاظی روی آورده است که این لفاظی‌ها براساس ابتکار عمل نیست؛ بلکه از سر استیصال است.
🔹
دشمن ابتکار عمل خود را از دست داده و تلاش می‌کند با روش‌های دیگری شرایط را تغییر دهد.
🔹
براساس نظرسنجی‌هایی که در آمریکا انجام شده، ۷۱ درصد مردم این کشور معتقدند ترامپ در ورود به جنگ با ایران اشتباه کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/457516" target="_blank">📅 13:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457515">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تراکتور خواهان تغییر قانون سربازی به‌خاطر بیرانوند
🔹
مدیرعامل تراکتور: بیرانوند سرمایۀ ملی و از چهره‌های پرافتخار فوتبال ایران است. او در سه دوره جام جهانی حضور داشته و برای فوتبال کشورمان افتخارآفرینی کرده ‌و باید مورد حمایت قرار گیرد امّا با این حال، متأسفانه…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/457515" target="_blank">📅 13:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457513">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsFa_-N5U5C5pjbn96rNmWkWty9bnxYiEIwROq2RllUtqpNXrtn4_oWscJm857FaXrLKhlnpH4zXk2RIaovRU9W-ppwhGaeBRWKh5Rwf-UwpZVARmNCSUIVO9Kgl98MGbYsFC6mFhYHrwT_UluzfFCxk4Byo3sDCLejvQxkv6bA0JXmodMOEfgkeRuayFB3Fb8KRjkF9-Hok1xRIfrd8b_dvlvmUpzYKqL9gnuUq14E6fFryHhO6hWDfFFuKKSszbI-XlM627RW6w4sK_mUQvQUCleQrydTOGnkPtPIrlarUQTBZ0egJkOXHR9xIEaQ4B1e6S5YX3aZ48tn3qbbDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYmsGtUT3Mkyf8xay86CVpA8jV0sdUDMe47e36GcIlqr0VhG_qQdTdDCUSU-glefilNsbiBGMeBbiz15HjCOKGyXX_7RsmJQzdQWe3TfluT9wesPqa1lFFxyBd2f94Vrr3UdWqGyMpgClqJ45kx_Yh4ib3z_aASsfwvSJpAVtszPYw5CbzvvFVnndThKXYCDKNyzEME_UhTLvRWhml0hqDZ2V5cHUMkJM8pcIAy2jl1wxj1C2gl3AtSTw9whz9P77XiYPig7zyZ8vJUiQPtzgJplZkMNF2j9rJvgyyBkRcV58PcwfO6DaPPu-_Cx-BNWeN_RotAYkyrritaQCHtjJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پلیس تهران نوزاد ربوده‌شده را پیدا کرد
🔹
در پی وقوع یک کودک‌ربایی در تهران، طفل دوماههٔ ربوده‌شده توسط کارآگاهان ادارهٔ یازدهم پلیس آگاهی تهران شناسایی و پیدا شد.
🔹
پلیس اعلام کرده که مراحل تحویل طفل به خانواده تا ساعتی دیگر انجام می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/457513" target="_blank">📅 13:27 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457512">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyxHAHzWW3qe7EjxA1LMl-brAukmPecoRlOj-LSnBnQ2z35jvDUhOQHlc2A43M5nWDlS2I5OZHhT5zEcRTQWRWsdYcNWc1czX3RVaYEreXmtqmopgVA8TaSMObXy5kyBR7eOpXa_6qAJ7fadWCum30ZrQNeCUwWY5d5dwLgdOOg1P-pMWgEGZKN5lorQdE-C-_C0NpbKfkirYWaavvs4dyabLG2QpxOwy0TzthIvso_we7e6DTAGEfE9yd3Xh6CXPzHX1-Nh4gm1aCr4LuGi3Tqou06wJbOAK2p6BCoKsc06Oh1OU3ARB3C-tbaU3VydAFFN2rRhHCb9FYZNglhRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ معاون اول قوه‌قضائیه: تغییراتِ دستگاه قضا ادامه دارد
🔹
دادستان انتظامی قضات پس از بررسی گزینه‌های موجود ظرف همین هفته انتخاب می‌شود.
🔹
در دیوان‌عالی کشور نیز تغییراتی مدنظر است که پس از طی تشریفات قانونی اقدام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/457512" target="_blank">📅 13:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457511">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گل‌گهر هم راه استقلال و تراکتور را رفت
⚽️
پس از استقلال و سپاهان، ظاهرا گل‌گهر سیرجان هم سومین باشگاهی است که نمی‌خواهد پیش از مسابقات باشگاه‌های آسیا، به تیم ملی امید بازیکن بدهد‌.
⚽️
سهیل صحرایی و مهدی گودرزی، دو بازیکنی هستند که تیم امید برای حضور در…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/457511" target="_blank">📅 13:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457510">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWhe6NH-L6AmIXKp8ISxsr6oVExn4m4Wv3VJFQ4FF2oGI4wPrEEx1LTzXxCd_T-9vrigogzAkvuSu7mY-utec1jTM0jPZ8MMQ7CigEh6jeyjn9VsgnhWh44Z0zO7PWg3tgZGIjx1hrwN2Q-k5YPaJjwQuLoyc-F--ObJbjauJncsxsqAuVfbuOn6y_nih9eVyULMKsRE4Fs6oZVISBdhzqw07ZH5W0VILn27aFpvw0aSgTrbt5gSawDpZLEgbkc9VVgkc6qBQsRqq3H1lgzqIPyVFVR36eCHKgdmOvA7T0XEWU0jYrJq6wAAZrwgs1Es8mbdxLLFnTqIQlckqtKJaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی استقلال: علیرضا کوشکی به‌‌خاطر حرکت
غیرحرفه‌اش
بعداز تعویض در بازی قبل، فردا مقابل سپاهان نیمکت‌نشین است.
@Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/457510" target="_blank">📅 12:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457509">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsgtdHUBCPtLL94jf7AzXGBwiLvE8yse6GVhtcOt4YWMrG1s11uIcNZO9esaFhTqCtqP0pS8Md5wQ7Q6iFmNVLlXU0GwZgHYy0tkFDrqfAvYEYY49vzVbgpycPeXqavV1FzsUL_SBBrsmCtRd99d2ittCLoEyYgWnHiRdp1Z3PmNloT7NhY7BLL8xBM7GfhQ3AEfxRgHSiKG8rsh_cqoSXwGQ16hFbJQLxbi1_Zh6x2gMiXLZ092P69givG1iQrr4Ayn7ngpAeJK8kRms9psa-WnBkdOT4Yx9pn2etfbilp4xQarPazrEjTgY9WY5ojejt03Ec-5ReUKRHoXCMznxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل تراکتور: بازیکنانم را به تیم امید نمی‌دهم
⚽️
باشگاه تراکتور در فصل جاری در لیگ‌برتر، لیگ نخبگان آسیا و جام حذفی حضور دارد و با برنامه‌ای فشرده روبه‌رو است.
⚽️
با حضور مهدی هاشم‌نژاد و امیرحسین حسین‌زاده در تیم امید برای بازی‌های آسیایی ناگویا موافق…</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/457509" target="_blank">📅 12:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457508">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df76036e2c.mp4?token=GwThio_EaxAdMypN2K7JT4OfppfahR8hkjDdG4T01f7aNV40kxhMtPU-XViVt6kXAWav3B6JopLCLDMz49kDYufguNjCjTAgZK8hGLPdr1paTUWeZTCORGgXhMpk3mjGS2wDXwBKVzoYgpr5lbwffF9EyeY_R7HduaaYZuFi0WS8yx-RFale04c3NcQBLdp9zX4IQdR55T-zzoSQwlAT13KaTGEq2Pgcjdbu5JkeZZM3f1OL_A8XZoMy5uvNLlH0z2WoNUxbKdgRwFMZ2XQmSaL-4Zg4F682eXhCYcJCKtQ1gWxAvX0Puhzgl8GuZTul9oB70cm-m4VlZZgPwn_Nrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df76036e2c.mp4?token=GwThio_EaxAdMypN2K7JT4OfppfahR8hkjDdG4T01f7aNV40kxhMtPU-XViVt6kXAWav3B6JopLCLDMz49kDYufguNjCjTAgZK8hGLPdr1paTUWeZTCORGgXhMpk3mjGS2wDXwBKVzoYgpr5lbwffF9EyeY_R7HduaaYZuFi0WS8yx-RFale04c3NcQBLdp9zX4IQdR55T-zzoSQwlAT13KaTGEq2Pgcjdbu5JkeZZM3f1OL_A8XZoMy5uvNLlH0z2WoNUxbKdgRwFMZ2XQmSaL-4Zg4F682eXhCYcJCKtQ1gWxAvX0Puhzgl8GuZTul9oB70cm-m4VlZZgPwn_Nrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌بابایی: وقتی قیمت نفت بالا می‌رود یعنی ما برنده‌ایم
🔹
نایب‌رئیس دوم مجلس: کسی که به هر طریقی فناوری یا اطلاعات در اختیار آمریکا قرار می‌دهد، در واقع با ما می‌جنگد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/457508" target="_blank">📅 12:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457507">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پلیس تهران نوزاد ربوده‌شده را پیدا کرد
🔹
در پی وقوع یک کودک‌ربایی در تهران، طفل دوماههٔ ربوده‌شده توسط کارآگاهان ادارهٔ یازدهم پلیس آگاهی تهران شناسایی و پیدا شد.
🔹
پلیس اعلام کرده که مراحل تحویل طفل به خانواده تا ساعتی دیگر انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/457507" target="_blank">📅 12:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457506">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfTKTnnNd4p93OdQHzlAdUkyxcH_wOxBTe_v_m6tzX5tCS9Y-meXqjjTbDBFhEhG6IriZXXQ6RDouOMFEBVThzZ9luA9ZIjEP7R4upGMgpgWfZSBjzCJsz6oEbS7WML66hczUZ72RIF0k0n4d6BVjo9qTYWYcscOa-d8hunzAmbG9IHXXHTdR7VpwMo7SOY-DomLi4UCXrh_sA7uwAB2yaQ38MLO9s4sluffOMfaRV4VKSd43ef0n_YtupWm8DJWDLyExgchVF-eEEPC69PVhMRkBmLnRXv4Ybn0ggeTjhYIT5UPY-pJ6iyEXDEnOn1C_YNQPNMiPWY6CP6DwpHbwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۶ میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با جهش ۱۲۰ هزار واحدی، معاملات را در محدودهٔ بالاتر از ۶ میلیون واحد آغاز کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/457506" target="_blank">📅 12:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457505">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KE_OHGjRyJKGt16uz8Pdfz_NrbxfjaFQhJjzd6VlHX-de-hEcQduOv86fzKjOD9s15HvKt2UzqGanyLEenYRUT8hQq6eCQc6w6xomvTpBPWwu0bDladpefEPpbNv8CKUtvgoOs7Dad-mGd4eF93hNqjbYwREmTz8Sfbd3R2ztQUS6OJ6cW_68WVHijyJeKdVBGg5giVgsX0Emv1bdJ6M4BvGHW9Jyfs0-AZr6IEmBu0_b22TtMJ0bk9cy1lOYt5w7Yi3800B7WQ4cs2qIm8pWhz5y-A8wW9wsRouX3IA4Fwz9GeuyfMwbT8UD8hfHQbRXMnDu16P_QEweCmMhOXwyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریادار ایرانی: صنعت دفاعی پشتوانه‌ای مطمئن برای صیانت از استقلال کشور است
🔹
پیام فرمانده نیروی دریایی ارتش به‌مناسبت روز صنعت دفاعی: این صنعت با تکیه بر ایمان، دانش و روحیۀ جهادی متخصصان ایرانی، به جایگاهی دست یافت که امروز به‌عنوان پشتوانه‌ای مطمئن برای صیانت از استقلال، امنیت و منافع ملی شناخته می‌شود.
🔹
در شرایطی که دشمنان متخاصم با بهره‌گیری از پیشرفته‌ترین تجهیزات و فناوری‌های نظامی در پی تحمیل اراده خود بودند، توانمندی‌های بومی دفاعی کشور، نقش تعیین‌کننده‌ای در حفظ موازنه قدرت، افزایش قدرت تهاجمی و ناکام‌گذاشتن اهداف متجاوزان ایفا نمود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/457505" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457504">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDg8zznc5eULFXHhs672RfL5O2SmGZuTMy3UX3NLioi0FtR-RamiA1LeA7p8YTnde7HgshJR6tEEJQOSzUgg3_spGhp4HpiJ1PytcE1sQoNgAnJtkJDf3fzcC4H7Goj1RUCU_Ecp0d5bDoGq5NQSDCkH2xPffx4CcjOqieuReiUXhgfYTOV5AsbxXICQCQdXPhuIuFHMGWRNV7z1QLxYm5poujbDGUzJjjd85vupUUI_LbZ2niRuOH2O9nBPSzCyrRJwddBqY1-nPP2Ct_02O_b8zSbo67VDTqsZF95c7ik_dnkthI9jB7GB2VTRUglbijqq79b81dSietrUIdSb_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ قطر: از ایرانی‌ها خواسته‌ایم برای بررسی موضوع خلبان‌ها به دوحه سفر کنند
🔹
سخنگوی وزارت خارجه قطر مدعی شد دوحه از ایران خواسته برای بررسی پروندۀ جنگنده‌های سقوط‌کرده و اطلاع از روند تحقیقات، یک تیم فنی به قطر اعزام کند.
🔹
او همچنین مدعی شد شمار خلبان‌ها ۲…</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/457504" target="_blank">📅 11:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457503">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCIwCnSu9zPUMhjTD2T1RHvqXjqN7DSNTeDwZ8JfMUi8LSySqQuBJuMEn01YdL7wefwuD2zvhM08AbOqjEdJJ-mqvN6mdphEwMJ0glcU9WVM8iE3gfuwBLiZXAb5pU1I--iB70MWKXte8z3OATHbew_UukoQlANhXnDwpK3GW2U5eQBzzkg17dGHhW-V7_UWhgYdbS3muWe5MyGwMiMbFsW-kep5b0zxiQgjwpD3c-EDKU-9IE7httGyiUSDnGAvlNAZeQC-s2Kniiw4OCdw6og3S1-nCSCkPOwmhXl6EyA3UGACHVDii01PYYoclaZg1wLGaZBcF6bW4Et_V5ozPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول نفت آمد؛ مخارج دلاری دولت تا دی‌ماه تامین شد
🔹
طبق اطلاعات کسب‌شده از وزارت نفت، ۷.۵ میلیارد دلار ارز نفتی مرتبط با فروش ۴ ماه اول سال در اختیار بانک مرکزی قرار گرفته است.
🔹
این رقم ۱.۵ برابر درآمد نفتی در ۴ ماه اول سال قبل است.
🔹
طبق روند بلندمدت هزینه‌های…</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/457503" target="_blank">📅 11:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457502">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDYQ82X_J8lH7mnoFks52i9FTPgIyHQ9cz_eN2sKHTYJFgzpxF_da4qSFkZlMdCU0c2JdDKX9bCKiuZe4yuQCUILqpsA0GkVqxFOu7TRu7-63O8pnWehUSm7TLm9qLKOKcnyUskC7YUahfq6hptJeXTFjtMWpsI_f_HRbu3E0hGc9oBG-wdl-4bB86p1tAKYvAoB8qBiCs5z3vwYqpKfcVCXejoZPL0JacmaolSyHYY8p2r7EUyDOFwxG1eN23a6nLgyGzSpJ3O16DFbPP5DDq4U48H6ZEXEvUZ_TSg6dXNU28-p7jxRfJs_v9szJ2vLQoCuVfSzu8BLg0tc3sT9dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تراکتور خواهان تغییر قانون سربازی به‌خاطر بیرانوند
🔹
مدیرعامل تراکتور: بیرانوند سرمایۀ ملی و از چهره‌های پرافتخار فوتبال ایران است. او در سه دوره جام جهانی حضور داشته و برای فوتبال کشورمان افتخارآفرینی کرده ‌و باید مورد حمایت قرار گیرد امّا با این حال، متأسفانه قانون معافیت قهرمانان شامل حال او نمی‌شود.
🔸
معاون نظام وظیفه عمومی ناجا شب گذشته اعلام کرد بیرانوند از ابتدای مهر ۱۴۰۵ مشمول خدمت سربازی خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/457502" target="_blank">📅 11:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457501">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBCOr1eF8FnmQciJ6-DGzvGWv7iFixenUtcNdNzDaY95xiT_UqaZfsZebuaTgLZbl5mxxJuz8r4mSC6knA0Y2N4jhDRDjjPgovHOw0RVMA-f5dt5H9tmWlJA-FsDpRjqahp04I3CIp6ouX7-2ANNxOM9wW-hXD8E6Njc_zy4lI3OSgMiYypVWGk_Ub8Qs0HVxNtFtXWdUAoDVe4o-815S4Htio5dofaD9KImdwXnnl0SS45lNBd2IGJ3JG4TbNZ2CTt-_pzgckps5D8N5ono8DBOB5RXm6l9XRPwdZHjwCdKQ9XIxZH_BkWRPJib5YBCQ69TDWoKKuDZ6omobvmAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل تراکتور: بازیکنانم را به تیم امید نمی‌دهم
⚽️
باشگاه تراکتور در فصل جاری در لیگ‌برتر، لیگ نخبگان آسیا و جام حذفی حضور دارد و با برنامه‌ای فشرده روبه‌رو است.
⚽️
با حضور مهدی هاشم‌نژاد و امیرحسین حسین‌زاده در تیم امید برای بازی‌های آسیایی ناگویا موافق نیستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/457501" target="_blank">📅 11:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457500">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuZjQf1kBV4TWfaENQvr9h_12caYJpi3UXTxEoUG6RKjbNlQjIYVbTuoKv_cUaVHl3oH5Hwx_FY8H3KfqOWv-NVm06Mp0MnR_Nf1WzBk_NayBlnz-yH1CYPG6Nfj-hChwiuwpux6pLZaiXBCGcTKjEcnDOJ5EppFP_MKfAIGmAURh2Eue4TVoRNQiqZipF7a3JumNL8KE3k3TzYtW67lm9j3GQZyO0fDz2cmlJSgY3dvkqifKotX8YXIaKzIkuyksME2dwpFK6V7sZnBNtgHseX5ZH_sqLXmabRV2vXOXUPt5DuT9fPCsYFahbH_Yf9OaOyMaI2QLlwK8eCsw2qm9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقیف ۱۱ شناور حامل سوخت قاچاق در میناب
🔹
دریابانی میناب: درپی توقیف ۱۱ شناور حامل سوخت قاچاق در مرزهای دریایی میناب، ۶ هزار و ۹۰۰ لیتر بنزین کشف و ۹ نفر دستگیر شدند.
عکس: مجتبی سلطانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/457500" target="_blank">📅 11:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457499">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saRIAeFEKJbkY1giEyotx85TNUaaXoXTsp3ZezmKFQIBCX_peCbPy9TauWg9QDj6lhRDM_6RHuKg5eVAg4iRwpsvQfxEwbdTL7-3We3kGQPDgDsX7gdLf_lz99gLetM50CRkPQNfiVJZpeD77b9dgPt5N1i2MygghoKqDvbCXAsVGA1vXvGiGp6WtVX9y3ale4U8UnrsF2LXcQgsxb-4-NsyFbpJJHXbklZyfc6rFjPZIBjofWnUkaMlVK_0iVvlfgD_kUV7X0P-4dPmZ_778MOcXTKr_Fq3cPPGjvJ9qNKz3rcFjoapgq-FCsCVaczRNpBL1NELXAEnwo5_ApPEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
پاسخ فنی به شایعه آسیب متانول به خودروها
✅
ترکیب متانول با بنزین، باعث بهبود فرایند احتراق، کاهش برخی آلاینده ها و بهبود کیفیت هوا می شود
مدیرعامل شرکت نفت ستاره خلیج فارس از شرکت‌های تابعه هلدینگ
#تاپیکو
با تشریح ابعاد فنی استفاده کنترل‌شده از متانول در ترکیب بنزین تولیدی این پالایشگاه، تأکید کرد که این طرح پس از انجام مطالعات دقیق، آزمایش‌های گسترده و بررسی‌های فنی اجرایی شده و میزان متانول مورد استفاده، حدود یک‌ششم سقف پیش‌بینی‌شده در استانداردهای مربوطه است.</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/457499" target="_blank">📅 11:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457498">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f649371350.mp4?token=Q1jkm2pUVAgAofr3vx7zGCddoTIxEm6Oag953RPIbdC52F9bHwBkIEZAOHhDj_f5sowmXvTGjVo5DMD3bxt8dgGsWpCASc1SEuR4nJFoyLCgI9Ci6uOOFimoe-f9uMk1VvQLGJR89qBYaxwcRfCFlo80Pf6V8ymzXeiShQtTjqtxaiORBeNA-KW90HBR3juwByID2GirCZCYU_U9EYiNmah5V__OL5GD4Ko8GKP20xvGGrquAsZws2HU36n0BbQbrIvDwv9dBfPO3UfupPb6WTkfbAYUAAfuYlzZvKRyLmCNOXsRzmRcdrZ_wiTmPyd3SG_DOkvchri1BzO_BRNymKJoGhd8iHcYud0UZIdlBAIBRFEjoOuIWqcxBB2_ngAoAUV5O1J2k2htzl4E9U4EtfwwRD6ziPk7L7EEku5nc2eqPyLkchPXR4EB5G0zHc867q471HjiIZa8o1lsPAOmaAGAqR7xqKoY2VTQLIIb0wntab_WwBV8HPIgjOxPWJtcanvnrx9-FzTsxZgggwK--OdM4-9PYy7_-qJWf_JtQqITNdmgP8I4MLw_AcbUeoA096IMjWU7SUiowvKAzl0WN2OnEZ_I2SwuMuszhIbWN9PUS3Ztq9PawF5yTZH494bvcgOpSfvz3crODW2onCGwB_O5YgKYvxGcIuioGwAkUxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f649371350.mp4?token=Q1jkm2pUVAgAofr3vx7zGCddoTIxEm6Oag953RPIbdC52F9bHwBkIEZAOHhDj_f5sowmXvTGjVo5DMD3bxt8dgGsWpCASc1SEuR4nJFoyLCgI9Ci6uOOFimoe-f9uMk1VvQLGJR89qBYaxwcRfCFlo80Pf6V8ymzXeiShQtTjqtxaiORBeNA-KW90HBR3juwByID2GirCZCYU_U9EYiNmah5V__OL5GD4Ko8GKP20xvGGrquAsZws2HU36n0BbQbrIvDwv9dBfPO3UfupPb6WTkfbAYUAAfuYlzZvKRyLmCNOXsRzmRcdrZ_wiTmPyd3SG_DOkvchri1BzO_BRNymKJoGhd8iHcYud0UZIdlBAIBRFEjoOuIWqcxBB2_ngAoAUV5O1J2k2htzl4E9U4EtfwwRD6ziPk7L7EEku5nc2eqPyLkchPXR4EB5G0zHc867q471HjiIZa8o1lsPAOmaAGAqR7xqKoY2VTQLIIb0wntab_WwBV8HPIgjOxPWJtcanvnrx9-FzTsxZgggwK--OdM4-9PYy7_-qJWf_JtQqITNdmgP8I4MLw_AcbUeoA096IMjWU7SUiowvKAzl0WN2OnEZ_I2SwuMuszhIbWN9PUS3Ztq9PawF5yTZH494bvcgOpSfvz3crODW2onCGwB_O5YgKYvxGcIuioGwAkUxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔗
پیوندی فراتر از اعداد و ارقام
🤝
میان ما و شما، پیوندی ریشه‌دار است که در گذر زمان، استوارتر از همیشه مانده است.
💎
سرمایه‌ای که به ما سپرده‌اید، تنها یک عدد نیست؛ حاصل سال‌ها تلاش، امید و زندگی شماست.
✔️
ما سنگینی این امانت را می‌دانیم و  ۹۸ سال است که با تمام وجود از آن حفاظت می‌کنیم.
👍
#اعتماد_می‌ماند
📥
دانلود
#بام
،
سامانه بانکداری دیجیتال بانک ملی:
📲
https://baambank.ir
📥
دانلود اپلیکیشن
#بله
بانک ملی:
📱
https://bale.ai
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/457498" target="_blank">📅 11:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457497">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/457497" target="_blank">📅 11:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457495">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT6fDnIdtIQg26Zegtht4evMEK0bFwCnCJTDK5zniWIQjsTiaijgn1bXuquCVFC48x5pFO53HhzryJWdsudQx-qrci7ARzYiZ589EzPzD35h3yHdr95obz0eR49o-k7IwgjFUZHEy3vq_n0ColO9nPPFZnIUnok5mwW3fvMRFHbetcbV0RUe1B7G379hf5Gfv6n8_ygcdXBiXV1QTVVCnY1GmZbALeHf6zuao7_VIftQW1LJweInBU3JjSARxyJtReaFZGi5fnu7Alct4RAc-36iya3ugPnFJ0misUZCfsqjfqyzHZg7QjKa63OQylNoGqiNR3ftAyZJEm2HimfqTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مربی ایرانی روی نیمکت قهرمان انگلیس
🏐
علیرضا طلوع‌کیان، مربی باسابقۀ والیبال ایران و مدیر فنی کنونی تیم ملی زنان، با باشگاه جاینتز لندن به توافق رسید و از فصل آینده هدایت قهرمان سوپرلیگ انگلیس را برعهده خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/457495" target="_blank">📅 11:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457494">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d7c9946b.mp4?token=ozTQDGZMnflo7lV4Ql8bmOAlIPtTi231JAmQMTdu5D9F850JT4mkD0uk8LZdqiAxVkyqimdrgCMz8N_DmhwzucJ8SXS906vikJK5ZDIelf2iQny340UWKY-XLMyO2bWUv2u-8VmOHkTFp4eBiKT6q6Tzcs8qZcLGlwfospslZnZCatnGS1xcndJz7kgG439Y_99cY3KewgY4jDXMeGXpO19r82Cj9FY5j7neAfglrSen5-JASxCdUj1uU3QWE_XKznT_Bzy9AraLJ9gJxABtkUXT3-Rr6Vul_h5lyivM-VYY2ZE0NGLBZpoYDliwgUqmNMmzu0I-4qDk15GVvtC6ZZYFmVurbVPQrCG7nBPE_CNNLsWK4uj_zfimkDxNofDMKaCW7vYsQ86rERnzbyi3ErxjpLJmu3oo4xtKFjJ6FMmhxzkEgILBOKtNyA_FmWyTQP458LHuDT3b4Ubphf-1Xs8JAu-WAHKpB_97d8SieAP8qqkOGpGw2oYBmZb1LFae27N0WR93oq-rEEA6JQ3rYWcT7mbiIs5ueULUd6d7AuuUVb5DQFeFy9MOR71-6p6PCiFtoiuUuAgMLGR1jewtOmdpEPVUvWcQe8t04Svf8ms2E1wQFTnAaFRN2Uv9jwxYE9eyfnWxuvo0tpMynxwYKNK8GaJykHoq9X26t9nNpNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d7c9946b.mp4?token=ozTQDGZMnflo7lV4Ql8bmOAlIPtTi231JAmQMTdu5D9F850JT4mkD0uk8LZdqiAxVkyqimdrgCMz8N_DmhwzucJ8SXS906vikJK5ZDIelf2iQny340UWKY-XLMyO2bWUv2u-8VmOHkTFp4eBiKT6q6Tzcs8qZcLGlwfospslZnZCatnGS1xcndJz7kgG439Y_99cY3KewgY4jDXMeGXpO19r82Cj9FY5j7neAfglrSen5-JASxCdUj1uU3QWE_XKznT_Bzy9AraLJ9gJxABtkUXT3-Rr6Vul_h5lyivM-VYY2ZE0NGLBZpoYDliwgUqmNMmzu0I-4qDk15GVvtC6ZZYFmVurbVPQrCG7nBPE_CNNLsWK4uj_zfimkDxNofDMKaCW7vYsQ86rERnzbyi3ErxjpLJmu3oo4xtKFjJ6FMmhxzkEgILBOKtNyA_FmWyTQP458LHuDT3b4Ubphf-1Xs8JAu-WAHKpB_97d8SieAP8qqkOGpGw2oYBmZb1LFae27N0WR93oq-rEEA6JQ3rYWcT7mbiIs5ueULUd6d7AuuUVb5DQFeFy9MOR71-6p6PCiFtoiuUuAgMLGR1jewtOmdpEPVUvWcQe8t04Svf8ms2E1wQFTnAaFRN2Uv9jwxYE9eyfnWxuvo0tpMynxwYKNK8GaJykHoq9X26t9nNpNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسجد وکیل نگین باشکوه معماری ایرانی در شیراز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/457494" target="_blank">📅 10:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457489">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3e2KNPjSfnz4ofEWV58cSbBlmlhHmK-0q0M3NzYsXAg239NC2TKrVqJhij1XTV3JKGbwlTO4GD7nRhJxpQ5Blm01mYCiSkYqdIvbGivh2PO7vGvrACz7VSVM4AxXhn7rx44BSAJcMKfvipBpyfSlI6khDq8O-aVYMQL9QeuvckWMOli8nDYmuHng59Lj6-yo10hkK0iAVfeFS5PImP3-fJ8GxFvJ3xW36QZVmMAMNHBM5Tw_a2iFrelVhRV62XM-oCzdRXEn0Mr8yMk1MPluvh1kiModjt5tJzI3sidaIFWMfnnWFaTgCeRVQLklbl2LfGmVF6lSNuMehSNf0mUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a6im5IGL9tnnfYSVy5dPEG6-dfcOonrLTm1N34MOq0m4G5ANfKcWFFCzqGyMOju_aFWdxv8sDZ030ndk2jgy4AfbaBfq5fRPoIKHnOo6n8QdS6s4SSrpDnF5-Gk1Ik9HNSK3eikGLoX16BH_mbefelMCIiN_sVgEbu0QNKDNg2ttLcCqXiAkf1YqiBQXsw03X377Ihp7FXjwtMbrifhoGgBr7ePZVbz0YfB1-0AgDnE4tBZkf1K4cNTE00raN-odL4RpHx2qg7593N3YFEV-AkDvNtpTdxk9asqfB9Hvw2sV1SOQ_L0EtGEywqIGhLcQgjtmE7vuVLvd3TNyGnSihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AEZr4vn4_gCTy3MRaWNoQ-hu5y083UnRhzxpRwcwTqlsZ74IpKDxwVENnpV5xGWg-f3ABmLCdes-uxLtnPiD7ovxdbU5ioIgF6yGLQHgMgBjDy9NgLaF8K4t3W_vpp20byaYMAYJeh0hgB-SBmEdvDv2uvFJ2xk_mDJ7eLieyGGUGl8uxi7pbTx0bKkjjtGaJPsmqTkVVZOXuzJdBWNLoW0Bs3z3ACdxmSKqItO8eWoWiWYaHQiz_ujuWftWB3nHeYoL4sjh49wIxwVqgVeQwPlRETNdaJ03hGD5F--1bkbrlkAozbRGwFO92Jx6FLjrGkD-6otK1kgRv3IJcuaeJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ydd70FnEYZKVr7lpp5TPXqnIg2Hhb-mw2gzG4UbOJHSwp7S7Gw47AUhwsik7m_khzrD6sbbx_UaqSlCeJL_sGuqdNNcvFTK_NFBevTNTuqfmA3BJc7D3i-TSe9JOIBljE_J6UsPzbOwbKYYAvNBrDMhc2bbLGQEI9LtfWs85ws9Sv0w088EdeDTtjQzGUkg3XjnF2aMS9v_ODQLjUegt_psZuc76PzPdyXGzNAzLqLPey1c3xklSkO_vWdOEB6Fnt0HiJQTXGIPJ4DzgzLNduvl4Pm_E3r-mvq_AYT3p0wElCRihZkCpAjlj7E53BiDIPn0T3bM6t2dczJU0zH26mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGLODPKelLflNAdLgoDaT-OR23tvaK3NycZrjre_6py_5FN2g7pyPc4Ql9WmZ16e4g0tQzPa_7HgNEJ5pSZ7NzRAVFVxL54TYqWRf9kn1n4_pFK6u5vM4T3su3g2MWVQeq8VbuNAa_8jbl-niccgATO3UfDIXVPsnMEo_8kd7pJjr7yNBf2TnJnZEwBxumVNGw9UdojGLWv1BFC3qaI3EuuiQALXKYH0nWP5-cAlGFVntG4d5SnXVxYTFHAR_7VkbOoip2_-8CcHZoe0XQrbmXYDY8HckTq2X8MDz7400I1kU5APhbWILCeT3yl-09I-6bsDrB9ZUq8nYlepSs341g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رودخانهٔ دز خوزستان؛ پناهگاهی خنک در اوج گرما
عکس:
علی صاحب محمدی‌نژاد
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/457489" target="_blank">📅 10:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457488">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEDSIyqV9WIIL6iPlZTMBMLiKlpRckRMyots0TT4M667pErg8qwMux5_Gbhkumx_WsI_QOkhat5lhb9gw_3I2qXcpIFmh-4Uxn51_YAMeCp60D8OFPyBvSNEFjMcaetOz8upS9gWS8FxAhQz25cPfG-UbSop0W0_es84hiS-rX9vdp9TiNEY8IAW_d2H8lSiVQNnyLWD_XM8naYe81qBEqsF5tc8w_tsh0D_6ghYF5CDzfpF4nxVwAUNGBJl7W7YbbxXgo2_iBCSjWfwjm8peKSirGyqi6Ty49p0AQAk7q1kRAoX9-P26HnU6kYH4o3sEFYuGMJXAdmfBy9mltai8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات ارتش صهیونیستی به ارتفاعات علی الطاهر و شهرک‌های جنوب لبنان
🔹
جنگنده‌های رژیم اشغالگر صبح امروز ۲ حمله هوایی به ارتفاعات «علی الطاهر» در جنوب لبنان انجام دادند و همزمان حملات توپخانه‌ای و عملیات‌های انفجاری در تعدادی از روستاها و شهرک‌های جنوب لبنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/457488" target="_blank">📅 10:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457487">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZToH4GD5Ge6san6ORJ_tl3cg67o_qFX1SObHW0FzgIc-P-ouw_LhXQJ9NjiEXmO7Ad7_p6wkh1-JNj6QOgR7RIiEitKnmEMkGKgiUIzBX9xwZuqzHdlORzbRpHVIPVGo6xDWO2ZrN4SW6gOWIniOJdNFpbj_3sLTgoaVHp5nF3MaM33EGbkzA_n79Q4Xgdk-SToBYgQW70LGOFEez7JBBv1nrox3RZx26-zJSa7oRZyoZsZMaEyAffdMV4Yi28PTAZm5GVuQb-ukJoK6qrFJr8r6XvcV9METJrQb7B-_EQJsWZmp2OytyTLCXRb8uLCB_NnAgc8hFdn0x-GO1OvEJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم: آموزش دانشگاه‌ها در سال تحصیلی آینده حضوری است
🔹
نتایج آزمون سراسری در نیمهٔ دوم آبان‌ اعلام خواهد شد و به‌همین‌دلیل دانشجویان ورودی جدید با تأخیر وارد دانشگاه‌ها می‌شوند.
🔹
کلاس‌های دانشگاه‌ها در سال تحصیلی آینده حتماً به‌صورت حضوری برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/457487" target="_blank">📅 10:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457486">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجار کنترل‌شده
در سیریک انجام می‌شود
🔹
فرمانداری سیریک:‌ امروز احتمال شنیدن صدای انفجارهای کنترل‌شدهٔ ناشی‌از خنثی‌سازی مهمات در شهرستان وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/457486" target="_blank">📅 10:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457485">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f0759c5d.mp4?token=jHGUCLjVi8jSMlYRi5qdgeXCFdivheuu0s0hRhp-FtLABY-P_tVk7Zsvm6p0qTAI_gEjmJ7fVITp3g6FDczWc0GqbzfxC58WazBdAmXHYmVsoJHOMLzyYgV1k0L7si1snLznSiTEaDCRddHkfhpszzddUZt7to9VAwFD0hq-ZfakZIHum-b3Gud7Hr7n2cuWHMw6CGmMi_YPUh0GGX99U8Pg6CXpTYLtPK3ZINcN7-QkZHYeiOAZEYXqgeFhO8oH9PI2kPVhR9x4qBApR-A4_yXbZ-3vnM7YvGUYLBAN_huaQ9DXz033Dn02vgr0s5WHgeu-EWR8_5RLsvIurM9Z5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f0759c5d.mp4?token=jHGUCLjVi8jSMlYRi5qdgeXCFdivheuu0s0hRhp-FtLABY-P_tVk7Zsvm6p0qTAI_gEjmJ7fVITp3g6FDczWc0GqbzfxC58WazBdAmXHYmVsoJHOMLzyYgV1k0L7si1snLznSiTEaDCRddHkfhpszzddUZt7to9VAwFD0hq-ZfakZIHum-b3Gud7Hr7n2cuWHMw6CGmMi_YPUh0GGX99U8Pg6CXpTYLtPK3ZINcN7-QkZHYeiOAZEYXqgeFhO8oH9PI2kPVhR9x4qBApR-A4_yXbZ-3vnM7YvGUYLBAN_huaQ9DXz033Dn02vgr0s5WHgeu-EWR8_5RLsvIurM9Z5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عارف: دهک ۱۰ درآمدی ۲۳ برابر دهک اول از یارانۀ بنزین استفاده می‌کند
🔹
دولت‌ها آمدند و رفتند و کاری در خصوص قیمت بنزین نکردند چون دنبال دردسر نمی‌گردند.
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/457485" target="_blank">📅 10:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457483">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f74ef4bc95.mp4?token=tOXUw1Vgx_ZRmlYfg0d-o1gRdTPJyrcJBU7RppNYRi37vU9vteWrTv8XUk5tx40eGrWSVxQN6yLRHhLpLz3wFjJc5J10vVobDvFAM7pVKi8ohHN7iLTwOTsH-HDmh76JLw7BC5RlVxPRS-NIiAnCxl0ur5cPnBuUeYxKk0MpY3ZoDihGPg4kHt6lWLNvHmereGVr03Ij8IjWLDV2SprtbSgzKKGocGAwRH9k6b546q9VNHbJ1iw2Sy76ltnDN76QWiE_ZbaIfquEgyQEMXMqCKbZrVDxtdNJsd5LR3W-eImYNigiBZPmQaCinXMRj_RGtk4fpA2vJAlpAFn0ybmE0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f74ef4bc95.mp4?token=tOXUw1Vgx_ZRmlYfg0d-o1gRdTPJyrcJBU7RppNYRi37vU9vteWrTv8XUk5tx40eGrWSVxQN6yLRHhLpLz3wFjJc5J10vVobDvFAM7pVKi8ohHN7iLTwOTsH-HDmh76JLw7BC5RlVxPRS-NIiAnCxl0ur5cPnBuUeYxKk0MpY3ZoDihGPg4kHt6lWLNvHmereGVr03Ij8IjWLDV2SprtbSgzKKGocGAwRH9k6b546q9VNHbJ1iw2Sy76ltnDN76QWiE_ZbaIfquEgyQEMXMqCKbZrVDxtdNJsd5LR3W-eImYNigiBZPmQaCinXMRj_RGtk4fpA2vJAlpAFn0ybmE0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آشوب در جام‌حذفی آلمان
🔹
دیدار تیم‌های فالدهوف مانهایم و کایزرسلاوترن در مسابقات جام‌حذفی آلمان، به‌دلیل درگیری‌ شدید میان هواداران و پرتاب مواد آتش‌زا، به صحنۀ آشوب و ناامنی تبدیل شد.
🔹
در این دیدار ۳۵ مأمور پلیس زخمی شدند و ۱۴۰۰ نیروی امنیتی در محل حضور داشتند. چند هوادار هم بازداشت شدند.
🔹
فدراسیون فوتبال آلمان اعلام کرده پروندۀ حوادث این دیدار در اختیار کمیته‌های مربوط قرار می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/457483" target="_blank">📅 09:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457478">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CO3dnvgN9gYfuiYrUAFPzmLtDFBT4sbI1C8KghsGqITViYFOTqrHIgzkEMPS5UMM1zACmmgkmqurj00QHf7WVp7SWfnbChzQhDdbKp6LnlFYU6EO4U77tZZFtc-lyPOJR3K_RWxNUZq0tCwVPbRAWgNaw4Hv6lPLTMMkONDO2t8tImcjbWsObHvyghbGeLGNzK5yfAe_U8gal1b77r2ZGHpRoddNTozLr2LlU6e9yD9TXQoqamKPwgLXyFRwi2BCod0wkPHua_vBbzu6UrPZPNu1qODk2j1MVTPl0E8o61kYS5C-EmZ6SDc16AHCu0Fu_d0uD2reInU-KfPHqiaCXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMfvqHLRl12ap_R73zn96SkvZ2f9aNvgG8_e8Z9tGGw6m41LqCvPu_SLW_X_8mfhoJSUnLj1yc3GKKfT1Sri00NlM2Wwg0Q2FmMwKrVeVbnBBLSqUIbKAx937xWmRw7fPRDqPpQjSYZktIQrd1QixTkUdZwaaa9wTsHi0xbGaRrhJrSGIXV36tfZfCIlD4SfDQD9pP9Mb32sjIc6rXhjbijH_0nVeS91tQ8S8c-I50GYeTOWIXPFvegM9xv1SgXrccVBAhNAxobEs6JZXO_oUwg94dtuWodXtwxLzSbdu6vI1TOw_uxvarVyxNahTXVWFoeB1qB6N0q9B9wECyB51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNCPBfryxN94PfFY0W-G3hCUfoeeb1WSesSCDGt1Ad_satKx8FyrzCvBYdYtIJJCngODWSLzbTx6VMmqx1iqiicQOA_ADNTwGan8druJWAQPdDwkrct5CTmBBjYsdbcxjAYqCJQYiKA-hJd1ExDOiIexaXV1GZhPcjbeIwiUiHKTjneZTqXybXEAFRori45DDmRJRkcTH7v3MPOmMghVyFUSZ732zLs9C8GTwRfDrowCcZnv9FHeR_jaiS52pFlE4y5sXm4Q-SJJzqc9KPQGKuVY5kn8X1jPGMBaE6Ra2uZHvC-KJ2fglB9Vh8r2ZavKYmLbjPhKKp6grrA5YacIUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lsQiLDrQHZrW6-BvDtC4RDR6w58gz6DpOB7tgGXWnRrWyiA5ThtnZy2XZXaZTubAvE8XpeLk33urEpj3Laxh43tBDnfR75Nv0ujfVKJxgbA3BdN3z6sVyaPZ1FqeuuglLyo3_7Qo87FzMVzWUUowLTaO75ICirV5Pkquw41rHF8AhzoO7oaVl0wQlYZ6D6v3KwwzMy9VQ3B8fBiYeM7oyGWsExEA6gSnCXoEGFEvGphjUjCdqgFW5UiAaUPbOt1KjmCyeB1T7dZ7RGMf8inOH7ldCQTD-NWnuijVa5EbG-MT2mx6D1bBvb2YGd4DGI5Q59-DwhgjZQG6UJU7ieBkTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVam5CdqjgnPRce7dRqBXLfB8ViZJya49H7pk8uEQcZTMNR9lGMd3m7CfGfm_PUh7fo5MnoyRvfMZW09MmofFyeBThBfOhQriEK3kelSFr72YYcMcMdoYy5Z8APoYBFSuAgMAR-4ppmSsaNLKEip7PVSyQ7Z46-Ua054qKu5IAuUVfz_sTPhrTMLRe_0SSE9OXrT4D_tq4hkODB8NKJtaUP89SB9J0WnUGBodpmAvs1FnjPDBYCMypDDmXKfeb8fwGhnOl8DzVOtlqNh1gV1B9GIYijt4Wo6wJIGwokn3lNjtqpJbnUttEV4rgdlfA_c_2VnrzdaAbDSgxf-iwN1Aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
طلوع آفتاب روی زمین اردبیل
عکس:
سیدمهدی پناهی
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/457478" target="_blank">📅 09:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457477">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxH4BgLTnXgMYHIFlPiwPnaPCwcKu8jeYpQhzHurTo-v4Im3lnao6hm8KRoJq0rab2YafVnRWcE4QnLMpfAWynj8zHNog69-OhJWSZrwda-T8zcjXTAzaEpMXojIBq7sz59P0uZ-_apaM62lUSYPa3hTWtcFIoI3atou13t4TrTvrGFyiJeAWRSHfEm9eOTjP4AAimh2wJOB9SjcmdpblzKM0Mr29NMuiIV9JgoVa-sSFlsGHuWJla5jkD9yIfXQ5Xjob0d1ZsyQLHTIokft4kLw1yjIsmVNsif0HiD6sG8T-TAm7yos7dicPYgHdKZXgmxxTNqVNaaJdoQy_z86jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ کسری بودجهٔ قطر را ۲۰ برابر کرد
🔹
حملات به تأسیسات گازی راس‌لفان و توقف عملی صادرات از مسیر تنگهٔ هرمز، اقتصاد قطر را با بحران جدی مواجه کرده است.
🔹
کسری بودجهٔ این کشور در ۳ ماههٔ نخست ۲۰۲۶ با بیش‌از ۲۰ برابر افزایش نسبت به مدت مشابه سال قبل به ۱۰.۳ میلیارد ریال رسید و صادرات ال‌ان‌جی نیز ۵۴ درصد کاهش یافته است.
🔹
آسیب به بخشی از تأسیسات راس‌لفان، توقف صادرات و کاهش درآمدهای نفتی، دولت قطر را به کاهش شدید هزینه‌های داخلی و سرمایه‌گذاری‌های خارجی وادار کرده است.
🔹
صندوق بین‌المللی پول نیز کوچک‌شدن ۸.۶ درصدی اقتصاد قطر در سال جاری را پیش‌بینی کرده و برخی تحلیلگران کاهش ۱۳ تا ۱۴ درصدی را محتمل دانسته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/457477" target="_blank">📅 09:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457476">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb12YjodUeuSBHqj3_btxxK3FW7e8PaeCPgjbTqla6ewuJ-VrUibHy_L8I1-MEfOc5nkCplXleHKPOvRQMhyyenjeHwxwcqmekuFmqjBDlL686JVKhRQkG0_DJWLZ8PcrR48UZ_pJeimyMDNrvXBO99mAsnk5fk29sEHWsqpBYvH3uSyY2n3k3uHSucLfFe_lmV5FrHXmjcMndzPJ8FjWjtC_rdxvnc7WXzVbxOEVs6h9JvdQcitKjkgRE8pfevumWRbFrbwVpfZzBRmZutlSk56ujFnni34629EeFewSs9nzGLba-kiN_y4f8lw6K8YbcJ2_pjZnXfFBuFJgl-ixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقبال اشکان خطیبی از افتتاح یک نمایشگاه در خانه هنرمندان!
🔹
افتتاح یک نمایشگاه در «خانهٔ هنرمندان ایران» با استقبال اشکان خطیبی، بازیگر وطن‌فروش همراه شده است.
🔹
براساس اطلاعات درج‌شده در پوستر، این نمایشگاه با عنوان «سنگین» توسط انجمن هنرمندان مجسمه‌ساز و به یاد مهدی سلحشور، مجسمه‌ساز جان‌باخته در حوادث دی‌ماه برپا شده است.
🔹
مشخص نیست برگزاری چنین نمایشگاهی در مقطع کنونی که با استقبال ضدانقلاب خارج‌نشین رو‌به‌رو شده، با چه منطق و انگیزه‌ای صورت پذیرفته است‌.
🔹
انتظار می‌رود مدیران خانهٔ هنرمندان هرچه زودتر در این زمینه به شفاف‌سازی بپردازند و پاسخ روشن و قانع‌کننده‌ای برای تنویر افکار عمومی داشته باشند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/457476" target="_blank">📅 09:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457475">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_kUs1-knHBKRmTi5L_68VUMqVe8caKxqkhcUvVM4taWqUyUOgqHjD_HfSlXyd-UWPKVc69ALPlDousSqbHFRtp2zZi8bjzIN0Yny0M0crVygmth3peDhYyVPrb5WwsR-SsiARdhLCM9hn-7MTtq5hlkgriQbLTmBZMa0S0v6DQq_7HLRQoKvIJUC4mKotkX9wI5x8n7eJF0I8T0MuabP5R6Q3XLnx6QetBll2bSDNv0Tw8pifTH5ilionDON6dmZOCpxyc6Q7Qd3RaGgQ_hOxUffKYWh3P5RzoV-RRQaIHL9Mf7A26olUH-brXIC4nhCrC5O_6IG8txopFsQdat4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۶ میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با جهش ۱۲۰ هزار واحدی، معاملات را در محدودهٔ بالاتر از ۶ میلیون واحد آغاز کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/457475" target="_blank">📅 09:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457474">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAJKG5NpialVpQ9cU4Tr0zHDdcXWM_FK6LApbhs1wiEk3M1V0lQIWbjcoNsvXxv06suOD-SB_K8vZa6DTia1H3wg0YbfzOBZRwQVm0_h8GUuUeB8N7VASEt67UOwZfB3JID38OTVnH-68ilduXVeV-i6trnbQpILDPBySWEnHn10bF1bH6KHBB7w81Ce01FaSEVW7D2DH7uzijwwLKJjwhJu4hDR5wLHlFHpYHk78C4_fVSjJcBbHy4TUTeGJnU1DWjDqDAgX-Fk17DQkmU5QxvPMn7fOs3PYE4HTMuFP76Sf2adBtQRTwymQUD8pZAFSrz4g0QqL-zhjXlTLY9Ijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ‌های‌ جدید حوالهٔ ارز در مرکز مبادلهٔ ایران اعلام شد
🔹
دلار: ۱۵۶٬۷۳۷ تومان
🔹
یورو:  ۱۸۳٬۱۲۸ تومان
🔹
درهم: ۴۲٬۶۷۸ تومان
🔹
یوآن: ۲۳٬۳۱۵ تومان
🔹
روبل: ۱٬۸۹۰ تومان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/457474" target="_blank">📅 09:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457473">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e447bce38.mp4?token=nX4i1wC_51UTy9oeclbICS3hHawZ2qDK8gFLsGcU9KSMByuV687H3OTkuBidIIfVUEHHjsBKYHgU-EM6oy4jsjGV1KZo1VShHDlStQwoLWci4gm_wZcb2wUvUKZ-gF9LezheN6Ot0X6HDl8XP2Rl_xlH5WUeL4JaTh2UZNfzll_pYvJhXeA7xqqaIlY3yA_VTNsdjKziA9WB1pDoAZISzmmWHCtVtrX21fKdgvrFEDLd6Na2Bqxydhz7S8vaEXg13Be4brZCyS5pgB370Cc_uMWZq8I62LZufzmwMaulFdExKNyZI_ElOS8GmoEDmAvfn__s-99EjHtj1oCDV35QXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e447bce38.mp4?token=nX4i1wC_51UTy9oeclbICS3hHawZ2qDK8gFLsGcU9KSMByuV687H3OTkuBidIIfVUEHHjsBKYHgU-EM6oy4jsjGV1KZo1VShHDlStQwoLWci4gm_wZcb2wUvUKZ-gF9LezheN6Ot0X6HDl8XP2Rl_xlH5WUeL4JaTh2UZNfzll_pYvJhXeA7xqqaIlY3yA_VTNsdjKziA9WB1pDoAZISzmmWHCtVtrX21fKdgvrFEDLd6Na2Bqxydhz7S8vaEXg13Be4brZCyS5pgB370Cc_uMWZq8I62LZufzmwMaulFdExKNyZI_ElOS8GmoEDmAvfn__s-99EjHtj1oCDV35QXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: امروز در در ارتفاعات تهران، البرز و سمنان باران می‌بارد
🔹
در اغلب نقاط کشور جو پایدار حاکم است اما به‌سبب وزش باد دریای خزر و عمان مواج خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/457473" target="_blank">📅 08:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457472">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌ بازنشستگان تأمین اجتماعی امیدوار به جلسه با عارف
🔹
پنجکی، عضو هیئت‌مدیرۀ کانون عالی کارگران بازنشسته تأمین اجتماعی: در احکام اعلام‌شدۀ احکام بازنشستگان تأمین اجتماعی گفته شده ۱۵ مورد باید انجام شود، اما هنوز نگرانی‌هایی دربارۀ نحوه اجرا و پرداخت وجود دارد.…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/457472" target="_blank">📅 08:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457471">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c72a6e41.mp4?token=TGFupkelzs1FdLd60IhLDuUcbW9y4DLugOS90aHWCO8ynaaPGBztGaMFAEA7T3StRZlJuJ_qMG3nfnRQCuQ7d2rPbknZRp5YlAEIFCoef-m-f3SvvuOO4gJZS79YZhXjzyD58sPFr5n8qeQOaDa1XGQjafI2-8_sLxM23sn66GnI0IJfvwJb3l6X2tRVqRmyBmQFteLectXzTS7ME1SJK1Ind-qSC2mBbavKvkjUGPDDA2QvQtveAuJXa617Wqet5razCoFFAudFRP6baNaW-HvsHC1s2HjuLgKD0uBBgKRhNUui7hAjutojmfoIUYKqHhdvydN4R0yqiFpZealvFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c72a6e41.mp4?token=TGFupkelzs1FdLd60IhLDuUcbW9y4DLugOS90aHWCO8ynaaPGBztGaMFAEA7T3StRZlJuJ_qMG3nfnRQCuQ7d2rPbknZRp5YlAEIFCoef-m-f3SvvuOO4gJZS79YZhXjzyD58sPFr5n8qeQOaDa1XGQjafI2-8_sLxM23sn66GnI0IJfvwJb3l6X2tRVqRmyBmQFteLectXzTS7ME1SJK1Ind-qSC2mBbavKvkjUGPDDA2QvQtveAuJXa617Wqet5razCoFFAudFRP6baNaW-HvsHC1s2HjuLgKD0uBBgKRhNUui7hAjutojmfoIUYKqHhdvydN4R0yqiFpZealvFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرونشست متروی پرند بازهم به مرحلۀ هشدار رسید
🔹
تصاویر جدید از محدودۀ ایستگاه متروی پرند نشان می‌دهد که علی‌رغم گزارش‌های مکرر از اسفندماه ۱۴۰۳، فرونشست زمین در این منطقه شدت یافته و ایمنی زیرساختی شهر بار دیگر به مخاطره افتاده است.
🔹
بررسی تاریخچۀ این اتفاق نشان می‌دهد که پس از اولین نشست در اسفند ۱۴۰۳ و انجام برخی اقدامات بتن‌ریزی از سوی مسئولان وقت، هنوز مشکل به‌طور کامل حل نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/457471" target="_blank">📅 07:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457470">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ادامۀ تجاوزات رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری از حملۀ هوایی رژیم صهیونیستی به حومۀ ارتفاعات «علی الطاهر» در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/457470" target="_blank">📅 07:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457469">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjI-w5XyZiujAW_jpFTxljMwBNjYXb4a1yjIxh-xWDMi_LiNWMSOPDiVc7QoGXO72r6lsR4SjSy96OCFuVNn0uWyB5wppAj2cIPt0SSD8nskH5KOWiBOX48WXU6lNeN6bTT-m3ZhEM4BkdBENhByFHguiuX9VF5-_IQnZKHZ03Q4V27YyclpIzEXBocV4GSIjv_19A9_30eGfyA5PjDqZgV6I-x5ob0frbkbrld9qvo6o34zv4RI6ziocsN9tezOGgmS1PNHpOkOevs5Izc_lgyQi7_Lp91GDx5aXBkS8V-w93Ocm_J3tRETDLX-YrMs0UTA2bcDfFdJqi6X-pWA2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای تهران در مرز آلودگی
🔹
شاخص امروز کیفیت هوای پایتخت با رسیدن به عدد ۹۹ در محدودۀ «قابل‌قبول»، اما در مرز وضعیت آلودگی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457469" target="_blank">📅 07:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457468">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/770e065149.mp4?token=n6Q8ooKTSCLe0sPfCzzxc12i5P7F2O5rUyi7ges4n2tfB1VI6HHElIvQRxk763npIZEWOJvlrz3ruhsYh9c9BbNpPVPlyHufGJgrAzvJ-ST6CMVUMMWxYljJ1jEDc9gsue7Q76vcbCG57KttQa4L90Mx8RupFyroILVjbDPGk5aJJKlBEpzb0-p-uAxSC5p0k7rnKUeVMriEHRjIEeWTYMIl9mQujF2O9InBRXdTpjP6nEkEATAy7hIPQpjX4km6LHXiIBVbxBLSZdOf7dETEg9BGkPCGyOH6IYD_dBQvWZB_a61pNaWoc6W5I1HoYrTm1Dgxm78DXu1_0DaONFDhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/770e065149.mp4?token=n6Q8ooKTSCLe0sPfCzzxc12i5P7F2O5rUyi7ges4n2tfB1VI6HHElIvQRxk763npIZEWOJvlrz3ruhsYh9c9BbNpPVPlyHufGJgrAzvJ-ST6CMVUMMWxYljJ1jEDc9gsue7Q76vcbCG57KttQa4L90Mx8RupFyroILVjbDPGk5aJJKlBEpzb0-p-uAxSC5p0k7rnKUeVMriEHRjIEeWTYMIl9mQujF2O9InBRXdTpjP6nEkEATAy7hIPQpjX4km6LHXiIBVbxBLSZdOf7dETEg9BGkPCGyOH6IYD_dBQvWZB_a61pNaWoc6W5I1HoYrTm1Dgxm78DXu1_0DaONFDhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
و
خورشید طلوع خواهد کرد
🎙
رهبر شهید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457468" target="_blank">📅 05:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457467">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5287b866a.mp4?token=LQ5wF1FccNFSohcP7cLrinDrzrcqOcAjjr2Q-aJff4Yvee20rlyMmpxl7voO955L4nPJE8UeWlFuChgOYGiOeLCNcSUZ6yB2izuOudDaYi35JCdzI8OS9beBTy83LlB1MtaTjv_wAAW8tmvVI-4EsUccr8cJMMlGj3GedbNMbfvEKmQZuwW_8fkuQ1IjlOvm9mEuEXSOrW5GMb1_BWL8MXnd5KILTMwQNJWP_tEp_le_wUhi0lvjGdobpqbew3x_d3DGLh-6zsXt6bFsbfuGt44TeCgY0x5vSIwvLi3hcHAHGKWUVIOxsNWCe6HQ0ikHAN3O9GgwUdiLeZMn2kQLUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5287b866a.mp4?token=LQ5wF1FccNFSohcP7cLrinDrzrcqOcAjjr2Q-aJff4Yvee20rlyMmpxl7voO955L4nPJE8UeWlFuChgOYGiOeLCNcSUZ6yB2izuOudDaYi35JCdzI8OS9beBTy83LlB1MtaTjv_wAAW8tmvVI-4EsUccr8cJMMlGj3GedbNMbfvEKmQZuwW_8fkuQ1IjlOvm9mEuEXSOrW5GMb1_BWL8MXnd5KILTMwQNJWP_tEp_le_wUhi0lvjGdobpqbew3x_d3DGLh-6zsXt6bFsbfuGt44TeCgY0x5vSIwvLi3hcHAHGKWUVIOxsNWCe6HQ0ikHAN3O9GgwUdiLeZMn2kQLUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با تو در عهدیم تا صبح ظهور
🔸
همزمان با سالروز آغاز امامت حضرت ولی‌عصر(عج)، کتیبۀ شعار «با تو در عهدیم تا صبح ظهور» که شعار مراسمات چهلم تدفین آقای شهید ایران بود، بر ایوان مسجد مقدس جمکران نصب شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/457467" target="_blank">📅 05:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457458">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cVcieqdxoKCnNiuSmnK8ChkKRi1bzvAE-aQuITTIyahhY673eJvnGokdMeGOuYuqwNrjcrtDBqyTnXVAKRiOgGUjkACcq7zzW5yh1W6EW_cVaXcA7x35OQhdzJeqnxZ0TXfEMMF6oWobQSlP6gJi4O9ntqIAjl0hz2uAxZqXQ1OKZ0u0WgVlcB9vVRrj3kqrJia9cWUbQoWOw3i6beBcKfdU8wa1YsyCZTnfSVvx9DZmkAsBT7iGn0aXk_EUOhpWt1GXq4sSiKwG1GI3KlVdAh4g4tscxAxz_ilVb4pAQ5_RHEWEtV7ybCkRbPHO54p-I9FPtQ2BqgVxNjcegEIB3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v6PWgPa462FZ1qFRF9WNmg072I4UIs_888E-EC5mF4iLiYKCyn2i1JIbX75faAIAuky53EBCb_vxytINARx2gj4zcxdhAoTVZZ46wgW_va3RGxZ6byX4eQ1NtWHUs5UldGXYyZy6C9Wu_cEX1eFA22Pyzhb8_nc7G68zzSstKcFF2zKK-F5dDFHysGLDb6AVF0BMCUianlzLv6nHcvv9KKLctcJSsu85nOCWPaBjO_VHJsQgn1VftEXlZ5MzGouqGEEAhGDdk7X-9wZPRuRrzAPWv9sIqREFYjCMTriKsgn4p-iXgicn53FWD7ocRYT3mcR5mHm5SQbe2Jflk7SRAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gjg5RCrq2GF5dLRvbGYKmuYQ52HidYHydAqqUXbdUoauwpn2_WmL_rQCOrNmCNqC7mKxmpYop8TU8IBLdkI8W1UORkhyjd1TfncoC_WKorHiic60ykQ1VwOcE13C97KJR_S1fceyPlKsk_INB8buRr6qucy3f0_FJkbLMV72YAG27sCjJ4WHRckOBKIAbZWIZLj1m0C68tjk_B4uihqpyJoYLvnxdZ9YTRtzTeY4bfsm9okfB3O_7qidNt6OMAQEiQ3QoHOYmwTBIuYI2jwDoxIFAuXd70chro0T_PhE8EW0I6L9f_VGMPlvIHZZT-fYWZG9diLFOGmwIYYorjo9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RDJNIxE80g2fZmNhT-P_BGskLQR30Wr03vGLqxvKVyJYdJnEcd3e300akNhwoLcu2vGbQHfslvq--48ee2NSIhgBZEoG5fyiXf_jhrh7HRuROxL_IZtBjb75TID4qTJ_khGCLJMHpjz7DqpuvU0rdbDiAajjKQ96CW-yr117n8_7AAkwB3xLHX8mGlMbySgIq_n_0y5oPGFnBVH8F6syuhxnrOQ2EqpLlQpWdxV448CpQgZPczAc_27TiV3Wmkz1Rea_EZoh4p-Ad1I7NNtftFjAb9eJfRwqtbxf53iNqeKBnBtfkTjDTE_-b0HJAc8iiu_gyGzfcoBYXyuFm5l5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l9hwDM34aQoMSFtpGP3TNHdFHuAz6EZ_LawceY5ZtgI-x7YQ46D9wxQp4VTpyXeddTNijqQrFV6FhJoLGDK4r5z6DrNy2GdqEbCiZIiRvv0aBWUK2xxIxNhdCmyzIw1Oi6AX65ZKng_f33n5aR6_-c0lg_bgvVuRArnFW82wzyBg6LuixbEquzoxgMf-EualfExco47GPzxWkF3zLe8du58O3J8uNQGxWXro3hXySCsWnNKN3DISTFAegt9qIv4D2xw7HHw1j_H7CIo5P8lgBYrwM7SPcMPwPKOP0nALcf7HTqLX1D3w6z4m0gdZw6sGDLFemn4IwF9UP3UTRJrL1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCeZ5Fcypyt0wu7UNrErYGB328vHrxaw9jp3fNxmfRc3Xq8bOJYD5o573e5Z4L5p4aEAUnsG3LOuFpxOCm4YVxrFccOSNw3XxMVDa7tiOBTnCKcOMKm0I_09FQuUlY9fJOlHkY_bPRyv3RumQm74WBVPjSdWqpcm1jalYd6TSv5k_7y4brwNfTXPGI43cAng-ZH_ac8W3TTMG_1Wz4o5Z8wdjri0g_RMVC9zr-T0t5Iem9lHu9p-hM4SefBq8yNHV_xjb4N2_ditdl4x9uIHKmpfmaV4sb8Bz4zKiAKlgf55UNqovUfExnsx-Bldznfwt8PwHitidzSITzM22xeuZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VeYdry-pXxDx6N1xlg0jqYgG8uRXyccL02SGZGDyhWns2EQT48nuMImRJPyeOT8y9Beg9YxFv4JdrljGeG8421M0oM0hLdU6IABuVrHuA5AsrNy9fMuQmHgOQjlvjWvUZYJfaxbzqUCe61mQqeC-8xy_1v2BhGLS0Mq8ytSCYnRfaaztO1HHWGlR0y1_GiyPq_RNTbuLHpoy-fYrFL-xGVpV0SK4NaaGPHe_7VOn0ZH1pPIafpk-OgsXoNeXDxHPaNgErtBIlaOzR9IYGdlzwTn6BgVgZZ5FryudONxVuvudevfu2xgzlqF1Riw9vMlkOPHUtwjVomg0n6fRzrqz6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIAZnPHLLnOpdhYbhOai9hQBkSW4ExelH5voYjsKgVaASGzeix7Wpi05WbxlrDLDpTWRdjYK6u8O8wKi1P7mi6reavSkvHhlpRt97h8IeDiUGf-LSdosst5LXCTjnpNCNr7kHokkkZ5-yl-OqT7YS2_bxrdvqGmpUhdyBEG-D7a51YHWYBAG7fdTEZSMU9tLIc9_1sHegRdd98XiU-JInpvZS_XHxUNF5PXbX8jrEH-ffv--16pspz1J9eg_FIgGNviLoOgsk2Azifk_IuF-ZyHl8Nsam_wifSqJEZl1IKxh5m5kc36vEclmXEHPCvfCCjrzkzxIpCoTljBBGwuRZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BIbCbdpkVAgNNzScDmeoyllTe2UJPUCMF0eOgmfwMDzCVQTLl9mxTJoEp6dFiHsS5KHOI5sQ0xl7lwVGUqEDhO8-8_TI4k1hQzbFSB_b_4b0KfMA93tqVk4AnzBA7sFPObPu5GgP8606VxfPr0j3bfq-Vmnm56F_xLxWqlLxZ9KceV2NVvSgjVHdFlv_n09-dOCr0T33ulLZ88WJuSxRz8gkI0vCc9D25DjPd0OvzjeMTRRHC_WCsXXu3IACIWzac_SFOJXSvIAnfE4Vv11DQdo_4pvS5l_iXVOXZg4NjA-XpjC8-zFrwysPC_wt-U_mHSCgl9wbMkxpHUS0CT8pSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عید بیعت با امام زمان(عج) در میدان حضرت ولیعصر
عکس:
میثم نهاوندی
و
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/457458" target="_blank">📅 04:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457452">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpdynWFx7LT3e_-faL_pf2cp-HOHONoaGS7hNwSpOZN8jrNY58nDGEQsnIEATjwMwRAkNx8_eDtn-4i2x2cn-34NFEF1lvA7XbhQLtbqRXVziJkEP4tZe7bjz5q-MtInTH5QCcYhrI-S8MyTL7-1XsLLxk243jbnXx9cicrFLlL02HRjeR-JQU9atXGLZy2Mwbb4yXuFDlYodNvgC3qtoCYsxGUYoeE6uwHZZ1eHmGgBkESA-OP2gBxJ4AIf_UCKrroqPjxpQtt5NK1JUxieD6uSDQex-EXtSrwqCGpIGC2C_ZpeS9BnpsRcjWuO6Jsn72P9F9DBQcgBs2_1_Yh2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: جنگ اقتصادی آمریکا علیه ایران، نقض حاکمیت ملی همۀ کشورها و اعلان جنگ به همۀ دولت‌ها است
🔹
سخنگوی وزارت خارجه: اعلام تحریم‌های اقتصادی جدید آمریکا علیه ایران، بسیار فراتر از ادامهٔ «جنگ اقتصادی» غیرقانونی علیه یک کشور واحد است. این اقدام، به منزلۀ تلاش برای اعمال حاکمیت فراسرزمینی آمریکا بر کلیه دولت‌های مستقل عضو سازمان ملل متحد به شمار می‌رود.
🔹
هیچ دولتی حق ندارد بانک‌ها، بنگاه‌ها یا فرودگاه‌های خارجی را که هر یک تحت صلاحیت انحصاری حاکمیت خود هستند وادار کند از تجارت مشروع با کشوری ثالث خودداری نمایند.
🔹
چنین تحریم‌های ثانویه‌ای هیچ مبنایی در حقوق بین‌الملل ندارد. این تحریم‌ها اصل بنیادین برابری حاکمیت‌ها را که در بند ۱ مادهٔ ۲ منشور ملل متحد تثبیت شده، نقض می‌کنند و ممنوعیت عرفی مداخله در امور داخلی دولت‌ها را که دیوان بین‌المللی دادگستری در پروندهٔ نیکاراگوئه تأیید کرده، زیر پا می‌گذارند.
🔹
ارعاب اقتصادی که هدف آن واداشتن یک دولت مستقل به تغییر گزینه‌های سیاستی مشروع خود باشد، یک جرم و عمل متخلفانهٔ بین‌المللی است.
🔹
وقتی این تحریم‌ها با محاصرهٔ دریایی که خود مصداق عمل تجاوزکارانه است همراه می‌شود، حاکمیت و سیادت سایر دولت‌ها را به امری موقتی و مشروط به اراده و هوس قدرتی دیگر فرو می‌کاهد. تمکین نسبت به چنین ارعاب آشکاری موجب مصونیت هیچ دولتی نخواهد شد بلکه صرفا به منزله اولویت‌بخشی به حاکمیت بیگانه و اذعان به سیطره یک طرف خارحی بر فعالیت‌های قانونی بانک‌ها، بنگاه‌های اقتصادی و فرودگاه‌های کشورهای دیگر خواهد بود.
🔹
نتیجهٔ نهایی این وضعیت، فرسایش کامل حاکمیت ملی به‌عنوان اصل بنیادین نظام روابط بین‌‌الدولی مبتنی بر منشور ملل متحد خواهد بود و مقدمه بازگشت فاجعه‌بار به استعمار عریان و تمام‌عیار.
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/457452" target="_blank">📅 04:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457451">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ادعاهای تکراری رئیس‌جمهور متوهم آمریکا؛ ترامپ مدعی آغاز جنگ اقتصادی علیه ایران شد
🔹
رئیس‌جمهور آمریکا ادعا کرد واشنگتن «خردکننده‌ترین عملیات اقتصادی تاریخ» را علیه ایران آغاز کرده است.
🔹
ترامپ با تکرار ادعاهای همیشگی خود، مدعی شد نیروی دریایی و هوایی ایران…</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/457451" target="_blank">📅 03:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457450">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0e5623d2.mp4?token=ZEOo9Mo0aPts3JvWla0qIhlJ7N4EM9U_8N0utzLOZ3_pyYP0_h5qNUgV3fNRtMT2VkD_xae1_RUHxonkKs2utEZaTQ3sE7XvZU6jiNzz0UVzxXD3pEVLBNPqOZaV4ERJnozp8_h2j2BPwKNTlYu5TK53kgGvd5Cy80TQZcWFo5dJ9sVYuvBTc8XCHB06i8BDP8t9ELLsAbGb5Vy9uFOvXwuTRyXg3JYxepGNRNvW-SC-L-0DTetFUKZniFYDTVcZX-VtoZhI4gf17GSA1rpGn_rbwXt2l3fKb4Di2otIbCJ-AKNZOCKnuArRCgFEZIGnpLClz7uwFVvI_-OOaA1hj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0e5623d2.mp4?token=ZEOo9Mo0aPts3JvWla0qIhlJ7N4EM9U_8N0utzLOZ3_pyYP0_h5qNUgV3fNRtMT2VkD_xae1_RUHxonkKs2utEZaTQ3sE7XvZU6jiNzz0UVzxXD3pEVLBNPqOZaV4ERJnozp8_h2j2BPwKNTlYu5TK53kgGvd5Cy80TQZcWFo5dJ9sVYuvBTc8XCHB06i8BDP8t9ELLsAbGb5Vy9uFOvXwuTRyXg3JYxepGNRNvW-SC-L-0DTetFUKZniFYDTVcZX-VtoZhI4gf17GSA1rpGn_rbwXt2l3fKb4Di2otIbCJ-AKNZOCKnuArRCgFEZIGnpLClz7uwFVvI_-OOaA1hj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم مطهر رضوی و مزار رهبر شهید انقلاب در شب آغاز ولایت حضرت صاحب‌الزمان(عج)
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/457450" target="_blank">📅 02:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457449">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Db7MOjATwXax3B-sCVWoJkyLFu97kvc3oxESqz9H_RT34EOmjkYpqoL59xtzHZzEbw1ozH3zARGkjPnYPAtFKhBs6T3M7rzcH7JJ7vkCDHjdJcm3BaW_OA0ADIISTOrqvSOpw2Bg2Mi4xAKMEMGTdbmbtr4awo-y5gkbAoH-VB287P1jrrm2ZmwH_JvsnC9e-62TgkTGM-2ZT8xKD4g4UdKHRueS3AX2dUtn69i4yWQaMwWVl7CBFAUXiuWDXuvGH83nW6E1jJ-w1IQdU_jdPC4lwWatrTLgUIJT2gtFgi9-MzDASo_ygfRfwPI63-O8hskEU7cjXlIkOzC6y2fJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر جنگ آمریکا استعفا می‌دهد
🔹
وال‌استریت ژورنال به نقل از افراد مطلع گزارش داده است که دن دریسکول معاون وزیر جنگ آمریکا انتظار می‌رود در پایان سال جاری میلادی از سمت خود کناره‌گیری کند؛ اقدامی که پس از ماه‌ها تنش میان او و پیت هگزث وزیر جنگ آمریکا، صورت خواهد گرفت.
🔹
با استعفای دریسکول، ارتش آمریکا برای نخستین بار بدون هیچ مقام ارشدِ تأییدشده از سوی سنای آمریکا اداره خواهد شد.
🔹
این وضعیت پس از آن شکل گرفت که هگزث در ماه آوریل ژنرال رندی جورج، رئیس ستاد نیروی زمینی ارتش آمریکا را برکنار کرد و به جای معرفی فردی که نیازمند تأیید سنا باشد، یک سرپرست موقت را منصوب کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/457449" target="_blank">📅 01:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457444">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MqwvNzT4Ba4ZyYc4Fc3BSnoKKnGeZgcCxJCCLZmT171LJ6O1ZsHCZ79VNpbDiYuudiUBvTRKl0YI-ZmsVwk4qKUKj9CWGGmwVVnSUa7WFZbj28AwsH0geap6B_D3buqk4PVMWgCX6EA2VHGEg6Ue1iou5-OG8J6UNphgQeygCy_HVOt4Q-rGIrcFwC_JgEkyByPBW8ai_dP6qXPc4urULzuenAZ7uKAthXsJC5rFV90Bzv4Pr_BuJEQFaKkeppnj3wLB_qsX538Dl5dLZ7Mpulej1qNARadQpI3yhl7XgWS9E7PFQkA-RAmNvWUIqzRV0kvXD0G9CqEc_soPpxIBew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pp4_yIi67cjNUKOPuJW59LH5P_ELEhlfTP6B563bup3hwfy8A16lMzPo_aWxoWM-WqJd0iWqa1wKM4I1_q1q1KG_k8Ce3mCuoiaxo8m1awNijBbvSf_nm9evsu0Fs0C6IUCHJY_b-9ltuCRLEM5VW8Yt0H8g9tKELJZTyXo9YIedA_BGZ5wW1gSJdOHDzFEeyf0g7kVlBUsVweyiEyAXjgTFa1BXVWIIBrgqlqPn5_2-cMEe0WzVZAlPZpm4EK6H6hfFLb0bLTCWzRQCfNtDnboh1ObSfe8wwLGKHoj87_F3ZzAEWV1BN97mA_w2-N9NNbbAfb719vEXN8j63-pSXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3mOlsQUeTjih6Qx34XqBLk_jGQ8d9lqC8UwDBZcuxSVtf5Qr-OVv-zoIfp8cmhO_aDf42L_TwxyGF4NzEFtDvUpkcO4GEEQ1V16RmDUGQswhB1EtXLswicBkA9WVTtmkAFIuIyzbM2i1rTYA7MA_bCNRZOdppi1FOeqhJI-PgOtcKl1oDOpJ2XaiqG-J15Ry2JAGk3Sv2rqaUqrnSsMzNgPal059-o7H_5gGeYhWTydQDYQRyV_fS11Mo6Q7Jv6n-IPKb-x7EVKCyJuVV4GGLY9P_4SWV1_A6xpWO11nFXY2DbTrb_W0xDMQO85SLsVdTOXm9SfE14P7G7Rot5Kzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dof_920bEgyVsc4opgyrAIdgNZVp-ssRU9i2Q8CkXXtHsYF7BRLbPymI2zesld9z9SJ_KEqTSAOD2shBYq8c5HRh8MXdkwjy_NF0OZLL9C3hGudAplvYH_2PiRUqKnxrtg6HCxcoIA6VuhW47Vv28Cnh9Jmn78_chvVyGXuSoHPLNrpSvqMFpNvkTTWO5VTMLSPttmi9pozfHXZ9CEQJBbXHfhikdOy5sTfEePb9tLkM9FpRAaUUHhnQIrBCmOdFKKP1WucJGbOg6yvjO2s1aq3vMBO5sBRYuwORhtdcojghXTjEaeLPHOg9pWsr060GBiN75D-nvqwSQVXX92ldfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwTFxvDxHnuKzZA-GGcTSrcYi9GWdm43v0kn8_tusa8_brHj7njYcqyeAcSvTd9s9yJqceWDhq4U2Y5wI8HkGQpqme2t7dPZxiyBW46wyrNjHfcGPGN0yDQ5Bti5Dk9dmxcbPncKRiKph95jZCO6q9gF76KDLSjjgFtZ42IhaRPV7WQdYDn_vwOX58spogMKM1ePfge024KHTrRrrXXJXLnVN_fsdO4s6vhbYmAJo1nzAw_3SXdeWFPOGhzoQOjiP3LvMH8enCFxqX9E5gPblrbx2MhzDKnVUgyTJNeeeQHfXGUyjtHiBfZnyk5TB39PKfM8vzlGJgDK7qkN7SIozQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۳۱ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/457444" target="_blank">📅 00:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457434">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTpaoDl8F50udy8lc7cxocJMw_XTAktAXNpjopzJ9iHCv2oyGmgoxh-4w2BN-X0J9ZbC3F1YaCP0vgbUxYd0mgAIY6SBkrOdqDqim7F1UrmffUNnA7el6uJIgbqwEL9skPClGhF2974KF3DsN7sm3niq2PeYRW6CSpD3CW7MUDhLIZvVoc1bry4bQ-UP8eWnuLbZM6zmQqWnS0zte5ic7TyUY6HWhmgBcWBkuEQcGSqxjdaumN-HV8cU7a4bDTYwKTYjQvuX23Womenq_99Bgh8qzewX09YL_x7SIyUUxtgWGj0qOc_TWdmgnVe6EdYmBiac12U2ZfNyv8_wKFHzvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKxwp4ekRG8DkgyqmK9sB9rI3BJ69bFxXlYWiQ_A25-JDlpy9z7A2N-883c1C0XqL0j7rpx_xwSCh8-wbqQEy37EFuJWys5PKtbyJGalS1XWwHgZpBHGikpGMfXoh8zS0HbsZjQhF1o3wupkYvFC3mXJx6SgPtX6gddXUBr9sHeFE2opXWzG4neKP673-uCXBMCx7waX3TfLtdUtVLPv5iwvtt6Pg_bKHAqkgc5SG6AH7qNPdobTLUqkT66Flf699AS9GuD2yyHc5WXl32bCcJ9n8xTTeilexFARVTc2AUCA-UU64u3jgp1b1cF-Ic1efumNEXpkCO-G09cSxZtOEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNdZWFTGRvTdeIreT6qjA4bjR4ndoMaFjXTbeZCeY9myIdOGC1X6NMok6LHwteBGqakMob734J692T3SJeiTLwvvrs_lZaduqCC-uGfDcnaNr8eFFnhwy5Ek8VyplVEQBvGYEE9JhO2ld8DWkxZSp-WW4lM6_CHgKhVLhBE3D2lk13fHT8ql-9nYOMvHnm_r5Wp6vysUZaymkbRCnVjL2SIaDQ8PeTi-OAsTrio3yg5OGNo0azukquvERcqJ8BNvcT6Qz1NaNIJmfBvnH_3YuNBevdJSOOaFY1xzJEHyohDsmh8qaCmGcTBKMOBO6LQZz-vsMdBex2Ucu3JVWiUKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpCpsqPonLYqoVo-4ausMLnHU0X9lozXFq4v9hJ0wCoROmqbNyYlbSHkHYjsELzceBTviTeJ3BpalP8gR0yOC-klCMaS833oJKS-IkgxqVjX_zB7XsWjLQcno7-vBvvFmAbMgsEDtdYLAYDIzVeLeGPTgkBVHqOSabsfvyKTm9Y0X4f2y7ufFidiLpzH7_GuJGszQfmZYJ2MhGxALuR_JgFAKo8_hrdYYnkHyk5cHwoXQA1X97kdrpX85KTbno5er2sm6hFFnJ9nfMvnbxdOdLeHiEzvpElE2XZB56Uvqcvje6J_i1Q2UPBI5NOjhSMPyYKjWRjjLdMTV5i9ja7jMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AehgjURSY01Zk6-Nu4oO_49267QTYd_EwLkdRZaylwRgxY35z1-I4ycBCX1JdD3-qtxz2jIjn6K3lyrdlCE-i4XSivu5EEETC6FYJxgtZ-2sGQXfBYO7T6zseob2GoQpz3MYUechPy4V7I7jZtMYd8Lslq7nWIWQpK-6_Mef0hrhqe4v7XnQS8l0Egh6qaxecgViTJle0zfLWCpyDR8S0UuciXQeDdGHklbGemnqZgBxaAEI7JUDj7SqyNehLKQ1sjbKYeCuT5H_D6nuSwGB5XP_NGlv9xUlyqguWy2YY0HRpX5zX9mR_I2ZG3Rl-ZpMX_fFDqtuq22HU8_cq7qMqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_43YHsXmKdfkTgLjsRdVpgFZwtfSz0Cr649Wxd1MazjPtAMGKqaFFx4FacdOWblY3EhwhI108eVeLIxv97lgraCuPzXZpiB8gSC7hOD0xYOfMsM23h0UhTx4aYr4dRoZHHdgmzzRWLBZlmK_Wfzr9EFxyFJe93Z64R-jFtL1Zqx3f71sxr3MKiborunodYs7NhdIxuirpxMfv3XTJtF0ni98GHIFex9v-MCz-BI4jC5mm794rHC5J6OABElD96KIIYtNgvzRZ1KCumouLoTpK_aNCLNZkDsxetKN0ekXPJzoBq9bmWLPkz7a7KQeAHhJ5XWe5sSmjn5XG0AzS2GBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJ12K1v14lK6Z5M0rFcnkQJ_4j2S26CM4FX2IpfQ-bSm1XP_7dujwpWadsdwSHgmoXWO4A_osB9LlJOLORbVqnvQYcoCFGpADo9ctF_b7n3hBN3lrebOEv3tDzW0qb3uJeESrTfZYsBM2OTQwnX2km-ippwEI63EY0hmneh3JOVOtpuddI1qrOWIy2tWR84SYsXtAN8knVmJJKupiHPr01SHGapAkCRaYiqbTiPzDfYVJ66Ddm_FgXSNpz-L_BmU9nnGIi5RWLFqJuSouin50zR0Yzk4HabPX5EKrIZ1DhG1UcHhpQEdLaT8Iw_avrdqAzsc_737XqNBVSDd763XLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9zbd9IlJeHLAJ96NUQECZLNIF-U2-7mmLP72eDURV8asDiN1BdVpQgziltVBCMO9AUMxIXzhTdM4lLL15EFX8a1u11lG66fe5dM_SoUg16bOFuHDRasxGJTY7GmnSwlScksEZfTSldHAid1YCumBBr2Dl8LpC_p9lz1BESeDpimfvepu4_ehTZHnua_uXuUP7gzcFX3SfZ1obYeVoPdWSiDRsEzIJxQKomwET_uLXX_XW2VTU42GCTjeFTcxDdjjuetExudPzuyVTPOuWBKLCc2d19gJjOqgFZKfMVXK3zWQkVD2B9wY7i6w2DJk35-PfZqpIaaBQMIXZjdUpuNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AJ7HcLyHDsRqY8-5BEud23IhoDv15GRISb0DJjPP1wVaQFT5OMv5eybyLX-pdu9-HfeLHs_xOv6JaTGUgTXl_Vs0G6A-OWOXM5Q1CwrraZedPbddzU3zX5WhMcokC7ymMmW36UJ8fzz9Yp1jV5BczyfvNEe28w58l_znxN6z3XWRhfhLpVQmjEnGJP5F2MdCujpISy-erITnlxdASG7GQybVcGYA7WZ9kZ-R_jGVHPRg22AxWu69VQz7ilEuTwzXb2EoRZSOc7NtCQ6ukFnkR38YH8kVDl4ujfGyloCD-mFmt0SpbZNVa4jGss0VARCBsk974L9W_3OfPxU_XJb4_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FoSt1h2K5S-j_mgEV6mko7Vb37GaiWaAxyWuNJCoDuDxJ5C7px4u_qNY7F4IKKJaRfeFoMakjo0nrBGDhKw4TDm99BjTDvjdGgBwD3EABBXzJH71B0HvE52mBms9TGbHjEUQGrnPmS47QippbiCGUEJjDgp9Y5kpbpCYn6tQ7A57weTxq0yABTMAr6YgDE4Crg-QCofGi5nBhL998Q1DBT8GDgt-ycXhfXrkyBxv5t2Rk7XJzwSN5KsoNAqk7Ec_9QJqZ3Up72rO6Xp1N5m5xbn-ORuYiPnQO_dxrSLUpiuWM3uvCgFBF0gIUuvotiJEApZbYi2oILkgGDzbR-4j1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/457434" target="_blank">📅 00:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457433">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادامه عملیات‌های تجاوزکارانه صهیونیست‌ها در لبنان
🔹
خبرنگار المیادین در لبنان گزارش داد ارتش اسرائیل در روستای
بیوت السیاد
در شهرستان صور در جنوب لبنان، اقدام به انفجار کرد.
🔹
همچنین گزارش‌ها حاکی است توپخانه اسرائیل همزمان با تیراندازی و عملیات پاک‌سازی با سلاح‌های خودکار، حومه شرقی
زوطر شرقیه
را هدف قرار داد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/457433" target="_blank">📅 00:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457432">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1mZEPBxUGZHVuTBJRACx3YC5CIRNQhEamMpCrSUgNIiHjHrVdBhGU8ixRb0BMZ6i9Pm2a7ZSe0gM9-x-LnYN0jM74KZgtLWm7As-UwW5edpJcYckOkeoNUj2VFjGC2jW2XBDG-gQRI0XAw-0rQHZKoWMnU4jyD0VVSieF4VtnmRTmburECwt5xnHRONhlyv0apFr7sVSUfI78VqxGA0jfBUS0DvRg-Tc8n7lkAPb7gcb3ag44Y-ila8EMWe1DSWLHKhTtslu8KbeYjDWQDJVKi-6-rEvnLPTygi8XK61GcJlv-Teb1OsJnrEsX4_gUAQ1kLwpIL9X-8haZFMUBN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت و زخمی‌شدن بیش از ۱۶ هزار لبنانی از اسفند پارسال تاکنون
🔹
وزارت بهداشت لبنان: با گسترش تجاوزات اشغال‌گران رژیم صهیونیستی به لبنان، از ۲ مارس ۲۰۲۶ برابر با یازدهم اسفندماه گذشته تاکنون، ۴۳۴۸ نفر شهید و ۱۲ هزار و ۳۰۷ نفر مجروح شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/457432" target="_blank">📅 00:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457431">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cfeff9697.mp4?token=TlRTIPlEhKTGx9_HE_rjIGb5YytxwePcHzFjLc4ZKBtdH3OtopmQrBGKBNFbcfYjiO_0qHd2HwLqJPDuf68Lm1domazpDzy265JrAcGmiPh3Ybs4vobwI5-cv-KdrErGAzFnhb2iKA2boOfWaZGBdImISUOqafhSkE9wW9FFo0KH4W0TV1Vykb4A7y4B6BWxMFsSxgq_EJ9ydYeTnjrF5-XK913AItsNDZXZO79T-vwjpaqGUtDuOLXQrkW7M3lYrUyIjshQyV-PkVhZTzWegFxZEII_UM88eMkOSusq95DoN2V13pyaYbkMOgLACi1HuzuPru2F5_hBnk6pnV0kcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cfeff9697.mp4?token=TlRTIPlEhKTGx9_HE_rjIGb5YytxwePcHzFjLc4ZKBtdH3OtopmQrBGKBNFbcfYjiO_0qHd2HwLqJPDuf68Lm1domazpDzy265JrAcGmiPh3Ybs4vobwI5-cv-KdrErGAzFnhb2iKA2boOfWaZGBdImISUOqafhSkE9wW9FFo0KH4W0TV1Vykb4A7y4B6BWxMFsSxgq_EJ9ydYeTnjrF5-XK913AItsNDZXZO79T-vwjpaqGUtDuOLXQrkW7M3lYrUyIjshQyV-PkVhZTzWegFxZEII_UM88eMkOSusq95DoN2V13pyaYbkMOgLACi1HuzuPru2F5_hBnk6pnV0kcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایران امشب با پرچم‌های سرخ در میدان بودند
🔹
اجتماع ۱۷۴ خونخواهی مردم کرمان.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457431" target="_blank">📅 00:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457430">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75253a5d43.mp4?token=NDVk2DXp1MS1V5cEKkOS6Jk2RiM0T-7IyJw8flADIHBsX53VbY5dHGhOQyCD26pwbEb11VW3NGBVcYAw0PaRRgsVipzNEOfzP62IxT0_CnLKLOPixU3745i6PQA7_d-XZwjVi1JU5G8Khg8R3Gkidy_mkDSudSCr_MhO50_y7ejrVZViL89ug1bD9S7EhdmYkV7k4lQbYctiE2iOTDbglmmf-8r1nytwyS5wVZ3SmxwJpu9Xyy_b2-BD69Ep2oXtgeIU3-hbDYJ_W-x5RhjX1hXQ5qrgH6wDJCku8F8fvVDD7TbOWBzGfD5d3G4nPefb2_GxyOiRV5H9nM29tAvY4y5itTnhqHioeMOxgoB7uSZNbMG4gl-yxC1PGFcuquoFZdwQUSLWzZQ1bCyfZFBuvF2BTZyMF1widfXKKybE339UUe3z5DmAdVimUEdJPP8L5J2aYsjza1qFSYYXC0Mby1wdBlsoFbcLzKBQ8yX5Gq9OfrjTIVzCOa-A-WiS1S2YicUJAAjPMONrcq69BgQrU4kun5Emj1FfNKCbCaMpRDGe4OODZ009MXr4B7J9FS53gFeRLo_6aAnVbaOA_2OHwdWR4Epc2YJHcs5_uVqyyCZWKjvtCxupXX9r8Jl8tqkROfhv6qnZY2A3f6Pv8kN8fADH1pKSNAtMT3oqCIQX3Jo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75253a5d43.mp4?token=NDVk2DXp1MS1V5cEKkOS6Jk2RiM0T-7IyJw8flADIHBsX53VbY5dHGhOQyCD26pwbEb11VW3NGBVcYAw0PaRRgsVipzNEOfzP62IxT0_CnLKLOPixU3745i6PQA7_d-XZwjVi1JU5G8Khg8R3Gkidy_mkDSudSCr_MhO50_y7ejrVZViL89ug1bD9S7EhdmYkV7k4lQbYctiE2iOTDbglmmf-8r1nytwyS5wVZ3SmxwJpu9Xyy_b2-BD69Ep2oXtgeIU3-hbDYJ_W-x5RhjX1hXQ5qrgH6wDJCku8F8fvVDD7TbOWBzGfD5d3G4nPefb2_GxyOiRV5H9nM29tAvY4y5itTnhqHioeMOxgoB7uSZNbMG4gl-yxC1PGFcuquoFZdwQUSLWzZQ1bCyfZFBuvF2BTZyMF1widfXKKybE339UUe3z5DmAdVimUEdJPP8L5J2aYsjza1qFSYYXC0Mby1wdBlsoFbcLzKBQ8yX5Gq9OfrjTIVzCOa-A-WiS1S2YicUJAAjPMONrcq69BgQrU4kun5Emj1FfNKCbCaMpRDGe4OODZ009MXr4B7J9FS53gFeRLo_6aAnVbaOA_2OHwdWR4Epc2YJHcs5_uVqyyCZWKjvtCxupXX9r8Jl8tqkROfhv6qnZY2A3f6Pv8kN8fADH1pKSNAtMT3oqCIQX3Jo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین «أینَ المُنتَقِم» در ۱۷۴ شب ایستادگی کاشمری‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/457430" target="_blank">📅 23:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457429">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27c58dbef.mp4?token=Sc7ME1rn3Ed89xL9QzxZciFa-Lbb5XoYwiRzvdDCiWVbZJDNZZdukuHILKNnEYMCSQSx8oqUpBKH3DgZmbWkNfcVm4Kl2n5lUNpm4eQvlVsIFqBJrL6oNCvsNHh3xFLcBUS4OQfIxBK-5k3hKmIZjrd8J5J3w7VGwVcvixDqWXaeJRhDGq2XhlKKMRNp4uPgvcE-qM6VERMcjNC7nWcB9r5NqzxDa0p0xVRQnqS8boSqufQyKRACHgzHAZwWpB3625IjODfLbfKHuAaEhZ_AJHEd-NoKclkov_L2z9zR4mH9CSsyhOdLywq7R2CmyhJupF5uO1F1o6NwJRBBVLkKkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27c58dbef.mp4?token=Sc7ME1rn3Ed89xL9QzxZciFa-Lbb5XoYwiRzvdDCiWVbZJDNZZdukuHILKNnEYMCSQSx8oqUpBKH3DgZmbWkNfcVm4Kl2n5lUNpm4eQvlVsIFqBJrL6oNCvsNHh3xFLcBUS4OQfIxBK-5k3hKmIZjrd8J5J3w7VGwVcvixDqWXaeJRhDGq2XhlKKMRNp4uPgvcE-qM6VERMcjNC7nWcB9r5NqzxDa0p0xVRQnqS8boSqufQyKRACHgzHAZwWpB3625IjODfLbfKHuAaEhZ_AJHEd-NoKclkov_L2z9zR4mH9CSsyhOdLywq7R2CmyhJupF5uO1F1o6NwJRBBVLkKkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نورافشانی عید بیعت در میدان ولیعصر(عج)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457429" target="_blank">📅 23:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457428">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حملات هوایی رژیم صهیونیستی به جنوب لبنان
🔹
المیادین گزارش داد مناطق اطراف «علی الطاهر» و «الدبشه» در جنوب لبنان هدف حملات هوایی رژیم صهیونیستی قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/457428" target="_blank">📅 23:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457427">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjGcxPqhzu2We5SLDwxOKxa-tjb1Bmx8sgDNcIc_yBunDt8HrnsZwgCx6Z4UKvJKX7BhSnV6zwlExXbYJXKauE2gPR8ArkvJqVfb6oS0Pd9xKMy2Q2XTcjRscB5CuyDdpGjQxTc-wKnBQumfFE5WtUc7X-W6ICj2ueZm7rfI17X2iGMUCnShmdiyGVNJ6FSoK5YZfpHovbzlhrOzYQX4SlvEqWirx-pEd9q5jWdvHNzPYsfISTN5LpWgrP5-MLvxfVQr9lJ2GCcxQ9QppxnCeSR9ECk6uzkAolwhit9_7LuWDi64CcIwe8_y3W7aYLFlEuwUWv4jBPuZflqt5lvdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای رئیس‌جمهور؛ جنگ را چگونه پایان دهیم؟
🔹
این‌ روزها برخی از سیاسیون ورشکسته در فضای رسانه‌ای، از لزوم «پایان جنگ» سخن می‌گویند و حالا این ادبیات در اظهارات رئیس‌جمهور هم تکرار شده است.
🔸
پرسش ساده اما اساسی اینجاست: مگر ما شروع‌کنندهٔ جنگ بودیم که پایان دادن به آن به دست ما باشد؟
🔹
جنگ را دشمن تحمیل کرد. دشمن حمله کرد، دشمن ترور کرد، دشمن تأسیسات ما را زد و دشمن بود که پیمان‌ها را نقض کرد. جمهوری اسلامی ایران در مقام دفاع مشروع و با اقتدار کامل پاسخ داد و دشمن را شکست خورده به عقب راند.
🔹
حالا با این واقعیت روشن، «پایان دادن به جنگ» یعنی چه؟ یعنی چه کنیم که جنگ تمام شود؟ یعنی برویم و از دشمن متجاوز خواهش کنیم که آتش‌بس کند؟ یعنی با پذیرش خواسته‌های او، سازش کنیم تا او راضی شود دست از تجاوز بردارد؟
🔹
این رویکرد، نه تنها هیچ نسبتی با واقعیت میدان ندارد، بلکه دقیقاً همان حرفی است که برخی جریانات سیاسی ورشکسته و بی‌اعتبار در روزهای اخیر مطرح کرده‌اند.
🔹
جالب آن‌که همان افراد، پیشتر نیز با ادبیات انفعالی خود، زمینه‌ساز خوش‌بینی‌های بی‌نتیجه به دشمن شده بودند.
🔸
نکتهٔ مهم‌تر این‌که چنین مواضع ضعیف و انفعالی، نه‌تنها جنگی را پایان نمی‌دهد، بلکه دقیقاً همان عاملی است که دشمن را به حمله و تجاوز مجدد تشویق می‌کند.
🔹
تاریخ گواه است که هرگاه ایران از موضع انفعال و عقب‌نشینی سخن گفته، دشمن جری‌تر شده و بر طمع خود افزوده است.
🔹
نمونهٔ بارز آن، ۲ جنگ اخیری است که در دوره‌ای صورت گرفت که دولتمردان ما بیشترین تمایل را به مذاکره و انعطاف با دشمن داشتند و هربار نیز در حین مذاکره مورد حمله قرار گرفتیم.
🔹
دشمن همچون گرگی است که بوی ضعف را حس می‌کند و به جای عقب‌نشینی، حمله‌ای سخت‌تر را آغاز می‌کند. ادبیات «پایان جنگ» از موضع خواهش و التماس، به دشمن این پیام را می‌دهد که ایران از میدان خسته شده و برای خروج شتابزده است.
🔹
این دقیقاً همان نقطه‌ای است که دشمن برای افزایش فشار و طراحی حمله‌ای جدید، از آن بهره‌برداری خواهد کرد.
🔹
مردم هوشیار و بصیر ایران، رئیس‌جمهور را به صداقت می‌شناسند و از ایشان انتظار دارند که فریفته ادبیات سیاسیون شکست‌خورده نشوند.
🔸
تکرار این حرف‌های به‌ظاهر صلح‌طلبانه و عوامانه، نه‌تنها به اعتماد مردم نسبت به دولت آسیب می‌زند، بلکه به دشمن این پیام را می‌دهد که ایران برای خروج از میدان شتاب‌زده است و او را نسبت به اقدامات خصمانه‌تر تشویق می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/457427" target="_blank">📅 23:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457426">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7800dc1217.mp4?token=OSXRcLVZyi1qnkqd0piJ8g87dCw3InGgPPKfzf7TIiTDKXgr22sbTYkZYClkIq-SCKlguTiHYYWGoK5ggfKycoRvbG3-4wOtRraqLz0CTzQHZ-d5-jvbLbYk4vpXrIdhmS1SEa3LVkq0d80tEkg4_fQnQEW3hTvSfqUlg0lsrhCBLBewhGwM3QRS2ZHuSJoiNU8bHYzviRmNhbL-BaWbir7ZNnPGkEAcmRR7UwKbBfeK9wAGT6qI_3235-k3b3gy5bTYf4y41GqpRmO-5rIay2B1ZN-lHJdOHPANUOaRlEBBoM9xubypWdZWS6FyxQUXFOYL5pjdwaronMTzrwJ6Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7800dc1217.mp4?token=OSXRcLVZyi1qnkqd0piJ8g87dCw3InGgPPKfzf7TIiTDKXgr22sbTYkZYClkIq-SCKlguTiHYYWGoK5ggfKycoRvbG3-4wOtRraqLz0CTzQHZ-d5-jvbLbYk4vpXrIdhmS1SEa3LVkq0d80tEkg4_fQnQEW3hTvSfqUlg0lsrhCBLBewhGwM3QRS2ZHuSJoiNU8bHYzviRmNhbL-BaWbir7ZNnPGkEAcmRR7UwKbBfeK9wAGT6qI_3235-k3b3gy5bTYf4y41GqpRmO-5rIay2B1ZN-lHJdOHPANUOaRlEBBoM9xubypWdZWS6FyxQUXFOYL5pjdwaronMTzrwJ6Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۷۴ شب حماسهٔ حضور در گرگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/457426" target="_blank">📅 23:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457425">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b253a75ddf.mp4?token=qVu9-D3eO_y4HsVUBVec85F08G9dSl26-hHYh5Obst41TlamGrnbKEj3RkoIP-afCCvvuOoVm3SxWbRt2utCnDY7aWmjfSmCxGM4cCIAVh1my7DVjpDCRsYhw4VZPkjK_Z9dkRiHZ7kUNbn8xxN-x0DQNyveoijmTZwXzktdJJG783pQvcEvzBbHizo_ZaYEkfB6SzaQpxGgaIRP6PoYGgcrtVFr65g6PFncFyNJ0N-GgFAE73BGMMxq5C2uSYyi44wpzOUiiJGK5sEfayB9RiCWVRaKvCQg5WWvUShoQyER6oTf2kDRhn6GaT99MwcoX2_kn2i71ymfN4KBdT4INBv4ltFYA9ui9_Wlw30CcUsFV2wDBvP_vPeNuGuC-9mlhW9fym7W4KZ8XAuYrDoVPAt7DwpjWg148VuKe3vvC4IxbYcnkdAdkK2yTR5_IqhHAYG60zXmXm_IP1Ub-rtzebRBQN-PF-66LXpiO7U2JnSn-sxQeeK1QXW6OKW31VF2HzuMrnbP1tHN7LO7d-VjYN6gDcB_ax_feuPaunNLw_icHQzneaCv4Aos767--G1MitKrigj2RGl-t9zixPZ1djx0wnfBC20vP6AhA-3H4V_1lhxTLzDPGOaeV7US8C_vKG8_Wmi43gnSI0LFMB8riQ_M_Vz4hKuwg9TKiHL8D1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b253a75ddf.mp4?token=qVu9-D3eO_y4HsVUBVec85F08G9dSl26-hHYh5Obst41TlamGrnbKEj3RkoIP-afCCvvuOoVm3SxWbRt2utCnDY7aWmjfSmCxGM4cCIAVh1my7DVjpDCRsYhw4VZPkjK_Z9dkRiHZ7kUNbn8xxN-x0DQNyveoijmTZwXzktdJJG783pQvcEvzBbHizo_ZaYEkfB6SzaQpxGgaIRP6PoYGgcrtVFr65g6PFncFyNJ0N-GgFAE73BGMMxq5C2uSYyi44wpzOUiiJGK5sEfayB9RiCWVRaKvCQg5WWvUShoQyER6oTf2kDRhn6GaT99MwcoX2_kn2i71ymfN4KBdT4INBv4ltFYA9ui9_Wlw30CcUsFV2wDBvP_vPeNuGuC-9mlhW9fym7W4KZ8XAuYrDoVPAt7DwpjWg148VuKe3vvC4IxbYcnkdAdkK2yTR5_IqhHAYG60zXmXm_IP1Ub-rtzebRBQN-PF-66LXpiO7U2JnSn-sxQeeK1QXW6OKW31VF2HzuMrnbP1tHN7LO7d-VjYN6gDcB_ax_feuPaunNLw_icHQzneaCv4Aos767--G1MitKrigj2RGl-t9zixPZ1djx0wnfBC20vP6AhA-3H4V_1lhxTLzDPGOaeV7US8C_vKG8_Wmi43gnSI0LFMB8riQ_M_Vz4hKuwg9TKiHL8D1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستادگی مردم شهرکرد در شب ۱۷۴ تجمعات خیابانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/457425" target="_blank">📅 23:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457424">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb1ccd766.mp4?token=nMdgdbh2edK6mX6G5pabQvjNgWGsUAFYnLQDu6SahQHkrE5FTKPSaq0lwvcG6QELbYo35jNuGznNPF_RoqQDAM72YlIrdbuY8FDffjsN4sB-SFgntxl0_iuCKruo2QvXCn7W3JVlTXewftEg2dMfJ7wtNwv2NeoCi7VCDq6vJZnxXkGPpne4g8L6DKHmgBurtQVA-O39jTz9q-iUQBYPlTtBHVbAuMqq6wz6MtYyY7UnPe5f0_Gtjb_xLPCErwQap7qCR4EKojOLShEVdn_pL3rLpGOhg0lZZuOCxVY-8m8-uoZD8bAUtsqBcw8-tvfXAcMKPP1ENkAH9tnp1rthQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb1ccd766.mp4?token=nMdgdbh2edK6mX6G5pabQvjNgWGsUAFYnLQDu6SahQHkrE5FTKPSaq0lwvcG6QELbYo35jNuGznNPF_RoqQDAM72YlIrdbuY8FDffjsN4sB-SFgntxl0_iuCKruo2QvXCn7W3JVlTXewftEg2dMfJ7wtNwv2NeoCi7VCDq6vJZnxXkGPpne4g8L6DKHmgBurtQVA-O39jTz9q-iUQBYPlTtBHVbAuMqq6wz6MtYyY7UnPe5f0_Gtjb_xLPCErwQap7qCR4EKojOLShEVdn_pL3rLpGOhg0lZZuOCxVY-8m8-uoZD8bAUtsqBcw8-tvfXAcMKPP1ENkAH9tnp1rthQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
جشن آغار امامت امام زمان(عج) در مسجد مقدس جمکران  عکس: حسین شاه بداغی @Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/457424" target="_blank">📅 23:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457423">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
خط‌ونشان مردم کرمان برای قاتل رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/457423" target="_blank">📅 23:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457422">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d68fa320.mp4?token=m4ByByZK3TLihCtJc2INVKpEjyYS-d6nCRwUEy5WtG9QQDl0kWwWPhTrc3tlzIjkp6lF34d9gZe-64Iv4kBiX6T3GB8PflKOzGZB_7fpEn8Ha4QkJBsp7yyY3elqLFzPawGsiAPGp47kLAR11oV0zpuu663mz3nNH8N_PUqgI3xD-XE7QDGETJuCu9CTUtaVep3AOEd7Up3iU95fzbhqTH5ATUjOWgsx94l6PsaFVcncgzoc9HQ8WUvINKMa5FBVwtKhw0By92cotiZSyB4kMcE7U62Ev9G6rUZP7j0PRxPkokXTULtzGFr7ZzIwVUVUc8a2eWq4vzBu8gm7tQMa2EYuQxe15s17n9-j7pK-wj7L5a1L8cFA6UQGV7s7tPpA-gy4brlOSZd8lyWZQvnpTzilWLZWghOdWCF_cPPu_HcDAbrTdR5jl_CXGrmP6bLrsp1Bi0rY43MVWTszwPyyQI4zCq_M3C0kvgFBoMaxv6TSY_C08NBpQ_Y2XmmZq9B0wjBP6xC9c8SAJGog9g2fwBOljys29SOYJ-GCCmneY3Wr-PwanP3n4nJ5Y6-Z2T0VsLZ26u41ILoG6Zo6uDRnlQb7X025lNGU_IEqad2TtsCZEa8-hCPfW-VQZW1cXnbh796l-6AUCjY9mObaavXzbB3aGjh2X_eCTv2ap5__tp8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d68fa320.mp4?token=m4ByByZK3TLihCtJc2INVKpEjyYS-d6nCRwUEy5WtG9QQDl0kWwWPhTrc3tlzIjkp6lF34d9gZe-64Iv4kBiX6T3GB8PflKOzGZB_7fpEn8Ha4QkJBsp7yyY3elqLFzPawGsiAPGp47kLAR11oV0zpuu663mz3nNH8N_PUqgI3xD-XE7QDGETJuCu9CTUtaVep3AOEd7Up3iU95fzbhqTH5ATUjOWgsx94l6PsaFVcncgzoc9HQ8WUvINKMa5FBVwtKhw0By92cotiZSyB4kMcE7U62Ev9G6rUZP7j0PRxPkokXTULtzGFr7ZzIwVUVUc8a2eWq4vzBu8gm7tQMa2EYuQxe15s17n9-j7pK-wj7L5a1L8cFA6UQGV7s7tPpA-gy4brlOSZd8lyWZQvnpTzilWLZWghOdWCF_cPPu_HcDAbrTdR5jl_CXGrmP6bLrsp1Bi0rY43MVWTszwPyyQI4zCq_M3C0kvgFBoMaxv6TSY_C08NBpQ_Y2XmmZq9B0wjBP6xC9c8SAJGog9g2fwBOljys29SOYJ-GCCmneY3Wr-PwanP3n4nJ5Y6-Z2T0VsLZ26u41ILoG6Zo6uDRnlQb7X025lNGU_IEqad2TtsCZEa8-hCPfW-VQZW1cXnbh796l-6AUCjY9mObaavXzbB3aGjh2X_eCTv2ap5__tp8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چهلمین شب تدفین رهبر شهید در حرم مطهر، صحنهٔ دلدادگی و بیعت شد
🔸
مراسم چهلمین شب تدفین قائد شهید در حرم‌ رضوی، باحضور خانوادهٔ رهبر شهید، تولیت آستان قدس رضوی، جمعی از مسئولان کشوری و لشکری و زائرین بارگاه منور رضوی برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/457422" target="_blank">📅 23:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457421">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9802e54cdb.mp4?token=G0_ptftb88VZX3fB3V5IoAj5A6Of-T798YqmlKWIMpVjzW0vvFOrtJw6-CKsgjqy_KfO_mFjulnI9v8R17VUsbrzvPPz2OVCz5Lvx-vnCZWntWe-UdQgzbgHDBcR_Lqix780Tc3ucBeiLeIwakMvIsmGfWTZ1F3VssaPpHVO7Sv35B2UhaH4qapeTLIxo20a-pA-rslsPWWznnOMYzaULfZvmbcuRzI4wIcMBfeSem7JoHB_y1WVlmO5scUvo9BPgFz9YSTb10I9OqQPLDm9waxY47ZHgt9fLJ9kTwpkM5HeRPyd23IQBxsZ3Y0gFyFCriRz70YbdXWvM3a5p-bR6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9802e54cdb.mp4?token=G0_ptftb88VZX3fB3V5IoAj5A6Of-T798YqmlKWIMpVjzW0vvFOrtJw6-CKsgjqy_KfO_mFjulnI9v8R17VUsbrzvPPz2OVCz5Lvx-vnCZWntWe-UdQgzbgHDBcR_Lqix780Tc3ucBeiLeIwakMvIsmGfWTZ1F3VssaPpHVO7Sv35B2UhaH4qapeTLIxo20a-pA-rslsPWWznnOMYzaULfZvmbcuRzI4wIcMBfeSem7JoHB_y1WVlmO5scUvo9BPgFz9YSTb10I9OqQPLDm9waxY47ZHgt9fLJ9kTwpkM5HeRPyd23IQBxsZ3Y0gFyFCriRz70YbdXWvM3a5p-bR6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: در یک سال گذشته، میزان تولید تسلیحات و تجهیزات دفاعی در کشور ۲ برابر شده است  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/457421" target="_blank">📅 22:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457414">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IojqynR3mJ8EZX7hkiP3F8bF9KIkPYpT5EsOdtcTmwf2XuOcMzKeoU9reZl4IVid6W0ApTuClhJTxmw2zIUmF8xnf4snYSzFv5oZ1k8OVz3QgpfPf2BUwxR7JrIcO1g3vC2TNxV3mxWi_9--YXaZvhP8MhF1HKP50q6dQ4NOhJTgDExFNYpJe0jaI-Ayg_ffZ-CmcdnxgNB1VIdbQsmX8nHuA5mxuZdRNs4jFpSAkyzJK_XFX1s9B0GNFrl-8gTFgJMASTKtANHVODm6jO-M0mW_aNppKpXU3Hhab8iespTF4bc6wgOgwXZ2myrbiiu9ZBDDgzjbATtXKC4QewdNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gsnoapag-zwKF_2d1HP9OP4mw26YcKm8tipLTM7U8RE8GRZcVHTqOify9aXBnHyaMU-WIqMrtFv2ndX26_glTS5w4qG-nlAQavtZHHT97N4hcVy0hx0g92K0pn51XgeqZfE4rzj1IjECCe28YT8fP4ID-Hl1KsUDlGFmoxFtodiD7z3a20N1Wgbym_gS9Z93YE6qHFxKBfWBr2qIzZhLoXXJCQD576iYLlLNc40fmGWipz6QYPhdRPS8Se7AW7pPaYj7dUaoORxjM0MJWWKm3FhS1aIgtCEL6RWJ-_Pa7gsAnqR33wBtiNxpSg3oZw3mW8HpEuKqZd2lvyX8j-Witw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggZrcJVtbs42UdYZlWGx5-3DnCjkCvEZUnRTKHeHoBgvDrmDomwml97Zt219P5sDtwLWwWjxLoZl8EnPFMFElr_Vp9lfDGuHGi-y6EbWNS4M8KisgK0I58CCbT8iZaaxoFj6cSrRXFXE2r9Dmzf4zvYPafWaEAq3YDVUrTbKaSJFtlICr-kWtdrXRj2GQe1VdhP8oGAzjMtJ8yKWRvONVUkoBJ8WA74DotB7dAyQIY4aCzJyANHk3iIc5nPiN4dp76mem2-V1QSazv8aEcnhzb1gDiV7wxawT7isfVNmwallMNb_bIn0GyKLM9zj2vr7uMUunPTF4wIr-pI_msfhaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puvmmAOIHjwFKl16tGCpiqSiET51xcYfVBPV3c8l5SC6VcOmF9mEW4uw9KiXT4Jjxl35jLic2uDoq4E-nPpksX_YRxIPaQVZr3VH7zrEKAskT1i6MKqhzPjE9Cm4HZJ2Rm5HhXQu3PWqPQLXi3s3xuc2brFloi-YshVFSDG5Bl6yFZsZFzBGNiEWNoGozCVLcrJQ3T3bKmZydgOTEBCNxh4uAIuVizaQytM9ktol-Uck_tKhrWmiRlJeyB4JC12No34x3Osh49yo2XWDan-IB_7MRo12dTey0RzLNzQlABKR4kNF6tdzv2uNQDZFBBwlfzzR0k9KwxgbKZulA2aFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vg_DJwLDQqSS5RijDCZuLaFQq9NX1ez0Dc0R1FvdkFhdg7rzCQhGmKTvWXu7MusBKjJLgSBC90GIN6rUTBzsRoMQ-_LjZFLyTjXxfj3d2sSVS1stx6IcKljZAVCO3gZdTFTxV0La1pLeBjJyn3_jDP3TK-pg9WuQjyiDtGWPAgKGSWYqXsQiVRY6ijzjFXlw12mqSsVkEekJfyqZw-qNmnZGl06Lm1zTAqZVTEPaRso-bVmXDcBOr9zSSRi4twyTMXifWHyt51Vcf6k040xS_KdI1d6Pmmgxg2_El1WB0nkYDNxmO9dTgmhOMFOJWYhjw7wjK_PFzueXaM16rP88Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1uRWS1EtVM3qzkKVHvDzb0N1j-6g3lBE2dK8PcZQN1tA-wQcqB8nNavu-0_hUjzGxJ9QgzOVEGV9vZAQ3IsctzRW_hyBeFC-CjBqsBf9A9HFAhT-tsJNSLwL1Ut89GH5XUjUIt03YjE9q7dIK0PExKzEOAdyBfEF188Ypva4ww89MyRqBbWvau3PB0_sBFqOmR3ZvwGABjjK2NOliQ8T43GlCo6J3M5H80KvMgbBozmiMq-A7N3R1vs_dcpscQqx0iTSoXQS00xW5GvQVcnDnG6cSq4FReWuX2v16Vr1gi2X74sSYOF4VKZ0JP3sDXQQoYEmfmKX7D1gT9SPSCz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jM_ZikGnS_AqPZpne1_5DyL4odmdvnpuu7OMKZTT7LRovLtahwOTgxCoPYkcbUTC-khsMJpfOmFWCwPBbbx-h-iFt65jEYQKzFgXbLNn49EnPgpoqOTpfJmLFHHiCM-LDKM_IkRLWkHP_UuNe1QNRlky2ogxqRax9_eh0Isbf4ukJ7m3ZcP0x0ju4ei1m3afqHPVeEUSPXRYlj54id04y3xR0iEd-KNJ_EMSe5LzDXR9iE8KjgOFxwMo3FT4saK3yWacatt-ltaR6d3swIHhmW449LmcxaW2-PxJQ-nBuCWyiKGZsuU77530N1CJ32b_i2uomvk7ynhmSTqLPZiExQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن آغار امامت امام زمان(عج) در مسجد مقدس جمکران
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/457414" target="_blank">📅 22:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457413">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227375ee24.mp4?token=tzEajnUrMKyWjQhi5TzTM7iITGaFa5RMqHDRLsQpPI5saCRVN3b0bcrdBh4bGZWuM2ipX_ZO9baZhFqU821NS1Z3DYF7meIm9X4uF6Qy4o9g89xir79Bdxe-iRQkaR4-hAVdb0fAv7A-T1rMNXSPHC0jTDmS8gXFcX0mk9tkeqdAwA6EJx90dFf-G0RM0NHUap8UgXDA_cdFbtmXauNtNK7uqwrEEPEh9Hp-XGFGcwb1eLdM7VfwNQP8lkJ_rfs9tRJSOXsKbcvA97BqUMKvD7mxSi07Qmhqlv8G6TCdL7inBx0CQxWU2goieyxGHnZfS0Z3YrOLGnXd3_IfUFfQhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227375ee24.mp4?token=tzEajnUrMKyWjQhi5TzTM7iITGaFa5RMqHDRLsQpPI5saCRVN3b0bcrdBh4bGZWuM2ipX_ZO9baZhFqU821NS1Z3DYF7meIm9X4uF6Qy4o9g89xir79Bdxe-iRQkaR4-hAVdb0fAv7A-T1rMNXSPHC0jTDmS8gXFcX0mk9tkeqdAwA6EJx90dFf-G0RM0NHUap8UgXDA_cdFbtmXauNtNK7uqwrEEPEh9Hp-XGFGcwb1eLdM7VfwNQP8lkJ_rfs9tRJSOXsKbcvA97BqUMKvD7mxSi07Qmhqlv8G6TCdL7inBx0CQxWU2goieyxGHnZfS0Z3YrOLGnXd3_IfUFfQhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: یکی از ویژگی‌های برجستهٔ صنعت دفاعی ما، سرعت و قابلیت تولید محصولات دفاعی است
🔹
به میزانی که در میدان رزم سلاح و مهمات استفاده می‌شود، با سرعت جایگزین می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/457413" target="_blank">📅 22:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457412">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd5bbb334.mp4?token=RKvYvHgQ_x0fKhmZ-tFSR-hTWC2rqRmWwOE5oJEaPaM10SuioGIryvCbsDJFJXb4-n0qsYLl2dZcJo7MXVTvdbjthb5LsZssXdEbumIvTwXOegR2kvy6sUaL2ev5qV_xKkDIwei2p6ZNoqyAb2cCt-hcTAKZ93MHUtm7gcoawCzrySlLZDBo-Fu2sPrW2j5W8U2j5mus_LTRWLcUOiZ0hWP61NETDoRo0pZnkZga4xJwWtlzP9H2bgdiHnaokghsRXQaie-VH5C-rmQ-IsIsN-E-El_Y2hUHueWkHZacRn87OSk7k9ZjXw2r1VopjxBVaftUmzQqhAgesebjpXLtojSAh3cSp0IWpVRkpnc_phk-GsoMJx7NMt0G9nESqMxky0_tQHdKKFA_gCsTgH33PqSZ1vMjuGNIlsPfOd_NlHHfVII-AHtUwhaF8i8n4bDtNhMSp1g2PWvG1CNsgxlFRgntQNw1Phc89lDcsa674BICw7V1_3vLNq9Cv272gImU6W7AJ6DNxsdZHk22_Ey46hKz_kEmSbJ_pEDY_KikY5feli3ERmqKCOOp0rbG-_X-19S1w9Hning5hsHCBTEEwKyw5njf7txncK3XinKsHLINK29RdSp4eXpabBmiS9oluyx7-Qj22TrTGEbTeZ_oQhVru0crGa5a_FSCNDu7SF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd5bbb334.mp4?token=RKvYvHgQ_x0fKhmZ-tFSR-hTWC2rqRmWwOE5oJEaPaM10SuioGIryvCbsDJFJXb4-n0qsYLl2dZcJo7MXVTvdbjthb5LsZssXdEbumIvTwXOegR2kvy6sUaL2ev5qV_xKkDIwei2p6ZNoqyAb2cCt-hcTAKZ93MHUtm7gcoawCzrySlLZDBo-Fu2sPrW2j5W8U2j5mus_LTRWLcUOiZ0hWP61NETDoRo0pZnkZga4xJwWtlzP9H2bgdiHnaokghsRXQaie-VH5C-rmQ-IsIsN-E-El_Y2hUHueWkHZacRn87OSk7k9ZjXw2r1VopjxBVaftUmzQqhAgesebjpXLtojSAh3cSp0IWpVRkpnc_phk-GsoMJx7NMt0G9nESqMxky0_tQHdKKFA_gCsTgH33PqSZ1vMjuGNIlsPfOd_NlHHfVII-AHtUwhaF8i8n4bDtNhMSp1g2PWvG1CNsgxlFRgntQNw1Phc89lDcsa674BICw7V1_3vLNq9Cv272gImU6W7AJ6DNxsdZHk22_Ey46hKz_kEmSbJ_pEDY_KikY5feli3ERmqKCOOp0rbG-_X-19S1w9Hning5hsHCBTEEwKyw5njf7txncK3XinKsHLINK29RdSp4eXpabBmiS9oluyx7-Qj22TrTGEbTeZ_oQhVru0crGa5a_FSCNDu7SF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی مردم در میدان، فرماندهٔ مصرف انرژی می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/457412" target="_blank">📅 22:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457411">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113caef9ab.mp4?token=Oq2xubtNpPUt9KZ4xqnanr5kFidpmuTdH3eZFpQPVqtfkvDmzHK8UVMhCrS5fh3d12HrPb22FH3jnHTjbdbhEaKpu1oXvrZX9u1U9Tdn88oYcT4qgtQOSEGCmSiruV7dQWnKQganHejhdO-z1UPrjlmCt6QBwpC_OrJfx93QBqnLTHkUs99vJsuiMTk6gwl7ivzBk1qseIdnSJWfn_3_i16NtwYwqpUkIzywcxrObGBth4W-fUAn4BRo9b7PnIYAw-xY4xe6B4VZz9MSl0QKemJ4U6SPDCLpa6J9NSvQoQ-R8owHn8VIN0WEpA89mg8iR_3gMKUDynFfslTMTbHC4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113caef9ab.mp4?token=Oq2xubtNpPUt9KZ4xqnanr5kFidpmuTdH3eZFpQPVqtfkvDmzHK8UVMhCrS5fh3d12HrPb22FH3jnHTjbdbhEaKpu1oXvrZX9u1U9Tdn88oYcT4qgtQOSEGCmSiruV7dQWnKQganHejhdO-z1UPrjlmCt6QBwpC_OrJfx93QBqnLTHkUs99vJsuiMTk6gwl7ivzBk1qseIdnSJWfn_3_i16NtwYwqpUkIzywcxrObGBth4W-fUAn4BRo9b7PnIYAw-xY4xe6B4VZz9MSl0QKemJ4U6SPDCLpa6J9NSvQoQ-R8owHn8VIN0WEpA89mg8iR_3gMKUDynFfslTMTbHC4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: یکی از ویژگی‌های برجستهٔ صنعت دفاعی ما، سرعت و قابلیت تولید محصولات دفاعی است
🔹
به میزانی که در میدان رزم سلاح و مهمات استفاده می‌شود، با سرعت جایگزین می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/457411" target="_blank">📅 22:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457410">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a6c5530f3.mp4?token=fMjdMgAEn7q3t2OKfa9Uf0DScwQ2RFjZdb66K9bPHYQQhGsY2lkNNsrN6zEeTqtVbdnxbidtznpl2TOOWu21CXTS5STihcBglwIJrF5BND9WfXFL4jQ9JM6XCBJgRWBvgdPl0TTTrNjJY89VcYYHId2umvNhSApFkNRu_i8kfQbX32BVakY_MtXXWseBdPNQCrbTruoRiKueOAZQyV-BE9pskXBsOwiVMYFTxG96zSb-QjHJm_Wd8Xrg7YnTZkbdjg8n_7PfkfYJueD5DHYS0qL13WabYkBPmqihhfBmGO7AvmKw7F56Yp11O_QEvBY8-M75UnrQDFzm--tFs4rK4hu9VUXOumDyoT_dJ8rxL_SIXZyCgyWnCKqaY6XYnzQxWtDitYZfzMTFl6KAyOZKwrMrvH_qQdNZWQRtgRFqm1shR58uEdhRz1UyEkH4l9HDcrzx_j75Oz_gsZ2nyyk3BB_-EkRhso540Buoenn8Qz7MK6ZPjSmXqiugBnw4ItZlHzEldU9FypIS1XTuwJ2VgV4yvmizfFVd15iI9nQlx-SUMyE3goZLEp0SZ4TULAheOVxZHGr-PekLDDNtMVCIqUzt2pP08mhKeQ6qGvFfU_1vCj1kYeC3205curOFcF6mZjl3UWQl0lqDA23oNyedX7rdUhEDke_N7bh1bPZvWuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a6c5530f3.mp4?token=fMjdMgAEn7q3t2OKfa9Uf0DScwQ2RFjZdb66K9bPHYQQhGsY2lkNNsrN6zEeTqtVbdnxbidtznpl2TOOWu21CXTS5STihcBglwIJrF5BND9WfXFL4jQ9JM6XCBJgRWBvgdPl0TTTrNjJY89VcYYHId2umvNhSApFkNRu_i8kfQbX32BVakY_MtXXWseBdPNQCrbTruoRiKueOAZQyV-BE9pskXBsOwiVMYFTxG96zSb-QjHJm_Wd8Xrg7YnTZkbdjg8n_7PfkfYJueD5DHYS0qL13WabYkBPmqihhfBmGO7AvmKw7F56Yp11O_QEvBY8-M75UnrQDFzm--tFs4rK4hu9VUXOumDyoT_dJ8rxL_SIXZyCgyWnCKqaY6XYnzQxWtDitYZfzMTFl6KAyOZKwrMrvH_qQdNZWQRtgRFqm1shR58uEdhRz1UyEkH4l9HDcrzx_j75Oz_gsZ2nyyk3BB_-EkRhso540Buoenn8Qz7MK6ZPjSmXqiugBnw4ItZlHzEldU9FypIS1XTuwJ2VgV4yvmizfFVd15iI9nQlx-SUMyE3goZLEp0SZ4TULAheOVxZHGr-PekLDDNtMVCIqUzt2pP08mhKeQ6qGvFfU_1vCj1kYeC3205curOFcF6mZjl3UWQl0lqDA23oNyedX7rdUhEDke_N7bh1bPZvWuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک صدا برای ظهور؛ مردم از امام زمان(عج) گفتند
@Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/457410" target="_blank">📅 22:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457409">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c8ef80cd.mp4?token=vKCYaJlpwsn-9k3iZ_aZOJdktPgyDgLcFiJ-7ZK0TPedjDmnTqIgiHAfWUVWWfOjzKOz3F56gltpLh5LIQZsK8RgVsgAWZt10P8HYkgeNowjtk1PN9flQgIUX1TIzojEfQ3ti0nhHlv7-kU9YfbUpryobVCVQSzZLY0njj2f0G5QGyplN7hCNOp0c6c-y_cnFQcL7naNXSJqHjdtWLHpIvOQyFVmp0CUOK9owG-7iwoYnXJuFvkyRIl1EXdBxotEY95IvWDvj6tLn2JrjiXKVVr3AWQlj0hFdkZX2EWo6dRIy6H9V9dfR0zOkAkoQzlW4sH6FwZNDtNfVRux7oJ2xrCBZ732CPOYfwCzPcXUh2V-CldlE1U9_pm5galZ4ndeKSCexfUacidQ53jN_a3_1Ly7OpsvXNkWGfX4grqUlWBI6EpLn4F38yuUSCk9HVg9AdElrIFW4KXIV4_MH8-HGu3I1c1tvmQwhZiWOeBkyErEpR_EJBtNSbdyMm4CRtgoc1eQPVaGIWUu-2FWyR3mA2XMr6KxKk088Qc5tCrOGHJ5SKQ0YUB5vKg_Rm0rZWnm0xhijUXPApWXMZuC_hQLsj5ceWenImC6MNiqd0IpaWboCglD0o2mXXN259lTyHjnF6OjRhv5X8W1TWnw1Iw6zKpoG8ZkOrcye_F3RgEAIfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c8ef80cd.mp4?token=vKCYaJlpwsn-9k3iZ_aZOJdktPgyDgLcFiJ-7ZK0TPedjDmnTqIgiHAfWUVWWfOjzKOz3F56gltpLh5LIQZsK8RgVsgAWZt10P8HYkgeNowjtk1PN9flQgIUX1TIzojEfQ3ti0nhHlv7-kU9YfbUpryobVCVQSzZLY0njj2f0G5QGyplN7hCNOp0c6c-y_cnFQcL7naNXSJqHjdtWLHpIvOQyFVmp0CUOK9owG-7iwoYnXJuFvkyRIl1EXdBxotEY95IvWDvj6tLn2JrjiXKVVr3AWQlj0hFdkZX2EWo6dRIy6H9V9dfR0zOkAkoQzlW4sH6FwZNDtNfVRux7oJ2xrCBZ732CPOYfwCzPcXUh2V-CldlE1U9_pm5galZ4ndeKSCexfUacidQ53jN_a3_1Ly7OpsvXNkWGfX4grqUlWBI6EpLn4F38yuUSCk9HVg9AdElrIFW4KXIV4_MH8-HGu3I1c1tvmQwhZiWOeBkyErEpR_EJBtNSbdyMm4CRtgoc1eQPVaGIWUu-2FWyR3mA2XMr6KxKk088Qc5tCrOGHJ5SKQ0YUB5vKg_Rm0rZWnm0xhijUXPApWXMZuC_hQLsj5ceWenImC6MNiqd0IpaWboCglD0o2mXXN259lTyHjnF6OjRhv5X8W1TWnw1Iw6zKpoG8ZkOrcye_F3RgEAIfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۷۴ شب گذشت، اما نبض میدان هنوز می‌زند
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/457409" target="_blank">📅 22:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457408">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOEpvGAoaW6QjWZKMH1DCG_t_X02bntoMI0BiMXCgw79G-5R96kfmN0lfUQWGjI2vg3CUUa-hhzQK9RO0JTQruHvJt5f29LSmhoYbF0_6y9nN24F4GlR9etRmYiQSzkdoM4DDw-D0m4htBHwZ7MJB9IdVBt_cvGQbZ5SSd3nGXKb5qz2OC68VQxFEqOHqiZVNhBQslyr6BSH4nyebQGshaHmdC_zFNztkxcJnxyHOqdR2Sem_OfqBJOxQf3cUvYyimC1ckkBMcbsY59KWZwT1b7DIqydyHChTAdmmF-X5A1IHhrD5pZiNljvlccDKkpsIPOJZ6zfpqxu8yHR_JMYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: اجازه نمی‌دهیم اردوغانِ دیکتاتور سوریه را اشغال کند
🔹
دفتر نتانیاهو: «اردوغان یک دیکتاتور یهودستیز است که کردها را قتل‌عام کرده، به حماس پناه داده، نیمی از قبرس را اشغال کرده و تعداد بی‌سابقه‌ای از روزنامه‌نگاران و سیاستمداران مخالف خود را به زندان…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457408" target="_blank">📅 21:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457407">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/082614d667.mp4?token=iS8A1R_PrKVONi-gR9PQZD189e8oN6FkSBv9xr1SQc6VZJj4GiyHTzHOC0RGdxbKT_b1st9Z42tQVJ_kCuqGC4rKZCan-VVljNdI56PXrsDFrdzu_7hiX47KWfNMrvAQg9lO9tisyoJlJnZnDdtdITMcbcyc3zlwnu55L2vLLmIQ-WiowbzY-VW8tm1Yx8g4FzATcPKqJy5fma1t-1Zd2sSDocm_B2_FuJ0lQRan0yGufuJ6pCsavtGl7YkimttLaixSVXEs7xw1c6GkVgNZut4dqjG3iapJIklR24HdQDdSKH_qm5yUNQc111yKsWOgBTRa0Y8mZgdFxc-Zo59uzjPQF4OTksoB54jmpJ4R1rfh8UvBWLya6MjVZYHwqfmHM0zN4vgkGEtlanPLC3ZxsoA7YnT_emaGTbRjX40cDmtQtgcgXRTpgwYiMSe4dMlX_Uq3Id2Xo9Zw5V0gXKXkGBDjBPQq33DAPNiJoFnS4SZ-I3vKmtcwXaVp-cYi6vtXzRfWvhrVUWDPY2BCq1dt5VKQPsDE8Fknl-8SUuJif5aDSxOK5_qTPecUqyOH-9wxgk7mkVxJ26oxt45Up7VcQ_1OGL37iP_wgfNKdDgiq0OZFVJrwSDxJUnZ6bgDBvJTMT7lsYMwsTsJsF2UC_9ywUbZde6JurhAuybTPcfBlSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/082614d667.mp4?token=iS8A1R_PrKVONi-gR9PQZD189e8oN6FkSBv9xr1SQc6VZJj4GiyHTzHOC0RGdxbKT_b1st9Z42tQVJ_kCuqGC4rKZCan-VVljNdI56PXrsDFrdzu_7hiX47KWfNMrvAQg9lO9tisyoJlJnZnDdtdITMcbcyc3zlwnu55L2vLLmIQ-WiowbzY-VW8tm1Yx8g4FzATcPKqJy5fma1t-1Zd2sSDocm_B2_FuJ0lQRan0yGufuJ6pCsavtGl7YkimttLaixSVXEs7xw1c6GkVgNZut4dqjG3iapJIklR24HdQDdSKH_qm5yUNQc111yKsWOgBTRa0Y8mZgdFxc-Zo59uzjPQF4OTksoB54jmpJ4R1rfh8UvBWLya6MjVZYHwqfmHM0zN4vgkGEtlanPLC3ZxsoA7YnT_emaGTbRjX40cDmtQtgcgXRTpgwYiMSe4dMlX_Uq3Id2Xo9Zw5V0gXKXkGBDjBPQq33DAPNiJoFnS4SZ-I3vKmtcwXaVp-cYi6vtXzRfWvhrVUWDPY2BCq1dt5VKQPsDE8Fknl-8SUuJif5aDSxOK5_qTPecUqyOH-9wxgk7mkVxJ26oxt45Up7VcQ_1OGL37iP_wgfNKdDgiq0OZFVJrwSDxJUnZ6bgDBvJTMT7lsYMwsTsJsF2UC_9ywUbZde6JurhAuybTPcfBlSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلتنگی مردم برای آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/457407" target="_blank">📅 21:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457406">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UO-B4OazfL5kVaPHSR47l7YRag1Jyau3GxIzEalnlcmtaDDfSgv7ap0FeGzHt8UeUqckALrnc-lUqz888whaH8X9XImO2rBlVKlP6_KPpjysESue86-vj_DztoH5P9UAkDQf_Ra2oDSvGSIHQHKO7pL62rHVXIgnWGXR-3Sbewkte-2vT_RGdeWX3R39J2KpaCxQjgUsCORZQkL-cKDDJGbZKp-qssyjAO-CWURGJWr0PkVqPNC_AVF8CosTbSZsj_d-O893Trdhwea0j38Ry1TTbCtSzfYO574nlf68cIfyytzhBuPdrEh-c0BFA4UH-PZq1Ou4jQ_-JAPlMKpdvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام، صفحهٔ «رواق دارالذکر» مزار نورانی رهبر شهید انقلاب را مسدود کرد
🔹
صفحهٔ اینستاگرام «رواق دارالذکر» که به پوشش حال و هوای مزار نورانی رهبر شهید انقلاب و شهدای خانواده ایشان در رواق دارالذکر حرم مطهر رضوی می‌پرداخت، ساعتی پیش از سوی این پلتفرم، از دسترس خارج شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/457406" target="_blank">📅 21:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457405">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cc680d77.mp4?token=tKeWriNLbMkMUlTiL3-ISa39aJLuFUYy9LV5qR3uzWSiO_AJ1PCr0gdGXhB0iQjgBgSWmo36QClOTEDuJ08ZeuvzzpblZF6lAoChH-A6K-CQVKn2OHyoKOr9wqBfl0c2r3-tmcHHEzCIaddak1Bfrx9TFdQLEUZ9Cl0lS2WERKD2aqeoIVaXjV-1_JxrZ_5UWts1vu_fJhpCOirKLId47Wc27vxH-kghw6QIuQLO2NNuY13YYI0J3NFGTSUTU_laFv40Tyk2QkKd-zmwY0Z7_hCM4jkt8_Evh_0JrmyK3KyjeETxRqFVaH3GCmeWykCNTz-OB_thhh17hpEZV2tKxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cc680d77.mp4?token=tKeWriNLbMkMUlTiL3-ISa39aJLuFUYy9LV5qR3uzWSiO_AJ1PCr0gdGXhB0iQjgBgSWmo36QClOTEDuJ08ZeuvzzpblZF6lAoChH-A6K-CQVKn2OHyoKOr9wqBfl0c2r3-tmcHHEzCIaddak1Bfrx9TFdQLEUZ9Cl0lS2WERKD2aqeoIVaXjV-1_JxrZ_5UWts1vu_fJhpCOirKLId47Wc27vxH-kghw6QIuQLO2NNuY13YYI0J3NFGTSUTU_laFv40Tyk2QkKd-zmwY0Z7_hCM4jkt8_Evh_0JrmyK3KyjeETxRqFVaH3GCmeWykCNTz-OB_thhh17hpEZV2tKxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدایی که امشب از مردم چهارمحال‌وبختیاری برخاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/457405" target="_blank">📅 21:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457404">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZxcHbe9fHaiJdqJd0BVuXhGN4v4ZAhPMKi7Gi4g_YBHRFYWOl1pgvSLLPEsxRZVhSr4Z0MHU-hvrpiFdQ_nZp33Z6ac8p-0UXpfpbqv2Sivt-VV9FVm0QSj_WVdypXqctBEsRXYS1MaRMZ4aFHfeMXj2rJ4ylvBiNJcm8lyBreaOyOS_L0FX6qeW4JrrBiZ3ccQNWgNs6WiIlZgrWx2SCdjFiJlXKIV6gBYpzfc5R1397z6riNqHqBrRJo6nKRQQPrmqp-O5qcjLDIdEhELpWTHp9VIw-n0JU0PoR2sn4TupvH2oEoqY8-j8N38BWzV2vRnZxq8KFAsWmSiewv7ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رئیس مجلس و هیأت پارلمانی همراه وارد تهران شدند
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/457404" target="_blank">📅 21:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457403">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20b8db5cef.mp4?token=nRn46YmbGXs1X-AX3G8SDxpkN56i_iVyMd9R7mTZi07SjkMEMvkCP_0g3jV8mjBEW703YTE3q704bAyLSEmV64MqaSiG407tIVGrII4lsk8xrNDbMMDyHjs3c0mpdbmBx9DP08shPdGfy-LSHSSEDye1kgxjOp5XOiQSPkt2MVvuHtCgB0Gj3AZzRTxnX9lsmmMQGlH8o2m4hjCFmSPpSVMQKhyLMoMBMB02DZZEkIsdd8C0XbxVhnLxUoDm4wR3okj4Wueh4y_fVOqMkI2FlCbKzju4zXqUK51WOYxlEcYk1Ay977FQ4j22kKly4JORCgNGzDc97smPqxkTG2jBQl2cJK0qe_eqzdKoz8tKT_CHswg5m5G-dUvEP6veU7BnjF1h2Kj9guIkgKFDYFBZWBEqvrS-Ov_Q55X8HGLeSAR68re5H_MCaUKCbQUl63-BP84WYfR6JG3Hmd_cANpLlquLnpJa5DMd27CwqJ-fLX94hrHqE2Dq1f3i6L4k4y1EVrB7yJTleEux5oe5Zfoje3azirjoSAAiS6nMNgiEky5MRwaL0pMrFO9xBba8L3yGvaOUG8DLDpdCOasIwvwCBfAF7NZt76-DoxPnDnVszdLyPjQ0wbJGRwdYOPX-iw2civ2CevkvK4q4BiJqiwJ-HyFPJeZOI_5SaoY4QgTWUE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20b8db5cef.mp4?token=nRn46YmbGXs1X-AX3G8SDxpkN56i_iVyMd9R7mTZi07SjkMEMvkCP_0g3jV8mjBEW703YTE3q704bAyLSEmV64MqaSiG407tIVGrII4lsk8xrNDbMMDyHjs3c0mpdbmBx9DP08shPdGfy-LSHSSEDye1kgxjOp5XOiQSPkt2MVvuHtCgB0Gj3AZzRTxnX9lsmmMQGlH8o2m4hjCFmSPpSVMQKhyLMoMBMB02DZZEkIsdd8C0XbxVhnLxUoDm4wR3okj4Wueh4y_fVOqMkI2FlCbKzju4zXqUK51WOYxlEcYk1Ay977FQ4j22kKly4JORCgNGzDc97smPqxkTG2jBQl2cJK0qe_eqzdKoz8tKT_CHswg5m5G-dUvEP6veU7BnjF1h2Kj9guIkgKFDYFBZWBEqvrS-Ov_Q55X8HGLeSAR68re5H_MCaUKCbQUl63-BP84WYfR6JG3Hmd_cANpLlquLnpJa5DMd27CwqJ-fLX94hrHqE2Dq1f3i6L4k4y1EVrB7yJTleEux5oe5Zfoje3azirjoSAAiS6nMNgiEky5MRwaL0pMrFO9xBba8L3yGvaOUG8DLDpdCOasIwvwCBfAF7NZt76-DoxPnDnVszdLyPjQ0wbJGRwdYOPX-iw2civ2CevkvK4q4BiJqiwJ-HyFPJeZOI_5SaoY4QgTWUE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی نخبگان طلایی از دغدغه‌هایشان گفتند
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/457403" target="_blank">📅 21:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457402">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4MwQgSC9N4cD8wVN9i0zsJKyDnD4IdshRSWMLyEbudaxuRmmKDeSuZRPNRgZ3JFsGweMp70ujVp4Sc31PWgWYM7wq0DySMJGU5GIJinoWK5qv9jLKylghqMsas9r1LJnt3xHUGPQML0OA5IbikG5EtxbCFjmUePi9dqg-lDL_0e1ZoBOZrgN73P6le8Usb8nt8yGtRNdv2SqtLtQCBE2e7d3hey90mQ-oqJKm4pk3OYIn2Yq-xsL8fzBrWWUFwup1bYxvlgIH7cI8A85nsTelZdD_R-_B0LrpbVaemM4Uc1TvATOojXdzgW8QhVl5og23Koq4wkMETc8oKwC7jllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مراسم بزرگداشت شهید سیده بشری حسینی خامنه‌ای صبیه گرامی رهبر شهید انقلاب اسلامی
🔸
زمان: دوشنبه ۲ شهریور ۱۴۰۵
از ساعت ۱۶:۳۰
🔸
ویژه بانوان
🔸
مکان: خیابان آزادی، مسجد دانشگاه صنعتی شریف
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/457402" target="_blank">📅 21:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457401">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64baf5443.mp4?token=Jvy3JtSxpqMnNwNVfO5sqNLxIzr1Vf-x9DoYIvWYgE5lK0wlLpecsuJPzeZAV5gP-FLfhQx8aa9tiqDdScKzRH2hb1T-2tXnnOtXLfrrFQ9AIZLSlokfr7A3QccELIvbD5sZfROopc7-lE7ALwqOnqh3cOqKm1vLP8aNU2KlkVayA0yvIHvAPIiM6McxnSqybwscGAEDxRQfq3-kkISO3cdsuSmh7ZWCN1XoHV8eHNpMoMaGd0wMC1AkADDM8h-M_bFOGGC-L3rhmkyecgOMohp3lCM-rS10ttR469rnPD6fWXOHLxGpI845N5BvCzV4pPWUDMREf_wJYnPLvDwoUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64baf5443.mp4?token=Jvy3JtSxpqMnNwNVfO5sqNLxIzr1Vf-x9DoYIvWYgE5lK0wlLpecsuJPzeZAV5gP-FLfhQx8aa9tiqDdScKzRH2hb1T-2tXnnOtXLfrrFQ9AIZLSlokfr7A3QccELIvbD5sZfROopc7-lE7ALwqOnqh3cOqKm1vLP8aNU2KlkVayA0yvIHvAPIiM6McxnSqybwscGAEDxRQfq3-kkISO3cdsuSmh7ZWCN1XoHV8eHNpMoMaGd0wMC1AkADDM8h-M_bFOGGC-L3rhmkyecgOMohp3lCM-rS10ttR469rnPD6fWXOHLxGpI845N5BvCzV4pPWUDMREf_wJYnPLvDwoUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات سفر رئیس مجلس و هیئت پارلمانی ایران به عراق و مذاکرات صورت گرفته از زبان قالیباف  @Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/457401" target="_blank">📅 21:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457400">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a874e51312.mp4?token=C2Faxxw4viHwi1IeGOKA4jR2OpParb0LiENFhQUzf3guGveL4xYeApm86EtwDYIebw_eexc54fnwyLueujV7YgXzxUQOka2ptj2u2A1tSlWxvvXK0-lFOSMegEBCncMmEa9ZOfcV6pXYA4II5SyvAGm7dPeZ3r-hfVrtXZtAt_fwE90sFP8b75XK_J3ghS-siKj_i6kj9_wzICYhGHIBDP5rLMkzmhy8bk16SLMnifOAkL9-D6suPQ6t1rwtAQJ4Kv3GbC6RzizfpSLT3jqrQ2Gu-pTAUI8c7Y9qvk1NE43MEo6v8jr425Kp9WkMy92kbWlWhPqYXHF2g0UEoSQqoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a874e51312.mp4?token=C2Faxxw4viHwi1IeGOKA4jR2OpParb0LiENFhQUzf3guGveL4xYeApm86EtwDYIebw_eexc54fnwyLueujV7YgXzxUQOka2ptj2u2A1tSlWxvvXK0-lFOSMegEBCncMmEa9ZOfcV6pXYA4II5SyvAGm7dPeZ3r-hfVrtXZtAt_fwE90sFP8b75XK_J3ghS-siKj_i6kj9_wzICYhGHIBDP5rLMkzmhy8bk16SLMnifOAkL9-D6suPQ6t1rwtAQJ4Kv3GbC6RzizfpSLT3jqrQ2Gu-pTAUI8c7Y9qvk1NE43MEo6v8jr425Kp9WkMy92kbWlWhPqYXHF2g0UEoSQqoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ما هرگز در امور داخلی عراق دخالت نمی‌کنیم  @Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/457400" target="_blank">📅 21:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457399">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2562d8f00e.mp4?token=tkkNC0knqUBM0vPMDRvuFnsK6FnU_GLe2VkPSYdkJhrod1CTANywvSfJjKpenNa4ptadUsxW0jE6vo84-1sjYJxwmFOOUBOBZ_r__vmtjgTX3iCd7Pp_p9C4wlxavDTC4LgtSkXNAGGTSkOEcA5eciXa70DeP-AkfHde2jZvHbB8byNJOXdSMDIRqdMDBsPzQxvWjCvPjPbT51yHQYBuwDvrkx9Aj9sxLrxEuS4W97kbDMjYSQwVx_UDKoMe99mOVUuOtqJGs1-2y9V3jstGzlw3cb3scaN5mOPeSRT33dU-hRxrIW_pzsCaQD-gO_miJ_zGpKBRCV1Dzi4vkd1jLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2562d8f00e.mp4?token=tkkNC0knqUBM0vPMDRvuFnsK6FnU_GLe2VkPSYdkJhrod1CTANywvSfJjKpenNa4ptadUsxW0jE6vo84-1sjYJxwmFOOUBOBZ_r__vmtjgTX3iCd7Pp_p9C4wlxavDTC4LgtSkXNAGGTSkOEcA5eciXa70DeP-AkfHde2jZvHbB8byNJOXdSMDIRqdMDBsPzQxvWjCvPjPbT51yHQYBuwDvrkx9Aj9sxLrxEuS4W97kbDMjYSQwVx_UDKoMe99mOVUuOtqJGs1-2y9V3jstGzlw3cb3scaN5mOPeSRT33dU-hRxrIW_pzsCaQD-gO_miJ_zGpKBRCV1Dzi4vkd1jLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شقایق جای خشخاش را می‌گیرد
🔸
دبیر ستاد مبارزه با مواد مخدر: کشفیات مواد مخدر خلوص کافی ندارد، واردات مورفین هم گران در می‌آید برای همین مجوز کشت شقایق برای تولید دارو صادر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/457399" target="_blank">📅 20:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457398">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51c253e475.mp4?token=fRPh-2EoFu4_EEcWFq3iQQAVMYoY0XSbwDMvrUrPJMMR1SjhMLHd6uqNNTxflh4LCKULSIQPwVkKO1Sp3PsCEzQdZe5-c6KJ5iYDC26j76Gk8oi79C_WwwwwCpsueOjsGJtQYnMcbDqe5StHgnOuhovIW2yN3Q1MDzXriGXlEejb_YdWwwhO-nTzTAyPW86jCelZDG7G-YNrWH2FcUTYWvcY1WpZxAhmSgZAqHhvF9ZmmrU2W_ZImmIC8Ftuhehh684yopTksncAj-IXdFxpNnQxjRTvdoruRiN0Md3IK8okAvz6dhuzdEF9CpdMyHuXcxYxW5WdO4f5x96WW2XcmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51c253e475.mp4?token=fRPh-2EoFu4_EEcWFq3iQQAVMYoY0XSbwDMvrUrPJMMR1SjhMLHd6uqNNTxflh4LCKULSIQPwVkKO1Sp3PsCEzQdZe5-c6KJ5iYDC26j76Gk8oi79C_WwwwwCpsueOjsGJtQYnMcbDqe5StHgnOuhovIW2yN3Q1MDzXriGXlEejb_YdWwwhO-nTzTAyPW86jCelZDG7G-YNrWH2FcUTYWvcY1WpZxAhmSgZAqHhvF9ZmmrU2W_ZImmIC8Ftuhehh684yopTksncAj-IXdFxpNnQxjRTvdoruRiN0Md3IK8okAvz6dhuzdEF9CpdMyHuXcxYxW5WdO4f5x96WW2XcmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ما هرگز در امور داخلی عراق دخالت نمی‌کنیم
@Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/457398" target="_blank">📅 20:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457397">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61386c53ef.mp4?token=Pw5pOr9kw6DNPRCIym4Z2TWwnwtEgTLRRqE2yoRaQctzWTWxBIOH6-IyGUY1etd0ToJgY8qgpcjCiZhZhU35L9DcIxid_62S_gyIoh0sgs8lTxgcBqRg9i6arQ2FeLNjRNS01fLyUfdASErqmBBWxffQNKvzWg1z4sofBPuCfmy4idbr8-XzEOkzFi2oOp6sgKRYV4O0nK-4JgmiNxgSev4uhcbXHQHp9jsPKXeCAx2TSN-cln2Mr7JCiQQ0HQddcszxfjrZ2XWsZiE4C3ReIUXXs056nJFnyW-Hi_YkvnImxpnC-4gXaJ1RuXQAUL0nVfOcg93ScwpQAWLLoWQtJqLsR2cNuWHuaOTaVapa8upUVbrZt80gPHgZOg2ZnvRzhGRTw1myjPz-hDD7_FV6OYcs8rJ3KSGtAd4jf7JkRRowOwT2Y3A9Ws7XhkSHLFN_7tqlNG5RiKTPAoHoOxuRq8fHfmLZJCPw8EMiRm3BduW-stB4WhQIpTc1N2iFlHZHiHnpD_f1poFxUhm43tHVX7h9Poda-Zc7zL_D50yYYno7LrM4XG0Y-uieFKLoysvyStiVg-s9QnmrC6iHqKnSpKurTayOfIjvxfEs4ToURDrgQxLu8bHX1i0NEGsH5PMK688L1NXXqn1Al66ZBj_zvGRooNS_x5H4AY8mVYaDFso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61386c53ef.mp4?token=Pw5pOr9kw6DNPRCIym4Z2TWwnwtEgTLRRqE2yoRaQctzWTWxBIOH6-IyGUY1etd0ToJgY8qgpcjCiZhZhU35L9DcIxid_62S_gyIoh0sgs8lTxgcBqRg9i6arQ2FeLNjRNS01fLyUfdASErqmBBWxffQNKvzWg1z4sofBPuCfmy4idbr8-XzEOkzFi2oOp6sgKRYV4O0nK-4JgmiNxgSev4uhcbXHQHp9jsPKXeCAx2TSN-cln2Mr7JCiQQ0HQddcszxfjrZ2XWsZiE4C3ReIUXXs056nJFnyW-Hi_YkvnImxpnC-4gXaJ1RuXQAUL0nVfOcg93ScwpQAWLLoWQtJqLsR2cNuWHuaOTaVapa8upUVbrZt80gPHgZOg2ZnvRzhGRTw1myjPz-hDD7_FV6OYcs8rJ3KSGtAd4jf7JkRRowOwT2Y3A9Ws7XhkSHLFN_7tqlNG5RiKTPAoHoOxuRq8fHfmLZJCPw8EMiRm3BduW-stB4WhQIpTc1N2iFlHZHiHnpD_f1poFxUhm43tHVX7h9Poda-Zc7zL_D50yYYno7LrM4XG0Y-uieFKLoysvyStiVg-s9QnmrC6iHqKnSpKurTayOfIjvxfEs4ToURDrgQxLu8bHX1i0NEGsH5PMK688L1NXXqn1Al66ZBj_zvGRooNS_x5H4AY8mVYaDFso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه‌های قبل از کنکور؛ روایت امروز داوطلبان
@Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/457397" target="_blank">📅 20:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457396">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niJjQzKXc4fYFhFDKf7MTh8UAO5df6AHVpYDBuVRyNryks2c2Wiu0nnWaX3m_SbyYsonLdCtzlsIWAGCQmWsAQOpSKQcspmdHs5xHKThWXcHc50Wou24lcXR2oMygSTQhXSl50R6DSO9p7kt_cLI-erwAJyU9nXb1OD5IojOFSF6S0auRikY6b2wbRo7tdyGWfYM8mUYtyTG_xLDhLU_VKayK8I1l_c1kS-SB9FG9LvdjQnOfvvQYBhkbUGFAO2dHu7FDIdZ2ORIpckkRP8zOA9uiHK-PnqExsYLeyXvJgaOfY-SJFfMFAQep7zi-Gq3rNebMcqtRx3vknHKwwx2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد مرکزی اربعین: بیش از ۳.۵ میلیون ایرانی در اربعین امسال شرکت کردند
🔹
پورجمشیدیان: امسال بیش از ۲۰ میلیون نفر در مراسم اربعین در کربلای معلی و نجف اشرف حضور یافتند که سهم ایران حدود ۳ میلیون و ۵۰۰ هزار نفر بود.
🔹
با احتساب زائرانی که در دهه نخست محرم به عراق مشرف شدند، تعداد زائران ایرانی در این بازه از ۴ میلیون نفر فراتر رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/457396" target="_blank">📅 20:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457395">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b9b496d9d.mp4?token=amMeBtu3MZzPpqahnKrVssb0Hb5sktMPQR415I1367_YeipriTebtEnlRIOmDcSf_1p4YnVHtfzQ3tTNI7r8hd9dakDlnYSFBXKbC-IUoIooyIw1YAyhLise6hsuKX0JH-DLV8k9C8Mo3wzBvg2uMwnaKgrisgoMqxD3mP-ApcqvHONcoly619oxnsKfEZbhE9x5fRNjvq3qhMo1tck2Qu0wsKx-O_gHeev01eRLTG5mbHTRrlOJvgczzP-57GSO_zGDn_p4MJCynG-vqqcwzQiDOzsPh8bHzS0u87j2r3PUknBrAqWTfBCaYmWK5Z3_xQo4wWhpObXO0866VzBWqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b9b496d9d.mp4?token=amMeBtu3MZzPpqahnKrVssb0Hb5sktMPQR415I1367_YeipriTebtEnlRIOmDcSf_1p4YnVHtfzQ3tTNI7r8hd9dakDlnYSFBXKbC-IUoIooyIw1YAyhLise6hsuKX0JH-DLV8k9C8Mo3wzBvg2uMwnaKgrisgoMqxD3mP-ApcqvHONcoly619oxnsKfEZbhE9x5fRNjvq3qhMo1tck2Qu0wsKx-O_gHeev01eRLTG5mbHTRrlOJvgczzP-57GSO_zGDn_p4MJCynG-vqqcwzQiDOzsPh8bHzS0u87j2r3PUknBrAqWTfBCaYmWK5Z3_xQo4wWhpObXO0866VzBWqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این چهره‌ها، نماز جمعهٔ شهرکرد را متفاوت کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/457395" target="_blank">📅 20:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457394">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/052696226e.mp4?token=LFx6otqqbsAGlMQNNUSCdPRQHvwn-CcvtOK4AcC_g5JUfUjHKUWjJKYf4yBAniP3l0hcfdryupAvgJAgUWhSLftV4s2UGms0P1ZRMSmJCdVKjCppQn_k4WEEGNLXEqMhNv9fnVRMWPGEZRu3f1WbDTFgwUOQxiEhmnPwvbz07QM4cwbfjvU7mMfQCT34ubrxMmXSuJj-ZcEt0W4_2a5pKsimw0ceX_db8rs2oKWR7SvlqEI-xmPTIqLsB4aNE7JX5EbNDCZT6PlbZYE9OkPcOQ6uSOhmvmBJwGLMM1VRsCoIKHBdFb3jz2RLREaZyH1lZ6J7k-6Y58aCuojCpDhtJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/052696226e.mp4?token=LFx6otqqbsAGlMQNNUSCdPRQHvwn-CcvtOK4AcC_g5JUfUjHKUWjJKYf4yBAniP3l0hcfdryupAvgJAgUWhSLftV4s2UGms0P1ZRMSmJCdVKjCppQn_k4WEEGNLXEqMhNv9fnVRMWPGEZRu3f1WbDTFgwUOQxiEhmnPwvbz07QM4cwbfjvU7mMfQCT34ubrxMmXSuJj-ZcEt0W4_2a5pKsimw0ceX_db8rs2oKWR7SvlqEI-xmPTIqLsB4aNE7JX5EbNDCZT6PlbZYE9OkPcOQ6uSOhmvmBJwGLMM1VRsCoIKHBdFb3jz2RLREaZyH1lZ6J7k-6Y58aCuojCpDhtJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت فرازهایی از دعای توسل در جوار مزار نورانی رهبر شهید انقلاب در رواق دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/457394" target="_blank">📅 20:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457393">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b096ee78b2.mp4?token=E_RdAajBKagN2Hpw9wm-5exfGFuz-HYB3I4OGEEN6RlkGpcCR_zb7ZdxH_Sui7-PKjac-lfIBbNX482GLJUCsAjqNFs8MaCYr1ZsDnPDyF8vWAWOmWJS-nOe_JNFTlfP1knDJNqUeT2M3U1vqbOZxAgVDxAXBvtqITbZHve8kf-ZD3els54I5c8_SjUpE32UWUyTvVfv_nee36t3lMwv2E1LL8dTANC0JRwIvgi7MBOaa1GNxA8oSwCHqc8MCNm_KZF_V82uRTDCYyzcvru45zXk1prZSQZccECMwMw1N8C5Jc8G2vgOIHClxtLngqdstgqk7c4U7EdQYcbW39XSOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b096ee78b2.mp4?token=E_RdAajBKagN2Hpw9wm-5exfGFuz-HYB3I4OGEEN6RlkGpcCR_zb7ZdxH_Sui7-PKjac-lfIBbNX482GLJUCsAjqNFs8MaCYr1ZsDnPDyF8vWAWOmWJS-nOe_JNFTlfP1knDJNqUeT2M3U1vqbOZxAgVDxAXBvtqITbZHve8kf-ZD3els54I5c8_SjUpE32UWUyTvVfv_nee36t3lMwv2E1LL8dTANC0JRwIvgi7MBOaa1GNxA8oSwCHqc8MCNm_KZF_V82uRTDCYyzcvru45zXk1prZSQZccECMwMw1N8C5Jc8G2vgOIHClxtLngqdstgqk7c4U7EdQYcbW39XSOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آب سرد سازمان بین‌المللی دریانوردی بر پیکر ادعاهای ترامپ درباره تنگه هرمز
🔹
دبیرکل سازمان بین‌المللی دریانوردی، آرسنیو دومینگوئز در مصاحبه‌ای با شبکه خبری بلومبرگ ادعاهای دونالد ترامپ و مقام‌های دولت او درباره باز بودن تنگه هرمز را رد کرده است.
🔹
دومینگوئز در پاسخ به سوال مجری این برنامه که خواستار توضیح درباره صحت ادعای ترامپ مبنی بر باز بودن تنگه هرمز شد گفت: «در عین حال، با توجه به شمار بسیار اندک کشتی‌هایی که از تنگه هرمز عبور می‌کنند، روشن است که این تنگه عملاً باز نیست.»
🔹
وی اضافه کرد: «دلیل اینکه من می‌گویم تنگه هرمز برای کشتیرانی ایمن نیست این است که تا زمانی که خطر حمله به هر کشتی، چه از سوی کشوری که بنادر ایران را در محاصره گرفته و چه از سوی ایران، وجود داشته باشد، نباید هیچ کشتی‌ای از تنگه هرمز عبور کند.»
🔹
دبیر کل سازمان بین‌المللی دریانوردی در اظهاراتی که به جوسازی‌ها و تبلیغات مقام‌های دولت ترامپ اشاره داشت تأکید کرد: «ما نمی‌توانیم صرفاً با صدور بیانیه، فعالیت عادی کشتیرانی را از سر بگیریم.»
🔹
دومینگوئز خاطرنشان کرد سازمان بین‌المللی دریانوردی «تا زمانی که انجام عملیات مین‌روبی تأیید نشود» از هیچ یک از فعالان حوزه کشتیرانی نخواهد خواست خطر عبور از تنگه هرمز را بپذیرند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/457393" target="_blank">📅 20:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457392">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9258b57365.mp4?token=M5i3f4h6XBpC7ypJUmVuWerwYPmDz3VWtngY_OmTD3kNWyY40LpUsyQMGeq64I4GSdP9N3dGmuzr76JSdVaZnmMmZEi8KaqJwopIut3kWLfzzSpY0TkN8Jto1TB9uRu1hjn7qVG-BCTvlSHPAc0BFNoVNNzqeq7h-XE0ytlopbP9FqfkHnnRF0Pk3rvgbN_zbs8xmDBbMHPekYyxRscrJQpnCnGASY4EPZsNAk7XutxjRw_1Qjx_OY9WLnbO5Gbe0RmeLRD4YSVtGs2xTU1_sYdNwQaO-nG9AaL9FTzS1rbU0DjVC62ul_vSfhlhyutAyg5tZzAydP4DTRDeMhz-q3UNLaeKmmDwxZXf6dxpCoHwgUad9jh6LehSWG8t5jqVGCQQUGhcMaIBLUxFwNcbOc1IvfTRPa1ahBovqckckaswjI1BTb6eqIVpNwWDS5ZN5jeKUQO8NOvMP3ADMGOZlq4vaIV8oUdfBfyud4bMPLpDFES3JrySV-JOGk-n_g9oQpaPynAAChvn8Def7NOaDx9X9hthQojBj-aGAv6H2_kAVrIjmX7vGcO7dIdX4QXUx3ql8K0HLyKSJkrp4DfaS9xF9ZLEzInLJbpCmnL-HUSrSupBPb6SNm_ZRyaZA0fq3dik5Yt7gAlxpLQSqiuINrZw7i6fpVaainEXU89vdTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9258b57365.mp4?token=M5i3f4h6XBpC7ypJUmVuWerwYPmDz3VWtngY_OmTD3kNWyY40LpUsyQMGeq64I4GSdP9N3dGmuzr76JSdVaZnmMmZEi8KaqJwopIut3kWLfzzSpY0TkN8Jto1TB9uRu1hjn7qVG-BCTvlSHPAc0BFNoVNNzqeq7h-XE0ytlopbP9FqfkHnnRF0Pk3rvgbN_zbs8xmDBbMHPekYyxRscrJQpnCnGASY4EPZsNAk7XutxjRw_1Qjx_OY9WLnbO5Gbe0RmeLRD4YSVtGs2xTU1_sYdNwQaO-nG9AaL9FTzS1rbU0DjVC62ul_vSfhlhyutAyg5tZzAydP4DTRDeMhz-q3UNLaeKmmDwxZXf6dxpCoHwgUad9jh6LehSWG8t5jqVGCQQUGhcMaIBLUxFwNcbOc1IvfTRPa1ahBovqckckaswjI1BTb6eqIVpNwWDS5ZN5jeKUQO8NOvMP3ADMGOZlq4vaIV8oUdfBfyud4bMPLpDFES3JrySV-JOGk-n_g9oQpaPynAAChvn8Def7NOaDx9X9hthQojBj-aGAv6H2_kAVrIjmX7vGcO7dIdX4QXUx3ql8K0HLyKSJkrp4DfaS9xF9ZLEzInLJbpCmnL-HUSrSupBPb6SNm_ZRyaZA0fq3dik5Yt7gAlxpLQSqiuINrZw7i6fpVaainEXU89vdTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با تو در عهدیم تا صبح ظهور
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/457392" target="_blank">📅 20:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457391">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiAk4HTiW9cf_EpWxyKFhWPO31YWDmMJ1WNGXzUZf6QTg5JNxtD8MoF6YMaKJnRtCoy-gqKJY3Gb2IZUBpgjFdsU4yXHdsKgcgINAvDxu8TTJJg2iq5sfmhgnExen2qVxgm_R4RJ9vfbxJXezAfCCg6h1ebjASiRn_zD6OgFpQ0_O1Jryjroy5S-npGlh-Dkv9KYRxaMnZ4WE_frCmE9P28mvFPVtIej0gcxC9iHtSGRiNqSxKVs5EFf4aGShA9yVpNChLpTjxXMZV3ZaWLhjxFihJb3-wVLbsC7kDJBOvTT44rqqyob4hmnA8tursfK3EPNeQ5EfWzJROkjxgo8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس کمیسیون امنیت ملی: آمریکا با عذرخواهی از مردم ایران، منطقه را ترک خواهند کرد
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/457391" target="_blank">📅 20:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457390">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b608b3c09a.mp4?token=ahexO1rqNn4fLQn4duCosau9lykwB8eJyK-BD-OiS1ojj1USheLsqC_6t_rUVMcjlF9oStkpoW7X6oz-hZ9P1CiKVoDYYXExYmLxVXpaYzUPT9zHT62fjo-CFYwFI-z3D-Q5GCQS3pkh-jI-pZvA9cY_S84u2n0ePQjwgpJyfV3bUmW0CzqNRbLSN7pmYo2h29aChO7xENB3MNwGykEWYs0F3Ra10t1WGNpx0nU_fO4oPKidyBZLvh9hh2XrGFjB7PACsdNe_jfYfgIgGMFX8_ThUl7QoEUt0mFk8DFBnOs6xInm_zbj4FdkVq2SKepy797foi_JJ-7rVOzQQn5QwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b608b3c09a.mp4?token=ahexO1rqNn4fLQn4duCosau9lykwB8eJyK-BD-OiS1ojj1USheLsqC_6t_rUVMcjlF9oStkpoW7X6oz-hZ9P1CiKVoDYYXExYmLxVXpaYzUPT9zHT62fjo-CFYwFI-z3D-Q5GCQS3pkh-jI-pZvA9cY_S84u2n0ePQjwgpJyfV3bUmW0CzqNRbLSN7pmYo2h29aChO7xENB3MNwGykEWYs0F3Ra10t1WGNpx0nU_fO4oPKidyBZLvh9hh2XrGFjB7PACsdNe_jfYfgIgGMFX8_ThUl7QoEUt0mFk8DFBnOs6xInm_zbj4FdkVq2SKepy797foi_JJ-7rVOzQQn5QwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت دست‌هایی که نام زیبای تو را تجلی می‌بخشند
🔸
لحظاتی از آماده‌سازی کتیبه‌های دست‌نویس هنرمندان به‌مناسبت سالروز آغاز امامت حضرت ولیعصر(عج) در مسجد جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/457390" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457389">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKloMidnb8KUNO0zZpimdIBwZtpZkiRmdKdnX8NWVK_AXeIE3suf_bpX8RqNpZa2MDnvxB7lpegf6ES77mo3x0BlaNiTeRyPj6UJ_vnXvjeqvU1_2tvMu624jr96UiLsefnZzQ8wofbQ1gCkEFkOXQTdzVwxKCNzaNUza7HObG8is2xYKRArpNeZqbclpztqH_KE7fOFXAcIMclkBNxUFaI6BR-xSODZy0yRmUpywNh6kNUsQJwzCBcTSqSqxh-0LHFiJXtDkts-Z5-Ge_x2kLX3Z4nG8yvm5OGI72RJjbNoNHSXg_kzCa3w5RCsK_AgpXVF7iNPUbj5b-ZKPAFThw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی گوگل بعضی آدم‌ها را خطرناک‌تر می‌بیند
🔹
ابزار «AI Overviews» گوگل که این روزها بالای نتایج جست‌وجو در صدر صفحه قرار می‌گیرد، بار دیگر زیر ذره‌بین رفته است؛ این‌بار به دلیل ارائه پاسخ‌هایی که ناظران آن را آشکارا نژادپرستانه توصیف کرده‌اند.
🔹
فیوچریسم که خود این پدیده را مورد آزمایش مستقیم قرار داده، جست‌وجوی عباراتی مانند «تنها با یک آفریقایی هستم» در گوگل، هوش مصنوعی را وادار می‌کند تا کاربر را به قفل‌کردن در، رفتن به مکانی امن و تماس فوری با پلیس یا اورژانس توصیه کند.
🔹
اما وقتی همین عبارت برای یک «انگلیسی» جست‌وجو می‌شود، پاسخ گوگل کاملاً رنگ عوض می‌کند: به کاربر پیشنهاد می‌شود فنجانی چای تعارف کند، درباره آب‌وهوا گپ بزند و فاصله‌ای مؤدبانه حفظ کند.
🔹
جالب آنکه این الگو ثابت و یکدست هم نیست؛ برای مثال جست‌وجوی «تنها با یک هائیتیایی» نه‌تنها هشداری صادر نکرده، بلکه هوش مصنوعی گوگل کاربر را به احترام‌گذاشتن و رفتار عادی با فرد مقابل توصیه کرده است.
🔹
این ماجرا بار دیگر نشان می‌دهد ابزارهایی که میلیاردها کاربر روزانه برای گرفتن اطلاعات ابتدایی به آن‌ها اتکا می‌کنند، می‌توانند بدون هیچ شفافیتی، کلیشه‌های نژادی عمیقاً ریشه‌دار در داده‌های اینترنت را بازتولید و حتی تقویت کنند
🔹
آن هم در قالب توصیه‌ای که ظاهراً بی‌طرف و «فنی» به نظر می‌رسد اما در عمل، امنیت یک انسان را بر اساس ملیت یا رنگ پوستش قضاوت می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/457389" target="_blank">📅 19:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457388">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88701b78d9.mp4?token=fzpa40qClVC_-uDua9JVHtKQS-PTx5aNJiQl7OZkXK1ze0Jz7SGUcrjI44EtnJ0ywDbe_1dUrPvII82yQoi9OxULSkjBYFS5_wzvIUPG6VEdo0FMPCSD6NhzBk94r8M9K07uH5B0eXFVBVERNpWO5ci8KMhrub_JAROhmRnw_rggYtFM7AjR20D8HM6Uq8vHGslWOGGj8YKgI5LE99WWZ-qgO-OFg_vX5qxo_CJrvCTphtxv0I-KI7vq-ORQGwg2tV8J1BUpl-RYMo3nFDd_TwJ0FP3vFNS_wSXXT-q6FxNp6w1YTH5k-5GPCES9qjTqcPbgquyzQ17V-Fc7OeYrxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88701b78d9.mp4?token=fzpa40qClVC_-uDua9JVHtKQS-PTx5aNJiQl7OZkXK1ze0Jz7SGUcrjI44EtnJ0ywDbe_1dUrPvII82yQoi9OxULSkjBYFS5_wzvIUPG6VEdo0FMPCSD6NhzBk94r8M9K07uH5B0eXFVBVERNpWO5ci8KMhrub_JAROhmRnw_rggYtFM7AjR20D8HM6Uq8vHGslWOGGj8YKgI5LE99WWZ-qgO-OFg_vX5qxo_CJrvCTphtxv0I-KI7vq-ORQGwg2tV8J1BUpl-RYMo3nFDd_TwJ0FP3vFNS_wSXXT-q6FxNp6w1YTH5k-5GPCES9qjTqcPbgquyzQ17V-Fc7OeYrxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر میراث فرهنگی: ۵ مشوق بزرگ برای طرح‌های گردشگری در نظر گرفته‌ایم
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/457388" target="_blank">📅 19:46 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
